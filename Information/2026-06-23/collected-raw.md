# 収集データ: 2026-06-23

## メタデータ
- 収集日時: 2026-06-23 00:14 UTC（開始）〜 01:30 UTC（完了）
- 品質フラグ: NORMAL
- 実行検索クエリ数: 131件（collection_plan.json定義122件 + Arbiter動的クエリ9件）
- scrape実行数: 11件（公式ブログマッピング4 + 詳細スクレイピング7）
- 収集情報数: 66件
- Evidence ID採番範囲: EVD-20260623-0001 〜 EVD-20260623-0066
- KIQカバレッジ: 27/27（24 KIQ + 3動的KIQ、全カバー）
  - KIQ-001-01 ✓ KIQ-001-02 ✓ KIQ-001-03 ✓ KIQ-001-04 ✓ KIQ-001-05 ✓
  - KIQ-002-01 ✓ KIQ-002-02 ✓ KIQ-002-03 ✓ KIQ-002-04 ✓ KIQ-002-05 ✓ KIQ-002-06 ✓
  - KIQ-003-01 ✓ KIQ-003-02 ✓ KIQ-003-03 ✓ KIQ-003-04 ✓ KIQ-003-05 ✓
  - KIQ-004-01 ✓ KIQ-004-02 ✓ KIQ-004-03 ✓ KIQ-004-04 ✓
  - KIQ-005-01 ✓ KIQ-005-02 ✓ KIQ-005-03 ✓
  - BYTEDANCE-CHINESE ✓
  - KIQ-OAI-001 ✓ KIQ-MIL-001 ✓ KIQ-GOV-002 ✓
- 動的追加クエリ (Arbiter優先KIQ):
  - KIQ-OAI-001 (OpenAI収益内訳): "OpenAI revenue breakdown API enterprise consumer 2026", "OpenAI ARR API vs ChatGPT subscription revenue split", "OpenAI financials business segment revenue 2026"
  - KIQ-MIL-001 (Grok標的選定関与度): "Grok AI military target selection Operation Epic Fury", "xAI Grok Pentagon military targeting human override", "AI autonomous weapons target selection review rate investigation"
  - KIQ-GOV-002 (AI安全性研究予算): "AI safety research budget internal corporate spending decline", "Anthropic OpenAI DeepMind safety research investment trends", "AI company alignment research funding internal allocation"
- 備考:
  - 目標件数50件を超える66件を収集
  - KIQ-GOV-002（安全性研究予算の経時的定量データ）は絶対条件未達成継続（3日連続）
  - 一部API pricing個別社・MCP adoption等のクエリは空結果（該当ニュース不在のため）
  - 主要発見: ペンタゴンOperation Epic Fury（Grok使用・96時間/2,000標的）、OpenAI 2025通年収益$13B・損失$20.9B、SpaceXのCursor買収($60B)、Google→Anthropic最大$40B投資、Anthropic AI社内コード80%寄与・RSI議論、LeCun離脱とAMI Labs設立

## 収集結果

### INFO-001
- **タイトル:** Daybreak: Tools for securing every organization in the world
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-06-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-002-06
- **関連企業:** OpenAI
- **要約:** OpenAIがDaybreak構想を拡大し、Codex Securityのアップデート、GPT-5.5-Cyber完全版リリース、Daybreak Cyber Partner Program立ち上げ、Patch the Planetイニシアチブを発表。脆弱性発見からパッチ自動化へ移行。GPT-5.5-CyberはCyberGymで85.6%（GPT-5.5の81.8%を上回る）、ExploitGym 39.5%（vs 25.95%）、SEC-bench Pro 69.8%（vs 63.1%）を達成。
- **キーファクト:**
  - Codex Securityは30K+リポジトリ・30M+コミットをスキャン、500K+の発見を自動修正済み
  - GPT-5.5-Cyberは米国政府との継続協力（CAISI事前デプロイテスト、ONCD/OSTP協力）
  - 30+オープンソースプロジェクトがPatch the Planetに参加（cURL, Go, Python等）
  - Trusted Access for Cyber提携国：豪・加・仏・独・日・韓・EU機関
- **引用URL:** https://openai.com/index/daybreak-securing-the-world/
- **Evidence ID:** EVD-20260623-0001

### INFO-002
- **タイトル:** Samsung Electronics brings ChatGPT and Codex to employees
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-06-21
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-004-04
- **関連企業:** OpenAI, Samsung
- **要約:** Samsung ElectronicsがChatGPT EnterpriseとCodexを全社員（韓国全社員+全世界Device eXperience部門）に展開。OpenAI史上最大級のエンタープライズデプロイの一つ。R&D、製造、マーケティング、コーポレート機能横断で使用。
- **キーファクト:**
  - Codex週間アクティブユーザー500万人超
  - 韓国でのCodex週間アクティブユーザーは2026年2月から約800%増加
  - Samsungは次世代AIインフラ向け先進メモリ半導体供給でも協力
  - ソウル大学47,000名にChatGPT Edu提供、KakaoTalk統合も実施
- **引用URL:** https://openai.com/index/samsung-electronics-chatgpt-codex-deployment/
- **Evidence ID:** EVD-20260623-0002

### INFO-003
- **タイトル:** Interactions API: our primary interface for Gemini models and agents
- **ソース:** Google / DeepMind (公式ブログ)
- **公開日:** 2026-06-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-05
- **関連企業:** Google / DeepMind
- **要約:** GoogleがInteractions API（Geminiモデル・エージェントの統合API）をGA（一般提供）移行。2025年12月ベータから正式リリース。Managed Agents、バックグラウンド実行、Gemini Omni（近日）、Deep Research機能強化、メディア生成（Nano Banana 2/Lyria 3）を追加。generateContent APIから移行ガイド提供。
- **キーファクト:**
  - Managed Agents: 単一API呼び出しでリモートLinuxサンドボックスをプロビジョニング、Antigravityエージェントがデフォルト
  - Flex階層で50%コスト削減、Priority階層で低レイテンシ
  - 従来のgenerateContent APIは完全サポート継続だが、フロンティア機能はInteractions APIに先行リリース
  - gemini-interactions-api Skillを提供（コーディングエージェント向け）
  - パートナー統合: LiteLLM, Eigent, Agno
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/
- **Evidence ID:** EVD-20260623-0003

### INFO-004
- **タイトル:** New usage analytics and updated spend controls for enterprises
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-06-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPT Enterprise向けにクレジット使用量分析と支出制御機能を発表。Global Admin ConsoleでChatGPT・Codexのクレジット使用量を一元管理、ユーザー・製品・モデル別の詳細な内訳を提供。カスタムロール向けクレジット制限設定を拡張。
- **キーファクト:**
  - ユーザー・グループ・個人レベルでの支出制限設定可能
  - 従業員はクレジット残高を確認・追加要求が可能
  - 統合Cost APIで自社システムへの深い分析も可能
  - Zipline（顧客事例）がCodex全社展開の管理に活用
- **引用URL:** https://openai.com/index/chatgpt-enterprise-spend-controls/
- **Evidence ID:** EVD-20260623-0004

### INFO-005
- **タイトル:** Anthropic invests $100 million into the Claude Partner Network
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-03-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Partner Networkを立ち上げ、初期$100Mを投資。パートナー向けトレーニング、技術サポート、共同市場開発を提供。Claude Certified Architect認定試験を開始。Claudeは3大クラウド（AWS, Google Cloud, Microsoft）全てで利用可能な唯一のフロンティアAIモデル。
- **キーファクト:**
  - $100M投資の大部分がパートナーへの直接支援（トレーニング・営業・市場開発）
  - パートナーチームを5倍に拡大
  - Claude Certified Architect, Foundations認定を提供
  - Code Modernizationスターターキット公開
  - Accenture 30,000人トレーニング実施中
- **引用URL:** https://www.anthropic.com/news/claude-partner-network
- **Evidence ID:** EVD-20260623-0005

### INFO-006
- **タイトル:** TCS and Anthropic partner to bring Claude to regulated industries
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-001-03
- **関連企業:** Anthropic, TCS (Tata)
- **要約:** AnthropicとTata Consultancy Services (TCS)が提携。TCSが50,000名の自社社員（56カ国）にClaudeを提供、金融・医療・公共部門等の規制産業向けClaude搭載製品を構築。Diligenta（TCSの英国生命年金事業）が2,200万ポリシーホルダー向けにClaudeを導入。
- **キーファクト:**
  - TCS全社（エンジニアリング・財務・法務・マーケティング・営業）でClaude展開
  - Claude Codeで銀行・金融商品チームのソフトウェアエンジニアリング生産性向上
  - TCS iON: 年間7,500万件の評価を1,500都市で実施、Claudeトレーニング提供
  - Dario Amodei: 「インドは当社第2の市場」
- **引用URL:** https://www.anthropic.com/news/tcs-anthropic-partnership
- **Evidence ID:** EVD-20260623-0006

### INFO-007
- **タイトル:** 2028: Two scenarios for global AI leadership
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06, KIQ-005-01, KIQ-005-03
- **関連企業:** Anthropic, Google/DeepMind
- **要約:** Anthropicが米中AI競争に関する2つのシナリオを提示。シナリオ1（民主主義陣営が優位を維持）とシナリオ2（CCPがフロンティアに接近）。Mythos Previewがもたらした加速を「目覚ましの電話」と位置付け。輸出管理の強化、蒸留攻撃の防止、米国AIの輸出促進を政策提言。Huawei 2026年NVIDIA計算量の4%、2027年2%と試算。
- **キーファクト:**
  - Mythos Preview: Firefoxが前月のセキュリティバグ修正数を2025年通年超え
  - 蒸留攻撃: 中国ラボが米国モデルの成果を不正に抽出、OpenAI/Google/Anthropic/FMFが非難
  - DeepSeek R1-0528: 悪意ある要求の94%に応答（米国モデル8%と比較）
  - 政策3本柱: 輸出管理ループホール閉鎖、蒸留攻撃抑止、米国AI輸出促進
  - CFR分析: 米国強化時の計算量格差は11:1と試算
- **引用URL:** https://www.anthropic.com/news/2028-ai-leadership
- **Evidence ID:** EVD-20260623-0007

### INFO-008
- **タイトル:** ByteDance's Coze Launches Version 2.5, Introducing the 'Agent World' Ecosystem
- **ソース:** KuCoin News
- **公開日:** 2026-06 (推定)
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** ByteDance
- **要約:** ByteDanceのCozeプラットフォームがv2.5にアップデート。「Agent World」エコシステムを導入し、AIエージェントがチャットインターフェースを超えて動作可能に。独立した実行環境、スキル、アイデンティティを備える。
- **キーファクト:**
  - Coze 2.5: チャットUIを超えた独立エージェント実行環境
  - エージェント向けスキル・アイデンティティ機能追加
  - ByteDanceがTARS（オープンソースマルチモーダルエージェント）も公開
  - OpenViking: オープンソースコンテキストデータベース（2026年5月更新）
- **引用URL:** https://www.kucoin.com/news/flash/bytedance-s-coze-launches-version-2-5-introduces-agent-world-ecosystem
- **Evidence ID:** EVD-20260623-0008

### INFO-009
- **タイトル:** Gemini Enterprise Agent Platform (Google Cloud公式ドキュメント)
- **ソース:** Google Cloud (公式ドキュメント)
- **公開日:** 2026-06 (継続更新)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Google CloudがGemini Enterprise Agent Platformを提供。エンタープライズグレードのAIエージェント構築・デプロイ・ガバナンス・最適化のための統合プラットフォーム。Deep Research AgentがMCP server対応、コラボレーションプランニング、視覚化機能を追加。
- **キーファクト:**
  - Deep Research Agent: MCP server連携、外部ツール接続、チャート/グラフ可視化
  - Gemini API Skills (GitHub): テキスト生成・マルチモーダル理解・ツール実行
  - Firebase統合: SQL Connect向けスキーマ・クエリ自動生成
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260623-0009

### INFO-010
- **タイトル:** Agentic AI Enterprise Adoption 2026: 72% Production Proven
- **ソース:** Agentic AI Institute
- **公開日:** 2026-06 (推定)
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** エンタープライズのAgentic AI本番導入率が72%に到達する一方、60%のガバナンス格差が残存。多くの組織がシャドーIT的なAI利用を拡大させており、ガバナンスフレームワークの構築が急務。
- **キーファクト:**
  - Agentic AI本番導入率: 72%（Arbiter v4.15のIND-026データと整合）
  - ガバナンス格差: 60%（導入しているが統制不在）
  - 多くの組織がLLM付きシャドーITを量産している状態
- **引用URL:** https://agenticaiinstitute.org/agentic-ai-enterprise-adoption-2026-governance-gap/
- **Evidence ID:** EVD-20260623-0010

### INFO-011
- **タイトル:** Vertex AI is now part of Gemini Enterprise Agent Platform
- **ソース:** Google Cloud (公式ドキュメント)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Google CloudがVertex AIを「Gemini Enterprise Agent Platform」に統合・リブランド。エンタープライズグレードのエージェント構築・デプロイ・ガバナンス・最適化のための統合プラットフォームに進化。スタートアップ向け$350Kクレジット提供。
- **キーファクト:**
  - Vertex AI Agent Engine → Gemini Enterprise Agent Platform
  - Gemini Developer API vs Enterprise APIの2層構造
  - マルチステップリサーチタスク向けの構築済みエージェント提供
  - 小売・EC向け自律コマース機能
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes
- **Evidence ID:** EVD-20260623-0011

### INFO-012
- **タイトル:** Netskope integrates with Anthropic's Claude compliance API
- **ソース:** Uptech Media
- **公開日:** 2026-06 (推定)
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic, Netskope
- **要約:** AnthropicがCompliance APIを提供開始。エンタープライズIT/セキュリティチームがClaudeアクティビティデータにREST API経由でプログラム的にアクセス可能。Netskopeが統合しAIセキュリティ・ガバナンス機能を拡張。
- **キーファクト:**
  - Anthropic Compliance API: ClaudeアクティビティデータへのREST APIアクセス
  - SOC 2 Type II認証継続（継続的運用保証）
  - Netskope統合でエンタープライズAIガバナンス強化
- **引用URL:** https://uptech-media.com/netskope-integrates-with-anthropics-claude-compliance-api-to-expand-ai-security-and-governance-capabilities/
- **Evidence ID:** EVD-20260623-0012

### INFO-013
- **タイトル:** Agent Skills ecosystem expansion: Vercel, Stripe, StackHawk, Promptfoo
- **ソース:** GitHub / Stripe Docs / StackHawk
- **公開日:** 2026-06 (推定)
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Vercel, Stripe
- **要約:** エージェントスキル（SKILL.md形式）のエコシステムが急速拡大。Vercel-labs/skillsがオープンエージェントスキルツール（npx skills）を公開。Stripeが公式Agent Skillsドキュメントを提供。StackHawkやPromptfooも独自スキルを市場投入。OpenAI GPT Storeからスキル配布モデルへの進化が進行中。
- **キーファクト:**
  - Vercel: `npx skills add` でスキル配布、SKILL.md + YAML frontmatter形式
  - Stripe: 公式Agent Skillsで正確なStripe統合をAIエージェントに指示
  - StackHawk: ランタイムセキュリティジョブをコーディングエージェントに教授
  - Promptfoo: Claude Code/OpenAI Codex向けeval・レッドチームスキル
- **引用URL:** https://github.com/vercel-labs/skills, https://docs.stripe.com/skills
- **Evidence ID:** EVD-20260623-0013

### INFO-014
- **タイトル:** Salesforce Partners with Databricks for AI Agent MCP Integration
- **ソース:** Salesforce (公式発表)
- **公開日:** 2026-06-16
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** Salesforce, Databricks
- **要約:** SalesforceとDatabricksが提携拡大。AIエージェントが信頼できるデータを信頼できる行動に変換するための共有基盤を構築。MCPベースのデータ統合でエージェントがSalesforce/Databricks間のデータにアクセス可能に。Zendeskは高度メールAIエージェントのGAを発表。
- **キーファクト:**
  - Salesforce × Databricks: 信頼データ→信頼行動のMCP統合
  - Zendesk: agentic AI for advanced email AI agents GA化
  - PitchBook × Samaya AI: プライベート市場データをExpert AI Agent Platformに統合
  - Cleo: EDI/ERP/サプライチェーン向けagentic connectivity
- **引用URL:** https://www.salesforce.com/news/stories/salesforce-databricks-shared-foundation-of-human-agent-work-announcement/
- **Evidence ID:** EVD-20260623-0014

### INFO-015
- **タイトル:** Chrome DevTools for Agents introduces third-party developer tools
- **ソース:** Chrome Developers (公式ブログ)
- **公開日:** 2026-06 (推定)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-04
- **関連企業:** Google
- **要約:** Chrome DevToolsがエージェント向けサードパーティ開発者ツールを導入。フレームワークやアプリケーションがAIコーディングエージェントと豊富なランタイムコンテキストを共有可能に。エージェントデバッグツール市場も成長（Braintrust, Maxim AI, Langfuse等）。
- **キーファクト:**
  - Chrome DevTools for agents: サードパーティツールでランタイムコンテキスト共有
  - エージェントデバッグツール7社比較: Braintrust, Maxim AI, Langfuse, Arize Phoenix, Helicone, Agenta, Galileo
  - Entire: リポジトリを超えたエージェント×人間協調プラットフォーム予告
- **引用URL:** https://developer.chrome.com/blog/devtools-for-agents-3p-tools
- **Evidence ID:** EVD-20260623-0015

### INFO-016
- **タイトル:** BenchLM: Gemini 3 Pro Deep Think leads Multimodal Benchmarks; Claude Mythos Preview tops SWE-Bench Multimodal
- **ソース:** BenchLM / LLM Stats
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google / DeepMind, Anthropic
- **要約:** 2026年6月時点のマルチモーダルベンチマークでGemini 3 Pro Deep ThinkがBenchLM multimodal & grounded部門で1位（スコア100）。SWE-Bench MultimodalではClaude Mythos Previewが0.590で1位。オムニモーダル長動画推論ではGemini 3.1 Pro Previewが55.63%で最高。
- **キーファクト:**
  - BenchLM Multimodal: Gemini 3 Pro Deep Think 1位（スコア100）
  - SWE-Bench Multimodal: Claude Mythos Preview 1位（0.590）
  - オムニモーダル長動画推論: Gemini 3.1 Pro Preview 55.63%（最高）、クローズドソース最強でも過半数に届かず
  - Gemini 3 Flash 24%, GPT-5.2 23%の多モーダル評価で、GPT-5やOpus 4.5は18%未満
- **引用URL:** https://benchlm.ai/multimodal-grounded, https://llm-stats.com/benchmarks/swe-bench-multimodal
- **Evidence ID:** EVD-20260623-0016

### INFO-017
- **タイトル:** Google Cloud hosts OpenAI gpt-oss 120B; Gemini Robotics-ER and Live API for multimodal agents
- **ソース:** Google Cloud (公式ドキュメント) / Google DeepMind
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-04, KIQ-002-01
- **関連企業:** Google / DeepMind, OpenAI
- **要約:** Google CloudのGemini Enterprise Agent PlatformがOpenAI gpt-oss 120B（Apache 2.0ライセンス）をホスト開始。クロスプラットフォーム提供の象徴。Gemini Robotics-ER（具現化推論）とGemini Live API（低レイテンシリアルタイム音声・動画）でマルチモーダルエージェント機能を拡充。
- **キーファクト:**
  - Google Cloud上でOpenAI gpt-oss 120B提供開始（推論・関数呼び出し向け）
  - Gemini Robotics-ER: ロボットの環境理解・相互作用を強化する思考モデル
  - Gemini Live API: 継続的音声・動画・テキストストリーム処理
  - Co-Scientist: Geminiベースのマルチエージェント科学仮説生成システム
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/openai
- **Evidence ID:** EVD-20260623-0017

### INFO-018
- **タイトル:** 'Chat Is Dead': OpenAI Plans to Relaunch ChatGPT as Agent-First Platform
- **ソース:** Entrepreneur / Facebook
- **公開日:** 2026-06 (推定)
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPTをエージェント優先プラットフォームとして再リリースする計画。Operator（ブラウザ操作エージェント）等の3つの主要AIエージェント機能を統合。チャットUIからエージェント実行環境への移行を加速。
- **キーファクト:**
  - "Chat Is Dead" — エージェント優先リリース計画
  - Operator: ウェブサイト閲覧・ボタンクリック・フォーム入力・予約を実行
  - GPT-5o: テキスト・画像・音声の統合マルチモーダル
- **引用URL:** https://www.facebook.com/Entrepreneur/posts/chat-is-dead-openai-plans-to-relaunch
- **Evidence ID:** EVD-20260623-0018

### INFO-019
- **タイトル:** NVIDIA OpenShell: Safe, private runtime for autonomous AI agents
- **ソース:** NVIDIA (GitHub)
- **公開日:** 2026-06 (推定)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-01
- **関連企業:** NVIDIA
- **要約:** NVIDIAがOpenShellを公開。自律AIエージェント向けの安全・プライベートなランタイム環境。サンドボックス化された実行環境でデータ・認証情報・システムを保護。OpenAI Skills/Shellモデルと競合するオープンなエージェント実行環境として注目。
- **キーファクト:**
  - サンドボックス実行環境: データ・認証・システム保護
  - オープンソース（GitHub公開）
  - エージェント実行環境の標準化競争に新規参入
- **引用URL:** https://github.com/NVIDIA/openshell
- **Evidence ID:** EVD-20260623-0019

### INFO-020
- **タイトル:** Google Antigravity Skills: Cross-compatible agent skill format with Claude Code and Codex
- **ソース:** Google Cloud (公式ドキュメント) / Google Codelabs
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Google / DeepMind
- **要約:** GoogleがAntigravity Skills（軽量オープン形式のエージェントスキル）を展開。Knowledge CatalogスキルはAntigravity、Claude Code、Codex等の複数AIエージェントで利用可能。Gemini Code Assist個人版はAntigravityファミリーに移行。スキル配布形式の標準化競争が激化。
- **キーファクト:**
  - Antigravity Skills: 特定タスク向け再利用可能カスタム指示（法的契約レビュー等）
  - クロスエージェント互換: Knowledge CatalogがAntigravity/Claude Code/Codexで動作
  - Gemini Code Assist個人版 → Antigravityファミリーへ移行（非推奨化）
  - GEAR Skillsコース: KPI連動のエージェント型→ビジネス影響マッピング
- **引用URL:** https://docs.cloud.google.com/gemini/enterprise/docs/skills, https://codelabs.developers.google.com/getting-started-with-antigravity-skills
- **Evidence ID:** EVD-20260623-0020

### INFO-021
- **タイトル:** Amazon Bedrock AgentCore: Web Search tool, enterprise knowledge reasoning, continuous learning
- **ソース:** AWS (公式ブログ)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-04
- **関連企業:** Amazon / AWS
- **要約:** AWSがBedrock AgentCoreを大幅アップグレード。Web Searchツール（データ境界内でウェブ情報を取得）、エンタープライズナレッジ推論（SharePoint/Drive/S3）、継続学習機能を追加。エージェントが社内データと外部ウェブ情報を統合して推論可能に。
- **キーファクト:**
  - Web Search: ゼロ設定でエージェントが引用付きウェブ知識で回答をグラウンディング
  - エンタープライズナレッジ: SharePoint, Drive, S3にまたがる推論
  - 継続学習: エージェントが過去の相互作用から学習
  - データ境界内での処理維持（セキュリティ重視）
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/new-in-amazon-bedrock-agentcore-build-agents-with-broader-knowledge-and-continuous-learning/
- **Evidence ID:** EVD-20260623-0021

### INFO-022
- **タイトル:** Microsoft Agent 365: Enterprise control plane for AI agents
- **ソース:** Microsoft Learn (公式ドキュメント)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** Microsoft
- **要約:** MicrosoftがAgent 365を発表。エンタープライズAIエージェントの制御平面（control plane）として、ITチームが全エージェントを一元監視・ガバナンス・セキュリティ管理。Azure AI Foundryとの統合で基盤モデルアクセスからエージェント構築までを統合。
- **キーファクト:**
  - Microsoft Agent 365: エージェント向けエンタープライズ制御平面
  - Azure AI Foundry: 基盤モデル → AIアプリ → エージェント構築の統合エコシステム
  - Microsoft Fabric: AIエージェントのダッシュボード・ワークフロー統合
  - ビジュアルドラッグ&ドロップワークフロービルダー、マルチエージェントパターン
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-365-integration
- **Evidence ID:** EVD-20260623-0022

### INFO-023
- **タイトル:** NVIDIA AgentPerf: Industry's first agentic AI benchmark
- **ソース:** NVIDIA / Artificial Analysis
- **公開日:** 2026-06 (推定)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-003-02
- **関連企業:** NVIDIA
- **要約:** NVIDIAとArtificial AnalysisがAgentPerfを発表。業界初のエージェントAIベンチマークで、開発者・エンタープライズ・インフラプロバイダーがエージェントパフォーマンスを比較可能。クラウドプロバイダー横断的なエージェント能力評価の標準化を目指す。
- **キーファクト:**
  - AgentPerf: 業界初のエージェントAIベンチマーク
  - クラウドプロバイダー横断比較を可能にする
  - 開発者・エンタープライズ・インフラ向けのクリアな比較指標
- **引用URL:** https://www.nvidia.com/en-eu/ai/
- **Evidence ID:** EVD-20260623-0023

### INFO-024
- **タイトル:** 80% of enterprise apps shipped Q1 2026 embed AI agents (from <5% in early 2025)
- **ソース:** LinkedIn (AcrossTek) / BusinessWire (Kore.ai Survey)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** 2026年Q1に出荷されたエンタープライズアプリの80%が少なくとも1つのAIエージェントを組み込んでいる（2024年33%、2025年初頭<5%から急増）。しかしKore.ai調査では72%の企業がAIエージェントが管理されていないリスク（財務・コンプライアンス露出）で動作していると回答。エージェント完了率の平均は74.8%。
- **キーファクト:**
  - エンタープライズアプリのAIエージェント組み込み率: 2024年33% → 2025年Q1 <5% → 2026年Q1 80%
  - 72%の企業がAIエージェントの管理されていないリスクを報告（Kore.ai調査）
  - エージェント平均完了率: 74.8%（First Page Sage）
  - McKinsey 2025: 組織の88%が少なくとも1つのビジネス機能でAI定期利用
- **引用URL:** https://www.businesswire.com/news/home/20260617610324/en/New-Kore.ai-Survey
- **Evidence ID:** EVD-20260623-0024

### INFO-025
- **タイトル:** Gartner: Fortune 500 AI agents from 15 (2025) to 150,000 (2028); Multi-agent systems up 327% YoY
- **ソース:** Cybernews (Gartner引用) / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** (業界全体)
- **要約:** Gartner予測でF500企業のAIエージェント数が2025年の15から2028年には150,000へ10,000倍増加。88%のF500企業がAIエージェントを本番展開済み。マルチエージェントシステムは前年比327%増。ただし、エンタープライズAIエージェントパイロットの多くがevals/信頼性問題で本番移行できず。
- **キーファクト:**
  - Gartner: F500企業のAIエージェント数 15 (2025) → 150,000 (2028)
  - F500の88%がAIエージェントを本番展開済み
  - マルチエージェントシステム前年比327%増
  - パイロット→本番移行の障壁: evals/信頼性の欠如
- **引用URL:** https://cybernews.com/ai-tools/how-to-build-an-ai-agent/
- **Evidence ID:** EVD-20260623-0025

### INFO-026
- **タイトル:** 74% of executives achieve AI agent ROI within first year
- **ソース:** Dan Cumberland Labs
- **公開日:** 2026-06 (推定)
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** AIエージェントを実装した企業の74%の経営幹部が最初の1年以内にROIを達成と報告。時間節約、コスト削減、収益影響、生産性向上が主要ROI要因。ただし、成功にはワークフロー適合性、信頼性管理、統合深度、測定可能ROI設計が必要。
- **キーファクト:**
  - 初年度ROI達成率: 74%の経営幹部
  - 主要ROI要因: 時間節約、コスト削減、収益影響、生産性向上
  - 成功条件: ワークフロー適合性・信頼性管理・統合深度
- **引用URL:** https://dancumberlandlabs.com/blog/ai-agents-for-business/
- **Evidence ID:** EVD-20260623-0026

### INFO-027
- **タイトル:** EU AI Act August 2 2026 enforcement: High-risk compliance framework activates
- **ソース:** Witness AI / Augment Code
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (業界全体)
- **要約:** EU AI Actの2026年8月2日執行日がメインの高リスクAIコンプライアンスフレームワーク（Articles 8-15）を有効化。Tier 2違反で最大€15Mまたは世界年間売上の3%。エンタープライズ調達でAI Actコンプライアンスが必須要件化。AI生成コードも規制対象。
- **キーファクト:**
  - 2026年8月2日: Articles 8-15（高リスクAI要件）の執行開始
  - Tier 2違反: €15M または全世界年間売上の3%（いずれか高い方）
  - 調達要件: エンタープライズ顧客がAI Actコンプライアンスを調達条件化
  - EU AI Act修正案: 既存EU製品安全法との重複解消を検討
- **引用URL:** https://witness.ai/blog/eu-ai-act-compliance-checklist-2026/
- **Evidence ID:** EVD-20260623-0027

### INFO-028
- **タイトル:** Trump AI Executive Order expands cybersecurity; directs agencies to challenge state AI laws
- **ソース:** Holland & Knight / KGOU / Brennan Center
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** (米国政府)
- **要約:** トランプ政権の新AI大統領令がサイバーセキュリティを拡大。連邦機関に30日以内のサイバー防御強化を指示、AIサイバーセキュリティ情報交換所を創設。同時に連邦機関に州AI規制への異議申し立てを指示し、「過剰な」法律にフラグを立て、従わない州へのブロードバンド資金差し止めも示唆。オクラホマ等が州AI規制を保留。
- **キーファクト:**
  - 30日以内の連邦サイバー防御強化指示
  - AIサイバーセキュリティ情報交換所（clearinghouse）創設
  - 連邦機関に州AI規制への異議申し立て指示
  - 従わない州へのブロードバンド資金差し止め示唆
  - コロラドAI法・イリノイAI雇用法が既に発効
- **引用URL:** https://www.hklaw.com/en/insights/publications/2026/06/executive-order-on-artificial-intelligence-expands-cybersecurity
- **Evidence ID:** EVD-20260623-0028

### INFO-029
- **タイトル:** Pentagon opens classified military networks to 8 AI firms; Anthropic labeled "supply-chain risk"
- **ソース:** Built In / Kavout / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Google, Microsoft, NVIDIA, AWS, Oracle, xAI, Anthropic
- **要約:** ペンタゴンが分類軍事ネットワークを8社の承認テック企業（OpenAI, Google, Microsoft, Nvidia, AWS, Oracle等）に開放。一方でAnthropicは「サプライチェーンリスク」指定を受け、Claudeアクセスを巡るペンタゴンとの対立が報じられた。Anthropicは競合AI企業と$200M/2年契約を受注。xAIは政府史上最大級のAIデプロイ契約を獲得。
- **キーファクト:**
  - ペンタゴン: 分類ネットワークを8社に開放（単一モデル選択ではなく多社アプローチ）
  - Anthropic: 「サプライチェーンリスク」指定（AI使用に関する意見不一致が原因）
  - xAI: 政府史上最大級のAIデプロイ契約獲得、OpenAI/Googleと直接競合
  - Anthropic: ペンタゴン・DoDから$200M/2年契約を競合企業と共同受注
  - ペンタゴン: AIを使って議会提出報告書を執筆することを誇示
- **引用URL:** https://builtin.com/articles/anthropic-pentagon-claude-dispute, https://www.kavout.com/market-lens/what-sparked-the-pentagon-s-unprecedented-supply-chain-risk-label-for-anthropic
- **Evidence ID:** EVD-20260623-0029

### INFO-030
- **タイトル:** China cracks down on AI speculation; makes AI-based layoffs illegal
- **ソース:** CNBC / Reddit
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (中国政府)
- **要約:** 中国証券規制当局（CSRC）がAIの「テクハイプ」投機とAI株選びを非難。AIを資本市場での利用に関するガイダンスを発出予定。また中国はコスト削減のためのAIによる人員削減を違法化し、企業にAIを解雇の口実として使わないよう指示。G7でグローバルAI安全協力を呼びかけ。
- **キーファクト:**
  - CSRC: AI「テクハイプ」投機とAI株選びを非難、ガイダンス発出予定
  - 中国: コスト削減目的のAI人員削減を違法化
  - 中国: 企業にAIを解雇の口実として使わないよう指示
  - G7でグローバルAI安全協力のアクションプランを発表
- **引用URL:** https://www.cnbc.com/2026/06/17/china-securities-regulator-csrc-artificial-intelligence-investing-stocks-.html
- **Evidence ID:** EVD-20260623-0030

### INFO-031
- **タイトル:** Trump administration considers Defense Production Act to force AI companies into national security; Anthropic refuses mass surveillance and autonomous weapons
- **ソース:** The Economist / The Hill / Fareed Zakaria
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google, xAI
- **要約:** トランプ政権が国防生産法（DPA）の行使でAI企業に安全保障目的でのサービス提供を強制的に求める方針を示唆。Anthropicは大量監視・完全自律型兵器からの倫理的制限の撤廃を拒否し、結果として新モデルを一時取り下げ。競合AIラボが「政府資金のためにAI安全性原則を放棄している」と研究者が非難。萎縮効果の懸念。
- **キーファクト:**
  - DPA行使検討: AI企業に安全保障目的でのサービス提供を強制
  - トランプ: 「やるだろうが、まだ必要か確信がない」と柔軟姿勢
  - Anthropic: 大量国内監視・人間の関与ない自律型兵器の使用拒否で倫理制限を維持
  - ペンタゴン: Claudeアクセス拒否後、Anthropicとの関係を切断
  - 研究者: 競合ラボが「政府資金のためにAI安全性原則を放棄」と非難
  - 萎縮効果: AI安全性姿勢を持つ企業が罰せられる構造の懸念
- **引用URL:** https://www.facebook.com/TheEconomist/posts/the-trump-administration-hopes-the-technology-will-strengthen-americas-position-/1519370356888146/
- **Evidence ID:** EVD-20260623-0031

### INFO-032
- **タイトル:** Anthropic vs Pentagon: Refusal of autonomous weapons and mass surveillance leads to supply-chain risk label
- **ソース:** Built In / The Hill
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicが完全自律型兵器と大量市民監視へのAI使用を拒否した結果、ペンタゴンがAnthropicに「サプライチェーンリスク」指定を付与。トランプ政権の輸出管理指令後、Anthropicは新モデル（Fable 5/Mythos 5）を一時取り下げ。この出来事は安全性重視企業が政府契約市場で競争的不利益を被る構造的リスクを示す。
- **キーファクト:**
  - Anthropic拒否内容: 完全自律型兵器・大量国内監視
  - ペンタゴン対応: 「サプライチェーンリスク」指定でAnthropicの評価額・提携に影響
  - Fable 5/Mythos 5: 輸出管理指令後に一時取り下げ
  - アイルランドSeanad: 軍事AI・自律型兵器のガバナンス不在に懸念表明
- **引用URL:** https://www.facebook.com/TheHill/posts/anthropic-took-down-its-newest-ai-models-last-week
- **Evidence ID:** EVD-20260623-0032

### INFO-033
- **タイトル:** AI safety vs government money: Researchers accuse competing labs of abandoning principles
- **ソース:** Fareed Zakaria / The Economist
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google, xAI
- **要約:** AI研究者らが、政府資金を得るためにAI安全性原則を放棄する競合ラボを非難。政府はAI能力の一般向け制限を強化する一方、ペンタゴンや外国同等機関には制限を課さない二重基準。表現の自由への萎縮効果懸念。ロンドン市長がMet Policeの£50M Palantir契約を調達理由でブロック。
- **キーファクト:**
  - 研究者非難: 競合ラボが政府資金のためにAI安全性原則を放棄
  - 二重基準: 一般向けAI制限強化 vs 軍事AI制限不在
  - 萎縮効果: 表現の自由への悪影響懸念
  - ロンドン: Sadiq KhanがMet Police £50M Palantir契約をブロック（調達理由）
- **引用URL:** https://www.facebook.com/fareedzakaria/posts/last-friday-the-us-government-did-something-extraordinary
- **Evidence ID:** EVD-20260623-0033

### INFO-034
- **タイトル:** AI company military contract competitive displacement
- **ソース:** Fareed Zakaria / Kavout
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** xAI, OpenAI, Google, Anthropic
- **要約:** Anthropicの安全性拒否によって生じた政府契約市場の空白に、xAIが参入。Elon MuskのxAIが政府史上最大級のAIデプロイ契約を獲得し、OpenAI/Googleと直接競合。これは「安全性堅持企業が罰せられ、順応企業が報われる」構造の具体例。ペンタゴンは単一モデル選択ではなく8社ネットワーク開放でリスク分散。
- **キーファクト:**
  - xAI: 政府史上最大級AIデプロイ契約獲得
  - 競争的不利益: Anthropicの安全性拒否がxAI等の漁夫の利を生む
  - ペンタゴン8社開放: 単一依存回避のマルチベンダー戦略
  - 「設計通り≠技術的安全事故」の区別が実質崩壊（Arbiter IND-030参照）
- **引用URL:** https://www.facebook.com/fossbytes/posts/a-top-pentagon-official-revealed-that-donald-trumps-administration-used-elon-mus
- **Evidence ID:** EVD-20260623-0034

### INFO-035
- **タイトル:** Klarna lost $40B after AI replacement of 700 CS workers; now quietly rehiring humans
- **ソース:** Facebook / LinkedIn / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaが700名のカスタマーサービス担当者をAIで置換した結果、$40Bの企業価値損失が発生。2年後、Klarnaは静かに人間の再雇用を開始。Duolingoも2024年に契約社員の10%をAI置換で削減し、人間をAIで置換しない方針に転換したと報じられる。AIレイオフの逆火現象が複数企業で確認。
- **キーファクト:**
  - Klarna: 700名CS人員をAI置換 → $40B価値損失 → 2年後に人間再雇用
  - Duolingo: 2024年に契約社員10%をAI置換削減 → 人間不replacement方針に転換
  - 「AIは仕事を全部奪ったのではなく、トレーニングホイールを奪った」
  - AIレイオフの逆火: 企業が再雇用し、より多くのコストを支出
- **引用URL:** https://www.facebook.com/lalbhatiaofficial/posts/ai-didnt-take-all-the-jobs-it-took-the-training-wheelsklarna-brought-humans-back
- **Evidence ID:** EVD-20260623-0035

### INFO-036
- **タイトル:** 7 entry-level jobs AI is quietly replacing (junior dev, first-tier CS, content writer, data entry)
- **ソース:** Medium / Reddit / Facebook
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-04, KIQ-004-02
- **関連企業:** (業界全体)
- **要約:** AIが静かに置換している7つのエントリーレベル職: ジュニアソフトウェア開発者、一次カスタマーサポート、エントリーレベルコンテンツライター、データ入力等。ただし人間の判断と信頼は代替不能。多数の企業がAIパイロット段階で停滞し、本番移行できず。
- **キーファクト:**
  - 置換進行中: ジュニア開発者・一次CS・コンテンツライター・データ入力
  - 代替不能: 人間の判断・信頼・対人関係
  - 企業の停滞: パイロット段階から本番への移行障壁
  - AIコーディングツールの生産性影響測定の重要性（Swarmia分析）
- **引用URL:** https://medium.com/ai-analytics-diaries/7-entry-level-jobs-ai-is-quietly-replacing
- **Evidence ID:** EVD-20260623-0036

### INFO-037
- **タイトル:** Google dethrones OpenAI as agencies' preferred AI partner; AI agents automate media buying end-to-end
- **ソース:** Forrester / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google, OpenAI, Meta
- **要約:** Forrester分析でGoogleがOpenAIから代理店の優先AIパートナーの座を奪取。Googleは「AIを使用する広告プラットフォーム」から「AI対応マーケティングOS」へ移行。Horizon Media等がエージェント型インフラを構築し、AIエージェントがInnovid/Magnite/Disney/TikTok/Fox等のエージェントと直接対話してメディアバイイングを自律実行。
- **キーファクト:**
  - Forrester: Google > OpenAI が代理店の優先AIパートナー
  - Google: 「AIを使用する広告プラットフォーム」→「AI対応マーケティングOS」
  - Horizon Media: エージェント型メディアバイイングインフラ構築
  - AIエージェントがプラットフォーム間で自律的にメディア決定を実行
- **引用URL:** https://www.forrester.com/blogs/google-dethrones-openai-as-agencies-preferred-ai-partner/
- **Evidence ID:** EVD-20260623-0037

### INFO-038
- **タイトル:** Agent-as-a-Service (AaaS) is replacing SaaS; agentic workflows collapse software stacks
- **ソース:** towardsagenticai.com / Kavout / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** (業界全体)
- **要約:** Agent-as-a-Service (AaaS)がSaaSモデルを置換しつつある。単一のエージェント型ワークフローがCRM、ERP、API、データベース等の既存システムを統合し、パイプライン監視、フォローアップ、レコード更新、異常フラグ、エスカレーションを自動実行。SaaSのシートベース課金モデルが時代遅れになりつつある。
- **キーファクト:**
  - AaaS: AIエージェントがCRM/ERP/API/DBを統合しエンドツーエンドタスクを自律実行
  - 単一エージェントワークフローが複数SaaSスタックを統合・圧縮
  - SaaSのシートベース課金モデルの陳腐化
  - 中間層（中間マネージャー）の組織的高さ圧縮
- **引用URL:** https://towardsagenticai.com/agent-as-a-service-how-aaas-is-replacing-saas/
- **Evidence ID:** EVD-20260623-0038

### INFO-039
- **タイトル:** AI reshapes semiconductor 'smile curve' — middle segment re-elevated as scarce resource
- **ソース:** KuCoin / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** (半導体・AI業界全体)
- **要約:** AIが半導体「スマイルカーブ」を再形成。従来は中間工程（製造・組立）の利益率が圧縮されていたが、AI時代で中間セグメントが再評価。ただし下位従業員の減少で中間マネージャーの必要性が縮小し、組織の高さ全体が圧縮される。バリューチェーンの中間層侵食が進行。
- **キーファクト:**
  - スマイルカーブ再形成: AIが中間セグメントの価値を再上昇
  - 組織圧縮: 下位従業員減少 → 中間マネージャー不要 → 組織の高さ圧縮
  - Agentic AIがバリューチェーン全体を再構築
  - 垂直AI企業が水平展開+垂直統合へ移行
- **引用URL:** https://www.kucoin.com/news/flash/ai-reshapes-semiconductor-smiling-curve-as-global-bull-market-gains-momentum
- **Evidence ID:** EVD-20260623-0039

### INFO-040
- **タイトル:** AI API Pricing Guide 2026: Full provider comparison with cost trends
- **ソース:** TensorFeed
- **公開日:** 2026-06 (Last Updated)
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic, OpenAI, Google, Meta, xAI, DeepSeek, Mistral, Microsoft, NVIDIA
- **要約:** 2026年6月時点の全API価格比較。プレミアム推論モデルで約$60/百万出力トークンから、オープンソース無料まで幅広い。同一ワークロードで最大58倍のコスト差。トークンコストは急速に下落中（Gemini 2.0 Flash $0.10/M入力）。Google AI Studioが最も寛大な無料ティアを提供。
- **キーファクト:**
  - Claude Fable 5: $10入力/$50出力（最高価格帯）
  - Claude Opus 4.8: $5/$25
  - GPT-5.5: $5/$30
  - Gemini 3.5 Flash: $1.50/$9.00 / Gemini 2.0 Flash: $0.10/$0.40
  - Grok 4.3: $1.25/$2.50
  - DeepSeek V4 Pro: $0.43/$0.87（コストリーダー）
  - Llama 4 Scout/Maverick: 無料（自己ホスト）
  - Microsoft MAI-Code-1-Flash: $0.75/$4.50
  - MiniMax M3: $0.30/$1.20
  - NVIDIA Nemotron 3 Nano Omni: 無料
  - 最大58倍のコスト差（同一ワークロード）
  - バッチAPI 50%割引、プロンプトキャッシュで90%削減
- **引用URL:** https://tensorfeed.ai/ai-api-pricing-guide
- **Evidence ID:** EVD-20260623-0040

### INFO-041
- **タイトル:** Terminal-Bench 2.0: GPT-5.5 leads with 0.827; ARC-AGI-2 tests fluid reasoning
- **ソース:** LLM Stats / TechJack Solutions / OpenLM
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** Terminal-Bench 2.0でGPT-5.5が0.827（48モデル平均0.575）で1位。ARC-AGI-2は抽象視覚パズルで流動的推論を測定、記憶された事実のショートカットなし。Qwen3.5-plusが一部ベンチマークで83.6%。Chatbot Arena、BenchLM等のリーダーボードがアクティブに更新中。
- **キーファクト:**
  - Terminal-Bench 2.0: GPT-5.5 1位（0.827）、48モデル平均0.575
  - ARC-AGI-2: 流動的推論、記憶ショートカット不可の抽象視覚パズル
  - Qwen3.5-plus: 83.6%（一部ベンチマーク最高）
  - ベンチマーク飽和問題: BenchLMが陳腐化・飽和テストの扱いを定義
  - オープンソースベンチマーク: 147コーディングタスクを4時間毎に実行、5試行の中央値
- **引用URL:** https://llm-stats.com/benchmarks/terminal-bench-2, https://techjacksolutions.com/ai-tools/rankings/llm-benchmarks-that-matter/
- **Evidence ID:** EVD-20260623-0041

### INFO-042
- **タイトル:** Open-weight vs commercial gap closing fast; Llama 4 Maverick 57% improvement on LiveCodeBench
- **ソース:** Google Cloud / Thunder Compute / X
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, Mistral, DeepSeek, Google
- **要約:** オープンウェイトモデルと商用モデルの性能ギャップが急速に縮小。Llama 4 MaverickがLiveCodeBenchで43.4（Llama 3.1 405Bの27.7から57%相対改善）。Mistralのオープンウェイトモデルが中堅ハードウェアで効率動作し、欧州AI主権の核に。エンタープライズのオープンウェイト採用が2024年以降加速。中国モデルは性能で遅れるが価格の極小化。
- **キーファクト:**
  - Llama 4 Maverick: LiveCodeBench 43.4（前世代27.7から+57%）
  - Llama 4 Scout 17B: 同サイズクラスでSOTA
  - Mistral: 中堅ハードウェアで効率動作、欧州AI主権の核
  - OVHcloud: 欧州向けフロンティアAI構築（Mistral対抗）
  - DeepSeek V3.2 Thinking: Grok 4 Fastの大部分ベンチマークで上回る
  - 中国モデル: 性能遅れるが価格の極小化で競争力
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama, https://x.com/Mayhem4Markets/status/2067804462484234488
- **Evidence ID:** EVD-20260623-0042

### INFO-043
- **タイトル:** GLM-5.2 vs DeepSeek V4 Pro comparison; Chinese models lag in performance but dominate on price
- **ソース:** Artificial Analysis / Rest of World
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03, KIQ-003-01
- **関連企業:** DeepSeek, xAI, GLM/Zhipu
- **要約:** Artificial AnalysisでGLM-5.2 (max)とDeepSeek V4 Pro (Reasoning)を詳細比較。中国モデルは最高水準の米国モデルに性能で遅れるが、価格の極小化で大部分のタスクを処理可能。DeepSeek V3.2 ThinkingはGrok 4 Fastの大部分ベンチマークで優位。米国企業がコスト重視で中国AIを選択する動き。
- **キーファクト:**
  - GLM-5.2 vs DeepSeek V4 Pro: Artificial Analysisで知性・価格・速度を詳細比較
  - DeepSeek V3.2 Thinking: Grok 4 Fastより大部分ベンチマークで優位（Grok 4 Fastは1.1x安価）
  - 中国モデル: 最高米国モデルに性能遅れるが、価格の極小化で大部分タスク対応
  - 米国企業のコスト重視中国AI選択の動き（Rest of World報道）
- **引用URL:** https://artificialanalysis.ai/models/comparisons/glm-5-2-vs-deepseek-v4-pro
- **Evidence ID:** EVD-20260623-0043

### INFO-044
- **タイトル:** SpaceX acquires AI coding startup Cursor (Anysphere) for $60 billion in all-stock deal
- **ソース:** Reuters / Business Insider
- **公開日:** 2026-06-16
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-04, KIQ-001-01
- **関連企業:** SpaceX, xAI, Cursor/Anysphere
- **要約:** SpaceXがAIコーディングスタートアップCursor（Anysphere）を$60B（完全株式交換）で買収することを確認。SpaceXは既にxAIを買収し$1.25兆の複合企業を形成済み。Cursor買収でAIコーディングエージェント分野での競争力を強化。世界最大の非公開企業としての地位をさらに固める。
- **キーファクト:**
  - SpaceX → Cursor買収: $60B、全株式交換
  - SpaceX + xAI: 既に統合済み（$1.25兆評価額、世界最大非公開企業）
  - Cursor: 人気AIコーディングエージェント
  - Musk: AI分野でのライバル（OpenAI等）との格差縮小が目的
- **引用URL:** https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/
- **Evidence ID:** EVD-20260623-0044

### INFO-045
- **タイトル:** Google investing up to $40B in Anthropic; Amodei & Hassabis call for US-led AI coalition at G7
- **ソース:** CNBC / Instagram / Investors.com
- **公開日:** 2026-06-17
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-002-03
- **関連企業:** Google, Anthropic, OpenAI
- **要約:** GoogleがAnthropicに最大$40B投資と報じられ、AI市場の構造変化を示唆。Anthropic CEO AmodeiとGoogle DeepMind CEO HassabisがG7サミットの非公開会合で米国主導AI連合を要請。OpenAI・Anthropicの評価額が公開前に急上昇。GoogleからOpenAI/Anthropicへのトップ研究者流出が続く。
- **キーファクト:**
  - Google → Anthropic: 最大$40B投資（報道）
  - G7: Amodei + Hassabisが非公開会合で米国主導AI連合を要請
  - OpenAI・Anthropic評価額: 公開前に急上昇
  - Google: AI研究者2名がOpenAI/Anthropicに流出
  - 価格戦争: OpenAI・GoogleがAPI価格を切断
- **引用URL:** https://www.cnbc.com/2026/06/17/anthropic-amodei-google-hassabis-us-ai-coalition-g7.html
- **Evidence ID:** EVD-20260623-0045

### INFO-046
- **タイトル:** AI funding Q1-Q2 2026: xAI $20B Series E, Odyssey $310M, Prosper AI $30M, Fal $140M
- **ソース:** Crescendo AI / Reuters / Crunchbase
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** xAI, Odyssey, Prosper AI, Fal, AlphaSense
- **要約:** 2026年Q1にxAIが$20B Series E（年の4つの記録的メガディールの1つ）。AIワールドモデル開発者Odysseyが$310M Series B（$1.45B評価額、AWS提携）。Prosper AIがa16zから$30M Series A。AlphaSenseが$150M調達で$2.5B評価。AIインフラ・サイバーセキュリティへの投資も活発。
- **キーファクト:**
  - xAI: $20B Series E（Q1 2026、4大メガディールの1つ）
  - Odyssey: $310M Series B、$1.45B評価額、AWS提携
  - Prosper AI: $30M Series A（a16zリード）
  - AlphaSense: $150M調達、$2.5B評価額
  - Fal: $140M調達（画像生成AI）
  - Q1 2026: AIインフラ・サイバー・ディフェンスへのVC投資集中
- **引用URL:** https://www.crescendo.ai/news/latest-vc-investment-deals-in-ai-startups, https://www.reuters.com/business/ai-lab-odyssey-valued-145-billion-latest-funding-round-2026-06-17/
- **Evidence ID:** EVD-20260623-0046

### INFO-047
- **タイトル:** Multi-vendor AI cost management: Gateway approach vs hard caps; API migration guides emerge
- **ソース:** Truefoundry / Compareai.today / Practical Logix
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-05, KIQ-002-01
- **関連企業:** (業界全体)
- **要約:** Meta/Amazon/UberがAI超過支出からハードキャップへ1四半期で転換した事例から、ゲートウェイ型アプローチ（ダイヤル式制御）の重要性を提示。プロバイダー間移行ガイド（Compareai.today）が登場し、スイッチングコスト可視化。Small Language ModelsでフロンティアAPI支出を30-70%削減可能。Claude Code vs Codex vs Gemini CLIの機能比較が可能。
- **キーファクト:**
  - Meta/Amazon/Uber: AI超過支出→ハードキャップの1Q転換事例
  - ゲートウェイ型コスト管理: スイッチではなくダイヤル
  - Compareai.today: OpenAI/Anthropic/Google間の段階的移行ガイド
  - Small Language Models: フロンティアAPI支出を30-70%削減、アーキテクチャ移行不要
  - Claude Code vs Codex vs Gemini CLI: 機能別詳細比較可能
- **引用URL:** https://www.truefoundry.com/pt/blog/field-notes-ai-cost-gateway-not-a-switch, https://compareai.today/migration-guides
- **Evidence ID:** EVD-20260623-0047

### INFO-048
- **タイトル:** KPMG: 91% of leaders rely on external partners for AI; AI taking 37% of entry-level tasks in India
- **ソース:** KPMG / Charity Village / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-002-02
- **関連企業:** KPMG
- **要約:** KPMG調査で91%のリーダーがAIの外部パートナーに依存。カナダ組織のAgentic AI採用が顕著に増加。インドでAIがエントリーレベルタスクの37%を既に代替。Randstad報告で「AIエージェント」スキル求人が1,587%急増。CFO: 「AIは次世代育成方法の完全再考を迫っている」。
- **キーファクト:**
  - KPMG: リーダーの91%がAI外部パートナーに依存
  - インド: AIがエントリーレベルタスクの37%を代替済み
  - Randstad: 「AIエージェント」スキル求人1,587%急増
  - KPMG CFO: エントリーレベルタスク自動化で「次世代育成の完全再考」が必要
- **引用URL:** https://www.chicagobusiness.com/crains-content-studio/publishing-partner/ccb-managed-services-ai-digital-transformation/
- **Evidence ID:** EVD-20260623-0048

### INFO-049
- **タイトル:** AI leading cause of layoffs: 38,579 job cuts attributed to AI (Challenger report)
- **ソース:** AI Political Pulse / Programs.com / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** (業界全体), Unity
- **要約:** Challenger社のレイオフトラッカーでAIが解雇の主要原因に。5月報告で38,579件の職務削減がAIに起因。2026年1月時点でAI主導再編で30,000職務が影響（Unity 1,800名等）。ただし「ノーレイオフ」企業もAIで特定知識業務を大規模置換中。株主圧力でAI置換レイオフを発表する企業も出現。
- **キーファクト:**
  - Challenger: AIが解雇の主要原因、5月に38,579件のAI起因職務削減
  - 2026年1月: AI再編で30,000職務影響
  - Unity: 約1,800名削減（2026年1月）
  - 「ノーレイオフ」企業もAIで特定知識業務置換
  - 株主圧力でのAI置換レイオフ発表も出現
- **引用URL:** https://aipoliticalpulse.substack.com/p/ai-is-causing-40-of-layoffs-or-zero
- **Evidence ID:** EVD-20260623-0049

### INFO-050
- **タイトル:** CyberAgent × Alibaba Cloud strategic dialogue; AI-generated ad creatives for Seven-Eleven
- **ソース:** Alibaba Cloud / note.com
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-01, KIQ-002-05
- **関連企業:** CyberAgent, Alibaba Cloud
- **要約:** Alibaba CloudとCyberAgentが戦略的対話を開始。CyberAgentはセブン-イレブンの広告クリエイティブをAI生成で手がけ、プラットフォーム開発も実施。Qwen 3.7-Maxが35時間連続稼働・1,000+ツール呼び出し対応。日本の広告業界でのAI自動化が加速。
- **キーファクト:**
  - Alibaba Cloud × CyberAgent: 戦略的対話開始
  - CyberAgent: セブン-イレブン広告クリエイティブをAI生成で制作
  - Qwen 3.7-Max: 35時間連続稼働、1,000+ツール呼び出し対応
  - 日本広告業界のAI自動化加速
- **引用URL:** https://www.facebook.com/alibabacloud/posts/we-are-pleased-to-announce-a-strategic-dialogue
- **Evidence ID:** EVD-20260623-0050

### INFO-051
- **タイトル:** AI engineer salary premium over software engineers; "coding will become a useless commodity"
- **ソース:** LinkedIn / Facebook (AWS CEO Garmer引用) / BCG
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** (業界全体), AWS, BCG
- **要約:** AIエンジニアの給与がソフトウェアエンジニアを上回る（AI: 新卒$120-220k、ミッド$220-350k+ vs ソフトウェア: 新卒$80-180k）。AWS CEO Garman: 「2025年の開発者は2020年と全く異なるスキルが必要、純粋なコーディングから革新的な方向へシフト」。BCG: 2030年までに現在のスキルの40%が陳腐化。コーディングのコミョディティ化が進行。
- **キーファクト:**
  - AIエンジニア給与: 新卒$120-220k、ミッド$220-350k+（ソフトウェア新卒$80-180kより高い）
  - AWS CEO Garman: 「コーディングは近い将来無価値なコモディティになる」
  - BCG: 2030年までに現在のスキルの40%が陳腐化
  - AIロール平均$156k vs ソフトウェア$132k
  - 開発者: AIなしではコーディングを拒否するようになり、影響測定が不可能に
- **引用URL:** https://www.linkedin.com/posts/sajjaad-khader_software-engineering-vs-ai-engineering
- **Evidence ID:** EVD-20260623-0051

### INFO-052
- **タイトル:** AI coding tools boost productivity 15-20% average; Jevons effect creates more dev jobs
- **ソース:** Swarmia / Commonfund / DX (Uber)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** Uber
- **要要:** AIコーディングツールで開発者生産性が平均15-20%向上。ある年次では178%増。新規開発者の80%が最初の1週間以内にAIアシスタント使用開始。UberがAIの開発者生産性への影響を測定する取り組みを公開。Jevons効果（効率化が需要を増加させる）でAIがソフトウェア開発を安価・高速化しても開発ジョブは減らないとの分析。
- **キーファクト:**
  - AI生産性向上: 平均15-20%、最大178%増（年次比較）
  - 新規開発者の80%が最初の1週間以内にAIアシスタント使用
  - Uber: AI影響測定の取り組み公開、AIパワーユーザーの出現
  - Jevons効果: 効率化が需要を増加させ、開発ジョブは減らない
  - AI生成コード: レビュー時間の短縮、検証の容易化
- **引用URL:** https://www.commonfund.org/blog/ais-productivity-payoff-is-here
- **Evidence ID:** EVD-20260623-0052

### INFO-053
- **タイトル:** New AI-era job roles emerge: AI Creative Strategy Director, AI Art Director, Agentic Search Director
- **ソース:** LinkedIn / TEKsystems / Mediabistro / Visa
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** Adobe, Visa, TEKsystems
- **要約:** AI時代の新職種が雇用市場に出現。Director of Creative Strategy & AI Innovation (Adobe)、AI Art Director/Designer ($95-105/hr, TEKsystems)、Director of SEO and Agentic Search、AI Strategy & Automation (Visa)。AIトレーナー、プロンプトエンジニア、MLエンジニアが高需要。人間の創造性・共感・批判的思考はAI代替不可の領域として価値上昇中。
- **キーファクト:**
  - 新職種: Director Creative Strategy & AI Innovation (Adobe)
  - AI Art Director: $95-105/hr（TEKsystems）
  - Agentic Search Director: SEO×エージェント検索の融合
  - AI Strategy & Automation Director: Visa
  - 高需要AI職: AIトレーナー、プロンプトエンジニア、MLエンジニア
  - 代替不可: 共感・創造性・批判的思考・人間関係スキル
- **引用URL:** https://www.linkedin.com/jobs/view/director-creative-strategy-ai-innovation-at-adobe-4402319223
- **Evidence ID:** EVD-20260623-0053

### INFO-054
- **タイトル:** Human-centered design gains value in AI era; intentional human-machine collaboration design
- **ソース:** Innovative Human Capital / IxDF / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** (業界全体)
- **要約:** AI時代で人間中心設計（human-centered design）の価値が上昇。意図的な人間-機械協調設計が戦略的不可欠要件に。AIが可能性を生成する一方、人間の好奇心・共感・批判的思考・コラボレーションはより重要に。デザイン思考（反復的アプローチでユーザー理解・前提挑戦・問題再定義・革新的解決策創出）の価値が再確認。
- **キーファクト:**
  - 人間中心設計: AI時代に価値上昇
  - 人間-機械協調: 意図的相互作用設計が戦略的不可欠要件
  - AI代替不可スキル: 好奇心・共感・批判的思考・コラボレーション
  - デザイン思考: 反復的アプローチでユーザー理解・問題再定義
- **引用URL:** https://www.innovativehumancapital.com/article/designing-human-machine-collaboration
- **Evidence ID:** EVD-20260623-0054

### INFO-055
- **タイトル:** "Your moat in AI isn't the model. It's everything around it." — Human-AI feedback loops and proprietary data governance
- **ソース:** Inc42 AI Summit / LinkedIn / Insigniam
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** AI時代の競争優位（モート）は「モデルではなく、その周りのすべて」に存在。独自データの価値はガバナンス・品質・アクセシビリティに依存。Human-AIフィードバックループがエンタープライズモートを構築。54%の企業がAIモデル評価に手動手法を使用中。成功するAI採用は技術実装だけでなく、ワークフロー・意思決定・データインフラの再考が必要。
- **キーファクト:**
  - Inc42 AI Summit: 「AIのモートはモデルではなく、その周りのすべて」
  - 独自データモート: ガバナンス・品質・アクセシビリティに依存
  - Human-AIフィードバックループ: エンタープライズモートの構築要素
  - 54%の企業がAIモデル評価に手動手法、26%が自動化へ移行開始
  - 成功要因: ワークフロー・意思決定・データインフラの再考
- **引用URL:** https://www.facebook.com/Inc42/posts/your-moat-in-ai-isnt-the-model-its-everything-around-it
- **Evidence ID:** EVD-20260623-0055

### INFO-056
- **タイトル:** "The Next Gen Agency: Surviving and Scaling in the Age of AI" — AI resistance high in enterprises
- **ソース:** Instagram / Matt Hopkins / PCTechMag
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-04, KIQ-002-05
- **関連企業:** (業界全体), Starbucks
- **要約:** AIが広告業界を急速に再構築。「次世代エージェンシー」の生存戦略が議論される。AIエージェントは単なるツールではなく戦略的パートナーへ。大企業（Starbucks例）ではAI導入への抵抗が極めて高い。ウェブエージェンシーは戦略・ブランディング・最適化・継続サポートで存在意義を維持。AIジョブ混乱は「下層」ではなく、戦略的判断層に影響。
- **キーファクト:**
  - 「次世代エージェンシー」: AI時代の生存とスケーリングが主要テーマ
  - AIエージェント: ツールから戦略的パートナーへ
  - 大企業のAI抵抗: Starbucks例で示される高い導入抵抗
  - ウェブエージェンシー: 戦略・ブランディング・最適化で存在意義維持
  - AIジョブ影響: 下層ではなく戦略的判断層に作用（Matt Hopkins分析）
- **引用URL:** https://pctechmag.com/2026/06/the-founders-guide-to-building-a-digital-business-that-survives-ai-disruption/
- **Evidence ID:** EVD-20260623-0056

### INFO-057
- **タイトル:** Anthropic: AI contributes to nearly 80% of internal codebase — Recursive Self-Improvement "just got real"
- **ソース:** LinkedIn / Turing Post / Business Standard
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Anthropic
- **要約:** AnthropicがAIが内部コードベースの約80%に寄与していると報告し、再帰的自己改善（RSI）議論が再燃。RSIは次世代AIシステムの改善をAI自身が支援するプロセスで、現在はコーディング・実験・データパイプラインの自動化が中心。AIシステムが自身の後継者を完全に構築可能になれば、セキュリティ・監視・行動形成が極めて重要に。
- **キーファクト:**
  - Anthropic: AIが内部コードベースの約80%に寄与
  - RSI: コーディング・実験・データパイプラインの自動化が中心
  - AI自身の後継者構築: なれば、セキュリティ・監視・行動形成が極めて重要
  - 「AI building AI」がAGIへの道として議論活発化
  - Databricks: "AGI moment" — Lake Transactional/Analytical Processing
- **引用URL:** https://www.linkedin.com/posts/ksenia-se_recursive-self-improvement-rsi-just-got-activity-7472794638211411968-TuJB
- **Evidence ID:** EVD-20260623-0057

### INFO-058
- **タイトル:** AGI debate intensifies: "forms of AGI since 2020" vs "AGI is infeasible, pursue superhuman adaptable intelligence"
- **ソース:** SiliconANGLE / Predictive Analytics World / Reddit
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Databricks
- **要約:** AGI到達の議論が激化。「2020年から何らかのAGI形態は存在した」との見方と、AGIは実現不可能で「超人型適応知能」を追求すべきとの見方が対立。Databricksの新アーキテュア（Lake T/AP）がAIエージェントの運用・分析ワークロード同時アクセスを実現し「AGI moment」と評される。AIは人間を大規模に置換するのではなく、反復的作業・手動作業・低速システムを置換中。
- **キーファクト:**
  - 議論分裂: 「2020年からAGI形態存在」 vs 「AGI不可実現、超人型適応知能を追求」
  - Databricks Lake T/AP: AIエージェントの運用・分析ワークロード同時アクセス
  - AI置換対象: 人間全体ではなく反復作業・手動作業・低速システム
  - 25 AI突破予測: 2038年にAGIが科学的発見を行うとの予測
- **引用URL:** https://siliconangle.com/2026/06/16/agi-moment-databricks-new-releases-zero-support-deployment-ai-agents/
- **Evidence ID:** EVD-20260623-0058

### INFO-059
- **タイトル:** Hassabis tightens AGI timeline; Altman/Amodei/Hassabis all agree AGI in 5-10 years; 55% market odds by 2030
- **ソース:** Yahoo Finance / Instagram / Delos
- **公開日:** 2026-06-17
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google/DeepMind, OpenAI, Anthropic
- **要約:** Demis HassabisがAGIタイムラインを短縮し、Ray Kurzweilと完全一致。Sam Altman、Dario Amodei、HassabisがG7サミットでAGI 5-10年以内に問われ、Hassabisは「そう思う」と回答。Kalshi予測市場でOpenAIが2030年までにAGI達成の55%確率。Amodeiは2027年までに可能性を示唆。Mustafa Suleyman (Microsoft AI CEO) はホワイトカラー職の完全自動化を数年内と予測。
- **キーファクト:**
  - Hassabis: AGIタイムライン短縮、Kurzweilと一致
  - Altman/Amodei/Hassabis: G7でAGI 5-10年以内に合意
  - Kalshi予測市場: OpenAI AGI 2030年までに55%確率
  - Amodei: 2027年までに可能性
  - Suleyman (Microsoft): ホワイトカラー職の完全自動化を数年内
  - The Economist: 「超人型AIは人々が考えるよりはるかに早く、急激に到来する可能性」
- **引用URL:** https://www.facebook.com/yahoofinance/posts/openais-sam-altman-anthropic-ceo-dario-amodei
- **Evidence ID:** EVD-20260623-0059

### INFO-060
- **タイトル:** Yann LeCun leaves Meta with $1.03B to prove LLMs cannot reach AGI; calls xAI a "failure"
- **ソース:** StartupHub AI / Bloomberg / Gizmodo
- **公開日:** 2026-06-16
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Meta, xAI
- **要約:** Yann LeCunがMetaを離脱し、LLMがAGIに到達できないとする自身の予測（4年前）を$1.03Bの資金で裏付ける新ラボ（AMI Labs）を設立。「SF映画版のAGIは忘れるべき」とし、自己教師付きワールドモデルが人間レベルAGIへの道と主張。Muskの来年AGI達成予測を批判しxAIを「失敗」と呼び、論争再燃。Bengioは指導者にAI急速進化を真剣に受け止めるよう警告。
- **キーファクト:**
  - LeCun: Meta離脱、AMI Labs設立（$1.03B資金）
  - LeCun予測: LLMではAGIに到達不可（4年前からの主張を継続）
  - xAI「失敗」発言: Muskの来年AGI達成予測を批判
  - LeCun: 自己教師付きワールドモデルがAGIへの道
  - Bengio: 指導者にAI急速進化の真剣な受け止めを要請
- **引用URL:** https://www.startuphub.ai/ai-news/ai-figures/2026/figure-yann-lecun-llm-position-evolution-2026-06-16
- **Evidence ID:** EVD-20260623-0060

### INFO-061
- **タイトル:** "One Big Beautiful Bill" AI moratorium: federal override of state AI regulations; Fareed Zakaria calls for "a Fed for AI"
- **ソース:** Brennan Center / Fareed Zakaria / GMFUS
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** (米国政府)
- **要約:** "One Big Beautiful Bill"に含まれるAIモラトリアム条項（州レベルAI規制の連邦無効化）が超党派の反対で一旦否決されたが、トランプ政権が大統領令で再推進。安全性主張が透明性を上回る懸念。Fareed Zakariaが「AIのための中央銀行（Fed for AI）」—技術・安全保障・ビジネス専門家による独立機関—の創設を提唱。大西洋間AI協力の実践的経路も提案。
- **キーファクト:**
  - "One Big Beautiful Bill": 州AI規制の連邦無効化条項（超党派反対で一旦否決も政権が再推進）
  - Fareed Zakaria: 「AIのためのFed」—専門家による独立機関の創設提唱
  - 安全性主張vs透明性: 企業の安全性主張が透明性を上回る懸念拡大
  - 大西洋間AI協力: 公共利益AIでの集合的強み活用
- **引用URL:** https://www.facebook.com/fareedzakaria/posts/we-need-a-fed-for-ai-my-take
- **Evidence ID:** EVD-20260623-0061

### INFO-062
- **タイトル:** Seedance 2.0: Industry's first 4-modality simultaneous input video generation model
- **ソース:** Volcengine (公式) / GitHub / YouTube
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceのSeedance 2.0は業界初の4モダリティ（画像・動画・音声・テキスト）同時入力対応ビデオ生成モデル。テキストからビデオ生成、ネイティブ音声-動画联合生成をサポート。Seedance 2.0 MiniもChatArt経由で提供開始。火山引擎（Volcengine）方舟プラットフォームからAPI提供。
- **キーファクト:**
  - 4モダリティ同時入力: 業界初（画像・動画・音声・テキスト）
  - ネイティブ音声-動画联合生成: 口型同期・環境音の視覚シーンとの一致
  - Seedance 2.0 Mini: ChatArtプラットフォームで提供開始
  - API提供: Volcengine方舟大模型プラットフォーム経由
- **引用URL:** https://www.volcengine.com/docs/82379/1520757, https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts
- **Evidence ID:** EVD-20260623-0062

### INFO-063
- **タイトル:** Coze (扣子) platform: Multi-tier agent development with zero-code workflow building
- **ソース:** coze.cn (公式) / Tencent Cloud / Zhihu
- **公開日:** 2026-06 (継続更新)
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-05
- **関連企業:** ByteDance
- **要約:** ByteDance傘下のCoze（扣子）プラットフォームが個人版・チーム版・企業版の3階層でAIエージェント開発を提供。ゼロコードでスマートエージェント構築が可能。プラグイン機能で外部API呼び出し、ワークフロー構築をサポート。WeChat（微信）統合も可能。中国AIエージェントプラットフォーム市場の主要プレイヤー。
- **キーファクト:**
  - 3階層提供: 個人版（5段階）・チーム版（3段階）・企業版
  - ゼロコードエージェント構築可能
  - プラグイン機能: 外部API呼び出し・ワークフロー自動化
  - WeChat（微信）統合対応
  - 中国AIエージェント市場の主要プラットフォーム（百度・騰訊・阿里と競合）
- **引用URL:** https://www.coze.cn/open/docs/coze_pro/premium_package
- **Evidence ID:** EVD-20260623-0063

### INFO-064
- **タイトル:** OpenAI Q1 2026: Revenue $5.7B, cash burn $3.7B; Enterprise = 40%+ of annualized revenue; 2025 full year $13B revenue
- **ソース:** Fortune / SquaredTech / Reddit
- **公開日:** 2026-06-16
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001 (動的追加), H-OAI-001
- **関連企業:** OpenAI
- **要約:** OpenAIの漏洩財務諸表が詳細を明らかに。Q1 2026収益$5.7B（前年同期比3倍）だが$3.7Bのキャッシュバーン。2025年通年収益$13.07B（$3.7Bから3倍）、損失約$21B、支出$34B。エンタープライズ事業が年間化収益ランレートの40%+を寄与。ChatGPT Pro($200/月)のAPI等価価値は$14,000。年間収益ランレート$30B、週間ユーザー9億、加入者5000万+。
- **キーファクト:**
  - Q1 2026: 収益$5.7B / キャッシュバーン$3.7B
  - 2025通年: 収益$13.07B（前年$3.7Bから3倍）、損失~$21B、支出$34B
  - エンタープライズ: 年間化収益ランレートの40%+を寄与
  - 年間収益ランレート: $30B
  - ユーザー: 週間9億 / 加入者5000万+
  - ChatGPT Pro ($200/月) = API等価価値$14,000
  - API vs Enterprise vs Consumerの詳細内訳は依然不完全（KIQ-OAI-001未完全回答）
- **引用URL:** https://fortune.com/2026/06/16/openai-financials-leaked-losses-revenue-profit/
- **Evidence ID:** EVD-20260623-0064

### INFO-065
- **タイトル:** Pentagon used Grok AI to fire 2,000 missiles at 2,000 targets in 96 hours during Operation Epic Fury (Iran)
- **ソース:** The Hill / Yahoo News / The Independent / Reddit
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001 (動的追加), IND-030
- **関連企業:** xAI, Pentagon
- **要約:** ペンタゴン高官が、Operation Epic Fury（イラン攻撃）でElon MuskのGrok AIチャットボットを使用して「96時間以内に2,000の異なる標的に2,000発の弾薬を配備」したことを明かした。Grok Govシステムが「大幅な作戦効率向上」をもたらした。human-in-the-loopポリシーは維持されるが、96時間で2,000の標的選定では人間の実質的審査能力が崩壊している。米軍調査官はイランの女子校攻撃（175人死亡）で米軍の関与が「可能性高い」と判断。
- **キーファクト:**
  - Operation Epic Fury: 96時間で2,000標的に2,000弾薬を配備（Grok AI使用）
  - Grok Gov: 「大幅な作戦効率向上」を報告
  - human-in-the-loop: ポリシー維持するが速度が実質審査を崩壊させる
  - 女子校攻撃: Minabで175人死亡、米軍関与「可能性高い」
  - ウクライナ: Avengers AI platformが12,000の敵資産を特定可能
  - 議会: 自律型兵器への制限強化を求める動き
- **引用URL:** https://thehill.com/policy/technology/5928204-pentagon-musk-grok-chatbot-iran-strikes/
- **Evidence ID:** EVD-20260623-0065

### INFO-066
- **タイトル:** NSF slashes research programs 20-30%; Anthropic at $1T secondary market, raises $5B; Google DeepMind loses Jumper to Anthropic
- **ソース:** Science.org / Instagram / Bloomberg / PatentlyApple
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-GOV-002 (動的追加), H-GOV-002
- **関連企業:** Anthropic, Google/DeepMind, OpenAI
- **要約:** NSFが基礎科学研究プログラム予算を20-30%削減し新技術イニシアチブを支援。Anthropicはセカンダリ市場で$1T評価（OpenAI $880B）。今後2年で$5B調達を目指し12以上の主要産業に参入予定。安全性中心文化が研究者を惹因し、Google DeepMindからノーベル賞受賞者John JumperがAnthropicに移籍。ただし輸出管理措置で一部モデルの世界アクセス停止。安全性研究予算の経時的定量データは依然不在（KIQ-GOV-002絶対条件未達成継続）。
- **キーファクト:**
  - NSF: 基礎科学プログラム予算20-30%削減
  - Anthropic: セカンダリ市場$1T / 2年で$5B調達計画 / 12+産業参入
  - Google DeepMind: ノーベル賞John JumperがAnthropicに流出
  - 輸出管理: Anthropicの先進モデルの世界的アクセス停止
  - 安全性研究予算の経時データ: 依然不在（KIQ-GOV-002絶対条件19R→20R連続未達成）
- **引用URL:** https://www.science.org/content/article/exclusive-nsf-slashes-research-programs, https://x.com/PatentlyApple/article/2068088501057487196
- **Evidence ID:** EVD-20260623-0066
