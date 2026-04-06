# Static Intelligence 更新記録: 2026-04-06

## 更新判定: 構造変化あり

Arbiterファイル（`state/arbiter-2026-04-06.md`）が存在しないため、収集データから直接構造変化を判定。

### 構造変化の根拠

| トリガー | 内容 | 対象ファイル |
|---------|------|-------------|
| フロンティアモデル新規リリース | Gemini 3.1 Flash-Lite/Flash Live、Gemma 4 | google.md |
| M&A（$400M） | AnthropicがCoefficient Bioを$400Mで買収 | anthropic.md |
| 基本情報変更 | Doubao日次トークン120兆、DAU 1.45億 | bytedance.md |
| 鮮度タイムアウト（7日以上未更新） | market-overview.md、scenario-tracker.md | 各ファイル |

### 更新したファイル

| ファイル | 更新内容 |
|---------|---------|
| `static_intelligence/google.md` | Gemma 4（Arena Elo 1452、AIME 89.2%）、Gemini 3.1 Flash-Lite/Flash Live、Search Live 200カ国、Gemini API Flex/Priorityティアを追加 |
| `static_intelligence/anthropic.md` | Coefficient Bio $400M買収、シドニーオフィス開設（APAC 4拠点）、Claude for Financial Services/Life Sciences、Claude Codeソース流出、Pentagonサプライチェーンリスク指定・連邦判事一時差止を追加 |
| `static_intelligence/bytedance.md` | Doubao日次トークン120兆（2年で1000倍）、DAU 1.45億、Seedance 2.0 API公開テスト、Coze MCP対応、中国規制を追加 |
| `static_intelligence/market-overview.md` | 上記全情報を統合。IND-027新規指標を反映 |
| `static_intelligence/scenario-tracker.md` | 鮮度タイムアウト対応。シナリオ確率は±0%維持（Arbiter未完了のため） |

### 更新しなかったファイル

| ファイル | 理由 |
|---------|------|
| `static_intelligence/openai.md` | 最終更新2026-03-29（8日前）。INFO-009（Codex価格変更）は「価格体系変更」だが、既存トレンドの延長。新モデルリリースなし。7日タイムアウトを超えているが、Arbiter判断待ちで構造変化の確定判定なし |
| `static_intelligence/xai.md` | 最終更新2026-04-01（5日前）。鮮度タイムアウト未到達。新規構造変化なし |

## 主な追加情報（INFO-001〜033）

### 新モデルリリース
- **INFO-005**: Gemini 3.1 Flash-Lite（最速最安価）、Flash Live（ComplexFuncBench Audio 90.8%）
- **INFO-006**: Gemma 4（Arena Elo 1452、AIME 89.2%、LiveCodeBench 80.0%、Apache 2.0）

### M&A
- **INFO-013**: AnthropicがCoefficient Bioを$400M（株式取引）で買収。ライフサイエンス領域の垂直統合

### 基本情報変更
- **INFO-001**: Anthropicシドニーオフィス開設（APAC 4拠点目）
- **INFO-002**: Claude for Financial Services（NBIM 20%生産性向上）
- **INFO-003**: Claude for Life Sciences（Sonnet 4.5 Protocol QA 0.83）
- **INFO-024**: Doubao日次トークン120兆（2年で1000倍）、DAU 1.45億
- **INFO-025**: CozeがMCPプロトコル対応

### 価格体系変更
- **INFO-009**: OpenAI Codexがトークン課金に移行
- **INFO-010**: Gemini APIにFlex/Priorityティアを導入

### 規制・政策
- **INFO-008**: PentagonがAnthropicをサプライチェーンリスク指定、連邦判事が一時差止
- **INFO-022**: 中国がデジタルヒューマン規制、子供向け没頭型AIサービス禁止

### セキュリティ
- **INFO-007**: Claude Codeソース流出（512,000行、npmリリースにソースマップ誤同梱）

## 次回の更新判断

Arbiterファイル（`state/arbiter-2026-04-06.md`）が作成された後、以下を再評価:
- シナリオ確率の変更要否
- 仮説確度の変更要否
- OpenAIファイルの更新要否（Codex価格変更の構造変化判定）
