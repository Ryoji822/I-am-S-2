# 収集データ: 2026-06-12

## メタデータ
- 収集日時: 2026-06-12 01:30 UTC
- 品質フラグ: NORMAL
- 動的追加クエリ（Arbiterフィードバック）:
  - KIQ-ANT-SAFETY: エンタープライズ顧客Claude選択理由定量調査 → Claude Enterprise Security Guide・KPMG事例等を収集（定量的選択理由調査は未発見）
  - KIQ-GOO-001: AWS/Azure同時期Cloud成長率比較データ → AWS Bedrock AgentCore更新・Azure Foundry Agent Serviceのデータ収集。成長率比較データは未発見
  - INFO-062元データ確認: AIレイオフ理由1位の統計的方法論 → Challenger, Gray & Christmas「AIが2026年4月レイオフ理由1位」を確認。方法論詳細は未取得
  - Visa-OpenAI提携実質確認: 排他性・取引量・技術統合 → Visa Payments Forum提携確認。排他性言及なし。ステーブルコイン決済年間$70億規模。Mastercard Agent Pay for Machinesも同時発表（non-exclusive裏付け）
- 実行クエリ数: 56 / 56（collection_plan.json全クエリ + 動的追加4件）
- scrape実行数: 13件（公式ブログ11件 + collection_plan.jpynbスクレイピング）
- 収集情報数: 51件
- Evidence ID 採番範囲: EVD-20260612-0001 〜 EVD-20260612-0051
- KIQカバレッジ:
  - KIQ-001-01 ✓ (OpenAI Codex/Ona, Anthropic Fable 5, Google Gemini 3.1 Pro, xAI Grok Build, ByteDance Coze 2.5)
  - KIQ-001-02 ✓ (OpenAI Oracle/AWS, Anthropic KPMG/UK Gov, Visa-OpenAI, Claude Enterprise)
  - KIQ-001-03 ✓ (MCP, AAIF, SkillsMP, Claude Partner Network, Grok Build Marketplace)
  - KIQ-001-04 ✓ (Gemini agentic era, Fable 5 vision/ゲームクリア, DiffusionGemma)
  - KIQ-001-05 ✓ (Ona persistent execution, Gemini Skills/CLI, Claude Code MCP, Codex plugins)
  - KIQ-002-01 ✓ (AWS Bedrock AgentCore, Azure Foundry, Oracle Cloud, ServiceNow-NVIDIA)
  - KIQ-002-02 ✓ (Gartner 40%, Deloitte, McKinsey 62%, Fortune 500, BCG)
  - KIQ-002-03 ✓ (WH EO NSPM-11, EU AI Act, China regulation)
  - KIQ-002-04 ✓ (AI layoff #1 reason, Klarna/Duolingo boomerang, Fortune 500 hierarchy)
  - KIQ-002-05 ✓ (Agentic Commerce, Mastercard Agent Pay, SaaS disruption)
  - KIQ-002-06 ✓ (Anthropic autonomous weapons refusal, NSPM-11)
  - KIQ-003-01 ✓ (OpenAI price cuts, Claude Fable 5 $10/M, Lindy→DeepSeek)
  - KIQ-003-02 ✓ (ARC Challenge GPT-5 96.3%, DeepSeek V4 Pro NIST, Fable 5 SOTA)
  - KIQ-003-03 ✓ (OSS 89% commercial, DeepSeek V4 Pro, Llama benchmark)
  - KIQ-003-04 ✓ (OpenAI S-1, Anthropic $965B valuation, SpaceX IPO)
  - KIQ-003-05 ✓ (Vendor lock-in analysis, switching costs, multi-vendor)
  - KIQ-004-01 ✓ (AI layoff boomerang, Salesforce 86人, 41% management trim)
  - KIQ-004-02 ✓ (AI coding $9.8-11B, 51% commits AI-assisted, Copilot 20M+)
  - KIQ-004-03 ✓ (Workday 83% human skills, AI-proof skills)
  - KIQ-004-04 ✓ (BCG AI transformation, Deloitte 25% transformative)
  - KIQ-005-01 ✓ (OpenAI Phase 3 / 2028 AI research, ARC-AGI-3, Fable 5)
  - KIQ-005-02 ✓ (OpenAI Phase 3宣言, Anthropic Fable 5, Sam Altman vision)
  - KIQ-005-03 ✓ (WH EO, EU AI Act, AAIF, AI safety fellowships)
  - BYTEDANCE-CHINESE ✓ (Coze 2.5, DeerFlow 2.0, 豆包MAU減少, 2000億元投資)

## 収集結果

### INFO-001
- **タイトル:** OpenAI to acquire Ona — Codexに安全な永続的クラウド実行環境を統合
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIがOnaを買収し、Codexエコシステムに安全な永続的クラウド実行・オーケストレーション技術を統合する。Codex週間利用者500万人（年初比400%増）。ラップトップを閉じてもエージェントが顧客のクラウド環境で稼働し続ける機能を実現。
- **キーファクト:**
  - Codex週間アクティブユーザー500万人（2026年初比400%増）
  - Onaは200万人の開発者が利用する安全なクラウド環境技術を持つ
  - エージェントが時間・日単位で自律的に作業を継続する「persistent agentic work」構想
- **引用URL:** https://openai.com/index/openai-to-acquire-ona/
- **Evidence ID:** EVD-20260612-0001

### INFO-002
- **タイトル:** Access OpenAI models and Codex through Oracle Cloud commitment
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI, Oracle
- **要約:** OpenAIとOracleが提携し、Oracle Cloud Infrastructure (OCI) 顧客が既存のOracle Universal Creditsを使ってOpenAIモデルとCodexにアクセスできるようになる。企業の調達プロセスとガバナンスフレームワーク内でAI導入を可能にする。
- **キーファクト:**
  - OCI顧客が既存のクラウドコミットメントを使ってOpenAIモデル・Codexにアクセス可能
  - 数週間以内に利用開始予定
  - 企業の既存購入ワークフローに統合
- **引用URL:** https://openai.com/index/openai-on-oracle-cloud/
- **Evidence ID:** EVD-20260612-0002

### INFO-003
- **タイトル:** OpenAIがSECに機密S-1を提出 — IPO準備
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIが機密S-1をSECに提出。タイミングは未定で「非上場のままで進めたいこともあるが、複雑なトレードオフ」と説明。早期上場の選択肢を確保する意図。
- **キーファクト:**
  - 機密S-1提出済み（Rule 135に基づく告知）
  - 上場タイミングは未定。「非上場の方が進めやすいこともある」
  - IPO準備の公式確認
- **引用URL:** https://openai.com/index/openai-submits-confidential-s-1/
- **Evidence ID:** EVD-20260612-0003

### INFO-004
- **タイトル:** Built to benefit everyone: OpenAI Phase 3宣言 — AGI研究自動化2028年3月目標
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI
- **要約:** Sam AltmanとJakub Pachockiによる長文マニフェスト。OpenAIは第3フェーズ（AIを豊富・安価・安全に普及）に入る。2028年3月までに「AI研究の大部分をAIシステムが実行」する目標を掲げる。国際的なAI協調機関の設立を提唱。
- **キーファクト:**
  - 2028年3月目標: AI研究の大部分をAIシステムが人間研究者と共同で実行
  - OpenAI Phase 3: 「先端能力を人々が実際に使える道具にする」フェーズ
  - 3つの目標: (1)自動AI研究構築、(2)経済加速、(3)全人類にパーソナルAGI提供
  - 国際AI協調機関の設立提唱、フロンティア開発減速の調整機能も想定
- **引用URL:** https://openai.com/index/built-to-benefit-everyone-our-plan/
- **Evidence ID:** EVD-20260612-0004

### INFO-005
- **タイトル:** Codex for every role, tool, and workflow — 6つの役割別プラグイン・Sites・注釈機能
- **ソース:** OpenAI Blog (公式)
- **公開日:** 2026-06-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** Codexに6つの役割別プラグイン（データ分析・クリエイティブ・営業・プロダクトデザイン・投資・投資銀行）、Sites（インタラクティブWebサイト生成）、Annotations（成果物のインプレース修正）を追加。非開発者ユーザーが全体の20%を占め、開発者比3倍速で増加中。
- **キーファクト:**
  - 6役割別プラグイン: 62アプリ・110スキル統合（Snowflake, Figma, Salesforce等）
  - 非開発者ユーザー20%、開発者比3倍速成長
  - Sites: Business/Enterprise向けにインタラクティブサイト生成・共有機能
  - GitHub上でオープンソースのrole-based-plugins公開
- **引用URL:** https://openai.com/index/codex-for-every-role-tool-workflow/
- **Evidence ID:** EVD-20260612-0005

### INFO-006
- **タイトル:** Claude Fable 5 and Claude Mythos 5 — AnthropicのMythos-classモデル一般公開
- **ソース:** Anthropic Blog (公式)
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Fable 5（Mythos-classの一般公開版）とClaude Mythos 5（サイバーセーフガード解除版）を発表。Fable 5はほぼ全ベンチマークでSOTA。ソフトウェア工学・知識作業・視覚・科学研究で大幅向上。価格は$10/M入力・$50/M出力トークン（Mythos Previewの半額以下）。
- **キーファクト:**
  - Fable 5: Mythos-classモデルの一般公開版。サイバー・バイオセーフガード付き
  - Mythos 5: 同一モデルだがサイバーセーフガード解除（Project Glasswing経由）
  - Stripe: 5000万行Rubyコードベースの移行を「チーム2ヶ月作業→1日」に圧縮
  - 価格: $10/M入力・$50/M出力（Mythos Previewの半額以下）
  - 新セーフガード: 分類器によるフォールバック（>95%セッションは影響なし）
  - 30日間データ保持ポリシー（Mythos-classモデル）
  - FrontierCode最高スコア（Cognition評価）
- **引用URL:** https://www.anthropic.com/news/claude-fable-5-mythos-5
- **Evidence ID:** EVD-20260612-0006

### INFO-007
- **タイトル:** KPMG integrates Claude across 276,000+ employees — グローバル戦略的提携
- **ソース:** Anthropic Blog (公式)
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Anthropic, KPMG
- **要約:** KPMGがAnthropicとグローバル戦略的提携を発表。276,000人以上の全従業員にClaudeアクセス提供。Digital GatewayプラットフォームにClaude Cowork/Managed Agents統合。PE会社向け優先パートナーに指名。
- **キーファクト:**
  - KPMG全276,000人以上の従業員にClaudeアクセス提供
  - Digital Gateway（Microsoft Azure基盤）にClaude Cowork/Managed Agents統合
  - 税務クライアント向け新ツールから開始
  - AnthropicのPE会社向け優先パートナーに指名
  - KPMG Blaze: Claude Codeを埋め込んだITモダナイゼーション製品
- **引用URL:** https://www.anthropic.com/news/anthropic-kpmg
- **Evidence ID:** EVD-20260612-0007

### INFO-008
- **タイトル:** Expanding Project Glasswing — 150新規組織へ拡大
- **ソース:** Anthropic Blog (公式)
- **公開日:** 2026-06-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Project Glasswingを約150の新規組織に拡大。15カ国以上にわたり、電力・水道・医療・通信・ハードウェア業界を新規カバレッジ。10,000件以上の高・重大 severity セキュリティ脆弱性を発見済み。
- **キーファクト:**
  - 初期50組織→約200組織に拡大（150新規追加）
  - 15カ国以上、電力・水道・医療・通信・ハードウェア業界を新規追加
  - 初期パートナーが10,000件以上の高/重大脆弱性発見済み
  - 「6-12ヶ月以内に他社もMythos-classモデルを持つ可能性」警告
  - Claude Security（Opus 4.8基盤）一般製品も発表
- **引用URL:** https://www.anthropic.com/news/expanding-project-glasswing
- **Evidence ID:** EVD-20260612-0008

### INFO-009
- **タイトル:** Claude Partner Network — $100M投資のパートナーエコシステム
- **ソース:** Anthropic Blog (公式)
- **公開日:** 2026-03-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Partner Networkを発表し、$100Mの初期投資をコミット。トレーニング・技術サポート・市場開発を提供。Claude Certified Architect認定資格を開始。Accentureが30,000人をClaude訓練中。
- **キーファクト:**
  - $100M初期投資（2026年）
  - パートナーチーム5倍に拡充
  - Claude Certified Architect（Foundations）認定試験開始
  - Accenture: 30,000人Claude訓練中
  - Code Modernizationスターターキット提供
- **引用URL:** https://www.anthropic.com/news/claude-partner-network
- **Evidence ID:** EVD-20260612-0009

### INFO-010
- **タイトル:** Grok Build Plugin Marketplace — xAIがプラグインマーケットプレイス発表
- **ソース:** xAI Blog (公式)
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** xAI
- **要約:** xAIがGrok Build用の内蔵プラグインマーケットプレイスを発表。開発者コミュニティによるエコシステム拡大を促進する構想。
- **キーファクト:**
  - Grok Buildに内蔵プラグインマーケットプレイス追加
  - 開発者エコシステム拡大の取り組み
- **引用URL:** https://x.ai/news/grok-plugin-marketplace
- **Evidence ID:** EVD-20260612-0010

### INFO-011
- **タイトル:** eToroと提携 — Toriにリアルタイム市場センチメント統合
- **ソース:** xAI Blog (公式)
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** xAI, eToro
- **要約:** SpaceXAIがeToroと提携し、リアルタイム市場センチメントデータをGrokのTori機能に統合。金融データのエコシステム拡大。
- **キーファクト:**
  - eToroとの提携でリアルタイム市場センチメントをToriに統合
- **引用URL:** https://x.ai/news/grok-etoro
- **Evidence ID:** EVD-20260612-0011

### INFO-012
- **タイトル:** Powering Gopuff's Go agent — xAIの配送AIエージェント
- **ソース:** xAI Blog (公式)
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-02
- **関連企業:** xAI, Gopuff
- **要約:** xAIがGopuffのGo agentをGrokで提供。即時配送サービスでのAIエージェント活用事例。
- **キーファクト:**
  - Gopuffの配送AIエージェント「Go agent」をGrokで提供
- **引用URL:** https://x.ai/news/grok-gopuff
- **Evidence ID:** EVD-20260612-0012

### INFO-013
- **タイトル:** I/O 2026: Welcome to the agentic Gemini era — Google I/O 2026基調講演
- **ソース:** Google Blog (公式)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** Google
- **要約:** Google I/O 2026でSundar Pichaiが「agentic Gemini era」を宣言。Geminiのエージェント機能強化とGoogle製品への深い統合を発表。
- **キーファクト:**
  - 「Agentic Gemini era」宣言
  - Gemini App が proactive・24/7ヘルプを提供するエージェント化
- **引用URL:** https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
- **Evidence ID:** EVD-20260612-0013

### INFO-014
- **タイトル:** DiffusionGemma: 4x faster text generation — Googleの拡散モデルベース高速テキスト生成
- **ソース:** Google Blog (公式)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01, KIQ-003-02
- **関連企業:** Google
- **要約:** GoogleがDiffusionGemmaを発表。拡散モデルベースのテキスト生成で従来比4倍高速化。Gemma 4のビルダー事例も公開。
- **キーファクト:**
  - 拡散モデルベースのテキスト生成で4倍高速化
  - Gemma 4のビルダー事例公開
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/
- **Evidence ID:** EVD-20260612-0014

### INFO-015
- **タイトル:** Anthropic partners with UK Government for GOV.UK AI assistant
- **ソース:** Anthropic Blog (公式)
- **公開日:** 2026-01-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** Anthropicが英国政府（DSIT）と提携し、GOV.UK向けAIアシスタントを構築。雇用支援に特化したエージェントシステム。安全性第一のアプローチ。
- **キーファクト:**
  - 英国DSITがGOV.UK AIアシスタントにAnthropicを選定
  - Claude基盤のエージェントシステム
  - 初期ユースケース: 雇用支援（求職・訓練・リソース案内）
  - DSIT「Scan, Pilot, Scale」フレームワークに従う段階的展開
- **引用URL:** https://www.anthropic.com/news/gov-UK-partnership
- **Evidence ID:** EVD-20260612-0015

### INFO-016
- **タイトル:** ByteDance Coze 2.5 — Agent World エコシステム導入
- **ソース:** KuCoin News
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのCozeがv2.5をリリースし、「Agent World」エコシステムを導入。AIエージェントがチャットUIを越えて独立実行環境・スキル・アイデンティティを持って稼働可能に。
- **キーファクト:**
  - Coze v2.5: Agent Worldエコシステム導入
  - エージェントが独立実行環境・スキル・アイデンティティを持つ
  - チャットUIを超えたエージェント運用を実現
- **引用URL:** https://www.kucoin.com/news/flash/bytedance-s-coze-launches-version-2-5-introduces-agent-world-ecosystem
- **Evidence ID:** EVD-20260612-0016

### INFO-017
- **タイトル:** ByteDance DeerFlow 2.0 — 複数AIエージェントを生成するスーパーエージェント
- **ソース:** Instagram (報道)
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0をリリース。複数AIエージェントを生成・コード実行・レポート・プレゼン・Webサイト構築が可能なスーパーエージェント。
- **キーファクト:**
  - DeerFlow 2.0: 複数AIエージェントを生成するスーパーエージェント
  - コード実行・レポート・プレゼン・Webサイト構築機能
- **引用URL:** https://www.instagram.com/reel/DZKkK6LJB1Q/
- **Evidence ID:** EVD-20260612-0017

### INFO-018
- **タイトル:** Google Gemini 3.1 Pro — SWE・エージェント能力改善
- **ソース:** Google Cloud Docs
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** Google
- **要約:** Gemini 3.1 Proがリリース。ソフトウェア工学・エージェント能力が改善。金融・ケース管理等のドメインでエージェント的改善を確認。
- **キーファクト:**
  - Gemini 3.1 Pro: SWE・エージェント能力改善
  - 金融ドメイン等でのエージェント改善
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-pro
- **Evidence ID:** EVD-20260612-0018

### INFO-019
- **タイトル:** OpenAI price cuts検討 — Anthropicとの競争激化でWSJ報道
- **ソース:** CNBC
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic
- **要約:** WSJ報道によりOpenAIが有料AIモデルアクセスの価格引き下げを検討中と報じられる。Anthropicとのユーザー獲得競争が背景。
- **キーファクト:**
  - OpenAIが価格引き下げ検討（WSJ報道・関係者情報）
  - Anthropicとのユーザー獲得競争が背景
  - 2026年4月にCodex価格改定（API token使用量ベースに移行）済み
- **引用URL:** https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html
- **Evidence ID:** EVD-20260612-0019

### INFO-020
- **タイトル:** OpenAI価格改定履歴 — $8 Go/月〜$100 Pro/月の新プラン体系
- **ソース:** LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** 2026年のOpenAI価格改定: Go $8/月、Business $30/ユーザー、Pro $100/月。8回の価格改定を実施。
- **キーファクト:**
  - Go plan: $8/月（2026年1月）
  - Team → Business改名 $30/user
  - Pro $100/月の新ティア
  - 2026年に8回の価格改定
- **引用URL:** https://www.linkedin.com/posts/krzysztof-szyszkiewicz_of-major-pricing-updates-these-9-fastest-activity-7470460134369062914-Ak4X
- **Evidence ID:** EVD-20260612-0020

### INFO-021
- **タイトル:** ARC-AGI-3 ベンチマーク — GPT-5が96.3%でトップ
- **ソース:** PricePerToken, Medium
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** ARC Challenge Leaderboard (2026年6月6日時点) でGPT-5が96.3%でトップ。ARC-AGI-3は2026年3月にリセット発売され、モデルが0%から急速に上昇中。ベンチマーク天井到達の議論が活発化。
- **キーファクト:**
  - GPT-5: ARC Challenge 96.3% (1位)
  - ARC-AGI-3: 2026年3月リセット後、急速にスコア上昇
  - ベンチマーク飽和問題の議論が活発化
- **引用URL:** https://pricepertoken.com/leaderboards/benchmark/arc-challenge
- **Evidence ID:** EVD-20260612-0021

### INFO-022
- **タイトル:** Anthropic自律兵器拒否 — ベンダー撤退不可能の構造的問題
- **ソース:** Instagram/TNW (報道)
- **公開日:** 2026-06-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** AnthropicがClaudeの自律兵器・監視目的での使用を拒否。しかし「ベンダーは一度軍事契約に入ると撤退できない」という構造的問題が指摘されている。Trump政権による軍事委託業者・AI企業への圧力報道。
- **キーファクト:**
  - Anthropic: Claudeの自律兵器・監視目的での使用を明確拒否
  - TNW報道: 「ベンダーは一度参加すると撤退不可能」の構造指摘
  - Trump政権が軍事委託業者・AI企業に圧力をかけている報道
- **引用URL:** https://www.instagram.com/p/DZTHbbhEcoi/
- **Evidence ID:** EVD-20260612-0022

### INFO-023
- **タイトル:** 白宮 先進AI大統領令 — 2026年6月2日署名
- **ソース:** White House, Skadden, Hogan Lovells
- **公開日:** 2026-06-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** (政府政策)
- **要約:** 2026年6月2日、Trump大統領が「Promoting Advanced Artificial Intelligence Innovation and Security」大統領令に署名。国家安全保障前提のAI政策への明確な転換。フロンティアモデルのセキュリティ要件・サイバー防衛・重要インフラ保護を指示。
- **キーファクト:**
  - 2026年6月2日: 「先進AIイノベーション・安全保障」大統領令署名
  - 国家安全保障前提のAI政策への転換
  - フロンティアモデルセキュリティ要件・サイバー防衛指示
  - NSPM-11（国家安全安全保障大統領覚書）も同時発表
- **引用URL:** https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-signs-historic-directive-on-ai-in-the-national-security-enterprise/
- **Evidence ID:** EVD-20260612-0023

### INFO-024
- **タイトル:** EU AI Act 2026年8月執行開始 — ハイリスクAIエージェント分類
- **ソース:** Stibbe, EWSolutions, KLA Digital
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** (規制)
- **要約:** EU AI Actが2026年8月に執行開始。金融・医療・法的決定を行うAIエージェントはAnnex IIIのハイリスク分類に該当。米国スタートアップにも適用。コンプライアンスソフトウェア市場が急拡大。
- **キーファクト:**
  - EU AI Act: 2026年8月執行開始
  - 金融・医療・法的決定エージェントはハイリスク分類
  - 米国企業にも適用（違反時は全球売上の4%罰金）
  - コンプライアンスソフトウェア4カテゴリ市場が急成長
- **引用URL:** https://www.stibbe.com/publications-and-insights/ai-act-reloaded-what-the-latest-ai-act-changes-mean-in-practice
- **Evidence ID:** EVD-20260612-0024

### INFO-025
- **タイトル:** 企業AIエージェント採用率 — Gartner予測40%がエージェント組み込み
- **ソース:** LinkedIn, Salesforce, Gartner
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界動向)
- **要約:** Gartner予測: 2026年末までにエンタープライズアプリの40%がタスク特化AIエージェントを組み込む（2025年5%未満から急増）。Salesforce調査: 企業平均12エージェント稼働、2年で67%増予測。Deloitte: 25%が「変革的効果」回答。
- **キーファクト:**
  - Gartner: 2026年末40%のエンタープライズアプリがAIエージェント組み込み（2025年<5%）
  - Salesforce: 平均12エージェント稼働、2年で67%増予測
  - Deloitte: 25%が「変革的効果」回答（前年12%から倍増）
- **引用URL:** https://www.linkedin.com/pulse/year-roi-ai-agents-how-enterprise-world-finally-de-castro-j%C3%BAnior-we66e
- **Evidence ID:** EVD-20260612-0025

### INFO-026
- **タイトル:** AIレイオフ「ブーメラン効果」— Klarna・IBM等が再雇用
- **ソース:** Facebook, Webwell, Prymage
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** Klarna, IBM, Duolingo, Salesforce
- **要約:** Klarna・IBM・Duolingo等がAI導入でレイオフ後、人間再雇用に転じる「AI Boomerang Effect」。Challenger, Gray & Christmas報告: AIが2026年4月のレイオフ理由1位。だがAIコストが予想以上で逆効果のケースも。SalesforceがAgentforce/Cloud部門で86人レイオフ。
- **キーファクト:**
  - AIが2026年4月のレイオフ理由1位（Challenger, Gray & Christmas）
  - Klarna: 5,500→3,000人に削減後、人材再雇用に転換
  - Salesforce: Agentforce/Cloud部門で86人レイオフ（9ヶ月で3回目）
  - 企業の6分の1が2026年中にAIによる人員削減を予定
- **引用URL:** https://www.metaintro.com/blog/salesforce-ai-cloud-layoffs-june-2026
- **Evidence ID:** EVD-20260612-0026

### INFO-027
- **タイトル:** オープンソースLLM性能ギャップ縮小 — 商用モデルの89%に到達
- **ソース:** Fungies.io, TechSy, Substack
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, DeepSeek, (OSS界隈)
- **要約:** オープンソースLLMが商用モデルの89%に到達し、ギャップが実質的に縮小。NIST CAISI評価でDeepSeek V4-Proと米国モデルを19ベンチマーク比較。OSSはフロンティアより7ヶ月遅れだが、大半の本番タスクでは差は無関係との分析。
- **キーファクト:**
  - オープンソースLLM: 商用モデルの89%に到達
  - NIST CAISI: DeepSeek V4-Pro vs 米国モデル19ベンチマーク比較
  - フロンティアとの差は7ヶ月だが、本番タスクでは無関係
  - 3つのOSSモデルがGPT-4を上回る結果（ベンチマーク）
- **引用URL:** https://fungies.io/best-open-source-llms-2026/
- **Evidence ID:** EVD-20260612-0027

### INFO-028
- **タイトル:** Visa-OpenAI提携詳細 — Agentic Commerce決済インフラ統合
- **ソース:** BizJournals, LiquidityFinder, AI Weekly
- **公開日:** 2026-06-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** OpenAI, Visa
- **要約:** VisaとOpenAIが戦略的提携を発表（Visa Payments Forum in San Francisco）。Visaのグローバルネットワーク・トークン化・リスクインフラをOpenAIプラットフォームに統合。ステーブルコイン決済層は年間$70億規模。排他性については言及なし。
- **キーファクト:**
  - Visa-OpenAI戦略的提携: Agentic Commerce決済インフラ
  - Visaのグローバルネットワーク・トークン化・リスクインフラ統合
  - ステーブルコイン決済層: 年間$70億（160+カードプログラム）
  - 排他性についての言及なし（non-exclusive可能性）
- **引用URL:** https://www.bizjournals.com/sanfrancisco/news/2026/06/10/openai-visa-secure-payments-agentic-commerce.html
- **Evidence ID:** EVD-20260612-0028

### INFO-029
- **タイトル:** OpenAI IPO vs Anthropic IPO — 競合上場レース
- **ソース:** Yahoo Finance, Instagram, Fox Business
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIが機密S-1提出。Anthropicも今秋IPO予定と報じられ、競合上場レースに。Anthropic評価額$965B（Series H）、OpenAI評価額$852B。SpaceX IPOも4倍超過认购。
- **キーファクト:**
  - OpenAI: 機密S-1提出、IPO準備
  - Anthropic: 今秋IPO予定（Yahoo Finance報道）
  - Anthropic評価額: $965B（Series H / Altimeter, Sequoia, Coatue等主導）
  - OpenAI評価額: $852B
  - SpaceX IPO: 4倍超過认购、$1.75兆評価額
- **引用URL:** https://finance.yahoo.com/video/openai-vs-anthropic-ipo-what-sets-these-ai-companies-apart-195206256.html
- **Evidence ID:** EVD-20260612-0029

### INFO-030
- **タイトル:** DeepSeek V4 Pro — NIST評価で米国モデルと比較、エンタープライズAPI利用率4.2%
- **ソース:** FutureSearch, Substack
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 ProがNIST CAISIの19ベンチマーク評価で米国モデルと比較。フロンティアモデル中のエンタープライズAPI利用率は中央値4.2%。GPT-5.5 Proは$180/M出力トークンで高価格維持。
- **キーファクト:**
  - DeepSeek V4 Pro: NIST CAISI 19ベンチマーク評価
  - エンタープライズAPI利用率中央値4.2%
  - GPT-5.5 Pro: $180/M出力トークン
- **引用URL:** https://futuresearch.ai/blog/deepseek-v4-pro-wont-move-the-market/
- **Evidence ID:** EVD-20260612-0030

### INFO-031
- **タイトル:** AIベンダーロックイン — 推論の「筋肉の記憶」による高いスイッチングコスト
- **ソース:** X (Twitter), Omnithium, Sakara Digital
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** (業界全体)
- **要約:** AIエージェントのベンダーロックインがクラウド以上に高いとの指摘。推論の暗黙知（プロンプト・エージェント設計の試行錯誤）が蓄積され、モデル切り替えで全て再発見が必要。マルチベンダーオーケストレーションの重要性が指摘。
- **キーファクト:**
  - AIベンダーのスイッチングコストはクラウド以上
  - ロックインはインフラではなく「推論の暗黙知」に
  - マルチベンダーオーケストレーションが必要
- **引用URL:** https://omnithium.ai/blog/ai-agent-vendor-lock-in-enterprise-escape-plan.html
- **Evidence ID:** EVD-20260612-0031

### INFO-032
- **タイトル:** Claude Fable 5がMicrosoft Foundryで利用可能 — Azureエージェント統合
- **ソース:** Microsoft Azure Blog
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Anthropic, Microsoft
- **要約:** Claude Fable 5がMicrosoft Foundryで利用可能に。長時間実行タスク・エンタープライズワークフロー向け。Azure AI Foundryのエージェント能力が大幅拡充。
- **キーファクト:**
  - Claude Fable 5がMicrosoft Foundryで利用可能
  - 長時間エージェントタスク・エンタープライズワークフロー対応
- **引用URL:** https://azure.microsoft.com/en-us/blog/claude-fable-5-is-now-available-in-microsoft-foundry-powering-the-next-era-of-autonomous-agents/
- **Evidence ID:** EVD-20260612-0032

### INFO-033
- **タイトル:** AWS Bedrock AgentCore — セキュリティ・ガバナンス更新
- **ソース:** ScaleFactory, AWS Blog
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** AWS Bedrock AgentCore Policy and EvaluationsがGA到達（2026年3月）。Agent Registryが2026年4月にリリース。Microsoft Entra Agent IDとの統合でBedrockエージェントのセキュリティ強化。
- **キーファクト:**
  - AgentCore Policy/Evaluations: 2026年3月GA
  - Agent Registry: 2026年4月リリース
  - Microsoft Entra Agent IDとの統合
- **引用URL:** https://scalefactory.com/amazon-bedrock-six-months-of-security-and-governance-updates-worth-knowing-about/
- **Evidence ID:** EVD-20260612-0033

### INFO-034
- **タイトル:** AIコーディング市場$9.8-11B — Gartner評価・51%のコミットがAI支援
- **ソース:** Virtualization Review, GetPanto
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** GitHub, Cursor, Anthropic
- **要約:** Gartner推計: エンタープライズAIコーディングエージェント市場年間$9.8-11B（2026年4月）。MIT研究: 2026年時点でGitHubコミットの51%以上がAI支援。GitHub Copilot累計20M+ユーザー。
- **キーファクト:**
  - Gartner: AIコーディングエージェント市場$9.8-11B年間
  - MIT: GitHubコミットの51%以上がAI支援（2026年）
  - GitHub Copilot: 累計20M+ユーザー
  - 91%の開発者がAIツール使用・使用予定
- **引用URL:** https://www.getpanto.ai/blog/ai-coding-assistant-statistics
- **Evidence ID:** EVD-20260612-0034

### INFO-035
- **タイトル:** 豆包(Doubao) MAU減少 — 610万人流失・ByteDance AI基盤投資2000億元
- **ソース:** 知乎, 直播吧, X
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceの豆包(Doubao)が有料化発表後、月間アクティブユーザー610万人減少。ByteDanceは2026年AI基盤投資を1600億元→2000億元に上方修正。2026年は有料化KPIを評価対象外とする方針。Seedance 2.0動画生成モデルを豆包に統合。
- **キーファクト:**
  - 豆包: 有料化後MAU 610万人減少
  - ByteDance AI基盤投資: 1600億→2000億元に上方修正
  - 2026年は有料化KPIを評価対象外
  - 基本機能（チャット・Q&A）は永久無料維持
- **引用URL:** https://x.com/GoSailGlobal/article/2063438628328505386
- **Evidence ID:** EVD-20260612-0035

### INFO-036
- **タイトル:** MCP (Model Context Protocol) — 企業採用の学術研究・仕様Release Candidate
- **ソース:** MCP Blog, arXiv, WriteHuman
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic (MCP作者)
- **要約:** MCP仕様のRelease Candidateが公開。ステートレスプロトコルコア・Extensions・Tasks・MCP Appsを含む。arXivに企業のMCP採用に関する学術研究が掲載。Host/Client/Server/Resourceの4コアコンポーネントによる標準化が進展。
- **キーファクト:**
  - MCP仕様Release Candidate公開
  - ステートレスプロトコルコア・Extensions・Tasks・MCP Apps
  - arXiv: 企業MCP採用の学術研究掲載
  - 4コアコンポーネント: Host/Client/Server/Resource
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260612-0036

### INFO-037
- **タイトル:** Lindy — Anthropic Claude→DeepSeek切り替えでコスト削減
- **ソース:** Develeap
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** Anthropic, DeepSeek
- **要約:** ノーコードAIエージェントプラットフォームLindyがAnthropic ClaudeからDeepSeekモデルに切り替えて推論コストを削減。ブロードなコスト圧力を反映。
- **キーファクト:**
  - Lindy: Anthropic Claude → DeepSeekに切り替え
  - 推論コスト削減が目的
  - エージェントプラットフォーム業界のコスト圧力反映
- **引用URL:** https://www.develeap.com/news/this-ai-agent-startup-ditched-anthropic-for-deepseek-and-say-b1c6d2ce/
- **Evidence ID:** EVD-20260612-0037

### INFO-038
- **タイトル:** BCG: AI時代の組織再設計 — 多くの企業がAI投資の意味ある収益を得られず
- **ソース:** BCG
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-004-04
- **関連企業:** (業界動向)
- **要約:** BCGが「AI時代に勝つ技術リーダー」レポート発表。先進企業はAI変革をコスト削減で資金調達。しかし大半の企業がAI投資から意味のある収益を得られていない。組織・オペレーティングモデルの再設計が必要。
- **キーファクト:**
  - BCG: 大半の企業がAI投資から意味ある収益を得られず
  - 先進企業はAI変革をコスト削減で資金調達
  - 組織・オペレーティングモデルの再設計が必要
- **引用URL:** https://www.bcg.com/publications/2026/to-thrive-in-the-ai-era-tech-leaders-must-reinvent-organization-and-operating-models
- **Evidence ID:** EVD-20260612-0038

### INFO-039
- **タイトル:** Workday調査 — 83%が「AIで人間固有スキルがより重要に」
- **ソース:** Facebook, Yahoo
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** (業界動向)
- **要約:** Workdayグローバル調査: 従業員の83%が「AIによってユニークな人間スキルがより重要になる」と回答。共感力・批判的思考・倫理的意思決定が人間中心スキルとして強調。
- **キーファクト:**
  - Workday調査: 83%がAIで人間スキルがより重要に
  - 共感力・批判的思考・倫理的意思決定が重要視
  - AI代替困難なスキル: 手動作業・規制・共感を要する職種
- **引用URL:** https://uk.style.yahoo.com/five-workplace-skills-humans-still-134750468.html
- **Evidence ID:** EVD-20260612-0039

### INFO-040
- **タイトル:** Microsoft — Claude Code GitHub ActionのCI/CDセキュリティ脆弱性発見
- **ソース:** Microsoft Security Blog
- **公開日:** 2026-06-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Microsoft, Anthropic
- **要約:** Microsoft Threat IntelligenceがAnthropicのClaude Code GitHub Actionのセキュリティ脆弱性を発見。AIエージェントが信頼できない入力を処理する際、CI/CDワークフローのシークレットが露出する可能性。
- **キーファクト:**
  - Claude Code GitHub ActionにCI/CDシークレット露出の脆弱性
  - Microsoft Threat Intelligenceが発見
  - エージェントAIのCI/CD統合における新セキュリティリスク
- **引用URL:** https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/
- **Evidence ID:** EVD-20260612-0040

### INFO-041
- **タイトル:** Mastercard Agent Pay for Machines — エージェントコマース決済インフラ
- **ソース:** Mastercard Press Release
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02
- **関連企業:** Mastercard
- **要約:** Mastercardが「Agent Pay for Machines」を発表。カード・口座・ステーブルコイン経由の安全なマシン間継続支払いを可能にする。Visa-OpenAIと並ぶエージェントコマース決済インフラ競争の激化。
- **キーファクト:**
  - Mastercard Agent Pay for Machines発表
  - カード・口座・ステーブルコイン経由のマシン間支払い
  - Visa-OpenAI提携と並ぶエージェントコマース決済競争
- **引用URL:** https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
- **Evidence ID:** EVD-20260612-0041

### INFO-042
- **タイトル:** Fortune: AIエージェントが企業階層をフラット化 — 41%が管理層削減
- **ソース:** Fortune
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-004-01
- **関連企業:** (業界動向)
- **要約:** Fortune報道: AIエージェントが企業の階層をフラット化している。Korn Ferry調査によると41%の従業員が「昨年、会社が管理層を削減した」と回答。Microsoft調査ではFortune 500企業の10%未満しかAIエージェントのガバナンス戦略を持たない。
- **キーファクト:**
  - Korn Ferry: 41%が管理層削減回答
  - Microsoft調査: Fortune 500の<10%しかAIエージェントガバナンス戦略なし
  - McKinsey: 62%がAIエージェント試験中だがスケール成功は少数
- **引用URL:** https://fortune.com/2026/06/09/ai-agents-flattening-corporate-hierarchies-companies-managers-develop-new-playbook/
- **Evidence ID:** EVD-20260612-0042

### INFO-043
- **タイトル:** AAIF (Agentic AI Foundation) — 6ヶ月の振り返り・標準化進展
- **ソース:** LinkedIn, TrendUsAI, Linux Foundation
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** (業界標準化)
- **要約:** Agentic AI Foundation (AAIF) が6ヶ月の振り返りを発表。MCP・AGENTS.md・メンバーシップを通じた業界標準化が急速に進展。エコシステム断片化を防止するオープンスタックの中立拠点として機能。
- **キーファクト:**
  - AAIF: MCP・AGENTS.mdを通じた標準化進展
  - エコシステム断片化防止の中立拠点
  - Ambassador Program 2026開始
- **引用URL:** https://www.linkedin.com/pulse/six-months-open-reflections-agentic-ai-foundations-mazin-hp3ec
- **Evidence ID:** EVD-20260612-0043

### INFO-044
- **タイトル:** Gemini Enterprise Agent Platform — Skill Registry・RAG Engine統合
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-01
- **関連企業:** Google
- **要約:** Google CloudのGemini Enterprise Agent PlatformにSkill RegistryとRAG Engineが統合。エージェントスキルのセキュア・低レイテンシな管理・発見リポジトリ。Gemini CLI Skills・サブエージェント機能も拡充。
- **キーファクト:**
  - Skill Registry: スキルのセキュア・低レイテンシ管理・発見
  - RAG Engine統合
  - Gemini CLIサブエージェント機能拡充
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260612-0044

### INFO-045
- **タイトル:** NSPM-11 — 国家安全保障AI大統領覚書
- **ソース:** White House
- **公開日:** 2026-06-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** (政府政策)
- **要約:** National Security Presidential Memorandum/NSPM-11が同時発表。AIの国家安全保障用途での開発・利用加速を4本柱で指示。高度AIコンピューティング施設の建設ロードマップを含む。
- **キーファクト:**
  - NSPM-11: 国家安全保障AI利用の4本柱
  - 高度AIコンピューティング施設建設ロードマップ
  - 採用・セキュリティ・国際協力・ガバナンスの柱
- **引用URL:** https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/
- **Evidence ID:** EVD-20260612-0045

### INFO-046
- **タイトル:** Fortune 500 AIエージェメント — 月額推論コスト数千万ドル
- **ソース:** Nosana
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01, KIQ-002-02
- **関連企業:** (業界動向)
- **要約:** 一部Fortune 500企業が月額AI推論コストとして数千万ドルを報告。トークン単価体系がエージェント大量利用で急速に増加。コスト管理がエージェント展開の課題に。
- **キーファクト:**
  - Fortune 500企業の一部: 月額AI推論コスト数千万ドル
  - per-token価格体系がエージェント大量利用で急増
- **引用URL:** https://nosana.com/blog/the-real-cost-of-ai-agents/
- **Evidence ID:** EVD-20260612-0046

### INFO-047
- **タイトル:** ServiceNow-NVIDIA提携 — エンタープライズ環境でのガバナンス付き自律エージェント
- **ソース:** Kanerika
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** ServiceNow, NVIDIA
- **要約:** Knowledge 2026（2026年5月）でServiceNowとNVIDIAがエンタープライズ環境向けのガバナンス付き自律エージェントパートナーシップを発表。
- **キーファクト:**
  - ServiceNow-NVIDIA: ガバナンス付き自律エージェント提携
  - Knowledge 2026で発表
  - エンタープライズ環境向け
- **引用URL:** https://kanerika.com/blogs/agentic-ai-companies/
- **Evidence ID:** EVD-20260612-0047

### INFO-048
- **タイトル:** SaaS disruption AI agent platform integration — コモディティ化圧力
- **ソース:** Google Cloud, Tinuiti, Facebook
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** (業界動向)
- **要約:** エージェントコマースがチェックアウトを再構築。金融機関はエージェントによる非中介化（disintermediation）回避のためにデジタルインフラ経由でAI導入を進める。Google CX Agent Studioがマルチモーダルエージェント構築を提供。
- **キーファクト:**
  - Agentic Commerce: AIエージェントが購買プロセスを再構築
  - 金融機関: エージェント非中介化回避のためデジタル+AI統合
  - Google CX Agent Studio: マルチモーダルエージェント構築プラットフォーム
- **引用URL:** https://tinuiti.com/blog/commerce/agentic-commerce/
- **Evidence ID:** EVD-20260612-0048

### INFO-049
- **タイトル:** SkillsMP — エージェントスキルのマーケットプレイス
- **ソース:** Threads
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** (エコシステム)
- **要約:** SkillsMPがエージェントスキルの検索可能カタログとして機能。Claude Code・Codex・ChatGPT等のツールで使えるスキルパック（ワークフロー・指示セット）を提供。オープンスキル標準化の動き。
- **キーファクト:**
  - SkillsMP: Claude Code/Codex/ChatGPT向けスキルマーケットプレイス
  - 再利用可能なエージェントスキルパック
  - オープンスキル標準化の動き
- **引用URL:** https://www.threads.com/@theaicontinuum/post/DZTlmAvCQz1/
- **Evidence ID:** EVD-20260612-0049

### INFO-050
- **タイトル:** Harvey AI — 法務エージェントの製品更新（2026年6月）
- **ソース:** Harvey AI Blog
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** Harvey AI
- **要約:** 法務特化AIプラットフォームHarveyが6月更新を発表。契約ワークフローの高度な制御・大規模文書レビューの高速化・モバイル対応強化。法務ドメインでのエージェント展開事例。
- **キーファクト:**
  - 契約ワークフロー制御の高度化
  - 大規模文書レビュー高速化
  - モバイル対応強化
- **引用URL:** https://www.harvey.ai/blog/the-brief-june-2026
- **Evidence ID:** EVD-20260612-0050

### INFO-051
- **タイトル:** AIベンチマーク飽和問題 — 本番環境での失敗が増加
- **ソース:** Kili Technology
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** (業界全体)
- **要約:** AIベンチマークが飽和する一方で本番環境での失敗が増加。主要2026評価カテゴリを網羅的に整理し、人間専門家レビューが依然として優位であることを示す分析。
- **キーファクト:**
  - ベンチマーク飽和と本番環境失敗の増大の並行
  - 人間専門家レビューの継続的優位性
- **引用URL:** https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough
- **Evidence ID:** EVD-20260612-0051
