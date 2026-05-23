# Static Intelligence 更新記録: 2026-05-23

## 更新判定

Arbiter v3.86 の統合判断を基に、以下の構造的変化を判定した。

### 更新した構造的変化

1. **Anthropic M&A + 収益急増 + 因果チェーンA-2確認 (anthropic.md)**: Stainless買収(INFO-004 A-3)、WSJ $10.9B収益130%急増(INFO-052 A-2)、Pentagon安全拒否→SCR因果チェーンA-2品質確認(INFO-069 A-2)、KPMG 276K従業員統合(INFO-010 A-3)、Project Glasswing 10K脆弱性(INFO-003 A-3)、控訴裁SCR懐疑(INFO-034 A-2)。H-ANT-001 47%整合性修正(旧ファイル49%→47%)。鮮度3日タイムアウト。

2. **Google围い込み15→17件 + 仮説確度変動 (google.md)**: Managed Agents API(INFO-007)とGoogle I/O包括分析「全テック企業に宣戦布告」(INFO-067)で围い込み2件追加。H-GOO-001 53→54%(+1%)、H-GOO-002 36→35%(-1%)。Chrome DevTools for Agents v1新製品(INFO-022)。鮮度3日タイムアウト。

3. **シナリオ確率変動 (scenario-tracker.md + market-overview.md)**: SCN-001 17→16%(-1%)、SCN-004 20→21%(+1%)。Epoch AI 9x-900x/年価格下落(INFO-065)で围い込み価値基盤侵食。推移表に2026-05-23行追加。順位不変(SCN-003>#2>#4>#1)。

### 更新しなかった日常変動

- H-BTD-002 55→54% (-1%): Epoch AI価格下落の影響。±10%未満
- H-CAR-001 27→28% (+1%): ±10%未満
- H-GOV-001 52% (±0%): Blue 4R連続+1%提案全て否認。変動なし
- H-OAI-001 62% (±0%): 変動なし

## 更新したファイル

| ファイル | 更新種別 | 変更内容 |
|---------|---------|---------|
| `static_intelligence/anthropic.md` | 全面書き直し | $10.9B収益+KPMG 276K+Stainless買収+Pentagon因果A-2+控訴裁懐疑+Glasswing 10K+固定料金終了を反映。H-ANT-001 49%→47%整合性修正。政府対立時系列に2026-05-21/22追加 |
| `static_intelligence/google.md` | 全面書き直し | 围い込み15→17件+Chrome DevTools v1+Managed Agents API+I/O包括分析+Goldman Sachs 66GW+Epoch AI価格下落を反映。H-GOO-001 53→54%+H-GOO-002 36→35% |
| `static_intelligence/market-overview.md` | 全面書き直し | 企業ファイル変更との整合性更新。SCN-001 16%+SCN-004 21%反映。全20仮説確度一致確認。プレイヤー表更新(Anthropic $14B/KPMG/Stainless、Google I/O 17件、xAI Grok Build 0.1) |
| `static_intelligence/scenario-tracker.md` | 全面書き直し | 推移表に2026-05-23行追加(21日分)。SCN-001 16%+SCN-004 21%反映。Epoch AI 9x-900x/year新観測を各シナリオに統合。Arbiter v3.86参照更新 |

## 更新しなかったファイル

| ファイル | 理由 |
|---------|------|
| `static_intelligence/openai.md` | 最終更新2026-05-22(1日前)。H-OAI-001 ±0%(62%)。新規製品なし、M&Aなし、構造的変化なし |
| `static_intelligence/xai.md` | 最終更新2026-05-22(1日前)。H-XAI全系±0%。軽微な製品更新のみ |
| `static_intelligence/bytedance.md` | 最終更新2026-05-21(2日前)。H-BTD-002 55→54%(-1%)は±10%未満。7日鮮度タイムアウト未到達 |

## 備考

- H-ANT-001の旧ファイル(49%)とhypotheses.json v3.86(47%)の不整合を修正した。Arbiter v3.85→v3.86間で±0%だったが、旧ファイルがv3.84時点の49%を維持していた
- Epoch AI 9x-900x/年価格下落(INFO-065)は围い込み系シナリオ(SCN-001/003)と開放系シナリオ(SCN-004)双方に影響する「二刃の剣」として分析
- 次回更新トリガー候補: bytedance.md鮮度タイムアウト(2026-05-28到達予定)、H-ANT-001 20R目上限条件見直し強制、围い込み20件閾値接近(現在17件)
