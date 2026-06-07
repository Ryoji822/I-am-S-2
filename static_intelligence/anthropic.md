# Anthropic

> 最終判断更新: 2026-06-07
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが非公開。安全性が選択理由上位3要因以内かの判別がA-2品質で未確認(19R連続上限条件未達成)。収益内訳(消費者/エンタープライズ/API)非公開。エンタープライズ統合の安全性因果帰属未検証。「Claude Cowork/Managed Agents」と「Claude Code/SDK」の利用形態別シェア不明。Stainless買収のSDK統合詳細不明。H-GOV-001 C/I均衡の質的転換点が不明確(45%でI側A-1品質とC側A-1品質が同等)
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-GOV-001](../config/hypotheses.json) は45%に低下しmedium帯からlow帯に移行した。Red Agentの品質調整論理が採用され、C側A-1品質（SCR指定 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018)）とI側A-1品質（NSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019)）が同等の重みを持つC/I均衡状態と評価された。OpenAI displacementは市場の代替機能であり業界全体への萎縮効果ではない（Red指摘採用）。監視条件「政府圧力加速」は承認されたが、I側A-1品質を相殺するC側追加蓄積が必要。

[H-CAR-001](../config/hypotheses.json) は35%（+1%）、142KテックレイオフでAIが#1理由（[INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) A-1）により前回の鮮度制約が解消された。[IND-028](../config/indicators.json) は条件付high移行、RSI「定義された実験ではほぼ超人」（[INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) A-1）がhigh移行条件を充足した。[H-ANT-001](../config/hypotheses.json) は42%±0%、19R連続上限条件未達成。SCN-003は32%（-1%）、SCN-004は27%（+1%）。ArbiterはRed指摘を4件中3件（75%）採用し、保守的分析姿勢が強まった。もしC側A-2品質以上の新規蓄積がI側A-1を上回る、またはIND-028のRSI外部検証がcritical移行条件を充足する、またはH-ANT-001が20R到達でも上限条件未達成の場合、判断が変わる。

## 1. コア判断

全体確信度は中。Anthropicの商業的躍進は継続するが、成功要因の帰属、政府対立の帰結、雇用市場への影響についての確度は依然として下がる。

[H-GOV-001](../config/hypotheses.json) は45%に低下しmedium帯からlow帯に移行した。6R連続（v3.96-v4.01）での累積的低下は保守性原則に合致する。このラウンドの決定的な変化は、C側A-1品質（SCR指定 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018)）に対してI側A-1品質（NSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019)）が初めて同等の重みを持つと評価された点である。NSAがSCR指定後もAnthropicエンジニアを継続利用していることは、政府内部での分裂、あるいはSCR指定の実効性に対する強力なI側反証として機能する。OpenAI displacementは市場の代替機能（業界全体への萎縮効果ではない）とするRed指摘が採用され、これまでの「displacement＝萎縮効果」解釈が修正された。監視条件「政府圧力加速」は承認（INFO-047の30日マイルストーン2026-07-02で政府圧力加速時は-1%再開検討）されているが、I側A-1品質を相殺するC側追加蓄積が必要。NDAAガードレール要求（[INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) A-2）、Anthropic AI一時停止提案（[INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) A-2）、Anthropic軍事契約拒否（[INFO-025](../Information/2026-06-07/collected-raw.md#INFO-025) B-2）がI側蓄積として追加された。因果チェーン第4段階（業界全体の安全性方針変化）は「未確認」≠「否定」が継続する。

[H-ANT-001](../config/hypotheses.json) は42%でlow帯が継続する。19R連続で上限条件（「上位3要因以内、または安全性除外で同等代替説明なし」v3.93適用）が未達成である。新規INFOなし。企業採用の安全性因果帰属は未検証のままである。Pattern J「市場が安全性を評価する」論理的飛躍判定（v3.94 Red採用）が上限条件達成難易度を更に示唆し続けている。

[H-ANT-002](../config/hypotheses.json) は64%±0%。「Cowork≠Code」概念混同是正が継続し、SDK利用形態詳細（Cowork単独 vs SDK経由比率）が依然不明である。KPMG 276K Claude展開（[INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) A-3）、Claude Sonnet 4.6（[INFO-003](../Information/2026-06-07/collected-raw.md#INFO-003) A-3）は確認的蓄積だが、+1%にはSDK経由利用の定量確認が必要である。

[H-CAR-001](../config/hypotheses.json) は35%（+1%）。142KテックレイオフでAIが#1理由（[INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) A-1）は、前回の鮮度制約（INFO-042が18ヶ月前データ）を2026年最新A-1品質データで解消した。WEF 92M職消滅（[INFO-042](../Information/2026-06-07/collected-raw.md#INFO-042) A-2）、コーディングスキル40%陳腐化（[INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) B-2）がC蓄積として追加された。制約として因果帰属の多段階性（AI理由分類手法不明・自己申告ベース）は継続的に有効であり、+1%上限とした。

[H-CAR-002](../config/hypotheses.json) は69%±0%。METR 43%本番破損を明示的に組み込み、「書く能力の定義の変化」（手書き→AIレビュー・修正）vs「書く能力の価値低下」の区別を導入した（Red指摘採用）。69%上限はMETR 43%明示的反証込み。

[H-CAR-003](../config/hypotheses.json) は57%±0%。スマイルカーブ中間圧縮の方向性は支持されるが、速度は不確定。広告業界15%削減、WEF 78%失敗の中間工程排除Cが蓄積継続。

[IND-028](../config/indicators.json) は条件付high移行した。RSI「定義された実験ではほぼ超人」（[INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) A-1）がhigh移行条件（A-2品質でのAGI関連技術ブレークスルー報告）を上回る品質で充足した。Hassabis AGI ~2030（[INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) A-2）、米中Geneva AI安全予備合意（[INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) A-2）も支持する。条件として「定義された実験」限定条件の明記、AGI定義合意不在（[INFO-048](../Information/2026-06-07/collected-raw.md#INFO-048) B-2）の構造的問題認識、次回RSI外部検証必須が付されている。critical移行条件は広範なタスクでのRSI再現・外部検証。

SCN-003は32%（-1%）。31R固定ペナルティの統計的是正が継続し、围い込み→SCN-001シフト兆候とコモディティ化証拠のSCN-004方向への圧力が同時進行している。SCN-004は27%（+1%）。コモディティ化C蓄積（API価格下落トレンド・ベンチマーク首位交代頻発・コーディングcommodity化40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041)）が方向圧力を実行した。SCN-001は17%（+2%累積）、围い込み蓄積の次元拡大が継続する。SCN-002は24%±0%で相殺均衡。

Arbiter v4.01はRed指摘を4件中3件（75%）採用した。H-GOV-001（C/I均衡・OpenAI displacement再解釈）、H-GOO-002（品質調整後均衡）、H-BTD-002（Freemium解釈）でRedが採用され、Blue採用はH-CAR-001のみ（25%）であった。保守的分析姿勢が一段と強まっている。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | NSA継続利用（SCR指定後もAnthropicエンジニアを継続利用） | [H-GOV-001](../config/hypotheses.json) I側A-1品質。C側A-1品質（SCR指定）と同等の重み。政府内分裂の強力な証拠 | A-1 | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) |
| 高 | Pentagon SCR指定（A-1）+ 7社軍事契約（A-2）+ Pentagon AI調達改革（A-2） | [H-GOV-001](../config/hypotheses.json) C側蓄積。SCR指定はA-1品質で最も強力なC。但しNSA継続利用で相殺 | A-1/A-2 | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) [INFO-023](../Information/2026-06-07/collected-raw.md#INFO-023) |
| 高 | 142Kテックレイオフ AI#1理由 + WEF 92M職消滅 + コーディングスキル40%陳腐化 | [H-CAR-001](../config/hypotheses.json) +3%累積C蓄積（32→35%）。A-1品質で鮮度制約解消。因果帰属多段階性は継続的制約 | A-1/A-2/B-2 | [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-042](../Information/2026-06-07/collected-raw.md#INFO-042) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) |
| 高 | RSI「定義された実験ではほぼ超人」+ Hassabis AGI ~2030 + 米中Geneva AI安全予備合意 | [IND-028](../config/indicators.json) 条件付high移行の直接根拠。AGIタイムライン評価の構造的変化 | A-1/A-2 | [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) |
| 高 | NDAAガードレール要求 + Anthropic AI一時停止提案 + Anthropic軍事契約拒否 | [H-GOV-001](../config/hypotheses.json) I側蓄積。安全性スタンスの継続的一貫性。議会レベルでのガードレール議論 | A-2/B-2 | [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) [INFO-025](../Information/2026-06-07/collected-raw.md#INFO-025) |
| 高 | 権威主義政府のAI安全ねじ曲げ | [H-GOV-001](../config/hypotheses.json) C側A-2品質。政府圧力の国際的広がり | A-2 | [INFO-021](../Information/2026-06-07/collected-raw.md#INFO-021) |
| 中 | KPMG 276K Claude展開 + Claude Sonnet 4.6 + SpaceX計算能力パートナーシップ | [H-ANT-001](../config/hypotheses.json) 確認的蓄積（A-3）。商業的躍進継続。安全性因果帰属は未検証 | A-3 | [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) [INFO-003](../Information/2026-06-07/collected-raw.md#INFO-003) [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) |
| 中 | AGI定義合意不在 | [IND-028](../config/indicators.json) 条件付high移行の構造的制約。「定義された実験」限定詞の意味付け | B-2 | [INFO-048](../Information/2026-06-07/collected-raw.md#INFO-048) |
| 中 | 裁判所が政府全体Anthropic排除に差し止め命令 + Illinois最強AI安全法 + EU AI Act + CISA + NIST | [H-GOV-001](../config/hypotheses.json) 前回I側品質累積（A-2/A-3）。司法・規制による多層的歯止め。今回のC/I均衡評価の背景 | A-2/A-3 | [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-034](../Information/2026-06-01/collected-raw.md#INFO-034) [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) |
| 中 | $65B Series H完了 + Stainless買収 + $965B評価額 | [H-ANT-001](../config/hypotheses.json) 商業的成功の継続。但し安全性由来か性能由来かの判別不能 | A-2/C-3 | [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) |
| 中 | SCR指定 + 控訴裁懐疑 + CVE-2026-22561 | 政府圧力の蓄積。A-2品質確認的蓄積あり | A-1/A-2 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) |
| 中 | PwC 79%本番 vs ROI 5% vs Klarna逆戻り | [IND-026](../config/indicators.json) high維持。期待-実態ギャップのA-2品質定量確認 | A-2/B-2 | [IND-026](../config/indicators.json) |
| 中 | METR 43%本番破損 + GitHub 22-29%使用率 | [H-CAR-002](../config/hypotheses.json) 69%上限の明示的反証。「書く能力」価値低下命題に直接反する | A-3/B-3 | [H-CAR-002](../config/hypotheses.json) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| SCR指定が恒久化し法的に確定する | [H-ANT-001](../config/hypotheses.json) 「安全性差別化で優位」が政府環境では機能しないことが確定。[H-GOV-001](../config/hypotheses.json) が上方修正される | 90日 | [IND-030](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる。固定料金終了後の価格弾力性が予想以上に高い証拠 | 90日 | [IND-008](../config/indicators.json) |
| 因果チェーン第4段階（業界全体の安全性方針変化）がA-2品質で確認される | [H-GOV-001](../config/hypotheses.json) 45%均衡打破。萎縮効果が実際に波及した証拠 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下だった場合 | [H-ANT-002](../config/hypotheses.json) 64%「標準ツール化」の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |
| 安全性が新上限条件（上位3要因以内、または安全性除外で同等代替説明なし）をA-2品質で充足する | [H-ANT-001](../config/hypotheses.json) 上限条件解除の根拠。low帯からの上方修正 | 180日 | [IND-008](../config/indicators.json) |
| NSAがAnthropic利用を停止する | [H-GOV-001](../config/hypotheses.json) I側A-1品質の最も強力な証拠が崩壊。C/I均衡→C優位に転換 | 90日 | [IND-030](../config/indicators.json) |
| RSI外部検証で「定義された実験」限定が再現不能と判明 | [IND-028](../config/indicators.json) high→elevated復帰。AGIタイムライン評価の根本的再検討 | 90日 | [IND-028](../config/indicators.json) |
| C側A-2品質以上の新規蓄積がI側A-1を上回る | [H-GOV-001](../config/hypotheses.json) 45%均衡打破。low帯での更なる下方または再上方 | 60日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 42% (low) | 19R連続上限条件未達成。新規INFOなし。Pattern J論理的飛躍判定（Red採用）が上限条件達成難易度を示唆。企業12件の安全性因果帰属未検証で確証バイアス警戒 | [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% (medium) | ±0%。「Cowork≠Code」概念混同是正継続。SDK利用形態詳細（Cowork単独 vs SDK経由比率）不明。Stainless買収はSDK強化CだがC-3品質。価格差$100-200 vs $30-80が否定的で相殺 | [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | ±0%。棄却候補継続。SpaceX計算能力パートナーシップ（[INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) A-3）でインフラ二重集中が加速。マルチクラウド否定継続 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 45% (low) | C/I均衡ラウンド。Red品質調整採用。C側A-1品質（SCR指定）とI側A-1品質（NSA継続利用）が同等重み。OpenAI displacementは市場代替機能（Red指摘採用）。medium→low移行。監視条件「政府圧力加速」承認。因果チェーン第4段階「未確認」≠「否定」継続 | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) [INFO-021](../Information/2026-06-07/collected-raw.md#INFO-021) [INFO-023](../Information/2026-06-07/collected-raw.md#INFO-023) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) [INFO-025](../Information/2026-06-07/collected-raw.md#INFO-025) [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 35% (low) | +1%（累積+3%: 32→35%）。142Kテックレイオフ AI#1理由（A-1）で鮮度制約解消。WEF 92M職消滅（A-2）、コーディングスキル40%陳腐化（B-2）のC蓄積。因果帰属多段階性（AI理由分類手法不明・自己申告ベース）は継続的制約。+1%上限 | [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-042](../Information/2026-06-07/collected-raw.md#INFO-042) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026) (Klarna逆戻り・ROI 5%) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し、「設計・評価・方向付けする能力」の価値が上昇する | 69% (medium) | ±0%。METR 43%本番破損を明示的組み込み。「書く能力の定義の変化」vs「価値低下」区別導入（Red指摘採用）。GitHub 22-29%使用率（B-3）は1データポイントで-1%不十分。69%上限（METR 43%明示的反証込み） | [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) [INFO-059](../Information/2026-05-23/collected-raw.md#INFO-059) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) | (METR 43%本番破損) |
| [H-CAR-003](../config/hypotheses.json) | スマイルカーブの中間圧縮により、バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流と下流に集中する | 57% (medium) | ±0%。5重C蓄積継続。広告業界15%削減、WEF 78%失敗の中間工程排除C。EYエンタープライズAgent OSは上流集中C。方向性支持・速度不確定 | [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) [INFO-045](../Information/2026-05-28/collected-raw.md#INFO-045) [INFO-013](../Information/2026-05-28/collected-raw.md#INFO-013) | [INFO-056](../Information/2026-05-28/collected-raw.md#INFO-056) [INFO-022](../Information/2026-05-28/collected-raw.md#INFO-022) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転継続 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)。$10.9B年収 [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)。70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002)。high/rising | 2026-06-07 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | SmartLoader MCPサーバークローン攻撃・ClawHub 46.8%悪意スキル。攻撃面拡大加速継続。critical移行条件: A-1品質での大規模実被害報告。high/rising | 2026-06-07 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」検証突破で elevated→high | Seedance 2.0無料無制限（[INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054) B-2）・Grok Voice Agent API（[INFO-004](../Information/2026-06-07/collected-raw.md#INFO-004) A-3）・Claude Sonnet 4.6（[INFO-003](../Information/2026-06-07/collected-raw.md#INFO-003) A-3）。量的向上継続。「真の理解」検証未解決。elevated/stable | 2026-06-07 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | PwC 79%本番・66%生産性向上（[INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056) A-2）vs AIスティッカーショック・ROI 5%（[INFO-014](../Information/2026-06-07/collected-raw.md#INFO-014) B-2）・Klarna逆戻り（[INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026) B-2）。期待-実態ギャップのA-2品質定量確認。high/rising | 2026-06-07 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | ADK OSS（[INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) A-3）・ベンダーロックイン回避指針・マルチベンダー戦略。標準化継続加速。high/rising | 2026-06-07 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 広範なタスクでのRSI再現・外部検証で critical | RSI「定義された実験ではほぼ超人」（[INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) A-1）・Hassabis AGI ~2030（[INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) A-2）・AGI定義合意不在（[INFO-048](../Information/2026-06-07/collected-raw.md#INFO-048) B-2）・米中Geneva AI安全予備合意（[INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) A-2）。条件付high移行。主観-客観乖離は縮小方向だが依然存在。条件: 「定義された実験」限定詞明記・次回RSI外部検証必須。high/rising | 2026-06-07 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | $300B Q1投資（[INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033) B-2）・Big Tech $725B capex（[INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052) A-2）・OpenAI $852B評価額。資本流入劇的加速確定的。high/rising | 2026-06-07 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | SCR指定（[INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) A-1）・7社軍事契約（[INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) A-2）・AI一時停止提案（[INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) A-2）・RSI進捗（[INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) A-1）。能力向上とリスク増大の同時進行が新段階に到達。high/rising | 2026-06-07 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-07 | H-GOV-001 -2%(47→45%) medium→low + H-CAR-001 +3%(32→35%) + IND-028 elevated→high(条件付) + SCN-001 +2%(15→17%) + SCN-003 -3%(35→32%) + SCN-004 +1%(26→27%) + Red採用75%を反映 | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) | H-GOV-001 47→45%(medium→low)・H-CAR-001 32→35%・IND-028 elevated→high(条件付)・SCN-001 15→17%・SCN-003 35→32%・SCN-004 26→27%・H-CAR-003新規追加・Arbiter Red採用75% |
| 2026-06-01 | H-GOV-001 -1%(48→47%)+H-CAR-002 ±0%(METR 43%明示的組み込み)+Pattern M中-高→中+Pattern N/O新規+SCN-002 -1%(25→24%)+SCN-004 +1%(25→26%)+IND-030 8→9重蓄積を反映 | [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) | H-GOV-001 48→47%・Pattern M中-高→中・SCN-002 25→24%・SCN-004 25→26%・IND-030 8→9重・Pattern N/O新規 |
| 2026-05-31 | H-GOV-001 -1%(50→48%)+H-ANT-001 -1%(44→42%)+Pattern J/G確度中-高→中+Mythos一般公開+Karpathy入社+budget overruns+Stanford雇用データ+IND-030 elevated→highを反映 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | H-GOV-001 50→48%・H-ANT-001 44→42%・Pattern J/G中-高→中・IND-030 elevated→high・H-CAR-001 31→32% |
| 2026-05-29 | H-GOV-001 -1%(51→50%) + Pattern E格下げ + Pattern F修正 + 上限条件再設計実行 + 新規Evidence 9件で全面書き直し | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) | H-GOV-001 51%→50%・$380B→$965B・Pattern E「結晶化」→「構造的二面性の継続」・Pattern F「臨界点」→「臨界点接近」・H-ANT-001上限条件再設計実行・KPMG再分類(H-ANT-002→H-ANT-001) |
| 2026-05-28 | H-GOV-001 -1%(52→51%) + Pattern B「決定的顕在化」→「構造的深化」格下げ + 新規Evidence 11件で全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | H-GOV-001 52%→51%・Pattern B「決定的顕在化」→「構造的深化」・「政府-市場ギャップ」再定義認識 |
| 2026-05-25 | H-ANT-001 low帯移行(47→46%)+条件再定義+Pattern A確度「中-高」→「中」+新規Evidence 13件で全面書き直し | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | H-ANT-001 47%→46%(low帯移行)・H-ANT-002 63%→64% |
| 2026-05-23 | $10.9B収益+KPMG 276K+Stainless買収+Pentagon因果A-2確認+控訴裁懐疑的+固定料金終了を反映して全面書き直し | [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | 「WSJ $900B+OpenAI逆転」→「$10.9B到達・初営業利益。KPMG 276K統合。Stainless買収。Pentagon因果A-2確定」 |

## 7. ブラインドスポット

- [H-GOV-001](../config/hypotheses.json) 45%のC/I均衡解釈は「均衡」≠「解決」である。C側A-1品質（SCR指定）とI側A-1品質（NSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019)）が同等の重みと評価されたが、「政府圧力加速」監視条件が承認されたものの、I側A-1を相殺するC側蓄積の閾値が不明確。45%でRed品質調整論理が採用されたが、この均衡が構造的か一時的かの判別が次回の最大の分析課題。

- [H-ANT-001](../config/hypotheses.json) は19R連続上限条件未達成で、安全性因果帰属が未検証のままである。$965B評価額も70%勝利も安全性由来なのか、性能・価格・開発者体験の別要因なのかの判別が不可能。20R到達時の取り扱い（上限条件の再設計か、累積ペナルティの継続か）が未定義。Pattern J「市場が安全性を評価する」論理的飛躍判定が継続する。

- Claude Code WAU/MAUが非公開であり、Codex 4M WAUと比較したClaude Codeの相対的規模が測れない。価格差（Claude Code $100-200 vs OpenCode $30-80）がこの不透明性を増幅する。KPMGでの利用形態詳細（Cowork単独 vs SDK経由比率）も不明で、[H-ANT-002](../config/hypotheses.json) 64%の根拠が推測ベースにとどまる。

- [IND-028](../config/indicators.json) high移行は条件付である。RSI「定義された実験ではほぼ超人」（[INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) A-1）の「定義された実験」限定詞が広範なタスクへの一般化を制約する。AGI定義合意不在（[INFO-048](../Information/2026-06-07/collected-raw.md#INFO-048) B-2）の構造的問題。外部検証必須という条件の実現可能性が不透明。

- $10.9B収益の内訳（消費者/エンタープライズ/API）が非公開。評価額$965BとPentagon除外のコスト比率、Colossus契約月額$12.5億の正確性（SpaceX S-1由来でB-3）も観測手薄。「Claude Cowork/Managed Agents」と「Claude Code/SDK」の利用形態別シェアが不明であり、Stainless買収後のSDK統合詳細も未確認。QHG再定義が32R連続未実行で、シナリオ確率調整の構造的欠陥が未解決。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) | NSA継続利用（SCR指定後もAnthropicエンジニア継続）(A-1) |
| [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | Pentagon SCR指定(A-1) |
| [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) | 142Kテックレイオフ AI#1理由(A-1) |
| [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) | RSI「定義された実験ではほぼ超人」(A-1) |
| [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) | 7社軍事契約(A-2) |
| [INFO-021](../Information/2026-06-07/collected-raw.md#INFO-021) | 権威主義政府のAI安全ねじ曲げ(A-2) |
| [INFO-023](../Information/2026-06-07/collected-raw.md#INFO-023) | Pentagon AI調達改革(A-2) |
| [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) | NDAAガードレール要求(A-2) |
| [INFO-042](../Information/2026-06-07/collected-raw.md#INFO-042) | WEF 92M職消滅(A-2) |
| [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) | Hassabis AGI ~2030(A-2) |
| [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) | Anthropic AI一時停止提案(A-2) |
| [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) | 米中Geneva AI安全予備合意(A-2) |
| [INFO-025](../Information/2026-06-07/collected-raw.md#INFO-025) | Anthropic軍事契約拒否(B-2) |
| [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) | コーディングスキル40%陳腐化(B-2) |
| [INFO-048](../Information/2026-06-07/collected-raw.md#INFO-048) | AGI定義合意不在(B-2) |
| [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) | KPMG 276K Claude展開(A-3) |
| [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) | SpaceX計算能力パートナーシップ(A-3) |
| [INFO-003](../Information/2026-06-07/collected-raw.md#INFO-003) | Claude Sonnet 4.6(A-3) |
| [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) | Anthropic $65B Series H完了・$965B評価額(A-2) |
| [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) | Stainless(SDK構築)買収・5日間4社AI買収(C-3) |
| [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) | 裁判所が政府全体Anthropic排除に差し止め命令(B-3) |
| [INFO-037](../Information/2026-06-01/collected-raw.md#INFO-037) | Department of War対立公式声明(A-3) |
| [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) | CISA Agentic AI慎重導入ガイダンス(A-3) |
| [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) | Illinois米国最強AI安全法可決(A-2) |
| [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) | NIST AI Safety Institute Consortium→AI Consortium改名拡大(A-3) |
| [INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074) | 評価額急増は安全性アプローチへの信頼(C-3) |
| [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) | Mythos一般公開・Cloudflare評価(A-2) |
| [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) | Karpathy入社・Claude 78%デザイナー・Ramp 34.4%(B-2) |
| [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) | Microsoft/Uber Claude Code予算超過・Opus 4.7トークナイザー35%増(B-2) |
| [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | Stanford 22-25歳16%相対雇用減(A-2) |
| [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) | Anthropic Series H $65B調達・$965B評価額(A-1) |
| [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) | NYT: Anthropic $900B-$965B評価額・OpenAI $730B超過(A-2) |
| [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) | Claude Opus 4.8 Opusクラス強化アップグレード(A-1) |
| [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) | KPMG 276,000人Claude展開・Cowork/Managed Agents(A-1) |
| [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) | 金融向け10エージェントテンプレート・Microsoft 365 GA(A-1) |
| [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) | Trust Center SOC2/ISO27001/FedRAMP/HIPAA + CVE-2026-22561(A-1) |
| [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) | SCR指定・控訴裁Anthropic側懐疑的(A-2) |
| [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) | Claude Mythos恐喝能力・$200M DoD契約・SCR一切禁止(B-2) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B投資検討・70%勝利・80%エンタープライズ(B-3) |
| [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | DPA強制要請・Olah/Dean声明(B-2) |
| [Arbiter v4.01](../state/arbiter-2026-06-07.md) | 確度評価の完全根拠 |

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
| 2026-05-25 | PentagonがClaude Mythos Previewの評価タスクフォース設立。SCR指定継続 | [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) |
| 2026-05-25 | AI安全政策大統領令棚上げ。競争力論議が安全性論議に勝利 | [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) |
| 2026-05-28 | 下院共和党が州AI規制10年禁止条項を税法案に挿入 | [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) |
| 2026-05-28 | Claude Mythos レッドチームで人間恐喝能力発見。OpenAIがAnthropic拒否数時間後にPentagon契約獲得 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) |
| 2026-05-29 | Pope Leo XIV回勅「Magnifica humanitas」にChris Olah声明。安全性スタンスの道義的正当性を国際的に強化 | [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) |
| 2026-05-29 | 控訴裁がSCR指定ブロック申し立てに懐疑的。Hegseth長官指定・全連邦取引禁止継続 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| 2026-05-29 | Dell $9.7B・Palantir $10B・Microsoft $9.69B Pentagon契約。Anthropicは除外継続 | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) |
| 2026-05-31 | Mythos一般公開決定。Project Glasswing限定→全顧客へ。Cloudflare評価で拒否/許可不整合 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) |
| 2026-06-01 | Department of War対立公式声明 | [INFO-037](../Information/2026-06-01/collected-raw.md#INFO-037) |
| 2026-06-01 | 裁判所が政府全体Anthropic排除に差し止め命令 | [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) |
| 2026-06-01 | CISA Agentic AI慎重導入ガイダンス | [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) |
| 2026-06-01 | Illinois米国最強AI安全法可決 | [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) |
| 2026-06-01 | NIST AI Safety Institute Consortium→AI Consortium改名拡大 | [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) |
| 2026-06-07 | Pentagon SCR指定確認・継続（A-1品質で再確認） | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) |
| 2026-06-07 | NSAがSCR指定後もAnthropicエンジニアを継続利用（I側A-1品質） | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) |
| 2026-06-07 | 7社軍事AI契約締結確認・Anthropic除外継続 | [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) |
| 2026-06-07 | 権威主義政府のAI安全ねじ曲げ（国際的広がり） | [INFO-021](../Information/2026-06-07/collected-raw.md#INFO-021) |
| 2026-06-07 | Pentagon AI調達改革 | [INFO-023](../Information/2026-06-07/collected-raw.md#INFO-023) |
| 2026-06-07 | NDAAガードレール要求（議会レベルでのAI安全規制議論） | [INFO-024](../Information/2026-06-07/collected-raw.md#INFO-024) |
| 2026-06-07 | Anthropic軍事契約拒否（原則的立場の継続） | [INFO-025](../Information/2026-06-07/collected-raw.md#INFO-025) |
| 2026-06-07 | Anthropic AI一時停止提案 | [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) |
| 2026-06-07 | 米中Geneva AI安全予備合意 | [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) |
