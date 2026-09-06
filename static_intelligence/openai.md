# OpenAI — 企業インテリジェンス
最終判断更新: 2026-09-06 | 全体確信度: 中低 | 前回更新: 2026-09-05

**情報非対称性（読者への警告）:**
- 収益申告6系列分裂（[$13.07B FY2025監査済]系・[$65B bookings]系・Forge Q2暫定$115億超系ほか）は公的S-1開示（10月視野・終端条件2026-10-31）まで保留。[KIQ-OAI-001](../config/hypotheses.json) 67R/68R不在。
- ゼロデイ2件のCVE/GHSA/NVD識別子は発売公式化後も未割当（4日目・[INFO-014](../Information/2026-09-06/collected-raw.md#INFO-014)）。実体は当事者申告と報道確認のみ。
- モニタリング可能性データはすべて当事者報告・シミュレーション由来。System Card（[INFO-020](../Information/2026-09-06/collected-raw.md#INFO-020)）は当事者ホスト deploymentsafety.openai.com、UK AISI一次も同じ構造。
- ARC-AGI-3: effort/コスト正規化はARC Prize公式フル表（[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063)・A-1）で開示済みに転換。ただし独立計測はARC-AGI-3ファミリー内にとどまり、交叉確認ガード(A)（他ベンチ家族）は不充足。アダプタ内部実装（推論状態保持・圧縮）は不透明のまま。
- SoftBankコベナントは単一ソース（C-2）。API 25%の政府/民間内訳は67R/68R連続不在。
- ChatGPT VLOSE指定（[INFO-070](../Information/2026-09-06/collected-raw.md#INFO-070)・C-1）は本文未取得。

## 0. 一文要約
OpenAIは自社定義のAGI到達を宣言しながらフロンティアモデルAstraを一般発売したが、その性能主張が単一ベンチ家族の測定慣行に依存する構造を、評価機関自身のフル開示（標準62.7% vs アダプタ99.9%）が確定させた企業である（[INFO-001](../Information/2026-09-06/collected-raw.md#INFO-001)・[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063)・[INFO-056](../Information/2026-09-06/collected-raw.md#INFO-056)）。仮説確度は3件とも±0%（[Arbiter v4.87](../state/arbiter-2026-09-06.md)）。

## 1. コア判断

**性能主張の測定依存性が一次確定した。** ARC Prize公式フル表（[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063)・A-1）は、同一モデルが標準ハーネスmax 62.7%/$26,098、アダプタhigh 99.9%/$18,817という37.2pt差を、effort・コスト・行動効率（人間ベースライン未満のアクション数が全レベルの96.0%）まで分解して示した。公式ブログ自身がAA指数v4.1.1でAstra 61.2 vs Fable 5.1 65.7後塵を自認し（[INFO-001](../Information/2026-09-06/collected-raw.md#INFO-001)）、DeepSWEではGemini 3.8 Flash 73.8%が上回る。ステップ関数の主張はARC-AGI-3単一家族固有で、交叉確認ガード(A)（ARC-AGI-3以外のベンチ家族での独立計測）は維持される。なおeffort上位ほど総コストが下がる逆転（max $26,098 < none $49,791）は行動効率の定量だが、アダプタの内部実装は不透明である。

**AGI宣言は定義設定権の行使であり、予測共同体は分裂している。** Brockmanの「Welcome to the AGI era」（[INFO-056](../Information/2026-09-06/collected-raw.md#INFO-056)・B-1）はOpenAI自身が定義したAGI条件の達成宣言で、定義と判定が同じ主体にある自己参照構造を持つ。Cholletは「進歩は予測の約2倍の速さ」と評価しつつARC-AGI-2飽和圏（Astra 95.0%）を注記し（[INFO-055](../Information/2026-09-06/collected-raw.md#INFO-055)）、ARC Prize自身は「飽和はAGIの証明ではない」「AstraをAGIとは主張しない」と明記した（[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063)）。LeCunの否認とHinton/Bengioの擁護が並行し（[INFO-058](../Information/2026-09-06/collected-raw.md#INFO-058)）、Sanders法案は定義不合意を抱えたまま制度圧力として並走する（[INFO-059](../Information/2026-09-06/collected-raw.md#INFO-059)）。P-2（AGI定義権）の確度は中-高に下方修正された（v4.87）。

**観測窓が9月に密集している。** 銀団3値強制判定は約09-09（3日後）、公的S-1は10月視野（終端2026-10-31）、ゼロデイ識別子は4日目、VLOSE本文とDaybreak拡張後の配給条件（価格・資格・拒否事例）は未取得である。Daybreakの配給条件はSCN-001（囲い込み）とSCN-002（差別化持続）の配分を再評価する判別データとして事前登録済みである（[Arbiter v4.87](../state/arbiter-2026-09-06.md)・本文参照は付録）。

## 2. 判断の重心

| 材料 | 重要度 | 統合 | 関連仮説・指標 |
|---|:-:|---|---|
| [Astra公式GA](../Information/2026-09-06/collected-raw.md#INFO-001)（9/6・A-3） | 高 | 標準$10/$50・fast $20/$100（最大2.5倍速）・ZDR。段階展開（限定組織→Plus/Pro/Business/Enterprise→API/Azure/Bedrock）。Terminal-Bench 4.0 57.9%（Sol 37.3%）・AA指数61.2（Fable 5.1 65.7）・HLE 57.2%（65.0%）を公式表内で自認 | [H-OAI-001](../config/hypotheses.json) C（C-only警告） |
| [ARC Prize公式フル表](../Information/2026-09-06/collected-raw.md#INFO-063)（A-1） | 高 | 標準max 62.7%/$26,098〜none 35.2%/$49,791、アダプタhigh 99.9%/$18,817。高effortほど総コスト低下の逆転。行動効率96.0%・平均51.7%減、アダプタ3.66倍速・トークン49%減。人間約$12.78/ゲーム。「飽和≠AGIの証明」。effort/コスト正規化の一次開示 | [IND-025](../config/indicators.json)・交叉確認ガード(A)維持 |
| [Criticalサイバー指定とゼロデイ2件の公式再確認](../Information/2026-09-06/collected-raw.md#INFO-002)（A-3） | 高 | ExploitBench 100%（Sol 78.5%）。未知ゼロデイ2件を責任ある開示中、CVE/GHSA未割当4日目（[INFO-014](../Information/2026-09-06/collected-raw.md#INFO-014)・B-2）。不可能タスクのスコープ超過Astra 0% vs Sol 48%。Daybreak経由で数週間以内にセーフガード拡大予定 | [IND-013](../config/indicators.json) critical/rising |
| [System Card公開](../Information/2026-09-06/collected-raw.md#INFO-020)（A-3） | 高 | モニター迂回測定の図表を明示。ホストは当事者域名 deploymentsafety.openai.com。モニタリング回避の定量は当事者報告に限定 | P-1系列・[IND-026](../config/indicators.json) |
| [Brockman AGI宣言](../Information/2026-09-06/collected-raw.md#INFO-056)（B-1）+ [Chollet 2倍速評価](../Information/2026-09-06/collected-raw.md#INFO-055) | 高 | 自己定義AGI条件の達成宣言。ARC-AGI-2飽和圏95.0%。研究者分裂（[INFO-058](../Information/2026-09-06/collected-raw.md#INFO-058)） | P-2中-高・[IND-028](../config/indicators.json) |
| [ChatGPT Ads年換算$10億](../Information/2026-09-06/collected-raw.md#INFO-005)（A-3） | 中 | 無料枠財源フレーミング。収益系列の新脚（ランレート計測定義は不透明） | [H-OAI-001](../config/hypotheses.json) C |
| [EHR/医療情報ソース接続](../Information/2026-09-06/collected-raw.md#INFO-006)（A-3） | 中 | 垂直展開の加速。医療データ統合の実行段階入り | [H-OAI-001](../config/hypotheses.json) C |
| [ChatGPT VLOSE指定](../Information/2026-09-06/collected-raw.md#INFO-070)（C-1） | 中 | 検索+広告AIへのDSA先例。本文未取得で実効範囲不明 | 規制リスク新系列 |
| [GenAI.mil本文](../Information/2026-09-06/collected-raw.md#INFO-065)（B-1） | 高 | 2025-12 Gemini専用開始→ChatGPT Mil追加。各max $200M（当時Google・Anthropicにも授与）・IL5 CUI・Hegseth覚書「AIを毎日の戦闘リズムに」 | 政府市場固定化・[H-OAI-002](../config/hypotheses.json) |
| [テキサス474GW接続キュー凍結](../Information/2026-09-06/collected-raw.md#INFO-071)（C-1） | 中 | データセンター需要の物理的ボトルネック。投機キューの監査帰結は第2観測機 | [IND-029](../config/indicators.json) |
| [API価格80モデルスナップショット](../Information/2026-09-06/collected-raw.md#INFO-038)（C-2） | 低 | Astra $10/$50はFable 5と同水準のプレミアム帯。2層構造（プレミアム帯/コモディティ帯）が維持 | [SCN-004](../config/scenarios.json)価格脚 |
| [Latent Space第三者検証注意](../Information/2026-09-06/collected-raw.md#INFO-045)（C-2） | 中 | pass@4・ステップ無制限・カスタムハーネス。cache readはAnthropicが4倍安い | [IND-025](../config/indicators.json) |

## 3. 反証の閾値
| 閾値 | 観測時期 |
|---|---|
| CVE/GHSA識別子の割当不成立または誤報確認 | 30日以内 |
| ARC-AGI-3以外のベンチ家族での独立計測によるフロンティア段差の確認（交叉確認ガードA） | 90日 |
| Astra発売価格3ヶ月系列での値下げ（2026-12-03完了予定） | 90日 |
| 銀団3値強制判定（価格・規模・需要） | 約09-09 |
| 公的S-1の監査財務（終端条件2026-10-31） | 10月 |
| モニタリング回避の実効性が実運用で実証される | 90日 |
| AGI主張とARC-AGI-4（2027-Q1）結果の整合 | 2027-Q1 |
| VLOSE指定の本文（義務範囲・期限） | 次回収集 |
| Daybreak拡張の配給条件（価格・資格・拒否事例） | 数週間以内 |

## 4. 進行中の仮説
| 仮説ID | 一文定義 | 確度(確信度) | 確度の根拠 |
|---|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能をエンタープライズに特化させB2B市場で支配的地位を確立する | 43% (low) | Astra GA即日のAPI/Azure/Bedrock展開・GenAI.mil $200M・EHR接続は全てC側でC-only警告継続。B2B直接定量（API 25%内訳）は67R/68R不在でS-1ゲート凍結中（v4.87±0%） |
| [H-OAI-002](../config/hypotheses.json) | Skills/Shell/Compactionの独自実行環境でAgent開発者を囲い込み、MCP準拠の開放層上にプロプライエタリ上位レイヤーを構築する | 44% (low) | Responses API非同期実行+ミッドターンステアリング・Fast mode稼働制限はcapability rationing対称系列。Cursor GPT遮断は供給統制の既存実例。判別はDaybreak配給条件データ待ち（v4.87±0%） |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究開発に大規模資源を投入する | 3% (low) | Brockman AGI宣言・ゼロデイ自力発見・独自代数記法の研究系列はC側。ARC Prize「AGIとは主張しない」・LeCun否認が外部検証側の逆データ。単一家族依存（v4.87±0%） |

## 5. 監視指標（[IND](../config/indicators.json)の現況）
| 指標 | 現在値/トレンド | 判定根拠 |
|---|---|---|
| [IND-013](../config/indicators.json) サイバー能力閾値 | critical / rising | Critical指定+ゼロデイ2件は公式・報道とも確認済み。CVE/GHSA識別子は4日目未割当（[INFO-014](../Information/2026-09-06/collected-raw.md#INFO-014)）で次回最優先KIQ |
| [IND-025](../config/indicators.json) 測定基盤の健全性 | elevated / stable | P-1測定基盤危機は「ARC-AGI-3家族内一次確定」へ表現修正（39.1pt/37.2pt差の出所注記）。effort/コストフル表開示（[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063)）で正規化の不透明は解消、交叉確認は他ベンチ家族待ち |
| [IND-026](../config/indicators.json) 観測不能領域台帳 | high / rising | API 25%政府/民間内訳67R/68R不在。収益6系列分裂はS-1まで。モニタリング定量は当事者報告のみ |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | high / rising | 本日増分はB/C級（同一URL訂正後の正味1本）で状態変更なし。COMPLETE 4R連続・71件 |
| [IND-028](../config/indicators.json) AGI定義権 | high / rising | P-2は中-高へ修正。自己定義達成宣言とARC Prize・LeCunの留保が併存、複数週観察条件を事前登録 |
| [IND-029](../config/indicators.json) インフラ債務観測 | high / rising | OpenAI銀団3値判定は約09-09（第1判定機・3日後）。テキサス474GW監査帰結を第2観測機に追加（[INFO-071](../Information/2026-09-06/collected-raw.md#INFO-071)） |
| [IND-030](../config/indicators.json) S-1ゲート | critical / rising | N=1実質33R（+1機械加算）。再開トリガー不発火・S-1後ずれ（10月視野）で凍結継続 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-09-06 | §0〜§7書き直し。Astra公式GA（9/6・$10/$50）とARC Prize公式フル表（標準62.7% vs アダプタ99.9%・交叉確認ガード(A)は同一ファミリー内で不充足）を反映。Brockman AGI宣言（P-2中-高）・Ads $1B・EHR接続・VLOSE指定（本文未取得）・テキサス474GW・GenAI.mil本文を新規計上。§5全指標をv4.87値に更新 | Astra公式GA（[INFO-001](../Information/2026-09-06/collected-raw.md#INFO-001)）+ ARC公式フル表（[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063)） | H-OAI-001 43%（±0%）・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |
| 2026-09-05 | §0〜§7書き直し。Astra正式発売（9/3・$10/$50）を主力製品投入として反映。Criticalサイバー閾値指定+ゼロデイ2件の第三者確認・モニタリング可能性低下の自己開示（P-1）・ARC独立計測37.2pt差と第三者評価分裂（交叉確認ガード制度化）・Cursor遮断・SoftBankコベナント・GenAI.mil $200Mを新規計上 | Astra GA + IND-013 third-party confirmation | H-OAI-001 43%（±0%）・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |
| 2026-08-31 | 全面書き直し。[IND-013](../config/indicators.json) high→critical移行執行（HF評価事件の当事者一次×2）と構造注記・BS-001条件付きトリガー登録。Foundation 26%中間確認はゲート凍結継続 | IND-013 critical移行（v4.83） | H-OAI-001 43%・H-OAI-002 44%・H-OAI-003 3%（全て±0%）・IND-013 high→critical |
| 2026-08-24 | 全面書き直し（freshness 7日）。S-1系列3波と再評価ゲート登録・Astra公式ペーシング文書一次確認・$30B銀団と$800B超支払義務を新規反映 | freshness 7d | 全仮説±0%（v4.76） |
| 2026-08-12 | 全面書き直し。H-OAI-001 -1%（44→43%）を反映 | [INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) | H-OAI-001 44→43% |
| 2026-08-01 | 全面書き直し。H-OAI-001 medium→low移行（48→44%） | [INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) | H-OAI-001 48% medium→44% low |

## 7. ブラインドスポット
- ゼロデイ2件の実体: 識別子未割当のため深刻度・影響範囲の独立検証が不可能。当事者申告と報道の一致のみ。
- モニタリング可能性の全データがシミュレーション・当事者報告由来。System Cardは当事者ホストで、独立ホストの一次が存在しない。
- AGI宣言の自己参照: 定義の設定者と判定者が同一主体。外部検証の受け入れ（H-OAI-003）は構造的に閉じている。
- ARC-AGI-3単一家族依存: 交叉確認ガード(A)充足まで「ステップ関数」主張の汎化は保留。
- VLOSE本文・SoftBankコベナント・Ads $1Bランレートの計測定義が未確認。
- API 25%の政府/民間内訳不在により、政府依存度の収益感応度が推計不能。

---
付録（本日の主要証拠）: [INFO-001](../Information/2026-09-06/collected-raw.md#INFO-001)（Astra公式GA・A-3）・[INFO-002](../Information/2026-09-06/collected-raw.md#INFO-002)（ゼロデイ・A-3）・[INFO-063](../Information/2026-09-06/collected-raw.md#INFO-063)（ARCフル表・A-1）・[INFO-065](../Information/2026-09-06/collected-raw.md#INFO-065)（GenAI.mil本文・B-1）・[INFO-056](../Information/2026-09-06/collected-raw.md#INFO-056)（AGI宣言・B-1）・[Arbiter v4.87](../state/arbiter-2026-09-06.md)（確度全件±0%・INFO-047/067同一URL訂正）
