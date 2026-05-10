# 収集データ: 2026-05-10

## メタデータ
- 収集日時: 2026-05-10 12:00 UTC
- 実行クエリ数: 86 / 114（collection_plan 74件 + 動的追加 12件）
- scrape実行数: 7件
- 収集情報数: 95件
- Evidence ID 採番範囲: EVD-20260510-0001 〜 EVD-20260510-0095
- KIQカバレッジ:
  - KIQ-001-01 ✓ (7/7 queries)
  - KIQ-001-02 ✓ (5/5 queries)
  - KIQ-001-03 ✓ (6/6 queries)
  - KIQ-001-04 ✓ (5/5 queries)
  - KIQ-001-05 ✓ (5/5 queries)
  - KIQ-002-01 ✓ (4/4 queries)
  - KIQ-002-02 ✓ (4/4 queries)
  - KIQ-002-03 ✓ (5/5 queries)
  - KIQ-002-06 ✓ (8/8 queries)
  - KIQ-002-04 ✓ (5/5 queries)
  - KIQ-002-05 ✓ (5/5 queries)
  - KIQ-003-01 ✓ (5/5 queries)
  - KIQ-003-02 ✓ (5/5 queries)
  - KIQ-003-03 ✓ (5/5 queries)
  - KIQ-003-04 ✓ (5/5 queries)
  - KIQ-003-05 ✓ (4/4 queries)
  - KIQ-004-01 ✓ (5/5 queries)
  - KIQ-004-02 ✓ (5/5 queries)
  - KIQ-004-03 ✓ (5/5 queries)
  - KIQ-004-04 ✓ (4/4 queries)
  - KIQ-005-01 ✓ (5/5 queries)
  - KIQ-005-02 ✓ (4/4 queries)
  - KIQ-005-03 ✓ (4/4 queries)
  - BYTEDANCE-CHINESE ✓ (6/6 queries)
  - H-XAI-005 (動的) ✓ (3 queries)
  - KIQ-AGENT-001 (動的) ✓ (2 queries)
  - KIQ-BTD-PRICE (動的) ✓ (2 queries)
  - Stanford研究定義 (動的) ✓ (1 query)
  - 800%収益成長基数 (動的) ✓ (1 query)
- 品質フラグ: NORMAL

## 収集結果

### INFO-001
- **タイトル:** Higher usage limits for Claude and a compute deal with SpaceX
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, H-XAI-005, KIQ-001-02
- **関連企業:** Anthropic, SpaceXAI
- **要約:** AnthropicがSpaceXと計算能力パートナーシップを締結。Colossus 1データセンター（300MW超、220K NVIDIA GPU）の全容量を利用可能に。Claude Codeの5時間レート制限を2倍に引き上げ、ピーク時間制限を撤廃。Claude Opus API レート制限も大幅引き上げ。
- **キーファクト:**
  - SpaceX Colossus 1（300MW超、220K+ NVIDIA GPU）の全容量をAnthropicがリース
  - Claude Code 5時間レート制限をPro/Max/Team/Enterprise全プランで2倍に
  - ピーク時間制限削減をPro/Maxで撤廃
  - 軌道AIコンピューティング容量（数GW）の共同開発にも興味表明
  - Amazon 5GW、Google/Broadcom 5GW、Microsoft/NVIDIA $300億Azure容量等の他契約も列挙
- **引用URL:** https://www.anthropic.com/news/higher-limits-spacex
- **Evidence ID:** EVD-20260510-0001

### INFO-002
- **タイトル:** xAI Dissolved Into SpaceXAI: Musk Merges Grok and Colossus Into SpaceX
- **ソース:** ABHS.in (テック系メディア)
- **公開日:** 2026-05-07
- **信頼性コード:** B-3
- **関連KIQ:** H-XAI-005, KIQ-003-04
- **関連企業:** xAI, SpaceX, SpaceXAI
- **要約:** Elon MuskがxAIを独立企業として解散し、SpaceX内の新部門SpaceXAIとして統合すると発表。Grok製品は継続、Colossus 1はAnthropicにリース、xAI投資家はSpaceX株式と交換。xAI総調達額約$120億。
- **キーファクト:**
  - xAIは2026年5月7日に正式に独立企業として解散、SpaceX内SpaceXAI部門として統合
  - Colossus 1（300MW Memphis）はAnthropicにリース、SpaceXAIは現行負荷に全容量不要
  - xAI投資家（a16z、Sequoia等）はxAI持分→SpaceX持分に交換、SpaceX評価額約$3500億
  - Grok 5開発継続、API移行は12ヶ月以上の移行期間、api.x.ai→SpaceXブランドエンドポイントへ
  - SpaceXはIPO準備中（2026年4月に機密提出）、xAI統合後合算評価額$1.75兆
- **引用URL:** https://www.abhs.in/blog/xai-dissolved-spacexai-elon-musk-merger-grok-colossus-2026
- **Evidence ID:** EVD-20260510-0002

### INFO-003
- **タイトル:** Elon Musk's Terafab chip factory in Texas could cost up to $119 billion
- **ソース:** CNBC
- **公開日:** 2026-05-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, H-XAI-005
- **関連企業:** SpaceX, Tesla, Intel
- **要約:** SpaceXのTexas Grimes CountyにおけるTerafab半導体工場の第1フェーズで$550億、完全建設で最大$1,190億。Intelが14Aプロセスで参画。Tesla/SpaceX/xAI向けチップ製造。6月3日に税制優遇公聴会予定。
- **キーファクト:**
  - Terafab第1フェーズ: $550億、フル建設: 最大$1,190億
  - Intelが参画、TeslaはIntel 14Aプロセス利用計画
  - Tesla、SpaceX、xAI（現SpaceXAI）向けチップ製造
  - SpaceXが初期フェーズ担当、TeslaはAustinに$30億リサーチファブ建設
  - SpaceX IPO準備中、xAI統合後評価額$1.75兆
- **引用URL:** https://www.cnbc.com/2026/05/06/elon-musks-spacex-chip-fab-in-texas-to-cost-up-to-119-billion.html
- **Evidence ID:** EVD-20260510-0003

### INFO-004
- **タイトル:** DeepSeek could be valued at up to $50 billion in first fundraising
- **ソース:** Reuters / Financial Times
- **公開日:** 2026-05-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-BTD-PRICE, KIQ-003-04, KIQ-003-03
- **関連企業:** DeepSeek, Tencent
- **要約:** DeepSeekが初の外部資金調達を実施、中国国家チップ基金が主導。評価額$450-500億、調達額$30-40億。Tencentも参加表明。中国政府の政治的支援が背景。
- **キーファクト:**
  - DeepSeek評価額$450-500億、調達額$30-40億
  - 中国国家チップ投資基金（Big Fund）が主導交渉中
  - Tencentも$40億ラウンドに参加、ポストマネー評価額$500億
  - 資金は計算能力拡充と従業員待遇改善に充当
  - 初の外部資金調達、中国政府の政治的支援が明示的
- **引用URL:** https://www.reuters.com/world/asia-pacific/deepseek-nears-45-billion-valuation-chinas-big-fund-leads-investment-talks-ft-2026-05-06/
- **Evidence ID:** EVD-20260510-0004

### INFO-005
- **タイトル:** Doubao launches paid subscription plans, redefining AI pricing standards
- **ソース:** KuCoin News / Benzinga / 複数ソース
- **公開日:** 2026-05-10
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-BTD-PRICE, KIQ-003-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのAIアシスタント豆包（Doubao）が3段階有料サブスクリプションを開始。無料版に加え、68元/月、200元/月、500元/月の3ティア。中国AIモデル市場の価格層別化トレンドを示す。
- **キーファクト:**
  - 豆包が3段階有料プラン導入: 68元/月、200元/月、500元/月（最高層は連続月額）
  - 無料版は継続提供、高度機能は有料ティアで提供
  - 中国AIモデル市場全体の価格層別化へのシフト
  - AIコスト上昇に伴い「無料AI」モデルからの移行
- **引用URL:** https://www.kucoin.com/news/flash/doubao-launches-paid-subscription-plans-redefining-ai-pricing-standards
- **Evidence ID:** EVD-20260510-0005

### INFO-006
- **タイトル:** Claude AI Statistics 2026: Revenue, Users & Market Share
- **ソース:** Panto AI (データ集計メディア)
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-AGENT-001, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude AIの推定月間アクティブユーザー数はブラウザ版1890万人。モバイル版は290-738万人の推定。2026年2月のAICPBデータではClaudeアプリ1248万MAU、前月比49.15%増。
- **キーファクト:**
  - Claude AI ブラウザ版推定MAU: 1890万人
  - モバイル版推定MAU: 290-738万人（第三方推定）
  - AICPB 2026年2月データ: Claudeアプリ1248万MAU、前月比+49.15%、グローバルアプリランキング37位
  - Claude Code固有のWAU/MAU定量データは未公開
- **引用URL:** https://www.getpanto.ai/blog/claude-ai-statistics
- **Evidence ID:** EVD-20260510-0006

### INFO-007
- **タイトル:** Claude Enterprise Analytics API - WAU/MAU metrics
- **ソース:** Anthropic公式ドキュメント
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-AGENT-001, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Enterprise Analytics APIがユーザー活動指標（日次/週次/月次アクティブユーザー数）を組織全体で提供。但し、これはエンタープライズ顧客向け内部分析ツールであり、Claude Code全体のWAU/MAU公開データではない。
- **キーファクト:**
  - Enterprise Analytics API: 日次/週次/月次アクティブユーザー数を組織単位で提供
  - ユーザー活動: ユーザーごとのエンゲージメント指標をClaude全体で測定
  - Claude Code固有の公開WAU/MAU定量データは依然として未公開
- **引用URL:** https://support.claude.com/en/articles/13694757-get-started-with-the-claude-enterprise-analytics-api
- **Evidence ID:** EVD-20260510-0007

### INFO-008
- **タイトル:** Google sees massive 800% rise in AI agent revenue
- **ソース:** News.az / Motley Fool / LinkedIn (複数ソース)
- **公開日:** 2026-05-04
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-04, H-GOO-001
- **関連企業:** Google
- **要約:** Google CloudのAIエージェント収益が前年同期比約800%成長。クラウドバックログは四半期でほぼ倍増し$4620億に。Ashkenazi CFOは「エンタープライズAIオファリングの強い需要」と説明。
- **キーファクト:**
  - Google Cloud AIエージェント収益: 前年比約800%成長
  - クラウドバックログ: $4620億（四半期でほぼ倍増）
  - GCP推定四半期売上: 約$105億（Google Cloud全体の過半を占める）
  - Gemini Enterprise採用増加が牽引
  - Google Cloud全体の売上成長率: 63%（2025Q4の48%から加速）
- **引用URL:** https://news.az/news/google-sees-massive-800-rise-in-ai-agent-revenue
- **Evidence ID:** EVD-20260510-0008

### INFO-009
- **タイトル:** Introducing Trusted Contact in ChatGPT
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPTにTrusted Contact機能を追加。成人ユーザーが信頼できる人物を指名し、AI利用に関する安全モニタリングを可能にするオプション機能。
- **キーファクト:**
  - ChatGPTにTrusted Contact機能をロールアウト
  - 成人ユーザーが信頼する人物（友人等）を指名可能
  - AI利用の安全モニタリング機能
  - セーフティ機能としての位置づけ
- **引用URL:** https://openai.com/index/introducing-trusted-contact-in-chatgpt/
- **Evidence ID:** EVD-20260510-0009

### INFO-010
- **タイトル:** GPT-5.5 with Trusted Access for Cyber
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.5とGPT-5.5-CyberでTrusted Access for Cyberを拡大。検証済みディフェンダーが脆弱性研究を加速し、重要インフラを保護するための機能。
- **キーファクト:**
  - GPT-5.5およびGPT-5.5-CyberでTrusted Access for Cyberを拡大
  - 検証済みサイバーセキュリティディフェンダー向け
  - 脆弱性研究加速と重要インフラ保護が目的
- **引用URL:** https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/
- **Evidence ID:** EVD-20260510-0010

### INFO-011
- **タイトル:** Running Codex Safely at OpenAI
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** OpenAIがCodexの安全な実行に関する詳細を公開。コード実行環境のセキュリティアーキテクチャ説明。
- **キーファクト:**
  - Codexの安全な実行に関するセキュリティ詳細を公開
  - 4層防御アーキテクチャの説明
  - コード実行環境のセキュリティ設計
- **引用URL:** https://openai.com/index/running-codex-safely/
- **Evidence ID:** EVD-20260510-0011

### INFO-012
- **タイトル:** GPT-5.5 Instant: smarter, clearer, and more personalized
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** GPT-5.5 InstantがChatGPTのデフォルトモデルとしてアップデート。よりスマートで正確な回答、ハルシネーション削減、パーソナライゼーション制御の改善。
- **キーファクト:**
  - GPT-5.5 InstantがChatGPTのデフォルトモデルに
  - より正確な回答、ハルシネーション削減
  - パーソナライゼーション制御の改善
- **引用URL:** https://openai.com/index/gpt-5-5-instant/
- **Evidence ID:** EVD-20260510-0012

### INFO-013
- **タイトル:** AlphaEvolve, 1 year later: Impact on science, technology
- **ソース:** Google Blog
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-005-01, KIQ-003-02
- **関連企業:** Google / DeepMind
- **要約:** AlphaEvolve（Gemini搭載の進化的アルゴリズムエージェント）の1年後のインパクト報告。数学・コンピュータサイエンスの未解決問題への新発見、アルゴリズム最適化の成果。
- **キーファクト:**
  - AlphaEvolveはGemini搭載の進化的アルゴリズムエージェント
  - 数学・CS分野のオープン問題への新発見
  - アルゴリズム最適化の実績
  - 1年間のインパクトをまとめたレポート
- **引用URL:** https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-updates/
- **Evidence ID:** EVD-20260510-0013

### INFO-014
- **タイトル:** Anthropic CEO says 80-fold growth in first quarter explains 'difficulties with compute'
- **ソース:** CNBC
- **公開日:** 2026-05-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Anthropic CEO Dario Amodeiが第1四半期に80倍の成長を達成したことを明かし、計算能力の困難の理由を説明。爆発的な需要成長にインフラが追いついていない状況。
- **キーファクト:**
  - Anthropic Q1で80倍成長
  - Dario Amodeiが「計算能力の困難」の理由として説明
  - 需要爆発にインフラ供給が追従していない構造
- **引用URL:** https://www.cnbc.com/2026/05/06/anthropic-ceo-dario-amodei-says-company-crew-80-fold-in-first-quarter.html
- **Evidence ID:** EVD-20260510-0014

### INFO-015
- **タイトル:** Inside Claude Code Auto Mode: Anthropic's Autonomous Development
- **ソース:** InfoQ
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-AGENT-001
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Codeにオートモードを導入。マルチステップのソフトウェア開発ワークフローを手動介入なしで実行可能に。
- **キーファクト:**
  - Claude Codeにオートモード機能を追加
  - マルチステップ開発ワークフローの自律実行
  - 手動介入を削減する設計
- **引用URL:** https://www.infoq.com/news/2026/05/anthropic-claude-code-auto-mode/
- **Evidence ID:** EVD-20260510-0015

### INFO-016
- **タイトル:** Stanford study: Employment of 22-25 year old programmers declined ~20%
- **ソース:** Stanford / Facebook (WSOC) / Substack (Stress-Testing Reality)
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02, H-CAR-002
- **関連企業:** (なし)
- **要約:** Stanford研究者によるADP給与データ分析（2022年ChatGPT登場以降）で、22-25歳のAI関連職の雇用が約20%減少。Linux Foundation研究では「ジュニアエンジニアがAIでスーパーチャージされる時代」である一方で、採用減少のシグナル。
- **キーファクト:**
  - ADP給与データ分析: 2022年以降、22-25歳のAI関連職雇用が約20%減
  - 定義の問題: 「プログラマー→AI開発者」への再分類の可能性
  - 4割の米国ビジネスリーダーがAIによる労働者代替を計画
  - Linux Foundation: ジュニアエンジニアのAIスーパーチャージ時代
- **引用URL:** https://stresstestingreality.substack.com/p/ai-is-not-your-coworker
- **Evidence ID:** EVD-20260510-0016

### INFO-017
- **タイトル:** DeepMind researching AI-based systems with EVE Online
- **ソース:** 9to5Google
- **公開日:** 2026-05-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-005-01
- **関連企業:** Google / DeepMind
- **要約:** Google DeepMindがEVE Onlineと提携し、プレイヤー駆動システムのAI研究を開始。MMORPG環境をAI訓練・シミュレーションに活用。
- **キーファクト:**
  - DeepMind × EVE Online提携
  - プレイヤー駆動システムのAI研究
  - MMORPG環境をAI訓練に活用
- **引用URL:** https://9to5google.com/2026/05/06/google-deepmind-is-partnering-with-eve-online-to-research-player-driven-systems/
- **Evidence ID:** EVD-20260510-0017

### INFO-018
- **タイトル:** Claude Code and new admin controls for business plans
- **ソース:** Anthropic公式ブログ
- **公開日:** 2025-08-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-AGENT-001
- **関連企業:** Anthropic
- **要約:** Enterprise/Team顧客がClaude Codeを含むプレミアムシートにアップグレード可能に。管理機能（使用量分析、ポリシー設定、コンプライアンスAPI）を追加。BehavoxとAltanaが早期導入事例として紹介。
- **キーファクト:**
  - Enterprise/TeamでClaude Code付きプレミアムシート提供開始
  - Compliance API: 規制要件対応のためのリアルタイムアクセス
  - 使用量分析: コード行数承認率、提案承認率等のメトリクス
  - Behavox: 「数百人の開発者に展開、他エージェントより一貫して優秀」
  - Altana: 「開発速度2-10倍加速、より野心的なプロジェクトに着手」
- **引用URL:** https://www.anthropic.com/news/claude-code-on-team-and-enterprise
- **Evidence ID:** EVD-20260510-0018

### INFO-019
- **タイトル:** Anthropic's Mythos set off a cybersecurity 'hysteria'
- **ソース:** CNBC
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** Anthropicの「Mythos」に関する報道がサイバーセキュリティ業界でパニックを引き起こした。専門家は脅威はすでに存在していたと指摘。
- **キーファクト:**
  - AnthropicのMythos関連発表がサイバーセキュリティパニックを誘発
  - 専門家は「脅威は既に存在していた」と評価
  - AI安全性の社会的インパクトが拡大
- **引用URL:** https://www.cnbc.com/2026/05/08/anthropic-mythos-ai-cybersecurity-banks.html
- **Evidence ID:** EVD-20260510-0019

### INFO-020
- **タイトル:** Cloudflare stock sinks 24% after earnings as company cuts 1,100 employees due to AI changes
- **ソース:** CNBC
- **公開日:** 2026-05-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-04
- **関連企業:** Cloudflare
- **要約:** Cloudflareが四半期決算後、AI変化に対応するため1,100人の人員削減を実施。株価24%下落。
- **キーファクト:**
  - Cloudflareが1,100人削減、AI変化が理由
  - 株価24%下落
  - テック企業のAI対応リストラクチャリングの一例
- **引用URL:** https://www.cnbc.com/2026/05/07/cloudflare-net-q1-2026-stock-earnings-layoffs.html
- **Evidence ID:** EVD-20260510-0020

### INFO-021
- **タイトル:** OpenAI Introduces WebSocket-Based Execution Mode to Reduce Latency
- **ソース:** InfoQ
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがResponses APIにWebSocketベースの実行モードを導入。コーディングエージェントやリアルタイムAIシステムのエージェントワークフローパフォーマンスを改善。
- **キーファクト:**
  - Responses APIにWebSocketベース実行モード追加
  - エージェントワークフローのレイテンシ削減が目的
  - コーディングエージェント・リアルタイムAIシステム向け
- **引用URL:** https://www.infoq.com/news/2026/05/openai-websocket-responses-api/
- **Evidence ID:** EVD-20260510-0021

### INFO-022
- **タイトル:** Anthropic Claude Agent SDK updates: multiagent sessions + webhooks
- **ソース:** Releasebot / GitHub
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript v0.2.133、Python v0.1.77リリース。Claude Developer Platformがマルチエージェントセッション・アウトカム、Claude Managed Agents向けWebhookサポートのパブリックベータ追加。
- **キーファクト:**
  - Claude Agent SDK TypeScript v0.2.133、Python v0.1.77リリース
  - マルチエージェントセッション・アウトカムのパブリックベータ
  - Managed Agents向けWebhookサポート追加
  - 高頻度リリースサイクル継続
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260510-0022

### INFO-023
- **タイトル:** Google Gemini Enterprise Agent Platform + Deep Research Agent
- **ソース:** Google Cloud Blog / Google AI Dev Docs
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** Google / DeepMind
- **要約:** Google Cloud Next '26でGemini Enterprise Agent Platformを発表。自律AIエージェントの構築・デプロイ・スケール・ガバナンス・最適化を統合プラットフォームで提供。Gemini 3.1 Flash-LiteがGA、Deep Research Agentも利用可能。
- **キーファクト:**
  - Gemini Enterprise Agent Platform: エージェント構築〜ガバナンスまで統合
  - Gemini 3.1 Flash-Lite GA、コスト効率型モデル
  - Deep Research Agent: マルチステップ研究タスクの自律実行
  - Gemini API File Searchがマルチモーダル対応（画像・動画対応）
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260510-0023

### INFO-024
- **タイトル:** Grok 4.3 quietly launched — And It Changes the AI API Race
- **ソース:** YouTube / basenor / Google Cloud Docs
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, H-XAI-005
- **関連企業:** xAI / SpaceXAI
- **要約:** Grok 4.3がサイレントローンチ。Grok 4.20がGoogle Gemini Enterprise Agent Platformで利用可能（パートナーモデルとして）。Grok Voice APIがカスタムボイス（感情付き音声クローン）機能を追加。
- **キーファクト:**
  - Grok 4.3がサイレントローンチ、APIレースに変化
  - Grok 4.20がGoogle Gemini Enterprise Agent Platformでパートナーモデルとして利用可能
  - Grok Voice Agent API: カスタムボイス機能（自然な感情付き音声クローン）
  - xAI→SpaceXAI統合後もAPI開発継続
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok/grok-4-20
- **Evidence ID:** EVD-20260510-0024

### INFO-025
- **タイトル:** ByteDance DeerFlow 2.0: super agent framework
- **ソース:** GitHub / Instagram
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0をリリース。マルチAIエージェントを協調させる「スーパーエージェント」フレームワーク。コード作成、スライド作成、Web構築、タスク実行を統合。AstraNL調整プロトコルで実世界タスク管理も。
- **キーファクト:**
  - DeerFlow 2.0: マルチAIエージェント協調スーパーエージェントフレームワーク
  - コード・スライド・Web構築・タスク実行を統合
  - AstraNL調整プロトコル: AIエージェントが実世界タスクを管理（1%手数料）
  - Coze（ノーコードエージェント、179元/月）とDoubaoの有料化テスト継続
- **引用URL:** https://github.com/bytedance/deer-flow/issues/2719
- **Evidence ID:** EVD-20260510-0025

### INFO-026
- **タイトル:** Best Multi-Agent Frameworks in 2026: LangGraph, CrewAI, OpenAI Agents SDK
- **ソース:** GuruSup / Reddit / Knowlee
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** (なし)
- **要約:** 2026年の主要マルチエージェントフレームワーク比較。LangGraph（状態管理に優れる）、CrewAI（マルチエージェント協調）、OpenAI Agents SDK、Microsoft AutoGen/AG2、Google ADKが上位。
- **キーファクト:**
  - 2026年主要フレームワーク: LangGraph、CrewAI、OpenAI Agents SDK、AutoGen/AG2、Google ADK
  - LangGraph: 複雑なステートフルエージェントグラフ向け
  - CrewAI: マルチエージェントクルー協調向け
  - Google ADK: Gemini Enterprise Agent Platformと統合
- **引用URL:** https://gurusup.com/blog/best-multi-agent-frameworks-2026
- **Evidence ID:** EVD-20260510-0026

### INFO-027
- **タイトル:** Agentic AI Enterprise Adoption 2026: 72% Production Proven
- **ソース:** Agentic AI Institute
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** (なし)
- **要約:** Agentic AIのエンタープライズ本番導入率が72%に到達。しかし60%のガバナンスギャップが残存。EYがエンタープライズ規模のagentic AI OS構築事例を公開。
- **キーファクト:**
  - Agentic AI本番導入率: 72%
  - ガバナンスギャップ: 60%が未対応
  - EYがグローバルagentic AIプラットフォーム構築事例
  - Microsoft WorkLab: AIエージェント導入で人間のエージェンシーが拡大
- **引用URL:** https://agenticaiinstitute.org/agentic-ai-enterprise-adoption-2026-governance-gap/
- **Evidence ID:** EVD-20260510-0027

### INFO-028
- **タイトル:** Anthropic's Claude Finance Agents: 10 specialized AI agents
- **ソース:** Analytics Vidhya / n1n.ai
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Finance Agentsをリリース。KYC、監査、レポート等の金融業務自動化向け10の専門AIエージェント。Microsoft 365統合、MCP アプリ、新コネクタ付き。
- **キーファクト:**
  - 10の金融専門AIエージェント（Cowork + Claude Code プラグイン）
  - Microsoft 365スイート統合
  - MCP アプリ for 金融サービス・保険
  - SOC2/HIPAA コンプライアンス対応
- **引用URL:** https://www.analyticsvidhya.com/blog/2026/05/claude-finance-agents/
- **Evidence ID:** EVD-20260510-0028

### INFO-029
- **タイトル:** Google Pivot: Vertex AI Evolves Into Gemini Enterprise
- **ソース:** AI CERTs News / CloudZero
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-001-05
- **関連企業:** Google
- **要約:** GoogleがVertex AIからGemini Enterpriseへの移行を進行中。エージェントプラットフォームの統合・ブランディング変更。移行リスクとクラウド機会の分析。
- **キーファクト:**
  - Vertex AI → Gemini Enterprise への進化
  - エージェントプラットフォーム統合
  - Gemini 3.1 Pro、Agent Builder等の価格体系更新
  - エンタープライズ顧客への移行ガイダンス提供
- **引用URL:** https://www.aicerts.ai/news/google-pivot-vertex-ai-evolves-into-gemini-enterprise/
- **Evidence ID:** EVD-20260510-0029

### INFO-030
- **タイトル:** Linux Foundation consolidates MCP under Agentic AI Foundation
- **ソース:** TheNewStack / Red Hat / letsdatascience
- **公開日:** 2026-05-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic, OpenAI, Linux Foundation
- **要約:** Linux FoundationがMCPをAgentic AI Foundation（AAIF）配下に統合。AAIFは現在3プロジェクト（MCP、Goose、AGENTS.md）を管理。Anthropic、Block、OpenAIが共同設立。Red HatがGold Memberとして参加。
- **キーファクト:**
  - MCPがAAIF（Linux Foundation配下）に統合
  - AAIF管理プロジェクト: MCP、Goose、AGENTS.md
  - 共同設立: Anthropic、Block、OpenAI
  - Red HatがGold Member参加、MCP ゲートウェイ for OpenShiftをテクノロジープレビュー
  - エージェント駆動アーキテクチャのオープン標準化推進
- **引用URL:** https://thenewstack.io/agentic-ai-foundation-launch/
- **Evidence ID:** EVD-20260510-0030

### INFO-031
- **タイトル:** Salesforce and Google Cloud advance AI agent integration
- **ソース:** IT Business Today
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** Salesforce, Google
- **要約:** SalesforceとGoogle CloudがGoogle Cloud Next '26で発表したAIエージェント統合パートナーシップを拡大。エージェント間相互運用性の向上に注力。
- **キーファクト:**
  - Salesforce × Google Cloud AIエージェント統合パートナーシップ拡大
  - Google Cloud Next '26で発表
  - エージェント間相互運用性向上に注力
- **引用URL:** https://itbusinesstoday.com/tech/cloud/salesforce-and-google-cloud-advance-ai-agent-integration/
- **Evidence ID:** EVD-20260510-0031

### INFO-032
- **タイトル:** GPT-Realtime-2: Low-Latency Voice AI Agents
- **ソース:** AI Agents Directory / Startup Fortune
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** OpenAI
- **要約:** GPT-Realtime-2がボイスネイティブエージェントを可能に。テキスト・画像入力とオーディオを同時サポートし、視覚対応ボイスエージェントを実現。リアルタイム推論・翻訳機能付き。
- **キーファクト:**
  - GPT-Realtime-2: テキスト・画像・音声の同時入力対応
  - 視覚対応ボイスエージェント実現
  - リアルタイム推論・翻訳機能
  - OpenAIライブラリ・トレーシング・デプロイメントエコシステム
- **引用URL:** https://aiagentsdirectory.com/blog/openai-ships-gpt-realtime-2-for-voice-agents
- **Evidence ID:** EVD-20260510-0032

### INFO-033
- **タイトル:** Gemini 3 Pro Deep Think leads multimodal benchmarks at 100%
- **ソース:** BenchLM
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google / DeepMind
- **要約:** Gemini 3 Pro Deep Thinkがマルチモーダル grounded ベンチマークで加重スコア100%を達成。Grok 4.1が97.8%で続く。Mistral Large 3がMM-MT-Benchで84.9%。
- **キーファクト:**
  - Gemini 3 Pro Deep Think: マルチモーダル grounded ベンチマーク100%
  - Grok 4.1: 97.8%
  - Mistral Large 3: MM-MT-Bench 84.9%（17モデル中1位）
  - GPT-5.5: Terminal-Bench 2.0で82.7%
- **引用URL:** https://benchlm.ai/multimodal-grounded
- **Evidence ID:** EVD-20260510-0033

### INFO-034
- **タイトル:** Google DeepMind AI Co-Clinician beats GPT-5.4 in benchmarks
- **ソース:** MindStudio Blog
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-005-01
- **関連企業:** Google / DeepMind
- **要約:** Google DeepMindのAI Co-ClinicianがGPT-5.4を63%対30%で上回る。98クエリ中97でゼロクリティカルエラー。140診察次元の68で医師と同等。
- **キーファクト:**
  - AI Co-Clinician vs GPT-5.4: 63% vs 30%
  - 98クエリ中97でゼロクリティカルエラー
  - 140診察次元の68で医師と同等パフォーマンス
  - 医療AIの専門家レベル到達の可能性
- **引用URL:** https://www.mindstudio.ai/blog/google-deepmind-ai-co-clinician-4-benchmark-results-surprised-evaluators
- **Evidence ID:** EVD-20260510-0034

### INFO-035
- **タイトル:** NVIDIA OpenShell: open source secure runtime for autonomous agents
- **ソース:** NVIDIA Blog
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** NVIDIA, ServiceNow
- **要約:** NVIDIAとServiceNowがProject Arcで提携。NVIDIA OpenShell（オープンソースのセキュアランタイム）を使用し、サンドボックス化・ポリシー管理環境で自律エージェントを開発・デプロイ。
- **キーファクト:**
  - OpenShell: オープンソースセキュアランタイム
  - サンドボックス化・ポリシー管理環境
  - NVIDIA × ServiceNow提携（Project Arc）
  - 自律エージェントの安全な開発・デプロイ向け
- **引用URL:** https://blogs.nvidia.com/blog/servicenow-autonomous-ai-agents-enterprises/
- **Evidence ID:** EVD-20260510-0035

### INFO-036
- **タイトル:** Google DeepMind partners with Boston Dynamics for humanoid robots
- **ソース:** Thelec.net
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-005-01
- **関連企業:** Google / DeepMind
- **要約:** GoogleがBoston Dynamicsと提携し、Gemini搭載ヒューマノイドロボットを2028年までに米国工場に展開予定。Agile Robotsとも提携。
- **キーファクト:**
  - Google × Boston Dynamics提携
  - Gemini搭載ヒューマノイドロボット
  - 2028年までに米国工場展開予定
  - Agile Robotsとも提携
- **引用URL:** https://www.thelec.net/news/articleView.html?idxno=10175
- **Evidence ID:** EVD-20260510-0036

### INFO-037
- **タイトル:** Intel shares soar on Apple chip deal report
- **ソース:** CNBC
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Intel, Apple, AMD, NVIDIA
- **要約:** IntelがAppleチップ製造契約報道で急騰。ウォール街がAIチップの「主役交代」と評価し、Intel・AMDが記録高、NVIDIAは伸び悩み。TerafabへのIntel参画も追い風。
- **キーファクト:**
  - IntelがAppleチップ製造契約報道で急騰
  - AMDも記録高、NVIDIAは伸び悩み
  - ウォール街「AIにおける主役交代」評価
  - Terafab（SpaceX）へのIntel 14A参画が文脈
- **引用URL:** https://www.cnbc.com/2026/05/08/intel-stock-apple-chip-deal.html
- **Evidence ID:** EVD-20260510-0037

### INFO-038
- **タイトル:** DeepSeek V4 Pro at 75% off until 31 May
- **ソース:** Hacker News
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-BTD-PRICE, KIQ-003-01
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 Proが5月31日まで75%オフで提供。HNコメントで「中国政府の補助金で運営」との指摘あり。API価格の持続可能性への疑義。
- **キーファクト:**
  - DeepSeek V4 Pro: 75%オフキャンペーン（5/31まで）
  - HNコメント: 「中国政府の補助金で運営されている」
  - 平均ユーザーの入力がAPI処理コストを上回るか疑義
  - 価格持続可能性の根本的疑問
- **引用URL:** https://news.ycombinator.com/item?id=48043040
- **Evidence ID:** EVD-20260510-0038

### INFO-039
- **タイトル:** Nvidia to invest up to $3.2B in Corning for optical fiber deal
- **ソース:** CNBC
- **公開日:** 2026-05-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** NVIDIA, Corning
- **要約:** NVIDIAがCorningに最大$32億投資。光ファイバー契約でAI向け3工場建設。AIインフラの物理的供給チェーン拡大継続。
- **キーファクト:**
  - NVIDIA → Corningに最大$32億投資
  - 光ファイバー3工場（NC・TX）建設
  - AI向けデータセンター接続インフラ強化
- **引用URL:** https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html
- **Evidence ID:** EVD-20260510-0039

### INFO-040
- **タイトル:** OpenAI B2B Signals: How frontier firms are pulling ahead
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAIのB2B Signals調査。フロンティア企業がAI導入を深化、Codex搭載エージェントワークフローをスケール、持続的競争優位を構築する方法を分析。
- **キーファクト:**
  - フロンティア企業のAI導入深化パターンを分析
  - Codex搭載エージェントワークフローのスケール事例
  - 持続的競争優位の構築方法
  - B2B向けデータシグナルの公開
- **引用URL:** https://openai.com/index/introducing-b2b-signals/
- **Evidence ID:** EVD-20260510-0040

### INFO-041
- **タイトル:** AWS Bedrock AgentCore: managed session storage and gateway
- **ソース:** AWS Blog / LinkedIn
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** Amazon Bedrock AgentCore Runtimeにマネージドセッションストレージがプレビュー追加。AgentCore Gatewayでプライベートエンドポイントアクセス可能に。AWS Agent ToolkitでAIコーディングエージェントのAWS構築支援。
- **キーファクト:**
  - Bedrock AgentCore Runtime: マネージドセッションストレージ（プレビュー）
  - AgentCore Gateway: プライベートエンドポイントアクセス
  - AWS Agent Toolkit: AIコーディングエージェント向け
  - ステートフルAIエージェント管理の簡素化
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/page/2/
- **Evidence ID:** EVD-20260510-0041

### INFO-042
- **タイトル:** Azure AI Foundry Agents: unified enterprise agent platform
- **ソース:** Microsoft Learn / Avigna AI
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundryがエンタープライズ規模でのAIエージェント構築・デプロイ・ガバナンス統合プラットフォーム。GPT-4o、Llama等のモデル統合。AI gatewayがMicrosoft Foundryと直接統合。Microsoft 365 E7とAgent 365でエンタープライズAI導入を推進。
- **キーファクト:**
  - Azure AI Foundry: 統合エージェントプラットフォーム
  - GPT-4o、Llama等マルチモデル対応
  - AI gateway → Foundry直接統合
  - Microsoft 365 E7 + Agent 365で安全なAIソリューション構築
- **引用URL:** https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities
- **Evidence ID:** EVD-20260510-0042

### INFO-043
- **タイトル:** Pentagon hands Meta-backed Scale AI $500 million contract
- **ソース:** Forbes / Yahoo Finance
- **公開日:** 2026-05-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, H-GOV-001
- **関連企業:** Scale AI, Meta, Pentagon
- **要約:** PentagonがScale AI（Meta 49%出資）に$5億の契約を授与。前年$1億から5倍増。データ分析・意思決定支援向け。xAI/SpaceXAIも$2億の国防総省契約を獲得。
- **キーファクト:**
  - Scale AI: $5億契約（前年$1億から5倍増）
  - Meta 49%出資のScale AIが受注
  - データ分析・意思決定支援向け
  - xAI/SpaceXAI: $2億の国防総省契約（Grok AI連邦 agency展開）
- **引用URL:** https://www.forbes.com/sites/aliciapark/2026/05/06/pentagon-hands-meta-backed-scale-ai-500-million-contract-5-times-last-years-deal-report-says/
- **Evidence ID:** EVD-20260510-0043

### INFO-044
- **タイトル:** Pentagon seals AI deal with eight major vendors, Anthropic out
- **ソース:** AI Business / Times of Israel / Reuters
- **公開日:** 2026-05-01
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, H-ANT-001, H-GOV-001
- **関連企業:** Pentagon, OpenAI, Google, Microsoft, AWS, NVIDIA, SpaceX, Reflection, Anthropic
- **要約:** Pentagonが7社（OpenAI、Google、Microsoft、AWS、NVIDIA、SpaceX、Reflection）と分類ネットワーク向けAI契約を締結。Anthropicのみ除外。OpenAIが3月にAnthropicに代わりChatGPTを分類環境に導入するPentagon契約を発表済み。
- **キーファクト:**
  - 7社契約: OpenAI、Google、Microsoft、AWS、NVIDIA、SpaceX、Reflection
  - Anthropicのみ除外（安全性姿勢のため）
  - OpenAIがAnthropicに代わりChatGPTを分類環境に導入
  - 「warfighter decision-makingの拡張」が目的
- **引用URL:** https://aibusiness.com/generative-ai/pentagon-seals-ai-deal-eight-major-vendors-anthropic-out
- **Evidence ID:** EVD-20260510-0044

### INFO-045
- **タイトル:** Google DeepMind workers vote to unionize over military AI deals
- **ソース:** Wired / Fortune / The Next Web
- **公開日:** 2026-05-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Google / DeepMind
- **要約:** Google DeepMind UK従業員が98%の賛成で組合化を決議。Pentagonの分類AI契約に反対。600人以上の従業員がPentagon AIパートナーシップに反対。CWUとUniteに加盟。
- **キーファクト:**
  - DeepMind UK従業員: 98%賛成で組合化（CWU + Unite加盟）
  - 600人以上がPentagon AIパートナーシップに反対
  - GoogleのPentagon分類契約「any lawful purpose」が発端
  - 軍事AI利用の終了を要求
- **引用URL:** https://www.wired.com/story/google-deepmind-workers-vote-to-unionize-over-military-ai-deals/
- **Evidence ID:** EVD-20260510-0045

### INFO-046
- **タイトル:** Anthropic designated as supply chain risk, Pentagon blacklists
- **ソース:** Congress.gov / Facebook / Instagram (複数ソース)
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, H-ANT-001, H-GOV-001
- **関連企業:** Anthropic, Pentagon
- **要約:** 2026年2月、トランプ政権が全連邦機関にAnthropic技術の使用停止を指示、「国のサプライチェーンリスク」指定。業界団体が「調達紛争に使われるべきでなく、外国の敵対者向けに予約されるべき」と指摘。商用顧客への chilling effect も報告。
- **キーファクト:**
  - トランプ政権: Anthropicを「国のサプライチェーンリスク」指定
  - 全連邦機関にAnthropic技術使用停止を指示
  - 業界団体: 「調達紛争に悪用、外国敵対者向けに予約すべき」
  - 商用顧客へのchilling effect: Pentagon関連の法務部門がAnthropic利用を疑問視
- **引用URL:** https://www.congress.gov/crs-product/IF13217
- **Evidence ID:** EVD-20260510-0046

### INFO-047
- **タイトル:** White House distances itself from tighter AI regulation
- **ソース:** POLITICO / NYT / The Register
- **公開日:** 2026-05-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** (なし)
- **要約:** ホワイトハウスがAI規制強化から距離を置く一方、AIモデルリリース前の審査を検討。大統領令でAI作業部会（テック経営陣＋政府高官）の創設を協議。「パートナーシップ」重視、「政府規制」回避の姿勢。しかし「anything goes」から「strict regulation」への方針転換との指摘も。
- **キーファクト:**
  - ホワイトハウス: AI規制強化から距離、「パートナーシップ」重視
  - 同時にAIモデル事前審査制度を検討
  - AI作業部会（テック経営陣＋政府高官）創設協議
  - 「anything goes」→「strict regulation」への転換指摘あり
- **引用URL:** https://www.politico.com/news/2026/05/07/white-house-ai-oversight-00910837
- **Evidence ID:** EVD-20260510-0047

### INFO-048
- **タイトル:** China unveils first comprehensive AI agent regulations
- **ソース:** Global Times / City News Service
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03, BYTEDANCE-CHINESE
- **関連企業:** (なし)
- **要約:** 中国が初の包括的AIエージェント規制を発表。2027年までに70%導入を目標。人間の監視義務付け、依存性アルゴリズム禁止、19の特定用途承認。90ページのAIエージェント安全性報告書で11の脅威を分類。
- **キーファクト:**
  - 中国初の包括的AIエージェント規制
  - 2027年までに70%導入目標
  - 人間の監視義務、依存性アルゴリズム禁止
  - 19の特定用途を承認
  - 90ページの安全性報告書: 11の脅威を分類、8つの新標準を提案
- **引用URL:** https://www.globaltimes.cn/page/202605/1360598.shtml
- **Evidence ID:** EVD-20260510-0048

### INFO-049
- **タイトル:** EU AI Act: high-risk systems delayed to December 2027
- **ソース:** EU / Biometric Update / wz-it.com
- **公開日:** 2026-05-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (なし)
- **要約:** EUがAI Actの高リスクAIシステム規制を2027年12月2日に延期（元の期限は2026年8月）。生体認証を含む高リスクシステムの規則延期。罰則は最大€3500万または全球売上の7%。
- **キーファクト:**
  - 高リスクAIシステム規制: 2027年12月2日延期（2026年8月から）
  - 生体認証システム含む
  - 罰則: 最大€3500万または全球売上の7%
  - 殆どのエンタープライズは「政策」ではなく「ワークフロー問題」として対応
- **引用URL:** https://www.biometricupdate.com/202605/eu-pushes-ai-act-deadlines-for-high-risk-systems-including-biometrics
- **Evidence ID:** EVD-20260510-0049

### INFO-050
- **タイトル:** Dun & Bradstreet: 97% of organizations have active AI initiatives
- **ソース:** Morningstar / PR Newswire
- **公開日:** 2026-05-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (なし)
- **要約:** Dun & Bradstreetの1万企業グローバル調査: 97%がAI活動を実施、56%が今後12ヶ月でAI投資増加予定、30%がAIを本番稼働にスケール、26%がパイロット段階。
- **キーファクト:**
  - 10,000企業グローバル調査
  - 97%がAI活動を実施中
  - 56%が今後12ヶ月でAI投資増加
  - 30%が本番稼働にスケール
  - 26%がパイロット段階
- **引用URL:** https://www.morningstar.com/news/pr-newswire/20260504fl50726/dun-bradstreet-global-survey-of-10000-businesses-finds-ai-impact-at-an-inflection-point
- **Evidence ID:** EVD-20260510-0050

### INFO-051
- **タイトル:** 88% of AI agents fail to reach production
- **ソース:** Instagram / LinkedIn / Gartner
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** (なし)
- **要約:** 組織が構築・デプロイを試みたAIエージェントの88%が本番に到達できず。Gartner予測: 2026年末までにエンタープライズアプリの40%がAIエージェント統合（2025年の5%未満から）。Snowflake/Omdia調査: AI早期導入者の92%がポジティブROIを報告。
- **キーファクト:**
  - AIエージェント本番到達率: 12%（88%が失敗）
  - Gartner: 2026年末にエンタープライズアプリ40%がAIエージェント統合
  - Snowflake/Omdia: AI早期導入者の92%がポジティブROI
  - 75%のC-level非技術組織が正のROI報告
- **引用URL:** https://www.snowflake.com/en/lp/radical-roi-generative-ai-short-form/
- **Evidence ID:** EVD-20260510-0051

### INFO-052
- **タイトル:** Klarna CEO cut workforce 40%, AI handles 700 support roles
- **ソース:** LinkedIn / The CS Café
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna
- **要約:** Klarna CEO Sebastian Siemiatkowskiが従業員を約40%削減（7400→3400）。AIアシスタントが700のサポート役割に相当する業務を処理。Duolingoが「AI-first」を宣言。1日882のテック職が消失中。
- **キーファクト:**
  - Klarna: 従業員40%削減（7400→3400）
  - AIアシスタントが700サポート役相当を処理
  - Duolingo: 「AI-first」宣言、AI中心のワークフロー再構築指示
  - テック職消失: 1日882件のペース
  - AIが2ヶ月連続でレイオフの最大理由
- **引用URL:** https://www.thecscafe.com/p/cs-org-defense-ai-headcount-review
- **Evidence ID:** EVD-20260510-0052

### INFO-053
- **タイトル:** AI Could Wipe Out Entry-Level Jobs, And That Should Terrify Business Leaders
- **ソース:** Forbes
- **公開日:** 2026-05-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-02
- **関連企業:** (なし)
- **要約:** AIがマーケティング・ファイナンス・法務・ソフトウェア開発・カスタマーサービスのジュニア職を急速に再形成。イェール専門家: 「AIによる実際の雇用破壊はキャリアが始まる前に起きている」。全体的な失業率は歴史的低水準だが、入門職が構造的に消滅。
- **キーファクト:**
  - AIが入門職（マーケティング・法務・CS・コーディング等）を急速に再形成
  - イェール: 「実際の雇用破壊はキャリア開始前に発生」
  - 全体失業率は低いが、入門職が構造的に消滅
  - シニア人材のパイプライン消失リスク
- **引用URL:** https://www.forbes.com/sites/bernardmarr/2026/05/04/ai-could-wipe-out-entry-level-jobs-and-that-should-terrify-business-leaders/
- **Evidence ID:** EVD-20260510-0053

### INFO-054
- **タイトル:** Google confirms 800% AI agent revenue growth, $462B backlog
- **ソース:** CX Today
- **公開日:** 2026-05-10
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-02, H-GOO-001
- **関連企業:** Google
- **要約:** AlphabetがエンタープライズAIエージェント収益の前年比800%成長を確認。$4620億バックログ。パイロットから本格的コミットメントへの移行を示すシグナル。
- **キーファクト:**
  - エンタープライズAIエージェント収益: 前年比800%成長
  - $4620億クラウドバックログ
  - パイロット→本格コミットメントへの移行
  - Google Cloud全体63%成長の主要牽引要因
- **引用URL:** https://www.cxtoday.com/contact-center/google-confirms-800-ai-agent-revenue-growth/
- **Evidence ID:** EVD-20260510-0054

### INFO-055
- **タイトル:** Freshworks lays off 11% as AI changes software sector
- **ソース:** Facebook / Forbes
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-04
- **関連企業:** Freshworks
- **要約:** Freshworksが従業員の約11%をレイオフ。ソフトウェア部門におけるAI変化への対応が理由。SaaS企業のAI適応リストラクチャリング事例。
- **キーファクト:**
  - Freshworks: 11%人員削減
  - ソフトウェア部門のAI変化が理由
  - SaaS企業のAI適応リストラ事例
- **引用URL:** https://www.facebook.com/womeplat/posts/freshworks-announced-plans-to-lay-off-about-11-of-its-workforce-as-the-company-a/1601502501982836/
- **Evidence ID:** EVD-20260510-0055

### INFO-056
- **タイトル:** AI agent business automation advertising operations
- **ソース:** MediaPost / mi-3.com.au
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** (なし)
- **要約:** AI技術が広告業界の背景ツールから中央OSに移行。AIエージェントがマーケティングスタックに流入。勝者は「マシンの再設計」をする企業。広告キャンペーンのほぼ全工程をAIが処理。
- **キーファクト:**
  - AIが広告業界の背景ツール→中央OSに移行
  - AIエージェントがマーケティングスタックに大量流入
  - 勝者は「マシンの再設計」をする企業
  - 広告キャンペーンのほぼ全工程をAIが処理可能に
- **引用URL:** https://www.mediapost.com/publications/article/414719/when-ai-becomes-tech-running-the-ad-industry.html
- **Evidence ID:** EVD-20260510-0056

### INFO-057
- **タイトル:** Microsoft WorkLab: culture and management account for 67% of AI impact
- **ソース:** Microsoft WorkLab
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** Microsoft
- **要約:** Microsoft WorkLab調査: AIの実際のインパクトの67%は組織要因（文化・マネージャー支援・タレントプラクティス）、個人マインドセット・行動は32%。エージェント導入で人間のエージェンシーが拡大。
- **キーファクト:**
  - AIインパクトの67%は組織要因（文化・管理・タレント）
  - 個人マインドセット・行動は32%
  - エージェント導入で人間のエージェンシーが拡大
  - 組織がAIの恩恵を捉える構造の必要性
- **引用URL:** https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
- **Evidence ID:** EVD-20260510-0057

### INFO-058
- **タイトル:** Retail industry sleepwalking into disintermediation
- **ソース:** LinkedIn
- **公開日:** 2026-05-10
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** (なし)
- **要約:** 小売業がAmazon以来「最も暴力的な非媒介化イベント」に向かっている。Google AI Modeがホテル予約を直接処理、OTA（オンライン旅行代理店）をバイパス。プラットフォーマーのAI統合が中間業者のバリューチェーンを侵食。
- **キーファクト:**
  - 小売業が「Amazon以来最も暴力的な非媒介化イベント」に直面
  - Google AI Mode: ホテル予約を直接処理、OTAをバイパス
  - プラットフォーマーAIが中間業者のバリューチェーンを侵食
- **引用URL:** https://www.linkedin.com/posts/shalvi-singh_most-retailers-will-lose-the-agent-war-and-activity-7456867265569968128-j94s
- **Evidence ID:** EVD-20260510-0058

### INFO-059
- **タイトル:** LLM API Pricing 2026: GPT-4-level capability from $30/M to under $1/M
- **ソース:** LLM Stats / BenchLM / DevTK
- **公開日:** 2026-05-10
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, Google, DeepSeek
- **要約:** GPT-4レベルの能力が2023年初頭の$30/百万トークンから現在$1未満に低下。競争とモデル効率化が牽引。OpenAI Codex料金をメッセージ単位→トークン単位に変更（4月）。GPT-5.5 Batch/Flex: $2.50/$15。Anthropicは200K超トークン2倍プレミアムを3月に撤廃。DeepSeek V3は$0.27/$1.10。
- **キーファクト:**
  - GPT-4レベル能力: $30/M（2023年初）→ <$1/M（現在）、30倍以上の価格低下
  - GPT-5.5 Batch/Flex: $2.50/$15 per M tokens（標準$5/$30から50%オフ）
  - Anthropic: 200K超トークン2倍プレミアム撤廃（3月）
  - DeepSeek V3: $0.27/$1.10、最安値水準
  - Gemini 2.5 Flash: $0.15/$0.60
- **引用URL:** https://llm-stats.com/ai-trends
- **Evidence ID:** EVD-20260510-0059

### INFO-060
- **タイトル:** State of LLM Benchmarks 2026: Open-weight models close gap
- **ソース:** BenchLM / Frontier Benchmarks
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** (なし)
- **要約:** オープンウェイトモデルが台頭。DeepSeek V4 Pro、Kimi K2.6、GLM-5/5.1が比較対象に。Claude Mythos PreviewがSWE-Bench Proで77.8%。ベンチマークと実運用の乖離が指摘される。
- **キーファクト:**
  - DeepSeek V4 Pro (Max)、Kimi K2.6、GLM-5/5.1がフロンティア比較に参入
  - Claude Mythos Preview: SWE-Bench Pro 77.8%（1位）
  - Gemini 3 Pro Preview: MMLU-Pro 89.8%（RAG最適）
  - ベンチマーク性能とデプロイ性能の乖離が議論
  - Llama 4 Scout: 2,600 tok/sでフロンティア最速
- **引用URL:** https://benchlm.ai/blog/posts/state-of-llm-benchmarks-2026
- **Evidence ID:** EVD-20260510-0060

### INFO-061
- **タイトル:** ARC-AGI-3: no frontier model exceeds 1%
- **ソース:** The Decoder / Reddit / Epoch AI
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** (なし)
- **要約:** ARC-AGI-3が2026年3月25日にv3アップデート（Seed IQ評価向け）。フロンティアモデル全てが1%未満。GPT-5.5含む最新モデルも3つの体系的推論エラー。ベンチマーク飽和と新規指標の必要性が議論。
- **キーファクト:**
  - ARC-AGI-3 v3: 2026年3月25日Y Combinatorでローンチ
  - Seed IQ（ByteDance）評価向けに更新
  - フロンティアモデル全て1%未満
  - 3つの体系的推論エラーを特定
  - クラシック推論ベンチマークの限界（飽和傾向）
- **引用URL:** https://the-decoder.com/even-the-latest-ai-models-make-three-systematic-reasoning-errors-arc-agi-3-analysis-shows/
- **Evidence ID:** EVD-20260510-0061

### INFO-062
- **タイトル:** Meta acquires ARI Robotics for humanoid AI ambitions
- **ソース:** Neura Market / Thelec.net
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Meta
- **要約:** MetaがAssured Robot Intelligence（ARI）を買収。ヒューマノイドロボティクス強化。ARI共同創業者がMeta Superintelligence Labsに参加。
- **キーファクト:**
  - MetaがARI買収
  - ヒューマノイドロボティクスAI強化
  - ARI共同創業者がSuperintelligence Labsに参加
  - Google-Boston Dynamicsと競合構造
- **引用URL:** https://www.neura.market/news/meta-acquires-ari-humanoid-robotics-ambitions
- **Evidence ID:** EVD-20260510-0062

### INFO-063
- **タイトル:** SpaceX eyes $60B Cursor acquisition ahead of IPO
- **ソース:** LinkedIn / Business Standard
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, KIQ-001-01
- **関連企業:** SpaceX, Cursor/Anysphere
- **要約:** SpaceXがCursor（Anysphere）の$600億買収オプションを確保。次世代「コーディング・ナレッジワークAI」の共同開発。Cursorは18ヶ月で$20億ARR、マーケティング費用ゼロで急成長。
- **キーファクト:**
  - SpaceX: Cursor買収オプション（$600億評価）
  - 次世代コーディング・ナレッジワークAI共同開発
  - Cursor: 18ヶ月で$20億ARR（マーケティング費用ゼロ）
  - 12ヶ月で$1億ARR到達（Slack 2.5年、Dropbox 4年と比較）
- **引用URL:** https://www.business-standard.com/technology/tech-news/elon-musk-cursor-anysphere-deal-ai-last-mile-control-explained-126050701267_1.html
- **Evidence ID:** EVD-20260510-0063

### INFO-064
- **タイトル:** OpenAI-Microsoft partnership amendment ends Azure exclusivity
- **ソース:** Fifth Row
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05, KIQ-002-01
- **関連企業:** OpenAI, Microsoft
- **要約:** OpenAI-Microsoft提携修正によりAzure排他性が終了。エンタープライズのマルチクラウドAI調達が可能に。コンプライアンスとコスト削減の新たな選択肢。マルチクラウドAI戦略がデフォルトに。
- **キーファクト:**
  - OpenAI-Microsoft提携修正: Azure排他性終了
  - エンタープライズのマルチクラウドAI調達が可能に
  - コンプライアンス・コスト削減の選択肢拡大
  - マルチクラウドAI戦略がデフォルト（例外ではなく）に
- **引用URL:** https://www.fifthrow.com/blog/from-lock-in-to-leverage-how-the-open-ai-microsoft-partnership-amendment-redefines-enterprise-multi-cloud-ai-procurement-in-2026
- **Evidence ID:** EVD-20260510-0064

### INFO-065
- **タイトル:** GitHub Copilot 4.7M paid subscribers, moving to usage-based billing
- **ソース:** Medium / Instagram / GitHub Community
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02, KIQ-001-01
- **関連企業:** Microsoft / GitHub
- **要約:** GitHub Copilotが470万有料サブスクライバー、42%市場シェア、Fortune 100の90%で利用。コードの46%を生成。使用量ベース課金に移行中。
- **キーファクト:**
  - GitHub Copilot: 470万有料サブスクライバー、75% YoY成長
  - 42%市場シェア
  - Fortune 100の90%で利用、コードの46%を生成
  - 使用量ベース課金に移行
- **引用URL:** https://medium.com/@krupeshraut/openai-and-anthropic-are-buying-the-tools-every-developer-uses-heres-why-you-should-care-e52006bc4707
- **Evidence ID:** EVD-20260510-0065

### INFO-066
- **タイトル:** Junior developer jobs down 50% since 2019, AI-exposed roles decline faster
- **ソース:** TechRadar / Linux Foundation / Metaintro
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02, H-CAR-002
- **関連企業:** (なし)
- **要約:** テック職求人が2019年比50%減、ジュニア職が最も打撃。Stanford研究: 22-25歳プログラマー雇用約20%減。AI導入企業では入門職採用の低下が7.7%速い。ジュニア職削減がAI人材不足を深刻化させる悪循環。
- **キーファクト:**
  - テック職求人: 2019年比50%減
  - Stanford: 22-25歳プログラマー雇用約20%減（2022年比）
  - AI導入企業: 入門職採用低下が7.7%速い
  - ジュニア職削減 → 将来のシニア人材パイプライン消失リスク
  - Linux Foundation: ジュニアエンジニアがAIスーパーチャージの中心
- **引用URL:** https://www.techradar.com/pro/why-cutting-junior-jobs-is-quietly-deepening-techs-ai-skills-shortage
- **Evidence ID:** EVD-20260510-0066

### INFO-067
- **タイトル:** AGI timeline predictions: Musk end 2026, Hassabis ~2030
- **ソース:** Medium Predict / Instagram / Cosmos Institute
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** (なし)
- **要約:** Musk: AGI by end 2026。Hassabis: 「5年以内に非常に良いチャンス」、~2030でアーキテクチャ50/50不確実性。HassabisはLLMだけではAGIに到達しないという中間的立場。Dario Amodeiはホワイトカラー職へのAI警告継続。
- **キーファクト:**
  - Musk: AGI by end 2026
  - Hassabis: 「5年以内にAGIの非常に良いチャンス」
  - Hassabis: LLMは正しい方向へのステップだが、純スケーリングだけでは不十分
  - Amodei: ホワイトカラー職へのAI警告継続
  - NYT: 「AI Populism Is Here. And No One Is Ready.」
- **引用URL:** https://medium.com/predict/deepminds-ceo-proposed-the-most-honest-agi-test-anyone-has-suggested-and-he-says-today-s-systems-45e23f18b57c
- **Evidence ID:** EVD-20260510-0067

### INFO-068
- **タイトル:** US to safety test new AI models from Google, Microsoft, xAI
- **ソース:** BBC / R Street Institute / The Hill
- **公開日:** 2026-05-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** Google, Microsoft, xAI
- **要約:** テック企業が商務省のCAISI（AI標準・イノベーションセンター）を通じたモデル安全性テストに自主的に参加。米中AI安全対話の再開。EU、AI規則の緩和で暫定合意。
- **キーファクト:**
  - Google、Microsoft、xAIがAIモデル安全性テストに自主参加
  - 商務省CAISI経由で実施
  - 米中AI安全対話再開
  - EU: AI規則緩和の暫定合意
  - Bernie Sanders: AIの生存リスク警告、米中協力呼びかけ
- **引用URL:** https://www.bbc.com/news/articles/cgjp2we2j8go
- **Evidence ID:** EVD-20260510-0068

### INFO-069
- **タイトル:** Mythos restarting US-China AI safety dialogue
- **ソース:** Geopolitechs
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** AnthropicのMythos公開が米中AI安全対話を再起する可能性。中国の観察者は米国の政治的コミットメントの持続性に深い懐疑的。大統領の意向が本当にAI安全協力を望んでいても、行政の交代で覆るリスク。
- **キーファクト:**
  - Mythosが米中AI安全対話再開の契機に
  - 中国側: 米国の政治的コミットメント持続性に深い懐疑
  - 政権交代でAI安全協力が覆るリスク
  - 対話の価値はあるが、合意署名は慎重べきとの指摘
- **引用URL:** https://www.geopolitechs.org/p/is-mythos-restarting-us-china-ai
- **Evidence ID:** EVD-20260510-0069

### INFO-070
- **タイトル:** 字节跳动AI资本支出2026年超2000亿元，国产芯片侧重
- **ソース:** 南华早报 / 新浪财经 / ZAKER
- **公開日:** 2026-05-09
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** ByteDanceが2026年AIインフラ支出を2000億元超（約$300億）に引き上げ。昨年末計画1600億元から25%増。より多くを国内AIチップに投資。2025年のAI関連支出は900億元。
- **キーファクト:**
  - 2026年AI資本支出: 2000億元超（約$300億）、前年計画比+25%
  - より多くの資金を国内AIチップに投資
  - 2025年AI関連支出: 約900億元
  - 2025年総資本支出1500億元、AI算力関連が過半
- **引用URL:** https://www.myzaker.com/article/69ff2ded1bc8e05873000006
- **Evidence ID:** EVD-20260510-0070

### INFO-071
- **タイトル:** 豆包3.45亿用户开始付费：68/200/500元三档
- **ソース:** 澎湃新闻 / 新京报 / 亿欧
- **公開日:** 2026-05-09
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-BTD-PRICE
- **関連企業:** ByteDance
- **要約:** 豆包（Doubao）が3.45億ユーザーを抱え、3段階有料プランをApp Storeで公開。標準版68元/月、加強版200元/月、専門版500元/月。Seedance 2.0動画生成が豆包に全面統合。中国大モデル「無料時代」の終了。
- **キーファクト:**
  - 豆包: 3.45億ユーザー
  - 有料プラン: 68/200/500元/月（3段階）
  - Seedance 2.0動画生成が全面統合
  - 梁汝波CEO: 豆包を「AI助手で既存業務統合」に位置づけ
  - 中国大モデル「無料時代」の終了シグナル
- **引用URL:** https://www.bjnews.com.cn/detail/1778131853129431.html
- **Evidence ID:** EVD-20260510-0071

### INFO-072
- **タイトル:** Coze 2.5版リリース：AI Agent从工具到伙伴的跨越
- **ソース:** CSDN / Tencent Cloud
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceの智能体平台Coze（扣子）が2.5版をリリース（2026年4月7日）。AI Agentが「工具」から「伙伴」へ進化。PPT制作、動画生成等のオフィス機能も追加。有料機能も導入。
- **キーファクト:**
  - Coze 2.5版: AI Agentが「工具」→「伙伴」に進化
  - PPT制作・動画生成等のオフィス機能追加
  - 有料機能導入
  - OpenClawの影響を受けた設計
- **引用URL:** https://gitcode.csdn.net/69f5fc130a2f6a37c5a7782d.html
- **Evidence ID:** EVD-20260510-0072

### INFO-073
- **タイトル:** Mistral Remote Vibe coding agents + Magistral release
- **ソース:** DevOps.com / LinkedIn / Facebook
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral AI
- **要約:** MistralがRemote Vibeエージェント（Medium 3.5搭載）をクラウドで提供。非同期でローカルマシンを占有しない。Magistral Small（24B、オープンソース）とMagistral Medium（エンタープライズ向け）をリリース。シンガポールHTXと提携。
- **キーファクト:**
  - Remote Vibe: クラウドベースのコーディングエージェント（非同期・ローカル非占有）
  - Magistral Small: 24Bパラメータ、オープンソース
  - Magistral Medium: エンタープライズ向け
  - シンガポールHTXと提携拡大
- **引用URL:** https://devops.com/mistral-moves-coding-agents-to-the-cloud-and-gets-out-of-your-way/
- **Evidence ID:** EVD-20260510-0073

### INFO-074
- **タイトル:** OpenAI $25B annualized revenue, Forbes AI 50
- **ソース:** Forbes / CNBC
- **公開日:** 2026-05-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIの年間収益化収益が$250億超。AIバブル懸念: DeepL、Picsart CEOがAI評価額への懸念を表明。「Vibe revenue」の指摘。AI株は年初の記録高評価額から下落、ミドルモーニングスターは「数年来の最良バリュー」と評価。
- **キーファクト:**
  - OpenAI: $250億超の年間収益化収益
  - DeepL・Picsart CEO: AI評価額への懸念表明
  - 「Vibe revenue」: AI企業のバブル懸念
  - AI株: 年初高値から下落、一部アナリストは「割安」評価
- **引用URL:** https://www.forbes.com/lists/ai50/
- **Evidence ID:** EVD-20260510-0074

### INFO-075
- **タイトル:** The List Price Is Lying: AI costs decoupled from pricing
- **ソース:** FairMind AI
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** (なし)
- **要約:** 3つのAIベンダーが異なるメカニズムでコスト構造を変更。リスト価格が実際のコストの弱い代理指標に。モデルスイッチングコストは技術的・運用的努力を意味するが、実際の課金は表示価格と乖離。
- **キーファクト:**
  - 3つのAIベンダーが異なるコスト構造変更を実施
  - リスト価格が実際のコストの弱い代理指標に
  - Batch/Flex/Priority等の価格ティアが複雑化
  - エンタープライズのAI支出管理が難化
- **引用URL:** https://www.fairmind.ai/en/blog/ai-costs-decoupled-from-pricing
- **Evidence ID:** EVD-20260510-0075

### INFO-076
- **タイトル:** AI-proof skills: problem definition and human collaboration value rising
- **ソース:** Forbes / Fast Company / Yale Insights
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** (なし)
- **要約:** AI代替が困難な能力（課題定義・対人関係・異領域統合）の市場価値が上昇中。入門職削減でも、AIを柔軟に使う若手は有利。新職種（AI creative director、AI strategist）の emergence。91%のエンタープライズがAIコーディングツールを本番利用。
- **キーファクト:**
  - 課題定義・対人関係・異領域統合の市場価値上昇
  - 新職種 emergence: AI creative director, AI strategist
  - 若手はAI利用に柔軟、シニアは慎重という逆説
  - 91%のエンタープライズがAIコーディングツールを本番利用
- **引用URL:** https://www.fastcompany.com/91521334/ai-is-wiping-out-entry-level-jobs-7-tips-to-ride-the-wave-instead-of-getting-knocked-down-by-it-ai-technology-entry-level-jobs
- **Evidence ID:** EVD-20260510-0076

### INFO-077
- **タイトル:** Paul Tudor Jones says US is late to regulating AI
- **ソース:** CNBC
- **公開日:** 2026-05-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** (なし)
- **要約:** ビリオネアヘッジファンドマネージャーPaul Tudor JonesがCNBCで米国のAI規制の遅れを警告。ディープフェイク識別のためのウォーターマーク導入の必要性を強調。
- **キーファクト:**
  - Paul Tudor Jones: 米国のAI規制遅れを警告
  - ディープフェイク識別用ウォーターマークの必要性
  - 米国の規制対応が遅れているとの認識
- **引用URL:** https://www.cnbc.com/2026/05/07/paul-tudor-jones-ai-regulation-warning.html
- **Evidence ID:** EVD-20260510-0077

### INFO-078
- **タイトル:** IREN inks AI infrastructure deal with Nvidia
- **ソース:** CNBC
- **公開日:** 2026-05-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** NVIDIA, IREN
- **要約:** IRENがNVIDIAとAIインフラ契約を締結。AIデータセンターインフラの拡大継続。
- **キーファクト:**
  - IREN-NVIDIA AIインフラ契約締結
  - AIデータセンターインフラ拡大の一環
- **引用URL:** https://www.cnbc.com/2026/05/07/iren-stock-ai-infrastructure-nvidia.html
- **Evidence ID:** EVD-20260510-0078

### INFO-079
- **タイトル:** State of global AI diffusion in 2026 - Microsoft
- **ソース:** Microsoft Blog
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** Microsoft
- **要約:** 2026年第1四半期にAI使用率が1.5ポイント上昇。MicrosoftのグローバルAI拡散状況レポート。
- **キーファクト:**
  - 2026 Q1: AI使用率+1.5ポイント上昇
  - グローバルAI拡散状況の定量分析
- **引用URL:** https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/
- **Evidence ID:** EVD-20260510-0079

### INFO-080
- **タイトル:** Google's AI deal with Pentagon sparks employee backlash
- **ソース:** Fortune / Washington Post
- **公開日:** 2026-05-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, H-GOV-001
- **関連企業:** Google / DeepMind
- **要約:** GoogleのPentagon AI契約が従業員の反発を引き起こし、数百人が公開書簡で反対。2018年Project Maven時より従業員の交渉力は低下。Anthropicのみが拒否し、Pentagonが同社を「サプライチェーンリスク」指定。
- **キーファクト:**
  - Google-Pentagon AI契約: 数百人の従業員が公開書簡で反対
  - 2018年Project Maven時より従業員の交渉力低下
  - AnthropicのみがPentagon契約を拒否
  - Anthropic → 「サプライチェーンリスク」指定の結果
- **引用URL:** https://fortune.com/2026/05/04/google-employee-backlash-pentagon-ai-contract-power-waned-since-project-maven/
- **Evidence ID:** EVD-20260510-0080

### INFO-081
- **タイトル:** 中国Kimi、阶跃星辰融资$45亿、大模型融资狂潮
- **ソース:** 21财经
- **公開日:** 2026-05-09
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** Moonshot AI (Kimi), 阶跃星辰
- **要約:** 中国大モデル企業Kimi（月之暗面）と阶跃星辰が24時間で計$45億の資金調達。OpenAIがスマートフォン開発加速、字节跳动もAI手机を戦略級入口と位置づけ。中兴と豆包チームが共同AI手机リリース済み。
- **キーファクト:**
  - Kimi + 阶跃星辰: 24時間で$45億調達
  - OpenAI: AIエージェントスマートフォン開発加速
  - 字节跳动: AI手机を戦略級入口と位置づけ
  - 中兴×豆包: AI搭载スマートフォン共同リリース済み
- **引用URL:** https://www.21jingji.com/article/20260509/herald/ce4be394a318585b01a018ead752bff3.html
- **Evidence ID:** EVD-20260510-0081

### INFO-082
- **タイトル:** Anthropic Claude Code auto mode: InfoQ detailed report
- **ソース:** InfoQ
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-AGENT-001
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Codeにオートモードを導入。マルチステップのソフトウェア開発ワークフローを手動介入なしで実行可能に。
- **キーファクト:**
  - Claude Code auto mode: マルチステップ開発自律実行
  - 手動介入を削減
  - 開発生産性向上が期待
- **引用URL:** https://www.infoq.com/news/2026/05/anthropic-claude-code-auto-mode/
- **Evidence ID:** EVD-20260510-0082

### INFO-083
- **タイトル:** Anthropic Institute: AI for Science program launch
- **ソース:** Anthropic公式
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** AnthropicがAI for Science Programを開始。Anthropic Instituteのアジェンダとして、ソフトウェアエンジニアリングの急激な変化を観察。
- **キーファクト:**
  - AI for Science Program開始
  - ソフトウェアエンジニアリングの急激な変化を内部で観察
  - Anthropic Instituteの研究アジェンダ
- **引用URL:** https://www.anthropic.com/news/ai-for-science-program
- **Evidence ID:** EVD-20260510-0083

### INFO-084
- **タイトル:** Anthropic enterprise AI services company with Blackstone, H&F, Goldman Sachs
- **ソース:** Anthropic公式ブログ（関連コンテンツ）
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-001-02
- **関連企業:** Anthropic, Blackstone, Goldman Sachs
- **要約:** AnthropicがBlackstone、Hellman & Friedman、Goldman Sachsと新エンタープライズAIサービス会社を設立。金融業界向けエンタープライズAIの本格展開。
- **キーファクト:**
  - Blackstone + H&F + Goldman Sachs + Anthropic の合弁
  - エンタープライズAIサービス会社設立
  - 金融業界向け特化
- **引用URL:** https://www.anthropic.com/news/enterprise-ai-services-company
- **Evidence ID:** EVD-20260510-0084

### INFO-085
- **タイトル:** Anthropic covering electricity price increases from data centers
- **ソース:** Anthropic公式（関連コンテンツ）
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Anthropicが米国内のデータセンターによる消費者電力料金上昇をカバーするコミットメント。国際展開でも同様のコミットメント拡大を検討。
- **キーファクト:**
  - 米国データセンターによる消費者電力値上げをAnthropicがカバー
  - 国際展開でも同様コミットメント検討
  - コミュニティ投資との両立
- **引用URL:** https://www.anthropic.com/news/covering-electricity-price-increases
- **Evidence ID:** EVD-20260510-0085

### INFO-086
- **タイトル:** Two-thirds of top SaaS companies won't survive the AI age
- **ソース:** Business Insider / Forbes / Bain
- **公開日:** 2026-05-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** (なし)
- **要約:** アナリストが「上位SaaS企業の3分の2はAI時代を生き残れない」と予測。Bain: Agentic AIの最大機会はSaaSの代替ではなく、調整作業の自動化で労働コストをソフトウェア支出に転換（$1000億機会）。「SaaSpocalypse」の指摘。
- **キーファクト:**
  - 上位SaaS企業の3分の2がAI時代に生き残れない予測
  - Bain: $1000億のクロスシステム労働自動化機会
  - AIはSaaSを代替するのではなく増幅するという見方も
  - SaaS企業は評価額低下と巨額債務の間に挟まる構造
- **引用URL:** https://www.businessinsider.com/ai-challenges-saas-giants-analyst-survive-twilio-atlassian-navan-2026-5
- **Evidence ID:** EVD-20260510-0086

### INFO-087
- **タイトル:** AI Overviews decrease Google Ads CTR from 19.7% to 6.34%
- **ソース:** Search Influence / Instagram
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google, Meta
- **要約:** Google AI Overviewsが表示されると有料広告CTRが19.7%→6.34%に低下。マーケティング代理店がクライアントを失い、ブランドが内製AIシステムに移行。Meta Ads管理が週40時間→4時間に自動化。
- **キーファクト:**
  - Google AI Overviews: 有料広告CTR 19.7%→6.34%に低下
  - ゼロクリック検索の常態化
  - マーケティング代理店: クライアントが内製AIに移行
  - Meta Ads管理: 週40時間→4時間に自動化、ROAS 40-60%改善
- **引用URL:** https://www.searchinfluence.com/blog/how-ai-search-affects-paid-ads-performance-strategy-2026/
- **Evidence ID:** EVD-20260510-0087

### INFO-088
- **タイトル:** CyberAgent Q1 2026: advancing AI in advertising, full automation goal
- **ソース:** Alpha Spread / Dev.to
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgentがQ1 2026決算で広告AIの推進を報告。動画広告制作の完全自動化を目指す。自社日本語LLM開発、AI Operations Office設立。レイヤーL2/L3（エージェント・業務システム）に注力。
- **キーファクト:**
  - 広告動画制作の完全自動化を目指す
  - 自社日本語LLM開発継続
  - AI Operations Office設立
  - レイヤーL2/L3（エージェント・業務システム）注力
- **引用URL:** https://www.alphaspread.com/de/security/tse/4751/investor-relations/earnings-call/q1-2026
- **Evidence ID:** EVD-20260510-0088

### INFO-089
- **タイトル:** Pentagon blacklisting of Anthropic called unconstitutional by federal judge
- **ソース:** Boston Globe / Instagram / Cambridge Forum
- **公開日:** 2026-05-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, H-GOV-001, H-ANT-001
- **関連企業:** Anthropic, Pentagon, US Government
- **要約:** 連邦判事がPentagonのAnthropicブラックリスト指定を「違憲の可能性」と評価。「政府は調達法をAI企業への政策不一致の強制に使えない」。Boston Globe: トランプの「自己取引軍産複合体」。HegsethがPentagon調達法の強制適用を脅しに使用。
- **キーファクト:**
  - 連邦判事: PentagonのAnthropicブラックリスト指定は「違憲の可能性」
  - 「政府は調達法をAI企業への政策不一致の強制に使えない」
  - Hegseth: Pentagon調達法の強制適用を脅しに使用
  - Boston Globe: 「自己取引軍産複合体」批判
- **引用URL:** https://www.bostonglobe.com/2026/05/06/opinion/donald-trump-palantir-military-contracts/
- **Evidence ID:** EVD-20260510-0089

### INFO-090
- **タイトル:** Microsoft, Google, xAI to give US government early access to AI models
- **ソース:** Reuters / Federal News Network
- **公開日:** 2026-05-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** Microsoft, Google, xAI
- **要約:** Microsoft、Google、xAIが米政府にAIモデルの早期アクセスを国家安全保障テスト用に提供することに合意。商務省のCAISI経由。ホワイトハウスがAIセキュリティ大統領令を検討中。
- **キーファクト:**
  - Microsoft/Google/xAI: 新AIモデルの早期アクセスを米政府に提供
  - 国家安全保障テスト向け
  - 商務省CAISI経由で実施
  - ホワイトハウス: AIセキュリティ大統領令を検討中
- **引用URL:** https://www.reuters.com/legal/litigation/microsoft-xai-google-will-share-ai-models-with-us-govt-security-reviews-2026-05-05/
- **Evidence ID:** EVD-20260510-0090

### INFO-091
- **タイトル:** Q1 2026: $300B global VC investment, AI accounts for 80%
- **ソース:** AI Funding Tracker / Crunchbase
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** (なし)
- **要約:** 2026年第1四半期のグローバルベンチャー投資は$3000億（過去最高、Crunchbase調べ）。AIが$2420億で全体の80%を占める。6000スタートアップが資金調達。
- **キーファクト:**
  - Q1 2026グローバルVC投資: $3000億（過去最高）
  - AI投資: $2420億（全体の80%）
  - 6000スタートアップが資金調達
  - AI投資がVC全体を牽引する構造
- **引用URL:** https://aifundingtracker.com/ai-startup-funding-news-today/
- **Evidence ID:** EVD-20260510-0091

### INFO-092
- **タイトル:** Recursive self-improvement edges closer in AI labs - IEEE Spectrum
- **ソース:** IEEE Spectrum / TechRadar
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic
- **要約:** 再帰的自己改善がAIラボで現実味を帯びる。AIシステムがコードを書き、チップを設計、研究を洗練。ただし主要部分は依然として人間管理。Anthropic共同創業者: 「いつかAIが自らのより良い版を構築する」と予測。チップ・電力・冷却の物理的制約が上限。
- **キーファクト:**
  - 再帰的自己改善がAIラボで実現に近づく
  - コード記述・チップ設計・研究洗練を自律実行
  - 主要部分は依然として人間管理
  - 物理的制約（チップ・電力・冷却）が自己改善速度の上限
- **引用URL:** https://spectrum.ieee.org/recursive-self-improvement
- **Evidence ID:** EVD-20260510-0092

### INFO-093
- **タイトル:** AGI-26 conference: top researchers debate future of AI
- **ソース:** MSN / RAND / Singularity Journey
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** (なし)
- **要約:** AGI SocietyがAGI-26（第19回年次会議）の基調講演者を発表。AGIの定義について「幅広い認知タスクを人間レベル以上で実行するシステム」という方向性で概ね一致。ただしスケーリング vs 新アプローチの議論は継続。
- **キーファクト:**
  - AGI-26: 第19回年次会議のキーノート発表
  - AGI定義: 推論・問題解決・状況適応を自律実行するシステム
  - スケーリング vs 新アプローチの議論継続
  - 安全性・人間監視の必要性で概ね一致
- **引用URL:** https://www.msn.com/en-us/news/technology/agi-26-brings-top-researchers-together-to-debate-future-of-ai/ar-AA22BDHt
- **Evidence ID:** EVD-20260510-0093

### INFO-094
- **タイトル:** Doubao-Seed-2.0-lite upgraded: full multimodal understanding
- **ソース:** 火山引擎开发者社区
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** Doubao-Seed-2.0-liteが新バージョンにアップグレード。豆包大模型家族初の全模態理解モデル。動画・画像・音声・テキストのネイティブ統一理解をサポート。Agent・Coding・GUI能力も同期アップグレード。同等算力で性能向上。
- **キーファクト:**
  - Doubao-Seed-2.0-lite: 全模態理解モデルにアップグレード
  - 動画・画像・音声・テキストのネイティブ統一理解
  - Agent・Coding・GUI能力も同期アップグレード
  - 同等算力で性能向上
- **引用URL:** https://developer.volcengine.com/articles/7636596381943070763
- **Evidence ID:** EVD-20260510-0094

### INFO-095
- **タイトル:** ByteDance Seed3D 2.0: 3D生成SOTA達成
- **ソース:** Threads / 火山引擎
- **公開日:** 2026-04-23
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceがSeed3D 2.0を2026年4月23日にリリース。画像1枚から高精度3Dモデルを数秒で生成。3D生成分野でSOTA達成。材質・光影・複雑形状に対応。3D素材のモデリングが不要になる可能性。
- **キーファクト:**
  - Seed3D 2.0: 画像1枚→高精度3Dモデル（数秒）
  - 3D生成分野SOTA達成
  - 材質・光影・複雑形状に対応
  - 従来の3Dモデリングが不要になる可能性
- **引用URL:** https://developer.volcengine.com/articles/7636596381943070763
- **Evidence ID:** EVD-20260510-0095


## X (Twitter) 投稿データ（ローカルRSSHub経由）

### INFO-096
- **タイトル:** @gdb (Greg Brockman) のX投稿
- **ソース:** X (Twitter) - @gdb (共同創業者)
- **公開日:** 2026-05-10
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** GPT-Realtime-2 for instantly translating audio in realtime

CHOI: I just added real-time AI translation into Chormex using GPT-Realtime-2… and this feels absolutely surreal.

It works across YouTube videos, live streams, meetings, presentations, basically anywhere audio is playing inside Chrome.

You can watch translated speech in real time
- **引用URL:** https://x.com/gdb/status/2053134883040514350

### INFO-097
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** Here’s how you can integrate GPT-Realtime-2 to bring voice control to a CRM workflow.
- **引用URL:** https://x.com/OpenAIDevs/status/2053161503470366881

### INFO-098
- **タイトル:** @sama (Sam Altman) のX投稿
- **ソース:** X (Twitter) - @sama (CEO)
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** kicking off a bunch of codex tasks, running around with my kid in the sunshine, and then coming back at naptime to find them all completed makes me very optimistic for the future
- **引用URL:** https://x.com/sama/status/2053191344999604409

### INFO-099
- **タイトル:** @jasonkwon (Jason Kwon) のX投稿
- **ソース:** X (Twitter) - @jasonkwon (戦略担当)
- **公開日:** 2026-05-10
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Sam Altman
5.5 is an autistic genius with very strange taste in naming

shocking that we would make such a thing
- **引用URL:** https://x.com/jasonkwon/status/2053201817862119698

### INFO-100
- **タイトル:** @gdb (Greg Brockman) のX投稿
- **ソース:** X (Twitter) - @gdb (共同創業者)
- **公開日:** 2026-05-10
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** Codex for expenses

Vaibhav (VB) Srivastav: Codex quite literally filed my reimbursements, downloaded invoices since the start of the month, updated the expenses spreadsheet and filled the actual form all by itself

Used Drive & Sheets plugin for state tracking
Gmail plugin for tracking invoices
Chrome extension for actual
- **引用URL:** https://x.com/gdb/status/2053221403868922114

### INFO-101
- **タイトル:** @kevinweil (Kevin Weil) のX投稿
- **ソース:** X (Twitter) - @kevinweil (製品責任者)
- **公開日:** 2026-05-10
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Shae McLaughlin
It’s estimated that the Protein Data Bank (PDB) cost around $13B to create. Alphafold was only possible because of it. If we want ML to solve biology, we should be funding the creation of databases and the development of new assay technologies. ML is nothing without data.
- **引用URL:** https://x.com/kevinweil/status/2053214758401437744

### INFO-102
- **タイトル:** @kevinweil (Kevin Weil) のX投稿
- **ソース:** X (Twitter) - @kevinweil (製品責任者)
- **公開日:** 2026-05-10
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** This a matter of extreme importance (and some of the best writing ever) https://www.theatlantic.com/magazine/2026/05/best-free-restaurant-bread-america/686582/?gift=OqVfOH3ElmhyC4FAR8f2MaTorngzDqk8QQbmUcBF3Wk&utm_source=copy-link&utm_medium=social&utm_campaign=share
- **引用URL:** https://x.com/kevinweil/status/2053225351946682733

