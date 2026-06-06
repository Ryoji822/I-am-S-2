# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-06-06
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。QHG Y軸v3.84以降とv3.83以前は非整合。QHG再定義31R連続未実行
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-06-06時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.8, Sonnet 4.6, Claude Code | $65B調達・$965B評価額(A-1) | SWE-bench首位(88.6%) | $65B調達 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039)・S-1機密提出 [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004). 再帰的自己改善分析 [INFO-045](../Information/2026-06-06/collected-raw.md#INFO-045). SCR指定 [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028). H-ANT-001 42%. H-GOV-001 45%(停止条件1R目) |
| OpenAI | GPT-5.5, Codex, Skills Beta | $852B評価額(C-1) | ARC-AGI 2首位(85%) | API価格体系: GPT-5.5 $5/$30・Nano $0.20/$1.25 [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037). Fine-tuning終了. 推論トークン隠しコスト. H-OAI-001 58% |
| Google | Gemini 3.1 Pro, 3.5 Flash, Antigravity Agent | Cloud $4,600億バックログ(A-1)・Capex $180-190B(A-3) | LMArena Elo首位(1501) | 围い込み32件+開放C 2件出現(30R解除). Capex $180-190B [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010). Gemini Enterprise Agent Platform [INFO-018](../Information/2026-06-06/collected-raw.md#INFO-018). Hassabis AGI 2029 [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044). H-GOO-002 23% |
| SpaceXAI | Grok 4.3, Grok Build | $20B調達(B-3) | 4位 | H-XAI-002 60%. 構造的変化なし |
| ByteDance | 豆包2.0, Coze 3.0, Seedance 2.1 | CAPEX RMB 2,300億(B-2) | 非公開 | 有料化MAU 6.1M減 [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046). Coze 3.0 [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047). 対外投資規制7/1 [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036). H-BTD-002 48% |

---

## 0. 一文要約

[H-GOO-002](../config/hypotheses.json)が23%（-2%/2R）に低下し、围い込み32件蓄積+次元拡大（ハードウェア・決済・SaaS）と開放C 30R不在解除（2件出現）が同時発生した。[H-BTD-002](../config/hypotheses.json)が48%（-1%）に低下し、豆包有料化MAU 6.1M減少 [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) が低価格戦略前提を定量的に直接矛盾させた。[H-GOV-001](../config/hypotheses.json)は45%で停止条件1R目。SCR指定 [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028)・DPA脅迫 [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030)・大統領令 [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032) のA-1品質3件が5日間に連続発生した。[H-CAR-001](../config/hypotheses.json)は34%±0%。AIレイオフ123K件YTD（71%AI理由） [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) がCだが、Klarna品質崩壊再採用 [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041) がIで相殺。Anthropic $65B調達・$965B評価額 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) はAI史上最大。OpenAI API価格体系 [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) でNano $0.20/$1.25がコモディティ化を加速。SCN-001が17%(+1%)に上昇しSCN-003が33%(-1%)に低下。QHG再定義31R連続未実行。

---

## 1. コア判断

[H-GOO-002](../config/hypotheses.json)は25→23%（-2%/2R）に低下した。围い込みI 32件蓄積（+3件: Capex围い込み・Googlebook围い込み・Workday SaaS围い込み）で围い込みの次元がエコシステム・データ・インフラからハードウェア・決済・SaaSに拡大した。同時に開放C 2件出現（Gemini Agent API MCP Server [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016)・agents-cli クロスエージェント [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023)）で30R連続不在が解除された。围い込み蓄積>開放C蓄積の評価は妥当だが、Red指摘の件数インフレリスク（Capexは業界全体Capex増加中での独立性疑問・Googlebookは標準垂直統合・Workdayは排他性未確認）と品質別内訳次回必須開示条件を記録する。SCN-001 +1%は围い込み次元拡大を反映し、SCN-003 -1%は30R固定ペナルティ+SCN-001再配分。

[H-BTD-002](../config/hypotheses.json)は49→48%（-1%）に低下し、low帯深化が続く。豆包有料化MAU 6.1M減少 [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046)（A-2品質）が「低価格戦略を維持」命題に定量的に直接矛盾する。Coze 3.0 [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047) はAgent生態系強化だが価格戦略には直接関連しない。中国対外投資規制 [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) が7月1日に発効し、グローバル展開に新たな障壁。

[H-GOV-001](../config/hypotheses.json)は45%±0%で停止条件1R目。SCR指定 [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028)（A-1）・DPA脅迫 [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030)（A-1）・大統領令自発的枠組み [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032)（A-1）のA-1品質3件がC側に蓄積し、$965B評価額 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039)（A-1）がI側に蓄積した。5日間に5つの重要イベントが連続発生し、C/I二面性が最も強くテストされたラウンド。Trump EO 30日マイルストーン（2026-07-02）が次の転換点。

[H-CAR-001](../config/hypotheses.json)は34%±0%。AIレイオフ123K件YTD（71%AI理由） [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040)（A-1品質）と初級SWE求人65%減 [INFO-042](../Information/2026-06-06/collected-raw.md#INFO-042)（B-2品質）がCだが、Klarna品質崩壊→再採用 [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041)（B-2品質）とエンタープライズパイロットROI 5% [INFO-034](../Information/2026-06-06/collected-raw.md#INFO-034)（C-2品質）がI。C/I相殺均衡。Red指摘: INFO-042は18ヶ月前データ・INFO-040因果帰属未検証。

Anthropic $65B調達・$965B評価額 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) はAI史上最大。2026年5月のグローバルVCは$92B（史上2位）、Anthropicの$50Bが54%を占め、AIセクター全体で$72B（全資金の79%）。資本集中が極まっている。Claude Opus 4.8がSWE-bench 88.6%・HLE 57.9%で首位 [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038)。OpenAI API価格体系でNano $0.20/$1.25 [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) はコモディティ化の加速。推論トークンの隠しコスト（500 token応答で2000+ token消費）は価格の見た目以上の実質負担。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 围い込み32件+開放C 2件出現(30R解除)+次元拡大 | H-GOO-002 25→23%。SCN-001 +1%。围い込み薄化リスク記録 | 統合判断 | [H-GOO-002](../config/hypotheses.json) |
| 高 | 豆包有料化MAU 6.1M減少 | H-BTD-002 49→48%。低価格戦略前提の定量矛盾 | A-2 | [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) |
| 高 | SCR指定+DPA脅迫+大統領令(A-1品質3件)が5日間に連続発生 | H-GOV-001 45%停止条件1R目。C/I二面性最強テスト。Trump EO 30日マイルストーン(2026-07-02) | A-1 | [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028) [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030) [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032) |
| 高 | AIレイオフ123K件YTD・71%AI理由(A-1) | H-CAR-001強力C。AIがレイオフ理由1位。因果帰属未検証(Red指摘) | A-1 | [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) |
| 高 | Anthropic $65B調達・$965B評価額・IPO準備 | AI史上最大調達。グローバルVC $92B/月・Anthropicが54%。資本集中の極致 | A-1 | [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) |
| 高 | OpenAI API価格: GPT-5.5 $5/$30・Nano $0.20/$1.25 | コモディティ化加速。推論トークン隠しコスト注意。SCN-004方向圧力 | B-2 | [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) |
| 高 | Claude Opus 4.8: SWE-bench 88.6%・HLE 57.9%首位 | ベンチマーク首位交代。Gemini 3 Pro LMArena Elo 1501首位。首位分散 | B-2 | [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038) |
| 高 | 中国対外投資規制7/1発効(A-1) | H-BTD-003 C・H-BTD-001 I。グローバル展開障壁追加 | A-1 | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) |
| 高 | Klarna 700人解雇→品質崩壊→再採用 | H-CAR-001 I。AI代替の象徴的教訓ケース。収益15%増と品質崩壊の乖離 | B-2 | [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041) |
| 高 | 初級SWE求人65%減・CS卒業者40%増(B-2) | H-CAR-001 C。供給過剰と需要減少のダブルパンチ。18ヶ月前データ(Red指摘) | B-2 | [INFO-042](../Information/2026-06-06/collected-raw.md#INFO-042) |
| 中 | MCP 97M DL・AAIF 43新メンバー | IND-027 high/rising。標準化爆発的加速。Gemini Agent API MCP対応(INFO-016) | A-2 | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) |
| 中 | Hassabis AGI 2029到達示唆 | IND-028 elevated/rising。主観-客観乖離拡大。AGI定義の曖昧さ | A-1 | [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) |
| 中 | Anthropic再帰的自己改善分析・制御喪失リスク警告 | 技術リスクの自己認識。IND-030 high/rising | A-3 | [INFO-045](../Information/2026-06-06/collected-raw.md#INFO-045) |
| 中 | EU AI Act第4条: 2026年8月3日施行・最大€35M罰金 | 規制環境包括的再構成。域外適用あり | A-2 | [INFO-035](../Information/2026-06-06/collected-raw.md#INFO-035) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | 「加速する構造的トレンド」判断が崩れ、SCN-004の前提が弱体化する | 180日 | [IND-025](../config/indicators.json) |
| Google围い込み蓄積が止まり、開放C証拠が5件以上に拡大する | H-GOO-002の上方修正根拠。30R不在解除が質的転換の開始を示す。現在開放C 2件 | 180日 | [IND-027](../config/indicators.json) |
| 豆包が有料化を撤回し無料低価格戦略に復帰する | H-BTD-002 low深化前提の再検証。価格戦略逸脱が一時的だった場合の確度回復 | 180日 | [H-BTD-002](../config/hypotheses.json) |
| Anthropic SCR指定が解除され政府市場アクセスが回復する | H-GOV-001萎縮効果前提が崩れる。停止条件の再検証が必要 | 180日 | [IND-030](../config/indicators.json) |
| AI本番到達率が採用率の50%以上に改善する | H-CAR-001のI側根拠が崩れ、雇用削減加速の確度が上昇する | 180日 | [IND-026](../config/indicators.json) |
| Trump大統領令自発的枠組みが30日後（2026-07-02）に機能確認される | H-GOV-001萎縮効果限界示唆→-1%検討 | 30日 | [IND-030](../config/indicators.json) |
| QHG Y軸定量評価基準が設定されない（次回Arbiter） | シナリオ確率凍結ペナルティ発動。31R連続未実行 | 次回 | [scenarios.json](../config/scenarios.json) |
| 围い込み32件の品質別内訳で独立性「高」件数が10件未満 | H-GOO-002件数インフレ指摘の妥当性確認。確度上方修正根拠 | 次回 | [IND-027](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 58% | medium ±0%。C/I 20件均衡。API価格体系 [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) は価格コモディティ化圧力。コモディティ化下での「支配」定義未解決。確証バイアス監視継続 | [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) | (Anthropic首位交代継続) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 44% | low ±0%。I蓄積34件。限界効率逓減。Fine-tuning終了 [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) は围い込みI | [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) | (MCP標準化深化) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究に大規模資源を投入する | 3% | low ±0%。新規直接関連証拠なし | (AGI研究継続) | (商業化加速) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 45% | medium ±0%。停止条件1R目。SCR指定+DPA脅迫+大統領令(A-1品質3件)vs $965B評価額(A-1品質1件)。C/I二面性最強テスト | [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028) [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030) [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032) | [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 42% | low ±0%。$65B調達 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) は資金基盤C。Opus 4.8首位 [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038) は技術C。上限条件19R未達成。安全性直接Cの定義曖昧さ継続 | [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038) | ($965B≠安全性評価) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 64% | medium ±0%。$65B調達で資金基盤強化。SDK活発開発C | [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) | (budget overruns構造的リスク) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持しAWS・GCP・Azure全てで同等の機能を提供する | 6% | low ±0%。マルチクラウド均衡証拠不在。棄却候補維持 | (マルチクラウド証拠不在) | (インフラ集中深化) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 51% | medium ±0%。I=0が14R連続。代替説明14R未解決。A-2+条件12R未達成。Cloud $4,600億・Capex $180-190Bは規模CだがGoogle固有性未確認 | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | (代替説明14R未解決) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し围い込みを回避する | 23% | low -2%/2R。围い込みI 32件蓄積+次元拡大。開放C 2件出現(30R解除)。品質別内訳次回必須開示。low帯深化 | (围い込みI蓄積継続) | [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 49% | medium ±0%。A-2+条件13R未達成。49%到達。次回low移行検討。Hassabis AGI 2029 [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044)。Capex $180-190B [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | (A-2+条件未達成継続) |
| [H-XAI-001](../config/hypotheses.json) | xAIはXのリアルタイムデータを活用し差別化する（棄却） | 35% | low。37R+証拠不在。正式棄却維持 | (証拠不在) | (全製品Xデータ非依存) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 60% | medium ±0%。構造的変化なし。API価格コモディティ化で独自性希薄化リスク | (価格低い) | (DL減・市場採用不在) |
| [H-XAI-003](../config/hypotheses.json) | xAIはSpaceX統合で宇宙・製造業特化AIを展開する（棄却） | 35% | low。38R+直接的特化AI製品証拠不在。正式棄却維持 | (証拠不在) | (特化製品不在) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 55% | medium ±0%。構造的変化なし。市場採用データ不在継続 | (Grok Build正式発売) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceは中国で取った規模を足がかりにグローバル展開する | 64% | medium ±0%。Coze 3.0 [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047)。対外投資規制 [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) はI。ミラーイメージングリスク継続 | [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047) | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 48% | low -1%。有料化MAU 6.1M減 [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) が直接矛盾。累積I 26件。low帯深化 | (MAU 330M) | [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% | medium ±0%。対外投資規制 [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) はC。著作権関連新規なし | [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) | (著作権新規なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 34% | low ±0%。AIレイオフ123K(A-1) C・初級SWE 65%減(B-2) C。Klarna再採用(B-2) I・パイロットROI 5%(C-2) I。C/I相殺均衡。Red指摘: INFO-042鮮度18ヶ月前・INFO-040因果帰属未検証 | [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) [INFO-042](../Information/2026-06-06/collected-raw.md#INFO-042) | [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041) [INFO-034](../Information/2026-06-06/collected-raw.md#INFO-034) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | medium ±0%。構造的裏付け継続。69%上限(METR 43%反証) | (構造的裏付け継続) | (METR本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | medium ±0%。中間工程排除C蓄積。AIレイオフ123K [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) 方向支持。速度不確定 | [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | SmartLoader MCPクローン攻撃・ClawHub 46.8%悪意スキル。攻撃面拡大基調。新規大規模実被害なし。high/rising | 2026-06-06 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Gemini Omni任意入力→動画生成 [INFO-012](../Information/2026-06-06/collected-raw.md#INFO-012)・Gemini 3 Pro Deep Think 100.0%首位 [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038)。「真の理解」検証未解決。elevated/stable | 2026-06-06 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | F500 51%本番稼働/ROI 23% [INFO-033](../Information/2026-06-06/collected-raw.md#INFO-033)・パイロットROI 5% [INFO-034](../Information/2026-06-06/collected-raw.md#INFO-034)・Klarna品質崩壊→再採用 [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041)。期待-実態ギャップ定量データ確認。high/rising | 2026-06-06 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 97M DL [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021)・A2A 150組織・Gemini Agent API MCP対応 [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016)・agents-cli [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023)。標準化爆発的加速。high/rising | 2026-06-06 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Hassabis AGI 2029 [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044)・再帰的自己改善分析 [INFO-045](../Information/2026-06-06/collected-raw.md#INFO-045)。主観的前倒し継続。客観的漸進的改善。elevated/rising | 2026-06-06 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | Capex $180-190B [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010)・Anthropic $965B評価額 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039)・VC $92B/月(史上2位)。資本集中加速。high/rising | 2026-06-06 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | SCR指定+DPA脅迫+大統領令+NSA回避+囚人のジレンマ。5日間5イベント。EU AI Act 8/3施行 [INFO-035](../Information/2026-06-06/collected-raw.md#INFO-035)。能力向上と治理多層化同時進行。high/rising | 2026-06-06 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-06 | H-GOO-002 25→23%(围い込み32件+開放C 30R解除)・H-BTD-002 49→48%(MAU 6.1M減)・H-GOV-001 45%±0%(停止条件1R目・SCR+DPA+EO)・H-CAR-001 34%±0%(AIレイオフ123K・Klarna逆転)・SCN-001 +1%(17%)・SCN-003 -1%(33%)・Anthropic $65B・Opus 4.8首位・API価格体系・対外投資規制・Hassabis AGI 2029・プレイヤースナップショット更新を反映して全面書き直し | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028) [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030) [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032) [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038) [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041) [INFO-042](../Information/2026-06-06/collected-raw.md#INFO-042) [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) [INFO-045](../Information/2026-06-06/collected-raw.md#INFO-045) [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047) | H-GOO-002 25→23%・H-BTD-002 49→48%・SCN-001 16→17%・SCN-003 34→33%・SCN-002 24%±0%・SCN-004 26%±0%・围い込み19→32件・開放C 28R不在→30R解除(2件出現) |
| 2026-06-04 | H-GOV-001 48→45%(停止条件宣言)・H-GOO-002 29→25%(围い込み19件)・H-BTD-002 51→49%(low移行)・H-CAR-001 32→33%・Trump大統領令・142K解雇・DeepSeek $7.4B・Meta Muse Sparkクローズド・S-1機密提出・プレイヤースナップショット更新を反映して全面書き直し | [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) | H-GOV-001 48→45%・H-GOO-002 29→25%・H-BTD-002 51→49%・H-CAR-001 32→33%・SCN-002 25→24%・SCN-004 25→26% |
| 2026-05-31 | Arbiter v3.94完了反映。SCN-004 tied SCN-002(25%)順位逆転。H-GOV-001 -2%・H-ANT-001 -2%・H-GOO-002 -2%・H-OAI-001 -2%・H-CAR-001 +1%を反映して全面書き直し | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) | SCN-002 27→25%・SCN-003 37→35%・SCN-004 21→25%・SCN-001 15%・H-GOV-001 50→48%・H-ANT-001 44→42%・H-GOO-002 31→29%・H-OAI-001 60→58% |
| 2026-05-28 | Arbiter v3.91完了反映。「政府-市場ギャップ」再定義。H-GOV-001 -1%・H-GOO-001 -1%・H-GOO-002 -1%・H-XAI-002 -1%・H-CAR-001 +1%・SCN-001 -1%を反映して全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | SCN-001 16→15%・SCN-003 36→37%・H-GOV-001 52→51%・H-GOO-001 54→53%・H-GOO-002 33→32%・H-XAI-002 62→61%・H-BTD-002 54→51%・H-CAR-001 30→31% |

---

## 7. ブラインドスポット

- [H-GOO-002](../config/hypotheses.json) 围い込み32件の品質別内訳が未開示。A-1/A-2品質の独立性「高」件数がいくつあるか不明。Red指摘の件数インフレリスク（同一イベント内複数機能別カウント・垂直統合の围い込み分類妥当性）は妥当。次回必須開示条件化。開放C 2件出現の質的転換可能性が未評価。
- [H-GOV-001](../config/hypotheses.json) 停止条件1R目。SCR指定+DPA脅迫+大統領令のA-1品質3件は強力Cだが、$965B評価額(A-1)は強力I。C/I二面性の最終帰趨が不明。Trump EO 30日マイルストーン（2026-07-02）が次の転換点。
- [H-BTD-002](../config/hypotheses.json) low帯深化（48%）は豆包有料化MAU 6.1M減による前提崩壊だが、有料化がどの価格帯で安定するかが未確定。対外投資規制7/1発効がグローバル展開に与える影響の定量評価が不在。
- AIレイオフ123K件YTD（71%AI理由） [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) の因果帰属未検証。AIが真の原因か口実かの判別が不能。初級SWE求人65%減 [INFO-042](../Information/2026-06-06/collected-raw.md#INFO-042) は18ヶ月前データ（2025年1月）で鮮度リスクあり。2026年最新データが3R連続未取得。
- Anthropic $65B調達 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) の使途・条件が非公開。S-1内容も非公開。上場が安全性スタンスに与える影響（株主圧力）の評価が不在。
- OpenAI API推論トークンの隠しコスト [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) が価格比較を複雑化。見た目の価格($0.20/$1.25)と実際のコストの乖離が他社にもある可能性。
- QHG再定義31R連続未実行（v3.74～v4.00）。Y軸「フロンティア差別化の持続性」の定量評価基準が未設定。次回Arbiterで強制設定。未設定の場合はシナリオ確率凍結ペナルティ発動。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral等の台頭は「5社フレーム」自体の妥当性を問う結果。
- Klarna事例 [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041) の「収益15%増」と「品質崩壊」の乖離が、ROI評価方法論の根本的限界を示唆。収益と品質の測定次元が異なる。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | Google I/O Capex $180-190B围い込み(A-3) |
| [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) | Googlebook围い込み(A-3) |
| [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) | Gemini Agent API MCP Server・開放C出現(A-3) |
| [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) | AAIF: MCP 97M DL・A2A 150組織(A-2) |
| [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) | agents-cli クロスエージェント・開放C出現(A-3) |
| [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028) | Anthropic SCR指定(A-1) |
| [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030) | DPA脅迫(A-1) |
| [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032) | Trump大統領令自発的枠組み(A-1) |
| [INFO-035](../Information/2026-06-06/collected-raw.md#INFO-035) | EU AI Act第4条8/3施行(A-2) |
| [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) | 中国対外投資規制7/1発効(A-1) |
| [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) | OpenAI API価格体系・Nano $0.20/$1.25(B-2) |
| [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038) | LLMベンチマーク: Opus 4.8 SWE-bench首位(B-2) |
| [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) | Anthropic $65B調達・$965B評価額(A-1) |
| [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) | AIレイオフ123K件YTD・71%AI理由(A-1) |
| [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041) | Klarna 700人解雇→品質崩壊→再採用(B-2) |
| [INFO-042](../Information/2026-06-06/collected-raw.md#INFO-042) | 初級SWE求人65%減(B-2) |
| [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) | Hassabis AGI 2029到達(A-1) |
| [INFO-045](../Information/2026-06-06/collected-raw.md#INFO-045) | 再帰的自己改善分析(A-3) |
| [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) | Doubao有料化MAU 6.1M減(A-2) |
| [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047) | Coze 3.0 マルチエージェント(B-2) |
| [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048) | Workday SaaS围い込み(B-2) |
| [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) | DeepSeek $7.4B初外部資金調達(B-2) |
| [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034) | Google Cloud $4,600億バックログ(A-1) |
| [Arbiter v4.00](../state/arbiter-2026-06-06.md) | 確度評価の完全根拠 |
