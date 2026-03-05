# 収集データ: 2026-03-05

## メタデータ
- 収集日時: 2026-03-05 00:00 UTC
- 品質フラグ: COLLECTING
- 動的追加クエリ: KIQ-RED-005 (ROI定義), KIQ-ANTHROPIC-MARKET (Claude Codeシェア), KIQ-OPENAI-ALLOCATION ($110B用途), KIQ-JUNIOR-CAUSE (ジュニア採用), KIQ-BYTEDANCE-ENGAGEMENT (DAU/エンゲージメント), KIQ-CODE-QUALITY (AIコード品質)

## 収集結果

### INFO-001
- **タイトル:** Statement from Dario Amodei on our discussions with the Department of War
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-02-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** Dario Amodei CEOが国防総省との対立について声明発表。Anthropicは政府のAI活用に協力してきたが、(1)大量国内監視、(2)完全自律型兵器の2点について安全保障上の懸念から拒否。DoWは「supply chain risk」指定やDefense Production Act発動を脅しとして使用。
- **キーファクト:**
  - Anthropicは米政府の機密ネットワークにClaudeを展開した最初のフロンティアAI企業
  - CCP関連企業へのClaude使用停止で数億ドルの収益を放棄
  - DoWは「any lawful use」を受け入れる企業のみと契約すると表明
  - Anthropicは「supply chain risk」指定（米国敵対国向けラベル、米国企業には前例なし）を脅されている
- **引用URL:** https://www.anthropic.com/news/statement-department-of-war

### INFO-002
- **タイトル:** Anthropic's Responsible Scaling Policy: Version 3.0
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-02-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** RSP（Responsible Scaling Policy）第3版を公開。ASL-3（バイオ兵器リスク）は2025年5月に実装済み。ASL-4/5の実装は単独では困難との認識。政策環境はAI競争力優先にシフトし、安全性議論は連邦レベルで十分な牽引力を得ていない。
- **キーファクト:**
  - RSPは「if-then」条件付きコミットメント方式
  - OpenAI、Google DeepMindも類似フレームワークを採用
  - ASL-3の実装コストは合理的だったが、より高いASLは単独実装困難の可能性
  - Frontier Safety Roadmap、Risk Reports（3-6ヶ月ごと公開）を新設
  - 外部専門家によるRisk Report査読を義務化
- **引用URL:** https://www.anthropic.com/news/responsible-scaling-policy-v3

### INFO-003
- **タイトル:** Claude for Financial Services
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-07-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** 金融分析向け統合ソリューションを発表。Databricks、Snowflake、S&P Global、FactSet等のデータプロバイダーとMCP連携。Bridgewater、NBIM、Commonwealth Bank、AIG等が採用事例。AWS Marketplaceで購入可能、Google Cloud Marketplaceは近日対応予定。
- **キーファクト:**
  - Claude 4はVals AI Finance Agentベンチマークで他フロンティアモデルを上回る
  - NBIM（ノルウェー銀行投資管理）は約20%の生産性向上（213,000時間相当）を達成
  - AIGはアンダーライティング時間を5倍短縮、データ精度75%→90%向上
  - Accenture、Deloitte、KPMG、PwC等が実装パートナー
- **引用URL:** https://www.anthropic.com/news/claude-for-financial-services

### INFO-004
- **タイトル:** AI Agent Architecture: From Bots to Agentic AI Systems
- **ソース:** AutomationEdge
- **公開日:** 2026-02-26
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** N/A (業界分析)
- **要約:** エンタープライズ向けAIエージェントアーキテクチャの解説記事。6層モデル（UI層、API Gateway、オーケストレーション、エージェント、ツール/メモリ、インフラ）を提示。マルチエージェントシステムがエンタープライズスケールに適していると指摘。
- **キーファクト:**
  - シングルエージェント vs マルチエージェント比較: マルチエージェントは高いスケーラビリティと耐障害性
  - 実装ロードマップ: 高影響ワークフローの特定→単一エージェントパイロット→オーケストレーション追加→マルチエージェント拡張
  - エンタープライズユースケース: 自律CS、IT運用、金融照合、コンプライアンス監視
- **引用URL:** https://automationedge.com/blogs/ai-agent-architecture-enterprise-guide/

### INFO-005
- **タイトル:** The AI Security Crisis Nobody Saw Coming (And Why Your DevOps Pipeline Just Became Critical)
- **ソース:** LinkedIn (Ted Elliott)
- **公開日:** 2026-03-04
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-06, KIQ-004-01
- **関連企業:** Anthropic, OpenAI, Block
- **要約:** Claude Code Security発表でサイバーセキュリティ株が暴落（CrowdStrike -8%、Okta -9%）。Blockが40%人員削減（4,000人）をAI生産性向上を理由に発表し株価24%急騰。AnthropicはPentagonの$200M契約を大量監視・完全自律兵器拒否で破棄。
- **キーファクト:**
  - 74%のCIOが直近のAI投資を後悔、2年以内にROI証明が必要
  - 企業は平均30種類のAIモデルを使用（Perplexity調査）
  - Salesforce Agentforce $800M ARR達成も収益目標未達、AIチーム1,000人削減
  - Claude Code SecurityはAI生成コードの脆弱性を検出するツール
- **引用URL:** https://www.linkedin.com/pulse/ai-security-crisis-nobody-saw-coming-why-your-devops-pipeline-ted-jvmte

### INFO-006
- **タイトル:** OpenAI and AWS Just Changed Everything With 'Frontier'
- **ソース:** Liora
- **公開日:** 2026-03-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI, AWS, Microsoft, Anthropic
- **要約:** OpenAIとAWSが2026年2月27日に戦略的提携を発表。AWSがOpenAIの新エンタープライズAIプラットフォーム「Frontier」の独占サードパーティクラウドプロバイダーに。Frontierは組織全体で共有コンテキストを維持するAIエージェント構築・管理プラットフォーム。
- **キーファクト:**
  - AWSはFrontierの唯一のサードパーティ販売業者
  - 価格・SLA・SOC2/HIPAA/FedRAMP認証は未発表
  - Microsoft Azure、Google Cloudとの競争激化
  - Anthropic、Cohere等の既存エンタープライズAIソリューションと競合
- **引用URL:** https://liora.io/en/openai-and-aws-just-changed-everything-with-frontier

### INFO-007
- **タイトル:** Vertex AI consumption options - Google Cloud Documentation
- **ソース:** Google Cloud (公式ドキュメント)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** Vertex AIの5つの消費オプションを詳細解説。Provisioned Throughput（SLA保証）、Standard PayGo（従量課金）、Priority PayGo（優先処理・プレミアム価格）、Flex PayGo（レイテンシ許容・約50%割引）、Batch inference（非同期大量処理）。
- **キーファクト:**
  - 1年Provisioned Throughputは1ヶ月比26%割引
  - Flex PayGoは約50%コスト削減可能
  - Batch処理はStandard PayGoより50%安価
  - Context Cachingでコスト・レイテンシ削減
- **引用URL:** https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deploy/consumption-options

### INFO-008
- **タイトル:** What AI Vendors Can Help us Operationalize AI Agents in our Bank Beyond the POC Phase?
- **ソース:** Neurons Lab
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Microsoft, AWS, Google, Oracle, Accenture
- **要約:** 金融機関がPOCから本番運用に移行するためのAIエージェントベンダー比較。Neurons Lab、Oracle Financial Services、Sphinx、Beam AI等の専門ベンダーと、Microsoft Copilot/Foundry、AWS Bedrock AgentCore、Google Vertex AI等のハイパースケーラーを比較。
- **キーファクト:**
  - BNY（ニューヨーク銀行）がGemini EnterpriseをEliza AIプラットフォームに統合
  - 金融規制（FCA、PRA、EBA、Basel）では説明責任・監査証跡・人間監視が必須
  - Day 2運用（監視、ロールバック、HITL）が最も失敗しやすい領域
  - OpenAIが大手コンサルティング企業との提携を拡大（POC→本番移行支援）
- **引用URL:** https://neurons-lab.com/what-ai-vendors-can-help-us-operationalize-ai-agents-in-our-bank-beyond-the-poc-phase/

### INFO-009
- **タイトル:** MCP Server for Cisco Services?
- **ソース:** Cisco Community
- **公開日:** 2026-02-27
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Cisco, Anthropic
- **要約:** CiscoパートナーがCisco Services向けMCPサーバーのローンチを要望。製品仕様、保証状況、サービス契約詳細、EOL/EOS通知へのAIツールアクセスを可能にする。CiscoコミュニティでThousandEyes/WebexとClaude DesktopのMCP統合記事も公開済み。
- **キーファクト:**
  - MCPはAIエージェントが構造化データにアクセスするためのプロトコル
  - パートナーの生産性向上、エラー削減、AI対応エコシステムでの競争優位性
  - Kali LinuxもClaude AIとのMCP統合を実施（ペネトレーションテスト向け）
- **引用URL:** https://community.cisco.com/t5/services-discussions/mcp-server-for-cisco-services/m-p/5373277

### INFO-010
- **タイトル:** Anthropic appoints Irina Ghose as Managing Director of India
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-01-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Irina GhoseがAnthropic India Managing Directorに就任。Microsoft Indiaでの経験（金融、医療、製造、政府でのエンタープライズAI導入）を活かし、バンガロールオフィス開設を準備。インドはClaude.aiの世界第2位の市場。
- **キーファクト:**
  - IndiaはClaude.aiの世界第2位の市場
  - インドユーザーの約半数がコンピュータ・数学タスクに集中（Economic Index）
  - 政策立案者、学術機関、企業との連携強化
- **引用URL:** https://www.anthropic.com/news/anthropic-appoints-irina-ghose-as-managing-director-of-india

### INFO-011
- **タイトル:** Anthropic expands global leadership in enterprise AI
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-09-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-003-04, KIQ-ANTHROPIC-MARKET
- **関連企業:** Anthropic
- **要約:** AnthropicがエンタープライズAI市場でトップシェアを獲得。Run-rate revenueが$87M（2024年初）から$5B+（2025年8月）に成長。$13B Series F調達（$183B評価）。顧客数は2年で300倍増（1,000未満→300,000以上）。
- **キーファクト:**
  - **エンタープライズAI市場トップシェア**（Menlo Ventures調査）
  - Run-rate revenue: $87M → $5B+（60倍成長）
  - Series F: $13B調達、$183B post-money valuation
  - 顧客数: 1,000未満 → 300,000以上（300倍）
  - 消費者利用の80%が米国外
  - NBIM: 20%生産性向上（213,000時間相当）
  - Novo Nordisk: 臨床文書時間99.9%削減（10週→10分）
  - Rakuten: Claude Codeで機能開発79%短縮
- **引用URL:** https://www.anthropic.com/news/anthropic-expands-global-leadership-in-enterprise-ai-naming-chris-ciauri-as-managing-director-of

### INFO-012
- **タイトル:** OpenAI for Developers in 2025
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2025-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-04
- **関連企業:** OpenAI
- **要約:** 2025年の開発者プラットフォーム総括。agent-native APIsへの移行、Reasoning統合、マルチモダリティ成熟、Responses API/Agents SDK/AgentKitによるエージェント構築ブロック提供、Codexの成熟を報告。
- **キーファクト:**
  - **Responses API**: Chat Completionsの簡潔さとAssistants APIのツール使用を統合
  - **Agents SDK**: オープンソース（Python/TypeScript）、provider-agnostic
  - **AgentKit**: 高レベルエージェント開発ツール
  - **Codex CLI**: ローカルリポジトリで動作するオープンソースCLI
  - **AGENTS.md**: エージェント向けプロジェクト設定標準
  - **MCP**: Model Context Protocol統合
  - **gpt-oss 120b/20b**: オープンウェイトモデル公開
  - 推奨モデル: GPT-5.2（汎用）、GPT-5.2 Pro（深い推論）、GPT-5.2-Codex（コード）
- **引用URL:** https://developers.openai.com/blog/openai-for-developers-2025/

### INFO-013
- **タイトル:** New tools for building agents
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2025-03-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** Responses API、Agents SDK、Computer Use Toolを発表。Responses APIはChat CompletionsとAssistants APIを統合したエージェント向けAPI。Computer Use ToolはOperatorと同じCUAモデルをAPIで提供（OSWorld 38.1%、WebArena 58.1%）。
- **キーファクト:**
  - **Responses API**: Web Search、File Search、Computer Useを組み込みツールとして提供
  - **Web Search**: SimpleQA 90%（GPT-4o search preview）
  - **Computer Use**: OSWorld 38.1%（人間72.4%）、WebArena 58.1%
  - **Agents SDK**: Swarm後継、Guardrails、Handoffs、Tracing搭載
  - **Assistants API廃止**: 2026年中盤にResponses APIへ移行
  - CoinbaseがAgentKitで数時間でエージェント構築
  - BoxがWeb Search + Agents SDKでエンタープライズ検索実現
- **引用URL:** https://openai.com/index/new-tools-for-building-agents/

### INFO-014
- **タイトル:** Introducing advanced tool use on the Claude Developer Platform
- **ソース:** Anthropic (Engineering Blog)
- **公開日:** 2025-11-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude Developer Platformに3つの新機能を追加: Tool Search Tool（動的ツール発見）、Programmatic Tool Calling（コード経由でのツール実行）、Tool Use Examples（使用例による学習）。大規模ツールライブラリでのコンテキスト節約と精度向上を実現。
- **キーファクト:**
  - **Tool Search Tool**: ツール定義を85%削減（77K→8.7K tokens）、MCP評価精度: Opus 4.5で79.5%→88.1%
  - **Programmatic Tool Calling**: トークン37%削減（43,588→27,297）、GIAベンチマーク46.5%→51.2%
  - **Tool Use Examples**: 複雑パラメータ処理精度72%→90%
  - 58ツール（GitHub 35、Slack 11等）で約55K tokens消費が課題
  - Claude for ExcelがPTC活用で大規模スプレッドシート処理を実現
- **引用URL:** https://www.anthropic.com/engineering/advanced-tool-use

### INFO-015
- **タイトル:** Agent SDK overview
- **ソース:** Anthropic (公式ドキュメント)
- **公開日:** 2025
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-ANTHROPIC-MARKET
- **関連企業:** Anthropic
- **要約:** Claude Code SDKがClaude Agent SDKに改名。Python/TypeScript対応。Read、Write、Edit、Bash、Glob、Grep、WebSearch、WebFetch等のビルトインツールを提供。Skills、Slash Commands、Memory、MCP、Pluginsをサポート。
- **キーファクト:**
  - Claude Code SDK → Claude Agent SDKに改名
  - ビルトインツール: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch, AskUserQuestion
  - Bedrock、Vertex AI、Azure AI Foundryに対応
  - Skills（.claude/skills/）、Commands（.claude/commands/）、Memory（CLAUDE.md）サポート
  - ライセンス: Anthropic Commercial Terms of Service
- **引用URL:** https://platform.claude.com/docs/en/agent-sdk/overview

### INFO-016
- **タイトル:** Building AI Agents with Google Gemini 3 and Open Source Frameworks
- **ソース:** Google Developers Blog
- **公開日:** 2025-11-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Google
- **要約:** Gemini 3 Pro Preview発表。thinking_level（推論深度制御）、Thought Signatures（状態保持）、media_resolution（マルチモーダル品質制御）を導入。LangChain、Vercel AI SDK、LlamaIndex、Pydantic AI、n8nがDay 0サポート。
- **キーファクト:**
  - **thinking_level**: high（深い計画）vs low（高速スループット）
  - **Thought Signatures**: ツール呼び出し間で推論状態を暗号化して保持
  - **media_resolution**: high（細かいテキスト）、medium（PDF最適）、low（動画・一般画像）
  - Vercel: Gemini 3 Proで推論+17%（Next.jsリーダーボード）
  - **ベストプラクティス**: CoTプロンプト不要、Temperature 1.0固定、Thought Signatures必須
- **引用URL:** https://developers.googleblog.com/building-ai-agents-with-google-gemini-3-and-open-source-frameworks/

### INFO-017
- **タイトル:** Using Tools & Agents with Gemini API
- **ソース:** Google AI for Developers
- **公開日:** 2026-02-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Google
- **要約:** Gemini APIのツール・エージェント機能概要。Google Search、Google Maps、Code Execution、URL Context、Computer Use、File Searchを組み込みツールとして提供。Deep Researchエージェントも利用可能。
- **キーファクト:**
  - 組み込みツール: Google Search, Google Maps, Code Execution, URL Context, Computer Use (Preview), File Search
  - **Deep Researchエージェント**: 市場分析、デューデリジェンス、文献レビュー
  - エージェントフレームワーク: LangChain/LangGraph, LlamaIndex, CrewAI, Vercel AI SDK, Google ADK
  - Live APIでリアルタイムストリーミング対応
- **引用URL:** https://ai.google.dev/gemini-api/docs/tools

### INFO-018
- **タイトル:** OpenAI Frontier - Enterprise platform for AI agents
- **ソース:** OpenAI (公式)
- **公開日:** 2026
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIのエンタープライズAIエージェントプラットフォーム。Business Context（組織データ連携）、Agent Execution（並列タスク実行）、Evaluation & Optimization（改善ループ）を提供。エネルギー、製造、金融などで導入。
- **キーファクト:**
  - **Business Context**: データウェアハウス、CRM、内部アプリと連携
  - **Agent Execution**: 並列で複雑タスクを完遂
  - **Enterprise IAM**: エージェントID・アクセス管理
  - **コンプライアンス**: SOC 2 Type II, ISO 27001/27017/27018/27701, CSA STAR
  - 顧客例: 製造業で$1B+ CapEx最適化、銀行で億単位イベント処理
- **引用URL:** https://openai.com/business/frontier/

### INFO-019
- **タイトル:** Anthropic Trust Center - Compliance Overview
- **ソース:** Anthropic (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** Anthropicの包括的コンプライアンス認証一覧。Claude API/EnterpriseでSOC 2、ISO 27001/42001、HIPAA、NIST 800-171、FedRAMP Highを取得。Claude for Government (C4G)はFedRAMP High認証済み。
- **キーファクト:**
  - **Claude API/Enterprise**: SOC 2 Type 2, ISO 27001, ISO 42001, CSA STAR, HIPAA, NIST 800-171
  - **Claude for Government (C4G)**: FedRAMP High認証
  - **Bedrock GovCloud/Vertex Assured Workloads**: FedRAMP High、DoD IL4/IL5
  - Web Search機能がC4Gで利用可能に（2026-02-26）
  - Claude Code FISMA Best Practicesガイド公開
- **引用URL:** https://trust.anthropic.com/

### INFO-020
- **タイトル:** Claude Code Security - Making frontier cybersecurity capabilities available
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-02-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-04, KIQ-CODE-QUALITY
- **関連企業:** Anthropic
- **要約:** Claude Code Securityを発表。コードベースをスキャンして脆弱性を検出し、パッチを提案。Opus 4.6でオープンソース500+脆弱性を発見。Enterprise/Team向け限定研究プレビュー。
- **キーファクト:**
  - 静的解析ではなく「人間のセキュリティ研究者のように推論」
  - 多段階検証プロセスで誤検知をフィルタリング
  - 信頼度評定付きで人間承認必須
  - Opus 4.6で本番OSS 500+脆弱性発見（数十年見逃されていたもの含む）
  - サイバーセキュリティ株に影響（CrowdStrike -8%、Okta -9%）
- **引用URL:** https://www.anthropic.com/news/claude-code-security

### INFO-021
- **タイトル:** Introducing the Model Context Protocol (MCP)
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2024-11-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Model Context Protocol (MCP)をオープンソース化。AIアシスタントとデータソースを接続する統一標準プロトコル。Block、Apollo、Zed、Replit、Codeium、Sourcegraphが採用。
- **キーファクト:**
  - Google Drive, Slack, GitHub, Git, Postgres, Puppeteer向けビルトインサーバー提供
  - Claude 3.5 SonnetがMCPサーバー実装に最適
  - Claude DesktopアプリでローカルMCPサーバー接続可能
  - Claude for Workでリモート本番MCPサーバー展開予定
  - 断片化した統合を単一プロトコルで置換
- **引用URL:** https://www.anthropic.com/news/model-context-protocol

### INFO-022
- **タイトル:** Security and privacy at OpenAI
- **ソース:** OpenAI (公式)
- **公開日:** 2026
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAIのセキュリティ・プライバシー commitments。API、ChatGPT Enterprise/Business/EduがSOC 2 Type 2、CSA STAR Level 1認証。GDPR、CCPA準拠。HIPAA BAA提供。
- **キーファクト:**
  - SOC 2 Type 2（Security & Confidentiality）
  - CSA STAR Level 1
  - GDPR、CCPA準拠、DPA提供
  - HIPAA BAA提供（対象ケース）
  - 定期的第三者ペネトレーションテスト
  - Bug Bounty Program運営
- **引用URL:** https://openai.com/security-and-privacy/

### INFO-023
- **タイトル:** 13 best AI agent platforms & builders in 2026
- **ソース:** Marketer Milk
- **公開日:** 2026-02-04
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** N/A (業界分析)
- **要約:** 2026年の主要AIエージェントプラットフォーム比較。Gumloop、Relay.app、Claude Code、Make、Stack AI、Voiceflow、OpenAI Operator、Devin AI等を評価。ノーコード〜エンジニア向けまで幅広くカバー。
- **キーファクト:**
  - **Gumloop**: $37/月〜、マーケティング向け、MCP対応
  - **Claude Code**: $20/月〜、カスタムエージェント構築に最適
  - **OpenAI Operator**: $199/月〜、Web操作エージェント
  - **Devin AI**: $500/月〜、プログラミングアシスタント
  - **Make**: $10.59/月〜、3,000+統合、Zapier代替
  - **Voiceflow**: $50/月〜、カスタマーサポート向け
- **引用URL:** https://www.marketermilk.com/blog/best-ai-agent-platforms

### INFO-024
- **タイトル:** Gemini 3 Deep Think benchmark results
- **ソース:** Google (公式評価) / Medium分析
- **公開日:** 2026-02-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** Google
- **要約:** Gemini 3 Deep Thinkが主要ベンチマークで記録的な結果を達成。ARC-AGI-2: 84.6%、Humanity's Last Exam (HLE): 48.4%、MMMU-Pro: 81.5%、Codeforces: Elo 3455。Turing Testに代わるベンチマークの重要性を示唆。
- **キーファクト:**
  - **ARC-AGI-2**: 84.6%（ARC Prize Verified v2 semi-private）
  - **HLE**: 48.4%（ツールなし）
  - **MMMU-Pro**: 81.5%
  - **Codeforces**: Elo 3455（ツールなし）
  - Claude Opus 4.6、GPT-5.2と比較公開（他社データは自己申告ベース）
  - ベンチマーク評価手法の重要性強調（検証プログラム、スコアリング規約等）
- **引用URL:** https://medium.com/data-science-collective/gemini-3-deep-think-shocked-everyone-why-benchmarks-are-the-new-turing-test-arc-agi-2-hle-c35562cd5190

### INFO-025
- **タイトル:** Anthropic raises $30 billion in Series G funding at $380 billion valuation
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-02-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-ANTHROPIC-MARKET
- **関連企業:** Anthropic
- **要約:** Anthropicが$30B Series G調達を発表（$380B post-money valuation）。Run-rate revenueは$14B。Claude CodeのRun-rate revenueは$2.5B。GIC、Coatue等が主導。OpenAIの$66.4Bに対し$69.1B調達で上回る。
- **キーファクト:**
  - **Series G**: $30B調達、$380B評価（前回$183Bから2倍超）
  - **Run-rate revenue**: $14B（3年間で毎年10倍成長）
  - **Claude Code revenue**: $2.5B run-rate（2026年初から2倍超）
  - **$100K+顧客**: 過去1年で7倍成長
  - **$1M+顧客**: 2年前12社→現在500社超
  - **Fortune 10**: 8社がClaude顧客
  - **GitHub commits**: 世界の公開コミット4%がClaude Code作成（1ヶ月で倍増）
  - 調達総額: $69.1B（OpenAI $66.4Bを上回る）
- **引用URL:** https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation

### INFO-026
- **タイトル:** Claude Code and Cowork expansion
- **ソース:** Anthropic (Series G発表内)
- **公開日:** 2026-02-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-ANTHROPIC-MARKET
- **関連企業:** Anthropic
- **要約:** Claude Codeが急成長。Run-rate revenue $2.5B（2026年初から倍増）。週間アクティブユーザーも倍増。ビジネス購読は2026年初から4倍。Cowork（知識労働向け）を発表、11のOSSプラグイン提供。
- **キーファクト:**
  - Claude Code revenue: $2.5B run-rate
  - 週間アクティブユーザー: 2026年1月から倍増
  - ビジネス購読: 2026年初から4倍
  - エンタープライズ: Claude Code収益の過半を占める
  - **Cowork**: 11のOSSプラグイン（sales, legal, finance等）
  - **Claude Opus 4.6**: GDPval-AAで世界最高
  - Healthcare/Life Sciences: HIPAA対応でClaude for Enterprise利用可能
- **引用URL:** https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation

## メタデータ（最終更新）
- 収集日時: 2026-03-05 03:00 UTC
- 実行クエリ数: 15 / 56
- scrape実行数: 8件
- 収集情報数: 26件
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-03 ✓, KIQ-002-06 ✓, KIQ-003-02 ✓, KIQ-003-04 ✓, KIQ-005-01 ✓, KIQ-ANTHROPIC-MARKET ✓, KIQ-CODE-QUALITY ✓
- 品質フラグ: PARTIAL - クエリ実行数が目標（56件）に未達。ネットワークエラーにより一部検索失敗。手動補完推奨。
