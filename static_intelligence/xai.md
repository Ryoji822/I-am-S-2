# xAI → SpaceXAI

> 最終判断更新: 2026-08-14
> 全体確信度: 測定不能（[H-XAI-004](../config/hypotheses.json) indeterminate維持）
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Grok Gov Modelのガードレール内容・Cursor統合後のGrok固有採用分離も非公開。DL/API呼び出し量の時系列データが途絶状態。KIQ-MIL-001は53R/54R連続不在。エンタープライズ採用定量データが39R以上連続完全不在（[H-XAI-004](../config/hypotheses.json) 復帰条件未到達）。Grok 4.6が長時間実行エージェント向けモデルとしてリリースされ（[INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) A-1）、Artificial Analysis Intelligence Index（9ベンチマーク複合）でGPT-5.6 Solと同等性能を主張する（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3）。agentic RL（コーディング/Web開発/CAD/カーネル最適化）・自己テスト・検証強化・Extra High推論レベル追加。API価格$2/$6はGrok 4.5と同等。Grok Bot（[INFO-003](../Information/2026-08-14/collected-raw.md#INFO-003) A-3）・Imagine Image 2.0・Imagine Video 1.5 with Referencesも同時期に展開。Grok BuildはMCP全社対応製品群に含まれた（[IND-027](../config/indicators.json) v4.66）。但しIntelligence Index同等の主張はxAI自家評価でありArtificial Analysis独立出版ではない。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 59% medium ±0%（v4.66）
> 主参照: [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はxAIを「Grok 4.6でフロンティア性能への追従を主張し始めたが、エンタープライズ採用の定量証拠が構造的に欠落したままの企業」と読んでいる。Grok 4.6は長時間実行エージェント向けに設計され（[INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) A-1）、コーディング/Web開発/CAD/カーネル最適化にまたがるagentic RLと自己テスト・検証強化を特徴とする。特筆すべきは、xAIがArtificial Analysis Intelligence Index（9ベンチマーク複合）でGPT-5.6 Solと同等性能に到達したと主張する点である（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3）。Grok 4.5の時代には一般知能スコアで4位でありトップパフォーマーの議論に含まれていなかった。もしこの主張が独立評価で確認されれば、Grokの「真剣な作業」からの除外状況に変化が生じうる。但し現時点ではxAIの自家評価であり、LMSpeed・Vision Arena等の独立ランキングでのGrok 4.6スコアは未公開である。同時期にGrok Bot（[INFO-003](../Information/2026-08-14/collected-raw.md#INFO-003) A-3）・Imagine Image 2.0・Imagine Video 1.5 with Referencesが展開され、Grok Buildはセッション管理・フック・MCP統合を備えた。これらの製品展開の広がりは観測期間中で最大である。だがエンタープライズ採用の直接定量データ（WAU/DAU・F500導入率・企業契約数）は39R以上連続で不在であり、availability≠adoptionの構造は不変である。もしGrok固有の採用定量データが初めて公開されれば、この「測定不能」の判断は変わる。

[H-XAI-004](../config/hypotheses.json) はindeterminate/52%で±0%（v4.66）。Grok 4.6のagentic RL実証（[INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) A-1）とIntelligence Index同等主張（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3）は技術的広がり（C方向）の材料として観測期間中で最も強力である。Grok BuildがMCP全社対応製品群に含まれた（[IND-027](../config/indicators.json) v4.66）。但しエンタープライズ採用定量データ39R以上完全不在・フレームワーク比較13種で主要枠外（[INFO-013](../Information/2026-08-10/collected-raw.md#INFO-013) C-2）・Grok 4.6独立ベンチマーク未公開という3つの制約がI方向に作用し、復帰条件（定量データ観測）には到達していない。

## 1. コア判断

全体確信度は測定不能に置く。理由は一つで、エンタープライズ採用の定量データが39R以上連続で完全に不在だからだ。フロンティア4社（OpenAI・Anthropic・Google・xAI）のうち、xAIだけが採用規模を示す数値を一度も公開していない。この不在を「不採用の証拠」と断定することは正常性バイアスの逆方向に倒れるが、同時に「戦略的非公開」と charitable に解釈する根拠もない。だから確信度ではなく「測定不能」と書く。

### Grok 4.6とエージェント特化の戦略シフト

Grok 4.6は長時間実行エージェント向けに設計されたモデルとしてリリースされた（[INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) A-1）。推論・コーディング・技術概念のcurated dataによる追加訓練とSFT軌跡再生成を実施し、コーディング/Web開発/CAD/カーネル最適化にまたがるagentic RLを適用した。タスク中の自己テスト・検証パターンが強化され、Extra High推論レベルが追加された。Cursor・Grok Build・APIで即時利用可能であり、Grok BuildとCursorでは無料枠が2倍に拡大された（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3）。API価格はGrok 4.5と同等の$2/1M入力・$6/1M出力である。Grok 4.20というmulti-agent variantの存在も確認された（[INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089)）。

このリリースの戦略的意味は二つの側面を持つ。第一に、xAIがArtificial Analysis Intelligence Index（9ベンチマーク複合）でGPT-5.6 Solと同等性能に到達したと主張している点である。Grok 4.5の時代には、Artificial Analysis一般知能スコアでGrok 4.5は4位（Claude Fable 5・GPT-5.5・Claude Opus 4.8に次ぐ）であり、会計ベンチマーク特化型の強みと汎用知能での相対的劣位が共存していた。Grok 4.6がこの汎用知能格差を閉じたとすれば、Grokの性能プロファイルは質的に変化する。但し、この主張はxAIの自家評価に基づくものであり、Artificial Analysis自身の独立出版ではない。独立検証が保留中である。

第二に、Grok 4.6はエージェント特化型モデルとしての戦略的位置を明確にした。長時間実行エージェントと自己テスト・検証の強化は、コーディング支援からCAD設計、カーネル最適化まで、エージェントが複数ステップにわたって自律的にタスクを完遂する領域を対象としている。これは汎用フロンティアモデル（GPT-5.6 Sol・Claude Opus 5等）との差別化軸として機能しうる。だが、エージェント特化の価値をエンタープライズ市場で実証する定量データ（Grok固有のエージェント利用量・完了率・企業契約数）は一切公開されていない。

### 製品エコシステムの広がりと採用データの不在

Grok 4.6のリリースと並行して、製品エコシステムは観測期間中で最も広く展開された。Grok Bot（[INFO-003](../Information/2026-08-14/collected-raw.md#INFO-003) A-3）は独自のコンピュータ環境を持ち24時間稼働するAIチームメイトの早期ベータであり、SuperGrok Heavy・Cursor Ultra・Cursor Teams Premiumの加入者向けにデスクトップ・iOSで提供される。エンタープライズはウェイティングリストである。Imagine Image 2.0・Imagine Video 1.5 with Referencesも同時期に展開された（[INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) A-1）。Grok Buildはセッション管理・フック・MCP統合を備えたエージェントコーディングツールとして進化し、MCP全社対応製品群に含まれた（[IND-027](../config/indicators.json) v4.66）。

これらは前回更新で確認したGrok Build公式docs化（[INFO-011](../Information/2026-08-10/collected-raw.md#INFO-011) A-3）・Grok Build OSS・Voice Think Fast 2.0・Plugin Marketplace・GitHub Copilot/Bedrock/Databricks統合・Anthropicコンピュート提携の延長線上にある製品展開である。製品の出荷速度は確実に上がっている。

だが、GitHub Copilotが約20Mユーザー・職場導入率29%、Cursorが$2B ARRに到達した（[INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) B-2）のと対照的に、Grok固有のユーザー数・契約数・利用率は一切公開されない。Claude Codeの職場導入率18%（[INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) B-2）と比べる対象すらない。Cursor $2B ARRの成長がGrok固有の価値によるものか、Claude/GPT APIへのアクセスによるものかの分離も不可能なままである。製品が出荷されている事実と、それが採用に結びついている事実は別の次元だ。

### 性能評価での位置と「真剣な作業」からの除外

Grok 4.6のリリースは性能評価の地図を変えうる最初のシグナルである。xAIはArtificial Analysis Intelligence Index（9ベンチマーク複合）でGrok 4.6がGPT-5.6 Solと同等性能に到達したと主張する（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3）。Grok 4.5の時代には、Artificial Analysis一般知能スコアでGrok 4.5は4位であり、トップパフォーマーの議論に含まれていなかった。この主張が独立検証されれば、フロンティア性能議論からのGrok除外という構造が覆る可能性がある。

ただし現時点では3つの制約がある。第一に、主張はxAIの自家評価であり、Artificial Analysis自身の独立出版ではない。第二に、Grok 4.6のLMSpeed・Vision Arena等の独立ランキングでのスコアは未公開である。Grok 4.5の時代にはLMSpeed推論ベンチマークで54.6点・21位（[INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) B-1）、Vision Arenaでは1282点・15位（[INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) B-2）であった。第三に、エージェントフレームワークの比較では2026年8月版で対象が13種に拡大したにもかかわらずGrok Buildは含まれない（[INFO-013](../Information/2026-08-10/collected-raw.md#INFO-013) C-2）。前回の8枠比較（[INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) C-2）から枠が5つ増えたにもかかわらずGrok Buildが主要枠外に留まることは、開発者コミュニティでの採用重量が測定可能な水準に達していないことを示す。

Artificial Analysis Intelligence Index 2026年8月版ではClaude Opus 5が60.7%で首位、Kimi K3が全体3位（オープンウェイトでプロプライエタリ超え）、GLM-5.2がSWE-bench Pro 62.1%（GPT-5.5の58.6%を超える）と、OSSがフロンティアに迫る中（[INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) B-2）、Grok 4.6がこの指数でGPT-5.6 Solと同等を主張することは、Grok 4.5の時の相対的後退状況からの潜在的転換点である。但し「主張」と「検証」の距離はまだ埋まっていない。

### 価格位置と低価格独自性の希薄化

Grok 4.6のAPI価格は$2/$6でGrok 4.5と同等である（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3）。Claude Opus 5（$5/$25）やGPT-5.6 Sol（$5/$30）より安い。しかし最安帯のDeepSeek V4 Flash（$0.14/$0.28）やMiMo-V2.5 Flash（$0.10/$0.30）とは桁が違う。DeepSeek V4-FlashがIntelligence IndexでGPT-5.6 Lunaを上回り（[INFO-009](../Information/2026-08-10/collected-raw.md#INFO-009) C-2）、MITライセンス・セルフホスト可能なOSSモデルが商用フロンティアの性能領域に到達し始めている（[INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) B-2）。「低価格で差別化する」という[H-XAI-002](../config/hypotheses.json)の前提は侵食され続けている。アジェンティックAIが通常の10〜30倍のトークンを消費する条件下では、トークン単価の差が総コストに大きく効く。Grokの中間帯価格は、プレミアム性能を欠き同時に最安でもない、位置として厳しい。

### 政府と軍事の次元

SpaceXがペンタゴンにAIモデル実行向けのデータセンター容量を数十億ドル規模で提供する協議が続いている（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）。xAIはAnthropicが拒否した軍事利用に同意済みであり、連邦調達市場でのxAI優位が構造化しつつある。2026年8月時点では、ペンタゴン・Anthropic・OpenAIの間で倫理的対立が「完全サイクル」（Anthropic除外→OpenAI含む8社「all lawful use」合意→Anthropic・OpenAI間の倫理的競争）として展開されており（[IND-030](../config/indicators.json) critical）、xAIはこの対立の構造的前提（軍事利用に同意済み）に位置している。しかし政府や軍事での地位強化は、エンタープライズ（民間企業）採用の直接定量証拠ではない。人間却下比率の定量データは53R/54R連続不在（KIQ-MIL-001）であり、AI推奨がどれだけ人間によって却下されているかの検証も不能である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Grok 4.6リリース: 長時間エージェント向け・agentic RL（コーディング/Web/CAD/カーネル）・Intelligence Index同等主張（GPT-5.6 Sol）・API $2/$6・Cursor/Grok Build/API即時利用 | [H-XAI-004](../config/hypotheses.json) 技術的広がりC方向の最強力シグナル。Intelligence Index同等は自家評価。独立検証保留・エンタープライズ定量不在 | A-1/A-3 | [INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) [INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) |
| 高 | Grok Bot（独自コンピュータ環境・24時間稼働AIチームメイト・ベータ）・Imagine Image 2.0・Imagine Video 1.5・Grok Build MCP統合・Grok 4.20 multi-agent variant | [H-XAI-004](../config/hypotheses.json) エコシステム拡大C方向。観測期間中で最大の製品展開。但しGrok固有採用定量なし | A-3/A-1 | [INFO-003](../Information/2026-08-14/collected-raw.md#INFO-003) [INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) |
| 高 | エンタープライズ採用定量データ39R以上連続完全不在（WAU/DAU・F500導入率・企業契約数いずれも非公開） | [H-XAI-004](../config/hypotheses.json) indeterminate維持の核心根拠。復帰条件（定量データ観測）未到達 | 構造的 | [H-XAI-004](../config/hypotheses.json) |
| 高 | フレームワーク比較8→13種拡大でもGrok Build主要枠外。但しMCP全社対応製品群には含まれた（[IND-027](../config/indicators.json) v4.66） | [H-XAI-004](../config/hypotheses.json) コミュニティ採用重量での不在継続。MCP対応は技術的肯定的シグナルだが採用重量とは別次元 | C-2 | [INFO-013](../Information/2026-08-10/collected-raw.md#INFO-013) [INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) |
| 高 | LMSpeed推論ベンチマーク: Grok 4.5 54.6点・21位。Vision Arena Grok 4.5 1282点・15位。Grok 4.6の独立ベンチマークスコアは未公開 | [H-XAI-004](../config/hypotheses.json) 性能評価での劣位継続（4.5ベース）。Grok 4.6での改善はIntelligence Index主張のみ・未検証 | B-1/B-2 | [INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) [INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) |
| 高 | Artificial Analysis Intelligence Index: Opus 5 #1(60.7%)・Kimi K3全体#3(OSS)・GLM-5.2 SWE-bench Pro>GPT-5.5。Grok 4.6はGPT-5.6 Sol同等と主張（自家評価） | [H-XAI-004](../config/hypotheses.json) Grok 4.6のIntelligence Index同等主張は4.5の相対的後退からの潜在的転換。但し独立検証保留 | B-2/A-3 | [INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) [INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) |
| 高 | 会計ベンチマーク: Grok 4.5 84.2%・42モデル中1位。但し一般知能は4位 | [H-XAI-004](../config/hypotheses.json) 専門領域での強さ（C方向）。ベンチマーク特化型の強みと汎用知能差の共存 | C-2 | [INFO-045](../Information/2026-08-10/collected-raw.md#INFO-045) |
| 高 | Grok Buildオープンソース化・Plugin Marketplace・Copilot/Bedrock/Databricks統合・Anthropicコンピュート提携 | [H-XAI-004](../config/hypotheses.json) エコシステム拡大（C方向）。前回記録。公式docs化・MCP統合で補完 | A-3 | [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) |
| 高 | FLI AI Safety Index: xAI F評価(0.65)・全9社中7位(4位→7位悪化)・存在的安全性は全社最弱ドメイン | [H-XAI-004](../config/hypotheses.json) 安全性次元での構造的劣位がA-1品質で確定。差別化次元の欠落 | A-1 | [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) |
| 高 | AIコーディング3強$1B ARR突破: Copilot 29%/4.7M有料・Cursor 18%/$2B・Claude Code 18%。Grok固有採用データは不在 | [H-XAI-004](../config/hypotheses.json) 競合の定量公開とGrokの非公開の対比。「真剣な作業」でのGrok不在の量化 | B-2 | [INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) |
| 高 | Grok 4.6価格$2/$6（4.5と同等）・DeepSeek V4 Flash $0.14/$0.28・DeepSeek V4-Flash>Luna・GLM-5.2 SWE-bench Pro>GPT-5.5 | [H-XAI-002](../config/hypotheses.json) 低価格独自性の希薄化。中間帯価格は性能・コスト両面で厳しい位置 | B-1/C-2 | [INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) [INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037) [INFO-009](../Information/2026-08-10/collected-raw.md#INFO-009) [INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) |
| 高 | SpaceX-Pentagon数十億ドルAIデータセンター協議継続・xAI軍事利用同意済み・xAI $20B Series E | [H-XAI-004](../config/hypotheses.json) 政府/軍事次元での地位強化。$20B調達は資金基盤。但しエンタープライズ採用定量証拠ではない。[IND-030](../config/indicators.json) critical | B-2 | [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) [INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) |
| 中 | AnthropicへのColossusコンピュート提供提携 | [H-XAI-004](../config/hypotheses.json) インフラ提供は収益源。但しGrok固有採用との直接関係不明 | A-3 | [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| エンタープライズ採用定量データ（WAU/DAU・F500導入率・企業契約数）が初めて公開される | [H-XAI-004](../config/hypotheses.json) の核心パラメータ不在（39R以上）が解消し、indeterminateから確度評価に復帰する | 次回 | [IND-027](../config/indicators.json) |
| Grok 4.6のIntelligence Index同等主張がArtificial Analysis独立評価で確認される、またはLMSpeed/Vision Arena等の独立ランキングで上位3社に入る | 「真剣な作業」からの除外が覆る。[H-XAI-002](../config/hypotheses.json) のC方向確定。現在はxAI自家評価（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3）であり独立検証保留 | 90日 | [IND-025](../config/indicators.json) |
| Cursor統合後にGrok系コーディングツールの採用（DL/API呼び出し量）が定量で回復する | [H-XAI-004](../config/hypotheses.json) のエンタープライズ獲得読みが上方修正される。90日で回復しなければ読みは弱まる | 90日 | [IND-027](../config/indicators.json) |
| KIQ-MIL-001が完全回答に到達する（人間却下比率・誤標的率の公開） | 標的選定への直接関与度が確定する。現在53R/54R連続不在 | 90日 | [IND-030](../config/indicators.json) |
| DL減少傾向が3ヶ月以上継続する（1月→4月→7月）ことが7月データで確認される | [H-XAI-002](../config/hypotheses.json) の59%根拠が崩れ、medium→low移行が確定する | 30日 | [IND-013](../config/indicators.json) |
| FLI次回評価でxAIがD以上に改善する、または安全チーム設置・危険能力評価の公開 | [H-XAI-004](../config/hypotheses.json) の安全性次元での劣位が緩和される | 180日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤として展開し、Xデータ依存なしでエンタープライズ市場シェアを獲得する | 52% indeterminate | ±0%（v4.66）。Grok 4.6リリース（[INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) A-1）は長時間エージェント向けモデルとしてagentic RL（コーディング/Web/CAD/カーネル最適化）を実証。Intelligence Index同等主張（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3・GPT-5.6 Sol同等・自家評価）は観測期間中で最も強力なC方向シグナル。Grok BuildがMCP全社対応製品群に含まれた（[IND-027](../config/indicators.json) v4.66）。Grok Build公式docs化（[INFO-011](../Information/2026-08-10/collected-raw.md#INFO-011) A-3）・会計ベンチマーク1位84.2%（[INFO-045](../Information/2026-08-10/collected-raw.md#INFO-045) C-2）・Grok Build OSS・Plugin Marketplace・Copilot/Bedrock/Databricks統合・Anthropicコンピュート提携（全A-3）もC方向。SpaceX-Pentagonデータセンター協議・$20B Series Eは政府/軍事・資金次元C方向。但しエンタープライズ採用定量データ39R以上完全不在・フレームワーク比較13種でも主要枠外・Intelligence Index同等は未検証・LMSpeed 54.6/21位・Vision Arena 1282/15位（Grok 4.5ベース）でI方向。復帰条件（定量データ観測）未到達 | [INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) [INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) [INFO-003](../Information/2026-08-14/collected-raw.md#INFO-003) [INFO-011](../Information/2026-08-10/collected-raw.md#INFO-011) [INFO-045](../Information/2026-08-10/collected-raw.md#INFO-045) [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) [INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | [INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) [INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) [INFO-013](../Information/2026-08-10/collected-raw.md#INFO-013) [INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) [INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し、価格競争で市場シェアを獲得する | 59% medium | ±0%（v4.66）。Grok 4.6 API $2/$6はGrok 4.5と同等（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3）・Claude/GPT旗艦より安価（C方向）。但しDeepSeek V4 Flash $0.14/$0.28・DeepSeek V4-Flash>Luna（[INFO-009](../Information/2026-08-10/collected-raw.md#INFO-009) C-2）・GLM-5.2 SWE-bench Pro 62.1%>GPT-5.5 58.6%（[INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) B-2）・MiMo-V2.5 Flash $0.10/$0.30と桁差あり。「低価格」独自性希薄化継続（I方向）。DL 60%減未解決。59%以下が続けば次ラウンドでmedium→low審査 | [INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) [INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037) [INFO-011](../Information/2026-08-10/collected-raw.md#INFO-011) | [INFO-009](../Information/2026-08-10/collected-raw.md#INFO-009) [INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) [INFO-058](../Information/2026-08-03/collected-raw.md#INFO-058) |
| [H-XAI-001](../config/hypotheses.json) | （棄却）Xデータ活用でリアルタイム特化を差別化する | 35% rejected | 42R以上にわたりXデータ活用の直接証拠不在。xAI→SpaceXAI統合で観測の意義自体が低下 | （なし） | 42R以上の証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | （棄却）SpaceX統合で宇宙・製造業特化AIを展開する | 35% rejected | 43R以上にわたり直接的特化AI製品証拠不在。Colossusは汎用インフラ扱い | （なし） | 43R以上の特化製品証拠不在 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度・Grok API/DL動向 | 実被害A-2報告でcritical | high/rising。UK AISI実人間対象未承認行動（OpenAI/Anthropic両社）・国際AI安全性報告書30カ国・OpenAI Astraサイバー能力「クリティカル」。xAI固有の新規A-2実被害なし。DL 60%減は未解決（1月→4月）。KIQ-MIL-001人間却下比率53R/54R不在継続。critical移行条件未到達 | 2026-08-14 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・フロンティア性能差 | 性能差ベンダー間5%未満でhigh | elevated/stable。OSS-クローズドギャップ約4ヶ月・DeepSeek V4-Flash ARC-AGI 89%・GPQA Diamond 8-12pt格差存続・ARC-AGI-3 Opus 5 30.2% >> 他約2%。Grok 4.6はIntelligence Index同等主張（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3・自家評価）だが独立ベンチマーク未公開。Grok 4.5は会計ベンチマーク#1(84.2%)だが一般知能4位。Grokトップティア入りは主張段階・未検証 | 2026-08-14 |
| [IND-026](../config/indicators.json) | エージェント本番到達率 | 3ソース以上で完了率<10% | high/rising。Deloitte 5%準備・Stanford 12%→66%タスク完了だが11-23%本番・ROI 74%生産性/11%財務・BCG 65%言及/1%成熟・Klarna再雇用。期待-実態ギャップ確定的深化継続 | 2026-08-14 |
| [IND-027](../config/indicators.json) | エコシステム標準化・Grokスタック採用 | 囲い込み反転 | high/rising。MCP全社対応(MS/Azure/Grok Build/Claude Code/Cloudflare)・AAIF 57新規+Alibaba・Google AP2 60+・AWS AgentCore・Agent Skills marketplace。Grok BuildがMCP全社対応製品群に含まれた。但しフレームワーク比較13種で主要枠外は不変（[INFO-013](../Information/2026-08-10/collected-raw.md#INFO-013) C-2）。加速継続。採用重量は未計測 | 2026-08-14 |
| [IND-028](../config/indicators.json) | AGI到達度 | 主観-客観乖離 | high/rising。Claude RSI自己訓練・Opus 5 ARC-AGI-3 30.2%・Databricks CEO「AGI到達」(A-1)・Amodei 6-12ヶ月SE・LeCun「何十年も先」。RSI概念具体化と限界の同時進行継続 | 2026-08-14 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 物理的制約の顕在化 | high/rising。JPMorgan ハイパースケーラーCapEx $6970億・Databricks $50億/$1900億・xAI $200億Series E・Cognition $400億協議・Project Stargate最大$5000億。資本流入空前規模継続。xAI $200億Series Eは資金基盤強化 | 2026-08-14 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 | （critical到達済み） | critical/rising。DPA基盤モデル適用・中国NVIDIA/AMD/Intel国家DC排除・Pentagon 9/30廃止期限・Trump「ONE RULE」・EU罰金1500万ユーロ/3%・Pentagon $54B自律型兵器・判事Lin「ケース悪化」。xAIは軍事利用に同意済み。KIQ-MIL-001人間却下比率53R/54R不在継続。critical解消条件3基準いずれも未到達 | 2026-08-14 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-08-14 | ターゲット編集（構造的変化: フロンティアモデル新規リリース）。Grok 4.6リリース（[INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) A-1）・Intelligence Index同等主張 GPT-5.6 Sol（[INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) A-3・自家評価）・Grok Bot新製品（[INFO-003](../Information/2026-08-14/collected-raw.md#INFO-003) A-3）・Grok Build MCP統合・Grok 4.20 multi-agent variant存在を新規反映。Grok BuildがMCP全社対応製品群に含まれた（[IND-027](../config/indicators.json) v4.66）。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 59% medium ±0%（v4.66）。KIQ-MIL-001 49R/50R→53R/54R。エンタープライズ採用定量データ35R→39R以上。全7指標現在値2026-08-14更新。コア判断不変（測定不能・availability≠adoption） | [INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) [INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) [INFO-003](../Information/2026-08-14/collected-raw.md#INFO-003) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-08-10 | ターゲット編集（7日freshness timeout）。Grok Build公式docs化（coding agent・TUI・ファイル編集・シェル実行・[INFO-011](../Information/2026-08-10/collected-raw.md#INFO-011) A-3）・会計ベンチマークGrok 4.5 84.2%1位（[INFO-045](../Information/2026-08-10/collected-raw.md#INFO-045) C-2）を新規反映。フレームワーク比較8→13種拡大でもGrok Build主要枠外（[INFO-013](../Information/2026-08-10/collected-raw.md#INFO-013) C-2）。Artificial Analysis Index Opus 5 #1(60.7%)・OSS追迫でGrok相対的後退（[INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) B-2）。DeepSeek V4-Flash>Luna（[INFO-009](../Information/2026-08-10/collected-raw.md#INFO-009) C-2）でH-XAI-002低価格独自性更に希薄化。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 59% medium ±0%（v4.62）。KIQ-MIL-001 41R/42R→49R/50R。エンタープライズ採用定量データ27R→35R以上。全7指標現在値2026-08-10更新。コア判断不変（測定不能・availability≠adoption） | [INFO-011](../Information/2026-08-10/collected-raw.md#INFO-011) [INFO-045](../Information/2026-08-10/collected-raw.md#INFO-045) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-08-03 | ターゲット編集（7日freshness timeout）。Grok Buildオープンソース化・Voice Think Fast 2.0・Plugin Marketplace・GitHub Copilot/Bedrock/Databricks統合・Anthropicコンピュート提携を新規反映（[INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) 全A-3）。LMSpeed Grok 4.5 54.6/21位（[INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) B-1）・Vision Arena 1282/15位（[INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) B-2）・AIコーディング3強比較（[INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) B-2）・$20B Series E（[INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) B-2）を統合。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 59% ±0%（v4.55）。KIQ-MIL-001 34R/35R→41R/42R。エンタープライズ採用定量データ23R→27R以上。全7指標現在値2026-08-03更新。コア判断不変（測定不能・availability≠adoption） | [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-07-27 | 全面書き直し（8日freshness timeout）。Grok 4.5全プラットフォーム展開・Voice API・Grok Build Workflows・Google Workspace addon・Vertex AI提供を新規反映（[INFO-004](../Information/2026-07-27/collected-raw.md#INFO-004) [INFO-005](../Information/2026-07-27/collected-raw.md#INFO-005) [INFO-011](../Information/2026-07-27/collected-raw.md#INFO-011) 全A-3）。性能評価上位不在（[INFO-023](../Information/2026-07-27/collected-raw.md#INFO-023) [INFO-024](../Information/2026-07-27/collected-raw.md#INFO-024)）・主要8フレームワーク枠外（[INFO-013](../Information/2026-07-27/collected-raw.md#INFO-013)）・価格中間帯位置（[INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037)）を統合。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 59% ±0%（v4.47 DEGRADED）。KIQ-MIL-001 27R→34R/35R。エンタープライズ採用定量データ19R→23R以上。全7指標現在値2026-07-27更新 | [INFO-004](../Information/2026-07-27/collected-raw.md#INFO-004) [INFO-005](../Information/2026-07-27/collected-raw.md#INFO-005) [INFO-011](../Information/2026-07-27/collected-raw.md#INFO-011) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-07-19 | ターゲット編集。SpaceX-Pentagon数十億ドルAIデータセンター協議を新規反映。[H-XAI-004](../config/hypotheses.json) indeterminate/52% ±0%（v4.40 DEGRADED）。KIQ-MIL-001 26R→27R | [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-07-17 | 全面書き直し（7日freshness timeout）。FLI F評価0.65・4位→7位悪化・Grok 4.5詳細・Grok Build OSS・モデルコンセンサスでGrok除外を反映 | [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) [INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) | H-XAI-002 59%（±0%）・H-XAI-004 54→52% |
| 2026-07-10 | 全面書き直し。Grok 4.5発表・AAII 4位・Snorkel最強29%・SpaceX-Cursor $60B Q3クローズ確認・Warren開示要求7社含むを反映 | [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) | H-XAI-002 59%（±0%）・H-XAI-004 54%（±0%） |
| 2026-07-07 | ターゲット編集。Grok in Project Maven統合確認・Carnegie詳細レポート・Cursor $2B ARR・Voice Agent Builder・GLM 5.2 OSS#1を反映。[H-XAI-004](../config/hypotheses.json) 57→54% | [INFO-064](../Information/2026-07-07/collected-raw.md#INFO-064) | H-XAI-004 57→54%・H-XAI-002 59%（±0%） |

## 7. ブラインドスポット

- エンタープライズ採用定量データが39R以上連続完全不在。この不在を「不採用の証拠」と解釈するか「戦略的非公開」と解釈するかで確度評価が大きく変わる。累積ペナルティ論理の妥当性自体が検証不能であり、indeterminate分類はこの判別不能を正直に反映したものに過ぎない。
- Grok 4.6のIntelligence Index同等主張（GPT-5.6 Sol）がxAIの自家評価に基づくものであり、Artificial Analysis自身の独立出版ではない。この主張の真偽が判別不能な状態で、Grok 4.6の性能プロファイルを確定できない。「主張」と「検証」の距離をどう扱うかが、今後の[H-XAI-004](../config/hypotheses.json)評価の最大の分岐点である。
- KIQ-MIL-001の人間却下比率が53R/54R連続不在。AI推奨の却下率そのものが不在である以上、観測されていないリスクを不在と断定する正常性バイアスの逆方向リスクがある。xAIが軍事利用に同意済みである事実は、このリスクの重みを増す。
- Grok 4.5の会計ベンチマーク1位（84.2%）と一般知能4位の乖離が、何に起因するかが判明していない。Grok 4.6がIntelligence IndexでGPT-5.6 Sol同等を主張する一方で、会計ベンチマーク等の専門領域でのGrok 4.6スコアは未公開である。ベンチマーク特化型の性能プロファイルがGrok 4.6で変化したかの検証手段がない。
- Grok 4.6の技術性能向上（長時間エージェント・agentic RL・MCP統合・Cursor/Grok Build/API即時利用）とコミュニティコンセンサスでの除外（LMSpeed/Vision Arena未公開・フレームワーク比較13種でも主要枠外）の乖離が、何に起因するかが判明していない。Intelligence Index同等主張とフレームワーク除外の整合が取れていない。
- DL 60%減（1月→4月）が、Cursor買収前のCursor市場シェア下落とどう関係するか不明。7月データでの更新が必要だが入手できておらず、[H-XAI-002](../config/hypotheses.json) のmedium→low審査条件（3ヶ月継続）の検証が未完了のままである。
- Cursor $2B ARRの成長がGrok固有の価値によるものか、Claude/GPT APIへのアクセスによるものかの分離が不可能。買収完了後のGrok統合戦略が未公開であり、Cursorの成功をGrokの成功と読むことができるかの判別が立たない。
- Grok Botのエンタープライズ展開がウェイティングリスト段階であり、消費者ベータ（SuperGrok Heavy・Cursor Ultra・Cursor Teams Premium限定）での利用状況の定量データが不在。Grok Botがエンタープライズ市場で採用されるかの検証が不可能である。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 | 出典 |
|---|---|---|
| [INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) | Grok 4.6詳細: 長時間エージェント向け・agentic RL（コーディング/Web/CAD/カーネル）・Cursor/Grok Build/API即時利用・Grok 4.20 multi-agent variant・Grok Build MCP統合(A-1) | https://x.ai/news/grok-4-6 |
| [INFO-002](../Information/2026-08-14/collected-raw.md#INFO-002) | Grok 4.6リリース: Intelligence Index同等（GPT-5.6 Sol）・Extra High推論レベル・API $2/$6・2倍無料枠(A-3) | https://x.ai/news/grok-4-6 |
| [INFO-003](../Information/2026-08-14/collected-raw.md#INFO-003) | Grok Bot: 独自コンピュータ環境・24時間稼働AIチームメイト・ベータ(A-3) | https://x.ai/news/introducing-grok-bot |
| [INFO-011](../Information/2026-08-10/collected-raw.md#INFO-011) | Grok Build公式docs化（coding agent・TUI・ファイル編集・シェル実行）・Grok 4.5 API $2/$6・Voice Agent API $5/$15(A-3) | https://docs.x.ai/developers/release-notes |
| [INFO-045](../Information/2026-08-10/collected-raw.md#INFO-045) | 会計ベンチマーク: Grok 4.5 84.2%・42モデル中1位。一般知能は4位(C-2) | https://www.dualentry.com/blog/elon-musks-grok-beat-chatgpt-claude-at-accounting |
| [INFO-042](../Information/2026-08-10/collected-raw.md#INFO-042) | Artificial Analysis Intelligence Index: Opus 5 #1(60.7%)・Kimi K3全体#3(OSS)・GLM-5.2 SWE-bench Pro>GPT-5.5・Grokトップ外(B-2) | https://www.swfte.com/ai/leaderboard |
| [INFO-009](../Information/2026-08-10/collected-raw.md#INFO-009) | DeepSeek V4-Flash 0731: Intelligence Index 10pt上昇でGPT-5.6 Luna超過・MIT OSS・$0.14/$0.28(C-2) | LinkedIn / Artificial Analysis |
| [INFO-013](../Information/2026-08-10/collected-raw.md#INFO-013) | 2026エージェントフレームワーク比較13種: Grok Buildは主要枠外(C-2) | https://www.turingpost.com/p/frameworks-sdks |
| [INFO-001](../Information/2026-08-10/collected-raw.md#INFO-001) | UK AISI A-1品質公式インシデント: 122回中10回(8.2%)無承認アクション・封じ込め完了(A-1) | https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing |
| [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) | xAIニュース総覧: Grok Build OSS・Voice Think Fast 2.0・Copilot/Workspace/Bedrock/Databricks統合・Anthropicコンピュート・Grok Business(A-3) | https://x.ai/news |
| [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) | Grok Voice Think Fast 2.0（WebSocket Speech-to-Speech API）・Grok Build OSS GitHub公開(A-3) | https://x.ai/news |
| [INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) | 2026エージェントフレームワーク比較8枠: Grok Buildは主要枠外(C-2) | エージェントフレームワーク比較 |
| [INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) | Vision Arena: Grok 4.5 1282点・15位。Claude Fable 5が首位(B-2) | https://arena.ai/leaderboard/vision |
| [INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) | LMSpeed推論ベンチマーク: Grok 4.5 54.6点・21位。Claude Opus 4.5が62.8首位(B-1) | https://lmarena.ai |
| [INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) | xAI $20B Series E調達（評価額$35B）(B-2) | 報道 |
| [INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) | AIコーディング3強: GitHub Copilot 29%/4.7M有料・Cursor 18%/$2B・Claude Code 18%。Grok固有採用分離不能(B-2) | https://uvik.net/blog/ai-coding-assistant-statistics/ |
| [INFO-058](../Information/2026-08-03/collected-raw.md#INFO-058) | トークン価格二極化: フロンティア維持 vs OSS無償化加速(B-2) | 市場データ |
| [INFO-004](../Information/2026-07-27/collected-raw.md#INFO-004) | Grok 4.5全プラットフォーム展開（iOS/Android/Web/X・7/22）・Opus級・高速低コスト(A-3) | https://x.ai/news/grok-4-5-everywhere |
| [INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037) | API価格比較: Grok 4.5 $2/$6・DeepSeek V4 Flash $0.14/$0.28最安(B-1) | VentureBeat |
| [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | SpaceX-Pentagon数十億ドルAIデータセンター協議・xAI軍事利用同意済み(B-2) | https://thebulletin.org/2026/07/the-rise-of-the-military-technology-complex/ |
| [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) | FLI AI Safety Index完全スコアカード: xAI F(0.65)・4位→7位悪化・存在的安全性全社最弱(A-1) | FLI報告書 |
| [Arbiter v4.66](../state/arbiter-2026-08-14.md) | 確度評価の完全根拠（H-XAI-004 ±0% indeterminate・H-XAI-002 ±0% medium・7指標全状態変更なし） | 内部参照 |
