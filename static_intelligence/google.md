# Google / DeepMind

> 最終判断更新: 2026-05-18
> 全体確信度: 中
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。TPU 対 NVIDIA の電力効率が外部から測れない
> 主参照: hypotheses.json#H-GOO-001/002/003, indicators.json#IND-001/006/025/027/030

## 0. 一文要約

我々はGoogleを、**Gemini 3.1 Proリリースで性能競争力を示しつつ、围い込みが13件に蓄積し開放証拠が13R連続で不在の企業**と読んでいる。最大の根拠は、Gemini 3.1 ProがARC-AGI-2で前世代の2倍性能を達成し [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041)、Cloud $20.03B/63% YoYと$462Bバックログが示す収益の構造性 [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) だ。围い込みはGemini Enterprise Agent Platformの包括的スタック [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) とGemini Spark常時稼働依存 [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) で13件に達し、開放C証拠は13R連続で完全に不在である [H-GOO-002](../config/hypotheses.json) 39%。SaaStr調査でGemini採用率27%→40%(+48%)だが [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025)、Claude +128%と比較してGoogle固有要因の分離ができない。もしWorkspace内Gemini利用率が3四半期連続で頭打ちになるか、围い込みが規制当局の介入を引き起こすなら、コア判断の前提が変わる。

## 1. コア判断

Googleの競争力の本体は、20億人規模の配布チャネルとTPUインフラとDeepMindの研究深度の三位一体にある。H-GOO-003の命題を「DeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する」に修正後、48%で安定化が続いている。

Gemini 3.1 Proは今回の最も具体的な性能証拠だ。ARC-AGI-2で前世代の2倍性能、MMLU-Pro 89.8%(RAG最適)を達成した [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041)。Google I/O 2026(5月18-19日)での詳細発表が控えている。Gemini 3 Pro Deep Thinkはマルチモーダルベンチマーク100%を維持し [INFO-018](../Information/2026-05-17/collected-raw.md#INFO-018)、GPQA Diamond 94.3%でGPT-5.5の93.6%を上回る [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046)。エコシステム側では、金融サービス向け10エージェントテンプレート、Moody's MCP app、Lenovo AI Library等が参入障壁を下げている。

围い込みはむしろ加速している。Gemini Enterprise Agent Platformは構築・スケール・ガバナンスを一体化した包括的スタックとして機能し [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007)、100万トークンコンテキストウィンドウとLive APIによるリアルタイム音声/動画対話でエコシステムへの依存を深める。Gemini Sparkは常時稼働AIエージェントで、ユーザーのアプリに接続して行動を観察・学習しプロアクティブに代行する [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024)。この2件で围い込み証拠は13件に達し、開放C証拠は13R連続で不在である。H-GOO-002は39%に低下した。

市場シェアデータは二面性を持つ。SaaStr調査でGemini採用率27%→40%(+48%)を記録したが [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025)、同時にClaude +128%(21%→48%)の急成長も観測された。「業界全体押し上げ」の代替説明が13R未解決で、Google固有要因を分離できない。この代替説明未解決がH-GOO-001を54%に押し下げている。

DeepMind従業員が軍事AI取引を巡り組合化に投票した事実は [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028)、研究卓越性から製品競争力への因果が実行レイヤーで阻害されるリスクを具現化している。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Gemini 3.1 Pro: ARC-AGI-2前世代2倍・MMLU-Pro 89.8%・RAG最適 | フロンティアモデルの新規リリース。性能競争力の直接証拠 | B-3 | [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) |
| 高 | Gemini Enterprise Agent Platform: 構築・スケール・ガバナンス一体化・100万context・Live API | 围い込み13件目。エコシステム依存を構造的に深化させる包括的スタック | A-3 | [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) |
| 高 | Gemini Spark: 常時稼働AIエージェント・アプリ接続→行動観察→プロアクティブ代行 | 围い込みの新ベクトル。常時依存関係の創出 | C-3 | [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) |
| 高 | Cloud $20.03B/63% YoY、GenAI 800% YoY、バックログ $462B | エコシステム収益が構造的に拡大。コア判断の基盤 | A-2 | [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) |
| 高 | 围い込み13件蓄積 + 開放C 13R連続不在 | H-GOO-002 39%。围い込み方向が一貫して強化。非対称性拡大 | A-3 | [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) |
| 高 | SaaStr: Gemini +48%(27%→40%)。Claude +128%(21%→48%)。「業界全体押し上げ」代替説明13R未解決 | Google固有要因の分離不能。H-GOO-001 54%押し下げ要因 | B-3 | [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) |
| 高 | DeepMind従業員組合化投票(軍事AI取引) | 研究卓越性→製品競争力の因果が実行レイヤーで阻害されるリスク | B-2 | [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) |
| 中 | AlphaEvolve アルゴリズム発見エージェント稼働 | DeepMind研究卓越性の製品化証拠。H-GOO-003支持 | A-3 | [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Workspace 内 Gemini の DAU/MAU または利用率が3四半期連続で頭打ちを示す | 「エコシステム統合優位」のコア判断と [H-GOO-001](../config/hypotheses.json) が崩れる | 180日 | [IND-006](../config/indicators.json) |
| 「業界全体押し上げ」代替説明を14R目でも解決できず、Gemini固有成長の証拠が出ない | H-GOO-001を更に-1%検討。Google固有要因の分離が構造的に不能の可能性 | 30日 | [IND-006](../config/indicators.json) |
| 围い込み証拠が15件を超え、開放C証拠が引き続き不在のまま規制当局が介入する | [H-GOO-002](../config/hypotheses.json) が棄却水準に到達。围い込みリスクがコア判断の脅威に昇格 | 120日 | [IND-027](../config/indicators.json) |
| DeepMind の研究成果が Gemini 製品に統合されない状態が4四半期続く | [H-GOO-003](../config/hypotheses.json) の「研究卓越性から製品競争力」因果が崩れる | 180日 | [IND-001](../config/indicators.json) |
| OpenAI / Anthropic が自前 TPU 相当のインフラを持つか、TPU を外部調達できるようになる | 「TPU 自前インフラの差別化」が崩れ、[H-GOO-002](../config/hypotheses.json) の再評価が必要 | 90日 | [IND-001](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | Gemini統合でエコシステム収益を拡大する | 54% | Cloud $20B/63% YoYは強力C。Gemini +48%(INFO-025 B-3)はgenuine CだがClaude +128%と比較でGoogle固有要因分離不能。「業界全体押し上げ」代替説明13R未解決で条件充足し54%に低下 | [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) | 代替説明13R未解決 |
| [H-GOO-002](../config/hypotheses.json) | 围い込み回避で開放維持 | 39% | Chrome DevTools MCP [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024)・TikTok MCP [INFO-014](../Information/2026-05-17/collected-raw.md#INFO-014)・Boomi MCP Registry [INFO-056](../Information/2026-05-17/collected-raw.md#INFO-056) は開放C。围い込み13件I蓄積(直近: Gemini Enterprise Agent Platform [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007)+Gemini Spark [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024))。開放C証拠13R連続不在 | [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) [INFO-014](../Information/2026-05-17/collected-raw.md#INFO-014) [INFO-056](../Information/2026-05-17/collected-raw.md#INFO-056) | [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) |
| [H-GOO-003](../config/hypotheses.json) | DeepMind統合シナジーで競争力を維持する | 48% | Gemini 3.1 Pro ARC-AGI-2 2x [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) は性能C。AlphaEvolve [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) は研究卓越性C。DeepMind組合 [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) は内部摩擦I。ペナルティ停止後安定化継続 | [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) | [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt 以上/期で high | Gemini 3.1 Pro ARC-AGI-2 前世代2x [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041)。GPQA Diamond 94.3% [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046)。MMMU-Pro 88.21%首位 | 2026-05-18 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated 維持で継続監視 | Gemini Enterprise Agent Platform [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007)。Gemini Spark [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024)。Interactions API [INFO-009](../Information/2026-05-17/collected-raw.md#INFO-009) | 2026-05-18 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Gemini 3.1 Pro ARC-AGI-2 2x [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041)。Gemini 3 Pro DT multimodal 100% [INFO-018](../Information/2026-05-17/collected-raw.md#INFO-018) | 2026-05-18 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | high / rising | Grok Build ACP [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006)+MCP 2026 [INFO-015](../Information/2026-05-18/collected-raw.md#INFO-015)。围い込み13件と開放の非対称性拡大 | 2026-05-18 |
| [IND-030](../config/indicators.json) | AI 能力とリスクの二面性 | elevated / rising | Pentagon saga A-2 [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036)+EU AI Act [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028)+DeepMind組合 [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) | 2026-05-18 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-18 | Gemini 3.1 Proリリース・Gemini Enterprise Agent Platform・Gemini Spark・围い込み13件目を反映して全面更新 | [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) | H-GOO-001 55→54%・H-GOO-002 40→39%・H-GOO-003 48%維持・围い込み12→13件・開放C 13R連続不在 |
| 2026-05-17 | Gemini Interactions API・Vertex AI Agent Builder・DeepMind組合化投票を反映 | [INFO-009](../Information/2026-05-17/collected-raw.md#INFO-009) [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) | H-GOO-001 55%・H-GOO-002 43→40%・围い込み6→12件 |
| 2026-05-14 | Pentagon秘密AI契約・AndroidエージェントAI・Chrome DevTools MCPを反映 | 複数INFO | 「三位一体」→「Pentagon契約で政府市場参入だが内部摩擦」 |
| 2026-05-08 | [H-GOO-003](../config/hypotheses.json) 仮説修正実行。「フロンティア性能競争」→「DeepMind統合シナジー」 | AlphaEvolve | H-GOO-003 49→48%・low帯 |

## 7. ブラインドスポット

- H-GOO-003 の評価指標がまだ不十分。「エコシステム深度・研究卓越性・インフラ統合」の3軸それぞれについて独立評価する定量指標を持っていない。
- DeepMind組合化の実効力が外部から測れない。軍事AI取引の実行にどの程度の影響を与えるかが不透明。
- Workspace 内 Gemini の DAU/MAU が公開されていない。「Cloud 顧客の 75% が AI 製品を使用」は投入量であって利用深度ではない。
- 「業界全体押し上げ」代替説明が13R未解決。Google固有の成長要因をClaude +128%等の他社成長から分離する方法論を持っていない。
- 围い込み13件蓄積に対する規制当局(EU DMA/DOJ)の動向が外部から不透明。围い込み行為と規制判断の対応関係を評価できない。
- Gemini Sparkが「開発中」であり、仕様・提供時期が不確定。常時稼働依存の围い込み効果は予測にすぎない。

## 付録: 直近30日の参照 Evidence

| Evidence | 用途 |
|---|---|
| [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) | Gemini 3.1 Pro(ARC-AGI-2 2x・MMLU-Pro 89.8%) |
| [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) | Gemini Enterprise Agent Platform(包括的スタック・100万context・Live API) |
| [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) | Gemini Spark(常時稼働AIエージェント・アプリ接続・行動観察) |
| [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) | SaaStr: Gemini +48%(27→40%) vs Claude +128%(21→48%) vs OpenAI -8% |
| [INFO-009](../Information/2026-05-17/collected-raw.md#INFO-009) | Gemini Interactions API(サーバー側状態管理) |
| [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) | DeepMind従業員組合化投票(軍事AI取引) |
| [INFO-018](../Information/2026-05-17/collected-raw.md#INFO-018) | Gemini 3 Pro Deep Think マルチモーダル100% |
| [INFO-023](../Information/2026-05-17/collected-raw.md#INFO-023) | Vertex AI Agent Builder Gemini/BigQuery統合 |
| [INFO-039](../Information/2026-05-17/collected-raw.md#INFO-039) | Gemini 3.1 Flash Lite $0.10-$0.40/M tokens |
| [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) | Pentagon秘密AI契約 + 従業員抗議 |
| [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) | Chrome DevTools MCP |
| [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) | Gemma 4 MTP 3x高速化・初週60M DL |
| [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) | Gemini 3.1 Pro GPQA Diamond 94.3% |
| [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) | AlphaEvolve アルゴリズム発見エージェント |
| [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) | Cloud $20.03B/63% YoY・GenAI 800%・バックログ $462B |
| [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) | AAIF/MCP統合 |
| [INFO-014](../Information/2026-05-17/collected-raw.md#INFO-014) | Boomi MCP Registry |
| [INFO-056](../Information/2026-05-17/collected-raw.md#INFO-056) | TikTok MCP server |
| [Arbiter v3.81](../state/arbiter-2026-05-18.md) | H-GOO-001/002/003確度評価の完全根拠 |
