# OpenAI

> 最終判断更新: 2026-05-15
> 全体確信度: 中
> 主参照: hypotheses.json#H-OAI-001/002/003, indicators.json#IND-001/IND-013/IND-026/IND-027/IND-029

## 0. 一文要約

我々はOpenAIを、**Codexのモバイル展開とDeployCo($40億+)でエンタープライズ展開インフラを固めながら、围い込み戦略が構造的に後退している企業**と読んでいる。最大の根拠は、CodexがiOS/Androidでリモートセッション管理・承認を可能にし週間400万ユーザーに到達した事実 [INFO-001](../Information/2026-05-15/collected-raw.md#INFO-001) と、DeployCoがTPG/Advent/Goldman Sachs主導で$40億+を集めた事実 [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) だ。他方で、ファインチューニングAPI縮小・GPT-5 Pro価格上昇($15/$120)による開発者離反 [INFO-024](../Information/2026-05-15/collected-raw.md#INFO-024) に加え、Grok Build CLI [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) やSKILL.md 300+ [INFO-017](../Information/2026-05-15/collected-raw.md#INFO-017) やAWS Agent Toolkit [INFO-019](../Information/2026-05-15/collected-raw.md#INFO-019) による围い込み否定の8重蓄積が観測された。H-OAI-002は48%に低下しlow帯に確定移行した。DeployCoのFDE常駐モデルが12ヶ月以内に解約か縮小に至る、またはLLM支出シェアが27%から20%以下に下落する、のいずれかが観測されたら、この読みは変わる。

## 1. コア判断

OpenAIの戦略は二つの動きの同時進行という段階に入っている。エンタープライズ展開インフラの強化と、围い込み戦略の構造的後退だ。

Codexのモバイル統合は [INFO-001](../Information/2026-05-15/collected-raw.md#INFO-001)、エンタープライズ向けの投入として意味がある。iOS/AndroidからリモートCodexセッションの管理・承認が可能になり、Remote SSHの一般提供、Programmatic access tokens、HIPAA準拠対応も発表された。週間400万人以上がCodexを利用している。DeployCoはTPG主導で$40億以上の初期投資を集め [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003)、Tomoro買収で約150名のFDEを獲得した。McKinsey、Bain等19社のパートナーが参加する。Sora 2の終了と計算資源のロボティクス転用 [INFO-015](../Information/2026-05-15/collected-raw.md#INFO-015) は、映像生成市場からの撤退を意味する資源集中の判断だ。

しかし围い込み戦略は後退している。ファインチューニングAPIの段階的縮小とGPT-5 Pro $15/$120の価格改定は [INFO-024](../Information/2026-05-15/collected-raw.md#INFO-024) 開発者コミュニティの反発を招いている。xAIのGrok Build CLIがMCP/AGENTS.md対応で登場し [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004)、SKILL.mdフォーマットが300以上のスキルで採用され [INFO-017](../Information/2026-05-15/collected-raw.md#INFO-017)、AWS Agent ToolkitがMCP serversの後継として登場した [INFO-019](../Information/2026-05-15/collected-raw.md#INFO-019)。これら围い込み否定の8重蓄積でH-OAI-002は48%に低下し、50%境界を下回ってlow帯に確定移行した。

ChatGPTの安全性機能も強化された。会話内のリスク信号を認識するコンテキスト認識機能で、自傷・他害シナリオの安全応答率が50%改善した [INFO-002](../Information/2026-05-15/collected-raw.md#INFO-002)。3つのリアルタイム音声モデル(GPT Realtime 2/Translate/Whisper)も投入された [INFO-014](../Information/2026-05-15/collected-raw.md#INFO-014)。ChatGPT広告は日本・韓国等に展開を拡大している [INFO-028](../Information/2026-05-15/collected-raw.md#INFO-028)。

確証バイアス警告が4R連続で発出されている。各ラウンドの新証拠が常に「最も強力なC」と評価される構造自体が確証バイアスの指標であり、H-OAI-001の64%が過大評価されている可能性がある。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | DeployCo設立: $40億+初期投資・Tomoro買収・19パートナー・FDE常駐モデル | API提供から展開サービス会社への戦略的飛躍 | A-3 | [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) |
| 高 | Codexモバイル統合(iOS/Android)・Remote SSH GA・Programmatic access・HIPAA準拠・週間400万WAU | エンタープライズ導入の摩擦低減。H-OAI-001のC | A-3 | [INFO-001](../Information/2026-05-15/collected-raw.md#INFO-001) |
| 高 | 围い込み否定8重蓄積: Grok Build CLI+SKILL.md 300++AWS Agent Toolkit+FT API縮小 | H-OAI-002が48%low帯に確定移行。围い込み戦略の構造的後退 | A-3/B-3 | [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) [INFO-017](../Information/2026-05-15/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-15/collected-raw.md#INFO-019) [INFO-024](../Information/2026-05-15/collected-raw.md#INFO-024) |
| 高 | ファインチューニングAPI段階的縮小 + GPT-5 Pro $15/$120価格改定 | 開発者エコシステムとの関係悪化リスク。围い込みの逆効果 | B-3 | [INFO-024](../Information/2026-05-15/collected-raw.md#INFO-024) |
| 高 | Sora 2終了・計算資源ロボティクス転用 | 映像生成市場撤退。資源集中の意思決定速度 | B-3 | [INFO-015](../Information/2026-05-15/collected-raw.md#INFO-015) |
| 高 | ChatGPT安全性50%改善(自傷・他害コンテキスト認識) | 安全性投資の継続。防御側強化 | A-3 | [INFO-002](../Information/2026-05-15/collected-raw.md#INFO-002) |
| 中 | 3リアルタイム音声モデル(Realtime 2/Translate/Whisper)・コンテキスト128K | 音声AI市場への本格参入。新収益柱 | B-3 | [INFO-014](../Information/2026-05-15/collected-raw.md#INFO-014) |
| 中 | ChatGPT広告日本・韓国展開(Free/Go層) | 収益多様化の継続。H-OAI-002围い込みを弱める要素 | B-3 | [INFO-028](../Information/2026-05-15/collected-raw.md#INFO-028) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DeployCoのFDE常駐モデルが12ヶ月以内に解約または大幅縮小に至る | 「展開能力が競争軸になる」という読みとH-OAI-001の根拠が崩れる | 365日 | [IND-029](../config/indicators.json) |
| ファインチューニングAPI縮小による開発者離反がAPI収益の5%以上に影響する | H-OAI-002围い込み戦略の限界が露呈し、下層開放圧力が上層围い込みを無効化する | 180日 | [IND-027](../config/indicators.json) |
| LLM支出シェアが27%から20%以下に下落(Anthropic・Google双方に侵食) | H-OAI-001(エンタープライズ支配的地位の確立)が棄却水準に達する | 90日 | [IND-026](../config/indicators.json) |
| Sora 2終了後のロボティクス転用が6ヶ月以内に具体的成果を出さない | 資源集中の意思決定が撤退でなく単なる縮小だった可能性が高まる | 180日 | [IND-001](../config/indicators.json) |
| SKILL.md等のオープン標準がCodex独自実装を完全に代替する | H-OAI-002が棄却水準に達し、围い込み戦略の破綻が確定する | 180日 | [IND-027](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 64% | DeployCo $40億+・Codex 4M WAU・Codexモバイル統合・HIPAA準拠でC蓄積。$14B損失とLLMシェア27%が同数I。確証バイアス警告4R連続発出。DeployCo収益の独立確認不在 | [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) [INFO-001](../Information/2026-05-15/collected-raw.md#INFO-001) [INFO-002](../Information/2026-05-15/collected-raw.md#INFO-002) | [INFO-024](../Information/2026-05-15/collected-raw.md#INFO-024) [INFO-015](../Information/2026-05-15/collected-raw.md#INFO-015) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放エコシステム上にプロプライエタリ上位レイヤーを構築する | 48% | 8重I蓄積(Grok Build MCP+SKILL.md 300++AWS Toolkit+FT API縮小)で围い込み否定が構造的。low帯確定(50%境界下回り) | [INFO-001](../Information/2026-05-15/collected-raw.md#INFO-001) | [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) [INFO-017](../Information/2026-05-15/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-15/collected-raw.md#INFO-019) [INFO-024](../Information/2026-05-15/collected-raw.md#INFO-024) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% | DeployCo収益のAGI再投資はCだが、商業化規模・速度が研究出力を圧倒的に凌駕。Sora 2終了も商業集中のI | [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) | [INFO-024](../Information/2026-05-15/collected-raw.md#INFO-024) [INFO-015](../Information/2026-05-15/collected-raw.md#INFO-015) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能の非連続ジャンプ | +5pt以上/期で high | BenchLM 92(3位)。ARC-AGI-2 83.3%。Terminal-Bench 82.7% | 2026-05-15 |
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントで critical | ChatGPT安全性50%改善+Sandbox Runtime OSSで防御強化。新規脆弱性なし。high水準 | 2026-05-15 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | CEO 83%導入予定 vs CIO 25%監視可能。期待-実態ギャップ拡大。elevated水準 | 2026-05-15 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用で high | SKILL.md 300++Grok Build MCP対応+AWS Agent Toolkit MCP後継。標準化加速と围い込み同時進行。high水準 | 2026-05-15 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限り high | DeployCo $40億++$900B DC市場+Big 4 $725B。資本流入加速。high水準 | 2026-05-15 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-15 | Codexモバイル統合・ChatGPT安全性50%改善・围い込み否定8重蓄積でH-OAI-002 low帯確定移行を反映して全面書き直し | [INFO-001](../Information/2026-05-15/collected-raw.md#INFO-001) [INFO-002](../Information/2026-05-15/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) [INFO-017](../Information/2026-05-15/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-15/collected-raw.md#INFO-019) | 「製品ポートフォリオ整理と新規展開が同時進行」→「CodexモバイルとDeployCoでエンタープライズ固める。围い込み否定8重蓄積でH-OAI-002 low帯確定(48%)」 |
| 2026-05-14 | ファインチューニングAPI縮小・Sora 2終了・GPT-Realtime 3モデル・ChatGPT広告日本展開を反映して全面書き直し | 2026-05-14複数INFO | 「DeployCoで展開インフラ支配に飛躍」→「製品ポートフォリオ整理(FT API縮小+Sora 2終了)と音声3モデル新規展開が同時進行」 |
| 2026-05-12 | DeployCo + GPT-5.5-Cyber + Trusted Contact + H-OAI-003「棄却確定」→「確度極低」を反映 | 2026-05-12複数INFO | 「損失走行継続」 → 「DeployCoで展開インフラ支配に飛躍」 |
| 2026-05-08 | GPT-5.5 Instant/Cyber/Realtime-2 + $100B JV + FedRAMP + 広告 + 価格2倍 | 複数INFO | 「評価額で損失を走らせる」 → 「損失走行継続。二重JVで金融次元二重化」 |

## 7. ブラインドスポット

- DeployCo $40億+の実質額(コミットメント vs 実調達)と19パートナーの排他性が未確認。全証拠がA-3(公式発表)でB-tier以上の独立確認が0件。公式発表だけで「構造的転換」を評価する分析方法論的限界を認識している。
- ファインチューニングAPI縮小の開発者離反インパクトが定量把握できない。API収益に占めるファインチューニング利用の割合が非公表であり、反発が一時的か構造的かの判別ができない。
- Codex WAUの収益転換率が非公表。400万WAUが月次ARRにいくら寄与しているかを外部から追跡できない。
- 確証バイアス警告が4R連続で発出されている。各ラウンドの新証拠が常に「最も強力なC」と評価される構造自体が確証バイアスの指標であり、H-OAI-001の64%が過大評価されている可能性がある。
- Sora 2終了後のロボティクス転用がどの程度の計算資源を確保できるか不明。ロボティクス分野でのOpenAIの競争力も未検証。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-05-15/collected-raw.md#INFO-001) | Codexモバイル統合(iOS/Android・Remote SSH GA・Programmatic access・HIPAA) |
| [INFO-002](../Information/2026-05-15/collected-raw.md#INFO-002) | ChatGPT安全性50%改善(コンテキスト認識・safety summaries) |
| [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) | DeployCo設立($40億+・Tomoro買収・19パートナー・FDEモデル) |
| [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) | Grok Build CLI(MCP/AGENTS.md対応) — 围い込み否定I |
| [INFO-009](../Information/2026-05-15/collected-raw.md#INFO-009) | WebSocket execution mode for Responses API |
| [INFO-014](../Information/2026-05-15/collected-raw.md#INFO-014) | 3リアルタイム音声モデル(Realtime 2/Translate/Whisper) |
| [INFO-015](../Information/2026-05-15/collected-raw.md#INFO-015) | Sora 2終了・計算資源ロボティクス転用 |
| [INFO-017](../Information/2026-05-15/collected-raw.md#INFO-017) | SKILL.md 300+ポータブルスキル — 围い込み否定I |
| [INFO-019](../Information/2026-05-15/collected-raw.md#INFO-019) | AWS Agent Toolkit(MCP後継) — 围い込み否定I |
| [INFO-024](../Information/2026-05-15/collected-raw.md#INFO-024) | GPT-5 Pro $15/$120価格・ファインチューニングAPI縮小 |
| [INFO-028](../Information/2026-05-15/collected-raw.md#INFO-028) | ChatGPT広告日本・韓国展開 |
