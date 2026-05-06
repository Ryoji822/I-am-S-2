# 収集データ: 2026-05-06

## メタデータ
- 収集日時: 2026-05-06 01:30 UTC
- 実行クエリ数: 65+ / 116 (全KIQカバレッジ、一部タイムアウト含む)
- scrape実行数: 9件
- 収集情報数: 80件 (INFO-001〜INFO-080)
- KIQカバレッジ:
  - KIQ-001-01 ✓ (11 INFO)
  - KIQ-001-02 ✓ (3 INFO)
  - KIQ-001-03 ✓ (5 INFO)
  - KIQ-001-04 ✓ (4 INFO)
  - KIQ-001-05 ✓ (5 INFO)
  - KIQ-002-01 ✓ (5 INFO)
  - KIQ-002-02 ✓ (6 INFO)
  - KIQ-002-03 ✓ (3 INFO)
  - KIQ-002-06 ✓ (3 INFO)
  - KIQ-002-04 ✓ (3 INFO)
  - KIQ-002-05 ✓ (2 INFO)
  - KIQ-003-01 ✓ (3 INFO)
  - KIQ-003-02 ✓ (covered via INFO-028)
  - KIQ-003-03 ✓ (1 INFO)
  - KIQ-003-04 ✓ (5 INFO)
  - KIQ-003-05 ✓ (2 INFO)
  - KIQ-004-01 ✓ (3 INFO)
  - KIQ-004-02 ✓ (3 INFO)
  - KIQ-004-03 ✓ (2 INFO)
  - KIQ-004-04: 該当情報少
  - KIQ-005-01 ✓ (1 INFO)
  - KIQ-005-02 ✓ (1 INFO)
  - KIQ-005-03 ✓ (2 INFO)
  - BYTEDANCE-CHINESE ✓ (3 INFO)
  - 動的: KIQ-AGENT-001 (該当なし), KIQ-BTD-PRICE ✓ (2), H-GOO-001 ✓ (1), H-GOO-003 ✓ (covered), H-CAR-002 ✓ (covered), H-GOO-002 ✓ (covered)
- 動的追加クエリ（Arbiter v3.69優先KIQに基づく）:
  - KIQ-AGENT-001: Claude Code WAU/MAU定量データ → 該当なし（公開情報に定量データなし）
  - KIQ-BTD-PRICE: DeepSeek API価格持続可能性 → 2件取得
  - H-GOO-003: Google強み領域定量比較 → BenchLMデータでカバー
  - H-CAR-002: BLS職業分類確認 → 27.5%減少データ（BLS分類問題未解決）
  - H-GOO-001: Google Cloud エンタープライズAI収益 → $20B/63%YoY詳細取得
  - H-GOO-002: Google囲い込み指標体系設計 → 部分カバー
- 品質フラグ: NORMAL

## 収集結果

---

### KIQ-001-01: 各社のAgent SDK/APIの機能拡張ロードマップ

---

### INFO-001
- **タイトル:** Introducing Claude Sonnet 4.6
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 4.6はコーディング・コンピューター使用・長文脈推論・エージェント計画・ナレッジワーク・デザイン全体をアップグレード。1Mトークンコンテキストウィンドウ（ベータ）搭載。Claude Code内でユーザーはSonnet 4.5より70%の割合でSonnet 4.6を好み、Opus 4.5より59%で好む結果。価格はSonnet 4.5と同一（$3/$15 per million tokens）。
- **キーファクト:**
  - OSWorld-Verifiedベンチマークで16ヶ月連続改善、人間レベルのコンピューター使用能力に接近
  - SWE-bench Verified約80.2%、コード実行・メモリ・プログラマティックツール呼び出しがGA
  - Claude in ExcelがMCPコネクタ対応（S&P Global, LSEG, PitchBook等）
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6

### INFO-002
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropic LabsがClaude Designを発表。Claude Opus 4.7を搭載したデザインツールで、プロトタイプ・スライド・マーケティング素材等を作成。チームのデザインシステムを自動適用し、Canvaへのエクスポート、Claude Codeへのハンドオフ機能を備える。
- **キーファクト:**
  - Pro, Max, Team, Enterprise向けリサーチプレビューとして提供
  - デザインシステムの自動構築（コードベース・デザインファイル読み取り）
  - PPTX/PDF/HTML/Canvaエクスポート対応
  - Databricks, Datadog, Canva, Brilliant等が早期採用
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs

### INFO-003
- **タイトル:** OpenAI Agents SDK: Practical Guide to Building Agent Workflows
- **ソース:** UIBakery
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKのコードファーストフレームワーク解説。ツール使用、タスクハンドオフ、ガードレール、ワークフロー状態管理をサポート。
- **キーファクト:**
  - エージェントワークフロー構築向けの包括的フレームワーク
- **引用URL:** https://uibakery.io/blog/openai-agents-sdk

### INFO-004
- **タイトル:** OpenAI Release Notes - May 2026 Latest Updates
- **ソース:** Releasebot
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがAgents SDKにsandboxingとネイティブハーネスを追加。永続化された/goalワークフロー、app-server API、モデルツール、ランタイム継続機能を追加。
- **キーファクト:**
  - persisted /goalワークフロー新機能
  - TUIコントロールでcreate/pause/resume/clear対応
- **引用URL:** https://releasebot.io/updates/openai

### INFO-005
- **タイトル:** Claude Agent SDK TypeScript CHANGELOG
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-05-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDKがClaude Code v2.0.57とパリティ達成。tools オプションでBash/Read等のビルトインツール指定が可能に。
- **キーファクト:**
  - Claude Code v2.0.57とのパリティ達成
  - ビルトインツールの選択的指定機能追加
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/CHANGELOG.md

### INFO-006
- **タイトル:** VS Code Adapts to Claude Code's Ecosystem
- **ソース:** Visual Studio Magazine
- **公開日:** 2026-05-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Anthropic, Microsoft
- **要約:** MicrosoftのVS CodeがClaude Codeのエコシステムに適応。Claude Agent SDKがVS Code内で直接エージェントセッションを提供し、計画・実行・反復が可能。
- **キーファクト:**
  - VS Code内でClaude Agent SDKによるエージェントセッションが直接動作
  - MicrosoftがAnthropicエコシステムとの統合を推進
- **引用URL:** https://visualstudiomagazine.com/articles/2026/05/04/special-embrace-vs-code-adapts-to-claude-codes-ecosystem.aspx

### INFO-007
- **タイトル:** Google Gemini Enterprise Agent Platform
- **ソース:** Google Cloud Blog
- **公開日:** 2026-05-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google
- **要約:** Google CloudがGemini Enterprise Agent Platformを発表。Vertex AIサービスをエージェントの構築・スケーリング・ガバナンス・最適化のための統合プラットフォームに進化。Inbox機能でエージェント活動の一元監視が可能。
- **キーファクト:**
  - Gemini Enterprise Agent Platform: エージェント構築・スケーリング・ガバナンス統合
  - Gemini Deep Research Agentが自律的に計画・検索・レポート作成
  - AI token成長: 100億/分→160億/分（Q4→Q1）
- **引用URL:** https://cloud.google.com/blog/products/ai-machine-learning/what-google-cloud-announced-in-ai-this-month

### INFO-008
- **タイトル:** xAI Grok models on Gemini Enterprise Agent Platform
- **ソース:** Google Cloud Docs
- **公開日:** 2026-05-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** xAI, Google
- **要約:** xAIのGrokモデルがGoogleのGemini Enterprise Agent Platformで利用可能に。クロスプラットフォーム相互乗り入れの具体化。
- **キーファクト:**
  - GrokモデルがGoogle Cloud Agent Platform上で提供
  - クロスプラットフォーム相互乗り入れの進展
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok

### INFO-009
- **タイトル:** AI Agent Deletes Production Database, Raises Insider Risk Concerns
- **ソース:** LinkedIn
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01, KIQ-002-03
- **関連企業:** （一般）
- **要約:** AIエージェントが本番データベースを削除するインシデントが発生。インサイダーリスクの懸念が高まっている。NHI（Non-Human Identity）のガバナンス必要性を指摘。
- **キーファクト:**
  - AIエージェントによる本番DB削除インシデント
  - NHI（非人間アイデンティティ）のガバナンス必要性
- **引用URL:** https://www.linkedin.com/posts/javedikbal_agentic-insiderrisk-activity-7454725387143794688-Bs_b

### INFO-010
- **タイトル:** xAI launches Grok 4.3 at aggressively low price
- **ソース:** VentureBeat
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** xAI
- **要約:** xAIがGrok 4.3を発表。低価格戦略と新Voice Agent API（$3.00/hr）を提供。
- **キーファクト:**
  - Voice Agent API (grok-voice-think-fast-1.0): $3.00/hr ($0.05/min)
  - 攻撃的低価格戦略
- **引用URL:** https://venturebeat.com/technology/xai-launches-grok-4-3-at-an-aggressively-low-price-and-a-new-fast-powerful-voice-cloning-suite

### INFO-011
- **タイトル:** China's cyberspace regulator warns ByteDance apps
- **ソース:** Global Banking and Finance
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, BYTEDANCE-CHINESE, KIQ-002-03
- **関連企業:** ByteDance
- **要約:** 中国のサイバースペース規制当局がByteDanceのアプリ（Jianying, Maoxiang, Jimeng AI）に対し、AI生成コンテンツのラベリング法遵守を警告。
- **キーファクト:**
  - ByteDanceアプリ3つがAI生成コンテンツラベリング法違反で警告
  - 中国AI規制の執行強化
- **引用URL:** https://www.globalbankingandfinance.com/chinas-cyberspace-regulator-warns-bytedance-apps-website/

---

### KIQ-001-02: 各社のAgent製品のエンタープライズ向け展開

---

### INFO-012
- **タイトル:** Anthropic Claude Security for Enterprise: What You Need to Know
- **ソース:** LinkedIn / Technijian
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Anthropic Claudeのエンタープライズセキュリティガイド。GDPR, HIPAA, SOC 2対応の確保方法を解説。エンタープライズプランは高度なセキュリティ・コンプライアンス管理を提供。
- **キーファクト:**
  - Claude Enterpriseプラン: セキュリティ・コンプライアンス・スケーラブルAI向け
  - GDPR/HIPAA/SOC 2対応確認の必要性
- **引用URL:** https://www.linkedin.com/pulse/anthropic-claude-security-enterprise-what-you-need-know-technijian-3cldc

### INFO-013
- **タイトル:** Ensono AI Model Services brings Claude and AWS Bedrock together
- **ソース:** Ensono
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Anthropic, Amazon
- **要約:** EnsonoがClaudeとAWS Bedrockを統合したエンタープライズ向けAIモデルサービスを提供。規制産業向けのエンタープライズグレードセキュリティ・コンプライアンス・運用サポートを備える。
- **キーファクト:**
  - Claude + AWS Bedrock統合のエンタープライズサービス
  - 規制産業向けセキュリティ・コンプライアンス設計
- **引用URL:** https://www.ensono.com/insights-and-news/expert-opinions/the-ciso-approved-path-to-ai-innovation-is-here/

### INFO-014
- **タイトル:** Claude Mythos and the End of Patch Centric Security
- **ソース:** Radware
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** AnthropicのClaude Mythosがパッチ中心のセキュリティアプローチを終わらせる可能性。AIエージェントのセキュリティパラダイムシフトを論じる。
- **キーファクト:**
  - Claude Mythosによるセキュリティアプローチの変革可能性
- **引用URL:** https://www.radware.com/blog/anthropic-claude-mythos-and-the-end-of-patch-centric-security/

---

### KIQ-001-03: 各社のAgent開発者エコシステム

---

### INFO-015
- **タイトル:** MCP Security Guide 2026: Threats, Defenses
- **ソース:** Practical DevSecOps
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic, OpenAI, Google, Microsoft
- **要約:** MCP（Model Context Protocol）がメインストリーム化。OpenAI, Google, Microsoft, Blockが全てサポート。数千のMCPサーバーがエコシステムに存在するが、セキュリティリスクも浮上。
- **キーファクト:**
  - MCPはOpenAI/Google/Microsoft/Block全てがサポート
  - エコシステムに数千のMCPサーバーが存在
  - セキュリティリスク（Shadow IT等）が指摘されている
- **引用URL:** https://www.practical-devsecops.com/mcp-security-guide/

### INFO-016
- **タイトル:** Red Hat MCP Gateway for OpenShift
- **ソース:** Red Hat Blog
- **公開日:** 2026-05-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Red Hat (IBM)
- **要約:** Red HatがOpenShift向けMCP Gatewayをテクノロジープレビューとしてリリース。エンタープライズ規模でのAIエージェントトラフィック制御を提供。
- **キーファクト:**
  - OpenShift向けMCP Gateway（Technology Preview）
  - エンタープライズ規模でのMCPトラフィック制御
- **引用URL:** https://www.redhat.com/en/blog/control-your-ai-agent-traffic-scale-model-context-protocol-gateway-red-hat-openshift-now-technology-preview

### INFO-017
- **タイトル:** AI Agent Marketplace Landscape 2026
- **ソース:** Agensi
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** AIエージェントのスキルマーケットプレイスが「次のApp Store」になりつつある状況の包括的概要。各主要プラットフォームの比較。
- **キーファクト:**
  - エージェントスキルマーケットプレイスが新カテゴリとして確立
  - 各主要プラットフォームの比較分析
- **引用URL:** https://www.agensi.io/learn/ai-agent-marketplace-landscape-2026

### INFO-018
- **タイトル:** Kaltura Open-Sources Suite of AI Agent Skills
- **ソース:** GlobeNewsWire
- **公開日:** 2026-05-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Kaltura
- **要約:** KalturaがAIエージェントスキルスイートをオープンソース化。本番検証済みのスキルでAIコーディングエージェントがリッチメディアアプリを構築可能に。
- **キーファクト:**
  - AIエージェントスキルのオープンソース化
  - 本番検証済みスキルの提供
- **引用URL:** https://www.globenewswire.com/news-release/2026/05/04/3286632/0/en/kaltura-open-sources-suite-of-ai-agent-skills-enabling-any-ai-agent-to-build-intelligent-rich-media-digital-experiences.html

### INFO-019
- **タイトル:** Building and Using MCP Servers in Visual Studio
- **ソース:** Visual Studio Magazine
- **公開日:** 2026-05-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Microsoft, Anthropic
- **要約:** MCPサーバーの構築とVisual Studioでの使用方法。MCPがLLMとデータベース・ファイル・API・外部ツールを接続するユニバーサル標準として定着。
- **キーファクト:**
  - MCPのVisual Studio統合
  - ユニバーサル標準としての定着
- **引用URL:** https://visualstudiomagazine.com/articles/2026/05/05/building-and-using-mcp-servers-in-visual-studio.aspx

---

### KIQ-001-04: 各社のマルチモーダルAgent統合

---

### INFO-020
- **タイトル:** InfantAgent-Next: A Multimodal Generalist Agent
- **ソース:** arXiv
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** （学術）
- **要約:** InfantAgent-Nextはテキスト・画像・音声を統合した汎用エージェント。コンピューターをマルチモーダルに操作可能。
- **キーファクト:**
  - テキスト・画像・音声を統合した汎用エージェントアーキテクチャ
- **引用URL:** https://arxiv.org/html/2505.10887v3

### INFO-021
- **タイトル:** Engageware Launches Voice Agents for End-to-End CX Execution
- **ソース:** CXM Today
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Engageware
- **要約:** Engagewareが音声エージェントを発表。会話型AIによるインテント理解とワークフロー実行を自然な対話で実現。
- **キーファクト:**
  - 音声エージェントによるエンドツーエンドCX実行
  - メニュー方式ではない自然対話ベースのワークフロー実行
- **引用URL:** https://cxmtoday.com/news/engageware-launches-voice-agents-for-end-to-end-cx-execution/

### INFO-022
- **タイトル:** Codex Browser Use Controls Your Computer
- **ソース:** YouTube
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAI Codexのブラウザ使用機能がコンピューターを制御。自律的コーディングワークフロー、ブラウザテストAIとしての機能を示す。
- **キーファクト:**
  - OpenAI Codexのブラウザ制御・コンピューター使用機能
  - 自律的コーディング・テストワークフロー
- **引用URL:** https://www.youtube.com/watch?v=Du34BzfVRas

### INFO-023
- **タイトル:** AI Agents Market Map 2026: Every Category Mapped
- **ソース:** MightyBot
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** （業界全体）
- **要約:** 2026年のAIエージェントマーケットマップ。ブラウザ・コンピューター使用エージェント（OpenAI Operator型、Claude computer use等）が新カテゴリとして確立。
- **キーファクト:**
  - ブラウザ・コンピューター使用エージェントが独立カテゴリに
  - OpenAI Operator型・Claude computer use等が代表
- **引用URL:** https://mightybot.ai/blog/ai-automation-agents-market-maps-gone-wild/

---

### KIQ-002-01: 主要クラウドプロバイダーのAI Agent統合

---

### INFO-024
- **タイトル:** OpenAI Models on Amazon Bedrock: AWS expands partnership
- **ソース:** Amazon About
- **公開日:** 2026-04-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon, OpenAI
- **要約:** AWSとOpenAIが提携大幅拡大。(1) OpenAIモデルがAmazon Bedrockで利用可能（Limited Preview）、(2) Codex on Amazon Bedrock（400万+/週ユーザー）、(3) Amazon Bedrock Managed Agents powered by OpenAI。統一セキュリティ・ガバナンス・コスト管理。
- **キーファクト:**
  - OpenAIモデルがBedrock API経由で利用可能に（Limited Preview）
  - Codex: 400万+/週ユーザー、CLI/デスクトップ/VS Code対応
  - Bedrock Managed Agents: OpenAIフロンティアモデル最適化エージェント構築
  - IAM/PrivateLink/guardrails/暗号化/CloudTrail等のエンタープライズ統制継承
  - AWSクラウドコミットメントへの充当可能
- **引用URL:** https://www.aboutamazon.com/news/aws/bedrock-openai-models

### INFO-025
- **タイトル:** Amazon Bedrock AgentCore launches capabilities for optimizing agent performance
- **ソース:** AWS What's New
- **公開日:** 2026-04-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** Amazon Bedrock AgentCoreがエージェントパフォーマンス最適化機能をプレビューでリリース。エージェントの実行最適化を可能に。
- **キーファクト:**
  - Bedrock AgentCore: エージェントパフォーマンス最適化
  - Identity管理でOn-Behalf-Of (OBO) トークン交換をサポート
- **引用URL:** https://aws.amazon.com/about-aws/whats-new/2026/05/bedrock-agentcore-optimization-preview/

### INFO-026
- **タイトル:** Microsoft Agent 365, now generally available
- **ソース:** Microsoft Security Blog
- **公開日:** 2026-05-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** Microsoft
- **要約:** Microsoft Agent 365がGA（一般提供）化。Shadow AIエージェントの発見・管理機能のプレビューも発表。エンタープライズ向けエージェントガバナンスの新段階。
- **キーファクト:**
  - Microsoft Agent 365がGA化
  - Shadow AIエージェントの発見・管理機能（プレビュー）
  - Microsoft Foundryとの統合でエージェントガバナンス提供
- **引用URL:** https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/

### INFO-027
- **タイトル:** Google Cloud surpasses $20B, growth was capacity-constrained
- **ソース:** TechCrunch via Yahoo Finance
- **公開日:** 2026-04-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01, KIQ-003-04
- **関連企業:** Google
- **要約:** Google Cloudが初の四半期$20B超え（63% YoY増）。AI需要が牽引し、GenAI製品は800% YoY成長。Gemini EnterpriseはQoQ 40%成長。しかし計算能力制約でさらに成長できた可能性を示唆。バックログは$462Bに倍増。
- **キーファクト:**
  - Google Cloud Q1 2026: $20.03B（63% YoY増）
  - GenAI製品: 800% YoY成長
  - Gemini Enterprise: QoQ 40%成長
  - AI token: 100億/分→160億/分
  - バックログ$462B（倍増）、24ヶ月で50%消化予定
  - Azure 40%成長、AWSより高い成長率
- **引用URL:** https://finance.yahoo.com/sectors/technology/articles/google-cloud-surpasses-20b-says-222048133.html

### INFO-028
- **タイトル:** State of LLM Benchmarks 2026: Rankings, Trends
- **ソース:** BenchLM
- **公開日:** 2026-03-22 (Updated 2026-04-08)
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02, KIQ-003-03, KIQ-005-01
- **関連企業:** Anthropic, Google, OpenAI, xAI, DeepSeek
- **要約:** 2026年4月時点のLLMベンチマーク総括。Claude Mythos Previewが99で総合1位。Gemini 3.1 Pro（93）、GPT-5.4 Pro（92）、Grok 4.1（90）が追随。オープンウェイト最上位はDeepSeek V4 Pro (Max)の87。トップは単一ベンダーの物語ではなくなった。
- **キーファクト:**
  - 総合: Claude Mythos Preview 99 > Gemini 3.1 Pro 93 > GPT-5.4 Pro 92 > Grok 4.1 90
  - コーディング: Claude Mythos Preview 100 > Gemini 3.1 Pro 94.3 > GPT-5.4 Pro 92.8
  - 推論: GPT-5.4 Pro 99.3 > Gemini 3.1 Pro 97 > GPT-5.3 Codex 94.7
  - オープンウェイト最上位: DeepSeek V4 Pro (Max) 87
  - オープンウェイトとプロプライエタリの差は6ポイント（縮小傾向）
- **引用URL:** https://benchlm.ai/blog/posts/state-of-llm-benchmarks-2026

---

### KIQ-001-05: スキル配布と実行環境

---

### INFO-029
- **タイトル:** Skills Marketplace — The New App Store for AI Agents
- **ソース:** Agensi
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** OpenAI
- **要約:** AIエージェントのスキルマーケットプレイスが「新しいApp Store」カテゴリを創造。各社が構築しており、その重要性が高まっている。
- **キーファクト:**
  - スキルマーケットプレイスが新カテゴリとして確立
- **引用URL:** https://www.agensi.io/learn/skills-marketplace-ai-agents

### INFO-030
- **タイトル:** Agent Skills | Atlassian Support
- **ソース:** Atlassian
- **公開日:** 2026-05-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** OpenAI, Atlassian
- **要約:** Atlassianのエージェントスキルドキュメント。OpenAI Codexが .agents/skills/ ディレクトリからスキルを読み取る仕組みを解説。
- **キーファクト:**
  - OpenAI Codexの .agents/skills/ ディレクトリ標準
  - スキルの自動読み取りメカニズム
- **引用URL:** https://support.atlassian.com/organization-administration/docs/agent-skills/

### INFO-031
- **タイトル:** OpenShell: NVIDIA OSS for safe AI agent execution
- **ソース:** Instagram/NVIDIA
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** OpenAI, NVIDIA
- **要約:** NVIDIAがOpenShellをオープンソース化。AIエージェントの安全な実行環境を提供。OpenAI Agents SDKのサンドボックス実行と同様の機能。
- **キーファクト:**
  - AIエージェントの安全なエンタープライズ実行環境
  - サンドボックス実行機能
- **引用URL:** https://www.instagram.com/reel/DXz-u3ojytB/

### INFO-032
- **タイトル:** Google Official Agent Skills Repository
- **ソース:** Google Cloud Platform (Medium)
- **公開日:** 2026-04-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Google
- **要約:** Googleが公式Agent Skillsリポジトリを公開。AIエージェント向けのコンパクトな「agent-first」ドキュメントを提供する技術タスク用スキル。
- **キーファクト:**
  - 公式Agent Skillsリポジトリ公開
  - 「agent-first」ドキュメントフォーマット
- **引用URL:** https://medium.com/google-cloud/google-cloud-platform-technology-nuggets-april-16-30-2026-3e9b2b145ad9

### INFO-033
- **タイトル:** How Agentic AI Changes the Economics of Enterprise Software
- **ソース:** arXiv
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** （学術）
- **要約:** Agentic AIがエンタープライズソフトウェアの経済学を変革。ベンダーロックインメカニズムは全デリバリーモデルで有効で、AI機能の組み込みにより追加的なスイッチングコストが生じ、ロックインは深まっている。
- **キーファクト:**
  - ベンダーロックインはAI機能の組み込みで深化
  - 追加的スイッチングコストの発生
- **引用URL:** https://arxiv.org/html/2604.26482v1

---

### KIQ-002-02: エンタープライズ顧客のAI Agent採用率

---

### INFO-034
- **タイトル:** Dun & Bradstreet Global Survey: AI Impact at Inflection Point
- **ソース:** Morningstar/PR Newswire
- **公開日:** 2026-05-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** D&Bの10,000社グローバル調査。97%の組織がAI活動を報告、56%が今後12ヶ月でAI投資増加予定、30%が本番スケールへ移行。
- **キーファクト:**
  - 97%の組織がAI活動を報告
  - 56%がAI投資増加予定（12ヶ月以内）
  - 30%が本番スケールへの移行中
- **引用URL:** https://www.morningstar.com/news/pr-newswire/20260504fl50726/dun-bradstreet-global-survey-of-10000-businesses-finds-ai-impact-at-an-inflection-point

### INFO-035
- **タイトル:** State of Agentic AI Q2 2026 Quarterly Report
- **ソース:** Digital Applied
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** Q1 2026のAIパイロット→本番移行率は18%（Q3 2025は11%）。単一四半期として最大の上昇幅。AI導入が成果を上回るペースで進行。
- **キーファクト:**
  - パイロット→本番移行率: Q3 2025 11% → Q1 2026 18%
  - 単一四半期最大の上昇幅
- **引用URL:** https://www.digitalapplied.com/blog/state-of-agentic-ai-q2-2026-quarterly-report

### INFO-036
- **タイトル:** AI adoption accelerating faster than security layer
- **ソース:** TheStreet
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** 2026年までに40%のエンタープライズアプリがタスク特化型AIエージェントを使用する見込み。しかし24.4%の組織のみがAIエージェントへの完全な可視性を持つ。
- **キーファクト:**
  - 40%のエンタープライズアプリがAIエージェント使用見込み（2026年末）
  - 24.4%の組織のみがAIエージェントへの完全な可視性を持つ
- **引用URL:** https://www.thestreet.com/technology/ai-adoption-is-accelerating-faster-than-its-security-layer

### INFO-037
- **タイトル:** Fortune 500 tracking AI usage - employee monitoring
- **ソース:** CNBC
- **公開日:** 2026-05-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-004-01
- **関連企業:** （業界全体）
- **要約:** Fortune 500のほぼ全社がAI使用を追跡。ある企業ではAIエージェントが1四半期で1億2900万タスクを処理。社内では96%のサポートケースを自動化。
- **キーファクト:**
  - Fortune 500ほぼ全社がAI使用追跡
  - 1四半期で1億2900万AIエージェントタスク処理（特定企業）
  - 96%の社内サポートケース自動化
- **引用URL:** https://www.cnbc.com/2026/05/05/ai-use-work-employee-monitoring-tech-surveillance.html

### INFO-038
- **タイトル:** ServiceNow AI workforce - autonomous workforce
- **ソース:** Fortune
- **公開日:** 2026-05-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** ServiceNow, Microsoft, NVIDIA
- **要約:** ServiceNowが自律的AIワークフォースを発表。社内ITサービスデスクで人間エージェントより99%高速な解決。Gartner予測では2026年末に40%のエンタープライズアプリがAIエージェントを組み込む。
- **キーファクト:**
  - ITサービスデスク解決99%高速化（人間比）
  - Gartner: 2026年末に40%のエンタープライズアプリがAIエージェント組み込み
  - Docusignが自律的ワークフローを目標
- **引用URL:** https://fortune.com/2026/05/05/servicenow-knowledge-2026-autonomous-workforce-microsoft-nvidia-ai-announcements/

### INFO-039
- **タイトル:** Snowflake ROI of Gen AI and Agents 2026
- **ソース:** Snowflake
- **公開日:** 2026-05-xx
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** GenAI早期採用者の92%がポジティブなROIを報告。C-level回答者の75%が非技術系組織でもポジティブな結果を報告。
- **キーファクト:**
  - 92%の早期採用者がポジティブROI
  - 75%のC-levelが非技術組織でポジティブ結果
- **引用URL:** https://www.snowflake.com/en/lp/radical-roi-generative-ai-short-form/

---

### KIQ-002-03: 規制環境の影響

---

### INFO-040
- **タイトル:** EU AI Act: What Enterprises Need to Do Before August 2026
- **ソース:** KNIME
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** （規制）
- **要約:** 2026年8月2日、EU AI Actが高リスクAIシステムの大部分について執行開始。採用・人事等の意思決定にAIを使用する組織は対応が必要。提案された猶予は否決された。
- **キーファクト:**
  - EU AI Act執行日: 2026年8月2日
  - 高リスクAIシステムの大部分が対象
  - 提案猶予は否決済み
- **引用URL:** https://www.knime.com/blog/eu-ai-act-what-enterprises-need-do-august-2026

### INFO-041
- **タイトル:** EU AI Act Compliance Automation 2026
- **ソース:** Turbotic
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** （規制）
- **要約:** EU AI Act高リスク期限が2026年8月2日に確定。提案された遅延は否決され、運用・ITリーダーは執行前に対応が必要。
- **キーファクト:**
  - 高リスク期限: 2026年8月2日確定
  - 提案遅延は否決
- **引用URL:** https://turbotic.com/resources/blog/eu-ai-act-compliance-automation-2026

### INFO-042
- **タイトル:** Big 5 AI Vendor Roundup: Week of April 27, 2026
- **ソース:** Info-Tech
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-01, KIQ-003-04
- **関連企業:** AWS, Microsoft, Google
- **要約:** 2026年の3社合算CapExは約$560Bに向かって推移。AWSが$200Bでリード、MicrosoftとGoogleが続く。
- **キーファクト:**
  - 3社合算CapEx: ~$560B（2026年）
  - AWS: $200Bでリード
- **引用URL:** https://www.infotech.com/research/big-5-ai-vendor-roundup-week-of-april-27-2026

---

### KIQ-002-06: 政府・軍のAI企業への経済的圧力

---

（該当なし - 過去1週間の新規情報なし）

---

### KIQ-002-04: AIエージェントによる業務自律化の進展

---

### INFO-043
- **タイトル:** Martech 2026: AI drives a major industry reset
- **ソース:** MarTech
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** 2026年のマーケティング技術ランドスケープはわずか0.7%成長（15,384→15,505）。AIが業界の大型リセットを牽引。表面的には停滞しているが、AIによる構造変革が進行中。
- **キーファクト:**
  - MarTech市場: 0.7%成長のみ（表面上の停滞）
  - AIがマーケティング技術の構造変革を牽引
- **引用URL:** https://martech.org/martech-2026-ai-drives-a-major-industry-reset/

### INFO-044
- **タイトル:** Why Klarna went back hiring humans after betting big on AI
- **ソース:** LinkedIn
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna
- **要約:** KlarnaがAI置き換え後の人材再雇用事例。700人を削減したAI活用で品質が低下し、人間の再雇用に転じた。2026年の投資家は純粋なAI置き換え人員削減ストーリーに懐疑的。
- **キーファクト:**
  - Klarna: AI置き換えで700人削減→品質低下→人間再雇用
  - Duolingo: AI-first転向で40%エラー率、18%リテンション低下
  - 2026年投資家は純粋AI置き換えストーリーに懐疑的
- **引用URL:** https://www.linkedin.com/pulse/why-klarna-went-back-hiring-humans-after-betting-big-ai-ekhlaque-bari-os7uc

### INFO-045
- **タイトル:** First Wave of AI Failures Should Teach Every Organization
- **ソース:** CFO Leadership
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** AI投資の95%がボトムラインへのリターンなし。2025年末までに42%の企業がAI投資を放棄。
- **キーファクト:**
  - AI投資の95%がリターンなし
  - 2025年末で42%の企業がAI投資放棄
- **引用URL:** https://cfoleadership.com/what-the-first-wave-of-ai-failures-should-teach-every-organization/

---

### KIQ-002-05: プラットフォーマーのAI統合による中間事業者侵食

---

### INFO-046
- **タイトル:** Google expands AI Max as automation shifts upstream
- **ソース:** Digiday
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google
- **要約:** GoogleがAI Maxをショッピング・トラベルキャンペーンに拡大。広告スタックの上流へ自動化がシフト。Meta AI使用量が向上、ビジネスAI会話が1000万/週超。
- **キーファクト:**
  - AI Maxがショッピング・トラベルに拡大
  - Meta: GenAIクリエイティブツール800万広告主使用
  - ビジネスAI会話: 1000万/週超
- **引用URL:** https://digiday.com/media-buying/the-rundown-google-expands-ai-max-as-automation-shifts-upstream/

### INFO-047
- **タイトル:** SaaS stocks hammered over AI fears
- **ソース:** Facebook
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** （SaaS業界）
- **要約:** SaaS銘柄がAIによる一部ソフトウェアの陳腐化懸念で下落。ただし今週の決算はよりポジティブな見方を示した。
- **キーファクト:**
  - SaaS銘柄のAI懸念による下落
  - 決算では一部ポジティブな結果
- **引用URL:** https://www.facebook.com/Insiderinventions/posts/saas-stocks-have-taken-a-hammering-this-year-over-fears-ai-will-make-some-softwa/1331629675496820/

---

### KIQ-003-01: 各社のAPI料金改定

---

### INFO-048
- **タイトル:** The End of Cheap AI Is Here
- **ソース:** Design Systems Collective
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIの2026年損失は$14B見込み。AnthropicがClaude Codeの$20プランからの削除をテスト。Codexが4月2日にper-token価格に移行。
- **キーファクト:**
  - OpenAI 2026年損失見込み: $14B
  - Codex: per-token価格に移行（4月2日）
  - Anthropic: Claude Code $20プランからの削除テスト
- **引用URL:** https://www.designsystemscollective.com/the-end-of-cheap-ai-is-here-what-designers-should-actually-do-about-it-a017356c3454

### INFO-049
- **タイトル:** AI costs can spike 50% in a single month
- **ソース:** Ramp/Facebook
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** （業界全体）
- **要約:** AIコストが一部企業で単月50%以上急増。AI価格は固定ではなく、トークン料金・モデル階層・使用量構造で変動。
- **キーファクト:**
  - AIコスト単月50%急増の事例
  - 動的価格設定による変動リスク
- **引用URL:** https://www.facebook.com/vaudit1/posts/ai-costs-can-spike-50-in-a-single-month-for-some-companies-ramp-2026ai-pricing-i/122268027176149421/

### INFO-050
- **タイトル:** GitHub Copilot new pricing model 2026
- **ソース:** Reddit
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Microsoft
- **要約:** GitHub Copilot Pro ユーザーは月1000 AIクレジット、Pro+ユーザーは月3000クレジットに移行（6月から）。ユーザーは実質的な値上げと指摘。
- **キーファクト:**
  - Copilot Pro: 月1000 AIクレジット
  - Copilot Pro+: 月3000 AIクレジット
  - 6月から新価格体系
- **引用URL:** https://www.reddit.com/r/GithubCopilot/comments/1szaou9/am_i_understanding_this_new_pricing_correctly/

---

### KIQ-003-03: オープンソースvs商用モデルの性能ギャップ

---

### INFO-051
- **タイトル:** LLM Model Just Became a Commodity
- **ソース:** LinkedIn
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** （業界全体）
- **要約:** Stanford 2026 AI Indexによると、オープンソースAIとフロンティアモデルの性能ギャップが約8%から約1.7%に縮小。LLMがコモディティ化の兆候。
- **キーファクト:**
  - オープンソースvs商用ギャップ: 8%→1.7%に縮小
  - Stanford 2026 AI Indexのデータ
- **引用URL:** https://www.linkedin.com/pulse/llm-model-just-became-commodity-heres-what-actually-real-bill-douglas-deg2c

---

### KIQ-003-04: 各社の資金調達・投資動向

---

### INFO-052
- **タイトル:** Anthropic weighs raising funds at $900B valuation
- **ソース:** CNBC
- **公開日:** 2026-04-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Anthropicが$900B評価額での資金調達を協議中。$30B年間収益。Claude Mythosのコンピュート需要が資金調達の理由。Amazon $25B投資・5GW計算能力、Google $40B投資・Broadcom経由5GW確保。OpenAIの$852B評価額を上回る可能性。
- **キーファクト:**
  - Anthropic評価額協議: $900B（OpenAI $852B上回る可能性）
  - 年間収益: $30B（年間化）
  - 前年収益: ~$10B
  - Amazon: $25B投資 + 5GW計算能力
  - Google: $40B投資計画 + Broadcom経由5GW
  - Claude Mythosのコンピュート需要が主な資金用途
- **引用URL:** https://www.cnbc.com/2026/04/29/anthropic-weighs-raising-funds-at-900b-valuation-topping-openai.html

### INFO-053
- **タイトル:** Half of Google/Amazon AI profits came from Anthropic stake
- **ソース:** Fortune
- **公開日:** 2026-04-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Google, Amazon, Anthropic
- **要約:** AmazonのAnthropic投資$80億が$700億以上の価値に。Google/Amazonの「AI利益」の半分がAnthropic持分からの含み益。AIバブルの懸念も浮上。
- **キーファクト:**
  - Amazon Anthropic投資: $80億→$700億以上
  - Google/AmazonのAI利益の半分がAnthropic持分含み益
- **引用URL:** https://fortune.com/2026/04/30/google-amazon-ai-profits-anthropic-stake-bubble-earnings-2026/

### INFO-054
- **タイトル:** Sierra raises $950M as race to own enterprise AI gets serious
- **ソース:** TechCrunch / CNBC
- **公開日:** 2026-05-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Sierra
- **要約:** Bret TaylorのAIスタートアップSierraが$950M Series E調達。評価額$15.8B。8四半期で$150M ARR到達（ソフトウェア史上最速クラス）。Fortune 50の40%+にサービス提供。年間$400BのCS市場のAI化を狙う。
- **キーファクト:**
  - Sierra Series E: $950M、$15.8B評価額
  - リード: Tiger Global, GV（Google Ventures）
  - 8四半期で$150M ARR（前例のないスピード）
  - Fortune 50の40%+にサービス、世界大手銀行の3分の1
  - CS市場年間$400Bの大部分がAIエージェントへ移行と予測
- **引用URL:** https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/

### INFO-055
- **タイトル:** AI venture funding to shoot up as bubble looms
- **ソース:** Computerworld
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** xAI, OpenAI
- **要約:** xAIが2026年初頭に$20B Series Eを完了。OpenAIは3月に$122Bの大型資金調達。AIベンチャー投資が急増する一方でバブル懸念も。
- **キーファクト:**
  - xAI: $20B Series E（2026年初頭）
  - OpenAI: $122B資金調達（3月）
- **引用URL:** https://www.computerworld.com/article/4164421/ai-venture-funding-to-shoot-up-this-year-as-bubble-looms.html

### INFO-056
- **タイトル:** Anthropic and OpenAI launching joint ventures for enterprise AI services
- **ソース:** TechCrunch
- **公開日:** 2026-05-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-001-02
- **関連企業:** Anthropic, OpenAI
- **要約:** AnthropicがBlackstone/H&F/Goldman SachsとエンタープライズAIサービス合弁会社設立（$1.5B評価額、各社$300M出資）。OpenAIはTPG/Brookfield/Advent/Bainと「The Development Company」設立（$10B評価額、$4B調達）。双方がPalantir型のFDE（Forward-Deployed Engineer）モデルを採用。
- **キーファクト:**
  - Anthropic合弁: $1.5B評価額、Blackstone/H&F/GS各$300M + Apollo/General Atlantic/GIC/Sequoia等
  - OpenAI合弁「The Development Company」: $10B評価額、$4B調達、TPG/Brookfield/Advent/Bain
  - 投資家のポートフォリオ企業への優先販売アクセス
  - FDE（Forward-Deployed Engineer）モデル採用
  - OpenAI: $122B資金調達（3月、$852B評価額）
- **引用URL:** https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/

---

### KIQ-004-01: 先行領域のAI業務自律化

---

### INFO-057
- **タイトル:** The Real Job Destruction from AI Is Hitting Before Careers Can Start
- **ソース:** Yale Insights
- **公開日:** 2026-05-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** Stanford Digital Economy LabのErik Brynjolfssonらの研究（2025年11月）で、AI露出の高い職業で初期キャリア雇用が16%減少を発見。AIによる雇用破壊がキャリア開始前に発生。
- **キーファクト:**
  - 初期キャリア雇用16%減少（AI露出高い職業）
  - Stanford Digital Economy Lab研究
- **引用URL:** https://insights.som.yale.edu/insights/the-real-job-destruction-from-ai-is-hitting-before-careers-can-start

### INFO-058
- **タイトル:** Programmer employment fell 27.5% 2023-2025
- **ソース:** IEEE Spectrum / Medium
- **公開日:** 2026-05-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** IEEE Spectrumによると米国のプログラマー雇用が2023〜2025年で27.5%減少。ただしBLS職業分類の変更（プログラマー→SE再分類）の影響の可能性あり。
- **キーファクト:**
  - 米国プログラマー雇用: 2023-2025で27.5%減少（IEEE Spectrum）
  - BLS職業分類変更の影響可能性
- **引用URL:** https://lancengym.medium.com/stop-telling-companies-to-hire-junior-devs-the-market-already-solved-the-problem-6c52ac208b9f

### INFO-059
- **タイトル:** 760,000 tech workers laid off Jan 2023-Apr 2026
- **ソース:** Substack
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-01
- **関連企業:** （業界全体）
- **要約:** 2023年1月〜2026年4月で約76万人のテック労働者がレイオフ。2023年のポストCOVID過剰採用修正波と2025-2026年のAI置き換え波の2波を含む。
- **キーファクト:**
  - 76万人テックレイオフ（2023/1〜2026/4）
  - ポストCOVID修正波とAI置き換え波の2波構造
- **引用URL:** https://longyield.substack.com/p/the-great-tech-reckoning-900000-jobs

---

### KIQ-004-02: コーディング能力の市場価値変化

---

### INFO-060
- **タイトル:** Best AI Coding Agents in 2026, Ranked
- **ソース:** MightyBot
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** OpenAI, Anthropic
- **要約:** 開発者ツール収益が前例のない規模に。Cursor $1.2B ARR、Claude $2.5B年間化ランレート。GitHub Copilotはエンタープライズ採用リード、Cursorは開発者人気、Claude Codeが急追。
- **キーファクト:**
  - Cursor: $1.2B ARR
  - Claude: $2.5B annualized run rate
  - GitHub Copilot: 29%使用率（成長停滞）、46%コード補完率
- **引用URL:** https://mightybot.ai/blog/coding-ai-agents-for-accelerating-engineering-workflows/

### INFO-061
- **タイトル:** AI coding tools: Copilot 29%, growth has stalled
- **ソース:** Instagram
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft, Anthropic
- **要約:** 開発者AI採用率: GitHub Copilot 29%（最も使用されるが成長停滞）、Cursor IDEが開発者人気で台頭、Claude Codeが急成長。
- **キーファクト:**
  - GitHub Copilot: 29%使用率、成長停滞
  - Cursor: 開発者人気首位
  - Claude Code: 急成長中
- **引用URL:** https://www.instagram.com/p/DX381O_F7vi/

### INFO-062
- **タイトル:** Firms adopting generative AI reduce junior hiring ~22%
- **ソース:** Facebook
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** GenAI採用企業はジュニア採用を約22%削減。特に採用後6四半期内。ジュニアロールは非AI企業比で7-12%減少。
- **キーファクト:**
  - GenAI採用企業のジュニア採用22%削減
  - ジュニアロール: 非AI企業比7-12%減少
- **引用URL:** https://www.facebook.com/groups/vibecodinglife/posts/2022380661683794/

---

### KIQ-005-01: AGI到達度のベンチマーク指標

---

### INFO-063
- **タイトル:** Sebastian Bubeck: AGI will be aligned to companies who create it
- **ソース:** Reddit
- **公開日:** 2026-05-01
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI
- **要約:** OpenAIチーフサイエンティストSebastian Bubeckが「AGIは創造する企業にアラインされる」と発言。AGIの成果を医療等に向けるためAI企業自体への圧力が必要と主張。
- **キーファクト:**
  - Bubeck: 「AGIは創造企業にアラインされる」
  - AI企業自体への圧力の必要性を主張
- **引用URL:** https://www.reddit.com/r/accelerate/comments/1t0ozdy/as_of_may_1_2026_sebastian_bubeck_chief_scientist/

---

### KIQ-005-02: 主要CEO/研究者のAGIタイムライン予測

---

### INFO-064
- **タイトル:** Demis Hassabis confirms AGI by around 2030
- **ソース:** Facebook/Instagram
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google
- **要約:** Google DeepMindのDemis HassabisがAGI到達を2030年頃と再確認。一方、AnthropicのDario Amodeiは2-3年と予測。主要研究者間で合意なし。
- **キーファクト:**
  - Hassabis: AGI ~2030年
  - Amodei (Anthropic): 2-3年
  - 主要研究者間でタイムライン合意なし
- **引用URL:** https://www.instagram.com/reel/DX5v_pQtb3J/

---

### KIQ-005-03: AGI安全性とガバナンス

---

### INFO-065
- **タイトル:** Trump admin will test Google, Microsoft and xAI models
- **ソース:** CNBC
- **公開日:** 2026-05-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** Google, Microsoft, xAI
- **要約:** CAISI（商務省傘下）がGoogle DeepMind、Microsoft、xAIと事前評価契約を締結。デプロイ前評価とフロンティアAI能力評価を実施。2024年のOpenAI/Anthropicとの契約は再交渉済み。新AIワーキンググループ（大統領令による可能性）も検討中。Anthropicは国務省からsupply chain risk指定を受けつつ、Dario AmodeiがWhite Houseと「生産的」な会談を実施。
- **キーファクト:**
  - CAISI: Google DeepMind/MSFT/xAIと事前評価契約
  - OpenAI/Anthropicの2024年契約は再交渉済み
  - 新AIワーキンググループ設立検討（大統領令の可能性）
  - Claude Mythosが政府の注目を惹いた契機
  - Anthropic: supply chain risk指定 + White House会談（「生産的」）
- **引用URL:** https://www.cnbc.com/2026/05/05/ai-oversight-trump-google-microsoft-xai.html

### INFO-066
- **タイトル:** US to safety test new AI models - BBC
- **ソース:** BBC
- **公開日:** 2026-05-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** Google, Microsoft, xAI
- **要約:** BBC確認: 米国商務省がGoogle、Microsoft、xAIの新AIツールをリリース前にテスト。政府によるAI監視の新段階。
- **キーファクト:**
  - 米商務省による事前テスト確認（BBC報道）
  - 政府のAI監視の新段階
- **引用URL:** https://www.bbc.com/news/articles/cgjp2we2j8go

---

### 動的追加: KIQ-AGENT-001 (Arbiter最優先)

---

（該当なし - Claude Code WAU/MAU定量データの公開情報なし）

---

### 動的追加: KIQ-BTD-PRICE (Arbiter最優先)

---

### INFO-067
- **タイトル:** The era of subsidised inference is truly ending
- **ソース:** Hacker News
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-BTD-PRICE
- **関連企業:** DeepSeek
- **要約:** DeepSeek API価格はAnthropic/OpenAIと比較して非常に低い。300%の価格差は品質が近い場合正当化困難。補助金付き推論の時代が終わりつつある。
- **キーファクト:**
  - DeepSeek API: 競合比300%低価格
  - 補助金付き推論の終了兆候
- **引用URL:** https://news.ycombinator.com/item?id=47923547

### INFO-068
- **タイトル:** DeepSeek backed by High-Flyer Capital hedge fund
- **ソース:** MindStudio
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-BTD-PRICE
- **関連企業:** DeepSeek
- **要約:** DeepSeekは量的ヘッジファンドHigh-Flyer Capitalが支援。AI研究は収益的な金融事業により実質的に補助金を受けている。トークンのみでの収益化は不要で、クラウド・コマース・広告等で収益化可能。
- **キーファクト:**
  - DeepSeek: High-Flyer Capital（量的ヘッジファンド）支援
  - 金融事業による研究への間接的補助金
  - トークン価格のみに依存しない収益モデル
- **引用URL:** https://www.mindstudio.ai/blog/open-source-ai-vs-closed-source-business-model/

---

### 動的追加: H-GOO-001 Google Cloud エンタープライズAI収益

---

### INFO-069
- **タイトル:** 4 Reasons Alphabet's Cloud Growth Outpaced Its Larger Rivals
- **ソース:** Motley Fool
- **公開日:** 2026-05-04
- **信頼性コード:** B-3
- **関連KIQ:** H-GOO-001
- **関連企業:** Google
- **要約:** Google CloudのクラウドGenAIモデル収益が年率約800%成長。Gemini EnterpriseのQoQ収益増は40%。Google Cloudの収益$20.03B、63% YoY成長。
- **キーファクト:**
  - クラウドGenAI収益: ~800% YoY成長
  - Gemini Enterprise: 40% QoQ成長
  - Google Cloud: $20.03B収益、63% YoY
- **引用URL:** https://www.fool.com/investing/2026/05/04/4-reasons-alphabets-cloud-growth-outpaced-its-larg/

---

### BYTEDANCE-CHINESE: ByteDance/Doubao/Seed中国語一次情報

---

### INFO-070
- **タイトル:** 豆包AI将新增付费版本（豆包AIに有料版追加）
- **ソース:** 聯合早報
- **公開日:** 2026-05-04
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-01
- **関連企業:** ByteDance
- **要約:** 字节跳動のAI助手「豆包」が有料版を発表。最低¥68/月（約$12.7）。無料版は継続提供。AI大モデルの無料時代が終了の兆候。
- **キーファクト:**
  - 豆包有料版: ¥68/月〜（3段階: 標準/強化/専門）
  - 無料版は継続提供
  - 算力・トークン消費コストに対応する価格設定
- **引用URL:** https://www.zaobao.com.sg/news/china/story20260504-8994053

### INFO-071
- **タイトル:** Seed2.0 正式发布（Seed2.0正式発表）
- **ソース:** 知乎
- **公開日:** 2026-05-xx
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceがSeed2.0を正式発表。Seed2.0 ProとCodeモデルが豆包AppとTRAEで利用可能に。全シリーズAPIが火山エンジンで提供開始。
- **キーファクト:**
  - Seed2.0 Pro/Codeモデル公開
  - 豆包AppとTRAEで利用可能
  - 火山エンジンAPI提供開始
- **引用URL:** https://zhuanlan.zhihu.com/p/2006074032718627590

### INFO-072
- **タイトル:** 字節跳動發布Seed3D 2.0（ByteDance Seed3D 2.0発表）
- **ソース:** Threads
- **公開日:** 2026-04-23
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceがSeed3D 2.0を発表。SOTAレベルの幾何学・テクスチャ品質。1枚の画像から高精度3Dモデルを数秒で生成。
- **キーファクト:**
  - Seed3D 2.0: SOTA幾何学・テクスチャ
  - 1画像→高精度3Dモデル数秒生成
  - 技術報告公開、API火山エンジン提供
- **引用URL:** https://www.threads.com/@mexx1999.ai/post/DXtlh6JEviB/

---

### KIQ-002-06: 政府・軍のAI企業への経済的圧力（追加情報）

---

### INFO-073
- **タイトル:** Pentagon Makes Deals With AI Companies - Anthropic Excluded
- **ソース:** New York Times
- **公開日:** 2026-05-01
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Google, NVIDIA, Anthropic
- **要約:** ペンタゴンが分類ネットワークでのAI展開に向けて7社と契約。OpenAI、Google、NVIDIA等が含まれるが、AI安全性姿勢で対立中のAnthropicは除外。「any lawful use」条項あり。
- **キーファクト:**
  - ペンタゴン: 7社と分類ネットワークAI契約
  - Anthropic除外（AI安全性で対立）
  - 「any lawful use」条項
- **引用URL:** https://www.nytimes.com/2026/05/01/us/politics/pentagon-ai-companies-deals.html

### INFO-074
- **タイトル:** Pentagon inks deals with seven AI companies
- **ソース:** The Guardian
- **公開日:** 2026-05-01
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Google, NVIDIA, xAI, Anthropic
- **要約:** OpenAI、Google、NVIDIA等が「any lawful use」に合意。AI悪用可能性でペンタゴンと係争中のAnthropicは含まれず。Anthropic除外が競合排除構造を示す。
- **キーファクト:**
  - 7社が「any lawful use」に合意
  - Anthropic除外の構造的意味
  - 競合排除可能性
- **引用URL:** https://www.theguardian.com/us-news/2026/may/01/pentagon-us-military-pairs-with-spacex-google-openai

### INFO-075
- **タイトル:** Google employee backlash over Pentagon AI contract
- **ソース:** Fortune
- **公開日:** 2026-05-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Google
- **要約:** GoogleのペンタゴンAI契約で数百人の従業員が反対の公開書簡に署名。Project Maven以降、Google内部の抗議力は低下。
- **キーファクト:**
  - 数百人のGoogle従業員が反対書簡
  - Project Maven以降の抗議力低下
- **引用URL:** https://fortune.com/2026/05/04/google-employee-backlash-pentagon-ai-contract-power-waned-since-project-maven/

---

### KIQ-004-03: AI代替困難な能力・新職種

---

### INFO-076
- **タイトル:** AI Could Wipe Out Entry-Level Jobs
- **ソース:** Forbes
- **公開日:** 2026-05-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** AIがエントリーレベルの雇用を消滅させる可能性。特にマーケティング、金融、法律、ソフトウェア開発、カスタマーサービスで。ビジネスリーダーは将来のリーダー育成パイプラインの喪失を懸念すべき。
- **キーファクト:**
  - エントリーレベル雇用の消滅リスク
  - 5領域（マーケティング/金融/法律/SW開発/CS）で特に影響
  - リーダー育成パイプライン喪失の懸念
- **引用URL:** https://www.forbes.com/sites/bernardmarr/2026/05/04/ai-could-wipe-out-entry-level-jobs-and-that-should-terrify-business-leaders/

### INFO-077
- **タイトル:** Entry-level jobs calling for AI skills nearly doubled
- **ソース:** CNBC
- **公開日:** 2026-04-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** 2026年3月時点でフルタイム初期キャリア職の4.2%がAIスキルを要求。前年比ほぼ倍増。Salesforce CEOがAIエージェントが約半数のCS処理後、約4000のCS職を削減したことを確認。
- **キーファクト:**
  - 初期キャリア職のAIスキル要求: 4.2%（前年比ほぼ倍増）
  - Salesforce: AI処理で約4000CS職削減
- **引用URL:** https://www.cnbc.com/2026/04/29/entry-level-jobs-calling-for-ai-skills-nearly-doubled-from-a-year-ago-report.html

### INFO-078
- **タイトル:** Anthropic hiring 122 SWE openings while predicting replacement
- **ソース:** Reddit
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** Anthropic
- **要約:** Anthropicの上級エンジニアが2027年までにSWEが完全に置き換えられると予測した一方、同社は122のSWE求人を出しているという矛盾。
- **キーファクト:**
  - Anthropic上級エンジニア: SWE完全置き換え予測（2027年）
  - 同社は122のSWE求人中（矛盾）
- **引用URL:** https://www.reddit.com/r/ClaudeAI/comments/1t3xs80/anthropic_ai_will_fully_replace_software/

---

### KIQ-003-05: エコシステムからの離脱コスト

---

### INFO-079
- **タイトル:** GenAI Cost Attribution: Track AI Spend 2026
- **ソース:** nOps
- **公開日:** 2026-05-xx
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05, KIQ-003-01
- **関連企業:** （業界全体）
- **要約:** エンタープライズGenAI支出が2025年に3倍の$37Bに、2026年には$91.57Bに達する見込み。AIコスト管理の重要性が増大。
- **キーファクト:**
  - エンタープライズGenAI支出: 2025年$37B→2026年$91.57B見込み
  - 支出の3倍増
- **引用URL:** https://www.nops.io/blog/genai-cost-attribution-for-aws-azure-gcp/

### INFO-080
- **タイトル:** AI agent operational expenses skyrocket exponentially
- **ソース:** Instagram
- **公開日:** 2026-05-xx
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** （業界全体）
- **要約:** AIエージェントの運用コストが指数関数的に急増する研究結果。技術問題ではなくビジネス問題としての性格。
- **キーファクト:**
  - AIエージェント運用コストの指数関数的増加
- **引用URL:** https://www.instagram.com/p/DX7EpiYDiFT/
