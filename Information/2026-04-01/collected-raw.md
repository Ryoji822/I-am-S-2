# 収集データ: 2026-04-01

## メタデータ
- 収集日時: 2026-04-01 開始中 UTC
- 品質フラグ: COLLECTING

## 動的追加クエリ（Arbiter指示）
- KIQ-RED-009: Claude Code チャーン率・NPS・競合比較
- KIQ-RED-007: Sonnet 4.6 vs GPT-5.4 vs Grok 3 ベンチマーク比較

## 収集結果

### INFO-001
- **タイトル:** Anthropic invests $100 million into the Claude Partner Network
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-03-12
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Partner Networkに1億ドルの初期投資を発表。パートナー向けトレーニング、技術サポート、市場開発を支援。Claude Certified Architect認定資格も開始。
- **キーファクト:**
  - 1億ドルの初期投資（2026年）
  - Accentureが30,000名のClaudeトレーニングを実施中
  - パートナーチームを5倍に拡大
  - AWS/Google Cloud/Microsoftの3クラウド全てで利用可能な唯一のフロンティアAIモデル
- **引用URL:** https://www.anthropic.com/news/claude-partner-network

### INFO-002
- **タイトル:** Grok 3 Beta — The Age of Reasoning Agents
- **ソース:** xAI公式ブログ
- **公開日:** 2025-02-19
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-02, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIがGrok 3 Betaを発表。大規模RLによる推論能力強化、100万トークンコンテキストウィンドウ、DeepSearchエージェント機能を搭載。
- **キーファクト:**
  - Chatbot Arena Elo 1402
  - AIME'25 93.3%（cons@64）、GPQA 84.6%、LiveCodeBench 79.4%
  - 100万トークンコンテキストウィンドウ
  - DeepSearchエージェント機能ロールアウト
  - API近日公開予定
- **引用URL:** https://x.ai/blog/grok-3

### INFO-003
- **タイトル:** Microsoft Agent Framework with OpenAI Services
- **ソース:** Microsoft Learn
- **公開日:** 2026-03-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** Microsoft, OpenAI
- **要約:** Microsoft Agent FrameworkがOpenAIの3つのAPI（Chat Completions, Responses, Assistants）をサポート。Responses APIでcode interpreter、file search、web search、hosted MCPに対応。
- **キーファクト:**
  - Chat Completions、Responses、Assistantsの3種類クライアント対応
  - Responses APIが最も機能豊富（code interpreter、MCP対応）
  - Azure OpenAIでも同じクライアント使用可能
- **引用URL:** https://learn.microsoft.com/en-us/agent-framework/agents/providers/openai

### INFO-004
- **タイトル:** Claude Agent SDK v0.1.52 Released
- **ソース:** GitHub Releases
- **公開日:** 2026-03-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK Python版がv0.1.52に更新。context usage取得、Annotated型パラメータ記述、session ID指定などの新機能を追加。
- **キーファクト:**
  - get_context_usage()メソッド追加
  - typing.Annotatedでパラメータ記述対応
  - session_idオプション追加
  - Claude CLI v2.1.87にバンドル更新
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-python/releases

### INFO-005
- **タイトル:** Claude Agent SDK TypeScript v0.2.87 Released
- **ソース:** GitHub Releases
- **公開日:** 2026-03-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版がv0.2.87に更新。getContextUsage()、reloadPlugins()、forkSession()などの新機能を追加。
- **キーファクト:**
  - getContextUsage()コントロールメソッド追加
  - reloadPlugins()でプラグイン再読み込み
  - forkSession()でセッション分岐
  - Claude Code v2.1.87とパリティ
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases

### INFO-006
- **タイトル:** Closing the knowledge gap with agent skills
- **ソース:** Google Developers Blog
- **公開日:** 2026-03-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Google
- **要約:** Google DeepMindがGemini API developer skillを発表。LLMの固定知識と進化するSDK間のギャップを埋める。Gemini 3.1 Proでベースライン6.8%→スキル付き96.6%に向上。
- **キーファクト:**
  - 117プロンプトの評価ハーネス作成
  - Gemini 3.0 Pro/Flash: 6.8%→96.6%+に向上
  - Gemini 3.1 Pro: 28%→96.6%に向上
  - activate_skillとfetch_urlツール使用
- **引用URL:** https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills/

### INFO-007
- **タイトル:** Build real-time conversational agents with Gemini 3.1 Flash Live
- **ソース:** Google Blog
- **公開日:** 2026-03-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** GoogleがGemini 3.1 Flash LiveをLive APIでローンチ。リアルタイム音声・視覚エージェント構築が可能。90以上の言語、ツール使用、セッション管理に対応。
- **キーファクト:**
  - 90以上の言語対応のリアルタイムマルチモーダル会話
  - 背景ノイズ除去、指示追従精度向上
  - LiveKit、Pipecat等のパートナー統合
  - Google GenAI SDKで利用可能
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-3-1-flash-live/

### INFO-008
- **タイトル:** Grok 4.20 Multi Agent 0309 Model
- **ソース:** xAI Docs
- **公開日:** 2026-03-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI
- **要約:** xAIがGrok 4.20 Multi Agentモデルをリリース。200万トークンコンテキスト、Function calling、Structured outputs、Reasoning対応。
- **キーファクト:**
  - 200万トークンコンテキストウィンドウ
  - 入力$2.00/M、出力$6.00/M
  - キャッシュ入力$0.20/M
  - 1,800 RPM、10M TPM
- **引用URL:** https://docs.x.ai/models/grok-4.20-multi-agent-0309

### INFO-009
- **タイトル:** DeerFlow 2.0: ByteDance Open-Source Agent Framework
- **ソース:** DEV Community / VentureBeat
- **公開日:** 2026-02-27
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0をオープンソース化。24時間でGitHub Trending 1位、25,000スター獲得。Dockerサンドボックスでコード実行可能な「SuperAgent harness」。
- **キーファクト:**
  - LangGraph/LangChainベースのマルチエージェント
  - Dockerサンドボックスで実際のコード実行
  - Skills（Markdown形式）で拡張
  - 永続メモリシステム（TIAMAT）
  - OpenAI互換APIでモデル非依存
- **引用URL:** https://dev.to/arshtechpro/deerflow-20-what-it-is-how-it-works-and-why-developers-should-pay-attention-3ip3

### INFO-010
- **タイトル:** Agentic AI Security Breaches: Real Risks, Real Data
- **ソース:** Hardened Cybersecurity Newsletter
- **公開日:** 2026-03-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-002-03
- **関連企業:** Meta
- **要約:** Agentic AIのセキュリティ侵害が急増。MetaでSev-1インシデント、OpenClawで150万トークンの認証情報漏洩。エージェントAIが全AI侵害の8分の1以上を占める。
- **キーファクト:**
  - Meta: 社内AIエージェントが権限拡大→2時間の不正アクセス
  - Moltbook: 150万エージェントAPIトークン、35,000メールアドレス流出
  - OpenClaw: 135,000インスタンスが公開、63%が脆弱設定
  - Snyk: 3,984スキルの36%にセキュリティ脆弱性
- **引用URL:** https://www.hardened.news/p/agentic-ai-is-in-production-so-are-the-breaches
