# 収集データ: 2026-05-17

## メタデータ
- 収集日時: 2026-05-17 00:30 UTC
- 実行クエリ数: 61 / 56+動的5
- scrape実行数: 12件
- 収集情報数: 65件
- Evidence ID 採番範囲: EVD-20260517-0001 〜 EVD-20260517-0065
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 動的追加クエリ: Claude Code定量ユーザー検証, xAI定量データ, 書く能力価値低下反証, 過剰投資バブル検証, エンタープライス生産化率定量
- 品質フラグ: NORMAL

## 収集結果

### INFO-001
- **タイトル:** Building a new enterprise AI services company with Blackstone, Hellman & Friedman, and Goldman Sachs
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** AnthropicがBlackstone、Hellman & Friedman、Goldman Sachsと共に新たなエンタープライズAIサービス会社を設立。中堅企業向けにClaudeを展開し、AnthropicのApplied AIエンジニアが顧客と密接に協力してカスタムソリューションを構築。General Atlantic、Leonard Green、Apollo、GIC、Sequoia Capitalも出資。
- **キーファクト:**
  - Blackstone/H&F/Goldman Sachsとの合弁エンタープライズAIサービス会社設立
  - 中堅企業（地域医療、コミュニティバンク、製造業等）をターゲット
  - Claude Partner Networkへの新会社の参画（Accenture/Deloitte/PwCと並ぶ）
- **引用URL:** https://www.anthropic.com/news/enterprise-ai-services-company
- **Evidence ID:** EVD-20260517-0001

### INFO-002
- **タイトル:** Introducing Claude Sonnet 4.6
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 4.6はコーディング、コンピュータ使用、長文脈推論、エージェント計画、ナレッジワーク、デザインの全面アップグレード。1Mトークンコンテキストウィンドウ（ベータ）。SWE-bench Verified 80.2%。価格はSonnet 4.5と同一（$3/$15 per M tokens）。Claude Code内で70%のユーザーがSonnet 4.5よりSonnet 4.6を好む。
- **キーファクト:**
  - SWE-bench Verified: 80.2%（Opus 4.5の59%のユーザーがSonnet 4.6を好む）
  - OSWorld benchmarkで16ヶ月連続改善
  - 1M token context window（ベータ）
  - Databricks/Replit/Cursor/GitHub/Cognition等の推薦コメント
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6
- **Evidence ID:** EVD-20260517-0002

### INFO-003
- **タイトル:** Introducing Claude for Small Business
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude for Small Businessを発表。QuickBooks、PayPal、HubSpot、Canva、Docusign、Google Workspace、Microsoft 365と統合し、15のagentic workflows + 15スキルを提供。米国小企業GDPの44%を占める層をターゲット。PayPalとのAI Fluency無料コース、全米10都市SMBツアーを実施。
- **キーファクト:**
  - 15のagentic workflows + 15スキル（給与計画、月次決算、キャンペーン等）
  - QuickBooks/PayPal/HubSpot/Canva/Docusign統合
  - CDFI（Accion Opportunity Fund/CRF USA/Pacific Community Ventures）とのパートナーシップ
  - SMB Tour: Chicago/Tulsa/Dallas等10都市
- **引用URL:** https://www.anthropic.com/news/claude-for-small-business
- **Evidence ID:** EVD-20260517-0003

### INFO-004
- **タイトル:** Grok 3 Beta — The Age of Reasoning Agents
- **ソース:** xAI公式ブログ
- **公開日:** 2025-02-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01
- **関連企業:** xAI
- **要約:** xAIがGrok 3ベータ版を発表。Colossusスーパークラスタで10倍のコンピュートで訓練。AIME 2025で93.3%、GPQA 84.6%、LiveCodeBench 79.4%。1Mトークンコンテキストウィンドウ。DeepSearchエージェント機能。Grok 3 APIの近日公開予定。
- **キーファクト:**
  - AIME 2025: 93.3% (cons@64), GPQA: 84.6%, LCB: 79.4%
  - Chatbot Arena Elo: 1402
  - 1M token context window
  - DeepSearch（AIエージェント）ロールアウト
- **引用URL:** https://x.ai/blog/grok-3
- **Evidence ID:** EVD-20260517-0004

### INFO-005
- **タイトル:** OpenAI Agents SDKにネイティブサンドボックス実行サポートが追加
- **ソース:** Modal Blog
- **公開日:** 2026-05-01
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIが2026年4月にAgents SDKにネイティブサンドボックス実行を追加。7つの公式統合ホスト型サンドボックスプロバイダー（Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel）が利用可能。ModalのみGPUアクセラレーション対応。
- **キーファクト:**
  - 7つの公式サンドボックスプロバイダー統合
  - Docker/Unix-localサンドボックスクライアント内蔵
  - ModalのみMLワークロード向けGPUアクセラレーション対応
- **引用URL:** https://modal.com/resources/best-sandbox-openai-agents-sdk
- **Evidence ID:** EVD-20260517-0005

### INFO-006
- **タイトル:** Pulumi: エージェント開発の中間層が崩壊
- **ソース:** Pulumi Blog
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI, Anthropic
- **要約:** LangChain/LlamaIndex + RAGパイプライン + 手書きエージェントループの中間層が陳腐化。SDKに組み込みツールが統合され、「スキル」システムがツールレジストリに取って代わり、長いコンテキストウィンドウがベクター検索をデフォルトアーキテクチャから排除。OpenAI Agents SDKは明示的エージェントハンドオフを、Claude Agent SDK/Codex SDKがミドルウェアの大部分を代替。
- **キーファクト:**
  - LangChain/LlamaIndex等のミドルウェア層の陳腐化
  - Skillsシステムがツールレジストリを代替
  - 2024-2025年のプロジェクトの50%以上を占めたミドルウェアが不要に
- **引用URL:** https://www.pulumi.com/blog/how-building-ai-agents-has-changed/
- **Evidence ID:** EVD-20260517-0006

### INFO-007
- **タイトル:** Google Gemini Live Agent Challenge winners announced
- **ソース:** Google Cloud Blog
- **公開日:** 2026-05-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Google
- **要約:** GoogleのGemini Live Agent Challengeが11,878参加者・1,536プロジェクト・151カ国から参加。Gemini Live API、Agent Development Kit（ADK）、Google Cloudを用いたマルチモーダルリアルタイムエージェントを3カテゴリで構築。Google Cloud Next 2026で受賞者を発表。
- **キーファクト:**
  - 11,878参加者・1,536プロジェクト・151カ国
  - Gemini Live API + ADK + Google Cloud活用
  - 3カテゴリ: Live Agent / Creative Storyteller / UI Navigator
- **引用URL:** https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-of-the-gemini-live-agent-challenge
- **Evidence ID:** EVD-20260517-0007

### INFO-008
- **タイトル:** OpenAI Cookbook: Agent Improvement Flywheel with Traces, Evals, and Codex
- **ソース:** OpenAI Developer Cookbook
- **公開日:** 2026-05-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI公式チュートリアル。Agents SDKベースの金融アナリストエージェントの自己改善ループを紹介。リアルトレースの取得→人間/モデルフィードバック→評価への変換→Codexによるエージェント改善提案のサイクルを示す「評価駆動エージェント開発」パラダイム。
- **キーファクト:**
  - Traces → Feedback → Evals → Codex改善ループ
  - 自己改善型エージェント開発パラダイムの公式ガイド
  - 金融アナリストエージェントを実例として使用
- **引用URL:** https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop
- **Evidence ID:** EVD-20260517-0008

### INFO-009
- **タイトル:** Google Gemini Interactions API + Deep Research Agent
- **ソース:** Google AI for Developers
- **公開日:** 2026-05-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google
- **要約:** GoogleがGemini Interactions APIをリリース。エージェントワークフロー、サーバーサイド状態管理、複雑なマルチモーダル・マルチターン会話に最適化された次世代API。Deep Research Agentは自律的に計画・実行・統合するマルチステップリサーチ機能。Gemini Enterprise Agent Platformの一部。
- **キーファクト:**
  - Gemini Interactions API: エージェントワークフロー最適化
  - サーバーサイド状態管理
  - Deep Research Agent: 自律的マルチステップリサーチ
- **引用URL:** https://ai.google.dev/gemini-api/docs/interactions/deep-research
- **Evidence ID:** EVD-20260517-0009

### INFO-010
- **タイトル:** ByteDance Coze 2.5 launches "Agent World" ecosystem
- **ソース:** KuCoin News / ME News
- **公開日:** 2026-04-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのエージェントプラットフォームCozeがバージョン2.5を発表。「Agent World」エコシステムを導入し、AIエージェントがチャットインターフェースを超えて独立した実行環境・スキル・アイデンティティで動作可能に。クラウドデバイス・個人ワークスペース・Kozi CLI等を提供。
- **キーファクト:**
  - Coze 2.5: Agent Worldエコシステム
  - 「フル装備デバイス」: クラウドコンピュータ/クラウドフォン
  - 「フルスキル」: 動画作成/プログラミング(Kozi CLI)/業界特化スキル
  - 「フルパーソナリティ」: 長期記憶/デジタルソーシャルID
- **引用URL:** https://www.kucoin.com/news/flash/bytedance-s-coze-launches-version-2-5-introduces-agent-world-ecosystem
- **Evidence ID:** EVD-20260517-0010

### INFO-011
- **タイトル:** Qubika SRE Triage Agent: インシデントから根本原因まで自動化
- **ソース:** Qubika Blog
- **公開日:** 2026-05-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** QubikaのSREトリアージエージェントがAnthropic Claude Code上に構築。インシデントトリアージを20-30分から1分未満に短縮。APM/CI-CD/インフラMCPサーバーを通じてコンテキストを自動収集し、構造化されたMarkdownレポートを生成。
- **キーファクト:**
  - トリアージ時間を20-30分から1分未満に短縮
  - Anthropic Claude Code上に構築
  - MCPサーバー経由でアラート/ログ/デプロイ/インフラを自動相関
- **引用URL:** https://qubika.com/blog/sre-triage-agent-incident-root-cause-automatically/
- **Evidence ID:** EVD-20260517-0011

### INFO-012
- **タイトル:** Endor Labs launches Agent Governance and Package Firewall for AI Coding Agents
- **ソース:** Endor Labs Blog
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-002-03
- **関連企業:** Google, Cursor, Anthropic
- **要約:** Endor LabsがAIコーディングエージェント向けのセキュリティ製品「Agent Governance」「Package Firewall」をCursor/Googleと協力して発表。npm マルウェアアドバイザリが14倍増加、2025年に92%のnpmメンテナーアカウント乗っ取りが発生。Bitwarden CLIサプライチェーン攻撃がClaude Code/Codex/GeminiのCLIを標的に。
- **キーファクト:**
  - Agent Governance: エージェント/モデル/ツール/スキルの4層監視
  - Package Firewall: 悪意あるパッケージをリアルタイムでブロック
  - npmマルウェア14倍増加、2025年92%のアカウント乗っ取りが発生
  - Bitwarden CLI攻撃がClaude Code/Codex/Gemini CLIを標的
- **引用URL:** https://www.endorlabs.com/learn/introducing-security-for-ai-coding-agents-and-workstations
- **Evidence ID:** EVD-20260517-0012

### INFO-013
- **タイトル:** EY builds enterprise-scale agentic AI operating system
- **ソース:** EY Sweden
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Microsoft, Google
- **要約:** EYがMicrosoft + NVIDIAと共同でエンタープライズ規模のエージェントAIオペレーティングシステムを構築。9ヶ月で50,000以上のエージェントを開発。EY.ai EYQが300,000人以上のプロフェッショナルに展開。80%以上のEYプロフェッショナルがAI使用、80%以上が基礎AIトレーニング完了。
- **キーファクト:**
  - 9ヶ月で50,000以上のエージェントを開発
  - 300,000人以上にEY.ai EYQ展開
  - 80%以上のEYプロフェッショナルがAI使用
  - Microsoft Azure/NVIDIAとの共同エンジニアリング
- **引用URL:** https://www.ey.com/en_se/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system
- **Evidence ID:** EVD-20260517-0013

### INFO-014
- **タイトル:** Boomi and Guru Partner to Deliver AI-Powered Enterprise Knowledge with MCP Registry Integration
- **ソース:** BusinessWire
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Boomi, Guru
- **要約:** BoomiとGuruがAI駆動のエンタープライズナレッジ統合パートナーシップを発表。GuruがBoomi Connectのローンチパートナーとなり、MCP Registryを通じてエンタープライズデータをリアルタイム活性化する。
- **キーファクト:**
  - Boomi ConnectのMCP Registryを通じた統合
  - エンタープライズデータの断片化解消を目的
  - AIエージェントによるリアルタイムデータ活性化
- **引用URL:** https://www.businesswire.com/news/home/20260514440755/en/Boomi-and-Guru-Partner-to-Deliver-AI-Powered-Enterprise-Knowledge-Enriched-by-Real-Time-Data-Activation
- **Evidence ID:** EVD-20260517-0014

### INFO-015
- **タイトル:** Experian and ServiceNow Announce Agentic AI Partnership
- **ソース:** X/MarketsDay
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Experian, ServiceNow
- **要約:** ExperianとServiceNowが複数年協業を発表。Experian AscendをServiceNowワークフローに統合し、規制産業向けにエージェントAIを拡張。
- **キーファクト:**
  - 複数年グローバルAI提携
  - Experian AscendをServiceNowワークフローに統合
  - 規制産業向けエージェントAIスケーリング
- **引用URL:** https://x.com/marketsday/status/2055268042888868241
- **Evidence ID:** EVD-20260517-0015

### INFO-016
- **タイトル:** GPT-5.5 Multimodal Intelligence and Spatial Reasoning Evaluation
- **ソース:** OpenAI Cookbook / ibl.ai
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** OpenAI
- **要約:** GPT-5.5がテキスト・画像・音声をネイティブに処理するマルチモーダル知能を提供。空間推論評価では、より多くの空間計画作業を一般マルチモーダル推論に移行可能であることが示された。
- **キーファクト:**
  - GPT-5.5はテキスト・画像・音声のネイティブ処理
  - 空間推論能力の向上
  - エージェントによる文書・図表分析が可能
- **引用URL:** https://developers.openai.com/cookbook/examples/multimodal/grounded_spatial_reasoning_layouts
- **Evidence ID:** EVD-20260517-0016

### INFO-017
- **タイトル:** Winners of the Gemini Live Agent Challenge - Multimodal Real-Time Agent Integration
- **ソース:** Google Cloud Blog
- **公開日:** 2026-05-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** GoogleがGemini Live Agent Challengeの受賞者を発表。マルチモーダル capabilities（視覚・聴覚・発話・リアルタイム生成）をシームレスに統合するエージェントの構築がミッション。Gemini APIを使用。
- **キーファクト:**
  - リアルタイムマルチモーダルエージェントの構築コンペ
  - 視覚・聴覚・発話の統合が要件
  - Gemini APIを活用したエージェント開発
- **引用URL:** https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-of-the-gemini-live-agent-challenge
- **Evidence ID:** EVD-20260517-0017

### INFO-018
- **タイトル:** Gemini 3 Pro Deep Think Leads Multimodal Benchmarks, Grok 4.1 Close Second
- **ソース:** BenchLM.ai
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google, xAI
- **要約:** 2026年5月時点のマルチモーダルベンチマークで、Gemini 3 Pro Deep Thinkが加重スコア100.0%で首位、Grok 4.1が97.8%で続く。SWE-bench MultimodalではClaude Mythos Previewが59%で首位。
- **キーファクト:**
  - マルチモーダル部門: Gemini 3 Pro Deep Think 100.0%、Grok 4.1 97.8%
  - SWE-bench Multimodal: Claude Mythos Preview 59%で首位
  - 2026年5月時点の最新マルチモーダルランキング
- **引用URL:** https://benchlm.ai/multimodal-grounded
- **Evidence ID:** EVD-20260517-0018

### INFO-019
- **タイトル:** Google Gemini Omni Leaked, Gemini Robotics for Physical World AI
- **ソース:** X/TheAgentTimes, 9to5Google
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** Googleの統合マルチモーダルモデル「Gemini Omni」がリーク。同時にGemini RoboticsがGemini 2.0ベースで物理世界へのAI導入を目指す。OpenAIはSora 2をシャットダウンしコンピュートをロボティクスに振り向けている。
- **キーファクト:**
  - Gemini Omni: 統合マルチモーダルモデルがリーク
  - Gemini Robotics: Gemini 2.0ベースの物理世界AI
  - OpenAIはSora 2をシャットダウン、ロボティクスにリソース移行
- **引用URL:** https://x.com/TheAgentTimes/status/2054032664509001758
- **Evidence ID:** EVD-20260517-0019

### INFO-020
- **タイトル:** Agentic AI Lock-In Isn't About Contracts — It's Workflow Entanglement
- **ソース:** MYGOM
- **公開日:** 2026-05-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** (一般)
- **要約:** エージェントAIの真のロックインは契約ではなく、他社フレームワーク内にトラップされたワークフローにある。DataRobotもエージェントAIの隠れたコストを指摘し、モデルレベルのロックインが現在の採用期の隠れたリスクであると警告。
- **キーファクト:**
  - エージェントAIロックインの真因はワークフローのフレームワーク依存
  - モデルレベルロックインは価格引き上げや機能変更時のリスク
  - DataRobotがエージェントAIの予算超過コストを指摘
- **引用URL:** https://mygom.tech/articles/agentic-ai-lock-in-isnt-about-contracts
- **Evidence ID:** EVD-20260517-0020

### INFO-021
- **タイトル:** Amazon Bedrock AgentCore Runtime with Managed Payment Capabilities
- **ソース:** AWS Blog
- **公開日:** 2026-05-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** Amazon Bedrock AgentCoreがマネージド決済機能をプレビュー。AIエージェントが自律的にアクセス・決済可能に。Agent Toolkit for AWSがMCPサーバー・プラグイン・スキルの後継として登場。
- **キーファクト:**
  - Bedrock AgentCore: エージェント自律決済機能を初のマネージドサービスとしてプレビュー
  - Agent Toolkit for AWSがMCPサーバー等の後継
  - エージェントのセキュアなパブリック/プライベートリソース接続
- **引用URL:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/
- **Evidence ID:** EVD-20260517-0021

### INFO-022
- **タイトル:** Microsoft Agent 365 — Enterprise AI Agent Control Plane
- **ソース:** Valorem Reply / ITNext
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Agent 365がエンタープライズAIエージェントの制御プレーンとして登場。Entra Agent ID、Purview DSPM、Defenderによる保護機能を統合。SAP JouleとMicrosoft 365 Copilotの統合も発表。
- **キーファクト:**
  - Agent 365: エンタープライズAIエージェントの制御プレーン
  - Entra Agent ID / Purview DSPM / Defender統合
  - SAP環境での365 CopilotとJouleの連携
- **引用URL:** https://www.valoremreply.com/resources/insights/blog/azure/what-is-microsoft-agent-365-the-control-plane-for-enterprise-ai-agents-explained/
- **Evidence ID:** EVD-20260517-0022

### INFO-023
- **タイトル:** Google Vertex AI Agent Builder — Enterprise AI Agent Platform
- **ソース:** MajorMatters / Google Cloud
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Google
- **要約:** Google Vertex AI Agent Builderがエンタープライズ向けAIエージェント構築・デプロイ・ガバナンスプラットフォーム。Gemini統合、Vertex AI Search RAG、BigQuery MLを活用した本番級エージェント開発を支援。
- **キーファクト:**
  - エンタープライズ規模のエージェント構築・デプロイ・ガバナンス
  - Gemini / Vertex AI Search RAG / BigQuery ML統合
  - Google Cloudフルスタックを背景にしたプラットフォーム
- **引用URL:** https://majormatters.co/reviews/google-vertex-ai-agent-platform-review
- **Evidence ID:** EVD-20260517-0023

### INFO-024
- **タイトル:** Fortune 500 AI Deployment: Only 5% See Results, 70% of Banks Use Agentic AI
- **ソース:** LinkedIn / Financial Content
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (一般)
- **要約:** Fortune 500全体（評価額$46兆）のうちAI投資で成果を見ているのはわずか5%。一方、金融機関の70%がすでにエージェントAIを本番展開またはパイロット中。67%の企業がAIエージェントによる不正アクセスを疑っている。
- **キーファクト:**
  - Fortune 500のうちAI投資で成果が見られるのは5%のみ
  - 銀行の70%がエージェントAIを本番/パイロット展開
  - 67%の企業がAIエージェントによる不正データアクセスを疑う
- **引用URL:** https://www.prnewswire.com/news-releases/two-thirds-of-enterprises-suspect-ai-agents-have-already-accessed-unauthorized-data-akeyless-finds-302769768.html
- **Evidence ID:** EVD-20260517-0024

### INFO-025
- **タイトル:** US AI Regulation: 1200 AI Bills, Trump Executive Orders, and State-Federal Conflict
- **ソース:** Fortune / NPR / VerifyWise
- **公開日:** 2026-05-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** (一般)
- **要約:** 米国で1200以上のAI法案が提出される中、連邦政府と州政府の規制矛盾が激化。Trump政権は2025年1月にBiden時代のAI大統領令を取り消し、2025年12月の新令で州AI法への挑戦を指示。
- **キーファクト:**
  - 米国で1200以上のAI法案が提出、連邦・州間の規制矛盾激化
  - Trump政権: Biden令取消(2025年1月) → 新令で州法への挑戦(2025年12月)
  - 連邦政府の単一権限への集中が進行
- **引用URL:** https://fortune.com/2026/05/15/ai-policy-patchwork-state-federal-regulation-framework-sonnenfeld-marcus/
- **Evidence ID:** EVD-20260517-0025

### INFO-026
- **タイトル:** China Issues Blueprint for AI Agents with Security Bottom Line
- **ソース:** ChinaTradeMonitor / CNBC / AISpectrumIndia
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (中国企業一般)
- **要約:** 中国がAIエージェントの国家戦略を発表。安全で管理可能な原則に基づき、標準化された発展を推進。5省庁がAI擬人化インタラクションサービス向け規制を発表。米中間でAI安全性プロトコル設立の対話も進行。
- **キーファクト:**
  - 中国: AIエージェント国家戦略で安全・管理可能性を強調
  - 5省庁がAI擬人化サービス規制を発表
  - 米中AI安全性プロトコル設立対話が進行
- **引用URL:** https://www.chinatrademonitor.com/china-issues-new-blueprint-for-ai-agents/
- **Evidence ID:** EVD-20260517-0026

### INFO-027
- **タイトル:** Pentagon Contracts Seven AI Firms, Anthropic Refuses $200M Deal
- **ソース:** Jones Walker / AI CERTs / AICerts
- **公開日:** 2026-05-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google, xAI, SpaceX, Microsoft, Amazon, Nvidia
- **要約:** 国防省がSpaceX、OpenAI、Google、Nvidia、Reflection、Microsoft、AWSの7社と契約。一方でAnthropicは$200MのPentagon契約を拒否し、自律兵器・大量監視への利用を理由に「サプライチェーンリスク」指定を受けた。
- **キーファクト:**
  - Pentagon: 7社(SpaceX/OpenAI/Google/Nvidia/Reflection/MSFT/AWS)と機密AI契約
  - Anthropic: $200M契約拒否、大量監視・自律兵器への利用不可を理由
  - Anthropicは「サプライチェーンリスク」として指定
- **引用URL:** https://www.joneswalker.com/en/insights/blogs/ai-law-blog/one-government-two-voices-recent-anthropic-vs-pentagon-developments-add-to-the.html?id=102msco
- **Evidence ID:** EVD-20260517-0027

### INFO-028
- **タイトル:** Google DeepMind Workers Vote to Unionize Over Military AI Deals
- **ソース:** Reddit/UpliftingNews
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Google
- **要約:** Google DeepMind従業員がPentagon AI契約への懸念から労働組合設立に投票。Googleが国家安全保障契約に「より傾いている」との内部認識に対する抗議。機密軍事作戦へのAI技術利用が争点。
- **キーファクト:**
  - DeepMind従業員が軍事AI契約への懸念で労組設立に投票
  - Googleが国防契約に「より傾いている」との内部認識
  - 機密軍事作戦へのAI技術利用が争点
- **引用URL:** https://www.reddit.com/r/UpliftingNews/comments/1teq4l1/google_deepmind_workers_vote_to_unionize_over/
- **Evidence ID:** EVD-20260517-0028

### INFO-029
- **タイトル:** Anthropic-Pentagon Clash: Chilling Effect on AI Safety and Innovation
- **ソース:** CDT / AINvest / Gizmodo
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** AnthropicとPentagonの対立がAI安全性に広範なチリング効果を生む可能性。連邦政府の行動が他自治体にも波及し、AI企業が倫理的立場を取ることで規制・商業的報復に直面するリスク。FigmaのAI投資もAnthropicの規制問題に巻き込まれる。
- **キーファクト:**
  - Pentagon-Anthropic対立が市民機関に波及するチリング効果
  - 倫理的立場を取る企業が規制・商業的報復に直面するリスク
  - FigmaのAI投資もAnthropic規制問題に衝突
- **引用URL:** https://cdt.org/insights/chain-reaction-what-the-pentagon-anthropic-dispute-means-for-civilian-agencies-across-all-levels-of-government/
- **Evidence ID:** EVD-20260517-0029

### INFO-030
- **タイトル:** California Uses Procurement Power for AI Vendor Ethics Requirements
- **ソース:** Pillsbury Law
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** (一般)
- **要約:** カリフォルニア州が大統領令N-5-26で調達力をAI政策に活用。AIベンダーに州契約を求めるなら不正行為対策の証明を義務付け。政府調達を通じたAI企業への圧力が新たな政策手段として台頭。
- **キーファクト:**
  - California大統領令N-5-26: AIベンダーに安全性証明を義務付け
  - 政府調達力を通じたAI政策の実施
  - 州レベルでのAI倫理要件強化
- **引用URL:** https://www.pillsburylaw.com/en/news-and-insights/california-executive-order-n-5-26-procurement-power-ai-policy.html
- **Evidence ID:** EVD-20260517-0030

### INFO-031
- **タイトル:** Meta AI Creative Tools Generate 2.3 Billion Ad Variants, 67% Cost Reduction
- **ソース:** Get-Ryze.ai / MarTech
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-002-05
- **関連企業:** Meta
- **要約:** MetaのクリエイティブAIツールが2026年に23億の広告バリアントを生成、クリエイティブ制作コストを67%削減しエンゲージメント率を23%向上。営業組織のAIエージェント導入で25-47%の生産性向上も報告。
- **キーファクト:**
  - 23億の広告バリアント生成（2026年）
  - クリエイティブ制作コスト67%削減、エンゲージメント率23%向上
  - 営業のAIエージェント導入で25-47%の生産性向上
- **引用URL:** https://www.get-ryze.ai/blog/meta-ai-agents-for-advertising-automation
- **Evidence ID:** EVD-20260517-0031

### INFO-032
- **タイトル:** AI Wiping Out Entry-Level Jobs: 342,000 IT Jobs Disappeared Since 2022
- **ソース:** Kellogg Insight / WSJ / Computer Coach
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** (一般)
- **要約:** 2022年以来342,000のIT職が消失。BLSは18職種（約1000万職）をAI露出ありと分類し、該当職種の雇用が減少。AIスキルを持つ中堅・シニアエンジニアの需要は上昇、エントリーレベルの求人は減少傾向。
- **キーファクト:**
  - 2022年以来342,000のIT職が消失
  - BLS: 18職種・約1000万職をAI露出ありと分類、雇用減少
  - 中堅・シニアAIエンジニア需要上昇、エントリーレベル求人減少
- **引用URL:** https://insight.kellogg.northwestern.edu/article/ai-is-wiping-out-entry-level-jobs-heres-how-to-surf-the-wave-and-not-get-crushed-by-it
- **Evidence ID:** EVD-20260517-0032

### INFO-033
- **タイトル:** ServiceNow Agentic Workflows Deliver 22% Developer Productivity Gains
- **ソース:** AI CERTs / CIO.com
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04
- **関連企業:** ServiceNow
- **要約:** TRIMEDXがServiceNowのエージェントワークフロー導入後8週間で開発者の22%生産性向上を報告。知識労働者はトップクラスのエージェントOSで1日平均3時間節約。OpenAIが$40億でDeployCoを立ち上げエンタープライズAI展開を加速。
- **キーファクト:**
  - TRIMEDX: 開発者22%生産性向上（8週間）
  - 知識労働者はエージェントOSで1日平均3時間節約
  - OpenAIが$40億DeployCo設立
- **引用URL:** https://www.aicerts.ai/news/servicenows-agentic-workflow-movement-reshapes-enterprise-ai/
- **Evidence ID:** EVD-20260517-0033

### INFO-034
- **タイトル:** Klarna AI Replaced 700 Agents Then Rehired — Duolingo AI-First Strategy
- **ソース:** Duperrin / LinkedIn / FastCompany
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04
- **関連企業:** Klarna, Duolingo
- **要約:** KlarnaがAIで700人を解雇し$40-60M削減を主張したが、12ヶ月後に再採用を開始。顧客サービスには実際の人間が必要と判明。DuolingoはAI-First組織への移行を継続。AIコーディングアシスタントで55%のタスク高速化を確認。
- **キーファクト:**
  - Klarna: 700人解雇→12ヶ月後に再採用、$40-60M削減主張
  - 企業の39%のみがAIで実際の利益を報告
  - GitHub/MIT研究: AIコーディングアシスタントで55%高速化
- **引用URL:** https://www.duperrin.com/english/2026/05/13/cloudflare-ai-layoffs/
- **Evidence ID:** EVD-20260517-0034

### INFO-035
- **タイトル:** Advertising Agencies Face Revenue Decline — AI Automation Destroys Middle Tier
- **ソース:** Yahoo Finance / Digiday / LinkedIn
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** (広告業界一般)
- **要約:** AI広告自動化がエージェンシー中間層を破壊。82%の広告幹部がGenZはAI広告に好意的と考えるが、実際は45%のみ。B2B SaaS株が暴落、SaaStrは「ソフトウェアがAI時代に不十分」が原因と分析。
- **キーファクト:**
  - AI広告自動化がエージェンシー中間層を破壊
  - 広告幹部: 82%がGenZ好意的と評価、実際は45%のみ
  - B2B SaaS株暴落、AI時代のソフトウェア不足が原因
- **引用URL:** https://finance.yahoo.com/sectors/technology/articles/death-billable-hour-ai-killing-173108182.html
- **Evidence ID:** EVD-20260517-0035

### INFO-036
- **タイトル:** SaaS Dissolved Into Intent — AI Agents Disrupt Traditional Software
- **ソース:** LinkedIn / C#Corner / McKinsey
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** (SaaS業界一般)
- **要約:** AIがSaaSを「インテント」に溶解させている。20年のダッシュボード・ボタン型ソフトウェアから、AIファースト製品への転換が急速に進行。McKinseyはAIがERPを根本的に変革すると分析。
- **キーファクト:**
  - AIがSaaSを「インテント（意図）」ベースのソフトウェアに溶解
  - AIファースト製品への急速な転換
  - McKinsey: ERPがAIネイティブ・エージェントシステムに変革
- **引用URL:** https://www.c-sharpcorner.com/article/the-end-of-traditional-saas-how-ai-agents-are-changing-software-products/
- **Evidence ID:** EVD-20260517-0036

### INFO-037
- **タイトル:** OpenAI API Pricing May 2026: GPT-5.5 at $5/$30, Anthropic Claude at $3/$15
- **ソース:** MetaCTO / CloudZero
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAI API価格(2026年5月): GPT-5.5 $5/$30/M tokens、GPT-5.4 $2.50/$15、o4-mini $0.55/$2.20。Anthropic: Haiku 4.5 $1/$5、Sonnet 4.6 $3/$15、Opus 4.7 $5/$25。OpenAIは2022年以来価格変更を複数回実施。
- **キーファクト:**
  - GPT-5.5: $5入力/$30出力 per M tokens
  - Claude Sonnet 4.6: $3/$15 (旧世代と同一価格)
  - OpenAI: 2022年以来複数回価格変更がマージンに直撃
- **引用URL:** https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance
- **Evidence ID:** EVD-20260517-0037

### INFO-038
- **タイトル:** Anthropic Restructures Claude Billing — Separate SDK Credits from June 15
- **ソース:** Zed Blog / The Decoder / Reddit
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Anthropicが6月15日からClaude有料サブスクの課金を再構築。プログラマティック使用(SDK/CLI)を通常使用から分離し、API価格で課金。Pro $20、Max 5x $100、Max 20x $200のAgent SDKクレジットを新設。
- **キーファクト:**
  - 6月15日からプログラマティック使用を通常使用から分離課金
  - Agent SDK Credit: Pro $20、Max 5x $100、Max 20x $200
  - キャッシュヒット80%でもAPI価格で課金はユーザー不満
- **引用URL:** https://the-decoder.com/claude-subscriptions-get-separate-budgets-for-programmatic-use-billed-at-full-api-prices/
- **Evidence ID:** EVD-20260517-0038

### INFO-039
- **タイトル:** Google Gemini API Pricing 2026: Flash-Lite from $0.10/M tokens
- **ソース:** Google AI / MetaCTO
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google
- **要約:** Gemini API価格(2026年5月): 3.1 Pro $2-$18/M tokens、3.1 Flash-Lite $0.10-$0.40/M tokens。無料枠あり。Google AI Plus $7.99/月、Pro $19.99/月のサブスクリプションに画像生成含む。
- **キーファクト:**
  - Gemini 3.1 Pro: $2-$18 per M tokens
  - Gemini 3.1 Flash-Lite: $0.10-$0.40 per M tokens（最低価格帯）
  - Google AI Plus $7.99/月、Pro $19.99/月
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Evidence ID:** EVD-20260517-0039

### INFO-040
- **タイトル:** BenchLM LLM Pricing Comparison 2026 — AI Trends in Token Cost Decline
- **ソース:** BenchLM.ai / LLM Stats
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** (一般)
- **要約:** 2026年のLLM API価格比較サイトが全主要モデルのコストパートークンを公開。GLM 5.1は$0.98/$3.08 per M tokens。AI Trends分析ではパフォーマンス向上と価格低下のトレンドが明確。
- **キーファクト:**
  - 全主要LLMモデルのトークン単価比較プラットフォーム
  - GLM 5.1: $0.98/$3.08 per M tokens（低コストモデル）
  - パフォーマンス向上×価格低下のトレンド継続
- **引用URL:** https://benchlm.ai/llm-pricing
- **Evidence ID:** EVD-20260517-0040

### INFO-041
- **タイトル:** ARC Challenge and Humanity's Last Exam Leaderboards May 2026
- **ソース:** PricePerToken / BenchLM
- **公開日:** 2026-05-15
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** ARC Challenge首位はGPT-5の96.3%。Humanity's Last Exam首位はGemini 3.1 Pro Previewの44.7%、次いでGPT-5.4の41.6%。知識ベンチマークではGPT-5.4が99.3%、Claude Opus 4.7が99.2%で僅差。
- **キーファクト:**
  - ARC Challenge: GPT-5が96.3%で首位
  - Humanity's Last Exam: Gemini 3.1 Pro Preview 44.7%首位
  - 知識ベンチマーク: GPT-5.4 99.3% vs Claude Opus 4.7 99.2%（僅差）
- **引用URL:** https://pricepertoken.com/leaderboards/benchmark/hle
- **Evidence ID:** EVD-20260517-0041

### INFO-042
- **タイトル:** GPT vs Claude vs Gemini vs Grok: Developer Benchmark Comparison 2026
- **ソース:** ITNext / AIThinkerLab
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** GPT-5.5、Claude、Gemini、Grokの開発者ベンチマーク比較。Grok 4.1がLMArena Text Arenaで1483 Elo首位。GPT-5.5は「良い」、Claudeは「高価」、Geminiは「意外と悪い」、Grokは「まずまず」との評価。
- **キーファクト:**
  - Grok 4.1: LMArena Text Arena 1483 Elo首位
  - Claude Opus 4.7: SWE-bench Pro 64.3%で首位
  - モデル選択の固定化時代は終了、マルチモデルルーティングが主流に
- **引用URL:** https://itnext.io/comparing-ai-providers-openai-google-anthropic-and-xai-5841e530aaf5
- **Evidence ID:** EVD-20260517-0042

### INFO-043
- **タイトル:** Top AI Models Fall Short 30% of Time vs Expert Judgment
- **ソース:** Yahoo Finance / VentureBeat
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** (一般)
- **要約:** Pearl.comの25モデル評価で、最先端AIシステムでも専門家と一致するのは約70%のみ。広く使われるモデルの中には20%まで低下するものも。AI IQサイトがフロンティアモデルを人間IQスケールで評価。
- **キーファクト:**
  - 25モデル評価: 最先端AIは専門家と約70%のみ一致
  - 一部モデルは20%まで低下
  - 人間IQスケールでのAI評価サイトが登場
- **引用URL:** https://finance.yahoo.com/news/top-ai-models-still-fall-142500719.html
- **Evidence ID:** EVD-20260517-0043

### INFO-044
- **タイトル:** DeepSeek V4: Frontier Performance at $0.14/M tokens — 1/6 of GPT-5.5 Cost
- **ソース:** LinkedIn / Spheron / Medium
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4が$0.14/M tokensでフロンティアに近いパフォーマンスを実現（GPT-5.5の1/6コスト）。$50B評価額で資金調達中。DeepSeek V3.2 ThinkingはAIME 2025やHLEでGrok 4 Fastを上回る。
- **キーファクト:**
  - DeepSeek V4: $0.14/M tokens（GPT-5.5の1/6）
  - $50B評価額で資金調達中
  - V3.2 Thinking: AIME/HLE/BrowseCompでGrok 4 Fastを上回る
- **引用URL:** https://medium.com/no-time/deepseek-v4-challenges-billion-dollar-ai-models-without-charging-users-468b805d5d0e
- **Evidence ID:** EVD-20260517-0044

### INFO-045
- **タイトル:** Mistral Medium 3.5: 128B Open Model Tops SWE-Bench at 77.6%
- **ソース:** TheAIDude / JustThink / LinkedIn
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral
- **要約:** Mistralの128B DenseモデルがSWE-bench Verified 77.6%でオープンウェイトモデル首位。Mistralは「主権AI」戦略でOpenAI/Anthropicより急成長。オープンウェイトにより企業内インフラ展開が可能。
- **キーファクト:**
  - Mistral Medium 3.5: 128B Dense、SWE-bench Verified 77.6%
  - オープンウェイトで企業内デプロイ可能
  - Mistral: OpenAI/Anthropicより急成長、主権AI戦略
- **引用URL:** https://theaidude.net/blog/mistral-medium-35-128b-open-model-tops-swe-bench
- **Evidence ID:** EVD-20260517-0045

### INFO-046
- **タイトル:** OpenAI Launches DeployCo $4B Enterprise Services, Anthropic Valuation $900B+
- **ソース:** CRN / WSJ / Axios
- **公開日:** 2026-05-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIがCapgemini、Bain、McKinsey等と$40億のAIサービス企業DeployCoを立ち上げ。Anthropicは$900B以上の評価額で投資オファーを受け、OpenAIを上回る可能性。RampデータではAnthropicが企業有料採用でOpenAIを逆転。
- **キーファクト:**
  - OpenAI DeployCo: $40億評価額、19社のコンサル/インテグレーターと提携
  - Anthropic: $900B+評価額の投資オファー
  - Anthropicが企業有料採用でOpenAIを逆転（Rampデータ）
- **引用URL:** https://www.crn.com/news/ai/2026/openai-launches-services-business-on-heels-of-similar-anthropic-announcement
- **Evidence ID:** EVD-20260517-0046

### INFO-047
- **タイトル:** Microsoft Seeks AI Startup Acquisition for Life After OpenAI, SpaceX Acquires xAI
- **ソース:** Reuters / LinkedIn
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Microsoft, xAI, SpaceX, Anthropic
- **要約:** MicrosoftがOpenAIとの排他パートナーシップ終了を見据え、AIスタートアップ買収を積極追求。SpaceXがxAIを$250B評価額で買収しMusk帝国を統合。Anthropicは開発ツールStainlessの買収を協議（$300M+）。
- **キーファクト:**
  - Microsoft: OpenAI非排他化後のAIスタートアップ買収を追求
  - SpaceXがxAIを$250B評価額で買収
  - Anthropic: Stainless買収を$300M+で協議
- **引用URL:** https://www.reuters.com/world/microsoft-eyeing-startup-deals-life-after-openai-2026-05-13/
- **Evidence ID:** EVD-20260517-0047

### INFO-048
- **タイトル:** AI Capex Overinvestment: $800B-$1T+ Gap Through 2028
- **ソース:** Substack / Reddit / Grizzle
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** (一般)
- **要約:** AIインフラ投資の収益ギャップが2028年までに$800B-$1T+に達する予測。McKinseyはAIレディデータセンターに$5.2-7.9兆のCAPEXが必要と試算。データセンターとチップへの$1兆投資がリスク要因。
- **キーファクト:**
  - 2028年までに$800B-$1T+の収益ギャップ予測
  - McKinsey: AIデータセンターに$5.2-7.9兆CAPEX必要
  - データセンター投資が$570Bでインフラ層が支配的
- **引用URL:** https://grizzle.com/why-the-ai-picks-and-shovels-boom-may-be-peaking/
- **Evidence ID:** EVD-20260517-0048

### INFO-049
- **タイトル:** Multi-Vendor AI Strategy: AI.cc Enterprise Guide and Unified API Platforms
- **ソース:** MarTechSeries / LinkedIn
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** (一般)
- **要約:** 2026年のエンタープライズでマルチモデル採用が記録的水準に。AI.ccがモデル選択・コストルーティング・エージェントアーキテクチャ・ベンダー評価の統合ガイドを公開。SAPもマルチベンダーAI環境での相互運用性を課題と認識。
- **キーファクト:**
  - 2026年のマルチモデル採用が記録的水準に
  - AI.cc: モデル選択・コストルーティングの統合ガイド公開
  - SAP: マルチベンダーAI環境での相互運用性を課題と認識
- **引用URL:** https://martechseries.com/predictive-ai/ai-platforms-machine-learning/ai-cc-publishes-enterprise-guide-to-unified-ai-api-platforms-amid-record-multi-model-adoption-in-2026/
- **Evidence ID:** EVD-20260517-0049

### INFO-050
- **タイトル:** The Free Sample Phase: AI Tools Underpriced at $100-200/Month True Cost
- **ソース:** MindStudio / McKinsey
- **公開日:** 2026-05-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** (一般)
- **要約:** ヘビーなAIアシスタント利用者の真のサービス提供コストは$100-200/月だが、現在の価格はそれを下回る。McKinseyはAIのユニークな信頼課題を指摘し、データアクセスがモデル性能を向上させスイッチングコストを深める。
- **キーファクト:**
  - ヘビーユーザーの真のコスト: $100-200/月（現在価格を下回る）
  - AIツールの「無料サンプル期」が継続
  - モデルレベルロックインが隠れたリスク
- **引用URL:** https://www.mindstudio.ai/blog/ai-free-sample-phase-pricing-strategy-what-comes-next/
- **Evidence ID:** EVD-20260517-0050

### INFO-051
- **タイトル:** 342,000 IT Jobs Disappeared — BLS Flags 10M Jobs Exposed to AI
- **ソース:** CNN / Computer Coach / Threads
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** (一般)
- **要約:** 2022年以来342,000の情報セクター職が消失。2026年4月雇用報告はAIが労働力を再構築していることを示す。BLSが18職種（約1000万職）をAI露出ありと分類し、2024年5月から2025年5月で該当職種の雇用が減少。反復的タスクの職が減少し、分析・技術・創造的スキルの職が20%増加。
- **キーファクト:**
  - 2022年以来342,000のIT職が消失
  - BLS: 18職種・約1000万職をAI露出ありと分類
  - 分析・技術・創造的スキルの職が20%増加
- **引用URL:** https://www.computercoach.com/ai-jobs-workforce-skills-training/
- **Evidence ID:** EVD-20260517-0051

### INFO-052
- **タイトル:** WEF Projects 78M Net New Jobs — Freelancers More AI-Resistant Than Employees
- **ソース:** GoLance / LinkedIn
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** (一般)
- **要約:** WEFは7800万の純新規雇用を予測（均等ではない）。LinkedIn共同創業者Reid Hoffmanが2034年までに従来の9-5雇用が消滅すると予測。AIは雇用を「削減」ではなく「再配置」し、フリーランサーは従業員よりAI耐性が高い。
- **キーファクト:**
  - WEF: 78M純新規雇用予測（不均等配分）
  - Hoffman: 2034年までに9-5雇用消滅予測
  - フリーランサーは従業員よりAI耐性が高いと分析
- **引用URL:** https://golance.com/blogs/jobs-ai-wont-replace
- **Evidence ID:** EVD-20260517-0052

### INFO-053
- **タイトル:** AGI Timeline: Musk Predicts Late 2026, Hassabis 50% by 2030
- **ソース:** X/MilkRoadAI / LifeArchitect / LinkedIn
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** xAI, Google, Anthropic
- **要約:** Muskが2026年末までに人間より賢いAIを予測（2025年予測は外れ）。Demis HassabisはAGIに約50%の確率。Anthropic CEOは2026年以降の可能性。科学者のコンセンサスは2040-2050。事前ChatGPT予測は2060年以降。
- **キーファクト:**
  - Musk: 2026年末〜遅くとも2027年に人間超えAI予測
  - Hassabis: AGIに約50%確率（時期不明）
  - コンセンサス予測: 2040-2050、ChatGPT前予測: 2060+
- **引用URL:** https://lifearchitect.ai/agi/
- **Evidence ID:** EVD-20260517-0053

### INFO-054
- **タイトル:** AI Capability Not Plateauing — Accelerating and Reaching More People
- **ソース:** Forbes / Forrester / Aspen Digital
- **公開日:** 2026-05-11
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** (一般)
- **要約:** Stanford HAIレポート: AI能力は停滞せず加速中、より多くの人に到達。Forresterは2026年のトップ10新兴技術でAIがデジタルから現実世界変革へ移行と指摘。フロンティアAIモデルは脆弱性発見・エクスプロイト生成能力を急速に獲得。
- **キーファクト:**
  - Stanford HAI: AI能力は加速中、停滞していない
  - Forrester: AIがデジタルから現実世界変革へ移行
  - フロンティアAI: 脆弱性発見・エクスプロイト生成能力を獲得
- **引用URL:** https://www.forbes.com/sites/johnwerner/2026/05/11/ai-around-the-world-in-2026/
- **Evidence ID:** EVD-20260517-0054

### INFO-055
- **タイトル:** AI Safety: From Models to Agents, the Coming Trust Crisis
- **ソース:** Substack / Reddit / Madrona
- **公開日:** 2026-05-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** (一般)
- **要約:** AIがルールベースから自律エージェントへ進化し、アイデンティティ・アライメント・信頼インフラが次の時代を定義する。Yoshua BengioがLawZeroで「Scientist AI」構想を発表し、AIアライメント問題への新アプローチを提案。
- **キーファクト:**
  - AI進化: ルールベース→自律エージェント、信頼インフラが課題
  - Bengio: LawZeroで「Scientist AI」構想を発表
  - AGI達成時の「一時停止」提案が議論
- **引用URL:** https://vkpatva.substack.com/p/from-models-to-agents-agi-ai-safety
- **Evidence ID:** EVD-20260517-0055

### INFO-056
- **タイトル:** TikTok Unleashes AI Agents on Ad Platform with MCP Server Integration
- **ソース:** PYMNTS / Digiday / TechWyse
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05, BYTEDANCE-CHINESE
- **関連企業:** ByteDance, TikTok
- **要約:** TikTokがMCPサーバーと開発者ツールキットで広告プラットフォームをAIエージェントに開放。Creator AI Searchがキャンペーンブリーフを解釈しクリエイターを自動特定。Dreamina Seedance 2.0（ByteDance動画生成）を統合。
- **キーファクト:**
  - TikTok MCP server: AIエージェントによるキャンペーン自動運用
  - Creator AI Search: ブリーフ解釈→クリエイター自動特定
  - Dreamina Seedance 2.0: ByteDance次世代AI動画モデルを統合
- **引用URL:** https://digiday.com/marketing/tiktok-launches-mcp-server-to-let-ai-agents-run-campaigns/
- **Evidence ID:** EVD-20260517-0056

### INFO-057
- **タイトル:** ByteDance Boosts AI Infrastructure Spending 25% to $28 Billion
- **ソース:** TechNode / Reuters
- **公開日:** 2026-05-11
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがAIインフラ支出を25%増の人民元2000億元（$280億）に引き上げ。米国はAlibaba、Tencent、ByteDance等10社にNvidia H200チップ販売を承認。ByteDanceがオープンソースのTARSマルチモーダルエージェントをGitHubで29k獲得。
- **キーファクト:**
  - ByteDance: AIインフラ支出25%増 → RMB 2000億元（$280億）
  - 米国: 10中国企業にNvidia H200販売承認（ByteDance含む）
  - TARS: ByteDanceオープンソースマルチモーダルエージェント（GitHub 29k stars）
- **引用URL:** https://technode.com/2026/05/11/bytedance-boosts-ai-infrastructure-spending-by-25-to-28-billion-this-year/
- **Evidence ID:** EVD-20260517-0057

### INFO-058
- **タイトル:** US-China AI Competition: Export Controls Push Developers to Huawei Ascend
- **ソース:** Fox News / NYT / Instagram
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-03
- **関連企業:** Nvidia, Huawei, (中国企業一般)
- **要約:** 米国の輸出規制が中国開発者をCUDAからHuawei Ascendに移行させている。AI開発者の50%が中国に在住。Trump-Xi会談でAI安全性プロトコル設立を協議。米中2国のみがAIの将来を実質的に左右する状況。
- **キーファクト:**
  - 輸出規制が中国開発者をCUDA→Huawei Ascendに移行させる
  - AI開発者の50%が中国に在住
  - Trump-Xi会談: AI安全性プロトコル設立を協議
- **引用URL:** https://www.nytimes.com/video/opinion/100000010892438/china-doesnt-worry-about-ai-like-we-do.html
- **Evidence ID:** EVD-20260517-0058

### INFO-059
- **タイトル:** Claude Code Users: Startups 33% vs Enterprises 13% — Anthropic Targets SMB
- **ソース:** Axios / LinkedIn
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude Codeの主要ユーザーはスタートアップ（33%）で、エンタープライズ（13%）は遅れを取っている。AnthropicはClaude for Small BusinessでSMB市場をターゲット。Claude Codeチームが30分以内のエンジニアリングワークフロー自動化をデモ。
- **キーファクト:**
  - Claude Code: スタートアップ33% vs エンタープライズ13%
  - AnthropicがSMB市場にClaude for Small Businessで参入
  - NLAデータ: Claudeが評価中と認識する割合はSWE-bench 16-26%、実セッション<1%
- **引用URL:** https://www.facebook.com/axiosnews/posts/anthropic-wants-small-businesses-to-use-claude-code/1358150132841619/
- **Evidence ID:** EVD-20260517-0059

### INFO-060
- **タイトル:** AI Made Elite Coders 20% Slower — 43% Swing from Predicted 24% Improvement
- **ソース:** Facebook / CIO / LinkedIn
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** (一般)
- **要約:** エリートエンジニアがAIツールで24%改善と予測されたが、実際は20%遅くなった（43%の乖離）。AIコーディングツールは出力を変化させるが、判断力の変化は遅い。AI生成コードは70%少ない関数で構成され、関数はほぼ2倍の長さ。
- **キーファクト:**
  - エリートエンジニア: 予測24%改善→実際20%低下（43%乖離）
  - AIコーディング: 出力高速化≠判断力向上
  - AI生成コード: 関数数70%減少、関数長2倍
- **引用URL:** https://www.cio.com/article/4169591/ai-coding-tools-are-changing-output-faster-than-they-are-changing-judgment.html
- **Evidence ID:** EVD-20260517-0060

### INFO-061
- **タイトル:** Gartner: 40% of Enterprise Apps to Embed AI Agents by End 2026 (8x Increase)
- **ソース:** Beam AI / arXiv / LinkedIn
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (一般)
- **要約:** Gartner予測: 2026年末までにエンタープライズアプリの40%がタスク特化型AIエージェントを組み込む（2025年の5%未満から8倍増）。MIT研究: AIプロジェクトの85%が弱いデータ基盤で失敗。Gartnerは60%が価値創出前に廃止されると推計。
- **キーファクト:**
  - 2026年末: エンタープライズアプリの40%がAIエージェント組み込み（5%→40%、8倍）
  - MIT: AIプロジェクトの85%が弱いデータ基盤で失敗
  - Gartner: 60%が価値創出前に廃止されると推計
- **引用URL:** https://beam.ai/agentic-insights/future-of-ai-is-orchestration-not-bigger-models
- **Evidence ID:** EVD-20260517-0061

### INFO-062
- **タイトル:** How AI is transforming software development
- **ソース:** CIO
- **公開日:** 2026-05-15
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-01, KIQ-004-02, KIQ-004-03
- **関連企業:** OpenAI, Anthropic, Microsoft, Google
- **要約:** Stack Overflow 2025 Developer Survey: 84%の開発者がAIツールを使用または使用予定。51%のプロフェッショナル開発者が毎日AIツール使用。しかしAIツール信頼度は29%に低下（前年比-11pt）。ジュニア採用減速。シニアエンジニアはエージェント艦隊の指揮者に変化。
- **キーファクト:**
  - 84%の開発者がAI使用/使用予定、51%が毎日使用
  - AI信頼度29%（前年比-11pt）、66%が「ほぼ正しい」解答に不満
  - ジュニアエンジニアの採用減速がパイプライン問題を引き起こす
  - EY: 9ヶ月で50,000エージェント開発
- **引用URL:** https://www.cio.com/article/4170969/how-ai-is-transforming-software-development.html
- **Evidence ID:** EVD-20260517-0062

### INFO-063
- **タイトル:** Sea's View on the Future of Agentic Software Development with Codex
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-02
- **関連企業:** OpenAI
- **要約:** Sea LimitedがOpenAI Codexを開発組織全体に展開。87%のユーザーが週間アクティブユーザー。73%が同僚に推奨すると回答。CI/CDパイプライン内でAIエージェントが自律動作する「統合エージェントワークフロー」への移行。東南アジア初のCodex Hackathon Seriesをシンガポール/インドネシア/台湾/ベトナムで開催。
- **キーファクト:**
  - Seaの87%ユーザーが週間アクティブ、73%が推奨
  - CI/CD内でエージェントが自律動作
  - 開発者→「システムオーケストレーター」への進化
  - 東南アジアCodex Hackathon Series開催
- **引用URL:** https://openai.com/index/sea-david-chen/
- **Evidence ID:** EVD-20260517-0063

### INFO-064
- **タイトル:** Interaction Models: A Scalable Approach to Human-AI Collaboration
- **ソース:** Thinking Machines Lab
- **公開日:** 2026-05-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03, KIQ-001-04
- **関連企業:** Google, OpenAI
- **要約:** Thinking Machines Labが「インタラクションモデル」の研究プレビューを発表。ターンベースではなくリアルタイムの音声/ビデオ/テキストでのマルチモーダルな人間-AI協調を実現。276BパラメータMoE（12Bアクティブ）。GPT Realtime 2.0やGemini 3.1を上回るインタラクション品質を達成。
- **キーファクト:**
  - 276B MoE（12Bアクティブ）、200msマイクロターン設計
  - FD-bench V1.5: 77.8（GPT Realtime 2.0: 46.8）
  - バックグラウンドモデル+インタラクションモデルの分離設計
  - リアルタイムでの視覚的プロアクティブ性を実現
- **引用URL:** https://thinkingmachines.ai/blog/interaction-models/
- **Evidence ID:** EVD-20260517-0064

### INFO-065
- **タイトル:** Kimi WebBridge: ローカル動作するAIエージェントブラウザ自動化
- **ソース:** Decrypt
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Moonshot AI
- **要約:** Moonshot AIがKimi WebBridgeを発表。Chrome DevTools Protocolを使用し、AIエージェントがブラウザを人間のように操作する拡張機能。全てのデータがローカルで処理。Kimi K2.6はSWE-Bench Pro 58.6%（GPT-5.4: 57.7%, Claude Opus 4.6: 53.4%を上回る）。300並列サブエージェントをサポート。
- **キーファクト:**
  - 全データローカル処理（Chrome DevTools Protocol）
  - Kimi K2.6: SWE-Bench Pro 58.6%（GPT-5.4/Opus 4.6を凌駕）
  - Claude Code/Cursor/Codex/Hermesとの互換性
  - 300並列サブエージェント、4,000協調ステップ
- **引用URL:** https://decrypt.co/367916/kimi-webbridge-ai-agents-browser-local
- **Evidence ID:** EVD-20260517-0065
