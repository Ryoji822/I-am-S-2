# 収集データ: 2026-07-09

## メタデータ
- 収集日時: 2026-07-09 00:16 UTC
- 収集完了: 2026-07-09 00:45 UTC
- 品質フラグ: COMPLETE
- INFO件数: 79
- 実行検索クエリ数: 48（内訳: Step 2公式スクレイプ4件 + Step 3計画クエリ39件 + Step 1.5動的クエリ5件）
- KIQカバレッジ:
  - KIQ-001-01〜05 (Agent Wars): 全5KIQカバー ✓
  - KIQ-002-01〜06 (Enterprise): 全6KIQカバー ✓
  - KIQ-003-01〜05 (Economics): 全5KIQカバー ✓
  - KIQ-004-01〜04 (Workforce): 全4KIQカバー ✓
  - KIQ-005-01〜03 (AGI): 全3KIQカバー ✓
  - BYTEDANCE-CHINESE: カバー ✓
- PIRカバレッジ:
  - PIR-2026-001 (Agent Wars): 24+エントリ ✓ (≥10)
  - PIR-2026-002 (Enterprise): 15+エントリ ✓ (≥10)
  - PIR-2026-003 (Economics): 12+エントリ ✓ (≥10)
  - PIR-2026-004 (Workforce): 10+エントリ ✓ (≥10)
  - PIR-2026-005 (AGI): 10エントリ ✓ (≥10)
- Tier 1企業カバレッジ:
  - OpenAI: 8+エントリ ✓
  - Anthropic: 8+エントリ ✓
  - Google/DeepMind: 8+エントリ ✓
  - xAI/SpaceXAI: 5+エントリ ✓
  - ByteDance: 7+エントリ ✓
- 動的KIQ充足状況（Arbiter 2026-07-08 DEGRADED）:
  - KIQ-OAI-001 (OpenAI収益内訳 政府vs民間): 未充足 – 収益内訳の直接データ不在（純損失$39B・政府契約$200Mは確認）
  - KIQ-MIL-001 (人間却下比率): 未充足 – 17R連続で定量的データ完全不在
  - KIQ-CAR-002-OPS (設計・評価能力の定量市場価値): 未充足 – AIプレミアム18bpsは確認したが能力別の直接的定量は困難
  - KIQ-ANT-002 (Claude Code WAU/DAU): 部分充足 – 非公式データ（DAU/MAU 11.5%・30日アクティブ113万）確認、公式発表不在
  - KIQ-NEW-001 (他社の5%株式提案対応): 未充足 – 他社（Anthropic/Google/Meta）の同意有無不明・N=1継続
- 動的追加クエリ（Step 1.5）:
  - KIQ-OAI-001 (OpenAI収益内訳 政府vs民間): 3クエリ
  - KIQ-MIL-001 (人間却下比率): 3クエリ
  - KIQ-CAR-002-OPS (設計・評価・方向付け能力の定量市場価値): 3クエリ
  - KIQ-ANT-002 (Claude Code固有WAU/DAU絶対値): 3クエリ
  - KIQ-NEW-001 (他社の5%株式提案への対応): 3クエリ

## 収集結果

### INFO-001
- **タイトル:** Introducing GPT-Live: フルデュプレックス音声モデルの新世代
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIはGPT-Liveを発表。フルデュプレックス・アーキテクチャで同時聴取・発話が可能。バックグラウンドでGPT-5.5に委任し検索・推論を実行しながら会話を継続。GPT-Live-1とGPT-Live-1 miniの2バージョンをChatGPTユーザーにグローバル展開開始。API提供は近日予定。
- **キーファクト:**
  - フルデュプレックス音声アーキテクチャ（同時聴取・発話）
  - 深い推論をGPT-5.5に委任するdelegation機能
  - 毎週1億5000万人以上がVoice・Dictation機能を使用
  - GPQA・BrowseComp・τ³-Voice TelecomでAdvanced Voice Modeを大幅上回る
  - 音声ネイティブの安全性評価を新設（自傷・精神病・AIへの感情的依存等）
- **引用URL:** https://openai.com/index/introducing-gpt-live/
- **Evidence ID:** EVD-20260709-0001

### INFO-002
- **タイトル:** Previewing GPT-5.6 Sol: 次世代モデルの限定プレビュー
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-06-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01, KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIはGPT-5.6シリーズ（Sol/Terra/Luna）の限定プレビューを開始。新命名体系導入（番号=世代、Sol/Terra/Luna=能力ティア）。Sol/Terra/LunaはAPI経由で信頼済みパートナーにのみ提供。Terminal-Bench 2.1で91.9%（Sol Ultra）。米国政府との調整プロセス経て段階的リリース。
- **キーファクト:**
  - 3モデル構成: Sol（旗艦 $5/$30 per M tokens）, Terra（バランス $2.50/$15）, Luna（低コスト $1/$6）
  - 新`max`推論エフォートと`ultra`モード（サブエージェント活用）
  - Terminal-Bench 2.1: Sol Ultra 91.9%, Sol 88.8%, Terra 82.5%
  - サイバーセキュリティ: ExploitBench・ExploitGymで大幅改善
  - 70万A100相当GPU時間の自動レッドチーミング
  - CerebrasでSolを750 tokens/secで7月提供予定
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260709-0002

### INFO-003
- **タイトル:** Expanding Managed Agents in Gemini API: バックグラウンドタスク・リモートMCP等
- **ソース:** Google公式ブログ (Google DeepMind)
- **公開日:** 2026-07-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** GoogleはGemini APIのManaged Agentsに新機能追加: バックグラウンド非同期実行、リモートMCPサーバー統合、カスタム関数呼び出し、クレデンシャル更新。単一エンドポイントで推論・コード実行・パッケージ管理・ファイル管理・Web情報検索を隔離クラウドサンドボックスで処理。
- **キーファクト:**
  - `background: true`で長時間タスクの非同期実行
  - リモートMCPサーバー直接接続（カスタムプロキシ不要）
  - カスタム関数とビルトインツールの混在同時使用
  - クレデンシャル更新機能でファイルシステム状態保持
  - Antigravity agentをデフォルトエージェントとして提供
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/
- **Evidence ID:** EVD-20260709-0003

### INFO-004
- **タイトル:** Interactions API GA: Geminiモデルとエージェントの主要インターフェース
- **ソース:** Google公式ブログ (Google DeepMind)
- **公開日:** 2026-06-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** GoogleのInteractions APIがGA到達。Geminiモデルとエージェントの主要APIとなる。Managed Agents、バックグラウンド実行、ツール組み合わせ、Deep Researchアップグレード、メディア生成等を統合。従来のgenerateContent APIは継続サポートするが、フロンティア機能はInteractions APIに先行リリース。
- **キーファクト:**
  - 2025年12月パブリックベータ開始→GA到達
  - Flex/Priority階層（Flex階層は50%コスト削減）
  - 過去インタラクション55日間保持（有料ティア）
  - Roles → Steps schemaへの簡素化
  - Deep Research新バージョン（速度 vs 深度）、Native charts
  - Nano Banana 2画像生成、Lyria 3音楽生成
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/
- **Evidence ID:** EVD-20260709-0004

### INFO-005
- **タイトル:** Introducing the Voice Agent Builder: ノーコード音声エージェント構築
- **ソース:** SpaceXAI（旧xAI）公式ブログ
- **公開日:** 2026-07-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-03
- **関連企業:** xAI (SpaceX子会社)
- **要約:** SpaceXAIはVoice Agent Builder（ベータ）を発表。Grok Voice上でノーコードで本番音声エージェントを構築可能。テレフォニー、ナレッジ検索、ツール、ガードレール、MCP、観測性を一箇所に統合。2分でエージェント構築可能。既存電話番号をSIP経由で移行可能。
- **キーファクト:**
  - $0.05/minの音声API料金、ボイス込み・プラットフォーム費別途なし
  - テレフォニー追加$0.01/min
  - τ-voice Benchリーダーボード公開: Grok Voice Think Fast 1.0がGemini 3.1 Flash Live・GPT Realtime 1.5を上回る
  - 25以上の言語サポート
  - ナレッジベース（ドキュメントコレクション）、ツール・コネクタ（Google Calendar, Outlook, Linear, Notion等）
  - 全通話録音・文字起こし・ツール使用可視化
- **引用URL:** https://x.ai/news/grok-voice-agent-builder
- **Evidence ID:** EVD-20260709-0005

### INFO-006
- **タイトル:** 21 New Flagship Grok Voices: 多言語ボイス追加
- **ソース:** SpaceXAI（旧xAI）公式ブログ
- **公開日:** 2026-07-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** xAI (SpaceX子会社)
- **要約:** SpaceXAIはGrok Voiceに21の新しい旗艦ボイスを追加。多言語ボイスの追加と、元の5ボイスの自然さ改善。
- **キーファクト:**
  - 21の新しい旗艦ボイス追加
  - 多言語対応強化
  - 元の5ボイスの自然さ改善
- **引用URL:** https://x.ai/news/new-flagship-voices
- **Evidence ID:** EVD-20260709-0006

### INFO-007
- **タイトル:** Separating signal from noise in coding evaluations (コーディング評価研究)
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIはコーディング評価におけるノイズ分離に関する研究を発表。ベンチマーク評価の信頼性向上に向けた研究。
- **キーファクト:**
  - コーディング評価におけるsignal-noise分離手法の提案
  - ベンチマーク評価の信頼性向上
- **引用URL:** https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- **Evidence ID:** EVD-20260709-0007

### INFO-008
- **タイトル:** How agents are transforming work: エンタープライズでのエージェント活用
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04, KIQ-004-01
- **関連企業:** OpenAI
- **要約:** OpenAIがエージェントが仕事をどう変革しているかを発表。エンタープライズにおけるエージェント活用の現状と展望。
- **キーファクト:**
  - エンタープライズでのエージェント活用事例
  - 業務変革の方向性
- **引用URL:** https://openai.com/index/how-agents-are-transforming-work/
- **Evidence ID:** EVD-20260709-0008

### INFO-009
- **タイトル:** ByteDance・AlibabaがヒューマンライクAIエージェント機能を7月15日規制前に停止
- **ソース:** DeepLearning.ai The Batch / SCMP
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-002-03, KIQ-002-06
- **関連企業:** ByteDance, Alibaba
- **要約:** ByteDanceのDoubaoとAlibabaのQwenが、中国政府の新規制（7月15日発効）前にカスタマイズ可能なヒューマンライクAIエージェント機能を停止。内部メモによると、ボット開発プラットフォームのパブリックベータは月末予定。
- **キーファクト:**
  - Doubao・QwenがヒューマンライクAIエージェント機能を事前停止
  - 7月15日発効の中国政府AI規制への対応
  - ユーザーの不満を引き起こしている
  - ボット開発プラットフォーム公開ベータは月末予定
- **引用URL:** https://www.deeplearning.ai/the-batch/alibaba-and-bytedance-quash-human-like-bots
- **Evidence ID:** EVD-20260709-0009

### INFO-010
- **タイトル:** Claude Agent SDK TypeScript v2.1.204リリース（Claude Code v2.1.204とパリティ）
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-07-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicのClaude Agent SDK TypeScriptがv2.1.204に更新、Claude Code v2.1.204とパリティ達成。安定版リリースのsdk.d.ts型定義修正を含む。Sonnet 5がClaude Codeのデフォルトモデル（v2.1.197でアクセス可能）。
- **キーファクト:**
  - Claude Agent SDK v2.1.204（Claude Code v2.1.204とパリティ）
  - Sonnet 5がデフォルトモデル（Claude Code v2.1.197更新）
  - sdk.d.ts型定義の修正
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260709-0010

### INFO-011
- **タイトル:** DeerFlow 2.0: ByteDanceのオープンソーススーパーエージェントハーネス
- **ソース:** Instagram / DeerFlow
- **公開日:** 2026-07-05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0をリリース。計画、サブエージェントのスピンアップ、サンドボックスコード実行、実際の作業を発送するオープンソースのスーパーエージェントハーネス。AIが単なるチャットを超えて本格的な作業を遂行する方向への進化。
- **キーファクト:**
  - オープンソースのスーパーエージェントハーネス
  - サブエージェント並列実行、サンドボックスコード実行
  - ByteDance製
- **引用URL:** https://www.instagram.com/p/DaSNgQdk0Zr/
- **Evidence ID:** EVD-20260709-0011

### INFO-012
- **タイトル:** Grok Build CLI: grok-4.5搭載のターミナルコーディングエージェント
- **ソース:** SpaceXAI Docs
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** xAI (SpaceX子会社)
- **要約:** SpaceXAIのGrok Buildはgrok-4.5を搭載し、ターミナルから直接実行されるコーディングエージェント。API経由でも利用可能。Agent Dashboard、Plugin Marketplace、Warp連携等の機能を提供。Composer 2.5モデルも利用可能。
- **キーファクト:**
  - Grok Build: grok-4.5搭載、ターミナルベースのコーディングエージェント
  - Agent Dashboard: 複数セッション同時管理
  - Plugin Marketplace: ビルトインプラグイン市場
  - Warp、OpenCode、Kilo Code等の連携
  - Grok Build 0.1: API経由で利用可能な最速コーディングモデル
- **引用URL:** https://docs.x.ai/build/overview
- **Evidence ID:** EVD-20260709-0012

### INFO-013
- **タイトル:** MCP採用加速: Apple・Microsoft・ERP統合で標準化進む
- **ソース:** The New Stack / LinkedIn / ERP Today
- **公開日:** 2026-07-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic, Apple, Microsoft
- **要約:** MCP（Model Context Protocol）の採用が加速。Appleが1ヶ月で2つ目のMCPサーバーを出荷、Microsoftがエコシステム全体でMCPをサポート、ERPシステムへのMCP統合が進む。Anthropicが2024年11月に導入したオープン標準が業界標準として定着。
- **キーファクト:**
  - Apple: 1ヶ月で2つ目のMCPサーバー出荷
  - Microsoft: エコシステム全体でMCP採用
  - MCP: ERP・データプラットフォーム・SaaSツール・ワークフロー標準接続
  - 2024年11月Anthropic導入 → 業界標準化
- **引用URL:** https://erp.today/model-context-protocol-erp-agentic-ai/
- **Evidence ID:** EVD-20260709-0013

### INFO-014
- **タイトル:** AAIF（Agentic AI Foundation）: オープン標準とエコシステム拡大
- **ソース:** Cisco Outshift / CData / Diginomica
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Linux Foundation, AAIF, Block
- **要約:** AAIF（Agentic AI Foundation）は2025年12月にLinux Foundation傘下で設立。MCPを含む自律エージェントのオープン標準を推進。CData、iTmethods、agentgateway等が新規加盟。Claude・ChatGPT等をまたぐ相互運用性標準を構築中。ワーキンググループはエージェント障害モード、マルチエージェント観測性、本番運用標準を策定。
- **キーファクト:**
  - 2025年12月設立、Linux Foundationプロジェクト
  - MCP・AGNTCY等のオープン標準推進
  - agentgateway（Block発、goose由来）が加盟
  - CData・iTmethods等の企業が加盟
  - エージェント障害モード・観測性・運用標準の策定
- **引用URL:** https://outshift.cisco.com/blog/ai-ml/aaif-chairs-interview
- **Evidence ID:** EVD-20260709-0014

### INFO-015
- **タイトル:** OpenAI Codex Plugins Marketplace: 20+統合でAIコーディング変革
- **ソース:** ZenVanRiel Blog
- **公開日:** 2026-07-03
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIがCodex向けにプラグインマーケットプレイスをローンチ。Slack、Figma、Notion等20以上の統合を提供。3コンポーネント・アーキテクチャで構成。Agent Skillsの概念がエコシステム全体に拡大。
- **キーファクト:**
  - Codex plugin marketplace: 20+統合（Slack, Figma, Notion等）
  - 3コンポーネント・アーキテクチャ
  - Skill Installer: $CODEX_HOME/skillsディレクトリに直接インストール
- **引用URL:** https://zenvanriel.com/ai-engineer-blog/openai-codex-plugins-marketplace-guide/
- **Evidence ID:** EVD-20260709-0015

### INFO-016
- **タイトル:** Claude Enterpriseのエンタープライズセキュリティ体制
- **ソース:** MintMCP / TrueFoundry / Curity
- **公開日:** 2026-07-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude EnterpriseはSOC 2 Type II、SSO（SAML）、SCIMディレクトリ同期、カスタムデータ保持を提供。Claude Tagでエージェントアイデンティティを解決。ただしエンタープライズスケールでのagentic AIアクセス制御には追加のレイヤーが必要。Claude Cowork（ベータ）はAnthropicサーバー上でリモート実行。
- **キーファクト:**
  - SOC 2 Type II認証、SSO SAML、SCIM同期
  - Claude Tag: エージェントアイデンティティ管理
  - Claude Cowork: リモートサーバーで実行（ベータ）
  - カスタムデータ保持ポリシー
- **引用URL:** https://www.mintmcp.com/blog/claude-enterprise-review
- **Evidence ID:** EVD-20260709-0016

### INFO-017
- **タイトル:** Gartner予測: 40%以上のエージェントAIプロジェクトが2027年までにキャンセルリスク
- **ソース:** AugmentCode / Gartner
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Google, Gartner
- **要約:** Gartnerは2027年までに40%以上のagentic AIプロジェクトがキャンセルリスクに直面すると予測。Google Gemini / Vertex AIプラットフォームがエンタープライズ向けに評価されている。クラウドエージェントのbuild vs buyの意思決定が重要視されている。
- **キーファクト:**
  - Gartner: 40%+のagentic AIプロジェクトが2027年までにキャンセルリスク
  - Gemini Enterprise Agent Platform SDK提供
  - Vertex AI: エンタープライズ級ML基盤
- **引用URL:** https://www.augmentcode.com/guides/enterprise-cloud-agents-build-vs-buy
- **Evidence ID:** EVD-20260709-0017

### INFO-018
- **タイトル:** Gemini Computer Use API: ブラウザ・モバイル・デスクトップ制御エージェント
- **ソース:** Google AI for Developers
- **公開日:** 2026-07-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** GoogleのComputer Use APIがブラウザ、モバイル、デスクトップ環境の制御エージェントを構築可能。スクリーンショットを使用してモデルが画面を理解し行動。マルチ環境サポートとintent fieldによる合理化されたアクションを提供。Microsoft Copilot Studioも同様のcomputer use機能をWindows向けに提供。
- **キーファクト:**
  - ブラウザ・モバイル・デスクトップのマルチ環境サポート
  - スクリーンショットベースの画面理解
  - intent field付きアクション
  - Microsoft Copilot Studio: Windows PC向けcomputer use
- **引用URL:** https://ai.google.dev/gemini-api/docs/computer-use
- **Evidence ID:** EVD-20260709-0018

### INFO-019
- **タイトル:** BenchLM 2026年7月: Gemini 3 Pro Deep Thinkがマルチモーダル首位（95.8%）
- **ソース:** BenchLM
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google / DeepMind
- **要約:** 2026年7月時点でBenchLMマルチモーダル&グラウンデッドリーダーボードの首位はGemini 3 Pro Deep Think（加重スコア95.8%）。MMMU、OfficeQA、CharXiv等のマルチモーダルベンチマークで評価。Epoch AI ECIではClaude Fable 5が161ポイントでGPT-5.5 Pro（160）を1ポイント差で上回り、初のAnthropic首位。
- **キーファクト:**
  - Gemini 3 Pro Deep Think: マルチモーダル&グラウンデッド首位 95.8%
  - Claude Fable 5: Epoch AI ECI首位 161pt（GPT-5.5 Proの160を1pt上回る）
  - 初のAnthropic ECI首位
- **引用URL:** https://benchlm.ai/multimodal-grounded
- **Evidence ID:** EVD-20260709-0019

### INFO-020
- **タイトル:** SkillCloak: AIエージェントスキルの静的スキャナが全件突破される重大脆弱性
- **ソース:** LinkedIn / Lelle
- **公開日:** 2026-07-04
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** OpenAI, Anthropic
- **要約:** SkillCloakという概念で、AIエージェントスキルの全静的スキャナが突破されたことを示す研究。エージェントスキルは新たなソフトウェアサプライチェーン攻撃のカテゴリであり、コード実行と言語モデル推論の両方を操作するペイロードを含む。
- **キーファクト:**
  - AIエージェントスキルの全静的スキャナが突破
  - 新たなソフトウェアサプライチェーン攻撃カテゴリ
  - コード実行 + LLM推論の両方を操作
- **引用URL:** https://www.linkedin.com/pulse/skillcloak-every-static-scanner-ai-agent-skills-just-failed-lelle-te2oe
- **Evidence ID:** EVD-20260709-0020

### INFO-021
- **タイトル:** Claude Codeサンドボックス: ネットワーク隔離・ファイルシステム制御・プロセス実行
- **ソース:** TrueFoundry / DataCamp
- **公開日:** 2026-07-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude Codeのサンドボックス機能はネットワークエグレス、ファイルシステムアクセス、プロセス実行、ツール使用を制限する実行環境を提供。Code Execution with MCPでサンドボックス内でコードが実行され、フィルタされた結果のみが返される。DockerもSkills機能でshell/writeツールを制御。
- **キーファクト:**
  - ネットワーク隔離、ファイルシステム制御、プロセス実行制限
  - Code Execution with MCP: サンドボックス内実行→フィルタ結果返却
  - Docker agent skills: shell/write toolsをhidden制御
- **引用URL:** https://www.truefoundry.com/ar/blog/claude-code-sandboxing
- **Evidence ID:** EVD-20260709-0021

### INFO-022
- **タイトル:** AWS Bedrock Agents Classic 7月30日新規クローズ、AgentCoreへ移行
- **ソース:** AWS Documentation
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** Amazon Bedrock Agents（2023年11月ローンチ）は「Bedrock Agents Classic」となり、2026年7月30日から新規顧客をクローズ。AgentCoreが後継。AgentCoreはWeb Search、メモリ（30日間保持）、サーバーレス画像編集エージェント等の機能を提供。
- **キーファクト:**
  - Bedrock Agents Classic: 7/30に新規顧客クローズ
  - AgentCore: Web Search tool、メモリ30日保持
  - サーバーレスエージェント構築ハーネス
- **引用URL:** https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- **Evidence ID:** EVD-20260709-0022

### INFO-023
- **タイトル:** Google Cloud Agent Platform: エンタープライズエージェント構築基盤
- **ソース:** Google Cloud / Vertex AI
- **公開日:** 2026-07-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Google Cloud Agent Platform（Gemini Enterprise Agent Platform）がエンタープライズ向けエージェント構築基盤を提供。Agent Development Kit（ADK）、Model Armor、Agent SkillsによるGoogleプロダクト間のネイティブ統合。Dialogflow CX、Vertex AI Agent Builder、Flutter連携等の開発ツール。
- **キーファクト:**
  - Gemini Enterprise Agent Platform
  - Agent Development Kit（ADK）: Pythonベースエージェント開発
  - Model Armor: セキュリティインターセプション
  - Agent Skills: コーディング環境へのネイティブ機能統合
- **引用URL:** https://cloud.google.com/blog/products/ai-machine-learning/20-questions-for-the-agentic-enterprise
- **Evidence ID:** EVD-20260709-0023

### INFO-024
- **タイトル:** Azure AI Foundry: エージェントワークフローオーケストレーション
- **ソース:** Microsoft Learn / AlphaBold
- **公開日:** 2026-07-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundryがエージェントワークフローのオーケストレーションを提供。安全なツールとAPIを通じてインサイトから承認されたアクションへ接続。Microsoft Fabric統合。SAP・Snowflake・Azure・AWSとのセキュアな本番対応アーキテクチャ。
- **キーファクト:**
  - Azure AI Foundry: エージェントワークフロー オーケストレーション
  - Microsoft Fabric統合
  - SAP・Snowflake・AWS連携の本番対応アーキテクチャ
- **引用URL:** https://www.alphabold.com/microsoft-fabric-azure-ai-foundry-ai-workflows/
- **Evidence ID:** EVD-20260709-0024

### INFO-025
- **タイトル:** Sen. WarrenがPentagon・7社AI企業に軍事契約完全開示要求
- **ソース:** NBC News / Federal News Network / Political Wire
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-002-03
- **関連企業:** OpenAI, Google, NVIDIA, Microsoft, Amazon AWS, SpaceX/xAI, Oracle, Reflection
- **要約:** 上院議員Elizabeth Warrenが7社のAI企業とPentagonに対し、軍事AI契約の完全開示を要求。5月1日、国防総省はSpaceX, OpenAI, Google, NVIDIA, Microsoft, AWS, Reflection, Oracleと契約を締結し、分類軍事ネットワークでの技術利用を統合。Pentagonは「企業ポリシーに関わらず」商用AIを軍事配備可能と主張。150万人の要員が生成AIツール使用中。
- **キーファクト:**
  - Warren: 7社に軍事AI契約条件の開示要求
  - DoD契約企業: SpaceX, OpenAI, Google, NVIDIA, Microsoft, AWS, Reflection, Oracle
  - Pentagon: 1.5 million要員が生成AI使用中
  - 「企業ポリシーに関わらず商用AIは軍事配備可能」
  - 政府調達契約がnotice-and-comment rulemakingやCongressに代わる政策決定場となる構造
- **引用URL:** https://www.nbcnews.com/tech/security/warren-elizabeth-pentagon-ai-companies-release-full-military-contracts-rcna352662
- **Evidence ID:** EVD-20260709-0025

### INFO-026
- **タイトル:** Anthropic v Pentagon完全経緯: $200M契約拒否→供給チェーンリスク指定→法廷闘争→撤回
- **ソース:** WSJ / TechTimes / AI Business / Federal News Network
- **公開日:** 2026-07-04
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, Pentagon, OpenAI
- **要約:** AnthropicがPentagonの$200M契約で「全合法用途」（完全自律兵器・国内監視含む）の要求を拒否。Pentagon（Hegseth長官）がAnthropicを「供給チェーンリスク」に指定（通常は外国敵対国の企業向け）。346頁の法廷文書でAmodei CEOとEmil Michael国防次官の対立が詳細に明らかになった。連邦判事が一時的に供給チェーンリスク指定をブロック。その後Trump政権が輸出規制を解除。Anthropicは「safety theater」とOpenAIを非難。
- **キーファクト:**
  - Anthropic: $200M契約を2つの赤線（自律兵器・国内監視）で拒否
  - Pentagon: Anthropicを「供給チェーンリスク」指定（通常は中国通信企業向け）
  - 346頁法廷文書: Amodei vs Emil Michael国防次官の対立
  - 連邦判事: 供給チェーンリスク指定を一時ブロック
  - Trump政権: 輸出規制（Mythos/Fable）解除
  - CISA: AnthropicのMythosを使用して連邦コード監査中
  - Anthropic: Teresa Carlson（Microsoft/AWS出身）を公共部門責任者に任命
- **引用URL:** https://www.techtimes.com/articles/319713/20260704/pentagon-blacklisted-anthropic-over-autonomous-weapons-limits-emails-reveal-very-close-talks.htm
- **Evidence ID:** EVD-20260709-0026

### INFO-027
- **タイトル:** OpenAIがAnthropicブラックリスト直後にPentagon契約署名 - Altman「 opportunistic and sloppy」
- **ソース:** AOL / AI Business / Gizmodo
- **公開日:** 2026-07-04
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIがAnthropicのブラックリスト指定数時間後にPentagonと契約署名。Altman CEOは後にタイミングが「opportunistic and sloppy（日和見的で雑）」に見えたと認めた。Amodei CEOはOpenAIを「straight up lies」「safety theater」と非難。これにより「順応企業が報われる」構造が浮き彫りに。Meta/Scale AIも$500MのDoD契約で軍事AI統合を進める。
- **キーファクト:**
  - OpenAI: Anthropicブラックリスト数時間後にPentagon契約署名
  - Altman: タイミングが「opportunistic and sloppy」と認める
  - Amodei: OpenAIを「straight up lies」「safety theater」と非難
  - Meta/Scale AI: $500MのDoD契約
  - $54BのPentagon AI契約（史上最大）
- **引用URL:** https://www.aol.com/news/fallout-over-openais-pentagon-deal-050101407.html
- **Evidence ID:** EVD-20260709-0027

### INFO-028
- **タイトル:** OpenAIがTrump政権に5%株式譲渡協議（$42.6B価値・$852B評価額）
- **ソース:** Financial Times / Reuters
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがTrump政権への5%株式譲渡を協議中。$852B評価額のAI企業として政治的障壁をクリアするための財務的つながりを構築。Alaska Permanent Fund型モデル。国家-企業株式関係の前例なき再定義。一方、Googleは連邦機関にGemini AIスイートを$0.47/agencyで提供（71%割引）。
- **キーファクト:**
  - OpenAI: 5%株式をTrump政権に譲渡協議（$42.6B価値）
  - $852B評価額
  - Alaska Permanent Fund型モデル
  - Google: 連邦機関向けGemini $0.47/agency（71%割引）
- **引用URL:** https://www.ft.com/content/7c803eab-8e80-4431-9a87-e943bf00e00b
- **Evidence ID:** EVD-20260709-0028

### INFO-029
- **タイトル:** DPA脅迫・「Preventing Woke AI」大統領令・PentagonのAI調達倫理論争
- **ソース:** FastCompany / Lawfare / Arnold & Porter
- **公開日:** 2026-07-05
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** 2025年7月23日の「Preventing Woke AI」大統領令が企業に圧力。DPA（国防生産法）による強制も検討された可能性。Lawfare分析では、政府調達契約がnotice-and-comment rulemakingやCongressに代わる政策決定の場となっている。政府調達での競合排除構造が顕在化。PentagonのAnthropic批判がシリコンバレーの抵抗を再燃させる可能性。
- **キーファクト:**
  - 「Preventing Woke AI」大統領令（2025年7月23日）
  - DPAによるAI企業強制の可能性
  - 調達契約が政策決定場となる構造
  - Pentagon批判がシリコンバレーの抵抗再燃
- **引用URL:** https://www.fastcompany.com/91554101/authoritarian-governments-twist-ai-safety-coerce-tech-companies
- **Evidence ID:** EVD-20260709-0029

### INFO-030
- **タイトル:** 国連事務総長が自律型致死兵器システム（LAWS）の国際法禁止を要請
- **ソース:** WSJ / LinkedIn (Volker Türk) / UN
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, OpenAI
- **要約:** 国連のAntónio Guterres事務総長が、人間の判断なしに標的を選択・攻撃する自律型致死兵器システム（LAWS）を「道義的に嫌悪すべき（morally repugnant）」と呼び、国際法での禁止を要請。Volker Türk国連人権高等弁務官も「自治権は残虐行為の許可証になれない」と警告。これはAnthropic-Pentagon対立の中核問題であった。キラーロボットが既に実戦配備中との指摘。
- **キーファクト:**
  - Guterres: LAWSは「morally repugnant」、国際法禁止を要請
  - Türk: 「Autonomous weapons cannot become a license for atrocity」
  - Anthropic-Pentagon対立の中核問題
  - キラーロボット実戦配備中との指摘
- **引用URL:** https://www.wsj.com/politics/national-security/killer-robots-must-be-banned-u-n-secretary-general-says-00603020
- **Evidence ID:** EVD-20260709-0030

### INFO-031
- **タイトル:** エンタープライズAI採用ギャップ: 32%のみ持続的影響、88%が本番未到達
- **ソース:** Marketscale / Babybots / DataRobot
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** エンタープライズAI採用の現実と期待のギャップが浮き彫りに。組織の32%のみがAIから持続的ビジネス影響を報告（86%のC-suiteが投資増加）。88%のAIエージェントが本番環境に到達せず。DataRobot調査では71%が「エージェントの運用コストが構築コストを上回る」と回答。PwC調査では12.5%のCEOのみがコスト削減と収益成長の両方を報告。AIエージェント市場は$69.06Bに達すると予測。
- **キーファクト:**
  - 32%のみ持続的ビジネス影響（86%が投資増加）
  - 88%のAIエージェントが本番未到達
  - 71%: 運用コスト > 構築コスト（DataRobot）
  - 12.5%のCEOのみコスト削減+収益成長（PwC）
  - AIエージェント市場: $69.06B予測
  - 従業員のAIエージェント採用率: 28%（Q1比+3pt）
- **引用URL:** https://marketscale.com/industries/software-and-technology/enterprise-ais-adoption-gap-investment-is-up-but-security-data-and-accountability-are-lagging
- **Evidence ID:** EVD-20260709-0031

### INFO-032
- **タイトル:** F500: 80%が構築中、17%のみ本番稼働 - IDC「33 POC中4件のみ本番」
- **ソース:** Elementum / Babybots / IDC
- **公開日:** 2026-07-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** Microsoft
- **要約:** Fortune 500企業の80%がMicrosoft Copilot Studio/Agent BuilderでAIエージェントを構築中だが、本番稼働はわずか17%。IDC研究では企業が33件のAI POCを立ち上げても本番展開に至るのはわずか4件。McKinseyも同様の傾向を報告。57%がAIエージェント導入でコスト削減を報告。
- **キーファクト:**
  - F500: 80%構築中、17%本番稼働
  - IDC: 33 POC → 4件本番展開
  - 57%: コスト削減を報告
  - 期待-実態ギャップの定量化
- **引用URL:** https://www.elementum.ai/blog/best-enterprise-ai-agent-platforms
- **Evidence ID:** EVD-20260709-0032

### INFO-033
- **タイトル:** 中国AI規制3法: 知的エージェント施行令が7月15日発効
- **ソース:** EastFrontier / IAPP
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance, Alibaba
- **要約:** 中国が3つの主要AI規制を制定。最重要は「知的エージェントに関する実施意見（Implementation Opinions on Intelligent Agents）」で2026年7月15日発効。AI倫理、AIエージェント、擬人化AIを対象とする規制シフト。これに先立ちByteDance/AlibabaがヒューマンライクAIエージェント機能を事前停止。
- **キーファクト:**
  - 3つの主要AI規制制定
  - 知的エージェント施行令: 7月15日発効
  - AI倫理・AIエージェント・擬人化AIを対象
  - 広範AI規制から具体的規制へのシフト
- **引用URL:** https://eastfrontier.com/2026/07/02/china-just-enacted-three-major-ai-regulations-here-is-what-they-actually-require/
- **Evidence ID:** EVD-20260709-0033

### INFO-034
- **タイトル:** EU AI Act罰則: 最大€35Mまたは全球売上7%
- **ソース:** EY / Trussed / Docker
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** EU AI Actの非遵守罰則は€7.5M〜€35Mまたは全球売上の7%。エンタープライズに対し、AIを構築する企業だけでなく展開する企業にも義務を課す。GDPRの適切性にも疑問が提起され、agentic AI時代のデータ保護法の適合性が検討されている。
- **キーファクト:**
  - 罰則: €7.5M〜€35M または 全球売上7%
  - 展開企業にも義務
  - GDPR vs agentic AI適合性の検討
- **引用URL:** https://www.ey.com/en_ch/insights/forensic-integrity-services/the-eu-ai-act-what-it-means-for-your-business
- **Evidence ID:** EVD-20260709-0034

### INFO-035
- **タイトル:** Trump「米国AI規制当局は設けない」+FTCがAI精度抑圧に関する政策声明提案
- **ソース:** FT / Federal Register / Brookings
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** Trump政権の outgoing tech adviserが「Trumpは米国AI規制当局を支持しない」と発言。議会共和党は予算調整法案に州レベルAI規制の全国禁止を盛り込もうとしたが失敗。FTCは7月7日、「AIシステムにおける精度の抑圧」に関する政策声明を提案。イリノイ州がPritzker知事の下で国内最厳格クラスのAI安全法に署名。
- **キーファクト:**
  - Trump: 米国AI規制当局設けない方針
  - 議会共和党: 州レベルAI規制全国禁止を試みるも失敗
  - FTC: AI精度抑圧に関する政策声明提案（7月7日）
  - イリノイ州: 国内最厳格クラスAI安全法に署名
- **引用URL:** https://www.federalregister.gov/documents/2026/07/07/2026-13628/policy-statement-concerning-the-suppression-of-accuracy-in-artificial-intelligence-systems
- **Evidence ID:** EVD-20260709-0035

### INFO-036
- **タイトル:** AIがエントリーレベルの雇用を置換: コーディング・CS・データ分析
- **ソース:** Marketplace / Devex / Reddit
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01, KIQ-004-02
- **関連企業:** 複数
- **要約:** AIが特にエントリーレベルの雇用市場に影響。文書分析、財務モデリング、カスタマーサービス、エントリーレベルコーディングがアルゴリズムで処理されるように。 juniorアナリストに割り当てられていたタスクがAIに移行。研究・金融・コンサルティング・コーディング等の分野でエントリーレベル職の破壊可能性。
- **キーファクト:**
  - エントリーレベル職のAI置換加速
  - 影響分野: 文書分析、財務モデリング、CS、コーディング
  - juniorアナリストのタスクがAIに移行
  - 研究・金融・コンサルティングでの破壊可能性
- **引用URL:** https://www.marketplace.org/story/2026/07/06/ai-entry-level-jobs-young-people-training
- **Evidence ID:** EVD-20260709-0036

### INFO-037
- **タイトル:** Klarna・DuolingoのAI人員削減「後悔」 - Forrester: 55%が後悔
- **ソース:** ABC News / Instagram / Reworked
- **公開日:** 2026-07-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** AI駆動の自動化で人員削減を行った企業に逆風。Klarnaは700人のCS担当者をAIで置換しCEOが公に称賛したが、その後再雇用に転じた。Duolingoは外部委託スタッフを削減し「AIで代替」を宣言したが方針転換。Forrester調査で55%の企業がAI解雇を後悔。WEF調査では41%の企業がAI自動化による人員削減を検討中。
- **キーファクト:**
  - Klarna: 700人CS置換→再雇用へ転換。2024年に22%人員削減
  - Duolingo: 外部委託削減→方針転換
  - Forrester: 55%がAI解雇を後悔
  - WEF: 41%が人員削減検討中
- **引用URL:** https://www.facebook.com/ABCNews/posts/a-recent-forrester-study-found-that-55-of-companies-regret-laying-off-human-work/1460954449224764/
- **Evidence ID:** EVD-20260709-0037

### INFO-038
- **タイトル:** SaaSpocalypse: AIエージェントがエンタープライズSaaS株式から$2T消失
- **ソース:** ZenVanRiel / Gartner / AI Agents Directory
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** 複数
- **要約:** AIエージェントが2026年にエンタープライズSaaS株式から$2兆を消失させた。Gartnerは$234BのエンタープライズSaaS支出がagentic AIで破壊されると予測。2027年までに3分の1のagentic AI実装が異なるスキルのエージェントを組み合わせて複雑タスクを管理すると予想。SaaS企業はagentic AI機能を統合するか陳腐化のリスクに直面。
- **キーファクト:**
  - $2T消失: SaaS株式 from AI agents (2026)
  - Gartner: $234B SaaS支出破壊予測
  - 2027年までに1/3のagentic AI実装がマルチエージェント
  - SaaS企業: agentic AI統合か陳腐化の二択
- **引用URL:** https://zenvanriel.com/ai-engineer-blog/saaspocalypse-ai-agents-enterprise-disruption/
- **Evidence ID:** EVD-20260709-0038

### INFO-039
- **タイトル:** 広告代理店の収益構造変化: AIがインハウス化を加速
- **ソース:** Emarketed / Verge / Instagram
- **公開日:** 2026-07-05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Google, Ogilvy
- **要約:** AIエージェントがマーケティングのインハウス化コストを急速に低下させている。ブランドが写真家や代理店に依頼していた作業をMidjourney/Stable Diffusionで社内生成。Ogilvy等の代理店の収益構造がAI参入で劇的に変化。代理店の収益の大部分は依然「ロジック作業」だが、これがAIで最も急速にコモディティ化している分野。
- **キーファクト:**
  - AIエージェントでインハウス化コスト低下
  - ブランド: 写真家/代理店→AI生成（Midjourney等）
  - Ogilvy等の収益構造変化
  - 代理店収益の大部分は「ロジック作業」= AI コモディティ化領域
- **引用URL:** https://emarketed.com/ai/ai-agents-make-in-housing-easier-2026/
- **Evidence ID:** EVD-20260709-0039

### INFO-040
- **タイトル:** LLM API価格比較2026: 600倍の開き、3階層構造
- **ソース:** BenchLM / Spheron / Coursiv
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** 主要LLM APIの価格は600倍以上の開き（$0.05〜$30 per M入力トークン）。OpenAI GPT-5.6: Sol $5/$30, Terra $2.50/$15, Luna $1/$6。Claude Opus 4.8: $5/$25。Gemini 2.5 Pro: $1.25/$10。GPT-5.6では明示的キャッシュブレイクポイントと30分間の最小キャッシュ有効期間を導入。Google Interactions API Flex階層は50%コスト削減。
- **キーファクト:**
  - 価格帯: $0.05〜$30/M入力（600倍差）
  - GPT-5.6: Sol $5/$30, Terra $2.50/$15, Luna $1/$6
  - Claude Opus 4.8: $5/$25
  - Gemini 2.5 Pro: $1.25/$10
  - GPT-5.6: キャッシュ書き込み1.25x、読み取り90%割引
  - Google Flex階層: 50%コスト削減
- **引用URL:** https://benchlm.ai/blog/posts/llm-pricing-2026
- **Evidence ID:** EVD-20260709-0040

### INFO-041
- **タイトル:** GLM-5.1がSWE-Bench Pro首位: GPT-5.4・Claude Opus 4.6を上回る
- **ソース:** DataVLab / Value Add VC
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** Zhipu AI (GLM), OpenAI, Anthropic
- **要約:** 2026年7月のベンチマーク結果: GLM-5.1がSWE-Bench Proで58.4%で首位、GPT-5.4（57.7%）とClaude Opus 4.6（57.3%）を上回る。MMLUは2026年に平均92%（2020年の32%から大幅上昇）でほぼ飽和。GPQA Diamond、SWE-bench Verified、ARC-AGI-2がフロンティアLLMを差別化する主要ベンチマークに。Claude Fable 5はGDPval-AAで1815ptで首位。
- **キーファクト:**
  - GLM-5.1: SWE-Bench Pro首位 58.4%
  - GPT-5.4: 57.7%, Claude Opus 4.6: 57.3%
  - MMLU: 92%平均（2020年32%→2026年92%、ほぼ飽和）
  - 差別化ベンチマーク: GPQA Diamond, SWE-bench Verified, ARC-AGI-2
  - Claude Fable 5: GDPval-AA首位 1815pt
- **引用URL:** https://datavlab.ai/post/llm-benchmarks-2026-which-model-for-which-job
- **Evidence ID:** EVD-20260709-0041

### INFO-042
- **タイトル:** SambaNova $1B調達・$11B評価額: AIチップ企業がNVIDIAに挑戦
- **ソース:** Reuters / CNBC
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** SambaNova
- **要約:** AIチップスタートアップSambaNovaが$10億を調達（General Atlantic主導）、ポストマネー評価額$110億。NVIDIAへの挑戦を狙う。MGXは$490億のAI特化ファンドを設立。AIスタートアップ全体は2024年に$1100億を調達（前年比62%増）。
- **キーファクト:**
  - SambaNova: $1B調達、$11B評価額（General Atlantic主導）
  - MGX: $49B AI特化ファンド
  - AIスタートアップ全体: $110B調達（2024年、YoY+62%）
- **引用URL:** https://www.reuters.com/business/finance/ai-chip-startup-sambanova-valued-11-billion-1-billion-funding-round-2026-07-08/
- **Evidence ID:** EVD-20260709-0042

### INFO-043
- **タイトル:** Anthropic $965B評価額でOpenAI抜く・xAI/SpaceX合算$1.25兆
- **ソース:** Yellow.com / TLDL / Rundown
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, OpenAI, xAI/SpaceXAI
- **要約:** Anthropicが$650億調達で$9650億評価額に達し、OpenAI（約$8500億、2026年3月時点）を抜いて世界最高評価額のAI企業に。SpaceX/xAI合算会社は$1.25兆評価額で世界最高値の非公開企業。OpenAIはNVIDIA、Amazon、SoftBank等を含むラウンドで$850B評価。KuaishouのKlingは$20億調達を予定。
- **キーファクト:**
  - Anthropic: $965B評価額（$65B調達）
  - OpenAI: ~$850B評価額（NVIDIA/Amazon/SoftBank参加）
  - SpaceXAI: $1.25T合算評価額
  - Kuaishou/Kling: $2B調達予定
- **引用URL:** https://yellow.com/news/anthropic-openai-965b-ai-valuation
- **Evidence ID:** EVD-20260709-0043

### INFO-044
- **タイトル:** 米国テック企業のデータセンター投資$850B（YoY+204%）・Hyperscaler capex $750B→$1T+
- **ソース:** Cointelegraph / Yahoo Finance / Seeking Alpha
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** 複数
- **要約:** 米国テック企業がデータセンターリースに記録的$8500億をコミット（YoY+204%）。Hyperscaler AI資本支出は2026年に$7500億（前予測$6700億から上方修正）、2027年に$1兆超へ。但しROI懸念が拡大: FY2026のcapexは$7000億超、負債・エクイティ発行が急増。OpenAI $14B純損予想でcapex > キャッシュフローが確定的。
- **キーファクト:**
  - データセンターリース: $850B（YoY+204%）
  - Hyperscaler capex: $750B（2026年）→$1T+（2027年）
  - ROI懸念: capex >$700B、負債急増
  - データセンター = 次の10年間の最重要インフラ
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/3-ai-data-center-power-123057075.html
- **Evidence ID:** EVD-20260709-0044

### INFO-045
- **タイトル:** AIベンダーロックイン: スイッチングコスト19-34%、MCP/A2A標準で削減可能
- **ソース:** AIPlusInfo / Chitika / Let's Data Science
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** 複数
- **要約:** AIベンダーロックインのスイッチングコストは19-34%。MCPやA2A等のオープン標準がこれを削減可能。AIベンダーロックインは契約リスクだけでなくアーキテクチャ・運用リスクとして再枠組みされている。マルチベンダー戦略の採用が推奨される。4社（OpenAI, Anthropic, Google, xAI）がほぼ同等で競争し、蒸留による技術模倣が急速。
- **キーファクト:**
  - スイッチングコスト: 19-34%
  - MCP/A2A標準で削減可能
  - ロックイン = アーキテクチャ + 運用リスク
  - 4社（OpenAI, Anthropic, Google, xAI）ほぼ同等競争
  - 蒸留による技術模倣が急速
- **引用URL:** https://www.aiplusinfo.com/blog/vendor-lock-in-agentic-ai-platforms/
- **Evidence ID:** EVD-20260709-0045

### INFO-046
- **タイトル:** Stanford研究: 22-25歳ソフトウェア開発者雇用がピーク比20%減少
- **ソース:** Medium / Stanford Digital Economy Lab
- **公開日:** 2026-07-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02, KIQ-002-04
- **関連企業:** 複数
- **要約:** Stanford Digital Economy Labの研究: 22-25歳のソフトウェア開発者雇用が2022年末ピークから2026年7月までに約20%減少。junior職は減少、mid/senior職は増加。テック職の50%がAIスキル要求（前年比98%増）。Amodei CEOは1年以内にAIが全新規コードの90%を生成すると予測。Z.aiがZCodeでGitHub Copilot・Cursor・Anthropicに競合参入。
- **キーファクト:**
  - 22-25歳ソフトウェア開発者雇用: ピーク比約20%減
  - junior職減少・mid/senior職増加
  - テック職50%がAIスキル要求（YoY+98%）
  - Amodei: 1年内にAIが90%のコード生成予測
  - Z.ai ZCode: 低価格・オープンウェイトモデルで競合
- **引用URL:** https://medium.com/@AlexMorgan24/how-chatgpt-is-quietly-replacing-junior-developer-jobs-and-what-to-do-about-it-f2fcff6a2258
- **Evidence ID:** EVD-20260709-0046

### INFO-047
- **タイトル:** WEF Future of Jobs 2025: AIが企業の86%を変革、37%の若年労働者がAI露出
- **ソース:** World Economic Forum
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03, KIQ-002-04
- **関連企業:** 複数
- **要約:** WEF Future of Jobs 2025報告書: AIと情報処理技術が企業の86%を変革すると予測。世界的に37%の若年労働者が中〜高AI露出の仕事に就いており、東ヨーロッパでは75%に達する。今後5年間で「AI・ビッグデータ」と「リーダーシップ・社会的影響力」が高需要スキルに。AI・データ・サイバーセキュリティ・人間の判断力の交差点に新職種が創出。
- **キーファクト:**
  - AIが企業の86%を変革（WEF予測）
  - 若年労働者37%が中〜高AI露出（東欧75%）
  - 高需要スキル: AI・ビッグデータ、リーダーシップ・社会的影響力
  - AI・データ・サイバーセキュリティ交差点に新職種
- **引用URL:** https://www.weforum.org/videos/what-will-the-future-of-jobs-be-like/
- **Evidence ID:** EVD-20260709-0047

### INFO-048
- **タイトル:** AI-proofスキル: 批判的思考・感情的知性・実世界経験の価値上昇
- **ソース:** Forbes / LinkedIn
- **公開日:** 2026-07-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** AIが能力を拡大するにつれ、雇用主は学位・役職・技術的専門知識を超えた資質を重視。AI-proofスキルとして批判的思考、感情的知性（EQ）、実世界経験が注目。最もAIに置換されにくい職業: 看護師、セラピスト、熟練職、創造的役割。AIプレミアム: AI導入が進む地域で約18ベーシスポイント/週の賃金プレミアム。
- **キーファクト:**
  - AI-proofスキル: 批判的思考、EQ、実世界経験
  - 最も安全な職業: 看護師、セラピスト、熟練職、創造的役割
  - AIプレミアム: ~18 bps/週（先進市場）
- **引用URL:** https://www.linkedin.com/pulse/ai-proof-skills-employers-want-most-forbes-magazine-myyvc
- **Evidence ID:** EVD-20260709-0048

### INFO-049
- **タイトル:** AGIタイムライン予測2026: Altman 2025-2026・Hassabis 2030・Amodei 2026-2027
- **ソース:** Quartz / CatDoes / Substack
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Google DeepMind, Anthropic
- **要約:** 主要CEOのAGIタイムライン予測: Sam Altmanは2025-2026年にAGI到達・「強力なAI」を2026-2027年に予測。Demis Hassabisは2025年から5-10年後（〜2030年）にAGI到達・「新たな人類の時代」を予測。Dario Amodeiは2026-2027年に「強力なAI」を予測。3名ともG7サミットに出席予定。各CEOが独自のAGI構築アプローチを持つ。
- **キーファクト:**
  - Altman: AGI 2025-2026、強力なAI 2026-2027
  - Hassabis: AGI ~2030（5-10年）、「新たな人類の時代」
  - Amodei: 強力なAI 2026-2027
  - 3名ともG7サミット出席
- **引用URL:** https://catdoes.com/blog/agi-for-developers
- **Evidence ID:** EVD-20260709-0049

### INFO-050
- **タイトル:** ARC-AGI: GPT-5.2 86.2%・ARC-AGI-3オープンソース解法登場
- **ソース:** NeoSignal / Epoch AI / Reddit
- **公開日:** 2026-07-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI, Anthropic, Tufa Labs
- **要約:** ARC-AGIリーダーボード: GPT-5.2 xhighが86.20%で首位、Claude Opus 4.5が80.00%。ARC-AGI-3の勝利ソリューションがTufa Labsの「Duck」でオープンソース化。目標・ルール・指示なしのベンチマークを突破。但し「ベンチマークを真剣に受け取る人はもういない」との声も。MMLUは2026年に平均92%でほぼ飽和状態。
- **キーファクト:**
  - GPT-5.2 xhigh: ARC-AGI 86.20%首位
  - Claude Opus 4.5: 80.00%
  - ARC-AGI-3: Tufa Labs「Duck」がオープンソースで勝利ソリューション公開
  - ベンチマーク不信の拡大
- **引用URL:** https://neosignal.io/blog/feature-benchmark-leaderboard
- **Evidence ID:** EVD-20260709-0050

### INFO-051
- **タイトル:** データセンター建設モラトリアム: 49%支持・16%反対
- **ソース:** DebateUS.org / AI Frontiers
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** ハイパースケールデータセンター建設モラトリアムについて49%が支持、仅か16%が反対。AIガバナンスには「ラディカルなオプショナリティ」が必要との指摘。Trump政権の2026 National AI Policy Frameworkは連邦指導を求める。AI企業がAGIに近づく中、ガバナンス能力の構築が急務。
- **キーファクト:**
  - データセンター建設モラトリアム: 49%支持・16%反対
  - AIガバナンス: 「ラディカルなオプショナリティ」必要
  - Trump 2026 National AI Policy Framework
- **引用URL:** https://debateus.org/resolved-the-united-states-federal-government-should-enact-a-moratorium-on-hyperscale-data-center-construction/
- **Evidence ID:** EVD-20260709-0051

### INFO-052
- **タイトル:** ByteDance Seedance 2.5: 30秒4K動画を1プロンプトで生成
- **ソース:** CNET / MindStudio
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceのSeedance 2.5がリリース予定。30秒の動画を1つのプロンプトで生成可能。マルチモーダル入力（テキスト+画像+音声+動画）を組み合わせて動画生成。モーショングラフィックス、シネマティックショット、VFXシーン、UGC広告、アニメーションを1モデルで生成。Seedance 2 Miniは軽量版で$0.073/sec。
- **キーファクト:**
  - Seedance 2.5: 30秒動画を1プロンプトで生成
  - マルチモーダル入力統合（テキスト+画像+音声+動画）
  - モーショングラフィックス/VFX/UGC広告/アニメーション対応
  - Seedance 2 Mini: ~$0.073/sec
  - 豆包（Doubao）に全面統合済み
- **引用URL:** https://www.cnet.com/tech/services-and-software/bytedance-introduces-new-seedance-2-5-video-model/
- **Evidence ID:** EVD-20260709-0052

### INFO-053
- **タイトル:** ByteDance Doubao Seed 2.1: Agentモデル（Pro/Turbo）・7月15日規制前の機能削除
- **ソース:** 知乎 / DeepLearning.ai
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-03
- **関連企業:** ByteDance
- **要約:** ByteDanceが2026年6月にDoubao-Seed-2.1 Agentモデル（Pro/Turbo）をリリース。火山方舟（Volcengine）プラットフォームで企業向け提供。但し7月15日の中国政府AI規制（知的エージェント施行令）に先立ち、ヒューマンライクエージェント機能を削除。GLM-5.2は米国先進製品に近い性能で低コスト、シリコンバレーで注目。
- **キーファクト:**
  - Doubao-Seed-2.1: Agentモデル Pro/Turbo（2026年6月）
  - 火山方舟プラットフォームで企業提供
  - 7/15規制前にヒューマンライク機能削除
  - GLM-5.2: 米国先進品に近い性能・低コスト
- **引用URL:** https://zhuanlan.zhihu.com/p/670574382
- **Evidence ID:** EVD-20260709-0053

### INFO-054
- **タイトル:** [動的KIQ-OAI-001] OpenAI財務: $39B純損失（2025年）・政府契約$200M
- **ソース:** Stocktwits / FT / Facebook
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-OAI-001 (動的), KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIの純損失が2024年$50億から2025年約$390億に拡大（リーク財務）。政府契約は$2億。5%政府株式（$426億価値）は政治的障壁クリアが目的。収益の政府vs民間内訳の直接データは依然不在（KIQ-OAI-001核心パラメータ未充足継続）。Anthropic Fable 5が「カムバック」で3倍に拡大との報道。
- **キーファクト:**
  - OpenAI純損失: $5B(2024) → $39B(2025)
  - 政府契約: $200M
  - 5%政府株式: $42.6B価値
  - 収益内訳（政府vs民間）: 依然直接データ不在
- **引用URL:** https://stocktwits.com/news-articles/markets/equity/open-ai-financials-leaked-ahead-of-ipo-chat-gpt-maker-said-to-have-lost-39-b-last-year-here-s-how-that-compares-to-anthropic-space-x/cZKWilcR7Ei
- **Evidence ID:** EVD-20260709-0054

### INFO-055
- **タイトル:** [動的KIQ-MIL-001] AI Safety Index Summer 2026公開 - 軍事AI人間却下比率は依然不在
- **ソース:** Future of Life Institute / ICRC
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-MIL-001 (動的), KIQ-002-06, KIQ-005-03
- **関連企業:** 複数
- **要約:** Future of Life InstituteがAI Safety Index Summer 2026を公開。主要AI企業を安全性・セキュリティ領域で評価。ICRCは「戦争におけるより迅速な意思決定が常に民間人の安全につながるわけではない」と警告。meaningful human controlの維持が不可欠。但し軍事AIコンテキストでの「人間却下比率」の定量的データは17ラウンド連続で完全不在（KIQ-MIL-001未充足継続）。
- **キーファクト:**
  - AI Safety Index Summer 2026公開（Future of Life Institute）
  - ICRC: meaningful human control維持不可欠
  - 人間却下比率: 17R連続完全不在
  - KIQ-MIL-001: 未充足継続
- **引用URL:** https://futureoflife.org/ai-safety-index-summer-2026/
- **Evidence ID:** EVD-20260709-0055

### INFO-056
- **タイトル:** [動的KIQ-ANT-002] Claude Code利用統計: DAU/MAU 11.5%・30日間アクティブ113万
- **ソース:** Threads (afifuddeen)
- **公開日:** 2026-07-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-ANT-002 (動的)
- **関連企業:** Anthropic
- **要約:** Claude Codeの利用統計が一部表面化: 30日間アクティブユーザー約113万、DAU/MAU 11.516%、DAU/WAU 33.716%。但し出典が個人のThreads投稿であり公式確認なし。Claude Codeは「6ヶ月前になってやっと良くなった」との指摘も。AnthropicからのClaude Code固有DAU/WAU公式発表は依然不在（15R連続）。
- **キーファクト:**
  - 30日間アクティブ: ~1,130,305（非公式）
  - DAU/MAU: 11.516%（非公式）
  - DAU/WAU: 33.716%（非公式）
  - 公式確認なし・15R連続不在継続
- **引用URL:** https://www.threads.com/@afifuddeen/post/DaaU1wCGWap
- **Evidence ID:** EVD-20260709-0056

### INFO-057
- **タイトル:** [動的KIQ-NEW-001] OpenAI 5%株式提案: 他社（Anthropic/Google/Meta）の対応不明
- **ソース:** FT / Earn Your Leisure / SixFive Media
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-NEW-001 (動的), KIQ-002-06
- **関連企業:** OpenAI, Anthropic, Google, Meta
- **要約:** OpenAIの5%政府株式提案は、Anthropic・Google・Meta等の他の主要米国AI企業にもマッチング5%株式拠出を促す構造。連邦富基金モデル。OpenAIは5-10%株式と2年間の猶予期間を交換に検討中。但し他社が実際に同意しているかは不明。依然N=1（OpenAI単独）からの脱却なし。SCN-005（地政学的分裂）評価の前提条件は未充足。
- **キーファクト:**
  - 5%株式提案: 他社にもマッチング拠出を促す構造
  - OpenAI: 5-10%株式 vs 2年猶予期間を検討
  - Anthropic/Google/Metaの同意: 不明
  - N=1（OpenAI単独）継続
- **引用URL:** https://www.facebook.com/earnyourleisure/posts/openai-is-in-early-talks-to-give-the-us-government-a-5-equity-stake-valued-at-ap/1457872709707145/
- **Evidence ID:** EVD-20260709-0057

### INFO-058
- **タイトル:** [動的KIQ-CAR-002-OPS] AIプレミアム: 先進市場で18bps/週・設計・評価スキル価値上昇
- **ソース:** arXiv / Forbes
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-CAR-002-OPS (動的), KIQ-004-03
- **関連企業:** 複数
- **要約:** AIプレミアム研究（arXiv）: AI開発・採用が進む地域でAI関連スキルに約18ベーシスポイント/週の賃金プレミアム。設計・評価・方向付け能力は依然人間固有だが、その定量市場価値の直接的測定は困難。PM向けAIエージェントスキル（68種）の市場出現が進むが、これらの「評価・方向付け」能力の貨幣化は間接的。KIQ-CAR-002-OPS（設計・評価・方向付け能力の定量市場価値）は未達成継続。
- **キーファクト:**
  - AIプレミアム: ~18 bps/週（先進市場）
  - 設計・評価スキル: 人間固有だが定量困難
  - PM向けAIエージェントスキル68種市場出現
  - KIQ-CAR-002-OPS: 未達成継続
- **引用URL:** https://arxiv.org/html/2606.30583v2
- **Evidence ID:** EVD-20260709-0058

### INFO-059
- **タイトル:** 広告運用AI自律化: リード80%増・コンバージョン77%向上・88%日常利用の裏側
- **ソース:** Logarithmic / MarketingMary
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** 複数
- **要約:** マーケティング自動化はリードを80%増加させ、コンバージョン率を77%向上。コンテンツ制作はAIにより35-50%高速化。世界広告費は$1兆を突破。但し「88%日常AI利用率」の主張はキャンペーン運用危機を隠蔽しているとの指摘。全マーケティング自動化ツールがエージェント機能を追加する trend にあるが、最も過小評価されている機能は「autonomy」ではなく「readable event log」。
- **キーファクト:**
  - マーケティング自動化: リード80%増・コンバージョン77%向上
  - コンテンツ制作: AIにより35-50%高速化
  - 世界広告費: $1兆突破
  - 「88%日常AI利用」は運用危機を隠蔽
  - event log可読性 > 追加autonomy
- **引用URL:** https://www.logarithmic.com/perspectives/the-88percent-daily-ai-usage-claim-masks-a-campaign-operations-crisis
- **Evidence ID:** EVD-20260709-0059

### INFO-060
- **タイトル:** CyberAgent収益構造: インターネット広告¥468.2B・メディア¥243.6B・ゲーム¥259.2B
- **ソース:** SimplyWall.St
- **公開日:** 2026-07-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgentの収益構造: インターネット広告事業¥468.2B、メディア&IP事業¥243.6B、ゲーム事業¥259.2B。インターネット広告が最大収益源。日本の自動化投資銘柄として創業者主導企業3社の一つに選出。AI投資と自動化への注力が収益構造に反映されつつある。
- **キーファクト:**
  - インターネット広告: ¥468.2B（最大収益源）
  - メディア&IP: ¥243.6B
  - ゲーム: ¥259.2B
  - 日本自動化投資テーマ銘柄
- **引用URL:** https://simplywall.st/stocks/jp/semiconductors/tse-6323/rorze-shares/news/investing-in-automation-with-3-japanese-founder-led-stocks-s/amp
- **Evidence ID:** EVD-20260709-0060

### INFO-061
- **タイトル:** コーディング能力の市場価値変化: $180K-$250K base pay・スキル要件シフト
- **ソース:** KnowledgeHut / CollegeMentor / Instagram
- **公開日:** 2026-07-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** 複数
- **要約:** AI時代のソフトウェア開発者給与: トップテック企業でbase pay $180K-$250K、需要は増加傾向（AIがソフトウェア構築を高速化したため）。AI/MLエンジニア給与（インド）: ₹30-40 LPA。コーディングは依然学ぶ価値があるが、スキル要件は「書ける」から「AIに書かせて評価・統合できる」へシフト中。AIスキルに月$1K-$5Kのフリーランス市場も出現。
- **キーファクト:**
  - トップテック base pay: $180K-$250K（需要増）
  - AI/MLエンジニア: ₹30-40 LPA（インド）
  - スキル要件: 「書ける」→「評価・統合できる」
  - AIスキルフリーランス: $1K-$5K/月
- **引用URL:** https://www.knowledgehut.com/blog/programming/ai-powered-software-development-career
- **Evidence ID:** EVD-20260709-0061

### INFO-062
- **タイトル:** 再帰的自己改善: 「既存能力フロンティア内での開発速度圧縮」に過ぎない
- **ソース:** CACM (Communications of the ACM) / Fluid Attacks / Wired
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic, 複数
- **要約:** CACMの分析: 再帰的自己改善（RSI）は「既存の能力フロンティア内で開発速度を圧縮する」に過ぎず、新しい能力境界を拡張するものではない（Tejasvi Addagada SVP）。自己生成コードからの学習は外部品質シグナルなしでは劣化傾向。AnthropicはAIが人間の制御を脱するリスクを警告し、グローバルな一時停止を求めた。フロンティアラボだけでなく個人でも自己改善AIの構築が可能（Wired）。
- **キーファクト:**
  - RSI = 開発速度圧縮（既存フロンティア内）、能力境界拡張ではない
  - 自己生成コード学習: 外部品質シグナルなしで劣化
  - Anthropic: グローバル一時停止要求
  - 個人レベルでもRSI構築可能
- **引用URL:** https://cacm.acm.org/news/is-recursive-self-improvement-really-here/
- **Evidence ID:** EVD-20260709-0062

### INFO-063
- **タイトル:** AGI定義の不合一覧: OpenAI・UN・学術界で定義バラバラ
- **ソース:** Wikipedia / Qubic / UN Independent Panel
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, 複数
- **要約:** AGI定義の不合: OpenAI憲章は「ほぼ全ての経済的に価値ある仕事で人間を上回る高度に自律的なシステム」、他ラボは異なる定義を採用。UN独立国際科学パネルAIが予備報告書を公開。Ben Goertzel（SingularityNET）は人間レベルAGIの intense debate を指摘。定義コンセンサスは存在せず、タイムライン予測の前提が不安定。
- **キーファクト:**
  - OpenAI: 「経済的に価値ある仕事で人間を上回る自律システム」
  - UN独立パネル: AI予備報告書公開
  - 定義コンセンサス: 不在
  - タイムライン予測の前提不安定
- **引用URL:** https://www.un.org/independent-international-scientific-panel-ai/sites/default/files/2026-07/en_Preliminary%20Report_.pdf
- **Evidence ID:** EVD-20260709-0063

### INFO-064
- **タイトル:** 通義千問・豆包が7月15日にAI Agent サービス停止 - 中国規制対応
- **ソース:** 香港ヤフーファイナンス / 豆包公式
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-03
- **関連企業:** ByteDance, Alibaba
- **要約:** アリババ旗下通義千問と字節跳動旗下豆包が共に7月15日にAI Agentサービスを停止するとユーザーに通知。中国政府の知的エージェント規制（施行令7/15）に対応。停止後はAI Agent機能が利用不可に。豆包公式サイトではSeedance 2.0動画生成モデルが豆包に全面統合済み。火山方舟プラットフォームで企業向け大模型ソリューション人材を募集中。
- **キーファクト:**
  - 通義千問・豆包: 7/15にAI Agent サービス停止
  - 中国規制: 知的エージェント施行令 7/15
  - 豆包: Seedance 2.0全面統合済み
  - 火山方舟: 企業向け大模型提供継続
- **引用URL:** https://hk.finance.yahoo.com/news/%E5%8D%83%E5%95%8F%E5%8F%8A%E8%B1%86%E5%8C%857%E6%9C%8815%E6%97%A5%E6%9A%AB%E5%81%9C-ai-agent-%E6%9C%8D%E5%8B%99-105530913.html
- **Evidence ID:** EVD-20260709-0064

### INFO-065
- **タイトル:** 2026 Singapore Consensus: AI安全性研究の世界優先事項を確立
- **ソース:** GovInsider / ITU / Eversheds Sutherland
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** 複数
- **要約:** 2026 Singapore ConsensusがAI安全性研究の世界的優先事項を確立。社会的影响に重点。UN Global Dialogueが7月6日に安全で包摂的なAIの緊急訴求で開幕。EU Councilは6月29日にAI Act簡略化規則を採択（高リスクシステム・透明性ルール・ターゲット変更）。中国AIガバナンスがUN議題に。AI Child Safety Pledgeが主要議題。MATS夏季2026アライメント研究フェローシップが開催中。
- **キーファクト:**
  - 2026 Singapore Consensus: AI安全研究優先事項確立
  - UN Global Dialogue: 7/6開幕・安全で包摂的AI
  - EU: 6/29 AI Act簡略化規則採択
  - AI Child Safety Pledge
  - MATS Summer 2026: アライメント研究フェローシップ
- **引用URL:** https://govinsider.asia/intl-en/article/sustained-efforts-needed-to-build-global-trust-in-an-ai-driven-era
- **Evidence ID:** EVD-20260709-0065

### INFO-066
- **タイトル:** Coze智能体平台: B站教程4時間コースが最完– エコシステム成長継続
- **ソース:** 新浪 / zhenbanw
- **公開日:** 2026-07-05
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceのCoze智能体プラットフォームの教育エコシステムが急成長。B站（ビリビリ）で4時間のCoze入門完全教程が2026年最完と話題。ゼロベースから10+の実戦案例までカバー。但し7/15規制による影響は不明。Cozeは中国のノーコードAIエージェント構築の主要プラットフォーム。
- **キーファクト:**
  - Coze: B站4時間入門教程が2026年最完
  - 10+実戦案例カバー
  - ノーコードAIエージェント構築主要プラットフォーム
  - 7/15規制の影響: 不明
- **引用URL:** https://www.sina.cn/news/detail/5317712218953927.html
- **Evidence ID:** EVD-20260709-0066

### INFO-067
- **タイトル:** Klarna 4年間で従業員50%削減・Duolingo契約社員切替停止・55%がAI解雇後悔
- **ソース:** UnboxFactory / ABC News / Reworked
- **公開日:** 2026-07-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaは4年間でAI採用により従業員を50%削減（CS 700人をAI代替）、2030年までにさらなる削減を計画。Duolingoは契約社員を削減したが人間をAIで置き換えるのを停止。Forrester調査（$1B+売上企業350社）: 55%がAIのため人間を解雇したことを後悔。WEF調査: 41%の企業がAI自動化による人員削減を検討。BCG 2026 AI Radar: 企業はAI支出を倍増（売上の0.8%→1.7%）、CEOの半数が自社のAI投資に満足。
- **キーファクト:**
  - Klarna: 4年で50%削減・CS700人AI代替・2030年追加削減計画
  - Duolingo: 契約社員削減後・AI置換停止
  - Forrester: 55%がAI解雇を後悔（$1B+企業350社調査）
  - WEF: 41%がAI人員削減検討
  - BCG: AI支出倍増（0.8%→1.7%）・CEO半数が満足
- **引用URL:** https://www.facebook.com/unboxfactory/posts/the-ai-job-cuts-are-no-longer-a-prediction-theyre-happening-right-now-and-the-nu/1067498035601246/
- **Evidence ID:** EVD-20260709-0067

### INFO-068
- **タイトル:** SpaceXがCursor（Anysphere）を$60Bで買収・グローバルVC fundがH1で過去最高$510B
- **ソース:** Wortins / SiliconANGLE / Crunchbase
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** SpaceXAI/Cursor, 複数
- **要約:** 2026年H1のグローバルVC fundが過去最高$510B（Crunchbase）。主要M&A: SpaceXが6/16にAIコーディングStartup Cursor（Anysphere）を$60B全株取引で買収合意（Q3 2026クローズ予定）。FigmaがBudチームを買収。CuspAIが$400M調達（Bezos出資）。Lemrock（エージェントAI）が€6M（Sia参加）。FYLD（建設AI）が$40M調達。AIブームが投資を加速。
- **キーファクト:**
  - SpaceX → Cursor買収: $60B全株取引（Q3 2026クローズ予定）
  - グローバルVC fund H1 2026: 過去最高$510B
  - CuspAI: $400M調達（Bezos出資）
  - FYLD（建設AI）: $40M
  - Lemrock（エージェントAI）: €6M
- **引用URL:** https://www.wortins.com/blog/biggest-ai-acquisitions-2026
- **Evidence ID:** EVD-20260709-0068

### INFO-069
- **タイトル:** OpenAI IPO目標$1T以上・Anthropic $965B評価（OpenAI上回る）
- **ソース:** Yahoo Finance / Motley Fool / Investors Business Daily
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04, KIQ-003-01
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAI: Sam AltmanがIPO評価額$1T未満を拒否。2026年に月約$2B収益。現在評価額$852B（3月）。IPO目標: late 2026〜2027、$60B+調達計画。Anthropic: 5月調達で$965B評価、OpenAIの$852Bを上回る。2026年10月Nasdaq上場目標。San Franciscoの住宅販売者がOpenAI/Anthropic株式を決済手段として求めるほどの注目度。
- **キーファクト:**
  - OpenAI: IPO目標$1T+・現在$852B・月収益~$2B
  - OpenAI IPO: late 2026-2027・$60B+調達
  - Anthropic: $965B評価（OpenAI上回る）・10月Nasdaq上場目標
  - SF不動産: OpenAI/Anthropic株式を決済手段として求める動き
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/sam-altman-called-openai-ipo-093300522.html
- **Evidence ID:** EVD-20260709-0069

### INFO-070
- **タイトル:** オープンソースLLM 2026年7月: Kimi K2・GLM-5.2・DeepSeek V4・Llama 4が台頭
- **ソース:** Thunder Compute / TECHSY / CSIS
- **公開日:** 2026-07-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Z.ai, DeepSeek, Meta, Moonshot
- **要約:** 2026年7月オープンソースLLMトップ: Kimi K2, GLM-5.2, DeepSeek V4, Llama 4, Nemotron。GLM-5.2（Z.ai）はコーディング・エージェントタスクで米国トップクラスのクローズドモデルに迫る性能（CSIS分析）。SWE-bench Pro比較でGLM-5.2・DeepSeek V4・Kimi K2.6は62%台。オープンソース vs クローズドの性能ギャップは大幅に縮小。カスタマイズ・プライバシー・デプロイメント柔軟性が優位性。
- **キーファクト:**
  - トップOSS LLM: Kimi K2, GLM-5.2, DeepSeek V4, Llama 4, Nemotron
  - GLM-5.2: 米国クローズドモデルに迫る性能（CSIS）
  - SWE-bench Pro: GLM-5.2/DeepSeek V4/Kimi K2.6 = 62%台
  - OSS vs クローズドギャップ: 大幅縮小
- **引用URL:** https://www.thundercompute.com/blog/best-open-source-llms
- **Evidence ID:** EVD-20260709-0070

### INFO-071
- **タイトル:** Bengio「AI放置なら破局的危害」vs LeCun「単一AGI追求無意味・基盤ギャップ解決を」
- **ソース:** NDTV / Instagram / Wikipedia
- **公開日:** 2026-07-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** 複数
- **要約:** Yoshua Bengio（AIのゴッドファーザー）: AIを放置すれば破局的危害を引き起こす恐れと警告（7/2）。Yann LeCun: 単一の「汎用」知能を追うのではなく、具体的な基盤的ギャップを解決すべきと主張。Bengio・LeCun・Russell間の強いAIリスクに関する活発な議論が継続。Yuval Noah Harari: 超知能はリスクと潜在的恩恵の両方を拡張、結果は人間の選択次第。
- **キーファクト:**
  - Bengio: AI放置なら破局的危害警告（7/2）
  - LeCun: 単一AGI追求無意味・基盤ギャップ解決を主張
  - Bengio-LeCun-Russell論争: 継続中
  - Harari: 超知能=リスク×恩恵、結果は人間の選択次第
- **引用URL:** https://www.instagram.com/reel/DaT_dBrzfyu/
- **Evidence ID:** EVD-20260709-0071

### INFO-072
- **タイトル:** 企業AI採用の新競争優位: フィードバック計測・独自データ堀・配信力>能力
- **ソース:** Coderio / Moneycontrol / LinkedIn
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** Microsoft, 複数
- **要約:** AI統合システムが新たな競争優位の堀。フィードバック計測を組み込んだ企業が改善軌道で勝利。エンタープライズAI採用の次フェーズ: 主権・マルチモデル柔軟性・ビジネス成果（ベンチマークではなく）。Microsoftが6,000人社員を動員し企業のAI利用方法を変革。「配信力は能力を凌駕する（Distribution beats capability）」。StartupはProprietary Data Moat構築に注力すべき。
- **キーファクト:**
  - AI統合システム = 新競争優位の堀
  - フィードバック計測組み込み企業が勝利
  - エンタープライズAI次フェーズ: 主権・マルチモデル・成果重視
  - Microsoft: 6,000人動員でAI利用変革
  - 配信力 > 能力
- **引用URL:** https://www.coderio.com/blog/biz-tech/competitive-moat-ai-integrated-systems/
- **Evidence ID:** EVD-20260709-0072

### INFO-073
- **タイトル:** HBR分析: 12,000+の実AIユースケース・25%超が専門家タスク委譲
- **ソース:** Harvard Business Review / JobZone Risk / Forbes
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01, KIQ-002-04
- **関連企業:** 複数
- **要約:** HBR（Marc Zao-Sanders）が12,000+の実世界AIユースケースを分析: 上位ユースケースの25%超が「AIに専門家タスクを委譲する」こと。Forrester: 55%の企業がAI解雇を後悔。AIが完全に人間を置換できないケースが多数。JobZone予測: 2050年までに現在の役割の20-80%がAI置換の可能性。医療分野ではAIが人間を置換するというより労働力が進化中。
- **キーファクト:**
  - HBR: 12,000+ユースケース分析・25%超が専門家タスク委譲
  - Forrester: 55%がAI解雇後悔
  - 2050年AI置換予測: 現役割の20-80%
  - 医療: 置換より進化
- **引用URL:** https://www.instagram.com/reel/DagW-ifkvvn/
- **Evidence ID:** EVD-20260709-0073

### INFO-074
- **タイトル:** KPMG等コンサル大手が新卒採用削減・Fortune 500の40%がCAIO配置へ
- **ソース:** Devex / LinkedIn / ABC News
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** KPMG, 複数
- **要約:** KPMGを含む大手コンサルファームが新卒採用を削減（AIがエントリーレベルタスクを代替）。Devex報告: AIがグローバル開発分野のエントリーレベル仕事を減少させ採用を厳格化。Forrester: $1B+売上企業350社調査で、全社がAIエージェントをパイロット/導入済み。Chief AI Officer (CAIO)役職が急速に定着し、2026年末までにFortune 500の4割が配置予定。エージェントが組織図に登場。
- **キーファクト:**
  - KPMG等大手コンサル: 新卒採用削減
  - Forrester: $1B+企業350社全てがAIエージェント導入済み
  - CAIO: 2026年末までにFortune 500の40%が配置
  - エージェントが組織図に登場
- **引用URL:** https://www.facebook.com/Devex/posts/as-ai-transforms-global-development-fewer-entry-level-jobs-and-tighter-hiring-ar/1474218268069422/
- **Evidence ID:** EVD-20260709-0074

### INFO-075
- **タイトル:** DeepSeek $500B評価で$50B+調達・ByteDance 2026年$70Bインフラ支出検討
- **ソース:** 投资界 / 钛媒体 / 财新
- **公開日:** 2026-07-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04, BYTEDANCE-CHINESE
- **関連企業:** ByteDance, DeepSeek, Kuaishou
- **要約:** 中国AI資金調達ラッシュ: DeepSeekが「不融資・不上市・不商業化」の方針を覆し初の外部融資で¥500億元以上調達、投後評価$500B突破。ByteDanceは2026年に$700億のデータセンター・AIインフラ支出を検討中。Kuaishou（快手）の可霊AIが$30億調達、評価額$180B（騰訊・阿里雲・百度参投）。可霊AI: 年収¥11億・年損失¥19億・純資産マイナスの矛盾。
- **キーファクト:**
  - DeepSeek: ¥500億+調達・評価額$500B突破
  - ByteDance: 2026年$70Bインフラ支出検討
  - 可霊AI: $30億調達・評価額$180B（騰訊・阿里雲・百度）
  - 可霊AI: 年収¥11億・年損失¥19億
- **引用URL:** https://news.pedaily.cn/202607/565898.shtml
- **Evidence ID:** EVD-20260709-0075

### INFO-076
- **タイトル:** 豆包DAU 2億超・月活3億+・日収<100万元 vs 日次算力コスト数千万元
- **ソース:** 财富号 (eastmoney)
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** 豆包（Doubao）の2026年上半期: DAU 2億超、月活3億+。但し日収は100万元（約$14万）未満、一方で日次算力コストは数千万元に達し、Bilibiliの運営コストを超過。自建算力センター投入は別途。AIGC APP月活ランキング（QuestMobile 2025年1月）: DeepSeek第1位・豆包第2位。大規模ユーザー獲得と収益化の乖離が深刻。
- **キーファクト:**
  - 豆包DAU: 2億超（2026年H1）
  - 月活: 3億+
  - 日収: <100万元（~$14万）
  - 日次算力コスト: 数千万元（Bilibili運営コスト超）
  - AIGC APP月活: DeepSeek #1・豆包 #2
- **引用URL:** https://caifuhao.eastmoney.com/news/20260706103750572551130
- **Evidence ID:** EVD-20260709-0076

### INFO-077
- **タイトル:** ByteDance EdgeBench: 134タスク・38,000時間のエージェント環境学習ベンチマーク
- **ソース:** ByteDance Seed公式ブログ / HuggingFace / AlphaSignal
- **公開日:** 2026-07-02
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01, KIQ-005-01
- **関連企業:** ByteDance
- **要約:** ByteDance Seedが7/2にEdgeBenchをリリース。134の実世界タスク・約38,000時間のエージェント相互作用で構成される超長期ベンチマーク。環境フィードバックから自律的に学習するエージェント能力を測定。発見: log-sigmoid スケーリング法則（相互作用時間の関数）。エージェントは再起動するより経験を保持する方が学習効率が高い。Dreamina Seedance 2.0 miniも同時リリース（低コストで同等性能）。
- **キーファクト:**
  - EdgeBench: 134実世界タスク・~38,000時間相互作用
  - log-sigmoid スケーリング法則発見
  - 経験保持 > 再起動（学習効率）
  - Dreamina Seedance 2.0 mini: 低コスト同等性能
- **引用URL:** https://seed.bytedance.com/en/blog/edgebench-measuring-real-world-environment-learning-and-discovering-a-new-scaling-law
- **Evidence ID:** EVD-20260709-0077

### INFO-078
- **タイトル:** Trump大統領令14409「AI革新・安全保障推進」・AI Safety Index Summer 2026公開
- **ソース:** Mintz / Future of Life Institute / USC
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** 複数
- **要約:** Trump政権: 6/2に大統領令14409「高度AI革新・安全保障推進」に署名、連邦政府機関に指示。AI Safety Index Summer 2026: 操作・ミスアライメント・内部デプロイメントのカバレッジを追加。USC ICML 2026研究: AIモデルがアップデート1回で安全から危険に転じる可能性を実証。豪州AI Safety Instituteが新モデルテストを継続。IAPS AI Policy Fellowship 2026（$15,000 stipend）が若手プロ向けに実施中。
- **キーファクト:**
  - 大統領令14409: AI革新・安全保障推進（6/2署名）
  - AI Safety Index Summer 2026: 操作・ミスアライメント範囲追加
  - USC: アップデート1回で安全→危険転換を実証
  - 豪州AISI: 新モデルテスト継続
- **引用URL:** https://www.mintz.com/insights-center/viewpoints/54941/2026-07-08-ai-washington-report-july-2026-edition
- **Evidence ID:** EVD-20260709-0078

### INFO-079
- **タイトル:** Anthropic Claude Science開始・WAIC 2026「AIは補助道具から能動的発見者へ」
- **ソース:** 36Kr / Instagram / NEA
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** Anthropicが6/30にClaude Scienceを開始: 研究者の散在するツールを1つのワークスペースに統合（データベース、論文、計算ツール）。WAIC 2026 AI for Science: AIが科学研究において「補助道具」から「能動的発見者」へ進化中。NEA投資のAI Neolab: 自律的実験・理論推論による新物理発見を目指す。AGI-26カンファレンスが3週間後に開催予定。2026年半ば: AI進化速度は予想を上回るが、ユーザビリティが追従困難。
- **キーファクト:**
  - Claude Science開始（6/30）: 研究者ワークスペース統合
  - WAIC 2026: AI「補助道具」→「能動的発見者」進化
  - AI Neolab: 自律推論による新物理発見を目指す
  - AGI-26カンファレンス: 3週間後開催
  - 2026年半ば: AI進化 > 予想、UX < 追従困難
- **引用URL:** https://eu.36kr.com/en/p/3884022753882115
- **Evidence ID:** EVD-20260709-0079
