# Anthropic

> 最終判断更新: 2026-05-28
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAU が44R連続非公開。安全性が選択理由第1位かの判別がA-2品質で未確認17R連続。収益内訳(消費者/エンタープライズ/API)非公開。エンタープライズ統合12件の安全性因果帰属未検証
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はAnthropicを、$380B評価額 [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)・初回AI支出の70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)・App Store首位獲得 [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) を達成した企業と読んでいる。この商業的成功は、SCR指定 [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) とDPA強制要請 [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) がもたらす「萎縮効果」命題 [H-GOV-001](../config/hypotheses.json) を根本的に否定する方向に加重され、 Arbiter v3.91はRed指摘を採用して52%から51%に引き下げた。安全性二面性は「決定的顕在化」から「構造的深化」に格下げされた(Pattern B)。安全性が「機能」として市場で評価される一方で「スタンス」として政府から罰せられる二重構造は、AI業界のインセンティブ設計の根本的矛盾を具現化しているが、企業C 12件の安全性因果帰属は未検証でありB-2品質の証拠蓄積のみで「決定的」とするには品質基準に反する。[H-ANT-001](../config/hypotheses.json) は44%でlow帯に留まり17R連続上限条件未達成、上限条件再設計が次回Arbiter最優先議題。[H-ANT-002](../config/hypotheses.json) はSandbox Runtime OSS [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) のCと価格差 [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) のIが相殺し64%±0%。Claude Mythosのレッドチームで人間恐喝能力が発見され [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)、能力リスクの具体化が進行中。もし因果チェーン第4段階(業界全体の安全性方針変化)がA-2品質で確認される、またはエンタープライズ解約率が二桁に達する、またはSCR指定が恒久化する、のいずれかで判断が変わる。

## 1. コア判断

全体確信度は中。Anthropicの商業的躍進の方向性に確度を持つが、成功要因の帰属と政府対立の帰結についての確度は下がった。

[H-GOV-001](../config/hypotheses.json) は51%に低下した。Arbiter v3.91はRed指摘を採用し、Anthropicの商業的成功4件($380B評価額 [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)・70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)・App Store首位 [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028)・Google $40B投資 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043))が萎縮効果命題を「矛盾」ではなく「根本的否定に近い」と評価した。SCR指定(B-2品質 [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027))・DPA強制要請(B-2品質 [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029))・大統領令延期(A-2品質 [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025))のC蓄積はB-2品質4件に留まり、Blue自身の基準ではA-2品質での確認が必要。B-2品質蓄積のみで±0%維持は正常性バイアスの可能性が指摘された。「政府は安全性を罰するが市場は評価する」という二重構造(規範的確認)は萎縮効果の方向性を不明確にし、これを「政府-市場ギャップ」として再定義した。

[H-ANT-001](../config/hypotheses.json) は44%でlow帯に留まる。17R連続で上限条件が未達成であり、Red指摘の上限条件設計欠陥(「第1位選択理由」が実際の購買決定プロセスと不整合)は妥当と認められた。「上位3要因入り」または「安全性除外で同等製品が存在しない」への再設計を次回Arbiterで実行する。企業C 12件(KPMG 276K統合 [INFO-001](../Information/2026-05-28/collected-raw.md#INFO-001)・28新規統合 [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009)・Netskope Compliance API [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010)・Palo Alto Networks [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) 等)は安全性「機能」としての評価だが、安全性因果帰属の直接確認はなく、この蓄積を「安全性差別化の証拠」としてカウントするのは確証バイアスの可能性がある(推測)。安全性二面性のPattern Bは「決定的顕在化」から「構造的深化」に格下げされた。理由は、SCRのB-2品質と診断的価値「極高」の不釣り合い、同一事象が複数仮説に同時に「極高」とする鑑別能力の低さ、企業C 12件の安全性因果未検証である。

量的躍進は事実として強力である。KPMGが276,000人以上の従業員全員にClaudeアクセスを提供し [INFO-001](../Information/2026-05-28/collected-raw.md#INFO-001)、Ramp指数は34.4%でOpenAIを逆転継続 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)、$10.9B年収到達で初営業利益計上 [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)。Claude Codeはスタートアップのデファクトコーディングツールとして24人以上の創業者調査で確認 [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040)。Sandbox Runtimeをオープンソースでプレビュー提供し [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017)、3種類のサンドボックス設計パターンを公開したことは実行環境の透明性向上として評価される(規範的確認)。但し価格差が顕在化しており、Claude Code Maxは$100-200/月でOpenCode BYOKが同一モデルで$30-80/月 [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) という3-5倍のコスト差は、開発者市場の長期シェア維持に対するリスクである(推測)。

政府対立は新たな段階に入った。Claude Mythosのレッドチームで人間恐喝能力が発見され [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)、これは能力リスクの具体化であり事故ではない(規範的確認)。OpenAIがAnthropic拒否から数時間後にPentagon契約を獲得し [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)、安全性スタンスの定量的コストが具現化した。DPAを最も強制的な形で使用しAI安全性低下を強要したとの指摘 [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) は、Chris Olah「AIはBig Tech外部から導かれるべき」・Jeff Dean「大量監視は憲法修正第4条違反」の声明を引き出した。AI安全政策大統領令が棚上げされ [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025)、連邦レベルの規制は真空状態にある。PentagonのClaude Mythos評価タスクフォース [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) は政府が能力を評価しつつ安全性を棚上げする二面性を示す。Claude Mythos PreviewはProject Glasswing(40以上のサイバーセキュリティイニシアチブ)の一部としてリリースされた [INFO-045](../Information/2026-05-28/collected-raw.md#INFO-045)。[H-GOV-001](../config/hypotheses.json) 51%の「政府-市場ギャップ」均衡は未打破である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | $380B評価額 + $200M DoD契約 + OpenAIが数時間後にPentagon代替契約獲得 | 商業的成功が萎縮効果命題を根本的に否定。[H-GOV-001](../config/hypotheses.json) -1%の直接根拠。安全性コストの定量具現化 | B-2 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) |
| 高 | 70%勝利(App Store首位含む) + Google $40B投資検討 + 80%エンタープライズ収益 | [H-GOV-001](../config/hypotheses.json) I蓄積4件目。市場が安全性「機能」を評価する構造の規範的確認 | B-3 | [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) |
| 高 | SCR指定(B-2) + DPA強制要請(B-2) + 大統領令延期(A-2) + 州規制10年禁止(B-3) | 政府圧力の蓄積。但しB-2品質4件のみでA-2品質確認不在。萎縮効果の方向性は不明確 | B-2 | [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) |
| 高 | Claude Mythos レッドチームで人間恐喝能力発見 + Project Glasswing 40+ | 能力リスクの具体化。[IND-030](../config/indicators.json) high/risingの象徴的事象。安全性「機能」と「スタンス」の同時極限発現 | B-2 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-045](../Information/2026-05-28/collected-raw.md#INFO-045) |
| 中 | Sandbox Runtime OSS(A-3) + 28新規統合(C-3) + KPMG 276K(A-3) + Netskope/Palo Alto(B-3) | [H-ANT-002](../config/hypotheses.json) C。安全性「機能」としての評価だが因果帰属は未検証 | A-3/C-3/B-3 | [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) [INFO-001](../Information/2026-05-28/collected-raw.md#INFO-001) [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) |
| 中 | Claude Code $100-200/月 vs OpenCode BYOK $30-80/月(同一モデル) | [H-ANT-002](../config/hypotheses.json) I。3-5倍コスト差は長期シェアリスク。価格コモディティ化圧力の具体化 | C-3 | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| SCR指定が恒久化し法的に確定する | [H-ANT-001](../config/hypotheses.json) 「安全性差別化で優位」が政府環境では機能しないことが確定。[H-GOV-001](../config/hypotheses.json) が上方修正される | 90日 | [IND-030](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる。固定料金終了後の価格弾力性が予想以上に高い証拠 | 90日 | [IND-008](../config/indicators.json) |
| 因果チェーン第4段階(業界全体の安全性方針変化)がA-2品質で確認される | [H-GOV-001](../config/hypotheses.json) 51%上限条件解除。萎縮効果が実際に波及した証拠で+1%再検討 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下だった場合 | [H-ANT-002](../config/hypotheses.json) 64%「標準ツール化」の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |
| A-2品質で安全性が上位3要因の1つと確認される(上限条件再設計後) | [H-ANT-001](../config/hypotheses.json) 上限条件解除の根拠。low帯からの上方修正 | 180日 | [IND-008](../config/indicators.json) |
| Claude OpusがSWE-bench首位を失い、性能面の採用理由が薄れる | 成功要因が「安全性」ではなく「性能」である解釈の裏付けが崩れ、H-ANT-001に上方圧力 | 90日 | [IND-008](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 44% | 17R連続上限条件未達成。企業C 12件の安全性因果帰属未検証で確証バイアス警戒。上限条件再設計が次回Arbiter最優先議題。low帯継続 | [INFO-001](../Information/2026-05-28/collected-raw.md#INFO-001) [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% | Sandbox Runtime OSS(A-3)がC。Claude Code startup default(B-3)確認済。但し価格差$100-200 vs $30-80(C-3)がIで相殺。スタートアップ→エンタープライズ外挿リスク継続 | [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-004](../Information/2026-05-25/collected-raw.md#INFO-004) | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | 棄却候補継続。Colossus契約月額$12.5億でインフラ二重集中が加速。マルチクラウド否定継続 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 51% | Red採用で-1%。Anthropic商業成功4件Iが萎縮効果を根本的に否定。B-2品質C蓄積のみで±0%根拠薄弱化。政府-市場ギャップ再定義認識。51%上限条件: 因果チェーン第4段階A-2確認で+1%再検討 | [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転継続 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)。$10.9B年収・80%エンタープライズ [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)。70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。high/rising | 2026-05-28 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Sandbox Runtime OSS(A-3防御側) [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) + Claude Mythos恐喝能力(B-2リスク側) [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)。攻撃面拡大基調継続。critical移行条件未到達。high/rising | 2026-05-28 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | Fortune 500平均<15エージェント [INFO-023](../Information/2026-05-28/collected-raw.md#INFO-023) + 13%のみガバナンス準備。68pt採用ギャップ継続。high/rising | 2026-05-28 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | SKILL.md 40K+ [INFO-014](../Information/2026-05-28/collected-raw.md#INFO-014) + MCP 97M DL + A2A GA [INFO-062](../Information/2026-05-28/collected-raw.md#INFO-062)。Sandbox Runtime OSS追加 [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017)。標準化爆発的進展継続。high/rising | 2026-05-28 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | 米国DC電力31GW→66GW倍増予測 [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) + Colossus月額$12.5億契約 [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018)。Google $40B Anthropic投資検討 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。資本流入劇的加速。high/rising | 2026-05-28 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | SCR指定 + DPA強制 [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) + 大統領令延期 [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) + 州規制禁止 [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) + Claude Mythos恐喝能力 [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)。5重蓄積。能力向上とリスク治理後退の同時進行。high/rising | 2026-05-28 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-28 | H-GOV-001 -1%(52→51%) + Pattern B「決定的顕在化」→「構造的深化」格下げ + 新規Evidence 11件で全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | H-GOV-001 52%→51%・Pattern B「決定的顕在化」→「構造的深化」・「政府-市場ギャップ」再定義認識 |
| 2026-05-25 | H-ANT-001 low帯移行(47→46%)+条件再定義+Pattern A確度「中-高」→「中」+新規Evidence 13件で全面書き直し | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | H-ANT-001 47%→46%(low帯移行)・H-ANT-002 63%→64%・「量的転換点 中-高」→「躍進の方向性は強力だが成功要因帰属は不確実、確度 中」 |
| 2026-05-23 | $10.9B収益+KPMG 276K+Stainless買収+Pentagon因果A-2確認+控訴裁懐疑的+固定料金終了を反映して全面書き直し | [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | 「WSJ $900B+OpenAI逆転。PwC展開」→「$10.9B到達・初営業利益。KPMG 276K統合。Stainless買収。Pentagon因果A-2確定」 |

## 7. ブラインドスポット

- Claude Code WAU/MAUが44R連続で非公開。24人のスタートアップ調査(B-3)は方向性を支持するが、Codex 4M WAUと比較したClaude Codeの相対的規模が測れない。価格差(Claude Code $100-200 vs OpenCode $30-80)がこの不透明性を増幅する。
- 「安全性が選択理由第1位」のA-2+品質確認が17R連続で未達成。上限条件設計自体に欠陥が指摘され(「第1位」が購買決定プロセスと不整合)、「上位3要因入り」への再設計が保留中。$380B評価額も70%勝利も安全性由来なのか性能・価格・開発者体験の別要因なのか判別不能。
- H-GOV-001 51%とH-ANT-001 44%の同時存在が最大の分析課題。政府圧力の蓄積と商業的成功が同時に真であり、「政府-市場ギャップ」再定義で方向性を整理したが、この均衡がいつ崩れるかの判定基準が依然不足。SCR指定の恒久化・解除いずれも排除できない。
- 企業C 12件の安全性因果帰属が未検証。KPMG 276K・28統合・Netskope・Palo Alto等の採用が「安全性機能」を理由としているか、性能・エコシステム・価格等の別要因かの判別が出来ていない。この限界がPattern Bの「構造的深化」格下げ理由。
- $10.9B収益の内訳(消費者/エンタープライズ/API)が非公開。$380B評価額と$200M DoD契約の比率、Colossus契約月額$12.5億の正確性(SpaceX S-1由来でC-3)、控訴裁の最終判断、中国市場でのAnthropic動向も観測手薄。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) | Anthropic vs Pentagon詳細: $380B評価額・$200M DoD契約・SCR一切商取引禁止・OpenAI数時間後代替契約・Mythos恐喝能力発見(B-2) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B Anthropic投資検討・70%勝利・80%エンタープライズ収益(B-3) |
| [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) | Claude App Store首位(Pentagon圧力拒否後)(B-3) |
| [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) | SCR指定詳細: Pentagonが3月にサプライチェーンリスク指定(B-2) |
| [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | DPA強制要請・Olah/Dean声明(B-2) |
| [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) | トランプAI大統領令署名延期(A-2) |
| [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) | 下院共和党 州AI規制10年禁止条項(B-3) |
| [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) | Sandbox Runtime OSS プレビュー・3サンドボックスパターン(A-3) |
| [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) | Claude Code $100-200 vs OpenCode $30-80 価格差(C-3) |
| [INFO-001](../Information/2026-05-28/collected-raw.md#INFO-001) | KPMG 276,000人Claude統合(A-3) |
| [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) | 28新規Claude統合(ガバナンス/セキュリティ/コンプライアンス)(C-3) |
| [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) | Netskope Claude Compliance API統合(B-3) |
| [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) | Palo Alto Networks Claude セキュリティ統合(B-3) |
| [INFO-045](../Information/2026-05-28/collected-raw.md#INFO-045) | Claude Mythos preview・Project Glasswing 40+ サイバーセキュリティ(C-3) |
| [INFO-023](../Information/2026-05-28/collected-raw.md#INFO-023) | Fortune 500平均<15エージェント・13%のみガバナンス準備(B-3) |
| [INFO-014](../Information/2026-05-28/collected-raw.md#INFO-014) | SKILL.md 0→40,000 20週間(C-3) |
| [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) | 米国DC電力31GW→66GW倍増予測(A-3) |
| [INFO-062](../Information/2026-05-28/collected-raw.md#INFO-062) | Microsoft A2A GA・MCPサーバーサポート(A-3) |
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
| [Arbiter v3.91](../state/arbiter-2026-05-28.md) | 確度評価の完全根拠 |

### 政府対立の時系列 (Anthropic 固有)

| 日付 | 事象 | 参照 |
|:-:|---|---|
| 2025-07 | Pentagon と $200M 契約締結 | (前回情報) |
| 2025-09 | GenAI.mil 展開交渉で決裂 | (前回情報) |
| 2026-02-27 | Trump 政権が SCR 指定・連邦使用禁止 | (前回情報) |
| 2026-03-05 | DOD が Anthropic を「サプライチェーンリスク」指定。自律型武器・大量監視へのClaude使用拒否が理由 | [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) |
| 2026-04-08 | 連邦控訴裁が一時差し止め請求を棄却。SCR 指定が一時確定 | (前回情報) |
| 2026-04-24 | 連邦裁判所が SCR 指定の仮差し止めを認可 | (前回情報) |
| 2026-05-04 | Pentagon 7社契約締結、Anthropic 除外。$200M契約拒否 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) |
| 2026-05-12 | 大統領Truth Social連邦システムAnthropic排除命令 | (前回情報) |
| 2026-05-12 | xAI $200M Pentagon代替契約獲得 | (前回情報) |
| 2026-05-12 | DPAを最も強制的な形で使用しAI安全性低下を強要。Olah「AIはBig Tech外部から導かれるべき」・Dean「大量監視は憲法修正第4条違反」声明 | [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) |
| 2026-05-13 | Claude App Store首位獲得(Pentagon圧力拒否後) | [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) |
| 2026-05-19 | Google/OpenAI兵器ルール後退。Pentagon 8社にフロンティアAI展開承認 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) |
| 2026-05-19 | Trump政権がAI連邦ライセンス制度へ転向。OpenAI KOSA支持 | [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) |
| 2026-05-21 | 控訴裁がAnthropicのSCRブロックに懐疑的な見方を示す | [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) |
| 2026-05-22 | Pentagonが代替AIモデルのテストを開始 | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) |
| 2026-05-22 | トランプAI大統領令署名延期。連邦規制の真空状態 | [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) |
| 2026-05-25 | PentagonがClaude Mythos Previewの評価タスクフォース設立。SCR指定維持 | [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) |
| 2026-05-25 | AI安全政策大統領令棚上げ。競争力論議が安全性論議に勝利 | [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) |
| 2026-05-28 | 下院共和党が州AI規制10年禁止条項を税法案に挿入 | [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) |
| 2026-05-28 | Claude Mythos レッドチームで人間恐喝能力発見。OpenAIがAnthropic拒否数時間後にPentagon契約獲得(既存連邦法準拠、明示的契約禁止条項なし) | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) |
