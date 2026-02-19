#!/usr/bin/env python3
"""
X (Twitter) posts fetcher via local RSSHub instance.
Saves daily posts to X_posts/YYYY-MM-DD/{company}.md.
Deduplicates based on tweet URL to avoid writing the same post twice.
"""

import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser

RSSHUB_URL = "http://localhost:1200"
REPO_DIR = "/Users/s18675/Desktop/I-am-S-2"
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


def fetch_posts(handle):
    """Fetch posts for a Twitter handle from local RSSHub (JSON Feed format)."""
    url = f"{RSSHUB_URL}/twitter/user/{handle}?format=json&limit=40"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "I-am-S-2/1.0"})
        resp = urllib.request.urlopen(req, timeout=60)
        data = json.loads(resp.read().decode())
        return data.get("items", [])
    except Exception as e:
        print(f"    Warning: Failed to fetch @{handle}: {e}", file=sys.stderr)
        return []


def get_existing_urls(filepath):
    """Extract all tweet URLs already present in a file to prevent duplicates."""
    urls = set()
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
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
    # Try RFC 2822 style: "Thu, 20 Feb 2026 01:23:45 GMT"
    try:
        from email.utils import parsedate_to_datetime
        return parsedate_to_datetime(date_str)
    except Exception:
        return None


def main():
    now = datetime.now(JST)
    today = now.strftime("%Y-%m-%d")
    today_dir = os.path.join(X_POSTS_DIR, today)
    os.makedirs(today_dir, exist_ok=True)

    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S JST')}] X posts fetch starting")

    if not check_internet():
        print("No internet connection. Skipping.")
        sys.exit(0)

    # Wait for RSSHub to be ready (may still be booting)
    import time
    MAX_WAIT = 120  # seconds
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

    total_new = 0
    total_skipped = 0

    for company_key, company_data in PERSONS.items():
        label = company_data["label"]
        accounts = company_data["accounts"]
        filepath = os.path.join(today_dir, f"{company_key}.md")

        existing_urls = get_existing_urls(filepath)

        # Create file with header if it doesn't exist
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {label} X投稿 - {today}\n\n")
                f.write(f"収集元: ローカルRSSHub (localhost:1200)\n\n---\n\n")

        company_new = 0

        for person in accounts:
            handle = person["handle"]
            name = person["name"]
            role = person["role"]

            print(f"  [{label}] @{handle} ({name})...", end=" ")
            items = fetch_posts(handle)

            new_posts = []
            for item in items:
                # Get URL and normalize
                url = item.get("url", "") or item.get("link", "")
                url = url.replace("twitter.com", "x.com")

                if not url or url in existing_urls:
                    continue

                # Filter to today's posts only (JST)
                date_str = item.get("date_published", "") or item.get("pubDate", "")
                post_date = parse_date(date_str)
                if post_date:
                    post_jst = post_date.astimezone(JST)
                    if post_jst.strftime("%Y-%m-%d") != today:
                        total_skipped += 1
                        continue
                    time_str = post_jst.strftime("%H:%M JST")
                else:
                    time_str = "時刻不明"

                # Extract content
                content = strip_html(
                    item.get("content_html", "") or item.get("description", "")
                )
                title = (item.get("title", "") or "").strip()
                display_text = content if content else title
                if not display_text:
                    continue

                # Truncate extremely long posts
                if len(display_text) > 1500:
                    display_text = display_text[:1500] + "...(truncated)"

                new_posts.append({
                    "url": url,
                    "time": time_str,
                    "text": display_text,
                })
                existing_urls.add(url)

            if new_posts:
                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(f"## @{handle} ({name} - {role})\n\n")
                    for post in new_posts:
                        # Quote each line for markdown blockquote
                        quoted = "\n> ".join(post["text"].split("\n"))
                        f.write(f"**{post['time']}** | [原文]({post['url']})\n\n")
                        f.write(f"> {quoted}\n\n---\n\n")
                company_new += len(new_posts)
                print(f"+{len(new_posts)} posts")
            else:
                print("no new")

        total_new += company_new

    print(f"\nSummary: {total_new} new posts, {total_skipped} skipped (not today)")

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
            subprocess.run(
                ["git", "commit", "-m", f"X posts: {today} (+{total_new} posts)"],
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
            print("Synced with remote (no new posts).")
    else:
        print(f"Push failed: {push.stderr}")

    print(f"[{datetime.now(JST).strftime('%H:%M:%S JST')}] Done.")


if __name__ == "__main__":
    main()
