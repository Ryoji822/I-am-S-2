# ByteDance

> 最終判断更新: 2026-05-06
> 全体確信度: 中
> 情報非対称性: 中国市場の透明性低・言論統制により、観測根拠は他社比で著しく限定的。確度%は記載するが、独立した裏付けを欠く項目が多い
> 主参照: hypotheses.json#H-BTD-001/002/003, indicators.json#IND-011/010/030

## 0. 一文要約

我々はByteDanceを、**中国AI市場で唯一MAU 3.45億規模を取ったが、CAC規制・DeepSeek価格競合・純利益急減が同時進行しており「低価格で世界へ」戦略の持続可能性が現時点で独立裏付けを欠く企業**と読んでいる。最大の根拠は3点。Doubao MAU 3.45億という規模感 [INFO-070](../Information/2026-05-06/collected-raw.md#INFO-070)、Seed 2.0 Pro が Claude Opus 比で約10倍安という価格事実 [INFO-071](../Information/2026-05-06/collected-raw.md#INFO-071)、そして2025年純利益が70%以上減少した財務圧力 [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011)。「中国規制当局が ByteDance の AI ライセンスを取り消す」「Doubao の MAU 増加が3ヶ月停滞する」「DeepSeek が Doubao より安い価格を維持する」のいずれかが観測されたら、現在の読みは更新が要る。

## 1. コア判断

ByteDance のAI事業の現構図は、**規模は本物だが、それを支える経済モデルが今まさに試されている**という局面にある。

規模の根拠は具体的だ。Doubao MAU 3.45億・DAU 1.45億。日次トークン使用量120兆超、2年で1000倍という成長率。中国AIアプリで首位の座は数字として確認できる。Seed 2.0 Pro は $0.47/M入力・$2.37/M出力と、 Claude Opus 比で約10倍安い。この低価格で日次120兆トークンを捌いていること自体が、ByteDance の規模の優位を示す。

だが2026年5月時点で、その優位を支える構造に3つの圧力が同時にかかっている。第一は規制。中国サイバースペース規制当局（CAC）がByteDanceのアプリ3本（Jianying/Maoxiang/Jimeng AI）にAI生成コンテンツのラベリング法違反で警告を出した [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011)。警告はアプリ単位だが、規制執行が強まる先例になる。第二は価格競合。DeepSeek が量的ヘッジファンド High-Flyer Capital の支援のもと低価格を維持しており [INFO-068](../Information/2026-05-06/collected-raw.md#INFO-068)、API価格次元での ByteDance の優位が削られている。DeepSeek V4 は $0.0036/M という価格帯まで引き下げている。第三は財務。2025年の純利益が70%以上減少し、AI投資の持続可能性に疑義がかかっている。

この3点は偶発的な悪材料ではない。低価格成長戦略の構造的な帰結として読める。Doubao が有料版（¥68/月〜）を発表したのは、無料戦略のままでは費用を賄えなくなった証左だ [INFO-070](../Information/2026-05-06/collected-raw.md#INFO-070)。ただし、このコア判断自体が中国国内情報源に依存している。ByteDance の月次収益も実際のAPI収益構造も、外部から独立して検証できていない。確信度は「中」にとどまる。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Doubao MAU 3.45億・DAU 1.45億、日次トークン120兆超（2年で1000倍） | 中国AI市場での規模優位の直接的な数値根拠。「規模は本物」の判断の柱 | B-2 (中国発表値・独立検証なし) | [INFO-070](../Information/2026-05-06/collected-raw.md#INFO-070) |
| 高 | 2025年純利益70%以上減少（$33B→$9B強）。数百億のAI投資が利益を圧迫 | 低価格・大規模投資戦略の継続可能性を問う財務的制約 | B-2 (非上場のため公式財務開示なし、リーク情報) | [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011) |
| 高 | CAC がアプリ3本（Jianying/Maoxiang/Jimeng AI）にラベリング法違反で警告 | 規制執行の強化が新製品リリース速度とグローバル展開を制約する構造リスク | A-3 | [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011) |
| 中 | Doubao 有料版 ¥68/月〜 を初発表（3段階: 標準/強化/専門）。無料版は継続 | 無料戦略の限界と収益化転換の開始。コスト圧力の顕在化を示す | A-3 | [INFO-070](../Information/2026-05-06/collected-raw.md#INFO-070) |
| 中 | DeepSeek が High-Flyer Capital 支援で低価格を維持。V4 は $0.0036/M | ByteDance の価格優位が同一市場参加者に侵食されている | A-3 | [INFO-068](../Information/2026-05-06/collected-raw.md#INFO-068) |
| 中 | Seed 2.0 正式リリース。Pro/Code モデルを豆包 App と TRAE で提供。API は火山エンジン経由 | 製品ラインナップの拡充がコア判断を支える。ただしベンチマーク自己報告のみ | C-2 (独立検証なし) | [INFO-071](../Information/2026-05-06/collected-raw.md#INFO-071) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 中国規制当局が ByteDance の AI サービスライセンスを取り消す・停止する | H-BTD-001（中国から世界へ）・H-BTD-002（低価格戦略）の両方が崩れる。事業基盤そのものへの打撃 | 60日 | [IND-030](../config/indicators.json) |
| Doubao の MAU 増加が3ヶ月連続で停滞（増加率 ≤ 1%/月） | 「中国市場での独占的規模成長」判断と H-BTD-001 の確度が崩れる。有料化への移行失敗も示唆 | 90日 | [IND-011](../config/indicators.json) |
| DeepSeek が Doubao 有料版と同等以下の価格でコンシューマ向けサービスを展開 | H-BTD-002（低価格優位）の根拠が崩れる。ByteDance の Consumer/API 両市場での価格競争力が失われる | 60日 | [IND-010](../config/indicators.json) |
| 2026年純利益が引き続き減少し、AI投資計画の縮小が公表される | コア判断の財務的根拠が崩れ、規模成長と投資継続の両立が困難と判断する | 180日 | [IND-011](../config/indicators.json) |
| TikTok の米国事業売却・分離が確定し、ByteDance グローバル組織が分断される | TikTok 収益を ByteDance AI 投資に充てるという構造が崩れ、H-BTD-001 の前提が変わる | 90日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文要約 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | 中国で取った規模を足がかりにグローバル展開する | 66% | MAU 3.45億・Seed 2.0 リリースは肯定材料だが、TikTok 問題・CAC 警告で障壁が顕在化。中国情報源の限定により独立裏付けなし | [INFO-070](../Information/2026-05-06/collected-raw.md#INFO-070) [INFO-071](../Information/2026-05-06/collected-raw.md#INFO-071) | [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011) [INFO-068](../Information/2026-05-06/collected-raw.md#INFO-068) |
| [H-BTD-002](../config/hypotheses.json) | 低価格で市場を獲得し続ける | 65% | 日次トークン120兆は低価格戦略の成果を示す。ただし DeepSeek V4 $0.0036/M、純利益急減、有料化開始が同時進行。中国情報源の限定により独立裏付けなし | [INFO-071](../Information/2026-05-06/collected-raw.md#INFO-071) | [INFO-068](../Information/2026-05-06/collected-raw.md#INFO-068) [INFO-070](../Information/2026-05-06/collected-raw.md#INFO-070) |
| [H-BTD-003](../config/hypotheses.json) | 著作権・規制の制約が競争力を削ぐ | 40% | CAC 警告3アプリは規制執行強化の証拠。ただし著作権関連の新証拠はなく、警告はラベリング法違反であり著作権とは別次元。中国情報源の限定により独立裏付けなし | [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011) | (著作権領域での新証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・ベンチマーク動向） | Doubao MAU 3ヶ月停滞またはベンチマーク独立検証で乖離が出た場合に elevated | MAU 3.45億（中国首位）。Seed 2.0 ベンチマーク自己報告のみ | 2026-05-06 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争 | ByteDance vs DeepSeek の価格逆転で high | Seed 2.0 Pro $0.47/$2.37。DeepSeek V4 $0.0036 が下限 | 2026-05-06 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | CAC 追加警告・ライセンス停止・TikTok 分断のいずれかで high | CAC 警告3アプリ [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011) | 2026-05-06 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-06 | コア判断を「規模成長と低価格優位」中心から「優位の持続可能性が試されている」へ | [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011) [INFO-068](../Information/2026-05-06/collected-raw.md#INFO-068) [INFO-070](../Information/2026-05-06/collected-raw.md#INFO-070) CAC警告・DeepSeek High-Flyer支援・Doubao有料化の同時進行 | 「中国首位・低価格で成長継続」 → 「規模は確認済みだが経済モデルが試されている局面」 |
| 2026-04-29 | Doubao MAU 3.45億・車載AI座舱助手2.0・DeepSeek V4価格破壊を反映 | 鮮度タイムアウト対応 | 「MAU規模・価格競争力に注目」 → 「DeepSeek との二軍競合が顕在化」 |
| 2026-04-22 | 2025年純利益70%以上減少・初回株買い戻しを反映 | 財務情報リーク | 「投資継続中」 → 「AI投資コストで収益圧迫が確認」 |

## 7. ブラインドスポット

- **Doubao の月次収益と収益構造が不明**。中国国内アプリは収益公開義務がなく、MAU 3.45億と ¥68/月の有料版があっても、実際の課金転換率・解約率・月次収益は外部から推定不能。「規模はある、収益は不明」という状態で確度を算出している。

- **ByteDance グローバル AI 戦略への中国共産党の介入度が見えない**。TikTok 問題では政府介入が報道されたが、AI 部門（Doubao/Seed）への介入の実態は公開情報にない。介入があれば製品ロードマップや人材配置が変わる。観測手段を持っていない。

- **Seed モデルの学習データに含まれる検閲フィルタの実態が不明**。中国国内で運用されるモデルが何をフィルタしているかは公開されていない。グローバル展開時に同一モデルを使う場合、西側市場での規制適合と中国側フィルタが矛盾する可能性がある。独立した調査は存在しない。

- **米中規制摩擦（CHIPS法・Entity List）でのコンピュート調達制約の実態が不明**。ByteDance が H100 等の高性能 GPU にどこまでアクセスできているかは非公開。国内 GPU（Ascend/Biren）への切り替え進捗も外部から確認できない。ベンチマーク自己報告値が正しくても、学習インフラの持続可能性は別問題として残る。

- **TikTok 米国事業の動向が ByteDance 全体の AI 投資に与える影響が測れない**。TikTok の収益が ByteDance AI 部門の投資原資になっているとされるが、両者のキャッシュフロー分離の実態は外部からわからない。TikTok 分断が AI 投資に直撃するシナリオを定量化できない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-070](../Information/2026-05-06/collected-raw.md#INFO-070) | Doubao 有料版 ¥68/月〜 発表、MAU 3.45億確認 |
| [INFO-071](../Information/2026-05-06/collected-raw.md#INFO-071) | Seed 2.0 正式リリース（Pro/Code）、価格 $0.47/$2.37 |
| [INFO-072](../Information/2026-05-06/collected-raw.md#INFO-072) | Seed3D 2.0、1画像→3Dモデル数秒生成 |
| [INFO-068](../Information/2026-05-06/collected-raw.md#INFO-068) | DeepSeek が High-Flyer Capital 支援で低価格維持 |
| [INFO-011](../Information/2026-05-06/collected-raw.md#INFO-011) | CAC 警告3アプリ（Jianying/Maoxiang/Jimeng AI）、純利益70%+減少 |
| [Arbiter v3.70](../state/arbiter-2026-05-06.md) | 確度評価の完全根拠（本書から外出し） |
