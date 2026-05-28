# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-05-28
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。QHG Y軸v3.84以降とv3.83以前は非整合
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-28時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.6, Sonnet 4.6, Mythos, Claude Code | $380B評価額(B-2) | 3位 (94) | Google $40B投資検討 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。70%直接対決勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。SCR指定後も商業的躍進継続。Mythos恐喝能力確認 [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) |
| OpenAI | GPT-5.5, Codex, Daybreak, DeployCo | $380B評価額 | 1位 (Elo 1502) | Pentagon空洞化数時間後に契約獲得 [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)。「漁夫の利」定量具現化。Codex 4M+利用者 [INFO-001](../Information/2026-05-23/collected-raw.md#INFO-001)。GPT-5.5 $5/$30 [INFO-046](../Information/2026-05-23/collected-raw.md#INFO-046) |
| Google | Gemini 3.5, Antigravity 2.0, Spark, Enterprise Agent Platform | Cloud $20B/63% YoY | 2位 | Vertex AI → Gemini Enterprise Agent Platform移行 [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005)。围い込み20件蓄積。Google $40B Anthropic投資検討 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) |
| SpaceXAI | Grok 4.3, Grok Build | $20B調達(B-3) | 4位 | Grok Build正式発売 [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006)。DL 60%減で価格競争I [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058)。市場採用データ不在継続 |
| ByteDance | 豆包2.0, Coze 2.5, Seedance 2.1 | $30B(B-3) | 非公開 | 豆包 > ChatGPT中国 [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060)。DeepSeek 75%カット [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060)。価格破壊加速 |

---

## 0. 一文要約

Anthropic安全性拒否→SCR指定の因果チェーンが「政府-市場ギャップ」として再定義された [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)。政府は安全性スタンスを罰するが市場は評価するという二重構造で、萎縮効果の方向性は不明確であり、H-GOV-001は51%（-1%）に低下した [H-GOV-001](../config/hypotheses.json)。OpenAIはAnthropic拒否から数時間でPentagon契約を獲得し、安全性コストの定量具現化が確定した [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)。LLM価格$30→$1-5/MTokの95%+削減が「加速する構造的トレンド」として継続し [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038)、ByteDance $30B資金でDeepSeek 75%カットが価格破壊を加速する [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060)。KPMG 64%/71% [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) とBCG 50-55% [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) がA-2品質で雇用再編を予測し、H-CAR-001は31%（+1%）に上昇した。Google围い込みはVertex AI → Gemini Enterprise Agent Platform移行で20件蓄積 [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005)、SCN-003「静かな围い込み」が37%で最高確率を維持する。

---

## 1. コア判断

市場の構図は「政府-市場ギャップ」の顕在化が最大の構造的洞察となった。Arbiter v3.91は安全性二面性を「構造的深化」に格下げした（旧「決定的顕在化」）。Red指摘の通り、B-2品質SCR証拠で「決定的」宣言は品質基準に反し、同一事象がH-ANT-001とH-GOV-001の両方に「極高」診断的価値を持つなら鑑別能力は低い。安全性「機能」（KPMG 276K名・$380B評価額・70%勝利）vs安全性「スタンス」（SCR・$200M喪失・一切商取rr禁止）が同時に極限発現しており、これはAI業界の安全性インセンティブ構造の根本的矛盾を具現化している。

H-GOV-001は51%（-1%）に低下した。Anthropic商業成功4件I（$380B評価額 [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)・70%直接対決勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)・App Store首位・Google $40B投資検討 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)）が萎縮効果命題を根本的に否定する方向で加重された。「矛盾する2つの真実」は「政府-市場ギャップ」への再理解を経て、萎縮効果の方向性そのものが不明確になった。

価格コモディティ化は「加速する構造的トレンド」に格下げされた（旧「終末期」）。API価格$30→$1-5/MTokの95%+削減 [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038)、DeepSeek 75%カット [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060)、ByteDance $30B資金で価格破壊が構造的に加速している。但しRed指摘の通り、API価格≠エコシステム価値の混同を避ける必要がある。価格下落はSCN-004も等しく支持する。SCN-001は15%（-1%）に低下し、SCN-004は21%維持、コモディティ化+開放の優位が安定した [scenarios.json](../config/scenarios.json)。

Google围い込みが多面的深化した。Vertex AI → Gemini Enterprise Agent Platform移行 [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) で围い込み20件蓄積。H-GOO-002は32%（-1%）に低下 [H-GOO-002](../config/hypotheses.json)、開放C証拠20R連続不在。H-GOO-001は53%（-1%）に低下 [H-GOO-001](../config/hypotheses.json)、6R連続A-3/C-3のみC蓄積の累積的重みでアンカリング認識。SCN-003は37%で最高確率を維持 [scenarios.json](../config/scenarios.json)。

AI主導雇用再編がA-2品質の予測調査で補強された。KPMG 64%/71%採用変更 [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) とBCG 50-55%米国職業再編 [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) でH-CAR-001は31%（+1%）に上昇した [H-CAR-001](../config/hypotheses.json)。但し「予測」≠「実績」の区別とKPMG/BCG利益相反リスクを認識する。Grok Build正式発売 [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) はSpaceXAIのエンタープライズ参入だが、DL 60%減 [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) でH-XAI-002は61%（-1%）に低下した [H-XAI-002](../config/hypotheses.json)。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 「政府-市場ギャップ」再定義。Anthropic安全性拒否→SCR+市場評価の二重構造 | H-GOV-001 -1%（52→51%）の根拠。萎縮効果方向性不明確化。安全性二面性「構造的深化」格下げ | B-2 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) |
| 高 | OpenAI、Anthropic拒否から数時間でPentagon契約獲得。「漁夫の利」定量具現化 | 安全性コストの定量化。H-OAI-001 60%据え置きの強力C | B-2 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) |
| 高 | LLM API価格$30→$1-5/MTok（95%+削減）。DeepSeek 75%カット。ByteDance $30B | 「加速する構造的トレンド」継続（旧「終末期」格下げ）。SCN-001 15%低下根拠。価格≠価値の区別必要 | B-3/C-3 | [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) |
| 高 | Anthropic $380B評価額・70%直接対決勝利・Google $40B投資検討 | H-GOV-001萎縮効果の根本的否定。H-ANT-001 44%据え置き。「政府-市場ギャップ」の市場側 | B-2/B-3 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) |
| 高 | Vertex AI → Gemini Enterprise Agent Platform移行。围い込み20件蓄積 | H-GOO-002 -1%（33→32%）根拠。開放C 20R不在。SCN-003 37%の根拠強化 | C-3 | [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) |
| 高 | KPMG 64%/71%採用変更 + BCG 50-55%米国職業再編 | H-CAR-001 +1%（30→31%）のA-2品質C。予測≠実績の区別必要 | A-2 | [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) |
| 高 | Grok Build正式発売 + DL 60%減（1月20M→4月8.3M） | H-XAI-002 -1%（62→61%）。発売直後短期的データ可能性注記 | A-3/B-2 | [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| 高 | Mythos恐喝能力確認。AI能力向上とリスク治理後退の同時進行 | IND-030 high/rising。能力-リスク二面性の新段階。Sandbox Runtime OSS防御側も確認 | B-2 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) |
| 中 | H-ANT-001上限条件再設計議題申し送り | 「第1位選択理由」→「上位3要因入り」再設計。17R累積ペナルティ構造問題認識 | 統合判断 | [Arbiter v3.91](../state/arbiter-2026-05-28.md) |
| 中 | 豆包 > ChatGPT中国。ByteDance $30B資金 | H-BTD-001 64%据え置き。中国国内C圧倒的。グローバル展開C不在 | B-3 | [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | 「加速する構造的トレンド」判断が崩れ、SCN-004の前提が弱体化する | 180日 | [IND-025](../config/indicators.json) |
| SCN-001がSCN-004を再度逆転する | コモディティ化+開放の優位判断が一時的変動の可能性。围い込み+差別化復活の根拠 | 180日 | [scenarios.json](../config/scenarios.json) |
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-025](../config/indicators.json) |
| Anthropicの政府市場アクセスが回復しSCR指定が解除される | H-GOV-001萎縮効果前提が崩れる。「政府-市場ギャップ」再定義の妥当性検証 | 180日 | [IND-030](../config/indicators.json) |
| Google围い込み項目の蓄積が止まり、開放C証拠が3件以上出現する | H-GOO-002 20R不在の前提が崩れ、SCN-003支持要因が弱体化 | 180日 | [IND-027](../config/indicators.json) |
| 因果チェーン第4段階（他社安全性方針変更）のA-2品質確認 | H-GOV-001の+1%条件充足。萎縮効果が業界全体に波及した証拠 | 180日 | [IND-030](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 60% | Pentagon「漁夫の利」(B-2)は強力C。コモディティ化下での「支配」定義未解決 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-001](../Information/2026-05-23/collected-raw.md#INFO-001) [INFO-046](../Information/2026-05-23/collected-raw.md#INFO-046) | [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 45% | 围い込み否定12件蓄積。low帯確定。OSSギャップ消滅がマルチモデル採用を加速 | (围い込み証拠不在継続) | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-029](../Information/2026-05-23/collected-raw.md#INFO-029) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究に大規模資源を投入する | 3% | 非営利支配構造で商業収益研究還流保証。但し商業化加速で確度極低 | [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 51% | 「政府-市場ギャップ」再定義。政府は罰するが市場は評価する二重構造で萎縮効果方向性不明確化。B-2品質C蓄積の限界。Anthropic商業成功4件Iが根本的否定 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) | [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 44% | 安全性「機能」（70%勝利・$380B・KPMG）vs「スタンス」（SCR）の二面性。17R連続上限条件未充足。上限条件再設計次回Arbiter最優先議題 | [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 64% | GitHub 4%コミット+Walleye 100%は強力C。Sandbox OSS C・価格差I相殺。安定観察 | [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) [INFO-025](../Information/2026-05-23/collected-raw.md#INFO-025) | [INFO-015](../Information/2026-05-23/collected-raw.md#INFO-015) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持しAWS・GCP・Azure全てで同等の機能を提供する | 6% | SpaceXAI Colossus契約でインフラ集中深化。マルチクラウド（均衡）から二重集中へ。棄却候補 | (マルチクラウド証拠不在) | [INFO-014](../Information/2026-05-23/collected-raw.md#INFO-014) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 53% | 6R連続A-3/C-3のみC蓄積でアンカリング認識。-1%。代替説明「業界全体押し上げ」未解決。A-2+定量証拠取得時+1%復帰条件維持 | [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) | [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-041](../Information/2026-05-28/collected-raw.md#INFO-041) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し围い込みを回避する | 32% | 围い込み20件I蓄積（Vertex AI → Gemini Enterprise Agent Platform）。開放C 20R連続不在。low帯深化 | (围い込みI蓄積継続) | (開放C不在継続) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 49% | Gemini 3.5 GPQA 74.2%（A-3）強力C。但し4R条件（A-2+定量分解）未達成。DeepMind union問題新規証拠なし | [INFO-007](../Information/2026-05-23/collected-raw.md#INFO-007) [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) | (DeepMind統合課題継続) |
| [H-XAI-001](../config/hypotheses.json) | xAIはXのリアルタイムデータを活用し差別化する（棄却） | 35% | 37R+証拠不在。xAI→SpaceXAI統合で独立企業前提崩壊。Grok全製品Xデータ非依存。正式棄却維持 | (証拠不在) | (全製品Xデータ非依存) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 61% | Grok Build正式発売C。但しReuters B-2高品質I（DL 60%減）+価格I蓄積で-1%。発売直後短期的データ可能性注記 | [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) [INFO-042](../Information/2026-05-28/collected-raw.md#INFO-042) | [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) |
| [H-XAI-003](../config/hypotheses.json) | xAIはSpaceX統合で宇宙・製造業特化AIを展開する（棄却） | 35% | 38R+直接的特化AI製品証拠不在。35%到達。正式棄却維持 | (証拠不在) | (特化製品不在) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 55% | Grok Build正式発売C。但し性能≠市場成功。市場採用データ継続不在。製品発表のみ+1%否認 | [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持する | 64% | 豆包 > ChatGPT中国 + $30B資金は中国市場genuine C。グローバル展開Cは実質1件。ミラーイメージングリスク | [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) [INFO-053](../Information/2026-05-23/collected-raw.md#INFO-053) | (グローバル展開制約継続) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 51% | DeepSeek 75%カット+価格$30→$1-5が低価格戦略独自性を希薄化。インフレ警戒で±0%。累積I 17件 | [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) | [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% | 新規著作権関連証拠なし。安定観察継続 | (著作権制約継続) | (新規証拠なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 31% | A-2品質C蓄積（KPMG 64%/71%・BCG 50-55%）。B-3主体→A-2格上げ。但し「予測」≠「実績」。KPMG/BCG利益相反リスク認識。矛盾信号存在で+1%は上限 | [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) | [INFO-032](../Information/2026-05-23/collected-raw.md#INFO-032) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | ジュニア採用67%減+ミドル/シニアAI需要上昇の構造的裏付け。METR 43%破損は反証。C/I相殺。69%上限 | [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) [INFO-059](../Information/2026-05-23/collected-raw.md#INFO-059) | (METR本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | 中間工程排除C蓄積。Walmart「顧客を失う」公認。McKinsey中間層スクイーズ。方向性支持・速度不確定 | [INFO-043](../Information/2026-05-23/collected-raw.md#INFO-043) [INFO-044](../Information/2026-05-23/collected-raw.md#INFO-044) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Sandbox Runtime OSS防御側（INFO-017 A-3）+Claude Mythos恐喝能力（INFO-061 B-2リスク側）。攻撃面拡大基調継続。新規A-2大規模実被害なし。high/rising | 2026-05-28 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Gemini 3 Pro Deep Think 100.0%（C-3）+Gemini 3.5 AIME 73.3% GPQA 74.2%（A-3）+Grok 4.1 97.8%（C-3）+Seedance 2.0（C-3）。量的向上継続。「真の理解」検証未解決。elevated/stable | 2026-05-28 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | Fortune 500平均<15エージェント（B-3）+Klarna 700代替11分→2分（B-3）+13%のみガバナンス準備+Gartner 150K予測。68pt採用ギャップ継続。high/rising | 2026-05-28 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | SKILL.md 40K+（C-3）+MCP 97M+A2A GA（A-3）+Copilot MCP server support（A-3）+Agent Client Protocol（A-3）。標準化爆発的進展継続。high/rising | 2026-05-28 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Altman 2025-2028（B-3）+Hassabis ~2030+multi-agent科学発見自動化（C-3）。主観-客観乖離継続。科学発見自動化は新規マイルストーンだが「特定分野」性質は不変。elevated/rising | 2026-05-28 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | US DC 31→66GW・$5.2T投資必要（A-3）+ByteDance $30B（B-3）+xAI $20B（B-3）。資本流入劇的加速継続。物理的制約ギャップ確定的。high/rising | 2026-05-28 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | SCR指定+DPA強制+大統領令延期（A-2）+州規制禁止（B-3）+Claude Mythos恐喝能力（B-2）。能力向上とリスク治理後退の同時進行継続。5重蓄積。high/rising | 2026-05-28 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-28 | Arbiter v3.91完了反映。「政府-市場ギャップ」再定義。Pattern B「構造的深化」格下げ。Pattern C「加速する構造的トレンド」格下げ。H-GOV-001 -1%・H-GOO-001 -1%・H-GOO-002 -1%・H-XAI-002 -1%・H-CAR-001 +1%・SCN-001 -1%。Vertex AI→Gemini Enterprise Agent Platform。Grok Build正式発売。LLM価格$30→$1-5。ByteDance $30B。KPMG/BCG A-2品質雇用予測。全20仮説・7指標更新反映して全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) | SCN-001 16→15%・SCN-002 27%据え置き・SCN-003 36→37%・SCN-004 21%据え置き・BS-001 17%据え置き・H-GOV-001 52→51%・H-GOO-001 54→53%・H-GOO-002 33→32%・H-XAI-002 62→61%・H-BTD-002 54→51%・H-CAR-001 30→31% |
| 2026-05-23 | Arbiter v3.86完了反映・INFO-069因果チェーンA-2確認・Epoch AI 9x-900x/年・Anthropic $10.9B・Goldman Sachs 66GW・Google围い込み17件・Big Tech $420B・H-GOO-001 +1%・H-GOO-002 -1%・H-BTD-002 -1%・H-CAR-001 +1%・全20仮説表示・7指標更新反映して全面書き直し | [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) | SCN-001 17→16%・SCN-002 27%据え置き・SCN-003 36%据え置き・SCN-004 20→21%・H-GOO-001 53→54%・H-GOO-002 36→35%·H-BTD-002 55→54%·H-CAR-001 27→28%·BS-001 17%据え置き |
| 2026-05-22 | SCN-004逆転SCN-001・API価格-67%・Pentagon A-2x2・Google围い込み16件・Erdős反証・世界支出$2.52T・H-CAR-001 +1%・H-ANT-001 -1%・H-GOO-002 -1%・H-BTD-002 -1%反映して全面書き直し | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | SCN-001 18→17%・SCN-002 28→27%・SCN-003 35→36%・SCN-004 19→20%(SCN-001逆転) |
| 2026-05-21 | QHG Y軸再定義採用・17R凍結解除・新確率体系反映・プレイヤー表更新 | Arbiter v3.84 Y軸再定義採用 | QHG 16R未定義→17R解除・SCN-001 20→18%・SCN-002 30→28%・SCN-003 35%据え置き・SCN-004 15→19% |

---

## 7. ブラインドスポット

- 「政府-市場ギャップ」は安全性インセンティブ構造の根本的矛盾を示すが、この二重構造がいつどちらに崩れるかの判定基準が不在。政府ペナルティが市場評価を上回る転換点と、市場評価が政府ペナルティを無効化する転換点の双方を定量的に監視する必要がある。
- H-ANT-001上限条件「安全性が第1位選択理由」は実際の購買決定プロセスと不整合。次回Arbiterで「上位3要因入り」または「安全性除外で同等製品が存在しない」への再設計が最優先議題。17R累積ペナルティ構造問題も未解決。
- Pattern B「構造的深化」格下げとPattern C「加速する構造的トレンド」格下げは表現の保守化だが、格下げ前の「決定的顕在化」「終末期」が確証バイアスを強化していた期間の影響が過去の確度変更に残存している可能性。
- KPMG 64%/71%とBCG 50-55%はA-2品質の「予測」であり「実績」ではない。KPMG/BCGのコンサルティング利害関係（AI導入推進で利益を得る）が予測の客観性に与える影響を品質コードに組み込む必要がある。
- $420B Big Tech投資+$1.4T OpenAIインフラ+ByteDance $30B+xAI $20Bの配分比率が不明確。分散投資ならSCN-004支持、集中投資ならSCN-003支持となるが、定量データがない。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral等の台頭は「5社フレーム」自体の妥当性を問う結果である。
- Mythos恐喝能力（INFO-061 B-2）はAI能力の両義性を示すが、この能力が実際に悪用された場合の市場・規制への波及効果評価が不在。Sandbox Runtime OSS（防御側）との非対称性分析が必要。
- Grok Build DL 60%減（1月20M→4月8.3M）が発売直後の短期的データか構造的トレンドかの判別が不能。2-3ヶ月後の再評価が必要。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) | Anthropic $380B評価額・OpenAI Pentagon漁夫の利・Mythos恐喝能力(B-2) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B Anthropic投資検討・Anthropic 70%直接対決勝利(B-3) |
| [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) | LLM API価格$30→$1-5/MTok(C-3) |
| [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) | ByteDance $30B・豆包 > ChatGPT中国・DeepSeek 75%カット(B-3) |
| [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) | KPMG 64%/71%採用変更(A-2) |
| [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) | BCG 50-55%米国職業再編(A-2) |
| [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) | Vertex AI → Gemini Enterprise Agent Platform移行(C-3) |
| [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) | Grok Build正式発売(A-3) |
| [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) | Reuters: Grok DL 60%減(B-2) |
| [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) | SCR指定+DPA強制(A-2) |
| [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) | Anthropic安全性拒否→SCR因果チェーンA-2確認 |
| [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) | Epoch AI: トークン価格年9x-900x下落(B-3) |
| [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) | WSJ: Anthropic $10.9B収益130%増(A-2) |
| [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) | Goldman Sachs: 米国DC電力66GW倍増(A-2) |
| [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) | Big Tech $420B・OpenAI $1.4Tインフラ(B-3) |
| [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) | Google I/O包括分析「全テック企業に宣戦布告」(B-3) |
| [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) | Google I/O 2026: 100件発表(A-3) |
| [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | OpenAI: Erdős予想反証(A-3) |
| [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) | Bloomberg: Pentagon代替テスト(A-2) |
| [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) | KPMG 276K名Claude統合(A-3) |
| [INFO-003](../Information/2026-05-23/collected-raw.md#INFO-003) | Anthropic: Glasswing 10,000件脆弱性(A-3) |
| [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) | Anthropic: Stainless買収(A-3) |
| [Arbiter v3.91](../state/arbiter-2026-05-28.md) | 確度評価の完全根拠 |
| [Arbiter v3.86](../state/arbiter-2026-05-23.md) | 前回確度評価の完全根拠 |
