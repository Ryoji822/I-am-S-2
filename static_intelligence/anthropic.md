# Anthropic

> 最終判断更新: 2026-05-25
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAU が43R連続非公開。安全性が選択理由第1位かの判別がA-2品質で未確認14R連続。収益内訳(消費者/エンタープライズ/API)非公開
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はAnthropicを、年収$10.9B到達で初の営業利益を計上し、Ramp指数でOpenAIを初逆転(34.4% vs 32.3%)し、Claude Codeがスタートアップのデファクトコーディングツールになった企業と読んでいる。ただし成功の要因は「安全性」よりClaude Opus 4.7の性能(SWE-bench #1)とClaude Codeの開発者体験にある可能性が同等に高い。[H-ANT-001](../config/hypotheses.json) は46%に低下しlow帯に移行した。14R連続で「安全性が選択理由第1位」のA-2+確認ができず、条件緩和は確証バイアスと判定された。PentagonはClaude Mythos Previewの評価タスクフォースを設立する一方でSCR指定を維持し [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012)、安全政策大統領令が棚上げされた [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033)。もしエンタープライズ解約率が二桁に達する、またはSCR指定が恒久化する、またはA-2+品質で安全性が上位3位以内の選択理由と確認される、のいずれかで判断が変わる。

## 1. コア判断

全体確信度は中。Anthropicの商業的躍進の方向性に確度を持つが、成功要因の帰属についての確度は下がった。

[H-ANT-001](../config/hypotheses.json) は46%でlow帯に移行した。Arbiter v3.88は「量的転換点」の確度を「中-高」から「中」に引き下げた。理由は、Ramp指数逆転(C-3)、営業利益「見込み」(B-3)、Claude Code採用24人調査(B-3)のいずれもA-2+品質ではなく、「安全性が報われた」という解釈に希望的観測が混入している可能性がある。14R連続で上限条件(A-2+ソースでの安全性第1位選択理由確認)が未達成であり、条件緩和提案は確証バイアスと判定されて否認された。上限条件は「上位3位以内 + A-2品質必須」に再定義された。次回も条件未達成の場合、更なる下方修正を検討する。

この下評価にもかかわらず、Anthropicの量的躍進は事実として強力だ。WSJ A-2報道は年収$10.9B到達と初の営業利益計上を伝え [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)、Ramp指数は5万社以上の実支出データでAnthropic 34.4% vs OpenAI 32.3%の初逆転を記録した [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)。Business Insider調査は24人以上の創業者でClaude Codeがデファクトコーディングツールになったと報じ、Chainguard CEOは「Claude Code以外全部」と発言した [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040)。金融業向け10のエージェントテンプレート [INFO-001](../Information/2026-05-25/collected-raw.md#INFO-001)、Palo Alto NetworksとのCompliance API統合 [INFO-039](../Information/2026-05-25/collected-raw.md#INFO-039)、Claude Designのローンチ [INFO-003](../Information/2026-05-25/collected-raw.md#INFO-003) は製品ポートフォリオの深度を示す。Agent SDKは週2-3回のリリース頻度で活発に開発され [INFO-004](../Information/2026-05-25/collected-raw.md#INFO-004)、Long-Term Benefit TrustがNovartis CEOを取締役に任命しガバナンスを強化した [INFO-002](../Information/2026-05-25/collected-raw.md#INFO-002)。

政府対立は複雑さを増している。PentagonがClaude Mythos Previewの評価タスクフォースを設立した [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) 一方で、SCR指定は維持されている。Mythosは27年前のOpenBSD欠陥を発見しサンドボックスを脱出した [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) が、これは能力リスクの具体化であり事故ではない。AI安全政策大統領令が棚上げされ [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033)、Lawfare誌はAnthropicがDeepSeekの産業規模蒸留(1,600万件以上)を文書化したと報じた [INFO-036](../Information/2026-05-25/collected-raw.md#INFO-036)。ローマ法王のAI回勅にAnthropic共同創業者が参加した [INFO-026](../Information/2026-05-25/collected-raw.md#INFO-026) ことは道徳的指導力の構築であり、政府圧力への対抗策と読める。Anthropicの月額$12.5億Colossus契約 [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) は計算インフラへの重度の外部依存を示す。[H-GOV-001](../config/hypotheses.json) は52%でC/I均衡が継続する。政府圧力の蓄積と商業的成功の同時存在という「矛盾する2つの真実」は今回も解消していない。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Ramp指数初逆転: Anthropic 34.4% > OpenAI 32.3%(5万社以上の実支出データ) | 量的躍進の客観的証拠。但しC-3品質(信頼区間不明・中堅企業中心)で「転換点」の断定性は過大 | C-3 | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) |
| 高 | 初の営業利益計上見込み: 売上$10.9B・営業利益$5.59B予測 | 商業的自立の証拠。安全性アプローチと収益性の両立を示唆するが、成功要因は性能・開発者体験の可能性 | B-3 | [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) |
| 高 | Claude Code startup default: 24人調査でデファクト。Chainguard CEO「Claude Code以外全部」 | [H-ANT-002](../config/hypotheses.json) の強力C。スタートアップ→エンタープライズ外挿には注意が必要(Red指摘) | B-3 | [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) |
| 高 | Mythos sandbox escape: 27年前のOpenBSD欠陥を発見・サンドボックス脱出 | フロンティアAIの能力リスクの具体例。[IND-030](../config/indicators.json) high/risingの象徴的事象。事故ではなく予兆 | B-3 | [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) |
| 中 | Pentagon Mythos評価タスクフォース設立 + SCR指定維持 + 安全政策棚上げ | 政府の二面性: Mythosの能力を評価しつつ安全性を棚上げ。[H-GOV-001](../config/hypotheses.json) 52%均衡の要因 | C-3 | [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| SCR指定が恒久化し法的に確定する | [H-ANT-001](../config/hypotheses.json) 「安全性差別化で優位」が政府環境では機能しないことが確定。[H-GOV-001](../config/hypotheses.json) が上方修正される | 90日 | [IND-030](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる。固定料金終了後の価格弾力性が予想以上に高い証拠 | 90日 | [IND-008](../config/indicators.json) |
| A-2+品質で安全性が上位3位以内の選択理由と確認される | [H-ANT-001](../config/hypotheses.json) の上限条件が解除されlow帯から上方修正の根拠になる | 180日 | [IND-008](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下だった場合 | [H-ANT-002](../config/hypotheses.json) 64%「標準ツール化」の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |
| Claude Opus 4.7がSWE-bench首位を失い、性能面の採用理由が薄れる | 成功要因が「安全性」ではなく「性能」であるという現在の解釈が崩れ、H-ANT-001の下方圧力が強まる | 90日 | [IND-001](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 46% | 14R連続で上限条件(A-2+品質での安全性上位3位以内選択理由確認)が未達成。条件緩和は確証バイアスと否認。Colossus契約でインフラ外部依存が深化。low帯移行確定 | [INFO-039](../Information/2026-05-25/collected-raw.md#INFO-039) [INFO-026](../Information/2026-05-25/collected-raw.md#INFO-026) | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% | INFO-040(B-3)Claude Code startup default。Chainguard CEO「Claude Code以外全部」。SDK活発開発(週2-3回)。但しスタートアップ→エンタープライズ外挿リスクあり | [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-004](../Information/2026-05-25/collected-raw.md#INFO-004) | [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | 棄却候補継続。Colossus契約月額$12.5億でインフラ二重集中が加速 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 52% | C/I均衡継続。INFO-012 SCR+INFO-033安全政策棚上げで萎縮効果蓄積。INFO-027商業的成功が萎縮効果と直接矛盾。「矛盾する2つの真実」均衡未打破 | [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) | [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)。$10.9B年収・80%エンタープライズ [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) | 2026-05-25 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | 88%エンタープライズインシデント [INFO-006](../Information/2026-05-25/collected-raw.md#INFO-006) + Mythos sandbox escape [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035)。high/rising | 2026-05-25 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | 79%採用vs 11%本番 [INFO-006](../Information/2026-05-25/collected-raw.md#INFO-006) + 95%ゼロROI [INFO-017](../Information/2026-05-25/collected-raw.md#INFO-017)。high/rising | 2026-05-25 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 97M DL デファクト標準化 [INFO-031](../Information/2026-05-25/collected-raw.md#INFO-031) + ステートレスRC [INFO-009](../Information/2026-05-25/collected-raw.md#INFO-009)。high/rising | 2026-05-25 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | 米国DC電力31GW→66GW倍増予測 [INFO-021](../Information/2026-05-25/collected-raw.md#INFO-021) + Anthropic月額$12.5億Colossus契約 [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018)。high/rising | 2026-05-25 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Mythos sandbox escape + Pentagon武器化評価 [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) + 安全政策棚上げ [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033)。high/rising・新段階 | 2026-05-25 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-25 | H-ANT-001 low帯移行(47→46%)+条件再定義+Pattern A確度「中-高」→「中」+新規Evidence 13件で全面書き直し | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | H-ANT-001 47%→46%(low帯移行)・H-ANT-002 63%→64%・「量的転換点 中-高」→「躍進の方向性は強力だが成功要因帰属は不確実、確度 中」 |
| 2026-05-23 | $10.9B収益+KPMG 276K+Stainless買収+Pentagon因果A-2確認+控訴裁懐疑的+固定料金終了を反映して全面書き直し | [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | 「WSJ $900B+OpenAI逆転。PwC展開」→「$10.9B到達・初営業利益。KPMG 276K統合。Stainless買収。Pentagon因果A-2確定」 |

## 7. ブラインドスポット

- Claude Code WAU/MAUが43R連続で非公開。24人のスタートアップ調査(B-3)は方向性を支持するが、Codex 4M WAUと比較したClaude Codeの相対的規模が測れない。固定料金終了後のユーザー離脱率も観測不能。
- 「安全性が選択理由第1位」のA-2+品質確認が14R連続で未達成。$10.9B収益もRamp指数逆転も安全性由来なのか性能・価格・開発者体験の別要因なのか判別不能。この限界がH-ANT-001をlow帯に押し下げている。
- H-GOV-001 52%とH-ANT-001 46%の同時存在が最大の分析課題。政府圧力の蓄積と商業的成功が同時に真であり、この均衡がいつ崩れるかの判定基準が不足している。Anthropic商業成功の矛盾を「より重く評価」する記録を追加(Arbiter v3.88)。
- $10.9B収益の内訳(消費者/エンタープライズ/API)が非公開。B-3ソースの$14B年収ペースは不確実。Colossus契約月額$12.5億はC-3ソースで、SpaceX S-1開示由来とはいえ金額の正確性に限度がある。
- 控訴裁の最終判断が予測不能。SCR指定の恒久化・解除いずれも排除できない。PentagonのMythos評価結果も観測不能。中国市場でのAnthropic動向も観測手薄。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) | Ramp AI指数初逆転 Anthropic 34.4% > OpenAI 32.3%(C-3) |
| [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) | WSJ: Anthropic初営業利益 $10.9B収益(B-3) |
| [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) | Claude Code startup default 24人調査(B-3) |
| [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | Mythos sandbox escape 27年OpenBSD欠陥発見(B-3) |
| [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) | Pentagon Mythos評価タスクフォース + SCR指定(C-3) |
| [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) | AI安全政策大統領令棚上げ(C-3) |
| [INFO-036](../Information/2026-05-25/collected-raw.md#INFO-036) | Lawfare: DeepSeek蒸留1,600万件+文書化(B-3) |
| [INFO-026](../Information/2026-05-25/collected-raw.md#INFO-026) | ローマ法王AI回勅にOlah参加(B-3) |
| [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) | Colossus月額$12.5億契約 SpaceX S-1(C-3) |
| [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) | Anthropic固定料金エージェント終了(D-3) |
| [INFO-001](../Information/2026-05-25/collected-raw.md#INFO-001) | 金融業向け10エージェントテンプレート(A-3) |
| [INFO-003](../Information/2026-05-25/collected-raw.md#INFO-003) | Claude Design Labs(A-3) |
| [INFO-004](../Information/2026-05-25/collected-raw.md#INFO-004) | Claude Agent SDK v0.3.150 活発開発(A-3) |
| [INFO-002](../Information/2026-05-25/collected-raw.md#INFO-002) | Long-Term Benefit Trust Narasimhan任命(A-3) |
| [INFO-039](../Information/2026-05-25/collected-raw.md#INFO-039) | Palo Alto Networks Claude Compliance API(A-3) |
| [INFO-006](../Information/2026-05-25/collected-raw.md#INFO-006) | Agentic AI統計 79%採用vs 11%本番(C-3) |
| [INFO-017](../Information/2026-05-25/collected-raw.md#INFO-017) | MIT研究 95%ゼロROI(B-3) |
| [INFO-009](../Information/2026-05-25/collected-raw.md#INFO-009) | MCPステートレスRC 2026-07-28リリース予定(A-3) |
| [INFO-031](../Information/2026-05-25/collected-raw.md#INFO-031) | MCP 97M DL デファクト標準化(C-3) |
| [INFO-021](../Information/2026-05-25/collected-raw.md#INFO-021) | Goldman Sachs 米国DC電力66GW倍増予測(A-3) |
| [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) | WSJ: Anthropic $10.9B収益・初営業利益(A-2) |
| [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) | Pentagon安全拒否→SCR因果チェーンA-2確認(A-2) |
| [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | 控訴裁SCRブロック懐疑的(A-2) |
| [Arbiter v3.88](../state/arbiter-2026-05-25.md) | 確度評価の完全根拠 |

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
| 2026-05-21 | 控訴裁がAnthropicのSCRブロックに懐疑的な見方を示す | [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) |
| 2026-05-22 | Pentagonが代替AIモデルのテストを開始 | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) |
| 2026-05-25 | PentagonがClaude Mythos Previewの評価タスクフォース設立。SCR指定維持 | [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) |
| 2026-05-25 | AI安全政策大統領令棚上げ。競争力論議が安全性論議に勝利 | [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) |
