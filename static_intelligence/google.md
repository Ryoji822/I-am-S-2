# Google / DeepMind

> 最終判断更新: 2026-05-14
> 全体確信度: 中
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。TPU 対 NVIDIA の電力効率が外部から測れない
> 主参照: hypotheses.json#H-GOO-001/002/003, indicators.json#IND-001/006/025/027/030

## 0. 一文要約

我々はGoogleを、**エコシステム深度とTPU自前インフラとDeepMind研究卓越性の三位一体で戦う企業**と読んでいる。ただしPentagon秘密AI契約による政府市場参入と、数百人の従業員抗議という内部摩擦が同時進行している [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036)。最大の根拠は Cloud $20.03B/63% YoY と $462B バックログが示す収益の構造性 [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) と、AlphaEvolveによるアルゴリズム発見能力 [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098) が示す研究卓越性だ。Cloud Next '26は260以上の発表を投入し [INFO-009](../Information/2026-05-14/collected-raw.md#INFO-009)、Gemini Enterprise Agent Platform、第8世代TPU、Gemma 4、Deep Research Maxを一挙に展開した。AndroidにエージェントAIを導入し [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023)、Chrome DevTools MCPをOSS化し [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024)、配布チャネルの厚みを強化している。一方で围い込み証拠が6件に蓄積し [H-GOO-002](../config/hypotheses.json) は43%に低下、開放C証拠は完全に不在である。もし Workspace 内 Gemini 利用率が3四半期連続で頭打ちになるか、Pentagon契約の従業員抗議が実行停止に至るなら、コア判断の前提が変わる。

## 1. コア判断

Google の競争力の本体は、ベンチマークスコアではなく20億人規模の配布チャネルとTPUインフラとDeepMindの研究深度の三位一体にある。この読みに到達するまでに10R以上を要した。H-GOO-003 を「フロンティア性能競争で対抗」という枠組みで測り続けた結果、確度は55%から49%へ下がり続けた。低下の原因は枠組みそのものがGoogleの強みを系統的に見落としていたことにある。命題を「DeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する」に修正後、ペナルティは停止し48%で安定化が続いている。

Cloud 側の数値は構造性を示している。$20.03B/63% YoY、GenAI 製品 800% YoY、バックログ $462B [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027)。Cloud Next '26では260以上の発表を一挙に投入し [INFO-009](../Information/2026-05-14/collected-raw.md#INFO-009)、Cloud 顧客の 75% が AI 製品を使い、330 組織が年間 1T 超のトークンを処理している [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)。Gemini Enterprise Agent Platform は構築・スケール・ガバナンスを一体化したプラットフォームに進化し [INFO-019](../Information/2026-05-08/collected-raw.md#INFO-019)、エコシステムの厚みが増している。Gemini CLIにはFirebase agent skills、DevOps extension、Data Agent Kitが追加され [INFO-028](../Information/2026-05-14/collected-raw.md#INFO-028)、開発者エコシステムの拡張も進む。

製品側は複数の新戦線が開かれた。AndroidにエージェントAIとバイブコーディングウィジェットを導入し [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023)、Gboard「Rambler」でGeminiマルチモーダル機能を組み込んだ。Gemini Omni統合マルチモーダルモデルがリークされており、配布チャネルの深度がさらに強化される可能性がある。Chrome DevTools MCPは [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024)、Gemini/Claude/Cursor/Copilot等のコーディングエージェントがライブChromeブラウザを制御可能にするOSSで、Googleがブラウザインフラの開放と同時にエコシステム中心性を強化する構図である。

研究側ではAlphaEvolveがアルゴリズム発見エージェントとして稼働し [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098)、DeepMind Co-Clinician は GPT-5.4 の 30% に対して 63% の正確性を記録した [INFO-078](../Information/2026-05-08/collected-raw.md#INFO-078)。Gemma 4はMTP draftersで最大3倍の推論高速化を実現し、初週6000万ダウンロードを記録、Apache 2.0ライセンスで提供されている [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008)。Gemini 3.1 ProはGPQA Diamond 94.3%でGPT-5.5の93.6%を上回るが [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046)、GPT-5.5がARC-AGI v2でリードしており、モデル間の得意領域分化が進行中である。Gemini 3.1 Flash Liteは$0.125/$0.75 per 1M tokensで価格競争力を示している [INFO-045](../Information/2026-05-14/collected-raw.md#INFO-045)。

政府側ではPentagon秘密AI契約が新たな変数である。GoogleがPentagonと秘密AI契約を締結した一方で [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036)、数百人の従業員が抗議している。AnthropicはPentagon契約を拒否しており、両社の立場の対比が鮮明である。これは政府市場参入の機会であると同時に内部摩擦のリスクでもある。DeepMind union 98% [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) と合わせて、組織の実行力に影響する監視ポイントである。

围い込み証拠は6件に蓄積した。Workspace無料围い込み、围い込み宣言、Gemini Enterprise統合スタック、VertexからGemini Enterpriseへの移行、AI Search围い込み深化に続き、Flash Lite価格設定が6件目のI証拠として追加された [INFO-045](../Information/2026-05-14/collected-raw.md#INFO-045)。開放C証拠は完全に不在であり、[H-GOO-002](../config/hypotheses.json) は43%に低下した。AAIF/MCP統合 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) と Red Hat MCP Gateway [INFO-033](../Information/2026-05-08/collected-raw.md#INFO-033) は開放標準への取り組みを示しているが、围い込みと開放の二重構造が継続している。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Cloud $20.03B/63% YoY、GenAI 800% YoY、バックログ $462B | エコシステム収益が構造的に拡大していることの直接証拠 | A-2 | [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) |
| 高 | Cloud Next '26 260+発表、顧客75%AI利用、330組織1T+トークン処理 | エコシステム深度の全面的な強化。Cloud顧客の埋め込みが加速 | A-3 | [INFO-009](../Information/2026-05-14/collected-raw.md#INFO-009) [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) |
| 高 | AlphaEvolve アルゴリズム発見エージェント稼働 | DeepMind の研究卓越性が製品化された証拠。H-GOO-003 新命題を直接支持 | A-3 | [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098) |
| 高 | Gemini Enterprise Agent Platform 正式リリース | Google がプラットフォーム側に回りつつある。モデル単体ではなく基盤を売る構造への転換 | A-2 | [INFO-019](../Information/2026-05-08/collected-raw.md#INFO-019) |
| 高 | Pentagon 秘密AI契約 + 数百人従業員抗議 | 政府市場参入の機会だが内部摩擦が同時進行。Anthropic(拒否)との対比が鮮明 | B-3 | [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) |
| 高 | Android エージェントAI + Gemini Omni リーク | 20億人規模の配布チャネルにエージェント機能を直接組み込む。エコシステム深度の強化 | B-3 | [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) |
| 中 | Chrome DevTools MCP ローンチ(OSS) | ブラウザインフラの開放とエコシステム中心性の同時強化。新規開源製品 | A-3 | [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) |
| 中 | Gemma 4 MTP 3x高速化、初週60M DL、Apache 2.0 | オープンソースモデルの競争力向上。配布チャネルの多様化 | A-3 | [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) |
| 中 | Gemini 3.1 Pro GPQA Diamond 94.3% vs GPT-5.5 93.6% | 科学推論で首位だがARC-AGI v2はGPT-5.5がリード。モデル分化進行 | B-3 | [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) |
| 中 | 围い込み6件目I蓄積(Flash Lite価格) + 開放C完全不在 | H-GOO-002 43%。围い込み方向が一貫して強化。二重構造の非対称性拡大 | A-3 | [INFO-045](../Information/2026-05-14/collected-raw.md#INFO-045) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Workspace 内 Gemini の DAU/MAU または利用率が3四半期連続で頭打ちを示す公式開示 | 「エコシステム統合優位」のコア判断と [H-GOO-001](../config/hypotheses.json) が崩れる | 180日 | [IND-006](../config/indicators.json) |
| Pentagon契約の従業員抗議が拡大し実行停止または大幅縮小に至る | 政府市場参入の機会損失が確定し、内部摩擦がエコシステム実行力に波及 | 60日 | [IND-030](../config/indicators.json) |
| OpenAI / Anthropic が自前 TPU 相当のインフラを持つか、TPU を外部調達できるようになる | 「TPU 自前インフラの差別化」が崩れ、[H-GOO-002](../config/hypotheses.json) の再評価が必要 | 90日 | [IND-001](../config/indicators.json) |
| エンタープライズLLMシェアで Google が 21% から低下し続け、Anthropic や OpenAI との差が拡大する | エコシステム優位が収益に転換できていないことになり、コア判断全体が疑われる | 90日 | [IND-006](../config/indicators.json) |
| DeepMind の研究成果が Gemini 製品に統合されない状態が4四半期続く | [H-GOO-003](../config/hypotheses.json) の「研究卓越性→製品競争力」因果が崩れる | 180日 | [IND-001](../config/indicators.json) |
| 围い込み証拠が7件目・8件目と蓄積し、開放C証拠が引き続き不在のまま規制当局が介入する | [H-GOO-002](../config/hypotheses.json) がlow帯に転落し、围い込みリスクがコア判断の脅威に昇格 | 120日 | [IND-027](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | Gemini 統合でエコシステム収益を拡大する | 54% | Cloud $20B/63% YoY と Gemini Enterprise Agent Platform [INFO-019](../Information/2026-05-08/collected-raw.md#INFO-019) が支持。Cloud Next 260+発表 [INFO-009](../Information/2026-05-14/collected-raw.md#INFO-009) でエコシステム深度強化。ただし800%収益成長基数不明が7R目未解決。エンタープライズLLMシェアが Anthropic 40% に劣後しており、投入指標と成果指標の乖離が残る。Pentagon契約で政府市場参入の新経路が開いたが実行リスクあり | [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) [INFO-009](../Information/2026-05-14/collected-raw.md#INFO-009) | エンタープライズLLMシェアの継続低下 |
| [H-GOO-002](../config/hypotheses.json) | 围い込み回避で開放維持 | 43% | AAIF/MCP統合 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) と Red Hat MCP Gateway [INFO-033](../Information/2026-05-08/collected-raw.md#INFO-033) が開放を支持。围い込み6件目I蓄積(1:Workspace無料围い込み・2:围い込み宣言・3:Gemini Enterprise統合スタック・4:Vertex→Gemini Enterprise移行・5:AI Search围い込み深化・6:Flash Lite価格围い込み [INFO-045](../Information/2026-05-14/collected-raw.md#INFO-045) A-3)。開放C証拠完全不在。low帯移行検討条件に接近 | [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) [INFO-033](../Information/2026-05-08/collected-raw.md#INFO-033) [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) | [INFO-076](../Information/2026-05-08/collected-raw.md#INFO-076) [INFO-045](../Information/2026-05-14/collected-raw.md#INFO-045) 围い込み6件蓄積 |
| [H-GOO-003](../config/hypotheses.json) | DeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% | 仮説修正実行済み(v3.71)。AlphaEvolve [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) は研究卓越性C。Gemma 4 MTP 3x高速化+60M DL [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) はインフラ統合C。Gemini 3.1 Pro GPQA Diamond 94.3% [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) は性能C。DeepMind union 98% [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) は内部摩擦I。ペナルティ停止後安定化継続 | [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) | [INFO-054](../Information/2026-05-08/collected-raw.md#INFO-054) [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt 以上/期で high | BenchLM 93 (3位)、MMMU-Pro 88.21% 首位、ARC-AGI-2 77.1%。Gemini 3.1 Pro GPQA Diamond 94.3% [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) | 2026-05-14 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated 維持で継続監視 | Gemini Enterprise Agent Platform [INFO-019](../Information/2026-05-08/collected-raw.md#INFO-019)。AAIF/MCP 統合 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032)。Gemini CLI拡張(Firebase/DevOps) [INFO-028](../Information/2026-05-14/collected-raw.md#INFO-028) | 2026-05-14 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Claude Design/Sonnet 4.6 OSWorld改善 [INFO-007](../Information/2026-05-14/collected-raw.md#INFO-007)。Gemini API File Searchマルチモーダル対応 [INFO-007](../Information/2026-05-14/collected-raw.md#INFO-007)。量的向上継続。「真の理解」検証未解決 | 2026-05-14 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | high / rising | 標準化加速(AAIF 97M+ SDK DL・Chrome DevTools MCP [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024)) + Gemini Enterprise围い込み同時進行。围い込み6件目I蓄積 | 2026-05-14 |
| [IND-030](../config/indicators.json) | AI 能力とリスクの二面性 | elevated / rising | Pentagon秘密AI契約+従業員抗議 [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) + DeepMind union 98% [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) + EU Act延期 + 中国規制。規制二方向同時進行深化 | 2026-05-14 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-14 | Pentagon秘密AI契約+従業員抗議・AndroidエージェントAI+Gemini Omniリーク・Chrome DevTools MCP・Gemma 4 MTPを反映して全面書き直し | [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) | 「エコシステム深度とTPUと研究卓越性の三位一体」→「三位一体維持。Pentagon契約で政府市場参入だが内部摩擦。围い込み6件目I蓄積」 |
| 2026-05-12 | §4 §5 更新(H-GOO-002 44%・围い込み5件目I蓄積・IND値最新化) | [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005) AI Search围い込み深化 | H-GOO-002 45→44%・IND-025最新化 |
| 2026-05-08 | [H-GOO-003](../config/hypotheses.json) 仮説修正実行。命題を「フロンティア性能競争」から「DeepMind統合シナジー（エコシステム深度・研究卓越性・インフラ統合）」に変更 | AlphaEvolve [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098) + BenchLM Gemini 3 Pro首位 [INFO-040](../Information/2026-05-08/collected-raw.md#INFO-040) + Hermes 94.1% [INFO-054](../Information/2026-05-08/collected-raw.md#INFO-054) | 「性能競争で対抗する企業（仮説修正中）」→「エコシステム深度と研究卓越性で競争力を維持する企業」 |
| 2026-05-08 | AlphaEvolve、DeepMind Co-Clinician、Workspace Gemini 無料围い込み、Pentagon 7社契約選出 + 従業員抗議を反映して全面更新 | H-GOO-003 修正実行 + 新規証拠 | H-GOO-003 49%→48%（low）、H-GOO-002 48%（low） |
| 2026-05-06 | H-GOO-003 仮説修正命令発出。コア判断を「性能競争への枠組み」から「エコシステム統合優位」へ修正開始 | BenchLM 3位 (93 vs Mythos 99) と10R連続確度低下 [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) | 「性能競争で対抗できる企業」→「エコシステム統合とTPUで戦う企業（性能枠組みの修正中）」 |
| 2026-05-06 | Cloud $20B/63% YoY、GenAI 800%成長、Gemini Enterprise Agent Platform、xAI Grok on Google Cloud、Agent Skills、Pentagon 契約 + 従業員抗議を反映して全面更新 | 鮮度タイムアウト (7日経過) | H-GOO-001 56%、H-GOO-002 48%、H-GOO-003 49% に更新 |
| 2026-04-29 | Gemini Enterprise Agent Platform 詳細・Anthropic $40B 投資を反映 | Cloud Next 2026 後続情報 | 基本情報・戦略方向性を全面書き直し |
| 2026-04-22 | Cloud Next 2026 定量データを初反映 | Pentagon 契約交渉、$240B バックログ | 「Cloud は AWS に大差で劣後」→「急拡大フェーズ」へ読み変え |

## 7. ブラインドスポット

- **H-GOO-003 の修正は完了したが、新命題を評価する指標がまだ不十分である**。「エコシステム深度・研究卓越性・インフラ統合」の3軸それぞれについて、確度を独立に評価する定量指標を持っていない。AlphaEvolve や Co-Clinician、Gemma 4 MTP は個別の C 証拠だが、これらを体系化する指標設計が未完了である。
- **Pentagon秘密AI契約の内容・規模・期間が非公開である**。AnthropicがPentagon契約を拒否した対比は明確だが、Googleが契約した条件(データ取扱い・軍事利用の範囲・監視機能の有無)が外部から不透明である。従業員抗議の規模が「数百人」以上に拡大する可能性を評価できない。
- **Workspace 内 Gemini の DAU/MAU が公開されていない**。「Cloud 顧客の 75% が AI 製品を使用」という数値は投入量であって利用深度ではない。利用が浅い 75% と深い 30% では意味が全く異なるが、外から区別できない。
- **TPU 対 NVIDIA H200 の電力効率比較が外部から測れない**。Google が TPU 優位を主張しているが、独立した検証がない。第8世代TPUの性能向上も公式発表のみで外部検証なし。
- **Gemini Omniの実態がリーク情報のみである**。統合マルチモーダルモデルとして配布チャネルに与える影響を評価したいが、公式発表前のため仕様・性能・提供時期がすべて不確定である。
- **DeepMind の研究成果が Gemini 製品にどの程度・どの速度で統合されているかが外部から不透明である**。AlphaEvolve は研究卓越性を示すが、これが Gemini の製品競争力にどう反映されるかの因果が未確認である。

## 付録: 直近30日の参照 Evidence

| Evidence | 用途 |
|---|---|
| [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) | Pentagon秘密AI契約 + 従業員抗議 |
| [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) | AndroidエージェントAI + Gemini Omniリーク |
| [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) | Chrome DevTools MCP(エージェントブラウザ制御OSS) |
| [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) | Gemma 4 MTP drafters 3x高速化・初週60M DL |
| [INFO-009](../Information/2026-05-14/collected-raw.md#INFO-009) | Cloud Next '26 260+発表・Gemini Enterprise Agent Platform・第8世代TPU |
| [INFO-007](../Information/2026-05-14/collected-raw.md#INFO-007) | Gemini API File Searchマルチモーダル・Gemini Embedding 2 |
| [INFO-028](../Information/2026-05-14/collected-raw.md#INFO-028) | Gemini CLI拡張(Firebase/DevOps/Data Agent Kit) |
| [INFO-045](../Information/2026-05-14/collected-raw.md#INFO-045) | Gemini 3.1 Flash Lite価格($0.125/$0.75) |
| [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) | Gemini 3.1 Pro GPQA Diamond 94.3% vs GPT-5.5 93.6% |
| [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005) | AI Search 5新機能(围い込み深化) |
| [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) | Cloud $20.03B/63% YoY、GenAI 800% YoY、バックログ $462B、AIトークン 160B/分 |
| [INFO-005](../Information/2026-05-08/collected-raw.md#INFO-005) | Cloud 顧客 75% AI 利用 |
| [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) | Gemini Enterprise Agent Platform 詳細、330 社 1T+ トークン |
| [INFO-019](../Information/2026-05-08/collected-raw.md#INFO-019) | Gemini Enterprise Agent Platform 正式リリース |
| [INFO-040](../Information/2026-05-08/collected-raw.md#INFO-040) | BenchLM Gemini 3 Pro Deep Think 100% 首位 |
| [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) | BenchLM 総合 93 (3位)、Gemini 3.1 Pro vs Mythos vs GPT-5.4 Pro 比較 |
| [INFO-041](../Information/2026-05-08/collected-raw.md#INFO-041) | GPT-5.5 Terminal-Bench 82.7% |
| [INFO-054](../Information/2026-05-08/collected-raw.md#INFO-054) | Hermes GPQA Diamond 94.1% (第三者推理首位) |
| [INFO-078](../Information/2026-05-08/collected-raw.md#INFO-078) | DeepMind Co-Clinician 63% vs GPT-5.4 30% |
| [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) | AlphaEvolve アルゴリズム発見エージェント |
| [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) | AlphaEvolve 詳細 |
| [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098) | AlphaEvolve 評価 |
| [INFO-076](../Information/2026-05-08/collected-raw.md#INFO-076) | Workspace Gemini 無料围い込み |
| [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) | AAIF/MCP 統合 |
| [INFO-033](../Information/2026-05-08/collected-raw.md#INFO-033) | Red Hat MCP Gateway |
| [INFO-064](../Information/2026-05-08/collected-raw.md#INFO-064) | Pentagon 7 社契約選出 |
| [INFO-066](../Information/2026-05-08/collected-raw.md#INFO-066) | 従業員 600+ 抗議 |
| [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) | DeepMind union 98% |
| [INFO-008](../Information/2026-05-06/collected-raw.md#INFO-008) | xAI Grok モデルが Google Cloud で提供開始、AI Overviews 購読出版物強調表示 |
| [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015) | Google Marketing Live 2026、MCP 全社サポート |
| [Arbiter v3.77](../state/arbiter-2026-05-14.md) | H-GOO-001/002/003 確度評価の完全根拠（本文から外出し） |
