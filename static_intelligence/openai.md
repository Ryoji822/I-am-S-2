# OpenAI

> 最終判断更新: 2026-07-10
> 全体確信度: 中低
> 情報非対称性: 収益内訳（API/Enterprise/Consumerセグメント・政府vs民間）が非公開（KIQ-OAI-001未回答継続・18R連続不在）。月次約$2B収益・年率$20-24Bは確認できたが、セグメント内訳は不変。H1 2025で収入$4.3Bに対し純損失$13.5B（構造的赤字）。MicrosoftがOpenAI Group PBCの約27%を所有（評価額$135B）（INFO-011 B-3）。GPT-5.6（Sol/Terra/Luna）一般提供開始（INFO-093 A-2）。ChatGPT Work Agent発表（INFO-010 B-2）。Arbiter v4.31は±0%の根拠を「核心パラメータ不在による確度変更保留」として維持。Arbiter v4.31 COMPLETE
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-OAI-001](../config/hypotheses.json) は49%（medium）で±0%。Arbiter v4.31は核心パラメータ不在（KIQ-OAI-001 18R連続不在）による確度変更保留を±0%の根拠として維持した。収益内訳（API/Enterprise/Consumer・政府vs民間）が非公開である限り、B2B支配地位の収益的裏付けを質的に評価できず、確度の上下いずれの変更も根拠不足となる。39.5%横ばいの企業AI採用率（[INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) B-3）が初確認されたが、これはavailability≠adoptionの二重基準（v4.26指摘）を逆方向から補強する。

本ラウンドの支配的展開は、GPT-5.6（Sol/Terra/Luna）の一般提供開始である（[INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) A-2）。3モデル構成でリリース。プログラム的ツール呼び出しをサポートする。GPT-5.6 SolはARC-AGI-3で7.8%を達成し、同ベンチマークで初めて有意義な進歩を示した（ローンチ時最高0.37%）。Terminal-Bench 91.9%。トークン効率1.72x向上。マルチホップタスク88%。ChatGPT Work Agent（[INFO-010](../Information/2026-07-10/collected-raw.md#INFO-010) B-2）はGPT-5.6搭載で数時間のタスク自律実行を可能にする。

MicrosoftがOpenAI Group PBCの約27%を所有し（評価額$135B）（[INFO-011](../Information/2026-07-10/collected-raw.md#INFO-011) B-3）、PBC移行が完了した。No-code Agent BuilderとEvalsが2026年11月30日で終了する（[INFO-023](../Information/2026-07-10/collected-raw.md#INFO-023) C-3）。ChatGPT Work Agentへの戦略的シフトの可能性がある。OpenAI Agents SDKがプロバイダー非依存（AWS Bedrock対応）として展開中（[INFO-015](../Information/2026-07-10/collected-raw.md#INFO-015) A-3）。API Multi-agent機能でモデルがサブエージェントを並列起動・協調する（[INFO-031](../Information/2026-07-10/collected-raw.md#INFO-031) A-3）。

[H-OAI-002](../config/hypotheses.json) は44%（low）で±0%。Agent SDKのプロバイダー非依存性で围い込み否定証拠の累積が継続。[H-OAI-003](../config/hypotheses.json) は3%（low）で±0%。商業化規模の圧倒的証拠が継続。

## 1. コア判断

全体確信度は中低。H-OAI-001 49% ±0%の根拠は前回と変わらない。収益内訳（KIQ-OAI-001）が不在であるため、確度変更の根拠が形成できない。

### GPT-5.6一般提供とARC-AGI-3 7.8%

GPT-5.6ファミリー（Sol/Terra/Luna）の一般提供が開始された（[INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) A-2）。3モデル構成で制限プレビューを経てリリース。プログラム的ツール呼び出しをサポートする。GPT-5.6 SolはARC-AGI-3で7.8%を達成し、同ベンチマークで初めて有意義な進歩を示したモデルになった。3月のローンチ時最高スコアは0.37%であった。ARC-AGI-1とARC-AGI-2では90%超。効率の新パレートフロンティアを確立した。全体で1.72xトークン効率向上、マルチホップタスク88%。

この結果は2つの含意を持つ。第一に、フロンティア差別化の残存を示す。SCN-004（コモディティ化）が33%で首位であるが、GPT-5.6 SolのARC-AGI-3 7.8%は特定ドメインでの差別化の存在を示す。第二に、GPT-5.6は防御的タスク（セキュアコードレビュー、パッチ適用、脅威モデリング）もサポートする（[INFO-031](../Information/2026-07-10/collected-raw.md#INFO-031) A-3）。安全性機能の製品統合が進んでいる。

ChatGPT Work AgentはGPT-5.6搭載で、ドキュメント、スプレッドシート、プレゼン、Webアプリを数時間で自律作成可能である（[INFO-010](../Information/2026-07-10/collected-raw.md#INFO-010) B-2）。Responses APIを基盤とする自律タスク実行エージェントで、エンタープライズエージェント戦略の新柱となる。Multi-agent APIにより、モデルがサブエージェントを並列起動・協調し、結果を統合して最終応答を生成する（[INFO-031](../Information/2026-07-10/collected-raw.md#INFO-031) A-3）。

### 企業AI採用率39.5%横ばいとコモディティ化圧力

Anthropicが米国企業AI有料サブスク採用率41%で首位に立ち、OpenAIは39.5%で横ばいであった（[INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) B-3）。39.5%横ばいの初確認は質的意義を持つ。企業がベンチマークより主権、マルチモデル柔軟性、ビジネス成果を重視する段階に移行している。availability≠adoptionの二重基準がここでも観測される。GPT-5.6の技術優位性と採用率横ばいの乖離は、技術性能が自動的に市場支配に直結しないことを示す。

コモディティ化圧力は量的に深化している。AIトークン価格が高値から約20%下落（[INFO-052](../Information/2026-07-10/collected-raw.md#INFO-052) A-2）。DeepSeek V4 Proが$1.74/M inputで提供される一方、GPT-5.5は$5/$30、Claude Opus 4.8は$5/$25である。GLM-5.2がオープンウェイト#1、全体4位にランクイン（[INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) B-3）。MMLUは90%超で飽和し、フロンティアモデルの差別化には不十分（[INFO-060](../Information/2026-07-10/collected-raw.md#INFO-060) C-3）。これらはH-OAI-001のI方向（コモディティ化）の証拠である。

### PBC移行完了と構造的赤字

OpenAI Group PBCへの移行が完了した。Microsoftが約27%を所有し、評価額は$135Bである（[INFO-011](../Information/2026-07-10/collected-raw.md#INFO-011) B-3）。No-code Agent BuilderとEvalsが2026年11月30日で終了する（[INFO-023](../Information/2026-07-10/collected-raw.md#INFO-023) C-3）。ホスト型ビルダーに依存する製品にプラットフォームリスクをもたらす。ChatGPT Work Agentへの戦略的シフトの可能性がある。

OpenAIがAI設計チップ「Jalapeño」を9ヶ月で開発した（[INFO-067](../Information/2026-07-10/collected-raw.md#INFO-067) C-3）。最大のAIラボがシリコン設計を9ヶ月で行う事実は、インフラ前提の有効期限を示唆する。AIの自律的ハードウェア設計能力の具体例であるが、C-3品質であり検証が必要。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | GPT-5.6（Sol/Terra/Luna）一般提供開始: ARC-AGI-3 7.8%・Terminal-Bench 91.9%・1.72x効率 | [H-OAI-001](../config/hypotheses.json) C方向。フロンティア差別化の残存。SCN-004完全コモディティ化の反証 | A-2 | [INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) |
| 高 | ChatGPT Work Agent: GPT-5.6搭載・数時間タスク自律実行・ドキュメント/スプレッドシート/プレゼン/Webアプリ作成 | [H-OAI-001](../config/hypotheses.json) C方向。エンタープライズエージェント戦略の新柱。Multi-agent API基盤 | B-2 | [INFO-010](../Information/2026-07-10/collected-raw.md#INFO-010) |
| 高 | 企業AI採用率39.5%横ばい（Anthropic 41%首位）。2024年12月10.6%からの成長が止まった初の観測 | [H-OAI-001](../config/hypotheses.json) I方向。39.5%横ばい初確認の質的意義。availability≠adoption | B-3 | [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) |
| 高 | Microsoft所有比率約27%（評価額$135B）・PBC移行完了・独占禁止分析 | [H-OAI-001](../config/hypotheses.json) 企業構造確定。Microsoft依存関係の定量化。AI市場構造への独占停止法文脈 | B-3 | [INFO-011](../Information/2026-07-10/collected-raw.md#INFO-011) |
| 高 | API価格崩壊: トークン指数高値から約20%下落・DeepSeek V4 Pro $1.74/M vs GPT-5.5 $5/$30 | [H-OAI-001](../config/hypotheses.json) I方向。コモディティ化の経済的次元深化。価格決定力の脆弱化 | A-2 | [INFO-052](../Information/2026-07-10/collected-raw.md#INFO-052) [INFO-091](../Information/2026-07-10/collected-raw.md#INFO-091) |
| 高 | GLM-5.2オープンウェイト#1・全体4位・$1.40/$4.40。MMLU全社>90%で飽和 | [H-OAI-001](../config/hypotheses.json) I方向。オープンソース-クローズドギャップ継続縮小。差別化技術的前提の侵食 | B-3 | [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) [INFO-060](../Information/2026-07-10/collected-raw.md#INFO-060) |
| 高 | No-code Agent Builder/Evals終了（11/30）・ChatGPT Work Agent戦略シフト | [H-OAI-001](../config/hypotheses.json) プラットフォームリスクの具体化。エージェント戦略の再編 | C-3 | [INFO-023](../Information/2026-07-10/collected-raw.md#INFO-023) |
| 中 | OpenAI Agents SDK: プロバイダー非依存（AWS Bedrock対応）・tools/handoffs/guardrails/tracing | [H-OAI-002](../config/hypotheses.json) 围い込み否定累積。プロバイダー非依存で排他性なし | A-3 | [INFO-015](../Information/2026-07-10/collected-raw.md#INFO-015) |
| 中 | Jalapeño: AI設計チップ9ヶ月開発・インフラ前提の有効期限示唆 | [IND-028](../config/indicators.json) AI自律的ハードウェア設計能力の具体例。但しC-3品質 | C-3 | [INFO-067](../Information/2026-07-10/collected-raw.md#INFO-067) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-OAI-001](../config/hypotheses.json) が45%を割る | 「B2B支配的地位確立」仮説が棄却水準に接近。medium→low帯移行 | 180日 | [H-OAI-001](../config/hypotheses.json) |
| KIQ-OAI-001が回答されAPI/Enterprise/Consumer収益内訳が公表される | 49%の凍結が解消し、B2B支配の収益的裏付けの質的評価が可能になる。核心パラメータ不在の制約が解除される | 90日 | [IND-027](../config/indicators.json) |
| 企業AI採用率39.5%が更に低下し、35%を下回る | 「支配」の定義が成立しなくなる。Anthropic 41%との差が構造化する | 180日 | [IND-008](../config/indicators.json) |
| OSSモデルのエンタープライズ採用シェアが10%を超える | 「勝者集中」前提が崩れ、SCN-004が上昇する。H-OAI-001のI方向確定 | 90日 | [IND-027](../config/indicators.json) |
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | コモディティ化の不可逆的加速判断が崩れる | 180日 | [IND-025](../config/indicators.json) |
| IPOが更に延期または評価額が$500Bを下回る | 構造的成長の外部検証が失敗する。$13.5B赤字の吸収見通し悪化 | 365日 | [IND-029](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 49% medium | ±0%（v4.24で48→49%+1%後4R連続±0%）。核心パラメータ不在（KIQ-OAI-001 18R）による確度変更保留。GPT-5.6 GA・ARC-AGI-3 7.8%・ChatGPT Work Agent・Multi-agent APIはC方向。39.5%横ばい・API価格崩壊・GLM-5.2 OSS#1・MMLU飽和はI方向。39.5%横ばい初確認の質的意義をI側評価に反映。medium維持 | [INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) [INFO-010](../Information/2026-07-10/collected-raw.md#INFO-010) | [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) [INFO-052](../Information/2026-07-10/collected-raw.md#INFO-052) [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放の上にプロプライエタリ上位レイヤーで围い込む | 44% low | ±0%。围い込み否定累積継続。Agent SDKプロバイダ非依存（INFO-015 A-3）・AWS Bedrock対応・排他性なし。No-code Agent Builder終了はプラットフォーム戦略の転換。low帯確定度増加 | (新規围い込み肯定Cなし) | [INFO-015](../Information/2026-07-10/collected-raw.md#INFO-015) [INFO-023](../Information/2026-07-10/collected-raw.md#INFO-023) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% low | ±0%。商業化規模（月次$2B収益・$20-24B年率・IPO準備・PBC移行・ChatGPT Work Agent）圧倒的。G7でAltman自身の在任中AGI到達可能と主張（INFO-075 B-2）だが、行動は商業化優先。AGI最優先支持A-2+証拠不在 | (該当なし) | [INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) [INFO-010](../Information/2026-07-10/collected-raw.md#INFO-010) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントでcritical | SkillCloak全静的スキャナ突破（INFO-022 B-2）・AI生成コード45% OWASP脆弱性（INFO-026 B-2）・AIエージェント本番DB削除（INFO-027 B-3）。GPT-5.6 Solセキュアコードレビュー・脅威モデリング対応（INFO-031 A-3）。新規A-2実被害なし。critical移行条件未到達。high/rising | 2026-07-10 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | GPT-5.6 Sol ARC-AGI-3 7.8%（INFO-061 A-2）・MMLU全社>90%飽和（INFO-060 C-3）・GLM-5.2 OSS#1全体4位（INFO-057 B-3）・API価格高値から約20%下落（INFO-052 A-2）。コモディティ化圧力量的深化。elevated/stable | 2026-07-10 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | 88%パイロット停滞（INFO-039 B-2）・97%コミット/18%デプロイ・IDC 4/33本番移行・リスク完全緩和7%（INFO-026 B-2）。期待-実態ギャップ更に強化（13+独立ソース）。high/rising | 2026-07-10 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | MCP RC（INFO-021 A-3）・OpenAI Agents SDK provider-agnostic（INFO-015 A-3）・AAIF拡大・MS Foundry→M365（INFO-037 A-3）。標準化加速と围い込み否定の同時進行。high/rising | 2026-07-10 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | GPT-5.6 Sol ARC-AGI-3 7.8%（INFO-061 A-2）・G7 Altman AGI討議（INFO-075 B-2）・AGI定義不合継続（INFO-076 B-2）・UN科学パネル発足（INFO-090 B-3）。RSI具体化と客観ベンチマーク限界の同時進行。high/rising | 2026-07-10 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | DC $850Bリース+204% YoY（INFO-059 A-2）・ビッグテック$650B/$2B/day（INFO-063 B-3）・H1 $252B投資（INFO-080 B-2）。資本流入加速・物理的制約ギャップ確定的。high/rising | 2026-07-10 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。Warren開示要求7社AI契約（INFO-044 A-2）・DPA脅迫確認（INFO-045 B-2）・Pentagon $54B自律戦争（INFO-004 C-3）・国連事務総長LAWS禁止要求（INFO-047 A-2）・human-in-loop法案（INFO-012 B-3）・June 2026 EO（INFO-050 A-2）。KIQ-MIL-001 18R不在。IND-030-SCN-BS-001連動関係形式的定義実行 | 2026-07-10 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-10 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% medium ±0%（核心パラメータ不在18R）。GPT-5.6（Sol/Terra/Luna）GA・ARC-AGI-3 7.8%（INFO-093 A-2）・ChatGPT Work Agent（INFO-010 B-2）・Multi-agent API・企業AI採用率39.5%横ばい（INFO-064 B-3）・Microsoft 27%所有（INFO-011 B-3）・API価格崩壊（INFO-052 A-2）を反映。Arbiter v4.31 COMPLETE | [INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) [INFO-010](../Information/2026-07-10/collected-raw.md#INFO-010) [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) | H-OAI-001 49%（±0%） |
| 2026-07-03 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% medium ±0%。根拠を「C/I均衡」から「核心パラメータ不在による確度変更保留」に修正。5%政府株式提案・GPT-5.6延期要請・月次$2B収益/$13.5B構造的赤字 | [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) [INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) | H-OAI-001 48→49%（v4.24）・根拠修正 |
| 2026-06-29 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 48% ±0% | [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) | H-OAI-001 48%（±0%） |
| 2026-06-27 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49→48% | [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) | H-OAI-001 49→48% |

## 7. ブラインドスポット

- 収益内訳（API/Enterprise/Consumer・政府vs民間）が非公開（KIQ-OAI-001 18R連続不在）。月次$2Bの内訳が判明しない限り、49%の確度変更は根拠不足。Arbiter v4.31が「核心パラメータ不在による確度変更保留」を正式根拠として維持したが、これは情報不足を認めることと同義。
- 39.5%横ばい初確認の質的意義が、確度変更の根拠として採用されなかった。技術性能（GPT-5.6 Sol ARC-AGI-3 7.8%）と採用率横ばいの乖離は、availability≠adoptionの構造を補強する。この乖離が持続するか、一時的かの判別が不能。
- $13.5B純損失（H1 2025）と月次$2B収益の乖離がいつ解消するか不明。Microsoft所有比率27%が確定したが、Microsoft支援縮小時に赤字構造が悪化する可能性がある。
- GPT-5.6のARC-AGI-3 7.8%が特定ドメイン（抽象推論）の差別化を示す一方で、MMLU全社>90%が汎用能力の平均化を示す。この二層構造を単一のI/C評価で表現できていない。
- No-code Agent Builder/Evals終了（11/30）が、ChatGPT Work Agentへの戦略シフトか、プラットフォーム能力の放棄かの判別が不能。戦略シフトであればC方向だが、放棄であればI方向。
- PBC移行完了後のMicrosoft 27%所有が、OpenAIの独立性にどう影響するか。MicrosoftのStargate合弁でOracleが追加され、Azure排他性が低下している。インフラ多角化は独立性強化という正面解釈と、Microsoft支援縮小という裏面解釈が両立する。
- G7でAltmanが自身の在任中AGI到達可能と主張した（INFO-075 B-2）が、行動はChatGPT Work Agent・PBC移行・IPO準備と商業化一辺倒。発言と行動の乖離をどう評価するかの基準が不在。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-010](../Information/2026-07-10/collected-raw.md#INFO-010) | ChatGPT Work Agent: GPT-5.6搭載・数時間自律実行・ドキュメント/スプレッドシート/プレゼン/Webアプリ(B-2) |
| [INFO-011](../Information/2026-07-10/collected-raw.md#INFO-011) | Microsoft所有比率約27%・評価額$135B・PBC移行完了・独占禁止分析(B-3) |
| [INFO-015](../Information/2026-07-10/collected-raw.md#INFO-015) | OpenAI Agents SDK: プロバイダー非依存・AWS Bedrock対応・tools/handoffs/guardrails/tracing(A-3) |
| [INFO-023](../Information/2026-07-10/collected-raw.md#INFO-023) | No-code Agent Builder/Evals 11/30終了・ChatGPT Work Agent戦略シフト(C-3) |
| [INFO-031](../Information/2026-07-10/collected-raw.md#INFO-031) | Multi-agent API: サブエージェント並列協調・GPT-5.6セキュアコードレビュー・脅威モデリング(A-3) |
| [INFO-052](../Information/2026-07-10/collected-raw.md#INFO-052) | AI API価格崩壊: トークン指数高値から約20%下落・中国モデル米国企業使用増(A-2) |
| [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) | GLM-5.2: オープンウェイト#1・全体4位・$1.40/$4.40・OSS-クローズドギャップ縮小(B-3) |
| [INFO-060](../Information/2026-07-10/collected-raw.md#INFO-060) | 2026年重要7ベンチマーク: MMLU-Pro/GPQA/SWE-bench/HLE/Chatbot Arena/SimpleBench/ARC-AGI-2。MMLU 90%超で飽和(C-3) |
| [INFO-061](../Information/2026-07-10/collected-raw.md#INFO-061) | GPT-5.6 Sol ARC-AGI-3 7.8%: 初の有意義な進歩・Terminal-Bench 91.9%・1.72x効率(A-2) |
| [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) | 企業AI採用率: Anthropic 41%首位・OpenAI 39.5%横ばい・2024年12月10.6%から(B-3) |
| [INFO-067](../Information/2026-07-10/collected-raw.md#INFO-067) | Jalapeño: AI設計チップ9ヶ月開発・インフラ前提の有効期限(C-3) |
| [INFO-075](../Information/2026-07-10/collected-raw.md#INFO-075) | G7: Altman/Hassabis/Amodei AGI討議・米国主導国際AI連合・強いAGI 2031-2035(B-2) |
| [INFO-091](../Information/2026-07-10/collected-raw.md#INFO-091) | AI API価格表: Gemini 3.5 Flash $1.50・DeepSeek V4 Pro $1.74・GPT-5.2/5.3 Codex $1.75・Sonnet 5 $3・Opus 4.8 $5(B-2) |
| [INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) | GPT-5.6（Sol/Terra/Luna）GA: 3ティア・ARC-AGI-3 7.8%・Terminal-Bench 91.9%・1.72x効率・マルチホップ88%(A-2) |
| [Arbiter v4.31](../state/arbiter-2026-07-10.md) | 確度評価の完全根拠 |
