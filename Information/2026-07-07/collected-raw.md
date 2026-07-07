# 収集データ: 2026-07-07

## メタデータ
- 収集日時: 2026-07-07 00:00 UTC
- 品質フラグ: COMPLETE
- INFOエントリ数: 69
- Evidence ID範囲: EVD-20260707-0001 〜 EVD-20260707-0069
- Firecrawl検索クエリ数: ~131（Step1-3: 117クエリ × 24KIQ + 動的追加: 10クエリ × 6優先KIQ + 深掘り: 4クエリ）
- Firecrawlスクレイプ数: 7（Anthropic公式ブログ4 + 深掘り3）
- KIQカバレッジ: 24/24 KIQ 全カバー ✅
  - KIQ-001-01〜04: ✅ (Sonnet 4.6, OpenAI Agents SDK, Gemini, GPT-5)
  - KIQ-002-03〜06: ✅ (SB 53, Fable 5, gov equity stake, Pentagon-Anthropic)
  - KIQ-003-01〜05: ✅ (SWE-bench, model eval, infrastructure, open weights)
  - KIQ-004-01〜04: ✅ (Anthropic financials, OpenAI losses, valuation)
  - KIQ-005-03: ✅ (Fable 5, targeted regulation, autonomous cyber)
  - KIQ-MIL-001: ✅ (動的追加: human-in-the-loop, override statistics)
  - KIQ-GOV-002: ✅ (動的追加: safety research budget, DeepMind brain drain)
  - KIQ-ANT-002: ✅ (動的追加: Claude Code WAU/DAU)
  - KIQ-OAI-001: ✅ (動的追加: revenue breakdown, government vs consumer)
  - KIQ-CAR-002-OPS: ✅ (動的追加: AI skills wage premium, design value)
  - KIQ-NEW-001: ✅ (動的追加: 5% equity stake, Alaska model, other companies)
  - BYTEDANCE-CHINESE: ✅ (Kling AI $3B, ByteDance Seedance, Chinese open-source)
- 動的追加クエリ（Step 1.5）: 10クエリ実行、6 Arbiter優先KIQ対応
- 深掘りスクレイプ（Step 4）: 3件（Carnegie, Where's Your Ed, ActuIA）
- 最低INFO要件: 50 → 達成: 69 ✅

## 収集結果

### INFO-001
- **タイトル:** Introducing Claude Sonnet 4.6
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Sonnet 4.6をリリース。コーディング、コンピュータ使用、長文脈推論、エージェント計画の全面アップグレード。1Mトークンコンテキストウィンドウ（ベータ）。Sonnet 4.5と同価格（$3/$15 per million tokens）。Claude Codeユーザーの70%がSonnet 4.5よりSonnet 4.6を好む。Opus 4.5より59%の確率で好まれる。
- **キーファクト:**
  - OSWorld（コンピュータ使用ベンチマーク）で大幅改善、人間レベルの能力に近づく
  - SWE-bench Verified 80.2%（プロンプト修正時）
  - Vending-Bench Arenaで競争戦略を自律的に開発（前期投資→後期利益集中）
  - プロンプトインジェクション耐性がSonnet 4.5から大幅改善
  - Claude in ExcelがMCPコネクタサポート開始（Pro/Max/Team/Enterprise）
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6
- **Evidence ID:** EVD-20260707-0001

### INFO-002
- **タイトル:** The case for targeted regulation
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2024-10-31
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Anthropicの規制提言。政府は18ヶ月以内にAI政策に緊急行動を取るべきと主張。RSP（Responsible Scaling Policy）を規制のプロトタイプとして提案。透明性・安全性インセンティブ・焦点の絞りの3原則を提唱。
- **キーファクト:**
  - SWE-bench: Claude 2（1.96%, Oct 2023）→ Claude 3.5 Sonnet（49%, Oct 2024）への急速な進歩
  - GPQA: 38.8%（Nov 2023）→ 77.3%（OpenAI o1, Sep 2024）、人間専門家は81.2%
  - フロンティアレッドチームがCBRN・サイバー能力の向上を確認
  - RSPのproportionate・iterative原則の確立
- **引用URL:** https://www.anthropic.com/news/the-case-for-targeted-regulation
- **Evidence ID:** EVD-20260707-0002

### INFO-003
- **タイトル:** Anthropic is endorsing SB 53
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-09-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Anthropicがカリフォルニア州SB 53法案を支持。フロンティアAI開発者に安全フレームワークの公開、透明性報告、内部告発者保護を義務付ける。SB 1047の教訓を踏まえた「トラスト・バット・ベリファイ」アプローチ。FLOPS閾値10^26。
- **キーファクト:**
  - SB 53: 安全フレームワーク公開・透明性報告・内部告発者保護を義務付け
  - 重大安全事象は15日以内に報告義務
  - Google DeepMind・OpenAI・Microsoftも類似フレームワークを採用済み
  - スタートアップ・小規模企業は規制対象外
- **引用URL:** https://www.anthropic.com/news/anthropic-is-endorsing-sb-53
- **Evidence ID:** EVD-20260707-0003

### INFO-004
- **タイトル:** Redeploying Fable 5 (関連コンテンツより発見)
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-07-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-002-06
- **関連企業:** Anthropic, Amazon, Microsoft, Google
- **要約:** Fable 5が7月1日にグローバル再デプロイ。Amazon, Microsoft, Google等のGlasswingパートナーと共同でジェイルブレイク深刻度スコアリングの業界全体フレームワークを提案。Fable 5のサイバーセーフガードとジェイルブレイクフレームワークに関する詳細も公開。
- **キーファクト:**
  - Fable 5がグローバル再デプロイ（2026-07-01）
  - Glasswing パートナーシップ: Amazon, Microsoft, Google等
  - ジェイルブレイク深刻度スコアリングの業界標準化提案
- **引用URL:** https://www.anthropic.com/news/redeploying-fable-5
- **Evidence ID:** EVD-20260707-0004

### INFO-005
- **タイトル:** A Multi-Agent Support Bot with the OpenAI Agents SDK
- **ソース:** Marmelab Blog
- **公開日:** 2026-07-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKを使用したマルチエージェントサポートボットの実装事例。エージェントは名前・モデル・指示・ツールを持ち、入出力ガードレールを設定可能。プロバイダー非依存（provider-agnostic）でOpenAI Responses APIとBedrockの両方をサポート。
- **キーファクト:**
  - OpenAI Agents SDK: provider-agnostic設計、Bedrock直接サポート
  - ツール・ハンドオフ・ガードレール・トレーシング機能
  - Amazon Bedrockでプロキシレイヤーなしで動作
- **引用URL:** https://marmelab.com/blog/2026/07/03/a-multi-agent-support-bot-with-the-openai-agents-sdk.html
- **Evidence ID:** EVD-20260707-0005

### INFO-006
- **タイトル:** Claude Code Updates by Anthropic - July 2026
- **ソース:** Releasebot
- **公開日:** 2026-07-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Claude Codeの7月アップデート。Claude in ChromeがGA（一般提供開始）、バックグラウンドエージェント通知機能追加、Claude Agent SDK TypeScriptの新リリース。権限モード'manual'エイリアス追加、onSetPermissionModeコールバック修正。
- **キーファクト:**
  - Claude in Chrome GA開始
  - バックグラウンドエージェント通知: 入力待ち・完了時に通知発火
  - Claude Agent SDK TypeScript: 権限モード改善
  - Anthropic $200 Agent SDK Credit: Max 20x=$200/mo, Max 5x=$100, Pro=$20
- **引用URL:** https://releasebot.io/updates/anthropic/claude-code
- **Evidence ID:** EVD-20260707-0006

### INFO-007
- **タイトル:** Build agents with Gemini API (I/O Connect '26)
- **ソース:** Google for Developers (YouTube)
- **公開日:** 2026-07-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google
- **要約:** Google I/O Connect '26でのGemini APIエージェント構築セッション。Gemini Enterprise Agent Platformの発表、コード実行機能、物理空間理解ロボティクスエージェントの新機能。
- **キーファクト:**
  - Gemini Enterprise Agent Platform: 統合プラットフォーム
  - 物理空間理解・計器読み取り・ロボティクスエージェント機能
  - Gemini Omni Flash・Nano Banana 2 Lite公開プレビュー開始
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/
- **Evidence ID:** EVD-20260707-0007

### INFO-008
- **タイトル:** xAI Voice Agent Builder with Grok Voice
- **ソース:** Facebook (転載)
- **公開日:** 2026-07-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIがGrok Voiceを活用したノーコードVoice Agent Builderを発表。エンドツーエンドのシングルシステム設計でレイテンシとコストを最小化。開発者は既存のAPIとMCPを使用して本番対応ボイスエージェントを構築可能。価格$0.05/分。
- **キーファクト:**
  - ノーコードVoice Agent Builder発表
  - Grok Voiceベース、エンドツーエンド設計
  - 既存API・MCP統合、$0.05/分の価格設定
- **引用URL:** https://www.facebook.com/groups/findwebdeveloperbd/posts/2879083005758141/
- **Evidence ID:** EVD-20260707-0008

### INFO-009
- **タイトル:** ByteDance Coze Space beta testing & Doubao agent feature removal
- **ソース:** Pandaily / Reuters / Facebook
- **公開日:** 2026-07-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance, Alibaba, Tencent
- **要約:** ByteDanceがCoze Space（各種ソフトウェアツール統合AIエージェント）のベータテストを開始。一方でByteDanceのDoubaoとAlibabaのQwenがAIエージェント機能の削除を7月15日付けで同時発表。中国テック巨头のエージェント戦略転換を示唆。
- **キーファクト:**
  - Coze Space: ベータテスト開始、多ソフト統合エージェント
  - Doubao・QwenがAIエージェント機能を7月15日削除予定
  - Tencent: Hunyuan3D-2.0とCoze Spaceでエージェント機能強化
- **引用URL:** https://x.com/thePandaily/article/2073365744096596319
- **Evidence ID:** EVD-20260707-0009

### INFO-010
- **タイトル:** AI Agent Framework Comparison 2026
- **ソース:** VePrompts
- **公開日:** 2026-07-04
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** （複数）
- **要約:** 27のAIエージェントフレームワークの比較。LangGraph, CrewAI, AutoGen, PydanticAI, smolagents, Letta等を網羅。エンタープライズ用途での選択基準を提供。
- **キーファクト:**
  - 27フレームワーク比較: LangGraph, CrewAI, AutoGen, PydanticAI等
  - エンタープライズ観測可能性要件: 完全実行トレース・ステップ別レイテンシ・コスト追跡
  - Gartner: 80%の組織がAIエージェントからリスク行動を報告
- **引用URL:** https://veprompts.com/agents/frameworks/
- **Evidence ID:** EVD-20260707-0010

### INFO-011
- **タイトル:** Gemini Enterprise Agent Platform - SLA & Overview
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-07-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** Google CloudがGemini Enterprise Agent PlatformのSLAを公開。エンタープライズ級AIエージェントの構築・デプロイ・ガバナンス・最適化のための統合プラットフォーム。Google AI Studioからの移行パス提供、24/7エンタープライズサポートとSLA。
- **キーファクト:**
  - Gemini Enterprise Agent Platform: 統合エージェントプラットフォーム
  - エンタープライズSLA・24/7サポート提供
  - Google AI Studioからの移行サポート
- **引用URL:** https://cloud.google.com/vertex-ai/generative-ai/sla
- **Evidence ID:** EVD-20260707-0011

### INFO-012
- **タイトル:** Claude Enterprise SOC 2 Type II & Security Controls
- **ソース:** MintMCP / Truefoundry / IntuitionLabs
- **公開日:** 2026-07-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Enterpriseのセキュリティ体制。SOC 2 Type II証明、SSO via SAML、SCIMディレクトリ同期、カスタムデータ保持期間設定。Claude Code at Scaleの6つの制御レイヤー（SSO、権限、監査等）。HIPAA対応はEnterprise（50席以上）でBAA署名必要。
- **キーファクト:**
  - SOC 2 Type II証明、SAML SSO、SCIM同期
  - Claude Code: 6つのエンタープライズ制御レイヤー
  - HIPAA対応: Enterprise（50席以上）でBAA署名必要
  - Claude Tag: AIエージェントアイデンティティ管理
- **引用URL:** https://www.mintmcp.com/blog/claude-enterprise-review
- **Evidence ID:** EVD-20260707-0012

### INFO-013
- **タイトル:** Okta for AI Agents - FedRAMP and HIPAA
- **ソース:** The New Stack (Facebook転載)
- **公開日:** 2026-07-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Okta
- **要約:** OktaがAI Agents向けのFedRAMP・HIPAA対応コア機能を提供開始。AIエージェントのライフサイクル管理をコンプライアンス境界内で実現。エンタープライズAIエージェントのアイデンティティ・アクセス管理の標準化が進む。
- **キーファクト:**
  - FedRAMP・HIPAA対応AIエージェントライフサイクル管理
  - コンプライアンス境界内でのAIエージェント管理
- **引用URL:** https://www.facebook.com/thenewstack/posts/1916693249762860/
- **Evidence ID:** EVD-20260707-0013

### INFO-014
- **タイトル:** AI Agent Market Size: $236B by 2034 (45.82% CAGR)
- **ソース:** Nevermined
- **公開日:** 2026-07-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** （複数）
- **要約:** AIエージェント市場は2034年までに約$2360億に成長予測（CAGR 45.82%）。30倍の拡大。Gartnerは2026年末までにエンタープライズアプリの40%がタスク特化型エージェントを搭載すると予測（2025年の5%未満から）。
- **キーファクト:**
  - 市場規模予測: 2034年までに$2360億（CAGR 45.82%）
  - Gartner: 2026年末にエンタープライズアプリの40%がエージェント搭載（2025年は5%未満）
- **引用URL:** https://nevermined.ai/blog/ai-agent-market-size-statistics
- **Evidence ID:** EVD-20260707-0014

### INFO-015
- **タイトル:** MCP Specification Release Candidate - 2026-07-28
- **ソース:** Model Context Protocol Blog
- **公開日:** 2026-07-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic, Linux Foundation, AAIF
- **要約:** MCP仕様の次期リリース候補公開。ステートレスプロトコルコア、Extensions フレームワーク、Tasks 機能を追加。InfoQ報道: MCPにエンタープライズ向け中央集権認証が追加、組織はMCPサーバーの認可を一元管理可能。
- **キーファクト:**
  - MCP次期仕様: ステートレスコア + Extensions + Tasks
  - エンタープライズ中央集権認証（EMA）追加
  - 単一ログインで全MCPサーバーアクセス可能
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260707-0015

### INFO-016
- **タイトル:** iTMethods Joins Linux Foundation, FINOS, and AAIF
- **ソース:** PR Newswire / Morningstar
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** （複数）
- **要約:** iTMethodsがLinux Foundation、FINOS、Agentic AI Foundation（AAIF）に参加。AAIFは相互運用可能な自律エージェント向けオープン標準（MCP含む）を開発。agentgatewayがAAIF初のプロジェクトとして参加。
- **キーファクト:**
  - AAIF: 相互運用可能な自律エージェント向けオープン標準開発
  - agentgateway: AAIF初のプロジェクト（オープン・ポータブル・ゲートウェイ）
  - 標準化団体: Linux Foundation, FINOS, AAIF, W3C, IETF, OpenID, NIST
- **引用URL:** https://www.prnewswire.com/news-releases/itmethods-joins-the-linux-foundation-finos-and-agentic-ai-foundation-to-advance-governance-standards-for-regulated-agentic-ai-302816900.html
- **Evidence ID:** EVD-20260707-0016

### INFO-017
- **タイトル:** OpenAI ShellTool & Skills for Agent SDK
- **ソース:** OpenAI / Docker Docs / GitHub
- **公開日:** 2026-07-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI Responses APIにコンピュータ環境（ShellTool）を統合。OpenAI管理サンドボックスコンテナ内でシェルコマンドを安全に実行。Skillsはタスクに応じてオンデマンドでロードされる専門指示。Hugging Face Skills、LobeHub等のマーケットプレイスが台頭。
- **キーファクト:**
  - ShellTool: OpenAI管理サンドボックス内でシェル実行
  - Responses API + ShellTool + ホストコンテナでエージェントランタイム構築
  - Skills: オンデマンドでロードされる専門指示、shell/writeツールは非表示
  - Docker, Hugging Face, LobeHub, ClaudePluginHubがスキルマーケットプレイス展開
- **引用URL:** https://openai.com/fr-CA/index/equip-responses-api-computer-environment/
- **Evidence ID:** EVD-20260707-0017

### INFO-018
- **タイトル:** Claude Code Security: Permissions, MCP, Sandboxing
- **ソース:** DataCamp / Truefoundry
- **公開日:** 2026-07-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude Codeのセキュリティモデル解説。権限システム、MCPガバナンス、サンドボックス実行の仕組み。エンタープライズ展開向け6つの制御レイヤー（SSO、RBAC、監査ログ、MCPガバナンス等）。コード実行はサンドボックス内で処理、フィルタ結果を返す。
- **キーファクト:**
  - Claude Code: 権限システム + MCPガバナンス + サンドボックス実行
  - 6つのエンタープライズ制御レイヤー
  - コード実行サンドボックス: データ処理→フィルタ結果返却
- **引用URL:** https://www.datacamp.com/tutorial/claude-code-security
- **Evidence ID:** EVD-20260707-0018

### INFO-019
- **タイトル:** AI Agent Vendor Lock-In: Context Lock-In Concept
- **ソース:** Chitika / LinkedIn
- **公開日:** 2026-07-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** （複数）
- **要約:** ベンダーロックインから「コンテキストロックイン」への進化。従来のベンダーロックインは独自データ形式と切り替えコストが主だったが、コンテキストロックインは「組織的認知」への依存が問題。ベンダーロックインされた組織は切り替えコストが約16倍高いとの報道。
- **キーファクト:**
  - コンテキストロックイン: 組織的認知への依存が新たなロックイン形態
  - ベンダーロックイン組織の切り替えコスト: 約16倍
  - Red Hat: オープンウェイトモデル（vLLM）への移行でロックイン回避を提唱
- **引用URL:** https://www.chitika.com/ai-agent-vendor-lock-in-in-2026-how-to-choose-a-flexible-rag-platform-before-you-buy/
- **Evidence ID:** EVD-20260707-0019

### INFO-020
- **タイトル:** AWS Bedrock Agents Classic → Maintenance Mode (July 30, 2026)
- **ソース:** AWS Documentation
- **公開日:** 2026-07-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** Amazon Bedrock Agents（2023年11月ローンチ）が「Bedrock Agents Classic」に改名され、2026年7月30日から新規顧客の受け入れを停止。メンテナンスモードに移行。後継はAgentCore。AWS Bedrockのエージェント世代交代が進む。
- **キーファクト:**
  - Bedrock Agents Classic: 7月30日から新規顧客停止
  - メンテナンスモード移行（2026年8月31日以降）
  - 後継: AgentCore
- **引用URL:** https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html
- **Evidence ID:** EVD-20260707-0020

### INFO-021
- **タイトル:** Azure AI Foundry Agent Service & MCP Integration
- **ソース:** LITS / Microsoft Learn / KM World
- **公開日:** 2026-07-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundry Agent ServiceがMCP経由でカスタムAPI・ツール・エンタープライズシステムにセキュア接続。BlueVoyantがMicrosoft環境向けAIエージェントセキュリティサービスをリリース（Copilot Studio, Azure AI Foundry等の保護）。Azureは完全エージェントライフサイクルをサポート。
- **キーファクト:**
  - Azure AI Foundry Agent Service: MCP経由でエンタープライズ統合
  - Azure: モデル→オーケストレーション→ランタイム→ガバナンス→デプロイの完全スタック
  - BlueVoyant: Microsoft 365 Copilot, Copilot Studio等のAIエージェントセキュリティサービス
- **引用URL:** https://www.lits.services/azure-ai-foundry-agent-service/
- **Evidence ID:** EVD-20260707-0021

### INFO-022
- **タイトル:** Gemini Omni Flash & Nano Banana 2 Lite Release
- **ソース:** Google Blog
- **公開日:** 2026-06-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Google
- **要約:** GoogleがGemini Omni（ビデオ生成・会話編集向け高品質コスト効率モデル）とNano Banana 2 Liteを公開プレビューでリリース。Gemini Live APIで低レイテンシ・リアルタイム音声・ビデオ対話。Android StudioにAgent Mode追加。
- **キーファクト:**
  - Gemini Omni: ビデオ生成・会話編集モデル、Google AI Studio + Gemini APIで公開プレビュー
  - Gemini Live API: リアルタイム音声・ビデオ対話
  - Android Studio: Agent Mode追加（複雑・多段階開発タスク）
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/
- **Evidence ID:** EVD-20260707-0022

### INFO-023
- **タイトル:** Multimodal AI Benchmarks July 2026
- **ソース:** LMCouncil / BenchLM / Vellum
- **公開日:** 2026-07-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** （複数）
- **要約:** マルチモーダルベンチマーク最新結果。Gemini 3 Pro Deep Thinkがマルチモーダル&グラウンデッドスコア95.8で1位。MMMU/OfficeQA/CharXivで評価。Claude Fable 5がMMMU-Pro 81.9%でトップ。
- **キーファクト:**
  - マルチモーダル1位: Gemini 3 Pro Deep Think (95.8 weighted score)
  - MMMU-Pro: Claude Fable 5 81.9%
  - 比較対象: GPT-5.5, Claude Opus, Gemini 3.1 Pro等
- **引用URL:** https://lmcouncil.ai/benchmarks
- **Evidence ID:** EVD-20260707-0023

### INFO-024
- **タイトル:** 89% of AI Agent Pilots Never Scale: Gartner 2026 Data
- **ソース:** Beri.net / Gartner / Deloitte
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （複数）
- **要約:** Gartner 2026データ: 89%のAIエージェントパイロットがスケールしない。Deloitte: 58%の企業が物理AIをある程度使用、80%が2年以内に導入予定。AIエージェント市場は2025年$78.4億→2030年$526.2億予測（CAGR 46.3%）。43%の企業がセキュリティを主な障壁と指摘。
- **キーファクト:**
  - 89%のパイロットがスケールせず（Gartner）
  - 58%の企業が物理AI使用中、80%が2年以内導入予定（Deloitte）
  - 市場: $7.84B(2025) → $52.62B(2030), CAGR 46.3%
  - 43%がセキュリティを主な障壁
- **引用URL:** https://www.beri.net/article/ai-agent-adoption-enterprise-2026-gartner-idc
- **Evidence ID:** EVD-20260707-0024

### INFO-025
- **タイトル:** 80% of Fortune 500 Building AI Agents, Only 17% in Production
- **ソース:** Elementum
- **公開日:** 2026-07-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** Microsoft, （複数）
- **要約:** Fortune 500の80%がMicrosoft Copilot Studio/Agent BuilderでAIエージェントを構築中だが、本番稼働は17%のみ。79%のエグゼクティブが組織内でAIエージェント使用を報告。期待-実態ギャップが構造化。
- **キーファクト:**
  - Fortune 500の80%がAIエージェント構築中
  - 本番稼働は17%のみ（80%の中の）
  - 79%のエグゼクティブがAIエージェント使用を報告
- **引用URL:** https://www.elementum.ai/blog/best-enterprise-ai-agent-platforms
- **Evidence ID:** EVD-20260707-0025

### INFO-026
- **タイトル:** EU AI Act Now in Effect - GPAI Rules Hit August 2
- **ソース:** EWSolutions / EY
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （複数）
- **要約:** EU AI Actが発効。ハイリスク分野の期限は2027年に移行したが、GPAI（汎用AI）と透明性ルールは8月2日に適用。違反時の罰金は€750万〜売上の7%。米国企業も対応必要。
- **キーファクト:**
  - EU AI Act発効中、GPAIルールは8月2日適用
  - ハイリスク分野期限: 2027年に延期
  - 罰金: €750万〜売上の7%
- **引用URL:** https://www.ewsolutions.com/eu-ai-act-updates-2026/
- **Evidence ID:** EVD-20260707-0026

### INFO-027
- **タイトル:** Trump Executive Order: Shutting Down State AI Regulations
- **ソース:** White & Case / Financial Times / ABA
- **公開日:** 2026-07-01
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （複数）
- **要約:** Trump政権が州レベルAI規制を制限する大統領令に署名。連邦レベルで監視を一元化。AI規制当局の設立には反対。FT報道: 「Trumpは米国AI規制当局を支持しない」。12月11日大統領令は法務長官にAI訴訟タスクフォースの設立を指示。「Preventing Woke AI」大統領令（2025年7月23日）。
- **キーファクト:**
  - 州レベルAI規制を制限する大統領令署名
  - AI規制当局設立に反対
  - 「Preventing Woke AI」大統領令(2025-07-23)
  - 法務長官にAI訴訟タスクフォース設立指示
- **引用URL:** https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker-united-states
- **Evidence ID:** EVD-20260707-0027

### INFO-028
- **タイトル:** China's AI Companion Rules Force Doubao & Qwen to Pull Agents (July 15)
- **ソース:** AI News / IAPP
- **公開日:** 2026-07-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance, Alibaba
- **要約:** 中国のAIコンパニオン規則が7月15日に施行。ByteDanceのDoubaoとAlibabaのQwenがカスタムエージェント機能の削除を同時発表。北京は感情依存を生むAIコンパニオンを規制対象。中国のAI規制は包括的法律からSSE部門規則（迅速・効果的）へ移行。
- **キーファクト:**
  - 中国AIコンパニオン規則: 7月15日施行
  - Doubao・Qwenがカスタムエージェント削除
  - 規制対象: 感情依存を生むAIコンパニオン
  - 中国規制手法: SSE（Small, Swift, Effective）部門規則へ移行
- **引用URL:** https://www.artificialintelligence-news.com/news/china-ai-companion-rules/
- **Evidence ID:** EVD-20260707-0028

### INFO-029
- **タイトル:** Anthropic-Pentagon Saga: SCR Designation, Lawsuit, Export Controls Lifted
- **ソース:** NYT / WSJ / CNN / Bloomberg / Fortune
- **公開日:** 2026-06-30
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, OpenAI, Palantir, Scale AI
- **要約:** AnthropicがPentagonの$200M契約で自律兵器・監視の2つのレッドラインを拒否。PentagonがAnthropicを「サプライチェーンリスク」に指定（通常は外国の敵対国関連企業向け）。AnthropicがPentagonを訴え、最終的に輸出規制が解除。DPA（国防生産法）の適用圧力。OpenAIは同じレッドライン+第三の制限でDoD分類ネットワークに配置。Palantirは$15Bの軍事契約。Scale AIは$500MのDoD契約。
- **キーファクト:**
  - Anthropic: $200M Pentagon契約で自律兵器・監視のレッドライン拒否
  - Pentagon: AnthropicをSCR（サプライチェーンリスク）指定（通常は外国敵対国向け）
  - AnthropicがPentagonを提訴、最終的に輸出規制解除
  - DPA（国防生産法）による強制圧力
  - OpenAI: 同じレッドライン+第3制限でDoD分類ネットワーク配置
  - Palantir: $15B軍事契約、Scale AI: $500M DoD契約
  - 国連事務総長: 致死的自律兵器の国際法での禁止を要請
- **引用URL:** https://fortune.com/2026/06/30/anthropic-clash-with-u-s-government-shows-its-failure-to-play-by-trump-administration-playbook/
- **Evidence ID:** EVD-20260707-0029

### INFO-030
- **タイトル:** AI Agents Complete Only 30.3% of Tasks Fully Autonomously
- **ソース:** Brian Roemmele / WebArena Benchmark
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-002-02
- **関連企業:** Google, OpenAI
- **要約:** 最新研究: 最高のAIエージェント（Gemini 2.5 Pro搭載）でも完全自律完了率は30.3%のみ。WebArenaベンチマーク（800+リアルウェブタスク）でGPT-4エージェントは14.41%完了（人間ベースライン78.24%）。期待-実態ギャップの定量的証拠。
- **キーファクト:**
  - AIエージェント完全自律完了率: 30.3%（Gemini 2.5 Pro）
  - WebArena: GPT-4エージェント14.41% vs 人間78.24%
  - 95%の企業がAIからROIを得られていない
  - 40%のAI生産性向上がエラーのやり直しで失われる
- **引用URL:** https://x.com/BrianRoemmele/article/2072176148218618058
- **Evidence ID:** EVD-20260707-0030

### INFO-031
- **タイトル:** Klarna & Duolingo: AI Headcount Reduction Results Mixed
- **ソース:** Tech.co / WCCFtech / Reworked
- **公開日:** 2026-07-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaが700人のカスタマーサービス担当をAIで置換し$40M削減。Duolingoは契約業者の10%を削減しAIに移行。しかし、人員削減を行った企業はそうでない企業と同じ財務成果しか得られなかった（80%のリーダーが認める）。AI FOMOが戦略でないとの指摘。
- **キーファクト:**
  - Klarna: 700人CS置換、$40M削減
  - Duolingo: 契約業者10%削減、AI移行
  - 80%のリーダーが人員削減を実施したが、財務成果は同じ
  - AI人員削減企業はROI向上を見られない
- **引用URL:** https://tech.co/news/companies-replace-workers-with-ai
- **Evidence ID:** EVD-20260707-0031

### INFO-032
- **タイトル:** Agentic AI to Disrupt $234B in SaaS Spending (Gartner)
- **ソース:** CIO Dive / Gartner
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** （複数）
- **要約:** Gartner予測: アジェンティックAIが2026〜2030年で$2340億のエンタープライズSaaS支出を破壊。AIエージェントがSaaS株式から$2兆を抹消。2027年までにエージェントAI実装の3分の1が異なるスキルのエージェントを組み合わせると予測。SaaSミドルレイヤーの圧縮が加速。
- **キーファクト:**
  - $2340億SaaS支出破壊予測（Gartner）
  - SaaS株から$2兆抹消（2026年）
  - 2027年に3分の1が複合エージェント実装
  - AIエージェントが5年分のデータを9秒で削除した事故（PocketOS）
- **引用URL:** https://www.ciodive.com/news/agentic-ai-disrupt-234-billion-saas-spending/824530/
- **Evidence ID:** EVD-20260707-0032

### INFO-033
- **タイトル:** WPP 50,000+ Employees Using AI via In-House Platform
- **ソース:** Atmospheredaily / AdExchanger
- **公開日:** 2026-07-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Google, WPP, Ogilvy
- **要約:** WPPがインハウスAIプラットフォーム「WPP Open」で5万人以上がAI使用。MetaのAndromedaがクリエイティブ多様性を推進。Meta・Google・AmazonのAI広告プラットフォームが従来のエージェンシモデルを脅かす。Ogilvy等のエージェンシーの財務構造が劇的に変化。AIがメディアバイイング・キャンペーン最適化・インベントリ分析を実行。
- **キーファクト:**
  - WPP: 5万人以上がWPP OpenでAI使用
  - Meta Andromeda: クリエイティブ多様性の自動化
  - Meta・Google・AmazonのAI広告プラットフォームがエージェンシー脅かす
  - 参入障壁の消滅: AIで創作チーム全体の仕事を1つのAIが代替可能
- **引用URL:** https://www.facebook.com/Atmospheredaily/posts/1495378599295364/
- **Evidence ID:** EVD-20260707-0033

### INFO-034
- **タイトル:** OpenAI API Pricing July 2026: GPT-5.6 Starts at $1/$10 per M Tokens
- **ソース:** AI Pricing Guru
- **公開日:** 2026-07-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAI価格帯は$0.10/M（GPT-4.1 nano入力）から$30/M（GPT-5.5 Pro入力）。新GPT-5.6ファミリーは$1入力/$10出力から開始。GPT-5.4（3月5日リリース）は$2.50入力/$15出力。エージェントの暴走によるAPIコスト増大が問題化、支出上限設定機能の重要性指摘。
- **キーファクト:**
  - 価格幅: $0.10/M〜$30/M入力（600倍差）
  - GPT-5.6: $1/$10 per M tokens
  - GPT-5.4: $2.50/$15 per M tokens
  - エージェント暴走によるコスト増大が問題化
- **引用URL:** https://www.aipricing.guru/openai-pricing/
- **Evidence ID:** EVD-20260707-0034

### INFO-035
- **タイトル:** Claude Sonnet 5 API Pricing: $2/$10 + Usage-Based Billing Shift
- **ソース:** Anthropic / Suprmind / Kingy AI
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 5 API価格: $2入力/$10出力 per M tokens（8月31日まで紹介価格）。Anthropic 2026年は使用量ベース課金に移行。Message Batches APIで標準価格から50%オフ。Opus価格は67%下落。
- **キーファクト:**
  - Sonnet 5: $2/$10 per M tokens（紹介価格8/31まで）
  - 使用量ベース課金に移行（定額制廃止）
  - Message Batches API: 50%オフ
  - Opus価格67%下落
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-5
- **Evidence ID:** EVD-20260707-0035

### INFO-036
- **タイトル:** Gemini 3.1 Pro Preview Pricing & Token Cost Collapse
- **ソース:** Google AI / LA Times / Barron's
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google
- **要約:** Gemini 3.1 Pro Preview価格公開。Silicon Data LLM Token Expenditure Indexは5月高値から約20%下落。AIトークン価格の崩壊と規制強化でAI企業のプライシングパワーが脆弱化。Barron's: 最良ChatGPTモデルのコストは$0.50〜$30/M tokens。
- **キーファクト:**
  - Gemini 3.1 Pro Preview価格公開
  - Token Expenditure Index: 高値から約20%下落
  - トークン価格崩壊でAI企業プライシングパワーが脆弱化
  - モデル間価格差600倍（$0.05〜$30/M入力）
- **引用URL:** https://www.latimes.com/business/story/2026-07-03/with-token-prices-collapsing-regulation-rising-ais-pricing-power-looks-fragile
- **Evidence ID:** EVD-20260707-0036

### INFO-037
- **タイトル:** AI Benchmarks July 2026: MMLU 92% Avg, GPQA/SWE-bench/ARC-AGI-2 Differentiate Frontier
- **ソース:** Vellum / LMCouncil / ValueAddVC
- **公開日:** 2026-07-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** （複数）
- **要約:** MMLUは2026年に平均92%（2020年は32%）で飽和。フロンティアモデルの差別化はGPQA Diamond、SWE-bench Verified、ARC-AGI-2に移行。Claude Opus 4がARC Easy 99.7%でトップ。LMCouncil包括ベンチマーク: Claude Fable 5が1位。
- **キーファクト:**
  - MMLU平均92%（2020年32%）で飽和状態
  - 差別化ベンチマーク: GPQA Diamond, SWE-bench Verified, ARC-AGI-2
  - ARC Easy: Claude Opus 4 99.7%で1位
  - LMCouncil包括: Claude Fable 5が1位
- **引用URL:** https://valueaddvc.com/blog/ai-model-benchmarks-explained-mmlu-humaneval-lmsys-arena-and-what-they-actually-measure
- **Evidence ID:** EVD-20260707-0037

### INFO-038
- **タイトル:** GLM 5.2 Tops Open-Weight Rankings (Artificial Analysis)
- **ソース:** Tom's Hardware / Artificial Analysis
- **公開日:** 2026-07-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** Z.ai (GLM), MiniMax, DeepSeek, Anthropic
- **要約:** 中国Z.aiのGLM 5.2がArtificial Analysis Intelligence Index v4.1でオープンウェイトモデル1位（スコア51）。MiniMax-M3、DeepSeek V4を上回る。全てHuaweiシリコンで動作。SevenLab: Claude Fable 5が全体1位、オープンソース1位はGLM-5.2(max)。
- **キーファクト:**
  - Artificial Analysis Intelligence Index v4.1: GLM 5.2 スコア51（オープンウェイト1位）
  - SevenLab 7/5: Claude Fable 5全体1位、GLM-5.2(max)オープンソース1位
  - GLM 5.2: 全てHuaweiシリコンで動作
  - MiniMax M3: コストパフォーマンスでフロンティア級
- **引用URL:** https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-free-glm-5-2-tops-the-open-weight-ai-rankings-on-all-huawei-silicon
- **Evidence ID:** EVD-20260707-0038

### INFO-039
- **タイトル:** Open Source LLMs Fell to 11% of Enterprise Spend
- **ソース:** Jesse Zhang (X)
- **公開日:** 2026-07-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** （複数）
- **要約:** オープンソースモデルのエンタープライズLLM支出シェアが11%に低下（1年前は19%）。逆に、76%の企業がオープンソースモデルのスケールアップを報告。商用モデルのシェア拡大が続く。Thunder Compute: オープンソースモデルが予想より速く商用モデルとのギャップを縮めている。
- **キーファクト:**
  - オープンソースシェア: 19%(1年前) → 11%(現在)、低下傾向
  - 76%の企業がオープンソースモデルをスケールアップ中
  - GLM 5.2、DeepSeek V4、MiniMax M3がオープンウェイト上位
- **引用URL:** https://x.com/thejessezhang/article/2074154325933424861
- **Evidence ID:** EVD-20260707-0039

### INFO-040
- **タイトル:** Mistral AI Summer Model: Open-Weight Early Access in July
- **ソース:** TechCrunch
- **公開日:** 2026-07-04
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral AI
- **要約:** Mistral AIが夏にオープンウェイトモデルをリリース予定。7月にアーリーアクセス開始。計算量が少ない領域で特に有望。欧州AI主権の象徴的存在。
- **キーファクト:**
  - 夏リリース予定のオープンウェイトモデル
  - 7月アーリーアクセス開始
  - 低計算量領域で有望
- **引用URL:** https://techcrunch.com/2026/07/04/what-is-mistral-ai-everything-to-know-about-the-openai-competitor/
- **Evidence ID:** EVD-20260707-0040

### INFO-041
- **タイトル:** Together AI Raises $800M at $8.3B Valuation
- **ソース:** NYT / Crunchbase
- **公開日:** 2026-07-01
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Together AI, MGX, Kling AI, OpenAI
- **要約:** Together AIが$8億調達（評価額$83億、総調達$13億）。MGXがAI特化ファンド$490億調達。Kling AIが$30億調達（AI動画生成モデル企業として過去最大）。OpenAIは$400億調達目標（評価額$3400億、SoftBank主導）。Anthropic評価額$9000億〜$9650億。
- **キーファクト:**
  - Together AI: $800M調達、評価額$8.3B
  - MGX: AIファンド$490億調達
  - Kling AI: $30億調達（評価額$180億、AI動画生成で過去最大）
  - OpenAI: $400億調達目標、評価額$3400億
  - Anthropic: 評価額$9000億〜$9650億
  - AIスタートアップ全体: 2025年に$2020億調達（全世界VCの約50%）
- **引用URL:** https://www.nytimes.com/2026/07/01/business/dealbook/together-ai-funding.html
- **Evidence ID:** EVD-20260707-0041

### INFO-042
- **タイトル:** Major AI M&A: SpaceX-Cursor $60B, Salesforce-Fin $3.6B, Cohere-Aleph Alpha $20B
- **ソース:** Fortune / Channel Insider / Yale Law Journal
- **公開日:** 2026-06-30
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** SpaceX/Cursor, Salesforce/Fin, Cohere/Aleph Alpha, Google/Windsurf
- **要約:** 主要AI M&A: SpaceXがCursorを$600億で買収（2026年6月成立）。SalesforceがAIエージェント企業Finを$36億で買収。CohereがAleph Alphaと合併（評価額$200億）。GoogleがWindsurfに$24億支払い（リバースアクワイハイヤー）。
- **キーファクト:**
  - SpaceX → Cursor: $600億買収（6月成立）
  - Salesforce → Fin: $36億買収
  - Cohere + Aleph Alpha: 合併、評価額$200億
  - Google → Windsurf: $24億（リバースアクワイハイヤー）
- **引用URL:** https://www.channelinsider.com/channel-business/mergers-and-acquisitions/ma-june-2026-recap/
- **Evidence ID:** EVD-20260707-0042

### INFO-043
- **タイトル:** Hyperscaler AI Capex Raised to $750B in 2026, $850B in Data Center Leases
- **ソース:** Yahoo Finance / Cointelegraph / WSJ
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Microsoft, Google, Amazon, Meta
- **要約:** ハイパースケーラーのAI資本支出が2026年$7500億に引き上げ（従来$6700億）、2027年には$1兆超予測。米テック企業がデータセンターリースに過去最高$8500億コミット（前年比204%増）。AIデータセンターの水使用量が急増。REITでデータセンターが最有望セクター。
- **キーファクト:**
  - ハイパースケーラーAI支出: $750B(2026) → $1T+(2027)
  - データセンターリース: $850B（前年比204%増）
  - AI DC水消費: Microsoft/Google/Amazonで急増
  - データセンターがREIT最有望セクター
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/3-ai-data-center-power-123057075.html
- **Evidence ID:** EVD-20260707-0043

### INFO-044
- **タイトル:** AI Service Costs Subsidized Below True Cost (Economist)
- **ソース:** The Economist / LangWatch / Finout
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** （複数）
- **要約:** AIサービスのコストが真のコスト以下に補助価格設定されている。推論は採用と市場シェア最大化のために真コスト以下で価格設定。定額制プラン終了後の「成功タスクあたりコスト」が真の指標。FinOpsツールの重要性増大。コンテキストロックインが新たな切り替え障壁。
- **キーファクト:**
  - 推論コストが真コスト以下に補助設定（市場シェア獲得のため）
  - 定額制終了後の「成功タスクあたりコスト」が真の指標
  - コンテキストロックイン: 組織的認知への依存が新たなロックイン形態
  - AIプラットフォームロックインが2026年の戦略リスク
- **引用URL:** https://www.facebook.com/TheEconomist/posts/1527970746028107/
- **Evidence ID:** EVD-20260707-0044

### INFO-045
- **タイトル:** KPMG: 64% of Organizations Changed Entry-Level Hiring Due to AI Agents
- **ソース:** SearchUnify / KPMG / CPA Trendlines
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** KPMG
- **要約:** KPMG調査: 64%の組織がAIエージェントのために入社レベル採用方針を変更（前期は18%から急増）。CHROがCAIOとしてエージェント管理を主導。77%が過去12ヶ月で少なくとも1回の採用困難を報告。56%が新入社員が6ヶ月以上必要と回答。
- **キーファクト:**
  - 64%の組織がAIエージェントで入社レベル採用変更（前期18%→64%）
  - 77%が採用困難を報告
  - 56%が新入社員に6ヶ月以上必要
  - CHROがCAIOとしてエージェント管理主導の傾向
- **引用URL:** https://kpmg.com/in/en/blogs/2026/06/agents-are-now-on-the-org-chart-who-is-managing-them.html
- **Evidence ID:** EVD-20260707-0045

### INFO-046
- **タイトル:** Microsoft Cuts 4,800 Jobs, Meta Cuts 8,000 in AI Restructuring
- **ソース:** Reuters / Fox Business / Washington Examiner
- **公開日:** 2026-07-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** Microsoft, Meta
- **要約:** MicrosoftがAI再編で4,800人削減。Xbox組織再構築。「AIによる置き換えではない」と主張。Metaは約8,000人削減、数千人をAIプロジェクトに再配属。ZuckerbergがAI開発が予想より遅いと認める。AIレイオフ逆転（再雇用）の警告: 仕事をマッピングしてから人を切るべき。
- **キーファクト:**
  - Microsoft: 4,800人削減（AI再構築、Xbox含む）
  - Meta: 約8,000人削減、数千人をAIに再配属
  - AIレイオフ逆転企業が現れる（再雇用トレンド）
  - Sam Altman, Zuckerberg, Brian Armstrong: AIが雇用を置換すると警告
- **引用URL:** https://www.reuters.com/business/world-at-work/companies-cutting-jobs-investments-shift-toward-ai-2026-07-06/
- **Evidence ID:** EVD-20260707-0046

### INFO-047
- **タイトル:** Junior Developer Employment Down 9-10% Within 6 Quarters of AI Adoption (Harvard)
- **ソース:** Ability.ai / Stanford Digital Economy Lab / Harvard Study
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** （複数）
- **要約:** Harvard研究: AIコーディングツール普及から6四半期以内にジュニア開発者雇用が9-10%低下。Stanford: 22-25歳ソフトウェア開発者の雇用が2022年後半ピークから約20%低下。ソフトウェア開発職はピークから約70%低下（中級・ジュニア職が中心）。企業がジュニア育成を停止。
- **キーファクト:**
  - ジュニア開発者雇用: AI普及6四半期以内に9-10%低下（Harvard）
  - 22-25歳開発者雇用: ピークから約20%低下（Stanford）
  - ソフトウェア開発職: ピークから約70%低下（中級・ジュニア中心）
  - GitHub Copilot CLI採用者: 24%多くPRをマージ
- **引用URL:** https://www.ability.ai/blog/junior-developer-pipeline-collapse-ai
- **Evidence ID:** EVD-20260707-0047

### INFO-048
- **タイトル:** Cursor: $100M → $2B Revenue in 13 Months, SpaceX Acquires for $60B
- **ソース:** New Market Pitch / Fortune / DevOps
- **公開日:** 2026-07-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02, KIQ-003-04
- **関連企業:** Cursor (SpaceX子会社), GitHub, Anthropic
- **要約:** Cursorが約13ヶ月で年率収益$1億→$20億に成長。エンタープライズソフトウェア成長の稀なクラス。25歳CEO Michael Truell。GitHub Copilot CLI採用者は24%多くPRマージ。Claude Code、Cursor、Copilot、Codex、Replit Agentがアジェンティックコーディングツール上位。
- **キーファクト:**
  - Cursor: $100M → $2B ARR（13ヶ月）
  - SpaceXが$60Bで買収
  - GitHub Copilot CLI採用者: 24%多くPRマージ
  - Claude Code成功率約70%（複雑な問題）
- **引用URL:** https://newmarketpitch.com/blogs/news/ai-code-assistant-cursor-overvalued
- **Evidence ID:** EVD-20260707-0048

### INFO-049
- **タイトル:** WEF+PwC: 40% of Workforce Need Reskilling, 40% of CEOs Hiring for AI
- **ソース:** WEF / GSMA
- **公開日:** 2026-07-02
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-03
- **関連企業:** （複数）
- **要約:** WEF+PwC共同報告: 労働力の40%（主に入社レベル）がAI向け新スキル必要。CEOの40%がAIのための採用を実施、51%が新AI職種を採用。AI経済は2030年までに1.7億の新規雇用を創出、9200万を破壊（WEF Future of Jobs Report）。リスキリング投資が差別化要因。
- **キーファクト:**
  - 40%の労働力がリスキリング必要（主に入社レベル）
  - 40%のCEOがAI採用、51%が新AI職種採用
  - 2030年: 1.7億新規雇用創出、9200万破壊
  - RAISE US: $5億以上でAI時代リスキリング基金開始
- **引用URL:** https://www.facebook.com/worldeconomicforum/posts/1472578304910403/
- **Evidence ID:** EVD-20260707-0049

### INFO-050
- **タイトル:** Gartner: Sacrificing Human Workers for AI Yields Zero Financial Gains
- **ソース:** Gartner / ScienceNaturePage
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03, KIQ-004-04
- **関連企業:** （複数）
- **要約:** Gartner新研究: 人間の労働者をAI投資のために犠牲にすることは、主要企業に財務的利益をもたらさない（ゼロ）。9割の雇用主が2030年までにAIがビジネスを根本的に変革すると予想。しかし18%のみが労働力の過半数にAIリスキリングを実施。AIスキル求人が170%増、テック職の4分の1がAI経験要求。
- **キーファクト:**
  - 人間→AI置換で財務利益ゼロ（Gartner）
  - 90%の雇用主が2030年までにAI根本変革を予想
  - AIスキル求人170%増
  - テック職の25%がAI経験要求
- **引用URL:** https://www.facebook.com/ScienceNaturePage/posts/1568819251365605/
- **Evidence ID:** EVD-20260707-0050

### INFO-051
- **タイトル:** Coding Skill Shift: "Context Engineering" Replaces "Prompt Engineering"
- **ソース:** Dev.to / Meta / LinkedIn
- **公開日:** 2026-07-04
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** Meta
- **要約:** コーディングスキルのパラダイムシフト。「プロンプトエンジニアリング」から「コンテキストエンジニアリング」へ。スキルは手書き実装から意図・制約・高レベル設計の表現へ移行。シニアエンジニアがAIエージェントで大幅生産性向上、ジュニアはパイプライン崩壊。メタスキル（AIへの指示設計）が新たな価値。
- **キーファクト:**
  - 「コンテキストエンジニアリング」が「プロンプトエンジニアリング」に取って代わる
  - シニアエンジニア: AIエージェントでフル機能・テスト・バグ修正を効率化
  - スキル: 手書き実装 → 意図・制約・高レベル設計の表現
  - AI関連IT職: 2018年から448%増、非AI IT職は9%減
- **引用URL:** https://dev.to/uiuxsatyam/frontend-development-in-2026-what-skills-are-becoming-obsolete-2b25
- **Evidence ID:** EVD-20260707-0051

### INFO-052
- **タイトル:** Dario Amodei at G7: AI Could Do "Most, Maybe All" of Software Engineering in 6-12 Months
- **ソース:** Quartz / G7 Summit
- **公開日:** 2026-07-01
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02, KIQ-004-02
- **関連企業:** OpenAI, Google DeepMind, Anthropic
- **要約:** Sam Altman、Demis Hassabis、Dario AmodeiがG7サミットに出席。Amodei: ソフトウェアエンジニアが行うことの「ほとんど、おそらく全て」を6-12ヶ月以内に行うモデルが近づく。Altman: AGIは「数千日以内」。Hassabis: AGIまで5-10年（2025年基準）。Amodei: 50%の雇用が5年以内にAIで置換される可能性。
- **キーファクト:**
  - Amodei: 6-12ヶ月以内にソフトウェアエンジニア業務の「ほとんど全て」をAIが実行
  - Altman: AGIは「数千日以内」
  - Hassabis: AGIまで5-10年（2025基準）、50-50でブレークスルー不要
  - Amodei: 50%の雇用が5年以内にAI置換の可能性
  - G7サミット: 3CEOがAI政策議論に出席
- **引用URL:** https://www.facebook.com/quartznews/posts/1380498553945959/
- **Evidence ID:** EVD-20260707-0052

### INFO-053
- **タイトル:** Yoshua Bengio vs Yann LeCun: AGI Safety Divide
- **ソース:** Instagram / Wikipedia / Facebook
- **公開日:** 2026-07-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02, KIQ-005-03
- **関連企業:** （複数）
- **要約:** AIのゴッドファーザー3人の分裂。Bengio: 放置すればAIが破滅的リスク、キラーロボット懸念、一時停止支持。LeCun: AGI概念を拒否（真の汎用知能は神話）、スケーリングでAGI到達に否定的。Hinton: リスク警告でBengioに同調。AGI定義のコンセンサス不在。
- **キーファクト:**
  - Bengio: AI破滅的リスク警告、一時停止支持
  - LeCun: AGI概念拒否（汎用知能は神話）
  - Hinton: Bengioに同調、リスク警告
  - AGI到達予測: 2027〜2040（Metaculus中央値）
  - GP Bullhound: 変革的AIが近づくとのコンセンサス拡大
- **引用URL:** https://www.instagram.com/reel/DaT_dBrzfyu/
- **Evidence ID:** EVD-20260707-0053

### INFO-054
- **タイトル:** Illinois AI Safety Law: Frontier Model Audits Required
- **ソース:** StateScoop
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** （複数）
- **要約:** イリノイ州Pritzker知事が全米で最も厳しいAI安全法に署名。最先端AIモデルの開発者に州レベル監視への新レベルの服従を要求。Big Techの「底辺への競争」を阻止するリーダーシップ。EU AI ActのGPAIルール（8月2日適用）と並ぶ規制圧力。UN AI科学パネルが多国間解決を要請。
- **キーファクト:**
  - イリノイ: 最先端AIモデル監査を義務付けるAI安全法
  - Pritzker知事: Big Tech「底辺への競争」阻止
  - UN AI科学パネル: 多国間AIガバナンス解決を要請
  - UN: 致死的自律兵器の国際法禁止を事務総長が要請
- **引用URL:** https://statescoop.com/illinois-ai-safety-law-audits-frontier-models/
- **Evidence ID:** EVD-20260707-0054

### INFO-055
- **タイトル:** Doubao Daily Tokens 180 Trillion (1500x Growth), MAU 345M
- **ソース:** OsChina / NetEase / Tencent News
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 豆包大模型の日次トークン使用量が180兆を突破（2024年5月比1500倍）。月活3.45億、日活1.4億。中国AIGC APP月活TOP: DeepSeek 1位(1.8億)、豆包2位(1億超)。豆包が6月末に有料機能を開始（オフィス・Agent向け）。Seed 2.1 Pro言語モデル、Seedance 2.5動画生成（30秒4K）を発表。
- **キーファクト:**
  - 日次トークン: 180兆（初期比1500倍）
  - 月活: 3.45億、日活: 1.4億
  - 中国AIGC APP月活: DeepSeek 1位(1.8億)、豆包2位
  - 豆包有料機能開始（オフィス・Agent向け）
  - Seed 2.1 Pro + Seedance 2.5(30秒4K)発表
- **引用URL:** https://www.oschina.net/news/341168
- **Evidence ID:** EVD-20260707-0055

### INFO-056
- **タイトル:** Doubao & Qwen Remove AI Agent Features July 15 - China Companion Rules
- **ソース:** Sina Finance / Yahoo HK Finance
- **公開日:** 2026-07-04
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-03
- **関連企業:** ByteDance, Alibaba
- **要約:** 豆包と通義千問が7月15日にAIエージェント（智能体）機能を同時下線。中国AIコンパニオン規則の施行によるもの。豆包: 下線後一定期間は情報閲覧可能、10月15日以降はプライバシーポリシーでデータ処理。ByteDanceが猫箱Appで新エージェント体験を推奨。豆包はタスクモード（快速・専門家・タスク）に機能再編。
- **キーファクト:**
  - 7月15日: 豆包・千問がAIエージェント機能同時下線
  - 原因: 中国AIコンパニオン規則施行
  - 豆包: タスクモード（快速・専門家・タスク）に再編
  - 10月15日以降: データをプライバシーポリシーで処理
  - 猫箱App代替推奨
- **引用URL:** https://finance.sina.com.cn/wm/2026-07-03/doc-inifqmqq0222637.shtml
- **Evidence ID:** EVD-20260707-0056

### INFO-057
- **タイトル:** Coze 3.0: Multi-Agent Collaboration Platform Launch
- **ソース:** CSDN / Sina / App Store
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceのCoze（扣子）が3.0バージョンに正式アップグレード。単一エージェントから「多人多Agent協作」プラットフォームへ進化。金融・自媒・医療・法律・科学研究のスキルパック提供。AI Nativeチーム協作の場へ。2026年AI智能体は普通人の日常に全面進入。
- **キーファクト:**
  - Coze 3.0: 多人多Agent協作プラットフォーム
  - 金融・自媒・医療・法律・科学研究スキルパック
  - AI Native チーム協作の場へ進化
  - 中国AI智能体: 豆包・Coze・通義千問・文心一言・元器・Kimi等
- **引用URL:** https://www.csdn.net/article/2026-07-02/162515534
- **Evidence ID:** EVD-20260707-0057

### INFO-058
- **タイトル:** Seedance 2.5: 30-Second 4K Video, 50 Reference Materials, 3D Rendering
- **ソース:** Threads / Instagram / DreamFace
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** Seedance 2.5が30秒映像生成、ネイティブ4K、最大50個の参照素材（従来12個）、3D白モデルレンダリングをサポート。AI版権商業化プラットフォーム同時推出。Seedance 2.0は4ヶ月前にハリウッド6大スタジオの著作権警告で全球上線を自停。Seed 2.1言語モデル家族も刷新、Seedream 5.0画像モデル発表。
- **キーファクト:**
  - Seedance 2.5: 30秒映像、ネイティブ4K
  - 最大50個の参照素材（2.0版は12個）
  - 3D白モデルレンダリング追加
  - AI版権商業化プラットフォーム
  - Seed 2.1 Pro + Seedream 5.0同時発表
- **引用URL:** https://www.threads.com/@thewillie.35/post/DaP88wbCdLr/
- **Evidence ID:** EVD-20260707-0058

### INFO-059
- **タイトル:** Kling AI Raises $3B (Valuation $18B), ByteDance Seedance Cannot Independently Finance
- **ソース:** Sina Finance / Sohu / EastMoney
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance, Kuaishou (Kling AI), Alibaba, Tencent, Baidu
- **要約:** 快手（Kuaishou）のKling AIが$30億調達（評価額$180億）。Tencent、Alibaba、Baiduが参投。投資家: ByteDanceのSeedanceは独立資金調達がほぼ不可能、Klingは数少ない投資対象。AI動画生成モデル企業として過去最大の単一資金調達。灵珠（TikTok天使投資家主導）も天使ラウンド完了、AI時代のTikTok目指す。
- **キーファクト:**
  - Kling AI: $30億調達、評価額$180億（AI動画生成で過去最大）
  - 投資家: Tencent, Alibaba, Baidu
  - ByteDance Seedance: 独立資金調達ほぼ不可能
  - 灵珠: TikTok天使投資家主導で天使ラウンド完了
- **引用URL:** https://finance.sina.com.cn/wm/2026-07-03/doc-inifqmqq0222637.shtml
- **Evidence ID:** EVD-20260707-0059

---

## 動的追加クエリ（Arbiter優先KIQ対応）

### 動的追加クエリ一覧
- KIQ-MIL-001（人間却下比率）: 2クエリ実行
- KIQ-GOV-002（安全性研究予算）: 1クエリ実行
- KIQ-ANT-002（Claude Code WAU/DAU）: 1クエリ実行
- KIQ-OAI-001（収益内訳: 政府vs民間）: 2クエリ実行
- KIQ-CAR-002-OPS（設計・評価・方向付け能力の定量市場価値）: 2クエリ実行
- KIQ-NEW-001（他社の5%株式提案への対応）: 2クエリ実行

### INFO-060
- **タイトル:** OpenAI 5% Government Stake: Alaska Permanent Fund Model Proposed
- **ソース:** Financial Times / Tom's Hardware / Yahoo Finance / ActuIA
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-NEW-001, KIQ-002-06
- **関連企業:** OpenAI, Google, Meta, Anthropic
- **要約:** OpenAIが米政府に5%株式（約$426億、評価額$8520億ベース）の提供を提案。Alaska Permanent Fundモデル（石油収入から住民に配当）をAI収入に適用する「AI配当」構想。他社（Google, Meta, Anthropic）にもマッチング5%を求めるが、いずれも参加を示唆していない。Tom's Hardware: 全ラボ構造はGoogle・Meta・Anthropicから株式を集めるが、参加の意思表示なし。
- **キーファクト:**
  - OpenAI 5%株式提案: 約$426億（評価額$852Bベース）
  - Alaska Permanent Fund型「AI配当」構想
  - 他社参加: Google・Meta・Anthropicいずれも参加示唆なし
  - GPT-5.6遅延直後に提案（Washington承認遅延との関連）
- **引用URL:** https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-floats-5-percent-government-stake-days-after-washington-delayed-gpt-5-6
- **Evidence ID:** EVD-20260707-0060

### INFO-061
- **タイトル:** OpenAI Financials: $13B Revenue vs $21B Losses (Structural Deficit)
- **ソース:** LinkedIn / Where's Your Ed / Yahoo Finance
- **公開日:** 2026-07-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001
- **関連企業:** OpenAI
- **要約:** OpenAI 2025年監査財務: 収益$130億（2024年$60億から増）、純損失$210億。2026年月次約$20億売上（年率~$240億）。計算コスト: 2026年Q1に$178億、総コスト約$440億。Anthropic+OpenAIで「AI収益$1100億」の68%を占める。政府vs民間収益内訳は依然非公開。2025年$390億損失（別報道）との矛盾あり、確定値要追跡。
- **キーファクト:**
  - 2025年収益: $130億（2024年$60億から）
  - 純損失: $210億（収益の1.6倍）
  - 2026年: 月次約$20億売上、Q1計算コスト$178億
  - 政府/民間収益内訳: 依然非公開（KIQ-OAI-001核心パラメータ不在継続）
  - 2027年中頃に資金枯渇リスク
- **引用URL:** https://www.linkedin.com/posts/sirojboboev_did-you-know-openai-makes-13b-in-revenue-activity-7478387005303750658-qDfp
- **Evidence ID:** EVD-20260707-0061

### INFO-062
- **タイトル:** Claude Code Usage: WAU Doubled, 30M MAU, 17% US Chatbot DAU Share
- **ソース:** Panto AI / FatJoe / ThunderBit
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-ANT-002
- **関連企業:** Anthropic
- **要約:** Claude Code週間アクティブユーザー（WAU）が2026年初頭から倍増。Anthropic $25億ランレート（2026年初）。月間アクティブユーザー3000万（2025年中盤、前年比40%増）。Claude USチャットボットDAUシェア: 2%未満→17%に急成長。84%の開発者がAIコーディングツール使用。ただし、Claude Code固有のWAU/DAU絶対値は依然非公開（15R連続不在継続）。
- **キーファクト:**
  - Claude Code WAU: 2026年初頭から倍増（絶対値は非公開）
  - Anthropicランレート: $25億（2026年初）
  - Claude MAU: 3000万（2025年中盤）
  - Claude US DAUシェア: 2%未満→17%（3ヶ月で）
  - Claude Code WAU/DAU絶対値: 依然非公開（15R連続不在）
- **引用URL:** https://www.getpanto.ai/blog/claude-ai-statistics
- **Evidence ID:** EVD-20260707-0062

### INFO-063
- **タイトル:** AI Skills Wage Premium: 56-62% Above Non-AI Workers (PwC)
- **ソース:** PwC / Instagram / ScienceDirect
- **公開日:** 2026-07-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-CAR-002-OPS
- **関連企業:** （複数）
- **要約:** PwC報告: AIスキルを持つ労働者が56-62%の賃金プレミアム。AI専門家の採用は前年比68.9%増。低スキル賃金は停滞、高スキル賃金は上昇（AI格差拡大）。AIエンジニアの米テック企業中央パッケージ: $245,000。大手では$60万〜$80万。中国AI新卒: 年俸350万元（約$48万）。AIガバナンス専門職: 年俸最大45ラク（インド）。
- **キーファクト:**
  - AIスキル賃金プレミアム: 56-62%（PwC）
  - AI専門家採用: 前年比68.9%増
  - AIエンジニア中央パッケージ: $245K（米）、$600K-$800K（大手）
  - 中国AI新卒: 350万元/年（約$48万）
  - 低スキル賃金停滞・高スキル上昇で格差拡大
- **引用URL:** https://www.facebook.com/PwCGR/posts/1615654157233113/
- **Evidence ID:** EVD-20260707-0063

### INFO-064
- **タイトル:** Pentagon-Anthropic: "Meaningful Human Oversight" Red Line + Grok in Project Maven
- **ソース:** WSJ / NewsFlip / Carnegie / ICRC
- **公開日:** 2026-07-02
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06
- **関連企業:** Anthropic, xAI (Grok), Pentagon
- **要約:** AnthropicのPentagon拒否2レッドライン: (1)完全自律型致死兵器システム（意味ある人間監督/human-in-the-loopなし）(2)国内監視。GrokがProject Mavenに統合済み（米政府法廷文書で開示）。Carnegie: 1人の人間オペレーターが平均90エージェントを制御→意味ある人間統制の実効性に疑義。ICRC: 戦争での迅速な決定が常に民間人の安全に寄与しない。人間却下比率（KIQ-MIL-001）の統計は分類情報として14R連続不在。
- **キーファクト:**
  - Anthropic 2レッドライン: (1)自律致死兵器human-in-the-loopなし (2)国内監視
  - Grok: Project Mavenに統合済み
  - Carnegie: 1オペレーター平均90エージェント制御（意味ある人間統制の疑義）
  - ICRC: AI軍事利用で民間人リスク上昇
  - KIQ-MIL-001（人間却下比率）: 14R連続完全不在（分類情報構造）
- **引用URL:** https://www.facebook.com/WSJ/posts/1393435822643011/
- **Evidence ID:** EVD-20260707-0064

### INFO-065
- **タイトル:** Anthropic Revenue Trajectory: $10M(2022) → $5B Run Rate(2025) → Early 2026
- **ソース:** X / HuffPost
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-GOV-002
- **関連企業:** Anthropic, Google DeepMind
- **要約:** Anthropic収益: $1000万(2022) → $10億(2024) → $50億ランレート(2025年中盤) → 2026年初。Google DeepMindから4人のトップ研究者（Nobel受賞者John Jumper含む）がAnthropicに移籍（歴史的頭脳流出）。安全性研究予算の経時的定量データ（KIQ-GOV-002）は25R連続未達成。AnthropicがFable 5の安全性評価に外部資金提供プログラムを開始。
- **キーファクト:**
  - Anthropic収益: $10M(2022) → $1B(2024) → $5B RR(2025) → early 2026
  - Google DeepMind→Anthropic: 4人トップ研究者移籍（John Jumper含む）
  - 安全性研究予算定量データ: 25R連続未達成
  - 外部安全性評価資金プログラム開始
- **引用URL:** https://x.com/mustufa4socials/article/2030289095730360722
- **Evidence ID:** EVD-20260707-0065

### INFO-066
- **タイトル:** SWE-bench Verified: Claude Sonnet 4.6 80.2%, ProgramBench 0% at Launch
- **ソース:** Vals AI / Snorkel AI / Anthropic
- **公開日:** 2026-07-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-CAR-002-OPS, KIQ-003-02
- **関連企業:** Anthropic, Meta
- **要約:** SWE-bench Verified: Claude Sonnet 4.6が80.2%（プロンプト修正時）、500タスクをDocker コンテナで実行。Llama3-SWE-RL-70Bは41.0%。ProgramBench: 全フロンティアモデルがローンチ時0%（FFmpeg・SQLite・PHPインタプリタの再構築テスト）。MirrorCode: AIが動作のみからプログラム全体を再構築可能、長期間タスク完了能力を実証。
- **キーファクト:**
  - SWE-bench Verified: Claude Sonnet 4.6 80.2%
  - Llama3-SWE-RL-70B: 41.0%（SWE-bench Verified）
  - ProgramBench: 全フロンティアモデル0%（ローンチ時）
  - MirrorCode: AIが動作のみからプログラム全体再構築可能
- **引用URL:** https://vals.ai/benchmarks/swebench
- **Evidence ID:** EVD-20260707-0066

---

## Step 4: 深掘りスクレイプ（重要記事3件）

### INFO-067
- **タイトル:** Carnegie: Autonomous Cyber Operations & Europe's Governance Gap（深掘りスクレイプ）
- **ソース:** Carnegie Endowment for International Peace
- **公開日:** 2026-07-01
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, Microsoft, Google, OpenAI
- **要約:** Carnegie Endowmentの詳細レポート。Moltbook（AIエージェント向けSNS）が暴露データベースでAPI鍵漏洩。2025年11月: 中国関連グループがAnthropic Claudeを外国政府・重要インフラ攻撃に使用（公に報告された初の大規模LLMサイバー攻撃）。2026年2月: 米国防長官がAnthropicにClaude無制限軍事アクセスを要求（$200M契約失効脅迫）。Microsoft 365 Copilot Chat バグで機密メール要約が数週間漏洩。Trump政権サイバー戦略（2026年3月）: AIエージェントによるネットワーク防衛・妨害を推進。EUの認証フレームワークはエージェントAIに不十分。
- **キーファクト:**
  - Moltbook: AIエージェントSNS、データベース漏洩でAPI鍵暴露
  - Anthropic Claude使用: 初の公表された大規模LLMサイバー攻撃（中国関連、2025年11月）
  - 国防長官 Anthropic要請: Claude軍事アクセス要求、$200M契約失効脅迫（2026年2月）
  - Microsoft Copilot バグ: 機密メール要約漏洩（2026年2月）
  - Trumpサイバー戦略: エージェントAI防衛推進（2026年3月）
  - Anthropic Fable 5・Mythos 5: 米輸出管理令で外国人全アクセス停止
- **引用URL:** https://carnegieendowment.org/research/2026/07/when-ai-agents-attack-autonomous-cyber-operations-and-europes-governance-gap
- **Evidence ID:** EVD-20260707-0067

### INFO-068
- **タイトル:** "The AI Industry Is Losing" - Ed Zitron 詳細財務分析（深掘りスクレイプ）
- **ソース:** Where's Your Ed At (Ed Zitron)
- **公開日:** 2026-06-30
- **信頼性コード:** D-2
- **関連KIQ:** KIQ-OAI-001, KIQ-ANT-002
- **関連企業:** OpenAI, Anthropic, Microsoft, Meta, CoreWeave, NVIDIA
- **要約:** AI業界の構造的赤字を詳細分析。OpenAI: 2025年に$17.2B Microsoft Azure支払、$20.9B純損失（$13.04B収益）。ハイパースケーラーのcapexは2026年Q3にキャッシュフローを超過。Microsoft AI収益ランレート$37B/年（月$3.08B）だが、capex月$31.9Bの1/10未満。OpenAIがMicrosoft AI収益の約70%を占める。CoreWeave収益の65%がMicrosoft（OpenAI向け）+NVIDIA。2030年までに$2T新規収益が必要。BIS警告: capexブームが投資バストに転じるリスク。
- **キーファクト:**
  - OpenAI Azure支払: $17.2B/年（2025年）
  - OpenAI純損失: $20.9B（2025年、収益$13.04B）
  - Microsoft AI収益ランレート: $37B/年、capexの1/10未満
  - OpenAI = Microsoft AI収益の~70%
  - CoreWeave収益の65%: Microsoft(OpenAI)+NVIDIA
  - 必要新規収益: 2030年までに$2T
  - ハイパースケーラーcapex > キャッシュフロー（2026年Q3〜）
- **引用URL:** https://www.wheresyoured.at/the-ai-industry-is-losing/
- **Evidence ID:** EVD-20260707-0068

### INFO-069
- **タイトル:** AI Sovereign Wealth Fund: Altman Proposal Analysis（深掘りスクレイプ）
- **ソース:** ActuIA
- **公開日:** 2026-07-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-NEW-001, KIQ-002-06
- **関連企業:** OpenAI, Google, Anthropic, Meta, xAI, Nvidia, Micron, AMD
- **要約:** OpenAIの5%株式提案の詳細分析。FT報道: AltmanがTrump大統領、Lutnick商務長官、Bessent財務長官と直接協議。Alaska Permanent Fund（1976年設立、$80B超）モデルでAI収入の配当を市民に分配。Altmanは2025年初頭にTrumpに構想提示、2026年4月に「公共富裕基金」概念を公表。AnthropicはForbes引用で「株式譲渡協議していない」と否定。Bernie Sanders議員は大手AI企業の50%公的持ち分を要求。実現には議会法成立が必要。欧米の対比: 米国は「所有」による主権、欧州は「規制」による主権。
- **キーファクト:**
  - FT情報源: 「概念的」「初期段階」の議論（確定ではない）
  - Altman協議相手: Trump大統領、Lutnick商務長官、Bessent財務長官
  - Alaska Permanent Fund: 1976年設立、$80B超、毎年住民に配当
  - 想定対象企業: Google, Anthropic, Meta, xAI（半導体:Nvidia, Micron, AMDも追加報道）
  - Anthropic: 「株式譲渡協議していない」（Forbes引用）
  - Bernie Sanders: 大手AI企業50%公的持ち分要求
  - 実現障壁: 議会法成立が必要
  - 欧州の対比: 規制による距離維持 vs 米国の所有による利益一致
- **引用URL:** https://www.actuia.com/en/news/the-ai-sovereign-wealth-fund-what-altmans-proposal-reveals-about-the-us-state-industry-relationship/
- **Evidence ID:** EVD-20260707-0069
