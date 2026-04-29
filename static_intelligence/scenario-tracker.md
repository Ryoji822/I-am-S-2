# シナリオ分析 — 4つの未来のどれに向かっているか

> 最終更新: 2026-04-29

AI市場の展開を、2つの軸（技術の開放度 × 性能の格差）で4つのシナリオに追跡している。

最有力は「技術は開くが勝者は出る」（SCN-002、44%）。三大クラウドAgent Platform同一週リリースとMicrosoft-OpenAI提携非排他化が、開放+格差構造を決定的に補強した [Arbiter v3.63](../state/arbiter-2026-04-29.md)。

## 現在の確率

| シナリオ | 確率 | 象限 | 前週(4/22)比 |
|---------|------|------|------------|
| **SCN-002 技術は開くが勝者は出る** | **44%** | **開放 × 格差拡大** | **+4%** |
| **SCN-003 静かな囲い込み** | **24%** | 閉鎖 × 収斂 | **-1%** |
| SCN-001 囲い込みの勝者 | 20% | 閉鎖 × 格差拡大 | -3% |
| SCN-004 誰でもAI | 12% | 開放 × 収斂 | ±0% |

| ブラックスワン | 確率 | 前回比 | 影響度 |
|--------------|------|--------|--------|
| SCN-BS-001 AI安全性大事故 | 16% | ±0% | 壊滅的 |
| SCN-BS-002 量子×AI融合 | 3% | ±0% | 根本的変化 |

## 2つの軸の意味

**X軸: AIは囲い込まれるか、開放されるか？**

AAIF（MCP+A2A、Linux Foundation配下）で標準化が完了した。MCP月間110M+ DL。Symphony OSS（OpenAI）。Agents CLI OSS（Google）。全主要AIプレイヤーがMCPに対応。（[IND-027](../config/indicators.json)、high）

Microsoft-OpenAI提携改訂が围い込みに決定的な打撃を与えた。非排他・全クラウド・IP非排他2032 [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)。OpenAI on AWS [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。単一クラウド依存が構造的に弱まった。

**Y軸: トップ企業と後発の性能差は広がるか、縮まるか？**

GPT-5.5 SOTA [INFO-032](../Information/2026-04-24/collected-raw.md#INFO-032)。Gemini 3.1 Pro MMMU-Pro 88.21% [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。ARC-AGI-3で全フロンティアモデル0%（人間100%）[INFO-059](../Information/2026-04-29/collected-raw.md#INFO-059)。格差維持の証拠が強い。

だがDeepSeek V4が$0.0036/MTokでGPT-5.5/Opus 4.7にほぼ匹敵 [INFO-038](../Information/2026-04-29/collected-raw.md#INFO-038)。Gemma 4 Arena Elo 1452。収斂方向の証拠も存在する。

## 各シナリオの詳細

### SCN-001 囲い込みの勝者（20%）— 閉鎖 × 格差拡大

1-2社が技術力で圧倒しつつ、実行環境・データ・ガバナンスで囲い込む世界。

20%に低下（3位維持）。Microsoft-OpenAI提携改訂（非排他・全クラウド）が围い込みに決定的な打撃 [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)。Symphony OSS [INFO-002](../Information/2026-04-29/collected-raw.md#INFO-002)、AAIF設立 [INFO-016](../Information/2026-04-29/collected-raw.md#INFO-016)、MCP 110M+/月DLで開放潮流が構造的に強化された。

監視指標: [IND-001](../config/indicators.json)、[IND-002](../config/indicators.json)、[IND-003](../config/indicators.json)、[IND-015](../config/indicators.json)、[IND-018](../config/indicators.json)、[IND-019](../config/indicators.json)、[IND-020](../config/indicators.json)、[IND-024](../config/indicators.json)

### SCN-002 技術は開くが勝者は出る（44%）— 開放 × 格差拡大 ★現在最有力★

AAIF標準で相互運用性は確保されるが、フロンティア性能はTier 1の3社に集中する世界。

44%に上昇（1位維持）。三大クラウドAgent Platform同一週リリースが業界構造変化の決定的証拠:

- AWS Bedrock AgentCore [INFO-027](../Information/2026-04-29/collected-raw.md#INFO-027)
- Azure Foundry Agent Service [INFO-028](../Information/2026-04-29/collected-raw.md#INFO-028)
- GCP Gemini Enterprise Agent Platform [INFO-009](../Information/2026-04-29/collected-raw.md#INFO-009)

Microsoft-OpenAI提携改訂（非排他・全クラウド）で開放+C [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)。Cisco 85/5 gap（80pt）は品質で勝者選別の実証 [INFO-030](../Information/2026-04-29/collected-raw.md#INFO-030)。GPT-5.5 SOTA + DeepSeek V4価格破壊で格差維持+開放進展が同時確認された。

監視指標: [IND-004](../config/indicators.json)、[IND-006](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-018](../config/indicators.json)、[IND-023](../config/indicators.json)、[IND-027](../config/indicators.json)、[IND-029](../config/indicators.json)

### SCN-003 静かな囲い込み（24%）— 閉鎖 × 収斂

モデル性能差は小さくなるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界。

24%で低下（2位維持）。OpenAI on AWSでマルチクラウド競争激化=単一エコ围い込みI [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。Bain分析ハードウェア分離でスイッチングコスト低下 [INFO-046](../Information/2026-04-29/collected-raw.md#INFO-046)。

だしGPT-5.5価格2倍はデータ層围い込みCとして部分支持 [INFO-033](../Information/2026-04-29/collected-raw.md#INFO-033)。収斂が起きなければSCN-001に吸収される構造的弱点は変わらない。

監視指標: [IND-007](../config/indicators.json)、[IND-008](../config/indicators.json)、[IND-009](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-015](../config/indicators.json)、[IND-017](../config/indicators.json)、[IND-019](../config/indicators.json)、[IND-020](../config/indicators.json)、[IND-022](../config/indicators.json)、[IND-024](../config/indicators.json)

### SCN-004 誰でもAI（12%）— 開放 × 収斂

性能差がなくなりオープン標準で自由に行き来できる世界。

12%で維持（4位）。DeepSeek V4 $0.0036/MTok [INFO-035](../Information/2026-04-29/collected-raw.md#INFO-035) + OSS商用90%到達 [INFO-038](../Information/2026-04-29/collected-raw.md#INFO-038) はSCN-004方向C。但し$5.2T CapEx [INFO-043](../Information/2026-04-29/collected-raw.md#INFO-043) + OpenAI+Anthropic=$242.6B（80%）[INFO-044](../Information/2026-04-29/collected-raw.md#INFO-044) で資本集中継続。分散の証拠は依然弱い。

監視指標: [IND-004](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-017](../config/indicators.json)、[IND-020](../config/indicators.json)

## ブラックスワン（低確率・高影響）

### SCN-BS-001 AI安全性大事故（16%）

Claude Mythosサイバー攻撃質的変化 [INFO-014](../Information/2026-04-29/collected-raw.md#INFO-014)。82%企業に未知AIエージェント [INFO-033](../Information/2026-04-29/collected-raw.md#INFO-033)。65%AI関連インシデント経験。大規模事故未到達。critical移行監視継続。

### SCN-BS-002 量子コンピューティング×AI融合（3%）

関連する新情報なし。

## 確率推移データ

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|---------|---------|---------|---------|--------|--------|
| 2026-04-29 | 20% | 44% | 24% | 12% | 16% | 3% |
| 2026-04-28 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-27 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-26 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-25 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-24 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-23 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-22 | 23% | 40% | 25% | 12% | 16% | 3% |
| 2026-04-21 | 23% | 39% | 26% | 12% | 16% | 3% |
| 2026-04-20 | 24% | 38% | 26% | 12% | 16% | 3% |
| 2026-04-19 | 24% | 38% | 26% | 12% | 16% | 3% |
| 2026-04-18 | 24% | 38% | 26% | 12% | 16% | 3% |
| 2026-04-17 | 24% | 37% | 27% | 12% | 16% | 3% |
| 2026-04-16 | 24% | 37% | 27% | 12% | 16% | 3% |
| 2026-04-15 | 24% | 37% | 27% | 12% | 16% | 3% |
| 2026-04-13 | 24% | 37% | 27% | 12% | 16% | 3% |
| 2026-04-12 | 23% | 37% | 28% | 12% | 16% | 3% |
| 2026-04-11 | 23% | 36% | 28% | 13% | 16% | 3% |
| 2026-04-10 | 23% | 36% | 28% | 13% | 16% | 3% |
| 2026-04-08 | 23% | 38% | 27% | 12% | 16% | 3% |
| 2026-04-06 | 24% | 37% | 26% | 13% | 14% | 3% |
| 2026-03-29 | 22% | 39% | 22% | 17% | 11% | 3% |
| 2026-03-24 | 20% | 41% | 21% | 18% | 11% | 3% |
| 2026-03-08 | 23% | 42% | 17% | 18% | 6% | 3% |

大きなトレンド: SCN-002は44%に到達。三大クラウドAgent Platform同一週リリース + Microsoft-OpenAI提携非排他化が同時に働いた。SCN-001はMicrosoft-OpenAI提携改訂で20%に低下。SCN-003は24%で2位だが、性能差非縮小と収斂前提の矛盾が深刻化。SCN-004は12%でフロンティア性能格差が壁。

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-29 | **鮮度タイムアウト対応（7日経過）**。三大クラウドAgent Platform同一週リリース・Microsoft-OpenAI提携改訂（非排他・全クラウド）・エンタープライズ実行ギャップ5独立ソース確認・DeepSeek V4価格破壊を反映。SCN-002 40→44%（+4%）・SCN-001 23→20%（-3%）・SCN-003 25→24%（-1%）に更新。確率推移データに04-23〜04-29分を追加 |
| 2026-04-22 | エンタープライズ決戦クラスター・IND-029 high移行を反映。SCN-002 37→40%に更新 |
| 2026-04-17 | 鮮度タイムアウト対応。SCN-002 36→37%に更新 |
| 2026-04-10 | スイッチングコスト定量データを反映 |
| 2026-04-08 | シナリオ順位入れ替わりを反映 |
