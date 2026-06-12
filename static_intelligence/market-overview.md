# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-06-12
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。QHG Y軸v3.84以降とv3.83以前は非整合。QHG再定義39R連続未実行。品質調整方法論のRed Agent採用率75%がメタレベル変化。DEGRADED状態でArbiter独自批判分析（Red Agent失敗）
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-06-12時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Fable 5, Mythos 5, Opus 4.8, Sonnet 4.6, Claude Code | $65B調達・$965B評価額(A-1) | FrontierCode首位(Cognition評価) | Fable 5/Mythos 5一般公開・$10/M入力・FrontierCode首位 [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006)・Glasswing 10K+脆弱性発見 [INFO-008](../Information/2026-06-12/collected-raw.md#INFO-008)・Microsoft Foundry統合 [INFO-032](../Information/2026-06-12/collected-raw.md#INFO-032)・UK政府提携 [INFO-015](../Information/2026-06-12/collected-raw.md#INFO-015)・自律兵器拒否 [INFO-022](../Information/2026-06-12/collected-raw.md#INFO-022). 秋IPO予定 [INFO-029](../Information/2026-06-12/collected-raw.md#INFO-029). H-ANT-001 38% |
| OpenAI | GPT-5.5, Codex, Skills Beta | $852B評価額(C-1)・年間収益$25B(A-2) | ARC-AGI 2首位(85%)・GPT-5 ARC 96.3% [INFO-021](../Information/2026-06-12/collected-raw.md#INFO-021) | 機密S-1提出 [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003)・Phase 3宣言・2028年3月AI研究自動化 [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004)・Ona買収・Codex 5M週間ユーザー [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001)・Oracle Cloud提携 [INFO-002](../Information/2026-06-12/collected-raw.md#INFO-002)・Visa提携 [INFO-028](../Information/2026-06-12/collected-raw.md#INFO-028)・価格引き下げ検討 [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019)・Codex 6役割別プラグイン [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005). H-OAI-001 56% |
| Google | Gemini 3.1 Pro, 3.5 Flash, DiffusionGemma | Cloud $4,600億バックログ(A-1)・Capex $180-190B(A-3) | LMArena Elo首位(1501) | DiffusionGemma 4倍高速化 [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014)・Skill Registry/RAG Engine [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044)・Gemini 3.1 Pro [INFO-018](../Information/2026-06-12/collected-raw.md#INFO-018)・Agentic Gemini宣言 [INFO-013](../Information/2026-06-12/collected-raw.md#INFO-013). H-GOO-001 47% low. H-GOO-002 23% |
| SpaceXAI | Grok 4.3, Grok Build | $20B調達(B-3) | 4位 | Grok Build Plugin Marketplace [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010)・eToro提携・リアルタイム市場センチメント [INFO-011](../Information/2026-06-12/collected-raw.md#INFO-011)・Gopuff Go agent [INFO-012](../Information/2026-06-12/collected-raw.md#INFO-012). H-XAI-002 59%. エコシステム拡大中 |
| ByteDance | 豆包2.0, Coze 2.5, DeerFlow 2.0, Seedance 2.1 | CAPEX 2000億元に上方修正(B-2) | 非公開 | Coze 2.5 Agent World [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016)・DeerFlow 2.0スーパーエージェント [INFO-017](../Information/2026-06-12/collected-raw.md#INFO-017)・豆包MAU 610万減 [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035)・有料化KPI評価対象外 [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035). H-BTD-002 46% |

---

## 0. 一文要約

SCN-004「誰でもAI」がSCN-003「静かな囲い込み」を抜いて首位に立った（30% vs 29%）。パターンNN「価格コモディティ化の不可逆的加速」（確度中-高）が7件の価格圧力シグナルを同時蓄積し、QHG Y軸「フロンティア差別化の持続性」を直接侵食している。OpenAI価格引き下げ検討 [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019)（B-3品質）、OSS LLMが商用モデルの89%に到達 [INFO-027](../Information/2026-06-12/collected-raw.md#INFO-027)（C-3品質）、LindyのAnthropic→DeepSeek切り替え [INFO-037](../Information/2026-06-12/collected-raw.md#INFO-037)（C-3品質）が同時出現した。パターンMM「エコシステム囲い込みの同時創発」（確度中）では、Codex Plugins [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005)・Grok Build Marketplace [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010)・Gemini Skill Registry [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044)・Coze 2.5 Agent World [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016)・SkillsMP [INFO-049](../Information/2026-06-12/collected-raw.md#INFO-049)の5社が同時期にスキルマーケットプレイスを構築した。[H-GOO-001](../config/hypotheses.json)が48→47%でmedium→low移行した。19R連続で代替説明「業界全体押し上げ」が未解決のまま、I=0が確証バイアスの構造的徴候と判断された。Claude Fable 5/Mythos 5 [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006)（A-3品質）はフロンティア性能競争の継続を示すが、Fable 5価格$10/M入力はコモディティ化圧力と矛盾しない。OpenAIの構造的変化（S-1提出 [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003)・Phase 3宣言 [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004)・Ona買収 [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001)）はパターンPP「IPO競争が安全性・商業性トレードオフに与える影響」（確度低-中）の前提条件を充足した。

---

## 1. コア判断

SCN-004が首位に立った背景には、パターンNN「価格コモディティ化の不可逆的加速」がある。7件の価格圧力シグナルが同時に蓄積した: (1) OpenAI価格引き下げ検討 [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019)（B-3品質・WSJ報道）(2) 2026年8回のOpenAI価格改定 [INFO-020](../Information/2026-06-12/collected-raw.md#INFO-020)（C-3品質）(3) OSS LLM商用モデル89%到達 [INFO-027](../Information/2026-06-12/collected-raw.md#INFO-027)（C-3品質）(4) DeepSeek V4 Pro NIST評価で米国モデルと比較 [INFO-030](../Information/2026-06-12/collected-raw.md#INFO-030)（C-3品質）(5) LindyのAnthropic→DeepSeek切り替え [INFO-037](../Information/2026-06-12/collected-raw.md#INFO-037)（C-3品質）(6) Fortune 500月額推論コスト数千万ドル [INFO-046](../Information/2026-06-12/collected-raw.md#INFO-046)（C-3品質）(7) Fable 5価格$10/M入力でMythos Previewの半額以下 [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006)（A-3品質）。個別の品質はB-3/C-3中心だが、7件の同時蓄積はQHG Y軸「フロンティア差別化の持続性」への構造的圧力として評価できる。確度は中-高とする。

パターンMM「エコシステム囲い込みの同時創発」はSCN-004（開放×コモディティ化）とSCN-003（閉鎖×コモディティ化）の境界を複雑化する。Codex Plugins [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005)・Grok Build Marketplace [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010)・Gemini Skill Registry [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044)・Coze 2.5 Agent World [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016)・SkillsMP [INFO-049](../Information/2026-06-12/collected-raw.md#INFO-049)の5プラットフォームが同時期にスキル配布インフラを構築した。これは囲い込み（QHG X軸左方向）と標準化（同右方向）の同時進行を意味する。MCP RC公開 [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036)とAAIF [INFO-043](../Information/2026-06-12/collected-raw.md#INFO-043)が標準化を推進する一方で、各社の独自スキルマーケットプレイスは囲い込み圧力として機能する。SCN-004とSCN-003の差が1%（30% vs 29%）に縮小しているのは、この二方向の同時進行を反映している。

[H-GOO-001](../config/hypotheses.json)がmedium→low移行した（48→47%）。v4.05で設定された条件「48%維持でmedium→low移行検討」が発動した。DiffusionGemma [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014)（A-3品質）は強力なCだが、19R連続で代替説明「業界全体押し上げ」が未解決であり、I=0の連続は確証バイアスの構造的徴候と判断された。low移行はGoogle固有寄与の定量分解（KIQ-GOO-001: AWS/Azure同時期成長率比較）が充足されればmedium復帰可能。パターンQQ「AIレイオフ ブーメラン効果」（確度中）では、Klarna・IBM等がAI導入後の人間再雇用に転じている [INFO-026](../Information/2026-06-12/collected-raw.md#INFO-026)（C-3品質）。Korn Ferry調査で41%が管理層削減と回答 [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042)（B-3品質）。BCGは「大半の企業がAI投資から意味ある収益を得られず」と評価 [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038)（B-3品質）。過度なAI導入の逆効果がH-CAR-001因果ギャップと関連する。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | OpenAI価格引き下げ検討・2026年8回価格改定 | パターンNN直接根拠。フロンティア価格決定力の構造的低下 | B-3 | [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019) [INFO-020](../Information/2026-06-12/collected-raw.md#INFO-020) |
| 高 | OSS LLM商用モデル89%到達・DeepSeek V4 Pro NIST比較 | SCN-004首位の直接根拠。フロンティア差別化の持続性を侵食 | C-3 | [INFO-027](../Information/2026-06-12/collected-raw.md#INFO-027) [INFO-030](../Information/2026-06-12/collected-raw.md#INFO-030) |
| 高 | 5社スキルマーケットプレイス同時構築 | パターンMM直接根拠。囲い込みと標準化の同時進行 | A-3 | [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) [INFO-049](../Information/2026-06-12/collected-raw.md#INFO-049) |
| 高 | Claude Fable 5/Mythos 5一般公開・$10/M入力・FrontierCode首位 | フロンティア性能競争継続。価格半減はコモディティ化圧力と両立 | A-3 | [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006) |
| 高 | OpenAI S-1提出・Phase 3宣言・Ona買収・Codex 5M WAU | OpenAI構造的変化の多面的確認。パターンPP前提条件充足 | A-3 | [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001) |
| 高 | H-GOO-001 medium→low移行（48→47%） | Google固有優位性の定量分解不可が19R連続で未解決 | Arbiter | [H-GOO-001](../config/hypotheses.json) |
| 高 | 豆包MAU 610万減少・有料化KPI評価対象外 | H-BTD-002低価格戦略維持への直接反証。low帯深化 | C-3 | [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) |
| 高 | Lindy Anthropic→DeepSeek切り替え | パターンNN補強。エージェントプラットフォーム業界のコスト圧力 | C-3 | [INFO-037](../Information/2026-06-12/collected-raw.md#INFO-037) |
| 高 | DiffusionGemma 4倍高速化 | H-GOO-001強力Cだが代替説明未解決。H-GOO-003もC方向 | A-3 | [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014) |
| 高 | WH EO先進AI・NSPM-11同時署名 | H-GOV-001 C方向。IND-030 high維持の直接根拠 | A-3 | [INFO-023](../Information/2026-06-12/collected-raw.md#INFO-023) [INFO-045](../Information/2026-06-12/collected-raw.md#INFO-045) |
| 中 | AIレイオフブーメラン効果・41%管理層削減 | パターンQQ直接根拠。H-CAR-001因果ギャップ関連 | B-3 | [INFO-026](../Information/2026-06-12/collected-raw.md#INFO-026) [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) |
| 中 | BCG「大半がAI投資から意味ある収益未達」 | IND-026 highのI方向。期待-実態ギャップ定量確認 | B-3 | [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) |
| 中 | Gartner 40%エンタープライズエージェント・McKinsey 62%試験中 | IND-026 highのC方向。採用率急速拡大の定量確認 | B-3 | [INFO-025](../Information/2026-06-12/collected-raw.md#INFO-025) [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) |
| 中 | MCP RC公開・AAIF 6ヶ月振り返り | IND-027 high維持。標準化と囲い込みの同時進行 | B-3 | [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036) [INFO-043](../Information/2026-06-12/collected-raw.md#INFO-043) |
| 中 | Visa-OpenAI提携・Mastercard Agent Pay | エージェントコマース決済インフラ競争。排他性言及なし | B-3 | [INFO-028](../Information/2026-06-12/collected-raw.md#INFO-028) [INFO-041](../Information/2026-06-12/collected-raw.md#INFO-041) |
| 中 | ARC-AGI-3 GPT-5 96.3%・ベンチマーク飽和議論 | IND-028 high維持。主観-客観乖離の新段階 | C-3 | [INFO-021](../Information/2026-06-12/collected-raw.md#INFO-021) [INFO-051](../Information/2026-06-12/collected-raw.md#INFO-051) |
| 中 | Claude Code CI/CD脆弱性（Microsoft発見） | IND-013 high維持。AIエージェント×CI/CD新攻撃面 | A-3 | [INFO-040](../Information/2026-06-12/collected-raw.md#INFO-040) |
| 中 | Glasswing 150組織拡大・10K+脆弱性発見 | Anthropic安全性インフラ拡大。防御側強化 | A-3 | [INFO-008](../Information/2026-06-12/collected-raw.md#INFO-008) |
| 中 | AIコーディング市場$9.8-11B・51%コミットAI支援 | H-CAR-002 C方向。コーディングAI商用成熟 | B-3 | [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034) |
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
| Anthropic安全性第1位選択理由のA-2品質定量確認 | H-ANT-001 25R連続上限条件充足。low→medium復帰検討 | 次回 | [H-ANT-001](../config/hypotheses.json) |
| RSI「ほぼ超人」の外部検証が失敗する | IND-028 high移行の根拠が弱体化。elevatedへの再下方検討 | 90日 | [IND-028](../config/indicators.json) |
| QHG Y軸定量評価基準が設定されない（次回Arbiter） | シナリオ確率凍結ペナルティ発動。39R連続未実行 | 次回 | [scenarios.json](../config/scenarios.json) |
| AIベンチマーク飽和で新ベンチマークが性能差を再現する | SCN-004前提の「差別化消失」が弱まり、SCN-002/003支持に転じる | 180日 | [IND-028](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 56% | medium -1%。10R連続C>I確証バイアスの累積ペナルティ。Codex 5M WAU [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001)・Oracle提携 [INFO-002](../Information/2026-06-12/collected-raw.md#INFO-002) はC。価格引き下げ検討 [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019) は「価格決定力なき支配」。56%到達・medium維持 | [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001) [INFO-002](../Information/2026-06-12/collected-raw.md#INFO-002) [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019) [INFO-020](../Information/2026-06-12/collected-raw.md#INFO-020) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 44% | low ±0%。Codex Plugins 62アプリ110スキル [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) は围い込みI蓄積。I蓄積35件。限界効率逓減 | [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) | [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036) (MCP標準化) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究に大規模資源を投入する | 3% | low ±0%。Phase 3宣言 [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) はC方向だが、S-1提出 [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) は商業化I | [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 41% | low -1%。仮説再定式化4R未実行の累積ペナルティ。WH EO先進AI [INFO-023](../Information/2026-06-12/collected-raw.md#INFO-023)・NSPM-11 [INFO-045](../Information/2026-06-12/collected-raw.md#INFO-045) はC。Anthropic商業成功（Fable 5・KPMG・Foundry）はI。I=0本ラウンド。low帯深化 | [INFO-023](../Information/2026-06-12/collected-raw.md#INFO-023) [INFO-045](../Information/2026-06-12/collected-raw.md#INFO-045) | [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006) [INFO-007](../Information/2026-06-12/collected-raw.md#INFO-007) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 38% | low -1%。24R連続上限条件未達成。KPMG 276K [INFO-007](../Information/2026-06-12/collected-raw.md#INFO-007)・UK政府 [INFO-015](../Information/2026-06-12/collected-raw.md#INFO-015) はC。自律兵器拒否 [INFO-022](../Information/2026-06-12/collected-raw.md#INFO-022) はI方向の可能性（軍事除外=市場制限）。安全性第1位選択理由A-2品質定量確認不在。low帯深化 | [INFO-007](../Information/2026-06-12/collected-raw.md#INFO-007) [INFO-015](../Information/2026-06-12/collected-raw.md#INFO-015) [INFO-008](../Information/2026-06-12/collected-raw.md#INFO-008) | [INFO-022](../Information/2026-06-12/collected-raw.md#INFO-022) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 64% | medium ±0%。Fable 5 FrontierCode首位 [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006)。Microsoft Foundry統合 [INFO-032](../Information/2026-06-12/collected-raw.md#INFO-032) はC。Claude Code CI/CD脆弱性 [INFO-040](../Information/2026-06-12/collected-raw.md#INFO-040) はI（品質問題） | [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006) [INFO-032](../Information/2026-06-12/collected-raw.md#INFO-032) | [INFO-040](../Information/2026-06-12/collected-raw.md#INFO-040) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持しAWS・GCP・Azure全てで同等の機能を提供する | 6% | low ±0%。Microsoft Foundry統合 [INFO-032](../Information/2026-06-12/collected-raw.md#INFO-032) はC。マルチクラウド均衡証拠不在。棄却候補維持 | [INFO-032](../Information/2026-06-12/collected-raw.md#INFO-032) | (マルチクラウド均衡証拠不在) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 47% | low -1%+medium→low移行。19R代替説明未解決。DiffusionGemma [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014)・Skill Registry [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) はC。I=0構造的問題。low移行。KIQ-GOO-001充足時medium復帰検討 | [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014) [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) [INFO-018](../Information/2026-06-12/collected-raw.md#INFO-018) | (代替説明未解決19R) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し围い込みを回避する | 23% | low ±0%。Skill Registry围い込みI蓄積 [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044)。MCP RC開放C [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036)。围い込みI 33件 vs 開放C 3件。蓄積速度比11:1 | [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036) | [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% | medium -1%。DiffusionGemma [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014)・Gemini 3.1 Pro [INFO-018](../Information/2026-06-12/collected-raw.md#INFO-018) はC。A-2+条件20R未達成。48%到達。次回low移行検討 | [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014) [INFO-018](../Information/2026-06-12/collected-raw.md#INFO-018) | (A-2+条件未達成継続) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 59% | medium ±0%。DeepSeek V4 Pro既織り込み済み。Grok Build Marketplace [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) はエコシステム拡大C。API価格コモディティ化で独自性希薄化リスク。次回59%以下継続でmedium→low移行検討 | [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) | (価格コモディティ化) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 55% | medium ±0%。Grok Build Marketplace [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010)・eToro提携 [INFO-011](../Information/2026-06-12/collected-raw.md#INFO-011)・Gopuff [INFO-012](../Information/2026-06-12/collected-raw.md#INFO-012) はエコシステム拡大C。市場採用データ不在継続 | [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) [INFO-011](../Information/2026-06-12/collected-raw.md#INFO-011) [INFO-012](../Information/2026-06-12/collected-raw.md#INFO-012) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceは中国で取った規模を足がかりにグローバル展開する | 64% | medium ±0%。Coze 2.5 Agent World [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) は中国市場深耕。2000億元投資上方修正 [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) はC。ミラーイメージングリスク継続 | [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) | (グローバル展開証拠限定的) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 46% | low -1%。豆包MAU 610万減 [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) が「低価格戦略維持」に直接反。有料化KPI評価対象外。I蓄積28件目。low帯深化 | (基本機能無料維持) | [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% | low ±0%。著作権関連新規なし。Coze 2.5・DeerFlow 2.0 [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) [INFO-017](../Information/2026-06-12/collected-raw.md#INFO-017) はグローバル展開能力Cだが中国市場中心 | [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) | (著作権新規なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 36% | low ±0%。因果ギャップ未解決・正常性バイアス指摘（v4.05）継続。BCG「大半が収益未達」 [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) はI方向。41%管理層削減 [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) はC方向。AIコーディング$9.8-11B [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034) はC | [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034) | [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) [INFO-026](../Information/2026-06-12/collected-raw.md#INFO-026) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | medium ±0%。AIコーディング$9.8-11B [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034)・51%コミットAI支援。69%上限（METR 43%反証組み込み済み） | [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034) | (METR本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | medium ±0%。41%管理層削減 [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042)・BCG「大半が収益未達」 [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038)。速度不確定 | [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Claude Code CI/CD脆弱性 [INFO-040](../Information/2026-06-12/collected-raw.md#INFO-040)（A-3）・Glasswing 10K+ [INFO-008](../Information/2026-06-12/collected-raw.md#INFO-008)（A-3）。AIエージェント×CI/CD新攻撃面顕在化。high/rising | 2026-06-12 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Fable 5視覚・科学研究向上 [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006)（A-3）・DiffusionGemma 4倍高速化 [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014)（A-3）。量的向上継続。「真の理解」検証未解決。elevated/stable | 2026-06-12 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | Gartner 40%エンタープライズエージェント [INFO-025](../Information/2026-06-12/collected-raw.md#INFO-025)（B-3）vs BCG「大半が収益未達」 [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038)（B-3）。期待-実態ギャップ確認継続。high/rising | 2026-06-12 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP RC公開 [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036)（B-3）・AAIF振り返り [INFO-043](../Information/2026-06-12/collected-raw.md#INFO-043)（B-3）・Gemini Skill Registry [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044)（A-3）・SkillsMP [INFO-049](../Information/2026-06-12/collected-raw.md#INFO-049)。標準化と囲い込みの同時加速。high/rising | 2026-06-12 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated→A-1品質ブレークスルーで high | Phase 3宣言2028年3月AI研究自動化 [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004)（A-3）・ARC GPT-5 96.3% [INFO-021](../Information/2026-06-12/collected-raw.md#INFO-021)（C-3）・ベンチマーク飽和 [INFO-051](../Information/2026-06-12/collected-raw.md#INFO-051)（C-3）。主観-客観乖離拡大継続。high/rising | 2026-06-12 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | Anthropic $965B評価額 [INFO-029](../Information/2026-06-12/collected-raw.md#INFO-029)（B-3）・ByteDance 2000億元投資上方修正 [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035)（C-3）。資本流入劇的加速確定的。high/rising | 2026-06-12 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | WH EO先進AI [INFO-023](../Information/2026-06-12/collected-raw.md#INFO-023)（A-3）・NSPM-11 [INFO-045](../Information/2026-06-12/collected-raw.md#INFO-045)（A-3）・自律兵器拒否 [INFO-022](../Information/2026-06-12/collected-raw.md#INFO-022)（C-3）・Phase 3宣言 [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004)（A-3）。能力-リスク二面性の新段階。high/rising | 2026-06-12 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-12 | §0-§2・§4・§5・プレイヤースナップショット・付録を全面書き直し。SCN-004がSCN-003を抜いて首位（30%）・H-GOO-001 medium→low・価格コモディティ化加速・エコシステム囲い込み同時創発を反映。v4.06 | [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006) [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014) [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019) [INFO-023](../Information/2026-06-12/collected-raw.md#INFO-023) [INFO-027](../Information/2026-06-12/collected-raw.md#INFO-027) [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) [INFO-037](../Information/2026-06-12/collected-raw.md#INFO-037) [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) | SCN-003 32→29%（首位陥落）・SCN-004 27→30%（首位奪取）・H-GOO-001 51→47% medium→low・H-OAI-001 58→56%・H-ANT-001 42→38%・H-GOV-001 45→41%・H-GOO-003 49→48%・H-BTD-002 48→46%・H-CAR-001 35→36% |
| 2026-06-07 | IND-028 elevated→high(RSI「ほぼ超人」A-1)・H-CAR-001 34→35%(142Kレイオフ A-1)・H-GOV-001 45%±0%(C/I均衡・SCR指定vs NSA継続)・H-GOO-002 23%±0%(ADK OSS vs Enterprise統合・品質調整後均衡)・H-BTD-002 48%±0%(Freemium進化)・SCN-003 33→32%(31R固定ペナルティ)・SCN-004 26→27%(コモディティ化C蓄積)・軍事-AI融合パターン中-高→中・エンタープライズエージェントパターン中→低-中・最重要発見高→中(政府-AI対立の新しい均衡点)・品質調整Red Agent採用率75%到達・プレイヤースナップショット更新を反映して全面書き直し | [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) [INFO-016](../Information/2026-06-07/collected-raw.md#INFO-016) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052) [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) [INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054) [INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056) | IND-028 elevated→high・H-CAR-001 34→35%・SCN-003 33→32%・SCN-004 26→27%・围い込みI 32→33件・開放C 2→3件 |
| 2026-06-06 | H-GOO-002 25→23%(围い込み32件+開放C 30R解除)・H-BTD-002 49→48%(MAU 6.1M減)・H-GOV-001 45%±0%(停止条件1R目・SCR+DPA+EO)・H-CAR-001 34%±0%(AIレイオフ123K・Klarna逆転)・SCN-001 +1%(17%)・SCN-003 -1%(33%)・Anthropic $65B・Opus 4.8首位・API価格体系・対外投資規制・Hassabis AGI 2029・プレイヤースナップショット更新を反映して全面書き直し | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028) [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030) [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032) [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038) [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041) [INFO-042](../Information/2026-06-06/collected-raw.md#INFO-042) [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) [INFO-045](../Information/2026-06-06/collected-raw.md#INFO-045) [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047) | H-GOO-002 25→23%・H-BTD-002 49→48%・SCN-001 16→17%・SCN-003 34→33%・SCN-002 24%±0%・SCN-004 26%±0%・围い込み19→32件・開放C 28R不在→30R解除(2件出現) |
| 2026-06-04 | H-GOV-001 48→45%(停止条件宣言)・H-GOO-002 29→25%(围い込み19件)・H-BTD-002 51→49%(low移行)・H-CAR-001 32→33%・Trump大統領令・142K解雇・DeepSeek $7.4B・Meta Muse Sparkクローズド・S-1機密提出・プレイヤースナップショット更新を反映して全面書き直し | [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) | H-GOV-001 48→45%・H-GOO-002 29→25%・H-BTD-002 51→49%・H-CAR-001 32→33%・SCN-002 25→24%・SCN-004 25→26% |
| 2026-05-31 | Arbiter v3.94完了反映。SCN-004 tied SCN-002(25%)順位逆転。H-GOV-001 -2%・H-ANT-001 -2%・H-GOO-002 -2%・H-OAI-001 -2%・H-CAR-001 +1%を反映して全面書き直し | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) | SCN-002 27→25%・SCN-003 37→35%・SCN-004 21→25%・SCN-001 15%・H-GOV-001 50→48%・H-ANT-001 44→42%・H-GOO-002 31→29%・H-OAI-001 60→58% |
| 2026-05-28 | Arbiter v3.91完了反映。「政府-市場ギャップ」再定義。H-GOV-001 -1%・H-GOO-001 -1%・H-GOO-002 -1%・H-XAI-002 -1%・H-CAR-001 +1%・SCN-001 -1%を反映して全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | SCN-001 16→15%・SCN-003 36→37%・H-GOV-001 52→51%・H-GOO-001 54→53%・H-GOO-002 33→32%・H-XAI-002 62→61%·H-BTD-002 54→51%・H-CAR-001 30→31% |

---

## 7. ブラインドスポット

- [H-GOO-001](../config/hypotheses.json) medium→low移行。19R連続で代替説明「業界全体押し上げ」が未解決。KIQ-GOO-001（AWS/Azure同時期成長率比較データ）が充足されない限りlow維持。low→medium復帰条件の達成タイムラインが不確定。
- パターンNN「価格コモディティ化の不可逆的加速」の7件シグナルの品質はB-3/C-3中心。高品質（A-1/A-2）での価格反転確認または否定が未実施。品質コードが低い証拠の蓄積でパターン確度を中-高としたことの妥当性限界。
- パターンMM「エコシステム囲い込みの同時創発」は5社の同時行動を観察しているが、意図的協調ではなく競争的模倣の可能性が未分離。囲い込み意図と標準化圧力の強さが未知数。
- QHG再定義39R連続未実行（v3.74～v4.06）。Y軸「フロンティア差別化の持続性」の定量評価基準が未設定。SCN-004首位（30%）の判定が定性蓄積のみに依存。手続き的崩壊確定。
- [H-ANT-001](../config/hypotheses.json) 24R連続上限条件未達成。安全性第1位選択理由のA-2品質定量確認が不在。KIQ-ANT-SAFETYが次回の収集優先だが、定量的選択理由調査自体が非公開の可能性。
- [H-GOV-001](../config/hypotheses.json) 仮説再定式化4R未実行。「萎縮効果」と「触媒効果」の分離が次回絶対条件。C/I均衡ラウンド連続は診断的識別力不足の徴候。
- OpenAI S-1内容・Anthropic IPO詳細が非公開。上場が安全性スタンスに与える影響（株主圧力）の評価が不在。パターンPPの確度低-中は情報不足の反映。
- AIレイオフ因果帰属の自己申告バイアス。AIが真の原因か口実かの判別不能。パターンQQ「ブーメラン効果」の確度中は限定的証拠に基づく。
- RSI「ほぼ超人」の外部検証状況が詳細不明。IND-028 high移行は条件付。ベンチマーク飽和問題 [INFO-051](../Information/2026-06-12/collected-raw.md#INFO-051) が性能評価全体の妥当性を問う。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral等の台頭は「5社フレーム」自体の妥当性を問う結果。
- 品質調整方法論のRed Agent採用率75%はメタレベル変化。Blue Agent提案とArbiter独自判断の乖離が拡大中（本ラウンドBlue採用17%・Arbiter独自83%）。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001) | OpenAI Ona買収・Codex 5M週間ユーザー(A-3) |
| [INFO-002](../Information/2026-06-12/collected-raw.md#INFO-002) | OpenAI-Oracle Cloud提携(A-3) |
| [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) | OpenAI機密S-1提出(A-3) |
| [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | OpenAI Phase 3宣言・2028年3月AI研究自動化(A-3) |
| [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) | Codex 6役割別プラグイン・62アプリ110スキル(A-3) |
| [INFO-006](../Information/2026-06-12/collected-raw.md#INFO-006) | Claude Fable 5/Mythos 5・$10/M入力・FrontierCode首位(A-3) |
| [INFO-007](../Information/2026-06-12/collected-raw.md#INFO-007) | KPMG 276K提携・グローバル戦略的提携(A-3) |
| [INFO-008](../Information/2026-06-12/collected-raw.md#INFO-008) | Glasswing 150組織拡大・10K+脆弱性発見(A-3) |
| [INFO-010](../Information/2026-06-12/collected-raw.md#INFO-010) | Grok Build Plugin Marketplace(A-3) |
| [INFO-011](../Information/2026-06-12/collected-raw.md#INFO-011) | eToro提携・リアルタイム市場センチメント(A-3) |
| [INFO-012](../Information/2026-06-12/collected-raw.md#INFO-012) | Gopuff Go agent・配送AIエージェント(A-3) |
| [INFO-013](../Information/2026-06-12/collected-raw.md#INFO-013) | Agentic Gemini宣言(A-3) |
| [INFO-014](../Information/2026-06-12/collected-raw.md#INFO-014) | DiffusionGemma 4倍高速化(A-3) |
| [INFO-015](../Information/2026-06-12/collected-raw.md#INFO-015) | UK政府GOV.UK AIアシスタント提携(A-3) |
| [INFO-016](../Information/2026-06-12/collected-raw.md#INFO-016) | Coze 2.5 Agent Worldエコシステム(C-3) |
| [INFO-017](../Information/2026-06-12/collected-raw.md#INFO-017) | DeerFlow 2.0スーパーエージェント(C-3) |
| [INFO-018](../Information/2026-06-12/collected-raw.md#INFO-018) | Gemini 3.1 Pro SWE・エージェント改善(A-3) |
| [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019) | OpenAI価格引き下げ検討・WSJ報道(B-3) |
| [INFO-020](../Information/2026-06-12/collected-raw.md#INFO-020) | OpenAI 2026年8回価格改定(C-3) |
| [INFO-021](../Information/2026-06-12/collected-raw.md#INFO-021) | ARC-AGI-3 GPT-5 96.3%(C-3) |
| [INFO-022](../Information/2026-06-12/collected-raw.md#INFO-022) | Anthropic自律兵器拒否・ベンダー撤退不可能(C-3) |
| [INFO-023](../Information/2026-06-12/collected-raw.md#INFO-023) | WH EO先進AI・NSPM-11同時署名(A-3) |
| [INFO-024](../Information/2026-06-12/collected-raw.md#INFO-024) | EU AI Act 2026年8月執行開始(B-3) |
| [INFO-025](../Information/2026-06-12/collected-raw.md#INFO-025) | Gartner 40%エンタープライズエージェント(B-3) |
| [INFO-026](../Information/2026-06-12/collected-raw.md#INFO-026) | AIレイオフブーメラン効果・Klarna再雇用(C-3) |
| [INFO-027](../Information/2026-06-12/collected-raw.md#INFO-027) | OSS LLM商用モデル89%到達(C-3) |
| [INFO-028](../Information/2026-06-12/collected-raw.md#INFO-028) | Visa-OpenAI提携・Agentic Commerce(B-3) |
| [INFO-029](../Information/2026-06-12/collected-raw.md#INFO-029) | OpenAI vs Anthropic IPO競争レース(B-3) |
| [INFO-030](../Information/2026-06-12/collected-raw.md#INFO-030) | DeepSeek V4 Pro NIST評価・API利用率4.2%(C-3) |
| [INFO-031](../Information/2026-06-12/collected-raw.md#INFO-031) | AIベンダーロックイン・推論の暗黙知(C-3) |
| [INFO-032](../Information/2026-06-12/collected-raw.md#INFO-032) | Fable 5 Microsoft Foundry統合(A-3) |
| [INFO-034](../Information/2026-06-12/collected-raw.md#INFO-034) | AIコーディング市場$9.8-11B・51%コミットAI支援(B-3) |
| [INFO-035](../Information/2026-06-12/collected-raw.md#INFO-035) | 豆包MAU 610万減・2000億元投資上方修正(C-3) |
| [INFO-036](../Information/2026-06-12/collected-raw.md#INFO-036) | MCP RC公開・ステートレスプロトコルコア(B-3) |
| [INFO-037](../Information/2026-06-12/collected-raw.md#INFO-037) | Lindy Anthropic→DeepSeek切り替え(C-3) |
| [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) | BCG AI時代組織再設計・大半が収益未達(B-3) |
| [INFO-040](../Information/2026-06-12/collected-raw.md#INFO-040) | Claude Code CI/CD脆弱性・Microsoft発見(A-3) |
| [INFO-041](../Information/2026-06-12/collected-raw.md#INFO-041) | Mastercard Agent Pay for Machines(A-3) |
| [INFO-042](../Information/2026-06-12/collected-raw.md#INFO-042) | Fortune 500 AI階層フラット化・41%管理層削減(B-3) |
| [INFO-043](../Information/2026-06-12/collected-raw.md#INFO-043) | AAIF 6ヶ月振り返り・標準化進展(B-3) |
| [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) | Gemini Skill Registry/RAG Engine(A-3) |
| [INFO-045](../Information/2026-06-12/collected-raw.md#INFO-045) | NSPM-11国家安全保障AI大統領覚書(A-3) |
| [INFO-046](../Information/2026-06-12/collected-raw.md#INFO-046) | Fortune 500月額推論コスト数千万ドル(C-3) |
| [INFO-049](../Information/2026-06-12/collected-raw.md#INFO-049) | SkillsMPスキルマーケットプレイス(C-3) |
| [INFO-051](../Information/2026-06-12/collected-raw.md#INFO-051) | AIベンチマーク飽和・本番失敗増加(C-3) |
| [Arbiter v4.06](../state/arbiter-2026-06-12.md) | 確度評価の完全根拠 |
