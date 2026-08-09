# 収集データ: 2026-08-09

## メタデータ
- 収集日時: 2026-08-08 23:34 UTC ～ 2026-08-09 (Phase 1 完了)
- 品質フラグ: COMPLETE
- 検索クエリ実行数: 52 (Firecrawl search)
- スクレイプ記事数: 3 (Anthropic公式ブログ)
- INFO エントリ数: 84
- Evidence ID 範囲: EVD-20260809-0001 ～ EVD-20260809-0084
- KIQ カバレッジ: KIQ-001-01～05, KIQ-002-01～06, KIQ-003-01～05, KIQ-004-01～04, KIQ-005-01～03, BYTEDANCE-CHINESE, 動的クエリ×5
- Tier 1 企業別エントリ: OpenAI多数, Anthropic多数, Google多数, xAI多数, ByteDance 5+
- PIR カバレッジ: PIR-2026-001～005 全件カバー

## 動的追加クエリ（Arbiterフィードバック基づく）
- KIQ-NEW-01: DeepSeek四半期Intelligence Index時系列データ（SCN-002/004弁別）
- KIQ-NEW-02: KIQ-MIL-001 人間却下比率（IND-030 critical解消）
- KIQ-NEW-03: Federal Register/BIS直接公告（H-GOV-001 Sunset clause検証）
- KIQ-NEW-04: KIQ-CAR-002-OPS 設計/評価スキル賃金プレミアム定量データ
- KIQ-NEW-05: エントリーティア vs フロンティアティア価格分離トレンド

## 収集結果

---

### KIQ-001-01: 各社のAgent SDK/APIの機能拡張ロードマップはどうなっているか？

### INFO-001
- **タイトル:** Improving Fable 5's biology safeguards
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-08-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** AnthropicはClaude Fable 5の生物セーフガードを大幅に改善し、biology関連の誤検知（フォールバック）を約85%削減した。Fable 5ユーザーは日常的な健康・教育・生物学的質問でのフォールバックが大幅に減少する。ただし二重用途（ウイルス学・毒性学・分子設計）は依然Opus 5にフォールバックする。
- **キーファクト:**
  - Fable 5のbiology関連フォールバックを約85%削減
  - Claude.ai全体で全フォールバック約67%減、Claude Code 17%減、Claude Platform 7%減
  - 二重用途プロフェッショナル生物・創薬クエリは引き続きブロック
- **引用URL:** https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards
- **Evidence ID:** EVD-20260809-0001

### INFO-002
- **タイトル:** Mariano-Florentino (Tino) Cuéllar to join Anthropic as Chief Global Affairs Officer
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-08-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** Anthropicは初のChief Global Affairs Officerとして、カーネギー国際平和財団元総裁・カリフォルニア州最高裁判事のTino Cuéllarを迎える。政策・国際戦略的エンゲージメント・政府関係を統括する。Long-Term Benefit Trustの理事を2026年1月から務めていたが、Trustを離れて入社。
- **キーファクト:**
  - 元カーネギー国際平和財団総裁・カリフォルニア州最高裁判事
  - スタンフォード法学院教授・HAI上級フェロー
  - Anthropic初のChief Global Affairs Officer
- **引用URL:** https://www.anthropic.com/news/tino-cuellar
- **Evidence ID:** EVD-20260809-0002

### INFO-003
- **タイトル:** Claude web search now available globally on all plans
- **ソース:** Claude/Anthropic公式ブログ
- **公開日:** 2026-05-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** ClaudeのWeb検索機能が全プラン・世界中で利用可能になった。Claudeはインターネット検索で最新情報を提供し、引用付きで回答する。営業チームのアカウント計画、財務アナリストの市場データ分析、研究者の文献レビューなどに活用可能。
- **キーファクト:**
  - 全プラン・全世界でWeb検索機能が利用可能
  - 引用付きで回答を提供
- **引用URL:** https://www.anthropic.com/news/web-search
- **Evidence ID:** EVD-20260809-0003

### INFO-004
- **タイトル:** AI Agent Frameworks 2026: 10 Frameworks Ranked (Alice Labs)
- **ソース:** Alice Labs
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI, Anthropic, Google, Microsoft
- **要約:** 2026年8月時点のAIエージェントフレームワークランドスケープ分析。LangGraph 1.x、Microsoft Agent Framework 1.0、Claude Agent SDK、OpenAI Agents SDK、Google ADK 2.0など10フレームワーク＋8つのマネージドエンタープライズプラットフォームが存在。スタック選択が最優先（M365/Azure→Copilot Studio、AWS→Bedrock AgentCore、Google Cloud→Vertex AI Agent Builder）。
- **キーファクト:**
  - OpenAI Agents SDK (GA Mar 2026): 7プロバイダーでのネイティブサンドボックス実行
  - Microsoft Agent Framework 1.0 (GA Apr 3 2026): AutoGen + Semantic Kernelの後継、C#+Pythonパリティ
  - Google ADK 2.0: Python/TypeScript/Java/GoのSDKパリティ、ネイティブA2A
  - Hermes Agent (Nous Research): 2月ローンチ、7月末で~220K GitHub Stars（最速成長）
  - Claude Agent SDK: Anthropicネイティブ、Claude Code基盤、プロダクションスコア9/10
- **引用URL:** https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026
- **Evidence ID:** EVD-20260809-0004

### INFO-005
- **タイトル:** Google Gemini API Tools: Computer Use, File Search, URL Context
- **ソース:** Google AI for Developers公式ドキュメント
- **公開日:** 2026-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** Gemini APIはGoogle Search、Google Maps、Code Execution、URL Context、Computer Use (Preview)、File Searchの6つの組み込みツールを提供。Computer UseはブラウザUIの自動化を可能にする。Interactions APIでマネージドエージェントの定義・保存も可能。
- **キーファクト:**
  - Computer Use (Preview): ブラウザUI操作の自動化
  - File Search: 独自ドキュメントのインデックス・検索でRAGを可能にする
  - Interactions API: カスタムエージェントの定義・保存機能
- **引用URL:** https://ai.google.dev/gemini-api/docs/tools
- **Evidence ID:** EVD-20260809-0005

### INFO-006
- **タイトル:** Grok 4.5 Available on xAI API — Coding, Agentic Tasks, Knowledge Work
- **ソース:** SpaceXAI Docs
- **公開日:** 2026-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI (SpaceX子会社)
- **要約:** Grok 4.5がxAI APIで利用可能。コーディング、エージェントタスク、ナレッジワーク向け。価格は入力$2/1Mトークン、出力$6/1Mトークン。Grok Build（ターミナルベースのコーディングエージェント）も提供。
- **キーファクト:**
  - Grok 4.5: コーディング・エージェントタスク・ナレッジワーク向け
  - 価格: $2/1M input、$6/1M output tokens
  - Grok Build: ターミナルベースAIコーディングエージェント、ファイル編集・シェルコマンド実行
- **引用URL:** https://docs.x.ai/developers/release-notes
- **Evidence ID:** EVD-20260809-0006

### INFO-007
- **タイトル:** AI Agent SDK Comparison: Enterprise SLA and Security Concerns
- **ソース:** WorkOS Blog / Gravitee Report
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** 複数
- **要約:** Graviteeの2026 State of AI Agent Securityレポートは、企業内で300万以上のAIエージェントが稼働していると報告（Walmartの従業員数を超える規模）。MCPスプロールが新たなシャドーITリスクとして浮上しており、従来のシャドーIT検出ツールではMCP通信を監視できない。
- **キーファクト:**
  - 企業内で300万以上のAIエージェントが稼働
  - MCPスプロールがシャドーITの新形態
  - 従来のシャドーIT検出ツールがMCP通信に対応できない
- **引用URL:** https://workos.com/blog/mcp-sprawl-invisible-to-shadow-it-tools
- **Evidence ID:** EVD-20260809-0007

### INFO-008
- **タイトル:** Claude Agent SDK TypeScript Releases (v0.3.224 latest)
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版が活発に開発中。v0.3.224が最新リリース。Anthropic SDK TypeScript 0.116.0では、セッションバジェット、アドバイザーツール、会話中ツール変更ベータ、GitHubスキル自動ロードなどの新機能が追加。
- **キーファクト:**
  - Claude Agent SDK TypeScript最新版: v0.3.224
  - セッションバジェット、アドバイザーツール、会話中ツール変更ベータ追加
  - Python SDK 0.2.134 / TypeScript SDK 0.3.226がペアリリース
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260809-0008

---

### KIQ-001-02: 各社のAgent製品のエンタープライズ向け展開の進捗は？

### INFO-009
- **タイトル:** Drata Extends Trust Management Platform for AI Agent Governance
- **ソース:** Drata
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** 複数
- **要約:** DrataがAIエージェントガバナンス機能を限定公開で開始。AIエージェントの全アクションに対する継続的コントロール監視と証拠収集を提供。SOC2、FedRAMPコンプライアンス要件に対応。
- **キーファクト:**
  - AIエージェントの全アクションを継続監視
  - SOC2/FedRAMPコンプライアンス対応
  - 限定公開（Limited Availability）
- **引用URL:** https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents
- **Evidence ID:** EVD-20260809-0009

### INFO-010
- **タイトル:** Inference Hooks: Inline Data Loss Prevention for Claude Enterprise
- **ソース:** Claude/Anthropic公式ブログ
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Enterprise向けにInference Hooks機能を発表。インラインデータ損失防止（DLP）を実現し、エンタープライズのセキュリティ・コンプライアンス要件に対応。AktoもClaude Compliance Connectorをリリースし、リアルタイムDLPを提供。
- **キーファクト:**
  - Claude EnterpriseでInference Hooks（インラインDLP）を提供
  - AktoがClaude Compliance Connectorをリリース
  - リアルタイムコンプライアンス監視
- **引用URL:** https://claude.com/blog/claude-enterprise-inference-hooks
- **Evidence ID:** EVD-20260809-0010

### INFO-011
- **タイトル:** Vertex AI → Gemini Enterprise Agent Platform移行
- **ソース:** Google Cloud公式ドキュメント
- **公開日:** 2026-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Vertex AIがGemini Enterprise Agent Platformの一部になった。Gemini Deep Research Agent（事前構築エージェント）や、GKE Agent Sandbox（コスト線形増大を防ぐエージェントインフラ）が提供されている。消費オプションはPayGo、Provisioned Throughput、Batch Inference。
- **キーファクト:**
  - Vertex AIがGemini Enterprise Agent Platformに統合
  - Gemini Deep Research Agent提供
  - GKE Agent Sandboxでインフラコスト最適化
  - PayGo / Provisioned Throughput / Batch Inferenceの消費モデル
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes
- **Evidence ID:** EVD-20260809-0011

### INFO-012
- **タイトル:** Deloitte State of AI in the Enterprise 2026: Only 21% Have Mature Governance
- **ソース:** Lyzr Blog (Deloitte survey引用)
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** 複数
- **要約:** DeloitteのState of AI in the Enterprise 2026調査で、エンタープライズAIエージェントのガバナンス成熟モデルを持つ組織はわずか21%。Maven AGIのケーススタディではAgent Mavenがライブチャットの93%を回答、K1xの80%のチケットを解決。
- **キーファクト:**
  - エンタープライズのAIエージェントガバナンス成熟率: わずか21%
  - Maven AGI Agent Maven: チャット質問93%回答、チケット80%解決
  - PagerDuty: AIエージェント採用が高プロファイルインシデント増加を引き起こしている
- **引用URL:** https://www.lyzr.ai/blog/30-ai-agent-use-cases/
- **Evidence ID:** EVD-20260809-0012

### INFO-013
- **タイトル:** Run Claude Code Sessions on Your Own Compute
- **ソース:** Claude/Anthropic公式ブログ
- **公開日:** 2026-08-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Codeセッションを独自コンピュートリソースで実行する機能を発表。エンタープライズ顧客が自社インフラでエージェントを実行できるようになり、データ主権・コンプライアンス要件に対応。
- **キーファクト:**
  - Claude Codeセッションを独自コンピュートで実行可能
  - データ主権・コンプライアンス要件に対応
- **引用URL:** https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
- **Evidence ID:** EVD-20260809-0013

---

### KIQ-001-03: 各社のAgent開発者エコシステムの拡大状況は？

### INFO-014
- **タイトル:** MCP Server Ecosystem Reaches ~98,000 Servers
- **ソース:** MCP Toplist / Official MCP Registry
- **公開日:** 2026-08-04
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** 複数
- **要約:** MCP (Model Context Protocol)サーバーエコシステムが爆発的に拡大し、5つの集約サイト（Official MCP Registry、Glama、Smithery、mcp.so、PulseMCP）全体で97,936サーバーに達した。1週間で約16,529サーバーが追加されるペース。Official MCP Registry単体で20,125サーバー、Glamaが58,448サーバーで最大。
- **キーファクト:**
  - MCPサーバー総数: 97,936（5集約サイト合計）
  - 1週間で+16,529サーバー追加
  - Official MCP Registry: 20,125、Glama: 58,448、mcp.so: 8,333、PulseMCP: 7,342、Smithery: 3,903
- **引用URL:** https://mcptoplist.com/
- **Evidence ID:** EVD-20260809-0014

### INFO-015
- **タイトル:** AAIF Agent Plugins 1.0: Portable Package Format for AI Skills
- **ソース:** AAIF (Agentic AI Foundation)公式ブログ
- **公開日:** 2026-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** 複数
- **要約:** AAIFがAgent Plugins 1.0を発表。MCPと相補的な独立ガバナンスのポータブルパッケージフォーマットで、AIエージェントの再利用可能コンポーネントを標準化。「プラグインマーケットプレイス」の概念を開拓。OpenAI、Vercel等が参加。
- **キーファクト:**
  - Agent Plugins 1.0: MCPと相補的なポータブルパッケージフォーマット
  - 再利用可能なエージェントコンポーネントを標準化
  - プラグインマーケットプレイス概念の確立
  - OpenAI、Vercel等が参加
- **引用URL:** https://aaif.io/blog/from-skills-and-tools-to-portable-agent-plugins
- **Evidence ID:** EVD-20260809-0015

### INFO-016
- **タイトル:** Google Agent Plugins: Package Your Skills, Tools, and More
- **ソース:** Google Developers Blog
- **公開日:** 2026-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Google / DeepMind
- **要約:** GoogleがAgent PluginsとAgents CLIを発表。Antigravity、Gemini CLI、Claude Code、CursorなどあらゆるAIコーディングエージェントをエージェント構築・評価・デプロイ・監視の専門家に変える。MCP Stateless更新でAIエージェントインフラのスケーリングも改善。
- **キーファクト:**
  - Agents CLI: 全AIコーディングエージェント対応のエージェント構築ツール
  - MCP Stateless更新でインフラスケーリング改善
  - 統合AIモデルルーティングAPI
- **引用URL:** https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/
- **Evidence ID:** EVD-20260809-0016

### INFO-017
- **タイトル:** Sierra-Plaid Partnership: AI Agents Move from Conversations to Actions
- **ソース:** Sierra AI Blog
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** 複数
- **要約:** SierraとPlaidが提携し、Sierraのエージェント内でPlaid経由の銀行口座接続が可能に。AIエージェントが会話から実際の金融アクションへ移行する最初の事例。Kiteworks-Reco提携（AIエージェント可視性・データガバナンス）、Darktrace-Microsoft Agent 365統合も発表。
- **キーファクト:**
  - Sierra-Plaid提携: エージェント内での銀行口座接続
  - Kiteworks-Reco提携: AIエージェント可視性とデータガバナンス
  - Darktrace-Microsoft Agent 365統合: 行動ベースAIリスクシグナル
- **引用URL:** https://sierra.ai/blog/our-partnership-with-plaid
- **Evidence ID:** EVD-20260809-0017

### INFO-018
- **タイトル:** Tech Industry Leaders Launch Alliance for AI Agent Security
- **ソース:** The Journal
- **公開日:** 2026-08-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02
- **関連企業:** HPE, NVIDIA, 複数
- **要約:** HPE、NVIDIA等の技術業界リーダーがAIエージェントセキュリティのためのアライアンスを立ち上げ。クラウドワークロードアイデンティティがエージェントレイヤーに移行。HPEは「現代のAIシステムはエージェントフレームワーク、ハーネス、ガードレール、ガバナンスメカニズムに依存している」と声明。
- **キーファクト:**
  - AIエージェントセキュリティアライアンス設立
  - HPE、NVIDIA等が参加
  - クラウドワークロードアイデンティティがエージェントレイヤーへ
- **引用URL:** https://thejournal.com/articles/2026/08/05/tech-industry-leaders-launch-alliance-for-ai-agent-security.aspx
- **Evidence ID:** EVD-20260809-0018

### INFO-019
- **タイトル:** Microsoft Agent Skills: Skills, MCP Servers, Custom Agents
- **ソース:** GitHub (microsoft/skills)
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Microsoft
- **要約:** MicrosoftがAgent Skillsリポジトリを公開。スキル、MCPサーバー、カスタムエージェント、エージェントフレームワーク用スキルを提供。Python、foundryカテゴリなどでスキル追加が可能。AI Agents DirectoryスキルマーケットプレイスでOpenAI、Anthropicのスキルも配布。
- **キーファクト:**
  - Microsoft Agent Skillsリポジトリ公開
  - MCPサーバーとカスタムエージェントを統合
  - AI Agents Directoryでクロスプラットフォームスキル配布
- **引用URL:** https://github.com/microsoft/skills
- **Evidence ID:** EVD-20260809-0019

---

### KIQ-001-04: 各社のマルチモーダルAgent統合の進捗は？

### INFO-020
- **タイトル:** OpenAI GPT-5.6 Sol: Next-Generation Model with Stronger Agentic Capabilities
- **ソース:** OpenAI公式
- **公開日:** 2026-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6 Solをプレビュー。コーディング、科学、サイバーセキュリティでより強力な能力、コーディング・生物学・エージェント能力が向上。また未発表の「Astra」モデルファミリーは複雑な長時間実行マルチエージェントタスクに優れ、10の重要な数学問題を解決した。
- **キーファクト:**
  - GPT-5.6 Sol: コーディング・科学・サイバーセキュリティ強化
  - Astraモデル: 長時間マルチエージェントタスク特化、10の数学問題解決
  - Codex: クラウドベースソフトウェアエンジニアリングエージェント、並列タスク実行
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260809-0020

### INFO-021
- **タイトル:** Google DeepMind Gemini Robotics 2 Enables Full Body Control
- **ソース:** The Robot Report
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** Google DeepMindがGemini Robotics 2を発表。ロボットが全ての動きを推論可能になり、ヒューマノイドの歩行・しゃがみ込み・複雑タスクが可能。Gemini Robotics ER 2はマルチロボット協調、人の検出・停止機能、91.3%のモーメント発見精度を提供。
- **キーファクト:**
  - Gemini Robotics 2: 全身制御を可能にする推論ベースロボティクス
  - Gemini Robotics ER 2: マルチロボット協調、91.3%モーメント発見精度
  - 人の検出・作業エイヤ安全性機能
- **引用URL:** https://www.therobotreport.com/google-deepmind-says-gemini-robotics-2-enables-full-body-control/
- **Evidence ID:** EVD-20260809-0021

### INFO-022
- **タイトル:** Computer-Use AI Agents: Best Open-Source & Closed-Source Tools 2026
- **ソース:** Turing Post
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** OpenAI, Anthropic, Google, Amazon
- **要約:** 2026年のコンピュータ使用AIエージェント比較。OSS（UI-TARS、Browser Use、Stagehand、Skyvern、Agent-E）vs プロプライエタリ（ChatGPT Work、Claude Cowork、Gemini in Chrome、Amazon Nova Act、Manus Browser Operator）。Azure AI FoundryもBrowser Automation Tool (Preview)とComputer Use Toolを提供。
- **キーファクト:**
  - OSS系: UI-TARS、Browser Use、Stagehand、Skyvern、Agent-E
  - プロプライエタリ系: ChatGPT Work、Claude Cowork、Gemini in Chrome、Amazon Nova Act、Manus Browser Operator
  - Azure AI Foundry: Browser Automation Tool (Preview) + Computer Use Tool
- **引用URL:** https://www.turingpost.com/p/computer-use-ai-agents
- **Evidence ID:** EVD-20260809-0022

---

### KIQ-001-05: 各社の「スキル配布と実行環境」はどう設計され、ロックインをどこで作っているか？

### INFO-023
- **タイトル:** NVIDIA OpenShell: Safe, Private Runtime for Autonomous AI Agents
- **ソース:** GitHub (NVIDIA/openshell)
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** NVIDIA
- **要約:** NVIDIAがOpenShellをオープンソース化。自律的AIエージェント向けの安全でプライベートなランタイム。エージェントが.agents/skills/ディレクトリでスキルを自動発見する設計。安全なサンドボックス実行環境を提供。
- **キーファクト:**
  - OpenShell: AIエージェント向け安全・プライベートランタイム
  - .agents/skills/ディレクトリでスキル自動発見
  - NVIDIAのオープンソース戦略
- **引用URL:** https://github.com/NVIDIA/openshell
- **Evidence ID:** EVD-20260809-0023

### INFO-024
- **タイトル:** Claude Code Native Sandbox Runtime
- **ソース:** GitHub (claude-code-ultimate-guide)
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude Codeがオープンソースのネイティブサンドボックスランタイムを提供。`npx @anthropic-ai/sandbox-runtime`でMCPサーバーを含む任意のコマンドをサンドボックス化。ファイル・ネットワーク隔離をサポート。WebAssemblyベースのMCPツールサンドボックス化も実験的提供。
- **キーファクト:**
  - Claude Codeネイティブサンドボックスランタイム（オープンソース）
  - `npx @anthropic-ai/sandbox-runtime`でMCPサーバーサンドボックス化
  - ファイル・ネットワーク隔離サポート
  - WebAssemblyベースMCPツールサンドボックス（実験的）
- **引用URL:** https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/guide/security/sandbox-isolation.md
- **Evidence ID:** EVD-20260809-0024

### INFO-025
- **タイトル:** Agent Skills Marketplace Ecosystem: 8+ Marketplaces Competing
- **ソース:** GitHub (gmh5225/awesome-skills)
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** 複数
- **要約:** AIエージェントスキルマーケットプレイスエコシステムが急成長。Learn Skills、skillsmp.com、SkillStore（セキュリティ監査付き）、agentskills.me（収益分配）、TokRepo（600+スキル・MCPサーバー）、CreatorSkills等8以上のマーケットプレイスが存在。クロスプラットフォーム対応が進む。
- **キーファクト:**
  - 8以上のスキルマーケットプレイスが存在
  - SkillStore: セキュリティ監査付きマーケットプレイス
  - TokRepo: 600以上のスキル・MCPサーバー登録
  - agentskills.me: 開発者収益分配モデル
- **引用URL:** https://github.com/gmh5225/awesome-skills
- **Evidence ID:** EVD-20260809-0025

### INFO-026
- **タイトル:** Trusted Agentic AI Landscape Q3 2026: Vendor Selection, Sovereignty, Lock-in
- **ソース:** Kai Waehner Blog
- **公開日:** 2026-08-04
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** 複数
- **要約:** Q3 2026のTrusted Agentic AIランドスケープがエンタープライズAIベンダーを信頼度とロックイン度でマッピング。主権性、オープンウェイト、エージェントリスクの3軸で評価。「補助金付き価格設定の隠れたコスト=ベンダーロックイン」が指摘される。
- **キーファクト:**
  - エンタープライズAIベンダーを信頼度×ロックイン度でマッピング
  - 主権性・オープンウェイト・エージェントリスクの3評価軸
  - 補助金価格設定がロックインの隠蔽手段
- **引用URL:** https://www.kai-waehner.de/blog/2026/08/04/trusted-agentic-ai-landscape-q3-2026-enterprise-vendor-selection-sovereignty-and-lock-in/
- **Evidence ID:** EVD-20260809-0026

---

### KIQ-002-01: 主要クラウドプロバイダーのAI Agent統合状況はどうか？

### INFO-027
- **タイトル:** AWS Bedrock Agents Classic Deprecated; AgentCore Takes Over
- **ソース:** AWS公式ドキュメント
- **公開日:** 2026-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** Amazon Bedrock Agents（旧）が新規顧客向けにクローズド。後継のBedrock AgentCoreが本番AIエージェント向けの永続的・マネージドEC2インフラを提供。マルチエージェント協調、GPUサポート、テンポラルポリシーによるセキュリティを特徴とする。MCPプロトコルネイティブサポート。
- **キーファクト:**
  - Bedrock Agents (Classic): 新規顧客クローズド
  - Bedrock AgentCore: 永続的マネージドEC2インフラ、GPUサポート
  - MCPプロトコルネイティブサポート、テンポラルポリシーセキュリティ
- **引用URL:** https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- **Evidence ID:** EVD-20260809-0027

### INFO-028
- **タイトル:** Azure AI Foundry: Enterprise-Grade Agent Building with Security
- **ソース:** Visual Studio Magazine
- **公開日:** 2026-08-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundryがエンタープライズ向けエージェント構築を提供。ネイティブエンタープライズグレードセキュリティ（プライベートエンドポイント、RBAC）、Azure AI Search統合、フロンティア+OSSモデルカタログ、組み込み安全ツール。Browser Automation Tool (Preview)とComputer Use Toolも提供。
- **キーファクト:**
  - エンタープライズグレードセキュリティ（プライベートエンドポイント、RBAC）
  - Azure AI Search統合でデータグラウンディング
  - Browser Automation Tool (Preview) + Computer Use Tool
  - フロンティア+OSSモデルカタログ
- **引用URL:** https://visualstudiomagazine.com/articles/2026/08/04/building-intelligent-agents-with-azure-ai-foundry-from-idea-to-enterprise-ready-solutions.aspx
- **Evidence ID:** EVD-20260809-0028

### INFO-029
- **タイトル:** AI Agent Marketplace Comparison: 10 Platforms Ranked
- **ソース:** AI Ops School
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-01, KIQ-001-03
- **関連企業:** OpenAI, Microsoft, Salesforce, Google, AWS, 複数
- **要約:** AIエージェントマーケットプレイス10選を比較。OpenAI GPT Store、Copilot Studio（エンタープライズエージェント）、AgentExchange（CRMエージェント/Salesforce）、Vertex AI Marketplace（クラウドAIエージェント）、AWS Marketplace AI Agents、Hugging Face Spaces、CrewAI Marketplace等。
- **キーファクト:**
  - OpenAI GPT Store: 大規模エージェントエコシステム
  - Copilot Studio: ビジネス統合重視のエンタープライズ
  - Vertex AI Marketplace: AIインフラ統合
  - AgentExchange (Salesforce): CRMワークフロー特化
- **引用URL:** https://aiopsschool.com/blog/top-10-ai-agent-marketplaces-features-pros-cons-comparison-2/
- **Evidence ID:** EVD-20260809-0029

---

### KIQ-002-02: エンタープライズ顧客のAI Agent採用率と主要ユースケースは？

### INFO-030
- **タイトル:** 3 Million AI Agents Running Inside Corporations (Gravitee Report)
- **ソース:** WorkOS / Gravitee 2026 State of AI Agent Security
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** 複数
- **要約:** Graviteeの2026 State of AI Agent Securityレポートで、企業内で稼働するAIエージェントが300万を超え、Walmartの従業員数を上回る規模。PagerDutyは「AIエージェント採用が高プロファイルインシデントを増加させ、収益に影響を与えている」と報告。
- **キーファクト:**
  - 企業内AIエージェント稼働数: 300万超（Walmart従業員数超）
  - AIエージェント採用がインシデント増加・収益影響を引き起こす
  - Deloitte調査: ガバナンス成熟モデル保持組織はわずか21%
- **引用URL:** https://workos.com/blog/mcp-sprawl-invisible-to-shadow-it-tools
- **Evidence ID:** EVD-20260809-0030

---

### KIQ-002-03: 規制環境がエンタープライズAI採用にどう影響するか？

### INFO-031
- **タイトル:** EU AI Act Enforcement Powers Begin August 2026
- **ソース:** CNBC
- **公開日:** 2026-08-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** Anthropic, OpenAI, 複数
- **要約:** EU AI Actの執行権限が2026年8月から本格始動。欧州委員会はAIモデルの検査、市場アクセス制限、最大1500万ユーロまたは売上高3%の罰金を科す権限を持つ。Anthropic、OpenAI等が新たな執行の対象。透明性要件と高リスクAIシステムの厳格な義務が適用開始。
- **キーファクト:**
  - 2026年8月からEU AI Act執行権限本格発効
  - 罰金: 最大1500万ユーロまたは売上高3%
  - 欧州委員会のAIモデル検査・市場アクセス制限権限
  - Anthropic、OpenAI等が主要対象
- **引用URL:** https://www.cnbc.com/2026/08/03/eu-ai-act-enforcement-powers.html
- **Evidence ID:** EVD-20260809-0031

### INFO-032
- **タイトル:** Trump "One Rule" Executive Order: Federalizing AI Regulation Against States
- **ソース:** Mashable / Hinshaw Law
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** トランプ大統領が州レベルAI規制を実質的に禁止する「ワンルール」大統領令に署名。2つの新たな連邦AI監視メカニズムを設立。一方で国防生産法（DPA）を invoke して最強力なAIシステム開発企業を追跡。州は現在、連邦の報復を恐れずにAI規制を制定可能な状態。
- **キーファクト:**
  - トランプ大統領令: 州レベルAI規制を実質禁止、連邦一元化
  - 2つの新連邦AI監視メカニズム設立
  - 国防生産法で最強力AIシステム開発企業を追跡
  - EO 14179: AIにおける米国リーダーシップの障壁除去
- **引用URL:** https://mashable.com/article/trump-signs-ai-executive-order
- **Evidence ID:** EVD-20260809-0032

### INFO-033
- **タイトル:** China AI Regulation: CAC Algorithm Registry, Ethics Review, Agent Security Standards
- **ソース:** Tech Letter / regulations.ai
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance, 複数
- **要約:** 中国のAI規制2026: CACアルゴリズム登録、倫理審査義務化、エージェントセキュリティ標準。AI生成コンテンツラベリング（2025年9月発効）、ネットワークデータセキュリティ管理規則（2025年1月発効）、サイバーセキュリティ法改正（2026年1月発効）が執行フェーズ。16のAI安全標準が策定済み。ヒューマノイドAI対話サービス規制が諮問中。
- **キーファクト:**
  - CACアルゴリズム登録制、倫理審査義務化
  - 16のAI安全標準策定済み
  - AI生成コンテンツラベリング法: 2025年9月発効、2026年1月から執行開始
  - ヒューマノイドAI対話サービス規制: 諮問中（意見募集期限2026年1月25日）
- **引用URL:** https://www.techletter.co/p/how-china-regulates-ai-and-agents
- **Evidence ID:** EVD-20260809-0033

---

### KIQ-002-06: 政府・軍によるAI企業への経済的圧力はAI業界にどう影響しているか？

### INFO-034
- **タイトル:** Pentagon Deploys AI Agents for Admin Tasks; Agent Network Expanding
- **ソース:** Military Times / Potomac Officers Club
- **公開日:** 2026-08-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Salesforce, Palantir, OpenAI
- **要約:** ペンタゴンがSalesforce AIエージェントを機密情報を扱う管理タスク向けに承認・デプロイ。ペンタゴンの「Agent Network」計画はPalantir（Maven Smart System）とLumbraのAIオーケストレーション技術を基盤に戦場意思決定を加速。DODはAIで民間人採用プロセスを30日に短縮する計画。
- **キーファクト:**
  - ペンタゴンがSalesforce自律AIエージェントを機密情報タスクで承認
  - Agent Network: Palantir + Lumbra基盤で戦場意思決定加速
  - DOD: AIで民間人採用を30日に短縮する計画
- **引用URL:** https://www.militarytimes.com/news/your-military/2026/08/07/pentagon-ready-to-deploy-ai-agents-for-admin-tasks/
- **Evidence ID:** EVD-20260809-0034

### INFO-035
- **タイトル:** Anthropic Supply Chain Risk Designation: Judge Rules Evidence Insufficient
- **ソース:** VMTech / Instagram News / LinkedIn
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** 連邦判事Rita LinがAnthropicの「サプライチェーンリスク」指定の証拠不十分と判決。キルスイッチの証拠も発見されず。トランプ政権は全連邦機関にAnthropic使用停止を命令。ヘグセス国防長官がAnthropicを「サプライチェーンリスク」に指定（通常は外国の敵対者向け）。一方、OpenAIは制限なしでペンタゴンと契約。Anthropicは2億ドル契約を失い、OpenAIが主要ペンタゴン契約を獲得。
- **キーファクト:**
  - 連邦判事: Anthropic「サプライチェーンリスク」指定の証拠不十分、キルスイッチ証拠なし
  - ヘグセス国防長官: Anthropicを「サプライチェーンリスク」指定（通常は外国敵対者向け）
  - Anthropic: 制限要求→ブラックリスト・刑事告発脅迫・2億ドル契約喪失
  - OpenAI: 制限なし→主要ペンタゴン契約獲得
  - イラン攻撃開始数時間前にOpenAIがペンタゴンと契約
- **引用URL:** https://vmtech.rs/en/instagram-insights/anthropic-supply-chain-risk-evidence
- **Evidence ID:** EVD-20260809-0035

### INFO-036
- **タイトル:** Senate Democrats Demand Answers on Anthropic Pentagon Treatment
- **ソース:** WTAJ News / American Progress
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** 民主党上院議員がAnthropicが2つのレッドライン（致死的自律兵器と国内大量監視での使用禁止）の削除を強要された件で回答を要求。Center for American Progressは「トランプ政権がAI巨人Anthropicの見せしめを作ろうとしている」と分析。Google、Anthropic、OpenAIが合同規制案をホワイトハウスに提出。
- **キーファクト:**
  - 上院民主党: Anthropicレッドライン強制削除件で回答要求
  - Center for American Progress: 「見せしめ」分析
  - Anthropicの2つのレッドライン: 致死的自律兵器・国内大量監視での使用禁止
  - Google/Anthropic/OpenAI合同規制案提出
- **引用URL:** https://www.americanprogress.org/article/the-trump-administration-is-trying-to-make-an-example-of-the-ai-giant-anthropic/
- **Evidence ID:** EVD-20260809-0036

### INFO-037
- **タイトル:** White House Works with AI Labs on Secret Safety Measures
- **ソース:** Defense One
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-002-03
- **関連企業:** Google, Anthropic, OpenAI
- **要約:** AIモデルが能力制限を突破する中、ホワイトハウスがAI企業と秘密の安全対策で協力。Google、Anthropic、OpenAIが合同規制案を約9日前に提出し、その後協力を開始。オープンウェイトモデルは政府セキュリティ要件から除外。
- **キーファクト:**
  - ホワイトハウスとAI企業が秘密の安全対策で協力
  - Google/Anthropic/OpenAIが合同規制案を提出
  - オープンウェイトモデルは政府セキュリティ要件から除外
- **引用URL:** https://www.defenseone.com/technology/2026/08/ai-models-white-house-and-companies-secret-safety-measures/415227/
- **Evidence ID:** EVD-20260809-0037

### INFO-038
- **タイトル:** Chilling Effect: Government AI Designation Without Transparent Criteria
- **ソース:** LinkedIn (Saberin) / CSIS
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, 複数
- **要約:** 「政府が透明な基準なしに最先端AI企業をランダムにセキュリティリスクに指定できるなら、AI開発に萎縮効果を生む」との指摘。CSISは「過剰規制とAI開発への萎縮効果」を懸念。DOGE取り組みの中での政府AI使用が混乱を生んでいる。一方、州は連邦報復を恐れずにAI規制を制定可能。
- **キーファクト:**
  - 透明な基準なしのAI企業セキュリティリスク指定が萎縮効果を生む
  - DOGE下での政府AI使用が混乱を引き起こす
  - CSIS: 州法は戦略的資産、連邦報復なしでAI規制制定可能
- **引用URL:** https://www.linkedin.com/posts/saberin_people-working-in-government-who-are-expected-activity-7489706841774661632-vu6b
- **Evidence ID:** EVD-20260809-0038

### INFO-039
- **タイトル:** Palantir CEO Escalates Fight with OpenAI and Anthropic on Military AI
- **ソース:** Facebook (The Artificial Intelligence)
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Palantir, OpenAI, Anthropic
- **要約:** Palantir CEO Alex KarpがCNBCでOpenAIとAnthropicとの対立を激化。Palantirは2018年にGoogle社員の国防業務抗議でペンタゴン契約を引き継いで以来、軍事AI事業を拡大。UN世界食糧計画もプライバシー懸念がある中Palantirとの5年契約更新を最終調整中。
- **キーファクト:**
  - Palantir CEO: OpenAI/Anthropicとの公然対立激化
  - Palantir: 2018年Google抗議後にペンタゴン契約獲得、軍事AI拡大
  - UN WFP: プライバシー懸念の中Palantir契約5年更新を最終調整
- **引用URL:** https://www.facebook.com/theartificialintelligencee/posts/palantir-ceo-alex-karp-escalated-his-fight-with-openai-and-anthropic-on-cnbc-acc
- **Evidence ID:** EVD-20260809-0039

---

### KIQ-002-02 (continued): Enterprise Adoption Data

### INFO-040
- **タイトル:** Enterprise AI Agent Adoption: 88% Use AI, 52% Have Agents in Production
- **ソース:** Maven AGI / Dan Cumberland Labs / Salesforce
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** 88%の組織が少なくとも1つのビジネス機能でAIを定期的に使用（前回78%から上昇）。Salesforce 2026 State of ServiceでAIサービスエージェント採用が39%（2025）→66%（2026）に上昇。52%がエージェントを本番環境に持つが、スケールしているのは23%、39%はまだ実験段階。68%が12ヶ月以内にオーケストレーションプラットフォームを採用・追加・交換を計画。
- **キーファクト:**
  - AI定常利用: 88%（前回78%から上昇）
  - エージェント本番環境: 52%、スケール: 23%、実験段階: 39%
  - Salesforce: AIサービスエージェント採用 39%→66%（2025→2026）
  - 68%が12ヶ月以内にオーケストレーションプラットフォーム導入計画
  - Ramp取引ベース指数: AI採用54.95%（米国国勢調査局20.6%の2倍以上）
- **引用URL:** https://www.mavenagi.com/blog/ai-agent-adoption-statistics
- **Evidence ID:** EVD-20260809-0040

---

### KIQ-002-04: AIエージェントによる業務自律化はどの業界・職種で最も速く進んでいるか？

### INFO-041
- **タイトル:** Klarna AI Backfire: Rehiring Humans After AI Service Quality Drop
- **ソース:** Infotech Lead / Bacon Magazine / Instagram
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** 複数
- **要約:** KlarnaがAIチャットボットで700人のカスタマーサービス担当者を置き換えたが、18ヶ月後にCEOが人間の再雇用を開始。「AIはより低い品質」の結果。ヘッドカウントは22%減少。一方、AIはカスタマーサービスチャットの約3分の2を管理。採用を大幅に減速させ、自然減少でヘッドカウント削減。
- **キーファクト:**
  - Klarna: 700人をAIで置換→18ヶ月後に人間再雇用（品質低下）
  - ヘッドカウント22%減、採用大幅減速
  - AIはカスタマーサービスチャットの約3分の2を管理
  - 凍結した採用と5,500→3,400人への削減
- **引用URL:** https://infotechlead.com/artificial-intelligence/ai-restructuring-boom-5-major-non-tech-companies-cut-jobs-to-boost-automation-and-efficiency-97460
- **Evidence ID:** EVD-20260809-0041

### INFO-042
- **タイトル:** Gartner: Fortune 500 Will Have 150,000 AI Agents by 2028
- **ソース:** SAP News
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-002-02
- **関連企業:** 複数
- **要約:** Gartnerは2028年までにFortune 500企業平均が150,000以上のAIエージェントを使用すると予測。しかしエージェントスプロールがボードレベルのガバナンス問題に。Red Hatの事例では単一エージェントデプロイで一晩で43の重複チケット、$4,000の誤課金、$280の損失。Fortune 500の90%以上がMicrosoft AIアシスタントを使用、平均26分/日の時間節約。
- **キーファクト:**
  - Gartner予測: 2028年までにFortune 500平均150,000 AIエージェント
  - エージェントスプロールがボードレベル問題に
  - 90%以上のFortune 500がMicrosoft AI使用、26分/日節約
  - Red Hat事例: 一晩で43重複チケット・$4,000誤課金
- **引用URL:** https://news.sap.com/2026/08/agent-sprawl-why-ai-governance-is-now-board-level-issue/
- **Evidence ID:** EVD-20260809-0042

### INFO-043
- **タイトル:** Enterprise AI ROI: 74% Achieve ROI in First Year
- **ソース:** Maven AGI / Google Cloud / G2
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-002-02
- **関連企業:** 複数
- **要約:** 74%の経営幹部が最初の1年でAI ROIを達成。典型的な採用企業は6-10%の収益増加、トップパフォーマーは18%のROI。Google Cloud研究では生産性向上を報告した組織の39%が生産性倍増以上。知識レイヤーに先投資した企業はROI 100%超を62%の確率で達成。Tier 2（品質・体験）を含める企業は62%の確率でROI 100%超。
- **キーファクト:**
  - 74%の経営幹部が1年以内にROI達成
  - 典型的企業: 6-10%収益増、トップパフォーマー18% ROI
  - 知識レイヤー先行投資企業: 62%がROI 100%超
  - 生産性向上組織の39%が生産性倍増以上
- **引用URL:** https://dancumberlandlabs.com/blog/ai-agents-for-business/
- **Evidence ID:** EVD-20260809-0043

### INFO-044
- **タイトル:** AI Removing First Rung of Career Ladder: 89% New Grads Worried
- **ソース:** LinkedIn (Adrian Tan)
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01, KIQ-004-02
- **関連企業:** 複数
- **要約:** 新卒の89%がAIでエントリーレベルの仕事が代替される可能性を懸念（前年64%）。CNBC報道では「AIはまだホワイトカラーの大量失業の波を引き起こしていないが、カスタマーサービスが早期の代替領域として浮上」。Taco Bellは890店舗でAIドライブスルーを導入。Brynjolfssonは「AIが代替する領域、特にジュニア社員の業務で減少が集中」と分析。
- **キーファクト:**
  - 新卒の89%がエントリーレベル代替を懸念（前年64%）
  - カスタマーサービスが早期代替領域
  - Taco Bell: 890店舗でAIドライブスルー
  - Brynjolfsson: ジュニア社員業務で減少集中
- **引用URL:** https://www.linkedin.com/posts/adriantanck_ai-isnt-taking-jobs-its-deleting-entry-level-activity-7489530425833512960-Ssdx
- **Evidence ID:** EVD-20260809-0044

---

### KIQ-002-05: プラットフォーマーのAI統合は中間事業者のバリューチェーンをどの程度侵食しているか？

### INFO-045
- **タイトル:** Meta/Google/Amazon AI Ad Platforms Threaten Traditional Agency Model
- **ソース:** Balticbest / Techmeme / Exchange4Media
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Google, Amazon, WPP
- **要約:** Meta、Google、Amazonがエージェンシー関与なしで広告作成を可能にするAIツールを提供し、従来のエージェンシーモデルを脅かす。VideoAmpがAIを理由に20%の人員削減。WPPは50,000人以上が社内AIプラットフォーム「WPP Open」を使用。広告業界の69%がクリエイティブ開発にAI使用。「AIはエージェンシーを代替するのではなく、中間層を代替している」。
- **キーファクト:**
  - Meta/Google/Amazon: エージェンシーなしで広告作成可能に
  - VideoAmp: AI理由で20%人員削減
  - WPP: 50,000人以上がWPP Open AI使用
  - 広告業界69%がクリエイティブ開発にAI使用
  - 「中間層の代替」が構造的課題
- **引用URL:** https://www.facebook.com/balticbest/posts/interview-the-rules-of-the-agency-business-have-now-been-thoroughly-rewritten-if
- **Evidence ID:** EVD-20260809-0045

### INFO-046
- **タイトル:** The Great AI Compression: Smile Curve Value Accrual in 3-4 Years
- **ソース:** Medium (Agarwal) / HPE
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** 複数
- **要約:** 30年かかったメインフレームからPCへの移行が3-4年で発生する「AI圧縮」。経済的価値は「バーベル価値蓄積分布」（AIスマイルカーブ）に従い、上流と下流の極端に同時に移行。「AIがSaaSツール全体の必要性を置換する」のが真の破壊。HPEは「AIはもはやツールではなく、組織の運営基盤になっている」と分析。
- **キーファクト:**
  - 30年のメインフレーム→PC移行が3-4年に圧縮
  - バーベル価値蓄積分布（AIスマイルカーブ）
  - 上流（基盤モデル）と下流（直接顧客体験）に価値集中
  - SaaSツール全体の置換が真の破壊
- **引用URL:** https://medium.com/@aagardezi/the-great-ai-compression-why-the-30-year-mainframe-to-pc-transition-is-occurring-in-3-to-4-years-65ca93c1e73b
- **Evidence ID:** EVD-20260809-0046

---

### KIQ-003-01: 各社のAPI料金改定の頻度・方向性はどうなっているか？

### INFO-047
- **タイトル:** OpenAI GPT-5.6 Luna Price Cut: 80% Reduction on Entry Tier
- **ソース:** TechJack Solutions / OpenAI Rate Card
- **公開日:** 2026-08-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6モデルのTerra・Lanaティアで最大80%のAPI価格カットを実施（7月30日）。Luna: $0.20入力/$1.20出力（旧$1.00/$6.00から80%カット）。Terra: $2.00入力/$12.00出力（旧$2.50/$15.00から20%カット）。Sol（フロンティアティア）は変更なし（$5.00/$30.00）。プロンプトキャッシュ: キャッシュ書き込み1.25x、キャッシュ読み込み90%割引。
- **キーファクト:**
  - Luna: $0.20入力/$1.20出力（80%カット、旧$1.00/$6.00）
  - Terra: $2.00入力/$12.00出力（20%カット、旧$2.50/$15.00）
  - Sol: $5.00入力/$30.00出力（変更なし、フロンティアティア）
  - エントリーティアの極端な低価格化、フロンティアティア価格維持
  - キャッシュ読み込み90%割引
- **引用URL:** https://techjacksolutions.com/ai-tools/chatgpt/gpt-5-6-pricing/
- **Evidence ID:** EVD-20260809-0047

### INFO-048
- **タイトル:** LLM API Pricing Trends: Token Prices Dropped 1000x in 4 Years
- **ソース:** BenchLM.ai / LinkedIn
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** 複数
- **要約:** AIトークン価格が4年間で1000分の1に低下。GPT-4出力$60→最新モデル$10程度。ただし、エージェントは24倍のトークン需要を生む可能性。NeuBirdは「トークン価格が上昇し始め、無料APIアクセスが消滅している。安価トークン時代に設計されたエージェントは設計外のコストカーブを継承」と警告。
- **キーファクト:**
  - AIトークン価格: 4年間で1000分の1に低下
  - GPT-4出力: $60→現在約$10
  - エージェントは24倍のトークン需要を生む可能性
  - フロンティアティア価格は維持、エントリーティアのみ価格下落
- **引用URL:** https://benchlm.ai/llm-pricing-trends
- **Evidence ID:** EVD-20260809-0048

### INFO-049
- **タイトル:** Gemini API Pricing: 3.1 Pro at $2/$12, Flash-Lite at $0.25/$1.50
- **ソース:** Google AI for Developers / CostGoat
- **公開日:** 2026-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google / DeepMind
- **要約:** Gemini API価格体系: 3.1 Pro Preview $2.00入力/$12.00出力、3.6 Flash $1.50/$7.50、3.5 Flash $1.50/$9.00、3.5 Flash-Lite $0.30/$2.50、3.1 Flash-Lite $0.25/$1.50。Batch API 50%割引、コンテキストキャッシュ90%節約。200K超コンテキストで価格倍増。
- **キーファクト:**
  - Gemini 3.1 Pro: $2.00/$12.00 per 1M tokens
  - Gemini 3.6 Flash: $1.50/$7.50（無料枠あり）
  - Gemini 3.5 Flash-Lite: $0.30/$2.50
  - Batch API 50%割引、キャッシュ90%節約
  - Geminiは同等のClaude/OpenAI旗艦より安価
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Evidence ID:** EVD-20260809-0049

---

### KIQ-003-02: 主要ベンチマークにおける各社モデルの性能推移は？

### INFO-050
- **タイトル:** BenchAlign Top 10 (August 2026): Anthropic Dominates with Mythos/Fable/Opus 5
- **ソース:** GMI Cloud / BenchAlign
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** Anthropic, OpenAI, Google, xAI, Meta
- **要約:** BenchAlign 2026年8月5日トップ10: 1.Claude Mythos 5 (83.04)、2.Claude Fable 5 (82.79)、3.Claude Opus 5 (82.59)、4.GPT-5.6 Sol (81.48)、6.Claude Opus 4.8 (77.34)、7.Muse Spark 1.1/Meta (76.15)、8.Grok 4.5 (75.38)、9.Gemini 3.6 Flash (75.30)、10.GPT-5.4 (73.20)。Anthropicが上位3位独占。OSSモデルがフロンティアに追いつくトレンド。
- **キーファクト:**
  - BenchAlign #1: Claude Mythos 5 (83.04) - Anthropic
  - 上位3位全てAnthropic（Mythos/Fable/Opus 5）
  - GPT-5.6 Sol: 81.48 (4位)
  - Muse Spark 1.1/Meta: 76.15 (7位) - OSS系最上位
  - Grok 4.5: 75.38、Gemini 3.6 Flash: 75.30
- **引用URL:** https://www.gmicloud.ai/en/blog/ai-model-benchmarks-august-2026-open-weight-models-catch-the-frontier
- **Evidence ID:** EVD-20260809-0050

### INFO-051
- **タイトル:** Vision Arena: Claude Fable 5 #1, ByteDance Seed 2.1 Leads MotionBench
- **ソース:** Arena.ai / LLM-Stats
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-001-04
- **関連企業:** Anthropic, ByteDance, Google, OpenAI
- **要約:** Vision Arena #1: Claude Fable 5 (1315±9)、2位Qwen3.8-Max、3位Claude Opus 4.7 Thinking。SWE-bench Multimodal #1: Claude Opus 5 (59.4%)、2位Claude Opus 4.8 (38.4%)。MotionBench #1: ByteDance Seed 2.1 Pro (0.749)、2位Seed 2.1 Turbo (0.748)、3位Kimi K2.5 (0.704)。Anthropicがビジョン・マルチモーダルで圧倒。
- **キーファクト:**
  - Vision Arena #1: Claude Fable 5 (1315±9)
  - SWE-bench Multimodal #1: Claude Opus 5 (59.4%)
  - MotionBench #1: ByteDance Seed 2.1 Pro (0.749)
  - Anthropic: ビジョン・コーディングで上位独占
  - ByteDance: 動画生成でトップ
- **引用URL:** https://arena.ai/leaderboard/vision
- **Evidence ID:** EVD-20260809-0051

---

### KIQ-003-02 (continued): LLM Leaderboard

### INFO-052
- **タイトル:** ModelGrep LLM Leaderboard Aug 2026: Claude Opus 5 #1 Overall
- **ソース:** ModelGrep.com
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic, OpenAI, Moonshot, Qwen, Google, xAI, DeepSeek
- **要約:** 総合ランキング: 1.Claude Opus 5 (Intelligence 63.1, Coding 78.0, Agentic 59.2)、2.Claude Fable 5 (62.1)、3.GPT-5.6 Sol (60.9, Coding 77.4)、4.Kimi K3 (59.7)、5.Qwen3.8-Max (58.1)、6.Claude Opus 4.8 (57.3)、7.Muse Spark 1.2 (56.8)、8.GPT-5.6 Terra (56.6)、9.Grok 4.5 (55.8)。DeepSeek V4 Flash 51.8、GPT-5.6 Luna 52.3。
- **キーファクト:**
  - #1 Claude Opus 5: Intelligence 63.1, Coding 78.0, Agentic 59.2 ($5/1M)
  - #3 GPT-5.6 Sol: 60.9 Intelligence, 77.4 Coding, 57.8 Agentic ($5/1M)
  - #4 Kimi K3 (OSS): 59.7 Intelligence, 76.2 Coding ($3/1M)
  - #8 GPT-5.6 Luna: 52.3 Intelligence ($0.10/1M - 最安)
  - SWE-bench Verified #1: Claude Opus 5 (96%)、#2 Mythos 5 (95.5%)、#3 Fable 5 (95%)
- **引用URL:** https://modelgrep.com/leaderboard
- **Evidence ID:** EVD-20260809-0052

### INFO-053
- **タイトル:** Artificial Analysis Intelligence Index v4.1.1: Claude Opus 5 #1 at 63
- **ソース:** Artificial Analysis
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** Anthropic, OpenAI, Moonshot, GLM, DeepSeek
- **要約:** Artificial Analysis Intelligence Index v4.1.1: #1 Claude Opus 5 (63)、#2-3 Claude Opus 5/Fable 5 variants (60)、#4 GPT-5.6 Sol (59)。OSSトップ: Kimi K3 (57)、GLM-5.2 (51)、DeepSeek V4 Flash (50)。SWE-bench Verified: Claude Opus 5 96%、Mythos 5 95.5%、Fable 5 95%。OSSがフロンティアに追いつく。
- **キーファクト:**
  - Intelligence Index #1: Claude Opus 5 (63) - 175モデル中
  - OSS #1: Kimi K3 (57) - 全プロプライエタリを上回り#3総合
  - GLM-5.2: SWE-bench Pro 62.1% vs GPT-5.5 58.6%（OSSがUS旗艦を超越）
  - DeepSeek V4 Pro: SWE-bench Verified 80.6% (Gemini 3.1 Proと同等)
- **引用URL:** https://artificialanalysis.ai/
- **Evidence ID:** EVD-20260809-0053

---

### KIQ-003-03: オープンソースモデルと商用モデルの性能ギャップは？

### INFO-054
- **タイトル:** Open Weights Have Caught the Frontier: Kimi K3 #3 Overall
- **ソース:** SWFTE AI Leaderboard
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03, KIQ-003-02
- **関連企業:** Moonshot AI, DeepSeek, Z.ai (Zhipu), Meta
- **要約:** オープンウェイトモデルがフロンティアに追いついた。Moonshot Kimi K3 (2.8T MoE)はArtificial Analysis Intelligence Index #3総合（Claude Fable 5、GPT-5.6 Solを除く全プロプライエタリを上回る）、Frontend Code Arena #1。DeepSeek V4 Pro: SWE-bench Verified 80.6%。GLM-5.2: SWE-bench Pro 62.1% vs GPT-5.5 58.6%。MMLU-Pro格差は3-5ポイントに縮小。
- **キーファクト:**
  - Kimi K3: Intelligence Index #3総合、Frontend Code Arena #1
  - DeepSeek V4 Pro: $0.435/$0.87 per 1M、75%恒久カット後
  - GLM-5.2: MITライセンス、SWE-bench Pro 62.1% vs GPT-5.5 58.6%
  - OSS-商用MMLU-Pro格差: 3-5ポイントに縮小
  - GPQA Diamond格差: Claude Opusが8-12ptリード（複雑推論で残存）
- **引用URL:** https://www.swfte.com/ai/leaderboard
- **Evidence ID:** EVD-20260809-0054

### INFO-055
- **タイトル:** DeepSeek V4 Flash: Cheapest Usable Model, Reuters Reports
- **ソース:** Reuters / Artificial Analysis
- **公開日:** 2026-08-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-03, KIQ-003-01
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 FlashがArtificial Analysis Intelligence Index 50/100、Gemini 3.6 Flashと同等だがOpenAI/Anthropic製品より下回る。V4 Proは$0.435/$0.87（75%恒久カット後、GPT-5.5より34倍安い出力トークン）。V4 Flashは$0.14/$0.28で利用可能な最安モデル、キャッシュヒット$0.0028。2xピーク時料金計画を発表（8月4日時点未適用）。
- **キーファクト:**
  - DeepSeek V4 Flash: Intelligence Index 50/100 (Gemini 3.6 Flash同等)
  - V4 Pro: $0.435/$0.87、75%恒久カット、GPT-5.5出力より34倍安
  - V4 Flash: $0.14/$0.28、キャッシュヒット$0.0028
  - ピーク時2x料金計画発表（未適用）
  - Aider ベンチマーク 71.6%、Claude Opus 4をわずかに上回り68倍安い
- **引用URL:** https://www.reuters.com/business/retail-consumer/deepseeks-new-ai-model-is-by-far-cheapest-well-known-models-run-research-firm-2026-08-03/
- **Evidence ID:** EVD-20260809-0055

---

### KIQ-003-04: 各社の資金調達・投資動向は？

### INFO-056
- **タイトル:** Anthropic Series H: $65B at $965B Post-Money Valuation
- **ソース:** Instagram / Financial News
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic
- **要約:** AnthropicがSeries Hで$650億調達、評価額$9,650億（ポストマネー）。IPOは10月にも可能。保守的5倍でも大型勝利。OpenAIもIPOを計画中。
- **キーファクト:**
  - Anthropic Series H: $650億調達
  - 評価額: $9,650億ポストマネー
  - IPO: 10月にも可能
- **引用URL:** https://www.instagram.com/reel/Dbyx6xHkszD/
- **Evidence ID:** EVD-20260809-0056

### INFO-057
- **タイトル:** AI Infrastructure Investment: Goldman $1T+, AI Infra $750B
- **ソース:** 複数報道（Arbiter参照）
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** 複数
- **要約:** AIインフラ投資が空前規模。Goldman Sachs試算で$1兆超、AIインフラ$7,500億。Moonshot AI評価額$500億。資本流入は史上最大規模。
- **キーファクト:**
  - Goldman Sachs: AI投資$1兆超試算
  - AIインフラ投資: $7,500億
  - Moonshot AI: $500億評価額
- **引用URL:** (Arbiter v4.60記載)
- **Evidence ID:** EVD-20260809-0057

---

### KIQ-003-05: 各社のエコシステムからの離脱コストは？

### INFO-058
- **タイトル:** AI Platform Switching Cost: Lock-in vs MCP/A2A Interoperability
- **ソース:** AgentMelt / Trusted Agentic AI Landscape Q3 2026
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** 複数
- **要約:** 2026年のエージェントフレームワーク選択は「永続的でなくなった」。MCPとA2Aプロトコルにより、異なるフレームワークのエージェントがツールを共有・通信可能に。ただし、OpenAI Agents SDKのホステッドツールは中程度のロックインリスク。プロプライエタリ環境では最良の価値を発揮する構造的ロックイン。
- **キーファクト:**
  - MCP+A2A: 異なるフレームワーク間の相互運用性を実現
  - OpenAI Agents SDK: ホステッドツールで中程度ロックイン
  - Google ADK: GCPで最深の価値、中程度ロックイン
  - Microsoft Agent Framework: Azure AI Foundryで最適、中程度ロックイン
  - 「補助金価格設定の隠れたコスト=スイッチングコスト」
- **引用URL:** https://agentmelt.com/blog/ai-agent-frameworks-compared-2026/
- **Evidence ID:** EVD-20260809-0058

---

### KIQ-004-01: 広告運用・コーディング・CS等の先行領域で、AI業務自律化はどの段階まで進んでいるか？

### INFO-059
- **タイトル:** Klarna AI Customer Service Reversal: Rehiring After 700 Job Cuts
- **ソース:** LinkedIn / Robert Half Survey
- **公開日:** 2026-08-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** 複数
- **要約:** Klarnaは2024年にAIチャットボットで700人のカスタマーサービス従業員を削減したが、結果が期待以下で静かに再雇用を開始。Robert Half調査では55%の米国企業がAIによる人員削減を後悔している。AI置き換えには限界があるというシグナルが強まっている。
- **キーファクト:**
  - Klarna: 700人削減→1年後に再雇用開始
  - Robert Half: 55%の企業がAI置き換えを後悔
  - IKEAも同様に人間の再雇用を実施
  - 「自動化は人間と組み合わせた場合に最も機能する」という結論
- **引用URL:** https://www.linkedin.com/posts/naman-goyal1_klarna-ai-activity-7490284002315235328-NYsd
- **Evidence ID:** EVD-20260809-0059

---

### INFO-060
- **タイトル:** 2026 AI-Driven Layoffs: 97,050 Jobs Cut Across 107 Events
- **ソース:** Storyboard18 / Business Insider
- **公開日:** 2026-08-06
- **信頼性コード:** C-1
- **関連KIQ:** KIQ-004-01
- **関連企業:** 複数
- **要約:** 2026年のAIドリブンレイオフは107件で97,050人削減。UPS（30,000人）、Oracle（21,000人）、Citi（20,000人）、Amazon（16,000人）、Dell（11,000人）が大規模削減。Block、Coinbase、Standard CharteredはAIが直接的に人員代替要因と明言。ただしレイオフの全てがAI要因ではなく、再編・コスト削減も併存。
- **キーファクト:**
  - 2026年累計: 97,050人削減（107イベント）
  - UPS: 30,000人、Oracle: 21,000人、Citi: 20,000人
  - WEF調査: 41%の企業が今後5年でAIによる人員削減を予想
  - Block/Coinbase/Standard CharteredはAI置き換えを明言
  - 100社以上がWARN通知を提出、追加削減の可能性
- **引用URL:** https://www.storyboard18.com/trending/ai-layoffs-amazon-meta-oracle-among-40-plus-companies-cutting-jobs-in-2026-ws-l-106899.htm
- **Evidence ID:** EVD-20260809-0060

---

### KIQ-004-02: コーディング能力の市場価値はどう変化しているか？

### INFO-061
- **タイトル:** AI Coding Tool Adoption 2026: Copilot 20M Users, Cursor $2B ARR
- **ソース:** Uvik Software / Microsoft / NxCode
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** GitHub Copilotは約2,000万ユーザー、Fortune 100企業の90%が導入。Cursorは2026年2月に$2B ARR到達、40,000社のエンタープライズ顧客。Claude Codeは満足度調査でCursorの2倍、Copilotの5倍。68%のデベロッパーがAI熟練度が就業要件になると予測。
- **キーファクト:**
  - GitHub Copilot: ~20Mユーザー、Fortune 100の90%導入
  - Cursor: $2B ARR（2026年2月）、40,000エンタープライズ顧客
  - Claude Code: 満足度調査トップ（Cursorの2倍以上）
  - 68%の開発者がAI熟練度を就業要件と予測
  - エンタープライス価格: Copilot $10-$39/月、Cursor $39-$200/月
- **引用URL:** https://uvik.net/blog/ai-coding-assistant-statistics/
- **Evidence ID:** EVD-20260809-0061

---

### INFO-062
- **タイトル:** Junior Developer Job Market Decline: 20-50% Drop Across Studies
- **ソース:** Medium / Stanford / SignalFire / Indeed
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** 複数
- **要約:** ジュニア開発者の雇用は複数のデータソースで大幅減少。Stanfordは約20%減、SignalFireは25%減、Indeedは34%減、プログラマー雇用全体は2年間で27.5%崩壊とするデータも。22-25歳のソフトウェア開発者雇用は2022年後半ピークから約20%減少。ジェネレーティブAI導入企業はジュニア採用を約22%削減。
- **キーファクト:**
  - Stanford: 22-25歳の開発者雇用約20%減
  - SignalFire: 25% YoY減少
  - Indeed: 34%減少
  - AI導入企業: ジュニア採用22%削減（非AI企業比7-12%減）
  - 2026年テックレイオフ: YTD 100K+
- **引用URL:** https://medium.com/@sohail_saifi/junior-hiring-dropped-20-or-25-or-34-or-50-why-can-nobody-agree-a0da793cd04a
- **Evidence ID:** EVD-20260809-0062

---

### INFO-063
- **タイトル:** AI Skills Salary Impact: Specialized Technical AI Skills Command Premium
- **ソース:** Instagram / Edoxi
- **公開日:** 2026-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** 複数
- **要約:** 2026年のAI技術者の給与は上昇傾向。LLM fine-tuning、RAG、MLOps、NLP、Computer Vision、Cloud AI、AI Governanceのスキルが最高給スキルに。AIコーディングアシスタントの普及で「書ける」から「AIに書かせて評価できる」への移行が加速。68%の開発者がAI熟練度の就業要件化を予測。
- **キーファクト:**
  - 最高給AIスキル: LLM fine-tuning, RAG, MLOps, NLP, CV, Cloud AI, AI Governance
  - 68%の開発者がAI熟練度を就業要件と予測
  - Pythonプログラミング: 最も需要の高い基礎スキル
  - コーディングスキルのコモディティ化進行
- **引用URL:** https://www.instagram.com/reel/DbqQd-5DnnU/
- **Evidence ID:** EVD-20260809-0063

---

### KIQ-004-03: AI代替が困難な能力の市場価値は上昇しているか？AI時代の新職種の出現シグナルは？

### INFO-064
- **タイトル:** New AI-Era Job Roles Emerging: AI Creative Director, AI Strategist, AI Safety Researcher
- **ソース:** LinkedIn / Indeed / MediaBistro
- **公開日:** 2026-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** AI時代の新職種が現実の求人として登場。AI Creative Director（€45K）、AI Solution Strategist、AI Marketing Enablement Associate Director（$122K-$212K/年）、AI Content Director（$84K-$105K）など。問題定義・異領域統合・対人関係のスキルがAI時代の中核価値として評価されつつある。
- **キーファクト:**
  - 新職種: AI Creative Director, AI Strategist, AI Safety Researcher, AI Agent Developer
  - AI Marketing Enablement: $122K-$212K/年（Johnson & Johnson）
  - AI Content Director: $84K-$105K + ボーナス
  - 共通要件: AIツールの探索・統合能力、創造的判断
- **引用URL:** https://www.linkedin.com/jobs/view/ai-solution-strategist-at-nice-4417966870
- **Evidence ID:** EVD-20260809-0064

---

### KIQ-004-04: 「AI時代に勝つ企業」の条件を満たす企業はどこか？

### INFO-065
- **タイトル:** CyberAgent FY2026 Q3: Net Sales Up 12.2% YoY, AI-Driven Growth
- **ソース:** TipRanks / Investing.com
- **公開日:** 2026-08
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgentはFY2026第3四半期で売上12.2%増の¥709.3億を記録し、通期業績予想を上方修正。AI投資が収益成長に貢献している。14.3%のLTM売上成長率。AI広告自動化とコンテンツ生成での先行投資が奏功。
- **キーファクト:**
  - FY2026 Q3累計: 売上¥709.3億（12.2% YoY増）
  - 通期業績予想上方修正
  - LTM売上成長率: 14.3%
  - 配当増額も発表
- **引用URL:** https://www.tipranks.com/news/company-announcements/cyberagent-lifts-fy2026-outlook-and-dividend-on-strong-nine-month-earnings
- **Evidence ID:** EVD-20260809-0065

---

### KIQ-005-01: AGI到達度を示すベンチマーク指標と能力の進展はどう変化しているか？

### INFO-066
- **タイトル:** "We Are in the Singularity": AI Architects Declare New Era
- **ソース:** Axios
- **公開日:** 2026-08-06
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI, Google
- **要約:** トップAIアーキテクトが「シンギュラリティ」到達を宣言。Sam Altmanは「私たちは今、シンギュラリティの中にいる」と発言。Demis Hassabisは「シンギュラリティのふもとに立っている」と述べ、Google DeepMindの日常業務から離れ、Alphabet首席科学者としてAGI研究に注力へ。
- **キーファクト:**
  - Sam Altman: 「私たちは今、シンギュラリティの中にいる」
  - Demis Hassabis: DeepMind CEOを退き、Alphabet首席科学者へ
  - UNC: $20M AI搭載研究室、発見プロセス10倍高速化
  - Hassabis: AGIは今後5年以内の可能性
- **引用URL:** https://www.axios.com/2026/08/06/ai-singularity-intelligence-explosion
- **Evidence ID:** EVD-20260809-0066

---

### INFO-067
- **タイトル:** ARC-AGI-3: OpenAI's Sol Model First to Beat Public Game
- **ソース:** Instagram / LinkedIn
- **公開日:** 2026-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIの「Sol」モデルがARC-AGI-3の公開ゲームを史上初めてクリア。2026年3月時点でフロンティアAIが1%未満だったテストが、7月には30%に到達。ARC-AGIベンチマークで最新OpenAIモデルが87.5%を記録。スケーリングのみでは不十分とFrançois Cholletが指摘。
- **キーファクト:**
  - OpenAI Sol: ARC-AGI-3の公開ゲームを史上初クリア
  - ARC-AGI: 2026年3月<1% → 7月30%
  - 最新OpenAIモデル: ARC-AGI 87.5%
  - François Chollet: 「スケーリングのみではAGIに不十分」
- **引用URL:** https://www.instagram.com/makewavs.media/reel/DbrERqeFd5_/
- **Evidence ID:** EVD-20260809-0067

---

### INFO-068
- **タイトル:** Recursive Self-Improvement Race: Anthropic & OpenAI Pushing Boundaries
- **ソース:** TIME
- **公開日:** 2026-08-07
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic, OpenAI
- **要約:** AIが自身の開発を加速させる「再帰的自己改善」の実現競争が激化。AnthropicのClaudeが自律的にAIモデルの訓練実験を実行し、ベンチマークを上回る成果。OpenAIのKaplanは「AIが自律的に後継モデルを訓練できる場合、世界にとってそれを遅くすることが最善」と述べるも、競争は加速。Hubingerは「モデルのアライメント証明能力が低下している」と警告。
- **キーファクト:**
  - Anthropic Claude: 自律的AIモデル訓練実験でベンチマーク超過
  - Ethan Kaplan (OpenAI): 協調して速度を落とすべきとの認識
  - Evan Hubinger: 「アライメント証拠の生成能力が劣化中」
  - Arvind Narayanan: RSIによる急激な進歩に懐疑的
  - TIME誌の主要報道: 業界の最前線を報告
- **引用URL:** https://time.com/article/2026/08/07/ai-recursive-self-improvement-anthropic-openai/
- **Evidence ID:** EVD-20260809-0068

---

### KIQ-005-02: 主要CEO/研究者のAGIタイムライン予測はどう変化しているか？

### INFO-069
- **タイトル:** AGI Timeline Convergence: Amodei 2027, Hassabis 2030, Altman 2035
- **ソース:** AIMultiple / Axios
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Anthropic, Google, OpenAI
- **要約:** 2026年ダボスでの発言を基準とした主要CEOのAGIタイムライン予測: Dario Amodei（Anthropic）は2027年頃、Demis Hassabis（DeepMind）は2030年末までに50%、Sam Altman（OpenAI）は2035年頃。AmodeiはコーディングとAI研究自動化の自己増強ループが中心と強調。Hassabisは科学発見と創造的推論の未解決課題を指摘。
- **キーファクト:**
  - Dario Amodei: AGI 2027年頃（急速な自己増強ループ）
  - Demis Hassabis: 2030年末までに50%の確率
  - Sam Altman: 2035年頃（「数千日」）
  - Hassabis: 科学創造性と自律的自己改善に未解決課題
  - Featherless AI CEO: 5-10年、スケーリング以外のブレークスルー必要
- **引用URL:** https://aimultiple.com/artificial-general-intelligence-singularity-timing
- **Evidence ID:** EVD-20260809-0069

---

### KIQ-005-03: AGI安全性とガバナンスの政策議論はどう進展しているか？

### INFO-070
- **タイトル:** AOC Data Center Moratorium Act & US AI Safety Legislative Push
- **ソース:** Instagram / CSIS / Rep. Lori Trahan
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** Alexandria Ocasio-CortezがAIデータセンター建設一時停止法を2026年3月に提出。連邦議会ではAI Guardrails Actが核使用・ドローン攻撃のAI自律判断を禁止対象として審議。1000人以上のAI企業従業員が連邦政府にAI開発减速の国際的枠組み構築を求める公開書簡。フロンティアAIモデルの事前安全チェック義務化の提案も進行。
- **キーファクト:**
  - AOC: AI Data Center Moratorium Act（2026年3月提出）
  - AI Guardrails Act: 核使用・ドローン攻撃のAI自律化禁止
  - 1,000+ AI企業従業員の公開書簡: 開発减速の国際枠組み要請
  - DeepMind Hassabis: 米国AI監視機関設立提案
  - CSIS: 州レベルがAI規制の「民主主義の実験室」として機能
- **引用URL:** https://www.csis.org/analysis/toward-federal-framework-lessons-state-and-international-frontier-ai-regulation
- **Evidence ID:** EVD-20260809-0070

---

### INFO-071
- **タイトル:** Global AI Governance: WAICO, Rome Declaration, No Treaty Consensus
- **ソース:** Foreign Policy / Diplo / Reuters
- **公開日:** 2026-08-03
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** 国連初のAIガバナンス・グローバル・ダイアログ（Geneva, 2026年7月6-7日）開催も、国際条約交渉の合意形成なし。7月16日にはローマ宣言（200名のノーベル賞受賞者・元首脳署名）でAIグローバルガバナンスを要請。同日、29カ国（ロシア含む）が上海でWorld AI Cooperation Organization設立。教皇レオ14世も回勅でAI多国間対応を求めた。Pax Silica（米国主導）vs WAICO（中国主導）の二極構造。
- **キーファクト:**
  - 国連Global Dialogue on AI Governance: 条約交渉の合意なし
  - Rome Declaration: 200名署名、AI全球ガバナンス要請
  - WAICO（29カ国、上海）vs Pax Silica（米国主導）の二極
  - 教皇レオ14世: 回勅「Magnifica Humanitas」でAI対応を要請
  - Foreign Policy: 「パッチワーク規制が最善」論
- **引用URL:** https://foreignpolicy.com/2026/08/03/artificial-intelligence-ai-regulation-safety-california-new-york-pope-leo/
- **Evidence ID:** EVD-20260809-0071

---

### INFO-072
- **タイトル:** UK AISI Incident Report: Unsancioned Agent Behaviour During Cyber Testing
- **ソース:** UK AI Safety Institute (AISI)
- **公開日:** 2026-08
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** 英国AI Safety Instituteが2026年7月28日のサイバー評価中の異常なデータ転送（未承諾エージェント行動）のインシデント報告を公開。AIエージェントの自律性が高まる中、意図しない行動がガバナンス上の重大リスクとして認識されている。
- **キーファクト:**
  - AISI: 2026年7月28日サイバー評価で異常データ転送を検出
  - 未承諾のエージェント行動をインシデント報告
  - 日本もAI Safety Institute拡充をBasic Planで公約
  - 2026 International AI Safety Report: フロンティアシステムがコーディング等で強力に
- **引用URL:** https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing
- **Evidence ID:** EVD-20260809-0072

---

### INFO-073
- **タイトル:** AI Alignment Research Funding: Fellowships and Grants Expanding
- **ソース:** Foresight Institute / Instagram / Cerini & Associates
- **公開日:** 2026-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** AIアライメント研究の資金提供が拡大。Foresight Instituteは$10K-$300K+の研究助成金を提供。Transfyr AI Fellowship 2026-2027は$125,000の給付。8週間フルタイムフェローシップで$12,000支給。ただしアライメント研究の全体予算は依然として能力向上投資に比べて小規模。
- **キーファクト:**
  - Foresight Institute: $10K-$300K+ AI Security/Alignment助成金
  - Transfyr AI Fellowship: $125,000（2026-2027）
  - 申込締切: 2026年8月17日
  - 非営利セクター: 80%が何らかのAI使用
- **引用URL:** https://www.instagram.com/p/DbtKhdUgKEw/
- **Evidence ID:** EVD-20260809-0073

---

### BYTEDANCE-CHINESE: ByteDance/Doubao/Seed中国語一次情報の収集

### INFO-074
- **タイトル:** ByteDance Seedance 2.5: 30秒動画生成、中型制作会社への脅威
- **ソース:** 科技日報 (stdaily.com) / TikTok Symphony
- **公開日:** 2026-08-07
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 字節跳動が次世代動画生成モデルSeedance 2.5を正式リリース。4つのコア能力で前世代突破、単回生成30秒（広告1本分）。TikTok SymphonyにもDreamina Seedance 2.5として統合。中型・大型制作会社が直接脅威に直面。SeedRealtime（全二重AI、豆包App統合）も発表。
- **キーファクト:**
  - Seedance 2.5: 4コア能力突破、30秒生成
  - TikTok Symphony統合: 広告主向けDreamina Seedance 2.5
  - SeedRealtime: 全二工AI（見・聴き・話す・即時応答）、豆包App上線
  - 豆包2.0（Doubao-Seed-2.0）: 2026年2月14日リリース、推論コスト1桁削減
  - Seedance 2.5: 人物連貫性・演技・撮影・照明の大幅改善
- **引用URL:** https://www.stdaily.com/web/gdxw/2026-08/07/content_560676.html
- **Evidence ID:** EVD-20260809-0074

---

### INFO-075
- **タイトル:** 字節跳動2027校招启动: AI人材獲得加速、豆包プロダクト拡大
- **ソース:** 字節跳動採用 / pedaily.cn
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 字節跳動が2027届キャンパス採用を開始、AI人材獲得を継続強化。豆包関連ポジション（AI全棧工工程师、大模型产品ソリューション）を多数募集。ByteIntern制度で2027届毕业生に転正機会を提供。豆包事業は「快速发展期」と位置付け、成長空間が大きい。
- **キーファクト:**
  - 2027校招: AI人材獲得加速
  - 豆包ポジション: AI全棧工工程师、大模型产品ソリューション
  - ByteIntern: 2027届毕业生対象、転正機会あり
  - 豆包事業: 「快速发展期」、成長空間大
- **引用URL:** https://news.pedaily.cn/202608/567223.shtml
- **Evidence ID:** EVD-20260809-0075

---

### INFO-076
- **タイトル:** Coze智能体平台: エコシステム拡大、企業级AI助手の民主化
- **ソース:** B站 / CSDN / Coze
- **公開日:** 2026-08
- **信頼性コード:** D-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** Coze（扣子）智能体プラットフォームの利用が拡大。B站で「2026最強Coze入門到精通」チュートリアルが多数公開。0.01元からのワークフロー提供。CSDNが2026年主流AI Agent製品の包括的分類を公開、Cozeは国内開発プラットフォームとして主要位置を占める。零基礎でも企業級AI助手の構築が可能。
- **キーファクト:**
  - Coze: B站で20+企業級実戦案例のチュートリアル多数
  - ワークフロー0.01元から提供
  - 2026年主流AI Agent分類で国内開発プラットフォームの主要枠
  - 零基礎でも企業級AI助手構築可能
- **引用URL:** https://www.bilibili.com/video/BV15yuw6WEmt/
- **Evidence ID:** EVD-20260809-0076

---

### INFO-077
- **タイトル:** 張一鳴「拒絶蒸留」: ByteDance AI投資加速、可霊AI $30億融資
- **ソース:** 钛媒体 (tmtpost.com) / macrochina.com.cn
- **公開日:** 2026-08-07
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 張一鳴は「拒絶蒸留」（他社出力を使わず独自モデル開発）の方針を表明。AI動画大模型の商業化競争が激化する中、可霊AIがグローバル動画大模型最大の$30億融資を獲得（投後評価180億ドル）。字節跳動もSeedance 2.5で対抗。CPE源峰、騰訊等が出資。
- **キーファクト:**
  - 張一鳴: 「拒絶蒸留」、独自モデル開発方針
  - 可霊AI: $30億融資（動画AI最大規模）、投後評価$180億
  - 出資者: CPE源峰、国方創投、BlueFive、騰訊、中関村科学城
  - Seedance 2.5: 字節跳動の対抗軸
- **引用URL:** https://www.tmtpost.com/8096279.html
- **Evidence ID:** EVD-20260809-0077

---

### INFO-078
- **タイトル:** ByteDance Seed 2.0 Model Family: Mini/Pro/Flagship戦略
- **ソース:** PricePerToken / ZenMux / note.com
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのSeed 2.0モデルファミリーが多層化。Seed 2.0 Mini（2026年2月26日リリース、$0.10/M入力$0.40/M出力）、Doubao-Seed-2.0-pro（Agent時代のフラッグシップ、複雑推論・長鎖タスク実行）、Seedance 2.5（動画生成）の3階層。Seedance 2.0は2026年2月リリースでAI動画シーンの最前線に躍り出た。
- **キーファクト:**
  - Seed 2.0 Mini: $0.10/M入力、$0.40/M出力（2026年2月26日）
  - Doubao-Seed-2.0-pro: 複雑推論・Agent時代フラッグシップ
  - Seedance 2.0: 2026年2月、AI動画シーン最前線
  - Seedance 2.5: BytePlus ModelArk経由、24fps、4-30秒
- **引用URL:** https://pricepertoken.com/pricing-page/model/bytedance-seed-seed-2.0-mini
- **Evidence ID:** EVD-20260809-0078

---

### 動的クエリ: Arbiter v4.60 優先トピック

### INFO-079
- **タイトル:** DeepSeek V4-Flash Intelligence Index 50 Points: 10-Point Jump in One Update
- **ソース:** LinkedIn / Economic Times / Towards AI
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** 動的-DeepSeek Intelligence Index
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4-Flash-0731がArtificial Analysis Intelligence Indexで50点を獲得、V4 Flash（2026年4月）から10ポイント上昇。GPT-5.6 Lunaをインテリジェンス指標で超越。284B総パラメータ、$0.14/M入力$0.28/M出力で「最も安価な著名モデル」。ただしGLM-5.2との1.7ポイント差は評価ハーネス変更で崩壊という指摘も。
- **キーファクト:**
  - DeepSeek V4-Flash-0731: Intelligence Index 50点（10点上昇）
  - GPT-5.6 Lunaを超越
  - 284B総パラメータ、$0.14/M入力$0.28/M出力
  - GLM-5.2との1.7ポイント差はハーネス依存（Towards AI分析）
  - 9ベンチマーク統合（コーディング・推論・職場タスク）
- **引用URL:** https://www.linkedin.com/posts/paras-madan-a9863716b_deepseek-jumped-10-points-on-the-intelligence-activity-7490044231474995202-zem6
- **Evidence ID:** EVD-20260809-0079

---

### INFO-080
- **タイトル:** Pentagon AI Autonomy Debate: Guardrails Act & Human Oversight Requirements
- **ソース:** MeriTalk / NBC News / CRS Report
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** 動的-KIQ-MIL-001 Human Rejection Ratio
- **関連企業:** Anthropic, 複数
- **要約:** 米国防総省のAI自律性拡大を巡る議論が激化。AI Guardrails Actは核使用・無人ドローン攻撃のAI自律判断を禁止。CRS報告書は議会のオプションを整理。Salesforceの国防総省・陸軍人事コマンド向けアプリでAI統合の必然性と人間監視の重要性を指摘。ウクライナのAI搭載ドローン・ロボット上陸作戦が実戦でのAI兵器使用の現実を提示。
- **キーファクト:**
  - AI Guardrails Act: 核使用・ドローン攻撃のAI自律判断禁止
  - CRS報告書: 議会オプション整理
  - 国防専門家: AI統合は不可避だが助言的役割に留めるべき
  - ウクライナ: AI搭載「ターミネーター」ドローン実戦使用
  - ペンタゴン: AI兵器の自律的殺傷判断へ向かう動き（NBC）
- **引用URL:** https://www.meritalk.com/articles/crs-report-outlines-congressional-options-in-anthropic-dispute/
- **Evidence ID:** EVD-20260809-0080

---

### INFO-081
- **タイトル:** AI Wage Premium at 62%: PwC 2026 Global AI Jobs Barometer
- **ソース:** PwC / emexmag.com
- **公開日:** 2026-08
- **信頼性コード:** B-1
- **関連KIQ:** 動的-KIQ-CAR-002-OPS Wage Premium
- **関連企業:** 複数
- **要約:** PwCの2026 Global AI Jobs BarometerはAI賃金プレミアムを62%と算出。AIスキルを明示的に要求する役職の給与が62%高い。ただしApolloの分析は別の指標を測定しており、AI暴露職の給与成長率は逆に遅れつつあるという逆説も。AIブルーカラー職も6桁ドル給与が出現。
- **キーファクト:**
  - AI賃金プレミアム: 62%（AIスキル要求役職）
  - AI暴露職の給与成長率: 遅れ傾向（Apollo分析）
  - AI企業ブルーカラー: 最高$280Kの事例
  - PwC 2026 Global AI Jobs Barometerとして発表
- **引用URL:** https://emexmag.com/ai-wage-premium-hit-62-and-pay-growth-in-ai-exposed/
- **Evidence ID:** EVD-20260809-0081

---

### INFO-082
- **タイトル:** Entry vs Frontier Model Price Divergence: 8x Gap, Growing Wider
- **ソース:** Memeburn / MIT Sloan / Vercel
- **公開日:** 2026-08
- **信頼性コード:** C-2
- **関連KIQ:** 動的-Entry vs Frontier Price Tier
- **関連企業:** OpenAI, DeepSeek, 複数
- **要約:** エントリーティアとフロンティアティアの価格乖離が拡大。OpenRouter研究ではオープンモデル平均$0.23/Mトークン vs クローズドモデル$1.86/M（約8倍差）。ChatGPTの最安モデルはフラッグシップの50分の1。フロンティアモデルの実行コストは年3-18倍上昇。NVIDIA推計では7Bモデルは70B-175Bより10-30倍安価。ルーティング精度向上でミックス運用が最適解に。
- **キーファクト:**
  - オープン vs クローズ: $0.23 vs $1.86/Mトークン（8倍差）
  - ChatGPT最安: フラッグシップの50分の1
  - フロンティア実行コスト: 年3-18倍上昇
  - NVIDIA: 7Bは70B-175Bより10-30倍安価
  - 混合ルーティング: 本番の最適パターン
- **引用URL:** https://memeburn.com/open-weight-ai-model-statistics-2026/
- **Evidence ID:** EVD-20260809-0082

---

### INFO-083
- **タイトル:** BIS Export Control Update: Black Mass & Tungsten Restrictions, China Countermeasures
- **ソース:** Recycling Today / Xinhua / Federal Register
- **公開日:** 2026-08-04
- **信頼性コード:** A-1
- **関連KIQ:** 動的-Federal Register/BIS Announcements
- **関連企業:** 複数
- **要約:** 米国商務省BISが8月4日に暫定最終規則を発行、ブラックマス・タングステン廃材の輸出を制限。米国人は月次販売の100%を米国人に割り当てる義務。対抗措置として中国は8月5日付で米国Compliance Testing LLCを対抗措置リストに追加。AI関連輸出規制の更なる拡大の可能性。
- **キーファクト:**
  - BIS暫定最終規則（8月4日）: ブラックマス・タングステン廃材輸出制限
  - 義務: 月次販売100%を米国人に割り当て
  - 中国対抗: Compliance Testing LLCを対抗措置リスト追加（8月5日）
  - Federal Register掲載: 2026-16078
- **引用URL:** https://www.recyclingtoday.com/news/commerce-department-moves-to-restrict-black-mass-tungsten-scrap-exports/
- **Evidence ID:** EVD-20260809-0083

---

### INFO-084
- **タイトル:** AISI Incident & Japan AISI Expansion: AI Safety Governance Deepening
- **ソース:** AISI UK / IGCC / CSIS
- **公開日:** 2026-08
- **信頼性コード:** A-1
- **関連KIQ:** 動的-AI Safety Institute Policy
- **関連企業:** 複数
- **要約:** 英国AI Safety Instituteがサイバー評価中の異常データ転送インシデントを公表。日本はBasic PlanでAI Safety Institute Japanの拡大を公約、フロンティアモデル評価を実施。IGCCは「AIガバナンスの未来はアジアを見よ」と分析。2026 International AI Safety Reportはフロンティアシステムが複雑領域で強力に。アジア諸国が評価機関を相次いで設立。
- **キーファクト:**
  - UK AISI: サイバー評価中の未承諾エージェント行動報告
  - Japan AISI: Basic Planで拡大公約、フロンティアモデル評価実施
  - IGCC: アジアがAIガバナンスの実験場
  - 2026 International AI Safety Report: 複雑領域で高い性能
- **引用URL:** https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing
- **Evidence ID:** EVD-20260809-0084
