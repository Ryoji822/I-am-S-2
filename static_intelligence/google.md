# Google / DeepMind

> 最終判断更新: 2026-06-06
> 全体確信度: 中
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。TPU 対 NVIDIA の電力効率が外部から測れない。Vertex AI から Gemini Enterprise Agent Platform への移行影響範囲が非公開。围い込みI 32件の品質別内訳未開示（次回必須条件化済み）。Cloud Next垂直統合のOpenAI/Anthropicへの実際の影響が外部から測れない
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-001](../config/indicators.json) [IND-006](../config/indicators.json) [IND-025](../config/indicators.json) [IND-027](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はGoogleを、**围い込みが32件に達しH-GOO-002が23%に低下した一方で、開放C証拠が30R連続不在から2件出現で解除され、围い込みの次元がエコシステムからハードウェア・決済・SaaSに拡大する企業**と読んでいる。最大の根拠は、Capex $180-190B围い込み [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) とGooglebook围い込み [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) とWorkday SaaS围い込み [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048) による围い込みI 3件追加蓄積と、Gemini Agent API MCP Server統合 [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) とagents-cli クロスエージェント [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) による開放C 30R不在解除の同時発生だ。Red指摘の件数インフレリスク（Capex围い込みは業界全体Capex増加中での独立性疑問、Googlebook围い込みはApple・Microsoftの垂直統合と同質、Workday統合はパートナーシップで排他性未確認）を記録する。もし围い込みが規制当局の介入を引き起こすか、開放C 2件が質的転換の開始を示すか、のいずれかが観測されたら、コア判断の前提が変わる。

## 1. コア判断

Googleの競争力の本体は、20億人規模の配布チャネルとTPUインフラとDeepMindの研究深度の三位一体にある。[H-GOO-003](../config/hypotheses.json)は49%で安定化が続いている。

围い込みは32件に達した。直近の蓄積はCapex围い込み（INFO-010、I/O 2026でCapex $180-190BとGoogle固有インフラ围い込みを宣言）+Googlebook围い込み（INFO-011、Gemini搭載ラップトップでハードウェア次元に拡大）+Workday SaaS围い込み（INFO-048、HR/財務ワークフローにAIエージェントを直接埋め込む）で围い込みI 3件が同時に蓄積された。围い込みの次元がエコシステム・データ・インフラに加え、ハードウェア・決済・SaaSに拡大している。Red指摘の件数インフレリスク（同一イベント内複数機能別カウント、Capex围い込みは業界全体Capex増加中での独立性疑問、Googlebook围い込みはApple・Microsoftの垂直統合と同質、Workday統合はパートナーシップで排他性未確認）は妥当であり、围い込みI 32件品質別内訳の開示を次回必須条件化した。H-GOO-002は23%に低下しlow帯深化が続く。

開放C証拠が30R連続不在から解除された。Gemini Agent APIがMCP Server統合を提供し [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016)（A-2品質）、agents-cliがClaude Code・Codex・Antigravityを含むクロスエージェント設計でv0.3.0をリリースした [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023)（A-3品質）。30R不在後の開放C同時出現は偶然ではなく意図的戦略転換の可能性がある。ただし围い込みIの蓄積速度が開放Cを上回る評価は妥当であり、-1%は保守的である。

Gemini Enterprise Agent PlatformがVertex AIを正式に置き換えた [INFO-018](../Information/2026-06-06/collected-raw.md#INFO-018)。Agent Search APIに正式SLAが設定された。これは围い込みの制度化が進行していることを示す。

[H-GOO-001](../config/hypotheses.json)は51%±0%。I=0が14R連続で延長した。代替説明「業界全体押し上げ」が14R未解決で、Google固有要因を分離できない状態が継続している。

HassabisがAGI 2029到達を示唆した [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044)（A-1品質）はH-GOO-003の時間軸に関するCだが、AGI定義の曖昧さから確度への寄与は限定的だ。Capex $180-190B [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) は2022年$31Bから6倍の増加であり、インフラ投資の構造的拡大を示す。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Capex $180-190B围い込み: I/O 2026でGoogle固有インフラ围い込みを宣言 | 围い込み25件目（Capex围い込み）。インフラ投資の構造的拡大。Red指摘: 業界全体Capex増加中での独立性疑問 | A-3 | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) |
| 高 | Googlebook围い込み: Gemini搭載ラップトップ（Acer/Asus/Dell/HP/Lenovo） | 围い込み26件目（ハードウェア次元）。围い込み次元がエコシステムからハードウェアに拡大。Red指摘: Apple・Microsoftの垂直統合と同質 | A-3 | [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) |
| 高 | Workday SaaS围い込み: HR/財務ワークフローにAIエージェント直接埋め込み | 围い込み27件目（SaaS次元）。围い込み次元がSaaSに拡大。Red指摘: パートナーシップで排他性未確認 | B-2 | [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048) |
| 高 | Gemini Agent API MCP Server統合: Deep Research Agent + MCP対応 | 開放C出現（30R不在解除）。Google APIがMCP標準に対応。意図的戦略転換の可能性 | A-2 | [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) |
| 高 | agents-cli クロスエージェント: Claude Code/Codex/Antigravity対応（2.7k Stars） | 開放C出現（30R不在解除）。Googleツールが他社エージェントをサポート | A-3 | [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) |
| 高 | 围い込み32件蓄積 + 開放C 2件出現（30R解除） | H-GOO-002 23%。围い込み方向が一貫して強化しつつ開放C初出現。非対称性は継続。low帯深化 | A-3 | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048) [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) |
| 高 | Gemini Enterprise Agent Platform: Vertex AI正式置き換え・Agent Search API SLA設定 | 围い込みの制度化進行。正式SLA設定で信頼性の商業的裏付け | A-3 | [INFO-018](../Information/2026-06-06/collected-raw.md#INFO-018) |
| 高 | Gemini Omni: 任意入力→動画生成 + 3.5 Flash 9デモ | 製品能力の拡張。新モダリティ対応 | A-3 | [INFO-012](../Information/2026-06-06/collected-raw.md#INFO-012) |
| 高 | Google Cloud製造業AIエージェントトレンド: 93%がデジタル/AI支出増計画・「AI成熟」は2%のみ | H-GOO-001のC。採用意欲と成熟度のギャップ確認。Google Cloud経由のエコシステム围い込みと整合 | A-2 | [INFO-052](../Information/2026-06-06/collected-raw.md#INFO-052) |
| 高 | Hassabis AGI 2029到達示唆 | H-GOO-003の時間軸C。AGI定義の曖昧さから確度寄与は限定的 | A-1 | [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) |
| 中 | 围い込み24件目（前回蓄積分、継続有効） | Cloud Next垂直統合 + Enterprise Agent Platform + Vertex AI移行 | C-3 | [INFO-067](../Information/2026-06-01/collected-raw.md#INFO-067) [INFO-019](../Information/2026-06-01/collected-raw.md#INFO-019) [INFO-027](../Information/2026-06-01/collected-raw.md#INFO-027) |
| 中 | agents-cli OSS（前回評価、継続有効） | 開放C候補。CLIツールOSS化は围い込み回避の十分条件ではない(Apple model) | A-3 | [INFO-024](../Information/2026-06-01/collected-raw.md#INFO-024) |
| 中 | SaaStr: Gemini +48%（27→40%）。Claude +128%。「業界全体押し上げ」14R未解決 | Google固有要因の分離不能。H-GOO-001 51%押し下げ要因継続 | B-3 | [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Workspace 内 Gemini の DAU/MAU または利用率が3四半期連続で頭打ちを示す | 「エコシステム統合優位」のコア判断と [H-GOO-001](../config/hypotheses.json) が崩れる | 180日 | [IND-006](../config/indicators.json) |
| 围い込み証拠が35件を超え、規制当局が介入する | [H-GOO-002](../config/hypotheses.json) が棄却水準に到達。围い込みリスクがコア判断の脅威に昇格。現在32件で接近中 | 120日 | [IND-027](../config/indicators.json) |
| 「業界全体押し上げ」代替説明を20R目でも解決できず、Gemini固有成長の証拠が出ない | H-GOO-001の更なる低下リスク。現在14R未解決 | 30日 | [IND-006](../config/indicators.json) |
| 開放C証拠が5件以上に拡大し、围い込み蓄積速度を上回る | H-GOO-002の上方修正根拠。30R不在解除が質的転換の開始を示す。現在2件 | 60日 | [IND-027](../config/indicators.json) |
| DeepMind の研究成果が Gemini 製品に統合されない状態が4四半期続く | [H-GOO-003](../config/hypotheses.json) の「研究卓越性から製品競争力」因果が崩れる | 180日 | [IND-001](../config/indicators.json) |
| Vertex AI からの移行でエンタープライズ顧客の離反が発生する | Gemini Enterprise Agent Platform移行が围い込みでなく自滅になる可能性 | 90日 | [IND-006](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | Gemini統合でエコシステム収益を拡大する | 51% | Arbiter v3.99: -1%（52→51%）。I=0が14R連続延長。代替説明14R未解決。A-2+条件12R未達成。Capex $180-190Bは規模Cだが業界全体Capex増加中でのGoogle固有性未確認。製造業93%支出増 [INFO-052](../Information/2026-06-06/collected-raw.md#INFO-052) は方向C | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) [INFO-018](../Information/2026-06-06/collected-raw.md#INFO-018) [INFO-052](../Information/2026-06-06/collected-raw.md#INFO-052) | 代替説明14R未解決 [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025)。Anthropic 70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) |
| [H-GOO-002](../config/hypotheses.json) | 围い込み回避で開放維持 | 23% | Arbiter v4.00: -1%（24→23%）。围い込みI 32件蓄積（+3件: Capex围い込み [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010)・Googlebook围い込み [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011)・Workday SaaS围い込み [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048)）。開放C 2件出現（INFO-016 MCP Server・INFO-023 agents-cli）で30R不在解除。Red指摘件数インフレリスク記録（Capex独立性疑問・Googlebookは標準垂直統合・Workdayは排他性未確認）。品質別内訳次回必須開示。low帯深化 | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048) | [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) |
| [H-GOO-003](../config/hypotheses.json) | DeepMind統合シナジーで競争力を維持する | 49% | Arbiter v3.99: ±0%（50→49%）。11R連続A-2+条件未達成。49%到達。medium維持。次回49%以下継続でlow移行検討。Co-Scientist Nature論文91%有効性(A-2)は「研究→製品」因果の最強C [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053)。Hassabis AGI 2029 [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044)。Capex $180-190B [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | [INFO-030](../Information/2026-05-28/collected-raw.md#INFO-030) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt 以上/期で high | Gemini 3.5 AIME 73.3%・GPQA 74.2%。Gemini 3 Pro Deep Think 100.0%首位。GPT-5.4・NVIDIA Nemotron追従。フロンティア競争激化継続 | 2026-06-06 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated 維持で継続監視 | Gemini Agent API MCP Server [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) + agents-cli クロスエージェント [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) + Gemini Enterprise Agent Platform SLA [INFO-018](../Information/2026-06-06/collected-raw.md#INFO-018) + Capex $180-190B [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | 2026-06-06 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated / stable | Gemini Omni任意入力→動画生成 [INFO-012](../Information/2026-06-06/collected-raw.md#INFO-012) + GPT-5.4 + Nemotron 3 Ultra。量的向上継続。「真の理解」検証未解決 | 2026-06-06 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | high / rising | MCP 97M DL [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) + Gemini Agent API MCP対応 [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) + agents-cli クロスエージェント [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023)。围い込み32件と開放C 2件の非対称性は継続 | 2026-06-06 |
| [IND-030](../config/indicators.json) | AI 能力とリスクの二面性 | high / rising | SCR指定 [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028) + DPA脅迫 [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030) + 大統領令自発的枠組み [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032) + Capex围い込み [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010)。5日間5イベント蓄積 | 2026-06-06 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-06 | H-GOO-002 -1%（24→23%）围い込みI 32件蓄積+開放C 30R解除+围い込み次元拡大（ハードウェア・SaaS）+H-GOO-001 ±0%（51%）I=0 14R連続+H-GOO-003 ±0%（49%）を反映して全面書き直し | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048) [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) [INFO-018](../Information/2026-06-06/collected-raw.md#INFO-018) [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) | H-GOO-001 52→51%（-1%）・H-GOO-002 24→23%（-1%）・H-GOO-003 49%（±0%）・围い込み24→32件（+8件）・開放C 30R不在→2件出現で解除・围い込み次元: エコシステム→ハードウェア・決済・SaaSに拡大 |
| 2026-06-01 | Cloud Next垂直統合+Enterprise Agent Platform+Vertex AI移行围い込み24件目+agents-cli OSS開放C評価+Google Cloud $20Bを反映して全面書き直し | [INFO-067](../Information/2026-06-01/collected-raw.md#INFO-067) [INFO-019](../Information/2026-06-01/collected-raw.md#INFO-019) [INFO-027](../Information/2026-06-01/collected-raw.md#INFO-027) [INFO-024](../Information/2026-06-01/collected-raw.md#INFO-024) [INFO-072](../Information/2026-06-01/collected-raw.md#INFO-072) | H-GOO-001 52%(±0%)・H-GOO-002 29→28%(-1%)・H-GOO-003 49%(±0%)・围い込み23→24件・開放C 23→24R連続不在・围い込みI 9件目蓄積 |
| 2026-05-28 | Gemini Enterprise Agent Platform(Vertex AI置き換え)围い込み18件目+$40B Anthropic投資围い込み19件目+Marketing Live围い込み20件目+Gemini 3.5 AIME/GPQA+DC 66GW+$5.2T+DeepMind組合化を反映して全面書き直し | [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037) [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039) [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) | H-GOO-001 54→53%・H-GOO-002 33→32%・围い込み17→20件・開放C 20R連続不在・Vertex AI→Gemini Enterprise Agent Platform移行・Anthropic 70%直接対決勝利 |

## 7. ブラインドスポット

- 围い込みI 32件の品質別内訳が未開示。A-1/A-2品質の独立性「高」件数がいくつあるか不明。Red指摘の件数インフレリスク（同一イベント内複数機能別カウント、ブランド変更の独立性、垂直統合の围い込み分類妥当性）は妥当。次回必須開示条件化済み。
- 開放C 2件出現の質的転換可能性が未評価。Gemini Agent API MCP対応とagents-cli クロスエージェントがGoogleの二層戦略（基盤開放・上位围い込み）の一部なのか、围い込み方向の転換なのかの判別が不能。
- Gemini 3.5のAIME 73.3%とGPQA 74.2%がGoogleの自家測定であり、独立ベンチマークでの検証が未完了。Gemini 3 Pro Deep Think 100.0%もBenchLMの集計方法に依存する [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016)。
- Vertex AIからGemini Enterprise Agent Platformへの移行が既存エンタープライズ顧客に与える影響が不透明。移行コストと離反リスクの定量評価がない。
- Googleの$40B Anthropic投資検討 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) が実現した場合、GoogleのAI戦略が自社プラットフォーム強化ではなく ecosystem dependency に反転する可能性がある。
- Co-Scientistの91%有効性はStanford単一施設での結果。他施設での再現性、商業スケールでの実用性が未検証。
- H-GOO-003の評価指標が依然として不十分。「エコシステム深度・研究卓越性・インフラ統合」の3軸それぞれについて独立評価する定量指標を持っていない。49%到達で次回low移行検討。
- Workspace 内 Gemini の DAU/MAU が公開されていない。「Cloud 顧客の 75% が AI 製品を使用」は投入量であって利用深度ではない。
- 「業界全体押し上げ」代替説明が14R未解決。Google固有の成長要因をClaude +128%等の他社成長から分離する方法論を持っていない。
- 围い込み32件蓄積に対する規制当局(EU DMA/DOJ)の動向が外部から不透明。DOJのGoogle分割判断の行方が未確定。
- AGENTS.md/SKILL.md仕様が独自規格であり、MCP等のオープン標準との互換性が不明。围い込みと開放標準の同時進行の帰結が測れない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | Google I/O 2026: Capex $180-190B围い込み・TPU 8t・3.2Q tokens/月(A-3) |
| [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) | Googlebook: Gemini搭載ラップトップ围い込み(A-3) |
| [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) | Gemini Agent API MCP Server統合・Deep Research Agent・開放C出現(A-2) |
| [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) | agents-cli クロスエージェント: Claude Code/Codex/Antigravity対応・開放C出現(A-3) |
| [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048) | Workday × Google Cloud: HR/財務AIエージェント围い込み(B-2) |
| [INFO-018](../Information/2026-06-06/collected-raw.md#INFO-018) | Vertex AI → Gemini Enterprise Agent Platform改名・SLA設定(A-3) |
| [INFO-012](../Information/2026-06-06/collected-raw.md#INFO-012) | Gemini Omni + 3.5 Flash 9デモ(A-3) |
| [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) | Hassabis AGI 2029到達示唆(A-1) |
| [INFO-052](../Information/2026-06-06/collected-raw.md#INFO-052) | Google Cloud製造業AIエージェントトレンド: 93%支出増・2%成熟(A-2) |
| [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) | AAIF: MCP 97M DL・A2A 150組織・43新メンバー(A-2) |
| [INFO-067](../Information/2026-06-01/collected-raw.md#INFO-067) | Google Cloud Next 2026: AI Agentフルスタック垂直統合(C-3) |
| [INFO-019](../Information/2026-06-01/collected-raw.md#INFO-019) | Gemini Enterprise Agent Platform公式ドキュメント公開(A-3) |
| [INFO-027](../Information/2026-06-01/collected-raw.md#INFO-027) | Vertex AI移行: Gemini Enterprise Agent Platformへ再構築(C-3) |
| [INFO-024](../Information/2026-06-01/collected-raw.md#INFO-024) | agents-cli OSS: Gemini Agent Platform向けCLI・スキル(A-3) |
| [INFO-072](../Information/2026-06-01/collected-raw.md#INFO-072) | Google Cloud収益Q1 2026: $20B/四半期・63.4% YoY(B-3) |
| [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) | DeepMind Co-Scientist: Nature論文・91%薬剤再利用(A-2) |
| [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) | SaaStr: Gemini +48%(27→40%) vs Claude +128%(B-3) |
| [Arbiter v4.00](../state/arbiter-2026-06-06.md) | 確度評価の完全根拠 |
| [Arbiter v3.99](../state/arbiter-2026-06-05.md) | 確度評価の完全根拠（付録のみ参照） |
