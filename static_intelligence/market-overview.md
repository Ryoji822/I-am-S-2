# AI市場全体 — 静的インテリジェンス

> 最終判断更新: 2026-05-19
> 全体確信度: 中
> 情報非対称性: ByteDance / DeepSeek のグローバルシェア追跡が困難。2nd tier (Mistral / Cohere) の動向が5社比較に入っていない。QHG象限再定義14R連続未実行で確率体系妥当性に疑義
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-001](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-19時点)

| 企業 | 主力モデル / 製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.6, Sonnet 4.6, Mythos, Claude Code | $50B調達中、$900B+評価額 | 3位 (94) | Ramp AI Index初逆転32% [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030)。PwC提携で30,000人認定 [INFO-001](../Information/2026-05-19/collected-raw.md#INFO-001)。SMB市場参入 [INFO-003](../Information/2026-05-19/collected-raw.md#INFO-003)。Opus 4.6がGemini 2.5 Proに5B勝利 [INFO-021](../Information/2026-05-19/collected-raw.md#INFO-021)。9連邦機関Claude停止 [INFO-019](../Information/2026-05-19/collected-raw.md#INFO-019) |
| OpenAI | GPT-5.5, Codex (4M WAU), DeployCo | $852B評価額 [INFO-024](../Information/2026-05-19/collected-raw.md#INFO-024) | 4位 (92) | Dell提携でハイブリッド/オンプレ展開 [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004)。IPO 2026年末目指す [INFO-024](../Information/2026-05-19/collected-raw.md#INFO-024)。ChatGPT広告開始 [INFO-007](../Information/2026-05-19/collected-raw.md#INFO-007)。Microsoft離反シグナル [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) |
| Google | Gemini 3.1 Pro, Enterprise Agent Platform, Googlebook | Cloud $20B/63% YoY | 1位 (98) | 兵器誓約削除 [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037)。I/O 2026で新Gemini+Gemini Omni予想 [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006)。围い込み14件蓄積+開放C 14R不在。Googlebook今秋発売。DeepMind労組投票 |
| SpaceXAI | Grok 4.3, Grok Build CLI, Voice Agent API | SpaceX $250BがxAIを買収 | 2位 (95) | Grok Build ACP対応 [INFO-010](../Information/2026-05-19/collected-raw.md#INFO-010)。Grok 4.3最新モデル。Voice Agent API提供。価格競争力の課題。H-XAI-001/H-XAI-003棄却確認 |
| ByteDance | 豆包2.0, Coze 2.5, DeerFlow 2.0 | CAPEX $28B | 非公開 | DeerFlow 2.0 GitHub 68K stars [INFO-008](../Information/2026-05-19/collected-raw.md#INFO-008)。豆包有料化開始。DeepSeek R2 OSS GPT-4oマッチ [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) |

---

## 0. 一文要約

IND-030がelevatedからhighに移行した [IND-030](../config/indicators.json)。Google兵器誓約削除 [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037)、CDT 9連邦機関Claude停止 [INFO-019](../Information/2026-05-19/collected-raw.md#INFO-019)、UK Safety→Security改名の5重C蓄積で、能力とリスクの二面性が新段階に到達した。H-GOV-001は52%に上昇した [H-GOV-001](../config/hypotheses.json)。Ramp AI Index初逆転(Anthropic 32%)とMicrosoft離反シグナルで [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023)、H-OAI-001は63%に低下した。OSS性能ギャップはDeepSeek R2 GPT-4oマッチで消滅が確定的になり [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031)、SCN-003「静かな围い込み」が35%で最高確率を維持する [scenarios.json](../config/scenarios.json)。QHG象限の再定義が14R連続で未実行であり、確率体系の妥当性自体に疑義がある。

---

## 1. コア判断

市場の構図は三重構造に深化した。「OSS性能ギャップ消滅」「围い込み深化」「市場シェア再編」の同時進行に、安全性萎縮効果の制度化が加わった。

OSS性能ギャップの消滅は確定的になった。DeepSeek R2がオープンソースでGPT-4oの9ベンチマークにマッチし [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031)、Mistralが$2.3B調達でopen weights戦略を継続している [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033)。V3.2-SpecialeがIMO/IOIで金レベルを達成した [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) ことは、OSSの能力上限が予想を上回っていることを示す。17R連続の収束方向はSCN-002「格差拡大」の前提を根本的に覆している。

围い込みは加速している。Google围い込み項目が14件に蓄積し、開放C証拠が14R連続で不在である。Gemini Enterprise Agent Platform [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011) とGooglebook [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006) が新たに加わった。OpenAI DeployCo $4B+とDell提携 [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004) がエンタープライズ展開の物理的基盤を構築している。性能均質化が围い込みを弱めるどころか、エコシステム深度を唯一の差別化要因として浮上させ、SCN-003「静かな围い込み」35%の根拠を強化している。

市場シェアの再編がRamp AI Indexの初逆転で具現化した。Anthropic 32% vs OpenAI [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) は、OpenAIの首位が終わった初の定量証拠である。Microsoftが「OpenAI後を見据えたスタートアップ買収」を検討している [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) ことは、パートナーシップ構造に亀裂が入った直接証拠だ。

安全性萎縮効果が制度化した。Google兵器誓約削除 [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037)、CDT 9連邦機関Claude停止 [INFO-019](../Information/2026-05-19/collected-raw.md#INFO-019)、Pentagon報酬構造 [INFO-016](../Information/2026-05-19/collected-raw.md#INFO-016)、UK改名、NYT安全性限界指摘 [INFO-041](../Information/2026-05-19/collected-raw.md#INFO-041) の5重C蓄積でIND-030がhighに移行した。H-GOV-001は52%に上昇した。しかしAnthropicの商業的成功(32%シェア)は萎縮効果への強力な反証として共存しており、両者の同時確度上昇が最大の分析課題である。

$1TNのCAPEX過剰投資 hanging [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) が市場の信頼性試験であり続ける。2030年までに$1兆がデータセンター容量に投資され、米国で680施設が計画中である。

QHG象限の再定義が14R連続で未実行である。SCN-002/003の差が5%に拡大したものの、QHG軸の区別能力が消失している。確率体系の妥当性自体に疑義があり、次回Arbiterでの再定義が必須。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | IND-030 high移行: Google兵器誓約削除+CDT 9機関停止+UK改名+Pentagon報酬+NYT限界指摘の5重C蓄積 | 能力-リスク二面性の新段階到達。H-GOV-001 52%上昇の根拠 | B-3/A-2 | [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037) [INFO-019](../Information/2026-05-19/collected-raw.md#INFO-019) [INFO-041](../Information/2026-05-19/collected-raw.md#INFO-041) |
| 高 | Ramp AI Index初逆転: Anthropic 32% > OpenAI。Microsoft離反シグナル(Reuters A-2) | 市場シェア再編の定量証拠。OpenAI首位終了。H-OAI-001 63%低下 | B-2/A-2 | [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) |
| 高 | DeepSeek R2 OSS GPT-4oマッチ・V3.2-Speciale IMO/IOI金レベル | OSS性能ギャップの確定的消滅。17R連続収束方向 | C-2 | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) |
| 高 | Google围い込み14件蓄積 + 開放C 14R不在 + Gemini Enterprise Agent Platform + Googlebook | 围い込みの多面的加速。SCN-003 35%の根拠強化 | A-3 | [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011) [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006) |
| 高 | OpenAI Dell提携+IPO $8520億+Codex 4M WAU+ChatGPT広告開始 | エンタープライス展開インフラ強化と収益多様化の同時進行 | A-3 | [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004) [INFO-024](../Information/2026-05-19/collected-raw.md#INFO-024) |
| 高 | $1TNデータセンター投資計画・2030年迄・米国680施設 | 資本集中が围い込み物理的基盤を強化。ROI不確定性が投資意欲を冷やす | B-2 | [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) |
| 中 | DeerFlow 2.0 GitHub 68K stars・Mistral $2.3B調達・Grok Build ACP | エコシステム標準化とOSSエコシステムの多面的進展 | C-3/B-3 | [INFO-008](../Information/2026-05-19/collected-raw.md#INFO-008) [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033) [INFO-010](../Information/2026-05-19/collected-raw.md#INFO-010) |
| 中 | METR 43%乖離+Klarna再採用+ジュニア採用67%減少 | H-CAR-001 C蓄積継続。方向性支持・速度不確定 | C-2/B-2 | [INFO-038](../Information/2026-05-19/collected-raw.md#INFO-038) [INFO-027](../Information/2026-05-19/collected-raw.md#INFO-027) [INFO-032](../Information/2026-05-19/collected-raw.md#INFO-032) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Ramp AI IndexでOpenAIが3四半期連続で首位を回復する | 「市場シェア再編」判断の強さが問われる | 180日 | [IND-026](../config/indicators.json) |
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-001](../config/indicators.json) |
| QHG象限の再定義でSCN-002/003が統合または再区分される | 三重構造判断の軸自体が変わり、確率推移の連続性が失われる | 30日 | [scenarios.json](../config/scenarios.json) |
| Pentagon SCR指定が法的に無効化され、Anthropicの政府市場アクセスが回復する | H-GOV-001の萎縮効果前提が崩れる | 180日 | [IND-030](../config/indicators.json) |
| Google兵器誓約削除がA-2+ソースで確認され、かつ他社も追従する | H-GOV-001萎縮効果が確定的となり、安全性後退が業界全体の構造的変数に昇格する | 90日 | [IND-030](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 63% | Codex 4M WAU+Dell提携+IPO $8,520億はgenuine C。市場シェア初逆転(INFO-030 B-2)+Microsoft離反(INFO-023 A-2)の2重診断的Iで初のI>Cラウンド。次回I>C継続で更に-1% | [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004) [INFO-024](../Information/2026-05-19/collected-raw.md#INFO-024) | [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 46% | 围い込み否定15件蓄積。low帯確定。OSSギャップ消滅がマルチモデル採用を加速 | [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-014](../Information/2026-05-19/collected-raw.md#INFO-014) | (围い込み証拠不在継続) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 52% | INFO-037 Google兵器誓約削除(B-3)は初の他社安全性後退直接証拠。CDT 9機関停止(A-2)+UK改名(B-3)の収斂。上限条件は「候補」に留めA-2+確認必要。Anthropic商業的成功(INFO-030 B-2)は反証として記録 | [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037) [INFO-019](../Information/2026-05-19/collected-raw.md#INFO-019) | [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 26% | METR 43%乖離+Klarna再採用+ジュニア採用67%減少のC蓄積。エリート遅延とAI信頼度低下は速度I。low範囲内 | [INFO-038](../Information/2026-05-19/collected-raw.md#INFO-038) [INFO-027](../Information/2026-05-19/collected-raw.md#INFO-027) [INFO-032](../Information/2026-05-19/collected-raw.md#INFO-032) | [INFO-027](../Information/2026-05-19/collected-raw.md#INFO-027) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | ジュニア採用67%減少+全体SE求人30%増加の構造的裏付け。METR 43%乖離は品質I | [INFO-032](../Information/2026-05-19/collected-raw.md#INFO-032) | [INFO-038](../Information/2026-05-19/collected-raw.md#INFO-038) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | 中間工程排除C蓄積。76%エンタープライスが統合ロギングなし(INFO-015)は監査 gaps の裏付け | [INFO-015](../Information/2026-05-19/collected-raw.md#INFO-015) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で high | DeepSeek R2 OSS GPT-4oマッチ。BenchLM上位差3-4ptに縮小。OSS性能ギャップ消滅確定。high水準 | 2026-05-19 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | MCP token theft+TanStack npm攻撃+AgentTrap 141タスク。攻撃面拡大加速。high水準 | 2026-05-19 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Opus 4.6 5B勝利+DeepSeek V3.2 Speciale金レベル。量的向上継続。elevated水準 | 2026-05-19 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | METR 43%乖離+Klarna再採用。high移行4ソース到達。次回検討。elevated水準 | 2026-05-19 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | 7サンドボックス+Grok Build ACP+DeerFlow 2.0。標準化爆発的加速。high水準 | 2026-05-19 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Hassabis AGI 2030+Opus 4.6ベンチマーク向上。主観-客観乖離継続。elevated水準 | 2026-05-19 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | $1TN+Mistral $2.3B+機関投資家必須+IPO $8,520億。資本流入劇的加速。high水準 | 2026-05-19 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Google兵器誓約削除+CDT 9機関停止+UK改名+Pentagon報酬+NYT限界指摘の5重C蓄積。high移行確定 | 2026-05-19 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-19 | IND-030 high移行+H-GOV-001 +1%(51→52%)+DeepSeek R2 OSS GPT-4oマッチ+Dell提携+Microsoft離反+プレイヤー表更新を反映して全面更新 | [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037) [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) | H-GOV-001 51→52%・H-OAI-001 64→63%・H-GOO-002 39→38%・IND-030 elevated→high・QHG 12→14R未定義・プレイヤー表更新 |
| 2026-05-18 | Ramp AI Index初逆転+$50B調達+Pentagon saga制度化+Gemini 3.1 Pro+Google围い込み13件+Grok ACPを反映 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-041](../Information/2026-05-18/collected-raw.md#INFO-041) | H-GOV-001 50→51%・H-GOO-001 55→54%・H-GOO-002 40→39% |

---

## 7. ブラインドスポット

- H-GOV-001とH-ANT-001の同時確度上昇(GOV 52% vs ANT 49%)が最大の分析課題。萎縮効果で安全性が低下する(GOV)という読みと、安全性差別化で優位に立つ(ANT)という読みが論理的緊張関係にある。両者の同時上昇は論理的矛盾の可能性(メソドロジー(3)監視中)。
- Ramp AI Index逆転が1四半期のデータポイントである。3四半期連続で維持されない場合、一時的変動の可能性が残る。Ramp AI Index単一指標の限界に注意。
- QHG象限の再定義が14R連続で未実行。SCN-002/003の差が5%に拡大したが、QHG軸の区別能力が消失しており、確率体系の妥当性自体に疑義がある。次回Arbiterでの再定義が必須(強制実行対象)。
- $1TN CAPEX overhangのtimelineが不明確。2030年に米国電力の9-17%をAIインフラが消費する予測 [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) は物理的制約の定量示唆だが、投資削減への転換点を特定できない。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral $2.3B調達 [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033) は「5社フレーム」自体の妥当性を問う結果である。
- 「業界全体押し上げ」代替説明が14R未解決。Claude +128%とGemini +48%とOpenAI逆転について、各社固有の成長要因を分離する方法論を持っていない。
- Anthropic H-ANT-001の確度判断で「6C中5Cは安全性直接Cでない」(Red指摘採用)が新ルールとして導入された。安全性差別化の直接的証拠(INFO-040 C-2のみ)が限定的であり、49%上限条件継続。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-037](../Information/2026-05-19/collected-raw.md#INFO-037) | Google兵器誓約削除(IND-030 high移行の根拠) |
| [INFO-019](../Information/2026-05-19/collected-raw.md#INFO-019) | CDT 9連邦機関Claude停止(IND-030 high移行の根拠) |
| [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) | Ramp AI Index初逆転(Anthropic 32% > OpenAI) |
| [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) | Microsoft離反シグナル(Reuters A-2) |
| [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) | DeepSeek R2 OSS GPT-4oマッチ・V3.2 Speciale金レベル |
| [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004) | OpenAI + Dell提携(ハイブリッド/オンプレ) |
| [INFO-024](../Information/2026-05-19/collected-raw.md#INFO-024) | IPO評価額$8,520億 |
| [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011) | Gemini Enterprise Agent Platform |
| [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006) | Google I/O 2026+Googlebook+Gemini Omni |
| [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) | $1TNデータセンター投資計画 |
| [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033) | Mistral $2.3B調達($14B評価額) |
| [INFO-008](../Information/2026-05-19/collected-raw.md#INFO-008) | DeerFlow 2.0 GitHub 68K stars |
| [INFO-041](../Information/2026-05-19/collected-raw.md#INFO-041) | NYT安全性コントロール限界指摘 |
| [INFO-016](../Information/2026-05-19/collected-raw.md#INFO-016) | Pentagon報酬構造($200M各社) |
| [INFO-038](../Information/2026-05-19/collected-raw.md#INFO-038) | METR 43%乖離(エリートコーダー20%遅延) |
| [INFO-027](../Information/2026-05-19/collected-raw.md#INFO-027) | Klarna AIレイオフ後再採用 |
| [INFO-032](../Information/2026-05-19/collected-raw.md#INFO-032) | ジュニア開発者採用67%減少 |
| [INFO-015](../Information/2026-05-19/collected-raw.md#INFO-015) | 76%エンタープライス統合ロギングなし |
| [Arbiter v3.82](../state/arbiter-2026-05-19.md) | 確度評価の完全根拠 |
