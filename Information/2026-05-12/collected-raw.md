# 収集データ: 2026-05-12

## メタデータ
- 収集日時: 2026-05-12 00:00 UTC
- 品質フラグ: COLLECTING
- 動的追加クエリ（Arbiter優先KIQに基づく）:
  - KIQ-AGENT-001 Claude Code WAU/MAU: 3クエリ
  - H-XAI-005 SpaceXAI新仮説: 3クエリ
  - Pentagon除外理由: 3クエリ
  - KIQ-BTD-PRICE DeepSeek API価格: 3クエリ
  - 800%収益成長基数 Google Cloud AI: 3クエリ
  - Pattern I 自律化vs孤立化: 3クエリ

## 収集結果

### INFO-001
- **タイトル:** OpenAI launches the OpenAI Deployment Company (DeployCo)
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01, KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIが新会社「OpenAI Deployment Company (DeployCo)」を設立。Tomoro（約150名のFDEを擁する適用AIコンサルティング企業）の買収を発表。TPG主導、Advent/Bain Capital/Brookfield共同主導で$40億以上の初期投資。McKinsey & CompanyやBain & Companyなど19社のパートナー参加。
- **キーファクト:**
  - DeployCoはOpenAIが過半数所有・支配、単一顧客体験を提供
  - Tomoro買収でTesco/Virgin Atlantic/Supercell等のエンタープライズ導入経験を獲得
  - 19の投資・コンサル・システムインテグレーターパートナー（TPG, Advent, Bain Capital, Brookfield, McKinsey等）
  - FDE（Forward Deployed Engineers）を顧客組織に常駐させるビジネスモデル
  - Denise Dresser CROが「AIは組織内でますます意味のある作業が可能になっている」とコメント
- **引用URL:** https://openai.com/index/openai-launches-the-deployment-company/
- **Evidence ID:** EVD-20260512-0001

### INFO-002
- **タイトル:** Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.5-Cyberを限定プレビューで提供開始。Trusted Access for Cyber (TAC)はID・信頼ベースのフレームワークで、検証済みディフェンダーにセキュリティワークフロー向けの緩和された安全ガードを提供。Cisco/Intel/SentinelOne/Snyk等がパートナー。
- **キーファクト:**
  - 3段階アクセスレベル: GPT-5.5(デフォルト) → GPT-5.5+TAC → GPT-5.5-Cyber
  - GPT-5.5-Cyberは認可されたレッドチーミング・ペネトレーションテスト向け
  - 2026年6月1日からAdvanced Account Security（フィッシング耐性認証）が必須化
  - Codex Securityプラグインで脅威モデリング→脆弱性発見→修正まで自動化
  - αテストでGPT-5.5-Cyberが重大脆弱性の自動レッドチーミングに使用済み
- **引用URL:** https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/
- **Evidence ID:** EVD-20260512-0002

### INFO-003
- **タイトル:** Introducing Trusted Contact in ChatGPT
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPTに「Trusted Contact」安全機能をロールアウト。成人ユーザーが信頼する人物を登録でき、自傷リスクが検出された場合に通知。170名以上のメンタルヘルス専門家と協力、APAのガイダンスに基づき設計。
- **キーファクト:**
  - 人間レビュアーによる審査（1時間以内のレビュー目標）
  - チャット詳細は通知に含まず（プライバシー保護）
  - American Psychological Association等の臨床家・研究者と共同開発
  - 既存の親コントロール安全通知を18歳以上に拡張
- **引用URL:** https://openai.com/index/introducing-trusted-contact-in-chatgpt/
- **Evidence ID:** EVD-20260512-0003

### INFO-004
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropic LabsがClaude Designを発表。Claude Opus 4.7搭載のビジュアルデザインツール。プロトタイプ/スライド/ワンペーパー等を作成。Canva統合、Claude Codeへの直接ハンドオフ機能付き。Pro/Max/Team/Enterprise向け。
- **キーファクト:**
  - Opus 4.7（最も能力の高いビジョンモデル）搭載
  - オンボーディング時にコードベース/デザインファイルからデザインシステムを自動構築
  - Canva/PDF/PPTX/HTMLエクスポート対応
  - Claude Codeへの直接ハンドオフ（設計→実装のシームレス移行）
  - Databricks/Brilliant/Datadogが初期採用
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260512-0004

### INFO-005
- **タイトル:** 5 new ways to explore the web with generative AI in Search
- **ソース:** Google Official Blog
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-002-05
- **関連企業:** Google
- **要約:** GoogleがAI ModeとAI Overviewsの5つの新機能を発表。ニュースサブスクリプション統合、コミュニティパースペクティブ、インラインリンク改善、ウェブサイトプレビュー機能等を追加。
- **キーファクト:**
  - ニュースサブスクリプションリンクをAI検索結果内にハイライト表示
  - SNS/フォーラムのパースペクティブをAI回答に統合
  - インラインリンク改善（関連テキスト横に直接リンク配置）
  - ホバープレビューでリンク先サイト情報を事前表示
  - query fan-out技術で関連サイトを深掘り
- **引用URL:** https://blog.google/products-and-platforms/products/search/explore-web-generative-ai-search/
- **Evidence ID:** EVD-20260512-0005

### INFO-006
- **タイトル:** Google Threat Intelligence Group reports on AI-powered threats - first AI-developed zero-day exploit identified
- **ソース:** Google Official Blog / Google Cloud Threat Intelligence
- **公開日:** 2026-05-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** Google
- **要約:** Google Threat Intelligence Group (GTIG)がAIで開発されたゼロデイエクスプロイトを初めて特定。攻撃者はAIを使用して脆弱性を発見・悪用。GoogleはBig SleepやCodeMender等のAI防御エージェントで対抗。
- **キーファクト:**
  - GTIGがAIで開発されたと判断されるゼロデイエクスプロイトを初検出
  - 攻撃者は大規模攻撃を計画していたが、Googleのプロアクティブな対抗発見で阻止の可能性
  - Big Sleep（脆弱性検出AIエージェント）とCodeMender（自動修正AIエージェント）が稼働
  - 敵対的ワークフローへの生成AIの産業規模適用への移行が進行中
- **引用URL:** https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-threat-intelligence-group-report/
- **Evidence ID:** EVD-20260512-0006

### INFO-007
- **タイトル:** Introducing Claude Sonnet 4.6
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 4.6はコーディング・コンピューター使用・長文脈推論・エージェント計画・デザインの全面改良。1Mトークンコンテキストウィンドウ（ベータ）。Claude Codeユーザーの70%がSonnet 4.5よりSonnet 4.6を好む。Opus 4.5より59%の確率で優先される。価格はSonnet 4.5と同じ$3/$15 per M tokens。
- **キーファクト:**
  - OSWorldベンチマークでSonnet 4.5から大幅改善（コンピューター使用）
  - SWE-bench Verified約80%、Humanity's Last Exam高分
  - Vending-Bench Arenaで長期戦略的投資↔収益ピボット戦略を自律的に開発
  - Databricks/Replit/Cursor/GitHub/Cognition/Windsurf/Hebbia等が称賛
  - 無料プランのデフォルトモデルに昇格（ファイル作成・コネクタ・スキル・コンパクション付き）
  - Excel統合でMCPコネクタ対応（S&P Global/LSEG/PitchBook/Moody's等）
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6
- **Evidence ID:** EVD-20260512-0007
