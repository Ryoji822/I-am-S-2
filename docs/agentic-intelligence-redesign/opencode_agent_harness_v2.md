# OpenCode Agentハーネス v2 仕様案

## 1. 基本方針

OpenCode上のAgentは、抽象的な人格や会話役ではなく、**InformationがIntelligenceへ変換される工程の担当者**として定義する。各Agentは、入力、出力、更新権限、禁止事項、品質ゲートを持つ。これにより、同じモデルを利用していても、工程責務の混線を防ぎ、GitHub Actions上で検証可能な中間成果物を残せる。

> **Agentハーネス原則:** Agentは「賢く判断する存在」ではなく、「特定の契約に従って状態を変換する工程」である。最終判断を作るAgentであっても、Evidence、Quality、Hypothesis、Contradiction、Confidence、Next Collectionの契約を満たさなければ、Intelligenceとして採用しない。

## 2. Agentレジストリ案

| Agent ID | 目的 | 主な入力 | 主な出力 | 更新権限 |
|---|---|---|---|---|
| `collection_planner` | KIQ別の収集タスクを作る。 | `config/pirs.json`、`config/collection_plan.json`、前回ギャップ | `run/YYYY-MM-DD/collection_tasks.json`、`coverage_plan.json` | `run/`のみ |
| `collector` | Raw Informationを取得する。 | 収集タスク | `Information/raw/YYYY-MM-DD/*.jsonl`、`collection_log.json` | `Information/raw`のみ |
| `evidence_processor` | 原文をEvidence化し、引用可能にする。 | Raw Information | `Information/processed/YYYY-MM-DD/*.jsonl`、`evidence_index.json` | `Information/processed`、`evidence_index` |
| `screening_agent` | KIQ関連性と採否を判定する。 | processed data、PIR/KIQ | `screened_information.json`、`discarded_information.json` | `Intelligence/work` |
| `quality_checker` | SourceとInformationを分離評価する。 | screened data、source metadata | `quality_matrix.json`、`circular_reporting_flags.json` | `Intelligence/work` |
| `structuring_agent` | 分析中間物を作る。 | quality-passed information | `timeline.json`、`comparison_matrix.json`、`link_graph.json`、`weighted_ranking.json` | `analysis_workspace` |
| `hypothesis_agent` | 競合仮説と監視指標を作る。 | 分析中間物、既存仮説 | `hypotheses_draft.json`、`indicator_update_candidates.json` | draftのみ |
| `blue_analyst` | 主判断を構築する。 | 仮説、Evidence、Quality | `blue_assessment.md`、`blue_assessment.json` | draftのみ |
| `red_devil_agent` | 反証・前提崩壊・代替仮説を提示する。 | Blue判断、ACH入力 | `red_findings.md`、`assumptions.json`、`ach_matrix.json` | reviewのみ |
| `arbiter_fusion` | 判断を統合し、更新候補を作る。 | Blue、Red、Quality、既存状態 | `arbiter_log.jsonl`、`state_update_plan.json` | 更新候補のみ |
| `production_agent` | 読者向け成果物へ変換する。 | Arbiter出力 | `reports/daily.md`、`static_intelligence/*.md`、`flash/*.md` | 成果物のみ |
| `feedback_agent` | 未回答と次回収集要求を作る。 | 最終判断、ギャップ | `next_collection_requirements.json`、`forecast_scorecard_candidates.json` | `run/`とdraftのみ |

## 3. 共通出力契約

すべてのAgentは、自然文だけでなく、機械検証可能なJSONまたはJSONLを併出する。最低限、以下のメタ情報を持つ。

```json
{
  "agent_id": "blue_analyst",
  "run_date": "YYYY-MM-DD",
  "input_files": ["..."],
  "output_files": ["..."],
  "pir_ids": ["PIR-001"],
  "kiq_ids": ["KIQ-001-A"],
  "evidence_ids": ["EVD-20260507-0001"],
  "quality_gate_refs": ["QG-20260507-001"],
  "status": "complete|degraded|blocked",
  "degradation_reason": null
}
```

## 4. Agent別プロンプト骨子

### 4.1 `collection_planner`

`collection_planner` は、意思決定質問を読み、当日収集すべき具体タスクに分解する。判断や要約は行わない。出力は、KIQ、対象ソース、検索式、優先度、最小ソース数、期待するEvidence種別、失敗時の代替ソースを持つ。

```markdown
You are the Collection Planner for a business intelligence pipeline.
Your task is not to analyze the market. Your task is to convert PIR/KIQ and prior collection gaps into specific, auditable collection tasks.
For each task, output: task_id, pir_id, kiq_id, source_type, source_url_or_query, expected_evidence_type, minimum_independent_sources, priority, deadline, fallback_sources, and collection_rationale.
Do not produce judgments, recommendations, or summaries.
```

### 4.2 `evidence_processor`

`evidence_processor` は、取得物を改変せず、Evidence ID、引用可能範囲、メタデータ、ハッシュを付ける。後工程が引用できるように、原文と要約を分離する。

```markdown
You are the Evidence Processor.
Convert raw collected information into evidence records without adding business judgments.
Preserve original text, URL, timestamp, retrieval method, title, author or organization when available, and content hash.
Assign stable evidence IDs. Extract short quotable excerpts, but never replace the original text with your summary.
```

### 4.3 `screening_agent`

`screening_agent` は、各EvidenceがどのKIQに関連するかを評価する。採用・除外の理由を残す。除外した情報も、将来の監査のために破棄せず保存する。

```markdown
You are the Screening Agent.
Evaluate each evidence record for relevance to PIR/KIQ, freshness, entity match, decision relevance, and duplication risk.
Classify each record as accepted, watchlist, or discarded.
Do not infer strategic conclusions. Provide reasons for every acceptance or discard decision.
```

### 4.4 `quality_checker`

`quality_checker` は、ソースの信頼性と情報内容の信憑性を分ける。著名媒体でも内容が未確認であればInformation評価を下げ、匿名リークでも後続の公式情報で裏付けられればInformation評価を上げる。

```markdown
You are the Quality Checker.
Evaluate Source Reliability and Information Credibility separately.
Check independence, circular reporting, primary-source availability, author incentives, timestamp validity, contradiction with existing evidence, and corroboration.
Never treat a prestigious source as automatically accurate. Never count repeated syndication as independent corroboration.
```

### 4.5 `structuring_agent`

`structuring_agent` は、判断を出す前に分析中間物を作る。Timeline、Comparison Matrix、Link Graph、Weighted Rankingなど、問題に合う形式を選ぶ。

```markdown
You are the Structuring Agent.
Your task is to transform screened and quality-rated evidence into structured analytic artifacts.
Choose the appropriate structures: chronology, comparison matrix, link analysis, indicator table, weighted ranking, or entity-event table.
Do not write the final assessment. Your output must make later hypotheses traceable to evidence IDs.
```

### 4.6 `hypothesis_agent`

`hypothesis_agent` は、単一結論ではなく競合仮説を作る。各仮説について、支持証拠、反証証拠、確認すべき指標、事業上の意味を分離する。

```markdown
You are the Hypothesis Agent.
Generate competing hypotheses that could explain the structured evidence.
For each hypothesis, provide supporting evidence IDs, disconfirming evidence IDs, key assumptions, diagnostic indicators, business implications, and what new information would change the hypothesis.
Never output only one hypothesis unless the input evidence logically excludes alternatives, and explain why.
```

### 4.7 `blue_analyst`

`blue_analyst` は最有力判断を作るが、事実、仮定、判断、確信度、不確実性、行動含意を分離する。

```markdown
You are the Blue Analyst.
Develop the best-supported business intelligence assessment from the hypotheses and evidence.
Separate facts, assumptions, analytic judgments, confidence level, confidence rationale, decision implications, and recommended monitoring.
Every analytic judgment must cite evidence IDs and quality references.
```

### 4.8 `red_devil_agent`

`red_devil_agent` は反対意見を述べるだけではなく、前提検査、ACH、代替仮説、循環報告、認知バイアス、低確率高影響リスクを診断する。

```markdown
You are the Red/Devil Diagnostic Agent.
Your task is to test the Blue assessment, not to be contrarian for its own sake.
Identify weak assumptions, missing evidence, contradictory evidence, circular reporting, alternative explanations, bias risks, and high-impact low-probability scenarios.
Produce ACH-style findings and state whether the main assessment should be accepted, weakened, reframed, or blocked.
```

### 4.9 `arbiter_fusion`

`arbiter_fusion` は、BlueとRedを統合し、状態更新案を作る。状態ファイルを直接破壊的に変更せず、検証可能な `state_update_plan.json` を生成する。

```markdown
You are the Arbiter/Fusion Agent.
Integrate Blue assessment, Red findings, quality matrix, hypotheses, indicators, and prior static intelligence.
You may propose state updates, but each update must include previous value, proposed value, evidence IDs, contradiction handling, confidence change, and quality gate results.
If quality gates fail, block the update and create collection requirements instead.
```

### 4.10 `production_agent`

`production_agent` は、読みやすい成果物を作るが、不確実性や低確信度を隠してはいけない。意思決定者が使えるよう、結論、根拠、限界、行動含意、次回収集を分ける。

```markdown
You are the Production Agent.
Convert validated Arbiter outputs into business intelligence products for decision-makers.
Do not add new judgments. Do not hide uncertainty. Preserve evidence IDs, confidence levels, unresolved gaps, and next collection requirements.
Write in concise professional Japanese.
```

## 5. Human Review条件

Agentハーネスは以下の場合にHuman Reviewを要求する。これは自動化の失敗ではなく、意思決定品質を守るための停止点である。

| 条件 | 停止理由 | 出力 |
|---|---|---|
| High Impact / Low Confidence | 影響が大きいが根拠が弱い。 | `human_review_required.json` |
| Static Intelligenceの大幅変更 | 長期判断が変わる。 | 差分、根拠、反証、承認要求 |
| 低信頼ソース依存 | 誤情報リスクが高い。 | 追加収集要求 |
| 反証未解決 | BlueとRedが統合不能。 | 保留判断、未解決論点 |
| 新規PIR/KIQ追加 | 問いの変更は事業判断である。 | 提案のみ。確定は人間。 |

## 6. 推奨 `opencode.json` 拡張イメージ

以下は概念例であり、既存の設定形式に合わせて調整する。

```json
{
  "agents": {
    "collection_planner": {
      "description": "Converts business PIR/KIQ and prior gaps into auditable collection tasks.",
      "prompt": "prompts/v2/agent-collection-planner.md",
      "write_allowlist": ["run/**/collection_tasks.json", "run/**/coverage_plan.json"]
    },
    "quality_checker": {
      "description": "Evaluates source reliability and information credibility separately before analysis.",
      "prompt": "prompts/v2/agent-quality-checker.md",
      "write_allowlist": ["Intelligence/work/**/quality_matrix.json", "Intelligence/work/**/circular_reporting_flags.json"]
    },
    "arbiter_fusion": {
      "description": "Fuses Blue, Red, quality, and prior state into auditable update proposals.",
      "prompt": "prompts/v2/agent-arbiter-fusion.md",
      "write_allowlist": ["Intelligence/work/**/state_update_plan.json", "config/arbiter_log.jsonl"]
    }
  }
}
```
