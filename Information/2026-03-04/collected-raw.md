# 収集データ: 2026-03-04

## メタデータ
- 収集日時: 2026-03-04 08:30 UTC
- 実行クエリ数: 52 / 56
- scrape実行数: 11件
- 収集情報数: 73件
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-004-02 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 動的追加クエリ: KIQ-RED-005 ✓, KIQ-CODE-QUALITY ✓, KIQ-JUNIOR-CAUSE ✓, KIQ-BYTEDANCE-ENGAGEMENT ✓, KIQ-OPENAI-ALLOCATION ✓, KIQ-ANTHROPIC-MARKET ✓, KIQ-CHINA-LOGIC ✓
- 品質フラグ: NORMAL
- 企業カバレッジ: OpenAI (12件), Anthropic (15件), Google (8件), xAI (3件), ByteDance (5件), Microsoft (6件), Amazon (4件), その他 (20件)
- 重要発見:
  - OpenAI-Amazon戦略的パートナーシップ ($110B調達、Bedrock統合)
  - OpenAI-国防総省契約 (Anthropic契約解除後)
  - Trump政権のAnthropic連邦機関使用停止命令
  - Doubao DAU 1億人突破、MAU 3.15億人 (全球2位)
  - AI生成コードの50%がセキュリティテスト失敗
  - プログラミング職求人70%減少
  - Fortune 500の80%がAIエージェント展開
  - エージェントAIで有意義なROIはわずか10%

## 収集結果

### INFO-001
- **タイトル:** Thoughts on America's AI Action Plan
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-07-23
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicが米国政府のAI行動計画に対する見解を発表。インフラ加速・連邦政府採用・安全性テスト強化を支持。H20チップの中国への輸出規制維持を強く推奨。AI開発の透明性基準の必要性を提言。
- **キーファクト:**
  - データセンター・エネルギー許認可の簡素化を支持
  - 連邦政府のAI採用促進（OMBによる障壁除去、調達基準更新）
  - H20チップの中国輸出規制維持を強く推奨（メモリ帯域幅の独自性を理由）
  - AI開発透明性基準（安全性テスト・能力評価の公開報告）の必要性
- **引用URL:** https://www.anthropic.com/news/thoughts-on-america-s-ai-action-plan

### INFO-002
- **タイトル:** Claude Code and new admin controls for business plans
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-08-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがEnterprise/Team向けにClaude Codeを統合したプレミアムシートを発表。管理者向けのCompliance API、支出管理、使用量分析を提供。Behavox社で「他のエージェントより優秀」、Altana社で「開発速度2-10倍向上」の結果。
- **キーファクト:**
  - プレミアムシートでClaude + Claude Codeを統合
  - Compliance APIでリアルタイム監視・監査機能を提供
  - Behavox: 「他のエージェントより一貫して優秀な結果」
  - Altana: 「開発速度2-10倍向上」
  - 粒度の細かい支出管理・使用量分析を提供
- **引用URL:** https://www.anthropic.com/news/claude-code-on-team-and-enterprise

### INFO-003
- **タイトル:** Anthropic and Infosys collaborate to build AI agents for telecommunications
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-002-02
- **関連企業:** Anthropic, Infosys
- **要約:** AnthropicとInfosysが提携し、通信・金融・製造・ソフトウェア開発向けにエージェントAIを構築。Claude Agent SDKとInfosys Topazを統合。インドはClaude.aiの第2位市場で、使用の約半分がアプリ構築・システム近代化。
- **キーファクト:**
  - 通信: ネットワーク運用近代化・顧客ライフサイクル管理
  - 金融: リスク検出・コンプライアンス自動化・パーソナライズドアドバイス
  - 製造: 製品設計・シミュレーション加速
  - インドはClaude.ai第2位市場、使用の約半分がアプリ構築関連
  - ClaudeはBedrock/Vertex AI/Azureの3大クラウドで唯一利用可能なフロンティアモデル
- **引用URL:** https://www.anthropic.com/news/anthropic-infosys

### INFO-004
- **タイトル:** Claude's extended thinking
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-02-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02, KIQ-005-01
- **関連企業:** Anthropic
- **要約:** Claude 3.7 Sonnetで「拡張思考モード」を導入。思考プロセスを可視化し、シリアル・パラレル両方のテスト時計算スケーリングを実現。GPQAで84.8%（物理96.5%）を達成。ポケモン赤で3つのジムバッジを獲得。
- **キーファクト:**
  - 拡張思考モード: より多くの認知努力を費やすことを可能に
  - 思考プロセスの可視化: 信頼性・アライメント研究・興味の観点から有益
  - OSWorld評価で行動スケーリング（マルチステップタスク）を改善
  - GPQA 84.8%（物理96.5%）をパラレルテスト時計算で達成
  - ポケモン赤で3つのジムリーダーを倒し、バッジを獲得
  - ASL-2基準を維持、CBRN関連で一部アップリフト観察
  - プロンプトインジェクション防御率74%→88%に向上
- **引用URL:** https://www.anthropic.com/news/visible-extended-thinking

### INFO-005
- **タイトル:** Introducing Anthropic's AI for Science Program
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** AnthropicがAI for Scienceプログラムを開始。高インパクト科学プロジェクトに無料APIクレジットを提供。特に生物学・ライフサイエンス分野に注力。複雑な生物システムの理解、遺伝データ分析、創薬加速を支援。
- **キーファクト:**
  - 科学研究加速のため無料APIクレジット提供
  - 特に生物学・ライフサイエンス分野に注力
  - 複雑な生物システム理解・遺伝データ分析・創薬加速を支援
  - Dario Amodeiの「Machines of Loving Grace」ビジョンに沿う
- **引用URL:** https://www.anthropic.com/news/ai-for-science-program

### INFO-006
- **タイトル:** Grok-1.5 Vision Preview
- **ソース:** xAI (公式ブログ)
- **公開日:** 2024-04-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** xAI
- **要約:** xAIが初のマルチモーダルモデルGrok-1.5Vを発表。RealWorldQAベンチマークで68.7%を達成し競合を上回る。文書、図表、チャート、スクリーンショット、写真を処理可能。RealWorldQAデータセット（700+画像）を公開。
- **キーファクト:**
  - 初のマルチモーダルモデル: 文書・図表・チャート・写真を処理
  - RealWorldQA 68.7%（GPT-4V 61.4%、Gemini Pro 1.5 67.5%を上回る）
  - Mathvista 52.8%（最高）、TextVQA 78.1%（最高）
  - RealWorldQAデータセット（700+画像）をCC BY-ND 4.0で公開
  - 物理世界の空間理解能力に注力
- **引用URL:** https://x.ai/news/grok-1.5v

---

## KIQ-001-01: Agent SDK/API機能拡張ロードマップ

### INFO-007
- **タイトル:** OpenAI Multi-agents Documentation
- **ソース:** OpenAI Developer Docs
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがマルチエージェント機能を公式ドキュメント化。並列実行の専門サブエージェント、探索・テスト・ログ分析ユースケース、生の仲介出力ではなく要約を返すパターンを文書化。
- **キーファクト:**
  - マルチエージェントの並列実行を公式サポート
  - 探索・テスト・ログ分析のユースケース
  - サブエージェントから要約を返すパターン推奨
- **引用URL:** https://developers.openai.com/codex/concepts/multi-agents/

### INFO-008
- **タイトル:** Claude Agent SDK - npm
- **ソース:** npm (Anthropic公式)
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Code SDKがClaude Agent SDKに改名。移行ガイドで破壊的変更を文書化。TypeScript版がリリースされ、GitHubで活発に更新中。
- **キーファクト:**
  - Claude Code SDK → Claude Agent SDKに改名
  - 移行ガイドで破壊的変更を文書化
  - TypeScript版がGitHubで活発に更新
  - Claude Code 2.1.63で26のCLI変更と6つのフラグ変更
- **引用URL:** https://www.npmjs.com/package/@anthropic-ai/claude-agent-sdk

### INFO-009
- **タイトル:** Google Gemini API Coding Agents
- **ソース:** Google AI for Developers
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google
- **要約:** GoogleがGemini APIでコーディングエージェント向け開発スキルを提供。最新Gemini APIドキュメントへの直接アクセス、統合パターンを提供。Gemini Live APIで低遅延リアルタイム音声・動画対話を実現。
- **キーファクト:**
  - コーディングエージェント向け開発スキル
  - 最新Gemini APIドキュメントへの直接アクセス
  - Gemini Live APIでリアルタイム音声・動画対話
  - Firebase AI Logic SDKsでもGemini API利用可能
- **引用URL:** https://ai.google.dev/gemini-api/docs/coding-agents

### INFO-010
- **タイトル:** xAI Grok API and Tools
- **ソース:** 複数ソース
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI
- **要約:** xAIがGrok Imagine API（テキスト・画像・動画生成）、Grok Search API（リアルタイムWeb/X検索）を展開。Grok 4.20 beta1がSearchベンチマークで#1獲得。Grok Code CLI開発中。
- **キーファクト:**
  - Grok Imagine API: テキスト→動画、画像→動画、動画→動画
  - Grok Search API: リアルタイムWeb/X検索、引用付き
  - Grok 4.20 beta1がSearchベンチマークで#1獲得
  - Grok Code CLI開発中
  - Intelligence Index 41.4で優秀なコーディング能力
- **引用URL:** https://termo.ai/skills/grok

### INFO-011
- **タイトル:** ByteDance Doubao 2.0 - Emotional Resonance
- **ソース:** LinkedIn/Instagram
- **公開日:** 2026-03
- **信頼性コード:** C-4
- **関連KIQ:** KIQ-001-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがDoubao 2.0を正式リリース。「エージェント時代」向けに設計。「感情的共鳴（Emotional Resonance）」を初めてマスターしたエージェントと評価。Cozeプラットフォームでアジア太平洋市場で強い地域支配力。
- **キーファクト:**
  - Doubao 2.0: 「エージェント時代」向けに設計
  - 「感情的共鳴」を初めてマスターしたエージェント
  - 米国エージェントの「Helpful, Harmless, Honest」とは異なるアプローチ
  - Cozeプラットフォームがアジア太平洋で地域支配
  - Seedance 2.0もアップデート（有料のみ）
- **引用URL:** https://www.linkedin.com/posts/gary-kolegraff-b5219b26a_the-agentic-social-moat-bytedances-doubao-activity-7432431491550367744-1XvX

### INFO-012
- **タイトル:** Top 5 AI Agent Frameworks 2026
- **ソース:** Intuz
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** 複数
- **要約:** 2026年の主要AIエージェントフレームワーク: LangGraph, AutoGen, CrewAI, OpenAgents, MetaGPT。Vercel AI SDK + Next.js、OpenClaw、OpenAI/Claudeの組み合わせも人気。
- **キーファクト:**
  - 主要フレームワーク: LangGraph, AutoGen, CrewAI, OpenAgents, MetaGPT
  - OpenClaw: 「今すぐ動くエージェント」向け
  - Vercel AI SDK + Next.js: カスタム構築向け
  - AI SDK v6でAgent() API、構造化出力、ツールパターン強化
- **引用URL:** https://www.intuz.com/blog/top-5-ai-agent-frameworks-2025

### INFO-013
- **タイトル:** Enterprise AI Agent Architecture and SLA
- **ソース:** IT Tech Pulse
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** 複数
- **要約:** エンタープライズAIエージェントのアーキテクチャ、ユースケース、リスク、ロードマップ。SLA保証、インシデント対応プロトコル、マルチテナント分離、リアルタイムパフォーマンスメトリクスが重要。
- **キーファクト:**
  - エンタープライズ対応: ロギング、監査証跡、SLA保証
  - インシデント対応プロトコル必須
  - マルチテナント分離
  - リアルタイムパフォーマンスメトリクス
  - AIエージェントが金融決定を実行し始める「マシンカスタマー時代」
- **引用URL:** https://ittech-pulse.com/our-tech-insights/generative-ai-ai-agents-in-the-enterprise-architecture-use-cases-risks-and-the-road-ahead/

---

## KIQ-001-02: エンタープライズ展開（セキュリティ認証・SLA・専用サポート）

### INFO-014
- **タイトル:** Anthropic Trust Center Updates - SOC 2 Type II, HIPAA
- **ソース:** Anthropic Trust Center
- **公開日:** 2026-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Anthropicが更新されたコンプライアンス認証をTrust Centerで公開。SOC 2 Type II、HIPAAアテステーション、Claude for Nonprofits（70-75%割引）を提供。
- **キーファクト:**
  - SOC 2 Type IIレポート更新
  - HIPAAアテステーション取得
  - Claude for Nonprofits: 非営利団体に70-75%割引
  - 専任チームがエンタープライズ対応
- **引用URL:** https://trust.anthropic.com/updates

### INFO-015
- **タイトル:** Claude Code Security - Research Preview
- **ソース:** Fluid Attacks / CSO Online
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Code SecurityをEnterprise/Team向けにリリース。AI推論でコードベースの脆弱性をスキャン。業界全体の「目覚めの呼び声」と評価。しかし「ローグAIメモ」で50の研究プロジェクト、63%の企業がAIの誤動作を防げていないと警告。
- **キーファクト:**
  - Claude Code Security: AI推論でコードベース脆弱性スキャン
  - Enterprise/Team向け限定リサーチプレビュー
  - ローグAIエージェント・スキーミングモデルの研究50プロジェクト
  - 63%の企業がAIの誤動作を防止できていない
- **引用URL:** https://fluidattacks.com/es/blog/claude-code-security

### INFO-016
- **タイトル:** Google Vertex AI Agent Engine Enterprise Security
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Google
- **要約:** Google Vertex AI Agent Engineがエンタープライズセキュリティ機能を追加。プライベートVPC環境へのデプロイ、Private Service Connect設定、プロビジョニングスループットでSLA保証を提供。
- **キーファクト:**
  - プライベートVPC環境へのエージェントデプロイ
  - Private Service Connect設定
  - プロビジョニングスループットで高スループット保証
  - Vertex AIでSLA（サービスレベル契約）提供
  - コンシューマAPIにはSLAなし
- **引用URL:** https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes

### INFO-017
- **タイトル:** Deloitte AI Adoption ROI Success - CIBC Case
- **ソース:** Deloitte
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** 複数
- **要約:** Deloitte調査: CIBCとの統制行動パイロットで開発者の90%採用、10-14%生産性向上を達成。人中心の採用アプローチが成功の鍵。
- **キーファクト:**
  - CIBC: 開発者の90%採用率
  - 10-14%の生産性向上
  - AIを既存ワークフローに埋め込むアプローチが成功
  - 人中心の採用アプローチが重要
- **引用URL:** https://www.deloitte.com/ca/en/Industries/financial-services/perspectives/ai-adoption-roi-success.html

### INFO-018
- **タイトル:** TELUS $600M+ AI Benefits - 53,000 Copilots
- **ソース:** TELUS Digital
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** TELUS
- **要約:** TELUSが53,000のコパイロットを展開し、$600M+のAI利益を創出。責任あるAIを具体的なビジネス価値に転換。
- **キーファクト:**
  - 53,000コパイロット展開
  - $600M+のAI利益創出
  - 責任あるAIのビジネス価値転換
- **引用URL:** https://www.telusdigital.com/insights/data-and-ai/resource/democratizing-enterprise-ai

### INFO-019
- **タイトル:** 20 Companies AI Agents Study - Why Most Will Fail
- **ソース:** Medium
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** 複数
- **要約:** 20社のAIエージェント導入を調査。成功事例では、現場チームメンバーを「障害」ではなく「ドメインエキスパート」として扱った。プロセス知識がエージェント設計を形成し、現場の合意が成功を決定。
- **キーファクト:**
  - 現場チームをドメインエキスパートとして扱うことが成功の鍵
  - プロセス知識がエージェント設計を形成
  - 現場の合意が成功を決定
  - 多くの企業が失敗する原因: 現場を障害として扱う
- **引用URL:** https://medium.com/@tayyeb.datar/i-studied-20-companies-using-ai-agents-heres-why-most-will-fail-68c7413bce03

### INFO-020
- **タイトル:** AI Security Certification - CAISE, CRAGE
- **ソース:** 複数ソース
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** 複数
- **要約:** AIセキュリティ認証が急増。CAISE（Certified AI Security Expert）、CRAGE（Certified Responsible AI Governance & Ethics）など、NIST/ISO準拠の企業規模認証が登場。
- **キーファクト:**
  - CAISE: AIセキュリティ・LLM保護・レッドチーミング認証
  - CRAGE: 責任あるAI・ガバナンス・倫理認証（NIST/ISO準拠）
  - 企業向けAIコンプライアンストレーニング・認証ライセンス
  - AIセキュリティガバナンスフレームワーク需要増加
- **引用URL:** https://trioscyber.com/caise-certified-ai-security-expert-the-future-proof-skill-every-cyber-ai-professional-must-have/

---

## KIQ-001-03: 開発者エコシステム（サードパーティ連携・マーケットプレイス）

### INFO-021
- **タイトル:** OpenAI and Amazon Strategic Partnership
- **ソース:** OpenAI / Amazon (公式発表)
- **公開日:** 2026-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-03, KIQ-002-01, KIQ-003-04
- **関連企業:** OpenAI, Amazon
- **要約:** OpenAIとAmazonが戦略的パートナーシップを発表。OpenAI FrontierをAWSに展開、Amazon BedrockでStateful Runtime Environmentを提供。AWSがOpenAI Frontierの唯一のサードパーティクラウド配信プロバイダーに。
- **キーファクト:**
  - OpenAI FrontierをAWSに展開
  - Stateful Runtime EnvironmentをBedrockで提供
  - AWSがOpenAI Frontierの唯一のサードパーティクラウド配信プロバイダー
  - 組織がAIチームを構築・デプロイ・管理可能に
  - カスタムモデル・エンタープライズAIを拡張
- **引用URL:** https://openai.com/index/amazon-partnership/

### INFO-022
- **タイトル:** Google ADK Integrations Ecosystem
- **ソース:** Google Developers Blog
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Google
- **要約:** GoogleがADK（Agent Development Kit）統合エコシステムを発表。Hugging Face、GitHubと統合。Daytona、Sentry、GitLabなど開発ツールに直接接続し、コード管理・APIテスト・スクリプト実行を可能に。
- **キーファクト:**
  - Hugging Face、GitHubとの統合
  - Daytona: コード実行環境
  - Sentry: エラー監視
  - GitLab: コード管理
  - 開発ツールに直接接続するエコシステム
- **引用URL:** https://developers.googleblog.com/en/supercharge-your-ai-agents-adk-integrations-ecosystem/

### INFO-023
- **タイトル:** MCP (Model Context Protocol) Adoption
- **ソース:** 複数ソース
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic, Microsoft, 複数
- **要約:** MCP（Model Context Protocol）がAIエージェント接続の標準として急速に普及。Anthropicが作成し、Microsoft FoundryがMCPサーバーエンドポイント対応を追加。セキュリティリスクとベストプラクティスの議論も活発化。
- **キーファクト:**
  - MCP: Anthropicが作成したオープンプロトコル
  - AIアプリと外部データソースの接続を標準化
  - 「AIアプリケーションのUSB-C」と呼ばれる
  - Microsoft FoundryがMCPサーバー対応
  - セキュリティリスク（MCPサーバー露出）への懸念
- **引用URL:** https://www.outreach.io/resources/blog/what-is-model-context-protocol-mcp

### INFO-024
- **タイトル:** Agentic AI Foundation (AAIF) Growth - UiPath, Huawei, Apollo
- **ソース:** 複数ソース
- **公開日:** 2026-02
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** UiPath, Huawei, Apollo GraphQL
- **要約:** AAIF（Agentic AI Foundation）にUiPath、Huawei、Apollo GraphQLが参加。2025年設立のオープン財団で、エージェントAIの透明性・相互運用性を推進。Huaweiの参加は「ルールが書かれる前に標準を形成する」計算された動き。
- **キーファクト:**
  - AAIF: 2025年設立、エージェントAIの相互運用性を推進
  - UiPath: RPAとエージェントAIの統合を推進
  - Huawei: アジア太平洋での標準形成を狙う計算された動き
  - Apollo GraphQL: Agent-to-API統合のオープン標準を推進
  - 「エージェント単独では価値が限られる」
- **引用URL:** https://www.zawya.com/en/press-release/companies-news/uipath-joins-agentic-ai-foundation-to-advance-interoperability-in-agentic-ai-adoption-v2h33mnq

### INFO-025
- **タイトル:** Agent Skills Marketplace - 500+ Skills
- **ソース:** GitHub / Medium
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Microsoft, OpenAI, 複数
- **要約:** Agent Skillsが主要プラットフォームで標準化。Microsoft、OpenAI、Atlassian、Figma、Cursor、GitHubが対応。GitHub Copilotがネイティブサポート。500以上のスキルがコミュニティから公開。
- **キーファクト:**
  - 主要プラットフォーム対応: Microsoft, OpenAI, Atlassian, Figma, Cursor, GitHub
  - GitHub Copilotがネイティブサポート追加
  - 500以上のエージェントスキルがコミュニティから公開
  - Claude Code Skills、Codex、Antigravity、Gemini CLI、Cursorと互換
  - Figmaスキル: デザイン→本番UIコード変換
- **引用URL:** https://github.com/VoltAgent/awesome-agent-skills

### INFO-026
- **タイトル:** Intuit-Anthropic Partnership - QuickBooks AI Agents
- **ソース:** LinkedIn
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** Intuit, Anthropic
- **要約:** IntuitがAnthropicと複数年パートナーシップを発表。中堅企業がQuickBooksとIntuit内でカスタムAIエージェントを構築可能に。
- **キーファクト:**
  - 複数年パートナーシップ
  - 中堅企業がQuickBooks内でカスタムAIエージェント構築
  - Intuit製品内でのエージェント構築を可能に
- **引用URL:** https://www.linkedin.com/posts/blaketoliver_intuit-just-announced-a-multi-year-partnership-activity-7434617414354583553-TMIw

### INFO-027
- **タイトル:** 2026: Year of the Agent OS Paradigm
- **ソース:** SitePoint / Medium
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** 複数
- **要約:** 2026年が「エージェントOSの年」と呼ばれる。オープンソースの個人AIエージェントエコシステムが急成長。AIエージェントと「バイブコーディング」が2025年にソフトウェア開発を根本的に変えたと評価。
- **キーファクト:**
  - 2026年は「エージェントOSの年」
  - オープンソース個人AIエージェントエコシステムが急成長
  - 2025年: AIが「実際の作業」を始めた年として記憶される
  - 新しいOSパラダイムとしてのAIエージェント
- **引用URL:** https://www.sitepoint.com/the-rise-of-open-source-personal-ai-agents-a-new-os-paradigm/

---

## KIQ-001-04: マルチモーダルAgent（音声・視覚・コード実行）

### INFO-028
- **タイトル:** OpenAI Realtime API - gpt-realtime
- **ソース:** OpenAI Developer Docs
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAIがgpt-realtime（最も高機能な音声対音声モデル）をAPIでリリース。Realtime APIが一般提供開始。ChatGPTアプリで長期・バックグラウンドタスク、クリーンなdiff、エージェント進捗表示が可能に。
- **キーファクト:**
  - gpt-realtime: 最も高機能な音声対音声モデル
  - Realtime APIが一般提供開始
  - 長期・バックグラウンドタスク実行
  - クリーンなdiff、エージェント進捗表示
  - 再利用可能なワークフロー実行
- **引用URL:** https://developers.openai.com/cookbook/examples/realtime_prompting_guide/

### INFO-029
- **タイトル:** Google Gemini 3.1 Flash-Lite - Multimodal Agentic
- **ソース:** Google AI for Developers / VentureBeat
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google
- **要約:** GoogleがGemini 3.1 Flash-Liteをプレビュー。高ボリューム・エージェントタスク向け、低レイテンシ・低コスト。Gemini Live APIでリアルタイム音声・動画対話。Androidでライドシェア・フードデリバリーを自動化。Arena.ai Elo 1432。
- **キーファクト:**
  - 高ボリューム・エージェントタスク向け、低レイテンシ
  - Gemini Live API: リアルタイム音声・動画対話
  - Androidでライドシェア・フードデリバリー自動化
  - Proの1/8のコスト
  - Arena.ai Elo 1432（競合より大幅に小さいパラメータ数）
- **引用URL:** https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview

### INFO-030
- **タイトル:** Microsoft Foundry Browser Automation Agent
- **ソース:** Microsoft Azure Documentation
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Microsoft
- **要約:** Microsoft Foundryがブラウザ自動化エージェントツールを追加。BrowserAutomationAgentToolでAIエージェントがブラウザタスクを自動化。Amazon Nova Actもブラウザ自動化で注目。
- **キーファクト:**
  - BrowserAutomationAgentToolでブラウザタスク自動化
  - 同期・非同期実行をサポート
  - Amazon Nova Actもブラウザ自動化で競合
  - オープンソースのPlaywrightベースのローカルAIエージェントも登場
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/browser-automation

### INFO-031
- **タイトル:** Computer Use - New AI Paradigm
- **ソース:** Deck / Stack AI
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** 複数
- **要約:** Computer Useが新しいAIパラダイムとして定着。エージェントが画面を見て、マウスを動かし、ボタンをクリックし、タイピングすることでソフトウェアと対話。Browser UseでWebを人間のようにナビゲート。
- **キーファクト:**
  - Computer Use: 画面を見て・マウスを動かし・クリックし・タイピング
  - APIやコネクタではなく、ページを見て理解
  - Browser Use: AIエージェントがWebを人間のようにナビゲート
  - JS-heavyサイト・認証フローも処理
- **引用URL:** https://www.stack-ai.com/blog/the-era-of-ai-employees-how-ai-agents-navigate-the-web-like-human-employees-with-browser-use

### INFO-032
- **タイトル:** Multimodal AI Leaderboard - Vision AI
- **ソース:** Arena.ai / AwesomeAgents
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** 複数
- **要約:** マルチモーダルAIベンチマークでClaudeが「決定的に勝っている」と評価。Vision AI Leaderboardで677,404票。MMMU-Pro、Video-MMMUなどでランキング。ベンチマークだけでは「AI競争の勝者」はわからないという議論。
- **キーファクト:**
  - Claudeがマルチモーダルで「決定的に勝っている」
  - Vision AI Leaderboard: 677,404票
  - MMMU-Pro、Video-MMMUでランキング
  - ベンチマークだけでは勝者を判断できない
  - OpenAIペンタゴン契約が「実際に重要」な理由として議論
- **引用URL:** https://arena.ai/leaderboard/vision

### INFO-033
- **タイトル:** Multimodal AI for Programmers - Code from Screenshots/Voice
- **ソース:** Medium / Dev.to
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** 複数
- **要約:** マルチモーダルAIがプログラマーに実用的に。スクリーンショット・音声・スケッチからコード生成。ビジョンエージェントは「ピクセルを見るだけでなく、意図・コンテキスト・意味を解釈」。オープンソースAI音声エージェントも登場。
- **キーファクト:**
  - スクリーンショット・音声・スケッチからコード生成
  - ビジョンエージェント: 意図・コンテキスト・意味を解釈
  - AVA: Asterisk/FreePBX向けオープンソースAI音声エージェント
  - モジュラーパイプラインアーキテクチャ（STT, LLM混在可能）
  - オンデバイスでLLM・画像生成・音声転写・ビジョンAI実行
- **引用URL:** https://medium.com/@putridamayanti/multimodal-ai-for-programmers-code-from-screenshots-voice-and-sketches-1b41f855728e

---

## KIQ-001-05: スキル配布と実行環境・ロックイン

### INFO-034
- **タイトル:** Claude Code Sandbox Security - Remote Control Risks
- **ソース:** Penligent / Medium
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Codeのサンドボックスにセキュリティリスク。サンドボックスはデフォルトでオフ（-sandbox/--no-sandboxフラグ）。ローカルセッションがHTTPS接続でリモートインターフェースになる可能性。CIパイプライン向けに権限チェックをバイパスするフラグも存在。
- **キーファクト:**
  - サンドボックスはデフォルトでオフ
  - ローカルセッションがリモートインターフェースになるリスク
  - CIパイプライン向けに権限チェックバイパスフラグ
  - Coworking Pythonスクリプトがサンドボックスでブロックされる問題
- **引用URL:** https://www.penligent.ai/hackinglabs/claude-code-remote-control-security-risks-when-your-local-session-becomes-a-remote-interface/

### INFO-035
- **タイトル:** OpenAI Codex Shell Tool and Skills
- **ソース:** OpenAI Developer Docs / DataCamp
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI Codexがシェルツールとupdate_planツールを推奨。100以上のエージェントスキルがOpenClaw、Claude Code、OpenAI Codex、Cursor CLIで利用可能。サンドボックス実行環境でネットワークアクセスなし、ランタイムパッケージインストールなし。
- **キーファクト:**
  - シェルツールとupdate_planツールを推奨
  - 100以上のエージェントスキルが利用可能
  - サンドボックス実行: ネットワークアクセスなし
  - ランタイムパッケージインストールなし
  - サードパーティスキルをサードパーティコードとして扱う
- **引用URL:** https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide/

### INFO-036
- **タイトル:** Google Gemini CLI - skill-creator and Extensions
- **ソース:** Google Cloud / Medium
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Google
- **要約:** Gemini CLIがskill-creator（メタスキル）を内蔵。自然言語プロンプト、スクリプティング、自動化をサポート。gemini-extension.jsonで拡張機能を定義。Hugging Faceのスキルリポジトリと互換。
- **キーファクト:**
  - skill-creator: メタスキルでスキルを簡単に作成
  - 自然言語プロンプト、スクリプティング、自動化
  - gemini-extension.jsonで拡張機能定義
  - Hugging Faceスキルリポジトリと互換
  - コード説明、デバッグ、コンテンツ生成を自動化
- **引用URL:** https://medium.com/google-cloud/building-agent-skills-with-skill-creator-855f18e785cf

### INFO-037
- **タイトル:** Agent Skills Marketplace - Economic Growth
- **ソース:** Medium / LobeHub
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** 複数
- **要約:** Agent Skillsの経済指標が爆発的成長を示す。スキルマーケットプレイス（LobeHub等）でClaude Code、Codex CLI、ChatGPT対応スキルを販売。Agent Skillsはワークフロー・能力、MCPはセキュアなデータ・ツール接続に注力。
- **キーファクト:**
  - AIエージェント市場が爆発的成長
  - スキルマーケットプレイスでスキルを販売可能
  - Agent Skills: ワークフロー・能力
  - MCP: セキュアなデータ・ツール接続
  - 100以上のスキルを比較・評価
- **引用URL:** https://jinlow.medium.com/agent-skills-the-hidden-architecture-powering-ais-next-evolution-9ada610d4ef2

### INFO-038
- **タイトル:** 2026 AI Cost Crisis - API Aggregation Platforms
- **ソース:** Press Release / a16z
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** 複数
- **要約:** 2026年のAIコスト危機でAPI集約プラットフォームが注目。統合コストを最大80%削減、ベンダーロックインへの耐性を強化。a16z: AIがアプリケーションソフトウェアを「食べる」中、エージェントがマイグレーションを支援しスイッチングコストを変更。
- **キーファクト:**
  - API集約プラットフォームで統合コスト最大80%削減
  - ベンダーロックインへの耐性強化
  - トークン単位価格でコストが変動
  - エージェントがマイグレーションを支援しスイッチングコストを変更
  - 広告業界がAdCPで相互運用性を向上させる動き
- **引用URL:** https://www.columbiatribune.com/press-release/story/60617/the-2026-ai-cost-crisis-the-rise-of-one-api-aggregation-platforms-and-their-potential-to-deliver-80-savings/

### INFO-039
- **タイトル:** AI Vendor Lock-in Warning Signs
- **ソース:** Gradient Flow
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** 複数
- **要約:** AIベンダーが「檻」になる警告サイン。トークン単位価格でコストが変動、プロンプト変更・コンテキスト拡大・リトライループで請求が急増。チームが予期せぬコスト急増を経験。
- **キーファクト:**
  - トークン単位価格でコストが変動
  - プロンプト変更・コンテキスト拡大・リトライで請求急増
  - 予期せぬコスト急増の事例
  - ベンダーが「檻」になる警告サインを認識
- **引用URL:** https://gradientflow.substack.com/p/we-watched-this-happen-with-the-internet

---

## KIQ-002-01: クラウドプロバイダー（AWS, Azure, GCP）のAI Agent統合

### INFO-040
- **タイトル:** OpenAI Stateful Runtime Environment in Amazon Bedrock
- **ソース:** OpenAI / Amazon (公式発表)
- **公開日:** 2026-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-01, KIQ-001-03
- **関連企業:** OpenAI, Amazon
- **要約:** OpenAIとAmazonがBedrockでStateful Runtime Environmentを共同開発。永続オーケストレーション、メモリ、セキュア実行をマルチステップAIワークフローに提供。KiroでAmazon Connect AIエージェント開発を加速。
- **キーファクト:**
  - Stateful Runtime: 永続オーケストレーション・メモリ・セキュア実行
  - BedrockでOpenAIモデルを利用可能
  - Kiro: 15のLambda関数、DynamoDB、Bedrock統合を自動生成
  - Bedrock AgentCoreでインテリジェントイベントエージェント構築
- **引用URL:** https://openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/

### INFO-041
- **タイトル:** Microsoft Foundry Agent Service
- **ソース:** Microsoft Documentation
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Foundryがエージェントサービスを提供。Bing、SharePoint、Azure AI Searchでエンタープライズ知識にアクセス。AIゲートウェイでAzure API Managementや非Azureホストモデルを接続。統合Azure PaaSでエンタープライズAI運用を実現。
- **キーファクト:**
  - Bing、SharePoint、Azure AI Searchでエンタープライズ知識アクセス
  - AIゲートウェイでAzure API Managementや非Azureモデル接続
  - 統合Azure PaaSでエンタープライズAI運用
  - Foundry IQでエージェント分析
  - ブラウザ自動化ツールを追加
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/overview

### INFO-042
- **タイトル:** Google Vertex AI Agent Builder
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Google
- **要約:** Google Vertex AI Agent Builderがエンタープライズグレードのマルチエージェント体験を構築・オーケストレーション。ADK（Agent Development Kit）でMemory Bankを管理し、長期記憶を実現。「ゼロオペレーション」エンジニアリングアプローチ。
- **キーファクト:**
  - エンタープライズグレードのマルチエージェント体験
  - ADKでMemory Bankを管理、長期記憶を実現
  - 「ゼロオペレーション」エンジニアリングアプローチ
  - 生産対応ジェネレーティブAIエージェントを構築・デプロイ
- **引用URL:** https://docs.cloud.google.com/agent-builder

### INFO-043
- **タイトル:** Cloud Provider AI Comparison 2026
- **ソース:** Intuz / Blue Prism
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** AWS, Azure, GCP
- **要約:** 2026年のクラウドプロバイダーAI比較。AWS vs Azure vs GCPでジェネレーティブAIの選択肢を評価。エンタープライズAIエージェントソリューションを7つのプラットフォームで比較（チャネルカバレッジ、コンプライアンス、統合深度）。
- **キーファクト:**
  - AWS、Azure、GCPのジェネレーティブAI比較
  - チャネルカバレッジ、コンプライアンス、統合深度で評価
  - 7つのエンタープライズAIエージェントプラットフォームを比較
  - n8n、Make、Pythonなどエージェントビルダーツール
- **引用URL:** https://medium.com/intuz/aws-vs-other-cloud-providers-for-generative-ai-which-one-to-choose-ed9c13bceb23

---

## KIQ-002-02: エンタープライズ顧客のAI Agent採用率と主要ユースケース

### INFO-044
- **タイトル:** Deloitte State of AI in Enterprise 2026
- **ソース:** Deloitte Global
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** エンタープライズAI採用が急成長。2025年に従業員のAIアクセスが50%増加。≥40%のプロジェクトが本番運用の企業数が増加。しかし、エージェントAIで「有意義なROI」を実現しているのはわずか10%。93%のAI予算が技術に割かれ、人材・プロセスが軽視。
- **キーファクト:**
  - 2025年: 従業員のAIアクセスが50%増加
  - ≥40%プロジェクトが本番運用の企業が増加
  - エージェントAIで「有意義なROI」はわずか10%
  - 93%のAI予算が技術に割かれ、人材・プロセスが軽視
- **引用URL:** https://www.deloitte.com/cy/en/issues/generative-ai/state-of-ai-in-enterprise.html

### INFO-045
- **タイトル:** McKinsey: 70-80% of Large Enterprises Adopt Agentic AI
- **ソース:** McKinsey
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** McKinsey調査: 大企業の70-80%がエージェントAIを積極的に導入。地域間で差はあるものの、勢いは非常に強い。ITSMでは84%がAIに「肯定的」、13%が「否定的」。
- **キーファクト:**
  - 大企業の70-80%がエージェントAIを積極導入
  - 地域間で差はあるが勢いは非常に強い
  - ITSM: 84%がAIに肯定的、13%が否定的
- **引用URL:** https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/winning-b2b-customers-in-technology-and-telecommunications

### INFO-046
- **タイトル:** 80% of Fortune 500 Deploy AI Agents - Microsoft
- **ソース:** Adoptify / Microsoft
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** Microsoft報告: Fortune 500のほぼ80%がAIエージェントを運用・開発・顧客ワークフローに展開。エージェントAIで5-10%の収益増、サポート業務で最大30%のコスト削減。Fortune 250で15倍のスピード向上。85%がSEC提出書類でAIに言及。
- **キーファクト:**
  - Fortune 500の80%がAIエージェントを展開
  - 5-10%の収益増、サポートで最大30%コスト削減
  - Fortune 250で15倍のスピード向上
  - 85%がSEC提出書類でAIに言及
  - 金融サービス11%、製造13%、小売9%がアクティブエージェント
- **引用URL:** https://www.adoptify.ai/news/agentic-visibility-gap-emerges-as-80-of-fortune-500-deploy-agents/

### INFO-047
- **タイトル:** Enterprise AI Agent Use Cases - Financial Services Lead
- **ソース:** Agility at Scale
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** 金融機関がエンタープライズAIエージェント採用をリード。不正検知が旗艦ユースケース。Goldman、Salesforce、OpenAIの教訓。AgentOpsが新しい規律として登場。
- **キーファクト:**
  - 金融機関がエンタープライズAIエージェント採用をリード
  - 不正検知が旗艦ユースケース
  - 高取引量と明確なROIメトリクスが推進要因
  - AgentOps: ガバナンス・観測可能性・ツール制御・人間監視
- **引用URL:** https://agility-at-scale.com/ai/ai-agents/enterprise-ai-agent-use-cases/

---

## KIQ-002-03: 規制環境（EU AI Act、米国大統領令、中国AI規制）

### INFO-048
- **タイトル:** EU AI Act Enforcement - Most Enterprise AI Non-Compliant
- **ソース:** LinkedIn / Seekr
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** EU AI Actの執行条項が2026年8月に発効。高リスクAIシステムの非準拠で最大€3,500万（約$3,850万）の罰金。ほとんどのエンタープライズAIが非準拠。AI意思決定のガバナンス実証が必須。
- **キーファクト:**
  - 2026年8月: 透明性条項が発効
  - 高リスクAI非準拠で最大€3,500万の罰金
  - ほとんどのエンタープライズAIが非準拠
  - AI意思決定のガバナンス実証が必須
  - 文書化されたAIガバナンスプログラムでセキュリティレビューが加速
- **引用URL:** https://www.seekr.com/resource/explainable-ai-enterprise-guide/

### INFO-049
- **タイトル:** Trump Targets State AI Regulations - Federal Preemption
- **ソース:** The Reg Review / GSA
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** Anthropic
- **要約:** トランプ大統領が州レベルAI規制を標的に。2025年12月の大統領令で連邦政策と矛盾する州AI規制を阻止。GSAが「Anthropic技術の即時使用停止」を支持。連邦権限の集中化と州レベル規制のパッチワーク防止を強調。
- **キーファクト:**
  - 2025年12月大統領令: 州AI規制を阻止
  - 連邦政策と矛盾する州規制を阻止
  - GSA: Anthropic技術の即時使用停止を支持
  - 連邦権限の集中化を強調
  - Executive Order 14179で新連邦フレームワーク確立
- **引用URL:** https://www.theregreview.org/2026/02/26/champagne-president-trump-targets-state-based-ai-regulations/

### INFO-050
- **タイトル:** China AI Regulation - Emotional Safety Measures
- **ソース:** Carnegie / Mashable
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance, 中国企業
- **要約:** 中国がAIコンパニオンを規制。2025年9月1日に規制と国家標準が同時発効。AIの「感情的影響」を世界で初めて規制する方向へ。2025年サイバー安全法改正が2026年1月1日発効、「最も厳格な改正」に。
- **キーファクト:**
  - 2025年9月1日: AI規制と国家標準が同時発効
  - AIの「感情的影響」を世界で初めて規制
  - 2025年サイバー安全法改正: 2026年1月1日発効
  - 「最も厳格な改正」と評価
  - NPC年次議会で5カ年技術戦略を発表予定
- **引用URL:** https://carnegieendowment.org/russia-eurasia/research/2026/02/china-is-worried-about-ai-companions-heres-what-its-doing-about-them

---

## KIQ-002-06: 政府・軍のAI企業への経済的圧力

### INFO-051
- **タイトル:** OpenAI Department of War Contract - Safety Red Lines
- **ソース:** OpenAI (公式発表)
- **公開日:** 2026-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIが国防総省と契約。安全レッドライン、法的保護、機密環境でのAI展開を概説。Anthropicの既存契約が解除された直後に締結。「Anthropicのどの契約よりも多くのガードレール」と主張。
- **キーファクト:**
  - OpenAI-国防総省契約を発表
  - 安全レッドライン、法的保護、機密環境でのAI展開
  - Anthropicの既存契約解除直後に締結
  - 「Anthropicのどの契約よりも多くのガードレール」
  - ChatGPTユーザー9億人以上
- **引用URL:** https://openai.com/index/our-agreement-with-the-department-of-war/

### INFO-052
- **タイトル:** Trump Orders All Agencies to Stop Using Anthropic
- **ソース:** CBC / Guardian
- **公開日:** 2026-03-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06, H-GOV-001
- **関連企業:** Anthropic, OpenAI
- **要約:** トランプ政権が全連邦機関にAnthropic技術の使用停止を命令。国防総省とヘグセス長官がAnthropicに「国防生産法に基づくモデルの完全利用」を脅迫。Altmanは契約が「日和見的で雑に見える」と認め修正。
- **キーファクト:**
  - 全連邦機関にAnthropic技術使用停止を命令
  - 国防総省が国防生産法に基づく完全利用を脅迫
  - Altman: 契約が「日和見的で雑に見える」と認め修正
  - 米国人大規模監視の防止を明記
  - 政府当局が何カ月もAnthropicを批判
- **引用URL:** https://www.cbc.ca/news/business/trump-anthropic-feud-ai-9.7109006

### INFO-053
- **タイトル:** OpenAI Caved to Pentagon on AI Surveillance - The Verge
- **ソース:** The Verge
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, H-GOV-001
- **関連企業:** OpenAI, Anthropic
- **要約:** 国防総省とAnthropicの劇的な対立の中、OpenAIがペンタゴンと新契約。なぜ国防総省がAnthropicではなくOpenAIを受け入れたかは不明。政府当局は何カ月もAnthropicを批判していた。
- **キーファクト:**
  - 国防総省-Anthropic対立の中でOpenAIが契約獲得
  - なぜAnthropicではなくOpenAIかは不明
  - 政府当局が何カ月もAnthropicを批判
  - OpenAIがペンタゴンのAI監視に譲歩
- **引用URL:** https://www.theverge.com/ai-artificial-intelligence/887309/openai-anthropic-dod-military-pentagon-contract-sam-altman-hegseth

---

## KIQ-002-04: AIエージェントによる業務自律化の進展

### INFO-054
- **タイトル:** AI Quietly Replacing Entry-Level Jobs - 50M at Risk
- **ソース:** Medium / USA Today
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, H-CAR-002
- **関連企業:** 複数
- **要約:** AIが静かにエントリーレベルの仕事を置き換え。カスタマーサービスの80%がAI自動化のリスク。全米で約5,000万のエントリーレベル職がリスク。World Economic Forum: AIは創出と同数の職を破壊、ホワイトカラー・エントリーレベルが特に脆弱。
- **キーファクト:**
  - カスタマーサービスの80%がAI自動化リスク
  - 全米で約5,000万のエントリーレベル職がリスク
  - WEF: AIは創出と同数の職を破壊
  - ホワイトカラー・エントリーレベルが特に脆弱
  - データ入力、レポート生成、CS、ジュニアコーディングを自動化
- **引用URL:** https://medium.com/activated-thinker/how-ai-is-quietly-replacing-entry-level-jobs-and-what-that-means-for-your-future-808090bfc51c

### INFO-055
- **タイトル:** Klarna, Block, Duolingo AI Headcount Reduction
- **ソース:** Built In / Reddit
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, H-CAR-001
- **関連企業:** Klarna, Block, Duolingo
- **要約:** KlarnaがAI動機の採用凍結で40%の人員削減、2030年までにさらに33%削減を計画。BlockがAI刷新で40%人員削減、Dorsey CEOは「他社も追随する」と予測。DuolingoがAI-first人員戦略を採用。
- **キーファクト:**
  - Klarna: 40%削減済み、2030年までにさらに33%削減計画
  - Block: 40%人員削減、Dorsey CEOが他社追随を予測
  - Duolingo: AI-first人員戦略採用
  - Amazon: 企業職を大量削減しながらAIインフラ投資を加速
  - Klarnaは「静かに再採用を開始」したとの報告
- **引用URL:** https://builtin.com/articles/ai-washing-layoffs

### INFO-056
- **タイトル:** 3 AI Agents Run Full Ad Workflow in Minutes
- **ソース:** Reddit / Google Business
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04
- **関連企業:** 複数
- **要約:** 3つのAIエージェントが広告ワークフローを最初から最後まで数分で実行。Googleが「アジェンティックマーケティング」を推奨: CMOがプロンプトツールからAIエージェント管理へ戦略的移行。
- **キーファクト:**
  - 3つのAIエージェントが広告ワークフロー全体を数分で実行
  - Google: アジェンティックマーケティングを推奨
  - CMOがプロンプトツールからAIエージェント管理へ移行
  - 従来の自動化と異なり、タスクを推論しツールを選択
- **引用URL:** https://business.google.com/us/think/ai-excellence/agentic-marketing-ai-strategy/

---

## KIQ-003-01: API料金改定の頻度・方向性

### INFO-057
- **タイトル:** AI Inference Costs Fell 78% in 2025
- **ソース:** X / News.aakashg
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** 複数
- **要約:** 2025年に一部プロバイダーで推論コストが78%低下。曲線は平坦化していない。OpenAIのBatch APIが非リアルタイムワークロードで50%割引。OpenAIの2025年トークン価格引上げで価格変動リスクが顕在化。
- **キーファクト:**
  - 2025年: 推論コストが78%低下
  - 曲線はまだ平坦化していない
  - OpenAI Batch API: 非リアルタイムで50%割引
  - OpenAI 2025年トークン価格引上げで価格変動リスク顕在化
  - 単一プロバイダー依存で価格急増・障害リスク
- **引用URL:** https://x.com/aakashgupta/status/2028267039828131910

### INFO-058
- **タイトル:** Claude Opus 4.6 API Pricing - $5/$25 per Million Tokens
- **ソース:** PricePerToken
- **公開日:** 2026-02-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claude Opus 4.6が2026年2月4日リリース。入力100万トークン$5、出力100万トークン$25。Claude Opus 3は2026年1月5日に引退（最初の完全引退プロセス）。一部開発者はAPIで1日$100-$200/開発者を支出。
- **キーファクト:**
  - Claude Opus 4.6: 入力$5/M、出力$25/M
  - 2026年2月4日リリース
  - Claude Opus 3は2026年1月5日に引退
  - 一部開発者は1日$100-$200/開発者を支出
  - Claude Pro $17/月、Max $100/月
- **引用URL:** https://pricepertoken.com/pricing-page/model/anthropic-claude-opus-4.6

---

## KIQ-003-02: 主要ベンチマークの性能推移

### INFO-059
- **タイトル:** Gemini 3.1 Pro Tops Intelligence Index - ARC-AGI 77.1%
- **ソース:** DeepLearning.AI / DreamWellTimes
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** Google
- **要約:** Gemini 3.1 ProがIntelligence Indexでトップ。ARC-AGI-2で77.1%達成（$0.96/タスク）、前世代の31.1%から倍増。NVIDIA NVARCがARC-AGI-2公開リーダーボードで27.64%（40億パラメータモデル）。MMLUは知識の幅、GPQAは深さを測定。
- **キーファクト:**
  - Gemini 3.1 Pro: ARC-AGI-2で77.1%（前世代31.1%から倍増）
  - $0.96/タスクで達成
  - NVIDIA NVARC: 40億パラメータで27.64%
  - MMLU: 知識の幅、GPQA: 博士レベルの深さ
  - 単一スコアでは全体像はわからない
- **引用URL:** https://www.deeplearning.ai/the-batch/google-releases-gemini-3-1-pro-in-preview-tops-intelligence-index-at-same-price/

---

## KIQ-003-04: 資金調達・投資動向

### INFO-060
- **タイトル:** OpenAI $110B Funding Round - Amazon $50B, NVIDIA $30B, SoftBank $30B
- **ソース:** CNBC / OpenAI (公式発表)
- **公開日:** 2026-02-27
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-04, H-OAI-001
- **関連企業:** OpenAI, Amazon, NVIDIA, SoftBank
- **要約:** OpenAIが$110Bの資金調達を発表。評価額$730B（プレマネー）。Amazon $50B、NVIDIA $30B、SoftBank $30Bが出資。2月の世界VC投資$189Bの記録、この3社で83%を占める。Waymoも$16B調達。
- **キーファクト:**
  - $110B調達、評価額$730B
  - Amazon $50B、NVIDIA $30B、SoftBank $30B
  - 2月世界VC投資$189Bの83%をこの3社が占める
  - Waymo $16B調達
  - 「Scaling AI for everyone」ビジョン
- **引用URL:** https://openai.com/index/scaling-ai-for-everyone/

---

## KIQ-005-01: AGI到達度を示すベンチマーク指標

### INFO-061
- **タイトル:** AGI Insider Predictions - 2047 for 50% Chance
- **ソース:** Medium / AIMultiple
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** 複数
- **要約:** 2023年AI Impacts専門家調査（2,778人）: 2047年に50%の確率で「高レベル機械知能」。コミュニティ予測では2030年代。起業家はより早い予測。Google DeepMindが内部モデル「Aletheia」で数学オリンピアドから現実の科学的ブレークスルーへ飛躍。
- **キーファクト:**
  - 2023年専門家調査: 2047年に50%の確率
  - コミュニティ予測: 2030年代
  - 起業家はより早い予測
  - 9,800のAGI予測を分析
  - DeepMind内部モデル「Aletheia」が科学的ブレークスルー達成
- **引用URL:** https://medium.com/@timventura/agi-insider-predictions-for-the-arrival-of-human-level-artificial-intelligence-40c1084dbcb3

### INFO-062
- **タイトル:** Superintelligence is Already Here - Noah Smith
- **ソース:** Noahpinion
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** Google DeepMind
- **要約:** Noah Smithが「スーパーインテリジェンスはすでにここにある」と主張。Google DeepMindのGemini Deep Thinkが数学オリンピアドレベルから現実の科学的ブレークスルーへ飛躍。内部モデル「Aletheia」で達成。
- **キーファクト:**
  - スーパーインテリジェンスはすでに存在すると主張
  - Gemini Deep Think: 数学オリンピアドから科学的ブレークスルーへ
  - 内部モデル「Aletheia」で達成
  - AGIまで12-18カ月という議論も
- **引用URL:** https://www.noahpinion.blog/p/superintelligence-is-already-here

---

## 動的KIQ: Arbiter優先指定の追加収集

### INFO-063 (KIQ-RED-005)
- **タイトル:** AI ROI Definition and Calculation Framework
- **ソース:** 複数ソース
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-RED-005 (動的), H-CAR-001
- **関連企業:** 複数
- **要約:** AI ROI測定の体系的フレームワーク。労働置換または「人間の入力」削減を含む直接的計算。ベンダーベンチマークではなく自社データから計算が必要。投資対効果は24カ月段階的ロールアウトで計算。
- **キーファクト:**
  - ROI: 労働置換・人間入力削減の直接計算
  - ベンダーベンチマークではなく自社データで計算
  - 24カ月段階的ロールアウトで予測
  - 空席コスト回避・純影響で計算
  - AI品質監視からのROI計算手法
- **引用URL:** https://www.ninetwothree.co/blog/how-to-calculate-the-roi-of-ai

### INFO-064 (KIQ-CODE-QUALITY)
- **タイトル:** AI-Generated Code Security - 50% Fails Basic Tests
- **ソース:** Leo de Moura / Black Duck / Endor Labs
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-CODE-QUALITY (動的), H-CAR-002
- **関連企業:** 複数
- **要約:** AI生成コードの約半数が基本セキュリティテストに失敗。より大きなモデルも大幅に安全なコードを生成しない。2026 OSSRAレポート: オープンソース脆弱性が倍増（コードベース当たり581）。87%のコードベースがリスク。AI生成コードの10%のみがセキュア。
- **キーファクト:**
  - AI生成コードの約50%が基本セキュリティテストに失敗
  - より大きなモデルも安全なコードを生成しない
  - 2026 OSSRA: 脆弱性が倍増（581/コードベース）
  - 87%のコードベースがリスク、65%が攻撃被害
  - AI生成コードの10%のみがセキュア（Endor Labs）
  - 3つのAI生成アプリで70の悪用可能な脆弱性を確認
- **引用URL:** https://leodemoura.github.io/blog/2026/02/28/when-ai-writes-the-worlds-software.html

### INFO-065 (KIQ-JUNIOR-CAUSE)
- **タイトル:** Programming Job Postings Fell 70% - AI Transition Crisis
- **ソース:** Great Leadership / LinkedIn
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-JUNIOR-CAUSE (動的), H-CAR-002
- **関連企業:** 複数
- **要約:** プログラミング職の求人が約70%減少。雇用減少は求人パイプラインが枯渇するにつれてさらに進む。組織はAIで拡張された経験豊富な開発者に依存し、ジュニア開発者職を削減。2025-2026年にAIアシスタントを採用した企業はジュニア採用を減少。
- **キーファクト:**
  - プログラミング職求人が約70%減少
  - 求人パイプライン枯渇でさらに減少進行
  - 組織は経験豊富な開発者+AIに依存
  - ジュニア開発者職を削減
  - 2025-2026年AI採用企業はジュニア採用減少
- **引用URL:** https://greatleadership.substack.com/p/the-ai-transition-five-year-crisis

### INFO-066 (KIQ-BYTEDANCE-ENGAGEMENT)
- **タイトル:** Doubao DAU 100M - Engagement Resilience
- **ソース:** Meyka / SCMP / Moomoo
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-BYTEDANCE-ENGAGEMENT (動的), H-BTD-001
- **関連企業:** ByteDance
- **要約:** Doubaoが2月16日にDAU 1億人突破（2月初頭の4倍）。平均使用時間は2月16-22日の週に15%低下（10.2分→8.7分）。しかし「エンゲージメントレジリエンス」は比較的強い。春節キャンペーンで$10億を費やした赤包合戦。
- **キーファクト:**
  - DAU 1億人突破（2月16日、2月初頭の4倍）
  - 平均使用時間: 10.2分→8.7分（15%低下）
  - 「エンゲージメントレジリエンス」は比較的強い
  - 春節赤包合戦で$10億を費やした
  - 月間アクティブユーザー3.15億人（全球2位、ChatGPTの1/3）
- **引用URL:** https://meyka.com/blog/bytedances-ai-chatbot-doubao-hits-100-million-users-during-china-holiday-surge/

### INFO-067 (KIQ-OPENAI-ALLOCATION)
- **タイトル:** OpenAI $110B Funding Allocation - How AI Finances Itself
- **ソース:** Forbes / OpenAI
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-OPENAI-ALLOCATION (動的), H-OAI-001
- **関連企業:** OpenAI
- **要約:** OpenAIの$110B調達が「AIがいかに自らを資金調達するか」を示す。Amazon $50B、NVIDIA $30B、SoftBank $30B。評価額$730B（プレマネー）、$840B（ポストマネー）。歴史上最大のプライベート調達。用途の詳細は未公開。
- **キーファクト:**
  - $110B調達: Amazon $50B、NVIDIA $30B、SoftBank $30B
  - 評価額$730B（プレマネー）、$840B（ポストマネー）
  - 歴史上最大のプライベート調達
  - 「AIがいかに自らを資金調達するか」を示す
  - 用途の詳細は未公開
- **引用URL:** https://www.forbes.com/sites/renanaashkenazi/2026/03/02/openais-110-billion-reveals-how-ai-now-finances-itself/

### INFO-068 (KIQ-ANTHROPIC-MARKET)
- **タイトル:** Anthropic Revenue and Market Position
- **ソース:** LinkedIn / Facebook
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-ANTHROPIC-MARKET (動的), H-ANT-001
- **関連企業:** Anthropic
- **要約:** Anthropicの収益の推定15%が直接コンシューマー購読から。年初の$1B ARRから2025年中期に$4Bに成長。OpenAIは$10B。単一製品リリースでサイバーセキュリティ株から$20Bを抹消。連邦機関使用停止命令が大きな打撃。
- **キーファクト:**
  - 収益の推定15%がコンシューマー購読
  - 年初$1B ARR→2025年中期$4B
  - OpenAIは$10B ARR
  - 単一製品でサイバーセキュリティ株$20B抹消
  - 連邦機関使用停止命令が大きな打撃
- **引用URL:** https://www.linkedin.com/pulse/anthropic-could-win-consumer-market-john-battelle-al7he

### INFO-069 (KIQ-CHINA-LOGIC)
- **タイトル:** 豆包月活跃用户3.15亿 全球第二 - 中国市場動向
- **ソース:** 东方财富 / 凤凰网 / 新浪
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-CHINA-LOGIC (動的), BYTEDANCE-CHINESE, H-BTD-001
- **関連企業:** ByteDance, 阿里, 腾讯, 百度, DeepSeek
- **要約:** 豆包が月間アクティブユーザー3.15億人で全球2位、ChatGPTの約1/3。2025年8月からDeepSeekを超えて1位を維持。春節红包大戦で字节が先行、阿里Qwen 3.5、蚂蚁Ming-flash-omni-2.0を発表。百度はWeb中心（63.2%）、阿里と騰訊はIn-App AI。
- **キーファクト:**
  - 豆包MAU 3.15億人、全球2位、ChatGPTの1/3
  - 2025年8月からDeepSeek超えで1位維持
  - 環比増速87.38%
  - 字节M153豆包AI手机（中興合作、3499元）
  - 百度: Web中心63.2%、阿里/騰訊: In-App AI
  - 春節红包大戦で字节が先行
- **引用URL:** https://i.ifeng.com/c/8rCFCSlZ4Y6

---

## KIQ-003-03: オープンソースモデルと商用モデルの性能ギャップ

### INFO-070
- **タイトル:** Llama 4 Maverick vs Grok 4.1 Benchmark Comparison
- **ソース:** DocsBot AI / Oracle
- **公開日:** 2026-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, xAI
- **要約:** Llama 4 MaverickとGrok 4.1のベンチマーク比較。Llama-13BがGPT-3 (175B)の大部分のベンチマークで上回る。Llama-65BはChinchilla-70B、PaLM-540Bと競合。Meta Llama 3.3 (70B)がOracle Cloudで利用可能。
- **キーファクト:**
  - Llama-13B: GPT-3 (175B)の大部分のベンチマークで上回る
  - Llama-65B: Chinchilla-70B、PaLM-540Bと競合
  - Llama 4 Maverick: Grok 4.1と比較
  - Meta Llama 3.3 (70B)がOracle Cloudで利用可能
- **引用URL:** https://docsbot.ai/models/compare/grok-4-1/llama-4-maverick

---

## KIQ-004-02: コーディング能力の市場価値変化

### INFO-071
- **タイトル:** GitHub Copilot 26M Users - Cursor $2B ARR
- **ソース:** Pragmatic Engineer / Tech in Asia / DevOps.com
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02, H-CAR-002
- **関連企業:** Microsoft, Cursor, OpenAI
- **要約:** GitHub Copilotが2,600万ユーザー突破。Fortune 100の90%が採用、130万有料購読者、5万以上のエンタープライズ組織。OpenAI Codexが週間150万アクティブユーザー。Cursorが$2B ARR達成。開発者の55%の生産性向上を報告。5%のGitHubコミットがAI作成、41%がAI支援。
- **キーファクト:**
  - GitHub Copilot: 2,600万ユーザー、Fortune 100の90%採用
  - 130万有料購読者、5万以上のエンタープライズ組織
  - OpenAI Codex: 週間150万アクティブユーザー
  - Cursor: $2B ARR達成
  - 開発者の55%が生産性向上を報告
  - 5%のGitHubコミットがAI作成、41%がAI支援
- **引用URL:** https://newsletter.pragmaticengineer.com/p/ai-tooling-2026

---

## KIQ-005-02: 主要CEO/研究者のAGIタイムライン予測

### INFO-072
- **タイトル:** AGI Timeline Predictions - Amodei, Altman, Hassabis
- **ソース:** Mule AI / Facebook / Times of India
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Anthropic, OpenAI, Google DeepMind
- **要約:** Dario Amodei (Anthropic): 「パワフルAI」を2026年末までに予測、AGIという用語を避ける。Sam Altman: AGIを5年以内に達成、「驚くほど少ない影響で通り過ぎる」と主張。Demis Hassabis: 真のAGIはまだ5-10年先、2030年までの確率を50%と予測。
- **キーファクト:**
  - Dario Amodei: 2026年末までに「パワフルAI」
  - Sam Altman: 5年以内にAGI、「驚くほど少ない影響」
  - Demis Hassabis: 真のAGIは5-10年先
  - Hassabis: 2030年まで50%の確率
  - Satya Nadella: Hassabisと次のAIブレークスルーで合意
- **引用URL:** https://muleai.io/blog/2026-02-25-agi-2026-perspective/

---

## KIQ-005-03: AGI安全性とガバナンスの政策議論

### INFO-073
- **タイトル:** AI Safety Moratorium Debate - Innovation Barrier
- **ソース:** AI CERTs / POLITICO / TechPolicy.Press
- **公開日:** 2026-03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** スタートアップリーダーが新しい安全性提案を「イノベーション障壁」と呼ぶ。AI「レッドライン」をめぐる権力闘争。年齢保証の科学的コンセンサスが定まるまで展開計画の一時停止を求める声。Microsoftは「新興AI規制に準拠する準備ができている」と報告。
- **キーファクト:**
  - スタートアップ: 安全性提案を「イノベーション障壁」と呼ぶ
  - AI「レッドライン」をめぐる権力闘争
  - 科学的コンセンサスまで展開一時停止を求める声
  - Microsoft: 新興AI規制準拠準備完了と報告
  - 州レベルでデータセンター一時停止の動き
- **引用URL:** https://www.aicerts.ai/news/startup-safety-laws-the-innovation-barrier-debate/


## X (Twitter) 投稿データ（ローカルRSSHub経由）

### INFO-074
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-03-04
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Steven Adler
OpenAI wants you to just trust them that the NSA is excluded from their contract.

Katrina seems to believe she has been "very transparent," but there are many issues:

-Two days ago, you promised "a clear and more comprehensive explanation shortly" of how the NSA is excluded. https://x.com/natseckatrina/status/2028170853746159961?s=20
-Your explanation now is a single sentence, with no contract language showing the Title 50 exclusion you had claimed to exist. https://x.com/bradr...
- **引用URL:** https://x.com/EthanJPerez/status/2028919081492201950

### INFO-075
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-03-04
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Max Schwarzer
I've decided to leave OpenAI. I'm incredibly proud of all the work I've been part of here, from helping create the reasoning paradigm with @MillionInt, scaling up test-time compute with @polynoamial, working on RL algorithms with my fellow strawberries, shipping o1-preview (which started life as of one of my derisking runs), to post-training o1 and o3 with @ericmitchellai, @yanndubs and many others. I'm most proud of having led the post-training team here for the last year -- th...
- **引用URL:** https://x.com/EthanJPerez/status/2028945024550092906

### INFO-076
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-03-04
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Woo! Welcome!

Max Schwarzer: I've decided to leave OpenAI. I'm incredibly proud of all the work I've been part of here, from helping create the reasoning paradigm with @MillionInt, scaling up test-time compute with @polynoamial, working on RL algorithms with my fellow strawberries, shipping o1-preview (which
- **引用URL:** https://x.com/sleepinyourhat/status/2028965007502000434

### INFO-077
- **タイトル:** @sundarpichai (Sundar Pichai) のX投稿
- **ソース:** X (Twitter) - @sundarpichai (Google CEO)
- **公開日:** 2026-03-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Gemini 3.1 Flash-Lite is the fastest and most cost-efficient Gemini 3 series model⚡️

It outperforms 2.5 Flash with a 2.5X faster Time to First Answer Token and a 45% increase in output speed, at a fraction of the cost of larger models!

koray kavukcuoglu: Gemini 3.1 Flash-Lite is available now! It takes an unbelievable amount of complex engineering to make AI feel instantaneous, enabling exciting new frontiers for experimentation!
- **引用URL:** https://x.com/sundarpichai/status/2028891212573491715

### INFO-078
- **タイトル:** @joshwoodward (Josh Woodward) のX投稿
- **ソース:** X (Twitter) - @joshwoodward (Geminiアプリ / AI Studio)
- **公開日:** 2026-03-04
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Meet Flash-Lite: the really, really fast one

Logan Kilpatrick: Introducing Gemini 3.1 Flash-Lite 🔦, a huge step forward on the boundary of intelligence, beating 2.5 Flash on many tasks.
- **引用URL:** https://x.com/joshwoodward/status/2028900917786100102

### INFO-079
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-03-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Vaibhav (VB) Srivastav
ICYMI: You can use Voice transcription in both Codex App as well as the CLI! 🎙️

Press the mic button or hit `Ctrl + M` and talk away!

Available to 100% of the codex users :)
- **引用URL:** https://x.com/OpenAIDevs/status/2028862529431392534

### INFO-080
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-03-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** brb building a new app for @ChatGPTapp with this new Codex skill:

corey.ching: Shipped a new $chatgpt-apps skill — now available in the Codex app.

It’s purpose-built for building @ChatGPTapp apps with the Apps SDK: scaffold projects, wire tools to widget resources, and iterate toward polished, host-aware UI inside ChatGPT.

Especially useful for:
•
- **引用URL:** https://x.com/OpenAIDevs/status/2028962246618230808

