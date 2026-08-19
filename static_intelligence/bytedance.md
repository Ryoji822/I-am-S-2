# ByteDance

> 最終判断更新: 2026-08-19
> 全体確信度: 中
> 情報非対称性: 収益・コストの内部数値は外部検証不可能。豆包DAUは同一出所（晚点LatePost系）内で6月「2億超」から8月系「1.78億」への減少方向の時系列が出現したが、測定定義の同等性は未確認（[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) C-2）。DAU表記は1.4億（別集計）や50M超（英語圏報道）とも併存（[INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) B-2、[INFO-135](../Information/2026-08-17/collected-raw.md#INFO-135)）。MAUも3.45億（QuestMobile 2026年Q1）・3.82億・5.28億（同6月報道）と分裂。$200億銀団への$30B超申込はBloomberg報道だが価格条件は未開示（[INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) B-1）。非上場・外部監査なし・中国情報源限定の構造は不変。中国AIコンパニオン規制が7/15に発効し機能制限の実害報道が出現（[INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) B-2）。
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-010](../config/indicators.json) [IND-011](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はByteDanceを「億級DAUの消費者規模とその貨幣化不在が同時に観測され、返済義務付き債務でAI投資原資を調達する段階に入った企業」と読んでいる。豆包DAU 1.78億（8月系測定）に対して有料ユーザーは数十万、日次の算力コスト数千万元に対して日収は百万元未満である（[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) C-2）。AI内取引への佣金徴収（最高18%・8/10発効・[INFO-121](../Information/2026-08-19/collected-raw.md#INFO-121)）がこの乖離への最初の体系的回答である。

[H-BTD-002](../config/hypotheses.json)は32% low（-1%・v4.71）。同一出所系列内で6月2億超から8月系1.78億（約11%減）の時系列が出現し、v4.69が設定した判別条件（測定時期特定）が充足された。減少シグナルにのみ独立ソースを要求し、ベースライン（2億超）を無検験のまま分母にする非対称な証拠基準が是正され、判別候補第2弾として反証計上された。ベースライン側にも無検験・激励文脈由来の注記が同格で付与されている。独立ソース（QuestMobile月次等）出現時の追加加重は別枠で事前登録済みである。

$30B超の銀団申込（8/19がコミット期限・Citi/JPMorgan主幹事）はAI投資の拡大原資だが、返済義務付き債務への依存は内部キャッシュ生成不在の帰結であって内部で閉じる増幅ループの側には立たない。[H-BTD-001](../config/hypotheses.json)は64% medium（±0%）で、この負債側注記付きで計上された。

## 1. コア判断

全体確信度は中。ByteDanceの現在位置は「消費者AIの規模優位を企業インフラの収益化に転換する組織的基盤を構築中」という読みを維持するが、今回の更新でその読みに2つの修正が入った。第一に消費者規模の指標（DAU）が同一出所系列内で初めて減少方向の時系列を持ったこと、第二にAI投資の原資が内部キャッシュではなく債務に依存していることが明示されたことである。

### H-BTD-002 32%: 判別条件の充足と非対称証拠基準の是正

[H-BTD-002](../config/hypotheses.json)は32% low（-1%・v4.71、前回更新時の34%から2段階）。08-17（v4.69）はDAU表記の分裂（2億超 vs 1.4億・[INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126)）を反証の蓄積として34%から33%へ引き下げた。本ラウンドで[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118)（C-2）が1.78億の出典を晚点LatePost系の8月報道と特定し、同一出所系列内の時系列（6月2億超から約11%減）が出現したため、v4.69の判別条件（測定時期特定）が充足された。Arbiterは減少シグナルにのみ独立ソースを要求しベースラインを無検験のまま扱う非対称な証拠基準を是正し、反証3件（全仮説最多）の蓄積を加重して33%から32%とした。同時にベースラインの2億超にも無検験・激励文脈由来（社内激励の逆説的表現の可能性）の注記を同格で付与した。独立ソースによる裏付けが出た場合の追加加重（-1〜2%）は別枠で事前登録されており、測定定義の同等性確認が次ラウンドの最優先である。10兆パラメータ訓練中・$230億AIインフラ投資計画（[INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) B-2）は「並行」（インフラ投資の同時拡大）の側を支えるが、「相乗的」（技術競争力の解消）の解消には不確実性が残る。CEO梁汝波の「大LLM格差拡大」自認（[INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) B-2）が技術競争力軸の反証として継続する。

### 貨幣化の乖離と抽傭18%

豆包の貨幣化の乖離が定量で裏付けられた。1.78億DAUに対して有料ユーザーは数十万（付费版開始から1ヶ月余り）で、月額500元の最上位プランは人気がない。毎日の算力コストは数千万元、日収は百万元未満、6月の日次EC取引額は約1,000万元にとどまる（[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) C-2、[INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) B-2）。ユーザー獲得コストは1DAUあたりRMB85-113との別系統もある（[INFO-135](../Information/2026-08-17/collected-raw.md#INFO-135)）。これに対する最初の体系的回答がAI内取引への佣金徴収で、最高18%（ホテル注文では12%との報道）が8/10 0時に発効した（[INFO-121](../Information/2026-08-19/collected-raw.md#INFO-121) C-2、[INFO-127](../Information/2026-08-17/collected-raw.md#INFO-127) B-2）。AI検索経由の取引を最適化するGEO（生成エンジン最適化）産業が即時に形成され、携程等を経由する迂回も観測されている。実効性の判定は8月中旬〜下旬のGMV・リピートデータ（4-6週後）を待つ。

### 債務駆動のAI投資: $30B超の銀団申込

ByteDanceが調達中の$20B想定オフショア銀団貸付に$30B超の銀行コミットを獲得した（Citi・JPMorgan主幹事、参加銀行のコミット期限は8/19、期間3年+最大2年延長、境外調達として社内最大）。目的はAI投資の加速である（[INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) B-1）。Arbiter v4.71はこの計上に負債側の注記を付けた。返済義務付き債務への依存は、内部キャッシュ生成の不在（日収百万元未満 vs 算力費数千万元/日）の帰結であって、内部で閉じる増幅ループ（「相乗的」の認定基準）の側証拠として併記されるべき片側帳簿だったという是正である。シナリオ側ではSCN-BS-003の材料が「規模材料／ユーフォリア材料」に区分され、$20B枠への$30B超（1.5倍超）の申込は信用市場の深度、すなわち当面の金融条件が緩いことの観測とされ、発火トリガー（信用収縮）側の逆方向証拠として処理された。銀団組成確定報道の価格条件（スプレッド・コベナント・割当）がAI信用リスクの直接の市場価格として監視に追加されている。

### DAU減少の規制実害仮説とH-BTD-001/003

中国のAIコンパニオン規制が7/15に発効し、感情操作コンテンツの生成禁止で利用者が「サービス消失」に直面したとの実害報道が出た（[INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) B-2）。豆包と千問が擬人エージェント機能を停止したとの速報もある（[INFO-136](../Information/2026-08-17/collected-raw.md#INFO-136) C-3）。2億超から1.78億への減少が競争力低下によるものか規制による機能制限によるものかの判別が次ラウンドの焦点で、規制実害仮説が成立すれば減少の解釈は変わり、[H-BTD-002](../config/hypotheses.json)の加重条件も変わる。[H-BTD-003](../config/hypotheses.json)は40% medium（±0%）で、規制インフラの蓄積は続くが核心命題（著作権問題によるグローバル展開の制限）への新規A-2以上の証拠は不在のまま。[H-BTD-001](../config/hypotheses.json)は64% medium（±0%）。Seedance 2.0が業界初の4モダリティ同時入力（画像・動画・音声・テキスト）に対応し豆包へ無料全面搭載、後継のSeedance 2.5も登場、MPA（米映画協会）とIP利用制限で合意済みとの報道がある（[INFO-120](../Information/2026-08-19/collected-raw.md#INFO-120) C-2・自家測定系）。無料搭載によるコスト吸収戦略は貨幣化の乖離と表裏である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 豆包DAU 1.78億（晚点LatePost系・8月測定）。同一出所系列内で6月「2億超」から約11%減 | [H-BTD-002](../config/hypotheses.json) 判別条件（測定時期特定）充足・反証3件目。減少方向の初の系列内時系列。測定定義の同等性は未確認 | C-2 | [INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) |
| 高 | 貨幣化の乖離: 有料ユーザー数十万・日次コスト数千万元 vs 日収百万元未満・月額500元プラン不人気・6月の日次EC取引約1,000万元 | 消費者規模と収益の構造的乖離。[IND-010](../config/indicators.json) highの根拠。抽傭の前提条件 | C-2/B-2 | [INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) [INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) |
| 高 | $20B想定銀団に$30B超の申込（Citi/JPMorgan主幹事・8/19コミット期限・3年+2年延長・境外調達として社内最大） | [H-BTD-001](../config/hypotheses.json)/[H-BTD-002](../config/hypotheses.json) の拡大原資。ただし返済義務付き債務で内部増幅ループの側には立たない（負債側注記）。[IND-029](../config/indicators.json) | B-1 | [INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) |
| 高 | AI内取引への佣金徴収（最高18%・ホテル注文12%との報道）が8/10 0時に発効。GEO（生成エンジン最適化）産業が即時発生・携程経由の迂回も | 億級DAU収益化の中核施策。実効性は4-6週後のGMV・リピートで判定。[IND-010](../config/indicators.json) | C-2/B-2 | [INFO-121](../Information/2026-08-19/collected-raw.md#INFO-121) [INFO-127](../Information/2026-08-17/collected-raw.md#INFO-127) |
| 高 | MAU 3.45億（国内C端AI首位・2位〜5位合計に相当）・日均180兆トークン消費・PC端5,104万で6位 | [H-BTD-001](../config/hypotheses.json) 規模優位の定量。DAU表記の分裂（2億超/1.4億/50M超）は定義検証待ち | B-2 | [INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) [INFO-135](../Information/2026-08-17/collected-raw.md#INFO-135) |
| 高 | CEO梁汝波年次全員会: 大LLM格差拡大の自認・自研堅持・短期的劣位受容 | [H-BTD-002](../config/hypotheses.json) 技術競争力軸の反証（前回計上・継続）。中国語一次ソースの検証が条件付き | B-2 | [INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) |
| 中 | 中国AIコンパニオン規制7/15発効: 感情操作禁止で「サービス消失」の実害報道。豆包・千問の擬人機能停止との速報 | DAU減少の規制実害仮説を支持。[H-BTD-003](../config/hypotheses.json) 規制インフラの蓄積。判別が次ラウンドの焦点 | B-2/C-3 | [INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) [INFO-136](../Information/2026-08-17/collected-raw.md#INFO-136) |
| 中 | Seedance 2.0: 業界初の4モダリティ同時入力・豆包への無料全面搭載・Seedance 2.5登場・MPAとIP制限合意 | [H-BTD-001](../config/hypotheses.json) 製品力の維持（自家測定系で独立検証なし）。無料戦略はコスト吸収の継続 | C-2 | [INFO-120](../Information/2026-08-19/collected-raw.md#INFO-120) |
| 中 | ByteDance 2025年売上$186B・純利益$48B | [H-BTD-001](../config/hypotheses.json) クロス補填の財務基盤。債務調達選択との対比で内部資金配分の解釈が未確定 | B-2 | [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| QuestMobile等の独立ソースによる8月以降のDAU測定が出現する | 事前登録済みの追加加重（-1〜2%）が発火し、[H-BTD-002](../config/hypotheses.json) の系列内時系列の解釈が確定する | 次回 | [IND-011](../config/indicators.json) |
| DAUが3ヶ月連続で1億を下回る | [H-BTD-002](../config/hypotheses.json) の消費者軸が崩れ、相乗的拡大フレームの再評価が必要になる | 90日 | [IND-011](../config/indicators.json) |
| 晚点系Appログ推計の測定定義が一次確認される | 1.78億と2億超の系列の同等性が判定され、約11%減の解釈（実減か定義差か）が確定する | 次回 | [IND-011](../config/indicators.json) |
| 銀団組成の確定報道で価格条件（スプレッド・コベナント・割当）が開示される | AI信用リスクの直接の市場価格が観測され、[IND-029](../config/indicators.json) とSCN-BS-003の材料区分が再検討される | 30日 | [IND-029](../config/indicators.json) |
| 抽傭18%のGMV・リピート率が4-6週データで確認される | 貨幣化転換の実効性が判定され、[IND-010](../config/indicators.json) の赤字構造評価が変わる | 60日 | [IND-010](../config/indicators.json) |
| 企業Token経済（火山方舟・Coze）の成長が停止する | [H-BTD-002](../config/hypotheses.json) の企業軸と8/1組織再編の効果が崩れる | 90日 | [IND-010](../config/indicators.json) |
| 中国の海外AIモデルアクセス制限が実施されオープンソース配布が停止される | [H-BTD-001](../config/hypotheses.json) のグローバル展開前提が崩壊し、確度を大幅に下方修正する | 90日 | [IND-011](../config/indicators.json) |
| 著作権関連の新規A-2以上の証拠が出現する | [H-BTD-003](../config/hypotheses.json) の核心命題が初めて直接検証される | 90日 | [H-BTD-003](../config/hypotheses.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持し、グローバル展開を図る | 64% medium | ±0%（v4.71）。$30B超銀団申込（[INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) B-1）を拡大原資として計上したが、返済義務付き債務への依存は内部キャッシュ生成不在（日収百万元未満 vs 算力費数千万元/日）の帰結で、内部で閉じる増幅ループの側には立たないという負債側注記付き。MAU 3.45億（[INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126)）・Seedance 2.0の4モダリティ入力（[INFO-120](../Information/2026-08-19/collected-raw.md#INFO-120)）・Tesla中国での豆包AI音声配信（[INFO-092](../Information/2026-08-07/collected-raw.md#INFO-092)）・2025年売上$186B（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060)）で規模・製品力は維持。海外アクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）が障壁で、MAU/DAU測定の分裂で絶対値の確定は不可 | [INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) [INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) [INFO-120](../Information/2026-08-19/collected-raw.md#INFO-120) [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084)・MAU/DAU測定の分裂 |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは消費者基盤と企業インフラの相乗的並行拡大を展開している。8月1日組織再編が消費者AI・企業コラボ・クラウドインフラの組織的融合を制度化 | 32% low | -1%（v4.71。前回更新時34%から08-17の34→33%、本ラウンドの33→32%の2段階を反映）。[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118)で同一出所系列内時系列（6月2億超→8月系1.78億・約11%減）が出現しv4.69判別条件が充足。反証3件は全仮説最多で、非対称証拠基準（減少シグナルのみ独立ソース要求）を是正して加重。ベースライン2億超にも無検験・激励文脈由来の注記を同格付与。独立ソース出現時の追加加重（-1〜2%）は別枠事前登録。10兆パラメータ・$230億投資（[INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012)）と$30B超銀団（[INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119)）は「並行」の側だが「相乗的」の解消には不確実性が残る | [INFO-092](../Information/2026-08-07/collected-raw.md#INFO-092) [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) [INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) [INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) | [INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) [INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) [INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受け、グローバル展開が制限される | 40% medium | ±0%（v4.71）。中国コンパニオン規制7/15発効の実害報道（[INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) B-2）・擬人機能停止の速報（[INFO-136](../Information/2026-08-17/collected-raw.md#INFO-136) C-3）・FCC中国製ロボット輸入禁止（[INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042)）で規制インフラは蓄積するが、核心命題（著作権）への新規A-2以上の証拠は不在 | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) [INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) | (著作権領域の新規A-2+証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・日コスト赤字拡大でhigh | high。日次売上百万元未満 vs 日次算力コスト数千万元（[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) C-2・[INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) B-2）・獲得コストRMB85-113/DAU（[INFO-135](../Information/2026-08-17/collected-raw.md#INFO-135)）。AI取引佣金最高18%が8/10に発効しGEO産業が発生（[INFO-121](../Information/2026-08-19/collected-raw.md#INFO-121)）。8/1組織再編でToB統合発効（[INFO-092](../Information/2026-08-07/collected-raw.md#INFO-092)）・Coze企業展開20件超（[INFO-093](../Information/2026-08-07/collected-raw.md#INFO-093)）・$230億AIインフラ投資計画（[INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012)）。GMV・リピートの4-6週データが次の判定材料 | 2026-08-19 |
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | elevated。豆包DAU 1.78億（晚点系8月測定・同一出所系列内で6月2億超から約11%減・[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118)）。DAU表記は1.4億（別集計）・50M超（英語圏）と併存（[INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126)）。MAU 3.45億（QuestMobile 26Q1・2位〜5位合計に相当）で3.82億/5.28億（6月）との分裂が未解消。Seedance 2.0の4モダリティ入力・豆包無料搭載（[INFO-120](../Information/2026-08-19/collected-raw.md#INFO-120)）。規制実害仮説（[INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043)）との判別が焦点。独立裏付けなし | 2026-08-19 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | high/rising（v4.71）。債務駆動インフラの米中同時制度化。ByteDance $30B超銀団申込（[INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) B-1）は規模材料／ユーフォリア材料に区分され、発火トリガー（信用収縮）側の逆方向。2025年売上$186B・純利益$48B（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060)）・$230億AIインフラ投資計画（[INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012)）。銀団価格条件（スプレッド・コベナント・割当）の監視を追加。中間閾値（CDS約7%<10%等）未充足 | 2026-08-19 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | critical/rising。中国AIコンパニオン規制7/15発効・感情操作禁止・実害報道（[INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) B-2）・豆包・千問の擬人機能停止速報（[INFO-136](../Information/2026-08-17/collected-raw.md#INFO-136) C-3）。EU AI Act執行開始（[INFO-035](../Information/2026-08-07/collected-raw.md#INFO-035) A-2）。海外AIモデルアクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）。米側はPax Silica協定で陣営化が加速（[INFO-113](../Information/2026-08-19/collected-raw.md#INFO-113) B-1） | 2026-08-19 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-08-19 | 全面書き直し（7日freshness timeoutと判別条件充足）。H-BTD-002 -2%を反映（34→32%: 08-17はDAU表記分裂の反証蓄積、本ラウンドは[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118)で同一出所系列内時系列が出現し判別条件が充足・非対称証拠基準の是正・反証3件で全仮説最多）。貨幣化の乖離定量（有料数十万・日次コスト数千万元 vs 日収百万元未満）・AI取引佣金最高18%の8/10発効・$30B超銀団申込（負債側注記付き）・Seedance 2.0/2.5・中国コンパニオン規制の実害報道を新規反映。全4指標last_checked更新 | Arbiter v4.69/v4.71・[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) [INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) [INFO-121](../Information/2026-08-19/collected-raw.md#INFO-121) | H-BTD-001 64%（±0%）・H-BTD-002 34→32%・H-BTD-003 40%（±0%） |
| 2026-08-12 | ターゲット編集。H-BTD-002 -1%（35→34%・CEO梁汝波「大LLM格差拡大」自認=技術競争力軸初のI証拠・AND条件「相乗的」否定・ミラー・イメージング是正・Red反証強度「中-強」採用・v4.64強制再評価メカニズム）を反映。CEO年次全員会([INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) B-2)・10兆パラメータモデル訓練/$230億投資([INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) B-2)・OpenRouter三極体制収束を新規反映。全4指標last_checked更新。Arbiter v4.64 COMPLETE | Arbiter v4.64・[INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) [INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) | H-BTD-001 64%（±0%）・H-BTD-002 35→34%・H-BTD-003 40%（±0%） |
| 2026-08-09 | ターゲット編集。H-BTD-002 -1%（36→35%・Red反証強度「中-強」採用・張一鳴宣言検証不可能性・可霊AI二重性・I=0人工性・財務/TikTokリスク評価不在）を反映。全4指標last_checked更新。Arbiter v4.61 COMPLETE | Arbiter v4.61 | H-BTD-001 64%（±0%）・H-BTD-002 36→35%・H-BTD-003 40%（±0%） |
| 2026-08-07 | 鮮度タイムアウト更新（7日経過）。Tesla中国での豆包AI音声配信・Seedance 2.5 SeedRealtime統合モデル・8月1日組織再編発効・MAU/CAPEXソース間乖離の明示を追加。Arbiter v4.59のH-BTD-002 3条件（I=0人工性・中国語ソース品質・TikTok損失矛盾）を§4に反映。仮説確度は全件±0%据え置き | [INFO-092](../Information/2026-08-07/collected-raw.md#INFO-092) [INFO-091](../Information/2026-08-07/collected-raw.md#INFO-091) [INFO-094](../Information/2026-08-07/collected-raw.md#INFO-094) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-31 | 構造的変化反映。7/30組織再編（豆包・飛書・火山エンジン統合）を新規反映。中国3社エージェントマーケットプレイス削除・ByteDance維持・FCC中国製ロボット輸入禁止を追加 | [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-30 | 豆包MAU 5.28億・過去最高・$700億AI投資計画・DAU差異技術的説明初確認 | [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-28 | Seed 2.0 Code 256K・豆包MAU 3.82億/+172% YoYのA-1品質確認 | [INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) | H-BTD-002 37→36% |
| 2026-07-23 | H-BTD-002ステートメント修正: 「移行過程」→「相乗的並行拡大」。$186B売上・豆包DAU 2億/日次赤字・Seed Audio 1.0を新規反映 | [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) | H-BTD-002 38→37% |

## 7. ブラインドスポット

- DAU系列が同一出所（晚点LatePost系のAppログ推計）に依存している。6月「2億超」と8月系「1.78億」の測定定義の同等性は未確認で、約11%減が実減か集計時点差かの判別ができない。ベースラインの2億超も無検験で、年次全員会の激励文脈で誇張された値である可能性が同格で付与された。独立ソース（QuestMobile月次等）が出ない限り、この時系列の解釈は確定しない。
- MAUの3系統の分裂（3.45億・3.82億・5.28億）が未解消である。測定対象・定義・時期の技術的差異か誤報かを外部から判別できず、国家統計基準準拠の影響可能性が数値の絶対的信用度を構造的に制約する。
- $30B超の銀団申込は当座の金融条件が緩いことの観測であって、投資の持続性の証明ではない。価格条件（スプレッド・コベナント・割当）が開示されるまで、この債務のコストと制約は不明である。規模の大きさ自体をユーフォリア材料と混同する評価の誤りをv4.71が是正したばかりである。
- 抽傭18%の実効性は未知数である。GEO最適化による取引誘導と、携程等を経由する迂回の減殺効果が相殺し合う可能性があり、4-6週後のGMV・リピートデータまで判定材料がない。
- DAU減少の原因帰属（競争力低下か7/15規制による機能制限か）が判別不能である。規制実害仮説が成立すれば減少は[H-BTD-002](../config/hypotheses.json)の技術競争力軸の反証としての重量を失う。擬人機能停止の速報（C-3）は規制主体・条文が未確認である。
- 投資計画のソース間乖離（$230億・$280億・$700億）が未解決のまま桁が揃っていない。計画値と実行の時間差もあり、鵜呑みは危険である。
- ミラーイメージングのリスクが残る。西側の「赤字=持続不能」という財務基準を、広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめるとモデルの優位を見落とす可能性があり、逆に過大に考慮すると赤字の実相を過小評価する。判別手段がない。
- Seedance 2.0/2.5の能力はByteDance自家測定・API仕様ベースで、独立ベンチマークでの検証が未完了である。MPAとのIP合意の内容（適用範囲・執行メカニズム）も詳細不明で、[H-BTD-003](../config/hypotheses.json)の著作権軸への影響評価には一次文書が要る。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) | 豆包DAU 1.78億の出典特定（晚点系8月報道）・同一出所系列内で6月2億超から約11%減・貨幣化乖離の定量（有料数十万・日次コスト数千万元 vs 日収百万元未満）(C-2) |
| [INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) | $20B想定銀団に$30B超申込・Citi/JPMorgan主幹事・8/19コミット期限・AI投資原資・負債側注記の対象(Bloomberg・B-1) |
| [INFO-120](../Information/2026-08-19/collected-raw.md#INFO-120) | Seedance 2.0: 4モダリティ同時入力（業界初）・豆包無料全面搭載・Seedance 2.5・MPAとIP制限合意(C-2) |
| [INFO-121](../Information/2026-08-19/collected-raw.md#INFO-121) | AI取引佣金最高18%が8/10発効・GEO（生成エンジン最適化）産業の即時発生・携程経由の迂回(C-2) |
| [INFO-113](../Information/2026-08-19/collected-raw.md#INFO-113) | 米国の「Pax Silica」協定: 同盟国に側の選択を要求・輸出管理と共同プロジェクトへ誘導(Reuters 8/14・B-1) |
| [INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) | 豆包MAU 3.45億・DAU表記の分裂（2億超/1.4億）・日均180兆トークン・算力コスト数千万元/日・6月の日次EC約1,000万元(B-2) |
| [INFO-127](../Information/2026-08-17/collected-raw.md#INFO-127) | ホテル注文で12%抽佣を8/10に開始・AIアシスタント初の本格取引課金(B-2) |
| [INFO-135](../Information/2026-08-17/collected-raw.md#INFO-135) | DAU表記の分裂（50M超英語圏 vs 140M-200M超中国側）・獲得コストRMB85-113/DAU・DeepSeek 163M MAU |
| [INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) | 中国AIコンパニオン規制7/15発効・感情操作禁止・「サービス消失」の実害報道(B-2) |
| [INFO-136](../Information/2026-08-17/collected-raw.md#INFO-136) | 中国新規制で豆包・千問が擬人エージェント機能を停止との速報・規制主体・条文は要確認(C-3) |
| [INFO-146](../Information/2026-08-17/collected-raw.md#INFO-146) | Anthropic Q2暫定開示（横断参照・対比文脈）(B-2) |
| [INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) | CEO梁汝波年次全員会: 大LLM格差拡大自認・自研堅持・短期的劣位受容・OpenRouter三極体制(B-2) |
| [INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) | 10兆パラメータモデル訓練中・$230億AIインフラ投資・Cozeオープンソース版(B-2) |
| [INFO-092](../Information/2026-08-07/collected-raw.md#INFO-092) | 豆包MAU 3.82億・DAU 1.78億（QuestMobile Jun 2026）・8月1日組織再編発効・Tesla中国豆包AI音声配信・CAPEX伝聞2000億人民元 |
| [INFO-091](../Information/2026-08-07/collected-raw.md#INFO-091) | Seedance 2.5ワンテイク30秒動画生成・SeedRealtime音動画全二重統一モデル |
| [INFO-094](../Information/2026-08-07/collected-raw.md#INFO-094) | CEO梁汝波が自主モデル研発堅持・競合AI蒸留否定・DeepSeek第2ラウンド500億人民元目標 |
| [INFO-093](../Information/2026-08-07/collected-raw.md#INFO-093) | CozeゼロコードAIエージェントプラットフォーム・企業展開20件超・中国第7位 |
| [INFO-037](../Information/2026-08-07/collected-raw.md#INFO-037) | 中国AIコンパニオン規則（世界初・4月10日執行）・AIコンテンツラベル義務化・AI倫理審査 |
| [INFO-035](../Information/2026-08-07/collected-raw.md#INFO-035) | EU AI Act執行開始（8月2日・最高€15Mまたは3%売上の罰金） |
| [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) | 7/30組織再編: 豆包・飛書・火山エンジン統合・新設「創造力サービスプラットフォーム部」(A-2) |
| [INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) | FCC: 中国製ヒューマノイド・四足ロボット新規輸入禁止(B-2) |
| [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) | 豆包MAU 5.28億・2026年6月過去最高・DAUピーク1.45億 vs 持続的~8000万(A-2) |
| [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) | ByteDance最大$700億AIインフラ投資計画2026(A-2) |
| [INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) | Seed 2.0 Code 256Kコンテキスト・Seedance 2.0(A-1) |
| [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) | ByteDance 2025年売上$186B・純利益$48B・張一鳴中国首富(B-2) |
| [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) | 豆包DAU 2億・日次売上<100万元・毎日数千万元損失(B-2) |
| [Arbiter v4.69](../state/arbiter-2026-08-17.md) | H-BTD-002 34→33%・DAU判別条件（測定時期特定）の設定・豆包DAU出典確認を最優先に |
| [Arbiter v4.71](../state/arbiter-2026-08-19.md) | H-BTD-002 33→32%（判別条件充足・非対称証拠基準是正・ベースライン注記の同格付与）・INFO-119負債側注記・材料区分 |
