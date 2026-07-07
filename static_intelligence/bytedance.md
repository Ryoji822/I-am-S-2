# ByteDance

> 最終判断更新: 2026-07-07
> 全体確信度: 中
> 情報非対称性: 中国市場の透明性低・言論統制により、観測根拠は他社比で著しく限定的。確度%は記載するが、独立した裏付けを欠く項目が多い。豆包MAUに複数ソース間で乖離（3.45億・3.3億・1.47億）があり、定義・時期・方法論の差の判別が不能。日コスト「数千万元」は火山引擎API価格からの推算であり実際の限界コストを過大評価する可能性。Seed 2.1のコーディング能力Claude Opus 4.7匹敵はByteDance自家測定であり独立ベンチマークでの検証が未完了。中国情報源の限定により独立裏付けなし
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-010](../config/indicators.json) [IND-011](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

中国AIコンパニオン規則の施行（7月15日）により、豆包と通義千問がAIエージェント（智能体）機能の同時削除を発表した [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056)（A-2）。感情依存を生むAIコンパニオンを規制対象とするこの規則は、Freemium + ECシナジーモデルのEC/Agent収益化パスを規制的に遮断する。同時に、豆包の日次トークン使用量が180兆に到達（初期比1500倍成長）し [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055)（A-2）、有料機能（オフィス・Agent向け）が開始された。快手のKling AIが$30億調達（評価額$180億）した一方で、ByteDanceのSeedanceは独立資金調達がほぼ不可能との投資家判断が報じられた [INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059)（A-2）。

[H-BTD-001](../config/hypotheses.json) 64% medium（±0%）・[H-BTD-002](../config/hypotheses.json) 38% low（42→38%・low深化）・[H-BTD-003](../config/hypotheses.json) 40% medium（±0%）。3件のA-2品質I証拠（エージェント機能強制削除 [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056)・有料機能開始 [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055)・Seedance調達不可能 [INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059)）がFreemium+ECシナジーモデル核心命題を直接反証した。もしエージェント機能削除後にEC転換率が急落するか、Seedanceの独立採算が確認されれば、コア判断の前提が変わる。

## 1. コア判断

中国AIコンパニオン規則によるエージェント機能強制削除は、本ラウンドで最も構造的な変化である。豆包と通義千問が7月15日にAIエージェント（智能体）機能の同時下線を発表した [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056)（A-2）。北京が感情依存を生むAIコンパニオンを規制対象とした結果、カスタムエージェント機能が削除される。豆包はタスクモード（快速・専門家・タスク）に機能再編し、猫箱Appで代替エージェント体験を推奨しているが、消費者向けエージェントプラットフォームの収益化パスが規制的に遮断された。中国の規制手法が包括的法律からSSE（Small, Swift, Effective）部門規則へ移行した点も [H-BTD-003](../config/hypotheses.json) の規制インフラ拡大を支持する。

豆包の日次トークン使用量180兆（初期比1500倍）と有料機能開始は、規模と収益化の二軸で相反するシグナルを示す [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055)（A-2）。月活3.45億・日活1.4億の規模は [H-BTD-001](../config/hypotheses.json) の足がかりを維持する。しかしオフィス・Agent向け有料機能の開始は、純Freemiumモデルからの戦略的移行を意味し、[H-BTD-002](../config/hypotheses.json) の核心命題（低価格無料層でのユーザー獲得からEC・広告・抖音シナジーでのクロス収益化）との距離を示す。前回確認した日算力費数千万元 vs 日収入100万元未満の赤字構造 [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095)（A-2）は引き続きFreemium持続性への最も直接的定量否定であり、有料化への移行はこの構造的圧力への対応と読める。

快手のKling AIが$30億調達（評価額$180億）し、Tencent・Alibaba・Baiduが参投した事実は [INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059)（A-2）、中国AI動画生成市場の競争構造を明らかにする。投資家が「ByteDanceのSeedanceは独立資金調達がほぼ不可能」と判断したことは、ECシナジーモデルの持続可能性への市場評価を示す。ByteDance本体の資本基盤（$200億境外融資 [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080)）がSeedanceを支える一方、独立採算性は市場で否定された。Coze 3.0の多人多Agent協作プラットフォームへの進化 [INFO-057](../Information/2026-07-07/collected-raw.md#INFO-057)（B-3）とSeedance 2.5の30秒4K・50参照素材 [INFO-058](../Information/2026-07-07/collected-raw.md#INFO-058)（B-3）は製品力向上（C方向）だが、エージェント機能削除の規制環境下での価値は限定的になる。

[H-BTD-002](../config/hypotheses.json) は42%から38%に低下した（low帯深化）。3件のA-2品質I証拠が核心命題を直接反証した。第一に、エージェント機能強制削除（INFO-056）はEC/Agent収益化パスの規制的遮断である。第二に、有料機能開始（INFO-055）は純Freemiumからの戦略的移行である。第三に、Seedance独立調達不可能（INFO-059）はECシナジーモデルの持続可能性への疑義である。前回確認した日算力費vs日収入の数十倍ギャップと合わせて、Freemiumモデルの財務的持続性に対する否定証拠の重みが決定的に増した。[H-BTD-001](../config/hypotheses.json) は64% mediumで±0%。日次トークン180兆・MAU 3.45億・Seedance 2.5・Coze 3.0は規模と製品力の維持（C方向）だが、グローバル直接証拠は依然限定的であり、エージェント機能削除は国内プラットフォームの制約となる。[H-BTD-003](../config/hypotheses.json) は40% mediumで±0%。AIコンパニオン規則の施行は規制インフラ拡大の新たな証拠として蓄積した。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 中国AIコンパニオン規則7/15施行: 豆包・千問がエージェント機能同時削除。感情依存規制対象 | [H-BTD-002](../config/hypotheses.json) 核心命題（EC/Agent収益化パス）の規制的遮断。Freemium+ECモデルのAgent層が強制除去。[H-BTD-003](../config/hypotheses.json) 規制インフラ拡大 | A-2 | [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) |
| 高 | 豆包日次トークン180兆（初期比1500倍）・MAU 3.45億・有料機能開始（オフィス・Agent向け） | 規模は[H-BTD-001](../config/hypotheses.json)足がかり維持（C方向）。有料機能開始は純Freemiumからの戦略的移行=[H-BTD-002](../config/hypotheses.json)核心命題との距離（I方向） | A-2 | [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055) |
| 高 | Kling AI $30億調達（評価額$180億・Tencent/Alibaba/Baidu参投）・Seedance独立調達ほぼ不可能 | 中国AI動画生成競争激化。SeedanceのECシナジーモデル持続可能性への市場の否認。[H-BTD-002](../config/hypotheses.json) I方向 | A-2 | [INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059) |
| 高 | 豆包DAU 2億突破・日算力費数千万元 vs 日収入<100万元（ギャップ数十倍）・有料化でMAU 610万減少 | Freemium + ECモデルの財務構造。ギャップ数十倍がA-2品質で確定。[H-BTD-002](../config/hypotheses.json) low深化の直接根拠 | A-2 | [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) |
| 高 | Seed 2.1 Pro: コーディングClaude Opus 4.7匹敵・コスト80%削減・ARC-AGI-2首位0.625 | [H-BTD-001](../config/hypotheses.json) フロンティアモデル製品力向上（C方向）。但し自家測定・独立検証なし | A-3 | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) |
| 高 | $200億境外融資seeking・史上最大・AIインフラ・チップ設計向け・Qualcommカスタムチップ協議 | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（C方向）。[IND-029](../config/indicators.json) high/rising強化 | A-2 | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) |
| 高 | QuestMobile: 豆包APP MAU 1.47億・抖音APP MAU 3.3億・収益化価値の81.1%がEC経由 | Freemium + ECモデルの核心メカニズムが動いている（C方向）。但しエージェント機能削除でEC経路に制約 | B-2 | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) |
| 高 | 中国対外投資規制強化: 7月1日発効・AIセクター影響懸念 | [H-BTD-003](../config/hypotheses.json) 規制強化の証拠（C方向）。[H-BTD-001](../config/hypotheses.json) グローバル障壁（I方向） | A-1 | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) |
| 中 | Coze 3.0: 多人多Agent協作プラットフォーム・金融・医療・法律スキルパック | [H-BTD-001](../config/hypotheses.json) エコシステム拡大（C方向）。但しエージェント機能削除環境下での価値は不確定 | B-3 | [INFO-057](../Information/2026-07-07/collected-raw.md#INFO-057) |
| 中 | Seedance 2.5: 30秒4K・50参照素材・3Dレンダリング・AI版権商業化プラットフォーム | [H-BTD-001](../config/hypotheses.json) 製品力向上（C方向）。但し独立調達不可能で持続性に疑義 | B-3 | [INFO-058](../Information/2026-07-07/collected-raw.md#INFO-058) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| エージェント機能削除後に豆包のEC転換率が81.1%から大幅に低下する | Freemium + ECモデルのEC収益メカニズムが規制で機能しなくなり、[H-BTD-002](../config/hypotheses.json) のコア判断が崩れる | 90日 | [IND-010](../config/indicators.json) |
| 豆包DAUが3ヶ月連続で大幅減少（2億を下回る） | Freemiumモデルの「集客」段階が破綻し、[H-BTD-001](../config/hypotheses.json) の規模優位前提が崩れる | 90日 | [IND-011](../config/indicators.json) |
| ByteDanceのグローバルAI展開（Doubao/Seed海外版・現地語対応・海外サーバー）が独立確認される | [H-BTD-001](../config/hypotheses.json) の「グローバル展開証拠欠落」判断が崩れ、確度が大幅上昇する | 180日 | [IND-011](../config/indicators.json) |
| AIコンパニオン規則が撤回・緩和され、エージェント機能が復活する | [H-BTD-002](../config/hypotheses.json) の規制的遮断が解除され、EC/Agent収益化パスが再開する | 180日 | [IND-030](../config/indicators.json) |
| Seedanceの独立採算性が確認される（独立法人化・外部資金調達成功） | [H-BTD-002](../config/hypotheses.json) のSeedance調達不可能によるI方向圧力が解消する | 120日 | [IND-010](../config/indicators.json) |
| 中国規制当局がByteDanceのAIサービスライセンスを取り消す・停止する | [H-BTD-001](../config/hypotheses.json)・[H-BTD-002](../config/hypotheses.json) の両方が崩れる。事業基盤への打撃 | 60日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | 中国で取った規模を足がかりにグローバル展開する | 64% medium | ±0%。日次トークン180兆(INFO-055)・Seedance 2.5(INFO-058)・Coze 3.0(INFO-057)で規模・製品力維持（C方向）。$200億融資(INFO-080)・Seed 2.1(INFO-060)・ARC-AGI-2首位で資本・技術基盤維持。但しグローバル直接証拠は限定的。エージェント機能削除(INFO-056)で国内プラットフォーム制約。対外投資規制(INFO-036)でグローバル障壁継続。ミラーイメージング警告継続。中国情報源の限定により独立裏付けなし | [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055) [INFO-058](../Information/2026-07-07/collected-raw.md#INFO-058) [INFO-057](../Information/2026-07-07/collected-raw.md#INFO-057) [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) |
| [H-BTD-002](../config/hypotheses.json) | 豆包でFreemium + ECシナジーモデルを維持し、低価格（無料層）でのユーザー獲得からEC・広告・抖音シナジーを通じたクロス収益化で競争優位を維持する | 38% low | 42→38%（low帯深化・4R連続低下）。3件A-2品質I証拠が核心命題を直接反証: (1)INFO-056 エージェント機能強制削除=EC/Agent収益化パスの規制的遮断 (2)INFO-055 有料機能開始=純Freemiumからの戦略的移行 (3)INFO-059 Seedance独立調達不可能=ECシナジーモデル持続可能性への市場否認。日算力費数千万元vs日収入<100万元ギャップ数十倍(INFO-095)は構造的赤字の直接定量否定。有料化でMAU 610万減少。EC収益化81.1%(INFO-013)はCだがエージェント機能削除でEC経路に制約。Seed 2.1コスト80%削減(INFO-060)で日コスト下方要因。ミラーイメージングリスク・日コストAPI推算過大評価リスクあり | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055) [INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059) [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079) |
| [H-BTD-003](../config/hypotheses.json) | 著作権・規制の制約が競争力を削ぐ | 40% medium | ±0%。AIコンパニオン規則(INFO-056 A-2)は規制インフラ拡大の新証拠。対外投資規制(INFO-036 A-1)・中国$295B国家計画(INFO-040)は規制強化蓄積。ただし著作権関連の新証拠はなく、Seedance 2.0はハリウッド6スタジオ著作権警告で全球上線自停の歴史あり(INFO-058)。中国情報源の限定により独立裏付けなし | [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | (著作権領域での新規A-2+証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | 豆包DAU 1.4億・MAU 3.45億(INFO-055 A-2)。日次トークン180兆（初期比1500倍）。Seed 2.1 Pro ARC-AGI-2首位0.625(INFO-060 A-3)。Seedance 2.5 30秒4K(INFO-058 B-3)。Coze 3.0(INFO-057 B-3)。但しエージェント機能削除(INFO-056)でプラットフォーム機能制約。MAUにソース間乖離（3.45億・3.3億・1.47億）継続 | 2026-07-07 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・DeepSeek価格逆転・日コスト赤字拡大でhigh | 日算力費数千万元 vs 日収入<100万元・ギャップ数十倍(INFO-095 A-2)。有料機能開始(INFO-055 A-2)。EC収益化81.1%(INFO-013 B-2)。Seedance独立調達不可能(INFO-059 A-2)。Seed 2.1コスト80%削減(INFO-060 A-3)。DeepSeek 1位MAU 1.8億(INFO-055) | 2026-07-07 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | $200億境外融資seeking(INFO-080 A-2)・CAPEX約2000億元超(INFO-054 B-3)・Kling AI $30億調達(INFO-059 A-2)。中国5年$295B国家AI計画(INFO-040)。Qualcommカスタムチップ協議(INFO-080) | 2026-07-07 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | **critical/rising**。AIコンパニオン規則7/15施行(INFO-056 A-2)でエージェント機能強制削除。対外投資規制7/1発効(INFO-036 A-1)。Operation Epic Fury 96h/2,000標的で軍事AI相転移。PentagonはHITLを公式要求したことがない=選択的執行(INFO-093 A-2)。Carnegie: 1オペレーター90エージェント問題(INFO-067 A-1) | 2026-07-07 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-07 | ターゲット編集。中国AIコンパニオン規則によるエージェント機能強制削除(INFO-056 A-2)を新規反映。豆包日次トークン180兆・有料機能開始(INFO-055 A-2)を反映。Kling AI $30億調達・Seedance独立調達不可能(INFO-059 A-2)を反映。Coze 3.0(INFO-057 B-3)・Seedance 2.5(INFO-058 B-3)を反映。[H-BTD-002](../config/hypotheses.json) 42→38% | [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055) [INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059) | H-BTD-002 42→38% |
| 2026-06-30 | ターゲット編集。$200億境外融資seeking(INFO-080 A-2)・日算力費vs日収入ギャップ数十倍A-2品質確認(INFO-095)・豆包有料版・Seedance $2B・戦略ピボット(INFO-079 A-2)を反映。[H-BTD-002](../config/hypotheses.json) 43→42% | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079) | H-BTD-002 43→42% |
| 2026-06-28 | 全面書き直し。Seed 2.1新規リリース(INFO-060 A-3)・DeerFlow 2.0 OSS(INFO-008 B-3)を反映 | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) | H-BTD-001 64%(±0%)・H-BTD-002 44→43%・H-BTD-003 40%(±0%) |
| 2026-06-21 | ターゲット編集。[IND-030](../config/indicators.json) high→critical移行反映 | [INFO-042](../Information/2026-06-21/collected-raw.md#INFO-042) [INFO-041](../Information/2026-06-21/collected-raw.md#INFO-041) | IND-030 high→critical |
| 2026-06-20 | [H-BTD-002](../config/hypotheses.json) 操作化再定義執行。EC 81.1%収益化のI誤分類を是正。全面書き直し | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | H-BTD-002 46→44% |
| 2026-06-13 | AI4S製薬分社化・CAPEX 2000億元・豆包MAU 3.45億/有料コンテンツ6月開始・Seedanceカンヌを反映して全面書き直し | [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | H-BTD-002 48→46% |

## 7. ブラインドスポット

- 中国AIコンパニオン規則によるエージェント機能削除([INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056))が、豆包の収益構造にどの程度の影響を与えるかの定量データがない。タスクモードへの再編や猫箱Appへの移行で実質的な機能代替がどの程度可能かが不明。
- 豆包MAUに複数ソース間で乖離がある。[INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055)は3.45億・日活1.4億、[INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095)は3.45億（QuestMobile）、[INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013)は1.47億。定義・測定期間・方法論の差の判別が不能。
- 「日コスト数千万元」の算出方法が外部から検証できない。火山引擎API価格からの推算であり、実際の限界コストを過大評価している可能性がある。Seed 2.1のコスト80%削減がこの推算をどう変えるかも不明。
- Seedance独立調達不可能([INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059))の投資家判断が、ByteDance全体の戦略的選択（社内リソース配分）なのか、市場の客観的評価なのかの判別ができない。
- Seed 2.1のClaude Opus 4.7匹敵はByteDance自家測定であり、独立ベンチマークでの検証が必要。ARC-AGI-2リーダーボード首位0.625は公開リーダーボードだが、評価条件・プロンプト手法の差が不明。
- ミラーイメージングリスクを統合判断が明示的に認めた。西側の「赤字=持続不能」という財務基準を、EC・広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめると、モデルの優位を見落とす。逆に、このリスクを過大に考慮すると赤字の実相を過小評価する。判別手段がない。
- AI資源重点を豆包→企業サービスへ移行([INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079))との報道と、エージェント機能削除([INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056))の関係が不明。後者が前者を加速させるのか、独立事象なのかが判別できない。
- ByteDanceグローバルAI戦略への中国共産党の介入度が見えない。対外投資規制([INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036))と国家$295B計画([INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040))は党の関与の兆候だが、AI部門への介入の実態は公開情報にない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) | 中国AIコンパニオン規則7/15施行: 豆包・千問エージェント機能同時削除(A-2) |
| [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055) | 豆包日次トークン180兆（1500倍成長）・MAU 3.45億・有料機能開始(A-2) |
| [INFO-059](../Information/2026-07-07/collected-raw.md#INFO-059) | Kling AI $30億調達・Seedance独立調達ほぼ不可能(A-2) |
| [INFO-057](../Information/2026-07-07/collected-raw.md#INFO-057) | Coze 3.0: 多人多Agent協作プラットフォーム(B-3) |
| [INFO-058](../Information/2026-07-07/collected-raw.md#INFO-058) | Seedance 2.5: 30秒4K・50参照素材・3Dレンダリング(B-3) |
| [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) | $200億境外融資seeking・史上最大・AIインフラ・チップ設計向け(A-2) |
| [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) | 豆包DAU 2億突破・日算力費数千万元vs日収入<100万元・有料化MAU 610万減少(A-2) |
| [INFO-079](../Information/2026-06-30/collected-raw.md#INFO-079) | 豆包有料版68-500元/月・Seedance年率$2B・AI資源重点を豆包→企業サービスへ移行(A-2) |
| [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | Seed 2.1: Claude Opus 4.7匹敵・コスト80%削減・ARC-AGI-2首位0.625(A-3) |
| [INFO-008](../Information/2026-06-28/collected-raw.md#INFO-008) | DeerFlow 2.0 OSS: LangGraphベース・Claude-to-DeerFlow マイグレーションツール(B-3) |
| [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | QuestMobile: 豆包APP MAU 1.47億・抖音APP MAU 3.3億・収益化価値の81.1%がEC経由(B-2) |
| [INFO-109](../Information/2026-06-20/collected-raw.md#INFO-109) | 火山引擎 中国agent開発プラットフォーム市場双首位・Coze 3.0(B-2) |
| [INFO-054](../Information/2026-06-13/collected-raw.md#INFO-054) | ByteDance AI4S製薬事業分社化・CAPEX 2000億元超上方修正(B-3) |
| [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | 中国5年間2兆元（$2,950億）全国AIインフラ計画(A-3) |
| [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) | 中国対外投資規制強化・7月1日発効(A-1) |
