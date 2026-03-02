# 収集データ: 2026-03-02

## メタデータ
- 収集日時: 2026-03-02 00:30 UTC
- 実行クエリ数: 61 / 56（+5動的追加）
- scrape実行数: 4件
- 収集情報数: 84件
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 動的追加KIQ: KIQ-RED-001 ✓, KIQ-RED-005 ✓, KIQ-RED-006 ✓, KIQ-RED-007 ✓
- 品質フラグ: NORMAL
- 特記事項: Anthropic SCR指定・OpenAI国防総省契約が重要ニュース（KIQ-002-06）

## 収集結果

### INFO-001
- **タイトル:** Statement on the comments from Secretary of War Pete Hegseth
- **ソース:** Anthropic (公式)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** Anthropic
- **要約:** Secretary of War Pete HegsethがAnthropicをサプライチェーンリスク(Supply Chain Risk)に指定すると発表。これは米国企業に対して公に適用された前例のない措置。Anthropicは2つの例外（米国人への大量監視、完全自律型兵器）で交渉が決裂したと説明。法的に争う姿勢。
- **キーファクト:**
  - SCR指定は歴史的に米国の敵対国向けに予約された措置であり、米国企業への公的適用は前例なし
  - 例外事項: (1)米国人への大量国内監視 (2)完全自律型兵器の2点
  - 商業契約・個人は影響なし、DoW契約業務のみ影響
- **引用URL:** https://www.anthropic.com/news/statement-comments-secretary-war

### INFO-002
- **タイトル:** Claude's new constitution
- **ソース:** Anthropic (公式)
- **公開日:** 2026-01-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03（AGI安全性・ガバナンス）
- **関連企業:** Anthropic
- **要約:** AnthropicがClaudeの新しい憲法(Constitution)を公開。CC0ライセンスで誰でも自由に使用可能。原則のリスト形式から、文脈と理由を説明する包括的文書に進化。
- **キーファクト:**
  - 4つの優先順位: (1)安全性 (2)倫理 (3)ガイドライン準拠 (4)有用性
  - Constitutional AI手法の進化版、合成トレーニングデータ生成にも使用
  - Claudeの意識・道徳的地位についての不確実性を認識
- **引用URL:** https://www.anthropic.com/news/claude-new-constitution

### INFO-003
- **タイトル:** Powering the next generation of AI development with AWS
- **ソース:** Anthropic (公式)
- **公開日:** 2024-11-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01（クラウドプロバイダー統合）
- **関連企業:** Anthropic, Amazon/AWS
- **要約:** AWSとの提携拡大を発表。Amazonから新たに40億ドル投資、総額80億ドルに。AWSが主要クラウド・トレーニングパートナーに。Trainiumハードウェア協業。
- **キーファクト:**
  - Amazon総投資額: 80億ドル（少数株主維持）
  - AWS GovCloud、Secret/Top SecretリージョンでのClaude提供
  - Pfizer、Intuit、Perplexity、欧州議会などの事例
- **引用URL:** https://www.anthropic.com/news/anthropic-amazon-trainium

### INFO-004
- **タイトル:** Grok-2 Beta Release
- **ソース:** xAI (公式)
- **公開日:** 2024-08-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02（ベンチマーク性能）
- **関連企業:** xAI
- **要約:** Grok-2とGrok-2 miniをリリース。LMSYS Chatbot ArenaでClaude 3.5 SonnetとGPT-4-Turboを上回る。Enterprise APIも提供開始。
- **キーファクト:**
  - GPQA 56.0%, MMLU 87.5%, MATH 76.1%, HumanEval 88.4%
  - FLUX.1モデルとの統合で画像生成
  - マルチリージョン推論デプロイメント対応API
- **引用URL:** https://x.ai/news/grok-2

### INFO-005
- **タイトル:** AI SDK v6 - Agent API, Structured Output & New Features
- **ソース:** AI SDK Agents
- **公開日:** 2026-02-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）
- **関連企業:** OpenAI
- **要約:** AI SDK v6がAgent() API、強化された構造化出力、高度なツールパターンを導入。
- **キーファクト:**
  - Agent() API新設
  - 構造化出力の強化
  - 高度なツールパターン対応
- **引用URL:** https://www.aisdkagents.com/explore/ai-sdk-v6

### INFO-006
- **タイトル:** Claude Code 2.1.63 with 26 CLI changes
- **ソース:** Reddit (公式発表転載)
- **公開日:** 2026-02-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Code 2.1.63をリリース。26のCLI変更と6つのフラグ変更。Task toolがAgent toolに置き換え。
- **キーファクト:**
  - 26 CLI変更、6フラグ変更
  - Task tool → Agent tool置き換え
  - Explore guidance更新
- **引用URL:** https://www.reddit.com/r/ClaudeCode/comments/1rgwctt/

### INFO-007
- **タイトル:** The Intelligent OS: Making AI agents more helpful for Android apps
- **ソース:** Android Developers Blog (Google)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）
- **関連企業:** Google
- **要約:** AppFunctionsを通じてGeminiがカレンダー、メモ、タスクアプリでタスク自動化を可能に。複数メーカーのデバイス対応。
- **キーファクト:**
  - AppFunctionsでアプリ間自動化
  - カレンダー、メモ、タスクカテゴリ対応
  - 複数メーカーデバイス対応
- **引用URL:** https://android-developers.googleblog.com/2026/02/the-intelligent-os-making-ai-agents.html

### INFO-008
- **タイトル:** Grok 4.20: Multi-Agent System for Faster, More Accurate Answers
- **ソース:** LinkedIn
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）
- **関連企業:** xAI
- **要約:** xAIがGrok 4.20をリリース。1つのモデルが推測するのではなく、4つの専門化されたエージェントが並列で動作するアーキテクチャ。
- **キーファクト:**
  - 4つの専門化エージェントが並列動作
  - Grok 420 Early Access、Grok 420 Multi-AgentがAPIに追加予定
  - 従来の単一モデルからマルチエージェントアーキテクチャへ転換
- **引用URL:** https://www.linkedin.com/posts/davidelkington_grok-doesnt-answer-your-question-anymore-activity-7431722149956026368-6VMM

### INFO-009
- **タイトル:** Doubao 2.0 released for "agent era"
- **ソース:** Instagram/ByteDance
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）
- **関連企業:** ByteDance
- **要約:** ByteDanceがDoubao 2.0を正式リリース。エージェント時代向けに設計されたアップグレード版。Seedance 2.0（動画生成ツール）も更新。
- **キーファクト:**
  - Doubao 2.0: エージェント時代向け設計
  - Seedance 2.0: 動画生成ツール更新（有料版のみ）
  - 中国市場向けAIエコシステム拡大
- **引用URL:** https://www.instagram.com/p/DVIeJVdDEac/

### INFO-010
- **タイトル:** Top 5 AI Agent Frameworks In 2026
- **ソース:** Intuz
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）
- **関連企業:** （業界全体）
- **要約:** 2026年の主要AIエージェントフレームワーク: LangGraph、Microsoft AutoGen、CrewAI、OpenAgents、MetaGPT。
- **キーファクト:**
  - 1位: LangGraph 2位: Microsoft AutoGen 3位: CrewAI 4位: OpenAgents 5位: MetaGPT
  - エンタープライズ向けGraphBit新世代インフラ
  - Vercel AI SDK + Next.jsが自前構築で人気
- **引用URL:** https://www.intuz.com/blog/top-5-ai-agent-frameworks-2025

### INFO-011
- **タイトル:** What fails first in AI automation is execution, not model quality
- **ソース:** Reddit r/SaaS
- **公開日:** 2026-02
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）
- **関連企業:** （業界全体）
- **要約:** 本番環境でLLMワークフローを実行するSaaSチームで、最初の重大インシデントは「モデルの回答品質」ではなく「実行失敗」であることが判明。
- **キーファクト:**
  - 本番インシデントの主因は実行失敗（モデル品質ではない）
  - SLA監視が重要
  - エンタープライズAIエージェントのアーキテクチャガイド公開
- **引用URL:** https://www.reddit.com/r/SaaS/comments/1rchefk/what_fails_first_in_ai_automation_is_usually/

### INFO-012
- **タイトル:** Anthropic Trust Center - SOC 2 Type II, HIPAA attestation updated
- **ソース:** Anthropic (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02（エンタープライズ展開）
- **関連企業:** Anthropic
- **要約:** AnthropicがTrust Centerで最新のコンプライアンス資料を公開。SOC 2 Type II、HIPAAアテステーションを更新。
- **キーファクト:**
  - SOC 2 Type IIレポート更新
  - HIPAAアテステーション追加
  - Claude Code Security: Enterprise/Team向け限定研究プレビュー
- **引用URL:** https://trust.anthropic.com/updates

### INFO-013
- **タイトル:** Claude Code Security rollout is an industry wakeup call
- **ソース:** CSO Online
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02（エンタープライズ展開）
- **関連企業:** Anthropic
- **要約:** AnthropicのClaude Code Securityが業界の注目を集める。AIモデルを使用してコードベースをスキャンし、重大な脆弱性を特定。
- **キーファクト:**
  - AI推論によるコードベースセキュリティスキャン
  - メモリ安全性問題など高重大度脆弱性を特定
  - Enterprise/Team向け限定研究プレビュー
- **引用URL:** https://www.csoonline.com/article/4136294/anthropics-claude-code-security-rollout-is-an-industry-wakeup-call.html

### INFO-014
- **タイトル:** Vertex AI Agent Engine enterprise security features
- **ソース:** Google Cloud (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02（エンタープライズ展開）
- **関連企業:** Google
- **要約:** Vertex AI Agent Engineがエンタープライズセキュリティ機能を追加。プライベートVPC環境へのデプロイ、Private Service Connect設定をサポート。
- **キーファクト:**
  - プライベートVPC環境へのエージェントデプロイ可能
  - Private Service Connect設定
  - Vertex AI SLA付きAPI提供
- **引用URL:** https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes

### INFO-015
- **タイトル:** Deloitte: AI adoption with CIBC achieved 90% developer adoption
- **ソース:** Deloitte
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02（エンタープライズ展開）
- **関連企業:** （業界全体）
- **要約:** DeloitteとCIBCの協業で、人中心の採用アプローチにより90%の開発者採用率と10-14%の生産性向上を達成。
- **キーファクト:**
  - CIBC協業: 90%開発者採用率
  - 10-14%生産性向上
  - 人中心の採用アプローチが有効
- **引用URL:** https://www.deloitte.com/ca/en/Industries/financial-services/perspectives/ai-adoption-roi-success.html

### INFO-016
- **タイトル:** TELUS: $600M+ in AI Benefits with 53,000 copilots
- **ソース:** TELUS Digital
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02（エンタープライズ展開）
- **関連企業:** （業界全体）
- **要約:** TELUSがAI採用を促進し、53,000のコパイロットをデプロイ。6億ドル以上のAI利益を実現。
- **キーファクト:**
  - 53,000コパイロットデプロイ
  - $600M+のAI利益
  - 責任あるAIをビジネス価値に変換
- **引用URL:** https://www.telusdigital.com/insights/data-and-ai/resource/democratizing-enterprise-ai

### INFO-017
- **タイトル:** Obsidian Security Achieves ISO/IEC 42001:2023 Certification for AI Governance
- **ソース:** Obsidian Security
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02（エンタープライズ展開）
- **関連企業:** （業界全体）
- **要約:** Obsidian SecurityがAIガバナンスに関するISO/IEC 42001:2023認証を取得。責任あるAI開発への取り組みを反映。
- **キーファクト:**
  - ISO/IEC 42001:2023認証取得
  - AIガバナンス認証の重要性増加
  - AIセキュリティ認証プログラム拡大
- **引用URL:** https://www.obsidiansecurity.com/news/obsidian-security-achieves-iso-iec-42001-2023-certification-for-ai-governance

### INFO-018
- **タイトル:** ADK Integrations Ecosystem with Hugging Face and GitHub
- **ソース:** Google Developers Blog
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）
- **関連企業:** Google
- **要約:** GoogleがADK統合エコシステムを発表。Hugging Face、GitHubと連携し、強力なAIエージェント構築を支援。Daytonaでコード実行環境も提供。
- **キーファクト:**
  - Hugging Face、GitHubとの統合
  - Daytona: コード実行環境
  - 開発ツールへの直接接続
- **引用URL:** https://developers.googleblog.com/supercharge-your-ai-agents-adk-integrations-ecosystem/

### INFO-019
- **タイトル:** AI Agents are delivering real ROI — 1,100 developers survey
- **ソース:** VentureBeat
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）
- **関連企業:** （業界全体）
- **要約:** DigitalOceanの2026 Currents調査で、60%がアプリケーションとエージェントがAIスタックで最大の長期価値を持つと回答。
- **キーファクト:**
  - 1,100人の開発者/CTO調査
  - 60%がアプリとエージェントに最大価値を見出す
  - エージェントのROIが実証されつつある
- **引用URL:** https://venturebeat.com/orchestration/ai-agents-are-delivering-real-roi-heres-what-1-100-developers-and-ctos

### INFO-020
- **タイトル:** Model Context Protocol is suddenly on every executive agenda
- **ソース:** CIO.com
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）
- **関連企業:** Anthropic
- **要約:** MCP（Model Context Protocol）が経営層のアジェンダに急浮上。MCPサーバーは認証・信頼される必要があり、ガバナンスポリシーがプロトコル層に近づく必要がある。
- **キーファクト:**
  - MCP: AIアプリとデータソース接続の標準化
  - 企業のMCP採用がセキュリティコントロールを上回るペース
  - 「AIアプリのUSB-C」と呼ばれる
- **引用URL:** https://www.cio.com/article/4136548/why-model-context-protocol-is-suddenly-on-every-executive-agenda.html

### INFO-021
- **タイトル:** Agentic AI Foundation grows to 146 members
- **ソース:** Techzine
- **公開日:** 2026-02-24
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）
- **関連企業:** （業界全体）
- **要約:** Agentic AI Foundation（AAIF）が146メンバーに拡大。18の新規Gold Member、79の新規Silver Memberを追加。MCPの本拠地として機能。
- **キーファクト:**
  - AAIF: 146メンバー（+97新規）
  - UiPathがAAIFに参加、MCP採用
  - オープンで協調的なエージェント標準化を推進
- **引用URL:** https://www.techzine.eu/news/applications/139057/agentic-ai-foundation-the-home-of-mcp-grows-to-146-members/

### INFO-022
- **タイトル:** Agent Skills: Microsoft, OpenAI, Atlassian, Figma, Cursor, GitHub all support
- **ソース:** Medium
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）
- **関連企業:** OpenAI, Microsoft
- **要約:** Agent Skillsが主要プラットフォームで標準化。Microsoft、OpenAI、Atlassian、Figma、Cursor、GitHubが対応。GitHub Copilotがネイティブサポートを追加。
- **キーファクト:**
  - 主要6社がAgent Skills標準をサポート
  - $skill-creator、$skill-installerスキル
  - Figmaスキル: デザインを本番UIコードに変換
- **引用URL:** https://jinlow.medium.com/agent-skills-the-hidden-architecture-powering-ais-next-evolution-9ada610d4ef2

### INFO-023
- **タイトル:** OpenAI and Amazon announce strategic partnership
- **ソース:** OpenAI/Amazon (公式)
- **公開日:** 2026-02-23
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）
- **関連企業:** OpenAI, Amazon/AWS
- **要約:** OpenAIとAmazonが戦略的パートナーシップを発表。OpenAIのFrontierプラットフォームをAWSに提供。Amazon BedrockでStateful Runtime Environmentを共同開発。
- **キーファクト:**
  - OpenAI FrontierをAWSで提供
  - Bedrock上でStateful Runtime Environment共同開発
  - カスタムモデル、エンタープライズAI拡大
- **引用URL:** https://openai.com/index/amazon-partnership/

### INFO-024
- **タイトル:** OpenAI partners with McKinsey, BCG, Accenture, Capgemini
- **ソース:** Fortune
- **公開日:** 2026-02-23
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）
- **関連企業:** OpenAI
- **要約:** OpenAIがMcKinsey、BCG、Accenture、Capgeminiとパートナーシップ。コンサルタントがクライアントのワークフロー再設計とAIエージェント統合を支援。
- **キーファクト:**
  - 4大コンサルティングファームと提携
  - Frontier AIエージェントプラットフォームを推進
  - ワークフロー再設計とエージェント統合
- **引用URL:** https://fortune.com/2026/02/23/openai-partners-with-mckinsey-bcg-accenture-and-capgemini-to-push-its-frontier-ai-agent-platform/

### INFO-025
- **タイトル:** Intuit and Anthropic Partner for Financial Intelligence
- **ソース:** Intuit (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）
- **関連企業:** Anthropic, Intuit
- **要約:** IntuitとAnthropicがパートナーシップ。Claudeを活用した信頼できる金融インテリジェンスとカスタムAIエージェントを消費者・企業に提供。ミッドマーケット企業が安全なカスタマイズ可能なAIエージェントを構築可能に。
- **キーファクト:**
  - Claudeベースの金融インテリジェンス
  - ミッドマーケット向けカスタムAIエージェント
  - 業界特化のニーズに対応
- **引用URL:** https://investors.intuit.com/news-events/press-releases/detail/1305/intuit-and-anthropic-partner-to-bring-trusted-financial-intelligence-and-custom-ai-agents-to-consumers-and-businesses

### INFO-026
- **タイトル:** OpenAI Codex Multi-agents - spawning specialized agents in parallel
- **ソース:** OpenAI Developers (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）
- **関連企業:** OpenAI
- **要約:** Codexがマルチエージェントワークフローを実行可能に。専門化されたエージェントを並列で起動し、結果を1つのレスポンスに統合。gpt-realtimeモデルで音声品質向上。
- **キーファクト:**
  - 専門化エージェントの並列起動
  - gpt-realtimeモデル: 音声品質・ツール呼び出し改善
  - 長期・バックグラウンドタスク実行対応
- **引用URL:** https://developers.openai.com/codex/concepts/multi-agents/

### INFO-027
- **タイトル:** OpenAI AI Devices: $200-300 camera smart speaker by Feb 2027
- **ソース:** TeckNexus
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）
- **関連企業:** OpenAI
- **要約:** OpenAIがAIネイティブハードウェアを計画。2027年2月までに$200-300のカメラ付きスマートスピーカーを投入し、アンビエント・マルチモーダルアシスタンスを提供。
- **キーファクト:**
  - カメラ付きスマートスピーカー: $200-300
  - 2027年2月投入予定
  - アンビエント・マルチモーダルアシスタンス
- **引用URL:** https://tecknexus.com/openai-ai-devices-multimodal-hardware-roadmap/

### INFO-028
- **タイトル:** Gemini Robotics Preview - embodied reasoning for robotic agents
- **ソース:** Google AI (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）
- **関連企業:** Google
- **要約:** Gemini Robotics Previewが公開。物理空間を理解し、ロボットエージェントのマルチステップタスク計画を行う高度な身体性推論モデル。Gemini Live APIでリアルタイム音声・動画対話も可能。
- **キーファクト:**
  - 物理空間理解・ロボットエージェント計画
  - Gemini Live API: 低レイテンシリアルタイム対話
  - Gemini 3.1 Pro: マルチモーダルAI・エージェント向け
- **引用URL:** https://ai.google.dev/gemini-api/docs/models

### INFO-029
- **タイトル:** Microsoft Foundry Browser Automation for AI agents
- **ソース:** Microsoft Learn (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）
- **関連企業:** Microsoft
- **要約:** Microsoft Foundryでブラウザ自動化ツールをAIエージェントに統合。BrowserAutomationAgentToolで同期・非同期操作をサポート。
- **キーファクト:**
  - BrowserAutomationAgentTool提供
  - 同期・非同期ブラウザ操作
  - Amazon Nova Actもブラウザ自動化で注目
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/browser-automation

### INFO-030
- **タイトル:** WebMCP: AI Agent Browser Interaction
- **ソース:** Medium
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）
- **関連企業:** （業界全体）
- **要約:** WebMCPはWebサイトが推測されるのではなく、構造化ツールとして能力を能動的に公開できるようにする。AIエージェントのブラウザ対話を改善。
- **キーファクト:**
  - Webサイトの能力を構造化ツールとして公開
  - エージェントの推測ではなく明示的インターフェース
  - Browser Use: 人間のようにWebをナビゲート
- **引用URL:** https://jinlow.medium.com/webmcp-ai-agent-browser-interaction-f86838a564ec

### INFO-031
- **タイトル:** Gemini 3.1 Pro: 77.1% ARC-AGI-2, Most Powerful AI Model
- **ソース:** Medium
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）
- **関連企業:** Google
- **要約:** Gemini 3.1 Proが独立ベンチマークで全AIモデルを上回る。ARC-AGI-2で77.1%（前世代の31.1%から2.5倍）。1Mトークンコンテキスト、ネイティブマルチモーダル。
- **キーファクト:**
  - ARC-AGI-2: 77.1%（前世代31.1%から2.5倍）
  - Terminal-Bench 2.0: 77.3%リード
  - SWE-Bench Pro: 56.8%
  - 1Mトークンコンテキスト
- **引用URL:** https://medium.com/ai-tomorrow/google-just-dethroned-every-ai-meet-gemini-3-1-pro-the-most-powerful-ai-model-on-earth-right-now-d387371ce195

### INFO-032
- **タイトル:** Long horizon tasks with Codex - Shell + Skills + Compaction
- **ソース:** OpenAI Developers (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05（スキル配布・実行環境）
- **関連企業:** OpenAI
- **要約:** Codexでの長期実行エージェント構築のベストプラクティス。Shell + Skills + Compactionの組み合わせ。ターミナルコマンドはshellツール、プラン/TODOはupdate_planツールを使用。
- **キーファクト:**
  - Shell + Skills + Compactionの組み合わせ
  - shellツール: ターミナルコマンド
  - update_planツール: プラン/TODO管理
  - サンドボックス実行環境が重要
- **引用URL:** https://developers.openai.com/cookbook/examples/codex/long_horizon_tasks/

### INFO-033
- **タイトル:** Claude Code Security finds 500+ vulnerabilities in sandboxed VM
- **ソース:** VentureBeat
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05（スキル配布・実行環境）
- **関連企業:** Anthropic
- **要約:** AnthropicがClaudeをサンドボックス仮想マシン内に配置し、標準ユーティリティと脆弱性分析ツールで500以上の脆弱性を発見・検証。MCPで外部ツール・サービスに接続。
- **キーファクト:**
  - 500+脆弱性を発見・検証
  - サンドボックス仮想マシン環境
  - MCP: 外部ツール・データソースへのブリッジ
- **引用URL:** https://venturebeat.com/security/anthropic-claude-code-security-reasoning-vulnerability-hunting

### INFO-034
- **タイトル:** Building Agent Skills with Gemini CLI skill-creator
- **ソース:** danicat.dev
- **公開日:** 2026-02-27
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05（スキル配布・実行環境）
- **関連企業:** Google
- **要約:** Gemini CLIのskill-creatorを使用して、カスタムAgent Skillsを自動生成・洗練・構造化する方法。自然言語プロンプト、スクリプティング、自動化をサポート。
- **キーファクト:**
  - skill-creator: カスタムスキル自動生成
  - コンテキスト、権限、メモリ、拡張機能の完全制御
  - コード説明、デバッグ、コンテンツ生成
- **引用URL:** https://danicat.dev/posts/20260227-gemini-cli-skills-part-2/

### INFO-035
- **タイトル:** Agent Skills vs MCP - marketplace growth
- **ソース:** GitHub/Medium
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05（スキル配布・実行環境）
- **関連企業:** （業界全体）
- **要約:** Agent Skillsはワークフロー・能力に焦点、MCPはセキュアで構造化されたデータ・ツールアクセスに焦点。スキルマーケットプレースのアイデアが議論され、AI Agent Storeなどが登場。
- **キーファクト:**
  - Agent Skills: ワークフロー・能力
  - MCP: セキュアなデータ・ツールアクセス
  - AI Agent Store: エージェントマーケットプレース登場
- **引用URL:** https://github.com/skillmatic-ai/awesome-agent-skills

### INFO-036
- **タイトル:** The 2026 AI Cost Crisis - One API Aggregation Platforms 80% savings
- **ソース:** Press Release
- **公開日:** 2026-02
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-05（スキル配布・実行環境）
- **関連企業:** （業界全体）
- **要約:** One API統合プラットフォームが統合コストを最大80%削減し、サプライヤーロックインに対する耐性を強化。OpenAI vs Anthropicのベンダーロックイン隠れコストが問題化。
- **キーファクト:**
  - 統合コスト最大80%削減可能
  - サプライヤーロックイン耐性強化
  - ベンダーロックインの隠れコスト問題
- **引用URL:** https://www.pressconnects.com/press-release/story/37419/the-2026-ai-cost-crisis-the-rise-of-one-api-aggregation-platforms-and-their-potential-to-deliver-80-savings/

### INFO-037
- **タイトル:** Introducing Stateful Runtime Environment for Agents in Amazon Bedrock
- **ソース:** OpenAI/Amazon (公式)
- **公開日:** 2026-02-23
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01（クラウドプロバイダー統合）
- **関連企業:** OpenAI, Amazon/AWS
- **要約:** Amazon BedrockでOpenAIモデルを使用したStateful Runtime Environment for Agentsを提供。永続的オーケストレーション、メモリ、セキュア実行をマルチステップAIワークフローにもたらす。
- **キーファクト:**
  - 永続的オーケストレーション
  - メモリ管理
  - セキュア実行環境
  - OpenAIモデル活用
- **引用URL:** https://openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/

### INFO-038
- **タイトル:** Microsoft Foundry - unified Azure platform for enterprise AI
- **ソース:** Microsoft (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01（クラウドプロバイダー統合）
- **関連企業:** Microsoft
- **要約:** Microsoft Foundryは、エンタープライズAI運用、モデルビルダー、アプリケーション開発のための統合Azure PaaS。AIゲートウェイ接続でAzure API Managementや非Azureホストモデルも利用可能。
- **キーファクト:**
  - 統合Azure PaaS
  - エンタープライズAI運用
  - AIゲートウェイ接続対応
  - Azure AI成長率39% YoY
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry

### INFO-039
- **タイトル:** Vertex AI Agent Builder with ADK Memory Bank
- **ソース:** Google Cloud (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01（クラウドプロバイダー統合）
- **関連企業:** Google
- **要約:** Vertex AI Agent BuilderがADK（Agent Development Kit）でMemory Bankをサポート。長期メモリ管理、Google Cloudツールへの直接アクセス、デプロイオファリングを提供。
- **キーファクト:**
  - ADK Memory Bankで長期メモリ管理
  - Google Cloudツール直接アクセス
  - セッション管理
  - エージェント構築・スケーリング・ガバナンス
- **引用URL:** https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/quickstart-adk

### INFO-040
- **タイトル:** 40% of Enterprise Apps Will Embed AI Agents by End of 2026
- **ソース:** Yahoo Finance
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01（クラウドプロバイダー統合）
- **関連企業:** （業界全体）
- **要約:** 2025年は5%のエンタープライズアプリのみがAIエージェントを統合していたが、2026年末までに40%に達すると予測。AWS 30%シェア、Azure AI 39%成長。
- **キーファクト:**
  - 2025年: 5%統合 → 2026年末: 40%予測
  - AWS: 30%クラウドシェア
  - Azure AI: 39% YoY成長
- **引用URL:** https://finance.yahoo.com/news/40-enterprise-apps-embed-ai-181310288.html

### INFO-041
- **タイトル:** OpenAI Our agreement with the Department of War
- **ソース:** OpenAI (公式)
- **公開日:** 2026-02-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** OpenAI
- **要約:** OpenAIが国防総省（Department of War）との契約詳細を公開。安全性レッドライン、法的保護、分類された軍事ネットワークでのAIシステム展開方法を説明。「国内大量監視の禁止」「武力使用への人間の責任」を含む。
- **キーファクト:**
  - 安全性レッドライン明記
  - 国内大量監視禁止
  - 武力使用への人間の責任
  - 分類ネットワークでの展開
- **引用URL:** https://openai.com/index/our-agreement-with-the-department-of-war/

### INFO-042
- **タイトル:** Trump directs all federal agencies to stop using Anthropic
- **ソース:** CBC News
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** Anthropic
- **要約:** トランプ政権が全米連邦機関に対しAnthropicのAI技術の使用停止を命令。主要な制裁措置を課す。Anthropicは2億ドルの国防総省契約を持っていたが、安全性制限の削減を拒否。
- **キーファクト:**
  - 全連邦機関への使用停止命令
  - $200M国防総省契約
  - 安全性制限削減拒否が原因
  - SCR（Supply Chain Risk）指定
- **引用URL:** https://www.cbc.ca/news/business/trump-anthropic-feud-ai-9.7109006

### INFO-043
- **タイトル:** OpenAI to work with Pentagon after Anthropic dropped by Trump
- **ソース:** The Guardian
- **公開日:** 2026-02-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIが国防総省と契約し、分類された米軍ネットワークにAIを提供すると発表。これはトランプが政府にAnthropic使用停止を命令した数時間後の出来事。Sam Altmanは「明らかに急がれた」「見た目は良くない」と認める。
- **キーファクト:**
  - Anthropic使用停止命令の数時間後にOpenAI契約
  - 「漁夫の利」構造成立
  - Sam Altman: 「明らかに急がれた」「見た目は良くない」
- **引用URL:** https://www.theguardian.com/technology/2026/feb/28/openai-us-military-anthropic

### INFO-044
- **タイトル:** Inside Anthropic's Killer-Robot Dispute With the Pentagon
- **ソース:** The Atlantic
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** Anthropic
- **要約:** 国防総省がAnthropicとの契約を一方的に再交渉すると主張。AnthropicのAIモデルは現在、米国の分類ネットワークに入ることが許可されている唯一のモデル。
- **キーファクト:**
  - 国防総省が一方的に契約再交渉を主張
  - Anthropicは分類ネットワーク唯一のアクセス許可モデル
  - 2025年7月に$200M契約締結
- **引用URL:** https://www.theatlantic.com/technology/2026/03/inside-anthropics-killer-robot-dispute-with-the-pentagon/686200/

### INFO-045
- **タイトル:** Pentagon $200M contracts with Anthropic, OpenAI, Google
- **ソース:** Reuters
- **公開日:** 2026-02-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** 国防総省は過去1年で主要AIラボと最大2億ドルの契約を締結（Anthropic、OpenAI、Google）。OpenAIは「階層化された保護」の詳細を公開。
- **キーファクト:**
  - 各社$200M契約
  - OpenAI: 階層化された保護措置
  - 国防総省のAI契約競争激化
- **引用URL:** https://www.reuters.com/business/media-telecom/openai-details-layered-protections-us-defense-department-pact-2026-02-28/

### INFO-046
- **タイトル:** Anthropic boss rejects Pentagon demand to drop AI safeguards - BBC
- **ソース:** BBC News
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** Anthropic
- **要約:** Anthropicは米国防総省とのAI技術使用方法をめぐる争いで譲歩しないと表明。Dario Amodei CEOは安全性基準の維持を主張。
- **キーファクト:**
  - 安全性基準維持を拒否しない姿勢
  - 完全自律型兵器・大量監視への反対継続
  - 法的争いへの準備
- **引用URL:** https://www.bbc.com/news/articles/cvg3vlzzkqeo

### INFO-047
- **タイトル:** Anthropic Hits Back After US Military Labels It a Supply Chain Risk
- **ソース:** Wired
- **公開日:** 2026-02-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** Anthropic
- **要約:** 国防長官Pete Hegsethが国防総省にAnthropicを「サプライチェーンリスク」として指定するよう指示。シリコンバレーに衝撃を与える。Anthropicは法的に争う姿勢。
- **キーファクト:**
  - 国防長官がSCR指定を指示
  - シリコンバレーに衝撃
  - 法的争いの姿勢
- **引用URL:** https://www.wired.com/story/anthropic-supply-chain-risk-shockwaves-silicon-valley/

### INFO-048
- **タイトル:** The dawning of authoritarian AI - chilling effect
- **ソース:** Steven Adler (Substack)
- **公開日:** 2026-02
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** Anthropic
- **要約:** Anthropicへの圧力は「萎縮効果」を生む。政府の過剰介入に対するチェックの一つは、これが一部の種類のAI開発を抑制する可能性があること。
- **キーファクト:**
  - Anthropic圧力が業界全体に萎縮効果
  - 国防総省と協力を検討する企業への悪影響
  - Google DeepMind Jeff Deanも大量監視に反対
- **引用URL:** https://stevenadler.substack.com/p/ai-powered-authoritarianism-is-coming

### INFO-049
- **タイトル:** Big Tech workers press bosses to back Anthropic in Pentagon clash
- **ソース:** Financial Times
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06（政府圧力・萎縮効果）
- **関連企業:** Google, Anthropic
- **要約:** Big Techの従業員が経営陣にAnthropic支持を求める。Google DeepMindのJeff Dean首席科学者が「大量監視は憲法修正第4条に違反し、表現の自由に萎縮効果を与える」と発言。
- **キーファクト:**
  - Big Tech従業員がAnthropic支持を要請
  - Jeff Dean: 大量監視は憲法違反
  - 表現の自由への萎縮効果
- **引用URL:** https://www.ft.com/content/7bbc4ad3-57f4-4cfd-b791-e50e625c2e0e

### INFO-050
- **タイトル:** Just 10% realizing significant ROI from agentic AI - Deloitte
- **ソース:** Deloitte
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02（エンタープライズ採用率）
- **関連企業:** （業界全体）
- **要約:** Deloitte調査で、わずか10%の組織のみがエージェントAIから大幅なROIを実現。93%のAI予算が技術に使われ、採用・トレーニングが不足。76%が2026年に戦略的投資を計画も30%のみがパイロット実施。
- **キーファクト:**
  - 10%のみが大幅ROI実現
  - 93%の予算が技術に（採用・トレーニング不足）
  - 76%が戦略的投資計画、30%のみパイロット
  - 80%がAIエージェント採用を戦略的優先事項
- **引用URL:** https://www.deloitte.com/ca/en/Industries/financial-services/perspectives/ai-adoption-roi-success.html

### INFO-051
- **タイトル:** Enterprise AI adoption: 25% today to 54% in 6 months
- **ソース:** Deloitte Global
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02（エンタープライズ採用率）
- **関連企業:** （業界全体）
- **要約:** エンタープライズAI採用が成長。本番環境でAI実験を行う企業が現在25%から6ヶ月以内に54%に増加すると予測。
- **キーファクト:**
  - 本番環境AI実験: 25% → 54%（6ヶ月）
  - ITSMで84%がAIに肯定的
  - 金融では6%のみが本番到達
- **引用URL:** https://www.deloitte.com/cz-sk/en/issues/generative-ai/state-of-ai-in-enterprise.html

### INFO-052
- **タイトル:** EU AI Act 2026: Preparatory Obligations in Force
- **ソース:** European Business Review
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03（規制環境）
- **関連企業:** （業界全体）
- **要約:** EU AI Actの準備義務が発効。政策の野心から運用上の執行へ移行。2026年8月にハイリスクAIシステム規制が適用。
- **キーファクト:**
  - 準備義務が発効
  - 2026年8月: ハイリスクAIシステム規制
  - ビジネスの管理負担25%削減目標
- **引用URL:** https://www.europeanbusinessreview.com/eu-ai-act-preparatory-obligations-in-force-what-it-means-for-risk-governance-and-leadership/

### INFO-053
- **タイトル:** 2026 International AI Safety Report - enterprise impact
- **ソース:** IBM
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03（規制環境）
- **関連企業:** （業界全体）
- **要約:** 2026年国際AI安全性レポートによると、AIの最も差し迫ったリスクはモデル自体ではなく、AIが組み込まれる複雑なシステムから生じる可能性がある。
- **キーファクト:**
  - リスクはモデルではなく複雑なシステムから
  - エンタープライズへの影響分析
  - ガバナンス・リスク管理の重要性
- **引用URL:** https://www.ibm.com/think/news/new-global-ai-safety-report-means-enterprise

### INFO-054
- **タイトル:** President Trump Targets State AI Regulations
- **ソース:** The Reg Review
- **公開日:** 2026-02-26
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03（規制環境）
- **関連企業:** （業界全体）
- **要約:** トランプ大統領が2025年12月に署名した命令で、連邦政策と矛盾する州レベルのAI規制の採用・執行を阻止。GSAがAnthropic使用停止を支持。
- **キーファクト:**
  - 州レベルAI規制を連邦政策に従わせる命令
  - GSAがAnthropic使用停止を支持
  - 連邦優先のAI規制方針
- **引用URL:** https://www.theregreview.org/2026/02/26/champagne-president-trump-targets-state-based-ai-regulations/

### INFO-055
- **タイトル:** How China is betting cheap AI will get the world hooked
- **ソース:** TechXplore
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03（規制環境）
- **関連企業:** ByteDance, DeepSeek
- **要約:** 中国は2030年までにAI技術と応用を世界最先端レベルにし、世界の主要AIセンターにする政策目標。安価なAIで世界を中国技術に依存させる戦略。
- **キーファクト:**
  - 2030年までに世界主要AIセンター目標
  - 2025年サイバーセキュリティ法改正が最も厳格
  - 入札・調達プロセスでのAI採用加速
- **引用URL:** https://techxplore.com/news/2026-02-china-cheap-ai-world-tech.html

### INFO-056
- **タイトル:** AI Agents in marketing - 76% teams using AI, 45%+ CAGR
- **ソース:** Averi AI
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04（業務自律化）
- **関連企業:** （業界全体）
- **要約:** エージェントAI市場は2026年に$10.9Bを超え、45%+ CAGRで成長。76%のマーケティングチームがコア業務でAI使用。43%がビジネスロジック・タスクオーケストレーション、41%がコンテンツ生成。
- **キーファクト:**
  - エージェントAI市場: $10.9B、45%+ CAGR
  - 76%マーケティングチームがAI使用
  - 43%ビジネスロジック、41%コンテンツ生成
  - 27%マーケティングワークフロー自動化
- **引用URL:** https://www.averi.ai/how-to/ai-agent-marketing-how-autonomous-ai-is-changing-content-ops-in-2026

### INFO-057
- **タイトル:** Meta's Manus AI assistant reshaping ad buying
- **ソース:** AdAge
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04（業務自律化）
- **関連企業:** Meta
- **要約:** Metaの広告プラットフォームの新AIツールManusが、エージェントがメディアプランを編成する未来を予感させる。クリエイティブから自動化へ。
- **キーファクト:**
  - Manus: Meta広告プラットフォームの新AIツール
  - エージェントによるメディアプラン編成
  - クリエイティブ自動化
- **引用URL:** https://adage.com/technology/meta/aa-manus-ai-advertising/

### INFO-058
- **タイトル:** 80% of customer service jobs at risk of automation
- **ソース:** Medium
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04（業務自律化）
- **関連企業:** （業界全体）
- **要約:** AIツールにより80%のカスタマーサービス職が自動化リスクに。米国で約5000万のエントリーレベル職がリスクにある。World Economic ForumはAIが創出と同数の職を破壊すると予測。
- **キーファクト:**
  - 80%カスタマーサービス職が自動化リスク
  - 米国で約5000万エントリーレベル職がリスク
  - WEF: AIが創出と同数の職を破壊
  - Microsoft幹部もエントリーレベル職への懸念
- **引用URL:** https://medium.com/activated-thinker/how-ai-is-quietly-replacing-entry-level-jobs-and-what-that-means-for-your-future-808090bfc51c

### INFO-059
- **タイトル:** AI really is changing the programming profession
- **ソース:** Understanding AI
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04（業務自律化）
- **関連企業:** （業界全体）
- **要約:** コーディングエージェントは人間プログラマーを置き換えるには程遠いが、プログラマーの仕事のやり方を変革している。インタビューしたほぼ全員が、プログラミング職の変化を信じている。
- **キーファクト:**
  - エージェントは人間置き換えより仕事変革
  - プログラミング職の根本的変化
  - エントリーレベル職の将来に懸念
- **引用URL:** https://www.understandingai.org/p/sorry-skeptics-ai-really-is-changing

### INFO-060
- **タイトル:** LLM API Pricing 2026 - DeepSeek undercut everyone, OpenAI slashed 80%
- **ソース:** TLDL
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01（API料金改定）
- **関連企業:** OpenAI, DeepSeek
- **要約:** LLM価格競争が激化。DeepSeekが全社をアンダーカット。OpenAIはフラッグシップ価格をYoY 80%削減。Googleは無料枠を提供。GPT-5 Mini: $0.25/1M入力、$2/1M出力。
- **キーファクト:**
  - DeepSeek: 最安値で競合他社をアンダーカット
  - OpenAI: フラッグシップ価格YoY 80%削減
  - GPT-5 Mini: $0.25/1M入力、$2/1M出力
  - GPT-5: $1.25/1M入力、$10/1M出力
- **引用URL:** https://www.tldl.io/resources/llm-api-pricing-2026

### INFO-061
- **タイトル:** Anthropic billing changes 2026 - Fast mode pricing
- **ソース:** LinkedIn
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01（API料金改定）
- **関連企業:** Anthropic
- **要約:** Anthropicが課金変更。Standard Opus 4.6: $5入力/$25出力/MTok。Fast mode Opus 4.6 (≤200K入力): $30入力/$150出力/MTok。Sonnet 4.5: $3入力/$15出力/MTok。
- **キーファクト:**
  - Standard Opus 4.6: $5/$25 per MTok
  - Fast mode Opus 4.6 (≤200K): $30/$150 per MTok
  - Sonnet 4.5: $3/$15 per MTok
  - Claude Opus 3は2026年1月5日に廃止
- **引用URL:** https://www.linkedin.com/pulse/explaining-anthropic-billing-changes-2026-fast-mode-pricing-liveanu-iwede

### INFO-062
- **タイトル:** Gemini API Pricing: $0.10-$4.00 per million input tokens
- **ソース:** Google AI (公式)
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01（API料金改定）
- **関連企業:** Google
- **要約:** Gemini API価格は2026年2月時点で$0.10〜$4.00/100万入力トークン、$0.40〜$18.00/100万出力トークン。Gemini 2.5 Flashが低レイテンシ・高ボリュームタスクに最適な価格性能比。画像出力は$60/100万トークン。
- **キーファクト:**
  - 入力: $0.10-$4.00/MTok
  - 出力: $0.40-$18.00/MTok
  - 画像出力: $60/MTok
  - 無料枠あり
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing

### INFO-063
- **タイトル:** Gemini 3.1 Pro: ARC-AGI-2 77.1%, Intelligence Index top
- **ソース:** DeepLearning.AI
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02（ベンチマーク性能）
- **関連企業:** Google
- **要約:** Google Gemini 3.1 Pro PreviewがARC-AGI-2で77.1%達成（前世代31.1%から2倍以上）。同じ価格でIntelligence Index首位。ハルシネーション削減も実用的改善。
- **キーファクト:**
  - ARC-AGI-2: 77.1%（前世代31.1%から2.5倍）
  - $0.96/task
  - Intelligence Index首位
  - ハルシネーション削減
- **引用URL:** https://www.deeplearning.ai/the-batch/google-releases-gemini-3-1-pro-in-preview-tops-intelligence-index-at-same-price/

### INFO-064
- **タイトル:** Open-source LLMs within single digits of proprietary models
- **ソース:** Reddit
- **公開日:** 2026-02
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-003-02（ベンチマーク性能）
- **関連企業:** DeepSeek
- **要約:** オープンソースLLMがプロプライエタリモデルとほぼ同等に。2026年2月ランキングでGLM-5、Kimi K2.5、DeepSeek V3.2がほぼ全ベンチマークで一桁差に迫る。
- **キーファクト:**
  - OSS-プロプライエタリ間が一桁差に
  - GLM-5、Kimi K2.5、DeepSeek V3.2が上位
  - タスクにより性能が大幅に変動
- **引用URL:** https://www.reddit.com/r/singularity/comments/1rh7dci/opensource_llms_are_now_within_single_digits_of/

### INFO-065
- **タイトル:** OpenAI announces $110 billion funding round - $730B valuation
- **ソース:** OpenAI/Reuters (公式)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04（資金調達・投資動向）
- **関連企業:** OpenAI, Amazon, NVIDIA, SoftBank
- **要約:** OpenAIが$110Bの資金調達を発表。評価額$730B（事前）。Amazon $50B、NVIDIA $30B、SoftBank $30Bが出資。ChatGPTメーカーにとって最大の資金調達。
- **キーファクト:**
  - $110B調達、$730B評価額
  - Amazon $50B、NVIDIA $30B、SoftBank $30B
  - AIスタートアップ史上最大規模
- **引用URL:** https://openai.com/index/scaling-ai-for-everyone/

### INFO-066
- **タイトル:** Andrew Ng says AGI is decades away
- **ソース:** Fast Company
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01（AGI到達度）
- **関連企業:** （業界全体）
- **要約:** Andrew Ng氏がAGIは数十年先と発言。業界の次のフェーズを定義するのは、人間レベルの知能ではなく、ワークフローを自動化するエージェントシステム。
- **キーファクト:**
  - Andrew Ng: AGIは数十年先
  - 次フェーズ: エージェントシステムによる自動化
  - AIバブルリスクは別に存在
- **引用URL:** https://www.fastcompany.com/91499247/andrew-ng-agi-decades-away-interview

### INFO-067
- **タイトル:** Humanity's Last Exam - toughest AI test for AGI measurement
- **ソース:** LiveScience
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01（AGI到達度）
- **関連企業:** （業界全体）
- **要約:** Center for AI SafetyとScale AIが「Humanity's Last Exam」を公開。今日の最強AIがAGIにどれだけ近いかを測定する世界最高難易度のテスト。
- **キーファクト:**
  - Center for AI Safety + Scale AI開発
  - AGI近接度測定のための最高難易度テスト
  - AGIタイムライン評価の新指標
- **引用URL:** https://www.livescience.com/technology/artificial-intelligence/acing-this-new-ai-exam-which-its-creators-say-is-the-toughest-in-the-world-might-point-to-the-first-signs-of-agi

### INFO-068
- **タイトル:** AGI Timeline: Sam Altman 2029前、Dario Amodei 2026-2027、Demis Hassabis 2030に50%
- **ソース:** LinkedIn/Medium
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02（AGIタイムライン予測）
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** AGIタイムライン予測が分化。Sam Altman: 2029年前、Dario Amodei: 2026-2027で「強力なAI」、Demis Hassabis: 2030年に50%の確率。9,000以上の予測を分析した調査も。
- **キーファクト:**
  - Sam Altman: 5年以内、2032-2035でスーパーインテリジェンス
  - Dario Amodei: 2026年末までに強力なAI
  - Demis Hassabis: 2030年に50%確率
- **引用URL:** https://www.linkedin.com/posts/prabhakar-kenneth-vemagiri-_agi-artificialintelligence-aifuture-activity-7431299620938620928-zSco

### INFO-069
- **タイトル:** Pentagon sets deadline for Anthropic to abandon ethics rules
- **ソース:** Reddit
- **公開日:** 2026-02-27
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-005-03（AGI安全性・ガバナンス）
- **関連企業:** Anthropic
- **要約:** 国防総省がAnthropicに金曜期限で倫理規定の放棄を要求。AnthropicはAIによる最終ターゲティング決定の人間の関与なき実施、および国内大量監視への使用を拒否。
- **キーファクト:**
  - 国防総省が倫理規定放棄の期限設定
  - 人間の関与なきターゲティング決定拒否
  - 国内大量監視拒否
- **引用URL:** https://www.reddit.com/r/technology/comments/1rdvlsb/pentagon_sets_friday_deadline_for_anthropic_to/

### INFO-070
- **タイトル:** Doubao 2.0 released - 1/4 price of Gemini 3 Pro
- **ソース:** Sina (中国語)
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがDoubao 2.0をリリース。価格はGemini 3 Proの1/4、マルチモーダル理解と推論能力がトップクラス。Seedance 2.0を支える基盤モデル。Pro、Lite、Miniの3バージョン展開。
- **キーファクト:**
  - 価格: Gemini 3 Proの1/4
  - Pro/Lite/Mini 3バージョン
  - Seedance 2.0の基盤モデル
  - マルチモーダル理解・複雑命令実行
- **引用URL:** https://k.sina.com.cn/article_7307132662_v1b389fef600102qpjc.html

### INFO-071
- **タイトル:** Doubao chatbot 100M+ daily active users during Chinese New Year
- **ソース:** Zaobao (中国語)
- **公開日:** 2026-02-25
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceの豆包(Doubao)チャットボットが中国の旧正月期間に1億人以上の日次アクティブユーザーを獲得。中国のテック大手が数十億ドルを費やすAI競争で勝利。
- **キーファクト:**
  - 1億DAU（旧正月期間）
  - 中国AI競争で優位
  - 国民的AIアシスタントとして浸透
- **引用URL:** https://www.zaobao.com.sg/news/china/story20260225-8637632

### INFO-072
- **タイトル:** DeepSeek-V3.2 offers strong reasoning performance
- **ソース:** Microsoft Azure
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-03（OSS vs商用モデル）
- **関連企業:** DeepSeek, Microsoft
- **要約:** DeepSeek-V3.2が強力な推論性能と幅広いタスクカバレッジを提供し、本番環境ワークロードに適している。Azure AI FoundryでNVFP4による高パフォーマンス推論を提供。
- **キーファクト:**
  - 強力な推論性能
  - 本番環境向け
  - Azure AI Foundryで利用可能
  - NVFP4による高効率推論
- **引用URL:** https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/unlocking-high-performance-inference-for-deepseek-with-nvfp4-on-nvidia-blackwell/4497936

### INFO-073
- **タイトル:** Klarna AI replacement reversed within months
- **ソース:** LinkedIn/CX Dive
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04（業務自律化）
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaは2024年にAIエージェントが700人の担当者に相当すると発表し、採用停止とレイオフを実施。しかし2025年に方針を撤回。DuolingoもAI-first宣言後、数ヶ月で撤回。
- **キーファクト:**
  - Klarna: 700人相当AI → 方針撤回
  - Duolingo: AI-first → 撤回
  - AIを人数削減ツールとして扱う企業が逆風
- **引用URL:** https://www.linkedin.com/posts/eitannorel_%F0%9D%90%91%F0%9D%90%A1%F0%9D%90%9E%F0%9D%90%AB%F0%9D%90%9E-%F0%9D%90%A2%F0%9D%90%A3-%F0%9D%90%A7%F0%9D%90%A8-%F0%9D%90%AC%F0%9D%90%AE%F0%9D%90%9C%F0%9D%90%A1-%F0%9D%90%AD%F0%9D%90%A1%F0%9D%90%A2%F0%9D%90%A7%F0%9D%90%A0-activity-7432083903672238080-v-Vi

### INFO-074
- **タイトル:** European Publishers antitrust complaint against Google
- **ソース:** Affiverse Media
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05（プラットフォーマーAI統合）
- **関連企業:** Google
- **要約:** 欧州出版社がGoogleに対して独占禁止法申立。7つの反競争行為を告発：体系的なトラフィック代替、媒介排除、搾取的データ利用など。GoogleのAI広告ツールが業界構造を変革。
- **キーファクト:**
  - 欧州出版社がGoogleを提訴
  - 7つの反競争行為カテゴリ
  - トラフィック代替・媒介排除
  - AI広告ツールによる業界構造変革
- **引用URL:** https://www.affiversemedia.com/european-publishers-take-on-google-what-the-epcs-antitrust-complaint-means-for-affiliate-marketers/

### INFO-075
- **タイトル:** Seat-Count Crisis: AI Agents Triggered 2026 Software Sell-Off
- **ソース:** Chronicle Journal
- **公開日:** 2026-02-23
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05（プラットフォーマーAI統合）
- **関連企業:** （業界全体）
- **要約:** 2026年ソフトウェア売却の引き金は「シート数危機」。ステークホルダーのナラティブが「AI強化機能の称賛」から「AIによる媒介排除への恐怖」にシフト。LLM活用でビジネスが従来SaaSを回避。
- **キーファクト:**
  - 2026年ソフトウェア売却の主因
  - シート数（ユーザー数）ビジネスモデル崩壊懸念
  - AIによる媒介排除への恐怖
  - SaaS回避のトレンド
- **引用URL:** http://markets.chroniclejournal.com/chroniclejournal/article/marketminute-2026-2-23-the-seat-count-crisis-how-ai-agents-triggered-the-2026-software-sell-off

### INFO-076
- **タイトル:** GitHub Copilot 26M users, Cursor 25% market share in AI code editors
- **ソース:** DevOps.com/Gitnux
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02（コーディング能力市場価値）
- **関連企業:** Microsoft, Cursor
- **要約:** GitHub Copilotが2600万ユーザー突破。CursorはAIコードエディタで25%市場シェア、GitHub Copilotより15 NPSポイント上回るユーザー満足度。有料AIコーディングツールユーザーは約130万人。
- **キーファクト:**
  - GitHub Copilot: 26Mユーザー
  - Cursor: 25%市場シェア、+15 NPS
  - 有料AIコーディングツール: 130万人
  - Microsoft Copilotは統合されているが使用率低い
- **引用URL:** https://devops.com/cursor-cloud-agents-get-their-own-computers-and-35-of-internal-prs-to-prove-it/

### INFO-077
- **タイトル:** Software Dev Jobs Rise 10% despite AI apocalypse warnings
- **ソース:** LinkedIn/AOL
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02（コーディング能力市場価値）
- **関連企業:** （業界全体）
- **要約:** AI職の終末論的な警告にもかかわらず、米国のソフトウェア開発職は2025年2月から2026年2月で約10%増加。2025年半ばから2026年1月で投稿数は約11%増加。ただし「コンピュータプログラマー」職は2年で27%減少。
- **キーファクト:**
  - ソフトウェア開発職: +10% YoY
  - 2025年半ばからの投稿: +11%
  - コンピュータプログラマー職: -27%（2年）
  - MBA需要を上回る需要
- **引用URL:** https://www.aol.com/articles/despite-constant-job-apocalypse-warnings-171553362.html

### INFO-078
- **タイトル:** 83% believe AI makes uniquely human skills more critical
- **ソース:** LinkedIn/Workday
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03（AI代替困難能力）
- **関連企業:** （業界全体）
- **要約:** Workdayグローバル調査で83%の従業員がAIによって人間固有のスキルがより重要になると回答。McKinsey報告では生成AIが従業員の時間の60-70%を占める活動を自動化可能。
- **キーファクト:**
  - 83%が人間スキルの重要性増加
  - McKinsey: 60-70%活動の自動化可能
  - ヘルスケア、メンタルヘルス職がAI耐性
  - 明確な文書コミュニケーション、自己方向付けが重要
- **引用URL:** https://www.linkedin.com/pulse/skills-survive-ai-decade-human-capability-age-andre-fsj6e

### INFO-079
- **タイトル:** Only 11% of companies achieve AI primary business objective
- **ソース:** WSJ/Bain
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-04（AI時代に勝つ企業）
- **関連企業:** （業界全体）
- **要約:** WSJが報じたところ、わずか11%の企業がAIで主要ビジネス目標を達成。72%の投資家が人間-AI統合企業に評価を与える姿勢。アップスキリング・リスキリング投資企業が高収益。
- **キーファクト:**
  - 11%のみが主要目標達成
  - 72%投資家が人間-AI統合を評価
  - 2030年までに99%技術企業がAI採用予定
  - アップスキリング投資企業が高収益
- **引用URL:** https://www.bain.com/insights/want-more-out-of-your-ai-investments-think-people-first/

### INFO-080
- **タイトル:** AMD $60B AI chip deal with Meta over 5 years
- **ソース:** Reuters
- **公開日:** 2026-02-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03（AGI安全性・ガバナンス）
- **関連企業:** Meta, AMD
- **要約:** AMDがMetaに5年間で最大600億ドル相当のAIチップを販売する契約を締結。OpenAIからNvidiaまで、企業がAIインフラに数十億ドルを投入中。
- **キーファクト:**
  - AMD-Meta: $60B/5年契約
  - AIチップ・データセンターへの巨額投資
  - $110B調達がインフラ投資と連動
- **引用URL:** https://www.reuters.com/business/autos-transportation/companies-pouring-billions-advance-ai-infrastructure-2026-02-24/

### INFO-081
- **タイトル:** MCP Enterprise Adoption - 726 repositories, Airia 1,000+ integrations
- **ソース:** Zircote/Airia
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-RED-001（MCP利用率）
- **関連企業:** （業界全体）
- **要約:** GitHubスキャンで726のMCPサーバーリポジトリ（50+スター）を発見。awslabs/mcpが8.2kスターで首位。AiriaのMCP Gatewayが1,000以上の事前設定済み統合を提供し、最大のエンタープライズMCPライブラリに。86%の企業がAIエージェント展開に技術スタックアップグレード必要。
- **キーファクト:**
  - 726 MCPサーバーリポジトリ（50+スター）
  - awslabs/mcp: 8.2kスター首位
  - Airia MCP Gateway: 1,000+統合
  - 86%企業がスタックアップグレード必要
- **引用URL:** https://zircote.com/blog/2026/02/friday-roundup-week-8/

### INFO-082
- **タイトル:** How Enterprises Measure ROI from AI Agents
- **ソース:** IT Tech Pulse
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-RED-005（ROI定義詳細）
- **関連企業:** （業界全体）
- **要約:** AIエージェントのROI測定には単なるコスト削減計算以上が必要。運用効率、認知的再配分、リスク削減を評価する必要がある。AIを「ムーンショット革新」ではなく「運用ソフトウェア」として位置付ける企業が持続可能なROIを達成。金融サービスで3-6倍ROIベンチマーク。
- **キーファクト:**
  - ROI測定: コスト削減+運用効率+認知再配分+リスク削減
  - 運用ソフトウェアとして位置付ける
  - 金融サービス: 3-6倍ROI
- **引用URL:** https://ittech-pulse.com/our-tech-insights/how-enterprises-measure-roi-from-ai-agents/

### INFO-083
- **タイトル:** Anthropic $14B revenue run rate, Vercept integration ongoing
- **ソース:** Instagram/LinkedIn
- **公開日:** 2026-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-RED-006（Vercept統合採用率）
- **関連企業:** Anthropic
- **要約:** Anthropicが年間収益ランレート$14B達成（最初の収益から3年未満）。Vercept買収のClaudeコンピュータ使用機能への統合が進行中。85.7%の会話が反復・洗練を含む。
- **キーファクト:**
  - 年間収益ランレート: $14B
  - Vercept統合進行中
  - 85.7%会話が反復・洗練含む
- **引用URL:** https://www.linkedin.com/pulse/week-ai-block-cuts-4000-overhaul-pentagon-ultimatum-anthropic-kleine-okrkf

### INFO-084
- **タイトル:** Big Tech to invest $650B in AI in 2026, IT spending $6T
- **ソース:** Reuters/Gartner
- **公開日:** 2026-02-23
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-RED-007（業界投資額推計）
- **関連企業:** Alphabet, Amazon, Meta, Microsoft
- **要約:** BridgewaterによるとAlphabet、Amazon、Meta、Microsoftが2026年に約$650BをAIインフラに投資予定。ハイパースケーラーは2026年だけでデータセンターに約$700Bを支出計画。世界IT支出は初めて$6Tを超える見込み。AI資本支出はGDPの2%に達する。
- **キーファクト:**
  - Big Tech AI投資: $650B（2026年）
  - データセンター支出: ~$700B
  - 世界IT支出: $6T突破（初）
  - AI資本支出: GDPの2%
- **引用URL:** https://www.reuters.com/business/big-tech-invest-about-650-billion-ai-2026-bridgewater-says-2026-02-23/



## X (Twitter) 投稿データ（ローカルRSSHub経由）

### INFO-085
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-03-02
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Aaron Bergman 🔍 ⏸️ (in that order)
Interesting

https://www.hiive.com/securities/anthropic-stock
- **引用URL:** https://x.com/EthanJPerez/status/2028224040591384675

### INFO-086
- **タイトル:** @demishassabis (Demis Hassabis) のX投稿
- **ソース:** X (Twitter) - @demishassabis (共同創業者・CEO)
- **公開日:** 2026-03-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** RT Pierrick Chevallier | IA
🚨PromptShare🚨
Okay… Banana 2 does not play
when it comes to exploded views.
Clean part separation. Accurate perspective.Full consistency.

PROMPT
product design, [object or vehicle with material accents], exploded view diagram, white background, three-dimensional, highly detailed internal components, studio lighting, product photography, best quality
- **引用URL:** https://x.com/demishassabis/status/2028209376192819241

