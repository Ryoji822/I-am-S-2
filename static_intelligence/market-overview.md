# AI市場の現在地
> 最終更新: 2026-04-29

安いAIは誰でも使える。だが最先端を作れるのは3社だけ——市場はその構造に向かっている（SCN-002、44%）。2026年4月最終週、その構造を補強する3つの出来事が同時に起きた。三大クラウドが同一週にAgent Platformを正式リリースし [INFO-009](../Information/2026-04-29/collected-raw.md#INFO-009) [INFO-027](../Information/2026-04-29/collected-raw.md#INFO-027) [INFO-028](../Information/2026-04-29/collected-raw.md#INFO-028)、Microsoft-OpenAI提携が非排他化され [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)、エンタープライズ実行ギャップが5独立ソースで構造的に確認された [INFO-030](../Information/2026-04-29/collected-raw.md#INFO-030) [INFO-031](../Information/2026-04-29/collected-raw.md#INFO-031) [INFO-012](../Information/2026-04-29/collected-raw.md#INFO-012)。

価格は二極化している。GPT-5.5は前世代の2倍（$5/$30 per MTok）に値上げし [INFO-033](../Information/2026-04-29/collected-raw.md#INFO-033)、DeepSeek V4は$0.0036/MTokでOpenAI比97%安 [INFO-035](../Information/2026-04-29/collected-raw.md#INFO-035)。中間帯が消えつつある。

## プレイヤー一覧

| 企業 | 主力 | 資金 | 今の位置 |
|------|------|------|---------|
| OpenAI | GPT-5.5、Codex（4M WAU）、**Symphony OSS**、Agents SDK | $122B調達（$852B評価額、$13.1B ARR） | **Microsoft提携改訂で全クラウド展開可能に** [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)。**OpenAI on AWS** [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。ベンチマーク首位 |
| Anthropic | Claude Opus 4.7、Claude Code、Managed Agents、Mythos | **Google $40B** + Amazon $25B（$350B評価値） | **$30B ARR**（OpenAI逆転確認）[INFO-041](../Information/2026-04-29/collected-raw.md#INFO-041)。エンタープライズ40%シェア。**SCR仮差し止め** |
| Google | Gemini 3.1シリーズ、**Gemini Enterprise Agent Platform**、Agents CLI | 自己資金 + **Anthropic $40B投資** | **MMMU-Pro 88.21%首位**。**$750Mパートナーファンド**。Salesforce/SAP/SAP提携 [INFO-018](../Information/2026-04-29/collected-raw.md#INFO-018)。Anthropic $40B投資で二面構造 |
| xAI | Grok 4.20シリーズ、**Grok Voice Think Fast 1.0** | $20B Series E（SpaceX $1.25兆合算） | STT WER 6.9%業界最良。**Pentagon GenAI.mil統合**（120万ユーザー） |
| ByteDance | **豆包2.0**（多模態Agent）、Seed 2.0、Seedance 2.0 | 非公開（評価額$520B） | **MAU 3.45億**（中国首位）[INFO-066](../Information/2026-04-29/collected-raw.md#INFO-066)。価格1/10。2025年純利益70%+減少。**DeepSeek V4価格破壊の逆風** |
| Meta | Llama 4、スーパーインテリジェンスチーム | 自己資金 + CoreWeave $21B契約 | OSS性能ギャップ閉じる方向。8,000人削減 |

## 今、市場で何が起きているか

### 三大クラウドAgent Platform同一週リリース — 主戦場が移った

2026年4月22-28日の1週間で、AWS Bedrock AgentCore [INFO-027](../Information/2026-04-29/collected-raw.md#INFO-027)、Azure Foundry Agent Service [INFO-028](../Information/2026-04-29/collected-raw.md#INFO-028)、GCP Gemini Enterprise Agent Platform [INFO-009](../Information/2026-04-29/collected-raw.md#INFO-009) が相次いで正式リリースされた。Agent戦争の主戦場がSDK/API層からプラットフォーム層に移行した。3クラウドが同時に動いたことは、エージェント技術がエンタープライズ実用の臨界点を通過したことを示唆する。

### Microsoft-OpenAI提携改訂 — 業界構造が変わった

OpenAI製品は全クラウドで提供可能になった。MicrosoftのIPライセンスは2032年まで非排他化 [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)。囲い込みシナリオ（SCN-001）を弱体化させ、開放+格差シナリオ（SCN-002）を強化する決定的な変数。

### エンタープライズ実行ギャップの構造化

5つの独立ソースが同じ結論に到達した:

- **Cisco**: 85%パイロット、5%本番（80pt gap）[INFO-030](../Information/2026-04-29/collected-raw.md#INFO-030)
- **S&P 500**: 25%のみAI ROI証明可能 [INFO-031](../Information/2026-04-29/collected-raw.md#INFO-031)
- **Fortune 500**: 95%がAI Level 1で停滞
- **Microsoft**: 「ほぼ本番で動いていない」[INFO-012](../Information/2026-04-29/collected-raw.md#INFO-012)
- **PwC**: 83%期待、27%本番稼働

パイロット→本番の構造的障壁が確定した。([IND-026](../config/indicators.json)、elevated→high移行が次回濃厚）

### 価格二極化 — 中間帯消滅

GPT-5.5は$5/$30（前世代2倍）[INFO-033](../Information/2026-04-29/collected-raw.md#INFO-033)。DeepSeek V4は$0.0036/MTok（OpenAI比97%安）[INFO-035](../Information/2026-04-29/collected-raw.md#INFO-035)。トークン価格は2021年から年10倍低下 [INFO-035](../Information/2026-04-29/collected-raw.md#INFO-035)。最高性能にプレミアムを払う層と、コスト最優先で性能は十分という層に二極化している。

### 第一波AI自動化の「教訓フェーズ」

Klarnaが700人AI代替を逆転、サービス品質低下で人間再雇用 [INFO-048](../Information/2026-04-29/collected-raw.md#INFO-048)。Forrester: AI自動化は米国6%の職場のみ（2030年まで）[INFO-048](../Information/2026-04-29/collected-raw.md#INFO-048)。広告AI「計算が合わない」[INFO-047](../Information/2026-04-29/collected-raw.md#INFO-047)。

反対方向のシグナルも並存する。Meta 8,000人削減 [INFO-050](../Information/2026-04-29/collected-raw.md#INFO-050)。KPMG 77%が新人採用方針変更 [INFO-049](../Information/2026-04-29/collected-raw.md#INFO-049)。矛盾シグナルの並存自体が「過渡期」を示す。

### Google $40B Anthropic投資で二面構造化

Googleが最大$40BをAnthropicに投じた [INFO-041](../Information/2026-04-29/collected-raw.md#INFO-041)。即時$10B、$350B評価値。Google自身がGeminiを推進しつつ、Anthropicにも巨額投資する構造。AI市場の競争が単一企業の枠を超えている。

### インフラ過熱と物理的制約

AI DC CapExが2030年までに$5.2Tに到達する予測 [INFO-043](../Information/2026-04-29/collected-raw.md#INFO-043)。NVIDIAがOpenAIに最大$100B投資予定 [INFO-043](../Information/2026-04-29/collected-raw.md#INFO-043)。資本流入vs物理的制約のギャップが確定的継続。（[IND-029](../config/indicators.json)、**high**）

### 「書く」から「評価する」への大転換

Stanford: 22-25歳開発者雇用20%低下 [INFO-052](../Information/2026-04-29/collected-raw.md#INFO-052)。プログラマー雇用2023-2025年で27.5%減少。ジュニアロール「基本的に消滅」。GitHubコード50%+がAI生成/支援 [INFO-051](../Information/2026-04-29/collected-raw.md#INFO-051)。（[IND-022](../config/indicators.json)、**high**）

## 寡占と分散のどちらに向かうか

**集中に向かう力**: 三大クラウドAgent Platform同時リリース。Microsoft提携改訂でOpenAI全クラウド展開。エンタープライス3社で88%シェア。Q1 AI投資$242B。OpenAI+Anthropic=$242.6B（AI 50の80%）[INFO-044](../Information/2026-04-29/collected-raw.md#INFO-044)。

**分散に向かう力**: AAIF標準化。MCP 110M+/月DL。Symphony OSS。Gemma 4。DeepSeek V4 671B MoE OSS。ByteDance DeerFlow OSS。

現時点では「技術は開くが、性能トップは集中する」（SCN-002、44%）が最有力。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | 前世代比30%超の性能向上 | GPT-5.4 Pro ARC-AGI-2 83.3%。Gemini MMMU-Pro 88.21% | **high** approaching |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | OpenAI+Anthropic=$242.6B（80%）[INFO-044](../Information/2026-04-29/collected-raw.md#INFO-044) | **high** |
| [IND-013](../config/indicators.json) AI安全性事故 | 大規模なAI関連事故 | Claude Mythos質的変化 [INFO-014](../Information/2026-04-29/collected-raw.md#INFO-014)。82%企業に未知AIエージェント [INFO-033](../Information/2026-04-29/collected-raw.md#INFO-033) | **high** rising |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理にシフト | ジュニア開発者採用20%低下 [INFO-052](../Information/2026-04-29/collected-raw.md#INFO-052)。GitHubコード50%+ AI生成 [INFO-051](../Information/2026-04-29/collected-raw.md#INFO-051) | **high** rising |
| [IND-026](../config/indicators.json) エージェント本番環境到達率 | エージェントの本番稼働成功率 | Cisco 85/5（80pt gap）[INFO-030](../Information/2026-04-29/collected-raw.md#INFO-030)。S&P 25% ROI。Microsoft「ほぼ本番なし」[INFO-012](../Information/2026-04-29/collected-raw.md#INFO-012) | elevated rising（high移行濃厚） |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | MCP/A2A等のオープンスタンダード採用率 | AAIF設立。MCP 110M+/月DL。Symphony OSS。SKILL.md 5主要ツール | **high** rising |
| [IND-028](../config/indicators.json) AGI到達度指標 | 主観-客観乖離 | ARC-AGI-3: 人間100% vs AI <1% [INFO-059](../Information/2026-04-29/collected-raw.md#INFO-059)。AGI予測6年で27年短縮 | elevated rising |
| [IND-029](../config/indicators.json) AIインフラ制約 | 計算能力投資の物理的限界 | AI DC CapEx $5.2T by 2030 [INFO-043](../Information/2026-04-29/collected-raw.md#INFO-043)。NVIDIA $100B OpenAI投資予定 | **high** rising |
| [IND-030](../config/indicators.json) AI能力とリスクの二面性 | 高性能モデルが最もリスク高い | Collin Burns更迭4日 [INFO-064](../Information/2026-04-29/collected-raw.md#INFO-064)。Mythosサイバー質的変化 [INFO-014](../Information/2026-04-29/collected-raw.md#INFO-014) | elevated rising |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-29 | **鮮度タイムアウト対応（7日経過）**。三大クラウドAgent Platform同一週リリース・Microsoft-OpenAI提携改訂・エンタープライズ実行ギャップ5独立ソース確認・価格二極化・Google $40B Anthropic投資・第一波AI自動化教訓フェーズ・AGI主観-客観乖離を反映して全面書き直し。SCN-002 40→44%に更新 |
| 2026-04-22 | エンタープライズ決戦クラスター・インフラ過熱-制約確定的化を反映して全面書き直し |
| 2026-04-17 | 鮮度タイムアウト対応。72時間4社同時エージェントリリースを反映 |
| 2026-04-10 | Anthropic $30B ARR・SCR確定を反映 |
| 2026-04-08 | シナリオ順位入れ替わり・MCP二面性を追加 |
