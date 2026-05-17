# AI市場全体 — 静的インテリジェンス

> 最終判断更新: 2026-05-17
> 全体確信度: 中
> 情報非対称性: ByteDance / DeepSeek のグローバルシェア追跡が困難。2nd tier (Mistral / Cohere) の動向が5社比較に入っていない。QHG象限再定義11R連続未実行で確率体系妥当性に疑義
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-001](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-17時点)

| 企業 | 主力モデル / 製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.7, Sonnet 4.6, Mythos, Claude Code | $900B+評価額オファー [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) | 3位 (94) | Claude for Small Business [INFO-003](../Information/2026-05-17/collected-raw.md#INFO-003)。SDK課金分離6/15 [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038)。スタートアップ33% vs エンタープライズ13% [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059)。SWE-bench Pro 64.3%首位 [INFO-042](../Information/2026-05-17/collected-raw.md#INFO-042)。Blackstone/H&F/GS合弁 [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001)。Pentagon SCR継続 [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) |
| OpenAI | GPT-5.5, Codex (4M WAU), DeployCo | $852B評価額, $122B調達 | 4位 (92) | DeployCo $4B+設立 [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046)。7プロバイダーサンドボックス統合 [INFO-005](../Information/2026-05-17/collected-raw.md#INFO-005)。Sora 2終了・ロボティクス転用 [INFO-019](../Information/2026-05-17/collected-raw.md#INFO-019)。Pentagon契約7社に参加 [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027)。Fine-tuning API縮小 [INFO-037](../Information/2026-05-17/collected-raw.md#INFO-037) |
| Google | Gemini 3.1, Enterprise Agent Platform | Cloud $20B/63% YoY | 1位 (98) | Interactions API + Deep Research [INFO-009](../Information/2026-05-17/collected-raw.md#INFO-009)。Gemini 3 Pro DT multimodal 100.0%首位 [INFO-018](../Information/2026-05-17/collected-raw.md#INFO-018)。DeepMind労組設立投票 [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028)。围い込み12項目蓄積。Pentagon秘密契約 [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) |
| SpaceXAI | Grok 4.1, Grok Connectors/STT/TTS | SpaceX $250BがxAIを買収 [INFO-047](../Information/2026-05-17/collected-raw.md#INFO-047) | 2位 (95) | Grok 4.1 LMArena 1483 Elo #1 [INFO-042](../Information/2026-05-17/collected-raw.md#INFO-042)。SpaceX $250BでのxAI買収完了 [INFO-047](../Information/2026-05-17/collected-raw.md#INFO-047)。Pentagon契約7社に参加 [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027)。H-XAI-001/H-XAI-003棄却 |
| ByteDance | 豆包2.0, Coze 2.5, Seed 2.0 | CAPEX $28B [INFO-057](../Information/2026-05-17/collected-raw.md#INFO-057) | 非公開 | Coze 2.5 Agent World [INFO-010](../Information/2026-05-17/collected-raw.md#INFO-010)。TikTok MCP Server [INFO-056](../Information/2026-05-17/collected-raw.md#INFO-056)。Huawei Ascend移行進行 [INFO-058](../Information/2026-05-17/collected-raw.md#INFO-058)。CAPEX 25%増の$28B [INFO-057](../Information/2026-05-17/collected-raw.md#INFO-057) |

---

## 0. 一文要約

OSS性能ギャップが構造的に消滅した。Kimi K2.6がSWE-bench Pro 58.6%でGPT-5.4 57.7%とOpus 4.6 53.4%を上回り [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065)、Mistral Medium 3.5 128B OpenがSWE-bench Verified 77.6%でオープンウェイト首位 [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045)、DeepSeek V4が$0.14/M tokensでフロンティア性能の1/6コストを実現 [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) している。SCN-002「格差拡大」の前提が15R連続の収束方向で崩壊した。しかし围い込みはむしろ深化しており、SCN-003「静かな围い込み」が35%で最高確率を維持し [scenarios.json](../config/scenarios.json)、Google围い込み項目が12に蓄積、OpenAI DeployCo $4B+がエンタープライズ深度を強化 [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) している。$800B-$1TのCAPEX過剰投資 hanging [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) がFortune 500の5%成功率 [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024) とGartner 60%放棄予測 [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061) の中で市場の信頼性を問うている。QHG象限の再定義が11R連続で未実行であり、確率体系の妥当性自体に疑義がある。

---

## 1. コア判断

市場の構図は「OSS性能ギャップ消滅」と「围い込み深化」の二重構造に転換した。前者は構造的シフトであり、後者はそれにもかかわらず進行する逆潮流である。

OSS性能ギャップの消滅は、SCN-002「格差拡大」前提の根本的崩壊を意味する。Kimi K2.6 SWE-bench Pro 58.6% > GPT-5.4 57.7% > Opus 4.6 53.4%という結果 [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) は、非米系OSSモデルがフロンティア性能を上回った初の明確な証拠である。Mistral Medium 3.5 128B OpenのSWE-bench Verified 77.6% [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) はオープンウェイトでSWE-bench首位を獲得し、DeepSeek V4の$0.14/M tokens [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) は性能コスト比の新基準を打ち立てた。15R連続の収束方向は、性能差を围い込みの主要な差別化要因とする論理を根底から覆す。しかし性能均質化は围い込みを弱めるどころか、エコシステム深度を唯一の差別化要因として浮上させ、SCN-003「静かな围い込み」35%の根拠をむしろ強化している [scenarios.json](../config/scenarios.json)。

围い込みは多面化している。Google围い込み項目が12に蓄積しており [H-GOO-002](../config/hypotheses.json) 40%で推移、Gemini Interactions API [INFO-009](../Information/2026-05-17/collected-raw.md#INFO-009) とEnterprise Agent Platform [INFO-023](../Information/2026-05-17/collected-raw.md#INFO-023) が開発者ツールチェーンからエンタープライズワークフローまで覆う。OpenAI DeployCo $4B+ [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) はBain/Capgemini/McKinseyとの提携でエンタープライズ展開の物理的基盤を構築する。AnthropicのSDK課金分離 [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) はAgent SDKクレジット制度で開発者围い込みを深化させるが、Claude Codeがスタートアップ33% vs エンタープライズ13% [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059) という分布は、エンタープライズ围い込みの有効性に限界がある可能性を示す。Agentic AIのロックインが契約ではなくワークフローのフレームワーク依存に起因する [INFO-020](../Information/2026-05-17/collected-raw.md#INFO-020) ことも围い込みの実態を補強する。

政府-AI関係の構造的再編が継続している。Pentagonが7社(SpaceX/OpenAI/Google/Nvidia/Reflection/MSFT/AWS)とAI契約を締結し [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027)、Anthropicのみが$200M契約を拒否してSCR指定を受けている。DeepMind従業員が労組設立に投票し [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028)、GoogleのPentagon傾斜に対する内部抵抗が顕在化した。米国では1200以上のAI法案が提出され連邦・州間の規制矛盾が激化 [INFO-025](../Information/2026-05-17/collected-raw.md#INFO-025) し、カリフォルニア州が調達力を通じたAIベンダー倫理要件を導入 [INFO-030](../Information/2026-05-17/collected-raw.md#INFO-030) している。中国はAIエージェント国家戦略を発表 [INFO-026](../Information/2026-05-17/collected-raw.md#INFO-026) し、Huawei Ascendへの移行が進行 [INFO-058](../Information/2026-05-17/collected-raw.md#INFO-058) している。[H-GOV-001](../config/hypotheses.json) は50%に上昇し、政府介入の萎縮効果と歯止めの均衡が続く。

$800B-$1TのCAPEX過剰投資 hanging [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) が市場の信頼性試験になりつつある。Big 4ハイパースケーラーの$7,250億AIインフラ投資 [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) に対し、Fortune 500のAI投資で成果を見ているのは5%に過ぎない [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024)。Gartnerは60%が価値創出前に放棄されると予測 [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061) する。この資本集中は围い込みの物理的基盤を強化する方向に働く一方で、ROIの不確定性が投資意欲を冷やす逆効果も持つ。Q1 2026 AI資金調達は$2,555億で2025年通年を超過 [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) しており、過剰投資の持続可能性が問われている。

雇用面ではH-CAR-001のC蓄積が続く。2022年以来342,000のIT職が消失し [INFO-032](../Information/2026-05-17/collected-raw.md#INFO-032)、BLSが18職種・約1000万職をAI露出ありと分類 [INFO-051](../Information/2026-05-17/collected-raw.md#INFO-051) している。エリートエンジニアがAIツールで20%遅くなった [INFO-060](../Information/2026-05-17/collected-raw.md#INFO-060) という発見は、AIツールの効果が期待と乖離していることを示す。Klarnaの再採用 [INFO-034](../Information/2026-05-17/collected-raw.md#INFO-034) は自動化速度に不確定性があることを再確認させた。ミドルウェア層の陳腐化 [INFO-006](../Information/2026-05-17/collected-raw.md#INFO-006) はSaaSpocalypseを加速させ [INFO-036](../Information/2026-05-17/collected-raw.md#INFO-036)、[H-CAR-003](../config/hypotheses.json) 57%を支えている。

QHG象限の再定義が11R連続で未実行である。SCN-002/003の差が5%に拡大したものの、QHG軸の区別能力が消失している。確率体系の妥当性自体に疑義があり、次回Arbiterでの再定義が必須。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Kimi K2.6 SWE-bench Pro 58.6% > GPT-5.4 57.7% > Opus 4.6 53.4%。Mistral Open 77.6%。DeepSeek V4 $0.14/M tokens | OSS性能ギャップの構造的消滅。SCN-002「格差拡大」前提の根本的崩壊。15R連続収束方向。性能差の価値低下がエコシステム深度の価値を相対的に高める | B-2 | [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) |
| 高 | SCN-003 35% > SCN-002 30%。15R連続同一方向シフト。QHG再定義11R未実行 | 围い込み方向が開放方向を確率で上回り継続。QHG軸の区別能力消失で確率体系妥当性に疑義 | B-3 | [scenarios.json](../config/scenarios.json) |
| 高 | $800B-$1T CAPEX過剰投資 hanging。Fortune 500 AI成功5%。Gartner 60%放棄予測 | 資本集中が围い込み物理的基盤を強化する一方、ROI不確定性が投資意欲を冷やす。市場信頼性試験 | B-2 | [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024) [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061) |
| 高 | Pentagon 7社契約+Anthropic SCR拒否+DeepMind労組+California調達要件 | 政府-AI関係の構造的再編継続。H-GOV-001 50%。安全性姿勢が市場変数として定着 | B-2 | [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) [INFO-030](../Information/2026-05-17/collected-raw.md#INFO-030) |
| 高 | DeployCo $4B+ + Anthropic $900B+ + SDK課金分離 + Claude for Small Business | エンタープライズ围い込みの物理的基盤強化(OpenAI)と多層化(Anthropic SMB~Enterprise)。Anthropicはスタートアップ33% vs エンタープライズ13%で偏り | A-3 | [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) [INFO-003](../Information/2026-05-17/collected-raw.md#INFO-003) [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059) |
| 高 | Google围い込み12項目蓄積+Interactions API+Vertex AI Agent Builder+Gemini Live Agent Challenge 11,878参加者 | Google围い込みの多面化が進行。開発者ツールチェーン~エンタープライズプラットフォーム~コンテストエコシステムの3層で囲い込む | A-3 | [INFO-009](../Information/2026-05-17/collected-raw.md#INFO-009) [INFO-023](../Information/2026-05-17/collected-raw.md#INFO-023) [INFO-007](../Information/2026-05-17/collected-raw.md#INFO-007) |
| 中 | ByteDance CAPEX $28B + Coze 2.5 Agent World + TikTok MCP + Huawei Ascend移行 | ByteDanceの多面的拡張。围い込みと開放の二面性。グローバル展開証拠は依然不在 | B-2 | [INFO-057](../Information/2026-05-17/collected-raw.md#INFO-057) [INFO-010](../Information/2026-05-17/collected-raw.md#INFO-010) [INFO-056](../Information/2026-05-17/collected-raw.md#INFO-056) [INFO-058](../Information/2026-05-17/collected-raw.md#INFO-058) |
| 中 | 342K IT職消失+エリートエンジニア20%遅延+Klarna再採用+AI信頼度29%(-11pt) | H-CAR-001 26%のC蓄積継続。方向性支持・速度不確定。AI効果の期待乖離が新たなI | B-2 | [INFO-032](../Information/2026-05-17/collected-raw.md#INFO-032) [INFO-060](../Information/2026-05-17/collected-raw.md#INFO-060) [INFO-034](../Information/2026-05-17/collected-raw.md#INFO-034) [INFO-062](../Information/2026-05-17/collected-raw.md#INFO-062) |
| 中 | ミドルウェア陳腐化(LangChain/LlamaIndex)+SaaS溶解+広告中間層破壊 | H-CAR-003 57%のC蓄積。バリューチェーン中間工程の大規模再編が加速 | B-2 | [INFO-006](../Information/2026-05-17/collected-raw.md#INFO-006) [INFO-036](../Information/2026-05-17/collected-raw.md#INFO-036) [INFO-035](../Information/2026-05-17/collected-raw.md#INFO-035) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-001](../config/indicators.json) |
| Agent Platformで3社以外(Mistral / Cohere等)が測定可能な10%以上のシェアを取る | 「Agent Platform三社鼎立」が崩れ、SCN-002の前提が弱まる | 180日 | [IND-027](../config/indicators.json) |
| QHG象限の再定義でSCN-002/003が統合または再区分される | 二重構造判断の軸自体が変わり、確率推移の連続性が失われる | 30日 | [scenarios.json](../config/scenarios.json) |
| Pentagon SCR指定が法的に無効化され、Anthropicの政府市場アクセスが回復する | H-GOV-001の萎縮効果前提が崩れ、安全性姿勢の市場変数化が後退する | 180日 | [IND-030](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される、またはFortune 500 AI成功率が20%を超える | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |
| EU AI Act高リスク条項が完全に撤回される | 規制コンプライアンスを差別化要因にする安全性戦略の前提が崩れる | 180日 | [IND-030](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 64% | DeployCo $4B++Codex 4M WAU+7プロバイダーサンドボックス+Sea 87%WAUの強力なC蓄積。$14B損失とLLMシェア27%がI。OSS性能ギャップ消滅がエコシステム深度の価値を相対的に高め、H-OAI-001を構造的に支持する | [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) [INFO-005](../Information/2026-05-17/collected-raw.md#INFO-005) [INFO-063](../Information/2026-05-17/collected-raw.md#INFO-063) | [INFO-037](../Information/2026-05-17/collected-raw.md#INFO-037) [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 46% | DeployCo $4B+のC蓄積vs Fine-tuning API縮小のI。下層開放圧力(MCPデファクト)が上位围い込み有効性を構造的に制約。OSSギャップ消滅がマルチモデル採用を加速させ围い込みを弱める方向。46%はlow帯境界 | [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) [INFO-005](../Information/2026-05-17/collected-raw.md#INFO-005) | [INFO-037](../Information/2026-05-17/collected-raw.md#INFO-037) [INFO-049](../Information/2026-05-17/collected-raw.md#INFO-049) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 50% | Pentagon SCR+DPA+7社契約+DeepMind労組+California調達要件+中国エージェント規制の6方向C蓄積。Anthropic提訴+Sanders法案は歯止めI。C/I均衡。50%はmid帯 | [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) [INFO-029](../Information/2026-05-17/collected-raw.md#INFO-029) [INFO-025](../Information/2026-05-17/collected-raw.md#INFO-025) | [INFO-030](../Information/2026-05-17/collected-raw.md#INFO-030) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 26% | 342K IT職消失+BLS 1000万職露出+エリート20%遅延+AI信頼度29%のC蓄積。エリート遅延とAI信頼度低下は速度I。Klarna再採用は方向性I。low範囲内 | [INFO-032](../Information/2026-05-17/collected-raw.md#INFO-032) [INFO-051](../Information/2026-05-17/collected-raw.md#INFO-051) [INFO-060](../Information/2026-05-17/collected-raw.md#INFO-060) | [INFO-034](../Information/2026-05-17/collected-raw.md#INFO-034) [INFO-062](../Information/2026-05-17/collected-raw.md#INFO-062) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | 84%開発者AI使用+51%毎日使用+342K IT職消失+SaaS溶解の強力なC蓄積。AI信頼度29%(-11pt)は品質I。方向性支持強い。シニア需要上昇+ジュニア採用減速が構造的裏付け | [INFO-062](../Information/2026-05-17/collected-raw.md#INFO-062) [INFO-051](../Information/2026-05-17/collected-raw.md#INFO-051) [INFO-006](../Information/2026-05-17/collected-raw.md#INFO-006) | [INFO-060](../Information/2026-05-17/collected-raw.md#INFO-060) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流・下流に集中する | 57% | ミドルウェア陳腐化+SaaS溶解+広告中間層破壊+Meta 23億バリアント+McKinsey ERP変革の5重C蓄積。方向性支持。速度不確定。Fortune 500 5%成功は運用実績I | [INFO-006](../Information/2026-05-17/collected-raw.md#INFO-006) [INFO-036](../Information/2026-05-17/collected-raw.md#INFO-036) [INFO-035](../Information/2026-05-17/collected-raw.md#INFO-035) [INFO-031](../Information/2026-05-17/collected-raw.md#INFO-031) | [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で high | BenchLM上位差3-4ptに縮小。OSS性能ギャップ消滅 [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045)。high水準 | 2026-05-17 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Endor Labs: npmマルウェア14倍増+Bitwarden CLI攻撃がClaude Code/Codex/Gemini CLI標的 [INFO-012](../Information/2026-05-17/collected-raw.md#INFO-012)。high水準 | 2026-05-17 |
| [IND-025](../config/indicators.json) | 規制・政策動向 | 主要市場で新規制発効で elevated | 米国1200+AI法案提出+連邦州矛盾激化 [INFO-025](../Information/2026-05-17/collected-raw.md#INFO-025)。California調達AI要件 [INFO-030](../Information/2026-05-17/collected-raw.md#INFO-030)。中国エージェント国家戦略 [INFO-026](../Information/2026-05-17/collected-raw.md#INFO-026)。elevated水準 | 2026-05-17 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | Fortune 500 AI成功5% [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024)。Gartner 60%放棄予測 [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061)。銀行70%パイロット/本番 [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024)。elevated水準 | 2026-05-17 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCPデファクト化継続+7プロバイダーサンドボックス [INFO-005](../Information/2026-05-17/collected-raw.md#INFO-005)+Boomi MCP Registry [INFO-014](../Information/2026-05-17/collected-raw.md#INFO-014)+AWS AgentCore [INFO-021](../Information/2026-05-17/collected-raw.md#INFO-021)。high水準 | 2026-05-17 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Hassabis AGI 2030+Musk 2026年末+Kimi K2.6 OSS首位 [INFO-053](../Information/2026-05-17/collected-raw.md#INFO-053) [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065)。ARC-AGI-3 33%+ [INFO-041](../Information/2026-05-17/collected-raw.md#INFO-041)。elevated水準 | 2026-05-17 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | $800B-$1T CAPEX overhang [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048)+ByteDance $28B [INFO-057](../Information/2026-05-17/collected-raw.md#INFO-057)+Q1 $2,555億調達 [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046)。high水準 | 2026-05-17 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で elevated | Pentagon 7社契約+SCR+DeepMind労組+California要件+中国戦略+Huawei Ascend [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) [INFO-030](../Information/2026-05-17/collected-raw.md#INFO-030) [INFO-026](../Information/2026-05-17/collected-raw.md#INFO-026) [INFO-058](../Information/2026-05-17/collected-raw.md#INFO-058)。elevated水準 | 2026-05-17 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-17 | OSS性能ギャップ消滅(Kimi K2.6>Mistral Open>DeepSeek V4)+$800B-$1T CAPEX overhang+Fortune 500 5%+SCN-002 31→30%/SCN-004 14→15%を反映して全面書き直し | [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024) | 「SCN-003最高確率。Pentagon圧力で政府-AI再編」→「OSSギャップ消滅が構造的シフト。围い込みは深化。$800B-$1T過剰投資hanging。QHG 11R未定義」 |
| 2026-05-14 | SCN-003が最高確率34%に順位変動・Pentagon SCR/DPA・GPT-Realtime 3モデル・TikTok MCP・DeerFlow OSSを反映して全面書き直し | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) [INFO-011](../Information/2026-05-14/collected-raw.md#INFO-011) [INFO-012](../Information/2026-05-14/collected-raw.md#INFO-012) | 「性能均質化と围い込みの二重構造」→「SCN-003が最高確率に。Pentagon圧力で政府-AI関係が構造的再編。Google受諾vs Anthropic拒否の分化が鮮明」 |
| 2026-05-12 | DeployCo設立・SCN-002/003同率33%・AI Search围い込み・GTIGゼロデイを反映 | [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-12/collected-raw.md#INFO-006) | SCN-002 34→33%・SCN-003 32→33%。同率でQHG軸区別能力消失 |
| 2026-05-12 | Azure排他性終了・OSSギャップ消滅・围い込み7重C蓄積・SCN-002/003差2%・雇用二極化を反映して全面書き直し | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) | SCN-002 37→34%・SCN-003 29→32%。差2%に縮小 |
| 2026-05-07 | Static v2構造に全面移行 | STATIC_INTELLIGENCE_v2.md 仕様適用 | 旧: 逐次トピック羅列 → 新: §0〜§7 + プレイヤー表 |
| 2026-05-06 | JV/FDE同時採用・Agent Platform三社鼎立・围い込みシグナル4重蓄積を反映 | [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) | SCN-002 44→38%・SCN-003 24→28% |

---

## 7. ブラインドスポット

- OSS性能ギャップ消滅の速度と範囲が不確定。Kimi K2.6とMistral Medium 3.5の結果は単一ベンチマーク(SWE-bench)に基づく。マルチモーダル・推論・長文脈など他領域でのOSS優位性は未検証。ベンチマーク水増し問題(Llama 4事案 [INFO-047](../Information/2026-05-14/collected-raw.md#INFO-047))が再発する可能性がある。
- QHG象限の再定義が11R連続で未実行。SCN-002/003の差が5%に拡大したが、QHG軸の区別能力が消失しており、確率体系の妥当性自体に疑義がある。次回Arbiterでの再定義が必須。このまま未実行が続けば、SCN-002とSCN-003を統合した新シナリオの検討が必要。
- $800B-$1T CAPEX overhangの timeline が不明確。McKinsey試算の$5.2-7.9兆と、Fortune 500の5%成功率の不整合がどの時点で投資削減に転じるかは、ハイパースケーラーの四半期決算とガイダンス次第だが、観測頻度が不十分。
- 2nd tier プレイヤーの動向を5社比較に入れていない。Mistral Medium 3.5 128B OpenのSWE-bench 77.6%首位 [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) は「5社フレーム」自体の妥当性を問う結果である。Cohere / AI21 / Reka の技術力・シェア・資金調達状況は評価できていない。
- 個人開発者(vs エンタープライズ)のツール選好変化を観測できていない。Claude Code・Codex・Cursor・Gemini CLI間のシェア推移は、エコシステム围い込みの実効性を判断する重要指標だが、定量データが構造的に取れていない。Agent Skills marketplaceの17Kユーザー [INFO-020](../Information/2026-05-14/collected-raw.md#INFO-020) は代替指標になりうるが継続追跡が必要。
- DeepSeek V4 $0.14/M tokens [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) が市場価格体系に与える影響が未分析。この価格設定が持続可能か、または dumping による一時的戦略かの区別が、トークン価格の67%低下トレンド [INFO-042](../Information/2026-05-14/collected-raw.md#INFO-042) がどこまで進むかに直結する。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) | Kimi K2.6 SWE-bench Pro 58.6%(GPT-5.4/Opus 4.6凌駕) |
| [INFO-045](../Information/2026-05-17/collected-raw.md#INFO-045) | Mistral Medium 3.5 128B Open SWE-bench Verified 77.6%首位 |
| [INFO-044](../Information/2026-05-17/collected-raw.md#INFO-044) | DeepSeek V4 $0.14/M tokens(フロンティア1/6コスト) |
| [INFO-046](../Information/2026-05-17/collected-raw.md#INFO-046) | DeployCo $4B+/Anthropic $900B+評価額/Rampデータ逆転 |
| [INFO-047](../Information/2026-05-17/collected-raw.md#INFO-047) | SpaceX $250BでxAI買収 |
| [INFO-042](../Information/2026-05-17/collected-raw.md#INFO-042) | Grok 4.1 LMArena 1483 Elo #1/Opus 4.7 SWE-bench Pro 64.3% |
| [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048) | $800B-$1T CAPEX過剰投資 hanging |
| [INFO-024](../Information/2026-05-17/collected-raw.md#INFO-024) | Fortune 500 AI成功5%/銀行70%エージェント展開 |
| [INFO-061](../Information/2026-05-17/collected-raw.md#INFO-061) | Gartner 60%放棄予測/エンタープライズ40%エージェント組み込み |
| [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) | Anthropic SDK課金分離6/15 |
| [INFO-003](../Information/2026-05-17/collected-raw.md#INFO-003) | Claude for Small Business |
| [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001) | Anthropic/Blackstone/H&F/GS合弁エンタープライズAIサービス |
| [INFO-005](../Information/2026-05-17/collected-raw.md#INFO-005) | OpenAI Agents SDK 7プロバイダーサンドボックス統合 |
| [INFO-006](../Information/2026-05-17/collected-raw.md#INFO-006) | ミドルウェア陳腐化(LangChain/LlamaIndex) |
| [INFO-009](../Information/2026-05-17/collected-raw.md#INFO-009) | Gemini Interactions API + Deep Research Agent |
| [INFO-010](../Information/2026-05-17/collected-raw.md#INFO-010) | Coze 2.5 Agent World |
| [INFO-018](../Information/2026-05-17/collected-raw.md#INFO-018) | BenchLM multimodal (Gemini 3 Pro DT 100%/Grok 4.1 97.8%) |
| [INFO-020](../Information/2026-05-17/collected-raw.md#INFO-020) | Agentic AI lock-in = workflow entanglement |
| [INFO-025](../Information/2026-05-17/collected-raw.md#INFO-025) | 米国1200+AI法案/連邦州規制矛盾 |
| [INFO-026](../Information/2026-05-17/collected-raw.md#INFO-026) | 中国AIエージェント国家戦略 |
| [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) | Pentagon 7社契約/Anthropic $200M拒否/SCR指定 |
| [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) | DeepMind労組設立投票 |
| [INFO-029](../Information/2026-05-17/collected-raw.md#INFO-029) | Anthropic-Pentagon対立のchilling effect |
| [INFO-030](../Information/2026-05-17/collected-raw.md#INFO-030) | California調達AI倫理要件 |
| [INFO-031](../Information/2026-05-17/collected-raw.md#INFO-031) | Meta AI 23億広告バリアント/67%コスト削減 |
| [INFO-032](../Information/2026-05-17/collected-raw.md#INFO-032) | 342K IT職消失/BLS 1000万職AI露出 |
| [INFO-034](../Information/2026-05-17/collected-raw.md#INFO-034) | Klarna 700人解雇→再採用/Duolingo AI-First |
| [INFO-035](../Information/2026-05-17/collected-raw.md#INFO-035) | 広告エージェンシー中間層破壊/B2B SaaS暴落 |
| [INFO-036](../Information/2026-05-17/collected-raw.md#INFO-036) | SaaS溶解→インテント/McKinsey ERP変革 |
| [INFO-037](../Information/2026-05-17/collected-raw.md#INFO-037) | API価格比較(GPT-5.5 $5/$30, Claude $3/$15) |
| [INFO-041](../Information/2026-05-17/collected-raw.md#INFO-041) | ARC/HLEベンチマーク最新 |
| [INFO-049](../Information/2026-05-17/collected-raw.md#INFO-049) | マルチベンダーAI戦略記録的水準 |
| [INFO-051](../Information/2026-05-17/collected-raw.md#INFO-051) | BLS 18職種1000万職AI露出 |
| [INFO-053](../Information/2026-05-17/collected-raw.md#INFO-053) | AGI timeline(Musk 2026/Hassabis 2030) |
| [INFO-056](../Information/2026-05-17/collected-raw.md#INFO-056) | TikTok MCP Server |
| [INFO-057](../Information/2026-05-17/collected-raw.md#INFO-057) | ByteDance CAPEX $28B(25%増) |
| [INFO-058](../Information/2026-05-17/collected-raw.md#INFO-058) | Huawei Ascend移行/Trump-Xi AI協議 |
| [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059) | Claude Code startups 33% vs enterprises 13% |
| [INFO-060](../Information/2026-05-17/collected-raw.md#INFO-060) | エリートエンジニアAI使用で20%遅延 |
| [INFO-062](../Information/2026-05-17/collected-raw.md#INFO-062) | 84%開発者AI使用/信頼度29%(-11pt) |
| [INFO-063](../Information/2026-05-17/collected-raw.md#INFO-063) | Sea Codex 87%WAU/73%推奨 |
| [INFO-012](../Information/2026-05-17/collected-raw.md#INFO-012) | Endor Labs Agent Governance/npmマルウェア14倍 |
| [INFO-023](../Information/2026-05-17/collected-raw.md#INFO-023) | Google Vertex AI Agent Builder |
| [INFO-007](../Information/2026-05-17/collected-raw.md#INFO-007) | Gemini Live Agent Challenge 11,878参加者 |
| [INFO-021](../Information/2026-05-17/collected-raw.md#INFO-021) | AWS Bedrock AgentCore Payments |
| [INFO-014](../Information/2026-05-17/collected-raw.md#INFO-014) | Boomi MCP Registry統合 |
| [INFO-050](../Information/2026-05-17/collected-raw.md#INFO-050) | AI tools underpriced $100-200/month真コスト |
| [INFO-019](../Information/2026-05-17/collected-raw.md#INFO-019) | Gemini Omniリーク/Sora 2終了 |
| [INFO-002](../Information/2026-05-17/collected-raw.md#INFO-002) | Claude Sonnet 4.6 SWE-bench 80.2%/1M context |
| [INFO-039](../Information/2026-05-17/collected-raw.md#INFO-039) | Gemini API pricing Flash-Lite $0.10/$0.40 |
| [INFO-040](../Information/2026-05-17/collected-raw.md#INFO-040) | BenchLM LLM価格比較プラットフォーム |
| [INFO-043](../Information/2026-05-17/collected-raw.md#INFO-043) | 25モデル評価: 最先端AI専門家70%一致 |
| [INFO-008](../Information/2026-05-17/collected-raw.md#INFO-008) | OpenAI Agent Improvement Loop |
| [INFO-064](../Information/2026-05-17/collected-raw.md#INFO-064) | Interaction Models 276B MoE(Thinking Machines Lab) |
| [Arbiter v3.77](../state/arbiter-2026-05-14.md) | 確度評価の完全根拠(付録のみ参照) |
