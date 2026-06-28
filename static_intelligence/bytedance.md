# ByteDance

> 最終判断更新: 2026-06-28
> 全体確信度: 中
> 情報非対称性: 中国市場の透明性低・言論統制により、観測根拠は他社比で著しく限定的。確度%は記載するが、独立した裏付けを欠く項目が多い。豆包MAUに複数ソース間で乖離（3.45億・3.3億・1.47億）があり、定義・時期・方法論の差の判別が不能。日コスト「数千万元」は火山引擎API価格からの推算であり実際の限界コストを過大評価する可能性。Seed 2.1のコーディング能力Claude Opus 4.7匹敵はByteDance自家測定であり独立ベンチマークでの検証が未完了。中国情報源の限定により独立裏付けなし
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-010](../config/indicators.json) [IND-011](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

ByteDanceがSeed 2.1シリーズを正式リリースした [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060)（A-3）。豆包2.1 Proのコーディング能力がClaude Opus 4.7に匹敵し、コストは80%低い。ARC-AGI-2リーダーボードで0.625を記録して首位に立ち、Seedance 2.5は30秒4K動画生成を実現した。Freemium + ECシナジーモデルを維持する企業という読み方は変わらないが、Seed 2.1はフロンティア性能のコモディティ化圧力を中国企業側から加速する証拠である。

もし豆包のEC転換率が急落するか、DAUが3ヶ月連続で大幅減少するか、グローバル展開が独立確認されれば、コア判断の前提が変わる。[H-BTD-001](../config/hypotheses.json) 64% medium・[H-BTD-002](../config/hypotheses.json) 43% low・[H-BTD-003](../config/hypotheses.json) 40% medium。

## 1. コア判断

Seed 2.1のリリース [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060)（A-3）は2つの意味を持つ。第一に、ByteDanceのフロンティアモデル開発能力が持続していることを示す。豆包2.1 Proのコーディング能力がClaude Opus 4.7に匹敵し、ARC-AGI-2で0.625を記録して首位に立った事実は、中国のAI技術力が量的向上の段階を過ぎ、特定領域で西側フロンティアと同等に到達した可能性を示す。ただしClaude Opus 4.7匹敵の主張はByteDance自家測定であり、独立ベンチマークでの検証が必要である。

第二に、コスト80%削減はSCN-004（コモディティ化）の経済的次元を強化する。同等性能で80%低コストのAPIが火山引擎で提供されている状況は、フロンティア性能の価格破壊が構造的に進行していることを示す。Arbiter v4.22はSCN-004を29%から30%に引き上げ、SCN-002（28%）を抜いて首位にした。ByteDanceはこの圧力の供給源の1つである。

Freemium + ECシナジーモデルの読み方は前回（2026-06-20の操作化再定義）から継続する。QuestMobileの計測で収益化価値の81.1%がEC経由 [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)（B-2）であり、無料層で集客してEC・広告・抖音シナジーでクロス収益化する構造は機能している。日収入<100万元（主にEC手数料）対 日コスト数千万元（API推算）の構造的ギャップ [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108)（B-2）は財務的持続性への問いとして残る。Seed 2.1のコスト80%削減は、この日コスト推算を下方修正する要因になりうる。但し「日コスト数千万元」がAPI価格からの推算であるため、コスト削減が実際の限界コストにどう反映されるかは外部から検証できない。

[H-BTD-001](../config/hypotheses.json) は64% mediumで±0%。Seed 2.1・Seedance 2.5・ARC-AGI-2首位は製品力向上の証拠（強める方向）だが、いずれも中国市場中心でグローバル直接証拠ではない。対外投資規制 [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036)（A-1）の障壁は継続する。[H-BTD-002](../config/hypotheses.json) は43% low。EC収益化81.1%はモデル核心メカニズムが動く証拠（強める方向）だが、日収入<日コストの構造的ギャップは genuine な制約として残る。[H-BTD-003](../config/hypotheses.json) は40% mediumで±0%。著作権関連の新証拠はなく、対外投資規制・国家AI計画は規制インフラ拡大の証拠（強める方向）として蓄積している。

DeerFlow 2.0のオープンソース化 [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008)（B-3）は、ByteDanceがエージェントプラットフォーム領域でOSS戦略を併用していることを示す。Claude-to-DeerFlow マイグレーションツールの提供は、開発者獲得競争でByteDanceが能動的に動いている証拠だが、B-3品質であり、グローバル展開の直接証拠ではない。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Seed 2.1 Pro: コーディングClaude Opus 4.7匹敵・コスト80%削減・ARC-AGI-2首位0.625・Seedance 2.5 30秒4K動画 | [H-BTD-001](../config/hypotheses.json) フロンティアモデル新規リリース。製品力向上（強める方向）。但し自家測定・独立検証なし | A-3 | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) |
| 高 | 豆包DAU 2億超・日収入<100万元 vs 日コスト数千万元。雅虎香港財経等複数ソース | Freemium + ECモデルの財務構造。日収入<日コストの構造的ギャップは genuine。Seed 2.1 コスト80%削減で日コスト推算の下方修正要因 | A-2 | [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) |
| 高 | QuestMobile: 豆包APP MAU 1.47億・抖音APP MAU 3.3億・収益化価値の81.1%がEC経由 | Freemium + ECモデルの核心メカニズムが動いている（強める方向）。低価格（無料層）で集客しEC・広告・抖音シナジーでクロス収益化する構造を定量裏付け | B-2 | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) |
| 高 | CAPEX約2000億元超に上方修正。RMB 2,300億・$700億とほぼ整合。中国5年$295B国家計画 | 投資加速の複数ソース確認。Freemiumモデルの赤字を支える資本基盤。[IND-029](../config/indicators.json) high/rising | B-3 | [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) |
| 高 | 中国対外投資規制強化: 7月1日発効・AIセクター影響懸念 | [H-BTD-003](../config/hypotheses.json) 規制強化の証拠（強める方向）。[H-BTD-001](../config/hypotheses.json) グローバル障壁追加（弱める方向） | A-1 | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) |
| 中 | DeerFlow 2.0 OSS化: LangGraphベース・Claude-to-DeerFlow マイグレーションツール提供 | [H-BTD-001](../config/hypotheses.json) エージェントプラットフォーム領域でのOSS戦略併用。開発者獲得競争への参入。但しB-3品質・グローバル直接証拠ではない | B-3 | [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) |
| 中 | 火山引擎が中国agent開発プラットフォーム市場で双首位・Coze 3.0アップグレード | [H-BTD-001](../config/hypotheses.json) エコシステム拡大（強める方向）。中国市場中心 | B-2 | [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) |
| 中 | 豆包プロフェッショナル版有料化（最高5,088元/年）・豆包有料版（Pro）ローンチ | Freemiumモデル内の階層化。有料化でMAU 6.1M減少は転換の摩擦データ | A-2 | [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 豆包のEC転換率（EC収益化シェア）が急落し、81.1%から大幅に低下する | Freemium + ECモデルの収益メカニズムが機能しなくなり、[H-BTD-002](../config/hypotheses.json) のコア判断が崩れる | 90日 | [IND-010](../config/indicators.json) |
| 豆包DAUが3ヶ月連続で大幅減少（2億を下回る） | Freemiumモデルの「集客」段階が破綻し、[H-BTD-001](../config/hypotheses.json) の規模優位前提が崩れる | 90日 | [IND-011](../config/indicators.json) |
| ByteDanceのグローバルAI展開（Doubao/Seed海外版・現地語対応・海外サーバー）が独立確認される | [H-BTD-001](../config/hypotheses.json) の「グローバル展開証拠欠落」判断が崩れ、確度が大幅上昇する | 180日 | [IND-011](../config/indicators.json) |
| Seed 2.1のClaude Opus 4.7匹敵が独立ベンチマークで否定される | [H-BTD-001](../config/hypotheses.json) のフロンティア能力評価の下方修正が必要になる | 90日 | [IND-011](../config/indicators.json) |
| 日コスト推算が実際の限界コストに近いことが独立検証される（赤字が構造的に拡大） | [H-BTD-002](../config/hypotheses.json) の財務的持続性への読みが下方に確定する | 120日 | [IND-010](../config/indicators.json) |
| 中国規制当局がByteDanceのAIサービスライセンスを取り消す・停止する | [H-BTD-001](../config/hypotheses.json)・[H-BTD-002](../config/hypotheses.json) の両方が崩れる。事業基盤への打撃 | 60日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | 中国で取った規模を足がかりにグローバル展開する | 64% medium | Seed 2.1 Claude Opus 4.7匹敵・ARC-AGI-2首位(INFO-060)・Seedance 2.5 30秒4K・DeerFlow 2.0 OSS(INFO-008)・Coze 3.0・CAPEX 2000億元・中国$295B国家計画で製品力向上蓄積。DAU 2億超(INFO-041)で規模維持。但しグローバル直接証拠は欠落・対外投資規制(INFO-036)で障壁・Seed人材流出(~70名)でR&D懸念。ミラーイメージング警告継続。中国情報源の限定により独立裏付けなし | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) |
| [H-BTD-002](../config/hypotheses.json) | 豆包でFreemium + ECシナジーモデルを維持し、低価格（無料層）でのユーザー獲得からEC・広告・抖音シナジーを通じたクロス収益化で競争優位を維持する | 43% low | EC収益化81.1%(INFO-013)はモデル核心メカニズムが動く証拠。DAU 2億超(INFO-041)で集客段階機能中。有料層（プロフェッショナル版・有料コンテンツ）はモデル内階層化。Seed 2.1 コスト80%削減(INFO-060)で日コスト推算の下方要因。ただし日収入<100万元 vs 日コスト数千万元(INFO-041)の構造的ギャップは genuine な制約。日コストはAPI推算で過大評価リスク・ミラーイメージングリスクあり | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) |
| [H-BTD-003](../config/hypotheses.json) | 著作権・規制の制約が競争力を削ぐ | 40% medium | 対外投資規制(INFO-036 A-1)は規制強化の証拠。中国$295B国家計画(INFO-040)は規制インフラ拡大の証拠。ただし著作権関連の新証拠はなく、Seed人材流出は著作権とは別次元。中国情報源の限定により独立裏付けなし | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | (著作権領域での新証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | 豆包DAU 2億超(INFO-041 B-2)・豆包APP MAU 1.47億/抖音APP 3.3億(INFO-013 B-2)。MAUにソース間乖離（3.45億・3.3億・1.47億）。Seed 2.1 Pro ARC-AGI-2首位0.625(INFO-060 A-3)。Seedance 2.5 30秒4K動画。火山引擎agent市場双首位・Coze 3.0(INFO-109) | 2026-06-28 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・DeepSeek価格逆転・日コスト赤字拡大でhigh | EC収益化81.1%(INFO-013 B-2)・日収入<100万元 vs 日コスト数千万元(INFO-041 A-2)。Seed 2.1 コスト80%削減(INFO-060 A-3)で日コスト推算の下方要因。豆包Pro有料化(最高5,088元/年)。DeepSeek $7.4B初外部資金(INFO-033)。中国API西側比90%安 | 2026-06-28 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | CAPEX約2000億元超(INFO-054 B-3)・RMB 2,300億(INFO-032 B-2)・$700億(INFO-045 B-3)とほぼ整合。中国5年$295B国家AI計画(INFO-040)。独自CPU開発・国内調達比率約50%(INFO-032) | 2026-06-28 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | **critical/rising**。対外投資規制7/1発効(INFO-036 A-1)。中国$295B国家計画(INFO-040)。Operation Epic Fury 96h/2,000標的で軍事AI相転移・全球IND-030 critical伝播。Seed人材流出年間約70名(INFO-032) | 2026-06-28 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-28 | 全面書き直し。Seed 2.1新規リリース（[INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) A-3: Claude Opus 4.7匹敵・コスト80%削減・ARC-AGI-2首位0.625・Seedance 2.5 30秒4K）・DeerFlow 2.0 OSS（[INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) B-3）を反映。7日間の鮮度タイムアウト解消 | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) | H-BTD-001 64%(±0%)・H-BTD-002 44→43%・H-BTD-003 40%(±0%) |
| 2026-06-21 | ターゲット編集。[IND-030](../config/indicators.json) high→critical移行反映。Seedance 2.0 mini品質A-2・豆包DAU 2億超/日収入<100万元の品質A-2格上げを反映 | [INFO-042](../Information/2026-06-21/collected-raw.md#INFO-042) [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) | IND-030 high→critical |
| 2026-06-20 | [H-BTD-002](../config/hypotheses.json) 操作化再定義執行。EC 81.1%収益化のI誤分類を是正（I→強める方向）。全面書き直し | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | H-BTD-002 46→44% |
| 2026-06-13 | AI4S製薬分社化・CAPEX 2000億元・豆包MAU 3.45億/有料コンテンツ6月開始・Seedanceカンヌを反映して全面書き直し | [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | H-BTD-002 48→46% |

## 7. ブラインドスポット

- 豆包MAUに複数ソース間で乖離がある。[INFO-055](../Information/2026-06-13/collected-raw.md#INFO-055)は3.45億、[INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044)は3.3億、[INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)は1.47億。DAU 2億超([INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041))は2ソースで整合するが、MAU 1.47億とDAU 2億は論理的に矛盾する（DAU>MAU）。定義・測定期間・方法論の差の判別が不能。
- 「日コスト数千万元」の算出方法が外部から検証できない。火山引擎API価格・モデル毛利率・ユーザー行動からの推算であり、実際の限界コストを過大評価している可能性がある。Seed 2.1のコスト80%削減がこの推算をどう変えるかも不明。
- Seed 2.1のClaude Opus 4.7匹敵はByteDance自家測定であり、独立ベンチマークでの検証が必要。ARC-AGI-2リーダーボード首位0.625は公開リーダーボードだが、評価条件・プロンプト手法の差が不明。
- ミラーイメージングリスクを統合判断が明示的に認めた。西側の「赤字＝持続不能」という財務基準を、EC・広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめると、モデルの優位を見落とす。逆に、このリスクを過大に考慮すると赤字の実相を過小評価する。判別手段がない。
- ByteDanceグローバルAI戦略への中国共産党の介入度が見えない。対外投資規制([INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036))と国家$295B計画([INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040))は党の関与の兆候だが、AI部門への介入の実態は公開情報にない。
- Seedance 2.5・Coze 3.0・DeerFlow 2.0・火山引擎agent市場双首位がいずれも中国市場中心の記述で、グローバル展開を含むかが不明。[H-BTD-001](../config/hypotheses.json) の蓄積は国内証拠中心で、グローバル投影のリスクが残る。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | Seed 2.1: Claude Opus 4.7匹敵・コスト80%削減・ARC-AGI-2首位0.625・Seedance 2.5 30秒4K(A-3) |
| [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) | DeerFlow 2.0 OSS: LangGraphベース・Claude-to-DeerFlow マイグレーションツール(B-3) |
| [INFO-042](../Information/2026-06-21/collected-raw.md#INFO-042) | Seedance 2.0 mini: 生成コスト約50%削減・業界初4モダリティ入力・AI製薬10億ドル分社(A-2) |
| [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) | 豆包DAU 2億超・日収入<100万元 vs 日コスト数千万元(A-2) |
| [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) | 豆包DAU 2億超・日収入<100万元 vs 日コスト数千万元・晩点Latepost中国語一次(B-2) |
| [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | QuestMobile: 豆包APP MAU 1.47億・抖音APP MAU 3.3億・収益化価値の81.1%がEC経由(B-2) |
| [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) | 火山引擎 中国agent開発プラットフォーム市場双首位・Coze 3.0(B-2) |
| [INFO-110](../Information/2026-06-20/collected-raw.md#INFO-110) | Seedance 2.0 SEED研究所マルチモーダル動画生成・1080p・音声同期(B-2) |
| [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | ByteDance AI4S製薬事業分社化・CAPEX 2000億元超上方修正(B-3) |
| [INFO-055](../Information/2026-06-13/collected-raw.md#INFO-055) | 豆包MAU 3.45億/DAU 2億・有料コンテンツ6月開始(B-3) |
| [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | 中国5年間2兆元（$2,950億）全国AIインフラ計画(A-3) |
| [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) | 豆包プロフェッショナル版有料化・4段階料金（最高5,088元/年）(B-2) |
| [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) | Doubao有料化MAU 6.1M減少・Seed 2 Mini 256K context(A-2) |
| [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) | 中国対外投資規制強化・7月1日発効(A-1) |
| [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) | Seed人材流出年間約70名・CAPEX RMB 1,600億→2,300億・独自CPU開発(B-2) |
| [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) | DeepSeek初外部資金調達$7.4B・評価額最大$59B(B-2) |
