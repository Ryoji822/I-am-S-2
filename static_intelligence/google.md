# Google / DeepMind

> 最終判断更新: 2026-05-11
> 全体確信度: 中
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。TPU 対 NVIDIA の電力効率が外部から測れない
> 主参照: hypotheses.json#H-GOO-001/002/003, indicators.json#IND-001/006/025/027/030

## 0. 一文要約

我々はGoogleを、**エコシステム深度とTPU自前インフラとDeepMind研究卓越性の三位一体で戦う企業**と読んでいる。最大の根拠は Cloud $20.03B/63% YoY と $462B バックログが示す収益の構造性 [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) と、AlphaEvolveによるアルゴリズム発見能力 [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098) が示す研究卓越性だ。H-GOO-003 を「フロンティア性能競争」から「DeepMind統合シナジー」に修正した。10R以上「性能競争」枠組みで測り続けた誤りは認識済みである。もし Workspace 内 Gemini 利用率が3四半期連続で頭打ちになるか、TPU インフラを外部も使えるようになるなら、エコシステム優位の読み自体が崩れる。

## 1. コア判断

Google の競争力の本体は、ベンチマークスコアではなく20億人規模の配布チャネルとTPUインフラとDeepMindの研究深度の三位一体にある。この読みに到達するまでに10R以上を要した。H-GOO-003 を「フロンティア性能競争で対抗」という枠組みで測り続けた結果、確度は55%から49%へ下がり続けた。低下の原因は枠組みそのものがGoogleの強みを系統的に見落としていたことにある。今回、命題を「DeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する」に修正した。

Cloud 側の数値は構造性を示している。$20.03B/63% YoY、GenAI 製品 800% YoY、バックログ $462B [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027)。Cloud 顧客の 75% が AI 製品を使い [INFO-005](../Information/2026-05-08/collected-raw.md#INFO-005)、330 社が年間 1T 超のトークンを処理している [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)。これは投入指標であり利用深度ではないが、切り替えコストが上昇している間接証拠としては機能する。Gemini Enterprise Agent Platform は構築・スケール・ガバナンスを一体化したプラットフォームに進化し [INFO-019](../Information/2026-05-08/collected-raw.md#INFO-019)、エコシステムの厚みが増している。

研究側では新たな証拠が加わった。AlphaEvolve はアルゴリズム発見エージェントとして機能し [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098)、DeepMind Co-Clinician は GPT-5.4 の 30% に対して 63% の正確性を記録した [INFO-078](../Information/2026-05-08/collected-raw.md#INFO-078)。BenchLM Gemini 3 Pro Deep Think は 100% 首位を獲得し [INFO-040](../Information/2026-05-08/collected-raw.md#INFO-040)、専門領域での研究卓越性が数値として現れている。ただし Hermes が GPQA Diamond 94.1% で第三者推理首位を取っており [INFO-054](../Information/2026-05-08/collected-raw.md#INFO-054)、GPT-5.5 が Terminal-Bench 82.7% を記録している [INFO-041](../Information/2026-05-08/collected-raw.md#INFO-041) ことから、競合の圧力は継続している。BenchLM 総合では Gemini 3.1 Pro 93 に対して Claude Mythos Preview 99 に 6pt 差をつけられている [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。

20 億人規模の検索・Workspace・Android・Chrome ユーザーを配布チャネルにできる企業にとって、性能での数 pt 差は顧客離脱に直結しない。ただし Workspace Gemini 無料围い込み [INFO-076](../Information/2026-05-08/collected-raw.md#INFO-076) は H-GOO-002 にとって19R+で初の I 証拠となった。AAIF/MCP 統合 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) と Red Hat MCP Gateway [INFO-033](../Information/2026-05-08/collected-raw.md#INFO-033) は開放標準への取り組みを示しているが、围い込みと開放の二重構造が継続している。Pentagon 7 社契約で選出された一方で [INFO-064](../Information/2026-05-08/collected-raw.md#INFO-064) 従業員 600+ が抗議している [INFO-066](../Information/2026-05-08/collected-raw.md#INFO-066) ことも、政府市場での実行リスクとして監視が必要である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Cloud $20.03B/63% YoY、GenAI 800% YoY、バックログ $462B | エコシステム収益が構造的に拡大していることの直接証拠 | A-2 | [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) |
| 高 | Cloud 顧客 75% が AI 製品利用、330 社が年間 1T+ トークン処理 | 顧客がエコシステムに深く埋め込まれている。切り替えコストが上昇中 | A-2 | [INFO-005](../Information/2026-05-08/collected-raw.md#INFO-005) [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) |
| 高 | AlphaEvolve アルゴリズム発見エージェント稼働 | DeepMind の研究卓越性が製品化された証拠。H-GOO-003 新命題を直接支持 | A-3 | [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098) |
| 高 | Gemini Enterprise Agent Platform 正式リリース | Google がプラットフォーム側に回りつつある。モデル単体ではなく基盤を売る構造への転換 | A-2 | [INFO-019](../Information/2026-05-08/collected-raw.md#INFO-019) |
| 中 | BenchLM 総合 93（Claude Mythos 99、GPT-5.4 Pro 92）。BenchLM Gemini 3 Pro Deep Think 100% 首位 | 総合では劣後だが専門領域で首位。エコシステム優位を崩す証拠にはなっていない | A-2 | [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) [INFO-040](../Information/2026-05-08/collected-raw.md#INFO-040) |
| 中 | Workspace Gemini 無料围い込み、Pentagon 7 社契約選出 + 従業員 600+ 抗議 | 围い込みは H-GOO-002 の初 I 証拠。Pentagon 契約は政府市場参入の機会だが内部摩擦が同時進行 | B-2 | [INFO-076](../Information/2026-05-08/collected-raw.md#INFO-076) [INFO-064](../Information/2026-05-08/collected-raw.md#INFO-064) [INFO-066](../Information/2026-05-08/collected-raw.md#INFO-066) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Workspace 内 Gemini の DAU/MAU または利用率が3四半期連続で頭打ちを示す公式開示 | 「エコシステム統合優位」のコア判断と [H-GOO-001](../config/hypotheses.json) が崩れる | 180日 | [IND-006](../config/indicators.json) |
| OpenAI / Anthropic が自前 TPU 相当のインフラを持つか、TPU を外部調達できるようになる | 「TPU 自前インフラの差別化」が崩れ、[H-GOO-002](../config/hypotheses.json) の再評価が必要 | 90日 | [IND-001](../config/indicators.json) |
| エンタープライズLLMシェアで Google が 21% から低下し続け、Anthropic や OpenAI との差が拡大する | エコシステム優位が収益に転換できていないことになり、コア判断全体が疑われる | 90日 | [IND-006](../config/indicators.json) |
| 従業員抗議が拡大し Pentagon 契約の実行停止または大幅縮小に至る | 政府市場参入の機会損失が確定し、[H-GOO-002](../config/hypotheses.json) の政府向け収益根拠が崩れる | 60日 | [IND-030](../config/indicators.json) |
| DeepMind の研究成果が Gemini 製品に統合されない状態が4四半期続く | [H-GOO-003](../config/hypotheses.json) の「研究卓越性→製品競争力」因果が崩れる | 180日 | [IND-001](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | Gemini 統合でエコシステム収益を拡大する | 54% | Cloud $20B/63% YoY と Gemini Enterprise Agent Platform [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) が支持。ただし800%収益成長基数不明が5R連続未解決→6R目。エンタープライズLLMシェアが Anthropic 40% に劣後しており、投入指標と成果指標の乖離が残る。業界全体押し上げ効果のGoogle固有証拠誤認リスク | [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) [INFO-005](../Information/2026-05-08/collected-raw.md#INFO-005) | エンタープライズLLMシェアの継続低下 |
| [H-GOO-002](../config/hypotheses.json) | 围い込み回避で開放維持 | 45% | AAIF/MCP統合 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) と Red Hat MCP Gateway [INFO-033](../Information/2026-05-08/collected-raw.md#INFO-033) が開放を支持。围い込み4件目I蓄積(Workspace無料围い込み+围い込み宣言+Gemini Enterprise統合+Vertex移行)。開放C証拠完全不在。次ラウンド围い込み5件目I蓄積で追加-1%検討条件。low帯 | [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) [INFO-033](../Information/2026-05-08/collected-raw.md#INFO-033) | [INFO-076](../Information/2026-05-08/collected-raw.md#INFO-076) Workspace 围い込み |
| [H-GOO-003](../config/hypotheses.json) | DeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% | 仮説修正実行済み(v3.71)。AlphaEvolve [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) は研究卓越性C。BenchLM Gemini 3 Pro Deep Think 100% [INFO-040](../Information/2026-05-08/collected-raw.md#INFO-040) は性能C。DeepMind union 98% [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) は内部摩擦I。48%はlow帯。ペナルティ停止後安定化継続 | [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-040](../Information/2026-05-08/collected-raw.md#INFO-040) | [INFO-054](../Information/2026-05-08/collected-raw.md#INFO-054) [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt 以上/期で high | BenchLM 93 (3位)、MMMU-Pro 88.21% 首位、ARC-AGI-2 77.1%、BenchLM Gemini 3 Pro Deep Think 100% [INFO-040](../Information/2026-05-08/collected-raw.md#INFO-040) | 2026-05-08 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated 維持で継続監視 | Gemini Enterprise Agent Platform [INFO-019](../Information/2026-05-08/collected-raw.md#INFO-019)。AAIF/MCP 統合 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) | 2026-05-08 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Sonnet 4.6 OSWorld大幅改善 [INFO-001](../Information/2026-05-11/collected-raw.md#INFO-001)。Doubao-Seed-2.0-lite フルマルチモーダル。Grok 4.3 ネイティブ動画 [INFO-020](../Information/2026-05-11/collected-raw.md#INFO-020)。量的向上継続。「真の理解」検証未解決 | 2026-05-11 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | high / rising | Azure排他性終了+OpenAI SDK provider-agnostic+157K OpenCode移行。標準化加速。Gemini Enterprise围い込み同時進行 | 2026-05-11 |
| [IND-030](../config/indicators.json) | AI 能力とリスクの二面性 | elevated / rising | Pentagon 7社契約選出+DeepMind union 98% [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026)+EU Act延期+中国裁判所+Sanders法案。規制二方向同時進行深化 | 2026-05-11 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-08 | [H-GOO-003](../config/hypotheses.json) 仮説修正実行。命題を「フロンティア性能競争」から「DeepMind統合シナジー（エコシステム深度・研究卓越性・インフラ統合）」に変更 | AlphaEvolve [INFO-096](../Information/2026-05-08/collected-raw.md#INFO-096) [INFO-097](../Information/2026-05-08/collected-raw.md#INFO-097) [INFO-098](../Information/2026-05-08/collected-raw.md#INFO-098) + BenchLM Gemini 3 Pro首位 [INFO-040](../Information/2026-05-08/collected-raw.md#INFO-040) + Hermes 94.1% [INFO-054](../Information/2026-05-08/collected-raw.md#INFO-054) | 「性能競争で対抗する企業（仮説修正中）」→「エコシステム深度と研究卓越性で競争力を維持する企業」 |
| 2026-05-08 | AlphaEvolve、DeepMind Co-Clinician、Workspace Gemini 無料围い込み、Pentagon 7社契約選出 + 従業員抗議を反映して全面更新 | H-GOO-003 修正実行 + 新規証拠 | H-GOO-003 49%→48%（low）、H-GOO-002 48%（low） |
| 2026-05-06 | H-GOO-003 仮説修正命令発出。コア判断を「性能競争への枠組み」から「エコシステム統合優位」へ修正開始 | BenchLM 3位 (93 vs Mythos 99) と10R連続確度低下 [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) | 「性能競争で対抗できる企業」→「エコシステム統合とTPUで戦う企業（性能枠組みの修正中）」 |
| 2026-05-06 | Cloud $20B/63% YoY、GenAI 800%成長、Gemini Enterprise Agent Platform、xAI Grok on Google Cloud、Agent Skills、Pentagon 契約 + 従業員抗議を反映して全面更新 | 鮮度タイムアウト (7日経過) | H-GOO-001 56%、H-GOO-002 48%、H-GOO-003 49% に更新 |
| 2026-04-29 | Gemini Enterprise Agent Platform 詳細・Anthropic $40B 投資を反映 | Cloud Next 2026 後続情報 | 基本情報・戦略方向性を全面書き直し |
| 2026-04-22 | Cloud Next 2026 定量データを初反映 | Pentagon 契約交渉、$240B バックログ | 「Cloud は AWS に大差で劣後」→「急拡大フェーズ」へ読み変え |

## 7. ブラインドスポット

- **H-GOO-003 の修正は完了したが、新命題を評価する指標がまだ不十分である**。「エコシステム深度・研究卓越性・インフラ統合」の3軸それぞれについて、確度を独立に評価する定量指標を持っていない。AlphaEvolve や Co-Clinician は個別の C 証拠だが、これらを体系化する指標設計が未完了である。
- **Workspace 内 Gemini の DAU/MAU が公開されていない**。「Cloud 顧客の 75% が AI 製品を使用」という数値は投入量であって利用深度ではない。利用が浅い 75% と深い 30% では意味が全く異なるが、外から区別できない。
- **TPU 対 NVIDIA H200 の電力効率比較が外部から測れない**。Google が TPU 優位を主張しているが、独立した検証がない。インフラ優位の主張の強度が評価できない。
- **DeepMind の研究成果が Gemini 製品にどの程度・どの速度で統合されているかが外部から不透明である**。AlphaEvolve は研究卓越性を示すが、これが Gemini の製品競争力にどう反映されるかの因果が未確認である。
- **Anthropic $40B 投資の戦略的含意が外部から不透明**。Gemini 普及を目指す企業が最大の競合モデルに巨額投資する構造は矛盾に見える。議決権なし出資という整理はあるが、この投資が Gemini 採用を遅らせるインセンティブとして内部で機能していないかが見えない。

## 付録: 直近30日の参照 Evidence

| Evidence | 用途 |
|---|---|
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
| [INFO-008](../Information/2026-05-06/collected-raw.md#INFO-008) | xAI Grok モデルが Google Cloud で提供開始、AI Overviews 購読出版物強調表示 |
| [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015) | Google Marketing Live 2026、MCP 全社サポート |
| [Arbiter v3.71](../state/arbiter-2026-05-08.md) | H-GOO-001/002/003 確度評価の完全根拠（本文から外出し） |
