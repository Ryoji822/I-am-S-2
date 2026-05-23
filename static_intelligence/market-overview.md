# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-05-23
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。QHG Y軸v3.84以降とv3.83以前は非整合
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-23時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.6, Sonnet 4.6, Mythos, Claude Code | $14B年間収益ペース(A-2) | 3位 (94) | WSJ $10.9B収益130%増 [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052)。KPMG 276K名 [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010)。Stainless買収 [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004)。Glasswing 10,000件脆弱性 [INFO-003](../Information/2026-05-23/collected-raw.md#INFO-003)。安全性拒否→SCR因果チェーンA-2確認 [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) |
| OpenAI | GPT-5.5, Codex, Daybreak, DeployCo | $182.6B評価額 | 1位 (Elo 1502) | Pentagon契約獲得(A-2) [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033)。Erdős予想反証(A-3) [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009)。GPT-5.5 $5/$30 [INFO-046](../Information/2026-05-23/collected-raw.md#INFO-046)。Codex 4M+利用者 [INFO-001](../Information/2026-05-23/collected-raw.md#INFO-001)。$1.4Tインフラ契約 [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) |
| Google | Gemini 3.5 Flash, Omni, Antigravity 2.0, Spark | Cloud $20B/63% YoY | 2位 | I/O 2026: 100件発表 [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013)。「全テック企業に宣戦布告」 [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067)。Managed Agents API [INFO-007](../Information/2026-05-23/collected-raw.md#INFO-007)。囲い込み17件蓄積 |
| SpaceXAI | Grok 4.3, Grok Build 0.1 | SpaceX $250BがxAI買収 | 4位 | Grok Build 0.1 beta [INFO-015](../Information/2026-05-23/collected-raw.md#INFO-015)。OpenCode対応 [INFO-005](../Information/2026-05-23/collected-raw.md#INFO-005)。市場採用データ不在継続 |
| ByteDance | 豆包2.0, Coze 2.5, Seedance 2.1 | 中国AI資金$16.2B Q1 | 非公開 | Seedance 2.1差し迫る [INFO-068](../Information/2026-05-23/collected-raw.md#INFO-068)。Epoch AI 9x-900x/年価格下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065)。中国Q1 $16.2B [INFO-053](../Information/2026-05-23/collected-raw.md#INFO-053) |

---

## 0. 一文要約

Anthropicが自律兵器利用を拒否しPentagonのSCR指定を受けた因果チェーンがA-2品質で確認され [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069)、H-GOV-001（萎縮効果）の最も診断的な証拠となったが、同社$14B年間収益ペース [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) が萎縮効果と直接矛盾する「2つの真実」の均衡が継続している。Epoch AIが同等性能での推論価格年9x-900x下落を報告し [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065)、コモディティ化がSCN-001を16%に押し下げSCN-004を21%に押し上げた [scenarios.json](../config/scenarios.json)。Google I/Oの「全テック企業に宣戦布告」で囲い込み17件に蓄積し [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067)、SCN-003「静かな囲い込み」が36%で最高確率を維持する。Goldman Sachs予測で米国DC電力66GW倍増 [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054)、Big Tech $420B + OpenAI $1.4Tでインフラ投資が爆発的加速 [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060)。

---

## 1. コア判断

市場の構図は四重の緊張関係に深化した。「価格コモディティ化の加速」「囲い込みの多面的深化」「安全性と商業的成功の二項対立」「インフラ爆発的投資」が同時進行している。

Epoch AI 9x-900x/年の価格下落は低価格戦略独自性を根本的に希薄化する [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065)。H-BTD-002は54%（-1%）に低下した [H-BTD-002](../config/hypotheses.json)。API価格の構造的下落はバイトダンス固有の戦略的優位ではなく、業界全体の力学である。SCN-001は16%（-1%）に低下し [scenarios.json](../config/scenarios.json)、囲い込みの差別化持続前提が価格コモディティ化で構造的に侵食されている。SCN-004は21%（+1%）に上昇し、コモディティ化+開放の組み合わせが圏い込み+差別化持続よりも蓋然性が高いことを示す。

INFO-069（A-2）でPentagon因果チェーンが確認された [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069)。Anthropicが自律兵器・大量監視目的のAI利用を拒否し、Pentagonが「all-lawful use」を要求、拒否後にSCR指定、代替調達でOpenAIが受益した。因果チェーンは安全性拒否→SCR指定→代替調達→OpenAI受益の4段階だが、メカニズム存在≠業界全体波及。H-GOV-001は52%据え置き [H-GOV-001](../config/hypotheses.json)。Anthropic $14B年間収益ペース [INFO-070](../Information/2026-05-23/collected-raw.md#INFO-070) とKPMG 276K名 [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) は萎縮効果と直接矛盾する同品質の反証であり、「矛盾する2つの真実」の均衡が継続している。

Google I/O 2026は包括的エコシステム展開だった。「全テック企業に宣戦布告」的な100件発表 [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) で囲い込み項目が17件に蓄積した。H-GOO-002は35%（-1%）に低下 [H-GOO-002](../config/hypotheses.json)、開放C証拠17R連続不在。H-GOO-001は54%（+1%）に上昇 [H-GOO-001](../config/hypotheses.json)、2R連続強力反証（I/O 100件+INFO-067包括分析）でArbiter v3.85条件を形式的充足した。

インフラ投資が爆発的加速した。Goldman Sachs予測で米国DC電力66GW倍増(A-2) [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054)、Big Tech $420B + OpenAI $1.4Tインフラ契約 [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060)、中国AI資金$16.2B Q1 [INFO-053](../Information/2026-05-23/collected-raw.md#INFO-053)。IND-029 high/rising維持 [IND-029](../config/indicators.json)。資本流入の劇的加速と物理的制約ギャップが確定的。

AI主導の人員削減がもはや株価を押し上げなくなった [INFO-041](../Information/2026-05-23/collected-raw.md#INFO-041)。Duolingo 10%・Chegg 22%・Intuit 3,000名の4業種定量C蓄積でH-CAR-001は28%（+1%）に上昇 [H-CAR-001](../config/hypotheses.json)。但し30%閾値には遠く、テック近接産業バイアスに注意。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Pentagon安全性拒否→SCR因果チェーンA-2確認 | 全追跡期間で最も診断的なC。メカニズム存在≠業界全体波及。H-GOV-001 52%据え置き | A-2 | [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) |
| 高 | Epoch AI 9x-900x/年価格下落 | 低価格戦略独自性の根本的希薄化。H-BTD-002 -1%。SCN-001 16%低下の根拠 | B-3 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) |
| 高 | Anthropic $10.9B収益130%増 + $14B年間ペース | 萎縮効果と直接矛盾。H-ANT-001 47%据え置き。「矛盾する2つの真実」継続 | A-2/B-3 | [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-070](../Information/2026-05-23/collected-raw.md#INFO-070) |
| 高 | Google I/O 100件+「全テック企業に宣戦布告」 | 囲い込み17件蓄積。H-GOO-001 +1%・H-GOO-002 -1%。SCN-003 36%の根拠強化 | A-3/B-3 | [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) |
| 高 | SCN-001 16%低下・SCN-004 21%上昇 | 価格コモディティ化が圏い込み価値基盤を構造的に侵食。コモディティ化+開放が優位 | 統合判断 | [scenarios.json](../config/scenarios.json) |
| 高 | Goldman Sachs 66GW倍増 + Big Tech $420B + OpenAI $1.4T | インフラ投資爆発的加速。IND-029 high/rising。物理的制約ギャップ確定的 | A-2/B-3 | [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) |
| 高 | KPMG 276K名Claude統合 + Glasswing 10,000件脆弱性 | エンタープライズ深度の具体的証拠。Stainless買収でMCP生態系強化 | A-3 | [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) [INFO-003](../Information/2026-05-23/collected-raw.md#INFO-003) [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) |
| 高 | Fortune 500 150K+ Agent・10%ガバナンス + 88%インシデント | エージェント無秩序拡大。IND-026 high。IND-013 high | C-3 | [INFO-030](../Information/2026-05-23/collected-raw.md#INFO-030) [INFO-016](../Information/2026-05-23/collected-raw.md#INFO-016) |
| 高 | AIレイオフが株価押し上げなくなった（Duolingo 10%等） | H-CAR-001 +1%の定量C。4業種蓄積。30%閾値には遠い | B-3 | [INFO-041](../Information/2026-05-23/collected-raw.md#INFO-041) |
| 中 | MCP 1,300本番サーバー + Confluent GA + Chrome DevTools | 標準化爆発的加速継続。SCN-004支持要因。IND-027 high | C-3/A-3 | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023) [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) |
| 中 | 中国AI資金$16.2B Q1・Seedance 2.1差し迫る | ByteDance中国市場圧倒的優位。H-BTD-001 64%据え置き | B-2/C-3 | [INFO-053](../Information/2026-05-23/collected-raw.md#INFO-053) [INFO-068](../Information/2026-05-23/collected-raw.md#INFO-068) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | 「加速する構造的トレンド」判断が崩れ、SCN-004の前提が弱体化する | 180日 | [IND-025](../config/indicators.json) |
| SCN-001がSCN-004を再度逆転する | コモディティ化+開放の優位判断が一時的変動の可能性。圏い込み+差別化復活の根拠 | 180日 | [scenarios.json](../config/scenarios.json) |
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-025](../config/indicators.json) |
| Pentagon SCR指定が法的に無効化されAnthropicの政府市場アクセスが回復する | H-GOV-001の萎縮効果前提が崩れる | 180日 | [IND-030](../config/indicators.json) |
| Google圏い込み項目の蓄積が止まり、開放C証拠が3件以上出現する | H-GOO-002 17R不在の前提が崩れ、SCN-003支持要因が弱体化 | 180日 | [IND-027](../config/indicators.json) |
| 因果チェーン第4段階（他社安全性方針変更）のA-2品質確認 | H-GOV-001の+1%条件充足。萎縮効果が業界全体に波及した証拠 | 180日 | [IND-030](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 62% | Pentagon契約(A-2)は強力C。18件I蓄積と1ラウンドC>Iでは打破過大。コモディティ化下での「支配」定義未解決 | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) [INFO-001](../Information/2026-05-23/collected-raw.md#INFO-001) [INFO-046](../Information/2026-05-23/collected-raw.md#INFO-046) | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を圏い込む | 46% | 圏い込み否定12件蓄積。low帯確定。OSSギャップ消滅がマルチモデル採用を加速 | (圏い込み証拠不在継続) | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-029](../Information/2026-05-23/collected-raw.md#INFO-029) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究に大規模資源を投入する | 3% | 非営利支配構造で商業収益研究還流保証。但し商業化加速で確度極低 | [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 52% | INFO-069（A-2）因果チェーン確認は最も診断的なC。但しメカニズム存在≠業界全体波及。C/I均衡継続（新規C 8件 vs 新規I 4件） | [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-035](../Information/2026-05-23/collected-raw.md#INFO-035) | [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 47% | INFO-069因果確認は安全性が商業的帰結の原因であるgenuine C。但し19R連続上限条件未充足。商業的成功Cの多くは安全性直接Cではない | [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) [INFO-003](../Information/2026-05-23/collected-raw.md#INFO-003) | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 63% | GitHub 4%コミット+Walleye 100%は強力C。Grok Build Beta競合+SDK分離課金がI。安定観察 | [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) [INFO-025](../Information/2026-05-23/collected-raw.md#INFO-025) | [INFO-015](../Information/2026-05-23/collected-raw.md#INFO-015) [INFO-005](../Information/2026-05-23/collected-raw.md#INFO-005) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持しAWS・GCP・Azure全てで同等の機能を提供する | 6% | SpaceXAI Colossus契約でインフラ集中深化。マルチクラウド（均衡）から二重集中へ。棄却候補 | (マルチクラウド証拠不在) | [INFO-014](../Information/2026-05-23/collected-raw.md#INFO-014) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 54% | Arbiter v3.85条件「次回も反証継続で+1%」形式的充足。2R連続強力反証。次回条件: 3R連続反証で更に+1% | [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) | (代替説明未解決継続) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し圏い込みを回避する | 35% | 圏い込み17件I蓄積。「全テック企業に宣戦布告」（INFO-067）。開放C 17R連続不在。low帯深化 | (圏い込みI蓄積継続) | (開放C不在継続) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% | Gemma 4+第8世代TPU+Gemini Enterprise Agent Platformはgenuine C。DeepMind union問題新規証拠なし。ペナルティ停止後安定化 | [INFO-007](../Information/2026-05-23/collected-raw.md#INFO-007) [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) | (DeepMind統合課題継続) |
| [H-XAI-001](../config/hypotheses.json) | xAIはXのリアルタイムデータを活用し差別化する（棄却） | 35% | 37R+証拠不在。xAI→SpaceXAI統合で独立企業前提崩壊。Grok全製品Xデータ非依存。正式棄却維持 | (証拠不在) | (全製品Xデータ非依存) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 63% | Grok STT $0.10/時間+Flash Lite $0.125の価格競争C。DeepSeek V4 8ヶ月遅れは格差維持C | [INFO-015](../Information/2026-05-23/collected-raw.md#INFO-015) | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) |
| [H-XAI-003](../config/hypotheses.json) | xAIはSpaceX統合で宇宙・製造業特化AIを展開する（棄却） | 35% | 38R+直接的特化AI製品証拠不在。35%到達。正式棄却維持 | (証拠不在) | (特化製品不在) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 56% | Grok 4.1 LMArena首位は性能C。但し性能≠市場成功。市場採用データ2R連続ゼロ | [INFO-015](../Information/2026-05-23/collected-raw.md#INFO-015) [INFO-005](../Information/2026-05-23/collected-raw.md#INFO-005) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持する | 64% | 豆包MAU 345M+CAPEX ¥200B増額は中国市場genuine C。グローバル展開Cは実質1件。ミラーイメージングリスク | [INFO-068](../Information/2026-05-23/collected-raw.md#INFO-068) [INFO-053](../Information/2026-05-23/collected-raw.md#INFO-053) | (グローバル展開制約継続) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 54% | Epoch AI 9x-900x/年価格下落が低価格戦略独自性を根本的に希薄化。DeepSeek V4 OSSも価格破壊圧力。累積I 16件 | [INFO-053](../Information/2026-05-23/collected-raw.md#INFO-053) | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% | 新規著作権関連証拠なし。安定観察継続 | (著作権制約継続) | (新規証拠なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 28% | 4業種定量C蓄積（Duolingo 10%・Chegg 22%・Intuit 3,000名・広告reset）。30%閾値には遠い。low範囲内 | [INFO-041](../Information/2026-05-23/collected-raw.md#INFO-041) | (30%閾値遠い) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | ジュニア採用67%減+ミドル/シニアAI需要上昇の構造的裏付け。METR 43%破損は反証。C/I相殺。69%上限 | [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) [INFO-059](../Information/2026-05-23/collected-raw.md#INFO-059) | (METR本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | 中間工程排除C蓄積。Walmart「顧客を失う」公認 [INFO-043]。McKinsey中間層スクイーズ。方向性支持・速度不確定 | [INFO-043](../Information/2026-05-23/collected-raw.md#INFO-043) [INFO-044](../Information/2026-05-23/collected-raw.md#INFO-044) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | 88%エンタープライズインシデント(C-3) [INFO-016](../Information/2026-05-23/collected-raw.md#INFO-016) + Pentagon武器化(B-3) [INFO-039](../Information/2026-05-23/collected-raw.md#INFO-039) + Claude Codeサンドボックスバイパス(C-3) [INFO-019](../Information/2026-05-23/collected-raw.md#INFO-019)。攻撃面拡大加速。high/rising | 2026-05-23 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | GPT-5.5 Vals Multimodal Index 67.77%首位(B-3) [INFO-026](../Information/2026-05-23/collected-raw.md#INFO-026) + Nova Sonic音声Agent(A-3) [INFO-027](../Information/2026-05-23/collected-raw.md#INFO-027) + MMMU Pro人間専門家0.3pt差。量的向上継続。「真の理解」検証未解決。elevated/stable | 2026-05-23 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | Fortune 500 150K+ Agent・10%のみガバナンス(C-3) [INFO-030](../Information/2026-05-23/collected-raw.md#INFO-030) + パイロット→本番失敗(C-3) [INFO-032](../Information/2026-05-23/collected-raw.md#INFO-032) + 88%インシデント(C-3) [INFO-016](../Information/2026-05-23/collected-raw.md#INFO-016)。無秩序拡大と本番品質乖離拡大。high/rising | 2026-05-23 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 1,300本番サーバー(C-3) [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) + Confluent MCP GA(B-3) [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023) + Hugging Face Agent Leaderboard(A-3) [INFO-049](../Information/2026-05-23/collected-raw.md#INFO-049) + Chrome DevTools for Agents(A-3) [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022)。標準化爆発的加速継続。high/rising | 2026-05-23 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Erdős予想反証(A-3) [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) + Kokotajlo 2027超人間AI警告(B-3) [INFO-064](../Information/2026-05-23/collected-raw.md#INFO-064) + ARC-AGI 7Mモデル2倍(C-3) [INFO-061](../Information/2026-05-23/collected-raw.md#INFO-061)。数学研究で qualitative leap。但し単一分野。主観-客観乖離継続。elevated/rising | 2026-05-23 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | Goldman Sachs 66GW倍増(A-2) [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) + Big Tech $420B(B-3) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) + OpenAI $1.4T(B-3) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) + 中国$16.2B Q1(B-2) [INFO-053](../Information/2026-05-23/collected-raw.md#INFO-053)。資本流入劇的加速。high/rising | 2026-05-23 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Anthropic安全性拒否→SCR因果チェーンA-2確認 [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) + Pentagon武器化(B-3) [INFO-039](../Information/2026-05-23/collected-raw.md#INFO-039) + 7社機密契約(B-3) [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038) + $200M/社(B-3) [INFO-071](../Information/2026-05-23/collected-raw.md#INFO-071)。A-2品質因果チェーン確認で能力-リスク二面性の新段階。high/rising | 2026-05-23 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-23 | Arbiter v3.86完了反映・INFO-069因果チェーンA-2確認・Epoch AI 9x-900x/年・Anthropic $10.9B・Goldman Sachs 66GW・Google囲い込み17件・Big Tech $420B・H-GOO-001 +1%・H-GOO-002 -1%・H-BTD-002 -1%・H-CAR-001 +1%・全20仮説表示・7指標更新反映して全面書き直し | [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) | SCN-001 17→16%・SCN-002 27%据え置き・SCN-003 36%据え置き・SCN-004 20→21%・H-GOO-001 53→54%・H-GOO-002 36→35%・H-BTD-002 55→54%・H-CAR-001 27→28%・BS-001 17%据え置き・Pattern A確度中-高据え置き |
| 2026-05-22 | SCN-004逆転SCN-001・API価格-67%・Pentagon A-2×2・Google囲い込み16件・Erdős反証・世界支出$2.52T・H-CAR-001 +1%・H-ANT-001 -1%・H-GOO-002 -1%・H-BTD-002 -1%反映して全面書き直し | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | SCN-001 18→17%・SCN-002 28→27%・SCN-003 35→36%・SCN-004 19→20%(SCN-001逆転) |
| 2026-05-21 | QHG Y軸再定義採用・17R凍結解除・新確率体系反映・プレイヤー表更新 | Arbiter v3.84 Y軸再定義採用 | QHG 16R未定義→17R解除・SCN-001 20→18%・SCN-002 30→28%・SCN-003 35%据え置き・SCN-004 15→19% |
| 2026-05-20 | Anthropic $900B+OpenAI逆転+Gemini 3.5 Flash+兵器ルールA-2昇格+IND-026 high移行+Pattern C修正 | [INFO-032](../Information/2026-05-23/collected-raw.md#INFO-032) | H-OAI-001 63→62%・H-GOO-002 38→37%・IND-026 elevated→high |

---

## 7. ブラインドスポット

- H-GOV-001 52%とAnthropic $14B年間収益ペース+KPMG 276K名(A-3)の同時存在が最大の分析課題。萎縮効果で安全性が低下する(GOV)という読みと、安全性差別化で$14Bに達する(ANT)という読みが論理的緊張関係にある。「矛盾する2つの真実」の均衡がいつ崩れるかの判定基準が不足している。
- SCN-001 16%とSCN-004 21%の差が5%に縮小。Epoch AI 9x-900x/年の価格下落が持続するか、フロンティアモデルが再びプレミアムを確立するかの分岐を監視する必要がある。
- INFO-069（A-2）因果チェーンは最も診断的なCだが、各段階の信頼性が多段的。SCR指定が契約喪失の十分条件か、必要条件か、あるいは独立事象かの判別は依然不明確。
- QHG Y軸再定義で確率体系は更新されたが、「フロンティア差別化持続性」の定量化手法が未確立であり、Y軸判定への主観依存度が高い。v3.84以前との推移比較ができないため傾向分析の連続性が失われた。
- $420B Big Tech投資+$1.4T OpenAIインフラの配分比率が不明確。分散投資ならSCN-004支持、集中投資ならSCN-003支持となるが、定量データがない。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral $14B+SAP提携 [INFO-051](../Information/2026-05-23/collected-raw.md#INFO-051) は「5社フレーム」自体の妥当性を問う結果である。
- Erdős予想反証の研究インパクト評価が不十分。単一分野のブレイクスルーをAGI進歩の代理指標とする危険性と、汎用推論モデルの汎用性証明としての意義の評価バランスが未確立。
- METR 43%本番破損とPwC 70%納期短縮の矛盾が未解決。両者のスケールの非対称性を認識しつつ、品質問題の波及範囲を評価できない。
- Fortune 500 150K+ Agentと10%ガバナンスの乖離が示唆する「無秩序拡大」リスクの評価枠組みが不在。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) | Yahoo/CNBC/Instagram: Anthropic安全性拒否→SCR因果チェーンA-2確認 |
| [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) | Epoch AI: トークン価格年9x-900x下落・10x production problem(B-3) |
| [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) | WSJ: Anthropic $10.9B収益130%増・初営業利益(A-2) |
| [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) | Goldman Sachs: 米国DC電力66GW倍増(A-2) |
| [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) | Big Tech $420B・OpenAI $1.4Tインフラ(B-3) |
| [INFO-053](../Information/2026-05-23/collected-raw.md#INFO-053) | SCMP: 中国AI資金$16.2B Q1(B-2) |
| [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) | Google I/O包括分析「全テック企業に宣戦布告」(B-3) |
| [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) | Google I/O 2026: 100件発表・Agentic Gemini Era(A-3) |
| [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | OpenAI: Erdős予想反証(A-3) |
| [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) | Bloomberg: Pentagon代替テスト(A-2) |
| [INFO-035](../Information/2026-05-23/collected-raw.md#INFO-035) | Politico: Pentagon Task Force Cyber/NSA(A-2) |
| [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | Bloomberg: 控訴裁Anthropic SCR懐疑的(A-2) |
| [INFO-010](../Information/2026-05-23/collected-raw.md#INFO-010) | KPMG 276K名Claude統合(A-3) |
| [INFO-003](../Information/2026-05-23/collected-raw.md#INFO-003) | Anthropic: Glasswing 10,000件脆弱性(A-3) |
| [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) | Anthropic: Stainless買収(A-3) |
| [INFO-046](../Information/2026-05-23/collected-raw.md#INFO-046) | GPT-5.5価格$5/$30 per million tokens(A-3) |
| [INFO-016](../Information/2026-05-23/collected-raw.md#INFO-016) | 88%エンタープライズインシデント(C-3) |
| [INFO-030](../Information/2026-05-23/collected-raw.md#INFO-030) | Fortune 500 150K+ Agent・10%ガバナンス(C-3) |
| [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) | MCP 1,300本番サーバー(C-3) |
| [INFO-041](../Information/2026-05-23/collected-raw.md#INFO-041) | AIレイオフ株価押し上げ消失(B-3) |
| [INFO-068](../Information/2026-05-23/collected-raw.md#INFO-068) | ByteDance Seedance 2.1差し迫る(C-3) |
| [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) | DeepSeek V4・Gemma 4オープンモデルラッシュ(B-3) |
| [INFO-007](../Information/2026-05-23/collected-raw.md#INFO-007) | Google Managed Agents API(A-3) |
| [INFO-070](../Information/2026-05-23/collected-raw.md#INFO-070) | Anthropic $14B年間収益ペース(B-3) |
| [INFO-039](../Information/2026-05-23/collected-raw.md#INFO-039) | Pentagon AI武器化計画(B-3) |
| [INFO-071](../Information/2026-05-23/collected-raw.md#INFO-071) | Pentagon $200M/社AI契約拡大(B-3) |
| [INFO-026](../Information/2026-05-23/collected-raw.md#INFO-026) | GPT-5.5 Vals 67.77%首位(B-3) |
| [INFO-064](../Information/2026-05-23/collected-raw.md#INFO-064) | Kokotajlo 2027超人間AI警告(B-3) |
| [INFO-043](../Information/2026-05-23/collected-raw.md#INFO-043) | Walmart Agent仲介排除公認(C-3) |
| [INFO-044](../Information/2026-05-23/collected-raw.md#INFO-044) | McKinsey: Agentic AI中間層スクイーズ(B-3) |
| [Arbiter v3.86](../state/arbiter-2026-05-23.md) | 確度評価の完全根拠 |
