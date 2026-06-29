# 収集データ: 2026-06-29

## メタデータ
- 収集日時: 2026-06-29 00:13 UTC (収集完了: 2026-06-29 01:05 UTC)
- 品質フラグ: COMPLETE
- 収集規模: 68件 (INFO-001〜INFO-068)
- Evidence ID範囲: EVD-20260629-0001〜EVD-20260629-0068
- 検索クエリ数: 18件（Arbiter動的6件 + collection_plan 全24 KIQ × 複数クエリ）
- スクレイプ数: 5件（公式ブログ3 + ディープスクレイプ2）
- KIQカバレッジ: 24/24（100%）— collection_plan.json の全KIQをカバー
- 企業カバレッジ（Tier 1）:
  - OpenAI: 50言及
  - Anthropic: 83言及
  - Google/DeepMind: 41言及
  - xAI/Grok: 30言及
  - ByteDance/Doubao: 24言及
- Arbiter優先KIQ対応状況:
  - KIQ-MIL-001 (Grok標的選定): INFO-004/005 で対応
  - H-ANT-002-DAU (Claude Code DAU): INFO-006 で対応（公式DAU未公表）
  - KIQ-OAI-001 (OpenAI収益内訳): INFO-007 で対応（API/Enterprise/Consumer内訳非公表）
  - H-GOV-001-XVAL (SCR後Anthropic連邦調達): INFO-008/064/067 で対応
  - H-GOV-002-ABS (安全性予算推移): INFO-009/067 で対応（直接予算推移データ限定的）
  - SCN-005-CB (クロスボーダーAI契約): INFO-010 で対応（契約レベルデータ限定的）
- データギャップ・注意事項:
  - KIQ-003-03 (OSS vs 商用モデル性能ギャップ): INFO 1件のみ — 情報源限定的
  - KIQ-004-04 (AI時代勝者企業条件): INFO 1件のみ — 定量的企業評価データ不足
  - H-ANT-002-DAU: Claude Code公式DAUデータ存在せず（推定値のみ）
  - H-GOV-002-ABS: 各社安全性予算の直接公開データ存在せず（間接的証拠のみ）
  - SCN-005-CB: 契約レベルのクロスボーダー取引データ限定的
- 動的追加クエリ（Arbiter Step 1.5）:
  - KIQ-MIL-001 (Grok標的選定関与度・人間却下比率): "Grok autonomous target selection military Pentagon human override", "xAI Grok weapon targeting human-in-the-loop verification", "Pentagon DoD doctrine AI target selection algorithm Grok 2026"
  - H-ANT-002-DAU (Claude Code DAU vs installs): "Claude Code daily active users DAU 2026", "Anthropic Claude Code enterprise adoption install numbers", "Claude Code usage statistics developer adoption rate"
  - KIQ-OAI-001 (OpenAI収益内訳 API/Enterprise/Consumer): "OpenAI revenue breakdown API enterprise consumer 2026", "OpenAI financial report segment revenue ChatGPT Plus Team Enterprise"
  - H-GOV-001-XVAL (SCR後Anthropic連邦調達収益): "Anthropic federal procurement revenue post SCR suspension", "US federal AI contract spending Anthropic 2026"
  - H-GOV-002-ABS (AI safety研究予算経時減少): "AI company safety research budget decline trend 2026", "Anthropic OpenAI DeepMind safety alignment spending 2025 2026"
  - SCN-005-CB (クロスボーダー AI契約): "cross-border AI services trade US EU China 2026", "global AI contract value cross-region transactions trend"

## 収集結果

### INFO-001
- **タイトル:** Previewing GPT-5.6 Sol: a next-generation model
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-06-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIが次世代モデルGPT-5.6シリーズ（Sol/Terra/Luna）の限定プレビューを開始。Sol/Terra/Lunaの3階層体制で、TerraはGPT-5.5同等性能で2倍低コスト。Terminal-Bench 2.1でSol Ultra 91.9%（Claude Mythos 5は84.3%）。政府との調整で限定的な信頼パートナー向けプレビューから開始する新規リリースプロセス採用。
- **キーファクト:**
  - GPT-5.6 Sol: Terminal-Bench 2.1 91.9%（Claude Mythos 5 84.3%を上回る）
  - 3モデル構成: Sol（$5/$30）・Terra（$2.50/$15）・Luna（$1/$6）
  - 米政府の要請で「限定的信頼パートナー向けプレビュー」から開始する新プロセス確立
  - 反復可能プロセス開発中・サイバーEO枠組みと協調
  - 70万A100相当GPU時間で自動レッドチーム実施・普遍的ジェイルブレイク探索
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260629-0001

### INFO-002
- **タイトル:** Interactions API: our primary interface for Gemini models and agents
- **ソース:** Google (公式ブログ)
- **公開日:** 2026-06-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** GoogleがInteractions APIをGA（一般提供開始）し、Geminiモデル/エージェントの主要APIに位置付け。2025年12月ベータからGA化し、Managed Agents・バックグラウンド実行・Gemini Omni（近日）等を追加。レガシーgenerateContent APIは継続サポートするが、フロンティア機能は順次Interactions API専用に。
- **キーファクト:**
  - Interactions APIがGeminiの主要APIに昇格（ドキュメントもデフォルト化）
  - Managed Agents: リモートLinuxサンドボックス・Antigravityエージェントがデフォルト
  - バックグラウンド実行・Google Search/Maps連携・画像返却対応
  - Flex/Priorityティア（Flexは50%コスト削減）
  - LiteLLM/Eigent/Agno等3P SDK統合開始
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/
- **Evidence ID:** EVD-20260629-0002

### INFO-003
- **タイトル:** Introducing Claude Corps
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02, KIQ-004-03
- **関連企業:** Anthropic
- **要約:** Anthropicが「Claude Corps」全国フェローシッププログラムを発表。初期投資$150Mで1000人フェローを訓練し、全米非営利団体に1年間フルタイム配置。CodePath（雇用主）・Social Finance（評価）と提携。AI普及による労働市場変化への責任投資位置づけ。
- **キーファクト:**
  - 初期投資$150M・1年間フルタイム・$85,000年俸+福利厚生
  - 400以上の非営利団体がホスト・1000人規模を目標
  - CodePath（雇用主）・Social Finance（評価）との3社パートナーシップ
  - AI政策枠組み"Policy on the AI Exponential"と同時発表
  - Goodwill・RAINN・YMCA・Team RWB等の主要非営利参加
- **引用URL:** https://www.anthropic.com/news/claude-corps
- **Evidence ID:** EVD-20260629-0003

### INFO-004
- **タイトル:** Pentagon official confirms Grok used in 2,000 munitions targeting (Iran strikes)
- **ソース:** Bloomberg (LinkedIn repost) / 複数SNS報道
- **公開日:** 2026-06-22
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-MIL-001 (Arbiter動的優先・9R連続未回答)
- **関連企業:** xAI
- **要約:** Pentagon上級AI担当官の法廷宣誓陳述で、Elon Musk氏のGrok AIがイラン攻撃作戦で2,000発以上の標的指定に使用されたと確認。標的選定関与度が初めて定量的に示された。human-in-the-loopからhuman-on-the-loopへの移行が示唆される。Bloombergが2026年4月改訂の共同標的ドクトリン（非公開）を閲覧しAI役割拡大を確認。
- **キーファクト:**
  - Grokがイラン作戦で2,000標的・96時間以内の攻撃を支援
  - Pentagon上級AI担当官の「法廷宣誓陳述」で確認（初の公式証言）
  - 「human-in-the-loopからhuman-on-the-loopへの移行」の発言
  - Grokが極秘ネットワーク上で稼働中と政府が主張
  - データセンターモラトリアムが「国家安全保障上の脅威」と政府が論じた
- **引用URL:** https://www.linkedin.com/posts/katrinamanson_pentagon-sees-broader-role-for-ai-in-setting-activity-7476259554775871488-Bs-A
- **Evidence ID:** EVD-20260629-0004

### INFO-005
- **タイトル:** Maven Smart System combined with Grok for Iran strikes (1,000+ targets in 24h)
- **ソース:** Instagram/Social media reposts of major outlets
- **公開日:** 2026-06-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-MIL-001
- **関連企業:** xAI, Palantir
- **要約:** PalantirのMaven Smart System（Project Maven由来）とGrokの統合がイラン攻撃で活用。初24時間で1,000標的特定。衛星画像・レーダー・信号情報の統合プラットフォーム。
- **キーファクト:**
  - Maven Smart System: Palantir AI標的プラットフォーム（Pentagon 2017 Project Maven由来）
  - イラン初24時間で1,000標的特定
  - 衛星画像・レーダー・SIGINT統合
  - GrokとMavenの統合が推測される（直接証拠は限定的）
- **引用URL:** https://www.instagram.com/reel/DaItkQlhQWe/
- **Evidence ID:** EVD-20260629-0005

### INFO-006
- **タイトル:** Claude Code enterprise adoption rising (3%→24% US), but no DAU figures
- **ソース:** Uvik Software / industry analysis
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** H-ANT-002-DAU (Arbiter動的優先・9R連続不在)
- **関連企業:** Anthropic
- **要約:** Claude Code認知率・採用率が上昇（2025年中3%→2026年1月18%→2026年6月24% US）。しかし**依然としてDAU数値の公式発表は不在**（9R連続未回答継続）。Cursorは1M+ DAU（2025報告）で対比継続。
- **キーファクト:**
  - Claude Code採用率: 2025年中3% → 2025年9月12% → 2026年1月18% → 2026年6月24%（米国）
  - DAU数値の公式発表は依然不在（Arbiter閾値9R連続超過継続）
  - Cursor: 1M+ DAU（2025年報告）との対比で競合劣位継続
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/
- **Evidence ID:** EVD-20260629-0006

### INFO-007
- **タイトル:** OpenAI financial picture: $25B run rate vs $14B annual loss
- **ソース:** 多数報道（Bloomberg/Reuters/The Business Times集約）
- **公開日:** 2026-06-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001 (Arbiter動的優先)
- **関連企業:** OpenAI
- **要約:** OpenAI財務の流出報道: 年間収益約$25Bランレート・年間$14B赤字。2025年12月末時点$20B収益。リーク財務諸表で2024年$13B収益vs$21B損失。詳細なAPI/Enterprise/Consumer内訳は依然非公開。2029年キャッシュフロー黒字化予想。IPO見送り方針。
- **キーファクト:**
  - 収益ランレート: $25B+（年率・Reuters）
  - 2024年実績: $13B収益 vs $21B損失
  - 2025年12月末: $20B+収益
  - 年間$14B赤字バーン
  - API/Enterprise/Consumerのセグメント内訳は非公開（KIQ-OAI-001核心未回答）
  - 2029年キャッシュフロー黒字化想定・IPO見送り
- **引用URL:** https://kakashiii111.substack.com/p/thoughts-of-the-week-june-28-2026
- **Evidence ID:** EVD-20260629-0007

### INFO-008
- **タイトル:** US suspension of Anthropic models prompts AI sovereignty calls
- **ソース:** Computer Weekly
- **公開日:** 2026-06-18
- **信頼性コード:** B-2
- **関連KIQ:** H-GOV-001-XVAL (Arbiter動的優先), H-GOV-001
- **関連企業:** Anthropic
- **要約:** Anthropicモデルの米政府アクセス停止指令が「AI主権」への懸念を喚起。Fable 5・Mythos 5の輸出管理指令。SCR指定後の連邦調達収益推移の直接データは依然不在（H-GOV-001-XVAL核心未回答）。
- **キーファクト:**
  - 6月18日付で「Anthropicモデル停止指令がAI主権懸念を喚起」報道
  - Fable 5/Mythos 5の輸出管理指令
  - 他国（欧州等）の「AI主権」ムーブメント加速
  - 連邦調達収益の定量的推移データは依然不在
- **引用URL:** https://www.computerweekly.com/resources/Data-protection-backup-and-archiving
- **Evidence ID:** EVD-20260629-0008

### INFO-009
- **タイトル:** AI budgets tightening; companies prioritize ROI over growth
- **ソース:** CNBC
- **公開日:** 2026-06-28
- **信頼性コード:** B-2
- **関連KIQ:** H-GOV-002-ABS (Arbiter動的優先), KIQ-002-02
- **関連企業:** OpenAI, Anthropic
- **要約:** 企業のAI予算が収益重視にシフト。OpenAIは年間数十億ドル赤字で成長優先、2029年にキャッシュフロー黒字化予定。Anthropicは$30B資金調達で評価額$900B（OpenAI超越）。H-GOV-002核心（安全性研究予算の経時的減少）の直接データは依然不在。
- **キーファクト:**
  - Anthropic: $30B調達・評価額$900B（OpenAI$852Bを超過）
  - OpenAI: 年間数十億ドル赤字・成長優先・2029年黒字化
  - 「資金は最大級フロンティアラボに集中」傾向
  - 安全性研究予算の経時的定量データは依然不在（H-GOV-002核心未回答）
- **引用URL:** https://www.facebook.com/cnbc/posts/companies-are-tightening-their-ai-budgets-to-focus-on-getting-a-return-on-their-/1408711621130227/
- **Evidence ID:** EVD-20260629-0009

### INFO-010
- **タイトル:** BIS: $1T hyperscaler AI capex 2025-26; cross-border AI investment tensions
- **ソース:** Bank for International Settlements (BIS) 年次報告書
- **公開日:** 2026-06-28
- **信頼性コード:** A-3
- **関連KIQ:** SCN-005-CB (Arbiter動的優先), KIQ-003-04
- **関連企業:** hyperscalers（AWS/Azure/GCP）
- **要約:** BIS年次報告書: 主要5ハイパースケーラーが2025-26年に$1兆超のAI関連資本支出計画。クロスボーダーAI投資の緊張拡大。EUが中国の低コスト商品（AI含む）ゲートクローズへ追従。SCN-005の「ブロック間分裂」概念を支持する間接証拠だが、直接的クロスボーダーAI契約定量データは限定的。
- **キーファクト:**
  - 主要5ハイパースケーラー: 2025-26年$1T+ AI資本支出
  - クロスボーダーAI投資の地政学的緊張拡大
  - EUが中国低コストAIゲートクローズに追従（米国に同調）
  - Taiwan AI servers/semis 輸出$67.42B; China輸出-35% YoY 2026年1月
- **引用URL:** https://www.bis.org/publ/arpdf/ar2026e1.htm
- **Evidence ID:** EVD-20260629-0010

### INFO-011
- **タイトル:** xAI launches /goal in Grok Build with long-running autonomous execution
- **ソース:** MarkTechPost / xAI公式
- **公開日:** 2026-06-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI
- **要約:** xAIがGrok Build（ターミナルコーディングエージェント）に「/goal」モードを追加。長時間実行・自律的タスク実行を可能にし、多段階コーディングタスク向けの組込み検証機構を提供。Grok 4.20モデル（推論/非推論/multi-agent beta）のAPIエイリアス公開。
- **キーファクト:**
  - /goal: Grok Build内の新長時間自律実行モード
  - 組込み検証機構（multi-step coding tasks向け）
  - Grok 4.20 APIエイリアス公開（6月24日時点）: reasoning/non-reasoning/multi-agent beta
  - xAI Voice Agent APIツール構成機能
- **引用URL:** https://www.marktechpost.com/2026/06/22/xai-launches-goal-in-grok-build-adding-long-running-autonomous-execution-with-built-in-verification-for-multi-step-coding-tasks/
- **Evidence ID:** EVD-20260629-0011

### INFO-012
- **タイトル:** Claude Code / Agent SDK TypeScript parity; Claude Opus 4.8 release
- **ソース:** Anthropic (GitHub changelog) / SNS報道
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScriptがClaude Code v2とパリティ達成。モデル情報にsupportsEffort/supportedEffortLevels/supportsAdaptiveThinkingを追加。Claude Opus 4.8（5月28日リリース）はコードレビューで4倍高い欠陥検出率。
- **キーファクト:**
  - Claude Agent SDK TypeScript v2でClaude Codeとパリティ
  - supportsEffort/supportedEffortLevels/supportsAdaptiveThinking追加
  - Claude Opus 4.8: 4倍少ないコード欠陥見逃し率
  - AnthropicがClaude Code課金変更を一時停止
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/CHANGELOG.md
- **Evidence ID:** EVD-20260629-0012

### INFO-013
- **タイトル:** Claude API outages: daily elevated errors, Notion 12-hour disruption
- **ソース:** LinkedIn / Instagram (業界報道)
- **公開日:** 2026-06-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01 (SLA), KIQ-002-01
- **関連企業:** Anthropic
- **要約:** Claude APIの継続的障害が顕在化。今月ほぼ毎日「elevated-error incidents」発生。Notionが12時間サービス障害後にAnthropic統合を一時無効化し復旧。AIベンダーはSLA提供なし、エンタープライズのfour-nines SLAと非互換。
- **キーファクト:**
  - Claude API月間ほぼ毎日elevated-error incidents
  - NotionのAnthropic統合12時間停止→一時無効化→復旧
  - AIベンダーはSLA提供なし
  - 4-nines SLA前提のエンタープライズとの非互換性
- **引用URL:** https://www.linkedin.com/posts/mikhaelf_elevated-errors-for-claude-opus-48-activity-7474914618830815232-ix9E
- **Evidence ID:** EVD-20260629-0013

### INFO-014
- **タイトル:** Enterprise AI compliance: AWS Bedrock and Azure OpenAI both hold FedRAMP High
- **ソース:** TechnologyMatch
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** AWS, Microsoft, Google
- **要約:** エンタープライズAIのコンプライアンス比較: AWS BedrockとAzure OpenAIは共にFedRAMP High認可（関連US政府リージョン）。標準エンタープライズ（SOC 2/ISO/GDPR）は主要3社対応。SOC 2監査がAIエージェントワークフローに新たな問いを投げかけ、ログ整合性課題を顕在化。
- **キーファクト:**
  - AWS Bedrock: FedRAMP High認可
  - Azure OpenAI: FedRAMP High認可
  - 標準SOC 2/ISO/GDPR: 主要3社対応
  - SOC 2監査がAIエージェントワークフローに未対応領域
- **引用URL:** https://technologymatch.com/blog/aws-bedrock-vs-azure-openai-vs-google-vertex-ai-enterprise-ai-comparison
- **Evidence ID:** EVD-20260629-0014

### INFO-015
- **タイトル:** ByteDance Coze platform: 60+ prebuilt components; ByteDance MAU dip
- **ソース:** DigitalByDefault / AInChina
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-002-02
- **関連企業:** ByteDance, Tencent
- **要約:** ByteDanceのCoze（ノーコードAIエージェントビルダー）は60以上のプリビルトコンポーネントで視覚的にエージェント構築可能。Tencentは10億ユーザー規模でAIエージェント展開。ByteDanceは2026年4月にMAU 345M→336Mに減少（競合激化）。
- **キーファクト:**
  - Coze: 60+プリビルトコンポーネント・ノーコードエージェント構築
  - Tencent: 10億ユーザー規模でAIエージェント展開
  - ByteDance MAU: 345M（2026年前）→336M（2026年4月）・減少傾向
- **引用URL:** https://www.ainchina.com/blog/china-ai-agent-revolution-2026/
- **Evidence ID:** EVD-20260629-0015

### INFO-016
- **タイトル:** Anthropic hiring Security Controls Assurance Lead; Mythos chains NSA vulns
- **ソース:** Anthropic job posting / Kiteworks
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがSecurity Controls Assurance Leadを採用（FedRAMP/multi-framework SOC 2/ISO portfolios経験必須）。Mythos AIがレッドチームテストでNSAシステム脆弱性を「数時間」でチェーン化。ゼロトラストAIガバナンスのエンタープライズ対応急務を示す。
- **キーファクト:**
  - AnthropicがSecurity Controls Assurance Lead採用（FedRAMP/SOC 2/ISO portfolios）
  - Mythos AI: NSAシステム脆弱性を「数時間」でチェーン化
  - Anthropic Zero Trust for AI Agents framework公開
- **引用URL:** http://job-boards.greenhouse.io/anthropic/jobs/5250063008
- **Evidence ID:** EVD-20260629-0016

### INFO-017
- **タイトル:** BARR: "Feds Pull Plug on Anthropic AI Models" - Fable 5/Mythos 5 suspension confirmed
- **ソース:** BARR Advisory
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, H-GOV-001
- **関連企業:** Anthropic
- **要約:** BARR Advisory月次サイバーセキュリティヘッドラインで「Feds Pull Plug on Anthropic AI Models」を掲載。米政府がAnthropicにFable 5/Mythos 5への外国人アクセス停止を命令したことを確認。
- **キーファクト:**
  - 米政府命令でAnthropic Claude Fable 5/Mythos 5への外国人アクセス停止
  - BARR Advisory月次Top 5ヘッドライン入り
- **引用URL:** https://www.barradvisory.com/resource/top-5-headlines-june-2026/
- **Evidence ID:** EVD-20260629-0017

### INFO-018
- **タイトル:** GitHub Copilot missed 99.9% SLA; Microsoft routed workloads to AWS
- **ソース:** LinkedIn (Frank Tepas repost)
- **公開日:** 2026-06-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Microsoft, GitHub, AWS
- **要約:** GitHubのAIエージェントが99.9%エンタープライズSLAを大幅に下回り、MicrosoftがワークロードをAWSにルーティング開始。Copilotは6月11日にダウン。エンタープライズSLA未達の典型例。Gemini Enterprise Agent Platformはグローバルエンドポイント対応。
- **キーファクト:**
  - GitHub Copilot: 99.9% SLA大幅下回り・6月11日ダウン
  - MicrosoftがワークロードをAWSにルーティング（競合先への流出）
  - Gemini Enterprise Agent Platform: グローバルエンドポイント対応
- **引用URL:** https://www.linkedin.com/posts/franktepas_agent-platform-memory-bank-gemini-enterprise-activity-7475335324601114624-0qdj
- **Evidence ID:** EVD-20260629-0018

### INFO-019
- **タイトル:** Agentic ERP mainstream: 75,000 businesses; Enterprise AI 300M weekly users / 90% F500
- **ソース:** LyntxGlobal / CovalenseGlobal
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** 多数
- **要約:** アジェンティックERPが75,000顧客（70カ国）で本番稼働。AIエージェントが仕訳作成・レシート投稿・請求書処理・在庫チェック実行。エンタープライズAIは3億週次ユーザー・Fortune 500の90%に浸透。FedRAMP 2026.06.25.01ルール更新（6月25日）。
- **キーファクト:**
  - アジェンティックERP: 75,000顧客・70カ国・本番稼働
  - 仕訳作成・レシート投稿・請求書処理・在庫チェック自動化
  - エンタープライズAI: 3億週次ユーザー・F500の90%浸透
  - FedRAMP 2026.06.25.01ルール更新（6月25日）
- **引用URL:** https://www.lyntxglobal.com/blog/agentic-erp-mainstream-75000-businesses-mid-market-adoption-case-study-lessons
- **Evidence ID:** EVD-20260629-0019

### INFO-020
- **タイトル:** MCP 2026-07-28 Release Candidate published; AAIF adoption metrics
- **ソース:** MCP blog / Agentic AI Foundation (AAIF)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic, OpenAI, Google DeepMind, Linux Foundation
- **要約:** MCP仕様の2026-07-28 RC公開: ステートレスプロトコルコア・Extensions framework・Tasks追加。Anthropic 2024年11月公開→OpenAI 2025年3月採用→Google DeepMind追随でde facto標準化。AAIF報告: MCP採用の大部分はクラウド環境（大規模モデル・豊富なコンピュート予算）。製造現場・医療機器での採用は限定的。
- **キーファクト:**
  - MCP 2026-07-28 RC: ステートレスコア・Extensions framework・Tasks導入
  - de facto標準化（Anthropic→OpenAI→Google DeepMindの1年内採用）
  - AAIF: MCP採用は主にクラウド環境中心・エッジデバイスは限定的
  - Linux Foundation: AGENTS.md規格が60,000+プロジェクト採用
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260629-0020

### INFO-021
- **タイトル:** 1000+ cross-vendor agent skills (VoltAgent); Claude Code Codex Gemini CLI Cursor互換
- **ソース:** VoltAgent GitHub / LobeHub Skills Marketplace
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Claude Code, Codex, Gemini CLI, Cursor, LobeHub
- **要約:** VoltAgentが1000以上のクロスベンダーエージェントスキルコレクションを公開。Claude Code/Codex/Gemini CLI/Cursor等主要ツール間で互換性確保。LobeHub Skills Marketplace/Firebase agent skills等のディストリビューション拡大。スキル層での相互運用性が進展。
- **キーファクト:**
  - 1000+エージェントスキル（公式dev teams+コミュニティ）
  - Claude Code/Codex/Gemini CLI/Cursor等主要ツール間互換
  - LobeHub Skills Marketplace/Firebase agent skills等の配信網
  - スキル層の相互運用性進展
- **引用URL:** https://github.com/voltagent/awesome-agent-skills
- **Evidence ID:** EVD-20260629-0021

### INFO-022
- **タイトル:** Adobe CX Enterprise Coworker + Marketing Agent across AWS; Okta XAA for AI agent governance
- **ソース:** Adobe News / Okta Press Release
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** Adobe, AWS, Okta, Salesforce, Google, Anthropic
- **要約:** AdobeがCX Enterprise CoworkerとAdobe Marketing Agentを主要AIプラットフォーム（AWS含む）で提供開始。ClaudeがEnterprise-Managed Auth for MCP追加・管理者のコネクタ一元認可実現。OktaがCross App Access (XAA)生態系をAIエージェントto-appガバナンス向けに拡張。Salesforce+Google Cloud cross-platform統合継続。
- **キーファクト:**
  - Adobe: CX Enterprise Coworker + Marketing Agent (AWS含む主要プラットフォーム)
  - Claude: Enterprise-Managed Auth for MCP追加（管理者一元認可）
  - Okta: Cross App Access (XAA)生態系拡張（AIエージェントto-app governance）
  - Salesforce + Google Cloud: cross-platform AIエージェント統合（4月22日Google Cloud Next）
  - Zenity: AIエージェントセキュリティのエンタープライズガバナンス（6月17日）
- **引用URL:** https://news.adobe.com/news/2026/06/adobe-accelerates-agentic-ai-adoption
- **Evidence ID:** EVD-20260629-0022

### INFO-023
- **タイトル:** Gemini Robotics-ER + Gemini Robotics 1.5 multimodal robotics advancement
- **ソース:** Google DeepMind / Google Cloud docs
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** Gemini Robotics-ER（Embodied Reasoning）思考モデルでロボットの環境理解・相互作用能力を強化。Gemini Robotics 1.5が次世代ロボティクスモデルとして実世界の複雑さ対応。Reachyロボットでのラップバトル（Gemini+音声合成+multi-agent orchestration）等のデモ。
- **キーファクト:**
  - Gemini Robotics-ER: Embodied Reasoning思考モデル
  - Gemini Robotics 1.5: 実世界複雑さ対応次世代モデル
  - DeepMind 3ヶ月プログラムでAIスタック+Roboticsモデルアクセス提供
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Evidence ID:** EVD-20260629-0023

### INFO-024
- **タイトル:** Microsoft ~20M AI agents; multimodal model family (reasoning/code/voice)
- **ソース:** Instagram (業界報道)
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-002-02
- **関連企業:** Microsoft
- **要約:** Microsoftで約2000万AIエージェントが稼働中と報道。インハウスマルチモーダルモデルファミリー（推論/コード/音声/その他）を展開。エージェントが「assistするだけでなくworkする」新段階。
- **キーファクト:**
  - Microsoft: 約2000万AIエージェント稼働
  - インハウスマルチモーダルモデル（推論/コード/音声等）
  - エージェントが「assistでなくwork」段階
- **引用URL:** https://www.instagram.com/reel/DaG0kEzSkBW/
- **Evidence ID:** EVD-20260629-0024

### INFO-025
- **タイトル:** Computer Use vs Browser Agents architecture split; OpenAI SandboxAgent
- **ソース:** AIMultiple / Promptfoo / Vercel / Railway
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** OpenAI, Anthropic, Google, Vercel, Railway
- **要約:** AIがソフトウェアを制御する2つのアーキテクチャ（Computer Use Agents=デスクトップ全体、Browser Agents=ブラウザ内）の分化が進行。Vercel agent-browser CLI・Railwayのエージェント用サンドボックス（filesystem+shell）等のインフラ整備。OpenAI SandboxAgentは明示的capability list（shell()+skills）推奨。
- **キーファクト:**
  - Computer Use Agents（デスクトップ全体）vs Browser Agents（ブラウザ内）の2アーキテクチャ分化
  - Vercel agent-browser CLI・Railwayエージェント用サンドボックス
  - OpenAI SandboxAgent: shell()+skillsの明示capability list推奨
  - Web Voyager benchmark等の評価指標整備
- **引用URL:** https://aimultiple.com/computer-use-agents
- **Evidence ID:** EVD-20260629-0025

### INFO-026
- **タイトル:** AWS Bedrock AgentCore: Web Search, Managed KB, payments, WAF monetization (June 25)
- **ソース:** AWS Insider / AWS News Blog
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** Amazon / AWS
- **要約:** AWSがAmazon Bedrock AgentCoreに3つの新レイヤー追加: Managed Knowledge Base・Web Search on AgentCore・AgentCore payments・AWS WAF AIトラフィック収益化。Bedrock AgentsはNovaモデル自動構成・multi-agent collaboration・memory・KB統合。Strands Agents framework（OSS）でAWS Health Analytics等を構築。
- **キーファクト:**
  - Bedrock AgentCore新機能3層: Managed Knowledge Base・Web Search・payments・WAF AI monetization
  - Bedrock Agents: Novaモデル自動構成・multi-agent collaboration
  - Strands Agents framework (OSS)・AWS Health Analytics活用事例
  - n8n等の3Pワークフロー統合
- **引用URL:** https://awsinsider.net/articles/2026/06/25/amazon-bedrock-agentcore-adds-three-new-layers-of-agent-knowledge.aspx
- **Evidence ID:** EVD-20260629-0026

### INFO-027
- **タイトル:** Microsoft Foundry + unified Agent Framework (AutoGen+Semantic Kernel)
- **ソース:** LinkedIn / Developers Digest
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** Microsoft
- **要約:** MicrosoftがAzure AI FoundryをMicrosoft Foundryに改名・統合。Foundry Agent Serviceをエンタープライズ ready基盤に。AutoGenとSemantic Kernelの統合ランタイム提供（graph-based composition・type safety）。AIライブラリをUnified Agent Frameworkに集約。ホステッドエージェントとAzure Durable Functions連携。
- **キーファクト:**
  - Azure AI Foundry → Microsoft Foundry改名・統合
  - Foundry Agent Service（エンタープライズ ready）
  - AutoGen + Semantic Kernelの統合ランタイム
  - graph-based composition・type safety
  - AIライブラリをUnified Agent Frameworkに集約
- **引用URL:** https://www.developersdigest.tech/blog/microsoft-agent-framework-developer-guide-2026
- **Evidence ID:** EVD-20260629-0027

### INFO-028
- **タイトル:** Gartner: 40% enterprise apps with AI agents by end 2026; 40% projects canceled by 2027
- **ソース:** First Page Sage / DataRobot / FwdSlash / Grand View Research
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** 業界全体
- **要約:** Gartner予測: 2026年末にエンタープライズアプリの40%がAIエージェント内蔵（2025年<5%から急増）。同時に40%のアジェンティックAIプロジェクトが2027年末までにキャンセル予測。DataRobot調査: 71%が「AIエージェント稼働は困難」回答。McKinsey: 62%が実験中、23%のみスケール。市場規模: $10.9B(2026)→$182.9B(2033)予測。
- **キーファクト:**
  - Gartner: エンタープライズアプリ40%がAIエージェント内蔵（2026年末・2025年<5%から急増）
  - Gartner: アジェンティックAIプロジェクト40%が2027年末までにキャンセル
  - DataRobot 2026 survey: 71%が「稼働困難」
  - McKinsey: 62%実験中・23%のみスケール
  - Grand View Research: 市場$10.9B(2026)→$182.9B(2033)
- **引用URL:** https://firstpagesage.com/reports/agentic-ai-adoption-statistics/
- **Evidence ID:** EVD-20260629-0028

### INFO-029
- **タイトル:** Vendor lock-in debate: Multi-vendor strategy cuts costs 40-60% vs single-vendor advantage
- **ソース:** Coder Legion / CIO / Computerworld
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** 業界全体
- **要約:** AIベンダーロックイン議論の2極化: マルチベンダー戦略で40-60%コスト削減可能（Coder Legion）vs 推論スケールでロックインが「アドバンテージ」になる（CIO/Vikrant Kaulgud）。Computerworldは「無料AIトークン提供」の罠を警告。AI調達エージェントのスイッチングコストは従来より1桁低い見方も。
- **キーファクト:**
  - マルチベンダー戦略: コスト40-60%削減可能
  - CIO: ロックインがAI推論スケールで「アドバンテージ」になる逆説
  - 無料AIトークン提供はロックイン罠
  - AI調達エージェントのスイッチングコストは従来より1桁低い見方
- **引用URL:** https://coderlegion.com/21492/the-vendor-lock-in-problem-that-cost-you-a-fortune
- **Evidence ID:** EVD-20260629-0029

### INFO-030
- **タイトル:** EU AI Act Article 50 transparency rules effective Aug 2, 2026
- **ソース:** BlackFog / Collibra / European Commission
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, SCN-005
- **関連企業:** 業界全体
- **要約:** EU AI Act Article 50透明性ルールが2026年8月2日に発効。AI生成コンテンツ・deepfake・AI対話の明示ラベリング義務化。受容不可AI慣行の禁止も同日発効。EU出力を使用するAIは全て対象（地理的基準・用途基準でなく）。アイルランドNiamh Smyth法案提出・EU指令実装。立法調整継続。
- **キーファクト:**
  - EU AI Act Article 50透明性ルール: 2026年8月2日発効
  - AI生成コンテンツ・deepfake・AI対話の明示ラベリング義務化
  - 受容不可AI慣行の禁止: 同日発効
  - 適用範囲: AI出力がEU内で使用される全ケース（地理的基準）
- **引用URL:** https://www.blackfog.com/eu-ai-act-compliance-requirements-2026-and-beyond/
- **Evidence ID:** EVD-20260629-0030

### INFO-031
- **タイトル:** Trump EOs 14409 (AI innovation) June 2 + 14412 (crypto attacks) June 22, 2026
- **ソース:** White House / EDUCAUSE / Brookings
- **公開日:** 2026-06-22
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, H-GOV-001
- **関連企業:** 業界全体
- **要約:** トランプ大統領が6月2日に大統領令14409「高度AI革新・安全保障推進」、6月22日に14412「高度暗号攻撃からの国家保全」に署名。世界的AI支出は2026年$2.5T（前年比44%増）。GPT-5.6リリース時のサイバーEO枠組み構築と連動。EO 14179の直接的後継措置。
- **キーファクト:**
  - EO 14409「高度AI革新・安全保障推進」6月2日署名
  - EO 14412「高度暗号攻撃からの国家保全」6月22日署名
  - 世界的AI支出: $2.5T (2026)・44% YoY増
  - GPT-5.6リリースプロセスのサイバーEO枠組みと連動
  - EO 14179後継の直接的措置
- **引用URL:** https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-secures-the-nation-against-advanced-cryptographic-attacks/
- **Evidence ID:** EVD-20260629-0031

### INFO-032
- **タイトル:** China GB 45438-2025 mandatory AI content labeling standard (Sept 1, 2025)
- **ソース:** Instagram / Atlantic Council
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, SCN-005
- **関連企業:** ByteDance他中国AI企業
- **要約:** 中国初のAIエージェント規制が稼働。2025年9月1日から国家強制標準GB 45438-2025でAI生成コンテンツの明示・暗黙ラベリング義務化。非準拠は法的制裁。EUのAI Act第50条と共通の透明性原則だが実装メカニズムが異なる。クロスボーダーデータガバナンスは別レイヤー。
- **キーファクト:**
  - 中国国家強制標準GB 45438-2025: AIコンテンツラベリング義務化
  - 発効: 2025年9月1日
  - 明示ラベル+暗黙ラベルの二重義務
  - 非準拠は法的制裁
- **引用URL:** https://www.instagram.com/p/DZ-A9sgAPnq/
- **Evidence ID:** EVD-20260629-0032

### INFO-033
- **タイトル:** Pentagon AI contracts: $200M to each of Anthropic/OpenAI/Google/xAI (July 2025)
- **ソース:** Facebook (Vibecodinglife / Claude Community)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, H-GOV-001, H-GOV-002
- **関連企業:** Anthropic, OpenAI, Google, xAI, Casepoint, Palantir
- **要約:** Pentagon AI局が2025年7月にフロンティアAI4社（Anthropic/OpenAI/Google/xAI）に各$200M契約を配布。Casepoint AI製品ブランケット購入契約$98.8M（6月24日・分類法務用）。Palantir Maven Smart System継続稼働。AnthropicとOpenAIが共に「同じ壁」に直面し、SCR指定等の差異発生。
- **キーファクト:**
  - Pentagon 2025年7月: フロンティアAI4社に各$200M契約配布
  - Casepoint: $98.8Mブランケット購入契約（6月24日・分類法務用）
  - Palantir Maven Smart System継続稼働（Iran攻撃で1,000+標的）
  - Anthropic/OpenAIの「同じ壁」直面・SCR指定等の差異
- **引用URL:** https://defensescoop.com/2026/06/24/pentagon-casepoint-ai-products-enhance-classified-legal-ops/
- **Evidence ID:** EVD-20260629-0033

### INFO-034
- **タイトル:** ICRC renews call for autonomous weapons treaty; AI cannot replace human responsibility
- **ソース:** ICRC (International Committee of Red Cross) / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** 業界全体
- **要約:** ICRCが自律型兵器の新条約を改めて要求。「AIは軍事意思決定を支援できるが人間の責任を代替できない」。法的責任は機械でなく人間にある原則を非交渉可能と強調。Ross Coffman将軍は「AIはキルチェーンを加速する目的」発言（論争）。Grok 2,000標的事例との対比で条約要求が急増。
- **キーファクト:**
  - ICRC: 自律型兵器新条約要求を再強調
  - 「AIは軍事意思決定を支援できるが人間責任を代替できない」
  - 法的責任は人間にある原則（非交渉可能）
  - Ross Coffman将軍「AIはキルチェーン加速目的」発言（論争喚起）
- **引用URL:** https://www.linkedin.com/posts/icrc_as-ai-becomes-increasingly-integrated-into-activity-7475563676729540608-nYBc
- **Evidence ID:** EVD-20260629-0034

### INFO-035
- **タイトル:** Hegseth labeled Anthropic "supply-chain risk"; Anthropic v. DoW First Amendment claim
- **ソース:** Quartz / SSRN (Grossi amicus brief)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, H-GOV-001, H-GOV-002
- **関連企業:** Anthropic
- **要約:** Pete Hegseth国防長官がAnthropicを「サプライチェーンリスク」指定（監視利用制限の争議後）。AIスタートアップがAnthropicのFable 5/Mythos 5アクセス無効化後、米政府を提訴。Grossi教授のアミカス・ブリーフが「修正第1条報復・見解差別」に該当すると主張。「反復可能パターン」と指摘。Quartzは「Anthropicの勝利宣言」と報じる（商業的爆発との対比）。
- **キーファクト:**
  - Hegseth国防長官がAnthropicを「サプライチェーンリスク」指定
  - 監視AI利用制限の争議が指定の直接要因
  - AIスタートアップがFable 5/Mythos 5無効化で米政府提訴
  - Grossi教授アミカス: 修正第1条報復・見解差別・反復可能パターン主張
  - Anthropic v. Department of War 法廷闘争本格化
- **引用URL:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6962668
- **Evidence ID:** EVD-20260629-0035

### INFO-036
- **タイトル:** Tech layoffs: Oracle 21K cut (13%), Elastic 281 cut (7%), 39% execs reduce headcount for AI
- **ソース:** HeroHunt / Hoodline / SEC filings
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01, H-CAR-002
- **関連企業:** Oracle, Elastic, 多数
- **要約:** Oracle年次SEC提出でFY2026に21,000人削減（13%・162Kから減少）・AI採用を明示的要因。Elasticは281人削減（7%）・AI再編。39%の経営者がAI能力見込みで頭数削減。2026年3月レイオフの約4分の1がAI関連。Klarna/Duolingo事例に加え大企業でのAI関連人員削減が本格化。
- **キーファクト:**
  - Oracle FY2026: 21,000人削減（13%）・AI明示的要因・162Kから減少
  - Elastic: 281人削減（7%）・AI再編
  - 39%経営者がAI能力見込みで頭数削減
  - 2026年3月レイオフの約1/4がAI関連
- **引用URL:** https://www.herohunt.ai/blog/tech-layoffs-and-ai-the-2026-reality-check/
- **Evidence ID:** EVD-20260629-0036

### INFO-037
- **タイトル:** AI agents = 88% of organic search activity; 2-10x productivity with workflow redesign
- **ソース:** LinkedIn / Harvard Data Science Review / McKinsey
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-02
- **関連企業:** 業界全体
- **要約:** AIエージェントが有機検索活動の88%を占め、2026年末には人間検索を超越予測。Harvard Data Science Review分析でワークフロー再設計時2-10x生産性向上。McKinsey: マーケティングAI 15-20%効率向上・10-20%売上増。但しLenovo研究で70%のエンタープライズAIは「制御不能」でリスク・コスト・ROI遅延の隠れ問題。
- **キーファクト:**
  - AIエージェント: 有機検索活動の88%・2026年末人間超越予測
  - Harvard Data Science Review: ワークフロー再設計で2-10x生産性
  - McKinsey: マーケティング15-20%効率向上・10-20%売上増
  - Lenovo: エンタープライズAIの70%は「制御不能」・リスク・ROI遅延
- **引用URL:** https://www.linkedin.com/posts/joe-lim-11a2a523b_since-february-marketing-tech-has-accelerated-activity-7475685460221198336-kkop
- **Evidence ID:** EVD-20260629-0037

### INFO-038
- **タイトル:** McKinsey: >50% media spend direct buying; Meta/Google AI disintermediation of agencies
- **ソース:** McKinsey / LinkedIn / Yahoo Finance
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Google, Coca-Cola, 広告代理店
- **要約:** McKinsey報告: メディア支出の過半数がダイレクトバイイングチャネル経由。GoogleとMetaがキャンペーンフォーマット全体をAI駆動（バジェット・ターゲティング・配信）。Coca-ColaがGoogle Geminiとのコクリエーションキャンペーン。伝統的代理店・adtech中間業者が「disintermediation圧力」直面。Metaは「Polymarket/Kalshiを破壊する潜在」も。
- **キーファクト:**
  - McKinsey: メディア支出過半数がダイレクトバイイング経由
  - Google/Metaがキャンペーン全体AI駆動
  - Coca-Cola: Google Gemini co-creationキャンペーン
  - 伝統的代理店・adtech中間業者のdisintermediation圧力
  - Metaは予測市場等の別業界への拡張潜力
- **引用URL:** https://www.facebook.com/McKinsey/posts/more-than-half-of-media-spend-already-flows-through-direct-buying-channels-and-w/1541891344073550/
- **Evidence ID:** EVD-20260629-0038

### INFO-039
- **タイトル:** SaaS era ending: HappyFox $1M expansion on $20 AI spend; MoEngage acquires Aampe
- **ソース:** SaaStr / Inc42 / BetterCloud
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** HappyFox, MoEngage, Aampe, NetSuite
- **要約:** SaaSからアジェンティックAIへの移行加速。HappyFox（SaaStr AI 2026）: $20のAIエージェント支出で$1M拡張収益をクローズ。MoEngageがAampe（週200B意思決定処理）を買収。NetSuite創業者Evan Goldberg「AIエージェントが仕事の大部分を担う」。伝統的SaaS収益モデルが圧力。BetterCloud: SaaS→AIネイティブ進化継続。
- **キーファクト:**
  - HappyFox: $20 AIエージェント支出→$1M拡張収益（ROI 50,000x）
  - MoEngage: Aampe買収（週200B意思決定処理）
  - NetSuite創業者: 「AIエージェントが仕事の大部分を担う」
  - SaaS→アジェンティックAI収益モデル転換加速
- **引用URL:** https://www.saastr.com/how-happyfox-closed-1m-in-expansion-on-a-20-ai-agent-spend-with-ceo-shalin-jain/
- **Evidence ID:** EVD-20260629-0039

### INFO-040
- **タイトル:** GPT-4-level cost $30/M (2023)→<$1/M (2026): 30x+ cost collapse
- **ソース:** LLM Stats / APIpulse / BenchLM
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** 業界全体
- **要約:** GPT-4レベル性能のコストが2023年$30/Mから2026年<$1/Mに低下（30倍以上の削減）。42モデル10プロバイダー比較。Anthropic: Haiku 4.5 $1/1M〜Fable 5/Mythos 5 $10/1M。Anthropic 2026年4月4日にPro/Maxブロックで使用量ベース課金移行。ハイブリッド価格モデルが主流。トークン課金=開発者向け、シート=エンタープライズ。
- **キーファクト:**
  - GPT-4レベル: 2023年$30/M → 2026年<$1/M（30x+削減）
  - Anthropic: Haiku 4.5 $1/1M〜Fable 5/Mythos 5 $10/1M
  - Anthropic 2026年4月4日: Pro/Maxブロック・使用量ベース課金移行
  - ハイブリッド価格モデル主流・トークン vs シート使い分け
- **引用URL:** https://llm-stats.com/ai-trends
- **Evidence ID:** EVD-20260629-0040

### INFO-041
- **タイトル:** MMLU全社>90%・GPQA Diamond GPT-5.4 94.4% vs Gemini 3.1 Pro 94.3%（実質同点）
- **ソース:** TeamAI / TechJackSolutions
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** 2026年初頭で全フロンティアモデルがMMLU 90%超、GSM8K ~99%でベンチマーク飽和。GPQA DiamondはGPT-5.4 94.4%とGemini 3.1 Pro 94.3%が実質同点。新論文: 84モデル×133ベンチマーク行列が実質rank-2（2数値で90%予測可能）= ベンチマークの独立性に構造的疑義。
- **キーファクト:**
  - MMLU: 全フロンティアモデル90%超（飽和）
  - GSM8K: ~99%（飽和）
  - GPQA Diamond: GPT-5.4 94.4% vs Gemini 3.1 Pro 94.3%（実質同点）
  - 84モデル×133ベンチマーク行列がrank-2（構造的独立性疑義）
- **引用URL:** https://teamai.com/blog/large-language-models-llms/best-ai-models-for-complex-reasoning-2026/
- **Evidence ID:** EVD-20260629-0041

### INFO-042
- **タイトル:** Artificial Analysis leaderboard: Claude Mythos 5 #1 (95.5%), Fable 5 #2, Opus 4.8 #3
- **ソース:** OpenLM Chatbot Arena / GitHub awesome-llm-bench
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic, OpenAI, DeepSeek
- **要約:** Artificial Analysis Leaderboard 6月22-25日時点: Claude Mythos 5が95.5%で首位、Claude Fable 5 #2、Claude Opus 4.8 #3とAnthropicが上位独占。DeepSeek V4 FlashはIntelligence 29・$0.06/1M tokens・Speed 106で圧倒的コストパフォーマンス。Anthropic 3モデルがトップ3を独占する構造継続。
- **キーファクト:**
  - Claude Mythos 5: 95.5%（首位）
  - Claude Fable 5: #2
  - Claude Opus 4.8: #3（Anthropic上位3独占）
  - DeepSeek V4 Flash: Intelligence 29・$0.06/1M tokens・Speed 106
- **引用URL:** https://openlm.ai/chatbot-arena/
- **Evidence ID:** EVD-20260629-0042

### INFO-043
- **タイトル:** OpenAI Series H $65B at $965B (May 28); IPO 2027 preferred at $1T target
- **ソース:** Financial Times / NYT / CNBC
- **公開日:** 2026-06-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIが5月28日にSeries H $65B調達（$965B評価）をAltimeter/Dragoneer/Greenoaks主導で完了。IPOは2027年まで見送り方向（$1T評価目標 or 即時下げめ）。Anthropicは$30B調達で$900B評価（OpenAI超過）。OpenAI $25Bランレート・2025年$13.1B収益。CNBC報道: ユーザー効率志向シフトで新AI支出現実。
- **キーファクト:**
  - OpenAI Series H: $65B調達・$965B評価（5月28日）
  - IPO: 2027年まで見送り方向・$1T評価目標
  - Anthropic: $30B調達・$900B評価（OpenAI超過）
  - OpenAI: $25Bランレート・2025年$13.1B収益
- **引用URL:** https://www.facebook.com/financialtimes/posts/competition-intensifies-for-anthropic-and-openai-ahead-of-ipos/1423059376534102/
- **Evidence ID:** EVD-20260629-0043

### INFO-044
- **タイトル:** 2026 hyperscaler capex $602B-$700B; JPMorgan $5.5T AI capex "profitable for now"
- **ソース:** Intellectia / William Blair / Fortune (JPMorgan)
- **公開日:** 2026-06-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** AWS, Microsoft, Google, Meta, Oracle
- **要約:** 2026年主要ハイパースケーラー5社資本支出: Intellectia $602B・William Blair ~$700B・Big Tech $650B（60-74%増）。JPMorgan: AI capex爆発は$5.5T規模・現時点では収益性あり。2026年にUS ハイパースケーラー債券発行$150B + 海外$100B + 追加融資$170B。データセンター新容量は2030年までに117GW到達予測。
- **キーファクト:**
  - 2026 hyperscaler capex: $602B〜$700B（5社合算）
  - Big Tech $650B（前年比60-74%増）
  - JPMorgan: $5.5T AI capex爆発・現時点では収益性あり
  - 2026年ハイパースケーラー債券: $150B(US)+$100B(海外)+$170B(追加融資)
  - データセンター新容量: 2030年までに117GW予測
- **引用URL:** https://intellectia.ai/blog/ai-infrastructure-investment-2026
- **Evidence ID:** EVD-20260629-0044

### INFO-045
- **タイトル:** M&A wave: SpaceX acquires Cursor (Anysphere) $60B; Qualcomm Modular $4B; ON Semi Synaptics $7B
- **ソース:** Reuters / CNBC / Axios / Facebook
- **公開日:** 2026-06-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** SpaceX, Anysphere (Cursor), Qualcomm, Modular, ON Semi, Synaptics, MoEngage, Aampe
- **要約:** 主要M&Aラッシュ: SpaceXが6月16日にAnysphere（Cursor親会社）を$60Bで完全買収。QualcommがModularを$4Bで買収（AIソフト）。ON SemiがSynapticsを$7Bで買収（フィジカルAI）。MoEngageがAampeを買収（AIエージェント）。AI産業の統合加速。
- **キーファクト:**
  - SpaceX: Anysphere（Cursor）$60B完全買収（6月16日）
  - Qualcomm: Modular $4B買収（6月24日・AIソフト）
  - ON Semi: Synaptics $7B買収（フィジカルAI・過去最大）
  - MoEngage: Aampe買収（AIエージェント）
- **引用URL:** https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/
- **Evidence ID:** EVD-20260629-0045

### INFO-046
- **タイトル:** Open source LLMs (Llama/Mistral/Qwen/DeepSeek/Gemma) narrow commercial gap
- **ソース:** SocialPrachar / LLM Stats
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, Mistral, Alibaba (Qwen), DeepSeek, Google (Gemma)
- **要約:** OSS LLM（Llama/Mistral/Qwen/DeepSeek/Gemma）がプライバシー・カスタマイズ・商用利用柔性で優位。DeepSeek V4 FlashはIntelligence 29・$0.06/1M tokens・Speed 106で圧倒的コストパフォーマンス維持。OSS フロンティアクラスモデルと商用モデルの性能ギャップは継続縮小。
- **キーファクト:**
  - 主要OSS LLM: Llama/Mistral/Qwen/DeepSeek/Gemma
  - DeepSeek V4 Flash: $0.06/1M tokens（コスト優位）
  - OSSは商用モデルとプライバシー・カスタマイズ性で差別化
- **引用URL:** https://socialprachar.com/blog/discover-the-best-open-source-llms-in-2026
- **Evidence ID:** EVD-20260629-0046

### INFO-047
- **タイトル:** NexGen Manufacturing $315K to migrate 40 AI workflows; vendor-change cost quantified
- **ソース:** LinkedIn (Sverdlek Veix)
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** Builder.ai, NexGen
- **要約:** NexGen ManufacturingがBuilder.ai倒産後に40のAIワークフローを新プラットフォームへ移行するのに$315K費やした（CTOが「過大」と後述）。AIベンダー変更の具体的スイッチングコスト定量事例。AIベンダー overnightでの所有権変更リスク。APIベースモデルから始めた組織が拡大と共に月額請求増大に直面。
- **キーファクト:**
  - NexGen Manufacturing: $315Kで40 AIワークフロー移行
  - Builder.ai倒産が契機・CTOは「過大コスト」評価
  - AIベンダーovernight変更リスク
  - APIベースモデル→拡大で月額急増パターン
- **引用URL:** https://www.linkedin.com/pulse/your-ai-vendor-can-change-hands-overnight-most-have-plan-sverdlik-veixf
- **Evidence ID:** EVD-20260629-0047

### INFO-048
- **タイトル:** Big Four graduate hiring slashed (KPMG down); KPMG Q1 2026: 63% require human AI validation
- **ソース:** Entrepreneur / Instagram / Thomson Reuters
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, H-CAR-002
- **関連企業:** Deloitte, EY, KPMG, PwC, Thomson Reuters
- **要約:** Big Four（Deloitte/EY/KPMG/PwC）が過去2年で新卒採用を大幅削減。KPMG Q1 2026調査: 63%の組織がAI出力の人間検証を義務化（1年前22%から急増）。Thomson Reuters Future of Professionals 2026: AI戦略ある専門家の仅か35%が日常業務への影響を回答。一部企業で方針転換（人間検証強化）とエントリーレベル雇用縮小が同時進行。
- **キーファクト:**
  - Big Four: 過去2年で新卒採用大幅削減・KPMG含む
  - KPMG Q1 2026: 63%組織がAI出力人間検証義務化（1年前22%から急増）
  - Thomson Reuters: AI戦略ある専門家の35%のみ日常業務影響
- **引用URL:** https://www.facebook.com/Entrepreneur/posts/colleges-are-restricting-ai-use-to-protect-academic-integrity-employers-are-raci/1391011236230418/
- **Evidence ID:** EVD-20260629-0048

### INFO-049
- **タイトル:** GitHub Copilot 29% / Cursor 18% / Claude Code 18% workplace adoption (JetBrains Jan 2026)
- **ソース:** Uvik Software / JetBrains
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** GitHub Copilot, Cursor, Anthropic (Claude Code), Continue
- **要約:** JetBrains Jan 2026データ: GitHub Copilot 29%職場採用・26M+総ユーザー。CursorとClaude Codeは18%で同率。CursorがContinue（OSS、34K GitHub stars）を静かに買収（acqui-hire）。Nvidia CEO Jensen Huangのお気に入りはCursor・Nvidia全エンジニア使用。GitHub Copilot使用量ベース課金が6月1日に全面稼働。
- **キーファクト:**
  - GitHub Copilot: 29%職場採用・26M+ユーザー
  - Cursor: 18%（Claude Codeと同率）
  - Claude Code: 18%
  - Cursor: Continue買収（OSS・34K stars・acqui-hire）
  - Nvidia全エンジニアがCursor使用（Jensen Huang CEO）
  - GitHub Copilot使用量課金: 6月1日全面稼働
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/
- **Evidence ID:** EVD-20260629-0049

### INFO-050
- **タイトル:** Stanford HAI 2026 AI Index: 20% decline in 22-25 software dev employment
- **ソース:** Stanford Institute for Human-Centered AI / LinkedIn / TechCrunch
- **公開日:** 2026-06-24
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02, H-CAR-002
- **関連企業:** 業界全体
- **要約:** Stanford HAI 2026 AI Index Report: 22-25歳ソフトウェア開発者の雇用が約20%減少。Stanford Digital Economy Labが同様に追跡。TechCrunch: SignalFireデータで全体としてエンジニアは新規採用のより大きい割合を占める（中堅以上のレジリエンス）。欧州のジュニアテック採用は2025年に3%縮小。AIがバグ修正・ボイラープレート・テストスイート等のエントリーレベル業務を吸収。
- **キーファクト:**
  - Stanford HAI 2026 AI Index: 22-25歳ソフト開発者雇用約20%減少
  - Stanford Digital Economy Lab: ~20% employment decline追跡
  - SignalFire (TechCrunch): エンジニアは新規採用のより大きい割合
  - 欧州ジュニアテック採用2025年に3%縮小
  - AIがエントリーレベル業務（バグ修正・ボイラープレート・テスト）を吸収
- **引用URL:** https://www.linkedin.com/posts/madhvesh-chokshi_juniordeveloper-stanfordai-aicoding-activity-7474797097213558784-2Nuw
- **Evidence ID:** EVD-20260629-0050

### INFO-051
- **タイトル:** WEF report: AI transforming 86% of organizations; entry-level work redesign agenda
- **ソース:** World Economic Forum / PwC
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03, H-CAR-002
- **関連企業:** 業界全体
- **要約:** WEF Future of Jobs 2025: AIと情報処理技術が組織の86%を変革予測。WEF最新「AIとエントリーレベルワークの未来」レポート（PwC共同）を公開。AIは単なる置換でなく人間作業の移行。83百万の仕事が自動化リスク（新規仕事で相殺）。Andrej Karpathyが全米仕事をAI暴露度でマップするツール公開。
- **キーファクト:**
  - WEF Future of Jobs: 組織の86%をAIが変革予測
  - WEF/PwC: 「AIとエントリーレベルワークの未来」レポート公開
  - 83百万仕事が自動化リスク
  - Karpathy: 全米仕事AI暴露度マップツール公開
- **引用URL:** https://reports.weforum.org/docs/WEF_Artificial_Intelligence_and_the_Future_of_Entry_Level_Work_2026.pdf
- **Evidence ID:** EVD-20260629-0051

### INFO-052
- **タイトル:** Microsoft Nadella: every company should build own AI model with proprietary data
- **ソース:** T2Conline / MIT Sloan / Citrix
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** Microsoft
- **要約:** Microsoft Satya Nadella CEOが「全企業は独自データ・プロセス・制度的知識で独自AIモデルを構築すべき」と主張。MIT Sloan研究: 高いデータ流動性がAI活用でビジネス性能を向上。Citrix: 「AIはプロダクトでなくデータがプロダクト」。データ準備性がAI構築の主要障壁・最初の優先課題。
- **キーファクト:**
  - Microsoft Nadella: 全企業独自AIモデル構築推奨
  - MIT Sloan: 高データ流動性がAI性能を向上
  - データ準備性: AI構築の主要障壁・最初の優先課題
  - 「AIはプロダクトでなくデータがプロダクト」(Citrix)
- **引用URL:** https://t2conline.com/microsofts-ceo-says-every-company-should-build-its-own-ai-model-heres-why-that-changes-everything/
- **Evidence ID:** EVD-20260629-0052

### INFO-053
- **タイトル:** ARC-AGI saturation question: Qwen3 96% on ARC-AGI-1; frontier still far from general
- **ソース:** arXiv (DiARC paper) / TechJackSolutions / HuggingFace
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** Alibaba (Qwen), Anthropic, Google DeepMind, OpenAI, xAI
- **要約:** DiARC論文: Qwen3がARC-AGI-1・MiniARC・ConceptARCで96%超の精度達成（ARC特化モデル・Closed-source強モデルを上回る）。4フロンティアラボ（Anthropic/Google DeepMind/OpenAI/xAI）が2025年公開モデルカードでARC-AGI性能報告・標準化定着。しかしARC-AGI-2では「フロンティア≠汎用」の批判的見方が活発化。
- **キーファクト:**
  - DiARC+Qwen3: ARC-AGI-1/MiniARC/ConceptARC 96%超
  - 4フロンティアラボが2025年モデルカードでARC-AGI性能報告
  - ARC-AGI-2: 「フロンティア≠汎用」批判的見方活発化
- **引用URL:** https://arxiv.org/html/2606.26530v1
- **Evidence ID:** EVD-20260629-0053

### INFO-054
- **タイトル:** Hassabis AGI ~2030 "new human era"; Amodei AGI 2026-2027 timeline divergence
- **ソース:** Bloomberg / FT / Instagram
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google DeepMind, Anthropic
- **要約:** Demis Hassabis DeepMind CEO: AGIは5-10年以内（Kurzweil ~2030とほぼ一致）・「新ヒト時代」をもたらす。現在のスケール拡大を超える主要ブレークスルー必要と強調。Dario Amodei Anthropic: AGI 2026-2027到達。Hassabis: 10年末までに50%可能性。主要CEO間でAGIタイムライン予測の乖鹿継続。
- **キーファクト:**
  - Hassabis: AGI 5-10年以内（Kurzweil ~2030とほぼ一致）
  - Hassabis: 「新ヒト時代」・スケール超えるブレークスルー必要
  - Amodei: AGI 2026-2027到達予測
  - Hassabis: 10年末までに50%可能性
  - CEO間タイムライン予測の乖鹿継続
- **引用URL:** https://www.facebook.com/bloombergbusiness/posts/deepminds-demis-hassabis-tells-francine-lacqua-ai-may-be-overhyped-in-the-near-t/1433783941941028/
- **Evidence ID:** EVD-20260629-0054

### INFO-055
- **タイトル:** ByteDance Doubao Pro版¥68-500/月 (June 24); Seed 2.1 + Seedance 2.5 (July)
- **ソース:** Reuters (TradingView) / ByteDance Seed blog / X
- **公開日:** 2026-06-24
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-01, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDance豆包が2026年6月24日にPro版を本格提供開始: ¥68-500/月（連続包月）でDoubao 2.1系列搭載。免費心象からの本格マネタイズ移行。Seed 2.1: 汎用Agent能力・コード工程・多模態基礎能力強化。Seedance 2.5: 7月初正式ローンチ予定・単段動画生成30秒・周星馳IPと初提携。
- **キーファクト:**
  - 豆包Pro版: ¥68-500/月（連続包月）6月24日ローンチ
  - Doubao 2.1系列搭載
  - Seed 2.1: 汎用Agent能力・コード工程・多模態強化
  - Seedance 2.5: 7月初正式ローンチ・単段動画30秒・周星馳IP初提携
- **引用URL:** https://es.tradingview.com/news/reuters.com,2026:newsml_L4S42W0AK:0/
- **Evidence ID:** EVD-20260629-0055

### INFO-056
- **タイトル:** Canada $300M AI Compute Access Fund; Horizon Europe funding continues
- **ソース:** Canada ISED / EU Horizon Europe
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** 政府（Canada, EU）
- **要約:** カナダAI Compute Access Fund $300Mで高コストAI計算資源への対抗。Horizon EuropeがEU研究革新資金プログラム継続・MTR後調整。各国がAI主権・計算リソース自給に向けた公的資金強化。NIH 2026 Pilot DMS Plan形式が全競争/非競争賞で必須化。
- **キーファクト:**
  - カナダ AI Compute Access Fund $300M
  - Horizon Europe: EU研究革新資金継続・MTR調整
  - 各国AI主権・計算自給向け公的資金強化
- **引用URL:** https://ised-isde.canada.ca/site/ised/en/canadian-sovereign-ai-compute-strategy/ai-compute-access-fund
- **Evidence ID:** EVD-20260629-0056

### INFO-057
- **タイトル:** RSI by 2028 (Anthropic co-founder); Recursive SOTA on small-model speed + GPU kernels
- **ソース:** Reason Magazine / Import AI / Business Standard
- **公開日:** 2026-06-22
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic, Recursive
- **要約:** Anthropic共同創業者Jared Kaplan: 2028年までにAIが「recursive self improvement」能力を持つ予測。Recursive社は言語モデル訓練・小モデル訓練速度・GPUカーネル最適化で新SOTA達成。AIが自律的に自後継者のコードを設計・テスト・最適化可能に。Business Standard: RSIの具体的説明とAGI到達可能性の中心的議論化。
- **キーファクト:**
  - Anthropic共同創業者: 2028年までにAIのRSI能力予測
  - Recursive社: 言語モデル訓練・小モデル速度・GPUカーネル最適化で新SOTA
  - AIが自律的に自後継者コード設計・テスト・最適化
  - RSI: AGI到達可能性の中心的議論化
- **引用URL:** https://www.business-standard.com/technology/artificial-intelligence/recursive-self-improvement-explained-is-ai-building-ai-the-path-to-agi-126062200661_1.html
- **Evidence ID:** EVD-20260629-0057

### INFO-058
- **タイトル:** Yann LeCun "xAI is a failure" - all 11 co-founders left by March 2026; scaling critique
- **ソース:** Instagram / CNBC reposts
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** xAI, Meta
- **要約:** Yann LeCun Turing Award受賞者がCNBCでxAIを「一種の失敗」と評。2026年3月までにDeepMind/OpenAI/GoogleからxAIを設立した11人のオリジナル共同創業者全員が退社。Musk氏のトップAI人材採用困難指摘。LeCunはLLM単純拡大ではヒト級知能に到達しないと主張（スケーリング批判派）。
- **キーファクト:**
  - LeCun: xAIを「一種の失敗」と評
  - 2026年3月までにオリジナル共同創業者11人全員退社
  - Musk氏のトップAI人材採用困難
  - LeCun: LLM単純拡大ではヒト級知智到達しない（スケーリング批判派）
- **引用URL:** https://www.instagram.com/reel/DaAfPuJNO38/
- **Evidence ID:** EVD-20260629-0058

### INFO-059
- **タイトル:** AOC+Sanders AI Data Center Moratorium Act; Pallone joins federal push
- **ソース:** Data Center Dynamics / Ocasio-Cortez press / MyCentralJersey
- **公開日:** 2026-06-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** 業界全体
- **要約:** AOC下院議員とBernie Sanders上院議員が「AI Data Center Moratorium Act」を提出。データセンター建設の一時停止を求め、環境・経済・安全問題への議会対応あるまで維持。Pallone下院議員（House Energy & Commerceトップ民主党）が連邦押しに合流。データセンター公共投資抑制の連邦レベル動向顕在化。
- **キーファクト:**
  - AOC + Sanders: AI Data Center Moratorium Act提出
  - データセンター建設一時停止求める
  - 環境・経済・安全問題への議会対応あるまで維持
  - Pallone下院議員が連邦押しに合流
- **引用URL:** https://www.datacenterdynamics.com/en/news/ocasio-cortez-and-sanders-introduce-ai-data-center-moratorium-act/
- **Evidence ID:** EVD-20260629-0059

### INFO-060
- **タイトル:** 豆包 DAU 2億超 / MAU 3.45億 (2026年3月); Pro版¥68-500/月でマネタイズ
- **ソース:** 鈦媒体 / Moomoo / 網易 / 腾訊網
- **公開日:** 2026-06-24
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, H-ANT-002
- **関連企業:** ByteDance
- **要約:** ByteDance豆包の日活（DAU）2億超・月活（MAU）3.45億（2026年3月・QuestMobile）。中国国内AI原生App月活4.4億の最大シェア。字節跳動は年間資本支出¥4000-5000億元計画。豆包股（doubao stock）最新$14.85（2ヶ月前$13.08から値上がり）・初回買戻し実施。分社化噂も。
- **キーファクト:**
  - 豆包 DAU 2億超・MAU 3.45億（2026年3月・QuestMobile）
  - 中国AI原生App月活4.4億中で最大シェア
  - 字節跳動年間資本支出¥4000-5000億元計画
  - 豆包股最新$14.85（2ヶ月前$13.08から値上がり）・初回買戻し実施
  - 分社化の噂も報道
- **引用URL:** https://www.tmtpost.com/8042678.html
- **Evidence ID:** EVD-20260629-0060

### INFO-061
- **タイトル:** AI Scientist published in Nature (Mar 26); Big Tech AI infra $2B/day (2026)
- **ソース:** Nature / Peter Diamandis / The Hatch Agency
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** 業界全体
- **要約:** Nature誌3月26日: 「AI Scientist」が研究ライフサイクル自動化の「可能性の木」を自律探索し科学的ブレークスルーを発見。Big Tech 2026 AI資本支出$650B（2025年$1B/日→2026年$2B/日）。Stanford研究者がVB Transform 2026でアジェンティック「科学者」による創薬革命を議論。2025年12月NASA Perseverance初AI自律マイルストーン。
- **キーファクト:**
  - AI Scientist (Nature 3月26日): 可能性の木自律探索・科学ブレークスルー
  - Big Tech AI資本支出: 2026年$650B（$2B/日・2025年$1B/日から倍増）
  - Stanford VB Transform 2026: アジェンティック科学者による創薬革命議論
  - 2025年12月: NASA Perseverance初AI自律マイルストーン
- **引用URL:** https://www.instagram.com/p/DZ_5KEkkapU/
- **Evidence ID:** EVD-20260629-0061

### INFO-062
- **タイトル:** ByteDance Seedance 2.5 July launch (30s segments, 50 multimodal refs); Seed 2.1 Pro/Turbo
- **ソース:** ByteDance Seed blog / 36kr / Volcengine / AtlasCloud
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04, KIQ-003-01
- **関連企業:** ByteDance
- **要約:** ByteDance Seed 2.1系列（Pro/Turbo）: 汎用Agent能力・コード工程で大幅向上。Seedance 2.5: 7月初正式ローンチ・単段動画30秒・最大50個full-modal参考素材・3D白模サポート。Seedance 2.0 Mini: 2倍速・半分コスト（6月中旬）。AI版権商業化プラットフォーム同時発表。Cozeは消費者/軽量シナリオ向け戦略維持。
- **キーファクト:**
  - Seed 2.1 (Pro/Turbo): 汎用Agent・コード工程大幅向上
  - Seedance 2.5: 7月初正式・単段30秒・最大50個full-modal参考
  - Seedance 2.0 Mini: 2倍速・半分コスト（6月中旬）
  - AI版権商業化プラットフォーム同時発表
  - Coze: 消費者/軽量シナリオ向け戦略維持
- **引用URL:** https://seed.bytedance.com/zh/seed2_1
- **Evidence ID:** EVD-20260629-0062

### INFO-063
- **タイトル:** ByteDance $900B gray market valuation; ¥1560B overseas loan; DeepSeek A轮 ¥51B ($55B val)
- **ソース:** Threads / Instagram / 香港経済日報 / 新浪財経
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance, DeepSeek, Qualcomm
- **要約:** ByteDance灰市場評価額$9000億・AI/データセンターに最大$700億投資。ByteDanceが¥1560億（歴来最大海外融資）+¥2000億ローン調達を模索。Qualcommとのチップ設計提携交渉（カスタム動画処理プロセッサ）。DeepSeek A輪¥510億（6月15日・評価額約¥4000億/$550億）で中国AI創業企業単輪調達記録更新・全部門人員倍増。
- **キーファクト:**
  - ByteDance灰市場評価額: $9000億
  - AI/データセンター投資: 最大$700億
  - 海外融資¥1560億（歴来最大）+ ¥2000億ローン模索
  - Qualcommとのチップ設計提携交渉（カスタム動画プロセッサ）
  - DeepSeek A輪¥510億（6月15日・評価額$550億）・中国AI創業記録
  - DeepSeek全部門人員倍増
- **引用URL:** https://www.threads.com/@whaleagent/post/DaIFvmTExuY
- **Evidence ID:** EVD-20260629-0063

### INFO-064
- **タイトル:** Pentagon testing OpenAI/Google to REPLACE Anthropic Claude (competitive displacement)
- **ソース:** Quartz / Instagram / Medium
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, H-GOV-001, H-GOV-002
- **関連企業:** Anthropic, OpenAI, Google, Pentagon
- **要約:** PentagonがAnthropicのClaudeを分類軍事システム全体で置換するため、OpenAI・GoogleのAIモデルの正式テストを開始。2025年7月Anthropic $200M・2年DoD契約後のアクセス停止（90分以内）で生じた空白を順応企業が埋める構造。Quartz報道: AnthropicはSCR指定後に提訴し、$30B収益を超越する「勝利宣言」。H-GOV-002（順応報酬構造）の初の具体的直接証拠。
- **キーファクト:**
  - Pentagon: Anthropic Claude置換のためOpenAI・Google AIモデル正式テスト
  - 2025年7月Anthropic $200M・2年DoD契約後アクセス停止（90分以内）
  - Quartz: Anthropic「勝利宣言」・SCR指定後に提訴し$30B収益超越
  - 順応企業（OpenAI/Google）が契約を獲得する順応報酬構造の直接証拠
- **引用URL:** https://www.facebook.com/quartznews/posts/icymi-anthropics-victory-lap-after-the-pentagon-labeled-anthropic-a-supply-chain/1372321724763642/
- **Evidence ID:** EVD-20260629-0064

### INFO-065
- **タイトル:** Enterprise autonomous AI marketing agents 14%→34% in 6 months; AI universal cost layer
- **ソース:** Business Insider / Instagram / Tomasz Tunguz
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-002-05, KIQ-004-01
- **関連企業:** 業界全体
- **要約:** エンタープライズでの自律AIマーケティングエージェント実行チームが6ヶ月で14%→34%に跳ね上がり。AIは「設計・調達・運用・QA・物流・マーケティングの全バリューチェーンに適用される普遍コスト削減レイヤー」。大手代理店は間接費削減が追いつかず・2人ショップが台頭。AI推論の再販が最も急成長するAIビジネスモデル。
- **キーファクト:**
  - エンタープライズ自律AIマーケティングエージェント: 6ヶ月で14%→34%
  - AI: 全バリューチェーン適用の普遍コスト削減レイヤー
  - 大手代理店は間接費削減追いつかず・2人ショップ台頭
  - AI推論再販が最急成長ビジネスモデル
- **引用URL:** https://www.instagram.com/reel/DaAhM-6E1Bu/
- **Evidence ID:** EVD-20260629-0065

### INFO-066
- **タイトル:** Meta CapEx projected $66-72B (2025) rising; Ukraine AI defense model for West
- **ソース:** YourStory / Atlantic Council / Journal Record
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04, KIQ-002-03
- **関連企業:** Meta
- **要約:** MetaのCapExは2025年$66-72B予測で更に上昇傾向。AI投資ブーム・インフラ資本集中継続。Atlantic Council: 欧米がウクライナのAI国防未来ビジョンから学ぶべき・次世代防衛技術注目。Oklahoma: トランプ秩序で州AI規制停滞（連邦優先）。New York: GenAI使用強制への憲法的懸念法案。
- **キーファクト:**
  - Meta CapEx: 2025年$66-72B予測・上昇傾向
  - Atlantic Council: 西側がウクライナAI国防モデルから学ぶべき
  - Oklahoma: 連邦優先で州AI規制停滞
  - New York: GenAI使用強制法案・憲法修正第1条懸念
- **引用URL:** https://www.facebook.com/yourstorycom/posts/meta-is-reportedly-in-talks-to-invest-in-or-acquire-fintech-unicorn-cred-at-a-va/1497138289114807/
- **Evidence ID:** EVD-20260629-0066

### INFO-067
- **タイトル:** Anthropic-Pentagon timeline detailed: Jul2025 $200M deal → Feb2026 HITL refusal → Feb27 Trump cease order → Jun12 90-min shutdown
- **ソース:** Medium (The_Architect) / 集約: Politico/NYT/TechCrunch/Foreign Policy
- **公開日:** 2026-06-24
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, H-GOV-001, H-GOV-002, KIQ-005-03
- **関連企業:** Anthropic, Pentagon, OpenAI, Google, xAI, Palantir
- **要約:** Anthropic-Pentagon対立の詳細タイムライン。2025年7月$200M DoD契約・Claudeが分類使用唯一クリア済モデル。2026年1月Palantir経由でベネズエラMaduro捕獲作戦で使用→DoDが「全合法用途・制限ゼロ」要求。2月Anthropic拒否（HITL・大量監視2レッドライン）。2月27日トランプ「全連邦機関Anthropic使用即時停止」投稿。3月Hegseth「サプライチェーンリスク」指定（中国/Huawei级别）・Emil MichaelがDarioを「嘘つき・神コンプレックス」と攻撃。連邦判事が違憲報復として阻止・DOJ控訴。4月控訴裁がAnthropic救済拒否。6月9日Fable 5公開→3日後の6月12日商務省90分輸出管理指令。**GPT-5.5にも同じ脆弱性存在するがOpenAIには無措置**＝選択的執行。OpenAI/Google/xAI/Amazon/Microsoft/Nvidiaは5月までに全社軍事協定署名。数百人のOpenAI/Google従業員がAnthropic支持請願。
- **キーファクト:**
  - 2025年7月: Anthropic $200M 2年DoD契約・Claude分類使用唯一クリア
  - 2026年1月: Palantir経由でMaduro捕獲作戦使用→DoD「全合法用途・制限ゼロ」要求
  - 2026年2月: Anthropic拒否（HITL・大量監視2レッドライン）
  - 2026年2月27日: トランプ「全連邦機関Anthropic使用即時停止」
  - 2026年3月: Hegseth「サプライチェーンリスク」指定（Huawei级别）・Emil Michael「嘘つき・神コンプレックス」Dario攻撃
  - 連邦判事違憲報復阻止→DOJ控訴→4月控訴裁Anthropic救済拒否
  - 6月9日Fable 5公開→6月12日90分商務省指令でFable 5/Mythos 5全世界停止
  - GPT-5.5同脆弱性だがOpenAI無措置＝選択的執行
  - OpenAI/Google/xAI/Amazon/Microsoft/Nvidia全社5月までに軍事協定署名
  - 数百人OpenAI/Google従業員がAnthropic支持請願
  - 6月22日時点: Fable 5/Mythos 5まだオフライン・トランプG7後軟化も指令継続
- **引用URL:** https://levelup.gitconnected.com/the-u-s-government-shut-down-anthropics-best-ai-in-90-minutes-26b31319dbc3
- **Evidence ID:** EVD-20260629-0067

### INFO-068
- **タイトル:** WEF/PwC framework: 4 dimensions for entry-level work redesign (job access/design/pipeline/education)
- **ソース:** World Economic Forum / Randstad (Myriam Beatove Moreale CHRO)
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03, H-CAR-002
- **関連企業:** WEF, PwC, Randstad
- **要約:** WEF/PwC共同「AIとエントリーレベルワークの未来」レポート発表。4次元フレームワーク: ジョブアクセス・ジョブデザイン・タレントパイプライン・教育システム適合。ジョブデザインが主要戦略レバー・役割ベース→能力ベースモデルへの移行推奨。Randstad CHRO: 「the great workforce adaptation」・AIがルーチン業務を担う中、人間は judgement・oversight・human connectionに集中。AIリテラシー加速器プログラム全従業員必修化。
- **キーファクト:**
  - WEF/PwC共同レポート: 4次元フレームワーク（アクセス/デザイン/パイプライン/教育）
  - ジョブデザイン主要戦略レバー・役割ベース→能力ベース移行推奨
  - Randstad: 「the great workforce adaptation」・人間はjudgement/oversight/human connectionに集中
  - AIリテラシー加速器プログラム全従業員必修化
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-is-transforming-entry-level-work-how-can-companies-redesign-jobs-to-keep-opportunity-alive/
- **Evidence ID:** EVD-20260629-0068
