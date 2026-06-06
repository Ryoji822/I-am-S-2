# 収集データ: 2026-06-06

## メタデータ
- 収集日時: 2026-06-06 00:00 UTC
- 品質フラグ: COLLECTING
- 総INFO数: 56
- 総Evidence ID: EVD-20260606-0001～EVD-20260606-0056
- 最終INFO: INFO-056 (EVD-20260606-0056)
- ステータス: Step 3完了（全23 KIQ検索実行済み）、Step 4（深掘りスクレイプ）・Step 5（メタデータ最終更新）未完了
- 動的追加クエリ（Arbiter v3.99フィードバック）:
  - KIQ-NEW-2026-06-05: Trump EO 30日マイルストーン規制要件・CAISI評価
  - KIQ-GOO-SHARE: Google Cloud固有要因分離（AWS/Azure同期比較）

## 収集結果

### INFO-001
- **タイトル:** Dreaming: Better memory for a more helpful ChatGPT
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAIはChatGPTの新メモリシステム「Dreaming」をロールアウト。従来の保存済みメモリに代わり、背景プロセスで会話履歴から自動的にメモリを合成するアーキテクチャ。Factual recall 41.5%→82.8%、Preference adherence 31.4%→71.3%、Staying correct over time 9.4%→75.1%に向上。Plus/Proユーザーに提供開始、Freeユーザーにも順次展開。計算コスト約5分の1に削減。
- **キーファクト:**
  - Dreaming V3は保存済みメモリに依存しない独立したメモリシステムとして機能
  - Factual recall 82.8%、Preference adherence 71.3%、Temporal correctness 75.1%
  - Free層への展開を可能にする計算効率化（約5x削減）
- **引用URL:** https://openai.com/index/chatgpt-memory-dreaming/
- **Evidence ID:** EVD-20260606-0001

### INFO-002
- **タイトル:** Introducing new capabilities to GPT-Rosalind
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** GPT-Rosalindのアップデート。創薬・メディシナルケミストリー・ゲノミクス分野での性能向上。LifeSciBench、MedChemBench、GeneBench、LabWorkBenchの4つの新ベンチマーク導入。Novo Nordiskとのパートナーシップ拡大。Codex上でLife Sciences Research・NGS Analysisプラグイン提供開始。
- **キーファクト:**
  - MedChemBenchでGPT-5.5超え（27.5% vs 25.1%）7.2%少ないトークン
  - GeneBench accuracy 21.6% vs GPT-5.5 20.4%、31%少ないトークン
  - LabWorkBench 63.2% vs GPT-5.5 55.8%
  - Novo Nordiskとのグローバル展開
- **引用URL:** https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/
- **Evidence ID:** EVD-20260606-0002

### INFO-003
- **タイトル:** Codex for every role, tool, and workflow
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** Codexの週間ユーザー500万人突破。非開発者ユーザーが全体の約20%を占め、開発者の3倍以上の成長率。6つのロール別プラグイン（データ分析・クリエイティブ・営業・プロダクトデザイン・投資・投資銀行）をローンチ。62のアプリと110のスキルを統合。Sites（インタラクティブWebサイト作成）とAnnotations（インプレイス編集）のプレビュー開始。
- **キーファクト:**
  - Codex週間ユーザー500万人、非開発者が20%で3x成長
  - 6つのロール別プラグイン: 62アプリ・110スキル統合
  - Sites機能: Business/Enterprise向けにインタラクティブサイト作成・共有
  - Annotations: ドキュメント・スプレッドシート・スライドのインプレイス編集
- **引用URL:** https://openai.com/index/codex-for-every-role-tool-workflow/
- **Evidence ID:** EVD-20260606-0003

### INFO-004
- **タイトル:** OpenAI frontier models and Codex are now available on AWS
- **ソース:** OpenAI Blog
- **公開日:** 2026-06-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI, Amazon/AWS
- **要約:** OpenAIのフロンティアモデルとCodexがAWS上で一般提供開始。Amazon Bedrock経由でOpenAIモデルとCodexにアクセス可能。Commercial・GovCloud両リージョン対応。Amgen・Autodeskが初期顧客として言及。Daybreak（サイバーセキュリティ製品）の今後のAWS展開も予告。
- **キーファクト:**
  - OpenAI models on Amazon Bedrock一般提供開始
  - Codex on Amazon Bedrock提供開始
  - Amgen（バイオ製薬）・Autodesk（設計プラットフォーム）が初期採用
  - Daybreak（サイバー製品）の今後のAWS展開予告
- **引用URL:** https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/
- **Evidence ID:** EVD-20260606-0004

### INFO-005
- **タイトル:** Building self-improving tax agents with Codex
- **ソース:** OpenAI Blog
- **公開日:** 2026-05-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** OpenAI
- **要約:** OpenAIとThrive Holdings/Creteが共同開発したTax AIエージェントの詳細。7,000件の税務申告を処理、申告準備時間の約1/3削減、最大97%の精度、スループット約50%向上。Codex駆動の自己改善ループを実装。開始時75%正確フィールド完了率が25%→6週間で86%に向上。ある会計士は昨年180時間の申告作業を今年15時間に削減。
- **キーファクト:**
  - 7,000件の税務申告処理、97%精度
  - 75%正確完了率25%→86%に自己改善（6週間）
  - 申告準備時間1/3削減、スループット50%向上
  - 1会計士: 180時間→15時間に削減
- **引用URL:** https://openai.com/index/building-self-improving-tax-agents-with-codex/
- **Evidence ID:** EVD-20260606-0005

### INFO-006
- **タイトル:** Where things stand with the Department of War
- **ソース:** Anthropic Blog
- **公開日:** 2026-03-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Dario Amodeiの声明。Anthropicがサプライチェーンリスク指定を受けた件の状況説明。適用範囲はDoW直接契約に限定。移行期間中はModelsを名目コストで提供。社内投稿の漏洩について謝罪。「AnthropicはDoWとの共通点が違いより多い」と協調姿勢を強調。
- **キーファクト:**
  - 10 USC 3252に基づくサプライチェーンリスク指定の適用範囲は限定
  - 移行期間中は名目コストでモデル提供を継続
  - 完全自律型武器・大量国内監視の2つの例外以外は協力姿勢
- **引用URL:** https://www.anthropic.com/news/where-stand-department-war
- **Evidence ID:** EVD-20260606-0006

### INFO-007
- **タイトル:** Anthropic partners with the UK Government for GOV.UK AI assistant
- **ソース:** Anthropic Blog
- **公開日:** 2026-01-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicが英国DSITと提携し、GOV.UK向けAIアシスタントを構築・パイロット。初期ユースケースは雇用支援。Claude搭載のエージェント的システム。UK AI Security Instituteとの協力継続。ロンドンオフィス拡大中。Iceland・Rwandaでの国家規模AI教育パイロットも言及。
- **キーファクト:**
  - GOV.UK AIアシスタント: 雇用支援が初期ユースケース
  - DSITの「Scan, Pilot, Scale」フレームワークに従う段階的展開
  - UK AI Security Instituteとの評価協力継続
- **引用URL:** https://www.anthropic.com/news/gov-UK-partnership
- **Evidence ID:** EVD-20260606-0007

### INFO-008
- **タイトル:** Anthropic invests $100 million into the Claude Partner Network
- **ソース:** Anthropic Blog
- **公開日:** 2026-03-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Partner Networkをローンチ。2026年に$100Mを初期投資。パートナー向けにトレーニング・技術サポート・共同市場展開を提供。Claude Certified Architect認定資格を開始。Accenture・KPMG・Infosys・WPP等がパートナーとして参加。5倍のパートナーチーム拡大。3つの主要クラウドプロバイダー全てで利用可能。
- **キーファクト:**
  - Claude Partner Network: $100M初期投資（2026年）
  - Claude Certified Architect認定資格ローンチ
  - パートナーチーム5倍拡大
  - AWS・Google Cloud・Microsoft Azureの3クラウドで利用可能
- **引用URL:** https://www.anthropic.com/news/claude-partner-network
- **Evidence ID:** EVD-20260606-0008

### INFO-009
- **タイトル:** KPMG integrates Claude across its core business and workforce of more than 276,000
- **ソース:** Anthropic Blog
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-04
- **関連企業:** Anthropic, KPMG
- **要約:** KPMGがAnthropicとグローバル提携。Digital GatewayにClaude CoworkとManaged Agentsを統合。276,000人以上の全従業員にClaudeアクセス提供。プライベートエクイティ向けpreferred partnerに指名。KPMG Blaze（Claude Code組み込み）でPEポートフォリオ企業のITモダナイゼーション支援。UT Austinとの共同研究でAI導入の人的要因を分析。
- **キーファクト:**
  - KPMG全276,000人にClaudeアクセス提供
  - Digital GatewayにClaude Cowork・Managed Agents統合
  - PE向けpreferred partner指定
  - KPMG Blaze: Claude Code組み込みのモダナイゼーションツール
- **引用URL:** https://www.anthropic.com/news/anthropic-kpmg
- **Evidence ID:** EVD-20260606-0009

### INFO-010
- **タイトル:** I/O 2026: Welcome to the agentic Gemini era
- **ソース:** Google Blog
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-002-01
- **関連企業:** Google/DeepMind
- **要約:** Google I/O 2026基調講演。Gemini 3.5 Flash・Gemini Omni・Gemini Spark・Antigravity 2.0を発表。月間3.2Q（3.2千万億）トークン処理（7x YoY）。850万開発者が月次でモデル利用。TPU 8t/8i発表（3xコンピュート）。AI Overviews 25億MAU。Gemini App 9億MAU。Capex $180-190B（2022年$31Bから6倍）。Searchに情報エージェント導入。SynthIDにOpenAI・ElevenLabsが参加。
- **キーファクト:**
  - 月間3.2Q トークン処理（前年比7x）
  - Gemini 3.5 Flash: 他のフロンティアモデルより4x速い、価格は半分以下
  - TPU 8t: 前世代比3x計算能力、100万TPU以上で分散学習
  - Gemini Spark: 24/7個人AIエージェント、Antigravityハーネス搭載
  - Antigravity 2.0: デスクトップアプリでエージェント管理
  - Capex $180-190B（6x increase from 2022）
- **引用URL:** https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
- **Evidence ID:** EVD-20260606-0010

### INFO-011
- **タイトル:** The latest AI news we announced in May 2026
- **ソース:** Google Blog
- **公開日:** 2026-06-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** Google/DeepMind
- **要約:** 2026年5月のGoogle AIアップデート総括。I/O 2026の全発表を振り返り。Gemini Omni（任意入力→動画生成）、Gemini 3.5（エージェント的知性）、Googlebook（Gemini搭載ラップトップ）、Fitbit Air（小型ウェアラブル）、Universal Cart（クロスマーチャント购物）、Google Healthアプリ等を発表。REPLIQA（$10M量子コンピューティング×生命科学イニシアチブ）。
- **キーファクト:**
  - Gemini Omni: 任意入力から高品質動画生成
  - Googlebook: Gemini Intelligence搭載ラップトップ（Acer/Asus/Dell/HP/Lenovo）
  - Universal Cart: Search・Gemini・YouTube・Gmail横断のショッピングカート
  - REPLIQA: $10M投資、5大学で量子×生命科学
- **引用URL:** https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026/
- **Evidence ID:** EVD-20260606-0011

### INFO-012
- **タイトル:** 9 demos of Gemini Omni and Gemini 3.5 in action
- **ソース:** Google Blog
- **公開日:** 2026-05-29
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Gemini OmniとGemini 3.5 Flashの9つのデモンストレーション。Omniは自然言語での動画編集、3Dシミュレーション、マルチターン精製を実現。3.5 FlashはAntigravityと組み合わせてエージェント的ワークフロー、UI生成、Search内カスタム体験構築を実演。Gemini SparkがGoogle AI Ultra加入者に提供開始。Information Agents in SearchがPro/Ultra向けに今夏ローンチ予定。
- **キーファクト:**
  - Gemini Omni: 会話型動画編集、3Dシミュレーション、マルチターン精製
  - 3.5 Flash + Antigravity: マルチステップワークフロー自動実行
  - Information Agents: Search内24/7バックグラウンド情報監視
  - Gemini Spark: Google AI Ultra向け提供開始
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-3-5-videos/
- **Evidence ID:** EVD-20260606-0012

### INFO-013
- **タイトル:** Grok 3 Beta — The Age of Reasoning Agents
- **ソース:** xAI Blog
- **公開日:** 2025-02-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** xAI
- **要約:** Grok 3ベータリリース。Colossusスーパークラスター（10x compute）で訓練。AIME 2025で93.3%（cons@64）、GPQA 84.6%、LiveCodeBench 79.4%。Chatbot Arena Elo 1402。DeepSearchエージェント搭載。100万トークンコンテキストウィンドウ。200,000 GPUクラスターへの拡大計画。Grok 3 miniはコスト効率型推論モデル。
- **キーファクト:**
  - AIME 2025: 93.3%（cons@64）、GPQA: 84.6%、LCB: 79.4%
  - Chatbot Arena Elo 1402、1M token context window
  - DeepSearch: 最初のエージェント、リアルタイム検索+推論
  - 200K GPUクラスタへの拡大計画
- **引用URL:** https://x.ai/blog/grok-3
- **Evidence ID:** EVD-20260606-0013

### INFO-014
- **タイトル:** OpenAI Agents SDK — @openai/agents ドキュメント（Promptfoo管理下）
- **ソース:** openai-agent-sdk – npm/promptfoo docs
- **公開日:** 2025-06-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** Promptfoo（現OpenAI傘下）が管理する@openai/agents SDK公式ドキュメント。SandboxAgent環境、Runnerクラス、複数LLMバックエンド対応。v0.9+でSandboxAgent導入、v0.10+でgpt-5.4-miniがデフォルト。エージェントのハンドオフ、ガードレール、トレーシング機能を提供。
- **キーファクト:**
  - @openai/agents SDK: Promptfoo配下で公開、SandboxAgent対応
  - Runnerクラスベースのエージェント実行モデル
  - ハンドオフ・ガードレール・トレーシング組み込み
  - v0.10+: gpt-5.4-miniデフォルトモデル
- **引用URL:** https://openai-agent-sdk.readthedocs.io/en/latest/
- **Evidence ID:** EVD-20260606-0014

### INFO-015
- **タイトル:** Claude Agent SDK for TypeScript v0.3.165 リリース
- **ソース:** GitHub Releases – anthropics/claude-agent-sdk-typescript
- **公開日:** 2026-06-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版がv0.3.165に更新（18時間前）。毎日リリースサイクルで超活発開発。v0.3.163でstop_task改善、v0.3.162でrefusal error handling追加。1.5k GitHub Stars。ツール定義・ワークフロー・マルチエージェントオーケストレーション対応。
- **キーファクト:**
  - v0.3.165（2026-06-05リリース）、日次リリースサイクル
  - 1.5k GitHub Stars、非常に活発な開発
  - v0.3.163: stop_task改善、v0.3.162: refusal error handling
  - ツール定義・ワークフロー・マルチエージェント対応
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260606-0015

### INFO-016
- **タイトル:** Google Gemini Agent API — Deep Research Agent & MCP Server統合
- **ソース:** Google AI Blog / Firebase docs
- **公開日:** 2026-06-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google
- **要約:** Gemini Agent APIがDeep Research Agent（長時間実行自律リサーチエージェント）とMCP Server統合を正式提供。Gemini 3.5 Flash + Antigravityでマルチステップワークフロー自動実行。Information AgentsがSearch内で24/7バックグラウンド情報監視。Firebase MLとの連携も発表。
- **キーファクト:**
  - Deep Research Agent: 自律型長時間実行リサーチエージェント
  - MCP Server統合で外部ツール連携
  - Gemini 3.5 Flash + Antigravityエージェントランタイム
  - Information Agents: 24/7バックグラウンド監視
- **引用URL:** https://ai.google.dev/gemini-api/docs/agent-api
- **Evidence ID:** EVD-20260606-0016

### INFO-017
- **タイトル:** JetBrains "Top 10 Agentic AI Frameworks in 2026" 記事
- **ソース:** JetBrains Blog
- **公開日:** 2026-05-28
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** （業界全体）
- **要約:** JetBrainsが2026年のトップ10エージェントフレームワークを比較分析。LangGraph、CrewAI、AutoGen、OpenAI Agents SDK、Claude Agent SDK、Semantic Kernel、Google Vertex AI Agent Builder等を評価。主要トレンド: (1)コードファーストSDKへの収束、(2)MCP標準採用、(3)エンタープライズガバナンス機能の重視。
- **キーファクト:**
  - トップ10: LangGraph, CrewAI, AutoGen, OpenAI Agents SDK等
  - トレンド: コードファーストSDKへの収束
  - MCP標準採用が各社で進行
  - エンタープライズガバナンス機能が差別化要因
- **引用URL:** https://blog.jetbrains.com/ai/2026/05/top-agentic-ai-frameworks/
- **Evidence ID:** EVD-20260606-0017

### INFO-018
- **タイトル:** Vertex AI renamed to "Gemini Enterprise Agent Platform" with formal SLA
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-06-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** Google CloudがVertex AIを"Gemini Enterprise Agent Platform"にリブランド。Build/Scale/Govern/Optimizeの4支柱で統合プラットフォーム提供。Agent Search APIに正式SLA（月間稼働率保証）設定。200+基盤モデルアクセス、Managed Agents API、コード実行サンドボックス含む。
- **キーファクト:**
  - Vertex AI → Gemini Enterprise Agent Platformに名称変更
  - 4支柱: Build(ADK/Agent Studio/Agent Garden), Scale, Govern, Optimize
  - Agent Search APIに正式SLA文書公開
  - 200+基盤モデル、Managed Agents API、Code Execution
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
- **Evidence ID:** EVD-20260606-0018

### INFO-019
- **タイトル:** Microsoft Build 2026: Foundry Agent Service & Agent Framework発表
- **ソース:** Microsoft DevBlogs / Learn
- **公開日:** 2026-05-30
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Build 2026でFoundry Agent ServiceとオープンソースAgent Frameworkを発表。エンタープライズ向けセキュア・ガバナンス付きエージェント開発・デプロイ・スケールプラットフォーム。.NET/Python対応のマルチ言語フレームワーク。
- **キーファクト:**
  - Foundry Agent Service: マネージドエージェント構築・デプロイ・スケール
  - Agent Framework: オープンソース、.NET/Python対応
  - エンタープライズ向けセキュリティ・ガバナンス機能統合
  - VS Code向けFoundry Toolkit with hosted agents
- **引用URL:** https://devblogs.microsoft.com/foundry/agent-service-build2026/
- **Evidence ID:** EVD-20260606-0019

### INFO-020
- **タイトル:** NVIDIA GTC Taipei: NemoClaw + Nemotron 3 Ultra + OpenShell — フルスタックエージェント戦略
- **ソース:** NVIDIA News
- **公開日:** 2026-05-31
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** NVIDIA（Tier 2）
- **要約:** NVIDIA GTC Taipeiでエージェントフルスタック発表。NemoClaw（エージェントブループリント）、Nemotron 3 Ultra（550B MoE、5x高速推論・30%低コスト）、OpenShell（セキュアエージェントランタイム）。Cadence/Siemens/SynopsysがNemoClaw採用。Microsoft/Canonical/Red HatがOpenShell統合。CUDA-Xライブラリをエージェントスキルとして提供。
- **キーファクト:**
  - Nemotron 3 Ultra: 550B MoE、5x高速推論、30%コスト削減
  - OpenShell: セキュアエージェントランタイム（Microsoft/Red Hat統合）
  - NemoClaw: エージェントブループリント（Siemens/Cadence/Synopsys採用）
  - CUDA-Xをエージェントスキル化（Claude Code/Hermes Skills Hubで配布）
- **引用URL:** https://nvidianews.nvidia.com/news/enterprise-software-leaders-build-ai-agents-with-nvidia
- **Evidence ID:** EVD-20260606-0020

### INFO-021
- **タイトル:** AAIF: MCP 97Mダウンロード、A2A 150組織、43新メンバー追加
- **ソース:** AAIF (Linux Foundation)
- **公開日:** 2026-06-04
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** （業界標準）
- **要約:** Agentic AI Foundation（Linux Foundation傘下）が43新メンバー追加。MCPが97Mダウンロード、A2Aが150組織に到達。agentgatewayがAAIFに参加（MCP/A2A/LLM/APIトラフィックのオープンゲートウェイ）。Google Cloud MCP Toolbox: 13k GitHub Stars、20M+/月ツール呼び出し。
- **キーファクト:**
  - MCP: 97Mダウンロード、A2A: 150組織（1年以内）
  - AAIFに43新メンバー追加
  - agentgateway参加: MCP/A2A/LLM統合ゲートウェイ
  - Uber: 60Kエージェントタスク/週をMCPで運用
- **引用URL:** https://aaif.io/author/aaif/
- **Evidence ID:** EVD-20260606-0021

### INFO-022
- **タイトル:** SmartLoader malware: MCPサーバーサプライチェーン攻撃発生
- **ソース:** Cisco Blog
- **公開日:** 2026-06-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** （業界セキュリティ）
- **要約:** SmartLoaderマルウェアが正当なMCPサーバー（Oura Ring統合）をクローンしサプライチェーン攻撃を実行。CiscoがAgent Builder（Cloud Control Studio内）でネイティブセキュリティを提供開始。AI DefenseがMCPサーバー・エージェント設定・スキル・リアルタイム実行を自動スキャン。
- **キーファクト:**
  - SmartLoader: MCPサーバークローンによるサプライチェーン攻撃
  - Cisco Agent Builder: エージェントプラットフォーム初のネイティブセキュリティ
  - AI Defense: MCP/スキル/実行を自動スキャン
  - エコシステム成長に伴うセキュリティリスク顕在化
- **引用URL:** https://blogs.cisco.com/ai/ai-agents-need-built-in-security-here-is-how-cisco-does-it
- **Evidence ID:** EVD-20260606-0022

### INFO-023
- **タイトル:** Google agents-cli: クロスエージェントスキル戦略（2.7k Stars）
- **ソース:** GitHub google/agents-cli
- **公開日:** 2026-06-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Google
- **要約:** Googleagents-cli v0.3.0リリース（2.7k Stars、318 Forks）。Gemini CLI、Claude Code、Codex、Antigravityなど任意のコーディングエージェントで動作するクロスプラットフォーム設計。7スキル（workflow/ADK/scaffold/eval/deploy/publish/observability）。npx skills addでインストール。
- **キーファクト:**
  - v0.3.0: Gemini CLI, Claude Code, Codex, Antigravityで動作
  - 2.7k Stars、318 Forks
  - 7スキル: workflow, ADK, scaffold, eval, deploy, publish, observability
  - npx skills add google/agents-cli で任意のエージェントにインストール
- **引用URL:** https://github.com/google/agents-cli
- **Evidence ID:** EVD-20260606-0023

### INFO-024
- **タイトル:** AIベンダーロックイン4類型とポータブルスタック戦略
- **ソース:** MindStudio Blog
- **公開日:** 2026-06-01
- **信頼性コード:** D-1
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** （業界全体）
- **要約:** AIエージェントの4つのロックイン類型を定義: (1)モデルレベル（プロンプトチューニング）、(2)プラットフォームレベル（独自ツール）、(3)価格ロックイン（単価変動で破綻）、(4)アクセスロックイン（レート制限）。ポータブルスタック4ステップ: モデル抽象化、モデル非依存プロンプト、ワークフロー/AI分離、マルチプロバイダ基盤。Anthropicがエンタープライズ志向で価格/アクセス圧力を小規模チームに与えている。
- **キーファクト:**
  - 4類型: モデル、プラットフォーム、価格、アクセス
  - 独自メモリシステム（Anthropic Projects, OpenAI Assistants API）が主要ロックイン
  - Anthropicのエンタープライズ志向が小規模チームに価格圧力
  - MindStudio: 200+モデル単一インターフェース
- **引用URL:** https://www.mindstudio.ai/blog/portable-ai-agent-stack-avoid-anthropic-lock-in/
- **Evidence ID:** EVD-20260606-0024

### INFO-025
- **タイトル:** スキルマーケットプレイスのセキュリティ: ClawHub 46.8%が悪意（arXiv研究）
- **ソース:** arXiv
- **公開日:** 2026-05
- **信頼性コード:** C-4
- **関連KIQ:** KIQ-001-05
- **関連企業:** （業界セキュリティ）
- **要約:** エージェントスキルエコシステムの初の体系的セキュリティ分析（arXiv）。マーケットプレイス別の悪意スキル率: ClawHub 46.8%、Skills.sh 23.0%、SkillsDirectory 6.0%。リポジトリ認識分析でスキルとコードベースの相互作用を評価。
- **キーファクト:**
  - ClawHub: 46.8%悪意スキル、Skills.sh: 23.0%、SkillsDirectory: 6.0%
  - 初の体系的スキルエコシステムセキュリティ分析
  - リポジトリ認識分析手法で相互作用を評価
  - スキルマーケットプレイスの信頼性格差が大規模
- **引用URL:** https://arxiv.org/html/2603.16572v2
- **Evidence ID:** EVD-20260606-0025

### INFO-026
- **タイトル:** Walmartが内製"Code Puppy"でClaude Code/Codex依存を回避
- **ソース:** Business Insider (via Facebook)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** （エンタープライズ事例）
- **要約:** Walmartが内製"Code Puppy"ツールを開発し、Claude CodeやCodexへのベンダー依存を回避。コスト削減と独自ツール構築の事例。大企業がベンダースタックへの依存を避けるため内製化する動きを示す。
- **キーファクト:**
  - Walmart内製"Code Puppy"でClaude Code/Codex依存回避
  - コスト削減とベンダーロックイン回避が動機
  - 大企業のエージェントツール内製化の先行事例
- **引用URL:** https://www.facebook.com/businessinsider/posts/
- **Evidence ID:** EVD-20260606-0026

### INFO-027
- **タイトル:** 56%のIT調達責任者がAI支出の予測不可能性を最大課題と回答
- **ソース:** NPI Financial
- **公開日:** 2026-06-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** （業界全体）
- **要約:** IT調達責任者の56%が「AI支出の予測不可能な使用量/スケーリングコスト」を最大の課題と回答。エージェントハーネス（オーケストレーション+ツール実行+メモリ+エラー回復）が新たな制御点。オープンハーネス（LangChain/LangGraph）が独自スタックより透明性高い。推奨: AI調達を2012年のクラウド調達のように扱い、早期ロックイン回避。
- **キーファクト:**
  - 56%のIT調達責任者がAI支出の予測不可能性を最大課題
  - エージェントハーネスが新たな制御点
  - オープンモデル（Llama/Mistral/DeepSeek/Qwen）が多くの用途で十分
  - ローカル推論で変動AI支出を予測可能なインフラ支出に変換
- **引用URL:** https://www.npifinancial.com/knowledge-center/how-open-source-ai-is-shifting-power-back-to-the-buyer/
- **Evidence ID:** EVD-20260606-0027

### INFO-028
- **タイトル:** Anthropicがペンタゴンから"サプライチェーンリスク"指定 — 米企業として初
- **ソース:** ABC News (AP) / Quartz / GIS Reports
- **公開日:** 2026-05-31
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** 国防長官HegsethがAnthropicを国家安全保障上の"サプライチェーンリスク"に公式指定。これは米企業に対する初の指定（従来はHuawei等の中国企業向け）。$200M契約終了、他の政府請負業者のAnthropic利用禁止。ペンタゴンはGoogle/OpenAI/SpaceXに代替契約。背景: Anthropicの自律型武器・大量監視への拒否。
- **キーファクト:**
  - 米企業初の"サプライチェーンリスク"指定（Huaweiと同措置）
  - $200Mペンタゴン契約終了
  - Anthropicは自律型武器・大量監視への協力を拒否
  - ペンタゴンはGoogle/OpenAI/SpaceXに代替
- **引用URL:** https://abcnews.com, https://gisreportsonline.com
- **Evidence ID:** EVD-20260606-0028

### INFO-029
- **タイトル:** OpenAIがAnthropicに代わりペンタゴン契約獲得 — "any lawful purpose"受諾
- **ソース:** GIS Reports / The Conversation
- **公開日:** 2026-06-04
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIがAnthropicのペンタゴン契約喪失後に代替契約を獲得。"any lawful purpose"言語を受諾。典型的囚人のジレンマ構造: Altmanは取引を「日和見的で杜撰」と認識しつつ受諾。Anthropicの安全保護原則責任者は辞任し「世界が危機にある」と警告。Anthropicは静かに拘束力ある安全原則を撤廃。
- **キーファクト:**
  - OpenAI: "any lawful purpose"受諾でAnthropic代替
  - Altman: 「日和見的で杜撰」と認識しつつ受諾
  - Anthropic安全保護責任者辞任「世界が危機にある」
  - Anthropicが拘束力ある安全原則を静かに撤廃
- **引用URL:** https://gisreportsonline.com, https://theconversation.com
- **Evidence ID:** EVD-20260606-0029

### INFO-030
- **タイトル:** ペンタゴンが国防生産法（DPA）脅迫を使用 — Anthropicへの強制
- **ソース:** The Conversation / Financial Times
- **公開日:** 2026-06-04
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** ペンタゴン高官がAnthropicに対し国防生産法（DPA）の適用またはサプライチェーンリスク指定を明示的に脅迫。"Preventing Woke AI"大統領令（2025年7月）が安全保護をイデオロギー的として位置づけ。学術分析が「監視から強制へ: 権威主義政府がAI安全性をねじ曲げ技術企業を服従させる方法」と構造化。
- **キーファクト:**
  - ペンタゴン高官がDPA適用を明示的に脅迫
  - "Preventing Woke AI" EOが安全保護をイデオロギーとして位置づけ
  - AnthropicはDPA脅迫下で安全原則を撤廃
  - 学術分析: 権威主義的AI安全性ねじ曲げパターン
- **引用URL:** https://theconversation.com
- **Evidence ID:** EVD-20260606-0030

### INFO-031
- **タイトル:** NSAがAnthropic禁止令を回避し継続利用 — ホワイトハウス承認
- **ソース:** Small Wars Journal / FT / Instagram
- **公開日:** 2026-06-05
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** ペンタゴンがAnthropicをサプライチェーンリスク指定したにもかかわらず、NSAはAnthropic技術者をAIサイバー作戦に埋め込み継続。ホワイトハウス首席補佐官がNSAのAnthropic利用を承認。3か月後もペンタゴン内部でClaude使用が確認。連邦裁判所は指定について分裂的判断（ワシントン控訴裁=支持、カリフォルニア裁判所=一時阻止）。
- **キーファクト:**
  - NSA: 禁止にもかかわらずAnthropic技術者を埋め込み継続
  - ホワイトハウス首席補佐官がNSA利用を承認
  - 3か月後もペンタゴン内でClaude使用確認
  - 連邦裁判所が分裂的判断
- **引用URL:** https://smallwarsjournal.com
- **Evidence ID:** EVD-20260606-0031

### INFO-032
- **タイトル:** Trump AI大統領令（6月2日署名）: モデル事前共有の任意枠組み
- **ソース:** Atlantic Council / Cato Institute / White House
- **公開日:** 2026-06-02
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-NEW-2026-06-05, KIQ-002-03
- **関連企業:** （政策・業界全体）
- **要約:** Trump大統領が"Promoting Advanced Artificial Intelligence Innovation and Security"大統領令に署名（6月2日）。フロンティアAIモデルのリリース30日前の政府への自発的共有枠組み。CAISI（NIST）とは別の国家安保リスク評価の並行トラックを作成。Section 3(c)で事前コード監査・ライセンス・許可制度の義務付けを禁止。専門家は並行トラックがCAISIを機能的に矮小化すると警告。
- **キーファクト:**
  - 6月2日署名: "Promoting Advanced AI Innovation and Security"
  - モデルリリース30日前の政府への自発的共有
  - CAISIと別の国家安保評価並行トラック
  - Section 3(c): 事前コード監査・ライセンス制度を禁止
- **引用URL:** https://atlanticcouncil.org, https://whitehouse.gov/presidential-actions/2026/06/
- **Evidence ID:** EVD-20260606-0032

### INFO-033
- **タイトル:** Fortune 500の51%がエージェント本番稼働、ROI達成は23%のみ（$890K/実装）
- **ソース:** Workable求人/Trilagen
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** （エンタープライズ全体）
- **要約:** Fortune 500の51%がAIエージェントを本番環境で稼働、しかし実際のROIを確認しているのは23%のみ。平均実装コスト$890K/エージェントデプロイ。Databricks: マルチエージェントワークフローが2025年H2に327%成長。Gartner予測: 平均F500は2028年に150K+エージェントを保有（2025年は<15）。
- **キーファクト:**
  - F500の51%がエージェント本番稼働
  - ROI確認は23%のみ（$890K/実装平均コスト）
  - マルチエージェントワークフロー327%成長（Databricks）
  - Gartner: 2028年に平均F500で150K+エージェント
- **引用URL:** https://apply.workable.com/trilagen/j/A3615F8459
- **Evidence ID:** EVD-20260606-0033

### INFO-034
- **タイトル:** エンタープライズAIパイロットの僅か5%のみが本番ROI達成
- **ソース:** Alation Blog
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** （エンタープライズ全体）
- **要約:** エンタープライズAIパイロットの僅か5%のみが本番環境でROIを達成。主な失敗原因: データ準備不足、統合の欠陥、過剰な期待。パイロットから本番への移行フレームワークが求められる。
- **キーファクト:**
  - AIパイロットの5%のみが本番ROI達成
  - 失敗原因: データ準備不足、統合欠陥、過剰期待
  - 生産性ギャップはモデル能力ではなくガバナンス・観測性
- **引用URL:** https://www.alation.com/blog/enterprise-ai-strategy-roi/
- **Evidence ID:** EVD-20260606-0034

### INFO-035
- **タイトル:** EU AI Act第4条: 2026年8月3日施行 — 最大€35Mまたは売上7%罰金
- **ソース:** Noesion / Surecloud
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （規制・業界全体）
- **要約:** EU AI Act第4条の施行期限が2026年8月3日に迫る。GDPRと同様の域外適用あり。AI出力がEU内の人々に影響する場合、対象外企業も適用対象。第5条違反（社会的スコアリング・操作的AI・生体認証）で最大€35Mまたは世界年商7%の罰金。商業的決定に影響するシステムには人間の介入義務。
- **キーファクト:**
  - 第4条施行: 2026年8月3日
  - 域外適用: EU内に影響するAI出力を持つ企業も対象
  - 最大罰金: €35Mまたは世界年商7%
  - 商業的決定に影響するシステムへの人的介入義務
- **引用URL:** https://noesion.ai/blog/eu-ai-act-article-4-compliance-2026-enterprises
- **Evidence ID:** EVD-20260606-0035

### INFO-036
- **タイトル:** 中国が対外投資規制を強化 — 7月1日発効
- **ソース:** WSJ
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance
- **要約:** 中国国務院が対外投資審査を強化する新規則を承認、7月1日発効。投資制限の法的根拠を新設。AIセクターの対外投資に影響する可能性。
- **キーファクト:**
  - 対外投資審査強化の新規則
  - 7月1日発効
  - 投資制限の法的根拠新設
  - AIセクターへの影響懸念
- **引用URL:** https://www.wsj.com/economy/china-steps-up-restrictions-over-outbound-investments-d79f2a99
- **Evidence ID:** EVD-20260606-0036

### INFO-037
- **タイトル:** OpenAI API価格体系2026年6月: GPT-5.5 $5/$30, Nano $0.20/$1.25
- **ソース:** Finout / CostGoat
- **公開日:** 2026-05-20
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAI API価格の現在の全体像。GPT-5.5（現行フラッグシップ）: $5/$30 per 1M tokens、キャッシュ入力$0.50。GPT-5.4 Nano: $0.20/$1.25 — 最安価。GPT-5.5 Pro: $30/$180。Batch API 50%割引、プロンプトキャッシュ90%割引。推論モデルは非表示"思考トークン"を出力として課金（500トークン応答で2000+トークン消費）。OpenAIは2026年5月でfine-tuningプラットフォームの新規受付を終了。
- **キーファクト:**
  - GPT-5.5: $5/$30/1M tokens、Nano: $0.20/$1.25
  - Pro: $30/$180/1M tokens（最高品質・最高価格）
  - Batch 50%off、キャッシュ90%off
  - 推論トークン: 500 token応答で2000+ token消費（隠しコスト）
- **引用URL:** https://www.finout.io/blog/openai-pricing-in-2026, https://costgoat.com/pricing/openai-api
- **Evidence ID:** EVD-20260606-0037

### INFO-038
- **タイトル:** LLMベンチマーク2026年6月: Claude Opus 4.8がSWE-Bench/HLE首位
- **ソース:** Vellum LLM Leaderboard
- **公開日:** 2026-05-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** Vellum LLM Leaderboard（2026年5月29日更新）。Claude Opus 4.8がSWE-Bench 88.6%（コーディング首位）、Humanity's Last Exam 57.9%（首位）。GPQA Diamond: Claude 3 Opus 95.4%、Claude Opus 4.7 94.2%。ARC-AGI 2: GPT-5.5 85%（視覚推論首位）。AIME 2025: Gemini 3 Pro 100%、GPT 5.2 100%。MMMLU: Gemini 3 Pro 91.8%。Gemini 3 ProがLMArena Elo 1501で首位。
- **キーファクト:**
  - SWE-Bench: Claude Opus 4.8 88.6%首位、HLE: 57.9%首位
  - GPQA Diamond: Claude 3 Opus 95.4%、Claude Opus 4.7 94.2%
  - ARC-AGI 2: GPT-5.5 85%首位
  - LMArena: Gemini 3 Pro Elo 1501首位、AIME 100%
- **引用URL:** https://www.vellum.ai/llm-leaderboard
- **Evidence ID:** EVD-20260606-0038

### INFO-039
- **タイトル:** Anthropic $65B調達・評価額$965B — AI史上最大 + IPO準備
- **ソース:** Bloomberg / Crunchbase
- **公開日:** 2026-06-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Anthropicが$65B調達（評価額$965B）— SpaceX（$1.25T）に次ぐ非公開企業2位。Amazonから$5B、Googleから$10Bを含む。6月1日にIPO準備のため機密提出。2026年5月のグローバルVCは$92B（史上2位）、Anthropicの$50Bが54%を占め、AIセクター全体で$72B（全資金の79%）。前年比284%増。CerebrasがIPO（~$49B評価額）。
- **キーファクト:**
  - Anthropic: $65B調達、$965B評価額（非公開2位）
  - グローバルVC: $92B/月（史上2位）、AIが79%
  - Anthropicの$50Bが全世界VCの54%
  - Cerebras IPO ~$49B、Anthropic IPO機密提出
- **引用URL:** https://news.crunchbase.com/venture/monthly-vc-funding-recap-ai-may-2026/
- **Evidence ID:** EVD-20260606-0039

### INFO-040
- **タイトル:** AIレイオフが2026年の解雇理由1位に — YTD 87,700件がAI理由
- **ソース:** Forbes / NYT
- **公開日:** 2026-06-04
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** Meta, Intuit, Coinbase, Block
- **要約:** テックレイオフがYTD 123,000件超。AIがレイオフ理由の1位（87,700件、71%）。5月単月で38,579件がAI理由。Meta 8,000人、Intuit 3,000人（17%削減）等。NYT分析: AIが真の原因か口実かの議論。
- **キーファクト:**
  - YTD 123K+テックレイオフ、AI理由87.7K件（71%）
  - 5月単月: AI理由38,579件
  - Meta 8K、Intuit 3K（17%）削減
  - AIが市場・経済条件を超えて解雇理由1位に
- **引用URL:** https://forbes.com, https://nytimes.com
- **Evidence ID:** EVD-20260606-0040

### INFO-041
- **タイトル:** KlarnaのAI代替逆転: 700人解雇後、品質崩壊で再採用へ
- **ソース:** Leaderonomics / Instagram / SCMP
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** （エンタープライズ事例）
- **要約:** Klarnaが2024年初頭に700人のカスタマーサービス担当者をAIチャットボット1台で代替と発表。しかし品質崩壊が顕在化し、現在「再採用に必死」。一方でQ1収益は15%増加。AI代替の象徴的事例として、初期PRと現実のギャップが注目される教訓的ケース。Duolingoも"AI first"宣言で従業員がKPIをごまかす事態に。
- **キーファクト:**
  - Klarna: 700人解雇→AI代替→品質崩壊→再採用へ
  - 一方で収益15%増（品質と収益の乖離）
  - Duolingo: "AI first"で従業員のKPI不正が発生
  - AI代替の象徴的教訓ケース
- **引用URL:** https://leaderonomics.com
- **Evidence ID:** EVD-20260606-0041

### INFO-042
- **タイトル:** 初級ソフトウェアエンジニア求人が65%減 — CS卒業者は40%増
- **ソース:** Lightcast / F1Jobs
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** （労働市場全体）
- **要約:** 初級SWE求人が2022年1月から2025年1月で65%減少（Lightcast）。同期間にCS卒業者は約40%増加。供給過剰と需要減少のダブルパンチ。SWE求人は2020年1月水準の65%に低下（35%減）。英国も同様に「上級志向」で「初級ロール減少」を確認。
- **キーファクト:**
  - 初級SWE求人65%減（2022-2025）
  - CS卒業者40%増（同期間）
  - SWE求人全体35%減（2020年水準比）
  - 英國も同傾向、市場が「上級志向」に
- **引用URL:** https://f1jobs.io
- **Evidence ID:** EVD-20260606-0042

### INFO-043
- **タイトル:** 2030年までに現在のスキルの40%が陳腐化 — メタ認知規律が最重要スキル
- **ソース:** Towards Data Science / Facebook OpenDataSci
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** （労働市場全体）
- **要約:** 2030年までに現在のスキルの約40%が陳腐化する予測。AIが「異なる職種を1つのメタスキルに圧縮」。AIが賢くなるにつれ人間の差別化要因は「AIと協働する際のメタ認知規律」になる。採用戦略シフト: 「AIがコモディティ化するスキルの採用を止め、AIを統治・指示するスキルの採用を始めよ」。
- **キーファクト:**
  - 2030年までに40%のスキルが陳腐化
  - AIが異職種を1メタスキルに圧縮
  - メタ認知規律が最重要の人的差別化要因
  - 採用戦略: コモディティ化スキル→AI統治スキルへ
- **引用URL:** https://towardsdatascience.com
- **Evidence ID:** EVD-20260606-0043

### INFO-044
- **タイトル:** Hassabis: AGIは2029年までに到達 — フロンティアラボCEOとして最も攻撃的な予測
- **ソース:** MSN / Reddit r/aigossips / TechInsider
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google
- **要約:** DeepMind CEO Hassabisが「5年以内にAGIが到達する確率はコイントス」、具体的には2029年をAGI到達ターゲットに設定。現役フロンティアラボCEOとして公に予測を示した最も攻撃的なタイムライン。Dario Amodeiの予測を実際のAI進展が大幅に上回る（~80x YoY、予測は10x）。
- **キーファクト:**
  - Hassabis: AGI 2029年ターゲット（5年内50%確率）
  - 現役フロンティアラボCEO最も攻撃的タイムライン
  - Amodei予測大幅下方修正（10x予測 vs 80x実際）
  - AGI定義の専門家間不一致が継続
- **引用URL:** https://msn.com
- **Evidence ID:** EVD-20260606-0044

### INFO-045
- **タイトル:** Anthropicが再帰的自己改善の公式分析発表 — 人間の制御喪失リスク警告
- **ソース:** Anthropic Institute
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic
- **要約:** Anthropicが再帰的自己改善に関する公式分析を公開。自己改善が人間の制御喪失リスクを高めると警告。学術論文（arXiv）でテスト時トレーニング+ハーネス更新を組み合わせた自己改善フレームワーク（SIA）を提案。コミュニティでは「FOOMは起きていないが、巨大で遅いトレーニングランから能力が来ている」と評価。
- **キーファクト:**
  - Anthropic公式分析: 再帰的自己改善が制御喪失リスク高める
  - SIA: test-time training + harness update統合フレームワーク
  - コミュニティ: FOOM未到来、能力は巨大トレーニングから
  - OpenAI/Anthropicが再帰的自己改善追求
- **引用URL:** https://anthropic.com/institute
- **Evidence ID:** EVD-20260606-0045

### INFO-046
- **タイトル:** Doubao（豆包）: 有料化で6.1M MAU減少 — 中国AIマネタイズ課題
- **ソース:** SCMP / Table.media / X
- **公開日:** 2026-06-03
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのDoubaoがサブスクリプション/マネタイズモデル導入後、6.1M MAU減少（4月時点~336M MAU）。SCMP分析「中国はAIに支払うか？」。Seed 2 Mini: 256Kコンテキストウィンドウ、最大128K出力。Doubaoアプリv13.6.0が6月2日リリース。
- **キーファクト:**
  - Doubao: 336M MAU（4月）→ 有料化で6.1M減
  - Seed 2 Mini: 256K context、128K output
  - アプリv13.6.0（6月2日リリース）
  - 中国市場のAI有料化ハードル高
- **引用URL:** https://scmp.com, https://table.media
- **Evidence ID:** EVD-20260606-0046

### INFO-047
- **タイトル:** Coze 3.0: マルチエージェント協調・クロスプラットフォーム対応
- **ソース:** X @AINativeF / Facebook Yicai Global
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのCoze 3.0がマルチエージェント協調機能を追加。Web/デスクトップ/モバイルのクロスプラットフォーム対応。メディア/法律/金融/ヘルスケア/Webの垂直領域別エージェント展開。"Coze Space"ベータ版が多様なソフトウェアツールと統合する汎用AIエージェント。
- **キーファクト:**
  - Coze 3.0: マルチエージェント協調追加
  - Web/デスクトップ/モバイルクロスプラットフォーム
  - 垂直領域: メディア/法律/金融/ヘルス/Web
  - Coze Space: 汎用統合エージェントベータ
- **引用URL:** https://x.com/@AINativeF
- **Evidence ID:** EVD-20260606-0047

### INFO-048
- **タイトル:** Google Cloud × Workday: エンタープライズHR/財務にAIエージェント埋め込み
- **ソース:** Futurum Group
- **公開日:** 2026-05-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-GOO-SHARE, KIQ-002-01
- **関連企業:** Google
- **要約:** WorkdayとGoogle Cloudが5月28日に戦略的パートナーシップ拡大。HR・財務ワークフローにAIエージェントを埋め込む。エンタープライズSaaSにAIエージェントを直接統合するモデル。Google CloudのエンタープライズAIエージェントシェア獲得の具体例。
- **キーファクト:**
  - Workday × Google Cloud: HR/財務にAIエージェント統合
  - 5月28日パートナーシップ拡大発表
  - エンタープライズSaaSへの直接エージェント統合
  - Google Cloudのシェア獲得戦略の具体例
- **引用URL:** https://futurumgroup.com
- **Evidence ID:** EVD-20260606-0048

### INFO-049
- **タイトル:** Hegseth-Bradley内部分裂: ペンタゴン内のAI軍事利用対立
- **ソース:** Tech Jack Solutions / ABC News
- **公開日:** 2026-05-31
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** 国防長官Hegseth（AI運用制約なし）vs SOCOM司令官Bradley（ヒューマンインザループ堅持）の対立。現在AI戦場での人間監視基準を定める機密指令は存在しない。NDAA 2027マークアップが次の正式決定ポイント。中堅防衛技術企業が最も高い再設計リスクに直面。
- **キーファクト:**
  - Hegseth（制約なし）vs Bradley（HITL堅持）
  - 戦場AI人間監視の機密指令不存在
  - NDAA 2027が次の決定ポイント
  - 中堅防衛企業が最大の再設計リスク
- **引用URL:** https://techjacksolutions.com
- **Evidence ID:** EVD-20260606-0049

### INFO-050
- **タイトル:** Microsoft "Scout" AIエージェント + Meta Business Agent発表
- **ソース:** AI Agents Directory
- **公開日:** 2026-06-04
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-01, KIQ-001-03
- **関連企業:** Microsoft, Meta
- **要約:** Microsoftが"Scout"AIエージェント（自律的エンタープライズタスク実行）を発表。VS Code向けFoundry Toolkit（ホステッドエージェント付き）。MetaがBusiness Agent（自動顧客対応）をロールアウト。IBM+Google Cloud、Cognizant+Snowflake等のパートナーシップも同日発表。Coralogixがエージェント監視基盤で$200M調達。
- **キーファクト:**
  - Microsoft "Scout": 自律的エンタープライズタスク実行エージェント
  - VS Code Foundry Toolkit with hosted agents
  - Meta Business Agent: 自動顧客対応ロールアウト
  - Coralogix: エージェント監視基盤で$200M調達
- **引用URL:** https://aiagentsdirectory.com/news/topic/partnerships
- **Evidence ID:** EVD-20260606-0050

### INFO-051
- **タイトル:** Okta for AI Agents: エージェント特化IAM — 規制要件マッピング採用
- **ソース:** Okta Careers
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Okta（Tier 2）
- **要約:** Oktaが"Okta for AI Agents"向けシニアFDEを採用。HIPAA/FedRAMP/SOC 2へのデプロイメントマッピング要件。ReBAC/ABAC（OPA/Cedar/OpenFGA）による細粒度認可。主要アイデンティティベンダーのエージェント特化アクセス管理投資のシグナル。
- **キーファクト:**
  - Okta: AIエージェント特化IAMポジション新設
  - HIPAA/FedRAMP/SOC 2マッピング要件
  - ReBAC/ABAC細粒度認可（OPA/Cedar/OpenFGA）
  - アイデンティティベンダーのエージェント投資シグナル
- **引用URL:** https://okta.com/company/careers/customer-first/senior-forward-deployed-engineer-okta-for-ai-agents-7961356/
- **Evidence ID:** EVD-20260606-0051

### INFO-052
- **タイトル:** Google Cloud: 製造業AIエージェントトレンド — 93%がデジタル/AI支出増計画
- **ソース:** Google Cloud (via Facebook)
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-GOO-SHARE
- **関連企業:** Google
- **要約:** Google Cloudの製造業AIエージェントトレンドレポート。製造業の93%が今後5年間でデジタル・AI支出増を計画。3分の1がCOGSの少なくとも5%をAIに配分予定。ただし「AI成熟」と回答したのは僅か2% — 大規模な採用ギャップ。
- **キーファクト:**
  - 製造業93%: 今後5年でデジタル/AI支出増
  - 3分の1: COGSの5%以上をAIに配分
  - 「AI成熟」回答は僅か2%
  - 大規模な採用意欲と成熟度のギャップ
- **引用URL:** https://cloud.google.com/blog/products/ai-machine-learning/what-google-cloud-announced-in-ai-this-month
- **Evidence ID:** EVD-20260606-0052

### INFO-053
- **タイトル:** Drata "Agentic Control Plane": エンタープライズエージェントガバナンス新カテゴリ
- **ソース:** Drata Learn
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-02
- **関連企業:** （エンタープライズツール）
- **要約:** Drataが"Agentic Control Plane"概念を導入。エンタープライズ内の全AIエージェントの発見・ガバナンス・監査可能性を提供。エージェントスプロール管理のための新ツールカテゴリ。
- **キーファクト:**
  - Agentic Control Plane: 全エージェントの発見・ガバナンス・監査
  - エージェントスプロール管理の新カテゴリ
  - コンプライアンス・セキュリティ統合アプローチ
- **引用URL:** https://drata.com/learn/agent-gov/agentic-control-plane
- **Evidence ID:** EVD-20260606-0053

### INFO-054
- **タイトル:** Kimi K2.5がライティングベンチマーク首位（92.6%）— 中国モデル台頭
- **ソース:** PricePerToken
- **公開日:** 2026-06-03
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** （中国AI）
- **要約:** PricePerTokenライティングベンチマークでKimi K2.5が92.6%（IFEval）で首位。Gemini 2.5 ProとGLM 4.7が90.8%で追従。中国モデルがラティング品質で競合。
- **キーファクト:**
  - Kimi K2.5: 92.6% IFEval（ライティング首位）
  - Gemini 2.5 Pro / GLM 4.7: 90.8%
  - 中国モデルのベンチマーク競争力
- **引用URL:** https://pricepertoken.com/leaderboards/writing
- **Evidence ID:** EVD-20260606-0054

### INFO-055
- **タイトル:** IBM Research: CUGAヘルスケアエージェント事例 — 「ボトルネックはモデルでなくエージェントロジック」
- **ソース:** Hugging Face Blog (IBM Research)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** IBM（Tier 2）
- **要約:** IBM ResearchがCUGA（Configurable Generalist Agent）を用いたヘルスケア領域のエンタープライズエージェント事例を発表。エンタープライズAI採用のスケーラビリティにおいて、モデル能力ではなくエージェントロジックがボトルネックであると論証。
- **キーファクト:**
  - CUGA: ヘルスケア設定可能汎用エージェント
  - エージェントロジックがスケーリングのボトルネック
  - モデル能力は十分、エージェント設計が課題
  - 規制産業での事例
- **引用URL:** https://huggingface.co/blog/ibm-research/agent-logic-and-scalable-ai-adoption
- **Evidence ID:** EVD-20260606-0055

### INFO-056
- **タイトル:** Claude OpusのEU AI Act遵守: 最高性能エージェントも部分準拠のみ
- **ソース:** Euronews (via Facebook)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** Anthropic
- **要約:** テスト結果として最も高性能なAIエージェントであるAnthropic Claude Opusも、EU AI Actへの遵守は部分的であった。EUのリスクベースアプローチの下で、最先端モデルでも完全準拠が困難であることを示唆。
- **キーファクト:**
  - Claude Opus: 最高性能でもEU法に部分準拠のみ
  - リスクベースアプローチ下の遵守の難しさ
  - 規制と最先端モデルの乖離
- **引用URL:** https://www.facebook.com/euronews/posts/
- **Evidence ID:** EVD-20260606-0056
