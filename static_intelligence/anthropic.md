# Anthropic

> 最終判断更新: 2026-06-15
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが非公開。安全性が選択理由上位3要因以内かの判別がA-2品質で未確認(27R連続上限条件未達成、37%下限宣言継続・Kano再定式化実行済み)。収益内訳(消費者/エンタープライズ/API)非公開。CVE-8.7(CVSS 8.7 RCE)が安全性差別化仮説に重大な矛盾を提示。H-GOV-001核心命題（業界全体萎縮効果）の証拠ゼロ・C蓄積は全てAnthropic固有・仮説分割次回議題化。INFO-002単一証拠依存リスク（5判断+1指標がA-3アクセス停止に依存）。IPO自己選択バイアスの除外が未完了。Fable 5 30日データ保持ポリシーが安全性差別化に潜在的I。Claude Code 90%自コードベースはAnthropic自己評価（利益相反・C蓄積から除外）。AI企業信頼15%(INFO-003)の二義的解釈（Must-be移行 vs 差別化機会未開拓）がKano分析の判別力を制限
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-ANT-001](../config/hypotheses.json) は37%で±0%維持。Arbiter v4.08命令のKano再定式化を実行し、仮説ステートメントを「差別化の消失」から「差別化次元の変化」に更新した。安全性がKanoモデルの「魅力的品質」から「当たり前品質」への移行過程にある可能性を特定したが、Red Agentの指摘に基づき4点の修正を適用した: (1) [INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003) AI企業信頼15%の二重カウント解消と代替解釈の明記、(2) 循環論法の削除、(3) [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047)/[INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) の規制捕獲戦略代替解釈の評価、(4) 中期予測の検証不可能性の明記。確度±0%は再定式化後も短期的Cと中期的Iが均衡することから妥当だが、37%の4R連続固定はアンカリングの制度化の徴候である。[H-GOV-001](../config/hypotheses.json) は39%(-1%)。Arbiter v4.08絶対条件（他社安全性方針の定量変化データ）が未達成のため-1%を再開した。核心命題（業界全体の萎縮効果）の証拠ゼロが13R連続で継続しており、Red Agent推奨の仮説分割（Anthropic固有政府介入 vs 業界全体萎縮効果）を次回議題化した。後者の証拠が更に3R不在の場合、棄却手続きへの移行を推奨する。もし安全性がA-2品質でエンタープライズ選択理由第1位と確認される、または規制産業と非規制産業でのClaude採用率に定量差が確認される、または他社の安全性方針の定量変化が確認される場合、判断が変わる。

パターンVV「安全性制度化」は確度中を維持しつつ、Red修正「差別化の消失」から「差別化次元の変化」を採用した。SOC 2・HIPAA・ISO27001がMust-beであるにもかかわらずセキュリティ企業が差別化して競争している類例通り、規制は差別化を消失させず次元を変える。[H-CAR-001](../config/hypotheses.json) は36%（±0%）。

## 1. コア判断

全体確信度は中。Kano再定式化の実行が本ラウンドの最大の分析的変化である。Arbiter v4.08が命じた再定式化（先送り4R+是正）を完了し、安全性が「魅力的差別化要因」から「当たり前品質（Must-be）」に移行している可能性をKano分析フレームで特定した。但し、Red Agentが指摘した分析の重大な偏向を修正条件として受理した。

第1の修正は[INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003)の二重カウント解消である。AI企業信頼15%を「一元的品質の低下（Must-be移行の証拠）」と「差別化機会の未開拓（C側の証拠）」の両方に配置することは証拠量のインフレを生む。この15%は二義的であり、どちらの解釈も成立する。両解釈を明記し、いずれにも確度を傾けない。

第2の修正は循環論法の削除である。再定式化の目的は確度の適切化であり、現状維持の正当化ではない。「37%の合理性が証明された」という論理構造を排除した。

第3の修正は[INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047)/[INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054)の規制捕獲戦略代替解釈である。Anthropicが「Policy on the AI Exponential」で政府のブロック権限を提唱することは、安全性差別化の放棄ではなく、規制の設計者としてのポジション確保と解釈できる。Microsoft Windows標準化やGoogle PCI-DSS準拠の類例通り、規制の設計に参加する企業は新しい差別化次元（コンプライアンス実装完成度・制度的影響力）を獲得する。Mythos Previewが全主要OS/ブラウザの高severity脆弱性を発見した事実（[INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) A-3）は、この「制度的影響力」が既に技術的実力に基づいていることを示す。

第4の修正は中期予測の検証不可能性の明記である。「中期（2027〜）」の差別化次元変化を現在の証拠で評価することは方法論的に不適切であり、短期の証拠のみで確度を評価する。

[H-GOV-001](../config/hypotheses.json) は39%(-1%)。Arbiter v4.08絶対条件（他社安全性方針の定量変化データ）が未達成のため、-1%を再開した。NSPM-11の構造的メカニズム存在を理由に前回は-1%を見送ったが、「再開」の第1ラウンドとして適用する。核心命題（業界全体の萎縮効果）の証拠ゼロが13R連続で継続する。C蓄積は全てAnthropic固有の事象（SCR指定・DPA脅迫・アクセス停止・ワークロード移行）に限定される。Red Agent推奨の仮説分割を採用し、次回議題化する: (a)「Anthropic固有の政府介入」はC蓄積豊富、(b)「AI業界全体への萎縮効果」は証拠ゼロ。(b)の証拠が更に3R不在の場合、棄却手続きへの移行を推奨する。カナダのCarney首相が米国AI制限は「過度な依存の危険性」を示すと警告した（[INFO-046](../Information/2026-06-15/collected-raw.md#INFO-046) B-2）が、これは同盟国の主権的AIインフラ必要性の認識であり、業界全体の安全性方針変更とは別次元の現象である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Anthropic「Policy on the AI Exponential」。政府のブロック・リコール権限を提唱。適用閾値10^25 FLOPs/AI収入$500M超 | [H-ANT-001](../config/hypotheses.json) 規制捕獲戦略代替解釈の評価対象。差別化の放棄ではなく規制設計者ポジション確保の可能性。Mythos Preview全OS/ブラウザ脆弱性発見は技術的実力の裏付け | A-3 | [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) |
| 高 | Anthropic Public Record 52K調査。AI企業信頼15%（全機関中最低）。政府規制支持71%（超党派的） | [H-ANT-001](../config/hypotheses.json) Kano分析の基礎データ。信頼15%の二義的解釈: (a)Must-be移行の証拠、(b)差別化機会未開拓の証拠。両解釈を明記し確度を傾けない | A-3 | [INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003) |
| 高 | Claude Fable 5/Mythos 5リリース。大部分ベンチマークSOTA。$10/$50 per MTok。Stripe 5000万行1日移行 | [H-ANT-002](../config/hypotheses.json) 確認的蓄積。フロンティアモデル性能競争の新段階。セーフガードは[H-ANT-001](../config/hypotheses.json) C側 | A-3 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) |
| 高 | 政府がFable 5/Mythos 5の全外国人アクセス停止を指令。輸出管理ディレクティブ。即時コンプライアンス | [H-GOV-001](../config/hypotheses.json) C側A-3品質（Anthropic固有）。[IND-030](../config/indicators.json) 直接根拠。主力製品の外国人アクセス停止は構造的事象だが他社波及なし | A-3 | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) |
| 高 | NSPM-11詳細分析。元CIA CTO・Project Maven創設者・GWU教授が「Anthropic紛争から直接生まれた」と一致確認 | [H-GOV-001](../config/hypotheses.json) C側B-3品質（Anthropic固有）。政府-AI構造的対立の制度化 | B-3 | [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) |
| 高 | Pentagon/Anthropic対立タイムライン。ワークロード2/3移行完了。OpenAI・Google・Microsoftが正式契約獲得 | [H-GOV-001](../config/hypotheses.json) C蓄積（Anthropic固有）。業界全体萎縮効果の証拠ではない。他社は軍事利用禁止条項を削除し受益 | C-3 | [INFO-053](../Information/2026-06-15/collected-raw.md#INFO-053) |
| 高 | カナダCarney首相が米国AI制限は「過度な依存の危険性」を示すと警告 | [H-GOV-001](../config/hypotheses.json) 文脈証拠。同盟国の主権的AIインフラ必要性の認識。業界全体安全性方針変更とは別次元 | B-2 | [INFO-046](../Information/2026-06-15/collected-raw.md#INFO-046) |
| 高 | Anthropic評価額ほぼ$1兆到達。IPO投資家のFable 5停止事件懸念 | [H-ANT-001](../config/hypotheses.json) 商業的成功の継続。安全性由来か否かの判別不可。IPO安全性研究資金使途の可能性 | B-3 | [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) [INFO-009](../Information/2026-06-15/collected-raw.md#INFO-009) |
| 高 | CVE-8.7（CVSS 8.7 RCE脆弱性）がClaude Codeで発見 | [H-ANT-001](../config/hypotheses.json) I重み「高」。安全性差別化企業の主力製品におけるCVSS 8.7のRCEは重大な矛盾。[IND-013](../config/indicators.json) 根拠強化 | A-3 | [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) |
| 高 | Anthropic S-1秘密提出。$965B評価額。IPO競争でOpenAI $852B上回る | [H-ANT-001](../config/hypotheses.json) 商業的成功の継続。IPO安全性研究資金使途はI蓄積の可能性。IPO自己選択バイアス除外必要 | B-3 | [INFO-033](../Information/2026-06-10/collected-raw.md#INFO-033) [INFO-069](../Information/2026-06-13/collected-raw.md#INFO-069) |
| 高 | Agent SDK課金分離。6月15日からプログラマティック使用を別課金。コミュニティ混乱 | [H-ANT-002](../config/hypotheses.json) 围い込み強化シグナル。SDK利用の経済的摩擦増大。Fable 5は6月23日以降サブスクリプション除外 | C-3 | [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) |
| 高 | GoogleがAnthropic $35Bチップ取引をバックストップ | [IND-029](../config/indicators.json) 資本投入加速のA-3品質直接証拠。[H-ANT-003](../config/hypotheses.json) 棄却候補更に強化（インフラ二重集中） | A-3 | [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) |
| 高 | NSPM-11署名。Anthropic事件の再発防止。非協力的AI企業は契約解除 | [H-GOV-001](../config/hypotheses.json) C側B-3品質（Anthropic固有）。政府圧力の制度化 | B-3 | [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) |
| 高 | トークンコスト$30→<$1/MTok（2023年初→2026年6月） | SCN-004 コモディティ化C蓄積。囲い込み価値の侵食圧力 | A-3 | [INFO-025](../Information/2026-06-10/collected-raw.md#INFO-025) |
| 中 | Anthropic RSI研究所。Claude自コードベース80-90%貢献報告（第三者検証不在） | [IND-028](../config/indicators.json) RSI部分的加速の証拠。利益相反のためC蓄積から除外。[H-ANT-002](../config/hypotheses.json) 確認的蓄積 | A-3 | [INFO-057](../Information/2026-06-15/collected-raw.md#INFO-057) [INFO-040](../Information/2026-06-15/collected-raw.md#INFO-040) |
| 中 | MicrosoftがFable 5アクセスを制限。30日データ保持ポリシーが理由 | [H-ANT-001](../config/hypotheses.json) 新I証拠。安全性差別化の矛盾（顧客企業が安全性企業のモデルを制限） | C-3 | [INFO-004](../Information/2026-06-13/collected-raw.md#INFO-004) |
| 中 | Anthropic Public Record 81K定性調査（Claude Interviewer使用） | [H-ANT-001](../config/hypotheses.json) エンタープライズ選択理由データの可能性。解析結果未確認。Kano分析の基礎データ候補 | A-3 | [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) |
| 中 | KPMG 138カ国276K人以上がClaude利用開始。Digital GatewayにCowork/Managed Agents統合 | [H-ANT-001](../config/hypotheses.json) 確認的蓄積。安全性因果帰属は未検証（並存≠因果） | A-3 | [INFO-002](../Information/2026-06-10/collected-raw.md#INFO-002) |
| 中 | 初級テック採用25%減少・Stanford 2026 AI Indexで26歳未満SE雇用-20% | [H-CAR-002](../config/hypotheses.json) 「書く能力」価値低下の支持。QAテスター・BA需要増加は「設計評価力」価値上昇と整合 | B-3 | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 安全性がA-2品質でエンタープライズ選択理由第1位と確認される | [H-ANT-001](../config/hypotheses.json) 上限条件解除。37%下限宣言の無効化。Kano再定式化後の新上限条件達成検討 | 180日 | [IND-008](../config/indicators.json) |
| 規制産業と非規制産業でのClaude採用率に定量差が確認される | [H-ANT-001](../config/hypotheses.json) Kano移行の定量検証。差があれば差別化次元変化仮説の実証 | 180日 | [IND-008](../config/indicators.json) |
| CVE-8.7が深刻な実被害（エンタープライズ環境での悪用確認）に至る | [H-ANT-001](../config/hypotheses.json) 37%から更なる下方。安全性差別化仮説の根本的崩壊。[IND-013](../config/indicators.json) critical移行 | 90日 | [IND-013](../config/indicators.json) |
| SCR指定が恒久化し法的に確定する | [H-GOV-001](../config/hypotheses.json) C/I均衡がC優位に転換。I側A-1品質（NSA継続利用）が崩壊する場合 | 90日 | [IND-030](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる | 90日 | [IND-008](../config/indicators.json) |
| 因果チェーン第4段階（業界全体の安全性方針変化）がA-2品質で確認される | [H-GOV-001](../config/hypotheses.json) 39%均衡打破。萎縮効果が実際に波及した証拠。仮説分割後の(b)命題成立 | 180日 | [IND-030](../config/indicators.json) |
| H-GOV-001(b)「業界全体萎縮効果」の証拠が更に3R不在 | 棄却手続きへの移行。仮説分割の実行。(a)のみ残存 | 次回+3R | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下 | [H-ANT-002](../config/hypotheses.json) 64%「標準ツール化」の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |
| NSAがAnthropic利用を停止する | [H-GOV-001](../config/hypotheses.json) I側A-1品質の崩壊。C/I均衡からC優位に転換 | 90日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性の制度化は差別化の消失ではなく次元の変化（製品機能からコンプライアンス実装完成度・制度的影響力）を意味し、規制捕獲戦略の側面も評価が必要 | 37% (low) | ±0%。Kano再定式化実行済み（Arbiter v4.08命令完了）。Red修正4点採用。37%の4R連続固定はアンカリング留意。AI企業信頼15%（[INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003)）は二義的（Must-be移行 vs 差別化機会未開拓）。Policy on AI Exponential（[INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047)）は規制設計者ポジション確保の可能性。CVE-8.7が継続的矛盾。並存≠因果継続 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) [INFO-002](../Information/2026-06-10/collected-raw.md#INFO-002) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-041](../Information/2026-06-14/collected-raw.md#INFO-041) [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) [INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003) [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% (medium) | ±0%。「Cowork≠Code」概念混同是正継続。SDK利用形態詳細不明。Fable 5 Dynamic Workflowsで数百並列サブエージェントはC蓄積。Agent SDK課金分離（[INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010)）は围い込み強化シグナル。Claude Code 90%自コードベース（利益相反・C除外） | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) [INFO-017](../Information/2026-06-10/collected-raw.md#INFO-017) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | ±0%。棄却候補継続。SpaceX Colossus契約・Google $35Bチップバックストップでインフラ二重集中が加速 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) [INFO-003](../Information/2026-06-10/collected-raw.md#INFO-003) [INFO-043](../Information/2026-06-10/collected-raw.md#INFO-043) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 39% (low) | -1%（40→39%）。絶対条件（他社安全性方針定量変化データ）未達成で-1%再開。核心命題（業界全体萎縮効果）の証拠ゼロ13R連続。C蓄積は全てAnthropic固有。仮説分割次回議題化: (a)Anthropic固有政府介入（C豊富）(b)業界全体萎縮効果（証拠ゼロ）。(b)が更に3R不在で棄却手続き移行推奨 | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) [INFO-053](../Information/2026-06-15/collected-raw.md#INFO-053) [INFO-046](../Information/2026-06-15/collected-raw.md#INFO-046) [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) [INFO-027](../Information/2026-06-13/collected-raw.md#INFO-027) [INFO-028](../Information/2026-06-13/collected-raw.md#INFO-028) [INFO-006](../Information/2026-06-10/collected-raw.md#INFO-006) [INFO-021](../Information/2026-06-10/collected-raw.md#INFO-021) [INFO-040](../Information/2026-06-10/collected-raw.md#INFO-040) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) [INFO-030](../Information/2026-06-13/collected-raw.md#INFO-030) [INFO-034](../Information/2026-06-13/collected-raw.md#INFO-034) [INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047) [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) [INFO-025](../Information/2026-06-07/collected-raw.md#INFO-025) [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 36% (low) | ±0%。Fortune 500 79%導入・41%管理層削減（B-3）。「79%導入」≠「30%自動化達成」の定義ギャップ未解決。因果帰属多段階性は継続的制約 | [INFO-020](../Information/2026-06-10/collected-raw.md#INFO-020) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-042](../Information/2026-06-07/collected-raw.md#INFO-042) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | [INFO-028](../Information/2026-06-10/collected-raw.md#INFO-028) [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し、「設計・評価・方向付けする能力」の価値が上昇する | 69% (medium) | ±0%。METR 43%本番破損を明示的組み込み。「書く能力の定義の変化」vs「価値低下」区別導入済み。初級SE採用25%減はC蓄積。69%上限（METR 43%明示的反証込み） | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) [INFO-059](../Information/2026-05-23/collected-raw.md#INFO-059) | (METR 43%本番破損) |
| [H-CAR-003](../config/hypotheses.json) | スマイルカーブの中間圧縮により、バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流と下流に集中する | 57% (medium) | ±0%。5重C蓄積継続。広告業界非中介化・初級職代替がC蓄積追加。方向性支持・速度不確定 | [INFO-024](../Information/2026-06-10/collected-raw.md#INFO-024) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) [INFO-045](../Information/2026-05-28/collected-raw.md#INFO-045) [INFO-013](../Information/2026-05-28/collected-raw.md#INFO-013) | [INFO-056](../Information/2026-05-28/collected-raw.md#INFO-056) [INFO-022](../Information/2026-05-28/collected-raw.md#INFO-022) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転継続 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)。$10.9B年収 [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)。70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。KPMG 276K [INFO-002](../Information/2026-06-10/collected-raw.md#INFO-002)。high/rising | 2026-06-15 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | 72%導入/31%セキュア（[INFO-013](../Information/2026-06-15/collected-raw.md#INFO-013)）・750:1セキュリティ投資比（[INFO-058](../Information/2026-06-15/collected-raw.md#INFO-058)）・政府jailbreak発見（[INFO-002](../Information/2026-06-15/collected-raw.md#INFO-002)）。CVE-8.7はI重み「高」。high/rising | 2026-06-15 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」検証突破で elevated→high | Fable 5視覚/科学改善（[INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) A-3）・Gemini Omni動画生成（[INFO-006](../Information/2026-06-15/collected-raw.md#INFO-006) A-3）・Seedance 2.0動画生成（[INFO-030](../Information/2026-06-15/collected-raw.md#INFO-030) C-3）。量的向上継続。「真の理解」検証未解決。elevated/stable | 2026-06-15 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | IBM 87%未展開（[INFO-018](../Information/2026-06-15/collected-raw.md#INFO-018)）・Gartner 2027年40%降格予測（[INFO-035](../Information/2026-06-15/collected-raw.md#INFO-035)）・Klarna AI Boomerang（[INFO-031](../Information/2026-06-15/collected-raw.md#INFO-031)）・72%/31%ギャップ（[INFO-013](../Information/2026-06-15/collected-raw.md#INFO-013)）。期待-実態ギャップの構造的パターン化。high/rising | 2026-06-15 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | Interactions API/Managed Agents API（[INFO-014](../Information/2026-06-15/collected-raw.md#INFO-014) A-3）・Skills/Codexカタログ拡大（[INFO-044](../Information/2026-06-15/collected-raw.md#INFO-044) C-3）・Coze Agent World（[INFO-012](../Information/2026-06-15/collected-raw.md#INFO-012) C-3）・Mastercard Agent Pay（[INFO-015](../Information/2026-06-15/collected-raw.md#INFO-015)）。標準化と囲い込みの同時加速継続。high/rising | 2026-06-15 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 広範なタスクでのRSI再現・外部検証で critical | ARC-AGI-3 <1% vs 人間100%（[INFO-022](../Information/2026-06-15/collected-raw.md#INFO-022)）・Amodei 2027/Hassabis 2029-30（[INFO-032](../Information/2026-06-15/collected-raw.md#INFO-032)）・RSI研究所（[INFO-040](../Information/2026-06-15/collected-raw.md#INFO-040)/[INFO-057](../Information/2026-06-15/collected-raw.md#INFO-057)・利益相反証拠除外）・LeCun LLM dead end（[INFO-039](../Information/2026-06-15/collected-raw.md#INFO-039)）。RSI具体化と客観的ベンチマーク限界の同時進行。high/rising | 2026-06-15 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | China $295B計画（[INFO-017](../Information/2026-06-15/collected-raw.md#INFO-017)）・Q1 $130Bブロック/遅延（[INFO-041](../Information/2026-06-15/collected-raw.md#INFO-041)）・ByteDance 2000億元（[INFO-029](../Information/2026-06-15/collected-raw.md#INFO-029)）・Q1 $242B VC・全VCの80%（[INFO-026](../Information/2026-06-15/collected-raw.md#INFO-026)）。資本流入加速確定的。high/rising | 2026-06-15 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | アクセス停止+IPO懸念（[INFO-002](../Information/2026-06-15/collected-raw.md#INFO-002)/[INFO-009](../Information/2026-06-15/collected-raw.md#INFO-009) A-3）・Mythos Preview全OS/ブラウザ脆弱性発見（[INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) A-3）・WH EO+GAAIA（[INFO-016](../Information/2026-06-15/collected-raw.md#INFO-016)/[INFO-052](../Information/2026-06-15/collected-raw.md#INFO-052)/[INFO-056](../Information/2026-06-15/collected-raw.md#INFO-056)）・DPA脅迫（[INFO-028](../Information/2026-06-15/collected-raw.md#INFO-028)）。能力-リスク二面性の深化。critical移行検討4R連続。high/rising | 2026-06-15 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-15 | H-ANT-001 ±0%(37%)・Kano再定式化実行・ステートメント更新（差別化消失→差別化次元変化）・Red修正4点採用 + H-GOV-001 -1%(40→39%)・絶対条件未達成・仮説分割次回議題化 + パターンVV表現修正（差別化消失→差別化次元変化） + Policy on AI Exponential（INFO-047 A-3） + Mythos Preview脆弱性発見（INFO-054 A-3） + Pentagon 2/3ワークロード移行（INFO-053 C-3） + カナダPM警告（INFO-046 B-2） + Public Record 52K（INFO-003 A-3・二義的解釈） + Agent SDK課金分離（INFO-010 C-3） + RSI研究所（INFO-057 A-3・利益相反除外）を反映 | [INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003) [INFO-046](../Information/2026-06-15/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) [INFO-053](../Information/2026-06-15/collected-raw.md#INFO-053) [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) | H-ANT-001 37%(±0%・Kano再定式化実行・ステートメント更新)・H-GOV-001 40→39%(絶対条件未達成・仮説分割議題化)・パターンVV表現修正・Policy on AI Exponential・Mythos Preview脆弱性・Pentagon 2/3移行・カナダPM警告・Public Record 52K・Agent SDK課金分離・RSI研究所 |
| 2026-06-14 | H-ANT-001 ±0%(37%)再定式化命令発令 + H-GOV-001 ±0%(40%)核心命題証拠ゼロ確定 + Pattern UU 高→中-高(C-3品質混入是正) + Pattern TT 新出・中(4事象全てAnthropic1社集中) + Pattern WW 中維持(INFO-060 C蓄積から除外) + Fable 5アクセス停止(A-3) + NSPM-11詳細分析(B-3) + 企業無効化権剥奪(B-3) + JAWBONE法(B-3) + Anthropic ~$1T(B-3) + Public Record 81K(A-3) + Claude Code 90%(A-3・C除外) + QHG 41R凍結打破を反映 | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) [INFO-060](../Information/2026-06-14/collected-raw.md#INFO-060) | H-ANT-001 37%(±0%・再定式化命令)・H-GOV-001 40%(±0%・核心命題証拠ゼロ)・Pattern UU高→中-高・Pattern TT新出・中・Pattern WW中(維持)・Fable 5アクセス停止・NSPM-11詳細・企業無効化権剥奪・JAWBONE法・~$1T評価額・Public Record 81K・Claude Code 90%(C除外)・QHG 41R打破 |
| 2026-06-13 | H-ANT-001 -1%(38→37%)下限宣言発動 + H-GOV-001 -1%(41→40%)絶対条件 + Pattern OO中-高→中(Red採用) + Pattern RR中-高→中(Red採用) + Fable 5/Mythos 5リリース + Google $35Bチップ取引(A-3) + NSPM-11 + Microsoft Fable 5制限 + Claude Code 80%+ + IPO競争 + SCN-004首位維持(30%) + Red採用2/3(OO/RR)を反映 | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) [INFO-004](../Information/2026-06-13/collected-raw.md#INFO-004) [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) [INFO-002](../Information/2026-06-13/collected-raw.md#INFO-002) [INFO-030](../Information/2026-06-13/collected-raw.md#INFO-030) | H-ANT-001 38→37%(下限宣言)・H-GOV-001 41→40%(絶対条件)・Pattern OO中-高→中・Pattern RR中-高→中・Fable 5/Mythos 5リリース・Google $35Bチップ・NSPM-11・SCN-004 30%首位維持・Arbiter Red採用2/3 |
| 2026-06-10 | H-ANT-001 -2%(42→40%) + H-GOV-001 -2%(45→43%) + H-CAR-001 +1%(35→36%) + CVE-8.7 I重み 中→高 + Pattern GG 中→低-中 + Pattern FF 中→低-中 + Pattern HH 低-中→低 + SCN-003 -3%(32→29%) + SCN-004 +3%(27→30%) + Red採用3/7(43%)を反映 | [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) [INFO-001](../Information/2026-06-10/collected-raw.md#INFO-001) [INFO-033](../Information/2026-06-10/collected-raw.md#INFO-033) [INFO-043](../Information/2026-06-10/collected-raw.md#INFO-043) [INFO-025](../Information/2026-06-10/collected-raw.md#INFO-025) [INFO-040](../Information/2026-06-10/collected-raw.md#INFO-040) [INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047) | H-ANT-001 42→40%(low帯深化)・H-GOV-001 45→43%(low帯深化)・H-CAR-001 35→36%・CVE-8.7 I重み中→高・Pattern GG中→低-中・Pattern FF中→低-中・Pattern HH低-中→低・SCN-003 32→29%・SCN-004 27→30%(SCN-004逆転)・Arbiter Red採用43% |
| 2026-06-07 | H-GOV-001 -2%(47→45%) medium→low + H-CAR-001 +3%(32→35%) + IND-028 elevated→high(条件付) + SCN-001 +2%(15→17%) + SCN-003 -3%(35→32%) + SCN-004 +1%(26→27%) + Red採用75%を反映 | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) | H-GOV-001 47→45%(medium→low)・H-CAR-001 32→35%・IND-028 elevated→high(条件付)・SCN-001 15→17%・SCN-003 35→32%・SCN-004 26→27%・H-CAR-003新規追加・Arbiter Red採用75% |
| 2026-06-01 | H-GOV-001 -1%(48→47%)+H-CAR-002 ±0%(METR 43%明示的組み込み)+Pattern M中-高→中+Pattern N/O新規+SCN-002 -1%(25→24%)+SCN-004 +1%(25→26%)+IND-030 8→9重蓄積を反映 | [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) | H-GOV-001 48→47%・Pattern M中-高→中・SCN-002 25→24%・SCN-004 25→26%・IND-030 8→9重・Pattern N/O新規 |
| 2026-05-31 | H-GOV-001 -1%(50→48%)+H-ANT-001 -1%(44→42%)+Pattern J/G確度中-高→中+Mythos一般公開+Karpathy入社+budget overruns+Stanford雇用データ+IND-030 elevated→highを反映 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | H-GOV-001 50→48%・H-ANT-001 44→42%・Pattern J/G中-高→中・IND-030 elevated→high・H-CAR-001 31→32% |
| 2026-05-29 | H-GOV-001 -1%(51→50%) + Pattern E格下げ + Pattern F修正 + 上限条件再設計実行 + 新規Evidence 9件で全面書き直し | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) | H-GOV-001 51%→50%・$380B→$965B・Pattern E「結晶化」→「構造的二面性の継続」・Pattern F「臨界点」→「臨界点接近」・H-ANT-001上限条件再設計実行・KPMG再分類(H-ANT-002→H-ANT-001) |
| 2026-05-28 | H-GOV-001 -1%(52→51%) + Pattern B「決定的顕在化」→「構造的深化」格下げ + 新規Evidence 11件で全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | H-GOV-001 52%→51%・Pattern B「決定的顕在化」→「構造的深化」・「政府-市場ギャップ」再定義認識 |
| 2026-05-25 | H-ANT-001 low帯移行(47→46%)+条件再定義+Pattern A確度「中-高」→「中」+新規Evidence 13件で全面書き直し | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | H-ANT-001 47%→46%(low帯移行)・H-ANT-002 63%→64% |

## 7. ブラインドスポット

- [H-ANT-001](../config/hypotheses.json) はKano再定式化を実行した。安全性が「魅力的品質」から「当たり前品質」への移行過程にある可能性を特定したが、Kano分析フレーム自体の循環性リスクを認識する。AI企業信頼15%（[INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003)）の解釈は二義的であり、「差別化機会の未開拓」とも「Must-be移行」とも読める。この判別不能性がKano分析の診断的識別力を根本的に制限する。37%の4R連続固定はアンカリングの制度化の徴候であり、次回以降は質的変化（A-2品質の新規C/I出現等）がない限り±0%を維持しつつ分析の質を向上させることを優先する。Public Record 81K調査は選択理由定量データの可能性だが、解析結果は未確認。規制産業と非規制産業でのClaude採用率比較がKano移行の定量検証に必要。

- [H-GOV-001](../config/hypotheses.json) 39%の核心命題（業界全体の萎縮効果）の証拠ゼロが13R連続で継続する。C蓄積は全てAnthropic固有の事象である。Fable 5アクセス停止（[INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) A-3）は設立以来最高品質のC蓄積だが、Anthropic1社に限定される。Pentagon/Anthropic対立タイムライン（[INFO-053](../Information/2026-06-15/collected-raw.md#INFO-053)）でワークロード2/3移行が確認されたが、他社（OpenAI・Google・Microsoft）は軍事利用禁止条項を削除して受益しており、萎縮効果とは逆方向である。仮説分割（Anthropic固有 vs 業界全体）を次回議題化し、後者の証拠が更に3R不在で棄却手続きへの移行を推奨する。

- Claude Code WAU/MAUが非公開であり、Codex 4M WAUと比較したClaude Codeの相対的規模が測れない。Agent SDK課金分離（[INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) C-3）が開発者エコシステムに与える影響の定量評価がない。価格差（Claude Code $100-200 vs OpenCode $30-80）が不透明性を増幅する。

- CVE-8.7（CVSS 8.7 RCE）が未解決であり、安全性差別化仮説に継続的な矛盾を提示する。深刻な実被害が確認された場合、[H-ANT-001](../config/hypotheses.json) は37%下限を突破して根本的崩壊の可能性がある。

- IPO S-1秘密提出は情報開示の機会であるが、安全性研究への資金コミットメントがIPO自己選択バイアス（上場前IR戦略としての安全性アピール）か真のコミットメントかの判別が、S-1公開後も困難な可能性がある。

- $10.9B収益の内訳（消費者/エンタープライズ/API）が非公開。評価額$965BとPentagon排除のコスト比率の正確性も観測手薄。「Claude Cowork/Managed Agents」と「Claude Code/SDK」の利用形態別シェア不明。

- [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002)（Fable 5アクセス停止 A-3）の単一証拠に5判断（[H-GOV-001](../config/hypotheses.json) C・[H-ANT-001](../config/hypotheses.json) I・パターンTT・パターンUU・[IND-030](../config/indicators.json)）と1指標が依存している。証拠の範囲（「全外国人」の実効性）と持続性（一時的措置か恒久的か）の確認が分析全体の堅牢性を左右する。政府の主張（セーフガードバイパス）とAnthropicの反論（狭い非汎用ジェイルブレイク）の技術的検証が不在。

- Anthropicの「Policy on the AI Exponential」（[INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047)/[INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054)）が規制捕獲戦略として機能するか、安全性原則の純粋な表明かの判別が困難。Mythos Previewの全主要OS/ブラウザ脆弱性発見は技術的実力の裏付けだが、それが規制設計者ポジションにどう転化するかは未検証。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-003](../Information/2026-06-15/collected-raw.md#INFO-003) | Anthropic Public Record 52K調査・AI企業信頼15%・規制支持71%(A-3・二義的解釈) |
| [INFO-009](../Information/2026-06-15/collected-raw.md#INFO-009) | Fortune Fable 5アクセス停止詳細・IPO投資家懸念(B-3) |
| [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) | Agent SDK課金分離・コミュニティ混乱・围い込み強化(C-3) |
| [INFO-046](../Information/2026-06-15/collected-raw.md#INFO-046) | カナダCarney首相・米国AI過度依存危険性警告(B-2) |
| [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) | Policy on AI Exponential・政府ブロック権限提唱・規制捕獲戦略代替解釈(A-3) |
| [INFO-053](../Information/2026-06-15/collected-raw.md#INFO-053) | Pentagon/Anthropic対立タイムライン・ワークロード2/3移行完了(C-3) |
| [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) | Advanced AI Framework詳細・Mythos Preview全OS脆弱性発見(A-3) |
| [INFO-057](../Information/2026-06-15/collected-raw.md#INFO-057) | Anthropic RSI研究所・Claude自コード80-90%(A-3・利益相反) |
| [INFO-013](../Information/2026-06-15/collected-raw.md#INFO-013) | AI Agent Security 72%導入/31%セキュア・750:1投資比(C-3) |
| [INFO-058](../Information/2026-06-15/collected-raw.md#INFO-058) | Drata AI Agent Governance・750:1セキュリティ投資比(A-3) |
| [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) | Fable 5/Mythos 5 SOTA維持・コスト効率(A-3) |
| [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) | 政府がFable 5/Mythos 5全外国人アクセス停止(A-3) |
| [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) | NSPM-11詳細分析・専門家一致確認(B-3) |
| [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) | JAWBONE法・超党派で政府AI企業強制禁止(B-3) |
| [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) | 企業無効化権剥奪・展開済み軍事AI無効化不可(B-3) |
| [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) | Anthropic評価額ほぼ$1兆・競争的IPO今秋(B-3) |
| [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) | Anthropic Public Record 81K定性調査・選択理由データ(A-3) |
| [INFO-060](../Information/2026-06-14/collected-raw.md#INFO-060) | Claude Code 90%自コードベース・Anthropic自己評価(A-3・C除外) |
| [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) | Fable 5/Mythos 5リリース・SOTA・$10/$50 per MTok(A-3) |
| [INFO-002](../Information/2026-06-13/collected-raw.md#INFO-002) | Anthropic Public Record 52K調査・AI失業64%・規制支持71%・企業信頼15%(A-3) |
| [INFO-004](../Information/2026-06-13/collected-raw.md#INFO-004) | Microsoft Fable 5アクセス制限・30日データ保持(C-3) |
| [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) | NSPM-11署名・非協力AI企業契約解除(B-3) |
| [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) | Google $35Bチップ取引バックストップ(A-3) |
| [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) | Claude Code 80%+公開コード執筆(A-3) |
| [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) | CVE-8.7 Claude Code RCE(CVSS 8.7)・RSI論文(A-3) |
| [INFO-001](../Information/2026-06-10/collected-raw.md#INFO-001) | Claude Opus 4.8リリース・SWE-bench 88.6%・Dynamic Workflows(A-3) |
| [INFO-002](../Information/2026-06-10/collected-raw.md#INFO-002) | KPMG 276K Claude展開・Digital Gateway統合(A-3) |
| [INFO-033](../Information/2026-06-10/collected-raw.md#INFO-033) | Anthropic S-1秘密提出・$965B評価額(B-3) |
| [INFO-047](../Information/2026-06-10/collected-raw.md#INFO-047) | Anthropic IPO資金使途・安全性研究・コンピュート拡大(B-3) |
| [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) | NSA継続利用（SCR指定後もAnthropicエンジニア継続）(A-1) |
| [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | Pentagon SCR指定(A-1) |
| [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) | Anthropic $65B Series H完了・$965B評価額(A-2) |
| [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) | Illinois米国最強AI安全法可決(A-2) |
| [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) | Anthropic Series H $65B調達・$965B評価額(A-1) |
| [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) | SCR指定・控訴裁Anthropic側懐疑的(A-2) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B投資検討・70%勝利(B-3) |
| [Arbiter v4.09](../state/arbiter-2026-06-15.md) | 確度評価の完全根拠 |

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
| 2026-05-29 | Pope Leo XIV回勅「Magnifica humanitas」にChris Olah声明 | [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) |
| 2026-05-29 | 控訴裁がSCR指定ブロック申し立てに懐疑的 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| 2026-06-01 | Department of War対立公式声明 | [INFO-037](../Information/2026-06-01/collected-raw.md#INFO-037) |
| 2026-06-01 | 裁判所が政府全体Anthropic排除に差し止め命令 | [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) |
| 2026-06-02 | White House EO on Advanced AI Innovation and Security | [INFO-034](../Information/2026-06-13/collected-raw.md#INFO-034) |
| 2026-06-07 | Pentagon SCR指定確認・継続（A-1品質で再確認） | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) |
| 2026-06-07 | NSAがSCR指定後もAnthropicエンジニアを継続利用（I側A-1品質） | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) |
| 2026-06-09 | NSPM-11署名。Anthropic事件の再発防止。非協力的AI企業は契約解除 | [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) |
| 2026-06-09 | Trump政権がAnthropicブラックリストへの違法報復を否定 | [INFO-027](../Information/2026-06-13/collected-raw.md#INFO-027) |
| 2026-06-09 | Pentagon Claude排除を確認。安全性ルールが理由 | [INFO-028](../Information/2026-06-13/collected-raw.md#INFO-028) |
| 2026-06-12 | 政府がFable 5/Mythos 5の全外国人アクセス停止を指令。輸出管理ディレクティブ | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) |
| 2026-06-12 | Pentagon/Anthropic対立。ワークロード2/3移行完了。OpenAI・Google・Microsoftが正式契約獲得 | [INFO-053](../Information/2026-06-15/collected-raw.md#INFO-053) |
| 2026-06-14 | カナダCarney首相が米国AI制限は「過度な依存の危険性」を示すと警告 | [INFO-046](../Information/2026-06-15/collected-raw.md#INFO-046) |
