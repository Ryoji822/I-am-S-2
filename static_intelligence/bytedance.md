# ByteDance

> 最終判断更新: 2026-06-30
> 全体確信度: 中
> 情報非対称性: 中国市場の透明性低・言論統制により、観測根拠は他社比で著しく限定的。確度%は記載するが、独立した裏付けを欠く項目が多い。豆包MAUに複数ソース間で乖離（3.45億・3.3億・1.47億）があり、定義・時期・方法論の差の判別が不能。日コスト「数千万元」は火山引擎API価格からの推算であり実際の限界コストを過大評価する可能性。Seed 2.1のコーディング能力Claude Opus 4.7匹敵はByteDance自家測定であり独立ベンチマークでの検証が未完了。中国情報源の限定により独立裏付けなし
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-010](../config/indicators.json) [IND-011](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

ByteDanceが約200億米ドルの境外融資を銀行と協議中である [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080)（A-2）。同社史上最大の境外融資で、期間3年（最大5年延長）、AIインフラ・計算基盤・チップ設計（Qualcomm協議）に充てる。前回（06-28）のSeed 2.1リリースに続き、資本と技術の両面でフロンティア追従を加速する姿勢は明確だが、豆包の日算力費数千万元 vs 日収入100万元未満という赤字構造がA-2品質で確認され [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095)、ギャップは数十倍に達する。AI資源の重点を豆包（消費者）から企業サービスへ移行中との報道 [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079)（A-2）は、消費者Freemiumモデルの限界を示唆する。

[H-BTD-001](../config/hypotheses.json) 64% medium（±0%）・[H-BTD-002](../config/hypotheses.json) 42% low（43→42%・low深化）・[H-BTD-003](../config/hypotheses.json) 40% medium（±0%）。もし豆包のEC転換率が急落するか、DAUが3ヶ月連続で大幅減少するか、グローバル展開が独立確認されれば、コア判断の前提が変わる。

## 1. コア判断

$200億の境外融資協議 [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080)（A-2）は2つの意味を持つ。第一に、ByteDanceのAI投資意欲が持続していることを示す。CAPEX約2000億元超 [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054)（B-3）に加え、Qualcommとのカスタムチップ設計協議、具身知能企業（自変量機器人）への投資参加（投後評価額200億元超）が報じられた。これらは [H-BTD-001](../config/hypotheses.json) のフロンティア追従を支える資本基盤の拡大である。

第二に、ユニットエコノミクスの改善を待たずにインフラを拡大している点である。豆包の日算力費数千万元に対し日収入は100万元未満であり [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095)（A-2）、ギャップは数十倍に達する。この数値は前回「日コスト数千万元 vs 日収入<100万元」と推算していた構造的ギャップ [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041)（A-2）を複数ソース（中国経営報・36kr・新浪財経・知乎）で確認した。Seed 2.1のコスト80%削減 [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060)（A-3）は日コスト推算の下方修正要因だが、数十倍のギャップを埋めるには不十分である。

豆包有料版（月額68〜500元）のローンチとSeedance年率収益$2B到達 [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079)（A-2）は収益化の試みであり、Seedanceは製品レベルでのマネタイズが成立している。ただし有料化で2026年5月にMAU約610万減少（-1.81%）が顕在化 [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095)（A-2）しており、収益化とユーザー離反のトレードオフが観測されている。ByteDanceはAI資源の重点を豆包から企業サービスへ移行中 [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079)（A-2）との報道は、消費者Freemiumモデルの限界と、より収益性の高いエンタープライズ領域への戦略ピボットを示唆する。

Freemium + ECシナジーモデルの読み方は2026-06-20の操作化再定義から継続する。QuestMobileの計測で収益化価値の81.1%がEC経由 [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)（B-2）であり、この構造自体は機能している。しかし日算力費vs日収入の数十倍ギャップがA-2品質で確定したことで、Freemiumモデルの財務的持続性に対する否定証拠の重みが増した。[H-BTD-002](../config/hypotheses.json) は43%から42%に低下し（low帯深化）、この方向を反映している。

[H-BTD-001](../config/hypotheses.json) は64% mediumで±0%。Seed 2.1・Seedance 2.5・ARC-AGI-2首位・$200億融資・CAPEX 2000億元は製品力と資本基盤の向上（強める方向）だが、いずれも中国市場中心でグローバル直接証拠ではない。対外投資規制 [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036)（A-1）の障壁は継続する。[H-BTD-003](../config/hypotheses.json) は40% mediumで±0%。著作権関連の新証拠はなく、対外投資規制・国家AI計画は規制インフラ拡大の証拠として蓄積している。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | $200億境外融資seeking・史上最大・期間3年・AIインフラ・チップ設計向け。Qualcommカスタムチップ協議 | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（強める方向）。[IND-029](../config/indicators.json) high/risingを更に強化。但しユニットエコノミクス改善不在 | A-2 | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) |
| 高 | 豆包DAU 2億突破・MAU 3.45億・日算力費数千万元 vs 日収入<100万元（ギャップ数十倍）。有料化でMAU 610万減少(-1.81%) | Freemium + ECモデルの財務構造。ギャップ数十倍が複数ソースでA-2確定。[H-BTD-002](../config/hypotheses.json) low深化の直接根拠。有料化vs離反トレードオフ顕在化 | A-2 | [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) |
| 高 | 豆包有料版ローンチ（68-500元/月）・Seedance年率$2B到達・AI資源重点を豆包→企業サービスへ移行 | 収益化加速と戦略ピボット。Seedance製品レベルマネタイズ成立。消費者Freemiumからの移行は[H-BTD-002](../config/hypotheses.json)核心命題への挑戦 | A-2 | [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079) |
| 高 | Seed 2.1 Pro: コーディングClaude Opus 4.7匹敵・コスト80%削減・ARC-AGI-2首位0.625・Seedance 2.5 30秒4K動画 | [H-BTD-001](../config/hypotheses.json) フロンティアモデル新規リリース。製品力向上（強める方向）。但し自家測定・独立検証なし | A-3 | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) |
| 高 | QuestMobile: 豆包APP MAU 1.47億・抖音APP MAU 3.3億・収益化価値の81.1%がEC経由 | Freemium + ECモデルの核心メカニズムが動いている（強める方向）。低価格（無料層）で集客しEC・広告・抖音シナジーでクロス収益化する構造を定量裏付け | B-2 | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) |
| 高 | CAPEX約2000億元超に上方修正。RMB 2,300億・$700億とほぼ整合。中国5年$295B国家計画 | 投資加速の複数ソース確認。Freemiumモデルの赤字を支える資本基盤。[IND-029](../config/indicators.json) high/rising | B-3 | [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) |
| 高 | 中国対外投資規制強化: 7月1日発効・AIセクター影響懸念 | [H-BTD-003](../config/hypotheses.json) 規制強化の証拠（強める方向）。[H-BTD-001](../config/hypotheses.json) グローバル障壁追加（弱める方向） | A-1 | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) |
| 中 | DeerFlow 2.0 OSS化: LangGraphベース・Claude-to-DeerFlow マイグレーションツール提供 | [H-BTD-001](../config/hypotheses.json) エージェントプラットフォーム領域でのOSS戦略併用。開発者獲得競争への参入。但しB-3品質・グローバル直接証拠ではない | B-3 | [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) |
| 中 | 火山引擎が中国agent開発プラットフォーム市場で双首位・Coze 3.0アップグレード | [H-BTD-001](../config/hypotheses.json) エコシステム拡大（強める方向）。中国市場中心 | B-2 | [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) |

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
| [H-BTD-001](../config/hypotheses.json) | 中国で取った規模を足がかりにグローバル展開する | 64% medium | Seed 2.1 Claude Opus 4.7匹敵・ARC-AGI-2首位(INFO-060)・Seedance 2.5 30秒4K・$200億境外融資(INFO-080)・DeerFlow 2.0 OSS(INFO-008)・Coze 3.0・CAPEX 2000億元・中国$295B国家計画で製品力向上蓄積。DAU 2億超(INFO-041)で規模維持。但しグローバル直接証拠は欠落・対外投資規制(INFO-036)で障壁・Seed人材流出(~70名)でR&D懸念。ミラーイメージング警告継続。中国情報源の限定により独立裏付けなし | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) |
| [H-BTD-002](../config/hypotheses.json) | 豆包でFreemium + ECシナジーモデルを維持し、低価格（無料層）でのユーザー獲得からEC・広告・抖音シナジーを通じたクロス収益化で競争優位を維持する | 42% low | -1%（43→42%・low深化）。INFO-095(A-2)日算力費数千万元 vs 日収入<100万元のギャップ数十倍はFreemium持続性の最も直接的定量否定。有料化でMAU 610万減少(-1.81%)=収益化vs離反トレードオフ。戦略ピボット(消費者→企業)で消費者Freemium放棄方向(INFO-079)。EC収益化81.1%(INFO-013)はモデル核心メカニズムが動く証拠。Seed 2.1 コスト80%削減(INFO-060)で日コスト推算の下方要因。ただしギャップ数十倍はgenuineな制約。日コストはAPI推算で過大評価リスク・ミラーイメージングリスクあり | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079) [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) |
| [H-BTD-003](../config/hypotheses.json) | 著作権・規制の制約が競争力を削ぐ | 40% medium | 対外投資規制(INFO-036 A-1)は規制強化の証拠。中国$295B国家計画(INFO-040)は規制インフラ拡大の証拠。ただし著作権関連の新証拠はなく、Seed人材流出は著作権とは別次元。中国情報源の限定により独立裏付けなし | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | (著作権領域での新証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | 豆包DAU 2億超(INFO-095 A-2)・豆包MAU 3.45億(INFO-095 A-2)・豆包APP MAU 1.47億/抖音APP 3.3億(INFO-013 B-2)。MAUにソース間乖離（3.45億・3.3億・1.47億）。有料化でMAU 610万減少(-1.81%)。Seed 2.1 Pro ARC-AGI-2首位0.625(INFO-060 A-3)。Seedance 2.5 30秒4K。火山引擎agent市場双首位・Coze 3.0(INFO-109) | 2026-06-30 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・DeepSeek価格逆転・日コスト赤字拡大でhigh | 日算力費数千万元 vs 日収入<100万元・ギャップ数十倍(INFO-095 A-2)。EC収益化81.1%(INFO-013 B-2)。Seed 2.1 コスト80%削減(INFO-060 A-3)。豆包有料版68-500元/月(INFO-079 A-2)。Seedance年率$2B(INFO-079 A-2)。DeepSeek $7.4B初外部資金(INFO-033)。中国API西側比90%安 | 2026-06-30 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | $200億境外融資seeking・史上最大(INFO-080 A-2)・CAPEX約2000億元超(INFO-054 B-3)・RMB 2,300億(INFO-032 B-2)・$700億(INFO-045 B-3)とほぼ整合。中国5年$295B国家AI計画(INFO-040)。独自CPU開発・国内調達比率約50%(INFO-032)。Qualcommカスタムチップ協議(INFO-080) | 2026-06-30 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | **critical/rising**。対外投資規制7/1発効(INFO-036 A-1)。中国$295B国家計画(INFO-040)。Operation Epic Fury 96h/2,000標的で軍事AI相転移・全球IND-030 critical伝播。Seed人材流出年間約70名(INFO-032)。INFO-093(A-2): PentagonはHITLを公式要求したことがない=選択的執行 | 2026-06-30 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-30 | ターゲット編集。$200億境外融資seeking(INFO-080 A-2: 史上最大・AIインフラ・チップ設計向け)を新規反映。日算力費vs日収入ギャップ数十倍のA-2品質複数ソース確認(INFO-095)を反映。豆包有料版68-500元/月・Seedance $2B ARR・戦略ピボット(INFO-079 A-2)を反映。[H-BTD-002](../config/hypotheses.json) 43→42% | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079) | H-BTD-002 43→42% |
| 2026-06-28 | 全面書き直し。Seed 2.1新規リリース（[INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) A-3: Claude Opus 4.7匹敵・コスト80%削減・ARC-AGI-2首位0.625・Seedance 2.5 30秒4K）・DeerFlow 2.0 OSS（[INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) B-3）を反映。7日間の鮮度タイムアウト解消 | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) | H-BTD-001 64%(±0%)・H-BTD-002 44→43%・H-BTD-003 40%(±0%) |
| 2026-06-21 | ターゲット編集。[IND-030](../config/indicators.json) high→critical移行反映。Seedance 2.0 mini品質A-2・豆包DAU 2億超/日収入<100万元の品質A-2格上げを反映 | [INFO-042](../Information/2026-06-21/collected-raw.md#INFO-042) [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) | IND-030 high→critical |
| 2026-06-20 | [H-BTD-002](../config/hypotheses.json) 操作化再定義執行。EC 81.1%収益化のI誤分類を是正（I→強める方向）。全面書き直し | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | H-BTD-002 46→44% |
| 2026-06-13 | AI4S製薬分社化・CAPEX 2000億元・豆包MAU 3.45億/有料コンテンツ6月開始・Seedanceカンヌを反映して全面書き直し | [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | H-BTD-002 48→46% |

## 7. ブラインドスポット

- 豆包MAUに複数ソース間で乖離がある。[INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095)は3.45億（QuestMobile 2026年3月）、[INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044)は3.3億、[INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)は1.47億。DAU 2億超([INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095))は複数ソースで整合するが、MAU 1.47億とDAU 2億は論理的に矛盾する（DAU>MAU）。定義・測定期間・方法論の差の判別が不能。
- 「日コスト数千万元」の算出方法が外部から検証できない。火山引擎API価格・モデル毛利率・ユーザー行動からの推算であり、実際の限界コストを過大評価している可能性がある。Seed 2.1のコスト80%削減がこの推算をどう変えるかも不明。INFO-095が「数十倍」という表現でギャップを確認したが、推算の前提自体に変化はない。
- $200億境外融資([INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080))の使途が「AI関連業務」という報道ベースであり、実際の配分（データセンター・計算インフラ・大模型研究・チップ設計）の内訳が不明。Qualcommとのチップ協議も「協議中」であり確定ではない。
- Seed 2.1のClaude Opus 4.7匹敵はByteDance自家測定であり、独立ベンチマークでの検証が必要。ARC-AGI-2リーダーボード首位0.625は公開リーダーボードだが、評価条件・プロンプト手法の差が不明。
- ミラーイメージングリスクを統合判断が明示的に認めた。西側の「赤字＝持続不能」という財務基準を、EC・広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめると、モデルの優位を見落とす。逆に、このリスクを過大に考慮すると赤字の実相を過小評価する。判別手段がない。
- AI資源重点を豆包→企業サービスへ移行([INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079))との報道が、消費者Freemiumの完全放棄か、企業領域への追加投資かが判別できない。前者であれば[H-BTD-002](../config/hypotheses.json)の核心命題が崩れる。後者であれば現行の読みは維持される。
- ByteDanceグローバルAI戦略への中国共産党の介入度が見えない。対外投資規制([INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036))と国家$295B計画([INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040))は党の関与の兆候だが、AI部門への介入の実態は公開情報にない。
- Seedance 2.5・Coze 3.0・DeerFlow 2.0・火山引擎agent市場双首位がいずれも中国市場中心の記述で、グローバル展開を含むかが不明。[H-BTD-001](../config/hypotheses.json) の蓄積は国内証拠中心で、グローバル投影のリスクが残る。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) | $200億境外融資seeking・史上最大・AIインフラ・チップ設計向け(A-2) |
| [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) | 豆包DAU 2億突破・MAU 3.45億・日算力費数千万元vs日収入<100万元（ギャップ数十倍）・有料化MAU 610万減少(A-2) |
| [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079) | 豆包有料版68-500元/月・Seedance年率$2B・AI資源重点を豆包→企業サービスへ移行(A-2) |
| [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | Seed 2.1: Claude Opus 4.7匹敵・コスト80%削減・ARC-AGI-2首位0.625・Seedance 2.5 30秒4K(A-3) |
| [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) | DeerFlow 2.0 OSS: LangGraphベース・Claude-to-DeerFlow マイグレーションツール(B-3) |
| [INFO-042](../Information/2026-06-21/collected-raw.md#INFO-042) | Seedance 2.0 mini: 生成コスト約50%削減・業界初4モダリティ入力・AI製薬10億ドル分社(A-2) |
| [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) | 豆包DAU 2億超・日収入<100万元 vs 日コスト数千万元(A-2) |
| [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) | 豆包DAU 2億超・日収入<100万元 vs 日コスト数千万元・晩点Latepost中国語一次(B-2) |
| [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | QuestMobile: 豆包APP MAU 1.47億・抖音APP MAU 3.3億・収益化価値の81.1%がEC経由(B-2) |
| [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) | 火山引擎 中国agent開発プラットフォーム市場双首位・Coze 3.0(B-2) |
| [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | ByteDance AI4S製薬事業分社化・CAPEX 2000億元超上方修正(B-3) |
| [INFO-055](../Information/2026-06-13/collected-raw.md#INFO-055) | 豆包MAU 3.45億/DAU 2億・有料コンテンツ6月開始(B-3) |
| [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | 中国5年間2兆元（$2,950億）全国AIインフラ計画(A-3) |
| [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) | Doubao有料化MAU 6.1M減少・Seed 2 Mini 256K context(A-2) |
| [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) | 中国対外投資規制強化・7月1日発効(A-1) |
| [INFO-032](../Information/2026-06-04/collected-raw.md#INFO-032) | Seed人材流出年間約70名・CAPEX RMB 1,600億→2,300億・独自CPU開発(B-2) |
| [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) | DeepSeek初外部資金調達$7.4B・評価額最大$59B(B-2) |
