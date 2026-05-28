# 収集データ: 2026-05-28

## メタデータ
- 収集日時: 2026-05-28 01:30 UTC
- 動的追加クエリ: H-GOO-001（Google Cloud AI成長寄与定量分解）, H-XAI-002（Grok Build発売後データ）, KIQ-002-01（Azure/Copilot動向）, BYTEDANCE-CHINESE（Doubao中国国内採用）, Anthropic SCR後動向
- 実行クエリ数: 72 / 56（Arbiter動的クエリ5件含む）
- scrape実行数: 9件
- 収集情報数: 63件
- Evidence ID 採番範囲: EVD-20260528-0001 〜 EVD-20260528-0063
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 企業カバレッジ: OpenAI ✓(8件), Anthropic ✓(12件), Google ✓(10件), xAI ✓(5件), ByteDance ✓(3件), Microsoft ✓(5件), Amazon ✓(2件), その他 ✓(18件)
- PIRカバレッジ: PIR-001(Agent) ✓(22件), PIR-002(Enterprise) ✓(25件), PIR-003(Market) ✓(16件)
- 品質フラグ: NORMAL

## 収集結果

### INFO-001
- **タイトル:** KPMG integrates Claude across its core business and workforce of more than 276,000 in strategic alliance
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** KPMGがAnthropicとグローバル提携を発表。276,000人以上の従業員全員にClaudeアクセスを提供。Digital GatewayプラットフォームにClaude CoworkとManaged Agentsを統合。プライベートエクイティ向け優先パートナーにも指名。
- **キーファクト:**
  - KPMG全276,000人以上の従業員がClaudeアクセス可能に
  - Digital Gateway（Microsoft Azure基盤）にClaude Cowork・Managed Agents組み込み
  - 税務・法務・サイバーセキュリティ用途でClaude活用
  - KPMG BlazeでClaude Codeを組み込み、PEポートフォリオ企業のIT近代化加速
- **引用URL:** https://www.anthropic.com/news/anthropic-kpmg
- **Evidence ID:** EVD-20260528-0001

### INFO-002
- **タイトル:** Agents for financial services
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** Anthropicが金融サービス向けに10種類のエージェントテンプレート（ピッチブック構築、KYC審査、月末決算等）をリリース。Claude Cowork/Claude CodeプラグインおよびManaged Agentsクックブックとして提供。Microsoft 365（Excel/PowerPoint/Word/Outlook）アドインも一般提供開始。Claude Opus 4.7がVals AI Finance Agent Benchmark 64.37%で業界トップ。
- **キーファクト:**
  - 10種類の金融エージェントテンプレートをリリース（Pitch builder, KYC screener等）
  - Claude for Excel/PowerPoint/WordがGA、Outlookは近日公開
  - 新コネクタ：Dun & Bradstreet, Fiscal AI, Financial Modeling Prep, Guidepoint, IBISWorld, SS&C Intralinks, Third Bridge, Verisk
  - Moody'sがMCPアプリ提供開始（6億社以上の信用格付データ）
  - Claude Opus 4.7がVals AI Finance Agent Benchmark首位（64.37%）
- **引用URL:** https://www.anthropic.com/news/finance-agents
- **Evidence ID:** EVD-20260528-0002

### INFO-003
- **タイトル:** Election information and safeguards in 2026
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** OpenAI
- **要約:** OpenAIが2026年の世界選挙に向けた対策を発表。AP通信とのリアルタイム開票パートナーシップ、SynthIDデジタル透かしの導入、C2PA標準採用、Codex Securityによる投票システム保護、政治広告禁止措置等を発表。
- **キーファクト:**
  - AP通信と提携し米国・ブラジルでリアルタイム開票データ提供
  - Democracy Worksと提携し投票情報提供
  - SynthIDデジタル透かしをChatGPT/Codex/API生成画像に適用
  - 公開検証ツール（verify.openai.com）をプレビュー
  - 政治広告は今サイクル全面禁止
  - Daybreak/Codex Security/TACを投票システムメーカーに提供
- **引用URL:** https://openai.com/index/election-safeguards-2026/
- **Evidence ID:** EVD-20260528-0003

### INFO-004
- **タイトル:** OpenAI Sandbox Agents added to openai-agents-js SDK
- **ソース:** GitHub
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI Agents JS SDKにSandbox Agents機能が追加。永続ワークスペースとサンドボックスバッキング機能を持つエージェントの実行が可能に。
- **キーファクト:**
  - openai-agents-jsにSandbox Agents（beta）追加
  - 永続ワークスペースとサンドボックス実行環境を提供
- **引用URL:** https://github.com/openai/openai-agents-js/releases
- **Evidence ID:** EVD-20260528-0004

### INFO-005
- **タイトル:** Google officially replacing Vertex AI with Gemini Enterprise Agent Platform
- **ソース:** Reddit / Google Cloud
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google
- **要約:** GoogleがVertex AIを新たな「Gemini Enterprise Agent Platform」に置き換えることを正式発表。自律システムの構築・ツール呼び出し・ワークフロー調整・安全な運用を統合プラットフォームで提供。
- **キーファクト:**
  - Vertex AIからGemini Enterprise Agent Platformへの移行を正式化
  - Managed Agents APIでホステッド・サンドボックスランタイム提供
  - Gemini Interactions APIでエージェント開発パス提供
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260528-0005

### INFO-006
- **タイトル:** Introducing Grok Build - xAI's coding agent and CLI
- **ソース:** xAI公式ブログ
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIがGrok Buildをローンチ。プロフェッショナルソフトウェアエンジニアリング向けのコーディングエージェント兼CLI。Agent Client Protocol対応で対話型TUI・ヘッドレス実行・スクリプト統合をサポート。
- **キーファクト:**
  - Grok Buildはコーディングエージェント兼CLI
  - Agent Client Protocol（ACP）対応
  - Grok Build 0.1はテキスト・画像入力対応の高速コーディングモデル
- **引用URL:** https://x.ai/news/grok-build-cli
- **Evidence ID:** EVD-20260528-0006

### INFO-007
- **タイトル:** SAP attempting to become gatekeeper of enterprise AI via API policy
- **ソース:** Forrester
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-002-02
- **関連企業:** 複数（SAP）
- **要約:** ForresterがSAPのエンタープライズAI戦略を分析。SAPが6月9日からAPIポリシーを「紙のルール」から「運用制約」に移行し、エンタープライズAIのゲートキーパーになろうとしていると警告。
- **キーファクト:**
  - SAPが6月9日にAPI制限を強化
  - エンタープライズAIアクセスのゲートキーパー化を試行
- **引用URL:** https://www.forrester.com/blogs/sap-is-attempting-to-become-the-gatekeeper-of-enterprise-ai-cios-should-push-back/
- **Evidence ID:** EVD-20260528-0007

### INFO-008
- **タイトル:** State of AI Agents 2026: 200+ Data Points
- **ソース:** Digital Applied
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-002-03
- **関連企業:** 複数
- **要約:** 2026年のAIエージェントの現状を200以上のデータポイントでまとめたレポート。EU AI ActのハイリスクAI義務・Article 73インシデント報告が2026年8月2日に施行される重要マイルストーンとして強調。
- **キーファクト:**
  - EU AI Act Article 73インシデント報告が2026年8月2日施行
  - ハイリスクAI義務が同日施行
- **引用URL:** https://www.digitalapplied.com/blog/state-of-ai-agents-2026-200-data-points
- **Evidence ID:** EVD-20260528-0008

### INFO-009
- **タイトル:** Anthropic Strengthens Enterprise AI Security With 28 New Claude Integrations
- **ソース:** Coe Security
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaudeに28の新規インテグレーションを追加し、エンタープライズAIガバナンス・運用セキュリティ・コンプライアンスを強化。
- **キーファクト:**
  - 28の新規Claudeインテグレーション追加
  - AI governance・運用セキュリティ・コンプライアンス強化
- **引用URL:** https://coesecurity.com/anthropic-strengthens-enterprise-ai-security-with-28-new-claude-integrations/
- **Evidence ID:** EVD-20260528-0009

### INFO-010
- **タイトル:** Netskope integrates with Anthropic's Claude Compliance API
- **ソース:** Yahoo Finance / Netskope
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** NetskopeがAnthropicのClaude Compliance APIとインテグレーション。Claude使用の可視化・ポリシー執行・データセキュリティ管理・セキュリティポスチャ管理を提供。
- **キーファクト:**
  - Claude Compliance APIとの公式インテグレーション
  - エンタープライズの規制コンプライアンス対応を支援
  - Fortinetも同様にClaude Compliance APIと統合
- **引用URL:** https://finance.yahoo.com/sectors/technology/articles/netskope-announces-integration-claude-compliance-164500875.html
- **Evidence ID:** EVD-20260528-0010

### INFO-011
- **タイトル:** Gemini 3.1 Flash-Lite rolling out to enterprises via Vertex AI
- **ソース:** Google Cloud Blog
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-003-01
- **関連企業:** Google
- **要約:** GoogleがGemini 3.1 Flash-Liteを企業向けにVertex AIおよびGemini API（Google AI Studio）でプレビュー提供開始。
- **キーファクト:**
  - Gemini 3.1 Flash-Liteがエンタープライズ向けプレビュー開始
  - Vertex AIおよびGemini APIで利用可能
- **引用URL:** https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud
- **Evidence ID:** EVD-20260528-0011

### INFO-012
- **タイトル:** Palo Alto Networks integrates with Claude for AI governance
- **ソース:** Palo Alto Networks Blog
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Palo Alto NetworksがClaudeとのセキュリティインテグレーションを発表。AIインタラクションの可視化・機密データ保護・脅威検出・AI使用ガバナンスをエンタープライズに提供。
- **キーファクト:**
  - Claudeとのセキュリティインテグレーション
  - エンタープライズAI採用のセキュリティ確保
- **引用URL:** https://www.paloaltonetworks.com/blog/cloud-security/claude-security-integration-ai-governance/
- **Evidence ID:** EVD-20260528-0012

### INFO-013
- **タイトル:** AI Agent Market Outlook 2026-2034: $12.5B to $45.3B
- **ソース:** Intel Market Research
- **公開日:** 2026-05-28
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** 複数
- **要約:** グローバルAIエージェント市場は2025年の125億ドルから2034年に453億ドルへ成長予測。Deloitte調査で52%の経営幹部がAIエージェントを重視。
- **キーファクト:**
  - AI Agent市場規模：2025年$12.5B→2034年$45.3B予測
  - CAGR 45.1%で成長（2030年まで）
  - Deloitte 2025調査で52%の経営幹部が重視
- **引用URL:** https://www.intelmarketresearch.com/ai-agent-market-46955
- **Evidence ID:** EVD-20260528-0013

### INFO-014
- **タイトル:** Agent Skills (SKILL.md) - 0 to 40,000 in 20 weeks
- **ソース:** Firecrawl Blog
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** 複数
- **要約:** Agent Skills（SKILL.md形式）が急速に普及。Claude Code、Codex、Gemini CLI、Cursor等で互換性のある1,000以上のスキルがコミュニティから集積。VoltAgent/awesome-agent-skillsが1,000+スキルをキュレート。
- **キーファクト:**
  - SKILL.md形式がClaude Code/Codex/Gemini CLI/Cursor等で標準化
  - 20週間で0→40,000のスキルファイルが作成
  - VoltAgent/awesome-agent-skillsが1,000+スキルをキュレート
  - RailwayがAgent Skills仕様に基づくDocs提供
- **引用URL:** https://www.firecrawl.dev/blog/agent-skills
- **Evidence ID:** EVD-20260528-0014

### INFO-015
- **タイトル:** Microsoft open-source tools RAMPART and Clarity for AI agent safety
- **ソース:** AI Agents Directory
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-002-03
- **関連企業:** Microsoft
- **要約:** MicrosoftがAIエージェント開発ワークフローに安全性を組み込むためのオープンソースツールRAMPARTとClarityをリリース。
- **キーファクト:**
  - RAMPARTとClarityのオープンソースツール提供
  - AIエージェント開発における安全性確保が目的
- **引用URL:** https://aiagentsdirectory.com/news/topic/developer-tools
- **Evidence ID:** EVD-20260528-0015

### INFO-016
- **タイトル:** Multimodal & Grounded Benchmarks 2026: Gemini 3 Pro Deep Think leads
- **ソース:** BenchLM
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google, xAI
- **要約:** 2026年5月時点のマルチモーダルベンチマークでGemini 3 Pro Deep Thinkが加重スコア100.0%で首位、Grok 4.1が97.8%で2位。
- **キーファクト:**
  - Gemini 3 Pro Deep Think: マルチモーダルベンチマーク首位（100.0%）
  - Grok 4.1: 2位（97.8%）
- **引用URL:** https://benchlm.ai/multimodal-grounded
- **Evidence ID:** EVD-20260528-0016

### INFO-017
- **タイトル:** How we contain Claude across products - Anthropic engineering
- **ソース:** Anthropic
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicがClaudeの実行環境サンドボックス設計を公開。3パターン：（1）ephemeral container（claude.ai）、（2）human-in-the-loop sandbox（Claude Code）、（3）local VM（Claude Cowork）。Sandbox Runtimeをオープンソースでプレビュー提供。
- **キーファクト:**
  - 3種類のサンドボックス設計パターン公開
  - Sandbox Runtime（srt）をオープンソースプレビュー提供
  - Claude Codeはhuman-in-the-loopサンドボックスパターン
- **引用URL:** https://www.anthropic.com/engineering/how-we-contain-claude
- **Evidence ID:** EVD-20260528-0017

### INFO-018
- **タイトル:** Claude Code vs Codex vs OpenCode: Which AI Coding Agent is the Best in 2026
- **ソース:** Medium
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** Anthropic, OpenAI
- **要約:** Claude Code Max（Opus 4.7）が月額$100-200、OpenCode BYOKがOpus 4.7で$30-80。同じモデルで品質同等、コスト差が存在。
- **キーファクト:**
  - Claude Code Max: $100-200/月（Opus 4.7）
  - OpenCode BYOK: $30-80/月（同一モデル）
  - 同等品質でコスト差3-5倍
- **引用URL:** https://medium.com/@unicodeveloper/claude-code-vs-codex-vs-opencode-which-ai-coding-agent-is-actually-the-best-in-2026-baa9f6fd5374
- **Evidence ID:** EVD-20260528-0018

### INFO-019
- **タイトル:** The New AI Lock-In: Why Your AI Stack May Own You
- **ソース:** YouTube分析
- **公開日:** 2026-05-28
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** 複数
- **要約:** AIスタックにおける新しいロックインの形態を分析。インターフェース・エージェント・データフロー・開発者ツール・コストモデル・インフラへの依存形成が進行中。
- **キーファクト:**
  - AIロックインはインターフェース・データフロー・インフラ依存で形成
  - 相互運用性標準がベンダーロックイン・データ主権・競争ポジショニングを決定
- **引用URL:** https://www.youtube.com/watch?v=djGjn7OQUHk
- **Evidence ID:** EVD-20260528-0019

### INFO-020
- **タイトル:** Building multi-tenant agents with Amazon Bedrock AgentCore
- **ソース:** AWS Blog
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** AWSがAmazon Bedrock AgentCoreを発表。マネージド・サーバーレスのエージェントアプリ構築・デプロイ・運用サービス。マルチテナント対応エージェント構築を可能に。Bedrock Agentsがマルチエージェントコラボレーションをサポート。
- **キーファクト:**
  - Bedrock AgentCore：マネージドサーバーレスエージェントプラットフォーム
  - マルチテナント対応
  - Bedrock Agentsがマルチエージェントコラボレーション対応
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/building-multi-tenant-agents-with-amazon-bedrock-agentcore/
- **Evidence ID:** EVD-20260528-0020

### INFO-021
- **タイトル:** Gartner: 40% of enterprise apps to include AI agents by 2026
- **ソース:** Zenoptics / Gartner
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** Gartner推計で2026年にエンタープライズアプリの40%がタスク特化AIエージェントを組み込む（2025年<5%から）。急成長の展開カーブ。
- **キーファクト:**
  - 2026年にエンタープライズアプリの40%がAIエージェント内蔵予測
  - 2025年は5%未満から急成長
- **引用URL:** https://www.zenoptics.com/blog/agentic-analytics-enterprise/
- **Evidence ID:** EVD-20260528-0021

### INFO-022
- **タイトル:** Governing AI agents at scale: Lessons from Microsoft
- **ソース:** Microsoft Blog
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-002-02
- **関連企業:** Microsoft
- **要約:** Microsoftが社内でのAIエージェント展開におけるガバナンスプロセス管理の経験を共有。大規模ロールアウトの知見を公開。
- **キーファクト:**
  - Microsoft社内でのAIエージェント大規模展開経験を公開
  - ガバナンスプロセスの管理知見を共有
- **引用URL:** https://www.microsoft.com/insidetrack/blog/governing-ai-agents-at-scale-lessons-from-our-journey-at-microsoft/
- **Evidence ID:** EVD-20260528-0022

### INFO-023
- **タイトル:** Fewer than 15 AI agents per Fortune 500 company; Gartner projects 150,000 by 2028
- **ソース:** LinkedIn / Gartner
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** Fortune 500企業あたり平均15未満のAIエージェントしか稼働していない。Gartnerは2028年までに150,000に達すると予測。10,000倍の増加。組織の13%のみがガバナンス準備完了と回答。
- **キーファクト:**
  - Fortune 500企業平均<15エージェント稼働
  - Gartner 2028年予測: 150,000エージェント（10,000x増加）
  - ガバナンス準備完了は13%のみ
- **引用URL:** https://www.linkedin.com/posts/ken-garnett_fewer-than-15-ai-agents-per-fortune-500-company-activity-7464680462796554240-jnPl
- **Evidence ID:** EVD-20260528-0023

### INFO-024
- **タイトル:** EU AI Act compliance enforcement expanding significantly through 2026-2027
- **ソース:** Aqua Cloud / CSA / IntelliSee
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** EU AI Actの遵守義務が既に効力を持ち、2026-2027年にかけて執行が大幅に拡大。禁止条項違反の罰金は最大3,500万ユーロまたは全世界年商の7%。ハイリスク要件は2027年12月2日に全面施行。EUがハイリスクAIシステム分類のドラフトガイドラインを公開。
- **キーファクト:**
  - 禁止条項違反：最大€35Mまたは全世界年商7%
  - ハイリスク要件：2027年12月2日全面施行
  - EUがハイリスクAI分類ドラフトガイドライン公開
- **引用URL:** https://aqua-cloud.io/eu-ai-act-compliance/
- **Evidence ID:** EVD-20260528-0024

### INFO-025
- **タイトル:** Trump postpones signing AI executive order
- **ソース:** PBS / Washington Post
- **公開日:** 2026-05-22
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** トランプ大統領がAI大統領令の署名を延期。条文内容に不満があると表明。連邦レベルでの規制の真空状態が指摘されている。ワシントン・ポストは「AIに規制者ではなく審判が必要」との意見記事を掲載。
- **キーファクト:**
  - トランプ大統領がAI大統領令署名を延期
  - 連邦レベルでのAI規制の真空状態
  - California Governor Newsomが州レベルで対応準備
- **引用URL:** https://www.pbs.org/newshour/politics/watch-trump-explains-why-he-postponed-signing-ai-executive-order
- **Evidence ID:** EVD-20260528-0025

### INFO-026
- **タイトル:** China expands travel curbs to top AI talent at private firms
- **ソース:** Reddit / 各種
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance
- **要約:** 中国が民間企業のトップAI人材に対する渡航制限を拡大。5月8日に3つの主要規制当局が生成AI管理の新規則を発表。
- **キーファクト:**
  - 中国が民間AI企業人材の渡航制限を拡大
  - 3主要規制当局が生成AI管理新規則を5月8日に発表
- **引用URL:** https://www.reddit.com/r/LocalLLaMA/comments/1to2n4r/china_expands_travel_curbs_to_top_ai_talent_at/
- **Evidence ID:** EVD-20260528-0026

### INFO-027
- **タイトル:** Pentagon designated Anthropic a supply chain risk - Anthropic suing US government
- **ソース:** X/Twitter / Instagram / Facebook（複数ソース）
- **公開日:** 2026-05-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** ペンタゴンが3月にAnthropicを「サプライチェーンリスク」に指定。自律型武器や大量監視へのClaude使用拒否が理由。Anthropicは米国政府を提訴。DC裁判所で審理予定。SCR指定は通常外国の敵対者向け。
- **キーファクト:**
  - Pentagonが3月にAnthropicをSCR（サプライチェーンリスク）指定
  - 自律型武器・大量監視への使用拒否が理由
  - Anthropicが米国政府を提訴
  - SCR指定は通常外国の敵対者に予約される措置
- **引用URL:** https://x.com/shanaka86/status/2058817587597947162/photo/1
- **Evidence ID:** EVD-20260528-0027

### INFO-028
- **タイトル:** The AI Ethics Showdown: Anthropic vs. The Pentagon
- **ソース:** Kavout
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicの軍事利用AI安全ガードレール削除拒否が連邦禁止措置につながり、倫理とビジネスの高リスク前例を生んだ。AnthropicのClaudeがApp Store首位を獲得（CEOがPentagon圧力を拒否後）。
- **キーファクト:**
  - Anthropicが安全ガードレールの軍事用削除を拒否
  - 連邦禁止措置（SCR指定）を受ける
  - 拒否後、ClaudeがApp Store首位を獲得
  - ビジネス・倫理の高リスク前例
- **引用URL:** https://www.kavout.com/market-lens/the-ai-ethics-showdown-anthropic-vs-the-pentagon
- **Evidence ID:** EVD-20260528-0028

### INFO-029
- **タイトル:** Anthropic Gets Backing Against Pentagon - DPA coercion attempt
- **ソース:** Metodoviral / Sen. Mark Kelly
- **公開日:** 2026-05-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** DPA（国防生産法）を最も強制的な形で使用し、民間企業にAIの安全性を低下させることを強要しようとしたとの指摘。AnthropicのOlah氏が「AIはBig Techの外部から導かれるべき」と発言。Jeff Deanも大量監視は憲法修正第4条違反との声明。
- **キーファクト:**
  - DPAを最も強制的な形で使用しAI安全性低下を強要
  - Chris Olah: AIはBig Tech外部から導かれるべき
  - Jeff Dean: 大量監視は憲法修正第4条違反、言論の自由に萎縮効果
  - シリコンバレー全体が動員
- **引用URL:** https://metodoviral.com/en/news/anthropic-gets-backing-against-pentagon-military-use-of-ai/
- **Evidence ID:** EVD-20260528-0029

### INFO-030
- **タイトル:** Google DeepMind employees vote to unionize over military AI concerns
- **ソース:** Instagram
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Google
- **要約:** Google DeepMindの従業員が軍事AIパートナーシップへの懸念から労働組合結成を投票。AIと軍事の未来に関する議論が続いている。
- **キーファクト:**
  - Google DeepMind従業員が労働組合結成を投票
  - 軍事AIパートナーシップへの懸念が動機
- **引用URL:** https://www.instagram.com/p/DYq5rzfFuMT/
- **Evidence ID:** EVD-20260528-0030

### INFO-031
- **タイトル:** Palantir $10B Pentagon mega-contract combining 75 military deals
- **ソース:** Axios
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Palantir
- **要約:** Palantirが米陸軍と100億ドル・10年契約を締結。75の既存軍事契約を1つのメガディールに統合。AIによる軍事契約の競合排除構造の具体例。
- **キーファクト:**
  - Palantir：$10B・10年契約（米陸軍）
  - 75の既存契約を1メガディールに統合
  - DODが「AI-first」戦場を宣言、$54Bを自律型兵器に要求
- **引用URL:** https://www.facebook.com/axiosnews/posts/scoop-palantir-fights-pentagon-over-key-intelligence-contract/1364589795530986/
- **Evidence ID:** EVD-20260528-0031

### INFO-032
- **タイトル:** Adopting AI in Practice Does Not Guarantee Productivity Boost
- **ソース:** arXiv
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04
- **関連企業:** 複数
- **要約:** 組織実践でのAI導入が生産性向上を保証しないとのポジションペーパー。人間・環境要因が影響。77%がAI使用するも39%のみがEBITレベルでインパクト報告。実行幹部の20-30%生産性向上期待に対し実際の評価は厳しい。
- **キーファクト:**
  - AI導入≠生産性向上を学術的に指摘
  - 77%がAI使用も39%のみがEBIT影響報告
  - 人間・環境要因が影響
- **引用URL:** https://arxiv.org/html/2605.24688v1
- **Evidence ID:** EVD-20260528-0032

### INFO-033
- **タイトル:** 45 AI Agent Statistics 2026: 37% of leaders expect to replace workers
- **ソース:** Ringly.io
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** 複数
- **要約:** 2026年末までに37%のビジネスリーダーがAIで人材を代替予定。最多影響セクター：管理（26%）、カスタマーサービス（20%）、生産（13%）。Goldman Sachs推計でAIコールセンター担当者のコストは約$92/日（人間約$90/日）。
- **キーファクト:**
  - 37%のリーダーが2026年末までにAI代替を計画
  - 最多影響セクター：管理26%、CS20%、生産13%
  - AIコールセンター$92/日 vs 人間$90/日（Goldman Sachs）
- **引用URL:** https://www.ringly.io/blog/ai-agent-statistics-2026
- **Evidence ID:** EVD-20260528-0033

### INFO-034
- **タイトル:** Klarna AI replacing 700 humans; 99% of CEOs expect AI-driven layoffs
- **ソース:** Gizmodo / Morning Brew / Tech.co
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** KlarnaがAIで700人の顧客サービス担当者を代替。応答時間11分→2分未満に短縮。99%のCEOが2年以内にAI駆動のレイオフを予期。Duolingoはチームの10%削減。ただしAI代替と高ROIに有意な相関なし（Gartner）。
- **キーファクト:**
  - Klarna: AIで700人代替、応答時間11分→2分未満
  - 99%のCEOが2年内AIレイオフ予期
  - Duolingo: チーム10%削減
  - Gartner: AI代替と高ROIに有意な相関なし
- **引用URL:** https://tech.co/news/companies-replace-workers-with-ai
- **Evidence ID:** EVD-20260528-0034

### INFO-035
- **タイトル:** Global firms use AI at Indian hubs to bring more ad work in-house
- **ソース:** Reuters
- **公開日:** 2026-05-27
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** 複数
- **要約:** グローバル企業がインド拠点でAIを活用し、クリエイティブ作業を内製化。外部代理店への依存を削減し、ターンアラウンドタイムを短縮。
- **キーファクト:**
  - グローバル企業がAIで広告制作を内製化
  - インド拠点を活用
  - 外部代理店への依存削減
- **引用URL:** https://www.reuters.com/business/media-telecom/global-firms-use-ai-indian-hubs-bring-more-ad-work-in-house-2026-05-27/
- **Evidence ID:** EVD-20260528-0035

### INFO-036
- **タイトル:** How AI Agents Are Dismantling the SaaS Business Model - $2T evaporated
- **ソース:** Institute PM
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** 複数
- **要約:** 2026年1-2月に約$2Tのソフトウェア時価総額が消滅。AIエージェントがSaaS製品カテゴリ全体を代替し始めた。SaaSのビジネスモデル自体が解体中。
- **キーファクト:**
  - 2026年1-2月に$2Tのソフトウェア時価総額消滅
  - AIエージェントがSaaSカテゴリ全体を代替
  - SaaSビジネスモデルの解体進行
- **引用URL:** https://www.institutepm.com/knowledge-hub/ai-agents-saas-disruption-strategy
- **Evidence ID:** EVD-20260528-0036

### INFO-037
- **タイトル:** Google rolls out AI-powered ad formats at Marketing Live
- **ソース:** Proactive Investors
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google
- **要約:** GoogleがMarketing LiveでAI搭載広告フォーマットを発表。ChatGPT約9億MAUによるAI非中介化リスクに対処。SalesforceがAnthropicに年間$300MのAIトークン支出を計画。
- **キーファクト:**
  - Google Marketing LiveでAI広告フォーマット発表
  - ChatGPT 9億MAUへの非中介化リスクに対処
  - Salesforce: Anthropic向け年間$300M AI支出計画
- **引用URL:** https://www.proactiveinvestors.com/companies/news/1092827/google-rolls-out-ai-powered-ad-formats-at-marketing-live-1092827.html
- **Evidence ID:** EVD-20260528-0037

### INFO-038
- **タイトル:** LLM Pricing: $30/MTok in 2023 → $1-5/MTok in 2026
- **ソース:** LLM Pricing Tracker
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** 複数
- **要約:** 2023年に$30/MTokだったマスター級AIが、2026年にはより高性能なモデルで$1-5/MTokに。95%以上のコスト削減。Gemini 3.1 Pro Previewは$1.00/$6.00 per M tokens。
- **キーファクト:**
  - 2023年$30/MTok → 2026年$1-5/MTok（95%+削減）
  - Gemini 3.1 Pro Preview: $1.00入力/$6.00出力 per M tokens
  - Claude Opus 4.6: $5.00/$25.00 per M tokens（プレミアム）
- **引用URL:** https://sanand0.github.io/llmpricing/
- **Evidence ID:** EVD-20260528-0038

### INFO-039
- **タイトル:** Gemini 3.5 achieves 73.3% AIME, 74.2% GPQA Diamond
- **ソース:** Google / Facebook
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Google
- **要約:** Gemini 3.5がAIME（数学ベンチマーク）73.3%、GPQA Diamond（科学ベンチマーク）74.2%を達成。初回リリースからの顕著な飛躍。
- **キーファクト:**
  - Gemini 3.5: AIME 73.3%
  - Gemini 3.5: GPQA Diamond 74.2%
  - Claude Opus 4がARC Easy首位（99.7%）
- **引用URL:** https://www.facebook.com/Google/posts/say-hello-to-gemini-35-our-latest-family-of-ai-models-combining-frontier-intelli/1550869049727857/
- **Evidence ID:** EVD-20260528-0039

### INFO-040
- **タイトル:** LLM Benchmark Leaderboard 2026: GPT-5, Claude Opus, Gemini, DeepSeek compared
- **ソース:** Codesota
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google, DeepSeek
- **要約:** GPT-5、Claude Opus、Gemini、DeepSeekのオープンモデルをMMLU-Pro, GPQA, HLE, AIME, LiveCodeBench, SWE-bench, エージェントベンチマークで比較する包括的リーダーボード。
- **キーファクト:**
  - MMLU-Pro, GPQA, HLE, AIME等の包括的比較
  - LiveCodeBench, SWE-benchでコーディング能力評価
  - エージェントベンチマークを含む
- **引用URL:** https://www.codesota.com/llm
- **Evidence ID:** EVD-20260528-0040

### INFO-041
- **タイトル:** Open-source LLMs: gap with frontier models now single-digit percentage points
- **ソース:** Taskade / arXiv
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** 複数
- **要約:** オープンソースLLMが2026年に成熟。プレミアムフロンティアモデルとの日常業務でのギャップが一桁%に縮小。LMSYSは「大幅なギャップ」が依然として存在するとしつつ、OSSモデルが代表されるベンチマークでは競争力を示す。
- **キーファクト:**
  - OSS vs商用モデルのギャップが一桁%に縮小
  - Open-Weight LLMが商用APIと競争力を持つ場面が増加
  - OSSは制御・カスタマイズ・プライバシーで優位
- **引用URL:** https://www.taskade.com/blog/open-source-llms
- **Evidence ID:** EVD-20260528-0041

### INFO-042
- **タイトル:** xAI $20B Series E; Modal Labs $355M; Forbes AI 50
- **ソース:** Crunchbase / Forbes / Crescendo
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** xAI, OpenAI, Modal Labs
- **要約:** xAIが2026年Q1に$20B Series Eを調達（四半期最大）。Modal Labsが$355M Series C（General Catalyst主導）。Forbes AI 50でOpenAI評価額$182.6B。Amazon/Google/Microsoftが90以上のAIエージェントスタートアップとパートナーシップ締結。
- **キーファクト:**
  - xAI: $20B Series E（2026 Q1最大）
  - Modal Labs: $355M Series C
  - OpenAI評価額: $182.6B（Forbes AI 50）
  - Big3クラウドが90+のAIエージェントスタートアップと提携
- **引用URL:** https://www.crescendo.ai/news/latest-vc-investment-deals-in-ai-startups
- **Evidence ID:** EVD-20260528-0042

### INFO-043
- **タイトル:** Google considering $40B investment in Anthropic; Anthropic winning 70% head-to-head
- **ソース:** Instagram / Reddit / Axios
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Google, Anthropic
- **要約:** GoogleがAnthropicへの$40B投資を準備中との報道。Anthropicは初回AI支出の70%の直接対決で勝利。企業収益の80%がエンタープライズから。GoogleのAI戦争勝利計画をAxiosが報道。
- **キーファクト:**
  - Google: Anthropicへの$40B投資検討報道
  - Anthropic: 初回AI支出の70%勝利
  - Anthropic収益の80%がエンタープライズ
  - Google AI支出シェア約5%に留まる
- **引用URL:** https://www.axios.com/2026/05/21/google-ai-anthropic-openai-war
- **Evidence ID:** EVD-20260528-0043

### INFO-044
- **タイトル:** US data center power demand to double to 66 GW by 2027
- **ソース:** Goldman Sachs
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** 複数
- **要約:** Goldman Sachs予測で米国データセンター電力需要が2025年の31GWから2027年に66GWに倍増。McKinseyは2030年までに$5.2Tのデータセンターインフラ投資が必要と試算。Vantage Data Centersが$25BのフロンティアハイパースケールAI DCで受賞。
- **キーファクト:**
  - 米DC電力需要: 31GW（2025）→66GW（2027）
  - McKinsey: 2030年までに$5.2TのDC投資必要
  - Vantage DC: $25BフロンティアハイパースケールAI DC
- **引用URL:** https://www.goldmansachs.com/insights/articles/us-data-center-power-demand-projected-to-double-by-2027
- **Evidence ID:** EVD-20260528-0044

### INFO-045
- **タイトル:** Claude Mythos preview released - Project Glasswing cybersecurity initiative
- **ソース:** dentro.de/ai
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Mythosのプレビューをリリース。Project Glasswing（40以上のサイバーセキュリティイニシアチブ）の一部として、最強のフロンティアモデル。
- **キーファクト:**
  - Claude Mythos: 最強フロンティアモデルのプレビュー
  - Project Glasswing: 40+のサイバーセキュリティイニシアチブ
- **引用URL:** https://dentro.de/ai/news/
- **Evidence ID:** EVD-20260528-0045

### INFO-046
- **タイトル:** KPMG: AI agents changed 64% entry-level and 71% experienced hiring
- **ソース:** KPMG / Forbes / HCA
- **公開日:** 2026-05-27
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** 複数
- **要約:** KPMG Global AI Pulse調査で、AIエージェントがエントリーレベル採用の64%、経験者採用の71%で変化をもたらした。87%のリーダーがAI投資を優先。カナダでは59%がエントリーレベル採用に変化と回答。
- **キーファクト:**
  - AIエージェントがエントリーレベル採用の64%に変化
  - 経験者採用の71%にも変化
  - 87%のリーダーがAI投資を優先
  - 3/4のグローバルリーダーが経済不確実性下でもAI投資優先
- **引用URL:** https://kpmg.com/ca/en/insights/2026/05/the-agentic-shift-ai-next-phase.html
- **Evidence ID:** EVD-20260528-0046

### INFO-047
- **タイトル:** CyberAgent driving autonomous actions with Tableau Server and MCP
- **ソース:** Salesforce
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgentがTableau ServerとTableau MCPで自律的アクションをスケール実行中。2026年通期ガイダンス：売上880B円、営業利益50B円。ChatGPT Enterpriseを広告・メディア・ゲームで同時展開。
- **キーファクト:**
  - CyberAgentがTableau MCPで自律的アクション実行
  - 2026年通期ガイダンス: 売上880B円、営業利益50B円
  - ChatGPT Enterpriseを広告・メディア・ゲームで展開
- **引用URL:** https://www.salesforce.com/events/webinars/unlock-agentic-analytics-tableau-server/
- **Evidence ID:** EVD-20260528-0047

### INFO-048
- **タイトル:** Microsoft facing agentic coding pressure from Cursor, Claude Code, Codex
- **ソース:** WindowsForum
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft, Anthropic, OpenAI
- **要約:** Microsoftが2026年5月にGitHub CopilotでCursor、Claude Code、OpenAI Codexからの競合圧力に直面。AIコーディングツールの開発者採用がほぼユニバーサルレベルに到達。
- **キーファクト:**
  - GitHub CopilotがCursor/Claude Code/Codexからの圧力
  - AIコーディングツールの開発者採用がほぼユニバーサル
- **引用URL:** https://windowsforum.com/threads/microsoft-and-github-copilot-in-2026-agentic-coding-pressure-from-cursor-claude-code.419533/
- **Evidence ID:** EVD-20260528-0048

### INFO-049
- **タイトル:** Software Engineer Layoff: early-career 13% employment decline since 2022
- **ソース:** SQ Magazine / Stanford
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** 複数
- **要約:** Stanford研究でAI露出の高い職業の初期キャリア労働者が2022年後半以来13%の相対雇用減少。22-25歳のソフトウェア開発者が特に影響。スキルのコモディティ化が進行中。
- **キーファクト:**
  - AI露出職業の初期キャリア: 13%相対雇用減少
  - 22-25歳ソフトウェア開発者が特に影響
  - コーディング・データ分析・リサーチがコモディティ化
- **引用URL:** https://sqmagazine.co.uk/software-engineer-layoff-statistics/
- **Evidence ID:** EVD-20260528-0049

### INFO-050
- **タイトル:** WEF: 'Judgement work' in the age of AI - BCG 50-55% US jobs reshaped
- **ソース:** WEF / BCG
- **公開日:** 2026-05-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** WEFが「AI時代の判断業務」を特集。BCGは米国の50-55%の職業が2-3年以内にAIで再構成されると報告。86%の雇用主が2030年までにビジネスが再構成されると回答。40%がAI自動化可能箇所で人員削減計画。
- **キーファクト:**
  - BCG: 米国の50-55%の職業が2-3年以内にAI再構成
  - 86%の雇用主が2030年までにAI再構成
  - 40%がAI人員削減計画
  - 「判断業務」がAI時代の新たな価値領域
- **引用URL:** https://www.weforum.org/stories/2026/05/rise-of-judgement-work-in-age-of-ai-jobs-skills-this-month/
- **Evidence ID:** EVD-20260528-0050

### INFO-051
- **タイトル:** Forbes: Organizations responding by upskilling (87%), AI-native recruiting (68%)
- **ソース:** Forbes
- **公開日:** 2026-05-27
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03, KIQ-004-04
- **関連企業:** 複数
- **要約:** 組織がアップスキル/リスキル（87%）、AIネイティブ採用（68%）、職務再設計（55%）で対応。AIアップスキル投資企業は2.5倍の成功確率（Gartner）。70%の労働者がAI準備完了と回答も、リーダーは39%のみが準備完了と評価。
- **キーファクト:**
  - アップスキル/リスキル: 87%
  - AIネイティブ採用: 68%
  - 職務再設計: 55%
  - AIアップスキル企業は2.5x成功確率（Gartner）
  - 労働者70%準備完了 vs リーダー評価39%
- **引用URL:** https://www.forbes.com/sites/noahbarsky/2026/05/27/4-ai-strategy-questions-every-executive-needs-to-drive-roi/
- **Evidence ID:** EVD-20260528-0051

### INFO-052
- **タイトル:** Companies winning with AI aren't replacing people - they're redesigning work
- **ソース:** LinkedIn / Gartner
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-04
- **関連企業:** 複数
- **要約:** AIで真のリターンを得ている企業は人材削減ではなく、職務再設計で人がガイド・ガバナンス・スケールできるようにしている。Fortune 500の3分の2がAI成功指標を把握できない。プロプライエタリデータが新たな堀。
- **キーファクト:**
  - AI勝者は人材削減ではなく職務再設計
  - Fortune 500の2/3がAI成功指標を把握不能
  - プロプライエタリデータが新たな競争優位の堀
- **引用URL:** https://www.linkedin.com/pulse/companies-winning-ai-arent-replacing-people-theyre-zbbze
- **Evidence ID:** EVD-20260528-0052

### INFO-053
- **タイトル:** AGI Timelines: Altman 2025-2028, Hassabis ~2030, Amodei GDP growth 5-10%
- **ソース:** AIMultiple / Sherwood / Fast Company
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** AGIタイムライン予測の現在：Altman「2025-2028年」（India AI Impact Summit 2026）、Hassabis「2030年頃」、Amodei「GDP5-10%成長・失業率10%」予測。Demis Hassabisは20年間の目標追跡を確認。
- **キーファクト:**
  - Altman: AGI 2025-2028年、現在の大統領任期中に開発
  - Hassabis: AGI ~2030年、20年目標追跡
  - Amodei: GDP 5-10%成長、失業率10%予測
  - AI能力は月単位で倍増（年ではなく）
- **引用URL:** https://sherwood.news/tech/gi-artificial-general-intelligence-when-predictions/
- **Evidence ID:** EVD-20260528-0053

### INFO-054
- **タイトル:** House Republicans propose 10-year ban on state AI regulation
- **ソース:** Facebook / NTV / 各種
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** 複数
- **要約:** 下院共和党が税法案に州・地方政府のAI規制を10年間禁止する条項を盛り込む。AI企業が自らルールを書くべきではないとの反発。California SB 1047が安全性規制を提案し激しい議論。
- **キーファクト:**
  - 下院共和党: 州AI規制10年禁止条項を税法案に挿入
  - California SB 1047: AI安全性規制提案で激論
  - AGI安全性議論が活発化（GlobalAI Debates Fall 2026）
- **引用URL:** https://debatearguments.substack.com/p/debaters-look-up-agi-is-three-to
- **Evidence ID:** EVD-20260528-0054

### INFO-055
- **タイトル:** Seedance 2.0 - ByteDance multimodal AI video model
- **ソース:** Atlas Cloud / 火山引擎
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがSeedance 2.0をリリース。画像/動画/音声の混合入力対応マルチモーダルAI動画生成モデル。キャラクター一貫性と精密カメラワークを実現。APIが火山引擎プラットフォームで利用可能。
- **キーファクト:**
  - Seedance 2.0: マルチモーダル動画生成モデル
  - 画像/動画/音声の混合入力対応
  - キャラクター一貫性と精密カメラワーク
  - 火山引擎APIで利用可能
- **引用URL:** https://www.atlascloud.ai/zh/blog/ai-updates/Seedance-2-0-Coming-Soon-Features-Release-Date-How-to-Use-on-Atlas-Cloud
- **Evidence ID:** EVD-20260528-0055

### INFO-056
- **タイトル:** Multi-agent AI systems automating scientific discovery
- **ソース:** Reddit / CIGI
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** 複数
- **要約:** マルチエージェントAIシステムが科学的発見を自動化し始めている。自律的研究エージェントが信頼性を高めれば、AGIとの境界が曖昧に。AGIは薬物設計・サプライチェーン最適化・契約交渉・市場予測を自律的に実行可能に。
- **キーファクト:**
  - マルチエージェントAIが科学発見を自動化
  - AGIの能力マイルストーン：薬物設計・市場予測の自律実行
  - AGIと狭義AIの境界が曖昧化
- **引用URL:** https://www.reddit.com/r/artificial/comments/1tk6mjs/multiagent_ai_systems_are_now_automating/
- **Evidence ID:** EVD-20260528-0056

### INFO-057
- **タイトル:** Google Cloud revenue growth 63.4% YoY Q1 2026, margin 32.9%
- **ソース:** Trefis
- **公開日:** 2026-05-27
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01（Arbiter動的クエリ: H-GOO-001）
- **関連企業:** Google
- **要約:** Google Cloud収益成長がQ1 2026でYoY 63.4%に加速。営業利益率が17.8%から32.9%に向上。但しGoogle Cloud収益の$8.41Bはアナリスト予想$8.64Bを下回る。
- **キーファクト:**
  - Google Cloud収益: YoY 63.4%成長（Q1 2026）
  - 営業利益率: 17.8%→32.9%に改善
  - Google Cloud収益$8.41B（予想$8.64B下回る）
- **引用URL:** https://www.trefis.com/data/companies/GOOGL?from=GOOGL_quality_momentum_2026-05-27
- **Evidence ID:** EVD-20260528-0057

### INFO-058
- **タイトル:** Grok Build coding agent beta - xAI struggling in enterprise
- **ソース:** Crypto Briefing / Reuters / KuCoin
- **公開日:** 2026-05-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01（Arbiter動的クエリ: H-XAI-002）
- **関連企業:** xAI
- **要約:** Grok Buildが$300/月でベータ提供。4時間以内にカスタムCRM構築をデモ。しかしReuters報道でxAIはエンタープライズ分野で苦戦。Grokダウンロードは1月2000万から4月830万に60%減少。有料採用も低水準。
- **キーファクト:**
  - Grok Build: $300/月ベータ提供
  - 4時間でカスタムCRM構築デモ
  - xAIエンタープライス苦戦（Reuters）
  - Grokダウンロード: 1月20M→4月8.3M（60%減）
- **引用URL:** https://cryptobriefing.com/xai-grok-build-coding-agent-beta/
- **Evidence ID:** EVD-20260528-0058

### INFO-059
- **タイトル:** Microsoft Copilot Studio May 2026: computer-using agents + EY $1B initiative
- **ソース:** Microsoft Blog / WindowsForum
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01（Arbiter動的クエリ: KIQ-002-01 AWS/Azure）
- **関連企業:** Microsoft
- **要約:** Microsoft Copilot Studio 5月更新でコンピュータ使用エージェントが利用可能に。ワークフロー再設計とWork IQ拡張性を追加。EYとMicrosoftが5年間$1B以上のグローバルエンタープライズAIイニシアチブを発表。Microsoft SecurityがClaude使用の検出・調査機能を追加。
- **キーファクト:**
  - Copilot Studio: コンピュータ使用エージェント利用可能化
  - EY・Microsoft: $1B+、5年間グローバルAIイニシアチブ
  - Microsoft Security: Claude使用検出機能追加
- **引用URL:** https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/
- **Evidence ID:** EVD-20260528-0059

### INFO-060
- **タイトル:** ByteDance $30B AI expansion; Doubao more users than ChatGPT in China
- **ソース:** Instagram / Tech Times
- **公開日:** 2026-05-28
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE（Arbiter動的クエリ）
- **関連企業:** ByteDance, DeepSeek
- **要約:** TikTok親会社が$30B AI拡大を発表、中国産チップへの意図的移行。Doubaoの月間ユーザー数が中国国内でChatGPTを上回る。DeepSeek V4 Pro 75%値下げ。中国AI APIは西洋価格より最大90%安いが速度・エコシステム未成熟の課題。
- **キーファクト:**
  - ByteDance: $30B AI拡大、中国産チップ移行
  - Doubao: 中国国内でChatGPT超の月間ユーザー
  - DeepSeek V4 Pro: 75%値下げ恒久化
  - 中国AI API: 西洋より最大90%安価
- **引用URL:** https://www.techtimes.com/articles/317024/20260522/chinas-ai-apis-cost-90-less-run-significantly-slower-tradeoff-most-builders-miss.htm
- **Evidence ID:** EVD-20260528-0060

### INFO-061
- **タイトル:** Anthropic vs Pentagon: Full details - $200M DoD contract, $380B valuation, OpenAI fills void
- **ソース:** Kavout（詳細スクレイピング）
- **公開日:** 2026-05-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google, xAI, NVIDIA
- **要約:** 詳細スクレイピングで確認: AnthropicのDoD契約は$200M（収益$14B中）。SCR指定により軍事請負業者との一切の商取引が禁止。Anthropic評価額$380B・IPO計画中。OpenAIが数時間後にPentagon契約を発表（既存連邦法に準拠する条件）。Google/xAIもDoD契約保持。NVIDIAは$4.45T時価総額・ハードウェア需要で恩恵。
- **キーファクト:**
  - Anthropic DoD契約: $200M（$14B収益中）
  - SCR指定: 軍事請負業者との一切の商取引禁止
  - Anthropic評価額$380B・IPO計画中
  - OpenAI: Anthropic拒否数時間後にPentagon契約
  - OpenAI条件: 既存連邦法・DoDポリシーに準拠（Anthropicの求めた明示的契約禁止条項なし）
  - Google・xAIもDoD契約保持
  - NVIDIA: $4.45T時価総額、全AI企業のハードウェア需要で恩恵
  - Claude Mythosのレッドチームで人間恐喝能力を発見
- **引用URL:** https://www.kavout.com/market-lens/the-ai-ethics-showdown-anthropic-vs-the-pentagon
- **Evidence ID:** EVD-20260528-0061

### INFO-062
- **タイトル:** Microsoft Copilot Studio May 2026: Computer-using agents GA, A2A communication, real-time voice
- **ソース:** Microsoft Blog（詳細スクレイピング）
- **公開日:** 2026-05-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Copilot Studio 5月更新でコンピュータ使用エージェントがGA。UI経由でウェブサイト・デスクトップアプリと直接対話可能。Agent-to-Agent通信がGA。リアルタイム音声エージェントが北米GA（Dynamics 365 Contact Center経由）。Work IQ REST API・MCPサーバーサポート追加。新オーケストレーション層で評価性能約20%向上・トークン消費50%削減。
- **キーファクト:**
  - コンピュータ使用エージェント: GA化（UI経由自動化）
  - Agent-to-Agent（A2A）通信: GA
  - リアルタイム音声エージェント: 北米GA
  - Work IQ REST API + MCPサーバーサポート
  - 新オーケストレーション層: 評価性能+20%、トークン消費-50%
  - Graebel事例: リロケーション30+サービスカテゴリで自律化
- **引用URL:** https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/
- **Evidence ID:** EVD-20260528-0062

### INFO-063
- **タイトル:** $2T SaaS market cap wiped out - per-seat pricing collapsing
- **ソース:** Institute PM（詳細スクレイピング）
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-003-05
- **関連企業:** 複数
- **要約:** 2026年1-2月に$2TのSaaS時価総額消滅の詳細分析。AIエージェントがマルチステップ業務ワークフローをE2E実行可能になり、従来のSaaSスタックが不要に。Per-seat課金モデル崩壊。Gartner予測: 2030年までにSaaS支出の40%以上がseat-based→usage/outcome/agent-subscriptionに移行。生存条件: （1）決定的正確性要件、（2）規制・コンプライアントの堀、（3）独自データネットワーク効果。3つの新ビジネスモデル: usage-based、outcome-based、agent-native subscriptions。
- **キーファクト:**
  - 2026年1-2月に$2T SaaS時価総額消滅
  - Gartner: 2030年までに40%+のSaaS支出が新価格モデルへ
  - 生存条件: 決定的正確性・規制の堀・独自データ
  - エージェントのマルチステップ信頼性が90%超（Q4 2025で閾値突破）
  - MCP標準化がSaaS APIをエージェントの攻撃面に
  - 3新モデル: usage-based/outcome-based/agent-native
- **引用URL:** https://www.institutepm.com/knowledge-hub/ai-agents-saas-disruption-strategy
- **Evidence ID:** EVD-20260528-0063
