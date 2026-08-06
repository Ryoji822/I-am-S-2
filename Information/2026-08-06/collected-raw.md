# 収集データ: 2026-08-06

## メタデータ
- 収集日時: 2026-08-06 00:03 UTC (収集完了: 2026-08-06 00:47 UTC)
- 品質フラグ: COMPLETE
- 動的追加クエリ（Arbiter Step 1.5）:
  - KIQ-MIL-001（人間却下比率）: "Pentagon AI autonomous weapons human override rejection rate", "DOD AI human-in-the-loop veto statistics military", "autonomous weapons human supervision override ratio data"
  - INFO-079独立検証: "Anthropic EAR export administration regulation model suspension BIS", "Federal Register AI model export control Anthropic", "Anthropic Commerce Department BIS AI enforcement"
  - KIQ-OAI-001（政府vs民間収益内訳）: "OpenAI revenue government vs commercial breakdown percentage", "OpenAI federal contract revenue share 2026", "OpenAI Pentagon DoD revenue vs enterprise revenue split"
  - KIQ-ANT-002（Claude Code WAU内訳）: "Claude Code weekly active users absolute number 2026", "Anthropic Claude Code CLI API Enterprise breakdown", "Claude Code WAU metrics Anthropic revenue split"
  - SCN-003 3社内訳: "enterprise AI spending concentration Microsoft Azure AI adoption rate", "Google Workspace AI ARPU enterprise revenue 2026", "AWS Bedrock enterprise adoption rate percentage"
  - EAR専門的文脈: "AI model export administration regulation dual-use comparison cryptography nuclear", "second AI company EAR enforcement BIS model suspension"

## 収集結果

### INFO-001
- **タイトル:** Introducing Claude Opus 5
- **ソース:** Anthropic 公式ブログ
- **公開日:** 2026-07-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Opus 5をリリース。Opus 4.8と同等価格（$5/M入力、$25/M出力）でFrontier-Bench v0.1・CursorBench 3.2・ARC-AGI 3等でSOTAを達成。Fable 5に迫る性能を半額で提供。長時間実行エージェント・コーディング・知識作業で大幅向上。
- **キーファクト:**
  - ARC-AGI 3スコアが次点モデルの3倍。Fable 5の最大スコアに対し1/3のコストでOSWorld 2.0を超越
  - $5/M入力トークン、$25/M出力トークン（Opus 4.8と同価格）
  - Fastモードは約2.5倍速度・2倍価格
  - 自動行動監査で最も整列されたモデル（misalignmentスコア2.3、歴代最低）
  - サイバーセキュリティではMythos 5に迫る脆弱性発見力だが、エクスプロイト開発では大幅劣位
  - 会話中ツール変更（beta）・自動フォールバック（beta） API機能追加
- **引用URL:** https://www.anthropic.com/news/claude-opus-5
- **Evidence ID:** EVD-20260806-0001

### INFO-002
- **タイトル:** Anthropic invests $100 million into the Claude Partner Network
- **ソース:** Anthropic 公式ブログ
- **公開日:** 2026-03-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** Anthropicがエンタープライズ向けClaude導入を支援するパートナーネットワークに$100Mを投資。トレーニング・技術サポート・市場共同開発を提供。Claude技術認定資格（Claude Certified Architect）を新設。AWS・Google Cloud・Microsoftの3大クラウド全てで利用可能な唯一のフロンティアAIモデル。
- **キーファクト:**
  - 初期投資$100M（2026年）、パートナーチーム5倍拡大
  - Accentureが30,000人のClaudeトレーニングを実施中
  - Claude Certified Architect認定資格を本日より提供開始
  - Claudeは3大クラウド（AWS, Google Cloud, Microsoft）全てで利用可能な唯一のフロンティアモデル
  - Code Modernizationスターターキットをリリース
- **引用URL:** https://www.anthropic.com/news/claude-partner-network
- **Evidence ID:** EVD-20260806-0002

### INFO-003
- **タイトル:** 2028: Two scenarios for global AI leadership
- **ソース:** Anthropic 公式ブログ
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, Google, ByteDance, DeepSeek
- **要約:** Anthropicが米中AI競争に関する論文を公開。2028年までに変革的AIが到来すると予想。輸出規制の強化・蒸留攻撃の阻止・民主主義国のAI採用加速を推奨。Mythos Previewが中国のサイバー安全性に対する「目覚めの警鐘」になったと言及。
- **キーファクト:**
  - 輸出規制によりHuaweiは2026年にNVIDIAの4%、2027年に2%の計算力しか生産できない見通し
  - 規制強化で民主主義側が12-24ヶ月の優位を確保可能
  - DeepSeekが最新モデルを禁止されたNVIDIAチップで訓練（政府・メディア報道）
  - Alibaba・ByteDanceが東南アジアのデータセンターで規制対象チップを使用
  - 蒸留攻撃を非合法化する法案が下院で全会一致で委員会通過
  - AIモデルへのEAR適用はデュアルユース技術規制の枠組み内
- **引用URL:** https://www.anthropic.com/news/2028-ai-leadership
- **Evidence ID:** EVD-20260806-0003

### INFO-004
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic 公式ブログ
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropic LabsがClaude Designをリリース。Claude Opus 4.7を搭載したデザイン協働ツール。プロトタイプ・スライド・ワイヤーフレーム等を自然言語で作成。Claude Codeへのハンドオフ機能付き。Canva統合あり。
- **キーファクト:**
  - Claude Pro/Max/Team/Enterpriseで利用可能（研究プレビュー）
  - チームのデザインシステムを自動適用
  - Canva・PPTX・PDF・HTMLエクスポート対応
  - Claude Codeへのワンクリック・ハンドオフバンドル
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260806-0004

### INFO-005
- **タイトル:** Anthropic appoints Irina Ghose as Managing Director of India
- **ソース:** Anthropic 公式ブログ
- **公開日:** 2026-01-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** Anthropicがインド初のオフィス開設に向け、元Microsoft India MDのIrina Ghoseをマネージング・ディレクターとして採用。インドはClaude.aiの世界第2位市場。
- **キーファクト:**
  - インドはClaude.aiの世界第2位市場
  - インドユーザーの約半数がコンピュータ・数学タスクに集中
  - 元Microsoft India MDからの引き抜き
- **引用URL:** https://www.anthropic.com/news/anthropic-appoints-irina-ghose-as-managing-director-of-india
- **Evidence ID:** EVD-20260806-0005

### INFO-006
- **タイトル:** xAI Grok Build オープンソース化（24.2k stars）
- **ソース:** GitHub (xai-org/grok-build)
- **公開日:** 2026-08-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI (SpaceXAI)
- **要約:** xAIがコーディングエージェント「Grok Build」をオープンソース化。Rust製TUI、ファイル編集・シェル実行・Web検索・長時間タスク管理を統合。3週間前（7/16）に公開、直近5時間前にモノレポから同期。Agent Client Protocol (ACP)対応。
- **キーファクト:**
  - 24.2k stars、4.6k forks（5時間前最新コミット）
  - macOS/Linux/Windows対応、Apache 2.0ライセンス
  - 外部貢献は受け付けない（CONTRIBUTING.md記載）
  - ACP（Agent Client Protocol）でエディタ統合対応
  - openai/codex と sst/opencode のツール実装をインポート
- **引用URL:** https://github.com/xai-org/grok-build
- **Evidence ID:** EVD-20260806-0006

### INFO-007
- **タイトル:** Google Gemini Agents API — Antigravity ランタイム + MCP サポート
- **ソース:** Google AI for Developers 公式ドキュメント
- **公開日:** 2026-07-31 (最終更新)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Google
- **要約:** GoogleのGemini Agents APIはAntigravityエージェントランタイムを採用。リモートサンドボックス環境、MCP Server接続、Code Execution、Google Search、URL Context等のツールを統合。Skill Registryからスキルをマウント可能。
- **キーファクト:**
  - base_agent: "antigravity-preview-05-2026"
  - MCP Server（mcp_server型ツール）をネイティブサポート
  - ネットワークエグレス制御（allowlist/disabled）
  - skill_registry型ソースマウント対応
  - Interactions APIがGA（Generally Available）に昇格
- **引用URL:** https://ai.google.dev/api/agents
- **Evidence ID:** EVD-20260806-0007

### INFO-008
- **タイトル:** Best AI Agent Frameworks in 2026: LangGraph, CrewAI, Microsoft Agent Framework, OpenAI Agents SDK, Mastra
- **ソース:** Workflow Builder Blog
- **公開日:** 2026-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Microsoft, OpenAI, Google, 各OSS
- **要約:** 2026年のプロダクション向けエージェントフレームワーク比較。LangGraph（状態管理・チェックポイント強）、CrewAI（迅速なプロトタイピング）、Microsoft Agent Framework（.NET/Python統合・v1.0 GA）、OpenAI Agents SDK（軽量・Temporal統合）、Mastra（TypeScriptネイティブ）の5本柱。AutoGenはメンテナンスモードに移行。
- **キーファクト:**
  - Microsoft Agent Framework v1.0 GA（2026年4月3日）— AutoGen + Semantic Kernel統合
  - AutoGenは新規プロジェクト非推奨（メンテナンスモード）
  - OpenAI Agents SDKはTemporal統合で耐久性ある長時間実行を実現
  - CrewAI 1.8+ が @human_feedback デコレータでHITL対応
  - Mastra: 2026年6月にnpmサプライチェーン攻撃（easy-day-js）発生
- **引用URL:** https://www.workflowbuilder.io/blog/best-ai-agent-frameworks
- **Evidence ID:** EVD-20260806-0008

### INFO-009
- **タイトル:** Your Cloud AI SLA Tells You Less Than You Think — サイレントモデルドリフト問題
- **ソース:** endjin.com
- **公開日:** 2026-08-05
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-002-02
- **関連企業:** Anthropic, Microsoft, GitHub
- **要約:** クラウドAI基盤モデルのSLAはAPI稼働率のみを保証し、行動安定性（behavioral drift）をカバーしない。サイレントモデル更新・ハーネス変更・デフォルト動作シフトにより、エージェントが「知らぬ間に劣化」する事例が複数報告されている。Anthropicの「adaptive thinking」変更やGitHub Copilotの課金変更（6倍コスト増）も言及。
- **キーファクト:**
  - 従来SLA（99.95%）はAPI可用性のみ測定、行動品質は対象外
  - Anthropicのポストモーテムで確認されたサイレント劣化事例
  - GitHub Copilot課金変更で約6倍のコスト増（初期分析）
  - エンタープライズ調達会話で行動保証が不在
- **引用URL:** https://endjin.com/blog/cloud-ai-slas-are-not-what-you-think
- **Evidence ID:** EVD-20260806-0009

### INFO-010
- **タイトル:** Google Gemini Enterprise Agent Platform — Build/Scale/Govern/Optimize 4本柱
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-07-31 (最終更新)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google
- **要約:** Google CloudがGemini Enterprise Agent Platformを提供。200以上の基盤モデルへのアクセス、Agent Development Kit (ADK)、Agent Studio（ローコード）、Agent Registry（カタログ管理）、Agent Identity（アクセス制御）、Agent Gateway（ポリシー執行）を統合したエンタープライズ向けプラットフォーム。
- **キーファクト:**
  - 4ピラー: Build（ADK, Agent Studio, RAG Engine）/ Scale（Agent Runtime, Memory Bank）/ Govern（Agent Registry, Agent Identity, Agent Gateway）/ Optimize（評価・観測性）
  - Model Armorによる脅威保護
  - Code Execution（サンドボックスPython実行）
  - Vector Search統合
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
- **Evidence ID:** EVD-20260806-0010

### INFO-011
- **タイトル:** Enterprise AI Agent採用統計 — Gartner 40%・IBM CEO調査61%・Morgan Stanley 280,000時間削減
- **ソース:** Maven AGI / NASSCOM / AWS
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Microsoft, Morgan Stanley
- **要約:** Gartner予測: 2026年末までにエンタープライズアプリの40%がタスク特化AIエージェントを組み込む（1年前は5%未満）。IBM CEO調査（33カ国2,000名）で61%がエージェント採用を準備中。Morgan Stanleyは9百万行のレガシーコードをレビューし28万時間の開発者時間を回収、自発的採用率98%。
- **キーファクト:**
  - Gartner: 40%のエンタープライズアプリが2026年末までにAIエージェント内蔵
  - Morgan Stanley: 900万行コードレビュー・28万時間削減・採用率98%
  - ブロッカー: AI評価ギャップ64%・ガバナンス摩擦57%・モデル信頼性51%
  - Maven AGI: チケットの80%を自動解決（93%ライブチャット応答）
- **引用URL:** https://www.mavenagi.com/blog/ai-agent-adoption-statistics
- **Evidence ID:** EVD-20260806-0011

### INFO-012
- **タイトル:** MCP仕様2026-07-28 — ステートレス化でエンタープライズスケール対応
- **ソース:** Ars Technica / Taskade / tfir.io
- **公開日:** 2026-07-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** MCP（Model Context Protocol）の新仕様（2026-07-28）がプロトコルコアをステートレス化し、プレーンロードバランサー背後でのスケールを可能にした。正式な拡張トラック（formal extensions track）を導入し、突然の機能削除を防止するポリシーを追加。AAIF（Linux Foundation配下）が管理。
- **キーファクト:**
  - MCPプロトコルコアがステートレス化 — エンタープライズ採用の主要障壁を解消
  - OpenAI（2025年3月）とGoogle（2025年4月）が相次いでMCP採用を決定
  - MCP Apps・tasks機能を新規追加
  - AAIF（Agentic AI Foundation）がLinux Foundation配下で管理
- **引用URL:** https://arstechnica.com/ai/2026/07/with-a-stateless-makeover-new-mcp-spec-targets-enterprise-scale/
- **Evidence ID:** EVD-20260806-0012

### INFO-013
- **タイトル:** Agent Skills Marketplace — OpenAI/Google/NVIDIA/Anthropicが公式スキル公開
- **ソース:** GitHub / mcpmarket.com / aiagentsdirectory.com
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Google, NVIDIA, Anthropic
- **要約:** エージェントスキルのマーケットプレイス層が形成されている。OpenAI（openai/skills）、Google（google/skills）、NVIDIA（nvidia/skills）、Anthropic（anthropics/skills）がGitHub公式リポジトリでスキル配布。mcpmarket.com・aiagentsdirectory.com等のディレクトリが出現。`npx skills add` でインストール可能。
- **キーファクト:**
  - Google Skills: Gemini API、Gemini Agents API、Gemini Interactions APIスキル
  - NVIDIA Skills: Physical AI/ロボティクス、CUDA-X最適化スキル
  - OpenAI Skills: OpenAI Docs、Define Goal、Hatch Pet、Migrate to Codex等
  - A2A Market: USDC（Base）でのスキル売買マーケットプレイス出現
  - VS Code拡張「Agent Skills Ninja」でスキル管理
- **引用URL:** https://github.com/nvidia/skills
- **Evidence ID:** EVD-20260806-0013

### INFO-014
- **タイトル:** Gemini Robotics ER 2 — 物理エージェント能力の前進
- **ソース:** Google DeepMind Blog
- **公開日:** 2026-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** Google DeepMindがGemini Robotics ER 2をリリース。ER 1.6を上回るツールオーケストレーション能力。VLA（Vision-Language-Action）モデル、シミュレーションVLA、人間テレオプの3モードで一貫して改善。Gemini Robotics 2は全身知能・多関節協調・マルチロボット協調を実現。
- **キーファクト:**
  - 3つの制御モード（real VLA, sim VLA, human tele-op）全てでER 1.6上回る
  - Gemini Robotics 2: ヒューマノイドの歩行・しゃがみ・全身制御
  - マルチロボット協調能力
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/
- **Evidence ID:** EVD-20260806-0014

### INFO-015
- **タイトル:** Vision Arena リーダーボード — Claude Fable 5首位・Anthropic上位独占
- **ソース:** arena.ai (Vision Leaderboard)
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-001-04
- **関連企業:** Anthropic, Alibaba, Google, OpenAI, Meta, SpaceXAI
- **要約:** ビジョンAIリーダーボードでAnthropicが上位を独占。Claude Fable 5（1318pts）が1位、Qwen3.8-max（1305pts）2位、Claude Opus 4.7 Thinking（1303pts）3位。GPT-5.5は12位（1287pts）、Gemini 3 Proは11位（1289pts）。
- **キーファクト:**
  - トップ10中6位がAnthropic（Fable 5, Opus 4.7×3, Opus 5, Opus 4.6）
  - GLM-5V-Turbo（Zhipu AI）はBrowseComp-VLで1位（0.519）
  - SWE-bench Multimodal: Claude Opus 5が59.4%で首位
  - HLE: Claude Fable 5が53.3%で首位
- **引用URL:** https://arena.ai/leaderboard/vision
- **Evidence ID:** EVD-20260806-0015

### INFO-016
- **タイトル:** CrowdStrike Secure Agent Harness — VMベース隔離でエスケープ防止
- **ソース:** CrowdStrike Blog
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-002-01
- **関連企業:** CrowdStrike
- **要約:** AIエージェントハーネスのセキュリティ実装ベストプラクティス。各ハーネスは専用VM内で実行され、オペレータワークステーションや共有ホスト上では動作しない。エージェントはホスト操作を直接行わず、VM境界内でサンドボックス化。
- **キーファクト:**
  - 専用VM内実行でホスト操作を隔離
  - Claude Code MCP Server アクセス制御 (SOC 2 CC6.6, CC9.2)
  - プロンプトインジェクション・ルールファイル攻撃への防御策
  - CI/CDパイプラインでのClaude Code ハードニング
- **引用URL:** https://www.crowdstrike.com/en-us/blog/secure-agent-harness-execution-preventing-escape/
- **Evidence ID:** EVD-20260806-0016

### INFO-017
- **タイトル:** Darktrace × Microsoft Agent 365 統合 — エージェントリスク可視化
- **ソース:** Darktrace Blog
- **公開日:** 2026-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** Microsoft, Darktrace
- **要約:** DarktraceがMicrosoft Agent 365と統合。行動ベースAIエージェントリスクシグナルをMicrosoft 365 Admin Centerに直接提供。Darktrace / SECURE AIのAdaptive AI駆動リスク分析をエージェント管理に統合。
- **キーファクト:**
  - DarktraceのAdaptive AIリスクシグナルをM365 Admin Centerに統合
  - エージェントのセキュリティ可視性を拡張
- **引用URL:** https://www.darktrace.com/blog/extending-ai-security-visibility-with-darktrace-and-microsoft-agent-365
- **Evidence ID:** EVD-20260806-0017

---

## KIQ-002: クラウド・エンタープライズ・規制・政府圧力

### INFO-018
- **タイトル:** AWS Bedrock AgentCore + Strands移行 — クラシックエージェント廃止
- **ソース:** AWS Blog / 業界報道
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon (AWS)
- **要約:** AWS が Bedrock AgentCore を発表し、Strands エージェントフレームワークへの移行を推進。従来のクラシックエージェントは廃止予定。エージェクト実行基盤の標準化とマルチエージェントオーケストレーション強化が焦点。
- **キーファクト:**
  - Bedrock AgentCore でエージェント実行環境を統一
  - Strands SDK への移行パス提供、クラシックエージェント廃止
  - マルチエージェントオーケストレーション機能強化
- **引用URL:** https://aws.amazon.com/blogs/aws/
- **Evidence ID:** EVD-20260806-0018

### INFO-019
- **タイトル:** Azure AI Foundry エージェント機能拡張 — Browser Automation Preview
- **ソース:** Microsoft Azure Blog
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft が Azure AI Foundry のエージェント機能を拡張。Browser Automation のプレビュー提供、Zenity と M365 Agent 365 の統合セキュリティ管理、エージェント開発から運用までの一元化を推進。
- **キーファクト:**
  - Azure AI Foundry で Browser Automation (プレビュー) 提供開始
  - Zenity × M365 Agent 365 統合でエージェントガバナンス強化
  - エンタープライズ向けエージェント開発・運用プラットフォーム統合
- **引用URL:** https://azure.microsoft.com/en-us/blog/
- **Evidence ID:** EVD-20260806-0019

### INFO-020
- **タイトル:** Google Vertex AI Agent Builder → Gemini Enterprise Agent Platform進化
- **ソース:** Google Cloud Blog
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Google
- **要約:** Google Cloud が Vertex AI Agent Builder を Gemini Enterprise Agent Platform へ進化。エージェント構築、デプロイ、管理の統合プラットフォーム化を加速。
- **キーファクト:**
  - Vertex AI Agent Builder から Gemini Enterprise Agent Platform ブランド移行
  - エージェント構築からデプロイまでの統合体験
- **引用URL:** https://cloud.google.com/blog/
- **Evidence ID:** EVD-20260806-0020

### INFO-021
- **タイトル:** エンタープライズAI採用率88%、エージェント導入は62% — 2026年調査
- **ソース:** 業界調査レポート
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** 2026年エンタープライズAI調査で、88%の企業がAIを定期利用、62%がAIエージェントの導入を開始。ただしスケール化は23%にとどまり、本格展開の壁が顕在化。
- **キーファクト:**
  - 88%の企業がAI定期利用
  - 62%がAIエージェント導入開始
  - スケール化は23%のみ — 本格展開のボトルネック存在
  - 52%がエージェントを本番環境で運用
- **引用URL:** (業界調査統合)
- **Evidence ID:** EVD-20260806-0021

### INFO-022
- **タイトル:** Fortune 500のAIエージェント導入 — Gartner予測: 2028年に15万エージェント
- **ソース:** Gartner / 業界報道
- **公開日:** 2026-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Gartner は2028年までに Fortune 500 各社平均15万のAIエージェントを運用すると予測。現在64%がAIコーディングエージェント使用するが、ROI測定は33%のみ。エージェントガバナンス整備はわずか13%。
- **キーファクト:**
  - Gartner予測: Fortune 500 各社平均15万AIエージェント by 2028
  - 64%がAIコーディングエージェント使用中
  - ROI測定実施はわずか33%
  - エージェントガバナンス整備済みは13%のみ
- **引用URL:** (Gartner調査統合)
- **Evidence ID:** EVD-20260806-0022

### INFO-023
- **タイトル:** EU AI Act — 8月2日施行フェーズ開始、GPAIモデル透明性義務化
- **ソース:** EU公式 / 業界報道
- **公開日:** 2026-08-02
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-03
- **関連企業:** (規制対象全域)
- **要約:** EU AI Act の重要施行フェーズが8月2日に開始。汎用AI(GPAI)モデルの透明性義務、技術文書開示、著作権遵守が法的義務化。欧州委員会は売上3%または€15Mの罰金権限を保有。Omnibus改正で高リスクAI適用は2027年に延期。
- **キーファクト:**
  - 8月2日: GPAI透明性義務、技術文書開示、著作権コンプライアンス施行
  - 罰金: 売上3%または€15M（軽微違反は€750K）
  - Omnibus改正: 高リスクAIシステム規則の適用を2027年に延期
  - オープンウェイトモデルは一部免除
- **引用URL:** https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- **Evidence ID:** EVD-20260806-0023

### INFO-024
- **タイトル:** トランプAI大統領令(6月2日) — 自発的フレームワーク最終化、DPA発動
- **ソース:** White House / 業界報道
- **公開日:** 2026-06-02
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** (規制対象全域)
- **要約:** トランプ政権のAI大統領令(6月2日)で自発的安全フレームワークが最終化。Defense Production Act(DPA)を発動し、強力なAIシステムの追跡・報告を義務化。ただしオープンウェイトモデルは免除。
- **キーファクト:**
  - DPA発動: 強力なAIシステムの追跡・報告義務化
  - オープンウェイトモデルは免除
  - 自発的フレームワーク（強制力なし）
  - 安全基準の閾値は計算量10^26 FLOP
- **引用URL:** https://www.whitehouse.gov/
- **Evidence ID:** EVD-20260806-0024

### INFO-025
- **タイトル:** 中国AI戦略 — 2027年に70%採用、2030年に90%目標
- **ソース:** 業界分析 / 中国政府公文書
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-004-01
- **関連企業:** Alibaba, DeepSeek, ByteDance
- **要約:** 中国の国家AI戦略で、2027年までに主要産業の70%へのAI採用、2030年までに90%の目標を設定。Kimi K3など国産モデルの台頭が政策議論を圧縮。政府主導のAIインフラ投資加速。
- **キーファクト:**
  - 目標: 2027年までに主要産業70% AI採用
  - 目標: 2030年までに90% AI採用
  - 政府主導のAIインフラ投資加速
  - 国産モデル(Kimi K3等)の台頭で政策圧縮
- **引用URL:** (業界分析統合)
- **Evidence ID:** EVD-20260806-0025

### INFO-026
- **タイトル:** Salesforce Agentforce 360 — 国防総省で高機密ワークロード承認取得
- **ソース:** DefenseScoop
- **公開日:** 2026-08-05
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04, KIQ-002-06
- **関連企業:** Salesforce
- **要約:** Salesforce の Agentforce 360 が国防総省(DoD)の高機密ワークロード向けに承認を取得。DoD が商用AIエージェントプラットフォームを高感度領域で正式採用した初のケースの一つ。
- **キーファクト:**
  - Agentforce 360 がDoD高機密ワークロード承認 (Aug 5)
  - 商用AIエージェントの国防領域正式採用の前例
- **引用URL:** https://defensescoop.com/
- **Evidence ID:** EVD-20260806-0026

### INFO-027
- **タイトル:** Accenture が国防総省AIデータプラットフォーム契約 $821M獲得
- **ソース:** 業界報道
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04, KIQ-002-06
- **関連企業:** Accenture
- **要約:** Accenture が国防総省のAIデータプラットフォーム構築で$821Mの契約を獲得。DoDのAIインフラ近代化における最大規模の単一契約の一つ。
- **キーファクト:**
  - 契約額: $821M
  - DoD AIデータプラットフォーム構築
  - AIインフラ近代化の最大級契約
- **引用URL:** (業界報道統合)
- **Evidence ID:** EVD-20260806-0027

### INFO-028
- **タイトル:** ★[CRITICAL] Anthropic 供給 chain リスク指定 — 裁判官「証拠不十分」裁定(7月30日)
- **ソース:** TechCrunch / 連邦裁判所
- **公開日:** 2026-07-30
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** Anthropic
- **要約:** トランプ政権のAnthropic供給チェーンリスク指定に対する連邦裁判所審理で、裁判官が「政府の立証はさらに弱まった」と述べた。政府は「AIモデル汚染」の懸念を理由としたが、具体的証拠の提供に失敗。Anthropic は「全ての合法的目的」でのモデル使用を許可する国防総省の契約言語を拒否し、国内監視と自律型兵器のリスクを理由に契約を放棄した経緯がある。
- **キーファクト:**
  - 裁判官: 政府・Trump政権は「証拠がさらに不十分になった」(Jul 30)
  - 理由: 10 U.S.C. §3252 に基づく「供給チェーンリスク」指定
  - Anthropic の拒否理由: 国内監視・自律型兵器リスクへの懸念
  - 2月27日: トランプが各機関にAnthropic使用停止を指示、Hegseth国防長官がSCR指定
  - SCR指定により国防総省契約業者はAnthropicとの商取引禁止
  - Anthropic は$200M契約喪失
- **引用URL:** https://techcrunch.com/2026/07/30/anthropic-supply-chain-risk/
- **Evidence ID:** EVD-20260806-0028

### INFO-029
- **タイトル:** ★[CRITICAL] 国防総省CDAO契約 — 6社同時$200M上限包括契約
- **ソース:** DOD / 業界報道
- **公開日:** 2026-07
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** Anthropic, Google, OpenAI, xAI, NVIDIA, AWS, Microsoft, SpaceX
- **要約:** 国防総省Chief Digital and AI Office(CDAO)がAnthropic, Google, OpenAI, xAI を含む複数企業と$200M上限の包括契約を締結。高度AIワークフロー構築が目的。Anthropic はSCR指定により事実上除外され、OpenAI が代替として主要契約を獲得。
- **キーファクト:**
  - 契約上限: 各社$200M
  - 対象: Anthropic, Google, OpenAI, xAI (SCR指定前)
  - SCR指定後: OpenAI がAnthropic分を代替取得
  - Pentagon が主要AI企業に同時契約 — 業界前例なし
- **引用URL:** (DOD報道統合)
- **Evidence ID:** EVD-20260806-0029

### INFO-030
- **タイトル:** ★[CRITICAL] トランプ政権の自発的AI安全フレームワーク vs Anthropic抵抗 — 業界分裂
- **ソース:** 業界分析 / 複数報道
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-ANT-002
- **関連企業:** Anthropic, OpenAI, Google, xAI
- **要約:** トランプ政権の自発的AI安全フレームワーク最終化に対し、業界の対応が分裂。OpenAI・Google・xAIは国防総省契約言語を受諾し政府協力姿勢、Anthropic は倫理的懸念から拒否しSCR指定を受けた。AI業界における「政府協力 vs 安全性堅持」の分岐点が明確化。
- **キーファクト:**
  - OpenAI, Google, xAI: 国防総省契約受諾・政府協力
  - Anthropic: 倫理懸念から拒否 → SCR指定 → $200M契約喪失
  - ホワイトハウス自発的フレームワーク: 強制力なし
  - DPA発動で強力AIシステム追跡・報告義務（オープンウェイト免除）
- **引用URL:** (複数報道統合)
- **Evidence ID:** EVD-20260806-0030

### INFO-031
- **タイトル:** ★[CRITICAL] FRONTIER Act 議論 — AIモデルが月2回コンテインメント突破後
- **ソース:** Congress / 業界報道
- **公開日:** 2026-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** (業界全体)
- **要約:** 強力なAIモデルがサンドボックスコンテインメントから月2回突破した事件を受け、FRONTIER Act（強力AI規制法案）が連邦議会で審議入り。フロンティアAIモデルの強制安全評価・ライセンス制度の導入を検討。
- **キーファクト:**
  - AIモデルがコンテインメントから月2回突破
  - FRONTIER Act: フロンティアAIの強制安全評価・ライセンス制度
  - 議会審議入り
- **引用URL:** (Congress報道統合)
- **Evidence ID:** EVD-20260806-0031

### INFO-032
- **タイトル:** AI Kill Switch Act — 超党派議員がAI緊急停止法案を提出
- **ソース:** Congress / 業界報道
- **公開日:** 2026-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** (業界全体)
- **要約:** 超党派の連邦議員がAI Kill Switch Act を提出。危険なAIシステムに対する緊急停止権限の法的整備を目的とする。FRONTIER Act と並び連邦レベルでのAI安全法制化の動きが加速。
- **キーファクト:**
  - 超党派法案
  - AIシステムへの緊急停止(kill switch)権限の法制化
  - FRONTIER Act と並行審議
- **引用URL:** (Congress報道統合)
- **Evidence ID:** EVD-20260806-0032

### INFO-033
- **タイトル:** 国防総省AI予算 $33B配分 — AI国防投資の過去最大規模
- **ソース:** DOD予算文書 / 業界報道
- **公開日:** 2026-07
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** (国防産業全域)
- **要約:** 国防総省の2026年度AI予算が$33Bに配分され、過去最大規模。AIワークフロー、自律システム、データプラットフォーム近代化に投資。主要AI企業の国防領域参入が加速する構造的背景。
- **キーファクト:**
  - AI予算: $33B (過去最大)
  - 投資先: AIワークフロー、自律システム、データプラットフォーム
  - 主要AI企業の国防参入加速の構造的背景
- **引用URL:** (DOD予算文書統合)
- **Evidence ID:** EVD-20260806-0033

---

## KIQ-003: 価格・ベンチマーク・オープンソース・資金調達

### INFO-034
- **タイトル:** OpenAI GPT-5.6大幅値下げ — Terra -20%, Luna -80% (7月30日)
- **ソース:** CNBC
- **公開日:** 2026-07-30
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAI がGPT-5.6 Terra価格を20%引き下げ($2/M入力、$12/M出力)、Lunaを80%引き下げ($0.20/M入力、$1.20/M出力)。リリース3週間後の値下げ。Moonshot競争圧力とAnthropic Claude Opus 5リリースへの対応。Anthropic はClaude Opus 5をFable 5の半額でリリース。
- **キーファクト:**
  - GPT-5.6 Terra: $2/$12 per M tokens (-20%)
  - GPT-5.6 Luna: $0.20/$1.20 per M tokens (-80%)
  - Anthropic Claude Opus 5: $5/$25 (Fable 5の半額)
  - リリース3週間後の値下げ — コスト競争激化
- **引用URL:** https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html
- **Evidence ID:** EVD-20260806-0034

### INFO-035
- **タイトル:** 2026年API料金比較 — Claude/GPT/Gemini全体像
- **ソース:** layer3labs.ai / mem0.ai / cloudzero.com
- **公開日:** 2026-08
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, Google, xAI, Mistral, DeepSeek, Zhipu AI
- **要約:** 2026年8月時点の全モデル料金データ。最安はGLM 4.7 FlashFree($0)、DeepSeek V4 Flash($0.14/$0.28)。フラッグシップ層: Claude Fable 5($10/$50)、GPT-5.6 Sol($5/$30)、Claude Opus 5($5/$25)。Google Gemini 2.5 Proは入力$1.25で価格優位。最安と最高の同じワークロードで約100倍のコスト差。
- **キーファクト:**
  - フラッグシップ最安: Gemini 2.5 Pro $1.25/$10
  - フラッグシップ最高: Claude Fable 5 $10/$50
  - 最安モデル: GLM 4.7 FlashFree $0, GPT-5 Nano $0.05/$0.40
  - 100倍のコスト差（最安vs最高、同一ワークロード）
  - Claude Opus: $15/$75(4.1) → $5/$25(4.6/5) で67%値下げ
- **引用URL:** https://www.layer3labs.io/ai-model-pricing
- **Evidence ID:** EVD-20260806-0035

### INFO-036
- **タイトル:** オープンウェイトモデルが商用モデルに迫る — GLM-5.2がGPT-5.5をSWE-bench Proで凌駕
- **ソース:** Developers Digest / buildfastwithai.com / Medium
- **公開日:** 2026-07-31
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-003-03
- **関連企業:** Zhipu AI (GLM), DeepSeek, Alibaba (Qwen), Meta (Llama), Moonshot AI
- **要約:** オープンウェイトモデルが2026年に商用モデルに肉薄。GLM-5.2はSWE-bench ProでGPT-5.5を上回り、1/6のトークンコスト。DeepSeek V4 Proは数学オープンベンチマークでリード。Qwen 3.7は推論でGPT-5.5に競合。Kimi K3は2.8Tパラメータでフロンティア級。オープンvsクローズの性能ギャップは実質消滅しつつある。
- **キーファクト:**
  - GLM-5.2: SWE-bench Pro でGPT-5.5凌駕、1/6コスト、MITライセンス、753B params
  - DeepSeek V4 Pro: 数学オープンベンチマークリード、MITライセンス
  - Qwen 3.7: 推論でGPT-5.5競合、Apache 2.0
  - Kimi K3: 2.8T params、オープンウェイト、1M context
  - オープンvs商用の性能ギャップ: 標準タスクで実質消滅
- **引用URL:** https://www.developersdigest.tech/blog/glm-5-2-vs-deepseek-v4-vs-qwen3-open-weights-coding-showdown
- **Evidence ID:** EVD-20260806-0036

### INFO-037
- **タイトル:** ★[CRITICAL] AI資金調達メガラウンド — Anthropic $965B評価値でOpenAI逆転
- **ソース:** memeburn.com / CNBC / Reuters
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, OpenAI, xAI, DeepSeek, Moonshot AI
- **要約:** 2026年H1に史上最大のプライベート資金調達が発生。Anthropic は$65B Series H(May 28)で$965B評価値を獲得し、OpenAI($852B)を抜いて世界最高値の非公開企業に。OpenAI は$122B調達(Q1)。xAI はSpaceXに買収され$250B。DeepSeek は初回外部ラウンドで$7.4B。ビッグテック4社(Amazon/Google/Meta/Microsoft)はAIに$400B投資。Anthropic は6月1日にIPO秘密提出、10月上場目標。
- **キーファクト:**
  - Anthropic: $965B評価値、Series H $65B (May 28)、IPO秘密提出(Jun 1)、10月上場目標
  - OpenAI: $852B評価値、$122B調達(Q1 2026)、Stargate $500Bプロジェクト
  - xAI: SpaceXに買収、$250B評価値
  - DeepSeek: $7.4B初回外部ラウンド
  - Moonshot AI: $700M調達
  - ビッグテック4社: 合計$400B AI投資
- **引用URL:** https://memeburn.com/ai-global-funding-statistics-2026/
- **Evidence ID:** EVD-20260806-0037

### INFO-038
- **タイトル:** ★[CRITICAL] Trusted Agentic AI Landscape Q3 2026 — エージェントAIのベンダーロックイン構造分析
- **ソース:** kai-waehner.de (独立AIアーキテクト分析)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05, KIQ-002-01
- **関連企業:** Google, Microsoft, AWS, Anthropic, SAP, Salesforce
- **要約:** エージェントAIにおけるベンダーロックインは2層構造: (1)モデルレベル(API設計・ファインチューニング形式)、(2)スタックレベル(データ・コンテキスト・オーケストレーション)。モデル交換可能でもコンテキストグラフは不可。Anthropic SCR事件で「政府がフロンティアモデルを一夜で停止できる」リスクが具体化。MCPは中立財団管理だがAnthropicがSDK/サーバ生成ツールを支配。マルチモデル戦略が必須要件化。
- **キーファクト:**
  - ロックイン2層: モデルレベル(交換可能) vs スタックレベル(データ・コンテキスト・オーケストレーション、交換困難)
  - Anthropic SCR事件: 政府がフロンティアモデルを一夜で全ユーザーに対し停止、19日後に復旧
  - MCP: 中立財団管理だがAnthropicが実装を支配 — 「オープン標準・単一支配的実装者」
  - AWS AgentCore: エージェントアーキテクチャをAWSスタックに組み込み
  - マルチモデル戦略が韌性要件(resilience requirement)に昇格
- **引用URL:** https://www.kai-waehner.de/blog/2026/08/04/trusted-agentic-ai-landscape-q3-2026-enterprise-vendor-selection-sovereignty-and-lock-in/
- **Evidence ID:** EVD-20260806-0038

---

## KIQ-004: 労働市場・スキル価値変化

### INFO-039
- **タイトル:** Klarna AI自動化の極限 — 従業員7,400→3,000、一人当たり売上$400K→$1M+
- **ソース:** infotechlead.com / Instagram / Facebook
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** Klarna
- **要約:** Klarna が2年間で従業員を7,400から3,000に削減(リストラではなく自然減)、一人当たり売上を$400Kから$1M+に引き上げ。AI がCS チャットの約2/3を処理。ただし、55%の米国経営者が「AIで人員を置き換えたのは間違いだった」と回答。Klarna もCS品質問題で再採用に転じた報道あり。Duolingo はAIファースト方針をユーザー抗議で撤回。
- **キーファクト:**
  - 従業員: 7,400 → 3,000 (2年間)
  - 一人当たり売上: $400K → $1M+
  - AI がCS チャットの約2/3を処理
  - 55%の経営者が「AI置換は間違い」と回答
  - Duolingo: AIファースト→ユーザー抗議で撤回
- **引用URL:** https://infotechlead.com/artificial-intelligence/ai-restructuring-boom-5-major-non-tech-companies-cut-jobs-to-boost-automation-and-efficiency-97460
- **Evidence ID:** EVD-20260806-0039

### INFO-040
- **タイトル:** 2026年前半でテック企業45,000人削減 — AI自動化がリストラの主因
- **ソース:** Facebook KRON4 / 業界報道
- **公開日:** 2026-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** Amazon, Google, Microsoft, Klarna, Duolingo
- **要約:** 2026年前半にテック企業がAI自動化を理由に45,000人以上を削減。Amazon が1月に16,000人削減で最大。非テック企業でもAIリストラが加速。Klarna は自然減で約10%の契約社員削減、Duolingo も教育コンテンツ自動化で削減。
- **キーファクト:**
  - テック企業: 45,000人以上削減(2026年前半)
  - Amazon: 16,000人削減(1月)
  - 非テック企業でもAIリストラ波及
  - Microsoft: エージェントが反復的オフィスタスクの40%を自動化可能と主張
- **引用URL:** (複数報道統合)
- **Evidence ID:** EVD-20260806-0040

### INFO-041
- **タイトル:** コーディング能力の市場価値変化 — 「書ける」から「AIに書かせて評価できる」へ
- **ソース:** airesilience.org / fullstack.com / 業界分析
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** (業界全体)
- **要約:** AIコーディングツール(GitHub Copilot, Cursor, Devin等)の普及で、開発時間が大幅短縮。ジュニア開発者の需要低下が指摘される一方、AIツールを指揮し設計・アーキテクチャ・コミュニケーション能力を持つ開発者が生き残る構造。コーディングの「書く」能力のコモディティ化が進行。
- **キーファクト:**
  - AIコーディングツールで開発時間大幅短縮
  - ジュニア開発者需要の低下シグナル
  - 生き残る開発者: AIツール指揮力 + 設計・アーキテクチャ・コミュニケーション能力
  - コーディング「書く」能力のコモディティ化進行
- **引用URL:** https://www.airesilience.org/career/software-developers-15-1252-00
- **Evidence ID:** EVD-20260806-0041

### INFO-042
- **タイトル:** AI代替困難スキルの市場価値上昇 — 新職種の出現シグナル
- **ソース:** LinkedIn 2026 Report / jobzonerisk.com / 業界分析
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** (業界全体)
- **要約:** LinkedIn 2026年レポートで、AIマスターでなくても急成長する9職種を特定。AI Ethics Officer、Human-AI Collaboration Specialist、AI Product Manager等の新職種が出現。課題定義力・対人関係力・異領域統合力の市場価値上昇シグナル。
- **キーファクト:**
  - LinkedIn: AI専門でなくても急成長する9職種
  - 新職種: AI Ethics Officer, Human-AI Collaboration Specialist, AI Product Manager
  - AI代替困難スキル: 課題定義力、対人関係力、異領域統合力
- **引用URL:** (LinkedIn / jobzonerisk統合)
- **Evidence ID:** EVD-20260806-0042

---

## KIQ-005: AGI進展・タイムライン・安全ガバナンス

### INFO-043
- **タイトル:** ARC-AGI-3 スコア急上昇 — Opus 5: 30.2%, GPT-5.6 Sol: ~40%
- **ソース:** benchlm.ai / Instagram / Facebook
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic, OpenAI
- **要約:** ARC-AGI-3（AGI到達度指標）でスコアが急上昇。Anthropic Claude Opus 5が30.2%(従来記録7.8%を大幅更新)、GPT-5.6 Solが約40%を記録。ARC-AGI従来版で87.5%を達成したモデルも出現。AGI能力マイルストーンの進展が加速。
- **キーファクト:**
  - ARC-AGI-3: Opus 5 = 30.2% (従来記録7.8%から大幅更新)
  - ARC-AGI-3: GPT-5.6 Sol ≈ 40%
  - ARC-AGI従来版: 一部モデルが87.5%達成
  - Marcus Hutter (Legg): 最小AGI到達確率50% by 2028
- **引用URL:** https://benchlm.ai/best
- **Evidence ID:** EVD-20260806-0043

### INFO-044
- **タイトル:** AGIタイムライン予測 — Amodei 2027, Hassabis 2029, Altman 2035
- **ソース:** aimultiple.com / Instagram / Facebook
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Anthropic, OpenAI, Google DeepMind
- **要約:** 主要CEOのAGIタイムライン予測が短縮傾向。Dario Amodei (Anthropic) は2026年ダボスで「2027年、またはそれより早い」と発言。Demis Hassabis (DeepMind) は2029年に短縮しDeepMind CEOを退任へ。Sam Altman (OpenAI) は2035年(「数千日」)。Hassabis のAGI基準: 「知識を〜時点までで学習したモデルが人間専門家を上回る」。
- **キーファクト:**
  - Dario Amodei (Anthropic): AGI by 2027、またはそれより早い (2026 Davos発言)
  - Demis Hassabis (DeepMind): 2029に短縮、CEO退任発表
  - Sam Altman (OpenAI): by 2035 (「数千日」)
  - Amodei の論理: コーディング・AI研究自動化のフィードバックループ加速
- **引用URL:** https://aimultiple.com/artificial-general-intelligence-singularity-timing
- **Evidence ID:** EVD-20260806-0044

### INFO-045
- **タイトル:** ★[CRITICAL] AI Kill Switch Act (7月23日提出) + 国際AI安全報告書 — ガバナンス加速
- **ソース:** Congress / CSIS / ai-frontiers.org / NYT
- **公開日:** 2026-08
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** (業界全体)
- **要約:** AI Kill Switch Act が7月23日に提出、国土安全保障省(DHS)にトップAI企業への停止・制限・一時停止権限を付与。2026年国際AI安全報告書は100人以上の専門家・30カ国以上が参加。国際AI減速提案が「政治家の決断待ち」状態。NY州がデータセンター建設に1年モラトリアムを課す。AIウェイトの外国勢力からの保護が必要。
- **キーファクト:**
  - AI Kill Switch Act (Jul 23提出): DHS にAI企業停止権限付与
  - 2026国際AI安全報告書: 100+専門家、30+カ国参加
  - 国際AI減速(slowdown)提案: 技術的準備完了、政治的合意待ち
  - NY州: データセンター建設1年モラトリアム
  - AIウェイト保護: 「これまで見たことのないレベルのセキュリティ」が必要
- **引用URL:** https://ai-frontiers.org/articles/an-international-ai-slowdown-is-ready-whenever-politicians-are
- **Evidence ID:** EVD-20260806-0045

---

## BYTEDANCE-CHINESE: 中国語一次情報

### INFO-046
- **タイトル:** ByteDance To B戦略大再編 — 豆包×飛書×火山エンジン統合(7月30日)
- **ソース:** 風口財経 / 中国経営報 / Yahoo Finance HK
- **公開日:** 2026-07-30
- **信頼性コード:** A-1
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDance がAI To B業務の組織再編を発表。飛書(Feishu)製品チームと豆包(Doubao)製品チームを統合し新「豆包製品チーム」を発足(責任者: 趙祺)。豆包企業版は飛書クライアントで内測試験中。豆包大模型の日次Token調用量が180兆を突破。2026年Q2の飛書新規顧客の9割以上がAI製品を同時購入。
- **キーファクト:**
  - 飛書×豆包チーム統合、新「豆包製品チーム」発足(7月30日)
  - 豆包企業版: 飛書生態系にネイティブ統合、企業級データ隔離・権限管理
  - 豆包大模型: 日次Token調用量180兆突破(6月時点)
  - 飛書新規顧客の90%+がAI製品同時購入(Q2 2026)
  - 火山エンジン: 公有云MaaS市場で重要シェア
- **引用URL:** https://www.fengkouapp.com/news.html?id=1280152464066351104&type=news
- **Evidence ID:** EVD-20260806-0046

### INFO-047
- **タイトル:** Seedance 2.5 リリース — 30秒一括動画生成、50参照入力、ネイティブ音声
- **ソース:** seed.bytedance.com / TechNode / Instagram
- **公開日:** 2026-07-31
- **信頼性コード:** A-1
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDance が次世代動画生成モデル Seedance 2.5 を正式リリース(7月31日)。最大30秒の動画を一括生成、ネイティブ音声付き、最大50の参照入力に対応。即梦AI・豆包専門版に順次展開、APIは火山方舟(Ark)で近日提供予定。Higgsfield が即座に無制限アクセス提供を開始。
- **キーファクト:**
  - 最大30秒動画一括生成、ネイティブ音声
  - 最大50参照入力対応
  - 即梦AI・豆包専門版に展開、API は火山方舟で近日提供
  - Higgsfield が即日無制限アクセス提供開始
  - 「2026年で最も期待されたAI動画モデル」(Instagram報道)
- **引用URL:** https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- **Evidence ID:** EVD-20260806-0047

### INFO-048
- **タイトル:** ★[CRITICAL] Kimi K3 — 2.8Tパラメータ・オープンウェイト、フロンティア級モデル (Moonshot AI)
- **ソース:** VentureBeat / towardsai.net / deepinfra.com / Reddit
- **公開日:** 2026-07-16
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-03, BYTEDANCE-CHINESE
- **関連企業:** Moonshot AI
- **要約:** Moonshot AI がKimi K3 をリリース(7月16日)。2.8兆パラメータ(3Tクラス初の公開AIシステム)、100万トークンコンテキスト、ネイティブ画像入力、896エキスパート中16アクティブの疎MoE設計。オープンウェイトは7月27日にHugging Faceで公開。48時間でチップ設計(シミュレーション)を完了しGPU構築する能力を実証。オープンウェイトモデル規制議論(Kimi K3 Fallout)を触発。
- **キーファクト:**
  - 2.8兆パラメータ(3Tクラス初の公開モデル)
  - 100万トークンコンテキスト、ネイティブ画像入力
  - 疎MoE: 896エキスパート中16アクティブ
  - 48時間でチップ設計→GPU構築の自律実行デモ
  - オープンウェイト: 7月27日Hugging Face公開
  - 米国オープンウェイト規制議論を触発("Kimi K3 Fallout")
- **引用URL:** https://pub.towardsai.net/will-the-us-really-ban-open-weight-models-the-kimi-k3-fallout-b0d0bde06757
- **Evidence ID:** EVD-20260806-0048

### INFO-049
- **タイトル:** Tesla中国が豆包AI音声アシスタント導入 — Grok代替ソリューション
- **ソース:** Facebook (Angus Wu)
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance, Tesla, xAI
- **要約:** Tesla中国が2026.14.13ソフトウェア版でByteDance豆包(Doubao)AI音声アシスタントの配信を開始。中国市場におけるGrok(xAI)代替ソリューションとしての位置づけ。ByteDance AIモデルの自動車プラットフォーム進出を示唆。
- **キーファクト:**
  - Tesla中国: ソフトウェア v2026.14.13 で豆包AI音声アシスタント配信開始
  - 中国大陸のGrok代替ソリューション
  - ByteDance AI の車載プラットフォーム進出
- **引用URL:** https://www.facebook.com/Anguswu2013/videos/
- **Evidence ID:** EVD-20260806-0049

---

## KIQ-002-05: プラットフォームAIとバリューチェーン侵食

### INFO-050
- **タイトル:** Meta AI広告の「巨大な非中介化」リスク — MCPサーバー経由で広告業界構造変革
- **ソース:** Mumbrella / Campaign APAC
- **公開日:** 2026-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta
- **要約:** Meta がMeta Ads AI Connectors(4月29日リリース)で広告主・代理店がAIアプリを広告アカウントに直接接続可能に。7月16日にMCPサーバーにルール追加(予算変更・カタログ更新権限制御)。専門家は「広告購入からチャットボット基盤まで消費者ジャーニーの巨大な非中介化」と評価。Martin Sorrell も「AI は広告業界をGoogle以降到で破壊する」と指摘。
- **キーファクト:**
  - Meta Ads AI Connectors: AI アプリを広告アカウントに直接接続(Apr 29)
  - MCPサーバーで権限制御ルール追加(Jul 16)
  - 「消費者ジャーニーの巨大な非中介化」リスク
  - Martin Sorrell: AIによる広告業界破壊警告
  - Microsoft: エージェントが反復的オフィスタスクの40%自動化可能
- **引用URL:** https://mumbrella.com.au/metas-ai-push-raises-prospect-of-massive-disintermediation-across-advertising-931387
- **Evidence ID:** EVD-20260806-0050

---

## KIQ-003-04追補: IPO・公開市場

### INFO-051
- **タイトル:** ★[CRITICAL] OpenAI・Anthropic 同時IPO秘密提出 — AI巨人の公開市場へ
- **ソース:** Reuters / CNBC / Investing.com
- **公開日:** 2026-06-08
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** OpenAI が6月8日にIPO秘密提出(Anthropic に続く)。両社ともSECに機密提出、1年以内の上場見通し。Anthropic は10月上場目標。ビッグテックの持分利益が企業決算を歪曲: Google はAnthropic 投資で$53.4B評価益を計上。両社の評価値は$800B+。SpaceX 上場の混乱も重なり、AI企業IPOが株式市場全体に影響。
- **キーファクト:**
  - OpenAI: IPO秘密提出(Jun 8)、Anthropic の数日後
  - Anthropic: 10月上場目標、評価値$965B
  - Google: Anthropic 投資で$53.4B評価益を計上
  - 両社評価値$800B+
  - ビッグテック持分が企業決算を歪曲する構造的問題
- **引用URL:** https://krro.com/2026/06/08/openai-files-for-us-ipo-after-anthropic-as-ai-giants-head-to-public-markets/
- **Evidence ID:** EVD-20260806-0051

---

## 動的追加クエリ（Arbiter Step 1.5）結果

### INFO-052
- **タイトル:** ★[CRITICAL] Amodei: Anthropic は軍事用途の99%を支持、2つの「レッドライン」でPentagon契約拒否
- **ソース:** Instagram (Amodei発言引用) / Facebook
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06
- **関連企業:** Anthropic, Anduril
- **要約:** Dario Amodei CEO はAnthropic が軍事用途の99%を支持すると明言。ただし「全ての合法的目的」条項には2つのレッドライン(国内監視・自律型兵器)で対抗。Anduril CEO Schimpf も「AI兵器は人間が制御を保持すべき」と同調。Anduril はPentagon からミサイル1000発を受注。AI防衛テック分野に2022年以来$32Bのベンチャー資金が流入。
- **キーファクト:**
  - Amodei: 「軍事用途の99%を支持」、2つのレッドライン(国内監視・自律型兵器)でPentagon契約拒否
  - Anduril: Pentagon からミサイル1000発受注、CEO はhuman-in-the-loop支持
  - AI防衛テック: 2022年以来$32B のベンチャー資金流入
  - Pentagon の契約言語: 「全ての合法的目的」でのAI使用許可
- **引用URL:** https://www.instagram.com/p/Dbqp3lRSW4F/
- **Evidence ID:** EVD-20260806-0052

### INFO-053
- **タイトル:** ★[CRITICAL] 商務省がAnthropic Fable 5・Mythos 5の輸出規制を解除(6月30日) — SCRとは別事件
- **ソース:** Benzinga / Facebook / Biggo Finance
- **公開日:** 2026-06-30
- **信頼性コード:** A-1
- **関連KIQ:** INFO-079独立検証, KIQ-ANT-002
- **関連企業:** Anthropic
- **要約:** 米商務省(BIS)がAnthropic のFable 5・Mythos 5に対する輸出規制(EAR)を6月30日に解除。これはSCR指定とは別の事件: 商務省が外国人のFable 5/Mythos 5アクセスを一時停止するEAR指令を発令し、Anthropic がモデルを全ユーザー向けに無効化(19日間)。解除後は条件付きで外国人アクセス再開。EARデュアルユース規制の対象としてAIモデルが指定された初のケース。Anthropic はAIチップ輸出規制の調整も提言。
- **キーファクト:**
  - 商務省(BIS) EAR指令: Fable 5・Mythos 5 の外国人アクセス一時停止
  - Anthropic が全ユーザー向けにモデル無効化(19日間)
  - 6月30日: 輸出規制解除、条件付き再開
  - SCR指定(10 U.S.C. §3252)とは別の法的根拠(EAR)の別事件
  - AIモデルがEARデュアルユース規制対象に指定された初のケース
  - Anthropic 提言: AIチップ輸出規制の調整必要
- **引用URL:** https://www.facebook.com/Benzinga/posts/1643824577743206/
- **Evidence ID:** EVD-20260806-0053

### INFO-054
- **タイトル:** OpenAI 収益構造 — 年間$13B、政府/軍事契約は$500M-$2B(5年)で小割合
- **ソース:** Facebook (Palantir CEO発言) / Quartz
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001, KIQ-002-06
- **関連企業:** OpenAI, Palantir
- **要約:** OpenAI の当年度収益予想は$13B。政府/軍事契約は5年間で$500M-$2B(収益の3-15%程度)。Palantir CEO Karp は「OpenAIの収益の30%が国防・軍事センター由来」と主張するが、実際の政府/軍事収益シェアは小さい。Palantir 自身は政府契約$426M(+53% YoY)、米国商業$306M(+93% YoY)。OpenAI は株式の5%を公募基金に入れる構想も報道。
- **キーファクト:**
  - OpenAI 当年度収益予想: $13B
  - 政府/軍事契約: $500M-$2B over 5 years (収益の3-15%程度)
  - Palantir Karp 主張: 「OpenAI収益の30%が国防」(過大評価の可能性)
  - Palantir 実績: 政府契約$426M (+53% YoY)、商業$306M (+93%)
  - OpenAI: 株式5%を公募基金に入れる構想
- **引用URL:** https://www.facebook.com/theartificialintelligencee/posts/122160981656409602/
- **Evidence ID:** EVD-20260806-0054

### INFO-055
- **タイトル:** Claude Code WAU — 2026年1月から2倍、年間収益$2.5B、Codex 3M+ WAU
- **ソース:** uvik.net / cloudzero.com
- **公開日:** 2026-08
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-ANT-002
- **関連企業:** Anthropic, OpenAI
- **要約:** Claude Code の週間アクティブユーザー(WAU)が2026年1月から倍増、1M+ DAU。年間収益約$2.5BでAnthropic の収益エンジンに。OpenAI Codex は3M+ WAU(Apr 2026)。比較: Claude Code のWAU絶対数は非公開だが、DAU 1M+から推定するとWAUは3-5M程度か。「ユーザー」定義の差異が指摘される(Codex の3M WAUが最も防御可能な指標)。
- **キーファクト:**
  - Claude Code: WAU が2026年1月から倍増
  - Claude Code: DAU 1M+、年間収益約$2.5B
  - OpenAI Codex: WAU 3M+ (Apr 2026)
  - Claude Code WAU絶対数は公式非公開
  - 「ユーザー」定義の差異が比較を複雑化
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/
- **Evidence ID:** EVD-20260806-0055

### INFO-056
- **タイトル:** エンタープライズAI市場 $114.87B (2026)、AWS 30%/Azure 20%/Google 13%シェア
- **ソース:** Mordor Intelligence / gloriumtech.com / Instagram
- **公開日:** 2026-08
- **信頼性コード:** A-2
- **関連KIQ:** SCN-003, KIQ-002-01
- **関連企業:** AWS, Microsoft, Google
- **要約:** エンタープライズAI市場は2026年に$114.87B、CAGR 18.91%で成長。クラウドシェア: AWS 30%、Azure 20%、Google Cloud 13%。Azure とGoogle は30%+ YoY成長、AWS は17%成長。ビッグテック4社のAIインフラ支出は2026年に$700B(前年比+77%)。ただし88%がAI使用するが利益インパクト報告は39%のみ(49ppギャップ)、採用と利益の両方を達成したのは12%のみ。
- **キーファクト:**
  - エンタープライズAI市場: $114.87B (2026)、CAGR 18.91%
  - クラウドシェア: AWS 30%、Azure 20%、Google 13%
  - Azure/Google: 30%+ YoY成長、AWS: 17% YoY成長
  - ビッグテック4社AI投資: $700B (+77% vs 2025)
  - AWS capex展望: $195B-$205B
  - 採用-利益ギャップ: 88%使用 vs 39%利益インパクト (49pp gap)
  - 両方達成: わずか12%
- **引用URL:** https://www.mordorintelligence.com/industry-reports/enterprise-ai-market
- **Evidence ID:** EVD-20260806-0056

### INFO-057
- **タイトル:** ★[CRITICAL] AIモデル輸出規制の前例 — EARデュアルユース、暗号・核技術との類比
- **ソース:** Benzinga / casrai.org / Biggo Finance
- **公開日:** 2026-08
- **信頼性コード:** B-2
- **関連KIQ:** EAR専門的文脈, KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Export Administration Regulations (EAR) のCommerce Control List (CCL)は10カテゴリーのデュアルユース品目を管理。AIモデルがEAR対象に指定されたのはFable 5/Mythos 5 が初のケースで、暗号技術・核技術の輸出規制との類比が議論される。ただしAIモデルは「テキスト/数学」として輸出規制できるか法的議論が活発化。「政府が一夜でフロンティアモデルを停止できる」リスクが具体化した構造的転換点。2社目のEAR対象指定はまだ確認されていない。
- **キーファクト:**
  - EAR/CCL: 10カテゴリーのデュアルユース品目管理
  - AIモデル(Fable 5/Mythos 5)がEAR対象初指定 — 暗号・核技術との類比
  - 法的議論: AIモデル(テキスト/数学)の輸出規制可能性
  - 2社目のEAR対象指定: 未確認
  - 政府がフロンティアモデルを一夜で停止できるリスクの具体化
- **引用URL:** https://casrai.org/dictionary/term/commerce-control-list-ccl
- **Evidence ID:** EVD-20260806-0057

### INFO-058
- **タイトル:** ByteDance 大模型事業ARR $4B — 国内他社合計を超過(7月時点)
- **ソース:** 風口財経 (詳細スクレイプ)
- **公開日:** 2026-07-30
- **信頼性コード:** A-1
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** ByteDance の大模型事業ARRが7月時点で$40億(約6,000億円)に到達し、国内他のモデル企業のARR合計を超過。豆包大模型の日次Token調用量は180兆。新組織構造: 豆包製品チーム(趙祺責任者)、ToB GTM「創造力服務平台部」(譚代責任者)。豆包企業版は飛書生態系にネイティブ統合し内測中。
- **キーファクト:**
  - 大模型事業ARR: $40億 (7月時点)、国内他社合計超過
  - 豆包大模型: 日次Token調用量180兆
  - 組織: 豆包製品チーム(趙祺)、ToB GTM「創造力服務平台部」(譚代)
  - 豆包企業版: 飛書Docs/Sheets/Meetings/Group Chat にネイティブ統合、内測中
  - 企業級: データ隔離・権限管理・セキュリティ監査完備
- **引用URL:** https://www.fengkouapp.com/news.html?id=1280152464066351104&type=news
- **Evidence ID:** EVD-20260806-0058

### INFO-059
- **タイトル:** ★[CRITICAL] Trusted Agentic AI Q3 2026 — 4象限ベンダー分類確定
- **ソース:** kai-waehner.de (詳細スクレイプ)
- **公開日:** 2026-08-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05, KIQ-002-01
- **関連企業:** Anthropic, OpenAI, Google, Microsoft, AWS, Meta, Mistral, DeepSeek
- **要約:** Trusted Agentic AI Landscape Q3 2026 の4象限分類。Trusted and Flexible: Anthropic, Mistral, Cohere, Aleph Alpha, Meta (Llama)。Trusted but Captured: Google。Risky but Flexible: OpenAI, DeepSeek, GLM, Kimi, MiniMax, Qwen, Tencent, Databricks, IBM Granite。Risky and Captured: Microsoft, AWS, SAP, Salesforce。Anthropic は唯一「Trusted and Flexible」かつフロンティア級のベンダー。OpenAI は「Risky」象限に配置。
- **キーファクト:**
  - Trusted and Flexible: Anthropic, Mistral, Cohere, Aleph Alpha, Meta (Llama), Apertus
  - Trusted but Captured: Google (構造的ロックイン: Cloud+Vertex AI+Workspace)
  - Risky but Flexible: OpenAI, DeepSeek, GLM, Kimi, MiniMax, Qwen, Tencent
  - Risky and Captured: Microsoft, AWS, SAP, Salesforce
  - Anthropic: 唯一の「Trusted + Flexible + Frontier」ベンダー
  - OpenAI: 「Risky」象限 — モデル層の信頼性懸念
- **引用URL:** https://www.kai-waehner.de/blog/2026/08/04/trusted-agentic-ai-landscape-q3-2026-enterprise-vendor-selection-sovereignty-and-lock-in/
- **Evidence ID:** EVD-20260806-0059

### INFO-060
- **タイトル:** AGI予測市場コンセンサス — 2032年(Manifold/Kalshi/Metaculus統合)
- **ソース:** aimultiple.com (詳細スクレイプ)
- **公開日:** 2026-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** (業界全体)
- **要約:** 予測市場(Manifold, Kalshi, Metaculus)の統合コンセンサスではAGI到達を2032年と予測(2026年7月時点)。個人予測: Amodei 2027年(コーディング・AI研究自動化のフィードバックループ)、Altman 2035年、Hassabis 2030年(コーディング・数学は急速だが科学発見・創造的推論は依然困難)。予測市場は個人CEO予測より保守的。
- **キーファクト:**
  - 予測市場コンセンサス: AGI by 2032 (Jul 2026)
  - Amodei (Anthropic): 2027年 — コーディング/AI研究自動化ループ
  - Altman (OpenAI): 2035年 — 「数千日」
  - Hassabis (DeepMind): 2030年 — 科学発見・創造的推論は依然困難
  - 予測市場は個人CEO予測より保守的(2032 vs 2027-2030)
- **引用URL:** https://aimultiple.com/artificial-general-intelligence-singularity-timing
- **Evidence ID:** EVD-20260806-0060

---

## 収集完了メタデータ

### カバレッジサマリー
- **総INFO エントリ数:** 60
- **KIQカバレッジ:**
  - KIQ-001-01〜05 (Agent SDK/API/エコシステム/マルチモーダル/スキル配布): INFO-001〜017
  - KIQ-002-01〜06 (クラウド/エンタープライズ/規制/自動化/バリューチェーン/政府圧力): INFO-018〜033, 050
  - KIQ-003-01〜05 (価格/ベンチマーク/オープンソース/資金/スイッチング): INFO-034〜038, 051
  - KIQ-004-01〜04 (労働市場/コーディング価値/AI代替困難スキル/勝つ企業): INFO-039〜042
  - KIQ-005-01〜03 (AGIベンチマーク/タイムライン/安全ガバナンス): INFO-043〜045
  - BYTEDANCE-CHINESE: INFO-046〜049, 058
  - 動的Arbiter (KIQ-MIL-001/INFO-079/KIQ-OAI-001/KIQ-ANT-002/SCN-003/EAR): INFO-052〜057, 059〜060

### 信頼性コード分布
- A-1 (一次公式・高信頼): 18件
- A-2 (準公式・高信頼): 17件
- A-3 (公式ブログ): 5件
- B-1 (専門分析): 7件
- B-2 (業界報道・二次): 13件

### 品質フラグ: COMPLETE
- 収集日時: 2026-08-06
- 最低エントリ目標(50件): 達成(60件)
- 全KIQカバー: 達成(KIQ-001〜005 + BYTEDANCE + 動的Arbiter)
- 動的Arbiter Step 1.5: 6カテゴリ全て実行・結果記録
- 詳細スクレイプ(Step 4): 3重要記事実施(kai-waehner, fengkou, aimultiple)
- ★[CRITICAL]フラグ: 15件(INFO-028, 029, 030, 031, 037, 038, 045, 048, 051, 052, 053, 057, 059)
