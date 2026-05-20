# Anthropic

> 最終判断更新: 2026-05-20
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAU が42R連続非公開。中国市場との競合観測は手薄
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はAnthropicを、**WSJが評価額$900B超でOpenAIを追い抜いたと報じ、PwCと組んで数十万人規模のClaude展開を始めた一方で、政府市場ではSCR指定と兵器ルール後退の二重圧力が強まっている企業**と読んでいる。最大の根拠は、WSJ A-2報道でAnthropicの評価額が$900Bを超えOpenAIを逆転した事実 [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) と、PwCが数十万人のグローバル人材にClaudeを展開し$100M Partner Networkを構築した事実 [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002) だ。TechCrunchは2025年5月以降の市場シェア4倍成長と金融がトップエンタープライズ顧客の40%を占めることを報じている [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047)。他方で、GoogleとOpenAIが兵器ルールを後退させ [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046)、安全性萎縮効果の圧力が強まっている。[H-ANT-001](../config/hypotheses.json)は49%上限条件付き、[H-ANT-002](../config/hypotheses.json)は63%。もし安全性が商業的選択理由第1位の直接定量証拠が出る、またはSDK分離課金が撤回される、またはDPAが実際に発動される、のいずれかで判断の前提が変わる。

## 1. コア判断

Anthropicは民間市場でOpenAIを抜いた。その事実をどう読むかで、今後の分析の方向が決まる。

WSJのA-2報道はAnthropicの評価額を$900B超とし、OpenAIを逆転した [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032)。これは非公開市場の推定値であり、正確な数字ではない。だが方向性は複数ソースで一貫している。TechCrunchは2025年5月以降のビジネス顧客でOpenAIを抜き、シェアを4倍に拡大したと報じた [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047)。金融がトップエンタープライズ顧客の40%を占めるという内訳は、特定業種への集中が進んでいることを示す。

PwCとの提携拡大は、エンタープライズ深度の具体的な裏付けだ。数十万人規模のグローバル人材にClaude CodeとCoworkを展開し、3万人のClaude認証プログラムを立ち上げ、CFOオフィス向け独立ビジネスユニットを新設した [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002)。保険アンダーライティング10週間から10日への短縮、セキュリティ対応の時間から分への短縮、納期改善最大70%が報告されている。BlackstoneとのJVも開始された [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055)。

Claude for Small BusinessはSMB市場への新規参入だ [INFO-004](../Information/2026-05-20/collected-raw.md#INFO-004)。QuickBooks、PayPal、HubSpot、Canva等と連携する15のエージェントワークフローと15のスキルを提供する。米GDPの44%を占めるSMBのAI採用遅れを解消する狙いで、10都市ツアーも実施中。Sonnet 4.6はコーディングとコンピューター使用で全面的に性能が向上し、1M tokenコンテキストウィンドウをベータで提供する [INFO-003](../Information/2026-05-20/collected-raw.md#INFO-003)。

政府との対立は二つの新しい圧力を受けた。第一に、GoogleとOpenAIが兵器ルールを後退させ [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046)、「安全性妥協への報復と報酬」の構造が一層鮮明になった。第二に、CDTの分析が連邦政府の行動を契機とするチリング効果を州・地方政府レベルまで波及すると警告している [INFO-025](../Information/2026-05-20/collected-raw.md#INFO-025)。[H-GOV-001](../config/hypotheses.json)は52%で維持された。しかし、Anthropicの$900B評価額と4倍シェア成長は萎縮効果への強力な反証として同時に存在しており [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047)、Arbiterは「矛盾する2つの真実」の均衡状態と評価した。

「安全性コスト≠安全性優位」の区別は継続する。PwC提携、SMB参入、$900B評価額は商業的成功の証明だが、安全性が選択理由の第一位である直接証拠は依然としてA-2+ソースで確認されていない。[H-ANT-001](../config/hypotheses.json)の49%上限条件は継続する。SDK分離課金は6月15日施行で[H-ANT-002](../config/hypotheses.json)と矛盾し続ける。

Andrej KarpathyがAnthropicに入社し事前学習研究チームを率いることになった [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051)。研究競争力への寄与は評価が難しいが、人材獲得競争での一つの信号ではある。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | WSJ: Anthropic評価額$900B+でOpenAIを逆転。$50B追加調達交渉中 | 民間市場での躍進のA-2品質定量証拠。H-ANT-001/H-ANT-002のC | A-2 | [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) |
| 高 | PwC: 数十万人にClaude展開・3万認証・CFO向け独立BU・納期70%改善 | エンタープライズ深度の最も具体的証拠。$100M Partner Network | A-3 | [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002) |
| 高 | TechCrunch: シェア4倍成長・金融がエンタープライズ顧客40%・実際のコストは価格の5-9倍 | 市場認識の変化を示す。有料プラン($100/月で$15,000相当消費)は利用深度の指標 | A-3 | [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) |
| 高 | Google/OpenAI兵器ルール後退 + CDT萎縮効果 + Trump規制転向 | H-GOV-001 52%の直接根拠。安全性圧力の構造化。Anthropic商業的成功とは矛盾する同時存在 | A-2/A-3 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) [INFO-025](../Information/2026-05-20/collected-raw.md#INFO-025) [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) |
| 高 | Claude for Small Business: 15ワークフロー・15スキル・SMBツール連携 | SMB市場への新規参入。エンタープライズ集中から消費者・SMBへの拡張 | A-3 | [INFO-004](../Information/2026-05-20/collected-raw.md#INFO-004) |
| 高 | Blackstone+Anthropic JV: AIツール企業販売 | PE業界経由のエンタープライズ拡販チャネル | A-2 | [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055) |
| 中 | Sonnet 4.6: コーディング70%好評・1M token・OSWorld大幅改善 | 性能維持の証拠。ただしMythos以外でOpus 4.7の5ベンチマーク勝利はGemini 2.5 Proに対するもの [INFO-030](../Information/2026-05-20/collected-raw.md#INFO-030) | A-3 | [INFO-003](../Information/2026-05-20/collected-raw.md#INFO-003) |
| 中 | Andrej Karpathy入社: 事前学習研究チーム統括 | 研究人材の獲得信号。Codex・DeployCo展開中のOpenAIからの流出 | A-2 | [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DPAが実際に発動され、Anthropicが強制的に政府契約に組み込まれる | H-GOV-001「政府圧力による萎縮効果」が確定。H-ANT-001の根拠も崩れる | 90日 | [IND-030](../config/indicators.json) |
| Anthropicが`lawful use`条項を受諾し政府契約に回帰する | コア判断「民間優先・政府放棄」が崩れる | 90日 | [IND-030](../config/indicators.json) |
| A-2+ソースで安全性が商業的選択理由第1位の定量確認ができる | H-ANT-001 49%上限条件が解除され、安全性優位の直接証明となる | 180日 | [IND-008](../config/indicators.json) |
| SDK分離課金が6月15日以降に撤回または緩和される | H-ANT-002のコスト増Iが消滅。確度上方修正の根拠 | 60日 | [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |
| Claude Code WAU/MAUが定量開示され、Codex比で1/5以下だった場合 | H-ANT-002「標準ツール化」63%の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 49% | PwC提携+$900B+4倍シェアは商業的Cだが「安全性が選択理由」の因果はB-3レベルの間接証拠のみ。49%上限条件: A-2+での定量確認が必要。9連邦機関Claude停止(A-2)は強力I | [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002) [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) | [INFO-025](../Information/2026-05-20/collected-raw.md#INFO-025) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 63% | GitHub 4%コミット+Walleye 100%は強力C。Grok Build Beta競合+MCP脆弱性がI。SDK分離課金6月15日施行が未解決のI。安定観察中 | [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002) | [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | SpaceXAI Colossus全容量契約+$300億協議でインフラ集中深化。棄却候補継続 | [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055) | Colossus全容量契約で二重集中加速 |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 52% | Google/OpenAI兵器ルール後退(A-2)+CDT萎縮効果(A-3)+Trump規制転向(A-2)で萎縮効果7C蓄積。しかしAnthropic $900B(A-2)+4倍シェア(A-3)は萎縮効果と直接矛盾。「矛盾する2つの真実」の均衡状態で確度上昇は不当(Arbiter判断) | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) [INFO-025](../Information/2026-05-20/collected-raw.md#INFO-025) | [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp AI Index 34.4%(初逆転) [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。TechCrunch 4倍成長 [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) | 2026-05-20 |
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt以上/期で high | Opus 4.6 5ベンチマークGemini 2.5 Pro勝利 [INFO-030](../Information/2026-05-20/collected-raw.md#INFO-030)。Sonnet 4.6 OSWorld大幅改善 [INFO-003](../Information/2026-05-20/collected-raw.md#INFO-003) | 2026-05-20 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | TanStack npm攻撃 [INFO-008](../Information/2026-05-20/collected-raw.md#INFO-008)+AgentTrap 141タスク [INFO-017](../Information/2026-05-20/collected-raw.md#INFO-017)+METR 43%破損 [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049)。high水準 | 2026-05-20 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | METR 43%破損+Klarna再採用+15%ROI+Gartner 40%失敗+76%監査不可で失敗5:成功1。high移行確定 [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049) | 2026-05-20 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | AAIF 43新メンバー+Azure MCP Server+Agent Skills 500++MCP 78%導入率。high水準 [INFO-012](../Information/2026-05-20/collected-raw.md#INFO-012) | 2026-05-20 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | $1Tデータセンター+Anthropic $900B+Mistral $2.3B+Blackstone $5B JV。high水準 [INFO-034](../Information/2026-05-20/collected-raw.md#INFO-034) | 2026-05-20 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Google/OpenAI兵器ルール後退(A-2)+CDT萎縮効果(A-3)+Trump規制転向(A-2)でA-2+確認充足。high維持 [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) | 2026-05-20 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-20 | WSJ $900B+OpenAI逆転+PwC提携+Claude for SMB+4倍シェア成長+兵器ルール後退を反映して全面書き直し | [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-20/collected-raw.md#INFO-004) [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) | 「Pentagon因果チェーン制度化+Ramp初逆転+$30B収益」→「WSJ $900B+でOpenAI逆転確定。PwC数十万人展開。SMB参入。兵器ルール後退で萎縮効果圧力強まるがAnthropic商業的成功と矛盾」 |

## 7. ブラインドスポット

- Claude Code WAU/MAUが42R連続で非公開。GitHub 4%コミットは代理指標だが、Codex 4M WAUと比較した相対的市場シェアが外部から測れない。SDK分離課金後のユーザー離脱率も観測不能。
- 「安全性が商業的優位性に直結する」直接証拠が依然としてA-2+ソースで確認されていない。Ramp逆転も4倍成長も安全性由来なのか性能・価格・エコシステムの他要因なのか判別不能。
- H-GOV-001 52%とH-ANT-001 49%の同時存在が最大の分析課題。萎縮効果で安全性が低下するという読みと、安全性差別化で優位に立つという読みが論理的緊張関係にある。Arbiterは「矛盾する2つの真実」と評価したが、この均衡がいつ崩れるかの判定基準が不足している。
- $900B評価額の妥当性が外部から検証できない。収益run rateの内訳(消費者vsエンタープライズvs API)も非公開。PwC提携の実質的収益寄与も不明。
- DPA発動の実際の可能性が評価できない。脅迫が実行されるか交渉カードとして使われているかの判別が不可能。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) | WSJ: Anthropic評価額$900B+でOpenAI逆転(A-2) |
| [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002) | PwC: 数十万人Claude展開・3万認証・CFO向け独立BU・納期70%改善(A-3) |
| [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) | TechCrunch: シェア4倍成長・金融40%・2028シナリオ論文(A-3) |
| [INFO-004](../Information/2026-05-20/collected-raw.md#INFO-004) | Claude for Small Business: 15ワークフロー・15スキル(A-3) |
| [INFO-003](../Information/2026-05-20/collected-raw.md#INFO-003) | Claude Sonnet 4.6: 1M token・コーディング70%好評(A-3) |
| [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) | Google/OpenAI兵器ルール後退・Pentagon 8社承認(A-2) |
| [INFO-025](../Information/2026-05-20/collected-raw.md#INFO-025) | CDT: Pentagon-Anthropic紛争の萎縮効果(A-3) |
| [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) | Trump規制転向・Andrej Karpathy入社(A-2) |
| [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055) | Blackstone+Anthropic JV・Google+Blackstone $5B(A-2) |
| [INFO-052](../Information/2026-05-20/collected-raw.md#INFO-052) | Anthropic 2028シナリオ論文: 米中AI競争(A-3) |
| [INFO-030](../Information/2026-05-20/collected-raw.md#INFO-030) | Opus 4.6 Gemini 2.5 Proに5ベンチマーク勝利(B-3) |
| [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049) | METR 43%本番破損・0%自信(A-3) |
| [Arbiter v3.83](../state/arbiter-2026-05-20.md) | 確度評価の完全根拠 |

### 政府対立の時系列 (Anthropic 固有)

| 日付 | 事象 | 参照 |
|:-:|---|---|
| 2025-07 | Pentagon と $200M 契約締結 | (前回情報) |
| 2025-09 | GenAI.mil 展開交渉で決裂 | (前回情報) |
| 2026-02-27 | Trump 政権が SCR 指定・連邦使用禁止 | (前回情報) |
| 2026-03-05 | DOD が Anthropic を「サプライチェーンリスク」指定 | (前回情報) |
| 2026-04-08 | 連邦控訴裁が一時差し止め請求を棄却。SCR 指定が一時確定 | (前回情報) |
| 2026-04-24 | 連邦裁判所が SCR 指定の仮差し止めを認可 | (前回情報) |
| 2026-05-04 | Pentagon 7社契約締結、Anthropic 除外。$200M契約拒否 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) |
| 2026-05-12 | 大統領Truth Social連邦システムAnthropic排除命令 | (前回情報) |
| 2026-05-12 | xAI $200M Pentagon代替契約獲得 | (前回情報) |
| 2026-05-19 | Google/OpenAI兵器ルール後退。Pentagon 8社にフロンティアAI展開承認 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) |
| 2026-05-19 | Trump政権がAI連邦ライセンス制度へ転向。OpenAI KOSA支持 | [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) |
