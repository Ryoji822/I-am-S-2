# OpenAI — 企業インテリジェンス

> 最終判断更新: 2026-09-07
> 全体確信度: 中低
> 情報非対称性: 収益申告6系列分裂は公的S-1（10月視野・終端条件2026-10-31）まで保留（KIQ-OAI-001: 収益の直接定量、68R/69R不在）。価格改定ラッシュ（Luna -80%・Terra -20%・GPT-6 Astra $10/$50）の出所はCloudZero第三者ブログ経由でOpenAI公式changelog一次が未引用（Astra日付の9/3 vs 9/6 GA不整合も未解消）。ARC-AGI-3系の交叉確認ガード(A)（他ベンチ家族での独立計測）は不充足で、本日のLLM Stats 0.999も同一ベンチ家族の別計測器である。ゼロデイ2件のCVE/GHSA識別子は5日目未割当。モニタリング可能性データはSystem Card当事者報告・シミュレーション由来。SoftBank $6.5Bコベナントは単一ソース（C-2）。ChatGPT VLOSE指定は本文未取得。
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はOpenAIを「自社定義のAGI到達を宣言しながら、その性能主張が単一ベンチ家族の測定慣行（ARC-AGI-3の標準ハーネス62.7% vs プロバイダアダプタ99.9%）に依存し、価格の2層運用（ボリューム層で切り・プレステージ層を維持）が出所注記付きでしか確定できない企業」と読む。ARC Prize公式フル表（[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063) A-1）が測定慣行依存を一次確定し、本日のLLM Stats 0.999（[INFO-061](../Information/2026-09-07/collected-raw.md#INFO-061) B-2）も同一ベンチ家族内の別計測器だった。評価軸首位も割れており（LLM Stats総合はAstra 60.7首位・AAII v4.2はFable 5.1 57首位）、性能の「単独ブレークスルー」読みには対抗系列がある。AGI宣言のP-2判定は「中-高」、価格2層分化のP-2判定も出所制約から「中-高」である。仮説確度は全件±0%（v4.88）。もしOpenAI公式changelog一次の取得と他ベンチ家族での独立計測が揃えば、性能と価格の両主張は別の土台に立つ。

## 1. コア判断

性能主張の測定慣行依存は一次資料で確定した。ARC Prize公式フル表（[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063) A-1）は、標準ハーネスmax 62.7%（$26,098）対プロバイダアダプタhigh 99.9%（$18,817）という同一モデルの計測器間差と、人間行動効率96%超、full effort別コスト表（max計算がnone計算より安い逆転 $26,098 < $49,791）を開示した。第三者検証注意報（[INFO-045](../Information/2026-09-06/collected-raw.md#INFO-045)・pass@4・ステップ無制限・カスタムハーネス）と重ねると、公表数値の多くは「計測器選択の産物」である。本日のLLM StatsリーダーボードもARC-AGI-3でAstra 0.999・Opus 5 0.302・Sol 0.078を示した（[INFO-061](../Information/2026-09-07/collected-raw.md#INFO-061) B-2）が、同一ベンチ家族内の別計測器であり、交叉確認ガード(A)は不充足のままである。評価軸でも首位が割れる（[INFO-062](../Information/2026-09-07/collected-raw.md#INFO-062) B-2）。Chollet自身は「進歩は予測の約2倍の速さ」と飽和予測を前倒しする一方でベンチマーク間不一致を認めた（[INFO-055](../Information/2026-09-06/collected-raw.md#INFO-055)）。

AGI定義権の行使は継続している。Brockmanの「Welcome to the AGI era」（[INFO-056](../Information/2026-09-06/collected-raw.md#INFO-056) B-1）はOpenAI自身が定義したAGI条件の達成宣言だが、ARC Prizeは「AGIとは主張しない」、LeCunは否認した。本日のダボス対決（[INFO-109](../Information/2026-09-07/collected-raw.md#INFO-109) A-2）でHassabis「AGIには程遠いが5-10年」対Amodei「1年で全開発者の業務代替・5年でホワイトカラー50%消滅」という最大級の乖離が観測され、Anthropic公式はRSIについて「未達・不可避でもない」（[INFO-104](../Information/2026-09-07/collected-raw.md#INFO-104) A-2）と宣言側と逆の位置にいる。定義権が分散するほど「宣言」の情報価値は相対化される。P-2判定は中-高（当事者宣言・未交叉確認）。

価格の2層運用が出所注記付きで観測された。Luna -80%（$0.20/$1.20）とTerra -20%（$2/$12）でボリューム層を切り、GPT-6 Astra $10/$50（fast 2倍・キャッシュ10%・Batch 50%）でプレステージ層を維持する（[INFO-056](../Information/2026-09-07/collected-raw.md#INFO-056) A-2）。ただし出所はCloudZero第三者ブログ経由で、OpenAI公式changelog一次が未引用、Astra日付の9/3 vs 9/6 GA不整合も残る。よってP-2判定は「中-高」に格下げ表現とし、公式一次取得で「高」復帰を事前登録する。観測窓は密集している。銀団3値強制判定は9/9（2日後）、S-1は10月、ゼロデイCVE/GHSA割当は5日目、Astra発売価格3ヶ月系列は2026-12-03完了、ARC-AGI-4は2027-Q1である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | ARC Prize公式フル表: 標準ハーネスmax 62.7%/$26,098 vs プロバイダアダプタhigh 99.9%/$18,817・人間行動効率96%・effort別コスト表（max $26,098 < none $49,791の逆転） | 性能主張の測定慣行依存を一次確定。effort/コスト正規化の一次開示 | A-1 | [INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063) |
| 高 | LLM Stats ARC-AGI-3: Astra 0.999・Opus 5 0.302・Sol 0.078 | 同一ベンチ家族の別計測器。交叉確認ガード(A)不充足の再確認 | B-2 | [INFO-061](../Information/2026-09-07/collected-raw.md#INFO-061) |
| 高 | 評価軸首位分裂: LLM Stats総合Astra 60.7首位 vs AAII v4.2 Fable 5.1 57首位・Vellum GPQA Sonnet 5 96.2%首位 | 「単独ブレークスルー」読みの対抗系列。測定器選択が順位を決める状態 | B-2 | [INFO-062](../Information/2026-09-07/collected-raw.md#INFO-062) |
| 高 | 価格改定: Luna -80%（$0.20/$1.20）・Terra -20%（$2/$12）・GPT-6 Astra $10/$50（fast 2倍・キャッシュ10%・Batch 50%） | 2層分化（P-2中-高）のOpenAI脚。CloudZero経由の出所注記付き | A-2 | [INFO-056](../Information/2026-09-07/collected-raw.md#INFO-056) |
| 高 | GPT-6 Astra公式GA（9/6・段階展開・Terminal-Bench 57.9% vs Sol 37.3%・AA指数61.2対Fable 5.1 65.7を自認） | C-only警告付きのC側材料。自社計測の限界を自認する開示 | A-3 | [INFO-001](../Information/2026-09-06/collected-raw.md#INFO-001) [INFO-003](../Information/2026-09-06/collected-raw.md#INFO-003) |
| 高 | Astra評価中に未知のゼロデイ2件を発見・開発者に開示。「Criticalサイバーしきい値超過」報道。CVE/GHSA識別子は5日目未割当 | IND-013 criticalの主因。Daybreak経由のセーフガード拡大予定 | A-3/B-2 | [INFO-002](../Information/2026-09-06/collected-raw.md#INFO-002) [INFO-014](../Information/2026-09-06/collected-raw.md#INFO-014) |
| 中 | Brockman「Welcome to the AGI era」宣言・ARC Prize留保・LeCun否認・ダボスHassabis vs Amodei最大乖離 | P-2中-高。AGI定義権の分散と宣言の情報価値の相対化 | B-1/A-2 | [INFO-056](../Information/2026-09-06/collected-raw.md#INFO-056) [INFO-109](../Information/2026-09-07/collected-raw.md#INFO-109) |
| 中 | GenAI.mil本文: ChatGPT Mil追加・各最大$200M・IL5 CUI承認 | 政府市場の多社化（独占でない）。収益系列の政府脚 | B-1 | [INFO-065](../Information/2026-09-06/collected-raw.md#INFO-065) |
| 低 | ChatGPT Ads年換算$10億・EHR接続・VLOSE指定（本文未取得） | 収益系列の新脚と規制リスク | A-3/C-1 | [INFO-005](../Information/2026-09-06/collected-raw.md#INFO-005) [INFO-006](../Information/2026-09-06/collected-raw.md#INFO-006) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| OpenAI公式changelog/価格ページの直接取得（出所解消+Astra日付9/3 vs 9/6判別） | 価格2層分化のP-2判定が「中-高」から「高」に復帰する | 次回収集（優先KIQ#4） | [H-OAI-001](../config/hypotheses.json) |
| ゼロデイ2件のCVE/GHSA識別子割当不成立または誤報確認 | IND-013 criticalの主因が解消し、H-OAI-002のC側安全材料になる | 30日 | [IND-013](../config/indicators.json) |
| ARC-AGI-3以外のベンチ家族での独立計測出現 | 交叉確認ガード(A)が充足され、性能主張の別土台が生まれる | 90日 | [IND-025](../config/indicators.json) |
| Astra発売価格3ヶ月系列での値下げ観測 | 「プレステージ層維持」読みが崩れ、SCN-004管理配給判定に直接接続する | 2026-12-03 | [SCN-004](../config/scenarios.json) |
| 銀団3値強制判定 | IND-029第1判定機。債務化の系列確定で資本基盤評価が変わる | 2026-09-09（2日後） | [IND-029](../config/indicators.json) |
| 公的S-1の監査財務 | 収益6系列分裂が解消し、KIQ-OAI-001（68R/69R）が閉じる | 2026-10-31（終端条件） | [IND-030](../config/indicators.json) |
| AGI主張とARC-AGI-4公式結果の整合/不整合 | 定義権行使の中身（実測対応）が判定される | 2027-Q1 | [H-OAI-001](../config/hypotheses.json) |
| VLOSE本文取得・Daybreak配給条件（価格・資格・拒否事例） | 規制リスクとセーフガード実装の実質が判定される | 次回収集/数週間 | [H-OAI-002](../config/hypotheses.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIが「ChatGPTのSuper App化」で収益源を多角化し、API単価下落（Luna -80%・Terra -20%）を広いユーザーベースで回収する | 43% (low) | Luna/Terra値下げとAds $10億・EHRは方向一致。ただし価格改定はCloudZero経由（公式一次未引用）で出所注記、価格2層分化P-2は中-高に据え置き（v4.88±0%） | 公式changelog一次・S-1での収益内訳開示 | API収益の単一依存が監査財務で判明 |
| [H-OAI-002](../config/hypotheses.json) | GPT-6 Astraの性能リードが6-12ヶ月持続する | 44% (low) | ARC Prize公式フル表（A-1）は測定慣行依存を確定させ、交叉確認ガード(A)不充足（本日LLM Stats 0.999も同一ベンチ家族）でC側の独力確認は不能。評価軸首位分裂が対抗系列として健在（v4.88±0%） | 他ベンチ家族での独立計測首位 | 独立計測での首位喪失 |
| [H-OAI-003](../config/hypotheses.json) | OpenAIが政府・軍市場で単独支配を持つ | 3% (low) | GenAI.mil本文（B-1）はChatGPT Mil追加とともにGrok for Government併記・各max $200Mで多社化を確認。単独支配の反証が本文で確定済み（v4.88±0%） | 政府契約の独占的集中の定量 | 追加プラットフォームの政府契約獲得 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | サイバー能力閾値・実被害 | critical解消条件 | critical/rising（v4.88）。Astra Critical指定+ゼロデイ2件（CVE/GHSA 5日目未割当）。Daybreak経由セーフガード拡大予定 | 2026-09-07 |
| [IND-025](../config/indicators.json) | 測定基盤の健全性 | 複数ベンチ家族での独立計測 | elevated/stable（v4.88）。交叉確認ガード(A)不充足の再確認（LLM Stats 0.999は同一ベンチ家族）。台帳訂正（本日INFO-022は9/6計上の再出現）を同期 | 2026-09-07 |
| [IND-026](../config/indicators.json) | 観測不能領域台帳 | 直接定量の出現 | high/rising（v4.88）。収益6系列分裂（KIQ-OAI-001 68R/69R）・価格公式一次不在・VLOSE本文未取得 | 2026-09-07 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度 | 標準化材料の品質と採用 | high/rising（v4.88）。SKILL.md/MCP系はTier-1到達（フォーム観測）。Daybreak配給条件の判別データは未出現 | 2026-09-07 |
| [IND-028](../config/indicators.json) | AGI定義権・予測分裂 | 予測共同体の分裂度 | high/rising（v4.88）。Brockman宣言（宣言側）対Anthropic RSI「未達」・ダボス最大乖離で分裂レンジ拡大 | 2026-09-07 |
| [IND-029](../config/indicators.json) | インフラ債務観測 | 銀団価格・capex下方修正 | high/rising（v4.88）。OpenAI銀団3値強制判定は9/9（2日後）。capex試算大型化（$5.3T/156GW系はB-3） | 2026-09-07 |
| [IND-030](../config/indicators.json) | S-1ゲート・政府介入の状態 | critical解消3基準 | critical/rising（v4.88）。N=1実質34R。S-1観測機は10月視野（終端2026-10-31） | 2026-09-07 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-09-07 | 台帳訂正に伴う全面書き直し。価格改定ラッシュ（Luna -80%・Terra -20%・Astra $10/$50）をCloudZero経由の出所注記付きで計上し、価格2層分化P-2を「中-高」に据え置き（公式一次取得で「高」復帰を事前登録）。LLM Stats 0.999（同一ベンチ家族）と評価軸首位分裂・ダボス最大乖離を新規計上。KIQ-OAI-001カウンターを68R/69Rに更新、CVE/GHSAを5日目に更新。§5全指標をv4.88値に更新 | Arbiter v4.88裁定2(c)/裁定8 + [INFO-056](../Information/2026-09-07/collected-raw.md#INFO-056) | H-OAI-001 43%（±0%）・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |
| 2026-09-06 | §0〜§7書き直し。ARC Prize公式フル表（標準62.7% vs アダプタ99.9%・行動効率96%・effort別コスト表）で性能主張の測定慣行依存を一次確定。Astra GA・System Card・GenAI.mil本文・Critical指定+ゼロデイを新規計上 | [INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063)（A-1） | H-OAI-002 44%（±0%）ほか全件±0% |
| 2026-09-05 | §0〜§7書き直し。Astra事前発表系・管理配給系列（Daybreak）・SoftBankコベナント（C-2単一ソース）を整理 | Astra発表ラッシュ | 全件±0% |
| 2026-09-01 | §0〜§7書き直し。SpaceXによるCursor $60B買収完了（当事者隣接一次）を「its acquisition by SpaceX」として確認 | [Arbiter v4.84](../state/arbiter-2026-09-01.md) | H-OAI-001 43%（±0%） |

## 7. ブラインドスポット

- 価格改定（Luna/Terra/Astra）の定量的錨がCloudZero第三者ブログ一点で、公式changelog・料金ページの一次が取れていない。Astra日付の9/3 vs 9/6不整合の判別も同時に行えていない。
- ARC-AGI-3ファミリー外での独立計測が存在しない。性能リードの評価は計測器選択に強く依存したままである。
- ゼロデイ2件のCVE/GHSA識別子が5日目も未割当で、脆弱性の実在規模（実被害の有無）が判定できない。
- モニタリング回避の測定結果はSystem Card当事者報告・シミュレーション由来で、独立検証がない。
- SoftBank $6.5Bコベナントは単一ソース（C-2）で、銀団3値強制判定（9/9）まで条件の全体像が不明である。
- ChatGPT VLOSE指定は本文未取得で、EU側の規制リスク定量化ができない。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-056](../Information/2026-09-07/collected-raw.md#INFO-056) | Luna -80%・Terra -20%・Astra $10/$50（A-2・CloudZero経由出所注記・台帳訂正2(c)） |
| [INFO-061](../Information/2026-09-07/collected-raw.md#INFO-061) | LLM Stats ARC-AGI-3 0.999（B-2・同一ベンチ家族・交叉確認ガード(A)不充足） |
| [INFO-062](../Information/2026-09-07/collected-raw.md#INFO-062) | 評価軸首位分裂（B-2・LLM Stats vs AAII vs Vellum） |
| [INFO-109](../Information/2026-09-07/collected-raw.md#INFO-109) | ダボスHassabis vs Amodei最大乖離（A-2・IND-028） |
| [INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063) | ARC Prize公式フル表（A-1・標準62.7% vs アダプタ99.9%・effort別コスト表） |
| [INFO-001](../Information/2026-09-06/collected-raw.md#INFO-001) | GPT-6 Astra公開（A-3・Terminal-Bench 57.9%・AA指数61.2自認） |
| [INFO-003](../Information/2026-09-06/collected-raw.md#INFO-003) | Astra価格・提供形態（A-3・$10/$50・ZDR・Astra Pro） |
| [INFO-002](../Information/2026-09-06/collected-raw.md#INFO-002) | ゼロデイ2件発見・開発者開示（A-3・IND-013主因） |
| [INFO-014](../Information/2026-09-06/collected-raw.md#INFO-014) | Critical報道・CVE/GHSA未割当（B-2） |
| [INFO-020](../Information/2026-09-06/collected-raw.md#INFO-020) | System Card・モニタリング回避測定（A-3・当事者報告） |
| [INFO-045](../Information/2026-09-06/collected-raw.md#INFO-045) | 第三者検証注意報（pass@4・ステップ無制限・cache read比較） |
| [INFO-054](../Information/2026-09-06/collected-raw.md#INFO-054) | ARC Prize公式 59.3%/98.4%（xhigh計測） |
| [INFO-055](../Information/2026-09-06/collected-raw.md#INFO-055) | Chollet「予測の約2倍の速さ」・ベンチマーク間不一致（A-2） |
| [INFO-056](../Information/2026-09-06/collected-raw.md#INFO-056) | Brockman「Welcome to the AGI era」（B-1・P-2中-高） |
| [INFO-065](../Information/2026-09-06/collected-raw.md#INFO-065) | GenAI.mil本文（B-1・多社化・各max $200M） |
| [Arbiter v4.88](../state/arbiter-2026-09-07.md) | 台帳訂正4件（うち(c) INFO-056出所注記・P-2中-高）・全19アクティブ仮説±0% |
