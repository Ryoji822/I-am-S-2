# 収集データ: 2026-06-11

## メタデータ
- 収集日時: 2026-06-11 01:30 UTC
- 実行クエリ数: 97 / 114 (collection_plan 91 + 動的 6)
- scrape実行数: 12件 (blog pages 5 + detailed articles 7)
- 収集情報数: 80件 (INFO-001〜INFO-080)
- Evidence ID 採番範囲: EVD-20260611-0001 〜 EVD-20260611-0080
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 動的KIQ: KIQ-ANT-SAFETY ✓, KIQ-NEW-01 ✓, KIQ-NEW-03 ✓, CVE-8.7追跡 ✓, KIQ-GOO-001 ✓
- 品質フラグ: NORMAL
- 企業カバレッジ: OpenAI(12件), Anthropic(10件), Google(12件), xAI(7件), ByteDance(8件), 業界全体(31件)
- Arbiter優先KIQ: KIQ-003-03(limit→10実行 ✓), KIQ-ANT-SAFETY(動的 ✓), KIQ-NEW-01(動的 ✓), KIQ-NEW-03(動化 ✓), CVE-8.7追跡(動的 ✓), KIQ-GOO-001(動的 ✓), QHG再定義(手続き事項)
- 動的追加クエリ:
  - KIQ-ANT-SAFETY: "enterprise Claude selection reason survey", "Anthropic Claude enterprise customer satisfaction Kano analysis", "enterprise AI vendor selection criteria safety", "Claude vs GPT enterprise adoption reasons"
  - KIQ-NEW-01: "Anthropic S-1 filing safety research budget", "Anthropic IPO safety investment allocation", "Anthropic financial disclosure research spending"
  - KIQ-NEW-03: "AI agent task completion rate HCAST benchmark monthly", "agent autonomous completion rate trend 2026", "HCAST benchmark results progress"
  - CVE-8.7: "CVE-8.7 Claude Code RCE patch enterprise response", "Claude Code CVE-8.7 vulnerability impact scope", "Anthropic CVE security patch enterprise customer reaction"
  - KIQ-GOO-001: "AWS Azure Google Cloud growth rate comparison 2026", "Google Cloud revenue growth vs AWS Azure quarterly", "cloud provider AI revenue market share comparison"

## 収集結果

### INFO-001
- **タイトル:** How an astrophysicist uses Codex to help simulate black holes
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAIのCodexが天体物理学研究でブラックホールシミュレーションに活用されている事例。科学研究におけるAIエージェントの実用化を示す。
- **キーファクト:**
  - Codexが天体物理学者のブラックホールシミュレーション作業を支援
  - 科学研究分野でのAIエージェント適用事例
- **引用URL:** https://openai.com/index/using-codex-to-simulate-black-holes/
- **Evidence ID:** EVD-20260611-0001

### INFO-002
- **タイトル:** Access OpenAI models and Codex through your Oracle cloud commitment
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** OpenAI, Oracle
- **要約:** OpenAIとOracleがパートナーシップを発表。Oracle Cloud Infrastructure (OCI)顧客が既存のOracle Cloud Universal Creditsを使ってOpenAIモデルとCodexにアクセス可能に。エンタープライズの調達プロセスを通じたAI導入を促進。
- **キーファクト:**
  - Oracle Cloud Universal Credits (UCM)でOpenAIフロントィアモデルとCodexにアクセス可能
  - 既存の調達ワークフローとクラウドコミットメント内でAI導入可能
  - 数週間以内に利用開始予定
- **引用URL:** https://openai.com/index/openai-on-oracle-cloud/
- **Evidence ID:** EVD-20260611-0002

### INFO-003
- **タイトル:** Confidential submission of draft S-1 to the SEC
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがSECに機密S-1を提出。「流出すると思われるので発表する」と明言。上場時期は未定で、非上場企業としてやりやすいこともあるとしつつ、より早く上場するオプションも確保。
- **キーファクト:**
  - SECに機密S-1提出済み
  - 上場時期は未定（非上場のまま進めたい事項もある）
  - 早期上場のオプションも確保
- **引用URL:** https://openai.com/index/openai-submits-confidential-s-1/
- **Evidence ID:** EVD-20260611-0003

### INFO-004
- **タイトル:** Built to benefit everyone: our plan
- **ソース:** OpenAI Blog (Sam Altman & Jakub Pachocki)
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI
- **要約:** OpenAI第3フェーズ宣言。AIの自律的研究者構築（2028年3月までに研究の大部分をAIシステムが実行）、経済加速、全人類へのパーソナルAGI提供を3つの主要目標として提示。AGI到達への具体的タイムライン含む。
- **キーファクト:**
  - 2028年3月までに研究の大部分をAIシステムが実行する内部見通し
  - 第3フェーズ: AIを豊富・安価・安全にする段階
  - 3目標: 自動AI研究者、経済加速、パーソナルAGI
  - 国際的なAI調整機関の必要性を提起
- **引用URL:** https://openai.com/index/built-to-benefit-everyone-our-plan/
- **Evidence ID:** EVD-20260611-0004

### INFO-005
- **タイトル:** Introducing the OpenAI Economic Research Exchange
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-04, KIQ-002-02
- **関連企業:** OpenAI
- **要約:** OpenAIが経済研究フォーラム「Economic Research Exchange」を立ち上げ。AIが経済に与える影響に関する研究を促進する取り組み。
- **キーファクト:**
  - AI経済影響研究のためのフォーラム設立
  - 研究コミュニティとの協力体制構築
- **引用URL:** https://openai.com/index/economic-research-exchange/
- **Evidence ID:** EVD-20260611-0005

### INFO-006
- **タイトル:** Dreaming: Better memory for a more helpful ChatGPT
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** ChatGPTに新機能「Dreaming」を実装。より良いメモリ機能により、ユーザーの好みや文脈を長期的に記憶し、パーソナライズされた体験を提供。
- **キーファクト:**
  - ChatGPTのメモリ機能を大幅改善（Dreaming機能）
  - 長期的なユーザーコンテキスト保持の強化
- **引用URL:** https://openai.com/index/chatgpt-memory-dreaming/
- **Evidence ID:** EVD-20260611-0006

### INFO-007
- **タイトル:** Introducing new capabilities to GPT-Rosalind
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** GPT-Rosalindの新機能を発表。医療・バイオ研究分野に特化したGPTモデルの性能向上。
- **キーファクト:**
  - GPT-Rosalindの新機能追加
  - 医療・バイオ研究分野でのAI適用拡大
- **引用URL:** https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/
- **Evidence ID:** EVD-20260611-0007

### INFO-008
- **タイトル:** Codex for every role, tool, and workflow
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** Codexをあらゆる役割・ツール・ワークフローに拡張。開発者だけでなく全職種のユーザー向けにコーディングエージェント機能を提供する戦略。
- **キーファクト:**
  - Codexの適用範囲を全職種・全ツールに拡大
  - 開発環境のロックイン戦略の一環
- **引用URL:** https://openai.com/index/codex-for-every-role-tool-workflow/
- **Evidence ID:** EVD-20260611-0008

### INFO-009
- **タイトル:** Expanding Project Glasswing
- **ソース:** Anthropic Blog
- **公開日:** 2026-06-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** AnthropicがProject Glasswingを約150の新規組織に拡大。15カ国以上の重要インフラ提供者を含む。Claude Mythos Previewを使ったセキュリティ脆弱性スキャンで10,000件以上の高/クリティカル重大度の欠陥を発見済み。6-12ヶ月以内に他社もMythosクラスのモデルを持つと予測。
- **キーファクト:**
  - Glasswingパートナー50→約200組織に拡大（150新規追加）
  - 10,000件以上の高/クリティカル脆弱性を発見済み
  - 6-12ヶ月以内に他社もMythosクラスモデルを持つ予測
  - Claude Security製品もリリース
  - 新規パートナーは電力・水道・医療・通信・ハードウェア業界を含む
- **引用URL:** https://www.anthropic.com/news/expanding-project-glasswing
- **Evidence ID:** EVD-20260611-0009

### INFO-010
- **タイトル:** Introducing the Services Track and Partner Hub of the Claude Partner Network
- **ソース:** Anthropic Blog
- **公開日:** 2026-06-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Partner NetworkにServices Track（Select/Preferred/Global Premierの3階層）とPartner Hubを導入。40,000社以上が応募、10,000人以上がClaude認証取得。Accenture 30,000人、Deloitte 470,000人、KPMG 276,000人等の大規模導入。$100M投資のパートナープログラム。
- **キーファクト:**
  - Services Track: Select/Preferred/Global Premierの3階層パートナー認定
  - 40,000社以上が応募、10,000人以上が認証取得
  - Accenture 30,000人、Cognizant 350,000人、Deloitte 470,000人、KPMG 276,000人規模の展開
  - MCPコネクタ経由でClaudeからパートナー情報にアクセス可能
- **引用URL:** https://www.anthropic.com/news/services-track-partner-hub
- **Evidence ID:** EVD-20260611-0010

### INFO-011
- **タイトル:** I/O 2026: Welcome to the agentic Gemini era
- **ソース:** Google Blog (Sundar Pichai)
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02, KIQ-003-01, KIQ-001-04
- **関連企業:** Google
- **要約:** Google I/O 2026基調講演。月間3.2Q（3,200兆）トークン処理（7x YoY）、8.5M開発者、Gemini 3.5 Flash発表、Gemini Omni（任意入力から任意出力生成）、Gemini Spark（24/7エージェント）、Antigravity 2.0（エージェントオーケストレーション）、TPU 8t/8i、$180-190Bキャップエックス投資計画。
- **キーファクト:**
  - 月間3.2Q+トークン処理（前年比7x）
  - 8.5M開発者が月次利用、19B tokens/分処理
  - Gemini 3.5 Flash: 3.1 Proよりほぼ全ベンチマークで優位、他フロントィア比4x高速
  - Gemini Omni: 任意入力→任意出力の新モデル、Flash版ローンチ済み
  - Gemini Spark: 24/7パーソナルエージェント、仮想マシン上で常時稼働
  - Antigravity 2.0: エージェント管理プラットフォーム、12x高速版Flash
  - TPU 8t/8i: 訓練/推論別チップ、1M+ TPU分散訓練
  - キャップエックス $180-190B（2022年$31Bから6x増）
  - OpenAI・Eleven LabsがSynthID採用
  - Gemini App 900M MAU（前年比2x以上）
- **引用URL:** https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
- **Evidence ID:** EVD-20260611-0011

### INFO-012
- **タイトル:** Gemini 3.5 Flash - frontier intelligence with action
- **ソース:** Google Blog
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-003-01
- **関連企業:** Google
- **要約:** Gemini 3.5 Flashは3.1 Proよりほぼ全ベンチマークで優位。GDPVal（実世界経済タスク）で大幅ジャンプ。他フロントィアモデル比4x高速。トークン予算80%をFlashに移行すれば年間$1B+節約可能。3.5 Proは来月リリース予定。
- **キーファクト:**
  - Gemini 3.1 Pro比ほぼ全ベンチマーク改善
  - GDPVal大幅改善（実世界経済タスク評価）
  - 他フロントィア比4x高速（出力スピード）
  - 同等フロントィア比半額以下
  - 3.5 Pro来月リリース予定
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/
- **Evidence ID:** EVD-20260611-0012

### INFO-013
- **タイトル:** Powering Gopuff's Go agent
- **ソース:** xAI Blog
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIとGopuffがAIショッピングアシスタント「Go」をローンチ。Grokのテキスト・音声・画像モデルを統合。Xとウェブのリアルタイム信号を活用し、13年分の需要インテリジェンスに基づくパーソナライズドカート構築。
- **キーファクト:**
  - Grok text/audio/imageモデルを統合したショッピングアシスタント
  - 13年分の需要インテリジェンス（数億件の注文データ）
  - Grok Imagineによる視覚的ショッピングフィード
  - 米国でiOS/Androidローンチ済み、UK続いて展開
- **引用URL:** https://x.ai/news/grok-gopuff
- **Evidence ID:** EVD-20260611-0013

### INFO-014
- **タイトル:** Grok Imagine 1.5 Preview
- **ソース:** xAI Blog
- **公開日:** 2026-06-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIが画像生成モデルGrok Imagine 1.5のプレビューを発表。
- **キーファクト:**
  - Grok Imagine 1.5 Previewリリース
  - 画像生成品質の向上
- **引用URL:** https://x.ai/news/grok-imagine-1-5
- **Evidence ID:** EVD-20260611-0014

### INFO-015
- **タイトル:** Grok Becomes the Voice of Vapi
- **ソース:** xAI Blog
- **公開日:** 2026-06-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIとVapiが提携。Grok VoiceがVapiの音声AIプラットフォームに統合。音声エージェントAPIの拡大。
- **キーファクト:**
  - Grok VoiceがVapiプラットフォームに統合
  - 音声AIエージェントの外部プラットフォーム展開
- **引用URL:** https://x.ai/news/grok-vapi
- **Evidence ID:** EVD-20260611-0015

### INFO-016
- **タイトル:** Composer 2.5
- **ソース:** xAI Blog
- **公開日:** 2026-06-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI
- **要約:** xAIがComposer 2.5を発表。コーディングエージェントの大幅アップデート。
- **キーファクト:**
  - Composer 2.5リリース
  - コーディングエージェント機能の強化
- **引用URL:** https://x.ai/news/composer-2-5
- **Evidence ID:** EVD-20260611-0016

### INFO-017
- **タイトル:** Grok Build 0.1 on API
- **ソース:** xAI Blog
- **公開日:** 2026-05-29
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** xAI
- **要約:** Grok Build 0.1がAPI経由で利用可能に。$1/MTokの低価格コーディングエージェント。
- **キーファクト:**
  - Grok Build 0.1 API経由で利用可能
  - 低価格戦略（$1/MTok）
- **引用URL:** https://x.ai/news/grok-build-0-1
- **Evidence ID:** EVD-20260611-0017

### INFO-018
- **タイトル:** Anthropic Compute Partnership with xAI (SpaceXAI)
- **ソース:** xAI Blog
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-002-01
- **関連企業:** xAI, Anthropic
- **要約:** SpaceXAIとAnthropicがコンピュートパートナーシップを締結。Colossus 1へのアクセスを提供。競合他社へのインフラ提供という異例の提携。
- **キーファクト:**
  - SpaceXAIがAnthropicにColossus 1へのアクセス提供
  - AI業界のインフラ共有の先例
- **引用URL:** https://x.ai/news/anthropic-compute-partnership
- **Evidence ID:** EVD-20260611-0018

### INFO-019
- **タイトル:** DiffusionGemma: 4x faster text generation
- **ソース:** Google Blog
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-003-01
- **関連企業:** Google
- **要約:** GoogleがDiffusionGemmaを発表。従来比4x高速なテキスト生成。拡散モデルをテキスト生成に応用した新アーキテクチャ。
- **キーファクト:**
  - 拡散モデルベースのテキスト生成で4x高速化
  - Gemmaシリーズの新アプローチ
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/
- **Evidence ID:** EVD-20260611-0019

### INFO-020
- **タイトル:** ByteDance's Coze Launches Version 2.5 - Agent World Ecosystem
- **ソース:** KuCoin News
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのCozeがv2.5をローンチ。AIエージェントがチャットインターフェースを超えて動作する「Agent World」エコシステムを導入。独立した実行環境、スキル、アイデンティティを持つエージェントを可能にする。
- **キーファクト:**
  - Coze 2.5がチャット外のエージェント実行を可能に
  - Agent Worldエコシステム導入
  - 独立実行環境・スキル・アイデンティティ機能
- **引用URL:** https://www.kucoin.com/news/flash/bytedance-s-coze-launches-version-2-5-introduces-agent-world-ecosystem
- **Evidence ID:** EVD-20260611-0020

### INFO-021
- **タイトル:** ByteDance releases DeerFlow 2.0 - multi-agent super agent
- **ソース:** Instagram (via search)
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0をリリース。複数AIエージェントを生成し、コード実行、レポート・プレゼン・ウェブサイト構築が可能なスーパーエージェント。
- **キーファクト:**
  - 複数エージェントを生成可能なスーパーエージェント
  - コード実行・レポート・プレゼン・ウェブサイト構築対応
- **引用URL:** https://www.instagram.com/reel/DZKkK6LJB1Q/
- **Evidence ID:** EVD-20260611-0021

### INFO-022
- **タイトル:** Google Gemini Interactions API - Agentic Workflows
- **ソース:** Google AI for Developers
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google
- **要約:** Google Gemini Interactions APIがエージェントワークフロー向けに最適化。サーバーサイド状態管理、複雑なマルチモーダル・マルチターン会話をサポート。Gemini 3.1 ProではSWE・エージェント能力が改善。
- **キーファクト:**
  - Interactions API: エージェントワークフロー最適化
  - サーバーサイド状態管理・マルチモーダル対応
  - Gemini 3.1 ProでSWE・エージェント能力改善
- **引用URL:** https://ai.google.dev/gemini-api/docs/interactions/interactions-overview
- **Evidence ID:** EVD-20260611-0022

### INFO-023
- **タイトル:** The AI Agents Report - LinkedIn
- **ソース:** LinkedIn
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI, Google, NVIDIA
- **要約:** NVIDIAがローカルハードウェアへのAIエージェント展開を推進。Googleがエージェントにエンタープライズデータベースへのダイレクトアクセスを提供。OpenAIがCodexを開発者以外にも拡大中。
- **キーファクト:**
  - NVIDIA: ローカルハードウェアでのAIエージェント実行
  - Google: エージェントのエンタープライズDB直接アクセス
  - OpenAI: Codexを開発者以外の職種に拡大
- **引用URL:** https://www.linkedin.com/pulse/ai-agents-report-rakesh-gohel-nyswe
- **Evidence ID:** EVD-20260611-0023

### INFO-024
- **タイトル:** Mastercard launches Agent Pay for Machines
- **ソース:** Mastercard
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** Mastercard
- **要約:** MastercardがAIエージェント向け決済「Agent Pay for Machines」をローンチ。エージェントコマースの実用化。ビジネスがAIエージェントからの支払いを受け付け可能に。
- **キーファクト:**
  - AIエージェント向け決済インフラ新設
  - エージェントコマースの実用化
- **引用URL:** https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
- **Evidence ID:** EVD-20260611-0024

### INFO-025
- **タイトル:** Visa and OpenAI: Building the future of AI commerce
- **ソース:** Visa Corporate
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** OpenAI, Visa
- **要約:** VisaがVisa Payments ForumでOpenAIとの戦略的提携を発表。エージェントコマースをメインストリームに持ち込む計画。
- **キーファクト:**
  - Visa-OpenAI戦略的提携発表
  - エージェントコマースのメインストリーム化狙う
- **引用URL:** https://corporate.visa.com/en/sites/visa-perspectives/innovation/visa-openai-partnership.html
- **Evidence ID:** EVD-20260611-0025

### INFO-026
- **タイトル:** Gartner Report: How to Secure Enterprise Agentic AI
- **ソース:** Quisitive/Gartner
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** (業界全体)
- **要約:** GartnerがエンタープライズAgentic AIのセキュリティに関する研究報告書を発表。CIO/CISO向けに、サイバーセキュリティプログラムがエージェントAIにどう対応すべきかを分析。
- **キーファクト:**
  - GartnerがエージェントAIのエンタープライズセキュリティガイド発行
  - CIO/CISO向け対応フレームワーク提示
- **引用URL:** https://quisitive.com/secure-enterprise-ai-gartner-research-report/
- **Evidence ID:** EVD-20260611-0026

### INFO-027
- **タイトル:** SkillsMP - Largest AI Skills Marketplace (>1.6M Skills)
- **ソース:** Product Market Fit
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** (業界全体)
- **要約:** SkillsMPが160万以上のエージェントスキルをインデックスするスキルマーケットプレイス。23の職業グループ、867の職種カテゴリに対応。AIエージェントスキルのエコシステム急速拡大を示す。
- **キーファクト:**
  - 160万以上のエージェントスキルがインデックス済み
  - 23職業グループ・867職種カテゴリ対応
  - Claude Code/Codex/ChatGPT等のSKILL.mdツール対応
- **引用URL:** https://www.productmarketfit.tech/p/the-largest-ai-skills-marketplace
- **Evidence ID:** EVD-20260611-0027

### INFO-028
- **タイトル:** Google Gemini Skills and Agents CLI
- **ソース:** GitHub
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Google
- **要約:** Googleがgemini-skillsリポジトリとagents-cliを公開。Gemini API/SDK用のスキル集と、Gemini Enterprise Agent Platform用のCLIツール。
- **キーファクト:**
  - Gemini Skills: エージェントにコンテキストを追加する軽量スキル
  - agents-cli: Gemini Enterprise Agent Platform用開発CLI
  - ADK（Agent Development Kit）パターンを提供
- **引用URL:** https://github.com/google-gemini/gemini-skills
- **Evidence ID:** EVD-20260611-0028

### INFO-029
- **タイトル:** How to Build Enterprise AI Agent Platform Without Vendor Lock-In
- **ソース:** VDF.ai
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** (業界全体)
- **要約:** エンタープライズAIエージェントプラットフォーム構築におけるベンダーロックイン回避ガイド。ロックインは単一決定ではなく5層にわたって蓄積し、各層がスイッチングコストを引き上げる構造を分析。
- **キーファクト:**
  - ロックインは5層で蓄積する構造
  - 各層がスイッチングコストを段階的に引き上げ
- **引用URL:** https://vdf.ai/blog/build-enterprise-ai-agent-platform-without-vendor-lock-in/
- **Evidence ID:** EVD-20260611-0029

### INFO-030
- **タイトル:** AI Agent switching cost higher than cloud
- **ソース:** X (Twitter)
- **公開日:** 2026-06-11
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** (業界全体)
- **要約:** AIエージェントベンダーのスイッチングコストはクラウドよりも高いとの指摘。ロックインはインフラではなく推論にあり、モデル切替は全ての発見のやり直しを意味する。
- **キーファクト:**
  - AIベンダーのスイッチングコストはクラウドより高い
  - ロックインはインフラではなく推論レイヤーにある
- **引用URL:** https://x.com/saen_dev/status/2064742558832447989
- **Evidence ID:** EVD-20260611-0030

### INFO-031
- **タイトル:** Multimodal AI Benchmarks 2026 - Gemini 3 Pro Deep Think leads
- **ソース:** BenchLM
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google, xAI
- **要約:** 2026年6月時点のマルチモーダルベンチマークでGemini 3 Pro Deep Thinkが100.0%、Grok 4.1が97.8%でトップ。MMMU/OfficeQA/CharXiv等のマルチモーダルグラウンデッド評価。
- **キーファクト:**
  - Gemini 3 Pro Deep Think: マルチモーダル重視スコア100.0%（暫定）
  - Grok 4.1: 97.8%
  - MMMU/OfficeQA/CharXiv等の複合評価
- **引用URL:** https://benchlm.ai/multimodal-grounded
- **Evidence ID:** EVD-20260611-0031

### INFO-032
- **タイトル:** AI Benchmarks 2026 - MMLU ceiling reached (>88% for all frontier)
- **ソース:** Kili Technology
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** (業界全体)
- **要約:** 全フロントィアLLMがMMLUで88%以上を達成し、MMLUが天井に達したことを確認。GPT-5.3 Codexがリード。MMLUはAI進歩の指標としての限界が明確化。
- **キーファクト:**
  - 全フロントィアLLMがMMLU 88%超
  - GPT-5.3 Codexがトップスコア
  - MMLUの天井効果確認
- **引用URL:** https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough
- **Evidence ID:** EVD-20260611-0032

### INFO-033
- **タイトル:** Mobile AI Agents Tested Across 65 Real-World Tasks
- **ソース:** AIMultiple
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** (業界全体)
- **要約:** 4つのモバイルAIエージェント（DroidRun, Mobile-Agent, AutoDroid, AppAgent）を65の実世界タスクでベンチマーク。モバイル環境でのエージェント自律性評価。
- **キーファクト:**
  - 4モバイルAIエージェントを65タスクで比較
  - Androidエミュレータでの実世界ベンチマーク
- **引用URL:** https://aimultiple.com/mobile-ai-agent
- **Evidence ID:** EVD-20260611-0033

### INFO-034
- **タイトル:** Enterprise AI Rollout Failures: Causes and Case Studies
- **ソース:** Intuition Labs
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** エンタープライズAI展開失敗の体系的要因を分析。データ準備不足、不適切な統合、過剰なハイプがROIに与える影響を調査。
- **キーファクト:**
  - データ準備不足・統合の欠陥・過剰ハイプが主要失敗要因
  - AI ROIへの影響を体系的に分析
- **引用URL:** https://intuitionlabs.ai/articles/enterprise-ai-rollout-failures
- **Evidence ID:** EVD-20260611-0034

### INFO-035
- **タイトル:** Claude Fable 5 available in Microsoft Foundry
- **ソース:** Azure Blog
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** Microsoft, Anthropic
- **要約:** Microsoft FoundryでClaude Fable 5が利用可能に。長時間実行タスク・エンタープライズワークフロー向けの高度エージェント機能を提供。
- **キーファクト:**
  - Claude Fable 5がMicrosoft Foundryで利用開始
  - 長時間実行タスク向け自律エージェント機能
- **引用URL:** https://azure.microsoft.com/en-us/blog/claude-fable-5-is-now-available-in-microsoft-foundry-powering-the-next-era-of-autonomous-agents/
- **Evidence ID:** EVD-20260611-0035

### INFO-036
- **タイトル:** AWS Bedrock AgentCore - Security/Governance updates
- **ソース:** Scale Factory
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** Amazon Bedrock AgentCore Policy/Evaluationsが2026年3月にGA到達。Agent Registryが2026年4月に追加。エージェント管理インフラの急速な整備進行中。
- **キーファクト:**
  - AgentCore Policy/Evaluations: 2026年3月GA
  - Agent Registry: 2026年4月追加
  - エージェント管理インフラの急速整備
- **引用URL:** https://scalefactory.com/amazon-bedrock-six-months-of-security-and-governance-updates-worth-knowing-about/
- **Evidence ID:** EVD-20260611-0036

### INFO-037
- **タイトル:** Agentic AI Statistics 2026 - Gartner: 40% enterprise apps include AI agents
- **ソース:** Unico Connect
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Gartner予測: 2026年末までにエンタープライズアプリの40%にタスク特化型AIエージェントが組み込まれる（2025年は5%未満）。但し導入≠本番運用。
- **キーファクト:**
  - 2026年末: エンタープライズアプリの40%にAIエージェント（2025年<5%）
  - 17%の組織のみAIエージェントをデプロイ済み
  - 60%以上がデプロイ予定
- **引用URL:** https://unicoconnect.com/blogs/agentic-ai-statistics-2026
- **Evidence ID:** EVD-20260611-0037

### INFO-038
- **タイトル:** Fortune: AI agents are flattening corporate hierarchies
- **ソース:** Fortune
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Fortune誌がAIエージェントによる企業階層の平坦化を報道。Korn Ferry調査で41%の従業員が昨年企業が管理レイヤーを削減したと回答。McKinsey: 62%がAIエージェントを試験中だが33%のみスケール超え。
- **キーファクト:**
  - 41%の従業員が管理レイヤー削減を経験（Korn Ferry）
  - 62%がAIエージェント試験中、33%のみスケール超え（McKinsey）
  - EBITインパクトを見るのはわずか6%
- **引用URL:** https://fortune.com/2026/06/09/ai-agents-flattening-corporate-hierarchies-companies-managers-develop-new-playbook/
- **Evidence ID:** EVD-20260611-0038

### INFO-039
- **タイトル:** 25% of enterprise AI agent deployments fail ROI expectations
- **ソース:** ITSM.tools / KTSL & BMC Helix
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** KTSLとBMC Helixの調査で、英国大企業のAIエージェントデプロイメントの25%がROI期待に未到達。ROI計測手法の不備とコスト構造の誤解が主要因。
- **キーファクト:**
  - 英国大企業の25%がAIエージェントROI未達成
  - ROI計測手法の不備が主要因
- **引用URL:** https://itsm.tools/ai-agent-deployment/
- **Evidence ID:** EVD-20260611-0039

### INFO-040
- **タイトル:** Anthropic vs Pentagon - Supply Chain Risk Designation Update
- **ソース:** Reuters
- **公開日:** 2026-06-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** トランプ政権がAnthropicへの不当な報復を否定。連邦控訴裁がAnthropicのサプライチェーンリスク指定の一時停止請求を却下済み。2件目の訴訟がワシントンDCで進行中。自律兵器拒否が指定の背景とされる。
- **キーファクト:**
  - トランプ政権が報復を否定
  - 連邦控訴裁が一時停止請求却下
  - 自律兵器拒否がSCR指定の背景
  - 2件目の訴訟がワシントンDCで進行中
- **引用URL:** https://www.reuters.com/legal/litigation/trump-administration-denies-unlawful-retaliation-anthropic-ai-blacklisting-2026-06-09/
- **Evidence ID:** EVD-20260611-0040

### INFO-041
- **タイトル:** The Pentagon is rewriting how it buys AI
- **ソース:** Federal News Network
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** (米政府)
- **要約:** ペンタゴンがAI調達方法を抜本的に見直し中。AI企業との関係構造そのものが問われている。将来の戦争の主導権を握る技術調達の再設計。
- **キーファクト:**
  - ペンタゴンAI調達の抜本的見直し
  - 技術調達が戦争の主導権を決定する構造
- **引用URL:** https://federalnewsnetwork.com/commentary/2026/06/the-pentagon-is-rewriting-how-it-buys-ai-control-of-the-future-of-warfare/
- **Evidence ID:** EVD-20260611-0041

### INFO-042
- **タイトル:** White House Executive Order on Advanced AI Innovation and Security (June 2, 2026)
- **ソース:** Inside Government Contracts
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** (米政府)
- **要約:** ホワイトハウスが6月2日に「先進AIイノベーションと安全保障の促進」大統領令を発令。フロンティアAIモデルの透明性要求、独立監査、連邦優先権を含む。
- **キーファクト:**
  - 2026年6月2日大統領令発令
  - フロンティアAIの透明性要求・独立監査・連邦優先権
  - サイバーセキュリティリスクに焦点
- **引用URL:** https://www.insidegovernmentcontracts.com/2026/06/white-house-releases-executive-order-on-advanced-ai-innovation-and-security/
- **Evidence ID:** EVD-20260611-0042

### INFO-043
- **タイトル:** China preparing 2 trillion yuan AI investment as national security
- **ソース:** Instagram (via search)
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-03, KIQ-003-04
- **関連企業:** (中国政府)
- **要約:** 中国が約2兆元（約2950億ドル）のAI投資を準備中。AIをビジネス分野から国家安全保障の問題に位置づける大きな転換。
- **キーファクト:**
  - 2兆元（約2950億ドル）のAI投資準備
  - AIを国家安全保障の問題に位置付け
- **引用URL:** https://www.instagram.com/reel/DZZdnUYir7C/
- **Evidence ID:** EVD-20260611-0043

### INFO-044
- **タイトル:** Pentagon partners with Scale AI for Thunderforge military AI agents
- **ソース:** Facebook (Interesting Engineering)
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Scale AI, (米政府)
- **要約:** ペンタゴンがScale AIと「Thunderforge」イニシアチブで提携。AIエージェントを軍事戦略・作戦に統合する取り組み。
- **キーファクト:**
  - ペンタゴン-Scale AI提携「Thunderforge」
  - AIエージェントの軍事戦略統合
- **引用URL:** https://www.facebook.com/interestingengineering/posts/the-pentagon-is-betting-that-the-next-war-wont-be-decided-by-who-has-the-most-fi/1456225676548865/
- **Evidence ID:** EVD-20260611-0044

### INFO-045
- **タイトル:** Democratic lawmakers introduce bills to curb Pentagon AI use
- **ソース:** MeriTalk
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** (米政府)
- **要約:** 民主党議員がペンタゴンのAI使用を制限する法案を提出。戦争・核運用・国内監視でのAI使用に新たな制限を課す内容。軍事AIへの監視強化を求める動き。
- **キーファクト:**
  - 戦争・核運用・国内監視でのAI使用制限法案
  - 軍事AIの議会監視強化
- **引用URL:** https://www.meritalk.com/articles/democratic-lawmakers-introduce-bills-to-curb-pentagon-ai-use/
- **Evidence ID:** EVD-20260611-0045

### INFO-046
- **タイトル:** Anthropic refused autonomous weapons - now excluded from Pentagon
- **ソース:** Instagram
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicが自律兵器の軍事ユースケースへの協力を拒否した後、ペンタゴンから除外された。AI倫理の正念場として注目されている事例。
- **キーファクト:**
  - Anthropicが自律兵器ユースケースへの協力拒否
  - 拒否後にペンタゴンから除外
  - AI倫理の正念場としての注目
- **引用URL:** https://www.instagram.com/p/DZTBbbhEcoi/
- **Evidence ID:** EVD-20260611-0046

### INFO-047
- **タイトル:** Great American AI Act - transparency and federal preemption
- **ソース:** DLA Piper
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** (米政府)
- **要約:** 「Great American AI Act」法案が起草。フロンティアAIモデルへの透明性要求、独立監査メカニズム、連邦優先権（州法の先取り）を含む。
- **キーファクト:**
  - フロンティアAI透明性要求・独立監査・連邦優先権
  - 269頁の包括的法案
- **引用URL:** https://www.dlapiper.com/insights/publications/2026/06/unpacking-the-great-american-ai-act
- **Evidence ID:** EVD-20260611-0047

### INFO-048
- **タイトル:** Agent-as-a-Service replacing SaaS
- **ソース:** Towards Agentic AI
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** (業界全体)
- **要約:** Agent-as-a-Service (AaaS) がSaaSを置き換えるパラダイムシフト。AIエージェントが自律的に計画・推論・ツール使用・行動実行する新しいソフトウェア配信モデル。
- **キーファクト:**
  - AaaSパラダイム: SaaSからの移行
  - 自律的計画・推論・ツール使用・行動実行
- **引用URL:** https://towardsagenticai.com/agent-as-a-service-how-aaas-is-replacing-saas/
- **Evidence ID:** EVD-20260611-0048

### INFO-049
- **タイトル:** AI is breaking the career ladder - UNSW
- **ソース:** UNSW
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-02
- **関連企業:** (業界全体)
- **要約:** UNSW研究: AIが職業のラダーを破壊。エントリーレベルの削減が将来のスキル不足を生む。カスタマーサービス・マーケティング・ソフトウェア開発が最も影響を受ける分野。
- **キーファクト:**
  - エントリーレベル削減が将来のスキル不足を生む構造
  - カスタマーサービス・マーケティング・開発が最も影響
- **引用URL:** https://www.unsw.edu.au/newsroom/news/2026/06/is-ai-breaking-the-career-ladder
- **Evidence ID:** EVD-20260611-0049

### INFO-050
- **タイトル:** IDC: Agentic AI is breaking your ROI model
- **ソース:** IDC
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** IDCが6柱フレームワークでAgentic AIのROI計測問題を分析。価値は非線形、コストは動的。従来のROIモデルではAgentic AIを正しく評価できない。
- **キーファクト:**
  - 価値は非線形、コストは動的
  - 従来ROIモデルの限界を指摘
  - 6柱評価フレームワーク提案
- **引用URL:** https://www.idc.com/resource-center/blog/agentic-ai-is-breaking-your-roi-model-heres-how-to-fix-it/
- **Evidence ID:** EVD-20260611-0050

### INFO-051
- **タイトル:** DeepSeek V4 Pro beats GPT-5.5 Pro on precision (Hacker News)
- **ソース:** Hacker News
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03, KIQ-003-02
- **関連企業:** DeepSeek, OpenAI
- **要約:** DeepSeek V4 ProがGPT-5.5 Proを精度で上回る。最大の価値は低価格。75%値下げと同等以上の精度でコモディティ化圧力を強める。
- **キーファクト:**
  - DeepSeek V4 Pro > GPT-5.5 Pro（精度評価）
  - 低価格が最大の価値提案
  - オープンソース/オープンウェイトモデルの競争力向上
- **引用URL:** https://news.ycombinator.com/item?id=48440448
- **Evidence ID:** EVD-20260611-0051

### INFO-052
- **タイトル:** ARC Challenge Leaderboard - GPT-5 leads at 96.3%
- **ソース:** PricePerToken
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** ARC ChallengeベンチマークでGPT-5が96.3%でトップ。GLM 5が96.0%で追従。37モデルが評価済み。
- **キーファクト:**
  - GPT-5: ARC Challenge 96.3%（1位）
  - GLM 5: 96.0%（2位）
  - 37モデルが評価対象
- **引用URL:** https://pricepertoken.com/leaderboards/benchmark/arc-challenge
- **Evidence ID:** EVD-20260611-0052

### INFO-053
- **タイトル:** MMLU saturated above 88% - benchmark meaningless at top
- **ソース:** Kili Technology
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** (業界全体)
- **要約:** MMLU/MMLU-ProがフロンティアAIで88%以上で機能的に飽和。トップのスコア差は統計的に無意味。新しい評価基準の必要性。
- **キーファクト:**
  - MMLU/MMLU-Pro 88%以上で飽和
  - トップスコア差は統計的に無意味
- **引用URL:** https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough
- **Evidence ID:** EVD-20260611-0053

### INFO-054
- **タイトル:** GPT-5.5 vs Claude Opus 4.7 vs Grok 4.3 comparison
- **ソース:** MorphLLM
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, xAI
- **要約:** GPT-5.5は数学とエコシステムでリード。Claude Opus 4.7はコーディングとライティングでリード。Grok 4.3はリアルタイムデータと安価なAPIでリード。3つのフロンティアで異なる強み。
- **キーファクト:**
  - GPT-5.5: 数学・エコシステム首位
  - Claude Opus 4.7: コーディング・ライティング首位
  - Grok 4.3: リアルタイムデータ・低価格API首位
- **引用URL:** https://www.morphllm.com/comparisons/chatgpt-vs-claude-vs-grok
- **Evidence ID:** EVD-20260611-0054

### INFO-055
- **タイトル:** Google's Backstops Underpin $35 Billion Chip Deal for Anthropic
- **ソース:** Bloomberg
- **公開日:** 2026-06-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Google, Anthropic
- **要約:** Googleが各拠点のリース支払いをバックストップし、Anthropicが実質$35Bのローンを獲得。AIインフラ投資の前例のない規模。
- **キーファクト:**
  - GoogleがAnthropicの$35Bチップ取引をバックストップ
  - 各拠点のリース支払いをGoogleが保証
  - AIインフラ投資の前例のない規模
- **引用URL:** https://www.bloomberg.com/news/articles/2026-06-09/google-s-backstops-underpin-35-billion-chip-deal-for-anthropic
- **Evidence ID:** EVD-20260611-0055

### INFO-056
- **タイトル:** OpenAI plans stock market debut - BBC
- **ソース:** BBC
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIが株式市場デビューを計画しAnthropicとの新たな競争が始まる。Anthropicは今年上半期の黒字化を投資家に伝えている。
- **キーファクト:**
  - OpenAI上場計画とAnthropicとの競争激化
  - Anthropic今年上半期黒字化見通し
- **引用URL:** https://www.bbc.com/news/articles/cd958eqg1n5o
- **Evidence ID:** EVD-20260611-0056

### INFO-057
- **タイトル:** Anthropic overtakes OpenAI as most valuable AI startup - $965B valuation
- **ソース:** Instagram (via search)
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, OpenAI
- **要約:** Anthropicが$65Bの資金調達で評価額$965Bに到達し、OpenAIを抜いて世界最高値のAIスタートアップに。
- **キーファクト:**
  - $65B調達で$965B評価額
  - OpenAIを抜いて世界最高値AIスタートアップに
- **引用URL:** https://www.instagram.com/p/DZXh4mVlScq/
- **Evidence ID:** EVD-20260611-0057

### INFO-058
- **タイトル:** Meta signs AI data center deal in India with Reliance - 168MW
- **ソース:** TechCrunch
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Meta
- **要約:** MetaがReliance Industriesと168MWのAI対応データセンター契約を締結。インドでの初のAIインフラ投資。$100M合弁。
- **キーファクト:**
  - 168MW AIデータセンターをインドに建設
  - $100M合弁
  - Metaのインド初AIインフラ投資
- **引用URL:** https://techcrunch.com/2026/06/10/meta-signs-first-ai-data-center-deal-in-india-with-reliance/
- **Evidence ID:** EVD-20260611-0058

### INFO-059
- **タイトル:** Alphabet raises $85B for AI infrastructure
- **ソース:** YouTube (via search)
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Google
- **要約:** AlphabetがAIインフラ向けにほぼ$85Bを調達。SpaceX、OpenAI、Anthropicの上場前にAIインフラ投資を先行。
- **キーファクト:**
  - $85B AIインフラ調達
  - 競合上場前にインフラ投資先行
- **引用URL:** https://www.youtube.com/watch?v=43KCI_4A_gs
- **Evidence ID:** EVD-20260611-0059

### INFO-060
- **タイトル:** Mistral selling open-weight models to enterprises and governments
- **ソース:** Forbes AI 50
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral
- **要約:** Forbes AI 50リストでMistralが選出。オープンウェイトモデルをCisco等の大企業やヨーロッパ政府機関に販売。オープンウェイトの柔軟性がエンタープライズで評価。
- **キーファクト:**
  - MistralがCisco等の大企業とヨーロッパ政府に販売
  - オープンウェイトの柔軟性がエンタープライズで評価
- **引用URL:** https://www.forbes.com/lists/ai50/
- **Evidence ID:** EVD-20260611-0060

### INFO-061
- **タイトル:** Anthropic IPO: Platform switching cost analysis
- **ソース:** Klover AI
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** Anthropic
- **要約:** Anthropic IPOの分析: スイッチングコストは「より良いモデルを見つけるコスト」ではなく「全ビジネスプロセスを再エンジニアリングするコスト」。プラットフォーム関係としてのロックイン構造を分析。
- **キーファクト:**
  - スイッチングコストは全プロセスの再エンジニアリング
  - モデル切替≠プラットフォーム切替
- **引用URL:** https://www.klover.ai/anthropic_ipo_platform_vs_product_comprehensive_research_2026/
- **Evidence ID:** EVD-20260611-0061

### INFO-062
- **タイトル:** AI Is Now The Leading Reason Cited For Layoffs - Forbes
- **ソース:** Forbes
- **公開日:** 2026-06-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** AIがレイオフの理由として市場・経済条件を抜いて1位に。5月だけで38,579件のAI関連削減、年初来87,714件。テクノロジー業界は今年123,000人を削減。
- **キーファクト:**
  - AIがレイオフ理由の1位（市場・経済条件抜く）
  - 5月: 38,579件AI関連削減、年初来: 87,714件
  - テクノロジー業界123,000人削減
- **引用URL:** https://www.forbes.com/sites/maryroeloffs/2026/06/04/tech-industry-loses-123000-jobs-this-year-ai-is-the-most-cited-reason-for-layoffs/
- **Evidence ID:** EVD-20260611-0062

### INFO-063
- **タイトル:** China Inc deploys quiet layoffs as Beijing promotes AI adoption
- **ソース:** Reuters
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-04
- **関連企業:** (中国業界)
- **要約:** 中国企業が「静かな」レイオフを展開。AIツールが役割を代替する中、大規模解雇を避けて段階的に削減。労働法と政治的配慮が背景。
- **キーファクト:**
  - 中国企業のAI代替による静かなレイオフ
  - 段階的削減で安定性維持
  - 労働法・政治的配慮が背景
- **引用URL:** https://www.reuters.com/business/world-at-work/china-inc-deploys-quiet-layoffs-beijing-promotes-ai-adoption-2026-06-10/
- **Evidence ID:** EVD-20260611-0063

### INFO-064
- **タイトル:** Klarna reversed AI-first pivot - service quality dropped
- **ソース:** Facebook / Prymage
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna
- **要約:** Klarnaが700人をAIで置き換えたが品質低下・成長減速で逆戻り。2023年から5,500人→3,800人に自然減らし、AIで補完する戦略だったがサービス品質が悪化。
- **キーファクト:**
  - 700人AI置換後に品質低下・成長減速
  - ヘッドカウント5,500→3,800に自然減
  - AIファースト戦略の逆戻り事例
- **引用URL:** https://prymage.com/insights/is-ai-saving-money-or-costing-more
- **Evidence ID:** EVD-20260611-0064

### INFO-065
- **タイトル:** AI Coding Statistics - 91% adoption, 20M+ Copilot users
- **ソース:** Panto AI
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** GitHub, Microsoft
- **要約:** 135,000人以上の開発者の91%がAIツール使用または計画中。GitHub Copilotの全時間ユーザー数20M+。51%のGitHubコミットがAI支援を含む（MIT研究）。
- **キーファクト:**
  - 開発者91%がAI使用・計画中
  - Copilot 20M+ユーザー
  - 51%のGitHubコミットにAI支援（MIT）
- **引用URL:** https://www.getpanto.ai/blog/ai-coding-assistant-statistics
- **Evidence ID:** EVD-20260611-0065

### INFO-066
- **タイトル:** Gartner AI coding market $9.8-11B annualized
- **ソース:** Virtualization Review
- **公開日:** 2026-06-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02, KIQ-003-01
- **関連企業:** (業界全体)
- **要約:** Gartner推定: エンタープライズAIコーディングエージェント市場は年間$9.8-11B（2026年4月時点）。AI企業がクラウド巨人をGartnerリーダー象限から押し出す構造変化。
- **キーファクト:**
  - AIコーディングエージェント市場年間$9.8-11B
  - AI企業がGartnerリーダー象限を獲得
- **引用URL:** https://virtualizationreview.com/articles/2026/06/05/ai-firms-push-cloud-giants-from-leaders-quadrant-in-gartner-ai-coding-report.aspx
- **Evidence ID:** EVD-20260611-0066

### INFO-067
- **タイトル:** Entry-level software developer jobs dropped 20% for under-26
- **ソース:** Instagram / WION
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** (業界全体)
- **要約:** 26歳未満のエントリーレベルソフトウェア開発者雇用が20%減少。30歳以上の開発者は同時期に増加。AI代替が若年層に集中する構造。
- **キーファクト:**
  - 26歳未満のエントリーレベル開発者雇用20%減
  - 30歳以上の開発者は増加
  - AI代替の影響が若年層に集中
- **引用URL:** https://www.instagram.com/reel/DZUvhSHyx9m/
- **Evidence ID:** EVD-20260611-0067

### INFO-068
- **タイトル:** SoftBank Son: AI designing OpenAI's next model - superintelligence sooner than 10 years
- **ソース:** CNBC
- **公開日:** 2026-06-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI, SoftBank
- **要約:** SoftBank孫社長が「10年でASI到達」という自身の予測を「保守的すぎる」と訂正。AIがOpenAIの次のモデルを設計していることを示唆。
- **キーファクト:**
  - 孫社長: ASI 10年予測を「保守的」と訂正
  - AIがOpenAI次期モデルを設計中
- **引用URL:** https://www.cnbc.com/2026/06/05/softbank-masayoshi-son-openai-model-super-intelligence.html
- **Evidence ID:** EVD-20260611-0068

### INFO-069
- **タイトル:** AGI timeline consensus: Amodei 2027, Hassabis 2030, Altman "in view"
- **ソース:** LinkedIn / multiple
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** AGIタイムライン予測の比較: Amodei 2027年、Hassabis 2029-30年、Altman 「すでに視界に入っている」。Suleyman 18ヶ月でホワイトカラー自動化。
- **キーファクト:**
  - Amodei: 2027年（Altmanより3年早い）
  - Hassabis: 2030年±1年
  - Suleyman: 18ヶ月でホワイトカラー自動化
  - Eric Schmidt: AIが制御不能になるリスク警告
- **引用URL:** https://www.linkedin.com/posts/brad-wolfe-b912047_the-three-people-most-responsible-for-building-activity-7469885979059703808-c13U
- **Evidence ID:** EVD-20260611-0069

### INFO-070
- **タイトル:** 豆包(Doubao) MAU 3.45億 - 中国C端AI首位
- **ソース:** 凤凰网 (ifeng)
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** QuestMobileデータ: 2026年Q1時点で豆包App月活3.45億。国内C端AI首位。2位〜5位（千問・DeepSeek・元宝等）の合計に相当。但し5月MAU 3.3億に減少、607万ユーザー流失。有料版発表後の逆風。
- **キーファクト:**
  - 豆包MAU 3.45億（2026Q1、QuestMobile）
  - 中国C端AI圧倒的首位
  - 5月MAU 3.3億に減少、607万流失
  - 有料版導入がユーザー離れの trigger
- **引用URL:** https://h5.ifeng.com/c/vivoArticle/v002fMOs100Jc0AVxZ8HB-_oyCIlD7PxP8N16SIlq-_ONrMF0__?isNews=1&showComments=0
- **Evidence ID:** EVD-20260611-0070

### INFO-071
- **タイトル:** Coze 3.0上线 - 多Agent协作"AI团队"模式
- **ソース:** 什么值得买 (smzdm)
- **公開日:** 2026-06-06
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDance旗下Coze（扣子）3.0版本6月6日正式上线。核心升级: 多Agent协作的「AI团队」模式。串联・并联・调度三种协作模式。自然语言编程免费公测。
- **キーファクト:**
  - Coze 3.0: 多Agent协作「AI团队」モード
  - 串联・并联・调度の3協作モード
  - 自然言語プログラミング無料公開テスト
- **引用URL:** https://post.m.smzdm.com/p/awweq3w4/
- **Evidence ID:** EVD-20260611-0071

### INFO-072
- **タイトル:** ByteDance AI制药业务启动拆分与独立融资
- **ソース:** 东方财富 / 新浪财经
- **公開日:** 2026-06-10
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** ByteDanceのAI創薬事業が分社化・独立資金調達を開始。ByteDanceは新会社を引き続き支配。コアチーム・アルゴリズム・技術プラットフォーム・パイプライン資産を新主体に移管。
- **キーファクト:**
  - AI創薬事業の分社化・独立資金調達開始
  - ByteDanceは新会社を支配継続
  - コアチーム・技術・パイプライン資産を移管
- **引用URL:** http://finance.eastmoney.com/a/202606103766585451.html
- **Evidence ID:** EVD-20260611-0072

### INFO-073
- **タイトル:** Seedance 2.0 视频生成模型 - API公开
- **ソース:** 火山引擎 (volcengine)
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** Seedance 2.0動画生成モデルのAPIが火山引擎プラットフォームで公開。画像+テキストから高品質動画を生成。豆包Appにも統合済み。
- **キーファクト:**
  - Seedance 2.0 API: 画像+テキスト→動画生成
  - 火山引擎プラットフォームで提供
  - 豆包Appにも統合済み
- **引用URL:** https://www.volcengine.com/docs/82379/1520757
- **Evidence ID:** EVD-20260611-0073

### INFO-074
- **タイトル:** Seed 3D V2.0 - ByteDance second-gen 3D model
- **ソース:** Atlas Cloud
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDance第2世代3D生成基盤モデルSeed3D V2.0が2026年4月23日リリース。単一画像・動画から3D生成。
- **キーファクト:**
  - Seed3D V2.0: 第2世代3D生成モデル
  - 単一画像・動画からの3D生成
  - 2026年4月23日リリース
- **引用URL:** https://www.atlascloud.ai/zh/models/seed-3d
- **Evidence ID:** EVD-20260611-0074

### INFO-075
- **タイトル:** Anthropic IPO filing - $965B valuation, $65B round
- **ソース:** SmarterX / Stark Insider
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04, KIQ-NEW-01
- **関連企業:** Anthropic
- **要約:** AnthropicがIPO申請。$65B調達で$965B評価。年間収益$47B超。安全性研究を目的に設立された企業。OpenAIも同週にS-1提出。
- **キーファクト:**
  - IPO申請（OpenAIと同週）
  - $65B調達・$965B評価額
  - 年間収益$47B超
  - 安全性研究目的で設立
- **引用URL:** https://smarterx.ai/smarterxblog/anthropic-ipo-recursive-self-improvement?hsLang=en
- **Evidence ID:** EVD-20260611-0075

### INFO-076
- **タイトル:** Cloud market share Q1 2026 - AWS 28-32%, Azure 21%, Google gaining
- **ソース:** Instagram / Finout
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-GOO-001
- **関連企業:** Amazon, Microsoft, Google
- **要約:** Q1 2026クラウド市場シェア: AWS 28-32%、Azure 21%、Googleが特定領域でシェア獲得中。3社で市場を独占する構造は継続。
- **キーファクト:**
  - AWS: 28-32%（リーダー）
  - Azure: 21%
  - Google: 特定領域でシェア獲得
  - 三強独占構造継続
- **引用URL:** https://www.finout.io/blog/49-cloud-computing-statistics-in-2026
- **Evidence ID:** EVD-20260611-0076

### INFO-077
- **タイトル:** OpenAI "Built to benefit everyone" - AGI timeline March 2028
- **ソース:** OpenAI Blog (Sam Altman & Jakub Pachocki)
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI
- **要約:** OpenAI内部見通し: 2028年3月までに研究の大部分をAIシステムが実行。第3フェーズ: AIを豊富・安価・安全に。国際AI調整機関の必要性提起。AGIは人類の利益のために。
- **キーファクト:**
  - 2028年3月: AIが研究の大部分を実行する内部見通し
  - 第3フェーズ宣言（AIを誰もが使えるように）
  - 国際AI調整機関の必要性
  - AGIは全人類に利益をもたらすべき
- **引用URL:** https://openai.com/index/built-to-benefit-everyone-our-plan/
- **Evidence ID:** EVD-20260611-0077

### INFO-078
- **タイトル:** BCG: AI skills drive 30% code productivity increase
- **ソース:** BCG
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** (業界全体)
- **要約:** BCG調査: AI導入でコード生産性約30%向上、shipped features 27%増加。AIスキルからビジネスパフォーマンスへの変換方法を分析。
- **キーファクト:**
  - コード生産性30%向上
  - shipped features 27%増加
  - AIスキル→ビジネス成果の変換プロセス分析
- **引用URL:** https://www.bcg.com/publications/2026/from-ai-skills-to-business-performance
- **Evidence ID:** EVD-20260611-0078

### INFO-079
- **タイトル:** Gartner: Fortune 500 will have 150,000 AI agents by 2028
- **ソース:** Kore.ai
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** Gartner予測: 2028年までに平均的なFortune 500企業は150,000以上のAIエージェントを使用（2025年は15未満）。
- **キーファクト:**
  - 2028年: Fortune 500平均150,000+エージェント
  - 2025年: 同15未満
  - 10,000倍の増加予測
- **引用URL:** https://www.kore.ai/blog/what-is-ai-agent-sprawl
- **Evidence ID:** EVD-20260611-0079

### INFO-080
- **タイトル:** Enterprise AI pilots stall - 51% didn't scale
- **ソース:** LinkedIn
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-004-04
- **関連企業:** (業界全体)
- **要約:** エンタープライズAIパイロットの51%がスケールに失敗。独自データ（プロプライエタリ・データ）が唯一の持続可能な堀（モート）。モデル自体は成功の最重要因子ではない。
- **キーファクト:**
  - 51%のAIパイロットがスケール失敗
  - プロプライエタリ・データが唯一の持続的モート
  - モデル自体は最重要因子ではない
- **引用URL:** https://www.linkedin.com/pulse/why-enterprise-ai-pilots-stall-51-didnt-john-brewton-5c3ze
- **Evidence ID:** EVD-20260611-0080
