# ByteDance

> 最終判断更新: 2026-06-20
> 全体確信度: 中
> 情報非対称性: 中国市場の透明性低・言論統制により、観測根拠は他社比で著しく限定的。確度%は記載するが、独立した裏付けを欠く項目が多い。豆包MAUに複数ソース間で乖離（3.45億・3.3億・1.47億）があり、定義・時期・方法論の差の判別が不能。日コスト「数千万元」は火山引擎API価格からの推算であり実際の限界コストを過大評価する可能性。中国情報源の限定により独立裏付けなし
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-011](../config/indicators.json) [IND-010](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はByteDanceを、豆包（Doubao）でFreemium + ECシナジーモデルを維持する企業と読んでいる。無料層で2億DAUを獲得し、収益化価値の81.1%をEC経由で回す構造だ [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)。最大の根拠は2点。QuestMobileが計測したEC収益化81.1%がモデルの収益メカニズムの稼働を示し [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)、晩点Latepostが報じた日収入<100万元（主にEC手数料）対 日コスト数千万元（API推算）の構造的ギャップ [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) がその財務的持続性への問いを残す。

もし豆包のEC転換率が急落するか、DAUが3ヶ月連続で大幅に減少するか、グローバル展開（Doubao海外版・現地語対応）が独立確認されれば、コア判断の前提が変わる。[H-BTD-001](../config/hypotheses.json) 64% medium・[H-BTD-002](../config/hypotheses.json) 44% low・[H-BTD-003](../config/hypotheses.json) 40% medium。

## 1. コア判断

ByteDanceのAI事業を読み直した。前回（2026-06-13）は「有料コンテンツ開始で低価格戦略の終焉が加速」と評価していた。この読みは間違っていた。有料コンテンツもEC収益化も抖音シナジーも、ByteDanceが維持しているFreemium + ECモデルの構成要素であり、低価格戦略の終わりではない。本日の統合判断が執行した [H-BTD-002](../config/hypotheses.json) の操作化再定義は、まさにこの点を修正する [arbiter-2026-06-20](../state/arbiter-2026-06-20.md)。決定的だったのは、QuestMobileのEC収益化81.1%というデータ [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)（B-2）の解釈を間違えていたことだ。低価格戦略とは「価格を低く保つ」ことであり、「収益化しない」ことではない。豆包APP（MAU 1.47億）と抖音APP（MAU 3.3億）で無料層のユーザーを集め、そのトラフィックをEC手数料・広告・抖音シナジーに転換する。収益化価値の81.1%がEC経由という数字は、このモデルの核心メカニズムが動いている証拠（C方向）であり、モデルを否定する証拠（I方向）ではない。以前はこれをIに分類していた。論理が逆転していた。

一方で、財務的持続性の問いは残る。晩点Latepostが報じた豆包の日収入<100万元（主にEC手数料）対 日コスト数千万元（火山引擎API推算）の構造的ギャップ [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108)（B-2・中国語一次ソース）は本物だ。DAU 2億超の規模を維持するコストが、アプリ直接収入を大きく上回る。ただし「日コスト数千万元」はAPI価格・毛利率・ユーザー行動からの推算であり、実際の限界コストを過大評価している可能性がある。西側の財務基準を中国の消費者アプリにそのまま当てはめるミラーイメージングのリスクも、統合判断が明示的に認めた。[H-BTD-002](../config/hypotheses.json) は44% low。モデルは機能しているが、財務的持続性の確証は取れていない。

投資とエコシステムの方向は変わらない。2026年AI関連CAPEX約2000億元 [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) と中国5年2兆元（$2,950億）国家AIインフラ計画 [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) の文脈は維持される。火山引擎が中国agent開発プラットフォーム市場で双首位を獲得し、Coze（扣子）が3.0へアップグレードした [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109)（B-2）。Seedance 2.0はSEED研究所のマルチモーダル動画生成として1080p・音声同期を実現した [INFO-110](../Information/2026-06-20/collected-raw.md#INFO-110)（B-2）。これらは [H-BTD-001](../config/hypotheses.json) のC蓄積だが、いずれも中国市場中心でグローバル直接証拠ではない。グローバル展開証拠の欠落と対外投資規制 [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) の障壁は継続する。確信度は「中」にとどめる。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | QuestMobile: 豆包APP MAU 1.47億・抖音APP MAU 3.3億・収益化価値の81.1%がEC経由 | Freemium + ECモデルの核心メカニズムが動いている証拠（C）。以前のI誤分類を是正。低価格（無料層）で集客しEC・広告・抖音シナジーでクロス収益化する構造を定量裏付け | B-2 | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) |
| 高 | 晩点Latepost: 豆包DAU 2億超・日収入<100万元（主にEC手数料）vs 日コスト数千万元（API推算） | Freemium + ECモデルの財務的持続性への問い（I）。日収入<日コストの構造的ギャップはgenuine。ただし日コストは推算で限界コスト過大評価リスク・ミラーイメージングリスクあり | B-2 | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) |
| 高 | 豆包DAU 2億超（上半期）。INFO-055(06-13)のDAU 2億と整合 | 無料層での規模獲得が維持されている。Freemiumモデルの「集客」段階は機能中。MAU数値にソース間乖離（3.45億・3.3億・1.47億）あり | B-2 | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-055](../Information/2026-06-13/collected-raw.md#INFO-055) |
| 高 | CAPEX約2000億元超に上方修正（約1,600億元から）。RMB 2,300億・$700億とほぼ整合 | 投資加速の複数ソース確認。中国5年$295B国家計画(INFO-040)の文脈。Freemiumモデルの赤字を支える資本基盤 | B-3 | [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) |
| 高 | 中国5年間2兆元（$2,950億）全国AIインフラ計画・Bloomberg報道 | ByteDance CAPEX 2000億元の文脈。国家主導インフラ投資。[H-BTD-001](../config/hypotheses.json) のC・[H-BTD-003](../config/hypotheses.json) のC | A-3 | [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) |
| 高 | 火山引擎が中国agent開発プラットフォーム市場で双首位・Coze 3.0アップグレード | Agent生態系の強化。[H-BTD-001](../config/hypotheses.json) のC（エコシステム拡大）。中国市場中心でグローバル直接証拠ではない | B-2 | [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) |
| 中 | Seedance 2.0: SEED研究所マルチモーダル動画生成・1080p・音声同期・即夢経由 | 製品品質の維持。Video Arena世界#2(INFO-039)の延長。[H-BTD-001](../config/hypotheses.json) のC | B-2 | [INFO-110](../Information/2026-06-20/collected-raw.md#INFO-110) [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039) |
| 中 | 豆包プロフェッショナル版有料化（最高5,088元/年）・豆包有料コンテンツ6月開始 | Freemiumモデルの「有料層」構成要素。低価格戦略の終焉ではなくモデル内の階層化。有料化でMAU 6.1M減少は転換の摩擦データ | A-2 | [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) [INFO-055](../Information/2026-06-13/collected-raw.md#INFO-055) |
| 中 | DeepSeek初外部資金調達$7.4B（Tencent約RMB 100億・CATL）・評価額最大$59B | 低価格競争の激化要因。Freemiumモデル独自性には直接影響しないが、API価格コモディティ化圧力 | B-2 | [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) |
| 中 | 中国対外投資規制強化: 7月1日発効・AIセクター影響懸念 | [H-BTD-003](../config/hypotheses.json) のC（規制強化）。[H-BTD-001](../config/hypotheses.json) のI（グローバル障壁追加） | A-1 | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) |
| 中 | Seed人材流出 年間約70名・独自CPU開発（ARM/RISC-V検討） | 人材流出はR&D持続力への懸念（I）。CAPEX増額は投資加速の確認（C） | B-2 | [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 豆包のEC転換率（EC収益化シェア）が急落し、81.1%から大幅に低下する | Freemium + ECモデルの収益メカニズムが機能しなくなり、[H-BTD-002](../config/hypotheses.json) のコア判断が崩れる。日収入<日コストのギャップが解決不能になる | 90日 | [IND-010](../config/indicators.json) |
| 豆包DAUが3ヶ月連続で大幅減少（2億を下回る）、またはMAUが持続的低下 | Freemiumモデルの「集客」段階が破綻し、[H-BTD-001](../config/hypotheses.json) の規模優位前提と [H-BTD-002](../config/hypotheses.json) の土台が崩れる | 90日 | [IND-011](../config/indicators.json) |
| ByteDanceのグローバルAI展開（Doubao/Seed海外版・現地語対応・海外サーバー）が独立確認される | [H-BTD-001](../config/hypotheses.json) の「グローバル展開証拠欠落」判断が崩れ、確度が大幅上昇する。ミラーイメージング警告の解除条件 | 180日 | [IND-011](../config/indicators.json) |
| 日コスト推算が実際の限界コストに近いことが独立検証される（赤字が構造的に拡大） | [H-BTD-002](../config/hypotheses.json) の財務的持続性への読みが下方に確定する。ミラーイメージングリスクの誤判定も露見する | 120日 | [IND-010](../config/indicators.json) |
| DeepSeekがDoubao有料版と同等以下の価格でコンシューマ向けサービスを展開し、豆包シェアを侵食する | [H-BTD-002](../config/hypotheses.json) の競争優位が崩れ、low帯深化が確定する。価格コモディティ化がByteDance固有の優位を消費する | 60日 | [IND-010](../config/indicators.json) |
| 中国規制当局がByteDanceのAIサービスライセンスを取り消す・停止する | [H-BTD-001](../config/hypotheses.json)・[H-BTD-002](../config/hypotheses.json) の両方が崩れる。事業基盤そのものへの打撃 | 60日 | [IND-030](../config/indicators.json) |
| Seed人材流出が加速（年間100名超）または主力モデルのリリース間隔が延長する | R&D持続力の低下が確認され、[H-BTD-001](../config/hypotheses.json) の確度に影響する。製品品質の維持が困難になる | 180日 | [IND-011](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | 中国で取った規模を足がかりにグローバル展開する | 64% medium | 火山引擎agent市場双首位(INFO-109)・Coze 3.0・Seedance 2.0(INFO-110)・AI4S分社化・4優先領域・CAPEX 2000億元・中国$295B国家計画でC蓄積継続。DAU 2億超(INFO-108)で規模維持。但しグローバル直接証拠は欠落・対外投資規制(INFO-036)で障壁・Seed人材流出(~70名)でR&D懸念。ミラーイメージング警告継続。中国情報源の限定により独立裏付けなし | [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) [INFO-110](../Information/2026-06-20/collected-raw.md#INFO-110) [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) |
| [H-BTD-002](../config/hypotheses.json) | 豆包でFreemium + ECシナジーモデルを維持し、低価格（無料層）でのユーザー獲得からEC・広告・抖音シナジーを通じたクロス収益化で競争優位を維持する | 44% low | EC収益化81.1%(INFO-013)はモデル核心メカニズムが動くC証拠（以前のI誤分類を是正）。DAU 2億超(INFO-108)で集客段階機能中。有料層（プロフェッショナル版・有料コンテンツ）はモデル内階層化。ただし日収入<100万元 vs 日コスト数千万元(INFO-108)の構造的ギャップはgenuineなI。日コストはAPI推算で過大評価リスク・ミラーイメージングリスクあり。モデルは機能するが財務的持続性の確証なし | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) |
| [H-BTD-003](../config/hypotheses.json) | 著作権・規制の制約が競争力を削ぐ | 40% medium | 対外投資規制(INFO-036 A-1)は規制強化のC。中国$295B国家計画(INFO-040)は規制インフラ拡大のC。ただし著作権関連の新証拠はなく、Seed人材流出は著作権とは別次元。中国情報源の限定により独立裏付けなし | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | (著作権領域での新証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | 豆包DAU 2億超(INFO-108 B-2)・豆包APP MAU 1.47億/抖音APP 3.3億(INFO-013 B-2)。MAUにソース間乖離（3.45億・3.3億・1.47億）。Seedance 2.0 SEED研究所(INFO-110)。火山引擎agent市場双首位・Coze 3.0(INFO-109) | 2026-06-20 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・DeepSeek価格逆転・日コスト赤字拡大でhigh | EC収益化81.1%(INFO-013 B-2)・日収入<100万元 vs 日コスト数千万元(INFO-108 B-2)。豆包プロフェッショナル版有料化(最高5,088元/年)・有料コンテンツ6月開始(INFO-031/055)。DeepSeek $7.4B初外部資金(INFO-033)。中国API西側比90%安(INFO-060) | 2026-06-20 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | CAPEX約2000億元超(INFO-054 B-3)・RMB 2,300億(INFO-032 B-2)・$700億(INFO-045 B-3)とほぼ整合。中国5年$295B国家AI計画(INFO-040)。独自CPU開発・国内調達比率約50%(INFO-032) | 2026-06-20 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | CAC追加警告・ライセンス停止・TikTok分断のいずれかでhigh | 対外投資規制7/1発効(INFO-036 A-1)。中国$295B国家計画(INFO-040)による規制インフラ拡大の可能性。民間AI人材渡航制限拡大(INFO-026)。Seed人材流出年間約70名(INFO-032) | 2026-06-20 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-20 | [H-BTD-002](../config/hypotheses.json) 操作化再定義執行（「低価格戦略維持」→「Freemium + ECシナジーモデル維持」）。EC 81.1%収益化のI誤分類を是正（I→C）。INFO-108（日収入<日コスト構造的ギャップ・中国語一次ソース）・INFO-013（EC収益化81.1%）・INFO-109（火山引擎agent市場双首位・Coze 3.0）・INFO-110（Seedance 2.0 SEED研究所）を反映して全面書き直し。7日鮮度タイムアウト対応 | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) [INFO-110](../Information/2026-06-20/collected-raw.md#INFO-110) | H-BTD-001 64%(±0%)・H-BTD-002 46→44%（低価格戦略終焉→Freemium+ECモデル再定義）・H-BTD-003 40%(±0%) |
| 2026-06-13 | AI4S製薬分社化・CAPEX 2000億元・豆包MAU 3.45億/有料コンテンツ6月開始・Seedanceカンヌ・4優先領域を反映して全面書き直し | [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) [INFO-055](../Information/2026-06-13/collected-raw.md#INFO-055) | H-BTD-001 64%(±0%)・H-BTD-002 48→46%・H-BTD-003 40%(±0%) |
| 2026-06-06 | 豆包有料化MAU 6.1M減少・Coze 3.0・対外投資規制・Seed 2 Miniを反映して全面書き直し | [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047) [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) | H-BTD-002 49→48% |
| 2026-06-04 | 豆包プロフェッショナル版有料化・Seed人材流出~70名・DeepSeek $7.4B・MAU 3.45→3.3億を反映して全面書き直し | [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) | H-BTD-002 51→49%（medium→low移行） |

## 7. ブラインドスポット

- 豆包MAUに複数ソース間で乖離がある。[INFO-055](../Information/2026-06-13/collected-raw.md#INFO-055)(06-13)は3.45億、[INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044)(06-04)は3.3億、[INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)(本日・QuestMobile)は1.47億。DAU 2億超(INFO-108/055)は2ソースで整合するが、MAU 1.47億とDAU 2億は論理的に矛盾する（DAU>MAU）。定義（豆包APP単体 vs 抖音統合含む）・測定期間・方法論の差の判別が不能。規模優位の判断がどの数字に依存するかで確度が変わる。
- 「日コスト数千万元」の算出方法が外部から検証できない。火山引擎API価格・モデル毛利率・ユーザー行動からの推算であり、実際の限界コスト（既存インフラの遊休容量・データセンターの減価償却済み部分）を過大評価している可能性がある。この推算が過大であれば、日収入<日コストのギャップは縮む。
- ミラーイメージングリスクを統合判断が明示的に認めた。西側の「赤字＝持続不能」という財務基準を、EC・広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめると、モデルの優位を見落とす。逆に、このリスクを過大に考慮すると赤字の実相を過小評価する。判別手段がない。
- 豆包の月次収益と収益構造の内訳が不明。EC 81.1%(INFO-013)は収益化価値の構成比であって絶対額ではない。有料層（プロフェッショナル版・有料コンテンツ）の課金転換率・解約率・ARPUが外部から推定不能。「規模は見えるが、単位経済の健全部が見えない」の状態で確度を算出している。
- ByteDanceグローバルAI戦略への中国共産党の介入度が見えない。対外投資規制(INFO-036)と国家$295B計画(INFO-040)は党の関与の兆候だが、AI部門（Doubao/Seed）への介入の実態は公開情報にない。介入があれば製品ロードマップや人材配置が変わる。観測手段を持っていない。
- Seedance 2.0・Coze 3.0・火山引擎agent市場双首位がいずれも中国市場中心の記述で、グローバル展開を含むかが不明。[INFO-010](../Information/2026-06-13/collected-raw.md#INFO-010) が「グローバル展開の一環」と記載されるが、実際の海外利用状況は未確認。[H-BTD-001](../config/hypotheses.json) のC蓄積は国内証拠中心で、グローバル投影のリスクが残る。
- 米中規制摩擦でのコンピュート調達制約の実態が不明。独自CPU開発(ARM/RISC-V検討) [INFO-009](../Information/2026-06-01/collected-raw.md#INFO-009) は方向性を示すが量産・性能は未検証。国内調達比率約50% [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) の残り50%の調達先が不明。CAPEX 2000億元が実行可能かはチップ調達に依存する。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) | 豆包DAU 2億超・日収入<100万元（主にEC手数料）vs 日コスト数千万元（火山引擎API推算）(B-2・晩点Latepost中国語一次ソース) |
| [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | QuestMobile: 豆包APP MAU 1.47億・抖音APP MAU 3.3億・収益化価値の81.1%がEC経由(B-2) |
| [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) | 火山引擎 中国agent開発プラットフォーム市場双首位・Coze 3.0アップグレード(B-2) |
| [INFO-110](../Information/2026-06-20/collected-raw.md#INFO-110) | Seedance 2.0 SEED研究所マルチモーダル動画生成・1080p・音声同期(B-2) |
| [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | ByteDance AI4S製薬事業分社化・独立融資・CAPEX 2000億元超上方修正(B-3) |
| [INFO-055](../Information/2026-06-13/collected-raw.md#INFO-055) | 豆包MAU 3.45億/DAU 2億・有料コンテンツ6月開始(B-3) |
| [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | 中国5年間2兆元（$2,950億）全国AIインフラ計画(A-3) |
| [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) | 豆包プロフェッショナル版有料化・4段階料金（最高5,088元/年）(B-2) |
| [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) | Doubao有料化MAU 6.1M減少・Seed 2 Mini 256K context(A-2) |
| [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) | 中国対外投資規制強化・7月1日発効(A-1) |
| [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) | Seed人材流出年間約70名・CAPEX RMB 1,600億→2,300億・独自CPU開発(B-2) |
| [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) | DeepSeek初外部資金調達$7.4B・評価額最大$59B(B-2) |
| [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039) | Seedance 2.0 Video Arena世界#2（ELO 1,271）(A-3) |
| [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) | Doubao > ChatGPT・中国API西側比90%安・DeepSeek大幅値下げ(B-3) |
