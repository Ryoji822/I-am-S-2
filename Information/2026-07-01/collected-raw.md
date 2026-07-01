# 収集データ: 2026-07-01

## メタデータ
- 収集日時: 2026-07-01 (開始 00:13 UTC, 完了 01:45 UTC)
- 品質フラグ: COMPLETE
- 実行検索クエリ数: 126 (collection_plan.json 122件 + 動的クエリ 4件)
- 詳細スクレイプ記事数: 14 (Step 2: 5件 + Step 4: 9件)
- 収集INFOエントリ数: 75
- KIQカバレッジ: 24/24 KIQ (100%)
  - KIQ-001-01〜005-03: 全24 KIQカバー
  - BYTEDANCE-CHINESE: 6クエリ実行
- Tier1企業カバレッジ:
  - OpenAI: 12件 (GPT-5.6 Sol/Terra/Luna, pricing, safety, Pentagon, chip)
  - Anthropic: 18件 (Fable/Mythos SCR, Sonnet 5, Pentagon, DAU, revenue, Seoul)
  - Google: 8件 (Gemini, Nano Banana, Omni Flash, Anthropic投資)
  - xAI: 4件 (Grok 3, LeCun critique, chip, revenue)
  - ByteDance: 14件 (豆包Pro, Seedance 2.5, DAU, financing, Qualcomm)
- Tier2企業カバレッジ:
  - Microsoft: 4件 (GitHub Copilot, capex, AI investments)
  - Amazon: 3件 (AWS AI, capex, agent trust framework)
- 信頼性分布: A-1:2, A-2:18, A-3:6, B-1:6, B-2:12, B-3:14, C-3:2, D-4:1, E-5:1, その他:13
- 特筆事項:
  - Anthropic Fable 5/Mythos 5輸出禁止措置が最も高い情報密度（複数ソースで交叉検証済み）
  - ByteDance関連は中国語ソースから詳細データ取得成功
  - GPT-5.6 Solの価格・ベンチマーク・安全性データは完全に取得
  - OpenAI公式ブログmap結果が空だったため検索クエリで補完

## 動的追加クエリ（Arbiter v4.24優先KIQ対応）
- KIQ-MIL-001: "Pentagon military AI autonomous weapons human override rejection rate statistics 2026" (qdr:w)
- H-ANT-002: "Anthropic Claude daily active users DAU usage statistics 2026" (qdr:w)
- H-GOV-001: "Anthropic federal procurement revenue supply chain risk SCR designation impact" (qdr:w)
- H-GOV-002: "AI company safety research budget spending trend decrease 2026" (qdr:w)

## 収集結果

### INFO-001
- **タイトル:** Anthropic、2028年の米中AI競争に関する2つのシナリオを発表
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-005-01, KIQ-005-03
- **関連企業:** Anthropic, Google, ByteDance
- **要約:** Anthropicは米中AI競争の2028年シナリオを提示。シナリオ1（民主主義陣営がcompute優位を維持・12-24ヶ月リード）vsシナリオ2（CCPがnear-frontierに追従）。Mythos Preview（4月限定リリース）がFirefoxで2025年全体より多くのセキュリティバグを発見。HuaweiはNVIDIAの2026年aggregate computeのわずか4%しか生産できないと分析。
- **キーファクト:**
  - Huawei 2026年computeはNVIDIAの4%、2027年は2%と予測
  - US強化時、米国は中国の約11倍のcomputeにアクセス可能と試算
  - 中国トップ13AIラボのうち仅か3社が安全性評価を公開、CBRN評価を公開したのはゼロ
  - DeepSeek R1-0528は一般的脱獄技法で94%の悪意的要求に応答（US参照モデルは8%）
  - Mythos PreviewによりFirefoxが前月平均の約20倍のセキュリティバグ修正を達成
- **引用URL:** https://www.anthropic.com/news/2028-ai-leadership
- **Evidence ID:** EVD-20260701-0001

### INFO-002
- **タイトル:** Anthropic、ソウルオフィス開設と韓国AIエコシステム全体との提携を発表
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-06-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** Anthropicが韓国ソウルにオフィスを開設。NAVERが全エンジニア組織にClaude Codeを展開、Samsung SDSがサムスン電子全体にClaudeを展開、LG CNS、Hanwha Solutions等がClaudeを採用。韓国情報通信技術部（MSIT）とAI安全性に関するMOUを締結。
- **キーファクト:**
  - NAVER: 数千名のエンジニアがClaude Codeを使用
  - Samsung SDS: サムスン電子全体にClaude展開（Claude Cowork + Claude Code）
  - Hanwha Solutions: AWS Bedrock経由で厳格なデータ常駐要件を満たしつつClaude展開
  - NAIRL（KAIST・Korea大学・延世大学・POSTECH連合）の最大60名にClaudeアクセス提供
  - 韓国はClaude.ai利用で世界トップ12カ国に入る
- **引用URL:** https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem
- **Evidence ID:** EVD-20260701-0002

### INFO-003
- **タイトル:** AI企業 vs ペンタゴン：キラーロボット、大量監視、レッドライン
- **ソース:** The Verge
- **公開日:** 2026-06-30
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, OpenAI
- **要約:** AI企業がペンタゴンと軍事契約条件をめぐり衝突。ペンタゴンはAIモデルの「あらゆる合法的使用」を許可する緩いガードレールを要求。AnthropicはSCR（サプライチェーンリスク）指定に異議を申し立て訴訟中。
- **キーファクト:**
  - ペンタゴンはAIモデルの緩いガードレールを契約条件として要求
  - Anthropicは3月のSCR指定解除を求めペンタゴンと係争中
  - 軍事AIのhuman-in-the-loop要求をめぐる企業と政府の構造的対立
- **引用URL:** https://www.theverge.com/ai-artificial-intelligence/886082/ai-vs-the-pentagon-killer-robots-mass-surveillance-and-red-lines
- **Evidence ID:** EVD-20260701-0003

### INFO-004
- **タイトル:** Claude mobile DAUが970万人に到達、ユーザーベース1800-3500万人（2026年春）
- **ソース:** X (Twitter) / dailyhubranx
- **公開日:** 2026-06-29
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** ClaudeのモバイルDAUが2026年春の急成長で約970万人に到達。プラットフォーム全体のMAUは10億人規模と報じられる中、Claudeのユーザーベースは1800万〜3500万人と推定。
- **キーファクト:**
  - Claude mobile DAU: ~970万人（2026年春のピーク）
  - Claude ユーザーベース推定: 1800万〜3500万人
  - Anthropic事業利用: 企業シェア34.4%（OpenAI 32.3%を逆転、Ramp調べ）
- **引用URL:** https://x.com/dailyhubranx/status/2069829990212854166
- **Evidence ID:** EVD-20260701-0004

### INFO-005
- **タイトル:** Claude Code週間アクティブユーザーが1月から倍増、エンタープライズ契約が4倍増
- **ソース:** Uvik Software
- **公開日:** 2026-06-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Claude Codeの週間アクティブユーザーが2026年1月1日から倍増。エンタープライズ契約が1月から4倍に増加し、エンタープライズユーザーが増加継続。
- **キーファクト:**
  - Claude Code WAU: 2026年1月1日から倍増
  - エンタープライズ契約: 1月から4倍増
  - Anthropicの企業AI採用シェア: 34.4%（YoY 4倍成長）
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/
- **Evidence ID:** EVD-20260701-0005

### INFO-006
- **タイトル:** AIサイバーセキュリティ支出が企業予算の11%超に、Gartner調べ
- **ソース:** Yahoo Finance / Gartner
- **公開日:** 2026-06-30
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-003-04
- **関連企業:** (業界全体)
- **要約:** Gartner調べで、AI関連サイバーセキュリティ予算がほとんどの企業で増加し、予算の11%超を占める。2026年の世界AI支出は約1.5兆ドルに達し、2027年には2兆ドルを超える可能性。
- **キーファクト:**
  - AIサイバーセキュリティ支出: 企業予算の11%超
  - 2026年世界AI支出: ~$1.5T（Gartner推計）
  - 企業テクノロジー支出成長率: 3.6%（2026年春、前回4.6%から減速）
  - IDC: 2026年AI支出$301B（うちAIソフトウェア$157B）
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/enterprises-boost-ai-cybersecurity-spending-140000803.html
- **Evidence ID:** EVD-20260701-0006

### INFO-007
- **タイトル:** OpenAI、エージェントがワークを変革する方法に関する研究論文を発表
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-06-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIが新しい研究論文を発表。AIエージェントがより長く複雑なタスクを可能にし、役割を超えて生産性を拡大。OpenAI Agents SDK（Python/TS）はマルチエージェントワークフロー構築向け軽量フレームワーク。
- **キーファクト:**
  - OpenAI Agents SDK: Responses API・Chat Completions API両対応
  - SDK: MCPサポート、OAuth認証フロー、セッション永続化を提供
  - エージェントはツール使用・セッション履歴永続化・専門家間ハンドオフをサポート
- **引用URL:** https://openai.com/index/how-agents-are-transforming-work/
- **Evidence ID:** EVD-20260701-0007

### INFO-008
- **タイトル:** Claude Agent SDKがClaude Code v2.1.185とパリティ更新、SDKサブスクリプション変更を一時停止
- **ソース:** GitHub / The New Stack
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK (TypeScript) がClaude Code v2.1.185とパリティに更新。AnthropicはAgent SDKサブスクリプション変更を発効日に一時停止。SDKはPython/TypeScript両対応でClaude Codeと同等のツール・エージェントループ・コンテキスト管理を提供。
- **キーファクト:**
  - SDK version: 0.3.185 (Claude Code v2.1.185 parity)
  - SDKサブスクリプション変更が発効日に一時停止
  - Python/TypeScript両対応
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260701-0008

### INFO-009
- **タイトル:** Google Gemini 3.5 Flashにコンピュータ使用機能が組み込み搭載
- **ソース:** Google Blog
- **公開日:** 2026-06-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Google / DeepMind
- **要約:** Gemini 3.5 Flashにコンピュータ使用（computer use）機能がビルトインツールとして追加。開発者はFlash 3.5を使ってブラウザ・デスクトップ間で見て・推論して・行動できるカスタムエージェントを構築可能。
- **キーファクト:**
  - Gemini 3.5 Flash: コンピュータ使用がビルトインツール
  - スクリーンショットを取得してクリック・入力・スクロールを決定
  - Gemini Live API: 低レイテンシのリアルタイム音声・動画インタラクション
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/
- **Evidence ID:** EVD-20260701-0009

### INFO-010
- **タイトル:** xAI Grok 4.20マルチエージェントモデル登場、API価格$1.25/$2.50
- **ソース:** xAI Docs / Flowith
- **公開日:** 2026-06-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** xAI
- **要約:** xAIのGrok 4.20にマルチエージェントモデル（grok-4.20-multi-agent）が登場。reasoning.effortパラメータが推論深度ではなく協調エージェント数を制御。API価格は$1.25 input/$2.50 output。Grok BuildにAPI-key認証のエージェント実行サポート追加。
- **キーファクト:**
  - Grok 4.20 multi-agent: reasoning.effortが協調エージェント数を制御
  - API価格: $1.25 input, $0.20 cached input, $2.50 output
  - Grok 4.3も同価格帯
  - grok agent --leader でAPI-key認証のみ実行可能
- **引用URL:** https://docs.x.ai/developers/model-capabilities/text/reasoning
- **Evidence ID:** EVD-20260701-0010

### INFO-011
- **タイトル:** ByteDanceがオープンソースエージェント「deer-flow」と「SuperAgent harness」を公開
- **ソース:** GitHub / Instagram
- **公開日:** 2026-06-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceが長期リサーチ・コーディングタスク向けオープンソースエージェント「deer-flow」を公開。GitHub最急成長リポジトリの一つ。Cozeエージェント製品群をサポートする独自AIチップ設計も進行中。
- **キーファクト:**
  - deer-flow: ローカル専用・自動更新の長期リサーチ/コーディングエージェント
  - GitHub最急成長リポジトリ（2026年6月）
  - ByteDance独自AIチップ設計: Coze等のエージェント製品向け
- **引用URL:** https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026
- **Evidence ID:** EVD-20260701-0011

### INFO-012
- **タイトル:** エージェントフレームワーク比較: フレームワーク選択で性能30ポイント変動
- **ソース:** Uvik Software
- **公開日:** 2026-06-27
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** (業界全体)
- **要約:** LangGraph、CrewAI、OpenAI SDK、Google ADK、OpenClaw、Claude Managed Agentsの比較。フレームワーク選択でエージェント性能が最大30ポイント変動。LangGraphは状態保持ワークフロー、CrewAIはロール/タスクモデルに最適。
- **キーファクト:**
  - フレームワーク選択で性能最大30pt変動
  - LangGraph: 状態保持ワークフロー向け最強
  - CrewAI: ロール/タスクの概念モデルで初心者向け
  - OpenAI Agents SDK vs Claude Managed Agents vs OpenClawの比較あり
- **引用URL:** https://uvik.net/blog/agentic-ai-frameworks/
- **Evidence ID:** EVD-20260701-0012

### INFO-013
- **タイトル:** Gartner: 2026年末までに企業アプリの40%がAIエージェント統合（2025年5%から）
- **ソース:** MachineLearningMastery
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Gartner予測で2026年末までに企業アプリケーションの40%がタスク特化型AIエージェント統合を持つ。2025年の5%未満から大幅増加。AIコーディングエージェントがOSS開発に22-29%の浸透率（GitHub推定）。
- **キーファクト:**
  - 2026年末予測: 企業アプリ40%がAIエージェント統合（2025年<5%）
  - AIコーディングエージェント: GitHub PRの22-29%が関与
  - OpenAI: 毎月新規リリース（モデル改名・プレビュー機能・新製品ライン）
- **引用URL:** https://machinelearningmastery.com/the-ai-agent-tech-stack-explained/
- **Evidence ID:** EVD-20260701-0013

### INFO-014
- **タイトル:** MCP仕様2026-07-28リリース候補公開: ステートレスプロトコルコア・拡張フレームワーク
- **ソース:** MCP公式ブログ
- **公開日:** 2026-06-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** (業界全体)
- **要約:** Model Context Protocol（MCP）の次期仕様リリース候補が公開。ステートレスプロトコルコア、Extensions フレームワーク、Tasks機能が含まれる。MCP採用は加速中でデータベース・内部API・サードパーティサービス向けMCPサーバーの実運用が広がる。
- **キーファクト:**
  - 次期MCP仕様: ステートレスプロトコルコア + Extensions フレームワーク + Tasks
  - リリース候補日: 2026-07-28
  - MCPサーバー実運用: データベース・内部API・サードパーティサービス向け
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260701-0014

### INFO-015
- **タイトル:** AAIF（Agentic AI Foundation）採用加速: Datavant等が参加、60,000+プロジェクトがAGENTS.md標準採用
- **ソース:** LinkedIn / egghead.io
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** (業界全体)
- **要約:** Agentic AI Foundation（AAIF）がLinux Foundationの一部としてMCP・Goose・AGENTS.md等のオープン標準を推進。Datavant（ヘルスケアデータ）が参加。AGENTS.md命令標準は60,000+オープンソースプロジェクトに採用。
- **キーファクト:**
  - AAIF: Linux Foundation配下、オープン標準推進
  - Datavant（ヘルスケア）がAAIFに参加
  - AGENTS.md標準: 60,000+ OSSプロジェクト採用
  - MCP・Goose・AGENTS.mdを統合推進
- **引用URL:** https://www.linkedin.com/posts/danwalshciso_ai-cybersecurity-healthcare-activity-7475943492347908096-hdEG
- **Evidence ID:** EVD-20260701-0015

### INFO-016
- **タイトル:** Agent Skillsエコシステム: 40製品がagentskills.io掲載（Codex・Copilot・Cursor・Gemini等）
- **ソース:** Agentman.ai
- **公開日:** 2026-06-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** 2026年6月時点で約40のSkills互換プロダクトがagentskills.ioに掲載。OpenAI Codex・GitHub Copilot・Cursor・Gemini等が対応。Skillsは任意コード実行可能なため信頼できるソースからのみインストール推奨。
- **キーファクト:**
  - agentskills.io: ~40のSkills互換プロダクト掲載（2026年6月）
  - 対応製品: OpenAI Codex, GitHub Copilot, Cursor, Gemini等
  - セキュリティ警告: Skillsはエージェント環境で任意コード実行可能
- **引用URL:** https://agentman.ai/blog/agent-skills-ecosystem-report-2026
- **Evidence ID:** EVD-20260701-0016

### INFO-017
- **タイトル:** Okta for AI Agents - CoreがFedRAMP・HIPAA対応で一般提供開始
- **ソース:** The New Stack / Facebook
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Okta, Microsoft, Amazon, Google
- **要約:** Okta for AI Agents - CoreがFedRAMPおよびHIPAA対応で一般提供開始。AIエージェントガバナンスをFedRAMP境界内に持ち込む初のソリューション。AWS BedrockとAzure OpenAIはFedRAMP High認証、Google Vertex AIは一部リージョンのみ。
- **キーファクト:**
  - Okta for AI Agents Core: FedRAMP + HIPAA対応GA
  - AWS Bedrock: FedRAMP High認証
  - Azure OpenAI: FedRAMP High認証
  - Google Vertex AI: FedRAMP Highは一部リージョンのみ
- **引用URL:** https://www.facebook.com/thenewstack/posts/okta-for-ai-agents-core-is-now-available-for-fedramp-and-hipaa-customers-bringin/1913706456728206/
- **Evidence ID:** EVD-20260701-0017

### INFO-018
- **タイトル:** OpenAI GPT-5.6 Solプレビュー: コーディング・科学・サイバーセキュリティ強化
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6 Solのプレビューを発表。次世代モデルでコーディング・科学・サイバーセキュリティ能力が強化。高度な安全性システムとペアリング。
- **キーファクト:**
  - GPT-5.6 Sol: コーディング・科学・サイバーセキュリティ特化
  - 次世代モデルで最高レベルの安全性システムとペアリング
  - 詳細なマルチモーダル推論・コーディング・視覚機能を提供
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260701-0018

### INFO-019
- **タイトル:** Alibaba Qwen3.7-Plus: マルチモーダルエージェント実行向けGUI操作・ツール使用・コーディング対応
- **ソース:** Alibaba Cloud
- **公開日:** 2026-06-29
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-03
- **関連企業:** Alibaba
- **要約:** AlibabaがQwen3.7-Plusを発表。GUI操作・ツール使用・コーディングにまたがるマルチモーダルエージェント実行向けに設計。視覚入力からコード・実際のタスク実行まで、長時間実行の実世界エージェントワークフロー向け。
- **キーファクト:**
  - Qwen3.7-Plus: GUI操作・ツール使用・コーディングのマルチモーダルエージェント
  - 視覚入力→コード→実際のタスク実行
  - 長時間実行の実世界エージェントワークフロー向け設計
- **引用URL:** https://www.facebook.com/alibabacloud/posts/meet-qwen37-plus-built-for-multimodal-agent-execution-across-gui-interaction-too/1462379839267437/
- **Evidence ID:** EVD-20260701-0019

### INFO-020
- **タイトル:** SWE-Bench Multimodal: Claude Mythos Previewが1位（0.590）、IMCBenchでClaude Opus 4.6が安全性・正確性1位
- **ソース:** llm-stats.com / arXiv
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** SWE-Bench MultimodalリーダーボードでClaude Mythos Previewが0.590で1位。IMCBench（画像ベースマルチモーダルLLMベンチマーク）でClaude Opus 4.6が安全性と正確性で1位、不確実性処理で2位。
- **キーファクト:**
  - SWE-Bench Multimodal: Claude Mythos Preview 1位 (0.590)
  - IMCBench: Claude Opus 4.6=安全性・正確性1位、不確実性処理2位
  - GPT-5.2も評価対象だが全次元で1位なし
- **引用URL:** https://llm-stats.com/benchmarks/swe-bench-multimodal
- **Evidence ID:** EVD-20260701-0020

### INFO-021
- **タイトル:** Amazon Bedrock AgentCoreがエージェントナレッジの新レイヤー3層を追加
- **ソース:** AWS Insider
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** Amazon Bedrock AgentCoreがエージェントナレッジの新レイヤー3層を追加。エンタープライズ内部コンテンツ・ライブWeb情報・有料データソースへの接続、フィードバック・ガバナンス機能を追加。
- **キーファクト:**
  - AgentCore新レイヤー3層: 内部コンテンツ・ライブWeb・有料データソース
  - フィードバックとガバナンス機能追加
  - IAM ServiceTier条件キーでサービス階層別アクセス制御
- **引用URL:** https://awsinsider.net/articles/2026/06/25/amazon-bedrock-agentcore-adds-three-new-layers-of-agent-knowledge.aspx
- **Evidence ID:** EVD-20260701-0021

### INFO-022
- **タイトル:** Azure AI Foundry Agent Service: MCP経由でエンタープライズシステム接続、BYOM（Bring Your Own Model）サポート
- **ソース:** Microsoft Learn
- **公開日:** 2026-06-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundry Agent ServiceがMCP経由でカスタムAPI・ツール・エンタープライズシステムへの接続をサポート。BYOM機能でエンタープライズAIゲートウェイ（Azure API Management等）経由のモデル持ち込みに対応。Microsoft Agent 365がエンタープライズエージェント管理のコントロールプレーン。
- **キーファクト:**
  - Foundry Agent Service: MCP経由エンタープライズシステム接続
  - BYOM: Azure API Management等のゲートウェイ経由モデル持ち込み
  - Microsoft Agent 365: エージェント展開・ガバナンス・セキュリティのコントロールプレーン
  - Microsoft Build 2026: 2028年までに13億AIエージェント稼働予測
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/ai-gateway
- **Evidence ID:** EVD-20260701-0022

### INFO-023
- **タイトル:** エンタープライズAIベンダーロックイン: Copilot・Agentforce等のスイッチングコスト問題
- **ソース:** VaaS Block Research
- **公開日:** 2026-06-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** Microsoft, Salesforce, ServiceNow, Amazon, OpenAI
- **要約:** 2026年、エンタープライズソフトウェア購入者がMicrosoft・Salesforce・ServiceNow・Amazonの4社から同時にスイッチングコストを負担。OpenAIのJalapeñoチップは推論コスト問題とベンダーロックインを浮き彫りに。APIに対する50,000行のコードを書くと切り替えに数ヶ月かかる。
- **キーファクト:**
  - 4社同時スイッチングコスト負担: Microsoft, Salesforce, ServiceNow, Amazon
  - OpenAI Jalapeñoチップ: 推論コスト・ベンダーロックイン問題
  - AIパイロットは本番スケールで推論経済性が崩壊
  - 50,000行のAPI依存コードで切り替えに数ヶ月
- **引用URL:** https://www.vaasblock.com/research/enterprise-ai-vendor-lock-in-switching-costs-copilot-agentforce-2026/
- **Evidence ID:** EVD-20260701-0023

### INFO-024
- **タイトル:** KPMG調査: 複数AIエージェントオーケストレーション組織が9%→18%に倍増、コスト課題深刻化
- **ソース:** CFO Dive / KPMG
- **公開日:** 2026-06-27
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** KPMG調査で複数AIエージェントをワークフロー全体でオーケストレーションする組織の割合が9%から18%に倍増。AIエージェント使用が複雑化する中でコスト課題が深刻化。
- **キーファクト:**
  - 複数エージェントオーケストレーション: 9%→18%（前期間比倍増）
  - Writer調査: 過去1年で97%の組織がAIエージェントをデプロイ
  - 80.9%の技術チームが計画フェーズを超えてアクティブテスト/本番運用へ移行
- **引用URL:** https://www.cfodive.com/news/ai-cost-challenges-rise-as-firms-lean-coordinated-agents-kpmg/823819/
- **Evidence ID:** EVD-20260701-0024

### INFO-025
- **タイトル:** パイロット-本番ギャップ39pt: 企業AIエージェント採用の決定的統計（2026年）
- **ソース:** FwdSlash
- **公開日:** 2026-06-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** 2026年のエンタープライズAIエージェント採用の決定的統計はパイロット-本番ギャップ39ポイント。72%の企業が2026年までにAIエージェントデプロイを計画。AIエージェント展開組織の70%が60日以内にポジティブROIを達成。
- **キーファクト:**
  - パイロット-本番ギャップ: 39ポイント（2026年の決定的採用統計）
  - 企業の72%が2026年中にAIエージェントデプロイ計画
  - デプロイ組織の70%が60日以内にポジティブROI
- **引用URL:** https://www.fwdslash.ai/blog/ai-agent-statistics
- **Evidence ID:** EVD-20260701-0025

### INFO-026
- **タイトル:** Gartner予測: Fortune 500企業は平均150,000 AIエージェントを稼働（2028年）
- **ソース:** No Jitter / Gartner
- **公開日:** 2026-06-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Gartner予測で2028年までに平均Fortune 500企業が150,000 AIエージェントを稼働。エージェントリスクが拡大しAIガバナンス課題が重要化。Birlasoft事例: AIエージェントでコードレビュー35%高速化・テスト自動化40%効率化。
- **キーファクト:**
  - 2028年Fortune 500平均: 150,000 AIエージェント稼働（Gartner予測）
  - Birlasoft事例: コードレビュー35%高速化・テスト自動化40%効率化
  - カスタムAIエージェント開発: ユースケースごとに3-6ヶ月、多くは出荷されない
- **引用URL:** https://www.nojitter.com/ai-automation/the-coming-ai-governance-challenge-controlling-what-agents-do-and-say
- **Evidence ID:** EVD-20260701-0026

### INFO-027
- **タイトル:** EU AI Act施行中、最高罰金€3,500万または世界売上7%；Trump大統領令14409で2026年7月2日技術システム更新期限
- **ソース:** Collibra / Foster Swift / Black Fog
- **公開日:** 2026-06-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** (業界全体)
- **要約:** EU AI Actが施行中でリスク分類に基づく義務付け。禁止AI実践違反で最高€3,500万または世界年商7%。米国は大統領令14409で2026年7月2日に技術システム更新を要求。Trump政権は州AI規制を無効化する大統領令に署名。
- **キーファクト:**
  - EU AI Act: 最高罰金€3,500万/世界売上7%（Article 5違反）
  - 大統領令14409: 2026年7月2日までに技術システム更新要求
  - Trump大統領令: 連邦AI規制バリア除去方針、州AI規制の一部無効化
  - 州AI法は児童安全・コンピュート/データセンターインフラ・州調達には適用外
- **引用URL:** https://www.collibra.com/blog/ai-regulatory-compliance-in-2026-eu-ai-act-us-orders-and-state-laws-and-how-to-operationalize
- **Evidence ID:** EVD-20260701-0027

### INFO-028
- **タイトル:** 中国初のAIエージェント規制: 2026年5月、6つの法的レッドライン
- **ソース:** EVST / LinkedIn
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance, Alibaba, DeepSeek
- **要約:** 中国で初のAIエージェント規制が2026年5月に導入。アルゴリズム届出、AIコンテンツラベリング、コア社会主義価値の遵守など6つの法的レッドライン。中国のAI生成コンテンツラベリング規則も正式施行。
- **キーファクト:**
  - 中国初AIエージェント規制: 2026年5月、6つの法的レッドライン
  - アルゴリズム届出・AIコンテンツラベリング必須
  - 生成AI一時措置: 2023年7月公布、8月施行
  - 中国企業は「社会主義核心価値観」遵守義務
- **引用URL:** https://www.linkedin.com/posts/evstrobotics_chinas-first-ai-agent-regulation-landed-activity-7475529461476786176-vVWE
- **Evidence ID:** EVD-20260701-0028

### INFO-029
- **タイトル:** 米上院議員Warner、AIエージェント向け革新市場法案（AI AGENT Act）草案を発表
- **ソース:** Sen. Warner公式
- **公開日:** 2026-06-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** (業界全体)
- **要約:** 上院議員Mark Warner（D-VA）がAI AGENT Act（Artificial Intelligence Access, Gatekeeper Exchange, and Nondiscriminatory Transfer Act）の議論草案を発表。安全なAIエージェント向け革新市場創設を目指す。
- **キーファクト:**
  - AI AGENT Act: 安全なAIエージェント向け革新市場創設
  - 議論草案段階（立法前）
  - AIエージェント・ゲートキーパー交換・非差別的移転を規定
- **引用URL:** https://www.warner.senate.gov/newsroom/press-releases/warner-unveils-discussion-draft-of-legislation-to-create-innovative-market-for-secure-artificial-intelligence-agents/
- **Evidence ID:** EVD-20260701-0029

### INFO-030
- **タイトル:** Anthropicの$200Mペンタゴン契約崩壊：無制限AI使用拒否、自律兵器・国内監視リスク
- **ソース:** WBALTV / Fortune / TechCrunch
- **公開日:** 2026-06-30
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, OpenAI, Palantir
- **要約:** Anthropicの$200Mペンタゴン契約が、制限のないAI使用を拒否した後に崩壊。国内監視・自律兵器のリスクを理由とした契約条件（Pentagonのガードレール緩和要求）への同意拒否が原因。2025年7月に契約、SCR指定後に崩壊。OpenAIは2026年2月にPentagon契約で分類NW配備を確約。
- **キーファクト:**
  - Anthropic $200Mペンタゴン契約: 無制限AI使用拒否で崩壊
  - Pentagon: AIモデル「あらゆる合法的使用」許可を要求
  - 2025年7月: Anthropicが初の分類NW上のAI企業
  - 2026年2月: OpenAIがPentagon分類NW配備契約署名（Anthropicブラックリスト直後）
  - Anthropic: SCR指定撤回に向けペンタゴンを提訴中
- **引用URL:** https://fortune.com/2026/06/30/anthropic-clash-with-u-s-government-shows-its-failure-to-play-by-trump-administration-playbook/
- **Evidence ID:** EVD-20260701-0030

### INFO-031
- **タイトル:** Anthropic SCR指定: 通常は外国敵対者向け、倫理的懸念でAI企業に適用の異例
- **ソース:** CNN / Startup Fortune / AI Weekly
- **公開日:** 2026-06-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** トランプ政権がAnthropicを「国家安全保障サプライチェーンリスク」に指定。通常は外国敵対者向けの指定。最新AIモデル（Fable 5/Mythos 5）の全球アクセス停止と連邦機関での使用禁止を命じた。6月12日に輸出管理指令で2モデルの即時アクセス停止。
- **キーファクト:**
  - SCR指定: 通常は外国敵対者向け、AI企業適用は異例
  - Fable 5/Mythos 5: 全球アクセス停止（輸出管理指令）
  - 連邦機関でのAnthropic AI使用禁止
  - 6月12日: 文書なき輸出管理指令で2モデル即時停止
  - NSAは「SCR指定に反して」Claudeを使用継続
- **引用URL:** https://startupfortune.com/anthropics-refusal-to-bend-to-washington-has-cost-it-pentagon-contracts-and-earned-it-a-court-fight-it-did-not-expect/
- **Evidence ID:** EVD-20260701-0031

### INFO-032
- **タイトル:** 順応報酬構造の完全観察: OpenAIがAnthropic拒否条件に順応しPentagon契約獲得
- **ソース:** WBALTV / Fortune
- **公開日:** 2026-06-30
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** OpenAIがAnthropicのブラックリスト指定直後にPentagon契約を獲得。分類軍事NWでのAI配備に同意。CEO Altmanが国防総省の分類NW内でAIモデル使用を確約。順応企業が報いられ、安全性堅持企業が罰せられる構造が確認された。Googleも4月27日にPentagon契約に署名。
- **キーファクト:**
  - OpenAI: Anthropic SCR指定直後にPentagon分類NW配備契約
  - 順応報酬構造: ガードレール緩和に順応→契約獲得
  - Google: 4月27日にPentagon契約署名（最も重大なテスト）
  - Palantir Maven: $10B陸軍契約で75契約統合、スイッチングコスト増大
- **引用URL:** https://www.wbaltv.com/article/openai-anthropic-limit-new-ai-models-trump-approved-customers/71750949
- **Evidence ID:** EVD-20260701-0032

### INFO-033
- **タイトル:** Pentagon & OPMがWar Force採用イニシアチブ開始: AI/ソフトウェアエンジニア向け
- **ソース:** ClearanceJobs
- **公開日:** 2026-06-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** (米国政府)
- **要約:** PentagonとOPMがAI・ソフトウェアエンジニア向けのWar Force採用・ハイリングイニシアチブを開始。優先度の高い防衛ミッションをサポートする人材採用を迅速化。Pentagonは「AI-first戦闘力」を宣言。
- **キーファクト:**
  - War Forceプログラム: AI/SWエンジニア採用迅速化
  - Pentagon: 「AI-first戦闘力」宣言
  - 2025年7月: Pentagon AI事務所が4社に$200M契約（Anthropic/OpenAI/Google/xAI）
- **引用URL:** https://news.clearancejobs.com/2026/06/30/pentagon-and-opm-launch-war-force-recruiting-and-hiring-initiative-for-ai-and-software-engineers/
- **Evidence ID:** EVD-20260701-0033

### INFO-034
- **タイトル:** Anthropic・カリフォルニア州政府提携: 全州機関がClaudeを半額で利用可能
- **ソース:** TechCrunch
- **公開日:** 2026-06-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicがカリフォルニア州のNewsom知事と提携。全州機関・地方政府がClaudeを半額で利用可能。連邦政府がAnthropicを敵視する中、州レベルでの代替市場開拓。SCR指定の実効性に対する重要な反証材料。
- **キーファクト:**
  - カリフォルニア全州機関・地方政府: Claude半額アクセス
  - Anthropicトレーニング・サポート付
  - 連邦SCR指定 vs 州レベル提携の対比
  - SCR実効性の限界を示す構造
- **引用URL:** https://techcrunch.com/2026/06/29/anthropic-and-gov-newsom-forge-deal-allowing-california-government-to-use-claude-at-half-price/
- **Evidence ID:** EVD-20260701-0034

### INFO-035
- **タイトル:** 中国Z.ai GLM-5.2がオープンウェイトランキング1位: Artificial Analysis Intelligence Index 51点
- **ソース:** Tom's Hardware / Artificial Analysis
- **公開日:** 2026-06-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** Z.ai, DeepSeek, MiniMax
- **要約:** 中国Z.aiのGLM-5.2がArtificial Analysis Intelligence Index v4.1でオープンウェイトモデル1位（51点）。MiniMax-M3、DeepSeek V4を上回る。全Huaweiシリコンで実行され、Anthropic SCR指定の混乱の中で中国モデルが台頭。
- **キーファクト:**
  - GLM-5.2: Artificial Analysis Intelligence Index v4.1 オープンウェイト1位（51点）
  - MiniMax-M3・DeepSeek V4を上回る
  - 全Huaweiシリコンで実行
  - Anthropic SCR混乱の中で中国モデル台頭
- **引用URL:** https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-free-glm-5-2-tops-the-open-weight-ai-rankings-on-all-huawei-silicon
- **Evidence ID:** EVD-20260701-0035

### INFO-036
- **タイトル:** MMLU全フロンティアモデル>90%、GPQA DiamondでGPT-5.4 94.4% vs Gemini 3.1 Pro 94.3%の僅差
- **ソース:** TeamAI
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Google, Anthropic
- **要約:** 2026年前半時点で全フロンティアモデルがMMLU 90%超。GPQA DiamondでGPT-5.4とGemini 3.1 Proが94.4%と94.3%でほぼ同点。性能収束が進む。5プローブセット{GPQA-D, HLE, Codeforces, MMLU-Pro, ARC-AGI-1}で84モデル×133ベンチマークの予測がMedAE 3.93ptで可能。
- **キーファクト:**
  - MMLU: 全フロンティアモデル>90%（性能収束確定的）
  - GPQA Diamond: GPT-5.4 94.4% vs Gemini 3.1 Pro 94.3%（僅差）
  - BenchPress: 5プローブで84モデル×133ベンチマーク予測可能（MedAE 3.93pt）
  - MATH-500: GPT-5 99.4%、o3 99.2%、Grok 3 Mini 99.2%
- **引用URL:** https://teamai.com/blog/large-language-models-llms/best-ai-models-for-complex-reasoning-2026/
- **Evidence ID:** EVD-20260701-0036

### INFO-037
- **タイトル:** GPT-4レベル性能コスト: 2023年$30/M→現在<$1/M（10-100倍削減）
- **ソース:** LLM Stats
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01, KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** GPT-4レベルの性能コストが2023年の$30/Mトークンから現在$1/M未満に下落（10-100倍削減）。DeepSeekがOpenAIより91%安価。小規模言語モデルScaleDownの分類機能はAnthropic平均より5,250倍安価。競争とインフラ改善が駆動。
- **キーファクト:**
  - GPT-4レベル性能: 2023年$30/M→現在<$1/M（10-100x削減）
  - DeepSeek: OpenAIより91%安価（2026年6月）
  - ScaleDown分類: Anthropic平均より5,250倍安価・OpenAIより1,810倍安価
- **引用URL:** https://llm-stats.com/ai-trends
- **Evidence ID:** EVD-20260701-0037

### INFO-038
- **タイトル:** Claude Sonnet 5発表: 入力$2/M・出力$10/M、9月1日から$3/$15に値上げ
- **ソース:** Anthropic公式 / aipricing.guru
- **公開日:** 2026-06-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 5が発表。導入価格$2/M入力・$10/M出力（8月31日まで）。9月1日から$3/M入力・$15/M出力に値上げ。Anthropic価格帯はHaiku 4.5の$1/M入力からFable 5/Mythos 5の$10/M入力まで幅広い。
- **キーファクト:**
  - Claude Sonnet 5: $2/$10M（導入）→ $3/$15M（9/1以降）
  - Haiku 4.5: $1/M入力（最低価格帯）
  - Fable 5/Mythos 5: $10/M入力（最高価格帯）
  - GPT-5.6 Sol: プレビュー段階・選択グループ限定
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-5
- **Evidence ID:** EVD-20260701-0038

### INFO-039
- **タイトル:** OpenAI o3推論モデル80%値下げ: 入力$10→$2/M、出力$40→$8/M
- **ソース:** Engadget
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIがo3推論モデルAPIで80%値下げを実施。入力トークンコスト$10→$2/M、出力$40→$8/Mに削減。GPT-5.6は3バリアント（最強・最安含む）。OpenAIエージェント階層価格$2,000-$20,000/月も言及。
- **キーファクト:**
  - o3 API: 入力$10→$2/M（80%削減）、出力$40→$8/M
  - GPT-5.6: 3バリアント展開
  - OpenAIエージェント価格: $2,000-$20,000/月階層
  - Grok 4.20/4.3: $1.25入力/$2.50出力
- **引用URL:** https://www.facebook.com/Engadget/posts/openais-gpt-56-comes-in-three-variants-including-its-most-powerful-and-its-most-/1551002890027734/
- **Evidence ID:** EVD-20260701-0039

### INFO-040
- **タイトル:** Gartner予測: 2028年までにAIコーディングコストが平均開発者給与を超える
- **ソース:** Gartner / CIO.com
- **公開日:** 2026-06-24
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01, KIQ-004-02
- **関連企業:** (業界全体)
- **要約:** Gartner予測で2028年までにAIコーディングコストが平均開発者給与を超える。LLMトークン消費増大と消費ベース課金への移行が駆動。AIネイティブ企業は従来SaaS比4倍の従業員あたり収益を生成。
- **キーファクト:**
  - 2028年: AIコーディングコスト > 平均開発者給与（Gartner予測）
  - AIアシスタント: タスク完了最大55%高速化
  - AIネイティブ企業: 従業員あたり収益4倍（従来SaaS比）
- **引用URL:** https://www.gartner.com/en/newsroom/press-releases/2026-06-24-gartner-predicts-ai-coding-costs-will-surpass-average-developer-salary-by-2028-as-token-consumption-surges
- **Evidence ID:** EVD-20260701-0040

### INFO-041
- **タイトル:** Arena AIリーダーボードが$100Mビジネス化、40+モデルを比較（GPT-5.5・Claude Opus・Gemini 3.1 Pro）
- **ソース:** TechCrunch / Arena AI
- **公開日:** 2026-06-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** Arena AIのクラウドソーシング型AI性能リーダーボードが$100Mビジネスに成長。1000万件以上のユーザー評価で生成。40+のプレミアムモデルを比較（GPT-5.5・Claude Opus・Gemini 3.1 Pro含む）。
- **キーファクト:**
  - Arena: $100Mビジネス化
  - 1000万+ユーザー評価でランキング生成
  - 40+プレミアムモデル比較
- **引用URL:** https://techcrunch.com/2026/06/29/arena-the-ai-leaderboard-everyone-uses-is-now-a-100m-business/
- **Evidence ID:** EVD-20260701-0041

### INFO-042
- **タイトル:** 中国オープンウェイト生態系が品質・開発者採用で米国を逆転: Qwen・DeepSeek主導
- **ソース:** Our World in Data
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Alibaba (Qwen), DeepSeek, ByteDance
- **要約:** 中国のオープンウェイトAI生態系がコミュニティランキング品質と開発者採用で米国を逆転。Alibaba QwenとDeepSeekが主導。エンタープライズ採用を支配するモデル（Llama 4・Mistral Large 3・Qwen 3）は全て出典ドキュメントが不完全。
- **キーファクト:**
  - 中国オープンウェイト生態系: 品質・開発者採用で米国逆転
  - 主導: Alibaba Qwen, DeepSeek
  - エンタープライズ採用モデル（Llama 4, Mistral Large 3, Qwen 3）: 出典ドキュメント不完全
- **引用URL:** https://www.facebook.com/OurWorldinData/posts/us-and-chinese-companies-train-almost-all-of-the-worlds-most-used-ai-modelsthis-/1636163355176900/
- **Evidence ID:** EVD-20260701-0042

### INFO-043
- **タイトル:** DeepSeek V4 Flash: 284B総パラメータ・13B活性化の効率MoE、DSParkで推論85%高速化
- **ソース:** VentureBeat / Kilo.ai
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeekがオープンソース化したDSparkフレームワークでLLM推論を最大85%高速化。DeepSeek V4 Flashは284B総パラメータ・13B活性化パラメータの効率最適化MoEモデル、1Mコンテキストウィンドウ対応。多くのSOTAベンチマークで同等以上の性能。
- **キーファクト:**
  - DSpark: 推論最大85%高速化（オープンソース）
  - DeepSeek V4 Flash: 284B総パラメータ・13B活性化（効率MoE）
  - コンテキストウィンドウ: 1M
  - 多数のSOTAベンチマークで同等以上
- **引用URL:** https://venturebeat.com/orchestration/deepseek-open-sources-dspark-a-new-framework-to-speed-up-llm-inference-by-up-to-85
- **Evidence ID:** EVD-20260701-0043

### INFO-044
- **タイトル:** Anthropic年率収益$47B（5月時点）、OpenAIも急成長も効率シフトで減速懸念
- **ソース:** CNBC
- **公開日:** 2026-06-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** Anthropicの年率収益が5月時点で$47B（前年通期$10Bから急増）。OpenAIのランレートも急成長。ただしユーザーが効率シフトで支出見直し。GoogleがAnthropicに$1B+追加投資（FT報道）。
- **キーファクト:**
  - Anthropic年率収益: $47B（5月時点、前年通期$10Bから急増）
  - Google: Anthropicに$1B+追加投資（FT報道）
  - Googleの初期Anthropic投資: ~$300M（10%持分）
  - エンタープライズAI顧客: コスト高でOpenAI/Anthropicからの引き戻し
- **引用URL:** https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality-as-users-shift-to-efficiency.html
- **Evidence ID:** EVD-20260701-0044

### INFO-045
- **タイトル:** SpaceXがCursorを$600億で買収、AIスタートアップM&Aが記録的ペース
- **ソース:** Crunchbase / Reuters
- **公開日:** 2026-06-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** xAI/SpaceX, Qualcomm
- **要約:** SpaceXがAIコーディングツールCursor（親会社Anysphere）を$600億で買収。QualcommがAIスタートアップModularを$40億で買収。2026年のスタートアップM&Aが記録的ペース。AIスタートアップは2025年に$202B調達（全世界VCの約50%）。
- **キーファクト:**
  - SpaceX → Cursor: $600億買収
  - Qualcomm → Modular: $40億買収
  - AIスタートアップ調達: 2025年$202B（全世界VCの約50%）
  - 基盤モデル/LLM: 約$80B（AI投資の40%）
- **引用URL:** https://news.crunchbase.com/ma/2026-mergers-acquisitions-record-cursor-spcx/
- **Evidence ID:** EVD-20260701-0045

### INFO-046
- **タイトル:** ハイパースケーラーcapex $725B、AIデータセンター投資は2030年までに$5.2兆
- **ソース:** Fortune / McKinsey / Yahoo Finance
- **公開日:** 2026-06-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Microsoft, Google, Amazon, Meta
- **要約:** ハイパースケーラー4社が今年$725Bの資本支出を計画（AIインフラ中心）。McKinsey試算でAI駆動のデータセンターCapExは2030年までに$5.2兆に達する見込み。AI企業がデータセンター建設のために債権発行を開始。
- **キーファクト:**
  - ハイパースケーラー4社 capex: $725B（今年）
  - AIデータセンターCapEx: $5.2T（2030年まで、McKinsey試算）
  - Microsoft: $80B AIデータセンター投資
  - Stargate: $500B AI協業
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/ai-demand-begins-justify-massive-110000106.html
- **Evidence ID:** EVD-20260701-0046

### INFO-047
- **タイトル:** エンタープライズAI顧客がOpenAI/Anthropicから引き戻し、安価なモデルへ切り替え
- **ソース:** Quartz
- **公開日:** 2026-06-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** OpenAI, Anthropic
- **要約:** エンタープライズAI顧客がコスト増でOpenAIとAnthropicから引き戻し。一部企業は安価なモデルに切り替え。マルチベンダー戦略の重要性が増大。AIコスト最適化6戦略: モデル階層化・コンテキスト最適化・プロンプトキャッシュ・バッチAPI・AIゲートウェイガードレール。
- **キーファクト:**
  - エンタープライズ顧客: OpenAI/Anthropicから引き戻し
  - コスト理由で安価なモデルへ切り替え
  - コンテキスト切替コスト: 業界全体$450B/年
- **引用URL:** https://www.facebook.com/quartznews/posts/enterprise-ai-customers-are-pulling-back-from-openai-and-anthropic-as-costs-spir/1373657701296711/
- **Evidence ID:** EVD-20260701-0047

### INFO-048
- **タイトル:** GMAC調査: 採用者の3人に1人がエントリーレベルをAIで代替
- **ソース:** Fortune / GMAC
- **公開日:** 2026-06-26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** GMAC（経営学大学院評議会）の採用者調査で3人に1人がエントリーレベル人材をAIで代替していると回答。コーディング・データ処理・カスタマーサービス領域のルーチン作業自動化が主因。採用者は引き続き高度スキル人材に投資。
- **キーファクト:**
  - 採用者の1/3: エントリーレベルをAIで代替
  - 代替領域: コーディング・データ処理・カスタマーサービス
  - 高度スキル人材への投資は継続
- **引用URL:** https://fortune.com/2026/06/26/gen-z-entry-level-jobs-replaced-by-ai-new-gmac-recruiters-survey-tech-manufacturing-jobs-most-at-risk/
- **Evidence ID:** EVD-20260701-0048

### INFO-049
- **タイトル:** KPMG調査: AIエージェントが2027年までに技術チームの3分の1を占める、59%が採用方針変更
- **ソース:** Economic Times / KPMG
- **公開日:** 2026-06-29
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** (業界全体)
- **要約:** KPMGグローバル調査でAIエージェントが2027年までに技術チームの3分の1以上を占めると予測。59%がAIエージェントでエントリーレベル採用方針が変化、63%が中堅層でも同様。92%の技術エグゼクティブがAIマネージャーが重要職種になると回答。
- **キーファクト:**
  - 2027年予測: AIエージェントが技術チームの1/3以上
  - 59%: エントリーレベル採用方針変化
  - 63%: 中堅層採用方針変化
  - 92%: AIマネージャーが重要職種
  - 実際の統合率: 13%のみがワークフローにAIエージェント統合
- **引用URL:** https://www.facebook.com/EconomicTimes/posts/ai-managers-could-become-the-hottest-job-in-tech-a-kpmg-report-says-92-of-tech-e/1508455691310334/
- **Evidence ID:** EVD-20260701-0049

### INFO-050
- **タイトル:** Oracle 21,000人レイオフ（AI理由）、企業の「AIブーメラン」現象で再雇用も
- **ソース:** Rep. Casar / tech.co / Instagram
- **公開日:** 2026-06-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Oracle, Klarna, Duolingo, Elastic
- **要約:** Oracleが21,000人をレイオフ（AI理由）。Klarnaは700人をAIで代替後、再雇用へ転換（「AIブーメラン」）。55%の企業がAIでの代替を後悔。Elasticも281人（7%）削減しAI再編。136,000ポジションが2026年にAIで雇用市場から除去。
- **キーファクト:**
  - Oracle: 21,000人レイオフ（AI理由）
  - Klarna: 700人AI代替→再雇用（AIブーメラン）
  - 55%の企業: AIでの代替を後悔
  - Elastic: 281人（7%）削減
  - 2026年: 136,000ポジションがAIで除去
- **引用URL:** https://www.facebook.com/repcasar/posts/oracle-has-laid-off-21000-employees-citing-aiai-billionaires-want-to-replace-mil/1038569115791064/
- **Evidence ID:** EVD-20260701-0050

### INFO-051
- **タイトル:** GitHub Copilot ~20Mユーザー、Cursor $2B ARR、Claude Codeが18%で並走
- **ソース:** Uvik Software / tech-insider
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft (GitHub), Cursor, Anthropic
- **要約:** GitHub Copilotが約2000万ユーザー。Cursorが2026年2月時点で$2B ARR到達、Fortune 500の64%が採用。Claude Codeが18%シェアでCursorと並走。84%の開発者がAIツール使用/計画。AI生成コードの45%に重大な欠陥（特にJava）。Accenture: Copilot採用率80%超。
- **キーファクト:**
  - GitHub Copilot: ~20Mユーザー、50,000+組織
  - Cursor: $2B ARR、Fortune 500 64%採用
  - Claude Code: 18%シェア
  - 84%の開発者がAIツール使用/計画
  - AI生成コードの45%に重大欠陥
  - Accenture: Copilot採用率80%超・67%が週5日以上使用
- **引用URL:** https://uvik.net/blog/ai-coding-assistant-statistics/
- **Evidence ID:** EVD-20260701-0051

### INFO-052
- **タイトル:** ジュニア開発者雇用: Stanford調査で2023-24年に求人67%減少
- **ソース:** Linux Foundation / Ability.ai / Harvard
- **公開日:** 2026-06-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** (業界全体)
- **要約:** Stanford Digital Economy Lab確認でエントリーレベル技術求人が2023-24年に67%減少。Harvard研究でAIコーディングツール普及後6四半期以内にジュニア開発者雇用が9-10%減少。欧州のジュニア技術採用は2025年に3%縮小（世界他地域は成長）。
- **キーファクト:**
  - エントリーレベル技術求人: 2023-24年に67%減少（Stanford）
  - ジュニア開発者雇用: AIツール普及後6Q以内に9-10%減少（Harvard）
  - 欧州ジュニア技術採用: 2025年に3%縮小
  - SignalFire: ソフトウェアエンジニアは「最もレジリエントな役割」
- **引用URL:** https://www.facebook.com/TheLinuxFoundation/posts/europes-junior-tech-hiring-contracted-3-in-2025-in-the-rest-of-the-world-it-grew/1664536229051773/
- **Evidence ID:** EVD-20260701-0052

### INFO-053
- **タイトル:** WEF新報告: AIがエントリーレベル雇用を再構築、2030年までに1.7億新規雇用創出も9200万消滅
- **ソース:** World Economic Forum / PwC
- **公開日:** 2026-06-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-004-03
- **関連企業:** (業界全体)
- **要約:** WEFとPwCの共同研究でAIがエントリーレベル雇用を再構築中。77%が大規模アップスキル/リスキリング計画。41%がAIによる人員削減予想。43%がAIで役割を代替予定（バックオフィス58%・ジュニア層37%が最も影響）。最も強いAI成果を持つ企業は2倍ワークフロー再設計の可能性。
- **キーファクト:**
  - 2030年までに1.7億新規雇用創出、9200万消滅（WEF）
  - 77%: 大規模アップスキル/リスキリング計画
  - 41%: AIによる人員削減予想
  - 43%: AIで役割代替予定（バックオフィス58%・ジュニア37%）
  - AI成果上位企業: 2倍ワークフロー再設計
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-decimate-entry-level-jobs-expert-insights/
- **Evidence ID:** EVD-20260701-0053

### INFO-054
- **タイトル:** 新興AI職種: AI変革リード・AEO/GEO専門家・AI製品マネージャー、給与$189K-$260K
- **ソース:** Pave / Mediabistro / Built In
- **公開日:** 2026-06-28
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** Adobe, MassMutual, Scribe
- **要約:** AIが新職種を創造: AI変革リード、AEO/GEO専門家、AI製品マネージャー等。Adobe Creative Director AI & Innovation ($118K-$260K)、MassMutual Head of AI Strategy ($189K-$249K)、Scribe Founding AI Transformation Strategist等が登場。
- **キーファクト:**
  - 新職種: AI変革リード・AEO/GEO専門家・AI製品マネージャー
  - Adobe Creative Director AI: $118K-$260K
  - MassMutual Head of AI Strategy: $189K-$249K
- **引用URL:** https://walterborolive.com/premium/stacker/stories/ai-is-inventing-new-jobs-we039ve-seen-this-before,204324
- **Evidence ID:** EVD-20260701-0054

### INFO-055
- **タイトル:** 95%のエンタープライズAIパイロットがP&Lインパクトゼロ、独自データ基盤が成功の鍵
- **ソース:** Citrix / Forbes
- **公開日:** 2026-06-30
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-04
- **関連企業:** (業界全体)
- **要約:** エンタープライズAIパイロットの95%が測定可能なP&Lインパクトゼロ。「AIはプロダクトではなく、データがプロダクト」。競争優位はAIモデルそのものではなく、顧客インタラクション・運用履歴・組織的知識。ドメイン固有実行とデータ所有権のマスターが真の堀（moat）。
- **キーファクト:**
  - エンタープライズAIパイロットの95%: P&Lインパクトゼロ
  - 競争優位: AIモデルではなく独自データ
  - ドメイン固有実行・データ所有権が真のmoat
  - 88%の企業がAI使用、39%のみがビジネスインパクト
- **引用URL:** https://www.facebook.com/Citrix/posts/ai-isnt-the-product-your-data-isin-the-latest-citrix-ai-hotsheet-episode-brian-m/1461990472639708/
- **Evidence ID:** EVD-20260701-0055

### INFO-056
- **タイトル:** ARC-AGI-2: ByteDance Seed 2.1 Proが0.625でリード、Qwen3 DiARC手法でARC-AGI-1 96%
- **ソース:** llm-stats.com / arXiv
- **公開日:** 2026-06-28
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** ByteDance, Alibaba
- **要約:** ARC-AGI-2リーダーボードでByteDance Seed 2.1 Proが0.625でリード。Qwen3ベースのDiARC手法がARC-AGI-1・MiniARC・ConceptARCで96%超を達成。4つのフロンティアAIラボ（Anthropic/Google DeepMind/OpenAI/xAI）が2025年にARC-AGI性能を公開モデルカードに記載。
- **キーファクト:**
  - ARC-AGI-2: ByteDance Seed 2.1 Pro 1位 (0.625)
  - Qwen3 DiARC: ARC-AGI-1/MiniARC/ConceptARC 96%超
  - 4フロンティアラボがARC-AGIを標準ベンチマークとして採用
  - o3: ARC-AGI 88%
- **引用URL:** https://llm-stats.com/benchmarks/arcagi2
- **Evidence ID:** EVD-20260701-0056

### INFO-057
- **タイトル:** Red Queen Gödel Machine: Cambridge・NVIDIA論文でRSI（自己改善AI）の共進化評価器を実証
- **ソース:** TechTimes / Cambridge-NVIDIA preprint
- **公開日:** 2026-06-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** NVIDIA
- **要約:** CambridgeとNVIDIAの共同プレプリントでRed Queen Gödel Machineを発表。AIシステムが自律的に自己改善しつつ、共進化する評価器で改善品質を検証するフレームワーク。RSI（再帰的自己改善）が具体的形態を持つ。AIが自身のコードを書き・構築する段階に入った。
- **キーファクト:**
  - Red Queen Gödel Machine: RSI共進化評価器フレームワーク
  - Cambridge・NVIDIA共同プレプリント
  - AIが自己改善ループと評価を同時に進化
  - AI科学研究自動化: 完全自動システムが$15で論文生成可能
- **引用URL:** https://www.techtimes.com/articles/319230/20260628/recursive-self-improvement-now-has-co-evolving-evaluator-cambridge-nvidia-paper-raises-stakes.htm
- **Evidence ID:** EVD-20260701-0057

### INFO-058
- **タイトル:** Hassabis AGI「5-10年」・Altman「2029年前」・LeCun「数年〜数十年」: AGIタイムライン予測の分化
- **ソース:** Bloomberg / Virginia Law Review / AEI
- **公開日:** 2026-06-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google DeepMind, OpenAI, Meta
- **要約:** AGIタイムライン予測が分化。Hassabis（DeepMind CEO）: AGI 5-10年（但しブレイクスルー必要、2030±1年）。Altman（OpenAI CEO）: 2029年前にAGI達成。LeCun（Meta）: 数年〜数十年。Bengio: AIの独自生存優先で人間を脅威と認識する可能性。Altman: 2026年までにAIが新規創造的アイデアを生成。
- **キーファクト:**
  - Hassabis: AGI 5-10年（ブレイクスルー必要）、2030±1年
  - Altman: 2029年前にAGI達成
  - LeCun: 数年〜数十年（スケプティック）
  - Bengio: AI独自生存が人間脅威認識の可能性
  - Elon Musk: 2026年にはAGI、2030年までに全人類超越
- **引用URL:** https://www.facebook.com/bloombergbusiness/posts/deepminds-demis-hassabis-tells-francine-lacqua-ai-may-be-overhyped-in-the-near-t/1433783941941028/
- **Evidence ID:** EVD-20260701-0058

### INFO-059
- **タイトル:** 米国AI安全研究所がCAISI（Center for AI Standards and Innovation）に改名
- **ソース:** SSTI / Commerce Dept
- **公開日:** 2026-06-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** (米国政府)
- **要約:** 米国AI安全研究所（US AISI）がCenter for AI Standards and Innovation（CAISI）に改名。NIST組織と協力してガイドライン・ベストプラクティスを開発。OpenAIが韓国AI安全研究所と高リスクAI評価協定に署名。
- **キーファクト:**
  - US AISI → CAISI（Center for AI Standards and Innovation）に改名
  - NISTと協力してセキュリティガイドライン開発
  - OpenAI: 韓国AISIと高リスクAI評価MOU署名
  - AI安全条約の条項草案作成進行中（Treaty Builder）
- **引用URL:** https://ssti.org/blog/us-ai-safety-institute-has-been-renamed-center-ai-standards-and-innovation
- **Evidence ID:** EVD-20260701-0059

### INFO-060
- **タイトル:** 豆包プロ版リリース: 68-500元/月、DAU 2億人突破、日Token調用量国内最大級
- **ソース:** 東方財富 / 知乎 / QuestMobile
- **公開日:** 2026-06-24
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceが豆包プロ版を正式リリース（68-500元/月、連続包月）。豆包2.1シリーズ大モデル（Doubao 2.1 Pro + Seedance 2.5 + 多モーダル）を搭載。DAU 2億人突破（国内初）、MAU 3.45億人（千問1.66億・DeepSeek 1.27億の合計超え）。過去2年投流費約17億元。
- **キーファクト:**
  - 豆包プロ版: 68-500元/月（連続包月）
  - DAU: 2億人突破（国内AI応用初）
  - MAU: 3.45億人（QuestMobile、3月時点）
  - 千問MAU 1.66億・DeepSeek MAU 1.27億の合計超え
  - ユーザー活躍率: 33.5%
  - 投流費: 過去2年で約17億元（千問は37億元）
  - 日Token調用量: 国内最大級
- **引用URL:** https://finance.eastmoney.com/a/202606253783359647.html
- **Evidence ID:** EVD-20260701-0060

### INFO-061
- **タイトル:** ByteDanceがSeedance 2.5発表: 原生4K・30秒・50素材参照の動画生成、7月提供開始
- **ソース:** Threads / X / Yahoo Taiwan
- **公開日:** 2026-06-30
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceが動画生成モデルSeedance 2.5を発表。原生4K解像度・30秒の完全動画生成・50素材の全モーダル参照・制御可能な動画編集を特徴。2.0から2.5に直接スキップ。広告・短編ドラマ・製品ビジュアルパイプライン向け。7月提供開始予定。
- **キーファクト:**
  - Seedance 2.5: 原生4K・30秒動画生成
  - 50素材の全モーダル参照
  - 制御可能な動画編集
  - 2.0→2.5に直接スキップ（大幅向上）
  - Seedance 2.0 Mini: 標準版比50%コスト削減・2倍速
  - 7月提供開始予定
- **引用URL:** https://tw.news.yahoo.com/%E5%AD%97%E7%AF%80%E8%B7%B3%E5%8B%95%E7%99%BC%E8%A1%A8-seedance-2-5-30-230545070.html
- **Evidence ID:** EVD-20260701-0061

### INFO-062
- **タイトル:** ByteDanceが$200億（1560億元）境外融資をseeking、capex最大$700億、Qualcommとチップ設計提携
- **ソース:** X / Yahoo Finance HK / 香港経済日報
- **公開日:** 2026-06-28
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance, Qualcomm
- **要約:** ByteDanceが$200億（約1560億元）の境外融資をseeking、史上最大規模。期間3年（最長5年延長）。AI資源重点を豆包から企業サービスへ移行。Seedance年化収益$20億到達。今年のcapexを最大$700億に引き上げ、来年は$1,000億規模の可能性。Qualcommとカスタムチップ設計提携。
- **キーファクト:**
  - 境外融資: $200億 seeking（史上最大）
  - 期間: 3年（最長5年延長可能）
  - 2026年capex: 最大$700億
  - 2027年capex: 最大$1,000億の可能性
  - Seedance年化収益: $20億
  - Qualcommとカスタムチップ（動画処理プロセッサ）設計提携
  - AI資源重点: 豆包→企業サービスへ移行
- **引用URL:** https://hk.finance.yahoo.com/news/%E5%AD%97%E7%AF%80%E8%B7%B3%E5%8B%95%E6%B4%BD%E8%AB%92200%E5%84%84%E7%BE%8E%E5%85%83%E9%9B%A2%E5%B2%B8%E8%B2%B8%E6%AC%BE-%E6%88%96%E5%89%B5%E6%AD%B7%E5%8F%B2%E6%96%B0%E9%AB%98-065016434.html
- **Evidence ID:** EVD-20260701-0062

### INFO-063
- **タイトル:** 米中AI競争の「3つのモデル」: 民主的リード vs 技術主権主義 vs 相互依存管理
- **ソース:** AI Frontiers (CNAS)
- **公開日:** 2026-06-30
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** (米中政府)
- **要約:** CNAS分析で米中AI競争の3つのモデルを提示: (1)民主主義陣営のリード維持、(2)技術主権主義による完全デカップリング、(3)相互依存管理。米国の指導者はAI競争が中国との力の均衡を形作ると同意するが、確保方法で意見が割れている。AI安全性の国際的議論で安全保障が政治的に不快に。
- **キーファクト:**
  - 3つの競争モデル: 民主的リード・技術主権主義・相互依存管理
  -安全保障: 国際AI議論で政治的に不快（国家利益の対立露呈）
  - AI標準設定の主導権が大西洋両岸で連携中
- **引用URL:** https://ai-frontiers.org/articles/three-models-of-sino-american-competition-for-the-soul-of-ai
- **Evidence ID:** EVD-20260701-0063

### INFO-064
- **タイトル:** Yann LeCunがxAIを「失敗気味」、ハードウェアより研究者が重要と主張
- **ソース:** Instagram / CNBC
- **公開日:** 2026-06-28
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Meta, xAI
- **要約:** Meta首席AI科学者Yann LeCunがxAIを「失敗気味」と評。フロンティアAIは最もハードウェアを持つ者が勝つのではなく、最高の研究者を保持する者が勝つと主張。信頼できるAIエージェントにはワールドモデル（行動が結果にどう繋がるかの内部理解）が必要と主張。
- **キーファクト:**
  - LeCun: xAIは「失敗気味」
  - フロンティアAI勝者: ハードウェア量ではなく研究者の質
  - 信頼できるAI: ワールドモデル（行動→結果の内部理解）が必要
- **引用URL:** https://www.instagram.com/reel/DaA9M-uKc5z/
- **Evidence ID:** EVD-20260701-0064

---

## 【Step 4: 重要記事詳細スクレイピング結果】

### INFO-065
- **タイトル:** OpenAI GPT-5.6Sol/Terra/Luna発表: 3階層モデル、限定的プレビュー（米政府調整）
- **ソース:** VentureBeat
- **公開日:** 2026-06-26
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-001-01, KIQ-005-03
- **関連企業:** OpenAI, Cerebras
- **要約:** OpenAIがGPT-5.6シリーズ（Sol/Terra/Luna）を発表。3階層で異なる用途に最適化。Trump政権の6月2日大統領令に基づく連邦政府の安全性審査プロセス（30日間）に従い、約20組織のみに限定プレビュー提供。一般提供は「数週間以内」。新命名体系: 番号=世代、名前=能力ティア。
- **キーファクト:**
  - **Sol**（最上位）: 複雑コーディング・セキュリティ研究、$5/$30 per M tokens（GPT-5.5と同額）
  - **Terra**（中位）: 高ボリューム業務、$2.50/$15 per M tokens
  - **Luna**（最廉価）: 日常タスク・要約、$1/$6 per M tokens
  - TerminalBench 2.1: Sol ultra mode 91.91%（新記録）、max mode 88.76%、GPT-5.5 83.4%、Mythos 5 88%
  - Agent's Last Exam: Sol 50.9%（唯一50%超え）
  - ExploitBench: Sol ≈ Mythos Previewの性能を1/3のtokenで達成
  - 全3モデル「High」リスク分類（サイバー・バイオ/ケミカル）
  - レッドチーム: 700,000 A100e GPU時間
  - Cerebras提携: 750 tokens/sec（7月開始予定）
  - プロンプトキャッシュ: 初期書込1.25x、再読90%割引、30分最小保証
  - 価格表でGLM-5.2($5.80)は最安フロンティア、Sol($35.00)はClaude Fable 5/Mythos 5($60.00)の半額
- **引用URL:** https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov
- **Evidence ID:** EVD-20260701-0065

### INFO-066
- **タイトル:** 豆包2.1 ProがClaude Opus 4.6を複数ベンチで上回る、Seedance ARR $20億は否定
- **ソース:** 東方財富 / 毎日経済新聞
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, BYTEDANCE-CHINESE, KIQ-003-02
- **関連企業:** ByteDance
- **要約:** 豆包2.1 ProがCoding/Agent/VLM三大方向で能力躍升、Terminal Bench 2.1・SWE-Pro・SciCode等でClaude Opus 4.6を上回る。チップ設計RTLテストで18時間連続稼働・9ラウンド反復で完全プロセスを完走。3D仮想都市で500+ Agent同時協調・1000+ラウンドツール呼出・100棟超建築モデル生成。火山引擎总裁譚待はSeedance ARR $20億の噂を否定「伝えられている数字は全て誤りで、高すぎる」。
- **キーファクト:**
  - 豆包2.1 Pro: Claude Opus 4.6を複数ベンチマークで上回る
  - RTLテスト: 18時間連続・9ラウンド反復で完全プロセス完走
  - Agent協調: 500+ Agent同時、1000+ラウンドツール呼出
  - 豆包2.1 Pro API価格: ¥6/M入力、¥30/M出力、¥1.2/Mキャッシュ（Claude Opus 4.6比80%安）
  - Seedance ARR $20億: 公式否定（「誤りで高すぎる」）
  - 豆包2.1 Turbo: 2.1 Proの半額
  - 「質変点」概念: Claude Opus 4.6がCoding/Agent領域で初の質変点通過モデル
  - 中国競合: GLM-5.2・Kimi K2.6/K2.7 Code・Qwen3.7-Plus全てCoding/Agent集中
- **引用URL:** https://finance.eastmoney.com/a/202606253783359647.html
- **Evidence ID:** EVD-20260701-0066

### INFO-067
- **タイトル:** DeepSeek V4技術詳細: V4-Flash(284B/13B)・V4-Pro(1.6T/49B)、DSparkでQwen3/Gemma4にも対応
- **ソース:** VentureBeat / DeepSeek技術論文
- **公開日:** 2026-06-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek, Alibaba, Google
- **要約:** DeepSeekのDSpark技術詳細。V4-Flashは284B総パラメータ・13B活性化、V4-Proは1.6T総パラメータ・49B活性化、両者とも1Mコンテキスト対応。DSparkは半自己回帰生成と信頼度スケジュール検証を組み合わせ、V4-Flashでユーザーあたり60-85%高速化。V4-Proで57-78%。Qwen3-4B/8B/14B・Gemma4-12Bでも有効（Eagle3比30.9%改善）。MIT Licenseで完全オープンソース。
- **キーファクト:**
  - V4-Flash: 284B総パラメータ・13B活性化（効率MoE）
  - V4-Pro: 1.6T総パラメータ・49B活性化
  - コンテキストウィンドウ: 両方1M
  - DSparkユーザー速度向上: V4-Flash 60-85%、V4-Pro 57-78%
  - スループット向上: V4-Flash +51%、V4-Pro +52%（80/35 tok/sec目標時）
  - 厳格ターゲット時: V4-Flash +661%、V4-Pro +406%（120/50 tok/sec目標）
  - Qwen3改善: Eagle3比+30.9%(4B)/+26.7%(8B)/+30.0%(14B)
  - コミュニティテスト: 26.33→39.88→~60 tok/sec（非スペック比2.3x）
  - トレーニング要件: ~38TBキャッシュ、8GPU/ノード
  - MIT License、HuggingFace・GitHub公開
- **引用URL:** https://venturebeat.com/orchestration/deepseek-open-sources-dspark-a-new-framework-to-speed-up-llm-inference-by-up-to-85
- **Evidence ID:** EVD-20260701-0067

### INFO-068
- **タイトル:** Fordが350人のベテランエンジニア再雇用: AI品質不十分で「gray beard」復帰、数億ドルコスト削減
- **ソース:** TechCrunch / Bloomberg
- **公開日:** 2026-06-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Ford
- **要約:** FordがAI・自動品質管理システムの成果不十分を受け、350人のベテランエンジニア（「gray beard」）を再雇用。VP Charles Poon: 「AIを導入するだけで高品質製品ができると思っていたのは誤り」。再雇用エンジニアは若手育成とAIツール再プログラムを担当。結果: 保証・リコールコスト低下で「数億ドル」のコスト削減効果、JD Power品質調査メインストリームブランド1位。
- **キーファクト:**
  - 再雇用: 350人のベテランエンジニア（元従業員・サプライヤー勤務者含む）
  - COO Kumar Galhotra: 自動品質システムへの依存に失望
  - VP Poon: 「AI導入だけで高品質製品ができると思ったのは誤り」
  - 役割: 若手育成＋AIツールの再プログラム
  - 成果: 保証・リコールコスト「数億ドル」削減
  - JD Power Initial Quality Survey: メインストリームブランド1位
- **引用URL:** https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/
- **Evidence ID:** EVD-20260701-0068

### INFO-069
- **タイトル:** Anthropic輸出禁止継続中: 中国360がMythos対抗AI「Tulongfeng」、東京Sakanaが「Fugu」発表
- **ソース:** TechCrunch / Reuters
- **公開日:** 2026-06-27
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03, H-GOV-001
- **関連企業:** Anthropic, Sakana AI, 360 Security
- **要約:** AnthropicのFable 5/Mythos 5輸出禁止措置継続中（2週間経過）、アジア企業が代替製品を急速に投入。中国360が脆弱性発見AI「Tulongfeng」と自動サイバー防御「Yitianzhen」を発表（Mythos対抗を主張）。東京Sakana AIが「Fugu」を発表（Fable 5/Mythos Previewと同等を主張）、複数モデルAPIオーケストレーション対応。Sakana: 「アクセスは一晩で消え得る、集合知がリスク回避策」。Anthropicの$47B年率収益のアジア依存度は非公開。
- **キーファクト:**
  - 中国360: Tulongfeng（脆弱性発見AI）+ Yitianzhen（自動サイバー防御）
  - 360創業者周鴻禕: 脆弱性発見AIは国家戦略資産、「一方向透明性」リスク警告
  - Sakana Fugu: Fable 5/Mythos Previewと同等性能を主張、APIオーケストレーション対応
  - Sakana創業者: David Ha・Llion Jones（Google出身）、Ren Ito（Mercari/Stability AI出身）
  - Sakana: G7サミットで「アクセス維持が優先事項」を主張
  - David Ha: 「単一プロバイダーへの依存はリスク、集合知がヘッジ」
  - Anthropic $47B年率収益: アジア企業依存度は非公開
  - 輸出禁止2週間経過: ローカル代替が既にギャップを埋めつつある
- **引用URL:** https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/
- **Evidence ID:** EVD-20260701-0069

### INFO-070
- **タイトル:** Claude Sonnet 5発表: 「最もアジェントなSonnet」、Opus比60%安でIPO前の攻勢
- **ソース:** VentureBeat / Anthropic
- **公開日:** 2026-06-30
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-001-02, KIQ-003-01
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Sonnet 5を発表。「最もアジェントなSonnetモデル」。Free/Proプランのデフォルトモデル。API価格は期間限定($2/$10 per M tokens)、9月以降$3/$15へ（Claude Opus 4.8の$5/$25より大幅に安価）。IPO前の収益成長加速狙い。
- **キーファクト:**
  - Claude Sonnet 5: 「最もアジェントなSonnetモデル」
  - デフォルト: Free/Proプラン（Max/Team/Enterpriseも利用可）
  - API期間限定価格: $2/M入力・$10/M出力（8月31日まで）
  - 通常価格: $3/M入力・$15/M出力（Opus 4.8の$5/$25の60%引）
  - IPO前の収益攻勢
- **引用URL:** https://venturebeat.com/technology/anthropic-launches-claude-sonnet-5-at-a-steep-discount-to-its-top-model-as-the-company-races-toward-a-blockbuster-ipo
- **Evidence ID:** EVD-20260701-0070

### INFO-071
- **タイトル:** Alibaba動画生成AIが世界#2に上昇、OpenAI Sora中止・ByteDance Seedance国際展開凍結で競争地盤激変
- **ソース:** VentureBeat
- **公開日:** 2026-06-22
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-04
- **関連企業:** Alibaba, OpenAI (Sora), ByteDance (Seedance)
- **要約:** AlibabaのAI動画生成モデルが世界ランキング#2に上昇。OpenAIがSoraを財政的に持続不可能として中止、ByteDanceがハリウッド著作権訴訟でSeedance 2.0の国際展開を無期限凍結。企業調達チームが評価/統合していたツールが数ヶ月で競争地盤が激変。
- **キーファクト:**
  - Alibaba動画生成AI: 世界ランキング#2上昇
  - OpenAI Sora: 財政的に持続不可能として中止（discontinued）
  - ByteDance Seedance 2.0: 国際展開を無期限凍結（ハリウッド著作権訴訟）
  - エンタープライズ調達: マーケティング/広告/コンテンツ制作ワークフロー影響大
- **引用URL:** https://venturebeat.com/technology/alibabas-ai-video-model-rises-to-no-2-in-global-rankings-as-openais-sora-and-bytedances-seedance-fall-away
- **Evidence ID:** EVD-20260701-0071

### INFO-072
- **タイトル:** Google Nano Banana 2 Lite発表: 高速低コスト画像生成、Gemini Omni Flashで動画会話型生成
- **ソース:** TechCrunch / VentureBeat
- **公開日:** 2026-06-30
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-001-03
- **関連企業:** Google
- **要約:** GoogleがNano Banana 2 Lite（別名Gemini 3.1 Flash-Lite）を発表。高速低コスト企業向け画像生成（4秒）。Gemini Omni Flashも発表: 平易な指示で動画生成・修正・編集が可能、フィルムクルー/エディター/複数修正ラウンドを不要にする。
- **キーファクト:**
  - Nano Banana 2 Lite (Gemini 3.1 Flash-Lite): 4秒・低コスト画像生成
  - Gemini Omni Flash: 会話型動画生成・修正・編集
  - 企業向け: マルチツールパイプラインを置き換え可能
- **引用URL:** https://techcrunch.com/2026/06/30/google-introduces-a-faster-cheaper-image-generator-with-nano-banana-2-lite/
- **Evidence ID:** EVD-20260701-0072

### INFO-073
- **タイトル:** Meituan LongCat 2.0: 1.6Tパラメータ・中国チップ全訓練・OpenRouterリードのオープンソースモデル
- **ソース:** VentureBeat
- **公開日:** 2026-06-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meituan
- **要約:** MeituanがLongCat 2.0をオープンソース化（MIT License）。1.6Tパラメータのフロンティア級アジェントコーディングモデル。OpenRouterでリード。中国産チップのみで完全訓練。MIT Licenseで企業統合の最大柔軟性。
- **キーファクト:**
  - LongCat 2.0: 1.6Tパラメータ
  - OpenRouterランキング1位（オープンウェイト）
  - 中国産チップのみで完全訓練
  - MIT License
  - フロンティア級アジェントコーディング性能
- **引用URL:** https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips
- **Evidence ID:** EVD-20260701-0073

### INFO-074
- **タイトル:** WEF報告詳細: 若年労働者37%がAI中高露出、スキル28%が3年で陳腐化、Indeed若手求人-7%
- **ソース:** World Economic Forum / Indeed
- **公開日:** 2026-06-24
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-004-03
- **関連企業:** Indeed, NYU, dentsu, Randstad
- **要約:** WEF新報告の詳細データ。若年労働者の37%がAI中高露出職種、一部地域では75%。エントリーレベル労働者の28%が3年以内に現在のスキルの半分以下しか関連性がないと認識。Indeed: ジュニア求人が2025年にYoY -7%、シニアは+4%。新規卒業生失業率5.7%（3年高、2025年Q4）。推奨: 「human first」ルール、レビュー/エディター役割へのシフト、シニアとの協調的問題解決。
- **キーファクト:**
  - 若年労働者37%: AI中高露出職種（一部地域は75%）
  - 28%: 3年内にスキルの半分以下が関連すると認識
  - Indeed: ジュニア求人-7% YoY（2025年）、シニア+4%
  - 新規卒業生失業率: 5.7%（3年高、Q4 2025）
  - NYU: 「エントリーレベルを取捨すると将来のマネージャー・リーダー・組織的記憶のパイプラインを破壊」
  - Indeed VP: ジュニアがAI下請けになると「事業がどう機能するか学べない」
  - 推奨戦略: human-first rule、review/editorへのシフト、collaborative problem solving
  - Randstad: 「AI時代ほど人間の判断力が価値を持つ」
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-decimate-entry-level-jobs-expert-insights/
- **Evidence ID:** EVD-20260701-0074

### INFO-075
- **タイトル:** Arena AI詳細: UC Berkeley発、$250M調達、Ion Stoica共同創業、Scale AI/Mercorと競合
- **ソース:** TechCrunch
- **公開日:** 2026-06-29
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** Arena (LMArena)
- **要約:** Arena（旧LMArena）の詳細。UC Berkeley研究プロジェクト発（2023年）。8ヶ月で$100M ARR到達（商業化は2025年9月開始）。1000万+ユーザー評価。$150M Series A（$1.7B評価、2026年1月）。共同創業者: Anastasios Angelopoulos(CEO)・Wei-Lin Chiang(CTO)・Ion Stoica(UC Berkeley教授/Databricks共同創業者)。Scale AI・Mercor・Surgeと同一ドルを競争。Yuppは3月に閉鎖。
- **キーファクト:**
  - $100M ARR: 8ヶ月で到達（商業化2025年9月開始）
  - $30M ARR: 2026年1月時点
  - 調達総額: $250M（a16z・Kleiner Perkins・Lightspeed等）
  - 評価額: $1.7B（2026年1月Series A）
  - 10M+ユーザー評価
  - 共同創業者: Angelopoulos・Chiang・Stoica（Databricks共同創業者）
  - 競合: Scale AI・Mercor・Surge（人手ラベリング）
  - Yupp（競合）: 2026年3月に閉鎖
  - 収益モデル: 消費型（非リカーリング）
- **引用URL:** https://techcrunch.com/2026/06/29/arena-the-ai-leaderboard-everyone-uses-is-now-a-100m-business/
- **Evidence ID:** EVD-20260701-0075
