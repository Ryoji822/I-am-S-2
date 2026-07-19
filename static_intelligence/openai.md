# OpenAI

> 最終判断更新: 2026-07-19
> 全体確信度: 中低
> 情報非対称性: 収益内訳（API/Enterprise/Consumerセグメント・政府vs民間）が非公開（KIQ-OAI-001未回答継続・27R連続不在）。OpenAI 2025年収益約$130億確認（[INFO-008](../Information/2026-07-18/collected-raw.md#INFO-008) C-2）だがセグメント内訳は不変。H1 2025で純損失$39億報道（構造的赤字継続）。Pentagon $200M契約「all lawful use」条項獲得（[INFO-040](../Information/2026-07-18/collected-raw.md#INFO-040) B-2）。政府へ5%持分（$426億）提供提案（[INFO-004](../Information/2026-07-18/collected-raw.md#INFO-004) C-2）。AI価格戦争: GPT-4o入力50%・出力33%値下げ・Codexトークン課金移行（[INFO-047](../Information/2026-07-18/collected-raw.md#INFO-047) B-1）。GPT-5.6 3ティア展開（Luna $1/$6・Sol・Ultra mode・54%トークン効率化）（[INFO-025](../Information/2026-07-19/collected-raw.md#INFO-025) C-2・[INFO-056](../Information/2026-07-19/collected-raw.md#INFO-056) B-2）。BenchLM 7月: GPT-5.6 Sol 82点・Claude Mythos 5 83.9・Fable 5 83.7に次ぐ3位（[INFO-027](../Information/2026-07-19/collected-raw.md#INFO-027) C-2）。Arbiter v4.40 DEGRADED
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-OAI-001](../config/hypotheses.json) は46% mediumで±0%（v4.40 DEGRADED）。前回v4.39で47→46%の-1%が適用された後、Red Agent不在のため新規B2B採用定量証拠の不在（KIQ-OAI-001 27R連続不在）を理由に±0%が承認された。46%の引き下げ根拠はavailability≠adoptionの非対称性が未解消であること、Anthropic収益逆転（[INFO-005](../Information/2026-07-18/collected-raw.md#INFO-005) C-2）が前回-1%の核心根拠でありながらBlue自ら「強化された」と認めた状況で±0%提案したことが「自認と行動の乖離」の典型であったこと、KIQ-OAI-001 27R連続不在が保留ではなく引き下げ根拠であることの3点である。H-OAI-001（定量採用証拠不在）46% mediumとH-ANT-002（採用証拠あり）53% lowの逆転関係が継続している。

Pentagon $200M契約の獲得が確認された（[INFO-040](../Information/2026-07-18/collected-raw.md#INFO-040) B-2）。OpenAIは「all lawful use」条項付きで軍事作業の禁止を撤回し、ドローン防衛企業と提携した。同時にAnthropicがSCR指定・連邦禁止を受ける中、順応企業が報われる構造が制度化された。OpenAIは米国政府に5%持分（$426億相当）の提供も提案している（[INFO-004](../Information/2026-07-18/collected-raw.md#INFO-004) C-2）。政府関係の深化は[H-OAI-001](../config/hypotheses.json)のC方向（B2B支配）の材料だが、政府vs民間の収益内訳が26R連続不在のため質的評価は不能である。

AI価格戦争が公式に開始された（[INFO-047](../Information/2026-07-18/collected-raw.md#INFO-047) B-1）。GPT-4oのAPI価格が入力50%・出力33%引き下げられ、Codexがメッセージ単位からトークンベース課金に移行した。GPT-5.6は3価格帯構成（Luna $1/$6・Sol・Ultra mode）で企業向けに展開され（[INFO-025](../Information/2026-07-19/collected-raw.md#INFO-025) C-2・[INFO-056](../Information/2026-07-19/collected-raw.md#INFO-056) B-2）、アジェンティックタスクで54%のトークン効率改善を達成した。Ultra modeは複数AIエージェントを協調させて複雑タスクを高速完了し、ChatGPT Workがマルチエージェント実行を可能にした。オープンソースLLMがほぼ全ベンチマークでクローズドに追いついた一方で支出の80%は有料モデルへ向かい（[INFO-050](../Information/2026-07-18/collected-raw.md#INFO-050) B-2）、スイッチングコストの縮小とベンダーロックイン懸念（94%企業・[INFO-030](../Information/2026-07-18/collected-raw.md#INFO-030) B-2）が同時進行している。コモディティ化圧力と差別化戦略の二層構造が深化している。

[H-OAI-002](../config/hypotheses.json) は44% lowで±0%。囲い込み否定証拠の累積が継続している。[H-OAI-003](../config/hypotheses.json) は3% lowで±0%。商業化規模が圧倒的継続である。

## 1. コア判断

全体確信度は中低。本ラウンドの最重要判断は3つある。第一に、H-OAI-001 46% medium ±0%（v4.40 DEGRADED最大保守性原則）。第二に、GPT-5.6 3ティア展開（Luna/Sol/Ultra mode）とアジェンティックタスク54%トークン効率改善による製品戦略の転換。第三に、AI価格戦争の深化とコモディティ化圧力の量的加速。

### H-OAI-001 46% ±0%とavailability≠adoption非対称性

H-OAI-001は46% mediumで±0%（v4.40 DEGRADED）。前回v4.39で47→46%の-1%が適用された。根拠は3点ある。第一に、Anthropic収益逆転（[INFO-005](../Information/2026-07-18/collected-raw.md#INFO-005) C-2）は前回v4.38で-1%を適用した核心根拠であり、Blue Agent自ら「強化された」と認めながら±0%を提案したことは「自認と行動の乖離」の典型である。第二に、KIQ-OAI-001（収益内訳）が27R連続不在であり、これは保留ではなく引き下げ根拠である。第三に、H-OAI-001（定量採用証拠不在）46% mediumとH-ANT-002（採用証拠あり）53% lowの逆転関係が継続しており、確度評価の一貫性が損なわれている。v4.40はRed Agent不在のため新規B2B採用定量証拠の不在を理由に±0%を承認した。

収益内訳の不在は構造的制約として持続する。OpenAIの2025年収益は約$130億（[INFO-008](../Information/2026-07-18/collected-raw.md#INFO-008) C-2）だが、API/Enterprise/Consumerの構成比が不明であり、政府vs民間の内訳も非公開である。ウォーレン上院議員が7社にAI契約条項の開示を要求しているが（[INFO-033](../Information/2026-07-11/collected-raw.md#INFO-033) A-2）、回答されていない。収益絶対値の成長は確認できるが、B2B支配の収益的裏付けの質的評価は不可能である。

### Pentagon $200M契約と政府持分提案

OpenAIがペンタゴンと$200Mの契約を締結した（[INFO-040](../Information/2026-07-18/collected-raw.md#INFO-040) B-2）。「all lawful use」条項付きであり、軍事作業の禁止を撤回した。ドローン防衛企業との提携も確認された。ペンタゴンは分類ネットワークでの物流・情報分析・サイバーセキュリティ・作戦計画にOpenAIのAIを配備する（[INFO-072](../Information/2026-07-18/collected-raw.md#INFO-072) B-1）。

同時期にOpenAIは米国政府に5%持分（$426億相当）の提供を提案した（[INFO-004](../Information/2026-07-18/collected-raw.md#INFO-004) C-2）。Altmanの原則として「国内大規模監視禁止」と「武力行使の人間責任」を掲げたが、実態として「all lawful use」条項を受け入れたことは、発言と行動の乖離を示す。安全性堅持企業が連邦調達市場から排除され、順応企業が報われる構造が制度化された。

これは[H-OAI-001](../config/hypotheses.json)のC方向（政府セグメントでのB2B支配）の材料である。但し政府vs民間の収益内訳が26R不在のため、政府契約がB2B支配の収益的裏付けにどれだけ寄与するかの質的評価は不能である。

### GPT-5.6 3ティア展開とAI価格戦争の深化

AI価格戦争が公式に開始された（[INFO-047](../Information/2026-07-18/collected-raw.md#INFO-047) B-1）。GPT-4oのAPI価格が入力50%・出力33%引き下げられ、Codexがメッセージ単位からトークンベース課金に移行した。GPT-5.6は3モデル構成（Luna $1/$6・Sol・Ultra mode）で企業向けに発表され（[INFO-025](../Information/2026-07-19/collected-raw.md#INFO-025) C-2・[INFO-056](../Information/2026-07-19/collected-raw.md#INFO-056) B-2）、アジェンティックタスクで54%のトークン効率改善を達成した。Ultra modeは複数AIエージェントを協調させ、ChatGPT Workが並行サブエージェントの同時実行を可能にした。全プロバイダーで最も広い価格ラダー（GPT-5 nano $0.05からGPT-5.5 Pro $30/$180まで600倍）を維持している（[INFO-057](../Information/2026-07-19/collected-raw.md#INFO-057) A-3）。BenchLM 7月ランキングではGPT-5.6 Sol 82点で、Claude Mythos 5（83.9）・Fable 5（83.7）に次ぐ3位である（[INFO-027](../Information/2026-07-19/collected-raw.md#INFO-027) C-2）。

価格戦争の背景にはオープンソースの追従がある。オープンウェイトモデルはほぼ全ベンチマークでクローズドに追いつき（[INFO-050](../Information/2026-07-18/collected-raw.md#INFO-050) B-2）、推論コストは5〜10倍安い。WaPo調査でオープンウェイトはクローズドより68%安価と判明した（[INFO-076](../Information/2026-07-18/collected-raw.md#INFO-076) B-2）。DeepSeek V4 ProがGPT-5.6 Solと直接比較される水準に達した（[INFO-068](../Information/2026-07-18/collected-raw.md#INFO-068) B-2）。一方で支出の80%は依然有料モデルへ向かい、94%の企業がAIベンダーロックインを懸念し2/3がモデル戦略をヘッジしている（[INFO-030](../Information/2026-07-18/collected-raw.md#INFO-030) B-2）。

これらは[H-OAI-001](../config/hypotheses.json)のI方向（コモディティ化）の証拠である。短期的にはSCN-004（コモディティ化）を強化するが、Arbiterは中長期的には弱者淘汰から再集中（SCN-001/003）への相転移可能性を指摘した。C/I均衡構造は不変だが、I方向の圧力が量的に深化している。

### 企業AI採用の期待-実態ギャップ

McKinsey State of AIでAI採用率は88%だが、有意EBITインパクトを創出しているのは6%のみである（[INFO-018](../Information/2026-07-18/collected-raw.md#INFO-018) B-1）。Stanford AI Indexでも88%がAI使用を報告する一方、agentデプロイはほぼ全ビジネス機能で一桁台である（[INFO-035](../Information/2026-07-18/collected-raw.md#INFO-035) B-1）。95%のAI取り組みが測定可能なリターンゼロ（2024年）とのデータもある（[INFO-065](../Information/2026-07-18/collected-raw.md#INFO-065) B-1）。

54%の企業が既にAI agentインシデントを経験し（[INFO-034](../Information/2026-07-18/collected-raw.md#INFO-034) B-1）、91%の組織がAI agentを使用しているがNHI管理の成熟した戦略を持つのは10%のみである。期待と実態のギャップが30+独立ソースで確定的となった。これはH-OAI-001の「支配」の定式化に対する構造的制約であり、[IND-026](../config/indicators.json) high/risingの評価を強化する。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | H-OAI-001 ±0%: 46% medium維持。availability≠adoption非対称性未解消・収益逆転I証拠持続・KIQ-OAI-001 27R不在 | [H-OAI-001](../config/hypotheses.json) DEGRADED最大保守性原則で±0%承認 | Arbiter | [Arbiter v4.40](../state/arbiter-2026-07-19.md) |
| 高 | Pentagon $200M契約「all lawful use」: 分類ネットワーク配備・ドローン防衛企業提携・軍事禁止撤回 | [H-OAI-001](../config/hypotheses.json) C方向（政府B2B）。順応報酬構造制度化。[IND-030](../config/indicators.json) critical強化 | B-2 | [INFO-040](../Information/2026-07-18/collected-raw.md#INFO-040) [INFO-072](../Information/2026-07-18/collected-raw.md#INFO-072) |
| 高 | AI価格戦争: GPT-4o入力50%・出力33%値下げ・Codexトークン課金移行・GPT-5.4 $1.25/$7.50 | [H-OAI-001](../config/hypotheses.json) I方向。使用量ベース課金への産業構造転換。コモディティ化深化 | B-1 | [INFO-047](../Information/2026-07-18/collected-raw.md#INFO-047) |
| 高 | GPT-5.6 3ティア展開: Luna $1/$6・Sol・Ultra mode（マルチエージェント協調）・54%トークン効率改善・ChatGPT Work並行サブエージェント | [H-OAI-001](../config/hypotheses.json) C方向（フロンティア製品継続）兼I方向（Luna低価格）。3ティアで市場階層化戦略 | C-2 | [INFO-025](../Information/2026-07-19/collected-raw.md#INFO-025) [INFO-056](../Information/2026-07-19/collected-raw.md#INFO-056) |
| 中 | BenchLM 7月: GPT-5.6 Sol 82点（3位）・Claude Mythos 5 83.9・Fable 5 83.7 | [IND-025](../config/indicators.json) elevated。性能パリティ深化。Anthropicが性能首位でC方向の競争圧力 | C-2 | [INFO-027](../Information/2026-07-19/collected-raw.md#INFO-027) |
| 高 | オープンソース追従: OSSほぼ全ベンチマーク追いつき・68%安価・DeepSeek V4 Pro=GPT-5.6 Sol水準・支出80%は有料 | [H-OAI-001](../config/hypotheses.json) I方向。但し支出80%有料=C方向残存。C/I二層構造深化 | B-2 | [INFO-050](../Information/2026-07-18/collected-raw.md#INFO-050) [INFO-076](../Information/2026-07-18/collected-raw.md#INFO-076) |
| 高 | 政府持分5%提案: $426億相当・Altman原則（監視禁止・人間責任）と「all lawful use」の乖離 | [H-OAI-001](../config/hypotheses.json) 政府関係深化。発言と行動の乖離 | C-2 | [INFO-004](../Information/2026-07-18/collected-raw.md#INFO-004) |
| 高 | McKinsey 88%/6%: 採用率88%・有意EBITインパクト6%のみ | [IND-026](../config/indicators.json) high/rising強化。期待-実態ギャップ確定（30+ソース） | B-1 | [INFO-018](../Information/2026-07-18/collected-raw.md#INFO-018) |
| 高 | 94%企業ベンダーロックイン懸念・2/3がモデル戦略ヘッジ・スイッチングコスト縮小 | [H-OAI-002](../config/hypotheses.json) 囲い込み否定累積。排他性なし。「真のスイッチングコスト」はデータ・習慣・agentロジック | B-2 | [INFO-030](../Information/2026-07-18/collected-raw.md#INFO-030) |
| 中 | OpenAI Skills + Agent Skillsオープン標準: 再利用可能ワークフロー・MS Azure SDK公開 | [H-OAI-002](../config/hypotheses.json) 開放方向。但しSkillsは任意コード実行可能でセキュリティ攻撃面 | A-3 | [INFO-022](../Information/2026-07-18/collected-raw.md#INFO-022) [INFO-028](../Information/2026-07-18/collected-raw.md#INFO-028) |
| 中 | Azure Foundry Agent Service BYOM: 非Azure管理モデル接続・エンタープライズ統制 | [H-OAI-002](../config/hypotheses.json) 囲い込み否定。プロバイダー非依存継続 | A-3 | [INFO-032](../Information/2026-07-18/collected-raw.md#INFO-032) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-OAI-001](../config/hypotheses.json) が45%を割る | 「B2B支配的地位確立」仮説が棄却水準に接近。medium→low帯移行 | 180日 | [H-OAI-001](../config/hypotheses.json) |
| KIQ-OAI-001が回答されAPI/Enterprise/Consumer収益内訳が公表される | 46%の凍結が解消し、B2B支配の収益的裏付けの質的評価が可能になる | 90日 | [IND-027](../config/indicators.json) |
| AI価格戦争の下落トレンドが反転しフロンティア価格が上昇に転じる | コモディティ化の不可逆的加速判断が崩れる | 180日 | [IND-025](../config/indicators.json) |
| オープンウェイトモデルのエンタープライズ採用シェアが支出ベースで20%を超える | 「勝者集中」前提が崩れ、SCN-004が上昇する。H-OAI-001のI方向確定 | 90日 | [IND-027](../config/indicators.json) |
| AI agentインシデントで実被害（A-2品質）が報告される | IND-013がcriticalに移行し、エージェントプラットフォーム信頼性が構造的課題化する | 90日 | [IND-013](../config/indicators.json) |
| OpenAI政府持分5%提案が実行され、政府が取締役席を獲得する | 企業統治構造が質的変化し、H-OAI-001の政府依存度が確定する | 180日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIは2026年内にAgent機能を全面的にエンタープライズ向けに特化させ、B2B市場での支配的地位を確立する | 46% medium | ±0%（v4.40 DEGRADED最大保守性原則）。availability≠adoption非対称性未解消・収益逆転I証拠持続（INFO-005 C-2）・KIQ-OAI-001 27R不在。Pentagon $200M契約（INFO-040 B-2）・GPT-5.6 3ティア展開 Luna/Sol/Ultra mode・54%トークン効率（INFO-025 C-2・INFO-056 B-2）=C方向。AI価格戦争 GPT-4o 50%値下げ（INFO-047 B-1）・OSS追いつき68%安価（INFO-076 B-2）・DeepSeek V4 Flash ¥1/百万Token=I方向。C/I均衡構造不変だがI方向深化。medium維持 | [INFO-040](../Information/2026-07-18/collected-raw.md#INFO-040) [INFO-025](../Information/2026-07-19/collected-raw.md#INFO-025) [INFO-056](../Information/2026-07-19/collected-raw.md#INFO-056) | [INFO-047](../Information/2026-07-18/collected-raw.md#INFO-047) [INFO-005](../Information/2026-07-18/collected-raw.md#INFO-005) [INFO-050](../Information/2026-07-18/collected-raw.md#INFO-050) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはSkills/Shell/Compactionの独自実行環境でAgent開発者を囲い込み、MCP準拠の開放エコシステム上にプロプライエタリな上位レイヤーを構築する | 44% low | ±0%。囲い込み否定累積継続。Agent Skillsオープン標準（INFO-022 A-3）・Azure Foundry BYOM（INFO-032 A-3）・94%企業ロックイン懸念/2/3ヘッジ（INFO-030 B-2）。排他性なし。low帯確定度増加 | [INFO-022](../Information/2026-07-18/collected-raw.md#INFO-022) [INFO-032](../Information/2026-07-18/collected-raw.md#INFO-032) | [INFO-030](../Information/2026-07-18/collected-raw.md#INFO-030) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先目標とし、商業化と並行して研究開発に大規模資源を投入する | 3% low | ±0%。商業化規模（収益$130億・Pentagon契約・政府持分提案・IPO準備）圧倒的。行動は商業化一辺倒。AGI最優先支持A-2+証拠不在 | (該当なし) | [INFO-040](../Information/2026-07-18/collected-raw.md#INFO-040) [INFO-004](../Information/2026-07-18/collected-raw.md#INFO-004) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントでcritical | 54%企業がAI agentインシデント経験（INFO-034 B-1）・CSA 10件7週間（INFO-014 B-2）・91%組織使用/NHI戦略成熟10%。攻撃面拡大継続。critical移行条件（実被害A-2報告）未到達。構造的バイアス記録: 実被害A-2報告の不在≠実被害の不在。high/rising | 2026-07-19 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | GPT-5.6 3ティア Luna $1/$6・Ultra mode 54%トークン効率（INFO-025 C-2・INFO-056 B-2）・BenchLM GPT-5.6 Sol 82点3位（INFO-027 C-2）・MMLU全社>90%飽和（INFO-050 B-2）・OSS追いつき68%安価（INFO-076 B-2）・DeepSeek V4 Flash ¥1/百万Token。コモディティ化圧力深化。elevated/stable | 2026-07-19 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | McKinsey 88%/6% EBIT（INFO-018 B-1）・Stanford 88%/agent一桁台（INFO-035 B-1）・Databricks 75%デプロイ/一桁台（INFO-033 B-1）・95%リターンゼロ（INFO-065 B-1）・Klarna失敗（INFO-045 B-2）。期待-実態ギャップ確定（30+独立ソース）。high/rising | 2026-07-19 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | MCP AAIF寄贈（INFO-020 B-1）・Agent Skillsオープン標準（INFO-022/028）・Azure Foundry BYOM（INFO-032 A-3）・AWS Bedrock AgentCore（INFO-031 A-3）・Google Gemini Enterprise Agent Platform（INFO-017 A-3）・Oracle AI Agent Studio（INFO-023 A-3）。標準化加速。high/rising | 2026-07-19 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | GPT-5.6 Sol ARC-AGI-3 7.8%（前世代20倍・INFO-067 C-2）・Hassabis AGI 2030年±1年（INFO-059 B-2）・AIDE² RSI Level 1主張（INFO-074 B-3）・Gemini 3.0 Ultra MMLU 90%「Level 4 AGI」主張（INFO-078 B-2）。RSI具体化と客観ベンチマーク限界の同時進行。high/rising | 2026-07-19 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | 世界AI支出$2.59兆/+47%（INFO-053 B-1）・AIスタートアップVC $1315億/+52%（INFO-052 B-1）・Microsoft $460億インフラ首位（INFO-053）・NY州DC 3年モラトリアム議論（INFO-060 B-1）。資本流入加速・物理的制約ギャップ確定的。high/rising | 2026-07-19 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。Pentagon $200M「all lawful use」契約（INFO-040 B-2）・米初の自律型戦闘攻撃実行（[INFO-002](../Information/2026-07-19/collected-raw.md#INFO-002) B-3）・Anthropic SCR指定「米国企業初」（[INFO-045](../Information/2026-07-19/collected-raw.md#INFO-045) B-1）・SpaceX-Pentagon数十億ドルデータセンター協議（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）・中国AI agent規制7/15施行（INFO-038 B-1）・EU AI Act 8/2施行（INFO-036 B-1）・政府持分5%提案（INFO-004 C-2）。KIQ-MIL-001 27R不在。条件2充実史上最大水準 | 2026-07-19 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-19 | ターゲット編集。GPT-5.6 3ティア展開（Luna $1/$6・Sol・Ultra mode・54%トークン効率化）（[INFO-025](../Information/2026-07-19/collected-raw.md#INFO-025) C-2・[INFO-056](../Information/2026-07-19/collected-raw.md#INFO-056) B-2）・BenchLM 7月 GPT-5.6 Sol 82点3位（[INFO-027](../Information/2026-07-19/collected-raw.md#INFO-027) C-2）を新規反映。[H-OAI-001](../config/hypotheses.json) 46% medium ±0%（DEGRADED最大保守性原則）。KIQ-OAI-001 26R→27R・KIQ-MIL-001 26R→27R。IND-030 critical強化（自律型戦闘攻撃初確認・SCR指定米国企業初・SpaceX-Pentagon数十億ドル協議）。Arbiter v4.40 DEGRADED | [INFO-025](../Information/2026-07-19/collected-raw.md#INFO-025) [INFO-056](../Information/2026-07-19/collected-raw.md#INFO-056) [INFO-027](../Information/2026-07-19/collected-raw.md#INFO-027) | H-OAI-001 46%（±0%） |
| 2026-07-18 | 全面書き直し（7日freshness timeout）。[H-OAI-001](../config/hypotheses.json) 47→46%（availability≠adoption非対称性未解消・収益逆転I証拠持続・KIQ-OAI-001 26R）。Pentagon $200M「all lawful use」契約（INFO-040 B-2）・政府持分5%提案（INFO-004 C-2）・AI価格戦争 GPT-4o 50%値下げ（INFO-047 B-1）・OSS追いつき68%安価（INFO-076 B-2）・McKinsey 88%/6%（INFO-018 B-1）・94%ロックイン懸念（INFO-030 B-2）を新規反映。KIQ-OAI-001 26R・KIQ-MIL-001 26R。Arbiter v4.39 COMPLETE | [INFO-040](../Information/2026-07-18/collected-raw.md#INFO-040) [INFO-047](../Information/2026-07-18/collected-raw.md#INFO-047) [INFO-018](../Information/2026-07-18/collected-raw.md#INFO-018) | H-OAI-001 47→46% |
| 2026-07-11 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% medium ±0%。GPT-5.6 M365 Copilot優先モデル選定・RSI 57.9%・Q2収益$10.9B・ChatGPT 1Bユーザー・GPT-5.6価格体系・SkillCloakを反映 | [INFO-065](../Information/2026-07-11/collected-raw.md#INFO-065) [INFO-068](../Information/2026-07-11/collected-raw.md#INFO-068) | H-OAI-001 49%（±0%） |
| 2026-07-10 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% medium ±0%。GPT-5.6 GA・ARC-AGI-3 7.8%・Microsoft 27%所有を反映 | [INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) | H-OAI-001 49%（±0%） |
| 2026-07-03 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 48→49%。根拠を「核心パラメータ不在による確度変更保留」に修正 | [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) | H-OAI-001 48→49% |

## 7. ブラインドスポット

- 収益内訳（API/Enterprise/Consumer・政府vs民間）が27R連続不在（KIQ-OAI-001）。OpenAIの収益$130億の成長は確認できるが、政府契約（Pentagon $200M等）がB2B支配の収益的裏付けにどれだけ寄与するかの質的評価が不可能。46%の確度変更は常に根拠不足の状態で行われている。
- Pentagon $200M契約は強力なC証拠だが、「all lawful use」条項の受諾はAltmanが掲げた原則（監視禁止・人間責任）との乖離を示す。発言と行動の乖離がH-OAI-001の評価にどう影響するかの分析が不十分。政府持分5%提案が実行された場合の企業統治構造変化も未評価である。
- AI価格戦争は短期的にはコモディティ化（SCN-004強化）だが、中長期的には弱者淘汰から再集中への相転移可能性がある。この両義性をH-OAI-001の確度評価にどう反映するかの基準が不在。GPT-4o 50%値下げが収益性に与える影響も$39億純損失の文脈で評価不能である。
- オープンソースがほぼ全ベンチマークで追いついたにもかかわらず支出の80%が有料モデルへ向かう現象の持続性が不明。スイッチングコスト（データ・習慣・agentロジック）が囲い込みの新メカニズムとして機能している可能性があるが、94%の企業がヘッジしている中でこの構造がいつ崩れるかの予測が不能。
- McKinsey 88%/6%の乖離（採用率vs EBITインパクト）がOpenAIのB2B支配の持続性にどう影響するか。エンタープライズ顧客がAI投資のROIに疑問を持ち始めた場合、ChatGPT 1Bユーザーの規模優位が収益成長を支え続けるかの予測が不能。95%のAI取り組みがリターンゼロとのデータがこの懸念を強化している。
- H-OAI-001 46% mediumとH-ANT-002 53% lowの逆転関係（定量採用証拠不在企業の確度が採用証拠あり企業より低い）が、確度評価体系の一貫性に対する構造的課題として持続している。
- KIQ-MIL-001（人間却下比率）が27R連続完全不在。OpenAIが「all lawful use」条項を受け入れた中で、AI推奨の人間による却下が実施されているかの検証が不可能。Slotkin法案が人間監視免除権限を国防長官に付与しており、構造的非対称評価基準の適用が更に強化されている。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-004](../Information/2026-07-18/collected-raw.md#INFO-004) | OpenAI政府5%持分提案: $426億相当・2025年収益約$130億・トークン価格引き下げ検討(C-2) |
| [INFO-008](../Information/2026-07-18/collected-raw.md#INFO-008) | OpenAI収益約$130億・スイッチングコスト縮小・ChatGPT月$10億ペース(C-2) |
| [INFO-009](../Information/2026-07-18/collected-raw.md#INFO-009) | GPT-5.6 Sol + ChatGPT Workリリース: コラボレーション機能・Codex Record&Replay(A-3) |
| [INFO-018](../Information/2026-07-18/collected-raw.md#INFO-018) | McKinsey State of AI: 88%採用/6% EBIT・デモ↔本番ギャップ(B-1) |
| [INFO-022](../Information/2026-07-18/collected-raw.md#INFO-022) | OpenAI Skills: 再利用可能ワークフロー・Agent Skillsオープン標準(A-3) |
| [INFO-030](../Information/2026-07-18/collected-raw.md#INFO-030) | 94%企業ベンダーロックイン懸念・2/3ヘッジ・真のスイッチングコストはデータ・習慣・agentロジック(B-2) |
| [INFO-032](../Information/2026-07-18/collected-raw.md#INFO-032) | Azure Foundry Agent Service BYOM: 非Azure管理モデル接続・エンタープライズ統制(A-3) |
| [INFO-040](../Information/2026-07-18/collected-raw.md#INFO-040) | OpenAI Pentagon $200M契約「all lawful use」・Anthropic SCR指定・萎縮効果(B-2) |
| [INFO-047](../Information/2026-07-18/collected-raw.md#INFO-047) | AI価格戦争: GPT-4o入力50%値下げ・Codexトークン課金移行・GPT-5.4 $1.25/$7.50(B-1) |
| [INFO-050](../Information/2026-07-18/collected-raw.md#INFO-050) | OSS追いつき: ほぼ全ベンチマーク追いつく・支出80%有料・推論5-10倍安い(B-2) |
| [INFO-052](../Information/2026-07-18/collected-raw.md#INFO-052) | AIスタートアップVC $1315億/+52%・Databricks $1880億評価額(B-1) |
| [INFO-053](../Information/2026-07-18/collected-raw.md#INFO-053) | 世界AI支出$2.59兆/+47%・Microsoft $460億インフラ首位(B-1) |
| [INFO-067](../Information/2026-07-18/collected-raw.md#INFO-067) | GPT-5.6 Sol ARC-AGI-3 7.8% SOTA・Fable 5 GDPval-AA首位・6週間で3フロンティアモデル(C-2) |
| [INFO-068](../Information/2026-07-18/collected-raw.md#INFO-068) | DeepSeek V4 Pro=GPT-5.6 Sol水準・R1金融ベンチマーク最良(B-2) |
| [INFO-072](../Information/2026-07-18/collected-raw.md#INFO-072) | Pentagon移行期間全容: OpenAI分類NW配備・Altman原則・Anthropic拒否2条件(B-1) |
| [INFO-076](../Information/2026-07-18/collected-raw.md#INFO-076) | オープンウェイト68%安価(WaPo)・Mistral CI&T提携・ロボットVLモデル(B-2) |
| [INFO-033](../Information/2026-07-11/collected-raw.md#INFO-033) | ウォーレン上院議員: 7社AI契約開示要求・政府vs民間不透明(A-2) |
| [INFO-025](../Information/2026-07-19/collected-raw.md#INFO-025) | GPT-5.6 3ティア: Luna/Sol/Ultra mode・54%トークン効率改善・ChatGPT Work並行サブエージェント(C-2) |
| [INFO-027](../Information/2026-07-19/collected-raw.md#INFO-027) | BenchLM 7月: Claude Mythos 5 83.9・Fable 5 83.7・GPT-5.6 Sol 82(C-2) |
| [INFO-056](../Information/2026-07-19/collected-raw.md#INFO-056) | AI価格戦争: GPT-5.6 Luna $1/$6・Meta Muse Spark 1.1 $1.25/$4.25(B-2) |
| [INFO-057](../Information/2026-07-19/collected-raw.md#INFO-057) | OpenAI API料金600倍スプレッド: GPT-5 nano $0.05〜GPT-5.5 Pro $30/$180(A-3) |
| [Arbiter v4.40](../state/arbiter-2026-07-19.md) | 確度評価の完全根拠 |
