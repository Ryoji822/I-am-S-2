# ByteDance

> 最終判断更新: 2026-07-30
> 全体確信度: 中
> 情報非対称性: ByteDance内部の財務データが外部検証不可能. 日コスト1.3〜2.4億元は36kr等の報道に基づく推算であり, 実際の限界コストを過大評価する可能性がある. 豆包MAUにソース間で乖離が存在したが, [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2がDAU差異の技術的説明（ピーク vs 持続的・測定対象・時期・定義の違い）を初めて提供し, 長年のDAU不確実性が部分的に解消された. 但し完全解消には至らず, 持続的DAUの正確な数値は依然として不確実. $700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）は史上最大規模だが, 投資計画と実行のギャップは未知数. Seed 2.0 Code 256K・Seedance 2.0の能力評価はByteDance自家測定・API仕様ベースであり, 独立ベンチマークでの検証が未完了. エージェント機能7/15終了が一時的か恒久的かの判別が不能. 中国情報源の限定により独立裏付けなし
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-010](../config/indicators.json) [IND-011](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

ByteDanceは豆包MAU 5.28億（2026年6月・過去最高・[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）で消費者基盤を拡大しつつ, 2026年に最大$700億をAIインフラに投入する計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）を発表した. 前回記録のMAU 3.82億から+38%成長し, DAUピーク1.45億（春節）の技術的説明も初めて確認された. 火山方舟上のSeed Audio・Coze・Seedance 2.0で企業インフラを並行拡大する構造は維持されている. 2025年売上$186B・純利益$48B（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2）はTikTok/抖音広告収益が消費者赤字をクロス補填する構造を示す. ただし日次売上<100万元 vs 日次コスト数千万元のギャップ（[INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2）は消費者AIビジネス単体の経済的持続性に懸念を呈している. Seed 2.0 Code 256Kはコーディング市場参入の意欲を示すが, A-1品質証拠の出所独立性（ByteDance自己開示）にArbiter v4.49が構造的リスクを記録し, v4.51まで未解消.

[H-BTD-001](../config/hypotheses.json) 64% medium（±0%）・[H-BTD-002](../config/hypotheses.json) 36% low（±0%, Blue +1%提案がArbiter v4.49/v4.50/v4.51で3R連続却下・出所独立性・保護市場・投資≠成果の3条件未解消）・[H-BTD-003](../config/hypotheses.json) 40% medium（±0%）. H-BTD-002のステートメントは「消費者基盤と企業インフラの相乗的並行拡大」. 反証条件（消費者DAU減少または企業Token経済成長停止）が明示されている. Arbiter v4.50が「DAU差異技術的説明」を絶対条件化し, [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2で部分的解消したが完全解消未達. 保護市場・ミラーイメージング・投資≠成果の3条件は3R未解消で, 保守的下限採用が継続.

## 1. コア判断

本ラウンドの構造的変化は豆包MAU 5.28億・過去最高更新（[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）とByteDance最大$700億AIインフラ投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）の確認である. 前回記録のMAU 3.82億から38%増加し, DAUピーク1.45億（春節期間）vs 持続的約8000万（AI検索領域）の差異が測定対象・時期・定義の違いによることが初めて技術的に説明された. Arbiter v4.50はこの「DAU差異技術的説明」を絶対条件として設定していたが, [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2で部分的解消に留まり, Blue AgentのH-BTD-002 +1%提案はArbiter v4.51で3R連続却下された.

$700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）は, 前回記録のCAPEX 2000億元（約$280億, [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) B-2）から2.5倍への拡大を示す. これは[ByteDance 2025年売上$186B・純利益$48B](../Information/2026-07-23/collected-raw.md#INFO-060)（B-2）の財務的基盤の上に構築される. 火山引擎が企業級クラウド・AIサービスプラットフォームとして大モデル・データインテリジェンス・推薦アルゴリズム・音声動画技術を提供し, Coze企業プラットフォーム（[INFO-077](../Information/2026-07-30/collected-raw.md#INFO-077) B-3）の低コードエージェント開発機能で企業向け私有化展開も進む. この全体収益構造の中で, 豆包の消費者AI赤字（日次売上<100万元 vs 日次コスト数千万元, [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2）はTikTok/抖音の広告収益でクロス補填されている可能性が高い. 但し投資計画と実行成果の乖裂は未知数であり, Arbiterは「投資≠成果」をH-BTD-002 +1%却下の3条件の一つとして継続.

[H-BTD-001](../config/hypotheses.json) は64% mediumで±0%. 豆包MAU 5.28億・過去最高更新（[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）・$700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）・Seed Audio 1.0（[INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) A-3）・Coze企業プラットフォーム（[INFO-068](../Information/2026-07-23/collected-raw.md#INFO-068) B-2・[INFO-077](../Information/2026-07-30/collected-raw.md#INFO-077) B-3）・豆包AI智能体手机（[INFO-049](../Information/2026-07-23/collected-raw.md#INFO-049) B-2）・Seedance市場シェア80%超・ByteDance $186B売上（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2）で規模・製品力の維持（C方向）が確認された. ただし中国の海外アクセス制限協議・Gemini Omni Flash首位奪取がI証拠として継続する.

[H-BTD-002](../config/hypotheses.json) は36% low（±0%, Blue +1%提案がArbiter v4.49/v4.50/v4.51で3R連続却下）. ステートメント「消費者基盤と企業インフラの相乗的並行拡大」に対し, MAU 5.28億・過去最高（消費者軸）と$700億投資・Coze企業版（企業軸）のデュアルアクシス拡大が確認された. 但しArbiter v4.51は出所独立性疑義（ByteDance自己開示）・保護市場・投資≠成果の3条件が3R未解消として+1%提案を却下した. DAU差異技術的説明は[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068)で部分的解消したが完全解消未達.

[H-BTD-003](../config/hypotheses.json) は40% mediumで±0%. 中国の海外AIモデルアクセス制限協議・エージェント機能7/15終了・AIエージェント規則7/15執行可能・WAICO設立（[INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) B-3）で規制インフラ拡大の証拠が蓄積した. ただし核心命題は著作権問題による法的制約であり, 著作権関連の新規A-2+証拠は今ラウンドでも確認されなかった.

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | ByteDance 2026年最大$700億AIインフラ投資計画（前回CAPEX ~2000億元から2.5x拡大） | [H-BTD-001](../config/hypotheses.json) 資本基盤の飛躍的拡大（C方向）. [H-BTD-002](../config/hypotheses.json) 企業インフラ投資軸強化（C方向）だが投資≠成果リスク. [IND-029](../config/indicators.json) high/accelerating | A-2 | [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) |
| 高 | 豆包MAU 5.28億・2026年6月過去最高（前回3.82億から+38%）. DAUピーク1.45億（春節）vs 持続的~8000万（AI検索） | [H-BTD-001](../config/hypotheses.json) 規模優位拡大（C方向）. [H-BTD-002](../config/hypotheses.json) 消費者軸成長確認・DAU差異技術的説明で絶対条件部分的解消 | A-2 | [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) |
| 高 | ByteDance 2025年売上$186B・純利益$48B・張一鳴43歳で中国首富・火山引擎企業級AI | [H-BTD-001](../config/hypotheses.json) 資本基盤の規模（C方向）. [H-BTD-002](../config/hypotheses.json) クロス補填構造の財務的裏付け | B-2 | [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) |
| 高 | 豆包DAU 2億突破・日次売上<100万元・毎日数千万元損失 | [H-BTD-001](../config/hypotheses.json) 規模優位維持（C方向）. [H-BTD-002](../config/hypotheses.json) 消費者AI経済的持続性への懸念 | B-2 | [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) |
| 高 | Seed Audio 1.0: 音声・効果音・環境音の統一フレームワーク・火山方舟でSeed Evolving/Seedance 2.0提供 | [H-BTD-001](../config/hypotheses.json) マルチモーダル製品拡張（C方向）. [H-BTD-002](../config/hypotheses.json) 企業インフラ並行拡大の証拠 | A-3 | [INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) |
| 高 | Coze agent platform・企業版私有化展開・中国AIエージェントプラットフォーム第7位 | [H-BTD-002](../config/hypotheses.json) 企業エージェントプラットフォーム基盤の拡大（C方向） | B-2/B-3 | [INFO-068](../Information/2026-07-23/collected-raw.md#INFO-068) [INFO-077](../Information/2026-07-30/collected-raw.md#INFO-077) |
| 高 | 豆包AI智能体手机（ByteDance×ZTE Nubia）・WAIC 2026展示・App→OS層へのAI入口拡張 | [H-BTD-001](../config/hypotheses.json) エコシステムハードウェア拡大（C方向） | B-2 | [INFO-049](../Information/2026-07-23/collected-raw.md#INFO-049) |
| 高 | Seedance 2.0業界初4モダリティ同時入力・Seedance 2.5 30秒動画・Seedance市場シェア80%超 | [H-BTD-001](../config/hypotheses.json) フロンティア能力・市場支配力（C方向）. Gemini Omni Flash首位奪取はI | A-3/B-2 | [INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) [INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) [INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) |
| 高 | 豆包エージェント機能7/15停止・ByteDance/Alibaba同時実施・「製品機能調整」 | [H-BTD-002](../config/hypotheses.json) EC/Agent収益化パス規制遮断の継続（I方向）. [H-BTD-003](../config/hypotheses.json) 規制インフラ拡大 | B-3/A-2 | [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) |
| 高 | 中国: 最先端AIモデル海外アクセス制限をAlibaba/ByteDance/Z.aiと協議・双方向AIデカップリング | [H-BTD-001](../config/hypotheses.json) グローバル展開の直接I証拠. [H-BTD-003](../config/hypotheses.json) 規制インフラ拡大C証拠 | A-2 | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) |
| 高 | WAICO設立: 中国が世界AI協力機構を設立し米国AI標準に挑戦・AIチャットボット規制強化 | [H-BTD-003](../config/hypotheses.json) 規制インフラの国際的次元拡大 | B-3 | [INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) |
| 高 | ByteDance 2026 AI CAPEX 2000億元超（前回記録）・Alibaba 4800億元検討・可霊AI ~$3B調達 | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（C方向）. [IND-029](../config/indicators.json) high/accelerating | B-2 | [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) |
| 高 | Seed 2.0 Pro/Lite/Mini追加・多モーダル深度思考能力拡張 | [H-BTD-001](../config/hypotheses.json) フロンティアモデル継続リリース（C方向） | A-3 | [INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) |
| 高 | Coze 3.0ゼロコード智能体開発プラットフォーム・ワークスペース/リソースライブラリ・DeepSeek統合 | [H-BTD-002](../config/hypotheses.json) エージェント代替プラットフォームの可能性（C方向） | B-3 | [INFO-098](../Information/2026-07-16/collected-raw.md#INFO-098) |
| 中 | $200億境外融資seeking・史上最大 | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（C方向） | A-2 | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 消費者DAUが減少に転じる（3ヶ月連続で2億を下回る） | [H-BTD-002](../config/hypotheses.json) ステートメント「相乗的並行拡大」の消費者軸が崩れる. 反証条件の片方が充足 | 90日 | [IND-011](../config/indicators.json) |
| 企業Token経済（火山方舟・Coze）の成長が停止する | [H-BTD-002](../config/hypotheses.json) ステートメントの企業軸が崩れる. 反証条件の片方が充足 | 90日 | [IND-010](../config/indicators.json) |
| 中国の海外AIモデルアクセス制限が実施され, オープンソース配布が停止される | [H-BTD-001](../config/hypotheses.json) のグローバル展開前提が崩壊. 確度大幅下方修正 | 90日 | [IND-011](../config/indicators.json) |
| 7/15エージェント機能停止が恒久的であることが確認される | [H-BTD-002](../config/hypotheses.json) の企業インフラ成長経路（Coze代替）の妥当性が問われる | 60日 | [IND-010](../config/indicators.json) |
| ByteDanceのグローバルAI展開（Doubao/Seed海外版・現地語対応・海外サーバー）が独立確認される | [H-BTD-001](../config/hypotheses.json) の「グローバル展開証拠欠落」判断が崩れる | 180日 | [IND-011](../config/indicators.json) |
| 中国規制当局がByteDanceのAIサービスライセンスを取り消す・停止する | [H-BTD-001](../config/hypotheses.json)・[H-BTD-002](../config/hypotheses.json) の両方が崩れる | 60日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持し、グローバル展開を図る | 64% medium | ±0%. MAU 5.28億・過去最高([INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2)・$700億AI投資計画([INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2)・$186B売上([INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2)・Seed Audio 1.0([INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) A-3)・Coze企業基盤([INFO-068](../Information/2026-07-23/collected-raw.md#INFO-068) B-2)・豆包AI智能体手机([INFO-049](../Information/2026-07-23/collected-raw.md#INFO-049) B-2)・Seedance市場シェア80%超で規模・製品力維持（C方向）. 但し中国海外アクセス制限協議(INFO-084 A-2)・Gemini Omni Flash首位奪取(INFO-064 B-1)はI証拠. ミラーイメージング警告継続 | [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) [INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) [INFO-049](../Information/2026-07-23/collected-raw.md#INFO-049) | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは消費者基盤（豆包DAU 2億）と企業インフラ（火山方舟・Coze・Seed Audio）の相乗的並行拡大を展開している。消費者DAUと企業Token経済が同時に成長する構造であり、消費者から企業への「移行」ではない。但し日次赤字（数千万元）が消費者ビジネスの経済的持続性に懸念を呈している。反証条件: 消費者DAUが減少に転じる、または企業Token経済の成長が停止する場合、本フレームの再評価が必要 | 36% low | ±0%. Blue +1%提案がArbiter v4.49/v4.50/v4.51で3R連続却下. MAU 5.28億・過去最高（消費者軸）と$700億投資・Coze企業版（企業軸）のデュアルアクシス拡大確認. 但し3条件が3R未解消: (1)出所独立性疑義（ByteDance自己開示）・(2)保護市場・(3)投資≠成果. Arbiter v4.50絶対条件「DAU差異技術的説明」は[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2で部分的解消（ピーク vs 持続的・測定対象・定義の違いを初めて説明）したが完全解消未達. 保守的下限採用継続. 日次赤字数千万元([INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2)・エージェント機能7/15停止で消費者持続性懸念継続. 反証条件明示で旧AND構造の反証不可能性を部分的解消 | [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) [INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) | [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受け、グローバル展開が制限される | 40% medium | ±0%. 中国海外アクセス制限協議(INFO-084 A-2)・AIエージェント規則7/15執行可能(INFO-038 B-1)・WAICO設立(INFO-039 B-3)・エージェント機能7/15終了(INFO-082 A-2)で規制インフラ拡大蓄積. 但し核心命題は著作権問題であり, 著作権関連の新規A-2+証拠は確認されず. Seedance 2.0はハリウッド6スタジオ警告で全球上線自停の歴史あり | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) [INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) | (著作権領域での新規A-2+証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | elevated. 豆包MAU 5.28億・2026年6月過去最高（[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）・DAUピーク1.45億（春節）vs 持続的~8000万（AI検索）. DAU差異技術的説明部分的解消. Seed 2.0 Code 256Kコンテキスト（[INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) A-1）・Seed Audio 1.0([INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) A-3)・Seedance市場シェア80%超. 但しGemini Omni Flash首位奪取・エージェント機能7/15終了で制約. A-1証拠出所独立性リスク（Arbiter v4.49記録） | 2026-07-30 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・日コスト赤字拡大でhigh | high. 日次売上<100万元 vs 日次コスト数千万元([INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2)・エージェント機能7/15終了([INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013)・[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082))・ByteDance CAPEX $700億計画([INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2)・$186B売上でクロス補填([INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2)・火山方舟企業Token経済成長([INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) A-3) | 2026-07-30 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | high/accelerating. ByteDance $186B売上$48B純利益([INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2)・2026年最大$700億AI投資計画([INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2)・AI Rack 3.0兆瓦級計算システム([INFO-061](../Information/2026-07-18/collected-raw.md#INFO-061) A-3)・$200億境外融資seeking([INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) A-2) | 2026-07-30 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | critical/deepening. 中国海外AIモデルアクセス制限協議([INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2)・エージェント機能7/15終了([INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2)・WAICO設立・AIチャットボット規制強化([INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) B-3) | 2026-07-30 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-30 | ターゲット編集. 豆包MAU 5.28億・2026年6月過去最高（前回3.82億から+38%, [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）. ByteDance最大$700億AIインフラ投資計画（前回~2000億元から2.5x, [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）. DAU差異技術的説明初確認（ピーク1.45億 vs 持続的~8000万・測定対象・定義の違い）. Arbiter v4.51がH-BTD-002 +1%提案を3R連続却下（出所独立性・保護市場・投資≠成果の3条件3R未解消・DAU差異技術的説明はINFO-068で部分的解消だが完全解消未達）. 仮説確度は全て±0%据え置き. Arbiter v4.51 COMPLETE | [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-28 | ターゲット編集. Seed 2.0 Code 256Kコンテキスト（[INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) A-1）・豆包MAU 3.82億/+172% YoY（[INFO-089](../Information/2026-07-28/collected-raw.md#INFO-089) A-1）のデュアルアクシスA-1品質確認. Arbiter v4.49がH-BTD-002 +1%提案を却下（出所独立性疑義・二重カウント・ミラーイメージングリスク）. H-BTD-002 37→36%（v4.46段階的引き下げ反映）. Arbiter v4.49 COMPLETE | [INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) [INFO-089](../Information/2026-07-28/collected-raw.md#INFO-089) | H-BTD-001 64%(±0%)・H-BTD-002 37→36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-23 | ターゲット編集. [H-BTD-002](../config/hypotheses.json) 第2回ステートメント修正実行（v4.39-v4.42累積絶対条件完了）: 「移行過程」→「相乗的並行拡大」. $186B売上$48B純利益([INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2)・豆包DAU 2億/日次赤字([INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2)・Seed Audio 1.0([INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) A-3)・Coze企業基盤([INFO-068](../Information/2026-07-23/collected-raw.md#INFO-068) B-2)・豆包AI智能体手机([INFO-049](../Information/2026-07-23/collected-raw.md#INFO-049) B-2)を新規反映. 仮説確度は全て±0%据え置き. Arbiter v4.43 COMPLETE | [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) [INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) | H-BTD-001 64%(±0%)・H-BTD-002 37%(±0%, ステートメント修正)・H-BTD-003 40%(±0%) |
| 2026-07-18 | ターゲット編集. [H-BTD-002](../config/hypotheses.json) 第1回ステートメント修正（v4.38絶対条件1実行, v4.39確認）: 「Freemium+ECシナジーモデルを維持」→「企業サービスへの移行過程」. 豆包DAU 2億突破・Seedance 2.5・Coze 3.0・ArkClawを反映. Arbiter v4.39 COMPLETE | [INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) [INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) | H-BTD-001 64%(±0%)・H-BTD-002 38→37%(ステートメント修正)・H-BTD-003 40%(±0%) |
| 2026-07-16 | 全面書き直し. Seed 2.0 Pro/Lite/Mini追加・Seedance 2.0業界初4モダリティ・Coze 3.0・Seedance市場シェア80%超・DeepSeek IPO準備・豆包AI智能体手机を新規反映. 仮説確度は全て±0%据え置き. Arbiter v4.37 COMPLETE | [INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) [INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) | H-BTD-001 64%(±0%)・H-BTD-002 38%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-10 | 全面書き直し. 中国海外AIモデルアクセス制限協議・豆包日コスト範囲精緻化・エージェント機能7/15終了正式確認・CAPEX 2000億元超を反映. Arbiter v4.31 COMPLETE | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) | H-BTD-001 64%(±0%)・H-BTD-002 38%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-07 | ターゲット編集. AIコンパニオン規則エージェント機能強制削除・日次トークン180兆・有料機能開始・Kling調達/Seedance調達不可能を反映. [H-BTD-002](../config/hypotheses.json) 42→38% | [INFO-056](../Information/2026-07-07/collected-raw.md#INFO-056) | H-BTD-002 42→38% |
| 2026-06-30 | ターゲット編集. $200億境外融資seeking・日算力費vs日収入ギャップ数十倍・戦略ピボットを反映. [H-BTD-002](../config/hypotheses.json) 43→42% | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) | H-BTD-002 43→42% |
| 2026-06-20 | [H-BTD-002](../config/hypotheses.json) 操作化再定義執行. EC 81.1%収益化のI誤分類を是正. 全面書き直し | [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) | H-BTD-002 46→44% |

## 7. ブラインドスポット

- 7/15エージェント機能停止（[INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) B-3・[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）が一時的か恒久的かの判別が不能. 一時的であればI証拠の重みは減じ, 恒久的であれば[H-BTD-002](../config/hypotheses.json)の企業インフラ成長経路（Coze代替）の妥当性が問われる.
- 中国の海外AIモデルアクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）が実施されるか, 協議段階で終わるかの判別が不能. オープンソースモデルは配布後に制御困難であり, 実効性に疑義がある. 但し実施された場合の[H-BTD-001](../config/hypotheses.json)への影響は大きい.
- 豆包MAUにソース間で乖離があったが, [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068)（A-2）がDAU差異の技術的説明を初めて提供した: ピーク1.45億（春節期間）vs 持続的~8000万（AI検索領域）は測定対象・時期・定義の違いによる. これにより長年のDAU不確実性が部分的に解消された. 但しMAU/DAU比の正確な計算は依然として不可能（MAU 5.28億に対する持続的DAUが8000万ならDAU/MAU比は15.2%, ピーク1.45億なら27.5%）.
- 日次コスト数千万元（[INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2）の算出方法が外部から検証できない. 火山引擎API価格からの推算の可能性があり, 実際の限界コストを過大評価している可能性.
- $186B売上（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2）の内訳が公開されていない. 消費者AI赤字をTikTok/抖音広告収益でクロス補填する構造の定量分解が不能.
- $700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）は「最大」表記であり, 実際の投資額は確定しない. 投資計画と実行成果の乖離は未知数. Arbiter v4.51が「投資≠成果」をH-BTD-002 +1%却下3条件の一つとして継続.
- Seed 2.0・Seedance 2.0の能力は火山引擎公式ドキュメント・API仕様ベース（[INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101)・[INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) A-3）であり, 独立ベンチマークでの検証が未完了. Seedance市場シェア80%超の測定方法・定義も不明.
- ミラーイメージングリスクを統合判断が明示的に認めた. 西側の「赤字=持続不能」という財務基準を, EC・広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめると, モデルの優位を見落とす. 逆に過大に考慮すると赤字の実相を過小評価する. 判別手段がない.
- ByteDanceグローバルAI戦略への中国共産党の介入度が見えない. WAICO設立・対外投資規制・海外アクセス制限協議は党の関与の兆候だが, AI部門への介入の実態は公開情報にない.

- Seed 2.0 Code 256K・MAU 3.82億/+172%のA-1品質証拠（[INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087)・[INFO-089](../Information/2026-07-28/collected-raw.md#INFO-089)）がByteDance自己開示ベースであり, 第三者測定による独立検証が不在. Arbiter v4.49が「単一A-1証拠の3件変更提案基盤への集中リスク」として構造的記録し, H-BTD-002 +1%提案を却下した. MAU 5.28億（[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）も中国メディア報道ベースであり, 自己開示データの系統的過大申告リスクと, 中国情報源の限定による独立裏付け不在が, H-BTD-001/002の確度評価の上限を構造的に制約する.

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) | 豆包MAU 5.28億・2026年6月過去最高・DAUピーク1.45億 vs 持続的~8000万・DAU差異技術的説明(A-2) |
| [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) | ByteDance最大$700億AIインフラ投資2026・DeepSeek評価額$500億超・OceanBase融資(A-2) |
| [INFO-077](../Information/2026-07-30/collected-raw.md#INFO-077) | Coze低コードエージェントプラットフォーム・企業版私有化展開・中国第7位(B-3) |
| [INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) | Seed 2.0 Code 256Kコンテキスト・Seedance 2.0・企業軸A-1品質(A-1) |
| [INFO-089](../Information/2026-07-28/collected-raw.md#INFO-089) | 豆包MAU 3.82億/+172% YoY・消費者軸A-1品質・出所独立性リスク(A-1) |
| [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) | ByteDance 2025年売上$186B・純利益$48B・張一鳴中国首富・火山引擎企業級AI(B-2) |
| [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) | 豆包DAU 2億・MAU 3.82億・日次売上<100万元・毎日数千万元損失・WAIC DAA新指標(B-2) |
| [INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) | Seed Audio 1.0音声・効果音・環境音統一フレームワーク・火山方舟Seed Evolving/Seedance(A-3) |
| [INFO-068](../Information/2026-07-23/collected-raw.md#INFO-068) | Coze agent platform vs Dify・Seedance 2.0 4モダリティ・即梦統合(B-2) |
| [INFO-049](../Information/2026-07-23/collected-raw.md#INFO-049) | 豆包AI智能体手机 ByteDance×ZTE Nubia・WAIC 2026・App→OS層拡張(B-2) |
| [INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) | WAICO設立: 中国が世界AI協力機構を設立・AIチャットボット規制強化(B-3) |
| [INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) | Doubao Seed 2.0 Pro/Lite/Mini追加・多モーダル深度思考能力拡張(A-3) |
| [INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) | Seedance 2.0/2.5業界初4モダリティ同時入力・最大50秒動画・4K/Mini版・API公開(A-3) |
| [INFO-099](../Information/2026-07-16/collected-raw.md#INFO-099) | Seedance市場シェア80%超・快手可霊AI $30億調達（評価額$180億）(B-2) |
| [INFO-094](../Information/2026-07-16/collected-raw.md#INFO-094) | 豆包MAU 3.45億・日活2億突破・国内C端AI首位(B-2) |
| [INFO-098](../Information/2026-07-16/collected-raw.md#INFO-098) | Coze 3.0ゼロコード智能体開発プラットフォーム・DeepSeek統合(B-3) |
| [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) | ByteDance/Alibaba Doubao・Qwenエージェント機能7月15日停止(B-3) |
| [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) | 豆包エージェント機能7/15終了正式確認(A-2) |
| [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) | 中国: 最先端AIモデル海外アクセス制限をAlibaba/ByteDance/Z.aiと協議(A-2) |
| [INFO-085](../Information/2026-07-10/collected-raw.md#INFO-085) | 豆包日活1.4億・日収<100万元CNY vs 日コスト1.3〜2.4億元・ギャップ数百倍(B-2) |
| [INFO-087](../Information/2026-07-10/collected-raw.md#INFO-087) | ByteDance 2026 AI CAPEX 2000億元超・Alibaba 4800億元検討(B-2) |
| [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) | $200億境外融資seeking・史上最大(A-2) |
| [Arbiter v4.51](../state/arbiter-2026-07-30.md) | 確度評価の完全根拠・H-BTD-002 +1%却下3R連続記録・DAU差異技術的説明部分的解消記録 |
