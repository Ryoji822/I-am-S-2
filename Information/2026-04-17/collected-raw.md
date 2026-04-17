# 収集データ: 2026-04-17

## メタデータ
- 収集日時: 2026-04-17 00:00 UTC
- 品質フラグ: COLLECTING

## 動的追加クエリ（Arbiterフィードバックに基づく）
以下は arbiter-latest.md の「明日の収集で優先すべきKIQ」セクションから自動生成:
1. KIQ-ARR-001: Anthropic $30B ARR第三者検証（新規KIQ）
2. E2B/Daytona/Modal/Vercel契約条件: OpenAI専属 vs マルチプラットフォーム（新規）
3. KIQ-AGENT-001: Managed Agents採用データ（新規KIQ）
4. xAI代替仮説情報: Grok汎用AI基盤方向性（新規）
5. MCP Orchestration層拡張可能性: 技術評価（新規）
6. Fortune 500 42%デプロイ内訳: 実験的 vs 本番比率（新規）

## 収集結果

### INFO-001
- **タイトル:** Anthropic expands partnership with Google and Broadcom for multiple gigawatts of next-generation compute
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-002-01
- **関連企業:** Anthropic, Google, Broadcom
- **要約:** AnthropicがGoogleおよびBroadcomと複数GW規模の次世代TPUコンピュート契約を締結。2027年以降に稼働予定。run-rate revenueが$30Bを超え、$1M+/年顧客が2ヶ月で倍増（1,000社超）。$50Bの米国内インフラ投資拡大。
- **キーファクト:**
  - run-rate revenue $30B超（2025年末$9Bから急成長）
  - $1M+/年顧客1,000社超（Series G発表時500社から2ヶ月で倍増）
  - 複数GWのTPUコンピュート契約（2027年以降稼働）
  - AWS Trainium、Google TPU、NVIDIA GPUの3プラットフォームで訓練・実行
  - Amazonが引き続き主要クラウドプロバイダー・訓練パートナー
- **引用URL:** https://www.anthropic.com/news/google-broadcom-partnership-compute

### INFO-002
- **タイトル:** Anthropic invests $100 million into the Claude Partner Network
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-03-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Partner Networkを立ち上げ、$100Mを初期投資。パートナー向けにトレーニング、技術サポート、市場開発を提供。Claude Certified Architect認証を新設。Accentureが30,000人をClaude訓練中。
- **キーファクト:**
  - $100Mの初期投資（2026年）
  - パートナーチーム5倍増員
  - Claude Certified Architect認証新設
  - Accenture 30,000人訓練、Infosys 350,000人アクセス提供
  - Claude Code modernization starter kit提供
- **引用URL:** https://www.anthropic.com/news/claude-partner-network

### INFO-003
- **タイトル:** Claude for Financial Services
- **ソース:** Anthropic公式ブログ
- **公開日:** 2025-07-15（2026-04-10更新）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** 金融業界向けClaude包括ソリューションを提供。Vals AI Finance Agent benchmarkでClaude 4が他フロントイアモデルを凌駕。Box, Databricks, FactSet, S&P Global等とMCP連携。AWS Marketplaceで提供開始。
- **キーファクト:**
  - Claude 4がVals AI Finance Agent benchmarkで首位
  - FundamentalLabs Excel agent: 83%精度（Financial Modeling World Cup 5/7レベルクリア）
  - Databricks, Snowflake, S&P Global, FactSet, Morningstar等とMCP接続
  - Bridgewater, Commonwealth Bank of Australia, AIGが導入
  - AIG: 審査プロセス5倍高速化、データ精度75%→90%以上改善
- **引用URL:** https://www.anthropic.com/news/claude-for-financial-services

### INFO-004
- **タイトル:** Anthropic's Long-Term Benefit Trust appoints Vas Narasimhan to Board of Directors
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Long-Term Benefit TrustがNovartis CEO Vas Narasimhanを取締役に任命。Trust任命の取締役が過半数に。医療・ライフサイエンス分野でのAI活用推進が期待。
- **キーファクト:**
  - Novartis CEO Vas Narasimhanが取締役に就任
  - Trust任命取締役が過半数を占める（ガバナンス強化）
  - 35以上の新薬開発・承認経験
  - US National Academy of Medicine選出メンバー
- **引用URL:** https://www.anthropic.com/news/narasimhan-board

### INFO-005
- **タイトル:** Anthropic appoints Irina Ghose as Managing Director of India ahead of Bengaluru office opening
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-01-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** 元Microsoft India MDのIrina GhoseがAnthropicインドMDに就任。Bengaluruオフィス開設予定。インドはClaude.ai第2位市場。Claudeの利用のほぼ半分がコンピュータ・数学タスク。
- **キーファクト:**
  - インドはClaude.ai世界第2位市場
  - 元Microsoft India MDがAnthropicインド事業を牽引
  - インドユーザーのClaude利用の約半分がコンピュータ・数学タスク
- **引用URL:** https://www.anthropic.com/news/anthropic-appoints-irina-ghose-as-managing-director-of-india

### INFO-006
- **タイトル:** Run long horizon tasks with Codex
- **ソース:** OpenAI Developers Blog
- **公開日:** 2026-04（推定）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** GPT-5.3-Codexが25時間連続稼働で約30K行のコードを生成するデザインツールを構築。長時間タスクの一貫性維持が実証。METRの時間地平線ベンチマークで約7ヶ月の倍増期間を確認。Codex Appにプランモード、Skills、Automations機能追加。
- **キーファクト:**
  - GPT-5.3-Codexが25時間・13Mトークン・30K行コード生成を連続実行
  - METR時間地平線ベンチマーク: 約7ヶ月の倍増期間
  - GPT-5-Codex (2025年9月)→5.2 (12月)→5.3 (最新)の進化
  - Cursor「OpenAIモデルは長時間自律作業で明確に優秀」と評価
  - durable project memory（spec/plan/implement/documentation.md）の手法確立
- **引用URL:** https://developers.openai.com/blog/run-long-horizon-tasks-with-codex

### INFO-007
- **タイトル:** Gemini 3.1 Pro: A smarter model for your most complex tasks
- **ソース:** Google Blog
- **公開日:** 2026-02-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-005-01
- **関連企業:** Google / DeepMind
- **要約:** Gemini 3.1 Proがリリース。ARC-AGI-2で77.1%を達成（3 Proの2倍以上の推論性能）。Google AI Studio、Vertex AI、Gemini app、NotebookLMで利用可能。Agentic workflows向けにさらなる改良を予定。
- **キーファクト:**
  - ARC-AGI-2: 77.1%（3 Proの2倍以上の推論性能）
  - Google AI Studio、Antigravity、Vertex AI、Gemini CLI、Android Studioで提供
  - 消費者向け: Gemini app、NotebookLM
  - コードベースアニメーション（SVG）、複雑システム統合、インタラクティブデザインが可能
  - Preview版として提供、GA前にagentic workflowsのさらなる改善を計画
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/

### INFO-008
- **タイトル:** Gemini 3.1 Flash TTS: the next generation of expressive AI speech
- **ソース:** Google Blog
- **公開日:** 2026-04-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google / DeepMind
- **要約:** Gemini 3.1 Flash TTSがリリース。Artificial Analysis TTS leaderboardでElo 1,211を達成。70+言語対応、audio tagsによる音声制御、SynthID透かし入り。Google AI Studio、Vertex AI、Google Vidsで利用可能。
- **キーファクト:**
  - Artificial Analysis TTS leaderboard Elo 1,211
  - 70+言語対応
  - audio tagsによる音声スタイル・ペース・配信の制御
  - SynthID透かし技術によるAI生成音声の検出
  - Google AI Studio、Vertex AI、Google Vidsで提供開始
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-tts/

### INFO-009
- **タイトル:** Grok 3 Beta — The Age of Reasoning Agents
- **ソース:** xAI Blog
- **公開日:** 2025-02-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** xAI
- **要約:** xAIがGrok 3 Betaを発表。Colossusスーパークラスタで10倍のコンピュートで訓練。AIME'25 93.3%、GPQA 84.6%。DeepSearchエージェント、1Mコンテキストウィンドウ。Chatbot Arena Elo 1402。
- **キーファクト:**
  - AIME'25 93.3%（cons@64）、GPQA 84.6%、LiveCodeBench 79.4%
  - 1Mトークンのコンテキストウィンドウ
  - DeepSearch: 最初のエージェント機能
  - Chatbot Arena Elo 1402
  - APIリリース予定（Grok 3 / Grok 3 mini）
- **引用URL:** https://x.ai/blog/grok-3

### INFO-010
- **タイトル:** The next evolution of the Agents SDK — OpenAI
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-04-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-001-03
- **関連企業:** OpenAI
- **要約:** OpenAIがAgents SDKを大幅アップデート。ネイティブサンドボックス実行、モデルネイティブハーネスを追加。7つのサンドボックスプロバイダー（Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel）に対応。MCP、Skills、AGENTS.md、shell/apply-patch toolを統合。
- **キーファクト:**
  - 7サンドボックスプロバイダー対応: Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel
  - Manifest抽象化でAWS S3, GCS, Azure Blob, Cloudflare R2をマウント可能
  - ハーネスとコンピュートの分離設計（セキュリティ・耐久性・スケーラビリティ）
  - スナップショット＆リハイドレーションによる durable execution
  - Python版先行リリース、TypeScript版は今後対応
- **引用URL:** https://openai.com/index/the-next-evolution-of-the-agents-sdk/

### INFO-011
- **タイトル:** Introducing Claude Opus 4.7
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-005-01
- **関連企業:** Anthropic
- **要約:** Claude Opus 4.7がGAリリース。Opus 4.6から大幅なソフトウェアエンジニアリング性能向上。CursorBench 70%（Opus 4.6: 58%）、高解像度画像対応（最大3.75MP）。Cyber Verification Program新設。価格はOpus 4.6と同一（$5/$25 per MTok）。
- **キーファクト:**
  - CursorBench: 70%（Opus 4.6比+12pt）
  - XBOW visual-acuity: 98.5%（Opus 4.6: 54.5%）
  - SWE-bench系列でOpus 4.6を一貫して上回る
  - 画像解像度: 最大2,576px長辺（3.75MP、従来比3倍以上）
  - 新 effort level `xhigh` 追加（high/max間の細かい制御）
  - Task budgets（public beta）、`/ultrareview`スラッシュコマンド新設
  - Claude Code auto modeがMaxユーザーに拡大
- **引用URL:** https://www.anthropic.com/news/claude-opus-4-7

### INFO-012
- **タイトル:** Subagents have arrived in Gemini CLI
- **ソース:** Google Developers Blog
- **公開日:** 2026-04-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Google / DeepMind
- **要約:** Gemini CLIにサブエージェント機能が追加。メインセッションとは別のコンテキストウィンドウ・カスタム指示・ツールセットで動作する専門エージェント。並列実行対応。Markdown+YAMLでカスタムサブエージェント定義可能。
- **キーファクト:**
  - 一般用途、CLI ヘルプ、コードベース調査の3つの内蔵サブエージェント
  - カスタムサブエージェントは~/.gemini/agentsまたは.gemini/agentsに定義
  - 並列実行で複数エージェント同時稼働可能
  - @agent構文で明示的なタスク委任
  - Gemini CLI拡張機能としてバンドル可能
- **引用URL:** https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/

### INFO-013
- **タイトル:** xAI Voice Agent API
- **ソース:** xAI Docs
- **公開日:** 2026-04-10（最終更新）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIがVoice Agent APIを提供。WebSocketベースのリアルタイム音声対話。file_search, web_search, x_search, MCP, カスタム関数ツール対応。OpenAI Realtime API互換。20+言語対応。
- **キーファクト:**
  - 5音声（eve, ara, rex, sal, leo）対応
  - MCP（Model Context Protocol）サーバー接続対応
  - Web search, X search, Collections search組み込み
  - OpenAI Realtime API互換（ベースURL変更で移行可能）
  - 20+言語ネイティブ対応
- **引用URL:** https://docs.x.ai/developers/model-capabilities/audio/voice-agent

### INFO-014
- **タイトル:** OpenAI takes aim at Anthropic with beefed-up Codex
- **ソース:** TechCrunch
- **公開日:** 2026-04-16
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIがCodexを大幅アップデートしAnthropic Claude Codeに対抗。デスクトップアプリ操作、インアプリブラウザ、メモリ機能、画像生成、111プラグイン統合を追加。Enterprise向けpay-as-you-go価格設定。
- **キーファクト:**
  - バックグラウンドでデスクトップアプリ操作可能（マウス・キーボード制御）
  - インアプリブラウザ追加
  - メモリ機能（preview）でセッション間のコンテキスト維持
  - 111のプラグイン統合（CodeRabbit, GitLab Issues等）
  - pay-as-you-go価格設定（Enterprise/Business向け）
- **引用URL:** https://techcrunch.com/2026/04/16/openai-takes-aim-at-anthropic-with-beefed-up-codex-that-gives-it-more-power-over-your-desktop/

### INFO-015
- **タイトル:** The Hundred Shrimp War: OpenClaw and China's AI Agent Explosion
- **ソース:** Tech Buzz China (Substack)
- **公開日:** 2026-04-12
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-003-04
- **関連企業:** ByteDance, Zhipu, MiniMax
- **要約:** OpenClaw（オープンソースAIエージェントフレームワーク）が中国で爆発的普及。GitHub 350K stars（Reactの8年分を2日で達成）。GPUレンタル価格25-30%上昇。Zhipu/MiniMaxのAPI収益が急加速。モデル非依存設計が最重要のアーキテクチャ選択。
- **キーファクト:**
  - OpenClaw: 350K GitHub stars（Reactの8年分を2日で達成）
  - GPU H200レンタル価格1ヶ月で25-30%上昇
  - エージェントのコンピュート消費はチャットセッションの10-50倍
  - Zhipu (~$40B時価総額)、MiniMax (~$40B時価総額)が2026年1月に香港上場
  - フレームワーク層は既に無料、派生層も無料化競争、お金はコンピュート・トークン販売に流れる
- **引用URL:** https://techbuzzchina.substack.com/p/the-hundred-shrimp-war-openclaw-and

### INFO-016
- **タイトル:** Claude Agent SDK TypeScript v0.2.111 — Opus 4.7対応
- **ソース:** GitHub
- **公開日:** 2026-04-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版がv0.2.111でOpus 4.7対応。MCPサーバーのper-tool permission_policy、startup()/WarmQueryの公開API化、envオーバーレイ動作変更を含む。
- **キーファクト:**
  - v0.2.112まで2日間に3回リリース（活発な開発）
  - Opus 4.7の利用にv0.2.111が必要
  - MCP per-tool permission_policyサポート
  - 1.3K GitHub stars
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases


## X (Twitter) 投稿データ（ローカルRSSHub経由）

### INFO-017
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-04-17
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Samuel Marks
Cool to see that Meta conducted and published a pre-deployment investigation of Muse Spark behaviors like reward hacking, honesty, and evaluation awareness!

Summer Yue: 🚀 Muse Spark Safety & Preparedness Report for Meta AI is out.

We start with our pre-deployment assessment under Meta's Advanced AI Scaling Framework, covering chemical and biological, cybersecurity, and loss of control risks. Our assessment flagged potentially elevated chem/bio
- **引用URL:** https://x.com/sleepinyourhat/status/2044855322309963857

### INFO-018
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-04-17
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT cat
Opus 4.7 is live in Claude Code today! 

The model performs best if you treat it like an engineer you're delegating to, not a pair programmer you're guiding line by line. Here are three workflow shifts we recommend for this model 🧵

https://www.anthropic.com/news/claude-opus-4-7
- **引用URL:** https://x.com/sleepinyourhat/status/2044827603417305503

### INFO-019
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-04-17
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Nathan Calvin
This part of the 4.7 Opus system card is pretty neat and seems potentially worth emulating (Anthropic showed Mythos the private discussions/evidence underlying the system card and asked Mythos if the Opus system card accurately characterized that private evidence)

Drake Thomas: @TheZvi Less juicy overall than last time, but I was happy we got to fit in section 6.1.3:
- **引用URL:** https://x.com/sleepinyourhat/status/2044809556988166550

### INFO-020
- **タイトル:** @GoogleDeepMind (Google DeepMind) のX投稿
- **ソース:** X (Twitter) - @GoogleDeepMind (公式アカウント)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** RT Eli Collins
Big news: "Dear Upstairs Neighbors" is premiering at @Tribeca! 🎬 Inspired by a sleepless pandemic night, our 45-person crew of Pixar alumni, an Academy Award winner, researchers, and engineers developed new workflows to bring original artwork and paintings to life. @GoogleDeepMind

Tribeca: Here we go!

Today we announced our full feature film lineup for the milestone 25th Tribeca Festival — a program that reflects where independent film has been and where it's headed.

Official S...
- **引用URL:** https://x.com/GoogleDeepMind/status/2044865278069084456

### INFO-021
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Won Park
Image generation is now live in Codex!

You can now generate visuals, edit existing images, and create GIFs from a single image directly inside Codex.

I spent a lot of time testing different use cases while working on this feature, and it was genuinely impressive to see how creative and useful the outputs could be.

Hope you enjoy 🚀
- **引用URL:** https://x.com/OpenAIDevs/status/2044848085424353634

### INFO-022
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT pash
Biggest lesson from OpenClaw is that a good teammate doesn't start from scratch everytime you check in. They remember what was decided, what's still open, and  proactively help you.

Today we launched heartbeats in Codex: automations that maintain context inside a single thread over time. 

Instead of each run starting fresh, Codex wakes up in the same conversation, with the history and context it needs already in place. You can also have it schedule its own next steps – just ask Codex.
...
- **引用URL:** https://x.com/OpenAIDevs/status/2044854702270243100

### INFO-023
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Kieraj Mumick
Re Onboarding + Permissions: Its so whimsical! Try it, and you'll see how slick this is
- **引用URL:** https://x.com/OpenAIDevs/status/2044870561097261398

### INFO-024
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Thomas Ricouard
One of the best things about this Codex app update is how good it is to work with other things than code! The app can now preview all kinds of documents natively, including spreadsheets!
- **引用URL:** https://x.com/OpenAIDevs/status/2044835431745986911

### INFO-025
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Tibo
Codex just got a lot more powerful.

Computer use, in-app browser, image generation and editing, 90+ new plugins to connect to everything, multi-terminal, SSH into devboxes, thread automations, rich document editing. Learns from experience and proactively suggestions work. And a ton more.
- **引用URL:** https://x.com/OpenAIDevs/status/2044835414004175074

### INFO-026
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** “People aren’t just building for humans anymore. They’re building for agents.”

@Cloudflare shares how Cloudflare Sandbox SDK works with the OpenAI Agents SDK to help agents run code in secure environments while keeping sensitive data separate from execution.
- **引用URL:** https://x.com/OpenAIDevs/status/2044808272289701935

### INFO-027
- **タイトル:** @sama (Sam Altman) のX投稿
- **ソース:** X (Twitter) - @sama (CEO)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Ari Weinstein
This is the first time I've ever seen an LLM operate a GUI as fast as a person, and it's surreal.
- **引用URL:** https://x.com/sama/status/2044858929491202435

### INFO-028
- **タイトル:** @npew (Peter Welinder) のX投稿
- **ソース:** X (Twitter) - @npew (研究・技術)
- **公開日:** 2026-04-17
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Tibo
Codex just got a lot more powerful.

Computer use, in-app browser, image generation and editing, 90+ new plugins to connect to everything, multi-terminal, SSH into devboxes, thread automations, rich document editing. Learns from experience and proactively suggestions work. And a ton more.
- **引用URL:** https://x.com/npew/status/2044848059922948252

