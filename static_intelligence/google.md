# Google / DeepMind

> 最終判断更新: 2026-05-06
> 全体確信度: 中
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。TPU 対 NVIDIA の電力効率が外部から測れない
> 主参照: hypotheses.json#H-GOO-001/002/003, indicators.json#IND-001/006/025/027/030

## 0. 一文要約

我々はGoogleを、**性能競争ではなくエコシステム統合とTPU自前インフラで戦う企業**と読んでいる。最大の根拠は Cloud $20B/63% YoY と $462B バックログが示す収益の構造性だ [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027)。ただし H-GOO-003「フロンティア性能競争で対抗」という枠組みで10R以上この企業を測ってきた。その枠組み自体が Google の実際の強みを系統的に見落としていた。「性能指標で負けている」という読みが「エコシステムで勝っている」という読みを上書きしてきたなら、これまでの判断の精度は再評価が要る。もし Workspace 内 Gemini の利用率が3四半期連続で頭打ちになるか、TPU インフラを外部も使えるようになるなら、エコシステム優位の読み自体が崩れる。

## 1. コア判断

Google の現在の構図は、**Cloud 収益の爆発的拡大とエコシステム統合の深化が共存しながら、性能ベンチマークでは Claude / GPT に劣後する**という分裂に集約される。

Cloud 側は数値がはっきりしている。$20.03B/63% YoY、GenAI 製品 800% YoY、Gemini Enterprise の QoQ 40% 成長、バックログ $462B [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027)。計算能力制約で抑えられた成長分がさらに残っているとすると、この数値は上限ではない。Gemini Enterprise Agent Platform は構築・スケール・ガバナンスを一体化したプラットフォームに進化し [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)、公式 Agent Skills リポジトリの公開 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) でエコシステムの厚みが増している。

性能側では対照的な数値が並ぶ。BenchLM 総合で Gemini 3.1 Pro は 93、Claude Mythos Preview (99) に 6pt 差をつけられている [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。ARC-AGI-2 では GPT-5.4 Pro (83.3%) に 6.2pt 劣る。

ここで読むべきは、この「劣後」がどこまで問題なのかだ。20 億人規模の検索・Workspace・Android・Chrome ユーザーを配布チャネルにできる企業にとって、性能での数 pt 差は顧客離脱に直結しない。Cloud 顧客の 75% が AI 製品を使い、330 社が年間 1T 超のトークンを処理している [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) という数値は、すでにエコシステムへの深い埋め込みが起きていることを示す。xAI の Grok が Google Cloud で動くようになったことも [INFO-008](../Information/2026-05-06/collected-raw.md#INFO-008)、Googleがプラットフォームとして機能し始めていることの証拠になる。

ただし、この読みには構造的な自己批判が必要だ。H-GOO-003 は「フロンティア性能競争で対抗」という仮説として設定されており、10R 以上にわたって確度が 55% から 49% へ下がり続けた。低下の原因は性能競争への枠組みそのものが誤りだった可能性がある。エコシステム深度・インフラ・検索統合・マルチモーダル埋め込みといった Google 固有の強みを、性能ベンチマークという一次元で測る枠組みが系統的に無視してきた。この反省は §7 に記録する。

Agent Platform の競争構図は現時点で「三社鼎立」と読んでいる。OpenAI / Anthropic / Google がそれぞれ異なる優位軸（モデル性能・安全性差別化・エコシステム統合）を持ち、単純な性能競争では収束しない構図だ。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Cloud $20.03B/63% YoY、GenAI 800% YoY、バックログ $462B | エコシステム収益が構造的に拡大していることの直接証拠 | A-2 | [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) |
| 高 | Cloud 顧客 75% が AI 製品利用、330 社が年間 1T+ トークン処理 | 顧客が既にエコシステムに深く埋め込まれている。切り替えコストが上がっている | A-2 | [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) |
| 高 | Gemini Enterprise Agent Platform 正式リリース、AIトークン処理 100B/分→160B/分 | Googleがプラットフォーム側に回りつつある。モデル単体ではなく基盤を売る構造への転換 | A-2 | [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) |
| 中 | BenchLM 総合 93（Claude Mythos 99、GPT-5.4 Pro 92）、ARC-AGI-2 77.1% | 性能での劣後は事実。ただしエコシステム優位を崩す証拠にはなっていない | A-2 | [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) |
| 中 | xAI Grok モデルが Google Cloud で利用可能に | Googleがモデル競争より「モデルが動く場所」の競争に軸を移している間接証拠 | A-2 | [INFO-008](../Information/2026-05-06/collected-raw.md#INFO-008) |
| 中 | Pentagon 7社契約で選出（従業員 600+ が拒否要請） | 政府市場参入と内部摩擦が同時進行。実行リスクが内在する | B-2 | [INFO-073](../Information/2026-05-06/collected-raw.md#INFO-073) [INFO-075](../Information/2026-05-06/collected-raw.md#INFO-075) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Workspace 内 Gemini の DAU/MAU または利用率が3四半期連続で頭打ちを示す公式開示 | 「エコシステム統合優位」のコア判断と H-GOO-001 が崩れる | 180日 | [IND-006](../config/indicators.json) |
| OpenAI / Anthropic が自前 TPU 相当のインフラを持つか、TPU を外部調達できるようになる | 「TPU 自前インフラの差別化」が崩れ、H-GOO-002 の再評価が要る | 90日 | [IND-001](../config/indicators.json) |
| エンタープライズLLMシェアで Google が 21% から低下し続け、Anthropic や OpenAI との差が拡大する | エコシステム優位が収益に転換できていないことになり、コア判断全体が疑われる | 90日 | [IND-006](../config/indicators.json) |
| 従業員抗議が拡大し Pentagon 契約の実行停止または大幅縮小に至る | 政府市場参入という機会損失が確定し、H-GOO-002 の政府向け収益根拠が崩れる | 60日 | [IND-030](../config/indicators.json) |
| Gemini を搭載した検索・Workspace の広告収益や課金収益が前年比で下落する | 統合優位が収益化につながっていない証拠になり、エコシステム戦略全体を再考する必要が出る | 180日 | [IND-027](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | 全プロダクトへの Gemini 統合でエコシステム収益を拡大する | 56% | Cloud $20B/63% YoY と Gemini Enterprise QoQ 40% 成長が支持する。ただしエンタープライズLLMシェア 21% がAnthropic 40% に劣後しており、投入指標と成果指標の乖離が残る | [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) | エンタープライズLLMシェアの継続低下 |
| [H-GOO-002](../config/hypotheses.json) | Vertex AI でクラウド市場を追い上げる | 48% | Cloud 収益の高成長が支持するが、Workspace/Vertex/Android での Gemini 優位を定量化する独立指標を持てていない。囲い込み設計の完成度が未確認 | [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015) [INFO-016](../Information/2026-05-06/collected-raw.md#INFO-016) | シェア定量指標の設計未完了が継続 |
| [H-GOO-003](../config/hypotheses.json) | フロンティア性能競争で対抗する（**仮説修正命令発出中**） | 49% | 10R 連続で確度が 55%→49% に低下。MMMU-Pro 88.21% 首位・GPQA Diamond 94.3% 首位だが BenchLM 総合 3 位 (93)。低下の主因は「性能競争」という枠組み自体がGoogleの強みを測れていないこと。仮説を「非性能次元（エコシステム深度・検索統合）での差別化」に再構成するか棄却するかを次回までに決める | [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) MMMU-Pro 首位 | BenchLM 総合での継続劣後 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt 以上/期で high | BenchLM 93 (3位)。MMMU-Pro 88.21% 首位、ARC-AGI-2 77.1% | 2026-05-06 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated 維持で継続監視 | Gemini Enterprise Agent Platform 正式リリース [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)。Agent Skills [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) | 2026-05-06 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Gemini Flash TTS、Deep Research Agent 稼働 [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) | 2026-05-06 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度 | high / rising | MCP 全社サポート [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015)。Red Hat MCP Gateway [INFO-016](../Information/2026-05-06/collected-raw.md#INFO-016) | 2026-05-06 |
| [IND-030](../config/indicators.json) | AI 能力とリスクの二面性 | elevated / rising | Pentagon 契約 + 従業員 600+ 抗議が同時進行 [INFO-075](../Information/2026-05-06/collected-raw.md#INFO-075) | 2026-05-06 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-06 | H-GOO-003 仮説修正命令発出。コア判断を「性能競争への枠組み」から「エコシステム統合優位」へ修正開始 | BenchLM 3位 (93 vs Mythos 99) と10R連続確度低下 [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) | 「性能競争で対抗できる企業」→「エコシステム統合とTPUで戦う企業（性能枠組みの修正中）」 |
| 2026-05-06 | Cloud $20B/63% YoY、GenAI 800%成長、Gemini Enterprise Agent Platform、xAI Grok on Google Cloud、Agent Skills、Pentagon 契約 + 従業員抗議を反映して全面更新 | 鮮度タイムアウト (7日経過) | H-GOO-001 56%、H-GOO-002 48%、H-GOO-003 49% に更新 |
| 2026-04-29 | Gemini Enterprise Agent Platform 詳細・Anthropic $40B 投資を反映 | Cloud Next 2026 後続情報 | 基本情報・戦略方向性を全面書き直し |
| 2026-04-22 | Cloud Next 2026 定量データを初反映 | Pentagon 契約交渉、$240B バックログ | 「Cloud は AWS に大差で劣後」→「急拡大フェーズ」へ読み変え |

## 7. ブラインドスポット

- **H-GOO-003 の失敗から何を学んだか、まだ結論が出ていない**。10R 以上「性能競争」枠組みで測り続け、エコシステム深度・TPU・検索統合という Google 固有の強みを系統的に見落としてきた。この枠組みの誤りは認識した。しかし「非性能次元での差別化」という代替仮説も、その確度を評価する指標をまだ持っていない。仮説を変えたと言えるのは、新しい指標が設計されたときだ。
- **Workspace 内 Gemini の DAU/MAU が公開されていない**。「Cloud 顧客の 75% が AI 製品を使用」という数値は投入量であって利用深度ではない。利用が浅い 75% と深い 30% では意味が全く異なるが、外から区別できない。
- **TPU 対 NVIDIA H200 の電力効率比較が外部から測れない**。Google が TPU 優位を主張しているが、独立した検証がない。インフラ優位の主張の強度が評価できない。
- **Search への AI 統合が広告収益に与える純影響が分離不能**。Gemini を Search に深く統合すれば検索体験が変わる。広告クリック率への影響がプラスかマイナスかは Google 以外には分からない。
- **Anthropic $40B 投資の戦略的含意が外部から不透明**。Gemini 普及を目指す企業が最大の競合モデルに巨額投資する構造は矛盾に見える。議決権なし出資という整理はあるが、この投資がGemini採用を遅らせるインセンティブとして内部で機能していないかが見えない。

## 付録: 直近30日の参照 Evidence

| Evidence | 用途 |
|---|---|
| [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) | Cloud $20B/63% YoY、GenAI 800% YoY、バックログ $462B、AIトークン 160B/分 |
| [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) | Gemini Enterprise Agent Platform 詳細、Cloud 顧客 75% AI 利用、330 社 1T+ トークン |
| [INFO-008](../Information/2026-05-06/collected-raw.md#INFO-008) | xAI Grok モデルが Google Cloud で提供開始 |
| [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) | BenchLM 総合 93 (3位)、Gemini 3.1 Pro vs Mythos vs GPT-5.4 Pro 比較 |
| [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) | 公式 Agent Skills リポジトリ公開 |
| [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015) | MCP 全社サポート |
| [INFO-016](../Information/2026-05-06/collected-raw.md#INFO-016) | Red Hat MCP Gateway |
| [INFO-073](../Information/2026-05-06/collected-raw.md#INFO-073) | Pentagon 7社契約で Google 選出 |
| [INFO-074](../Information/2026-05-06/collected-raw.md#INFO-074) | Pentagon 契約の詳細 |
| [INFO-075](../Information/2026-05-06/collected-raw.md#INFO-075) | 従業員 600+ が CEO に Pentagon 契約拒否を要請 |
| [INFO-065](../Information/2026-05-06/collected-raw.md#INFO-065) | CAISI 事前評価 |
| [Arbiter v3.70](../state/arbiter-2026-05-06.md) | H-GOO-001/002/003 確度評価の完全根拠（本文から外出し）|
