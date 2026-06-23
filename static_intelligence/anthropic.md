# Anthropic

> 最終判断更新: 2026-06-23
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが非公開。安全性が選択理由上位3要因以内かの判別がA-2品質で未確認(32R連続上限条件未達成・Kano再定式化実行済み)。収益内訳(消費者/エンタープライズ/API)非公開。CVE-8.7(CVSS 8.7 RCE)が安全性差別化仮説に継続的矛盾。H-GOV-001(a)/(b)分割実行済み。(a)Anthropic固有政府介入はC=10件・I=3件で54% medium（56→55→54%・2R連続-1%・Google $40B投資・$1T評価額+Jumper流入・研究者非難の三重Iが持続性・合法性を三重に挑戦）。(b)業界全体萎縮効果はH-GOV-002として分離（21% low）。Claude Code 90%自コードベースはAnthropic自己評価（利益相反・C蓄積から除外）。Claude Code DAU/日常利用者データ4R連続不在（v4.16条件到達・medium→low移行検討起動・DEGRADED制約で次回COMPLETE保留）。IPO自己選択バイアスの除外が未完了。輸出管理指令(INFO-054 A-1)の原因となったAmazon研究者論文の技術的妥当性について専門家間で意見分裂（Moussouris「輸出管理をtriggeredすべきでない」vs 商務省指令）。Arbiter v4.17はDEGRADED状態（Red Agent失敗・2R連続）。Google $40B投資(INFO-045 B-2)は「最大$40B」であり最終額は未確定
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

GoogleがAnthropicに最大$40Bの投資を報じられた [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045)（B-2）。同時にAnthropicはセカンダリ市場で$1T評価に達し [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066)（B-2）、ノーベル賞受賞者John JumperがDeepMindからAnthropicに移籍した。これら3事象はAnthropicの商業的・研究的吸引力が政府圧力にも増さず加速していることを示す。[H-GOV-001](../config/hypotheses.json) は56%から54%に2R連続の-1%低下となった。介入能力の拡大（DPA検討・8社開放・サプライチェーンリスク）はC蓄積だが、Google $40B投資・$1T評価+Jumper流入・研究者非難の三重Iが先例確立核心要件（持続性・合法性）を三重に挑戦している。介入能力の拡大と介入効果の不在の不均衡が2R連続で拡大した。[H-ANT-002](../config/hypotheses.json) は64%から62%に低下した。Claude Code DAU/日常利用者データ4R連続不在（v4.16条件到達）でmedium→low移行検討が起動したが、DEGRADED制約で実際のラベル変更は次回COMPLETEラウンドに保留されている。

[IND-030](../config/indicators.json) はcriticalを維持。Operation Epic Fury 96h/2,000標的が複数独立ソースで再確認され [INFO-065](../Information/2026-06-23/collected-raw.md#INFO-065)、DPA行使検討 [INFO-031](../Information/2026-06-23/collected-raw.md#INFO-031) で「設計通り」と「技術的安全事故」の区別の実質崩壊がさらに進行した。条件2（A-2品質技術的安全事故報告）は未到達。

## 1. コア判断

全体確信度は中。本ラウンドの最大の構造的変化はGoogleのAnthropicへの最大$40B投資報道 [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045)（B-2）と、それに続くAnthropic $1Tセカンダリ市場評価・John Jumper移籍 [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066)（B-2）である。

Googleが最大$40Bを投じることは、AI市場の競争構造を変える可能性がある。AnthropicはAWS（Amazon）を主要インフラとしながら、Googleから最大$40Bの資金を受け入れる。これはインフラ二重集中を深化させる方向でもあり、同時にAnthropicの独立性を支える方向でもある。ただし「最大$40B」であり最終投資額は未確定。Google自身がGeminiを展開する中で競合への大型投資を行うことは、プラットフォーム戦略の転換を示唆する。[H-ANT-003](../config/hypotheses.json)（マルチクラウド戦略）は6% lowで、マルチクラウド均衡の前提が更に遠ざかる。

John JumperのDeepMindからAnthropicへの移籍は、安全性中心文化がトップ研究者を惹きつけていることを示す証拠である。AlphaFoldでノーベル化学賞を受賞したJumperの移籍は、研究コミュニティにおけるAnthropicの吸引力の象徴的事例だ。ただし個人の移籍はトレンドの指標にはなっても、組織能力の量的評価には直結しない。[IND-028](../config/indicators.json) のAGI到達度評価におけるRSI具体化（Anthropic AI 80%内部コード寄与 [INFO-057](../Information/2026-06-23/collected-raw.md#INFO-057)）との関連で記録する。

[H-GOV-001](../config/hypotheses.json) は56%から54%に低下した（2R連続-1%: v4.16 56→55%・v4.17 55→54%）。Arbiter v4.17の判断では、介入ツールの拡大（DPA検討・サプライチェーンリスク・8社開放）はC蓄積だが、3つのI方向証拠が先例確立核心要件を三重に挑戦している。第一にGoogle $40B投資 [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) は民間資本が政府圧力を上回る勢いであることを示す。第二に$1T評価額+Jumper流入 [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) はAnthropicの商業的・研究的吸引力が政府圧力にも増さず加速していることを示す。第三に研究者非難 [INFO-033](../Information/2026-06-23/collected-raw.md#INFO-033) は政府介入の正統性への学術界からの挑戦である。介入能力の拡大（C）と介入効果の不在（I）の不均衡が2R連続で拡大している。medium維持はC=10件の蓄積強度を反映する。

[H-ANT-002](../config/hypotheses.json) は64%から62%に低下した（2R連続-1%: v4.16 64→63%・v4.17 63→62%）。Claude Code DAU/日常利用者データが4R連続不在となり（v4.16設定条件到達）、medium→low移行検討が起動した。ただしDEGRADED制約（Red Agent失敗2R連続）により、実際のラベル変更は次回COMPLETEラウンドでRed交差検証後に実施される。62%維持はFable 5 #1・Opus 4.8 SWE-bench #1等の技術的リーダーシップへの依存度が高い。

[H-ANT-001](../config/hypotheses.json) は37%で±0%維持。Kano再定式化後の上限条件未達成が継続する。[H-GOV-002](../config/hypotheses.json) は21%で±0%維持。業界全体萎縮効果の定量証拠は不在のまま。NSFが基礎科学研究プログラム予算を20-30%削減したこと [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) は、連邦政府のAI安全研究支援縮小の一環だが、KIQ-GOV-002絶対条件（安全性研究予算の経時的定量データ）は依然20R連続未達成である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | GoogleがAnthropicに最大$40B投資と報じられる。Amodei+HassabisがG7で米国主導AI連合要請 | [H-GOV-001](../config/hypotheses.json) I側B-2品質。民間資本が政府圧力を上回る勢い。[H-ANT-003](../config/hypotheses.json) インフラ二重集中深化 | B-2 | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) |
| 高 | Anthropic $1Tセカンダリ市場評価。2年で$5B調達計画。12+産業参入予定 | [H-GOV-001](../config/hypotheses.json) I側。商業的成功の持続。[H-ANT-001](../config/hypotheses.json) 商業的競争力の裏付け | B-2 | [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| 高 | ノーベル賞John JumperがDeepMindからAnthropicに移籍 | [H-GOV-001](../config/hypotheses.json) I側。安全性中心文化がトップ研究者を惹きつける。[IND-028](../config/indicators.json) 関連 | B-2 | [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| 高 | NSF基礎科学プログラム予算20-30%削減。AI安全研究支援縮小 | [H-GOV-002](../config/hypotheses.json) 文脈。KIQ-GOV-002絶対条件20R連続未達成。安全性研究予算の経時データ依然不在 | B-2 | [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| 高 | 連邦判事Rita Lin: Anthropic連邦禁止を「違法な報復」と判断・法院令で阻止 | [H-GOV-001](../config/hypotheses.json) I側A-2品質。政府介入の持続性に対する初のA-2否定的証拠 | A-2 | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) |
| 高 | 商務省がFable 5/Mythos 5の全外国人アクセス禁止（輸出管理指令） | [H-GOV-001](../config/hypotheses.json) C側A-1品質。政府介入の具体的手法 | A-1 | [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) |
| 高 | Grok Gov Model Operation Epic Fury 96h/2,000標的/2,000発 | [IND-030](../config/indicators.json) critical維持。順応報酬構造の最強証拠。複数独立ソースで再確認 | A-2 | [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) [INFO-065](../Information/2026-06-23/collected-raw.md#INFO-065) |
| 高 | ミナブ小学校攻撃168人死亡・Operation Epic Fury全体600-1,400+民間人死亡 | [IND-030](../config/indicators.json) 民間被害のB-2品質証拠 | B-2 | [INFO-043](../Information/2026-06-21/collected-raw.md#INFO-043) [INFO-049](../Information/2026-06-21/collected-raw.md#INFO-049) |
| 高 | DPA行使検討・Pentagon 8社選別契約（Anthropic除外）・サプライチェーンリスク | [H-GOV-001](../config/hypotheses.json) C側。介入ツール拡大。順応報酬構造の制度化 | B-2 | [INFO-031](../Information/2026-06-23/collected-raw.md#INFO-031) [INFO-029](../Information/2026-06-23/collected-raw.md#INFO-029) |
| 高 | 全連邦政府でのAnthropic使用停止命令。SCR指定（Huawei級ラベル・米国企業初） | [H-GOV-001](../config/hypotheses.json) C側A-2品質。(a)分割後の中核証拠。但しRita Lin判事が「違法な報復」と判断 | A-2 | [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) |
| 高 | PentagonがAnthropicを提訴。政府調達からの排除を法的に強制 | [H-GOV-001](../config/hypotheses.json) C側A-2品質。法的帰趗は未確定 | A-2 | [INFO-044](../Information/2026-06-17/collected-raw.md#INFO-044) |
| 高 | Anthropic「Policy on the AI Exponential」。政府のブロック・リコール権限を提唱 | [H-ANT-001](../config/hypotheses.json) 規制捕獲戦略代替解釈の評価対象 | A-3 | [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) |
| 高 | Claude Fable 5/Mythos 5リリース。大部分ベンチマークSOTA | [H-ANT-002](../config/hypotheses.json) 確認的蓄積。但しFable 5/Mythos 5はアクセス停止中 | A-3 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) |
| 高 | Claude Code採用3%→24%（米国）。JetBrains 1万人調査 | [H-ANT-002](../config/hypotheses.json) C蓄積。DAU/日常利用者データは4R連続不在 | B-3 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) |
| 高 | CVE-8.7（CVSS 8.7 RCE脆弱性）がClaude Codeで発見 | [H-ANT-001](../config/hypotheses.json) I重み「高」。安全性差別化企業の主力製品におけるCVSS 8.7のRCE | A-3 | [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) |
| 高 | トークンコスト$30→<$1/MTok（2023年初→2026年6月） | SCN-004 コモディティ化C蓄積。围い込み価値の侵食圧力 | A-3 | [INFO-025](../Information/2026-06-10/collected-raw.md#INFO-025) |
| 中 | Anthropic S-1秘密提出。$965B評価額。IPO競争でOpenAI $852B上回る | [H-ANT-001](../config/hypotheses.json) 商業的成功の継続 | B-3 | [INFO-033](../Information/2026-06-10/collected-raw.md#INFO-033) |
| 中 | Agent SDK課金分離。6月15日からプログラマティック使用を別課金 | [H-ANT-002](../config/hypotheses.json) 围い込み強化シグナル | C-3 | [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) |
| 中 | 初級テック採用25%減少・Stanford 2026 AI Indexで26歳未満SE雇用-20% | [H-CAR-002](../config/hypotheses.json) 「書く能力」価値変容の支持 | B-3 | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 判事Rita Linの法院令が上訴裁判所で覆る | [H-GOV-001](../config/hypotheses.json) のI側A-2証拠が弱体化。54%から再上昇 | 180日 | [IND-030](../config/indicators.json) |
| 安全性がA-2品質でエンタープライズ選択理由第1位と確認される | [H-ANT-001](../config/hypotheses.json) 上限条件解除。37%下限宣言の無効化 | 180日 | [IND-008](../config/indicators.json) |
| 規制産業と非規制産業でのClaude採用率に定量差が確認される | [H-ANT-001](../config/hypotheses.json) Kano移行の定量検証 | 180日 | [IND-008](../config/indicators.json) |
| CVE-8.7が深刻な実被害（エンタープライズ環境での悪用確認）に至る | [H-ANT-001](../config/hypotheses.json) 37%から更なる下方。[IND-013](../config/indicators.json) critical移行 | 90日 | [IND-013](../config/indicators.json) |
| SCR指定が恒久化し上訴裁判所も合憲と判断する | [H-GOV-001](../config/hypotheses.json) 54%から再上昇。政府介入の不可逆化 | 180日 | [IND-030](../config/indicators.json) |
| Fable 5/Mythos 5のアクセス停止が60日以上継続する | [H-ANT-002](../config/hypotheses.json) 62%「標準ツール化」の根拠が弱まる | 60日 | [IND-027](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる | 90日 | [IND-008](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下 | [H-ANT-002](../config/hypotheses.json) 62%「標準ツール化」の根拠が崩れる。medium→low移行確定 | 30日 | [IND-027](../config/indicators.json) |
| 次回COMPLETEラウンドでRed交差検証後にH-ANT-002 medium→low移行が実施される | [H-ANT-002](../config/hypotheses.json) ラベル変更。62%は過渡期の仮の値 | 次回 | [H-ANT-002](../config/hypotheses.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性の制度化は差別化の消失ではなく次元の変化を意味し、規制捕獲戦略の側面も評価が必要 | 37% (low) | ±0%。Kano再定式化実行済み。AI企業信頼15%は二義的。CVE-8.7が継続的矛盾。並存≠因果継続 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-041](../Information/2026-06-14/collected-raw.md#INFO-041) [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) [INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 62% (medium) | -2%（64→62%・2R連続-1%）。Claude Code採用24% [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) のC蓄積継続だがDAU/日常利用者データ4R連続不在（v4.16条件到達）。medium→low移行検討起動・DEGRADED制約でラベル変更は次回COMPLETE保留。Agent SDK課金分離 [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) は围い込み強化。62%はFable 5 #1・Opus 4.8 SWE-bench #1技術リーダーシップに依存 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) [INFO-017](../Information/2026-06-10/collected-raw.md#INFO-017) | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | ±0%。棄却候補継続。Google $40B投資でインフラ二重集中更に加速 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) [INFO-003](../Information/2026-06-10/collected-raw.md#INFO-003) [INFO-043](../Information/2026-06-10/collected-raw.md#INFO-043) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) |
| [H-GOV-001](../config/hypotheses.json) | 政府が経済的手段でAnthropicの安全性姿勢に圧力をかける先例が確立された。(a)命題に特化。(b)はH-GOV-002として分離 | 54% (medium) | -2%（56→54%・2R連続-1%）。介入ツール拡大（DPA検討・8社開放・サプライチェーンリスク）はC蓄積だが、Google $40B投資・$1T評価+Jumper流入・研究者非難の三重Iが先例確立核心要件（持続性・合法性）を三重に挑戦。介入能力の拡大（C）と介入効果の不在（I）の不均衡が2R連続拡大。C=10件蓄積は健在。medium維持 | [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) [INFO-044](../Information/2026-06-17/collected-raw.md#INFO-044) [INFO-053](../Information/2026-06-17/collected-raw.md#INFO-053) [INFO-104](../Information/2026-06-17/collected-raw.md#INFO-104) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) [INFO-031](../Information/2026-06-23/collected-raw.md#INFO-031) [INFO-029](../Information/2026-06-23/collected-raw.md#INFO-029) | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) [INFO-033](../Information/2026-06-23/collected-raw.md#INFO-033) |
| [H-GOV-002](../config/hypotheses.json) | 政府のAnthropic圧力先例がAI業界全体に波及し、順応報酬構造を通じて安全性研究の戦略的価値が構造的に低下する | 21% (low) | ±0%。絶対条件（他社安全性方針定量変化データ）20R連続未達成。NSF予算削減 [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) は文脈証拠だが経時的定量データ不在。順応報酬構造の代替解釈で完全棄却回避 | [INFO-051](../Information/2026-06-17/collected-raw.md#INFO-051) | [INFO-044](../Information/2026-06-17/collected-raw.md#INFO-044) [INFO-045](../Information/2026-06-17/collected-raw.md#INFO-045) [INFO-047](../Information/2026-06-17/collected-raw.md#INFO-047)（範疇誤謬・除外済） [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 36% (low) | ±0%。「79%導入」≠「30%自動化達成」の定義ギャップ未解決 | [INFO-020](../Information/2026-06-10/collected-raw.md#INFO-020) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) | [INFO-028](../Information/2026-06-10/collected-raw.md#INFO-028) [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が変容し、「設計・評価・方向付けする能力」の価値が上昇する | 70% (medium) | ±0%。ステートメント修正実行済み。METR 43%本番破損が上限制約として継続 | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) | (METR 43%本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流と下流に集中する | 58% (medium) | +1%（57→58%）。4件の直接C蓄積（スマイル曲線再形成・AaaS/SaaS置換・代理店変容B-2 Forrester・Next Gen Agency生存）。方向性支持・速度不確定 | [INFO-024](../Information/2026-06-10/collected-raw.md#INFO-024) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) | [INFO-056](../Information/2026-05-28/collected-raw.md#INFO-056) [INFO-022](../Information/2026-05-28/collected-raw.md#INFO-022) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転継続。$10.9B年収。KPMG 276K。high/rising | 2026-06-23 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Daybreak Security・GPT-5.5-Cyber・Codex Security=防御側強化。CVE-8.7はI重み「高」。新規A-2実被害なし。high/rising | 2026-06-23 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」検証突破で elevated→high | Fable 5視覚/科学改善・Seedance 2.0 4モダリティ同時入力・Gemini Robotics-ER/Live API。量的向上継続。「真の理解」未解決。elevated/stable | 2026-06-23 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | ALE完遂<2.5%・成功率10%・Klarna $40B損失・72%/60%ガバナンス格差。7+独立ソースで期待-実態ギャップ確定的。high/rising | 2026-06-23 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | Interactions API GA・Agent Skills生態系・Antigravityクロス互換・NVIDIA OpenShell・AgentPerf。標準化臨界点通過。high/rising | 2026-06-23 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 広範なタスクでのRSI再現・外部検証で critical | Anthropic AI 80%内部コード寄与=RSI具体化・CEO3氏AGI 5-10年合意・Jumper流入・LeCun AMI Labs。RSI具体化とベンチマーク限界同時進行。high/rising | 2026-06-23 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | SpaceX Cursor $60B・Google $40B投資・xAI $20B・OpenAI Q1 $5.7B/$3.7Bバーン・Anthropic $1T。資本流入加速確定的。high/rising | 2026-06-23 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | （critical到達済み） | **critical/rising**。Operation Epic Fury複数独立再確認(96h/2,000標的)・DPA行使検討・中国AIレイオフ違法化。「設計通り≠技術的安全事故」区別の実質崩壊更に進行。条件2（A-2技術的安全事故）は未到達。判事Rita Lin判断・Gillibrand法案・DeepMind AI Control Roadmapは緩和要因 | 2026-06-23 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-23 | 全面書き直し。Google最大$40B投資報道（[INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) B-2）・Anthropic $1Tセカンダリ+Jumper移籍（[INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) B-2）・NSF予算20-30%削減を反映。[H-GOV-001](../config/hypotheses.json) 56→54%（2R連続-1%・三重I拡大）。[H-ANT-002](../config/hypotheses.json) 64→62%（DAU/日常利用者4R連続不在・medium→low移行検討起動・DEGRADED制約でラベル変更保留）。[H-CAR-003](../config/hypotheses.json) 57→58%。IND-030 critical維持（DPA検討・複数独立再確認）。全§5最終確認日更新 | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) [INFO-031](../Information/2026-06-23/collected-raw.md#INFO-031) [INFO-065](../Information/2026-06-23/collected-raw.md#INFO-065) | H-GOV-001 56→54%・H-ANT-002 64→62%・H-CAR-003 57→58% |
| 2026-06-21 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 58→56%（判事Rita Lin「違法な報復」判断 [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) A-2でI側初のA-2品質証拠）。[H-ANT-002](../config/hypotheses.json) 65→64%（Fable 5/Mythos 5アクセス停止の開発者影響）。[IND-030](../config/indicators.json) high→critical（Operation Epic Fury相転移） | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) | H-GOV-001 58→56%・H-ANT-002 65→64%・IND-030 high→critical |
| 2026-06-20 | ターゲット編集。H-CAR-002確信度69→70%・ステートメント修正（価値低下→価値変容） | [arbiter-2026-06-20](../state/arbiter-2026-06-20.md) | H-CAR-002 69→70%・ステートメント修正 |
| 2026-06-17 | H-GOV-001(a)/(b)分割実行。(a)39→55% low→medium・(b)H-GOV-002新規20% low。IND-030 critical移行条件確定 | 2026-06-17複数INFO | H-GOV-001 39→55%・H-GOV-002新規20% |
| 2026-06-15 | H-ANT-001 ±0%(37%)・Kano再定式化実行・ステートメント更新・Red修正4点採用 | 2026-06-15複数INFO | |

## 7. ブラインドスポット

- [H-GOV-001](../config/hypotheses.json) 54%（medium）はC=10件・I=3件（Rita Lin判断・Google $40B投資・$1T評価+Jumper流入）になった。C蓄積は強力だが、介入能力の拡大と介入効果の不在の不均衡が2R連続で拡大。法的帰趗が確定するまで54%は仮の均衡値である。次回COMPLETEラウンドでのRed交差検証が54%の妥当性を左右する。
- Google $40B投資（[INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) B-2）は「最大$40B」であり最終額が未確定。Google自身がGeminiを展開する中での競合大型投資の戦略的意図の判別が不完全。資本提携 vs インフラ依存の強化のいずれが主要効果か不明。
- Jumper移籍（[INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) B-2）は象徴的意義は大きいが、個人の移籍は組織研究能力の定量的評価には直結しない。DeepMindの研究体制への影響の定量評価がない。
- [H-ANT-002](../config/hypotheses.json) 62%は過渡期の仮の値。DAU/日常利用者データ4R連続不在でmedium→low移行検討が起動したが、DEGRADED制約でラベル変更が保留。次回COMPLETEラウンドのRed交差検証後に62%の妥動が決まる。
- 判事Rita Linの判断が「政府介入=違法」を意味するのか「手続き的瑕疵」を意味するのかの技術的判別が不完全。前者ならH-GOV-001の前提そのものが揺らぐ。後者なら手続きの修正で政府の介入権限自体は維持される。
- Fable 5/Mythos 5のアクセス停止が開発者エコシステム（H-ANT-002）に与える影響が定量評価できない。利用不可期間が長引けばClaude Code採用24%の成長曲線が頭打ちになる。
- [H-ANT-001](../config/hypotheses.json) はKano再定式化を実行したが、AI企業信頼15%の二義的解釈が判別力を制限する。37%の長期固定はアンカリングの制度化の徴候。
- Claude Code WAU/MAUが非公開。Agent SDK課金分離の影響の定量評価がない。
- CVE-8.7が未解決であり、安全性差別化仮説に継続的な矛盾を提示する。
- IPO S-1秘密提出は情報開示の機会だが、安全性研究への資金コミットメントがIPO自己選択バイアスか真のコミットメントかの判別が困難。
- NSF予算20-30%削減（[INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) B-2）は連邦AI安全研究支援縮小の一環だが、KIQ-GOV-002絶対条件（安全性研究予算の経時的定量データ）は20R連続未達成。NSF削減のAnthropic特定影響の判別が不完全。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) | Google最大$40B Anthropic投資報道・G7 Amodei+Hassabis米国主導AI連合要請(B-2) |
| [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) | Anthropic $1Tセカンダリ/$5B調達計画/Jumper移籍・NSF予算20-30%削減(B-2) |
| [INFO-031](../Information/2026-06-23/collected-raw.md#INFO-031) | DPA行使検討(B-2) |
| [INFO-029](../Information/2026-06-23/collected-raw.md#INFO-029) | Pentagon 8社選別契約・サプライチェーンリスク(B-2) |
| [INFO-065](../Information/2026-06-23/collected-raw.md#INFO-065) | Operation Epic Fury独立再確認(96h/2,000標的・The Hill/Yahoo/Independent)(B-2) |
| [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) | 判事Rita Lin「違法な報復」判断・Anthropic連邦禁止阻止・Fable 5/Mythos 5アクセス停止(A-2) |
| [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | 輸出管理指令全容: Amazon研究者論文→商務省指令→Moussouris批判(A-1) |
| [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) | Grok Gov Model Operation Epic Fury 96h/2,000標的(A-2) |
| [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) | DoD CDAO宣誓陳述書・Colossus 2国家安保不可欠・Gillibrand法案(A-1) |
| [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) | DeepMind AI Control Roadmap: 高度AIエージェントを「内部脅威」と扱う(A-1) |
| [Arbiter v4.17](../state/arbiter-2026-06-23.md) | H-GOV-001 56→54%・H-ANT-002 64→62%・H-CAR-003 57→58%・DEGRADED 2R連続 |
| [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) | Claude Code採用3%→24%・JetBrains 1万人調査(B-3) |
| [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) | Anthropic ARR $470億 vs OpenAI $330億逆転(C-2) |
| [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) | 全連邦政府Anthropic使用停止・SCR指定Huawei級(A-2) |
| [INFO-044](../Information/2026-06-17/collected-raw.md#INFO-044) | Pentagon Anthropic提訴(A-2) |
| [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) | Fable 5/Mythos 5 SOTA維持(A-3) |
| [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) | 政府がFable 5/Mythos 5全外国人アクセス停止(A-3) |
| [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) | CVE-8.7 CVSS 8.7 RCE脆弱性(A-3) |
