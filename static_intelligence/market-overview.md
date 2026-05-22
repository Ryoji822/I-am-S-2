# AI市場全体 — 静的インテリジェンス

> 最終判断更新: 2026-05-22
> 全体確信度: 中
> 情報非対称性: ByteDance / DeepSeek のグローバルシェア追跡が困難。2nd tier (Mistral / Cohere) の動向が5社比較に入っていない。QHG Y軸再定義がArbiter v3.84で採用され、v3.84以降の確率体系はv3.83以前と非整合のため推移比較に注意
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-001](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-22時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.6, Sonnet 4.6, Mythos, Claude Code | $900B+評価額(A-2) | 3位 (94) | PwC 30,000名Claude訓練(A-2) [INFO-053](../Information/2026-05-22/collected-raw.md#INFO-053)。Stainless買収 [INFO-009](../Information/2026-05-22/collected-raw.md#INFO-009)。SCR指定で政府市場喪失 [INFO-024](../Information/2026-05-22/collected-raw.md#INFO-024) |
| OpenAI | GPT-5.5, Codex, Daybreak, DeployCo | $730B IPO評価額(B-3) | 4位 (92) | Pentagon契約獲得(A-2) [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048)。Erdős予想反証(A-3) [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006)。GPT-5.5 $5/$30 [INFO-029](../Information/2026-05-22/collected-raw.md#INFO-029) |
| Google | Gemini 3.5 Flash, Omni, Antigravity 2.0, Spark | Cloud $20B/63% YoY | 1位 (98) | I/O 2026: 100件発表 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007)。WebMCP標準提案。MCP Atlas 83.6%。围い込み16件 |
| SpaceXAI | Grok 4.3, Grok Build CLI | SpaceX $250BがxAI買収 | 2位 (95) | Grok Build Beta [INFO-010](../Information/2026-05-22/collected-raw.md#INFO-010)。市場採用データ不在継続 |
| ByteDance | 豆包2.0, Coze 2.5, Seedance 2.0 | CAPEX ¥200B+(A-3) | 非公開 | 豆包MAU 345M(A-3) [INFO-054](../Information/2026-05-22/collected-raw.md#INFO-054)。CAPEX ¥200B増額 [INFO-050](../Information/2026-05-22/collected-raw.md#INFO-050)。有料化開始 |

---

## 0. 一文要約

PentagonがAnthropic代替のAIモデルテストを開始し、OpenAIが契約を獲得した [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049)。Google I/O 2026で100件の発表があり [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007)、围い込み項目が16件に蓄積した。OpenAIがErdős予想を反証する数学的ブレイクスルーを達成した [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006)。API価格が全主要プロバイダーで-67%下落し [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031)、コモディティ化が加速する構造的トレンドになっている。SCN-004「誰でもAI」が20%に上昇しSCN-001「围い込みの勝者」17%を初めて逆転した [scenarios.json](../config/scenarios.json)。SCN-003「静かな围い込み」が36%で最高確率を維持する。

---

## 1. コア判断

市場の構図は三重構造に深化した。「価格コモディティ化の加速」「围い込みの多面的深化」「シナリオ階層の再編」が同時進行している。

API価格-67%下落は加速する構造的トレンドである。全主要プロバイダーで価格が下落し [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031)、GPT-5.5が$5/$30 per million tokensで提供される [INFO-029](../Information/2026-05-22/collected-raw.md#INFO-029)。フロンティア差別化の持続性というQHG Y軸の前提を直接侵食する。価格構造の変化は围い込みの価値自体を減殺し、SCN-003とSCN-004を同時に強化する方向で作用している。

SCN-004がSCN-001を初めて逆転した。SCN-004「誰でもAI」が20%(+1%)に上昇し、SCN-001「围い込みの勝者」17%(-1%)を順位で上回った [scenarios.json](../config/scenarios.json)。これはコモディティ化+開放の組み合わせが、围い込み+差別化持続よりも蓋然性が高いことを示す。-67%価格下落とMCP 1,300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) がSCN-004を支える一方、围い込み16件蓄積とGoogle I/O 100件発表がSCN-003を36%に押し上げている。SCN-001は围い込みCがあるものの、価格コモディティ化で差別化持続前提が侵食されている。

围い込みは16件に蓄積した。Google I/O 2026でAntigravity 2.0, Managed Agents API, Gemini Spark, WebMCP標準提案が追加され [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007)、開放C証拠が16R連続で不在である。H-GOO-002は36%に低下した [H-GOO-002](../config/hypotheses.json)。しかし围い込みの質は「エコシステム深度による暗黙的固定化」であり、価格コモディティ化と围い込み深化が同時進行するSCN-003の力学そのものを示している。

Pentagon-Anthropic構造的対立が新段階に入った。PentagonがAnthropic代替モデルのテストを開始し(A-2) [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048)、Task ForceがCyber Command/NSA向けAI展開を決定した(A-2) [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049)。OpenAIが契約を獲得した。因果チェーンはSCR指定→代替調達→OpenAI契約だが、各段階の因果性は多段的であり、各段階の信頼性は未検証である。Pattern Aを中-高に据え置く。H-GOV-001は52%据え置き [H-GOV-001](../config/hypotheses.json)。AnthropicのPwC 30,000名訓練(A-2) [INFO-053](../Information/2026-05-22/collected-raw.md#INFO-053) は萎縮効果と矛盾する同品質の反証であり、「矛盾する2つの真実」の均衡が継続している。

Erdős予想反証は研究マイルストーンだが単一分野である。OpenAIの汎用推論モデルが80年前の離散幾何学予想を反証し [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006)、Fields賞受賞者Gowersが「Annals of Mathematics掲載推薦レベル」と評価した。しかしAGI到達度指標(IND-028)はARC-AGI-3 <1%未到達で、主観-客観乖離が継続する [IND-028](../config/indicators.json)。

世界AI支出が$2.52Tに達した。Brookings分析で2025年$1.75Tから44% YoY成長 [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052)。Big Tech $725B投資 [INFO-043](../Information/2026-05-22/collected-raw.md#INFO-043) とByteDance ¥200B増額 [INFO-050](../Information/2026-05-22/collected-raw.md#INFO-050) で資本集中が加速している。AI露出業種の雇用12-15%減少がA-2品質で確認された [INFO-046](../Information/2026-05-22/collected-raw.md#INFO-046)。H-CAR-001は27%(+1%)に上昇した [H-CAR-001](../config/hypotheses.json)。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Pentagon代替テスト+OpenAI契約+Task Force設立(A-2×2) | SCR→代替調達→OpenAI契約の因果チェーン。各段階多段的。Pattern A中-高据え置き | A-2 | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049) |
| 高 | API価格-67%全主要プロバイダー下落 | 加速する構造的トレンド。フロンティア差別化持続前提の侵食。SCN-004逆転の根拠 | C-3 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) |
| 高 | Google I/O 2026: 100件発表・围い込み16件目 | 围い込み多面的深化。SCN-003 36%の根拠強化。H-GOO-002 36%低下 | A-3 | [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) |
| 高 | SCN-004(20%)がSCN-001(17%)を初逆転 | コモディティ化+開放が围い込み+差別化持続より蓋然性高い。価格構造変化が順位逆転の主因 | 統合判断 | [scenarios.json](../config/scenarios.json) |
| 高 | OpenAI Erdős予想反証(A-3)・Gowers推薦レベル | AI数学研究の画期的成果。汎用推論モデル。但し単一分野。AGI指標はARC-AGI-3 <1% | A-3 | [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) |
| 高 | 世界AI支出$2.52T・44% YoY(A-2) + Big Tech $725B | 資本流入劇的加速。IND-029 high維持の根拠 | A-2/B-3 | [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) [INFO-043](../Information/2026-05-22/collected-raw.md#INFO-043) |
| 高 | PwC 30,000名Claude訓練・CoE設立(A-2) | エンタープライズ深度の具体的証拠。萎縮効果(A-2)と直接矛盾する同品質反証 | A-2 | [INFO-053](../Information/2026-05-22/collected-raw.md#INFO-053) |
| 高 | 79%導入vs11%本番+METR 43%乖離+失敗6:成功1 | エージェント本番環境信頼性の構造化。IND-026 high維持 | A-3/B-3 | [INFO-021](../Information/2026-05-22/collected-raw.md#INFO-021) [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) |
| 高 | AI露出業種雇用12-15%減少(A-2 CNBC) | H-CAR-001 +1%(26→27%)の定量C。30%閾値には遠い | A-2 | [INFO-046](../Information/2026-05-22/collected-raw.md#INFO-046) |
| 中 | MCP 1,300本番サーバー+WebMCP標準提案 | 標準化爆発的加速。SCN-004支持要因 | C-3/A-3 | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) |
| 中 | 豆包MAU 345M・有料化開始(A-3) + CAPEX ¥200B増額 | ByteDance中国市場圧倒的優位。有料化はH-BTD-002のI。H-BTD-001 64%据え置き | A-3 | [INFO-054](../Information/2026-05-22/collected-raw.md#INFO-054) [INFO-050](../Information/2026-05-22/collected-raw.md#INFO-050) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | 「加速する構造的トレンド」判断が崩れ、SCN-004の前提が弱体化する | 180日 | [IND-001](../config/indicators.json) |
| SCN-001がSCN-004を再度逆転する | コモディティ化+開放の優位判断が一時的変動の可能性。围い込み+差別化復活の根拠 | 180日 | [scenarios.json](../config/scenarios.json) |
| OSS性能が再びフロンティアから8pt以上離れる | 「OSSギャップ消滅」判断が崩れ、SCN-002前提が復活する | 180日 | [IND-001](../config/indicators.json) |
| Pentagon SCR指定が法的に無効化されAnthropicの政府市場アクセスが回復する | H-GOV-001の萎縮効果前提が崩れる | 180日 | [IND-030](../config/indicators.json) |
| Google围い込み項目の蓄積が止まり、開放C証拠が3件以上出現する | H-GOO-002 16R不在の前提が崩れ、SCN-003支持要因が弱体化 | 180日 | [IND-027](../config/indicators.json) |
| CAPEX過剰投資が$500B以下に修正される | 「過剰投資 hanging」判断が崩れ、資本集中の持続可能性前提が変わる | 180日 | [IND-029](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 62% | Pentagon契約(A-2)は強力C。18件I蓄積と1ラウンドC>Iでは打破過大。コモディティ化下での「支配」定義未解決 | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-029](../Information/2026-05-22/collected-raw.md#INFO-029) | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-032](../Information/2026-05-22/collected-raw.md#INFO-032) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 46% | 围い込み否定16件蓄積。low帯確定。OSSギャップ消滅がマルチモデル採用を加速 | (围い込み証拠不在継続) | (開放C蓄積継続) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 52% | Pentagon A-2品質2件C。Anthropic提訴+PwC 30,000名(A-2)+Bengio予防原則がI。「矛盾する2つの真実」均衡継続 | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049) | [INFO-053](../Information/2026-05-22/collected-raw.md#INFO-053) [INFO-040](../Information/2026-05-22/collected-raw.md#INFO-040) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 47% | 18R連続上限条件未充足の累積的ペナルティ。安全性直接CではないPwCでの相殺は論理的でない。medium帯下限に接近 | [INFO-053](../Information/2026-05-22/collected-raw.md#INFO-053) | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-038](../Information/2026-05-22/collected-raw.md#INFO-038) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 63% | GitHub 4%コミット+Walleye 100%は強力C。Grok Build Beta競合+SDK分離課金がI。安定観察 | [INFO-009](../Information/2026-05-22/collected-raw.md#INFO-009) | [INFO-008](../Information/2026-05-22/collected-raw.md#INFO-008) [INFO-010](../Information/2026-05-22/collected-raw.md#INFO-010) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 53% | Google I/O 100件は初の強力な反証として記録。16R代替説明未解決。次回反証継続で+1%条件設定 | [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) | (代替説明未解決継続) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し围い込みを回避する | 36% | 围い込み16件I蓄積。開放C 16R連続不在。low帯深化 | (围い込みI蓄積継続) | (開放C不在継続) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持する | 64% | 豆包MAU 345M+CAPEX ¥200B増額は中国市場genuine C。グローバル展開Cは実質1件。ミラーイメージングリスク | [INFO-054](../Information/2026-05-22/collected-raw.md#INFO-054) [INFO-050](../Information/2026-05-22/collected-raw.md#INFO-050) | (グローバル展開制約継続) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 55% | 豆包有料化開始(A-3)は低価格戦略に直接反する。業界-67%価格下落で独自性希薄化。累積I 13件目 | [INFO-054](../Information/2026-05-22/collected-raw.md#INFO-054) | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 56% | Grok 4.1 LMArena首位は性能C。但し性能≠市場成功。市場採用データ2R連続ゼロ | [INFO-010](../Information/2026-05-22/collected-raw.md#INFO-010) | (市場採用データ不在) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 27% | AI露出業種雇用12-15%減少(A-2)の定量C。30%閾値には遠い。low範囲内 | [INFO-046](../Information/2026-05-22/collected-raw.md#INFO-046) | (30%閾値遠い) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | ジュニア採用67%減+ミドル/シニアAI需要上昇の構造的裏付け。METR 43%破損は反証。C/I相殺。69%上限 | [INFO-045](../Information/2026-05-22/collected-raw.md#INFO-045) | [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | 中間工程排除C蓄積。76%監査不可+15%ROI達成は監査 gaps の裏付け。方向性支持・速度不確定 | [INFO-043](../Information/2026-05-22/collected-raw.md#INFO-043) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で high | Gemini 3.5 Flash AIME 73.3% [INFO-030](../Information/2026-05-22/collected-raw.md#INFO-030)。Deep Think HLE 41%。BenchLM上位差縮小。high水準 | 2026-05-22 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | 88%エンタープライズインシデント(C-3) [INFO-011](../Information/2026-05-22/collected-raw.md#INFO-011)。攻撃面拡大加速。high水準 | 2026-05-22 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Gemini 3.5 Flash AIME 73.3% [INFO-030](../Information/2026-05-22/collected-raw.md#INFO-030) + Deep Think HLE 41% [INFO-036](../Information/2026-05-22/collected-raw.md#INFO-036)。ベンチマーク大幅改善。「真の理解」検証未解決。elevated水準 | 2026-05-22 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | 79%導入vs11%本番 [INFO-021](../Information/2026-05-22/collected-raw.md#INFO-021) + METR 43%乖離 [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) + AI生産性不十分(A-2) [INFO-042](../Information/2026-05-22/collected-raw.md#INFO-042)。失敗6:成功1でhigh維持 | 2026-05-22 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 1,300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) + WebMCP標準提案 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007)。標準化爆発的加速。high水準 | 2026-05-22 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Erdős予想反証(A-3) [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) + Hassabis AGI 5-10年(A-3) [INFO-033](../Information/2026-05-22/collected-raw.md#INFO-033)。数学研究画期的。但し単一分野。ARC-AGI-3 <1%。elevated水準 | 2026-05-22 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | $725B Big Tech [INFO-043](../Information/2026-05-22/collected-raw.md#INFO-043) + $2.52T世界支出44% YoY(A-2) [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052)。資本流入劇的加速。high水準 | 2026-05-22 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Pentagon代替テスト(A-2) [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) + Task Force(A-2) [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049) + 大統領令(C-3) [INFO-025](../Information/2026-05-22/collected-raw.md#INFO-025)。A-2品質2件確認。high維持 | 2026-05-22 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-22 | SCN-004逆転SCN-001・API価格-67%・Pentagon A-2×2・Google围い込み16件・Erdős反証・世界支出$2.52T・H-CAR-001 +1%・H-ANT-001 -1%・H-GOO-002 -1%・H-BTD-002 -1%反映して全面書き直し | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) [INFO-046](../Information/2026-05-22/collected-raw.md#INFO-046) | SCN-001 18→17%・SCN-002 28→27%・SCN-003 35→36%・SCN-004 19→20%(SCN-001逆転)・H-ANT-001 48→47%・H-GOO-002 37→36%・H-BTD-002 56→55%・H-CAR-001 26→27%・Pattern A 高→中-高・Pattern C「臨界点」→「加速する構造的トレンド」・BS-001 17%据え置き(v3.83から) |
| 2026-05-21 | QHG Y軸再定義採用・17R凍結解除・新確率体系反映・プレイヤー表更新 | Arbiter v3.84 Y軸再定義採用 | QHG 16R未定義→17R解除・SCN-001 20→18%・SCN-002 30→28%・SCN-003 35%据え置き・SCN-004 15→19% |
| 2026-05-20 | Anthropic $900B+OpenAI逆転+Gemini 3.5 Flash+Co-Scientist+兵器ルールA-2昇格+IND-026 high移行+Pattern C「多極化」フレーム修正 | [INFO-032](../Information/2026-05-20/collected-raw.md#INFO-032) [INFO-015](../Information/2026-05-20/collected-raw.md#INFO-015) [INFO-053](../Information/2026-05-20/collected-raw.md#INFO-053) [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) | H-OAI-001 63→62%・H-GOO-002 38→37%・H-GOV-001 52%据え置き・IND-026 elevated→high・Pattern A中-高→中 |

---

## 7. ブラインドスポット

- H-GOV-001 52%とAnthropic $900B評価額+PwC 30,000名訓練(A-2)の同時存在が最大の分析課題。萎縮効果で安全性が低下する(GOV)という読みと、安全性差別化で評価額に達する(ANT)という読みが論理的緊張関係にある。「矛盾する2つの真実」の均衡がいつ崩れるかの判定基準が不足している。
- SCN-004のSCN-001逆転が1ラウンドの変動か、構造的転換点かの区別が不可能。-67%価格下落が持続するか、フロンティアモデルが再びプレミアムを確立するかの分岐を監視する必要がある。
- Pentagon SCR→代替テスト→OpenAI契約の因果チェーンは各段階が多段的であり、各段階の信頼性が未検証である。SCR指定が契約喪失の十分条件か、必要条件か、あるいは独立事象かの判別ができていない。
- QHG Y軸再定義で確率体系は更新されたが、「フロンティア差別化持続性」の定量化手法が未確立であり、Y軸判定への主観依存度が高い。v3.84以前との推移比較ができないため、傾向分析の連続性が失われた。
- $2.52T世界AI支出の内訳が不明確。分散投資(業界全体インフラ整備)ならSCN-004支持、集中投資(少数プレイヤーへの資本集中)ならSCN-003支持となるが、配分比率の定量データがない。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Cohere Command A+ OSS [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) は「5社フレーム」自体の妥当性を問う結果である。
- Erdős予想反証の研究インパクト評価が不十分。単一分野のブレイクスルーをAGI進歩の代理指標とする危険性と、汎用推論モデルの汎用性証明としての意義の評価バランスが未確立。
- METR 43%本番破損とPwC 70%納期短縮の矛盾が未解決。両者のスケールの非対称性を認識しつつ、品質問題の波及範囲を評価できない。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) | Bloomberg: Pentagon代替テスト・OpenAI契約(A-2) |
| [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049) | Politico: Pentagon Task Force Cyber/NSA(A-2) |
| [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) | OpenAI: Erdős予想反証(A-3) |
| [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) | Google I/O 2026: 100件発表・Gemini 3.5 Flash・Antigravity 2.0・WebMCP |
| [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) | API価格-67%全社下落(C-3) |
| [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) | Brookings: 世界AI支出$2.52T・44% YoY(A-2) |
| [INFO-050](../Information/2026-05-22/collected-raw.md#INFO-050) | ByteDance CAPEX ¥200B増額(A-3) |
| [INFO-054](../Information/2026-05-22/collected-raw.md#INFO-054) | 豆包MAU 345M・有料化開始(A-3) |
| [INFO-053](../Information/2026-05-22/collected-raw.md#INFO-053) | PwC 30,000名Claude訓練・CoE設立(A-2) |
| [INFO-029](../Information/2026-05-22/collected-raw.md#INFO-029) | GPT-5.5価格$5/$30 per million tokens(A-3) |
| [INFO-046](../Information/2026-05-22/collected-raw.md#INFO-046) | CNBC: AI露出業種雇用12-15%減少(A-2) |
| [INFO-043](../Information/2026-05-22/collected-raw.md#INFO-043) | Big Tech $725B AI投資・92,000人テック解雇(B-3) |
| [INFO-021](../Information/2026-05-22/collected-raw.md#INFO-021) | Microsoft WTI: 79%導入vs11%本番・18倍増(B-3) |
| [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) | METR Frontier Risk: 43%乖離(A-3) |
| [INFO-042](../Information/2026-05-22/collected-raw.md#INFO-042) | Forbes: AI生産性だけでは不十分(A-2) |
| [INFO-011](../Information/2026-05-22/collected-raw.md#INFO-011) | 88%エンタープライズインシデント(C-3) |
| [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) | MCP 1,300本番サーバー(C-3) |
| [INFO-030](../Information/2026-05-22/collected-raw.md#INFO-030) | Gemini 3.5 Flash AIME 73.3%・GPQA 74.2%(A-3) |
| [INFO-033](../Information/2026-05-22/collected-raw.md#INFO-033) | Hassabis AGI 5-10年(A-3) |
| [INFO-025](../Information/2026-05-22/collected-raw.md#INFO-025) | Trump AI審査大統領令(C-3) |
| [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) | Cohere Command A+ OSS(A-3) |
| [INFO-009](../Information/2026-05-22/collected-raw.md#INFO-009) | Anthropic Stainless買収(A-3) |
| [INFO-045](../Information/2026-05-22/collected-raw.md#INFO-045) | コーディング価値シフト(B-3) |
| [Arbiter v3.85](../state/arbiter-2026-05-22.md) | 確度評価の完全根拠 |
