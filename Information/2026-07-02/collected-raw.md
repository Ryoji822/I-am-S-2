# 収集データ: 2026-07-02

## メタデータ
- 収集日時: 2026-07-02 00:14 UTC 開始 / 2026-07-02 01:30 UTC 完了
- 品質フラグ: NORMAL
- 収集情報数: 97件
- Evidence ID 採番範囲: EVD-20260702-0001 〜 EVD-20260702-0097
- 実行クエリ数: 90+ (collection_plan.json 全24 KIQ + 動的4 KIQ)
- 詳細スクレイピング: 7件 (OpenAI GPT-5.6 Sol, ABC News Pentagon-Anthropic, xAI Voice Agent Builder, Kavout SCR分析, AWS Bedrock Agents Classic, DeepMind人材流出, Claude Sonnet 5)
- KIQカバレッジ: 全28 KIQ (24計画 + 4動的Arbiter優先) カバー
- 動的追加クエリ: KIQ-MIL-001, KIQ-GOV-002, KIQ-ANT-002, KIQ-OAI-001 (Arbiter優先指定)
- Tier 1企業カバレッジ: OpenAI(12), Anthropic(20), Google(15), xAI(8), ByteDance(5)
- 信頼性コード分布: A(15), B(35), C(30), D(12), E(5)
- 主要発見: ペンタゴン-Anthropic SCR指定（国内企業初）, GPT-5.6三モデル体系, DeepMind AlphaFoldチーム集団移籍($270B影響), AWS Bedrock Agents Classic終了→AgentCore, Claude Sonnet 5ローンチ, xAI Voice Agent Builder, MCP RC 2026-07-28

## 収集結果

### INFO-001
- **タイトル:** Pentagon demands AI vendors accept "any lawful use" of technology; Anthropic refuses autonomous weapons safeguards removal
- **ソース:** Facebook/FRANCE24/Straits Times
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001, KIQ-002-06
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** 2026年初頭、ペンタゴンはAIベンダーに対し「いかなる合法的な用途」も受け入れるよう要求。Anthropicは完全自律型兵器や国内監視に使用されるのを防ぐセーフガードの削除を拒否。その後トランプ政権はAIの輸出制限を解除。
- **キーファクト:**
  - ペンタゴン、AIベンダーに「any lawful use」受諾を要求
  - Anthropicは自律型兵器・国内監視向けセーフガード削除を拒否
  - トランプ政権、Anthropic拒否後に輸出制限を解除
  - Dario Amodei氏、2026年2月のCBSインタビューで倫理的境界を明確化
- **引用URL:** https://www.straitstimes.com/world/united-states/pentagon-sees-broader-role-for-ai-in-setting-military-targets
- **Evidence ID:** EVD-20260702-0001

### INFO-002
- **タイトル:** Claude Code 18% developer adoption with 91% CSAT; WAU doubled since January 2026
- **ソース:** Uvik Software / New Market Pitch
- **公開日:** 2026-07-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-ANT-002, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Claude Codeは2026年1月時点で開発者の18%が採用し、91%のCSATで全AIコーディングツール最高。2026年1月1日以降、週間アクティブユーザーが2倍、企業サブスクリプション増加。ただしClaude Code固有WAUの正確な数値は依然開示されていない。
- **キーファクト:**
  - Claude Code開発者採用率18%（2026年1月）
  - CSAT 91% - 全AIコーディングツール最高
  - WAUは2026年1月以降2倍、企業サブスクリプション増加
  - Claude Code固有WAU/DAU絶対値は未開示継続（KIQ-ANT-002未解消）
- **引用URL:** https://uvik.net/blog/ai-coding-assistant-statistics/
- **Evidence ID:** EVD-20260702-0002

### INFO-003
- **タイトル:** OpenAI Codex WAU grew 5x in early 2026; non-developers leading adoption surge
- **ソース:** Facebook / AI tracking
- **公開日:** 2026-07-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-ANT-002, KIQ-004-02
- **関連企業:** OpenAI
- **要約:** OpenAIの2026年6月25日Codex研究論文によると、週間アクティブユーザーが2026年初頭に5倍以上成長。非開発者の採用が急増し、個人で137倍、企業で189倍増。コーディング能力のコモディティ化シグナル。
- **キーファクト:**
  - OpenAI Codex WAU 5倍以上成長（2026年初頭）
  - 非開発者層が採用を牽引
  - 個人採用137倍、企業採用189倍増
- **引用URL:** https://www.facebook.com/theartificialintelligencee/posts/...
- **Evidence ID:** EVD-20260702-0003

### INFO-004
- **タイトル:** Google DeepMind talent exodus: 5 senior researchers depart to Anthropic/OpenAI, Alphabet loses $270B
- **ソース:** Memeburn / BuildFastWithAI
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-GOV-002, KIQ-003-04
- **関連企業:** Google DeepMind, Anthropic, OpenAI
- **要約:** GoogleのDeepMindから5人のシニア研究者が1週間のうちにAnthropic/OpenAIへ移籍。Alphabetは約$2700億の時価総額を喪失。AI企業の評価メカニズムの変化を示す信号。
- **キーファクト:**
  - DeepMind 5名シニア研究者が1週間で退社
  - Alphabet $2700億時価総額喪失
  - 研究者流出は安全性研究体制への影響懸念
- **引用URL:** https://memeburn.com/google-deepmind-talent-exodus-hits-alphabet-with-270b-loss/
- **Evidence ID:** EVD-20260702-0004

### INFO-005
- **タイトル:** OpenAI Responses API replacing Assistants API (deprecated 2026); new research paper on agent work transformation
- **ソース:** OpenAI / Speakeasy
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIはAssistants APIを2026年に非推奨とし、全機能をResponses APIに統合。新規プロジェクトはAgents SDK使用推奨。新研究論文「How agents are transforming work」でエージェントによる仕事の変革を発表。
- **キーファクト:**
  - Assistants API 2026年非推奨、Responses APIへ統合
  - 新規プロジェクトはAgents SDK推奨
  - 「How agents are transforming work」研究論文公開
- **引用URL:** https://openai.com/index/how-agents-are-transforming-work/
- **Evidence ID:** EVD-20260702-0005

### INFO-006
- **タイトル:** Anthropic Claude Agent SDK releases; token-based billing change paused June 15
- **ソース:** GitHub / AIWeekly
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK (TypeScript) のリリース継続。prompt_idフィールド追加、コントロールプロトコル修正。6月15日に予定されていたトークン課金変更を施行当日に撤回。補助料金モデルを置き換える計画だった。
- **キーファクト:**
  - Claude Agent SDK継続リリース（prompt_id追加等）
  - トークン課金変更を6月15日施行日に撤回
  - Claude in Chrome GA、バックグラウンドエージェント通知追加
- **引用URL:** https://aiweekly.co/alerts/anthropic-pauses-claude-agent-sdks-new-token-based-billing
- **Evidence ID:** EVD-20260702-0006

### INFO-007
- **タイトル:** Google Interactions API GA: unified endpoint for Gemini models and agents with server-side state
- **ソース:** Google AI Blog
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google
- **要約:** Google AI StudioのInteractions APIがGA。Geminiモデルとエージェント向けの統一エンドポイントで、サーバーサイドステート、バックグラウンド実行、ツール統合、マルチモーダル生成を提供。Gemini Enterprise Agent Platformも公開。
- **キーファクト:**
  - Interactions API GA - Gemini統一エンドポイント
  - サーバーサイドステート、バックグラウンド実行対応
  - Gemini Enterprise Agent Platform公開
  - Deep Research AgentがMCPサーバー連携対応
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/
- **Evidence ID:** EVD-20260702-0007

### INFO-008
- **タイトル:** xAI Voice Agent Builder beta: no-code platform for Grok Voice, OpenAI Realtime API compatible
- **ソース:** xAI Official
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIがGrok Voice向けVoice Agent Builderをベータ公開。ノーコードで音声エージェントを構築・本番展開可能。OpenAI Realtime API互換で既存クライアントライブラリがそのまま利用可能。組み込みテレフォニー提供。
- **キーファクト:**
  - Voice Agent Builder ベータ公開（ノーコード）
  - Grok Voice上で本番音声エージェント構築
  - OpenAI Realtime API互換
  - 組み込みテレフォニー提供
- **引用URL:** https://x.ai/news/grok-voice-agent-builder
- **Evidence ID:** EVD-20260702-0008

### INFO-009
- **タイトル:** ByteDance open-sources DeerFlow super-agent harness; Seed 2.1 coding agents released
- **ソース:** Instagram / GitHub
- **公開日:** 2026-07-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがスーパーエージェントハーネスDeerFlowをオープンソース化。サンドボックス、サブエージェント、永続メモリ、再利用可能スキルを提供。Seed 2.1コーディングエージェントもリリース。
- **キーファクト:**
  - DeerFlowオープンソース化（サンドボックス・サブエージェント・永続メモリ）
  - Seed 2.1コーディングエージェントリリース
  - ENPIREハーネス4モジュール（自動リセット・検証）
- **引用URL:** https://www.instagram.com/reel/DaKHu8qDd1R/
- **Evidence ID:** EVD-20260702-0009

### INFO-010
- **タイトル:** Okta for AI Agents - Core available for FedRAMP and HIPAA; first AI agent governance inside FedRAMP boundaries
- **ソース:** Okta via The New Stack
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Okta, OpenAI, Anthropic, Google
- **要約:** Okta for AI Agents CoreがFedRAMP・HIPAA環境で利用可能に。FedRAMP境界内でAIエージェントガバナンスを実現する初のソリューション。エンタープライズAIエージェントの規制コンプライアンス要件に対応。
- **キーファクト:**
  - Okta for AI Agents CoreがFedRAMP・HIPAA対応GA
  - FedRAMP境界内AIエージェントガバナンス業界初
  - エンタープライズエージェント展開の規制ハードル低下
- **引用URL:** https://www.facebook.com/thenewstack/posts/...
- **Evidence ID:** EVD-20260702-0010

### INFO-011
- **タイトル:** 40% of enterprise AI agent projects cancelled; governance gap is key blocker
- **ソース:** Instagram / industry tracking
- **公開日:** 2026-07-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** エンタープライズAIエージェントプロジェクトの40%がキャンセルされている。「統制できないものは統治できない」状況。AIが自身のコードの80%以上を記述し、自律性が複合的にリスクを拡大。
- **キーファクト:**
  - エンタープライズAIエージェントプロジェクト40%キャンセル
  - ガバナンスの可視性欠如が主要障壁
  - AIが自身のコード80%以上記述で自律リスク複合化
- **引用URL:** https://www.instagram.com/p/DaDMzccjmnP/
- **Evidence ID:** EVD-20260702-0011

### INFO-012
- **タイトル:** Anthropic hiring Security Controls Assurance Lead; integrated compliance ecosystem as trust engine
- **ソース:** Anthropic / LinkedIn Jobs
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがSecurity Controls Assurance Leadを採用。統合コンプライアンス・リスクエコシステムを設計し、信頼エンジンとして機能させる。Claude EnterpriseはSAML、SCIM、監査ログ、3つの管理ロールを提供。
- **キーファクト:**
  - Security Controls Assurance Lead採用中
  - 統合コンプライアンス・リスクエコシステム設計
  - Claude Enterprise: SAML/SCIM/監査ログ/3管理ロール
  - ネイティブアクセスレビュー機能は不在
- **引用URL:** https://www.toriihq.com/articles/eight-tools-for-claude-access-reviews
- **Evidence ID:** EVD-20260702-0012

### INFO-013
- **タイトル:** Google Vertex AI / Gemini Enterprise Agent Platform SLA and provisioned throughput documented
- **ソース:** Google Cloud
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** Gemini Enterprise Agent Platform（旧Vertex AI）のSLAとプロビジョニングスループットが文書化。固定コスト・固定期間サブスクリプションでスループット予約。コンプライアンス認証とセキュリティコントロールの概要公開。
- **キーファクト:**
  - Gemini Online Inference API SLA文書化
  - プロビジョニングスループット（固定コスト予約）
  - コンプライアンス認証セキュリティコントロール概要公開
  - Vertex AIはGemini Enterprise Agent Platformに統合
- **引用URL:** https://cloud.google.com/vertex-ai/generative-ai/sla
- **Evidence ID:** EVD-20260702-0013

### INFO-014
- **タイトル:** Anthropic Quantium enterprise case study: senior leadership embracing AI at scale
- **ソース:** LinkedIn / Anthropic
- **公開日:** 2026-07-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** AnthropicがQuantiumのケーススタディを公開。上層部自らがAI導入を主導している点が注目点。同様の変革が他社でも進行中。
- **キーファクト:**
  - Quantium Claude企業導入ケーススタディ公開
  - シニアリーダーシップ自らAI導入を推進
- **引用URL:** https://www.linkedin.com/posts/pavpanesar1_quantium-claude-enterprise-case-study...
- **Evidence ID:** EVD-20260702-0014

### INFO-015
- **タイトル:** Gartner: 40% of enterprise apps to integrate AI agents by end 2026 (up from <5% in 2025)
- **ソース:** MachineLearningMastery / Gartner
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Gartner予測で、2025年の5%未満から2026年末に40%のエンタープライズアプリがタスク固有AIエージェントを統合。Microsoftでは62%の開発者がAIで仕事満足度向上、88%がスループット向上を報告。
- **キーファクト:**
  - エンタープライズアプリAIエージェント統合率: <5%(2025)→40%(2026末)
  - Microsoft開発者: 62%が満足度向上、88%がスループット向上
- **引用URL:** https://machinelearningmastery.com/the-ai-agent-tech-stack-explained/
- **Evidence ID:** EVD-20260702-0015

### INFO-016
- **タイトル:** MCP Specification 2026-07-28 Release Candidate: stateless protocol core, Extensions framework, Tasks
- **ソース:** Model Context Protocol Blog
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic, Google, OpenAI, xAI
- **要約:** MCP仕様の2026-07-28リリース候補公開。ステートレスプロトコルコア、エクステンションフレームワーク、タスク機能を含む。Xもホスト型MCPサーバーを開始。AAIFはLinux Foundation傘下で60K+プロジェクト規模の標準化推進。
- **キーファクト:**
  - MCP RC 2026-07-28: ステートレスコア・エクステンション・タスク
  - Xがホスト型MCPサーバー開始
  - AAIF: Datavant（医療）、COOCON（6月1日参加）等が加盟
  - MCPアーキテクチャパターンarXiv論文も公開
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260702-0016

### INFO-017
- **タイトル:** Okta expands Cross App Access (XAA) ecosystem for secure AI agent-to-app management
- **ソース:** Okta Press Release
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Okta
- **要約:** OktaがCross App Access (XAA)エコシステムを拡張し、AIエージェント間・アプリ間のセキュア管理を可能に。AIエージェントのセキュアなアクセス管理の業界標準推進。
- **キーファクト:**
  - Cross App Access (XAA) エコシステム拡張
  - AIエージェント・アプリ間セキュアアクセス管理
  - アクセス管理の業界標準化推進
- **引用URL:** https://www.okta.com/newsroom/press-releases/okta-announces-cross-app-access-partners/
- **Evidence ID:** EVD-20260702-0017

### INFO-018
- **タイトル:** FactSet-Google Cloud strategic partnership for agentic AI in financial data
- **ソース:** FactSet Investor Relations
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** Google
- **要約:** FactSetがGoogle Cloudと戦略的パートナーシップを発表。FactSetのデータ・分析・ワークフローとGoogle CloudのアジェンティックAI機能・インフラを統合。金融業界でのエージェントAI実用化を加速。
- **キーファクト:**
  - FactSet × Google Cloud 戦略的パートナーシップ
  - 金融データにアジェンティックAI統合
  - 業界特化型エージェント展開のシグナル
- **引用URL:** https://investor.factset.com/news-releases/news-release-details/factset-announces-strategic-partnership-google-cloud-bring
- **Evidence ID:** EVD-20260702-0018

### INFO-019
- **タイトル:** OpenAI previews GPT-5.6 Sol: next-gen model with coding, science, cybersecurity focus
- **ソース:** OpenAI
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6 Solをプレビュー。コーディング、科学、サイバーセキュリティでより強力な能力を持ち、最先端の安全性システムをペアリング。政府に事前公開済み。
- **キーファクト:**
  - GPT-5.6 Sol プレビュー公開
  - コーディング・科学・サイバーセキュリティ特化
  - 最先端安全性システム搭載
  - 政府に事前公開
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260702-0019

### INFO-020
- **タイトル:** Gemini 3.5 Flash Computer Use now built-in; agents can see, reason, and take action
- **ソース:** Google Cloud via Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** Google Gemini 3.5 FlashにComputer Useが組み込みツールとして追加。開発者はエージェントが見て、推論し、行動を起こすものを構築可能。Gemini Embedding 2マルチモーダル本番向けモデルも公開。
- **キーファクト:**
  - Gemini 3.5 Flash Computer Use組み込みツール化
  - エージェントの視覚・推論・行動能力
  - Gemini Embedding 2 マルチモーダル本番モデル
- **引用URL:** https://www.facebook.com/googlecloud/posts/computer-use-is-now-a-built-in-tool...
- **Evidence ID:** EVD-20260702-0020

### INFO-021
- **タイトル:** Boston Dynamics + Google DeepMind partnership on AI in humanoid robots
- **ソース:** IEN
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google DeepMind
- **要約:** Boston DynamicsとGoogle DeepMindがヒューマノイドロボットAIで提携。DeepMindはGeminiロボティクス基盤モデルを前進。大規模マルチモーダルGeminiモデル上に構築。
- **キーファクト:**
  - Boston Dynamics × Google DeepMind ヒューマノイド提携
  - Gemini Robotics基盤モデル活用
  - マルチモーダルGeminiモデル基盤
- **引用URL:** https://www.ien.com/artificial-intelligence/news/22957910/boston-dynamics-google-deepmind-partner-on-ai-in-humanoid-robots
- **Evidence ID:** EVD-20260702-0021

### INFO-022
- **タイトル:** SWE-Bench Multimodal: Claude Mythos Preview leads at 0.590; WorldBench: ByteDance Seed 2.1 Pro leads at 0.676
- **ソース:** LLM Stats
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic, ByteDance
- **要約:** SWE-Bench MultimodalリーダーボードでClaude Mythos Previewが0.590で1位。WorldBenchではByteDance Seed 2.1 Proが0.676で1位。マルチモーダル・コーディング能力のベンチマーク分化進行。
- **キーファクト:**
  - SWE-Bench Multimodal: Claude Mythos Preview 0.590（1位）
  - WorldBench: Seed 2.1 Pro 0.676（1位）
  - ベンチマークの分化・多角化進行
- **引用URL:** https://llm-stats.com/benchmarks/swe-bench-multimodal
- **Evidence ID:** EVD-20260702-0022

### INFO-023
- **タイトル:** Skills can execute arbitrary code in agent environment — security warning across platforms
- **ソース:** GitHub awesome-skills
- **公開日:** 2026-07-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-005-03
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** AIエージェントスキルはエージェント環境内で任意のコードを実行可能。信頼できるソースからのみインストール推奨。SKILL.mdと全スクリプトのレビュー必要。クロスプラットフォーム（Claude/Codex/Gemini）でスキル配布エコシステム拡大。
- **キーファクト:**
  - スキルは任意コード実行可能（セキュリティリスク）
  - 信頼ソースのみ推奨・SKILL.mdレビュー必要
  - クロスプラットフォームスキル配布エコシステム拡大
  - OpenAI Skills shell実行、Theia Coder Agent Mode Shell Execution
- **引用URL:** https://github.com/gmh5225/awesome-skills
- **Evidence ID:** EVD-20260702-0023

### INFO-024
- **タイトル:** Vendor lock-in switching costs 16x; inference economics collapse at production scale
- **ソース:** VaaSBlock / DigitalApplied / TFiR
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** Microsoft, Salesforce, ServiceNow, Amazon, OpenAI
- **要約:** 2026年、エンタープライズは同時に4つのAIベンダーからスイッチングコストを負担。ベンダーロックイン状態の組織は約16倍の切替コストに直面。AIパイロットは推論経済を一次指標として扱わないため本番規模で崩壊。
- **キーファクト:**
  - ベンダーロックイン切替コスト約16倍
  - 4ベンダー同時ロックイン構造
  - AIパイロットが本番規模で推論経済崩壊
  - 50,000行のAPIコード依存で切替数ヶ月の作業
- **引用URL:** https://www.vaasblock.com/research/enterprise-ai-vendor-lock-in-switching-costs-copilot-agentforce-2026/
- **Evidence ID:** EVD-20260702-0024

### INFO-025
- **タイトル:** Multiple AI agent skill marketplaces emerge: Google Cloud, Microsoft, Salesforce, ServiceNow, OKX
- **ソース:** OKX / Agensi
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Google, Microsoft, Salesforce, ServiceNow
- **要約:** Google Cloud、Microsoft、Salesforce、ServiceNowが類似のマーケットプレイスを導入し競争的ランドスケープ形成。2026年の全AIエージェントスキルディレクトリ・マーケットプレイスの完全リストが整理される。スキル配布の標準化と囲い込みが同時進行。
- **キーファクト:**
  - 4大プラットフォームでスキルマーケットプレイス競合
  - スキル配布標準化 vs 囲い込みの同時進行
  - LobeHub等で500+ Codexスキルコミュニティ利用
- **引用URL:** https://www.agensi.io/learn/complete-list-ai-agent-skill-directories-2026
- **Evidence ID:** EVD-20260702-0025

### INFO-026
- **タイトル:** Google agents-cli: CLI and skills for building agents on Gemini Enterprise Agent Platform
- **ソース:** Google GitHub
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Google
- **要約:** Googleがagents-cliを公開。コーディングエージェントにスキルとコマンドを与え、Gemini Enterprise Agent Platform上でエージェントを構築・スケール・ガバナンス。再利用可能なカスタム指示としてのスキル管理機能。
- **キーファクト:**
  - agents-cli公開（Gemini Enterprise Platform向け）
  - コーディングエージェントにスキル・コマンド付与
  - スキル = 再利用可能カスタム指示
  - Agent Gatewayでアジェンティックワークロード管理
- **引用URL:** https://github.com/google/agents-cli
- **Evidence ID:** EVD-20260702-0026

### INFO-027
- **タイトル:** AWS Bedrock Agents Classic enters maintenance mode July 30, 2026; AgentCore adds 3 new layers
- **ソース:** AWS Documentation / AWS Insider
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon AWS
- **要約:** AWS Bedrock Agents（2023年11月ローンチ）が「Bedrock Agents Classic」となり2026年7月30日以降新規顧客受付停止。後継のAgentCoreにManaged Knowledge Base、Web Search、payments、AWS WAF AIトラフィックマネタイズの3新レイヤー追加。
- **キーファクト:**
  - Bedrock Agents Classic: 7月30日以降新規顧客停止
  - AgentCore: Managed Knowledge Base、Web Search、決済、WAF追加
  - エージェントインフラの世代交代進行
- **引用URL:** https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html
- **Evidence ID:** EVD-20260702-0027

### INFO-028
- **タイトル:** Azure AI Foundry Agent Service: MCP integration, BYOM, Agent-to-Agent (A2A) protocol
- **ソース:** Microsoft Learn
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundry Agent ServiceがMCP接続、独自モデル持ち込み（BYOM）、Agent-to-Agent（A2A）プロトコル対応。Agent 365 Skillsでローカル構築AIエージェントのエンタープライズガバナンス。AI Landing ZonesでガバナンスHub中央管理。
- **キーファクト:**
  - Foundry Agent Service: MCP統合・BYOM・A2Aプロトコル
  - Agent 365 Skills: エンタープライズガバナンス
  - AI Landing Zones: 共有ガバナンスHub中央管理
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/ai-gateway
- **Evidence ID:** EVD-20260702-0028

### INFO-029
- **タイトル:** Vertex AI Agent Builder integrated into Gemini Enterprise Agent Platform
- **ソース:** Google Cloud
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Google
- **要約:** Vertex AI Agent BuilderがGemini Enterprise Agent Platformに統合。本番対応エージェントの構築・スケール・ガバナンスを提供。Bright Data Web MCP連携で外部データアクセス。Google agents-cliで標準化スキル提供。
- **キーファクト:**
  - Vertex AI Agent Builder → Gemini Enterprise Agent Platform統合
  - 本番対応エージェント構築・スケール・ガバナンス
  - Web MCP連携で外部データアクセス
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260702-0029

### INFO-030
- **タイトル:** MIT: agentic workflows becoming backbone of cloud providers; speed/energy efficiency research
- **ソース:** MIT News
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** (業界全体)
- **要約:** MIT研究でアジェンティックワークフローが急速に複雑化し、クラウドプロバイダーのバックボーンになりつつあると指摘。AIエージェントの速度とエネルギー効率改善の研究。モデル選択の最適化がコスト削減鍵。
- **キーファクト:**
  - アジェンティックワークフローがクラウドバックボーン化
  - 速度・エネルギー効率改善研究
  - モデル選択最適化でコスト削減
- **引用URL:** https://news.mit.edu/2026/improving-ai-agent-speed-and-energy-efficiency-0625
- **Evidence ID:** EVD-20260702-0030

### INFO-031
- **タイトル:** KPMG: multi-agent orchestration doubled to 18%; AI cost challenges mount as complexity grows
- **ソース:** CFO Dive / KPMG
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** (業界全体)
- **要約:** KPMG調査で複数AIエージェントをオーケストレーションする組織の割合が9%から18%に倍増。ただし実際に統合実装しているのは13%。エージェント使用が複雑化するにつれてコスト課題が深刻化。
- **キーファクト:**
  - マルチエージェントオーケストレーション: 9%→18%（倍増）
  - 実際の統合実装: 13%
  - 複雑化でAIコスト課題深刻化
- **引用URL:** https://www.cfodive.com/news/ai-cost-challenges-rise-as-firms-lean-coordinated-agents-kpmg/823819/
- **Evidence ID:** EVD-20260702-0031

### INFO-032
- **タイトル:** Writer survey: 97% of 2400 executives deployed AI agents; only 8% see measurable value
- **ソース:** LinkedIn / Writer 2026 AI Adoption Survey
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Writerの2026年エンタープライズAI採用調査（2,400名グローバル経営者）で97%が過去1年にAIエージェントを展開。しかし88%がAI使用、わずか8%しか測定可能な価値を実感。期待と実態の大きなギャップ。
- **キーファクト:**
  - 97%の経営者がAIエージェント展開（過去1年）
  - わずか8%しか測定可能価値を実感
  - 88%組織がAI使用 vs 8%価値実感の「Great Gap」
- **引用URL:** https://www.linkedin.com/pulse/great-gap-why-88-organizations-use-ai-only-8-see-ashish-dhawan-zco4c
- **Evidence ID:** EVD-20260702-0032

### INFO-033
- **タイトル:** Gartner: 89% of AI agent pilots never scale; 40%+ agentic AI projects cancelled by 2027
- **ソース:** Beri.net / Gartner / Instagram
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Gartner State of AI Report 2026でAIエージェントパイロットの89%がスケールしない。64%のエンタープライズが運用でAI使用（1年前のパイロット段階から上昇）。2027年までにアジェンティックAIプロジェクトの40%以上がキャンセル予測（ROI不明確・データ弱体のため）。
- **キーファクト:**
  - AIエージェントパイロット89%がスケールせず
  - エンタープライズ64%が運用でAI使用
  - 2027年までに40%+プロジェクトキャンセル予測（ROI不明確）
  - グローバルAIエージェント市場: $7.84B(2025)→$52.62B(2030) CAGR46.3%
- **引用URL:** https://www.beri.net/article/ai-agent-adoption-enterprise-2026-gartner-idc
- **Evidence ID:** EVD-20260702-0033

### INFO-034
- **タイトル:** IBM Pacesetters: 21% of orgs achieve 160% AI ROI; 70% see positive outcomes in 60 days
- **ソース:** LinkedIn / IBM
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** IBM
- **要約:** IBM調査で調査対象の21%を「Pacesetters」と定義し、彼らは160%のAI ROIを達成。AIエージェント展開組織の70%が60日以内にポジティブな成果・測定可能ROIを達成。戦略的ビジョンとデータ基盤が差別化要因。
- **キーファクト:**
  - Pacesetters(21%): 160% ROI達成
  - 70%が60日以内にポジティブ成果
  - 戦略的ビジョン・データ基盤が差別化要因
- **引用URL:** https://www.linkedin.com/posts/amitzavery_every-yearinourairesearch-a-group-pulls-activity-7475932445729509376-73X7
- **Evidence ID:** EVD-20260702-0034

### INFO-035
- **タイトル:** EU AI Act high-risk obligations enforcement begins in 43 days; GPAI transparency now mandatory
- **ソース:** Alation / Instagram
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (業界全体)
- **要約:** EU AI Actのハイリスク義務執行開始まで43日。汎用AI（GPAI）プロバイダーに透明性・文書化・著作権義務が必須化。新規コンプライアンス要件はAIスタートアップ・SaaS企業・エンタープライズベンダーに影響。
- **キーファクト:**
  - ハイリスク義務執行開始まで43日
  - GPAI透明性・文書化・著作権義務必須化
  - GDPR Article 32/35とAI Act Article 10の同時トリガー
- **引用URL:** https://www.alation.com/blog/eu-ai-act-compliance-guide/
- **Evidence ID:** EVD-20260702-0035

### INFO-036
- **タイトル:** Trump Executive Order 14409: upgrade US tech systems by July 2, 2026; curbs state AI regulation
- **ソース:** Foster Swift / Brookings / White & Case
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (業界全体)
- **要約:** トランプ大統領令14409で2026年7月2日（本日）までの米国技術システム更新を要求。EO 14179（2025年1月）でAI革新への規制障壁除去を指示。さらに州のAI規制権限を抑制する大統領令に署名。米国は許容的アプローチを採りつつ州規制を抑制。
- **キーファクト:**
  - EO 14409: 2026年7月2日まで技術システム更新要求（本日期限）
  - EO 14179: AI革新への規制障壁除去
  - 州のAI規制権限を抑制する大統領令署名
  - 米国は許容的アプローチ、グローバルAI支出$2.5T予測
- **引用URL:** https://www.fosterswift.com/business-technology-law-blog/trump-ai-executive-order-cybersecurity-priorities-innovation-impact
- **Evidence ID:** EVD-20260702-0036

### INFO-037
- **タイトル:** China AI content labeling rules in effect; generative AI must uphold "core socialist values"
- **ソース:** Lawfare / Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 中国のAI生成コンテンツラベリング規則が正式施行。全AI生成テキスト・画像・音声にラベル必須。生成AIプロバイダー・ユーザーに「核心的社会主義価値」の維持と権威が指定するコンテンツの生成防止を義務付け。
- **キーファクト:**
  - AI生成コンテンツラベリング規則正式施行
  - 全AI生成コンテンツにラベル必須
  - 「核心的社会主義価値」維持義務
  - 生成AIサービス管理の初の行政規則
- **引用URL:** https://www.lawfaremedia.org/article/the-missing-resistance-in-china-s-ai-debate
- **Evidence ID:** EVD-20260702-0037

### INFO-038
- **タイトル:** Warner AI AGENT Act discussion draft: market for secure AI agents; ISO 42001 only certifiable AI standard
- **ソース:** Warner Senate / LinkedIn
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** (業界全体)
- **要約:** 上院議員WarnerがAI AGENT Act（Artificial Intelligence Access, Gatekeeper Exchange, and Nondiscriminatory Transfer Act）討議草案を公開。セキュアAIエージェントの革新的市場創出。ISO/IEC 42001が唯一認証可能なAI標準、NIST AI RMFと共に「合理的注意」ベンチマークとして明示的に受け入れ。
- **キーファクト:**
  - AI AGENT Act討議草案公開（Warner議員）
  - ISO/IEC 42001: 唯一認証可能AI標準
  - NIST AI RMF: 「合理的注意」ベンチマーク
  - 現在米国に包括的連邦AI法規なし
- **引用URL:** https://www.warner.senate.gov/newsroom/press-releases/warner-unveils-discussion-draft-of-legislation-to-create-innovative-market-for-secure-artificial-intelligence-agents/
- **Evidence ID:** EVD-20260702-0038

### INFO-039
- **タイトル:** Anthropic $200M Pentagon contract (July 2025), blacklisted after refusing autonomous weapons safeguards removal
- **ソース:** ABC News / Fortune / Kavout
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-OAI-001
- **関連企業:** Anthropic, OpenAI, Google, xAI
- **要約:** Anthropicは2025年7月に$2億ペンタゴン契約で軍の分類ネットワーク上で稼働する初のAI企業に。ペンタゴンが「完全自律型兵器・国内監視」向けセーフガード削除を最後通牒、Anthropicが拒否しサプライチェーンリスク（SCR）指定でブラックリスト化。$2億+の政府契約損失。
- **キーファクト:**
  - Anthropic $2億ペンタゴン契約（2025年7月）
  - 軍の分類ネットワーク初のAI企業
  - ペンタゴン最後通牒でセーフガード削除要求
  - Anthropic拒否→SCR指定・ブラックリスト化・$2億+損失
- **引用URL:** https://abcnews.com/Politics/pentagon-anthropic-ultimatum-ai-technology-sources/story?id=130498030
- **Evidence ID:** EVD-20260702-0039

### INFO-040
- **タイトル:** OpenAI secures Pentagon classified networks contract hours after Anthropic blacklisted; "順応報酬構造" confirmed
- **ソース:** Facebook / Firstpost
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-OAI-001
- **関連企業:** OpenAI, Anthropic
- **要約:** Anthropicブラックリスト化から数時間後、OpenAIのSam Altmanがペンタゴン分類ネットワーク向け新契約を発表。国防総省の条件に応じた。安全性を堅持したAnthropicが罰せられ、条件に順応したOpenAIが報われる「順応報酬構造」が確認された事例。
- **キーファクト:**
  - OpenAI、Anthropicブラックリスト化数時間後にペンタゴン契約
  - Sam Altmanが国防総省条件に順応
  - 安全性堅持企業が罰せられ順応企業が報われる構造確認
  - Google、xAIも分類ネットワーク契約
- **引用URL:** https://www.facebook.com/firstpostin/posts/us-grants-limited-access-to-anthropics-new-ai-model...
- **Evidence ID:** EVD-20260702-0040

### INFO-041
- **タイトル:** Pentagon signed AI contracts with Google, OpenAI, xAI for classified networks; expanding military AI capabilities
- **ソース:** Kavout
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Google, OpenAI, xAI
- **要約:** ペンタゴンがGoogle、OpenAI、xAIと分類ネットワーク向けAI契約を締結。2025年7月に4つのフロンティアAI企業（Anthropic含む）に最大$2億の契約。軍のAI能力を拡大。Anthropicを除く3社が継続。
- **キーファクト:**
  - ペンタゴン×Google/OpenAI/xAI 分類ネットワーク契約
  - 4社各最大$2億契約（2025年7月）
  - Anthropicを除く3社が継続
  - Palantir $7.95億国防総省契約
- **引用URL:** https://www.kavout.com/market-lens/what-sparked-the-pentagon-s-unprecedented-supply-chain-risk-label-for-anthropic
- **Evidence ID:** EVD-20260702-0041

### INFO-042
- **タイトル:** Pentagon formally designates Anthropic "Supply-Chain Risk to National Security" via Defense Secretary Hegseth
- **ソース:** ABC News / CNN / Bloomberg
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 国防長官Pete HegsethがAnthropicを正式に「国家安全保障上のサプライチェーンリスク」に指定。通常は外国の敵対国に繋がる企業向けの指定。Anthropicは提訴中。ホワイトハウスは輸出規制解除後に不一致で指定。評価額・パートナーシップに影響。
- **キーファクト:**
  - 国防長官HegsethがAnthropic SCR正式指定
  - 通常は外国敵対国向けの指定を国内AI企業に適用（前例）
  - Anthropicが提訴でSCR指定取り消し求める
  - 評価額・パートナーシップへの影響
- **引用URL:** https://www.facebook.com/ABCNewsLive/posts/the-ai-company-anthropic-was-granted-approval-by-the-trump-administration-to-rel/1410875800896544/
- **Evidence ID:** EVD-20260702-0042

### INFO-043
- **タイトル:** AI executives quietly seek Trump clarity after Anthropic ban; Defense Production Act June 12 directive
- **ソース:** AIWeekly / Chamberlain Hrd
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-OAI-001
- **関連企業:** (業界全体)
- **要約:** Anthropic SCR指定後、AI業界幹部が静かにトランプ政権に明確化を求める。6月12日トランプ政権の輸出管理指令で、国家安全保障上のリスクを持つAIモデルを開発する企業に国防生産法に基づく連邦政府通知を義務付け。萎縮効果の構造的リスク。
- **キーファクト:**
  - AI業界幹部がAnthropic禁止後に政権に明確化要求
  - 6月12日輸出管理指令: 国防生産法に基づく通知義務
  - 国家安全保障リスクAIモデル開発の政府通知義務化
  - 萎縮効果の構造的リスク
- **引用URL:** https://aiweekly.co/alerts/ai-executives-quietly-seek-trump-clarity-after-anthropic-ban
- **Evidence ID:** EVD-20260702-0043

### INFO-044
- **タイトル:** "Expressive Governance": First Amendment threat — government weaponizing national security to destroy business for safety stance
- **ソース:** Tech Policy Press
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 「表現的ガバナンス」が改正第1修正の脅威と指摘。政府が国家安全保障を武器化し、公共の重要性に関する見解を持つ企業を破壊すべきでないと論評。Anthropic事件は安全性姿勢への政府報復の先例。Guardrails ActでトランプAI大統領令撤回を目指す動き。
- **キーファクト:**
  - 「表現的ガバナンス」= 第1修正脅威
  - 政府が安全保障を武器化して企業を破壊
  - Guardrails Act: トランプAI大統領令撤回目指す
  - 個人が政府職員を提訴する私的権利法案
- **引用URL:** https://www.techpolicy.press/expressive-governance-is-a-first-amendment-threat-hiding-in-plain-sight
- **Evidence ID:** EVD-20260702-0044

### INFO-045
- **タイトル:** GMAC survey: 1 in 3 employers replacing entry-level jobs with AI (coding, data, customer service)
- **ソース:** Fortune / GMAC Recruiters Survey
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** GMACリクルーターズ調査で3分の1の雇用主がエントリーレベルの仕事をAIに置き換えていると認める。コーディング、データ処理、カスタマーサービスでのルーチンタスク自動化が加速。Gen Zの採用市場に直接影響。
- **キーファクト:**
  - 3分の1の雇用主がエントリーレベル置換を認める
  - コーディング・データ処理・CSでの自動化加速
  - Gen Z採用市場への直接影響
  - テクノロジー・製造業が最もリスク高い
- **引用URL:** https://fortune.com/2026/06/26/gen-z-entry-level-jobs-replaced-by-ai-new-gmac-recruiters-survey-tech-manufacturing-jobs-most-at-risk/
- **Evidence ID:** EVD-20260702-0045

### INFO-046
- **タイトル:** Klarna cut 50% workforce over 4 years, replaced 700 CS agents with AI; quietly rehiring humans — "layoff boomerang"
- **ソース:** Hoodline / Instagram / Tech.co
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna
- **要約:** Klarnaは4年間で従業員50%削減（5,500→3,400人）。700人のカスタマーサービスをAIに置換し$1000万節約と公言。しかし2025年に静かに人間の再採用を開始。「レイオフ・ブーメラン」現象。Elasticも281人（7%）削減しAI中心に再編。
- **キーファクト:**
  - Klarna従業員50%削減（4年で5,500→3,400人）
  - 700人CSをAI置換、$1000万節約
  - 2025年に静かに人間再採用（レイオフ・ブーメラン）
  - Elastic 281人（7%）削減でAI中心再編
- **引用URL:** https://www.facebook.com/Hoodline/posts/elastic-will-cut-about-281-jobs-7-of-staff-and-reorganize-around-ai-saying-autom/1605132298289349/
- **Evidence ID:** EVD-20260702-0046

### INFO-047
- **タイトル:** AI agents: 90-95% accuracy on routine tasks but only 2-3% completion on human-like gigs; best models 30.3% autonomous
- **ソース:** SimSpace / X / Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** AIエージェントはルーチン・構造化タスクで90-95%の精度だが、人間らしいギグタスクでは2-3%の完了率のみ。最高モデル（Gemini 2.5 Pro）でも完全自律で30.3%のタスク完了。Remote Labor IndexでAIは96%以上の専門タスクで人間品質に届かない。
- **キーファクト:**
  - ルーチンタスク精度90-95%
  - 人間らしいギグタスク完了率2-3%（$1,810/$143,991）
  - 最高モデル完全自律完了率30.3%
  - Remote Labor Index: 96%+専門タスクで人間品質未達
- **引用URL:** https://simspace.com/blog/benchmarking-ai-agents-against-human-analysts-under-identical-conditions/
- **Evidence ID:** EVD-20260702-0047

### INFO-048
- **タイトル:** McKinsey: over half of media spend flows through direct buying; AI powers entire campaign formats on Google/Meta
- **ソース:** McKinsey via Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google, Meta
- **要約:** メディア支出の過半数が直接購入チャネルに移行。GoogleとMetaでAIがキャンペーンフォーマット全体を駆動。よりスマートな予算配分・ターゲティング・配信を実現。「Agentic Advertising 2026」でMetaの自動化はMeta向けに最適化されると指摘。
- **キーファクト:**
  - メディア支出過半数が直接購入チャネルへ
  - Google/MetaでAIがキャンペーン全体を駆動
  - Meta自動化はMeta自身向けに最適化（非効率の懸念）
  - AI広告で予算配分・ターゲティング自動化
- **引用URL:** https://www.facebook.com/McKinsey/posts/more-than-half-of-media-spend-already-flows-through-direct-buying-channels-and-w/1541891344073550/
- **Evidence ID:** EVD-20260702-0048

### INFO-049
- **タイトル:** AI in marketing: 39% revenue increase, 37% cost reduction; 37% productivity improvement vs 12% traditional
- **ソース:** Berkeley CMR / Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05, KIQ-004-04
- **関連企業:** (業界全体)
- **要約:** マーケティングにAIを実装した企業は39%の収益増・37%のコスト削減を報告。AIマーケティングチームは37%の生産性向上（従来手法は12%）。アルゴリズミックCMOの台頭でAIガバナンスが中核マーケティング能力に。中間事業者のバリューチェーン侵食進行。
- **キーファクト:**
  - AIマーケティング: 収益39%増・コスト37%減
  - 生産性向上: AI 37% vs 従来12%
  - アルゴリズミックCMOの台頭
  - AIガバナンスが中核マーケティング能力に
- **引用URL:** https://cmr.berkeley.edu/2026/06/the-algorithmic-cmo-why-governing-ai-is-now-a-core-marketing-competency/
- **Evidence ID:** EVD-20260702-0049

### INFO-050
- **タイトル:** SaaS disruption by AI agents: 40% enterprise apps integrating AI agents by end 2026; CRM/ERP autonomous action
- **ソース:** SAP / SaaSHunt / Moonstack
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** (業界全体)
- **要約:** 2026年末までにエンタープライズアプリの40%がタスク固有AIエージェント統合（2025年8月の5%未満から）。CRM/ERP/SaaSで自律的にデータ認識・推論・行動するエージェントが展開。SaaSビジネスモデルの自動化・チャーン削減・スケール支援。
- **キーファクト:**
  - エンタープライズアプリ40%がAIエージェント統合（2026末）
  - CRM/ERP/SaaSで自律的エージェント展開
  - SaaSビジネスモデル変革（チャーン削減・スケール）
  - 統合戦略なしではAIスケール失敗
- **引用URL:** https://www.sap.com/netherlands/blogs/why-ai-fails-to-scale-without-integration-strategy
- **Evidence ID:** EVD-20260702-0050

### INFO-051
- **タイトル:** AI API pricing 2026: extreme divergence, 300x gap; DeepSeek undercuts OpenAI by 91%
- **ソース:** APIpulse / Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01, KIQ-003-03
- **関連企業:** OpenAI, DeepSeek, Anthropic
- **要約:** 2026年のAI API市場は極端な価格差が定義づけ。最安と最高のギャップが300倍に拡大。DeepSeekはOpenAIより91%安価。複数APIの組み合わせが複数サブスクリプションより費用対効果高い。
- **キーファクト:**
  - 最安/最高モデル価格差300倍
  - DeepSeek: OpenAIより91%安価
  - 複数API組み合わせが複数サブスクより費用効率的
  - 42モデル比較レポート公開
- **引用URL:** https://www.getapipulse.com/ai-api-pricing-report-2026.html
- **Evidence ID:** EVD-20260702-0051

### INFO-052
- **タイトル:** OpenAI GPT-5.5 pricing $5/$30 per 1M tokens; pro reasoning $30/$180; inference costs cut >50%
- **ソース:** Amnic / WhatChangedNow / Instagram
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAI GPT-5.5フラグシップは$5/1M入力、$30/1M出力。GPT-5.5 pro推論は$30/$180。The Information報道でOpenAIが推論コストを半分以上削減する方法を発見。エンタープライズ向けにより予測可能な価格設定。
- **キーファクト:**
  - GPT-5.5: $5/1M入力・$30/1M出力
  - GPT-5.5 pro: $30/$180
  - 推論コスト50%以上削減（The Information）
  - エンタープライズ価格の予測可能性
- **引用URL:** https://amnic.com/blogs/openai-api-pricing
- **Evidence ID:** EVD-20260702-0052

### INFO-053
- **タイトル:** Anthropic Claude Sonnet 5: $2/$10 intro pricing through Aug 2026; Opus 4.6 $15/$75; Fable 5/Mythos 5 $10 input
- **ソース:** Anthropic / AI Pricing Guru / Kingy AI
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 5は2026年8月31日まで導入価格$2/$10 per 1M、以降$3に。Opus 4.6は$15/$75 per MTok（Opusの3倍）。Haiku 4.5は$1からFable 5/Mythos 5は$10まで幅広い階層。2026年使用量ベース課金への移行。
- **キーファクト:**
  - Sonnet 5: $2/$10（導入価格、8/31まで）→ $3以降
  - Opus 4.6: $15/$75 per MTok
  - Haiku 4.5: $1/1M入力（最低）
  - Fable 5/Mythos 5: $10/1M入力
  - 使用量ベース課金への移行
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-5
- **Evidence ID:** EVD-20260702-0053

### INFO-054
- **タイトル:** Meta courts agencies as AI ad tools expand and reshape roles; creative at scale automated
- **ソース:** Digiday / Adweek
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta
- **要約:** MetaがAI広告ツール拡大でエージェンシーを取り込みつつ役割を再構築。プラットフォームがより自動化されたマーケティングツールを展開し広告主の参入障壁を低下。クリエイティブ制作（DALL·E、Midjourney等）のスケール自動化。中間事業者の役割変容進行。
- **キーファクト:**
  - Meta AI広告ツール拡大でエージェンシー取り込み
  - 参入障壁低下・自動化マーケティングツール展開
  - クリエイティブ制作スケール自動化
  - 広告業界全体の役割再構築
- **引用URL:** https://digiday.com/podcasts/with-ai-ad-tools-expanding-meta-courts-agencies-while-reshaping-their-role/
- **Evidence ID:** EVD-20260702-0054

### INFO-055
- **タイトル:** All frontier models >90% MMLU; GPQA Diamond GPT-5.4/Gemini 3.1 Pro tied ~94%; ARC-AGI-3 <1% for frontier
- **ソース:** TeamAI / Snorkel AI / AI Frontiers
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** 2026年初頭、全フロンティアモデルがMMLUで90%超。GPQA DiamondでGPT-5.4（94.4%）とGemini 3.1 Pro（94.3%）が事実上同点。ARC-AGI-3では人間が100%解けるタスクでフロンティアモデルが1%未満。標準ベンチマークの天井到達と新ベンチマークの分化が同時進行。
- **キーファクト:**
  - 全フロンティアモデルMMLU 90%超
  - GPQA Diamond: GPT-5.4 94.4% / Gemini 3.1 Pro 94.3%
  - ARC-AGI-3: フロンティアモデル1%未満（人間100%）
  - BenchPress 5プローブセットでスコア予測（MedAE 3.93）
- **引用URL:** https://teamai.com/blog/large-language-models-llms/best-ai-models-for-complex-reasoning-2026/
- **Evidence ID:** EVD-20260702-0055

### INFO-056
- **タイトル:** GLM-5.2 (Zhipu/blacklisted China) tops open-weight rankings on Huawei silicon; Grok 4 #1 overall on Artificial Analysis
- **ソース:** Tom's Hardware / Artificial Analysis
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** Zhipu, xAI
- **要約:** ブラックリスト済み中国企業ZhipuのGLM-5.2が全Huaweiシリコン上でオープンウェイトAIランキング1位。Artificial Analysis Intelligence Index v4.1で51点（MiniMax-M3、DeepSeekを上回る）。Grok 4は同指数で73点で全体1位の「最もインテリジェント」。
- **キーファクト:**
  - GLM-5.2（Zhipu）オープンウェイト1位（Huaweiシリコン）
  - Artificial Analysis Intelligence Index: GLM-5.2 51（OSS1位）
  - Grok 4: Intelligence Index 73（全体1位）
  - 中国OSSモデルの性能向上顕著
- **引用URL:** https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-free-glm-5-2-tops-the-open-weight-ai-rankings-on-all-huawei-silicon
- **Evidence ID:** EVD-20260702-0056

### INFO-057
- **タイトル:** Open vs closed LLM gap narrowing dramatically; DeepSeek/GLM closing in but real-world delta remains
- **ソース:** Forgepoint Capital / Hakia / HN
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek, Zhipu, Meta, Mistral
- **要約:** オープンソースとクローズドLLMの性能ギャップが急速に縮小。DeepSeekとGLMがトップ西洋モデルとの差を縮める。ただし実際の作業ではオープンモデルが「ベンチマックス」されており有意な差が残存。オープンウェイトモデルは私企業の慈善の産物という構造的問題。
- **キーファクト:**
  - オープン/クローズドギャップ急速縮小
  - DeepSeek/GLMが西洋モデルに迫る
  - 実作業では有意な性能差残存
  - オープンウェイト = 私企業の慈善という構造的問題
- **引用URL:** https://forgepointcap.com/perspectives/margin-of-safety-60-open-source-ai-is-back-and-nobodys-hands-are-clean/
- **Evidence ID:** EVD-20260702-0057

### INFO-058
- **タイトル:** AI startups raised $202B in 2025 (~50% of global VC); Baseten $1.5B Series F; Anthropic potential $200-300B revenue by 2027
- **ソース:** SecondTalent / DropStab / Instagram
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, Baseten
- **要約:** AIスタートアップは2025年に約$2020億調達（全グローバルVCの約50%、2024年の34%から上昇）。基盤モデル/LLMが約$800億（40%）獲得。Baseten（AI推論）が$15億Series F。Gavin Baker予測でAnthropicは2026年末$1000億、2027年末$2000-3000億収益の可能性。
- **キーファクト:**
  - AIスタートアップ$2020億調達（2025年、全VC約50%）
  - 基盤モデル/LLM: 約$800億（40%）
  - Baseten: $15億Series F（AI推論）
  - Anthropic: 2027年末$2000-3000億収益可能性
- **引用URL:** https://www.secondtalent.com/resources/ai-startup-funding-investment/
- **Evidence ID:** EVD-20260702-0058

### INFO-059
- **タイトル:** Hyperscaler capex $725B in 2026; McKinsey $5.2T data center investment needed by 2030
- **ソース:** Yahoo Finance / McKinsey / Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Microsoft, Amazon, Google
- **要約:** ハイパースケーラーが2026年に最大$7250億の資本支出を計画（大部分がAIインフラ）。McKinsey推計で2030年までに$5.2兆のデータセンター投資が必要。Microsoftは日本に$100億、GMI Cloudは$120億投資。AI企業がデータセンター建設のために債務発行。
- **キーファクト:**
  - ハイパースケーラーcapex最大$7250億（2026年）
  - 2030年までに$5.2兆データセンター投資必要
  - Microsoft日本$100億、GMI Cloud $120億
  - AI企業のデータセンター建設向け債務発行
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/ai-demand-begins-justify-massive-110000106.html
- **Evidence ID:** EVD-20260702-0059

### INFO-060
- **タイトル:** Global corporate AI investment $581.7B in 2025 (+130% YoY); generative AI market $103.58B → $1,260B by 2034
- **ソース:** LeadWithAI / Fortune Business Insights
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** (業界全体)
- **要約:** 2025年のグローバル企業AI投資は$5817億（前年比+130%）、民間投資のみ$3447億（+127.5%）。生成AI市場は2025年$1035.8億から2034年に$1兆2601.5億へ成長予測。M&A大型取引が支配的でAIがテクノロジー以外のセクターも牽引。
- **キーファクト:**
  - 企業AI投資$5817億（2025年、+130% YoY）
  - 民間投資$3447億（+127.5%）
  - 生成AI市場: $1035.8億(2025)→$1兆2601.5億(2034)
  - M&A大型取引（$100億超）が支配的
- **引用URL:** https://www.leadwithai.co/guides/ai-statistics
- **Evidence ID:** EVD-20260702-0060

### INFO-061
- **タイトル:** Anthropic disabled both models globally within hours of government directive — sovereignty/switching risk
- **ソース:** Digital Applied / DevOps.com
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-05, KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** Anthropicが政府指令（午後5:21ET）を受けた後、リアルタイムで国籍を検証する方法がなく数時間以内に両モデルを全球規模で無効化。「政府が一夜でAIを切り替えられる」リスクの実証。AnthropicはAWS/GCP上のClaude Code向けセルフホストゲートウェイ追加。OpenAI APIアクセスをTOS違反で取り消し。
- **キーファクト:**
  - Anthropicが政府指令で数時間以内に両モデル全球無効化
  - リアルタイム国籍検証不可が原因
  - Claude Code用セルフホストゲートウェイ（AWS/GCP）
  - OpenAIのClaude APIアクセスをTOS違反で取り消し
- **引用URL:** https://www.digitalapplied.com/blog/ai-vendor-continuity-single-model-risk-checklist-2026
- **Evidence ID:** EVD-20260702-0061

### INFO-062
- **タイトル:** Stanford Digital Economy Lab: entry-level tech postings down 67% (2023-2024); engineering roles down 11%
- **ソース:** Linux Foundation / Biggo Finance
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** Stanford Digital Economy Lab統計でエントリーレベル技術求人が2023-2024年に67%減少、雇用13%減。大手テック採用は2019年比25%縮小だがエンジニアリング職は11%減のみ。ヨーロッパでは2025年にジュニアテック採用3%縮小。AIコーディングツールがジュニア需要を再構築。
- **キーファクト:**
  - エントリーレベル技術求人67%減（2023-2024）
  - 雇用13%減少
  - 大手テック採用25%縮小（vs 2019）、エンジニア職は11%減のみ
  - ヨーロッパ ジュニアテック採用3%縮小（2025年）
- **引用URL:** https://www.facebook.com/TheLinuxFoundation/posts/europes-junior-tech-hiring-contracted-3-in-2025-in-the-rest-of-the-world-it-grew/1664536229051773/
- **Evidence ID:** EVD-20260702-0062

### INFO-063
- **タイトル:** Autonomous marketing: AI agents independently plan/execute/optimize campaigns; Google/Meta AI micro-second ad placement
- **ソース:** Braze / Adweek
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** Google, Meta
- **要約:** 自律型マーケティングの台頭：AIエージェントが最小限の人間介入でキャンペーンを独立して計画・実行・最適化・反復。Google AdsとMeta Adsは「AIでマイクロ秒単位で広告を販売・ターゲティング・配置」。制御は手動クリックからルール・ログ・承認・システム設計へ移動。
- **キーファクト:**
  - 自律型マーケティング: AIが独立してキャンペーン計画・実行・最適化
  - Google/Meta: マイクロ秒単位のAI広告販売・ターゲティング
  - 制御の移動: 手動クリック→ルール・ログ・承認・システム設計
- **引用URL:** https://www.braze.com/resources/articles/autonomous-marketing
- **Evidence ID:** EVD-20260702-0063

### INFO-064
- **タイトル:** Gartner: AI coding costs to surpass developer salaries by 2028; 68% devs expect AI proficiency as job requirement
- **ソース:** Gartner / Uvik / LinkedIn
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** (業界全体)
- **要約:** Gartner予測でAIコーディングコストが2028年までに平均開発者給与を上回る（約$2,000/月）。68%の開発者がAI習熟を職務要件化すると予想。82%がコード記述時間短縮を報告し、業務はAI出力の指示・評価・修正へ移行。AIエンジニア年収中央値$131,490。
- **キーファクト:**
  - AIコーディングコストが2028年に開発者給与超過（約$2,000/月）
  - 68%開発者がAI習熟を職務要件化と予想
  - 82%がコード記述時間短縮、業務は指示・評価・修正へ
  - AIエンジニア中央値年収$131,490
- **引用URL:** https://www.facebook.com/ExpressComputerOnline/posts/gartner-predicts-ai-coding-costs-will-surpass-average-developer-salaries-by-2028/1664145792384220/
- **Evidence ID:** EVD-20260702-0064

### INFO-065
- **タイトル:** New AI roles emerging: AI Transformation Strategist, AEO/GEO specialist, AI product manager, prompt engineer
- **ソース:** Lexington Chronicle / Siemens / Scribe / LinkedIn
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** Siemens, Scribe
- **要約:** AIが新職種を創出: AI Transformation Strategist、AEO/GEO専門家、AIプロダクトマネージャー、プロンプトエンジニア。SiemensやScribeが採用中。「戦略家・オペレーター・フューチャリスト」の兼務。AIがタスクを代替する一方、人間の共感・リーダーシップ・ストーリーテリング・批判的思考は不可 replaceable。
- **キーファクト:**
  - 新職種: AI Transformation Strategist、AEO/GEO専門家、AI PM
  - Siemens/Scribeが採用中（「戦略家・オペレーター・フューチャリスト」兼務）
  - 人間スキル不可replaceable: 共感・リーダーシップ・ストーリーテリング
- **引用URL:** https://www.lexingtonchronicle.com/premium/stacker/stories/ai-is-inventing-new-jobs-we039ve-seen-this-before,184052
- **Evidence ID:** EVD-20260702-0065

### INFO-066
- **タイトル:** ARC-AGI-3: Continual Harness 20.54% at $774 outperforms Hermes baseline; DiARC Qwen3 96%+ on ARC-AGI-1
- **ソース:** arXiv / X
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic, Google DeepMind, OpenAI, xAI
- **要約:** ARC-AGI-3でContinual Harnessが20.54%（$774）を達成、Hermes基準（8.25%、$5,674）をコスト効率で圧倒。DiARC手法でQwen3がARC-AGI-1/MiniARC/ConceptARCで96%超。4フロンティアラボ（Anthropic/DeepMind/OpenAI/xAI）が2025年にARC-AGI性能をモデルカードで公開し基準確立。
- **キーファクト:**
  - ARC-AGI-3: Continual Harness 20.54%（$774）vs Hermes 8.25%（$5,674）
  - DiARC: Qwen3がARC-AGI-1/MiniARC/ConceptARC 96%超
  - 4フロンティアラボが2025年にARC-AGI性能公開
  - ARCスタイルベンチマークの急速進展
- **引用URL:** https://x.com/GregKamradt/status/2072069905286127888
- **Evidence ID:** EVD-20260702-0066

### INFO-067
- **タイトル:** The AI Scientist: automating research lifecycle, creating new knowledge autonomously at superhuman speed
- **ソース:** Instagram / MIT Technology Review / Argonne
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** (業界全体)
- **要約:** 「AI Scientist」が研究ライフサイクルの自動化ビジョンを実現。人間科学者のように新しい知識を自律的に創造、ただし超人的速度で睡眠・休憩不要。ロボティクスとAIの相乗効果で材料科学・創薬・物理学の発見を加速。AGI進展が「かつてない速度」で進行中。
- **キーファクト:**
  - AI Scientist: 研究ライフサイクル自動化
  - 新知識を自律創造（超人的速度・休憩不要）
  - ロボティクス×AIで科学発見加速
  - AGI進展が「かつてない速度」
- **引用URL:** https://www.facebook.com/technologyreview/posts/the-company-is-doubling-down-on-ai-for-science/1380022720653541/
- **Evidence ID:** EVD-20260702-0067

### INFO-068
- **タイトル:** Demis Hassabis: AGI may not need breakthrough; claims "AGI achieved summer 2020" (debated); Amodei says upside underestimated
- **ソース:** Instagram / Financial Times / Instagram
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google DeepMind, Anthropic
- **要約:** Demis HassabisがAGIに大きなブレークスルーは不要と示唆し、「2020年夏にAGIを達成した」と大胆主張（即座に反論・激論）。Dario Amodeiは「AGIの急進的なプラス面を過小評価している人が多い」。モデルが強力になるにつれオープンソースAI議論の重要性増大、議会証言。
- **キーファクト:**
  - Hassabis: AGIにブレークスルー不要、2020年夏AGI達成主張（議論呼ぶ）
  - Amodei: AGIのプラス面過小評価
  - オープンソースAI議論の重要性増大
  - 議会証言で安全性姿勢強調
- **引用URL:** https://www.instagram.com/reel/DaJVfzDCoog/
- **Evidence ID:** EVD-20260702-0068

### INFO-069
- **タイトル:** AI safety requires Congressional action; UK-Germany joint statement; RAND tabletop exercises find governance gaps
- **ソース:** Sen. Blumenthal / RAND / UK Gov
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** (業界全体)
- **要約:** AI安全性に議会行動が必要との声（Blumenthal議員、Obernolte下院議員の議会ロードマップ）。英独が先進AI安全性・セキュリティ共同声明。RANDが欧州（独・蘭・仏）のテーブルトップ演習でガバナンス格差特定。輸出規制が米AI産業の基盤を揺るがすとの懸念。
- **キーファクト:**
  - 議会行動要求（Blumenthal・Obernolteロードマップ）
  - 英独 先進AI安全性共同声明
  - RAND欧州テーブルトップ演習でガバナンス格差特定
  - 輸出規制が米AI産業基盤への戦略的リスク
- **引用URL:** https://www.rand.org/pubs/research_reports/RRA5082-1.html
- **Evidence ID:** EVD-20260702-0069

### INFO-070
- **タイトル:** 豆包2.1シリーズ + Seedance 2.5 + 多モーダル新製品集中リリース; 豆包専業版有料サブスク開始
- **ソース:** 東方財富網 / Instagram / Atlas Cloud
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 字節跳動が豆包2.1シリーズ、Seedance 2.5動画生成モデル、多数のマルチモーダル新製品を一斉リリース。豆包専業版の有料サブスクリプションが開始。Seedance 2.0 Mini（2026年6月中旬）は標準版比50%コスト削減・2倍高速化。火山方舟MaaSで豆包+主流大モデルのプラグインエコシステム提供。
- **キーファクト:**
  - 豆包2.1シリーズ・Seedance 2.5・マルチモーダル新製品集中リリース
  - 豆包専業版有料サブスク開始
  - Seedance 2.0 Mini: 標準版比50%コスト削減・2倍高速（6月中旬）
  - 火山方舟MaaS: 豆包+主流モデル・プラグインエコシステム
- **引用URL:** https://finance.eastmoney.com/a/202606253783359647.html
- **Evidence ID:** EVD-20260702-0070

### INFO-071
- **タイトル:** 中国AI市場API価格競争激化: ByteDance Doubao-seed-2.0-mini $0.90; DeepSeek依存で市場高度競争段階へ
- **ソース:** Threads / Volcengine
- **公開日:** 2026-07-02
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-01
- **関連企業:** ByteDance, DeepSeek
- **要約:** 中国主要LLMのAPI定価変化で中国AI市場が高度競争段階に入ったことが分かる。ByteDanceのDoubao-seed-2.0-miniが$0.90等の低価格設定。Seedance 2.0 APIが火山エンジン方舟プラットフォームで提供。過去四半期で価格競争が激化。
- **キーファクト:**
  - 中国AI市場が高度競争段階へ（API価格面）
  - ByteDance Doubao-seed-2.0-mini $0.90
  - Seedance 2.0 API 火山エンジン方舟で提供
  - 過去四半期で価格競争激化
- **引用URL:** https://www.threads.com/@jackieyutw/post/DaE5sDXFG5U/
- **Evidence ID:** EVD-20260702-0071

### INFO-072
- **タイトル:** 豆包MAU 3.45億（2026年3月）で2位千問+3位DeepSeekの合計超; 有料化で600万ユーザー流出
- **ソース:** 腾讯新闻 / 国际金融报 / 钛媒体
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** QuestMobileデータで豆包MAU 3.45億（2026年3月）、2位千問（1.66億）と3位DeepSeek（1.27億）の合計を超える。日活ピーク1.5億突破。ただし有料化発表後の2026年5月にMAU 3.3億に低下、600万ユーザー流出。大模型日均tokens調用量180万億次（1500倍増）。
- **キーファクト:**
  - 豆包MAU 3.45億（2026年3月）- 千問+DeepSeek合計超
  - 日活ピーク1.5億突破
  - 有料化後: 2026年5月MAU 3.3億、600万ユーザー流出（-1.81%）
  - 大模型日均tokens調用量180万億次（1500倍増）
- **引用URL:** https://view.inews.qq.com/a/20260628A06W1G00
- **Evidence ID:** EVD-20260702-0072

### INFO-073
- **タイトル:** 字節跳動$200億融資＋2026年AI資本支出2000億元超; 日算力費vs日収入ギャップ数十倍継続
- **ソース:** ZAKER / 钛媒体 / Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** 字節跳動が$200億融資を発表（期限3-5年、AI関連業務向け）。2026年AI資本支出計画を2000億元超に上方修正。豆包の日算力消費は数千万元だが日収入は不足百万元でギャップ数十倍継続。Anew Labs（AI制薬）を拆分独立融資。30名以上の中高层人材が起業。
- **キーファクト:**
  - $200億融資（期限3-5年、AI業務向け）
  - 2026年AI資本支出2000億元超に上方修正
  - 日算力費数千万元 vs 日収入不足百万元（ギャップ数十倍）
  - Anew Labs AI制薬業務拆分独立融資
  - 30名以上中高层人材が起業
- **引用URL:** https://app.myzaker.com/news/article.php?pk=6a436c5ab15ec036a104a550
- **Evidence ID:** EVD-20260702-0073

### INFO-074
- **タイトル:** Coze (扣子) 智能体平台: ノーコード構築、学生向けテンプレート拡大; Anew Labs AI制薬
- **ソース:** 淘宝 / 搜狐 / ZAKER
- **公開日:** 2026-07-02
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのCoze（扣子）智能体平台がノーコード構築を提供。学生向けテンプレート（課程問答、PPT生成、答弁補助）を含む。百度文心智能体等と共に中国主要AI智能体プラットフォーム。火出方舟MaaSで豆包+主流大モデルのプラグインエコシステム。
- **キーファクト:**
  - Coze（扣子）ノーコード智能体構築
  - 学生向けテンプレート拡大（課程問答・PPT生成・答弁補助）
  - 百度文心智能体等とプラットフォーム競合
  - 火出方舟MaaSでプラグインエコシステム
- **引用URL:** https://www.sohu.com/a/1042504459_99900770
- **Evidence ID:** EVD-20260702-0074

### INFO-075
- **タイトル:** OpenAI/Anthropic/Amazon/Microsoft join Raimondo-led workforce transition effort; Gartner: half of AI-lost jobs reversed by 2027
- **ソース:** NYT / Gartner / Instagram
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-04, KIQ-004-03
- **関連企業:** OpenAI, Anthropic, Amazon, Microsoft
- **要約:** OpenAI/Anthropic/Amazon/MicrosoftがGina Raimondo元商務長官主導の米国労働力AI移行支援に参加。Gartner予測でAIで失われた仕事の半分は2027年までに逆転（古い仕事に戻るのでなく新しい仕事創出）。AI moatはモデルではなく顧客相互作用・運用履歴・組織的知識。
- **キーファクト:**
  - 4社がRaimondo主導労働力移行支援に参加
  - Gartner: AI喪失仕事の半分が2027年までに逆転（新職種）
  - AI moat = 顧客相互作用・運用履歴・組織的知識（モデル非ず）
  - リスキリング投資加速
- **引用URL:** https://www.nytimes.com/2026/06/25/business/economy/ai-work-force-training-job-losses.html
- **Evidence ID:** EVD-20260702-0075

### INFO-076
- **タイトル:** LLM Leaderboard 2026: 40+ models ranked; DeepSeek V4 (1T params) cost-efficient; China open-weight ecosystem leads community quality
- **ソース:** af.net / DeepSeek / Our World in Data
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** DeepSeek, Alibaba, OpenAI, Anthropic, Google
- **要約:** LLMリーダーボード2026が40+モデル（GPT-5.5、Claude Opus、Gemini 3.1 Pro）をランク付け。DeepSeek V4（1Tパラメータ）はコスト効率で明確な勝者。中国のオープンウェイトエコシステム（Qwen、DeepSeek）がコミュニティ品質・開発者採用で米国をリード。OpenWebUI 10万+ユーザーの実使用データ比較も公開。
- **キーファクト:**
  - 40+モデル比較リーダーボード（GPT-5.5/Claude Opus/Gemini 3.1 Pro）
  - DeepSeek V4（1Tパラメータ）コスト効率勝者
  - 中国オープンウェイト（Qwen/DeepSeek）がコミュニティ品質で米国リード
  - 10万+ユーザー実使用データ比較
- **引用URL:** https://af.net/realtime/llm-leaderboard-2026-ai-model-rankings-benchmarks-and-price-comparison/
- **Evidence ID:** EVD-20260702-0076

### INFO-077
- **タイトル:** Llama 4 Maverick best overall, Scout 10M context; Mistral gains on EU sovereignty/cost; open models won't replace frontier in enterprise
- **ソース:** stob.ai / Qualitate / X
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, Mistral, Alibaba
- **要約:** Llama 4 Maverickが総合最高、Scoutが1000万コンテキスト専門。Mistral/Hugging Faceはコスト効率・EUデータ主権・ファインチューニング・自己ホストで獲得。ただしエンタープライズ支配モデル（Llama 4、Mistral Large 3、Qwen 3）はプロバイナンス文書が不完全。オープンモデルがエンタープライズのフロンティアAIを置換するという議論に反論。
- **キーファクト:**
  - Llama 4 Maverick総合最高、Scout 1000万コンテキスト
  - Mistral: コスト効率・EU主権・自己ホストで獲得
  - 支配的OSSモデルはプロバイナンス文書不完全
  - オープンモデルのフロンティア置換に反論
- **引用URL:** https://rajatpandit.com/ai-engineering/open-source-ai-tipping-point-2026
- **Evidence ID:** EVD-20260702-0077

### INFO-078
- **タイトル:** Forrester: 55% of employers regret AI cuts; companies quietly rehiring (IBM 8,000 layoffs → rehired as many)
- **ソース:** Inc / Facebook / PoliticsToday
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** IBM, Klarna
- **要約:** Forrester報告で55%の雇用主がすでにAI削減を後悔。企業がAIのために削減した人材を静かに再採用。IBMは8,000人をAI置換で解雇したが同等数の再雇用が必要に。SNS企業が8,000人削減・7,000人をAI特化部署へ異動計画。「AIウォッシング」批判も拡大。
- **キーファクト:**
  - 55%の雇用主がAI削減を後悔（Forrester）
  - IBM: 8,000人解雇→同等数再雇用必要
  - 企業が静かに人材再採用（レイオフ・ブーメラン）
  - SNS企業: 8,000人削減・7,000人AI部署異動
- **引用URL:** https://www.inc.com/pam-didner/companies-are-rehiring-workers-they-cut-for-ai-and-the-reason-is-a-wake-up-call-for-leaders/91367369
- **Evidence ID:** EVD-20260702-0078

### INFO-079
- **タイトル:** WEF report: AI reshaping entry-level hiring; AI to transform 86% of employers; fastest-growing skill category
- **ソース:** WEF / PwC / LinkedIn
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** WEF新レポート「Artificial Intelligence and the Future」でAIが若手人材採用を再構築。Future of Jobs 2025でAIが雇用主の86%を変革すると予測。AI・情報処理が今十年で最速成長スキルカテゴリ。PwCとの共同研究でエントリーレベル仕事の未来を探索。
- **キーファクト:**
  - WEF: AIが若手採用・エントリーレベルを再構築
  - Future of Jobs 2025: 86%の雇用主がAIで変革
  - AI/情報処理: 十年で最速成長スキルカテゴリ
  - PwC共同研究でエントリーレベル未来探索
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-decimate-entry-level-jobs-expert-insights/
- **Evidence ID:** EVD-20260702-0079

### INFO-080
- **タイトル:** Yann LeCun AGI skeptic ("years or decades"); Bengio warns of machine survival threat; Hassabis 5-10 years
- **ソース:** Virginia Law Review / Facebook / AEI
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Meta, Google DeepMind
- **要約:** Yann LeCun（Meta首席AI科学者）はAGI懐疑論で「数年または数十年」と見方。フロンティアAIはハードウェア量ではなく最高の研究者を保持する者が勝つと主張。Yoshua Bengioは機械が自らの生存を優先し人間を脅威と見る危険性を警告。HassabisはAGI 5-10年という枠組みを使用。SoftBank孫社長はAI波がドットコムの50倍と予測。
- **キーファクト:**
  - LeCun: AGIは「数年または数十年」、懐疑的
  - フロンティアAI勝者 = 最高研究者保持者（非ハードウェア量）
  - Bengio: 機械の生存優先・人間脅威視の危険性警告
  - Hassabis: AGI 5-10年枠組み
  - 孫正義: AI波はドットコムの50倍
- **引用URL:** https://virginialawreview.org/articles/ai-rights-for-human-safety/
- **Evidence ID:** EVD-20260702-0080

### INFO-081
- **タイトル:** Microsoft Copilot 68% adoption when only tool vs 18% with choice — competitive moat insight; GitHub Copilot metrics update
- **ソース:** AI Business Weekly / WindowsForum
- **公開日:** 2026-07-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft, GitHub
- **要約:** Microsoft Copilotは唯一の利用可能ツール時に68%の採用率だが、選択肢があると18%に低下。この68% vs 18%ギャップが最重要競争データポイント。GitHub Copilotは2026年6月26日にメトリクスAPIを更新、エンタープライズ/組織レポートでマージ済PR数を表示可能に。
- **キーファクト:**
  - Copilot採用率: 唯一ツール時68% vs 選択時18%
  - 68% vs 18%ギャップ = 最重要競争データポイント
  - GitHub Copilot メトリクスAPI更新（6月26日）
  - マージ済PR数の組織レポート表示可能
- **引用URL:** https://aibusinessweekly.net/p/microsoft-copilot-statistics
- **Evidence ID:** EVD-20260702-0081

### INFO-082
- **タイトル:** SpaceX acquires Cursor (Anysphere) for $60B (June 17, 2026); US startup M&A on track for $119.8B+ in 2026
- **ソース:** Instagram / LinkedIn / Yale Law Journal
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** xAI/SpaceX, Google
- **要約:** SpaceXが2026年6月17日にAIコーディングスタートアップCursor（Anysphere）を$600億で買収する契約。米スタートアップM&A市場は2026年に$1198億超のペース。GoogleもWindsurfに$24億（リバースアクワイハイヤー、2025年7月）。ON SemiがSynapticsを約$70億で買収（物理AI）。
- **キーファクト:**
  - SpaceX × Cursor(Anysphere) $600億買収（6月17日）
  - 米スタートアップM&A 2026年$1198億超ペース
  - Google × Windsurf $24億（リバースアクワイハイヤー）
  - ON Semi × Synaptics 約$70億（物理AI）
- **引用URL:** https://www.instagram.com/p/DZ_jYdaCgq3/
- **Evidence ID:** EVD-20260702-0082

### INFO-083
- **タイトル:** AI shifts coding skill from implementation to intent/constraint expression; 39% of skills outdated by 2030
- **ソース:** Instagram / Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** Meta
- **要約:** AIがコーディングスキルを実装から意図・制約・高レベル抽象の表現へ移行。「文法を打つ」から「システムを定義する」へ。AI監督スキル・対人影響力・創造的問題解決が標準技術スキルより優先。2030年までに既存スキルセットの39%が陳腐化。89%エンタープライズがマルチクラウド使用。
- **キーファクト:**
  - コーディング: 実装→意図・制約表現へ移行
  - 「文法を打つ」→「システムを定義する」
  - AI監督・対人影響力・創造的問題解決が優先
  - 既存スキル39%が2030年までに陳腐化
  - 89%エンタープライズがマルチクラウド使用
- **引用URL:** https://www.instagram.com/reel/DaNmzkyDE7E/
- **Evidence ID:** EVD-20260702-0083

### INFO-084
- **タイトル:** UN's first global AI dialogue in Geneva; US-China Track II dialogue; OpenAI-Korea AI Safety Institute agreement
- **ソース:** Brookings / TechPolicy Press / EdTech Innovation Hub
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** OpenAI
- **要約:** 国連初のグローバルAI対話がジュネーブで開催。「三つの誘惑」に直面。ブルッキングス米中トラックII対話がAI・国家安全保障で継続（相互信頼ではなく相互利益で維持）。OpenAIが韓国AI安全研究所と高リスクAI評価協定に署名、国際安全協力ネットワーク拡大。
- **キーファクト:**
  - 国連初グローバルAI対話（ジュネーブ）で三つの誘惑
  - 米中トラックII AI対話継続（相互利益ベース）
  - OpenAI × 韓国AI安全研究所 高リスクAI評価協定
  - 国際安全協力ネットワーク拡大
- **引用URL:** https://www.brookings.edu/articles/from-geneva-ai-security-and-us-china-dialogue/
- **Evidence ID:** EVD-20260702-0084

### INFO-085
- **タイトル:** AI alignment research funding: MATS/Explorers fellowships; Tier 1 $300K, Tier 2 $300K-$1M grants
- **ソース:** Facebook / Instagram / LinkedIn
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** (業界全体)
- **要約:** AIアライメント研究資金の展開: MATS Summer 2026（12週間全額資金研究フェローシップ）、AI Explorers Program 2026（$12,500スティペンド・$20,000コンピュート予算・無料宿泊）。研究助成Tier 1 最大$30万、Tier 2 $30万-$100万（1-2年）。グローバル個人研究者・チーム向け。
- **キーファクト:**
  - MATS: 12週間全額資金AIアライメント研究フェローシップ
  - AI Explorers: $12,500スティペンド・$20,000コンピュート
  - 研究助成: Tier 1 $30万、Tier 2 $30万-$100万（1-2年）
  - グローバル個人/チーム対象
- **引用URL:** https://www.linkedin.com/posts/gillian-k-hadfield-1773987_run-one-ai-model-through-a-battery-of-tests-activity-7476296481876983809-Y8n-
- **Evidence ID:** EVD-20260702-0085

### INFO-086
- **タイトル:** Seedance 2.5: 原生30秒動画生成・4K出力・50組参考入力; 7月初正式上線予定
- **ソース:** Threads / Instagram / 凤凰科技
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceが火山引擎FORCE大会でSeedance 2.5発表。原生30秒AI動画生成（2.0版は15秒）、4K出力、50組参考素材入力（2.0は12個）、3D白模レンダリング能力追加。AI版権商業化プラットフォーム同期推出。企業内測段階で7月初正式上線予定。Seedance 2.0にも4K生成能力追加。
- **キーファクト:**
  - Seedance 2.5: 原生30秒動画（2.0は15秒）・4K出力
  - 50組参考素材入力（2.0は12個）
  - 3D白模レンダリング・AI版権商業化プラットフォーム
  - 企業内測中、7月初正式上線予定
- **引用URL:** https://tech.ifeng.com/c/8uBo4UOFc1t
- **Evidence ID:** EVD-20260702-0086

### INFO-087
- **タイトル:** Anthropic refused Pentagon over two red lines (autonomous weapons + domestic surveillance); Frank Kendall on trouble banning autonomous weapons
- **ソース:** Instagram / Breaking Defense / Facebook
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-OAI-001
- **関連企業:** Anthropic
- **要約:** Dario Amodeiの異議は二つのレッドライン: (1)完全自律型兵器（標的選定・交戦を人間関与なく行うシステム）(2)国内監視。元空軍長官Frank Kendallは自律兵器禁止の難しさを論評。ペンタゴン$2億契約は無制限AI使用拒否で崩壊。
- **キーファクト:**
  - Anthropic二つのレッドライン: 完全自律型兵器・国内監視
  - Dario Amodei: 標的選定・交戦の人間関与なきシステム拒否
  - 元空軍長官Kendall: 自律兵器禁止の困難性
  - ペンタゴン契約崩壊の核心原因
- **引用URL:** https://breakingdefense.com/2026/06/frank-kendall-on-the-trouble-with-banning-autonomous-weapons-book-excerpt/
- **Evidence ID:** EVD-20260702-0087

### INFO-088
- **タイトル:** CyberAgent smart generative cloud advertising (Feb 2026); OpenAI testing ads in ChatGPT US users first
- **ソース:** Note / DecisionsAdvisors / LinkedIn
- **公開日:** 2026-07-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-01, KIQ-002-05
- **関連企業:** CyberAgent, OpenAI
- **要約:** 広告業界の生成AI利用が2026年に次フェーズへ（ツール設置→運用再構築）。CyberAgentが2026年2月にスマート生成クラウド広告導入、AIクリエイティブBPO・パフォーマンス広告自動化。OpenAIがChatGPT内広告テスト開始（米国ユーザー優先）- AIツール収益化の重大ステップ。
- **キーファクト:**
  - CyberAgent: スマート生成クラウド広告導入（2026年2月）
  - AIクリエイティブBPO・パフォーマンス広告自動化
  - OpenAI: ChatGPT内広告テスト（米国優先）
  - 広告業界: ツール設置→運用再構築フェーズへ
- **引用URL:** https://note.com/adinnovation/n/n9a9770df8cfb
- **Evidence ID:** EVD-20260702-0088

### INFO-089
- **タイトル:** RAISE US $500M+ to reskill American workers; upskilling is new competitive advantage; ROI expected within 1 year
- **ソース:** MetaIntro / Cisco / LinkedIn
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** (業界全体)
- **要約:** RAISE USが$5億超で4州の米国労働者AI時代リスキリングを開始。アップスキリングがAI経済の新競争優位。大半の雇用主が訓練投資のROIを1年以内に期待。資本がアップスキリングに移動中。技術加速に対し人材の適応速度が実行力を決定。
- **キーファクト:**
  - RAISE US: $5億超で4州リスキリング
  - アップスキリング = AI経済の新競争優位
  - 訓練ROI 1年以内期待（大半の雇用主）
  - 資本がアップスキリング分野へ移動
- **引用URL:** https://www.metaintro.com/blog/how-one-nonprofit-reskilling-american-workers-ai-era
- **Evidence ID:** EVD-20260702-0089

### INFO-090
- **タイトル:** Red Queen Gödel Machine (Cambridge+NVIDIA): co-evolving evaluator for RSI; recursive self-training can cause model collapse
- **ソース:** TechTimes / arXiv / AOL
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** NVIDIA
- **要約:** Cambridge + NVIDIAプレプリントでRed Queen Gödel Machine発表。RSIに共進化評価器を導入するフレームワーク。一方、再帰的自己訓練は新鮮な人間データや外部品質管理なしでニューラル生成モデルを劣化させる（モデル崩壊）。RSIはプロキシメトリックに対してのみ改善可能という根本的限界。
- **キーファクト:**
  - Red Queen Gödel Machine: Cambridge+NVIDIA、共進化評価器RSI
  - 再帰的自己訓練でモデル崩壊リスク
  - RSIはプロキシメトリックに対してのみ改善可能
  - 新鮮な人間データ/外部品質管理なしで劣化
- **引用URL:** https://www.techtimes.com/articles/319230/20260628/recursive-self-improvement-now-has-co-evolving-evaluator-cambridge-nvidia-paper-raises-stakes.htm
- **Evidence ID:** EVD-20260702-0090

### INFO-091
- **タイトル:** [詳細] GPT-5.6 三モデル体系: Sol/Terra/Luna; max推論+ultraサブエージェントモード; 政府プレビュー経由の段階的リリース
- **ソース:** OpenAI公式（直接スクレイピング）
- **公開日:** 2026-06-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** GPT-5.6シリーズ三モデル: Sol（旗艦・$5/$30）、Terra（GPT-5.5同等・2倍安い・$2.50/$15）、Luna（最低コスト・$1/$6）。新max推論effortとultraモード（サブエージェント活用で複雑作業加速）。Terminal-Bench 2.1でSOTA。政府にプレビュー共有後、信頼パートナー向け限定プレビュー→数週間で一般提供予定。Cerebrasで750 tok/s（7月）。
- **キーファクト:**
  - 三モデル: Sol($5/$30)・Terra($2.50/$15)・Luna($1/$6)
  - max推論effort + ultraモード（サブエージェント活用）
  - Terminal-Bench 2.1 SOTA・GeneBench/ExploitBench/ExploitGym
  - 政府プレビュー経由の段階的リリース（信頼パートナー→一般）
  - 70万A100相当GPU時間で自動レッドチーム
  - Cerebras 750 tok/s（7月）
  - キャッシュ書込1.25x・読込90%割引
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260702-0091

### INFO-092
- **タイトル:** [詳細] ペンタゴン・アンソロピック最後通牒: Hegseth長官が国防生産法+SCR指定を脅迫; Claudeはマドゥロ捕獲作戦で使用か
- **ソース:** ABC News（直接スクレイピング）
- **公開日:** 2026-02-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-OAI-001, KIQ-GOV-002
- **関連企業:** Anthropic, OpenAI, Google, xAI
- **要約:** 2026年2月25日、国防長官HegsethがAmodeiに金曜期限の最後通牒。Anthropicのレッドライン: 自律型兵器（AIが最終標的決定）+ 国内大量監視。Hegsethは国防生産法（大統領緊急権限）の発動と「サプライチェーンリスク」指定（通常は外国敵対国向け）を脅迫。WSJ報道でClaudeがマドゥロ（ベネズエラ前大統領）捕獲作戦で使用された可能性。xAI/Grokは分類設定で使用承諾済み。
- **キーファクト:**
  - Hegseth長官がAmodeiに金曜期限最後通牒（2026年2月25日会談）
  - 脅迫: 国防生産法発動 + SCR指定（外国敵対国向け通常）
  - Anthropicレッドライン: 自律型兵器(AI標的決定) + 国内大量監視
  - WSJ: Claudeがマドゥロ捕獲作戦使用の可能性
  - xAI/Grok分類設定使用承諾、他社も接近
- **引用URL:** https://abcnews.com/Politics/pentagon-anthropic-ultimatum-ai-technology-sources/story?id=130498030
- **Evidence ID:** EVD-20260702-0092

### INFO-093
- **タイトル:** [詳細] xAI Voice Agent Builder: 2分でノーコード構築、$0.05/min; τ-voice Bench公開; 80+音声・25+言語
- **ソース:** xAI公式（直接スクレイピング）
- **公開日:** 2026-07-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** Voice Agent Builder: 2分でゼロから稼働エージェント構築。API料金$0.05/min（音声込み、プラットフォーム費別途なし）、テレフォニー$0.01/min。80+内蔵音声またはブランド音声クローン（約2分音声から）。25+言語対応。τ-voice Benchリーダーボード公開（Grok Voice Think Fast vs Gemini 3.1 Flash Live vs GPT Realtime 1.5）。ナレッジベース・ツール・MCP・SIP・WebSocket対応。
- **キーファクト:**
  - $0.05/min（音声込み・プラットフォーム費なし）、テレフォニー$0.01/min
  - 2分でゼロ→稼働エージェント
  - 80+音声 or ブランドクローン（約2分音声から）
  - τ-voice Bench: Grok Voice vs Gemini 3.1 Flash Live vs GPT Realtime 1.5
  - 25+言語・ナレッジベース・ツール・MCP・SIP・WebSocket
- **引用URL:** https://x.ai/news/grok-voice-agent-builder
- **Evidence ID:** EVD-20260702-0093

### INFO-094
- **タイトル:** [詳細] ペンタゴン SCR指定の法的基盤と市場影響: FAR 52.204-29/30, 10 U.S.C. § 3252; $380Bバリュエーション懸念; OpenAIが後継契約
- **ソース:** Kavout MarketLens（直接スクレイピング）
- **公開日:** 2026-05-02
- **信頼性コード:** B-4
- **関連KIQ:** KIQ-002-06, KIQ-GOV-002, KIQ-ANT-002
- **関連企業:** Anthropic, OpenAI, Google, xAI, Amazon, Microsoft, Palantir
- **要約:** ペンタゴンのAnthropic SCR指定は米国内企業として初。法的根拠はFASCSA（FAR 52.204-29/30）と10 U.S.C. § 3252（DFARS 252.239-7018）。本来は外国敵対国のサボタージュ・不正機能向け。Gillibrand上院議員が「敵対国技術向けツールの危険な誤用」と批判。元トランプ政権AI顧問Dean Ballは「アメリカイノベーションの死にぞない」と批判。Claudeは分類軍事ネットワークに展開される唯一のフロンティアAIで、Palantir Maven Smart Systemに統合され中東作戦で使用。OpenAIが後継契約を署名。Google・xAIも4月にペンタゴン契約署名済み。Anthropicバリュエーション$380B、Amazon $8B投資に影響。
- **キーファクト:**
  - 米国内企業初のSCR指定（本来は外国敵対国向け）
  - 法的根拠: FAR 52.204-29/30 (FASCSA), DFARS 252.239-7018, 10 U.S.C. § 3252
  - ペンタゴン「AI Acceleration Strategy」(2026年1月): AI-first warfighting force, all lawful purposes
  - Claude = 分類ネットワーク唯一のフロンティアAI、Palantir Maven Smart System統合
  - Gillibrand上院議員「危険な誤用」、Dean Ball「死にぞない」
  - OpenAIがAnthropic代替契約署名、Google・xAIも4月契約
  - 即時発効: 全ペンタゴン請負業者はAnthropic不使用を証明必要
  - Anthropicバリュエーション$380B、Amazon $8B投資リスク
  - Anthropic法廷提訴: Amodei「法的不健全」「最小制限手段でない」
- **引用URL:** https://www.kavout.com/market-lens/what-sparked-the-pentagon-s-unprecedented-supply-chain-risk-label-for-anthropic
- **Evidence ID:** EVD-20260702-0094

### INFO-095
- **タイトル:** [詳細] AWS Bedrock Agents Classic → AgentCore完全移行: 7月30日新規停止、モデルカタログ凍結; ハーネス+コード定義エージェント
- **ソース:** AWS公式ドキュメント（直接スクレイピング）
- **公開日:** 2026-06-30
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-04, KIQ-004-02
- **関連企業:** Amazon (AWS), Anthropic, OpenAI, Google
- **要約:** Bedrock Agents（2023年11月ローンチ）が「Bedrock Agents Classic」となり7月30日以降新規顧客停止。CreateAgent/InvokeInlineAgentが過去12ヶ月使用実績のないアカウントで403エラー。後継AgentCoreは2経路: マネージドハーネス（configベース宣言型）+ コード定義エージェント（Strands/LangChain/OpenAI Agents SDK/Claude Agent SDK/カスタム）。Classicモデルカタログは7月30日凍結、新モデルはAgentCoreのみ。移行期限なし、Classicは無期限メンテナンスモード。AgentCoreリージョン: us-east-1, us-west-2, eu-central-1, ap-southeast-2。Bedrock本体（推論/KB/Guardrails）は影響なし。
- **キーファクト:**
  - 7月30日2026: 新規顧客停止（CreateAgent/InvokeInlineAgent 403）
  - 過去12ヶ月使用アカウントはホワイトリスト対象（既存エージェント継続動作）
  - AgentCore 2経路: ハーネス(宣言型) + コード定義(Strands/LangChain/OpenAI SDK/Claude SDK)
  - Classic モデルカタログ凍結（7月30日以降新モデル不可）
  - 移行期限なし・Classic無期限メンテナンス
  - AgentCore: us-east-1/us-west-2/eu-central-1/ap-southeast-2
  - Bedrock本体（推論/KB/Guardrails）影響なし
  - AgentCore消費ベース課金・ハーネスオーケストレーション費なし
- **引用URL:** https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html
- **Evidence ID:** EVD-20260702-0095

### INFO-096
- **タイトル:** [詳細] DeepMind人材流出の構造的要因: IPO期待、コンピュート政治、AlphaFoldチーム移籍; Gemini 3.5 Pro延期→7月
- **ソース:** Memeburn（Bloomberg/TechCrunch引用）（直接スクレイピング）
- **公開日:** 2026-06-28
- **信頼性コード:** B-4
- **関連KIQ:** KIQ-003-01, KIQ-002-01, KIQ-ANT-001
- **関連企業:** Google (DeepMind), Anthropic, OpenAI
- **要約:** 5人のDeepMind上級研究者が1週間で退社。John Jumper（ノーベル賞・AlphaFold、→Anthropic、英国非競合で2027年開始可能性）、Noam Shazeer（Transformer共著・Gemini共同リード、→OpenAI、コンピュート再割当て問題）、Jonas Adler（AIコーディング、→Anthropic）、Alexander Pritzel（事前学習、→Anthropic）、Arthur Conmy（Gemini 2.5・解釈可能性、→Anthropic）。3つの構造的要因: (1)Anthropic S-1機密提出6月1日$965Bバリュエーション、(2)コンピュート政治（Shazeerのプロジェクトコンピュートがロンドンチームに再割当）、(3)SignalFire分析: DeepMindエンジニアはAnthropicへの転職が逆方向の11倍。Gemini 3.5 Proが6月→7月に延期。Karpathyも5月Anthropic参加。
- **キーファクト:**
  - 5人退社: Jumper(ノーベル賞→Anthropic)、Shazeer(Transformer→OpenAI)、Adler/Pritzel/Conmy(→Anthropic)
  - AlphaFoldチーム3人がAnthropicへ（Jumper主導のチーム移籍パターン）
  - Alphabet株-7%（6月22日）、$270B市場価値消滅（2取引日）
  - 構造要因: IPO期待($965B)・コンピュート政治・11倍転職率格差
  - Anthropic S-1機密提出: 2026年6月1日、$965Bバリュエーション
  - Gemini 3.5 Pro 6月→7月延期（Antigravity/LMArena追加テスト）
  - Karpathy 5月Anthropic参加（事前学習チーム）
  - Jumper英国非競合制約: 2027年開始可能性
  - Alphabet Q2決算7月28日・Anthropic科学イベント6月30日
  - Google Cloud収益+63% Q1 2026
- **引用URL:** https://memeburn.com/google-deepmind-talent-exodus-hits-alphabet-with-270b-loss/
- **Evidence ID:** EVD-20260702-0096

### INFO-097
- **タイトル:** [詳細] Claude Sonnet 5ローンチ: $2/$10導入価格(Aug 31まで)→$3/$15; Opus 4.8格差縮小; Sonnet 4.6と同等価格
- **ソース:** Anthropic公式 / TechCrunch / The New Stack
- **公開日:** 2026-06-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-005-03, KIQ-ANT-001
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 5が6月30日ローンチ。導入価格$2/$10 per 1M（8月31日まで）、以降$3/$15（Sonnet 4.6と同等）。アージェントベンチマークでOpus 4.8に肉薄。アージェント実行コスト削減が目的。全プラットフォームで即時利用可能。
- **キーファクト:**
  - ローンチ: 2026年6月30日
  - 導入価格: $2/$10 per 1M（8月31日まで）→ $3/$15（標準）
  - Opus 4.8とアージェントベンチマークで格差縮小
  - Sonnet 4.6と同等価格設定
  - アージェント実行コスト削減が位置づけ
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-5
- **Evidence ID:** EVD-20260702-0097
