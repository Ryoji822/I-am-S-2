# AI市場全体 - 静的インテリジェンス

> 最終判断更新: 2026-06-07
> 全体確信度: 中
> 情報非対称性: ByteDance/DeepSeek グローバルシェア追跡困難。2nd tier不在。QHG Y軸v3.84以降とv3.83以前は非整合。QHG再定義32R連続未実行。品質調整方法論のRed Agent採用率75%がメタレベル変化
> 主参照: [hypotheses.json](../config/hypotheses.json) [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json), [scenarios.json](../config/scenarios.json) SCN-001/002/003/004, [indicators.json](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## プレイヤー一覧スナップショット (2026-06-07時点)

| 企業 | 主力モデル/製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.8, Sonnet 4.6, Claude Code | $65B調達・$965B評価額(A-1) | SWE-bench首位(88.6%) | Pentagon SCR指定 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018)・NSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019)・KPMG 276K提携 [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001)・RSI「ほぼ超人」 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046)・EU AI法適合率首位 [INFO-058](../Information/2026-06-07/collected-raw.md#INFO-058). H-ANT-001 42%. H-GOV-001 45%(±0%) |
| OpenAI | GPT-5.5, Codex, Skills Beta | $852B評価額(C-1)・年間収益$25B(A-2) | ARC-AGI 2首位(85%) | Pentagon対抗契約 [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020)・年間収益$25B [INFO-034](../Information/2026-06-07/collected-raw.md#INFO-034)・Trump EO 30日前提出要請 [INFO-016](../Information/2026-06-07/collected-raw.md#INFO-016)・Astral買収 [INFO-035](../Information/2026-06-07/collected-raw.md#INFO-035). H-OAI-001 58% |
| Google | Gemini 3.1 Pro, 3.5 Flash, Antigravity Agent | Cloud $4,600億バックログ(A-1)・Capex $180-190B(A-3) | LMArena Elo首位(1501) | GCP 16→22%シェア [INFO-051](../Information/2026-06-07/collected-raw.md#INFO-051)・Cloud 63.4%増 [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052)・Gemini Enterprise Agent Platform [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006)・ADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011)・Hassabis AGI ~2030 [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047). H-GOO-002 23% |
| SpaceXAI | Grok 4.3, Grok Build | $20B調達(B-3) | 4位 | Grok Voice Agent API [INFO-004](../Information/2026-06-07/collected-raw.md#INFO-004). H-XAI-002 60%. 構造的変化なし |
| ByteDance | 豆包2.0, Coze 3.0, Seedance 2.1 | CAPEX RMB 2,300億(B-2) | 非公開 | 豆包有料プロ版 [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053)・Seedance 2.0無料無制限 [INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054)・対外投資規制7/1 [INFO-017](../Information/2026-06-07/collected-raw.md#INFO-017). H-BTD-002 48% |

---

## 0. 一文要約

IND-028がelevated→highに条件付移行した。Anthropic RSI「定義された実験ではほぼ超人」 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046)（A-1品質）がhigh移行条件を充足した。SCN-003が32%（-1%）、SCN-004が27%（+1%）にそれぞれ変動し、首位シナリオとの差が7%から5%に縮小した。[H-CAR-001](../config/hypotheses.json)が34→35%（+1%）に上昇し、142KテックレイオフでAIが解雇理由第1位 [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038)（A-1品質、87,714人分）が強力なCとなった。[H-GOV-001](../config/hypotheses.json)は45%±0%で、Pentagon SCR指定 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018)（A-1）の強力CとNSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019)（A-1）の強力Iが均衡した。[H-GOO-002](../config/hypotheses.json)は23%±0%。ADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) の開放CとGemini Enterprise統合スタック [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) の围い込みIが同時出現し、品質調整後実質均衡。[H-BTD-002](../config/hypotheses.json)は48%±0%。豆包有料プロ版 [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) はFreemium進化であり全面的転換ではない。品質調整方法論でRed Agent採用率75%に到達し、メタレベル変化が進行中。

---

## 1. コア判断

IND-028がelevatedからhighに条件付移行した。これは本ラウンドで最も重要な構造的変化である。AnthropicがRSI研究で「定義された実験ではほぼ超人」レベルに到達した [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046)（A-1品質）ことが移行条件を充足した。Hassabis AGI ~2030 [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047)（A-2品質）、孫正義の超知能2年以内予測、Altman/Amodeiの「稀な一致」が主観的前倒しの持続を示す一方、AGI定義の合意不在 [INFO-048](../Information/2026-06-07/collected-raw.md#INFO-048) も確認された。主観と客観の乖離は縮小方向だが依然として存在する。

[H-CAR-001](../config/hypotheses.json)が34→35%（+1%）に上昇した。142KテックレイオフでAIが解雇理由第1位 [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038)（A-1品質、年間87,714人分）は極めて強力なC証拠である。前回Arbiter制約「INFO-042鮮度18ヶ月前」に対し、2026年の最新A-1品質データで鮮度問題を解消した。コーディングスキル40%陳腐化予測 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041)（B-2品質）もH-CAR-001/H-CAR-003双方のC方向。一方、Klarna品質崩壊再採用 [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026)（B-2品質）とPwC 79%本番運用のAIスティッカーショック [INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056)（A-2品質）がI側。C/I比は3:3だが、A-1品質Cの重みで+1%。

[H-GOV-001](../config/hypotheses.json)は45%±0%で、C/I均衡ラウンドとなった。Pentagon SCR指定・$200M契約打切 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018)（A-1品質）は強力なCである。7社軍事契約・OpenAI即座対抗 [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020)（A-2品質）は安全性拒否の機会費用が$200M+で定量化された初の事例である。しかしNSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019)（A-1品質）は政府機関内でも安全性重視企業の需要が存続することを示す強力なIである。Anthropic AI一時停止提案 [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049)（A-2品質）・米中Geneva AI安全予備合意 [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050)（A-2品質）もI。C側8件（A-1×1）vs I側6件（A-1×1）。品質調整後、A-1品質同士の直接対決（SCR指定vs NSA継続）は均衡と評価し±0%。

[H-GOO-002](../config/hypotheses.json)は23%±0%で品質調整後実質均衡。Gemini Enterprise Agent Platform統合スタック [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006)（A-3品質）の围い込みI蓄積（累計33件）に対し、ADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011)（A-3品質）の開放C（累計3件）が出現した。蓄積速度比11:1で围い込み圧倒だが、围い込みIの品質別内訳はA-3品質比率90.6%（企業公式発表中心）であり、運用実態に基づく围い込み確認ではない。品質調整で実質均衡と評価。

[H-BTD-002](../config/hypotheses.json)は48%±0%。豆包有料プロ版 [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053)（A-2品質）は低価格戦略からの転換点だが、Seedance 2.0無料無制限 [INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054)（B-2品質）と無料版の維持からFreemium進化と評価する。全面的転換ではなく、有料層と無料層の二層化である。low帯（48%）の前提に定量的矛盾はない。

SCN-003が32%（-1%）、SCN-004が27%（+1%）に変動した。SCN-004のコモディティ化C蓄積はGitHub Copilot定額→従量制移行 [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039)（A-2品質）・API価格下落トレンド確認 [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030)（B-2品質）で強化された。首位シナリオSCN-003との差が7%から5%に縮小。SCN-003の31R固定ペナルティ統計的是正は継続。

政府-AI対立の「新しい均衡点」が出現した（確度: 中、前回: 高）。Pentagon SCR指定（A-1）とNSA継続利用（A-1）の同時発生は、政府-AI関係が単純な「圧力→萎縮」ではなく政府内分裂を含む複雑な均衡に移行していることを示唆する。軍事-AI融合パターンは中-高→中に下方修正。エンタープライズエージェントプラットフォームパターンは中→低-中（Google・Microsoft同時プラットフォーム化は業界コンセンサス形成で独自戦略的選択ではない）。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | RSI「定義された実験ではほぼ超人」到達(A-1) | IND-028 elevated→high移行。AGI到達度指標の最重要構造的変化 | A-1 | [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) |
| 高 | 142Kテックレイオフ・AI #1理由・87,714人分(A-1) | H-CAR-001 +1%。2026年最新A-1品質で鮮度問題解消 | A-1 | [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) |
| 高 | Pentagon SCR指定+$200M契約打切(A-1) | H-GOV-001強力C。安全性拒否の機会費用定量可視化 | A-1 | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) |
| 高 | NSA継続利用・Anthropicエンジニア埋め込み(A-1) | H-GOV-001強力I。政府内分裂確認。萎縮効果限界示唆 | A-1 | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) |
| 高 | GitHub Copilot定額→従量制移行(A-2) | SCN-004 +1%の直接根拠。コーディングAI商用成熟 | A-2 | [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) |
| 高 | 7社軍事契約・OpenAI即座対抗(A-2) | H-GOV-001 C。安全性の機会費用$200M+で定量化 | A-2 | [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) |
| 高 | 豆包有料プロ版(A-2) | H-BTD-002 I方向だがFreemium進化。全面的転換ではない | A-2 | [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) |
| 高 | Cloud 63.4%増・Big Tech $725B capex(A-2) | H-GOO-001 C方向。Google固有優位性の定量確認接近 | A-2 | [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052) |
| 高 | Gemini Enterprise Agent Platform・ADK OSS同時出現 | H-GOO-002 ±0%の直接根拠。围い込みIと開放Cの同時蓄積 | A-3 | [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) |
| 高 | コーディングスキル40%陳腐化予測(B-2) | H-CAR-001/H-CAR-003 C。スキル価値の構造的変化 | B-2 | [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) |
| 中 | GCP 16→22%シェア・4年+6pt(B-2) | H-GOO-001 C方向。低基数効果含む | B-2 | [INFO-051](../Information/2026-06-07/collected-raw.md#INFO-051) |
| 中 | Hassabis AGI ~2030・孫正義2年・Altman/Amodei一致(A-2) | IND-028 主観的前倒し持続。客観的証拠との乖離縮小方向 | A-2 | [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) |
| 中 | Anthropic AI一時停止メカニズム提案(A-2) | H-GOV-001 I。安全性提唱強化で萎縮の反対方向 | A-2 | [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) |
| 中 | PwC 79%本番運用・AIスティッカーショック(A-2) | H-CAR-001 I。コスト増大が生産性向上を相殺 | A-2 | [INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056) |
| 中 | Trump EO 30日前モデル提出要請(A-2) | H-GOV-001 C方向。政府アクセス拡大 | A-2 | [INFO-016](../Information/2026-06-07/collected-raw.md#INFO-016) |
| 中 | 米中Geneva AI安全予備合意(A-2) | H-GOV-001 I。国際的安全性枠組み構築進展 | A-2 | [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) |
| 中 | EU AI法Article 4: 2026年8月3日施行(A-2) | 規制環境包括的再構成。域外適用あり | A-2 | [INFO-015](../Information/2026-06-07/collected-raw.md#INFO-015) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | 「加速する構造的トレンド」判断が崩れ、SCN-004の前提が弱体化する | 180日 | [IND-025](../config/indicators.json) |
| Google围い込み蓄積が止まり、開放C証拠が5件以上に拡大する | H-GOO-002の上方修正根拠。現在開放C 3件 | 180日 | [IND-027](../config/indicators.json) |
| 豆包が有料化を撤回し無料低価格戦略に復帰する | H-BTD-002 low深化前提の再検証。価格戦略逸脱が一時的だった場合の確度回復 | 180日 | [H-BTD-002](../config/hypotheses.json) |
| Anthropic SCR指定が解除され政府市場アクセスが回復する | H-GOV-001萎縮効果前提が崩れる。停止条件の再検証が必要 | 180日 | [IND-030](../config/indicators.json) |
| AI本番到達率が採用率の50%以上に改善する | H-CAR-001のI側根拠が崩れ、雇用削減加速の確度が上昇する | 180日 | [IND-026](../config/indicators.json) |
| Trump大統領令自発的枠組みが30日後（2026-07-02）に機能確認される | H-GOV-001萎縮効果限界示唆→-1%検討 | 30日 | [IND-030](../config/indicators.json) |
| QHG Y軸定量評価基準が設定されない（次回Arbiter） | シナリオ確率凍結ペナルティ発動。32R連続未実行 | 次回 | [scenarios.json](../config/scenarios.json) |
| 围い込み33件の品質別内訳で独立性「高」件数が10件未満 | H-GOO-002件数インフレ指摘の妥当性確認。確度上方修正根拠 | 次回 | [IND-027](../config/indicators.json) |
| RSI「ほぼ超人」の外部検証が失敗する | IND-028 high移行の根拠が弱体化。elevatedへの再下方検討 | 90日 | [IND-028](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 58% | medium ±0%。$25B年間収益 [INFO-034](../Information/2026-06-07/collected-raw.md#INFO-034)・Pentagon対抗契約 [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) はC。コモディティ化下での「支配」定義未解決。確証バイアス監視継続 | [INFO-034](../Information/2026-06-07/collected-raw.md#INFO-034) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) | (Anthropic首位交代継続) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を围い込む | 44% | low ±0%。I蓄積34件。限界効率逓減 | (新規直接関連証拠なし) | (MCP標準化深化) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先とし商業化と並行して研究に大規模資源を投入する | 3% | low ±0%。新規直接関連証拠なし | (AGI研究継続) | (商業化加速) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 45% | medium ±0%。C/I均衡ラウンド。SCR指定(A-1)vs NSA継続利用(A-1)。政府内分裂確認。新しい均衡点出現 | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) [INFO-016](../Information/2026-06-07/collected-raw.md#INFO-016) | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) |
| [H-ANT-001](../config/hypotheses.json) | Anthropicは安全性を差別化要因としてエンタープライズ市場で優位に立つ | 42% | low ±0%。KPMG 276K提携 [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001)・EU AI法適合率首位 [INFO-058](../Information/2026-06-07/collected-raw.md#INFO-058) はC。SCR指定(A-1)はI。上限条件20R未達成継続 | [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) [INFO-058](../Information/2026-06-07/collected-raw.md#INFO-058) | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Agent SDKが開発者エコシステムで急成長し標準ツールになる | 64% | medium ±0%。Opus 4.8記録的コーディング [INFO-055](../Information/2026-06-07/collected-raw.md#INFO-055)。SDK活発開発C | [INFO-055](../Information/2026-06-07/collected-raw.md#INFO-055) | (budget overruns構造的リスク) |
| [H-ANT-003](../config/hypotheses.json) | Anthropicはマルチクラウド戦略を維持しAWS・GCP・Azure全てで同等の機能を提供する | 6% | low ±0%。SpaceX Colossus提携 [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) はインフラ集中I。マルチクラウド均衡証拠不在。棄却候補維持 | (マルチクラウド証拠不在) | [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) |
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かしシェアを拡大する | 51% | medium ±0%。Cloud 63.4%増 [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052)・GCP +6pt [INFO-051](../Information/2026-06-07/collected-raw.md#INFO-051) はC。低基数効果含む。A-2+条件14R未達成だが大幅接近 | [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052) [INFO-051](../Information/2026-06-07/collected-raw.md#INFO-051) [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) | (低基数効果未分離) |
| [H-GOO-002](../config/hypotheses.json) | Googleはオープン標準とのDay 0サポートを維持し围い込みを回避する | 23% | low ±0%。品質調整後実質均衡。围い込みI 33件蓄積。開放C 3件出現。蓄積速度比11:1。围い込みI品質A-3比率90.6% | [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) | [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 49% | medium ±0%。Cloud 63.4%増 [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052)。Hassabis AGI ~2030 [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047)。A-2+条件14R未達成。49%到達。次回low移行検討 | [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052) [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) | (A-2+条件未達成継続) |
| [H-XAI-001](../config/hypotheses.json) | xAIはXのリアルタイムデータを活用し差別化する（棄却） | 35% | low。37R+証拠不在。Grok Voice Agent API [INFO-004](../Information/2026-06-07/collected-raw.md#INFO-004) もXデータ非依存。正式棄却維持 | (証拠不在) | [INFO-004](../Information/2026-06-07/collected-raw.md#INFO-004) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し価格競争でシェアを獲得する | 60% | medium ±0%。構造的変化なし。API価格コモディティ化で独自性希薄化リスク | (価格低い) | (DL減・市場採用不在) |
| [H-XAI-003](../config/hypotheses.json) | xAIはSpaceX統合で宇宙・製造業特化AIを展開する（棄却） | 35% | low。38R+直接的特化AI製品証拠不在。正式棄却維持 | (証拠不在) | (特化製品不在) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤としてエンタープライズ市場シェアを獲得する | 55% | medium ±0%。Grok Voice Agent API [INFO-004](../Information/2026-06-07/collected-raw.md#INFO-004) はエージェント機能拡張C（A-3品質）。市場採用データ不在継続 | [INFO-004](../Information/2026-06-07/collected-raw.md#INFO-004) | (市場採用データ不在) |
| [H-BTD-001](../config/hypotheses.json) | ByteDanceは中国で取った規模を足がかりにグローバル展開する | 64% | medium ±0%。豆包プロ版は中国市場深耕 [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053)。対外投資規制7/1 [INFO-017](../Information/2026-06-07/collected-raw.md#INFO-017) はI。ミラーイメージングリスク継続 | [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) | [INFO-017](../Information/2026-06-07/collected-raw.md#INFO-017) |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは豆包で低価格戦略を維持し価格競争でシェアを獲得する | 48% | low ±0%。豆包有料プロ版 [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) はFreemium進化。Seedance 2.0無料無制限 [INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054) は無料層維持。全面的転換ではない。low帯深化 | [INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054) | [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受けグローバル展開が制限される | 40% | medium ±0%。対外投資規制 [INFO-017](../Information/2026-06-07/collected-raw.md#INFO-017) はC。著作権関連新規なし | [INFO-017](../Information/2026-06-07/collected-raw.md#INFO-017) | (著作権新規なし) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の中間層雇用を大幅に削減する | 35% | low +1%。142Kレイオフ AI#1理由(A-1) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) が極めて強力なC。コーディング40%陳腐化(B-2) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) もC。Klarna再採用(B-2) [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026)・PwC sticker shock(A-2) [INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056) はI。C/I 3:3だがA-1品質Cの重みで+1% | [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) | [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026) [INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | medium ±0%。Copilot従量制 [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039)・コーディング→インテント [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) はC。69%上限(METR 43%反証) | [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) | (METR本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編される | 57% | medium ±0%。142Kレイオフ [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) 方向支持。WPP 50K AI展開 [INFO-028](../Information/2026-06-07/collected-raw.md#INFO-028) は中間工程排除C。速度不確定 | [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-028](../Information/2026-06-07/collected-raw.md#INFO-028) | (新規Iなし) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | 攻撃面拡大基調。新規大規模実被害なし。high/rising | 2026-06-07 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated | Seedance 2.0無料無制限 [INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054)・Grok Voice Agent API [INFO-004](../Information/2026-06-07/collected-raw.md#INFO-004)。量的向上継続。「真の理解」検証未解決。elevated/stable | 2026-06-07 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | PwC 79%本番・66%生産性向上 [INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056) vs ROI 5% [INFO-014](../Information/2026-06-07/collected-raw.md#INFO-014)・Klarna逆戻り [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026)。期待-実態ギャップA-2品質定量確認。high/rising | 2026-06-07 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | ADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011)・マルチベンダー戦略 [INFO-036](../Information/2026-06-07/collected-raw.md#INFO-036)・ベンダーロックイン回避指針 [INFO-037](../Information/2026-06-07/collected-raw.md#INFO-037)。標準化継続加速。high/rising | 2026-06-07 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated→A-1品質ブレークスルーで high | RSI「ほぼ超人」到達 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046)（A-1）。Hassabis AGI ~2030 [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047)。AGI定義合意不在 [INFO-048](../Information/2026-06-07/collected-raw.md#INFO-048)。米中Geneva合意 [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050)。条件付high移行。high/rising | 2026-06-07 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | $300B Q1投資 [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033)・Big Tech $725B capex [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052)・OpenAI $852B評価額 [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033)。資本流入劇的加速。high/rising | 2026-06-07 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | SCR指定 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018)・Trump EO [INFO-016](../Information/2026-06-07/collected-raw.md#INFO-016)・7社軍事契約 [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020)・RSI進捗 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046)・AI一時停止提案 [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049)。能力向上とリスク増大の同時進行が新段階。high/rising | 2026-06-07 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-07 | IND-028 elevated→high(RSI「ほぼ超人」A-1)・H-CAR-001 34→35%(142Kレイオフ A-1)・H-GOV-001 45%±0%(C/I均衡・SCR指定vs NSA継続)・H-GOO-002 23%±0%(ADK OSS vs Enterprise統合・品質調整後均衡)・H-BTD-002 48%±0%(Freemium進化)・SCN-003 33→32%(31R固定ペナルティ)・SCN-004 26→27%(コモディティ化C蓄積)・軍事-AI融合パターン中-高→中・エンタープライズエージェントパターン中→低-中・最重要発見高→中(政府-AI対立の新しい均衡点)・品質調整Red Agent採用率75%到達・プレイヤースナップショット更新を反映して全面書き直し | [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) [INFO-016](../Information/2026-06-07/collected-raw.md#INFO-016) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052) [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) [INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054) [INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056) | IND-028 elevated→high・H-CAR-001 34→35%・SCN-003 33→32%・SCN-004 26→27%・围い込みI 32→33件・開放C 2→3件 |
| 2026-06-06 | H-GOO-002 25→23%(围い込み32件+開放C 30R解除)・H-BTD-002 49→48%(MAU 6.1M減)・H-GOV-001 45%±0%(停止条件1R目・SCR+DPA+EO)・H-CAR-001 34%±0%(AIレイオフ123K・Klarna逆転)・SCN-001 +1%(17%)・SCN-003 -1%(33%)・Anthropic $65B・Opus 4.8首位・API価格体系・対外投資規制・Hassabis AGI 2029・プレイヤースナップショット更新を反映して全面書き直し | [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028) [INFO-030](../Information/2026-06-06/collected-raw.md#INFO-030) [INFO-032](../Information/2026-06-06/collected-raw.md#INFO-032) [INFO-036](../Information/2026-06-06/collected-raw.md#INFO-036) [INFO-037](../Information/2026-06-06/collected-raw.md#INFO-037) [INFO-038](../Information/2026-06-06/collected-raw.md#INFO-038) [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) [INFO-040](../Information/2026-06-06/collected-raw.md#INFO-040) [INFO-041](../Information/2026-06-06/collected-raw.md#INFO-041) [INFO-042](../Information/2026-06-06/collected-raw.md#INFO-042) [INFO-044](../Information/2026-06-06/collected-raw.md#INFO-044) [INFO-045](../Information/2026-06-06/collected-raw.md#INFO-045) [INFO-046](../Information/2026-06-06/collected-raw.md#INFO-046) [INFO-047](../Information/2026-06-06/collected-raw.md#INFO-047) | H-GOO-002 25→23%・H-BTD-002 49→48%・SCN-001 16→17%・SCN-003 34→33%・SCN-002 24%±0%・SCN-004 26%±0%・围い込み19→32件・開放C 28R不在→30R解除(2件出現) |
| 2026-06-04 | H-GOV-001 48→45%(停止条件宣言)・H-GOO-002 29→25%(围い込み19件)・H-BTD-002 51→49%(low移行)・H-CAR-001 32→33%・Trump大統領令・142K解雇・DeepSeek $7.4B・Meta Muse Sparkクローズド・S-1機密提出・プレイヤースナップショット更新を反映して全面書き直し | [INFO-023](../Information/2026-06-04/collected-raw.md#INFO-023) [INFO-041](../Information/2026-06-04/collected-raw.md#INFO-041) [INFO-033](../Information/2026-06-04/collected-raw.md#INFO-033) [INFO-040](../Information/2026-06-04/collected-raw.md#INFO-040) [INFO-004](../Information/2026-06-04/collected-raw.md#INFO-004) | H-GOV-001 48→45%・H-GOO-002 29→25%·H-BTD-002 51→49%・H-CAR-001 32→33%・SCN-002 25→24%・SCN-004 25→26% |
| 2026-05-31 | Arbiter v3.94完了反映。SCN-004 tied SCN-002(25%)順位逆転。H-GOV-001 -2%・H-ANT-001 -2%・H-GOO-002 -2%・H-OAI-001 -2%・H-CAR-001 +1%を反映して全面書き直し | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) | SCN-002 27→25%・SCN-003 37→35%・SCN-004 21→25%・SCN-001 15%・H-GOV-001 50→48%・H-ANT-001 44→42%・H-GOO-002 31→29%・H-OAI-001 60→58% |
| 2026-05-28 | Arbiter v3.91完了反映。「政府-市場ギャップ」再定義。H-GOV-001 -1%・H-GOO-001 -1%・H-GOO-002 -1%・H-XAI-002 -1%・H-CAR-001 +1%・SCN-001 -1%を反映して全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | SCN-001 16→15%・SCN-003 36→37%・H-GOV-001 52→51%・H-GOO-001 54→53%・H-GOO-002 33→32%・H-XAI-002 62→61%・H-BTD-002 54→51%・H-CAR-001 30→31% |

---

## 7. ブラインドスポット

- [H-GOV-001](../config/hypotheses.json) C/I均衡ラウンド。SCR指定(A-1)とNSA継続利用(A-1)の同時発生は政府内分裂を示すが、最終帰趨が不明。Washington控訴裁 vs California裁の分裂判断の解消タイムライン不明。Trump EO 30日マイルストーン（2026-07-02）が次の転換点。
- [H-GOO-002](../config/hypotheses.json) 围い込み33件の品質別内訳: A-1品質0件・A-2品質3件・A-3品質29件。A-3品質比率90.6%は企業公式発表中心で運用実態に基づく围い込み確認ではない。開放C 3件出現の質的転換可能性が未評価。蓄積速度比11:1は围い込み圧倒だが品質調整で実質均衡。
- [H-BTD-002](../config/hypotheses.json) Freemium進化評価（48%）は豆包有料プロ版とSeedance 2.0無料無制限の二層化を反映。有料層がどの価格帯で安定するかが未確定。対外投資規制7/1発効がグローバル展開に与える影響の定量評価が不在。
- AIレイオフ142K件（AI #1理由・87,714人分） [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) の因果帰属は自己申告ベース。AIが真の原因か口実かの判別が不能。
- RSI「ほぼ超人」 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) の「定義された実験」の具体的内容・再現性・外部検証状況がA-1品質だが詳細不明。IND-028 high移行は条件付であり、外部検証失敗時はelevatedへの再下方検討が必要。
- Anthropic $65B調達の使途・条件が非公開。S-1内容も非公開。上場が安全性スタンスに与える影響（株主圧力）の評価が不在。
- OpenAI API推論トークンの隠しコストが価格比較を複雑化。見た目の価格と実際のコストの乖離が他社にもある可能性。
- QHG再定義32R連続未実行（v3.74～v4.01）。Y軸「フロンティア差別化の持続性」の定量評価基準が未設定。次回Arbiterで強制設定。未設定の場合はシナリオ確率凍結ペナルティ発動。
- 2nd tierプレイヤーの動向を5社比較に入れていない。Mistral等の台頭は「5社フレーム」自体の妥当性を問う結果。
- Klarna事例の「収益15%増」と「品質崩壊」の乖離が、ROI評価方法論の根本的限界を示唆。収益と品質の測定次元が異なる。
- 品質調整方法論のRed Agent採用率75%はメタレベル変化。Blue Agent提案（H-GOV-001 -1%、H-GOO-002 -1%、H-BTD-002 -1%）が品質調整で全却下されたことは、方法論自体が評価結果に与える影響の評価が必要。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) | KPMG 276K提携・Anthropicエンタープライス拡大(A-3) |
| [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) | SpaceX Colossus 300MW・220K GPU提携(A-3) |
| [INFO-004](../Information/2026-06-07/collected-raw.md#INFO-004) | Grok Voice Agent API・xAIエージェント拡張(A-3) |
| [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) | Gemini Enterprise Agent Platform 4支柱(A-3) |
| [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) | ADKオープンソース化・開放C出現(A-3) |
| [INFO-014](../Information/2026-06-07/collected-raw.md#INFO-014) | エンタープライズAIパイロットROI 5%(B-2) |
| [INFO-015](../Information/2026-06-07/collected-raw.md#INFO-015) | EU AI法Article 4: 8/3施行(A-2) |
| [INFO-016](../Information/2026-06-07/collected-raw.md#INFO-016) | Trump AI大統領令・30日前提出要請(A-2) |
| [INFO-017](../Information/2026-06-07/collected-raw.md#INFO-017) | 米中テクノロジー競争激化・対外投資規制7/1(A-2) |
| [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | Pentagon SCR指定・$200M契約打切(A-1) |
| [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) | NSA継続利用・Anthropic埋め込み(A-1) |
| [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) | 7社軍事契約・OpenAI対抗(A-2) |
| [INFO-026](../Information/2026-06-07/collected-raw.md#INFO-026) | Klarna 700人解雇→品質崩壊→再採用(B-2) |
| [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) | AI API価格比較・下落トレンド確認(B-2) |
| [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033) | 2026年Q1 AI投資$300B(B-2) |
| [INFO-034](../Information/2026-06-07/collected-raw.md#INFO-034) | OpenAI年間収益$25B・Anthropic IPO $1T可能性(A-2) |
| [INFO-036](../Information/2026-06-07/collected-raw.md#INFO-036) | BMWマルチベンダーAI戦略(B-2) |
| [INFO-037](../Information/2026-06-07/collected-raw.md#INFO-037) | ベンダーロックイン回避指針(B-2) |
| [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) | 142Kテックレイオフ・AI #1理由・87,714人分(A-1) |
| [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) | GitHub Copilot定額→従量制移行(A-2) |
| [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) | コーディングスキル40%陳腐化・インテントエンジニアリング(B-2) |
| [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) | RSI「定義された実験ではほぼ超人」(A-1) |
| [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047) | Hassabis AGI ~2030・孫正義2年・Altman/Amodei一致(A-2) |
| [INFO-048](../Information/2026-06-07/collected-raw.md#INFO-048) | AGI定義の合意不在(B-2) |
| [INFO-049](../Information/2026-06-07/collected-raw.md#INFO-049) | Anthropic AI一時停止メカニズム提案(A-2) |
| [INFO-050](../Information/2026-06-07/collected-raw.md#INFO-050) | 米中Geneva AI安全予備合意(A-2) |
| [INFO-051](../Information/2026-06-07/collected-raw.md#INFO-051) | GCP 16→22%シェア・4年+6pt(B-2) |
| [INFO-052](../Information/2026-06-07/collected-raw.md#INFO-052) | Cloud 63.4%増・AWS 28%・Big Tech $725B capex(A-2) |
| [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) | 豆包有料プロ版(A-2) |
| [INFO-054](../Information/2026-06-07/collected-raw.md#INFO-054) | Seedance 2.0無料無制限(B-2) |
| [INFO-056](../Information/2026-06-07/collected-raw.md#INFO-056) | PwC 79%本番運用・AIスティッカーショック(A-2) |
| [INFO-058](../Information/2026-06-07/collected-raw.md#INFO-058) | Claude Opus EU AI法適合率首位(B-2) |
| [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | Google I/O Capex $180-190B(A-3) |
| [INFO-028](../Information/2026-06-06/collected-raw.md#INFO-028) | Anthropic SCR指定(A-1) |
| [INFO-034](../Information/2026-06-04/collected-raw.md#INFO-034) | Google Cloud $4,600億バックログ(A-1) |
| [Arbiter v4.01](../state/arbiter-2026-06-07.md) | 確度評価の完全根拠 |
