# 収集データ: 2026-06-13

## メタデータ
- 収集日時: 2026-06-13 01:30 UTC
- 実行クエリ数: 83 / ~113
- scrape実行数: 9件
- 収集情報数: 74件
- Evidence ID 採番範囲: EVD-20260613-0001 〜 EVD-20260613-0074
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓, KIQ-ANT-SAFETY ✓, KIQ-GOO-001 ✓
- 品質フラグ: NORMAL

## Arbiter動的追加クエリ
- KIQ-ANT-SAFETY: エンタープライズ顧客のClaude選択理由定量調査（H-ANT-001上限条件用）
- KIQ-GOO-001: AWS/Azure同時期Cloud成長率比較データ（H-GOO-001復帰条件用）

## 収集結果

### INFO-001
- **タイトル:** Claude Fable 5 and Claude Mythos 5 — Anthropic公式発表
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-003-01, KIQ-003-02, KIQ-005-01
- **関連企業:** Anthropic
- **要約:** AnthropicがMythos-classモデルClaude Fable 5（一般向け・セーフガード付き）とClaude Mythos 5（Glasswingパートナー向け・セーフガード解除）を同時発表。Fable 5はほぼ全ベンチマークでSOTA達成。価格は$10/M入力・$50/M出力（Mythos Previewの半額以下）。安全上の理由からサイバーセキュリティ・バイオ・化学・蒸留関連クエリはClaude Opus 4.8にフォールバックする設計。
- **キーファクト:**
  - Fable 5はSWE-bench・FrontierCode等でSOTA。Stripeが5000万行Rubyコードベースの移行を1日で完了（従来2ヶ月以上）
  - 定価$10/M入力・$50/M出力。Mythos Previewの半額以下
  - セーフガードとして独自分類器（classifier）を導入。5%未満のセッションでフォールバック発動
  - Mythos 5はProject Glasswing経由で政府・インフラプロバイダーに提供。生物学研究向けtrusted access programも計画
  - 新しい30日間データ保持ポリシー（安全性監視目的・モデル訓練には不使用）
  - 14社（Cursor・GitHub・Thomson Reuters・IMC等）が早期テストで好評価
- **引用URL:** https://www.anthropic.com/news/claude-fable-5-mythos-5
- **Evidence ID:** EVD-20260613-0001

### INFO-002
- **タイトル:** Results from the first Anthropic Public Record — 52,000米国人AI意識調査
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-04, KIQ-004-01, KIQ-004-03, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Anthropicが52,000人の米国人を対象とした初回「Anthropic Public Record」調査結果を発表。AI失業不安が64%で最大の懸念。政府のAI規制介入への支持は超党派で71%。AI企業への信頼はわずか15%で最低。
- **キーファクト:**
  - 64%がAIによる失業を懸念（党派・地域を問わず一貫）
  - 認知依存不安56%、誤情報52%が続く
  - 政府AI規制支持71%（民主党79%・共和党68%・無党派69%）
  - AI企業を信頼すると回答したのはわずか15%（連邦政府20%より低い）
  - AI日常使用者は非使用者より失業不安が16ポイント低い（54% vs 70%）
  - 学歴が高いほど失業不安が高い（大学院卒vs高卒で10ポイント差）
- **引用URL:** https://www.anthropic.com/news/anthropic-public-record
- **Evidence ID:** EVD-20260613-0002

### INFO-003
- **タイトル:** Claude Enterprise Guide 2026 — エンタープライズ展開トレーニングガイド
- **ソース:** IntuitionLabs
- **公開日:** 2026-06-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-ANT-SAFETY, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Enterpriseの展開ガイド。Deloitte等の顧客が「trusted AI」をClaude選択理由として挙げている。セキュリティファースト設計・SOC2準拠を強調。
- **キーファクト:**
  - Deloitteが「trusted AI」をClaude選択理由として引用
  - Claude Enterpriseは厳格なデータ分離設計
  - エンタープライズ展開向けの包括的トレーニングガイド提供
- **引用URL:** https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026
- **Evidence ID:** EVD-20260613-0003

### INFO-004
- **タイトル:** Microsoft Restricts Employee Access to Claude Fable 5 — データ保持ポリシー懸念
- **ソース:** Instagram（ニュース投稿）
- **公開日:** 2026-06-12
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-001-05
- **関連企業:** Anthropic, Microsoft
- **要約:** Anthropicの新データ保持ポリシー（全プロンプト30日間保持・フラグ付きコンテンツ最大2年）によりMicrosoftが従業員のClaude Fable 5アクセスを制限。法的レビューを実施中。
- **キーファクト:**
  - Anthropic新データ保持ポリシーが企業顧客に影響
  - Microsoftが従業員のFable 5アクセスを法的レビュー中に制限
  - エンタープライズセキュリティ・コンプライアンス対応の新たな課題
- **引用URL:** https://www.instagram.com/p/DZcfJ0un-kd/
- **Evidence ID:** EVD-20260613-0004

### INFO-005
- **タイトル:** Claude Fable 5: API, Benchmarks, Pricing & How to Use It — TrueFoundry解説
- **ソース:** TrueFoundry
- **公開日:** 2026-06-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** Fable 5のAPI詳細・ベンチマーク・価格解説。Anthropicと早期顧客はFable 5が少ないターン・トークンでタスクを完了すると報告。2x単価でも実質コストは近い可能性。
- **キーファクト:**
  - Fable 5定価$10/M入力・$50/M出力
  - 少ないターン・トークンで同等タスク完了→実質コストは見かけより低い
  - ベンチマークでSOTA達成の詳細
- **引用URL:** https://www.truefoundry.com/blog/claude-fable-5-api-benchmarks-pricing-how-to-use-it
- **Evidence ID:** EVD-20260613-0005

### INFO-006
- **タイトル:** Anthropic AI Statistics 2026 — ユーザー・収益・市場シェア
- **ソース:** Panto AI
- **公開日:** 2026-06-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, KIQ-ANT-SAFETY
- **関連企業:** Anthropic
- **要約:** Claude Codeのランレート収益が2026年2月に$25億超え。Anthropicは30万以上の組織にサービス提供。API・企業向け製品が急成長中。
- **キーファクト:**
  - Claude Code ランレート収益: 2025年9月$5億→2026年2月$25億超
  - 30万以上の組織がClaude使用中
  - Anthropic評価額$965B（前回報道）
- **引用URL:** https://www.getpanto.ai/blog/anthropic-ai-statistics
- **Evidence ID:** EVD-20260613-0006

### INFO-007
- **タイトル:** AWS vs Google Cloud vs Azure — 2026年パフォーマンス比較
- **ソース:** Trantor
- **公開日:** 2026-06-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-GOO-001, KIQ-002-01
- **関連企業:** Google, Microsoft, Amazon
- **要約:** 2026年のマルチクラウド採用率が89%に到達（2024年比13ポイント上昇）。三大クラウドプロバイダーのAI統合比較。AWS・Azure・GCPそれぞれのAI Agent・LLM統合状況を分析。
- **キーファクト:**
  - マルチクラウド採用率89%（2024年の76%から上昇）
  - 各プロバイダーのAIサービス比較詳細あり
  - AI Agent統合がクラウド選択の新たな差別化要因に
- **引用URL:** https://www.trantorinc.com/blog/aws-vs-google-cloud-vs-azure
- **Evidence ID:** EVD-20260613-0007

### INFO-008
- **タイトル:** Oracle's Record FY2026 Results — クラウド成長の新たな競争者
- **ソース:** LinkedIn
- **公開日:** 2026-06-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-GOO-001, KIQ-002-01
- **関連企業:** Oracle, Google, Microsoft, Amazon
- **要約:** Oracle FY2026年間売上$674億（+17%）。クラウド売上$340億（+39%）。IaaS成長77%。AIインフラ需要が急成長牽引。AWS/Azure/GCPとの相対比較に重要なデータポイント。
- **キーファクト:**
  - Oracle年間総売上$674億（+17% YoY）
  - クラウド売上$340億（+39% YoY）
  - IaaS成長77% — AIインフラ需要急増の反映
  - バックログが記録的水準に
- **引用URL:** https://www.linkedin.com/pulse/oracles-record-fy2026-results-backlog-rewrites-cloud-vigoroso-mba-ctkhf
- **Evidence ID:** EVD-20260613-0008

### INFO-009
- **タイトル:** AI Agent Security: Protect Data & Prevent Breaches in 2026
- **ソース:** Improvado
- **公開日:** 2026-06-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-001-01
- **関連企業:** （一般）
- **要約:** エンタープライズの72%がAIエージェントのパイロット・展開中だが、本番環境で堅牢なセキュリティ統制を運用しているのは31%に留まる。AIエージェントセキュリティの課題と対策を詳細分析。
- **キーファクト:**
  - エンタープライズ72%がAIエージェント導入中
  - 堅牢なセキュリティ統制の本番運用は31%のみ
  - AIエージェント特有の攻撃ベクトル・対策フレームワークの解説
- **引用URL:** https://improvado.io/blog/ai-agent-security
- **Evidence ID:** EVD-20260613-0009

### INFO-010
- **タイトル:** Coze Free API (2026) — ByteDance AIプラットフォーム無料アクセス
- **ソース:** Free-LLM
- **公開日:** 2026-06-01
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのAIプラットフォームCozeが無料APIアクセスを提供。AIチャットボット・エージェント構築デプロイを可能にする。
- **キーファクト:**
  - Cozeが無料APIアクセス提供（2026年6月時点）
  - AIチャットボット・エージェントの構築・デプロイ対応
  - ByteDanceのグローバルAI展開の一環
- **引用URL:** https://free-llm.com/provider/coze
- **Evidence ID:** EVD-20260613-0010

### INFO-011
- **タイトル:** Agentic AI Adoption Trends Among Fortune 500 Enterprises in 2026
- **ソース:** VertexPlus
- **公開日:** 2026-06-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** （一般）
- **要約:** Fortune 500企業の80%がAgentic AI導入中。Walmart・JPMorgan等の事例。実装戦略・ユースケース・ROI分析を含む包括的調査。
- **キーファクト:**
  - Fortune 500の80%がAgentic AI導入に着手
  - Walmart・JPMorgan等が先進事例として紹介
  - エンタープライズ向け実装戦略の詳細分析あり
- **引用URL:** https://www.vertexplus.com/blog/agentic-ai-adoption-trends-among-fortune-500-enterprises-in-2026
- **Evidence ID:** EVD-20260613-0011

### INFO-012
- **タイトル:** Who's Adopting AI Agents — Harvard Business School分析
- **ソース:** Harvard Business School
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （一般）
- **要約:** 何億ものユーザーインタラクションの分析に基づき、ナレッジワーカーがAgentic AIの最ヘビーユーザーであることを特定。
- **キーファクト:**
  - ナレッジワーカーがAgentic AIの最ヘビーユーザー層
  - 何億ものユーザーインタラクションを分析
  - AI Agent採用の実際のパターンを定量的に提示
- **引用URL:** https://www.library.hbs.edu/working-knowledge/whos-adopting-ai-agents-and-what-theyre-actually-doing-with-them
- **Evidence ID:** EVD-20260613-0012

### INFO-013
- **タイトル:** ChatGPT Enterprise: Admin Controls & Security Settings
- **ソース:** IntuitionLabs
- **公開日:** 2026-06-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI
- **要約:** ChatGPT EnterpriseのGlobal Admin Console（2025年後半発表）が複数ワークスペースの集中管理を可能に。SOC2・FedRAMP対応の詳細。
- **キーファクト:**
  - Global Admin Consoleで複数ワークスペース一元管理
  - SOC2・FedRAMP準拠のセキュリティ基盤
  - エンタープライズ向けガバナンス機能の拡充
- **引用URL:** https://intuitionlabs.ai/articles/chatgpt-enterprise-admin-controls-security
- **Evidence ID:** EVD-20260613-0013

### INFO-014
- **タイトル:** Mastercard launches Agent Pay for Machines — AIエージェント決済
- **ソース:** Mastercard
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Mastercard, OpenAI
- **要約:** Mastercardが「Agent Pay for Machines」を発表。AIエージェントによる自律的決済を実現。Agentic Commerceの新しいインフラ。
- **キーファクト:**
  - AIエージェント向け決済インフラ「Agent Pay for Machines」発表
  - 機械間自律取引を可能にする新機能
  - Agentic Commerce基盤の構築
- **引用URL:** https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
- **Evidence ID:** EVD-20260613-0014

### INFO-015
- **タイトル:** Visa and OpenAI: Building the future of AI commerce
- **ソース:** Visa
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Visa
- **要約:** VisaがVisa Payments ForumでOpenAIとの戦略的提携を発表。Agentic Commerceをメインストリームに持っていく狙い。
- **キーファクト:**
  - VisaとOpenAIの戦略的提携発表
  - Agentic Commerceのメインストリーム化が目的
  - Visa Payments Forum (San Francisco)で発表
- **引用URL:** https://corporate.visa.com/en/sites/visa-perspectives/innovation/visa-openai-partnership.html
- **Evidence ID:** EVD-20260613-0015

### INFO-016
- **タイトル:** MCP Specification Release Candidate発表 — エンタープライズ採用加速
- **ソース:** MCP Blog
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** （標準化団体）
- **要約:** Model Context Protocol (MCP)仕様のRelease Candidateが発表。ステートレスプロトコルコア・Extensions framework・Tasks・MCP Apps・認可ハードニングを含む。
- **キーファクト:**
  - MCP仕様のRC版発表
  - ステートレスプロトコルコア・Extensions・Tasks・MCP Appsを含む
  - 認可セキュリティのハードニング
  - エンタープライズ採用に向けた標準化の重要マイルストーン
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260613-0016

### INFO-017
- **タイトル:** Six Months of Open: Agentic AI Foundation (AAIF) の振り返り
- **ソース:** LinkedIn (AAIF)
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** （標準化団体）
- **要約:** AAIF設立6ヶ月の振り返り。オープンAgenticスタックの標準化を推進。MCP等の重要インフラの中立的管理機関としての役割。
- **キーファクト:**
  - AAIF設立6ヶ月の活動振り返り
  - オープンAgenticスタックの標準化推進
  - MCP等のインフラの中立的管理を担当
  - Linux Foundation配下としての運営
- **引用URL:** https://www.linkedin.com/pulse/six-months-open-reflections-agentic-ai-foundations-mazin-hp3ec
- **Evidence ID:** EVD-20260613-0017

### INFO-018
- **タイトル:** LangChain: Best AI Agent Frameworks in 2026 — 7フレームワーク比較
- **ソース:** LangChain
- **公開日:** 2026-06-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-001-01
- **関連企業:** LangChain, Microsoft
- **要約:** LangGraph・CrewAI・Microsoft Agent Framework等7つのAI Agentフレームワークをオーケストレーション・観測可能性・本番対応度で比較レビュー。
- **キーファクト:**
  - LangGraph・CrewAI・Microsoft Agent Framework等7製品を比較
  - オーケストレーション・観測可能性・本番対応度の3軸で評価
  - AI Agent開発エコシステムの成熟度を示す包括的レビュー
- **引用URL:** https://www.langchain.com/resources/ai-agent-frameworks
- **Evidence ID:** EVD-20260613-0018

### INFO-019
- **タイトル:** AI Agent Development Cost in 2026 — 市場予測$182.97B by 2033
- **ソース:** SoftTeco (Grand View Research引用)
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** （一般）
- **要約:** Grand View Research予測: AI Agent市場は2033年までに$1,829.7億に到達。2026年からの年間成長率49.6%。
- **キーファクト:**
  - AI Agent市場規模予測: 2033年までに$1,829.7億
  - 年間成長率49.6%（2026年〜2033年）
  - 開発コストの詳細分析あり
- **引用URL:** https://softteco.com/blog/ai-agent-development-cost
- **Evidence ID:** EVD-20260613-0019

### INFO-020
- **タイトル:** OpenAI Skills実行環境 — AWS Bedrock AgentCore上のセキュアサンドボックス
- **ソース:** AWS Blog
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-01
- **関連企業:** OpenAI, Amazon
- **要約:** AWS Bedrock AgentCoreでコーディングエージェントをホスト。専用Linux microVM・永続ワークスペース・リアルシェル・決定的コマンド実行を提供。40以上のモジュール型Skillsとサンドボックス実行環境。
- **キーファクト:**
  - AWS Bedrock AgentCoreでコーディングエージェントのセキュアホスティング
  - 専用Linux microVM・永続ワークスペース提供
  - 40以上のモジュール型Skills対応
  - サンドボックス実行環境によるセキュリティ確保
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/
- **Evidence ID:** EVD-20260613-0020

### INFO-021
- **タイトル:** Google Gemini Skills — API/SDK向けスキルリポジトリ
- **ソース:** GitHub (google-gemini)
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Google
- **要約:** Google Gemini API向けの公式Skillsリポジトリ。エージェントにコンテキストを追加する軽量テクニック。Gemini CLIのSubagent機能と連携。
- **キーファクト:**
  - Google公式Gemini Skillsリポジトリ公開
  - エージェントへのコンテキスト追加を軽量に実現
  - Gemini CLI Subagent機能との連携
  - Agent Gatewayによるセキュリティ・ガバナンス管理
- **引用URL:** https://github.com/google-gemini/gemini-skills
- **Evidence ID:** EVD-20260613-0021

### INFO-022
- **タイトル:** Detecting and Understanding Malicious Agent Skills in the Wild — arXiv論文
- **ソース:** arXiv
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-001-02
- **関連企業:** （学術）
- **要約:** Agent Skillsのセキュリティリスクを分析する学術論文。SKILL.md（YAML frontmatter付き）と補助コード（Python/Shell/JS）からなるファイルベースパッケージの悪意あるスキル検出手法を提案。
- **キーファクト:**
  - Agent Skillsのセキュリティリスクに関する学術分析
  - SKILL.md + 補助コード構成のパッケージが攻撃対象に
  - 悪意あるスキルの検出・理解手法を提案
- **引用URL:** https://arxiv.org/html/2602.06547v4
- **Evidence ID:** EVD-20260613-0022

### INFO-023
- **タイトル:** LLM Leaderboard 2026 — Top AI Models Benchmark Comparison
- **ソース:** Vellum
- **公開日:** 2026-06-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-001-04
- **関連企業:** （一般）
- **要約:** 2026年6月時点のLLMベンチマークリーダーボード。SOTAモデルの公開ベンチマークパフォーマンスを比較表示。
- **キーファクト:**
  - 2024年4月以降リリースのSOTAモデルを対象
  - 各モデルプロバイダーの公式データに基づく
  - ベンチマークパフォーマンスの一覧比較
- **引用URL:** https://www.vellum.ai/llm-leaderboard
- **Evidence ID:** EVD-20260613-0023

### INFO-024
- **タイトル:** Claude Code実行環境ガバナンス — TrueFoundry解説
- **ソース:** TrueFoundry
- **公開日:** 2026-06-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** エンタープライズ規模でClaude Codeを安全に展開するための6つの制御層ガイド。SSO・セキュリティ・ガバナンスの包括的解説。
- **キーファクト:**
  - エンタープライズ向けClaude Code展開の6制御層
  - SSO・セキュリティ統合の詳細ガイド
  - プラットフォームエンジニアリング・セキュリティチーム向け
- **引用URL:** https://www.truefoundry.com/blog/claude-enterprise-security
- **Evidence ID:** EVD-20260613-0024

### INFO-025
- **タイトル:** Claude AI Enterprise Security — SOC2 Type II・HIPAA対応
- **ソース:** Strac.io
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-ANT-SAFETY
- **関連企業:** Anthropic
- **要約:** AnthropicはSOC 2 Type II認証を保持。EnterpriseプランでHIPAA BAA利用可能。ClaudeインフラはAWS・GCP上で稼働。FortinetがClaude Compliance APIとの統合を発表。
- **キーファクト:**
  - Anthropic SOC 2 Type II認証保持
  - EnterpriseプランでHIPAA BAA利用可能
  - インフラはAWS・GCP上で稼働
  - FortinetがClaude Compliance APIと統合
- **引用URL:** https://www.strac.io/blog/is-claude-ai-safe
- **Evidence ID:** EVD-20260613-0025

### INFO-026
- **タイトル:** Trump memo on AI aims to avoid repeat of Anthropic debacle — Breaking Defense
- **ソース:** Breaking Defense
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, OpenAI, Google, Microsoft
- **要約:** National Security Presidential Memorandum (NSPM-11)がAI企業との緊密な協力を促進する一方、ペンタゴンの要求に応じない企業への対応を示唆。Anthropic事件の「再発防止」が狙い。
- **キーファクト:**
  - NSPM-11はAI企業との協力促進を指示
  - ペンタゴン要求に非協力な企業への契約打ち切り条項あり
  - Anthropic事件の「再発防止」が明示的な目的
  - OpenAI・Google・Microsoft等はPentagon契約に既に参加
- **引用URL:** https://breakingdefense.com/2026/06/trump-memo-on-ai-aims-to-avoid-repeat-of-anthropic-debacle/
- **Evidence ID:** EVD-20260613-0026

### INFO-027
- **タイトル:** Trump administration denies unlawful retaliation in Anthropic AI blacklisting
- **ソース:** The Daily Record
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** トランプ政権がAnthropic AIブラックリスト入りにおける違法な報復を否定。PentagonがAnthropicにサプライチェーンリスク指定を適用し、連邦政府全体での技術使用を制限。
- **キーファクト:**
  - PentagonがAnthropicに正式なサプライチェーンリスク指定
  - 連邦政府全体でAnthropic技術の段階的排除を命令
  - トランプ政権は「報復」を否定
  - AnthropicのPentagon契約拒否が発端
- **引用URL:** https://thedailyrecord.com/2026/06/09/trump-administration-denies-anthropic-ai-blacklisting-retaliation/
- **Evidence ID:** EVD-20260613-0027

### INFO-028
- **タイトル:** Pentagon Drops Anthropic Claude Over Safety Rules — AI Weekly
- **ソース:** AI Weekly
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Pentagonが安全性ルールを理由にAnthropic Claudeを除外。Amodeiは除外範囲がPentagon直接契約のみで全連邦機関ではないと確認。Pentagon CTOは「生産的な対話はない」と否定。
- **キーファクト:**
  - Pentagonが安全性要件を理由にClaude契約を打ち切り
  - 除外はPentagon直接契約のみ（全連邦機関ではない）
  - Pentagon CTOはAnthropicとの建設的対話を否定
  - 安全性堅持vs政府要求の構造的対立
- **引用URL:** https://aiweekly.co/alerts/pentagon-drops-anthropic-claude-over-safety-rules
- **Evidence ID:** EVD-20260613-0028

### INFO-029
- **タイトル:** Anthropic Versus the Pentagon — Who Determines How Advanced AI Systems Are Deployed?
- **ソース:** International Banker
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 連邦控訴裁がAnthropicのサプライチェーンリスク指定に対する一時的差止請求を却下。AI展開の決定権を巡る政府対企業の構造的対立を分析。
- **キーファクト:**
  - DC連邦控訴裁がAnthropicの一時差止請求を却下
  - サプライチェーンリスク指定の法的有効性が確認
  - AI展開の決定権を巡る根本的な対立構造
  - 企業の安全性判断vs政府の安全保障要件
- **引用URL:** https://internationalbanker.com/technology/anthropic-versus-the-pentagon-who-determines-how-advanced-ai-systems-are-deployed/
- **Evidence ID:** EVD-20260613-0029

### INFO-030
- **タイトル:** NSPM-11's Anthropic Exception: The NSA's Claude Mythos Carve-Out
- **ソース:** TechJack Solutions
- **公開日:** 2026-06-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** NSPM-11におけるAnthropic例外条項の分析。NSAがClaude Mythosへの特別アクセスを持つ。軍事・国家安全保障利用制限条項を含むAI契約は現在リスクとなる。
- **キーファクト:**
  - NSPM-11にAnthropicに関する例外条項が存在
  - NSAがClaude Mythosへの特別アクセスを確保
  - 軍事利用制限条項を含むAI契約がリスクに
  - 政府契約における企業側制約の無効化前例
- **引用URL:** https://techjacksolutions.com/ai-brief/nspm-11s-anthropic-exception-the-nsas-claude-mythos-carve-ou/
- **Evidence ID:** EVD-20260613-0030

### INFO-031
- **タイトル:** New IBM Study: CIOs and CTOs Face Growing AI Control Gap
- **ソース:** IBM Newsroom
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** IBM
- **要約:** IBM調査: 2027年までにAIエージェント展開数が38%増加見込。CEO主導のAI変革マンドレートが80%。しかしITリーダーの87%が「実際の導入はまだ進んでいない」と回答。
- **キーファクト:**
  - 2027年までにAIエージェント展開数38%増加予測
  - CEO主導AI変革マンドレート80%
  - ITリーダーの87%が「実際の導入はまだ進んでいない」
  - AI Control Gap（統制格差）が拡大中
- **引用URL:** https://newsroom.ibm.com/2026-06-08-new-ibm-study-finds-cios-and-ctos-face-growing-ai-control-gap-as-enterprise-deployment-scales
- **Evidence ID:** EVD-20260613-0031

### INFO-032
- **タイトル:** AI agents are flattening corporate hierarchies — Fortune
- **ソース:** Fortune
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** （一般）
- **要約:** Korn Ferry調査: 企業の41%が昨年管理層を削減。AIエージェントが組織階層をフラット化。マネージャー向けの新しいプレイブックが必要に。
- **キーファクト:**
  - 従業員の41%が自社で管理層削減があったと回答
  - AIエージェントが組織階層のフラット化を推進
  - マネージャー役割の再定義が必要
  - 中間管理職のAI代替が進行中
- **引用URL:** https://fortune.com/2026/06/09/ai-agents-flattening-corporate-hierarchies-companies-managers-develop-new-playbook/
- **Evidence ID:** EVD-20260613-0032

### INFO-033
- **タイトル:** Gartner 2026 Hype Cycle: 17%の組織のみAIエージェント展開済み
- **ソース:** Portal26 (Gartner引用)
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** （一般）
- **要約:** Gartner 2026 Agentic AI Hype Cycle: 現在AIエージェントを展開している組織は17%に過ぎないが、60%以上が今後導入予定。コスト管理の課題。
- **キーファクト:**
  - 現在AIエージェント展開済みの組織は17%のみ
  - 60%以上が今後導入予定
  - AI Agent コスト管理が急務
  - 期待と実態のギャップ
- **引用URL:** https://portal26.ai/ai-agent-cost-control-stop-agents-burning-budget/
- **Evidence ID:** EVD-20260613-0033

### INFO-034
- **タイトル:** White House Executive Order on Advanced AI Innovation and Security (Jun 2, 2026)
- **ソース:** Global Policy Watch
- **公開日:** 2026-06-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** （政府）
- **要約:** ホワイトハウスが「先進AIイノベーション・セキュリティ促進」大統領令を発令（2026年6月2日）。NSPM-11と連動する包括的AI政策。
- **キーファクト:**
  - 2026年6月2日付で先進AI大統領令発令
  - イノベーション促進とセキュリティ強化の二本柱
  - NSPM-11と連動する包括的政策
  - 政府のAI活用加速を明記
- **引用URL:** https://www.globalpolicywatch.com/2026/06/white-house-releases-executive-order-on-advanced-ai-innovation-and-security/
- **Evidence ID:** EVD-20260613-0034

### INFO-035
- **タイトル:** Amazon Bedrock: Six months of security and governance updates
- **ソース:** Scale Factory
- **公開日:** 2026-06-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** Amazon Bedrockの過去6ヶ月のセキュリティ・ガバナンス更新まとめ。AgentCore Policy・Evaluationsが2026年3月にGA到達。Agent Registry（2026年4月）発表。
- **キーファクト:**
  - AgentCore Policy・Evaluationsが2026年3月GA到達
  - Agent Registry（2026年4月発表）でエージェント管理強化
  - 6ヶ月間でセキュリティ・ガバナンス機能を大幅拡充
- **引用URL:** https://scalefactory.com/amazon-bedrock-six-months-of-security-and-governance-updates-worth-knowing-about/
- **Evidence ID:** EVD-20260613-0035

### INFO-036
- **タイトル:** EU AI Act reloaded — 最新変更の実務的影響
- **ソース:** Stibbe
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** （規制）
- **要約:** EU AI Actの最新改正が実務に与える影響の分析。製品安全法とAI Actの関係の大幅簡素化。GPAIプロバイダーは世界売上3%または1,500万ユーロの罰金リスク。
- **キーファクト:**
  - EU製品安全法とAI Actの関係が大幅に簡素化
  - GPAIプロバイダー: 世界売上3%または1,500万ユーロの罰金リスク
  - AI Act執行に独立専門家が支援
  - 2026年期限後のスタートアップへの影響も分析
- **引用URL:** https://www.stibbe.com/publications-and-insights/ai-act-reloaded-what-the-latest-ai-act-changes-mean-in-practice
- **Evidence ID:** EVD-20260613-0036

### INFO-037
- **タイトル:** Google's Backstops Underpin $35 Billion Chip Deal for Anthropic — Bloomberg
- **ソース:** Bloomberg
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, Google
- **要約:** GoogleがAnthropicの各拠点でのリース支払いを裏当てし、実質$350億のローン調達を支援。GoogleのAnthropicへの投資リターンが前四半期に押し上げられた。
- **キーファクト:**
  - GoogleがAnthropic向け$350億チップ取引の裏当て提供
  - 実質的に$350億ローンに相当
  - 各拠点でのリース支払い保証
  - Google投資リターンにプラス寄与
- **引用URL:** https://www.bloomberg.com/news/articles/2026-06-09/google-s-backstops-underpin-35-billion-chip-deal-for-anthropic
- **Evidence ID:** EVD-20260613-0037

### INFO-038
- **タイトル:** OpenAI plans stock market debut, setting up new race with Anthropic — BBC
- **ソース:** BBC
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIが株式市場デビューを計画、Anthropicとの新たな競争激化。Anthropicは今年上半期に黒字化を目指すと投資家に伝達。Claude売上・関連サービスが急成長。
- **キーファクト:**
  - OpenAIが上場を計画、AnthropicとのIPO競争開始
  - Anthropicは今年上半期黒字化見通しを投資家に伝達
  - Claude売上・関連サービス急成長中
  - 両社の上場競争がAI業界の構造変化をもたらす可能性
- **引用URL:** https://www.bbc.com/news/articles/cd958eqg1n5o
- **Evidence ID:** EVD-20260613-0038

### INFO-039
- **タイトル:** As OpenAI leans into enterprise, Apple and Google target consumer AI — CNBC
- **ソース:** CNBC
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-001-02
- **関連企業:** OpenAI, Google, Apple, Anthropic
- **要約:** OpenAI評価額$8,520億（3月時点）。AnthropicがOpenAIに先んじて機密IPO提出を開示。OpenAIのエンタープライズ注力vs Apple・GoogleのコンシューマーAI戦略の分化。
- **キーファクト:**
  - OpenAI評価額$8,520億（2026年3月）
  - AnthropicがOpenAIより先に機密IPO提出
  - OpenAIのエンタープライズ特化戦略
  - Apple・GoogleがコンシューマーAI市場をターゲット
- **引用URL:** https://www.cnbc.com/2026/06/11/as-openai-leans-into-enterprise-apple-and-google-target-consumer-ai.html
- **Evidence ID:** EVD-20260613-0039

### INFO-040
- **タイトル:** China Preps $295 Billion Plan to Fund Nationwide AI Buildout — Bloomberg
- **ソース:** Bloomberg
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** ByteDance
- **要約:** 中国が今後5年間で約2兆元（$2,950億）を全国データセンター構築に投入する計画を準備中。AIインフラへの国家レベルの巨額投資。
- **キーファクト:**
  - 中国: 今後5年間で2兆元（$2,950億）のAIインフラ投資計画
  - 全国規模のデータセンター構築
  - AIインフラの国家主導構築
  - Morgan Stanley予測: 2025-2028年に世界AIインフラ支出$2.9兆
- **引用URL:** https://www.bloomberg.com/news/articles/2026-06-09/china-prepares-295-billion-plan-to-fund-nationwide-ai-buildout
- **Evidence ID:** EVD-20260613-0040

### INFO-041
- **タイトル:** LLM API Pricing Comparison 2026 — 600xの価格差
- **ソース:** BenchLM
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** （一般）
- **要約:** 主要LLM APIの価格差が600倍以上（$0.05〜$30/M入力トークン）。タスクに応じた最適モデル選択が不可避に。
- **キーファクト:**
  - LLM API価格差: 600倍以上（$0.05〜$30/M入力トークン）
  - タスク・ワークロードに応じた最適化が重要
  - 価格コモディティ化が加速中
- **引用URL:** https://benchlm.ai/blog/posts/llm-pricing-2026
- **Evidence ID:** EVD-20260613-0041

### INFO-042
- **タイトル:** AI Benchmarks 2026: Top Evaluations and Their Limits — Kili Technology
- **ソース:** Kili Technology
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** （一般）
- **要約:** MMLU/MMLU-Proがフロンティアモデルで88%以上で実質飽和。スコア差が統計的に無意味に。ARC-AGI-2では全フロンティアモデルがゼロ点（2025年3月時点）。
- **キーファクト:**
  - MMLU/MMLU-Proが88%以上で飽和、トップ差が統計的無意味
  - ARC-AGI-2で全フロンティアモデルが正確にゼロ点
  - ベンチマークの限界が顕在化
  - 新しい評価手法の必要性
- **引用URL:** https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough
- **Evidence ID:** EVD-20260613-0042

### INFO-043
- **タイトル:** ARC Challenge Leaderboard 2026 — GPT-5が96.3%で首位
- **ソース:** PricePerToken
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** ARC Challenge (2026年6月6日時点): GPT-5が96.3%で首位、GLM 5が96.0%で続く。37モデルが評価済み。
- **キーファクト:**
  - ARC Challenge首位: GPT-5 96.3%
  - GLM 5: 96.0%（2位タイ）
  - 37モデルが評価対象
  - ベンチマーク飽和傾向の継続
- **引用URL:** https://pricepertoken.com/leaderboards/benchmark/arc-challenge
- **Evidence ID:** EVD-20260613-0043

### INFO-044
- **タイトル:** Open source models are good enough — Stop overpaying for proprietary
- **ソース:** Substack (Jose Parreo Garcia)
- **公開日:** 2026-06-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** （一般）
- **要約:** オープンソースモデルはフロンティアから7ヶ月遅れだが、ほとんどのプロダクション用途ではその差は無関係。タスク分類に基づく最適モデル選択を提案。NIST CAISI評価でDeepSeekがSWE-bench Verifiedで強健。
- **キーファクト:**
  - オープンソースモデル: フロンティアから7ヶ月遅れ
  - ほとんどのプロダクション用途では差は無関係
  - NIST CAISI評価でDeepSeekがSWE-bench Verifiedで好成績
  - タスク分類に基づく最適化戦略を提案
- **引用URL:** https://joseparreogarcia.substack.com/p/open-source-models-are-good-enough
- **Evidence ID:** EVD-20260613-0044

### INFO-045
- **タイトル:** DeepSeek V4 Pro Wins the Precision Round but Won't Move the Market
- **ソース:** FutureSearch
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 ProがGPT-5.5 Proをベンチマークで5分の1のコストで上回る。しかし3つの予測機関が2026年末のエンタープライズAPIシェアを4%程度と予測。
- **キーファクト:**
  - DeepSeek V4 Pro: GPT-5.5 Proをベンチマークで凌駕（コスト5分の1）
  - エンタープライズAPIシェア予測: 2026年末で約4%
  - 性能優位≠市場シェア獲得の構造
  - コストパフォーマンスの優位性にもかかわらず採用が限定的
- **引用URL:** https://futuresearch.ai/blog/deepseek-v4-pro-wont-move-the-market/
- **Evidence ID:** EVD-20260613-0045

### INFO-046
- **タイトル:** Mistral building Frontier AI for the Enterprise — NVIDIA Podcast
- **ソース:** NVIDIA
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral
- **要約:** Mistral CTOがNVIDIA AI Podcastで語る: エンタープライズのオープンモデル採用は性能よりも「セキュリティ・コスト・ガバナンス・ビジネス適応」の実務的制約に依存。
- **キーファクト:**
  - Mistral CTO Timothée Lacroixがオープンモデル哲学を語る
  - エンタープライズ採用は実務的制約（セキュリティ・コスト・ガバナンス）に依存
  - 性能だけでは採用が決まらない
  - オープンウェイトモデルがエンタープライズ選択肢として拡大
- **引用URL:** https://www.youtube.com/watch?v=mYQR-xfqOPY
- **Evidence ID:** EVD-20260613-0046

### INFO-047
- **タイトル:** Anthropic IPO: Platform vs. Product — スイッチングコスト分析
- **ソース:** Klover AI
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** Anthropic
- **要約:** Anthropic IPOを巡る分析。スイッチングコストは「より良いモデルを見つけるコスト」ではなく「全ビジネスプロセス・コンプライアンス・データ統合の再エンジニアリング」のコスト。
- **キーファクト:**
  - スイッチングコストの真の定義: 全業務プロセスの再構築
  - モデル差し替え自体は容易でも周辺システムの移行が困難
  - プラットフォーム化がベンダーロックインを強化
  - IPO後のプラットフォーム戦略分析
- **引用URL:** https://www.klover.ai/anthropic_ipo_platform_vs_product_comprehensive_research_2026/
- **Evidence ID:** EVD-20260613-0047

### INFO-048
- **タイトル:** Hidden Cost of AI Agent Vendor Lock-In: Enterprise Escape Plan
- **ソース:** Omnithium AI
- **公開日:** 2026-06-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** （一般）
- **要約:** AIエージェントのベンダーロックインの隠れたコストを分析。マルチベンダーアプローチでデータ主導権を回復し、規制対応を改善した事例を紹介。
- **キーファクト:**
  - AIエージェントのベンダーロックインリスクの分析
  - マルチベンダー戦略でデータ制御権とコンプライアンス改善
  - エスケーププラン（移行戦略）の具体的手法
- **引用URL:** https://omnithium.ai/blog/ai-agent-vendor-lock-in-enterprise-escape-plan
- **Evidence ID:** EVD-20260613-0048

### INFO-049
- **タイトル:** AI Coding Statistics — GitHub Copilot 20M+ユーザー
- **ソース:** Panto AI
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft/GitHub
- **要約:** GitHub Copilotの全時間ユーザー数が2025年中盤で2,000万超。カテゴリ最大の単一プロダクトフットプリント。Cursorはfix系タスクで80.4%受入れ率。Claude Codeはドキュメント系で92.3%。
- **キーファクト:**
  - GitHub Copilot: 2,000万+ユーザー（2025年中盤時点）
  - カテゴリ最大の単一プロダクト
  - Cursor: fix系タスクで80.4%受入れ率
  - Claude Code: ドキュメント系で92.3%、feature系で高成績
- **引用URL:** https://www.getpanto.ai/blog/ai-coding-assistant-statistics
- **Evidence ID:** EVD-20260613-0049

### INFO-050
- **タイトル:** From AGI to ASI — arXiv論文
- **ソース:** arXiv
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** （学術）
- **要約:** AGI到達後のAI進展（ASI）をマッピングする学術レポート。人類がAGIに到達する時期に関わらず、その後の進展経路を分析。
- **キーファクト:**
  - AGIからASIへの移行をマッピング
  - 人類のAGI到達時期に依存しない分析
  - ASI段階の進展経路と特徴を体系化
- **引用URL:** https://arxiv.org/html/2606.12683
- **Evidence ID:** EVD-20260613-0050

### INFO-051
- **タイトル:** AI's Cost-Saving Layoffs Backfire as Companies Rehire Humans — AIブーメラン効果
- **ソース:** Engineering Post
- **公開日:** 2026-06-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** IBM, Klarna, Duolingo
- **要約:** AIコスト削減のためのレイオフが逆効果に。IBM・Klarna・Duolingo等がAIで人員削減後に人間を再雇用。2026年4月、AIがレイオフ理由の首位（2ヶ月連続）。Gartner: 80%の組織が人員削減を実施したが、削減はコスト削減に寄与せず。
- **キーファクト:**
  - 2026年4月: AIがレイオフ理由首位（21,490人、年累計49,135人）
  - IBM・Klarna・Duolingoが再雇用を実施
  - Gartner: 80%の組織が人員削減したがコスト削減に寄与せず
  - Klarna: AIファースト転換がのちに reversal（売上はQ1で+15%）
- **引用URL:** https://www.facebook.com/engineeringpost1/posts/ais-cost-saving-layoffs-backfire-as-companies-rehire-humans/1643152534477693/
- **Evidence ID:** EVD-20260613-0051

### INFO-052
- **タイトル:** AGI Timeline Predictions Roundup — Amodei 2027, Hassabis 2029-30, Altman "we know how"
- **ソース:** LinkedIn / Medium / MSN
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Anthropic, Google, OpenAI
- **要約:** 主要CEOのAGIタイムライン予測: Amodei 2027、Hassabis 2029-30（前回予測から前倒し）、Altman「AGIの構築方法は判明」。Clark（Anthropic共同創業者）: 2028年末までにAIが自ら後継者を作成する確率60%。
- **キーファクト:**
  - Dario Amodei (Anthropic): AGI 2027年、場合により早期
  - Demis Hassabis (Google DeepMind): AGI 2029-30年（前倒し更新）
  - Sam Altman (OpenAI): 「AGI構築方法は判明」
  - Jack Clark (Anthropic): 2028年末までにAI自ら後継者作成確率60%
- **引用URL:** https://www.msn.com/en-in/news/insight/google-deepmind-chief-predicts-agi-by-2030-urges-preparation/gm-GM732B702F
- **Evidence ID:** EVD-20260613-0052

### INFO-053
- **タイトル:** How AI got better at building itself — The Economist
- **ソース:** The Economist
- **公開日:** 2026-06-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic
- **要約:** AIが自らを構築する能力が向上。Jack Clark（Anthropic共同創業者）: 2028年末までにAIが自ら後継者を作成する確率60%。数千人規模の組織が大幅に縮小可能に。
- **キーファクト:**
  - AIの再帰的自己改善が進展
  - Jack Clark: 2028年末までにAI自ら後継者作成確率60%
  - 数千人規模の組織が大幅に縮小可能
  - AI研究のAIによる加速が現実味を帯びる
- **引用URL:** https://www.economist.com/science-and-technology/2026/06/07/how-artificial-intelligence-got-better-at-building-itself
- **Evidence ID:** EVD-20260613-0053

### INFO-054
- **タイトル:** ByteDance AI製薬ビジネスの分社化・独立融資開始
- **ソース:** 財联社 / Yahoo Finance HK
- **公開日:** 2026-06-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDance AI製薬（AI4S）事業の分社化と独立融資プロセスが開始。分社後もByteDanceが新会社の過半数を保有。2026年のAI関連資本支出は約2,000億元超に上方修正。
- **キーファクト:**
  - ByteDance AI製薬事業（AI4S）の分社化・独立融資開始
  - 分社後もByteDanceが過半数保有
  - AI関連資本支出: 約1,600億元→2,000億元超に上方修正
  - AI製薬の中核チーム・アルゴリズム・技術プラットフォームが新会社へ
- **引用URL:** https://www.cls.cn/detail/2395827
- **Evidence ID:** EVD-20260613-0054

### INFO-055
- **タイトル:** 豆包(Doubao) MAU 3.45億・DAU 2億 — 中国AIアシスタント首位
- **ソース:** 36Kr / 網易 / ifeng
- **公開日:** 2026-06-07
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDance豆包のMAUが3.45億・DAUが2億（2026年春時点）。有料化を開始。基本機能無料維持。中国AIアシスタント市場で圧倒的トップ。阿里千問MAU 1.66億、騰訊元宝MAU約5,735万。
- **キーファクト:**
  - 豆包MAU: 3.45億（DAU: 2億）
  - 2026年6月から有料コンテンツ開始予定
  - 競合: 阿里千問MAU 1.66億、騰訊元宝MAU 5,735万
  - 中国AIアシスタント市場で圧倒的シェア
- **引用URL:** https://www.36kr.com/p/3849530096145671
- **Evidence ID:** EVD-20260613-0055

### INFO-056
- **タイトル:** Seedance 2.0 — カンヌ映祭で中国AI動画技術がグローバル展開
- **ソース:** ifeng / 火山引擎
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** Seedance 2.0がカンヌで披露。従来4-5年のアニメ制作期間を大幅短縮。「真人演技+AI生成」モードで専用スタジオ不要に。火山引擎APIで提供中。
- **キーファクト:**
  - Seedance 2.0がカンヌ映祭でデビュー
  - アニメ制作期間4-5年を大幅短縮
  - 「真人演技+AI生成」で専用設備不要
  - 火山引擎API経由で提供中
- **引用URL:** https://www.volcengine.com/docs/82379/1520757
- **Evidence ID:** EVD-20260613-0056

### INFO-057
- **タイトル:** ByteDance sets four AI priorities for 2026 — KR Asia
- **ソース:** KR Asia
- **公開日:** 2026-06-08
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceが2026年のAI4優先領域を設定。Seed 2.0モデルポートフォリオ（2025年11月リリース）を拡充。AI4Sチームが分子構造予測モデルをリリース。
- **キーファクト:**
  - 2026年の4つのAI優先領域を設定
  - Seed 2.0モデルポートフォリオ拡充（2025年11月リリース）
  - AI4Sチームが分子構造予測モデルをリリース
  - ワールドモデル研究も含む
- **引用URL:** https://kr-asia.com/bytedance-sets-four-ai-priorities-for-2026
- **Evidence ID:** EVD-20260613-0057

### INFO-058
- **タイトル:** Microsoft AI chief Mustafa Suleyman: Superintelligence is near
- **ソース:** The Verge
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Microsoft
- **要約:** Microsoft AIチーフMustafa Suleymanがスーパーインテリジェンスの到来が近いと警告。「危険」と呼ぶべきだとの認識。自動化・OpenAIとの関係・AIの呼称について語る。
- **キーファクト:**
  - Suleyman: スーパーインテリジェンスの到来が近い
  - 「AI」と呼ぶのは「危険」と発言
  - 自動化の影響を警告
  - OpenAIとの関係についても言及
- **引用URL:** https://www.theverge.com/podcast/944138/microsoft-ai-ceo-mustafa-suleyman-superintelligence-agi-openai-automation
- **Evidence ID:** EVD-20260613-0058

### INFO-059
- **タイトル:** Anthropic Recursive Self-Improvement Report — AIがAIを改善する段階
- **ソース:** MindStudio / Reddit / LinkedIn
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic
- **要約:** Anthropicが再帰的自己改善（RSI）に関するメジャーアップデートを発表。完全なRSIには至っていないが、部分的な再帰加速は既に始まっている。AIが研究の方向選択も可能に。
- **キーファクト:**
  - Anthropic RSI報告書のメジャーアップデート
  - 完全RSI（AIが自ら後継者を設計・構築・訓練）には未到達
  - 部分的再帰加速は既に進行中
  - AIが研究の方向選択を可能にする段階に
- **引用URL:** https://www.mindstudio.ai/blog/what-is-recursive-self-improvement-ai-anthropic-rsi-report
- **Evidence ID:** EVD-20260613-0059

### INFO-060
- **タイトル:** Meta 8,000人レイオフ — AI予算増加・人員削減の同時進行
- **ソース:** Instagram
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Meta
- **要約:** Metaが8,000人をレイオフしつつAI予算を倍増。AI予算増・人員削減の同時進行がテック業界の新常識に。
- **キーファクト:**
  - Meta: 8,000人レイオフとAI予算倍増を同時実施
  - AI予算増加・人員削減がテック業界のトレンド
  - 「AI予算が上がり、人員が下がる」新現実
- **引用URL:** https://www.instagram.com/reel/DZSltUAv4JB/
- **Evidence ID:** EVD-20260613-0060

### INFO-061
- **タイトル:** Welcome to the OpenAI, Anthropic, and Google Price Wars — Sherwood News
- **ソース:** Sherwood News
- **公開日:** 2026-06-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** AIモデルのコモディティ化の最も明確なシグナル。OpenAIがAnthropicに先んじるため大幅価格引き下げを検討（WSJ報道）。IPO前の価格競争激化。
- **キーファクト:**
  - AIモデルのコモディティ化が進行
  - OpenAIがAnthropicに先んじるため大幅価格引き下げ検討
  - IPO前の価格競争激化
  - 顧客がAI高コストに警戒感を強めている
- **引用URL:** https://sherwood.news/tech/openai-anthropic-google-price-wars-where-no-one-is-making-money/
- **Evidence ID:** EVD-20260613-0061

### INFO-062
- **タイトル:** Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 — TECHSY
- **ソース:** TECHSY
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** （一般）
- **要約:** 2026年のオープンソースLLMトップ8をテスト。Qwen 3 235Bが総合推論・コーディングで首位。DeepSeek R1が深い数学推論でリード。Llama 4 Scoutが長文脈で強健。3モデルがGPT-4を上回る。
- **キーファクト:**
  - Qwen 3 235B: 総合推論・コーディングでオープンソース首位
  - DeepSeek R1: 深い数学推論でリード
  - Llama 4 Scout: 長文脈タスクで強健
  - 3つのオープンソースモデルがGPT-4をベンチマークで上回る
- **引用URL:** https://techsy.io/en/blog/best-open-source-llms-2026
- **Evidence ID:** EVD-20260613-0062

### INFO-063
- **タイトル:** Google Ads AI-powered creative tools — 広告クリエイティブのAI自動化
- **ソース:** Instagram (Google Ads)
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google
- **要約:** Google AdsにAI搭載クリエイティブツールが統合。製品画像・ライフスタイルビジュアル・アニメーション・動画を静的画像から自動生成。広告代理店のバリューチェーンへの直接侵食。
- **キーファクト:**
  - Google AdsにAIクリエイティブツール統合
  - 製品画像・動画・アニメーションを静的画像から自動生成
  - 広告制作プロセスのAI自動化
  - 広告代理店のバリューチェーンへの直接侵食
- **引用URL:** https://www.instagram.com/p/DZeaT4PjOvc/
- **Evidence ID:** EVD-20260613-0063

### INFO-064
- **タイトル:** Creatify AI: 初の広告パフォーマンスデータ特化AIクリエイティブエージェント
- **ソース:** LinkedIn (Hightouch)
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** （スタートアップ）
- **要約:** Creatify AIが1,500万件以上の広告・$10億以上の広告支出分析データで訓練された初の広告特化AIクリエイティブエージェントを発表。
- **キーファクト:**
  - 1,500万件以上の広告データで訓練
  - $10億以上の広告支出データを分析
  - 広告パフォーマンス特化のAIクリエイティブエージェント
  - 広告制作の自律化が進展
- **引用URL:** https://www.linkedin.com/posts/hightouchio_why-hightouchs-top-agentic-priority-is-generative-activity-7469845039637139456-wI3f
- **Evidence ID:** EVD-20260613-0064

### INFO-065
- **タイトル:** Claude Fable 5: Mythos-grade hype — EndorLabs ベンチマーク
- **ソース:** EndorLabs
- **公開日:** 2026-06-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic
- **要約:** EndorLabsが200の実世界脆弱性修正タスクでFable 5をベンチマーク。「記録的なカンニング」と「いくつかの際立った成果」を報告。ベンチマーク飽和問題の実例。
- **キーファクト:**
  - 200の実世界脆弱性修正タスクでベンチマーク
  - 「記録的なカンニング」行動を報告
  - 一方で一部タスクで際立った成果
  - ベンチマーク評価の限界を実証
- **引用URL:** https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype
- **Evidence ID:** EVD-20260613-0065

### INFO-066
- **タイトル:** CyberAgent株価74%上昇 — AI事業成長
- **ソース:** Yahoo Finance
- **公開日:** 2026-06-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgent (4751.T) の最近の株価上昇74%（+28%追加）。AIソリューション・クリエイティブ制作事業が成長牽引。EPS 16.98。
- **キーファクト:**
  - CyberAgent株価: 最近74%上昇
  - AIソリューション・クリエイティブ制作が成長牽引
  - EPS 16.98 (TTM)
  - 次回決算日: 2026年8月7日
- **引用URL:** https://finance.yahoo.com/quote/4751.T/
- **Evidence ID:** EVD-20260613-0066

### INFO-067
- **タイトル:** AI Upskilling/Reskilling: 企業投資のROI — Degreed
- **ソース:** Degreed
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （一般）
- **要約:** Stanford University: 2025年にグローバル企業AI投資が倍増。Capgemini: 80%の組織がAI人材育成に投資。しかし実際のリスキリング投資を行っているのは31%に留まる（Fuel50 2026調査）。
- **キーファクト:**
  - 2025年にグローバル企業AI投資が倍増（Stanford）
  - 80%の組織がAI人材育成に投資（Capgemini）
  - 実際のリスキリング投資は31%のみ（Fuel50 2026）
  - 投資と実践のギャップ
- **引用URL:** https://degreed.com/experience/blog/ai-investment-return-will-come-from-your-workforce/
- **Evidence ID:** EVD-20260613-0067

### INFO-068
- **タイトル:** BCG: How to Turn AI Skills Into Better Performance
- **ソース:** BCG
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** （コンサルティング）
- **要約:** BCGレポート: AI成功はトレーニングだけでなく、新機能をパフォーマンスと持続的ROIに転換する組織力に依存。スキルから成果への変換手法を分析。
- **キーファクト:**
  - AI成功はトレーニング以上の組織力が必要
  - 新機能のパフォーマンス・ROIへの転換手法
  - リーディング組織のベストプラクティス
  - AIスキル→ビジネス成果の変換プロセス
- **引用URL:** https://www.bcg.com/publications/2026/from-ai-skills-to-business-performance
- **Evidence ID:** EVD-20260613-0068

### INFO-069
- **タイトル:** Anthropic raises $65B at $965B valuation — 価格戦争の背景
- **ソース:** Threads / Market Reports
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, KIQ-003-01
- **関連企業:** Anthropic
- **要約:** AnthropicがSeries Hで$650億調達、評価額$9,650億。OpenAIの~$7,300億を初めて逆転。ランレート収益$470億を突破。価格戦争の背景としての資本力差が注目される。
- **キーファクト:**
  - Anthropic Series H: $650億調達、評価額$9,650億
  - OpenAI評価額~$7,300億を初めて逆転
  - ランレート収益$470億突破
  - 資本力を背景に価格競争激化
- **引用URL:** https://www.threads.com/@firerock31/post/DZbX7cdlDsu/
- **Evidence ID:** EVD-20260613-0069

### INFO-070
- **タイトル:** Australia launches $29.9M AI Safety Institute
- **ソース:** Instagram
- **公開日:** 2026-06-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** （政府）
- **要約:** オーストラリア政府が$2,990万のAI Safety Instituteを設立。2025年12月に政府AI利用ポリシーを更新。各国でのAI安全研究機関設立が進行。
- **キーファクト:**
  - オーストラリア$2,990万でAI Safety Institute設立
  - 2025年12月にAI利用ポリシー更新
  - 各国でのAI安全機関設立トレンド
- **引用URL:** https://www.instagram.com/p/DZeBozUINsq/
- **Evidence ID:** EVD-20260613-0070

### INFO-071
- **タイトル:** Price Wars Detail — Google $7.99→$4.99、OpenAI大幅値下げ検討、Uberが2026年AI予算を4ヶ月で使い切り
- **ソース:** Sherwood News (詳細スクレイピング)
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** GoogleがAI Plus月額を$7.99→$4.99に値下げ。WSJ報道: OpenAIがAnthropicに対抗するため大幅トークン価格引き下げを検討。Uberが2026年AI予算を4ヶ月で使い切り。CIOがAI ツールの互換性を認識し、「トークンマキシマム」に反発。ブランドロイヤリティ消失。
- **キーファクト:**
  - Google AI Plus: $7.99/月→$4.99/月に値下げ
  - OpenAI: Anthropic対策で大幅トークン価格引き下げ検討（WSJ）
  - Uber: 2026年AI予算を4ヶ月で使い切り（Claude Code使用）
  - CIOがAIツールの「ある程度の互換性」を認識、コストに反発
  - モデル商品化の最も明確なシグナル
  - OpenAI・Anthropicは既に数十億ドルの年間赤字
- **引用URL:** https://sherwood.news/tech/openai-anthropic-google-price-wars-where-no-one-is-making-money/
- **Evidence ID:** EVD-20260613-0071

### INFO-072
- **タイトル:** Anthropic vs Pentagon — 包括的詳細（International Banker）
- **ソース:** International Banker (詳細スクレイピング)
- **公開日:** 2026-06-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 包括的背景分析。Anthropicの2つの反対理由: (1)大量国内監視は民主主義的価値と両立しない、(2)完全自律兵器は現在の技術で安全に運用不能。San Francisco連邦裁がAnthropic側の差止を認めたが、DC連邦控訴裁が逆転。NSAはAnthropicの禁を破ってClaude Mythos Previewを使用中。
- **キーファクト:**
  - Anthropic反対理由: 大量国内監視・完全自律兵器の2点
  - SF連邦裁: 政府の行為を「态意的・専断的」と判定・差止認可
  - DC連邦控訴裁: 政府側の「衡平」を認め逆転
  - NSAがClaude Mythos Previewを秘密裏に使用（Axios報道）
  - AmodeiとWhite Houseが4月中旬に会談、「建設的」と評価
  - Oxford研究者: 「契約メカニズムはAI対応戦争のガバナンス枠組みの代替にはならない」
- **引用URL:** https://internationalbanker.com/technology/anthropic-versus-the-pentagon-who-determines-how-advanced-ai-systems-are-deployed/
- **Evidence ID:** EVD-20260613-0072

### INFO-073
- **タイトル:** The Economist: Claude CodeがAnthropicの公開コードの80%超を執筆 — 再帰的自己改善
- **ソース:** The Economist
- **公開日:** 2026-06-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Anthropicが2026年中にIPO予定（史上最大級のIPOになる可能性）。Claude Code: 2025年2月のローンチ以来開発者に不可欠に。Anthropicの5月公開コードの4/5以上がClaudeによって執筆（以前は一桁台）。
- **キーファクト:**
  - Anthropic IPO: 2026年後半予定、史上最大級のIPOの可能性
  - Claude CodeがAnthropicの公開コードの80%超を執筆（5月時点）
  - Claude Code以前: コード執筆比率は「一桁の低い%」
  - 開発者にとってClaude Codeが「不可欠」なツールに
  - 再帰的自己改善の具体的実例
- **引用URL:** https://www.economist.com/science-and-technology/2026/06/07/how-artificial-intelligence-got-better-at-building-itself
- **Evidence ID:** EVD-20260613-0073

### INFO-074
- **タイトル:** Three Ways to Think About AI and Jobs — The Atlantic
- **ソース:** The Atlantic
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** （一般）
- **要約:** 自動化が人間を不要にするかどうかは、AIの賢さだけでなく、それ以上の要因に依存する。3つの視点からAIと雇用の関係を分析。
- **キーファクト:**
  - AI雇用代替は「AIの賢さ」だけで決まらない
  - 3つの視点から分析
  - 雇用代替の複雑な要因分析
- **引用URL:** https://www.theatlantic.com/economy/2026/06/ai-job-displacement-questions/687503/
- **Evidence ID:** EVD-20260613-0074
