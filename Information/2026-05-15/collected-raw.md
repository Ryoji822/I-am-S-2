# 収集データ: 2026-05-15

## メタデータ
- 収集日時: 2026-05-15 02:30 UTC
- 実行クエリ数: 56 / 56
- scrape実行数: 12件
- 収集情報数: 40件
- Evidence ID 採番範囲: EVD-20260515-0001 〜 EVD-20260515-0040
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 品質フラグ: PARTIAL (40件のみ。50件目標に未達だが主要KIQは全カバー。BYTEDANCE中国語一次情報は36Kr/知乎等で確保)

## 収集結果

### INFO-001
- **タイトル:** Work with Codex from anywhere
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIがCodexをChatGPTモバイルアプリに統合しプレビュー公開。携帯からリモート環境で動作中のCodexに接続し、スレッド管理・承認・差分確認が可能。Remote SSHの一般提供、Programmatic access tokens、Hooks GA、HIPAA準拠対応も発表。400万人以上が週間でCodexを利用中。
- **キーファクト:**
  - Codexモバイル: iOS/AndroidでリモートCodexセッションの管理・承認が可能
  - Remote SSH GA: 管理されたリモート環境への直接接続
  - Programmatic access tokens: CIパイプライン向けスコープ付き認証情報（Enterprise/Business）
  - HIPAA準拠: ChatGPT Enterpriseのローカル環境でのCodex利用
  - 週間400万+ユーザーがCodexを利用
- **引用URL:** https://openai.com/index/work-with-codex-from-anywhere/
- **Evidence ID:** EVD-20260515-0001

### INFO-002
- **タイトル:** Helping ChatGPT better recognize context in sensitive conversations
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPTの安全性機能を強化。会話内で徐々に現れるリスク信号を認識するコンテキスト認識機能を導入。自傷・他害シナリオで安全応答率が50%改善。会話をまたぐ安全性要約（safety summaries）も導入。精神的健康専門家との2年以上の協力に基づく。
- **キーファクト:**
  - 長文会話での安全応答率: 自傷ケース50%改善、他害ケース16%改善
  - GPT-5.5 Instantで他害52%、自傷39%改善
  - Safety summaries: 安全性関連コンテキストの短いメモ（限定期間保持）
  - 精神科医・心理学者との協力で自殺防止・自傷・他害に特化
- **引用URL:** https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations/
- **Evidence ID:** EVD-20260515-0002

### INFO-003
- **タイトル:** OpenAI launches the OpenAI Deployment Company (DeployCo) — acquires Tomoro
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01, KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがOpenAI Deployment Company（DeployCo）を設立。エンタープライズ向けのAI展開特化企業で、Tomoro（AIコンサルティング企業、約150名のFDE）を買収。TPG、Advent、Bain Capital、Goldman Sachs、SoftBank等19社がパートナー。$40億+の初期投資で開始。OpenAIが過半数所有・支配。
- **キーファクト:**
  - DeployCo: OpenAI過半数所有のエンタープライズAI展開会社
  - Tomoro買収: 約150名のForward Deployed Engineers獲得
  - 投資: $40億+の初期投資（TPG、Advent、Goldman Sachs、SoftBank等19社）
  - コンサルパートナー: Bain、Capgemini、McKinsey
  - 100万+のビジネスがOpenAI製品/APIを採用済み
- **引用URL:** https://openai.com/index/openai-launches-the-deployment-company/
- **Evidence ID:** EVD-20260515-0003

### INFO-004
- **タイトル:** Introducing Grok Build Early Beta — xAI coding agent CLI
- **ソース:** xAI Official Blog
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIがGrok Build（コーディングエージェントCLI）のアーリーベータをローンチ。SuperGrok Heavy向け。プランレビュー・差分承認のワークフロー、サブエージェント並列実行、AGENTS.md/プラグイン/フック/スキル/MCPサーバー対応。ヘッドレスモード（-p）とACPサポート。
- **キーファクト:**
  - Grok Build: ターミナルベースのコーディングエージェント（SuperGrok Heavy向け）
  - プラン→レビュー→承認のワークフロー
  - サブエージェントの並列実行、worktree統合
  - AGENTS.md、プラグイン、フック、スキル、MCPサーバーのネイティブ対応
  - ヘッドレスモード・ACPサポートでCI/自動化対応
- **引用URL:** https://x.ai/news/grok-build-cli
- **Evidence ID:** EVD-20260515-0004

### INFO-005
- **タイトル:** Introducing Claude Sonnet 4.6 — full upgrade across coding, computer use, reasoning
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-001-04, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Sonnet 4.6をリリース。コーディング・コンピュータ使用・長文脈推論・エージェント計画の全面アップグレード。1M tokenコンテキストウィンドウ（ベータ）。価格は$3/$15 per 1M tokens（Sonnet 4.5と同価格）。Claude CodeでSonnet 4.5より70%好まれる。OSWorldベンチマークで大幅改善。SWE-bench Verified 80.2%。
- **キーファクト:**
  - Sonnet 4.6: 1M tokenコンテキストウィンドウ（ベータ）
  - Claude Code: Sonnet 4.5より70%、Opus 4.5より59%好まれる
  - SWE-bench Verified: 80.2%
  - OSWorld: Sonnet 4.5から大幅改善（コンピュータ使用スキル）
  - 価格: $3/$15 per 1M tokens（変更なし）
  - Databricks、Replit、Cursor、GitHub等が評価で好意的
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6
- **Evidence ID:** EVD-20260515-0005

### INFO-006
- **タイトル:** Anthropic builds enterprise AI services company with Blackstone, H&F, Goldman Sachs
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-05-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01, KIQ-003-04
- **関連企業:** Anthropic
- **要約:** AnthropicがBlackstone、Hellman & Friedman、Goldman Sachsと共同で新AIサービス企業を設立。中堅企業向けにClaudeを導入するカスタムソリューションを構築。General Atlantic、Apollo、Sequoia等も出資。Claude Partner Networkの拡張。AnthropicのApplied AIエンジニアが顧客と直接協力。
- **キーファクト:**
  - 新AIサービス会社: Blackstone、H&F、Goldman Sachsとの合弁
  - 対象: 中堅企業（地域医療、製造業、コミュニティバンク等）
  - 出資: General Atlantic、Leonard Green、Apollo、GIC、Sequoia
  - Claude Partner Networkの拡張（Accenture、Deloitte、PwC等と併存）
- **引用URL:** https://www.anthropic.com/news/enterprise-ai-services-company
- **Evidence ID:** EVD-20260515-0006

### INFO-007
- **タイトル:** Introducing Claude for Small Business — connectors and workflows for SMBs
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-002-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude for Small Businessをローンチ。QuickBooks、PayPal、HubSpot、Canva、Docusign等のツールと統合する15のエージェントワークフローと15のスキルを提供。給与計画、月次決算、キャンペーン実行等を自動化。SMBツアー（10都市）とPayPal提携のAI教育コースも発表。
- **キーファクト:**
  - 15のエージェントワークフロー: 給与、月次決算、キャンペーン等
  - 統合: QuickBooks、PayPal、HubSpot、Canva、Docusign、Google Workspace、Microsoft 365
  - SMBツアー: 10都市（シカゴ〜インディアナポリス）
  - AI Fluency for Small Business: PayPal提携の無料オンラインコース
  - CDFI 3社と提携しAI活用支援
- **引用URL:** https://www.anthropic.com/news/claude-for-small-business
- **Evidence ID:** EVD-20260515-0007

### INFO-008
- **タイトル:** Google AI Impact Summit 2026 — $15B India investment, global partnerships
- **ソース:** Google Official Blog
- **公開日:** 2026-02-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-003-04, KIQ-005-03
- **関連企業:** Google
- **要約:** GoogleがAI Impact Summit（インド）で包括的なAI展開計画を発表。インドに$150億インフラ投資、$3000万AI for Government Innovation Challenge、$3000万AI for Science Impact Challenge。DeepMindがインド政府とAI for Scienceパートナーシップ。70+言語のリアルタイム翻訳モデル、SynthID 2000万回利用。
- **キーファクト:**
  - インド: $150億AIインフラ投資
  - $3000万 AI for Government Innovation Impact Challenge
  - $3000万 AI for Science Impact Challenge
  - DeepMind: インド政府とのAI for Scienceパートナーシップ
  - リアルタイム翻訳: 70+言語（10インド言語含む）
  - SynthID: 2000万回以上の利用
- **引用URL:** https://blog.google/innovation-and-ai/technology/ai/ai-impact-summit-2026-india/
- **Evidence ID:** EVD-20260515-0008

### INFO-009
- **タイトル:** OpenAI introduces WebSocket execution mode for Responses API — reduces agent latency
- **ソース:** InfoQ
- **公開日:** 2026-05-13
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがResponses APIにWebSocketベースの実行モードを導入。エージェントワークフローのレイテンシを大幅削減。コーディングエージェントやリアルタイムAIシステムでのパフォーマンス向上。
- **キーファクト:**
  - Responses APIにWebSocket実行モードを追加
  - エージェントワークフローのレイテンシ大幅削減
  - コーディングエージェント・リアルタイムAI向け最適化
- **引用URL:** https://www.infoq.com/news/2026/05/openai-websocket-responses-api/
- **Evidence ID:** EVD-20260515-0009

### INFO-010
- **タイトル:** ByteDance plans to turn OpenClaw craze into profitable AI business
- **ソース:** South China Morning Post
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがOpenClawブームを収益化する戦略。Claude Code、OpenCode、Trae、OpenClaw、Hermes Agent、ArkClaw等のコーディング・エージェントプラットフォームと連携するパッケージを提供。Coze/豆包エコシステムからエージェント市場への展開を加速。
- **キーファクト:**
  - OpenClaw/Cozeエコシステムの収益化戦略
  - Claude Code、Trae、Hermes Agent等との連携パッケージ
  - ArkClawエージェントの提供
  - コーディングエージェント市場への本格参入
- **引用URL:** https://amp.scmp.com/tech/tech-trends/article/3353310/how-bytedance-plans-turn-openclaw-craze-profitable-ai-business
- **Evidence ID:** EVD-20260515-0010

### INFO-011
- **タイトル:** AI Agent Framework comparison 2026 — LangGraph leads, Claude Agent SDK rising
- **ソース:** Respan / Reddit / Medium
- **公開日:** 2026-05-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI, Anthropic, Google, Microsoft
- **要約:** 2026年のAIエージェントフレームワーク比較。トップ12はClaude Agent SDK、Vercel AI SDK、LangGraph、OpenAI Agents SDK、CrewAI、Mastra、AutoGen/AG2、Google ADK、Pydantic AI等。LangGraphが本番比較で勝利。DatadogのState of AI Engineering 2026レポートでは運用複雑性が最大の課題。
- **キーファクト:**
  - トップフレームワーク: Claude Agent SDK、LangGraph、OpenAI Agents SDK等
  - LangGraphがメモリ・コンテキスト管理・ツール呼び出しで総合優位
  - Datadog: 運用複雑性がAIスケーリングの最大課題
  - Auth0: AIエージェント向けAPI認証の新機能提供
- **引用URL:** https://www.respan.ai/articles/best-ai-agent-frameworks-2026
- **Evidence ID:** EVD-20260515-0011

### INFO-012
- **タイトル:** ChatGPT Enterprise vs Claude Enterprise: Feature Matrix — Claude matches or exceeds compliance
- **ソース:** Intuition Labs
- **公開日:** 2026-05-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI, Anthropic
- **要約:** ChatGPT EnterpriseとClaude Enterpriseの詳細比較。Claude Enterpriseがエンドツーエンド暗号化、SOC2、ISO認証で同等以上。OpenAIはSOC2 Type IIとISO 27001を文書化。FedRAMP対応デプロイはOpenAIが先行。
- **キーファクト:**
  - Claude Enterprise: SOC2、ISO認証、エンドツーエンド暗号化で同等以上
  - OpenAI: SOC2 Type II、ISO 27001、FedRAMP対応で先行
  - OpenAIのDPAは一部競合より弱いとの指摘
  - Gartner: エンタープライズエージェントAIのセキュリティリスク拡大
- **引用URL:** https://intuitionlabs.ai/articles/chatgpt-vs-claude-enterprise-comparison
- **Evidence ID:** EVD-20260515-0012

### INFO-013
- **タイトル:** KPMG: Enterprise AI Agents Strategy — when to employ or forgo
- **ソース:** KPMG
- **公開日:** 2026-05-13
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** N/A
- **要約:** KPMGがCIO向けにAIエージェント戦略の意思決定フレームワークを発表。エージェントが価値を生む領域とリスクを導入する領域の判別、安全な運用化方法を解説。Forrester調査では45%以上の企業がエンタープライズ全体でAIエージェント導入を加速中。
- **キーファクト:**
  - KPMG: CIO向けAIエージェント戦略フレームワーク
  - Forrester: 45%+の企業がエンタープライズ全体でAIエージェント加速
  - エージェントが価値を生む領域とリスク領域の判別が必要
  - 安全な運用化の実践的ガイダンス
- **引用URL:** https://kpmg.com/us/en/articles/2026/enterprise-ai-agents-strategy.html
- **Evidence ID:** EVD-20260515-0013

### INFO-014
- **タイトル:** OpenAI launches 3 new realtime voice models — GPT Realtime 2, Translate, Whisper
- **ソース:** MindStudio / OpenAI
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIが3つのリアルタイム音声モデルを一挙ローンチ。GPT Realtime 2はGPT-5クラスの推論を音声エージェントに提供。gpt-realtime-translateは多言語リアルタイム翻訳。GPT-5.5はテキスト・画像・音声をネイティブ処理するマルチモーダルモデル。
- **キーファクト:**
  - GPT Realtime 2: GPT-5クラス推論をリアルタイム音声に提供
  - gpt-realtime-translate: マルチ言語リアルタイム翻訳モデル
  - GPT-5.5: テキスト・画像・音声ネイティブマルチモーダル
  - 音声エージェントがリアルタイムで実用化
- **引用URL:** https://www.mindstudio.ai/blog/openai-3-new-realtime-voice-models-api-access
- **Evidence ID:** EVD-20260515-0014

### INFO-015
- **タイトル:** Google Gemini Omni leaked — unified multimodal model; OpenAI shuts down Sora 2
- **ソース:** TechCrunch / X (Twitter)
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-04
- **関連企業:** Google, OpenAI
- **要約:** GoogleのGemini Omni統合マルチモーダルモデルがリーク。OpenAIがSora 2をシャットダウンしコンピュートをロボティクスに転用。Gemini Agentsがアクションのスケジューリングとスキル自律利用を開始。AI企業の戦略的シフトが鮮明に。
- **キーファクト:**
  - Gemini Omni: Googleの統合マルチモーダルモデル（リーク）
  - OpenAI: Sora 2シャットダウン、ロボティクスにコンピュート転用
  - Gemini Agents: アクションのスケジューリング・スキル自律利用開始
  - 両社の戦略的シフトが進行
- **引用URL:** https://techcrunch.com/2026/05/12/google-brings-agentic-ai-and-vibe-coded-widgets-to-android/
- **Evidence ID:** EVD-20260515-0015

### INFO-016
- **タイトル:** Anthropic Sandbox Runtime open-sourced for Claude Code
- **ソース:** GitHub (Anthropic)
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがSandbox Runtime（srt）をオープンソース公開。Claude Code向けの安全なエージェント実行環境。ネットワーク隔離、ファイルシステム制御、プロセス実行制限を提供。CheckmarxがClaude Codeのセキュリティリスク6項目と管理策を分析。
- **キーファクト:**
  - Sandbox Runtime: Claude Code向けOSS実行環境
  - ネットワーク隔離、ファイルシステム制御、プロセス制限
  - Checkmarx: コマンド実行リスクを権限・承認・サンドボックスで軽減
  - Bifrost MCP: MCP問題の解決策として90%コスト削減を主張
- **引用URL:** https://github.com/anthropic-experimental/sandbox-runtime
- **Evidence ID:** EVD-20260515-0016

### INFO-017
- **タイトル:** Agent Skills standard: SKILL.md format gains adoption — cross-agent portability
- **ソース:** Agensi / GitHub
- **公開日:** 2026-05-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** N/A
- **要約:** SKILL.mdフォーマットがエージェント間ポータビリティ標準として採用拡大。1つのスキルを全エージェントで利用可能。AGENTS.md、CLAUDE.md、.cursorrulesとの比較でSKILL.mdが移植性に優れる。300+のポータブルスキルが利用可能。
- **キーファクト:**
  - SKILL.md: エージェント間ポータビリティ標準フォーマット
  - 300+のポータブルスキルが利用可能
  - AGENTS.md vs SKILL.md vs CLAUDE.md vs .cursorrulesの比較
  - 1スキル・全エージェント対応の設計思想
- **引用URL:** https://www.agensi.io/learn/agents-md-vs-skill-md-vs-claude-md-cursorrules
- **Evidence ID:** EVD-20260515-0017

### INFO-018
- **タイトル:** NVIDIA and SAP: OpenShell for specialized enterprise agents
- **ソース:** NVIDIA Blog / SAP Newsroom
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-05, KIQ-001-03
- **関連企業:** NVIDIA, SAP, Anthropic, Google, Microsoft, Amazon
- **要約:** SAPがNVIDIA OpenShell（OSSエージェントランタイム）をSAP Business AI Platformに組み込み。専門エージェントの信頼できる開発・展開を実現。Azure/SAP連携強化。Boomi/CouchbaseパートナーシップもエンタープライズAIエージェントの信頼性・ガバナンス強化。
- **キーファクト:**
  - SAP: NVIDIA OpenShellをBusiness AI Platformに統合
  - Azure/SAP: SAP Sapphire 2026で連携強化
  - Boomi/Couchbase: エンタープライズAIエージェント向けパートナーシップ
  - Google ADK: GPU加速マルチエージェントアプリ構築
- **引用URL:** https://blogs.nvidia.com/blog/sap-specialized-agents/
- **Evidence ID:** EVD-20260515-0018

### INFO-019
- **タイトル:** AWS Bedrock AgentCore: Payments preview, Agent Toolkit replaces MCP servers
- **ソース:** AWS Blog
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-05
- **関連企業:** Amazon
- **要約:** AWS Bedrock AgentCoreの重要アップデート。AgentCore Payments（プレビュー）でAIエージェントが自律的にAPI/MCPサーバーに支払い可能。Agent Toolkit for AWSがMCP servers/plugins/skillsの後継。マルチエージェントコラボレーション対応。マネージドネットワーク接続パターン追加。
- **キーファクト:**
  - AgentCore Payments: エージェントの自律支払い機能（プレビュー）
  - Agent Toolkit for AWS: MCP serversの後継
  - マルチエージェントコラボレーション対応
  - マネージドネットワーク接続パターン追加
- **引用URL:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/
- **Evidence ID:** EVD-20260515-0019

### INFO-020
- **タイトル:** TIME: Small businesses already replacing workers with AI — 90% code, 70% support automated
- **ソース:** TIME
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** N/A
- **要約:** TIME誌の調査で、中小企業が既にAIで従業員を代替。ある企業ではコードの90%をAI生成、サポート問い合わせの70%をAI対応。McKinseyはエージェントAIがキャンペーン作成・実行を10-15倍加速すると推計。AIエージェントが企業のワークフローの不完全さを露呈。
- **キーファクト:**
  - コード生成90%、サポート対応70%をAI化
  - McKinsey: キャンペーン作成・実行を10-15倍加速
  - AIエージェントが既存ワークフローの構造的欠陥を露呈
  - 中小企業でのAI代替が本格化
- **引用URL:** https://time.com/article/2026/05/14/ai-small-businesses-layoffs/
- **Evidence ID:** EVD-20260515-0020

### INFO-021
- **タイトル:** EU AI Act: Rules changed and deadlines extended — simplification agreement
- **ソース:** Latham & Watkins
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** N/A
- **要約:** EU立法者がAI Actの簡素化合意。ルール重複の削減、新しい禁止事項の導入、ハイリスクAIシステムの期限延長。ただし規制緩和と解釈するのは誤りで、ガバナンス要件は実質的に強化される。8種類のAIが完全禁止、違反時は€3500万または世界売上7%の罰金。
- **キーファクト:**
  - EU AI Act簡素化合意: ルール重複削減・期限延長
  - 8種類のAI完全禁止、違反時€3500万または売上7%罰金
  - ハイリスクAIシステムの期限延長
  - 専門家: 「規制緩和」との解釈は誤り、ガバナンス強化
- **引用URL:** https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines
- **Evidence ID:** EVD-20260515-0021

### INFO-022
- **タイトル:** White House considers AI vetting executive order — conflicting messages
- **ソース:** KXAN / Facebook / Instagram
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** N/A
- **要約:** ホワイトハウスがAI企業向け「審査レジーム」を含む大統領令を浮上。AI企業に政府承認を義務付ける案。90+のAI政策アクションを推進。「AIレースに勝つ」方針と安全性の対立。Sanders上院議員が中国人AI研究者2名を招聘しAI安全性協議。
- **キーファクト:**
  - AI審査レジーム大統領令の可能性
  - 90+のAI政策アクション推進中
  - 「AIレース勝利」方針と安全性の衝突
  - Sanders: 中国人AI研究者招聘で国際AI安全性協議
- **引用URL:** https://www.kxan.com/news/white-house-scrambles-to-tame-ai-fears/
- **Evidence ID:** EVD-20260515-0022

### INFO-023
- **タイトル:** Forbes AI 50 list: Cognition $1B, Anthropic $30B raise, Isomorphic Labs $2.1B
- **ソース:** Forbes / Crunchbase / PRNewswire
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, DeepMind, Cognition
- **要約:** Forbes 2026 AI 50リスト発表。Cognition（AIコーディングエージェント）が$10億調達。Anthropicが$300億追加調達協議中。Isomorphic Labs（DeepMind系）が$21億調達でAI創薬エンジンを拡大。Q1 2026のAI資金調達は$2555億で2025年通年超過。
- **キーファクト:**
  - Forbes AI 50: Cognition $10億、Clay $2.04億等
  - Anthropic: $300億追加調達協議中
  - Isomorphic Labs: $21億調達（AI創薬）
  - Q1 2026 AI資金調達: $2555億
- **引用URL:** https://www.forbes.com/lists/ai50/
- **Evidence ID:** EVD-20260515-0023

### INFO-024
- **タイトル:** OpenAI pricing 2026: GPT-5 Pro $15/$120 per 1M tokens, fine-tuning API winding down
- **ソース:** OpenAI Community / PricePerToken
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** OpenAI
- **要約:** OpenAIのAPI価格は2026年に低下せず上昇。GPT-5 Pro: $15/$120 per 1M tokens。ファインチューニングAPIの段階的縮小。開発者からの不満続出。Pro購読の価格変更（5x→20x）も議論。代替プロバイダーへの移行で80%コスト削減可能との試算。
- **キーファクト:**
  - GPT-5 Pro: $15/$120 per 1M tokens
  - ファインチューニングAPI段階的縮小
  - Pro価格5x→20xへの変更議論
  - 代替プロバイダー移行で80%コスト削減の試算
- **引用URL:** https://community.openai.com/t/openai-is-winding-down-the-fine-tuning-api-and-platform-discussion-thread/1380522
- **Evidence ID:** EVD-20260515-0024

### INFO-025
- **タイトル:** Best open source LLM 2026: DeepSeek V4 leads, gap narrowing with frontier
- **ソース:** BenchLM / Reddit / SAGE Journals
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03, KIQ-003-02
- **関連企業:** DeepSeek, Meta, Google
- **要約:** 2026年のオープンソースLLMランキング。DeepSeek V4がトップ、Kimi K2.6、GLM-5、Qwen3.5、Gemma 4、Llamaが続く。ファインチューニングされたOSSモデルが商用ベースラインに匹敵。ローカルLLMは12-24ヶ月で主流化との見方。Gemma 4はApache 2.0で最強のオープンモデル。
- **キーファクト:**
  - DeepSeek V4: オープンソースLLM首位
  - ファインチューニングOSSが商用ベースラインに匹敵
  - ローカルLLM: 12-24ヶ月で主流化の見方
  - Qwen3.6を夜間バッチで活用する戦略
- **引用URL:** https://benchlm.ai/blog/posts/best-open-source-llm
- **Evidence ID:** EVD-20260515-0025

### INFO-026
- **タイトル:** Kellogg / NACE: AI wiping out entry-level jobs — but unlocking junior potential
- **ソース:** Kellogg Northwestern / NACE / TechRadar
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02, KIQ-004-01
- **関連企業:** N/A
- **要約:** Kellogg経営大学院がAIによるエントリーレベル職消滅を分析。ジュニア社員はAIエージェントを管理するスキルが必要に。NACE調査では、初期キャリア層がルーチン業務をAIで代替される一方、AIを柔軟に使う若手の優位性も指摘。ホワイトカラー全般でエントリーレベル職への影響懸念。
- **キーファクト:**
  - Kellogg: エントリーレベル職のAI代替進行
  - NACE: ジュニア社員はAIエージェント管理スキルが必要
  - 若手のAI適応力が逆に優位性に
  - 金融・税務等のホワイトカラー職への波及
- **引用URL:** https://insight.kellogg.northwestern.edu/article/ai-is-wiping-out-entry-level-jobs-heres-how-to-surf-the-wave-and-not-get-crushed-by-it
- **Evidence ID:** EVD-20260515-0026

### INFO-027
- **タイトル:** AGI timeline: Hassabis 2030, community 2030s, researchers 2040s — 9,800 predictions analyzed
- **ソース:** AIMultiple / AI Corner
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02, KIQ-005-01
- **関連企業:** Google, Anthropic, OpenAI
- **要約:** 9,800件のAGI予測を分析。Hassabis（DeepMind）は2030年。AI研究コミュニティ中央値は2030年代。研究者調査は2040年代。起業家はより早い時期を予測。Dario Amodei（Anthropic）は収益性タイムラインについて不確実性を表明。AGIの「System of No」概念が議論。
- **キーファクト:**
  - Hassabis: AGI 2030年
  - AI研究者予測中央値: 2030年代
  - 学術調査: 2040年代
  - 起業家: より早い予測傾向
  - Dario Amodei: AI収益性の不確実性
- **引用URL:** https://aimultiple.com/artificial-general-intelligence-singularity-timing
- **Evidence ID:** EVD-20260515-0027

### INFO-028
- **タイトル:** OpenAI expands ChatGPT Ads platform — advertising automation advances
- **ソース:** LinkedIn / Facebook
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPT Adsプラットフォームのテスト段階を終了し本格展開。広告自動化が進展。エージェントAIがショッピングに導入される一方、小売業者が利用規約を変更。従来の広告代理店戦略がビジネスの成長を妨げているとの指摘。AIによる広告中間層の排除が加速。
- **キーファクト:**
  - ChatGPT Ads: テスト終了、本格展開へ
  - エージェントAIのショッピング導入
  - AIによる広告中間層排除の加速
  - Gallagher: AI自動化で生産性向上、ROIは2年以内に
- **引用URL:** https://www.linkedin.com/posts/nikilprakashfiji_aiadvertising-chatgpt-openai-activity-7458047404370673665-5qA
- **Evidence ID:** EVD-20260515-0028

### INFO-029
- **タイトル:** Klarna reverses AI automation, rehires humans — Duolingo shifts 10% to AI-first
- **ソース:** Duperrin / CFO Leadership / Instagram
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** N/A
- **要約:** KlarnaがAI代替の方向転換、約700人を再雇用。Duolingoは労働力の10%をAI-first企業に移行。GitHub/MIT研究でAIコーディングアシスタント使用時タスク55%高速化。Cloudflareが20%削減（1100人+）。Gartner: AIが自動的に良い結果や雇用減少を導くわけではない。
- **キーファクト:**
  - Klarna: 700人をAI代替後に人間再雇用（収益Q1で15%増）
  - Duolingo: 労働力10%をAI-firstに移行
  - Cloudflare: 20%（1100人+）削減
  - GitHub/MIT: AIコーディングでタスク55%高速化
  - Gartner: AI≠自動的な成果改善
- **引用URL:** https://www.duperrin.com/english/2026/05/13/cloudflare-ai-layoffs/
- **Evidence ID:** EVD-20260515-0029

### INFO-030
- **タイトル:** 67% of entry-level dev jobs gone — Stanford warns, CS enrollment declining
- **ソース:** Medium / LinkedIn (Stanford) / VnExpress
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** N/A
- **要約:** Stanford Digital Economy Lab: プログラマー22-25歳の雇用が約20%減少。10人のジュニアが必要だった企業がAIツールを使う3人のシニアで対応。ウェブ・モバイル開発求人が2020年ピークから60%+減少。CS専攻登録者が初めて減少傾向。MLエンジニア求人は依然として増加。
- **キーファクト:**
  - 22-25歳プログラマー雇用: 約20%減少
  - 10人ジュニア→3人シニア+AI
  - ウェブ・モバイル開発求人: 2020年ピークから60%+減
  - CS専攻登録者初の減少傾向
  - MLエンジニア求人は増加
- **引用URL:** https://medium.com/codetodeploy/67-of-entry-level-developer-jobs-are-gone-1b48bd8f218b
- **Evidence ID:** EVD-20260515-0030

### INFO-031
- **タイトル:** WEF HR leaders: AI transformation reshaping work — 92% invested, 78% stalled
- **ソース:** WEF / Orgvue / Forbes
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03, KIQ-004-04
- **関連企業:** N/A
- **要約:** WEF: AI変革は技術的課題以上に人的課題。92%の組織がAI投資済みだが78%がプロジェクト停滞/失敗。52%がAI使用ポリシー策定。LinkedIn: 2030年までに70%のスキルセットが変化。スキル変化がCEO問題に昇格。リスキリング・アップスキルが急務。
- **キーファクト:**
  - WEF: AI変革は人的課題としてHR必須
  - 92%投資済み、78%停滞/失敗
  - 52%がAI使用ポリシー策定
  - LinkedIn: 2030年までに70%スキル変化
  - スキル変化がCEO問題に
- **引用URL:** https://www.weforum.org/stories/2026/05/ai-transformation-reshaping-work-hr-leaders-must-help-redesign-it/
- **Evidence ID:** EVD-20260515-0031

### INFO-032
- **タイトル:** ARC-AGI-3 benchmark: coding agents with world models get 33%+
- **ソース:** Reddit / arXiv / Bengoertzel Substack
- **公開日:** 2026-05-14
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** N/A
- **要約:** ARC Prize FoundationがARC-AGI-3をローンチし「Seed IQ」評価に対応。LLM+手続き型世界モデル+検証で33%以上のスコアを達成。実行可能Python世界モデルを維持するコーディングエージェントシステム。AI IQサイトがフロンティアモデルを人間IQ尺度で評価。ARC-AGI-2のリセット問題が浮上。
- **キーファクト:**
  - ARC-AGI-3: Seed IQ評価向け特化設計
  - LLM+世界モデル+検証で33%+ vs LLM単体トップ
  - 実行可能Python世界モデルによるコーディングエージェント評価
  - AI IQサイト: フロンティアモデルの人間IQ尺度評価
  - ARC-AGI-2リセットで過去スコアの実効性疑問視
- **引用URL:** https://www.reddit.com/r/agi/comments/1t66tsy/arc_prize_just_updated_arcagi3_specifically_to/
- **Evidence ID:** EVD-20260515-0032

### INFO-033
- **タイトル:** Pentagon will never again rely on single AI provider — 8 companies signed
- **ソース:** Nextgov / Meritalk / Instagram
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, Google, Microsoft, Palantir
- **要約:** ペンタゴンが「単一AIプロバイダー依存は二度としない」と宣言。8社とAI契約を締結しAnthropicのみ除外。Claude Mythosは既にペンタゴンで展開済み。Googleがペンタゴンと秘密AI契約。Microsoft/PalantirがGPT-4を国防・情報機関に提供。AnthropicはSCR指定で連邦政府利用禁止。
- **キーファクト:**
  - ペンタゴン: 単一AIプロバイダー依存否定
  - 8社契約、Anthropic除外
  - Claude Mythos: 既にペンタゴン展開済みの矛盾
  - Google: ペンタゴン秘密AI契約
  - Microsoft/Palantir: GPT-4を国防機関に提供
- **引用URL:** https://www.nextgov.com/artificial-intelligence/2026/05/pentagon-will-never-again-rely-single-ai-provider-official-says/413399/
- **Evidence ID:** EVD-20260515-0033

### INFO-034
- **タイトル:** AI data center: $900B opportunity, $725B hyperscaler spend, orbital compute
- **ソース:** Business Insider / Seeking Alpha / Yahoo Finance
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Microsoft, Amazon, Google, Meta
- **要約:** AIデータセンターに$9000億の第三者投資機会。Big 4ハイパースケーラーが合計$7250億をAIインフラに投資。プライベートエクイティ投資が急増。Cowboy Space Corpが$2.75億調達で軌道データセンター計画。Googleはテキサスに$400億、Stargateは$5000億AIインフラ。AIデータセンターへの反発も拡大。
- **キーファクト:**
  - サードパーティデータセンター: $9000億機会
  - Big 4: $7250億AIインフラ投資（2026年）
  - Cowboy Space Corp: $2.75億調達・軌道DC計画
  - Google: テキサス$400億、Stargate: $5000億
  - データセンター反発拡大
- **引用URL:** https://www.businessinsider.com/how-private-equity-chasing-data-center-opportunity-blackstone-ares-apollo-2026-5
- **Evidence ID:** EVD-20260515-0034

### INFO-035
- **タイトル:** DeepSeek V4: most powerful open-source model, 8 months behind frontier
- **ソース:** Analytics Vidhya / Gigazine (CAISI)
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4がオープンソース最強モデルに。CAISI分析ではフロンティアモデルより約8ヶ月遅れ。ただし同等性能モデルよりコスト効率が高い。DeepSeek V3.1は$0.27/$1.10 per 1M tokens。OSSと商用の性能ギャップは縮小中。
- **キーファクト:**
  - DeepSeek V4: オープンソース最強モデル
  - CAISI: フロンティアから約8ヶ月遅れ
  - コスト効率は同等性能モデルより高い
  - V3.1: $0.27/$1.10 per 1M tokens
  - OSS-商用ギャップ縮小中
- **引用URL:** https://www.analyticsvidhya.com/blog/2026/04/deepseek-v4/
- **Evidence ID:** EVD-20260515-0035

### INFO-036
- **タイトル:** Meta AI Agents for advertising automation — 2026 complete guide
- **ソース:** Ryze.ai / The Current
- **公開日:** 2026-05-14
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** Meta
- **要約:** Meta AIエージェントがFacebook/Instagram広告を自動化。Business AI、Advantage+、自律的クリエイティブ生成。エージェント型メディアプランニングが2026年初頭に急拡大。AdMove.aiがクリエイティブエージェンシー向けAIエージェントプラットフォームをローンチ。デジタルマーケティング全体の自律化が進行。
- **キーファクト:**
  - Meta AI Agents: Facebook/Instagram広告完全自動化
  - Business AI、Advantage+、自律クリエイティブ生成
  - エージェント型メディアプランニングが急拡大
  - AdMove.ai: クリエイティブエージェンシー向けAIエージェント
  - デジタルマーケティング自律化の進行
- **引用URL:** https://www.get-ryze.ai/blog/meta-ai-agents-for-advertising-automation
- **Evidence ID:** EVD-20260515-0036

### INFO-037
- **タイトル:** Coze (扣子) evolving into enterprise AI platform — WeChat and DingTalk integration
- **ソース:** Tencent Cloud / CSDN / Sohu
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのCoze（扣子）がエンタープライズ展開を加速。企業WeChat・DingTalkとの統合比較ガイドが登場。Coze 2.0はエージェント開発プラットフォームからスマートオフィスアシスタントプラットフォームに進化。PPT作成・動画生成機能を追加。
- **キーファクト:**
  - Coze: エージェント開発→スマートオフィスアシスタントに進化
  - 企業WeChat・DingTalkとの統合ガイド登場
  - PPT作成・動画生成機能を追加
  - Coze 2.0の企業展開加速
- **引用URL:** https://cloud.tencent.com/developer/article/2665808
- **Evidence ID:** EVD-20260515-0037

### INFO-038
- **タイトル:** Seedance 2.0 complete guide — four-modal input, world model direction
- **ソース:** Atlas Cloud / GitHub (YouMind) / Zhihu
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** Seedance 2.0の完全ガイド。業界初の四モダリティ同時入力（画像・動画・音声・テキスト）対応。真人動画モードの回帰。コストは0.35元/秒。Seedシリーズ全体がWorld Model（世界模型）方向に発展。Seed3Dで空間生成・シーン生成能力を追加。
- **キーファクト:**
  - 四モダリティ同時入力: 業界初
  - 真人動画モードの回帰
  - コスト: 0.35元/秒
  - Seed3D: 空間生成・シーン生成
  - World Model方向への発展
- **引用URL:** https://www.atlascloud.ai/zh/blog/guides/seedance-2.0-complete-guide
- **Evidence ID:** EVD-20260515-0038

### INFO-039
- **タイトル:** AI alignment research: negative to positive alignment shift — HumanityAI $18M grants
- **ソース:** arXiv / Facebook (MacArthur Foundation) / EA Forum
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** N/A
- **要約:** AIアライメント研究がネガティブ（安全性）からポジティブ（人間の繁栄）への転換を議論。HumanityAIが$1800万助成金。MATS秋季フェローシップ（$7680/月）。AIアライメント財団が独立研究者に助成。AI Safety Mapがアライメント研究の全体像を公開。
- **キーファクト:**
  - アライメント研究: ネガティブ→ポジティブ転換の議論
  - HumanityAI: $1800万助成金
  - MATS秋季フェローシップ: $7680/月
  - AI Alignment Foundation: 独立研究者向け助成
  - AI Safety Map: アライメント研究の全体像
- **引用URL:** https://arxiv.org/html/2605.10310v1
- **Evidence ID:** EVD-20260515-0039

### INFO-040
- **タイトル:** US-China AI talks: Sanders invites Chinese researchers, CFR recommends targeted dialogue
- **ソース:** CFR / POLITICO / Sanders.senate.gov
- **公開日:** 2026-05-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** N/A
- **要約:** トランプ・習近平首脳会談でのAI協議に向けた動き。CFR: 北京はAI安全性で誠実交渉しないとの見方、標的対話と最大圧力を推奨。Sanders上院議員: 超知能禁止条約への進展目指す。清華大・北大の中国人AI研究者2名が議会招聘。EUはAI Actのハイリスク規制を1年+延期。
- **キーファクト:**
  - CFR: 北京はAI安全性で誠実交渉なし→標的対話+最大圧力推奨
  - Sanders: 超知能禁止条約への進展
  - 清華大・北大研究者が議会招聘
  - EU AI Act: ハイリスク規制1年+延期
  - R Street: 中国とは「話すが署名しない」方針
- **引用URL:** https://www.cfr.org/articles/how-trump-should-approach-ai-talks-with-china-targeted-dialogue-maximum-pressure
- **Evidence ID:** EVD-20260515-0040
