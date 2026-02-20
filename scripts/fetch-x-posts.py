#!/usr/bin/env python3
"""
X (Twitter) posts fetcher via local RSSHub instance.
Saves posts to X_posts/YYYY-MM-DD/{company}.md filed by actual post date.
Deduplicates based on tweet URL to avoid writing the same post twice.
"""

import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import urllib.error
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser

RSSHUB_URL = "http://localhost:1200"
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
X_POSTS_DIR = os.path.join(REPO_DIR, "X_posts")
JST = timezone(timedelta(hours=9))

PERSONS = {
    "anthropic": {
        "label": "Anthropic",
        "accounts": [
            {"handle": "AnthropicAI", "name": "Anthropic", "role": "公式アカウント"},
            {"handle": "jackclarkSF", "name": "Jack Clark", "role": "共同創業者 / Policy"},
            {"handle": "AmandaAskell", "name": "Amanda Askell", "role": "Claudeの人格設計研究者"},
            {"handle": "janleike", "name": "Jan Leike", "role": "Alignment Scienceリーダー"},
            {"handle": "sleepinyourhat", "name": "Sam Bowman", "role": "技術安全性"},
            {"handle": "EthanJPerez", "name": "Ethan Perez", "role": "Research scientist"},
            {"handle": "dpkingma", "name": "Durk Kingma", "role": "研究者"},
        ],
    },
    "openai": {
        "label": "OpenAI",
        "accounts": [
            {"handle": "OpenAIDevs", "name": "OpenAI Developers", "role": "公式開発者アカウント"},
            {"handle": "sama", "name": "Sam Altman", "role": "CEO"},
            {"handle": "gdb", "name": "Greg Brockman", "role": "共同創業者"},
            {"handle": "kevinweil", "name": "Kevin Weil", "role": "製品責任者"},
            {"handle": "markchen90", "name": "Mark Chen", "role": "研究責任者"},
            {"handle": "bradlightcap", "name": "Brad Lightcap", "role": "業務執行"},
            {"handle": "jasonkwon", "name": "Jason Kwon", "role": "戦略担当"},
            {"handle": "woj_zaremba", "name": "Wojciech Zaremba", "role": "共同創業者"},
            {"handle": "npew", "name": "Peter Welinder", "role": "研究・技術"},
            {"handle": "polynoamial", "name": "Noam Brown", "role": "研究者"},
            {"handle": "prafdhar", "name": "Prafulla Dhariwal", "role": "研究者"},
        ],
    },
    "google-deepmind": {
        "label": "Google DeepMind",
        "accounts": [
            {"handle": "GoogleDeepMind", "name": "Google DeepMind", "role": "公式アカウント"},
            {"handle": "demishassabis", "name": "Demis Hassabis", "role": "共同創業者・CEO"},
            {"handle": "jeffdean", "name": "Jeff Dean", "role": "AI研究中心人物"},
            {"handle": "oriolvinyalsml", "name": "Oriol Vinyals", "role": "研究リーダー"},
            {"handle": "pushmeet", "name": "Pushmeet Kohli", "role": "研究リーダー"},
            {"handle": "OfficialLoganK", "name": "Logan Kilpatrick", "role": "AI Studio / Gemini API"},
            {"handle": "joshwoodward", "name": "Josh Woodward", "role": "Geminiアプリ / AI Studio"},
            {"handle": "sundarpichai", "name": "Sundar Pichai", "role": "Google CEO"},
            {"handle": "rosterloh", "name": "Rick Osterloh", "role": "Devices & Services責任者"},
            {"handle": "lockheimer", "name": "Hiroshi Lockheimer", "role": "Android/Chrome責任者"},
            {"handle": "thomasortk", "name": "Thomas Kurian", "role": "Google Cloud CEO"},
        ],
    },
}


class HTMLStripper(HTMLParser):
    """Strip HTML tags and return plain text."""
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip = True
        elif tag == "br":
            self.result.append("\n")
        elif tag == "p":
            self.result.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            self.result.append(data)

    def get_text(self):
        return re.sub(r'\n{3,}', '\n\n', ''.join(self.result)).strip()


def strip_html(html):
    if not html:
        return ""
    s = HTMLStripper()
    s.feed(html)
    return s.get_text()


def check_rsshub():
    try:
        resp = urllib.request.urlopen(f"{RSSHUB_URL}/healthz", timeout=5)
        return resp.read().decode().strip() == "ok"
    except Exception:
        return False


def check_internet():
    try:
        urllib.request.urlopen("https://x.com", timeout=10)
        return True
    except Exception:
        return False


def fetch_posts(handle, max_retries=2):
    """Fetch posts for a Twitter handle from local RSSHub (JSON Feed format).
    Retries on failure with backoff. Long timeout to accommodate slow Twitter API."""
    url = f"{RSSHUB_URL}/twitter/user/{handle}?format=json&limit=40"
    for attempt in range(max_retries + 1):
        try:
            t0 = time.monotonic()
            req = urllib.request.Request(url, headers={"User-Agent": "I-am-S-2/1.0"})
            resp = urllib.request.urlopen(req, timeout=180)
            data = json.loads(resp.read().decode())
            elapsed = time.monotonic() - t0
            items = data.get("items", [])
            print(f"{len(items)} items ({elapsed:.0f}s)", end=" ")
            return items
        except Exception as e:
            elapsed = time.monotonic() - t0 if 't0' in dir() else 0
            if attempt < max_retries:
                wait = 10 * (attempt + 1)
                print(f"err({elapsed:.0f}s), retry in {wait}s...", end=" ")
                time.sleep(wait)
            else:
                print(f"FAILED({e})", end=" ", file=sys.stderr)
                return []


def load_all_known_urls():
    """Load all tweet URLs from all existing X_posts date directories."""
    urls = set()
    if not os.path.exists(X_POSTS_DIR):
        return urls
    for date_dir in os.listdir(X_POSTS_DIR):
        dir_path = os.path.join(X_POSTS_DIR, date_dir)
        if not os.path.isdir(dir_path) or not re.match(r'\d{4}-\d{2}-\d{2}', date_dir):
            continue
        for fname in os.listdir(dir_path):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dir_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                for line in f:
                    matches = re.findall(
                        r'https://(?:x\.com|twitter\.com)/\S+/status/\d+', line
                    )
                    urls.update(m.split(")")[0].split("]")[0] for m in matches)
    return urls


def parse_date(date_str):
    """Parse ISO 8601 or RFC 2822 date string."""
    if not date_str:
        return None
    try:
        date_str = date_str.replace("Z", "+00:00")
        return datetime.fromisoformat(date_str)
    except Exception:
        pass
    try:
        from email.utils import parsedate_to_datetime
        return parsedate_to_datetime(date_str)
    except Exception:
        return None


def ensure_date_file(date_str, company_key, label):
    """Ensure a date directory and company file exist, return filepath."""
    date_dir = os.path.join(X_POSTS_DIR, date_str)
    os.makedirs(date_dir, exist_ok=True)
    filepath = os.path.join(date_dir, f"{company_key}.md")
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {label} X投稿 - {date_str}\n\n")
            f.write(f"収集元: ローカルRSSHub (localhost:1200)\n\n---\n\n")
    return filepath


def main():
    now = datetime.now(JST)
    today = now.strftime("%Y-%m-%d")

    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S JST')}] X posts fetch starting")

    if not check_internet():
        print("No internet connection. Skipping.")
        sys.exit(0)

    # Wait for RSSHub to be ready (may still be booting)
    MAX_WAIT = 120
    INTERVAL = 5
    waited = 0
    while not check_rsshub():
        if waited >= MAX_WAIT:
            print(f"RSSHub not ready after {MAX_WAIT}s. Skipping.")
            sys.exit(0)
        print(f"  Waiting for RSSHub... ({waited}s/{MAX_WAIT}s)")
        time.sleep(INTERVAL)
        waited += INTERVAL
    if waited > 0:
        print(f"  RSSHub ready after {waited}s.")

    # Load all known URLs across all dates for global dedup
    known_urls = load_all_known_urls()
    print(f"  Known URLs: {len(known_urls)}")

    total_new = 0
    # Collect posts grouped by (date, company_key) for batched writing
    # Structure: {(date_str, company_key): [(handle, name, role, posts_list)]}
    date_company_posts = defaultdict(list)

    for company_key, company_data in PERSONS.items():
        label = company_data["label"]
        accounts = company_data["accounts"]

        for person in accounts:
            handle = person["handle"]
            name = person["name"]
            role = person["role"]

            print(f"  [{label}] @{handle} ({name})...", end=" ")
            items = fetch_posts(handle)

            person_posts_by_date = defaultdict(list)
            for item in items:
                url = item.get("url", "") or item.get("link", "")
                url = url.replace("twitter.com", "x.com")

                if not url or url in known_urls:
                    continue

                # Determine post date (JST)
                date_str = item.get("date_published", "") or item.get("pubDate", "")
                post_date = parse_date(date_str)
                if post_date:
                    post_jst = post_date.astimezone(JST)
                    post_date_str = post_jst.strftime("%Y-%m-%d")
                    time_str = post_jst.strftime("%H:%M JST")
                else:
                    # Unknown date -> file under today
                    post_date_str = today
                    time_str = "時刻不明"

                content = strip_html(
                    item.get("content_html", "") or item.get("description", "")
                )
                title = (item.get("title", "") or "").strip()
                display_text = content if content else title
                if not display_text:
                    continue

                if len(display_text) > 1500:
                    display_text = display_text[:1500] + "...(truncated)"

                person_posts_by_date[post_date_str].append({
                    "url": url,
                    "time": time_str,
                    "text": display_text,
                })
                known_urls.add(url)

            person_total = sum(len(v) for v in person_posts_by_date.values())
            if person_total > 0:
                dates_summary = ", ".join(
                    f"{d}:{len(ps)}" for d, ps in sorted(person_posts_by_date.items())
                )
                print(f"-> +{person_total} ({dates_summary})")
                for date_str, posts in person_posts_by_date.items():
                    date_company_posts[(date_str, company_key)].append(
                        (handle, name, role, posts)
                    )
                total_new += person_total
            else:
                print("-> no new")

    # Write all collected posts to their respective date/company files
    dates_touched = set()
    for (date_str, company_key), person_entries in sorted(date_company_posts.items()):
        label = PERSONS[company_key]["label"]
        filepath = ensure_date_file(date_str, company_key, label)
        dates_touched.add(date_str)

        with open(filepath, "a", encoding="utf-8") as f:
            for handle, name, role, posts in person_entries:
                f.write(f"## @{handle} ({name} - {role})\n\n")
                for post in posts:
                    quoted = "\n> ".join(post["text"].split("\n"))
                    f.write(f"**{post['time']}** | [原文]({post['url']})\n\n")
                    f.write(f"> {quoted}\n\n---\n\n")

    if dates_touched:
        print(f"\nDates updated: {', '.join(sorted(dates_touched))}")
    print(f"Summary: {total_new} new posts across {len(dates_touched)} dates")

    # Git sync & commit
    os.chdir(REPO_DIR)

    # Always pull remote first (Actions may have pushed)
    pull = subprocess.run(
        ["git", "pull", "--rebase", "--autostash"],
        capture_output=True, text=True,
    )
    if pull.returncode != 0:
        print(f"Pull --rebase failed, trying merge: {pull.stderr}")
        subprocess.run(["git", "rebase", "--abort"], capture_output=True)
        subprocess.run(
            ["git", "pull", "--no-rebase", "--autostash"],
            capture_output=True,
        )

    if total_new > 0:
        subprocess.run(["git", "add", "X_posts/"], check=False)
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"], capture_output=True
        )
        if diff.returncode != 0:
            dates_label = ", ".join(sorted(dates_touched))
            subprocess.run(
                ["git", "commit", "-m",
                 f"X posts: +{total_new} posts ({dates_label})"],
                check=False,
            )

    # Always try to push (covers both new posts and synced state)
    push = subprocess.run(
        ["git", "push"], capture_output=True, text=True,
    )
    if push.returncode == 0:
        if total_new > 0:
            print("Committed and pushed.")
        else:
            print("Synced with remote.")
    else:
        print(f"Push failed: {push.stderr}")

    print(f"[{datetime.now(JST).strftime('%H:%M:%S JST')}] Done.")


if __name__ == "__main__":
    main()
