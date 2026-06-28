# 収集データ: 2026-06-28

## メタデータ
- 収集日時: 2026-06-28 00:30 UTC
- 実行クエリ数: 42 / collection_plan全件 + 動的追加3件
- scrape実行数: 5件（Anthropic Claude Corps, Anthropic SKT, OpenAI GPT-5.6 Sol, CNBC, Anthropic Fable/Mythos）
- 収集情報数: 80件
- Evidence ID 採番範囲: EVD-20260628-0001 〜 EVD-20260628-0080
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-06 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓, KIQ-MIL-001 (動的) ✓, H-ANT-002-DAU (動的) ✓
- 動的追加クエリ:
  1. "Grok AI military targeting selection human override rate Pentagon Department of Defense" (KIQ-MIL-001)
  2. "xAI Grok government targeting doctrine AI weapons systems involvement" (KIQ-MIL-001)
  3. "Claude Code daily active users DAU installation numbers adoption metrics" (H-ANT-002)
- 品質フラグ: NORMAL

## 収集結果

### INFO-001
- **タイトル:** Introducing Claude Corps - Anthropic launches national AI fellowship program
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-04, KIQ-004-03, KIQ-004-04
- **関連企業:** Anthropic
- **要約:** Anthropicが「Claude Corps」を発表。初期投資$150Mで全米の非営利団体に1000人のAIフェローを配置。若年層のAIスキル育成と社会課題解決を同時に狙う。年収$85K+福利厚生、12ヶ月間フルタイム。
- **キーファクト:**
  - 初期投資$150M、1000人のフェロー、400以上の非営利団体ホスト
  - CodePath（公式雇用主）・Social Finance（評価・財務）との3者提携
  - AIが労働市場にもたらす変化への責任投資を明示
- **引用URL:** https://www.anthropic.com/news/claude-corps
- **Evidence ID:** EVD-20260628-0001

### INFO-002
- **タイトル:** Pentagon used Grok AI to direct 2,000 munitions against Iran targets in 96 hours
- **ソース:** Social media reports citing Pentagon sworn court statement
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001 (動的追加)
- **関連企業:** xAI
- **要約:** PentagonのAI責任者が宣誓法廷声明で、Elon MuskのGrok AIがイラン攻撃の標的選定に使用され、96時間以内に2,000の標的に対して2,000発の弾薬を発射したと明らかにした。
- **キーファクト:**
  - Grok AIが2,000標的の選定に関与、96時間で2,000発の弾薬使用
  - Pentagon責任者の宣誓法廷声明として提出
  - 人間の却下比率は声明に含まれていない（KIQ-MIL-001未回答継続）
- **引用URL:** https://www.facebook.com/OfficialRehamKhan/posts/1547399583421109
- **Evidence ID:** EVD-20260628-0002

### INFO-003
- **タイトル:** Pentagon quietly updated classified joint targeting doctrine for AI
- **ソース:** Social media / news aggregation
- **公開日:** 2026-06-26
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** xAI, OpenAI, Anthropic
- **要約:** PentagonがAIを組み込んだ秘密の共同標的選定ドクトリンを静かに更新。White HouseはAI採用加速を命令、PentagonはAI搭載・自律型兵器システムの新ルールを準備中。
- **キーファクト:**
  - 分類された共同標的選定ドクトリンがAI用に更新
  - 自律型兵器システムの新ルール策定プロセス開始
  - Claude embedded in Mavenという言及あり（Anthropicの軍事利用）
- **引用URL:** https://www.instagram.com/p/DaDXD9lk28n/
- **Evidence ID:** EVD-20260628-0003

### INFO-004
- **タイトル:** OpenAI shipped 30+ models in 6 months via API
- **ソース:** OpenAI Devs (LinkedIn), 公式発表
- **公開日:** 2026-06-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIが過去6ヶ月で30以上のモデルと機能をリリース。メインラインGPTモデル、リアルタイム音声、画像など12以上のモデルをAPI経由で提供。
- **キーファクト:**
  - 6ヶ月で30+モデル/機能リリース
  - 12以上のAPIモデル（GPT、リアルタイム音声、画像）
  - コスト・レイテンシ最適化モデル提供
- **引用URL:** https://www.linkedin.com/posts/openai-devs_over-the-past-six-months-we-shipped-30-activity-7475265584939749376-0_Ht
- **Evidence ID:** EVD-20260628-0004

### INFO-005
- **タイトル:** Google Interactions API reaches General Availability - unified endpoint for Gemini models and agents
- **ソース:** Google AI Blog (公式)
- **公開日:** 2026-06-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Google
- **要約:** GoogleがInteractions APIをGA（一般提供）に移行。Geminiモデルとエージェントのための単一統合エンドポイントで、サーバーサイド状態管理、バックグラウンド実行、ツール組み合わせ、マルチモーダル生成を提供。
- **キーファクト:**
  - Interactions API GA到達
  - 単一エンドポイントでモデル+エージェント+ツール統合
  - サーバーサイド状態管理・バックグラウンド実行対応
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/
- **Evidence ID:** EVD-20260628-0005

### INFO-006
- **タイトル:** xAI launches /goal - autonomous execution mode in Grok Build
- **ソース:** xAI (公式ブログ)
- **公開日:** 2026-06-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIがGrok Buildに「/goal」モードを新設。長時間実行の自律的実行を可能にし、より大きな実装タスクをAIエージェントに委譲できる。
- **キーファクト:**
  - /goalモードで自律的長時間実行が可能
  - 開発者が単一の目標を指定してコーディングタスクを委譲
  - grok-4.20-multi-agentモデルでマルチエージェント推論対応
- **引用URL:** https://x.ai/news/introducing-goal
- **Evidence ID:** EVD-20260628-0006

### INFO-007
- **タイトル:** Claude Agent SDK TypeScript v0.3.185 released (active development)
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-06-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版がv0.3.185に更新（前日リリース）。Python版も活発に開発中。Claude Codeと同等のツール、エージェントループ、コンテキスト管理をプログラム可能。
- **キーファクト:**
  - TypeScript版 v0.3.185（前日リリース）、Python版も活発
  - Claude Codeと同等の機能をSDK化
  - MCP統合対応（Telegram等の外部ツール連携実例あり）
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260628-0007

### INFO-008
- **タイトル:** ByteDance open-sources DeerFlow 2.0 - AI agent research framework
- **ソース:** Data Science Dojo / GitHub
- **公開日:** 2026-06-20
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0をオープンソース化。LangGraphベースのAIエージェントプラットフォームで、サブエージェントをオーケストレーションし、リサーチ、コード実行、Webブラウジングを実行。
- **キーファクト:**
  - LangGraphベースのエージェントオーケストレーション
  - 研究・コード実行・Webブラウジングを統合
  - Claude-to-DeerFlow マイグレーションツール提供
- **引用URL:** https://www.facebook.com/datasciencedojo/posts/1034772602406224/
- **Evidence ID:** EVD-20260628-0008

### INFO-009
- **タイトル:** Claude Code DAU data still missing - Cursor reports 1M+ DAU for comparison
- **ソース:** Uvik Software / Panto AI
- **公開日:** 2026-06-25
- **信頼性コード:** C-4
- **関連KIQ:** KIQ-001-01, H-ANT-002 (動的優先)
- **関連企業:** Anthropic, Cursor (Anysphere)
- **要約:** Claude CodeのDAU（日次アクティブユーザー）データが依然として公開されていない。比較としてCursorの1M+ DAUが報告されているが、Claude Code本体のDAUは不明。9R連続でDAU不在継続。
- **キーファクト:**
  - Claude Code DAU: 公式データなし（9R連続不在）
  - Cursor DAU: 1M+（2025年報告）
  - GitHub Copilot 有料購読者: 4.7M
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/
- **Evidence ID:** EVD-20260628-0009

### INFO-010
- **タイトル:** Agent frameworks largely interchangeable - top platforms compared
- **ソース:** YouTube / Domo / Uvik Software
- **公開日:** 2026-06-27
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** （複数社）
- **要約:** 2026年のAIエージェントフレームワーク比較で、主要フレームワーク（CrewAI、LangChain、OpenAI Agents SDK等）は大部分が交換可能との分析。主要プラットフォーム: Salesforce Agentforce、Microsoft Copilot Studio、Google Vertex AI Agent Builder、AWS Bedrock Agents。
- **キーファクト:**
  - フレームワーク間の差異縮小、交換可能性が高い
  - 2026年の主要9プラットフォーム比較で機能面の収束確認
  - Google Vertex AIが「Gemini Enterprise Agent Platform」にリブランディング
- **引用URL:** https://www.domo.com/learn/article/ai-agent-platforms
- **Evidence ID:** EVD-20260628-0010

### INFO-011
- **タイトル:** 74% of enterprise AI agent deployments get rolled back
- **ソース:** LinkedIn (業界リーダー投稿)
- **公開日:** 2026-06-26
- **信頼性コード:** C-4
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** エンタープライズAIエージェント展開の74%がロールバックされている。また40%のエンタープライズAIエージェントプロジェクトがキャンセル。デジタル断片化がAIイニシアチブの「沈黙の殺人者」と指摘。
- **キーファクト:**
  - エンタープライズAIエージェント展開の74%がロールバック
  - 40%のプロジェクトがキャンセル
  - SLA監視とガバナンス不在が主要因
- **引用URL:** https://www.linkedin.com/posts/chrishanpan_every-enterprise-leader-i-talk-to-wants-to-activity-7474866068516343808-75fi
- **Evidence ID:** EVD-20260628-0011

### INFO-012
- **タイトル:** AWS Bedrock and Azure OpenAI both hold FedRAMP High authorization
- **ソース:** TechnologyMatch
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Amazon, Microsoft, Google
- **要約:** AWS BedrockとAzure OpenAIの両方が関連する米国政府リージョンでFedRAMP High認証を保持。Google Vertex AIのFedRAMP Highは一般には利用不可。エンタープライズAIの政府向けセキュリティ認証競争。
- **キーファクト:**
  - AWS Bedrock: FedRAMP High認証あり
  - Azure OpenAI: FedRAMP High認証あり
  - Google Vertex AI: FedRAMP Highは一般利用不可
- **引用URL:** https://technologymatch.com/blog/aws-bedrock-vs-azure-openai-vs-google-vertex-ai-enterprise-ai-comparison
- **Evidence ID:** EVD-20260628-0012

### INFO-013
- **タイトル:** Google Vertex AI renamed to "Gemini Enterprise Agent Platform" with SLA
- **ソース:** Google Cloud (公式ドキュメント)
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** GoogleがVertex AIを「Gemini Enterprise Agent Platform」にリブランディング。Provisioned Throughputにトークン/秒レイテンシSLAを追加。Gemini Online Inference APIの正式SLA定義を公開。
- **キーファクト:**
  - Vertex AI → Gemini Enterprise Agent Platformにリブランディング
  - Provisioned Throughputにトークン/秒レイテンシSLA追加
  - Developer APIとEnterprise Agent Platform APIの2層構造
- **引用URL:** https://cloud.google.com/vertex-ai/generative-ai/sla
- **Evidence ID:** EVD-20260628-0013

### INFO-014
- **タイトル:** Proofpoint integrates with Claude Compliance API for enterprise data protection
- **ソース:** Proofpoint / NetMon (LinkedIn)
- **公開日:** 2026-06-26
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** ProofpointがAnthropic Claude Compliance APIと統合。エンタープライズ環境でのデータ保護とガバナンスをClaude Enterpriseに直接提供。規制コンプライアンスとデータアーカイブ要件を維持。
- **キーファクト:**
  - Claude Compliance APIがエンタープライズパートナーに提供開始
  - Proofpoint統合でデータ保護・ガバナンス強化
  - Claude Enterprise向けセキュリティエコシステム拡大
- **引用URL:** https://www.linkedin.com/posts/netmon_proofpoint-netmon-claudeai-activity-7474681077953896449-gyA5
- **Evidence ID:** EVD-20260628-0014

### INFO-015
- **タイトル:** Agentic ERP goes mainstream - 75,000 businesses deploying AI agents
- **ソース:** LyntxGlobal
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （ERP産業全体）
- **要約:** ミッドマーケットERPベンダーが75,000社・70カ国にAIエージェントを展開。仕訳入力、レシート処理、請求書処理を自動化するAIエージェントをERPに組み込み。
- **キーファクト:**
  - 75,000社・70カ国でアージェンティックERP展開
  - 仕訳入力・レシート処理・請求書処理をAI自動化
  - エンタープライズAIエージェントの生産導入が進行中
- **引用URL:** https://www.lyntxglobal.com/blog/agentic-erp-mainstream-75000-businesses-mid-market-adoption-case-study-lessons
- **Evidence ID:** EVD-20260628-0015

### INFO-016
- **タイトル:** Anthropic launches Claude Code Security tool for enterprise code auditing
- **ソース:** VendorDeep
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-004-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Code Securityを発表。エンタープライズ向けのAI生成コードの脆弱性監査ツール。開発チームがAI生成コードの脆弱性を監査できる。
- **キーファクト:**
  - Claude Code Security: AI生成コードの脆弱性監査ツール
  - エンタープライズ開発チーム向け
  - Anthropicのエンタープライズセキュリティ製品ライン拡大
- **引用URL:** https://vendordeep.com/analysis/anthropic-security-paradox-v2-claude-code-security-launch-vs-critical-vulnerability-disclosure.html
- **Evidence ID:** EVD-20260628-0016

### INFO-017
- **タイトル:** Anthropic hiring Security Controls Assurance Lead - SOC 2, ISO 27001/42001, HIPAA
- **ソース:** Anthropic (採用ページ)
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがSecurity Controls Assurance Leadを採用中。SOC 2、ISO 27001/42001、HIPAA、公共部門向けのグローバルコンプライアンス義務の管理要件を担当。
- **キーファクト:**
  - SOC 2、ISO 27001/42001、HIPAAコンプライアンス管理体制強化中
  - 公共部門向けコンプライアンス要件の管理
  - エンタープライズ・政府向けセキュリティ認証取得の積極的推進
- **引用URL:** https://job-boards.greenhouse.io/anthropic/jobs/5250063008
- **Evidence ID:** EVD-20260628-0017

### INFO-018
- **タイトル:** 84% of developers use AI tools, 80% run multiple AI coding environments
- **ソース:** IP With Ease / Snyk
- **公開日:** 2026-06-26
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** 84%の開発者がAIツールを使用または計画中。51%が毎日使用。46%のコードがAI生成。80%の開発者が2つ以上のAIコーディング環境を実行し、50.8%が本番ツールに接続するMCPサーバーを持つ。
- **キーファクト:**
  - 開発者の84%がAIツール使用、51%が毎日使用
  - 46%のコードがAI生成
  - 80%が2+のAI環境を実行、50.8%がMCPサーバー接続
- **引用URL:** https://ipwithease.com/how-ai-is-reshaping-software-development/
- **Evidence ID:** EVD-20260628-0018

### INFO-019
- **タイトル:** MCP 2026-07-28 Release Candidate - stateless protocol core and Extensions framework
- **ソース:** Model Context Protocol Blog (公式)
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-003-05
- **関連企業:** （標準化コンソーシアム）
- **要約:** MCP仕様の次期リリース候補（2026-07-28 RC）が公開。ステートレスプロトコルコア、Extensions フレームワーク、Tasks機能を含む。MCPがエンタープライズとAIエージェント間の重要なブリッジとして定着。
- **キーファクト:**
  - 2026-07-28 RC公開: ステートレスプロトコルコア・Extensions framework・Tasks
  - MCPサーバーは3つのプリミティブ（Tools, Resources, Prompts）で構成
  - スタックロック/ToolHive等でセキュリティ管理ツールも登場
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260628-0019

### INFO-020
- **タイトル:** AAIF membership tripling, 60,000+ projects adopting agentic AI standard
- **ソース:** AAIF / egghead.io / Linux Foundation
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-003-05
- **関連企業:** （標準化コンソーシアム）
- **要約:** Agentic AI Foundation (AAIF) のメンバーシップが3倍に増加。60,000以上のプロジェクトが命令標準を採用。Linux FoundationがAIエージェント向けDNSスタイルのトラストプロジェクトを新設。AAIFは「build first」アプローチで実装優先。
- **キーファクト:**
  - AAIF メンバーシップ3倍増、60,000+プロジェクト採用
  - Linux Foundation新設: AIエージェント向けDNS型トラストプロジェクト
  - 「build first」アプローチで実装を正式標準化プロセスより優先
- **引用URL:** https://egghead.io/ai-dev-essentials-36-agentic-ai-foundation-mistral-devstral-2-and-critical-react-exploit~w9jbl
- **Evidence ID:** EVD-20260628-0020

### INFO-021
- **タイトル:** Agent Skills ecosystem: 40+ skills-compatible products, 100,000+ pre-built skills
- **ソース:** AgentMan / agentskills.io
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Microsoft, Google
- **要約:** 2026年6月時点でagentskills.ioに約40のSkills互換製品が掲載。OpenAI Codex、GitHub Copilot、Cursor、Gemini等が対応。100,000以上の事前構築済みスキルがマーケットプレイスに存在。
- **キーファクト:**
  - 40+ Skills互換製品（OpenAI Codex、Copilot、Cursor、Gemini等）
  - 100,000+事前構築スキル
  - MicrosoftがAIコーディングエージェント向けSkills GitHub repo公開
- **引用URL:** https://agentman.ai/blog/agent-skills-ecosystem-report-2026
- **Evidence ID:** EVD-20260628-0021

### INFO-022
- **タイトル:** Google Gemini 3.5 Flash built-in computer use - agents that can see and act
- **ソース:** Google Cloud (公式 Facebook)
- **公開日:** 2026-06-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Google
- **要約:** Gemini 3.5 Flashにコンピュータ使用機能が組み込みツールとして追加。開発者はブラウザ、モバイル、デスクトップインターフェースで見て、推論し、行動するエージェントを構築可能。
- **キーファクト:**
  - Gemini 3.5 Flashにネイティブコンピュータ使用機能
  - ブラウザ・モバイル・デスクトップに対応
  - 開発者がカスタムエージェントを直接構築可能
- **引用URL:** https://www.facebook.com/googlecloud/posts/1341494701461187/
- **Evidence ID:** EVD-20260628-0022

### INFO-023
- **タイトル:** Google Gemini Robotics-ER - embodied reasoning for physical robots
- **ソース:** Google DeepMind / Gemini API Pricing
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** Google DeepMindのGemini Roboticsプログラムが、物理的推論とマルチステップロボット操作が可能なVision-Language-Actionモデルを実装。Gemini Robotics-ER（Embodied Reasoning）モデルが提供開始。
- **キーファクト:**
  - Gemini Robotics-ER: 身体化推論モデル
  - Vision-Language-Action モデルで物理的推論とロボット操作
  - Gemini API PricingページにRobotics-ERが記載（商用提供）
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Evidence ID:** EVD-20260628-0023

### INFO-024
- **タイトル:** Qwen3.7-Plus built for multimodal agent execution across GUI, tools, coding
- **ソース:** Alibaba Cloud (公式)
- **公開日:** 2026-06-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-03
- **関連企業:** Alibaba
- **要約:** Alibaba CloudがQwen3.7-Plusを発表。GUI操作、ツール使用、コーディングにまたがるマルチモーダルエージェント実行向けに設計。視覚入力からコード・実タスク実行まで対応する長時間実行エージェント向け。
- **キーファクト:**
  - Qwen3.7-Plus: マルチモーダルエージェント実行向け設計
  - GUI操作・ツール使用・コーディング統合
  - 長時間実行の実世界エージェントタスク対応
- **引用URL:** https://www.facebook.com/alibabacloud/posts/1462379839267437/
- **Evidence ID:** EVD-20260628-0024

### INFO-025
- **タイトル:** AI browser automation agents - Claude Computer Use and Operator capabilities analyzed
- **ソース:** TopReviewed AI
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Anthropic, OpenAI
- **要約:** Claude Computer UseとOperatorクラスのAIブラウザ自動化エージェントの能力分析。自律的なWebナビゲーションをLLMに委譲する技術の現状と限界を評価。
- **キーファクト:**
  - Claude Computer Use: 画面操作自動化エージェント
  - OpenAI Operator: ブラウザ自動化クラス
  - 自律Webナビゲーション技術の現状評価
- **引用URL:** https://topreviewed.ai/blog/ai-browser-automation-agents-what-computer-use-ai-can-and-cannot-do-yet
- **Evidence ID:** EVD-20260628-0025

### INFO-026
- **タイトル:** Anthropic Sandbox Runtime open-sourced - safer execution for Claude Code agents
- **ソース:** GitHub (anthropic-experimental/sandbox-runtime)
- **公開日:** 2026-06-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Code向けのSandbox Runtimeをオープンソースの早期プレビューとして公開。AIエージェントのより安全な実行を可能にする。ファイルシステム・ネットワーク隔離（macOS Seatbelt、Linux bubblewrap）を提供。
- **キーファクト:**
  - Sandbox Runtime (srt) オープンソース化
  - ファイルシステム・ネットワーク隔離機能
  - Claude APIで自己ホスト型サンドボックスオプション提供
- **引用URL:** https://github.com/anthropic-experimental/sandbox-runtime
- **Evidence ID:** EVD-20260628-0026

### INFO-027
- **タイトル:** Gartner: AI agent spending to reach $206.5B in 2026, up 139% YoY
- **ソース:** Gartner / HamzaAutomates
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-003-04
- **関連企業:** （業界全体）
- **要約:** GartnerがAIエージェントソフトウェア支出が2026年に$206.5B（約23.7兆円）に達すると予測。2025年の$86.4Bから139%増。前年比139%の急成長を確認。
- **キーファクト:**
  - 2026年AIエージェント支出予測: $206.5B
  - 2025年$86.4Bから139%増
  - パイロットから本番への移行が最大の課題
- **引用URL:** https://hamzaautomates.com/blog/gartner-just-confirmed-what-we-already-knew-ai-agent-spending-is-up-139-in-a-single-year-here-s-how-to-actually-capture-that-growth
- **Evidence ID:** EVD-20260628-0027

### INFO-028
- **タイトル:** 71% say running AI agents costs more than building them - DataRobot survey
- **ソース:** DataRobot 2026 Unmet AI Needs Survey
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** DataRobotの2026年調査で、回答者の71%が「エージェントの運用コストが構築コストを上回る」と回答。39ポイントのパイロットから本番へのギャップが2026年の決定的な採用統計。
- **キーファクト:**
  - 71%: エージェント運用コスト > 構築コスト
  - 72%の企業が2026年までにAIエージェント導入を計画
  - 39ポイントのパイロット→本番ギャップ
- **引用URL:** https://www.fwdslash.ai/blog/ai-agent-statistics
- **Evidence ID:** EVD-20260628-0028

### INFO-029
- **タイトル:** Customer service AI agent adoption jumps from 39% to 66%, 70% see ROI
- **ソース:** Salesforce survey / ZDNet
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04, KIQ-004-01
- **関連企業:** Salesforce
- **要約:** Salesforceが3,075人のサービス専門家を調査。カスタマーサービスでのAIエージェント導入が2025年の39%から2026年に66%に急増。70%の企業がROIを確認。
- **キーファクト:**
  - CS AIエージェント導入: 39% (2025) → 66% (2026)
  - 70%がROI確認
  - 3,075人のサービス専門家へのSalesforce調査
- **引用URL:** https://www.zdnet.com/article/agentic-ai-in-customer-service/
- **Evidence ID:** EVD-20260628-0029

### INFO-030
- **タイトル:** AWS Bedrock AgentCore adds three new knowledge layers for agents
- **ソース:** AWS Insider
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** AWS Bedrock AgentCoreに3つの新しい知識レイヤーが追加。エンタープライズ内部コンテンツ、ライブWeb情報、有料データソースへの接続、フィードバックとガバナンス機能を強化。
- **キーファクト:**
  - AgentCore: 内部コンテンツ・Web情報・有料データの3知識レイヤー追加
  - エージェントメモリ機能の設定可能化
  - Strands Agents統合で自然言語クエリ対応
- **引用URL:** https://awsinsider.net/articles/2026/06/25/amazon-bedrock-agentcore-adds-three-new-layers-of-agent-knowledge.aspx
- **Evidence ID:** EVD-20260628-0030

### INFO-031
- **タイトル:** Azure AI Foundry Agent Service - BYO model via enterprise AI gateways
- **ソース:** Microsoft Learn (公式)
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundry Agent ServiceがBring Your Own Modelに対応。Azure API Management等のエンタープライズAIゲートウェイ経由でホストされた独自モデルを接続可能。Microsoft 365、Dynamics 365、Databricks等との統合。
- **キーファクト:**
  - BYOモデル対応（Azure API Management経由）
  - Microsoft 365、Dynamics 365、Azure、Databricks統合
  - エンタープライズグレードのセキュリティとガバナンス
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/ai-gateway
- **Evidence ID:** EVD-20260628-0031

### INFO-032
- **タイトル:** OpenAI Jalapeno chip raises inference cost and vendor lock-in concerns
- **ソース:** TFiR
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** OpenAI
- **要約:** OpenAIのJalapenoチップが推論コストとベンダーロックインの懸念を引き起こしている。AIパイロットは内部デモとコスト分析を通過するが、本番規模で推論経済性を考慮していないため崩壊する。
- **キーファクト:**
  - Jalapenoチップ: 推論コスト最適化の意図だがロックイン懸念
  - 無料AIトークン提供がロックイントラップとして機能
  - コンピュート・コロケーション容量の集中がサプライヤーリスク増大
- **引用URL:** https://tfir.io/openai-jalapeno-chip-inference-costs-vendor-lock-in/
- **Evidence ID:** EVD-20260628-0032

### INFO-033
- **タイトル:** Pentagon opens classified military networks to 8 AI tech firms
- **ソース:** Instagram / Social media reports
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** OpenAI, Google, Microsoft, Nvidia, AWS, Oracle, Anthropic, xAI
- **要約:** Pentagonが単一モデルではなく、8社の承認されたテック企業（OpenAI、Google、Microsoft、Nvidia、AWS、Oracle等）の分類された軍事ネットワークへのアクセスを開放。AIの軍事標的選定への関与を正式化。
- **キーファクト:**
  - 8社のテック企業が分類された軍事ネットワークにアクセス可能
  - OpenAI、Google、Microsoft、Nvidia、AWS、Oracle等が含まれる
  - 単一モデル選定ではなく複数社オープンアクセス方式
- **引用URL:** https://www.instagram.com/p/DZ599V9Dv9R/
- **Evidence ID:** EVD-20260628-0033

### INFO-034
- **タイトル:** Pentagon formalizing AI role in military targeting - procurement stakes in billions
- **ソース:** Startup Fortune
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** （複数社）
- **要約:** PentagonがAIの軍事標的選定への関与を正式化。Pentagonは速度・規模・契約制限の最小化を求め、AI企業は防衛市場を欲しているが全社が同じ条件に署名するわけではない。調達ステークスは数十億ドル規模。
- **キーファクト:**
  - AIの軍事標的選定関与を正式化プロセス進行中
  - 調達ステークス: 数十億ドル規模
  - 企業間で倫理的条件の署名に差異あり
- **引用URL:** https://startupfortune.com/the-pentagon-is-formalizing-ais-role-in-military-targeting-and-the-procurement-stakes-run-into-the-billions/
- **Evidence ID:** EVD-20260628-0034

### INFO-035
- **タイトル:** OpenAI limits GPT-5.6 release to government-approved partners per Trump request
- **ソース:** CNBC / Politico
- **公開日:** 2026-06-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがまもなくリリースするGPT-5.6モデルを、トランプ政権の要請で少数の政府承認パートナーのみに提供。Anthropicも輸出管理指令に従い最新モデル2つ（Fable 5、Mythos 5）のアクセスを無効化済み。
- **キーファクト:**
  - GPT-5.6: 政府承認パートナーのみに制限リリース
  - トランプ政権がリリース制限を要請
  - Anthropic Fable 5・Mythos 5: 輸出管理指令でアクセス無効化
- **引用URL:** https://www.cnbc.com/2026/06/26/openai-limits-new-ai-models-to-trusted-partners-request-us-government.html
- **Evidence ID:** EVD-20260628-0035

### INFO-036
- **タイトル:** Trump signs executive order on AI innovation and cybersecurity
- **ソース:** EDUCAUSE Review
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （米国政府）
- **要約:** トランプ大統領がAIイノベーションとサイバーセキュリティに焦点を当てた新規大統領令に署名。連邦政府機関にAI採用加速を指示。Brennan Centerは「危険緩和に不十分」と批判。
- **キーファクト:**
  - 新規大統領令: AIイノベーション・サイバーセキュリティ重点
  - 連邦政府機関にAI採用加速を指示
  - Brennan Center等からの「規制不十分」批判あり
- **引用URL:** https://er.educause.edu/articles/2026/6/president-trump-signs-executive-order-on-ai-innovation-and-cybersecurity
- **Evidence ID:** EVD-20260628-0036

### INFO-037
- **タイトル:** EU AI Act Article 50 transparency rules take effect August 2026
- **ソース:** BlackFog / Collibra
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （EU規制対象）
- **要約:** EU AI Act第50条（透明性ルール）が2026年8月に発効。AIシステム（チャットボット等）との対話時にユーザーへの開示義務。欧州委員会の影響評価ではAIシステムの5-15%のみが高リスクに該当。
- **キーファクト:**
  - 第50条透明性ルール: 2026年8月発効
  - 高リスクAIシステム: 5-15%のみ該当（85%は最小リスク）
  - 63%の組織がAI目的制限を強制できない（2026年調査）
- **引用URL:** https://www.blackfog.com/eu-ai-act-compliance-requirements-2026-and-beyond/
- **Evidence ID:** EVD-20260628-0037

### INFO-038
- **タイトル:** China AI content labeling rules now in effect - all AI-generated content must be labeled
- **ソース:** Unbox Engineering / Lawfare
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance
- **要約:** 中国のAI生成コンテンツラベリング規則が正式に施行。全AI生成テキスト・画像・音声・動画にラベル付けが義務化。生成AIについて中国法は「社会主義核心価値観」の維持を要求。
- **キーファクト:**
  - AI生成コンテンツラベリング規則: 施行開始
  - 全AI生成コンテンツ（テキスト・画像・音声・動画）にラベル義務
  - 「社会主義核心価値観」維持の法的義務
- **引用URL:** https://www.facebook.com/unboxengineeringusa/posts/1359626202973761/
- **Evidence ID:** EVD-20260628-0038

### INFO-039
- **タイトル:** Gartner: Fortune 500 to grow from 15 AI agents (2025) to 150,000 (2028)
- **ソース:** Cybernews / Gartner
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-003-04
- **関連企業:** （業界全体）
- **要約:** Gartner予測: 平均Fortune 500企業のAIエージェント数が2025年の15から2028年に150,000に増加。80%のFortune 500企業が現在アクティブなAIエージェントを運用。
- **キーファクト:**
  - Fortune 500 AIエージェント: 15 (2025) → 150,000 (2028) 予測
  - 80%のFortune 500企業がアクティブAIエージェント運用中
  - 10,000倍の成長予測
- **引用URL:** https://cybernews.com/ai-tools/how-to-build-an-ai-agent/
- **Evidence ID:** EVD-20260628-0039

### INFO-040
- **タイトル:** Fortune 500 case study: AI agents deliver 35% faster reviews, 40% higher test coverage
- **ソース:** Birlasoft
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-004-01
- **関連企業:** Birlasoft
- **要約:** Fortune 500テックリーダー（Birlasoft）がコードレビュー、テスト自動化、DevOpsパイプラインにアージェンティックAIを組み込み。結果: レビュー35%高速化、テストカバレッジ40%向上、デプロイ25%安定化。
- **キーファクト:**
  - コードレビュー35%高速化
  - テストカバレッジ40%向上
  - デプロイメント25%安定化
- **引用URL:** https://www.facebook.com/Birlasoft/posts/1453119033500531/
- **Evidence ID:** EVD-20260628-0040

### INFO-041
- **タイトル:** Anthropic SCR designation - typically reserved for foreign adversaries, applied to US company
- **ソース:** CNN / WION
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, H-GOV-001
- **関連企業:** Anthropic
- **要約:** 米政府がAnthropicに供給チェーンリスク（SCR）指定を適用。SCR指定は通常外国の敵対国に関連する企業に予約される措置。両者が膠着状態に陥った後に適用。その後制限の一部緩和へ。
- **キーファクト:**
  - SCR指定: 通常は外国敵対国企業向け措米国AI企業への異例適用
  - 倫理・安全基準維持を巡る膠着後に指定
  - その後Mythos 5等の制限一部緩和（取引成立）
- **引用URL:** https://www.facebook.com/cnn/posts/1397698332222814/
- **Evidence ID:** EVD-20260628-0041

### INFO-042
- **タイトル:** Anthropic v. Department of War - amicus briefs filed in support of Anthropic
- **ソース:** SSRN (Legal)
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, H-GOV-001
- **関連企業:** Anthropic
- **要約:** Anthropic PBC v. U.S. Department of War 訴訟において、Anthropicの簡易判決申立を支持するアミカス・ブリーフ（意見書）が提出。AI企業と政府の安全性を巡る法廷闘争が本格化。
- **キーファクト:**
  - Anthropic PBC v. U.S. Department of War 訴訟進行中
  - 学術専門家によるアミカス・ブリーフ提出
  - 簡易判決申立が争点
- **引用URL:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6962668
- **Evidence ID:** EVD-20260628-0042

### INFO-043
- **タイトル:** The Atlantic: "Would Claude Refuse an Illegal Military Order?" - Hegseth furious at Anthropic
- **ソース:** The Atlantic
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** Anthropic
- **要約:** The Atlanticの調査記事: Hegseth国防長官がAnthropic幹部に対し、自律型致死兵器システムや大量監視での製品使用拒否に激怒。Claudeが違法な軍事命令を拒否するかが焦点。
- **キーファクト:**
  - Hegseth国防長官がAnthropicの安全基準維持に激怒
  - 自律型致死兵器・大量監視での使用拒否が対立の核
  - Claudeの違法命令拒否能力が法的・倫理的焦点
- **引用URL:** https://www.theatlantic.com/national-security/2026/06/claude-anthropic-ai-warfare-orders/687581/
- **Evidence ID:** EVD-20260628-0043

### INFO-044
- **タイトル:** AI boomerang: companies rehiring workers after AI replacement failures
- **ソース:** MindStudio / Instagram
- **公開日:** 2026-06-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Starbucks, Klarna, Duolingo, McDonald's
- **要約:** AI代替のロールバック現象「AIブーメラン」が拡大。Starbucks、Klarna、McDonald's等がAI代替後に人間の再雇用を実施。Duolingoは請負業者の作業をAI生成コンテンツに切り替え人員削減。
- **キーファクト:**
  - AIブーメラン: AI代替失敗後に人間再雇用する企業増加
  - Starbucks、Klarna、McDonald's等がAI代替ロールバック
  - Duolingo: 請負業者作業をAIに切り替え、人員削減
- **引用URL:** https://www.mindstudio.ai/blog/ai-replacement-rollback-starbucks-klarna-mcdonalds
- **Evidence ID:** EVD-20260628-0044

### INFO-045
- **タイトル:** Elastic cuts 281 jobs (7%) to reorganize around AI automation
- **ソース:** Hoodline / Facebook
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Elastic
- **要約:** Elasticが約281人（全社員の7%）を削減し、AIを中心に再編成。自動化が複雑さを減らすとし、成長への投資を強調。内部メモでAI自動化を人員削減の要因として明示。
- **キーファクト:**
  - 281人（7%）削減、AI中心に再編
  - 自動化による複雑さ削減を理由
  - 内部メモでAI自動化が削減要因と明記
- **引用URL:** https://www.facebook.com/Hoodline/posts/1605132298289349/
- **Evidence ID:** EVD-20260628-0045

### INFO-046
- **タイトル:** 39% of executives made AI-driven headcount reductions
- **ソース:** HeroHunt.ai / Tech industry reports
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** （業界全体）
- **要約:** 2026年のテック業界リストラとAIの現実チェック。エグゼクティブの39%が低〜中程度の人員削減を実施。内部メモでAI自動化が削減要因として明示的に引用される事例が増加。
- **キーファクト:**
  - エグゼクティブの39%がAI要因の人員削減を実施
  - 内部メモでAI自動化を削減要因として明示
  - テック業界でAI自動化とリストラの相関が明確化
- **引用URL:** https://www.herohunt.ai/blog/tech-layoffs-and-ai-the-2026-reality-check/
- **Evidence ID:** EVD-20260628-0046

### INFO-047
- **タイトル:** WPP forecasts $100B AI search ad market by 2026
- **ソース:** LinkedIn / WPP
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** WPP, Meta, Google
- **要約:** WPP（年間$640億の広告支出を管理）がAI検索広告市場を2026年に$1000億と予測。5年前の$3.01億からの急成長。プラットフォームAIによる広告自動化が代理店のバリューチェーンを侵食。
- **キーファクト:**
  - AI検索広告市場: $3.01億 → $1000億（5年間）
  - WPP: $640億/年の広告支出管理
  - プラットフォームAI広告自動化が代理店ディスインターミディエーション
- **引用URL:** https://www.linkedin.com/posts/tomer-kotler-32b8a1250_301-million-100-billion-five-years-activity-7474375988919984128-h0A_
- **Evidence ID:** EVD-20260628-0047

### INFO-048
- **タイトル:** OpenAI GPT-5.6 Sol preview - limited to select partners, Business Plan price cut 23.5%
- **ソース:** OpenAI (公式) / Reddit
- **公開日:** 2026-06-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6 Solモデルのプレビューを公開。プレビュー期間中は限定的なAPI/Codexアクセス。同時にBusiness Plan価格を約23.5%引き下げ、Codex料金をトークンベースに変更（4月2日）。
- **キーファクト:**
  - GPT-5.6 Solプレビュー: 限定的パートナー向け
  - Business Plan価格23.5%引き下げ
  - Codex料金: メッセージ単位→トークンベースに変更
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260628-0048

### INFO-049
- **タイトル:** Treasury concludes AI Innovation Series implementing Executive Order 14179
- **ソース:** U.S. Treasury (公式)
- **公開日:** 2026-06-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** （米国政府）
- **要約:** 米財務省がAIイノベーションシリーズを完了。大統領令14179「人工知能における米国の指導力への障壁除去」の実施を支援。政府全体でのAI採用加速と規制緩和が推進中。
- **キーファクト:**
  - 大統領令14179: AI指導力への障壁除去
  - 財務省AIイノベーションシリーズ完了
  - 連邦政府全体でのAI採用加速推進
- **引用URL:** https://home.treasury.gov/news/press-releases/sb0540
- **Evidence ID:** EVD-20260628-0049

### INFO-050
- **タイトル:** MMLU >90% for all frontier models; GPQA Diamond GPT-5.4 and Gemini 3.1 Pro tied
- **ソース:** TeamAI / LLM Stats
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** 2026年前半、全フロンティアモデルがMMLUで90%超え。GPQA DiamondでGPT-5.4（94.4%）とGemini 3.1 Pro（94.3%）が実質同点。Claude Fable 5がGDPval-AAリーダーボードで1815点で首位。
- **キーファクト:**
  - MMLU: 全フロンティアモデル90%超え
  - GPQA Diamond: GPT-5.4 94.4% vs Gemini 3.1 Pro 94.3%（実質同点）
  - GDPval-AA: Claude Fable 5首位（1815点）
  - 5ベンチマーク省略セットで84モデル×133ベンチマークをMedAE 3.93で再現可能
- **引用URL:** https://teamai.com/blog/large-language-models-llms/best-ai-models-for-complex-reasoning-2026/
- **Evidence ID:** EVD-20260628-0050

### INFO-051
- **タイトル:** ARC-AGI-2: Seed 2.1 Pro leads at 0.625; DiARC achieves 96% on ARC-AGI-1 with Qwen3
- **ソース:** LLM Stats / arXiv
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** ByteDance, Alibaba
- **要約:** ARC-AGI-2リーダーボードでByteDance Seed 2.1 Proが0.625で首位。DiARC手法でQwen3モデルがARC-AGI-1、MiniARC、ConceptARCで96%超を達成し、闭源モデルを上回る。
- **キーファクト:**
  - ARC-AGI-2首位: Seed 2.1 Pro (ByteDance) 0.625
  - DiARC+Qwen3: ARC-AGI-1/MiniARC/ConceptARCで96%超
  - オープンソースモデルが特定ドメインで闭源逆転
- **引用URL:** https://llm-stats.com/benchmarks/arcagi2
- **Evidence ID:** EVD-20260628-0051

### INFO-052
- **タイトル:** Open source models closing gap - Kimi and DeepSeek post frontier-class coding results
- **ソース:** MindsHub / HN
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek, Moonshot AI (Kimi), Meta
- **要約:** オープンウェイトモデルが急速にギャップを縮小。GPT-5.5とClaudeがコーディング全体でリードするが、KimiとDeepSeekがフロンティアクラスのコーディング結果をはるかに低いコストで達成。
- **キーファクト:**
  - オープンウェイトモデル: コーディングでフロンティアクラス到達
  - Kimi・DeepSeek: 低コストでフロンティア級結果
  - オープンモデルの最大課題: 私的組織の慈善事業に依存
- **引用URL:** https://mindshub.ai/blog/navigating-the-llm-landscape-a-comparative-analysis-of-leading-large-language-models
- **Evidence ID:** EVD-20260628-0052

### INFO-053
- **タイトル:** Baseten raises $1.5B Series F for AI inference; 9th $1B+ AI round this year
- **ソース:** Crunchbase / Forbes / Law360
- **公開日:** 2026-06-26
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Baseten, OpenAI, SSI
- **要約:** AI推論技術プロバイダーBasetenが$1.5BのSeries Fを完了。今年9つ目の$1B+ AIエクイティラウンド。3社のAI企業が産業全体よりも多くの資金を調達。OpenAIが$40B、SSI等の大型ラウンドが継続。
- **キーファクト:**
  - Baseten: $1.5B Series F（AI推論）
  - 今年9つ目の$1B+ AIラウンド
  - Airwallex: $320M Series H（$11B評価、AI金融）
- **引用URL:** https://news.crunchbase.com/venture/biggest-funding-rounds-ai-marketing-robotics-baseten/
- **Evidence ID:** EVD-20260628-0053

### INFO-054
- **タイトル:** Big tech to spend $725B on AI capex in 2026; McKinsey $5.2T data center need by 2030
- **ソース:** Yahoo Finance / McKinsey / Microsoft Blog
- **公開日:** 2026-06-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Microsoft, Google, Amazon, Meta
- **要約:** ビッグテック4社が2026年にAIインフラ向け資本支出$725Bを計画。McKinseyは2030年までに$5.2Tのデータセンター投資が必要と試算。MicrosoftがPecos, Texasに2GWデータセンター新設を発表。
- **キーファクト:**
  - ビッグテック2026年資本支出: $725B
  - McKinsey: 2030年までに$5.2Tデータセンター投資必要
  - Microsoft: Pecos, Texasに2GW新データセンター
  - 今10年間で約$2Tのデータセンター投資軌道
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/ai-demand-begins-justify-massive-110000106.html
- **Evidence ID:** EVD-20260628-0054

### INFO-055
- **タイトル:** AGI now "engineering problem not research problem" - autonomous scientific AI advancing
- **ソース:** Peter Diamandis / Scientific American
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** （研究コミュニティ）
- **要約:** AGIがエンジニアリング問題（研究問題ではなく）になったとの見方が台頭。"Robot Scientist"が自ら仮説を生成し実験を設計する自律科学AIが登場。AIの科学研究ライフサイクル自動化が進行。
- **キーファクト:**
  - AGI = エンジニアリング問題（研究的飛躍不要、段階的ブレークスルーで到達可能）
  - "Robot Scientist": 自ら仮説生成・実験設計
  - AI科学研究ライフサイクル自動化進行
- **引用URL:** https://x.com/PeterDiamandis/article/2021255300305551374
- **Evidence ID:** EVD-20260628-0055

### INFO-056
- **タイトル:** Cursor: 64% of Fortune 500 use it; acquires Continue; Copilot goes usage-based
- **ソース:** Panto AI / The New Stack
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Cursor (Anysphere), GitHub/Microsoft
- **要約:** CursorのFortune 500利用率が64%、50,000+企業が採用。Cursorがオープンソースcodr Continue（34K GitHub stars）を静かに買収。GitHub Copilotが6月1日から使用量ベースAI Creditsに移行（Business $19/月、Enterprise $39/月）。
- **キーファクト:**
  - Cursor: Fortune 500の64%、50,000+企業、100M+行のコード
  - Cursor → Continue買収（acqui-hire）
  - GitHub Copilot: 使用量ベース課金に移行（6月1日）
- **引用URL:** https://www.getpanto.ai/blog/cursor-ai-statistics
- **Evidence ID:** EVD-20260628-0056

### INFO-057
- **タイトル:** Stanford: Entry-level tech job postings down 67%, junior dev demand down 20%
- **ソース:** Stanford Digital Economy Lab / Medium
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** Stanford Digital Economy Lab確認: エントリーレベルテック求人が2023-2024で67%減少、雇用13%減。ジュニア開発者需要は約20%減少。AWS CEOが「壊滅的」と警告。欧州ジュニアテック採用は2025年に3%縮小。
- **キーファクト:**
  - エントリーレベルテック求人: 2023-2024で67%減
  - ソフトウェア開発者雇用（22-39歳）: 約20%減
  - AWS CEOが「壊滅的」と評価
- **引用URL:** https://www.facebook.com/TheLinuxFoundation/posts/1664536229051773/
- **Evidence ID:** EVD-20260628-0057

### INFO-058
- **タイトル:** Demis Hassabis tightens AGI timeline to ~2030; "species-level transition"
- **ソース:** Bloomberg / ZME Science
- **公開日:** 2026-06-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google DeepMind
- **要約:** DeepMind CEO Demis HassabisがAGIタイムラインを約2030年（5-10年）に短縮。AIが「種レベルの移行」に入っていると警告。現在のスケーリングアプローチ以上のブレークスルーが必要としつつ、Kurzweil予測とほぼ一致。
- **キーファクト:**
  - Hassabis AGIタイムライン: ~2030年（5-10年）
  - 「種レベルの移行」宣言
  - 単純スケーリング以上のブレークスルー必要
- **引用URL:** https://www.zmescience.com/future/deepmind-ceo-agi-2030/
- **Evidence ID:** EVD-20260628-0058

### INFO-059
- **タイトル:** Red Cross calls for new treaty on autonomous weapons; US-China AI negotiations needed
- **ソース:** Lawfare / Carnegie / Brookings
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-06
- **関連企業:** （政府・国際機関）
- **要約:** 赤十字国際委員会が自律型兵器の新条約を求める声明。米中AI交渉でワシントンは中国の国家統制を明確に理解すべきとLawfareが指摘。Brookingsが4部構成のAI労働政策フレームワーク（ブレーキ・操舵・バッファー・シフト）を発表。
- **キーファクト:**
  - 赤十字: 自律型兵器新条約要求
  - 米中AI交渉の必要性（中国国家統制の理解前提）
  - Brookings: AI労働政策4部フレームワーク
- **引用URL:** https://www.facebook.com/Lawfareblog/posts/1617793573687508/
- **Evidence ID:** EVD-20260628-0059

### INFO-060
- **タイトル:** ByteDance Seed 2.1 released: cost cut 80%, coding matches Claude Opus 4.7
- **ソース:** ByteDance Seed (公式) / Wall Street CN
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-01, KIQ-003-02
- **関連企業:** ByteDance
- **要約:** ByteDanceがSeed 2.1シリーズを正式リリース。豆包2.1 Proのコーディング能力がClaude Opus 4.7に匹敵し、コストは80%削減。Seedance 2.5は30秒4K動画生成で世界一。APIは火山引擎で提供中。
- **キーファクト:**
  - Seed 2.1 Pro: コーディング能力Claude Opus 4.7匹敵、コスト80%削減
  - Seedance 2.5: 30秒4K動画生成（世界一）
  - 豆包有料版（Pro）ローンチ、企業向け機能強化
  - ARC-AGI-2リーダーボード首位（0.625）
- **引用URL:** https://seed.bytedance.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity
- **Evidence ID:** EVD-20260628-0060

### INFO-061
- **タイトル:** AI-proof skills: emotional intelligence, critical thinking, skilled trades remain irreplaceable
- **ソース:** Upwork / CFR / AIJobsRisk
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** AI代替困難な職業の共通条件: 感情的知性、批判的思考、人間の相互作用、創造性。医療、熟練工、教育、精密運動を要する仕事が最も安全。AI Fluency（AIと効果的に協働する能力）が新たな必須スキルとして浮上。
- **キーファクト:**
  - AI-proof条件: 感情的知性・批判的思考・人間相互作用・創造性
  - 最安全職種: 医療・熟練工・教育・精密運動
  - AI Fluencyが新たな必須メタスキルとして台頭
- **引用URL:** https://www.upwork.com/resources/jobs-ai-wont-replace
- **Evidence ID:** EVD-20260628-0061

### INFO-062
- **タイトル:** Agentic AI ROI: 171% average, 3x traditional automation; but 80%+ see no measurable AI gains
- **ソース:** BERI / ManpowerGroup / WEF
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-002-02
- **関連企業:** JPMorgan, Klarna, Morgan Stanley
- **要約:** アージェンティックAIの平均ROIは171%で従来自動化の3倍。JPMorgan、Klarna、Morgan Stanley等12の企業ケーススタディ。一方で80%以上の企業が過去3年間でAIによる測定可能な利益を報告していない（WEF）。
- **キーファクト:**
  - アージェンティックAI ROI: 平均171%（従来自動化の3倍）
  - 80%+の企業: 過去3年間で測定可能なAI利益なし（WEF）
  - AI開発支援: タスク完了が最大55%高速化
- **引用URL:** https://www.beri.net/article/agentic-ai-roi-171-percent-enterprise-case-studies
- **Evidence ID:** EVD-20260628-0062

### INFO-063
- **タイトル:** AI agents score 0% on ALE benchmark hardest tier - deployment reality check
- **ソース:** Sedai
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-005-01
- **関連企業:** （業界全体）
- **要約:** AIエージェントがALEベンチマークの最難関ティアで0%スコア。エンジニアリングリーダーが現在のエージェント展開の限界を分析。自律的タスク完了には人間レベルの推論がまだ不足。
- **キーファクト:**
  - ALEベンチマーク最難関ティア: AIエージェント0%
  - 自律的タスク完了の限界露呈
  - エージェント展開の現実評価必要性
- **引用URL:** https://sedai.io/blog/ai-failed-human-benchmark
- **Evidence ID:** EVD-20260628-0063

### INFO-064
- **タイトル:** SaaS shifting to AI-native Agent-as-a-Service (AaaS) model
- **ソース:** BetterCloud / TowardsAgenticAI
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** （SaaS産業全体）
- **要約:** SaaS産業が人間を支援するツールから、自律的に実行し結果を所有するAIネイティブアプリ・エージェントへ移行。Agent-as-a-Service (AaaS)がSaaSを置き換える趨勢。ソフトウェアツールの販売から成果の販売へ。
- **キーファクト:**
  - SaaS → AIネイティブ AaaS への産業構造変化
  - ツール販売から成果（アウトカム）販売への転換
  - AIエージェントがCRM・ERP・API・DBと直接統合
- **引用URL:** https://www.bettercloud.com/monitor/saas-industry/
- **Evidence ID:** EVD-20260628-0064

### INFO-065
- **タイトル:** AI ad visibility impact: 25% of ads lose top spot due to AI overview
- **ソース:** AdWeek / Facebook
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google, Meta
- **要約:** AI概要により広告の約25%がトップ位置を失い、視認性低下。広告代理店への影響拡大。AI駆動マーケティング自動化市場は$5.1B (2024) → $47.1B (2030)へ成長予測。
- **キーファクト:**
  - AI概要: 広告の25%がトップ位置喪失
  - AIマーケティング自動化市場: $5.1B → $47.1B (2024-2030)
  - 広告代理店への構造的影響拡大
- **引用URL:** https://www.facebook.com/adweekbrandshare/posts/1613124724156481/
- **Evidence ID:** EVD-20260628-0065

### INFO-066
- **タイトル:** AI token cost reduction: Strategy AI Agents cut usage up to 98%, Mosaic 50%
- **ソース:** Strategy.com / LinkedIn (Tomasz Tunguz)
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** （業界全体）
- **要約:** Strategy AI AgentsがAIトークン使用量を最大98%削減、Mosaicは最大50%削減。組織はAIをコスト最適化レイヤーとして活用。推論コストを60-80%削減するマルチベンダー戦略が台頭。IaC・標準APIでベンダーロックイン最小化。
- **キーファクト:**
  - Strategy AI Agents: トークン使用量98%削減
  - 推論コスト60-80%削減可能
  - IaC・標準APIでロックイン最小化
- **引用URL:** https://www.strategy.com/it/software/ai-token-cost-and-accuracy-benchmark
- **Evidence ID:** EVD-20260628-0066

### INFO-067
- **タイトル:** Gemini 3.1 Pro: $2 input / $12 output per million tokens; Flash free tier available
- **ソース:** Google AI for Developers (公式)
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google
- **要約:** Gemini API料金: 3.1 Proが$2入力/$12出力（100万トークン）、FlashとFlash-Liteはより低価格。出力（思考トークン含む）は無料枠あり。コンテキストキャッシング価格も設定。
- **キーファクト:**
  - Gemini 3.1 Pro: $2入力 / $12出力 / 1M tokens
  - Flash/Flash-Lite: より低価格設定
  - コンテキストキャッシング: $0.15-$1.00/1M tokens/hour
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Evidence ID:** EVD-20260628-0067

### INFO-068
- **タイトル:** Anthropic Claude pricing: usage-based billing, Fast Mode $30/$150, Max plan $200/mo ≈ $8K tokens
- **ソース:** Kingy AI / CheckThat.ai / Reddit
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Anthropicが使用量ベース課金に移行。Fast Mode（≤200K input）: $30入力/$150出力。Extended Mode: $60入力/$225出力。Claude Max 20xプラン$200/月は約$8,000相当のトークン使用量。Opus 4.6: $3-15/1M tokens。
- **キーファクト:**
  - Fast Mode: $30入力 / $150出力 / 1M tokens
  - Extended Mode: $60入力 / $225出力
  - Max 20x ($200/月) ≈ $8,000トークン価値
  - API: 標準トークン価格から50%オフ
- **引用URL:** https://kingy.ai/ai/usage-based-billing-no-flat-rate-why-anthropics-2026-pricing-shift-changes-everything-for-claude-users/
- **Evidence ID:** EVD-20260628-0068

### INFO-069
- **タイトル:** Global M&A on track for $4T in 2026, AI-driven dealmaking record pace
- **ソース:** PwC / Solganick
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** （業界全体）
- **要約:** 2026年グローバルM&Aディールバリューが$4Tに到達する軌道（2021年以来最高）。$5B超のメガディールが総価値のほぼ半分。AIがディールメイキングを激化させている。
- **キーファクト:**
  - 2026年グローバルM&A: $4T軌道（2021年以来最高）
  - $5B超メガディールが総価値の約半分
  - AI駆動のディールメイキングが記録的ペース
- **引用URL:** https://www.pwc.com/gx/en/services/deals/trends.html
- **Evidence ID:** EVD-20260628-0069

### INFO-070
- **タイトル:** Google DeepMind AGI-to-ASI paper: four pathways including recursive self-improvement
- **ソース:** MindStudio / DeepMind
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** Google DeepMind
- **要約:** Google DeepMindがAGIからASI（人工超知能）への4つの経路を提示。1つは再帰的自己改善。AIシステムが自身のアーキテクチャ・訓練プロセス・アルゴリズムを修正し、より能力を高す経路。
- **キーファクト:**
  - DeepMind AGI→ASI 論文: 4経路提示
  - 再帰的自己改善が主要経路の1つ
  - Anthropic研究リード: 「エンジニアの99%が自己改善モデル構築にClaude使用」
- **引用URL:** https://www.mindstudio.ai/blog/google-deepmind-agi-to-asi-paper-four-pathways
- **Evidence ID:** EVD-20260628-0070

### INFO-071
- **タイトル:** WEF: AI and Future of Entry-Level Work 2026 - 44% of core skills to change in 5 years
- **ソース:** World Economic Forum
- **公開日:** 2026-06-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03, KIQ-004-01
- **関連企業:** （世界経済全体）
- **要約:** WEFが「AIとエントリーレベルワークの未来」レポート発表。今後5年でコアスキルの44%が変化。「AIとビッグデータ」「リーダーシップ」が最重要スキルに。7つの主要職業クラスターが新興。
- **キーファクト:**
  - コアスキルの44%が5年以内に変化
  - 7つの新興職業クラスター: データ&AI、ケア経済等
  - エントリーレベルワークへの影響フレームワーク発表
- **引用URL:** https://reports.weforum.org/docs/WEF_Artificial_Intelligence_and_the_Future_of_Entry_Level_Work_2026.pdf
- **Evidence ID:** EVD-20260628-0071

### INFO-072
- **タイトル:** Coze (扣子): ByteDance's zero-code AI agent platform; HiAgent for enterprise
- **ソース:** CSDN / AI-Bot.cn
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのCozeプラットフォームがゼロコード/ローコードでAIエージェント構築を可能に。企業向けHiAgentプラットフォームも提供し、データセキュリティ・プライバシー要件に対応。自動化オフィス、スマートCS、コンテンツ生成に対応。
- **キーファクト:**
  - Coze: ゼロコード/ローコード AIエージェント構築プラットフォーム
  - HiAgent: 企業級データセキュリティ対応
  - 自動化オフィス・スマートCS・コンテンツ生成対応
- **引用URL:** https://ai-bot.cn/hiagent/
- **Evidence ID:** EVD-20260628-0072

### INFO-073
- **タイトル:** Export controls give US administration "great discretion" in regulating AI
- **ソース:** Programmable Mutter / Lawfare
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, H-GOV-001
- **関連企業:** Anthropic
- **要約:** 輸出管理と関連国家セキュリティツールが政権にAI技術規制における「極めて大きな裁量」を提供。これはトランプ第2期以前から真。Anthropic闘争がAI規制の構造的問題を浮き彫り。
- **キーファクト:**
  - 輸出管理: AI規制における政権の「極めて大きな裁量」
  - 国家セキュリティツールのAI企業への適用が構造的問題
  - Anthropic闘争がAI規制メカニズムの限界を露呈
- **引用URL:** https://www.programmablemutter.com/p/what-the-anthropic-fight-says-about
- **Evidence ID:** EVD-20260628-0073

### INFO-074
- **タイトル:** One red line, two outcomes: Anthropic refuses vs OpenAI complies with Pentagon
- **ソース:** Social media analysis / Frontier AI x Pentagon
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** Anthropic, OpenAI
- **要約:** フロンティアAI企業とPentagonの関係で「1つのレッドライン、2つの結果」: Anthropicは完全に拒否（大量監視・自律型致死兵器）、OpenAIは既存の法的枠組み内でPentagon契約を獲得。競争上の変位効果が発生。
- **キーファクト:**
  - Anthropic: 大量監視・自律型致死兵器への使用を完全拒否
  - OpenAI: 既存法的枠組み内でPentagon契約獲得
  - 倫理的拒否企業が罰せられ、順応企業が報われる構造確認
- **引用URL:** https://www.facebook.com/groups/vibecodinglife/posts/2069103323678194/
- **Evidence ID:** EVD-20260628-0074

### INFO-075
- **タイトル:** Open-source models: Ollama v0.30.8 top models - Qwen 3.6 27B, Kimi K2.6, gpt-oss:20b
- **ソース:** PromptQuorum / Kingy AI
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Alibaba, Moonshot AI, Meta
- **要約:** Ollama v0.30.8 (June 12 2026)のトップオープンソースモデル: Qwen 3.6 27B、Kimi K2.6、gpt-oss:20b。DeepSeek CoderがコーディングベンチマークでLlama 3を上回る。Llama 4は「オープンウェイト」であり完全なオープンソースではない。
- **キーファクト:**
  - トップOSSモデル: Qwen 3.6 27B、Kimi K2.6、gpt-oss:20b
  - DeepSeek Coder: コーディングでLlama 3を上回る
  - Llama 4: オープンウェイト（完全OSSではない）
- **引用URL:** https://www.promptquorum.com/local-llms/top-open-source-models-ollama
- **Evidence ID:** EVD-20260628-0075

### INFO-076
- **タイトル:** GPT-5.6 Sol detailed: 3-tier pricing (Sol/Terra/Luna), Terminal-Bench 91.9%, ultra mode with subagents
- **ソース:** OpenAI (公式ブログ - スクレイピング詳細)
- **公開日:** 2026-06-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** GPT-5.6シリーズ3モデル詳細公開。Sol（旗艦）$5入力/$30出力、Terra（バランス）$2.50/$15、Luna（低コスト）$1/$6。Terminal-Bench 2.1でSol Ultra 91.9%。新「ultra」モードでサブエージェント活用。「max」推論エフォート新設。700,000 A100時間相当の自動レッドチーミング実施。Cerebrasで750 tokens/sec（7月予定）。
- **キーファクト:**
  - 3ティア: Sol $5/$30, Terra $2.50/$15, Luna $1/$6 (per 1M tokens)
  - Terminal-Bench 2.1: Sol Ultra 91.9%, Sol 88.8%, Mythos 5 84.3%
  - 新「ultra」モード: サブエージェントで複雑作業加速
  - 新命名体系: 世代番号（5.6）+ 能力ティア（Sol/Terra/Luna）
  - 700,000 A100時間の自動レッドチーミング
  - 30分最小キャッシュライフ、プロンプトキャッシング改善
  - Cerebras: 750 tokens/sec（7月ローンチ予定）
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260628-0076

### INFO-077
- **タイトル:** Anthropic Fable 5/Mythos 5 export control: government cited narrow non-universal jailbreak
- **ソース:** Anthropic (公式声明 - スクレイピング詳細)
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06, H-GOV-001, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** 米政府が国家安保権限に基づきFable 5/Mythos 5の全外国人（米国内外国人含む）のアクセス停止を命じる輸出管理指令。理由は狭い非普遍的ジェイルブレイクの発見。Anthropicは「この基準を全業界に適用すれば全フロンティアモデルの新規展開が停止する」と反論。defense-in-depth戦略と30日データ保持を維持。
- **キーファクト:**
  - 輸出管理指令: 全外国人（米国内含む）のFable 5/Mythos 5アクセス停止
  - 理由: 狭い非普遍的ジェイルブレイク（特定コードベースの脆弱性発見）
  - Anthropic反論: 同能力はGPT-5.5等の他モデルでも利用可能
  - Mythos級モデル: 30日データ保持必須（実コストあり）
  - 「透明・公平・明確・技術事実に基づく法定プロセス」の不在を批判
- **引用URL:** https://www.anthropic.com/news/fable-mythos-access
- **Evidence ID:** EVD-20260628-0077

### INFO-078
- **タイトル:** CNBC confirms: OpenAI government-limited rollout, Trump AI executive order framework in development
- **ソース:** CNBC (スクレイピング詳細)
- **公開日:** 2026-06-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** OpenAI, Anthropic
- **要約:** CNBC確認: OpenAIが政府要請で信頼パートナーのみに限定。トランプ政権が6月初頭にAI大統領令に署名（詳細乏しいが、AI開発者にリリース前の政府評価を自主的に求める）。OpenAIはサイバー大統領令フレームワークと「将来のモデルリリース向け反復可能なプロセス」開発で政権と協力中。Anthropicは2週間前にFable 5/Mythos 5アクセス無効化済み。
- **キーファクト:**
  - トランプAI大統領令（6月初頭）: モデル評価の自主的事前政府協議要請
  - OpenAI: サイバー大統領令フレームワーク開発で政権協力
  - 「この種の政府アクセスプロセスが長期デフォルトになるべきではない」（OpenAI声明）
  - Anthropic: Fable 5/Mythos 5無効化から2週間、交渉継続中
- **引用URL:** https://www.cnbc.com/2026/06/26/openai-limits-new-ai-models-to-trusted-partners-request-us-government.html
- **Evidence ID:** EVD-20260628-0078

### INFO-079
- **タイトル:** BCG: 60% of AI investors generate no value, only 5% create substantial value at scale
- **ソース:** HBR / BCG / Bain / Deloitte
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** （業界全体）
- **要約:** BCG分析: AIに投資する企業の60%が物質的価値を生み出さず、仅か5%が規模で大きな価値を創出。Bainは「AIの正しいドメイン」が競争優位性・独自データ・エンドツーエンド再発明ポテンシャルの交差点にあると指摘。リスキリングは投資でありコストではない。
- **キーファクト:**
  - AI投資企業の60%: 物質的価値なし、5%のみが規模で大きな価値
  - 正しいAIドメイン: 競争優位性×独自データ×エンドツーエンド再発明の交差点
  - リスキリング = 投資（コストではない）
- **引用URL:** https://hbr.org/2026/06/the-5-types-of-ai-investment-and-how-to-capture-their-value
- **Evidence ID:** EVD-20260628-0079

### INFO-080
- **タイトル:** Meta projected $66-72B AI CapEx in 2025; AI token prices fall but total bills rise
- **ソース:** YourStory / Zenn
- **公開日:** 2026-06-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, KIQ-004-04
- **関連企業:** Meta
- **要約:** Metaが2025年に$66-72Bの積極的AI資本支出を計画、さらに増加へ。AIトークン価格は継続的に下落するが、総請求額は増加傾向（使用量増加が単価低下を相殺）。「AIは安くなっていない、単価格が下落しているだけ」の構造。
- **キーファクト:**
  - Meta AI資本支出: 2025年$66-72B予測（さらに増加）
  - トークン単価下落 vs 総請求額増加のパラドックス
  - 単価格下落が使用量増大で相殺される構造
- **引用URL:** https://www.facebook.com/yourstorycom/posts/1497138289114807/
- **Evidence ID:** EVD-20260628-0080
