# 収集データ: 2026-09-07

## メタデータ
- 収集日時: 2026-09-07 00:49 UTC
- 品質フラグ: COLLECTING

## 収集結果

### INFO-001
- **タイトル:** Introducing Grok 4.6
- **ソース:** xAI (SpaceXAI) 公式ニュース
- **公開日:** 2026-08-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02, KIQ-003-01
- **関連企業:** xAI
- **要約:** xAIがGrok 4.6をリリース。長時間実行エージェント（long-running agents）とインタラクティブ・ビジュアル作業に特化し、Grok 4.5の後継。AA Intelligence Index 61でGPT-5.6 Sol Maxと並ぶ。Cursor・Grok Build・API・OpenRouter/Vercel/Cloudflareで利用可能。
- **キーファクト:**
  - AA Intelligence Index: Grok 4.6=61, GPT-5.6 Sol Max=61, Fable 5 Max=62, Grok 4.5 High=56
  - CursorBench v3.2 69.9% / DeepSWE v1.1 65.9% / Terminal-Bench v3.0 26% / APEX-Agents 57.5%
  - API価格: $2/M入力トークン、$6/M出力トークン（fast版は2倍）
  - SFT軌道をGrok 4.5で再生成、kernel最適化・Web開発・CAD等のドメイン別エージェントRL
- **引用URL:** https://x.ai/news/grok-4-6
- **Evidence ID:** EVD-20260907-0001

### INFO-002
- **タイトル:** Grok Bot for Enterprise
- **ソース:** xAI (SpaceXAI) 公式ニュース
- **公開日:** 2026-09-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-01, KIQ-004-01
- **関連企業:** xAI
- **要約:** 自律エージェントチーム「Grok Bot」のエンタープライズ版提供開始。各Botはクラウド上で専用コンピュータを持ち人間と同じツール/アプリを操作。アクセス・ネットワーク・監査のコントロールで大規模ガバナンスに対応。Grok/Cursor Enterprise顧客は2週間無料。
- **キーファクト:**
  - 顧客例: Legora, Supermicro, ServiceTitan。数千組織が採用、エンジニアリング以外（営業・採用・マーケ・財務）での利用が最重度
  - ユーザーごとに分離されたセキュア環境、デフォルトでアクセス権なし
  - Cursor Enterpriseとの統合提供（cursor.comのドキュードにセキュリティ設計）
- **引用URL:** https://x.ai/news/grok-bot-for-enterprise
- **Evidence ID:** EVD-20260907-0002

### INFO-003
- **タイトル:** Previewing the Model Hardware Standard
- **ソース:** Anthropic 公式ニュース
- **公開日:** 2026-08-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-03, KIQ-005-01
- **関連企業:** Anthropic
- **要約:** AIエージェントが物理デバイス（顕微鏡・液体ハンドラ・ロボットアーム等）を安全に操作するための共通仕様「Model Hardware Standard (MHS)」のリサーチプレビューを科学研究所・先進製造業の最初のグループに公開。HHMI Janelia Research Campusとの共同開発。将来オープンソース化予定。
- **キーファクト:**
  - 統合作業を週/月単位から時間/分単位に短縮する標準ドライバ（read/writeプリミティブ）
  - モデル非依存・MCP等の標準プロトコルで任意のエージェントハーネスからアクセス可能
  - 対象操作: 創薬実験のルーチンから量子コンピュータのレーザーキャリブレーションまで
- **引用URL:** https://www.anthropic.com/news/model-hardware-standard-research-preview
- **Evidence ID:** EVD-20260907-0003

### INFO-004
- **タイトル:** The next evolution of the Agents SDK
- **ソース:** OpenAI 公式
- **公開日:** 2026-08（正式日時は本文未記載・直近投稿）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIがAgents SDKに標準化インフラを導入: モデルネイティブなハーネス（ファイル・ツール横断操作）とネイティブサンドボックス実行。MCP、スキル（progressive disclosure / agentskills.io）、AGENTS.md、シェルツール、apply patchツールを primitives として統合。
- **キーファクト:**
  - エージェントループ向け「model-native harness」と安全な実行のための「native sandbox execution」
  - ツール使用はMCP経由、コード実行はshellツール、ファイル編集はapply patchツール
  - GPT-5.x系モデルに最適化された公式SDKとして lightweight 抽象化を維持
- **引用URL:** https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- **Evidence ID:** EVD-20260907-0004

### INFO-005
- **タイトル:** Claude Agent SDK v0.2.152リリース・Bunコンパイルバイナリ配布
- **ソース:** GitHub (anthropics/claude-agent-sdk-python) / npm
- **公開日:** 2026-09-02〜09-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDKのPython版v0.2.152（9/2リリース）とバンドルCLI 2.1.260（9/3コミット）を確認。npmパッケージはBunの `bun build --compile` によるコンパイル済みバイナリ配布に移行し、darwin-arm64等のプラットフォーム別実行ファイルをextractして利用する構成。
- **キーファクト:**
  - v0.2.152 (2026-09-02)、bundled CLI 2.1.260 (2026-09-03)
  - Python/TypeScriptライブラリのみ提供（code.claude.com/docs）
  - AnthropicのBun買収（companies.json記載）がSDK配布形態に反映
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-python
- **Evidence ID:** EVD-20260907-0005

### INFO-006
- **タイトル:** Introducing Managed Agents in the Gemini API（Antigravityハーネス）
- **ソース:** Google 公式ブログ
- **公開日:** 2026-05以降（antigravity-preview-05-2026）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Google
- **要約:** Gemini APIにマネージドエージェント「Managed Agents」を導入。1回のAPI呼び出しで指示・ツール・リモートLinux環境を提供し、Google自身のエージェントを支えるプロダクション-gradeエージェントハーネス「Antigravity」とGeminiモデルを共同最適化したものを構築基盤として利用可能。
- **キーファクト:**
  - agent="antigravity-preview-05-2026"、environment="remote"（Googleホストの隔離Linuxサンドボックス）
  - コード実行・ファイル管理・Web閲覧を統合（client.interactions.create API）
  - Google内製エージェント群と同じハーネスを開発者に開放
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/
- **Evidence ID:** EVD-20260907-0006

### INFO-007
- **タイトル:** Gemini Enterprise Agent Platform（旧Vertex AIの改名・統合プラットフォーム化）
- **ソース:** Google Cloud 公式ドキュメント/製品ページ
- **公開日:** 2026-09初頭（docs更新「5日前」表記）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** Vertex AIが「Gemini Enterprise Agent Platform」に改名。エンタープライズ-grade AIエージェントとモデルベースソリューションを構築・デプロイ・ガバナンス・最適化する統合プラットフォームとして位置づけ。
- **キーファクト:**
  - 「formerly Vertex AI」の明記（cloud.google.com/products/gemini-enterprise-agent-platform）
  - 構築・デプロイ・ガバナンス・最適化の4機能を統一プラットフォームで提供
  - Gemini API経由でGeminiモデルにアクセス（JS/Pythonコード例）
- **引用URL:** https://cloud.google.com/products/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260907-0007

### INFO-008
- **タイトル:** xAI Agent Tools API・grok-build-0.1コーディングモデルAPI提供
- **ソース:** xAI (SpaceXAI) 公式
- **公開日:** 2026（Grok 4.1 Fast同時期〜）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIはサーバーサイドツール群「Agent Tools API」（web_search、x_search、code_execution、collections_search、MCP接続）でGrokを完全自律エージェントとして動作可能。コーディング特化モデル「grok-build-0.1」をAPI提供し、Grok Build TUI・Cursor・OpenClaw・Kilo Code・OpenCode等のハーネスで動作。
- **キーファクト:**
  - APIベースは https://api.x.ai/v1（OpenAI互換 responses エンドポイント）
  - grok-4.6がResponses APIの主力モデル（docs.x.ai/overview）
  - Grok Build はGitHub公開のターミナル型コーディングエージェント（xai-org/grok-build）
- **引用URL:** https://x.ai/news/grok-4-1-fast
- **Evidence ID:** EVD-20260907-0008

### INFO-009
- **タイトル:** ByteDance Coze 2.0→3.0進化とDoubao 2.1完全統合
- **ソース:** AI NEWS (aibase.com) / 百度百科 / X投稿
- **公開日:** 2026-01〜2026-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** Cozeは2026年1月にv2.0（Skill Store・Long-term Plan搭載、「Workplace AI」定位）、その後v3.0（Web/デスクトップ/モバイル横断のマルチエージェント対応）をリリース。2026-06-23にDoubao大模型2.1と完全統合。
- **キーファクト:**
  - Coze 2.0: スキルストアと長期計画機能、「Workplace AI」へ再定位
  - Coze 3.0: マルチエージェント機能追加、全プラットフォーム展開
  - 2026-06-23 Doubao 2.1完全統合（百度百科英語版記載）
- **引用URL:** https://news.aibase.com/news/24737
- **Evidence ID:** EVD-20260907-0009

### INFO-010
- **タイトル:** 2026年エージェントフレームワーク比較: LangGraph 37kスター・主要ラボ全社がSDK提供
- **ソース:** Towards AI / Langfuse / Speakeasy（3ソース整合）
- **公開日:** 2026-07比較表更新
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** （業界全体）
- **要約:** 2026年はOpenAI・Anthropic・Google全社がエージェントSDK/ADKを提供、MicrosoftはAutoGenをスクラッチ再構築（Agent Framework=AutoGen+Semantic Kernel後継）。LangGraphが37,000 GitHubスターで本番標準、CrewAIは資金調達とエンタープライズ機能を提供。
- **キーファクト:**
  - LangGraphは患者データ・金融取引等コンプラ要件向けの唯一の本番-ready選択肢との評価（Towards AI）
  - Langfuse比較表（2026年7月時点）: LangGraph/DeepAgents/OpenAI Agents SDK/Claude Agent SDK/Google ADK/Pydantic AI/CrewAI/Strands/Mastra/Vercel AI SDK/MS Agent Framework/Agno/Smolagents
  - 医療事例でLangGraphの文脈分離実装により精度71%→93%（Towards AI検証報告）
- **引用URL:** https://langfuse.com/blog/2025-03-19-ai-agent-comparison
- **Evidence ID:** EVD-20260907-0010

### INFO-011
- **タイトル:** From assistance to execution: How enterprises put AI to work
- **ソース:** OpenAI 公式
- **公開日:** 2026-09（直近）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-004-01
- **関連企業:** OpenAI
- **要約:** OpenAIが企業利用実態レポートを公開。エンタープライズCodexの週間アクティブユーザーは2月以降、法務108倍・営業41倍・採用41倍・マーケ26倍とエンジニアリング(5倍)を大きく上回る成長。「フロンティア企業」とそれ以外の格差が拡大。若手・初期キャリア社員の方がAIを多く使用。
- **キーファクト:**
  - 週アクティブ企業Codexユーザー成長率: 法務108×/営業41×/採用41×/マーケ26×/エンジニアリング5×（2026年2月比）
  - プラグイン・スキル等の高度機能はフロンティア企業で普及も、全体では可能な範囲のごく一部
  - アクセスだけではスケール不十分——会社コンテキスト・ツール・反復ワークフローへの接続が格差要因
- **引用URL:** https://openai.com/index/how-enterprises-put-ai-to-work/
- **Evidence ID:** EVD-20260907-0011

### INFO-012
- **タイトル:** Gemini Enterprise Agent Platform SLA 99.5%・旧Vertex AI全家販の改名完了
- **ソース:** Google Cloud 公式SLAページ群
- **公開日:** 2026-09（docs更新）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** Gemini Online Inference API on Gemini Enterprise Agent PlatformのSLAは99.5%。Vertex AI Vision→「Gemini Enterprise Agent Platform Vision」等、全家販の改名がSLA文書まで完了し、エンタープライズ契約体系がGemini Enterpriseブランドに統一。
- **キーファクト:**
  - SLA 99.5%（金融クレジット規定あり・SLO不達時の唯一救済）
  - Vertex AI Search for Commerce→AI Commerce Search on Gemini Enterprise等の改名が進行
  - CloudZero分析: Vertex AI価格は$0.10/1M起点、月$100未満（試作）〜$100,000+（大企業）
- **引用URL:** https://cloud.google.com/vertex-ai/generative-ai/sla
- **Evidence ID:** EVD-20260907-0012

### INFO-013
- **タイトル:** Gemini EnterpriseサブスクリプションがantigravityをGoogle Cloud標準のセキュリティ・コンプラ保護下に
- **ソース:** Google Cloud 公式（Facebook投稿）
- **公開日:** 2026-09-06（12時間前）
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-02, KIQ-001-01
- **関連企業:** Google
- **要約:** Gemini Enterpriseサブスクリプションにより、エージェントハーネス「antigravity」がGoogle Cloudの標準セキュリティ・コンプライアンス保護の管轄下に入ったと公式アカウントが発表。管理者・ITチームによるガバナンス対応を強調。
- **キーファクト:**
  - antigravity（Managed Agentsのハーネス）が企業セキュリティ枠組みに統合
  - 管理者・IT部門による標準的なセキュリティ/コンプライアンス管理適用
- **引用URL:** https://www.facebook.com/googlecloud/posts/1402829528661037/
- **Evidence ID:** EVD-20260907-0013

### INFO-014
- **タイトル:** エンタープライズAIアシスタント比較: 4大プラットフォームのコンプライアンス認証状況
- **ソース:** Intuition Labs（比較記事・一次認証ページ参照付き）
- **公開日:** 2026-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI, Anthropic, Microsoft, Google
- **要約:** Claude Enterprise/ChatGPT Enterprise/M365 Copilot/Gemini Enterpriseのセキュリティ認証を比較。ChatGPT Enterprise: CSA STAR・SOC 2 Type 2・ISO 27001/17/18/27701。Claude Enterprise: SOC 2・ISO 27001・ISO 42001・GDPR/CCPA。Gemini Enterprise: SOC 1/2/3・ISO 27001/17/18/27701・PCI DSS・BSI C5。
- **キーファクト:**
  - AnthropicがAI管理システムISO/IEC 42001:2023認証を取得済み（support.claude.com一次リンク付き）
  - AktoのClaude Compliance API統合がClaude Enterpriseのチャット・ファイル・コネクタ・MCP横断の可視性を提供（3日前）
  - 規制産業向けプラットフォーム選定ではSOC 2/FedRAMP/HIPAA/GDPRが必須条件化（Seekr）
- **引用URL:** https://intuitionlabs.ai/articles/enterprise-ai-assistants-comparison
- **Evidence ID:** EVD-20260907-0014

### INFO-015
- **タイトル:** Stanford「Enterprise AI Playbook」: 51の成功事例に共通する変数
- **ソース:** Stanford Digital Economy Lab
- **公開日:** 2026（直近）
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** 5か月間で51の企業AI開発事例を分析。同一技術でも変革期間は数週間から数年に分布し、成功変数は技術以外（組織・データ基盤等）にあると示唆。DeloitteもエージェントAI企業導入ガイドを公開。
- **キーファクト:**
  - 51事例・5か月の観察で「週単位」から「年単位」まで変革速度が分布
  - Deloitte: エージェントAI導入は効率・生産性・動的スケールの変革を推進
  - Appian: エラーバジェットほぼゼロ・コンプラ・倫理領域はエージェント不適との境界設定
- **引用URL:** https://digitaleconomy.stanford.edu/publication/enterprise-ai-playbook/
- **Evidence ID:** EVD-20260907-0015

### INFO-016
- **タイトル:** MCP生態系の規模: 公開サーバー10K+・月次SDKダウンロード97M+
- **ソース:** Digital Applied（一次はAnthropic AAIF発表・GitHub APIスナップショット）
- **公開日:** 2026-05-24検証時点
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic, （業界全体）
- **要約:** Model Context Protocolの採用が急拡大。公開MCPサーバー10K以上（Anthropic 2025年12月発表）、月次SDKダウンロード97M以上、公式serversリポジトリは86,148スター/10,799フォーク（2026-05-24 GitHub API）。主要AIプラットフォーム全体がMCPクライアント/サーバー/コネクタをドキュメント化。
- **キーファクト:**
  - modelcontextprotocol/servers: 86,148 stars / 10,799 forks（2026-05-24時点）
  - MCP登場は2024-11-25（Anthropic）→ Linux Foundation傘下AAIFへ寄贈
  - 100サーバーストレステスト研究も公開（信頼性・レイテンシ・ツール呼び出し成功率）
- **引用URL:** https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol
- **Evidence ID:** EVD-20260907-0016

### INFO-017
- **タイトル:** OpenAIがLinux Foundation傘下Agentic AI Foundation (AAIF) 共同設立・AGENTS.md寄贈
- **ソース:** OpenAI公式 + Linux Foundation公式プレス（2ソース整合）
- **公開日:** 2025-12-09（LF発表）
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Anthropic, Linux Foundation
- **要約:** Linux FoundationがAAIF設立を発表。寄贈プロジェクトはMCP（Anthropic）、goose（Block）、AGENTS.md（OpenAI・2025年8月リリース）。OpenAIは共同設立メンバーとして参加。中立財団による標準管理で「企業OSSへの抵抗層」の採用も見込む。
- **キーファクト:**
  - AAIF設立日2025-12-09・アンカープロジェクトはMCP/goose/AGENTS.md
  - Bloombergは金融規制環境向けの安全なMCP拡張を約束（Supporting Quote）
  - AGENTS.md: コーディングエージェントにリポジトリ横断で一貫したプロジェクト指示を与える標準
- **引用URL:** https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- **Evidence ID:** EVD-20260907-0017

### INFO-018
- **タイトル:** OpenAI Skills API（/v1/skills）とhosted shell・curated skills
- **ソース:** OpenAI 公式開発者ドキュメント
- **公開日:** 2026-09時点の現行仕様
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIのSkills APIはSKILL.md+スクリプトをディレクトリ/zipでアップロードし、shellツールのcontainer_auto環境からskill_referenceで呼び出す構成。curated skills（例: openai-spreadsheets）は公式キュレーション配布。ローカルshellモードも選択可能。
- **キーファクト:**
  - POST /v1/skills でスキル登録、Responses APIのtools[].type="shell"環境でskills参照
  - ドキュメント例のモデルは「gpt-6-astra」（現行フラッグシップ系モデル名）
  - ChatGPT向けSkillsビルドドキュメントも整備（learn.chatgpt.com）・MCP依存関係宣言対応
- **引用URL:** https://developers.openai.com/api/docs/guides/tools-skills
- **Evidence ID:** EVD-20260907-0018

### INFO-019
- **タイトル:** エージェント間連携標準A2A+MCPによる企業エコシステム統合の進展
- **ソース:** Workday Newsroom / Kore.ai / Salesforce
- **公開日:** 2025-06〜2025-11（継続展開）
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** Workday, Microsoft, Google, AWS, Accenture
- **要約:** Workday Agent Partner NetworkはAccenture/AWS/Google Cloud/Microsoft/PwC等のエージェントをAgent System of Recordに接続し、共有プロトコルにMCPとAgent-to-Agent Protocol (A2A)を使用。Microsoftは「Agent 365」をローンチしKore.ai等がローンチパートナー。エンタープライズSaaS横断のエージェント相互運用が標準化しつつある。
- **キーファクト:**
  - Workday Agent GatewayはMCP+A2AでWorkday内外のエージェント協調を実現
  - Microsoft Agent 365: Kore.aiがローンチパートナー（2025-11-18）として統合ガバナンス提供
  - Salesforce AgentforceもA2Aベースのエージェント統合を製品化
- **引用URL:** https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces
- **Evidence ID:** EVD-20260907-0019

### INFO-020
- **タイトル:** AIエージェント市場規模予測: 2033年に$182.97B・CAGR 49.6%
- **ソース:** Grand View Research（SoftTeco記事引用）/ Gartner（OpenSourceForYou投稿引用）
- **公開日:** 2026-09（引用時点）
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03, KIQ-003-04
- **関連企業:** （業界全体）
- **要約:** Grand View ResearchはグローバルAIエージェント市場を2033年$182.97B・2026年以降年率49.6%成長と予測。Gartner予測では2028年までに企業ソフトウェアの33%がエージェントAI内蔵（2024年<1%から）。
- **キーファクト:**
  - 市場予測: $182.97B by 2033・CAGR 49.6%（Grand View Research）
  - 2028年: 企業ソフトの33%がagentic AI搭載（Gartner・2024年の<1%から）
  - OpenAI公式: AIネイティブ企業（Basis/Clay/Exa Labs）が従業員オンボーディング・アカウント管理にエージェント内蔵
- **引用URL:** https://softteco.com/blog/ai-agent-development-cost
- **Evidence ID:** EVD-20260907-0020

### INFO-021
- **タイトル:** Gemini Robotics ER 2・Gemini Robotics 2: ロボティクス特化VLMの公開
- **ソース:** Google Cloud公式ドキュメント + DeepMind関連報道（2ソース）
- **公開日:** 2026-09初頭（docs更新3日前）
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** Googleは物理世界推論に特化したVLM「Gemini Robotics ER 2」をプレビュー公開（131Kコンテキスト、マルチモーダル入力、ツールオーケストレーション、$2/$10価格）。Gemini Robotics 2はヒューマノイドロボットにリアルタイム空間認識を与えるマルチモーダル基盤モデル。
- **キーファクト:**
  - Gemini Robotics ER 2: ロボティクス向け高度推論・視覚データ解釈・Agent Platform経由で提供
  - Gemini Robotics 2: 環境理解と適応を行うヒューマノイド向け基盤モデル（DeepMind）
  - 生成メディア: Gemini Omni Flash（ネイティブ音声付き高速動画生成・gemini-omni-1.1-flash）
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/gemini-robotics-er
- **Evidence ID:** EVD-20260907-0021

### INFO-022
- **タイトル:** マルチモーダルLLMランキング: Qwen3.8 Maxが87.1で首位（オープンモデル）
- **ソース:** BenchLMリーダーボード
- **公開日:** 2026-08-27時点
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02, KIQ-003-03
- **関連企業:** Alibaba, Moonshot AI, Anthropic, Google, OpenAI
- **要約:** マルチモーダル部門の総合首位はAlibaba Qwen3.8 Max（87.1）、Kimi K3（86.2）、Claude Opus 5（85.9）が続く。グラウンデッド視覚推論ではGemini 3 Pro Deep Thinkが95、Claude Mythos 5が92.8、GPT-5.1が91.8（$1.25/$10と低価格）。
- **キーファクト:**
  - 総合prov. avg: Qwen3.8 Max 87.1 > Kimi K3 86.2 > Claude Opus 5 85.9
  - グラウンデッド理解: Gemini 3 Pro Deep Think 95 > Claude Mythos 5 92.8 > GPT-5.1 91.8
  - オープン weight モデルがマルチモーダル首位という象徴的出来事
- **引用URL:** https://benchlm.ai/best/multimodal
- **Evidence ID:** EVD-20260907-0022

### INFO-023
- **タイトル:** MMLUスコア: GPT-5.2が93.5%で首位・Gemini 3.1 Pro 92.6%
- **ソース:** LM Market Capベンチマーク集計
- **公開日:** 2026-09時点
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** OpenAI, Google, DeepSeek, Meta
- **要約:** MMLUでGPT-5.2（93.5%）> GPT-5.1（93.2%）> GPT-5（93.0%）> Gemini 3.1 Pro Preview（92.6%・hybrid）。DeepSeek V3.2は88.5%、Llama 4 Maverick 88.0%、Llama 4 Scout 79.6%。
- **キーファクト:**
  - Elite tier: GPT-5.2/5.1/5、Gemini 3.1 Pro、Gemini 2.5 Pro（90.8%）
  - オープン系最上位: DeepSeek V3.2 88.5% — 首位GPT-5.2と5.0pt差
  - Gemini 3.1 Proは「hybrid」分類で従来モデルとアーキテクチャ区分が異なる
- **引用URL:** https://lmmarketcap.com/benchmarks
- **Evidence ID:** EVD-20260907-0023

### INFO-024
- **タイトル:** ブラウザ自動化エージェント基盤の勃興: Browser Use 112.5Kスター・$0.02/hr
- **ソース:** Browser Use公式/GitHub + Firecrawl + Browserbase（3ソース）
- **公開日:** 2026-09時点
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-04, KIQ-001-03
- **関連企業:** （業界全体）Browser Use, Browserbase
- **要約:** オープンソースのBrowser Useが112.5K GitHubスター・月46Mダウンロードに到達し、クラウドブラウザ$0.02/hrで最安。Claude Code/Codex/Cursor/Hermes/OpenClaw等のコーディングエージェントにskillとして組み込む使い方が標準化。モデル例はgpt-5.5/claude-sonnet-4-6/gemini-3-pro。
- **キーファクト:**
  - 競合クラウドブラウザ価格: Browser Use $0.02/hr < Notte/Anchor $0.05 < Browserbase $0.12/hr
  - DeepMindがBrowserbaseの掲載顧客（ログ一覧）
  - 「APIが届かない85%のWeb」へのアクセスを商品化（Browserbase）
- **引用URL:** https://browser-use.com/
- **Evidence ID:** EVD-20260907-0024

### INFO-025
- **タイトル:** Claude Codeサンドボックス・アーキテクチャとcode execution tool（ネット遮断コンテナ）
- **ソース:** Anthropic Engineering / Claude Platform Docs（公式）
- **公開日:** 2026-09時点の現行仕様
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** AnthropicはClaude Codeにsandbox runtime（プロセス全体・MCPサーバー・フックをOS境界で隔離、Docker不要）とホスト型フルOS「Claude Code on the web」を提供。APIのcode execution toolはインターネットアクセスなしのコンテナで動作し、MCP経由のコード実行はトークン消費を平均37%（最大98%）削減。
- **キーファクト:**
  - sandbox runtimeはBashだけでなくfile tools・MCPサーバー・hooks全体を1つのOS境界で拘束
  - code_execution_20250825: 電源断なしの安全コンテナ・事前インストールライブラリのみ・追加課金なし
  - ドキュメント例の現行モデル: claude-opus-5 / Claude Mythos Preview（Claude API + Microsoft Foundry対応）
- **引用URL:** https://www.anthropic.com/engineering/claude-code-sandboxing
- **Evidence ID:** EVD-20260907-0025

### INFO-026
- **タイトル:** スキルマーケットプレイス激増: 2025年12月1レジストリ→2026年Q2に8大市場
- **ソース:** Agensi / skills.sh / SkillsMP（3ソース）
- **公開日:** 2026-Q2〜Q3
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** （業界全体）Vercel, Anthropic
- **要約:** SKILL.mdオープン標準を軸にスキル配布市場が急拡大。Vercel-backed skills.sh（2026年1月ローンチ・npm型パッケージマネージャ、トップスキル70万+インストール）、Agensi（5,000+スキル・8ポイントセキュリティスキャン・クリエイター収益分配80/20）、SkillsMP（GitHub走査80万+スキル）等。スキルはClaude Code/Cursor/Codex CLI/Gemini CLI等20+エージェントで横断動作。
- **キーファクト:**
  - Agensi: 5,000+スキル・6,000+ユーザー・400+クリエイター（有料スキル$5-$35）
  - skills.sh: トップスキル700,000+インストール、Claude Code/Cursor/Copilot対応
  - スクレイピング型（SkillsMP 80万+/LobeHub 16.9万+）はセキュリティ審査なし——監査は自己責任
- **引用URL:** https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
- **Evidence ID:** EVD-20260907-0026

### INFO-027
- **タイトル:** 悪意あるスキル/MCPサーバーによるエージェント乗っ取りリスク（Shadow AI）
- **ソース:** BeyondTrust + The Hacker News + arXiv論文（3ソース）
- **公開日:** 2026-08〜09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-05, KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** Codexスキルのタイポスクワッティング（例: opnai/codex-research-skills）や悪意あるMCPサーバー・プラグイン・リポジトリ設定が、資格情報窃取・データ流出・コード実行に使われる実例が報告。arXiv論文はスキル読み込みパス（.claude/skills/*/SKILL.md）経由の「コンテキスト権限昇格攻撃」を形式化。
- **キーファクト:**
  - BeyondTrust: exec_commandツール昇格経路（~/.codex/rules/default.rules改竄）
  - Hacker News (2026-08): 認可済みAIツール内に潜伏するShadow AIの実例報告
  - arXiv 2609.01222: Context Privilege Escalation Attacks——スキルロードパス共通脆弱性
- **引用URL:** https://www.beyondtrust.com/blog/entry/malicious-codex-skills-ai-agent-security
- **Evidence ID:** EVD-20260907-0027

### INFO-028
- **タイトル:** エンタープライズAIスイッチングコストの「4経路同時蓄積」問題
- **ソース:** VaaS Block研究（Hamilton Helmer Seven Powers適用）
- **公開日:** 2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** Microsoft, Salesforce, ServiceNow, AWS
- **要約:** Copilot（M365/Teams/GitHub埋込・習慣形成）、Agentforce（CRM移行18-36か月と複合）、ServiceNow AI（数万エンジニア時間の構成と不可分）、Bedrock（IAM/VPC/S3との統合）の4経路でスイッチングコストが同一組織内で同時に蓄積し、集計測定の責任者が誰にも存在しない「アカウンタビリティ・ギャップ」を指摘。
- **キーファクト:**
  - Copilot利用は席の3.3%だが、その3%に行動依存が集中しロックインは蓄積
  - Agentforce脱退は暗黙にCRM移行（18-36か月・失敗率CFO拒否水準）を伴う
  - 買い手は能力評価、売り手はスイッチングコスト蓄積キャンペーン——交渉前に敗北
- **引用URL:** https://www.vaasblock.com/research/enterprise-ai-vendor-lock-in-switching-costs-copilot-agentforce-2026/
- **Evidence ID:** EVD-20260907-0028

### INFO-029
- **タイトル:** 平均企業移行コスト$315KとAzure AI Foundryの「超加算的」ロックイン
- **ソース:** Kong（CIO Dive引用）+ DiVA学術論文（2ソース）
- **公開日:** 2026
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05, KIQ-002-01
- **関連企業:** Microsoft, AWS, OpenAI
- **要約:** 平均エンタープライズ移行プロジェクトは$315K（CIO Dive）。学術研究はAzure AI Foundryの多層依存（technical/data/commercial）が「super-additive lock-in」を生むと実証: EDP割引が最深の顧客が最高の退出コストに直面する構造。Azure OpenAIは2025年初頭に大幅値上げし予算前提を崩した実例も。
- **キーファクト:**
  - 移行平均$315K（データ移行・リファクタ・再訓練・ダウンタイム込み）
  - 2025-01 ChatGPT大規模障害: 単一ベンダー依存企業は代替経路なし
  - Builder.ai崩壊（2025）: 資金豊富なプラットフォームも消失するリスク実例
- **引用URL:** https://konghq.com/blog/learning-center/vendor-lock-in
- **Evidence ID:** EVD-20260907-0029

### INFO-030
- **タイトル:** AvePoint警告「Fable 5」復帰時の価格戦略——マルチモデル戦略の必要性
- **ソース:** AvePoint
- **公開日:** 2026
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-01, KIQ-003-05
- **関連企業:** Anthropic
- **要約:** 「Fable 5が復帰した際、AnthropicはそれをOpus 4.8の2倍の従量課金に移行し、同社がリストした中最高額のモデルにした」と報告。単一ベンダー依存のコストリスクの実例として、エージェント・ガバナンスにおけるマルチモデル戦略を推奨。
- **キーファクト:**
  - Fable 5はOpus 4.8の2倍価格で従量課金化（Anthropicリスト内最高額）
  - コストリスクは静かに進行——代替なき値上げの吸収を強制
  - 注: 「Fable 5」のAnthropic帰属はAvePoint記載のみで単ソース（要交叉確認）
- **引用URL:** https://www.avepoint.com/blog/manage/ai-vendor-lock-in-multi-model-strategy
- **Evidence ID:** EVD-20260907-0030

### INFO-031
- **タイトル:** Amazon Bedrock AgentCore——エージェント構築・接続・最適化の統合プラットフォーム
- **ソース:** AWS公式
- **公開日:** 2026-09時点の現行製品
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** AWSはBedrock AgentCoreを「エージェントの構築・システム接続・ツールコール保護・デバッグ・最適化を1プラットフォームで」と提供。Bedrock Agentsはメモリ保持（タスク連続性）とGuardrails内蔵を明記。CLI/APIはオーケストレーション型（custom/LLM）・エージェント間協調（agent-collaboration）・メモリ設定に対応。
- **キーファクト:**
  - AgentCore=構築・接続・セキュアなツールコール・デバッグ・運用のフルライフサイクル
  - Agents: memory retention と Guardrails 標準搭載
  - update-agent API: orchestration-type/custom-orchestration/agent-collaboration/memory-configuration
- **引用URL:** https://aws.amazon.com/bedrock/agentcore/
- **Evidence ID:** EVD-20260907-0031

### INFO-032
- **タイトル:** Microsoft Foundry Agent Service——任意フレーム/任意モデルでエージェントを統合ガバナンス
- **ソース:** Microsoft Azure公式
- **公開日:** 2026-09時点の現行製品
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Foundry Agent Serviceは任意フレームワーク・任意サポートモデルでエージェントを構築・デプロイ・スケールするマネージドプラットフォーム。Microsoft Foundry全体は「AIアプリとエージェントの工場」としてエージェントライフサイクル全体を統合。AnthropicのClaude Mythos PreviewがMicrosoft Foundry上でcode execution対応（INFO-025）。
- **キーファクト:**
  - Foundry Agent Service: ガバナンス・可観測性・エンタープライズ統合を標榜
  - Microsoft Agent Framework（AutoGen+Semantic Kernel後継）との学習パス統合
  - Igniteで簡略化された開発者体験をローンチ済み
- **引用URL:** https://azure.microsoft.com/en-us/products/ai-foundry/agent-service
- **Evidence ID:** EVD-20260907-0032

### INFO-033
- **タイトル:** 汎用ワークエージェント製品比較: Claude Cowork・Gemini Enterprise・OpenClaw
- **ソース:** Artificial Analysis（エージェント比較表）
- **公開日:** 2026-09時点
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** Anthropic, Google, （OpenClaw=OSS）
- **要約:** Anthropic「Claude Cowork」（2026年1月、$20-200/月、隔離環境でタスク実行・ローカルファイルアクセス・computer use/MCPコネクタ/ブラウザ拡張接続）。Google「Gemini Enterprise」（2025年10月、$21-30/月、Workspace/M365/Salesforce/Jira/Confluence/Boxコネクタ、権限認識検索、Deep Research等プリビルド）。OSSのOpenClaw（2025年11月、セルフホスト・WhatsApp/Slack/Teamsを自律アシスタント化）。
- **キーファクト:**
  - Claude Cowork: デスクトップでローカルファイル編集・プリセットスキル（Excel等）
  - Gemini Enterprise: ノーコードワークベンチ+Code Assist内蔵
  - OpenClaw: コミュニティSkillsマーケットプレイスとNVIDIA NemoClawスタックでスケール
- **引用URL:** https://artificialanalysis.ai/agents
- **Evidence ID:** EVD-20260907-0033

### INFO-034
- **タイトル:** 採用のパラドックス: アプリの80%がエージェント内蔵・本番運用組織は31%
- **ソース:** Gartner + S&P Global Market Intelligence + Microsoft（3ソース、Digital Applied集計）
- **公開日:** 2026-Q1データ（Microsoft投稿2026-02-10）
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界全体）Microsoft
- **要約:** 2026年Q1に出荷/更新された企業アプリの80%が少なくとも1つのAIエージェントを内蔵（Gartner）する一方、プロダクションでエージェントを稼働させる組織は31%止まり（S&P Global）。Fortune 500の80%以上がlow-code/no-codeツールで構築したアクティブなエージェントを使用（Microsoft公式ブログ）。
- **キーファクト:**
  - 2024→2026: エージェント内蔵アプリ33%→80%、本番運用組織9%→31%
  - マルチエージェント(3+)オーケストレーション活用は1%→22%
  - 「agent owner」役職を置く組織は11%→56%へ急増
- **引用URL:** https://www.digitalapplied.com/blog/ai-agent-adoption-2026-enterprise-data-points
- **Evidence ID:** EVD-20260907-0034

### INFO-035
- **タイトル:** PwC調査: 79%の幹部が「AIエージェント導入済み」回答
- **ソース:** PwC（AI agent survey）
- **公開日:** 2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** PwC調査で79%が自社でAIエージェント採用済みと回答。内訳は限定導入27%・幅広い導入35%・全社導入17%・検討中15%・導入予定なし4%。名目採用率と実稼働（INFO-034の31%）の乖離が読み取れる。
- **キーファクト:**
  - 幅広い導入35% + 限定導入27% + 全社導入17% = 採用済み79%
  - 「開始予定なし」はわずか4%
  - Prefactor集計: 2026年末までにエンタープライズアプリの40%がタスク特化エージェントを内蔵予測（2025年<5%から）
- **引用URL:** https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html
- **Evidence ID:** EVD-20260907-0035

### INFO-036
- **タイトル:** ROIの実態: 88%がAI利用するも5%+のEBIT寄与は6%のみ・現場は4:1 ROI
- **ソース:** McKinsey State of AI 2025 + AI4SP + Code with Claude London（3ソース）
- **公開日:** 2026（会議報告は5月19日の週）
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-004-01
- **関連企業:** （業界全体）Anthropic
- **要約:** McKinsey: 88%の組織がAIを常用するが5%以上のEBIT寄与を報告するのは6%のみ。AI4SP: 企業の80%はAIからROIゼロ、42%の企業AIプロジェクトが本番前に行き詰まり。一方Code with Claude London会議の企業チームは4:1 ROI（増分PR単価$37.50 vs 開発者時間$150）を報告——成功例と平均の二極化。
- **キーファクト:**
  - McKinsey: 88%常用 vs 6%のみがEBIT 5%+寄与
  - AI4SP: 80%ゼロROI・42%が本番前断念
  - Code with Claude London: エンタープライズチームの4:1 ROI・PR単価$37.50（vs $150人件費）
- **引用URL:** https://www.digitalapplied.com/blog/ai-agent-roi-calculator-enterprise-business-case
- **Evidence ID:** EVD-20260907-0036

### INFO-037
- **タイトル:** EU AI Act: Chapter V執行開始・最高€35Mまたは全世界売上7%の制裁
- **ソース:** EU AI Act公式ポータル + Sentra（2ソース）
- **公開日:** 2026-03-31執行
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** EU AI Actは「理論から執行」段階に移行。Chapter V（一般目的AIモデル）の執行が2026-03-31に開始。禁止行為の執行は即時有効で最大€35Mまたは全世界売上の7%の制裁。Article 15は高リスクシステムの精度・頑健性・サイバーセキュリティ要求を定める。
- **キーファクト:**
  - Article 15(5): 許可なし変更・敵対的回避の試みに対する耐性要求
  - デプロイヤー（企業ユーザー）向け義務とSME簡素化措置を併存
  - 執行は加盟国レベル+EU AI Officeの二層構造
- **引用URL:** https://artificialintelligenceact.eu/
- **Evidence ID:** EVD-20260907-0037

### INFO-038
- **タイトル:** 大統領令14365号（2025年12月）: 州AI規制の先取りと連邦統一政策
- **ソース:** White House公式 + Wikipedia（2ソース）
- **公開日:** 2025-12
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** （米国政府）
- **要約:** トランプ政権はEO 14365「Ensuring a National Policy Framework for Artificial Intelligence」に署名。連邦機関に(A)統一的国内AI政策の策定、(B)州AI法の連邦法抵触評価と法的挑戦、(C)州のコンプライアンスを連邦資金の条件とすることを指示。児童安全・データセンターインフラ・州政府調達関連州法は免除。
- **キーファクト:**
  - 州規制の先取り（preemption）が明示的な政策目標
  - 2025-01: Biden EO 14110を撤回（EO 14148）→ EO 14179「AIにおける米国リーダーシップへの障害除去」
  - 米国はG20に対し新規AI規制回避を要請（Carolina Principles・Kratsios）
- **引用URL:** https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/
- **Evidence ID:** EVD-20260907-0038

### INFO-039
- **タイトル:** 大統領令14409号（2026年6月2日）: フロンティアAIの「自主的」セキュリティ枠組み
- **ソース:** White House公式 + CFR分析（2ソース）
- **公開日:** 2026-06-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** （米国政府）
- **要約:** EO 14409「Promoting Advanced Artificial Intelligence Innovation and Security」は連邦サイバーセキュリティ強化・AI搭載防御ツールの拡大・フロンティアAIモデルの安全な展開に関する自主的（voluntary）枠組みの構築・AI犯罪への執行優先を指示。5月版は90日レビュー窓が対中競争力を鈍らせる懸念で差し止えられた経緯がある。
- **キーファクト:**
  - フロンティアAI配備の安全枠組みは「自主的」——法的義務でない点がEUと対照的
  - AI搭載サイバー犯罪への執行優先
  - CFR専門家は「良い第一步だがより頑健な政策が必要」と評価
- **引用URL:** https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
- **Evidence ID:** EVD-20260907-0039

### INFO-040
- **タイトル:** 中国「擬人化AI対話サービス暫定弁法」2026年7月15日施行——コンパニオンAIへの許可制実質化
- **ソース:** Lexology + Barron's + Transcend（3ソース）
- **公開日:** 2026-07-15施行
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （中国政府）ByteDance
- **要約:** 中国は自然人の性格・思考パターン・コミュニケーション様式をシミュレートし持続的な感情的相互作用を提供するAIサービス（コンパニオンAI）向けの暫定弁法を施行。AI生成コンテンツのラベリング、連続2時間使用後のリマインダー、大規模事業者（登録100万+/MAU10万+）は省級CACへのセキュリティ評価提出が必須。
- **キーファクト:**
  - 対象外のグローバル企業も中国ユーザー向けペルソナAI提供で届出（実質ライセンス）義務の可能性
  - ユーザー相互作用データのグローバルモデル訓練への使用制限
  - Barron's: AI悪用取り締まりで560万件超の違法・有害情報を削除。AI Safety Governance Framework 2.0（2025-09-15）は雇用喪失等の「応用派生リスク」を新設
- **引用URL:** https://www.lexology.com/library/detail.aspx?g=a35cf048-7413-4c76-8d9c-b6e99f838690
- **Evidence ID:** EVD-20260907-0040

### INFO-041
- **タイトル:** NIST AI Agent Standards Initiativeと民間AARTS標準——エージェント安全標準の整備競争
- **ソース:** NIST + Gen Digital + IEEE Spectrum（3ソース）
- **公開日:** 2026
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-001-05
- **関連企業:** （米国政府）Gen Digital, Fujitsu
- **要約:** NISTが「AI Agent Standards Initiative」を開始——自律行動をするAIの信頼ある普及のための連邦標準整備。民間ではGen DigitalがAI Agent Runtime Safety Standard (AARTS)とSkill IDs（決定論的スキル識別）を公開、富士通は人間の監督なしで業務運用可能かを測る3つの安全ベンチマークを開発。
- **キーファクト:**
  - 連邦調達規則（FAR)にはAIエージェントのセキュリティ要求を定める条項が未整備（CSA研究ノート）
  - AARTS: エージェントホスト横断のランタイム決定強制
  - EU AI Act Service Desk: エージェントはAI Actの禁止規定（有害操作・脆弱性悪用）の直接的適用対象と公式回答
- **引用URL:** https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative
- **Evidence ID:** EVD-20260907-0041

### INFO-042
- **タイトル:** Anthropic×国防総省紛争の全体像: 「全合法用途」条項拒否→サプライチェーンリスク指定→$200M契約打切り
- **ソース:** Wikipedia紛争記事 + Axios + EFF + Fox Business（多ソース）
- **公開日:** 2026-01〜02（経緯）
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06, KIQ-002-03
- **関連企業:** Anthropic, xAI, OpenAI
- **要約:** Anthropicは国防総省によるClaudeの「全合法用途（all lawful purposes）」利用条項を、国内大量監視・完全自律致死兵器への懸念から拒否。2026-02-27にペンタゴンはAnthropicを「サプライチェーンリスク」に指定し、$200M契約を終了、他の全軍事請負業者にAnthropic製品の使用停止を命令。Anthropicは米政府分類ネットワーク上の最初のフロンティアAI企業だった。ヘグセス国防長官は1月に「woke AI」批判とともにxAI Grok契約を発表。
- **キーファクト:**
  - 2026-01: Semafor報道（致死兵器政策で対立）・Die Zeit（1/13 Hegseth Grok軍事利用発言）
  - 2026-02-14: Axios「ペンタゴン、AI安全規約をめぐりAnthropic契約打切りを脅迫」
  - 2026-02-27: サプライチェーンリスク指定・契約終了・全面的な使用停止命令（CNN）
  - 2026-03-04: ワシントンポスト——指定後もイラン作戦でClaude使用継続との報道
- **引用URL:** https://en.wikipedia.org/wiki/Anthropic%E2%80%93United_States_Department_of_Defense_dispute
- **Evidence ID:** EVD-20260907-0042

### INFO-043
- **タイトル:** OpenAI、Anthropicブラックリスト数時間後にペンタゴンと機密環境向け合意
- **ソース:** OpenAI公式 + CNBC + Reuters（3ソース）
- **公開日:** 2026-02-27〜28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI
- **要約:** Sam AltmanはAnthropicがブラックリスト入りした同日夜、国防総省との機密環境への先進AI配備合意を発表。「他のすべてのAI企業にも同じ条件を開放するよう要請した」と声明。バックラッシュ後に主要条項の修正をSNSで公表した経緯もある（Lawfare）。競合排除の「漁夫の利」構造の典型例。
- **キーファクト:**
  - 合意は分類ネットワークへのモデル配備（Reuters 2026-02-28）
  - AltmanのX投稿 (2027578652477821175) で即時発表
  - CAP: 「議会が行動すべき」との分析——調達によるガバナンスの限界
- **引用URL:** https://openai.com/index/our-agreement-with-the-department-of-war/
- **Evidence ID:** EVD-20260907-0043

### INFO-044
- **タイトル:** ペンタゴン、8社のAI企業と機密軍事作業の契約——「全合法用途」標準で
- **ソース:** The Guardian
- **公開日:** 2026-05-01
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-002-01
- **関連企業:** OpenAI, Google, xAI, SpaceX, Anthropic
- **要約:** ペンタゴンは8社のAI企業と機密軍事作業の契約を締結。各社は米軍による技術の「全合法用途（any lawful use）」展開に合意。Anthropicのみが先月の高調な対立で同水準の受け入れを拒否していた。Anthropicのサイバーセキュリティ特化モデル「Mythos」は堅牢なソフトウェアの脆弱性発見能力で政府当局者と銀行を動揺させた。
- **キーファクト:**
  - 8社契約: OpenAI/Google/SpaceX等が「any lawful use」基準を受け入れ
  - Google GeminiはGenAI.milで国防職員300万人全員に展開（2025-12 Breaking Defense）
  - OpenAIは2025-06にCDAO経由で$200M契約、SpaceXは政府契約総額約$22B
- **引用URL:** https://www.theguardian.com/us-news/2026/may/01/pentagon-us-military-pairs-with-spacex-google-openai
- **Evidence ID:** EVD-20260907-0044

### INFO-045
- **タイトル:** 連邦判事「違法的報復」とAnthropic指定撤去を命令——ペンタゴンは「効力継続」主張で拒否
- **ソース:** Quartz + mezha.net + Reason + Seeking Alpha（4ソース）
- **公開日:** 2026-08-31〜09-04
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 連邦判事はAnthropicのサプライチェーンリスク指定について「国防総省のAI利用見解への批判に対する違法な報復」と裁定し撤去を命令（約8/31）。しかし国防次官Emil Michaelは9/3（木）に「指定は依然有効」と発言、商務長官Lutnickは「問題は解決済み」と述べるなど政権内で分裂。控訴が継続中。
- **キーファクト:**
  - 判決: 報復的指定は違法（DoDのAI利用見解に対する批判が原因）
  - Reason (8/31): 「政府は好きなAIベンダーを選べるが、セキュリティは批判者を罰する白紙小切手ではない」（Lin）
  - 9/3時点: 判決と指定の並存——法廷vs行政の膠着
- **引用URL:** https://qz.com/pentagon-anthropic-supply-chain-risk-designation-090326
- **Evidence ID:** EVD-20260907-0045

### INFO-046
- **タイトル:** 「肩透かしの統治」: 法廷がNOと言っても効く強制手法——38名のAI関係者による chilling effect 主張
- **ソース:** Lawfare + Internet Lab提出amicus書簡（PDF）
- **公開日:** 2026-09-02〜04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Lawfareは「Governance by Shakedown」で、政権が法的口実を強制レバレッジに変換する手法を分析——「法廷が拒否しても戦術は機能する」構造を指摘。Anthropic PBC v. U.S. Department of War訴訟には38名のAI技術者によるamicus書簡が提出され、指定は「フロンティアAIの利益とリスクに関する専門的討議を冷え込ませる」と主張。
- **キーファクト:**
  - 事件名: Anthropic PBC v. U.S. Department of War et al.（amicus PDF公開済み）
  - Lawfare: 調達契約による軍事AI統治の限界——判決後も指定維持が実効的圧力
  - 萎縮効果は本KIQの核心仮説（安全性堅持企業が罰せられ順守企業が報われる構造）の直接証拠
- **引用URL:** https://www.lawfaremedia.org/article/governance-by-shakedown
- **Evidence ID:** EVD-20260907-0046

### INFO-047
- **タイトル:** ペンタゴン、Grok for GovernmentとChatGPTを軍事利用に本格導入（9/1発表）
- **ソース:** WGN-TV/The Hill + News10 + Polymarket投稿（3ソース）
- **公開日:** 2026-09-01
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-002-01
- **関連企業:** xAI, OpenAI, Scale AI, Google
- **要約:** ペンタゴンはStarshield AI（SpaceX傘下）の「Grok for Government」とOpenAIのChatGPTを非機密軍事利用に導入と発表。xAIとの合意でGrokモデルを国防総省公式生成AIプラットフォームGenAI.milに統合、国防職員300万人に展開。Scale AIとは軍事計画・作戦へのエージェント利用「Thunderforge」契約。
- **キーファクト:**
  - GenAI.mil: Google Gemini基盤→Grok/ChatGPT追加のマルチベンダー化
  - 軍事AI予算: サイバー軍AI $500M + AI搭載一方向攻撃システム $145M
  - Anthropic除外のまま競合3社（Google/xAI/OpenAI）+Scale AIが軍事エコシステムを形成
- **引用URL:** https://www.news10.com/hill-politics/pentagon-brings-on-grok-and-chatgpt-for-military-use/
- **Evidence ID:** EVD-20260907-0047

### INFO-048
- **タイトル:** 米エントリーレベル求人18か月で35%減——AIが主因（Revelio Labs/WEF）
- **ソース:** World Economic Forum + Revelio Labs + Stanford研究（3ソース）
- **公開日:** 2026
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-02
- **関連企業:** （業界全体）Cognizant
- **要約:** 米国のエントリーレベル求人は過去18か月で35%急減、主因はAI（Revelio Labs）。データ入力からコーディング、カスタマーサポートまで基礎タスクのAI化が進行。Stanford研究は3年でジュニア求人13%減を示唆。一方Cognizantは2025年に新卒25,000人を採用し2026年は超える見通し。
- **キーファクト:**
  - エントリーレベル求人 -35%（18か月・Revelio Labs）
  - Stanford: ジュニア職種の求人リストが3年で13%減
  - Cognizant AI責任者「大手IT企業への脅威は誇張」——新卒採用25,000人（2025）
- **引用URL:** https://www.weforum.org/stories/artificial-intelligence/how-ai-is-changing-the-nature-of-entry-level-work/
- **Evidence ID:** EVD-20260907-0048

### INFO-049
- **タイトル:** Klarna 4年で従業員50%減・AI削減後の「再雇用」の波
- **ソース:** Entrepreneur + tech.co + remotify（3ソース）
- **公開日:** 2026-09（投稿3-7日前）
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaは4年間で従業員を50%削減。Duolingoは2024年1月に契約業者10%をAI転換でオフボーディング。しかし「AIで削減した役割の再雇用を始めた企業」の報道が相次ぎ、タスク自動化から役割削除への移行が速すぎたとの教訓が語られる。
- **キーファクト:**
  - Klarna: 4年で50%減（AI統合による伝統的役割の冗長化と説明）
  - Duolingo: 2024-01契約社員10%オフボード
  - 再雇用事例の報道（6-7日前）: 「AIは人員を減らさないという意味ではない。役割削除が速すぎた」
- **引用URL:** https://tech.co/news/companies-replace-workers-with-ai
- **Evidence ID:** EVD-20260907-0049

### INFO-050
- **タイトル:** エージェント平均タスク完遂率75.3%: 8,128ユーザーパネル（Devin 86%〜Perplexity 65%）
- **ソース:** First Page Sage パネル（Digital Applied検証分析）
- **公開日:** 2026-04-09
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-04
- **関連企業:** OpenAI, Cognition, Perplexity
- **要約:** 8,128ユーザーのパネル（完遂率は487人のサブサンプル）で平均タスク完遂率75.3%。Devn 86%、OpenClaw 81%、OpenAI Agents 73%（MAU 2.7Mで最大）、Replit 69%、Perplexity 65%と21ポイントの格差。成功完了のうち追跟进力が必要だったのは18%のみ。平均時間節約66.8%。ただし54%はエージェント結果より手動検索を信頼。
- **キーファクト:**
  - 完遂率: Devin 86% > OpenClaw 81% > OpenAI Agents 73% > Replit 69% > Perplexity 65%
  - OpenClaw（旧Moltbot/Warelay、2026年1月改名）MAU 2.3M——OSSとして2位
  - WebArena構造化タスク: トップ68.7% vs 人間78%（2年前の約14%から急伸）
  - 注意: ベンダー委託パネルデータであり査読なし——業界定数ではない
- **引用URL:** https://www.digitalapplied.com/blog/ai-agent-task-completion-rates-2026-user-study-analysis
- **Evidence ID:** EVD-20260907-0050

### INFO-051
- **タイトル:** METR時間地平線研究と「10ステップ限界」: 長時間タスクの信頼性データ
- **ソース:** METR + MindStudio + Atlan（3ソース）
- **公開日:** 2026
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-005-01
- **関連企業:** （業界全体）
- **要約:** METRの「AI Ability to Complete Long Tasks」は50%成功率で達成できるタスク時間（time-horizon）が指数的に伸長する一方、実運用では68%のプロダクションエージェントが10ステップ以下で人間の介入を要する。構造化タスクでは85-95%の自律完遂が可能という業界目標値との格差が実態。
- **キーファクト:**
  - 68%の本番エージェントが10ステップ以下で人間介入必要（MindStudio業界データ）
  - 構造化タスクの目標自律完遂率: 85-95%
  - 人間92% vs GPT-4+プラグイン15%（初期ベンチマーク）——成果物完遂ベースでの格差
- **引用URL:** https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
- **Evidence ID:** EVD-20260907-0051

### INFO-052
- **タイトル:** 広告運用のエージェント自動化: ROAS +23%・キャンペーン開発73%高速化
- **ソース:** MindStudio + Fluency + Demandbase（3ソース）
- **公開日:** 2026
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-002-05
- **関連企業:** （業界全体）
- **要約:** マーケティングAIエージェントの実例: PPC最適化でROAS 10-25%改善、デバイス別入札自動調整でROAS 23%向上、キャンペーン開発73%高速化、見込み客167%増。AdOpsの定義タスク（コピー生成・キャンペーン分析・レポート）を特化エージェントが分担する構成が普及しつつある。
- **キーファクト:**
  - PPC自動最適化: ROAS +10-25%（小売実例）
  - キャンペーン開発73%高速化・資格ありリード167%増（利用企業報告）
  - Fluency: AdOps 4領域（コピー生成/分析/レポート/運用）のエージェント分担モデル
- **引用URL:** https://www.mindstudio.ai/blog/ai-powered-marketing-automation-idea-to-execution
- **Evidence ID:** EVD-20260907-0052

### INFO-053
- **タイトル:** Bain「Will Agentic AI Disrupt SaaS?」: 5シナリオ・3層スタック・セマンティック層の覇権争い
- **ソース:** Bain & Company（Technology Report）
- **公開日:** 2025〜2026継続
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05, KIQ-001-03
- **関連企業:** Salesforce, Microsoft, Google, Amazon
- **要約:** エージェントAIはSaaSを5シナリオ（No AI/AI強化/支出圧縮/AI優越/AI共食い）で再編。スタックは「記録システム→エージェントOS→成果インターフェース」の3層に再束Bundle。MCPとA2Aはツール呼び出し構文の標準化にとどまり、語彙・ポリシー意味層の標準が未整備——この意味層を握る者が次波の価値を収穫する「winner takes most」と予測。シート課金から成果課金への移行を指示。
- **キーファクト:**
  - OpenAI o3は2か月でコスト80%低下——3年以内に定型デジタル業務は「AIエージェント+API」へ
  - 4戦略シナリオ: core strongholds / open doors / gold mines / battlegrounds
  - 「中立エージェントプラットフォームになるか、それを支えるユニークデータを供給するか」の二択——両方はSalesforceなど数社のみ可能
- **引用URL:** https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
- **Evidence ID:** EVD-20260907-0053

### INFO-054
- **タイトル:** 60%のマーケティングリーダーがAIにより代理店支出を削減（2025年）
- **ソース:** Typeface Signal Report + Forrester/Star + DemandGenReport（3ソース）
- **公開日:** 2025-2026
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** （広告代理店業界）
- **要約:** Typeface調査ではマーケティングリーダーの60%が2025年にAI自動化の結果として代理店支出を削減。Forrester調査では47%のCMOが「代理店プラットフォームはAI自動化で不足」と回答。「広告代理店」への検索関心は約15%低下（19.2→16.4）。時間課金の代理店はAIによる制作時間30-50%+削減に比例した収入減に直面。
- **キーファクト:**
  - 60%が代理店支出削減（Typeface Signal Report）
  - 47%のCMO: 代理店のAI自動化が不十分（Forrester）
  - 時間課金モデルの構造的収入減——価値課金への転換が業界の生き残り条件
- **引用URL:** https://www.linkedin.com/pulse/how-ai-disrupting-traditional-marketing-agencies-while-townsend-2u2ce
- **Evidence ID:** EVD-20260907-0054

### INFO-055
- **タイトル:** プラットフォーマー直 pressing: Meta/Google/AmazonのAI広告プラットフォームが代理店モデルを脅かす
- **ソース:** Startups Magazine + InMobi + Razorpay（3ソース・SNS投稿含む）
- **公開日:** 2026-09（3-7日前）
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-002-04
- **関連企業:** Meta, Google, Amazon, InMobi
- **要約:** Meta/Google/AmazonはAI駆動広告プラットフォーム（自動入札・生成クリエイティブ）を直接提供し、従来の代理店モデルを脅かす。過去6か月でFacebook/Google広告のAIが大進展し、AI入札戦略がメディア購入を再形成。ゼロクリック化（検索→回答エンジン）で広告モデル自体の構造再編も進行。
- **キーファクト:**
  - InMobiがBuyer HubにAIエージェントを同梱し代理店に開放（7日前）
  - Razorpay Agent Studio: カート回復・リマインダー・紛争をエージェントが自律処理
  - URL→完成広告を$1.50/クリエイティブで生成（AdCreative.ai）——制作コストの桁違いの低下
- **引用URL:** https://www.linkedin.com/pulse/zero-click-shift-why-ai-generated-ads-failing-how-engine-kiran-voleti-fnzdf
- **Evidence ID:** EVD-20260907-0055

### INFO-056
- **タイトル:** OpenAI価格改定ラッシュ: 7/30にLuna -80%・Terra -20%削減、9/3にGPT-6 Astra $10/$50
- **ソース:** OpenAI公式changelog + CloudZero（2ソース）
- **公開日:** 2026-07-30〜09-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** OpenAIはGPT-5.6ファミリーGA（7/9、1.05Mコンテキスト）後の7月30日、Lunaを80%削減（$0.20/$1.20）しTerraを20%削減（$2/$12）——GPT-5ローンチ以来最大の価格変更で「フロンティアAIの価格戦争」の最明確なシグナル。9月3日には新フラッグシップGPT-6 Astraを$10/$50でリリース。ボリューム層で切り、プレステージ層（Sol $5/$30）は維持。
- **キーファクト:**
  - GPT-6 Astra (9/3): $10/$50・現行フラッグシップ
  - GPT-5.6 Luna $0.20/$1.20（GPT-5.4 Mini比4倍安）、Terra $2/$12（GPT-5.4 $2.50/$15下回る）
  - コスト削減はエンドツーエンド提供コスト20%低減の推論作業による資金調達（OpenAI説明）
  - キャッシュ入力10%・Batch API 50%・2026-03-05以降モデルに地域処理+10%
- **引用URL:** https://www.cloudzero.com/blog/openai-pricing/
- **Evidence ID:** EVD-20260907-0056

### INFO-057
- **タイトル:** Claude現行ラインナップ: Fable 5.1 $10/$50・Opus 5 $5/$25・Mythos Preview $25/$125
- **ソース:** Claude Platform公式ドキュメント + BenchLM（2ソース）
- **公開日:** 2026-09時点
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claudeの現行4層: Claude Fable 5.1（$10/$50・長時間エージェント向け最上位）> Claude Opus 5（$5/$25・複雑なエージェントコーディング）> Claude Sonnet 5（$2/$10は8/31まで、以降$3/$15）> Claude Haiku 4.5（$1/$5）。サイバーセキュリティ特化「Claude Mythos Preview」は$25/$125（4/7、Project Glasswing経由・限定アクセス）で同社史上最高額。
- **キーファクト:**
  - Fable 5.1 (9月): $10/$50・キャッシュ読み込み$0.25/M
  - Sonnet 5は8/31まで$2/$10の期間限定→$3/$15に戻る
  - Opus 4.1時代($15/$75)からOpus 5($5/$25)で67%値下げの歴史
  - US限定推論はClaude 4.6以降+10%追加
- **引用URL:** https://platform.claude.com/docs/en/models/overview
- **Evidence ID:** EVD-20260907-0057

### INFO-058
- **タイトル:** Opus 4.7の新トークナイザは同テキストで最大35%多くトークン消費——「影の値上げ」
- **ソース:** Metacto + Reddit r/ClaudeAI（2ソース）
- **公開日:** 2026-04-16以降
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claude Opus 4.7（2026-04-16）はトークン単価は$5/$25と据え置きだが、新トークナイザが同じテキストに対し最大35%多くのトークンを消費する可能性があり、実効価格を実質的に引き上げる構造。サブスクとAPIの価格乖離（$200サブスク vs $7,470相当のAPI利用の事例報告）も議論沸騰。
- **キーファクト:**
  - Opus 4.7新トークナイザ: 同一テキストで最大+35%トークン消費
  - Fast Mode: Opus 4.8は$10/$50と4.7比3倍安い
  - Claude Managed Agents (β): $0.08/セッション時間+標準トークン費
- **引用URL:** https://www.metacto.com/blogs/anthropic-api-pricing-a-full-breakdown-of-costs-and-integration
- **Evidence ID:** EVD-20260907-0058

### INFO-059
- **タイトル:** Google、Gemini 3.6-3.8 Flashのキャンペーン価格を2027年1月1日に倍額へ scheduled increase
- **ソース:** Google公式 Gemini Developer API料金ページ
- **公開日:** 2026-09時点の公示
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google
- **要約:** Gemini 3.8/3.7/3.6 Flashは2026年12月31日まで$0.75入力/$3.75出力（キャッシュ$0.075）のキャンペーン価格だが、2027年1月1日から倍額（$1.50/$7.50・キャッシュ$0.15）に移行するよう公示済み。先取りの価格戻しで「価格戦争」の持続可能性を疑う材料。無料枠は2026年4月1日からProモデルを除外しFlashのみに縮小済み。
- **キーファクト:**
  - Gemini 3.8/3.7/3.6 Flash: 2026年末まで$0.75/$3.75 → 2027年から$1.50/$7.50
  - Gemini 3.5 Flash (5/19 I/O): $1.50/$9・3.1 Proをコーディングで上回り25%安い
  - Gemini 3.1 Pro: $2/$12（≤200K）・$4/$18（>200K）・2Mコンテキスト
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Evidence ID:** EVD-20260907-0059

### INFO-060
- **タイトル:** LLM価格変動トレンド: Gemini 3.1 Pro出力$5→$12・Mistral Large 3 $6→$1.5
- **ソース:** BenchLM価格履歴
- **公開日:** 2026-09時点
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google, Mistral, OpenAI, Anthropic, xAI, Moonshot AI
- **要約:** 主要モデル価格の変動履歴で値下げ（OpenAI Luna/Terra、Mistral Large 3 $6→$1.5）と値上げ（Gemini 3.1 Pro出力$5→$12、Sonnet 5の期間限定$2→$3復帰、Gemini Flashの2027年倍額予定）が同時進行。最上位帯はGPT-5.4/5.5 Pro $30/$180、Claude Mythos $25/$125、Fable 5.1 $10/$50、GPT-6 Astra $10/$50、Grok 4.6 $2/$6（低価格戦略）。
- **キーファクト:**
  - 最高額帯: GPT-5.4/5.5 Pro $30/$180 > Claude Mythos $25/$125
  - フラッグシップ標準帯: Fable 5.1/GPT-6 Astra $10/$50、Opus 5/GPT-5.6 Sol $5/$25-30
  - Grok 4.6 $2/$6 は同性能帯で最安（GPT-5.6 Terra $2.50/$15相当と競合）
- **引用URL:** https://benchlm.ai/llm-pricing-trends
- **Evidence ID:** EVD-20260907-0060

### INFO-061
- **タイトル:** GPT-6 AstraがARC-AGI-3で99.9%——最新の抽象推論ベンチマークをほぼ完全解決
- **ソース:** LLM Stats ARC-AGI-3リーダーボード（9月更新）
- **公開日:** 2026-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI, Anthropic
- **要約:** ARC-AGI-3リーダーボード（2026年9月更新）で、9/3リリースのGPT-6 Astraが0.999を記録し新ベンチマークをほぼ完全解決。2位Claude Opus 5は0.302、GPT-5.6 Sol 0.078、Terra 0.008、Luna 0.002と桁違い。ARC-AGI-2ですら2026年4月時点でGPT-5.5が85%・平均30%未満だったことを踏まえると、Astraは「新規パターンの抽象推論」能力で単独ブレークスルーを達成。
- **キーファクト:**
  - ARC-AGI-3: GPT-6 Astra 0.999 / Opus 5 0.302 / Sol 0.078
  - 参考比較: GPT-4oはARC-AGI-1で約5%、Llama 4 MaverickはARC-AGI-2で0.00%
- **引用URL:** https://llm-stats.com/benchmarks/arc-agi-3
- **Evidence ID:** EVD-20260907-0061

### INFO-062
- **タイトル:** 9月総合ランキング: GPT-6 Astra 60.7でLLM Stats首位、AAII v4.2ではFable 5.1が57で首位
- **ソース:** LLM Stats + Artificial Analysis（2ソース）
- **公開日:** 2026-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Meta
- **要約:** LLM Stats総合でGPT-6 Astra（60.7、GPQA 96.0%）が首位、2位Claude Fable 5.1（56.8）、3位Claude Opus 5（55.4、コーディングArena首位）。一方Artificial Analysis Intelligence Index v4.2ではClaude Fable 5.1（Adaptive/Max Effort）が57で首位、GPT-6 Astra (max) 55が追う。評価軸により首位が分かれる接戦。Meta Muse Spark 1.3（55.3）がTOP5入り。
- **キーファクト:**
  - LLM Stats: GPT-6 Astra 60.7 > Fable 5.1 56.8 > Opus 5 55.4 > GPT-5.6 Sol 55.3 > Muse Spark 1.3 55.3
  - AAII v4.2: Fable 5.1 (57) > GPT-6 Astra (55) > Fable 5.1 xhigh (56)
  - Vellum GPQA: Sonnet 5が96.2%で首位、GPT-6 Astra 96%
- **引用URL:** https://llm-stats.com/
- **Evidence ID:** EVD-20260907-0062

### INFO-063
- **タイトル:** BenchLM 9月: プロバイダー上位3平均でAnthropic 81.5が首位、OpenAI 78、Google 72.9
- **ソース:** BenchLM
- **公開日:** 2026-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic, OpenAI, Google, Moonshot AI
- **要約:** BenchLM総合スコアでClaude Fable 5.1（82.95、Elo 1504）が首位、GPT-6 Astra（81.05、推定値）2位、Fable 5（80.9）3位、Opus 5（80.66）4位。Google最高位はGemini 3.8 Flash（78.41、6位）でPro系をFlashが上回る構図。オープン系最高位はKimi K3（74.87、7位）。Anthropicは上位3平均81.5でモデル数20社中最多の厚み。
- **キーファクト:**
  - Fable 5.1: Score 82.95・Elo 1504.21・66 tok/s・282s latency（遅い）
  - Gemini 3.8 Flash: 327 tok/s・10.75s・$0.75/$3.75と速度価格で圧倒
  - Grok 4.6: 70.19で18位（500K context）
- **引用URL:** https://benchlm.ai/
- **Evidence ID:** EVD-20260907-0063

### INFO-064
- **タイトル:** オープンウェイトがフロンティアに到達: Kimi K3がAAII総合3位、DeepSeek V4 Pro 80.6% SWE-bench
- **ソース:** Swfte分析 + LLM Stats（2ソース）
- **公開日:** 2026-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** Moonshot AI, DeepSeek, Alibaba, Zhipu AI, MiniMax
- **要約:** MoonshotのKimi K3（2.8T MoE）がArtificial Analysis Intelligence Indexで総合3位——Fable 5とGPT-5.6 Solを除く全専有モデルを上回り、Frontend Code Arenaで1位。DeepSeek V4 ProはSWE-bench Verified 80.6%でGemini 3.1 Proと同等、GLM-5.2はSWE-bench Pro 62.1%でGPT-5.5（58.6%）を上回る——MITライセンスでセルフホスト可能なモデルが米フラッグシップをエージェントコーディングで超えた。
- **キーファクト:**
  - Kimi K3: $3/$15・BrowseComp 91.2%（GPT-6 Astra 91.5%に僅差）・Terminal-Bench 88.3%
  - GLM-5.2はセルフホスト可能な最速フロンティア（168 t/s）
  - MiniMax M3 SWE-bench Verified 80.5%
- **引用URL:** https://www.swfte.com/ai/leaderboard
- **Evidence ID:** EVD-20260907-0064

### INFO-065
- **タイトル:** Meta、オープンフロンティア離脱: Llama 5は2027年予測、初のクローズドモデルMuse Sparkへピボット
- **ソース:** Swfte分析 + LLM Stats（Muse Spark 1.3がProprietary表記）
- **公開日:** 2026-09時点
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta
- **要約:** Llama 5は出荷されず2027年予測に後ろ倒し。Metaは2026年4月に初のクローズドフロンティアモデル「Muse Spark」をリリース（ウェイト・アーキテクチャ論文なし）。Muse Spark 1.1はScale LabsのSWE-Bench Pro Public（61.50）・MultiChallenge（75.52）・Finance/Legal Professional Reasoning・MCP Atlas（88.10）で首位級。中国ラボ（DeepSeek/Moonshot/Z.ai/Alibaba/MiniMax）がオープンウェイトフロンティアの実質的な担い手に。
- **キーファクト:**
  - Muse Spark 1.3: LLM Stats 5位・$0.10/M（低価格）だがProprietary
  - オープンモデルは「1TB VRAM級MoE（GLM-5.2、Kimi K3は64+アクセラレータ）」と「単GPU動作の小モデル（Qwen3.8 27B・Gemma 4・Nemotron 3 Nano）」に二極化
- **引用URL:** https://www.swfte.com/ai/leaderboard
- **Evidence ID:** EVD-20260907-0065

### INFO-066
- **タイトル:** Grok 4.5の経済性と代償: 4.2倍のトークン効率・$2.49/タスクだが幻覚率は倍増、EUではAI Actでブロック
- **ソース:** analystuttam Substack（Artificial Analysisデータ引用）
- **公開日:** 2026-08〜09
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02, KIQ-005-03
- **関連企業:** xAI
- **要約:** Grok 4.5は約80 tok/sで動作しSWE-bench ProタスクでClaude Opus 4.8比4.2倍少ない出力トークンを使用、同等タスク$2.49 vs Claude $11.80。数十万基のGB300とCursorの実際の開発者セッションデータで非同期RL学習。ただしArtificial Analysis計測で幻覚率が4.3→4.5で倍増（MoE設計に起因する較正トレードオフ）。さらにEU AI Actのシステミックリスク条項でEU内ブロック、コンテキストも1M→500Kに縮小。
- **キーファクト:**
  - 幻覚率: Grok-4-fast-reasoningはグラウンデッド要約で20.2%（GPT-5・Sonnet 4.5・Grok-4・Gemini-3-Proも10%超）
  - 「考える」モデルほど出典を超えた推論を加え、事実タスクで幻覚化するパターン
- **引用URL:** https://analystuttam.substack.com/p/claude-gpt-56-gemini-grok-and-chatllm
- **Evidence ID:** EVD-20260907-0066

### INFO-067
- **タイトル:** DeepSeekが価格の床へ: V4 Pro $0.435/$0.87（75%値下げ恒久化）、ピーク時間帯2倍料金を予告
- **ソース:** Swfte分析（公式価格追跡）
- **公開日:** 2026-05-31〜08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 Proは$1.74/$3.48でローンチ後、75%値下げプロモを2026年5月31日に恒久化し$0.435/$0.87に。V4 Flash（$0.14/$0.28、キャッシュヒット$0.0028）は利用可能な最安モデル。タスクあたり実測コストはV4 Pro約$0.04 vs Kimi K3 $0.94。$1でV4 Pro出力約115万トークン（GLM-5.2の22.7万、Kimi K3の6.7万）。ただし1日2回のピーク時間帯に2倍料金を予告（8/4時点で未発動）。
- **キーファクト:**
  - V4 Pro 0813版: LLM Stats 10位・52.5・$0.46でTOP10最安
  - 米Labの値下げ（OpenAI Luna -80%等）は中国オープン重量級への直接的な回答
- **引用URL:** https://www.swfte.com/ai/leaderboard
- **Evidence ID:** EVD-20260907-0067

### INFO-068
- **タイトル:** Claude Opus 5（7/24リリース）: thinkingデフォルトON、プロンプトキャッシュ最小512トークンに半減
- **ソース:** Swfte分析
- **公開日:** 2026-07-24
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic
- **要約:** Claude Opus 5は7月24日リリース。深い推論と長時間エージェント作業でOpus 4.8から一段の向上、価格は$5/$25据え置き（Fable 5の約半額）。thinkingがデフォルトでON、プロンプトキャッシュ最小トークン数が半減して512に。Vellum計測でBrowseComp 90.8%・GPQAでも上位。
- **キーファクト:**
  - OSWorld: Fable 5 85% > Opus 4.8 83.4% > Sonnet 5 81.2%
  - Terminal-Bench 2.1: GPT-5.6 Sol 88.8% > Kimi K3 88.3% > Mythos 5 88%
  - SWE-bench Verified: GPT-5.6 Sol 96.2% > Mythos 5 95.5% > Fable 5 95%
- **引用URL:** https://www.swfte.com/ai/models/anthropic-claude-opus-5
- **Evidence ID:** EVD-20260907-0068

### INFO-069
- **タイトル:** ベンチマーク飽和の現状: MMLU 92-94%・HumanEval 90%超は飽和、GPQA 94-96%に到達、HLEは46.5%が最高
- **ソース:** Value Add VC + Scale Labs + Vellum（3ソース）
- **公開日:** 2026-09時点
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** （業界全体）
- **要約:** MMLU（92-94%）とHumanEval（90%+）は飽和。SWE-bench Verified 88-95%はニア飽和。2026年のモデルカードはGPQA Diamond・SWE-bench Pro（最高69.2%）・ARC-AGI-2/3・HLE・AIME 2025に移行。HLE最高はFable 5.1 xhigh 46.50%とGemini 3.1 Pro thinking-high 46.44%（テキストのみ47.31%）。Remote Labor Index（経済的価値あるリモート作業）はFable-5 15.80%が最高で、実務自動化はまだ初期。
- **キーファクト:**
  - Arena: 680万票・360+モデル、上位5モデルが約55 Elo圏内の僅差
  - HiL-Bench（聞き返し能力）: Fable 5.1 61.50%が首位
  - DrugDiscoveryBench: GPT-5.5 mini-SWE-agent 51.60%が首位
- **引用URL:** https://valueaddvc.com/blog/ai-model-benchmarks-explained-mmlu-humaneval-lmsys-arena-and-what-they-actually-measure
- **Evidence ID:** EVD-20260907-0069

### INFO-070
- **タイトル:** Epoch AI: オープンウェイトはSOTA専有モデルから平均3ヶ月遅れに短縮、MMLU-Pro差3-5ポイント
- **ソース:** BentoML（Epoch AIデータ引用） + Sitepoint（2ソース）
- **公開日:** 2026年
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** （業界全体）
- **要約:** Epoch AI分析で、オープンウェイトモデルのSOTA専有モデルからの遅れは平均約3ヶ月に短縮。MMLU-Pro等では3-5ポイント差、標準的なコード生成・要約・構造抽出では実用上の差はほぼ消滅。残る差は複雑な多段推論（GPQA Diamondで専有首位がオープン勢に8-12ポイントリード）と低リソース言語。用途別ではコーディングエージェント・数学推論は「小」、極端な長コンテキスト+高信頼性は「中」の差。
- **キーファクト:**
  - 量子化進展とGPU単価低下で推論コスト40-60%低下
  - vLLM/TensorRT-LLM/Ollamaにセルフホスト環境が収斂
- **引用URL:** https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models
- **Evidence ID:** EVD-20260907-0070

### INFO-071
- **タイトル:** オープンソース主要モデル: DeepSeek-V4-Pro（MIT・1.6T/49B）SWE-bench 80.6%、Kimi K3ウェイトは7/27公開予定
- **ソース:** Onyx + MIT Technology Review（2ソース）
- **公開日:** 2026-04〜09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek, Moonshot AI, Tencent, Alibaba, Nvidia, Google, Zhipu AI
- **要約:** 2026年のオープン系主要モデル（ライセンス別）: DeepSeek-V4-Pro（MIT・1.6T/49B・SWE-bench 80.6%・GPQA 90.1%・LiveCodeBench 93.5%）、GLM-5.2（MIT・753B/40B・GPQA 91.2%・Arena Elo 1468）、DeepSeek-V4-Flash（MIT・284B/13B・SWE 79.0%）、Hunyuan Hy3（Apache 2.0・295B/21B）、Qwen3.6-27B（Apache 2.0・SWE 77.2%）、Nemotron 3 Ultra（OpenMDW・550B/55B）、Gemma 4 31B。MIT Tech Review（4/24）は「V4はR1同様、価格の何分の一かで最高性能に匹敵するオープンソースの新機軸」と評価。
- **キーファクト:**
  - Kimi K3: API先行公開（Arena Elo 1486）後、ウェットを7/27公開予定
  - 別計測（MindStudio）ではV4 Pro SWE-bench ~91.2% vs GPT-5.5 ~93.5% vs Opus 4.7 ~93.9%
  - GLM-4.7（THUDM）はClaudeの1/7コストでSWE-bench Verified 73.8%
- **引用URL:** https://onyx.app/insights/best-open-source-llms-2026
- **Evidence ID:** EVD-20260907-0071

### INFO-072
- **タイトル:** Meta: Llama 5は未発売（2027年予測）、年内はLlama 4.X、フロンティアはMuseブランドに移行
- **ソース:** Coursiv + Business Insider/Yahoo Finance（2ソース）
- **公開日:** 2026-08下旬時点
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta
- **要約:** 2026年8月下旬時点でMetaがLlama名義で公開した最新オープンウェイトはLlama 4ファミリーのまま。2026年のフロンティア開発は「Meta Superintelligence Labs」によるMuse Spark（4月、Museファミリー初号機、その後1.1アップデート）で展開。Business Insider報道ではLlama 4.X/4.5を年内投入予定。開発者向けにはMuse Codeがベータを卒業。INFO-065の「Metaオープン離脱」を複数ソースで裏付け。
- **キーファクト:**
  - Muse Sparkは「Muse family of models」の第一弾（今後シリーズ展開）
  - Llama 4.X系は従来型オープンウェイト継続の可能性
- **引用URL:** https://coursiv.io/blog/llama-5-release-date/
- **Evidence ID:** EVD-20260907-0072

### INFO-073
- **タイトル:** Mistral: Bedrockに18の管理対象オープンウェイトモデル（Large 3/Ministral 3含む）、フランス主権投資と結合
- **ソース:** AWS公式ブログ + Reddit/LocalLLaMA + NVIDIA AI Podcast（3ソース）
- **公開日:** 2026年
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral AI, Amazon
- **要約:** Amazon BedrockがMistral Large 3・Ministral 3を含む18のフルマネージドオープンウェイトモデルを追加。Mistralは7月に新オープンウェイトファミリーを発表。フランス政府系機関からの実質的資金提供と主権AI投資への統合が進み、EU域内AI主権の担い手としての位置を強化。NVIDIAポッドキャストでは「オープンウェイトが企業導入を加速する」とArthur Mensch路線を継続。
- **キーファクト:**
  - Mistral Large 3はカスタム商用ライセンス、Mixtral 8x22BはApache 2.0
  - 価格: Large 3 $0.50/$1.50（BenchLM 7月値下げ履歴あり）
- **引用URL:** https://aws.amazon.com/blogs/aws/amazon-bedrock-adds-fully-managed-open-weight-models/
- **Evidence ID:** EVD-20260907-0073

### INFO-074
- **タイトル:** 企業のOSS AI採用、データが割れる: 「89%の大企業が利用・ROI25%高」vs「ワークロードシェアは13%に頭打ち」
- **ソース:** MLflow + Typedef（Menlo Venturesレポート引用）（2ソース）
- **公開日:** 2025年後半〜2026年
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** （業界全体）
- **要約:** MLflowは「大組織の89%がオープンソースAIを利用し、クローズド源比ROIが25%高い。オープンソースが主推論経路になった比率は1年で23%→67%」と主張。一方Menlo Venturesのミッドイヤーレポートでは、企業AIワークロードに占めるオープンソースモデル比率は19%→13%に減少して頭打ち。「どこかで使っている」企業比率と「ワークロードに占めるシェア」の定義差で相反する数字が流通中。分析時は定義の確認が必須。
- **キーファクト:**
  - OSS AIモデル市場: 企業セグメントが68.9%を占めCAGR 15.1%（market.us）
  - 「主推論経路67%」と「ワークロード13%」の乖離は調査設計差と推定
- **引用URL:** https://mlflow.org/articles/the-role-of-open-source-in-enterprise-ai-in-2026/
- **Evidence ID:** EVD-20260907-0074

### INFO-075
- **タイトル:** AnthropicがSeries H $65B・$965B評価でOpenAI（$852B）を上回り最高評価AIスタートアップに
- **ソース:** CNBC + NYT（2ソース、公表値はCNBC優先）
- **公開日:** 2026-05-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04, KIQ-001-02
- **関連企業:** Anthropic, OpenAI
- **要約:** Anthropicは5月28日、Altimeter Capital・Dragoneer・Greenoaks・Sequoia CapitalがリードするSeries Hで$65Bを調達し、ポストマネー評価額$965Bに到達——初めてOpenAIを上回った。2月の$30Bラウンド（$380B評価）からわずか3ヶ月で約2.5倍。OpenAIは3月末に記録的な$122Bラウンドをクローズし$852B評価。NYTは$900B vs $730Bと別集計で報道（評価時点差）。Anthropicの評価額は2021年の$623Mから5年で約1,550倍。
- **キーファクト:**
  - Series H: $65B @ $965B（5/28）／Series G: $30B @ $380B（2月）
  - OpenAI: $122B調達・$852B評価（3月末クローズ）
- **引用URL:** https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html
- **Evidence ID:** EVD-20260907-0075

### INFO-076
- **タイトル:** Anthropic IPOは10月・評価額$2T超で史上最大級へ、2028年収益予測$190-200B・Amazon持分21%
- **ソース:** Financial Post/FT + GraniteShares（Reuters・Motley Fool引用）（3ソース）
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, Amazon, SpaceX
- **要約:** Anthropic投資家らは10月のIPOで$2T以上の評価額を期待。6月に$1.77T評価で上場したSpaceXを超える可能性があり、史上最大のIPOになる。$2T評価は2028年収益予測$190-200B（Reuters 8月報道）に基づく。Amazonは約21%持ち分（約$33B投資）を保有し、$400B超の価値になり得る。参謀: SpaceXが6月上場、Anthropic-OpenAIのIPO競争が「AI IPO race」として展開中。
- **キーファクト:**
  - IPO予定: 2026年10月・浮動評価 $2T+
  - SpaceX IPO: 2026年6月・$1.77T
  - Amazon持分: 約21%・約$33B投資
- **引用URL:** https://financialpost.com/financial-times/anthropic-investors-bet-valuation-ipo
- **Evidence ID:** EVD-20260907-0076

### INFO-077
- **タイトル:** M&A記録年: SpaceXがCursor買収$60Bを完了（8/14）、QualcommがModularを$4Bで買収へ
- **ソース:** Crunchbase + American Bazaar Online（2ソース）
- **公開日:** 2026-08-14〜09月上旬
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** SpaceX, Anysphere (Cursor), Qualcomm, Modular
- **要約:** SpaceXがAIコーディング企業Cursor（Anysphere）の$60B買収を8月14日に完了——米スタートアップM&A記録年を決定づける大型ディール。直後にはQualcommがAIチップスタートアップModularを$4Bで買収すると発表。2025年のAI M&A総額$155Bの約半分が特定プラットフォーム関連とされ、2026年は$512Bがdeployedと伝えられる（Forbes）。週次でもCrusoe・FluidstackなどマルチビリオンAIインフララウンドが続く（Crunchbase 9/4）。
- **キーファクト:**
  - SpaceX×Cursor: $60B・完了8/14
  - Qualcomm×Modular: $4B・9月上旬発表
  - Lyte: $165M調達・評価額$1.6B（9/3）
- **引用URL:** https://news.crunchbase.com/ma/2026-mergers-acquisitions-record-cursor-spcx/
- **Evidence ID:** EVD-20260907-0077

### INFO-078
- **タイトル:** AIインフラの巨大化: Goldman「ビッグ4でFY25-30に$5.3T」、McKinsey「2030年までに156GW・$5.2T」
- **ソース:** Goldman Sachs（Amanda Lynam） + McKinsey + AFCOM/S&P Global（3ソース）
- **公開日:** 2026年
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Microsoft, Alphabet, Amazon, Meta
- **要約:** Goldman SachsはMeta・Microsoft・Amazon・Alphabetの4社によるFY2025-2030の合計キャップエクスを$5.3T、ベースライン集計（2026-2031・計算機/DC/電力込み）で$7.6Tと予測。McKinseyは2030年までにAI向けデータセンターキャパシティ156GWが必要で、コンピュートのコストは$5.2T（$7Tレースの一部）と試算。2025年のAI起因DCディールは$61B（S&P Global・史上最高）。大型DCは単体で最大2GW規模に達し「ギガワット時代」が本格化。
- **キーファクト:**
  - 156GW@2030必要 vs 現在の電力網・許認可ボトルネック
  - 2025年AI DCディール $61B（前年比大幅増）
- **引用URL:** https://avidsolutionsinc.com/13-data-center-growth-projections-that-will-shape-2026-2030/
- **Evidence ID:** EVD-20260907-0078

### INFO-079
- **タイトル:** 2026年ハイパースケーラーcapex合計$700-760B: Amazon $200B・Microsoft $190B・Alphabet $175-185B・Meta $115-135B、FCF圧迫
- **ソース:** CNBC + Futurum + Statista（3ソース）
- **公開日:** 2026-02〜年中改定
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Amazon, Microsoft, Alphabet, Meta, Oracle
- **要約:** 2026年のビッグ4キャップエクスは当初ガイダンスで合計~$700B、その後Amazon・Alphabetが上方修正しStatista集計では$760Bに。FuturumはOracle $50B込みの5社で$660-690B・前年比ほぼ2倍と算定。BarclaysはMetaのFCFが約90%減少、Microsoft -28%（2027年に回復予想）、CitiはAmazonのFCFがマイナス転落と分析（Googleは回避）。AWSは年換算収益$142B・成長率24%加速（3年ぶり高）。AlphabetはGemini提供コストを2025年に78%削減と効率化を強調。
- **キーファクト:**
  - Amazon $200B（コンセンサス$147Bを大幅上回る）→ 発表で株価8-10%下落
  - Meta: オハイオ1GW DC・ルイジアナは最終的に5GWへ拡張可能
  - Microsoft: 直近四半期だけで$37.5B支出
- **引用URL:** https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html
- **Evidence ID:** EVD-20260907-0079

### INFO-080
- **タイトル:** 電力制約がボトルネック化: 「2026年予定AI DCの50%が送電未整備で開設不能」主張も
- **ソース:** Sightline Climate系動画（Facebook経由） + Deloitte 2025 AI Infrastructure Survey
- **公開日:** 2026年
- **信頼性コード:** D-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** （業界全体）
- **要約:** 米国で発表済みのAI計算キャパシティ数十GWが、送電網の許認可・相互接続待ちで電気的進捗ゼロとする分析が拡散（「2026年予定AI DCの50%が開設できない」）。SNS由来で一次ソース確認要だが、Deloitte調査も大型DCは単体2GW・電網拡張とサプライチェーンが課題と裏付け。ERCOT（テキサス）の大規模接続要求474GW（KIQ-INFRA-TX関連）とも整合する「ギガワット時代の電力制約」構図。
- **キーファクト:**
  - 主張: 数十GWのAIキャパシティが送電未整備
  - Deloitte: 最大級DCは2GW規模・グリッド容量が律速
- **引用URL:** https://www.deloitte.com/us/en/insights/industry/power-and-utilities/data-center-infrastructure-artificial-intelligence.html
- **Evidence ID:** EVD-20260907-0080

### INFO-081
- **タイトル:** 企業は同時に4ベンダー（Microsoft/Salesforce/ServiceNow/AWS）からスイッチングコストを蓄積、測定手法を持つ調達部門はほぼゼロ
- **ソース:** VaaSBlock研究
- **公開日:** 2026年
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** Microsoft, Salesforce, ServiceNow, Amazon
- **要約:** 2026年の企業ソフトウェア購入者はMicrosoft・Salesforce・ServiceNow・AWSの4社から同時にAIスイッチングコストを獲得しているが、蓄積を測定する方法論を持つ組織はほぼない。ServiceNowが最大（設定に数万エンジニア時間、AI機能がワークフローロジックと不可分）。Copilotは利用率3%でも知識労働者の60%に日常習慣として埋め込み、契約更新時（2027-28）の交渉力を規定する。データパイプライン・ワークフロー自動化・従業員習慣・組繊的知識という貸借対照表に載らない4経路で蓄積。
- **キーファクト:**
  - スイッチングコストは「副産物」であり項目立て計上されない
  - 1990s-2000sのOracle+SAP+Siebel+IBM多層ロックインの再演
- **引用URL:** https://www.vaasblock.com/research/enterprise-ai-vendor-lock-in-switching-costs-copilot-agentforce-2026/
- **Evidence ID:** EVD-20260907-0081

### INFO-082
- **タイトル:** Zapier調査: 米企業幹部の81%がAIベンダー依存に懸念、47%「主要ベンダー喪失で基幹機能が停止」
- **ソース:** Zapier調査（AvePoint・Kong引用）（3ソース）
- **公開日:** 2026年
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** （業界全体）
- **要約:** Zapier調査で米国企業幹部の81%が特定AIベンダーへの依存に少なくともある程度懸念、47%は主要AIベンダーの完全喪失でキービジネス機能が混乱すると回答。別集計では「AIベンダー喪失で4分の3の企業に支障」。2025年1月のChatGPT障害でOpenAI単独依存の企業はAI機能を維持する手段がなかった事例が単一障害点の教訓として引用され続ける。ガバナンス対応はベンダー非依存抽象レイヤー・データ形式のエクスポート要件・スイッチングコスト定期評価。
- **キーファクト:**
  - 81%懸念 / 47%基幹機能停止リスク / 「3/4企業に支障」
  - 抽象レイヤー+輸出可能データ形式+切替コスト定期評価が対策の三本柱
- **引用URL:** https://www.avepoint.com/blog/manage/ai-vendor-lock-in-multi-model-strategy
- **Evidence ID:** EVD-20260907-0082

### INFO-083
- **タイトル:** BCG「AIロックインは技術から認知へ」——学術研究は「価値創造機能に埋め込まれたロックイン>エグレス料金」を実証
- **ソース:** BCG 2026 + DiVA学術論文（Azure/AWS事例分析）（2ソース）
- **公開日:** 2026年
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** Microsoft, Amazon
- **要約:** BCGは2026年のAIロックインを「技術から認知へシフト」と定義——AI推論が企業の意思決定自体を形作ることで認知的ロックインが発生。Azure/AWSを分析した学術研究は6つのスイッチングコスト機構を特定し、最も深いロックインはエグレス料金等の制限的機構ではなく、ファインチューニング済みモデル・マネージドツールチェーン・統合開発環境など「価値創造そのもの」に構造的に埋め込まれていると結論。人材資本層（プラットフォーム固有のノウハー蓄積）は技術層のコストを実務上超え得る。
- **キーファクト:**
  - 価値創造メカニズム＝ロックインメカニズムの構造的不可分性
  - CMA（2025）はエグレス料金を「実在だが二次的」と評価
- **引用URL:** https://www.bcg.com/publications/2026/how-ceos-avoid-ai-vendor-lock-in-risk
- **Evidence ID:** EVD-20260907-0083

### INFO-084
- **タイトル:** OpenAIがAssistants APIを2026年にサンセット——Responses APIへの強制移行で開発者に移行負担、ロックインはモデル層からスタック層へ
- **ソース:** Developers Digest + Kai Waehner（2ソース）
- **公開日:** 2026年
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** OpenAI, Microsoft
- **要約:** OpenAIはAssistants APIを2026年中に廃止し、Responses APIへの移行を強制——ベンダー内でさえ非互換移行コストが発生する実例。Kai WaehnerのQ3 2026ランドスケープ分析では、ロックインの主戦場がモデル層からスタック層（オーケストレーション・エージェント基盤・統合）に移行したと指摘。Microsoft Azure OpenAI + Copilotが「市場で最も深い企業AIロックイン」。同分析は米輸出規制エピソードでフロンティアモデルアクセスが一時停止した事象もカバー。Morningstarは逆に「AIは企業ソフトウェアのスイッチングコスト持続期間を短縮」と分析（Technology One・Hansenの株価下落）。
- **キーファクト:**
  - Assistants API→Responses API移行: state/threads/toolsの再設計が必要
  - Morningstar: AI対応遅れERP2社が9月以降20-30%下落
- **引用URL:** https://www.developersdigest.tech/blog/openai-responses-api-migration
- **Evidence ID:** EVD-20260907-0084

### INFO-085
- **タイトル:** サイバーエージェント、入札・配信設定を24時間365日自動最適化する広告配信運用AIエージェント「効果おまかせAI」を4/20提供開始
- **ソース:** サイバーエージェント公式リリース + Web担（2ソース）
- **公開日:** 2026-04-20（発表4/7）
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** サイバーエージェント
- **要約:** サイバーエージェントはインターネット広告事業本部で、入札・配信設定の自動最適化に特化したAIエージェント「効果おまかせAI」を開発し2026年4月20日から提供開始。配信状況をリアルタイム分析し、入札・キャンペーン最適化・クリエイティブステータス変更・ターゲティング設計を独自AIアルゴリズムで自動実施。広告主は戦略立案など本質業務に注力。同社は「審査AI」など生成AI広告運用プロセス群も展開中。
- **キーファクト:**
  - 効果おまかせAI: 24時間365日自動最適化・改善施策の自動実施
  - 審査AI: 広告主指定ルールでクリエイティブ審査を自動化
- **引用URL:** https://www.cyberagent.co.jp/news/detail/id=33180
- **Evidence ID:** EVD-20260907-0085

### INFO-086
- **タイトル:** KPMG調査: エントリーレベル採用変更企業が18%→64%→87%と急加速、「適応力・継続学習83%＞プログラミング67%」
- **ソース:** KPMG AI Quarterly Pulse Survey（Q4 2025・Q1 2026・業種別）
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-01
- **関連企業:** （業界全体）
- **要約:** KPMG四半期パルス調査で、AIエージェントの影響でエントリーレベル採用方針を変更済みの組織は前季度18%→Q4 2025で64%→業種別調査では87%へ急加速。Q1 2026では新卒・初級人材に求めるスキルは「適応力と継続的学習」（83%）が「技術的プログラミング」（67%）を上回り、学習速度と判断力が差別化要因に。76%のビジネスリーダーは今後2-3年で従業員がAIエージェントを管理すると期待、56%が職務変更を予期。
- **キーファクト:**
  - 18%→64%（四半期で3.5倍）→87%
  - 求人再設計: データ・自動化・責任あるAIの新コンピテンシー
- **引用URL:** https://kpmg.com/us/en/media/news/q4-ai-pulse.html
- **Evidence ID:** EVD-20260907-0086

### INFO-087
- **タイトル:** 解雇の実態: 39%が2025年にAI関連レイオフ実施・58%が2026年に可能性、HBR「AIの実績でなくポテンシャルで解雇」
- **ソース:** HR Dive調査 + HBR + Stanford Digital Economy Lab（3ソース）
- **公開日:** 2025-11〜2026-01
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-01
- **関連企業:** （業界全体）
- **要約:** 米ビジネスリーダー1,000人調査: 半数が採用抑制、39%が2025年にレイオフ実施、35%が年内追加解雇予期、58%が2026年解雇を可能性と回答。高給・AIスキルなし・入社直後・エントリーレベルが最高リスク群。HBRは「企業はAIの実際の業績ではなくポテンシャルゆえに解雇している」と分析。Stanford「Canaries in the Coal Mine」はカスタマーサービスとプログラミング職で初期の雇用減を実証、Fortuneは「約束に反し昨年120万件削減」と報道。非検証系集計では2026年1月以降33万件が「AIのため」と主張される解雇（要確認）。
- **キーファクト:**
  - 39%実施 / 58%2026年可能性 / 2/3の企業がエントリーレベル採用減速
  - Amodei予測（参考）: 5年でエントリーレベル白書50%消滅・失業率10-20%
- **引用URL:** https://hbr.org/2026/01/companies-are-laying-off-workers-because-of-ais-potential-not-its-performance
- **Evidence ID:** EVD-20260907-0087

### INFO-088
- **タイトル:** Klarna: AIが月230万チャット・853人分の業務を処理も「AIのみ」戦略は手詰まり——人員の再採用へ後退
- **ソース:** Digital Applied + Reddit/Fast Company（3ソース）
- **公開日:** 2025-2026
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-01
- **関連企業:** Klarna
- **要約:** KlarnaのAIアシスタントは230万件のカスタマーサービスチャットを処理し700人分のフルタイム役割を代替、ヘッドカウント約48%削減と平均給与約60%上昇を達成したが、品質低下を受けてカスタマーサービス人員の再採用に転換。「AIのみ」ワークフォース戦略の限界が露呈した。現在AIは853人分（旧700人分から増加）の業務をこなすとされる。
- **キーファクト:**
  - 230万チャット/月・700人分→853人分相当
  - 削減後の再採用（バックペダル）が「AIファースト」戦略の教訓事例に
- **引用URL:** https://www.digitalapplied.com/blog/ai-first-layoff-trend-10-corporations-amazon-to-klarna
- **Evidence ID:** EVD-20260907-0088

### INFO-089
- **タイトル:** Duolingo「AIファースト」方針が逆風: 契約者代替・自動化優先のヘッドカウント原則が評判を毀損
- **ソース:** Fast Company + hirewithlumi + LinkedIn（3ソース）
- **公開日:** 2025-2026
- **信頼性コード:** C-3
 **関連KIQ:** KIQ-004-01
- **関連企業:** Duolingo
- **要約:** Duolingoは「自動化で代替できない場合にのみヘッドカウント増を認める」AIファースト方針を公言し契約者をAIで代替したが、Fast Companyは「AIファーストが KlarnaとDuolingoで裏目に出ている」と報道。社内外の反発と品質・評判リスクから方針を軟化。「従業員を置き換えるのではない」というメッセージへの転換を余儀なくされた。AI置換の初期事例2社（Klarna・Duolingo）がそろって部分撤退したことは、完全自動化シナリオへの強い反証データ。
- **キーファクト:**
  - 「自動化し尽くしてから増員」原則の公開→後退
  - KlarnaとDuolingoのセットで「AIファースト逆風」の代表事例に
- **引用URL:** https://hirewithlumi.com/blog/when-ai-first-backfires-lessons-from-klarna-and-duolingo/
- **Evidence ID:** EVD-20260907-0089

### INFO-090
- **タイトル:** JetBrains調査（2026年4月）: 84%の開発者が毎日AIコーディングツール使用、Claude Code職場導入18%・CSAT 91%
- **ソース:** JetBrains調査（Medium検証記事引用）
- **公開日:** 2026-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** JetBrains, Anysphere (Cursor), GitHub/Microsoft, Anthropic
- **要約:** JetBrains最新調査で84%の開発者が日常的にAIコーディングツールを使用。Claude Codeは認知57%・職場導入18%（米加24%）・CSAT 91%でカテゴリ最高NPSを獲得し急伸。Cursorは認知69%で首位だが成長は鈍化。GitHub Copilotは職場利用29%で特に大企業で優位（Fortune 100の90%が利用、累計ユーザー2,000万人超、有料ツール市場シェア約42%）。実測比較では3ツールとも3-5倍の機能提供速度とされる。
- **キーファクト:**
  - 84%毎日使用 / 97%が何らか使用（GitHub調査）
  - Copilot: アクティブユーザーのコードの46%がAI生成
  - ターミナルエージェント vs AI IDEの陣営争い（Karpathy投稿、Cursor Glass新UI）
- **引用URL:** https://ai.plainenglish.io/claude-code-vs-cursor-vs-github-copilot-in-april-2026-i-tested-all-three-on-production-systems-fed398b02a5e
- **Evidence ID:** EVD-20260907-0090

### INFO-091
- **タイトル:** Stanford研究: 22-25歳ソフトウェア開発者の雇用が2022年後半ピークから約20%減少
- **ソース:** Stanford Digital Economy Lab（Canaries in the Coal Mine） + Stack Overflow Blog
- **公開日:** 2025-08〜12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** Stanford Digital Economy LabのBrynjolfssonらによる「Canaries in the Coal Mine」研究で、22-25歳のソフトウェア開発者雇用は2025年7月時点で2022年後半のピークから約20%減少。エントリーレベル技術職採用は2024年に前年比25%減。ただしクラッシング的意見は「ソフトウェア職の消滅ではなくジュニア層のタスク圧縮」。「ジュニア開発者 listing」は5年前比で3分の1超減との集計も（要確認）。
- **キーファクト:**
  - 22-25歳開発者雇用: ピーク比-20%
  - エントリーレベル技術採用: 2024年-25% YoY
  - 若手の基礎スキル低下懸念（leaddev: CEOsがreckon with）
- **引用URL:** https://stackoverflow.blog/2025/12/26/ai-vs-gen-z/
- **Evidence ID:** EVD-20260907-0091

### INFO-092
- **タイトル:** 生産性エビデンスの混乱: METR「体感24%短縮・実測20%遅延」（2025）が2026年更新で「実測20%短縮」に反転
- **ソース:** METR + OSS開発者実測研究（Reddit r/programming集計）
- **公開日:** 2025〜2026
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** METR研究（2025）は経験豊富な開発者がAIで24%速くなったと感じるが実測では約20%遅いと報告し話題に。ところが2026年更新版では開発者はAIで約20%速いという逆の結果に。別のOSS経験者対象研究でも「AI使用時は19%長くかかる」との結果があり、エビデンスは完全には定まっていない。ツール・タスク・習熟の組み合わせに強く依存するため単一数値の引用は危険。
- **キーファクト:**
  - METR 2025: 体感-24% / 実測+20%時間 → 2026更新: 実測-20%時間
  - OSS研究: +19%時間（経験者）
- **引用URL:** https://www.reddit.com/r/programming/comments/1lwk6nj/measuring_the_impact_of_ai_on_experienced/
- **Evidence ID:** EVD-20260907-0092

### INFO-093
- **タイトル:** 生産性エビデンスの対立: Microsoft RCT「55.8%高速」vs UpLevel「約800人で有意差なし」vs McKinsey「16-30%向上」
- **ソース:** Microsoft Research + UpLevel + McKinsey（3ソース）
- **公開日:** 2023〜2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft, GitHub
- **要約:** MicrosoftのRCTではHTTPサーバー実装タスクでCopilot群が55.8%高速Completion。一方UpLevelは約800人の実エンジニアリングデータ（サイクルタイム・PRスループット・バグ率）でCopilotアクセスの有意な改善を検出せず。McKinseyは高绩效組織でチーム生産性16-30%・品質31-45%向上と報告。測定環境（統制実験vs実務メトリクス）によって結論が大きく分かれる「AI生産性パラドックス」の典型。
- **キーファクト:**
  - Microsoft RCT: +55.8%（単純タスク・新規実装）
  - UpLevel: 有意差なし（実務メトリクス）
  - McKinsey: +16-30%（自己報告込み高绩效組織）
- **引用URL:** https://uplevelteam.com/blog/ai-for-developer-productivity
- **Evidence ID:** EVD-20260907-0093

### INFO-094
- **タイトル:** 効果の非一様性: Copilotは新卒・ジュニアの完了率を上げるがシニアには無効、ANZ銀行は逆にPython専門家に最効
- **ソース:** SSRN研究（2024） + ANZ Bank内部研究 + GitHub研究（3ソース）
- **公開日:** 2024〜2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** GitHub, ANZ Bank
- **要約:** SSRN研究「Copilotは新規採用者・ジュニア職のタスク完了率を有意に上げるが、長期勤務・シニア職には効果なし」。一方ANZ銀行の内部研究ではCopilotは専門家級Pythonプログラマに最も有益で、GitHub研究は経験の浅い開発者ほど利益とするなど結果が割れる。いずれにせよ「誰が」「どんなコードで」効果を出すかの条件付き評価が必要。スキル要件は構文暗記から問題定義・システム統合・テストへシフト（Michigan Tech）。
- **キーファクト:**
  - ジュニア有利説（SSRN・GitHub）vs 専門家有利説（ANZ）の対立
  - 96%の開発者がテスト・ドキュメント生成等の単調作業のAI移管を期待（Microsoft 2024）
- **引用URL:** https://uplevelteam.com/blog/ai-for-developer-productivity
- **Evidence ID:** EVD-20260907-0094

### INFO-095
- **タイトル:** WEF: 2030年までに1.7億人創出・9,200万人消滅・39%のスキルセット変換、エントリーレベルはAI高暴露でスキル変化2倍
- **ソース:** WEF Future of Jobs Report 2025 + WEF「AIとエントリーレベル仕事の未来」2026
- **公開日:** 2025-01〜2026
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** WEF Future of Jobs 2025は2030年までに1.7億人の新規雇用創出・9,200万人の消失（純+7,800万）・既存スキルセットの39%が変換または陳腐化と予測。2026年のエントリーレベル特化報告書では、AI暴露が最も高い四分位のエントリーレベル職は非エントリーレベル職の約2倍のネットスキル変化率を示し、エントリーレベル労働者の28%が「3年後に自分のスキルの半分以下しか残っていない」と回答。教育システムの追従限界を指摘。
- **キーファクト:**
  - +170M / -92M / スキル39%変換（2030年）
  - AI高暴露エントリーレベル: スキル変化率約2倍
  - Reskilling Revolution: 次の10年で11億人の仕事が技術により転換
- **引用URL:** https://www.weforum.org/stories/artificial-intelligence/future-of-work-define-roles-humans-ai/
- **Evidence ID:** EVD-20260907-0095

### INFO-096
- **タイトル:** LinkedIn集計: AIは既に130万件の新規職を創出、CAIOはFortune 500の多数で一般職種化、「判断業務」の台頭
- **ソース:** WEF/LinkedIn Economic Graph + Mercor
- **公開日:** 2026-01〜05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** LinkedInデータに基づくWEF分析で、AI関連の新規職は既に130万件追加された。Chief AI Officerは多くのFortune 500企業で一般的な役職に。新興職種はAIエンジニア・MLエンジニア・AIプロダクトマネージャー・AI自動化スペシャリスト等の技術職に加え、AIガバナンス・戦略系の非技術職も成長。WEFは2026年5月「AI時代の判断業務（judgement work）の台頭」を特集——分析・生成・意思決定支援をAIが担う中、人間の価値は問題定義・制約設定・成果評価・最終決定に移ると定式化。
- **キーファクト:**
  - +130万AI新規職（LinkedIn既存集計）
  - 人間の残存価値: 問題定義・制約設定・評価・最終決定
- **引用URL:** https://www.weforum.org/stories/2026/01/ai-has-already-added-1-3-million-new-jobs-according-to-linkedin-data/
- **Evidence ID:** EVD-20260907-0096

### INFO-097
- **タイトル:** AIスキル賃金プレミアム56%——スタンフォードHAI/LinkedIn経済グラフ
- **ソース:** Stanford HAI / LinkedIn Economic Graph（aimagicx要約）
- **公開日:** 2026
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** AIスキルを持つ労働者はそうでない労働者より56%高い収入を得るという賃金プレミアム計測（Stanford HAI/LinkedIn）。対象はAIコンテンツパイプライン運用マーケター、AI予測分析ファイナンスアナリスト、AI採用HR、AIサプライチェーンOps、AI契約分析法務など「ドメイン×AI運用」職。AIリテラシーは生産性問題を超え、定着・報酬の retention 問題と位置づけられる。
- **キーファクト:**
  - AIスキル賃金プレミアム: +56%
  - 抽象的eラーニングでなく実践的・社会的・管理者主導のリスキリングが有効
- **引用URL:** https://www.aimagicx.com/blog/wef-ai-future-of-work-manager-guide-2026
- **Evidence ID:** EVD-20260907-0097

### INFO-098
- **タイトル:** アップスキル格差: 雇用主の72%が全従業員に会社負担アップスキルを提供せず、男女差（女性43% vs 男性51%が利用）
- **ソース:** DeVry年次報告 + McKinsey + HCL年次報告（3ソース）
- **公開日:** 2024-2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** HCLTech
- **要約:** DeVry調査: 雇用主の約9割がアップスキル給付を提供するが利用率は55%。72%の雇用主は全従業員ではなく選抜者（高绩效・キャリア軌道ベース）のみに提供。雇用主は自社労働者の32%をAI初心者と評価するが、自己評価では3%のみ——認識ギャップ。女性はAIスキルによるキャリア機会で男性比50%低い評価、アップスキル利用も43% vs 51%。HCLは従業員の約80%をコアスキル研修、GenAI研修11.6万人超。McKinsey: gen AI早期導入企業の3分の2が戦略的タレント開発アプローチ保有。
- **キーファクト:**
  - 提供企業9割・利用率55%・全社提供は28%
  - 雇用主評価32%初心者 vs 自己評価3%
- **引用URL:** https://www.devry.edu/content/dam/devry_edu/newsroom/2024-devry-ai-report.pdf
- **Evidence ID:** EVD-20260907-0098

### INFO-099
- **タイトル:** AI耐性職の類型: 対人相互作用・身体的複雑性・道徳的責任が3条件、看護・セラピー・熟練職・クリエイティブ
- **ソース:** Upwork（120+職種分析） + metaintro + Michigan Tech（3ソース）
- **公開日:** 2026
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** AI耐性（AI-proof）職の共通条件は(1)対人相互作用・信頼構築、(2)身体的複雑性・熟練技能、(3)道徳的責任・最終判断の3点。看護師・セラピスト・緊急対応・熟練トレード（ skilled trades）・クリエイティブ職が代表。スキル面では批判的思考・創造性・AIリテラシー・EQ（AI拡張チーム管理で「いつAIを信頼しいつ上書きするか」の判断）・倫理フレーム適用が不可欠要素に。基礎スキル弱いままAIツールに依存する労働者は「脆弱性（fragility）」を生むとの指摘。
- **キーファクト:**
  - 3条件: 対人・身体・道徳的責任
  - AI出力の解釈・誤り検出・文脈判断が新規中核スキル
- **引用URL:** https://www.upwork.com/resources/jobs-ai-wont-replace
- **Evidence ID:** EVD-20260907-0099

### INFO-100
- **タイトル:** サイバーエージェントFY2025営業利益176億円（前年比14.0%減）、2026年9月期Q2決算を公表
- **ソース:** サイバーエージェント新規投資家向け資料・IRライブラリ（公式）
- **公開日:** 2026（FY2025実績・FY2026 Q2）
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-04
- **関連企業:** サイバーエージェント
- **要約:** サイバーエージェントのFY2025通期営業利益は176億円で前年比14.0%減。2026年9月期第2四半期（中間期）決算短信・決算説明会資料を公表済み。AI Labはデジタルマーケティング全般のAI研究開発組織として継続。「効果おまかせAI」（INFO-085）等の広告運用AIエージェント展開中だが、広告市場環境と投資負担が利益を圧迫している構図。AI収益化の進捗は決算資料本文での確認が必要。
- **キーファクト:**
  - FY2025営業利益: 176億円（-14.0% YoY）
  - AI Lab: マーケティングAI研究開発の中核組織
- **引用URL:** https://www.cyberagent.co.jp/files/topics/20015_ext_21_0.pdf
- **Evidence ID:** EVD-20260907-0100

### INFO-101
- **タイトル:** WEFダボス「32のAI事例」: 病院AIエージェントで400 Staff Hours超節減・$1.4M増収、PwC「AI変革で利益率40-60%向上余地」
- **ソース:** WEF（CIO.com経由） + PwC Strategy&（2ソース）
- **公開日:** 2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-04
- **関連企業:** Fujitsu
- **要約:** WEFが実ビジネスインパクトを持つ32のAI事例を提示。その中でGenshukai & Fujitsu（日本）の病院経営AIエージェントは400スタッフ時間超を節減し$140万の増収。PwC Strategy&は徹底したAI変革戦略で利益率40-60%向上を投影。国内事例集では¥5億の追加利益を創出したAI導入も紹介。AI収益化の実例は「業務時間節減+増収」の複合効果として現れ始めている。
- **キーファクト:**
  - 病院AI: 400+時間節減・$1.4M増収
  - PwC: 利益率+40-60%（徹底変革シナリオ）
- **引用URL:** https://www.cio.com/article/4122937/davos-from-hype-to-ai-transformation-in-the-economy.html
- **Evidence ID:** EVD-20260907-0101

### INFO-102
- **タイトル:** 広告業界2026: 4As「人間の判断・文化的洞察・ストーリーテリングが新たなIP」、GenAIはマーケティング価値の5-15%解放、市場は$35B→$82B
- **ソース:** 4As Look Ahead 2026 + eMarketer + LinkedIn/industry（3ソース）
- **公開日:** 2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-04
- **関連企業:** （広告業界）
- **要約:** 米4As（American Association of Advertising Agencies）は2026年展望で、AIが執行を commodity 化する中、人間の判断力・文化的洞察・ストーリーテリングを「新たなIP」と位置づけ、報酬モデルを稼動時間・実行から戦略的インパクト・創造IP・アドバイザリー価値への成果報酬型転換を提言。生成AIはマーケティング総価値の5-15%を効率化・効果化で解放すると試算。主要ホールディングカンパニーはAI開発に大幅な資本投入を約束。AIマーケティング市場は2026年$35.05B→2030年$82.2B予測。eMarketerはAI破壊と統合（consolidation）が業界の並行トレンドと分析。
- **キーファクト:**
  - GenAI: マーケティング価値の5-15%解放
  - AIマーケティング市場: $35.05B（2026）→$82.2B（2030）
  - ビジネスアプリの40%にエンタープライズAIエージェント組込み予測（2026年末）
- **引用URL:** https://www.aaaa.org/look-ahead/partner-agency/
- **Evidence ID:** EVD-20260907-0102

### INFO-103
- **タイトル:** データ堀の条件: 専有データでカスタマイズしたAIはビジネスタスク性能35-50%向上（McKinsey）、相互作用データが観察データに勝る
- **ソース:** McKinsey（LinkedIn引用） + IBM + Acceldata/SaaS Mag（3ソース）
- **公開日:** 2024-2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-04
- **関連企業:** IBM
- **要約:** McKinsey 2024研究: 専有データでAIモデルをカスタマイズした企業はビジネスタスクで35-50%の性能向上。データ堀の本質は「データ量」でなく「そのデータがAIシステムをどれだけ速く改善するか」であり、観察ではなく相互作用（インタラクション）を通じたデータ生成が真の優位性を作る。NRRデータではACV $100K超のエンタープライズSaaS中央値118% vs SMB 97%と、データフライホイールを持つ企業が継続率・評価額プレミアムを獲得。IBMはRAG・ファインチューニングによる企業コンテキスト接地を「総合AIの唯一無二の差別化源」と強調。
- **キーファクト:**
  - 専有データ活用: 性能+35-50%（McKinsey）
  - NRR: エンタープライズ118% / ミドル108% / SMB 97%
  - 注意点: AI機能投資は推論コストを吸収し続ける
- **引用URL:** https://www.ibm.com/think/insights/proprietary-data-gen-ai-competitive-edge
- **Evidence ID:** EVD-20260907-0103

### INFO-104
- **タイトル:** MIT Tech Review: 「AIの再帰的自己改善は想的ほど速く来ない」、Anthropic公式「When AI Builds Itself」——RSIは未達・不可避でもない
- **ソース:** MIT Technology Review + Anthropic Institute公式（2ソース）
- **公開日:** 2026-06〜08-18
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Anthropic
- **要約:** Anthropicは6月にブログ「When AI Builds Itself」を公開し、モデルが自身の開発を加速する進捗を報告するとともに「我々はまだそこに至っておらず、再帰的自己改善（RSI）は不可避でもない」と明言。8月18日付MIT Tech Reviewは「AIのRSIは想的ほど速く来ないかもしれない」と分析。LLMは既にコード記述・合成データ生成・チップ最適化を行うが、爆発的進歩予測（AI-2027等）に対して実測の進捗は漸進的。学術レビュー（arXiv 2607.07663）は「有界な自己精練（bounded self-refinement）は既に産業実務」「開放的RSIはグラウンディング要件・崩壊ダイナミクス・計算制約で依然有界」と分類。
- **キーファクト:**
  - Anthropic: RSI未達・不可避でない（公式見解）
  - bounded self-refinement＝実用化済み／open-ended RSI＝未達の二分法
- **引用URL:** https://www.anthropic.com/institute/recursive-self-improvement
- **Evidence ID:** EVD-20260907-0104

### INFO-105
- **タイトル:** METRフロンティアリスク報告（2-3月）: 非公開モデルは公開最先端を有意に上回らず——「隠された超強力モデル」の公算低い
- **ソース:** METR Frontier Risk Report
- **公開日:** 2026-05-19
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** （業界全体）
- **要約:** METRが参加企業から共有された内部展開モデルを評価した結果、「共有されたモデルのいずれも2026年5月19日時点で公開文書化された最強モデルより有意に高い能力を示さなかった」。また非参加企業の内部モデルが公開最先端を大幅に上回るとの信頼に足る公開報告も存在しない。監視項目はAI R&D・長期計画・継続学習・推論スケーリング・実環境自律運用での「大型または驚異的能力ジャンプ」。
- **キーファクト:**
  - 非公開モデル優位の証拠なし（2026年5月時点）
  - 監視: AI R&D・長期計画・継続学習・自律運用の能力ジャンプ
- **引用URL:** https://metr.org/blog/2026-05-19-frontier-risk-report/
- **Evidence ID:** EVD-20260907-0105

### INFO-106
- **タイトル:** 英AISI: 4月にClaude Mythos PreviewとGPT-5.5が「観測史上最大級のサイバー能力ジャンプ」、NCSCが国際警告
- **ソース:** UK AISI公式ブログ + NCSC（2ソース）
- **公開日:** 2026-04〜
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01, KIQ-005-03
- **関連企業:** Anthropic, OpenAI
- **要約:** 英AI Safety Instituteは「2026年4月、クローズド2モデル——Claude Mythos PreviewとGPT-5.5——がテスト開始以来最大級のAIサイバー能力ジャンプを示し、急速に変容するサイバーリスクへの対処を促す国際警告を引き起こした」と公表。Mythos（Anthropicのサイバーセキュリティ特化モデル、$25/$125）の能力が攻撃側にも転用可能な水準に達した可能性を示唆。オープンウェイトのサイバー能力のフロンティアとの差もAISIが測定中。KIQ-SEC-001（ゼロデイ特定）の背後にある能力基盤を裏付ける。
- **キーファクト:**
  - 対象: Claude Mythos Preview・GPT-5.5（4月、クローズドモデル）
  - NCSC「The AI Shift in Cyber Risk: Why Leaders Must Act Now」発出
- **引用URL:** https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
- **Evidence ID:** EVD-20260907-0106

### INFO-107
- **タイトル:** 職務代替エビデンスはまだ弱い: Google調査「AI利用は広く自動化証拠は僅少」、MIT Sloan「人間集約タスクは2016-24に増加」
- **ソース:** Google調査 + MIT Sloan（EPOCH指数） + McKinsey + Stanford調査（4ソース）
- **公開日:** 2025-2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-004-01
- **関連企業:** Google
- **要約:** Googleの研究はAI利用の広がりに対し実際の職務自動化の証拠は少ないと報告。MIT Sloan研究（EPOCH指数・代替リスク・増強潜在力の3指標）は、機械だけでは有効に出来ない人間集約的タスクが多く、2016-2024年にその量と頻度が増加したと結論。McKinseyは米国の労働時間の約57%が技術的には自動化可能だが大半の職は消滅でなく変化と予測。Stanford調査では46.1%のタスクが自動化肯定的評価を受けつつ、労働者は「自動化」より「H3対等パートナーシップ」を希望。
- **キーファクト:**
  - McKinsey: 労働時間57%が技術的自動化可能
  - EPOCH: 人間集約タスクは2016-24に増加傾向
- **引用URL:** https://mitsloan.mit.edu/press/new-mit-sloan-research-suggests-ai-more-likely-to-complement-not-replace-human-workers
- **Evidence ID:** EVD-20260907-0107

### INFO-108
- **タイトル:** 自律科学研究: AI Scientistシステム（Sakana/Kosmos等）は初期段階、Nobel Turing Challenge（2050年ノーベル賞）は未達
- **ソース:** arXiv（From AGI to ASI） + Nature（Kitano） + HPCwire/Academy（3ソース）
- **公開日:** 2024-2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** （業界全体）
- **要約:** 「AI Scientist」（Lu et al. 2024）やKosmos（Novikov et al. 2025）等の全自動科学発見システムは、LLMが独立に科学発見を推進する潜在力を示すが、人間の関与を減らした自律的再帰改善は「間もなく可能かもしれない」段階にとどまる。KitanoのNobel Turing Challenge（2050年までにAI科学者がノーベル賞受賞級発見）は2026年時点で未達。Demis Hassabis（ノーベル受賞者）とYann LeCun（チューリング受賞者）の対談では科学の未来に対する見解が明確に分かれる。AGI→ASI移行の技術経路は5つの瓶頸とともに整理されつつある。
- **キーファクト:**
  - AI Scientist系: デモ段階・実用発見はまだ限定
  - Bodenの創造性レベル1-2（探索的・組合せ的）にとどまる既存達成
- **引用URL:** https://arxiv.org/html/2606.12683v1
- **Evidence ID:** EVD-20260907-0108

### INFO-109
- **タイトル:** ダボス2026 CEO対決: Hassabis「AGIには程遠いが5-10年」vs Amodei「1年で全開発者の業務代替・2年でノーベル級研究・5年でホワイトカラー50%消滅」
- **ソース:** Fortune（ダボス現地報道） + Business Insider（2ソース）
- **公開日:** 2026-01-20〜23
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google DeepMind, Anthropic, OpenAI
- **要約:** WEFダボス2026「The Day After AGI」セッションでHassabisは「今日のAIは印象的だがAGIにはnowhere near。ただし5-10年内に到達、10年内50%の確率（現行アーキテクチャそのものではない）」と発言。Amodeiは「1年以内に全ソフトウェア開発者の業務を代替」「2年以内に複数分野でノーベル級科学研究」「5年でホワイトカラー職50%消滅」を主張。Altman（欠席）は「人間級AGIを通り越し超知能へ滑り込みつつある」との従来見解。3者の見解が最大限に乖離した場面。
- **キーファクト:**
  - Amodei: 1年=開発者代替 / 2年=ノーベル級 / 5年=白書50%
  - Hassabis: AGI 5-10年・10年内50%・現行LLM直接ではない
- **引用URL:** https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/
- **Evidence ID:** EVD-20260907-0109

### INFO-110
- **タイトル:** Hassabis最新見解: 「AGIは2030年前後・2029もあり得る」、2026年は「エージェントの時代」——「AGIまで4分の3到達」
- **ソース:** Techmeme経由 + YouTubeインタビュー（2ソース）
- **公開日:** 2026年後半（約5ヶ月前）
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google DeepMind
- **要約:** Hassabisは2026年半ばのインタビューで「AGIまで4分の3の道程にいる」と述べ、最新見解では「2030年前後を広く期待しつつ2029年の可能性も視野」に。2026年を「エージェントの時代」と位置づけつつ、その誇張に一定の距離を置く発言も。jagged intelligence（金メダル級数学と12歳でも解ける問題への失敗の同居）を引き続き警告し、協調の困難を主要懸念に挙げる。
- **キーファクト:**
  - AGI: ~2030（2029の可能性）
  - 「AGIまで4分の3」発言（2026年5月頃）
- **引用URL:** https://www.facebook.com/Techmeme/posts/1429654482530195/
- **Evidence ID:** EVD-20260907-0110

### INFO-111
- **タイトル:** Metaculus予測の圧縮: 2020年「50年先」→2026年2月「2029年25%・2033年50%」、学術シフト派は2030年28%
- **ソース:** Metaculus（veracalloway集計） + AIMultiple（10,000予測分析）
- **公開日:** 2026-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** （業界全体）
- **要約:** Metaculusコミュニティ中央値は2020年にAGIを約50年先と予測していたが、2026年2月には「2029年までに25%・2033年までに50%」へ圧縮——実質10年以上の前倒し。AI進展と深く接した学術グループは2026年1月に2030年28%へ更新。数千人規模の専門家調査では超知能到達を2040-2061に置く合意も残存し、業界-学術間の乖離が構造化。FPI調査ではAGI後超知能への移行は「2年（10%）〜30年（75%）」。
- **キーファクト:**
  - Metaculus: 25%@2029 / 50%@2033（2026年2月）
  - 専門家調査群: 超知能2040-2061（業界側は2026-2028と大幅に前倒し）
- **引用URL:** https://www.veracalloway.com/blog/ai-culture/agi-timeline/
- **Evidence ID:** EVD-20260907-0111

### INFO-112
- **タイトル:** LeCun「LLMはAGIに至らない、human-level AIは数年〜10年先」、Hinton「数十年内の人類絶滅10-20%」
- **ソース:** LeCun発言（X・YouTube・capacityglobal） + Hinton（veracalloway引用）（3ソース）
- **公開日:** 2024-2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Meta
- **要約:** Yann LeCunは「AGI」という概念自体が誤解を招くとし、LLMは真の推論・計画ができないためAGI経路ではないと主張。human-level AIは「数年、遅くとも10年」先で、5-10年後に正しい経路かどうかが判明すると説明。Altmanの「数千日」発言とは対照的。一方Geoffrey Hintonは「AIが数十年以内に人類を絶滅させる確率10-20%」を割り当て、能力曲線の近さを重く見積もる。Yampolskiyの「2030年までに99.9%絶滅」は周縁的意見として扱われる。
- **キーファクト:**
  - LeCun: LLM≠AGI経路・数年-10年先・5-10年で経路判明
  - Hinton: 絶滅確率10-20%（数十年内）
- **引用URL:** https://capacityglobal.com/news/yann-lecun-agi-overhyped-gates-nvidia-pullout/
- **Evidence ID:** EVD-20260907-0112

### INFO-113
- **タイトル:** AI 2027シナリオ: 超人コーダー2027年3月→超人AI研究者2027年9-11月→ASI 2027年12月、AGI定義の合意不存在
- **ソース:** AI 2027（Kokotajlo） + IEEE Spectrum + arXiv Levels of AGI（3ソース）
- **公開日:** 2025-2026
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02, KIQ-005-03
- **関連企業:** （業界全体）
- **要約:** 元OpenAI研究員Kokotajloらの「AI 2027」シナリオは、OpenBrain社が2027年3月に超人コーダー、9月にAgent-4（超人AI研究者）、12月にASIに到達する急進展を描く（racing ending）。影響は産業革命超と予測。一方、AGIの定義は「ベンチマーク」「内部動作」「経済的インパクト」「雰囲気」で判断が分かれ合意不存在（IEEE Spectrum）。Google DeepMindのLevels of AGI（レベル0-5框架）が運用化の試み。定義不在のため各社の「AGI達成」宣言の相互比較は不可能。
- **キーファクト:**
  - AI 2027: SC 3月→SIAR 11月→ASI 12月（シナリオ値）
  - 定義: ベンチマーク/内部/経済/vibesの4分類で分裂
- **引用URL:** https://ai-2027.com/
- **Evidence ID:** EVD-20260907-0113

### INFO-114
- **タイトル:** 州AI法モラトリアムは上院で圧倒的否決も「死んでいない」——連邦先取提案が再上程へ、業界主導と批判
- **ソース:** The Hill + GWU Regulatory Studies + CAP（3ソース）
- **公開日:** 2025-2026
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** （米政策）
- **要約:** 予算調整法案（BBB）に組み込まれた州AI法の10年間モラトリアム条項は上院で圧倒的多数の反対で否決。ただしCruz議員らは連邦先取（preemption）法案として再提案を準備中で「モラトリアムは死んでいない」。批判側は同条項が業界主導（商業会議所支持）で、現存する唯一のガードレールである州・地方保護を無効化すると主張。修正版テキストは$500M追加枠を超え$42.5B BEADプログラム全体に執行を拡大する曖昧な文言だったと分析。州AI立法は2026年も継続進行中。
- **キーファクト:**
  - 上院否決: 圧倒的多数 / 再提案の動き継続
  - 私的当事者による執行訴訟を許す設計が規制麻痺を招くリスク
- **引用URL:** https://thehill.com/opinion/congress-blog/technology/5413757-state-ai-legislation-threat/
- **Evidence ID:** EVD-20260907-0114

### INFO-115
- **タイトル:** 英AISI「Alignment Project」第1回で£27M超を60+プロジェクトに授与、OpenAIが$7.5M（£5.6M）追加共同出資
- **ソース:** OpenAI公式 + AISI公式 + CIFAR（3ソース）
- **公開日:** 2025-08〜2026
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** OpenAI, Microsoft, Amazon, Anthropic, Google DeepMind
- **要約:** 英AI Security Instituteが創設した国際的アライメント研究基金「The Alignment Project」は第1回ラウンドで£27M超を60以上のプロジェクト（1件£50K-£1M）に授与。OpenAIは$7.5M（約£5.6M）を追加出資し、審査既通過プロジェクトの追加支援とする。資金は計算複雑性理論・経済学・ゲーム理論・認知科学・情報理論/暗号理論など学際領域に分散。連合は英AISI・カナダCAISI/CIFAR（$1M）・豪州DISR・OpenAI・Microsoft・AWS（£5Mクラウドクレジット）・Schmidt Sciences・Anthropic・UKRI・ARIA等。2026年の同種プログラム開催は見込み薄。
- **キーファクト:**
  - £27M+ / 60+プロジェクト / 1件£50K-£1M
  - OpenAI: $7.5M（政策への影響なしの建前を明記）
- **引用URL:** https://openai.com/index/advancing-independent-research-ai-alignment/
- **Evidence ID:** EVD-20260907-0115

### INFO-116
- **タイトル:** 国際AI安全性報告書2026年版が2月に発行、豪・加がAI安全性協力MoU締結（3/5）、英米AISI共通テスト構築継続
- **ソース:** International AI Safety Report 2026 + SafeAI-Aus + Science|Business（3ソース）
- **公開日:** 2026-02〜03-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** （各国政府）
- **要約:** Bengio主導の「International AI Safety Report」第2版が2026年2月に発行され、汎用AIの能力・リスク・管理策の科学的総括を更新。2026年3月5日にはオーストラリアとカナダがAI安全性協力MoUを締結し、国際ネットワーク経由の二国間協力を強化。英米のAI Safety Instituteは先進AIシステムの安全性テスト共通アプローチ構築と能力共有で協働継続。UNIDIRは「AI・安全保障・倫理2026」国際会議を開催し、国際平和・安全保障への含意を審議。BrookingsはAIの戦時行動規範に関する世界的条約交渉の開始を提言。
- **キーファクト:**
  - International AI Safety Report 2026: 2月発行（第2版）
  - 豪-加MoU: 3/5・AI安全性協力
- **引用URL:** https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- **Evidence ID:** EVD-20260907-0116

### INFO-117
- **タイトル:** 安全性研究資金の多層化: DARPA-NSF「AI Forge」、Schmidt×DeepMindマルチエージェント安全性$1M、OpenAI Foundation $25B、Astralis年間$25M
- **ソース:** AISafety.com資金データベース（55基金） + DARPA/NSF + Schmidt Sciences
- **公開日:** 2026
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** Google DeepMind, OpenAI, DARPA, NSF
- **要約:** AI安全性資金は55以上の基金・プログラムに多層化。政府系ではDARPA-NSF共同「AI Forge」（解釈可能性・制御・敵対的頑健性、国家安全応用）、英ARIA「Mathematics for Safe AI」。産業系ではSchmidt SciencesがGoogle DeepMind・ARIA・CAIFと共同でマルチエージェント安全性研究に最大$1M（大規模AIエージェントネットワークの安全性）。OpenAI Foundationは各種助成に$25Bコミット、Astralis Foundationは年間$25M、Frontier Model ForumのAI Safety Fund等。.pause擁護のNonlinear助成金など主義色の強い資金も并存。
- **キーファクト:**
  - 55+資金源・rolling採択多数
  - マルチエージェント安全性: 新たな優先領域（Schmidt×DeepMind）
- **引用URL:** https://aisafety.com/funding
- **Evidence ID:** EVD-20260907-0117

### INFO-118
- **タイトル:** 豆包DAUが1億人を突破（字节史上最少の宣伝費で達成）、QuestMobile 2026Q1: 豆包MAU 3.4億・千問1.7億・DeepSeek 1.3億
- **ソース:** 36氪独家 + 财联社 + QuestMobile（3ソース・中国語）
- **公開日:** 2025-12-24〜2026-Q1
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-05
- **関連企業:** ByteDance, Alibaba, DeepSeek
- **要約:** 豆包（Doubao）AppのDAUが1億人を突破——ByteDance史上、億級DAU到達製品の中で宣伝・獲得費用が最少。生図・生動画・P図機能が留存を牽引。春節（除夕）当日のAIインタラクション総数は19億回。QuestMobile 2026年Q1で中国AIアプリMAUは 豆包3.4億＞千問1.7億＞DeepSeek 1.3億。千問は初日注文1,000万件超・DAU単日+5,100万でApp Store首位を一時獲得し「Chatbot入口争い」が新段階に。
- **キーファクト:**
  - 豆包: DAU 1億超・MAU 3.4億（2026Q1）
  - 春節除夕: AIインタラクション19億回
  - 7.1億AI月活全体の算力コスト負担が業界課題化（鈦媒体）
- **引用URL:** https://www.tmtpost.com/8030988.html
- **Evidence ID:** EVD-20260907-0118

### INFO-119
- **タイトル:** ByteDance Seed2.1が6/23正式リリース（Agent & Coding全面強化）、Seed2.0 ProはSuperGPQA・FrontierSciでGPT-5.2上回る
- **ソース:** ByteDance Seed公式（2ソース）
- **公開日:** 2026-06-23（Seed2.1）／Seed2.0は先行
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-02
- **関連企業:** ByteDance
- **要約:** Seed2.1は「AI生産力の深掘り」を掲げ、汎用Agent能力の信頼性向上・ツール/環境横断のタスク交付・複雑シーンでの安定提供を強化。Seed2.0シリーズ（Pro/Lite/Mini）は BabyVision等の視覚認識でSOTA、数学視覚推論（MathVista/MathVision等）でSOTA、SuperGPQAでGPT-5.2超、FrontierSci一部シナリオでGPT-5.2超、AInstein Bench（仮説駆動型科学発見）で首位。LMSYS Chatbot Arenaでも大規模展開モデルとして高評価。
- **キーファクト:**
  - Seed2.1: 汎用Agent・Coding・複雑シーン安定性
  - Seed2.0 Pro: SuperGPQA＞GPT-5.2・AInstein Bench首位
- **引用URL:** https://seed.bytedance.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity
- **Evidence ID:** EVD-20260907-0119

### INFO-120
- **タイトル:** ByteDance 8/24組織統合: TRAE・扣子（Coze）チームを豆包体系へ統合、独立AIオフィス製品「豆包工作」を週内リリース
- **ソース:** 百度百科（8/24報道収録） + coze.cn公式
- **公開日:** 2026-08-24
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-06
- **関連企業:** ByteDance
- **要約:** ByteDanceはオフィスAI製品の組織統合を実施: TRAE Work・扣子（Coze）は豆包と仕事シーンの機能を統合、TRAE IDE・CLIは豆包ブランド下のコーディング製品線として継続。同時にAIオフィス向け統一製品「豆包工作」を週内にも独立リリース（8月末）。Coze（扣子）は「職場AIパートナー+ワンストップAI開発プラットフォーム（扣子编程）」へ再定位され、PC・スマホ操作と結果直接交付を売りに。豆包は5月に「豆包支付」も開始し、スーパーアプリ化を加速。
- **キーファクト:**
  - TRAE Work/Coze→豆包統合、TRAE IDE/CLIは豆包コーディング線
  - 豆包工作: 8月末独立リリース・オフィスシーン統一ブランド
- **引用URL:** https://baike.baidu.com/item/豆包/63344333
- **Evidence ID:** EVD-20260907-0120

### INFO-121
- **タイトル:** Seedance 2.0/2.5: 統合マルチモーダル音声-動画共同生成アーキテクチャ、1分未満でネイティブ音声付き2K動画、2.5は「一鏡成片」
- **ソース:** ByteDance Seed公式 + Atlas Cloud + 中国語Wikipedia（3ソース・中国語）
- **公開日:** 2026
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** Seedance 2.0はテキスト・画像・音声・動画の4モダリティ入力を支持する統合マルチモーダル音動画共同生成アーキテクチャで、業界最全面のマルチモーダル参照・編集機能を統合。10秒1080p動画を30-60秒で生成、ネイティブ音声付き2K動画を1分未満で生成。豆包Appに全面接入され無料利用可能。後継のSeedance 2.5は「一鏡成片（ワンテイク）・随心参考（自在な参照指定）」で生成後の編集・リズム制御精度を向上。日本のFable等、動画生成競争の中国側主力。
- **キーファクト:**
  - 4モダリティ入力・音声-動画共同生成
  - 2K動画1分未満・豆包に無料全面接入
- **引用URL:** https://seed.bytedance.com/zh/seedance2_0
- **Evidence ID:** EVD-20260907-0121

### INFO-122
- **タイトル:** ByteDanceの算力投資: 2024年800億元（BAT合計に匹敵）→2025年1,600億元→2026年は1,600〜2,000億元・半分をAIチップに
- **ソース:** 华尔街见闻 + 财联社（浙商証券） + 萝卜投研（3ソース・中国語）
- **公開日:** 2025-2026
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** 浙商証券: ByteDanceの2024年資本支出は約800億元で百度・阿裏・騰訊合計（約1,000億元）に接近。2025年は1,600億元計画（900億元がAI算力調達、700億元がIDC・光モジュール・スイッチ等）。2026年は1,600億元で半分をAIチップに投入し海外DC拡張（华尔街见聞）、その後メモリチップ価格高騰等を背景にAIインフラ支出を25%増の2,000億元へ引き上げとの報道（萝卜投研）。中国最大のAI利用プラットフォームとして算力需要が供給を上回る「字節算力承圧」状態。
- **キーファクト:**
  - 2024: ¥800億 / 2025: ¥1,600億 / 2026: ¥1,600-2,000億
  - 2026年算力産業チェーンは「全鏈条インフレ」段階
- **引用URL:** https://wallstreetcn.com/articles/3761890
- **Evidence ID:** EVD-20260907-0122
