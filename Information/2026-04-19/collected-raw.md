# 収集データ: 2026-04-19

## メタデータ
- 収集日時: 2026-04-19 00:00 UTC
- 品質フラグ: COLLECTING

## 動的追加クエリ（Arbiterフィードバックに基づく）
- KIQ-ARR-001: Anthropic $30B vs $19B乖離の第三者検証
- KIQ-NEW-SCR: SCR審査要件・Anthropic不合格理由の裏付け
- KIQ-NEW-DOLA: Dola/豆包第三者推定値（SensorTower/data.ai）
- KIQ-NEW-FEDPROC: 連邦機関AI調達先の月次推移データ

## 収集結果

### INFO-001
- **タイトル:** Codex for (almost) everything
- **ソース:** OpenAI Blog
- **公開日:** 2026-04-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIがCodexの大型アップデートを発表。バックグラウンドコンピューター使用（macOSで複数エージェント並列動作）、アプリ内ブラウザ、画像生成（gpt-image-1.5）、メモリ機能、自動化（長期タスクの自動スケジューリング）、90+の新規プラグイン（Atlassian Rovo, CircleCI, GitLab Issues等）を追加。300万以上の開発者が週次利用。
- **キーファクト:**
  - Codexがバックグラウンドコンピューター使用を開始（macOS、複数エージェント並列）
  - 90+の新規プラグイン追加（スキル+アプリ統合+MCPサーバーの統合）
  - メモリ機能と自動化（長期タスクスケジューリング）を導入
  - SSH接続、PRレビュー、複数ターミナルタブ対応
- **引用URL:** https://openai.com/index/codex-for-almost-everything/

### INFO-002
- **タイトル:** The next evolution of the Agents SDK
- **ソース:** OpenAI Blog
- **公開日:** 2026-04-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-001-03
- **関連企業:** OpenAI
- **要約:** OpenAIのAgents SDKが大型アップデート。ネイティブサンドボックス実行（Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel対応）、モデルネイティブハーネス、MCP/スキル/AGENTS.md/shell/apply-patchツール統合、Manifest抽象化によるポータブルワークスペース定義を導入。分離されたハーネスとコンピュートでセキュリティ・耐久性・スケーラビリティを向上。
- **キーファクト:**
  - ネイティブサンドボックス実行（7プロバイダー対応: Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel）
  - MCP、Skills (agentskills.io)、AGENTS.md、Shell、Apply Patch ツールを標準統合
  - Manifest抽象化でローカル→本番のポータビリティ実現
  - スナップショット・リハイドレーションによる耐久実行
  - Python先行、TypeScript対応予定
- **引用URL:** https://openai.com/index/the-next-evolution-of-the-agents-sdk/

### INFO-003
- **タイトル:** Introducing GPT-Rosalind for life sciences research
- **ソース:** OpenAI Blog
- **公開日:** 2026-04-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがライフサイエンス研究向けの専門モデルGPT-Rosalindを発表。薬剤発見、ゲノミクス解析、タンパク質推論に最適化。Amgen, Moderna, Allen Institute, Thermo Fisher等と提携。BixBenchで最高性能（Pass@1: 0.751）、Dyno Therapeuticsの評価で95%タイル以上の人間専門家を超える成績。Codex用Life Sciences研究プラグイン（50+データベース接続）をOSS公開。
- **キーファクト:**
  - ライフサイエンス特化型フロンティア推論モデル
  - BixBench Pass@1: 0.751（Gemini 3.1 Pro: 0.550, GPT-5.4: 0.732を上回る）
  - 50+の科学データベース・ツール接続のCodexプラグイン
  - Trusted Access Program（米国企業顧客限定、研究プレビュー期間中は無料）
  - Amgen, Moderna, Allen Institute, Thermo Fisher, Los Alamos National Lab等と提携
- **引用URL:** https://openai.com/index/introducing-gpt-rosalind/

### INFO-004
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic Blog
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Anthropic LabsがClaude Designを発表。Claude Opus 4.7を搭載したビジュアルデザインツール。プロトタイプ、スライド、マーケティング素材を対話で作成。デザインシステム自動構築、Canva/PDF/PPTX/HTMLエクスポート、Claude Codeへの直接ハンドオフ機能を備える。Pro/Max/Team/Enterprise向け。
- **キーファクト:**
  - Claude Opus 4.7搭載のビジュアルデザインツール（Anthropic Labs製品）
  - オンボーディング時にコードベースとデザインファイルからデザインシステム自動構築
  - Canva、PDF、PPTX、standalone HTMLエクスポート対応
  - Claude Codeへのワンクリックハンドオフ
  - Brilliant, Canva, Datadogが初期パートナーとして評価
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs

### INFO-005
- **タイトル:** Introducing Claude Sonnet 4.6
- **ソース:** Anthropic Blog
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-04, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 4.6はSonnet最強モデル。コーディング、コンピューター使用、長文脈推論、エージェント計画の全面アップグレード。1Mトークンコンテキストウィンドウ（ベータ）。価格はSonnet 4.5と同一（$3/$15 per M tokens）。Claude Codeで70%のユーザーがSonnet 4.5より好意、Opus 4.5より59%好意。OSWorld（コンピューター使用ベンチマーク）で大幅改善。
- **キーファクト:**
  - 1Mトークンコンテキストウィンドウ（ベータ）
  - OSWorld-VerifiedベンチマークでSonnet 4.5から大幅改善
  - Claude Codeでユーザーの70%がSonnet 4.5、59%がOpus 4.5より好意的評価
  - Vending-Bench Arenaで競合を圧倒（投資→利益転換戦略）
  - Databricks, Replit, Cursor, GitHub, Cognition等が推薦コメント
  - コンテキストコンパクション、ウェブ検索/フェッチ/コード実行/メモリ等がGA
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6

### INFO-006
- **タイトル:** Claude for Financial Services
- **ソース:** Anthropic Blog
- **公開日:** 2025-07-15 (Updated 2026-04-10)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaudeの金融サービス向け包括的ソリューションを発表。S&P Global, FactSet, PitchBook, Morningstar等のデータプロバイダーとMCP接続。Accenture, Deloitte, KPMG, PwC等が実装パートナー。AWS Marketplaceで利用可能。Bridgewater（AIA Labs）とCommonwealth Bank of Australiaが初期採用。AIGでのアンダーライティングで5x圧縮・90%以上の精度を実現。
- **キーファクト:**
  - 金融データプロバイダー（S&P Global, FactSet, PitchBook, Morningstar, Daloopa等）とMCP統合
  - Accenture, Deloitte, KPMG, PwC, Slalom等が実装パートナー
  - AWS Marketplaceで利用可能、Google Cloud Marketplace近日対応
  - AIG: アンダーライティング評価タイムライン5x圧縮、データ精度75%→90%+
  - Bridgewater: Investment Analyst Assistant、Commonwealth Bank of Australia: 詐欺防止・CS強化
- **引用URL:** https://www.anthropic.com/news/claude-for-financial-services

### INFO-007
- **タイトル:** Grok Speech to Text and Text to Speech APIs
- **ソース:** xAI Blog
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** xAI
- **要約:** xAIがGrok STT/TTS APIを発表。Tesla車両・Starlinkカスタマーサポートと同じスタック。STT: $0.10/hour（バッチ）・$0.20/hour（ストリーミング）。TTS: $4.20/1M文字。25+言語対応。Grok STTは電話エンティティWER 5.0%（ElevenLabs 12.0%）、全体WER 6.9%（ElevenLabs 9.0%）で競合を凌駕。スピーカータグ（[laugh], [whisper], <emphasis>等）による表現制御。
- **キーファクト:**
  - Grok STT: 全体WER 6.9%、電話エンティティWER 5.0%（競合最強）
  - Grok TTS: $4.20/1M文字、スピーチタグで感情・トーン制御
  - 25+言語対応、話者分離・マルチチャンネル対応
  - REST API + WebSocket API（リアルタイムストリーミング）
  - Tesla/Starlinkと同じオーディオスタック
- **引用URL:** https://x.ai/news/grok-stt-and-tts-apis

### INFO-008
- **タイトル:** Turn your best AI prompts into one-click tools in Chrome
- **ソース:** Google Blog
- **公開日:** 2026-04-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03, KIQ-001-04
- **関連企業:** Google
- **要約:** GoogleがChrome内でAIプロンプトをワンクリックツール（Skills）として保存・再利用できる機能を発表。「/」または「+」で呼び出し、複数タブのコンテキストで実行可能。プリセットのスキルライブラリも提供。Mac/Windows/ChromeOSで英語USユーザー向けにローンチ。
- **キーファクト:**
  - Chrome内のGeminiでAIプロンプトを保存・再利用（Skills）
  - 「/」または「+」で即座に呼び出し、複数タブのコンテキストで実行
  - プリセットスキルライブラリ提供
  - Chromeのセキュリティ基盤上に構築（自動レッドチーミング、自動更新）
  - Mac/Windows/ChromeOS、英語US向けロールアウト
- **引用URL:** https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/

### INFO-009
- **タイトル:** Gemini 3.1 Flash TTS: the next generation of expressive AI speech
- **ソース:** Google Blog
- **公開日:** 2026-04-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** Google
- **要約:** GoogleがGemini 3.1 Flash TTSを発表。Artificial Analysis TTSリーダーボードでElo 1,211を達成。オーディオタグによる音声スタイル・ペース・トーンの精密制御、70+言語対応、ネイティブマルチスピーカー対話、SynthID透かし入り。Google AI Studio、Vertex AI、Google Vidsで利用可能。
- **キーファクト:**
  - Artificial Analysis TTSリーダーボード Elo 1,211
  - 70+言語対応、ネイティブマルチスピーカー対話
  - オーディオタグによる精密な表現制御（自然言語コマンド）
  - SynthID透かしによるAI生成音声の識別
  - Google AI Studio、Vertex AI、Google Vidsで利用可能
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-tts/

### INFO-010
- **タイトル:** OpenAI Accelerating the cyber defense ecosystem
- **ソース:** OpenAI Blog
- **公開日:** 2026-04-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI
- **要約:** OpenAIがサイバー防衛エコシステムの加速を発表。セキュリティ分野でのエンタープライズ展開を強化。
- **キーファクト:**
  - サイバー防衛エコシステムの加速
  - Trusted Access Programの拡大（Apr 14別記事）
- **引用URL:** https://openai.com/index/accelerating-cyber-defense-ecosystem/

### INFO-011
- **タイトル:** OpenAI The next phase of enterprise AI
- **ソース:** OpenAI Blog
- **公開日:** 2026-04-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** OpenAI
- **要約:** OpenAIがエンタープライズAIの次フェーズを発表。エンタープライズ向け戦略・展開方針の更新。
- **キーファクト:**
  - エンタープライズAIの次フェーズ戦略
- **引用URL:** https://openai.com/index/next-phase-of-enterprise-ai/

### INFO-012
- **タイトル:** Google AI Impact Summit 2026 India
- **ソース:** Google Blog
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-002-01
- **関連企業:** Google
- **要約:** GoogleがインドでのAI Impact Summit 2026を開催。新たなグローバルパートナーシップと資金提供を発表。
- **キーファクト:**
  - インドでのAI Impact Summit開催
  - 新たなグローバルパートナーシップと資金提供発表
- **引用URL:** https://blog.google/innovation-and-ai/technology/ai/ai-impact-summit-2026-india/

### INFO-013
- **タイトル:** Introducing Claude Opus 4.7
- **ソース:** Anthropic Blog
- **公開日:** 2026-04-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Opus 4.7を一般提供開始。高度なソフトウェアエンジニアリングで大幅改善、特に最も困難なタスクで大幅な向上。ビジョン能力が3倍に向上（最大2,576px長辺、約3.75メガピクセル）。新しいxhigh effort レベル、タスクバジェット（パブリックベータ）、Claude Code用/ultrareviewスラッシュコマンドを導入。価格はOpus 4.6と同じ$5/$25 per M tokens。Mythos Previewの制限付きリリースに伴うサイバー防御機能の差別化低減を試みる最初のモデル。Claude Agent SDK v0.2.111がOpus 4.7対応。28社以上のパートナーが評価コメント提供（CursorBench 70% vs Opus 4.6の58%、XBOW視覚精度98.5% vs 54.5%等）。
- **キーファクト:**
  - 高解像度画像対応（最大2,576px長辺、Opus 4.6の3倍以上）
  - 新しいxhigh effortレベル（highとmaxの間）
  - タスクバジェット機能（パブリックベータ）
  - Claude Code用/ultrareviewコマンド、auto mode拡張
  - CursorBench: Opus 4.7 70% vs Opus 4.6 58%
  - XBOW視覚精度ベンチマーク: 98.5% vs Opus 4.6 54.5%
  - GitHub 93タスクベンチマークで13%向上
  - トークナイザ更新で同じ入力が1.0-1.35xトークンに増加の可能性
- **引用URL:** https://www.anthropic.com/news/claude-opus-4-7

### INFO-014
- **タイトル:** OpenAI updates its Agents SDK to help enterprises build safer, more capable agents
- **ソース:** TechCrunch
- **公開日:** 2026-04-15
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** OpenAI
- **要約:** TechCrunchがOpenAI Agents SDKのアップデートを報道。サンドボックス機能とモデルネイティブハーネスが主要追加機能。Oscar Healthが臨床記録ワークフロー自動化で本番利用可能と評価。Python先行、TypeScript対応予定。
- **キーファクト:**
  - サンドボックス分離でエージェントのリスクを低減
  - Oscar Healthが本番利用可能と評価（臨床記録ワークフロー）
  - 標準API価格で提供
- **引用URL:** https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/

### INFO-015
- **タイトル:** Claude Agent SDK v0.2.111-112: Opus 4.7対応
- **ソース:** GitHub Releases
- **公開日:** 2026-04-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** AnthropicのClaude Agent SDK TypeScript版がv0.2.111でOpus 4.7対応。MCPサーバーのper-tool permission_policy、startup()/WarmQueryの公開API化、envオーバーレイ動作変更を含む。v0.2.112でClaude Code v2.1.112とのパリティ達成。直近1週間でv0.2.101-112まで12リリース（毎日更新ペース）。
- **キーファクト:**
  - Opus 4.7サポート（v0.2.111以降必須）
  - MCP per-tool permission_policy対応
  - startup()/WarmQueryの公開API化
  - メモリrecallイベント/パス対応（v0.2.105）
  - セキュリティ修正: GHSA-5474-4w2j-mq4c対応（v0.2.101）
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases

### INFO-016
- **タイトル:** ByteDance DeerFlow 2.0: オープンソーススーパーエージェントハーネス
- **ソース:** Progressive Robot
- **公開日:** 2026-04-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** ByteDance
- **要約:** ByteDanceのDeerFlow 2.0はv1から全面書き直しのオープンソース（MIT）スーパーエージェントハーネス。LangGraph/LangChainベース、スキル・サブエージェント・サンドボックス実行・ファイルシステムアクセス・長期メモリを統合。研究レポートからスライド・Webページ・メディア生成まで対応。Dockerベースサンドボックス推奨。Doubao-Seed-2.0-Code、DeepSeek v3.2、Kimi 2.5等を推奨モデルとして紹介。SkillClaw（マルチユーザースキル進化フレームワーク）のコミュニティ貢献も進行。
- **キーファクト:**
  - v1から全面書き直し（コード共有なし）
  - MITライセンス、自己ホスト型
  - LangGraph/LangChainベース
  - Docker/Kubernetesサンドボックス対応
  - MCP、Slack/Telegramメッセージングチャネル対応
  - Claude Code統合スキルあり
  - 推奨モデル: Doubao-Seed-2.0-Code, DeepSeek v3.2, Kimi 2.5
- **引用URL:** https://www.progressiverobot.com/2026/04/11/what-is-deerflow-2-0/

### INFO-017
- **タイトル:** Cloudflare AI Platform: エージェント向け統一推論レイヤー
- **ソース:** Cloudflare Blog
- **公開日:** 2026-04-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** Cloudflare
- **要約:** CloudflareがAI Gatewayを統一推論レイヤーに進化。12+プロバイダー・70+モデルに1APIでアクセス可能。Alibaba Cloud, ByteDance, Google, OpenAI等のモデルを含む。マルチモーダルモデル（画像・動画・音声）も追加。BYOモデル（Cog技術でコンテナ化）対応予定。ReplicateがCloudflareに合流。Workers AI bindingで1行変更でモデル切替。エージェント向けの自動フェイルオーバー、ストリーミングレスポンスバッファリングを提供。
- **キーファクト:**
  - 12+プロバイダー・70+モデルを1APIで統合
  - 企業は平均3.5モデルを複数プロバイダーで使用
  - BYOモデル（Cog技術）対応予定
  - 自動フェイルオーバー（プロバイダー障害時に別プロバイダーへ自動ルーティング）
  - ストリーミングレスポンスのバッファリング（エージェント切断時の再接続対応）
  - ReplicateがCloudflare AI Platformチームに合流
- **引用URL:** https://blog.cloudflare.com/ai-platform/

### INFO-018
- **タイトル:** 8 Best AI Agent Frameworks for Enterprise in 2026
- **ソース:** Rasa Blog
- **公開日:** 2026-04-16
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03, KIQ-001-01
- **関連企業:** Various
- **要約:** Rasaが8つのエージェントフレームワークを評価。Rasa CALM 9.4/10（エンタープライズ向けトップ）、LangChain 7.6/10（柔軟性）、Microsoft Agent Framework 7.2/10（Azure統合）、CrewAI 7.0/10（マルチエージェント協調）、Vellum 7.1/10（ローコード）等。評価基準: オーケストレーション20%、ガバナンス20%、デプロイ柔軟性15%、拡張性15%、音声10%、価格10%、コミュニティ10%。LangChain 2500万+ダウンロード、CrewAI 60%のFortune 500採用を主張。Semantic KernelとAutoGenはメンテナンスモードに移行（Microsoft Agent Frameworkが後継）。
- **キーファクト:**
  - Rasa CALM: エンタープライズ向け9.4/10、ガバナンス10/10
  - LangChain: 2500万+ダウンロード、最大エコシステム
  - Microsoft Agent Framework: AutoGen+Semantic Kernel統合、Q1 2026 GA目標
  - CrewAI: 450M+/月ワークフロー処理、Apache 2.0
  - Semantic Kernel/AutoGen: メンテナンスモード移行
- **引用URL:** https://rasa.com/blog/best-ai-agent-framework

### INFO-019
- **タイトル:** AI Agent Security Maturity Audit: 97% of enterprises expect incident within 12 months
- **ソース:** VentureBeat
- **公開日:** 2026-04-17
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-002-01, KIQ-001-01
- **関連企業:** Various
- **要約:** VentureBeat調査（108企業）: 97%のセキュリティリーダーが12ヶ月以内にAIエージェント関連の重大インシデントを予期。OWASP Agentic Applications Top 10 2026を形式化。3段階セキュリティ成熟度監査（Observe→Enforce→Isolate）を提案。Anthropic Managed Agentsがステージ3（サンドボックス分離）をベータ提供（$0.08/session-hour）。OpenAI Agents SDKのPythonサンドボックスもベータ。Mercor $10Bサプライチェーン侵害、Meta不正AIエージェント事例（2026年3月）を分析。45.6%が共有APIキー使用、25.5%のエージェントが他エージェントを作成可能。
- **キーファクト:**
  - 97%が12ヶ月以内に重大AIエージェントインシデント予期（Arkose Labs 2026）
  - 88%が過去12ヶ月以内にAIエージェントセキュリティインシデント報告
  - 45.6%が共有APIキー使用、21.9%のみエージェントに固有ID付与
  - OWASP Top 10 for Agentic Applications 2026形式化
  - Anthropic Managed Agents: ベータ$0.08/session-hour
  - Mercor $10Bサプライチェーン侵害（LiteLLM経由）
  - 43%のAI生成コード変更が本番でデバッグ必要
- **引用URL:** https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds

### INFO-020
- **タイトル:** Grok models on Google Vertex AI
- **ソース:** Google Cloud Docs
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** xAI, Google
- **要約:** xAI GrokモデルがGoogle Vertex AIでマネージドAPIとして利用可能に。Grok 4.20（Reasoning/Non-Reasoning）、Grok 4.1 Fast（Reasoning/Non-Reasoning）の4モデル。Grok 4.20は「業界最低のハルシネーション率」を特徴とし、長期エージェントツール呼び出しに優れる。Grok 4.1 Fastは検索タスク向けのコスト効率モデル。
- **キーファクト:**
  - Grok 4.20 Reasoning: フラッグシップ、低ハルシネーション率
  - Grok 4.1 Fast: コスト効率型、検索タスク向け
  - Vertex AIでマネージドAPI提供（SSEストリーミング対応）
  - Google Cloudの既存認証・IAMインフラでアクセス可能
- **引用URL:** https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/grok



## X (Twitter) 投稿データ（ローカルRSSHub経由）

### INFO-021
- **タイトル:** @AmandaAskell (Amanda Askell) のX投稿
- **ソース:** X (Twitter) - @AmandaAskell (Claudeの人格設計研究者)
- **公開日:** 2026-04-19
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** I might pause tweeting about AI for a while and get back to my shower thought roots. People on here seem to have all the AI takes covered.
- **引用URL:** https://x.com/AmandaAskell/status/2045556055556731249

### INFO-022
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-04-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** Agents that run code need a controlled workspace ready when work starts.

@modal shares why scale matters for long-running agents built with the Agents SDK.
- **引用URL:** https://x.com/OpenAIDevs/status/2045561701010202826

