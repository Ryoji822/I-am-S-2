# Anthropic

> 最終判断更新: 2026-06-14
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが非公開。安全性が選択理由上位3要因以内かの判別がA-2品質で未確認(26R連続上限条件未達成、37%下限宣言継続・再定式化命令発令)。収益内訳(消費者/エンタープライズ/API)非公開。CVE-8.7(CVSS 8.7 RCE)が安全性差別化仮説に重大な矛盾を提示。H-GOV-001核心命題（業界全体萎縮効果）の証拠ゼロ・C7件は全てAnthropic固有。INFO-002単一証拠依存リスク（5判断+1指標がA-3アクセス停止に依存）。IPO自己選択バイアスの除外が未完了。Fable 5 30日データ保持ポリシーが安全性差別化に潜在的I。Public Record 81K調査のエンタープライズ選択理由データ解析待ち。Claude Code 90%自コードベースはAnthropic自己評価（利益相反・C蓄積から除外）
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-ANT-001](../config/hypotheses.json) は37%で±0%維持。再定式化命令が発令された（次回必須実行・Kano分析導入）。26R連続で上限条件が未達成であり、先送りが4R以上継続する構造的問題を是正するため、次回未実行の場合はArbiterが独自に仮説ステートメント修正を実行する。[H-GOV-001](../config/hypotheses.json) は40%で±0%維持。Blue Agentの+1%提案が否認され、核心命題（業界全体の萎縮効果）の証拠ゼロが確定した。政府によるFable 5/Mythos 5全アクセス停止指令（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002)、A-3品質・全外国人対象）は設立以来最高品質のC蓄積だが、Anthropic1社に限定された事象である。NSPM-11詳細分析（[INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027)）で元政府高官が「Anthropic紛争から直接生まれた」と一致確認。企業無効化権剥奪（[INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032)）とJAWBONE法（[INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029)）で政府-AI構造的対立が顕在化。もし安全性がA-2品質で選択理由第1位と確認される、またはKano分析で安全性がMust-be要件と確認される、または他社の安全性方針の定量変化が確認される場合、判断が変わる。

SCN-004は31%で首位を維持し、SCN-003（28%）との差が3%に拡大した。QHG 41R連続凍結が打破され、今後は毎R方向圧力評価に基づく修正が標準プロセスとなる。パターンUU「パラドックス」は高→中-高に引き下げられ（C-3品質混入是正・代替解釈「戦略的シナジー」未評価）、パターンTT「政府-AI構造的対立の顕在化」は中と判定された（4事象が全てAnthropic1社に集中）。[H-CAR-001](../config/hypotheses.json) は36%（±0%）。

## 1. コア判断

全体確信度は中。政府によるFable 5/Mythos 5全アクセス停止指令（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002)、A-3品質）が今週最大の構造変化である。ローンチ（6/9）から3日後（6/12）に全外国人（同盟国政府・研究者・商用顧客含む）のアクセスが無効化された。政府は「Fable 5のセーフガードをバイパスする方法」を発見したと主張するが、Anthropicは「狭い非汎用ジェイルブレイク」であり業界全体のリコール基準として不適切と反論した。この単一証拠に5判断（[H-GOV-001](../config/hypotheses.json) C・[H-ANT-001](../config/hypotheses.json) I・パターンTT・パターンUU・[IND-030](../config/indicators.json)）が依存しており、証拠の範囲と実効性の確認が分析全体の堅牢性を左右する。

[H-ANT-001](../config/hypotheses.json) は37%で±0%維持。C/I均衡（A-3品質で相殺）が継続し、限界宣言ルールが適用されている。再定式化命令がArbiterから直接発令された。内容は安全性が「魅力的差別化要因」から「当たり前品質（KanoモデルMust-be）」に移行している可能性の本格的検討である。Public Record 81K調査（[INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038)）はエンタープライズ選択理由の定量データソースとなる可能性があるが、解析結果は未確認。CVE-8.7（CVSS 8.7 RCE）が継続的に安全性差別化に矛盾を提示する。Anthropic評価額ほぼ$1T（[INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035)）は商業的成功の継続を示すが、安全性由来の成功か性能・価格の別要因かの判別が不可能な状態が継続する。

[H-GOV-001](../config/hypotheses.json) は40%で±0%維持。Blue Agentが設立以来最強のC蓄積（7件・A-3含む）を根拠に+1%を提案したが、Red Agentの指摘「核心命題（業界全体の萎縮効果）の証拠ゼロ・C7件は全てAnthropic固有」が採用された。NSPM-11詳細分析（[INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027)）で元CIA CTO・Project Maven創設者・GWU法律教授が「Anthropic紛争から直接生まれた」と一致確認した。企業無効化権剥奪（[INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032)）で展開済み軍事AIを企業が単独で無効化できなくなった。一方、JAWBONE法（[INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029)）は超党派（Cruz+Wyden）で政府のAI企業強制を禁止する法案であり、「対立の結晶化」と「対立の法的解決の進行」の双方に解釈可能である。他社（Google・OpenAI・Meta）の安全性方針の定量変化データが不在であり、波及効果の実証は次回の絶対条件として継続する。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Claude Fable 5/Mythos 5リリース。大部分ベンチマークSOTA。$10/$50 per MTok。Stripe 5,000万行1日移行。5%セッションOpus 4.8フォールバック | [H-ANT-002](../config/hypotheses.json) 確認的蓄積。フロンティアモデル性能競争の新段階。セーフガードは[H-ANT-001](../config/hypotheses.json) C側 | A-3 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) |
| 高 | 政府がFable 5/Mythos 5の全外国人アクセス停止を指令。輸出管理ディレクティブ。即時コンプライアンス | [H-GOV-001](../config/hypotheses.json) C側A-3品質。設立以来最高品質の政府圧力証拠。[IND-030](../config/indicators.json) 直接根拠。主力製品の外国人アクセス停止は構造的事件 | A-3 | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) |
| 高 | NSPM-11詳細分析。元CIA CTO・Project Maven創設者・GWU教授が「Anthropic紛争から直接生まれた」と一致確認。DoD 3000.09の90日以内更新命令 | [H-GOV-001](../config/hypotheses.json) C側B-3品質。政府-AI構造的対立の制度化。パターンTT直接根拠 | B-3 | [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) |
| 高 | 企業無効化権剥奪。展開済み軍事AIを企業が単独で無効化できない規則導入 | [H-GOV-001](../config/hypotheses.json) C側B-3品質。政府権限の拡大。安全性スタンスの制度的代償 | B-3 | [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) |
| 高 | JAWBONE法。超党派（Cruz+Wyden）で連邦政府のAI企業強制を禁止。ACLU支持 | [H-GOV-001](../config/hypotheses.json) I側B-3品質。「対立の結晶化」または「解決の進行」の双方に解釈可能 | B-3 | [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) |
| 高 | Anthropic評価額ほぼ$1兆到達。OpenAIと競争的IPO今秋 | [H-ANT-001](../config/hypotheses.json) 商業的成功の継続。IPO安全性研究資金使途の可能性。IPO自己選択バイアス除外必要 | B-3 | [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) |
| 高 | Anthropic Public Record。81,000人Claudeユーザーへのグローバル定性調査。Anthropic Interviewer使用 | [H-ANT-001](../config/hypotheses.json) エンタープライズ選択理由の定量データソースの可能性。Kano分析の基礎データ。解析結果未確認 | A-3 | [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) |
| 高 | CVE-8.7（CVSS 8.7 RCE脆弱性）がClaude Codeで発見 | [H-ANT-001](../config/hypotheses.json) I重み「高」。安全性差別化企業の主力製品におけるCVSS 8.7のRCEは重大な矛盾。[IND-013](../config/indicators.json) 根拠強化 | A-3 | [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) |
| 高 | GoogleがAnthropic $35Bチップ取引をバックストップ。Bloomberg報道 | [IND-029](../config/indicators.json) 資本投入加速のA-3品質直接証拠。[H-ANT-003](../config/hypotheses.json) 棄却候補更に強化（インフラ二重集中） | A-3 | [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) |
| 高 | NSPM-11署名。Anthropic事件の再発防止。非協力的AI企業は契約解除 | [H-GOV-001](../config/hypotheses.json) C側B-3品質。政府圧力の制度的化。Pentagon排除確認（[INFO-028](../Information/2026-06-13/collected-raw.md#INFO-028)）と整合 | B-3 | [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) |
| 高 | Anthropic S-1秘密提出（6月1日）・$965B評価額・IPO競争でOpenAI $852B上回る | [H-ANT-001](../config/hypotheses.json) 商業的成功の継続。IPO安全性研究資金使途（[INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047)）はI蓄積の可能性。IPO自己選択バイアス除外必要 | B-3 | [INFO-033](../Information/2026-06-10/collected-raw.md#INFO-033) [INFO-069](../Information/2026-06-13/collected-raw.md#INFO-069) [INFO-039](../Information/2026-06-13/collected-raw.md#INFO-039) |
| 高 | トークンコスト$30→<$1/MTok（2023年初→2026年6月） | SCN-004 コモディティ化C蓄積。囲い込み価値の侵食圧力 | A-3 | [INFO-025](../Information/2026-06-10/collected-raw.md#INFO-025) |
| 中 | Claude CodeがAnthropic公開コードの80%以上を執筆（Economist報道） | [IND-028](../config/indicators.json) RSI部分的加速の証拠。コード生成≠RSIの限定詞継続。[H-ANT-002](../config/hypotheses.json) 確認的蓄積 | A-3 | [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) |
| 中 | MicrosoftがFable 5アクセスを制限。30日データ保持ポリシーが理由 | [H-ANT-001](../config/hypotheses.json) 新I証拠。安全性差別化の矛盾（顧客企業が安全性企業のモデルを制限） | C-3 | [INFO-004](../Information/2026-06-13/collected-raw.md#INFO-004) |
| 中 | Anthropic Public Record調査。52,000米国人調査。AI失業懸念64%。政府規制支持71%。AI企業信頼15% | [H-GOV-001](../config/hypotheses.json) 文脈証拠。世論の規制支持と企業不信は政府圧力の社会的基盤 | A-3 | [INFO-002](../Information/2026-06-13/collected-raw.md#INFO-002) |
| 中 | KPMG 138カ国276K人以上がClaude利用開始。Digital GatewayにCowork/Managed Agents統合 | [H-ANT-001](../config/hypotheses.json) 確認的蓄積。安全性因果帰属は未検証（並存≠因果） | A-3 | [INFO-002](../Information/2026-06-10/collected-raw.md#INFO-002) |
| 中 | Fortune 500 79%経営者がAI agents導入済み・41%企業が管理階層削減 | [H-CAR-001](../config/hypotheses.json) C側蓄積。「79%導入」≠「30%自動化達成」の定義ギャップ | B-3 | [INFO-020](../Information/2026-06-10/collected-raw.md#INFO-020) |
| 中 | 初級テック採用25%減少・Stanford 2026 AI Indexで26歳未満SE雇用-20% | [H-CAR-002](../config/hypotheses.json) 「書く能力」価値低下の支持。QAテスター・BA需要増加は「設計評価力」価値上昇と整合 | B-3 | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 安全性がA-2品質でエンタープライズ選択理由第1位と確認される | [H-ANT-001](../config/hypotheses.json) 上限条件解除。37%下限宣言の無効化。25R連続未達成の累積ペナルティ無効化 | 180日 | [IND-008](../config/indicators.json) |
| CVE-8.7が深刻な実被害（エンタープライズ環境での悪用確認）に至る | [H-ANT-001](../config/hypotheses.json) 37%から更なる下方。安全性差別化仮説の根本的崩壊。[IND-013](../config/indicators.json) critical移行 | 90日 | [IND-013](../config/indicators.json) |
| SCR指定が恒久化し法的に確定する | [H-GOV-001](../config/hypotheses.json) C/I均衡がC優位に転換。I側A-1品質（NSA継続利用）が崩壊する場合 | 90日 | [IND-030](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる | 90日 | [IND-008](../config/indicators.json) |
| 因果チェーン第4段階（業界全体の安全性方針変化）がA-2品質で確認される | [H-GOV-001](../config/hypotheses.json) 40%均衡打破。萎縮効果が実際に波及した証拠 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下 | [H-ANT-002](../config/hypotheses.json) 64%「標準ツール化」の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |
| NSAがAnthropic利用を停止する | [H-GOV-001](../config/hypotheses.json) I側A-1品質の崩壊。C/I均衡→C優位に転換 | 90日 | [IND-030](../config/indicators.json) |
| C側A-2品質以上の新規蓄積がI側A-1を上回る | [H-GOV-001](../config/hypotheses.json) 40%均衡打破 | 60日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 37% (low) | ±0%。26R連続上限条件未達成。限界宣言ルール適用。再定式化命令発令（次回必須実行・Kano分析導入）。CVE-8.7（I重み「高」）が継続的矛盾。Fable 5アクセス停止（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002)）は安全性差別化の制度的外部制約を示す。Public Record 81K調査（[INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038)）は選択理由データの可能性。並存≠因果継続 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) [INFO-002](../Information/2026-06-10/collected-raw.md#INFO-002) [INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047) [INFO-051](../Information/2026-06-10/collected-raw.md#INFO-051) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-041](../Information/2026-06-14/collected-raw.md#INFO-041) [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% (medium) | ±0%。「Cowork≠Code」概念混同是正継続。SDK利用形態詳細（Cowork単独 vs SDK経由比率）不明。Fable 5 Dynamic Workflowsで数百並列サブエージェントはC蓄積。Claude Code 90%自コードベース（[INFO-060](../Information/2026-06-14/collected-raw.md#INFO-060)）はAnthropic自己評価のためC蓄積から除外（利益相反）。80%+（[INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073)）は継続参照 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) [INFO-017](../Information/2026-06-10/collected-raw.md#INFO-017) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | ±0%。棄却候補継続。SpaceX Colossus契約（[INFO-003](../Information/2026-06-10/collected-raw.md#INFO-003)）・Google $35Bチップバックストップ（[INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037)）でインフラ二重集中が加速 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) [INFO-003](../Information/2026-06-10/collected-raw.md#INFO-003) [INFO-043](../Information/2026-06-10/collected-raw.md#INFO-043) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 40% (low) | ±0%。Blue Agent +1%提案否認。核心命題（業界全体の萎縮効果）の証拠ゼロ・C7件は全てAnthropic固有。Fable 5アクセス停止（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) A-3）は設立以来最高品質CだがAnthropic1社限定。NSPM-11詳細分析（[INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027)）で専門家一致確認。他社波及効果の実証が絶対条件 | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) [INFO-027](../Information/2026-06-13/collected-raw.md#INFO-027) [INFO-028](../Information/2026-06-13/collected-raw.md#INFO-028) [INFO-006](../Information/2026-06-10/collected-raw.md#INFO-006) [INFO-021](../Information/2026-06-10/collected-raw.md#INFO-021) [INFO-040](../Information/2026-06-10/collected-raw.md#INFO-040) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) [INFO-030](../Information/2026-06-13/collected-raw.md#INFO-030) [INFO-034](../Information/2026-06-13/collected-raw.md#INFO-034) [INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047) [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) [INFO-025](../Information/2026-06-07/collected-raw.md#INFO-025) [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 36% (low) | ±0%。Fortune 500 79%導入・41%管理層削減（B-3）。「79%導入」≠「30%自動化達成」の定義ギャップ未解決。因果帰属多段階性（AI理由分類手法不明・自己申告ベース）は継続的制約 | [INFO-020](../Information/2026-06-10/collected-raw.md#INFO-020) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-042](../Information/2026-06-07/collected-raw.md#INFO-042) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | [INFO-028](../Information/2026-06-10/collected-raw.md#INFO-028) [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し、「設計・評価・方向付けする能力」の価値が上昇する | 69% (medium) | ±0%。METR 43%本番破損を明示的組み込み。「書く能力の定義の変化」vs「価値低下」区別導入済み。初級SE採用25%減（[INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029)）はC蓄積。69%上限（METR 43%明示的反証込み） | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) [INFO-059](../Information/2026-05-23/collected-raw.md#INFO-059) | (METR 43%本番破損) |
| [H-CAR-003](../config/hypotheses.json) | スマイルカーブの中間圧縮により、バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流と下流に集中する | 57% (medium) | ±0%。5重C蓄積継続。広告業界非中介化（[INFO-024](../Information/2026-06-10/collected-raw.md#INFO-024)）・初級職代替（[INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023)）がC蓄積追加。方向性支持・速度不確定 | [INFO-024](../Information/2026-06-10/collected-raw.md#INFO-024) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) [INFO-045](../Information/2026-05-28/collected-raw.md#INFO-045) [INFO-013](../Information/2026-05-28/collected-raw.md#INFO-013) | [INFO-056](../Information/2026-05-28/collected-raw.md#INFO-056) [INFO-022](../Information/2026-05-28/collected-raw.md#INFO-022) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転継続 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)。$10.9B年収 [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)。70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。KPMG 276K [INFO-002](../Information/2026-06-10/collected-raw.md#INFO-002)。high/rising | 2026-06-14 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | CVE-8.7 Claude Code RCE（[INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) A-3）・Fable 5アクセス停止（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) A-3・政府がセーフガードバイパス主張）・OWASP Top 10 Agents・Microsoft Fable 5制限。CVE-8.7はI重み「高」。high/rising | 2026-06-14 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」検証突破で elevated→high | Fable 5視覚/科学改善（[INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) A-3）・Seedance 2.0動画生成（[INFO-041](../Information/2026-06-10/collected-raw.md#INFO-041) A-3）。量的向上継続。「真の理解」検証未解決。elevated/stable | 2026-06-14 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | IBM 87%未展開・Gartner 17%展開済み・リハイアパターン継続・SentinelBench 46-75%完了率（[INFO-042](../Information/2026-06-10/collected-raw.md#INFO-042) C-3）・Fortune 500 79%導入（[INFO-020](../Information/2026-06-10/collected-raw.md#INFO-020) B-3）。期待-実態ギャップ確認継続。high/rising | 2026-06-14 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP RC・AAIFリフレクション・Gemini Skills OSS・OpenAI Skills Bedrock・ADK OSS（[INFO-019](../Information/2026-06-10/collected-raw.md#INFO-019) A-3）・10+ OSSフレームワーク（[INFO-013](../Information/2026-06-10/collected-raw.md#INFO-013) C-3）。標準化爆発的加速継続。high/rising | 2026-06-14 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 広範なタスクでのRSI再現・外部検証で critical | Claude Code 90%自コードベース（[INFO-060](../Information/2026-06-14/collected-raw.md#INFO-060) A-3・Anthropic自己評価のためC蓄積から除外）・Claude Code 80%+（[INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) A-3）・RSI部分的加速・GPT-5 ARC 96.3%・ARC-AGI-3 <1%。主観-客観乖離拡大継続。high/rising | 2026-06-14 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | China $295B計画・ByteDance 2000億元・Google $35Bチップ（[INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) A-3）・Anthropic ほぼ$1T評価額（[INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) B-3）・Google $85B増資。資本流入劇的加速確定的。high/rising | 2026-06-14 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Fable 5アクセス停止（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) A-3・政府がセーフガードバイパス主張）・NSPM-11詳細分析（[INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) B-3）・企業無効化権剥奪（[INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) B-3）・CVE-8.7（[INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) A-3）・RSI部分的。能力向上とリスク増大の同時進行が更に深化。high/rising | 2026-06-14 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-14 | H-ANT-001 ±0%(37%)再定式化命令発令 + H-GOV-001 ±0%(40%)核心命題証拠ゼロ確定 + Pattern UU 高→中-高(C-3品質混入是正) + Pattern TT 新出・中(4事象全てAnthropic1社集中) + Pattern WW 中維持(INFO-060 C蓄積から除外) + Fable 5アクセス停止(A-3) + NSPM-11詳細分析(B-3) + 企業無効化権剥奪(B-3) + JAWBONE法(B-3) + Anthropic ~$1T(B-3) + Public Record 81K(A-3) + Claude Code 90%(A-3・C除外) + QHG 41R凍結打破を反映 | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) [INFO-060](../Information/2026-06-14/collected-raw.md#INFO-060) | H-ANT-001 37%(±0%・再定式化命令)・H-GOV-001 40%(±0%・核心命題証拠ゼロ)・Pattern UU高→中-高・Pattern TT新出・中・Pattern WW中(維持)・Fable 5アクセス停止・NSPM-11詳細・企業無効化権剥奪・JAWBONE法・~$1T評価額・Public Record 81K・Claude Code 90%(C除外)・QHG 41R打破 |
| 2026-06-13 | H-ANT-001 -1%(38→37%)下限宣言発動 + H-GOV-001 -1%(41→40%)絶対条件 + Pattern OO中-高→中(Red採用) + Pattern RR中-高→中(Red採用) + Fable 5/Mythos 5リリース + Google $35Bチップ取引(A-3) + NSPM-11 + Microsoft Fable 5制限 + Claude Code 80%+ + IPO競争 + SCN-004首位維持(30%) + Red採用2/3(OO/RR)を反映 | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) [INFO-004](../Information/2026-06-13/collected-raw.md#INFO-004) [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) [INFO-002](../Information/2026-06-13/collected-raw.md#INFO-002) [INFO-030](../Information/2026-06-13/collected-raw.md#INFO-030) | H-ANT-001 38→37%(下限宣言)・H-GOV-001 41→40%(絶対条件)・Pattern OO中-高→中・Pattern RR中-高→中・Fable 5/Mythos 5リリース・Google $35Bチップ・NSPM-11・SCN-004 30%首位維持・Arbiter Red採用2/3 |
| 2026-06-10 | H-ANT-001 -2%(42→40%) + H-GOV-001 -2%(45→43%) + H-CAR-001 +1%(35→36%) + CVE-8.7 I重み 中→高 + Pattern GG 中→低-中 + Pattern FF 中→低-中 + Pattern HH 低-中→低 + SCN-003 -3%(32→29%) + SCN-004 +3%(27→30%) + Red採用3/7(43%)を反映 | [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) [INFO-001](../Information/2026-06-10/collected-raw.md#INFO-001) [INFO-033](../Information/2026-06-10/collected-raw.md#INFO-033) [INFO-043](../Information/2026-06-10/collected-raw.md#INFO-043) [INFO-025](../Information/2026-06-10/collected-raw.md#INFO-025) [INFO-040](../Information/2026-06-10/collected-raw.md#INFO-040) [INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047) | H-ANT-001 42→40%(low帯深化)・H-GOV-001 45→43%(low帯深化)・H-CAR-001 35→36%・CVE-8.7 I重み中→高・Pattern GG中→低-中・Pattern FF中→低-中・Pattern HH低-中→低・SCN-003 32→29%・SCN-004 27→30%(SCN-004逆転)・Arbiter Red採用43% |
| 2026-06-07 | H-GOV-001 -2%(47→45%) medium→low + H-CAR-001 +3%(32→35%) + IND-028 elevated→high(条件付) + SCN-001 +2%(15→17%) + SCN-003 -3%(35→32%) + SCN-004 +1%(26→27%) + Red採用75%を反映 | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) | H-GOV-001 47→45%(medium→low)・H-CAR-001 32→35%・IND-028 elevated→high(条件付)・SCN-001 15→17%・SCN-003 35→32%・SCN-004 26→27%・H-CAR-003新規追加・Arbiter Red採用75% |
| 2026-06-01 | H-GOV-001 -1%(48→47%)+H-CAR-002 ±0%(METR 43%明示的組み込み)+Pattern M中-高→中+Pattern N/O新規+SCN-002 -1%(25→24%)+SCN-004 +1%(25→26%)+IND-030 8→9重蓄積を反映 | [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) | H-GOV-001 48→47%・Pattern M中-高→中・SCN-002 25→24%・SCN-004 25→26%・IND-030 8→9重・Pattern N/O新規 |
| 2026-05-31 | H-GOV-001 -1%(50→48%)+H-ANT-001 -1%(44→42%)+Pattern J/G確度中-高→中+Mythos一般公開+Karpathy入社+budget overruns+Stanford雇用データ+IND-030 elevated→highを反映 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | H-GOV-001 50→48%・H-ANT-001 44→42%・Pattern J/G中-高→中・IND-030 elevated→high・H-CAR-001 31→32% |
| 2026-05-29 | H-GOV-001 -1%(51→50%) + Pattern E格下げ + Pattern F修正 + 上限条件再設計実行 + 新規Evidence 9件で全面書き直し | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) | H-GOV-001 51%→50%・$380B→$965B・Pattern E「結晶化」→「構造的二面性の継続」・Pattern F「臨界点」→「臨界点接近」・H-ANT-001上限条件再設計実行・KPMG再分類(H-ANT-002→H-ANT-001) |
| 2026-05-28 | H-GOV-001 -1%(52→51%) + Pattern B「決定的顕在化」→「構造的深化」格下げ + 新規Evidence 11件で全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | H-GOV-001 52%→51%・Pattern B「決定的顕在化」→「構造的深化」・「政府-市場ギャップ」再定義認識 |
| 2026-05-25 | H-ANT-001 low帯移行(47→46%)+条件再定義+Pattern A確度「中-高」→「中」+新規Evidence 13件で全面書き直し | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | H-ANT-001 47%→46%(low帯移行)・H-ANT-002 63%→64% |
| 2026-05-23 | $10.9B収益+KPMG 276K+Stainless買収+Pentagon因果A-2確認+控訴裁懐疑的+固定料金終了を反映して全面書き直し | [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | 「WSJ $900B+OpenAI逆転」→「$10.9B到達・初営業利益。KPMG 276K統合。Stainless買収。Pentagon因果A-2確定」 |

## 7. ブラインドスポット

- [H-ANT-001](../config/hypotheses.json) は26R連続上限条件未達成。再定式化命令が発令された（次回必須実行・Kano分析導入）。次回未実行の場合はArbiterが独自に仮説ステートメント修正を実行する。Public Record 81K調査（[INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038)）は選択理由定量データの可能性だが、解析結果は未確認。安全性が「魅力的差別化要因」から「当たり前品質（Must-be）」に移行している可能性の本格検討が必要。

- [H-GOV-001](../config/hypotheses.json) 40%の核心命題（業界全体の萎縮効果）の証拠ゼロが確定した。C7件は全てAnthropic固有の事象である。Fable 5アクセス停止（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) A-3）は設立以来最高品質のC蓄積だが、Anthropic1社に限定された事象であり、他社（Google・OpenAI・Meta）の安全性方針の定量変化データが不在である。波及効果の実証が絶対条件。NSPM-11詳細分析（[INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027)）で「Anthropic紛争から直接生まれた」と専門家一致確認されたが、制度の適用範囲が他社に及ぶかは未検証。

- Claude Code WAU/MAUが非公開であり、Codex 4M WAUと比較したClaude Codeの相対的規模が測れない。価格差（Claude Code $100-200 vs OpenCode $30-80）が不透明性を増幅する。KPMGでの利用形態詳細（Cowork単独 vs SDK経由比率）も不明で、[H-ANT-002](../config/hypotheses.json) 64%の根拠が推測ベースにとどまる。

- CVE-8.7（CVSS 8.7 RCE）が未解決であり、安全性差別化仮説に継続的な矛盾を提示する。深刻な実被害が確認された場合、[H-ANT-001](../config/hypotheses.json) は37%下限を突破して根本的崩壊の可能性がある。

- IPO S-1秘密提出は情報開示の機会であるが、安全性研究への資金コミットメント（[INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047)）がIPO自己選択バイアス（上場前IR戦略としての安全性アピール）か真のコミットメントかの判別が、S-1公開後も困難な可能性がある。CVE-8.7の発見タイミングとIPO時期の関係も未検証。

- $10.9B収益の内訳（消費者/エンタープライズ/API）が非公開。評価額$965BとPentagon除外のコスト比率、Colossus契約月額$12.5億の正確性も観測手薄。「Claude Cowork/Managed Agents」と「Claude Code/SDK」の利用形態別シェア不明。QHG再定義が40R連続未実行で、シナリオ確率が凍結状態。

- [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002)（Fable 5アクセス停止 A-3）の単一証拠に5判断（[H-GOV-001](../config/hypotheses.json) C・[H-ANT-001](../config/hypotheses.json) I・パターンTT・パターンUU・[IND-030](../config/indicators.json)）と1指標が依存している。証拠の範囲（「全外国人」の実効性）と持続性（一時的措置か恒久的か）の確認が分析全体の堅牢性を左右する。政府の主張（セーフガードバイパス）とAnthropicの反論（狭い非汎用ジェイルブレイク）の技術的検証が不在。

- [INFO-060](../Information/2026-06-14/collected-raw.md#INFO-060)（Claude Code 90%自コードベース）はAnthropic自己評価であり、利益相反のためC蓄積から除外された。[INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073)（Claude Code 80%+公開コード）と同様に、外部検証のない自己報告データがRSI議論の基礎となっている構造的弱点。

- Microsoft Fable 5アクセス制限（[INFO-004](../Information/2026-06-13/collected-raw.md#INFO-004)・30日データ保持ポリシー）は、その後の政府による全外国人アクセス停止指令（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) A-3）に尺度を一変された。企業内制限から国家権限による全面アクセス停止への拡大は、安全性差別化の制度的外部制約が想定以上に急速に進展したことを示す。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) | Fable 5/Mythos 5 SOTA維持・コスト効率(A-3) |
| [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) | 政府がFable 5/Mythos 5全外国人アクセス停止・輸出管理ディレクティブ(A-3) |
| [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) | NSPM-11詳細分析・元CIA CTO等専門家一致確認(B-3) |
| [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) | JAWBONE法・超党派で政府AI企業強制禁止(B-3) |
| [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) | 企業無効化権剥奪・展開済み軍事AI無効化不可(B-3) |
| [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) | Anthropic評価額ほぼ$1兆・競争的IPO今秋(B-3) |
| [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) | Anthropic Public Record 81K定性調査・選択理由データ(A-3) |
| [INFO-060](../Information/2026-06-14/collected-raw.md#INFO-060) | Claude Code 90%自コードベース・Anthropic自己評価(A-3・C除外) |
| [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) | Fable 5/Mythos 5リリース・SOTA・$10/$50 per MTok・Stripe移行(A-3) |
| [INFO-002](../Information/2026-06-13/collected-raw.md#INFO-002) | Anthropic Public Record 52K調査・AI失業64%・規制支持71%・企業信頼15%(A-3) |
| [INFO-004](../Information/2026-06-13/collected-raw.md#INFO-004) | Microsoft Fable 5アクセス制限・30日データ保持(C-3) |
| [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) | NSPM-11署名・非協力AI企業契約解除(B-3) |
| [INFO-027](../Information/2026-06-13/collected-raw.md#INFO-027) | Anthropicブラックリスト報復否定(B-3) |
| [INFO-028](../Information/2026-06-13/collected-raw.md#INFO-028) | Pentagon Claude排除確認・安全性ルール理由(B-3) |
| [INFO-030](../Information/2026-06-13/collected-raw.md#INFO-030) | NSA Claude Mythos例外確認(C-3) |
| [INFO-034](../Information/2026-06-13/collected-raw.md#INFO-034) | White House EO Advanced AI Innovation and Security(A-3) |
| [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) | Google $35Bチップ取引バックストップ(A-3) |
| [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038) | OpenAI IPO競争・株式市場デビュー計画(A-3) |
| [INFO-039](../Information/2026-06-13/collected-raw.md#INFO-039) | OpenAI $852B評価額(A-3) |
| [INFO-047](../Information/2026-06-13/collected-raw.md#INFO-047) | Anthropic IPO切り替えコスト分析(C-3) |
| [INFO-069](../Information/2026-06-13/collected-raw.md#INFO-069) | Anthropic $965B評価額(C-3) |
| [INFO-072](../Information/2026-06-13/collected-raw.md#INFO-072) | Anthropic vs Pentagon包括的分析(B-3) |
| [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) | Claude Code 80%+公開コード執筆(A-3) |
| [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) | CVE-8.7 Claude Code RCE(CVSS 8.7)・RSI論文(A-3) |
| [INFO-001](../Information/2026-06-10/collected-raw.md#INFO-001) | Claude Opus 4.8リリース・SWE-bench 88.6%・Dynamic Workflows(A-3) |
| [INFO-002](../Information/2026-06-10/collected-raw.md#INFO-002) | KPMG 276K Claude展開・Digital Gateway統合(A-3) |
| [INFO-003](../Information/2026-06-10/collected-raw.md#INFO-003) | SpaceX Colossus 300MW/220K GPU契約(A-3) |
| [INFO-043](../Information/2026-06-10/collected-raw.md#INFO-043) | Google $35Bチップ取引バックストップ・追加$10億投資(A-2) |
| [INFO-025](../Information/2026-06-10/collected-raw.md#INFO-025) | トークンコスト$30→<$1/MTok・エンタープライズ支出$8.4B(A-3) |
| [INFO-033](../Information/2026-06-10/collected-raw.md#INFO-033) | Anthropic S-1秘密提出・$965B評価額(B-3) |
| [INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047) | Anthropic IPO資金使途・安全性研究・コンピュート拡大(B-3) |
| [INFO-007](../Information/2026-06-10/collected-raw.md#INFO-007) | 3社準兆ドルIPO集中・SpaceX $1.75T・Anthropic $965B(C-3) |
| [INFO-006](../Information/2026-06-10/collected-raw.md#INFO-006) | Pentagon SCR指定確認・Claude排除(C-3) |
| [INFO-021](../Information/2026-06-10/collected-raw.md#INFO-021) | Pentagon AI調達再構築・連邦控訴裁SCR指定阻止否認(B-3) |
| [INFO-040](../Information/2026-06-10/collected-raw.md#INFO-040) | 権威主義政府AI安全ねじ曲げ・構造的分析(B-2) |
| [INFO-017](../Information/2026-06-10/collected-raw.md#INFO-017) | Bubblewrapサンドボックス・Claude Code Actions CI/CD(A-3) |
| [INFO-020](../Information/2026-06-10/collected-raw.md#INFO-020) | Fortune 500 79% AI agents導入・41%管理層削減(B-3) |
| [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) | 初級テック採用25%減・Stanford SE雇用-20%(B-3) |
| [INFO-051](../Information/2026-06-10/collected-raw.md#INFO-051) | Claude Enterprise vs ChatGPT Enterprise詳細比較(C-3) |
| [INFO-030](../Information/2026-06-10/collected-raw.md#INFO-030) | ARC-AGI-3 <1%・SuperARC Nature・GPT-5 ARC 96.3%(A-2) |
| [INFO-031](../Information/2026-06-10/collected-raw.md#INFO-031) | AGIタイムライン・Hassabis 2029・Amodei 2027(B-3) |
| [INFO-032](../Information/2026-06-10/collected-raw.md#INFO-032) | 269頁AIガバナンス法案・再帰的自己改善規制(C-3) |
| [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) | 初級職AI代替・キャリアラダー破壊(C-3) |
| [INFO-024](../Information/2026-06-10/collected-raw.md#INFO-024) | 広告代理店非中介化(C-3) |
| [INFO-028](../Information/2026-06-10/collected-raw.md#INFO-028) | Klarna AIブーメラン・再採用苦戦(C-3) |
| [INFO-042](../Information/2026-06-10/collected-raw.md#INFO-042) | SentinelBench完了率46-75%・500K+トークン消費(C-3) |
| [INFO-046](../Information/2026-06-10/collected-raw.md#INFO-046) | MATS/Anthropic Fellows AIアラインメント研究(C-3) |
| [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) | NSA継続利用（SCR指定後もAnthropicエンジニア継続）(A-1) |
| [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | Pentagon SCR指定(A-1) |
| [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) | 142Kテックレイオフ AI#1理由(A-1) |
| [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) | NDAAガードレール要求(A-2) |
| [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) | Anthropic AI一時停止提案(A-2) |
| [INFO-025](../Information/2026-06-07/collected-raw.md#INFO-025) | Anthropic軍事契約拒否(B-2) |
| [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) | Anthropic $65B Series H完了・$965B評価額(A-2) |
| [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) | Stainless(SDK構築)買収(C-3) |
| [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) | 裁判所が政府全体Anthropic排除に差し止め命令(B-3) |
| [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) | Illinois米国最強AI安全法可決(A-2) |
| [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) | NIST AI Safety Institute→AI Consortium改名(A-3) |
| [INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074) | 評価額急増は安全性アプローチへの信頼(C-3) |
| [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) | Mythos一般公開・Cloudflare評価(A-2) |
| [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | Stanford 22-25歳16%相対雇用減(A-2) |
| [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) | Microsoft/Uber Claude Code予算超過(B-2) |
| [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) | Anthropic Series H $65B調達・$965B評価額(A-1) |
| [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) | Claude Opus 4.8 Opusクラス強化アップグレード(A-1) |
| [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) | KPMG 276,000人Claude展開(A-1) |
| [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) | Trust Center SOC2/ISO27001/FedRAMP/HIPAA(A-1) |
| [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) | SCR指定・控訴裁Anthropic側懐疑的(A-2) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B投資検討・70%勝利(B-3) |
| [Arbiter v4.08](../state/arbiter-2026-06-14.md) | 確度評価の完全根拠 |

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
| 2026-05-12 | DPAを最も強制的な形で使用しAI安全性低下を強要。Olah・Dean声明 | [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) |
| 2026-05-13 | Claude App Store首位獲得(Pentagon圧力拒否後) | [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) |
| 2026-05-19 | Google/OpenAI兵器ルール後退。Pentagon 8社にフロンティアAI展開承認 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) |
| 2026-05-21 | 控訴裁がAnthropicのSCRブロックに懐疑的な見方を示す | [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) |
| 2026-05-29 | Pope Leo XIV回勅「Magnifica humanitas」にChris Olah声明。安全性スタンスの道義的正当性を国際的に強化 | [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) |
| 2026-05-29 | 控訴裁がSCR指定ブロック申し立てに懐疑的。Hegseth長官指定・全連邦取引禁止継続 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| 2026-06-01 | Department of War対立公式声明 | [INFO-037](../Information/2026-06-01/collected-raw.md#INFO-037) |
| 2026-06-01 | 裁判所が政府全体Anthropic排除に差し止め命令 | [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) |
| 2026-06-02 | White House EO on Advanced AI Innovation and Security | [INFO-034](../Information/2026-06-13/collected-raw.md#INFO-034) |
| 2026-06-07 | Pentagon SCR指定確認・継続（A-1品質で再確認） | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) |
| 2026-06-07 | NSAがSCR指定後もAnthropicエンジニアを継続利用（I側A-1品質） | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) |
| 2026-06-09 | NSPM-11署名。Anthropic事件の再発防止。非協力的AI企業は契約解除 | [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) |
| 2026-06-09 | Trump政権がAnthropicブラックリストへの違法報復を否定 | [INFO-027](../Information/2026-06-13/collected-raw.md#INFO-027) |
| 2026-06-09 | Pentagon Claude排除を確認。安全性ルールが理由。Pentagon直接契約に限定 | [INFO-028](../Information/2026-06-13/collected-raw.md#INFO-028) |
| 2026-06-10 | Pentagon AI調達再構築分析。SCR指定阻止否認確認 | [INFO-021](../Information/2026-06-10/collected-raw.md#INFO-021) |
| 2026-06-10 | NSPM-11 Anthropic例外。NSA Claude Mythos例外確認 | [INFO-030](../Information/2026-06-13/collected-raw.md#INFO-030) |
| 2026-06-12 | 政府がFable 5/Mythos 5の全外国人アクセス停止を指令。輸出管理ディレクティブ。即時コンプライアンス。政府は「セーフガードバイパス」を主張、Anthropicは「狭い非汎用ジェイルブレイク」と反論 | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) |
| 2026-06-13 | NSPM-11詳細分析。元CIA CTO・Project Maven創設者・GWU法律教授が「Anthropic紛争から直接生まれた」と一致確認。DoD 3000.09の90日以内更新命令 | [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) |
| 2026-06-13 | 企業無効化権剥奪。展開済み軍事AIを企業が単独で無効化できない規則導入 | [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) |
| 2026-06-13 | JAWBONE法。超党派（Cruz+Wyden）で連邦政府のAI企業強制を禁止する法案。ACLU支持 | [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) |
