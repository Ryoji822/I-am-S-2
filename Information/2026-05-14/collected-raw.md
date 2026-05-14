# 収集データ: 2026-05-14

## メタデータ
- 収集日時: 2026-05-14 09:00 UTC
- 実行クエリ数: 56 / 56
- scrape実行数: 10件
- 収集情報数: 52件
- Evidence ID 採番範囲: EVD-20260514-0001 〜 EVD-20260514-0052
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 品質フラグ: NORMAL

## 収集結果

### INFO-001
- **タイトル:** Building a safe, effective sandbox to enable Codex on Windows
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIがWindows向けCodexサンドボックスを自前実装。Windows標準の隔離ツール（AppContainer, Windows Sandbox, MIC）ではコーディングエージェントのユースケースに合わず、SID・書き込み制限トークン・ファイアウォールルールを組み合わせた独自の「elevated sandbox」を設計。CodexSandboxOffline/Onlineユーザーを作成し、ネットワークアクセスを制御。
- **キーファクト:**
  - Windows用カスタムサンドボックス: 合成SID + write-restricted token + ファイアウォールルール
  - CodexSandboxOffline（ネットワーク遮断）とCodexSandboxOnline（許可）の2ユーザー作成
  - codex-command-runner.exeで制限付きトークン配下で子プロセスを起動
  - 従来のunelevated方式はネットワーク保護がadvisory onlyだったため不採用
- **引用URL:** https://openai.com/index/building-codex-windows-sandbox/
- **Evidence ID:** EVD-20260514-0001

### INFO-002
- **タイトル:** Running Codex safely at OpenAI
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-005-03, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI社内でのCodex安全運用の実践報告。サンドボックス・承認ポリシー・ネットワークプロキシ・エージェントネイティブテレメトリの4層構造でコーディングエージェントを管理。Auto-reviewモードで低リスク操作を自動承認。OpenTelemetryログエクスポートとAIセキュリティトリアージエージェントを組み合わせた監査体制。
- **キーファクト:**
  - Auto-reviewモード: 低リスク操作を自動承認し、高リスク操作のみ人間の確認を要求
  - ネットワークプロキシで許可ドメイン（Microsoft Online, OpenAI等）のみアクセス可能
  - MCP OAuth資格情報をOSキーリングに保存、ChatGPTエンタープライズワークスペースに固定
  - OpenTelemetry + AIセキュリティトリアージエージェントでエージェント行動の意図を分析
- **引用URL:** https://openai.com/index/running-codex-safely/
- **Evidence ID:** EVD-20260514-0002

### INFO-003
- **タイトル:** New Compute Partnership with Anthropic
- **ソース:** xAI Official Blog
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-002-01, KIQ-001-01
- **関連企業:** xAI, Anthropic
- **要約:** SpaceXAI（旧xAI）とAnthropicがコンピューティング提携を締結。Colossus 1（220,000+ NVIDIA GPU、H100/H200/GB200搭載の世界最大級AIスパコン）へのアクセスを提供。AnthropicはClaude Pro/Max向けのキャパシティ改善に活用。軌道AIコンピューティングの共同開発にも関心を表明。
- **キーファクト:**
  - Colossus 1: 220,000+ NVIDIA GPU（H100, H200, GB200）
  - AnthropicがClaude Pro/Max購読者向けキャパシティ改善に利用
  - 軌道コンピューティングのギガワット規模開発に共同で関心
  - SpaceXの打ち上げ頻度と軌道経済性が軌道コンピュート実現の鍵
- **引用URL:** https://x.ai/news/anthropic-compute-partnership
- **Evidence ID:** EVD-20260514-0003

### INFO-004
- **タイトル:** Connectors in web, iOS, and Android
- **ソース:** xAI Official Blog
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05, KIQ-002-01
- **関連企業:** xAI
- **要約:** xAIがGrok Connectorsをローンチ。SharePoint、Outlook、OneDrive、Google Workspace、Notion、GitHub、Linearとの深い統合を実現。Bring Your Own MCPサーバー機能も追加。Web/iOS/Androidの全プラットフォームで利用可能。エンタープライズ向けの強力なツール統合プラットフォーム。
- **キーファクト:**
  - 7コネクタ: SharePoint, Outlook, OneDrive, Google Workspace, Notion, GitHub, Linear
  - SharePoint: Grok 4.3による高度なドキュメント編集対応
  - Bring Your Own MCP: カスタムMCPサーバー接続対応
  - Web/iOS/Android全対応
- **引用URL:** https://x.ai/news/grok-connectors
- **Evidence ID:** EVD-20260514-0004

### INFO-005
- **タイトル:** Grok Speech to Text and Text to Speech APIs
- **ソース:** xAI Official Blog
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-01
- **関連企業:** xAI
- **要約:** xAIがGrok STT/TTS APIをローンチ。STTは$0.10/時間（バッチ）、TTSは$15/100万文字。Grok STTは電話・会議・ビデオ/ポッドキャスト・電話の全ドメインで競合（ElevenLabs, Deepgram, AssemblyAI）を上回るWERを記録。25+言語対応、話者分離・マルチチャンネル対応。
- **キーファクト:**
  - STT価格: $0.10/時間（バッチ）、$0.20/時間（ストリーミング）
  - TTS価格: $15/100万文字
  - Grok STT Overall WER 6.9% vs ElevenLabs 9.0% vs Deepgram 11.0% vs AssemblyAI 12.9%
  - スピーチタグ（[laugh], [sigh], [whisper], <emphasis>等）で感情制御可能
  - 25+言語対応、話者分離・マルチチャンネル対応
- **引用URL:** https://x.ai/news/grok-stt-and-tts-apis
- **Evidence ID:** EVD-20260514-0005

### INFO-006
- **タイトル:** Grok Imagine Quality Mode API
- **ソース:** xAI Official Blog
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIがGrok Imagine Quality Mode APIをローンチ。リアリズム・テキストレンダリング・クリエイティブコントロールが大幅向上。Text-to-Image Arenaでトップ5にランクイン。エンタープライズ向けに商品ビジュアライゼーション、UGCコンテンツ生成、ブランド一貫性維持に最適化。
- **キーファクト:**
  - Text-to-Image Arena ラボ別トップ5ランキング
  - 高度な商品ビジュアライゼーション: 参照画像からブランドスタイルを維持した広告生成
  - UGCスタイルコンテンツ生成: 顔・服装の一貫性を維持した複数シーン生成
  - 動画生成とも連携可能
- **引用URL:** https://x.ai/news/grok-imagine-quality-mode
- **Evidence ID:** EVD-20260514-0006

### INFO-007
- **タイトル:** Custom Voices and Voice Library
- **ソース:** xAI Official Blog
- **公開日:** 2026-04-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIがCustom VoicesとVoice Libraryをローンチ。短い録音から音声クローンを作成し、TTS/Voice Agent APIで即座に利用可能。パスフレーズチェック＋話者類似性検証の2段階認証で安全性を確保。80+内蔵音声・28言語対応のVoice Libraryも新設。
- **キーファクト:**
  - 2分以内で音声クローン作成可能
  - 2段階認証: パスフレーズチェック + 話者類似性検証
  - 80+内蔵音声、28言語対応
  - カスタム音声の追加料金なし
- **引用URL:** https://x.ai/news/grok-custom-voices
- **Evidence ID:** EVD-20260514-0007

### INFO-008
- **タイトル:** Accelerating Gemma 4: faster inference with multi-token prediction drafters
- **ソース:** Google Official Blog
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-03, KIQ-001-01, KIQ-003-02
- **関連企業:** Google
- **要約:** GoogleがGemma 4ファミリー向けMulti-Token Prediction (MTP) ドラフターをリリース。投機的デコーディングで最大3倍の推論高速化を実現。出力品質・推論ロジックの劣化なし。Apache 2.0ライセンスで公開。Gemma 4は初週で6000万ダウンロードを記録。
- **キーファクト:**
  - MTPドラフターで最大3倍の推論高速化
  - 投機的デコーディング: 軽量ドラフターが複数トークンを予測、ターゲットモデルが並列検証
  - KVキャッシュ共有でコンテキスト再計算を排除
  - E2B/E4Bエッジモデルではエンベッダーのクラスタリングで更に高速化
  - Gemma 4: 初週6000万ダウンロード
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
- **Evidence ID:** EVD-20260514-0008

### INFO-009
- **タイトル:** The latest AI news we announced in April 2026
- **ソース:** Google Official Blog
- **公開日:** 2026-05-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01, KIQ-003-04
- **関連企業:** Google
- **要約:** Googleの2026年4月AIアップデート総括。Cloud Next '26で260+の発表、Gemini Enterprise Agent Platform、第8世代TPU、Gemma 4オープンモデル、Deep Research Max、Google Vids無料動画生成等。75%のCloud顧客がGoogle Cloud AIを使用、330組織が年間1兆トークン以上を処理。
- **キーファクト:**
  - Cloud Next '26: 32,000+参加者、260+発表
  - Gemini Enterprise Agent Platform: 組織向け自律エージェント構築・管理プラットフォーム
  - 第8世代TPU: エージェントAIの巨大コンピュート需要に最適化
  - 75%のCloud顧客がGoogle Cloud AI使用、330組織が年間1兆トークン+処理
  - Gemma 4: バイト単位で最も性能の高いオープンモデル、累計5億ダウンロード超
- **引用URL:** https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-april-2026/
- **Evidence ID:** EVD-20260514-0009

### INFO-010
- **タイトル:** Anthropic reinstates OpenClaw and third-party agent usage on Claude subscriptions with Agent SDK credit
- **ソース:** VentureBeat
- **公開日:** 2026-05-13
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01, KIQ-003-05
- **関連企業:** Anthropic
- **要約:** Anthropicが6月15日から有料Claudeプラン（Pro/Max/Team/Enterprise）にAgent SDK向け月額クレジットを含めることを発表。OpenClaw等のサードパーティエージェント利用が再開。Agent SDK credit方式で、非効率なエージェントの過剰利用コストをユーザー負担に移行。
- **キーファクト:**
  - 6月15日から有料ClaudeプランにAgent SDK向けクレジット付与
  - OpenClaw等サードパーティエージェント利用が再開
  - Agent SDK credit: 専用ドル建てクレジットでAPI利用量を管理
  - Claude Developer Platform（API key）は対象外、従量課金維持
- **引用URL:** https://venturebeat.com/technology/anthropic-reinstates-openclaw-and-third-party-agent-usage-on-claude-subscriptions-with-a-catch
- **Evidence ID:** EVD-20260514-0010

### INFO-011
- **タイトル:** TikTok launches MCP server to let AI agents run campaigns
- **ソース:** Digiday
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-05, KIQ-001-05
- **関連企業:** ByteDance
- **要約:** TikTok（ByteDance）が広告プラットフォーム向けMCPサーバーとデベロッパーツールキットをローンチ。AIエージェントによるキャンペーン作成・管理・最適化の自動化を可能にする。MCPプロトコルの採用が広告業界にも拡大。
- **キーファクト:**
  - TikTok MCP Server: AIエージェント経由でキャンペーン作成・管理を自動化
  - MCPプロトコルの広告プラットフォームへの拡大採用
  - デベロッパーツールキットも提供
- **引用URL:** https://digiday.com/marketing/tiktok-launches-mcp-server-to-let-ai-agents-run-campaigns/
- **Evidence ID:** EVD-20260514-0011

### INFO-012
- **タイトル:** ByteDance DeerFlow: Open-source super agent harness for deep research
- **ソース:** GitHub
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceがオープンソースのスーパーエージェントフレームワーク「DeerFlow (Deep Exploration and Efficient Research Flow)」を公開。サブエージェントのオーケストレーション、メモリ管理、サンドボックス実行を統合。深い研究タスク向けに設計。
- **キーファクト:**
  - サブエージェントのオーケストレーション機能
  - メモリ管理とサンドボックス実行環境を統合
  - 深い研究タスク（Deep Research）向けに最適化
- **引用URL:** https://github.com/bytedance/deer-flow
- **Evidence ID:** EVD-20260514-0012

### INFO-013
- **タイトル:** EY case study: Building an enterprise-scale agentic AI operating system
- **ソース:** EY
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-04, KIQ-002-02
- **関連企業:** N/A
- **要約:** EYが社内のGenAI成果を統合したグローバルエージェントAIプラットフォームの構築事例。業務プロセス変革とクライアントのAI大規模展開を加速。エンタープライズ規模でのエージェントAI導入の実際の実装パターンを示す。
- **キーファクト:**
  - EYが社内GenAI成果を統合したグローバルエージェントAI OSを構築
  - クライアント向けAI大規模展開の加速
  - エンタープライズ規模のエージェントAI実装パターン
- **引用URL:** https://www.ey.com/en_se/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system
- **Evidence ID:** EVD-20260514-0013

### INFO-014
- **タイトル:** MCP (Model Context Protocol) becomes default integration layer for enterprise AI agents
- **ソース:** KuppingerCole
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** MCPがAIエージェントとエンタープライズシステムを接続するデフォルト統合レイヤーに急速に成長。しかしAPIセキュリティ問題が浮上。MCPサーバーの認証・認可・監査のガバナンス不足が指摘され、企業は対応に追われている。
- **キーファクト:**
  - MCPがAIエージェント統合のデファクトスタンダードに成長
  - APIセキュリティ問題: 認証・認可・監査のガバナンス不足
  - 企業はMCP利用時のセキュリティリスク管理に課題
- **引用URL:** https://www.kuppingercole.com/research/lb80918/model-context-protocol
- **Evidence ID:** EVD-20260514-0014

### INFO-015
- **タイトル:** Agent Skills Marketplace and standard emerging — 1000+ skills catalog
- **ソース:** GitHub / Reddit
- **公開日:** 2026-05-12
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Anthropic
- **要約:** AIエージェント向けスキルのマーケットプレイスとオープン標準が急速に発展。VoltAgent/awesome-agent-skillsは1000+のスキルカタログを持ち、Claude Code、Codex、Gemini CLI、Cursor等に対応。独立系Agent Skills marketplaceも17Kユーザーに到達。
- **キーファクト:**
  - VoltAgent/awesome-agent-skills: 1000+スキルのキュレーション
  - Claude Code、Codex、Gemini CLI、Cursor等の主要ツールに対応
  - オープン標準フォーマットでツール非依存のスキル定義
  - 独立系Agent Skills marketplaceが17Kユーザー到達（$0広告費）
- **引用URL:** https://github.com/VoltAgent/awesome-agent-skills
- **Evidence ID:** EVD-20260514-0015

### INFO-016
- **タイトル:** Microsoft Copilot Studio computer use: Automate web and desktop apps
- **ソース:** Microsoft Learn
- **公開日:** 2026-05-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-002-01
- **関連企業:** Microsoft
- **要約:** MicrosoftがCopilot Studioでcomputer use機能を一般提供。エージェントがGUIを通じてウェブ・デスクトップアプリと対話可能に。エンタープライズ向けのコンピュータ使用自動化が普及段階に。
- **キーファクト:**
  - Copilot Studioのcomputer useでエージェントがGUI操作可能
  - ウェブ・デスクトップアプリ両方に対応
  - エンタープライズ環境でのGUI自動化が本格化
- **引用URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use
- **Evidence ID:** EVD-20260514-0016

### INFO-017
- **タイトル:** AWS Bedrock AgentCore: Payments, Agent Toolkit, and network connectivity
- **ソース:** AWS Blog
- **公開日:** 2026-05-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01, KIQ-001-05
- **関連企業:** Amazon
- **要約:** AWSがBedrock AgentCoreの大幅アップデート。AgentCore Payments（プレビュー）でAIエージェントが自律的にAPI/MCPサーバーの支払いを実行。Agent Toolkit for AWSがMCPサーバーの後継として登場。AgentCore Runtimeのマネージドネットワーク接続オプションも追加。
- **キーファクト:**
  - AgentCore Payments: AIエージェントが自律的にAPI・MCPサーバーに支払い可能
  - Agent Toolkit for AWS: MCP servers/plugins/skillsの後継
  - AgentCore Runtime: マネージドネットワーク接続オプション
  - Bedrock Agentsのマルチエージェントコラボレーション対応
- **引用URL:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-bedrock-agentcore-payments-agent-toolkit-for-aws-and-more-may-11-2026/
- **Evidence ID:** EVD-20260514-0017

### INFO-018
- **タイトル:** Anthropic higher limits with SpaceX Colossus 1 deal — Claude Opus API rate limits大幅引き上げ
- **ソース:** Anthropic Official Blog / MindStudio
- **公開日:** 2026-05-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01, KIQ-001-01, KIQ-003-04
- **関連企業:** Anthropic, xAI
- **要約:** AnthropicがColossus 1提携に伴いClaude Opus APIのレート制限を大幅引き上げ。Tier 1の入力トークンが30K→500K/minに跳ね上がり、Claude Codeの利用制限も倍増。xAI Colossus 1との提携でコンピュートキャパシティを確保し、Pro/Max購読者向けサービス向上に活用。
- **キーファクト:**
  - Claude Opus API Tier 1: 30K→500K input tokens/min（約16倍）
  - Claude Code利用制限が倍増
  - Colossus 1提携でコンピュートキャパシティ確保
  - Opus 4.7 Fast新モデル登場（$15/$75 per 1M tokens）
- **引用URL:** https://www.anthropic.com/news/higher-limits-spacex
- **Evidence ID:** EVD-20260514-0018

### INFO-019
- **タイトル:** Gemini 3.1 Pro vs GPT-5.5: Benchmark comparison
- **ソース:** Blackthorn Vision
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Google, OpenAI
- **要約:** 2026年のフラッグシップAIモデルのベンチマーク比較。Gemini 3.1 ProがGPQA Diamond 94.3%でGPT-5.5の93.6%を上回るが、GPT-5.5がARC-AGI v2でリード。Grok 4も特定領域でトップ。各モデルの得意領域の分化が顕著に。
- **キーファクト:**
  - Gemini 3.1 Pro: GPQA Diamond 94.3%（科学推論トップ）
  - GPT-5.5: ARC-AGI v2でリード（汎用知能指標）
  - Grok 4: 特定領域でトップ
  - モデル間の得意領域の分化が進行中
- **引用URL:** https://blackthorn-vision.com/blog/ai-titan-clash-gemini-vs-chatgpt/
- **Evidence ID:** EVD-20260514-0019

### INFO-020
- **タイトル:** Q1 2026 AI funding blows past 2025 total — $255.5B raised globally
- **ソース:** Yahoo Finance / PitchBook
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** N/A
- **要約:** 2026年Q1のAIスタートアップ資金調達が$2555億に到達し、2025年通年のAIベンチャー資金総額を既に超過。Anthropicが$300億の追加調達を協議中。Isomorphic Labs（DeepMind系）が$21億を調達。
- **キーファクト:**
  - Q1 2026 AI資金調達: $2555億（2025年通年超過）
  - Anthropic: $300億の追加調達を協議中
  - Isomorphic Labs: $21億調達（AI創薬）
  - 主要3件で大部分を占める
- **引用URL:** https://finance.yahoo.com/sectors/technology/articles/q1-2026-ai-funding-blows-175036425.html
- **Evidence ID:** EVD-20260514-0020

### INFO-021
- **タイトル:** OpenAI winding down fine-tuning API — pricing concerns from developers
- **ソース:** OpenAI Community / Reddit
- **公開日:** 2026-05-12
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** OpenAI
- **要約:** OpenAIがファインチューニングAPIとプラットフォームの段階的縮小を発表。開発者コミュニティからは価格上昇への不満が噴出。2026年の新モデルリリースで価格低下ではなく上昇が起きている。GPT-5 Proは$15/$120 per 1M tokens。
- **キーファクト:**
  - ファインチューニングAPIの段階的縮小
  - GPT-5 Pro: $15/$120 per 1M tokens（高価格帯）
  - 開発者から価格上昇への不満
  - モデル非推奨化（GPT-3.5 Turbo等）の継続
- **引用URL:** https://community.openai.com/t/openai-is-winding-down-the-fine-tuning-api-and-platform-discussion-thread/1380522
- **Evidence ID:** EVD-20260514-0021

### INFO-022
- **タイトル:** Anthropic Agent Lock-In: 9 Critical Risks for Enterprise AI
- **ソース:** Progressive Robot
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropicエコシステムへのロックインリスクの分析。エージェントのメモリがエクスポート不可の場合、スイッチングコストになる点を指摘。エージェントメモリをデータベースのように扱い、エクスポート・移行可能性を確保すべきと提言。
- **キーファクト:**
  - エージェントメモリのエクスポート不可がロックイン要因
  - エージェントメモリをデータベースと同様に管理すべき
  - 9つのエンタープライズ向けロックインリスク
  - アーキテクチャレベルでのベンダー非依存設計が重要
- **引用URL:** https://www.progressiverobot.com/2026/05/08/anthropic-agent-lock-in/
- **Evidence ID:** EVD-20260514-0022

### INFO-023
- **タイトル:** AI agents success rate jumps to 77.3% in 2026 — but 74% of companies rolled back AI customer agents
- **ソース:** SQ Magazine / Metaintro (Sinch survey)
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** N/A
- **要約:** Stanford AI IndexによるとAIエージェントの実タスク成功率が2025年の20%から2026年の77.3%に向上（Terminal-Bench）。一方、Sinch調査では74%の企業が2026年にAI顧客対応エージェントをロールバック。23%の組織が少なくとも1事業部でエージェントAIをスケール中。Deloitte調査では53%のAI導入企業が年間$20M以上を投資。
- **キーファクト:**
  - AIエージェント成功率: 20% (2025) → 77.3% (2026)
  - 74%の企業がAI顧客対応エージェントをロールバック（Sinch調査）
  - 23%の組織がエージェントAIをスケール中
  - 53%のAI導入企業が年間$20M以上投資
- **引用URL:** https://sqmagazine.co.uk/predictive-ai-statistics/
- **Evidence ID:** EVD-20260514-0023

### INFO-024
- **タイトル:** Pentagon boosts Scale AI contract to $500M — Meta-backed defense AI expansion
- **ソース:** Yahoo Finance / TNW
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-003-04
- **関連企業:** Meta, Scale AI
- **要約:** ペンタゴンCDAOがScale AI（Meta 49%出資）への契約を$1億から$5億に5倍増額。AI企業への政府・軍事契約が急拡大。Metaの49%出資という構造で、ビッグテックとAI企業の軍事関与が深まっている。
- **キーファクト:**
  - Scale AI: ペンタゴン契約$1億→$5億に5倍増額
  - MetaがScale AIに49%出資
  - CDAO（Chief Digital and AI Office）による大型契約
  - AI企業への政府・軍事契約の急拡大トレンド
- **引用URL:** https://finance.yahoo.com/sectors/technology/articles/pentagon-boosts-meta-backed-scale-113113834.html
- **Evidence ID:** EVD-20260514-0024

### INFO-025
- **タイトル:** AI and automation driving surge in job cuts — 21,490 layoffs in April
- **ソース:** The Hill / Reuters
- **公開日:** 2026-05-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01, KIQ-004-02
- **関連企業:** N/A
- **要約:** 2026年4月にAI・自動化が原因のレイオフが21,490件に達し、全レイオフの4分の1以上を占める。2026年初頭にテック大手93,000人以上の削減。Cloudflareが従業員の20%（1,100人+）を削減。Challenger調査ではAIが全米計画レイオフの7%を占める。
- **キーファクト:**
  - 4月のAI・自動化関連レイオフ: 21,490件（全レイオフの25%+）
  - 2026年初頭テック大手: 93,000人以上削減
  - Cloudflare: 20%（1,100人+）削減
  - Challenger調査: AI関連が全米計画レイオフの7%
- **引用URL:** https://thehill.com/policy/technology/5870898-ai-job-cuts-analysis-trump-admin/
- **Evidence ID:** EVD-20260514-0025

### INFO-026
- **タイトル:** GitHub Copilot 4.7M paid subscribers, 84% developer adoption — AI coding tool stats 2026
- **ソース:** Uvik Software / Towards AI
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02, KIQ-001-01
- **関連企業:** Microsoft, OpenAI
- **要約:** GitHub Copilotが470万有料購読者（前年比75%増）、Fortune 100の90%が採用。AIコーディングアシスタントの全体採用率84%。OpenAI GPTモデルがLLM使用の81%を占める。Copilot、Cursor、Claude Codeの3つで1500万以上の開発者をカバー。
- **キーファクト:**
  - GitHub Copilot: 4.7M有料購読者（YoY +75%）
  - Fortune 100の90%が採用
  - AIコーディングアシスタント全体採用率: 84%
  - OpenAI GPT: LLM使用の81%シェア
  - Copilot + Cursor + Claude Codeで15M+開発者カバレッジ
- **引用URL:** https://uvik.net/blog/ai-coding-assistant-statistics/
- **Evidence ID:** EVD-20260514-0026

### INFO-027
- **タイトル:** Demis Hassabis predicts AGI by 2030 — DeepMind CEO speaks on what AGI truly lacks
- **ソース:** AI Corner / Epsilla
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02, KIQ-005-01
- **関連企業:** Google
- **要約:** DeepMind CEO Demis HassabisがAGI到達を2030年と予測。AGIに真に欠けているのはコンピュートではなく、特定の技術的ボトルネック。責任あるAGI開発の重要性を強調し、不注意な開発は人類を永久に破壊するリスクがあると警告。
- **キーファクト:**
  - Hassabis: AGI到達2030年予測
  - AGIのボトルネックはコンピュート以外に存在
  - 責任あるAGI開発の重要性を強調
  - AGI研究コミュニティの予測中央値: 2030年代
- **引用URL:** https://www.the-ai-corner.com/p/demis-hassabis-agi-2030-deep-tech-founder-playbook-2026
- **Evidence ID:** EVD-20260514-0027

### INFO-028
- **タイトル:** US-China AI talks at Trump-Xi summit — EU AI Act restrictions rolled back
- **ソース:** POLITICO / CFR / Sanders.senate.gov
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** N/A
- **要約:** トランプ・習近平首脳会談でのAI協議が予定されるも、北京はAI安全性について誠実に交渉しないとの見方が大勢。超知能禁止条約に向けた対話の動き。一方、EUはAI Actのハイリスクシステム規制を1年以上延期する合意に達した。
- **キーファクト:**
  - トランプ・習近平首脳会談でAI協議予定
  - 北京はAI安全性について誠実交渉なしとの見方
  - Sanders上院議員: 超知能禁止条約への進展目指す
  - EU AI Act: ハイリスクシステム規制を1年+延期
- **引用URL:** https://www.politico.eu/article/eu-clinches-deal-to-roll-back-ai-restrictions/
- **Evidence ID:** EVD-20260514-0028

### INFO-029
- **タイトル:** DeepSeek V4 Pro: Most powerful open-source model, 8 months behind frontier
- **ソース:** Analytics Vidhya / Gigazine (CAISI)
- **公開日:** 2026-05-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03, KIQ-003-02
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4が「最も強力なオープンソースモデル」と評価されるが、CAISI分析ではフロンティアモデルより約8ヶ月遅れ。ただし同等性能のAIモデルよりコスト効率が高いと評価。オープンソースと商用モデルのギャップは縮小途上。
- **キーファクト:**
  - DeepSeek V4 Pro: フロンティアから約8ヶ月遅れ（CAISI）
  - 同等性能モデルよりコスト効率が高い
  - オープンソースと商用の性能ギャップは縮小中
  - OpenAI GPT-5.5が米国製トップとの比較
- **引用URL:** https://www.analyticsvidhya.com/blog/2026/04/deepseek-v4/
- **Evidence ID:** EVD-20260514-0029

### INFO-030
- **タイトル:** Klarna reverses AI automation — rehires humans after replacing 700 employees
- **ソース:** Duperrin / Instagram / CFO Leadership
- **公開日:** 2026-05-13
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** N/A
- **要約:** KlarnaがAI代替の方向転換。約700人の従業員をAIに置き換え、採用凍結と自動化シフトを行ったが、現在は人間の再採用に転じた。AI失敗の「第1波」から学ぶべき教訓。Duolingoは労働力の10%をAI-first企業に移行。多くの企業がAI生産性向上を報告しつつもポジティブな影響を確認できず。
- **キーファクト:**
  - Klarna: 約700人をAIに代替後に人間再採用へ転換
  - Duolingo: 労働力の10%をAI-first企業に再配置
  - GitHub/MIT研究: AIコーディングアシスタントでタスク55%高速化
  - 多くの企業がAI生産性向上のポジティブインパクトを確認できず
- **引用URL:** https://www.duperrin.com/english/2026/05/13/cloudflare-ai-layoffs/
- **Evidence ID:** EVD-20260514-0030

### INFO-031
- **タイトル:** 67% of entry-level developer jobs gone — Stanford warns of AI-driven collapse
- **ソース:** Reddit / LinkedIn (Stanford) / Second Talent
- **公開日:** 2026-05-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02, KIQ-004-01
- **関連企業:** N/A
- **要約:** スタンフォード研究がAIによるジュニア開発者市場の崩壊を警告。10人のジュニアが必要だった企業がAIツールを使う3人のシニアで済むように。22-25歳のプログラマーの雇用が20%減少。ウェブ・モバイル開発の求人は2020年のピークから60%以上減少。
- **キーファクト:**
  - 10人のジュニア → 3人のシニア+AIツール（Stanford）
  - 22-25歳プログラマー雇用: 20%減少
  - ウェブ・モバイル開発求人: 2020年ピークから60%+減少
  - CS専攻の登録者数が初めて減少傾向
- **引用URL:** https://www.linkedin.com/posts/aslam-ahamed_futureofwork-techhiring-ai-activity-7457991599755644928-07Bh
- **Evidence ID:** EVD-20260514-0031

### INFO-032
- **タイトル:** 豆包（Doubao）が有料サブスクリプション導入 — 68/200/500元の3プラン
- **ソース:** 36Kr
- **公開日:** 2026-05-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDance傘下AI製品「豆包」がApp Storeで有料サブスクリプションを導入。標準版68元/月、強化版200元/月、専門版500元/月の3段階。完全無料の大モデルが減少する中国市場の転換点。
- **キーファクト:**
  - 豆配有料化: 標準版68元/月、強化版200元/月、専門版500元/月
  - 完全無料の大模型が減少する中国市場のトレンド転換
  - App Storeで5月4日に更新
- **引用URL:** https://m.36kr.com/p/3802970281041408
- **Evidence ID:** EVD-20260514-0032

### INFO-033
- **タイトル:** Pentagon designates Anthropic as supply chain risk — federal ban enacted then contested
- **ソース:** CDT / Meritalk / Instagram
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** トランプ政権がAnthropicを「サプライチェーンリスク」に指定し、全連邦政府機関に利用停止を指示。外国敵対企業に使われる designation を米国企業に初適用。Anthropicは提訴。5月1日にペンタゴンは8社とAI契約を締結したがAnthropicは除外。CDTは連邦政府の行動が広範な「chilling effect」を生むと警告。
- **キーファクト:**
  - Anthropicを「サプライチェーンリスク」に指定（米国企業初）
  - 全連邦政府機関に利用停止命令
  - Anthropicは提訴、一部裁判所が判断
  - ペンタゴン8社AI契約でAnthropicのみ除外
  - 公共サービス提供の中断とリソース浪費
- **引用URL:** https://cdt.org/insights/chain-reaction-what-the-pentagon-anthropic-dispute-means-for-civilian-agencies-across-all-levels-of-government/
- **Evidence ID:** EVD-20260514-0033

### INFO-034
- **タイトル:** Pentagon CTO: Anthropic won't be DOD vendor — but deploys Mythos AI cyber model
- **ソース:** Meritalk
- **公開日:** 2026-05-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, Google, Microsoft
- **要約:** ペンタゴンCTOがAnthropicをDODベンダーとして使用しないと明言。しかしAnthropicのClaude Mythos（サイバーモデル）は既にペンタゴン内で展開済み。Googleもペンタゴンと秘密AI契約を締結し、数百人の従業員が抗議。ペンタゴンは「単一AIプロバイダーに依存しない」と宣言。
- **キーファクト:**
  - ペンタゴンCTO: AnthropicをDODベンダーとして不使用
  - Claude Mythos: 既にペンタゴンで展開済み
  - Google: ペンタゴンと秘密AI契約、従業員抗議
  - ペンタゴン: 「単一AIプロバイダー依存は二度としない」
- **引用URL:** https://www.meritalk.com/articles/pentagon-cto-says-anthropic-wont-be-dod-vendor-but-mythos-raises-national-security-stakes/
- **Evidence ID:** EVD-20260514-0034

### INFO-035
- **タイトル:** SAP unveils autonomous enterprise with NVIDIA, Anthropic, AWS, Google, Microsoft partnerships
- **ソース:** SAP Newsroom / NVIDIA Blog
- **公開日:** 2026-05-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** SAP, NVIDIA, Anthropic, Google, Microsoft, Amazon
- **要約:** SAPが自律的エンタープライズを発表。統合SAP Business AI PlatformにNVIDIA OpenShell（オープンソースのエージェントランタイム）を組み込み。Anthropic、AWS、Google Cloud、Microsoftとの提携を深層化。エンタープライズ向けエージェントの信頼性・セキュリティ基盤を構築。
- **キーファクト:**
  - SAP Business AI Platform: 統合AIプラットフォーム
  - NVIDIA OpenShell: エージェント開発・展開用OSSランタイム
  - Anthropic/AWS/Google/Microsoftとの包括的提携
  - エンタープライズ向け自律エージェントの信頼性基盤
- **引用URL:** https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/
- **Evidence ID:** EVD-20260514-0035

### INFO-036
- **タイトル:** Google faces employee backlash over Pentagon AI deal
- **ソース:** MSN
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Google
- **要約:** Googleがペンタゴンと秘密AI契約を締結し、数百人の従業員が軍事・倫理リスクを理由に抗議。Googleの軍事関与に対する内部反発が再燃。Anthropicが「自律兵器・監視拒否」で政府と対立する一方、Googleは政府契約を受け入れる対照的な姿勢。
- **キーファクト:**
  - Googleとペンタゴンの秘密AI契約
  - 数百人の従業員が抗議
  - Googleの軍事関与に対する内部反発再燃
  - Anthropic（拒否）vs Google（受諾）の対照的姿勢
- **引用URL:** https://www.msn.com/en-au/news/insight/google-faces-backlash-over-pentagon-ai-deal/
- **Evidence ID:** EVD-20260514-0036

### INFO-037
- **タイトル:** Enterprise token costs drop 67% YoY — multi-model adoption hits record high
- **ソース:** AICC Report / LLM Stats
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** N/A
- **要約:** AICCレポートによるとエンタープライズのトークンコストが前年比67%低下。GPT-4レベルの性能が2023年の$30/M tokensから現在は$1/M未満に。多モデル採用が記録的高水準に。ただしNVIDIA幹部は、エージェント自動化のトークン課金が急上昇し、一部で人件費を超えつつあると警告。
- **キーファクト:**
  - エンタープライズトークンコスト: 前年比67%低下
  - GPT-4レベル性能: $30/M→$1/M未満（10-100倍低コスト化）
  - 多モデル採用が記録的高水準
  - NVIDIA: エージェント自動化のトークンコストが人件費を超えるリスク
- **引用URL:** https://llm-stats.com/ai-trends
- **Evidence ID:** EVD-20260514-0037

### INFO-038
- **タイトル:** Doubao-Seed-2.0-lite upgrades to full multimodal understanding
- **ソース:** 知乎 (Zhihu)
- **公開日:** 2026-05-06
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** Doubao-Seed-2.0-liteが5月6日に新バージョンにアップグレード。豆包大モデルファミリー初の全モダリティ理解モデルで、ビデオ・画像・音声・テキストのネイティブ統一理解をサポート。Agent、Coding、GUI能力も同期アップグレード。
- **キーファクト:**
  - 豆包大モデル初の全モダリティ理解モデル
  - ビデオ・画像・音声・テキストのネイティブ統一理解
  - Agent、Coding、GUI能力の同期アップグレード
  - Seedシリーズ: World Model方向への発展
- **引用URL:** https://zhuanlan.zhihu.com/p/2036404477750728271
- **Evidence ID:** EVD-20260514-0038

### INFO-039
- **タイトル:** Seedance 2.0 ranks #2 globally in video generation — ByteDance world model ambitions
- **ソース:** Atlas Cloud / 稀土掘金
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceのSeedance 2.0がArtificial Analysis Video Arenaで世界第2位（ELO 1,271）。Seedシリーズ全体が「World Model（世界模型）」方向に発展中。Seedance 2.0は単なる動画生成ではなく、複雑性を制御するマルチモーダルエンジンとしてのパラダイムシフト。
- **キーファクト:**
  - Seedance 2.0: Video Arena世界第2位（ELO 1,271）
  - Seedシリーズ: World Model方向に発展
  - Seed3Dで空間生成・シーン生成能力を追加
  - パラダイムシフト: 単純動画生成→複雑性制御のマルチモーダルエンジン
- **引用URL:** https://www.atlascloud.ai/zh/blog/case-studies/how-to-use-seedance-2
- **Evidence ID:** EVD-20260514-0039

### INFO-040
- **タイトル:** Meta fudged Llama 4 benchmarks — Yann LeCun confirmed different variants used
- **ソース:** Remio.ai
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03, KIQ-003-02
- **関連企業:** Meta
- **要約:** Yann LeCunがMetaがLlama 4のベンチマークで異なるバリアントを使用してスコアを水増ししたことを認めた。この問題は単一モデルの問題を超え、$100億のベンチマーク依存産業全体の問題を露呈。
- **キーファクト:**
  - MetaがLlama 4ベンチマークで異なるバリアントを使用
  - Yann LeCunが事実を確認
  - ベンチマーク水増し問題が$100億産業に影響
  - オープンソースモデルの信頼性への打撃
- **引用URL:** https://www.remio.ai/post/yann-lecun-confirmed-meta-fudged-llama-4-benchmarks-the-scandal-is-bigger-than-one-model
- **Evidence ID:** EVD-20260514-0040

### INFO-041
- **タイトル:** AI data center investment: $900B opportunity, orbital compute, and $725B hyperscaler spending
- **ソース:** Business Insider / Yahoo Finance
- **公開日:** 2026-05-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Microsoft, Amazon, Google, Meta
- **要約:** AIデータセンター市場に$9000億の機会。Big 4ハイパースケーラー（Microsoft/Amazon/Alphabet/Meta）が今年$7250億をAIインフラに投資。Cowboy Space Corpが$2.75億調達で軌道データセンターを計画。Googleはテキサスに$400億投資、Stargate（OpenAI+SoftBank）は$5000億AIインフラ計画。
- **キーファクト:**
  - AIデータセンター市場: $9000億機会
  - Big 4ハイパースケーラー: 合計$7250億をAIインフラに投資（2026年）
  - 軌道データセンター: Cowboy Space Corp $2.75億調達
  - Google: テキサスに$400億、Stargate: $5000億AIインフラ
- **引用URL:** https://www.businessinsider.com/how-private-equity-chasing-data-center-opportunity-blackstone-ares-apollo-2026-5
- **Evidence ID:** EVD-20260514-0041

### INFO-042
- **タイトル:** AAIF (Agentic AI Foundation) under Linux Foundation gains adoption — ACP vs MCP vs A2A
- **ソース:** NeosAlpha / InvestorPlace
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic, OpenAI, Google, Block
- **要約:** Linux Foundation傘下のAgentic AI Foundation (AAIF) が2025年12月に設立され、OpenAI・Google・Anthropic・Block等が参加。97M+の月間SDKダウンロード。ACP (Agent Communication Protocol)、MCP、A2A等のエージェント標準プロトコルが競合・併存状態に。
- **キーファクト:**
  - AAIF: Linux Foundation傘下、2025年12月設立
  - 参加: OpenAI, Google, Anthropic, Block等
  - 97M+月間SDKダウンロード
  - ACP vs MCP vs A2A: 複数標準プロトコルの競合状態
- **引用URL:** https://neosalpha.com/blogs/ai-agent-protocols-acp-vs-mcp-vs-a2a/
- **Evidence ID:** EVD-20260514-0042

### INFO-043
- **タイトル:** ARC-AGI-3 launched specifically to evaluate "Seed IQ" — coding agents get 33%+
- **ソース:** Reddit / Bengoertzel Substack / arXiv
- **公開日:** 2026-05-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** N/A
- **要約:** ARC Prize Foundationが2026年3月25日にARC-AGI-3 (v3) をY Combinatorでローンチ。Seed IQの評価に特化。LLM + 手続き型世界モデル + 検証で33%以上のスコアを達成。実行可能なPython世界モデルを維持するコーディングエージェントシステムの評価。
- **キーファクト:**
  - ARC-AGI-3: Seed IQ評価向けに特化して設計
  - LLM単体トップスコア vs LLM+世界モデル+検証で33%+
  - 実行可能Python世界モデルによるコーディングエージェント評価
  - ARC-AGI-2のリセットで過去スコアの実効性が疑問視
- **引用URL:** https://www.reddit.com/r/agi/comments/1t66tsy/arc_prize_just_updated_arcagi3_specifically_to/
- **Evidence ID:** EVD-20260514-0043

### INFO-044
- **タイトル:** 'Mad Men' era over as AI takes over advertising — 15% headcount reduction
- **ソース:** AFR (Australian Financial Review)
- **公開日:** 2026-05-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** N/A
- **要約:** 英国のメディア支出の3分の2以上がテクノロジープラットフォームに直接流れ、メディアエージェンシーをバイパス。AIが広告業界の人員削減約15%をもたらした。AIクリエイティブ市場は爆発的に拡大し、24時間で100の広告バリエーションを約束する新エージェンシーが毎週登場。
- **キーファクト:**
  - 英国メディア支出の2/3+がテックプラットフォームに直接
  - AIによる広告業界の人員削減: 約15%
  - AIクリエイティブ市場の爆発的拡大
  - 従来の広告エージェンシーのバイパス進行
- **引用URL:** https://www.afr.com/world/north-america/mad-men-era-over-as-ai-takes-over-advertising-20260512-p5zw1u
- **Evidence ID:** EVD-20260514-0044

### INFO-045
- **タイトル:** WEF: 92 million jobs displaced by 2030, 78 million new opportunities for upskilled workers
- **ソース:** Forbes / WEF / Inc.
- **公開日:** 2026-05-11
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03, KIQ-002-04
- **関連企業:** N/A
- **要約:** World Economic Forum Future of Jobs Report: 2025-2030年で9200万の職が消滅する一方、7800万の新機会が創出されるが、スキルアップした労働者のみ対象。92%の組織がAI投資済みだが、78%がプロジェクトが停滞または失敗と報告。スキル変化がCEO問題に昇格。
- **キーファクト:**
  - WEF: 2025-2030年で92M職消滅、78M新機会創出
  - 92%の組織がAI投資済み、78%がプロジェクト停滞/失敗
  - 52%がAI使用ポリシー策定（2024年の46%から上昇）
  - LinkedIn: 2030年までに70%のスキルセットが変化
- **引用URL:** https://www.forbes.com/sites/catward/2026/05/11/the-ai-tsunami-doesnt-have-to-be-a-disaster/
- **Evidence ID:** EVD-20260514-0045

### INFO-046
- **タイトル:** Pentagon threatens Defense Production Act against Anthropic — coercion infrastructure
- **ソース:** Boston Sunday Globe / PressReader
- **公開日:** 2026-05-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** トランプ政権のAI駆動軍産複合体がAnthropicに圧力をかけ、Hegseth長官がDefense Production Actの発動を警告。Anthropicが拒否した場合のペンタゴンによる強制措置の可能性。政府が提供するのは「強制インフラ」であり、顧客は米国政府。
- **キーファクト:**
  - Hegseth長官: Anthropic拒否時にDPA発動を警告
  - トランプ政権のAI駆動軍産複合体
  - 政府「強制インフラ」の提供
  - Anthropicの安全性姿勢と政府圧力の衝突
- **引用URL:** https://www.pressreader.com/usa/boston-sunday-globe/20260510/282961046756867
- **Evidence ID:** EVD-20260514-0046

### INFO-047
- **タイトル:** US AI Safety Institute rebranded — focus shifts from safety to innovation
- **ソース:** Instagram / Quartz / WSGR
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** N/A
- **要約:** US AI Safety Instituteが革新重視にリブランド。CAISIが約40件のAIモデル評価を実施し国家セキュリティリスクを評価。一方、政府はAIセキュリティテストに関するページを静かに削除。4月23日にProtecting Consumers From Deceptive AI Actが連邦議会に提出。
- **キーファクト:**
  - US AI Safety Institute → 革新重視にリブランド
  - CAISI: 約40件のAIモデル国家セキュリティ評価
  - AIセキュリティテストページの削除
  - Protecting Consumers From Deceptive AI Act (4/23提出)
- **引用URL:** https://www.instagram.com/p/DYPiP1ij-aX/
- **Evidence ID:** EVD-20260514-0047

### INFO-048
- **タイトル:** Red Hat launches agentic AI developer tools — skill packs and sandboxing
- **ソース:** Red Hat / The New Stack
- **公開日:** 2026-05-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-001-03
- **関連企業:** Red Hat (IBM)
- **要約:** Red HatがエージェントAI向け開発者ツールをローンチ。Red Hat Desktop for local AI agents、分離AIサンドボックス、Red Hat Advanced Developer Suiteの強化。RHEL、OpenShift、Ansibleをガバナンス付きAIエージェントプラットフォームに変換するスキルパックを導入。
- **キーファクト:**
  - Red Hat Desktop: ローカルAIエージェント構築環境
  - 分離AIサンドボックス
  - スキルパック: RHEL/OpenShift/Ansibleをエージェントプラットフォーム化
  - metal-to-agentsスタックの提供
- **引用URL:** https://www.redhat.com/en/about/press-releases/red-hat-launches-new-developer-tools-agentic-ai
- **Evidence ID:** EVD-20260514-0048

### INFO-049
- **タイトル:** Google brings agentic AI to Android — Gemini Omni multimodal model leaked
- **ソース:** TechCrunch / X
- **公開日:** 2026-05-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** Google
- **要約:** GoogleがAndroidにエージェントAIとバイブコーディングウィジェットを導入。GboardにGeminiのマルチモーダル機能を活用した「Rambler」機能を追加。Gemini Omni統合マルチモーダルモデルがリーク。OpenAIがSora 2をシャットダウンしコンピュートをロボティクスに転用中。
- **キーファクト:**
  - AndroidにエージェントAIとバイブコーディングウィジェット導入
  - Gboard「Rambler」: Geminiマルチモーダル機能
  - Gemini Omni: 統合マルチモーダルモデルがリーク
  - OpenAI: Sora 2シャットダウン、コンピュートをロボティクスに転用
- **引用URL:** https://techcrunch.com/2026/05/12/google-brings-agentic-ai-and-vibe-coded-widgets-to-android/
- **Evidence ID:** EVD-20260514-0049

### INFO-050
- **タイトル:** Google Gemini 3.1 Flash Lite: $0.125/$0.75 per 1M tokens — new pricing tier
- **ソース:** Google AI / OpenRouter
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google
- **要約:** GoogleがGemini 3.1 Flash Liteの価格を設定。入力$0.125/1M tokens、出力$0.75/1M tokens。高効率マルチモーダルモデルで低レイテンシ・大容量ワークロード向け。無料枠も提供。Gemini API価格体系の最下層として位置づけ。
- **キーファクト:**
  - Gemini 3.1 Flash Lite: $0.125 input / $0.75 output per 1M tokens
  - 高効率マルチモーダルモデル
  - 低レイテンシ・大容量ワークロード向け
  - 無料枠あり
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Evidence ID:** EVD-20260514-0050

### INFO-051
- **タイトル:** Anthropic $30 billion new funding round in talks — largest AI funding yet
- **ソース:** YouTube (Bloomberg)
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Anthropicが$300億の新規資金調達を協議中。AI業界最大の資金調達ラウンドになる可能性。既に$600億評価での$20億調達を完了した数ヶ月後。Isomorphic Labs（DeepMind系）も$21億を調達し、AI創薬分野に大規模投資。
- **キーファクト:**
  - Anthropic: $300億新規調達協議中
  - 既に$600億評価で$20億調達完了
  - AI業界最大の資金調達ラウンドの可能性
- **引用URL:** https://www.youtube.com/watch?v=_-FfW1BFUoY
- **Evidence ID:** EVD-20260514-0051

### INFO-052
- **タイトル:** HumanityAI announces $18M grants for people-centered AI alignment research
- **ソース:** MacArthur Foundation / arXiv
- **公開日:** 2026-05-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** N/A
- **要約:** HumanityAIが$1800万の新規助成金を発表。$800万がAIを人間中心に保つ組織に、$1000万が新しい助成金プログラムに配分。AIアライメント研究はネガティブ（安全性）アライメントからポジティブ（人間の繁栄）アライメントへの転換が必要という議論。
- **キーファクト:**
  - HumanityAI: $18M助成金
  - $8M: 人間中心AI組織向け
  - $10M: 新規助成金プログラム
  - アライメント研究: ネガティブ→ポジティブ転換の議論
- **引用URL:** https://www.facebook.com/macarthurfdn/posts/-were-excited-to-share-that-humanityai-has-announced-18-million-in-new-grants-8-/1530266161794141/
- **Evidence ID:** EVD-20260514-0052
