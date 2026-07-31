# ByteDance

> 最終判断更新: 2026-07-31
> 全体確信度: 中
> 情報非対称性: ByteDance内部の財務データが外部検証不可能. 日コスト1.3〜2.4億元は36kr等の報道に基づく推算であり, 実際の限界コストを過大評価する可能性がある. 豆包MAUにソース間で乖離が存在したが, [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2がDAU差異の技術的説明（ピーク vs 持続的・測定対象・時期・定義の違い）を初めて提供し, 長年のDAU不確実性が部分的に解消された. 但し完全解消には至らず, 持続的DAUの正確な数値は依然として不確確実. $700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）は史上最大規模だが, 投資計画と実行のギャップは未知数. Seed 2.0 Code 256K・Seedance 2.0の能力評価はByteDance自家測定・API仕様ベースであり, 独立ベンチマークでの検証が未完了. 7/30組織再編の効果は発表段階であり実行結果は未知数. エージェント機能7/15終了が一時的か恒久的かの判別が不能. 中国情報源の限定により独立裏付けなし
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-010](../config/indicators.json) [IND-011](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

ByteDanceは豆包MAU 5.28億（2026年6月・過去最高・[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）で消費者基盤を拡大しつつ, 2026年に最大$700億をAIインフラに投入する計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）を発表した. 前回記録のMAU 3.82億から+38%成長し, DAUピーク1.45億（春節）の技術的説明も初めて確認された. 7月30日には豆包・飛書・火山エンジンの3大事業を統合する組織再編を開始し（[INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) A-2）, 消費者AIと企業インフラの組織的融合を制度化した. 新設の「創造力サービスプラットフォーム部」がToB事業の顧客サービス能力を統合し, AI toB戦略の優先度を引き上げた. 2025年売上$186B・純利益$48B（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2）はTikTok/抖音広告収益が消費者赤字をクロス補填する構造を示す. ただし日次売上<100万元 vs 日次コスト数千万元のギャップ（[INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2）は消費者AIビジネス単体の経済的持続性に懸念を呈している. Seed 2.0 Code 256Kはコーディング市場参入の意欲を示すが, A-1品質証拠の出所独立性（ByteDance自己開示）に構造的リスクが記録されている.

[H-BTD-001](../config/hypotheses.json) 64% medium（±0%, v4.52）・[H-BTD-002](../config/hypotheses.json) 36% low（±0%, Blue +1%提案がv4.49/v4.50/v4.51/v4.52で4R連続却下・出所独立性・保護市場・投資≠成果の3条件未解消）・[H-BTD-003](../config/hypotheses.json) 40% medium（±0%）. H-BTD-002のステートメントは「消費者基盤と企業インフラの相乗的並行拡大」. 7/30組織再編はこのステートメントの組織的裏付けとして機能するが, 出所独立性（ByteDance自己開示ベース）・保護市場・投資≠成果の3条件が4R連続未解消であり, +1%提案は継続して却下されている. 反証条件（消費者DAU減少または企業Token経済成長停止）が明示されている.

## 1. コア判断

本ラウンドの構造的変化は7月30日の組織再編である（[INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) A-2）. ByteDanceが豆包（消費者AI）・飛書（企業コラボレーション）・火山エンジン（クラウドインフラ）の製品開発チームと商業化システムを統合し, 新設の「創造力サービスプラットフォーム部」がToB事業の顧客サービス能力を一元化した. 飛書製品チームと豆包製品チームの統合は, これまで別々の事業ラインとして運営されてきた消費者向けAIと企業向けインフラの組織的融合を意味する.

この再編は[H-BTD-002](../config/hypotheses.json)のステートメント「消費者基盤と企業インフラの相乗的並行拡大」の組織的裏付けとして読める. 消費者AI（豆包）と企業コラボレーション（飛書）とクラウドインフラ（火山エンジン）が同一の製品開発組織の下に置かれることで, データ・モデル・インフラの共有が組織的に可能になる. ただし発表段階であり, 統合が実際の製品統合や収益シナジーにつながるかは未知数である. [H-BTD-002](../config/hypotheses.json) +1%提案は出所独立性疑義（ByteDance自己開示ベースの中国メディア報道）・保護市場・投資≠成果の3条件が4R連続未解消として, Arbiter v4.52で再び却下された.

前回記録の豆包MAU 5.28億・過去最高更新（[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）と$700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）の文脈にこの再編を置くと, ByteDanceが消費者AIの規模優位を企業インフラの収益化に転換する組織的基盤を構築している像が見える. 火山引擎が企業級クラウド・AIサービスプラットフォームとして大モデル・データインテリジェンス・推薦アルゴリズム・音声動画技術を提供し, Coze企業プラットフォーム（[INFO-077](../Information/2026-07-30/collected-raw.md#INFO-077) B-3）の低コードエージェント開発機能で企業向け私有化展開も進む. この全体収益構造の中で, 豆包の消費者AI赤字（日次売上<100万元 vs 日次コスト数千万元, [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2）はTikTok/抖音の広告収益でクロス補填されている可能性が高い.

中国3社（ByteDance・Alibaba・Tencent）が旗艦AIアプリからエージェントマーケットプレイスを削除した中で（[INFO-014](../Information/2026-07-31/collected-raw.md#INFO-014) C-2）, ByteDanceはCoze・Trae・ArkClaw・Feishu Miaodaを維持し, 火山引擎はLanceDB上にAIデータスタックを再構築して100K+ QPSでエージェントメモリを駆動している. エージェントマーケットプレイスの削除が規制対応か戦略転換かは判別不能だが, ByteDanceがエージェント機能の維持を選んだ点は企業インフラ戦略の継続性を示す. FCCが中国製ヒューマノイド・四足ロボットの新規輸入を禁止したこと（[INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) B-2）は, ハードウェア領域での米中分離が深化している傍証であり, ソフトウェア領域での中国製安価AIモデルのアジア市場優位（CNBC報道）と両立している.

[H-BTD-001](../config/hypotheses.json) は64% mediumで±0%（v4.52）. 豆包MAU 5.28億・過去最高更新・$700億AI投資計画・Seed Audio 1.0・Coze企業プラットフォーム・豆包AI智能体手机・Seedance市場シェア80%超・ByteDance $186B売上で規模・製品力の維持（C方向）が確認された. 組織再編はAI toB戦略の優先度引き上げを示す追加的C証拠である. ただし中国の海外アクセス制限協議・Gemini Omni Flash首位奪取がI証拠として継続する.

[H-BTD-002](../config/hypotheses.json) は36% low（±0%, Blue +1%提案がv4.49/v4.50/v4.51/v4.52で4R連続却下）. 組織再編は「相乗的並行拡大」ステートメントの組織的裏付けとして機能する. ただしArbiter v4.52は出所独立性疑義（ByteDance自己開示ベースの中国メディア報道）・保護市場・投資≠成果の3条件が4R未解消として+1%提案を再び却下した. DAU差異技術的説明は[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068)（07-30バッチ）で部分的解消したが完全解消未達. 日次赤字数千万元・エージェント機能7/15停止で消費者持続性懸念継続.

[H-BTD-003](../config/hypotheses.json) は40% mediumで±0%（v4.52）. 中国の海外AIモデルアクセス制限協議・エージェント機能7/15終了・AIエージェント規則7/15執行可能・WAICO設立で規制インフラ拡大の証拠が蓄積した. FCCの中国製ロボット輸入禁止（[INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) B-2）は規制インフラの拡大を示す追加的証拠である. ただし核心命題は著作権問題による法的制約であり, 著作権関連の新規A-2+証拠は今ラウンドでも確認されなかった.

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | ByteDance 7/30組織再編: 豆包・飛書・火山エンジンの製品開発統合・新設「創造力サービスプラットフォーム部」・AI toB戦略優先度引き上げ | [H-BTD-002](../config/hypotheses.json) 「相乗的並行拡大」ステートメントの組織的裏付け（C方向）. 但し発表段階・出所独立性疑義継続 | A-2 | [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) |
| 高 | ByteDance 2026年最大$700億AIインフラ投資計画（前回CAPEX ~2000億元から2.5x拡大） | [H-BTD-001](../config/hypotheses.json) 資本基盤の飛躍的拡大（C方向）. [H-BTD-002](../config/hypotheses.json) 企業インフラ投資軸強化（C方向）だが投資≠成果リスク. [IND-029](../config/indicators.json) high/accelerating | A-2 | [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) |
| 高 | 豆包MAU 5.28億・2026年6月過去最高（前回3.82億から+38%）. DAUピーク1.45億（春節）vs 持続的~8000万（AI検索） | [H-BTD-001](../config/hypotheses.json) 規模優位拡大（C方向）. [H-BTD-002](../config/hypotheses.json) 消費者軸成長確認・DAU差異技術的説明で絶対条件部分的解消 | A-2 | [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) |
| 高 | 中国3社が旗艦AIアプリからエージェントマーケットプレイス削除・ByteDanceはCoze/Trae/ArkClaw/Feishu Miaoda維持・火山引擎がLanceDB上にAIスタック再構築 | [H-BTD-002](../config/hypotheses.json) エージェントインフラ維持の選択（C方向）. 規制対応か戦略転換かは判別不能 | C-2 | [INFO-014](../Information/2026-07-31/collected-raw.md#INFO-014) |
| 高 | ByteDance 2025年売上$186B・純利益$48B・張一鳴43歳で中国首富・火山引擎企業級AI | [H-BTD-001](../config/hypotheses.json) 資本基盤の規模（C方向）. [H-BTD-002](../config/hypotheses.json) クロス補填構造の財務的裏付け | B-2 | [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) |
| 高 | 豆包DAU 2億突破・日次売上<100万元・毎日数千万元損失 | [H-BTD-001](../config/hypotheses.json) 規模優位維持（C方向）. [H-BTD-002](../config/hypotheses.json) 消費者AI経済的持続性への懸念 | B-2 | [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) |
| 高 | Seed Audio 1.0: 音声・効果音・環境音の統一フレームワーク・火山方舟でSeed Evolving/Seedance 2.0提供 | [H-BTD-001](../config/hypotheses.json) マルチモーダル製品拡張（C方向）. [H-BTD-002](../config/hypotheses.json) 企業インフラ並行拡大の証拠 | A-3 | [INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) |
| 高 | Coze agent platform・企業版私有化展開・中国AIエージェントプラットフォーム第7位 | [H-BTD-002](../config/hypotheses.json) 企業エージェントプラットフォーム基盤の拡大（C方向） | B-2/B-3 | [INFO-068](../Information/2026-07-23/collected-raw.md#INFO-068) [INFO-077](../Information/2026-07-30/collected-raw.md#INFO-077) |
| 高 | 豆包AI智能体手机（ByteDance×ZTE Nubia）・WAIC 2026展示・App→OS層へのAI入口拡張 | [H-BTD-001](../config/hypotheses.json) エコシステムハードウェア拡大（C方向） | B-2 | [INFO-049](../Information/2026-07-23/collected-raw.md#INFO-049) |
| 高 | Seedance 2.0業界初4モダリティ同時入力・Seedance 2.5 30秒動画・Seedance市場シェア80%超 | [H-BTD-001](../config/hypotheses.json) フロンティア能力・市場支配力（C方向）. Gemini Omni Flash首位奪取はI | A-3/B-2 | [INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) [INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) [INFO-071](../Information/2026-07-18/collected-raw.md#INFO-071) |
| 高 | 豆包エージェント機能7/15停止・ByteDance/Alibaba同時実施・「製品機能調整」 | [H-BTD-002](../config/hypotheses.json) EC/Agent収益化パス規制遮断の継続（I方向）. [H-BTD-003](../config/hypotheses.json) 規制インフラ拡大 | B-3/A-2 | [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) |
| 高 | 中国: 最先端AIモデル海外アクセス制限をAlibaba/ByteDance/Z.aiと協議・双方向AIデカップリング | [H-BTD-001](../config/hypotheses.json) グローバル展開の直接I証拠. [H-BTD-003](../config/hypotheses.json) 規制インフラ拡大C証拠 | A-2 | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-043](../Information/2026-07-10/collected-raw.md#INFO-043) |
| 高 | FCC: 中国製ヒューマノイド・四足ロボット新規輸入禁止・中国製パワーインバーターも禁止 | [H-BTD-003](../config/hypotheses.json) 規制インフラ拡大・米中分離深化. ソフトウェア領域での中国製安価AIモデルのアジア優位と両立 | B-2 | [INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) |
| 高 | WAICO設立: 中国が世界AI協力機構を設立し米国AI標準に挑戦・AIチャットボット規制強化 | [H-BTD-003](../config/hypotheses.json) 規制インフラの国際的次元拡大 | B-3 | [INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) |
| 中 | $200億境外融資seeking・史上最大 | [H-BTD-001](../config/hypotheses.json) 資本基盤拡大（C方向） | A-2 | [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 消費者DAUが減少に転じる（3ヶ月連続で2億を下回る） | [H-BTD-002](../config/hypotheses.json) ステートメント「相乗的並行拡大」の消費者軸が崩れる. 反証条件の片方が充足 | 90日 | [IND-011](../config/indicators.json) |
| 企業Token経済（火山方舟・Coze）の成長が停止する | [H-BTD-002](../config/hypotheses.json) ステートメントの企業軸が崩れる. 反証条件の片方が充足 | 90日 | [IND-010](../config/indicators.json) |
| 中国の海外AIモデルアクセス制限が実施され, オープンソース配布が停止される | [H-BTD-001](../config/hypotheses.json) のグローバル展開前提が崩壊. 確度大幅下方修正 | 90日 | [IND-011](../config/indicators.json) |
| 7/15エージェント機能停止が恒久的であることが確認される | [H-BTD-002](../config/hypotheses.json) の企業インフラ成長経路（Coze代替）の妥当性が問われる | 60日 | [IND-010](../config/indicators.json) |
| 7/30組織再編が実行されず形骸化する, または統合効果が定量で確認できない | [H-BTD-002](../config/hypotheses.json) の組織的裏付けが無効化され, +1%条件から除外される | 180日 | [IND-010](../config/indicators.json) |
| ByteDanceのグローバルAI展開（Doubao/Seed海外版・現地語対応・海外サーバー）が独立確認される | [H-BTD-001](../config/hypotheses.json) の「グローバル展開証拠欠落」判断が崩れる | 180日 | [IND-011](../config/indicators.json) |
| 中国規制当局がByteDanceのAIサービスライセンスを取り消す・停止する | [H-BTD-001](../config/hypotheses.json)・[H-BTD-002](../config/hypotheses.json) の両方が崩れる | 60日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持し、グローバル展開を図る | 64% medium | ±0%（v4.52）. MAU 5.28億・過去最高（[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）・$700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）・$186B売上（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2）・Seed Audio 1.0（[INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) A-3）・Coze企業基盤・豆包AI智能体手机・Seedance市場シェア80%超で規模・製品力維持（C方向）. 7/30組織再編（[INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) A-2）はAI toB優先度引き上げの追加C証拠. 但し中国海外アクセス制限協議・Gemini Omni Flash首位奪取はI証拠. ミラーイメージング警告継続 | [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-064](../Information/2026-07-18/collected-raw.md#INFO-064) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは消費者基盤（豆包DAU 2億）と企業インフラ（火山方舟・Coze・Seed Audio）の相乗的並行拡大を展開している. 7/30組織再編が消費者AI（豆包）・企業コラボレーション（飛書）・クラウドインフラ（火山エンジン）の組織的融合を制度化した. 反証条件: 消費者DAUが減少に転じる、または企業Token経済の成長が停止する場合、本フレームの再評価が必要 | 36% low | ±0%（v4.52）. Blue +1%提案がv4.49/v4.50/v4.51/v4.52で4R連続却下. 7/30組織再編（[INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) A-2）は「相乗的並行拡大」ステートメントの組織的裏付け（C方向）. MAU 5.28億・過去最高（消費者軸）と$700億投資・Coze企業版（企業軸）のデュアルアクシス拡大確認. 但し3条件が4R未解消: (1)出所独立性疑義（中国メディア報道ベース・ByteDance自己開示の系統的過大申告リスク）・(2)保護市場・(3)投資≠成果. DAU差異技術的説明は[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068)（07-30バッチ）で部分的解消したが完全解消未達. 日次赤字数千万元・エージェント機能7/15停止で消費者持続性懸念継続 | [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) [INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) | [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受け、グローバル展開が制限される | 40% medium | ±0%（v4.52）. 中国海外アクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）・エージェント規則7/15執行可能（[INFO-038](../Information/2026-07-18/collected-raw.md#INFO-038) B-1）・WAICO設立（[INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) B-3）・エージェント機能7/15終了（[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）・FCC中国製ロボット輸入禁止（[INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) B-2）で規制インフラ拡大蓄積. 但し核心命題は著作権問題であり, 著作権関連の新規A-2+証拠は確認されず | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) [INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) | (著作権領域での新規A-2+証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-011](../config/indicators.json) | 中国AI性能到達（Doubao MAU・DAU・ベンチマーク） | DAU 3ヶ月連続大幅減少またはMAU持続的低下でelevated | elevated. 豆包MAU 5.28億・2026年6月過去最高（[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）・DAUピーク1.45億（春節）vs 持続的~8000万（AI検索）. DAU差異技術的説明部分的解消. Seed 2.0 Code 256Kコンテキスト（[INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) A-1）・Seed Audio 1.0・Seedance市場シェア80%超. 但しGemini Omni Flash首位奪取・エージェント機能7/15終了で制約. A-1証拠出所独立性リスク | 2026-07-31 |
| [IND-010](../config/indicators.json) | 新興国AI価格競争・収益化モデル | EC転換率急落・日コスト赤字拡大でhigh | high. 日次売上<100万元 vs 日次コスト数千万元（[INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2）・エージェント機能7/15終了（[INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013)・[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082)）・ByteDance CAPEX $700億計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）・$186B売上でクロス補填（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2）・火山方舟企業Token経済成長（[INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) A-3）・7/30組織再編でToB統合（[INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) A-2） | 2026-07-31 |
| [IND-029](../config/indicators.json) | AIインフラ制約（資本流入） | 資本流入劇的加速でhigh | high/accelerating. ByteDance $186B売上$48B純利益（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2）・2026年最大$700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）・AI Rack 3.0兆瓦級計算システム（[INFO-061](../Information/2026-07-18/collected-raw.md#INFO-061) A-3）・$200億境外融資seeking（[INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) A-2） | 2026-07-31 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | critical/deepening. 中国海外AIモデルアクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）・エージェント機能7/15終了（[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）・WAICO設立・AIチャットボット規制強化（[INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) B-3）・FCC中国製ロボット輸入禁止（[INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) B-2） | 2026-07-31 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-31 | 構造的変化反映. 7/30組織再編（豆包・飛書・火山エンジン統合・新設「創造力サービスプラットフォーム部」・AI toB優先度引き上げ, [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) A-2）を新規反映. §0/§1/§2に組織再編の構造的意味を追加. §3に組織再編形骸化の反証条件を追加. 中国3社エージェントマーケットプレイス削除・ByteDance維持（[INFO-014](../Information/2026-07-31/collected-raw.md#INFO-014) C-2）・FCC中国製ロボット輸入禁止（[INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) B-2）を追加. 仮説確度は全て±0%据え置き（v4.52 COMPLETE）. KIQ-OAI-001 38R/39R・KIQ-MIL-001 38R/39R | [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) [INFO-014](../Information/2026-07-31/collected-raw.md#INFO-014) [INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-30 | ターゲット編集. 豆包MAU 5.28億・2026年6月過去最高（前回3.82億から+38%, [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）. ByteDance最大$700億AIインフラ投資計画（前回~2000億元から2.5x, [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）. DAU差異技術的説明初確認. Arbiter v4.51がH-BTD-002 +1%提案を3R連続却下. 仮説確度は全て±0%据え置き | [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-28 | ターゲット編集. Seed 2.0 Code 256Kコンテキスト（[INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) A-1）・豆包MAU 3.82億/+172% YoY（[INFO-089](../Information/2026-07-28/collected-raw.md#INFO-089) A-1）のデュアルアクシスA-1品質確認. Arbiter v4.49がH-BTD-002 +1%提案を却下. H-BTD-002 37→36% | [INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) [INFO-089](../Information/2026-07-28/collected-raw.md#INFO-089) | H-BTD-001 64%(±0%)・H-BTD-002 37→36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-23 | ターゲット編集. [H-BTD-002](../config/hypotheses.json) 第2回ステートメント修正実行: 「移行過程」→「相乗的並行拡大」. $186B売上$48B純利益・豆包DAU 2億/日次赤字・Seed Audio 1.0・Coze企業基盤・豆包AI智能体手机を新規反映 | [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) | H-BTD-001 64%(±0%)・H-BTD-002 37%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-18 | ターゲット編集. [H-BTD-002](../config/hypotheses.json) 第1回ステートメント修正: 「維持」→「移行過程」. 豆包DAU 2億突破・Seedance 2.5・Coze 3.0・ArkClawを反映 | [INFO-062](../Information/2026-07-18/collected-raw.md#INFO-062) | H-BTD-001 64%(±0%)・H-BTD-002 38→37%・H-BTD-003 40%(±0%) |
| 2026-07-16 | 全面書き直し. Seed 2.0 Pro/Lite/Mini追加・Seedance 2.0業界初4モダリティ・Coze 3.0・Seedance市場シェア80%超を新規反映 | [INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) | H-BTD-001 64%(±0%)・H-BTD-002 38%(±0%)・H-BTD-003 40%(±0%) |

## 7. ブラインドスポット

- 7/30組織再編（[INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) A-2）は発表段階であり, 統合が実際の製品統合や収益シナジーにつながるかは未知数. 組織図の変更と実行成果の間には通常時間差があり, 中国企業の組織再編は政治的文脈（規制圧力・党内調整）で実施される場合がある. 再編の動機が市場戦略的か規制対応かの判別が不能.
- 7/15エージェント機能停止（[INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) B-3・[INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) A-2）が一時的か恒久的かの判別が不能. 一時的であればI証拠の重みは減じ, 恒久的であれば[H-BTD-002](../config/hypotheses.json)の企業インフラ成長経路（Coze代替）の妥当性が問われる.
- 中国の海外AIモデルアクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）が実施されるか, 協議段階で終わるかの判別が不能. オープンソースモデルは配布後に制御困難であり, 実効性に疑義がある. 但し実施された場合の[H-BTD-001](../config/hypotheses.json)への影響は大きい.
- 豆包MAUにソース間で乖離があったが, [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068)（A-2）がDAU差異の技術的説明を初めて提供した. 但しMAU/DAU比の正確な計算は依然として不可能（MAU 5.28億に対する持続的DAUが8000万ならDAU/MAU比は15.2%, ピーク1.45億なら27.5%）.
- 日次コスト数千万元（[INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) B-2）の算出方法が外部から検証できない. 火山引擎API価格からの推算の可能性があり, 実際の限界コストを過大評価している可能性.
- $186B売上（[INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) B-2）の内訳が公開されていない. 消費者AI赤字をTikTok/抖音広告収益でクロス補填する構造の定量分解が不能.
- $700億AI投資計画（[INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) A-2）は「最大」表記であり, 実際の投資額は確定しない. 投資計画と実行成果の乖離は未知数.
- Seed 2.0・Seedance 2.0の能力は火山引擎公式ドキュメント・API仕様ベースであり, 独立ベンチマークでの検証が未完了. Seedance市場シェア80%超の測定方法・定義も不明.
- ミラーイメージングリスクを統合判断が明示的に認めた. 西側の「赤字=持続不能」という財務基準を, EC・広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめると, モデルの優位を見落とす. 逆に過大に考慮すると赤字の実相を過小評価する. 判別手段がない.
- Seed 2.0 Code 256K・MAU 3.82億/+172%のA-1品質証拠（[INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087)・[INFO-089](../Information/2026-07-28/collected-raw.md#INFO-089)）がByteDance自己開示ベースであり, 第三者測定による独立検証が不在. MAU 5.28億（[INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) A-2）も中国メディア報道ベースであり, 自己開示データの系統的過大申告リスクと, 中国情報源の限定による独立裏付け不在が, H-BTD-001/002の確度評価の上限を構造的に制約する.

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) | ByteDance 7/30組織再編: 豆包・飛書・火山エンジン統合・新設「創造力サービスプラットフォーム部」・AI toB優先度引き上げ(A-2) |
| [INFO-014](../Information/2026-07-31/collected-raw.md#INFO-014) | 中国3社が旗艦AIアプリからエージェントマーケットプレイス削除・ByteDanceはCoze/Trae/ArkClaw/Feishu Miaoda維持・火山引擎LanceDB AIスタック(C-2) |
| [INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) | FCC: 中国製ヒューマノイド・四足ロボット新規輸入禁止・中国製パワーインバーターも禁止(B-2) |
| [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) | 豆包MAU 5.28億・2026年6月過去最高・DAUピーク1.45億 vs 持続的~8000万・DAU差異技術的説明(A-2) |
| [INFO-076](../Information/2026-07-30/collected-raw.md#INFO-076) | ByteDance最大$700億AIインフラ投資2026・DeepSeek評価額$500億超(A-2) |
| [INFO-077](../Information/2026-07-30/collected-raw.md#INFO-077) | Coze低コードエージェントプラットフォーム・企業版私有化展開・中国第7位(B-3) |
| [INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) | Seed 2.0 Code 256Kコンテキスト・Seedance 2.0・企業軸A-1品質(A-1) |
| [INFO-089](../Information/2026-07-28/collected-raw.md#INFO-089) | 豆包MAU 3.82億/+172% YoY・消費者軸A-1品質・出所独立性リスク(A-1) |
| [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) | ByteDance 2025年売上$186B・純利益$48B・張一鳴中国首富・火山引擎企業級AI(B-2) |
| [INFO-054](../Information/2026-07-23/collected-raw.md#INFO-054) | 豆包DAU 2億・MAU 3.82億・日次売上<100万元・毎日数千万元損失(B-2) |
| [INFO-055](../Information/2026-07-23/collected-raw.md#INFO-055) | Seed Audio 1.0音声・効果音・環境音統一フレームワーク・火山方舟(A-3) |
| [INFO-049](../Information/2026-07-23/collected-raw.md#INFO-049) | 豆包AI智能体手机 ByteDance×ZTE Nubia・WAIC 2026(B-2) |
| [INFO-039](../Information/2026-07-23/collected-raw.md#INFO-039) | WAICO設立: 中国が世界AI協力機構を設立・AIチャットボット規制強化(B-3) |
| [INFO-101](../Information/2026-07-16/collected-raw.md#INFO-101) | Doubao Seed 2.0 Pro/Lite/Mini追加・多モーダル深度思考能力拡張(A-3) |
| [INFO-097](../Information/2026-07-16/collected-raw.md#INFO-097) | Seedance 2.0/2.5業界初4モダリティ同時入力・最大50秒動画・4K/Mini版(A-3) |
| [INFO-013](../Information/2026-07-16/collected-raw.md#INFO-013) | ByteDance/Alibaba Doubao・Qwenエージェント機能7月15日停止(B-3) |
| [INFO-082](../Information/2026-07-10/collected-raw.md#INFO-082) | 豆包エージェント機能7/15終了正式確認(A-2) |
| [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) | 中国: 最先端AIモデル海外アクセス制限をAlibaba/ByteDance/Z.aiと協議(A-2) |
| [INFO-080](../Information/2026-06-30/collected-raw.md#INFO-080) | $200億境外融資seeking・史上最大(A-2) |
| [Arbiter v4.52](../state/arbiter-2026-07-31.md) | 確度評価の完全根拠・H-BTD-002 +1%提案4R連続却下記録・出所独立性・保護市場・投資≠成果3条件継続 |
