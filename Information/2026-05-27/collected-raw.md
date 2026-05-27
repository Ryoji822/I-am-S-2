# 収集データ: 2026-05-27

## メタデータ
- 収集日時: 2026-05-27 01:30 UTC
- 実行クエリ数: 56 / 56 (collection_plan全件) + 5件動的追加 = 計61件
- scrape実行数: 15件
- 収集情報数: 50件
- Evidence ID 採番範囲: EVD-20260527-0001 〜 EVD-20260527-0050
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE partial (中国語検索空), KIQ-AGENT-001 ✓ (動的), H-GOO-001 partial, H-XAI-002 ✓ (動的), SCN-001/SCN-003 ✓ (動的)
- 品質フラグ: NORMAL
- 動的追加クエリ:
  - KIQ-AGENT-001: Anthropic安全性エンタープライズ選択理由（collection_plan.json未登録、Arbiter指示）→ INFO-040 収集
  - H-GOO-001: Google Cloud AI収益固有寄与分解（4R条件対応）→ INFO-003/046 収集（Google I/Oから一部推測可能だがA-2+品質定量分解は未取得）
  - H-XAI-002: Grok Build CLI発売後データ（Arbiter指示）→ INFO-014 収集
  - SCN-001/SCN-003: 囲い込み形態分類枠組み（Arbiter指示）→ INFO-034/042/043/044 収集

## 収集結果

### INFO-001
- **タイトル:** OpenAI named a Leader in enterprise coding agents by Gartner
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-05-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGartner Magic Quadrant for Enterprise AI Coding AgentsでLeaderに認定。Codexは週400万人以上が利用し、Cisco、Datadog、Dell、NVIDIAが採用。GPT-5.5導入後、ツール使用・パフォーマンス・エンタープライズワークフロー対応が強化。
- **キーファクト:**
  - Codex週間利用者400万人以上
  - CiscoがAI Defense platformの大部分をCodexで開発、数四半期→数週間に短縮
  - エンタープライズ向け承認ゲート・RBAC・サンドボックス・監査機能を評価
  - HIPAA準拠対応、Amazon Bedrock上でも提供開始
- **引用URL:** https://openai.com/index/gartner-2026-agentic-coding-leader/
- **Evidence ID:** EVD-20260527-0001

### INFO-002
- **タイトル:** OpenAI and Dell Technologies partner to bring Codex to hybrid and on-premises enterprise environments
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-05-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-05, KIQ-002-01
- **関連企業:** OpenAI, Dell
- **要約:** OpenAIとDell Technologiesが提携、Codexをハイブリッド・オンプレミス環境に展開。Dell AI Data PlatformおよびDell AI Factoryとの統合で、エンタープライズデータの近くでエージェントを動作可能に。
- **キーファクト:**
  - CodexはOpenAIで最速成長のエンタープライズ製品
  - Codexがコーディングを超えてビジネスワークフロー（レポート作成、リード選別等）に拡張
  - Dell AI Factory経由でChatGPT Enterprise、APIソリューションも統合予定
- **引用URL:** https://openai.com/index/dell-codex-enterprise-partnership/
- **Evidence ID:** EVD-20260527-0002

### INFO-003
- **タイトル:** I/O 2026: Welcome to the agentic Gemini era
- **ソース:** Google Blog (公式, Sundar Pichai CEO)
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-003-01
- **関連企業:** Google
- **要約:** Google I/O 2026基調講演。Gemini 3.5 Flash、Gemini Omni、Antigravity 2.0、Gemini Spark（24/7個人エージェント）を発表。月間3.2 Quadrillionトークン処理（前年比7倍）。Geminiアプリ月間アクティブユーザー9億人突破。
- **キーファクト:**
  - 月間3.2 Quadrillion tokens処理（前年480Tから7倍増）
  - 850万デベロッパーが月間でGoogleモデルでビルド
  - 375以上のCloud顧客が各1Trillion tokens以上処理
  - Gemini 3.5 Flash: 他のフロンティアモデルの4倍速い、ほぼ全ベンチマークで3.1 Proを上回る
  - Gemini Spark: 24/7エージェント、Google Cloud VM上で動作、MCP経由でサードパーティツール統合予定
  - Antigravity 2.0: スタンドアロンデスクトップアプリ、エージェントオーケストレーション
  - TPU 8t/8i: 8世代目、トレーニング推論で専門化。100万TPU以上で分散トレーニング
  - capex年間$180-190B（2022年の$31Bから6倍）
  - OpenAI、Kakao、ElevenLabsがSynthID採用
- **引用URL:** https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
- **Evidence ID:** EVD-20260527-0003

### INFO-004
- **タイトル:** Introducing Managed Agents in the Gemini API
- **ソース:** Google Blog (公式)
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-001-03
- **関連企業:** Google
- **要約:** Gemini APIでManaged Agents機能をローンチ。AGENTS.md/SKILL.md形式でエージェントを定義し、リモートLinuxサンドボックスで実行。Antigravityエージェントベースにカスタムエージェント構築可能。Interactions API経由で利用。
- **キーファクト:**
  - AGENTS.mdとSKILL.mdでエージェント定義（OpenAIのSkills/Shellと同パターン）
  - リモートLinuxサンドボックスでコード実行・Web閲覧・ツール使用
  - Ramp、ResembleAI、Klipy、Stitchが初期採用
  - エンタープライズ向けはGemini Enterprise Agent Platformで提供
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/
- **Evidence ID:** EVD-20260527-0004

### INFO-005
- **タイトル:** Agents for financial services
- **ソース:** Anthropic Blog (公式)
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Anthropicが金融サービス向け10個のエージェントテンプレートをリリース。Microsoft 365統合（Excel/PowerPoint/Word/Outlook）、8社の新コネクタ、Moody's MCP app追加。Citadel、FIS、BNY、Carlyle、Mizuho等が採用。Claude Opus 4.7がVals AI Finance Agent benchmark首位（64.37%）。
- **キーファクト:**
  - 10個の金融エージェントテンプレート（Pitch builder、KYC screener、Month-end closer等）
  - Claude for Excel/PowerPoint/Word/Outlook統合（Outlookは近日公開）
  - 8社新コネクタ（Dun & Bradstreet、Fiscal AI、Guidepoint、IBISWorld等）
  - Moody'sがMCP app提供開始（6億社以上の信用データ）
  - 100% of Walleye Capital employees use Claude Code（400人ヘッジファンド）
- **引用URL:** https://www.anthropic.com/news/finance-agents
- **Evidence ID:** EVD-20260527-0005

### INFO-006
- **タイトル:** Anthropic's Long-Term Benefit Trust appoints Vas Narasimhan to Board of Directors
- **ソース:** Anthropic Blog (公式)
- **公開日:** 2026-04-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** Anthropic
- **要約:** AnthropicのLong-Term Benefit TrustがNovartis CEOのVas Narasimhanを取締役に任命。Trust任命の取締役が過半数となり、公益使命のガバナンス強化。Narasimhanは医師科学者で35以上の新薬承認を監督。
- **キーファクト:**
  - Trust任命取締役がBoard過半数に
  - NarasimhanはUS National Academy of Medicine選出メンバー
  - 医療・ライフサイエンス分野でのAI安全性に関与
- **引用URL:** https://www.anthropic.com/news/narasimhan-board
- **Evidence ID:** EVD-20260527-0006

### INFO-007
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic Blog (公式)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropic LabsがClaude Designをローンチ。Claude Opus 4.7搭載のビジュアル作成ツール。デザイン、プロトタイプ、プレゼン等を作成。Canva、Brilliant、Datadogがパートナー。Claude Codeへのハンドオフ機能付き。
- **キーファクト:**
  - Claude Opus 4.7のビジョンモデル活用
  - チームのデザインシステムを自動適用
  - Canva/PDF/PPTX/HTMLエクスポート対応
  - Claude Codeへのワンクリックハンドオフ
  - Pro/Max/Team/Enterprise向けリサーチプレビュー
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260527-0007

### INFO-008
- **タイトル:** OpenAI model disproves Erdős unit distance conjecture — first autonomous AI solution of a major open math problem
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-05-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** OpenAIの汎用推論モデルが80年間未解決だったErdősの単位距離問題を自律的に解決。離散幾何学の中心的予想を反証し、代数的整数論の高度な手法（class field towers、Golod-Shafarevich理論）を用いた多項式改善を示す構成を発見。初めてAIが著名な未解決問題を自律的に解いた事例。Fields medalist Tim Gowersが「AI数学のマイルストーン」と評価。外部数学者によるcompanion paper付き。
- **キーファクト:**
  - 80年間未解決のErdős unit distance problem（1946年）を反証
  - n^{1+o(1)}の上界予想を否定、n^{1+δ}の構成を発見（δ=0.014: Will Sawin精密化）
  - 代数的整数論（class field towers、Golod-Shafarevich理論）を離散幾何学に初適用
  - 汎用推論モデル（数学専用訓練なし）が自律的に発見
  - Noga Alon「全组合せ幾何学者が考えた問題」、Tim Gowers「Annals of Mathematicsに躊躇なく受理推奨」
  - Arul Shankar「AIは人間数学者のヘルパーを超え、独創的アイデアを実行できる」
  - Princeton Prof Will Sawinの精密化でδ=0.014を達成
- **引用URL:** https://openai.com/index/model-disproves-discrete-geometry-conjecture/
- **Evidence ID:** EVD-20260527-0008

### INFO-009
- **タイトル:** OpenAI advancing content provenance for safer AI ecosystem
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** OpenAIがコンテンツの出所証明技術の推進を発表。Google SynthIDへの参加を含む、AI生成コンテンツの透明性向上取り組み。
- **キーファクト:**
  - OpenAIがGoogle SynthIDを採用（I/O 2026で発表）
  - コンテンツの出所証明技術の業界横断展開
- **引用URL:** https://openai.com/index/advancing-content-provenance/
- **Evidence ID:** EVD-20260527-0009

### INFO-010
- **タイトル:** OpenAI Codex on Windows sandbox + TanStack npm supply chain response
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** CodexのWindows向けセーフサンドボックス構築の技術解説。TanStack npmサプライチェーン攻撃への対応報告。
- **キーファクト:**
  - Windows向けOSレベルサンドボックス実装
  - npm supply chain攻撃に対するセキュリティ対応
- **引用URL:** https://openai.com/index/building-codex-windows-sandbox/
- **Evidence ID:** EVD-20260527-0010

### INFO-011
- **タイトル:** OpenAI Sandbox Agents SDK with persistent workspaces
- **ソース:** GitHub (openai/openai-agents-js releases)
- **公開日:** 2026-05-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKにSandbox Agents機能を追加。永続的ワークスペースとサンドボックス機能を持つエージェントをJavaScriptで実行可能に。
- **キーファクト:**
  - Sandbox Agents SDK機能がbeta追加
  - 永続的ワークスペース対応
- **引用URL:** https://github.com/openai/openai-agents-js/releases
- **Evidence ID:** EVD-20260527-0011

### INFO-012
- **タイトル:** Anthropic Claude Agent SDK活発な開発継続（v0.3.150）
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-05-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版がv0.3.150に更新。2日前のリリース。6月15日から有料Claudeプランに月額クレジット付与（Agent SDK、Claude Code GitHub Actions含む）。
- **キーファクト:**
  - v0.3.150リリース（頻繁な更新継続）
  - 6月15日から有料プランにAgent SDK利用クレジット付与
  - Stainless買収によりSDK品質向上
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260527-0012

### INFO-013
- **タイトル:** Google Gemini Enterprise Agent PlatformでVertex AI置き換え
- **ソース:** Reddit (r/googlecloud)
- **公開日:** 2026-05-20
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google
- **要約:** GoogleがVertex AIを新「Gemini Enterprise Agent Platform」に置き換え。自律システム構築向けに再設計。Managed Agents API、Antigravity連携。
- **キーファクト:**
  - Vertex AI → Gemini Enterprise Agent Platform名称変更
  - 自律エージェント構築に特化した再設計
  - Managed Agents、Interactions API提供
- **引用URL:** https://www.reddit.com/r/googlecloud/comments/1tix8qi/
- **Evidence ID:** EVD-20260527-0013

### INFO-014
- **タイトル:** xAI Grok Build coding agent public beta launch
- **ソース:** xAI Blog + Crypto Briefing + TECHi
- **公開日:** 2026-05-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIがGrok Buildコーディングエージェントをpublic betaでローンチ。CLI版は200万トークンコンテキスト、API版は256K。MCP、プラグイン、エンタープライズコントロール対応。CodexやClaude Codeと競合。
- **キーファクト:**
  - 5月25日public beta開始（SuperGrok/X Premium+向け）
  - CLI版: 200万トークンコンテキスト
  - API版: 256Kコンテキスト（5月20日頃利用可能）
  - MCP、プラグイン、Plan Mode、Imagine機能
  - エンタープライズ向けAPI + 監査機能
- **引用URL:** https://x.ai/news/grok-build-cli
- **Evidence ID:** EVD-20260527-0014

### INFO-015
- **タイトル:** Anthropic enterprise security: 28 new Claude integrations + Compliance API
- **ソース:** Coe Security + Netskope + Yahoo Finance
- **公開日:** 2026-05-20
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Anthropicが28の新Claude統合でエンタープライズセキュリティを強化。Netskope、Fortinet、Palo Alto NetworksがClaude Compliance APIと統合。SOC 2 Type II認証。Claude利用の可視性・ポリシー執行・データセキュリティ提供。
- **キーファクト:**
  - 28の新規エンタープライズセキュリティ統合
  - Claude Compliance API提供開始
  - Netskope、Fortinet、Palo Alto Networksが統合パートナー
  - SOC 2 Type II認証維持
- **引用URL:** https://coesecurity.com/anthropic-strengthens-enterprise-ai-security-with-28-new-claude-integrations/
- **Evidence ID:** EVD-20260527-0015

### INFO-016
- **タイトル:** SAP attempts to become gatekeeper of enterprise AI via API policy
- **ソース:** Forrester Blog
- **公開日:** 2026-05-22
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01, KIQ-001-05
- **関連企業:** SAP
- **要約:** SAPが6月9日からAPI政策を「紙の規則」から「運用制約」に移行。エンタープライズAIのゲートキーパー化を図る。サードパーティAIエージェントによるSAPデータアクセス制限の可能性。
- **キーファクト:**
  - 6月9日からAPI policy変更（紙のルール→運用制約）
  - エンタープライズAIデータアクセスの制御強化
  - CIOは抵抗すべきとForresterが提言
- **引用URL:** https://www.forrester.com/blogs/sap-is-attempting-to-become-the-gatekeeper-of-enterprise-ai-cios-should-push-back/
- **Evidence ID:** EVD-20260527-0016

### INFO-017
- **タイトル:** AI Agent Market $12.5B → $45.3B by 2034
- **ソース:** Intel Market Research
- **公開日:** 2026-05-20
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (市場全体)
- **要約:** グローバルAIエージェント市場は2025年$125億から2034年$453億に成長予測。Deloitte調査で52%の経営者がAIエージェントを最重要技術と認識。
- **キーファクト:**
  - 2025年$12.5B → 2034年$45.3B（CAGR 45.1%）
  - 52%の経営者がAIエージェントを最重要技術と回答
- **引用URL:** https://www.intelmarketresearch.com/ai-agent-market-46955
- **Evidence ID:** EVD-20260527-0017

### INFO-018
- **タイトル:** Agentic AI production deployment: 20-70% cost reductions
- **ソース:** JadaSquad
- **公開日:** 2026-05-20
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (市場全体)
- **要約:** 本番環境でAIエージェントを展開する組織が20-70%のコスト削減、30-80%の時間短縮を報告。Gartner推計で2026年にエンタープライズアプリの40%がタスク特化AIエージェントを組み込む。
- **キーファクト:**
  - 対象プロセスで20-70%コスト削減
  - 30-80%の時間改善
  - Gartner: 2026年にエンタープライズアプリの40%がAIエージェント組み込み
- **引用URL:** https://www.jadasquad.com/blog/agentic-ai-business-impact
- **Evidence ID:** EVD-20260527-0018

### INFO-019
- **タイトル:** Trump postpones AI executive order
- **ソース:** PBS + Fox News
- **公開日:** 2026-05-22
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (政策)
- **要約:** トランプ大統領がAI大統領令の署名を延期。「令の内容に満足していない」と説明。AI企業にモデルの政府提出を求める条項が含まれていたと報道。連邦レベルのAI規制の真空が拡大。
- **キーファクト:**
  - 大統領令署名を直前で延期
  - モデル提出要件に不満との報道
  - 連邦規制の空白拡大
- **引用URL:** https://www.pbs.org/newshour/politics/watch-trump-explains-why-he-postponed-signing-ai-executive-order
- **Evidence ID:** EVD-20260527-0019

### INFO-020
- **タイトル:** EU AI Act enforcement timeline: August 2026 high-risk obligations
- **ソース:** Digital Applied + Aqua Cloud
- **公開日:** 2026-05-20
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** (規制)
- **要約:** EU AI Actの高リスクAI義務とArticle 73インシデント報告が2026年8月2日に発効。禁止条項は既に適用中。違反罰金は最大€3500万または全世界年商7%。
- **キーファクト:**
  - 高リスクAI義務: 2026年8月2日発効
  - Article 73インシデント報告制度
  - 違反罰金: €3500万または年商7%
- **引用URL:** https://www.digitalapplied.com/blog/state-of-ai-agents-2026-200-data-points
- **Evidence ID:** EVD-20260527-0020

### INFO-021
- **タイトル:** Anthropic designated Pentagon supply chain risk for refusing autonomous weapons — Kavout detailed analysis
- **ソース:** Kavout + Reuters + PBS + Fox News
- **公開日:** 2026-05-22
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Pentagon, NVIDIA
- **要約:** ペンタゴンがAnthropicをSCR（サプライチェーンリスク）に指定。自律型兵器・大規模監視へのClaude利用拒否が理由。トランプ大統領が全連邦機関にAnthropic製品使用停止を命令。OpenAIは直後に既存法規に準拠する形でペンタゴン契約を獲得（Anthropicが求めた明示的契約禁止条項は含まず）。Anthropic $200M DoD契約 vs $14B総収益。Anthropicは$380B評価額でIPO計画中に規制リスク直面。NVIDIA $4.45T市場Cap、ハードウェア層は両陣営から需要。
- **キーファクト:**
  - ペンタゴンがAnthropicをSCR指定（通常は外国敵対企業向け）
  - トランプ大統領命令: 全連邦機関がAnthropic製品使用停止
  - SCR指定 = 軍事請負業者はAnthropicとの一切の商取引禁止
  - Anthropic DoD契約: $200M（総収益$14Bの一部）
  - OpenAI: 既存連邦法・DoD政策に準拠する形でペンタゴン契約獲得
  - Undersecretary Lewin「OpenAIの条件はAnthropicにも提示されたが拒否された」
  - NVIDIA $4.45T市場Cap、ハードウェア需要は両陣営に共通
  - Anthropic $380B評価額、IPO予定日に規制リスク
  - Treasury、State、HHSがClaude段階的廃止確認
- **引用URL:** https://www.kavout.com/market-lens/the-ai-ethics-showdown-anthropic-vs-the-pentagon
- **Evidence ID:** EVD-20260527-0021

### INFO-022
- **タイトル:** AI layoffs accelerating: 99% CEOs expect AI-driven layoffs in 2 years
- **ソース:** Gizmodo + Morning Brew + tech.co
- **公開日:** 2026-05-22
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo, Oracle, Amazon, Meta, Microsoft, Intel
- **要約:** AIレイオフ加速中。Oracle、Amazon、Meta、Microsoft、Intel、CognizantがAI自動化による大規模人員削減。KlarnaはAIが700人のCS業務代替を発表もROI疑問視。Duolingoは10%チーム削減しAIに移行。99%のCEOが2年内にAIレイオフ予測。Gartner調査で80%のAI採用企業がレイオフ実施。
- **キーファクト:**
  - Klarna: AIが700人分のCS業務代替（しかし反応時間2分→短縮も品質疑問）
  - Duolingo: 10%チーム削減→AI移行
  - 8社が10,000人以上のAI関連レイオフ（Accenture、Amazon、Microsoft等）
  - Gartner: AI採用企業の80%がレイオフ実施（ROI無関係）
- **引用URL:** https://tech.co/news/companies-replace-workers-with-ai
- **Evidence ID:** EVD-20260527-0022

### INFO-023
- **タイトル:** SaaS market cap $2T evaporation as AI agents replace SaaS categories
- **ソース:** Institute PM
- **公開日:** 2026-05-20
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** (SaaS業界全体)
- **要約:** 2026年1-2月で約$2兆のソフトウェア市場キャップが消失。AIエージェントがSaaS製品カテゴリ全体を代替開始。SaaSビジネスモデルの根本的解体進行中。
- **キーファクト:**
  - 2026年1-2月で$2T market cap消失
  - AIエージェントがSaaS製品全体を代替
  - 従来のSaaSビジネスモデル解体
- **引用URL:** https://www.institutepm.com/knowledge-hub/ai-agents-saas-disruption-strategy
- **Evidence ID:** EVD-20260527-0023

### INFO-024
- **タイトル:** Google rolls out AI-powered ad formats at Marketing Live
- **ソース:** Proactive Investors
- **公開日:** 2026-05-20
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google
- **要約:** GoogleがMarketing LiveでAI搭載広告フォーマットを発表。ChatGPT約9億ユーザーによるAI非中介化リスクに対処。SalesforceがAnthropicに年間$3億のトークン支出を計画。
- **キーファクト:**
  - AI搭載広告フォーマット発表
  - ChatGPT 9億ユーザーへの対抗
  - Salesforce Anthropic年間$300M予算
- **引用URL:** https://www.proactiveinvestors.com/companies/news/1092827/google-rolls-out-ai-powered-ad-formats-at-marketing-live-1092827.html
- **Evidence ID:** EVD-20260527-0024

### INFO-025
- **タイトル:** LLM API pricing crisis: $30/MTok → $1-5/MTok compression
- **ソース:** llmpricing + Investing.com + Reddit
- **公開日:** 2026-05-20
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, (業界全体)
- **要約:** 2023年に$30/MTokが2026年には$1-5/MTokに価格低下。Claude Codeは平均$6/開発者/日（90%が$12以下）。DeepSeekがV4-Pro価格を75%カット。Gemini 3.5 Flashは他のフロンティアモデルの半額以下。
- **キーファクト:**
  - 2023年$30/MTok → 2026年$1-5/MTok（95%以上のコスト削減）
  - Claude Code平均$6/開発者/日
  - DeepSeek V4-Pro価格75%カット
  - Gemini 3.5 Flash: 80%ワークロード移行で年間$1B+節約可能
- **引用URL:** https://sanand0.github.io/llmpricing/
- **Evidence ID:** EVD-20260527-0025

### INFO-026
- **タイトル:** DeepSeek V4 Pro 75% price cut hits OpenAI and Anthropic
- **ソース:** Techzine + Reddit + Facebook
- **公開日:** 2026-05-22
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeekがV4-Pro価格を75%カット。1.6兆パラメータのオープンソースモデル。$10.29Bの資金調達を実施し、オープンソースAI開発を継続。Western商用モデルに価格圧力。
- **キーファクト:**
  - V4-Pro価格75%カット
  - 1.6Tパラメータ、オープンソース
  - $10.29B資金調達
  - 梁文鋒がオープンソース継続をコミット
- **引用URL:** https://www.techzine.eu/news/applications/141586/
- **Evidence ID:** EVD-20260527-0026

### INFO-027
- **タイトル:** AI startup funding: xAI $20B Series E, Modal Labs $355M, OpenAI $182.6B valuation
- **ソース:** Forbes + Crunchbase + Crescendo AI
- **公開日:** 2026-05-22
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** xAI, OpenAI, Modal Labs
- **要約:** xAIが年初に$200億Series Eを調達（Q1 2026の4つのメガディールの1つ）。OpenAI評価額$1826億。Modal Labsが$3.55億Series C。Anthropic、Mistral、Google DeepMind、Metaが5日間に4件の買収を実施（ consolidation signal）。
- **キーファクト:**
  - xAI: $20B Series E（Q1 2026最大）
  - OpenAI: $182.6B評価額（Forbes AI 50）
  - Anthropic买Stainless、Mistral/Google/Metaも買収
  - Q1 2026に4件の記録的メガディール
- **引用URL:** https://news.crunchbase.com/venture/biggest-funding-rounds-medical-devices-futuristic-ai-gadgets-frontier-labs-mirus/
- **Evidence ID:** EVD-20260527-0027

### INFO-028
- **タイトル:** US data center power demand to double by 2027
- **ソース:** Goldman Sachs + McKinsey
- **公開日:** 2026-05-20
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** (インフラ業界)
- **要約:** 米国データセンター電力需要が2025年31GW→2027年66GWに倍増予測。McKinsey推計で2030年までに$5.2兆のデータセンターインフラ投資が必要。AIインフラ投資劇的加速。
- **キーファクト:**
  - 米国DC電力: 31GW (2025) → 66GW (2027)
  - $5.2T投資必要（McKinsey、2030年まで）
  - Vantage Data Centers $25Bフロンティアhyperscale案件
- **引用URL:** https://www.goldmansachs.com/insights/articles/us-data-center-power-demand-projected-to-double-by-2027
- **Evidence ID:** EVD-20260527-0028

### INFO-029
- **タイトル:** Gemini 3.5 Flash benchmark: 73.3% AIME, 74.2% GPQA Diamond
- **ソース:** Google Blog (Facebook repost) + Codesota
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Google
- **要約:** Gemini 3.5 FlashがAIME 73.3%、GPQA Diamond 74.2%を達成。3.1 Proをほぼ全ベンチマークで上回る。4倍速い出力速度。OpenAI Erdos証明（離散幾何学予想反証）がAI研究能力の新段階を示す。
- **キーファクト:**
  - Gemini 3.5 Flash: AIME 73.3%, GPQA Diamond 74.2%
  - 他フロンティアモデルの4倍速い
  - 3.1 Proをほぼ全ベンチマークで上回る
  - OpenAI Erdos証明で数学推論能力の新段階
- **引用URL:** https://www.codesota.com/llm
- **Evidence ID:** EVD-20260527-0029

### INFO-030
- **タイトル:** Open-Weight LLMs approaching commercial API performance
- **ソース:** arXiv + Taskade
- **公開日:** 2026-05-20
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** (オープンソース)
- **要約:** オープンウェイトLLMが商用APIパフォーマンスに接近。日常業務でのギャップは一桁百分比に縮小。LMSYSによると「大幅なギャップ」は依然存在するが、オープンソースモデルが急速に改善。
- **キーファクト:**
  - 日常業務でのギャップが一桁%に縮小
  - arXiv論文: Open-Weight LLMs competitive with commercial APIs
  - コスト面ではオープンソースが圧倒的優位
- **引用URL:** https://arxiv.org/html/2605.19275v1
- **Evidence ID:** EVD-20260527-0030

### INFO-031
- **タイトル:** AGI timeline: Altman 2025-2028, Hassabis ~2030, Amodei 5-10% GDP growth
- **ソース:** AIMultiple + Sherwood News + Fast Company
- **公開日:** 2026-05-20
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** Sam Altman AGI 2025-2028予測。Demis Hassabis ~2030。Dario AmodeiはGDP5-10%成長・失業率10%持続を予測。9,800のAGI予測を分析したAIMultipleレポート。OpenAI離散幾何学証明がAGI能力の一端を示唆。
- **キーファクト:**
  - Altman: AGI 2025-2028
  - Hassabis: AGI ~2030（20年目標）
  - Amodei: GDP 5-10%成長、失業率10%持続予測
  - 9,800件のAGI予測を統合分析
- **引用URL:** https://aimultiple.com/artificial-general-intelligence-singularity-timing
- **Evidence ID:** EVD-20260527-0031

### INFO-032
- **タイトル:** AI safety regulation debate: 10-year state AI ban proposed in tax bill
- **ソース:** Washington Post + Facebook (NTV News)
- **公開日:** 2026-05-22
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** (政策)
- **要約:** 共和党が税法案に10年間の州AI規制禁止条項を挿入。AI企業が自らルールを書くことに批判。「AI needs a referee not regulator」の議論。California SB 1047の再燃。トランプ政権下で連邦規制の後退継続。
- **キーファクト:**
  - 10年州AI規制禁止条項が税法案に挿入
  - Sam Liccardo「AI needs a referee, not a regulator」
  - California SB 1047安全規制法案の再燃
- **引用URL:** https://www.washingtonpost.com/opinions/2026/05/22/ai-needs-safety-standards-heres-better-way-implement-them/
- **Evidence ID:** EVD-20260527-0032

### INFO-033
- **タイトル:** Canada releases guide on agentic AI use in government
- **ソース:** Canada.ca
- **公開日:** 2026-05-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** (政策)
- **要約:** カナダ政府がAgent AIの政府利用に関するガイドライン発表。責任ある利用原則、リスク管理、実践的ガイダンスを含む。政府機関向けのAgent AI利用ガイドは世界的に先駆的。
- **キーファクト:**
  - カナダ政府Agent AI利用ガイドライン
  - 責任ある利用原則・リスク管理フレームワーク
  - 政府職員向け実践ガイダンス
- **引用URL:** https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-agentic-artificial-antelligence.html
- **Evidence ID:** EVD-20260527-0033

### INFO-034
- **タイトル:** MCP: 97M downloads dominant agent-to-tool protocol
- **ソース:** Digital Applied
- **公開日:** 2026-05-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic, (業界全体)
- **要約:** MCP（Model Context Protocol）が9700万ダウンロードでagent-to-tool protocolの支配的地位に。SKILL.mdが40,000+に急増。NVIDIAもVerified Agent Skills提供開始。複数プラットフォーム間互換性の標準化進行中。
- **キーファクト:**
  - MCP: 97M downloads（agent-to-tool protocol支配的）
  - SKILL.md 40,000+ファイル
  - NVIDIA Verified Agent Skills提供開始
  - Claude Code, Codex, Gemini CLI, Cursor等で相互運用
- **引用URL:** https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp
- **Evidence ID:** EVD-20260527-0034

### INFO-035
- **タイトル:** AWS Bedrock AgentCore: multi-tenant agents + MCP support
- **ソース:** AWS Blog + Scale Factory
- **公開日:** 2026-05-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon/AWS
- **要約:** AWS Bedrock AgentCoreがmulti-tenant agents機能を追加。Agent Registry（preview）でエージェント・ツール・スキル・MCPサーバーのカタログ化・共有・再利用が可能に。Strands Agentsでサーバーレスマルチエージェントオーケストレーション。
- **キーファクト:**
  - Multi-tenant agents対応
  - Agent Registry（preview）でMCPサーバー含むカタログ管理
  - Strands Agents: サーバーレス・マルチエージェント
  - ガバナンス・セキュリティ6ヶ月間のアップデート累積
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/building-multi-tenant-agents-with-amazon-bedrock-agentcore/
- **Evidence ID:** EVD-20260527-0035

### INFO-036
- **タイトル:** Four labs four acquisitions in five days: AI consolidation
- **ソース:** StartupHub AI
- **公開日:** 2026-05-20
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, Mistral, Google DeepMind, Meta
- **要約:** Anthropic、Mistral、Google DeepMind、Metaが5日間に4件のAIスタートアップ買収をそれぞれ実施。AnthropicはStainless（SDKツール）を買収。AI業界のconsolidation加速シグナル。
- **キーファクト:**
  - 5日間に4ラボが4件買収
  - Anthropic → Stainless（SDK品質向上）
  - consolidation加速の明確なシグナル
- **引用URL:** https://www.startuphub.ai/ai-news/ai-news/2026/four-labs-four-acquisitions-ai-consolidation-may-2026
- **Evidence ID:** EVD-20260527-0036

### INFO-037
- **タイトル:** OpenAI Deployment Company $4B bet on implementation
- **ソース:** Kursol + OpenAI Blog
- **公開日:** 2026-05-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI
- **要約:** OpenAIが$40億のDeployment Companyを立ち上げ。モデル品質ではなく実装に真の価値があるとの判断。エンタープライズ向け導入支援に特化。Accenture、Capgemini、PwC等GSIパートナーと協業。
- **キーファクト:**
  - $4B Deployment Company新設
  - 実装（導入支援）に価値の重心移動
  - GSIパートナー網（Accenture、Capgemini等）拡充
- **引用URL:** https://www.kursol.io/blog/ai-breaking-news-2026-05-21-openai-deployment-company
- **Evidence ID:** EVD-20260527-0037

### INFO-038
- **タイトル:** Microsoft governing AI agents at scale: lessons from internal deployment
- **ソース:** Microsoft Blog
- **公開日:** 2026-05-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-002-02
- **関連企業:** Microsoft
- **要約:** Microsoftが社内AIエージェント展開から得たガバナンス経験を共有。Fortune 500企業あたり平均15未満のAIエージェント（Gartner: 2028年に15万予測＝10,000倍増）。
- **キーファクト:**
  - Fortune 500企業あたり平均<15 AIエージェント
  - Gartner: 2028年に150,000予測
  - 13%の組織のみがガバナンス準備完了と自己評価
- **引用URL:** https://www.microsoft.com/insidetrack/blog/governing-ai-agents-at-scale-lessons-from-our-journey-at-microsoft/
- **Evidence ID:** EVD-20260527-0038

### INFO-039
- **タイトル:** Fortune 500 AI agent adoption: fewer than 15 per company
- **ソース:** LinkedIn (Ken Garnett) + Gartner
- **公開日:** 2026-05-22
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (エンタープライズ市場)
- **要約:** Fortune 500企業あたり平均15未満のAIエージェント。Gartnerは2028年に150,000を予測（10,000倍増）。スタートアップとFortune 500が同じAIロードマップ（Sales agent、Support agent、文書要約等）を持つ傾向。
- **キーファクト:**
  - Fortune 500あたり平均<15 AIエージェント
  - Gartner: 2028年150,000予測（10,000x増）
  - 13%の組織のみガバナンス準備完了
- **引用URL:** https://www.linkedin.com/posts/ken-garnett_fewer-than-15-ai-agents-per-fortune-500-company-activity-7464680462796554240-jnPl
- **Evidence ID:** EVD-20260527-0039

### INFO-040
- **タイトル:** Anthropic Claude enterprise: safety-first design with 4.9/5 stars
- **ソース:** Intuition Labs + Reddit + Quasa
- **公開日:** 2026-05-20
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02 (KIQ-AGENT-001 動的)
- **関連企業:** Anthropic
- **要約:** Anthropic Claudeのエンタープライズ展開で安全性が主要な選択理由。SOC 2 Type II認証維持、セキュリティファースト設計。ユーザー評価4.9/5（推論深度・安全性・エンタープライズ対応）。Redditユーザー「安全性と管理性のブランドポジショニングが非常に強力」。
- **キーファクト:**
  - Claude Enterprise: セキュリティファースト設計
  - SOC 2 Type II認証維持
  - ユーザー評価4.9/5
  - 安全性・管理性がブランドの差別化要因
- **引用URL:** https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026
- **Evidence ID:** EVD-20260527-0040

### INFO-041
- **タイトル:** Anthropic sandbox architecture: ephemeral container, human-in-loop, local VM
- **ソース:** Anthropic Engineering Blog + GitHub
- **公開日:** 2026-05-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude製品群のサンドボックスアーキテクチャを公開。3パターン: (1)一時コンテナ(claude.ai)、(2)human-in-the-loopサンドボックス(Claude Code)、(3)ローカルVM(Claude Cowork)。オープンソースSandbox Runtimeも公開。
- **キーファクト:**
  - 3つのサンドボックスパターン公開
  - Sandbox Runtime（srt）をオープンソース化
  - Claude Code: human-in-the-loop設計
  - Claude Cowork: ローカルVM隔離
- **引用URL:** https://www.anthropic.com/engineering/how-we-contain-claude
- **Evidence ID:** EVD-20260527-0041

### INFO-042
- **タイトル:** SKILL.md explosion: 40,000+ agent skills across platforms
- **ソース:** Firecrawl Blog + Railway Docs + GitHub
- **公開日:** 2026-05-20
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** (業界全体)
- **要約:** SKILL.md形式のエージェントスキルが40,000+に爆発的増加。Claude Code、Codex、Gemini CLI、Cursor等で相互運用。Railway、Promptfoo等がAgent Skills仕様に対応。オープンフォーマット標準化が進行中。
- **キーファクト:**
  - SKILL.md 40,000+ファイル（20日で0→40K）
  - Claude Code、Codex、Gemini CLI、Cursor間で相互運用
  - Railway、Promptfoo、LobeHub等が対応
  - オープンフォーマット標準化進行
- **引用URL:** https://www.firecrawl.dev/blog/agent-skills
- **Evidence ID:** EVD-20260527-0042

### INFO-043
- **タイトル:** Claude Code vs Codex vs OpenCode comparison: same model different pricing
- **ソース:** Medium (unicodeveloper)
- **公開日:** 2026-05-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Anthropic, OpenAI
- **要約:** Claude Code Max（Opus 4.7）$100-200/月 vs OpenCode BYOK（Opus 4.7）$30-80/月。同じモデルで類似品質、異なる価格。エコシステムの囲い込みが価格差に現れる構造。
- **キーファクト:**
  - Claude Code Max: $100-200/月（Opus 4.7）
  - OpenCode BYOK: $30-80/月（同Opus 4.7）
  - 同一モデル・類似品質・価格差3-5倍
- **引用URL:** https://medium.com/@unicodeveloper/claude-code-vs-codex-vs-opencode-which-ai-coding-agent-is-actually-the-best-in-2026-baa9f6fd5374
- **Evidence ID:** EVD-20260527-0043

### INFO-044
- **タイトル:** Google AI Studio managed agents: Antigravity with SKILL.md/AGENTS.md
- **ソース:** Google Blog
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Google
- **要約:** Google AI Studioでmanaged agents提供開始。AGENTS.md + SKILL.md形式でエージェント定義。Antigravityエージェントベースにカスタムエージェント構築。OpenAIのSkills/Shellと同一パターンの採用が囲い込み構造の収束を示唆。
- **キーファクト:**
  - AGENTS.md + SKILL.md形式採用（OpenAI同パターン）
  - Antigravityエージェントベース
  - Interactions API経由で利用
  - Ramp、ResembleAI、Stitchが初期採用
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/
- **Evidence ID:** EVD-20260527-0044

### INFO-045
- **タイトル:** Anthropic Ethics Showdown: CEO rejects Pentagon pressure to weaponize AI
- **ソース:** Kavout + Reuters + MetodoViral
- **公開日:** 2026-05-22
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Dario AmodeiがClaudeの自律型兵器・大規模監視への利用を拒否。これに対しペンタゴンがSCR指定で報復。Jeff Dean「大規模監視は憲法修正第4条違反」DeepMind従業員が労働組合結成（軍事AI懸念）。Palantirが$100億陸軍契約獲得。
- **キーファクト:**
  - Amodei: 自律型致死兵器・大量監視への利用拒否
  - Jeff Dean: 大規模監視は第4条違反、言論の自由へのchilling effect
  - DeepMind従業員が労働組合結成（軍事AI懸念）
  - Palantir $10B陸軍契約（75の既存軍事契約を統合）
- **引用URL:** https://www.kavout.com/market-lens/the-ai-ethics-showdown-anthropic-vs-the-pentagon
- **Evidence ID:** EVD-20260527-0045

### INFO-046
- **タイトル:** Google I/O 2026: Gemini 3.5 Flash cost savings - $1B+ annually shifting 80% workloads
- **ソース:** Google Blog (Sundar Pichai keynote)
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01, KIQ-001-01
- **関連企業:** Google
- **要約:** Sundar Pichai基調講演で、トップ企業が1日1兆トークン処理する場合、80%のワークロードを3.5 Flashに移行すると年間$10億以上節約可能と強調。月間3.2 Quadrillion tokens処理。Capex年間$180-190B。
- **キーファクト:**
  - 80%移行で$1B+/年の節約試算
  - 月間3.2 Quadrillion tokens（前年比7倍）
  - 3.5 Flash: 他フロンティアモデルの4倍速い
  - Capex: 年間$180-190B（2022年の6倍）
- **引用URL:** https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
- **Evidence ID:** EVD-20260527-0046

### INFO-047
- **タイトル:** GitHub Copilot facing agentic coding pressure from Cursor, Claude Code, Codex
- **ソース:** WindowsForum + Vellum
- **公開日:** 2026-05-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft, Anthropic, OpenAI
- **要約:** MicrosoftがGitHub Copilotでagent coding圧力に直面。Cursor、Claude Code、OpenAI Codexが競合激化。AIコーディングツールのdeveloper adoptionがほぼ普遍的レベルに到達。
- **キーファクト:**
  - GitHub Copilotがagentic coding競争で圧力
  - AIコーディングツール導入がほぼ普遍的
  - Cursor、Claude Code、Codexが市場再形成
- **引用URL:** https://windowsforum.com/threads/microsoft-and-github-copilot-in-2026-agentic-coding-pressure-from-cursor-claude-code.419533/
- **Evidence ID:** EVD-20260527-0047

### INFO-048
- **タイトル:** Fortune 500 and startups share identical AI agent roadmaps
- **ソース:** Reddit (r/AI_Agents)
- **公開日:** 2026-05-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (エンタープライズ市場)
- **要約:** スタートアップとFortune 500企業が全く同じAIロードマックを持つ：Sales agent、Support agent、Document summarization、Internal chat、CRM統合。AIエージェントの普及パターンが企業規模を問わず収束。
- **キーファクト:**
  - 全企業規模で同一AIロードマップ
  - Sales/Support agent、文書要約が共通トップ优先度
  - ユースケースの収束傾向
- **引用URL:** https://www.reddit.com/r/AI_Agents/comments/1tmkuyw/
- **Evidence ID:** EVD-20260527-0048

### INFO-049
- **タイトル:** Multimodal benchmark 2026: Gemini 3 Pro Deep Think leads
- **ソース:** benchlm.ai
- **公開日:** 2026-05-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-001-04
- **関連企業:** Google, xAI
- **要約:** Gemini 3 Pro Deep Thinkがマルチモーダル&グラウンデッドベンチマークで暫定首位（加重スコア100.0%）。Grok 4.1が97.8%で追走。GPT-5.5、Claude Opus 4.7等も高スコア。
- **キーファクト:**
  - Gemini 3 Pro Deep Think: 100.0%（暫定首位）
  - Grok 4.1: 97.8%
  - マルチモーダル理解でモデル間競争激化
- **引用URL:** https://benchlm.ai/multimodal-grounded
- **Evidence ID:** EVD-20260527-0049

### INFO-050
- **タイトル:** China expands travel curbs to top AI talent at private firms
- **ソース:** Reddit (r/LocalLLaMA)
- **公開日:** 2026-05-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance, (中国AI企業)
- **要約:** 中国が民間AI企業のトップ人材に対する渡航制限を拡大。AI人材の国外流出防止と技術保護が目的。中国規制当局が生成AIサービス管理の新規則も発表。
- **キーファクト:**
  - 民間AI企業トップ人材に渡航制限拡大
  - 2026年5月8日に3規制当局が合同で生成AI規制発表
  - AI人材の国外流出防止が目的
- **引用URL:** https://www.reddit.com/r/LocalLLaMA/comments/1to2n4r/
- **Evidence ID:** EVD-20260527-0050
