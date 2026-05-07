# Quality Gates and State Schemas 仕様案

## 1. 目的

本仕様は、GitHub ActionsとOpenCode AgentハーネスでInformationをIntelligenceへ変換する際に、各工程の成果物を機械検証できるようにするための契約である。自然文レポートだけでは、根拠、品質、反証、確信度、状態更新の整合性を検証できない。そのため、各AgentはMarkdown成果物と同時にJSONまたはJSONLの構造化成果物を出力する。

> **実装上の判断:** Markdownは人間向け成果物であり、JSON/JSONLは監査・検証・状態更新向け成果物である。最終レポートが読みやすくても、JSON契約を満たさない場合はIntelligenceとしてコミットしない。

## 2. Evidence Record

Raw情報は、分析に入る前にEvidence Recordへ変換する。Evidence Recordは、情報源・取得時点・引用可能範囲・原文ハッシュを持つ。

```json
{
  "evidence_id": "EVD-20260507-0001",
  "run_date": "2026-05-07",
  "source_url": "https://example.com/article",
  "source_title": "Example title",
  "source_organization": "Example Corp",
  "source_type": "official|news|social|github|regulatory|job_posting|research|other",
  "retrieved_at": "2026-05-07T08:12:33+09:00",
  "retrieval_method": "firecrawl|browser|api|manual|rss",
  "content_hash": "sha256:...",
  "language": "ja|en|other",
  "raw_path": "Information/raw/2026-05-07/example.json",
  "processed_path": "Information/processed/2026-05-07/EVD-20260507-0001.json",
  "quotable_excerpt": "原文からの短い引用。",
  "summary_for_indexing": "検索・分類用の短い要約。判断は含めない。"
}
```

| 必須項目 | 理由 |
|---|---|
| `evidence_id` | 後工程の判断を根拠へ接続するため。 |
| `source_url` / `raw_path` | 監査と再確認のため。 |
| `retrieved_at` | 情報鮮度と時点差分を評価するため。 |
| `content_hash` | 原文改変や重複を検知するため。 |
| `quotable_excerpt` | レポートで引用可能な根拠を保持するため。 |

## 3. Screening Record

Screeningは、EvidenceがどのPIR/KIQに関連するか、分析へ送ってよいかを判定する工程である。

```json
{
  "screening_id": "SCR-20260507-0001",
  "evidence_id": "EVD-20260507-0001",
  "pir_id": "PIR-001",
  "kiq_id": "KIQ-001-A",
  "decision_relevance": "high|medium|low|none",
  "freshness": "current|stale|historical_context",
  "entity_match": ["OpenAI", "Google"],
  "accepted_status": "accepted|watchlist|discarded",
  "accept_or_discard_reason": "なぜ分析対象にする／しないか。",
  "duplicate_group_id": "DUP-20260507-003",
  "screened_by": "screening_agent"
}
```

## 4. Quality Matrix

Source ReliabilityとInformation Credibilityを分ける。著名ソースの未確認報道、低信頼ソースの公式資料引用、同一リークの循環報道などを識別するためである。

```json
{
  "quality_id": "QG-20260507-0001",
  "evidence_id": "EVD-20260507-0001",
  "source_reliability": "A|B|C|D|E|F",
  "source_reliability_reason": "過去実績、一次性、専門性、利害関係の評価。",
  "information_credibility": "1|2|3|4|5|6",
  "information_credibility_reason": "裏付け、矛盾、具体性、鮮度の評価。",
  "is_primary_source": true,
  "independent_corroboration_count": 2,
  "circular_reporting_risk": "none|possible|likely",
  "contradicts_evidence_ids": ["EVD-20260507-0007"],
  "usable_for_major_judgment": true,
  "quality_notes": "判断に使う際の注意。"
}
```

| 評価軸 | 高評価の条件 | 低評価の条件 |
|---|---|---|
| Source Reliability | 一次資料、専門性、実績、透明性がある。 | 匿名、利害不明、過去誤報、出所不明。 |
| Information Credibility | 独立裏付け、具体性、時点整合、矛盾なし。 | 噂、単一ソース、循環報告、過去情報、矛盾あり。 |

## 5. Hypothesis Record

仮説は、単一結論ではなく、競合仮説として保存する。各仮説は、支持証拠、反証証拠、前提、指標を持つ。

```json
{
  "hypothesis_id": "HYP-001",
  "kiq_id": "KIQ-001-A",
  "hypothesis_statement": "競合Aは今後6か月で価格競争を強める。",
  "status": "active|weakened|strengthened|retired|new",
  "supporting_evidence_ids": ["EVD-20260507-0001"],
  "disconfirming_evidence_ids": ["EVD-20260507-0009"],
  "key_assumptions": ["API価格が顧客獲得の主要因である。"],
  "diagnostic_indicators": ["IND-PRICE-001", "IND-PARTNER-002"],
  "business_implication": "価格戦略と差別化訴求の再評価が必要。",
  "what_would_change_this": "主要競合が値上げまたは高付加価値化へ転じる公式証拠。"
}
```

## 6. ACH Matrix

ACHは、証拠がどの仮説を支持するかではなく、どの仮説と矛盾するかを重視する。これにより、支配的仮説への過剰適合を防ぐ。

```json
{
  "ach_id": "ACH-20260507-001",
  "kiq_id": "KIQ-001-A",
  "hypotheses": ["HYP-001", "HYP-002", "HYP-003"],
  "evidence_tests": [
    {
      "evidence_id": "EVD-20260507-0001",
      "diagnosticity": "high|medium|low",
      "hypothesis_consistency": {
        "HYP-001": "consistent",
        "HYP-002": "inconsistent",
        "HYP-003": "not_applicable"
      },
      "notes": "この証拠が何を区別できるか。"
    }
  ],
  "least_disconfirmed_hypothesis": "HYP-001",
  "remaining_uncertainties": ["価格改定の正式発表がまだない。"]
}
```

## 7. Blue Assessment JSON

Blue Assessmentは自然文だけではなく、構造化された判断を併出する。

```json
{
  "assessment_id": "BLUE-20260507-001",
  "pir_id": "PIR-001",
  "kiq_id": "KIQ-001-A",
  "facts": [
    {
      "statement": "競合Aは新しいAPI価格を発表した。",
      "evidence_ids": ["EVD-20260507-0001"]
    }
  ],
  "assumptions": [
    {
      "statement": "価格は主要顧客の導入判断に影響する。",
      "confidence": "moderate",
      "test_method": "顧客導入事例と価格比較を次回収集する。"
    }
  ],
  "judgments": [
    {
      "statement": "競争軸は短期的に性能から価格・配布チャネルへ広がる可能性が高い。",
      "confidence": "moderate",
      "confidence_reason": "一次情報はあるが顧客反応は未確認。",
      "evidence_ids": ["EVD-20260507-0001", "EVD-20260507-0004"],
      "decision_implication": "営業資料では価格比較だけでなく導入容易性を訴求する。"
    }
  ],
  "unresolved_gaps": ["顧客側の実際の乗り換え意向は未確認。"]
}
```

## 8. Red Findings JSON

Red Findingsは、単なる反対意見ではなく、判断を弱める根拠、代替仮説、前提の弱さ、バイアスを構造化する。

```json
{
  "red_review_id": "RED-20260507-001",
  "blue_assessment_id": "BLUE-20260507-001",
  "overall_recommendation": "accept|weaken|reframe|block",
  "critical_assumptions": [
    {
      "assumption": "価格が主要な競争軸になる。",
      "risk": "顧客は価格より既存ワークフロー統合を重視する可能性がある。",
      "test": "導入事例と顧客コメントを追加収集する。"
    }
  ],
  "contradictory_evidence_ids": ["EVD-20260507-0012"],
  "alternative_hypotheses": ["HYP-002"],
  "bias_risks": ["availability_bias", "recency_bias"],
  "required_revisions": ["確信度をHighではなくModerateに下げる。"]
}
```

## 9. State Update Plan

Arbiterは直接状態を書き換えず、検証可能な更新計画を作る。

```json
{
  "state_update_plan_id": "SUP-20260507-001",
  "run_date": "2026-05-07",
  "updates": [
    {
      "target_file": "config/hypotheses.json",
      "target_id": "HYP-001",
      "field": "confidence",
      "previous_value": "low",
      "proposed_value": "moderate",
      "change_reason": "一次情報と独立裏付けが追加されたため。",
      "evidence_ids": ["EVD-20260507-0001", "EVD-20260507-0004"],
      "quality_gate_results": ["gate_source_quality:pass", "gate_corrob:pass", "gate_hypothesis_competition:pass"],
      "red_team_status": "reviewed_no_blocking_issue",
      "human_review_required": false
    }
  ]
}
```

## 10. Intelligence Product Contract

最終レポートは、読みやすさよりも、意思決定に使える構造を優先する。

```json
{
  "product_id": "DAILY-20260507",
  "product_type": "daily|flash|static|weekly",
  "audience": "business_decision_maker",
  "key_judgments": [
    {
      "judgment": "競合Aの価格戦略は短期的に市場獲得圧力を高める。",
      "confidence": "moderate",
      "evidence_ids": ["EVD-20260507-0001"],
      "facts": ["競合Aが価格改定を発表。"],
      "assumptions": ["価格は導入判断に一定影響する。"],
      "contradictions": ["導入障壁は価格以外にも存在。"],
      "decision_implication": "価格比較だけでなく導入容易性とサポート体制を訴求する。",
      "next_collection_requirements": ["顧客反応と導入事例を48時間以内に確認。"]
    }
  ],
  "overall_degradation_status": "GREEN|YELLOW_COLLECTION_GAP|RED_QUALITY_FAIL"
}
```

## 11. Validation Scriptで検査すべき項目

| 検査 | 具体内容 | 失敗時 |
|---|---|---|
| Schema Validation | 必須キー、型、列挙値を検査する。 | Job失敗。 |
| Reference Integrity | `evidence_ids` が `evidence_index` に存在する。 | Job失敗。 |
| PIR/KIQ Alignment | 判断がPIR/KIQに紐づく。 | 出力無効。 |
| Quality Consistency | High確信度が低品質単一ソースに依存していない。 | 確信度校正失敗。 |
| State Update Safety | 更新計画に前値、後値、理由、Evidence、Red状態がある。 | 状態更新禁止。 |
| Report Contract | 最終成果物に判断、根拠、不確実性、行動含意、次回収集がある。 | コミット禁止。 |

## 12. 最小実装順

最初から全スキーマを厳密に導入すると移行負荷が高いため、最低限の順序は次の通りである。

| 順序 | 導入項目 | 理由 |
|---:|---|---|
| 1 | Evidence Record | 根拠追跡が全工程の基礎になる。 |
| 2 | Screening Record | 関連性のない情報を分析へ流さない。 |
| 3 | Quality Matrix | 情報品質とソース品質を分離する。 |
| 4 | Blue/Red JSON | 判断と反証を検証可能にする。 |
| 5 | State Update Plan | Static Intelligenceの安全な更新を実現する。 |
| 6 | Product Contract | レポート品質を機械検査できるようにする。 |
