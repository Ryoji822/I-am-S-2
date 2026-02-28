# 収集データ: 2026-02-28

## メタデータ
- 収集日時: 2026-02-28 00:00 UTC
- 実行クエリ数: 42 / 56
- scrape実行数: 12件
- 収集情報数: 19件
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-05 ✓, KIQ-002-02 ✓, KIQ-003-02 ✓, KIQ-003-04 ✓, KIQ-005-02 ✓, BYTEDANCE-CHINESE ✓
- 動的追加クエリ: KIQ-RED-001 (MCP採用率), KIQ-RED-002 (Skills vs Claude Code), KIQ-RED-005 (ROI失敗理由), KIQ-RED-006 (Vercept統合), KIQ-RED-007 (政府契約競合)
- 品質フラグ: PARTIAL (19/50件、主要KIQはカバー済み)

## 収集結果

### INFO-001
- **タイトル:** Anthropic's Responsible Scaling Policy: Version 3.0
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-02-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** RSP v3.0を公開。企業単独の緩和策と業界全体の推奨策を分離、Frontier Safety Roadmap導入、Risk Reports（3-6ヶ月ごと）と外部レビュー制度を新設。ASL-3は実装済みだが、生物リスク評価の「曖昧な領域」と政府対応の遅れが課題。
- **キーファクト:**
  - ASL-3対策（化学・生物兵器対策）は2025年5月に有効化済み
  - 高ASL（4以降）は単独実装困難、国家セキュリティコミュニティの支援が必要（RAND報告引用）
  - Risk Reportsを3-6ヶ月ごとに公開、特定条件で外部専門家レビュー必須
  - Frontier Safety Roadmapに「月箭R&D」「自動化レッドチーミング」「規制ラダー」等の目標
- **引用URL:** https://www.anthropic.com/news/responsible-scaling-policy-v3

### INFO-002
- **タイトル:** Claude for Financial Services
- **ソース:** Anthropic公式ブログ
- **公開日:** 2025-07-15
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** 金融業界向け包括ソリューションを発表。S&P Global、FactSet、PitchBook等とのMCPコネクタ、拡張利用制限付きClaude Code、AWS Marketplaceで調達可能。NBIM（ノルウェー政府年金基金）で20%生産性向上（213,000時間相当）。
- **キーファクト:**
  - Claude 4はVals AI Finance Agent benchmarkで他フロンティアモデルを上回る
  - Claude Opus 4はFinancial Modeling World Cup 7段階中5段階クリア
  - パートナー: Box, Daloopa, Databricks, FactSet, Morningstar, Palantir, PitchBook, S&P Global, Snowflake
  - NBIM: 20%生産性向上=213,000時間相当、9,000社のニュースフロー自動監視
  - AIG: アンダーライティング5倍高速化、データ精度75%→90%以上
- **引用URL:** https://www.anthropic.com/news/claude-for-financial-services

### INFO-003
- **タイトル:** Updates to Consumer Terms and Privacy Policy
- **ソース:** Anthropic公式ブログ
- **公開日:** 2025-08-28
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** Consumer Terms更新。Free/Pro/Maxユーザーにモデル訓練へのデータ使用選択肢を提供。訓練許可時はデータ保持期間を30日→5年に延長。Commercial Terms（API、Bedrock、Vertex AI）には適用外。
- **キーファクト:**
  - 既存ユーザーは2025年10月8日までに選択必要
  - 商用利用（Claude for Work/Gov/Education、API）は対象外
  - 5年保持は新規/再開チャットのみ適用、削除会話は訓練に使用しない
  - Clio等の自動処理でセンシティブデータをフィルタリング
- **引用URL:** https://www.anthropic.com/news/updates-to-our-consumer-terms

### INFO-004
- **タイトル:** Grok-2 Beta Release
- **ソース:** xAI公式ブログ
- **公開日:** 2024-08-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** xAI
- **要約:** Grok-2とGrok-2 miniをβリリース。LMSYS Chatbot Arenaで「sus-column-r」としてテスト、Claude 3.5 SonnetとGPT-4-Turboを上回るEloスコア。GPQA 56%、MMLU 87.5%、MATH 76.1%。Enterprise APIも同月公開予定。
- **キーファクト:**
  - Chatbot ArenaでClaude/GPT-4を上回るEloスコア
  - ビジョンタスク: MathVista 69.0%、DocVQA 93.6%
  - X Premium/Premium+で利用可能
  - Black Forest LabsのFLUX.1モデルで画像生成統合実験中
  - Enterprise API: 多要素認証必須、管理API提供
- **引用URL:** https://x.ai/blog/grok-2

### INFO-005
- **タイトル:** Claude Agent SDK v0.2.58 Released
- **ソース:** GitHub
- **公開日:** 2026-02-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK最新版v0.2.58公開。Claude Code v2.1.58とパリティ。v0.2.51でBunバイナリでのクラッシュ修正、メモリリーク修正、task_progressイベント追加等の重要修正を実施。
- **キーファクト:**
  - v0.2.53: listSessions()追加で過去セッションの検出・一覧表示が可能に
  - v0.2.51: Bunコンパイル済みバイナリでのReferenceError修正、長時間実行でのメモリ増大修正
  - v0.2.49: supportsEffort/supportedEffortLevels/supportsAdaptiveThinkingフィールド追加
  - v0.2.47: promptSuggestion()メソッド追加
  - v0.2.45: Claude Sonnet 4.6サポート追加、task_startedイベント追加
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases

### INFO-006
- **タイトル:** Grok 4.2 Status: Public Beta Signals
- **ソース:** Data Studios
- **公開日:** 2026-02-23
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI
- **要約:** Grok 4.2はパブリックβとしてオプイン選択で展開中。xAIのエージェントツールシステム（サーバーサイドツール、検索引用、ファイル添付検索）の技術基盤を解説。「Grok 420 Multi-Agent」がAPIロードマップに存在。
- **キーファクト:**
  - Grok 4.2はデフォルトではなくモデルピッカーで明示選択必要
  - サーバーサイドツール: Web検索、X検索、コード実行、ドキュメント検索が統合
  - ファイル添付最大48MB、添付でdocument search toolが自動起動
  - Grok 420 Early Access、Grok 420 Multi-Agentが「API coming soon」と公式記載
  - Grok 4はreasoning modelとして一部パラメータが非対応
- **引用URL:** https://www.datastudios.org/post/grok-4-2-status-public-beta-signals-agentic-tooling-model-picker-reality-and-what-is-technically

### INFO-007
- **タイトル:** ByteDance Prepares China's Next AI Shock
- **ソース:** Trending Topics
- **公開日:** 2026-02-20
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** ByteDance
- **要約:** ByteDanceのDola-Seed-2.0がArena.aiプレビューでGrok-4.1を上回る順位。Seed 2.0シリーズ（Pro/Lite/Mini/Code）はコスト効率（トークン価格が競合の約1/10）を売り。マルチモーダル・エージェント能力でGPT-5.2やGemini 3 Proに匹敵。
- **キーファクト:**
  - Dola-Seed-2.0はArena.aiプレビューでGrok-4.1、Gemini 3、Claude Opus 4.5より上位
  - Seed 2.0 Pro: MathVista/MathVision/LogicVista等の視覚推論ベンチマークで業界トップ
  - SuperGPQAでGPT-5.2を上回る、科学ベンチマークでGemini 3 Pro相当
  - トークン価格は競合の約1/10
  - Seedance 2.0は著作権問題で著名人・著作権キャラクター生成を制限
- **引用URL:** https://www.trendingtopics.eu/bytedance-prepares-chinas-next-ai-shock/

### INFO-008
- **タイトル:** Claude Code for Enterprise
- **ソース:** Anthropic
- **公開日:** 2026-02-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Code Enterprise版の詳細公開。SOC 2 Type II準拠、SSO/SCIM、ロールベース権限、組織全体ポリシー適用を提供。Zapierで89%従業員採用、800以上のAIエージェントデプロイ。Rakutenで市場投入時間79%短縮（24日→5日）。
- **キーファクト:**
  - セキュリティ: SOC 2 Type II、TLS 1.3（転送中）、AES-256（保存時）、BYOK対応
  - デプロイ: AWS Bedrock、Google Vertex AI、Microsoft Foundry、VPC分離・プライベートエンドポイント
  - OpenTelemetryでリアルタイムメトリクス出力
  - 顧客事例: Notion、Zapier（89%採用）、Ramp（1M+行実装）、HubSpot、Shopify、Wiz、Spotify、Rakuten
  - Rakuten: 機能市場投入時間79%短縮（24日→5日）、複雑コード修正99.9%精度
- **引用URL:** https://claude.com/product/claude-code/enterprise

### INFO-009
- **タイトル:** AI ROI: High Investment, Low Returns
- **ソース:** Deloitte
- **公開日:** 2026-02-26
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** AI投資は増加（85%が増額、91%が今年も増額予定）だがROI実現率は低い（6%のみが1年以内に回収）。予算の93%が技術、7%のみが人・ワークフローに配分。CIBCでGitHub Copilot導入、10-14%生産性向上・90%採用率達成。
- **キーファクト:**
  - AI予算の93%が技術、7%のみが人・ワークフロー
  - 85%がAI投資増額、91%が今年も増額予定
  - 6%のみが1年以内にROI回収
  - エージェントAIの本番デプロイ成功は11%のみ
  - CIBC: 1,800+開発者でGitHub Copilot導入、10-14%生産性向上、90%採用率
  - 76%の経営幹部が「従業員は熱心」と回答、実際は31%のみが同意
- **引用URL:** https://www.deloitte.com/ca/en/Industries/financial-services/perspectives/ai-adoption-roi-success.html

### INFO-010
- **タイトル:** 字节跳动旗下AI聊天机器人农历新年假期斩获1亿用户
- **ソース:** 联合早报
- **公開日:** 2026-02-25
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-02
- **関連企業:** ByteDance
- **要約:** ByteDanceの豆包（Doubao）チャットボットが中国農暦新年期間に日次アクティブユーザー1億人を突破。中央電視台春晩との提携で19億件以上のAIクエリを処理。阿里千問は3,000万、騰訊元宝は5,000万にとどまる。
- **キーファクト:**
  - 豆包: 農暦除夕（2/16）にDAU 1億人突破、2月初の4倍
  - 春晩放送中に19億件以上のAI関連クエリを処理
  - 阿里千問: 30億元投資、DAU 3,000万（除夕）
  - 騰訊元宝: 10億元投資、DAU 5,000万（除夕）
  - 業界全体で農暦新年期間に80億元以上を投資
  - 専門家: 紅包ドリブンの7日リテンションは20%以下、30日で5%以下
- **引用URL:** https://www.zaobao.com.sg/news/china/story20260225-8637632

### INFO-011
- **タイトル:** Gemini 3.1 Pro Hits Record Reasoning Gains
- **ソース:** Unite.AI
- **公開日:** 2026-02-27
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Google
- **要約:** Gemini 3.1 Proが18ベンチマーク中12で1位獲得。ARC-AGI-2で前世代比2倍の77.1%、GPQA Diamond 94.3%。MMLU-Pro 91.2%、HumanEval 96.4%。
- **キーファクト:**
  - ARC-AGI-2: 77.1%（Gemini 3 Proの2倍）
  - GPQA Diamond: 94.3%（業界トップ）
  - MMLU-Pro: 91.2%
  - HumanEval: 96.4%
  - 18追跡ベンチマーク中12で1位
- **引用URL:** https://www.unite.ai/gemini-3-1-pro-hits-record-reasoning-gains/

### INFO-012
- **タイトル:** Skills + Shell + Compaction: Building Auditable Workcells
- **ソース:** LinkedIn (Rohit Sharma)
- **公開日:** 2026-02-24
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIのSkills/Shell/Compactionスタックの実践的解説。Skillsでバージョン管理可能なSOP、Shellでサンドボックス実行環境、Compactionで長期実行時のコンテキスト管理。監査可能なワークセル構築パターン。
- **キーファクト:**
  - Skills: 各ワークフローを独立したバージョン管理可能なSOPバンドルに分離
  - Shell: container_auto（単発実行）/container_reference（永続的マルチターン）の2モード
  - Compaction: トークン閾値超過で自動発火、手動要約不要
  - 監査証跡: container ID、response ID、skill ID/バージョン、shellコマンド、ファイルハッシュ
  - 月次OpsレビューPOC: 5スキル、8ターン、QAゲート、署名付きZIP出力
- **引用URL:** https://www.linkedin.com/pulse/skills-shell-compaction-practical-pattern-building-auditable-sharma-jwrvc

### INFO-013
- **タイトル:** AGI Timeline: Sam Altman Predicts 2028
- **ソース:** Multiple Sources
- **公開日:** 2026-02-27
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Google DeepMind
- **要約:** Sam Altmanが「2028年末までに人類の知的能力の大部分がデータセンター内に存在する可能性」と予測。Demis Hassabisは2030年までに50%の確率でAGIと予測。Yann LeCunは懐疑的。
- **キーファクト:**
  - Sam Altman: 2028年末までにスーパーインテリジェンス到達の可能性
  - Demis Hassabis: 2030年までにAGI到達50%確率、2031-2036の範囲も示唆
  - 2023年調査: 2,778研究者の50%が人間レベル機械知能を2040年代と予測
  - 起業家はより楽観的、研究者はより保守的
- **引用URL:** https://www.medianama.com/2026/02/223-superintelligence-within-years-sam-altman-meta-ai-scientist-disagrees/

### INFO-014
- **タイトル:** MCP Governance: Cloudflare Warns of Shadow MCP
- **ソース:** Cloudflare
- **公開日:** 2026-02-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** （業界全体）
- **要約:** CloudflareがMCPガバナンスドキュメント公開。MCP採用拡大に伴い、シャドーMCP（非承認サーバー）問題が顕在化。ガバナンスフレームワークの必要性を提唱。
- **キーファクト:**
  - MCP: LLMが独自データ・内部ツールと対話するためのクライアントサーバープロトコル
  - MCP.so等のディレクトリに数万のコミュニティ構築サーバー
  - Microsoft、Azure Functions、GitHub等がMCP対応
  - シャドーMCP問題: 非承認サーバーによるデータ漏洩リスク
  - ガバナンス: 承認サーバーのみ許可、監査ログ、アクセス制御
- **引用URL:** https://developers.cloudflare.com/agents/model-context-protocol/governance/

### INFO-015
- **タイトル:** AI Funding: World Labs $1B, Basis $100M
- **ソース:** Crunchbase, Reuters
- **公開日:** 2026-02-27
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** World Labs, Basis
- **要約:** World Labs（3D世界と対話するAIモデル）が10億ドル調達。Basis（AI会計スタートアップ）が1億ドル調達、評価額11.5億ドル。SolveAIが8ヶ月で5,000万ドル調達。
- **キーファクト:**
  - World Labs: 10億ドル調達、3D世界対話AIモデル開発
  - Basis: 1億ドルSeries B、評価額11.5億ドル、AI会計エージェント
  - SolveAI: 8ヶ月で5,000万ドル、Google Ventures主導
  - Axelera AI: 2.5億ドル以上、EU最大のAIハードウェア投資
  - エージェントAI分野への投資が加速
- **引用URL:** https://news.crunchbase.com/venture/biggest-funding-rounds-cloud-energy-ai-world-labs/

### INFO-016
- **タイトル:** Anthropic Statement on Department of War Discussions
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-02-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-RED-007
- **関連企業:** Anthropic
- **要約:** Dario Amodei CEOが国防部門との協力に関する声明。2つの例外（大量国内監視、完全自律兵器）でセーフガード維持を拒否。契約額2億ドル、サプライチェーンリスク指定の脅威を受けるも立場維持。
- **キーファクト:**
  - Anthropicは米政府の機密ネットワークに初めてモデル展開したフロンティアAI企業
  - 国防部門は「いかなる合法的使用」にも応じるAI企業のみと契約すると表明
  - 2つの拒否: (1)大量国内監視、(2)完全自律兵器（現在の技術では信頼性不足）
  - 契約額: 最大2億ドル
  - 脅威: サプライチェーンリスク指定、国防生産法発動
  - 中国共産党関連企業への販売停止で数億ドルの収益放棄済み
- **引用URL:** https://www.anthropic.com/news/statement-department-of-war

### INFO-017
- **タイトル:** State of MCP Ecosystem: 2026 Report
- **ソース:** Ooty
- **公開日:** 2026-02-22
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-RED-001
- **関連企業:** （業界全体）
- **要約:** MCP（Model Context Protocol）の2026年状況レポート。SDK月間ダウンロード9,700万、アクティブサーバー1万以上、Fortune 500の80%がAIエージェントを本番展開。セキュリティ問題（ツールポイズニング、ラグプル攻撃）も顕在化。
- **キーファクト:**
  - SDK月間ダウンロード: 9,700万（Python + TypeScript）
  - アクティブサーバー: 10,000以上（MCP.soは17,000以上）
  - Fortune 500の80%がアクティブAIエージェントを本番展開
  - プラットフォーム採用: OpenAI（2025年3月）、Google（4月）、Microsoft（5月）
  - 2025年12月: Linux FoundationのAgentic AI Foundationに寄贈
  - セキュリティ: 492の公開MCPサーバーが認証欠落で脆弱
  - コスト削減: オンデマンドデータフェッチで最大70%
- **引用URL:** https://ooty.io/blog/state-of-mcp-ecosystem-2026

### INFO-018
- **タイトル:** Claude Code vs Codex: Enterprise Adoption Comparison
- **ソース:** LinkedIn, TechBuzz
- **公開日:** 2026-02-24
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-RED-002
- **関連企業:** Anthropic, OpenAI
- **要約:** Claude Codeが業界横断で大規模採用。非開発者もターミナルアクセスを学んで使用。OpenAI CodexはClaude Desktop/Claude Codeに遅れを取るとの評価。
- **キーファクト:**
  - Claude Code: 非開発者がターミナルアクセスを学んで使用するほどの製品市場適合
  - 業界横断採用: 技術企業以外でも広がり
  - 比較評価: OpenAI CodexはClaude Codeに大きく遅れ
  - GPTシリーズはAnthropic競合製品に実質的に遅れ
- **引用URL:** https://www.techbuzz.ai/articles/claude-code-cracks-product-market-fit-across-industries

### INFO-019
- **タイトル:** Enterprise AI ROI: 95% of POCs Fail
- **ソース:** TFIR, Portal26
- **公開日:** 2026-02-26
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-RED-005, KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** Portal26 CEOインタビュー。エンタープライズAIプロジェクトの95%が失敗。原因はデータ準備不足、セキュリティ、可視性欠如。AI投資の42%が現在失敗中。
- **キーファクト:**
  - エンタープライズAI POC失敗率: 95%
  - AI投資の42%が現在失敗中
  - 組織の88%がAI使用中
  - 主な失敗原因: データ準備不足、セキュリティ、可視性欠如
  - 解決策: AI可視性、セキュリティ、価値実現の統合
- **引用URL:** https://tfir.io/enterprise-ai-roi-portal26-arti-raman/
