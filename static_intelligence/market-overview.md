# AI市場全体 — 静的インテリジェンス

> 最終判断更新: 2026-05-14
> 全体確信度: 中
> 情報非対称性: ByteDance / DeepSeek のグローバルシェア追跡が困難。2nd tier (Mistral / Cohere) の動向が5社比較に入っていない。Pentagon SCR/DPAの因果チェーン「未確認」継続
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), scenarios.json#SCN-002/SCN-003, [indicators.json](../config/indicators.json) [IND-001](../config/indicators.json) [IND-013](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-14時点)

| 企業 | 主力モデル / 製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.7, Sonnet 4.6, Mythos, Claude Code | $3,800億評価額(Series G)。Google最大$400億 | 1位 (99) | Pentagon SCR+DPA [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040) [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039)。Agent SDK credit 6/15 [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010)。Mythos Preview SWE-bench Multimodal 59% [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026)。Sandbox Runtime OSS [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027) |
| OpenAI | GPT-5.5, Codex (4M WAU), DeployCo | $852B評価額, $122B調達 | 3位 (92) | Fine-tuning API縮小 [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043)。Sora 2終了・ロボティクス転用 [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023)。GPT-Realtime 3モデル [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005)。広告日本/UK/Korea等展開 [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008)。Codex Windows sandbox [INFO-078](../Information/2026-05-14/collected-raw.md#INFO-078) |
| Google | Gemini 3.1, Enterprise Agent Platform | 自己資金 + Anthropic投資 | 2位 (93) | Pentagon秘密契約+抗議 [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039)。AndroidエージェントAI+Gemini Omni [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023)。Chrome DevTools MCP [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024)。Gemini CLI extensions [INFO-028](../Information/2026-05-14/collected-raw.md#INFO-028) |
| SpaceXAI | Grok 4.3, Grok Connectors/STT/TTS | SpaceX $3,500億評価 | 4位 (90) | Colossus 1 Anthropic貸与。Grok 5製品連続リリース [INFO-012](../Information/2026-05-14/collected-raw.md#INFO-012)。[H-XAI-001](../config/hypotheses.json)/[H-XAI-003](../config/hypotheses.json)棄却 |
| ByteDance | 豆包2.0, Seed 2.0, Coze 2.5 | CAPEX 2000億元($30B) | 非公開 | TikTok MCP Server [INFO-013](../Information/2026-05-14/collected-raw.md#INFO-013)。DeerFlow OSS。Seedance 2.0世界#2 [INFO-064](../Information/2026-05-14/collected-raw.md#INFO-064)。CAPEX 25%増 [INFO-065](../Information/2026-05-14/collected-raw.md#INFO-065)。Doubao全モダリティ [INFO-062](../Information/2026-05-14/collected-raw.md#INFO-062) |

---

## 0. 一文要約

SCN-003「静かな围い込み」が34%で初めて最高確率シナリオに浮上し、SCN-002「開放標準と勝者」の32%を上回った。技術は開き続けるが、エコシステム深度を通じた围い込みが確率で先行する構造に転換した。最大の根拠は、PentagonのAnthropic SCR指定+DPA脅迫が米国企業初の措置であること [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040) と、GoogleがPentagon秘密AI契約を受諾しつつAnthropicがこれを拒否した分化 [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039) だ。この「受諾vs拒否」の対立は、安全性姿勢が市場変数になる最も明確なシグナルである。同時にMCPデファクト標準化が加速し [INFO-021](../Information/2026-05-14/collected-raw.md#INFO-021)、エンタープライズトークンコストは67%低下 [INFO-042](../Information/2026-05-14/collected-raw.md#INFO-042) するなど技術面の開放圧力も継続している。もしQHG象限の再定義が実行されSCN-002/003が統合されるか、Pentagon圧力が法的・政治的に無効化されるなら、この読みは変わる。

---

## 1. コア判断

市場の構図は「技術は開くが、围い込みは深まる」という二重構造に収束し続けている。しかし、SCN-003が初めてSCN-002を上回り、围い込み方向が確率で先行する新たな段階に入った。

SCN-003が34%で最高確率になった意味は大きい。11R連続でSCN-002からSCN-003へのシフトが続いており [H-GOV-001](../config/hypotheses.json)、围い込みの蓄積速度が開放の蓄積を上回っている。MCPデファクト標準化がAAIF 97M SDKダウンロードに達したことは [INFO-021](../Information/2026-05-14/collected-raw.md#INFO-021) 開放の強力な推進力だが、Chrome DevTools MCPがGoogle围い込みツールとして機能する二面性 [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) や、Codex Windowsサンドボックス独自実装 [INFO-078](../Information/2026-05-14/collected-raw.md#INFO-078) は围い込みの多様化を示している。エンタープライズトークンコストの67%低下 [INFO-042](../Information/2026-05-14/collected-raw.md#INFO-042) は技術コモディティ化を加速させ、性能差の価値を低下させる一方で、エコシステム深度の価値を相対的に高めている。

政府-AI関係の構造的再編が市場の新たな次元になった。PentagonがAnthropicをSCR(サプライチェーンリスク)に指定したことは、外国敵対企業に使われるdesignationを米国企業に初適用した前例である [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040)。DPA(国防生産法)に基づく脅迫の存在も報じられている [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039)。同時にGoogleはPentagonと秘密AI契約を締結し [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039)、従業員抗議が発生している。Scale AIへの契約も$1億から$5億に5倍増額され、Metaの49%出資が懸念材料として付随する [INFO-038](../Information/2026-05-14/collected-raw.md#INFO-038)。Google受諾vs Anthropic拒否の分化は、安全性姿勢が調達資格・市場アクセスに直結する構造的転換点である。この分化が [H-GOV-001](../config/hypotheses.json) の萎縮効果Cとして蓄積している。ただしAnthropicの提訴 [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040) とSanders法案 [INFO-066](../Information/2026-05-14/collected-raw.md#INFO-066) は歯止めIとして機能する可能性がある。

OpenAIは多面的な戦略転換を進めている。Fine-tuning APIの段階的縮小 [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) とSora 2のシャットダウン・ロボティクス転用 [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) は製品ポートフォリオの再編を示す。GPT-Realtime-2/Translate/Whisperの3モデル同時リリース [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) は音声領域への本格参入だ。Codexの2ヶ月無料エンタープライズプロモーション [INFO-072](../Information/2026-05-14/collected-raw.md#INFO-072) は、DeployCo $4B+の展開インフラ [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004) と合わせて [H-OAI-001](../config/hypotheses.json) のC蓄積である。ただし確証バイアス警告が3R連続で発出されており、DeployCo収益・採用実績の独立確認が不在であることに注意が必要である。ChatGPT広告の日本/UK/Korea等への展開 [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) は収益モデルの多角化だが、[H-OAI-002](../config/hypotheses.json) の围い込みを弱める要素でもある。

Anthropicは技術面で強いシグナルを出している。Claude Mythos PreviewがSWE-bench Multimodal 59%でトップを獲得し [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026)、サイバーセキュリティにおけるstep changeとして評価されている。Sandbox RuntimeのOSS公開 [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027) は安全性を開発者エコシステムに組み込む戦略だ。Agent SDKクレジット制度が6月15日に開始される [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010)。ただしPentagon SCR+DPAによる政府市場への影響は、 Anthropicのエンタープライズ戦略にとって重大なIである [H-GOV-001](../config/hypotheses.json)。

Googleは围い込みを多面化している。AndroidへのエージェントAI導入とGemini Omniリーク [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) はモバイルエコシステムへの围い込みを示す。Chrome DevTools MCP [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) とGemini CLI extensions [INFO-028](../Information/2026-05-14/collected-raw.md#INFO-028) は開発者ツールチェーンへの围い込みだ。Pentagon秘密契約受諾は政府市場アクセスを確保するが、安全性姿勢の後退リスクを伴う。

ByteDanceの拡張が顕著である。TikTok MCP Server [INFO-013](../Information/2026-05-14/collected-raw.md#INFO-013) は広告プラットフォームのAI自動化を進め、DeerFlow OSSはエージェント開発のオープン化を示す。Seedance 2.0がVideo Arena世界第2位に [INFO-064](../Information/2026-05-14/collected-raw.md#INFO-064) なり、Doubaoの全モダリティ対応 [INFO-062](../Information/2026-05-14/collected-raw.md#INFO-062) が進展。CAPEX 25%増の$30B [INFO-065](../Information/2026-05-14/collected-raw.md#INFO-065) は中国AI投資の規模を示す。中国初の包括的AIエージェント規制が2027年70%採用を目標に発表された [INFO-037](../Information/2026-05-14/collected-raw.md#INFO-037) ことは、規制主導の市場形成を示唆する。

雇用面では6重のC蓄積が [H-CAR-001](../config/hypotheses.json) を支えている。Stanford研究が67%の初級開発者職の消滅を警告し [INFO-057](../Information/2026-05-14/collected-raw.md#INFO-057)、4月のAI関連レイオフは21,490件で全レイオフの25%以上を占める [INFO-041](../Information/2026-05-14/collected-raw.md#INFO-041)。WEFは92Mの雇用が2030年までに消滅すると予測する一方で、78%のAIプロジェクトが停滞/失敗している [INFO-059](../Information/2026-05-14/collected-raw.md#INFO-059)。KlarnaがAI代替後に人間再採用に転じた [INFO-056](../Information/2026-05-14/collected-raw.md#INFO-056) ことは、自動化の速度と方向性に不確定性があることを示す。AIエージェント成功率は77.3%に向上したが、74%がロールバックされている [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) という矛盾が、技術能力と運用実績の乖離を示している。

Q1 2026のAI資金調達は$2,555億に達し、2025年通年を超過した [INFO-049](../Information/2026-05-14/collected-raw.md#INFO-049)。Big 4ハイパースケーラーは合計$7,250億をAIインフラに投資している [INFO-050](../Information/2026-05-14/collected-raw.md#INFO-050)。この資本集中は围い込みの物理的基盤を強化する方向に働く。QHG象限の再定義が6R連続で未実行であり、SCN-002/003の区別能力低下が継続している。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | SCN-003 34% > SCN-002 32%。11R連続同一方向シフトでSCN-003が初めて最高確率に | 围い込み方向が開放方向を確率で上回る構造的転換点 | B-3 | scenarios.json |
| 高 | Pentagon SCR指定(米国企業初)+DPA脅迫+Google秘密契約受諾 vs Anthropic拒否 | 政府-AI関係の構造的再編。安全性姿勢が市場変数化。H-GOV-001の6重C蓄積 | B-2 | [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040) [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039) |
| 高 | MCPデファクト標準化加速(AAIF 97M SDK DL)+エンタープライズトークンコスト67%低下 | 技術面の開放圧力は継続。性能差の価値低下がエコシステム深度の価値を相対的に高める | B-3 | [INFO-021](../Information/2026-05-14/collected-raw.md#INFO-021) [INFO-042](../Information/2026-05-14/collected-raw.md#INFO-042) |
| 高 | GPT-Realtime 3モデル+Codex Windows sandbox+2ヶ月無料プロモ+DeployCo $4B+ | OpenAIの多面的围い込み(音声+コーディング+展開インフラ)が進行。H-OAI-001 C蓄積 | A-3 | [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) [INFO-078](../Information/2026-05-14/collected-raw.md#INFO-078) [INFO-072](../Information/2026-05-14/collected-raw.md#INFO-072) [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004) |
| 高 | Claude Mythos SWE-bench Multimodal 59%+Sandbox Runtime OSS+Agent SDK credit 6/15 | Anthropicの技術的優位性維持+安全性の開発者エコシステム統合。SCR/DPAの重大Iと拮抗 | B-3 | [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026) [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027) [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010) |
| 中 | TikTok MCP+DeerFlow OSS+Seedance 2.0 #2+CAPEX $30B(25%増)+Doubao全モダリティ | ByteDanceの多面的拡張。围い込みと開放の二面性。グローバル展開証拠は依然不在 | B-3 | [INFO-013](../Information/2026-05-14/collected-raw.md#INFO-013) [INFO-064](../Information/2026-05-14/collected-raw.md#INFO-064) [INFO-065](../Information/2026-05-14/collected-raw.md#INFO-065) [INFO-062](../Information/2026-05-14/collected-raw.md#INFO-062) |
| 中 | AIエージェント成功率77.3%だが74%ロールバック。78%のAIプロジェクトが停滞/失敗 | 技術能力と運用実績の乖離。エージェント本番到達率の低さが围い込みの実効性を制約 | B-3 | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-059](../Information/2026-05-14/collected-raw.md#INFO-059) |
| 中 | 67%初級開発者職消滅(Stanford)+21,490件/月AIレイオフ+Klarna逆転+WEF 92M | H-CAR-001の6重雇用削減C蓄積。方向性支持・速度不確定。Klarna逆転は速度のI | B-2 | [INFO-057](../Information/2026-05-14/collected-raw.md#INFO-057) [INFO-041](../Information/2026-05-14/collected-raw.md#INFO-041) [INFO-056](../Information/2026-05-14/collected-raw.md#INFO-056) [INFO-059](../Information/2026-05-14/collected-raw.md#INFO-059) |
| 中 | Q1 2026 AI資金調達$2,555億(2025年通年超過)+Big 4 $7,250億AIインフラ投資 | 資本集中が围い込みの物理的基盤を強化。性能差価値低下と資本集中の逆相関 | B-2 | [INFO-049](../Information/2026-05-14/collected-raw.md#INFO-049) [INFO-050](../Information/2026-05-14/collected-raw.md#INFO-050) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DeepSeek / ByteDance がグローバル展開でシェア10%以上を取り、米中AI市場の分断が解消される | 「3社だけが最先端」という構図と围い込み判断の双方が崩れる | 180日 | [IND-001](../config/indicators.json) |
| Agent Platformで3社以外(Mistral / Cohere等)が測定可能な10%以上のシェアを取る | 「Agent Platform三社鼎立」が崩れ、SCN-002の前提が弱まる | 180日 | [IND-027](../config/indicators.json) |
| QHG象限の再定義でSCN-002/003が統合または再区分される | 二重構造判断の軸自体が変わり、確率推移の連続性が失われる | 30日 | scenarios.json |
| Pentagon SCR指定が法的に無効化され、Anthropicの政府市場アクセスが回復する | H-GOV-001の萎縮効果前提が崩れ、安全性姿勢の市場変数化が後退する | 180日 | [IND-030](../config/indicators.json) |
| EU AI Act高リスク条項が完全に撤回される | 規制コンプライアンスを差別化要因にする安全性戦略の前提が崩れる | 180日 | [IND-030](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 63% | DeployCo $4B++Codex 4M WAU+Codex Windows sandbox+GPT-Realtime 3モデルのC蓄積。$14B損失とLLMシェア27%がI。確証バイアス警告3R連続。DeployCo収益・採用実績の独立確認不在 | [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004) [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) [INFO-072](../Information/2026-05-14/collected-raw.md#INFO-072) [INFO-078](../Information/2026-05-14/collected-raw.md#INFO-078) | [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 49% | MCPデファクト化7重I蓄積+Codex独自サンドボックスCの相殺。下層開放圧力が上位围い込み有効性を構造的に制約。49%はlow帯境界 | [INFO-078](../Information/2026-05-14/collected-raw.md#INFO-078) [INFO-072](../Information/2026-05-14/collected-raw.md#INFO-072) | [INFO-021](../Information/2026-05-14/collected-raw.md#INFO-021) [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 47% | Pentagon SCR+DPA+CTO不使用明言+Google秘密契約+抗議+Scale AI $5億の6重C蓄積。Anthropic提訴+Sanders法案は歯止めI。C/I均衡 | [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040) [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039) [INFO-038](../Information/2026-05-14/collected-raw.md#INFO-038) | [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040) [INFO-066](../Information/2026-05-14/collected-raw.md#INFO-066) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 24% | 6重雇用削減C蓄積(67%初級職消滅+21K/月レイオフ+WEF 92M+広告15%削減+テック93K+Klarna逆転)。77.3%成功率vs74%ロールバックの矛盾は速度のI。low範囲内 | [INFO-057](../Information/2026-05-14/collected-raw.md#INFO-057) [INFO-041](../Information/2026-05-14/collected-raw.md#INFO-041) [INFO-059](../Information/2026-05-14/collected-raw.md#INFO-059) | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-056](../Information/2026-05-14/collected-raw.md#INFO-056) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | GitHub Copilot 4.7M+75%+84%採用率の強力なC蓄積。67%初級職消滅は「書く能力」価値低下C。BLS職業分類未解決の時間減衰 | [INFO-058](../Information/2026-05-14/collected-raw.md#INFO-058) [INFO-057](../Information/2026-05-14/collected-raw.md#INFO-057) | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流・下流に集中する | 57% | SaaSpocalypse+23K削減+AI Capex増+パートナー非媒介化+エンタープライズメモリー堀+企業再構成の5重C蓄積。方向性支持。速度不確定。確証バイアス警告 | [INFO-059](../Information/2026-05-14/collected-raw.md#INFO-059) [INFO-041](../Information/2026-05-14/collected-raw.md#INFO-041) | (速度の不確定性) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で high | BenchLM上位差6-7pt。モデル間得意領域分化進行 [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) | 2026-05-14 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Claude Mythos cybersecurity step change [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026)。GPT-5.5-Cyber TAC [INFO-006](../Information/2026-05-14/collected-raw.md#INFO-006)。high水準 | 2026-05-14 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | 成功率77.3%だが74%ロールバック [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033)。78%プロジェクト停滞/失敗 [INFO-059](../Information/2026-05-14/collected-raw.md#INFO-059)。high水準 | 2026-05-14 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCPデファクト化+AAIF 97M SDK DL [INFO-021](../Information/2026-05-14/collected-raw.md#INFO-021)。Chrome DevTools MCP [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024)。high水準 | 2026-05-14 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Hassabis AGI 2030予測 [INFO-052](../Information/2026-05-14/collected-raw.md#INFO-052)。ARC-AGI-3 33%+ [INFO-051](../Information/2026-05-14/collected-raw.md#INFO-051)。elevated水準 | 2026-05-14 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | Q1 2026 $2,555億 [INFO-049](../Information/2026-05-14/collected-raw.md#INFO-049)+Big 4 $7,250億 [INFO-050](../Information/2026-05-14/collected-raw.md#INFO-050)+ByteDance $30B [INFO-065](../Information/2026-05-14/collected-raw.md#INFO-065)。high水準 | 2026-05-14 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で elevated | Pentagon SCR/DPA+Google秘密契約+EU延期+中国エージェント規制+Sanders法案。規制二方向深化 [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040) [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) [INFO-037](../Information/2026-05-14/collected-raw.md#INFO-037) [INFO-066](../Information/2026-05-14/collected-raw.md#INFO-066)。elevated水準 | 2026-05-14 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-14 | SCN-003が最高確率34%に順位変動・Pentagon SCR/DPA・GPT-Realtime 3モデル・TikTok MCP・DeerFlow OSSを反映して全面書き直し | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) [INFO-011](../Information/2026-05-14/collected-raw.md#INFO-011) [INFO-012](../Information/2026-05-14/collected-raw.md#INFO-012) | 「性能均質化と围い込みの二重構造」→「SCN-003が最高確率に。Pentagon圧力で政府-AI関係が構造的再編。Google受諾vs Anthropic拒否の分化が鮮明」 |
| 2026-05-12 | DeployCo設立・SCN-002/003同率33%・AI Search围い込み・GTIGゼロデイを反映 | [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-12/collected-raw.md#INFO-006) | SCN-002 34→33%・SCN-003 32→33%。同率でQHG軸区別能力消失 |
| 2026-05-12 | Azure排他性終了・OSSギャップ消滅・围い込み7重C蓄積・SCN-002/003差2%・雇用二極化を反映して全面書き直し | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) | SCN-002 37→34%・SCN-003 29→32%。差2%に縮小 |
| 2026-05-07 | Static v2構造に全面移行 | STATIC_INTELLIGENCE_v2.md 仕様適用 | 旧: 逐次トピック羅列 → 新: §0〜§7 + プレイヤー表 |
| 2026-05-06 | JV/FDE同時採用・Agent Platform三社鼎立・围い込みシグナル4重蓄積を反映 | [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) | SCN-002 44→38%・SCN-003 24→28% |

---

## 7. ブラインドスポット

- 中国市場の実態が追跡できていない。ByteDance / DeepSeek のグローバルシェアと日本・欧州での浸透状況は、5社テーブルに組み込む観測指標を持っていない。ByteDance CAPEX $30B+DeerFlow OSS+TikTok MCPは観測できたが、グローバル展開の実効性までは見えていない。
- QHG象限の再定義が6R連続で未実行。SCN-002/003の差が2%に縮小し、区別能力が消失している。次回Arbiterでの再定義が必須。
- Pentagon SCR/DPAの因果チェーンが「未確認」継続。政府介入が安全性抑圧なのか安全保障要件なのかの区別が、[H-GOV-001](../config/hypotheses.json) の評価精度を左右する。Anthropic提訴の結果が分岐点になる。
- DeployCo $4B+の実質額(コミットメント vs 実調達)・パートナー排他性・FDE稼働率が未確認。全証拠がA-3(公式発表)でB-tier以上独立確認0件の分析方法論的限界。
- 2nd tier プレイヤーの動向を5社比較に入れていない。Mistral / Cohere の技術力・シェア・資金調達状況は、Agent Platform三社鼎立が本当に「鼎立」かを検証するために必要だが、評価できていない。
- 個人開発者(vs エンタープライズ)のツール選好変化を観測できていない。Claude Code・Copilot・Cursor間のシェア推移は、エコシステム围い込みの実効性を判断する重要指標だが、定量データが構造的に取れていない。
- AIエージェント成功率77.3%と74%ロールバックの矛盾が解消されていない。技術能力の向上が運用実績に直結していない原因(品質・ガバナンス・コスト・信頼)の特定が、エージェント本番到達率の予測に不可欠だが未分析。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) | GPT-Realtime-2/Translate/Whisper 3モデルリリース |
| [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004) | DeployCo設立($4B+・Tomoro買収・19パートナー) |
| [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) | ChatGPT広告日本/UK/Korea等展開 |
| [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010) | Agent SDK credit 6/15開始 |
| [INFO-012](../Information/2026-05-14/collected-raw.md#INFO-012) | Grok 5製品連続リリース・マルチエージェントリサーチ |
| [INFO-013](../Information/2026-05-14/collected-raw.md#INFO-013) | TikTok MCP Server・OpenClaw収益化 |
| [INFO-021](../Information/2026-05-14/collected-raw.md#INFO-021) | MCPデファクト標準化(AAIF 97M SDK DL) |
| [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) | AndroidエージェントAI・Gemini Omniリーク・Sora 2終了 |
| [INFO-024](../Information/2026-05-14/collected-raw.md#INFO-024) | Chrome DevTools MCP |
| [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026) | Claude Mythos SWE-bench Multimodal 59% |
| [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027) | Sandbox Runtime OSS |
| [INFO-028](../Information/2026-05-14/collected-raw.md#INFO-028) | Gemini CLI extensions(Firebase/DevOps) |
| [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) | AIエージェント成功率77.3%・74%ロールバック |
| [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) | EU AI Act高リスク期限延期 |
| [INFO-037](../Information/2026-05-14/collected-raw.md#INFO-037) | 中国初のAIエージェント規制(70%採用2027) |
| [INFO-038](../Information/2026-05-14/collected-raw.md#INFO-038) | Pentagon Scale AI $500M(5倍増)・Meta 49%出資 |
| [INFO-039](../Information/2026-05-14/collected-raw.md#INFO-039) | Pentagon CTO Anthropic不使用・Google秘密契約 |
| [INFO-040](../Information/2026-05-14/collected-raw.md#INFO-040) | Anthropic SCR指定(米国企業初) |
| [INFO-041](../Information/2026-05-14/collected-raw.md#INFO-041) | AI関連レイオフ21,490件/月(25%+) |
| [INFO-042](../Information/2026-05-14/collected-raw.md#INFO-042) | エンタープライズトークンコスト67%低下 |
| [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) | Fine-tuning API段階的縮小 |
| [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) | モデル間得意領域分化(Gemini 94.3% vs GPT-5.5 93.6%) |
| [INFO-049](../Information/2026-05-14/collected-raw.md#INFO-049) | Q1 2026 AI資金調達$2,555億(2025年通年超過) |
| [INFO-050](../Information/2026-05-14/collected-raw.md#INFO-050) | Big 4ハイパースケーラー$7,250億AIインフラ投資 |
| [INFO-057](../Information/2026-05-14/collected-raw.md#INFO-057) | 67%初級開発者職消滅(Stanford) |
| [INFO-058](../Information/2026-05-14/collected-raw.md#INFO-058) | GitHub Copilot 4.7M+75%+84%採用率 |
| [INFO-059](../Information/2026-05-14/collected-raw.md#INFO-059) | WEF 92%投資・78%プロジェクト停滞/失敗 |
| [INFO-062](../Information/2026-05-14/collected-raw.md#INFO-062) | Doubao全モダリティ対応 |
| [INFO-064](../Information/2026-05-14/collected-raw.md#INFO-064) | Seedance 2.0 Video Arena世界#2 |
| [INFO-065](../Information/2026-05-14/collected-raw.md#INFO-065) | ByteDance CAPEX $30B(25%増) |
| [INFO-066](../Information/2026-05-14/collected-raw.md#INFO-066) | トランプ・習近平首脳会談AI協議・Sanders超知能禁止条約 |
| [INFO-072](../Information/2026-05-14/collected-raw.md#INFO-072) | Codex 2ヶ月無料エンタープライズプロモーション |
| [INFO-078](../Information/2026-05-14/collected-raw.md#INFO-078) | Codex Windows sandbox |
| [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) | DeployCo設立($4B+・Tomoro買収・19パートナー) |
| [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) | Azure排他性終了・GPT-5.5 on AWS Bedrock |
| [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) | OSS/クローズド性能ギャップほぼ消滅 |
| [Arbiter v3.77](../state/arbiter-2026-05-14.md) | 確度評価の完全根拠(付録のみ参照) |
