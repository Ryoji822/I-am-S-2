# Google / DeepMind

> 最終判断更新: 2026-09-05
> 全体確信度: 測定不能（H-GOO-001 indeterminate維持）
> 情報非対称性: Geminiアプリ月間10億ユーザーはGoogle自身が公表した（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1）が、Gemini固有のエンタープライズ定量採用データ（シェア・収益・利用率の直接定量A-2+）は57R超にわたり構造的に不在（v4.70計上）。MAUは消費者指標でありエンタープライズ採用シェアではない。UBS試算はGoogle Cloud収益の27%（2026）→48%超（2027・$124B超）がOpenAI+Anthropicの2社依存と定量化し（[INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067) B-2）、Cloud収益成長とGemini固有需要の分離不能性が拡大したまま。GEAP公式ドキュメント（[INFO-008](../Information/2026-09-05/collected-raw.md#INFO-008) A-2）は文書層の整備であって採用定量ではない。3.7 Flash価格は$0.75/$3.75紹介→2027年1月1日倍増（[INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) A-1）と半額$0.38/$1.88報道（[INFO-045](../Information/2026-08-23/collected-raw.md#INFO-045) B-2）が依然併存し定義が未統一。Deep Thinkグラウンデッド視覚推論95首位（[INFO-010](../Information/2026-09-05/collected-raw.md#INFO-010)）はC-2品質。
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はGoogleを「GEAPの文書層を整備しSKILL.md配給形式を公共財化しながら、固有の採用定量だけが57R超にわたり現れない企業」と読む枠組みを維持する。確度の変化は1件である。[H-GOO-002](../config/hypotheses.json)はgoogle/skillsとgoogle/agents-cliの公開（[INFO-021](../Information/2026-09-01/collected-raw.md#INFO-021) A-1・GitHub公式・任意のコーディングエージェント向け）で24%から25%へ上がった（v4.84・9/1裁定）。配給形式の開放はデプロイ実体の開放でないため、次の+1%にはGCP公式self-deploy利用定量または同等のデプロイ実体の開放定量を要求する条件が新しく事前登録された。

[H-GOO-003](../config/hypotheses.json) 48% mediumは、v4.06が事前登録した「48%以下継続でmedium→low移行検討」が長期未執行のままだったプロセス負債を本日解消した。審査の結果は移行しないである。Gemini 3.8 FlashがDeepSWEでAstraを上回る（73.8% vs 73.3%・[INFO-047](../Information/2026-09-05/collected-raw.md#INFO-047) B-1）第三者勝利とDeep Thinkのグラウンデッド首位（[INFO-010](../Information/2026-09-05/collected-raw.md#INFO-010)）が移行反対方向に効いた。旧条件は明示解除され、Google固有の採用定量出現時または2026-12-31のいずれか早い方で確度ラベルを再審査する新条件に置き換わった。[H-GOO-001](../config/hypotheses.json) 50% indeterminateはC-onlyの駐車化注記付きで据え置きである。

## 1. コア判断

全体確信度は測定不能に置く。Gemini固有の定量採用データが構造的に不在である以上、この座標軸は今回の更新でも変わらない。変わったのは3点である。配給形式の公共財化がA-1品質で確定したこと、研究卓越性仮説の条件が運用可能な形に入れ替わったこと、そして第三者ベンチで「全部勝ち」の反例が取れたことである。

### 配給形式の公共財化と新しい条件

v4.84（9/1裁定）はgoogle/skillsとgoogle/agents-cliの公開を「SKILL.md配給形式の公共財化」として認定し、再評価条件「A-2以上の開放C出現」の条件充足を形式的に満たすとして[H-GOO-002](../config/hypotheses.json)を+1%（24→25%）とした。審査は条件充足性のみで実施し（審査前アンカリングの排除）、逆方向材料の層混同も排除された。GEAP中央統制（プラットフォーム層）と紹介価格の2倍予約（価格層）は形式層命題の反証として不適格である（v4.69層区別原則）。9/4にはgemini-skills公式リポジトリ（[INFO-013](../Information/2026-09-05/collected-raw.md#INFO-013) A-2）が続き、Gemini Enterpriseドキュメントでスキルを再利用可能なカスタム命令として管理する機能が定義された。ただし配給形式の開放はデプロイ実体の開放でない。同一証拠クラスからの反復積み上げを防ぐため、次回以降の+1%には「GCP公式self-deploy利用定量または同等のデプロイ実体の開放定量」を要求する条件文言の改訂が事前登録済みである。

### 研究卓越性仮説の条件入替

[H-GOO-003](../config/hypotheses.json)のv4.06条件（48%以下継続でmedium→low移行検討）は前提が「鑑別証拠の長期不在」であり、A-2+品質の研究卓越性定量が20R連続未達成だった時代の産物だった。本日の審査では、Gemini 3.8 FlashのDeepSWE第三者勝利（[INFO-047](../Information/2026-09-05/collected-raw.md#INFO-047) B-1）とDeep Thinkのグラウンデッド視覚推論95首位（[INFO-010](../Information/2026-09-05/collected-raw.md#INFO-010) C-2）が鑑別証拠として現れたため移行は不支持となり、旧条件を明示解除した。新条件は「Google固有の採用定量（GEAP利用実績・デプロイ実体・事業KPI影響の一次確認）出現時または2026-12-31のいずれか早い方で確度ラベル再審査」である。BenchLMマルチモーダル総合ではQwen3.8 Max 87.1・Kimi K3 86.2・Claude Opus 5 85.9が上位を占め（[INFO-010](../Information/2026-09-05/collected-raw.md#INFO-010)）、Geminiは部分指標（グラウンデッド）首位に留まる。DeepSWEの勝利は「全部勝ち」でない反例としてAstra評価分裂の対極に位置する第三者横断データである。

### GEAP文書層とエコシステムの逆流

GEAP公式ドキュメント（[INFO-008](../Information/2026-09-05/collected-raw.md#INFO-008) A-2・9/2更新）は、構築・デプロイ・ガバナンス・最適化の統合プラットフォームを文書層で確定させた。Anthropic側記事で「Google Agent Platform」へのClaude提供が言及され、競合モデルの自社プラットフォーム搭載という同居構造が温存されている。エコシステム全体では逆流も観測される。機械トラフィックが57.5%で人間を超え（2026年6月）、OpenAI・Google・Anthropicの3社でエージェント市場84%を保有する（フランス競争当局・[INFO-026](../Information/2026-09-05/collected-raw.md#INFO-026) B-2）。Googleのトークン処理は9.7兆（2024-05）から3.2京超（2026-05）へ約7倍に伸びた。他方でクロスエージェント4,500スキルの流通（[INFO-014](../Information/2026-09-05/collected-raw.md#INFO-014) C-2）が形式層の開放を底上げし、84%集中と開放流通が逆方向に同時進行する構造（層区別原則の再確認）は[SCN-003](../config/scenarios.json) 25%の材料である。規制面ではAnthropicがマサチューセッツ州安全法案を支持してOpenAI/Googleと決別し（[INFO-053](../Information/2026-09-05/collected-raw.md#INFO-053)）、業界の規制戦線が一枚岩でないことをGoogleはEU AI法執行と並んで受け止める。Google自身は新規コードの75%がAI生成（2026年4月・エンジニア承認済み・[INFO-049](../Information/2026-09-05/collected-raw.md#INFO-049) B-2）と、採用側の最大値を申告している。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | google/skills+google/agents-cli公開（9/1・GitHub公式・任意のコーディングエージェント向け） | [H-GOO-002](../config/hypotheses.json) +1%（24→25%・v4.84）の直接根拠。SKILL.md配給形式の公共財化 | A-1 | [INFO-021](../Information/2026-09-01/collected-raw.md#INFO-021) |
| 高 | gemini-skills公式リポジトリ（9/4）: スキルを軽量な文脈追加手法と定義・Gemini Enterpriseで再利用可能カスタム命令として管理 | v4.84と同一キャンペーン族の反響。context層（Gemini）とshell層（SKILL.md）の設計思想の対比のみ注記 | A-2 | [INFO-013](../Information/2026-09-05/collected-raw.md#INFO-013) |
| 高 | Gemini 3.8 FlashがDeepSWEでAstra超え（73.8% vs 73.3%・第三者計測） | [H-GOO-003](../config/hypotheses.json)条件入替審査のC側材料。「全部勝ち」でない反例として測定基盤文脈でも重要 | B-1 | [INFO-047](../Information/2026-09-05/collected-raw.md#INFO-047) |
| 高 | GEAP公式ドキュメント公開（9/2更新）: 構築・デプロイ・ガバナンス・最適化の統合プラットフォーム。ClaudeのGoogle Agent Platform搭載言及も | [H-GOO-001](../config/hypotheses.json) C-side（C-only警告付き）。文書層の整備で採用定量ではない | A-2 | [INFO-008](../Information/2026-09-05/collected-raw.md#INFO-008) |
| 高 | 機械トラフィック57.5%で人間超え（6月）・エージェントは人間比5倍トークン（85%超がキャッシュ再読み）・3社でエージェント市場84%（仏競争当局） | [SCN-003](../config/scenarios.json) 25%の集中材料。Googleトークン処理3.2京超（約7倍YoY） | B-2 | [INFO-026](../Information/2026-09-05/collected-raw.md#INFO-026) |
| 中 | Deep Thinkグラウンデッド視覚推論95首位（BenchLM部分指標・総合はQwen3.8 Max 87.1首位） | [H-GOO-003](../config/hypotheses.json)移行反対方向の第二材料。C-2品質で計上留保 | C-2 | [INFO-010](../Information/2026-09-05/collected-raw.md#INFO-010) |
| 中 | Google新規コード75%AI生成（2026年4月・エンジニア承認済み）・採用84% vs 信頼33%の乖離 | [IND-026](../config/indicators.json)三次定量。採用側最大値の当事者申告 | B-2 | [INFO-049](../Information/2026-09-05/collected-raw.md#INFO-049) |
| 中 | 9月価格表: Gemini 3.1 Flash-Lite $0.25/$1.50・3.6 Flash $1.50/$7.50・3.1 Pro $2/$12（プレビュー） | 低価格帯の拡大継続。2027年1月倍増予約（3.7 Flash）はSCN-003材料として蓄積 | C-2 | [INFO-029](../Information/2026-09-05/collected-raw.md#INFO-029) |
| 中 | Anthropicがマサチューセッツ安全法案支持でOpenAI/Googleと決別・Amodei「too blunt」批判・AI DCモラトリアム法提出 | 規制戦線の分裂。GoogleはEU AI法執行と州規制乱立の両方に曝される | B-2 | [INFO-053](../Information/2026-09-05/collected-raw.md#INFO-053) |
| 中 | Google Ads MCPは読み取り専用（2025-10・OSS）のまま、X Ads MCPは本番書き込み10ツールで先行 | 広告MCP標準化競争でのGoogleの位置。書き込み権限の標準化は攻撃表面の拡大 | B-2 | [INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Gemini固有の定量採用データ（A-2+品質のシェア・収益・利用率）が初めて公表される | [H-GOO-001](../config/hypotheses.json) indeterminate状態が解消し、low/mediumのいずれかに復帰する。[H-GOO-003](../config/hypotheses.json)新条件の発火点でもある | 2026-12-31（新条件の期限） | [H-GOO-001](../config/hypotheses.json) |
| GCP公式self-deploy利用定量または同等のデプロイ実体の開放定量が出現する | [H-GOO-002](../config/hypotheses.json)次回+1%審査の必須条件（v4.84事前登録）が充足される | 90日 | [H-GOO-002](../config/hypotheses.json) |
| 2026-12-31までにGoogle固有の採用定量が出ない | [H-GOO-003](../config/hypotheses.json)の確度ラベル再審査が期限で強制発火する（新条件） | 2026-12-31 | [H-GOO-003](../config/hypotheses.json) |
| 旧Vertex顧客の移行率・解約率・GEAP固有の採用数が定量で観測される | プラットフォーム統合の採用実態が初めて測定され、開放と統合の重心判別が始まる | 90日 | [IND-026](../config/indicators.json) |
| Extensions EOL（2026-11-26）までの移行完了率・機能ギャップ報告 | 強制移行の実害が判定され、[H-GOO-002](../config/hypotheses.json)囲い込みI側の確定または失効が始まる | 2026-11-26 | [H-GOO-002](../config/hypotheses.json) |
| 3.x系価格が2027年1月1日に実際に倍増する、または期間延長・撤回 | 価格権力の事前告知の検証。SCN-003材料の確定または失効 | 2027-01-01 | [IND-027](../config/indicators.json) |
| Google Cloud収益の対AIラボ依存度（UBS試算27%→48%）が四半期開示で検証される | [H-GOO-001](../config/hypotheses.json)のCloud-level成長解釈が変わり、分離不能性の実態判定が始まる | 90日 | [H-GOO-001](../config/hypotheses.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かし、エンタープライズAI市場でシェアを拡大する | 50% indeterminate | v4.86 ±0%（v4.70のindeterminate維持以来）。GEAP公式docs（[INFO-008](../Information/2026-09-05/collected-raw.md#INFO-008) A-2）はGCP側進捗の実質証拠だがGoogle固有の採用定量は構造的不在（57R超）。C-only不定状態の駐車化注記継続（確証而非観測限界）。強制再評価条件の本章拡張が検討事項のまま | [INFO-008](../Information/2026-09-05/collected-raw.md#INFO-008) [INFO-026](../Information/2026-09-05/collected-raw.md#INFO-026) | [INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067)（2社依存の定量化） |
| [H-GOO-002](../config/hypotheses.json) | GoogleはGemini Tools & Agentsでオープン標準（LangChain等）とのDay 0サポートを維持し、囲い込みを回避する | 25% low | v4.84 +1%（24→25%・9/1裁定）を反映。google/skills+agents-cli公開（A-1・GitHub公式）が再評価条件「A-2以上の開放C出現」を形式的に充足（SKILL.md配給形式の公共財化）。層区別原則でGEAP統制・価格2倍予約は形式層命題の反証から除外。次回+1%には「GCP公式self-deploy利用定量または同等のデプロイ実体の開放定量」を要求（条件文言改訂の事前登録）。gemini-skills（[INFO-013](../Information/2026-09-05/collected-raw.md#INFO-013)）は同一キャンペーン族の反響で低評価 | [INFO-021](../Information/2026-09-01/collected-raw.md#INFO-021) [INFO-013](../Information/2026-09-05/collected-raw.md#INFO-013) [INFO-014](../Information/2026-09-05/collected-raw.md#INFO-014) | [INFO-010](../Information/2026-08-23/collected-raw.md#INFO-010)（Extensions EOL） [INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012)（GEAP統合） |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% medium | v4.86 ±0%・プロセス負債解消ラウンド。v4.06条件「48%以下継続でmedium→low移行検討」の長期未執行を本日審査執行し移行せず: DeepSWE第三者勝利（[INFO-047](../Information/2026-09-05/collected-raw.md#INFO-047) B-1）・Deep Think 95首位（[INFO-010](../Information/2026-09-05/collected-raw.md#INFO-010) C-2）が移行反対方向。旧条件を明示解除し「Google固有の採用定量出現時または2026-12-31のいずれか早い方で確度ラベル再審査」を新登録 | [INFO-047](../Information/2026-09-05/collected-raw.md#INFO-047) [INFO-010](../Information/2026-09-05/collected-raw.md#INFO-010) | A-2+研究卓越性定量の連続未達成・研究者流失2人目（[INFO-056](../Information/2026-08-17/collected-raw.md#INFO-056) C-3） |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・測定慣行 | 複数ベンチマーク×複数ラボで再現ならhigh | elevated/stable（v4.86）。Gemini 3.8 FlashのDeepSWE勝利（73.8%・[INFO-047](../Information/2026-09-05/collected-raw.md#INFO-047)）は第三者単一ベンチで閾値不充足。ARC-AGI-3標準62.7% vs Provider 99.9%の37.2pt差が測定慣行問題の一次立証（A-1）として同一指標に計上済み。high移行候補在庫（AVO・DeepSeek V4-Pro）継続 | 2026-09-05 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 期待-実態ギャップの定量蓄積 | high/rising（v4.86）。三次定量: 配備26-50体→76-100体/四半期 vs 成熟ガバナンス21%・採用84% vs 信頼33%（Google新規コード75%AI生成・[INFO-049](../Information/2026-09-05/collected-raw.md#INFO-049)を含む） | 2026-09-05 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度 | 攻撃表面の標準化進行 | high/rising（v4.86）。google/skills+agents-cli公開・gemini-skills反響（[INFO-021](../Information/2026-09-01/collected-raw.md#INFO-021)/[INFO-013](../Information/2026-09-05/collected-raw.md#INFO-013)）・クロスエージェント4,500スキル（[INFO-014](../Information/2026-09-05/collected-raw.md#INFO-014)）で形式層標準化が継続。Google Ads MCPは読み取り専用のまま（[INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025)）。3.7 Flash 2027年倍増予約はKIQ-MONETIZATION監視継続 | 2026-09-05 |
| [IND-028](../config/indicators.json) | AGI到達度（予測分裂） | 分裂の深化・法制化圧力 | high/rising（v4.86）。Hassabis「2030年まで50%」でフロンティアCEO中最も保守的な位置は不変。Chollet「sooner」前倒し・Sanders超知能禁止法案（[INFO-052](../Information/2026-09-05/collected-raw.md#INFO-052)）で予測分裂のレンジ拡大 | 2026-09-05 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | critical解消3基準 | critical/rising（v4.86）。N=1実質32R。DoD 4社$200M契約の一角（GenAI.milはGoogle以外にも拡大・[INFO-018](../Information/2026-09-05/collected-raw.md#INFO-018)）。EU AI法執行・AI DCモラトリアム法案提出（[INFO-053](../Information/2026-09-05/collected-raw.md#INFO-053)）。critical解消3基準いずれも未到達 | 2026-09-05 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-09-05 | §0〜§7書き直し（鮮度タイムアウト7日）。[H-GOO-002](../config/hypotheses.json) +1%（24→25%・v4.84・google/skills+agents-cli公開のA-1）を反映し、次回+1%条件（デプロイ実体の開放定量）を明記。[H-GOO-003](../config/hypotheses.json) 48%の条件入替（v4.06旧条件の明示解除・採用定量出現時または2026-12-31で再審査の新条件）を反映。Gemini 3.8 Flash DeepSWE勝利・GEAP公式docs・gemini-skills・機械トラフィック57.5%/84%集中・Google新規コード75%を新規計上。§5全指標をv4.86値に更新 | 鮮度タイムアウト7日 + H-GOO-003条件入替（v4.86） | H-GOO-001 50%（±0%）・H-GOO-002 24→25%・H-GOO-003 48%（±0%・条件入替） |
| 2026-08-29 | 全面書き直し（8日freshness timeout）。GEAP吸収統合・Extensions EOL・A2A v1.0 AAIF移管・UBS 2社依存定量化を新規反映。H-GOO-002 23→24%（v4.76）を遅って反映 | 鮮度タイムアウト + Arbiter v4.76〜v4.81 | H-GOO-001 50%（±0%）・H-GOO-002 23→24%・H-GOO-003 48%（±0%） |
| 2026-08-21 | 鮮度タイムアウト更新。08-15〜08-19バッチ統合（10億MAU・組織再編・3.7 Flash価格設計等） | 鮮度タイムアウト（7日） | H-GOO-001 50%（±0%）・H-GOO-002 23%（±0%）・H-GOO-003 48%（±0%） |
| 2026-08-14 | ターゲット編集（フロンティアモデル新規リリース: Gemini 3.7 Flash） | [INFO-001](../Information/2026-08-14/collected-raw.md#INFO-001) | H-GOO-001 50%（±0%） |
| 2026-08-12 | 全面書き直し（CEO交代・新モデル群: 9.5億MAU・Koray新CEO・Gemini 3.1 Pro等） | [INFO-005](../Information/2026-08-12/collected-raw.md#INFO-005) | KIQ-GOO-001 44R/45R→46R/47R |

## 7. ブラインドスポット

- google/skills公開の+1%（v4.84）は配給形式の評価である。デプロイ実体（誰が・どの規模で実際にself-deployしているか）は依然測定できておらず、新条件が充足されないまま同一キャンペーン族の反響（gemini-skills）が積み上がる危険を、条件文言の改訂で封じたに過ぎない。
- H-GOO-003の新条件は期限（2026-12-31）つきである。採用定量が出ないまま期限を迎えた場合の再審査が今度こそ執行されるか、プロセス負債の再発を防ぐ担保は運用規律しかない。
- Gemini固有定量データが57R超構造的に不在。indeterminate分類の駐車化対処（強制再評価条件の本章拡張）が記録されたまま実施されていない。下位命題分解の評価設計も未完成である。
- UBSの2社依存試算（27%→48%）は単一試算で前提が開示されていない。Cloud収益のGemini寄与分の分離は四半期開示でもそのまま残る可能性がある。
- Deep Thinkグラウンデッド95首位はC-2品質で、BenchLM総合ではQwen3.8 Maxが首位である。部分指標の選択性が誰の視点で行われているか（Google自家選択か集計側か）が読めない。
- 3.7 Flashの実効価格が確定できない（$0.75/$3.75紹介 vs $0.38/$1.88報道）。一次価格ページの時系列確認なしにはティア差か価格改定かの判別ができない。
- GEAPドキュメントは文書層の完成で、旧Vertex顧客の移行率・解約率・GEAP固有採用数は取れていない。ClaudeのGoogleプラットフォーム搭載がGEAP戦略の差別化なのか中立化なのかも、利用定量なしには判別できない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-021](../Information/2026-09-01/collected-raw.md#INFO-021) | google/skills+google/agents-cli公開・任意のコーディングエージェント向け(A1・H-GOO-002 +1%の直接根拠・v4.84) |
| [INFO-013](../Information/2026-09-05/collected-raw.md#INFO-013) | gemini-skills公式リポジトリ・Gemini Enterpriseのスキル管理(A2・同一キャンペーン族の反響) |
| [INFO-008](../Information/2026-09-05/collected-raw.md#INFO-008) | GEAP公式ドキュメント・ClaudeのGoogle Agent Platform搭載言及(A2・H-GOO-001 C-only材料) |
| [INFO-047](../Information/2026-09-05/collected-raw.md#INFO-047) | Gemini 3.8 Flash DeepSWE 73.8%>Astra 73.3%(B1・H-GOO-003条件入替のC側) |
| [INFO-010](../Information/2026-09-05/collected-raw.md#INFO-010) | Deep Thinkグラウンデッド95首位・BenchLM総合はQwen3.8 Max首位(C2) |
| [INFO-026](../Information/2026-09-05/collected-raw.md#INFO-026) | 機械トラフィック57.5%・3社84%・Googleトークン3.2京超(B2・SCN-003材料) |
| [INFO-049](../Information/2026-09-05/collected-raw.md#INFO-049) | Google新規コード75%AI生成・採用84% vs 信頼33%(B2・IND-026) |
| [INFO-014](../Information/2026-09-05/collected-raw.md#INFO-014) | Agensi クロスエージェント4,500スキル・5,500ユーザー・400クリエイター(C2・形式層標準化) |
| [INFO-029](../Information/2026-09-05/collected-raw.md#INFO-029) | 9月価格表: Flash-Lite $0.25/$1.50・3.6 $1.50/$7.50・3.1 Pro $2/$12(C2) |
| [INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025) | 広告MCP比較: Google読み取り専用 vs X本番書き込み10ツール(B2) |
| [INFO-053](../Information/2026-09-05/collected-raw.md#INFO-053) | AnthropicがOpenAI/Googleと決別・AI DCモラトリアム法案(B2・規制戦線分裂) |
| [INFO-037](../Information/2026-09-05/collected-raw.md#INFO-037) | ECB警告: 米テック5社（Google含む）債務+18%・計$142B(C2・IND-029文脈) |
| [INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012) | Vertex AI→GEAP吸収統合(A-2) |
| [INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067) | UBS試算: 2社依存27%→48%超・$124B超(B-2) |
| [INFO-002](../Information/2026-08-24/collected-raw.md#INFO-002) | Grok 4.6 on GEAP: $2/$6・500k ctx(A-3) |
| [INFO-010](../Information/2026-08-23/collected-raw.md#INFO-010) | Vertex AI Extensions 2026-11-26 EOL(A-3) |
| [INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) | Gemini月間10億ユーザー・Google公式(A-1) |
| [INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) | 3.7 Flash $0.75/$3.75→2027/1/1倍増予約(A-1) |
| [INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) | 組織再編: Koray統括・Hassabis専任(B-1) |
| [INFO-116](../Information/2026-08-17/collected-raw.md#INFO-116) | Hassabis「2030年まで50%」・最も保守的(B-2) |
| [Arbiter v4.86](../state/arbiter-2026-09-05.md) | H-GOO-003条件入替（プロセス負債解消）・全仮説±0%・指標全件維持 |
| [Arbiter v4.84](../state/arbiter-2026-09-01.md) | H-GOO-002 +1%（24→25%・条件(ii)形式的充足・条件文言改訂の事前登録） |
