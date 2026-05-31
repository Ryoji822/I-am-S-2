# 収集データ: 2026-05-31

## メタデータ
- 収集日時: 2026-05-31 00:00 UTC
- 完了日時: 2026-05-31 (Phase 1完了)
- 品質フラグ: NORMAL
- 総INFO数: 58件
- Evidence ID範囲: EVD-20260531-0001〜EVD-20260531-0058
- 実行クエリ数: 約130（collection_plan 110+動的5+補強15）
- スクレイプ数: 約25（公式ブログ12+詳細記事13）
- KIQカバー率: 28/28（23基本+5動的=100%）
- 信頼性コード分布: A-1:約8件、A-2:約10件、A-3:約5件、B-2:約25件、B-3:約3件、C-3:約7件
- 主要発見: Anthropic $65B Series H/$965B評価額、Mythos一般公開、Karpathy入社、Claude 78%デザイナー採用、Microsoft/Uber Claude Code予算超過、Stanford 22-25歳16%雇用減

## 動的追加クエリ（Arbiter Step 1.5）
- KIQ-ANT-SAFETY: Anthropic安全性選択理由の定量確認（2クエリ）
- KIQ-GOO-SHARE: Google Cloud AI寄与の定量分解（1クエリ）
- KIQ-ANT-SDK: Claude Code SDK利用比率（1クエリ）
- KIQ-GOV-CHILL: SCR指定後の安全性政策変化（1クエリ）

## 収集結果

### INFO-001
- **タイトル:** Anthropic Agents for Financial Services - 10の金融エージェントテンプレート発表
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Anthropicが金融サービス向けに10のエージェントテンプレート（ピッチビルダー、KYCスクリーナー、月末決済等）を発表。Claude Cowork/Claude CodeプラグインおよびManaged Agentsクックブックとして提供。Microsoft 365統合（Excel/PowerPoint/Word/Outlook）も追加。8つの新コネクタ（D&B、Moody's MCP app等）も発表。
- **キーファクト:**
  - Claude Opus 4.7がVals AI Finance Agent benchmarkで64.37%で業界首位
  - Citadel、FIS、BNY、Carlyle、Mizuho、Travelers等の金融機関がClaude導入
  - 100%のWalleye Capital従業員（400名）がClaude Code使用
  - Moody'sがMCP appをローンチ（6億社以上の信用データ統合）
- **引用URL:** https://www.anthropic.com/news/finance-agents
- **Evidence ID:** EVD-20260531-0001

### INFO-002
- **タイトル:** KPMGがAnthropicとグローバル提携、276,000人以上にClaude導入
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** KPMGがAnthropicとグローバル提携を発表。Digital Gateway（Azure基盤）にClaude Cowork/Managed Agentsを統合。全276,000人以上の従業員にClaudeアクセス提供。プライベートエクイティ向け優先パートナー指定。
- **キーファクト:**
  - KPMG 276,000人以上がClaudeアクセス可能（138カ国・地域）
  - Digital Gateway（Microsoft Azure基盤）にClaude統合
  - KPMG Blaze（PE向け）がClaude CodeでレガシーIT近代化を加速
  - UT Austinとの共同研究で「人間の役割」の定量的評価を実施
- **引用URL:** https://www.anthropic.com/news/anthropic-kpmg
- **Evidence ID:** EVD-20260531-0002

### INFO-003
- **タイトル:** OpenAI Rosalind Biodefense - バイオ防御プログラム発表
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-29
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** OpenAIがRosalind Biodefenseプログラムを発表。信頼できる開発者にGPT-Rosalindアクセスを提供し、バイオ防御・パンデミック準備アプリケーション構築を支援。米政府・同盟パートナーへの信頼できるアクセス拡大。Lawrence Livermore National Lab、Johns Hopkins APL、CEPIとの協力。
- **キーファクト:**
  - GPT-Rosalind（生命科学向けフロンティア推論モデル）の信頼できるアクセス拡大
  - Fourth Eon BiosecurityがAIネイティブスクリーニングインフラ構築
  - LLNLがAI×スパコンで医療対抗措置設計評価を加速
  - CEPIが100 Days Mission（ワクチン開発加速）でGPT-Rosalind活用
- **引用URL:** https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/
- **Evidence ID:** EVD-20260531-0003

### INFO-004
- **タイトル:** CiscoとOpenAIがCodexでエンタープライズエンジニアリングを再定義
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-004-02
- **関連企業:** OpenAI
- **要約:** CiscoがCodexを広範に導入し、AIネイティブ開発をエンタープライズソフトウェア構築の中核に。AI Defenseの新機能95%以上をCodexが作成。欠陥解決スループット10-15倍向上、月間1,500エンジニアリング時間節約。
- **キーファクト:**
  - 新AI機能の95%以上がCodexで作成
  - 欠陥解決スループット10-15倍向上（Codex CLI使用）
  - 月間1,500+エンジニアリング時間節約
  - ビルド時間約20%削減（15リポジトリ横断最適化）
  - DaybreakイニシアチブでGPT-5.5-Cyberモデルにアクセス
- **引用URL:** https://openai.com/index/cisco/
- **Evidence ID:** EVD-20260531-0004

### INFO-005
- **タイトル:** GPT-5.5 Instant Update + o3/GPT-4.5モデル退役
- **ソース:** OpenAI Help Center
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.5 Instantを更新（応答スタイル・品質改善）。canvas機能を段階的に廃止し、チャットレスポンス内のwriting/code blocksに移行。o3は2026年8月26日、GPT-4.5は2026年6月27日にChatGPTから退役。
- **キーファクト:**
  - GPT-5.5 Instant更新: より自然な会話、実用的なタスク改善
  - o3: 90日サンセット期間後、2026-08-26 ChatGPTから退役
  - GPT-4.5: 30日サンセット期間後、2026-06-27 ChatGPTから退役
  - APIへの変更はなし
- **引用URL:** https://help.openai.com/en/articles/9624314-model-release-notes
- **Evidence ID:** EVD-20260531-0005

### INFO-006
- **タイトル:** xAI Grok Build - ターミナル動作するコーディングエージェントCLI発表
- **ソース:** xAI公式ブログ
- **公開日:** 2026-05-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI
- **要約:** xAIがGrok Build（アーリーベータ）を発表。ターミナル上で動作するコーディングエージェント。プランレビュー・承認フロー、並列サブエージェント、AGENTS.md/MCP/プラグイン互換、ヘッドレスモード(-p)対応。SuperGrok/X Premium Plus加入者向け。
- **キーファクト:**
  - プランモード: タスク実行前にプランをレビュー・修正可能
  - 並列サブエージェント: 大規模タスクを並列分散処理
  - AGENTS.md、プラグイン、フック、スキル、MCPサーバー互換
  - ヘッドレスモード(-p)でスクリプト・自動化内で実行可能
  - ACP（Agent Communication Protocol）サポート
- **引用URL:** https://x.ai/news/grok-build-cli
- **Evidence ID:** EVD-20260531-0006

### INFO-007
- **タイトル:** Google I/O 2026 - Gemini Omni & Gemini 3.5 Flash発表
- **ソース:** Google公式ブログ
- **公開日:** 2026-05-29
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-05
- **関連企業:** Google
- **要約:** Google I/O 2026でGemini Omni（任意入力から高品質動画生成・会話型編集）とGemini 3.5 Flash（フロンティア性能+エージェント行動）を発表。Antigravityハーネスでマルチステップワークフロー実行。Search内でのジェネレーティブUI、情報エージェント等の新機能。
- **キーファクト:**
  - Gemini Omni: 画像/音声/動画/テキスト入力から高品質動画生成、会話型編集対応
  - Gemini 3.5 Flash: エージェント・コーディングでフロンティア性能、Antigravity統合
  - Gemini Spark: 24/7パーソナルAIエージェント、Workspace統合
  - Information Agents: Search内で24/7動作する情報エージェント
  - Gemini Omni Flash: YouTube Shorts/YouTube Create Appで無料ロールアウト
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-3-5-videos/
- **Evidence ID:** EVD-20260531-0007

### INFO-008
- **タイトル:** Google I/O 2026 主要12発表 - Search Agent、Neural Expressive、SynthID拡大
- **ソース:** Google公式ブログ
- **公開日:** 2026-05-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-005-03
- **関連企業:** Google
- **要約:** Google I/O 2026の主要12発表をまとめた記事。Gemini Omni/3.5 Flash、Search内情報エージェント、AntigravityジェネレーティブUI、Daily Brief、Universal Cart、Neural Expressive、Gemini Spark、macOSアプリ、Android XRインテリジェント眼鏡、SynthID拡大（OpenAI/Kakao/ElevenLabs採用）、Gemini for Science等。
- **キーファクト:**
  - SynthID: 1000億以上の画像/動画、6万年分の音声にウォーターマーク付与済み
  - OpenAI、Kakao、ElevenLabsがSynthID採用
  - AI content detection APIをGoogle Cloudでローンチ
  - Gemini 3.5 Proは内部利用中、来月ロールアウト予定
  - Android XR: 音声グラス（今秋）とディスプレイグラスの2種類発表
- **引用URL:** https://blog.google/innovation-and-ai/technology/ai/io-2026-keynote-moment-videos/
- **Evidence ID:** EVD-20260531-0008

### INFO-009
- **タイトル:** Anthropic安全性企業選択理由 - セキュリティ統合とエンタープライズCopilot首位
- **ソース:** AI CERTs / coesecurity.com
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-ANT-SAFETY, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがエンタープライズAIセキュリティで28の新統合を発表。RampデータでClaudeがOpenAIを逆転し企業利用で首位に。AICerts調査で企業CopilotカテゴリでClaudeがリード。BankInfoSecurityで「Top Gun」評価。88%のエンタープライズがAIセキュリティギャップに直面。
- **キーファクト:**
  - ClaudeがRampデータで企業利用シェア首位（OpenAI逆転）
  - Anthropic 28新Claude統合でエンタープライズセキュリティ強化
  - 88%のエンタープライズがAIセキュリティギャップに直面（okoone調査）
  - Claude Opus 4.5/4.8はプロンプトインジェクション耐性でフロンティアモデル最高
- **引用URL:** https://www.aicerts.ai/news/enterprise-copilots-why-claude-now-leads-corporate-adoption/
- **Evidence ID:** EVD-20260531-0009

### INFO-010
- **タイトル:** クラウドシェア比較 2026 Q1 - AWS 30%, Azure 25%, GCP 13%
- **ソース:** Usage.ai
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-GOO-SHARE, KIQ-002-01
- **関連企業:** Google, Microsoft, Amazon
- **要約:** 2026年Q1クラウドインフラシェア: AWS 30%、Azure 25%、GCP 13%（Synergy Research）。AWS EBITマージン213bps改善（QoQ）、Azureマージン低下。Amazon $2000億capex計画。Microsoft AI business $370億ARR。Google Cloud 63%成長。
- **キーファクト:**
  - クラウドシェア: AWS 30%, Azure 25%, GCP 13%（Q1 2026）
  - AWS EBITマージン213bps改善（Claude販売寄与）
  - Microsoft AI business: $370億ARR
  - Google Cloud: 63%成長、$200億ランレート
  - Amazon: 2026年capex $2000億計画
- **引用URL:** https://www.usage.ai/blogs/top-cloud-service-providers-2026/
- **Evidence ID:** EVD-20260531-0010

### INFO-011
- **タイトル:** Claude AI統計 2026 - エンタープライズシェア29%、利用の52%が拡張型
- **ソース:** SeoProfy
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-ANT-SDK, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude AI統計: エンタープライズAIアシスタント市場シェア29%、利用の52%が拡張型（augmentation-based）、34%がコンピュータ・数学タスク。Claude Code/Coworkの企業導入が加速。
- **キーファクト:**
  - エンタープライズAIアシスタント市場シェア: 29%
  - 利用の52%が拡張型（augmentation-based）
  - 34%がコンピュータ・数学タスク
- **引用URL:** https://seoprofy.com/blog/claude-ai-statistics/
- **Evidence ID:** EVD-20260531-0011

### INFO-012
- **タイトル:** ペンタゴンが8社とAI機密契約 - SCR後の安全性政策変化
- **ソース:** Instagram/Facebook (Reuters引用)
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-GOV-CHILL, KIQ-002-06
- **関連企業:** OpenAI, Google, Microsoft, Amazon, xAI, Anthropic
- **要約:** ペンタゴンがOpenAI、Google、Microsoft、Amazon、Nvidia、xAI、Reflectionと新たな機密AI契約を締結。米政府がAI企業に安全性プロトコル緩和を要求（大規模監視のため）。Anthropicの安全性制限がホワイトハウスのAI調達テンプレートになる。
- **キーファクト:**
  - ペンタゴンが8社（Google、OpenAI等）と機密AI契約
  - 米政府がAI企業に安全性プロトコル緩和を要求（市民監視のため）
  - Anthropicの安全性制限がホワイトハウス調達テンプレートに
  - Chris Olah（Anthropic共同創業者）がAI開発に関する発言
- **引用URL:** https://www.instagram.com/p/DYzqecbMtZC/
- **Evidence ID:** EVD-20260531-0012

### INFO-013
- **タイトル:** Claude Agent SDK更新 - 動的ワークフロー・並列エージェント機能
- **ソース:** GitHub (anthropics/claude-code)
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Claude Codeに動的ワークフロー機能が追加。数十〜数百のエージェントをバックグラウンドで並列実行可能に。Claude Agent SDK v0.3.150でSessionStart hooksのreloadSkills機能を追加。Netlify AI GatewayでClaude Opus 4.8が利用可能に。
- **キーファクト:**
  - Claude Code動的ワークフロー: 数十〜数百エージェントの並列実行
  - Claude Agent SDK v0.3.150リリース
  - Claude Opus 4.8がNetlify AI Gateway/Agent Runnersで利用可能
- **引用URL:** https://github.com/anthropics/claude-code/releases
- **Evidence ID:** EVD-20260531-0013

### INFO-014
- **タイトル:** Google Interactions API / Gemini Enterprise Agent Platform概要
- **ソース:** Google AI for Developers / Google Cloud Docs
- **公開日:** 2026-05-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Google
- **要約:** Google Interactions API（Beta）がネイティブサーバーサイド履歴、バックグラウンドタスク、エージェントワークフローを提供。Gemini Enterprise Agent Platformが企業向けエージェント構築・管理プラットフォーム。Skill Registry、RAG Engine等の機能含む。
- **キーファクト:**
  - Interactions API: ネイティブ履歴管理、バックグラウンドタスク
  - Gemini Enterprise Agent Platform: 構築・スケール・ガバナンス
  - Skill Registry: セキュアなスキル管理リポジトリ
- **引用URL:** https://ai.google.dev/gemini-api/docs/interactions-overview
- **Evidence ID:** EVD-20260531-0014

### INFO-015
- **タイトル:** AAIF（Agentic AI Foundation）が43新メンバー追加
- **ソース:** AAIF公式
- **公開日:** 2026-05-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** その他
- **要約:** Agentic AI Foundationが43の新メンバーを追加。エンタープライズ・政府のオープンエージェント標準採用が加速。
- **キーファクト:**
  - AAIF 43新メンバー追加（2026-05-18）
  - エンタープライズ・政府でのオープンエージェント標準採用加速
- **引用URL:** https://aaif.io/author/aaif/
- **Evidence ID:** EVD-20260531-0015

### INFO-016
- **タイトル:** Agent Skills (SKILL.md) - 0から40,000への爆発的成長
- **ソース:** Firecrawl Blog
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** その他
- **要約:** Agent Skills（SKILL.md）が0から40,000以上に急増。再利用可能な専門知識パッケージとして、Codex、Claude Code、Pi等のAIコーディングエージェント間でポータブル。OpenAI Skills、Claude Code Marketplace、LobeHub Skills Marketplace等のエコシステムが形成。
- **キーファクト:**
  - SKILL.mdが40,000+に成長（20日間で）
  - 複数エージェント間でポータブルなスキル仕様
  - GitHub Codex CLI、Claude Code、Gemini CLI等で対応
- **引用URL:** https://www.firecrawl.dev/blog/agent-skills
- **Evidence ID:** EVD-20260531-0016

### INFO-017
- **タイトル:** Workday-Google Cloud提携拡大 / Snowflake-AWS $60億契約
- **ソース:** Workday IR / Snowflake Press Release
- **公開日:** 2026-05-27
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** Google, Amazon
- **要約:** WorkdayとGoogle Cloudが戦略的提携拡大、HR・財務向けAIエージェント統合。SnowflakeがAWSと$60億の5年契約、エンタープライズAgentic AI採用加速。Parloa $3.5億Series DでEpic統合（医療AIエージェント）。
- **キーファクト:**
  - Workday × Google Cloud: HR・財務AIエージェント統合
  - Snowflake × AWS: $60億5年契約、Agentic AI加速
  - Parloa $3.5億Series D、Epic HIPAA準拠AIエージェント
- **引用URL:** https://www.snowflake.com/en/news/press-releases/snowflake-expands-aws-collaboration-with-6b-commitment-to-accelerate-enterprise-agentic-ai-adoption/
- **Evidence ID:** EVD-20260531-0017

### INFO-018
- **タイトル:** EYがエンタープライズ規模Agentic AI OS構築
- **ソース:** EY
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** その他
- **要約:** EYがGenAIの成果をグローバルAgentic AIプラットフォームに統合。人々の働き方を変革し、クライアントのAI大規模導入を加速。
- **キーファクト:**
  - EYグローバルAgentic AIプラットフォーム構築
  - GenAI成果を統合したエンタープライズ規模OS
- **引用URL:** https://www.ey.com/en_fi/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system
- **Evidence ID:** EVD-20260531-0018

### INFO-019
- **タイトル:** Infor調査: 49%のエンタープライズがAI初期段階で停滞
- **ソース:** Infor / Portalerp
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** その他
- **要約:** Infor調査で49%のエンタープライズがAI初期段階（パイロット）で停滞。31%が自律エージェントによる重要業務実行に不快感。49%のAI生成インサイトが行動に移されず。Writer調査では79%の組織がAI採用で課題（2025年から2桁増加）。
- **キーファクト:**
  - 49%がAI初期段階で停滞（Infor調査）
  - 31%が自律エージェントの重要業務実行に不快感
  - 79%の組織がAI採用で課題（Writer 2026調査）
  - IBM: 85%がAI使用可能だが25%のみ実際に使用
- **引用URL:** https://portalerp.com/noticia/infor-survey-finds-49-of-enterprises-are-stuck-in-early-stage-ai-pilots-despite-80-believing-they-have-the-capability-to-implement
- **Evidence ID:** EVD-20260531-0019

### INFO-020
- **タイトル:** Gartner予測: 2026年末に40%のエンタープライズアプリがAIエージェント搭載
- **ソース:** LinkedIn (Gartner引用)
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** その他
- **要約:** Gartner予測: 2026年末に40%のエンタープライズアプリがタスク特化AIエージェントを内蔵（2024年<5%から）。Fortune 500各社でAIエージェント15個未満、2028年までに150,000へ10,000倍増加予測。
- **キーファクト:**
  - 2026年末: 40%のエンタープライズアプリにAIエージェント（Gartner）
  - Fortune 500: 現在15未満→2028年150,000（10,000倍増）
  - 13%のみがエージェント管理に自信あり
- **引用URL:** https://www.linkedin.com/pulse/40-enterprise-apps-run-ai-agents-year-end-agentic-bartek-kotlarczyk-uv5fe
- **Evidence ID:** EVD-20260531-0020

### INFO-021
- **タイトル:** Fortune: 「Tokenmaxxing」終焉 - ROIで見るAI投資の現実
- **ソース:** Fortune
- **公開日:** 2026-05-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** Amazon
- **要約:** Fortune記事で「Tokenmaxxing」の非現実性を指摘。Amazonで一部従業員が無意味なタスクでAIエージェントを使用しトークン使用量を維持。$1のAIトークン支出で$0.18のユーザー価値しか生成されていない（Goldman Sachs推定）。
- **キーファクト:**
  - Amazon従業員が無意味タスクでトークン使用量維持
  - $1 AI支出→$0.18ユーザー価値（Goldman Sachs）
  - $0.44はAI導入バグ修正、$0.27は手直しに消費
- **引用URL:** https://fortune.com/2026/05/28/tokenmaxxing-is-dead-companies-didnt-get-the-roi-from-ai-they-wanted-to-see/
- **Evidence ID:** EVD-20260531-0021

### INFO-022
- **タイトル:** トランプ大統領がAI大統領令を撤回 - テック業界からの圧力
- **ソース:** MSNBC / CNBC
- **公開日:** 2026-05-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** その他
- **要約:** トランプ大統領がAI安全性審査制度の大統領令署名を直前で撤回。テック大手からの反発が背景。White House CTO Ethan KleinがCNBCでAI戦略を説明。
- **キーファクト:**
  - AI安全性大統領令を署名直前で撤回
  - テック業界からの反発が原因
  - White House CTO Ethan KleinがAI戦略説明
- **引用URL:** https://www.cnbc.com/video/2026/05/29/white-house-cto-ethan-klien-on-white-houses-ai-ambitions.html
- **Evidence ID:** EVD-20260531-0022

### INFO-023
- **タイトル:** Anthropic SCR指定 - 供給連鎖リスク指定とNSA $90億取引の同時進行
- **ソース:** The Next Web / Reuters
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-CHILL
- **関連企業:** Anthropic
- **要約:** ペンタゴンがAnthropicを供給連鎖リスクに指定（自律武器・大規模監視へのClaude使用拒否が理由）と同時に、米諜報機関が$90億規模の取引を準備。Anthropic v. Department of War訴訟で連邦裁判所が政府全体禁止命令をブロック。37名のAI専門家が「寒蝉効果」を記述した法廷意見書提出。
- **キーファクト:**
  - ペンタゴンAnthropic供給連鎖リスク指定（2026年3月）
  - NSA等が同時に$90億規模の取引準備
  - 裁判所が政府全体禁止命令をブロック
  - 37名AI専門家が寒蝉効果法廷意見書提出
- **引用URL:** https://thenextweb.com/news/us-government-chip-shortage-anthropic-nsa-9-billion
- **Evidence ID:** EVD-20260531-0023

### INFO-024
- **タイトル:** EU AI Act執行開始 - 企業のコンプライアンス対応加速
- **ソース:** Sovy / Salt Security / Archer
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** その他
- **要約:** EU AI Actの執行が開始。ハイリスクAIシステムのコンプライアンス要件が具体化。「SOC 2 for AI agents」が調達要件になりつつある（Reddit議論）。Digital Omnibusで中小企業への exempt措置拡大。
- **キーファクト:**
  - EU AI Act執行開始、4段階リスク分類
  - 「SOC 2 for AI agents」が調達要件化
  - Digital Omnibus: 中小中堅企業への exempt措置
- **引用URL:** https://www.sovy.com/blog/eu-ai-act-enforcement-date/
- **Evidence ID:** EVD-20260531-0024

### INFO-025
- **タイトル:** AI関連レイオフ加速 - 14社がAI要因で人員削減
- **ソース:** Business Insider / LA Times
- **公開日:** 2026-05-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** その他
- **要約:** AI駆動の人員削減が加速。Snap、Coinbase、Wix、Groupon（最大400名削減）等14社がAI要因のレイオフを実施。経済学者は「AIは雇用喪失を限定的に抑えつつ採用を抑制」と分析。
- **キーファクト:**
  - 14社がAI要因のレイオフ（Snap、Coinbase、Wix、Groupon等）
  - Groupon: 最大400名削減（AI再構築計画）
  - AIは採用抑制を通じて労働市場に影響（経済学者分析）
- **引用URL:** https://www.latimes.com/business/story/2026-05-29/another-tech-company-says-it-will-cut-hundreds-of-jobs-amid-pivot-to-ai
- **Evidence ID:** EVD-20260531-0025

### INFO-026
- **タイトル:** Klarna - AIで50%人員削減も人材再雇用、Duolingoも採用削減
- **ソース:** Instagram / Fortune / Entrepreneur
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** その他
- **要約:** Klarnaが4年間で50%人員削減（AI採用）、2023年に700名CS担当をAIアシスタントで代替。Q3 2025で$6000万節約も、一部人材を再雇用。45%のチケットを「deflect」したが実際に解決したのは14%のみ（Gartner測定）。Duolingoも新規採用30%削減。
- **キーファクト:**
  - Klarna: 4年間で50%人員削減（AI自動化）
  - $6000万節約→一部人材再雇用
  - チケットdeflect 45% / 実際解決14%（Gartner）
  - Duolingo: 新規採用30%削減
- **引用URL:** https://employerbranding.news/the-efficiency-trap-ai-the-jevons-paradox-and-the-future-of-the-human-workforce/
- **Evidence ID:** EVD-20260531-0026

### INFO-027
- **タイトル:** Google Marketing LiveでAI広告フォーマット発表 - 非媒介化リスクに対応
- **ソース:** Proactive Investors
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google
- **要約:** GoogleがMarketing LiveでAI搭載広告フォーマット発表。ChatGPT約9億ユーザーによるAI非媒介化リスクに対応。ZuckerbergがMeta $1250億AI投資の明確な防御を提示。Third PointのAI破壊的投資リスク・リポジショニング分析。
- **キーファクト:**
  - Google AI広告フォーマット発表（Marketing Live）
  - ChatGPT 9億ユーザーによる非媒介化リスク対応
  - Meta $1250億AI投資（Zuckerberg防御）
- **引用URL:** https://www.proactiveinvestors.com/companies/news/1092827/google-rolls-out-ai-powered-ad-formats-at-marketing-live-1092827.html
- **Evidence ID:** EVD-20260531-0027

### INFO-028
- **タイトル:** OpenAI価格体系再考 - Codex価格改定、ChatGPT無制限プラン見直し
- **ソース:** OpenAI Help Center / AOL / Finout
- **公開日:** 2026-05-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIがCodex価格をAPIトークン使用量ベースに変更（2026年4月2日、メッセージ単位から）。Sam AltmanがChatGPT無制限プランの見直しを示唆。Web Search $10/1K呼び出し、GitHub Copilot新AIC課金で$28→$746に跳ね上がる例。
- **キーファクト:**
  - Codex価格: メッセージ単位→トークン使用量ベース（4/2変更）
  - ChatGPT無制限プラン見直し検討（Altman発言）
  - GitHub Copilot新AIC課金: $28→$746（ユーザー報告）
- **引用URL:** https://www.aol.com/articles/openai-rethinking-chatgpt-pricing-unlimited-143826922.html
- **Evidence ID:** EVD-20260531-0028

### INFO-029
- **タイトル:** AIベンチマーク飽和 - MMLU 88%以上がフロンティア全滅
- **ソース:** Kili Technology / Codesota
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** その他
- **要約:** MMLU/MMLU-Proが88%以上で機能的に飽和、トップ差が統計的に無意味。SWE-bench Verified 70%超がPro公開セットでは23%に急落。ARC-AGI: Claude Opus 4が99.7%（ARC Easy）。GPT-5.4 ProがARC-AGI-2で83.3%。LLM benchmark leaderboard 2026でGPT-5.5、Claude Opus、Gemini、DeepSeek比較。
- **キーファクト:**
  - MMLU 88%+でフロンティア全社が飽和
  - SWE-bench Verified→Pro公開セットで70%→23%に急落
  - ARC Easy: Claude Opus 4 99.7%
  - ARC-AGI-2: GPT-5.4 Pro 83.3%（Gemini 3.1 Pro 84.6%に近接）
- **引用URL:** https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough
- **Evidence ID:** EVD-20260531-0029

### INFO-030
- **タイトル:** Anthropic $650億Series H - $9650億評価額でOpenAI逆転
- **ソース:** CNBC / WSJ / Yahoo Finance
- **公開日:** 2026-05-28
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Anthropicが$650億Series H調達、評価額$9650億でOpenAI（$8520億）を逆転し最も価値あるAIスタートアップに。Altimeter Capital、Dragoneer、Greenoaks、Sequoia Capitalがリード。Crunchbaseで最大の資金調達ラウンド。
- **キーファクト:**
  - $650億Series H調達
  - $9650億評価額（OpenAI $8520億超え）
  - Altimeter Capital、Dragoneer、Greenoaks、Sequoia Capitalリード
  - 史上最大の資金調達ラウンド（Crunchbase）
- **引用URL:** https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html
- **Evidence ID:** EVD-20260531-0030

### INFO-031
- **タイトル:** DeepSeek V4 - SWE-bench 80.6%でフロンティアに肉薄
- **ソース:** VentureBeat / DeepSeek.ai
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 ProがSWE-bench Verified 80.6%で西側フロンティアモデルにほぼ匹敵。急進的なアーキテクチャでシリコンバレーのトークンモットを破壊。1Tパラメータ、Qwen3.7 Max等との比較レーダーも公開。
- **キーファクト:**
  - DeepSeek V4 Pro: SWE-bench Verified 80.6%
  - 1Tパラメータモデル
  - 急進的アーキテクチャでコスト優位性
- **引用URL:** https://venturebeat.com/infrastructure/how-deepseeks-radical-architecture-is-shattering-silicon-valleys-token-moat
- **Evidence ID:** EVD-20260531-0031

### INFO-032
- **タイトル:** Claude Opus 4.8リリース - 価格据え置き、3倍安いFast Mode
- **ソース:** Anthropic / VentureBeat / Finout
- **公開日:** 2026-05-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Opus 4.8リリース。API価格据え置き（$5/100万入力、$25/100万出力）。Fast Modeは3倍安い$10/$40。claude.ai、Claude Code、API、Coworkで即時利用可能。アライメント・安全性評価で向上。
- **キーファクト:**
  - Opus 4.8: 価格据え置き $5/$25（100万トークンあたり）
  - Fast Mode: $10/$40（3倍安い）
  - コーディング・エージェント的タスク・プロフェッショナル業務で性能向上
- **引用URL:** https://www.anthropic.com/news/claude-opus-4-8
- **Evidence ID:** EVD-20260531-0032

### INFO-033
- **タイトル:** Hassabis AGI予測を2029年に前倒し - 3〜4年以内
- **ソース:** Sherwood News / Reddit / India Today
- **公開日:** 2026-05-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google
- **要約:** Google DeepMind CEO Demis HassabisがAGI到達予測を2029年に短縮（従来2030〜2035）。Google I/Oで発表。最も積極的なフロンティアラボCEOの公的予測。Altman、Amodeiの対応が注目される。
- **キーファクト:**
  - Hassabis: AGI 2029年可能性（従来2030〜2035から前倒し）
  - 最も積極的なフロンティアラボCEO予測
  - AIエージェントの急速進展が理由
- **引用URL:** https://sherwood.news/tech/google-deepminds-hassabis-agi-is-3-to-4-years-away/
- **Evidence ID:** EVD-20260531-0033

### INFO-034
- **タイトル:** RSIが新しいAGI指標に - TechCrunch分析
- **ソース:** TechCrunch
- **公開日:** 2026-05-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** その他
- **要約:** Recursive Self-Improvement（RSI）がAGIに代わる新指標として議論。研究者は「破滅的再帰AIシステムはまだ存在しない」点で合意。DeepMind研究リーダーOriol Vinyals「今日のAIは数年前の基準ならAGIだったかも」。
- **キーファクト:**
  - RSI（Recursive Self-Improvement）が新AGI指標
  - 研究者合意: 破滅的再帰AIはまだ存在せず
  - DeepMind Vinyals: 「今日のAIは数年前の基準ならAGI」
- **引用URL:** https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/
- **Evidence ID:** EVD-20260531-0034

### INFO-035
- **タイトル:** オープンモデルはフロンティアから8-10ヶ月遅れ - LessWrong分析
- **ソース:** LessWrong
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** その他
- **要約:** プライベートベンチマーク（公開データなし）で、オープンモデルはクローズドフロンティアから約8-10ヶ月遅れ。閉鎖モデル最良でもMUSEベンチマーク19-21%に対しオープンは3-4%。Llama 4 Scout/MaverickがGPT-5.5と比較されるがベンチマークデータ不足。
- **キーファクト:**
  - オープンモデル: フロンティアから8-10ヶ月遅れ（プライベートベンチマーク）
  - MUSE: 閉鎖19-21% vs オープン3-4%
  - Llama 4 Scout/Maverick vs GPT-5.5比較データ不足
- **引用URL:** https://www.lesswrong.com/posts/rJcCrXyEsJKmmDpWG/how-far-behind-are-open-models
- **Evidence ID:** EVD-20260531-0035

### INFO-036
- **タイトル:** Google $400億テキサスDC投資が本格始動
- **ソース:** KTXS / Yahoo Finance
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Google
- **要約:** Googleが2025年11月発表の$400億テキサスデータセンター投資が本格始動。地元の反響大きい。PIMCO分析でAIインフラブームは長期的投資機会。Nvidiaが$7250億AIインフラ投資の最大恩恵銘柄。
- **キーファクト:**
  - Google $400億テキサスDC投資本格始動
  - $7250億AIインフラ投資（Nvidia最大恩恵）
  - PIMCO: DC・電力・チップ構築が長期投資機会
- **引用URL:** https://ktxs.com/news/local/its-jarring-googles-40-billion-data-center-investment-to-transform-texas-town
- **Evidence ID:** EVD-20260531-0036

### INFO-037
- **タイトル:** CyberAgent AI展開加速 - ChatGPT Enterprise/Codex導入
- **ソース:** Instagram / SimplyWall.st
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-04, KIQ-004-01
- **関連企業:** その他
- **要約:** CyberAgentがChatGPT Enterprise/Codex導入でAI展開時間を半減。広告・メディア・ゲームチームで活用。2026年通期ガイダンス: 売上8800億円、営業利益500億円。AI Shift子会社が企業向けAI自動化ソリューション提供。
- **キーファクト:**
  - CyberAgent: ChatGPT Enterprise/CodexでAI展開半減
  - FY2026ガイダンス: 売上8800億円、営業利益500億円
  - AI Shift子会社がCS・マーケティング・営業自動化
- **引用URL:** https://www.instagram.com/p/DY3h0q-kQ9C/
- **Evidence ID:** EVD-20260531-0037

### INFO-038
- **タイトル:** オープンソースエージェントツールキット 2026 - ベンダーロックイン分析
- **ソース:** Medium (Data Science Collective)
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** その他
- **要約:** ベンダーSDK（Claude Agent SDK、OpenAI Agents SDK、Google ADK）がオーケストレーション摩擦を減らす一方、プロバイダーにロックイン。Codex vs Claude Code 2026比較。NVIDIA OpenShellがセキュア実行環境提供。GitHubがMCPツールプルーニングでトークンコスト62%削減。
- **キーファクト:**
  - ベンダーSDK: 摩擦減→ロックイン増
  - Codex vs Claude Code: アーキテクチャ・価格・ガバナンス比較
  - GitHub: MCP最適化でトークンコスト62%削減
  - NVIDIA OpenShell: セキュアコード実行環境
- **引用URL:** https://medium.com/data-science-collective/the-open-source-agent-toolkit-in-2026-da66dda36c9b
- **Evidence ID:** EVD-20260531-0038

### INFO-039
- **タイトル:** マルチモーダルベンチマーク - Gemini 3 Pro Deep Thinkが首位
- **ソース:** BenchLM
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google
- **要約:** マルチモーダル・グラウンデッドベンチマーク2026でGemini 3 Pro Deep Thinkが加重スコア100%で暫定首位。Grok 4.1が97.8%で追走。MMMU、OfficeQA、CharXiv等の複合指標。
- **キーファクト:**
  - Gemini 3 Pro Deep Think: マルチモーダル加重100%
  - Grok 4.1: 97.8%
  - MMMU、OfficeQA、CharXiv等の複合評価
- **引用URL:** https://benchlm.ai/multimodal-grounded
- **Evidence ID:** EVD-20260531-0039

### INFO-040
- **タイトル:** AIトークンコスト危機 - Goldman Sachs推定24倍増
- **ソース:** Tom's Hardware / TechFlowPost
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-002-02
- **関連企業:** その他
- **要約:** Goldman Sachs推定: Agentic AIでトークン需要が数年内に24倍増。AI推論コストはトークン価格低下にもかかわらず増加（エージェント使用量増大）。$1 AI支出→$0.18価値、$0.44バグ修正。
- **キーファクト:**
  - Agentic AIでトークン需要24倍増予測（Goldman Sachs）
  - トークン価格低下≠コスト低下（使用量増大）
  - $1支出→$0.18価値（残りはバグ修正・手直し）
- **引用URL:** https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-costs-begin-to-bite-as-agents-may-increase-token-demand-by-24-times-says-goldman-sachs-report-uber-and-microsoft-among-companies-feeling-the-bite-of-tokenized-billing
- **Evidence ID:** EVD-20260531-0040

### INFO-041
- **タイトル:** Snowflake × AWS $60億契約 - エンタープライズAgentic AI加速
- **ソース:** TechCrunch / Snowflake / Yahoo Finance
- **公開日:** 2026-05-27
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-01, KIQ-003-04
- **関連企業:** Amazon
- **要約:** SnowflakeがAWSと5年$60億のインフラ契約。Agentic AI導入加速のためのチップ確保が目的。Snowflake史上最大の契約。TechCrunch「Amazonに朗報、Nvidia牽制」。
- **キーファクト:**
  - $60億5年契約（Snowflake史上最大）
  - Agentic AI向けチップ確保
  - Nvidia牽制の意味合い
- **引用URL:** https://techcrunch.com/2026/05/27/in-more-good-news-for-amazon-snowflake-signs-6b-deal-with-aws-for-ai-cpu-chips/
- **Evidence ID:** EVD-20260531-0041

### INFO-042
- **タイトル:** Dario AmodeiのAI安全性姿勢の変遷 2021-2026
- **ソース:** StartupHub AI
- **公開日:** 2026-05-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Dario Amodeiの安全性姿勢変遷追跡。2025年6月に州レベルAI規制10年モラトリアム上院案に批判的意見。GDP 5%成長予測。AltmanとAmodei両者がAI雇用破壊警告を後退しつつある。
- **キーファクト:**
  - Amodei: 州レベルAI規制モラトリアムに反対（2025年6月）
  - GDP 5%成長予測
  - Altman/Amodei両者: 雇用破壊警告を後退
- **引用URL:** https://www.startuphub.ai/ai-news/ai-figures/2026/figure-dario-amodei-public-position-evolution-2026-05-28
- **Evidence ID:** EVD-20260531-0042

### INFO-043
- **タイトル:** Anthropic v. Department of War - 裁判所が政府全体禁止命令ブロック
- **ソース:** RiefKohl Law
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-CHILL
- **関連企業:** Anthropic
- **要約:** Anthropic対戦争省訴訟で裁判所が政府全体禁止命令をブロック。37名AI専門家が寒蝉効果法廷意見書。因果関係の第3要件で政府側に不利な判断。Anthropicが勝訴すれば全AI企業に軍事契約倫理的拒否の法的先例。
- **キーファクト:**
  - 裁判所が政府全体禁止命令ブロック
  - 37名AI専門家の寒蝉効果意見書
  - 因果関係要件で政府側不利
  - 勝訴時: 倫理的軍事拒否の法的先例確立
- **引用URL:** https://www.riefkohllaw.com/blog/anthropic-v-department-of-war-preliminary-injunction
- **Evidence ID:** EVD-20260531-0043

### INFO-044
- **タイトル:** Axios: CEOがAI安価モデルに乗り換え加速
- **ソース:** Axios
- **公開日:** 2026-05-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-002-02
- **関連企業:** その他
- **要約:** 企業がAI使用量増大でIT予算超過、ROI未確立の中で安価なモデルへのシフト加速。トークンコスト危機がエージェント利用で深刻化。
- **キーファクト:**
  - 企業: 安価なAIモデルへのシフト加速
  - IT予算超過 + ROI未確立
  - エージェント利用でコスト深刻化
- **引用URL:** https://www.axios.com/2026/05/29/ceos-ai-cheaper-tokens
- **Evidence ID:** EVD-20260531-0044

### INFO-045
- **タイトル:** ペンタゴン8社AI機密契約 - Anthropic SCR指定と同時進行
- **ソース:** Reddit / X (Twitter)
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Google, Microsoft, Amazon, xAI, Anthropic
- **要約:** ペンタゴンがOpenAI、Google、Microsoft、Amazon、Nvidia、xAI、Reflectionと新AI機密契約。Anthropicは供給連鎖リスク指定を受けながらも諜報機関と$90億取引を準備。OpenAI契約は「全合法目的」に使用可能で自律武器・大量監視のみ禁止。
- **キーファクト:**
  - 8社ペンタゴン機密AI契約
  - Anthropic: SCR指定 + 諜報$90億取引の二面性
  - OpenAI: 「全合法目的」許可（自律武器・監視のみ禁止）
- **引用URL:** https://www.reddit.com/r/Anthropic/comments/1tm26tb/trump_administration_and_anthropic_finalizing/
- **Evidence ID:** EVD-20260531-0045

### INFO-046
- **タイトル:** AIエージェントのマーケティング導入率12%未満
- **ソース:** Neil Patel
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-002-04
- **関連企業:** その他
- **要約:** AIエージェントのマーケティング導入率が全企業規模で12%未満。PwCがAgentic Marketing Console発表。MartechプラットフォームのAIエージェント対応力不足が指摘。
- **キーファクト:**
  - AIエージェントマーケティング導入率: 12%未満
  - PwC Agentic Marketing Console発表
  - MartechのAIエージェント対応力不足
- **引用URL:** https://neilpatel.com/marketing-stats/ai-agent-adoption/
- **Evidence ID:** EVD-20260531-0046

### INFO-047
- **タイトル:** UN AI治理対話開始 / 米議会AI法案協議
- **ソース:** CFR / Politico
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** その他
- **要約:** 国連のAI治理グローバル対話が開始。欧米議員交流（TTX）。Politico: 米下院議員Trahan/Obernolte間でAI法案協議、カリフォルニア等の州法を先取する連邦法可能性。
- **キーファクト:**
  - 国連AI治理グローバル対話開始
  - 欧米AI規制交流（TTX）
  - 米下院: 連邦AI法案協議（州法先取の可能性）
- **引用URL:** https://www.cfr.org/articles/the-world-is-trying-to-govern-ai-the-un-wants-in
- **Evidence ID:** EVD-20260531-0047

### INFO-048
- **タイトル:** AI新職種 - Gen AI Creative Director / AI Strategy Director登場
- **ソース:** LinkedIn / Orange.com
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** その他
- **要約:** AI需要が245%増（2025年）。新職種としてGen AI Creative Director（Brandtech Group）、AI & Strategy Director（A+E Networks）等が登場。AI人材需要の多様化。
- **キーファクト:**
  - AI人材需要245%増（2025年）
  - Gen AI Creative Director職登場
  - AI & Strategy Director等の新役職
- **引用URL:** https://www.orange.com/en/whats-up/ai-jobs-2026-skills-training-and-career-opportunities
- **Evidence ID:** EVD-20260531-0048

### INFO-049
- **タイトル:** IBM 2026 CEO研究: 85%がAI使用可能、25%のみ使用
- **ソース:** MindStudio
- **公開日:** 2026-05-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** その他
- **要約:** IBM 2026 CEO研究: 61ポイントの採用ギャップ（85%使用可能 vs 25%実際使用）。投資浪費・未実現ROI。39%のスキルセットが2030年までに陳腐化予測。
- **キーファクト:**
  - 85%使用可能 vs 25%実際使用（61ptギャップ）
  - 39%スキルセットが2030年までに陳腐化
- **引用URL:** https://www.mindstudio.ai/blog/ai-adoption-gap-ibm-2026-study/
- **Evidence ID:** EVD-20260531-0049

### INFO-050
- **タイトル:** AI自律武器・軍事倫理論争 - Anthropic拒否vs OpenAI許容
- **ソース:** Stefan Bauschard / Yahoo News
- **公開日:** 2026-05-30
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** ペンタゴンは企業による自律武器使用制限を軍事的権限への侵害と見なす。Anthropicが倫理的拒否の法的先例確立を目指す一方、OpenAI契約は「全合法目的」を許可。Shield AI（元Navy SEAL CEO）が自律性の道徳的問題に直面。
- **キーファクト:**
  - ペンタゴン: 企業制限を軍事的権限侵害と認識
  - Anthropic: 倫理的拒否の法的先例確立狙い
  - OpenAI: 「全合法目的」許可（自律武器のみ禁止）
- **引用URL:** https://stefanbauschard.substack.com/p/students-debate-lethal-autonomous
- **Evidence ID:** EVD-20260531-0050

### INFO-051
- **タイトル:** Anthropic Mythosモデルの一般公開決定 - Project Glasswing限定から全顧客へ
- **ソース:** Forbes (Ron Schmelzer)
- **公開日:** 2026-05-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-ANT-SAFETY, KIQ-001-01, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Anthropicがサイバーセキュリティ特化AIモデル「Claude Mythos」を全顧客に向けて一般公開する方針に転換。当初は安全性懸念からProject Glasswing（Amazon/Microsoft/Apple等の限定プログラム）内のみで提供。Cloudflareの評価ではMythosはエクスプロイトチェーンを自律構築できる能力を持ち、安全性拒否が一貫していなかった。Anthropicは「より良いサイバーセーフガードが準備できた」として一般公開を判断。
- **キーファクト:**
  - Mythos: ソフトウェア脆弱性発見・エクスプロイト構築・攻撃経路推論が可能
  - Cloudflare評価: 同一タスクでも異なるフレーミングで拒否/許可が不整合
  - AWSが自社重要コードベースでMythosテスト実施済み
  - Microsoft CTI-REALMベンチマークで大幅改善確認
  - Anthropic以前は一般公開予定なし→方針転換
- **引用URL:** https://www.forbes.com/sites/ronschmelzer/2026/05/29/anthropics-guarded-mythos-model-is-headed-for-wider-release/
- **Evidence ID:** EVD-20260531-0051

### INFO-052
- **タイトル:** KarpathyがAnthropic入社、91%デザイナーがAI週次利用、ClaudeがChatGPT逆転
- **ソース:** Eidos Design / Designer Fund / Ramp
- **公開日:** 2026-05-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-ANT-SAFETY, KIQ-ANT-SDK, KIQ-002-02, KIQ-004-02
- **関連企業:** Anthropic, OpenAI, Meta, Figma
- **要約:** Andrej KarpathyがAnthropic入社（事前学習チーム、ClaudeでClaude研究を加速）。Designer Fund調査: デザイナーの91%がAI週次利用（前年54%）、75%が毎日利用。Claude使用率78%がChatGPT 65%を逆転。Ramp実取引データでもClaude 34.4% vs ChatGPT 32.3%で逆転。Meta 8,000人削減、Cloudflare 1,100人削減（5分の1）。tech layoffs 113,000人超。Google/Microsoft/Meta/Amazon $7,250億capex計画（77%増）。
- **キーファクト:**
  - Karpathy: OpenAI共同創業者→Anthropic事前学習チーム（Nick Joseph配下）
  - デザイナー91%週次AI利用（前年54%）、75%每日利用
  - Claude 78% vs ChatGPT 65%（ツール使用率）
  - Claude Code: 公開1年で2/3のスタックに組み込まれる
  - Ramp: Claude 34.4% vs ChatGPT 32.3%（米国ビジネス実取引）
  - デザイナーの50%がAI生成コードを本番にシップ（早期企業68%）
  - Meta 8,000人削減、7,000人AIチームへ異動、6,000採用取消
  - Cloudflare 1,100人削減（5分の1）、社内AI使用600%増
  - Figma: 収益46%増$333M、純ドルリテンション139%
  - Anthropic調査パートナー開示あり（独立性注意）
- **引用URL:** https://eidosdesign.substack.com/p/may-2026-the-data-caught-up-to-the
- **Evidence ID:** EVD-20260531-0052

### INFO-053
- **タイトル:** MIT Technology Review: AI暴露職業の22-25歳雇用16%相対減 - エントリーレベル危機
- **ソース:** MIT Technology Review / Stanford Digital Economy Lab
- **公開日:** 2026-05-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-02, KIQ-004-03, KIQ-002-04
- **関連企業:** その他
- **要約:** Stanford Digital Economy Lab論文: AI暴露度の高い職業の22-25歳層で16%の相対雇用減（他要因統制後）。上位経験者は同減なし。AI非暴露エントリーレベルも減なし。Anthropic 2026年3月レポートも同方向の示唆的証拠。最近卒大学生失業率5.6%、アンダーインプロイメント42.5%（コロナ以来最高）。「Learn to code」前提崩壊。
- **キーファクト:**
  - 22-25歳AI暴露職業: 16%相対雇用減（2025年11月Stanford論文）
  - 上位経験者: 同減なし→AI特有の影響
  - 最近卒大学生失業率: 5.6%（NY連銀Q4 2025）
  - アンダーインプロイメント: 42.5%（コロナ以来最高）
  - 「Learn to code」前提崩壊: AIが丁度その層を代替
  - Anthropic 2026年3月労働市場レポートも同方向の示唆的証拠
- **引用URL:** https://www.technologyreview.com/2026/05/26/1137865/its-time-to-address-the-looming-crisis-in-entry-level-work/
- **Evidence ID:** EVD-20260531-0053

### INFO-054
- **タイトル:** Microsoft/Uber Claude Code予算超過の真相 - トークン経済学とROI未証明
- **ソース:** eCorpIT / Fortune / TechRadar / Cybernews
- **公開日:** 2026-05-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-ANT-SDK, KIQ-001-05, KIQ-003-01, KIQ-002-02
- **関連企業:** Anthropic, Microsoft, Uber
- **要約:** Microsoft Experiences & Devices部門がClaude Code内部分キャンセル（6月30日）。Uberが2026年AI予算を4ヶ月で消化。Uber: 84%がエージェント利用者（3月）、95%が月次AI利用（4月）、コミットコード70%がAI生成。エンジニア月額$500-$2,000。トークン消費リーダーボードが過剰利用を助長。Uber COO: 「そのリンクはまだない」(ROI未証明)。Anthropic $30Bランレート（80x成長）。6月15日サブスク分割: エージェントSDK/ヘッドレスを別課金化。Microsoft $5B Anthropic投資、Foundry/365 Copilot/Copilot StudioでClaude統合深化。
- **キーファクト:**
  - Microsoft E&D: 年間AI予算を数ヶ月で消費、6/30 Claude Code終了
  - Uber: 5,000エンジニア展開、32%(2月)→84%エージェント(3月)→95%月次(4月)
  - コミットコード70%がAI生成（Uber春季）
  - エンジニア月額$500-$2,000（トークン課金）
  - リーダーボード: チーム別トークン消費ランク付け→過剰利用助長
  - Uber COO: 「消費増とコンシューマー改善のリンクはまだない」
  - Anthropic: $30B収益ランレート（80x成長）
  - 6/15 Anthropic課金変更: エージェントSDK/ヘッドレスを別クレジット化
  - Microsoft同時: $5B Anthropic投資+Foundry/365 Copilot/Copilot Studio統合
  - Maia 200 AIチップでClaude推論の協議中
  - Opus 4.7トークナイザー変更で同一テキスト35%トークン増
- **引用URL:** https://ecorpit.com/microsoft-uber-claude-code-token-cost-2026/
- **Evidence ID:** EVD-20260531-0054

### INFO-055
- **タイトル:** Anthropic安全性選択理由の定量データ - Claude 78%採用 vs ChatGPT 65%
- **ソース:** Designer Fund / Ramp AI Index
- **公開日:** 2026-05-20
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-ANT-SAFETY, KIQ-001-02
- **関連企業:** Anthropic, OpenAI
- **要約:** Designer Fund第2回AI in Designレポート（906名、60カ国以上）: Claude 78% vs ChatGPT 65%。Ramp実取引データ: Claude 34.4% vs ChatGPT 32.3%（4月時点）。Claude Code公開1年でスタックの約3分の2に組み込まれる。注意: Anthropicは調査の開示パートナー。Rampデータは自報告ではなく実取引に基づくため独立性が高い。
- **キーファクト:**
  - Claude 78% vs ChatGPT 65%（906名デザイナー調査）
  - Ramp実取引データ: Claude 34.4% vs ChatGPT 32.3%
  - Claude Code: 1年で3分の2のスタックに組み込まれる
  - デザイナーの50%がAI生成コードを本番シップ
  - Anthropic調査パートナー開示あり（独立性制約）
- **引用URL:** https://eidosdesign.substack.com/p/may-2026-the-data-caught-up-to-the
- **Evidence ID:** EVD-20260531-0055

### INFO-056
- **タイトル:** Spotify 99%エンジニアがAIコーディングツール週次利用 - Claude Code採用急増
- **ソース:** Digital Applied / Spotify Code with Claude London
- **公開日:** 2026-05-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-ANT-SDK, KIQ-004-02, KIQ-002-02
- **関連企業:** Anthropic, Spotify
- **要約:** SpotifyがCode with Claude London（5月19日）で発表: 99%以上のエンジニアがAIコーディングツールを毎週使用。Claude Code採用が急速に拡大。Microsoftでは2月32%→3月84%「エージェント利用者」→4月95%月次AI利用。Uberではコミットコード70%がAI生成。
- **キーファクト:**
  - Spotify: 99%+エンジニアがAIコーディング週次利用
  - Microsoft: 32%(2月)→84%エージェント(3月)→95%(4月)
  - Uber: 70%コミットコードがAI生成
  - Claude Code: 2025年公開→2026年に急速な企業採用
- **引用URL:** https://www.digitalapplied.com/blog/ai-industry-weekly-recap-may-18-25-2026-8-stories
- **Evidence ID:** EVD-20260531-0056

### INFO-057
- **タイトル:** AI暴露エントリーレベル雇用の構造的危機 - 「Learn to code」時代の終焉
- **ソース:** MIT Technology Review (Georgios Petropoulos, USC Marshall)
- **公開日:** 2026-05-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** その他
- **要約:** Stanford Digital Economy Lab + Anthropic労働市場レポートの証拠に基づく分析。AI暴露職業の22-25歳雇用16%相対減は「AIが丁度ジュニアタスク層を代替している」ことを示唆。エントリーレベルは経済の訓練システムの一部であり、AIがドラフト・トリアージ・コーディング・要約を吸収すると、企業は短期的に効率化するが長期的に判断力のストックを失う。「Learn to code」の前提崩壊、AI流暢性と領域判断力の組み合わせが希少価値に。
- **キーファクト:**
  - AI暴露職業22-25歳: 16%相対雇用減
  - ジュニアタスク（ドラフト・コーディング・要約等）がAI代替の第一波
  - 「Learn to code」前提崩壊: AIがそのスキル層を代替
  - AI流暢性×領域判断力の組み合わせが新希少価値
  - エントリーレベル雇用は短期的経費ではなく長期的判断力投資
- **引用URL:** https://www.technologyreview.com/2026/05/26/1137865/its-time-to-address-the-looming-crisis-in-entry-level-work/
- **Evidence ID:** EVD-20260531-0057

### INFO-058
- **タイトル:** ハイパースケーラー$7,250億AIキャップエックス計画 - 採用削減との同時進行
- **ソース:** Eidos Design / FT / Challenger Gray & Christmas
- **公開日:** 2026-05-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-002-04
- **関連企業:** Google, Microsoft, Meta, Amazon
- **要約:** Google/Microsoft/Meta/Amazonが2026年に$7,250億の資本支出を計画（77%増、大部分がAIインフラ）。一方でtech layoffsが113,000人を超え、AIが4月のtech削減理由の26%を占める。Oxford Economics: 企業は実際にはAIで労働者を大規模代替していない。Wharton Peter Cappelli: 企業はAIが仕事をすると主張しつつ証明できず「希望しているだけ」。予算が人からAIへ移動しているが、ジョブがAI代替可能である必要はない。
- **キーファクト:**
  - $7,250億capex計画（Google/Microsoft/Meta/Amazon、77%増）
  - Tech layoffs 113,000人+（5月18日時点）
  - AI理由の削減: 4月tech全体の26%
  - Oxford Economics: 大規模AI代替の証拠なし
  - Wharton: 企業は証明できず「希望しているだけ」
  - Sam Altmanも認める（AI実際の仕事力過大評価）
- **引用URL:** https://eidosdesign.substack.com/p/may-2026-the-data-caught-up-to-the
- **Evidence ID:** EVD-20260531-0058
