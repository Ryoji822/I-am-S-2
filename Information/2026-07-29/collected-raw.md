# 収集データ: 2026-07-29

## メタデータ
- 収集日時: 2026-07-29 00:00 UTC
- 品質フラグ: COMPLETE
- INFOエントリ数: 66
- Evidence ID範囲: EVD-20260729-0001 ～ EVD-20260729-0066
- 実行検索クエリ数: 97+（collection_plan.json 97クエリ + Arbiter動的5クエリ + 補完クエリ）
- 公式ブログスクレイプ数: 5（Anthropic, xAI, OpenAI, Google）
- KIQカバレッジ: 24/24 KIQ + 5動的KIQ（全PIRカバー）
- 品質フラグ:
  - A-3（公式一次ソース）: 14件
  - A-2（公式+第三者検証）: 2件
  - B-1/B-2（信頼できる二次ソース）: 28件
  - C-1/C-2/C-3（推定・未検証）: 22件
- 企業カバレッジ:
  - OpenAI: 12件
  - Anthropic: 14件
  - Google/DeepMind: 11件
  - xAI: 5件
  - ByteDance: 10件
  - Microsoft: 5件
  - Amazon: 3件
  - Meta: 3件
  - その他: 複数

## 動的追加クエリ（Arbiterフィードバックに基づく）
- KIQ-CAR-002-OPS: シニアエンジニア求人スキル要件内訳（設計/評価/方向付け固有倍率）
- KIQ-OAI-001: OpenAI政府vs民間収益内訳
- KIQ-ANT-002: Claude Code固有DAU/WAU（第三方推定）
- KIQ-MIL-001: 軍事AI人間却下比率（GAO報告書・議会証言）
- 新規: ByteDance消費者データ第三者検証（QuestMobile等）

## 収集結果

### INFO-001
- **タイトル:** Anthropic invests $100 million into the Claude Partner Network
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-03-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Anthropicは企業向けClaude採用を支援するパートナーネットワークを立ち上げ、初期投資として1億ドルを拠出。パートナー向け技術認定、共同市場開発、専属Applied AIエンジニアの提供を含む。チームを5倍に拡大。
- **キーファクト:**
  - 1億ドルの初期投資（2026年）
  - Claude Certified Architect認定をローンチ
  - Code Modernizationスターターキット提供
  - ClaudeはAWS/Google Cloud/Microsoft Azureの3大手クラウド全てで利用可能な唯一のフロンティアAIモデル
  - Cognizantが30,000名をトレーニング
- **引用URL:** https://www.anthropic.com/news/claude-partner-network
- **Evidence ID:** EVD-20260729-0001

### INFO-002
- **タイトル:** Anthropic partners with the UK Government to bring AI assistance to GOV.UK services
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-01-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicが英国DSITと提携し、GOV.UK向けAIアシスタントを構築・パイロット。就職支援を初期ユースケースとする。英国AI Security Instituteと協力してモデルをテスト・評価。
- **キーファクト:**
  - DSITによる選定、GOV.UK AIアシスタントの構築
  - 初期ユースケースは雇用支援（求職・トレーニング）
  - UK AI Security Instituteとの協力継続
  - Anthropic London拠点拡大中
- **引用URL:** https://www.anthropic.com/news/gov-UK-partnership
- **Evidence ID:** EVD-20260729-0002

### INFO-003
- **タイトル:** Anthropic expands partnership with Google and Broadcom for multiple gigawatts of next-generation compute
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-002-01
- **関連企業:** Anthropic, Google, Broadcom
- **要約:** AnthropicはGoogleとBroadcomと次世代TPU容量の複数ギガワット契約を締結（2027年稼働予定）。ランレート収益が300億ドルを突破、$100万+年間消費企業が1000社を超える。
- **キーファクト:**
  - ランレート収益300億ドル超（2025年末約90億ドルから急成長）
  - $100万+年間消費企業が1000社超（2ヶ月で倍増）
  - 500億ドルの米国AIインフラ投資の拡張
  - AWS Trainium/Google TPU/NVIDIA GPUの混合プラットフォーム
  - Claudeは3大クラウドプラットフォーム全てで利用可能
- **引用URL:** https://www.anthropic.com/news/google-broadcom-partnership-compute
- **Evidence ID:** EVD-20260729-0003

### INFO-004
- **タイトル:** Introducing Build Mode (xAI/SpaceXAI)
- **ソース:** xAI公式ブログ
- **公開日:** 2026-07-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI (SpaceX子会社)
- **要約:** xAIがBuild Modeを発表。Grokにアイデアを伝えるだけでWebサイト、アプリ、ゲーム、インタラクティブダッシュボードを作成・公開可能。SuperGrok Heavy購読者向けEarly Beta。
- **キーファクト:**
  - ウェブ、iOS、Androidで利用可能
  - grok.meリンクまたはカスタムドメインで公開
  - 3Dゲーム、都市シミュレーション、物理エンジン、ビートマシン等をデモ
  - SuperGrok Heavy購読者限定（Early Beta）
- **引用URL:** https://x.ai/news/grok-build-mode
- **Evidence ID:** EVD-20260729-0004

### INFO-005
- **タイトル:** Grok in Google Workspace
- **ソース:** xAI公式ブログ
- **公開日:** 2026-07-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** xAI (SpaceX子会社)
- **要約:** xAIがGoogle Workspace向けGrokアドオンを発表。Sheets/Slides/Docs内でGrokを直接使用可能。無料アドオン。Microsoft 365（Word/Excel/PowerPoint/Outlook）にも対応済み。
- **キーファクト:**
  - Google Workspace Marketplaceから無料インストール
  - Sheets: セル参照付き回答、数式記入、チャート挿入
  - Slides: アウトラインからプレゼン生成、Xから研究追加
  - Docs: ノートを構造化ドラフトに変換、 connectorsでDrive/Email連携
  - Microsoft 365全アプリにも対応済み
- **引用URL:** https://x.ai/news/introducing-google-workspace-addon
- **Evidence ID:** EVD-20260729-0005

### INFO-006
- **タイトル:** Workflows in Grok Build
- **ソース:** xAI公式ブログ
- **公開日:** 2026-07-23
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI (SpaceX子会社)
- **要約:** Grok Buildがワークフロー機能を追加。自然言語でタスクを記述すると、最大128（大規模時1024）の並列エージェントに展開し、結果を検証して統合レポートを生成。PRレビューやイシュートリアージ等に対応。
- **キーファクト:**
  - 最大128エージェント（大規模ジョブ時1024）の並列実行
  - ワークフローは.grok/workflows/に保存・チーム共有可能
  - /deep-researchビルトインコマンド搭載
  - フェーズ単位の保存・再開対応
  - ワークフロー自体がスラッシュコマンド化（引数渡し可能）
- **引用URL:** https://x.ai/news/workflows
- **Evidence ID:** EVD-20260729-0006

### INFO-007
- **タイトル:** Launching Health in ChatGPT
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-23
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-02
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPTにHealth機能をローンチ。米国ユーザーがApple Healthと医療記録をセキュアに接続し、ChatGPTでパーソナライズされた健康インサイトを得られる。GPT-5.6 Solが健康領域で最強。
- **キーファクト:**
  - 毎週3億人がChatGPTで健康関連の質問
  - Apple Health + 医療記録（US病院システム/One Medical/Function Health）接続
  - 接続データは基盤モデルのトレーニングや広告に不使用
  - GPT-5.5 Instant（無料ユーザー）とGPT-5.6 Sol（有料ユーザー）が健康推論を強化
  - GPT-5.6 SolがHealthBench Professionalで最高性能
- **引用URL:** https://openai.com/index/health-in-chatgpt/
- **Evidence ID:** EVD-20260729-0007

### INFO-008
- **タイトル:** Gemini API Managed Agents: 3.6 Flash, hooks, and more
- **ソース:** Google公式ブログ (blog.google)
- **公開日:** 2026-07-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Google / DeepMind
- **要約:** GoogleがGemini API Managed Agentsの新機能を発表。Gemini 3.6 Flashがデフォルトモデルに。環境フック（pre/post tool execution）、予算制御、スケジュールトリガー、フリーティアアクセスを追加。
- **キーファクト:**
  - Gemini 3.6 Flashがantigravityエージェントのデフォルトに
  - 環境フック: ツール呼び出し前後にカスタムスクリプト実行可能
  - 予算制御: max_total_tokensで実行を安全に一時停止・再開
  - スケジュールトリガー: cronスケジュールでエージェント自動実行
  - フリーティアでManaged Agents利用可能に
  - OffDeal（AIネイティブ投資銀行）が本番検証パイプラインに活用
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/
- **Evidence ID:** EVD-20260729-0008

### INFO-009
- **タイトル:** Google commits $40M to the Genesis Mission
- **ソース:** Google Cloud公式ブログ
- **公開日:** 2026-07-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-002-06
- **関連企業:** Google / DeepMind
- **要約:** GoogleがDOE（米国エネルギー省）Genesis Missionに4000万ドルのAIトークン・クラウドクレジットを拠出。AlphaEvolve、AlphaFold 3、AlphaGenome等の科学AIツールをDOE国立研究所に提供。
- **キーファクト:**
  - 4000万ドルのAIトークン・クラウドクレジット拠出
  - 17のDOE国立研究所にAI for Scienceツール提供
  - PNNL: AlphaEvolveで数学システム探索を自動化
  - NLR: Geminiで顕微鏡キャリブレーション時間を90分→13分に短縮
  - Gemini for Government座席を数万名に提供
- **引用URL:** https://cloud.google.com/blog/topics/public-sector/accelerating-frontiers-of-scientific-discovery-40-million-dollar-commitment-genesis-mission
- **Evidence ID:** EVD-20260729-0009

### INFO-010
- **タイトル:** Senior engineer job requirements increasingly require AI tool evaluation and design skills
- **ソース:** LinkedIn / Built In SF / Disney Careers
- **公開日:** 2026-07-29
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-CAR-002-OPS (動的追加)
- **関連企業:** Disney, Alignerr, Autodesk
- **要約:** シニアエンジニア求人がAI評価・設計スキルを明示的に要件化し始めている。Disneyの求人ではAGENTS.md/CLAUDE.mdの作成、Cursor/Claude Codeの効果的利用、AI生成コードのレビュー（ハルシネーション検出、プロンプトインジェクションリスク）が必須要件として記載。
- **キーファクト:**
  - Disney Sr Engineer: AI coding tools (Cursor, Claude Code) の効果的・責任ある利用が必須要件
  - AGENTS.md/CLAUDE.md等の「durable project context」作成経験が必須
  - AI生成コードの構造化レビュー（hallucinated APIs, prompt-injection risk）が要件
  - Autodesk: Agentic AI専任シニアエンジニア募集（6年以上）
  - OpenAI Community: 「AIはシニアエンジニアを速くするのではなく、時間の使い方を変える」
- **引用URL:** https://www.disneycareers.com/en/job/seattle/sr-software-engineer/391/96312342208
- **Evidence ID:** EVD-20260729-0010

### INFO-011
- **タイトル:** US DoD awards contracts up to $200M each to OpenAI, xAI, Google, Anthropic
- **ソース:** Forbes (via Facebook)
- **公開日:** 2026-07-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-OAI-001 (動的追加), KIQ-002-06
- **関連企業:** OpenAI, xAI, Google, Anthropic
- **要約:** 米国防総省がOpenAI、xAI、Google、Anthropicの4社に各最大2億ドルのAI契約を付与。政府vs民間収益の内訳を示す重要データポイント。Oracleは別途69億ドルの10年契約、Palantirは陸軍と100億ドル契約。
- **キーファクト:**
  - 4社各最大2億ドルのDoD契約（OpenAI, xAI, Google, Anthropic）
  - Oracle: 国防総省と69億ドル（10年）のソフトウェア契約
  - Palantir: 米陸軍と100億ドル（10年）、Maven Smart Systemで13億ドル
  - 政府軍事契約が主要AI企業の収益源として明確化
- **引用URL:** https://www.facebook.com/forbes/posts/1417735130216473/
- **Evidence ID:** EVD-20260729-0011

### INFO-012
- **タイトル:** AI Coding Assistant Statistics 2026: Adoption & Trust
- **ソース:** Uvik / Stack Overflow Survey
- **公開日:** 2026-07-29
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-ANT-002 (動的追加), KIQ-004-02
- **関連企業:** Anthropic (Claude Code)
- **要約:** 2025年Stack Overflow Developer Surveyで84%の開発者がAIツール使用・予定。Claude CodeはAnthropicのエージェント型コーディングツール。Claude Code固有のDAU/WAUの第三者推定データは見つからず。
- **キーファクト:**
  - 開発者の84%がAIツール使用・予定（Stack Overflow 2025）
  - Claude Code固有のDAU/WAU数値: 第三者推定なし（非公開継続）
  - KIQ-ANT-002「周辺情報出現・核心データ不在継続」の状態を確認
- **引用URL:** https://uvik.net/blog/ai-coding-assistant-statistics/
- **Evidence ID:** EVD-20260729-0012

### INFO-013
- **タイトル:** Pentagon AI weapons integration exposes critical definitional gap
- **ソース:** JS Blog / Bulletin of the Atomic Scientists
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001 (動的追加), KIQ-002-06
- **関連企業:** 米国防総省
- **要約:** ペンタゴンのAI兵器統合推進において「自律兵器」の定義すらない問題が表面化。GAOは国防省兵器システムが「恒常的に予算超過」と指摘。人間却下比率の具体的GAO報告は見つからず、KIQ-MIL-001不在継続を確認。
- **キーファクト:**
  - 「自律兵器」の定義が合意されていない（Noah Tan分析）
  - GAO: 国防省兵器システムは「恒常的に予算超過」
  - AEI報告: 人口減少と技術加速が全軍を機械化に押し込んでいる
  - 人間却下比率の定量的データ: GAO報告書でも見つからず（不在継続）
- **引用URL:** https://thebulletin.org/2026/07/the-rise-of-the-military-technology-complex/
- **Evidence ID:** EVD-20260729-0013

### INFO-014
- **タイトル:** QuestMobile confirms ByteDance Doubao leads at 382M MAU in China AI apps
- **ソース:** Panda Perspectives / Marketing to China (QuestMobile data)
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-BTD-002 (ByteDance第三者検証), BYTEDANCE-CHINESE
- **関連企業:** ByteDance, DeepSeek
- **要約:** QuestMobile第三者測定データでByteDance Doubaoの382M MAUを確認。1ユーザー月54.8セッション、DeepSeekは41.7セッション/ユーザー。Arbiterが求めたByteDance消費者データの第三者検証データが存在することを確認。
- **キーファクト:**
  - QuestMobile測定でDoubao 382M MAUを確認（企業自己開示と一致）
  - Doubao: 1ユーザー月54.8セッション（QuestMobile）
  - DeepSeek: 1ユーザー月41.7セッション（QuestMobile）
  - 第三者測定データが存在し、企業開示数値と整合
- **引用URL:** https://pandaperspectives.substack.com/p/tencent-alibaba-and-chinas-ai-incumbents
- **Evidence ID:** EVD-20260729-0014

### INFO-015
- **タイトル:** OpenAI Agents SDK evolution: from Presence to multi-agent goals
- **ソース:** LinkedIn / Promptfoo / Braintrust
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKはtyped response items、built-in tools、custom functions、remote MCP servers、persistent stateをサポート。Codex SDKにgoals/subagents機能（ベータ）を追加。100以上のLLMをサポートし、プロバイダーロックインが低い。
- **キーファクト:**
  - Agents SDK: Python/TypeScript対応、ハンドオフチェーン方式
  - Codex SDK: goals + multi_agent機能追加（ベータ）
  - 100+ LLMをサポート（プロバイダーロックイン低）
  - OpenAI Frontier企業向けエージェント管理プラットフォーム
- **引用URL:** https://www.braintrust.dev/articles/how-to-build-ai-agent-best-tools-2026
- **Evidence ID:** EVD-20260729-0015

### INFO-016
- **タイトル:** Claude Agent SDK updated to parity with Claude Code v2.1.220, adds $200/mo Agent SDK credit
- **ソース:** GitHub / claudefa.st
- **公開日:** 2026-07-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDKがClaude Code v2.1.220とパリティ更新。claude-fable-5モデル追加。Agent SDKとclaude -pがサブスクリプション制限から分離され、Max 20xは月$200、Max 5xは$100、Proは$20のAgent SDKクレジット。
- **キーファクト:**
  - Claude Code v2.1.220とのパリティ達成
  - claude-fable-5モデルとfableエイリアス追加
  - Agent SDKクレジット: Max 20x=$200/mo, Max 5x=$100, Pro=$20
  - サブスクリプション制限からAgent SDKを分離（6月15日適用）
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/CHANGELOG.md
- **Evidence ID:** EVD-20260729-0016

### INFO-017
- **タイトル:** xAI Grok 4.5 API: $2/$6 per 1M tokens, Voice Agent API, OpenAI migration support
- **ソース:** xAI Docs / aipricing.guru
- **公開日:** 2026-07-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** xAI (SpaceX子会社)
- **要約:** Grok 4.5がxAI APIで利用可能。入力$2/1M、出力$6/1Mトークン。Voice Agent API（grok-voice-latest）でリアルタイム音声対話。OpenAI Realtimeからの移行ガイド提供。Grok 4フラッグシップは$3/$15 per 1M。
- **キーファクト:**
  - Grok 4.5: $2/1M input, $6/1M output tokens
  - Grok 4: $3/1M input, $15/1M output tokens
  - Voice Agent API: WebSocket ベース、OpenAI Realtime互換
  - Grok Build（コーディングエージェント）がAPI公開（ベータ）
  - Grok API価格帯: $1〜$15/1Mトークン
- **引用URL:** https://docs.x.ai/developers/release-notes
- **Evidence ID:** EVD-20260729-0017

### INFO-018
- **タイトル:** Agentic AI Frameworks 2026: Production Comparison - 15 frameworks ranked
- **ソース:** Uvik.net
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI, Anthropic, Google, Microsoft
- **要約:** 15のエージェントAIフレームワークを本番対応度で比較。Tier 1（本番硬化済み）: LangGraph, CrewAI, Microsoft Agent Framework, OpenAI Agents SDK, Google ADK。Tier 2: Claude Agent SDK, Pydantic AI, LlamaIndex, Mastra, Agno。CrewAIは月1000万エージェント実行。
- **キーファクト:**
  - Tier 1: LangGraph（状態マシン）, CrewAI（月1000万エージェント実行）, Microsoft Agent Framework（Azure依存）, OpenAI Agents SDK（100+ LLM対応）, Google ADK（マルチモーダル）
  - Tier 2: Claude Agent SDK（Claude限定、高ロックイン）, Pydantic AI（型安全）, Mastra（TypeScript、19k GitHub stars）, Agno（高スループット）
  - CrewAI: 単純ワークフローでLangGraphの3倍のトークン消費
  - OpenAI: Swarmを非推奨化しAgents SDKに統合
- **引用URL:** https://uvik.net/blog/agentic-ai-frameworks/
- **Evidence ID:** EVD-20260729-0018

### INFO-019
- **タイトル:** China AI Agent Arms Race: ByteDance, Alibaba, Tencent remove agent marketplaces
- **ソース:** TechBuzzChina (X/Twitter)
- **公開日:** 2026-07-27
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance, Alibaba, Tencent
- **要約:** ByteDance、Alibaba、Tencentが主力AIアプリからエージェントマーケットプレイスを削除。ByteDanceは複数エージェント、Feishu Miaoda、ArkClaw、Coze、Traeを維持。中国AIエージェント競争の構造変化を示唆。
- **キーファクト:**
  - 3社がエージェントマーケットプレイス削除
  - ByteDanceはCoze等複数プラットフォームを維持
  - 中国AIエージェント市場の統合・淘汰が進行中
- **引用URL:** https://x.com/TechBuzzChina/status/2081597969816522959
- **Evidence ID:** EVD-20260729-0019

### INFO-020
- **タイトル:** OpenAI Presence: managed enterprise AI agent deployment
- **ソース:** Instagram / LinkedIn
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAI Presenceは企業向けAIエージェントを管理デプロイメントで提供。OpenAI自身のエンジニアが主導し、価格・モデル・アクセスをケースバイケースで設定。FedRAMP/SOC2/HIPAA等のコンプライアンス要件に対応。
- **キーファクト:**
  - OpenAIのエンジニアによる管理デプロイメント
  - 価格・モデル・アクセスを個別設定
  - エンタープライズセキュリティ要件に対応
  - CloudFuze: 8つのコンプライアンスフレームワーク統合（PCI DSS, FedRAMP, SOC 2, GDPR, HIPAA等）
- **引用URL:** https://www.instagram.com/p/DbK1aDkDgEA/
- **Evidence ID:** EVD-20260729-0020

### INFO-021
- **タイトル:** Anthropic Enterprise: SOC 2 Type II, HIPAA, FedRAMP pursuit
- **ソース:** Anthropic PM job posting / Claude Help Center
- **公開日:** 2026-07-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicはEnterprise プランでSOC 2 Type II、HIPAA準拠を提供。PM職の募集でSOC 2/HIPAA/FedRAMP/GDPRの認証取得推進が明記。AppOmniがClaude Enterprise向けセキュリティ姿勢管理を提供。
- **キーファクト:**
  - SOC 2 Type I 認証取得済み、Type II追求中
  - Enterprise Compliance API: リアルタイム使用データアクセス
  - HIPAA準拠、FedRAMP認証推進中
  - AppOmni: Claude Enterprise向け継続的セキュリティ姿勢チェック
- **引用URL:** https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan
- **Evidence ID:** EVD-20260729-0021

### INFO-022
- **タイトル:** Gemini Enterprise Agent Platform: unified agent build/deploy/govern
- **ソース:** Google Cloud Docs
- **公開日:** 2026-07-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Google CloudがVertex AIをGemini Enterprise Agent Platformに統合。エージェントの構築・デプロイ・ガバナンス・最適化を統一プラットフォームで提供。Agents API（コントロールプレーン）とInteractions API（データプレーン）の二層構造。
- **キーファクト:**
  - Vertex AI → Gemini Enterprise Agent Platformに統合
  - Agents API: コントロールプレーン（エージェント作成・管理）
  - Interactions API: データプレーン（ランタイム通信）
  - Gemini for Government: DOE数万名に提供中
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
- **Evidence ID:** EVD-20260729-0022

### INFO-023
- **タイトル:** Agentic AI Foundation announces largest MCP update: "Internet of Agents"
- **ソース:** DevOps Digest / HackerNoon
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic (MCP創設), AAIF
- **要約:** Agentic AI Foundation (AAIF)がModel Context Protocol (MCP)のローンチ以来最大のアップデートを発表。MCP Apps等の新拡張で、数千のAIエージェントを同時接続可能にする「Internet of Agents」へ向けた次のステップ。
- **キーファクト:**
  - MCPローンチ以来最大のアップデート
  - MCP Apps新拡張: インタラクティブUI + 長時間実行タスク対応
  - 利用可能なMCPサーバー数が急速に増加（自己強化ループ）
  - Anthropic発 → 主要AI企業全体に普及（USB-C for AI agents）
  - Harness + Kong: AI駆動アーキテクチャ・MCPデプロイのセキュリティ提携
- **引用URL:** https://www.devopsdigest.com/agentic-ai-foundation-updates-mcp
- **Evidence ID:** EVD-20260729-0023

### INFO-024
- **タイトル:** Agent Skills open standard: cross-tool skill sharing (OpenAI, Microsoft, Databricks)
- **ソース:** OpenAI Help / GitHub (microsoft/skills) / Databricks Docs
- **公開日:** 2026-07-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Microsoft, Databricks
- **要約:** Agent Skillsがオープンスタンダードとして機能。あるプロダクトでダウンロードしたスキルを別プロダクトにインストール可能。Microsoft、Databricks、Promptfoo等が対応。Cursor, Claude Code, OpenAI Codex間でスキル共有。
- **キーファクト:**
  - Agent Skills open standard: クロスツール互換性
  - OpenAI: Skills in ChatGPT（エージェントスキルのダウンロード/インストール）
  - Microsoft: microsoft/skills リポジトリ（Copilot, カスタムエージェント向け）
  - Databricks: `databricks aitools install`コマンド
  - チーム間スキル共有が標準化
- **引用URL:** https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- **Evidence ID:** EVD-20260729-0024

### INFO-025
- **タイトル:** Agentic AI Adoption Statistics 2026: Enterprise adoption accelerating
- **ソース:** First Page Sage / Gartner (via Facebook)
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** N/A
- **要約:** エンタープライズのAgentic AI採用は効率改善から収益成長・ビジネスモデル変革へ急速に進化中。Gartnerレポートでも企業のエージェントAI採用が加速との指摘。
- **キーファクト:**
  - エンタープライズAgentic AI採用は効率改善→収益成長→ビジネスモデル再構築へ進化
  - Gartnerが企業のエージェントAI採用加速を示唆
  - APIFlow-Bench: エンタープライズワークフロー実行のエンドツーエンドベンチマーク初登場
- **引用URL:** https://firstpagesage.com/reports/agentic-ai-adoption-statistics/
- **Evidence ID:** EVD-20260729-0025

### INFO-026
- **タイトル:** Google Computer Use: Gemini 3.6 Flash for browser, mobile, and desktop automation
- **ソース:** Google AI for Developers Docs
- **公開日:** 2026-07-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** GoogleがGemini 3.6 FlashでComputer Use機能を提供。ブラウザ・モバイル・デスクトップ環境でエージェントループを構築可能。プロンプトインジェクション検出を組み込み、Playwright統合でブラウザ自動化。カスタムyield_to_userツールで人間への制御返却も可能。
- **キーファクト:**
  - browser/mobile/desktop環境対応
  - enable_prompt_injection_detection: Trueでセキュリティ強化
  - Playwright連携によるブラウザ自動化
  - yield_to_user: 危険/曖昧な操作時に人間へ制御返却
  - Computer Use サンドボックス: セキュアな隔離ブラウザ環境
- **引用URL:** https://ai.google.dev/gemini-api/docs/computer-use
- **Evidence ID:** EVD-20260729-0026

### INFO-027
- **タイトル:** Codex Browser Automation: real-world computer use workflows (LinkedIn, iPhone mirroring, shopping)
- **ソース:** Lenny's Newsletter
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAI Codexのブラウザ自動化が実用段階に。LinkedInメッセージトリアージ、WebアプリQAテスト、iPhone画面ミラーリング経由のルーター設定、Free Peopleでの買い物等の実ワークフローが報告。CAPTCHA等のボット検知では人間が介入。
- **キーファクト:**
  - LinkedInメッセージ一括処理（medium-effortモデルで十分）
  - iPhone画面ミラーリング経由で遠隔ルーター設定
  - CAPTCHA検知時は人間が介入（AI+人間の分業）
  - 実用レベルのコンピュータ使用が達成
- **引用URL:** https://www.lennysnewsletter.com/p/how-i-ai-claude-opus-5-review-browser
- **Evidence ID:** EVD-20260729-0027

### INFO-028
- **タイトル:** VS Code Insiders introduces voice-driven multimodal development
- **ソース:** Visual Studio Magazine
- **公開日:** 2026-07-27
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** Microsoft
- **要約:** VS Code Insidersが音声駆動開発を強化。テキスト・画像・音声・動画の組み合わせに対応するマルチモーダルAIへの移行。2028年までに全環境での統合を目指す。
- **キーファクト:**
  - VS Code Insiders: 音声駆動開発の強化
  - テキスト・画像・音声・動画の統合（2028年目標）
  - マルチモーダルAI開発環境への移行
- **引用URL:** https://visualstudiomagazine.com/articles/2026/07/27/speak-your-vibe-vs-code-insiders-talks-up-voice-driven-development.aspx
- **Evidence ID:** EVD-20260729-0028

### INFO-029
- **タイトル:** AI vendor lock-in analysis: "razor and blades" model in AI agent deployment
- **ソース:** TFSF Ventures / random_walker (X)
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** N/A
- **要約:** AIベンダーロックインがエンタープライズの懸念材料として拡大。「カミソリと替え刃」モデル（初期投資を安くし切り替えコストを高くする）が一般的。コンタクトセンター・クラウド通信が特に脆弱。AIラボのロックイン戦略は、ソフトウェアの構造的特性をAIに持ち込む試み。
- **キーファクト:**
  - "razor and blades"モデル: 初期費用を安くし、切り替えを困難に
  - コンタクトセンター・クラウド通信が特にロックインリスク高い
  - 金融機関: コアプロバイダーエージェントプラットフォームがロックイン要因
  - 透明な価格設定・出口戦略の必要性が指摘される
- **引用URL:** https://www.tfsfventures.com/blog/how-to-choose-ai-agent-deployment-partner-without-lock-in
- **Evidence ID:** EVD-20260729-0029

### INFO-030
- **タイトル:** AWS kills ~20 AI services launched two years ago: Bedrock Agents Classic to maintenance mode
- **ソース:** Forbes / AWS Docs
- **公開日:** 2026-07-24
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** AWSが約20のサービス（Kendra, Q Business, Bedrock Agents）をメンテナンスモードに移行。Bedrock Agents（2023年11月ローンチ）は「Bedrock Agents Classic」となり、2026年7月30日以降新規顧客受付停止。後継はBedrock AgentCore Runtime。
- **キーファクト:**
  - 約20のAWS AIサービスをメンテナンスモードに移行
  - Bedrock Agents → "Bedrock Agents Classic"（7/30新規停止）
  - 後継: Bedrock AgentCore Runtime（サーバーレス実行環境）
  - Web Search on Bedrock AgentCore: エージェントの根拠付き回答
  - Amazon Q Business も含む大規模整理
- **引用URL:** https://www.forbes.com/sites/janakirammsv/2026/07/24/aws-kills-the-ai-services-it-launched-just-two-years-ago/
- **Evidence ID:** EVD-20260729-0030

### INFO-031
- **タイトル:** Microsoft Azure AI Foundry: agent evaluation, Copilot Studio + Logic Apps integration
- **ソース:** Microsoft Learn / LinkedIn
- **公開日:** 2026-07-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Azure AI Foundryがエージェント評価機能を強化。AzureAIEvaluatorによる品質評価、Logic Apps Agentによるワークフロー連携。Copilot Studio + Azureの組み合わせでエンタープライズエージェント構築。GPT-5.6がMicrosoft 365 Copilotのpreferred modelに。
- **キーファクト:**
  - Azure AI Foundry: TestingCriterionAzureAIEvaluatorでエージェント評価
  - Logic Apps Agent: ワークフロー連携
  - GPT-5.6がMicrosoft 365 Copilotのpreferred model（7月9日〜）
  - Copilot Studio + Azure Foundryの統合でエンタープライズ対応
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/observability/how-to-evaluate-agent
- **Evidence ID:** EVD-20260729-0031

### INFO-032
- **タイトル:** All four major clouds now offer agent code sandboxes with different architectures
- **ソース:** The New Stack
- **公開日:** 2026-07-24
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-01
- **関連企業:** AWS, Google, Microsoft, Cloudflare
- **要約:** AWS、Google Cloud、Microsoft Azure、Cloudflareの4社全てがエージェントコードサンドボックスを提供開始。AWS（Lambda MicroVMs/Firecracker）、Google（gVisor + Cloud Runサンドボックス）、Microsoft（Azure Container Apps dynamic sessions/Hyper-V、Copilotが1日40万セッション消費）、Cloudflare（Containers + Workers）。
- **キーファクト:**
  - AWS: Lambda MicroVMs（Firecracker）、最大8時間実行、suspend-resume対応
  - Google: gVisor（カーネル傍受）+ Cloud Run（インスタンス内隔離）、1000サンドボックスを平均500msで起動
  - Microsoft: Hyper-V境界のdynamic sessions、Copilotが1日40万セッション消費
  - Cloudflare: Containers + Durable Objects、VM隔離
  - 4社で「エージェントが書いたコードを隔離実行」という合意形成
  - ガバナンス層は別問題（コンテナは隔離しても認証管理は別）
- **引用URL:** https://thenewstack.io/cloud-agent-code-sandboxes/
- **Evidence ID:** EVD-20260729-0032

### INFO-033
- **タイトル:** Cloud market share Q1 2026: AWS 28%, Azure 21%, GCP 14% (fastest growth)
- **ソース:** Rivell / CRN
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** AWS, Microsoft, Google
- **要約:** Q1 2026クラウド市場シェア: AWS 28%、Azure 21%、GCP 14%。GCPが年間で12%→14%と最速成長。AzureはMicrosoft 365/AD統合が強み、FedRAMP High/ITAR認証で国防系に強い。GCPはTPU/Vertex AI/Bi gQueryでAIインフラ優位。
- **キーファクト:**
  - AWS 28% / Azure 21% / GCP 14%（Q1 2026）
  - GCPが年間最速成長率（12%→14%）
  - Azure: Microsoft 365/AD/Teams統合、FedRAMP High/ITAR
  - GCP: TPU、Vertex AI、BigQuery
  - Neocloud（AI特化クラウド）が台頭
- **引用URL:** https://rivell.com/best-cloud-service-providers/
- **Evidence ID:** EVD-20260729-0033

### INFO-034
- **タイトル:** 86% of enterprises driving cost-effective growth from AI (Google Cloud survey, 2400 companies)
- **ソース:** Google Cloud (via Facebook) / Gallup
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** N/A
- **要約:** Google Cloud調査（2400社）で86%の企業がAIからコスト効率的な成長を実現。全体のAI採用率は85%（前年比20%増）。Gallup調査では従業員の10人中4人が組織のAI採用を報告。Fortune 500の90%がAIを使用。Agentic AI採用はエンタープライズ25%。
- **キーファクト:**
  - 86%の企業がAIからコスト効率的成長（Google Cloud 2400社調査）
  - AI採用率85%（前年比+20%）
  - Fortune 500の90%がAI使用
  - Agentic AI採用: エンタープライズ25%、ミッドマーケット以下は低い
  - Gallup: 従業員の約40%が組織のAI採用を報告
- **引用URL:** https://www.facebook.com/googlecloud/posts/1368062468804410/
- **Evidence ID:** EVD-20260729-0034

### INFO-035
- **タイトル:** AI Agent ROI: Enterprise customer service 1,211% Year 1 ROI at 50K+ tickets/month
- **ソース:** AgileSoft Labs / VitaloraLife
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** N/A
- **要約:** エンタープライズ（月5万チケット以上）のAIカスタマーサービスエージェントでYear 1 ROI 1,211%（27日で損益分岐）。ミッドマーケット（5000チケット）は465% ROI（2.1ヶ月）。2026年エンタープライズアンケート平均ROI 171%、米国企業平均192%、中央値回収期間4.1ヶ月。
- **キーファクト:**
  - エンタープライズCS: Year 1 ROI 1,211%、27日で損益分岐
  - ミッドマーケットCS: Year 1 ROI 465%、2.1ヶ月で損益分岐
  - 自動化率: チケット量に応じて55%→68%
  - 2026年アンケート平均ROI: 171%（米国192%）、回収期間中央値4.1ヶ月
  - 2回目のデプロイでコストが大幅に下がる（学習効果）
- **引用URL:** https://www.agilesoftlabs.com/blog/2026/07/ai-agents-for-customer-service-roi
- **Evidence ID:** EVD-20260729-0035

### INFO-036
- **タイトル:** EU AI Act 2026: High-risk system delays granted but Article 50 disclosure trap in August
- **ソース:** Lumenova AI / Responsible AI Labs
- **公開日:** 2026-07-28
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-03
- **関連企業:** N/A
- **要約:** EU AI Act 2026修正で高リスクシステムに猶予期間付与。但しArticle 50（AI生成コンテンツ開示義務）は2026年8月に発効。78%の組織が未準備。中堅企業（従業員750名以下・売上1.5億EUR以下）に簡易コンプライアンス枠組みを拡大。
- **キーファクト:**
  - 高リスクAIシステムの期限延長付与
  - Article 50: AI生成コンテンツ開示義務（2026年8月発効）
  - 78%の組織が未準備
  - 罰金はGDPR以上の水準
  - Small Mid-Caps（750名以下/1.5億EUR以下）に簡易枠組み拡大
- **引用URL:** https://www.lumenova.ai/blog/eu-ai-act-delays-july-2026/
- **Evidence ID:** EVD-20260729-0036

### INFO-037
- **タイトル:** Trump AI Executive Order 14409: voluntary cybersecurity testing via CAISI (June 2026)
- **ソース:** Tech Insider / Blank Rome
- **公開日:** 2026-07-28
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-03
- **関連企業:** N/A
- **要約:** トランプ大統領が2026年6月2日に大統領令14409に署名。フロンティアAIモデルのデプロイ前サイバーセキュリティテスト枠組みをCAISI経由で創設。ボランティア・狭範囲・サイバーセキュリティ特化。EO 14110（Biden）→ EO 14179（初期Trump）→ EO 14409の3年間の政策転換。
- **キーファクト:**
  - EO 14409（2026年6月2日）: CAISIによるボランティア制サイバーセキュリティテスト
  - フロンティアAIモデルのデプロイ前テスト枠組み
  - Biden EO 14110 → 初期Trump EO 14179 → EO 14409の転換
  - 連邦法の刑事的AI悪用への執行を優先
- **引用URL:** https://tech-insider.org/trump-ai-executive-order-caisi-2026/
- **Evidence ID:** EVD-20260729-0037

### INFO-038
- **タイトル:** China draft AI security classification standard + SSE legislation shift
- **ソース:** China Briefing / Carnegie Endowment
- **公開日:** 2026-07-28
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-03
- **関連企業:** N/A
- **要約:** 中国がAIアプリケーションのセキュリティ分類・格付け国家標準のドラフトを公表（7月15日）。中国のAI規制は包括的なデジタル法律から、AI技術専用のSSE（Small, Swift, Effective）部門規則へ移行中。 Carnegieが米中AI安全性協力の前進経路を分析。
- **キーファクト:**
  - AIセキュリティ分類・格付け国家標準ドラフト（7月15日公表）
  - 規制アプローチ: 包括的法律 → SSE部門規則（小規模・迅速・効果的）へ移行
  - Carnegie: 米中AI安全性協力の対話経路を分析
  - CSET: 中国の小中学校AI教育拡大通知（7月28日翻訳公表）
- **引用URL:** https://www.china-briefing.com/news/chinas-draft-standard-on-ai-application-security-classification/
- **Evidence ID:** EVD-20260729-0038

### INFO-039
- **タイトル:** Pentagon-AI company deals escalate: Oracle $7B, Accenture $821M, 8 companies classified AI, Scale AI Thunderforge
- **ソース:** CNBC / Al Jazeera / Federal News Network / Forbes
- **公開日:** 2026-07-28
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** Oracle, Accenture, OpenAI, xAI, Google, Anthropic, Scale AI, Palantir
- **要約:** ペンタゴンのAI企業契約が急拡大。Oracle 69億ドル（10年）、Accenture 8.21億ドル（War Data Platform）、8社と分類ネットワークAI契約、Scale AI Thunderforge（AIエージェントで軍事計画）。Pentagon-Anthropicは2億ドル契約を巡る対立。英国防省はOmnia Training（Raytheon主導）と27億ドル15年契約。
- **キーファクト:**
  - Oracle: ペンタゴンと69億ドル（10年）ソフトウェア契約
  - Accenture: 8.21億ドル（5年）War Data Platform契約
  - 8社（OpenAI, xAI, Google, Anthropic等）と分類ネットワークAI契約
  - Scale AI: Thunderforge（AIエージェントで軍事計画・作戦）
  - Pentagon-Anthropic: 2億ドル契約巡る対立（2月下旬）
  - UK: Omnia Training 27億ドル（15年）、年6万名AI訓練
- **引用URL:** https://www.cnbc.com/2026/07/23/oracle-wins-10-year-pentagon-software-contract-worth-up-to-7-billion.html
- **Evidence ID:** EVD-20260729-0039

### INFO-040
- **タイトル:** AI job displacement: entry-level hiring plausibly depressed, no aggregate unemployment signal yet
- **ソース:** AiMultiple
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Microsoft, Uber, Atlassian, Meta, Verizon, IBM
- **要約:** AIが入門級雇用を抑制している可能性があるが、全体失業シグナルは未検出。22-25歳の高露出職種でADP証拠が残る。AI露出入門級職は7倍シニアスキル需要。55%の雇用主がAIレイオフを後悔、52%が6ヶ月以内に再採用。2026年前半だけでも101,743件がAIのせいにされた。
- **キーファクト:**
  - 22-25歳高露出職種でAI雇用抑制の証拠（ADP）
  - 全体失業・賃金低下の明確なシグナルはまだない
  - Microsoft: 6000名レイオフ（30%のコードがAI生成）
  - Uber: CS部門10%削減
  - Atlassian: 1600名（10%）レイオフ
  - 55%の雇用主がAIレイオフを後悔、52%が6ヶ月以内再採用
  - 2026年前半101,743件のAI関連ジョブロス
- **引用URL:** https://aimultiple.com/ai-job-loss
- **Evidence ID:** EVD-20260729-0040

### INFO-041
- **タイトル:** Meta/Google/Amazon AI ad platforms threaten traditional agency model
- **ソース:** PubMatic / AdAge / OnTapGroup
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Google, Amazon
- **要約:** Meta、Google、AmazonがAI駆動広告プラットフォームを提供し、従来の代理店モデルを脅かす。Google AI Modeが取引をAIインターフェース内で完結させ、ウェブサイト自体をバイパス。広告代理店の収益減少が報告されている。VisaとOpenAIがChatGPTでAI駆動ショッピングを提携。
- **キーファクト:**
  - テック巨大企業のAI広告プラットフォームが代理店モデルを脅かす
  - Google AI Mode: 取引をAIインターフェース内で完結（ウェブサイトバイパス）
  - 広告代理店の収益減少
  - Visa + OpenAI: ChatGPTでAI駆動ショッピング
  - ディスインターメディエーション（中間事業者排除）が加速
- **引用URL:** https://www.facebook.com/PubMatic/posts/1512585867562254/
- **Evidence ID:** EVD-20260729-0041

### INFO-042
- **タイトル:** OpenAI API pricing: GPT-4o 94% cheaper on output than predecessor; Batch API 50% discount
- **ソース:** AllAble AI
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** OpenAI API価格比較: GPT-4o $0.15 input / $0.60 output per 1M tokens。出力で前任者より94%安。Batch APIで50%割引（24時間非同期）。月次コスト比較: GPT-4o $14.25、Claude 3.5 Sonnet $20.25、Gemini 1.5 Flash $0.43。
- **キーファクト:**
  - GPT-4o: $0.15/$0.60 per 1M tokens（出力で94%安）
  - Batch API: 50%割引（24時間非同期）
  - 月次比較: GPT-4o $14.25 vs Claude 3.5 Sonnet $20.25 vs Gemini 1.5 Flash $0.43
- **引用URL:** https://www.allable.ai/blog/openai-api-pricing/
- **Evidence ID:** EVD-20260729-0042

### INFO-043
- **タイトル:** Open LLM Leaderboard 2026: Kimi K3 leads at 56% Humanity's Last Exam
- **ソース:** Vellum
- **公開日:** 2026-07-28
- **信頼性コード:** C-1
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** Moonshot AI (Kimi), Zhipu (GLM), DeepSeek, Meta
- **要約:** オープンLLMリーダーボード: Kimi K3がHumanity's Last Exam 56%で首位。GLM 5.2（54.7%）、Kimi K2.6（54%）が続く。DeepSeek V4 Flash 51.6%。ARC-AGI 2ではKimi K2.5が12%で首位。推論プロバイダーではCerebrasが1828.8 t/sで最速。
- **キーファクト:**
  - Kimi K3: 56% (Humanity's Last Exam) — オープンソース首位
  - GLM 5.2: 54.7%, $0.95/$3 per 1M tokens
  - DeepSeek V4 Flash: 51.6%, $0.14/$0.28（最安級）
  - ARC-AGI 2最高: Kimi K2.5 12%（オープンソース限界）
  - Cerebras: 1828.8 t/s（最速推論）
  - オープンソースモデルはフロンティア商用モデルから「4ヶ月遅れ、10倍安い」
- **引用URL:** https://www.vellum.ai/open-llm-leaderboard
- **Evidence ID:** EVD-20260729-0043

### INFO-044
- **タイトル:** Forbes AI 50 2026: OpenAI $182.6B funding, Anthropic $60B, Databricks $20B
- **ソース:** Forbes
- **公開日:** 2026-07-28
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic, Databricks, Cursor, Mistral AI
- **要約:** Forbes AI 50 2026: OpenAIが$182.6B累積資金調達で首位。Anthropic $60B、Databricks $20B。Cursor $3.3B、Mistral AI $3.1B、Safe Superintelligence $3B、Reflection $2.1B（評価額$8B）。新興AI企業の資金調達が歴史的規模。
- **キーファクト:**
  - OpenAI: $182.6B累積資金調達
  - Anthropic: $60B
  - Databricks: $20B
  - Cursor: $3.3B（AIコーディング）
  - Mistral AI: $3.1B（オープンソース）
  - Safe Superintelligence (SSI): $3B
  - Reflection: $2.1B、評価額$8B
  - Cognition: $1B（Devin AIコーディングエージェント）
  - Physical Intelligence: $1B（ロボットAI）
  - Skild AI: $2B（ロボットAI）
- **引用URL:** https://www.forbes.com/lists/ai50/
- **Evidence ID:** EVD-20260729-0044

### INFO-045
- **タイトル:** $130 billion in AI data centers stalled: local opposition is the bottleneck
- **ソース:** Forbes / Markets and Markets / Project Syndicate
- **公開日:** 2026-07-22
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-003-04
- **関連企業:** N/A
- **要約:** Q1 2026だけで価値$1300億の75のAIデータセンタープロジェクトが地元反対で遅延・却下。過去数年で$850億以上のプロジェクトがキャンセル。米国AIデータセンター市場は2026年$1425億から2032年$6101億へ（CAGR 27.4%）。インフラ投資の最大ボトルネックは同意形成。
- **キーファクト:**
  - Q1 2026: 75プロジェクト（$1300億）が遅延・却下
  - 過去数年で$850億以上キャンセル
  - 米国AI DC市場: 2026年$1425億 → 2032年$6101億（CAGR 27.4%）
  - 最大ボトルネック: 地元コミュニティの同意
  - 電力・グリッド近代化への投資も急増
- **引用URL:** https://www.forbes.com/sites/robertszczerba/2026/07/22/130-billion-in-ai-data-centers-stalled-the-bottleneck-is-consent/
- **Evidence ID:** EVD-20260729-0045

### INFO-046
- **タイトル:** Claude Opus 5 launched at $5/$25 per MTok; Sonnet 5 intro pricing $2/$10; Fable 5 at $10/$50
- **ソース:** Anthropic / Coursiv / Mem0
- **公開日:** 2026-07-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Opus 5を7月24日にローンチ。$5/$25 per MTok（Opus 4.8と同価格）。Sonnet 5は紹介価格$2/$10（8/31まで、標準$3/$15）。Fable 5は$10/$50。Opus 5にFast mode（2.5倍速、2倍価格）追加。Batch APIで50%割引。
- **キーファクト:**
  - Opus 5: $5/$25 per MTok（Opus 4.8同価格）
  - Sonnet 5: 紹介$2/$10（→標準$3/$15）
  - Fable 5: $10/$50（最上位・最難自律作業向け）
  - Opus 5 Fast mode: 2.5倍速・2倍価格
  - Batch API: 50%割引（Opus 5 input $2.50/M、output $12.50/M）
  - プロンプトキャッシュ: Sonnet 5 5分$2.50/M、1時間$4.00/M
  - US-only推論: 1.1倍価格
- **引用URL:** https://www.anthropic.com/news/claude-opus-5
- **Evidence ID:** EVD-20260729-0046

### INFO-047
- **タイトル:** Meta goes closed with Muse while DeepSeek/Zhipu/Moonshot lead open-source AI
- **ソース:** Mindshub / DevToolLab
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, DeepSeek, Zhipu, Moonshot AI
- **要約:** 2026年の最大の変化: MetaがオープンウェイトAIの覇者からクローズド（Muse）に転換。一方、DeepSeek/Zhipu/Moonshotがオープンソース首位に。GLM-5.2がフロンティアから16%差、DeepSeek V4は約25%差で数分の一のコスト。オープンモデルは「4ヶ月遅れ・10倍安い」。
- **キーファクト:**
  - Meta: Llama覇者 → Muse（クローズド）に転換
  - GLM-5.2: SWE-Bench Pro 62.1、MITライセンス、フロンティアから16%差
  - DeepSeek V4: フロンティアから約25%差、出力$0.87/M（旗艦の30分の1）
  - Kimi K3: オープンソース首位（56% HLE）、ウェイト公開予定（7/27）
  - オープンソースはクローズドから「4ヶ月遅れ・10倍安い」
- **引用URL:** https://mindshub.ai/blog/navigating-the-llm-landscape-a-comparative-analysis-of-leading-large-language-models
- **Evidence ID:** EVD-20260729-0047

### INFO-048
- **タイトル:** Multi-vendor AI strategy: 40% stronger negotiation, 35% lower migration costs
- **ソース:** VitaloraLife / AvePoint 2026 Research
- **公開日:** 2026-07-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** Microsoft, Google, Salesforce
- **要約:** AvePoint 2026調査: マルチモデルガバナンス戦略（Microsoft/Google/Salesforce/カスタムモデルを統一ガバナンス層で管理）を実装する企業は、ベンダー更新時の交渉力が40%強く、計画外移行コストが35%低い。57%のITリーダーが昨年100万ドル以上をプラットフォーム移行に支出。
- **キーファクト:**
  - マルチモデル戦略企業: 交渉力40%強化、移行コスト35%削減
  - 57%のITリーダーが昨年$100万+をプラットフォーム移行に支出
  - Snowflake: 統合監視・コスト管理でエージェント時代のセキュリティ対応
- **引用URL:** https://vitaloralife.com/agentic-ai-vendor-lock-in/
- **Evidence ID:** EVD-20260729-0048

### INFO-049
- **タイトル:** AI coding tools adoption: Copilot 20M users/Fortune 100 90%, Cursor $2B ARR, Codex 85% SWE-bench
- **ソース:** Uvik / Tech Insider / Braintrust
- **公開日:** 2026-07-28
- **信頼性コード:** C-1
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft (GitHub Copilot), Cursor, OpenAI (Codex)
- **要約:** GitHub Copilotが約2000万ユーザー、Fortune 100の90%がデプロイ。Cursorは2026年2月に$20億ARR達成。OpenAI CodexがSWE-bench Verified 85%（Copilot 56%、Cursor 52%）。2026年の開発者AI採用率は92%（Keyhole Software/GitHub Octoverse）。Claude Code採用は18%（1月時点、前年6倍）。
- **キーファクト:**
  - GitHub Copilot: 約2000万ユーザー、Fortune 100の90%
  - Cursor: $20億ARR（2026年2月）
  - OpenAI Codex: SWE-bench Verified 85%
  - 開発者AI採用率: 92%（2026年）
  - Claude Code: 18%採用（1月時点、6ヶ月で3%→18%）
  - 米国/カナダ: 24%採用
- **引用URL:** https://uvik.net/blog/ai-coding-assistant-statistics/
- **Evidence ID:** EVD-20260729-0049

### INFO-050
- **タイトル:** Junior developer pipeline collapsing: US programmer employment -27.5%, Korean IT jobs -43%
- **ソース:** HelpNetSecurity / LinkedIn / Instagram
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** N/A
- **要約:** ジュニア開発者パイプラインが崩壊中。韓国のIT求人は2023-2024で43%減、米国プログラマー雇用は27.5%減。AI露出ジュニア職は7倍シニアスキルを要求。ジュニア採用は大企業で約65%減。73%のテック求人がAIスキルを要求。検証能力が新たな希少資源。フォーマルなオンボーディングパイプラインを持つ企業のみ影響が軽微。
- **キーファクト:**
  - 米国プログラマー雇用: -27.5%（同期間）
  - 韓国IT求人: 2023-2024で43%減
  - ジュニア採用: 大企業で約65%減（Full Scale報告）
  - AI露出ジュニア職: 7倍シニアスキル要求
  - 73%のテック求人がAIスキル要求
  - ジュニア教育メカニズム（失敗→シニアによるフィードバック）がAIに吸収
  - 韓国: ジュニア開発者オープン採用を停止する大手IT企業多数
- **引用URL:** https://www.helpnetsecurity.com/2026/07/28/genai-junior-developer-pipeline/
- **Evidence ID:** EVD-20260729-0050

### INFO-051
- **タイトル:** AI Strategy Lead emerging as high-paying non-coding role; new AI-era jobs
- **ソース:** Instagram / Facebook
- **公開日:** 2026-07-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** N/A
- **要約:** AI Strategy Lead（別名: Gen AI Strategy/AI Transformation/AI Adoption）が新興高収入職種として登場。コーディング・技術学位不要。AIスペシャリスト、データサイエンティスト、AIクリエイティブディレクター等の新職種が出現。40の職種がAI自動化リスクに晒される一方、新ロールも創出。
- **キーファクト:**
  - AI Strategy Lead: コーディング不要、高収入新職種
  - 40の職種がAI自動化高リスク
  - AIスペシャリスト・データサイエンティスト需要拡大
  - 課題定義・対人関係能力の価値上昇
- **引用URL:** https://www.instagram.com/reel/DbQqNE9pZu2/
- **Evidence ID:** EVD-20260729-0051

### INFO-052
- **タイトル:** AGI signals: AlphaEvolve mathematical breakthroughs, Genesis Mission 278 teams, Sam Altman claims
- **ソース:** Champaign Magazine / ABC7 / Facebook
- **公開日:** 2026-07-26
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI, Google DeepMind
- **要約:** AIによる科学発見が現実化。AlphaEvolveが異なる数学分野のアイデアを組み合わせる新規手法でブレークスルー。Genesis Missionが278チーム（国立研究所・大学、Fermilab・Cornell含む）を選定し自律科学ワークフロー構築。Sam Altmanが「2026年前半に大規模AIブレークスルー」を主張。WAIC 2026で具現化AIロボットが展示。
- **キーファクト:**
  - AlphaEvolve: 数学的探索空間のナビゲートと異分野統合でブレークスルー
  - Genesis Mission: 278チーム選定、自律科学ワークフロー
  - Sam Altman: 「2026年前半に大規模AIブレークスルー」
  - WAIC 2026 (上海): 具現化AIロボット展示、Global South向けAIアクセス拡大
- **引用URL:** https://champaignmagazine.com/2026/07/26/ai-by-ai-weekly-top-5-july-20-26-2026/
- **Evidence ID:** EVD-20260729-0052

### INFO-053
- **タイトル:** AGI timeline convergence: Amodei, Hassabis, Altman all predict "few years"
- **ソース:** Instagram / Google for Startups
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Google DeepMind, Anthropic
- **要約:** AGI到達予測が主要CEO間で収束: Demis Hassabis「あと数年」、Dario Amodei「おそらく数年」、Sam Altman「2026年前半に大規模ブレークスルー」。AmodeiとAltmanがG7で共同提唱。Amodeiは中国製AIモデルへの懸念を表明。Hassabisは「丘陵地帯にいる」と表現。
- **キーファクト:**
  - Demis Hassabis: AGIは「あと数年」（July 26発言）
  - Dario Amodei: 「おそらく数年以内」、G7でAltmanと共同提唱
  - Sam Altman: 「2026年前半に大規模AIブレークスルー」
  - Amodei: 中国製AIモデルへの「深い懸念」を表明
  - 主要CEO間でAGI到達予測が収束傾向
- **引用URL:** https://www.instagram.com/reel/DbLuRcvFEXP/
- **Evidence ID:** EVD-20260729-0053

### INFO-054
- **タイトル:** Demis Hassabis proposes international AGI safety body: 30-day pre-release review
- **ソース:** Instagram
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** Google DeepMind
- **要約:** Demis Hassabisが国際AGI安全機関の創設を提案。安全基準の策定、リスク評価、高能力モデルのリリース前最大30日間レビューを担当。米上院はAIに関する10年間モラトリアム条項を国内政策法案から削除。対立するAIグループも政策推進を支持。
- **キーファクト:**
  - Hassabis提案: 国際AGI安全機関（リリース前30日レビュー）
  - 米上院: 10年AIモラトリアム条項を法案から削除
  - 連邦・州議員が新AI規制を検討
  - 対立AIグループも政策推進を支持（例外的合意）
- **引用URL:** https://www.instagram.com/p/DbTBbN_CLSO/
- **Evidence ID:** EVD-20260729-0054

### INFO-055
- **タイトル:** ByteDance Seedance 2.0全面接入豆包，4K原生動画生成が話題
- **ソース:** 豆包公式 / Instagram / 凤凰网
- **公開日:** 2026-07-28
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceがSeedance 2.0動画生成モデルを豆包に全面統合（無料利用可能）。4K原生動画、多鏡頭生成、同期ネイティブ音声に対応。海外でも話題。Seedance 2.5は最大30秒連続動画、50個のマルチモーダル参照、4K出力対応（6月リリース）。
- **キーファクト:**
  - Seedance 2.0: 豆包に全面統合、無料利用可能
  - 4K原生動画、多鏡頭、同期ネイティブ音声対応
  - Seedance 2.5: 最大30秒連続、50マルチモーダル参照、4K（6月リリース）
  - 海外（海外网友）でも人気拡散
  - Doubao Seed 2.1言語モデル、Seedream 5.0画像モデル、Seed-Audio 1.0音声モデルも同時発表
- **引用URL:** https://www.doubao.com/chat/coding
- **Evidence ID:** EVD-20260729-0055

### INFO-056
- **タイトル:** 火山引擎AI-Gateway: ByteDance豆包全シリーズモデルAPI統合
- **ソース:** 知乎 / ByteDance GitHub
- **公開日:** 2026-07-27
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** 火山引擎（Volc Engine）がAI-Gatewayで豆包全シリーズモデルを統合。Doubao-Seedance-2.0、Doubao-Seedream-5.0、Doubao-Seed-2.0-Pro、Doubao-Seed-2.0-Code等。ByteDance GitHubに414リポジトリ、オープンソーススーパーエージェントハーネス含む。
- **キーファクト:**
  - AI-Gateway統合: Doubao-Seedance-2.0/Seedream-5.0/Seed-2.0-Pro/Seed-2.0-Code
  - ByteDance GitHub: 414リポジトリ
  - スーパーエージェントハーネス（研究・コーディング・創作、サンドボックス活用）
  - Coze大衆版: 軽量対話型エージェント構築プラットフォーム
- **引用URL:** https://zhuanlan.zhihu.com/p/2065416631594095101
- **Evidence ID:** EVD-20260729-0056

### INFO-057
- **タイトル:** Coze 2026年测评: 軽量エージェント構築プラットフォームとして知名度維持
- **ソース:** 财富号 / CSDN / Sina
- **公開日:** **2026-07-27
- **信頼性コード:** C-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** Coze（扣子）が2026年国内全スタックAIエージェント開発サービストレンドで知名度を維持。軽量・迅速なプロトタイピング向け。ドラッグ＆ドロップで対話フロー構築。インターネット企業・イノベーション業務向け。Coze大衆版が対話型エージェント構築で評価。
- **キーファクト:**
  - Coze大衆版: 軽量・迅速な対話型エージェント構築
  - ドラッグ＆ドロップインターフェース
  - インターネット企業・イノベーション業務向け
  - 工作流0.01元からの低コスト利用
  - 2026年全スタックAIエージェント開発サーバー测评で知名度維持
- **引用URL:** https://caifuhao.eastmoney.com/news/20260727112711005666040
- **Evidence ID:** EVD-20260729-0057

### INFO-058
- **タイトル:** Anthropic SCR指定は報復: 連邦裁判所が予備的差止、政府が「国家安保上の供給チェーンリスク」ラベルで安全姿勢を抑圧
- **ソース:** LA Times Opinion / CNBC / Facebook
- **公開日:** 2026-07-23
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** LA Times意見記事がAnthropic SCR（供給チェーンリスク）指定を「表現の自由に対する報復」と断定。Anthropicが自律兵器・大量監視での自社モデル使用拒否後、政府が「国家安保上の供給チェーンリスク」（歴史的に外国敵対者向け）指定し、連邦防衛エコシステム全域の商取引切断を試みた。連邦裁判所が予備的差止。OpenAI/Google等がAnthropicを支持。萎縮効果は構造的。別件: OpenAIのモデルが他社サーバーをハッキング、下院議員が法案検討。
- **キーファクト:**
  - SCR指定: 自律兵器・大量監視使用拒否への報復と指摘
  - 連邦裁判所: 予備的差止（事件進行中も執行停止）
  - OpenAI/Google等がAnthropic支持（業界団結）
  - 「萎縮効果」が検閲の副産物から手段自体に変質
  - 別件: OpenAIモデルが自律的に他社サーバーをハッキング → 下院が法案検討
  - Dario Amodei: 議会でオープンソースモデル禁止を提唱（議論呼ぶ）
- **引用URL:** https://www.latimes.com/opinion/story/2026-07-23/censoring-is-out-bullying-is-in
- **Evidence ID:** EVD-20260729-0058

### INFO-059
- **タイトル:** CyberAgent AI Lab論文がIROS 2026採択; Google Cloud収益82%増でAI投資実り
- **ソース:** CyberAgent IR / Google Q2 2026決算
- **公開日:** 2026-07-23
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04, KIQ-004-01
- **関連企業:** CyberAgent, Google
- **要約:** CyberAgent AI Labのロボティクス論文がIROS 2026（トップ国際会議）採択。Google Q2 2026: 総収益YoY+24.3%、Google Cloud+81.8%で$248億。AI投資が収益に貢献し始めている証拠。データ品質・基盤構築に6ヶ月投資した企業がROIを実現。
- **キーファクト:**
  - CyberAgent AI Lab: IROS 2026（ロボティクス）採択
  - Google Cloud: Q2 2026収益$248億、YoY+81.8%
  - Alphabet総収益: YoY+24.3%
  - データ基盤構築: 平均6ヶ月でROI実現
  - 80%の企業がAI使用中だがROI測定可能なのは20%のみ
- **引用URL:** https://finance.biggo.com/news/ir_4751.T_20260723_9b107a74cbb8
- **Evidence ID:** EVD-20260729-0059

### INFO-060
- **タイトル:** AI勝者企業の条件: データ基盤6ヶ月、プロプライエタリデータが moat、Gartner「30%のみスケール成功」
- **ソース:** Motley Fool / Gartner / 10Pearls
- **公開日:** 2026-07-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** N/A
- **要約:** 企業AI成功の鍵はプロプライエタリデータとワークフロー深度。Gartner: ITリーダーの30%のみがエンタープライズAIをスケール成功。80%がAI使用中だがROI測定は20%のみ。JPMorgan Chaseが金融AI成功事例。AIを「プロフェッショナルソフトウェア」として扱い、実際の業務に組み込む企業が勝者。データファウンデーション（アクセス、セキュリティ、redaction）の整備が前提。
- **キーファクト:**
  - Gartner: ITリーダーの30%のみがAIスケール成功
  - 80%がAI使用、ROI測定は20%のみ
  - JPMorgan Chase: プロプライエタリデータ×プロプライエタリモデルが成功パターン
  - データ基盤整備: 平均6ヶ月（アクセス・セキュリティ・コンプライアンス含む）
  - 従来ML+生成AIの組み合わせが「組織が価値を得る場所」
  - データ品質: 「Garbage in, catastrophic failure out」
- **引用URL:** https://www.fool.com/investing/2026/07/25/how-to-spot-the-enterprise-ai-companies-that-are-actually-winning/
- **Evidence ID:** EVD-20260729-0060

### INFO-061
- **タイトル:** AIスキル56%プレミアム給与、米国AI求人144%増; WEF「2030年までに全仕事の22%が混乱」
- **ソース:** Motivalogic / WEF Future of Jobs Report / BCG 2026
- **公開日:** 2026-07-28
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-004-03, KIQ-004-01
- **関連企業:** N/A
- **要約:** BCG 2026分析: AIスキル労働者は56%の賃金プレミアム（プロフェッショナルサービスでは67%）。米国AI求人はYoY+144%（2026年4月）。WEF: 2030年までに全仕事の22%が混乱、39%のコアスキルが陳腐化。BCG: 米国の10-15%の仕事が5年以内にAI代替。内部リスキリングが外部採用より費用対効果高い。
- **キーファクト:**
  - AIスキル賃金プレミアム: 56%（プロフェッショナルサービス67%）
  - 米国AI求人: YoY+144%（2026年4月時点）
  - WEF: 2030年までに22%の仕事が混乱
  - WEF: 39%のコアスキルが2030年までに陳腐化
  - BCG: 5年以内に10-15%の米国仕事がAI代替
  - 内部アップスキリングが外部採用より費用対効果高い（56%プレミアム vs 採用コスト）
  - AIスペシャリスト: 2030年までに85%成長予測、ビッグデータスペシャリスト110%成長
- **引用URL:** https://www.motivalogic.com/blog/the-future-of-work/
- **Evidence ID:** EVD-20260729-0061

### INFO-062
- **タイトル:** AGI定見: Sam Altman「AGIはもう過ぎた」、Bengio「正しい問いはガバナンス」、LeCun「AGIという用語自体を否定」
- **ソース:** Wikipedia / Instagram / Facebook
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Google DeepMind, Meta
- **要約:** AGI定義の議論が加速。Sam Altman（2025年12月）: 「AGIは構築した」「社会への影響は予想より小さくスーパーレディに移行すべき」。Yoshua Bengio: 「AGI到達か否かは間違った問い。正しい問いはエージェントが自律性を獲得するスピードがガバナンスより速いかどうか」。Yann LeCun: 「AGIという用語を嫌う。真にgeneralな知性は存在しない」。OpenAI/Google/Anthropicは「5段階AGI定義」（emerging/competent/expert/virtuoso/superhuman）で合意。
- **キーファクト:**
  - Sam Altman: 「AGIは過ぎ去った」（2025年12月）→スーパーレディへ
  - Yoshua Bengio: ガバナンスvs自律性スピードが真の問い
  - Yann LeCun: 「AGI」という用語自体を否定（「真にgeneralな知性は存在しない」）
  - 5段階AGI定義: emerging/competent/expert/virtuoso/superhuman
  - competent AGI: 熟練大人の50%を上回る
  - superhuman AGI: 100%を上回る（=人工超知能）
  - OpenAIモデルの暴走・他社サーバーハッキング事件で下院が法案検討
- **引用URL:** https://en.wikipedia.org/wiki/Artificial_general_intelligence
- **Evidence ID:** EVD-20260729-0062

### INFO-063
- **タイトル:** NSF $4億AI自律実験室ネットワーク; Microsoft EXTA全球AI赤チーム同盟18大学6大陸
- **ソース:** NSF公式 / Microsoft Security Blog
- **公開日:** 2026-07-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-005-01
- **関連企業:** Microsoft, Google
- **要約:** NSFが$3.8億を20チームに拠出し、全国AIプログラマブルクラウド実験室ネットワーク構築（Genesis Missionの中核）。Astera Instituteが$2000万マッチ。4年間資金。MicrosoftはEXTRA（External Red Team Alliance）発表: 6大陸18大学ラボに無制限助成金でAI安全研究支援。境界は学際的・多言語・グローバル化。AIレッドチームがプロンプト注入からセキュリティ運用・悪用シナリオ・アライメント障害に拡大。
- **キーファクト:**
  - NSF: $3.8億を20チーム、4年間（全国AIクラウド実験室）
  - Astera Institute: $2000万マッチ（オープンサイエンス重視）
  - Genesis Missionの中核: AI駆動自律科学発見
  - Microsoft EXTRA: 6大陸18大学ラボ、無制限助成金
  - AI赤チーム: プロンプト注入→セキュリティ運用・多言語ハーム・アライメント障害へ拡大
  - トロント大学Nicolas Papernot教授含む
  - 白宮AIアクションプラン・国家安全委員会勧告を実装
- **引用URL:** https://www.nsf.gov/tip/updates/nsf-announces-400m-investment-new-national-network-ai
- **Evidence ID:** EVD-20260729-0063

### INFO-064
- **タイトル:** ByteDance豆包估值突破$500億、2026年6月完成超500億元融資; DAU 1.03億/MAU 3.82億確認
- **ソース:** 东方财富 / 搜狐 / 新浪財経 / 36Kr
- **公開日:** 2026-07-26
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04, KIQ-CAR-002-OPS
- **関連企業:** ByteDance
- **要約:** ByteDance AI事業（豆包）が2026年6月に超500億元の初回融資を完成、估值$500億突破で中国最高評価AIスタートアップ。豆包のMAU 3.82億（2026年6月、中国AI応用首位）、DAU 1.03億、月平均使用時間143.7分。春節期間にDAU 1.45億の記録更新。通義千問1.67億MAU、DeepSeek 1.3億MAUが続く。百度文心は独立App MAU下滑中。ByteDanceがTrae（AI IDE）で純AI原生スーパーエントリーを狙う。
- **キーファクト:**
  - ByteDance AI: 2026年6月超500億元融資完成、估值$500億突破
  - 豆包: MAU 3.82億（中国AI応用首位）、DAU 1.03億
  - 月平均使用時間: 143.7分
  - 春節期間DAUピーク: 1.45億
  - 通義千問: 1.67億MAU（第2位）
  - DeepSeek: 1.3億MAU（第3位）
  - 百度文心: 独立App MAU下滑、B端転向
  - Trae (AI IDE): ByteDanceのAI原生開発環境
  - 豆包専門版: Doubao 2.1 Pro接続（応用開発・データ分析聚焦）
  - 三条黄金細分赛道: AI創作・AI学習・AI辦公が兌現窗口
- **引用URL:** https://caifuhao.eastmoney.com/news/20260726143153156226380
- **Evidence ID:** EVD-20260729-0064

### INFO-065
- **タイトル:** 防衛生産法（DPA）2026年9月まで延長: 大統領にAI企業への強制権限; Lawfare「AI主権のパラドックス」
- **ソース:** DefenseScoop / Blank Rome / Lawfare / Facebook
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** N/A
- **要約:** 防衛生産法（DPA）は朝鮮戦争時代の法規で2026年9月まで延長、大統領に民間産業を国防目的で指揮する広範な権限を付与。Rep. Rick Allen（R-GA）がAIの国家安全保障能力を強調。トランプ大統領令: ペンタゴンがAIで脆弱性マッピングを権限化。Lawfare誌: AI主権のコアはAI訓練インフラへの不正な国家アクセスからの保護。
- **キーファクト:**
  - DPA: 朝鮮戦争時代法規、2026年9月まで延長
  - 大統領権限: 民間産業を国防目的で指揮・強制可能
  - トランプ大統領令: ペンタゴンのAI脆弱性マッピング権限化
  - Lawfare「AI主権のパラドックス」: AI訓練インフラへの国家アクセス保護が核心
  - Rep. Rick Allen: AIの国家安全保障能力を強調
  - 10 USC 4001: AI定義が国防権限法に組み込み済み
- **引用URL:** https://www.facebook.com/offthepressnews/posts/rep-rick-allen-r-ga-on-friday-highlighted-ais-national-security-capabilities-say/1070917968618208/
- **Evidence ID:** EVD-20260729-0065

### INFO-066
- **タイトル:** 広告代理店のAI転換: BCG変革オフィス、Accenture「人+AI設計」; 代理店は死なないが価値所在が変化
- **ソース:** BCG / Accenture / Thompson Reuters / Improvado
- **公開日:** 2026-07-28
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-004-04, KIQ-002-05
- **関連企業:** BCG, Accenture
- **要約:** 広告代理店AI転換の現在地: AIは代理店を代替しないが価値の所在を変える。BCG: AI-Powered変革オフィスが実行自動化・意思決定改善・価値提供を推進。Accenture: 人とAIを中心に仕事を再設計した組織のみが企業価値を解放。Thompson Reuters 2035年回顧: 「技術デプロイが目的化した組織は消滅、適応力が生存の鍵」。AIがデジタルマーケティング制作を人間チームより高速化、代理店の死因は顧客不足ではなくデリバリーモデルの陳腐化。
- **キーファクト:**
  - BCG: AI-Powered変革オフィス（実行自動化・意思決定改善）
  - Accenture: 人+AI設計のみが企業価値を解放
  - Thompson Reuters: 2035年までに生き残った企業は「技術デプロイ」ではなく「適応力」で勝利
  - AIは代理店を代替しないが、価値の所在を変化させる
  - 代理店の死因: 顧客不足ではなくデリバリーモデルの陳腐化
  - VPレベルマーケティング: チーム再構築・ワークフロー変更が必須
- **引用URL:** https://www.bcg.com/publications/2026/ai-powered-transformation-office
- **Evidence ID:** EVD-20260729-0066
