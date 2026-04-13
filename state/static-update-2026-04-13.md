# Static Intelligence 更新記録: 2026-04-13

## 更新サマリ

| ファイル | 更新有無 | トリガー |
|---------|---------|---------|
| `static_intelligence/google.md` | **更新** | 鮮度タイムアウト（7日経過）+ 新ベンチマークデータ |
| `static_intelligence/openai.md` | 更新なし | 6日経過（7日未満）。構造変化なし |
| `static_intelligence/anthropic.md` | 更新なし | 3日前更新済み。最新情報反映済み |
| `static_intelligence/xai.md` | 更新なし | 5日経過。本日xAI関連新規証拠0件（Arbiter判断通り） |
| `static_intelligence/bytedance.md` | 更新なし | 3日前更新済み。最新情報反映済み |
| `static_intelligence/market-overview.md` | 更新なし | 3日前更新済み。シナリオ順位変動なし |
| `static_intelligence/scenario-tracker.md` | 更新なし | 3日前更新済み。全シナリオ±0%（順位変動なし） |

## 更新詳細: google.md

**トリガー**: 鮮度タイムアウト（最終更新 2026-04-06、7日経過）+ 本日収集データにGoogle関連重要情報を含む

**更新内容**:

1. **Gemini 3.1 Pro multimodal 95.0%首位を追加**
   - マルチモーダル&グラウンデッドリーダーボードで95.0%を記録 [INFO-023](../Information/2026-04-13/collected-raw.md#INFO-023)
   - エグゼクティブサマリー、直近の動き、H-GOO-003、強み、監視ポイントに反映

2. **SWE-bench首位喪失を修正**
   - 従来「80.6%で首位獲得」→ Claude Opus 4.6（80.8%）に0.2pt差で逆転 [INFO-025](../Information/2026-04-13/collected-raw.md#INFO-025)
   - エグゼクティブサマリー、直近の動き、強みと弱み、監視ポイントに反映

3. **Gemma 4 31B MRCR v2 128K 66.4%を追加**
   - 前世代13.5%から大幅改善（約5倍）[INFO-026](../Information/2026-04-13/collected-raw.md#INFO-026)
   - H-GOO-003、強み、監視ポイントに反映

## 更新しなかった根拠

### openai.md（6日経過）
- 7日未満のため鮮度タイムアウト未発動
- 構造変化トリガーなし:
  - 仮説確度変動: H-OAI-001 ±0%（60%維持）、H-OAI-002 ±0%（56%維持）→ ±10%未満
  - 新モデルリリースなし（Codex価格変更はパッチ・価格調整であり新モデル名を伴わない）
  - CEO交代・$10B超資金調達・M&Aなし
  - I&W指標critical到達なし
- 注: ペンタゴン$200M契約（4/8）は重要だが、openai.md既存記述「DoW契約で政府市場に参入」で方向性は反映済み。具体額の追加は次回更新時または構造変化時に対応

### anthropic.md（3日経過）
- SCR確定、$30B ARR、Managed Agents GA等は4/10更新で反映済み
- 本日の確度変動: H-ANT-001 ±0%、H-ANT-002 ±0%、H-ANT-003 ±0% → トリガーなし

### xai.md（5日経過）
- 本日収集データ52件中xAI関連0件（Arbiter判断「10日+連続証拠不在」と整合）
- H-XAI-001 -1%（57%）、H-XAI-003 -1%（55%）→ ±10%未満の日常変動
- 新モデル・新製品発表なし

### bytedance.md（3日経過）
- 豆包DAU 1億突破・Seedance 2.0・Coze 2.5等は前回更新で反映済み
- HappyHorse-1.0（Alibaba）のSeedance逆転はAlibaba側の動向でありByteDance基本情報の変更なし
- AI感情陪伴規制（7/15施行）は注記済み

### market-overview.md（3日経過）
- シナリオ確率: SCN-002 37% > SCN-003 28% > SCN-001 23% > SCN-004 12%（順位変動なし）
- 価格コモディティ化+囲い込みのパラドックスはArbiter申送り事項だが、構造変化トリガーに該当しない

### scenario-tracker.md（3日経過）
- 全シナリオ±0%（Arbiter v3.49）。確率推移グラフデータの追加のみ不要（順位変動なし）

## 次回留意事項

1. **openai.md**（最終更新 4/7）→ 次回（4/14）で7日到達。ペンタゴン$200M契約・エンタープライズ収益>40%の反映を検討
2. **xai.md**（最終更新 4/8）→ H-XAI-001（57%）とH-XAI-003（55%）が構造見直しトリガーに接近。次回55%到達で仮説文見直しが必要になる可能性
