# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-06-04
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。QHG Y軸v3.84以降とv3.83以前は非整合
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-06-04時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.8, Sonnet 4.6, Claude Code | $965B評価額(A-1)・S-1提出(A-3) | 3位 | S-1機密提出 [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004). v.DoW仮処分 [INFO-020](../Information/2026-06-04/collected-raw.md#INFO-020). Partner Network $100M [INFO-002](../Information/2026-06-04/collected-raw.md#INFO-002). UK政府提携 [INFO-001](../Information/2026-06-04/collected-raw.md#INFO-001). H-GOV-001 45%(停止条件宣言). H-ANT-001 42% |
| OpenAI | GPT-5.5, Codex, Skills Beta | $852B評価額(C-1) | 1位 (Elo 1502) | H-OAI-001 58%. AWS Bedrock GA [INFO-024](../Information/2026-06-04/collected-raw.md#INFO-024). Erdős予想反証 [INFO-039](../Information/2026-06-04/collected-raw.md#INFO-039). Skills/Shell/Compaction [INFO-007](../Information/2026-06-04/collected-raw.md#INFO-007) |
| Google | Gemini 3.1 Pro, 3.5 Flash, Antigravity Agent | Cloud $4,600億バックログ(A-1) | 2位 | 围い込み19件. Gemini 3全ラインナップ [INFO-018](../Information/2026-06-04/collected-raw.md#INFO-018). Antigravity Agent [INFO-011](../Information/2026-06-04/collected-raw.md#INFO-011). Cloud $4,600億 [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034). H-GOO-002 25% |
| SpaceXAI | Grok 4.3, Grok Build | $20B調達(B-3) | 4位 | H-XAI-002 60%. 前回更新から構造的変化なし |
| ByteDance | 豆包2.0, Coze 2.5, Seedance 2.1 | CAPEX RMB 2,300億(B-2) | 非公開 | 豆包有料化 [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031). MAU 3.3億 [INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044). DeepSeek $7.4B [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033). H-BTD-002 49%(low移行) |

---

## 0. 一文要約

[H-GOV-001](../config/hypotheses.json)が45%に低下し停止条件が宣言された。政府萎縮効果の確度低下が定着した。[H-GOO-002](../config/hypotheses.json)は25%（-4%/3R）に低下し、围い込み19件・開放C 28R不在でlow帯が確定的である。[H-BTD-002](../config/hypotheses.json)は49%（-2%/2R）に低下し、豆包有料化 [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) が低価格戦略前提を直接矛盾させた。[H-CAR-001](../config/hypotheses.json)は33%に微増し、142K解雇 [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041)（A-2）が強力Cだが、97%採用5%本番到達 [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027)（C-2）が強力Iで相殺構造にある。Trump大統領令 [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023)・30/60日タイムライン [INFO-047](../Information/2026-06-04/collected-raw.md#INFO-047) が新規A-2品質規制証拠として蓄積した。DeepSeek $7.4B [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033)・Meta Muse Spark クローズドソース [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) がそれぞれ資本集中と围い込み加速の信号である。Anthropic S-1機密提出 [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) は上場準備の具体化を示す。SCN-003が35%で最高確率を維持し、SCN-004が26%でSCN-002（24%）を再逆転した。

---

## 1. コア判断

[H-GOV-001](../config/hypotheses.json)は48→45%に低下し、停止条件が宣言された。政府萎縮効果の確度低下が複数ラウンドにわたり累積し、監視条件に移行した。$965B評価額 [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) は商業ポテンシャルへの市場評価であり、安全性スタンスへの評価とは同義ではない。S-1機密提出は資金調達の具体化だが、政府市場アクセス制約（SCR指定継続）との二重構造は変わらない。v.DoW仮処分 [INFO-020](../Information/2026-06-04/collected-raw.md#INFO-020) は安全性立場の堅持を示すA-2品質I側証拠である。

[H-GOO-002](../config/hypotheses.json)は29→25%（-4%/3R）に低下した。围い込み19件蓄積と開放C 28R連続不在で、low帯確定が深まった。Gemini 3全ラインナップ [INFO-018](../Information/2026-06-04/collected-raw.md#INFO-018)・Antigravity Agent [INFO-011](../Information/2026-06-04/collected-raw.md#INFO-011) は製品能力の向上だが、围い込み方向への寄与に過ぎない。Cloud $4,600億バックログ [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034) はデータ優位の商業的裏付けであり、围い込みインセンティブを強化する。

[H-BTD-002](../config/hypotheses.json)は51→49%（-2%/2R）に低下し、low帯に移行した。豆包有料化 [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) は低価格戦略の前提を直接矛盾させる。MAU 3.3億 [INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044) は到達規模のCだが、有料化は価格競争戦略からの逸脱を示す。DeepSeek $7.4B [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) は外部資金調達の具体化で、ByteDanceの価格圧力環境が変化しつつある。

[H-CAR-001](../config/hypotheses.json)は32→33%に微増した。142K解雇 [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041)（A-2）はMeta/Coinbase/Block 10%以上削減で強力Cである。しかし97%採用・5%本番到達 [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027)（C-2）は強力Iであり、C/Iの高品質均衡で±0%が維持された。「採用爆発」と「本番到達停滞」の二重構造が雇用影響の速度不確定性を示す。

Trump大統領令 [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023)・30/60日タイムライン [INFO-047](../Information/2026-06-04/collected-raw.md#INFO-047) はfrontier model review・DPA・中国競争を含む包括的枠組みである。IND-030 high/risingを維持する。Meta Muse Spark クローズドソース [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) はLlama後継の闭源転換であり、围い込み加速の新たな信号である。Big 4 $7,250B投資 [INFO-042](../Information/2026-06-04/collected-raw.md#INFO-042) とAPI価格 $30→$1/MTok [INFO-028](../Information/2026-06-04/collected-raw.md#INFO-028) は、資本集中と価格崩壊が同時進行する構造を示す。Erdős予想反証 [INFO-039](../Information/2026-06-04/collected-raw.md#INFO-039) は数学的推論能力の新たな到達点を示す。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | H-GOV-001 48→45% 停止条件宣言 | 政府萎縮効果確度低下の定着。監視条件移行。$965B≠安全性評価の判断維持 | 統合判断 | [H-GOV-001](../config/hypotheses.json) |
| 高 | 142K tech layoffs 2026（A-2）Meta/Coinbase/Block 10%+ | H-CAR-001強力C。採用97%と本番5%の二重構造で均衡 | A-2 | [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) |
| 高 | Trump AI EO frontier model review・DPA・中国競争（A-2） | IND-030 high/rising維持。規制環境の包括的再構成 | A-2 | [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) [INFO-047](../Information/2026-06-04/collected-raw.md#INFO-047) |
| 高 | 豆包有料化が低価格戦略を直接矛盾 | H-BTD-002 51→49% low移行。価格戦略前提の崩壊 | B-2 | [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) |
| 高 | 围い込み19件・開放C 28R不在 | H-GOO-002 29→25% low帯確定深化。3R連続-1% | 統合判断 | [H-GOO-002](../config/hypotheses.json) |
| 高 | S-1機密提出（A-3）+v.DoW仮処分（A-2） | Anthropic上場準備具体化。安全性立場維持との二重構造 | A-3/A-2 | [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) [INFO-020](../Information/2026-06-04/collected-raw.md#INFO-020) |
| 高 | DeepSeek $7.4B初外部資金調達（B-2） | 中国AI資本集中の新段階。H-BTD-002価格圧力環境変化 | B-2 | [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) |
| 高 | Meta Muse Spark クローズドソース（B-2） | Llama後継闭源。围い込み加速の新信号。SCN-004支持 | B-2 | [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) |
| 高 | 97%採用・5%本番到達（C-2） | H-CAR-001強力I。C/I高品質均衡で±0%維持。採用-本番ギャップの構造的性質 | C-2 | [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027) |
| 中 | Erdős予想反証（B-2）・API価格$30→$1（C-2） | IND-028 elevated/rising。数学推論到達点・価格崩壊同時進行 | B-2/C-2 | [INFO-039](../Information/2026-06-04/collected-raw.md#INFO-039) [INFO-028](../Information/2026-06-04/collected-raw.md#INFO-028) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | 「加速する構造的トレンド」判断が崩れ、SCN-004の前提が弱体化する | 180日 | [IND-025](../config/indicators.json) |
| SCN-001がSCN-004を再度逆転する | コモディティ化+開放の優位判断が一時的変動の可能性。围い込み+差別化復活の根拠 | 180日 | [scenarios.json](../config/scenarios.json) |
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-025](../config/indicators.json) |
| Anthropic SCR指定が解除され政府市場アクセスが回復する | H-GOV-001萎縮効果前提が崩れる。停止条件の再検証が必要 | 180日 | [IND-030](../config/indicators.json) |
| Google围い込み項目の蓄積が止まり、開放C証拠が3件以上出現する | H-GOO-002 28R不在の前提が崩れ、SCN-003支持要因が弱体化 | 180日 | [IND-027](../config/indicators.json) |
| 豆包が有料化を撤回し無料低価格戦略に復帰する | H-BTD-002 low移行前提の再検証。価格戦略逸脱が一時的だった場合の確度回復 | 180日 | [H-BTD-002](../config/hypotheses.json) |
| AI本番到達率が採用率の50%以上に改善する | H-CAR-001のI側根拠が崩れ、雇用削減加速の確度が上昇する | 180日 | [IND-026](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 58% | medium ±0%。AWS Bedrock GA [INFO-024](../Information/2026-06-04/collected-raw.md#INFO-024) は配信拡大C。Erdős反証 [INFO-039](../Information/2026-06-04/collected-raw.md#INFO-039) は技術的優位I。コモディティ化下での「支配」定義未解決 | [INFO-024](../Information/2026-06-04/collected-raw.md#INFO-024) [INFO-007](../Information/2026-06-04/collected-raw.md#INFO-007) | [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 44% | low ±0%。Skills/Shell/Compaction [INFO-007](../Information/2026-06-04/collected-raw.md#INFO-007) は独自実行環境围い込みI。OSSギャップ消滅がマルチモデル採用を加速 | [INFO-007](../Information/2026-06-04/collected-raw.md#INFO-007) | [INFO-024](../Information/2026-06-04/collected-raw.md#INFO-024) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究に大規模資源を投入する | 3% | low ±0%。確度極低。Erdős反証 [INFO-039](../Information/2026-06-04/collected-raw.md#INFO-039) は研究能力の到達点だがAGI優先方針とは非直結 | [INFO-039](../Information/2026-06-04/collected-raw.md#INFO-039) | [INFO-007](../Information/2026-06-04/collected-raw.md#INFO-007) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 45% | medium ±0%。停止条件宣言。48→45%。$965B評価額≠安全性評価。v.DoW仮処分はI側A-2蓄積。監視条件移行 | [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) [INFO-047](../Information/2026-06-04/collected-raw.md#INFO-047) | [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) [INFO-020](../Information/2026-06-04/collected-raw.md#INFO-020) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 42% | low ±0%。Partner Network $100M [INFO-002](../Information/2026-06-04/collected-raw.md#INFO-002)・UK政府提携 [INFO-001](../Information/2026-06-04/collected-raw.md#INFO-001) はCだが、安全性直接Cの定義曖昧さ継続 | [INFO-002](../Information/2026-06-04/collected-raw.md#INFO-002) [INFO-001](../Information/2026-06-04/collected-raw.md#INFO-001) | [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 64% | medium ±0%。S-1提出 [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) は資金基盤強化C。Partner Network $100M [INFO-002](../Information/2026-06-04/collected-raw.md#INFO-002) は生態系拡大C | [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) [INFO-002](../Information/2026-06-04/collected-raw.md#INFO-002) | (budget overruns構造的リスク継続) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持しAWS・GCP・Azure全てで同等の機能を提供する | 6% | low ±0%。マルチクラウド均衡証拠不在。棄却候補維持 | (マルチクラウド証拠不在) | (インフラ集中深化) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 52% | medium ±0%。Cloud $4,600億バックログ [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034) はA-1品質C。Gemini 3全ラインナップ [INFO-018](../Information/2026-06-04/collected-raw.md#INFO-018) は製品力C。アンカリング認識継続 | [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034) [INFO-018](../Information/2026-06-04/collected-raw.md#INFO-018) | (代替説明「業界全体押し上げ」未解決) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し围い込みを回避する | 25% | low -1%。29→25%（3R累積）。围い込み19件I蓄積。開放C 28R連続不在。low帯確定深化 | (围い込みI蓄積継続) | (開放C不在継続) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 50% | medium ±0%。Antigravity Agent [INFO-011](../Information/2026-06-04/collected-raw.md#INFO-011) は研究応用C。Gemini 3全ラインナップは統合力C。方向は上向き | [INFO-011](../Information/2026-06-04/collected-raw.md#INFO-011) [INFO-018](../Information/2026-06-04/collected-raw.md#INFO-018) | (DeepMind統合課題継続) |
| [H-XAI-001](../config/hypotheses.json) | xAIはXのリアルタイムデータを活用し差別化する（棄却） | 35% | low。37R+証拠不在。xAI→SpaceXAI統合で独立企業前提崩壊。正式棄却維持 | (証拠不在) | (全製品Xデータ非依存) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 60% | medium ±0%。前回更新から構造的変化なし。価格競争下でのシェア獲得難度増大。API価格$30→$1 [INFO-028](../Information/2026-06-04/collected-raw.md#INFO-028) は業界全体の価格圧力強化 | (価格低い) | (DL減・市場採用不在) |
| [H-XAI-003](../config/hypotheses.json) | xAIはSpaceX統合で宇宙・製造業特化AIを展開する（棄却） | 35% | low。38R+直接的特化AI製品証拠不在。正式棄却維持 | (証拠不在) | (特化製品不在) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 55% | medium ±0%。前回更新から構造的変化なし。性能≠市場成功。市場採用データ不在継続 | (Grok Build正式発売) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持する | 64% | medium ±0%。MAU 3.3億 [INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044) は到達規模C。中国国内C圧倒的。グローバル展開C不在。ミラーイメージングリスク | [INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044) | (グローバル展開制約継続) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 49% | low -1%。51→49%（2R累積）。豆包有料化 [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) が低価格前提を直接矛盾。low帯移行 | (MAU 3.3億) | [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% | medium ±0%。新規著作権関連証拠なし。安定観察継続 | (著作権制約継続) | (新規証拠なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 33% | medium ±0%。142K解雇（A-2）強力C。97%採用5%本番到達（C-2）強力I。C/I高品質均衡 | [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) | [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | medium ±0%。ジュニア採用67%減+ミドル/シニアAI需要上昇の構造的裏付け。69%上限 | (構造的裏付け継続) | (METR本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | medium ±0%。中間工程排除C蓄積。142K解雇 [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) は方向性支持。速度不確定 | [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | AIセキュリティ認証義務化・shadow AI 86%。攻撃面拡大基調。新規大規模実被害なし。high/rising | 2026-06-04 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Gemini 3全ラインナップ [INFO-018](../Information/2026-06-04/collected-raw.md#INFO-018) 全モダリティ対応。API価格$30→$1 [INFO-028](../Information/2026-06-04/collected-raw.md#INFO-028)。「真の理解」検証未解決。elevated/stable | 2026-06-04 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | 97%採用・5%本番到達 [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027)。Glean 73→85%。68pt採用-本番ギャップ構造的固定化。high/rising | 2026-06-04 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | AAIF 190メンバー・Microsoft Skills OSS・MCP継続拡大。標準化進展継続。high/rising | 2026-06-04 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Erdős予想反証 [INFO-039](../Information/2026-06-04/collected-raw.md#INFO-039)・ARC-AGI 2 GPT-5.5初達成。客観的到達点の蓄積。elevated/rising | 2026-06-04 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | Cloud $4,600億 [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034)・ByteDance CAPEX RMB 2,300億・DeepSeek $7.4B [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033)・Big 4 $7,250B [INFO-042](../Information/2026-06-04/collected-raw.md#INFO-042)。資本集中加速。high/rising | 2026-06-04 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Trump EO [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023)・自律型武器議論・EU AI Act更新。規制環境包括的再構成。high/rising | 2026-06-04 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-04 | H-GOV-001 48→45%(停止条件宣言)・H-GOO-002 29→25%(围い込み19件)・H-BTD-002 51→49%(low移行)・H-CAR-001 32→33%・Trump大統領令(INFO-023/047)・142K解雇(INFO-041)・DeepSeek $7.4B(INFO-033)・Meta Muse Sparkクローズド(INFO-040)・S-1機密提出(INFO-004)・プレイヤースナップショット更新を反映して全面書き直し | [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) [INFO-047](../Information/2026-06-04/collected-raw.md#INFO-047) [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) [INFO-020](../Information/2026-06-04/collected-raw.md#INFO-020) [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034) [INFO-018](../Information/2026-06-04/collected-raw.md#INFO-018) [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) [INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044) | H-GOV-001 48→45%・H-GOO-002 29→25%・H-BTD-002 51→49%・H-CAR-001 32→33%・SCN-002 25→24%・SCN-004 25→26%(SCN-002再逆転) |
| 2026-05-31 | Arbiter v3.94完了反映。SCN-004 tied SCN-002(25%)順位逆転。H-GOV-001 -2%(50→48%・6R連続)・H-ANT-001 -2%(44→42%)・H-GOO-002 -2%(31→29%)・H-OAI-001 -2%(60→58%)・H-CAR-001 +1%(31→32%)。Pattern J/G確度中-高→中。Pattern H/I確度高。Mythos一般公開・Karpathy入社・budget overruns・Stanford雇用データ。IND-030 elevated→high。全20仮説・7指標更新反映して全面書き直し | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-014](../Information/2026-05-31/collected-raw.md#INFO-014) [INFO-007](../Information/2026-05-31/collected-raw.md#INFO-007) | SCN-002 27→25%・SCN-003 37→35%・SCN-004 21→25%(SCN-002と同率)・SCN-001 15%据え置き・BS-001 17%据え置き・H-GOV-001 50→48%・H-ANT-001 44→42%・H-GOO-002 31→29%・H-OAI-001 60→58%・H-CAR-001 31→32% |
| 2026-05-29 | Arbiter v3.92完了反映。H-GOV-001 -1%（A-1品質I証拠5件累積否定）・H-GOO-002 -1%（围い込み22件・開放C 21R不在）・H-ANT-002 ±0%（概念混同是正）・H-ANT-001上限条件再設計実行。Pattern E格下げ（確度: 中）。Pattern F確度中-高。全20仮説・7指標更新反映して全面書き直し | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004) [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) | H-GOV-001 51→50%・H-GOO-002 32→31%・H-ANT-002 64%据え置き・SCN全件±0%（15/27/37/21%）・BS-001 17%据え置き |
| 2026-05-28 | Arbiter v3.91完了反映。「政府-市場ギャップ」再定義。Pattern B/C格下げ。H-GOV-001 -1%・H-GOO-001 -1%・H-GOO-002 -1%・H-XAI-002 -1%・H-CAR-001 +1%・SCN-001 -1%。全20仮説・7指標更新反映して全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) | SCN-001 16→15%・SCN-002 27%据え置き・SCN-003 36→37%・SCN-004 21%据え置き・H-GOV-001 52→51%・H-GOO-001 54→53%・H-GOO-002 33→32%・H-XAI-002 62→61%・H-BTD-002 54→51%・H-CAR-001 30→31% |
| 2026-05-23 | Arbiter v3.86完了反映・INFO-069因果チェーンA-2確認・Epoch AI 9x-900x/年・Anthropic $10.9B・Goldman Sachs 66GW・Google围い込み17件・Big Tech $420B・H-GOO-001 +1%・H-GOO-002 -1%・H-BTD-002 -1%・H-CAR-001 +1%・全20仮説表示・7指標更新反映して全面書き直し | [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) | SCN-001 17→16%・SCN-002 27%据え置き・SCN-003 36%据え置き・SCN-004 20→21%・H-GOO-001 53→54%・H-GOO-002 36→35%·H-BTD-002 55→54%·H-CAR-001 27→28%·BS-001 17%据え置き |

---

## 7. ブラインドスポット

- [H-GOV-001](../config/hypotheses.json)停止条件は確度低下の定着を示すが、萎縮効果の有無そのものの判定基準が「市場評価≠安全性評価」の論理に依存している。Trump大統領令 [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) の30/60日タイムライン [INFO-047](../Information/2026-06-04/collected-raw.md#INFO-047) が執行された場合、停止条件の再評価が必要になる。
- [H-BTD-002](../config/hypotheses.json) low移行は豆包有料化 [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) による前提崩壊だが、有料化がどの価格帯で安定するかが未確定である。DeepSeek $7.4B [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) が中国AI価格構造全体に与える影響の定量評価が不在。
- 142K解雇 [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) と97%採用5%本番到達 [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027) のC/I均衡は[H-CAR-001](../config/hypotheses.json)の確度を膠着させる。採用率と本番到達率の乖離が解消される方向（どちらでも）が雇用影響の速度を決定するが、その触発要因の特定ができていない。
- Meta Muse Spark クローズドソース [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) はLlama後継の闭源転換であり、OSSコミュニティへの影響がSCN-004の前提（围い込み+差別化）を強化する。しかし単一企業の意思決定が他社に波及するかの因果チェーンが未検証である。
- [H-GOO-002](../config/hypotheses.json) 围い込み19件・開放C 28R不在の累積はlow帯確定だが、围い込み項目の「質的重み付け」が不在。全項目を等価とする集計が実際の围い込み強度を過小または過大評価している可能性。
- SCN-004が26%でSCN-002（24%）を再逆転したが、その差は2ptでありノイズレベルに近い。SCN-003（35%）の優位は安定的だが、SCN-002/004の順位変動は意味のあるシグナルかどうかの判定基準が不在。
- S-1機密提出 [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) の内容が非公開であり、財務健全性・ガバナンス構造・安全性コミットメントの詳細が不明。上場が安全性スタンスに与える影響（株主圧力）の評価が不在。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral等の台頭は「5社フレーム」自体の妥当性を問う結果である。
- IND-026 high/risingの根拠である97%採用と5%本番到達の出所 [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027) はC-2品質。採用率の定義（「何」を採用しているか）と本番到達の定義（「何」が本番か）が曖昧で、68ptギャップの構造的性質の解釈が不安定である。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-06-04/collected-raw.md#INFO-001) | Anthropic UK政府提携(A-2) |
| [INFO-002](../Information/2026-06-04/collected-raw.md#INFO-002) | Anthropic Partner Network $100M(A-1) |
| [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) | Anthropic S-1機密提出(A-3) |
| [INFO-007](../Information/2026-06-04/collected-raw.md#INFO-007) | OpenAI Skills/Shell/Compaction(A-1) |
| [INFO-011](../Information/2026-06-04/collected-raw.md#INFO-011) | Google Antigravity Agent(A-1) |
| [INFO-018](../Information/2026-06-04/collected-raw.md#INFO-018) | Gemini 3全ラインナップ(A-1) |
| [INFO-020](../Information/2026-06-04/collected-raw.md#INFO-020) | Anthropic v.DoW仮処分(A-2) |
| [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) | Trump AI EO frontier model review(A-2) |
| [INFO-024](../Information/2026-06-04/collected-raw.md#INFO-024) | OpenAI AWS Bedrock GA(A-1) |
| [INFO-027](../Information/2026-06-04/collected-raw.md#INFO-027) | 97%採用・5%本番到達(C-2) |
| [INFO-028](../Information/2026-06-04/collected-raw.md#INFO-028) | API価格$30→$1/MTok(C-2) |
| [INFO-031](../Information/2026-06-04/collected-raw.md#INFO-031) | 豆包有料化(B-2) |
| [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) | DeepSeek $7.4B初外部資金調達(B-2) |
| [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034) | Google Cloud $4,600億バックログ(A-1) |
| [INFO-039](../Information/2026-06-04/collected-raw.md#INFO-039) | Erdős予想反証(B-2) |
| [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) | Meta Muse Spark クローズドソース(B-2) |
| [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) | 142K tech layoffs 2026(A-2) |
| [INFO-042](../Information/2026-06-04/collected-raw.md#INFO-042) | Big 4 $7,250B AI投資(C-1) |
| [INFO-044](../Information/2026-06-04/collected-raw.md#INFO-044) | ByteDance MAU 3.3億(B-2) |
| [INFO-047](../Information/2026-06-04/collected-raw.md#INFO-047) | Trump EO 30/60日タイムライン(A-2) |
