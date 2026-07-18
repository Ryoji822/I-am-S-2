# ByteDance

> 最終判断更新: 2026-07-18
> 全体確信度: 中
> 情報非対称性: ByteDance内部の財務データが外部検証不可能. 日コスト1.3〜2.4億元は36kr等の報道に基づく推算であり, 実際の限界コストを過大評価する可能性がある. 豆包MAUにソース間で乖離（3.45億・2億日活等）があり, 定義・時期・方法論の差の判別が不能. Seed 2.0・Seedance 2.0の能力評価はByteDance自家測定・API仕様ベースであり, 独立ベンチマークでの検証が未完了. エージェント機能7/15終了が一時的か恒久的かの判別が不能. 中国情報源の限定により独立裏付けなし
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-010](../config/indicators.json) [IND-011](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

ByteDanceは豆包DAU 2億突破・月活3.82億（[INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3）で消費者基盤の規模を拡大している. Seedance 2.5がネイティブ30秒シネマティック動画生成を実現し（[INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) B-1）, SeedanceのAI動画市場シェア80%超が再確認された（[INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) A-3）. ただしGoogle Gemini Omni FlashがText-to-Video/Image-to-VideoランキングでSeedance 2.0を僅差で上回り首位を奪取し（[INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) B-1）, 競争環境に変化が生じている. ArkClawクラウドネイティブagent平台のVolcano Engine経由展開（[INFO-012](../Information/2026-07-18/collected-raw.md#INFO-012) C-2）とCoze 3.0智能体平台の効率化（[INFO-063](../Information/2026-07-18/collected-raw.md#INFO-063) A-3）は企業サービス方向のインフラ整備を示す. AI Rack 3.0兆瓦級計算システム（[INFO-061](../Information/2026-07-18/collected-raw.md#INFO-061) A-3）はインフラ投資の継続を示すが, 字节資本支出1600億元（[INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3）と日収<100万元 vs 日コスト1.3〜2.4億元の数百倍ギャップ（[INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) B-2）は構造的赤字の継続を示す. 中国AIエージェント規則の7/15執行可能性確認（[INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) B-1）が規制環境の硬化を示す.

[H-BTD-001](../config/hypotheses.json) 64% medium（±0%）・[H-BTD-002](../config/hypotheses.json) 37% low（38→37%, ステートメント修正）・[H-BTD-003](../config/hypotheses.json) 40% medium（±0%）. Arbiter v4.39はv4.38絶対条件1を実行し, [H-BTD-002](../config/hypotheses.json)のステートメントを旧「Freemium+ECシナジーモデルを維持」から新「Freemium+ECシナジーから企業サービスへの移行過程」に修正した. 消費者基盤（豆包）は残余的役割と再定義され, CapEx再配分の戦略的方向が明示された. ステートメントのAND構造に対する反証可能性懸念（Red指摘）を記録し, 反証可能な定量条件の組み込みを次回絶対条件化した.

## 1. コア判断

本ラウンドの構造的変化は6点ある. 第一にv4.38絶対条件1の実行として, [H-BTD-002](../config/hypotheses.json)のステートメントが修正された（Arbiter v4.39確認）. 旧ステートメント「Freemium+ECシナジーモデルを維持し, 低価格でのユーザー獲得からクロス収益化で競争優位を維持する」は, 7/15エージェント機能停止と構造的赤字の継続によって核心命題が維持困難になった. 新ステートメント「Freemium+ECシナジーから企業サービスへの移行過程にある. Freemiumの消費者基盤（豆包）は残余的役割として機能しつつ, CapEx再配分（企業サービス+25%）が戦略的方向を決定づける」は, ArkClaw agent平台のVolcano Engine展開（[INFO-012](../Information/2026-07-18/collected-raw.md#INFO-012) C-2）・Coze 3.0智能体平台の効率化（[INFO-063](../Information/2026-07-18/collected-raw.md#INFO-063) A-3）・AI Rack 3.0兆瓦級計算システム（[INFO-061](../Information/2026-07-18/collected-raw.md#INFO-061) A-3）で方向性が裏付けられた. ただし新ステートメントのAND構造に対し, Redは反証可能性の懸念を指摘した. 反証可能な定量条件（例: 2027年中に企業サービス収益が消費者を超過するか）の組み込みを次回絶対条件化している.

第二に豆包DAU 2億突破・月活3.82億の確認である（[INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3）. QuestMobile 2026年6月データで, 豆包3.82億・千問・DeepSeekの順で活躍ユーザー規模. 字节内部で豆包は「歴史上破億DAU製品で推広費最低」とされ, 自然成長の可能性を示す. ただし字节資本支出は2025年に1600億元に達する見込みで, 3.82億月活ユーザーがH800/A100集群算力を消耗する構造は変わらない. これは[H-BTD-001](../config/hypotheses.json)（規模・製品力維持）のC方向証拠であると同時に, [H-BTD-002](../config/hypotheses.json)の構造的赤字文脈でもある.

第三にSeedance 2.5のリリースである（[INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) B-1）. ネイティブ30秒のシネマティックAI動画生成, 最大50の参照（画像・音声・動画・3D）を利用可能. ただしGoogle Gemini Omni FlashがArtificial Analysis Text-to-Video・Image-to-VideoランキングでSeedance 2.0を僅差で上回り首位を獲得した（[INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) B-1）. Seedance 2.5での巻き返しを図る段階である. SeedanceのAI動画市場シェア80%超は再確認された（[INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) A-3）. 競合の快手可霊AIが$30億調達（評価額$180億）, 演语科技（字节離職者設立）が$3億/$20億超で資本を強化している.

第四に中国AIエージェント規則の7/15執行可能性確認である（[INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) B-1）. 「智能体実施意見」が7/15以降執行可能と確認され, エージェント機能停止の規制根拠が明確化された. これは[H-BTD-002](../config/hypotheses.json)の移行圧力を強化する証拠である. 第五にSeed 2.0モデルファミリー（Pro/Lite/Mini）の多モーダル深度思考能力拡張が継続している（[INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) A-3）. 第六にDeepSeekが新ラウンド調達を計画し, 2026年中国本土IPOを準備中である（[INFO-100](../Information/2026-07-16/collected-raw.md#INFO-100) B-2）.

[H-BTD-001](../config/hypotheses.json) は64% mediumで±0%. 豆包MAU 3.82億（[INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3）・Seedance 2.5（[INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) B-1）・Seedance市場シェア80%超（[INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) A-3）・AI Rack 3.0（[INFO-061](../Information/2026-07-18/collected-raw.md#INFO-061) A-3）・CAPEX 1600億元（[INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3）で規模・製品力の維持（C方向）が確認された. ただし中国の海外アクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）がI証拠として継続する. 協議段階であるため確度変更には反映していない.

[H-BTD-002](../config/hypotheses.json) は37% low（38→37%, ステートメント修正）. 旧ステートメントの「維持」前提が7/15エージェント機能停止（[INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) B-3・[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）・AIエージェント規則7/15執行可能（[INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) B-1）・日コスト1.3〜2.4億元 vs 日収<100万元の数百倍ギャップ（[INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) B-2）によって維持困難になった. 新ステートメントは「移行過程」を明示し, ArkClaw・Coze 3.0での企業サービス基盤構築が方向性を示す. 但し反証可能性の懸念（AND構造, Red指摘）を記録し, 定量条件の組み込みを次回絶対条件化した.

[H-BTD-003](../config/hypotheses.json) は40% mediumで±0%. 中国の海外AIモデルアクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）・双方向AIデカップリング・エージェント機能7/15終了（[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）・AIエージェント規則7/15執行可能（[INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) B-1）で規制インフラ拡大の証拠が蓄積した. ただし本仮説の核心命題は著作権問題による法的制約であり, 著作権関連の新規A-2+証拠は今ラウンドでも確認されなかった.

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Seed 2.0 Pro/Lite/Mini追加・多モーダル深度思考能力拡張・260428シリーズ | [H-BTD-001](../config/hypotheses.json) フロンティアモデル継続リリース（C方向） | A-3 | [INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) |
| 高 | Seedance 2.0業界初4モダリティ同時入力・Seedance 2.5最大50秒動画・4K/Mini版・API公開 | [H-BTD-001](../config/hypotheses.json) フロンティア能力（C方向） | A-3 | [INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) |
| 高 | Seedance AI動画生成市場シェア80%超・快手可霊AI $30億調達（評価額$180億）・愛詩科技C+調達 | [H-BTD-001](../config/hypotheses.json) 市場支配力維持（C方向）. [H-BTD-002](../config/hypotheses.json) Seedance独立採算性の市場文脈 | B-2 | [INFO-099](../Information/2026-07-16/collected-raw.md#INFO-099) |
| 高 | 豆包MAU 3.45億（2026年Q1, QuestMobile）・日活2億突破・国内C端AI首位 | [H-BTD-001](../config/hypotheses.json) 規模優位維持（C方向） | B-2 | [INFO-094](../Information/2026-07-16/collected-raw.md#INFO-094) |
| 高 | 豆包エージェント機能7/15停止・ByteDance/Alibaba同時実施・「製品機能調整」 | [H-BTD-002](../config/hypotheses.json) EC/Agent収益化パス規制遮断の継続（I方向）. [H-BTD-003](../config/hypotheses.json) 規制インフラ拡大 | B-3/A-2 | [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) |
| 高 | 豆包日活1.4億・日収<100万元CNY vs 日コスト1.3〜2.4億元・ギャップ数百倍 | [H-BTD-002](../config/hypotheses.json) Freemium+ECモデル財務持続性の否定的証拠（I方向） | B-2 | [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) |
| 高 | 中国: 最先端AIモデル海外アクセス制限をAlibaba/ByteDance/Z.aiと協議・オープンソース含む・双方向AIデカップリング | [H-BTD-001](../config/hypotheses.json) グローバル展開の直接I証拠. [H-BTD-003](../config/hypotheses.json) 規制インフラ拡大C証拠 | A-2 | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) |
| 高 | ByteDance 2026 AI CAPEX 2000億元超・Alibaba 4800億元検討・可霊AI ~$3B調達 | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（C方向）. [IND-029](../config/indicators.json) high/rising | B-2 | [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) |
| 高 | Coze 3.0ゼロコード智能体開発プラットフォーム・ワークスペース/リソースライブラリ・DeepSeek統合 | [H-BTD-002](../config/hypotheses.json) エージェント代替プラットフォームの可能性（C方向） | B-3 | [INFO-098](../Information/2026-07-16/collected-raw.md#INFO-098) |
| 高 | 豆包AI智能体手機（ByteDance×中興努比亚）・WAIC 2026発表予定・全体出荷約20万台・世界初 | [H-BTD-001](../config/hypotheses.json) エコシステムハードウェア拡大（C方向） | B-2 | [INFO-096](../Information/2026-07-16/collected-raw.md#INFO-096) |
| 高 | DeepSeek新ラウンド調達計画+2026年中国本土IPO準備・WAIC 2026発表期待 | 中国AI生態系の資本自律性. ByteDance競合環境の構造変化兆候 | B-2 | [INFO-100](../Information/2026-07-16/collected-raw.md#INFO-100) |
| 中 | Seedream 5.0 Pro・EdgeBench新Scaling Law・Seedance 2.5 30秒4K世界初（前回確認） | [H-BTD-001](../config/hypotheses.json) 製品力・研究力向上（C方向） | A-3/B-2 | [INFO-081](../Information/2026-07-10/collected-raw.md#INFO-081) [INFO-083](../Information/2026-07-10/collected-raw.md#INFO-083) [INFO-086](../Information/2026-07-10/collected-raw.md#INFO-086) |
| 中 | $200億境外融資seeking・史上最大（前回確認） | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（C方向） | A-2 | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 中国の海外AIモデルアクセス制限が実施され, オープンソース配布が停止される | [H-BTD-001](../config/hypotheses.json) のグローバル展開前提が崩壊. 確度大幅下方修正. 現在協議段階（A-2） | 90日 | [IND-011](../config/indicators.json) |
| 7/15エージェント機能停止が恒久的であることが確認される | [H-BTD-002](../config/hypotheses.json) のFreemium+EC核心命題への直接Iが強化され, low帯深化が加速 | 60日 | [IND-010](../config/indicators.json) |
| エージェント機能削除後に豆包のEC転換率が大幅に低下する | Freemium + ECモデルのEC収益メカニズムが規制で機能しなくなり, [H-BTD-002](../config/hypotheses.json) の前提が崩れる | 90日 | [IND-010](../config/indicators.json) |
| 豆包DAUが3ヶ月連続で大幅減少（1.4億を下回る） | Freemiumモデルの「集客」段階が破綻し, [H-BTD-001](../config/hypotheses.json) の規模優位前提が崩れる | 90日 | [IND-011](../config/indicators.json) |
| ByteDanceのグローバルAI展開（Doubao/Seed海外版・現地語対応・海外サーバー）が独立確認される | [H-BTD-001](../config/hypotheses.json) の「グローバル展開証拠欠落」判断が崩れる | 180日 | [IND-011](../config/indicators.json) |
| Seedanceの独立採算性が確認される（独立法人化・外部資金調達成功） | [H-BTD-002](../config/hypotheses.json) のSeedance調達不可能によるI方向圧力が解消する | 120日 | [IND-010](../config/indicators.json) |
| AIコンパニオン規則が撤回・緩和され, エージェント機能が復活する | [H-BTD-002](../config/hypotheses.json) の規制的遮断が解除される | 180日 | [IND-030](../config/indicators.json) |
| 中国規制当局がByteDanceのAIサービスライセンスを取り消す・停止する | [H-BTD-001](../config/hypotheses.json)・[H-BTD-002](../config/hypotheses.json) の両方が崩れる | 60日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持し、グローバル展開を図る | 64% medium | ±0%. DAU 2億突破・MAU 3.82億([INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3)・Seedance 2.5([INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) B-1)・Seedance市場シェア80%超([INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) A-3)・AI Rack 3.0([INFO-061](../Information/2026-07-18/collected-raw.md#INFO-061) A-3)・CAPEX 1600億元([INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3)で規模・製品力維持（C方向）. 但し中国海外アクセス制限協議(INFO-084 A-2)・Gemini Omni Flash首位奪取(INFO-064 B-1)はI証拠. 協議段階・僅差のため確度変更保留. ミラーイメージング警告継続 | [INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) [INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) [INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) [INFO-061](../Information/2026-07-18/collected-raw.md#INFO-061) | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) [INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceはFreemium+ECシナジーから企業サービスへの移行過程にある. Freemiumの消費者基盤（豆包）は残余的役割として機能しつつ、CapEx再配分（企業サービス+25%）が戦略的方向を決定づける | 37% low | 38→37%. ステートメント修正(v4.38絶対条件1実行, v4.39確認). 旧「Freemium+ECシナジーモデルを維持」→新「企業サービスへの移行過程」. ArkClaw agent平台([INFO-012](../Information/2026-07-18/collected-raw.md#INFO-012) C-2)・Coze 3.0([INFO-063](../Information/2026-07-18/collected-raw.md#INFO-063) A-3)で企業サービス基盤構築の方向性. 但し日コスト1.3〜2.4億元 vs 日収<100万元の数百倍ギャップ(INFO-085 B-2)・エージェント機能7/15停止(INFO-013 B-3・INFO-082 A-2)・AIエージェント規則7/15執行可能(INFO-038 B-1)で移行圧力強化. 新ステートメントAND構造の反証可能性懸念(Red指摘)記録, 定量条件組み込み次回絶対条件化 | [INFO-012](../Information/2026-07-18/collected-raw.md#INFO-012) [INFO-063](../Information/2026-07-18/collected-raw.md#INFO-063) [INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) | [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) [INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受け、グローバル展開が制限される | 40% medium | ±0%. 中国海外アクセス制限協議(INFO-084 A-2)・AIエージェント規則7/15執行可能([INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) B-1)・双方向AIデカップリング・エージェント機能7/15終了(INFO-082 A-2)で規制インフラ拡大蓄積. 但し核心命題は著作権問題であり, 著作権関連の新規A-2+証拠は確認されず. Seedance 2.0はハリウッド6スタジオ警告で全球上線自停の歴史あり | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) | (著作権領域での新規A-2+証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | elevated. 豆包DAU 2億突破・MAU 3.82億([INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3)・Seedance 2.5 30秒シネマティック([INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) B-1)・Seedance市場シェア80%超([INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) A-3). 但しGemini Omni Flash首位奪取([INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) B-1)・エージェント機能7/15終了([INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013)・[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082))で制約 | 2026-07-18 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・日コスト赤字拡大でhigh | high. 日コスト1.3〜2.4億元 vs 日収<100万元・ギャップ数百倍([INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) B-2)・エージェント機能7/15終了([INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013)・[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082))・ByteDance CAPEX 1600億元([INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3)・ArkClaw企業サービス移行基盤([INFO-012](../Information/2026-07-18/collected-raw.md#INFO-012) C-2) | 2026-07-18 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | high/rising. ByteDance CAPEX 1600億元([INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) A-3)・AI Rack 3.0兆瓦級計算システム([INFO-061](../Information/2026-07-18/collected-raw.md#INFO-061) A-3)・$200億境外融資seeking(前回 [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) A-2)・可霊AI ~$3B調達([INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) A-3) | 2026-07-18 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | critical/rising. 中国海外AIモデルアクセス制限協議([INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2)・エージェント機能7/15終了([INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2)・AIコンパニオン規則(前回 [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) A-2) | 2026-07-16 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-16 | 全面書き直し. Seed 2.0 Pro/Lite/Mini追加([INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) A-3)・Seedance 2.0業界初4モダリティ([INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) A-3)・Coze 3.0([INFO-098](../Information/2026-07-16/collected-raw.md#INFO-098) B-3)・Seedance市場シェア80%超([INFO-099](../Information/2026-07-16/collected-raw.md#INFO-099) B-2)・DeepSeek IPO準備([INFO-100](../Information/2026-07-16/collected-raw.md#INFO-100) B-2)・豆包AI智能体手機([INFO-096](../Information/2026-07-16/collected-raw.md#INFO-096) B-2)を新規反映. 仮説確度は全て±0%据え置き. Arbiter v4.37 COMPLETE | [INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) [INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) [INFO-099](../Information/2026-07-16/collected-raw.md#INFO-099) | H-BTD-001 64%(±0%)・H-BTD-002 38%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-10 | 全面書き直し. 中国海外AIモデルアクセス制限協議(INFO-084/043 A-2)・豆包日コスト範囲精緻化1.3〜2.4億元(INFO-085 B-2)・エージェント機能7/15終了正式確認(INFO-082 A-2)・CAPEX 2000億元超(INFO-087 B-2)・Seedream 5.0 Pro(INFO-081 A-3)・EdgeBench(INFO-083 A-3)・Seedance 2.5(INFO-086 B-2)・Coze 2.5(INFO-020 B-3)を新規反映. 仮説確度は全て±0%据え置き. Arbiter v4.31 COMPLETE | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) | H-BTD-001 64%(±0%)・H-BTD-002 38%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-07 | ターゲット編集. AIコンパニオン規則エージェント機能強制削除(INFO-056 A-2)・日次トークン180兆・有料機能開始(INFO-055)・Kling調達/Seedance調達不可能(INFO-059)を反映. [H-BTD-002](../config/hypotheses.json) 42→38% | [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) [INFO-055](../Information/2026-07-07/collected-raw.md#INFO-055) | H-BTD-002 42→38% |
| 2026-06-30 | ターゲット編集. $200億境外融資seeking・日算力費vs日収入ギャップ数十倍・戦略ピボットを反映. [H-BTD-002](../config/hypotheses.json) 43→42% | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) [INFO-095](../Information/2026-06-30/collected-raw.md#INFO-095) | H-BTD-002 43→42% |
| 2026-06-28 | 全面書き直し. Seed 2.1新規リリース・DeerFlow 2.0 OSSを反映 | [INFO-060](../Information/2026-06-28/collected-raw.md#INFO-060) | H-BTD-001 64%(±0%)・H-BTD-002 44→43%・H-BTD-003 40%(±0%) |
| 2026-06-20 | [H-BTD-002](../config/hypotheses.json) 操作化再定義執行. EC 81.1%収益化のI誤分類を是正. 全面書き直し | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) | H-BTD-002 46→44% |

## 7. ブラインドスポット

- 7/15エージェント機能停止（[INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) B-3・[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）が一時的か恒久的かの判別が不能. Arbiter v4.37がこの評価を次回絶対条件化した. 一時的であればI証拠の重みは減じ, 恒久的であれば[H-BTD-002](../config/hypotheses.json)核心命題への直接Iが確定する.
- 中国の海外AIモデルアクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）が実施されるか, 協議段階で終わるかの判別が不能. オープンソースモデルは配布後に制御困難であり, 実効性に疑義がある. 但し実施された場合の[H-BTD-001](../config/hypotheses.json) への影響は大きい.
- 豆包MAUにソース間で乖離がある. [INFO-094](../Information/2026-07-16/collected-raw.md#INFO-094)（B-2）は月活3.45億・日活2億, [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085)（B-2）は日活1.4億. 定義・測定期間・方法論の差の判別が不能.
- 日コスト1.3〜2.4億元（[INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) B-2）の算出方法が外部から検証できない. 火山引擎API価格からの推算の可能性があり, 実際の限界コストを過大評価している可能性.
- Seed 2.0・Seedance 2.0の能力は火山引擎公式ドキュメント・API仕様ベース（[INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101)・[INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) A-3）であり, 独立ベンチマークでの検証が未完了. Seedance市場シェア80%超（[INFO-099](../Information/2026-07-16/collected-raw.md#INFO-099) B-2）の測定方法・定義も不明.
- Coze 3.0（[INFO-098](../Information/2026-07-16/collected-raw.md#INFO-098) B-3）が豆包エージェント終了後の代替プラットフォームとして機能するかが不明. 機能レベルでの実質代替が可能か, 単なる別製品なのかの判別ができない.
- ミラーイメージングリスクを統合判断が明示的に認めた. 西側の「赤字=持続不能」という財務基準を, EC・広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめると, モデルの優位を見落とす. 逆に過大に考慮すると赤字の実相を過小評価する. 判別手段がない.
- DeepSeek IPO準備（[INFO-100](../Information/2026-07-16/collected-raw.md#INFO-100) B-2）がByteDanceの競争環境にどのような影響を与えるかが不明. DeepSeekの資本自律性が価格競争を激化させるか, 逆にByteDanceの差別化を促すかの判別ができない.
- ByteDanceグローバルAI戦略への中国共産党の介入度が見えない. 対外投資規制・海外アクセス制限協議は党の関与の兆候だが, AI部門への介入の実態は公開情報にない.

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) | Doubao Seed 2.0 Pro/Lite/Mini追加・多モーダル深度思考能力拡張・260428シリーズ(A-3) |
| [INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) | Seedance 2.0/2.5業界初4モダリティ同時入力・最大50秒動画・4K/Mini版・API公開(A-3) |
| [INFO-099](../Information/2026-07-16/collected-raw.md#INFO-099) | Seedance市場シェア80%超・快手可霊AI $30億調達（評価額$180億）・愛詩科技C+調達(B-2) |
| [INFO-094](../Information/2026-07-16/collected-raw.md#INFO-094) | 豆包MAU 3.45億・日活2億突破・国内C端AI首位・人均月使用76.7回(B-2) |
| [INFO-096](../Information/2026-07-16/collected-raw.md#INFO-096) | 豆包AI智能体手機（ByteDance×中興努比亚）・WAIC 2026発表予定・出荷約20万台(B-2) |
| [INFO-098](../Information/2026-07-16/collected-raw.md#INFO-098) | Coze 3.0ゼロコード智能体開発プラットフォーム・ワークスペース/リソースライブラリ・DeepSeek統合(B-3) |
| [INFO-100](../Information/2026-07-16/collected-raw.md#INFO-100) | DeepSeek新ラウンド調達計画+2026年中国本土IPO準備・WAIC 2026発表期待(B-2) |
| [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) | ByteDance/Alibaba Doubao・Qwenエージェント機能7月15日停止・「製品機能調整」(B-3) |
| [INFO-095](../Information/2026-07-16/collected-raw.md#INFO-095) | 豆包日活2億突破も日次収益不足100万元・毎日数千万の損失・規模と収益の乖離(B-3) |
| [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) | 豆包エージェント機能7/15終了正式確認・努比亚AI智能体手機WAIC展示(A-2) |
| [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) | 中国: 最先端AIモデル海外アクセス制限をAlibaba/ByteDance/Z.aiと協議・オープンソース含む・双方向AIデカップリング(A-2) |
| [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) | Reuters/CNBC: 北京が中国AIモデル海外アクセス制限協議・米国議員が国内中国AI採用阻止検討・双方向AIデカップリング(A-2) |
| [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) | 豆包日活1.4億・日収<100万元CNY vs 日コスト1.3〜2.4億元・ギャップ数百倍・エージェント終了は高コスト低収益整理(B-2) |
| [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) | ByteDance 2026 AI CAPEX 2000億元超・Alibaba 4800億元検討・可霊AI ~$3B調達(B-2) |
| [INFO-081](../Information/2026-07-10/collected-raw.md#INFO-081) | Seedream 5.0 Pro: マルチモーダル画像創作モデル・火山方舟/豆包/即夢で展開(A-3) |
| [INFO-083](../Information/2026-07-10/collected-raw.md#INFO-083) | EdgeBench: 真実世界環境学習の超長期評価セット・新Scaling Law発見・統合マルチモーダルスタック(A-3) |
| [INFO-086](../Information/2026-07-10/collected-raw.md#INFO-086) | Seedance 2.5: 30秒4K動画生成世界初・50個全モーダル素材同時入力・局所修正(B-2) |
| [Arbiter v4.37](../state/arbiter-2026-07-16.md) | 確度評価の完全根拠 |
