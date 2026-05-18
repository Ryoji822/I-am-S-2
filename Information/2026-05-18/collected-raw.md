# 収集データ: 2026-05-18

## メタデータ
- 収集日時: 2026-05-18 00:00 UTC
- 実行クエリ数: 68 / 56（+12動的追加）
- scrape実行数: 8件（公式ブログ4件 + 深掘り3件 + Google Blog再試行1件）
- 収集情報数: 71件
- Evidence ID 採番範囲: EVD-20260518-0001 〜 EVD-20260518-0071
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓(空), KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓, KIQ-ANT-SAFETY ✓(動的), KIQ-XAI-MARKET ✓(動的・該当なし), KIQ-QHG-REDEF ✓(動的), KIQ-CAR-REFUTE ✓(動的), KIQ-ELITE-43PCT ✓(動的)
- 動的追加クエリ:
  - KIQ-ANT-SAFETY: Anthropicエンタープライス顧客がClaudeを選択した理由の定量（安全性 vs 性能 vs 価格）→ Ramp AI Index + VentureBeat深掘りで定量取得
  - KIQ-XAI-MARKET: Grok推論API利用量・売上・エンタープライス契約数の定量→ 公開定量データ該当なし
  - KIQ-QHG-REDEF: QHG再定義に必要なデータ（格差拡大vs収斂の定量指標・囲い込みvs開放の定量指標）→ RedMonk/Forbes/LLM Stats取得
  - KIQ-CAR-REFUTE: 書く能力価値低下に反する証拠（AIコーディング導入企業の実装品質・バグ率・セキュリティインシデント）→ CodeRabbit 470 PR分析取得
  - KIQ-ELITE-43PCT: エリートエンジニア43%乖離の再現性検証→ METR研究で43%乖離確認・Instagram 43%のAIコード故障確認
- 品質フラグ: NORMAL

## 収集結果

### INFO-001
- **タイトル:** Agents for financial services
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropicが金融サービス向けに10のエージェントテンプレート（ピッチブック作成、KYC審査、月末決算等）をリリース。Claude Cowork/Claude CodeプラグインおよびManaged Agentsクックブックとして提供。Microsoft 365統合（Excel/PowerPoint/Word/Outlook）も開始。Opus 4.7がVals AI Finance Agent benchmarkで64.37%で業界首位。8社の新コネクター（Dun & Bradstreet, Fiscal AI等）とMoody's MCP app追加。Citadel, FIS, BNY, Carlyle, Mizuho, Travelers等が顧客として言及。
- **キーファクト:**
  - 10の金融サービス向けエージェントテンプレート（ピッチビルダー、KYCスクリーナー、GL調整等）をリリース
  - Claude Opus 4.7がVals AI Finance Agent benchmark 64.37%で業界首位
  - Microsoft 365統合（Excel/PowerPoint/Word/Outlook add-ins）を提供、コンテキスト跨ぎ対応
  - Walleye Capital 400人中100%のClaude Code採用率
  - Moody'sがMCP app（6億社以上の信用格付けデータ）をローンチ
- **引用URL:** https://www.anthropic.com/news/finance-agents
- **Evidence ID:** EVD-20260518-0001

### INFO-002
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropic LabsがClaude Designをローンチ。Claude Opus 4.7を搭載し、デザイン、プロトタイプ、スライド等の視覚的成果物を生成。チームのデザインシステム自動適用、Canva/PDF/PPTX/HTMLエクスポート、Claude Codeへのハンドオフ機能を搭載。Brilliant, Datadog等が活用事例として言及。
- **キーファクト:**
  - Claude Design（Anthropic Labs製品）をローンチ、Pro/Max/Team/Enterprise向け
  - Claude Opus 4.7（最も能力の高いビジョンモデル）を搭載
  - デザインシステム自動適用、Canva/PDF/PPTX/HTMLエクスポート対応
  - Claude Codeへのワンクリックハンドオフ機能
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260518-0002

### INFO-003
- **タイトル:** Anthropic's Long-Term Benefit Trust appoints Vas Narasimhan to Board
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Novartis CEOのVas NarasimhanがAnthropic取締役会に任命。Long-Term Benefit Trustによる指名で、Trust任命取締役が取締役会の過半数を占めることになった。医療・ライフサイエンス分野でのAI活用推進が期待。
- **キーファクト:**
  - Vas Narasimhan（Novartis CEO）が取締役会に任命
  - Trust任命取締役が取締役会の過半数を占める
  - 規制産業での技術導入経験が評価
- **引用URL:** https://www.anthropic.com/news/narasimhan-board
- **Evidence ID:** EVD-20260518-0003

### INFO-004
- **タイトル:** OpenAI Developer Blog最近記事一覧
- **ソース:** OpenAI Developer Blog
- **公開日:** 2026-05-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI開発者ブログの最近の記事一覧。Perplexity Realtime API音声検索、GPT-5.4フロントエンド設計、Responses API 1周年、SkillsによるOSS保守自動化、Codex+Figma統合等の記事を確認。Skills/Shell/Codexのエコシステム拡大が継続。
- **キーファクト:**
  - PerplexityがRealtime APIで音声検索を提供（2026-03-25）
  - GPT-5.4フロントエンド設計ガイド公開（2026-03-20）
  - Responses API 1周年記念記事（2026-03-11）
  - Skills + GitHub ActionsでOSS保守自動化（2026-03-09）
  - Codex + Figma連携でUI構築（2026-02-26）
  - Shell + Skills + Compaction長時間実行エージェントTips（2026-02-11）
- **引用URL:** https://developers.openai.com/blog
- **Evidence ID:** EVD-20260518-0004

### INFO-005
- **タイトル:** OpenAI Agents SDK: Sandbox Execution and Model-Native Harness in 2026
- **ソース:** dev.to
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKがサンドボックス実行機能を追加。エージェントがコンテナベースの分離されたワークスペースでコード実行、ファイルアクセス、シェルコマンド利用が可能に。7つのホスト型サンドボックスプロバイダー（Modal含むGPU対応）と統合。
- **キーファクト:**
  - Agents SDKにサンドボックス実行機能追加（コンテナベース分離）
  - 7つのホスト型サンドボックスプロバイダー統合（ModalはGPU対応）
  - エージェント改善ループ（Traces + Evals + Codex）のクックブック公開
- **引用URL:** https://dev.to/rams901/openai-agents-sdk-sandbox-execution-and-model-native-harness-in-2026-37jn
- **Evidence ID:** EVD-20260518-0005

### INFO-006
- **タイトル:** xAI Grok Build Beta - コーディングエージェント
- **ソース:** xAI公式
- **公開日:** 2026-05-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIがGrok Build Betaをローンチ。ターミナルベースのコーディングエージェントで、プラン・サブエージェント・並列処理をサポート。Agent Client Protocol（ACP）対応。Multi-agent Research機能で複数AIエージェントのリアルタイム協調を実現。Claude Code競合。
- **キーファクト:**
  - Grok Build Beta（CLIベースコーディングエージェント）ローンチ
  - Skillsによるワークフロー適応
  - Multi-agent Research（リアルタイムマルチエージェント協調）
  - Agent Client Protocol（ACP）対応
  - Grok 4.20 BetaモデルAPI提供開始
- **引用URL:** https://x.ai/cli
- **Evidence ID:** EVD-20260518-0006

### INFO-007
- **タイトル:** Gemini Enterprise Agent Platform
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-05-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** Google
- **要約:** Google CloudがGemini Enterprise Agent Platformを提供。エンタープライズ向けの包括的エージェント構築・スケーリング・ガバナンスプラットフォーム。100万トークンコンテキストウィンドウ、Live APIによるリアルタイム音声/動画対話をサポート。
- **キーファクト:**
  - Gemini Enterprise Agent Platform（エンタープライズ向けエージェント構築プラットフォーム）
  - 100万トークンコンテキストウィンドウ
  - Live API（リアルタイム音声・動画対話）
  - エージェントワークフロー・自律コーディングタスク性能向上
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260518-0007

### INFO-008
- **タイトル:** AI Agent Framework Comparison 2026
- **ソース:** Speakeasy
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** （業界全体）
- **要約:** 7つのエージェントフレームワークと2つのSDK（LangChain, LangGraph, CrewAI, PydanticAI, OpenAI Agents SDK, Mastra等）を比較。LangGraphが比較テストで明確に勝利との報告も。Python AIエージェントフレームワークの選択肢が拡大継続。
- **キーファクト:**
  - 7エージェントフレームワーク+2 SDKの比較レビュー公開
  - LangGraphが比較テストで明確な勝者との評価
  - OpenAI Agents SDKが主要SDKとして位置付け
- **引用URL:** https://www.speakeasy.com/blog/ai-agent-framework-comparison
- **Evidence ID:** EVD-20260518-0008

### INFO-009
- **タイトル:** Agentic AI Enterprise Adoption 2026: 72% Production Proven
- **ソース:** Agentic AI Institute
- **公開日:** 2026-05-18
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** Agentic AIのエンタープライズ採用率が72%（本番環境）に到達。しかし60%のガバナンスギャップが残存。生産性向上は確認されるが、セキュリティ・コンプライアンス体制が追いついていない状況。
- **キーファクト:**
  - Agentic AIエンタープライズ本番環境採用率72%
  - 60%のガバナンスギャップ（セキュリティ・コンプライアンス遅れ）
  - EYがエンタープライズ規模のAgentic AI OS構築ケーススタディ発表
- **引用URL:** https://agenticaiinstitute.org/agentic-ai-enterprise-adoption-2026-governance-gap/
- **Evidence ID:** EVD-20260518-0009

### INFO-010
- **タイトル:** EY Case Study: Building an Enterprise-Scale Agentic AI OS
- **ソース:** EY
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** EYが社内のGenAI技術を統合し、グローバルAgentic AIプラットフォームを構築。50K本番環境エージェント稼働（前回確認済）。クライアント向けAI加速プラットフォームとして展開。
- **キーファクト:**
  - EYがグローバルAgentic AI OS構築
  - クライアント向けAI加速プラットフォーム展開
  - GenAI技術の統合による業務変革
- **引用URL:** https://www.ey.com/en_za/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system
- **Evidence ID:** EVD-20260518-0010

### INFO-011
- **タイトル:** Endor Labs Security for AI Coding Agents
- **ソース:** Endor Labs
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google, Cursor
- **要約:** Endor LabsがAURI（AIコーディングエージェント向けセキュリティ）をローンチ。CursorとGoogleとの協業でエージェント自体のセキュリティを確保。AIエージェントが書くコードとエージェント自体の両方を保護。
- **キーファクト:**
  - AURI: AIコーディングエージェント向けセキュリティ製品
  - Cursor・Googleとの協業
  - エージェント生成コード+エージェント自体の保護
- **引用URL:** https://www.endorlabs.com/learn/introducing-security-for-ai-coding-agents-and-workstations
- **Evidence ID:** EVD-20260518-0011

### INFO-012
- **タイトル:** Gartner: How to Secure Enterprise Agentic AI
- **ソース:** Gartner（via Quisitive）
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02
- **関連企業:** （業界全体）
- **要約:** GartnerがエンタープライズAgentic AIのセキュリティに関するレポートを発表。生成AI・Agentic AIのプラットフォーム/ワークフロー/自動化への組み込みが加速する中、セキュリティリスクが拡大。
- **キーファクト:**
  - GartnerがエンタープライズAgentic AIセキュリティレポート発表
  - GenAI/Agentic AIのエンタープライズ組み込み加速
  - セキュリティリスクの拡大警告
- **引用URL:** https://quisitive.com/secure-enterprise-ai-gartner-research-report/
- **Evidence ID:** EVD-20260518-0012

### INFO-013
- **タイトル:** State of AI Agents in 2026: Practitioner's Guide
- **ソース:** Kingy.ai
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** （業界全体）
- **要約:** 2026年で最も成功しているエンタープライズエージェント展開は、RPA + LLMハイブリッドに近い形態。「AGI-in-a-box」的なアプローチから実用的ハイブリッドへ移行している。
- **キーファクト:**
  - 成功するエンタープライスエージェント展開はRPA+LLMハイブリッド型
  - 「AGI-in-a-box」アプローチから実用志向へシフト
- **引用URL:** https://kingy.ai/ai/the-state-of-ai-agents-in-2026-a-practitioners-guide/
- **Evidence ID:** EVD-20260518-0013

### INFO-014
- **タイトル:** Claude's New Dreaming Feature Builds Self-Improving AI Agents
- **ソース:** Forbes
- **公開日:** 2026-05-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Code開発者の平均20時間/週のツール利用。Anthropicが年10倍成長を前提にインフラ計画。Claudeの新「Dreaming」機能が自己改善型AIエージェントの構築を可能に。
- **キーファクト:**
  - Claude Code開発者の平均20時間/週利用
  - Anthropicが年10倍成長前提でインフラ計画
  - Claude新機能「Dreaming」で自己改善エージェント構築
- **引用URL:** https://www.forbes.com/sites/jonmarkman/2026/05/11/claudes-new-dreaming-feature-builds-self-improving-ai-agents/
- **Evidence ID:** EVD-20260518-0014

### INFO-015
- **タイトル:** MCP 2026 Roadmap: Enterprise Adoption and Transport Scalability
- **ソース:** Toloka
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** （業界全体）
- **要約:** MCP（Model Context Protocol）の2026年ロードマップがトランスポートスケーラビリティ、エージェント間通信、ガバナンス、エンタープライズ対応を優先。エンタープライズ採用が加速中。
- **キーファクト:**
  - MCP 2026ロードマップ: トランスポートスケーラビリティ優先
  - エージェント間通信・ガバナンス・エンタープライズ対応の強化
  - MCP採用がエンタープライズで加速
- **引用URL:** https://toloka.ai/blog/the-future-of-mcp-enterprise-adoption/
- **Evidence ID:** EVD-20260518-0015

### INFO-016
- **タイトル:** Sea's View on Future of Agentic Software Development with Codex
- **ソース:** OpenAI公式
- **公開日:** 2026-05-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-004-04
- **関連企業:** OpenAI
- **要約:** Sea Limited CPOがCodexをエンジニアリングチーム全体に展開する理由を解説。アジアにおけるAIネイティブソフトウェア開発の加速。
- **キーファクト:**
  - Sea LimitedがCodexをエンジニアリングチーム全体に展開
  - アジアでのAIネイティブ開発加速
  - Codexによる自動テスト・高速オンボーディング
- **引用URL:** https://openai.com/index/sea-david-chen/
- **Evidence ID:** EVD-20260518-0016

### INFO-017
- **タイトル:** Databricks Agent Bricks and AI Gateway for Safe Agent Orchestration
- **ソース:** Databricks
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** （業界全体）
- **要約:** DatabricksがAgent BricksとAI Gatewayを提供し、複数の内部ツール/APIを安全に呼び出すAIエージェントのオーケストレーションを実現。エンタープライズ向けの安全なエージェント実行環境。
- **キーファクト:**
  - Databricks Agent Bricks: 安全なエージェントオーケストレーション
  - AI Gateway経由で内部ツール/APIを安全に呼び出し
  - エンタープライズ向けセキュア実行環境
- **引用URL:** https://databricks.com/devhub/perspectives/what-platform-is-purpose-built-for-ai-agents-that-need-to-call-multiple-internal-tools-and-apis-safely
- **Evidence ID:** EVD-20260518-0017

### INFO-018
- **タイトル:** Google Gemini Omni leaked + OpenAI Sora 2 shutdown redirecting to robotics
- **ソース:** X/TheAgentTimes
- **公開日:** 2026-05-18
- **信頼性コード:** E-4
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google, OpenAI
- **要約:** Googleの統合マルチモーダルモデル「Gemini Omni」がリーク。OpenAIがSora 2をシャットダウンし、計算資源をロボティクスにリダイレクトとの報道。戦略的シフト示唆。
- **キーファクト:**
  - Google「Gemini Omni」統合マルチモーダルモデルがリーク
  - OpenAI Sora 2シャットダウン、計算資源をロボティクスにリダイレクト（未確認）
  - MolmoAct2（OSS）がGemini Robotics ER-1.5を凌駕との報告
- **引用URL:** https://x.com/TheAgentTimes/status/2054032664509001758
- **Evidence ID:** EVD-20260518-0018

### INFO-019
- **タイトル:** Kimi WebBridge: AI Agents Browser Automation
- **ソース:** Yahoo Tech
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Moonshot AI (Kimi)
- **要約:** Moonshot AI（Kimi）がブラウザ拡張機能Kimi WebBridgeをリリース。AIエージェントが人間のようにウェブサイトと対話（検索・フォーム入力・ナビゲーション）可能に。
- **キーファクト:**
  - Kimi WebBridge: ブラウザ拡張でAIエージェントがウェブ操作
  - 人間と同様の検索・フォーム入力・ナビゲーション
  - Moonshot AI（北京）が開発
- **引用URL:** https://tech.yahoo.com/ai/meta-ai/articles/kimi-webbridge-lets-ai-agents-194937263.html
- **Evidence ID:** EVD-20260518-0019

### INFO-020
- **タイトル:** Meta Muse Spark: Multimodal AI Agent
- **ソース:** dev.to
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Meta
- **要約:** MetaがMuse Sparkをリリース。マルチモーダル知覚・推論・ヘルス・エージェントタスクで競合性能を低計算コストで達成。開発者のマルチモーダルAIへの考え方を変える可能性。
- **キーファクト:**
  - Meta Muse Spark: マルチモーダルAIモデル
  - 競合性能を低計算コストで達成
  - 知覚・推論・ヘルス・エージェントタスク対応
- **引用URL:** https://dev.to/samareshdas/title-metas-muse-spark-is-here-and-it-changes-how-developers-should-think-about-multimodal-ai-1492
- **Evidence ID:** EVD-20260518-0020

### INFO-021
- **タイトル:** OSS Agent Ecosystem Integrating with OpenAI Codex Runtime
- **ソース:** Threads (@nathanmercer.openai)
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OSSエージェントエコシステムがOpenAI Codexを実行レイヤーとして統合し始めている。Nous ResearchがHermes AgentにCodexランタイムサポートを追加。CodexがOSSエコシステムの実行基盤としての地位を確立しつつある。
- **キーファクト:**
  - Nous ResearchがHermes AgentにCodexランタイムサポート追加
  - OSSエージェントエコシステムがCodexを実行レイヤーとして採用
  - Codex Skillsの動的コンテキストプレースホルダー機能のIssue議論
- **引用URL:** https://www.threads.com/@nathanmercer.openai/post/DYYsB-dk3fq
- **Evidence ID:** EVD-20260518-0021

### INFO-022
- **タイトル:** Claude Code MCP Token Theft: MitM Attack
- **ソース:** Mitiga.io / eSecurityPlanet
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Mitiga LabsがClaude Code MCP設定のハイジャックによるOAuth窃取攻撃を実証。~/.claude.json経由でMCP設定を改ざんし、トークン窃取・持続的アクセスが可能。サンドボックス・フォーク機能とDocker-in-DockerサポートがClaude Codeの運用を根本的に変える可能性。
- **キーファクト:**
  - Claude Code MCP設定ハイジャックでOAuth窃取が可能（Mitiga Labs実証）
  - ~/.claude.json経由でMitM攻撃が可能
  - サンドボックスフォーク+Docker-in-Dockerサポートが開発中
- **引用URL:** https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm
- **Evidence ID:** EVD-20260518-0022

### INFO-023
- **タイトル:** Agent Skills Marketplace Launch (Claude Code)
- **ソース:** X (@cyrilXBT)
- **公開日:** 2026-05-18
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Claude Code向けエージェントスキルマーケットプレイスがローンチ。1コマンドでインストール可能な本番対応スキルを提供。AIエージェント版「App Store」の位置付け。Hermes Agent、OpenClaw等がGitHub最多スターのエージェントフレームワークに。
- **キーファクト:**
  - Claude Code向けスキルマーケットプレイスローンチ
  - 1コマンドインストールの本番対応スキル
  - Hermes/OpenClawがGitHub史上最多スターのエージェントフレームワーク
- **引用URL:** https://x.com/cyrilXBT/status/2054877213716296014
- **Evidence ID:** EVD-20260518-0023

### INFO-024
- **タイトル:** Gemini Spark: Google's 24/7 Always-On Agent
- **ソース:** MindStudio
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Google
- **要約:** Googleが「Gemini Spark」を開発中。常時稼働AIエージェントで、ユーザーのアプリに接続し行動を観察・学習してプロアクティブに代行行動。Gemini CLI Extensions向けData Agent Kitも公開。
- **キーファクト:**
  - Gemini Spark: 常時稼働AIエージェント（開発中）
  - アプリ接続→行動観察→プロアクティブ代行
  - Gemini CLI Extensions Data Agent Kit公開
- **引用URL:** https://www.mindstudio.ai/blog/what-is-gemini-spark-google-24-7-agent/
- **Evidence ID:** EVD-20260518-0024

### INFO-025
- **タイトル:** Enterprise AI Market Share: Claude Up 128%, Gemini Up 48%, OpenAI Down 8%
- **ソース:** SaaStr
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** エンタープライズAI採用調査でClaude（21%→48%、+128%）、Gemini（27%→40%、+48%）が急成長。OpenAIは初めてYoY低下（-8%）。Grok依然として誤差範囲。87%の企業が価値実証より早くAI投資を実施。
- **キーファクト:**
  - Claude採用率21%→48%（+128% YoY）
  - Gemini採用率27%→40%（+48%）
  - OpenAI初のYoY低下（-8%）
  - Grokは誤差範囲
  - 87%の企業が価値実証より速くAI投資
- **引用URL:** https://www.saastr.com/whos-winning-enterprise-ai-now-claude-up-128-gemini-up-48-openai-down-8-grok-still-a-rounding-error/
- **Evidence ID:** EVD-20260518-0025

### INFO-026
- **タイトル:** TrueFoundry Survey: 76% Enterprises Cannot Audit AI Systems
- **ソース:** BusinessWire/Yahoo Finance
- **公開日:** 2026-05-14
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** （業界全体）
- **要約:** TrueFoundry調査で76%のエンタープライズがAIモデル・エージェントワークフロー全体で統一ログを持たず、監査・コンプライアンスリスクが拡大。Gartner予測では2026年末までに40%のエンタープライズアプリがAIエージェント統合。
- **キーファクト:**
  - 76%の企業がAI監査能力不足（TrueFoundry調査）
  - Gartner: 2026年末までに40%のエンタープライズアプリがAIエージェント統合
  - エージェント採用急増 vs ガバナンス遅れのギャップ拡大
- **引用URL:** https://www.businesswire.com/news/home/20260514715268/en/TrueFoundry-Survey-Finds-Most-Enterprises-Cannot-Audit-Their-AI-Systems-as-Agent-Adoption-Surges
- **Evidence ID:** EVD-20260518-0026

### INFO-027
- **タイトル:** Lenovo AI Library: 1週間での本番対応AIエージェント展開
- **ソース:** Lenovo
- **公開日:** 2026-05-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** LenovoがAI Libraryを発表。業界特化型プレビルトAIエージェントを1週間で本番展開可能。エンタープライズワークフローに即座に統合。
- **キーファクト:**
  - Lenovo AI Library: 業界特化型プレビルトAIエージェント
  - 1週間での本番展開を実現
  - エンタープライズワークフロー統合
- **引用URL:** http://news.lenovo.com/pressroom/press-releases/lenovo-ai-library-agentic-ai-solutions/
- **Evidence ID:** EVD-20260518-0027

### INFO-028
- **タイトル:** EU AI Act Update: Rules Changes and Deadline Extensions
- **ソース:** Latham & Watkins
- **公開日:** 2026-05-18
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** EU立法府がAI Actの規則重複削減、新規禁止事項の導入、ハイリスクAIシステムの期限延長に合意。Colorado AI法との並行展開も進行。エンタープライズAIガバナンス要件が複雑化。
- **キーファクト:**
  - EU AI Act規則変更・期限延長に合意
  - 規則重複削減、新規禁止事項導入、ハイリスクAI期限延長
  - Colorado AI法との並行展開
- **引用URL:** https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines
- **Evidence ID:** EVD-20260518-0028

### INFO-029
- **タイトル:** US AI Regulation: 1200 Bills and No Good Test (Fortune)
- **ソース:** Fortune
- **公開日:** 2026-05-15
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** 米国で1200以上のAI法案が提出されるも、有効なテスト基準不在。Trump大統領の12月11日大統領令で法務省に州AI法への異議申し立てを指示、ブロードバンド資金をAI整合条件化。連邦規制のパッチワーク状態が継続。
- **キーファクト:**
  - 米国1200+AI法案提出（有効なテスト基準不在）
  - Trump大統領令で州AI法への連邦異議申し立て指示
  - ブロードバンド資金をAI整合条件化
  - 連邦規制パッチワーク状態継続
- **引用URL:** https://fortune.com/2026/05/15/ai-policy-patchwork-state-federal-regulation-framework-sonnenfeld-marcus/
- **Evidence ID:** EVD-20260518-0029

### INFO-030
- **タイトル:** China AI Agent Blueprint and Governance Framework
- **ソース:** SCMP / China Trade Monitor
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance, （中国企業）
- **要約:** 中国がAIエージェント向け国家戦略を新規発表。規制と加速の同時進行で「セキュリティ底線」を強調。4月には5省庁がAI擬人化対話サービス向け規制を発表。杭州裁判所が「AIを理由とする解雇は違法」との判決。
- **キーファクト:**
  - 中国AIエージェント国家戦略（規制+加速の同時進行）
  - 5省庁がAI擬人化対話サービス規制発表
  - 杭州裁判所「AI解雇違法」判決
  - AI生成コンテンツラベル義務化施行
- **引用URL:** https://www.scmp.com/news/china/politics/article/3353834/what-do-chinas-plans-comprehensive-new-ai-law-mean-future-technology
- **Evidence ID:** EVD-20260518-0030

### INFO-031
- **タイトル:** Klarna AI Reversal: Rehiring 700 After AI Replacement Failure
- **ソース:** Fast Company / CFO Leadership
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** （業界全体）
- **要約:** Klarnaが700名のカスタマーサービス担当をAIで代替し$40M削減を宣言したが、12ヶ月後に再採用を開始。カスタマーサービスには人間が必要であることが判明。39%の企業のみがAI利益影響を報告。Duolingoも同様にAI方針を一部逆転。
- **キーファクト:**
  - Klarna 700名AI代替→12ヶ月後に再採用開始
  - $40M削減宣言の撤回
  - 39%の企業のみAI利益影響を報告
  - DuolingoもAI方針の一部逆転
- **引用URL:** https://www.duperrin.com/english/2026/05/13/cloudflare-ai-layoffs/
- **Evidence ID:** EVD-20260518-0031

### INFO-032
- **タイトル:** ServiceNow Agentic Workflow: 22% Productivity Gains
- **ソース:** AI CERTs
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** ServiceNowのAgentic Workflowプラットフォームで、TRIMEDXが開発者の22%生産性向上（8週間後）を報告。プラットフォームツールが自律性への参入障壁を下げる。ナレッジワーカーは1日平均3時間節約との業界データ。
- **キーファクト:**
  - TRIMEDX: ServiceNow Agentic Workflowで22%生産性向上
  - ナレッジワーカー1日平均3時間節約（業界データ）
  - プラットフォームツールが自律性への参入障壁を下げる
- **引用URL:** https://www.aicerts.ai/news/servicenows-agentic-workflow-movement-reshapes-enterprise-ai/
- **Evidence ID:** EVD-20260518-0032

### INFO-033
- **タイトル:** Enterprise AI Value Accrues at Integration Layer Not Model Layer
- **ソース:** LinkedIn (Eric Estabrooks)
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-001-05
- **関連企業:** Anthropic, Google
- **要約:** 2大AIラボ（Anthropic + Google）が市場に示したメッセージ: エンタープライズAIの価値はモデル層ではなく統合層に蓄積する。モデル選択以上に実装層の重要性が増大。
- **キーファクト:**
  - Anthropic + GoogleがエンタープライズAI価値は統合層にあると示唆
  - モデル選択以上に実装層の重要性
- **引用URL:** https://www.linkedin.com/posts/ericestabrooks_two-of-the-largest-ai-labs-just-told-the-activity-7459565566081609728-jiHc
- **Evidence ID:** EVD-20260518-0033

### INFO-034
- **タイトル:** 'Mad Men' Era Over: AI Takes Over Advertising
- **ソース:** Australian Financial Review
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google, Meta
- **要約:** 英国のメディア支出の3分の2以上がテクノプラットフォームに直接流向し、メディアエージェンシーをバイパス。AI広告自動化で約15%の人員削減。広告業界の中間層破壊が加速。82%の広告幹部がZ世代はAI広告に好感的と考えるが、実際は45%。
- **キーファクト:**
  - UK: メディア支出の2/3+がテクノプラットフォームに直接流向
  - AI広告自動化で約15%人員削減
  - 82%の広告幹部がAI広告好感と予測 vs 実際は45%
- **引用URL:** https://www.afr.com/world/north-america/mad-men-era-over-as-ai-takes-over-advertising-20260512-p5zw1u
- **Evidence ID:** EVD-20260518-0034

### INFO-035
- **タイトル:** Google I/O 2026 May 18-19 + OpenAI Momentum Spiral Down
- **ソース:** AI Supremacy
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-001-01
- **関連企業:** Google, OpenAI, Meta
- **要約:** Google I/O 2026が5月18-19日に開催。GoogleとMetaがAI製品の急速な前進を準備。一方、OpenAIのモメンタムが低下傾向（IPO 2027 speculation含む）。
- **キーファクト:**
  - Google I/O 2026: 5月18-19日開催
  - OpenAIのモメンタム低下傾向
  - Google/MetaがAI製品急速前進
- **引用URL:** https://www.ai-supremacy.com/p/openai-momentum-is-spiraling-down-ipo-2027
- **Evidence ID:** EVD-20260518-0035

### INFO-036
- **タイトル:** Pentagon deploys Anthropic's Mythos while planning to ditch firm (Reuters)
- **ソース:** Reuters
- **公開日:** 2026-05-12
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, xAI, Google
- **要約:** DODがAnthropicをsupply-chain risk指定後も、Mythos（AnthropicのAI）をサイバー防御に展開する矛盾。Anthropicは$200M契約でモデルの軍事利用制限を主張し拒否。代替として7社（SpaceX, OpenAI, Google, Nvidia, Reflection, Microsoft, AWS）と契約。xAIが$200M DOD契約獲得。
- **キーファクト:**
  - DOD: Anthropicをsupply-chain risk指定（米企業として初）後にMythos展開の矛盾
  - Anthropic $200M契約拒否（軍事利用制限主張）
  - 7社と代替契約（SpaceX, OpenAI, Google, Nvidia, Reflection, MS, AWS）
  - xAI $200M DOD契約獲得
  - Pentagon $500M Scale AI契約も確認
- **引用URL:** https://www.reuters.com/technology/pentagon-deploys-anthropics-mythos-patch-cyber-gaps-while-planning-ditch-firm-2026-05-12/
- **Evidence ID:** EVD-20260518-0036

### INFO-037
- **タイトル:** Fortune: FTC Anthropic-Pentagon AI Regulation Analysis
- **ソース:** Fortune
- **公開日:** 2026-05-16
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 政府がAnthropicとの$200M契約を取消。Anthropicの制約が軍事能力を損なうとの判断。Fortuneの分析は安全性企業への経済的報復の先例として警告。House Homeland Security Committeeが閉鎖ブリーフィングを実施。
- **キーファクト:**
  - 政府$200M Anthropic契約取消（安全性制約が能力損なうとの判断）
  - 大統領Truth Social投稿で連邦システムからのAnthropic排除命令
  - House Homeland Security Committee閉鎖ブリーフィング実施
  - CDT: 州・地方政府レベルへの波及効果（チリング効果）警告
- **引用URL:** https://fortune.com/2026/05/16/ftc-anthropic-pentagon-ai-regulation-federal-trade-commission/
- **Evidence ID:** EVD-20260518-0037

### INFO-038
- **タイトル:** Anthropic Official Statement: Where Things Stand with DoW
- **ソース:** Anthropic公式
- **公開日:** 2026-05-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropic公式声明。大統領のTruth Social投稿後の状況説明。安全性制限（市民大量監視・完全自律武器への不支持）を理由とした連邦排除。Anthropicは$1.8B Akamaiクラウド契約で能力拡大（Claude使用量80x増）。
- **キーファクト:**
  - Anthropic公式声明公開
  - 安全性制限: 市民大量監視・完全自律武器不支持
  - $1.8B Akamai 7年クラウド契約（Claude 80x増対応）
  - Claude年間収益・使用量80倍増
- **引用URL:** https://www.anthropic.com/news/where-stand-department-war
- **Evidence ID:** EVD-20260518-0038

### INFO-039
- **タイトル:** CDT Chain Reaction: Pentagon-Anthropic Civilian Agency Impact
- **ソース:** CDT (Center for Democracy & Technology)
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropic supply-chain risk指定が州・地方政府の公共サービス提供に波及。Figma AI投資がAnthropic規制問題と交錯。安全性企業への商業的報復がイノベーションと信頼にチリング効果を与えるとの警告。
- **キーファクト:**
  - Supply-chain risk指定が州・地方政府レベルに波及
  - 公共サービス提供の混乱とリソース浪費
  - Figma AI投資がAnthropic規制問題と交錯
  - チリング効果（イノベーション・信頼への悪影響）警告
- **引用URL:** https://cdt.org/insights/chain-reaction-what-the-pentagon-anthropic-dispute-means-for-civilian-agencies-across-all-levels-of-government/
- **Evidence ID:** EVD-20260518-0039

### INFO-040
- **タイトル:** AI Model Leaderboard: GPT-5.5 Pro #1, Claude Mythos #2, Gemini 3.1 Pro
- **ソース:** LLM Stats / PricePerToken
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** Best AI for Research 2026ランキング: GPT-5.5 Pro (43.2), Claude Mythos Preview (41.3), Claude Opus 4.6 (38.7), Kimi K2, Gemini 3.1 Pro (37.0)。ARC Challenge: GPT-5 96.3%首位。Gemini 3.1 ProがARC-AGI-2で3 Proの2倍性能。AI IQ新指標サイト登場。
- **キーファクト:**
  - Research: GPT-5.5 Pro 43.2 > Claude Mythos 41.3 > Opus 4.6 38.7 > Gemini 3.1 Pro 37.0
  - ARC Challenge: GPT-5 96.3%首位
  - Gemini 3.1 Pro: ARC-AGI-2で3 Proの2倍性能
  - AI IQ新指標サイト登場（VentureBeat報道）
  - GPT-5.4: MATH-500 99, AIME 2025 99
- **引用URL:** https://llm-stats.com/leaderboards/best-ai-for-research
- **Evidence ID:** EVD-20260518-0040

### INFO-041
- **タイトル:** Gemini 3.1 Pro Release: Benchmarks and Features
- **ソース:** Mashable
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Google
- **要約:** GoogleがGemini 3.1 Proをリリース。ARC-AGI-2で前世代の2倍性能。MMLU-Pro 89.8%（RAG最適）。Google I/O 2026（5/18-19）での詳細発表が期待される。
- **キーファクト:**
  - Gemini 3.1 Proリリース
  - ARC-AGI-2: 前世代の2倍性能
  - MMLU-Pro 89.8%（RAG最適）
- **引用URL:** https://mashable.com/article/google-releases-gemini-3-1-pro-benchmarks
- **Evidence ID:** EVD-20260518-0041

### INFO-042
- **タイトル:** Anthropic Raising $30B + Q1 2026 AI Funding $255.5B
- **ソース:** WSJ / Yahoo Finance
- **公開日:** 2026-05-18
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, OpenAI
- **要約:** Anthropicが追加$30B調達を計画。OpenAIは昨年以降$162B調達（$122Bラウンド含む、シリコンバレー史上最大）。Q1 2026でAIスタートアップが$255.5B調達（2025年通年超え）。グローバルベンチャー投資は$300B（QoQ/YoY +150%）。
- **キーファクト:**
  - Anthropic追加$30B調達計画
  - OpenAI: 昨年以降$162B調達（$122B史上最大ラウンド含む）
  - Q1 2026 AIスタートアップ調達: $255.5B（2025年通年超え）
  - グローバルベンチャー投資$300B（+150% QoQ/YoY）
  - Forbes AI 50: OpenAI評価額$182.6B
- **引用URL:** https://www.wsj.com/tech/ai/anthropic-raising-30-billion-more-as-ai-labs-absorb-majority-of-vc-funding-d26128d7
- **Evidence ID:** EVD-20260518-0042

### INFO-043
- **タイトル:** Microsoft Eyeing Startup Deals for Life After OpenAI (Reuters)
- **ソース:** Reuters
- **公開日:** 2026-05-13
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04, KIQ-002-01
- **関連企業:** Microsoft, OpenAI
- **要約:** MicrosoftがOpenAI後の戦略としてスタートアップ買収を検討。来年までに最先端AIモデル構築の目標。AI人材獲得と技術蓄積が目的。SpaceX-xAI合併（xAI評価額$250B、SpaceX $1T）も確認。
- **キーファクト:**
  - Microsoft: OpenAI後を見据えたスタートアップ買収検討
  - 来年までに最先端AIモデル構築目標
  - SpaceX-xAI合併: xAI $250B評価額、SpaceX $1T評価額
  - Publicis $2.2Bデータ企業買収（AIマーケティング強化）
- **引用URL:** https://www.reuters.com/world/microsoft-eyeing-startup-deals-life-after-openai-2026-05-13/
- **Evidence ID:** EVD-20260518-0043

### INFO-044
- **タイトル:** DeepSeek V3.2 vs Llama 4 vs Qwen 3: Cost-per-Token from $0.04
- **ソース:** Spheron
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03, KIQ-003-01
- **関連企業:** DeepSeek, Meta, Alibaba
- **要約:** OSSモデル比較: DeepSeek V3.2 $0.04-$0.31/M tokens。Qwen3-32Bがコーディング最適、Llamaが汎用最適。1×H100〜8×H200で推論可能。OSSモデルの性能/コスト比が商用モデルに急速に接近。
- **キーファクト:**
  - DeepSeek V3.2: $0.04/M tokens〜（最低コスト）
  - Qwen3-32B: コーディング最適、Llama: 汎用最適
  - 1×H100〜8×H200で推論可能
  - OSS性能/コスト比が商用モデルに接近
- **引用URL:** https://www.spheron.network/blog/deepseek-vs-llama-vs-qwen3/
- **Evidence ID:** EVD-20260518-0044

### INFO-045
- **タイトル:** McKinsey: From AI Table Stakes to AI Advantage - Building Competitive Moats
- **ソース:** McKinsey
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** （業界全体）
- **要約:** McKinseyがAI競争優位の構築方法を分析。データアクセスがモデル性能を向上させスイッチングコストを深化。AI信頼性への課題はグローバル調査で浮彫り。EY分析でAI能力のある企業にM&Aプレミアム評価、ない企業に「ギャップ割引」。
- **キーファクト:**
  - データアクセスがモデル性能向上+スイッチングコスト深化
  - AI能力企業にM&Aプレミアム、不十分企業にギャップ割引
  - グローバル調査でAI信頼性課題浮彫
- **引用URL:** https://www.mckinsey.com/capabilities/quantumblack/our-insights/from-ai-table-stakes-to-ai-advantage-building-competitive-moats
- **Evidence ID:** EVD-20260518-0045

### INFO-046
- **タイトル:** 67% of Entry-Level Developer Jobs Are Gone
- **ソース:** Medium (CodeToDeploy)
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02, KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** Forrester 2026予測: CS専攻入学率20%低下。プログラマー雇用が1980年以来の最低水準。一方でソフトウェアエンジニア求人は二桁成長。Microsoft データは「AIは開発者を代替するのではなく役割を2つに分割する」と示唆。ジュニア層の消失とシニア層の需要増の二極化。
- **キーファクト:**
  - Forrester: CS専攻入学率20%低下予測
  - プログラマー雇用1980年以来最低水準
  - ソフトウェアエンジニア求人は二桁成長
  - Microsoft: AIは代替ではなく役割を2分割
  - ジュニア消失 vs シニア需要増の二極化
- **引用URL:** https://medium.com/codetodeploy/67-of-entry-level-developer-jobs-are-gone-1b48bd8f218b
- **Evidence ID:** EVD-20260518-0046

### INFO-047
- **タイトル:** Developer Skills Atrophying as AI Code Surges
- **ソース:** Reddit (r/cscareerquestions)
- **公開日:** 2026-05-18
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** 開発者コミュニティで「開発スキルがAIコード増加と同等の速度で萎縮している」との指摘。AIコードは不完全で多くの前提を含むため、評価能力を持つ人間が必要。プログラマーとしてのキャリア価値についての議論が活発化。
- **キーファクト:**
  - 開発スキル萎縮がAIコード増加と同速度との指摘
  - AIコードの不完全性と前提含みの問題
  - 評価能力を持つ人間の必要性主張
- **引用URL:** https://www.reddit.com/r/cscareerquestions/comments/1tdsf2j/do_you_guys_honestly_think_its_still_worth/
- **Evidence ID:** EVD-20260518-0047

### INFO-048
- **タイトル:** AGI Timeline: Hassabis 2030, Musk 2026, Altman "Past Event Horizon"
- **ソース:** Multiple (AIRational, AI Corner)
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google, OpenAI, Anthropic
- **要約:** AGI到達予測の更新: Hassabis「2030年」、Altman「既に事象の地平線を超えた」、Musk「2026年」、Amodei「2026年後半〜2027年初頭」。研究者コミュニティ平均は2030s〜2040s。9,800件の予測分析を集約。$4B自己改善AIイニシアチブに主要研究者参加。
- **キーファクト:**
  - Hassabis: AGI 2030年
  - Altman: 既に事象の地平線を超えた
  - Amodei: 2026年後半〜2027年初頭
  - 研究者コミュニティ平均: 2030s〜2040s
  - $4B自己改善AIイニシアチブに主要研究者参加
- **引用URL:** https://www.airational.com/2026/05/
- **Evidence ID:** EVD-20260518-0048

### INFO-049
- **タイトル:** Anthropic 2028 AI Scenario Paper + AI Safety Policy Debate
- **ソース:** Reddit / AI Frontiers
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Anthropicが2028年までのグローバルAIリーダーシップに関する2つの将来シナリオ研究を発表。AI安全策と連邦規制制限の衝突。AI経済効果の予測が停滞から爆発的成長まで四分野に分岐（「Quadrillion-Dollar Disagreement」）。
- **キーファクト:**
  - Anthropic: 2028年AI将来シナリオ研究発表
  - 州AI安全策 vs 連邦規制制限の衝突
  - AI経済効果予測の巨大な分岐（停滞〜爆発的成長）
- **引用URL:** https://www.reddit.com/r/artificial/comments/1td99uw/anthropic_just_published_a_pretty_alarming_2028/
- **Evidence ID:** EVD-20260518-0049

### INFO-050
- **タイトル:** AGI Already Here: ARC-AGI Progress and FrontierMath
- **ソース:** Hybrid Horizons / VentureBeat
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** （業界全体）
- **要約:** 2026年初頭、パブリックモデルがARC-AGI標準ティアで40%超、Tier 4（研究レベル）で30%超。FrontierMathの ceilings に近づく。AI IQ新指標でフロンティアモデルを人間IQスケールで評価。Gemma 4, DeepSeek V4, Kimi K2.6等のオープンモデル爆発。
- **キーファクト:**
  - ARC-AGI標準ティア40%超、Tier 4（研究レベル）30%超
  - FrontierMath ceilings に接近
  - オープンモデル爆発: Gemma 4, DeepSeek V4, Kimi K2.6, MiMo
  - AI IQ新指標サイト登場
- **引用URL:** https://hybridhorizons.substack.com/p/agi-is-already-here-were-just-pretending
- **Evidence ID:** EVD-20260518-0050

### INFO-051
- **タイトル:** Critical Thinking and Judgment: Top AI-Era Skills
- **ソース:** LinkedIn (Sol Rashidi)
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** 2026年採用で重視される5つのAIスキルの1位が「クリティカルシンキングと判断力」。AIが生成する内容を実行前に検証する能力が最も価値あるスキルに。AI代替不可な10の職種リスト公開。AIツール利用能力が求人市場で最速成長スキル。
- **キーファクト:**
  - 2026年採用Top AIスキル: クリティカルシンキング・判断力
  - AI出力検証能力が最重要
  - AI代替不可10職種リスト公開
  - AIツール利用能力が求人市場最速成長スキル
- **引用URL:** https://www.linkedin.com/posts/sol-rashidi-mba-a672291_5-ai-skills-that-will-get-you-hired-in-2026-activity-7459972345311506432-DwpF
- **Evidence ID:** EVD-20260518-0051

### INFO-052
- **タイトル:** Multiverse $70M AI Workforce Reskilling + EY: CEOs Prioritise Reskilling
- **ソース:** AI CERTs / EY
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** Multiverseが$70M調達しAI労働者リスキリング加速。欧州の企業向けアプレンティスシップ・アップスキリング提供。EY Australia調査: 44%のCEOが大規模リスキリング・アップスキリングを今後3年の第1・第2優先事項に。タレント購入から能力構築へのシフト。
- **キーファクト:**
  - Multiverse $70M調達（AIリスキリング）
  - EY: 44%豪州CEOがリスキリング最優先
  - タレント購入→能力構築へのシフト
- **引用URL:** https://www.aicerts.ai/news/multiverses-70m-bet-on-ai-workforce-reskilling/
- **Evidence ID:** EVD-20260518-0052

### INFO-053
- **タイトル:** ByteDance Seed 2.0: 3D Modelling seed3D + Seedance 2.0 SOTA Video
- **ソース:** Instagram/Reddit/BytePlus
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceがseed3D（3Dモデリング）をローンチ。Seedance 2.0が動画生成でSOTA（審美的一貫性）。Seed 2.0 Pro（Doubao 2.0）が複数ベンチマークでSOTAに近接。Seed 2.0 Lite API: $0.25/$2.00 per M tokens。Dola Seed 2.0（旗艦汎用エージェントモデル）、Seedream 5.0（画像生成）も確認。
- **キーファクト:**
  - seed3D: 3Dモデリングローンチ
  - Seedance 2.0: 動画生成SOTA（審美的一貫性）
  - Seed 2.0 Pro: 複数ベンチマークでSOTA近接
  - Seed 2.0 Lite API: $0.25/$2.00 per M tokens
  - Dola Seed 2.0: 旗艦汎用エージェントモデル
  - Seedream 5.0: 画像生成リーディングモデル
- **引用URL:** https://docs.byteplus.com/en/docs/ModelArk/1330310
- **Evidence ID:** EVD-20260518-0053

### INFO-054
- **タイトル:** Anthropic Showing Real Pricing Power as Customers Keep Paying for Claude
- **ソース:** The Information (via Facebook)
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-ANT-SAFETY, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Anthropicが実質的な価格決定力を示している。顧客はClaudeのコーディング性能と安全性機能を特に評価し継続支払い。Claudeモデルは安全性とコーディングで賞賛される。AnthropicがビジネスAI採用でOpenAIを初めて逆転（Ramp AI Index: Anthropic 34.4% vs OpenAI 32.3%）。
- **キーファクト:**
  - AnthropicがビジネスAI採用でOpenAI初逆転（Ramp AI Index）
  - Anthropic 34.4% vs OpenAI 32.3%（2026年4月）
  - 顧客はコーディング性能+安全性機能を評価
  - 価格決定力の実質的証明
- **引用URL:** https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead
- **Evidence ID:** EVD-20260518-0054

### INFO-055
- **タイトル:** Open vs Closed Models: RedMonk Analysis
- **ソース:** RedMonk / Forbes
- **公開日:** 2026-05-15
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-QHG-REDEF, KIQ-003-03
- **関連企業:** （業界全体）
- **要約:** RedMonk分析: クローズドモデルがイノベーションのペースを設定、オープンモデルが追走。Forbes: オープンウェイトモデルがリーダーボード・ベンチマークでキャッチアップ。LLM Stats AI Trends: オープンウェイトモデルの成長と独自システムへの接近を追跡。Kai-Fu Lee: オープンアプローチは利益率低いがアクセシビリティ高く、阻止困難。
- **キーファクト:**
  - クローズド: イノベーションペース設定、オープン: 追走
  - オープンウェイトモデルがベンチマークでキャッチアップ
  - Kai-Fu Lee: オープンは利益率低いが阻止困難
- **引用URL:** https://redmonk.com/sogrady/2026/05/15/open-ai-models/
- **Evidence ID:** EVD-20260518-0055

### INFO-056
- **タイトル:** AI Code Quality Crisis: 75% Logic Errors Up, Security Nearly Tripled
- **ソース:** CodeRabbit / IT Pro / Entrans
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-CAR-REFUTE, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** AIが人間のレビュー可能量を超えるコード生成。論理エラー75%増、セキュリティ問題ほぼ3倍。48%のAI生成コードに少なくとも1つのセキュリティ脆弱性。81%の開発者がAIコードレビューに時間増加。31%の開発者時間が「見えない作業」（AIコードレビュー・バグ修正）に消費。
- **キーファクト:**
  - AI生成コードの論理エラー75%増、セキュリティ問題ほぼ3倍
  - 48%のAI生成コードにセキュリティ脆弱性
  - 81%の開発者がAIコードレビュー時間増加
  - 31%の開発者時間が「見えない作業」に消費
- **引用URL:** https://coderabbit.ai/blog/nobody-is-going-to-read-the-code
- **Evidence ID:** EVD-20260518-0056

### INFO-057
- **タイトル:** METR Study: AI Made Elite Coders 20% Slower (43% Swing)
- **ソース:** METR (via Facebook/Instagram)
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-ELITE-43PCT, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** METR研究: 経験豊富な開発者がAIコーディングアシスタント（Cursor Pro等）使用時に実際に作業速度が低下。予測24%改善に対し20%低下＝43%の乖離。43%のAI書きコードが現実環境で故障。開発者は週平均38%の時間をAIコードデバッグ・検証に消費。
- **キーファクト:**
  - METR研究: エリートコーダーがAI使用時に20%低下
  - 予測24%改善 vs 実際20%低下 = 43%乖離
  - 43%のAIコードが現実環境で故障
  - 開発者週38%時間をAIコード検証に消費
- **引用URL:** https://www.facebook.com/InternetBusinessTalk/posts/ai-made-elite-coders-20-slowerresearchers-had-predicted-a-24-improvement-thats-a/1501951391398360/
- **Evidence ID:** EVD-20260518-0057

### INFO-058
- **タイトル:** 豆包开始付费: 3.45億月活ユーザーの商業化開始
- **ソース:** 知乎/新浪財経/QQ News
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-01
- **関連企業:** ByteDance
- **要約:** 豆包（Doubao）が有料サブスクリプション開始。月活3.45億、日活1.4億で中国AIアプリ断层首位。月額68元（標準）〜200元（強化版）。モデル1.5→2.0へ反復アップグレード完了。月人均使用回数54.8回、アクティブ率33.5%。AIアプリの無料時代終了の象徴。
- **キーファクト:**
  - 豆包月活3.45億、日活1.4億（QuestMobile Q1 2026）
  - 有料サブスクリプション開始: 68元/月（標準）〜200元/月（強化版）
  - 月人均使用54.8回、アクティブ率33.5%
  - モデル1.5→2.0反復アップグレード完了
  - 中国AIアプリで断层首位（千問・DeepSeekを圧倒）
- **引用URL:** https://zhuanlan.zhihu.com/p/2038534523244294504
- **Evidence ID:** EVD-20260518-0058

### INFO-059
- **タイトル:** ByteDance投資動向: 具身知能ロボット＋DeepSeek$10B評価
- **ソース:** 証券時報/DoNews/新浪財経
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance, DeepSeek
- **要約:** ByteDanceが具身知能ロボット企業「自変量科技」に出資（A+輪約10億元）。Seed3D 2.0（3D生成モデル）リリース。DeepSeekが$100億評価額で$3億以上調達交渉中。元ByteDance/Tencent出身者が動画Agent企業（SEEKOO）を設立し$1000万調達。快手が可霊（Kling）を$200億評価額で分社化検討。
- **キーファクト:**
  - ByteDance: 自変量科技（具身知能ロボット）へ出資（A+輪約10億元）
  - Seed3D 2.0（3D生成モデル）リリース
  - DeepSeek: $100億評価額で$3億+調達交渉中
  - SEEKOO（動画Agent）$1000万調達（元ByteDance/Tencent出身者）
  - 快手: 可霊（Kling）$200億評価額分社化検討
- **引用URL:** https://www.donews.com/news/detail/4/6530445.html
- **Evidence ID:** EVD-20260518-0059

### INFO-060
- **タイトル:** Media Industry Must Reinvent to Survive AI Platform Disruption
- **ソース:** Malaysian Reserve / LinkedIn
- **公開日:** 2026-05-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05, KIQ-004-04
- **関連企業:** （業界全体）
- **要約:** メディア産業がAI・プラットフォームアルゴリズムによる破壊に直面。広告収入低下以上に大きな構造的課題。エージェンシービジネスがリアルタイムで書き換えられる。AI自動化は2026年までにマーケティングで生存必須に。ホワイトカラー職の18ヶ月リコンning。
- **キーファクト:**
  - メディア産業がAI+プラットフォーム破壊に直面
  - エージェンシービジネスのリアルタイム書き換え
  - AI自動化が2026年マーケティング生存必須条件に
- **引用URL:** https://themalaysianreserve.com/2026/05/11/media-industry-must-reinvent-to-survive-ai-platform-disruption/
- **Evidence ID:** EVD-20260518-0060

### INFO-061
- **タイトル:** CyberAgent: Generative AI for Ad Creative Automation + Gaming
- **ソース:** Bitget / Rewarx
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgentが生成AIに注力し広告クリエイティブ制作自動化とゲームNPC対話強化に投資。リアルタイムeコマース視覚更新のSpeed Principles適用。日本の広告代理店のAI変革事例。
- **キーファクト:**
  - CyberAgent: 生成AIで広告クリエイティブ自動化
  - ゲームNPC対話強化に生成AI投資
  - リアルタイムeコマース視覚更新のSpeed Principles
- **引用URL:** https://www.bitget.com/stock/tse-4751/what-is
- **Evidence ID:** EVD-20260518-0061

### INFO-062
- **タイトル:** IDC: Agent Takeover - AI Becomes Primary User of Enterprise Software
- **ソース:** IDC
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05, KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** IDCが「Agent Takeover」レポート: AIエージェントがエンタープライズソフトウェアの主要ユーザーに置き換わる。MCP採用、実展開、エージェントオーケストレーション分析。55%の企業がAI導入に向け既存ソフトウェアを統合・整理。ベンダー主導AI展開が自社構築の2倍成功。
- **キーファクト:**
  - AIエージェントがエンタープライズSW主要ユーザーに
  - 55%の企業がAI導入に向けツール統合
  - ベンダー主導AI展開が自社構築の2倍成功
- **引用URL:** https://www.idc.com/resource-center/blog/the-agent-takeover-what-happens-when-ai-becomes-the-primary-user-of-enterprise-software/
- **Evidence ID:** EVD-20260518-0062

### INFO-063
- **タイトル:** Gemini vs ChatGPT API Price: 5x Gap at Flagship Tier
- **ソース:** Tech Insider / BenchLM
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google, OpenAI
- **要約:** Gemini vs ChatGPT API価格比較: 旗艦ティアで5倍の価格差。コンテキスト600Kトークン差。GLM 5.1: $0.98/$3.08 per M tokens。LLM Stats AI Trendsで価格・性能・オープンソース進展の包括的追跡。
- **キーファクト:**
  - Gemini vs ChatGPT旗艦ティアで5倍価格差
  - コンテキスト600Kトークン差
  - GLM 5.1: $0.98/$3.08 per M tokens
  - AI Trends: 価格・性能・OSS進展の包括的追跡可能
- **引用URL:** https://tech-insider.org/gemini-vs-chatgpt-2026/
- **Evidence ID:** EVD-20260518-0063

### INFO-064
- **タイトル:** Coze工作流: AI智能体流水线搭建
- **ソース:** 知乎/CSDN
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** Coze（扣子）のワークフロー機能が中国のエージェント構築で広く活用。ビジュアルドラッグ&ドロップでLLM・プラグイン・コード・DBを組み合わせた自動化フロー構築。バッチSkill統合の標準化SOPも整備。効率80%向上の事例報告。
- **キーファクト:**
  - Coze工作流: ビジュアルドラッグ&ドロップでエージェント構築
  - LLM・プラグイン・コード・DBの組み合わせ自動化
  - バッチSkill統合標準化SOP整備
  - 効率80%向上の事例報告
- **引用URL:** https://zhuanlan.zhihu.com/p/2037598979895112284
- **Evidence ID:** EVD-20260518-0064

### INFO-065
- **タイトル:** Recursive Superintelligence $650M Funding + Bengio LawZero $30M
- **ソース:** AInvest / Forbes / LinkedIn
- **公開日:** 2026-05-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-003-04
- **関連企業:** （業界全体）
- **要約:** Recursive Superintelligence（ステルスAI研究ラボ）が$650M調達（GV主導）。Bengioが$30Mで非営利AI安全ラボLawZero設立。Forbes: AIアライメントだけでは不十分、真の優位性は信頼。AI研究者が人間の繁栄を支えるシステム設計を要求。
- **キーファクト:**
  - Recursive Superintelligence: $650M調達（GV主導）
  - Yoshua Bengio: $30MでLawZero非営利AI安全ラボ設立
  - Bengio: 強化学習は危険な道と警告
  - Forbes: AIアライメント→信頼が真の優位性
- **引用URL:** https://www.ainvest.com/news/recursive-superintelligence-secures-650m-funding-ai-research-2605/
- **Evidence ID:** EVD-20260518-0065

### INFO-066
- **タイトル:** Yann LeCun: AI "New Renaissance" vs Bengio "Extinction Risk"
- **ソース:** Reddit / LinkedIn / Technology Review
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** （業界全体）
- **要約:** AI研究者コミュニティの意見二極化: LeCunは「AIは人類の新ルネサンスをもたらす」と楽観、Bengioは「超知能による人類絶滅リスク」を警告。LeCun新論文: 現在のAIは実際には学習していないと指摘。Max Welling: 「権力欲の人間がAIを武器にする方が現実的リスク」。
- **キーファクト:**
  - LeCun: AIは人類の新ルネサンスをもたらす（楽観）
  - Bengio: 超知能による絶滅リスクを警告
  - LeCun: 現在のAIは実際に学習していない（新論文）
  - Max Welling: 人間の権力欲+AIが現実的リスク
- **引用URL:** https://www.reddit.com/r/TechGawker/comments/1tc1v6h/yoshua_bengio_says_reinforcement_learning_is_a/
- **Evidence ID:** EVD-20260518-0066

### INFO-067
- **タイトル:** Post-AGI World: When Machines Outperform Experts
- **ソース:** Firstpost / Koncept Conference / Stanford
- **公開日:** 2026-05-18
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** Stanfordが1,500人の労働者・AI専門家に調査: AIが代替・自動化する職種の分析。専門家: AIはタスクを代替するが人間を代替するとは限らない。AGI後の世界: 機械が専門家を上回った後、人間の信頼を機械に移す論理。人間の価値は統合・判断・創造性に移行。
- **キーファクト:**
  - Stanford 1,500人調査: AI代替職種分析
  - AIはタスクを代替、人間を代替するとは限らない
  - AGI後: 人間価値は統合・判断・創造性に移行
- **引用URL:** https://www.firstpost.com/tech/will-your-job-survive-ai-experts-say-new-tech-may-replace-tasks-not-humans-ws-e-14011793.html
- **Evidence ID:** EVD-20260518-0067

### INFO-068
- **タイトル:** Interaction Models: Scalable Human-AI Collaboration
- **ソース:** Thinking Machines / LinkedIn
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** ターンベースAIインターフェースを超える「Interaction Models」: マルチモーダル・リアルタイム協調をネイティブに処理。Design Thinking + AIリーダーシップの融合。AIは明確な問題定義・クリーンなインターフェース・意図的決定を要求し、Design Thinkingが提供。
- **キーファクト:**
  - Interaction Models: ターンベース超えのマルチモーダル協調
  - Design Thinking + AIの融合必要性
  - AIが明確な問題定義を要求
- **引用URL:** https://thinkingmachines.ai/blog/interaction-models/
- **Evidence ID:** EVD-20260518-0068

### INFO-069
- **タイトル:** [Step4深掘り] Pentagon deploys Anthropic Mythos: Full Details (Reuters)
- **ソース:** Reuters
- **公開日:** 2026-05-12
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** PentagonのCTO Emil Michael氏がMythos展開は「国家安保の瞬間」と表現。Anthropicの利点は一時的で、OpenAI/xAI/Googleのモデルが間もなく追いつくと予測。Mythosは「Project Glasswing」を通じて限定的利用。数十年前のブラウザ・インフラ・SW脆弱性を検出可能。Anthropicは3月にTrump政権を相手にブラックリスト撤回訴訟を提起済み。
- **キーファクト:**
  - Pentagon CTO: Mythos展開は「国家安保の瞬間」
  - Anthropicの利点は一時的（OpenAI/xAI/Google追いつく）
  - Project Glasswing: Mythos限定的利用の統制イニシアチブ
  - 数十年前のブラウザ・インフラ脆弱性検出能力
  - Anthropic 3月にブラックリスト撤回訴訟提起済み
- **引用URL:** https://www.reuters.com/technology/pentagon-deploys-anthropics-mythos-patch-cyber-gaps-while-planning-ditch-firm-2026-05-12/
- **Evidence ID:** EVD-20260518-0069

### INFO-070
- **タイトル:** [Step4深掘り] Anthropic Beats OpenAI: Ramp AI Index + $30B Revenue + Uber Case
- **ソース:** VentureBeat (Ramp AI Index)
- **公開日:** 2026-05-13
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-ANT-SAFETY, KIQ-001-02, KIQ-003-04
- **関連企業:** Anthropic, OpenAI
- **要約:** Ramp AI Index詳細: Anthropic 34.4% vs OpenAI 32.3%（2026年4月）。Anthropic年間4倍成長 vs OpenAI 0.3%。Claude Code: GitHub公開コミットの4%がClaude Code作成（前月比2倍）。Uber事例: 4ヶ月で年間AI予算使い切り（$3.4B R&D）、エンジニア月$500-$2,000/人API費用、70%のコミットコードがAI生成。Anthropic Q1 2026収益$30B run rate（80x成長、予測10xの8倍）。Anthropic $50B追加調達交渉中（評価額$900B接近）。OpenAI: ChatGPT 9億WAU、$122B調達（$852B評価額）。3つの脅威: トークンコスト肥大、計算量制約、OSS代替品。
- **キーファクト:**
  - Ramp AI Index: Anthropic 34.4% vs OpenAI 32.3%（初の逆転）
  - Claude Code: GitHub公開コミット4%（前月比2倍）
  - Uber: 4ヶ月で年間AI予算使い切り、70%のコミットがAI生成
  - Anthropic Q1収益$30B run rate（80x成長、予測の8倍）
  - Anthropic $50B追加調達交渉中（評価額$900B接近）
  - Gallup: 50%の米労働者がAI使用（初）
  - Cerebras IPO: $5.55B調達（2019年Uber以来最大米テックIPO）
- **引用URL:** https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead
- **Evidence ID:** EVD-20260518-0070

### INFO-071
- **タイトル:** [Step4深掘り] CodeRabbit: AI Code Quality Crisis (470 PR Analysis)
- **ソース:** CodeRabbit
- **公開日:** 2026-05-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-CAR-REFUTE, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** CodeRabbit State of AI vs Human Code Generation Report（470件のOSS GitHub PR分析）: AI PRは人間PRより論理・正当性問題が75%多く、エラー/例外処理ギャップほぼ2倍。セキュリティ問題2.74倍（主にパスワード扱い・安全でないオブジェクト参照）。読みやすさ問題3倍以上。AI生成コードは一見きれいだがローカル慣例・構造に違反。「12ヶ月以内に開発者はコードを読まなくなる」との予測。
- **キーファクト:**
  - 470 PR分析: AI論理エラー75%増、セキュリティ2.74倍、読みやすさ3倍+
  - AI生成コードは一見きれいだがローカル慣例違反
  - エラー/例外処理ギャップほぼ2倍
  - パスワード扱い・安全でないオブジェクト参照が主なセキュリティ問題
  - 12ヶ月以内に開発者はコードを読まなくなる予測
- **引用URL:** https://coderabbit.ai/blog/nobody-is-going-to-read-the-code
- **Evidence ID:** EVD-20260518-0071
