# AI市場全体 — 静的インテリジェンス

> 最終判断更新: 2026-05-12
> 全体確信度: 中
> 情報非対称性: ByteDance / DeepSeek のグローバルシェア追跡が困難。2nd tier (Mistral / Cohere) の動向が5社比較に入っていない
> 主参照: hypotheses.json#H-GOV-001/H-OAI-001/H-OAI-002/H-CAR-002, scenarios.json#SCN-002/SCN-003, indicators.json#IND-001/003/013/022/026/027/028/029/030

## プレイヤー一覧スナップショット (2026-05-12時点)

| 企業 | 主力モデル / 製品 | 資金規模 | BenchLM | 直近の動向 |
|---|---|---|:-:|---|
| Anthropic | Claude Opus 4.7, Sonnet 4.6, Mythos, Claude Code | $3,800億評価額(Series G)。Google最大$400億 | 1位 (99) | $300億ARR。Fortune 10中8社。Claude Design(Opus 4.7)。Pentagon除外(因果未確認) |
| OpenAI | GPT-5.5, Codex (4M WAU), Agents SDK | $1,220億調達($852B評価) | 3位 (92) | $14B損失見込。DeployCo($40億+・Tomoro買収・19パートナー)設立。GPT-5.5-Cyber限定プレビュー |
| Google | Gemini 3.1シリーズ, Gemini Enterprise Agent Platform | 自己資金 + Anthropic投資 | 2位 (93) | Cloud $20B/63% YoY。AI Search围い込み深化。GTIG AIゼロデイ初検出 |
| xAI→SpaceXAI | Grok 4.3, Grok Build | SpaceX $3,500億評価 | 4位 (Grok 4.1: 90) | xAI解散→SpaceXAI統合。Colossus 1 Anthropic貸与。Pentagon 7社契約内 |
| ByteDance | 豆包2.0, Seed 2.0, Coze 2.5 | 2,000億元CAPEX(2026) | 非公開 | MAU 3.45億。有料版68/200/500元/月。DeepSeek V4 Pro 75%オフ競合 |

---

## 0. 一文要約

我々はAI市場を「性能が均質化に向かう一方、資本とエコシステムの囲い込みが少数社に集中する二重構造」と読んでいる。最大の根拠は、OSSとクローズドソースの性能ギャップがほぼ消滅した事実 [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) と、Azure排他性終了+OpenAI SDK provider-agnostic+157K OpenCode移行が示す標準化の加速 [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) だ。同時にGemini Enterprise围い込み+Doubao有料化エコシステム围い込み+エンタープライズメモリー唯一の堀が同時進行している [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009) [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042)。SCN-002/003が33%同率でQHG軸の区別能力が消失した。DeployCo $40億+の展開インフラ围い込み [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) は围い込み方向への新たな構造証拠。もしOSS/中国プレイヤーがグローバル展開で米中分断を解消するか、围い込みモデルが複数で失敗したなら、この読みは変わる。

---

## 1. コア判断

市場の構図は「技術は開くが、围い込みは深まる」という二重構造に収束し続けている。

技術面では開放の力がさらに強まった。Azure排他性が2026年4月27日に終了し、翌日にGPT-5.5がAWS Bedrockで利用可能になった [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003)。クラウドプロバイダーは「排他的流通パートナー」から「純粋な流通レイヤー」に転換した。OpenAI Agents SDKはprovider-agnosticの軽量マルチエージェントフレームワークとして展開されている [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017)。157K人の開発者がモデル非依存ツールOpenCodeに移行した [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015)。OSSとクローズドソースの性能ギャップがほぼ消滅した [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037)。NVIDIAの中国AIアクセラレータ市場シェアがゼロに低下した [INFO-014](../Information/2026-05-11/collected-raw.md#INFO-014) ことは、地政学的格差の変容を示す。

围い込み側も深まっている。Gemini Enterprise Agent Platformが構築・デプロイ・ガバナンスを一体化 [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019)。Doubao有料版3段階(68/200/500元/月)でエコシステム围い込み [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009)。Coze 2.5 Agent Worldエコシステム [INFO-021](../Information/2026-05-11/collected-raw.md#INFO-021)。Sequoiaが「エンタープライズメモリーが唯一の防御可能な堀」と宣言した [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042)。SaaSpocalypseで中間層が排除されている [INFO-041](../Information/2026-05-11/collected-raw.md#INFO-041)。EU AI Act高リスク期限が延期された [INFO-032](../Information/2026-05-11/collected-raw.md#INFO-032) ことも規制コストの低下として围い込みを促進する方向だ。

DeployCoの設立は围い込みに新たな次元を加えた。OpenAIがAPI提供から展開サービス会社に転換し、McKinsey/Bain等19パートナーとFDE常駐モデルでエンタープライス展開を囲い込む構造だ [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001)。Google AI Search 5新機能は検索エコシステムへの围い込み深化を示す [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005)。GTIGがAI開発ゼロデイを初検出したことは [INFO-006](../Information/2026-05-12/collected-raw.md#INFO-006) セキュリティ围い込み必要性を増す材料だが、検出≠被害であることに注意が必要。

雇用面では二極化が鮮明になっている。1日882人のテック職消滅 [INFO-028](../Information/2026-05-11/collected-raw.md#INFO-028) と271K新規求人 [INFO-010](../Information/2026-05-11/collected-raw.md#INFO-010) が同時進行。130万のAI関連雇用が創出された [INFO-036](../Information/2026-05-11/collected-raw.md#INFO-036)。削減は中間層に集中し、創出はAI職に偏る非対称分布が構造的になっている。

SCN-002/003が33%同率になったことで、QHG軸の区別能力が消失した。10R連続で同一方向にシフトしており、QHG象限の再定義が次回Arbiterの最優先必須条件。3R連続未実行の場合はシナリオ確率調整を凍結するペナルティ条件が設定された。

---

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Azure排他性終了+GPT-5.5 on AWS Bedrock+OpenAI SDK provider-agnostic | 標準化の最も具体的な制度化。クラウドは流通レイヤー化 | B-2 | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) |
| 高 | OSS/クローズド性能ギャップほぼ消滅 | コモディティ化の方向性を示す観測。6ヶ月前には商用が圧倒的リード | C-3 | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) |
| 高 | Gemini Enterprise Agent Platform + Doubao有料化 + エンタープライズメモリー堀 | 围い込みが配布・エコシステム・データの3次元で同時進行 | A-3 | [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009) [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042) |
| 高 | SCN-002/003確率33%同率(0%差)。10R連続同一方向シフト。QHG軸区別能力消失 | QHG象限の再定義が次回Arbiter最優先必須条件 | B-3 | scenarios.json |
| 高 | DeployCo $40億+(Tomoro買収・19パートナー・FDE常駐) | 展開インフラ围い込みの新次元。API→展開サービス会社への戦略的飛躍 | A-3 | [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) |
| 中 | 157K開発者OpenCode移行(サードパーティブロック後) | モデル非依存ツールへの需要を実証。围い込みに対する市場の反発 | C-3 | [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) |
| 中 | NVIDIA中国市場シェアゼロ。輸出規制で中国の自給自足が加速 | 地政学的格差の変容。米中AI市場の構造的分断が確定的に | C-3 | [INFO-014](../Information/2026-05-11/collected-raw.md#INFO-014) |
| 中 | 雇用二極化: 882人/日消滅 vs 271K求人 vs 130万新規 | 非対称分布が構造化。削減は中間層・創出はAI職に集中 | B-2 | [INFO-028](../Information/2026-05-11/collected-raw.md#INFO-028) [INFO-010](../Information/2026-05-11/collected-raw.md#INFO-010) [INFO-036](../Information/2026-05-11/collected-raw.md#INFO-036) |

---

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DeepSeek / ByteDance がグローバル展開でシェア10%以上を取り、米中AI市場の分断が解消される | 「3社だけが最先端」という构图と围い込み判断の双方が崩れる | 180日 | [IND-001](../config/indicators.json) |
| Agent Platformで3社以外(Mistral / Cohere等)が測定可能な10%以上のシェアを取る | 「Agent Platform三社鼎立」が崩れ、SCN-002の前提が弱まる | 180日 | [IND-027](../config/indicators.json) |
| QHG象限の再定義でSCN-002/003が統合または再区分される | 二重構造判断の軸自体が変わり、確率推移の連続性が失われる | 30日 | scenarios.json |
| EU AI Act高リスク条項が完全に撤回される | 規制コンプライアンスを差別化要因にする安全性戦略の前提が崩れる | 180日 | [IND-030](../config/indicators.json) |

---

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIはAgentをエンタープライズ特化させB2B市場を支配する | 63% | DeployCo $40億++JV $110B+Codex 4M WAUでC蓄積。$14B損失とLLMシェア27%がI。確証バイアス警告2R連続。DeployCo収益・採用実績未確認 | [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) [INFO-074](../Information/2026-05-08/collected-raw.md#INFO-074) | [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはMCP開放の上にプロプライエタリ上位レイヤーで開発者を囲い込む | 50% | 6重I蓄積(マルチクラウド+provider-agnostic+OpenCode移行)が下層開放を示し上位围い込み有効性を構造的に制約 | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) | [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) |
| [H-GOV-001](../config/hypotheses.json) | 政府が安全性姿勢を抑圧する先例が確立し業界全体に萎縮効果が生じる | 46% | Pentagon除外は萎縮Cだが因果チェーン「未確認」。DeepMind union 98%は二面性。EU延期+中国裁判所判決のI蓄積。C/I均衡 | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) | [INFO-032](../Information/2026-05-11/collected-raw.md#INFO-032) [INFO-046](../Information/2026-05-11/collected-raw.md#INFO-046) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% | Codex 12x+Cursor 47%+Claude Code $10億のC蓄積。ソフトウェア開発者求人+32.3%は需要継続I。BLS 10R未解決の時間減衰 | [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) | [INFO-010](../Information/2026-05-11/collected-raw.md#INFO-010) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流・下流に集中する | 57% | SaaSpocalypse+23K削減+AI Capex増+パートナー非媒介化+エンタープライズメモリー堀+企業再構成の5重C。方向性支持。速度不確定。確証バイアス警告 | [INFO-041](../Information/2026-05-11/collected-raw.md#INFO-041) [INFO-047](../Information/2026-05-11/collected-raw.md#INFO-047) [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042) | (速度の不確定性) |

---

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で high | OSS/クローズドギャップほぼ消滅 [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037)。BenchLM上位差6-7pt | 2026-05-12 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | 品質問題(バグ等)は観測。大規模脆弱性なし。high水準 | 2026-05-12 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+ソース<10%到達で high | CEO 83% vs CIO 25%の期待-実態ギャップ拡大。elevated水準 | 2026-05-12 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | Azure排他性終了+provider-agnostic SDK+OpenCode移行。high水準 | 2026-05-12 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 主観-客観乖離拡大で elevated | AGI timeline synthesis+AGI arms race trial+Amodei rhetoric shift。客観ベンチマーク新規なし。elevated水準 | 2026-05-12 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入vs物理制約で high | VC $2,672億(Q1)+ByteDance 2,000億元+SpaceX $3,500億+Anthropic $3,800億。high水準 | 2026-05-12 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で elevated | Pentagon 7社+DeepMind union+EU延期+中国裁判所+Sanders法案。規制二方向深化。elevated水準 | 2026-05-12 |

---

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-12 | DeployCo設立・SCN-002/003同率33%・AI Search围い込み・GTIGゼロデイを反映 | [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005) [INFO-006](../Information/2026-05-12/collected-raw.md#INFO-006) | SCN-002 34→33%・SCN-003 32→33%。同率でQHG軸区別能力消失 |
| 2026-05-12 | Azure排他性終了・OSSギャップ消滅・围い込み7重C蓄積・SCN-002/003差2%・雇用二極化を反映して全面書き直し | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) | SCN-002 37→34%・SCN-003 29→32%。差2%に縮小 |
| 2026-05-07 | Static v2構造に全面移行 | STATIC_INTELLIGENCE_v2.md 仕様適用 | 旧: 逐次トピック羅列 → 新: §0〜§7 + プレイヤー表 |
| 2026-05-06 | JV/FDE同時採用・Agent Platform三社鼎立・围い込みシグナル4重蓄積を反映 | [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) | SCN-002 44→38%・SCN-003 24→28% |

---

## 7. ブラインドスポット

- 中国市場の実態が追跡できていない。ByteDance / DeepSeek のグローバルシェアと日本・欧州での浸透状況は、5社テーブルに組み込む観測指標を持っていない。NVIDIA中国シェアゼロは観測できたが、その先の中国AIの主体性までは見えていない。
- SCN-002/003が33%同率でQHG軸の区別能力が消失した。10R連続同一方向シフト。QHG象限の再定義が次回Arbiter最優先必須条件。3R連続未実行でシナリオ確率調整凍結ペナルティ。
- DeployCo $40億+の実質額(コミットメント vs 実調達)・19パートナー排他性・FDE稼働率が未確認。全証拠がA-3(公式発表)でB-tier以上独立確認0件の分析方法論的限界。
- 2nd tier プレイヤーの動向を5社比較に入れていない。Mistral / Cohere の技術力・シェア・資金調達状況は、Agent Platform三社鼎立が本当に「鼎立」かを検証するために必要だが、評価できていない。
- 個人開発者(vs エンタープライズ)のツール選好変化を観測できていない。Claude Code・Copilot・Cursor間のシェア推移は、エコシステム围い込みの実効性を判断する重要指標だが、定量データが構造的に取れていない(KIQ-AGENT-001、37R連続未回答)。
- Pentagon除外の因果チェーンが「未確認」になったことで、H-GOV-001の評価基盤が不安定になっている。政府介入が安全性抑圧なのか安全保障要件なのかの区別が、今後の仮説評価の精度を左右する。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) | DeployCo設立($40億+・Tomoro買収・19パートナー) |
| [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005) | Google AI Search 5新機能(围い込み深化) |
| [INFO-006](../Information/2026-05-12/collected-raw.md#INFO-006) | GTIG AI開発ゼロデイ初検出 |
| [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) | Azure排他性終了・GPT-5.5 on AWS Bedrock |
| [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) | OpenAI SDK provider-agnostic・WebSocket実行モード |
| [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) | 157K開発者OpenCode移行 |
| [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) | OSS/クローズド性能ギャップほぼ消滅 |
| [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) | Gemini Enterprise Agent Platform |
| [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009) | Doubao有料版3段階(68/200/500元/月) |
| [INFO-021](../Information/2026-05-11/collected-raw.md#INFO-021) | Coze 2.5 Agent Worldエコシステム |
| [INFO-041](../Information/2026-05-11/collected-raw.md#INFO-041) | SaaSpocalypse中間層排除 |
| [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042) | エンタープライズメモリー唯一の堀(Sequoia) |
| [INFO-014](../Information/2026-05-11/collected-raw.md#INFO-014) | NVIDIA中国シェアゼロ |
| [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) | Pentagon 7社契約 |
| [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) | DeepMind union 98% |
| [INFO-032](../Information/2026-05-11/collected-raw.md#INFO-032) | EU AI Act高リスク期限延期 |
| [INFO-028](../Information/2026-05-11/collected-raw.md#INFO-028) | 882人/日テック職消滅 |
| [INFO-010](../Information/2026-05-11/collected-raw.md#INFO-010) | 271K新規求人 |
| [INFO-036](../Information/2026-05-11/collected-raw.md#INFO-036) | 130万AI関連雇用創出(LinkedIn) |
| [Arbiter v3.75](../state/arbiter-2026-05-12.md) | 確度評価の完全根拠(付録のみ参照) |
