"""Reports derive from saved records; a renderer cannot invent a forecast."""

import json
import os
import posixpath
import re
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

from .forecast_contract import instant, require
from .forecast_learning import digest, load_state
from .forecast_scoring import scorecard
from .learning_brief import brief_text, is_feed, prior_sections, relative_link
from .report_knowledge import dossier_text, relocate_links, validate_dossiers


LABELS = {"short": "短期（1〜3か月）", "medium": "中期（3か月超〜1年）",
          "long": "長期（1年超〜3年）", "exploration": "探索（3〜10年）"}
COLLECTION_LABELS = {"complete": "今回の確認範囲で資料の収集を完了しました。",
                     "partial": "一部の資料を取得できませんでした。",
                     "stale": "当日の情報を確認できず、保存済み資料を参照しました。",
                     "failed": "今回の処理が完了しませんでした。"}
PERIOD_LABELS = {"weekly": "週次", "monthly": "月次", "quarterly": "四半期", "semiannual": "半年"}
RESOLUTION_LABELS = {"draft": "準備中", "open": "観測中", "awaiting_data": "実績待ち",
                     "resolved_true": "命題が成立", "resolved_false": "命題が不成立",
                     "resolved_value": "実績値を確認", "unresolvable": "判定不能",
                     "invalidated": "無効", "condition_not_met": "前提条件が不成立"}
CLAIM_LABELS = {"observed_fact": "確認した事実", "announced_plan": "発表された計画",
                "reported_claim": "発表元の説明", "expert_opinion": "専門家の見解", "analysis": "分析"}
WARNING_LABELS = {"normal": "通常", "watch": "要観察", "warning": "警戒", "critical": "重大"}
JST = ZoneInfo("Asia/Tokyo")


def atomic_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".pending-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as output:
            output.write(text)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def score_table(state, now):
    lines = ["| 期間 | 採点済み | 独立した出来事 | 二択予測の確率誤差 | 比較用予測の確率誤差 |",
             "|---|---:|---:|---:|---:|"]
    for horizon, score in scorecard(state, now).items():
        value = lambda key: "未評価" if score[key] is None else f"{score[key]:.3f}"
        lines.append(f"| {LABELS[horizon]} | {score['scored_questions']} | {score['independent_families']} | "
                     f"{value('latest_brier')} | {value('baseline_brier')} |")
    return lines + ["", "採点済みが0件の期間は未評価です。誤差が小さいほど、その期間の予測は実績に近いと判断します。",
                    "同じ出来事は、複数の記事で確認しても1件と数えます。"]


def local_date(timestamp):
    return instant(timestamp).astimezone(JST).date().isoformat()


def source_links(identifiers, evidence):
    groups = {}
    for identifier in identifiers:
        groups.setdefault(evidence[identifier]["url"], []).append(identifier)
    return "、".join(f"[{', '.join(ids)}]({url})" for url, ids in groups.items())


def evidence_lines(records):
    if not records:
        return ["今日、新しい根拠として採用した資料はありません。"]
    sources = {}
    for record in records:
        sources.setdefault(record["url"], []).append(record)
    lines = []
    for url, group in sources.items():
        feed = is_feed(url)
        label = "発表元のフィード" if feed else "参照資料"
        lines += [f"### {urlparse(url).hostname}", "", f"[{label}を開く]({url})", ""]
        for record in group:
            kind = "フィードで確認した記述" if feed and record["claim_type"] == "observed_fact" else CLAIM_LABELS[record["claim_type"]]
            date = local_date(record["published_at"])
            lead, stop, remaining = record["summary"].partition("。")
            lines += [f'<a name="evidence-{record["id"]}"></a>', "",
                      f"**{kind}**　{lead}{stop}（公開日 {date} JST、{record['id']}）", ""]
            if remaining.strip():
                lines += ["<details>", "<summary>資料の内容と注意点</summary>", "",
                          remaining.strip(), "", "</details>", ""]
        lines.append("")
    return lines


def dossier_heading(dossiers, update):
    dossier = dossiers[update['subject']]
    title = next(section['title'] for section in dossier['sections'] if section['id'] == update['section'])
    return f"{dossier['title'].partition('：')[0]} ／ {title}"


def dossier_update_lines(changes, dossiers, evidence, new_ids):
    if not changes:
        return ["企業・市場の本文は前回までの確認内容を引き継いでいます。基準日は各資料の冒頭にあります。"]
    lines = []
    for update in changes:
        heading = dossier_heading(dossiers, update)
        today = [key for key in update["evidence_ids"] if key in new_ids]
        sources = source_links(today, evidence)
        lead, stop, remaining = update["analysis"].partition("。")
        uncertainty, period, other = update["uncertainty"].partition("。")
        lines += [f"### {heading}", "", lead + stop, "",
                  f"**未確認・次の確認**　{uncertainty}{period}", ""]
        if sources:
            lines += [f"今回採用した資料 {sources}", ""]
        if remaining.strip() or other.strip():
            lines += ["<details>", "<summary>詳しい分析と未確認事項</summary>", "",
                      remaining.strip(), "", other.strip(), "", "</details>", ""]
    return lines


def dossier_history_lines(records, dossiers, changes, date):
    previous = prior_sections(records, changes, date, local_date, limit=3)
    if not previous:
        return ["関連する過去の記録は、末尾の企業・市場資料に基準日と出典を記載しています。"]
    lines = ["今回の更新に関連する過去の記録です。", ""]
    for row in previous:
        heading = dossier_heading(dossiers, row)
        sources = source_links(row["evidence_ids"], records["evidence"])
        lines += ["<details>", f"<summary>{local_date(row['reviewed_at'])}の確認　{heading}</summary>", "",
                  row["analysis"], "", f"当時の未確認事項　{row['uncertainty']}", "",
                  f"出典 {sources}", "", "</details>", ""]
    return lines


def dossier_index(dossiers):
    lines = ["| 企業・市場資料 | 最終更新（JST） |", "|---|---|"]
    for subject, dossier in dossiers.items():
        dates = [local_date(section["reviewed_at"]) for section in dossier["sections"] if section.get("reviewed_at")]
        date = max(dates, default=dossier["available_on"])
        label = dossier["title"].partition("：")[0]
        revision = f"{date}（初版）" if not dates else date
        lines.append(f"| [{label}]({subject}.md) | {revision} |")
    return lines


def report_text(state, manifest, proposed, dossiers, embed_dossiers=True):
    records = state["records"]
    mode = "試行運用" if manifest["mode"] == "shadow" else "本運用"
    changes = [row for row in proposed if row["type"] == "dossier_section"]
    new = [row for row in proposed if row["type"] == "evidence"]
    groups = {row["source_group"] for row in new}
    urls = {row["url"] for row in new}
    finished = instant(manifest["finished_at"]).astimezone(JST).strftime("%Y-%m-%d %H:%M")
    lines = [f"# {manifest['date']} AI企業と市場の日報", "",
             f"作成 {finished} JST（{mode}）", "",
             COLLECTION_LABELS[manifest["quality"]],
             f"採用した記録 {len(new)}件（{len(groups)}出所・{len(urls)} URL）。確認できなかった点 {len(manifest['gaps'])}件。",
             "", "## 今日採用した資料", "", *evidence_lines(new),
             "", "## 今日の更新", "", *dossier_update_lines(changes, dossiers, records["evidence"], {row["id"] for row in new}),
             "", "## 確認できなかったこと", ""]
    if manifest["gaps"]:
        lines += ["以下の収集メモには、確認範囲外の項目と採用に必要な確認を終えていない言及を含みます。", "",
                  "<details>", f"<summary>確認できなかった点 {len(manifest['gaps'])}件</summary>", "",
                  *[f"- {gap}" for gap in manifest["gaps"]], "", "</details>"]
    else:
        lines.append("今回の確認範囲で、資料の不足は報告されていません。")
    lines += ["", "会社の顧客・利益、個人の所得は、許可された実績がなければ未観測です。", "",
              "## 過去の調査とのつながり", "",
              *dossier_history_lines(records, dossiers, changes, manifest["date"])]
    lines += ["", "## 仮説の見直し", ""]
    reviews = [r for r in proposed if r["type"] in {"hypothesis_review", "review", "link_review"}]
    for review in reviews:
        identifier = review.get("hypothesis_id", review.get("question_id", review.get("link_id")))
        lines += [f"- **{identifier}**：{review.get('reason', ' / '.join(review.get('cause_hypotheses', [])))}",
                  f"  次の確認：{review['next_check']}"]
        for key, label in [("supporting_evidence_ids", "支える根拠"), ("opposing_evidence_ids", "反対の根拠")]:
            if key in review:
                links = source_links(review[key], records["evidence"])
                lines.append(f"  {label}　{links or '今回は未取得'}。")
    if not reviews:
        lines.append("今回、判断を更新した仮説はありません。")
    warnings = list(records["warning"].values())
    replaced = {r["supersedes"] for r in warnings}
    lines += ["", "## 危険と行動", ""]
    lines += [f"- {r['risk_id']}　{WARNING_LABELS[r['level']]}。{r['reason']}\n  次の確認　{r['next_check']}\n"
              f"  出典　{source_links(r['evidence_ids'], records['evidence']) or '未取得'}"
              for r in warnings if r["id"] not in replaced] or ["正式な警戒水準はまだ判定していません。記録がないことを、安全という意味には使いません。"]
    lines += ["", "## 予測の採点結果", "", *score_table(state, manifest["finished_at"]), "",
              "短期は料金・利用条件と特定の業務での実績、中期は継続利用・顧客維持・採用、長期は実質所得・仕事への移行・利益の分配を確認します。",
              "因果関係は一つずつ確認します。中期・長期の予測はそれぞれの期間の実績で評価します。", "",
              "## 企業・市場の詳しい情報", "", *dossier_index(dossiers), ""]
    if embed_dossiers:
        lines += ["<details>", "<summary>企業・市場の全文</summary>", "",
                  *[dossier_text(dossier, heading=3) for dossier in dossiers.values()], "", "</details>", ""]
    return "\n".join(lines)


def review_due(date):
    day = datetime.fromisoformat(date)
    return {"weekly": day.weekday() == 0, "monthly": day.day == 1,
            "quarterly": day.day == 1 and day.month in {1, 4, 7, 10},
            "semiannual": day.day == 1 and day.month in {1, 7}}


def write_failure_snapshot(root, state, manifest, dossiers):
    base = root / ("state/shadow" if manifest['mode'] == 'shadow' else '.')
    path = base / 'Intelligence' / f"{manifest['date']}.md"
    if path.exists():
        return
    validate_dossiers(dossiers)
    text = "> 収集・検証に失敗しました。以下は以前の確認済み情報を持ち越した参考資料です。当日の新しい判断は含みません。\n\n"
    text += report_text(state, manifest, [], dossiers)
    atomic_text(path, relocate_links(text, path.parent.relative_to(root).as_posix()))


def write_outputs(root, state, manifest, proposed, dossiers):
    base = root / ("state/shadow" if manifest["mode"] == "shadow" else ".")
    write_report_documents(root, base, state, manifest, proposed, dossiers)
    scores = scorecard(state, manifest["finished_at"])
    atomic_text(base / "state/scores/latest.json", json.dumps(scores, ensure_ascii=False, indent=2) + "\n")
    write_reviews(base, state, manifest, dossiers, scores)


def review_updates(base, state, manifest, dossiers, period):
    date = manifest["date"]
    end = datetime.fromisoformat(date).date()
    if period == "weekly":
        start = end - timedelta(days=7)
    else:
        months = {"monthly": 1, "quarterly": 3, "semiannual": 6}[period]
        year, month = divmod(end.year * 12 + end.month - 1 - months, 12)
        start = end.replace(year=year, month=month + 1, day=1)
    start += timedelta(days=1)
    sections = state["records"]["dossier_section"]
    latest = {}
    for row in sorted(sections.values(), key=lambda item: instant(item["reviewed_at"])):
        day = local_date(row["reviewed_at"])
        if start.isoformat() <= day <= date:
            key = row["subject"], row["section"]
            latest[key] = row, latest.get(key, (row, row))[1]
    lines = [f"{start.isoformat()}〜{date} JST", ""]
    if not latest:
        return lines + ["この期間に企業・市場資料の節を更新した記録はありません。"]
    lines += ["| 論点 | 期間前の確認 | 期間中の最終更新 |", "|---|---|---|"]
    for current, first in sorted(latest.values(), key=lambda pair: instant(pair[0]["reviewed_at"]), reverse=True):
        day = local_date(current["reviewed_at"])
        previous = sections.get(first["supersedes"])
        earlier = local_date(previous["reviewed_at"]) if previous else None
        day_link = lambda value: (f"[{value}](../../Intelligence/{value}.md)"
                                  if (base / "Intelligence" / f"{value}.md").is_file() else value)
        lines.append(f"| {dossier_heading(dossiers, current)} | "
                     f"{day_link(earlier) if earlier else '初回'} | {day_link(day)} |")
    return lines


def write_reviews(base, state, manifest, dossiers, scores):
    for period, due in review_due(manifest["date"]).items():
        if not due:
            continue
        detail = [f"# {manifest['date']} {PERIOD_LABELS[period]}レビュー", "",
                  "## 期間中の更新", "", *review_updates(base, state, manifest, dossiers, period),
                  "", "## 予測の採点結果", "", *score_table(state, manifest["finished_at"])]
        detail += ["", "## 予測ごとの判定", "", *resolution_table(scores)]
        detail += ["", "## 次に見直す点", "", {
            "weekly": "外れた理由、反対の根拠、次の測定を残します。採点対象の実績がなければ原因は未判定です。",
            "monthly": "社会の仕事と所得、会社の顧客と利益、個人の選択肢を別々に確認します。会社の利益が増えても、雇用や個人所得が改善したとは限りません。",
            "quarterly": "作業の自動化から時間、雇用、所得へ進む関係を一つずつ見直します。短期の成功を長期へそのまま当てはめません。",
            "semiannual": "所有と生活保障の仕組みについて、議論・制度化・実際の支給や利用を分けます。3〜10年の探索を短期の成績で採点しません。"}[period], ""]
        atomic_text(base / "reviews" / period / f"{manifest['date']}.md", "\n".join(detail))


def write_report_documents(root, base, state, manifest, proposed, dossiers):
    validate_dossiers(dossiers)
    daily_dir = (base / 'Intelligence').relative_to(root).as_posix()
    date = manifest["date"]
    archive_dir = "state/shadow/Intelligence" if manifest["mode"] == "shadow" else "Intelligence/details"
    dossier_dir = (base / "static_intelligence").relative_to(root).as_posix()
    detail_path = f"{archive_dir}/{date}.md"
    if base != root or manifest["mode"] != "shadow":
        detail = report_text(state, manifest, proposed, dossiers, embed_dossiers=False)
        atomic_text(root / detail_path, relocate_links(detail, archive_dir))
    if base == root:
        archived = (root / detail_path).read_text(encoding="utf-8")
        detail_link = posixpath.relpath(detail_path, daily_dir)
        brief = brief_text(state, manifest, proposed, dossiers, daily_dir, archive_dir, detail_link, archived,
                           CLAIM_LABELS, COLLECTION_LABELS, local_date, dossier_heading, dossier_dir,
                           lambda path: (root / path).is_file())
        atomic_text(base / "Intelligence" / f"{date}.md", brief)
        write_report_indexes(base, dossiers)
    for subject, dossier in dossiers.items():
        text = dossier_text(dossier, navigation=base == root)
        if base == root and manifest["mode"] == "shadow":
            title, body = text.split("\n\n", 1)
            text = f"{title}\n\n> 試行運用で検証した資料を反映しています。\n\n{body}"
        atomic_text(base / 'static_intelligence' / f'{subject}.md', relocate_links(text, dossier_dir))


def write_report_indexes(base, dossiers):
    directory = base / "Intelligence"
    dates = sorted((path for path in directory.glob("*.md")
                    if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", path.name)), reverse=True)
    lines = ["# AI市場の調査日報", "", "[企業・市場資料](../static_intelligence/README.md)", ""]
    lines += [f"- [{day.stem}]({day.name})" for day in dates]
    atomic_text(directory / "README.md", "\n".join(lines) + "\n")
    lines = ["# 企業・市場資料", "", "[日報一覧](../Intelligence/README.md)", "", *dossier_index(dossiers), "",
             "最終更新は、本文の節を最後に見直した日です。資料の最初に、更新した節とその日付を表示します。", ""]
    atomic_text(base / "static_intelligence/README.md", "\n".join(lines))


def project_shadow_reports(root, manifest):
    require(manifest["mode"] == "shadow" and manifest["outcome"] in {"complete", "partial"},
            "only successful shadow runs can publish reports")
    run_id = manifest["run_id"]
    date = local_date(manifest["started_at"])
    require(manifest["date"] == date, "report date does not match run")
    saved = json.loads((root / "state/runs" / run_id / "accepted-plan.json").read_text(encoding="utf-8"))
    state = load_state(root / "state/shadow", through_run=run_id)
    plan, dossiers = saved["plan"], saved["dossiers"]
    require(state["revision"] == manifest["revision_after"], "report ledger revision mismatch")
    require(state["runs"][run_id] == digest(plan), "report plan does not match committed records")
    require(digest(dossiers) == manifest["dossier_hash"], "report snapshot hash mismatch")
    require(saved["gaps"] == manifest["gaps"] and saved["finished_at"] == manifest["finished_at"]
            and plan["quality"] == manifest["quality"] == manifest["outcome"], "report metadata mismatch")
    write_report_documents(root, root, state, manifest, plan["records"], dossiers)
    write_reviews(root, state, manifest, dossiers, scorecard(state, manifest["finished_at"]))


def resolution_table(scores):
    rows = [row for score in scores.values() for row in score["details"]]
    if not rows:
        return ["今回の集計対象に登録済みの予測はありません。"]
    lines = ["| 予測ID | 現在の状態 | 初回の誤差 | 最新実績での誤差 |", "|---|---|---:|---:|"]
    for row in rows:
        first = row["initial"]["value"] if row["initial"] else "未評価"
        latest = row["latest"]["value"] if row["latest"] else "未評価"
        lines.append(f"| {row['question_id']} | {RESOLUTION_LABELS[row['status']]} | {first} | {latest} |")
    return lines
