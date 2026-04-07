# 収集データ: 2026-04-07

## メタデータ
- 収集日時: 2026-04-07 12:30 UTC
- 品質フラグ: NORMAL
- 収集件数: 50件
- 対応KIQ: KIQ-001-01〜05, KIQ-002-01〜06, KIQ-003-01〜04, KIQ-004-01〜03, KIQ-005-01〜03, BYTEDANCE-CHINESE
- 動的追加クエリ実施: Claude Code競合比較, 中国AI市場調査, 政府圧力・萎縮効果分析, AI導入失敗分析
- 主要発見:
  - Claude Codeソースコードリーク（512,000行、npm経由）
  - OpenAI-Pentagon $200M契約、#QuitGPT運動で250万ユーザー削除
  - Anthropic連邦禁止措置、裁判所仮差止命令
  - OpenAI $122B調達、評価額$852B
  - ByteDance豆包日次Token 120兆突破
  - AWS DevOps/Security Agent GA
  - Klarna AIレイオフ失敗、55%企業が後悔

## 収集結果

### INFO-001
- **タイトル:** Claude for Financial Services
- **ソース:** Anthropic（公式ブログ）
- **公開日:** 2025-07-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** Anthropicが金融サービス向け総合ソリューションを発表。Databricks、Snowflake、FactSet、S&P Global等とのMCPコネクタ統合、Claude 4がVals AI Finance Agent benchmarkで他社フロンティアモデルを上回る性能を記録。NBIM（世界最大のソブリンウェルスファンド）で約20%生産性向上（213,000時間相当）を達成。
- **キーファクト:**
  - Claude 4モデルが金融タスクで他社フロンティアモデルを上回る（Vals AI Finance Agent benchmark）
  - NBIM: 20%生産性向上、9,000社以上のポートフォリオ分析自動化
  - AIG: アンダーライティング時間5倍短縮、データ精度75%→90%以上向上
  - Databricks、Snowflake、FactSet、Morningstar、PitchBook、S&P Global等と統合
  - AWS Marketplaceで提供開始、Google Cloud Marketplace近日対応
- **引用URL:** https://www.anthropic.com/news/claude-for-financial-services

### INFO-002
- **タイトル:** Anthropic expands global leadership in enterprise AI
- **ソース:** Anthropic（公式ブログ）
- **公開日:** 2025-09-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** AnthropicがエンタープライズAI市場でトップシェアを獲得。ARRが2024年初頭の$87Mから2025年8月に$5B以上へ急成長（57倍）。$13B Series F調達、評価額$183B（ポストマネー）。グローバル顧客数が2年前の1,000社未満から30万社以上へ（300倍成長）。
- **キーファクト:**
  - エンタープライズAI市場トップシェア（Menlo Ventures調査）
  - ARR: $87M（2024年初頭）→ $5B以上（2025年8月）、57倍成長
  - Series F: $13B調達、評価額$183B
  - 顧客数: 1,000社未満（2年前）→ 30万社以上（300倍成長）
  - Chris CiauriがInternational Managing Directorに就任（元Google Cloud EMEA社長、Salesforce EMEA EVP）
  - EMEA: ダブリン・ロンドンで100名以上の新規採用、チューリッヒ研究所
  - 日本: 東京にアジア初のオフィス開設
- **引用URL:** https://www.anthropic.com/news/anthropic-expands-global-leadership-in-enterprise-ai-naming-chris-ciauri-as-managing-director-of

### INFO-003
- **タイトル:** Claude for Life Sciences
- **ソース:** Anthropic（公式ブログ）
- **公開日:** 2025-10-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** Anthropicがライフサイエンス向けClaudeソリューションを発表。Sonnet 4.5がProtocol QA benchmarkで0.83（人間ベースライン0.79）。Benchling、BioRender、PubMed、10x Genomics等とのMCPコネクタ、科学的プロトコル用Agent Skillsを提供。
- **キーファクト:**
  - Sonnet 4.5: Protocol QA 0.83（人間0.79、Sonnet 4は0.74）
  - 新MCPコネクタ: Benchling、BioRender、PubMed、Wiley Scholar Gateway、Synapse.org、10x Genomics
  - Agent Skills: single-cell-rna-qc（scverseベストプラクティス準拠）
  - 顧客: Sanofi、Novo Nordisk、Broad Institute、Stanford、Genmab等
  - Novo Nordisk: 臨床ドキュメント作成時間99.9%短縮（10週以上→10分）
- **引用URL:** https://www.anthropic.com/news/claude-for-life-sciences

### INFO-004
- **タイトル:** Offering expanded Claude access across all three branches of the U.S. government
- **ソース:** Anthropic（公式ブログ）
- **公開日:** 2025-08-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicが米国政府の三権（行政・立法・司法）すべてに対し、Claude for Enterprise/Governmentを$1で提供開始。FedRAMP High認証取得済み。国防総省と$200M上限の契約、ローレンス・リバモア国立研究所で1万人の科学者が日常利用。
- **キーファクト:**
  - 三権（連邦行政機関、立法府、司法府）すべてに$1で提供
  - FedRAMP High認証（非機密扱いの最高基準）
  - 国防総省: CDAO経由で$200M上限の契約
  - ローレンス・リバモア国立研究所: 1万人の科学者が日常利用
  - AWS、Google Cloud、Palantir経由で提供
- **引用URL:** https://www.anthropic.com/news/offering-expanded-claude-access-across-all-three-branches-of-government

### INFO-005
- **タイトル:** Grok 3 Beta — The Age of Reasoning Agents
- **ソース:** xAI（公式ブログ）
- **公開日:** 2025-02-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01
- **関連企業:** xAI
- **要約:** xAIがGrok 3 Betaを発表。Colossusスーパークラスターで従来のSOTAモデルの10倍のコンピュートで学習。AIME 2025で93.3%（cons@64）、GPQAで84.6%、LiveCodeBenchで79.4%。Chatbot Arena Elo 1402。DeepSearch（AIエージェント）を初公開。
- **キーファクト:**
  - AIME 2025: 93.3%（cons@64）、AIME 2024: 52.2%
  - GPQA: 84.6%（Grok 3 Think）、75.4%（Grok 3 Beta）
  - LiveCodeBench: 79.4%（Think）、57.0%（Beta）
  - MMLU-pro: 79.9%、MMMU: 73.2%
  - コンテキストウィンドウ: 100万トークン（従来の8倍）
  - Chatbot Arena Elo: 1402（コードネーム「chocolate」で1位）
  - DeepSearch: 真実を追求するAIエージェント
  - API近日公開（標準モデル＋推論モデル）
- **引用URL:** https://x.ai/blog/grok-3

### INFO-006
- **タイトル:** Claude Agents SDK vs. OpenAI Agents SDK vs. Google ADK Comparison
- **ソース:** Composio（テックブログ）
- **公開日:** 2026-04-05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** 2026年の主要Agent SDK（Claude Agent SDK、OpenAI Agents SDK、Google ADK）の詳細比較。OpenAIは軽量でVoice対応、ClaudeはOS直接アクセス可能、Google ADKはマルチ言語（Python/Java/Go）対応が特徴。
- **キーファクト:**
  - OpenAI Agents SDK: Python/TSファースト、100+ LLM対応、Voice/TTS内蔵
  - Claude Agent SDK: Bash実行・ファイルシステム直接アクセス、Claude Codeから進化
  - Google ADK: Python/TS/Java/Go対応、グラフベースワークフロー（2.0 Alpha）、A2Aプロトコル
  - MCP対応: 全SDK対応（Composio経由で850+ツール統合）
- **引用URL:** https://composio.dev/content/claude-agents-sdk-vs-openai-agents-sdk-vs-google-adk

### INFO-007
- **タイトル:** Claude Agent SDK TypeScript v0.2.92 Released
- **ソース:** GitHub（anthropics/claude-agent-sdk-typescript）
- **公開日:** 2026-04-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版がv0.2.92に更新。Claude Code v2.1.92とパリティ達成。v0.2.89でstartup()による初回クエリ20倍高速化、v0.2.91でterminal_reason追加。
- **キーファクト:**
  - v0.2.92: Claude Code v2.1.92とパリティ
  - v0.2.91: terminal_reasonフィールド追加（completed, aborted_tools, max_turns等）、sandboxのfailIfUnavailableデフォルトtrue
  - v0.2.89: startup()で初回クエリ~20倍高速化、listSubagents()/getSubagentMessages()追加
  - v0.2.86: getContextUsage()追加、session_id自動割り当て
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases

### INFO-008
- **タイトル:** Grok 4.20 Multi-Agent Released
- **ソース:** Puter Developer
- **公開日:** 2026-03-31
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI
- **要約:** xAIがGrok 4.20 Multi-Agentをリリース。複数AIエージェントが協調して複雑なタスクを実行。低/中reasoning effortで4エージェント、高/最高で16エージェント並列動作。Artificial Analysis Agentic Index 68.7。
- **キーファクト:**
  - コンテキストウィンドウ: 200万トークン
  - 最大出力: 200万トークン
  - 価格: 入力$2/M、出力$6/M
  - Agentic Index: 68.7（最高水準）
  - エージェント数: 4（低/中effort）〜16（高/最高effort）
  - Web検索、X検索、ツールオーケストレーション内蔵
- **引用URL:** https://developer.puter.com/ai/x-ai/grok-4.20-multi-agent/

### INFO-009
- **タイトル:** Grok 4.1 Fast on Oracle Cloud
- **ソース:** Oracle Cloud Infrastructure Documentation
- **公開日:** 2026-04-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** xAI, Oracle
- **要約:** Oracle CloudでxAI Grok 4.1 Fastが利用可能に。2Mトークンコンテキスト、ハルシネーション率約3分の1削減、エージェントワークフロー特化。Reasoning/Non-Reasoning両モード提供。
- **キーファクト:**
  - モデル名: xai.grok-4-1-fast-reasoning / xai.grok-4-1-fast-non-reasoning
  - コンテキスト: 200万トークン
  - ハルシネーション率: Grok 4 Fast比で約3分の1削減
  - 機能: 関数呼び出し、構造化出力、キャッシュ入力トークン
  - マルチモーダル: テキスト+画像入力
- **引用URL:** https://docs.oracle.com/en-us/iaas/Content/generative-ai/xai-grok-4-1-fast.htm

### INFO-010
- **タイトル:** Grok 4.20 API Pricing & Performance
- **ソース:** OpenRouter
- **公開日:** 2026-03-31
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-001-01
- **関連企業:** xAI
- **要約:** Grok 4.20がOpenRouterで提供開始。市場最低クラスのハルシネーション率78%、2Mコンテキスト。価格は入力$2/M、出力$6/M。キャッシュヒット率72.3%。
- **キーファクト:**
  - 非ハルシネーション率: 78%（Artificial Analysis Omniscience benchmark、最高）
  - コンテキスト: 200万トークン、最大出力200万トークン
  - 価格: 入力≤200K=$2/M、>200K=$4/M、出力≤200K=$6/M、>200K=$12/M
  - スループット: 平均118 tok/s、レイテンシ0.59s
  - ツールコールエラー率: 3.83%、構造化出力エラー率: 3.08%
- **引用URL:** https://openrouter.ai/x-ai/grok-4.20-beta

### INFO-011
- **タイトル:** Top AI Agents of 2026 Comparison
- **ソース:** Medium
- **公開日:** 2026-04-05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** 複数
- **要約:** 2026年の主要AIエージェント（OpenClaw、Hermes Agent、Paperclip、CrewAI、AutoGen、LangGraph）の比較レビュー。市場がパーソナルエージェント、チーム/エンタープライズオーケストレーション、独自システムの3カテゴリに分化。
- **キーファクト:**
  - 評価軸: メモリ、拡張性、調整機能、デプロイ柔軟性、制御/安全性、価値実現までの時間
  - OpenClaw: 3.31Bトークン使用（OpenRouter月間トップ）
  - 市場の3分化: パーソナルエージェント vs エンタープライズフレームワーク vs 独自システム
- **引用URL:** https://medium.com/@orami98/i-compared-the-top-ai-agents-of-2026-heres-what-they-re-actually-built-for-eaef228f61a9

### INFO-012
- **タイトル:** Claude Code CLI Source Code Leaked via npm Source Maps
- **ソース:** Reddit / GitHub
- **公開日:** 2026-03-31
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Code CLIのソースコード（約512,000行）をnpmレジストリの.mapファイル経由で誤って公開。SOC2コンプライアンス違反の懸念、サプライチェーン攻撃リスク、競合他社による解析が発生。Anthropicは公開リポジトリの削除を要求。
- **キーファクト:**
  - ソースコード: TypeScript製、約512,000行
  - 原因: npmパッケージにソースマップファイル(.map)を同梱
  - 内容: 未来の機能ロードマップ、ユーザーフラストレーション検出パターン等が含まれる
  - 影響: SOC2違反の可能性、サプライチェーン攻撃リスク、競合解析
  - 公開リポジトリ: GitHubで削除要請中
- **引用URL:** https://www.reddit.com/r/singularity/comments/1s8izpi/claude_code_source_code_has_been_leaked_via_a_map/

### INFO-013
- **タイトル:** OpenAI Secures $200M Pentagon Defense Contract
- **ソース:** IT-Daily / Jacobin / Lever News
- **公開日:** 2026-02-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Pentagon
- **要約:** OpenAIが米国防総省と$200Mの契約を締結。高度なAIプロトタイプの開発が目的。OpenAIは政策を変更し軍事利用を許可、国家安全保障関係者を大量採用、国防請負業者と提携。Anthropicが安全性制限の削除を拒否した後の契約獲得。
- **キーファクト:**
  - 契約額: $200M（国防総省）
  - 目的: 高度なAIプロトタイプ開発
  - 政策変更: 「合法的な目的」であれば軍事利用を許可
  - 人事: 国家安全保障関係者を大量採用
  - 文脈: Anthropicの安全性制限拒否後に契約獲得
- **引用URL:** https://www.it-daily.net/shortnews-en/openai-200-million-dollar-contract-from-the-us-department-of-defense

### INFO-014
- **タイトル:** #QuitGPT Movement: 2.5 Million Users Delete ChatGPT After Pentagon Deal
- **ソース:** Forbes
- **公開日:** 2026-04-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIのペンタゴン契約後、#QuitGPT運動が急拡大。250万ユーザーがChatGPTを削除し、1日でアンインストールが295%急増。ClaudeがApp Storeで1位に到達。AIツール選択がブランド価値の表明となり、切り替えコストがほぼゼロであることを示唆。
- **キーファクト:**
  - 削除ユーザー数: 250万人以上
  - アンインストール増加: 1日で295%急増
  - Claude App Store: 1位に到達
  - 原因: ペンタゴン契約、安全性制限削除への反発
  - OpenAI内部: ロボティクス責任者Caitlin Kalinowskiが辞任
- **引用URL:** https://www.forbes.com/sites/jodiecook/2026/04/03/why-chatgpts-pentagon-deal-sparked-25-million-quitgpt-uninstalls/

### INFO-015
- **タイトル:** Anthropic Federal Ban: Judge Grants Injunction But Pentagon CTO Says Ban Stands
- **ソース:** Tully Legal / Defense Communities / NextGov
- **公開日:** 2026-04-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, Pentagon
- **要約:** 連邦裁判所がAnthropicの「サプライチェーンセキュリティリスク」指定に対し仮差止命令を発令。しかしペンタゴンCTOは禁止措置が継続すると表明。2026年2月27日の大統領指令による連邦機関でのAnthropic排除、3月26日の差止命令という経緯。
- **キーファクト:**
  - 2/27: 大統領指令が連邦機関でのAnthropic使用を禁止
  - 3/26: 連邦裁判所が仮差止命令を発令
  - 4/2: ペンタゴンCTOが禁止継続を表明
  - 原因: 安全性制限削除拒否による政府報復
  - 影響: 18連邦機関、17人の政府職員が被告
- **引用URL:** https://www.tullylegal.com/our-firm/news/judge-grants-anthropic-preliminary-injunction-but-pentagon-cto-says-ban-still-stands/

### INFO-016
- **タイトル:** OpenAI Closes Record $122B Funding Round at $852B Valuation
- **ソース:** CNBC
- **公開日:** 2026-03-31
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがシリコンバレー史上最大の資金調達ラウンドを完了。$122Bの確定コミットメント、評価額$852B（ポストマネー）。SoftBank、Amazon（$50B）、Nvidia（$30B）が主要投資家。月間収益$2B、前年収益$13.1B。IPO準備中。
- **キーファクト:**
  - 調達額: $122B（当初$110Bから増額）
  - 評価額: $852B（ポストマネー）
  - 主要投資家: SoftBank、Amazon（$50B）、Nvidia（$30B）、Microsoft
  - 月間収益: $2B
  - 前年収益: $13.1B（まだ黒字化せず）
  - ChatGPT利用者: 週間9億アクティブユーザー、5000万以上のサブスクライバー
- **引用URL:** https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html

### INFO-017
- **タイトル:** ByteDance Doubao Token Usage Exceeds 120 Trillion Daily
- **ソース:** InfoQ（中国）
- **公開日:** 2026-04-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-02, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 字節跳動の火山エンジンが豆包（Doubao）大モデルの利用状況を発表。日次Token使用量が120兆を突破、過去3ヶ月で倍増。累計Token使用量1兆超の企業顧客が100社→140社に増加。Seedance2.0 API公測開始、Agent製品ArkClawとHiAgentを発表。
- **キーファクト:**
  - 日次Token使用量: 120兆（3ヶ月で倍増、2024年5月比1000倍）
  - 累計1兆Token超企業: 140社（昨年末比+40社）
  - Seedance2.0: 動画生成API公測開始
  - ArkClaw: クラウド智能体サービス、飛書・微信・釘釘連携
  - HiAgent: エンタープライズAgent プラットフォーム
  - ClawHub中国ミラーサイト: OpenClawと共同構築
- **引用URL:** https://www.infoq.cn/article/SF95yJdFgaWk9vDhZa2I

### INFO-018
- **タイトル:** AWS DevOps Agent & Security Agent GA Released
- **ソース:** AWS Blog
- **公開日:** 2026-04-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon, AWS
- **要約:** AWSがDevOps AgentとSecurity Agentを一般提供開始。Bedrock AgentCore EvaluationsもGA、AIエージェントの品質評価を自動化。MCPサーバーをAgentCore Gatewayに接続するOAuth認証フローも提供開始。
- **キーファクト:**
  - DevOps Agent: 一般提供開始
  - Security Agent: 一般提供開始
  - AgentCore Evaluations: GA、AIエージェント品質評価自動化
  - AgentCore Gateway: MCPサーバー接続、OAuth認証フロー対応
  - ライフサイクル変更: 2026年3月31日更新
- **引用URL:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-devops-agent-security-agent-ga-product-lifecycle-updates-and-more-april-6-2026/

### INFO-019
- **タイトル:** KPMG Global AI Pulse Survey: 32% Deploying AI Agents
- **ソース:** KPMG
- **公開日:** 2026-03-xx
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** KPMGグローバル調査: 世界のリーダーの75%がAI投資を優先。AIエージェント採用が加速、32%がデプロイ・スケーリング中、27%が複数エージェントのオーケストレーションを実施。
- **キーファクト:**
  - AI投資優先リーダー: 75%
  - AIエージェントデプロイ中: 32%
  - 複数エージェントオーケストレーション: 27%
  - エンタープライズAIエージェント利用・テスト中: 72%
  - 投資増加計画: 84%
- **引用URL:** https://kpmg.com/xx/en/media/press-releases/2026/03/kpmg-global-ai-pulse-survey.html

### INFO-020
- **タイトル:** AI Blamed for 25% of March Job Cuts - Challenger Report
- **ソース:** Forbes / BCG
- **公開日:** 2026-04-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** 複数
- **要約:** 2026年3月の人員削減理由の25%がAI。Challenger, Gray and Christmasの報告によると92,000件の米国人員削減がAIを理由とした。BCGは今後2-3年で米国の50-55%の職務がAIで再形成されると予測。OracleがAI投資拡大中に数千人を解雇。
- **キーファクト:**
  - 3月人員削減理由: AIが25%で首位
  - AI理由の解雇: 約92,000件（米国ベース）
  - BCG予測: 今後2-3年で50-55%の職務がAI再形成
  - Oracle解雇: 数千人、AI投資拡大と並行
  - テック業界: 解雇の主要セクター
- **引用URL:** https://www.forbes.com/sites/maryroeloffs/2026/04/02/ai-blamed-heavily-for-march-job-cuts-report-says/

### INFO-021
- **タイトル:** Claude Reaches #1 on App Store After #QuitGPT Movement
- **ソース:** Instagram / Polymarket / Facebook
- **公開日:** 2026-03-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** #QuitGPT運動の結果、Claudeが米国App Storeで1位に到達。日次ダウンロード149K vs ChatGPT 124K。米国・カナダ・欧州の多くで1位。OpenAIの政府契約への反発が代替案を探るユーザーの流入を促進。
- **キーファクト:**
  - 日次ダウンロード: Claude 149K vs ChatGPT 124K
  - App Store: 米国・カナダ・欧州で1位
  - 米国ダウンロード増加: 37-88%
  - 原因: OpenAI政府契約への反発
  - 移行の容易さ: AIアシスタントの切り替えコストほぼゼロ
- **引用URL:** https://www.instagram.com/p/DWsIqSGlIbr/

### INFO-022
- **タイトル:** OpenAI Codex Moves to Token-Based Pricing
- **ソース:** Reddit / OpenAI Help
- **公開日:** 2026-04-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIがCodexの価格体系をメッセージ単位からトークン単位に変更。Business・Enterprise新規プランが対象。API使用と価格を統一。Plus・Proは従来の価格体系を維持。
- **キーファクト:**
  - 変更日: 2026年4月2日
  - 対象: Business・Enterprise新規プラン
  - 変更内容: メッセージ単位→トークン単位価格
  - API価格との統一
  - Plus・Pro: 従来体系維持
- **引用URL:** https://openai.com/index/codex-flexible-pricing-for-teams/

### INFO-023
- **タイトル:** MCP Ecosystem Explosive Growth in 2026
- **ソース:** Cal.com / TrueFoundry / Medium
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** 複数
- **要約:** MCP（Model Context Protocol）エコシステムが2026年に爆発的成長。MCPサーバー開発企業、レジストリ、セキュリティツールが急増。DomainToolsが20年以上のドメインインテリジェンスに接続するMCPサーバーをローンチ。AWS AgentCore GatewayがMCP接続をサポート。
- **キーファクト:**
  - MCP: AIツールと外部ツール・DB・サービスの統合レイヤー
  - エコシステム: サーバー開発、レジストリ、ガバナンスツール急増
  - DomainTools MCP: 20年分のドメインインテリジェンス接続
  - AWS AgentCore Gateway: MCP OAuth認証フロー対応
  - 企業適用: ガバナンス、セキュリティ、エンタープライズ対応
- **引用URL:** https://cal.com/blog/best-mcp-servers

### INFO-024
- **タイトル:** ZTE Partners with ByteDance for New Doubao AI Phone
- **ソース:** Sina Finance / 36Kr
- **公開日:** 2026-03-31
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance, ZTE
- **要約:** 中興通訊（ZTE）が字節跳動と協力し、新世代の豆包AI携帯電話を開発中。2026年第2四半期末頃に発売予定。豆包が「推奨」機能でEC購入を代行するなど、大モデルが「実務時代」に入ったことを示す。
- **キーファクト:**
  - パートナー: ZTE × ByteDance
  - 製品: 新世代豆包AI携帯電話
  - 発売予定: 2026年Q2末
  - 機能: EC購入代行、推奨機能
  - 背景: 大モデルが「実務時代」へ
- **引用URL:** https://finance.sina.com.cn/tech/roll/2026-03-31/doc-inhswavw3390689.shtml

### INFO-025
- **タイトル:** Fed Reserve: 18% of US Firms Adopted AI by End of 2025
- **ソース:** Federal Reserve
- **公開日:** 2026-04-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** 連邦準備制度理事会の調査: 2025年末時点で米国企業の約18%がAIを採用。国勢調査局のビジネス調査データに基づく。手法変更前のデータとの比較では継続的な上昇傾向を示唆。
- **キーファクト:**
  - AI採用企業: 米国企業の約18%（2025年末）
  - データソース: 国勢調査局ビジネス調査
  - 傾向: 継続的な上昇
  - 手法変更: 2025年末に調査方法を変更
- **引用URL:** https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html

### INFO-026
- **タイトル:** Gemini 3.1 ADK Multimodal Agent with Live API
- **ソース:** Medium / Google AI for Developers
- **公開日:** 2026-04-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** Google Agent Development Kit (ADK)とGemini Flash Live 3.1を使用したマルチモーダルエージェント構築。Gemini Live APIでリアルタイム音声・動画対話を実現。VideoSDKがGemini Live APIでVoice AI Agentをローンチ、コスト40%削減、レイテンシ30%改善、収益2倍。
- **キーファクト:**
  - Gemini Live API: リアルタイム音声・動画対話
  - VideoSDK: コスト40%削減、レイテンシ30%改善、収益2倍
  - マルチモーダル埋め込み: テキスト・画像・動画・音声・PDFを統一空間にマッピング
  - Gemini 3.1: テキストから動画生成機能を追加
- **引用URL:** https://ai.google.dev/gemini-api/docs/models

### INFO-027
- **タイトル:** AI Model Benchmark Leaderboard April 2026
- **ソース:** Artificial Analysis / PricePerToken / BenchLM
- **公開日:** 2026-04-05
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** 複数
- **要約:** 2026年4月のAIモデルベンチマークランキング。GPQAでGPT-5.4が92.0%、GPT-5.3 Codexが91.5%、Gemini 3 Pro Previewが90.8%。Claude Opus 4.6はGPQA 93%（100万トークン時）、MMLU-Pro 88.9%。RAG最適はGemini 3 Pro Preview 89.8%。
- **キーファクト:**
  - GPQA: GPT-5.4 92.0%、GPT-5.3 Codex 91.5%、Gemini 3 Pro Preview 90.8%
  - Claude Opus 4.6: GPQA 93%（100万トークン）、MMLU-Pro 88.9%、Codeforces 2150 ELO
  - RAG最適: Gemini 3 Pro Preview 89.8%、Claude Opus 4.5 88.9%
  - Llama 4 Maverick: Gemma 4 31Bと比較（MMLU Pro 85.2%、AIME 2026 89.2%）
- **引用URL:** https://benchlm.ai/best/overall

### INFO-028
- **タイトル:** $1.2 Trillion AI M&A in Q1 2026 - Record Breaking
- **ソース:** Financial Content Markets
- **公開日:** 2026-04-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** 複数
- **要約:** 2026年第1四半期のAI関連M&Aが$1.2兆で過去最高を記録。GoogleがWizを$320億で買収（史上最大）。MetaがManus AIを$20億超で買収。昨年の$1,550億のAI M&Aの約半分がエージェント関連。
- **キーファクト:**
  - Q1 2026 M&A: $1.2兆（過去最高）
  - Google-Wiz: $320億（Alphabet史上最大買収）
  - Meta-Manus AI: $20億超（Meta最大級のAI買収）
  - 昨年AI M&A: $1,550億、約半分がエージェント関連
- **引用URL:** https://markets.financialcontent.com/stocks/article/marketminute-2026-4-3-the-12-trillion-ai-land-grab-q1-2026-m-and-a-smashes-records-as-corporate-giants-pivot-to-aggressive-expansion

### INFO-029
- **タイトル:** Klarna AI Layoffs Backfire - 55% of Companies Regret AI Cuts
- **ソース:** Forbes / Instagram / Medium
- **公開日:** 2026-04-xx
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo, IBM
- **要約:** Klarnaが2023年に700人のCS担当をAIに置換したが、2026年には教科書的な失敗例に。AIレイオフを実施した企業の55%が後悔、74%が品質低下を報告、再雇用コストは当初の節約の3倍。IBMも8,000人を削減後に課題。
- **キーファクト:**
  - Klarna: 700人CS削減→失敗の教訓
  - AIレイオフ後悔企業: 55%（Forrester 2026）
  - 品質低下報告: 74%
  - 再雇用コスト: 当初節約の3倍
  - Duolingo: 10%人員削減
- **引用URL:** https://www.sandhu.co.uk/insights/the-machines-were-supposed-to-replace-us-instead-they-need-us-more-than-ever

### INFO-030
- **タイトル:** DeepSeek V4 Fuels China AI Ambitions, Moves to Huawei Chips
- **ソース:** MSN / TechWire Asia
- **公開日:** 2026-04-xx
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek, Huawei
- **要約:** DeepSeek V4が中国のAI野望を加速。Huaweiチップへの移行を進め、Nvidia依存を削減。中国のAI独立戦略を反映。オープンウェイトモデルで中国AIセクターが急成長。
- **キーファクト:**
  - DeepSeek V4: Huaweiチップへの移行
  - 目的: Nvidia依存削減、中国AI独立
  - 影響: 中国AIセクター急成長
  - オープンウェイトモデル: 中国の競争力強化
- **引用URL:** https://techwireasia.com/2026/04/deepseek-v4-points-to-growing-use-of-huawei-chips-in-ai-models/

### INFO-031
- **タイトル:** Half of US Data Center Builds Delayed or Canceled in 2026
- **ソース:** Tom's Hardware / Reddit / WEF
- **公開日:** 2026-04-xx
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** 複数
- **要約:** 2026年に計画された米国データセンターの約半分が遅延またはキャンセル。Alphabet、Amazon、Meta、Microsoftは2026年に$6,500億以上の投資を計画。電力インフラと中国製部品の不足が制約。AIインフラを重要インフラとして扱うべきという議論。
- **キーファクト:**
  - 2026年計画DC: 約半数が遅延・キャンセル
  - Big 4投資計画: $6,500億以上（2026年）
  - 制約: 電力インフラ不足、中国製部品不足
  - WEF提言: AIインフラを重要インフラとして扱うべき
- **引用URL:** https://www.tomshardware.com/tech-industry/artificial-intelligence/half-of-planned-us-data-center-builds-have-been-delayed-or-canceled-growth-limited-by-shortages-of-power-infrastructure-and-parts-from-china-the-ai-build-out-flips-the-breakers

### INFO-032
- **タイトル:** EU AI Act Readiness - 78% of Enterprises Unprepared
- **ソース:** Vision Compliance / Corporate Compliance Insights
- **公開日:** 2026-04-xx
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** 2026年EU AI Act準備度調査: 企業の78%が義務に対応できていない。AI生成コンテンツの透かし義務が2026年11月2日に前倒し。適合性評価の第三者機関vs自己評価の選択肢、2026年8月の期限。
- **キーファクト:**
  - 未準備企業: 78%
  - 透かし義務発効: 2026年11月2日（前倒し）
  - 適合性評価期限: 2026年8月
  - 評価方法: 自己評価 vs 第三者機関
- **引用URL:** https://www.clarionledger.com/press-release/story/132138/vision-compliance-releases-2026-eu-ai-act-readiness-report-finds-78-of-enterprises-unprepared-for-obligations/

### INFO-033
- **タイトル:** 44 States Enact AI Laws as Federal Regulation Stalls
- **ソース:** TechStrong AI / Politico
- **公開日:** 2026-04-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** 連邦AI法が議会で停滞する中、44州が少なくとも1つのAI関連法を制定。州レベルのパッチワーク規制が進行。メンタルヘルスチャットボット、保険AI、子供の安全、ディープフェイク等をカバー。商務省は3月11日に州法評価を発表予定。
- **キーファクト:**
  - AI法制定州: 44州
  - 対象: メンタルヘルス、保険、子供の安全、ディープフェイク
  - 連邦法: 議会で停滞
  - 商務省評価: 2026年3月11日（「過度な」州法特定）
- **引用URL:** https://techstrong.ai/articles/states-defy-white-house-as-battle-over-ai-regulation-intensifies/

### INFO-034
- **タイトル:** Claude Code Source Code Leak Exploited for Malware Distribution
- **ソース:** Cyware Daily
- **公開日:** 2026-04-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** Claude Codeソースコードリークを悪用し、Vidar情報窃取マルウェアを配布する攻撃が出現。偽GitHubリポジトリ経由で配布。AnthropicのSOC2コンプライアンス違反の懸念が現実化。
- **キーファクト:**
  - 攻撃手法: 偽GitHubリポジトリでマルウェア配布
  - マルウェア: Vidar情報窃取型
  - 原因: Claude Codeソースコードリーク悪用
  - 影響: SOC2コンプライアンス違反の現実化
- **引用URL:** https://www.cyware.com/resources/threat-briefings/daily-threat-briefing/cyware-daily-threat-intelligence-april-03-2026

### INFO-035
- **タイトル:** GitHub Copilot vs Cursor 2026 - 5M+ Developers Served
- **ソース:** NxCode / GuruSup / LinkedIn
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft, Cursor
- **要約:** GitHub CopilotとCursorが2026年の主要AIコーディングツールとして500万人以上の開発者に利用。CopilotはVS Code・JetBrains・Neovimとのネイティブ統合で摩擦最小、Cursorはパワーユーザーと複雑プロジェクト向け。エンタープライズはAIコーディングツールに大きく投資。
- **キーファクト:**
  - 合計利用者: 500万人以上
  - Copilot: VS Code・JetBrains・Neovim統合、摩擦最小
  - Cursor: パワーユーザー向け、複雑プロジェクト対応
  - 企業投資: AIコーディングツールに大きく投資
- **引用URL:** https://www.nxcode.io/resources/news/github-copilot-vs-cursor-2026-which-ai-editor-worth-paying

### INFO-036
- **タイトル:** LinkedIn CEO: 5 Skills AI Can't Replace
- **ソース:** CNBC / LinkedIn
- **公開日:** 2026-03-31
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** LinkedIn CEOがAIが代替できない5つのスキルを提示。創造性、共感力、倫理的推論、複雑な判断、対人関係がAI時代に価値上昇。人間独自のスキルが非代替可能で、変動する雇用市場で若者に必要。
- **キーファクト:**
  - 非代替スキル: 創造性、共感力、倫理的推論、複雑な判断、対人関係
  - 市場価値: AI時代に上昇
  - 対象: 若手労働者に特に重要
  - 背景: 変動する雇用市場
- **引用URL:** https://www.cnbc.com/2026/03/31/ai-cant-replace-these-5-skills-says-linkedin-ceo-young-workers-need-them-now.html

### INFO-037
- **タイトル:** Coze AI Agent Platform 2026 - WeChat Integration Guide
- **ソース:** CSDN / Zhihu / GitHub
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** Coze（扣子）智能体平台の2026年最新ガイド。個人微信（WeChat）への接続方法、低コード/ゼロコードでのAIアプリ開発、AIカスタマーサービス構築を解説。自然言語対話で開発可能、学習コースも提供。
- **キーファクト:**
  - 機能: 微信接続、低コード/ゼロコード開発
  - 特徴: 自然言語対話で開発、閾値が低い
  - 用途: AIカスタマーサービス、スマートアプリ
  - 教育: ア炳老師のトレーニングコース提供
- **引用URL:** https://gitcode.csdn.net/69d0a2c50a2f6a37c59cec94.html

### INFO-038
- **タイトル:** Sam Altman vs Dario Amodei on AGI Timeline 2026
- **ソース:** Times of India / New Yorker / Instagram
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Anthropic
- **要約:** Sam AltmanがAGI到達を主張、AIエージェントが今年職場を変革すると予測。Dario Amodeiも急速な進展を認めるが、AGIの定義自体に合意がない。Altmanは2025年にAGIを「あまり有用な用語ではない」と発言。2026年のAGI予測は合意なき基盤の上にある。
- **キーファクト:**
  - Altman: AGI到達近い、エージェントが今年職場変革
  - Amodei: 急速な進展認めるが定義に合意なし
  - Altman 2025: 「AGIはあまり有用な用語ではない」
  - 問題: 2026年AGI予測は合意なき基盤上
- **引用URL:** https://timesofindia.indiatimes.com/technology/tech-news/what-sam-altman-said-is-the-goal-of-openai-anthropic-ceo-dario-amodei-complains-we-are-close-to-reaching-that-but-there-is-no/articleshow/129922151.cms

### INFO-039
- **タイトル:** Perplexity Comet - AI-Native Browser for Task Execution
- **ソース:** Till Freitag / Gamma
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** Perplexity
- **要約:** Perplexityが2025年7月にAIネイティブブラウザ「Comet」をローンチ。Chromiumベースで、受動的なブラウジングを能動的なタスク実行に変換。WhatsAppメッセージでタスクを実行するAIエージェントのプロトタイプも登場。
- **キーファクト:**
  - Comet: AIネイティブブラウザ、Chromiumベース
  - 機能: 受動的ブラウジング→能動的タスク実行
  - ローンチ: 2025年7月
  - WhatsAppエージェント: 1時間でプロトタイプ構築可能
- **引用URL:** https://till-freitag.com/en/blog/perplexity-comet-ai-browser

### INFO-040
- **タイトル:** AI Data Center Insurance Market Under Stress
- **ソース:** CNBC
- **公開日:** 2026-04-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** 複数
- **要約:** AIデータセンターブームが保険業界にストレスを与える。急速な技術進歩と巨額の資金流入が保険会社にリスクと報酬の両方をもたらす。プライベートキャピタルが殺到し、保険契約の複雑化。
- **キーファクト:**
  - 影響: 保険業界にストレス
  - 原因: 技術進歩の速さ、巨額資金流入
  - リスク/報酬: 保険会社に両方をもたらす
  - プライベートキャピタル: 大量流入
- **引用URL:** https://www.cnbc.com/2026/04/06/ai-data-centers-financing-insurance-deals-gpu-debt.html

### INFO-041
- **タイトル:** Claude Enterprise Security Compliance - SOC2, FedRAMP, ISO 27001
- **ソース:** Intuition Labs / Aikido / Facebook
- **公開日:** 2026-04-xx
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Enterpriseが主要セキュリティ認証（ISO 27001、SOC2、GDPR、HIPAA）をサポート。データは保管時・転送時に暗号化。FedRAMP認証を実装中。政府機関向けClaude for GovernmentもFedRAMP対応。1,000回のAIペンテストで過大なサイバーセキュリティリスクという神話を反証。
- **キーファクト:**
  - 認証: ISO 27001、SOC2、GDPR、HIPAA準拠
  - 暗号化: 保管時・転送時
  - FedRAMP: 実装中
  - AIペンテスト: 1,000回実施、リスクは過大視されていない
- **引用URL:** https://intuitionlabs.ai/articles/claude-vs-chatgpt-vs-copilot-vs-gemini-enterprise-comparison

### INFO-042
- **タイトル:** Llama 4 vs Gemma 4 vs Qwen 3.5 - Open Weight Model Comparison 2026
- **ソース:** LushBinary / Artificial Analysis
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, Google, Alibaba
- **要約:** 2026年の主要オープンウェイトモデル比較。Gemma 4 31BがMMLU Pro 85.2%、AIME 2026 89.2%、Codeforces 2150 ELO。Llama 4 MaverickとQwen 3.5 27Bと比較。オープンソースモデルと商用モデルのギャップが縮小。
- **キーファクト:**
  - Gemma 4 31B: MMLU Pro 85.2%、AIME 2026 89.2%、Codeforces 2150
  - Llama 4 Maverick: Gemma 4と比較可能
  - Qwen 3.5 27B: 競合モデル
  - 傾向: オープンソースと商用のギャップ縮小
- **引用URL:** https://www.lushbinary.com/blog/gemma-4-vs-llama-4-vs-qwen-3-5-open-weight-model-comparison/

### INFO-043
- **タイトル:** Anthropic Third-Party Tool Subscription Restriction
- **ソース:** Reddit
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Pro/Maxサブスクリプションのサードパーティツール内での使用を制限。直接的なAPI利用または公式アプリ経由のみに変更。エコシステムパートナーへの影響とベンダーロックインの懸念。
- **キーファクト:**
  - 制限: Claude Pro/Maxのサードパーティツール内使用禁止
  - 許可: 直接API利用、公式アプリ経由のみ
  - 影響: エコシステムパートナーへの影響
  - 懸念: ベンダーロックイン強化
- **引用URL:** https://www.reddit.com/r/AI_Agents/comments/1sbxshw/omg_anthropic_just_ended_claude_subscriptions_for/

### INFO-044
- **タイトル:** Oracle Layoffs Thousands While AI Spending Booms
- **ソース:** CNBC / Guardian
- **公開日:** 2026-03-31
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04
- **関連企業:** Oracle
- **要約:** Oracleが数千人規模のレイオフを実施しながらAI投資を急拡大。テック企業が人員削減とAI投資を同時に進行。一部企業は「AIウォッシュ」でレイオフを正当化している可能性。Challenger, Gray and Christmasの報告で92,000件のAI理由の人員削減。
- **キーファクト:**
  - Oracle: 数千人レイオフ、AI投資拡大
  - AI理由の人員削減: 92,000件（米国ベース）
  - テック業界: レイオフとAI投資の同時進行
  - 「AIウォッシュ」: レイオフの正当化にAIを利用する懸念
- **引用URL:** https://www.cnbc.com/2026/03/31/oracle-layoffs-ai-spending.html

### INFO-045
- **タイトル:** IASCA - International AI Safety Certification Authority Framework
- **ソース:** SSRN
- **公開日:** 2026-04-xx
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** 国際AI安全認証機関（IASCA）の枠組み提案。業界自主規制の失敗に対処し、条約ベースのガバナンス構造とキャプチャー防止条項を提案。AI安全性の国際認証制度の必要性。
- **キーファクト:**
  - 目的: 業界自主規制の失敗に対処
  - 構造: 条約ベースのガバナンス
  - 機能: キャプチャー防止条項
  - 対象: 国際AI安全認証制度
- **引用URL:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6240398

### INFO-046
- **タイトル:** 7 AI Agents That Actually Automate Workflows in 2026
- **ソース:** Gamma / Domino.ai
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** 複数
- **要約:** 2026年に実際にワークフローを自動化する7つのAIエージェント。タスク管理からマルチアプリワークフローまで、これらのツールが時間を節約し手動作業を削減。WhatsAppメッセージでタスクを実行するエージェントも登場。
- **キーファクト:**
  - 対象: タスク管理、マルチアプリワークフロー
  - 効果: 時間節約、手動作業削減
  - WhatsAppエージェント: メッセージでタスク実行
  - 自律AIエージェント時代の到来
- **引用URL:** https://gamma.app/nl/explore/content/guides/7-ai-agents-that-actually-help-you-automate-your-workflows-in-2026

### INFO-047
- **タイトル:** AI vs Human Intelligence - Comparing Strengths and Limits
- **ソース:** Intuit Blog / UTS Online
- **公開日:** 2026-04-xx
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** AIと人間知能の強みと限界の比較。AIが多くを担う中、最も価値のある人間スキルは代替困難で開発がより重要に。創造性、共感、倫理的推論、複雑な判断がAI時代に価値上昇。5つのAI代替不可能なキャリアパス。
- **キーファクト:**
  - 人間強み: 創造性、共感、倫理的推論、複雑な判断
  - 傾向: AI時代に価値上昇
  - 学習/適応: AIと人間で異なるアプローチ
  - キャリア: 5つのAI代替不可能な職種
- **引用URL:** https://www.intuit.com/blog/innovative-thinking/ai-vs-human-intelligence/

### INFO-048
- **タイトル:** ZTE Doubao AI Phone Coming Q2 2026
- **ソース:** Sina Finance / 36Kr / Jiemian
- **公開日:** 2026-03-31
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance, ZTE
- **要約:** 中興通訊が字節跳動と協力し新世代豆包AI携帯を開発。2026年第2四半期末発売予定。豆包がEC購入を代行するなど、大モデルが「実務時代」へ。豆包の「推奨」機能で話費チャージも可能。
- **キーファクト:**
  - パートナー: ZTE × ByteDance
  - 発売: 2026年Q2末
  - 機能: EC購入代行、推奨機能
  - 背景: 大モデルが「実務時代」へ移行
- **引用URL:** https://eu.36kr.com/zh/p/3746553942802953

### INFO-049
- **タイトル:** Amazon Bedrock AgentCore Gateway MCP Integration
- **ソース:** AWS ML Blog
- **公開日:** 2026-03-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-03
- **関連企業:** Amazon, AWS
- **要約:** AWS Bedrock AgentCore GatewayがMCPサーバー接続をサポート。OAuth認証コードフローで保護されたMCPサーバーに接続。エンタープライズ向けAIエージェント構築の柔軟性向上。
- **キーファクト:**
  - 機能: MCPサーバー接続
  - 認証: OAuth認証コードフロー
  - 対象: 保護されたMCPサーバー
  - 効果: エンタープライズAIエージェント構築の柔軟性向上
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/connecting-mcp-servers-to-amazon-bedrock-agentcore-gateway-using-authorization-code-flow/

### INFO-050
- **タイトル:** AI Agent Quality Assessment with AgentCore Evaluations GA
- **ソース:** AWS ML Blog
- **公開日:** 2026-03-xx
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon, AWS
- **要約:** Amazon Bedrock AgentCore Evaluationsが一般提供開始。AIエージェントの品質評価を開発ライフサイクル全体で自動化。信頼性の高いAIエージェント構築をサポート。
- **キーファクト:**
  - ステータス: 一般提供開始（GA）
  - 機能: AIエージェント品質評価の自動化
  - 対象: 開発ライフサイクル全体
  - 目的: 信頼性の高いAIエージェント構築
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/


## X (Twitter) 投稿データ（ローカルRSSHub経由）

### INFO-051
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Nathan Calvin
Appreciate that this recent "Industrial Policy for the Intelligence Age" doc is more frank about safety risks than many other OpenAI global affairs docs I've previously seen. 

As always though, I'll believe it when the attacks on Alex Bores from their Superpac stop
- **引用URL:** https://x.com/EthanJPerez/status/2041182492103946576

### INFO-052
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT 🚀Henry is leading AI Safety Research Programs
🚀 Applications are now open: Constellation's Astra Fellowship 🚀

Fully funded, 5-month fellowship at our Berkeley research institute. Pair with mentors across empirical AI safety research, strategy, and governance at @ConstellOrg!

📅 Apply by May 3rd (begins Sep 2026) 
🔗 https://www.constellation.org/programs/astra-fellowship
- **引用URL:** https://x.com/EthanJPerez/status/2041236906147823793

### INFO-053
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Pablo Torre 👀
👀

The New Yorker: .@RonanFarrow and @AndrewMarantz interviewed more than a hundred people with firsthand knowledge of how Sam Altman, the head of OpenAI, conducts business. They also obtained closely guarded documents that have not been previously disclosed.
https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted
- **引用URL:** https://x.com/EthanJPerez/status/2041236808860885159

### INFO-054
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Ronan Farrow
(🧵1/11) For the past year and a half, I've been investigating OpenAI and Sam Altman for @NewYorker. With my coauthor @andrewmarantz, I reviewed never-before-disclosed internal memos, obtained 200+ pages of documents related to a close colleague, including extensive private notes, and interviewed more than 100 people.

OpenAI was founded on the premise that A.I. could be the most dangerous invention in human history—and that its C.E.O. would need to be a person of uncommon integri...
- **引用URL:** https://x.com/EthanJPerez/status/2041232440015102015

### INFO-055
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT OpenAI
Introducing the OpenAI Safety Fellowship, a new program supporting independent research on AI safety and alignment—and the next generation of talent.

https://openai.com/index/introducing-openai-safety-fellowship/
- **引用URL:** https://x.com/EthanJPerez/status/2041232872846303425

### INFO-056
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Jeremy Slevin
OpenAI just put out a policy paper announcing their support for a 32-hour work week with no loss in pay and expanded Social Security, Medicare and Medicaid. 

Now they just need to stop spending hundreds of millions of dollars to defeat candidates who run on these policies!
- **引用URL:** https://x.com/EthanJPerez/status/2041233556962529606

### INFO-057
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Tomek Korbak
OpenAI is spinning up an AI safety research fellowship program similar to MATS or Anthropic Fellows. People should apply!

OpenAI: Introducing the OpenAI Safety Fellowship, a new program supporting independent research on AI safety and alignment—and the next generation of talent.

https://openai.com/index/introducing-openai-safety-fellowship/
- **引用URL:** https://x.com/EthanJPerez/status/2041270803782832344

### INFO-058
- **タイトル:** @sama (Sam Altman) のX投稿
- **ソース:** X (Twitter) - @sama (CEO)
- **公開日:** 2026-04-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Adrien Ecoffet
Proud to have been part of this. We outline policy ideas for the transition to superintelligence, to build an open economy where everyone benefits and a society that is resilient to the risks. Progress is fast, and we must navigate these issues urgently. https://openai.com/index/industrial-policy-for-the-intelligence-age/
- **引用URL:** https://x.com/sama/status/2041186468010545331

### INFO-059
- **タイトル:** @jasonkwon (Jason Kwon) のX投稿
- **ソース:** X (Twitter) - @jasonkwon (戦略担当)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Adrien Ecoffet
Proud to have been part of this. We outline policy ideas for the transition to superintelligence, to build an open economy where everyone benefits and a society that is resilient to the risks. Progress is fast, and we must navigate these issues urgently. https://openai.com/index/industrial-policy-for-the-intelligence-age/
- **引用URL:** https://x.com/jasonkwon/status/2041183648494588327

### INFO-060
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-04-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** Let’s talk about building with Codex.

Join @ryannystrom, @derrickcchoi and @varunrau for a chat about Codex workflows, from exploring feature ideas to shipping together as a team.

https://x.com/i/spaces/1YxNrZDqrOLxw
- **引用URL:** https://x.com/OpenAIDevs/status/2041247305286996373

### INFO-061
- **タイトル:** @markchen90 (Mark Chen) のX投稿
- **ソース:** X (Twitter) - @markchen90 (研究責任者)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** We’re excited to launch the OpenAI Safety Fellowship - supporting rigorous, independent research on AI safety and alignment, including areas like evaluation, robustness, and scalable mitigations.

Applications are open through May 4, 2026!

OpenAI: Introducing the OpenAI Safety Fellowship, a new program supporting independent research on AI safety and alignment—and the next generation of talent.

https://openai.com/index/introducing-openai-safety-fellowship/
- **引用URL:** https://x.com/markchen90/status/2041250842255425767

### INFO-062
- **タイトル:** @markchen90 (Mark Chen) のX投稿
- **ソース:** X (Twitter) - @markchen90 (研究責任者)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT OpenAI
Introducing the OpenAI Safety Fellowship, a new program supporting independent research on AI safety and alignment—and the next generation of talent.

https://openai.com/index/introducing-openai-safety-fellowship/
- **引用URL:** https://x.com/markchen90/status/2041250745568399819

### INFO-063
- **タイトル:** @jasonkwon (Jason Kwon) のX投稿
- **ソース:** X (Twitter) - @jasonkwon (戦略担当)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Mark Chen
We’re excited to launch the OpenAI Safety Fellowship - supporting rigorous, independent research on AI safety and alignment, including areas like evaluation, robustness, and scalable mitigations.

Applications are open through May 4, 2026!

OpenAI: Introducing the OpenAI Safety Fellowship, a new program supporting independent research on AI safety and alignment—and the next generation of talent.

https://openai.com/index/introducing-openai-safety-fellowship/
- **引用URL:** https://x.com/jasonkwon/status/2041285392234590465

### INFO-064
- **タイトル:** @jasonkwon (Jason Kwon) のX投稿
- **ソース:** X (Twitter) - @jasonkwon (戦略担当)
- **公開日:** 2026-04-07
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT prinz
Re For those who are not interested in falling for this obvious bait, here is some actual information about OpenAI's safety practices:

1. OpenAI has a comprehensive Preparedness Framework in place, which is used to track and respond to critical AI safety risks. It's available here: https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf

2. With each major model release, OpenAI publishes a comprehensive system card that shows the safety evals perfo...
- **引用URL:** https://x.com/jasonkwon/status/2041282533959118858

