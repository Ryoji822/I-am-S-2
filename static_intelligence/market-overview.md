# AI市場全体 — 静的インテリジェンス

> 最終判断更新: 2026-05-07
> 全体確信度: 中
> 情報非対称性: ByteDance / DeepSeek のグローバルシェア追跡が困難。2nd tier (Mistral / Cohere) の動向が5社比較に入っていない。
> 主参照: hypotheses.json#H-GOV-001/H-OAI-001/H-OAI-002/H-CAR-002, scenarios.json#SCN-002/SCN-003, indicators.json#IND-001/003/013/022/026/027/028/029/030

## プレイヤー一覧スナップショット (2026-05-07時点)

| 企業 | 主力モデル / 製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.7, Sonnet 4.6, Mythos, Claude Code | Google $40B + Amazon $25B ($900B評価協議中) | 1位 (99) | $30B ARR。JV (Blackstone/H&F/GS)。Pentagon除外 |
| OpenAI | GPT-5.5, Codex (4M WAU), Agents SDK | $122B調達 ($852B評価) | 3位 (92) | $14B損失見込。JV「The Development Company」(TPG/Brookfield $10B) |
| Google | Gemini 3.1シリーズ, Gemini Enterprise Agent Platform | 自己資金 + Anthropic投資 | 2位 (93) | Cloud $20B/63% YoY。Pentagon契約選出。従業員600+抗議 |
| xAI | Grok 4.3, Voice Agent API | $20B Series E | 4位 (Grok 4.1: 90) | Google Cloud乗り入れ。Pentagon 7社契約内 |
| ByteDance | 豆包2.0, Seed 2.0, Seed3D 2.0 | 非公開 ($520B評価) | 非公開 | MAU 3.45億。有料版¥68/月。CAC警告3アプリ |

---

## 0. 一文要約

我々はAI市場を「性能が均質化に向かう一方、资本と生態系の围い込みが少数社に集中する二重構造」と読んでいる。最大の根拠は、BenchLM上位3社の差が6-7ptまで縮まったにもかかわらず [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)、AnthropicとOpenAIが同週にPEファンドJVを設立し围い込みの「金融次元」が加わった事実 [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) だ。もし DeepSeek / ByteDance がグローバル展開で米中分断を解消するか、JVモデルが複数で失敗したなら、この読みは根底から変わる。

---

## 1. コア判断

市場の現在の構図は、「技術は開くが、围い込みは深まる」という二重構造に収束している。

技術面では開放の力が働く。Stanford 2026 AI Indexによると、OSSとフロンティアモデルの性能差は8%から1.7%に縮小した [INFO-051](../Information/2026-05-06/collected-raw.md#INFO-051)。MCPを全主要プレイヤーが採用し [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015)、エコシステム標準化が進んでいる。BenchLM上位3社の差は6-7ptで、性能だけで「勝者」を決める時代は終わりに近い。SCN-002「技術トップが3社に集中」(38%) は前ラウンドまで最有力だったが、均質化がその前提である「勝者格差の持続」を侵食している。

同時に、围い込みの力が深まっている。AnthropicがBlackstone/H&F/GS、OpenAIがTPG/Brookfield「The Development Company」を同週に設立した [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)。双方がPalantir型FDE (Forward-Deployed Engineer) モデルを採用し、PEファンドのポートフォリオ企業への優先アクセスという「金融次元」の围い込みが加わった。これはAPIの便利さや価格による旧来の囲い込みとは性質が違う。顧客とAI企業が資本で結びつく。Microsoft Agent 365 GA [INFO-026](../Information/2026-05-06/collected-raw.md#INFO-026)、Copilot credit system [INFO-050](../Information/2026-05-06/collected-raw.md#INFO-050)、ベンダーロックイン深化 [INFO-033](../Information/2026-05-06/collected-raw.md#INFO-033) と合わせて、4種類の围い込みシグナルが同時進行している (以下、「围い込みシグナル4重蓄積」と呼ぶ)。SCN-003「静かな围い込み」は3ラウンド連続で確率を上げ25→28%に達した。

この二重構造をどう読むか。技術の開放と围い込みの深化は矛盾ではなく、「開放されたインフラの上に、プロプライエタリな関係とスイッチングコストが乗る」構造として両立する。SCN-002とSCN-003の確率は現時点で38% vs 28%であり、SCN-002がまだ優位だが、4ラウンド連続でSCN-003が+1pt以上であれば逆転は観測の問題になる。因果は未検証だが、現在の观测の延長線上にその可能性がある。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Anthropic・OpenAI同週JV設立。各々PEファンドとFDEモデルを採用 | 围い込みに「金融次元」が加わった最初の観測。API便利さとは異なる資本結合 | B-2 | [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) |
| 高 | BenchLM Mythos 99・Gemini 3.1 93・GPT-5.4 92。上位3社差が6-7pt | 性能格差が「勝者独占」の維持に十分かという問いを開く | A-3 | [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) |
| 高 | OSS対フロンティア性能差 8%→1.7% (Stanford 2026 AI Index) | コモディティ化の方向性を示す最も信頼性の高い観測。但しBenchLM上位12pt差は残る | B-2 | [INFO-051](../Information/2026-05-06/collected-raw.md#INFO-051) |
| 高 | 围い込みシグナル4重蓄積: MSFT Agent 365 GA + Copilot credit + ベンダーロックイン深化 + JV金融次元 | 个別シグナルは非固有だが、4種同時進行は構造的変化の兆候と読む | C-3 | [INFO-026](../Information/2026-05-06/collected-raw.md#INFO-026) [INFO-050](../Information/2026-05-06/collected-raw.md#INFO-050) [INFO-033](../Information/2026-05-06/collected-raw.md#INFO-033) [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) |
| 中 | SCN-003確率推移: 24→25→26→27→28% (5ラウンド連続上昇) | 围い込みシナリオが統計的に支持され続けている方向性を示す | B-3 | scenarios.json |
| 中 | D&B 10,000社調査: 97%がAI活動報告、30%が本番スケール移行 [INFO-034](../Information/2026-05-06/collected-raw.md#INFO-034)。パイロット→本番18% (Q1 2026) [INFO-035](../Information/2026-05-06/collected-raw.md#INFO-035) | エンタープライズ採用が加速する局面は、围い込みが有効に働く最も重要なタイミング | B-2 | [INFO-034](../Information/2026-05-06/collected-raw.md#INFO-034) [INFO-035](../Information/2026-05-06/collected-raw.md#INFO-035) |
| 中 | 3社合算CapEx ~$560B [INFO-042](../Information/2026-05-06/collected-raw.md#INFO-042)。Anthropic $900B評価額協議 [INFO-052](../Information/2026-05-06/collected-raw.md#INFO-052) | 资本集中は技術の開放と並行して起きている。インフラ構築コストが参入障壁として機能 | C-3 | [INFO-042](../Information/2026-05-06/collected-raw.md#INFO-042) [INFO-052](../Information/2026-05-06/collected-raw.md#INFO-052) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DeepSeek / ByteDance がグローバル展開でシェア10%以上を取り、米中AI市場の分断が解消される | 「3社だけが最先端」という构图と围い込み判断の双方が崩れる。5社テーブルの外から競争が来る | 180日 | [IND-001](../config/indicators.json) |
| AnthropicとOpenAIの両JVのうち1件以上が設立から12ヶ月以内に顧客離れまたは解散 | 「金融次元の围い込み」がFDE戦略の有効性の核心を失う。SCN-003の根拠が一つ消える | 365日 | [IND-003](../config/indicators.json) |
| Agent Platformで3社以外 (Mistral / Cohere等) が測定可能な10%以上のシェアを取る | 「Agent Platform三社鼎立」が崩れ、SCN-002の前提が弱まる | 180日 | [IND-027](../config/indicators.json) |
| 4ラウンド連続でSCN-002が+2pt以上かつSCN-003が±0%以下 | 均質化が「勝者格差の侵食」ではなく「勝者格差の維持」に転じたと読む。二重構造判断の修正が要る | 120日 | scenarios.json |
| EU AI Act高リスク条項の執行停止または大幅延期 | 規制コンプライアンスを差別化要因にする安全性差別化戦略 (H-GOV-001) の前提が崩れる | 60日 | [IND-030](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIは2026年内にAgentをエンタープライズ特化させB2B市場を支配する | 63% | JV $10BとCodex 4M WAUはC。$14B損失と価格2倍がI。C/I均衡で medium | [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) [INFO-022](../Information/2026-05-06/collected-raw.md#INFO-022) | [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで开発者を囲い込む | 53% | Symphony OSS・MSFT非独占・OpenAI on AWSの3件A-3独立Iが下層開放を示し上位囲い込み有効性を構造的に制約 | (Skills利用数増加) | [INFO-003](../Information/2026-05-06/collected-raw.md#INFO-003) [INFO-021](../Information/2026-05-06/collected-raw.md#INFO-021) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し、業界全体に萎縮効果が生じる | 46% | Pentagon除外はC vs 市場喪失Iの二面性。EU AI Act 8/2執行確定はC。CAISI事前評価はI。次回INFO-073以外の独立C不可欠 | [INFO-040](../Information/2026-05-06/collected-raw.md#INFO-040) | [INFO-065](../Information/2026-05-06/collected-raw.md#INFO-065) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 70% | プログラマー-27.5%・ジュニア採用-22%・Salesforce 4000CS削減はC蓄積。BLS職業分類定義問題が方法論的地盤を不安定にしている。BLS問題のA-3以上解決で+1%復帰 | [INFO-058](../Information/2026-05-06/collected-raw.md#INFO-058) [INFO-062](../Information/2026-05-06/collected-raw.md#INFO-062) [INFO-077](../Information/2026-05-06/collected-raw.md#INFO-077) | BLS職業分類定義問題 |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流・下流に集中する | 57% | ウォール街AI雇用削減はC。Klarna再雇用はI。中間圧縮の方向性は支持されるが速度が不確定 | (中間職削減データ) | [INFO-044](../Information/2026-05-06/collected-raw.md#INFO-044) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ (前世代比30%超) | 非連続ジャンプ観測で high | BenchLM: Mythos 99 / Gemini 93 / GPT-5.4 92。上位差6-7pt | 2026-05-06 |
| [IND-003](../config/indicators.json) | 資金集中 (上位3社が業界調達額80%超) | 80%超で high | 3社合算CapEx ~$560B。Anthropic $900B評価協議 | 2026-05-06 |
| [IND-013](../config/indicators.json) | AI安全性インシデント (月3件超) | 月3件超で high | AIエージェント本番DB削除。24.4%のみAI完全可視性 | 2026-05-06 |
| [IND-022](../config/indicators.json) | スキル再定義 (コーディング価値がAI管理にシフト) | 測定可能な職種別雇用変化 | プログラマー-27.5%。ジュニア-22%。Salesforce 4000CS削減 | 2026-05-06 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソースで<10%到達ならhigh | D&B 30%本番スケール。パイロット→本番18%。Cisco 5%・Fortune <10%で2ソース確認 | 2026-05-06 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度 (MCP/A2A採用率) | MCP 110M+DL/月で high | MCP全主要プレイヤー対応。Red Hat MCP Gateway。Skills Marketplace | 2026-05-06 |
| [IND-028](../config/indicators.json) | AGI到達度指標 (主観-客観乖離) | 主観・客観の乖離拡大で elevated | Hassabis ~2030。Bubeck「AGIは創造企業にアライン」。ARC-AGI-3新ベンチ登場 | 2026-05-06 |
| [IND-029](../config/indicators.json) | AIインフラ制約 (計算能力投資の物理的限界) | 資本流入vs物理制約ギャップ継続で high | 3社合算CapEx ~$560B。Sierra $950M Series E | 2026-05-06 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 (同時進行件数) | 同時進行3件で elevated | CAISI事前評価。EU AI Act 8/2執行確定。Pentagon 7社契約 | 2026-05-06 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-07 | Static v2構造に全面移行 | STATIC_INTELLIGENCE_v2.md 仕様適用。予測・規範分離、反証可能条件の明示化 | 旧: 逐次トピック羅列 → 新: §0〜§7 + プレイヤー表の v2 構造 |
| 2026-05-06 | コア判断・SCN確率更新 | JV/FDE同時採用・Agent Platform三社鼎立・围い込みシグナル4重蓄積・BenchLMランキング | SCN-002 44→38%・SCN-003 24→28% |
| 2026-04-29 | 三大クラウドAgent Platform同一週リリース反映 | MSFT提携改訂・OpenAI on AWS | SCN-002 +2%・三社鼎立を主軸に据える |
| 2026-04-22 | エンタープライズ決戦クラスター・インフラ過熱を反映 | 複数CapEx更新 | コア判断を「寡占 vs 分散」から「二重構造」へ |
| 2026-04-17 | 72時間4社同時エージェントリリース反映 | 4社同時発表 | Agent Platform が市場構造の主軸に |

---

## 7. ブラインドスポット

- **中国市場の実態が追跡できていない。** ByteDance / DeepSeek のグローバルシェアと日本・欧州での浸透状況は、5社テーブルに組み込む観測指標を持っていない。APIの価格比較 (DeepSeek $1.74/$3.48 vs Claude $5/$30) は見えているが、実シェアの変化は見えない。
- **2nd tier プレイヤーの動向を5社比較に入れていない。** Mistral / Cohere / Inflection の技術力・シェア・资金調達状況は、Agent Platform三社鼎立が本当に「鼎立」かを検証するために必要だが、現在は評価できていない。
- **規制動向の影響を仮説評価に十分織り込めていない。** EU AI法・CHIPS法・Executive Orderの影響は定性的に言及しているが、どの仮説の確度をどれだけ変化させるかのロジックが薄い。
- **JVモデルの実効性が未検証のまま判断に組み込まれている。** AnthropicとOpenAIのJVがPEファンドの顧客基盤に実際にリーチできるか、FDEモデルがAI以外の業種でどう機能するかは、設立直後のため観測データがない。
- **個人開発者 (vs エンタープライズ) のツール選好変化を観測できていない。** Claude Code・Copilot・Cursor間のシェア推移は、エコシステム围い込みの実効性を判断する重要指標だが、解約率・定着率データが構造的に取れていない (KIQ-AGENT-001、30R連続未回答)。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) | JV同週設立 (Anthropic+OpenAI)。FDEモデル確認 |
| [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) | BenchLMランキング (Mythos 99/Gemini 93/GPT-5.4 92) |
| [INFO-051](../Information/2026-05-06/collected-raw.md#INFO-051) | OSS対フロンティア性能差 8%→1.7% (Stanford 2026 AI Index) |
| [INFO-026](../Information/2026-05-06/collected-raw.md#INFO-026) | Microsoft Agent 365 GA |
| [INFO-050](../Information/2026-05-06/collected-raw.md#INFO-050) | Copilot credit system |
| [INFO-033](../Information/2026-05-06/collected-raw.md#INFO-033) | ベンダーロックイン深化 |
| [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015) | MCP全主要プレイヤー対応 |
| [INFO-034](../Information/2026-05-06/collected-raw.md#INFO-034) | D&B 10,000社調査 (97%/30%本番スケール) |
| [INFO-035](../Information/2026-05-06/collected-raw.md#INFO-035) | パイロット→本番移行率 18% (Q1 2026) |
| [INFO-042](../Information/2026-05-06/collected-raw.md#INFO-042) | 3社合算CapEx ~$560B |
| [INFO-052](../Information/2026-05-06/collected-raw.md#INFO-052) | Anthropic $900B評価額協議 |
| [INFO-058](../Information/2026-05-06/collected-raw.md#INFO-058) | プログラマー雇用 -27.5% (2023-2025) |
| [INFO-062](../Information/2026-05-06/collected-raw.md#INFO-062) | GenAI採用企業のジュニア採用 -22% |
| [INFO-077](../Information/2026-05-06/collected-raw.md#INFO-077) | Salesforce CEOが4000 CS職削減を確認 |
| [INFO-040](../Information/2026-05-06/collected-raw.md#INFO-040) | EU AI Act高リスク期限 2026-08-02確定 |
| [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) | OpenAI $14B損失見込 |
| [INFO-009](../Information/2026-05-06/collected-raw.md#INFO-009) | AIエージェントが本番DB削除インシデント |
| [INFO-036](../Information/2026-05-06/collected-raw.md#INFO-036) | 24.4%の組織のみAIエージェントへの完全可視性 |
