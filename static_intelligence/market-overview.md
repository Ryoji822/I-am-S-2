# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-05-31
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。QHG Y軸v3.84以降とv3.83以前は非整合
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-05-31時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.8, Sonnet 4.6, Claude Code | $965B評価額(A-1) | 3位 | Karpathy入社 [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052). Mythos一般公開 [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051). Series H $65B [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013). KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002). SCR指定継続. H-ANT-001 42% |
| OpenAI | GPT-5.5, Codex, Skills Beta | $730B評価額(A-2) | 1位 (Elo 1502) | H-OAI-001 58%. Skills Beta open standard準拠 [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008). Pentagon受益 [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016). gpt-oss-120b/20b [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) |
| Google | Gemini 3.5, Gemini Omni, 3.5 Flash | Cloud $20B/63% YoY | 2位 | 围い込み23件. Gemini Omni/3.5 Flash [INFO-007](../Information/2026-05-31/collected-raw.md#INFO-007). Managed Agents API [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004). H-GOO-002 29% |
| SpaceXAI | Grok 4.3, Grok Build | $20B調達(B-3) | 4位 | H-XAI-002 61%. 前回更新から構造的変化なし. DL 60%減で苦戦継続 |
| ByteDance | 豆包2.0, Coze 2.5, Seedance 2.1 | $30B(B-3) | 非公開 | 前回更新から構造的変化なし. DeepSeek価格圧力継続 |

---

## 0. 一文要約

SCN-004がSCN-002と同率25%で順位逆転し、差別化持続とコモディティ化の境界が曖昧化した [scenarios.json](../config/scenarios.json)。SCN-003は35%（-2%）で最高確率を維持し、SCN-001は15%据え置きである。H-GOV-001は48%（-2%/2R）に低下し、Pattern J「市場が安全性を評価する」が論理的飛躍（Red採用）と判定されて中確度に格下げされた [H-GOV-001](../config/hypotheses.json)。H-ANT-001は42%（-2%）でlow帯深化が進行する [H-ANT-001](../config/hypotheses.json)。H-GOO-002は29%（-2%）に低下し、围い込み23件蓄積で開放Cが23R連続不在となった [H-GOO-002](../config/hypotheses.json)。H-OAI-001は58%（-2%）に低下した [H-OAI-001](../config/hypotheses.json)。H-CAR-001は32%（+1%）に上昇し、Stanford 22-25歳16%相対雇用減 [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) がA-2品質Cとして蓄積した [H-CAR-001](../config/hypotheses.json)。IND-030がelevated→highに移行し8重蓄積に達した。Mythos一般公開 [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) が能力-リスク二面性を具体化した。Pattern H（投資膨張vs ROI空洞化）が確度高、Pattern I（エントリーレベル雇用危機）が確度高となり、Pattern G/Jは中に格下げされた。

---

## 1. コア判断

H-GOV-001は48%（-2%/2R）に低下した。6R連続-1%が継続し、I側A-1（$965B評価額）とA-2（Mythos一般公開・裁判所）の累積がmedium帯下限に接近させている。Pattern J「市場が安全性を評価する」が論理的飛躍（Red採用）と判定され、中確度に格下げされた。$965B評価額は商業ポテンシャルへの評価であり安全性スタンスへの評価と同義ではない。Mythos一般公開はA-2品質I側蓄積である。

H-ANT-001は42%（-2%）に低下し、H-ANT-002は64%（±0%）維持である。Pattern J downgradeが上限条件達成難易度を示唆し、low帯深化が進行する。H-ANT-002はbudget overruns [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) が否定的だが、B-2品質単一ソース構造的リスクを抱える。

Google围い込みが23件蓄積に達した。H-GOO-002は29%（-2%）に低下し、開放Cが23R連続不在でlow帯深化が確定的である。Gemini Omni/3.5 Flash [INFO-007](../Information/2026-05-31/collected-raw.md#INFO-007) はA-3品質だが围い込みI蓄積には貢献しない。

開放標準の爆発的進展が継続している。SKILL.md 40K+・MCP 97M・AAIF 43新メンバーでIND-027 high/risingを維持する。各社独自実行環境围い込みが同時進行し、「開放標準＋围い込み実装」パターンの定着が観察される。

資本流入が劇的加速している。$7,250億capex [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) でPattern H（投資膨張vs ROI空洞化）が確度高となった。IND-029 high/risingを維持する。

雇用面ではStanford 22-25歳16%相対雇用減 [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) がA-2品質Cとして蓄積し、Pattern I（エントリーレベル雇用危機）が確度高となった。H-CAR-001は32%（+1%）に上昇する。

IND-030がelevated→highに移行した。SCR指定（A-2）+Trump EO撤回（B-2）+Pope回勅（A-1）+EU multi-agent規制（C-3）+CVE-2026-22561（A-1）+Mythos一般公開（A-2） [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) +大統領令延期+DeepMind組合化投票で8重蓄積に達した。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Pattern J downgrade「市場が安全性を評価する」論理的飛躍（Red採用） | H-ANT-001上限条件影響。$965Bは商業ポテンシャル評価≠安全性スタンス評価。H-GOV-001評価にも影響 | 統合判断 | [Arbiter v3.94](../state/arbiter-2026-05-31.md) |
| 高 | Mythos一般公開（A-2）能力-リスク二面性具体化 | IND-030 high移行。8重蓄積。H-GOV-001 I側蓄積 | A-2 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) |
| 高 | Stanford 22-25歳16%相対雇用減（A-2） | H-CAR-001 +1%。Pattern I（エントリーレベル雇用危機）確度高 | A-2 | [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) |
| 高 | Karpathy入社+Claude 78%（B-2） | INFO-052感度リスク。H-ANT-001/H-ANT-002への影響制約記録 | B-2 | [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) |
| 高 | Budget overruns Microsoft/Uber（B-2） | H-ANT-002否定的。Pattern K確度中。B-2品質単一ソース構造的リスク | B-2 | [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) |
| 高 | SCN-004 +2% rank swap（SCN-002と同率25%） | 4件直接支持+Pattern H支持。Goldman Sachs+DeepSeek+MMLU+CEOs | 統合判断 | [Arbiter v3.94](../state/arbiter-2026-05-31.md) |
| 高 | 围い込み23件蓄積。開放C 23R連続不在 | H-GOO-002 -2%（31→29%）。low帯深化確定 | A-1/C-3 | [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004) [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) |
| 高 | SKILL.md 40K+・MCP 97M・AAIF 43新メンバー | IND-027 high/rising。開放標準爆発的進展継続 | A-1/B-2 | [INFO-014](../Information/2026-05-31/collected-raw.md#INFO-014) [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) |
| 高 | $7,250億capex | IND-029 high/rising。Pattern H（投資膨張vs ROI空洞化）確度高 | B-2 | [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) |
| 中 | H-GOV-001 48%（6R連続-1%）medium帯下限接近 | I側A-1+A-2累積。Pattern J→中格下げ。次回動向注目 | 統合判断 | [Arbiter v3.94](../state/arbiter-2026-05-31.md) |

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
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 58% | Anthropic逆転3重確認+価格体系混乱。INFO-052感度制約記録。コモディティ化下での「支配」定義未解決。累積I 22件 | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) | [INFO-027](../Information/2026-05-29/collected-raw.md#INFO-027) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 45% | 围い込み否定12件蓄積。low帯確定。OSSギャップ消滅がマルチモデル採用を加速。Skills Beta open standard準拠 | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究に大規模資源を投入する | 3% | 非営利支配構造で商業収益研究還流保証。但し商業化加速で確度極低。gpt-oss-120b/20b [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) は開放CだがAGI優先とは非直結 | [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 48% | 6R連続-1%。I側A-1（$965B）+A-2（Mythos・裁判所）累積。medium帯下限に接近。Pattern J→中格下げ | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 42% | Pattern J論理的飛躍が上限条件達成難易度示唆。low帯深化。KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) は強力C（再分類） | [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) | [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 64% | ±0%維持。budget overruns [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) は否定的だがB-2品質単一ソース構造的リスク。Pattern K確度中 | (Cowork/Managed Agentsは別概念) | [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持しAWS・GCP・Azure全てで同等の機能を提供する | 6% | SpaceXAI Colossus契約でインフラ集中深化。マルチクラウド（均衡）から二重集中へ。棄却候補 | (マルチクラウド証拠不在) | [INFO-046](../Information/2026-05-29/collected-raw.md#INFO-046) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 52% | 8R連続A-3/C-3のみC蓄積。Hassabis AGI 2029はA-2品質C。アンカリング認識。代替説明「業界全体押し上げ」未解決 | [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004) [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) | [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し围い込みを回避する | 29% | 围い込み23件I蓄積。開放C 23R連続不在。low帯深化 | (围い込みI蓄積継続) | (開放C不在継続) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 49% | ±0%維持。Gemini 3.5 Flash/3.1 Pro Preview [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) A-1品質。4R条件（A-2+定量分解）未達成。方向は上向き | [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) | (DeepMind統合課題継続) |
| [H-XAI-001](../config/hypotheses.json) | xAIはXのリアルタイムデータを活用し差別化する（棄却） | 35% | 37R+証拠不在。xAI→SpaceXAI統合で独立企業前提崩壊。Grok全製品Xデータ非依存。正式棄却維持 | (証拠不在) | (全製品Xデータ非依存) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 61% | ±0%維持。DL 60%減で苦戦継続。前回更新から構造的変化なし。価格競争下でのシェア獲得難度増大 | (価格低い) | (DL減・市場採用不在) |
| [H-XAI-003](../config/hypotheses.json) | xAIはSpaceX統合で宇宙・製造業特化AIを展開する（棄却） | 35% | 38R+直接的特化AI製品証拠不在。35%到達。正式棄却維持 | (証拠不在) | (特化製品不在) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 55% | ±0%維持。Grok Build正式発売はC。但し性能≠市場成功。DL 60%減継続。市場採用データ不在 | [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持する | 64% | ±0%維持。前回更新から構造的変化なし。中国国内C圧倒的。グローバル展開C不在。ミラーイメージングリスク | (中国市場C蓄積) | (グローバル展開制約継続) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 51% | ±0%維持。DeepSeek価格圧力継続。前回更新から構造的変化なし。低価格戦略独自性希薄化 | (価格競争継続) | (DeepSeek価格圧力) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% | ±0%維持。新規著作権関連証拠なし。安定観察継続 | (著作権制約継続) | (新規証拠なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 32% | A-2品質C（Stanford 16%相対雇用減）。+1%上限。KPMG/BCG利益相反リスク認識。「予測」≠「実績」 | [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) | (矛盾信号存在) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | ±0%維持。ジュニア採用67%減+ミドル/シニアAI需要上昇の構造的裏付け。METR 43%破損は反証。C/I相殺。69%上限 | [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) [INFO-059](../Information/2026-05-23/collected-raw.md#INFO-059) | (METR本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | ±0%維持。中間工程排除C蓄積。Walmart「顧客を失う」公認。McKinsey中間層スクイーズ。方向性支持・速度不確定 | [INFO-043](../Information/2026-05-23/collected-raw.md#INFO-043) [INFO-044](../Information/2026-05-23/collected-raw.md#INFO-044) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | CVE-2026-22561 DLL hijacking（A-1）。Mythos自律エクスプロイト構築能力（A-2）。クライアントサイド脆弱性A-1開示。新規大規模実被害なし。攻撃面拡大基調継続。critical移行条件未到達。high/rising | 2026-05-31 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Gemini 3.5 Flash/3.1 Pro Preview（A-1）+Gemini Omni動画生成 [INFO-007](../Information/2026-05-31/collected-raw.md#INFO-007)。新モデル定量ベンチマーク待ち。「真の理解」検証未解決。elevated/stable | 2026-05-31 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | Fortune 500 <15エージェント（B-3）+88%失敗（C-3）+Gartner 150K予測（B-2）。68pt採用ギャップ構造的固定化。high/rising | 2026-05-31 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 97M（B-2）+SKILL.md 40K+（B-2）+OpenAI Skills Beta open standard（A-1）。標準化爆発的進展継続。上昇トレンド確定的。high/rising | 2026-05-31 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | Altman 2025-2028（C-3）+Hassabis AGI 2029 [INFO-033](../Information/2026-05-31/collected-raw.md#INFO-033)（A-2）。主観-客観乖離継続。新規客観的ベンチマークなし。elevated/rising | 2026-05-31 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | US DC $50B/yr（B-3）+McKinsey $5.2T（B-3）+Anthropic $65B（A-1）+$7,250億capex [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052)（B-2）。資本流入劇的加速。物理的制約ギャップ確定的。high/rising | 2026-05-31 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | SCR指定（A-2）+Trump EO撤回（B-2）+Pope回勅（A-1）+EU multi-agent規制（C-3）+CVE-2026-22561（A-1）+Mythos一般公開（A-2） [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) +大統領令延期+DeepMind組合化投票。8重蓄積。high/rising | 2026-05-31 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-31 | Arbiter v3.94完了反映。SCN-004 tied SCN-002(25%)順位逆転。H-GOV-001 -2%(50→48%・6R連続)・H-ANT-001 -2%(44→42%)・H-GOO-002 -2%(31→29%)・H-OAI-001 -2%(60→58%)・H-CAR-001 +1%(31→32%)。Pattern J/G確度中-高→中。Pattern H/I確度高。Mythos一般公開・Karpathy入社・budget overruns・Stanford雇用データ。IND-030 elevated→high。全20仮説・7指標更新反映して全面書き直し | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-014](../Information/2026-05-31/collected-raw.md#INFO-014) [INFO-007](../Information/2026-05-31/collected-raw.md#INFO-007) | SCN-002 27→25%・SCN-003 37→35%・SCN-004 21→25%(SCN-002と同率)・SCN-001 15%据え置き・BS-001 17%据え置き・H-GOV-001 50→48%・H-ANT-001 44→42%・H-GOO-002 31→29%・H-OAI-001 60→58%・H-CAR-001 31→32% |
| 2026-05-29 | Arbiter v3.92完了反映。H-GOV-001 -1%（A-1品質I証拠5件累積否定）・H-GOO-002 -1%（围い込み22件・開放C 21R不在）・H-ANT-002 ±0%（概念混同是正）・H-ANT-001上限条件再設計実行。Pattern E「構造的二面性の継続」格下げ（確度: 中）。Pattern F「臨界点接近」確度中-高。Anthropic $965B・Opus 4.8・KPMG 276K・Trust Center。OpenAI Skills Beta・gpt-oss-120b/20b。Google Managed Agents API・Interactions API。CVE-2026-22561。SCN-003 5R連続±0%警告。全20仮説・7指標更新反映して全面書き直し | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-29/collected-raw.md#INFO-004) [INFO-005](../Information/2026-05-29/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) | H-GOV-001 51→50%・H-GOO-002 32→31%・H-ANT-002 64%据え置き・SCN全件±0%（15/27/37/21%）・BS-001 17%据え置き・BS-002 3%据え置き |
| 2026-05-28 | Arbiter v3.91完了反映。「政府-市場ギャップ」再定義。Pattern B「構造的深化」格下げ。Pattern C「加速する構造的トレンド」格下げ。H-GOV-001 -1%・H-GOO-001 -1%・H-GOO-002 -1%・H-XAI-002 -1%・H-CAR-001 +1%・SCN-001 -1%。Vertex AI→Gemini Enterprise Agent Platform。Grok Build正式発売。LLM価格$30→$1-5。ByteDance $30B。KPMG/BCG A-2品質雇用予測。全20仮説・7指標更新反映して全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-005](../Information/2026-05-28/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-060](../Information/2026-05-28/collected-raw.md#INFO-060) [INFO-046](../Information/2026-05-28/collected-raw.md#INFO-046) [INFO-050](../Information/2026-05-28/collected-raw.md#INFO-050) | SCN-001 16→15%・SCN-002 27%据え置き・SCN-003 36→37%・SCN-004 21%据え置き・BS-001 17%据え置き・H-GOV-001 52→51%・H-GOO-001 54→53%・H-GOO-002 33→32%・H-XAI-002 62→61%・H-BTD-002 54→51%・H-CAR-001 30→31% |
| 2026-05-23 | Arbiter v3.86完了反映・INFO-069因果チェーンA-2確認・Epoch AI 9x-900x/年・Anthropic $10.9B・Goldman Sachs 66GW・Google围い込み17件・Big Tech $420B・H-GOO-001 +1%・H-GOO-002 -1%・H-BTD-002 -1%・H-CAR-001 +1%・全20仮説表示・7指標更新反映して全面書き直し | [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) | SCN-001 17→16%・SCN-002 27%据え置き・SCN-003 36%据え置き・SCN-004 20→21%・H-GOO-001 53→54%・H-GOO-002 36→35%·H-BTD-002 55→54%·H-CAR-001 27→28%·BS-001 17%据え置き |
| 2026-05-22 | SCN-004逆転SCN-001・API価格-67%・Pentagon A-2x2・Google围い込み16件・Erdős反証・世界支出$2.52T・H-CAR-001 +1%・H-ANT-001 -1%・H-GOO-002 -1%・H-BTD-002 -1%反映して全面書き直し | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-013](../Information/2026-05-23/collected-raw.md#INFO-013) [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | SCN-001 18→17%・SCN-002 28→27%・SCN-003 35→36%・SCN-004 19→20%(SCN-001逆転) |
| 2026-05-21 | QHG Y軸再定義採用・17R凍結解除・新確率体系反映・プレイヤー表更新 | Arbiter v3.84 Y軸再定義採用 | QHG 16R未定義→17R解除・SCN-001 20→18%・SCN-002 30→28%・SCN-003 35%据え置き・SCN-004 15→19% |

---

## 7. ブラインドスポット

- 「政府-市場ギャップ」は安全性インセンティブ構造の根本的矛盾を示すが、この二重構造がいつどちらに崩れるかの判定基準が不在。Pattern E「構造的二面性の継続」格下げは表現の保守化だが、格下げ前の「結晶化」が確証バイアスを強化していた期間の影響が過去の確度変更に残存している可能性。50%到達で方向性不明確化が定着した。
- Pattern J「市場が安全性を評価する」が論理的飛躍と判定された。$965B評価額は商業ポテンシャルへの評価であり安全性スタンスへの評価と同義ではない。この判定がH-ANT-001上限条件とH-GOV-001評価の両方に影響する。
- H-ANT-001上限条件再設計が実行されたが（新: 上位3要因以内）、17R累積ペナルティ構造問題の根本原因（「安全性直接C」の定義曖昧さ）が完全に解決されたかは次回Arbiterでの検証が必要。KPMG 276KのH-ANT-001再分類も判定基準の一貫性を問う。
- SCN-004 tied SCN-002(25%)は差別化持続とコモディティ化の境界が曖昧化したことを示す。Y軸(v3.84再定義)の操作的定義が22R連続未実行であり、境界判定の基盤が薄弱。QHG再定義が次回Arbiter最優先課題。
- SCN-003は5R連続±0%で警告発出済み。次回±0%で-1%自動適用条件が設定されているが、围い込みI蓄積と開放標準爆発的進展の真正な方向混成が続く場合、QHG軸区別能力消失リスクが増大する。18R目のQHG再定義を次回最優先強制実行する。
- OpenAI Skills Betaがopen standard準拠で発表されたことはH-OAI-002围い込み否定の強力なCだが、Skills/Shell/Compactionの独自実行環境围い込みは同時進行している。「開放標準＋围い込み実装」パターンの下で、MCP上の固有拡張がどの程度の围い込み力を持つかの定量的評価が不在。
- CVE-2026-22561（A-1品質DLL hijacking）はクライアントサイド脆弱性として新段階を示すが、この脆弱性が実際に悪用された場合の市場・規制への波及効果評価が不在。Sandbox Runtime OSS（防御側）との非対称性分析が必要。
- KPMG 64%/71%とBCG 50-55%はA-2品質の「予測」であり「実績」ではない。KPMG/BCGのコンサルティング利害関係（AI導入推進で利益を得る）が予測の客観性に与える影響を品質コードに組み込む必要がある。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral等の台頭は「5社フレーム」自体の妥当性を問う結果である。
- Microsoft E&DのClaude Code内部分キャンセル [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) はB-2品質単一ソース。INFO-054誤りの場合、Pattern K・H-ANT-002否定的証拠・H-OAI-001(I側)が同時に動揺する構造的リスク。

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
