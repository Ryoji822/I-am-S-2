# Static Intelligence 更新記録: 2026-05-26

## 判定: 本日更新なし

Arbiter v3.89 の確度変更は全5件が -1% であり、「更新してはいけない日常変動」に該当するため、static_intelligence/ の更新は行わない。

## 構造変化判定の根拠

| 判定基準 | 本日の状況 | 判定 |
|---------|-----------|------|
| 仮説の新設または棄却 | なし。H-OAI-001 60%・H-ANT-001 45%・H-XAI-002 62%・H-XAI-004 55%・H-BTD-002 52% 全て -1% | 更新不要 |
| シナリオ順位の入れ替わり | なし。SCN-001 15%・SCN-002 27%・SCN-003 37%・SCN-004 21% 全件 ±0% | 更新不要 |
| 企業基本情報の事実変更 | なし。CEO交代・$10B超資金調達・主力製品発表/終了・M&Aなし | 更新不要 |
| I&W指標がcritical到達 | なし。IND-013/026/027/029/030 全て high 維持・critical未到達 | 更新不要 |
| フロンティアモデルの新規リリース | なし。Grok Build CLI は既に xai.md (2026-05-22) で coverage 済み。Gemini 3.5 Flash は google.md (2026-05-23) で coverage 済み | 更新不要 |
| Arbiter による明示的更新指示 | なし | 更新不要 |
| 鮮度タイムアウト (7日以上) | 該当なし。最古: bytedance.md 5日 (2026-05-21) | 更新不要 |

## 確度変更サマリ (config のみ更新、static は不変更)

| 仮説ID | 前回 → 現在 | 変化 |
|--------|-----------|------|
| H-OAI-001 | 61% → 60% | -1% |
| H-ANT-001 | 46% → 45% | -1% |
| H-XAI-002 | 63% → 62% | -1% |
| H-XAI-004 | 56% → 55% | -1% |
| H-BTD-002 | 53% → 52% | -1% |

## 注目すべき新規証拠 (日次レポートで追跡、static は不変更)

- [INFO-006](../Information/2026-05-26/collected-raw.md#INFO-006) Reuters A-2: Grok 連邦政府での採用 3/400+ 件。xAI の政府・エンタープライズ市場苦戦の直接証拠 (H-XAI-002・H-XAI-004 の I)
- [INFO-025](../Information/2026-05-26/collected-raw.md#INFO-025) WSJ A-2: Anthropic $10.9B 収益・130% 増・初営業利益 (H-ANT-001・H-ANT-002 の C)
- [INFO-018](../Information/2026-05-26/collected-raw.md#INFO-018) MCP RC ステートレス A-3: 15,930+ サーバー (IND-027 high/rising の根拠)
- [INFO-019](../Information/2026-05-26/collected-raw.md#INFO-019) AI 大統領令延期 A-2: リスク治理後退 (IND-030 high/rising の根拠)
- [INFO-038](../Information/2026-05-26/collected-raw.md#INFO-038) ByteDance $12B+ AI 投資 C-3: 3x YoY (IND-029 high/rising の根拠)

## 次回更新の潜在的トリガー

- bytedance.md: 2026-05-28 に鮮度タイムアウト (7日) 到達。重要情報が含まれていれば更新が必要
- openai.md / xai.md: 2026-05-29 に鮮度タイムアウト到達
- Arbiter 次回議題「H-ANT-001 上限条件見直し」「H-GOO-001 4R 条件」の結果次第で構造変化の可能性
- 2026-07-28 MCP リリース前後の SCN-001/003 全面再評価予約済み
