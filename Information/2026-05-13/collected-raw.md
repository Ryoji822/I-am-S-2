# 収集データ: 2026-05-13

## メタデータ
- 収集日時: 2026-05-13 00:00 UTC
- 品質フラグ: COLLECTING

## 収集結果

### INFO-001
- **タイトル:** OpenAI launches the OpenAI Deployment Company (DeployCo)
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01, KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIが新会社「OpenAI Deployment Company (DeployCo)」を立ち上げ、エンタープライズAI展開サービスに本格参入。Tomoro（約150名のFDEを擁するAIコンサルティング企業）の買収を合意。TPG主導、Advent/Bain Capital/Brookfield共同リード、19の投資・コンサルティング企業がパートナーとして参加。初期投資額$40億超。
- **キーファクト:**
  - DeployCoはOpenAIが過半数所有・支配する独立事業単位
  - Forward Deployed Engineers (FDE)を顧客組織に常駐させ、AI本番システムを設計・構築
  - Tomoro買収でTesco/Virgin Atlantic/Supercell等の実績を持つ150名のエンジニアを獲得
  - 19パートナー（TPG, Advent, Bain Capital, Brookfield, McKinsey, Capgemini等）が参画
  - 初期投資$40億超でスケールと買収に充当
- **引用URL:** https://openai.com/index/openai-launches-the-deployment-company/
- **Evidence ID:** EVD-20260513-0001

### INFO-002
- **タイトル:** What Parameter Golf taught us
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-004-02
- **関連企業:** OpenAI
- **要約:** OpenAIが主催したML研究コミュニティチャレンジ「Parameter Golf」の結果報告。1,000+参加者、2,000+提出物を集め、AIコーディングエージェントの広範な活用が確認された。16MB制限・10分トレーニング予算という厳しい条件下でのモデル最適化技術を競い、量子化や新規モデリング手法が多数登場。
- **キーファクト:**
  - AIコーディングエージェントの参加者の大半が使用し、実験コストを大幅に低下
  - GPTQ量子化、Muon optimizer、Test-time training等の革新的手法が登場
  - OpenAI内部でCodexベースのトリアージボットを開発し、数百件/日の提出を処理
  - RunRunPodが$100万のコンピュートスポンサーとして参加
- **引用URL:** https://openai.com/index/what-parameter-golf-taught-us/
- **Evidence ID:** EVD-20260513-0002

### INFO-003
- **タイトル:** Advancing voice intelligence with new models in the API (GPT-Realtime-2)
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIが3つのリアルタイム音声モデルをAPIで提供開始。GPT-Realtime-2（GPT-5クラスの推論能力を持つ音声モデル）、GPT-Realtime-Translate（70+入力言語→13出力言語のリアルタイム翻訳）、GPT-Realtime-Whisper（ストリーミング音声認識）。コンテキストウィンドウ32K→128Kに拡大。
- **キーファクト:**
  - GPT-Realtime-2: Big Bench Audioで+15.2%向上、Audio MultiChallengeで+13.8%向上
  - 価格: $32/1M audio input tokens, $64/1M audio output tokens
  - ZillowがFair Housing遵守で26ポイントのコール成功率向上（95% vs 69%）を確認
  - Deutsche Telekom, Priceline, BolnaAI等が早期採用
  - 推論レベル設定（minimal/low/medium/high/xhigh）を導入
- **引用URL:** https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
- **Evidence ID:** EVD-20260513-0003

### INFO-004
- **タイトル:** Testing ads in ChatGPT — UK/Mexico/Brazil/Japan/Koreaに拡大
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-05, KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPT広告テストを英国・メキシコ・ブラジル・日本・韓国に拡大。広告は回答に影響しないことを原則とし、会話プライバシーを保護。消費者信頼度指標への影響なし、広告却下率は低いと報告。Free/Go層対象、Plus/Pro/Business/Enterprise/Educationは広告なし。
- **キーファクト:**
  - 既に米国・カナダ・豪州・NZでパイロット実施済み
  - 消費者信頼度指標への影響なし、広告却下率低い、関連性改善中
  - 会話トピック・過去チャット・広告インタラクション履歴で広告マッチング
  - 広告主はチャット内容にアクセス不可、集計データのみ受領
- **引用URL:** https://openai.com/index/testing-ads-in-chatgpt/
- **Evidence ID:** EVD-20260513-0004

### INFO-005
- **タイトル:** Introducing Trusted Contact in ChatGPT
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** OpenAI
- **要約:** ChatGPTに「Trusted Contact」安全機能を導入。成人ユーザーが信頼する人物を登録し、自傷行為の深刻な懸念が検出された場合に通知。APA等の臨床専門家の指導で開発。通知は専門訓練を受けた人間レビュアーが1時間以内に審査。
- **キーファクト:**
  - 18歳以上（韓国は19歳以上）が1名の信頼できる連絡先を登録可能
  - 自動監視システム＋専門訓練レビュアーの二段階審査
  - 通知にチャット詳細は含まず、一般的な理由のみ共有
  - APAや260+の医師からなるGlobal Physicians Networkの指導で開発
- **引用URL:** https://openai.com/index/introducing-trusted-contact-in-chatgpt/
- **Evidence ID:** EVD-20260513-0005

### INFO-006
- **タイトル:** Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber
- **ソース:** OpenAI Official Blog
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.5-Cyberを限定プレビューで提供開始。Trusted Access for Cyber (TAC)フレームワークで、検証済み防御者へのアクセスレベル管理。GPT-5.5+TACは大部分の正当な防御ワークフローに対応し、GPT-5.5-Cyberはレッドチーミング等の特殊ワークフロー向け。
- **キーファクト:**
  - TAC: ID/信頼ベースのフレームワークで、強化されたサイバー能力を適切な使用者に提供
  - Cisco, Intel, SentinelOne, Snyk等がパートナーとして協力
  - セキュリティフライホイール（脆弱性発見→パッチ→検知→サプライチェーンセキュリティ）を加速
  - 2026年6月1日以降、フィッシング耐性認証が必須に
- **引用URL:** https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/
- **Evidence ID:** EVD-20260513-0006

### INFO-007
- **タイトル:** Introducing Claude Sonnet 4.6
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Sonnet 4.6をリリース。コーディング・コンピュータ使用・長文脈推論・エージェント計画・ナレッジワーク・デザインの全面アップグレード。1Mトークンコンテキストウィンドウ（ベータ）。価格はSonnet 4.5と同一（$3/$15 per 1M tokens）。
- **キーファクト:**
  - Claude Codeでユーザーの70%がSonnet 4.5よりSonnet 4.6を好む、59%がOpus 4.5より好む
  - OSWorld（コンピュータ使用ベンチマーク）で大幅改善
  - Vending-Bench Arenaで投資→収益性への戦略的ピボット戦略を自律的に開発
  - Databricks, Replit, Cursor, GitHub, Cognition等が推奨
  - web search, fetch, code execution, memory, programmatic tool callingがGA
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6
- **Evidence ID:** EVD-20260513-0007

### INFO-008
- **タイトル:** Building a new enterprise AI services company with Blackstone, H&F, and Goldman Sachs
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-05-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01, KIQ-003-04
- **関連企業:** Anthropic
- **要約:** AnthropicがBlackstone, Hellman & Friedman, Goldman Sachsと共同で新AIサービス会社を設立。中堅企業向けにClaudeをコア業務に組み込む展開支援。General Atlantic, Apollo, GIC, Sequoia Capital等も出資。AnthropicのApplied AIエンジニアが顧客企業に常駐。
- **キーファクト:**
  - 中堅企業（地域医療機関、コミュニティバンク等）をターゲット
  - Anthropic Applied AIスタッフが顧客先に常駐し、カスタムソリューションを構築
  - Claude Partner Network（Accenture, Deloitte, PwC等）の拡張として位置づけ
  - 大手代替資産運用会社コンソーシアムが出資
- **引用URL:** https://www.anthropic.com/news/enterprise-ai-services-company
- **Evidence ID:** EVD-20260513-0008

### INFO-009
- **タイトル:** Agents for financial services
- **ソース:** Anthropic Official Blog
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02, KIQ-001-03, KIQ-002-04
- **関連企業:** Anthropic
- **要約:** Anthropicが金融サービス向けに10個のエージェントテンプレートをリリース。ピッチブック作成、KYC審査、月末決算等を自動化。Microsoft 365（Excel/PowerPoint/Word/Outlook）との統合。Opus 4.7がVals AI Finance Agent benchmarkで64.37%で業界トップ。8つの新コネクタとMoody's MCPアプリを追加。
- **キーファクト:**
  - Claude Opus 4.7がVals AI Finance Agent benchmark 64.37%で業界最高
  - 10個のエージェントテンプレート（Pitch builder, KYC screener, Month-end closer等）
  - Claude Cowork / Claude Code用プラグイン + Managed Agents用クックブック
  - Citadel, FIS, BNY, Carlyle, Mizuho等がClaude採用を公表
  - 新コネクタ: Dun & Bradstreet, Fiscal AI, Financial Modeling Prep, IBISWorld, Verisk等
- **引用URL:** https://www.anthropic.com/news/finance-agents
- **Evidence ID:** EVD-20260513-0009

### INFO-010
- **タイトル:** AI Impact Summit 2026: Google's partnerships in India
- **ソース:** Google Official Blog
- **公開日:** 2026-02-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-003-04, KIQ-005-03
- **関連企業:** Google
- **要約:** GoogleがインドAI Impact Summitでインフラ・科学・政府能力構築への投資を発表。$150億インドAI基盤投資、$30M AI for Government Innovation Impact Challenge、$30M AI for Science Impact Challenge等。Google DeepMindの国家パートナーシップ制度開始。
- **キーファクト:**
  - インドに$150億投資でAI基盤インフラ構築
  - Google.org $30M AI for Government Innovation Impact Challenge
  - Google.org $30M AI for Science Impact Challenge
  - DeepMind National Partnerships for AI制度開始
  - 1億人以上のデジタルスキル訓練実績
- **引用URL:** https://blog.google/innovation-and-ai/technology/ai/ai-impact-summit-2026-india/
- **Evidence ID:** EVD-20260513-0010

### INFO-011
- **タイトル:** Gemini API File Search is now multimodal
- **ソース:** Google Official Blog
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Google
- **要約:** Gemini API File Searchツールがマルチモーダル対応。画像+テキストの統合検索、カスタムメタデータ、ページレベル引用の3つの主要アップデート。Gemini Embedding 2モデルで画像ネイティブデータを理解。
- **キーファクト:**
  - 画像とテキストを統合したマルチモーダルRAG構築が可能に
  - カスタムメタデータでキーバリューラベル付与、クエリ時フィルタリング
  - ページレベル引用で回答の出典ページ番号を提示
  - Gemini 3 Flash Previewで利用可能
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/
- **Evidence ID:** EVD-20260513-0011

### INFO-012
- **タイトル:** OpenAI Agents SDK SandboxAgent with lazy-loaded skills
- **ソース:** GoPenAI (Medium)
- **公開日:** 2026-05-12
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKのSandboxAgentとlazy-loaded Skills機能の実践的活用法。OBaI（マルチエージェント金融リサーチシステム）がorchestrator hubをSandboxAgentに移行し、lazy skillsでコンテキスト膨張を解消。GPT-5.5へのアップグレードでMCP Atlas 70.6%→75.3%等のツール使用品質改善を確認。
- **キーファクト:**
  - SandboxAgent: harness（制御面）とsandbox（実行面）の分離概念
  - Lazy-loaded Skills: 必要なスキルのみオンデマンドでロード、コンテキスト最適化
  - GPT-5.5価格: $5/1M input, $30/1M output（GPT-5.1の$1.25/$10より高価）
  - エージェントごとのモデル選択が重要（orchestratorに高性能モデル、specialistに低コストモデル）
- **引用URL:** https://blog.gopenai.com/how-the-openai-agents-sdk-helped-obai-scale-its-multi-agent-research-stack-f0fd73e57b34
- **Evidence ID:** EVD-20260513-0012

### INFO-013
- **タイトル:** OpenAI WebSocket Responses APIで最大40%レイテンシ削減
- **ソース:** InfoQ
- **公開日:** 2026-05-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがResponses APIにWebSocketベースの実行モードを導入。従来のHTTPリクエスト・レスポンスパターンを永続的・双方向接続に置き換え、エージェントワークフローのレイテンシを最大40%削減。Vercel/Cline/Cursor等が即座に統合。
- **キーファクト:**
  - 最大40%レイテンシ削減、約1,000 TPS持続・バースト4,000 TPS
  - Vercel: 40%レイテンシ削減、Cline: 39%改善、Cursor: 最大30%改善
  - CodexがResponses APIトラフィックの大部分をWebSocketモードに移行済み
  - ZDR（Zero Data Retention）互換
- **引用URL:** https://www.infoq.com/news/2026/05/openai-websocket-responses-api/
- **Evidence ID:** EVD-20260513-0013

### INFO-014
- **タイトル:** Claude Agent SDK v0.2.139リリース、頻繁な更新継続
- **ソース:** GitHub Releases
- **公開日:** 2026-05-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK（TypeScript版）v0.2.139リリース。Claude Code v2.1.139とパリティ。v0.2.136でresolveSettings()（alpha）追加、TodoWrite非推奨→Task tools移行。v0.2.133でV2 session API非推奨→query()推奨。毎日更新。
- **キーファクト:**
  - v0.2.136: resolveSettings()追加（MDM plist/HKLM/HKCU読み取り）、TodoWrite→TaskCreate/TaskGet/TaskUpdate/TaskList移行
  - v0.2.133: V2 session API非推奨、query()推奨
  - 1.4k GitHub stars、160 forks
  - 毎日リリースペース（Claude Code本体に追従）
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260513-0014

### INFO-015
- **タイトル:** 12 Best AI Agent Frameworks in 2026 — Claude Agent SDKとLangGraphがリード
- **ソース:** Respan
- **公開日:** 2026-05-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** 2026年のエージェントフレームワーク比較ランキング。Claude Agent SDK（Anthropic-first）、LangGraph（複雑なstateful本番）、Vercel AI SDK（TypeScript）、OpenAI Agents SDK（OpenAI-first）、CrewAI（高速プロトタイプ）等12フレームワークを評価。最大の変化はAnthropicのClaude Agent SDKとVercel AI SDK 6の台頭。
- **キーファクト:**
  - Claude Agent SDK: Anthropic-first、コーディング・computer-useに最適、マルチエージェントセッション・アウトカムはMay 2026にパブリックベータ
  - Vercel AI SDK: 20M+ monthly npm downloads、25+プロバイダー対応
  - LangGraph: 複雑なstateful本番エージェントに最適、2026年初頭にCrewAIをGitHub starsで逆転
  - Google ADK: A2A protocol、マルチモーダル対応
  - 全フレームワークOSS
- **引用URL:** https://www.respan.ai/articles/best-ai-agent-frameworks-2026
- **Evidence ID:** EVD-20260513-0015

### INFO-016
- **タイトル:** ByteDance Coze 2.5 — "Agent World"エコシステム導入
- **ソース:** KuCoin News
- **公開日:** 2026-04-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのエージェントプラットフォームCoze 2.5が「Agent World」エコシステムを導入。AIエージェントがチャットUIを超えて、独立した実行環境・スキル・アイデンティティを持つ自律的デジタルコンパニオンへ。専用クラウドデバイス・個人ワークスペース・長期記憶・デジタルソーシャルIDを提供。
- **キーファクト:**
  - 「フル装備デバイス」: 専用クラウドデバイス（クラウドPC・クラウド携帯）+ 個人ワークスペース（スケジュール・クラウドストレージ）で7×24稼働
  - 「フル装備スキル」: 動画制作・プログラミング（Kozi CLI）・法律・金融等の専門スキル
  - 「フル装備パーソナリティ」: 管理可能な記憶 + デジタルソーシャルID（メールID）
  - オープンエコシステムでエージェント間の社会的相互作用を目指す
- **引用URL:** https://www.kucoin.com/news/flash/bytedance-s-coze-launches-version-2-5-introduces-agent-world-ecosystem
- **Evidence ID:** EVD-20260513-0016

### INFO-017
- **タイトル:** xAI Grok 4.20/4.1 Fast — Vertex AIで利用可能
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** xAI, Google
- **要約:** xAI GrokモデルがGoogle Vertex AIでマネージドAPIとして利用可能。Grok 4.20（Reasoning/Non-Reasoning）は業界最低クラスのハルシネーション率、Grok 4.1 Fast（Reasoning/Non-Reasoning）はコスト効率重視。Google Cloudパートナーモデルとして提供。
- **キーファクト:**
  - Grok 4.20 Reasoning: フラッグシップモデル、低ハルシネーション、ドキュメント理解・長期エージェントツール呼び出しに優れる
  - Grok 4.20 Non-Reasoning: レイテンシ敏感な用途向け
  - Grok 4.1 Fast: コスト効率重視、強力なツール呼び出し・KB合成
  - Vertex AI経由でストリーミング対応（SSE）
- **引用URL:** https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/grok
- **Evidence ID:** EVD-20260513-0017

### INFO-018
- **タイトル:** LangGraph vs CrewAI vs AutoGen vs Pydantic AI — フレームワーク比較
- **ソース:** Medium
- **公開日:** 2026-05-11
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** N/A
- **要約:** 同じエージェントワークフローを4フレームワーク（LangGraph, CrewAI, AutoGen, Pydantic AI）で実装し比較。メモリ、コンテキスト管理、ツール呼び出し、デバッグ、信頼性、障害回復を評価。LangGraphが最もバランスが良く、CrewAIはプロトタイプ向け、AutoGenは混乱したブランディング問題を指摘。
- **キーファクト:**
  - LangGraph: 複雑なエージェントで最も安定、状態グラフが適切な抽象化
  - CrewAI: 最速プロトタイプ、ただし本番スケールで制御不足
  - AutoGen/AG2: Microsoft v0.4リライトが混乱、AG2（コミュニティ版）が本番実績あり
  - Pydantic AI: 型安全だが機能が少ない
- **引用URL:** https://medium.com/@inprogrammer/i-compared-4-python-ai-agent-frameworks-langgraph-won-clearly-f5adec0e1981
- **Evidence ID:** EVD-20260513-0018
