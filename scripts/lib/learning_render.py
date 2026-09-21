"""Reports derive from saved records; a renderer cannot invent a forecast."""

import json
import os
import tempfile
from datetime import datetime
from pathlib import Path

from .forecast_scoring import scorecard


LABELS = {"short": "短期（1〜3か月）", "medium": "中期（3か月超〜1年）",
          "long": "長期（1年超〜3年）", "exploration": "探索（3〜10年）"}


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
    lines = ["| 期間 | 採点済み | 独立した出来事 | 確率の誤差 | 比較用予測の誤差 |",
             "|---|---:|---:|---:|---:|"]
    for horizon, score in scorecard(state, now).items():
        value = lambda key: "未評価" if score[key] is None else f"{score[key]:.3f}"
        lines.append(f"| {LABELS[horizon]} | {score['scored_questions']} | {score['independent_families']} | "
                     f"{value('latest_brier')} | {value('baseline_brier')} |")
    return lines + ["", "誤差は小さいほどよい値です。0件は未評価です。同じ出来事を複数の記事で数えません。",
                    "短期の結果だけで、中期・長期も正確になったとは判断しません。"]


def evidence_line(record):
    return f"- {record['summary']} [原資料]({record['url']})（{record['id']}、公開 {record['published_at'][:10]}）"


def report_text(state, manifest, proposed):
    records = state["records"]
    lines = [f"# {manifest['date']} — 仮説と実績の確認", "",
             f"作成：{manifest['finished_at']}。運用：{manifest['mode']}。資料の状態：{manifest['quality']}。", "",
             "## 今日わかったこと", ""]
    new = [r for r in proposed if r["type"] == "evidence"]
    lines += [evidence_line(r) for r in new] or ["新しい根拠として採用できる資料はありません。前回の資料を今日の発見として扱いません。"]
    lines += ["", "## 仮説の見直し", ""]
    reviews = [r for r in proposed if r["type"] in {"hypothesis_review", "review", "link_review"}]
    for review in reviews:
        identifier = review.get("hypothesis_id", review.get("question_id", review.get("link_id")))
        lines += [f"- **{identifier}**：{review.get('reason', ' / '.join(review.get('cause_hypotheses', [])))}",
                  f"  次の確認：{review['next_check']}"]
        for key, label in [("supporting_evidence_ids", "支える根拠"), ("opposing_evidence_ids", "反対の根拠")]:
            if key in review:
                lines.append(f"  {label}：{', '.join(review[key]) or '今回は未取得'}。")
    if not reviews:
        lines.append("判断を変えるだけの材料はありません。仮説の見込みを機械的に上げ下げしません。")
    lines += ["", "## 短期・中期・長期で確かめること", "",
              "短期は料金・利用条件と固定業務の実測。中期は継続利用・顧客維持・採用。長期は実質所得・仕事への移行・利益の分配を確認します。",
              "いまの情報がどの因果関係を確かめたのかを記録し、別の関係まで一度に結論づけません。", ""]
    lines += score_table(state, manifest["finished_at"])
    warnings = list(records["warning"].values())
    replaced = {r["supersedes"] for r in warnings}
    lines += ["", "## 危険と行動", ""]
    lines += [f"- {r['risk_id']}：{r['level']}。{r['reason']} 次の確認：{r['next_check']}"
              for r in warnings if r["id"] not in replaced] or ["正式な警戒水準はまだ判定していません。記録がないことを、安全という意味には使いません。"]
    lines += ["", "## 足りない情報", ""] + [f"- {gap}" for gap in manifest["gaps"]]
    if not manifest["gaps"]:
        lines.append("今回の収集対象内では、未処理の不足は報告されていません。対象外まで確認できたことは意味しません。")
    lines += ["", "会社の顧客・利益、個人の所得は、許可された実績がなければ未観測です。", ""]
    return "\n".join(lines)


def review_due(date):
    day = datetime.fromisoformat(date)
    return {"weekly": day.weekday() == 0, "monthly": day.day == 1,
            "quarterly": day.day == 1 and day.month in {1, 4, 7, 10},
            "semiannual": day.day == 1 and day.month in {1, 7}}


def write_outputs(root, state, manifest, proposed):
    base = root / ("state/shadow" if manifest["mode"] == "shadow" else ".")
    atomic_text(base / "Intelligence" / f"{manifest['date']}.md", report_text(state, manifest, proposed))
    scores = scorecard(state, manifest["finished_at"])
    atomic_text(base / "state/scores/latest.json", json.dumps(scores, ensure_ascii=False, indent=2) + "\n")
    for period, due in review_due(manifest["date"]).items():
        if not due:
            continue
        detail = [f"# {manifest['date']} {period} — 予測と実績", ""] + score_table(state, manifest["finished_at"])
        detail += ["", "## 判定の一覧", "", "| 予測 | 現在の状態 | 初回の誤差 | 最新実績での誤差 |", "|---|---|---:|---:|"]
        for score in scores.values():
            for row in score["details"]:
                first = row["initial"]["value"] if row["initial"] else "未評価"
                latest = row["latest"]["value"] if row["latest"] else "未評価"
                detail.append(f"| {row['question_id']} | {row['status']} | {first} | {latest} |")
        detail += ["", "## 次に見直す点", "", {
            "weekly": "外れた理由、反対の根拠、次の測定を残します。採点対象の実績がなければ原因は未判定です。",
            "monthly": "社会の仕事と所得、会社の顧客と利益、個人の選択肢を別々に確認します。会社の利益が増えても、雇用や個人所得が改善したとは限りません。",
            "quarterly": "作業の自動化から時間、雇用、所得へ進む関係を一つずつ見直します。短期の成功を長期へそのまま当てはめません。",
            "semiannual": "所有と生活保障の仕組みについて、議論・制度化・実際の支給や利用を分けます。3〜10年の探索を短期の成績で採点しません。"}[period], ""]
        atomic_text(base / "reviews" / period / f"{manifest['date']}.md", "\n".join(detail))
