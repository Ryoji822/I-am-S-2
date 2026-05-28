# Google / DeepMind

> 最終判断更新: 2026-05-28
> 全体確信度: 中
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。TPU 対 NVIDIA の電力効率が外部から測れない。Vertex AI から Gemini Enterprise Agent Platform への移行影響範囲が非公開
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-001](../config/indicators.json) [IND-006](../config/indicators.json) [IND-025](../config/indicators.json) [IND-027](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はGoogleを、**Gemini Enterprise Agent PlatformがVertex AIを正式に置き換え围い込みが20件に達した一方で、開放C証拠が20R連続で不在、H-GOO-002が32%に低下した企業**と読んでいる。最大の根拠は、Vertex AIからGemini Enterprise Agent Platformへの移行がエコシステム围い込みの構造的深化を示す事実 [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) と、GoogleがAnthropicへの$40B投資を検討しつつAnthropicが直接対決の70%で勝利している事実 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) だ。Gemini 3.5はAIME 73.3%・GPQA Diamond 74.2%を達成し [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039)、Gemini 3 Pro Deep Thinkはマルチモーダルベンチマーク100.0%で首位 [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016) だが、6R連続A-3/C-3のみのC蓄積でH-GOO-001は53%に低下した。Goldman Sachsは米国DC電力が31GWから66GWに倍増し$5.2T投資が必要と予測した [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044)。もし围い込みが規制当局の介入を引き起こすか、Anthropic直接対決勝率がGoogle有利に反転するなら、コア判断の前提が変わる。

## 1. コア判断

Googleの競争力の本体は、20億人規模の配布チャネルとTPUインフラとDeepMindの研究深度の三位一体にある。[H-GOO-003](../config/hypotheses.json)は49%で安定化が続いている。

Gemini Enterprise Agent PlatformがVertex AIを正式に置き換えた [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005)。これは围い込み18件目に該当し、Google CloudのAI開発プラットフォーム全体をGeminiブランドに統合する構造的変化だ。Managed Agents APIによるホステッド・サンドボックスランタイムとGemini Interactions APIによるエージェント開発パスの提供は、デベロッパーのGemini依存をインフラレベルで不可逆化する。

GoogleがAnthropicへの$40B投資を検討しているとの報道 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) は围い込み19件目に該当する。Anthropicが初回AI支出の直接対決で70%勝利し、収益の80%がエンタープライズである状況下で、Googleの投資は ecosystem dependency の形での围い込みと評価できる。Google Marketing LiveでのAI広告フォーマット発表 [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037) は围い込み20件目で、ChatGPT 9億MAUによる非中介化リスクへの対処として広告プラットフォームへのAI围い込みを拡張する。

围い込みは20件に達した。直近3件はGemini Enterprise Agent Platform [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005)、Anthropic $40B投資検討 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)、Marketing Live AI広告フォーマット [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037) で、共にI蓄積。開放C証拠は20R連続で不在である。H-GOO-002は32%に低下した。SKILL.md 40K+ と MCP 97M の開放標準爆発的進展 [INFO-014](../Information/2026-05-28/collected-raw.md#INFO-014) は開放側の動きだが、Google固有の開放Cとは評価できない。

Gemini 3.5がAIME 73.3%・GPQA Diamond 74.2%を達成した [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039)。Gemini 3 Pro Deep Thinkはマルチモーダルベンチマーク100.0%で首位 [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016)。これらはA-3品質の強力Cだが、4R条件（A-2+定量分解）は未達成であり、H-GOO-001の+1%復帰には至っていない。6R連続A-3/C-3のみのC蓄積は確度不変のアンカリングを示しており、Arbiter v3.91は-1%を裁定した。

Google Cloud Q1収益$8.41Bはアナリスト予想$8.64Bを下回ったが [INFO-057](../Information/2026-05-28/collected-raw.md#INFO-057)、YoY 63.4%成長・営業利益率32.9%（前年17.8%から改善）は強力な基調だ。Arbiterは予想下回りをノイズ範囲と評価し、-1%の根拠から除外した。「業界全体押し上げ」の代替説明は18R未解決で、Google固有要因を分離できない。

兵器誓約削除はA-2確認を維持している。DeepMind従業員が軍事AI懸念から労働組合結成を投票した [INFO-030](../Information/2026-05-28/collected-raw.md#INFO-030) は、経営層と従業員の対立リスクを示唆する。AnthropicのSCR指定 [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) とOpenAIのPentagon漁夫の利 [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) の文脈で、GoogleはPentagon受益者側に位置する。

DeepMind Co-ScientistのNature論文 [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) はH-GOO-003「研究卓越性から製品競争力」因果の最も具体的な証拠として継続して有効だ。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Gemini Enterprise Agent Platform: Vertex AIを正式に置き換え | 围い込み18件目。AI開発プラットフォーム全体のGeminiブランド統合。インフラレベルでの依存不可逆化 | C-3 | [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) |
| 高 | Google $40B Anthropic投資検討。Anthropic 70%直接対決勝利 | 围い込み19件目。ecosystem dependency形での围い込み。Google AI支出シェア約5%の現状を反映 | B-3 | [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) |
| 高 | Google Marketing Live: AI広告フォーマット発表・ChatGPT 9億MAU非中介化対処 | 围い込み20件目。広告プラットフォームへのAI围い込み拡張 | B-3 | [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037) |
| 高 | Gemini 3.5: AIME 73.3%・GPQA Diamond 74.2% | A-3品質強力Cだが4R条件未達成。フロンティア競争激化継続 | A-3 | [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039) |
| 高 | Gemini 3 Pro Deep Think: マルチモーダルベンチマーク100.0%首位 | 研究卓越性の定量指標。H-GOO-003のC蓄積 | C-3 | [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016) |
| 高 | DeepMind Co-Scientist: Nature論文・91%薬剤再利用・AlphaFold統合 | H-GOO-003「研究卓越性→製品競争力」因果の最も具体的証拠 | A-2 | [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) |
| 高 | 围い込み20件蓄積 + 開放C 20R連続不在 | H-GOO-002 32%。围い込み方向が一貫して強化。非対称性拡大継続 | A-3 | [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037) |
| 高 | Google/OpenAI兵器ルール後退(A-2) + Anthropic SCR指定 + Pentagon契約 | 安全性後退確定。因果チェーンA-2確認。GoogleはPentagon受益者側 | A-2 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) |
| 高 | Goldman Sachs: 米国DC電力31→66GW倍増・McKinsey $5.2T投資必要 | TPUインフラ外部展開の巨視的文脈確認。電力制約下での優位性指標 | A-3 | [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) |
| 高 | Cloud $8.41B/63.4% YoY・営業利益率32.9% | エコシステム収益が構造的に拡大。予想下回りはノイズ範囲(Arbiter評価) | B-3 | [INFO-057](../Information/2026-05-28/collected-raw.md#INFO-057) |
| 高 | SaaStr: Gemini +48%(27→40%)。Claude +128%(21→48%)。「業界全体押し上げ」18R未解決 | Google固有要因の分離不能。H-GOO-001 53%押し下げ要因継続 | B-3 | [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) |
| 高 | Google I/O 2026包括分析: 「全テック企業に宣戦布告」的围い込み(継続有効) | 围い込み17件目(前回)のI蓄積。エコシステム依存の包括的深化 | B-3 | [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) |
| 中 | Managed Agents API: Antigravity Agent + AGENTS.md/SKILL.md(継続有効) | 围い込み16件目。デベロッパーのGemini依存をコードレベルで構造化 | A-3 | [INFO-007](../Information/2026-05-23/collected-raw.md#INFO-007) |
| 中 | Gemini 3.1 Flash-Lite: エンタープライズプレビュー開始 | フロンティア性能の低コスト提供。围い込み価値を強化する一方で独自性を希薄化 | A-3 | [INFO-011](../Information/2026-05-28/collected-raw.md#INFO-011) |
| 中 | DeepMind従業員組合化投票(軍事AI取引) | 兵器ルール後退の文脈で経営層と従業員の対立激化リスク | C-3 | [INFO-030](../Information/2026-05-28/collected-raw.md#INFO-030) |
| 中 | Gemini Enterprise Agent Platform(前回围い込み14件目、継続有効) | build/deploy/govern/optimize一体化でエコシステム依存を構造的に深化 | A-3 | [INFO-010](../Information/2026-05-20/collected-raw.md#INFO-010) |
| 中 | Chrome DevTools for Agents v1: エージェント開発者向け(継続有効) | Googleブラウザ依存をエージェント開発に拡張する新ベクトル | A-3 | [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Workspace 内 Gemini の DAU/MAU または利用率が3四半期連続で頭打ちを示す | 「エコシステム統合優位」のコア判断と [H-GOO-001](../config/hypotheses.json) が崩れる | 180日 | [IND-006](../config/indicators.json) |
| 围い込み証拠が25件を超え、開放C証拠が引き続き不在のまま規制当局が介入する | [H-GOO-002](../config/hypotheses.json) が棄却水準に到達。围い込みリスクがコア判断の脅威に昇格。現在20件で接近中 | 120日 | [IND-027](../config/indicators.json) |
| 「業界全体押し上げ」代替説明を20R目でも解決できず、Gemini固有成長の証拠が出ない | H-GOO-001の更なる低下リスク。A-2+定量証拠取得が復帰の必須条件 | 30日 | [IND-006](../config/indicators.json) |
| DeepMind の研究成果が Gemini 製品に統合されない状態が4四半期続く | [H-GOO-003](../config/hypotheses.json) の「研究卓越性から製品競争力」因果が崩れる | 180日 | [IND-001](../config/indicators.json) |
| Anthropicが直接対決勝率70%を維持しGoogle AI支出シェアが5%に留まり続ける | Googleの$40B Anthropic投資が依存の承認になり、围い込みが自社プラットフォームではなく ecosystem dependency に反転 | 90日 | [IND-006](../config/indicators.json) |
| Vertex AI からの移行でエンタープライズ顧客の離反が発生する | Gemini Enterprise Agent Platform移行が围い込みでなく自滅になる可能性 | 90日 | [IND-006](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | Gemini統合でエコシステム収益を拡大する | 53% | Arbiter v3.91: -1%。6R連続A-3/C-3のみC蓄積の累積的重み。予想下回りはノイズ範囲として除外。代替説明18R未解決。A-2+定量証拠取得時+1%復帰条件 | [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039) [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016) [INFO-057](../Information/2026-05-28/collected-raw.md#INFO-057) [INFO-011](../Information/2026-05-28/collected-raw.md#INFO-011) | 代替説明18R未解決 [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025)。Anthropic 70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) |
| [H-GOO-002](../config/hypotheses.json) | 围い込み回避で開放維持 | 32% | 围い込み20件I蓄積(Vertex AI置き換え [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005)・$40B Anthropic投資 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)・Marketing Live [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037))。開放C証拠20R連続不在。low帯深化 | (開放C不在継続) | [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) |
| [H-GOO-003](../config/hypotheses.json) | DeepMind統合シナジーで競争力を維持する | 49% | Co-Scientist Nature論文91%有効性(A-2)は「研究→製品」因果の最強C [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053)。Gemini 3.5強力C(A-3)だが4R条件未達成。ペナルティ停止後安定化継続 | [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039) [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016) | [INFO-030](../Information/2026-05-28/collected-raw.md#INFO-030) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt 以上/期で high | Gemini 3.5 AIME 73.3%・GPQA 74.2% [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039)。Gemini 3 Pro Deep Think 100.0%首位 [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016)。Grok 4.1 97.8%2位。フロンティア競争激化継続 | 2026-05-28 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated 維持で継続監視 | Gemini Spark(個人エージェント)+Agent-to-UI+Enterprise Agent Platform(Vertex AI置き換え [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005))+Managed Agents API+Chrome DevTools for Agents | 2026-05-28 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated / stable | Gemini 3 Pro Deep Think 100.0% [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016)+Gemini 3.5 AIME 73.3% GPQA 74.2% [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039)。量的向上継続。「真の理解」検証未解決 | 2026-05-28 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | high / rising | SKILL.md 40K+ [INFO-014](../Information/2026-05-28/collected-raw.md#INFO-014)+MCP 97M+A2A GA [INFO-062](../Information/2026-05-28/collected-raw.md#INFO-062)。围い込み20件と開放の非対称性拡大継続 | 2026-05-28 |
| [IND-030](../config/indicators.json) | AI 能力とリスクの二面性 | high / rising | SCR指定 [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027)+DPA強要 [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029)+大統領令延期 [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025)+DeepMind組合化投票 [INFO-030](../Information/2026-05-28/collected-raw.md#INFO-030) | 2026-05-28 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-28 | Gemini Enterprise Agent Platform(Vertex AI置き換え)围い込み18件目+$40B Anthropic投資围い込み19件目+Marketing Live围い込み20件目+Gemini 3.5 AIME/GPQA+DC 66GW+$5.2T+DeepMind組合化を反映して全面書き直し | [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037) [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039) [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) | H-GOO-001 54→53%・H-GOO-002 33→32%・围い込み17→20件・開放C 20R連続不在・Vertex AI→Gemini Enterprise Agent Platform移行・Anthropic 70%直接対決勝利 |
| 2026-05-23 | Google I/O包括分析「全テック企業に宣戦布告」(围い込み17件目)+Managed Agents API(围い込み16件目)+Chrome DevTools for Agents v1+Goldman Sachs 66GW+Epoch AI 9x-900x価格下落+DeepSeek V4+Gemma 4 OSSを反映して全面書き直し | [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) [INFO-007](../Information/2026-05-23/collected-raw.md#INFO-007) [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) | H-GOO-001 53→54%・H-GOO-002 36→35%・围い込み15→17件・開放C 17R連続不在 |
| 2026-05-20 | Google I/O 2026結果(Gemini 3.5 Flash+Spark+Agent-to-UI)+Co-Scientist Nature論文+Blackstone $5B JV+兵器ルールA-2昇格を反映して全面書き直し | [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015) [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055) [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) | H-GOO-002 38→37%・围い込み14→15件・開放C 15R連続不在・兵器誓約B-3→A-2昇格 |
| 2026-05-19 | Google兵器誓約削除+Gemini Enterprise Agent Platform围い込み14件目+Googlebook围い込み+I/O 2026を反映して全面更新 | [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037) [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011) [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006) | H-GOO-002 39→38%・围い込み13→14件・開放C 14R連続不在 |

## 7. ブラインドスポット

- Gemini 3.5のAIME 73.3%とGPQA 74.2%がGoogleの自家測定であり、独立ベンチマークでの検証が未完了。Gemini 3 Pro Deep Think 100.0%もBenchLMの集計方法に依存する [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016)。
- Vertex AIからGemini Enterprise Agent Platformへの移行が既存エンタープライズ顧客に与える影響が不透明。移行コストと離反リスクの定量評価がない。
- Googleの$40B Anthropic投資検討 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) が実現した場合、GoogleのAI戦略が自社プラットフォーム強化ではなく ecosystem dependency に反転する可能性がある。围い込みと依存の区別が不明確になる。
- Co-Scientistの91%有効性はStanford単一施設での結果。他施設での再現性、商業スケールでの実用性が未検証。
- H-GOO-003の評価指標が依然として不十分。「エコシステム深度・研究卓越性・インフラ統合」の3軸それぞれについて独立評価する定量指標を持っていない。
- Workspace 内 Gemini の DAU/MAU が公開されていない。「Cloud 顧客の 75% が AI 製品を使用」は投入量であって利用深度ではない。
- 「業界全体押し上げ」代替説明が18R未解決。Google固有の成長要因をClaude +128%等の他社成長から分離する方法論を持っていない。
- 围い込み20件蓄積に対する規制当局(EU DMA/DOJ)の動向が外部から不透明。DOJのGoogle分割判断の行方が未確定。
- AGENTS.md/SKILL.md仕様が独自規格であり、MCP等のオープン標準との互換性が不明。围い込みと開放標準の同時進行の帰結が測れない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) | Gemini Enterprise Agent Platform: Vertex AI置き換え(C-3) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B Anthropic投資検討・Anthropic 70%直接対決勝利(B-3) |
| [INFO-037](../Information/2026-05-28/collected-raw.md#INFO-037) | Google Marketing Live AI広告フォーマット・ChatGPT非中介化リスク(B-3) |
| [INFO-039](../Information/2026-05-28/collected-raw.md#INFO-039) | Gemini 3.5 AIME 73.3%・GPQA Diamond 74.2%(A-3) |
| [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016) | Gemini 3 Pro Deep Think マルチモーダル100.0%首位(C-3) |
| [INFO-011](../Information/2026-05-28/collected-raw.md#INFO-011) | Gemini 3.1 Flash-Lite エンタープライズプレビュー(A-3) |
| [INFO-057](../Information/2026-05-28/collected-raw.md#INFO-057) | Google Cloud Q1 $8.41B/63.4% YoY・利益率32.9%(B-3) |
| [INFO-030](../Information/2026-05-28/collected-raw.md#INFO-030) | DeepMind従業員組合化投票(軍事AI)(C-3) |
| [INFO-044](../Information/2026-05-28/collected-raw.md#INFO-044) | Goldman Sachs: 米国DC電力31→66GW・$5.2T投資必要(A-3) |
| [INFO-014](../Information/2026-05-28/collected-raw.md#INFO-014) | SKILL.md 0→40K in 20週(C-3) |
| [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) | Google I/O包括分析: 「全テック企業に宣戦布告」的围い込み(B-3) |
| [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) | Google I/O 2026: 「Agentic Gemini Era」100件発表(A-3) |
| [INFO-007](../Information/2026-05-23/collected-raw.md#INFO-007) | Managed Agents API: Antigravity Agent + AGENTS.md/SKILL.md(A-3) |
| [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) | Chrome DevTools for Agents v1(A-3) |
| [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) | Epoch AI: トークン価格年9x-900x低下(B-3) |
| [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) | DeepMind Co-Scientist: Nature論文・91%薬剤再利用(A-2) |
| [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) | Google/OpenAI兵器ルール後退(A-2昇格)(A-2) |
| [INFO-010](../Information/2026-05-20/collected-raw.md#INFO-010) | Gemini Enterprise Agent Platform(包括的スタック)(A-3) |
| [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) | SaaStr: Gemini +48%(27→40%) vs Claude +128%(21→48%)(B-3) |
| [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027) | Cloud $20.03B/63% YoY・GenAI 800%・バックログ $462B(A-2) |
| [Arbiter v3.91](../state/arbiter-2026-05-28.md) | 確度評価の完全根拠 |
