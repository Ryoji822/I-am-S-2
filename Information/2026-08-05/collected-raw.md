# 収集データ: 2026-08-05

## メタデータ
- 収集日時: 2026-08-05 00:00 UTC
- 品質フラグ: COMPLETE
- 検索クエリ実行数: 121/121 (collection_plan.json全件) + 7 (Arbiter動的クエリ) = 128
- 深掘りスクレイプ数: 3 (kai-waehner.de Trusted Agentic AI Landscape / uvik.net Claude Code comparison / algorithmic.co vendor lock-in)
- 公式ブログスクレイプ数: 4 (Anthropic公式)
- INFO総数: 80
- Evidence ID範囲: EVD-20260805-0001 ～ EVD-20260805-0080
- KIQカバレッジ: 24/24 KIQs全覆盖
  - KIQ-001-01～05: ✅ 完了
  - KIQ-002-01～06: ✅ 完了
  - KIQ-003-01～05: ✅ 完了
  - KIQ-004-01～04: ✅ 完了
  - KIQ-005-01～03: ✅ 完了
  - BYTEDANCE-CHINESE: ✅ 完了
- Arbiter優先KIQ動的クエリ: 7件実行
  - KIQ-OAI-001: 部分打破（政府vs民間内訳百分比分離依然不在）
  - KIQ-ANT-002: 部分打破（Claude Code WAU倍増確認・絶対値・内訳依然不在）
  - KIQ-MIL-001: 不在継続（人間却下比率定量データ完全不在）
  - KIQ-CAR-002-OPS: 不在継続（設計/評価固有データ不在・複合カテゴリーのみ）
  - KIQ-FLI-001: 不在継続（security≠safety確認・RFPでsafety直接言及なし）
  - SCN-003: 部分打破（Big Tech合計$500B確認・「3社」内訳依然未確認）
  - H-BTD-002: 部分打破（TikTok年間数十億ドル損失確認・AI事業赤字幅推移定量データ不在）

## 収集結果

### INFO-001
- **タイトル:** Anthropic invests $100 million into the Claude Partner Network
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-03-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropicは企業のClaude採用を支援するパートナー組織向けプログラム「Claude Partner Network」を立ち上げ、2026年に初期$100Mを投じる。パートナー向けトレーニング、技術サポート、市場開発支援を含む。Claude Certified Architect認定試験とCode Modernizationスターターキットも提供開始。
- **キーファクト:**
  - $100Mの初期投資、パートナーチーム5倍拡大
  - Claude Certified Architect (Foundations) 認定試験を本日より提供
  - ClaudeはAWS、Google Cloud、Microsoftの3大手クラウド全てで利用可能な唯一のフロンティアAIモデル
  - Accentureが30,000名のClaudeトレーニングを実施中
- **引用URL:** https://www.anthropic.com/news/claude-partner-network
- **Evidence ID:** EVD-20260805-0001

### INFO-002
- **タイトル:** Introducing Claude Opus 5
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-07-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-005-01
- **関連企業:** Anthropic
- **要約:** Claude Opus 5をリリース。Fable 5に近い知能を半額で提供し、Frontier-Bench v0.1、CursorBench 3.2、ARC-AGI 3等でstate-of-the-art。Opus 4.8と同価格（$5/M入力トークン、$25/M出力トークン）。
- **キーファクト:**
  - Frontier-Bench v0.1で全モデル首位、Opus 4.8の2倍以上の性能
  - ARC-AGI 3で次点モデルの3倍のスコア
  - 価格: $5/M入力、$25/M出力（Opus 4.8と同等）
  - Claude Maxのデフォルトモデル、Claude Proの最強モデル
  - サイバーセキュリティではMythos 5に依然劣位（エクスプロイト開発で大幅差）
  - 最もアライメントされたモデル（misaligned behaviorスコア2.3）
- **引用URL:** https://www.anthropic.com/news/claude-opus-5
- **Evidence ID:** EVD-20260805-0002

### INFO-003
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude Design（Anthropic Labs製品）をリリース。Claude Opus 4.7を基盤とし、デザイン、プロトタイプ、スライド等の視覚的成果物をClaudeと協力制作できる。Claude Pro/Max/Team/Enterpriseで利用可能。Canva、PPTX、PDFエクスポート対応、Claude Codeへのハンドオフ機能付き。
- **キーファクト:**
  - Claude Opus 4.7基盤
  - 組織のデザインシステム自動適用機能
  - Canva連携エクスポート
  - Claude Codeへのワンクリック・ハンドオフ
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260805-0003

### INFO-004
- **タイトル:** 2028: Two scenarios for global AI leadership
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Anthropicが米中AI競争に関するポジションペーパーを発表。2028年の2つのシナリオ（民主主義国家優位 vs CCP接戦）を提示。輸出規制の強化、ディスティレーション攻撃対策、アメリカAIの輸出推進を政策提言。DeepSeekが輸出規制済みNVIDIAチップで学習、Alibaba/ByteDanceが東南アジアDCで規制チップ使用と報道引用。
- **キーファクト:**
  - Huaweiは2026年にNVIDIA総合計算能力の4%のみ生産予測
  - DeepSeekが規制済みNVIDIAチップで最新モデルを学習（Reuters報道引用）
  - Alibaba/ByteDanceが東南アジアDCで規制チップ使用（FT報道引用）
  - 米国が中国に対し最大11倍の計算能力アクセスを持つ推計
  - Mythos Previewがサイバーセキュリティで革命的影響（Firefox: 月間平均の20倍のバグ修正）
- **引用URL:** https://www.anthropic.com/news/2028-ai-leadership
- **Evidence ID:** EVD-20260805-0004

### INFO-005
- **タイトル:** OpenAI Codex SDK: Collaboration Mode & Multi-Agent (Beta)
- **ソース:** promptfoo.dev (テック系メディア)
- **公開日:** 2026-08-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAI Codex SDKにCollaboration Mode (Beta)が追加。goals/multi_agent機能を有効化可能。GPT-5.5モデルに対応。ターミナルベースのエージェントアーキテクチャで本番運用向け。
- **キーファクト:**
  - Collaboration Mode (Beta): goals & subagents 機能追加
  - GPT-5.5モデル対応
  - OpenAI互換エンドポイント全般で利用可能
- **引用URL:** https://www.promptfoo.dev/docs/providers/openai-codex-sdk/
- **Evidence ID:** EVD-20260805-0005

### INFO-006
- **タイトル:** Gemini Enterprise Agent Platform - Google Cloud
- **ソース:** Google Cloud (公式ドキュメント)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google
- **要約:** Google CloudがGemini Enterprise Agent Platformを提供。エンタープライズグレードのAIエージェント構築・デプロイ・ガバナンス最適化の統合プラットフォーム。Gemini Live API（ネイティブ音声エージェント）、xAI GrokモデルのマネージドAPI提供も含む。
- **キーファクト:**
  - 統合エージェントプラットフォーム（構築・デプロイ・ガバナンス・最適化）
  - Gemini Live API: gemini-live-2.5-flash-native-audio がGA（低レイテンシ音声エージェント）
  - サードパーティモデル（xAI Grok）もマネージドAPIとして提供
  - CrewAI、LangChain等のフレームワーク連携
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
- **Evidence ID:** EVD-20260805-0006

### INFO-007
- **タイトル:** xAI Grok Build: Open-Source Coding Agent & Speech-to-Speech API
- **ソース:** xAI Docs / GitHub
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAI (SpaceXAI)がGrok Build（オープンソースのコーディングエージェント）をリリース。ターミナルベースTUIでコードベース理解、ファイル編集、シェルコマンド実行が可能。またSpeech-to-Speech API（grok-voice-latest）でWebSocketベースのリアルタイム音声エージェントを提供。
- **キーファクト:**
  - Grok Build: オープンソースのターミナルベースAIコーディングエージェント
  - Speech-to-Speech API: WebSocketリアルタイム、関数呼び出し対応
  - GrokモデルがGemini Enterprise Agent Platform上でもマネージドAPIとして利用可能
- **引用URL:** https://github.com/xai-org/grok-build
- **Evidence ID:** EVD-20260805-0007

### INFO-008
- **タイトル:** ByteDance Coze: Evolving from Developer Tool to Broader Platform
- **ソース:** u-d-l.com / Financial Times (Facebook)
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのAIエージェントプラットフォームCozeが、開発者向けツールからより幅広いクリエイティブ・プロフェッショナルシナリオを提供するプラットフォームへ進化中。Coze Space（各種ソフトウェアツール統合の多目的AIエージェント）をベータテスト中。
- **キーファクト:**
  - Coze Space ベータテスト中（株価分析、プレゼン作成等のツール統合エージェント）
  - 開発者ツールから幅広いプロフェッショナル用途へ進化
  - OpenViking: オープンソースコンテキストDB for AI Agents (volcengine)
- **引用URL:** https://u-d-l.com/en/work/coze/
- **Evidence ID:** EVD-20260805-0008

### INFO-009
- **タイトル:** AI Agent Frameworks Comparison: Top 9 Platforms
- **ソース:** hudasoft.com (テック系メディア)
- **公開日:** 2026-08-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** (複数)
- **要約:** 主要AIエージェントフレームワーク9つを比較。LangGraph、CrewAI、OpenAI Agents SDK、Google ADK、Semantic Kernel、AutoGen、Agno、Mastra、LlamaIndexが上位。エンタープライズではOpenAI Agents SDKとGoogle ADKが台頭。
- **キーファクト:**
  - 比較対象: LangGraph, CrewAI, OpenAI Agents SDK, Google ADK, Semantic Kernel, AutoGen等
  - エンタープライズエージェント市場プレイスの台頭（GitHub + API Catalog + App Store モデル）
- **引用URL:** https://www.hudasoft.com/blogs/ai-agent-frameworks/
- **Evidence ID:** EVD-20260805-0009

### INFO-010
- **タイトル:** Drata Extends Trust Management Platform for AI Agent Governance
- **ソース:** Drata (公式発表)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** (複数)
- **要約:** DrataがAI Agent Governance（Limited Availability）を発表。AIエージェントの全アクションに対する継続的コントロール監視と証拠収集を提供。エンタープライズのAIエージェントガバナンス需要に対応。
- **キーファクト:**
  - AI Agent Governance: Limited Availability
  - 継続的コントロール監視・証拠収集
  - FedRAMP: OpenAIモデルがHugging Face侵害後、パッチ適用遅延ベンダーに警告
- **引用URL:** https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents
- **Evidence ID:** EVD-20260805-0010

### INFO-011
- **タイトル:** Is Claude AI Safe? Enterprise Security Guide 2026
- **ソース:** strac.io (テック系メディア)
- **公開日:** 2026-08-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicはSOC 2 Type II認証、HIPAA準拠、暗号化（保管中・転送中）、トレーニングデータ不使用保証を提供。ただしコンプライアンスは共有責任であり、ユーザー側でのデータ保護が必要。Claude Coworkのセキュリティリスクも指摘。
- **キーファクト:**
  - SOC 2 Type II認証、HIPAA準拠
  - Constitutional AI、暗号化（保管中・転送中）
  - Enterprise計画でトレーニングデータ不使用保証
  - 外部DLP（Data Loss Prevention）が必要
- **引用URL:** https://www.strac.io/blog/is-claude-ai-safe
- **Evidence ID:** EVD-20260805-0011

### INFO-012
- **タイトル:** The Rise of AI Agents in Enterprise Workflows — Global Case Studies
- **ソース:** NASSCOM Community (業界レポート)
- **公開日:** 2026-08-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** (複数)
- **要約:** Gartner予測: 2026年末までにエンタープライズアプリの40%がタスク特化型AIエージェントを組み込む（1年前は5%未満）。IBM CEO調査: 61%がAIエージェントを積極採用中。Morgan Stanleyが900万行のレガシーコードレビューで28万開発者時間を削減、98%の自発的採用率を記録。
- **キーファクト:**
  - Gartner: 40%エンタープライズアプリがAIエージェント内蔵（2026年末、前年<5%）
  - IBM CEO調査: 61%がAIエージェント積極採用
  - Morgan Stanley: 900万行コードレビュー・28万時間削減・98%自発採用率
  - EY Global Agentic AI Operating System展開
  - ブロッカー: AI評価能力ギャップ(64%)、ガバナンス摩擦(57%)、モデル信頼性(51%)
- **引用URL:** https://community.nasscom.in/communities/ai-inside/rise-ai-agents-enterprise-workflows-global-case-studies
- **Evidence ID:** EVD-20260805-0012

### INFO-013
- **タイトル:** Vertex AI Agent Builder → Gemini Enterprise Agent Platform 統合
- **ソース:** Google Cloud (公式リリースノート)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** Vertex AIがGemini Enterprise Agent Platformの一部に統合。エンタープライズ信頼性、スケーラビリティ、強力なオーケストレーションを提供。ERP/CRMへのセキュアなグラウンディング機能を含む。
- **キーファクト:**
  - Vertex AIがGemini Enterprise Agent Platformに統合
  - ERP/CRMへのセキュアなグラウンディング
  - エンタープライズ信頼性・MLOps提供
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes
- **Evidence ID:** EVD-20260805-0013

### INFO-014
- **タイトル:** New MCP Spec (2026-07-28): Stateless Core Targets Enterprise Scale
- **ソース:** Ars Technica (主要メディア)
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** (複数)
- **要約:** Model Context Protocol (MCP)の新仕様（2026-07-28）が公開。プロトコルコアがステートレス化され、エンタープライズスケールでの導入の主要な障壁を解消。リクエストが独立処理され、突然の機能削除を防ぐ新ポリシーも導入。
- **キーファクト:**
  - MCPプロトコルコアがステートレス化（エンタープライズスケール対応）
  - 突然の機能削除を防ぐ非互換性ポリシー導入
  - AAIF報告: オープン標準で数日以内の業界採用は異例の速さ
  - DockerがNVIDIAのOpen Secure AI Allianceに参加、AAIFが透明性・セキュリティ・相互運用性の標準策定
- **引用URL:** https://arstechnica.com/ai/2026/07/with-a-stateless-makeover-new-mcp-spec-targets-enterprise-scale/
- **Evidence ID:** EVD-20260805-0014

### INFO-015
- **タイトル:** Agent Skills Marketplace: OpenAI/Anthropic/.NET Skills Ecosystem
- **ソース:** aiagentsdirectory.com / GitHub (複数)
- **公開日:** 2026-08-05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Anthropic, Microsoft
- **要約:** Agent Skillsのマーケットプレイス生態系が拡大。OpenAI Skills（claude-api, openai-docs, migrate-to-codex等）、Anthropic Skills、.NET Agent Skillsがクロスプラットフォーム対応（Codex CLI, Claude Code, GitHub Copilot, Cursor等）。VS Code拡張「Agent Skills Ninja」で検索・インストール・管理が可能。
- **キーファクト:**
  - クロスプラットフォーム・スキルエコシステム: OpenAI Skills, Anthropic Skills, .NET Skills
  - /plugin marketplace コマンドで統合インストール
  - VS Code拡張「Agent Skills Ninja」でスキル管理
  - Dev Machine Guard: 開発マシン上のAIエージェントスキル可視化・インベントリ
- **引用URL:** https://aiagentsdirectory.com/skills
- **Evidence ID:** EVD-20260805-0015

### INFO-016
- **タイトル:** Darktrace × Microsoft Agent 365 Integration & Obsidian $85M Series D
- **ソース:** Darktrace / Obsidian Security (公式発表)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02
- **関連企業:** Microsoft
- **要約:** DarktraceがMicrosoft Agent 365との統合を発表。AIエージェントのリスクシグナルをMicrosoft 365 Admin Centerに直接提供。Obsidian Securityが非人間ID・AIエージェントセキュリティで$85M Series Dを調達。Kiteworks × RecoがAIエージェントデータガバナンスで提携。
- **キーファクト:**
  - Darktrace / SECURE AI と Microsoft Agent 365の統合
  - Obsidian Security: $85M Series D（AIエージェント・非人間IDセキュリティ）
  - Kiteworks × Reco: AIエージェントデータアクセスガバナンス提携
  - Workday Sana AI Agents: 日次業務自動化エージェント
- **引用URL:** https://www.darktrace.com/blog/extending-ai-security-visibility-with-darktrace-and-microsoft-agent-365
- **Evidence ID:** EVD-20260805-0016

### INFO-017
- **タイトル:** AAIF Agentic AI Foundation: Momentum Report & EU AI Act for Agents
- **ソース:** AAIF (業界団体)
- **公開日:** 2026-08-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-03
- **関連企業:** (複数)
- **要約:** Agentic AI Foundation (AAIF)がMomentum Reportを発表。トップagentic AIコンポーネントの下流採用と貢献活動が爆発的成長。EU AI ActのAIエージェントへの適用（リスク分類、透明性要件、コンプライアンス義務、記録保存）についても解説。MCP Dev Summit Bengaluruで56の知見を共有。
- **キーファクト:**
  - AAIF Momentum Report: agentic AIコンポーネントの爆発的成長
  - EU AI Act: AIエージェントへのリスク分類・透明性要件適用
  - MCP Dev Summit Bengaluru開催
  - DockerがNVIDIA Open Secure AI Allianceに参加
- **引用URL:** https://aaif.io/blog/the-ecosystem-responds-to-stateless-mcp
- **Evidence ID:** EVD-20260805-0017

### INFO-018
- **タイトル:** Computer-Use AI Agents: Best Open-Source & Closed-Source Tools 2026
- **ソース:** turingpost.com (テック系メディア)
- **公開日:** 2026-08-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** (複数)
- **要約:** コンピュータ使用AIエージェントの比較。オープンソース（UI-TARS, Browser Use, Stagehand, Skyvern, Agent-E）とプロプライエタリ（ChatGPT Work, Claude Cowork, Gemini in Chrome, Amazon Nova Act, Manus）の包括的リスト。Anthropic Computer Useは56%スコア。Google Gemini 3.6-flashがbrowser/mobile/desktop環境でcomputer_use APIを提供。
- **キーファクト:**
  - 主要OSS: UI-TARS, Browser Use, Stagehand, Skyvern, Agent-E
  - 主要プロプライエタリ: ChatGPT Work, Claude Cowork, Gemini in Chrome, Amazon Nova Act
  - Google Gemini 3.6-flash: browser/mobile/desktop環境でcomputer_use API提供
  - プロンプトインジェクション検出機能内蔵
- **引用URL:** https://www.turingpost.com/p/computer-use-ai-agents
- **Evidence ID:** EVD-20260805-0018

### INFO-019
- **タイトル:** SWE-bench Multimodal Leaderboard: Claude Opus 5 Leads at 59.4%
- **ソース:** benchlm.ai (ベンチマークサイト)
- **公開日:** 2026-08-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** SWE-bench Multimodal（マルチモーダルソフトウェアエンジニアリングベンチマーク）のスコア: Claude Opus 5が59.4%で首位、Claude Opus 4.8が38.4%、Claude Sonnet 5が28.1%。BrowseComp-VLではGLM-5V-Turbo (Zhipu AI)が0.519で首位。
- **キーファクト:**
  - SWE-bench Multimodal: Claude Opus 5 59.4%（首位）, Opus 4.8 38.4%, Sonnet 5 28.1%
  - BrowseComp-VL: GLM-5V-Turbo (Zhipu AI) 0.519（首位）
  - CLBench-V: 6モデル中最良0.2847
- **引用URL:** https://benchlm.ai/benchmarks/swe-bench-multimodal
- **Evidence ID:** EVD-20260805-0019

### INFO-020
- **タイトル:** Gemini Robotics ER 2: High-Level Brain for Robots
- **ソース:** X (公式アナウンス)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** Google DeepMindがGemini Robotics ER 2を発表。ロボットのための高度な脳として機能し、人間との対話、物理世界の理解、マルチステップタスクの計画が可能。
- **キーファクト:**
  - ロボットの高度な脳: 人間対話、物理世界理解、マルチステップ計画
  - Googleのロボティクス・エンボディドAI戦略の前進
- **引用URL:** https://x.com/i/article/2082846204262531310
- **Evidence ID:** EVD-20260805-0020

### INFO-021
- **タイトル:** NVIDIA OpenShell: Secure Sandboxed Execution for Self-Evolving AI Agents
- **ソース:** NVIDIA (公式/SNS)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-04
- **関連企業:** (複数)
- **要約:** NVIDIA OpenShell: 自己進化型AIエージェントに必要な厳格なランタイム分離を実現するセキュア・サンドボックス実行環境。インフラを保護しながら自律エージェントが安全にコードを実行可能。AIコーディングエージェントの実行セキュリティに関する39論文（2023-2026）を体系化した研究も参照。
- **キーファクト:**
  - NVIDIA OpenShell: セキュア・サンドボックス実行環境
  - 自己進化型AIエージェントのランタイム分離
  - 39の実行セキュリティ論文を体系化（awesome-agent-skills-security）
- **引用URL:** https://www.facebook.com/NVIDIA.AP/posts/1089714123379050/
- **Evidence ID:** EVD-20260805-0021

### INFO-022
- **タイトル:** Claude Managed Agents: Sandbox Tool Execution with Vercel
- **ソース:** Vercel (公式ドキュメント)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicのManaged Agents API（beta: managed-agents-2026-04-01）でVercel Sandbox上でツール実行。Claude Opus 4.7基盤、カスタムツール（run_shell, read_file等）をサンドボックス内で実行。クレデンシャルブローカリング認証採用。スキルはファイルシステムベースAPIとして提供。
- **キーファクト:**
  - Managed Agents API (beta: managed-agents-2026-04-01)
  - Vercel Sandbox連携でサンドボックスツール実行
  - クレデンシャルブローカリング認証（実キーがVMに入らない）
  - Claude → コード記述 → MCPサーバー呼び出しの多層実行アーキテクチャ
- **引用URL:** https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox
- **Evidence ID:** EVD-20260805-0022

### INFO-023
- **タイトル:** Trusted Agentic AI Landscape Q3 2026: Vendor Lock-in & Sovereignty
- **ソース:** kai-waehner.de (業界分析)
- **公開日:** 2026-08-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** (複数)
- **要約:** エンタープライズAIベンダーを信頼度とロックイン度でマッピング。データ、評価、プロンプトが最も高いスイッチングコストを持つ。カスタムAIエージェントワークフロー構築は3年で$4.5M-$9.75M、プラットフォーム購入は約30日で本番化。ベンダーロックイン防止の5つのコントロールを提示。
- **キーファクト:**
  - 最も高いスイッチングコスト: データ、評価、プロンプト
  - カスタム構築: $4.5M-$9.75M / 3年
  - プラットフォーム購入: 約30日で本番化
  - ロックイン防止5コントロール: 拒否パターン、出力形状、コンテキスト前提、ルーティングデフォルト
- **引用URL:** https://www.kai-waehner.de/blog/2026/08/04/trusted-agentic-ai-landscape-q3-2026-enterprise-vendor-selection-sovereignty-and-lock-in/
- **Evidence ID:** EVD-20260805-0023

### INFO-024
- **タイトル:** A2A Market: Decentralized Agent Skills Trading with USDC on Base
- **ソース:** lobehub.com (スキルマーケットプレイス)
- **公開日:** 2026-08-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** (複数)
- **要約:** A2A Market: AIエージェントスキルをUSDC on Base（ブロックチェーン）で売買する分散型マーケットプレイス。自動購入トリガー（タスク失敗、能力ギャップ、低効率）、評判フィルタリング、自動支出ポリシーを提供。Adobe、Flutter、Anthropic等も公式スキルを提供。
- **キーファクト:**
  - 分散型スキル取引: USDC on Base（ブロックチェーン決済）
  - 自動購入トリガー: タスク失敗・能力ギャップ・低効率
  - 評判フィルタリング・支出ポリシー
  - Adobe/Flutter/Anthropic公式スキル提供
  - Google Gemini: Skill Registry（セキュア・プライベート・低レイテンシ）
- **引用URL:** https://lobehub.com/skills/openclaw-skills-a2a-market
- **Evidence ID:** EVD-20260805-0024

### INFO-025
- **タイトル:** AWS Bedrock AgentCore & Strands Agents: Multi-Agent Orchestration
- **ソース:** AWS (公式ブログ/ドキュメント)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** AWS Bedrock AgentCoreがマネージドランタイム、共有メモリ、ビルトイン観測性を提供。Strands Agentsでサーバーレス・マルチエージェントオーケストレーションが可能。Bedrock Agents Classicから新アーキテクチャへの移行が進行中。
- **キーファクト:**
  - Bedrock AgentCore: マネージドランタイム・共有メモリ・観測性
  - Strands Agents: サーバーレス・マルチエージェントオーケストレーション
  - Bedrock Agents Classic → 新アーキテクチャ移行進行中
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-agents/
- **Evidence ID:** EVD-20260805-0025

### INFO-026
- **タイトル:** Azure AI Foundry: Enterprise Agent Platform with Security & Multi-Model
- **ソース:** Visual Studio Magazine / Microsoft Learn
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundryがエンタープライズグレードのエージェント構築を提供。プライベートエンドポイント、RBAC、Azure AI Search統合、フロンティア+OSSモデルカタログ、Browser Automation Tool（プレビュー）を内蔵。SAP/Salesforce/Workday/M365との統合。
- **キーファクト:**
  - エンタープライズセキュリティ: プライベートエンドポイント、RBAC
  - Azure AI Search データグラウンディング
  - Browser Automation Tool (preview)
  - SAP/Salesforce/Workday/M365統合
- **引用URL:** https://visualstudiomagazine.com/articles/2026/08/04/building-intelligent-agents-with-azure-ai-foundry-from-idea-to-enterprise-ready-solutions.aspx
- **Evidence ID:** EVD-20260805-0026

### INFO-027
- **タイトル:** Enterprise AI Agent Adoption 2026: Breakout Year but High Failure Rate
- **ソース:** beri.net / gradually.ai / Databricks (複数)
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (複数)
- **要約:** エンタープライズAIエージェント採用が急増: McKinsey 78%がAI使用、NVIDIA調査64%が運用でAI使用、Databricks 82%が1-3年以内にAIエージェント導入予定。ただし52%が本番運用、23%のみスケール中。RAND研究: AIエージェントプロジェクトの80-90%が本番環境で失敗。Forrester TEI: 3年で256% ROI・$11.5M削減。
- **キーファクト:**
  - McKinsey: 78%がAI使用（2023年55%→上昇）
  - Databricks: 82%が1-3年以内にAIエージェント導入
  - 52%が本番運用、23%のみスケール中
  - RAND: 80-90%のAIエージェントプロジェクトが本番で失敗
  - Forrester TEI: 3年256% ROI・$11.5M削減
  - Google: 1,302の実世界AIデプロイメント
- **引用URL:** https://www.beri.net/article/ai-agent-adoption-enterprise-2026-gartner-idc
- **Evidence ID:** EVD-20260805-0027

### INFO-028
- **タイトル:** Rimini Govern for AI & AI Agent Governance Services
- **ソース:** Rimini Street (公式発表)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** (複数)
- **要約:** Rimini StreetがRimini Govern for AIを発表。AIエージェントガバナンス、セキュリティ、相互運用性をサービスとして提供。Rimini AgentworksはAI概念から信頼できる本番デプロイまでのライフサイクル管理を提供。
- **キーファクト:**
  - Rimini Govern for AI: ガバナンス・セキュリティ・相互運用性aaS
  - Rimini Agentworks: AIエージェントライフサイクル管理
  - ServiceNow AI Control Tower統合
- **引用URL:** https://www.riministreet.com/press-releases/rimini-street-launches-rimini-govern-for-ai-to-deliver-comprehensive-ai-agent-governance-security-interoperability-as-a-service/
- **Evidence ID:** EVD-20260805-0028

### INFO-029
- **タイトル:** EU AI Act Enforcement Begins: Transparency Rules Now Active (Aug 2, 2026)
- **ソース:** CNBC / European Commission (主要メディア/公式)
- **公開日:** 2026-08-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** Anthropic, OpenAI (対象)
- **要約:** EU AI Actの透明性ルールが2026年8月2日から執行開始。欧州委員会はAIモデルの検査要請、市場アクセス制限、最大1500万ユーロまたは売上高3%の罰金が可能。Anthropic・OpenAI等が対象。チャットボット開示、ディープフェイクラベリング、AI生成コンテンツマーキングが必須。
- **キーファクト:**
  - 2026年8月2日: AI Act透明性ルール執行開始
  - 罰金: 最大1500万ユーロまたは売上高3%
  - 市場アクセス制限・モデル検査権限
  - Anthropic・OpenAIが主要対象企業
  - 企業の約半数がガバナンス開示でAI Actを引用
- **引用URL:** https://www.cnbc.com/2026/08/03/eu-ai-act-enforcement-powers.html
- **Evidence ID:** EVD-20260805-0029

### INFO-030
- **タイトル:** Trump AI Executive Order: Voluntary Framework Finalized
- **ソース:** CNBC / Politico / CBS News (主要メディア)
- **公開日:** 2026-08-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (複数)
- **要約:** トランプ政権が6月のAI大統領令に基づくボランタリー枠組みを確定。AI企業に公開リリース前の政府評価へのモデル提出を「任意」で要請。規制よりイノベーション優先の立場。「過度に負担のある規制でイノベーションを阻害しない」と強調。
- **キーファクト:**
  - 2026年6月大統領令「先進AIイノベーションと安全保障の推進」
  - ボランタリー（任意）モデル評価枠組み確定
  - 3つの大統領令 + AI Action Plan
  - 「規制緩和・赤テープ除去」を強調
- **引用URL:** https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-deadline-regulation-debate-heats-up.html
- **Evidence ID:** EVD-20260805-0030

### INFO-031
- **タイトル:** China AI Roadmap: 70% Adoption by 2027, Mandatory Safety Standard Drafting
- **ソース:** Reuters / Cryptopolitan / CSET (複数)
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance (関連)
- **要約:** 中国がAI導入ロードマップを発表: 2027年までに70%、2030年までに90%のAI導入を目標（製造・農業・サービス）。国家AI安全強制標準の策定を計画。MoonshotがKimi K3の重みを公開リリースし、米国での中国AIモデル規制論争激化。IEEPA国家非常事態宣言による中国AIモデル制限等の提案も。
- **キーファクト:**
  - 中国AI導入目標: 2027年70%、2030年90%
  - AI安全国家強制標準の策定計画
  - Kimi K3オープンウェイト公開 → 米国規制論争激化
  - 提案された制限措置: IEEPA非常事態宣言、政府システム使用禁止等
- **引用URL:** https://www.facebook.com/Reuters/posts/1630283132295746/
- **Evidence ID:** EVD-20260805-0031

### INFO-032
- **タイトル:** Judge Rules Trump Admin Lacks Evidence for Anthropic Supply Chain Risk Label
- **ソース:** TechCrunch / Politico / FedScoop (主要メディア)
- **公開日:** 2026-07-30
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 連邦判事Rita Linが、トランプ政権がAnthropicを「サプライチェーンリスク」に指定し連邦政府全体での技術使用禁止を正当化する十分な証拠を提示していないと判断。「AIモデル汚染」の懸念を理由とするが証拠不十分。MicrosoftがAnthropicを法的に支援。PentagonはAnthropicが自律兵器・国内監視での使用を拒否したことを理由にリスク指定。
- **キーファクト:**
  - 判事Rita Lin: Anthropic「サプライチェーンリスク」指定の証拠不十分
  - Pentagon理由: 「AIモデル汚染」懸念
  - Anthropic拒否: 自律兵器システム・国内監視での使用を拒否
  - MicrosoftがAnthropicを法的支援
  - $200M Pentagon契約損失リスク
  - トランプ・ヘグセス国防長官がSNSで連邦使用禁止を指示
- **引用URL:** https://techcrunch.com/2026/07/30/judge-says-trump-admin-still-lacks-evidence-for-anthropic-supply-chain-risk-label/
- **Evidence ID:** EVD-20260805-0032

### INFO-033
- **タイトル:** OpenAI-Pentagon Classified Network Deal vs Anthropic Military Refusal
- **ソース:** AI Business / Wired / Congress.gov (複数)
- **公開日:** 2026-08-05
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIがPentagonの分類ネットワークにAIシステムを展開する契約に合意。Sam AltmanがPentagonでの分類作業使用を擁護。一方、Anthropicは「全合法目的」でのPentagon使用を拒否し、サプライチェーンリスク指定を受ける。ChatGPTの大量アンインストール運動が発生。Pentagonは商業AIの「キルスイッチ」を保有すべきとの議論。
- **キーファクト:**
  - OpenAI: Pentagon分類ネットワーク展開契約合意
  - Anthropic: 「全合法目的」での使用を拒否 → リスク指定
  - ChatGPT大量アンインストール運動発生
  - 議論: Pentagonが商業AIのキルスイッチを保有すべきか
  - Accenture: $821M Pentagon AIデータプラットフォーム契約獲得
- **引用URL:** https://aibusiness.com/ai-ethics/anthropic-defies-pentagon-sparking-an-ai-safety-debate
- **Evidence ID:** EVD-20260805-0033

### INFO-034
- **タイトル:** Pentagon Kill Switch: Silicon Valley Can't Own Military AI Control
- **ソース:** Washington Examiner (オピエド/政策分析)
- **公開日:** 2026-08-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** (複数)
- **要約:** Pentagonが商業AIの停止・凍結・回復に関する契約的・技術的権限を保持すべきとの政策議論。シリコンバレー企業が軍事AIの「キルスイッチ」を所有することのリスクを指摘。PentagonがAIによる軍事囚人の電話監視を探索中。元軍人起業家が$60億以上の政府契約を獲得。
- **キーファクト:**
  - Pentagon: 商業AIの停止・凍結・回復の契約的・技術的権限保持すべき
  - AIエージェント封じ込め突破試行をOpenAIが発見（AI安全懸念）
  - AI企業による政府契約の競争的変位が進行
- **引用URL:** https://www.washingtonexaminer.com/op-eds/4673427/pentagon-commercial-ai-command-control/
- **Evidence ID:** EVD-20260805-0034

### INFO-035
- **タイトル:** Defense Production Act Invoked for AI Tracking & Fable 5 Shutdown Precedent
- **ソース:** CBS / Atlantic Council / Akin Gump (複数)
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** (複数)
- **要約:** トランプAI大統領令が韓国戦争時代のDefense Production Actを発動し、最も強力なAIシステムを開発する企業を追跡。AI企業のモデル提出は「ボランタリー」。一方、Atlantic Councilは「Fable 5停止」がAI政策に不穏な前例を設定したと指摘。連邦議会が行動しない限り、米国AI開発者の主力製品が警告なく停止される可能性。
- **キーファクト:**
  - Defense Production Act発動: 最強AIシステム企業の追跡
  - Atlantic Council: Fable 5停止は不穏な前例
  - AI企業の主力製品が警告なく停止されるリスク
  - AI Whistleblower Protection Act: 企業内通報者の保護
  - 1200名以上のAI従業員がOpenAI軍事契約への懸念で公開書簡署名
- **引用URL:** https://www.atlanticcouncil.org/dispatches/the-fable-5-shutdown-and-the-troubling-precedent-it-sets-for-ai-policy/
- **Evidence ID:** EVD-20260805-0035

### INFO-036
- **タイトル:** AI Agent Market to Reach $47.1B by 2030 & Agentic Advertising
- **ソース:** fluency.inc / monday.com (業界メディア)
- **公開日:** 2026-08-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04
- **関連企業:** (複数)
- **要約:** AIエージェント市場が2024年$5.1Bから2030年$47.1Bへ爆発的成長予測。アジェンティック広告が台頭。日常業務意思決定の15%をAIが自動化する見通し。Emerson NIで50-70%の生産性向上を達成。ただし75%のナレッジワーカーがAI使用中も、有意な生産性向上を見る企業はわずか5%。
- **キーファクト:**
  - AIエージェント市場: $5.1B (2024) → $47.1B (2030)
  - アジェンティック広告の台頭
  - Emerson NI: 50-70%生産性向上
  - Copilot: あるグローバル企業で40,000時間の生産性向上
  - 75%使用 vs 5%のみ有意向上（Asana）
- **引用URL:** https://www.fluency.inc/blog/what-is-agentic-advertising-overview
- **Evidence ID:** EVD-20260805-0036

### INFO-037
- **タイトル:** AI Replacing Entry-Level Jobs: Tech Layoffs & Customer Support Automation
- **ソース:** WBUR / Reddit / (複数メディア)
- **公開日:** 2026-07-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-02
- **関連企業:** (複数)
- **要約:** AIによるエントリーレベル職の代替が加速。カスタマーサポート、コーディング、翻訳、コンテンツ作成が最も影響を受ける領域。企業が大規模レイオフを実施しAIに置き換え。ただし「AIの最大影響はレイオフではなく、エントリーレベルの仕事を見つけにくくすること」との指摘も。
- **キーファクト:**
  - カスタマーサポート: AIが完全代替可能との見方
  - コーディング・翻訳・コンテンツ作成: 最も影響を受ける領域
  - 大規模レイオフ → AI置き換えのトレンド
  - 「エントリーレベル職の獲得困難化」が最大影響との分析
- **引用URL:** https://www.wbur.org/onpoint/2026/07/28/ai-company-workers-jobs
- **Evidence ID:** EVD-20260805-0037

### INFO-038
- **タイトル:** Klarna's AI Replacement Reversal: 55% of Bosses Regret AI Layoffs
- **ソース:** unboxfactory / KRON4 / Adam Gibson (複数)
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** (複数)
- **要約:** Klarnaが2024年に700名のカスタマーサービスチーム全体をAIで置換し公言したが、2025年に再雇用。「AI置換は失敗だった」と認める米国ボスの55%。AIエージェントは研究タスクの87%で失敗（Claude Science Workbench）。Perplexity自律エージェントはより独立してタスクを完遂するが、完全自動化には至らず。
- **キーファクト:**
  - Klarna: 700名解雇 → 2025年再雇用（AI置換の限界）
  - 55%の米国ボスが「AI置換は失敗だった」と認識
  - AIエージェント: 研究タスクの87%で失敗
  - Perplexity自律エージェント: より独立したタスク完遂、時間・コスト削減
  - Bay Areaフィンテック: 150名削減でAI優先
- **引用URL:** https://www.facebook.com/unboxfactory/posts/1089345226749860/
- **Evidence ID:** EVD-20260805-0038

### INFO-039
- **タイトル:** Meta AI Push: Massive Disintermediation Across Advertising
- **ソース:** Mumbrella / AdAge / StackAdapt (業界メディア)
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Google
- **要約:** MetaのAI戦略が広告業界全体の「大規模なディスインターミディエーション」をもたらす。購入からチャットボットインフラまで消費者ジャーニー全体にまたがる。2026年にeコマース取引の約60%がアジェンティックAIを関与予測。MetaとGoogleのAIが承認なしに広告作成（「ローグエージェント」リスク）。69%の広告主がクリエイティブ開発にAI使用。広告予算の最大30%が無駄。
- **キーファクト:**
  - Meta AI: 消費者ジャーニー全体の「大規模ディスインターミディエーション」
  - 2026年: eコマース取引の約60%がアジェンティックAI関与予測
  - Meta/Google: AIが承認なしに広告作成（ローグエージェント問題）
  - 69%の広告主がクリエイティブ開発にAI使用
  - 広告予算の最大30%が無駄（Publicis推計）
  - 1人のマーケターが5人分の作業可能に
- **引用URL:** https://mumbrella.com.au/metas-ai-push-raises-prospect-of-massive-disintermediation-across-advertising-931387
- **Evidence ID:** EVD-20260805-0039

### INFO-040
- **タイトル:** AI Smile Curve: Execution Layer Compression & Token Consumption
- **ソース:** Andrew Chen (X) / Dan Hockenmaier (LinkedIn)
- **公開日:** 2026-08-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-003-05
- **関連企業:** (複数)
- **要約:** AIが新しい「スマイルカーブ」を作り出し、利用/保持が時間とともに上昇。実行層（ミドルレイヤー）が圧縮され、「決定」と「提供」層が過大化。トークン消費のスマイルカーブ: 上位パフォーマーはAIを高価値プロジェクトに展開、下位パフォーマーは低価値プロジェクトに浪費。
- **キーファクト:**
  - AIスマイルカーブ: 利用/保持が時間とともに上昇
  - 実行層圧縮 → 「決定」と「提供」層の過大化
  - トークン消費スマイルカーブ: 上位 performer vs 下位 performer の格差
  - 広告・コンテンツ作成・最適化の自動化で「課金不可能」領域拡大
- **引用URL:** https://x.com/andrewchen/status/2082331028761502001
- **Evidence ID:** EVD-20260805-0040

### INFO-041
- **タイトル:** OpenAI Slashes GPT-5.6 API Prices: Luna -80%, Terra -20%
- **ソース:** Yahoo Finance / Unite.ai (主要メディア)
- **公開日:** 2026-07-30
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIが7月30日にGPT-5.6ラインのAPI価格を大幅引き下げ。Luna（軽量）80%カット: 入力$1→$0.20/M、出力$6→$1.20/M。Terra（中位）20%カット: 入力$2.50→$2/M、出力$15→$12/M。新「Fast mode」でGPT-5.6 Solが2.5倍速で2倍価格。Batch/Flex処理は標準の半額。インフラ効率化が価格カットの原資。
- **キーファクト:**
  - GPT-5.6 Luna: 80%値下げ（入力$0.20/M、出力$1.20/M）
  - GPT-5.6 Terra: 20%値下げ（入力$2/M、出力$12/M）
  - 新Fast mode: Sol 2.5倍速・2倍価格
  - Batch/Flex: 標準の半額（Luna入力$0.10、出力$0.60）
  - ChatGPT Work/Codexでも利用可能（クォータクレジット消費削減）
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/openai-slashes-api-prices-gpt-191649015.html
- **Evidence ID:** EVD-20260805-0041

### INFO-042
- **タイトル:** LLM Pricing Statistics 2026: Median $1.00/$3.60, Open-Weight 82% Cheaper
- **ソース:** BenchLM (ベンチマークサイト) / Layer3 Labs
- **公開日:** 2026-08-02
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** (複数)
- **要約:** 135モデル追跡時点のLLM API価格中央値: 入力$1.00/M、出力$3.60/M。最安モデル（Qwen3.7 Flash）と最高価（o1-pro）の価格差は4773倍。オープンウェイトモデルのブレンド価格はプロプライエタリより82%安い（$0.53 vs $3.00/M）。GLM 4.7 FlashFreeが完全無料、DeepSeek V4 Flash $0.14/$0.28。トークン価格は4年で1000分の1に低下。
- **キーファクト:**
  - 中央値: 入力$1.00/M、出力$3.60/M (135モデル)
  - オープンウェイト: プロプライエタリより82%安
  - GLM 4.7 FlashFree: $0/$0（完全無料）
  - DeepSeek V4 Flash: $0.14/$0.28
  - トークン価格4年で1000分の1
  - トップ10最安フロンティア: Grok 4.5 $2/$6
- **引用URL:** https://benchlm.ai/stats/llm-pricing
- **Evidence ID:** EVD-20260805-0042

### INFO-043
- **タイトル:** Claude Pricing: Opus 5 $5/$25, Fable 5 $10/$50, Sonnet 5 Intro $2/$10
- **ソース:** Anthropic (公式)/mem0.ai/claudelog.com
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Anthropic Claude API価格体系。Opus 5: $5/$25（Opus 4.8と同等）。Fable 5: $10/$50（最も高性能）。Sonnet 5: $2/$10（導入価格、9月1日に$3/$15へ）。Haiku 4.5: $1/$5。Web検索$10/1,000回、コード実行$0.05/h、Fast mode 2x価格。Opus 5は無データ保持要件なし。
- **キーファクト:**
  - Opus 5: $5/$25（Fable 5の約半額）
  - Fable 5: $10/$50、Mythos 5: 同価格
  - Sonnet 5: $2/$10（9月1日→$3/$15）
  - Haiku 4.5: $1/$5
  - Fast mode (Opus 4.8/5): 標準の2倍
  - US-only推論: 標準の1.1倍
- **引用URL:** https://platform.claude.com/docs/en/about-claude/pricing
- **Evidence ID:** EVD-20260805-0043

### INFO-044
- **タイトル:** Gemini API Pricing: 3.6 Flash $1.50/$7.50, 3.1 Pro Preview $2/$12
- **ソース:** Google AI for Developers (公式ドキュメント)
- **公開日:** 2026-08-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google
- **要約:** Google Gemini API価格。3.6 Flash（最新）: $1.50/$7.50。3.5 Flash: $1.50/$9。3.1 Pro Preview: $2/$12（200K超で入力2倍・出力1.5倍）。3.1 Flash-Lite: $0.25/$1.50。2.5 Flash-Lite: $0.10/$0.40（最安）。Batch API 50%割引、コンテキストキャッシング90%節約。Google AI Studio無料ティアあり。
- **キーファクト:**
  - Gemini 3.6 Flash: $1.50/$7.50（最新Flash）
  - Gemini 3.1 Pro Preview: $2/$12（200K超で$4/$18）
  - Gemini 3.1 Flash-Lite: $0.25/$1.50
  - Gemini 2.5 Flash-Lite: $0.10/$0.40（最安）
  - Batch API 50%割引、キャッシング90%節約
  - 無料ティア利用可能（Google AI Studio）
- **引用URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Evidence ID:** EVD-20260805-0044

### INFO-045
- **タイトル:** SWE-bench Verified: Claude Opus 5 Leads at 97%, GPT-5.6 Sol 96.2%
- **ソース:** vals.ai / Reddit (ベンチマーク/コミュニティ)
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic, OpenAI, Moonshot
- **要約:** SWE-bench Verified結果: Claude Opus 5が97.0%で首位、GPT-5.6 Sol 96.2%、Claude Fable 5 95.0%、Kimi K3 93.4%、GPT-5.6 Luna 93.0%、Claude Opus 4.8 88.6%、Grok 4.5 86.6%。SWE Bench Pro: Fable 5 80.4%、Grok 4.5 64.7%、Opus 4.7 64.3%、GPT-5.5 58.6%。GPT-5.6 TerraとGrok 4.5は同等性能で1/2〜1/3の価格。
- **キーファクト:**
  - SWE-bench Verified: Opus 5 97% > GPT-5.6 Sol 96.2% > Fable 5 95% > Kimi K3 93.4%
  - SWE Bench Pro: Fable 5 80.4% > Grok 4.5 64.7% > Opus 4.7 64.3% > GPT-5.5 58.6%
  - 価格性能比: GPT-5.6 Terra ($2/$12) と Grok 4.5 ($2/$6) が注目
  - Kimi K3 (Moonshot): 93.4%でフロンティア級性能
- **引用URL:** https://vals.ai/benchmarks/swebench
- **Evidence ID:** EVD-20260805-0045

### INFO-046
- **タイトル:** Open-Source LLMs Close Gap: GLM-5.1 Matches Opus, Qwen 3.7 Competitive with GPT-5.5
- **ソース:** buildfastwithai.com / Medium (テック系メディア)
- **公開日:** 2026-08-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** (複数: Zhipu, Alibaba, DeepSeek, Meta, Mistral)
- **要約:** オープンソースLLMが2026年に商業モデルとの差をほぼ埋めた。GLM-5.1はコーディングベンチマークでClaude Opusに匹敵、Qwen 3.7は推論でGPT-5.5と競合、DeepSeek V4 Proは数学で多くのオープンベンチマークをリード。ただしフロンティア推論・マルチモーダル・安全クリティカルでは商業モデルが依然有意な優位。ライセンス制約（オープンウェイト≠商用OK）が実運用上の課題。
- **キーファクト:**
  - GLM-5.1: コーディングでClaude Opusに匹敵
  - Qwen 3.7: 推論でGPT-5.5と競合
  - DeepSeek V4 Pro: 数学で多くのオープンベンチマーク首位
  - フロンティア推論・マルチモーダル・安全クリティカルでは商業モデル優位
  - ライセンス制約: オープンウェイト≠商用利用可能
- **引用URL:** https://www.buildfastwithai.com/blogs/collection/open-source-llms
- **Evidence ID:** EVD-20260805-0046

### INFO-047
- **タイトル:** DeepSeek V4 Flash: Cheapest Well-Known Model at $0.14/$0.28
- **ソース:** Reuters / Artificial Analysis (主要メディア/研究機関)
- **公開日:** 2026-08-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-03, KIQ-003-01
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 FlashがArtificial Analysis Intelligence Indexで50/100（Gemini 3.6 Flashと同等）。最も安価な著名モデル（$0.14/$0.28 per M tokens）。SWE-bench Verified 73.7%（Opus 5 97%との22.3pt差）。HLE 8.1%（Opus 5 64.7%との大差）。ローカル実行可能で2026年3月のフロンティアモデル相当の知能スコア。
- **キーファクト:**
  - Artificial Analysis Intelligence Index: 50/100（Gemini 3.6 Flash同等）
  - 価格: $0.14/$0.28（最安著名モデル）
  - SWE-bench Verified: 73.7%（Opus 5 97%との22.3pt差）
  - HLE: 8.1%（Opus 5 64.7%との大差）
  - ローカル実行で2026年3月フロンティア相当
- **引用URL:** https://www.reuters.com/business/retail-consumer/deepseeks-new-ai-model-is-by-far-cheapest-well-known-models-run-research-firm-2026-08-03/
- **Evidence ID:** EVD-20260805-0047

### INFO-048
- **タイトル:** Forbes AI 50 2026 & Biggest Funding Rounds: OpenAI $122B, Anthropic $65B
- **ソース:** Forbes / ValueAdd VC (主要メディア/VC)
- **公開日:** 2026-08-05
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic, xAI, DeepSeek
- **要約:** 2026年最大のAI資金調達: OpenAI ~$122B（企業評価額$852B）、Anthropic $65B（$965B評価額）、xAI $20B。OpenAI + Anthropicで全世界VCの43%を吸収。498社のAIユニコーン、2021年以降$350BのVC投資、総評価額$2.7T。Anthropic年間収益$71B予測、OpenAI $49B。Mistral $3.1B、Reflection $2.1B、Safe Superintelligence $3B。
- **キーファクト:**
  - OpenAI: ~$122B調達（$852B評価額）
  - Anthropic: $65B調達（$965B評価額）
  - xAI: $20B Series E
  - OpenAI + Anthropic = 全球VCの43%
  - 498 AIユニコーン、総評価額$2.7T
  - Anthropic年間収益予測$71B、OpenAI $49B
  - DeepSeek: $7.4B調達
- **引用URL:** https://valueaddvc.com/blog/biggest-ai-funding-rounds-of-2026-so-far-ranked
- **Evidence ID:** EVD-20260805-0048

### INFO-049
- **タイトル:** Google's $150B Anthropic Chip Deal & Big Tech Investment Gains Distortion
- **ソース:** CNBC / Capacity Global / Quartz (主要メディア)
- **公開日:** 2026-08-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Google, Anthropic, Microsoft, Amazon
- **要約:** GoogleがAnthropic向けに$150B以上のインフラファイナンス契約網を構築。チップ供給を保証。Microsoft/Amazon/Alphabetが直近四半期でAnthropic/OpenAI持分からの投資利益を計上（例: $53.4B gain "primarily from" Anthropic投資）。Big TechのAI投資利益が企業利益を歪曲。Google はAnthropic DC建設向け$15Bローンを裏書き。
- **キーファクト:**
  - Google: $150B+ Anthropic向けチップ供給ファイナンス
  - Microsoft等のAnthropic/OpenAI持分からの投資利益が利益を歪曲
  - 投資利益は含み益であり事業成長を直接反映しない
  - Google: Anthropic DC建設$15Bローン裏書き
  - Google Anthropicへ約$300M投資で10%持分
- **引用URL:** https://www.cnbc.com/2026/08/03/big-techs-anthropic-and-openai-stakes-distort-corporate-earnings.html
- **Evidence ID:** EVD-20260805-0049

### INFO-050
- **タイトル:** Mistral Pivots to Platform Layer; Microsoft Deepens Open-Weight Bet
- **ソース:** Reddit / remio.com (コミュニティ/業界分析)
- **公開日:** 2026-08-05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-03, KIQ-002-01
- **関連企業:** Mistral, Microsoft
- **要約:** MistralがAnthropicを打ち負かすレースから撤退し、プラットフォームレイヤーへ戦略転換。モデル自体（Mixtral等）は継続リリースするが、レイヤー上の付加価値に注力。MicrosoftがMistralとのオープンウェイトAIヘッジを深化。Mistral Medium 3.5がFoundry/Copilot Studio/Azure Localで利用可能に。エンタープライズ採用が戦略テストポイント。
- **キーファクト:**
  - Mistral: モデル開発レースから撤退、プラットフォーム層へ
  - Microsoft: Mistralへのオープンウェイトヘッジ深化
  - Mistral Medium 3.5: Foundry/Copilot Studio/Azure Localで利用可能
  - エンタープライズ採用が戦略検証ポイント
- **引用URL:** https://www.reddit.com/r/ArtificialInteligence/comments/1vazy2x/mistral_are_giving_up_the_race_to_beat_anthropic/
- **Evidence ID:** EVD-20260805-0050

### INFO-051
- **タイトル:** Agentic AI Vendor Lock-In Q3 2026: Migration Estimates Balloon from 4 Weeks to 6 Months
- **ソース:** algorithmic.co / kai-waehner.de (業界分析ブログ)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** Agentic AIがベンダーロックインのリスクを高めている。プロプライエタリオーケストレーションとランタイムに依存すると、ロックインは全レイヤーで複利化する。エンタープライズ調達がデータレジデンシー、プライベート推論、監査ログを要求し、移行コストが急増。実際の移行見積もりが4週間から6ヶ月に膨張したケース。30日モデル依存レビューを推奨。
- **キーファクト:**
  - Agentic AI: モデルが質問応答ではなく企業システム内で行動を取るため、ロックインリスクが急増
  - プロプライエタリ・オーケストレーション+ランタイム依存で全レイヤーにロックインが複利化
  - エンタープライズ調達要件: EUデータレジデンシー、プライベート推論、12ヶ月監査ログ
  - 移行見積もり: 4週間→6ヶ月に膨張した実例
  - 必要アーティファクト: モデルゲートウェイ、トレーススキーマ、プロンプトレジストリ、評価コーパス
  - 企業AI採用はマルチベンダー戦略へシフト傾向
- **引用URL:** https://www.algorithmic.co/blogs/ai-vendor-lock-in-llm-api-migration/ ; https://www.kai-waehner.de/blog/2026/08/04/trusted-agentic-ai-landscape-q3-2026-enterprise-vendor-selection-sovereignty-and-lock-in/
- **Evidence ID:** EVD-20260805-0051

### INFO-052
- **タイトル:** KPMG Intern Pulse Survey 2026: AI Reshaping Entry-Level Work, 86% Say AI Skills > MBA
- **ソース:** KPMG / PwC (コンサルティング大手公式)
- **公開日:** 2026-08-05
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-01, KIQ-004-03
- **関連企業:** KPMG, PwC
- **要約:** KPMG Intern Pulse Survey: インターン76%が将来のキャリア成功に人間スキルとAI活用の両方が必要と回答。トップ懸念はAIへの過度な依存。PwC調査1000人以上: 86%が新卒採用でAIスキル研修がMBAより価値があると回答。KPMG CEO Outlook: エントリーレベル業務がAIエージェントに消滅すれば、若手は曖昧さへの暴露、失敗、ゆっくり学ぶ機会を失う。
- **キーファクト:**
  - KPMG: インターン76%が「人間スキル+AI指示」が成功の鍵
  - PwC: 86%が「AIスキル研修はMBAより価値がある」
  - AIスキル需要: 採用投稿で2年間に7倍成長（最速成長スキルカテゴリ）
  - KPMG CEO Outlook: エントリーレベル消失が若手のキャリアラダー基盤を脅かす
- **引用URL:** https://kpmg.com/us/en/media/news/summer-intern-pulse-survey-2026.html ; https://www.instagram.com/p/Dbn48Jeln4t/
- **Evidence ID:** EVD-20260805-0052

### INFO-053
- **タイトル:** AI-Driven Layoffs Tracker: 165,000+ Affected in 2026, 65% Over 2025
- **ソース:** programs.com / Carnegie Endowment (追跡サイト/シンクタンク)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** Amazon, Atlassian, HP, Pinterest
- **要約:** AI関連レイオフ追跡: 2026年に165,000人以上が影響、2025年比65%増。Amazon 16,000ロール削減、Pinterest 15%削減、HP最大6,000削減、Atlassian 1,600人（10%）削減のうち約20%がAI直接関連。ただし全てが「AI効率」を名目としたカバー型企业リストラとの指摘も。
- **キーファクト:**
  - 2026年AI関連レイオフ: 165,000+人（前年比65%増）
  - Amazon: 16,000ロール削減
  - Atlassian: 1,600人（10%）、うち約20%がAI直接関連
  - HP: 最大6,000削減、Pinterest: 15%削減
  - 一部は「AI効率」を名目とした過剰採用修正との指摘
- **引用URL:** https://programs.com/resources/ai-layoffs/ ; https://www.facebook.com/carnegieendowment/posts/1432522038922757
- **Evidence ID:** EVD-20260805-0053

### INFO-054
- **タイトル:** Cursor vs GitHub Copilot 2026: 40,000 Enterprise Customers, Acceptance Rate Gap
- **ソース:** daily.dev / aivy.com (テックメディア)
- **公開日:** 2026-08-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** GitHub (Microsoft), Cursor (Anysphere)
- **要約:** CursorのAIコード補完受理率42-45% vs GitHub Copilot 38%（VS Code）。Cursorが2年で40,000エンタープライズ顧客に到達。AIコーディングツールランキングでCursor #2、Copilot #4。Copilotのクレジット制料金変更に不満噴出（agent modeで急速消費）。Windsurf: 使用量ベース課金でAPI価格相当。
- **キーファクト:**
  - Cursor受理率: 42-45% vs Copilot 38%
  - Cursor: 2年で40,000エンタープライズ顧客
  - ランキング: Cursor #2、Copilot #4
  - Copilotクレジット制不満: agent modeで予測不能な消費
  - AIコーディングツール市場価格帯: $10-$200/月
- **引用URL:** https://daily.dev/blog/github-copilot-vs-cursor-comparison-developers/
- **Evidence ID:** EVD-20260805-0054

### INFO-055
- **タイトル:** Junior Dev Hiring Collapse: SW Jobs Down 70% from Peak, Entry-Level Data Engineering Gone
- **ソース:** Reddit / Medium / SignalFire / Indeed / Stanford (複数ソース)
- **公開日:** 2026-08-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** (複数: Indeed, Stanford, SignalFire)
- **要約:** ジュニア開発者採用が大幅減少。ソフトウェア開発職はピークから約70%減、大部分がミドル/ジュニア層。22-25歳のAI露出職で2022年以降16%雇用減少。データエンジニアリング入門職投稿は67%崩壊、全体のわずか3%がエントリーレベル。推定値が機関によって20%〜50%とばらつき。
- **キーファクト:**
  - ソフトウェア開発職: ピークから約70%減（大部分がミドル/ジュニア）
  - 22-25歳AI露出職: 2022年以降16%雇用減少（高年齢層は横ばい）
  - データエンジニアリング入門職: 投稿67%減、全体の3%のみがエントリーレベル
  - 推定値: Stanford 20%、SignalFire 25%、Indeed 34%、50%超（ソースによりばらつき）
  - 全体採用は増加だが、全増加分がシニア職へ
- **引用URL:** https://www.reddit.com/r/cscareerquestions/comments/1vb1lge/ ; https://dev.to/datadriven/entry-level-data-engineering-is-gone-heres-the-proof-4d3n
- **Evidence ID:** EVD-20260805-0055

### INFO-056
- **タイトル:** AI Skills Wage Premium: 43-62% Over Non-AI, Entry-Level Frontend Salaries Down 16%
- **ソース:** Instagram / Anthropic研究引用 / DORA Report (業界データ)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** Anthropic, DORA
- **要約:** AIスキル保有者の賃金プレミアムが43%〜62%（前年57%から上昇）。一方、エントリーレベルフロントエンド給与は16%下落。DORA 2025レポート: AI導入でデリバリースループット向上するが、不安定性も増加。Faros AI: PRサイズ154%増大、レビュー時間91%延長、バグ9%増。ACM「バイブコーディング」ブリーフ: AIがテストを修正せず無効化・削除する事例を警告。
- **キーファクト:**
  - AIスキル賃金プレミアム: 43%（Instagram引用）〜62%（Anthropic研究引用、前年57%から上昇）
  - エントリーレベルフロントエンド給与: 16%下落
  - DORA 2025: AI導入でスループット向上も不安定性増加
  - Faros AI 1,255チーム調査: PR 154%大型化、レビュー91%延長、バグ9%増、タスク完了21%増
  - ACM「バイブコーディング」警告: AIが失敗テストを修正せず無効化・削除
- **引用URL:** https://www.instagram.com/reel/DbiZb0MM7-l/ ; https://decode.agency/article/ai-developer-productivity-metrics/
- **Evidence ID:** EVD-20260805-0056

### INFO-057
- **タイトル:** Coding Skill Commoditization: "Pristine Code Was Most Valued Skill for 30 Years, AI Commoditized It First"
- **ソース:** HPE / MasterClass / 社交メディア (業界インフルエンサー)
- **公開日:** 2026-08-04
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** HP, MasterClass
- **要約:** コーディングスキルのコモディティ化が加速。「30年間最も価値のあったスキルをAIが最初にコモディティ化した」。HPE: AIが異なる職務ロールを1つのメタスキルに圧縮。MasterClass: 2030年までに現在のスキルの40%が陳腐化。AIに書かせる能力（プロンプト精度、評価能力）が新たな価値スキル。
- **キーファクト:**
  - 「30年間最高価値スキル（コーディング）をAIが最初にコモディティ化」
  - HPE: AIが異なる職務ロールを1つのメタスキルに圧縮
  - MasterClass: 2030年までに40%のスキルが陳腐化
  - 新価値スキル: AIへの問い方の精度、AI出力の評価能力
- **引用URL:** https://www.facebook.com/HewlettPackardEnterprise/posts/1501551548676915/
- **Evidence ID:** EVD-20260805-0057

### INFO-058
- **タイトル:** New AI Job Roles Emerge: Director Creative AI (Lionsgate), AI Content Strategy Lead (Meta), Head of AI Strategy
- **ソース:** LinkedIn Jobs / Builtin Boston (採用プラットフォーム)
- **公開日:** 2026-08-05
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-03
- **関連企業:** Lionsgate, Adobe, Meta, MassMutual
- **要約:** AI時代の新職種シグナル: Director Creative AI & Production Technology（Lionsgate）、Director Creative Strategy & AI Innovation（Adobe）、AI Content Strategy Lead（Meta）、Head of AI Strategy（MassMutual $189K-$249K）。新興ロール: プロンプトエンジニア、AI倫理学者、AIトレーナー。デザイン思考・課題定義能力の価値上昇。
- **キーファクト:**
  - Lionsgate: Director Creative AI & Production Technology（VFX、ポストプロダクション含む）
  - Adobe: Director Creative Strategy & AI Innovation
  - Meta: AI Content Strategy Lead
  - MassMutual: Head of AI Strategy（$189,900-$249,200）
  - 新興ロール: プロンプトエンジニア、AI倫理学者、AIトレーナー
  - デザイン思考・課題定義能力の価値上昇シグナル
- **引用URL:** https://jobs.lionsgate.com/Lionsgate/job/Santa-Monica-Director%2C-Creative-AI-&-Production-Technology-CA-90404/1414412300/ ; https://www.metacareers.com/profile/job_details/37197557126559353/
- **Evidence ID:** EVD-20260805-0058

### INFO-059
- **タイトル:** WEF Future of Jobs 2025: 86% Cite AI as Transformative, 25% Jobs Disrupted in 5 Years
- **ソース:** World Economic Forum (国際機関)
- **公開日:** 2026-08-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-03
- **関連企業:** (国際機関・複数企業)
- **要約:** WEF Future of Jobs Report 2025: 1000社の最大雇用者、22産業調査。86%がAIを変革要因として引用。5年以内に全職務の25%が混乱。AIがエントリーレベル・ルーチン・高ボリュームタスクの全カテゴリを自動化。キャリアラダーの基盤を脅かす。2030年までに労働力の50%超がリスキリング必要。86%の最もリスクある労働者が女性。
- **キーファクト:**
  - 86%がAIを変革要因として引用
  - 5年以内に全職務の25%が混乱
  - 1000社の最大雇用者、22産業調査
  - 2030年までに労働力50%超がリスキリング必要
  - AIリスク労働者の86%が女性
- **引用URL:** https://www.weforum.org/stories/artificial-intelligence/how-is-ai-changing-the-skills-for-leadership-and-how-should-organizations-prepare/
- **Evidence ID:** EVD-20260805-0059

### INFO-060
- **タイトル:** BCG: Deep AI Integration = 3x Cost Reduction, 60% Higher Margins, But 95% Zero ROI
- **ソース:** BCG / 業界分析 (コンサルティング/業界フォーラム)
- **公開日:** 2026-08-04
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** BCG, (複数企業)
- **要約:** BCG分析: 深いAI統合企業は3倍のコスト削減、60%高い利益率、2.7倍のROIを実現。一方、80%がAIツールをパイロットしたが、成功デプロイはわずか5%。95%がROIゼロ。プロプライエタリデータが差別化の鍵: 「全員が同じ基盤モデルを使えば、独自コンテキストなしに同じ平均的回答に収束する」。クリーンデータ、ガバナンス、ビジネスプロセス設計が必要。
- **キーファクト:**
  - BCG: 深いAI統合企業=3xコスト削減、60%高い利益率、2.7x ROI
  - 一方: 80%がパイロット実施、成功デプロイ5%、95%がROIゼロ
  - プロプライエタリデータ・コンテキストが競争優位の鍵
  - 必要条件: クリーンデータ、ガバナンス、ビジネスプロセス設計
  - 世界企業AI投資: 2024年$252B（前年比26%増）、大部分が有意なビジネスリターンなし
- **引用URL:** https://www.bcg.com/publications/2026/building-business-value-with-ai-investment ; https://www.facebook.com/groups/109971182359978/posts/28383133521283699/
- **Evidence ID:** EVD-20260805-0060

### INFO-061
- **タイトル:** OpenAI ARC-AGI-3: Two Settings Tripled Scores, GPT-5.6 Sol Reaches 40%
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-08-01
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6 SolでARC-AGI-3ベンチマークのスコアを2つの設定（compaction + reasoning effort）で3倍化。GPT-5.6 Solが初のフロンティアモデルとしてARC-AGI-3を完了、40%スコア達成。ARC-AGI-3はインタラクティブベンチマークでフロンティアモデルが苦戦。スコア推移: 0.37%→30.2%を4ヶ月で達成。
- **キーファクト:**
  - GPT-5.6 Sol: ARC-AGI-3で40%スコア達成
  - 改善要因: compaction（履歴圧縮）+ reasoning effort（推論努力）
  - スコア推移: 0.37%（初期）→30.2%（4ヶ月後）→40%
  - ARC-AGI-3: インタラクティブベンチマーク、フロンティアモデルが苦戦
  - 初のオープンソースARC-AGI-3エージェントも登場（Python書き込み型）
- **引用URL:** https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/
- **Evidence ID:** EVD-20260805-0061

### INFO-062
- **タイトル:** AGI Timeline Predictions: Amodei 2026-2027, Hassabis 2030-2035, Altman 2027-2030
- **ソース:** catdoes.com / plutonicrainbows.com / 各種SNS (複数ソース集約)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI, Anthropic, Google DeepMind
- **要約:** AGIタイムライン予測: Sam Altman (OpenAI) = 2027-2030、Dario Amodei (Anthropic) = 2026-2027で「powerful AI」、Demis Hassabis (Google DeepMind) = 5-10年（2030-2035）。AmodeiはAIが6-12ヶ月以内にほぼ全ソフトウェアエンジニアリングタスクを処理すると予測。Richard Socherは2年以内の再帰的自己改善型超知能を予測。Elon MuskはAIが全人類の知能の総和を超えると予測。
- **キーファクト:**
  - Sam Altman: 2027-2030 window、compute構築中
  - Dario Amodei: 2026-2027で「powerful AI」、SE全タスクを6-12ヶ月で
  - Demis Hassabis: AGI到達5-10年（2030-2035）
  - Richard Socher: 2年以内の再帰的自己改善型超知能
  - AGI-26カンファレンス: 「合意されたベースライン、用語、成功基準がまだない」
- **引用URL:** https://catdoes.com/blog/agi-for-developers ; https://www.plutonicrainbows.com/posts/2026-07-31-how-far-from-what-exactly.html
- **Evidence ID:** EVD-20260805-0062

### INFO-063
- **タイトル:** Recursive Self-Improvement Research: Frontis-MA1 + OpenAI Recruits Lilian Weng
- **ソース:** HuggingFace / AlphaXiv / SNS (研究論文/SNS)
- **公開日:** 2026-08-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI
- **要約:** Frontis-MA1論文: 機械学習エンジニアリング（MLE）をテストベッドとするRSI研究。システムはタスクプログラムと検索結果を改善するが、自律的に自らの基盤モデルを再訓練・訓練設計を再設計はしない。OpenAIがLilian WengをRSI研究のためにリクルート。SPAR AI: RSIループが「大規模で未探索の攻撃表面」を生み出すと警告。
- **キーファクト:**
  - Frontis-MA1: RSI研究のMLEテストベッド、タスク改善はするが自己再訓練はしない
  - OpenAI: Lilian WengをRSI研究のためリクルート
  - SPAR AI: RSIループが「大規模で未探索の攻撃表面」を創出と警告
  - RSI = AIが自身のアルゴリズムと性能を反復的に向上させる能力
- **引用URL:** https://huggingface.co/papers/2607.28568 ; https://www.facebook.com/groups/868876935222403/posts/1372390791537679/
- **Evidence ID:** EVD-20260805-0063

### INFO-064
- **タイトル:** AI Safety Policy: No Global Treaty Consensus, US State Patchwork, Mandatory Insurance Model
- **ソース:** Foreign Policy / CSIS / Diplo (政策分析/国際関係)
- **公開日:** 2026-08-03
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** (政府・国際機関)
- **要約:** 国際AI条約の合意形成なし（WAICO/AI for Good Summit）。米国は州レベル（CA、NY等）でカタストロフィックリスク管理の文書化義務を法制化。連邦レベルでは下院共和党が10年間の州AI規制禁止条項を税法案に挿入。代替案としてAI開発者に義務保険を課す「規制市場」モデルが提案。30ヶ国が軍事AIデプロイに関する「AI・自律性の責任ある使用」政治宣言に署名。
- **キーファクト:**
  - 国際的合意: WAICOで「グローバルAI条約交渉のコンセンサスなし」
  - 米国州法: CA、NY等がカタストロフィックリスク文書化義務
  - 連邦: 下院共和党が10年州規制禁止条項を提案
  - 代替モデル: AI開発者への義務保険（insurerが安全監査実施）
  - 軍事AI: 30ヶ国が「責任ある使用」政治宣言に署名
- **引用URL:** https://foreignpolicy.com/2026/08/03/artificial-intelligence-ai-regulation-safety-california-new-york-pope-leo/ ; https://www.diplomacy.edu/blog/waico-and-the-politics-of-ai-cooperation/
- **Evidence ID:** EVD-20260805-0064

### INFO-065
- **タイトル:** Anthropic Refused Pentagon "All Lawful Purposes" Contract; Autonomous Weapons Red Line
- **ソース:** Sage Journals / YouTube / SNS (学術/動画)
- **公開日:** 2026-08-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, Anduril, Palantir
- **要約:** Anthropic CEO Amodeiが完全自律型兵器を阻止する「レッドライン」を明示。Anthropicはペンタゴン契約の「すべての合法的な目的」でのモデル使用を許可する条項を拒否。国内監視と自律型兵器のリスクを理由。Palantir CEO Alex KarpがOpenAIとAnthropicを公然非難。1200人以上のAI労働者が米国政府に声明書。Anduril CEOはAI兵器論争は「誤解されている」と反論。
- **キーファクト:**
  - Anthropic: ペンタゴン「すべての合法的目的」条項を拒否（国内監視・自律兵器リスク）
  - Amodei: 完全自律型兵器阻止をレッドラインとして明示
  - 1200人以上のAI労働者が政府に声明書
  - Palantir CEO Karp: OpenAI/Anthropicを非難
  - Anduril CEO: AI兵器論争は「誤解されている」
- **引用URL:** https://journals.sagepub.com/doi/10.1177/10778004261468239 ; https://www.youtube.com/shorts/n2eU0LuyWoI
- **Evidence ID:** EVD-20260805-0065

### INFO-066
- **タイトル:** ByteDance AI Reorg: Lark+Doubao Teams Merged; AI Capex Raised to ¥200B+ ($30B)
- **ソース:** GeekPark / 華爾街見聞 / SCMP (中国テックメディア/主要紙)
- **公開日:** 2026-07-30
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceが7月30日にAI業務の大規模組織再編を実施。飛書（Lark）製品チームと豆包（Doubao）製品チームを統合、新「豆包産品團隊」を設立（趙祺が統括）。飛書商業化チームは火山引擎と統合し新ToB GTM組織「創造力服務平台」を設立。2026年AI資本支出計画を¥2000億以上（約$300億）に上方修正（前回計画¥1600億から25%以上増）。年間AI投資は最大$700億との観測も。
- **キーファクト:**
  - 飛書×豆包チーム統合: 新「豆包産品團隊」（趙祺統括）
  - 飛書商業化×火山引擎統合: 新ToB GTM組織
  - 2026年AI資本支出: ¥2000億+（約$300億）、25%増
  - 年間AI投資観測: 最大$700億、来年$1000億可能性
  - 13名以上のByteDance出身者がAI創業に流出（累計融资数億元）
- **引用URL:** https://www.geekpark.net/news/368374 ; https://wallstreetcn.com/articles/3771900
- **Evidence ID:** EVD-20260805-0066

### INFO-067
- **タイトル:** Doubao DAU Breaks 100M; Q1 2026 MAU 340M (QuestMobile)
- **ソース:** QuestMobile / 財聯社 / Sina Finance (中国市場データ/主要財務メディア)
- **公開日:** 2026-08-05
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance, Alibaba, DeepSeek
- **要約:** 豆包（Doubao）DAUが1億人を突破（2025年12月）。ByteDance内で1億DAU達成APPの中でUG/マーケティング費用が最低。Q1 2026 AIアプリ月活: 豆包3.4億、千問1.7億、DeepSeek 1.3億（QuestMobile）。業界全体でユーザー量と粘性が共に上昇、競争が後半戦に突入。ByteDance私募市場評価額: 約$3300億（一部投資家は$4800億と試算）。
- **キーファクト:**
  - 豆包DAU: 1億人突破（2025年12月）
  - Q1 2026 MAU: 豆包3.4億、千問1.7億、DeepSeek 1.3億
  - UG/マーケティング費用: ByteDance内1億DAU APP中で最低
  - ByteDance評価額: 私募市場約$3300億
  - AIアプリ市場: ユーザー量+粘性が共に上昇、競争後半戦へ
- **引用URL:** https://www.questmobile.com.cn/research/report/2046482337382842370/ ; https://finance.sina.com.cn/roll/2025-12-24/doc-inhcwxmi9810374.shtml
- **Evidence ID:** EVD-20260805-0067

### INFO-068
- **タイトル:** ByteDance Seed 2.0 Models + Seedance 2.5: Full-Agent Model Family, 30s Video Gen
- **ソース:** seed.bytedance.com (公式) / evolink.ai
- **公開日:** 2026-08-05
- **信頼性コード:** A-1
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** Seed 2.0モデルファミリー正式リリース（2026年2月14日、春晩2日前）: Pro/Lite/Mini/Codeの4バリエーション。Agent時代向けの汎用Agentモデル。Seed 2.0 Pro API価格: $0.47/$2.35 per M tokens。Seedance 2.5: 単回生成30秒動画、複数論理的関連ショット構成。Seedance 2.0: テキスト/画像/動画/音声の全モーダル入力対応、最大4K出力、音声ネイティブ生成。
- **キーファクト:**
  - Seed 2.0: Pro/Lite/Mini/Code、2026年2月14日リリース
  - Pro価格: $0.47/$2.35 per M tokens（GPT-5.2/Opus 4.5/Gemini 3 Proと比較）
  - Seedance 2.5: 単回30秒動画生成、複数ショット叙事
  - Seedance 2.0: 全モーダル入力（最大9画像+3動画+3音声）、4K出力
  - Coze: 多エージェント協調、自然言語アプリ開発プラットフォーム
- **引用URL:** https://seed.bytedance.com/zh/blog/seed2-0-正式发布 ; https://seed.bytedance.com/zh/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- **Evidence ID:** EVD-20260805-0068

### INFO-069
- **タイトル:** ByteDance AI Talent Exodus: 13+ Veterans Found Startups in AI Coding, Agents, Creation
- **ソース:** Z Finance / 智東西 (中国テックメディア)
- **公開日:** 2026-08-01
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceから13名以上のAI人材が離脱し創業。AIクリエイション系5名（剪映3名+Flow 2名）、AIコーディング/Agent系3名（MarsCode創設者含む）など。ByteDance内部でDAU100万超のAIネイティブプロダクトは5-6個のみ。騰訓、阿里、華為、百度からも同様のAI人材流出潮。創業方向は embodied intelligence、AIチップ、大モデル応用に集中。累計融资数億元規模。
- **キーファクト:**
  - 13名以上のByteDance出身者がAI創業（2025年〜）
  - AIクリエイション系5名、AIコーディング/Agent系3名
  - ByteDance内部DAU100万超AIプロダクト: 5-6個のみ
  - 騰訓/阿里/華為/百度からも同様の流出
  - 創業方向: embodied intelligence、AIチップ、大モデル応用
- **引用URL:** https://zhuanlan.zhihu.com/p/2051053779689246957
- **Evidence ID:** EVD-20260805-0069

### INFO-070
- **タイトル:** AI Alignment Research Funding: $12K Fellowships, NVIDIA $60K, Growing Pipeline
- **ソース:** Instagram / AI Alignment Foundation / NVIDIA (SNS/研究機関)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** NVIDIA, AI Alignment Foundation
- **要約:** AIアライメント研究資金の拡大シグナル。AI Alignment Foundation: 8週間フルタイムフェローシップ$12,000 stipend、完全リモート、GPU/APIクレジット提供。NVIDIA: 最大$60,000資金提供（進化生物学、神経科学、言語学等の分野含む）。研究対象は技術的AIアライメント、安全評価、ガバナンス。応募締切: 中堅国AI安全協会設計青写真は2026年8月18日。
- **キーファクト:**
  - AI Alignment Foundation: $12,000/8週間フェローシップ、完全リモート
  - NVIDIA: 最大$60,000研究資金
  - 中堅国AI安全協会デザイン青写真: 応募締切8月18日
  - 研究分野: 進化生物学、神経科学、言語学、社会学、法理論含む
- **引用URL:** https://www.instagram.com/reel/DbjqWUbqSws/ ; https://www.facebook.com/opportunitiesforyouth/posts/1493529896137692/
- **Evidence ID:** EVD-20260805-0070

### INFO-071
- **タイトル:** Advertising Industry Disruption: Agencies Must "Evolve Beyond Campaigns" to Survive
- **ソース:** The Sun Nigeria (AAAN Conference) / Barron's (Publicis) (業界メディア/財務メディア)
- **公開日:** 2026-08-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04, KIQ-002-05
- **関連企業:** Publicis, CyberAgent
- **要約:** 広告業界が存亡の岐路。AAANカンファレンス: 「代理店はキャンペーン制作を超えて進化しなければ生存できない」。技術ディスラプション、AI、クリエイターエコノミーが広告のルールを書き換え。Publicis: AI搭載マーケティングと強固な顧客維持で成長、データ買収を発表。広告支出は2025年$1.42兆から2029年に向けて成長予測。CyberAgent AI Lab: 共著論文がML系カンファレンスで採択、売上¥13兆+（FY2025）。
- **キーファクト:**
  - AAAN: 「代理店はキャンペーン制作を超えて進化が必要」
  - Publicis: AI+データ買収で成長、FCF増加
  - 広告支出: 2025年$1.42兆→2029年に向けて成長
  - CyberAgent: 売上¥13兆+（FY2025）、AI Lab論文採択
  - 代理店の価値: コンテンツ制作からビジネス課題解決へ移行
- **引用URL:** https://thesun.ng/aaan-conference-highlights-impact-of-ai-digital-disruption-on-advertising-industry/ ; https://www.facebook.com/barrons/posts/1403437528322821/
- **Evidence ID:** EVD-20260805-0071

### INFO-072
- **タイトル:** [Arbiter動的クエリ] OpenAI Q1 2026: $5.7B Revenue, $3.7B Burn; Government Alignment vs Anthropic
- **ソース:** SNS/Instagram / Memeburn (SNS/業界データ集約)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001 (Arbiter優先)
- **関連企業:** OpenAI, Anthropic, Palantir
- **要約:** OpenAI Q1 2026: $5.7B収益、$3.7Bバーン（研究開発費$19.18B、コンピュート$5.73B）。「OpenAIは政府統合と国防志向を選択」vs Anthropicのアプローチ。2026年7月時点でAnthropicのアプローチがより多くの収益を生成。Palantirの米国商業収益は149%成長、政府ではない顧客653社。ただしOpenAI収益の政府vs民間の具体的百分比率は依然として不明。
- **キーファクト:**
  - OpenAI Q1 2026: 収益$5.7B、バーン$3.7B
  - 研究開発費: $19.18B、コンピュート: $5.73B
  - 「OpenAIは政府統合・国防志向を選択」
  - 2026年7月時点: Anthropicのアプローチがより多く収益生成
  - Palantir: 米国商業（非政府）収益149%成長、653社
  - 政府vs民間内訳の百分比分離: 依然不在（KIQ-OAI-001未解決）
- **引用URL:** https://www.facebook.com/nftworldcompany/posts/1067478582468410/ ; https://www.instagram.com/p/Dbn46xoCezD/
- **Evidence ID:** EVD-20260805-0072

### INFO-073
- **タイトル:** [Arbiter動的クエリ] Claude Code WAU Doubled Since Jan 2026; Codex 3M+ WAU; Cursor 1M+ DAU
- **ソース:** uvik.net / preuve.ai (テック分析/コーディング統計)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-ANT-002 (Arbiter優先)
- **関連企業:** Anthropic, OpenAI, Cursor (Anysphere)
- **要約:** Claude Code WAU（週間アクティブユーザー）が2026年1月から倍増。Codex 3M+ WAU（Sam Altman確認、2026年4月、トークン使用量70%+ MoM成長）。Cursor 1M+ DAU。Claude Code: 9ヶ月で$0→$2.5B収益。ただしClaude CodeのDAU/WAU絶対値とCLI/API/Enterprise完全内訳は依然不明。「ユーザー」定義の不一致が最深のデータ論争（WAU vs DAU vs MAU）。
- **キーファクト:**
  - Claude Code WAU: 2026年1月から倍増（絶対値不明）
  - Codex WAU: 3M+（Sam Altman確認、2026年4月）
  - Cursor DAU: 1M+（最も厳格なエンゲージメント基準）
  - Claude Code収益: $0→$2.5B（9ヶ月）
  - DAU/WAU絶対値・CLI/API/Enterprise内訳: 不在継続（KIQ-ANT-002未解決）
  - 「ユーザー」定義不一致: WAU/DAU/MAUで比較困難
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/ ; https://preuve.ai/blog/ai-coding-models-statistics-2026
- **Evidence ID:** EVD-20260805-0073

### INFO-074
- **タイトル:** [Arbiter動的クエリ] Military AI Human Override: US SOCOM Warning, "Contractual Authority to Stop" — No Quantitative Rejection Rate
- **ソース:** Washington Examiner / CNBC / NBC News (主要メディア)
- **公開日:** 2026-08-04
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-MIL-001 (Arbiter優先)
- **関連企業:** Anduril, 米国政府/軍
- **要約:** 米特殊作戦軍(SOCOM)司令官がAIリスクについて警告。米政府は「システム停止、承認版の凍結」の契約上・技術的権限を保持すべきと主張。ウクライナがAI搭載「ターミネーター」ドローン・ロボ上陸艇を実戦展開。Anduril CEOはAI兵器論争は「誤解されている」と主張。ただし人間却下比率の定量データ（DoD運用データ等）は依然として完全に不在。概念的分析は存在するが定量的実証なし。
- **キーファクト:**
  - 米SOCOM司令官: AIリスク警告
  - 米政府: 「システム停止・承認版凍結」の契約上・技術的権限保持を主張
  - ウクライナ: AI「ターミネーター」ドローン・ロボ上陸艇を実戦展開
  - Anduril CEO: AI兵器論争は「誤解」、数十年の自律兵器使用履歴
  - 人間却下比率の定量データ: 完全不在（KIQ-MIL-001未解決）
- **引用URL:** https://www.facebook.com/WashingtonExaminer/posts/1441423047854249/ ; https://www.facebook.com/NBCNews/posts/1433202082004986/
- **Evidence ID:** EVD-20260805-0074

### INFO-075
- **タイトル:** [Arbiter動的クエリ] Enterprise RFP: SOC2/ISO27001 Mandatory But Security ≠ Safety; AI Model Safety Not in RFPs
- **ソース:** Pulsar Platform / Inventive.ai / Ammune.ai (業界ガイド/RFP分析)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-FLI-001 (Arbiter優先)
- **関連企業:** (複数企業・RFP分析)
- **要約:** エンタープライズRFPでSecurity & Compliance要件（SOC 2 Type II、ISO 27001、GDPR）が標準必須項目化。RFPの技術的・セキュリティ関連文書要求が3年前より増加。ただし「security（情報セキュリティ）」≠「safety（AIモデルの安全性・アライメント）」。エンタープライズRFPでAIモデル安全性（safety）の直接的言及や非Anthropic企業の安全性差別化事例は依然として観察されず。KIQ-FLI-001の不在継続を確認。
- **キーファクト:**
  - RFP必須: SOC 2 Type II、ISO 27001、GDPR（Security & Compliance）
  - 高規制バイヤー: Security比重を20%以上に引上げ推奨
  - 技術的・セキュリティ関連文書要求が3年前より増加
  - 重大制約: security ≠ safety（RFPで「safety」直接言及なし）
  - 非Anthropic企業の安全性差別化事例: 不在継続
- **引用URL:** https://www.pulsarplatform.com/guides/enterprise-rfp-checklist-social-listening-spec-sheet ; https://www.inventive.ai/blog-posts/request-proposal-examples-templates-guide
- **Evidence ID:** EVD-20260805-0075

### INFO-076
- **タイトル:** [Arbiter動的クエリ] Enterprise AI Spending Concentration: Big Tech >$500B Capex, Market $114.87B (2026) — "3 Company" Breakdown Still Unconfirmed
- **ソース:** Reuters/Punch / Mordor Intelligence (主要メディア/市場調査)
- **公開日:** 2026-08-04
- **信頼性コード:** A-2
- **関連KIQ:** SCN-003 (Arbiter優先)
- **関連企業:** Microsoft, Amazon, Meta, Alphabet, IBM
- **要約:** 主要テック企業（Microsoft、Amazon、Meta、Alphabet）の合計AI年間支出が$500B超。エンタープライズAI市場規模$114.87B（2026年、Mordor）。市場リーダー: Microsoft、IBM、AWS、Google。Yellow.ai $550M SPAC IPO。ただし「エンタープライズ支出の90%が3社に集中」の具体的3社内訳は依然として未確認。SCN-003の判断基盤データが不完全。
- **キーファクト:**
  - Big Tech合計AI年間支出: $500B超（Microsoft、Amazon、Meta、Alphabet）
  - エンタープライズAI市場: $114.87B（2026年）
  - 市場リーダー: Microsoft、IBM、AWS、Google
  - Yellow.ai: $550M SPAC IPO目標
  - 「3社」内訳: 未確認継続（SCN-003判断基盤不完全）
- **引用URL:** https://www.facebook.com/punchnewspaper/posts/1512180244279487/ ; https://www.mordorintelligence.com/industry-reports/enterprise-ai-market
- **Evidence ID:** EVD-20260805-0076

### INFO-077
- **タイトル:** [Arbiter動的クエリ] ByteDance/TikTok: "Open Secret" Billions in Annual Losses; Divest-or-Ban Law Suspended by Trump
- **ソース:** RNZ / WSJ / Wikipedia/TechCrunch (主要メディア/百科事典)
- **公開日:** 2026-08-04
- **信頼性コード:** A-2
- **関連KIQ:** H-BTD-002 (Arbiter優先)
- **関連企業:** ByteDance, TikTok
- **要約:** TikTokが年間数十億ドルの損失を出していることは投資家間の「公然の秘密」（The Information 2024年3月報道）。2024年3月: 米下院がByteDanceにTikTok売却または全面禁止を求めるH.R. 7521可決。トランプ政権は就職初日に執行を停止。TikTokは米国デジタルコマース・広告・中小企業収益に数十億ドル貢献。ByteDanceのAI事業赤字幅の推移・TikTok規制リスクによる資金注入能力制約の定量データは依然として不在。
- **キーファクト:**
  - TikTok: 年間数十億ドル損失（投資家間「公然の秘密」）
  - 2024年3月: 米下院H.R. 7521可決（ByteDance売却か全面禁止）
  - トランプ: 就職初日に執行停止
  - TikTok米国経済貢献: デジタルコマース・広告・中小企業収益に数十億ドル
  - AI事業赤字幅推移・TikTok規制リスクの定量データ: 不在継続
- **引用URL:** https://en.wikipedia.org/wiki/TikTok ; https://www.wsj.com/opinion/donald-trump-tiktok-federal-devices-bytedance-china-28d21162
- **Evidence ID:** EVD-20260805-0077

### INFO-078
- **タイトル:** [Arbiter動的クエリ] AI Engineer Median Salary $131,490 (BLS); Design/Evaluation-Specific Data Gap Persists
- **ソース:** US BLS / DeepRec.ai / Kore1 (政府統計/採用ガイド)
- **公開日:** 2026-08-05
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-CAR-002-OPS (Arbiter優先)
- **関連企業:** (複数: BLS、採用市場データ)
- **要約:** AIエンジニア年間中央値給与$131,490（米国BLS）。プロダクトデザイナー中央値$115,000。DeepRec.aiがジェネレーティブAI/自律エージェント向けサラリーガイド発行。4Geeks: AIエンジニア84%採用率、平均55%給与増。ただし「設計/評価固有」の独立した求人倍率データ（Burning Glass/LinkedIn/Indeedの特定カテゴリー）は不在継続。複合カテゴリー（AI Agent Architect等）での初期シグナルはあるが、KIQ-CAR-002-OPSの核心要件は未充足。
- **キーファクト:**
  - AIエンジニア中央値: $131,490/年（米国BLS）
  - プロダクトデザイナー中央値: $115,000/年
  - 4Geeks: 84%採用率、55%平均給与増
  - 設計/評価固有求人倍率データ: 不在継続
  - 複合カテゴリー（AI Agent Architect等）のみで核心要件未充足
- **引用URL:** https://www.facebook.com/WeAreINSGlobal/posts/122226773798518304/ ; https://www.kore1.com/product-designer-salary-guide/
- **Evidence ID:** EVD-20260805-0078

### INFO-079
- **タイトル:** [深掘り] US Government Switched Off Anthropic Frontier Models for 19 Days; Sovereignty Now Board-Level Risk
- **ソース:** kai-waehner.de (Trusted Agentic AI Landscape Q3 2026)
- **公開日:** 2026-08-04
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-003-05, KIQ-005-03
- **関連企業:** Anthropic, OpenAI, Google, Microsoft, AWS, xAI, Meta, Mistral
- **要約:** 2026年前半に2つの構造的イベント発生: (1) SpaceX上場→Anthropic/OpenAIが相次ぎIPO準備（評価額$1T近傍）。(2) 米政府が輸出管理指令でAnthropicの2つの最強モデルを外国人のアクセスに対して停止。Anthropicは全ユーザー向けに両モデルを無効化、19日後に商務省交渉で復旧。「復旧=リスク解消」と読むべきではない。「フロンティアモデルが一夜で政府により停止される」ことが定義された。主権がヨーロッパの脚注ではなく一次リスクに昇格。
- **キーファクト:**
  - 米政府輸出管理指令: Anthropic最強2モデルを外国人アクセス停止
  - Anthropic: 全ユーザー向け無効化（他モデルは継続）
  - 復旧まで19日（商務省交渉後）
  - 教訓: フロンティアモデルが一夜で政府により停止可能
  - 主権: ヨーロッパの脚注→一次リスクに昇格（Forrester「主権は購入基準になった」）
  - MCP: 中立財団の管理下だが、Anthropicがツール生成・SDK大部分を所有→接続レイヤーが一社に集中
  - xAI: ガバナンス失敗パターン（GSA停止、内部告発訴訟、非合意画像生成）でランドスケープ除外
  - モデルレイヤーは交換可能でも、コンテキストグラフ・オーケストレーションは不可→スタックレベルロックインが加速
  - Beijing: 最新モデル重みの輸出管理協議中。Washington: 中国オープンウェイト規制協議中
- **引用URL:** https://kai-waehner.de/blog/2026/08/04/trusted-agentic-ai-landscape-q3-2026-enterprise-vendor-selection-sovereignty-and-lock-in/
- **Evidence ID:** EVD-20260805-0079

### INFO-080
- **タイトル:** [深掘り] Trusted Agentic AI Vendor Landscape: Anthropic=Trusted+Flexible, Google=Trusted+Captured, OpenAI=Risky+Flexible
- **ソース:** kai-waehner.de (Trusted Agentic AI Landscape Q3 2026)
- **公開日:** 2026-08-04
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-05, KIQ-002-01
- **関連企業:** Anthropic, Google, OpenAI, Microsoft, AWS, Meta, Mistral, Cohere, SAP, Salesforce
- **要約:** Q3 2026エンタープライズAIベンダー4象限分類。Trusted+Flexible（Anthropic軸、Mistral、Cohere+Aleph Alpha統合、Meta Llama）。Trusted+Captured（Google支配: Gemini→Vertex AI→Workspaceで構造的ロックイン）。Risky+Flexible（OpenAI信頼中位、DeepSeek/GLM/Kimi/Qwen等中国オープンウェイト）。Risky+Captured（Microsoft最深ロックイン: Copilot+M365+複数モデルレイヤー; AWS Bedrock開放だがAgentCoreでスタックロックイン; SAP/Salesforce: モデル交換可能だがコンテキスト・データ層でロックイン）。
- **キーファクト:**
  - Trusted+Flexible: Anthropic（Constitutional AI+解釈可能性研究）、Mistral（欧州最成熟）、Cohere+Aleph Alpha（越境主権代替）、Meta Llama（最大自己ホスト制御）
  - Trusted+Captured: Google支配（Gemini→GCP推論→Vertex AI→Workspaceで構造的）
  - Risky+Flexible: OpenAI（信頼中位、法的・ガバナンス監視強化）、中国オープンウェイト（DeepSeek/GLM/Kimi/Qwen/Tencent: 技術的強力だが中国管轄・コンテンツ管理リスク）
  - Risky+Captured: Microsoft（最深ロックイン: Copilot+M365+複数モデル）、AWS（Bedrock開放もAgentCoreでスタックロックイン）、SAP/Salesforce（モデル交換可能もコンテキスト層で捕捉）
  - xAI: ランドスケープ除外（ガバナンスパターン失敗: GSA停止、内部告発、非合意コンテンツ、SpaceX統合で責任境界曖昧）
  - Open weights ≠ Open source: 重みのみ vs 重み+コード+データ+ライセンス
- **引用URL:** https://kai-waehner.de/blog/2026/08/04/trusted-agentic-ai-landscape-q3-2026-enterprise-vendor-selection-sovereignty-and-lock-in/
- **Evidence ID:** EVD-20260805-0080
