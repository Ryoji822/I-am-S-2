# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-05-29
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。QHG Y軸v3.84以降とv3.83以前は非整合
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-29時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.8, Sonnet 4.6, Claude Code | $965B評価額(A-1) | 3位 | Series H $65B [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013). KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002). Opus 4.8 [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045). SCR指定継続. Trust Center包括認証 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006). Milan/Seoul開設 [INFO-046](../Information/2026-05-29/collected-raw.md#INFO-046) |
| OpenAI | GPT-5.5, Codex, Skills Beta | $730B評価額(A-2) | 1位 (Elo 1502) | Skills Beta open standard準拠 [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008). o3引退8/26 [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011). gpt-oss-120b/20b [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043). Pentagon受益 [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) |
| Google | Gemini 3.5, Spark, Enterprise Agent Platform | Cloud $20B/63% YoY | 2位 | 围い込み22件蓄積. Managed Agents API [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004). Interactions API [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005). H-GOO-002 31% |
| SpaceXAI | Grok 4.3, Grok Build | $20B調達(B-3) | 4位 | 前回更新から構造的変化なし. DL 60%減で苦戦継続 |
| ByteDance | 豆包2.0, Coze 2.5, Seedance 2.1 | $30B(B-3) | 非公開 | 前回更新から構造的変化なし. DeepSeek価格圧力継続 |

---

## 0. 一文要約

AnthropicのA-1品質証拠5件（Series H $65B [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013)・$965B評価額・KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002)・Trust Center包括認証 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006)・Opus 4.8 [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045)）がH-GOV-001萎縮効果命題を累積否定し、H-GOV-001は50%（-1%）に低下した [H-GOV-001](../config/hypotheses.json)。「政府-市場ギャップ」の構造的二面性が継続し、Pattern Eは「構造的二面性の継続」（確度: 中）に格下げされた。Google围い込みは22件蓄積（Managed Agents API [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004)・Interactions API [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005)）で開放C証拠が21R連続不在となり、H-GOO-002は31%（-1%）に低下した [H-GOO-002](../config/hypotheses.json)。OpenAI Skills Beta [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) がopen standard準拠で発表され、MCP 97M・SKILL.md 40K+と合わせて開放標準の爆発的進展が継続する（IND-027 high/rising）。CVE-2026-22561 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006)・SCR指定継続・Trump EO撤回で能力-リスク二面性が深化し（IND-030 high/rising）、SCN-003「静かな围い込み」は37%で最高確率を維持する [scenarios.json](../config/scenarios.json)。US DC $50B/yr・McKinsey $5.2T・Anthropic $65Bで資本流入が劇的加速し（IND-029 high/rising）、Pattern F「臨界点接近」は確度中-高を維持する。

---

## 1. コア判断

H-GOV-001は50%（-1%）に低下した。A-1品質I証拠5件（Series H $65B [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013)・$965B評価額・KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002)・金融採用・Trust Center包括認証 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006)）が萎縮効果命題を累積否定した。SCR C証拠（Pentagon除外・控訴裁懐疑）も蓄積するが、I側が品質で圧倒する。3R連続-1%は保守性原則に合致する。50%到達で「政府-市場ギャップ」の構造的二面性が定着した。Pattern Eは「構造的二面性の継続」（確度: 中）に格下げされた（旧「結晶化」・Red採用）。

H-ANT-002は64%維持（±0%）であった。Red指摘の「Claude Cowork/Managed Agents」≠「Claude Code/SDK」概念混同是正を採用し、Blue自身の「SDK基盤と推測される」に基づく+1%は不適切と判断した。KPMG 276K・金融エージェントはH-ANT-001強化証拠として再分類された。H-ANT-001上限条件は再設計実行された（旧: 安全性第1位選択理由A-2確認 → 新: 上位3要因以内または安全性除外で同等代替説明なしA-2確認）。上限条件見直しが長期議題として累積してきた17Rの構造的問題に対応する。

Google围い込みが多面的深化した。围い込み22件蓄積でH-GOO-002は31%（-1%）に低下した [H-GOO-002](../config/hypotheses.json)。Managed Agents API [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004)・Interactions API [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) は同一プラットフォーム異機能で別件カウントとした。開放C証拠は21R連続不在となり、low帯深化が確定的である。H-GOO-001は53%据え置き [H-GOO-001](../config/hypotheses.json)。SCN-003は37%で最高確率を維持するが、5R連続±0%で警告発出済みであり、次回±0%で-1%自動適用条件が設定された [scenarios.json](../config/scenarios.json)。

開放標準の爆発的進展が継続している。OpenAI Skills Beta [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) がopen standard準拠で発表され、MCP 97M・SKILL.md 40K+と合わせてIND-027 high/risingを維持する。同時に各社独自実行環境围い込みが同時進行しており、「開放標準＋围い込み実装」パターンの定着が観察される。SCN-003とSCN-004の支持要因が真正に混在する方向混成状態にある。

資本流入が劇的加速している。US DC $50B/yr・McKinsey $5.2T [INFO-025](../Information/2026-05-29/collected-raw.md#INFO-025)・Anthropic $65B [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) でIND-029 high/risingを維持する。Anthropic $65Bは単一企業として過去最大である。CVE-2026-22561 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006)・SCR指定継続・Trump EO撤回・Pope回勅・EU multi-agent規制で能力向上とリスク治理後退の同時進行が深化し、IND-030 high/risingの6重蓄積が加速する。Fortune 500平均<15エージェント・88%失敗・Gartner 150K予測でIND-026 high/risingが継続し、エージェント本番到達の68pt採用ギャップが構造的固定化している。Pattern F「臨界点接近」は確度中-高を維持する（Red部分採用・B-2品質単一ソースで高過大）。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | A-1品質I証拠5件（$65B・$965B・KPMG 276K・金融採用・Trust Center）が萎縮効果を累積否定 | H-GOV-001 -1%（51→50%）の根拠。50%到達。3R連続-1%。Pattern E格下げ | A-1 | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) |
| 高 | 围い込み22件蓄積。Managed Agents API・Interactions API追加。開放C 21R連続不在 | H-GOO-002 -1%（32→31%）根拠。low帯深化。SCN-003 37%の根拠強化 | A-1/C-3 | [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004) [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) |
| 高 | OpenAI Skills Beta open standard準拠。MCP 97M・SKILL.md 40K+ | IND-027 high/rising。開放標準爆発的進展。「開放標準＋围い込み実装」パターン定着 | A-1/B-2 | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) |
| 高 | CVE-2026-22561 DLL hijacking・SCR指定継続・Trump EO撤回・Pope回勅・EU multi-agent規制 | IND-030 high/rising。能力-リスク二面性6重蓄積加速。新段階 | A-1/A-2 | [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) |
| 高 | US DC $50B/yr・McKinsey $5.2T・Anthropic $65B | IND-029 high/rising。資本流入劇的加速。Anthropic $65Bは単一企業過去最大 | A-1/B-3 | [INFO-025](../Information/2026-05-29/collected-raw.md#INFO-025) [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) |
| 高 | Fortune 500 <15エージェント・88%失敗・Gartner 150K予測 | IND-026 high/rising。68pt採用ギャップ構造的固定化 | B-2/B-3 | [INFO-020](../Information/2026-05-29/collected-raw.md#INFO-020) [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021) [INFO-041](../Information/2026-05-29/collected-raw.md#INFO-041) |
| 高 | H-ANT-002 ±0%（64%維持）Red採用。概念混同是正・KPMG 276K→H-ANT-001再分類 | Claude Cowork/Managed Agents ≠ Claude Code/SDK。推測ベース+1%否認。上限条件再設計実行 | 統合判断 | [Arbiter v3.92](../state/arbiter-2026-05-29.md) |
| 中 | H-ANT-001上限条件再設計実行。旧:安全性第1位選択理由 → 新:上位3要因以内 | 17R累積ペナルティ構造問題への対応。v3.93適用 | 統合判断 | [Arbiter v3.92](../state/arbiter-2026-05-29.md) |
| 中 | SCN-003 5R連続±0%警告発出。次回±0%で-1%自動適用。QHG再定義次回最優先強制実行 | 方向圧力記録双方向化。18R目。QHG軸区別能力消失リスク | 統合判断 | [Arbiter v3.92](../state/arbiter-2026-05-29.md) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | 「加速する構造的トレンド」判断が崩れ、SCN-004の前提が弱体化する | 180日 | [IND-025](../config/indicators.json) |
| SCN-001がSCN-004を再度逆転する | コモディティ化+開放の優位判断が一時的変動の可能性。围い込み+差別化復活の根拠 | 180日 | [scenarios.json](../config/scenarios.json) |
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-025](../config/indicators.json) |
| Anthropicの政府市場アクセスが回復しSCR指定が解除される | H-GOV-001萎縮効果前提が崩れる。「政府-市場ギャップ」再定義の妥当性検証 | 180日 | [IND-030](../config/indicators.json) |
| Google围い込み項目の蓄積が止まり、開放C証拠が3件以上出現する | H-GOO-002 21R不在の前提が崩れ、SCN-003支持要因が弱体化 | 180日 | [IND-027](../config/indicators.json) |
| 因果チェーン第4段階（他社安全性方針変更）のA-2品質確認 | H-GOV-001の+1%条件充足。萎縮効果が業界全体に波及した証拠 | 180日 | [IND-030](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 60% | Pentagon「漁夫の利」(B-2)は強力C。コモディティ化下での「支配」定義未解決。累積I 22件 | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) | [INFO-027](../Information/2026-05-29/collected-raw.md#INFO-027) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 45% | 围い込み否定12件蓄積。low帯確定。OSSギャップ消滅がマルチモデル採用を加速。Skills Beta open standard準拠 | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究に大規模資源を投入する | 3% | 非営利支配構造で商業収益研究還流保証。但し商業化加速で確度極低。gpt-oss-120b/20b [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) は開放CだがAGI優先とは非直結 | [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 50% | A-1品質I証拠5件（$65B・$965B・KPMG 276K・金融採用・Trust Center）が萎縮効果を累積否定。SCR Cも蓄積だがI側品質圧倒。50%到達。Pattern E格下げ「構造的二面性の継続」 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 44% | KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) は強力C（再分類）。上限条件再設計実行（新: 上位3要因以内）。安全性「機能」vs「スタンス」二面性。low帯深化 | [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) | [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 64% | ±0%維持。Red採用。Claude Cowork/Managed Agents ≠ Claude Code/SDK概念混同是正。KPMG 276KはH-ANT-001再分類。推測ベース+1%否認 | (Cowork/Managed Agentsは別概念) | (推測的証拠の除外) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持しAWS・GCP・Azure全てで同等の機能を提供する | 6% | SpaceXAI Colossus契約でインフラ集中深化。マルチクラウド（均衡）から二重集中へ。棄却候補 | (マルチクラウド証拠不在) | [INFO-046](../Information/2026-05-29/collected-raw.md#INFO-046) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 53% | 7R連続A-3/C-3のみC蓄積でアンカリング認識。代替説明「業界全体押し上げ」未解決。A-2+定量証拠取得時+1%復帰条件維持 | [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004) [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) | [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し围い込みを回避する | 31% | 围い込み22件I蓄積（Managed Agents API [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004)・Interactions API [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005)）。開放C 21R連続不在。low帯深化 | (围い込みI蓄積継続) | (開放C不在継続) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 49% | ±0%維持。Gemini 3.5 Flash/3.1 Pro Preview [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) A-1品質。4R条件（A-2+定量分解）未達成。方向は上向き | [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) | (DeepMind統合課題継続) |
| [H-XAI-001](../config/hypotheses.json) | xAIはXのリアルタイムデータを活用し差別化する（棄却） | 35% | 37R+証拠不在。xAI→SpaceXAI統合で独立企業前提崩壊。Grok全製品Xデータ非依存。正式棄却維持 | (証拠不在) | (全製品Xデータ非依存) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 61% | ±0%維持。DL 60%減で苦戦継続。前回更新から構造的変化なし。価格競争下でのシェア獲得難度増大 | (価格低い) | (DL減・市場採用不在) |
| [H-XAI-003](../config/hypotheses.json) | xAIはSpaceX統合で宇宙・製造業特化AIを展開する（棄却） | 35% | 38R+直接的特化AI製品証拠不在。35%到達。正式棄却維持 | (証拠不在) | (特化製品不在) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 55% | ±0%維持。Grok Build正式発売はC。但し性能≠市場成功。DL 60%減継続。市場採用データ不在 | [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持する | 64% | ±0%維持。前回更新から構造的変化なし。中国国内C圧倒的。グローバル展開C不在。ミラーイメージングリスク | (中国市場C蓄積) | (グローバル展開制約継続) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 51% | ±0%維持。DeepSeek価格圧力継続。前回更新から構造的変化なし。低価格戦略独自性希薄化 | (価格競争継続) | (DeepSeek価格圧力) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% | ±0%維持。新規著作権関連証拠なし。安定観察継続 | (著作権制約継続) | (新規証拠なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 31% | ±0%維持。A-2品質C蓄積（KPMG 64%/71%・BCG 50-55%）。「予測」≠「実績」。KPMG/BCG利益相反リスク認識。+1%は上限 | [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) | (矛盾信号存在) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | ±0%維持。ジュニア採用67%減+ミドル/シニアAI需要上昇の構造的裏付け。METR 43%破損は反証。C/I相殺。69%上限 | [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) [INFO-059](../Information/2026-05-23/collected-raw.md#INFO-059) | (METR本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | ±0%維持。中間工程排除C蓄積。Walmart「顧客を失う」公認。McKinsey中間層スクイーズ。方向性支持・速度不確定 | [INFO-043](../Information/2026-05-23/collected-raw.md#INFO-043) [INFO-044](../Information/2026-05-23/collected-raw.md#INFO-044) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | CVE-2026-22561 DLL hijacking（A-1）。クライアントサイド脆弱性A-1開示。新規大規模実被害なし。攻撃面拡大基調継続。critical移行条件未到達。high/rising | 2026-05-29 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Gemini 3.5 Flash/3.1 Pro Preview（A-1）+Gemini Omni動画生成。新モデル定量ベンチマーク待ち。「真の理解」検証未解決。elevated/stable | 2026-05-29 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | Fortune 500 <15エージェント（B-3）+88%失敗（C-3）+Gartner 150K予測（B-2）。68pt採用ギャップ構造的固定化。high/rising | 2026-05-29 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 97M（B-2）+SKILL.md 40K+（B-2）+OpenAI Skills Beta open standard（A-1）。標準化爆発的進展継続。上昇トレンド確定的。high/rising | 2026-05-29 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Altman 2025-2028（C-3）+Hassabis ~2030（C-3）。主観-客観乖離継続。新規客観的ベンチマークなし。elevated/rising | 2026-05-29 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | US DC $50B/yr（B-3）+McKinsey $5.2T（B-3）+Anthropic $65B（A-1）。資本流入劇的加速。Anthropic $65Bは単一企業過去最大。物理的制約ギャップ確定的。high/rising | 2026-05-29 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | SCR指定継続（A-2）+Trump EO撤回（B-2）+Pope回勅（A-1）+EU multi-agent規制（C-3）+CVE-2026-22561（A-1）。能力向上とリスク治理後退の同時進行。6重蓄積加速。high/rising | 2026-05-29 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-29 | Arbiter v3.92完了反映。H-GOV-001 -1%（A-1品質I証拠5件累積否定）・H-GOO-002 -1%（围い込み22件・開放C 21R不在）・H-ANT-002 ±0%（概念混同是正）・H-ANT-001上限条件再設計実行。Pattern E「構造的二面性の継続」格下げ（確度: 中）。Pattern F「臨界点接近」確度中-高。Anthropic $965B・Opus 4.8・KPMG 276K・Trust Center。OpenAI Skills Beta・gpt-oss-120b/20b。Google Managed Agents API・Interactions API。CVE-2026-22561。SCN-003 5R連続±0%警告。全20仮説・7指標更新反映して全面書き直し | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004) [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) | H-GOV-001 51→50%・H-GOO-002 32→31%・H-ANT-002 64%据え置き・SCN全件±0%（15/27/37/21%）・BS-001 17%据え置き・BS-002 3%据え置き |
| 2026-05-28 | Arbiter v3.91完了反映。「政府-市場ギャップ」再定義。Pattern B「構造的深化」格下げ。Pattern C「加速する構造的トレンド」格下げ。H-GOV-001 -1%・H-GOO-001 -1%・H-GOO-002 -1%・H-XAI-002 -1%・H-CAR-001 +1%・SCN-001 -1%。Vertex AI→Gemini Enterprise Agent Platform。Grok Build正式発売。LLM価格$30→$1-5。ByteDance $30B。KPMG/BCG A-2品質雇用予測。全20仮説・7指標更新反映して全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) | SCN-001 16→15%・SCN-002 27%据え置き・SCN-003 36→37%・SCN-004 21%据え置き・BS-001 17%据え置き・H-GOV-001 52→51%・H-GOO-001 54→53%・H-GOO-002 33→32%・H-XAI-002 62→61%・H-BTD-002 54→51%・H-CAR-001 30→31% |
| 2026-05-23 | Arbiter v3.86完了反映・INFO-069因果チェーンA-2確認・Epoch AI 9x-900x/年・Anthropic $10.9B・Goldman Sachs 66GW・Google围い込み17件・Big Tech $420B・H-GOO-001 +1%・H-GOO-002 -1%・H-BTD-002 -1%・H-CAR-001 +1%・全20仮説表示・7指標更新反映して全面書き直し | [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) | SCN-001 17→16%・SCN-002 27%据え置き・SCN-003 36%据え置き・SCN-004 20→21%・H-GOO-001 53→54%・H-GOO-002 36→35%·H-BTD-002 55→54%·H-CAR-001 27→28%·BS-001 17%据え置き |
| 2026-05-22 | SCN-004逆転SCN-001・API価格-67%・Pentagon A-2x2・Google围い込み16件・Erdős反証・世界支出$2.52T・H-CAR-001 +1%・H-ANT-001 -1%・H-GOO-002 -1%・H-BTD-002 -1%反映して全面書き直し | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | SCN-001 18→17%・SCN-002 28→27%・SCN-003 35→36%・SCN-004 19→20%(SCN-001逆転) |
| 2026-05-21 | QHG Y軸再定義採用・17R凍結解除・新確率体系反映・プレイヤー表更新 | Arbiter v3.84 Y軸再定義採用 | QHG 16R未定義→17R解除・SCN-001 20→18%・SCN-002 30→28%・SCN-003 35%据え置き・SCN-004 15→19% |

---

## 7. ブラインドスポット

- 「政府-市場ギャップ」は安全性インセンティブ構造の根本的矛盾を示すが、この二重構造がいつどちらに崩れるかの判定基準が不在。Pattern E「構造的二面性の継続」格下げは表現の保守化だが、格下げ前の「結晶化」が確証バイアスを強化していた期間の影響が過去の確度変更に残存している可能性。50%到達で方向性不明確化が定着した。
- H-ANT-001上限条件再設計が実行されたが（新: 上位3要因以内）、17R累積ペナルティ構造問題の根本原因（「安全性直接C」の定義曖昧さ）が完全に解決されたかは次回Arbiterでの検証が必要。KPMG 276KのH-ANT-001再分類も判定基準の一貫性を問う。
- SCN-003は5R連続±0%で警告発出済み。次回±0%で-1%自動適用条件が設定されているが、围い込みI蓄積と開放標準爆発的進展の真正な方向混成が続く場合、QHG軸区別能力消失リスクが増大する。18R目のQHG再定義を次回最優先強制実行する。
- OpenAI Skills Betaがopen standard準拠で発表されたことはH-OAI-002围い込み否定の強力なCだが、Skills/Shell/Compactionの独自実行環境围い込みは同時進行している。「開放標準＋围い込み実装」パターンの下で、MCP上の固有拡張がどの程度の围い込み力を持つかの定量的評価が不在。
- CVE-2026-22561（A-1品質DLL hijacking）はクライアントサイド脆弱性として新段階を示すが、この脆弱性が実際に悪用された場合の市場・規制への波及効果評価が不在。Sandbox Runtime OSS（防御側）との非対称性分析が必要。
- KPMG 64%/71%とBCG 50-55%はA-2品質の「予測」であり「実績」ではない。KPMG/BCGのコンサルティング利害関係（AI導入推進で利益を得る）が予測の客観性に与える影響を品質コードに組み込む必要がある。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral等の台頭は「5社フレーム」自体の妥当性を問う結果である。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) | Anthropic Series H $65B・$965B評価額(A-1) |
| [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) | KPMG 276K名Claude統合(A-1) |
| [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004) | Google Managed Agents API(A-1) |
| [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) | Google Interactions API・Gemini 3.5 Flash/3.1 Pro Preview(A-1) |
| [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) | CVE-2026-22561 DLL hijacking・Trust Center包括認証(A-1) |
| [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) | OpenAI Skills Beta open standard準拠(A-1) |
| [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) | o3引退8/26(A-3) |
| [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) | OpenAI Pentagon受益(A-2) |
| [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) | SCR指定継続(A-2) |
| [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) | Trump EO撤回(B-2) |
| [INFO-020](../Information/2026-05-29/collected-raw.md#INFO-020) | Fortune 500 <15エージェント(B-3) |
| [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021) | 88%エージェント失敗(C-3) |
| [INFO-025](../Information/2026-05-29/collected-raw.md#INFO-025) | US DC $50B/yr・McKinsey $5.2T(B-3) |
| [INFO-041](../Information/2026-05-29/collected-raw.md#INFO-041) | Gartner 150K予測(B-2) |
| [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) | gpt-oss-120b/20b(A-3) |
| [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) | Pope回勅(A-1) |
| [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) | Claude Opus 4.8(A-1) |
| [INFO-046](../Information/2026-05-29/collected-raw.md#INFO-046) | Anthropic Milan/Seoul開設(A-3) |
| [INFO-037](../Information/2026-05-29/collected-raw.md#INFO-037) | EU multi-agent規制(C-3) |
| [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) | Anthropic $380B評価額・OpenAI Pentagon漁夫の利・Mythos恐喝能力(B-2) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B Anthropic投資検討・Anthropic 70%直接対決勝利(B-3) |
| [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) | LLM API価格$30→$1-5/MTok(C-3) |
| [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) | ByteDance $30B・豆包 > ChatGPT中国・DeepSeek 75%カット(B-3) |
| [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) | KPMG 64%/71%採用変更(A-2) |
| [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) | BCG 50-55%米国職業再編(A-2) |
| [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) | Vertex AI → Gemini Enterprise Agent Platform移行(C-3) |
| [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) | Grok Build正式発売(A-3) |
| [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) | Reuters: Grok DL 60%減(B-2) |
| [Arbiter v3.92](../state/arbiter-2026-05-29.md) | 確度評価の完全根拠 |
| [Arbiter v3.91](../state/arbiter-2026-05-28.md) | 前回確度評価の完全根拠 |
