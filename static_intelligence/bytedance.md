# ByteDance

> 最終判断更新: 2026-07-10
> 全体確信度: 中
> 情報非対称性: 中国市場の透明性低・言論統制により、観測根拠は他社比で著しく限定的。豆包MAUに複数ソース間で乖離（3.45億・3.3億・1.47億）があり、定義・時期・方法論の差の判別が不能。日コスト「1.3〜2.4億元」は36kr等の報道に基づくが、火山引擎API価格からの推算であり実際の限界コストを過大評価する可能性。Seed 2.1のコーディング能力Claude Opus 4.7匹敵はByteDance自家測定であり独立ベンチマークでの検証が未完了。中国情報源の限定により独立裏付けなし
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-010](../config/indicators.json) [IND-011](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

中国が最先端AIモデルへの海外アクセス制限をAlibaba・ByteDance・Z.aiと協議中であることがTime Magazine（A-2）とReuters（A-2）で確認された（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084)・[INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043)）。オープンソースモデルを含む制限であり、双方向AIデカップリングが進行している。これは[H-BTD-001](../config/hypotheses.json)（グローバル展開）の直接I証拠であり、[H-BTD-003](../config/hypotheses.json)（規制制約）のC証拠である。同時に、豆包の財務構造がより精緻に判明した。日活約1.4億・日収入100万元（人民幣）未満 vs 日次算力コスト1.3〜2.4億元で、ギャップは数百倍に上る（[INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) B-2）。

[H-BTD-001](../config/hypotheses.json) 64% medium（±0%）・[H-BTD-002](../config/hypotheses.json) 38% low（±0%）・[H-BTD-003](../config/hypotheses.json) 40% medium（±0%）。Arbiter v4.31は3仮説とも±0%を維持した。中国の海外アクセス制限協議は構造的な新展開だが、協議段階であり確定していない。豆包エージェント機能の7月15日終了が正式確認された（[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）。もし海外アクセス制限が実施され、かつ豆包がオープンソース配布を停止すれば、[H-BTD-001](../config/hypotheses.json) のグローバル展開前提が崩れる。

## 1. コア判断

中国の最先端AIモデル海外アクセス制限協議は、本ラウンドで最も構造的な変化である。Time Magazine（A-2）とReuters（A-2）が独立して報じた内容は一致する。北京当局がAlibaba・ByteDance・Z.aiと最先端AIモデル（オープンソース含む）への海外アクセス制限について協議中である。同時に米国議員が国内企業による中国AIモデルの採用拡大を阻止する戦略を検討しており、双方向AIデカップリングが進行している。中国AI基本法は2026年1月22日に発効済みである。

この協議は[H-BTD-001](../config/hypotheses.json)（中国規模を足がかりにグローバル展開）の直接I証拠である。ByteDanceが最先端モデルの海外アクセスを制限される場合、グローバル展開の技術的パスが遮断される。但し3点の制約がある。第一に、協議段階であり実施されていない。第二に、オープンソースモデルは配布後に完全な制御が困難である。第三に、ByteDance本体は抖音/TikTokグローバル展開を持ち、AIモデルの制限が全体的グローバル戦略を遮断するわけではない。

豆包の財務構造がより精緻に判明した（[INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) B-2）。日活約1.4億（月活3.45億）、国内AI製品第1位。日収100万元（人民幣）未満、日次算力コスト1.3〜2.4億元。日収vs日次コストのギャップが数百倍。7月15日エージェント機能終了は高コスト低収益サービスの整理が目的と分析されている。AI原生App全体月活4.4億（豆包>千問1.66億>DeepSeek 1.27億）。前回確認した日算力費数千万元vs日収入<100万元の構造的赤字（INFO-095 A-2）が、より精緻なデータで確認された。日コスト範囲（1.3〜2.4億元）が判明したことは、[H-BTD-002](../config/hypotheses.json) のFreemium+ECシナジーモデルの財務的持続性への否定的証拠を強化する。

豆包エージェント機能の7月15日終了が正式確認された（[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）。機能終了後も一定期間スマートエージェント情報・履歴会話の閲覧・保存が可能。努比亚（Nubian）との提携で世界初AI智能体手機をWAIC 2026（7/17-20）で初展示予定。Coze 2.5が「Agent World」エコシステムを導入し、独立実行環境・スキル・アイデンティティを持つエージェントを提供する（[INFO-020](../Information/2026-07-10/collected-raw.md#INFO-020) B-3）。Doubaoエージェント終了後の代替プラットフォームとしての位置づけの可能性がある。

ByteDanceの2026年AI資本支出が2000億元（人民幣）超に引き上げられた（[INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) B-2）。Alibabaは2025-2027年AIインフラ投資を3800億元から4800億元への引き上げを検討中。可霊AIが約$3B調達。中国AIインフラ投資が加速する一方、海外アクセス制限と国内スタートアップへの海外投資制限も協議中という二面性がある。Seedream 5.0 Pro（マルチモーダル画像創作）（[INFO-081](../Information/2026-07-10/collected-raw.md#INFO-081) A-3）・EdgeBench（真実世界環境学習の新Scaling Law発見）（[INFO-083](../Information/2026-07-10/collected-raw.md#INFO-083) A-3）・Seedance 2.5（30秒4K動画生成・世界初）（[INFO-086](../Information/2026-07-10/collected-raw.md#INFO-086) B-2）は製品力・研究力向上（C方向）を示す。

[H-BTD-002](../config/hypotheses.json) は38% lowで±0%。前回3件A-2品質I証拠（エージェント機能強制削除・有料機能開始・Seedance調達不可能）で42→38%に低下した構造は変わらない。本ラウンドでは日コスト範囲の精緻化（1.3〜2.4億元）が財務的赤字の否定的証拠を量的に強化したが、確度変更の閾値には到達しなかった。low帯深化の方向は維持されている。

[H-BTD-001](../config/hypotheses.json) は64% mediumで±0%。日活1.4億・月活3.45億・CAPEX 2000億元超・Seedream 5.0 Pro・EdgeBench・Seedance 2.5は規模と製品力の維持（C方向）だが、中国の海外アクセス制限協議は新たなI証拠である。協議段階であるため確度変更には反映していないが、実施された場合は下方圧力が強まる。

[H-BTD-003](../config/hypotheses.json) は40% mediumで±0%。中国の海外アクセス制限協議・双方向AIデカップリング・AIコンパニオン規則は規制インフラ拡大の証拠として蓄積した。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 中国: 最先端AIモデル海外アクセス制限をAlibaba/ByteDance/Z.aiと協議。オープンソース含む。双方向AIデカップリング | [H-BTD-001](../config/hypotheses.json) グローバル展開の直接I証拠。[H-BTD-003](../config/hypotheses.json) 規制インフラ拡大C証拠。構造的新展開 | A-2 | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) |
| 高 | 豆包日活1.4億・日収<100万元CNY vs 日コスト1.3〜2.4億元。ギャップ数百倍。エージェント終了は高コスト低収益整理が目的 | [H-BTD-002](../config/hypotheses.json) Freemium+ECモデル財務的持続性の否定的証拠強化。日コスト範囲精緻化 | B-2 | [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) |
| 高 | 豆包エージェント機能7/15終了正式確認。努比亚提携AI智能体手機WAIC展示。Coze 2.5 Agent World代替プラットフォーム | [H-BTD-002](../config/hypotheses.json) EC/Agent収益化パス規制遮断の正式確認。[H-BTD-001](../config/hypotheses.json) Coze代替で部分維持 | A-2/B-3 | [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) [INFO-020](../Information/2026-07-10/collected-raw.md#INFO-020) |
| 高 | ByteDance 2026 AI CAPEX 2000億元超引き上げ。Alibaba 4800億元検討。可霊AI ~$3B調達 | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（C方向）。[IND-029](../config/indicators.json) high/rising強化 | B-2 | [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) |
| 高 | AIコンパニオン規則7/15施行: 豆包・千問エージェント機能同時削除（前回確認） | [H-BTD-002](../config/hypotheses.json) 核心命題の規制的遮断。[H-BTD-003](../config/hypotheses.json) 規制インフラ拡大 | A-2 | 前回確認 [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) |
| 高 | Seedream 5.0 Pro・EdgeBench新Scaling Law・Seedance 2.5 30秒4K世界初 | [H-BTD-001](../config/hypotheses.json) 製品力・研究力向上（C方向）。統合マルチモーダルスタック構築 | A-3/B-2 | [INFO-081](../Information/2026-07-10/collected-raw.md#INFO-081) [INFO-083](../Information/2026-07-10/collected-raw.md#INFO-083) [INFO-086](../Information/2026-07-10/collected-raw.md#INFO-086) |
| 高 | Kling AI $30億調達（評価額$180億・Tencent/Alibaba/Baidu参投）・Seedance独立調達ほぼ不可能（前回確認） | 中国AI動画生成競争激化。Seedance ECシナジーモデル持続可能性への市場否認 | A-2 | 前回確認 [INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059) |
| 高 | $200億境外融資seeking・史上最大（前回確認） | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（C方向）。[IND-029](../config/indicators.json) high/rising | A-2 | 前回確認 [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) |
| 中 | 中国対外投資規制強化7/1発効（前回確認） | [H-BTD-003](../config/hypotheses.json) 規制強化C証拠。[H-BTD-001](../config/hypotheses.json) グローバル障壁I方向 | A-1 | 前回確認 [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 中国の海外AIモデルアクセス制限が実施され、オープンソース配布が停止される | [H-BTD-001](../config/hypotheses.json) のグローバル展開前提が崩壊。確度大幅下方修正。現在協議段階（A-2） | 90日 | [IND-011](../config/indicators.json) |
| エージェント機能削除後に豆包のEC転換率が81.1%から大幅に低下する | Freemium + ECモデルのEC収益メカニズムが規制で機能しなくなり、[H-BTD-002](../config/hypotheses.json) の前提が崩れる | 90日 | [IND-010](../config/indicators.json) |
| 豆包DAUが3ヶ月連続で大幅減少（1.4億を下回る） | Freemiumモデルの「集客」段階が破綻し、[H-BTD-001](../config/hypotheses.json) の規模優位前提が崩れる | 90日 | [IND-011](../config/indicators.json) |
| ByteDanceのグローバルAI展開（Doubao/Seed海外版・現地語対応・海外サーバー）が独立確認される | [H-BTD-001](../config/hypotheses.json) の「グローバル展開証拠欠落」判断が崩れる | 180日 | [IND-011](../config/indicators.json) |
| AIコンパニオン規則が撤回・緩和され、エージェント機能が復活する | [H-BTD-002](../config/hypotheses.json) の規制的遮断が解除される | 180日 | [IND-030](../config/indicators.json) |
| Seedanceの独立採算性が確認される（独立法人化・外部資金調達成功） | [H-BTD-002](../config/hypotheses.json) のSeedance調達不可能によるI方向圧力が解消する | 120日 | [IND-010](../config/indicators.json) |
| 中国規制当局がByteDanceのAIサービスライセンスを取り消す・停止する | [H-BTD-001](../config/hypotheses.json)・[H-BTD-002](../config/hypotheses.json) の両方が崩れる | 60日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | 中国で取った規模を足がかりにグローバル展開する | 64% medium | ±0%。日活1.4億・月活3.45億(INFO-085 B-2)・CAPEX 2000億元超(INFO-087 B-2)・Seedream 5.0 Pro(INFO-081 A-3)・EdgeBench(INFO-083 A-3)・Seedance 2.5(INFO-086 B-2)で規模・製品力・研究力維持（C方向）。但し中国海外アクセス制限協議(INFO-084/043 A-2)は新たなI証拠。協議段階のため確度変更保留。グローバル直接証拠限定的。ミラーイメージング警告継続 | [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) [INFO-081](../Information/2026-07-10/collected-raw.md#INFO-081) [INFO-086](../Information/2026-07-10/collected-raw.md#INFO-086) | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) 前回 [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) |
| [H-BTD-002](../config/hypotheses.json) | 豆包でFreemium + ECシナジーモデルを維持し、低価格（無料層）でのユーザー獲得からEC・広告・抖音シナジーを通じたクロス収益化で競争優位を維持する | 38% low | ±0%。日コスト範囲精緻化1.3〜2.4億元vs日収<100万元（INFO-085 B-2）で数百倍ギャップ確認。エージェント機能7/15終了正式確認(INFO-082 A-2)。Coze 2.5代替(INFO-020 B-3)。前回3件A-2品質I証拠(INFO-056/055/059)で42→38%。有料機能開始(INFO-055)・Seedance調達不可能(INFO-059)。low帯深化方向維持だが本ラウンドは新規確度変更材料の閾値未到達 | 前回 [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) 前回 [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) |
| [H-BTD-003](../config/hypotheses.json) | 著作権・規制の制約が競争力を削ぐ | 40% medium | ±0%。中国海外アクセス制限協議(INFO-084/043 A-2)・双方向AIデカップリング・エージェント機能7/15終了正式確認(INFO-082 A-2)・AIコンパニオン規則(INFO-056 A-2)・対外投資規制(前回 INFO-036 A-1)・中国$295B国家計画(前回)で規制インフラ拡大蓄積。但し著作権関連の新証拠はなく、Seedance 2.0はハリウッド6スタジオ警告で全球上線自停の歴史あり | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) | (著作権領域での新規A-2+証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | 豆包DAU ~1.4億・MAU 3.45億(INFO-085 B-2)・日次トークン180兆・Seedream 5.0 Pro(INFO-081 A-3)・EdgeBench新Scaling Law(INFO-083 A-3)・Seedance 2.5 30秒4K(INFO-086 B-2)。但しエージェント機能7/15終了(INFO-082)・海外アクセス制限協議(INFO-084)で制約。MAUソース間乖離継続 | 2026-07-10 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・DeepSeek価格逆転・日コスト赤字拡大でhigh | 日コスト1.3〜2.4億元vs日収<100万元・ギャップ数百倍(INFO-085 B-2)・エージェント機能7/15終了(INFO-082 A-2)・ByteDance CAPEX 2000億元超(INFO-087 B-2)・Seedance独立調達不可能(前回)・Seed 2.1コスト80%削減(前回) | 2026-07-10 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | ByteDance CAPEX 2000億元超(INFO-087 B-2)・$200億境外融資seeking(前回 INFO-080 A-2)・Alibaba 4800億元検討(INFO-087 B-2)・可霊AI ~$3B調達(INFO-087 B-2)・DC $850Bリース+204% YoY(INFO-059 A-2) | 2026-07-10 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | **critical/rising**。中国海外AIモデルアクセス制限協議(INFO-084/043 A-2)・双方向AIデカップリング・エージェント機能7/15終了(INFO-082 A-2)・AIコンパニオン規則(INFO-056 A-2)・Warren開示要求(INFO-044 A-2)・国連LAWS禁止要求(INFO-047 A-2) | 2026-07-10 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-10 | 全面書き直し。中国海外AIモデルアクセス制限協議(INFO-084/043 A-2)・豆包日コスト範囲精緻化1.3〜2.4億元(INFO-085 B-2)・エージェント機能7/15終了正式確認(INFO-082 A-2)・CAPEX 2000億元超(INFO-087 B-2)・Seedream 5.0 Pro(INFO-081 A-3)・EdgeBench(INFO-083 A-3)・Seedance 2.5(INFO-086 B-2)・Coze 2.5(INFO-020 B-3)を新規反映。仮説確度は全て±0%据え置き。Arbiter v4.31 COMPLETE | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) | H-BTD-001 64%(±0%)・H-BTD-002 38%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-07 | ターゲット編集。AIコンパニオン規則エージェント機能強制削除(INFO-056 A-2)・日次トークン180兆・有料機能開始(INFO-055)・Kling調達/Seedance調達不可能(INFO-059)を反映。[H-BTD-002](../config/hypotheses.json) 42→38% | [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055) | H-BTD-002 42→38% |
| 2026-06-30 | ターゲット編集。$200億境外融資seeking・日算力費vs日収入ギャップ数十倍・戦略ピボットを反映。[H-BTD-002](../config/hypotheses.json) 43→42% | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) | H-BTD-002 43→42% |
| 2026-06-28 | 全面書き直し。Seed 2.1新規リリース・DeerFlow 2.0 OSSを反映 | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | H-BTD-001 64%(±0%)・H-BTD-002 44→43%・H-BTD-003 40%(±0%) |
| 2026-06-20 | [H-BTD-002](../config/hypotheses.json) 操作化再定義執行。EC 81.1%収益化のI誤分類を是正。全面書き直し | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | H-BTD-002 46→44% |

## 7. ブラインドスポット

- 中国の海外AIモデルアクセス制限協議（INFO-084/043 A-2）が実施されるか、協議段階で終わるかの判別が不能。オープンソースモデルは配布後に制御困難であり、実効性に疑義がある。但し実施された場合の[H-BTD-001](../config/hypotheses.json) への影響は大きい。
- 豆包MAUに複数ソース間で乖離がある。INFO-085は月活3.45億・日活1.4億、前回INFO-013は1.47億。定義・測定期間・方法論の差の判別が不能。
- 日コスト1.3〜2.4億元（INFO-085 B-2）の算出方法が外部から検証できない。火山引擎API価格からの推算の可能性があり、実際の限界コストを過大評価している可能性。Seed 2.1のコスト80%削減がこの推算をどう変えるかも不明。
- エージェント機能削除（7/15）が豆包の収益構造にどの程度の影響を与えるかの定量データがない。Coze 2.5「Agent World」への移行で実質的な機能代替がどの程度可能かが不明。
- AI資源重点を豆包→企業サービスへ移行（前回確認）とエージェント機能削除（INFO-082）の関係が不明。後者が前者を加速させるのか、独立事象なのかが判別できない。
- ミラーイメージングリスクを統合判断が明示的に認めた。西側の「赤字=持続不能」という財務基準を、EC・広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめると、モデルの優位を見落とす。逆に過大に考慮すると赤字の実相を過小評価する。判別手段がない。
- ByteDanceグローバルAI戦略への中国共産党の介入度が見えない。対外投資規制・国家$295B計画・海外アクセス制限協議は党の関与の兆候だが、AI部門への介入の実態は公開情報にない。
- Seed 2.1のClaude Opus 4.7匹敵はByteDance自家測定。ARC-AGI-2リーダーボード首位0.625は公開だが、評価条件・プロンプト手法の差が不明。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) | 中国: 最先端AIモデル海外アクセス制限をAlibaba/ByteDance/Z.aiと協議・オープンソース含む・双方向AIデカップリング(A-2) |
| [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) | Reuters/CNBC: 北京が中国AIモデル海外アクセス制限協議・米国議員が国内中国AI採用阻止検討・双方向AIデカップリング(A-2) |
| [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) | 豆包日活1.4億・日収<100万元CNY vs 日コスト1.3〜2.4億元・ギャップ数百倍・エージェント終了は高コスト低収益整理(B-2) |
| [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) | 豆包エージェント機能7/15終了正式確認・努比亚AI智能体手機WAIC展示(A-2) |
| [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) | ByteDance 2026 AI CAPEX 2000億元超・Alibaba 4800億元検討・可霊AI ~$3B調達(B-2) |
| [INFO-081](../Information/2026-07-10/collected-raw.md#INFO-081) | Seedream 5.0 Pro: マルチモーダル画像創作モデル・火山方舟/豆包/即夢で展開(A-3) |
| [INFO-083](../Information/2026-07-10/collected-raw.md#INFO-083) | EdgeBench: 真実世界環境学習の超長期評価セット・新Scaling Law発見・統合マルチモーダルスタック(A-3) |
| [INFO-086](../Information/2026-07-10/collected-raw.md#INFO-086) | Seedance 2.5: 30秒4K動画生成世界初・50個全モーダル素材同時入力・局所修正(B-2) |
| [INFO-020](../Information/2026-07-10/collected-raw.md#INFO-020) | Coze 2.5: Agent Worldエコシステム・独立実行環境/スキル/アイデンティティ・Doubao代替可能性(B-3) |
| [INFO-019](../Information/2026-07-10/collected-raw.md#INFO-019) | Doubao/Qwenエージェント機能7/15同時終了・中国AI規制対応・Coze 2.5別プラットフォーム継続(B-2) |
| [Arbiter v4.31](../state/arbiter-2026-07-10.md) | 確度評価の完全根拠 |
