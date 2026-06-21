# Anthropic

> 最終判断更新: 2026-06-21
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが非公開。安全性が選択理由上位3要因以内かの判別がA-2品質で未確認(30R連続上限条件未達成・Kano再定式化実行済み)。収益内訳(消費者/エンタープライズ/API)非公開。CVE-8.7(CVSS 8.7 RCE)が安全性差別化仮説に継続的矛盾。H-GOV-001(a)/(b)分割実行済み。(a)Anthropic固有政府介入はC=10件・I=0件で56% medium（58→56%・判事Rita Lin「違法な報復」判断で-2%）。(b)業界全体萎縮効果はH-GOV-002として分離（21% low）。Red範疇誤謬是正採用済み。IPO自己選択バイアスの除外が未完了。Claude Code 90%自コードベースはAnthropic自己評価（利益相反・C蓄積から除外）。AI企業信頼15%の二義的解釈がKano分析の判別力を制限。輸出管理指令(INFO-054 A-1)の原因となったAmazon研究者論文の技術的妥当性について専門家間で意見分裂（Moussouris「輸出管理をtriggeredすべきでない」vs 商務省指令）
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-GOV-001](../config/hypotheses.json) は58%から56%に-2%低下した。連邦判事Rita LinがAnthropic連邦使用禁止を「違法な報復」と判断し法院令で阻止したことが決定的要因だ [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046)（A-2）。政府の介入措置が司法によって違法と判断されたことは、政府圧力の持続性と不可逆性に対する初のA-2品質の否定的証拠である。C=10件の蓄積は健在だが、I=0からI=1（司法による違法認定）への質的変化が起きた。[H-ANT-002](../config/hypotheses.json) は65%から64%に-1%低下した。

[IND-030](../config/indicators.json) がhighからcriticalに移行した。Operation Epic FuryでGrok Gov Modelが96時間以内に2,000標的に2,000発を展開したことがA-2品質で文書化され [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044)、ミナブ小学校攻撃で168人 [INFO-043](../Information/2026-06-21/collected-raw.md#INFO-043)、全体で600〜1,400人以上の民間人が死亡した [INFO-049](../Information/2026-06-21/collected-raw.md#INFO-049)。軍事AIが個別実験から構造的実践に相転移した。Anthropic排除とGrok採用は同一プロセスの両面であり、この文脈でAnthropic連邦禁止も再位置付けられる。ただし判事Rita Linの判断とGillibrand法案 [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) は、制度化された歯止めとして出現しており、criticalレベル内の緩和要因と記録する。

## 1. コア判断

全体確信度は中。本ラウンドの最大の分析的変化は [H-GOV-001](../config/hypotheses.json) の58→56%（-2%）である。

連邦判事Rita LinがTrump政権によるAnthropic連邦使用禁止を「違法な報復（unlawful retaliation）」と判断し、法院令で阻止した [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046)（A-2）。TechCrunchは禁止が「AI脱獄とは無関係」で報復的または反応的と指摘した。Anthropicは newest AIモデルをオフラインにし、法的措置で保護を求めた。この判事の判断は、政府介入の持続性に対する初のA-2品質の否定的証拠である。(a)命題のC=10件の蓄積は変わらないが、「政府介入が確立された先例」の持続性が司法によって直接挑戦された。-2%はこの質的変化を反映する。法的帰趗は未確定（上訴可能性）だが、連邦裁判所レベルでの「違法」認定は、55-58%帯の確度を支える「不可逆性」の前提を弱体化させる。

輸出管理指令の全容も判明した [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054)（A-1）。商務省がAnthropicに外国人（従業員含む）のFable 5/Mythos 5アクセスを禁止する指令を送った。原因はAmazonのセキュリティ研究者によるガードレール回避論文だった。セキュリティ専門家Katie Moussourisは「回避はコードレビューとコード修正の差に過ぎず、輸出管理をtriggeredすべきでない」と批判し、数十人の専門家が撤回を要求した。この内部批判は、政府介入が技術的妥当性を欠く可能性を示すI方向の補強データだ。Amazon CEO Andy Jassyが事前にAnthropicモデルへの懸念を政府に提起した可能性は [INFO-104](../Information/2026-06-17/collected-raw.md#INFO-104)（B-2）の因果チェーン起点を補強する。

[IND-030](../config/indicators.json) がhighからcriticalに移行した。三つの根拠がある。第一に、Operation Epic FuryでGrok Gov Modelが96時間以内に2,000標的に2,000発を展開した [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044)（A-2）。軍事AIが個別実験から構造的実践に相転移した初の事象だ。第二に、ミナブ小学校攻撃で168人（児童・教師）が死亡し [INFO-043](../Information/2026-06-21/collected-raw.md#INFO-043)、Operation Epic Fury全体で600〜1,400人以上の民間人が死亡した [INFO-049](../Information/2026-06-21/collected-raw.md#INFO-049)。第三に、DeepMindが「AI Control Roadmap」で高度AIエージェントを「内部脅威」と扱い [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048)、Sen. GillibrandがLLM人間監視なし武力行使禁止法案を提出した [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053)。立法府と最先端開発者自身が最高警戒レベルで認識している。

ただし三つの制約がある。第一に、判事Rita Lin「違法な報復」判断 [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) とGillibrand法案 [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) は制度化された歯止めであり、criticalレベル内の緩和要因だ。第二に、条件2（A-2品質技術的安全事故報告）は未到達で、政府リスク認定（A-1/A-2）と技術的安全事故は区別される。第三に、KIQ-MIL-001（Grok AIの標的選定関与度）は未回答で、ミナブ攻撃とAI標的特定の因果関係は確定していない。

[H-ANT-002](../config/hypotheses.json) は65%から64%に-1%低下した。決定的な新規I証拠が出たわけではない。Claude Code採用24% [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) のC蓄積は継続する。Agent SDK課金分離 [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) の围い込み圧力も記録済み。ただしAnthropicがFable 5/Mythos 5をオフラインにした事実 [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) は、開発者エコシステムの成長曲線に不確実性を導入する。モデルが利用不可になれば、開発者は代替を探す。-1%はこの利用不可期間の影響を保守的に反映する。[H-ANT-001](../config/hypotheses.json) は37%で±0%維持。Kano再定式化後の上限条件未達成が継続する。[H-GOV-002](../config/hypotheses.json) は21%で±0%維持。業界全体萎縮効果の定量証拠は不在のまま。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 連邦判事Rita Lin: Anthropic連邦禁止を「違法な報復」と判断・法院令で阻止 | [H-GOV-001](../config/hypotheses.json) I側A-2品質。政府介入の持続性に対する初のA-2否定的証拠。C=10件蓄積は健在だがI=0→1の質的変化 | A-2 | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) |
| 高 | 商務省がFable 5/Mythos 5の全外国人アクセス禁止（輸出管理指令）。原因はAmazon研究者のガードレール回避論文 | [H-GOV-001](../config/hypotheses.json) C側A-1品質。政府介入の具体的手法。Moussouris「輸出管理をtriggeredすべきでない」は技術的妥当性への内部批判 | A-1 | [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) |
| 高 | Grok Gov Model Operation Epic Fury 96h/2,000標的/2,000発（A-2）。Anthropic排除と同時にGrokが軍事投入 | [IND-030](../config/indicators.json) critical移行の核心。順応報酬構造の最強証拠: Anthropic排除↔Grok軍事投入の二重 displacement | A-2 | [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) |
| 高 | ミナブ小学校攻撃168人死亡（児童・教師）・Operation Epic Fury全体600-1,400+民間人死亡 | [IND-030](../config/indicators.json) 民間被害のB-2品質証拠。AI標的特定との因果関係は未確定（KIQ-MIL-001未回答） | B-2 | [INFO-043](../Information/2026-06-21/collected-raw.md#INFO-043) [INFO-049](../Information/2026-06-21/collected-raw.md#INFO-049) |
| 高 | DoD CDAO宣誓陳述書: Grok Gov Modelは「他のフロンティアAIにない独自機能」。Gillibrand法案 | [H-GOV-001](../config/hypotheses.json) 文脈証拠。Anthropic排除とGrok独自機能の並置は順応報酬構造を強化。Gillibrand法案は緩和要因 | A-1 | [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) |
| 高 | 全連邦政府でのAnthropic使用停止命令。SCR指定（Huawei級ラベル・米国企業初） | [H-GOV-001](../config/hypotheses.json) C側A-2品質。(a)分割後の中核証拠。但しRita Lin判事が「違法な報復」と判断 | A-2 | [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) |
| 高 | PentagonがAnthropicを提訴。政府調達からの排除を法的に強制 | [H-GOV-001](../config/hypotheses.json) C側A-2品質。法的帰趗は未確定（係争中・Rita Lin判断で弱体化） | A-2 | [INFO-044](../Information/2026-06-17/collected-raw.md#INFO-044) |
| 高 | Anthropicが法廷で政府の排除命令を否認・争っている | [H-GOV-001](../config/hypotheses.json) I側。Rita Lin判事の「違法な報復」判断がAnthropicの抵抗を法的に裏付け | A-2 | [INFO-053](../Information/2026-06-17/collected-raw.md#INFO-053) |
| 高 | Pentagon 8社選別契約（Anthropic除外）。OpenAI・Google・Microsoftが正式契約獲得 | [H-GOV-001](../config/hypotheses.json) C側。順応報酬構造の制度化。他社は軍事利用禁止条項を削除し受益 | B-3 | [INFO-046](../Information/2026-06-17/collected-raw.md#INFO-046) |
| 高 | Amazon CEOが政府介入前にAnthropicモデルへの懸念を提起。Amazon研究が政府介入の引き金 | [H-GOV-001](../config/hypotheses.json) C側。政府介入の民間起点。商務省指令の原因もAmazon研究者論文（INFO-054で補強） | B-2 | [INFO-104](../Information/2026-06-17/collected-raw.md#INFO-104) |
| 高 | Anthropic「Policy on the AI Exponential」。政府のブロック・リコール権限を提唱 | [H-ANT-001](../config/hypotheses.json) 規制捕獲戦略代替解釈の評価対象。Mythos Preview全OS脆弱性発見は技術的実力の裏付け | A-3 | [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) |
| 高 | Claude Fable 5/Mythos 5リリース。大部分ベンチマークSOTA。$10/$50 per MTok。Stripe 5000万行1日移行 | [H-ANT-002](../config/hypotheses.json) 確認的蓄積。但しFable 5/Mythos 5は現在アクセス停止中（INFO-046/054） | A-3 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) |
| 高 | Claude Code採用3%→24%（米国）。JetBrains 1万人調査 | [H-ANT-002](../config/hypotheses.json) C蓄積。開発者エコシステムでのAnthropic追い上げの第三者定量証拠 | B-3 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) |
| 高 | CVE-8.7（CVSS 8.7 RCE脆弱性）がClaude Codeで発見 | [H-ANT-001](../config/hypotheses.json) I重み「高」。安全性差別化企業の主力製品におけるCVSS 8.7のRCEは重大な矛盾 | A-3 | [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) |
| 高 | トークンコスト$30→<$1/MTok（2023年初→2026年6月） | SCN-004 コモディティ化C蓄積。囲い込み価値の侵食圧力 | A-3 | [INFO-025](../Information/2026-06-10/collected-raw.md#INFO-025) |
| 中 | Anthropic S-1秘密提出。$965B評価額。IPO競争でOpenAI $852B上回る | [H-ANT-001](../config/hypotheses.json) 商業的成功の継続。IPO安全性研究資金使途の可能性 | B-3 | [INFO-033](../Information/2026-06-10/collected-raw.md#INFO-033) |
| 中 | Agent SDK課金分離。6月15日からプログラマティック使用を別課金 | [H-ANT-002](../config/hypotheses.json) 围い込み強化シグナル。SDK利用の経済的摩擦増大 | C-3 | [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) |
| 中 | 初級テック採用25%減少・Stanford 2026 AI Indexで26歳未満SE雇用-20% | [H-CAR-002](../config/hypotheses.json) 「書く能力」価値変容の支持。QAテスター・BA需要増加は「設計評価力」価値上昇と整合 | B-3 | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 判事Rita Linの法院令が上訴裁判所で覆る | [H-GOV-001](../config/hypotheses.json) のI側A-2証拠が弱体化。56%から再上昇 | 180日 | [IND-030](../config/indicators.json) |
| 安全性がA-2品質でエンタープライズ選択理由第1位と確認される | [H-ANT-001](../config/hypotheses.json) 上限条件解除。37%下限宣言の無効化 | 180日 | [IND-008](../config/indicators.json) |
| 規制産業と非規制産業でのClaude採用率に定量差が確認される | [H-ANT-001](../config/hypotheses.json) Kano移行の定量検証 | 180日 | [IND-008](../config/indicators.json) |
| CVE-8.7が深刻な実被害（エンタープライズ環境での悪用確認）に至る | [H-ANT-001](../config/hypotheses.json) 37%から更なる下方。[IND-013](../config/indicators.json) critical移行 | 90日 | [IND-013](../config/indicators.json) |
| SCR指定が恒久化し上訴裁判所も合憲と判断する | [H-GOV-001](../config/hypotheses.json) 56%から再上昇。政府介入の不可逆化 | 180日 | [IND-030](../config/indicators.json) |
| Fable 5/Mythos 5のアクセス停止が60日以上継続する | [H-ANT-002](../config/hypotheses.json) 64%の「標準ツール化」根拠が弱まる。開発者の代替移行リスク | 60日 | [IND-027](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる | 90日 | [IND-008](../config/indicators.json) |
| 順応企業（OpenAI/Google/Microsoft）の安全性ポリシー定量変化がA-2品質で確認される | [H-GOV-002](../config/hypotheses.json) 21%からの上昇。業界全体萎縮効果の発現 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下 | [H-ANT-002](../config/hypotheses.json) 64%「標準ツール化」の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性の制度化は差別化の消失ではなく次元の変化を意味し、規制捕獲戦略の側面も評価が必要 | 37% (low) | ±0%。Kano再定式化実行済み。AI企業信頼15%は二義的。CVE-8.7が継続的矛盾。並存≠因果継続 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-041](../Information/2026-06-14/collected-raw.md#INFO-041) [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) [INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% (medium) | -1%（65→64%）。Claude Code採用24% [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) のC蓄積継続。Fable 5/Mythos 5のアクセス停止 [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) が開発者エコシステムの成長に不確実性を導入。Agent SDK課金分離 [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) は围い込み強化 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) [INFO-017](../Information/2026-06-10/collected-raw.md#INFO-017) | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | ±0%。棄却候補継続。Google $35Bチップバックストップでインフラ二重集中加速 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) [INFO-003](../Information/2026-06-10/collected-raw.md#INFO-003) [INFO-043](../Information/2026-06-10/collected-raw.md#INFO-043) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) |
| [H-GOV-001](../config/hypotheses.json) | 政府が経済的手段でAnthropicの安全性姿勢に圧力をかける先例が確立された。(a)命題に特化。(b)はH-GOV-002として分離 | 56% (medium) | -2%（58→56%）。判事Rita Lin「違法な報復」判断 [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) A-2がI側初のA-2品質証拠。政府介入の持続性に対する初のA-2否定的証拠。C=10件蓄積は健在（連邦停止・Pentagon提訴・法廷否認・Amazon起点・輸出管理 A-1 等）。I=0→1の質的変化。56%はC蓄積強さ反映＋司法逆圧＋上訴可能性織込み | [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) [INFO-044](../Information/2026-06-17/collected-raw.md#INFO-044) [INFO-053](../Information/2026-06-17/collected-raw.md#INFO-053) [INFO-104](../Information/2026-06-17/collected-raw.md#INFO-104) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-053](../Information/2026-06-17/collected-raw.md#INFO-053)（法廷係争中・確定判決ではない） |
| [H-GOV-002](../config/hypotheses.json) | 政府のAnthropic圧力先例がAI業界全体に波及し、順応報酬構造を通じて安全性研究の戦略的価値が構造的に低下する | 21% (low) | ±0%。絶対条件（他社安全性方針定量変化データ）17R連続未達成。順応報酬構造の代替解釈で完全棄却回避だが定量的証拠不在 | [INFO-051](../Information/2026-06-17/collected-raw.md#INFO-051) | [INFO-044](../Information/2026-06-17/collected-raw.md#INFO-044) [INFO-045](../Information/2026-06-17/collected-raw.md#INFO-045) [INFO-047](../Information/2026-06-17/collected-raw.md#INFO-047)（範疇誤謬・除外済） [INFO-048](../Information/2026-06-17/collected-raw.md#INFO-048)（範疇誤謬・除外済） |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 36% (low) | ±0%。「79%導入」≠「30%自動化達成」の定義ギャップ未解決 | [INFO-020](../Information/2026-06-10/collected-raw.md#INFO-020) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) | [INFO-028](../Information/2026-06-10/collected-raw.md#INFO-028) [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が変容し、「設計・評価・方向付けする能力」の価値が上昇する | 70% (medium) | ±0%。ステートメント修正実行済み。METR 43%本番破損が上限制約として継続 | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) | (METR 43%本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流と下流に集中する | 57% (medium) | ±0%。5重C蓄積継続。方向性支持・速度不確定 | [INFO-024](../Information/2026-06-10/collected-raw.md#INFO-024) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) | [INFO-056](../Information/2026-05-28/collected-raw.md#INFO-056) [INFO-022](../Information/2026-05-28/collected-raw.md#INFO-022) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転継続。$10.9B年収。KPMG 276K。high/rising | 2026-06-21 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | 72%導入/31%セキュア・750:1セキュリティ投資比・政府jailbreak発見。CVE-8.7はI重み「高」。high/rising | 2026-06-21 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」検証突破で elevated→high | Fable 5視覚/科学改善・Gemini Omni動画生成・Seedance 2.0動画生成。量的向上継続。「真の理解」未解決。elevated/stable | 2026-06-21 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | IBM 87%未展開・Gartner 2027年40%降格予測・Klarna AI Boomerang・72%/31%ギャップ。期待-実態ギャップ構造的。high/rising | 2026-06-21 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | Interactions API/Managed Agents API・Skills/Codexカタログ拡大・Coze Agent World・Mastercard Agent Pay。標準化と围い込み同時加速。high/rising | 2026-06-21 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 広範なタスクでのRSI再現・外部検証で critical | ARC-AGI-3 <1%・Amodei 2027/Hassabis 2029-30・RSI研究所（利益相反除外）・LeCun LLM dead end。RSI具体化と客観ベンチ限界同時進行。high/rising | 2026-06-21 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | China $295B計画・Q1 $130B・ByteDance 2000億元・Q1 $242B VC・全VCの80%。資本流入加速確定的。high/rising | 2026-06-21 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | （critical到達済み） | **critical/rising**。Operation Epic Fury 96h/2,000標的で軍事AI相転移。ミナブ168人死亡・全体600-1,400+民間人死亡。判事Rita Lin「違法な報復」・Gillibrand法案・DeepMind AI Control Roadmapで司法・立法・開発者が最高警戒認識。条件2（A-2技術的安全事故）は未到達 | 2026-06-21 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-21 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 58→56%（判事Rita Lin「違法な報復」判断 [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) A-2でI側初のA-2品質証拠）。[H-ANT-002](../config/hypotheses.json) 65→64%（Fable 5/Mythos 5アクセス停止の開発者影響）。[IND-030](../config/indicators.json) high→critical（Operation Epic Fury相転移）。輸出管理指令全容（[INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) A-1）・Grok Gov Model A-2（[INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044)）を反映 | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) | H-GOV-001 58→56%・H-ANT-002 65→64%・IND-030 high→critical |
| 2026-06-20 | ターゲット編集。H-CAR-002確信度69→70%・ステートメント修正（価値低下→価値変容） | [arbiter-2026-06-20](../state/arbiter-2026-06-20.md) | H-CAR-002 69→70%・ステートメント修正 |
| 2026-06-17 | H-GOV-001(a)/(b)分割実行。(a)39→55% low→medium・(b)H-GOV-002新規20% low。IND-030 critical移行条件確定 | 2026-06-17複数INFO | H-GOV-001 39→55%・H-GOV-002新規20% |
| 2026-06-15 | H-ANT-001 ±0%(37%)・Kano再定式化実行・ステートメント更新・Red修正4点採用 + Policy on AI Exponential + Mythos Preview脆弱性 + Pentagon 2/3ワークロード移行 + カナダPM警告 + Public Record 52K + Agent SDK課金分離 + RSI研究所を反映 | 2026-06-15複数INFO | |
| 2026-06-14 | H-ANT-001 ±0%(37%)再定式化命令発令 + H-GOV-001 ±0%(40%)核心命題証拠ゼロ確定 + Fable 5アクセス停止(A-3) + NSPM-11詳細分析(B-3) + 企業無効化権剥奪(B-3) + Anthropic ~$1T(B-3)を反映 | 2026-06-14複数INFO | |

## 7. ブラインドスポット

- [H-GOV-001](../config/hypotheses.json) 56%（medium）はC=10件・I=1件（Rita Lin判断）になった。C蓄積は強力だが、Rita Lin判事の「違法な報復」判断が上訴される場合、確度は上下両方向に変動する。法的帰趗が確定するまで56%は仮の均衡値である。
- 判事Rita Linの判断が「政府介入=違法」を意味するのか「手続き的瑕疵」を意味するのかの技術的判別が不完全。前者ならH-GOV-001の前提そのものが揺らぐ。後者なら手続きの修正で政府の介入権限自体は維持される。
- 輸出管理指令（INFO-054 A-1）の技術的妥当性について専門家間で意見が分裂している。Moussouris「コードレビューとコード修正の差に過ぎない」vs 商務省「国家安全保障上の懸念」。この技術的論争の帰結が政府介入の正統性に直接影響する。
- Fable 5/Mythos 5のアクセス停止が開発者エコシステム（H-ANT-002）に与える影響が定量評価できない。利用不可期間が長引けば、Claude Code採用24%の成長曲線が頭打ちになる。
- [H-ANT-001](../config/hypotheses.json) はKano再定式化を実行したが、AI企業信頼15%の二義的解釈が判別力を制限する。37%の長期固定はアンカリングの制度化の徴候。
- Claude Code WAU/MAUが非公開。Agent SDK課金分離の影響の定量評価がない。
- CVE-8.7が未解決であり、安全性差別化仮説に継続的な矛盾を提示する。
- IPO S-1秘密提出は情報開示の機会だが、安全性研究への資金コミットメントがIPO自己選択バイアスか真のコミットメントかの判別が困難。
- [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002)（輸出管理指令）の単一証拠に複数判断が依存している。指令の範囲（「全外国人」の実効性）と持続性の確認が分析の堅牢性を左右する。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) | 判事Rita Lin「違法な報復」判断・Anthropic連邦禁止阻止・Fable 5/Mythos 5アクセス停止(A-2) |
| [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | 輸出管理指令全容: Amazon研究者論文→商務省指令→Moussouris批判・専門家撤回要求(A-1) |
| [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) | Grok Gov Model Operation Epic Fury 96h/2,000標的(A-2) |
| [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) | DoD CDAO宣誓陳述書・Colossus 2国家安保不可欠・Gillibrand法案(A-1) |
| [INFO-043](../Information/2026-06-21/collected-raw.md#INFO-043) | ミナブ小学校攻撃168人死亡(B-2) |
| [INFO-049](../Information/2026-06-21/collected-raw.md#INFO-049) | Operation Epic Fury全体600-1,400+民間人死亡(B-2) |
| [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) | DeepMind AI Control Roadmap: 高度AIエージェントを「内部脅威」と扱う(A-1) |
| [Arbiter v4.15](../state/arbiter-2026-06-21.md) | H-GOV-001 58→56%・H-ANT-002 65→64%・IND-030 critical移行 |
| [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) | Claude Code採用3%→24%・JetBrains 1万人調査(B-3) |
| [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) | Anthropic ARR $470億 vs OpenAI $330億逆転(C-2) |
| [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) | 全連邦政府Anthropic使用停止・SCR指定Huawei級(A-2) |
| [INFO-044](../Information/2026-06-17/collected-raw.md#INFO-044) | Pentagon Anthropic提訴(A-2) |
| [INFO-053](../Information/2026-06-17/collected-raw.md#INFO-053) | Anthropic法廷否認・係争中(A-2) |
| [INFO-104](../Information/2026-06-17/collected-raw.md#INFO-104) | Amazon CEO政府介入前Anthropic懸念(B-2) |
| [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) | Fable 5/Mythos 5 SOTA維持(A-3) |
| [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) | 政府がFable 5/Mythos 5全外国人アクセス停止(A-3) |
| [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) | NSPM-11詳細分析・専門家一致確認(B-3) |
| [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) | CVE-8.7 CVSS 8.7 RCE脆弱性(A-3) |
