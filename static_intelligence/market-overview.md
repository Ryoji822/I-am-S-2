# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-06-23
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。Y軸「フロンティア差別化の持続性」の完全な定量評価基準は未設定。H-GOV-001/(002)分割実行済み。(a)Anthropic固有政府介入54% medium（2R連続-1%）・(b)業界全体萎縮効果はH-GOV-002 21% low。H-OAI-001 49% medium（ペナルティ停止）。SCN-002(31%)が単独首位（SCN-004 30%・SCN-003 23%・SCN-001 16%）。H-BTD-002操作化再定義実行済み。H-CAR-002ステートメント修正実行済み。IND-030 critical維持（Operation Epic Fury複数独立再確認・DPA検討・中国AIレイオフ違法化）。Arbiter v4.17 DEGRADED 2R連続。品質チェックPASS
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-06-23時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|:-:|:-:|---|
| Anthropic | Claude Fable 5, Mythos 5, Opus 4.7, Claude Code | ARR $470億 [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011)(C-2)・$1Tセカンダリ市場評価 [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066)(B-2)・Google最大$40B投資 [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045)(B-2) | FrontierCode首位 | Jumper（ノーベル賞）がDeepMindから移籍 [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066)。判事Rita Lin「違法な報復」判断で連邦禁止阻止。Fable 5/Mythos 5アクセス停止中。秋IPO予定。H-ANT-001 37% low・H-ANT-002 62% medium・H-GOV-001 54% medium |
| OpenAI | GPT-5.5, Codex, Skills Beta | Q1収益$5.7B(3倍成長)・IPO評価額最大$1T [INFO-050](../Information/2026-06-21/collected-raw.md#INFO-050)(B-2) | ARC-AGI 2首位(85%) | ChatGPTシェア初の50%割れ。Pentagon GenAI.mil 300万人。IPO Q4 2026目標。H-OAI-001 49% medium（ペナルティ停止） |
| Google | Gemini 3.5 Flash, Omni, Spark, DiffusionGemma | Cloud $4,600億バックログ・63%成長・Anthropic最大$40B投資 [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045)(B-2) | LMArena Elo首位 | DeepMind AI Control Roadmap。Jumper流出 [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066)。安全チーム離職。NSF基礎科学20-30%削減。H-GOO-001 50% low・H-GOO-003 48% medium |
| SpaceXAI | Grok 4.3, Grok Build, Grok Gov Model | $20B Series E・Cursor $60B買収 | 4位 | Grok Gov Model Operation Epic Fury 96h/2,000標的（複数独立再確認）。DoD CDAO宣誓陳述書「独自機能」。Gillibrand法案。H-XAI-002 59% medium・H-XAI-004 57% medium |
| ByteDance | 豆包2.0, Coze 3.0, Seedance 2.0 mini | CAPEX 2000億元 | 非公開 | Seedance 2.0 mini品質A-2。DAU 2億超・Freemium+ECシナジーモデル（EC収益化81.1%）。H-BTD-001 64% medium・H-BTD-002 44% low |

---

## 0. 一文要約

SCN-002「技術は開くが勝者は出る」が31%に上昇しSCN-004「誰でもAI」(30%)を1ポイント差で抑えて単独首位になった [scenarios.json](../config/scenarios.json)。SCN-001「監視資本主義围い込み」が17%から16%に-1%低下した。プロトコル開放の臨界点通過（5件A-2/A-3品質開放証拠同一ラウンド）が围い込み戦略の技術的前提を構造的に侵食した。SCN-003は23%維持、SCN-004は30%維持。

本ラウンドの構造的変化はGoogle最大$40B Anthropic投資報道 [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045)（B-2）とAnthropic $1Tセカンダリ+Jumper移籍 [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066)（B-2）である。Google自身がGeminiを展開する中で競合に最大$40Bを投じることは、AI市場の競争構造の転換を示唆する。ノーベル賞受賞者JumperのDeepMind流出は、人材流動が新次元に入ったことを示す。SpaceX Cursor $60B買収 [INFO-044](../Information/2026-06-23/collected-raw.md#INFO-044)（A-1）と合わせ、資本集中が加速している [IND-029](../config/indicators.json)。

[H-GOV-001](../config/hypotheses.json) は56%から54%に2R連続-1%。介入能力の拡大（DPA検討・8社開放・サプライチェーンリスク）はC蓄積だが、Google $40B投資・$1T評価+Jumper流入・研究者非難の三重Iが先例確立核心要件（持続性・合法性）を三重に挑戦。[H-ANT-002](../config/hypotheses.json) は64%から62%に2R連続-1%。Claude Code DAU/日常利用者データ4R連続不在。Arbiter v4.17はDEGRADED状態（Red Agent失敗2R連続）。

---

## 1. コア判断

v4.13の最重要変化はSCN-002/003順位逆転である。SCN-002が28%（+1%）に上昇し、SCN-003が25%（-2%）に低下した。06-14の同率27%（v4.12）から分化した構造的変化だ。SCN-002上昇は、Anthropicの収益逆転 [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) とClaude Code採用急増 [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) が「開放標準上での差別化持続」を支持したため。SCN-003低下は、Jevons paradox [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) がコモディティ化圧力（差別化消失＝SCN-004方向）として作用し、「静かな囲い込み」の説明力が低下したため。

H-OAI-001 50%（-1%）は17R連続 I>Cペナルティの継続。Anthropic ARR $470億 vs OpenAI $330億の収益逆転 [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) がI（不一致）方向の最強力な定量証拠。但し、Arbiterは3つの留保をつけた。第一にゼロサム仮定の未検証（拡大市場で両社成長可能）。第二にJevons paradoxの二面性（コモディティ化圧力＝Iだが、コスト優位企業の支配強化＝Cの代替解釈も可能）。第三に「B2B支配」の定義未解決（収益・シェア・デプロイ数のいずれで測るか）。

H-GOV-001/(002)分割が確定した。(a)Anthropic固有政府介入は57% medium（Pentagon GenAI.mil [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) で政府チャネル獲得がC蓄積）。(b)業界全体萎縮効果は21% low（核心証拠不在継続・他社安全性方針の定量変化データ不在）。H-ANT-002は65%（+1%）に上昇。Claude Code採用3%→24% [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) が開発者エコシステムでの急成長を確認した。H-GOO-001は49%（+2%）に上昇。Gemini 3.1 Pro動画推論55.63%・ARC-AGI-3改善でC蓄積だが、代替説明（業界全体成長）は19R+未解決。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | SCN-002(28%)がSCN-003(25%)を逆転。06-14同率27%から分化 | 構造的順位変更。収益逆転+Claude Code採用が開放x差別化支持。Jevons paradoxが囲い込み否定 | Arbiter | [SCN-002](../config/scenarios.json) [SCN-003](../config/scenarios.json) |
| 高 | Anthropic ARR $470億 vs OpenAI $330億。12カ月未満で逆転。最大10社中8社がAnthropic有料顧客 | H-OAI-001のI。SCN-002支持。ゼロサム仮定未検証（拡大市場で両社成長可能） | C-2 | [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) |
| 高 | Jevons paradox: トークン90%安価化で使用量倍増。業界全体現象 | SCN-004支持の最強力定量証拠。H-OAI-001二面性（コモディティ化I vs predatory pricing C）。SCN-003押し下げ | A-2 | [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) |
| 高 | Claude Code採用 3%→24%（米国）。JetBrains 1万人調査 | H-ANT-002のC。開発者エコシステムでのAnthropic追い上げ第三者定量証拠。SCN-002支持 | B-3 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) |
| 高 | Pentagon GenAI.mil 2026年7月上旬提供予定・職員最大300万人 | H-GOV-001(a)のC。順応報酬構造参加。政府系B2Bチャネル獲得 | C-3 | [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) |
| 高 | H-GOV-001/(002)分割確定。(a)57% medium・(b)21% low | 核心命題（業界全体萎縮）の証拠不在が制度化。Anthropic固有圧力は観測されるが波及効果は未証明 | Arbiter | [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) |
| 高 | H-OAI-001 50%（medium帯中央）。17R連続 I>Cペナルティ | ゼロサム仮定未検証・predatory pricing代替解釈・「B2B支配」定義未解決の3留保 | Arbiter | [H-OAI-001](../config/hypotheses.json) |
| 高 | DeepSeek V4 Pro > GPT-5.5 Pro 精度・コスト1/5 | SCN-004首位の最強力な定量裏付け。フロンティア差別化消失の決定的証拠 | B-3 | [INFO-042](../Information/2026-06-14/collected-raw.md#INFO-042) |
| 高 | OSS 3モデルGPT-4超え | SCN-004直接支持。OSS性能ギャップ消滅方向 | B-3 | [INFO-043](../Information/2026-06-14/collected-raw.md#INFO-043) |
| 高 | OpenAI大幅値下げ検討・MMLU/ARC-AGI-2飽和 | パターンNN直接根拠。価格決定力低下と性能差消失の同時進行 | B-3 | [INFO-061](../Information/2026-06-14/collected-raw.md#INFO-061) [INFO-036](../Information/2026-06-14/collected-raw.md#INFO-036) |
| 高 | 政府がFable 5/Mythos 5全外国人アクセス停止 | 囲い込みの新次元。但しAnthropic1社限定。H-GOV-001(a)のC | A-3 | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) |
| 高 | Google Cloud 63%成長$460Bバックログ | SCN-003資本集中C蓄積。但し代替説明（業界全体成長）未解決 | C-3 | [INFO-051](../Information/2026-06-14/collected-raw.md#INFO-051) |
| 高 | OpenAI S-1提出・Phase 3宣言・Ona買収 | OpenAI構造的変化の多面的確認。パターンPP前提条件充足 | A-3 | [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001) |
| 高 | 5社スキルマーケットプレイス同時構築 | パターンMM直接根拠。囲い込みと標準化の同時進行 | A-3 | [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) [INFO-049](../Information/2026-06-12/collected-raw.md#INFO-049) |
| 高 | MCP RC公開・AAIF振り返り・Gemini Skills OSS | SCN-002開放支持の4重C蓄積。標準化の制度化確定 | B-3 | [INFO-014](../Information/2026-06-14/collected-raw.md#INFO-014) [INFO-015](../Information/2026-06-14/collected-raw.md#INFO-015) [INFO-020](../Information/2026-06-14/collected-raw.md#INFO-020) |
| 高 | Grok軍事展開96h/2,000目標/2,000発弾薬 | IND-030 high/rising直接根拠。能力-リスク二面性極大化 | B-2 | [INFO-008](../Information/2026-06-19/collected-raw.md#INFO-008) |
| 高 | AIレイオフブーメラン効果・41%管理層削減 | パターンQQ直接根拠。H-CAR-001因果ギャップ関連 | B-3 | [INFO-026](../Information/2026-06-12/collected-raw.md#INFO-026) [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) |
| 中 | BCG「大半がAI投資から意味ある収益未達」 | IND-026 highのI方向。期待-実態ギャップ定量確認 | B-3 | [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) |
| 中 | Gartner 40%エンタープライズエージェント・McKinsey 62%試験中 | IND-026 highのC方向。採用率急速拡大の定量確認 | B-3 | [INFO-025](../Information/2026-06-12/collected-raw.md#INFO-025) [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) |
| 中 | AIベンダーロックイン「推論の暗黙知」・スイッチングコスト | SCN-003支持要因。パターンMM囲い込み圧力の補強 | C-3 | [INFO-031](../Information/2026-06-12/collected-raw.md#INFO-031) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | パターンNN「不可逆的加速」判断が崩れ、SCN-004の前提が弱体化する | 180日 | [IND-025](../config/indicators.json) |
| 5社スキルマーケットプレイスがMCP/AAIF標準に完全移行する | パターンMM囲い込み圧力が否定され、SCN-004支持に転じる | 180日 | [IND-027](../config/indicators.json) |
| OpenAI IPO後に安全性投資比率が維持または増加する | パターンPP「利益圧力が安全性圧縮」前提が崩れる | 365日 | [IND-030](../config/indicators.json) |
| AIレイオフブーメラン効果が広範に確認され、再雇用が加速する | パターンQQ確度上昇。H-CAR-001の因果ギャップが「AI不可逆」前提を弱める | 180日 | [H-CAR-001](../config/hypotheses.json) |
| Google围い込み蓄積が止まり、開放C証拠が5件以上に拡大する | H-GOO-002の上方修正根拠。現在開放C 3件 | 180日 | [IND-027](../config/indicators.json) |
| 豆包が有料化を撤回し無料低価格戦略に復帰する | H-BTD-002 low深化前提の再検証 | 180日 | [H-BTD-002](../config/hypotheses.json) |
| Google固有寄与の定量分解が成功し、AWS/Azure成長率を上回る | H-GOO-001 low→medium復帰条件充足。KIQ-GOO-001 | 次回 | [H-GOO-001](../config/hypotheses.json) |
| Anthropic安全性第1位選択理由のA-2品質定量確認 | H-ANT-001 上限条件充足。再定式化後の新上限条件達成検討 | 次回 | [H-ANT-001](../config/hypotheses.json) |
| RSI「ほぼ超人」の外部検証が失敗する | IND-028 high移行の根拠が弱体化。elevatedへの再下方検討 | 90日 | [IND-028](../config/indicators.json) |
| Y軸定量評価基準が設定されない（次回） | シナリオ確率修正の精度が制限される。方向圧力評価のみで絶対位置評価なし | 次回 | [scenarios.json](../config/scenarios.json) |
| AIベンチマーク飽和で新ベンチマークが性能差を再現する | SCN-004前提の「差別化消失」が弱まり、SCN-002/003支持に転じる | 180日 | [IND-028](../config/indicators.json) |
| Anthropic ARRが$200億以上のリードを90日間維持する | 収益逆転が一時的でなく構造的と判定され、H-OAI-001下方圧力確定 | 90日 | [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgent機能でB2B市場の支配的地位を確立する | 49% medium | ±0%。ペナルティ機構一時停止継続。Q1収益$5.7B 3倍成長・IPO $1TがC。ChatGPT 50%割れがI。ゼロサム仮定未検証・KIQ-OAI-001（収益内訳）未回答 | [INFO-045](../Information/2026-06-21/collected-raw.md#INFO-045) [INFO-050](../Information/2026-06-21/collected-raw.md#INFO-050) [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) | [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放上にプロプライエタリ上位レイヤーで围い込む | 44% low | 围い込み否定累積継続。Partner Network・Apps SDK MCP統合の排他性なし | [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) [INFO-019](../Information/2026-06-19/collected-raw.md#INFO-019) | (围い込み肯定C不在) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とする | 3% low | 商業化規模圧倒的。AGI最優先支持A-2+証拠不在 | [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) |
| [H-GOV-001](../config/hypotheses.json) | 政府がAnthropicの安全性姿勢に圧力をかける先例が確立された | 54% medium | -2%（56→54%・2R連続-1%）。介入ツール拡大（DPA検討・8社開放）はC蓄積だがGoogle $40B投資・$1T評価+Jumper流入・研究者非難の三重Iが核心要件を三重に挑戦。介入能力拡大と介入効果不在の不均衡2R連続拡大 | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) [INFO-031](../Information/2026-06-23/collected-raw.md#INFO-031) [INFO-029](../Information/2026-06-23/collected-raw.md#INFO-029) | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| [H-GOV-002](../config/hypotheses.json) | 政府のAnthropic圧力がAI業界全体に波及し萎縮効果が生じる | 21% low | ±0%。核心命題（業界全体萎縮効果）証拠不在。他社安全性方針定量変化データ不在20R連続。NSF予算削減は文脈証拠。棄却候補 | (業界全体波及証拠不在) | [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicの安全性はKano「魅力的品質」→「当たり前品質」移行過程 | 37% low | Kano再定式化後。「差別化次元の変化」採用。37%の固定はアンカリング。中期検証不可能性明記 | [INFO-001](../Information/2026-06-15/collected-raw.md#INFO-001) [INFO-038](../Information/2026-06-14/collected-raw.md#INFO-038) | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-022](../Information/2026-06-12/collected-raw.md#INFO-022) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステム標準ツールになる | 62% medium | -2%（64→62%・2R連続-1%）。Claude Code採用24%のC蓄積継続だがDAU/日常利用者データ4R連続不在（v4.16条件到達）。medium→low移行検討起動・DEGRADED制約でラベル変更保留。Fable 5 #1・Opus 4.8 SWE-bench #1技術リーダーシップに依存 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006) | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-040](../Information/2026-06-12/collected-raw.md#INFO-040) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持し全クラウド同等機能を提供する | 6% low | マルチクラウド均衡証拠不在。Google $40B投資でインフラ二重集中更に加速。棄却候補維持 | [INFO-032](../Information/2026-06-12/collected-raw.md#INFO-032) | (マルチクラウド均衡証拠不在) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合でデータ優位を活かしシェアを拡大する | 50% low | +1%（49→50%）。7件多面的C蓄積。Forrester「Google > OpenAI」代理店逆転B-2。$40B投資。広告領域でのみ部分充足。low維持（DEGRADED制約・A-2+条件未達成） | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-037](../Information/2026-06-23/collected-raw.md#INFO-037) [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055) | (代替説明未解決19R+) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準Day 0サポートを維持し围い込みを回避する | 23% low | Skill Registry围い込みI蓄積。MCP RC開放C。围い込みI 33件 vs 開放C 3件。蓄積速度比11:1 | [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036) | [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーで競争力を維持する | 48% medium | ±0%。AI Control Roadmap・AGI→ASI論文・Boston Dynamics提携C蓄積。Jumper流出はI方向。A-2+条件未達成。48%境界維持 | [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) [INFO-072](../Information/2026-06-16/collected-raw.md#INFO-072) [INFO-046](../Information/2026-06-16/collected-raw.md#INFO-046) | [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 59% medium | ±0%。DeepSeek V4 Pro既織り込み済み。Grok Build Marketplace C。価格コモディティ化で独自性希薄化リスク | [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) | (価格コモディティ化) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 57% medium | +2%（55→57%・2R連続+1%）。SpaceX Cursor $60B買収は本ラウンド最高品質証拠A-1。コーディング+軍事+インフラ垂直統合完了。確証バイアス警告(availability≠adoption)継続 | [INFO-044](../Information/2026-06-23/collected-raw.md#INFO-044) [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceは中国市場規模を足がかりにグローバル展開する | 64% medium | ±0%。Coze 2.5 Agent World・2000億元投資上方修正C。ミラーイメージングリスク継続 | [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) | (グローバル展開証拠限定的) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包でFreemium + ECシナジーモデルを維持する | 44% low | ±0%。EC収益化81.1%はC証拠へ再分類。DAU 2億超の無料層獲得→EC・広告・抖音クロス収益化。日収入vs日コストの構造的ギャップはIとして残存 | (Freemium+ECシナジー維持) | [INFO-013](../Information/2026-06-20/collected-raw.md#INFO-013) [INFO-108](../Information/2026-06-20/collected-raw.md#INFO-108) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% medium | ±0%。著作権関連新規なし。Coze 2.5・DeerFlow 2.0はグローバル展開能力Cだが中国市場中心 | [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) | (著作権新規なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 36% low | ±0%。因果ギャップ未解決。「79%導入」≠「30%自動化達成」 | [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034) | [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) [INFO-026](../Information/2026-06-12/collected-raw.md#INFO-026) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が変容し「設計・評価・方向付けする能力」の価値が上昇する | 70% medium | ±0%。ステートメント修正実行済み。METR 43%本番破損・ALE完遂<5%が上限制約として継続 | [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034) | (METR 43%本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 58% medium | +1%（57→58%）。4件直接C蓄積（スマイル曲線再形成・AaaS/SaaS置換・代理店変容B-2 Forrester・Next Gen Agency生存）。方向性支持・速度不確定 | [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Daybreak Security・GPT-5.5-Cyber・Codex Security=防御側強化。新規A-2実被害なし。high/rising | 2026-06-23 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満で high | Gemini 3 Pro Deep Thinkマルチモーダル#1・Seedance 2.0 4モダリティ同時入力。量的向上継続・真の理解未解決。elevated/stable | 2026-06-23 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | ALE完遂<2.5%・成功率10%・Klarna $40B損失・72%/60%ガバナンス格差。7+独立ソースで期待-実態ギャップ確定的。high/rising | 2026-06-23 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用で high | Interactions API GA・Agent Skills生態系・Antigravityクロス互換・NVIDIA OpenShell・AgentPerf。標準化臨界点通過。high/rising | 2026-06-23 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大で high | Anthropic AI 80%内部コード寄与=RSI具体化・CEO3氏AGI 5-10年合意・Jumper移籍・LeCun AMI Labs。RSI具体化とベンチマーク限界同時進行。high/rising | 2026-06-23 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限り high | SpaceX Cursor $60B・Google $40B投資・xAI $20B・OpenAI Q1 $5.7B/$3.7Bバーン・Anthropic $1T。資本流入加速・物理的制約ギャップ確定的。high/rising | 2026-06-23 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。Operation Epic Fury複数独立再確認(96h/2,000標的)・DPA行使検討・中国AIレイオフ違法化。条件2（A-2技術的安全事故）未到達。判事Rita Lin判断・Gillibrand法案・DeepMind AI Control Roadmapは緩和要因 | 2026-06-23 |

---

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-23 | 全面書き直し（§0・§4・§5・プレイヤースナップショット・ヘッダー）。Google最大$40B Anthropic投資報道（[INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) B-2）・$1Tセカンダリ+Jumper移籍（[INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) B-2）を反映。[H-GOV-001](../config/hypotheses.json) 56→54%（2R連続-1%）。[H-ANT-002](../config/hypotheses.json) 64→62%（DAU 4R不在）。[H-GOO-001](../config/hypotheses.json) 49→50%。[H-XAI-004](../config/hypotheses.json) 55→57%。[H-CAR-003](../config/hypotheses.json) 57→58%。SCN-001 17→16%・SCN-002 30→31%（単独首位）。全§5最終確認日更新。DEGRADED 2R連続 | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) [INFO-044](../Information/2026-06-23/collected-raw.md#INFO-044) | SCN-001 17→16%・SCN-002 30→31%・H-GOV-001 56→54%・H-ANT-002 64→62%・H-GOO-001 49→50%・H-XAI-004 55→57%・H-CAR-003 57→58% |
| 2026-06-21 | 全面書き直し（§0・§1・§2・§4・§5・プレイヤースナップショット）。[IND-030](../config/indicators.json) high→critical移行。SCN-002 29→30%(+1%)・SCN-003 24→23%(-1%)・SCN-002とSCN-004が同率30%首位。[H-GOV-001](../config/hypotheses.json) 58→56%（判事Rita Lin A-2）。[H-ANT-002](../config/hypotheses.json) 65→64%。[H-OAI-001](../config/hypotheses.json) 49% ±0%（ペナルティ停止）。DeepMind AI Control Roadmap(A-1)・輸出管理全容(A-1)・IPO $1T・ChatGPT 50%割れを反映 | [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) [INFO-050](../Information/2026-06-21/collected-raw.md#INFO-050) [INFO-045](../Information/2026-06-21/collected-raw.md#INFO-045) | SCN-002 29→30%・SCN-003 24→23%・H-GOV-001 58→56%・H-ANT-002 65→64%·H-OAI-001 49%（ペナルティ停止）・IND-030 critical |
| 2026-06-20 | ターゲット編集。H-BTD-002操作化再定義・H-CAR-002ステートメント修正・プレイヤースナップショットByteDance行更新・H-OAI-001 50→49%・H-GOV-001 57→58%・IND-030 critical移行条件見直し（累積トリガー追加）・全§5最終確認日更新。§0/§1/§2/§3叙述はv4.13ラウンド記述のため維持 | [arbiter-2026-06-20](../state/arbiter-2026-06-20.md) | H-OAI-001 50→49%・H-GOV-001 57→58%・H-BTD-002 ステートメント修正・H-CAR-002 ステートメント修正・IND-030 条件見直し |
| 2026-06-19 | §0〜§5・プレイヤースナップショット・付録を全面書き直し。SCN-002(28%)がSCN-003(25%)を逆転（順位変更）。H-OAI-001 51→50%・H-GOV-001/(002)分割値更新(57% medium/21% low)・H-ANT-002 64→65%・H-GOO-001 47→49%・H-BTD-002 45→44%・H-CAR-002 69→70%。Anthropic ARR $470億 vs OpenAI $330億収益逆転・Jevons paradox・Pentagon GenAI.mil・Claude Code採用24%を反映 | [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) | SCN-001 16→17%・SCN-002 27→28%・SCN-003 27→25%・SCN-004 30%維持・H-OAI-001 51→50%・H-GOV-001 39→57%(分割)・H-ANT-002 64→65%・H-GOO-001 47→49% |
| 2026-06-14 | QHG 41R凍結打破。SCN-001 -1%(17→16%)・SCN-002 +1%(24→25%)・SCN-003 -1%(29→28%)・SCN-004 +1%(30→31%)。H-OAI-001 56→54%・H-ANT-001 38→37%・H-GOV-001 41→40%・H-BTD-002 46→45% | [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) [INFO-042](../Information/2026-06-14/collected-raw.md#INFO-042) [INFO-043](../Information/2026-06-14/collected-raw.md#INFO-043) [INFO-061](../Information/2026-06-14/collected-raw.md#INFO-061) | SCN-001 17→16%・SCN-002 24→25%・SCN-003 29→28%・SCN-004 30→31%・H-OAI-001 56→54% |
| 2026-06-12 | §0-§2・§4・§5・プレイヤースナップショット・付録を全面書き直し。SCN-004がSCN-003を抜いて首位（30%）・H-GOO-001 medium→low・価格コモディティ化加速・エコシステム囲い込み同時創発を反映 | [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) | SCN-003 32→29%（首位陥落）・SCN-004 27→30%（首位奪取）・H-GOO-001 51→47% medium→low |
| 2026-06-07 | IND-028 elevated→high(RSI「ほぼ超人」A-1)・H-CAR-001 34→35%・H-GOV-001 45%±0%・SCN-003 33→32%・SCN-004 26→27%・品質調整Red Agent採用率75%到達を反映して全面書き直し | [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) [INFO-016](../Information/2026-06-07/collected-raw.md#INFO-016) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) | IND-028 elevated→high・H-CAR-001 34→35%・SCN-003 33→32%・SCN-004 26→27% |
| 2026-06-04 | H-GOV-001 48→45%(停止条件宣言)・H-GOO-002 29→25%(围い込み19件)・H-BTD-002 51→49%(low移行)・Trump大統領令・142K解雇・S-1機密提出を反映して全面書き直し | [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) | H-GOV-001 48→45%・H-GOO-002 29→25%・H-BTD-002 51→49%・SCN-002 25→24%・SCN-004 25→26% |
| 2026-05-31 | Arbiter v3.94完了反映。SCN-004 tied SCN-002(25%)順位逆転。H-GOV-001 -2%・H-ANT-001 -2%・H-OAI-001 -2%を反映して全面書き直し | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) | SCN-002 27→25%・SCN-003 37→35%・SCN-004 21→25% |

---

## 7. ブラインドスポット

- [H-OAI-001](../config/hypotheses.json) 50%（medium帯中央）の3つの未解決問題。第一にゼロサム仮定の未検証（AI市場が拡大市場の場合、Anthropic成功≠OpenAI劣位）。第二にJevons paradoxの二面性（コモディティ化圧力=Iだが、コスト優位企業の支配強化=Cの代替解釈）。第三に「B2B支配」の定義未解決（収益・シェア・デプロイ数のいずれか）。17R連続 I>Cペナルティの過大評価リスク。
- SCN-002/003順位逆転の安定性が未検証。06-14同率27%から1週間で3ポイント差に開いたが、単一証拠（Anthropic ARR逆転）への依存度が高い。Anthropic ARRが一時的急成長の場合、SCN-002上昇は反転する。
- [H-GOV-001](../config/hypotheses.json) / [H-GOV-002](../config/hypotheses.json) 分割後の(b)業界全体萎縮効果の証拠不在が制度化された。(a)Anthropic固有圧力は57% mediumで確度高いが、他社（Google・OpenAI・Meta）への波及効果の定量データが不在。(b)は棄却候補。
- [H-GOO-001](../config/hypotheses.json) 49% low。19R+代替説明「業界全体押し上げ」未解決。KIQ-GOO-001（AWS/Azure同時期成長率比較データ）が充足されない限りlow維持。+2%上昇したがband変更なし。
- パターンNN「価格コモディティ化の不可逆的加速」の品質はB-3/C-3中心。高品質（A-1/A-2）での価格反転確認または否定が未実施。Jevons paradox(INFO-058 A-2)が品質向上に寄与したが、 predatory pricing代替解釈との判別が不能。
- Y軸「フロンティア差別化の持続性」の完全な定量評価基準は未設定。毎R方向圧力評価に基づく修正が標準プロセス化したが、Y軸上の定量位置評価基準の策定は次回に継続。
- [H-ANT-001](../config/hypotheses.json) Kano再定式化後の上限条件未達成継続。37%の長期固定はアンカリングの制度化。中期検証可能性の欠如が構造的に組み込まれた。
- OpenAI S-1内容・Anthropic IPO詳細が非公開。収益内訳（API/Enterprise/Consumer）の時系列データがH-OAI-001確度変更の鍵だが入手不能。
- AIレイオフ因果帰属の自己申告バイアス。AIが真の原因か口実かの判別不能。パターンQQ「ブーメラン効果」の確度中は限定的証拠に基づく。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral等の台頭は「5社フレーム」自体の妥当性を問う結果。
- IND-030 critical移行見送り継続の妥当性。Grok軍事展開（96h/2,000弾薬）は「設計通りの軍事利用」と「技術的安全事故」の区別に基づくが、Gillibrand法案進捗がcritical移行の关键変数。民間被害データ不在は正常性バイアス逆方向リスク。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) | OpenAI Partner Network立ち上げ・$150M投資(A-3) |
| [INFO-008](../Information/2026-06-19/collected-raw.md#INFO-008) | Grok軍事展開96h/2,000弾薬(B-2) |
| [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) | OpenAI Pentagon GenAI.mil 300万人(C-3) |
| [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) | Anthropic ARR $470億 vs OpenAI $330億逆転(C-2) |
| [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) | Claude Code採用3%→24%・JetBrains 1万人調査(B-3) |
| [INFO-019](../Information/2026-06-19/collected-raw.md#INFO-019) | OpenAI Apps SDK更新・MCP統合完全対応(A-3) |
| [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) | Jevons paradox・トークン90%安価化・支出倍増(A-2) |
| [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) | Fable 5/Mythos 5 SOTA維持(A-3) |
| [INFO-002](../Information/2026-06-14/collected-raw.md#INFO-002) | 政府がFable 5/Mythos 5全外国人アクセス停止(A-3) |
| [INFO-014](../Information/2026-06-14/collected-raw.md#INFO-014) | MCP RC公開・ステートレスプロトコルコア(B-3) |
| [INFO-015](../Information/2026-06-14/collected-raw.md#INFO-015) | AAIF 6ヶ月振り返り・標準化進展(B-3) |
| [INFO-020](../Information/2026-06-14/collected-raw.md#INFO-020) | Gemini Skills OSS・開放支持(A-3) |
| [INFO-027](../Information/2026-06-14/collected-raw.md#INFO-027) | NSPM-11詳細分析・専門家一致確認(B-3) |
| [INFO-029](../Information/2026-06-14/collected-raw.md#INFO-029) | JAWBONE法・超党派で政府AI企業強制禁止(B-3) |
| [INFO-032](../Information/2026-06-14/collected-raw.md#INFO-032) | 企業無効化権剥奪(B-3) |
| [INFO-035](../Information/2026-06-14/collected-raw.md#INFO-035) | Anthropicほぼ$1T評価額(B-3) |
| [INFO-042](../Information/2026-06-14/collected-raw.md#INFO-042) | DeepSeek V4 Pro > GPT-5.5 Pro 1/5コスト(B-3) |
| [INFO-043](../Information/2026-06-14/collected-raw.md#INFO-043) | OSS 3モデルGPT-4超え(B-3) |
| [INFO-051](../Information/2026-06-14/collected-raw.md#INFO-051) | Google Cloud 63%成長$460Bバックログ(C-3) |
| [INFO-061](../Information/2026-06-14/collected-raw.md#INFO-061) | OpenAI大幅値下げ検討(B-3) |
| [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001) | OpenAI Ona買収・Codex 5M週間ユーザー(A-3) |
| [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) | OpenAI機密S-1提出(A-3) |
| [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | OpenAI Phase 3宣言・2028年3月AI研究自動化(A-3) |
| [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) | Codex 6役割別プラグイン・62アプリ110スキル(A-3) |
| [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006) | Claude Fable 5/Mythos 5・$10/M入力・FrontierCode首位(A-3) |
| [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) | Grok Build Plugin Marketplace(A-3) |
| [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014) | DiffusionGemma 4倍高速化(A-3) |
| [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019) | OpenAI価格引き下げ検討・WSJ報道(B-3) |
| [INFO-023](../Information/2026-06-12/collected-raw.md#INFO-023) | WH EO先進AI・NSPM-11同時署名(A-3) |
| [INFO-025](../Information/2026-06-12/collected-raw.md#INFO-025) | Gartner 40%エンタープライズエージェント(B-3) |
| [INFO-026](../Information/2026-06-12/collected-raw.md#INFO-026) | AIレイオフブーメラン効果・Klarna再雇用(C-3) |
| [INFO-031](../Information/2026-06-12/collected-raw.md#INFO-031) | AIベンダーロックイン・推論の暗黙知(C-3) |
| [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034) | AIコーディング市場$9.8-11B・51%コミットAI支援(B-3) |
| [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) | 豆包MAU 610万減・2000億元投資上方修正(C-3) |
| [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036) | MCP RC公開・ステートレスプロトコルコア(B-3) |
| [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) | BCG AI時代組織再設計・大半が収益未達(B-3) |
| [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) | Fortune 500 AI階層フラット化・41%管理層削減(B-3) |
| [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) | Gemini Skill Registry/RAG Engine(A-3) |
| [INFO-045](../Information/2026-06-12/collected-raw.md#INFO-045) | NSPM-11国家安全保障AI大統領覚書(A-3) |
| [Arbiter v4.13](../state/arbiter-2026-06-19.md) | 確度評価の完全根拠 |
