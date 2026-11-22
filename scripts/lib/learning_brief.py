"""Compact reading views over accepted intelligence records."""

import html
import posixpath
import re
from urllib.parse import urlparse


def short_sentence(value, limit=185):
    """Return a complete sentence, or leave lengthy material in the detail."""
    line = value.strip().partition("\n")[0]
    pairs = ("()", "（）", "「」", "『』", "【】")
    for boundary in re.finditer(r"。|[.!?](?=\s)|$", line):
        end = boundary.end()
        if end > limit:
            break
        sentence = line[:end]
        if sentence and all(sentence.count(left) == sentence.count(right) for left, right in pairs):
            return re.sub(r"([\\\[\]*_`])", r"\\\1", html.escape(sentence, quote=False))
    return ""


def evidence_headline(summary, feed):
    first, stop, rest = summary.partition("。")
    if feed and stop and ("公開されたことを確認" in first or "掲載を確認" in first):
        description = re.match(r"\s*説明文は「([^」\n]{1,120})」", rest)
        if description:
            return short_sentence(f"説明文では「{description[1]}」と記載。")
        title = re.search(r"「[^」\n]{4,110}」", first)
        if title:
            return short_sentence(f"{title.group()}の掲載を確認。")
    return short_sentence(summary)


def is_feed(url):
    path = urlparse(url).path.lower()
    return "rss" in path or "atom" in path or path.endswith(("/feed", "/feed.xml"))


def relative_link(label, source_dir, target, anchor=""):
    return f"[{label}]({posixpath.relpath(target, source_dir)}{anchor})"


def highlight_lines(new, detail, detail_text, claim_labels, local_date):
    if not new:
        return ["今回、新たに採用した資料はありません。"]
    lines = []
    ordered = sorted(new, key=lambda row: "Demos分類" in row["summary"])
    for row in ordered[:3]:
        host = urlparse(row["url"]).hostname
        feed = is_feed(row["url"])
        kind = "公式フィードで確認" if feed else claim_labels[row["claim_type"]]
        if feed and row["claim_type"] == "reported_claim":
            kind = "公式フィードに掲載された説明"
        summary = evidence_headline(row["summary"], feed)
        anchor = f'evidence-{row["id"]}'
        link = detail + (f"#{anchor}" if f'name="{anchor}"' in detail_text else "")
        date = local_date(row["published_at"])
        context = "・公式フィードの記載" if feed else ""
        lines += [f"**{kind}**　{summary}" if summary else f"**{host}の資料を採用**", "",
                  f"公開日 {date}・{host}{context} · [採用記録]({link})", ""]
    return lines


def prior_sections(records, changes, date, local_date, limit=2):
    sections = records["dossier_section"]
    previous = [sections[row["supersedes"]] for row in changes if row["supersedes"] in sections]
    for row in changes:
        cited = re.findall(r"[A-Za-z0-9_@.:-]+", row["analysis"])
        previous.extend(sections[key] for key in cited if key in sections)
    if not previous:
        recent = sorted(sections.values(), key=lambda row: (row["reviewed_at"], row["id"]), reverse=True)
        topics = {(row["subject"], row["section"]) for row in changes}
        previous = [row for row in recent if local_date(row["reviewed_at"]) < date
                    and (not topics or (row["subject"], row["section"]) in topics)]
    unique = {}
    for row in previous:
        if local_date(row["reviewed_at"]) < date:
            unique.setdefault((row["subject"], row["section"]), row)
    return list(unique.values())[:limit]


def history_links(rows, directory, archive_dir, dossiers, local_date, heading, archive_exists):
    lines = []
    for row in rows:
        date = local_date(row["reviewed_at"])
        title = heading(dossiers, row)
        path = f"{archive_dir}/{date}.md"
        if archive_exists(path):
            link = relative_link(f"{date}の詳しい記録", directory, path)
        else:
            link = f"{date}の確認"
        lines.append(f"- {title} · {link}")
    return lines


def next_checks(proposed, dossiers, detail, heading, gaps):
    changes = [row for row in proposed if row["type"] == "dossier_section"]
    notes = []
    for row in changes[:2]:
        value = re.sub(r"^判断を進めるために次に見る資料(?:・実績)?[：:]\s*", "", row["uncertainty"])
        note = short_sentence(value)
        if note:
            notes.append(f"- **{heading(dossiers, row)}**　{note}")
    for row in [item for item in proposed if item["type"] == "warning"][:1]:
        value = row["next_check"]
        first, stop, rest = value.partition("。")
        note = short_sentence(rest, 150) if re.fullmatch(r"\d{4}-\d\d-\d\d頃?", first) and stop else ""
        if note:
            note = f"{first}に再確認。{note}"
        else:
            note = short_sentence(value)
        if note:
            notes.append(f"- **警戒項目の再確認**　{note}")
    first_gap = next((text for gap in gaps if not gap.startswith("https://")
                      and (text := short_sentence(gap))), "")
    if not notes and first_gap:
        notes.append(f"- **確認が残る項目**　{first_gap}")
    return notes or [f"[詳しい記録]({detail})で調査範囲と継続中の論点を確認できます。"]


def brief_text(state, manifest, proposed, dossiers, directory, archive_dir, detail, archived,
               claim_labels, collection_labels, local_date, heading, dossier_index_dir, archive_exists):
    date = manifest["date"]
    new = [row for row in proposed if row["type"] == "evidence"]
    changes = [row for row in proposed if row["type"] == "dossier_section"]
    groups = {row["source_group"] for row in new}
    mode = "試行運用" if manifest["mode"] == "shadow" else "本運用"
    past = prior_sections(state["records"], changes, date, local_date)
    history = history_links(past, directory, archive_dir, dossiers, local_date, heading, archive_exists)
    index = relative_link("企業・市場資料", directory, dossier_index_dir + "/README.md")
    lines = [f"# AI市場の調査日報｜{date}", "", f"[日報一覧](README.md) · {index}", "",
             "## 今回分かったこと", "", *highlight_lines(new, detail, archived, claim_labels, local_date),
             "", f"{mode} · 採用 {len(new)}件・出所 {len(groups)}系統 · 確認できなかった点 {len(manifest['gaps'])}件",
             collection_labels[manifest["quality"]], ""]
    if changes:
        links = [relative_link(heading(dossiers, row), directory,
                               f"{dossier_index_dir}/{row['subject']}.md", f"#section-{row['section']}")
                 for row in changes[:3]]
        lines += [f"見直した資料　{' · '.join(links)}", ""]
    lines += ["## 前回の確認", ""]
    lines += history or ["同じ論点の過去記録は、企業・市場資料から確認できます。"]
    lines += ["", "## 次に確かめること", "", *next_checks(proposed, dossiers, detail, heading, manifest["gaps"]),
              "", f"[出典・分析・採点の詳しい記録]({detail})", ""]
    return "\n".join(lines)
