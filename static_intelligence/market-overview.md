# AI市場全体 — 静的インテリジェンス

> 最終判断更新: 2026-05-21
> 全体確信度: 中
> 情報非対称性: ByteDance / DeepSeek のグローバルシェア追跡が困難。2nd tier (Mistral / Cohere) の動向が5社比較に入っていない。QHG Y軸再定義がArbiter v3.84で採用され、v3.84以降の確率体系はv3.83以前と非整合のため推移比較に注意
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-001](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-21時点)

| 企業 | 主力モデル / 製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.6, Sonnet 4.6, Mythos, Claude Code | $900B+評価額(A-2) | 3位 (94) | WSJ: OpenAI逆転 [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032)。PwC数十万人展開 [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002)。SMB参入。4倍シェア成長 [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047)。Karpathy入社 |
| OpenAI | GPT-5.5, Codex (4M WAU), DeployCo | $852B評価額 | 4位 (92) | 兵器ルール後退(A-2) [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046)。Dell提携 [INFO-001](../Information/2026-05-20/collected-raw.md#INFO-001)。IPO $852B。Microsoft離反検討(Reuters) |
| Google | Gemini 3.5 Flash, Spark, Enterprise Agent Platform, Co-Scientist | Cloud $20B/63% YoY, Blackstone $5B JV | 1位 (98) | I/O 2026: 3.5 Flash 4x高速 [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015)。Co-Scientist Nature論文91% [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053)。兵器誓約削除(A-2) [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046)。围い込み15件 |
| SpaceXAI | Grok 4.3, Grok Build CLI, Voice Agent API | SpaceX $250BがxAI買収 | 2位 (95) | Grok Build ACP対応。強制採用戦略。市場採用データ不在 |
| ByteDance | 豆包2.0, Coze 2.5, DeerFlow 2.0 | CAPEX $28B | 非公開 | DeerFlow 2.0 Docker of AI Workers。Seedance 2.0産業再構築。豆包有料化 |

---

## 0. 一文要約

Anthropicの評価額が$900Bに達しOpenAIを逆転した [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032)。Google I/OでGemini 3.5 Flashがリリースされ [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015)、DeepMind Co-ScientistがNature論文で薬剤再利用91%を達成した [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053)。GoogleとOpenAIが兵器ルールを後退させたことがA-2品質で確認され [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046)、安全性萎縮効果の直接証拠が確定したが、Anthropicの$900B評価額は同じ萎縮効果と直接矛盾する。H-GOV-001は52%で据え置かれ [H-GOV-001](../config/hypotheses.json)、H-OAI-001は62%に低下した [H-OAI-001](../config/hypotheses.json)。SCN-003「静かな围い込み」が35%で最高確率を維持し [scenarios.json](../config/scenarios.json)、SCN-002が28%、SCN-001が18%、SCN-004が19%である。QHG Y軸再定義がArbiter v3.84で採用され、確率体系が更新された。

---

## 1. コア判断

市場の構図は三重構造に深化した。「OSS性能ギャップ消滅」「围い込み深化」「市場シェア再編」の同時進行に、安全性萎縮効果の制度化が加わった。今期は「多極化」が新たな認識枠組みとして浮上した。

市場シェアの多極化が確定した。WSJがAnthropicの評価額を$900B+とし、OpenAIを逆転した [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032)。TechCrunchは2025年5月以降のシェア4倍成長を報じた [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047)。Arbiterは「首位交代」から「多極化でのAnthropic台頭」へのフレーム修正を採用した。単一指標への依存は指摘されたが、WSJ A-2品質の評価額逆転と4倍シェア成長の方向性は一貫している。

OSS性能ギャップの消滅は確定的になった。DeepSeek R2がオープンソースでGPT-4oの9ベンチマークにマッチし [INFO-031](../Information/2026-05-20/collected-raw.md#INFO-031)、推論コストは$0.04-$0.31/M tokensに下がった。Mistralが$2.3B調達でopen weights戦略を継続している [INFO-033](../Information/2026-05-20/collected-raw.md#INFO-033)。収束方向はSCN-002「格差拡大」の前提を根本的に覆している。

围い込みは加速している。Google围い込み項目が15件に蓄積し、開放C証拠が15R連続で不在である。Gemini 3.5 Flash + Spark + Agent-to-UI [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015) がI/O 2026で追加された。Blackstone+Google $5B新AIクラウド企業 [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055) がTPUインフラ外部展開を開始する。性能均質化が围い込みを弱めるどころか、エコシステム深度を唯一の差別化要因として浮上させ、SCN-003「静かな围い込み」35%の根拠を強化している。

安全性萎縮効果がA-2品質で確定したが、矛盾する同時証拠もA-2品質で存在する。GoogleとOpenAIが兵器ルールを後退させたことがA-2品質で確認された [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046)。前回のB-3からA-2への昇格はH-GOV-001の根拠を大幅に強化する。しかしAnthropicの$900B評価額(A-2)+4倍シェア成長(A-3)は萎縮効果と直接矛盾する [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047)。Arbiterはこれを「矛盾する2つの真実」の均衡状態と評価した。H-GOV-001は52%据え置き。

エージェント本番環境の信頼性問題が構造化した。METR 43%本番破損+0%自信 [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049)、Gartner 40%失敗予測 [INFO-020](../Information/2026-05-20/collected-raw.md#INFO-020)、TrueFoundry 76%監査不可 [INFO-021](../Information/2026-05-20/collected-raw.md#INFO-021)、15%のみROI達成 [INFO-022](../Information/2026-05-20/collected-raw.md#INFO-022) で失敗5:成功1の比率が確定した。

$1TNのCAPEX過剰投資 hanging [INFO-034](../Information/2026-05-20/collected-raw.md#INFO-034) が市場の信頼性試験であり続ける。Blackstone $5B JV [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055) とAnthropic $900B [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) は資本集中の加速を示す。

QHG Y軸再定義がArbiter v3.84で採用された。Y軸が「格差拡大/収斂」から「フロンティア差別化の持続性: 持続(高付加価値維持) ←→ 薄薄(コモディティ化)」に変更され、17R連続のQHG凍結が解除された。新確率体系はSCN-001: 18%(-2%)、SCN-002: 28%(-2%)、SCN-003: 35%(±0%)、SCN-004: 19%(+4%)。v3.84以降の確率はv3.83以前と直接比較できないことに留意が必要である。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Anthropic $900B+でOpenAI逆転(WSJ A-2)。4倍シェア成長(TechCrunch) | 市場シェア多極化のA-2品質定量証拠。「首位交代」→「多極化」フレーム修正の根拠 | A-2/A-3 | [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) |
| 高 | Google/OpenAI兵器ルール後退(A-2) + Pentagon 8社承認(Anthropic除外) | 安全性萎縮効果のA-2品質確定。H-GOV-001 52%据え置き | A-2 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) |
| 高 | Google I/O 2026: Gemini 3.5 Flash 4x高速 + Spark + Agent-to-UI | 新フロンティアモデルリリース。围い込み15件。性能競争力継続 | B-3 | [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015) |
| 高 | DeepMind Co-Scientist: Nature論文・91%薬剤再利用・AlphaFold統合 | H-GOO-001「研究→製品」因果の最強証拠。DeepMind研究競争力の定量証明 | A-2 | [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) |
| 高 | METR 43%破損+0%自信+Gartner 40%失敗+76%監査不可+15%ROI | エージェント本番環境信頼性の構造化。失敗5:成功1でhigh移行確定 | A-3/B-2 | [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049) [INFO-020](../Information/2026-05-20/collected-raw.md#INFO-020) [INFO-021](../Information/2026-05-20/collected-raw.md#INFO-021) [INFO-022](../Information/2026-05-20/collected-raw.md#INFO-022) |
| 高 | DeepSeek R2 OSS GPT-4oマッチ・推論$0.04-$0.31/M | OSS性能ギャップの確定的消滅。収束方向継続 | B-3 | [INFO-031](../Information/2026-05-20/collected-raw.md#INFO-031) |
| 高 | Google围い込み15件蓄積 + 開放C 15R不在 + Blackstone $5B JV | 围い込みの多面的加速。SCN-003 35%の根拠強化。TPUインフラ外部展開 | A-2/A-3 | [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015) [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055) |
| 高 | PwC数十万人Claude展開・3万認証・CFO向け独立BU・納期70%改善 | エンタープライズ深度の最も具体的証拠。Anthropic商業的成功の直接確認 | A-3 | [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002) |
| 高 | Trump連邦ライセンス制度転向・OpenAI KOSA支持・米中AI安全協議 | 各国規制動機の異質性確認 | A-2 | [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) |
| 中 | OpenAI製品再編(Brockman統括)+IPO $852B+Microsoft離反検討 | OpenAI内部構造変化。IPO前の組織整理 | A-2 | [INFO-054](../Information/2026-05-20/collected-raw.md#INFO-054) |
| 中 | METR 43%乖離+Klarna再採用+ジュニア採用67%減少 | H-CAR-001/002/003関連C蓄積。方向性支持・速度不確定 | A-3/B-2 | [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Ramp AI IndexまたはWSJ評価額でOpenAIが3四半期連続で首位を回復する | 「多極化」判断が一時的変動の可能性。H-OAI-001回復の根拠 | 180日 | [IND-026](../config/indicators.json) |
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-001](../config/indicators.json) |
| SCN-002(28%)がSCN-003(35%)を逆転する | 围い込みコモディティ化の支配的地位が崩れ、多極化判断の前提が変わる | 180日 | [scenarios.json](../config/scenarios.json) |
| Pentagon SCR指定が法的に無効化され、Anthropicの政府市場アクセスが回復する | H-GOV-001の萎縮効果前提が崩れる | 180日 | [IND-030](../config/indicators.json) |
| Anthropicが`lawful use`条項を受諾し政府契約に回帰する | 「多極化」の前提が崩れ、安全性と商業の両立パターンが変わる | 90日 | [IND-030](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 62% | Codex 4M WAU+Dell提携+IPO $852Bはgenuine C。Anthropic首位交代(A-2)+DeepSeek R2ギャップ消失の2重IでI>C 2R連続 | [INFO-001](../Information/2026-05-20/collected-raw.md#INFO-001) [INFO-054](../Information/2026-05-20/collected-raw.md#INFO-054) | [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-031](../Information/2026-05-20/collected-raw.md#INFO-031) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 46% | 围い込み否定15件蓄積。low帯確定。OSSギャップ消滅がマルチモデル採用を加速 | (围い込み証拠不在継続) | (開放C蓄積継続) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 52% | INFO-046(A-2)兵器ルール後退は萎縮効果の直接A-2品質証拠。CDT萎縮効果(A-3)+Trump規制転向(A-2)の収斂。Anthropic $900B(A-2)+4xシェア(A-3)は萎縮効果と直接矛盾。「矛盾する2つの真実」の均衡状態で確度上昇不当 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) [INFO-025](../Information/2026-05-20/collected-raw.md#INFO-025) [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) | [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 26% | METR 43%破損+Klarna再採用+ジュニア採用67%減少のC蓄積。エリート遅延とAI信頼度低下は速度I。low範囲内 | [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049) | METR 43%品質問題 |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | ジュニア採用67%減+ミドル/シニアAI需要上昇の構造的裏付け。METR 43%破損+Klarna再採用は「書く」価値低下に直接反する。C/I相殺。69%上限 | [INFO-026](../Information/2026-05-20/collected-raw.md#INFO-026) | [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | 中間工程排除C蓄積。76%監査不可+15%ROI達成は監査 gaps の裏付け。41%企業が2030年まで人員削減計画 | [INFO-021](../Information/2026-05-20/collected-raw.md#INFO-021) [INFO-022](../Information/2026-05-20/collected-raw.md#INFO-022) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で high | Gemini 3.5 Flash 4x高速(独立検証待ち)。DeepSeek R2 OSS GPT-4oマッチ。BenchLM上位差3-4ptに縮小。high水準 | 2026-05-21 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | TanStack npm攻撃+AgentTrap 141タスク+METR 43%破損。攻撃面拡大加速。high水準 | 2026-05-21 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Opus 4.6 5B勝利+Gemini 3.5 Flash+Gemini Roboticsオンデバイス。量的向上継続。elevated水準 | 2026-05-21 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | METR 43%破損+0%自信+Gartner 40%失敗+76%監査不可+15%ROI。失敗5:成功1でhigh移行確定 | 2026-05-21 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | AAIF 43新メンバー+Azure MCP Server+Agent Skills 500++MCP 78%導入率。標準化加速。high水準 | 2026-05-21 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Hassabis AGI 2030+性能向上継続。主観-客観乖離継続。elevated水準 | 2026-05-21 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | $1TN+Anthropic $900B+Mistral $2.3B+Blackstone $5B JV。資本流入劇的加速。high水準 | 2026-05-21 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Google/OpenAI兵器ルール後退(A-2)+CDT萎縮効果+Trump規制転向+Pentagon 8社承認。high維持 | 2026-05-21 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-21 | QHG Y軸再定義採用・17R凍結解除・新確率体系反映・プレイヤー表更新 | Arbiter v3.84 Y軸再定義採用 | QHG 16R未定義→17R解除・SCN-001 20→18%・SCN-002 30→28%・SCN-003 35%据え置き・SCN-004 15→19%・§3反証閾値QHG行更新・§7ブラインドスポットQHG行更新 |
| 2026-05-20 | Anthropic $900B+OpenAI逆転+Gemini 3.5 Flash+Co-Scientist+兵器ルールA-2昇格+IND-026 high移行+Pattern C「多極化」フレーム修正を反映して全面書き直し | [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015) [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049) | H-OAI-001 63→62%・H-GOO-002 38→37%・H-GOV-001 52%据え置き・H-CAR-002 69%据え置き・IND-026 elevated→high・IND-030 B-3→A-2昇格・Pattern A中-高→中・Pattern C「首位交代」→「多極化」 |
| 2026-05-19 | IND-030 high移行+H-GOV-001 +1%(51→52%)+DeepSeek R2 OSS GPT-4oマッチ+Dell提携+Microsoft離反+プレイヤー表更新を反映 | [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037) [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) | H-GOV-001 51→52%・H-OAI-001 64→63%・H-GOO-002 39→38%・IND-030 elevated→high・QHG 12→14R未定義 |

---

## 7. ブラインドスポット

- H-GOV-001 52%とAnthropic $900B評価額の同時存在が最大の分析課題。萎縮効果で安全性が低下する(GOV)という読みと、安全性差別化で$900B評価額に達する(ANT)という読みが論理的緊張関係にある。Arbiterは「矛盾する2つの真実」と評価したが、この均衡がいつ崩れるかの判定基準が不足している。
- Anthropic $900Bの評価額が非公開市場推定値であり、収益run rateの内訳(消費者vsエンタープライズvs API)が非公開。PwC提携の実質的収益寄与も不明。評価額と実収益の乖離リスクを評価できない。
- Ramp AI Index逆転とWSJ評価額逆転がそれぞれ1データポイント。3四半期連続で多極化が維持されない場合、一時的変動の可能性が残る。
- QHG Y軸再定義で確率体系は更新されたが、「フロンティア差別化持続性」の定量化手法が未確立であり、Y軸判定への主観依存度が高い。v3.84以前との推移比較ができないため、傾向分析の連続性が失われた。
- $1TN CAPEX overhangのtimelineが不明確。2030年に米国電力の9-17%をAIインフラが消費する予測は物理的制約の定量示唆だが、投資削減への転換点を特定できない。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral $2.3B調達は「5社フレーム」自体の妥当性を問う結果である。
- 「業界全体押し上げ」代替説明が15R未解決。Claude +128%とGemini +48%とOpenAI逆転について、各社固有の成長要因を分離する方法論を持っていない。
- METR 43%本番破損とPwC 70%納期短縮の矛盾が未解決。両者のスケールの非対称性(体系的評価vs単一企業事例)を認識しつつ、品質問題の波及範囲を評価できない。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) | WSJ: Anthropic評価額$900B+でOpenAI逆転(A-2) |
| [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) | Google/OpenAI兵器ルール後退(A-2昇格) |
| [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015) | Google I/O 2026: Gemini 3.5 Flash+Spark+Agent-to-UI |
| [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) | DeepMind Co-Scientist: Nature論文・91%薬剤再利用(A-2) |
| [INFO-055](../Information/2026-05-20/collected-raw.md#INFO-055) | Blackstone+Google $5B JV + Blackstone+Anthropic JV(A-2) |
| [INFO-002](../Information/2026-05-20/collected-raw.md#INFO-002) | PwC数十万人Claude展開・3万認証・CFO向け独立BU(A-3) |
| [INFO-047](../Information/2026-05-20/collected-raw.md#INFO-047) | TechCrunch: 4倍シェア成長・金融40%・2028シナリオ論文(A-3) |
| [INFO-031](../Information/2026-05-20/collected-raw.md#INFO-031) | DeepSeek R2 OSS GPT-4oマッチ・推論$0.04-$0.31/M |
| [INFO-049](../Information/2026-05-20/collected-raw.md#INFO-049) | METR 43%本番破損・0%自信(A-3) |
| [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) | Trump連邦ライセンス転向(A-2) |
| [INFO-054](../Information/2026-05-20/collected-raw.md#INFO-054) | OpenAI製品再編・Brockman統括(A-2) |
| [INFO-021](../Information/2026-05-20/collected-raw.md#INFO-021) | TrueFoundry: 76%監査不可(B-2) |
| [INFO-020](../Information/2026-05-20/collected-raw.md#INFO-020) | Gartner: 40%Agentic AI失敗予測(C-3) |
| [INFO-022](../Information/2026-05-20/collected-raw.md#INFO-022) | 15%のみROI達成(C-3) |
| [INFO-025](../Information/2026-05-20/collected-raw.md#INFO-025) | CDT: Pentagon-Anthropic萎縮効果(A-3) |
| [INFO-033](../Information/2026-05-20/collected-raw.md#INFO-033) | Mistral $2.3B調達(A-2) |
| [INFO-034](../Information/2026-05-20/collected-raw.md#INFO-034) | $1TNデータセンター投資計画 |
| [INFO-026](../Information/2026-05-20/collected-raw.md#INFO-026) | WSJ: AIスキル持つエンジニア需要上昇(B-3) |
| [INFO-001](../Information/2026-05-20/collected-raw.md#INFO-001) | Codex + Dell提携 |
| [Arbiter v3.84](../state/arbiter-2026-05-21.md) | 確度評価の完全根拠 |
