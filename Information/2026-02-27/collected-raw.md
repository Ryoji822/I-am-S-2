# 収集データ: 2026-02-27

## メタデータ
- 収集日時: 2026-02-27 00:00 UTC
- 品質フラグ: COLLECTING

## 動的追加クエリ（Arbiterフィードバック基づく）
- KIQ-RED-001: MCPサーバーアクティブ率
- KIQ-RED-002: Skills vs Claude Code採用比較
- KIQ-RED-005: ROI正5%の定義詳細・PoC失敗理由
- KIQ-005-02: Erdos #846・FirstProof解決の査読状況（優先強化）
- KIQ-RED-003: Gemini Deep Think正確なARC-AGI-2スコア

## 収集結果

### INFO-001
- **タイトル:** Anthropic Responsible Scaling Policy Version 3.0
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-02-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03 (AGI安全性とガバナンス)
- **関連企業:** Anthropic
- **要約:** AnthropicがRSP第3版をリリース。企業としての単独コミットメントと業界全体への推奨事項を分離し、Frontier Safety RoadmapとRisk Reportsを新設。ASL-3は2025年5月に発動済みだが、バイオリスク評価の「曖昧性ゾーン」問題や政府対応の遅れを認識。
- **キーファクト:**
  - RSP v3.0は2年強の運用経験から学んだ改善を反映
  - 単独行動（企業内）と多国間行動（業界/政府）を明確に分離
  - Risk Reportsを3-6ヶ月ごとに公開、特定条件で第三者レビュー必須化
  - ASL-3は2025年5月に発動済み、バイオ兵器分類子を開発
- **引用URL:** https://www.anthropic.com/news/responsible-scaling-policy-v3

### INFO-002
- **タイトル:** Claude for Financial Services
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-07-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02 (エンタープライズ向け展開)
- **関連企業:** Anthropic
- **要約:** Claude 4モデルが金融業界向け包括的ソリューションを提供。Bridgewater、NBIM、Commonwealth Bank、AIGなどが導入事例。AWS Marketplaceで利用可能。
- **キーファクト:**
  - Claude 4はVals AI Finance Agent benchmarkで他フロンティアモデルを上回る
  - NBIM（ノルウェー投資銀行）で約20%の生産性向上（213,000時間相当）
  - AIGでアンダーライティング時間を5倍短縮、データ精度75%→90%向上
  - Databricks、Snowflake、FactSet、S&P Global等とのMCPコネクタ提供
- **引用URL:** https://www.anthropic.com/news/claude-for-financial-services

### INFO-003
- **タイトル:** Claude for Life Sciences
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2025-10-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03 (開発者エコシステム), KIQ-005-01 (AGI到達度)
- **関連企業:** Anthropic
- **要約:** Claudeがライフサイエンス研究向けに特化した機能を追加。Benchling、PubMed、10x Genomics等の科学ツールとのMCPコネクタ、Agent Skills（single-cell-rna-qc）を提供。
- **キーファクト:**
  - Sonnet 4.5はProtocol QA benchmarkで0.83（人間ベースライン0.79）
  - Sanofi、Broad Institute、Novo Nordisk等が導入
  - 科学的発見を自律的に行うAIモデルへの長期目標を表明
- **引用URL:** https://www.anthropic.com/news/claude-for-life-sciences

### INFO-004
- **タイトル:** Building frontend UIs with Codex and Figma
- **ソース:** OpenAI Developers Blog
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01 (Agent SDK/API機能拡張), KIQ-001-03 (開発者エコシステム)
- **関連企業:** OpenAI
- **要約:** OpenAI CodexがFigma MCPサーバーと統合。Figmaデザインからコード生成、実行中UIからFigmaデザイン生成の双方向ワークフローを実現。
- **キーファクト:**
  - Figma MCPサーバーでデザインファイルからコード生成が可能
  - 実行中アプリのUIをキャプチャしてFigmaフレームとして出力可能
  - Codexデスクトップアプリは複数エージェントの並列管理をサポート
- **引用URL:** https://developers.openai.com/blog/building-frontend-uis-with-codex-and-figma

### INFO-005
- **タイトル:** Flow updates: New ways to create and refine content
- **ソース:** Google Blog
- **公開日:** 2026-02-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04 (マルチモーダルAgent)
- **関連企業:** Google
- **要約:** Google Flowがリデザイン。Whisk/ImageFX機能を統合し、画像・動画生成を単一ワークスペースで提供。Nano Banana画像生成を組み込み。
- **キーファクト:**
  - Flowで15億以上の画像・動画を生成済み
  - 画像・動画の統合アセット管理機能を追加
  - ラッソツールでの精密選択と自然言語編集をサポート
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/

### INFO-006
- **タイトル:** Nano Banana 2: Combining Pro capabilities with lightning-fast speed
- **ソース:** Google Blog
- **公開日:** 2026-02-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02 (ベンチマーク性能), KIQ-001-04 (マルチモーダル)
- **関連企業:** Google
- **要約:** Google DeepMindがNano Banana 2（Gemini 3.1 Flash Image）をリリース。Nano Banana Proの高機能とFlash速度を統合。最大5キャラクター・14オブジェクトの一貫性維持をサポート。
- **キーファクト:**
  - Gemini、Search、Ads、Flow、AI Studio/API、Vertex AIで利用可能
  - SynthID検証機能が2,000万回以上使用済み
  - C2PA Content Credentialsとの相互運用性を追加
- **引用URL:** https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/

### INFO-007
- **タイトル:** Claude Agent SDK v0.2.58 Released
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-02-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01 (Agent SDK/API機能拡張)
- **関連企業:** Anthropic
- **要約:** Claude Agent SDKがv0.2.58に更新。Claude Code v2.1.58とのパリティ達成。v0.2.51ではremote-control機能、メモリ使用量改善、task_progressイベントを追加。
- **キーファクト:**
  - v0.2.58でClaude Code v2.1.58とパリティ
  - v0.2.53でlistSessions()追加（過去セッション一覧取得）
  - v0.2.51でremote-controlサブコマンド、メモリリーク修正
  - v0.2.49でsupportsEffort/supportedEffortLevelsフィールド追加
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases

### INFO-008
- **タイトル:** Anthropic acquires Vercept for Computer Use
- **ソース:** Anthropic (公式発表)
- **公開日:** 2026-02-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04 (マルチモーダルAgent), KIQ-001-01 (Agent SDK/API)
- **関連企業:** Anthropic
- **要約:** AnthropicがVerceptを買収し、Computer use機能を強化。Claude Sonnet 4.6はOSWorld benchmarkで72.5%（2024年末15%から大幅向上）。Bun買収に続く2件目の買収。
- **キーファクト:**
  - Vercept創業者: Kiana Ehsani, Luca Weihs, Ross Girshick
  - Claude Sonnet 4.6 OSWorld: 72.5%（人間レベルに接近）
  - 複雑スプレッドシート・Webフォーム操作で人間レベル性能に接近
  - Computer useは2024年末に15%から72.5%に向上
- **引用URL:** https://www.anthropic.com/news/acquires-vercept

### INFO-009
- **タイトル:** Gemini API Coding Agents Skill
- **ソース:** Google AI for Developers
- **公開日:** 2026-02-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01 (Agent SDK/API), KIQ-001-03 (開発者エコシステム)
- **関連企業:** Google
- **要約:** GoogleがGemini API開発スキルを提供開始。skills.shとContext7 CLIに対応。Gemini 3 Flashで87%、Gemini 3 Proで96%のAPI正確性を達成。
- **キーファクト:**
  - gemini-api-devスキルで最新Gemini APIドキュメントにアクセス
  - Agent Skills open standard (agentskills.io)を採用
  - Claude Code、Cursor、Copilot等のツールで利用可能
  - 3層ディスカバリー: workspace, user, extension
- **引用URL:** https://ai.google.dev/gemini-api/docs/coding-agents

### INFO-010
- **タイトル:** Durable AI Agent with Gemini and Temporal
- **ソース:** Google AI for Developers
- **公開日:** 2026-02-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01 (Agent SDK/API), KIQ-002-02 (エンタープライズ採用)
- **関連企業:** Google
- **要約:** Gemini APIとTemporalを使った耐久性のあるAIエージェント構築チュートリアル。LLM呼び出し・ツール実行の全ステップがTemporalで永続化され、クラッシュから復旧可能。
- **キーファクト:**
  - ReActスタイルのエージェントループを実装
  - ネットワーク障害・ワーカークラッシュから自動復旧
  - Gemini 3 Flash Previewを使用
  - 自動関数呼び出しを無効化し、Temporalで個別管理
- **引用URL:** https://ai.google.dev/gemini-api/docs/temporal-example

### INFO-011
- **タイトル:** xAI Grok 4.20 Multi-Agent System Details
- **ソース:** NextBigFuture (Substack)
- **公開日:** 2026-02-19
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01 (Agent SDK/API), KIQ-005-01 (AGI到達度)
- **関連企業:** xAI
- **要約:** xAI Grok 4.20が4エージェントシステム（Grok/Captain, Harper, Benjamin, Lucas）をネイティブ統合。Grok 4.20 Heavyは16エージェントで$300/月。200トラッカーを同時管理可能。
- **キーファクト:**
  - 4エージェント: Grok(統括), Harper(検索), Benjamin(数学/コード), Lucas(創造)
  - Grok 4.20 Heavy: 16エージェント、$300/月
  - 並列推論でコストは1.5-2.5倍に抑制
  - ハルシネーション大幅削減、Alpha Arenaで唯一収益性達成
- **引用URL:** https://nextbigfuture.substack.com/p/xai-grok-420-grok-420-heavy-and-200

### INFO-012
- **タイトル:** Grok 4.2 Status and Agentic Tooling
- **ソース:** Data Studios
- **公開日:** 2026-02-23
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01 (Agent SDK/API)
- **関連企業:** xAI
- **要約:** Grok 4.2はパブリックベータ/リリース候補として明示的選択で利用可能。Grok 4.1が公式ベースライン。Grok 420 Multi-AgentがAPIに追加予定。ファイル添付は48MB上限。
- **キーファクト:**
  - Grok 4.2はオプトイン選択（デフォルトではない）
  - Grok 4.1はgrok.com, X, mobileで公式利用可能
  - Grok 420 Early Access / Multi-AgentがAPIロードマップ
  - サーバーサイドツール: Web検索、X検索、コード実行、ドキュメント検索
- **引用URL:** https://www.datastudios.org/post/grok-4-2-status-public-beta-signals-agentic-tooling-model-picker-reality-and-what-is-technically

### INFO-013
- **タイトル:** ByteDance Dola-Seed-2.0 Ranks High on Arena.ai
- **ソース:** Trending Topics
- **公開日:** 2026-02-20
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02 (ベンチマーク性能), BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのDola-Seed-2.0がArena.aiプレビュー版でGrok-4.1、Gemini 3、Claude Opus 4.5を上回る順位。Seed 2.0シリーズはPro/Lite/Mini/Codeの4種類。コストは競合の約1/10。
- **キーファクト:**
  - Dola-Seed-2.0はArena.aiでxAI Grok-4.1より上位
  - 数学・コーディング・ソフトウェア分野で強い
  - トークン価格は競合の約1/10
  - SuperGPQAでGPT-5.2上回る、ICPC/IMO金メダル相当
- **引用URL:** https://www.trendingtopics.eu/bytedance-prepares-chinas-next-ai-shock/

### INFO-014
- **タイトル:** ByteDance Seedance 2.0 Copyright Issues
- **ソース:** AIbase
- **公開日:** 2026-02-26
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-03 (規制環境), KIQ-001-04 (マルチモーダル)
- **関連企業:** ByteDance
- **要約:** ByteDanceの動画生成AI Seedance 2.0がDisney等から著作権侵害で指摘。日本政府も是正要求。今後は著作権キャラクター・著名人の生成を制限。
- **キーファクト:**
  - Disneyが弁護士通知送付
  - 日本AI戦略担当大臣が是正要求
  - 統合音声・動画生成アーキテクチャ
  - 今後は著作権キャラクター生成を制限
- **引用URL:** https://www.aibase.com/news/25717

### INFO-015
- **タイトル:** Agent Framework Wars: Container Wars Repeated
- **ソース:** The New Stack
- **公開日:** 2026-02-26
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03 (開発者エコシステム), KIQ-001-01 (Agent SDK/API)
- **関連企業:** 複数
- **要約:** Big TechがAIエージェントフレームワークを無償提供する理由を分析。Docker対コンテナ標準の戦争と同様の構図。プロトコル（MCP等）への投資を推奨。
- **キーファクト:**
  - フレームワークはロックイン戦略
  - MCP等のプロトコルへの投資を推奨
  - コンテナ戦争と同様のパターン
  - Big Techはフレームワークで囲い込み狙う
- **引用URL:** https://thenewstack.io/agent-framework-container-wars/

### INFO-016
- **タイトル:** Claude Code Security Launch
- **ソース:** Fluid Attacks / CSO Online
- **公開日:** 2026-02-24
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02 (エンタープライズ向け展開), KIQ-001-03 (開発者エコシステム)
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Code Securityをリミテッドリサーチプレビューで提供開始。Claude Opus 4.6を使用し、OSSで500件以上の高深刻度脆弱性を発見。自己検証ステップでハルシネーション低減。
- **キーファクト:**
  - Enterprise/Team顧客向けリミテッドリサーチプレビュー
  - Claude Opus 4.6でコードベーススキャン
  - OSSで500件以上の高深刻度脆弱性を発見（数十年見逃し）
  - 自己検証ステップで誤検知低減
- **引用URL:** https://fluidattacks.com/blog/claude-code-security

### INFO-017
- **タイトル:** MCP Governance by Cloudflare
- **ソース:** Cloudflare Developers
- **公開日:** 2026-02-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03 (開発者エコシステム), KIQ-002-01 (クラウドプロバイダー統合)
- **関連企業:** Cloudflare
- **要約:** CloudflareがMCPガバナンスソリューションを提供。「Shadow MCP」問題に対処し、リモートMCPサーバーの可視性と制御を実現。Accessでアイデンティティ・条件・スコープ制御。
- **キーファクト:**
  - Shadow MCP（管理外ローカルサーバー）のリスク対応
  - MCP server portalで集中管理
  - アイデンティティ・条件・ツールスコープ制御
  - リモートMCPサーバーを推奨（ローカルはshadow ITリスク）
- **引用URL:** https://developers.cloudflare.com/agents/model-context-protocol/governance/

### INFO-018
- **タイトル:** Outreach MCP Integration for Revenue Teams
- **ソース:** Outreach Blog
- **公開日:** 2026-02-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03 (開発者エコシステム), KIQ-002-02 (エンタープライズ採用)
- **関連企業:** Outreach
- **要約:** OutreachがMCP対応を発表。MCP Server/Client両方として動作し、Salesforce Agentforce、Microsoft Copilot等と連携。AIエージェント間のコンテキスト共有を実現。
- **キーファクト:**
  - MCP ServerとしてOutreachインサイトを他ツールに提供
  - MCP Clientとして外部知識ベースから情報取得
  - トグルタックス削減、リアルタイムコンテキスト共有
  - フューチャープルーフなオープン標準採用
- **引用URL:** https://www.outreach.io/resources/blog/what-is-model-context-protocol-mcp


## X (Twitter) 投稿データ（ローカルRSSHub経由）

### INFO-019
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-02-27
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Jake Eaton
I am especially proud to work at Anthropic today

Anthropic: A statement from Anthropic CEO, Dario Amodei, on our discussions with the Department of War.

https://www.anthropic.com/news/statement-department-of-war
- **引用URL:** https://x.com/sleepinyourhat/status/2027153428162719853

### INFO-020
- **タイトル:** @oriolvinyalsml (Oriol Vinyals) のX投稿
- **ソース:** X (Twitter) - @oriolvinyalsml (研究リーダー)
- **公開日:** 2026-02-27
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Banana^2

Arena.ai: 🚨BREAKING: Nano Banana 2 debuts at #1 in Image Arena, and it changes the game again 🍌🍌

Officially released as Gemini 3.1 Flash Image Preview, it is powered by real-time information and images from web search.

Highlights:
- #1 Text-to-Image scoring 1279, surpassing
- **引用URL:** https://x.com/OriolVinyalsML/status/2027057776535720347

### INFO-021
- **タイトル:** @jeffdean (Jeff Dean) のX投稿
- **ソース:** X (Twitter) - @jeffdean (AI研究中心人物)
- **公開日:** 2026-02-27
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Our new Nano Banana 2 model is out today!  Even better image generation, and it debuts at #1 on the Image Arena.  You too can make a bunch of awesome images!

Arena.ai: 🚨BREAKING: Nano Banana 2 debuts at #1 in Image Arena, and it changes the game again 🍌🍌

Officially released as Gemini 3.1 Flash Image Preview, it is powered by real-time information and images from web search.

Highlights:
- #1 Text-to-Image scoring 1279, surpassing
- **引用URL:** https://x.com/JeffDean/status/2027073624411369767

### INFO-022
- **タイトル:** @lockheimer (Hiroshi Lockheimer) のX投稿
- **ソース:** X (Twitter) - @lockheimer (Android/Chrome責任者)
- **公開日:** 2026-02-27
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Welcome to Google!! 🤖

Intrinsic: Intrinsic has joined @Google to accelerate the future of physical AI!

As a distinct group working closely with other teams across Google, we’re excited to continue evolving the @IntrinsicAI platform to build the Android of robotics.

Learn more: https://www.intrinsic.ai/blog/posts/intrinsic-joins-google-to-accelerate-physical-ai
- **引用URL:** https://x.com/lockheimer/status/2027064253061222530

### INFO-023
- **タイトル:** @joshwoodward (Josh Woodward) のX投稿
- **ソース:** X (Twitter) - @joshwoodward (Geminiアプリ / AI Studio)
- **公開日:** 2026-02-27
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** True

Karan: Pomelli can be a game changer for local brands or startups that can’t afford professional photoshoots

It can also create social media posts for your products

And if that wasn’t enough you can use Google Veo 3 to turn these images into video ads.
- **引用URL:** https://x.com/joshwoodward/status/2027087186005496121

### INFO-024
- **タイトル:** @demishassabis (Demis Hassabis) のX投稿
- **ソース:** X (Twitter) - @demishassabis (共同創業者・CEO)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** top

Arena.ai: 🚨BREAKING: Nano Banana 2 debuts at #1 in Image Arena, and it changes the game again 🍌🍌

Officially released as Gemini 3.1 Flash Image Preview, it is powered by real-time information and images from web search.

Highlights:
- #1 Text-to-Image scoring 1279, surpassing
- **引用URL:** https://x.com/demishassabis/status/2027107164980965470

### INFO-025
- **タイトル:** @demishassabis (Demis Hassabis) のX投稿
- **ソース:** X (Twitter) - @demishassabis (共同創業者・CEO)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** top 🍌

Arena.ai: 🚨BREAKING: Nano Banana 2 debuts at #1 in Image Arena, and it changes the game again 🍌🍌

Officially released as Gemini 3.1 Flash Image Preview, it is powered by real-time information and images from web search.

Highlights:
- #1 Text-to-Image scoring 1279, surpassing
- **引用URL:** https://x.com/demishassabis/status/2027109383922933863

### INFO-026
- **タイトル:** @joshwoodward (Josh Woodward) のX投稿
- **ソース:** X (Twitter) - @joshwoodward (Geminiアプリ / AI Studio)
- **公開日:** 2026-02-27
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Nano Banana 2 (today) + Flow redesign (yesterday) = 🔥

Flow by Google: Nano Banana 2 has officially arrived! What does this mean for Flow?

0️⃣ Zero credits for all users

📸 Advanced character and scene consistency

🖼️ 2K & 4K image upscaling is now available for everyone

Try it today!
- **引用URL:** https://x.com/joshwoodward/status/2027126982778200210

### INFO-027
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Figma
Codex to Figma

Join designer advocate, Ana Boyer and OpenAI’s Ed Bayes as they talk through roundtripping between code and canvas https://x.com/i/broadcasts/1qJVmQmMRaAGB
- **引用URL:** https://x.com/OpenAIDevs/status/2027071488218791936

### INFO-028
- **タイトル:** @sama (Sam Altman) のX投稿
- **ソース:** X (Twitter) - @sama (CEO)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** We often get asked how people who are not technical can contribute to AGI. One area is research recruiting. 

Tifa (@tifafafafa) is looking for exceptional recruiters from non-traditional backgrounds, former founders especially.

We believe the best research teams are built through context, taste and a real feel for where the field is headed next; research recruiting is about finding people who will move the frontier forward, not just filling roles.

Should be an interesting thing!
- **引用URL:** https://x.com/sama/status/2027087700214591913

### INFO-029
- **タイトル:** @sama (Sam Altman) のX投稿
- **ソース:** X (Twitter) - @sama (CEO)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** Thank you and will work hard to continue to earn your tokens!

Mitchell Hashimoto: I know this is pretty well established at this point, but Codex 5.3 is a much more effective model than Opus 4.6. I went back and forth on both for a bit, but haven’t touched Opus at all now for a full week. First model to get me off of Opus… ever. Good job Codex team.
- **引用URL:** https://x.com/sama/status/2027087689359753483

### INFO-030
- **タイトル:** @sama (Sam Altman) のX投稿
- **ソース:** X (Twitter) - @sama (CEO)
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** Many times, Greg has shown clear conviction in doing whatever he thought would be important to defend the mission and people of OpenAI, especially when it was hard. Here he talks about many of those moments.

Rick Rubin: NEW EPISODE: “At every single stage of OpenAI, the way that I operate, I've learned, changed, and grown. There's so much of how I work today, and when I look back at last-year me and five-year-ago me, I realize I knew nothing. I go back to the very beginning, having the humility
- **引用URL:** https://x.com/sama/status/2027087128514183553

