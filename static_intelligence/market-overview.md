# AI市場全体 — 静的インテリジェンス

> 最終判断更新: 2026-05-18
> 全体確信度: 中
> 情報非対称性: ByteDance / DeepSeek のグローバルシェア追跡が困難。2nd tier (Mistral / Cohere) の動向が5社比較に入っていない。QHG象限再定義12R連続未実行で確率体系妥当性に疑義
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-001](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-18時点)

| 企業 | 主力モデル / 製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.7, Sonnet 4.6, Mythos, Claude Code | $50B調達中 [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)、$900B+評価額 [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) | 3位 (94) | Ramp AI Index初逆転34.4% vs OpenAI 32.3% [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。SaaStr Claude +128% [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025)。$30B収益run rate [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。Dario「SCR後も変えない」 [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038)。SWE-bench Pro 64.3%首位 [INFO-042](../Information/2026-05-17/collected-raw.md#INFO-042)。SDK課金分離6/15 |
| OpenAI | GPT-5.5, Codex (4M WAU), DeployCo | $852B評価額, $122B調達 | 4位 (92) | SaaStr OpenAI -8% [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025)。DeployCo $4B+。Sora 2終了・ロボティクス転用。Pentagon契約7社に参加。Fine-tuning API縮小 |
| Google | Gemini 3.1 Pro, Enterprise Agent Platform, Spark | Cloud $20B/63% YoY | 1位 (98) | Gemini 3.1 Pro ARC-AGI-2前世代2x [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041)。Enterprise Agent Platform [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007)。Gemini Spark常時依存 [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024)。围い込み13件蓄積+開放C 13R不在。DeepMind労組投票。SaaStr Gemini +48% [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) |
| SpaceXAI | Grok 4.1, Grok Connectors/STT/TTS | SpaceX $250BがxAIを買収 [INFO-047](../Information/2026-05-17/collected-raw.md#INFO-047) | 2位 (95) | Grok 4.1 LMArena 1483 Elo #1。Grok Build ACP [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006)。Pentagon契約7社に参加。H-XAI-001/H-XAI-003棄却 |
| ByteDance | 豆包2.0, Coze 2.5, Seed 2.0 | CAPEX $28B [INFO-057](../Information/2026-05-17/collected-raw.md#INFO-057) | 非公開 | Coze 2.5 Agent World。TikTok MCP Server。Huawei Ascend移行進行。CAPEX 25%増の$28B |

---

## 0. 一文要約

Ramp AI Indexが初めてOpenAIを逆転した [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。Claude 34.4% vs OpenAI 32.3%は、Anthropicの$50B調達 [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) と$30B収益run rate [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) が示す構造的成長の客観的裏付けだ。SaaStr調査でもClaude +128%(21→48%)がGemini +48%(27→40%)とOpenAI -8%を上回る [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025)。OSS性能ギャップは消滅したままで [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065)、SCN-003「静かな围い込み」が35%で最高確率を維持し [scenarios.json](../config/scenarios.json)、Google围い込みが13件に蓄積し [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) 開放証拠が13R連続不在である。Pentagon sagaが制度化した [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036)。Anthropic SCR + 7社契約 + Dario「変えない」宣言 [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) は、政府-AI関係が一過性ではない構造的変数であることを確定させた [H-GOV-001](../config/hypotheses.json) 51%。QHG象限の再定義が12R連続で未実行であり、確率体系の妥当性自体に疑義がある。

---

## 1. コア判断

市場の構図は三重構造に深化した。「OSS性能ギャップ消滅」「围い込み深化」「市場シェア再編」の同時進行である。

OSS性能ギャップの消滅は継続している。Kimi K2.6 SWE-bench Pro 58.6%がGPT-5.4 57.7%とOpus 4.6 53.4%を上回り [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065)、Mistral Medium 3.5 128B OpenがSWE-bench Verified 77.6%でオープンウェイト首位 [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045)、DeepSeek V4が$0.14/M tokensを実現 [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) している。Gemini 3.1 ProがARC-AGI-2で前世代の2倍性能を達成した [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) ことは、性能競争が終結したのではなく、差が縮小した状態で高位平準化していることを示す。15R連続の収束方向はSCN-002「格差拡大」の前提を根本的に覆し、性能均質化がエコシステム深度を唯一の差別化要因として浮上させている。

围い込みは加速している。Google围い込み項目が13件に蓄積し [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024)、開放C証拠が13R連続で不在である。Gemini Enterprise Agent Platformが構築・スケール・ガバナンスを一体化し [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007)、Gemini Sparkが常時稼働依存を創出する [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024)。OpenAI DeployCo $4B+がエンタープライズ展開の物理的基盤を構築し [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046)、AnthropicのSDK課金分離が開発者围い込みを深化させる [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038)。性能均質化が围い込みを弱めるどころか、エコシステム深度を唯一の差別化要因として浮上させ、SCN-003「静かな围い込み」35%の根拠を強化している [scenarios.json](../config/scenarios.json)。

市場シェアの再編がRamp AI Indexの初逆転で具現化した。Claude 34.4% vs OpenAI 32.3% [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) は、OpenAIの5四半期連続首位が終わった初の定量証拠である。SaaStr調査のClaude +128%(21→48%)・Gemini +48%(27→40%)・OpenAI -8% [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) も、三極化の進行を示す。Anthropicの$50B調達 [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) と$30B収益run rate [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) は、シェア拡大が資金力に裏付けられた構造的推移であることを示す。ただしSaaStrの「業界全体押し上げ」代替説明 [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) は、各社固有の成長要因を分離できない13R未解決の問題として残る。

Pentagon sagaが制度化した [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036)。7社契約 + Anthropic SCR拒否 + Dario「変えない」宣言 [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) + DeepMind労組投票 + FTC調査 [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) + EU AI Act [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028) の多面的展開は、政府-AI関係が一過性のイベントではなく構造的変数であることを確定させた。[H-GOV-001](../config/hypotheses.json) は51%に上昇した。安全性姿勢の市場変数化がAnthropicの$50B調達と共存していることは、萎縮効果と市場評価の均衡が成立していることを示す。

$800B-$1TのCAPEX過剰投資 hanging [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) が市場の信頼性試験であり続ける。Big 4ハイパースケーラーの$7,250億AIインフラ投資に対しFortune 500のAI成功は5%に過ぎない [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024)。Gartnerは60%が価値創出前に放棄されると予測する [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061)。Q1 2026 AI資金調達は$2,555億で2025年通年を超過 [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) しており、Anthropic $50B [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) もこの流れに加わる。

QHG象限の再定義が12R連続で未実行である。SCN-002/003の差が5%に拡大したものの、QHG軸の区別能力が消失している。確率体系の妥当性自体に疑義があり、次回Arbiterでの再定義が必須。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Ramp AI Index初逆転: Claude 34.4% vs OpenAI 32.3%。SaaStr: Claude +128% vs Gemini +48% vs OpenAI -8% | 市場シェア再編の定量証拠。OpenAI首位終了。三極化進行。各社固有要因分離は13R未解決 | A-2 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) |
| 高 | Anthropic $50B調達 + $30B収益run rate + Dario「変えない」 | $10B+調達の構造的変化。シェア拡大が資金力に裏付けられた推移。SCR後の戦略不変が市場評価と共存 | A-2 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |
| 高 | Pentagon saga制度化: 7社契約 + SCR + Dario宣言 + FTC + EU AI Act + DeepMind労組 | 政府-AI関係の構造的変数化確定。H-GOV-001 51%。安全性姿勢が市場変数として定着 | A-2 | [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028) |
| 高 | Google围い込み13件蓄積 + 開放C 13R不在 + Gemini Enterprise Agent Platform + Gemini Spark | 围い込みの多面的加速。開発者ツールチェーン~常時依存まで覆う。SCN-003 35%の根拠強化 | A-3 | [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) |
| 高 | Gemini 3.1 Pro ARC-AGI-2前世代2x + GPQA Diamond 94.3% | 高位平準化の継続。性能競争は終結せず差が縮小した状態で持続。OSSギャップ消滅と両立 | B-3 | [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) |
| 高 | Kimi K2.6 SWE-bench Pro 58.6% > GPT-5.4 57.7%。Mistral Open 77.6%。DeepSeek V4 $0.14/M tokens | OSS性能ギャップの構造的消滅継続。15R連続収束方向 | B-2 | [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) |
| 高 | $800B-$1T CAPEX過剰投資 hanging。Fortune 500 AI成功5%。Gartner 60%放棄予測 | 資本集中が围い込み物理的基盤を強化する一方、ROI不確定性が投資意欲を冷やす | B-2 | [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024) [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061) |
| 中 | Grok Build ACP [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006) + MCP 2026 [INFO-015](../Information/2026-05-18/collected-raw.md#INFO-015) + AWS AgentCore + Boomi MCP Registry | エコシステム標準化の多面的進展。IND-027 high | B-3 | [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006) [INFO-015](../Information/2026-05-18/collected-raw.md#INFO-015) |
| 中 | ByteDance CAPEX $28B + Coze 2.5 + TikTok MCP + Huawei Ascend移行 | ByteDanceの多面的拡張。围い込みと開放の二面性。グローバル展開証拠は依然不在 | B-2 | [INFO-057](../Information/2026-05-17/collected-raw.md#INFO-057) [INFO-010](../Information/2026-05-17/collected-raw.md#INFO-010) [INFO-056](../Information/2026-05-17/collected-raw.md#INFO-056) [INFO-058](../Information/2026-05-17/collected-raw.md#INFO-058) |
| 中 | 342K IT職消失 + エリートエンジニア20%遅延 + Klarna再採用 + AI信頼度29%(-11pt) | H-CAR-001 C蓄積継続。方向性支持・速度不確定 | B-2 | [INFO-032](../Information/2026-05-17/collected-raw.md#INFO-032) [INFO-060](../Information/2026-05-17/collected-raw.md#INFO-060) [INFO-034](../Information/2026-05-17/collected-raw.md#INFO-034) [INFO-062](../Information/2026-05-17/collected-raw.md#INFO-062) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Ramp AI IndexでOpenAIが3四半期連続で首位を回復する | 「市場シェア再編」判断の強さが問われる。Anthropic固有要因vs一時的変動の区別が必要 | 180日 | [IND-027](../config/indicators.json) |
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-001](../config/indicators.json) |
| Agent Platformで3社以外が測定可能な10%以上のシェアを取る | 「Agent Platform三社鼎立」が崩れ、SCN-002の前提が弱まる | 180日 | [IND-027](../config/indicators.json) |
| QHG象限の再定義でSCN-002/003が統合または再区分される | 二重構造判断の軸自体が変わり、確率推移の連続性が失われる | 30日 | [scenarios.json](../config/scenarios.json) |
| Pentagon SCR指定が法的に無効化され、Anthropicの政府市場アクセスが回復する | H-GOV-001の萎縮効果前提が崩れ、安全性姿勢の市場変数化が後退する | 180日 | [IND-030](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される、またはFortune 500 AI成功率が20%を超える | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |
| EU AI Act高リスク条項が完全に撤回される | 規制コンプライアンスを差別化要因にする安全性戦略の前提が崩れる | 180日 | [IND-030](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 64% | DeployCo $4B++Codex 4M WAU+7プロバイダーサンドボックス+Sea 87%WAUの強力なC蓄積。$14B損失とLLMシェア27%とRamp逆転がI。OSS性能ギャップ消滅がエコシステム深度の価値を相対的に高め構造的に支持 | [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) [INFO-005](../Information/2026-05-17/collected-raw.md#INFO-005) [INFO-063](../Information/2026-05-17/collected-raw.md#INFO-063) | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 46% | DeployCo $4B+のC蓄積vs Fine-tuning API縮小のI。下層開放圧力が上位围い込み有効性を構造的に制約。OSSギャップ消滅がマルチモデル採用を加速させ围い込みを弱める方向 | [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) [INFO-005](../Information/2026-05-17/collected-raw.md#INFO-005) | [INFO-037](../Information/2026-05-17/collected-raw.md#INFO-037) [INFO-049](../Information/2026-05-17/collected-raw.md#INFO-049) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 51% | Pentagon SCR+DPA+7社契約+DeepMind労組+California調達要件+FTC調査+EU AI Actの7方向C蓄積。Dario「変えない」宣言 [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) は萎縮効果が Anthropicの戦略選択に影響していないことを示す。Anthropic提訴+Sanders法案は歯止めI。51%はmid帯 | [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) | [INFO-030](../Information/2026-05-17/collected-raw.md#INFO-030) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 26% | 342K IT職消失+BLS 1000万職露出+エリート20%遅延+AI信頼度29%のC蓄積。エリート遅延とAI信頼度低下は速度I。Klarna再採用は方向性I。low範囲内 | [INFO-032](../Information/2026-05-17/collected-raw.md#INFO-032) [INFO-051](../Information/2026-05-17/collected-raw.md#INFO-051) [INFO-060](../Information/2026-05-17/collected-raw.md#INFO-060) | [INFO-034](../Information/2026-05-17/collected-raw.md#INFO-034) [INFO-062](../Information/2026-05-17/collected-raw.md#INFO-062) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | 84%開発者AI使用+51%毎日使用+342K IT職消失+SaaS溶解の強力なC蓄積。AI信頼度29%(-11pt)は品質I。シニア需要上昇+ジュニア採用減速が構造的裏付け | [INFO-062](../Information/2026-05-17/collected-raw.md#INFO-062) [INFO-051](../Information/2026-05-17/collected-raw.md#INFO-051) [INFO-006](../Information/2026-05-17/collected-raw.md#INFO-006) | [INFO-060](../Information/2026-05-17/collected-raw.md#INFO-060) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流・下流に集中する | 57% | ミドルウェア陳腐化+SaaS溶解+広告中間層破壊+Meta 23億バリアント+McKinsey ERP変革の5重C蓄積。Fortune 500 5%成功は運用実績I | [INFO-006](../Information/2026-05-17/collected-raw.md#INFO-006) [INFO-036](../Information/2026-05-17/collected-raw.md#INFO-036) [INFO-035](../Information/2026-05-17/collected-raw.md#INFO-035) [INFO-031](../Information/2026-05-17/collected-raw.md#INFO-031) | [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で high | Gemini 3.1 Pro ARC-AGI-2前世代2x [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041)。BenchLM上位差3-4ptに縮小。OSS性能ギャップ消滅継続。high水準 | 2026-05-18 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Endor Labs: npmマルウェア14倍増+Bitwarden CLI攻撃がClaude Code/Codex/Gemini CLI標的 [INFO-012](../Information/2026-05-17/collected-raw.md#INFO-012)。high水準 | 2026-05-17 |
| [IND-025](../config/indicators.json) | 規制・政策動向 | 主要市場で新規制発効で elevated | 米国1200+AI法案+California調達AI要件+EU AI Act [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028)+中国エージェント国家戦略。elevated水準 | 2026-05-18 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | Fortune 500 AI成功5% [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024)。Gartner 60%放棄予測 [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061)。銀行70%パイロット/本番。elevated水準 | 2026-05-18 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 2026 [INFO-015](../Information/2026-05-18/collected-raw.md#INFO-015)+Grok Build ACP [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006)+7プロバイダーサンドボックス+Boomi MCP Registry。high水準 | 2026-05-18 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Hassabis AGI 2030+Musk 2026年末+Kimi K2.6 OSS首位+ARC-AGI-3 33%+。elevated水準 | 2026-05-17 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | $800B-$1T CAPEX overhang+ByteDance $28B+Q1 $2,555億調達+Anthropic $50B [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。high水準 | 2026-05-18 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で elevated | Pentagon saga制度化 [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036)+FTC調査 [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037)+EU AI Act [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028)+DeepMind労組。elevated水準 | 2026-05-18 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-18 | Ramp AI Index初逆転+$50B調達+Pentagon saga制度化+Gemini 3.1 Pro+Google围い込み13件+Grok ACPを反映して全面更新 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) | H-GOV-001 50→51%・H-GOO-001 55→54%・H-GOO-002 40→39%・H-BTD-002 58→57%・QHG 11→12R未定義・プレイヤー表更新・「二重構造」→「三重構造」 |
| 2026-05-17 | OSS性能ギャップ消滅+$800B-$1T CAPEX overhang+Fortune 500 5%を反映して全面書き直し | [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) | 「SCN-003最高確率。Pentagon圧力で政府-AI再編」→「OSSギャップ消滅が構造的シフト。围い込みは深化。$800B-$1T過剰投資hanging」 |
| 2026-05-14 | SCN-003最高確率34%+Pentagon SCR/DPAを反映して全面書き直し | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) | 「性能均質化と围い込みの二重構造」→「SCN-003最高確率。Pentagon圧力で政府-AI関係が構造的再編」 |
| 2026-05-12 | DeployCo設立+SCN-002/003同率33%を反映 | [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005) | SCN-002 34→33%・SCN-003 32→33%。同率でQHG軸区別能力消失 |
| 2026-05-07 | Static v2構造に全面移行 | STATIC_INTELLIGENCE_v2.md 仕様適用 | 旧: 逐次トピック羅列 → 新: §0〜§7 + プレイヤー表 |

---

## 7. ブラインドスポット

- Ramp AI Index逆転が1四半期のデータポイントである。3四半期連続で維持されない場合、一時的変動の可能性が残る。SaaStr調査との相互検証は可能だが、調査手法の差異が比較を複雑にする。
- OSS性能ギャップ消滅の速度と範囲が不確定。Kimi K2.6とMistral Medium 3.5の結果は単一ベンチマーク(SWE-bench)に基づく。マルチモーダル・推論・長文脈など他領域でのOSS優位性は未検証。ベンチマーク水増し問題(Llama 4事案 [INFO-047](../Information/2026-05-14/collected-raw.md#INFO-047))が再発する可能性がある。
- QHG象限の再定義が12R連続で未実行。SCN-002/003の差が5%に拡大したが、QHG軸の区別能力が消失しており、確率体系の妥当性自体に疑義がある。次回Arbiterでの再定義が必須。
- $800B-$1T CAPEX overhangの timeline が不明確。Fortune 500の5%成功率とガイダンスの不整合がどの時点で投資削減に転じるかは、ハイパースケーラーの四半期決算次第だが観測頻度が不十分。Anthropic $50Bがこの流れを加速させるか鈍化させるかも未評価。
- 2nd tier プレイヤーの動向を5社比較に入れていない。Mistral Medium 3.5 128B OpenのSWE-bench 77.6%首位 [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) は「5社フレーム」自体の妥当性を問う結果である。Cohere / AI21 / Reka の技術力・シェア・資金調達状況は評価できていない。
- 「業界全体押し上げ」代替説明が13R未解決。Claude +128%とGemini +48%とOpenAI -8%の同期間変動について、各社固有の成長要因を分離する方法論を持っていない。
- 個人開発者(vs エンタープライズ)のツール選好変化を観測できていない。Claude Code・Codex・Cursor・Gemini CLI間のシェア推移は、エコシステム围い込みの実効性を判断する重要指標だが、定量データが構造的に取れていない。
- DeepSeek V4 $0.14/M tokens [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) が市場価格体系に与える影響が未分析。この価格設定が持続可能か、または dumping による一時的戦略かの区別が、トークン価格の67%低下トレンドがどこまで進むかに直結する。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) | Ramp AI Index初逆転(Claude 34.4% vs OpenAI 32.3%) + $30B収益run rate |
| [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) | Pentagon saga制度化(7社契約+SCR+DPA) |
| [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) | FTC調査 |
| [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) | Dario「SCR後も変えない」宣言 |
| [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) | Gemini 3.1 Pro(ARC-AGI-2前世代2x) |
| [INFO-007](../Information/2026-05-18/collected-raw.md#INFO-007) | Gemini Enterprise Agent Platform(包括的スタック) |
| [INFO-024](../Information/2026-05-18/collected-raw.md#INFO-024) | Gemini Spark(常時稼働AIエージェント) |
| [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) | SaaStr: Claude +128% vs Gemini +48% vs OpenAI -8% |
| [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028) | EU AI Act |
| [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006) | Grok Build ACP |
| [INFO-015](../Information/2026-05-18/collected-raw.md#INFO-015) | MCP 2026 |
| [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) | Kimi K2.6 SWE-bench Pro 58.6%(GPT-5.4/Opus 4.6凌駕) |
| [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) | Mistral Medium 3.5 128B Open SWE-bench Verified 77.6%首位 |
| [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) | DeepSeek V4 $0.14/M tokens(フロンティア1/6コスト) |
| [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) | DeployCo $4B+/Anthropic $900B+評価額/Q1 $2,555億調達 |
| [INFO-047](../Information/2026-05-17/collected-raw.md#INFO-047) | SpaceX $250BでxAI買収 |
| [INFO-042](../Information/2026-05-17/collected-raw.md#INFO-042) | Grok 4.1 LMArena 1483 Elo #1/Opus 4.7 SWE-bench Pro 64.3% |
| [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) | $800B-$1T CAPEX過剰投資 hanging |
| [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024) | Fortune 500 AI成功5%/銀行70%エージェント展開 |
| [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) | Anthropic SDK課金分離6/15 |
| [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) | Pentagon 7社契約/Anthropic SCR |
| [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) | DeepMind労組設立投票 |
| [INFO-006](../Information/2026-05-17/collected-raw.md#INFO-006) | ミドルウェア陳腐化(LangChain/LlamaIndex) |
| [INFO-032](../Information/2026-05-17/collected-raw.md#INFO-032) | 342K IT職消失/BLS 1000万職AI露出 |
| [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061) | Gartner 60%放棄予測 |
| [INFO-057](../Information/2026-05-17/collected-raw.md#INFO-057) | ByteDance CAPEX $28B(25%増) |
| [INFO-058](../Information/2026-05-17/collected-raw.md#INFO-058) | Huawei Ascend移行 |
| [Arbiter v3.81](../state/arbiter-2026-05-18.md) | 確度評価の完全根拠 |
