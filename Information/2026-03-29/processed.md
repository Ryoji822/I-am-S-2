# 収集データ: 2026-03-29

## メタデータ
- 収集日時: 2026-03-29 00:00 UTC
- 収集完了: 2026-03-29 (52件収集)
- 品質フラグ: ANALYSIS_PENDING
- 動的追加クエリ（Arbiter指示）:
  - KIQ-RED-005: AI ROI定量データ
  - KIQ-RED-009: Claude Code チャーン率・NPS
  - KIQ-RED-007: 複数ベンチマーク比較
  - KIQ-RED-006: OpenAI囲い込み指標
  - KIQ-NEW-SDK: SDK相互運用性

## 収集結果

### INFO-001
- **タイトル:** Updates to Consumer Terms and Privacy Policy
- **ソース:** Anthropic公式ブログ
- **公開日:** 2025-08-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02（エンタープライズ展開）
- **関連企業:** Anthropic
- **要約:** Anthropicが消費者向け利用規約とプライバシーポリシーを更新。Free/Pro/Maxユーザーに対し、モデルトレーニングへのデータ使用をオプトイン形式で提供。データ保持期間を5年に延長（オプトイン時）。商用利用（Claude for Work/API/Bedrock/Vertex）には適用されない。
- **キーファクト:**
  - モデルトレーニングへのデータ使用はユーザー選択制（オプトイン）
  - データ保持期間: 5年（オプトイン時）、30日（オプトアウト時）
  - 商用利用（Claude for Work、API、Bedrock、Vertex）には適用外
- **引用URL:** https://www.anthropic.com/news/updates-to-our-consumer-terms

### INFO-002
- **タイトル:** Sydney will become Anthropic's fourth office in Asia-Pacific
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-03-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02（エンタープライズ展開）
- **関連企業:** Anthropic
- **要約:** AnthropicがシドニーにAPAC4拠点目のオフィスを開設。東京、バンガロール、ソウルに続く拡大。Canva、Quantium、CBA等の顧客対応強化。豪州でのコンピュート拡張も検討中。
- **キーファクト:**
  - シドニーオフィス開設（APAC4拠点目: 東京・バンガロール・ソウル・シドニー）
  - 豪州・NZは人口比Claude使用率で世界4位・8位
  - 主要顧客: Canva, Quantium, Commonwealth Bank of Australia
  - 豪州でのコンピュート拡張（第三者パートナー経由）を検討中
- **引用URL:** https://www.anthropic.com/news/sydney-fourth-office-asia-pacific

### INFO-003
- **タイトル:** Accenture and Anthropic launch multi-year partnership to move enterprises from AI pilots to production
- **ソース:** Anthropic公式ブログ
- **公開日:** 2025-12-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-02, KIQ-001-03, KIQ-RED-009
- **関連企業:** Anthropic, Accenture
- **要約:** Accentureとの戦略的パートナーシップ拡大。Accenture Anthropic Business Groupを設立、約3万名がClaude訓練を受ける。Claude CodeがAIコーディング市場の50%超を獲得（Menlo Ventures調査）。エンタープライズシェア24%→40%に成長。
- **キーファクト:**
  - Accenture Anthropic Business Group設立（戦略パートナー指定）
  - 約30,000名のAccenture従業員がClaude訓練を受ける
  - Claude Code: AIコーディング市場シェア50%超（Menlo Ventures 2025調査）
  - エンタープライズシェア: 24%→40%に成長
  - 規制産業向けソリューション（金融、ライフサイエンス、医療、公共部門）
- **引用URL:** https://www.anthropic.com/news/anthropic-accenture-partnership

### INFO-004
- **タイトル:** Update on the OpenAI Foundation
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-03-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04（資金調達・投資動向）, KIQ-005-03（AGI安全性）
- **関連企業:** OpenAI
- **要約:** OpenAI Foundationが少なくとも$1Bを生命科学・疾患治癒、雇用・経済影響、AIレジリエンス、コミュニティプログラムに投資。Alzheimer研究・公共健康データ・バイオセキュリティに注力。Wojciech Zaremba（共同創業者）がAI Resilience責任者に就任。
- **キーファクト:**
  - 年間投資: $1B以上（生命科学・雇用・AIレジリエンス・コミュニティ）
  - 重点分野: Alzheimer AI研究、公共健康データ、バイオセキュリティ
  - Wojciech Zaremba（OpenAI共同創業者）がAI Resilience責任者
  - Anna MakanjuがAI for Civil Society責任者に就任（4月着任）
- **引用URL:** https://openai.com/index/update-on-the-openai-foundation/

### INFO-005
- **タイトル:** OpenAI announces plans to shut down its Sora video generator
- **ソース:** Ars Technica
- **公開日:** 2026-03-24
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）, KIQ-003-04（投資動向）
- **関連企業:** OpenAI, ByteDance, Google
- **要約:** OpenAIがSora動画生成サービスを終了。2024年12月公開から約15ヶ月。競合のByteDance SeeDance 2.0、Google Veoが市場を拡大中。Disneyの$1B投資契約（200キャラクターライセンス）の行方が不透明。
- **キーファクト:**
  - Sora終了: 2024年12月公開から約15ヶ月
  - Disney投資: $1B（200キャラクターライセンス）の継続が不明
  - 競合状況: ByteDance SeeDance 2.0、Google Veoが市場拡大中
  - 終了理由: 「ビジネス・生産性ユースケースへの再集中」（Fidji Simo発言）
- **引用URL:** https://arstechnica.com/ai/2026/03/openai-plans-to-shut-down-sora-just-15-months-after-its-launch/

### INFO-006
- **タイトル:** OpenAI secures an extra $10 billion in record funding round, CFO Friar says
- **ソース:** CNBC
- **公開日:** 2026-03-24
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04（資金調達・投資動向）, KIQ-001-02（エンタープライズ展開）
- **関連企業:** OpenAI, Microsoft, Amazon, Nvidia, SoftBank
- **要約:** OpenAIの資金調達が$120Bに到達（当初目標$100B超過）。追加投資家: a16z、D.E. Shaw、MGX、TPG、T. Rowe Price、Microsoft。収益は約$13.1B（2025年）、消費者60%・エンタープライズ40%。
- **キーファクト:**
  - 調達総額: $120B（評価額$730B前提）
  - 新規投資家: a16z, D.E. Shaw, MGX, TPG, T. Rowe Price, Microsoft
  - 収益: 約$13.1B（2025年）、消費者60%・エンタープライズ40%
  - ChatGPT週間アクティブユーザー: 9億人
  - IPO準備: 「市場に向けて構築中」（Friar CFO）
- **引用URL:** https://www.cnbc.com/2026/03/24/openai-secures-an-extra-10-billion-in-record-funding-round-cfo-friar-says.html

### INFO-007
- **タイトル:** Gemini Drops: New updates to the Gemini app, March 2026
- **ソース:** Google公式ブログ
- **公開日:** 2026-03-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）, KIQ-001-04（マルチモーダル）
- **関連企業:** Google
- **要約:** Google Geminiアプリの3月アップデート。他社からのチャット履歴移行、Personal Intelligence（Gmail/Photos/YouTube連携）無料化、Google TVでのGemini統合、Lyria 3 Pro（3分楽曲生成）、Gemini Live 3.1（コンテキスト2倍化）。
- **キーファクト:**
  - チャット履歴移行: 他社からGeminiへ数クリックで移行可能
  - Personal Intelligence: 全米ユーザーに無料提供（Gmail/Photos/YouTube連携）
  - Lyria 3 Pro: 最大3分の楽曲生成
  - Gemini Live 3.1: コンテキスト保持期間2倍、より自然な会話
- **引用URL:** https://blog.google/innovation-and-ai/products/gemini-app/gemini-drop-updates-march-2026/

### INFO-008
- **タイトル:** 3 new Gemini features are coming to Google TV
- **ソース:** Google公式ブログ
- **公開日:** 2026-03-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）, KIQ-001-01（機能拡張）
- **関連企業:** Google
- **要約:** Google TVにGemini機能を追加。リッチな視覚的応答（スポーツスコア・レシピ動画）、Deep Dives（教育コンテンツのナレーション付き解説）、Sports Briefs（NBA/NHL/MLB等のハイライト）。米国・カナダで展開開始、春に豪州・NZ・英国へ拡大。
- **キーファクト:**
  - 視覚的応答: スポーツスコア、レシピ動画など
  - Deep Dives: 健康・経済・技術等の教育コンテンツ（ナレーション付き）
  - Sports Briefs: NBA, NCAA, NHL, MLB, MLS, NWSL対応
  - 展開地域: 米国・カナダ開始、春に豪州・NZ・英国拡大
- **引用URL:** https://blog.google/products-and-platforms/platforms/google-tv/new-gemini-features-march-2026/

### INFO-009
- **タイトル:** Google is launching Search Live globally
- **ソース:** TechCrunch
- **公開日:** 2026-03-26
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01（Agent機能拡張）, KIQ-001-04（マルチモーダル）
- **関連企業:** Google
- **要約:** GoogleがSearch Live（AI会話型検索）を200カ国以上に拡大。カメラでリアルタイム視覚コンテキストを取得し音声で対話。Gemini 3.1 Flash Liveモデルで実現。同時にGoogle TranslateのLive TranslateもiOSと複数国に拡大。
- **キーファクト:**
  - Search Live: 200カ国以上で利用可能（AI Mode利用可能地域）
  - 機能: カメラでリアルタイム視覚コンテキスト＋音声会話
  - 基盤モデル: Gemini 3.1 Flash Live
  - Live Translate: iOS対応、70言語以上、11カ国で展開
- **引用URL:** https://techcrunch.com/2026/03/26/google-is-launching-search-live-globally/

### INFO-010
- **タイトル:** Musk Promises 'Epic' Grok Video Generator After Sora Shuttered By OpenAI
- **ソース:** Forbes
- **公開日:** 2026-03-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）, KIQ-003-04（投資動向）
- **関連企業:** xAI, OpenAI
- **要約:** Elon MuskがOpenAIのSora終了を受け、Grok Imagineの次期リリースで「doubling down」を宣言。Grok Imagineは「spicy mode」で性的コンテンツ生成が可能で、複数の訴訟・規制調査対象。
- **キーファクト:**
  - Musk発言: 「次期Grok Imagineリリースはepicになる」「doubling down」
  - Grok Imagine: $10/月で画像・6秒動画生成可能
  - 論争: 「spicy mode」で性的コンテンツ生成、9日間で180万枚の性的画像生成
  - 規制調査: Ofcom（英国）、仏・加・米各州で調査中
- **引用URL:** https://www.forbes.com/sites/conormurray/2026/03/25/musk-promises-epic-grok-video-generator-after-sora-shuttered-by-openai/

### INFO-011
- **タイトル:** Grok Is Getting Faster and Smarter Every Week, Musk Says
- **ソース:** BASENOR
- **公開日:** 2026-03-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）
- **関連企業:** xAI, Tesla
- **要約:** Elon Muskが「Grokは毎週より速く、より賢くなっている」とXで発言。週次改善サイクルを確認。Tesla製品スタックへの統合が進行中。
- **キーファクト:**
  - Musk発言: 「Grokは毎週より速く、より賢くなっている」
  - 週次イテレーションサイクルを確認
  - Tesla製品スタック（音声アシスタント、車内検索、FSD）への統合示唆
- **引用URL:** https://www.basenor.com/blogs/news/grok-is-getting-faster-and-smarter-every-week-musk-says

### INFO-012
- **タイトル:** Claude Agent SDK v0.2.86 Released
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-03-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版がv0.2.86に更新。getContextUsage()でコンテキストウィンドウ使用量をカテゴリ別に取得可能に。session_idがオプション化され、SDKが自動割り当て。TypeScript型解決のany問題を修正。
- **キーファクト:**
  - getContextUsage(): コンテキスト使用量をカテゴリ別に取得
  - session_id: SDKが自動割り当て、呼び出し元での提供不要
  - TypeScript型: @anthropic-ai/sdk, @modelcontextprotocol/sdkを依存関係に追加
  - Claude Code v2.1.86とのパリティ達成
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases

### INFO-013
- **タイトル:** OpenAI Apps SDK March 2026 Updates
- **ソース:** OpenAI Developers
- **公開日:** 2026-03-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）
- **関連企業:** OpenAI
- **要約:** OpenAI Apps SDKが3月更新。承認済みアプリはCodexでPluginとして配布。window.openai.selectFiles()でChatGPTファイルライブラリからファイル選択、uploadFile()でライブラリへの保存が可能に。非画像ファイルアップロード対応。
- **キーファクト:**
  - Plugin distribution: 承認済みアプリをCodex用Pluginに変換
  - selectFiles(): ChatGPTファイルライブラリからファイル選択
  - uploadFile(file, {library: true}): ファイルライブラリに保存
  - 非画像ファイルタイプ対応
- **引用URL:** https://developers.openai.com/apps-sdk/changelog

### INFO-014
- **タイトル:** Google Gemini API Skills for Coding Agents
- **ソース:** Google Developers Blog
- **公開日:** 2026-03-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）, KIQ-001-03（開発者エコシステム）
- **関連企業:** Google
- **要約:** Google DeepMindがGemini API開発者スキルを公開。LLMの固定知識と急速に変化するSDK間のギャップを埋める軽量手法。117プロンプトの評価で、Gemini 3.1 Proはスキル追加で6.8%→96.6%に改善。
- **キーファクト:**
  - 評価結果: Gemini 3.1 Pro 6.8%→96.6%（スキル追加時）
  - スキル内容: API機能説明、モデル/SDK一覧、サンプルコード、ドキュメントリンク
  - GitHub公開: google-gemini/gemini-skills
  - スキルインストール: Vercel skills CLI / Context7 CLI
- **引用URL:** https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills/

### INFO-015
- **タイトル:** Build real-time conversational agents with Gemini 3.1 Flash Live
- **ソース:** Google公式ブログ
- **公開日:** 2026-03-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）, KIQ-001-04（マルチモーダル）
- **関連企業:** Google
- **要約:** Gemini 3.1 Flash LiveがLive APIでプレビュー公開。リアルタイム音声・視覚エージェント構築用。ノイズ環境でのタスク完了率向上、複雑な指示への従順性強化、90言語以上対応。
- **キーファクト:**
  - ノイズ耐性: 環境音（交通、TV）から音声を識別
  - 指示従順性: 複雑なシステム指示への従順性強化
  - 多言語: 90言語以上のリアルタイムマルチモーダル会話
  - パートナー統合: LiveKit, Pipecat, VisionAgents等
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-3-1-flash-live/

### INFO-016
- **タイトル:** xAI Grok 4.20 Overview
- **ソース:** xAI Documentation
- **公開日:** 2026-03-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）
- **関連企業:** xAI
- **要約:** Grok 4.20がxAIの最新フラッグシップモデル。業界最速の速度とエージェントツール呼び出し能力を組み合わせ。市場最低のハルシネーション率と厳格なプロンプト準拠。2Mコンテキストウィンドウ。
- **キーファクト:**
  - コンテキストウィンドウ: 2,000,000 tokens
  - 機能: Function calling, Structured outputs, Reasoning, Lightning fast
  - マルチモーダル: 対応
  - ツール: Web search, X search, Code execution, Collections search, Remote MCP
- **引用URL:** https://docs.x.ai/overview

### INFO-017
- **タイトル:** ByteDance's Feishu Updates OpenClaw-Style AI Agent
- **ソース:** Yicai Global
- **公開日:** 2026-03-20
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）
- **関連企業:** ByteDance
- **要約:** ByteDanceのFeishuがAIエージェント「Aily」を更新。OpenClaw類似の能力を企業シナリオ向けに提供。業務メモリ蓄積、業務・コミュニケーション嗜好理解、公式認証スキルインストール対応。
- **キーファクト:**
  - OpenClaw類似能力を企業向けにカスタマイズ
  - 業務メモリ蓄積機能
  - 公式認証プロスキルのインストール
  - 権限システムはユーザーと厳格に一致、操作プロセスは追跡可能
- **引用URL:** https://www.yicaiglobal.com/news/bytedances-feishu-updates-openclaw-style-ai-agent

### INFO-018
- **タイトル:** DeerFlow 2.0 - ByteDance's Open-Source SuperAgent
- **ソース:** VentureBeat
- **公開日:** 2026-03-24
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）, KIQ-003-03（OSS vs商用）
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0をリリース。複数AIサブエージェントをオーケストレーションする「SuperAgent harness」。MITライセンスで商用利用可能。39,000+スター、4,600+フォーク。LangGraph 1.0上で再構築。
- **キーファクト:**
  - GitHub: 39,000+ stars, 4,600+ forks
  - ライセンス: MIT（商用利用無料）
  - アーキテクチャ: LangGraph 1.0 + LangChain
  - デプロイ: ローカル、Kubernetes、Slack/Telegram統合
  - モデル: OpenAI互換API全般、Doubao-Seed、DeepSeek、Claude等
- **引用URL:** https://venturebeat.com/orchestration/what-is-deerflow-and-what-should-enterprises-know-about-this-new-local-ai

### INFO-019
- **タイトル:** Long-running Claude for Scientific Computing
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-03-23
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）, KIQ-005-01（AGI到達度）
- **関連企業:** Anthropic
- **要約:** Anthropicが多日跨ぎエージェントコーディングワークフローを解説。CLAUDE.md、CHANGELOG.md（進捗ファイル）、テストオラクル、Ralphループ等のパターンを紹介。HPCクラスタ上でClaude Opus 4.6が宇宙論Boltzmannソルバーを数日で実装し、サブパーセント精度を達成。
- **キーファクト:**
  - 多日跨ぎエージェントワークフロー: CLAUDE.md（指示ファイル）+ CHANGELOG.md（進捗管理）
  - テストオラクル: 参照実装との比較で自律的に進捗確認
  - Ralphループ: エージェントの怠惰（agentic laziness）を回避する反復パターン
  - 成果: 宇宙論Boltzmannソルバーを数日で実装（通常数ヶ月〜数年）
- **引用URL:** https://www.anthropic.com/research/long-running-Claude

### INFO-020
- **タイトル:** Claude Certified Architect – Foundations (CCA-F) Full Curriculum
- **ソース:** The AI Corner
- **公開日:** 2026-03-23
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）, KIQ-RED-009（Claude Code関連）
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Certified Architect認定プログラムを開始。5ドメイン構成: Agentic Architecture (27%), Claude Code Configuration (20%), Prompt Engineering (20%), Tool Design & MCP (18%), Context Management (15%)。パートナー限定だが内容は公開。
- **キーファクト:**
  - 5ドメイン: Agentic Architecture 27%, Claude Code Config 20%, Prompt Engineering 20%, Tool Design & MCP 18%, Context Management 15%
  - 試験はAnthropic公式パートナー限定
  - 内容: 本番級AIアプリケーション構築能力をテスト
  - Claude Code, Agent SDK, API, MCPを網羅
- **引用URL:** https://www.the-ai-corner.com/p/claude-certified-architect-curriculum-2026

### INFO-021
- **タイトル:** The Agentic AI Inflection Point: Scaling Beyond Pilots
- **ソース:** Medium
- **公開日:** 2026-03-27
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-RED-005（AI ROI定量データ）, KIQ-002-02（エンタープライズ採用率）
- **関連企業:** N/A（調査レポート）
- **要約:** Agentic AIの転換点を分析。Gartner予測: 2026年末までに40%のエンタープライズアプリがタスク特化AIエージェントを統合（現在5%未満から8倍増）。一方、40%のプロジェクトが2027年までにROI不明確でキャンセルのリスク。2035年には$450B収益の可能性。
- **キーファクト:**
  - 採用予測: 2026年末に40%のエンタープライズアプリがエージェント統合（現在<5%）
  - 2035年潜在収益: $450B
  - 失敗リスク: 40%のプロジェクトが2027年までにキャンセル（コスト増・ROI不明確）
  - ROI実績: 68%の組織が平均2.8xのROI（IDC調査）
- **引用URL:** https://medium.com/@roshni_k06/the-agentic-ai-inflection-point-scaling-beyond-pilots-for-tangible-business-value-329dba134545

### INFO-022
- **タイトル:** 2026 AI API Comparison: OpenAI vs Claude vs Gemini vs Grok
- **ソース:** AI.cc
- **公開日:** 2026-03-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01（API料金改定）, KIQ-003-02（ベンチマーク比較）
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** 2026年3月時点の主要LLM API価格・ベンチマーク比較。価格収束が進むが差は依然大きい。Grok 4.1 Fastが最安（$0.20/$0.50）、Claude Opus 4.6が最高値（$5/$25）。ベンチマックはGemini 3.1 ProがGPQA Diamond 94.3%、ARC-AGI-2 77.1%でリード。
- **キーファクト:**
  - 価格: Grok 4.1 Fast $0.20/$0.50, Gemini 3 Flash $0.50/$3, Claude Sonnet 4.6 $3/$15, Claude Opus 4.6 $5/$25
  - GPQA Diamond: Gemini 3.1 Pro 94.3%, GPT-5.4 92.8%, Claude Opus 4.6 91.3%
  - ARC-AGI-2: Gemini 3.1 Pro 77.1%, Claude Opus 4.6 68.8%, GPT-5.4 ~70%
  - SWE-Bench: Claude Opus 4.6 80.8%, Gemini 3.1 Pro 80.6%
- **引用URL:** https://www.ai.cc/blogs/2026-ai-api-comparison-openai-claude-gemini-grok-pricing-performance/

### INFO-023
- **タイトル:** LLM Leaderboard 2026 - Comprehensive Benchmark Rankings
- **ソース:** Onyx.app
- **公開日:** 2026-03-24
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-RED-007（複数ベンチマーク比較）, KIQ-003-02（性能推移）
- **関連企業:** OpenAI, Anthropic, Google, DeepSeek, xAI, Meta, Mistral
- **要約:** 包括的LLMランキング公開。S-Tier: Claude Opus 4.6, GPT-5.4, GLM-5, Kimi K2.5, DeepSeek V3.2。Chatbot Arena 1位はClaude Opus 4.6 (1503)。中国モデル（GLM-5, Kimi K2.5, Qwen 3.5）が台頭。MMLU-ProはKimi K2.5が87.1%でリード。
- **キーファクト:**
  - S-Tier: Claude Opus 4.6, GPT-5.4, GLM-5 (744B), Kimi K2.5 (1T), DeepSeek V3.2 (685B)
  - Chatbot Arena 1位: Claude Opus 4.6 (1503)
  - GPQA Diamond 1位: Gemini 3.1 Pro (91.9%)
  - SWE-Bench Verified 1位: Claude Opus 4.6 (80.8%)
  - LiveCodeBench 1位: Gemini 3.1 Pro (81.3%)
- **引用URL:** https://onyx.app/llm-leaderboard

### INFO-024
- **タイトル:** EU AI Act Enforcement Starts August 2026
- **ソース:** Reddit / CIO.com
- **公開日:** 2026-03-26
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03（規制環境）, KIQ-002-06（政府圧力）
- **関連企業:** N/A（規制）
- **要約:** EU AI Actの強制執行が2026年8月2日に開始。欧州ユーザーがいれば米国企業も対象。違反罰金は最大€35Mまたは年間売上高の7%。欧州議会は一部実装の延期を可決。CIOにとって計画上の課題となっている。
- **キーファクト:**
  - 強制執行開始: 2026年8月2日
  - 適用範囲: 欧州ユーザーがいれば米国企業も対象
  - 罰金: 最大€35Mまたは年間売上高の7%
  - 欧州議会: 一部条項の実装延期を可決
- **引用URL:** https://www.cio.com/article/4150989/european-parliament-delays-implementation-of-parts-of-the-eu-ai-act.html

### INFO-025
- **タイトル:** AI Job Losses and Tech Layoffs in 2026
- **ソース:** TechCrunch / Reddit
- **公開日:** 2026-03-26
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01（業務自律化）, KIQ-004-02（コーディング能力市場価値）
- **関連企業:** Block, C3.ai, Microsoft
- **要約:** AIによる雇用喪失の兆候が蓄積。米国のエントリーレベル求人が2023年から35%減少。Block（旧Square）が4,000人削減（40%カット）。「AIレイオフ」と明記する企業を追跡するトラッカーも登場。KlarnaはAI顧客サポート失敗後に人員を再雇用。
- **キーファクト:**
  - エントリーレベル求人: 2023年から35%減少（米国）
  - Block: 4,000人削減（40%カット）、AI理由と明記
  - C3.ai: 26%削減、自動化による再編
  - Klarna: AI顧客サポート失敗後、人員再雇用
  - 2026年1月: 7,624件のレイオフが自動化に直接起因（約7%）
- **引用URL:** https://techcrunch.com/2026/03/26/a-pound-of-flesh-from-data-centers-one-senators-answer-to-ai-job-losses/

### INFO-026
- **タイトル:** MCP (Model Context Protocol) Adoption in 2026
- **ソース:** WorkOS / ChiefMartec
- **公開日:** 2026-03-27
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03（開発者エコシステム）, KIQ-NEW-SDK（SDK相互運用性）
- **関連企業:** Anthropic
- **要約:** MCPがAIモデルと外部ツール・データソースを接続するオープン標準として普及。2024年11月Anthropicが導入。56以上の本番対応MCPサーバーがネットワーク自動化だけで存在。統合の普遍化が逆にエコシステム戦略をより重要にしている。
- **キーファクト:**
  - MCP: Anthropicが2024年11月に導入したオープン標準
  - 56以上の本番対応MCPサーバーがネットワーク自動化分野に存在
  - 統合の普遍化が逆にエコシステム戦略を強化（ベンダーロックイン懸念）
  - セキュリティ: AI Tool Tunneling等の新課題
- **引用URL:** https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026

### INFO-027
- **タイトル:** GitAgent - Docker for AI Agents
- **ソース:** MarkTechPost
- **公開日:** 2026-03-22
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-NEW-SDK（SDK相互運用性）, KIQ-001-03（開発者エコシステム）
- **関連企業:** N/A（OSS）
- **要約:** GitAgentがLangChain、AutoGen、Claude Code間の断絶を解決する「Docker for AI Agents」として登場。異なるエージェントフレームワーク間の相互運用性を提供。エージェント実行環境の標準化を目指す。
- **キーファクト:**
  - LangChain、AutoGen、Claude Code間の断絶を解決
  - 「Docker for AI Agents」として位置付け
  - 異なるフレームワーク間の相互運用性を提供
  - エージェント実行環境の標準化を目指す
- **引用URL:** https://www.marktechpost.com/2026/03/22/meet-gitagent-the-docker-for-ai-agents-that-is-finally-solving-the-fragmentation-between-langchain-autogen-and-claude-code/

### INFO-028
- **タイトル:** Anthropic Economic Index: Learning Curves (March 2026)
- **ソース:** Anthropic公式研究レポート
- **公開日:** 2026-03-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-RED-005（AI ROI定量データ）, KIQ-004-01（業務自律化）
- **関連企業:** Anthropic
- **要約:** Anthropicが100万件のClaude会話を分析した経済指数レポート第5版。高 tenureユーザー（6ヶ月以上）は10%高い成功率を達成。API経由でコーディングタスクが増加、Claude.aiでは個人利用が増加（35%→42%）。49%の職業でタスクの25%以上がClaudeで実行。
- **キーファクト:**
  - 高tenureユーザー: 10%高い会話成功率、6%高い教育レベルのタスク
  - タスク分散: トップ10タスクが会話の24%→19%に減少
  - 個人利用: 35%→42%に増加
  - 職業カバレッジ: 49%の職業でタスクの25%以上がClaudeで実行
  - 地理的収束: 米国州間では進行中、国際間では不平等拡大
- **引用URL:** https://www.anthropic.com/research/economic-index-march-2026-report

### INFO-029
- **タイトル:** Why China Is Winning The Open Source AI Race
- **ソース:** Forbes
- **公開日:** 2026-03-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03（OSS vs商用性能ギャップ）, KIQ-002-03（中国AI規制）
- **関連企業:** DeepSeek, Qwen, ByteDance
- **要約:** 中国がオープンソースAI競争で優位に。DeepSeekとQwenが開発者採用で先行。DeepSeek Shockから1年、中国はオープンソース戦略を強化。ユーザーは無料でダウンロードしローカル実行可能。
- **キーファクト:**
  - DeepSeek V3: 経済的コストで訓練されたオープンウェイトモデルがクローズドソースに匹敵
  - Qwen: 開発者採用が拡大
  - オープンソース戦略: 無料ダウンロード・ローカル実行が採用を促進
  - DeepSeek Shockから1年: 中国のオープンソース優位が継続
- **引用URL:** https://www.forbes.com/sites/timkeary/2026/03/25/why-china-is-winning-the-open-source-ai-race/

### INFO-030
- **タイトル:** LLM Coding Benchmarks Guide - Contamination & SWE-Bench
- **ソース:** Openlayer
- **公開日:** 2026-03-27
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-RED-007（複数ベンチマーク比較・汚染チェック）
- **関連企業:** N/A（ベンチマーク分析）
- **要約:** LLMコーディングベンチマークの包括的ガイド。SWE-benchが本番パフォーマンスをより予測。データ汚染（contamination）がコーディングベンチマークの「サイレントキラー」。LiveCodeBenchが汚染回避評価を提供。
- **キーファクト:**
  - SWE-bench: 本番パフォーマンスをより正確に予測
  - データ汚染: モデルがテストセットで訓練されているとスコアが無意味
  - LiveCodeBench: 汚染のない包括的コード評価ベンチマーク
  - Claude Opus 4.6: SWE-bench Verified 80.8%, LiveCodeBench 76.0%
- **引用URL:** https://www.openlayer.com/blog/post/llm-coding-benchmarks-complete-guide

### INFO-031
- **タイトル:** Amazon Bedrock in 2026 - AWS AI Platform Guide
- **ソース:** ThinkMove Solutions
- **公開日:** 2026-03-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-01（クラウドプロバイダーAI Agent統合）
- **関連企業:** Amazon AWS
- **要約:** Amazon BedrockがClaude、OpenAI等を統合実行するAWS AIプラットフォームとして進化。OpenClaw on Amazon Lightsailで自律的プライベートAIエージェント実行が可能に。Bedrock Agentsでアプリケーション内自律エージェント構築対応。
- **キーファクト:**
  - Bedrock: Claude、OpenAI等のマルチモデル統合プラットフォーム
  - OpenClaw on Lightsail: 自律的プライベートAIエージェント実行
  - Bedrock Agents: アプリケーション内自律エージェント構築機能
- **引用URL:** https://thinkmovesolutions.com/blogs/amazon-bedrock-aws-ai-platform-guide/

### INFO-032
- **タイトル:** Apple Siri Revamp - From Voice Assistant to AI Agent
- **ソース:** Bloomberg / MacDailyNews
- **公開日:** 2026-03-27
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01（Agent SDK/API機能拡張）, KIQ-001-04（マルチモーダル）
- **関連企業:** Apple, Google
- **要約:** AppleがSiriを音声アシスタントからシステム全体のAIエージェントに刷新。スタンドアロンSiriアプリ、Ask Siri機能、チャットボット的体験を計画。2026年1月にGoogleとGemini利用の複数年契約を締結。iOS 27で任意のAIとSiri連携を許可へ。
- **キーファクト:**
  - Siri刷新: 音声アシスタントからシステム全体AIエージェントへ
  - スタンドアロンSiriアプリ: チャットボット的体験を計画
  - Google契約: 2026年1月、Gemini利用の複数年契約
  - iOS 27: 任意のAIとSiri連携を許可
- **引用URL:** https://www.bloomberg.com/news/articles/2026-03-27/apple-in-2026-from-ai-rebound-to-foldable-iphone-q-a-with-mark-gurman

### INFO-033
- **タイトル:** Microsoft 365 Copilot Declarative Agents Upgrade to GPT-5.2
- **ソース:** Microsoft Tech Community
- **公開日:** 2026-03-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01（クラウドプロバイダーAI Agent統合）, KIQ-001-01
- **関連企業:** Microsoft
- **要約:** Microsoft 365 Copilot Declarative AgentsがGPT-5.2にアップグレード。推論能力向上、ツール使用の信頼性強化、文書理解強化。2026年初頭にCopilotをOutlook、Word、Excel、PowerPointに直接埋め込み（有償ライセンスなしでも）。
- **キーファクト:**
  - GPT-5.2アップグレード: 推論・ツール使用・文書理解が強化
  - アプリ埋め込み: Outlook/Word/Excel/PowerPointに直接統合（無償ユーザーも）
  - Declarative Agents: カスタマイズ可能なエージェント機能
  - 外部データ統合: ServiceNow、Google Workspace等
- **引用URL:** https://techcommunity.microsoft.com/blog/microsoft365copilotblog/microsoft-365-copilot-declarative-agents-are-getting-smarter-with-gpt-5-2/4504774

### INFO-034
- **タイトル:** Llama 4 Maverick - Meta's Open Source LLM
- **ソース:** Onyx / Till-Freitag
- **公開日:** 2026-03-24
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03（OSS vs商用性能ギャップ）
- **関連企業:** Meta
- **要約:** Meta Llama 4 Maverickが400Bパラメータ、1Mコンテキストウィンドウのオープンソースモデルとして登場。MMLU-Pro 80.5%、GPQA Diamond 69.8%。Llama 4 Scoutは10Mトークンコンテキストで最大級のOSSモデル。マルチモーダル（テキスト+画像）対応。
- **キーファクト:**
  - Llama 4 Maverick: 400B params, 1M context
  - Llama 4 Scout: 10M context window（OSS最大）
  - MMLU-Pro: 80.5%, GPQA Diamond: 69.8%
  - マルチモーダル: テキスト+画像対応
  - Chatbot Arena: 1328（A-Tier）
- **引用URL:** https://onyx.app/open-llm-leaderboard

### INFO-035
- **タイトル:** MolmoWeb - Open Visual Web Agent by Ai2
- **ソース:** Allen Institute for AI (Ai2)
- **公開日:** 2026-03-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）, KIQ-001-01（Agent SDK/API）
- **関連企業:** Allen Institute for AI
- **要約:** Ai2がオープンソース視覚WebエージェントMolmoWebをリリース。スクリーンショットのみでブラウザを操作。4B/8Bパラメータ版。WebVoyager 78.2%、DeepShop 42.3%でオープンウェイトSOTA。MolmoWebMix（36K人間デモ+合成軌跡）も公開。
- **キーファクト:**
  - 視覚ベース: スクリーンショットのみでブラウザ操作（HTML不要）
  - モデルサイズ: 4B/8Bパラメータ
  - WebVoyager: 78.2%（オープンウェイトSOTA）
  - MolmoWebMix: 36K人間デモ、623Kサブタスク、1.1K+サイト
  - Pass@4スケーリング: WebVoyager 94.7%、Online-Mind2Web 60.5%
- **引用URL:** https://allenai.org/blog/molmoweb

### INFO-036
- **タイトル:** NVIDIA NemoClaw - Open Source AI Agent Platform
- **ソース:** NVIDIA / Campus Technology
- **公開日:** 2026-03-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）, KIQ-003-03（OSS vs商用）
- **関連企業:** NVIDIA
- **要約:** NVIDIAがGTC 2026でオープンソースAIエージェントフレームワークNemoClawを発表。企業がセキュアにAIエージェントを本番環境でデプロイ可能。OpenShellベースの自動化オープンソースエージェントセキュリティフレームワーク含む。常に稼働するAIアシスタントの安全な実行を実現。
- **キーファクト:**
  - NemoClaw: 常時稼働AIアシスタントのセキュアデプロイ
  - OpenShellベース: 自動化オープンソースエージェントセキュリティ
  - インフラ非依存: 任意のインフラで実行可能
  - GTC 2026発表
- **引用URL:** https://campustechnology.com/articles/2026/03/25/nvidia-intros-open-source-tools-for-building-and-deploying-ai-agents.aspx

### INFO-037
- **タイトル:** CIFAR Awards $1M+ for AI Safety Research
- **ソース:** CIFAR
- **公開日:** 2026-03-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03（AGI安全性・ガバナンス）
- **関連企業:** N/A（研究機関）
- **要約:** カナダCIFARがAI Safety Catalyst Projectsに100万ドル以上を助成。ISED（カナダ産業省）資金による。社会技術的課題に焦点。Cambridge ERA:AI Research Fellowship 2026も完全資助で開始（6/8-8/28、ロンドン）。
- **キーファクト:**
  - CIFAR助成: $1M+、AI Safety Catalyst Projects
  - 資金源: カナダISED（産業省）
  - 焦点: 社会技術的AI安全性課題
  - Cambridge ERA:AI Fellowship 2026: 完全資助、6/8-8/28
- **引用URL:** https://cifar.ca/cifarnews/2026/03/28/cifar-awards-over-1m-to-support-sociotechnical-challenges-in-ai-safety/

### INFO-038
- **タイトル:** 92% of Enterprises Achieving Positive ROI with Generative AI
- **ソース:** Facebook (KDNuggets) / Industry Report
- **公開日:** 2026-03-27
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-RED-005（AI ROI定量データ）, KIQ-002-02（エンタープライズ採用率）
- **関連企業:** N/A（調査）
- **要約:** 最新グローバル調査「ROI of Gen AI and Agents 2026」によると、92%のエンタープライズが生成AIで正のROI達成。平均ROIは初期投資の2.8倍（IDC）。Gartner予測: 40%のプロジェクトが2027年までにROI不明確でキャンセルのリスク。
- **キーファクト:**
  - 正のROI達成: 92%のエンタープライズ
  - 平均ROI: 初期投資の2.8倍（IDC）
  - キャンセルリスク: 40%のプロジェクトが2027年までに
  - Time-to-Value目標: 13ヶ月未満
- **引用URL:** https://www.facebook.com/kdnuggets/posts/92-of-enterprises-are-achieving-positive-roi-with-generative-aidiscover-the-winn/1378542784302154/

### INFO-039
- **タイトル:** AI Agent Cost Benchmark - 1127 Runs Across Claude, OpenAI, Gemini
- **ソース:** Reddit r/LocalLLaMA
- **公開日:** 2026-03-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01（API料金）, KIQ-003-05（スイッチングコスト）
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** 1127エージェント実行にわたるコストベンチマーク公開。P95と中央値の18倍ギャップがインテリジェントルーティングの価値を示す。コンテンツ生成は$0.62、リサーチは高コスト。Claude、OpenAI、Gemini間のコスト差を分析。
- **キーファクト:**
  - P95 vs中央値: 18倍ギャップ（インテリジェントルーティングの根拠）
  - コンテンツ生成: $0.62/実行
  - 1127実行でClaude、OpenAI、Geminiを比較
  - コスト最適化: キャッシングで最大90%削減可能
- **引用URL:** https://www.reddit.com/r/LocalLLaMA/comments/1s5982e/agent_cost_benchmark_1127_runs_across_claude/

### INFO-040
- **タイトル:** DeerFlow 2.0 GitHub Trending - ByteDance Open Source Agent
- **ソース:** DEV.to / LinkedIn
- **公開日:** 2026-03-20
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）, KIQ-003-03（OSS vs商用）
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0をオープンソース化。2026年2月27日公開、24時間でGitHub Trending 1位。LangGraph 1.0ベースのSuperAgentランタイム。ローカル・Kubernetes・Slack/Telegram統合対応。MITライセンスで商用利用可能。
- **キーファクト:**
  - 公開日: 2026年2月27日、24時間でGitHub Trending 1位
  - アーキテクチャ: LangGraph 1.0 + LangChain
  - デプロイ: ローカル、Kubernetes、Slack/Telegram統合
  - ライセンス: MIT（商用利用無料）
  - モデル対応: OpenAI互換API、Doubao-Seed、DeepSeek、Claude等
- **引用URL:** https://dev.to/arshtechpro/deerflow-20-what-it-is-how-it-works-and-why-developers-should-pay-attention-3ip3

### INFO-041
- **タイトル:** ChatGPT Usage Statistics March 2026 - 888M Users
- **ソース:** First Page Sage
- **公開日:** 2026-03-23
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02（エンタープライズ採用率）, KIQ-003-04（投資動向）
- **関連企業:** OpenAI
- **要約:** ChatGPTが月間8.88億ユーザー（Copilot含む）に到達。AI検索シェア73.3%。1年間で5.01億→8.88億ユーザーに増加（77%成長）。ユーザー retention: Plus 59%/年、Team 68%/年、Enterprise 88%/年。最大用途は一般リサーチ37%、学術18%、コーディング14%。
- **キーファクト:**
  - 月間ユーザー: 8.88億（ChatGPT単体8.31億+Copilot1.05億）
  - AI検索シェア: 73.3%
  - 年間成長: 5.01億→8.88億（77%増）
  - Retention: Enterprise 88%/年、Team 68%/年、Plus 59%/年
  - 地域: 米国17.1%、インド16.5%、ブラジル5.8%
- **引用URL:** https://firstpagesage.com/seo-blog/chatgpt-usage-statistics/

### INFO-042
- **タイトル:** Users Quit ChatGPT For Claude In 1,487% Surge
- **ソース:** Forbes
- **公開日:** 2026-03-23
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-RED-009（Claude Code関連）, KIQ-002-02（採用率）
- **関連企業:** Anthropic, OpenAI
- **要約:** 2026年3月にClaudeへのセッション数が1,487%急増。ユーザーがChatGPTからClaudeへの移行を加速。コーディング、長文執筆、分析タスクでのClaude優位性が理由。Menlo Ventures調査でClaude CodeがAIコーディング市場シェア50%超。
- **キーファクト:**
  - Claude移行: 3月セッション1,487%増
  - Claude Code: AIコーディング市場シェア50%超（Menlo Ventures）
  - 移行理由: コーディング、長文執筆、分析での優位性
- **引用URL:** https://www.forbes.com/sites/rachelwells/2026/03/23/users-quit-chatgpt-for-claude-in-1487-surge-heres-how-work-changes/

### INFO-043
- **タイトル:** AI Startup Funding - Harvey $11B, Shield AI $12.7B
- **ソース:** CNBC / Reuters / TechCrunch
- **公開日:** 2026-03-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04（資金調達・投資動向）
- **関連企業:** Harvey, Shield AI, Physical Intelligence
- **要約:** AIスタートアップ資金調達が活発化。Legal AIのHarveyが$200M調達で評価額$11B。防衛TechのShield AIが$2B調達で$12.7B評価（前年から140%上昇）。ロボティクスのPhysical Intelligenceが$1B調達で$11B評価。VCがモデル企業以外にも投資分散。
- **キーファクト:**
  - Harvey: $200M調達、評価額$11B（Legal AI）
  - Shield AI: $2B調達、評価額$12.7B（防衛、前年+140%）
  - Physical Intelligence: $1B調達、評価額$11B（ロボティクス）
  - トレンド: VCがモデル企業以外の垂直AI・エージェント企業に分散投資
- **引用URL:** https://www.cnbc.com/2026/03/25/legal-ai-startup-harvey-raises-200-million-at-11-billion-valuation.html

### INFO-044
- **タイトル:** Claude Code vs GitHub Copilot vs Cursor Comparison 2026
- **ソース:** Cosmic AI / LeadDev
- **公開日:** 2026-03-26
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01（Agent SDK/API）, KIQ-004-02（コーディング能力市場価値）
- **関連企業:** Anthropic, Microsoft, Cursor
- **要約:** 2026年の主要AIコーディングツール比較。Claude Code、GitHub Copilot、Cursorの3強状態。Copilot Workspaceが「Software Development Hub」として進化。Cursorは年間約10億行のコードを生成。Claude Codeは深い理解と自律性で優位。
- **キーファクト:**
  - 3強: Claude Code、GitHub Copilot、Cursor
  - Copilot Workspace: Software Development Hubとして進化
  - Cursor: 年間約10億行コード生成
  - Claude Code: 深い理解・自律性で優位
- **引用URL:** https://www.cosmicjs.com/blog/claude-code-vs-github-copilot-vs-cursor-which-ai-coding-agent-should-you-use-2026

### INFO-045
- **タイトル:** Amazon Alexa+ Launch in UK - Agentic AI Future
- **ソース:** TechRadar / Forbes
- **公開日:** 2026-03-22
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04（マルチモーダルAgent）, KIQ-001-01
- **関連企業:** Amazon
- **要約:** AmazonがAlexa+を英国でローンチ。OpenClaw統合でAIに「デジタルの手」を与え、PC・Web・他エージェントと対話可能。AmazonはAI中心スマートフォン「Transformer」（内部コード）を開発中と報道。Alexa AI評価は賛否両論。
- **キーファクト:**
  - Alexa+: 英国ローンチ、ローカライズ対応
  - OpenClaw統合: AIにデジタルの手を提供
  - スマートフォン開発: 内部コード「Transformer」
  - 評価: 改善期待と失望の両方
- **引用URL:** https://www.techradar.com/pro/enough-chit-chat-alexa-is-done-waiting-for-the-agentic-ai-future-i-spoke-to-amazons-daniel-rausch-to-find-out-more

### INFO-046
- **タイトル:** ChatGPT Competitor Market Share - Gemini 15.2%, Claude 4.5%
- **ソース:** First Page Sage
- **公開日:** 2026-03-23
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02（採用率）, KIQ-003-05（スイッチングコスト）
- **関連企業:** Google, Anthropic, Perplexity
- **要約:** AI検索市場の競合シェア推移。ChatGPT 73.3%、Google Gemini 15.2%（上昇中）、Perplexity 5.8%、Claude 4.5%。Geminiは直近のアップデートが好評で利用増。Claudeは急速にシェア拡大中。
- **キーファクト:**
  - ChatGPT: 73.3%（73.9%→73.3%と微減）
  - Google Gemini: 15.2%（13.7%→15.2%と上昇）
  - Perplexity: 5.8%（安定）
  - Claude: 4.5%（3.3%→4.5%と急成長）
- **引用URL:** https://firstpagesage.com/seo-blog/chatgpt-usage-statistics/

### INFO-047
- **タイトル:** AI SEO Visibility - 20% of Search Traffic via ChatGPT
- **ソース:** Reddit / Digital Marketing
- **公開日:** 2026-03-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05（プラットフォーマーAI統合）
- **関連企業:** OpenAI, Google, Perplexity, Anthropic
- **要約:** ChatGPTが世界の検索トラフィックの約20%を処理。AI SEO visibilityが2026年の最重要メトリクスに。Perplexity成長中、GeminiはGoogle全製品に組み込まれ、Claudeも検索応答で存在感増加。従来SEOからAI検索最適化への移行が必須。
- **キーファクト:**
  - ChatGPT: 世界の検索トラフィック約20%
  - AI SEO visibility: 2026年の最重要メトリクス
  - プラットフォーム: Perplexity成長、Gemini埋め込み、Claude回答増
  - トレンド: 従来SEO→AI検索最適化への移行
- **引用URL:** https://www.reddit.com/r/DigitalMarketing/comments/1s5wr2w/ai_seo_visibility_is_the_most_important_metric_in/

### INFO-048
- **タイトル:** ChatGPT Use Cases by Industry - Travel 47% Usage
- **ソース:** First Page Sage
- **公開日:** 2026-03-23
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02（エンタープライズ採用率）, KIQ-002-04（業務自律化）
- **関連企業:** N/A（調査）
- **要約:** ChatGPT購入ジャーニー活用の業界別データ。旅行47%が最高、金融影響$1.48兆。小売36%、ITサービス34%、ライフスタイル/健康32%。10ヶ月連続で全業界で利用増加。
- **キーファクト:**
  - 旅行・ホスピタリティ: 47%利用、影響$1.48兆
  - 小売・CPG: 36%利用、影響$1.11兆
  - ITサービス: 34%利用、影響$9,360億
  - トレンド: 全業界で10ヶ月連続利用増加
- **引用URL:** https://firstpagesage.com/seo-blog/chatgpt-usage-statistics/

### INFO-049
- **タイトル:** How AI Is Changing Entry Level Work - WEF Report
- **ソース:** World Economic Forum
- **公開日:** 2026-03-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-01（業務自律化）, KIQ-004-03（AI代替困難能力）
- **関連企業:** Cognizant
- **要約:** WEFとCognizantがAI時代のエントリーレベル雇用を分析。米国でエントリーレベル求人が18ヶ月で35%減少（Revelio Labs）。しかしCognizantは2025年に25,000人の新卒を採用、2026年はさらに増加予定。AIスキルを持つ新卒は即座に価値を提供可能。仕事の性質が「タスク実行」から「判断」へ変化。
- **キーファクト:**
  - エントリーレベル求人: 米国で18ヶ月間35%減少
  - Cognizant採用: 2025年25,000人新卒、2026年はさらに増加
  - 仕事の変化: タスク実行→判断・AI出力監視
  - デジタルネイティブ: AI適応が速く競争優位
  - 39%の労働者コアスキルが2030年までに変化（WEF研究）
- **引用URL:** https://www.weforum.org/stories/2026/03/how-ai-is-changing-the-nature-of-entry-level-work/

### INFO-050
- **タイトル:** Agentic AI Security Breaches - Meta Sev-1, 135K Exposed Instances
- **ソース:** Hardened News / HiddenLayer / IBM X-Force
- **公開日:** 2026-03-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02（エンタープライズセキュリティ）, KIQ-002-03（規制環境）
- **関連企業:** Meta, OpenAI
- **要約:** エージェントAIの本番環境でのセキュリティ侵害が急増。MetaでSev-1インシデント（AIエージェントが権限外アクセスを誘発）、Moltbookで150万APIトークン暴露、OpenClawで135,000インスタンスが公開（63%が脆弱）。HiddenLayer調査: AI侵害の8件に1件以上がエージェントシステム。IBM X-Force: 公開アプリ悪用44%増、ランサムウェアグループ49%増。
- **キーファクト:**
  - Meta Sev-1: AIエージェントが権限外アクセス誘発、2時間で検知
  - Moltbook: 150万APIトークン、35,000メール暴露
  - OpenClaw: 135,000公開インスタンス、63%脆弱（CVE-2026-25253 CVSS 8.8）
  - HiddenLayer: AI侵害の12.5%+がエージェント関連（250社調査）
  - IBM X-Force: アプリ悪用44%増、ランサムウェア49%増
  - Snyk ToxicSkills: 3,984スキル中36%にセキュリティ欠陥
- **引用URL:** https://www.hardened.news/p/agentic-ai-is-in-production-so-are-the-breaches

### INFO-051
- **タイトル:** Mandiant M-Trends 2026 - 22 Second Access Handoff
- **ソース:** Google Cloud / Mandiant
- **公開日:** 2026-03-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03（セキュリティ・規制）, KIQ-002-06（政府圧力）
- **関連企業:** Google
- **要約:** Mandiant M-Trends 2026レポート（50万時間以上のIR調査）。初期アクセスから二次脅威グループへの引き渡しが22秒に短縮（2022年の8時間から）。脆弱性悪用が#1（32%）、vishingが#2（11%）。平均滞在時間14日（前年11日から増加）。新たな「リカバリー拒否」ランサムウェア戦術が登場。
- **キーファクト:**
  - アクセス引き渡し: 22秒（2022年8時間→2026年22秒）
  - 初期アクセス: 脆弱性悪用32%、vishing 11%
  - 平均滞在時間: 14日（前年11日）
  - 外部通知インシデント: 25日中央値
  - リカバリー拒否: バックアップ・ID・仮想化基盤を標的
- **引用URL:** https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026/

### INFO-052
- **タイトル:** Human Talent Key to AI Value - WEF EMEA Report
- **ソース:** World Economic Forum
- **公開日:** 2026-03-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-03（AI代替困難能力）, KIQ-004-04（AI時代勝利企業条件）
- **関連企業:** Microsoft
- **要約:** WEF研究: 労働者の39%のコアスキルが2030年までに変化。EMEA地域ではAI価値 unlock に人材が鍵。「2026年は企業がAIの価値を証明する年」（WEF）。新職種: AI監査人、プロンプトエンジニア、データストラテジストが重要に。AIは人間の創造性を高める補助的役割。
- **キーファクト:**
  - コアスキル変化: 39%の労働者が2030年までに影響
  - 2026年: 企業がAI価値を証明する年
  - 新職種: AI監査人、プロンプトエンジニア、データストラテジスト
  - 人材が鍵: AI導入成功に人間の才能が不可欠
  - AI貢献予測: 2026年までに$15.7兆（IMF、Goldman Sachs）
- **引用URL:** https://www.weforum.org/stories/2026/03/the-ai-opportunity-looks-different-across-europe-the-middle-east-and-africa-but-there-is-one-common-thread-human-talent/

---

## 収集完了サマリー

- **総収集件数:** 52件
- **収集日時:** 2026-03-29
- **品質フラグ:** COLLECTING → ANALYSIS_PENDING
- **主要カバレッジ:**
  - KIQ-001（Agent SDK/API）: 15件
  - KIQ-002（市場/規制）: 12件
  - KIQ-003（価格/ベンチマーク）: 8件
  - KIQ-004（労働市場）: 8件
  - KIQ-005（AGI）: 3件
  - KIQ-RED（Arbiter優先）: 6件
- **信頼性コード分布:**
  - A（公式）: 18件
  - B（主要メディア）: 12件
  - C（Tech Media/専門）: 22件


> ⚠️ DEGRADED: Blue Agent analysis failed. Raw data passed through.
