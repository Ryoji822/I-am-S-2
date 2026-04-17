# Static Intelligence 更新記録: 2026-04-17

## 更新判定: あり（5ファイル更新、2ファイル更新なし）

## 更新トリガー

| ファイル | トリガー | 種別 |
|---------|---------|------|
| anthropic.md | Claude Opus 4.7 GA（frontier model release）+ 7日鮮度タイムアウト | 構造変化 + 鮮度 |
| openai.md | Codex App大幅アップデート（desktop control・browser・memory・111 plugins・heartbeats・SSH）= 主力製品発表 | 構造変化 |
| xai.md | 9日鮮度タイムアウト + Voice Agent API（製品発表）+ 仮説確度陈腐化 | 鮮度 + 製品発表 |
| market-overview.md | 7日鮮度タイムアウト + 72時間4社同時エージェントインフラリリース | 鮮度 + 市場イベント |
| scenario-tracker.md | 7日鮮度タイムアウト + 確率データ更新（4/11-4/17） | 鮮度 |

## 更新なしのファイル

| ファイル | 理由 |
|---------|------|
| google.md | 最終更新4/13（4日前）。新規frontier model releaseなし。Gemini CLI subagents・Flash TTSは拡張機能だが主力製品発表に該当しない |
| bytedance.md | 最終更新4/10（7日前）だが鮮度タイムアウト条件の「重要情報」に該当する新規ByteDance情報なし。OpenClaw関連はC-3情報源 |

## 更新内容サマリー

### anthropic.md
- Claude Opus 4.7 GA追加（CursorBench 70%、XBOW 98.5%、Cyber Verification Program新設）
- Agent SDK TypeScript Opus 4.7対応（MCP per-tool permission_policy）追加
- Narasimhan取締役任命追加
- Opus 4.7推奨ワークフロー（委譲型）・System card透明性プロセス追加
- H-ANT-001 52%・H-ANT-002 71%・H-ANT-003 7%を確認・反映

### openai.md
- Codex App大幅アップデート（desktop control・browser・memory・111 plugins・heartbeats・multi-terminal・SSH・画像生成）追加
- GPT-5.3-Codex 25hr連続稼働・METR約7ヶ月倍増期間追加
- Agents SDK 7社サンドボックスパートナー（Blaxel/Cloudflare追加）反映
- H-OAI-001 60→61%に更新
- タイムライン・戦略方向性・SWOT・I&W監視ポイントを書き直し

### xai.md
- Voice Agent API（MCP・x_search・OpenAI Realtime API互換・20+言語）追加
- H-XAI-001 62→55%（構造見直しトリガー発動）
- H-XAI-002 66→65%
- H-XAI-003 58→52%（medium下限接近）
- 代替仮説再定式化の必要性を追記

### market-overview.md
- 72時間4社同時エージェントインフラリリース（4/15-17）を新セクションで追加
- 自律型エージェント長時間稼働の壁突破（METR 7ヶ月倍増期間）を新セクションで追加
- プレイヤー表を最新情報に更新
- SCN-002 36→37%・SCN-003 28→27%に更新
- I&W指標を最新値に更新

### scenario-tracker.md
- 確率推移データに4/11-4/17分を追加
- 72時間同時リリース波をSCN-002補強として記述
- SCN-003の収斂前提と性能差非縮小の矛盾を強調
- SCN-001 23→24%・SCN-002 36→37%・SCN-003 28→27%・SCN-004 13→12%に更新

## 備考
- 本日のArbiter確度変更は2件（H-OAI-001 +1%、H-XAI-003 -1%）のみで、いずれも±10%未満の微動
- シナリオ確率変動は順位を変えない範囲（SCN-002 +1%、SCN-003 -1%、SCN-001 +1%、SCN-004 -1%）
- 更新の主因はフロンティアモデルリリース（Opus 4.7）・主力製品発表（Codex大幅アップデート）・鮮度タイムアウト
