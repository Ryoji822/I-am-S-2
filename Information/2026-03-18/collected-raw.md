# 収集データ: 2026-03-18

## メタデータ
- 収集日時: 2026-03-18 00:00 UTC
- 品質フラグ: COLLECTING
- 動的追加クエリ（Arbiter指示）:
  - KIQ-RED-006: Claude Code解約率・Fortune 500導入率
  - KIQ-RED-005: AI導入ROI定義詳細
  - KIQ-GOO-001: Google仮説の反証証拠
  - KIQ-NEW-SDK: 5社SDK囲い込み度合い（API互換性、データ移植性、ロックイン機能）

## 収集結果

### INFO-001
- **タイトル:** Anthropic acquires Bun as Claude Code reaches $1B milestone
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-12-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Claude Codeが一般公開から6ヶ月で$1B ARR（年間経常収益）を達成。AnthropicはJavaScriptランタイムBunを買収し、Claude Codeのインフラを強化。Netflix、Spotify、KPMG、L'Oreal、Salesforce等が採用。
- **キーファクト:**
  - Claude Code: 一般公開(May 2025)から6ヶ月で$1B ARR達成
  - Bun買収: JavaScript/TypeScript開発体験を統合
  - 企業採用: Netflix, Spotify, KPMG, L'Oreal, Salesforce等
  - Bun月間700万ダウンロード、GitHub 82,000スター
- **引用URL:** https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone

### INFO-002
- **タイトル:** From model to agent: Equipping the Responses API with a computer environment
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-03-11
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIがResponses APIにコンピュータ環境（shell tool + ホストコンテナ）を統合。エージェントがファイルシステム、データベース、制御されたネットワークアクセスを利用可能に。Skillsによる再利用可能なワークフローのパッケージ化も提供。
- **キーファクト:**
  - Shell tool: PythonだけでなくGo/Java/NodeJS等も実行可能
  - ホストコンテナ: ファイルシステム、SQLite、制御されたネットワーク
  - Agent Skills: 再利用可能なワークフローのパッケージ化
  - Context Compaction: 長時間実行タスク向けのコンテキスト圧縮機能
- **引用URL:** https://openai.com/index/equip-responses-api-computer-environment/

### INFO-003
- **タイトル:** Introducing GPT-5.4
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-03-05
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-02, KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.4をリリース。フロンティアモデルの最新版。
- **キーファクト:**
  - GPT-5.4: 最新フロンティアモデル
  - 2026年3月5日発表
- **引用URL:** https://openai.com/index/introducing-gpt-5-4/

### INFO-004
- **タイトル:** Introducing GPT-5.4 mini and nano
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-03-17
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-02, KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.4の小型版miniとnanoをリリース。エッジデバイス向けの軽量モデル。
- **キーファクト:**
  - GPT-5.4 mini/nano: 軽量版モデル
  - 2026年3月17日発表
- **引用URL:** https://openai.com/news/company-announcements/

### INFO-005
- **タイトル:** Codex Security: now in research preview
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-03-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAIがCodex Securityをリサーチプレビューとしてリリース。セキュリティ分析向けのエージェント機能。
- **キーファクト:**
  - Codex Security: セキュリティ分析向けエージェント
  - リサーチプレビュー段階
- **引用URL:** https://openai.com/index/codex-security-now-in-research-preview/

### INFO-006
- **タイトル:** OpenAI to acquire Promptfoo
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-03-09
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-04, KIQ-001-03
- **関連企業:** OpenAI
- **要約:** OpenAIがPromptfoo（プロンプトテスト・評価ツール）の買収を発表。開発者エコシステムの強化。
- **キーファクト:**
  - Promptfoo買収: プロンプトテスト・評価ツール
  - 開発者ツールエコシステムの拡充
- **引用URL:** https://openai.com/index/openai-to-acquire-promptfoo/

### INFO-007
- **タイトル:** Measuring progress toward AGI: A cognitive framework
- **ソース:** Google DeepMind (公式ブログ)
- **公開日:** 2026-03-17
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-01, KIQ-005-03
- **関連企業:** Google / DeepMind
- **要約:** Google DeepMindがAGI進捗測定のための認知フレームワークを発表。10の認知能力を定義し、Kaggleハッカソン（$200,000賞金）を開催。
- **キーファクト:**
  - 10の認知能力: 知覚、生成、注意、学習、記憶、推論、メタ認知、実行機能、問題解決、社会認知
  - Kaggleハッカソン: $200,000賞金プール
  - 3段階評価プロトコル: AI評価、人間ベースライン、相対マッピング
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/

### INFO-008
- **タイトル:** The Check Up with Google 2026
- **ソース:** Google (公式ブログ)
- **公開日:** 2026-03-17
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-04, KIQ-005-01
- **関連企業:** Google / DeepMind
- **要約:** Google年次ヘルスイベントThe Check Up 2026。医療AIの進展を発表。$10Mの臨床医AIトレーニング投資、Fitbit Personal Health Coach、MedGemma等。
- **キーファクト:**
  - $10M投資: 臨床医AIトレーニング
  - Fitbit Personal Health Coach: 個人健康エージェント
  - MedGemma: 医療画像・テキスト解釈モデル
  - AMIE: マルチモーダル診断対話AI（臨床研究段階）
- **引用URL:** https://blog.google/innovation-and-ai/technology/health/google-health-check-up-2026/

### INFO-009
- **タイトル:** Platform 37 and The AI Exchange
- **ソース:** Google (公式ブログ)
- **公開日:** 2026-03-12
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-03
- **関連企業:** Google / DeepMind
- **要約:** Google DeepMindの新拠点Platform 37がロンドンKing's Crossに開設。AI Exchange（AI理解を深める公共スペース）を併設。Demis Hassabisがブログで発表。
- **キーファクト:**
  - Platform 37: King's Cross新拠点、2026年夏入居開始
  - AI Exchange: AI理解向け公共スペース（無料教育プログラム、展示）
  - 名称由来: AlphaGo Move 37（2016年）
- **引用URL:** https://blog.google/company-news/inside-google/around-the-globe/google-europe/united-kingdom/platform-37-the-ai-exchange/

### INFO-010
- **タイトル:** OpenAI agreement with the Department of War (Pentagon)
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-02-28
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI
- **要約:** OpenAIが米国防総省（Department of War）との提携を発表。軍事関連の政府契約進出。
- **キーファクト:**
  - Department of War（国防総省）との契約
  - 政府市場への本格進出
- **引用URL:** https://openai.com/index/our-agreement-with-the-department-of-war/

### INFO-011
- **タイトル:** OpenAI and Amazon announce strategic partnership
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-02-27
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-01
- **関連企業:** OpenAI, Amazon
- **要約:** OpenAIとAmazonが戦略的パートナーシップを発表。Amazon BedrockでのStateful Runtime Environment for Agentsも同時発表。
- **キーファクト:**
  - OpenAI-Amazon戦略的パートナーシップ
  - Bedrock上のStateful Runtime Environment for Agents
  - クラウド統合の深化
- **引用URL:** https://openai.com/index/amazon-partnership/

### INFO-012
- **タイトル:** Claude Code v2.1.76 - Major Update with MCP Elicitation, 1M Context
- **ソース:** Anthropic (公式Changelog)
- **公開日:** 2026-03-14
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Claude Code v2.1.76がリリース。MCP elicitationサポート、Opus 4.6で1M context window（Max/Team/Enterprise）、/loopコマンド、cron scheduling等の新機能。
- **キーファクト:**
  - MCP elicitation: MCPサーバーがタスク中に構造化入力を要求可能に
  - Opus 4.6: 全プランで1M context window標準化
  - /loopコマンド: 定期実行プロンプト（例: `/loop 5m check the deploy`）
  - Voice STT: 20言語対応（ロシア語、ポーランド語等10言語追加）
- **引用URL:** https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

### INFO-013
- **タイトル:** xAI Grok 4.20 Multi-Agent Beta Released
- **ソース:** xAI (公式ドキュメント)
- **公開日:** 2026-03-12
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** xAI
- **要約:** xAIがGrok 4.20 Multi-Agent Betaをリリース。複数AIエージェントが協調して深いリサーチタスクを実行。4エージェント/16エージェント構成が可能。
- **キーファクト:**
  - モデル名: grok-4.20-multi-agent-beta-0309
  - 4エージェント（low/medium effort）/ 16エージェント（high/xhigh effort）
  - web_search、x_search、code_execution等のビルトインツール対応
  - 2M context window
- **引用URL:** https://docs.x.ai/developers/model-capabilities/text/multi-agent

### INFO-014
- **タイトル:** Alibaba launches Wukong AI platform for enterprises
- **ソース:** Reuters / Economic Times
- **公開日:** 2026-03-17
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Alibaba
- **要約:** Alibabaがエンタープライズ向けAIエージェントプラットフォーム「Wukong」を発表。複数AIエージェントが協調してドキュメント編集、スプレッドシート更新、会議議事録、リサーチ等を処理。招待制ベータテスト中。
- **キーファクト:**
  - Wukong: Alibaba Token Hub (ATH)配下のWukong Business Unitが開発
  - DingTalk統合: 2,000万以上の法人ユーザー
  - Slack、Microsoft Teams、WeChat連携予定
  - 中国でOpenClaw（オープンソースAIエージェントツール）ブームが進行中
- **引用URL:** https://m.economictimes.com/tech/artificial-intelligence/alibaba-launches-ai-platform-for-enterprises-as-agent-craze-sweeps-china/amp_articleshow/129631965.cms

### INFO-015
- **タイトル:** ByteDance DeerFlow 2.0 Open Source Agent Framework
- **ソース:** LinkedIn / GitHub
- **公開日:** 2026-03-14
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceが内部AIエージェントシステム「DeerFlow 2.0」をオープンソース化。GitHub 25Kスター、トレンド1位達成。各エージェントに専用コンピュータ環境を割り当て。
- **キーファクト:**
  - DeerFlow 2.0: オープンソーススーパーエージェント
  - 25K GitHubスター、トレンド1位
  - マルチエージェントオーケストレーション、メモリ、サンドボックス
  - リサーチ、コーディング、ウェブサイト構築、動画生成が可能
- **引用URL:** https://www.linkedin.com/posts/lioralex_bytedance-just-gave-each-agent-its-own-computer-activity-7438539641101844481-Fhf9

### INFO-016
- **タイトル:** Top 7 AI Agent Orchestration Frameworks 2026
- **ソース:** KDnuggets
- **公開日:** 2026-03-12
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** 複数
- **要約:** 2026年の主要AIエージェントオーケストレーションフレームワーク7選。LangGraph、CrewAI、Pydantic AI、Google ADK、AutoGen、Semantic Kernel、LlamaIndex Agent Workflow。
- **キーファクト:**
  - LangGraph: グラフベース、状態管理、永続性
  - CrewAI: ロールベース、シンプルで本番運用向け
  - Pydantic AI: 型安全性、MCP/A2A標準対応
  - Google ADK: Vertex AI統合、エンタープライズ向け
  - AutoGen: Microsoft Research、会話型エージェント
  - Semantic Kernel: Azure統合、プラグインアーキテクチャ
  - LlamaIndex: RAG特化、イベント駆動
- **引用URL:** https://www.kdnuggets.com/top-7-ai-agent-orchestration-frameworks
