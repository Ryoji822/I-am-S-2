# Static Intelligence 更新記録: 2026-03-29

## 更新サマリー

**状態**: 構造変化を検出、3ファイル更新

## 構造変化の判定根拠

### 更新トリガー

| トリガー | 内容 | 対象ファイル |
|---------|------|-------------|
| 主力製品の終了 | OpenAI Sora終了（15ヶ月で撤退）[INFO-005] | openai.md |
| 大型資金調達 | OpenAI $120B調達完了（評価額$730B）[INFO-006] | openai.md, market-overview.md |
| シナリオ確率不一致 | scenarios.json (22/39/22/17) vs scenario-tracker.md (20/41/21/18) | scenario-tracker.md |

### 更新なしのファイル

| ファイル | 最終更新 | 判定理由 |
|---------|---------|---------|
| anthropic.md | 2026-03-28 | 新規構造変化なし（1日前更新済み） |
| google.md | 2026-03-28 | Gemini 3.1 Flash Liveは既に反映済み |
| xai.md | 2026-03-25 | Grok 4.20は既に反映済み |
| bytedance.md | 2026-03-24 | 新規構造変化なし（5日前だが重要情報なし） |

## 更新内容詳細

### openai.md

**更新セクション**: 全体書き直し

**主な変更点**:
- 調達額: $110B → $120B（評価額$730B）
- 収益: $25B → $13.1B
- ChatGPT週間アクティブユーザー9億人追加
- Sora終了（15ヶ月で撤退）を追加
- OpenAI Foundation $1B投資追加
- H-OAI-003確度 2%→1%に低下
- 確度表示をヘッダーに追加

**引用**:
- [INFO-005](../Information/2026-03-29/collected-raw.md#INFO-005): Sora終了
- [INFO-006](../Information/2026-03-29/collected-raw.md#INFO-006): $120B調達
- [INFO-004](../Information/2026-03-29/collected-raw.md#INFO-004): OpenAI Foundation

### market-overview.md

**更新セクション**: プレイヤー一覧、市場動向、I&W監視指標

**主な変更点**:
- OpenAI情報更新（$120B、$13.1B ARR、Sora終了）
- AI ROI二極化データ追加（92%正のROI vs 40%キャンセルリスク）
- 7社SDK同時更新を記録
- セキュリティ事件連鎖（OpenClaw 135K暴露、Meta Sev-1）追加
- IND-024 monitoring→elevated反映

### scenario-tracker.md

**更新セクション**: 確率分布、各シナリオ詳細、確率推移データ

**確率変更**:
- SCN-001: 20% → 22% (+2pt) — 資金集中加速
- SCN-002: 41% → 39% (-2pt)
- SCN-003: 21% → 22% (+1pt) — データ囲い込み加速
- SCN-004: 18% → 17% (-1pt)

**変更根拠**:
- OpenAI $120B調達、xAI-SpaceX $1.25兆統合で集中化加速
- Grok x_search内蔵、Google Personal Intelligence無料化でデータ囲い込み加速
- 7社SDK同時更新で競争激化（反証）

## 品質確認

- [x] 引用リンクが正しく付与されている
- [x] indicators.jsonへのリンクがMarkdown形式
- [x] シナリオ確率合計100%（22+39+22+17=100）
- [x] 変更履歴テーブルに1行要約を記録
- [x] 取り消し線による差分パッチは使用していない

## 次回申し送り事項

1. **bytedance.md鮮度**: 5日未更新。次回はSeed 2.0第三者ベンチマーク結果や著作権訴訟進展を確認
2. **KIQ-RED-005完了後**: IND-024（AI実効性）の最終評価
3. **KIQ-RED-007完了後**: ベンチマーク多面化の分析精度向上
