# xAI → SpaceXAI

> 最終判断更新: 2026-08-03
> 全体確信度: 測定不能（H-XAI-004 indeterminate維持）
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Grok Gov Modelのガードレール内容・Cursor統合後のGrok固有採用分離も非公開。DL/API呼び出し量の時系列データが途絶状態。KIQ-MIL-001は41R/42R連続不在。エンタープライズ採用定量データが27R以上連続完全不在（[H-XAI-004](../config/hypotheses.json) 復帰条件未到達）。7月下旬から8月上旬にGrok 4.5全プラットフォーム展開・Grok Buildオープンソース化・Voice Think Fast 2.0・GitHub Copilot統合・Google Workspace・Amazon Bedrock・Databricks対応・AnthropicへのColossusコンピュート提供で製品・エコシステム面は拡大した（[INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) 全A-3）、availability≠adoption制約は不変。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 59% medium ±0%（v4.55 ±0%）
> 主参照: [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はxAIを「製品とエコシステムの広がりは加速しているが、エンタープライズ採用の定量証拠が構造的に欠落したままの企業」と読んでいる。最大の根拠は、7月下旬から8月上旬にかけてGrok Buildがオープンソース化され（[INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) A-3）、GitHub Copilot・Google Workspace・Amazon Bedrock・Databricksへの統合が相次ぎ（[INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) A-3）、Voice Think Fast 2.0のSpeech-to-Speech APIが提供されたことだ。xAIがAnthropicにColossusコンピュートを提供する提携も確認された。製品面での広がりはフロンティア4社に次ぐ水準にある。しかしWAU/DAU・F500導入率・企業契約数といった採用の直接定量データが27R以上連続で不在であり、この広がりが市場シェアに結びついているかの検証が不可能である。もしGrok固有の採用定量データが初めて公開されれば、この「測定不能」の判断は変わる。

[H-XAI-004](../config/hypotheses.json) はindeterminate/52%で±0%（v4.55）。Grok Buildのオープンソース化とエコシステム統合の拡大は技術的広がり（C方向）の材料だが、availability≠adoptionの制約を覆す定量証拠を含まない。LMSpeed推論ベンチマークでGrok 4.5は54.6点・21位にとどまり（[INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) B-1）、首位Claude Opus 4.5（62.8）との差は開いたままである。Vision ArenaではGrok 4.5が1282点・15位（[INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) B-2）。コミュニティコンセンサスでGrokが「真剣な作業」から除外される状況に変化はない。

## 1. コア判断

全体確信度は測定不能に置く。理由は一つで、エンタープライズ採用の定量データが23R以上連続で完全に不在だからだ。フロンティア4社（OpenAI・Anthropic・Google・xAI）のうち、xAIだけが採用規模を示す数値を一度も公開していない。この不在を「不採用の証拠」と断定することは正常性バイアスの逆方向に倒れるが、同時に「戦略的非公開」と charitable に解釈する根拠もない。だから確信度ではなく「測定不能」と書く。

### 製品面の広がりと採用データの不在

7月下旬から8月上旬にかけてxAIの製品面は一段と広がった。Grok Buildがオープンソース化されGitHubで公開された（[INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) A-3）。WebSocketベースのSpeech-to-Speech API「Grok Voice Think Fast 2.0」が提供され、関数呼続・Web検索ツールに対応する。Grok Skills・Connectors・Plugin Marketplaceが導入され、GitHub Copilot・Google Workspace・Amazon Bedrock・Databricksへの統合が相次いだ（[INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) A-3）。Imagine Video 1.5はテキスト・画像・音声リファレンスに対応し、Grok Business / Enterpriseプランが2025年12月以降提供されている。xAIがAnthropicにColossusコンピュートを提供する提携も確認された。

これらは技術的速度とエコシステム拡大の実物である。だが、GitHub Copilotが約20Mユーザー・職場導入率29%、Cursorが$2B ARRに到達した（[INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) B-2）のと対照的に、Grok固有のユーザー数・契約数・利用率は一切公開されない。Claude Codeの職場導入率18%（[INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) B-2）と比べる対象すらない。Cursor $2B ARRの成長がGrok固有の価値によるものか、Claude/GPT APIへのアクセスによるものかの分離も不可能なままである。製品が出荷されている事実と、それが採用に結びついている事実は別の次元だ。

### 性能評価での位置と「真剣な作業」からの除外

ベンチマークの断面でもGrokの位置は明確だ。LMSpeed推論ベンチマークでClaude Opus 4.5が62.8で首位、GPT-5.6 Solが61.8で2位に入る一方、Grok 4.5は54.6点・21位である（[INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) B-1）。Vision ArenaではGrok 4.5が1282点・15位にとどまり（[INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) B-2）、1位のClaude Fable 5（1318点）との差は開いている。Vellum LLM LeaderboardのHumanity's Last Exam・SWE-bench上位にGrokは名を連ねない。

エージェントフレームワークの比較でも、2026年の主要8枠（LangChain・CrewAI・Microsoft Agent Framework・Google ADK・OpenAI Agents SDK・Mastra等）にGrok Buildは含まれない（[INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) C-2）。Grok Buildのオープンソース化とPlugin Marketplace導入にもかかわらず、開発者コミュニティの採用重量で測ると、Grokスタックは主要枠の外にいる。これは「コミュニティコンセンサスでGrokが真剣な作業の議論から除外される」状況が覆っていないことを示す。

### 価格位置と低価格独自性の希薄化

Grok 4.5のAPI価格は$2/$6（[INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037) B-1）で、Claude Opus 5（$5/$25）やGPT-5.6 Sol（$5/$30）より安い。しかし最安帯のDeepSeek V4 Flash（$0.14/$0.28）やMiMo-V2.5 Flash（$0.10/$0.30）とは桁が違う。Kimi K3（2.8Tパラメータ・HLE 56%）やDeepSeek V4 Pro（GPQA 90.1%）がフロンティアに肉薄する中（[INFO-029](../Information/2026-07-27/collected-raw.md#INFO-029) C-2）、「低価格で差別化する」という[H-XAI-002](../config/hypotheses.json)の前提は侵食され続けている。アジェンティックAIが通常の10〜30倍のトークンを消費する条件下では、トークン単価の差が総コストに大きく効く。Grokの中間帯価格は、プレミアム性能を欠き同時に最安でもない、位置として厳しい。

### 政府と軍事の次元

SpaceXがペンタゴンにAIモデル実行向けのデータセンター容量を数十億ドル規模で提供する協議が続いている（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）。xAIはAnthropicが拒否した軍事利用に同意済みであり、連邦調達市場でのxAI優位が構造化しつつある。しかし政府や軍事での地位強化は、エンタープライズ（民間企業）採用の直接定量証拠ではない。Pentagon 2012年指令は自律兵器を制限し、人間の軍事指揮官が着弾を決定する方針を維持するが（[INFO-057](../Information/2026-07-27/collected-raw.md#INFO-057) B-2）、「自律兵器」の定義自体が合意に至っていない。人間却下比率の定量データは34R/35R連続不在（KIQ-MIL-001）であり、AI推奨がどれだけ人間によって却下されているかの検証も不能である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Grok Buildオープンソース化（GitHub公開）・Plugin Marketplace・GitHub Copilot/Bedrock/Databricks統合 | [H-XAI-004](../config/hypotheses.json) エコシステム拡大（C方向）。但し採用規模の定量なし。8フレームワーク比較で主要枠外は不変 | A-3 | [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) [INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) |
| 高 | Grok Voice Think Fast 2.0（WebSocket Speech-to-Speech API）・Imagine Video 1.5・Grok Business/Enterprise | [H-XAI-004](../config/hypotheses.json) 製品ラインの拡張（C方向）。音声・動画は新領域。但し採用規模の定量なし | A-3 | [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) |
| 高 | LMSpeed推論ベンチマーク: Grok 4.5 54.6点・21位。首位Claude Opus 4.5（62.8）と8.2点差。Vision Arena Grok 4.5 1282点・15位 | [H-XAI-004](../config/hypotheses.json) 性能評価での劣位継続。首位Claude Fable 5（1318点）との差維持 | B-1/B-2 | [INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) [INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) |
| 高 | エンタープライズ採用定量データ27R以上連続完全不在（WAU/DAU・F500導入率・企業契約数いずれも非公開） | [H-XAI-004](../config/hypotheses.json) indeterminate維持の核心根拠。復帰条件（定量データ観測）未到達 | 構造的 | [H-XAI-004](../config/hypotheses.json) |
| 高 | AIコーディング3強$1B ARR突破: Copilot 29%/4.7M有料・Cursor 18%/$2B・Claude Code 18%。Grok固有採用データは不在 | [H-XAI-004](../config/hypotheses.json) 競合の定量公開とGrokの非公開の対比。「真剣な作業」でのGrok不在の量化 | B-2 | [INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) |
| 高 | FLI AI Safety Index: xAI F評価(0.65)・全9社中7位(4位→7位悪化)・存在的安全性は全社最弱ドメイン | [H-XAI-004](../config/hypotheses.json) 安全性次元での構造的劣位がA-1品質で確定。差別化次元の欠落 | A-1 | [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) |
| 高 | Grok 4.5価格$2/$6・DeepSeek V4 Flash $0.14/$0.28・GLM FlashFree $0・Kimi K3 HLE 56% | [H-XAI-002](../config/hypotheses.json) 低価格独自性の希薄化。中間帯価格は性能・コスト両面で厳しい位置 | B-1/B-2 | [INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037) [INFO-058](../Information/2026-08-03/collected-raw.md#INFO-058) |
| 高 | SpaceX-Pentagon数十億ドルAIデータセンター協議継続・xAI軍事利用同意済み・xAI $20B Series E | [H-XAI-004](../config/hypotheses.json) 政府/軍事次元での地位強化。$20B調達は資金基盤。但しエンタープライズ採用定量証拠ではない。[IND-030](../config/indicators.json) critical | B-2 | [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) [INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) |
| 中 | AnthropicへのColossusコンピュート提供提携 | [H-XAI-004](../config/hypotheses.json) インフラ提供は収益源。但しGrok固有採用との直接関係不明 | A-3 | [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| エンタープライズ採用定量データ（WAU/DAU・F500導入率・企業契約数）が初めて公開される | [H-XAI-004](../config/hypotheses.json) の核心パラメータ不在（23R以上）が解消し、indeterminateから確度評価に復帰する | 次回 | [IND-027](../config/indicators.json) |
| Cursor統合後にGrok系コーディングツールの採用（DL/API呼び出し量）が定量で回復する | [H-XAI-004](../config/hypotheses.json) のエンタープライズ獲得読みが上方修正される。90日で回復しなければ読みは弱まる | 90日 | [IND-027](../config/indicators.json) |
| KIQ-MIL-001が完全回答に到達する（人間却下比率・誤標的率の公開） | 標的選定への直接関与度が確定する。現在41R/42R連続不在 | 90日 | [IND-030](../config/indicators.json) |
| DL減少傾向が3ヶ月以上継続する（1月→4月→7月）ことが7月データで確認される | [H-XAI-002](../config/hypotheses.json) の59%根拠が崩れ、medium→low移行が確定する | 30日 | [IND-013](../config/indicators.json) |
| Grokが次期性能評価で上位3社に入る、またはコミュニティコンセンサスでトップティア入りする | フロンティア差別化の残存が強化され、[H-XAI-002](../config/hypotheses.json) のC方向確定。「真剣な作業」からの除外が覆る | 90日 | [IND-025](../config/indicators.json) |
| FLI次回評価でxAIがD以上に改善する、または安全チーム設置・危険能力評価の公開 | [H-XAI-004](../config/hypotheses.json) の安全性次元での劣位が緩和される | 180日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤として展開し、Xデータ依存なしでエンタープライズ市場シェアを獲得する | 52% indeterminate | ±0%（v4.55）。復帰条件（定量データ観測）未到達のためindeterminate維持。Grok Buildオープンソース化・Voice Think Fast 2.0・Plugin Marketplace・GitHub Copilot/Bedrock/Databricks統合・Anthropicコンピュート提携（全A-3）は技術的広がり（C方向）。SpaceX-Pentagonデータセンター協議・$20B Series Eは政府/軍事・資金次元C方向。但しエンタープライズ採用定量データが27R以上完全不在・I=0継続。LMSpeed 54.6/21位・Vision Arena 1282/15位・主要8フレームワーク枠外で性能・採用上位不在がI方向 | [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) [INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | [INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) [INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) [INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し、価格競争で市場シェアを獲得する | 59% medium | ±0%（v4.55）。Grok 4.5 $2/$6はClaude/GPT旗艦より安価（C方向）。但しDeepSeek V4 Flash $0.14/$0.28・GLM FlashFree $0・MiMo-V2.5 Flash $0.10/$0.30と桁差あり。Kimi K3・DeepSeek V4 Proがフロンティア肉薄で「低価格」独自性希薄化継続（I方向）。DL 60%減未解決。59%以下が続けば次ラウンドでmedium→low審査 | [INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037) [INFO-058](../Information/2026-08-03/collected-raw.md#INFO-058) | [INFO-060](../Information/2026-08-03/collected-raw.md#INFO-060) [INFO-061](../Information/2026-08-03/collected-raw.md#INFO-061) |
| [H-XAI-001](../config/hypotheses.json) | （棄却）Xデータ活用でリアルタイム特化を差別化する | 35% rejected | 42R以上にわたりXデータ活用の直接証拠不在。xAI→SpaceXAI統合で観測の意義自体が低下 | （なし） | 42R以上の証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | （棄却）SpaceX統合で宇宙・製造業特化AIを展開する | 35% rejected | 43R以上にわたり直接的特化AI製品証拠不在。Colossusは汎用インフラ扱い | （なし） | 43R以上の特化製品証拠不在 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度・Grok API/DL動向 | 実被害A-2報告でcritical | high/rising。7月90件AIセキュリティインシデント・33組織影響（[INFO-018](../Information/2026-08-03/collected-raw.md#INFO-018) C-2）。DL 60%減は未解決（1月→4月）。新規A-2実被害なし。critical移行条件未到達 | 2026-08-03 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・フロンティア性能差 | 性能差ベンダー間5%未満でhigh | elevated/stable。LMSpeed Claude Opus 4.5首位62.8・Grok 4.5 54.6/21位（[INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) B-1）。DeepSeek V4 LiveCodeBench全球1位93.5%（[INFO-060](../Information/2026-08-03/collected-raw.md#INFO-060) B-1）。Vision Arena Grok 4.5 1282/15位（[INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) B-2）。Grokのトップティア不在は不変 | 2026-08-03 |
| [IND-026](../config/indicators.json) | エージェント本番到達率 | 3ソース以上で完了率<10% | high/rising。Fortune 500 80%+デプロイ/リーダー28%のみ（[INFO-039](../Information/2026-08-03/collected-raw.md#INFO-039) C-2）。企業32%のみスケール・55%後悔（[INFO-026](../Information/2026-08-03/collected-raw.md#INFO-026) B-2）。期待-実態ギャップ更に深化 | 2026-08-03 |
| [IND-027](../config/indicators.json) | エコシステム標準化・Grokスタック採用 | 囲い込み反転 | high/rising。MCPステートレス化AAIF/Linux Foundation昇格・全社採用（[INFO-022](../Information/2026-08-03/collected-raw.md#INFO-022) [INFO-023](../Information/2026-08-03/collected-raw.md#INFO-023) A-2）。8フレームワーク比較でGrok Buildは主要枠外（[INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) C-2）。Grok Build OSS・Plugin Marketplace追加だが採用重量は未計測 | 2026-08-03 |
| [IND-028](../config/indicators.json) | AGI到達度 | 主観-客観乖離 | high/rising。CEO予測分裂（Altman特異点/Amodei 2027/Hassabis 5-10年）（[INFO-028](../Information/2026-08-03/collected-raw.md#INFO-028) B-2）。RSI概念具体化と限界の同時進行 | 2026-08-03 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 物理的制約の顕在化 | high/rising。ビッグテック4社$2.4Tコミットメント・NVIDIA $750B・xAI $20B Series E（[INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) B-2）。資本流入加速・物理的制約ギャップ確定的 | 2026-08-03 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 | （critical到達済み） | critical/rising。トランプAI大統領令・ペンタゴン8社契約・SCR指定・EU AI Act 8月2日執行開始（[INFO-042](../Information/2026-08-03/collected-raw.md#INFO-042) [INFO-041](../Information/2026-08-03/collected-raw.md#INFO-041) A-1/A-3）。条件2充実史上最大水準継続。KIQ-MIL-001 41R/42R不在。critical解消条件3基準いずれも未到達 | 2026-08-03 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-08-03 | ターゲット編集（7日freshness timeout）。Grok Buildオープンソース化・Voice Think Fast 2.0・Plugin Marketplace・GitHub Copilot/Bedrock/Databricks統合・Anthropicコンピュート提携を新規反映（[INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) 全A-3）。LMSpeed Grok 4.5 54.6/21位（[INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) B-1）・Vision Arena 1282/15位（[INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) B-2）・AIコーディング3強比較（[INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) B-2）・$20B Series E（[INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) B-2）を統合。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 59% ±0%（v4.55）。KIQ-MIL-001 34R/35R→41R/42R。エンタープライズ採用定量データ23R→27R以上。全7指標現在値2026-08-03更新。コア判断不変（測定不能・availability≠adoption） | [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-07-27 | 全面書き直し（8日freshness timeout）。Grok 4.5全プラットフォーム展開・Voice API・Grok Build Workflows・Google Workspace addon・Vertex AI提供を新規反映（[INFO-004](../Information/2026-07-27/collected-raw.md#INFO-004) [INFO-005](../Information/2026-07-27/collected-raw.md#INFO-005) [INFO-011](../Information/2026-07-27/collected-raw.md#INFO-011) 全A-3）。性能評価上位不在（[INFO-023](../Information/2026-07-27/collected-raw.md#INFO-023) [INFO-024](../Information/2026-07-27/collected-raw.md#INFO-024)）・主要8フレームワーク枠外（[INFO-013](../Information/2026-07-27/collected-raw.md#INFO-013)）・価格中間帯位置（[INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037)）を統合。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 59% ±0%（v4.47 DEGRADED）。KIQ-MIL-001 27R→34R/35R。エンタープライズ採用定量データ19R→23R以上。全7指標現在値2026-07-27更新 | [INFO-004](../Information/2026-07-27/collected-raw.md#INFO-004) [INFO-005](../Information/2026-07-27/collected-raw.md#INFO-005) [INFO-011](../Information/2026-07-27/collected-raw.md#INFO-011) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-07-19 | ターゲット編集。SpaceX-Pentagon数十億ドルAIデータセンター協議を新規反映。[H-XAI-004](../config/hypotheses.json) indeterminate/52% ±0%（v4.40 DEGRADED）。KIQ-MIL-001 26R→27R | [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-07-17 | 全面書き直し（7日freshness timeout）。FLI F評価0.65・4位→7位悪化・Grok 4.5詳細・Grok Build OSS・モデルコンセンサスでGrok除外を反映 | [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) [INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) | H-XAI-002 59%（±0%）・H-XAI-004 54→52% |
| 2026-07-10 | 全面書き直し。Grok 4.5発表・AAII 4位・Snorkel最強29%・SpaceX-Cursor $60B Q3クローズ確認・Warren開示要求7社含むを反映 | [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) | H-XAI-002 59%（±0%）・H-XAI-004 54%（±0%） |
| 2026-07-07 | ターゲット編集。Grok in Project Maven統合確認・Carnegie詳細レポート・Cursor $2B ARR・Voice Agent Builder・GLM 5.2 OSS#1を反映。[H-XAI-004](../config/hypotheses.json) 57→54% | [INFO-064](../Information/2026-07-07/collected-raw.md#INFO-064) | H-XAI-004 57→54%・H-XAI-002 59%（±0%） |

## 7. ブラインドスポット

- エンタープライズ採用定量データが27R以上連続完全不在。この不在を「不採用の証拠」と解釈するか「戦略的非公開」と解釈するかで確度評価が大きく変わる。累積ペナルティ論理の妥当性自体が検証不能であり、indeterminate分類はこの判別不能を正直に反映したものに過ぎない。
- KIQ-MIL-001の人間却下比率が41R/42R連続不在。AI推奨の却下率そのものが不在である以上、観測されていないリスクを不在と断定する正常性バイアスの逆方向リスクがある。xAIが軍事利用に同意済みである事実は、このリスクの重みを増す。
- Grok 4.5の技術性能向上（全プラットフォーム展開・Grok Build OSS・Voice Think Fast 2.0・Plugin Marketplace・GitHub Copilot/Bedrock/Databricks統合）とコミュニティコンセンサスでの除外（LMSpeed 54.6/21位・Vision Arena 1282/15位・主要8フレームワーク枠外）の乖離が、何に起因するかが判明していない。ベンチマーク成績と実用性のギャップなのか、ブランド・エコシステム・信頼の問題なのか。
- DL 60%減（1月→4月）が、Cursor買収前のCursor市場シェア下落とどう関係するか不明。7月データでの更新が必要だが入手できておらず、H-XAI-002のmedium→low審査条件（3ヶ月継続）の検証が未完了のままである。
- Cursor $2B ARRの成長がGrok固有の価値によるものか、Claude/GPT APIへのアクセスによるものかの分離が不可能。買収完了後のGrok統合戦略が未公開であり、Cursorの成功をGrokの成功と読むことができるかの判別が立たない。
- Grok Buildオープンソース化・Plugin Marketplace・Voice Think Fast 2.0の追加が、開発者コミュニティでの採用重量をどれだけ動かすかが未測定。主要8フレームワーク枠外という事実との整合が取れていない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 | 出典 |
|---|---|---|
| [INFO-010](../Information/2026-08-03/collected-raw.md#INFO-010) | xAIニュース総覧: Grok Build OSS・Voice Think Fast 2.0・Copilot/Workspace/Bedrock/Databricks統合・Anthropicコンピュート・Grok Business(A-3) | https://x.ai/news |
| [INFO-015](../Information/2026-08-03/collected-raw.md#INFO-015) | Grok Voice Think Fast 2.0（WebSocket Speech-to-Speech API）・Grok Build OSS GitHub公開(A-3) | https://x.ai/news |
| [INFO-017](../Information/2026-08-03/collected-raw.md#INFO-017) | 2026エージェントフレームワーク比較8枠: Grok Buildは主要枠外(C-2) | エージェントフレームワーク比較 |
| [INFO-031](../Information/2026-08-03/collected-raw.md#INFO-031) | Vision Arena: Grok 4.5 1282点・15位。Claude Fable 5が首位(B-2) | https://arena.ai/leaderboard/vision |
| [INFO-059](../Information/2026-08-03/collected-raw.md#INFO-059) | LMSpeed推論ベンチマーク: Grok 4.5 54.6点・21位。Claude Opus 4.5が62.8首位(B-1) | https://lmarena.ai |
| [INFO-062](../Information/2026-08-03/collected-raw.md#INFO-062) | xAI $20B Series E調達（評価額$35B）(B-2) | 報道 |
| [INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) | AIコーディング3強: GitHub Copilot 29%/4.7M有料・Cursor 18%/$2B・Claude Code 18%。Grok固有採用分離不能(B-2) | https://uvik.net/blog/ai-coding-assistant-statistics/ |
| [INFO-058](../Information/2026-08-03/collected-raw.md#INFO-058) | トークン価格二極化: フロンティア維持 vs OSS無償化加速(B-2) | 市場データ |
| [INFO-060](../Information/2026-08-03/collected-raw.md#INFO-060) | DeepSeek V4 Pro: 97%低コスト・LiveCodeBench全球1位93.5%(B-1) | DeepSeek発表 |
| [INFO-061](../Information/2026-08-03/collected-raw.md#INFO-061) | OSS LLM: フロンティア70-90%能力・コストほぼゼロ(B-2) | ベンチマーク |
| [INFO-042](../Information/2026-08-03/collected-raw.md#INFO-042) | トランプAI大統領令・ペンタゴン8社契約・EU AI Act 8/2執行開始(A-1/A-3) | 政府発表 |
| [INFO-004](../Information/2026-07-27/collected-raw.md#INFO-004) | Grok 4.5全プラットフォーム展開（iOS/Android/Web/X・7/22）・Opus級・高速低コスト(A-3) | https://x.ai/news/grok-4-5-everywhere |
| [INFO-037](../Information/2026-07-27/collected-raw.md#INFO-037) | API価格比較: Grok 4.5 $2/$6・DeepSeek V4 Flash $0.14/$0.28最安(B-1) | https://venturebeat.com/technology/googles-gemini-3-6-flash-model-cuts-ai-agent-token-costs-by-up-to-65-on-long-horizon-engineering-tasks-and-3-5-pro-is-on-the-way |
| [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | SpaceX-Pentagon数十億ドルAIデータセンター協議・xAI軍事利用同意済み(B-2) | https://thebulletin.org/2026/07/the-rise-of-the-military-technology-complex/ |
| [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) | FLI AI Safety Index完全スコアカード: xAI F(0.65)・4位→7位悪化・存在的安全性全社最弱(A-1) | FLI報告書 |
| [Arbiter v4.55](../state/arbiter-2026-08-03.md) | 確度評価の完全根拠（H-XAI-004 ±0% indeterminate・H-XAI-002 ±0% medium・7指標全状態変更なし） | 内部参照 |
