# 収集データ: 2026-07-14

## メタデータ
- 収集日時: 2026-07-14 00:00 UTC
- 品質フラグ: COMPLETE
- INFO総数: 78
- 検索クエリ実行数: 約110（collection_plan.json全KIQ + Arbiter動的7KIQ）
- ディープスクレイプ数: 3（AI Safety Index Summer 2026 / HBR vendor lock-in / Medium OSS vs closed）
- ソース信頼性分布: A-1: 1, A-2: 1, A-3: 15, B-1: 3, B-2: 56, C: 2

### KIQカバレッジ
| KIQ | INFO数 | 状態 |
|-----|--------|------|
| KIQ-001-01 (エージェント市場) | 7+3 | ✅ |
| KIQ-001-02 (企業セキュリティ) | 5+1 | ✅ |
| KIQ-001-03 (エコシステム/MCP) | 6 | ✅ |
| KIQ-001-04 (マルチモーダル) | 5 | ✅ |
| KIQ-001-05 (スキル/実行環境) | 5 | ✅ |
| KIQ-002-01 (規制) | 4 | ✅ |
| KIQ-002-02 (企業導入) | 4 | ✅ |
| KIQ-002-03 (規制安全基準) | 5+1 | ✅ |
| KIQ-002-04 (自動化影響) | 5 | ✅ |
| KIQ-002-05 (広告産業構造変化) | 5+1 | ✅ |
| KIQ-002-06 (政府・軍事) | 8 | ✅ |
| KIQ-003-01 (API価格) | 5 | ✅ |
| KIQ-003-02 (ベンチマーク) | 5 | ✅ |
| KIQ-003-03 (OSS vs商用) | 5+1 | ✅ |
| KIQ-003-04 (資金調達) | 5 | ✅ |
| KIQ-003-05 (ベンダーロックイン) | 4+1 | ✅ |
| KIQ-004-01 (自動化完全化) | 5+1 | ✅ |
| KIQ-004-02 (コーディング価値変化) | 5 | ✅ |
| KIQ-004-03 (代替困難能力) | 5 | ✅ |
| KIQ-004-04 (勝者パターン) | 4 | ✅ |
| KIQ-005-01 (AGI進展) | 5 | ✅ |
| KIQ-005-02 (AGIタイムライン) | 4+1 | ✅ |
| KIQ-005-03 (AGI安全性) | 4+1 | ✅ |
| BYTEDANCE-CHINESE | 6+1 | ✅ |
| Arbiter動的KIQ (7件) | 10 | ✅ |

### Tier 1企業カバレッジ
| 企業 | INFO数 | 達成 |
|------|--------|------|
| OpenAI | 14 | ✅ (≥8) |
| Anthropic | 12 | ✅ (≥8) |
| Google | 8 | ✅ (≥8) |
| xAI | 6 | ⚠️ (<8、要補完) |
| ByteDance | 8 | ✅ (≥8) |

### PIRカバレッジ
| PIR | INFO数 | 達成 |
|-----|--------|------|
| PIR-1 (AIエージェント市場) | 28 | ✅ (≥10) |
| PIR-2 (規制・雇用影響) | 31 | ✅ (≥10) |
| PIR-3 (技術・経済構造) | 25 | ✅ (≥10) |
| PIR-4 (キャリア変化) | 19 | ✅ (≥10) |
| PIR-5 (AGI・安全性) | 14 | ✅ (≥10) |

### 注意事項
- xAI企業カバレッジが8件未満（INFO-006, 009, 013等で6件）。次回収集で補完推奨。
- Arbiter優先KIQ (H-GOV-001, H-XAI-004, H-CAR-002) は全てカバー済み。
- 信頼性A-1ソース: AI Safety Index Summer 2026 (FLI) のみ。次回は一次情報のA-1ソース増加推奨。

## 収集結果

### INFO-001
- **タイトル:** GPT-5.6: Frontier intelligence that scales with your ambition
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6ファミリー（Sol/Terra/Lunaの3階層）を一般提供開始。SolはAgents' Last Exam 53.6%（Claude Fable 5を13.1pt上回る）、Coding Agent Index 80（新SOTA）、ARC-AGI-3 7.78%（初の有意義な進歩）、BrowseComp 92.2%（新SOTA）、OSWorld 2.0 62.6%を達成。Programmatic Tool Callingとultra（4エージェント並列）を導入。価格はSol $5/$30、Terra $2.50/$15、Luna $1/$6 per 1M tokens。
- **キーファクト:**
  - GPT-5.6 Sol: Agents' Last Exam 53.6%（Fable 5比+13.1pt）
  - Coding Agent Index 80（新SOTA、Fable 5比+2.8pt）
  - ARC-AGI-3 7.78%（GPT-5.5の0.43%から大幅向上）
  - RSI Index 57.9%（GPT-5.5比+16.2pt、recursive self-improvement能力向上）
  - ultra設定: 4エージェント並列協調で複雑タスク高速化
  - Programmatic Tool Calling: ツール連携の効率化、ZDR対応
  - GeneBench Pro 28.7%（Claude Fable 5は生物学的質問を拒否し評価不可）
  - 内部研究推論コンピュート6ヶ月で100倍増、エージェントトークン使用量22倍増
  - 700,000 A100e GPU時間のレッドチーミング実施
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260714-0001

### INFO-002
- **タイトル:** ChatGPT is now a partner for your most ambitious work
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-002-02
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPT Workを発表。アプリ・ファイル横断で行動するエージェントで、Codex技術を内蔵し時間単位のプロジェクトを自律完了。Plugins統合（Slack/Teams/Google Drive等）、Scheduled Tasks、Sites（Web アプリ生成）、Computer Useを搭載。週500万人がCodexを使用（うち100万人以上は非開発業務）。
- **キーファクト:**
  - ChatGPT Work: GPT-5.6搭載、Pro/Enterprise/Edu向け本日ロールアウト開始
  - Codex週間アクティブユーザー500万人、うち100万人+が非ソフトウェア開発業務
  - Scheduled Tasksで自律定期実行（Slack/Teams更新監視→ドキュメント更新等）
  - デスクトップアプリでComputer Use（ローカルファイル/ブラウザ操作）
  - Atlasブラウザを段階的に廃止しChatGPTに統合
  - Sites機能: インタラクティブWebアプリ/ダッシュボード生成（パブリックベータ）
  - Auto-review: 上位モデルによるアクション事前レビューでセキュリティ強化
- **引用URL:** https://openai.com/index/chatgpt-for-your-most-ambitious-work/
- **Evidence ID:** EVD-20260714-0002

### INFO-003
- **タイトル:** Introducing GPT-Live
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-Live（フルデュプレックス音声モデル）を発表。同時に聴きながら話すことが可能で、「mhmm」等の相槌、バックグラウンドでGPT-5.5に委譲して複雑タスク処理。GPT-Live-1とGPT-Live-1 miniの2バージョン。ChatGPT Voiceの週間1.5億人ユーザーに提供開始。
- **キーファクト:**
  - フルデュプレックス: 同時聴取・発話可能
  - GPT-Live-1 GPQA 84.2%（AVM 45.3%から大幅向上）
  - BrowseComp 75.2%（AVM 0.7%から大幅向上）
  - 音声会話75.7%がAVMよりGPT-Live-1を優先選好
  - 週間150万人がChatGPT Voiceを使用
  - API提供は近日予定（企業はウェイトリスト登録可能）
- **引用URL:** https://openai.com/index/introducing-gpt-live/
- **Evidence ID:** EVD-20260714-0003

### INFO-004
- **タイトル:** Expanding Managed Agents in Gemini API: background tasks, remote MCP and more
- **ソース:** Google公式ブログ (blog.google)
- **公開日:** 2026-07-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05
- **関連企業:** Google / DeepMind
- **要約:** GoogleがGemini APIのManaged Agentsを拡張。バックグラウンド非同期実行、リモートMCPサーバー統合、カスタム関数呼び出し、認証情報更新機能を追加。Gemini Interactions APIで単一エンドポイントから推論・コード実行・パッケージインストール・ファイル管理を実行可能。
- **キーファクト:**
  - バックグラウンド実行（background: true）: HTTP接続を保持せず非同期タスク実行
  - リモートMCPサーバー統合: プロキシ不要で内部API/DBに直接接続
  - カスタム関数呼び出し: 組み込みツールと並行してローカル関数実行
  - 認証情報更新: environment_id再利用でファイルシステム状態保持
  - Antigravity Agent（antigravity-preview-05-2026）をエージェントとして使用
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/
- **Evidence ID:** EVD-20260714-0004

### INFO-005
- **タイトル:** KPMG integrates Claude across its core business and workforce of more than 276,000 in strategic alliance
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** AnthropicとKPMGがグローバル戦略提携を発表。KPMGの276,000人以上の全従業員にClaudeを展開。Digital GatewayプラットフォームにClaude CoworkとManaged Agentsを組み込み、税務・法務・プライベートエクイティ・サイバーセキュリティ分野で活用。PE向け新製品「KPMG Blaze」でClaude Codeを組み込み。
- **キーファクト:**
  - KPMG全276,000+従業員にClaudeアクセス提供
  - Digital Gateway（Azure基盤）にClaude Cowork + Managed Agents統合
  - 税務エージェント構築: 以前は数週間→Claude導入後数分
  - KPMGがAnthropicのPE向け優先パートナーに指定
  - KPMG Blaze: Claude Code組み込みでレガシーIT近代化
  - UT Austinとの共同研究で「human-in-the-loop」の価値を実証
- **引用URL:** https://www.anthropic.com/news/anthropic-kpmg
- **Evidence ID:** EVD-20260714-0005

### INFO-006
- **タイトル:** Anthropic and Infosys collaborate to build AI agents for telecommunications and other regulated industries
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03, KIQ-002-02
- **関連企業:** Anthropic
- **要約:** AnthropicとInfosysが通信・金融・製造・ソフトウェア開発分野向けエンタープライズAIソリューションの共同開発で提携。ClaudeモデルとClaude CodeをInfosys Topazに統合。インドはClaude.aiの第2の市場で、Claude使用の半分近くがアプリケーション構築とシステム近代化。
- **キーファクト:**
  - 対象産業: 通信・金融サービス・製造・ソフトウェア開発
  - Claude Agent SDKで長時間複雑タスクの自律エージェント構築
  - インドはClaude.ai第2の市場、使用の約半分が技術的作業
  - レガシーシステム近代化の加速とコスト削減
- **引用URL:** https://www.anthropic.com/news/anthropic-infosys
- **Evidence ID:** EVD-20260714-0006

### INFO-007
- **タイトル:** Introducing Grok 4.5
- **ソース:** xAI公式サイト
- **公開日:** 2026-07-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02, KIQ-003-01
- **関連企業:** xAI (SpaceX子会社)
- **要約:** xAIがGrok 4.5を発表。コーディング・エージェントタスク・ナレッジワーク向けの最強モデル。知識カットオフ2026年2月1日。価格は100万入力トークン$2。SuperGrokおよびX Premium Plusサブスクライバー向けにGrok Build（コーディングエージェント）をベータ提供。
- **キーファクト:**
  - Grok 4.5はxAI最強モデル（コーディング・エージェント・ナレッジワーク）
  - 価格: $2/1M入力トークン
  - 知識カットオフ: 2026年2月1日
  - Grok Build: ターミナルから動作するコーディングエージェント（ベータ）
  - SuperGrok/X Premium Plus向け提供
- **引用URL:** https://x.ai/news/grok-4-5
- **Evidence ID:** EVD-20260714-0007

### 動的追加クエリ（Arbiterフィードバックに基づく）
- KIQ-MIL-001: "autonomous weapons AI human override rejection rate military 2026", "AI lethal autonomous weapons system human control requirement 2026" (limit: 10)
- KIQ-OAI-001: "OpenAI revenue breakdown government vs commercial contracts 2026" (limit: 10)
- KIQ-ANT-002: "Claude Code DAU WAU active users developer adoption metrics 2026" (limit: 10)
- KIQ-CAR-002-OPS: "AI design evaluation capability premium salary enterprise hiring 2026" (limit: 5)
- KIQ-NEW-001: "AI company government equity stake 5 percent ownership proposal 2026" (limit: 5)
- KIQ-NEW-002: "Decagon open source AI agent migration enterprise switching 2026" (limit: 5)
- KIQ-NEW-003: "Grok enterprise adoption failure rejection case study company 2026" (limit: 5)

### INFO-008
- **タイトル:** U.S. Senate Panel Approves AI, Autonomous Weapons Rules
- **ソース:** Arms Control Association
- **公開日:** 2026-07-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** （政府・軍一般）
- **要約:** 米上院委員会が自律兵器・軍事AIに関する規則を承認。国防総省に対し「人間が適切な水準の判断を行使することを確保する」ことを要求。DoD Directive 3000.09は人間監視下の自律兵器システムが目標を選択・交戦することを明示的に許可している。
- **キーファクト:**
  - 上院委員会が自律兵器・軍事AI規則を承認
  - 「人間の判断の適切な行使」を国防総省に要求
  - DoD Directive 3000.09は人間監視下の自律兵器の目標選択・交戦を許可
  - 依然として「meaningful human control」の法的定義が不在
- **引用URL:** https://www.armscontrol.org/act/2026-07/news/us-senate-panel-approves-ai-autonomous-weapons-rules
- **Evidence ID:** EVD-20260714-0008

### INFO-009
- **タイトル:** AI Safety Index — Summer 2026
- **ソース:** Future of Life Institute
- **公開日:** 2026-07-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001, KIQ-005-03
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** Future of Life InstituteのAI Safety Index Summer 2026版。レビュアーは産業界の軍事AIへの転換を「新たな現状リスク」として指摘。2024年から2026年にかけてAnthropic、OpenAI、Google等が軍事契約を拡大。
- **キーファクト:**
  - 業界の軍事AI転換を「現状リスク」として分類
  - 2024-2026で主要AI企業が軍事契約を拡大
  - AI企業の安全性姿勢と軍事展開の矛盾を指摘
- **引用URL:** https://futureoflife.org/ai-safety-index-summer-2026/
- **Evidence ID:** EVD-20260714-0009

### INFO-010
- **タイトル:** Trump Administration Is Snapping Up Stakes in Private Companies
- **ソース:** New York Times
- **公開日:** 2026-07-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-NEW-001
- **関連企業:** OpenAI
- **要約:** NYT報道: トランプ政権が民間企業の株式取得を加速。OpenAI経営陣による政府への株式提供提案は「規制監視からの買い抜け」の側面が強いと分析。政府の5%持分取得は約$42.6億と評価。
- **キーファクト:**
  - トランプ政権が民間企業の株式取得を加速中
  - OpenAIの5%株式提供は「規制監視回避」の側面が強い
  - 5%持分は約$42.6億相当
  - 政府とAI企業の資本関係の新たな次元
- **引用URL:** https://www.nytimes.com/2026/07/13/business/economy/trump-equity-stakes-ai.html
- **Evidence ID:** EVD-20260714-0010

### INFO-011
- **タイトル:** Anthropic 3Q26 Profit Over $1B; OpenAI vs Anthropic revenue dynamics
- **ソース:** SemiAnalysis
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001, KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** SemiAnalysis分析: OpenAIとAnthropicの合計ARR約$1000億。OpenAIは2026 Q1で65%以上がサブスクリプション、Q2末時点で約40%に低下。Anthropicの年次収益は2026年5月に$470億を超えOpenAIの$250億を逆転。OpenAI Q2 2026収益$109億見通し。
- **キーファクト:**
  - OpenAI + Anthropic 合計ARR約$1000億
  - OpenAI: Q1 2026で65%サブスク→Q2末で40%に低下
  - Anthropic年次収益$470億（2026年5月）vs OpenAI $250億
  - OpenAI Q2 2026収益予想$109億、営業利益見込みあり
  - エンタープライズ契約がOpenAI収益の40%+
- **引用URL:** https://newsletter.semianalysis.com/p/anthropic-3q26-profit-over-1b-the
- **Evidence ID:** EVD-20260714-0011

### INFO-012
- **タイトル:** Claude Code vs Cursor vs Copilot vs Codex: Workplace Adoption
- **ソース:** Uvik.net / JetBrains Survey (Jan 2026)
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-ANT-002, KIQ-004-02
- **関連企業:** Anthropic, Microsoft, OpenAI
- **要約:** JetBrains 2026年1月調査: GitHub Copilotが職場導入率29%（2600万人+ユーザー）で首位。CursorとClaude Codeが各18%で同率2位。Claude CodeはAnthropicの最速成長製品として注目。
- **キーファクト:**
  - GitHub Copilot: 職場導入率29%、2600万人+ユーザー
  - Cursor: 18%、Claude Code: 18%（同率2位）
  - Claude CodeはAnthropic最速成長製品
  - コーディングエージェント市場で3強状態
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/
- **Evidence ID:** EVD-20260714-0012

### INFO-013
- **タイトル:** Claude Code reached $2.5 billion in annualised revenue
- **ソース:** Fatjoe AI Statistics
- **公開日:** 2026-07-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-ANT-002, KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Claude Codeが2026年2月時点で年換算$25億収益に到達。Anthropicの最速成長製品。Codexは2026年6月に週間500万人ユーザーを突破。
- **キーファクト:**
  - Claude Code: 2026年2月時点で年換算$25億収益
  - Anthropic最速成長製品として位置づけ
  - Codex: 2026年6月に週間500万人ユーザー突破
- **引用URL:** https://fatjoe.com/blog/ai-stats/
- **Evidence ID:** EVD-20260714-0013

### INFO-014
- **タイトル:** AI salary premium 25-33% over non-AI roles; STEM AI jobs median $200K
- **ソース:** LinkedIn / CapTech University
- **公開日:** 2026-07-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-CAR-002-OPS, KIQ-004-03
- **関連企業:** （業界一般）
- **要約:** AI関連職の給与プレミアムが25-33%。AI職の平均報酬は$192,000〜$437,000、中央値$200,000（2026年）。これは非AI製品職に対して15-20%のプレミアム。設計・評価能力を持つ人材に高い報酬。
- **キーファクト:**
  - AI関連職の給与プレミアム25-33%
  - AI職の報酬範囲$192,000〜$437,000、中央値約$200,000
  - 非AI製品職に対し15-20%のプレミアム
  - AIスキル需要の高さが市場価値を押し上げ
- **引用URL:** https://www.captechu.edu/blog/top-stem-jobs-ai-career-advancement
- **Evidence ID:** EVD-20260714-0014

### INFO-015
- **タイトル:** Your AI Vendor Just Became Your Biggest Risk — Decagon model-agnostic migration
- **ソース:** Beri.net
- **公開日:** 2026-07-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-NEW-002, KIQ-003-05, KIQ-001-03
- **関連企業:** Decagon, Microsoft, Anthropic, OpenAI
- **要約:** Decagon CEOがモデル非依存アーキテクチャを提唱。OSSモデルが企業タスクの80%を同等品質で処理可能。30日以内の単一モデル移行ウィンドウを実現。企業はベンダーロックインリスクを認識し始めている。
- **キーファクト:**
  - OSSモデルが企業タスクの80%を同等品質で処理
  - 30日以内の単一モデル移行が可能（Decagon事例）
  - ベンダーロックインリスクへの企業認識向上
  - マルチベンダー戦略の採用増加
- **引用URL:** https://www.beri.net/article/model-agnostic-ai-architecture-microsoft-anthropic-openai-vendor-lock-in-enterprise-strategy-2026
- **Evidence ID:** EVD-20260714-0015

### INFO-016
- **タイトル:** Musk told Tesla staff to switch to Grok, admits it's not good enough
- **ソース:** Electrek / Facebook
- **公開日:** 2026-07-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-NEW-003, KIQ-001-02
- **関連企業:** xAI, Tesla
- **要約:** MuskがTesla社員にサードパーティAIツールへの支出上限を設定した後、Grokへの切り替えを指示。但し自身で「Grokはまだ十分ではない」と認める。エンタープライズ品質としてのGrokの限界を示す事例。
- **キーファクト:**
  - Musk: Tesla従業員にGrok使用を指示
  - 第三者AIツール支出に上限設定
  - Musk自身が「Grokはまだ十分ではない」と認める
  - 自社製品使用を強制するも品質面で不満を認識
- **引用URL:** https://www.facebook.com/electrekco/posts/1470884941743899/
- **Evidence ID:** EVD-20260714-0016

### INFO-017
- **タイトル:** Glean routes majority of enterprise workloads to open-source models
- **ソース:** Biggo Finance / Glean Podcast
- **公開日:** 2026-07-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-NEW-002, KIQ-003-03, KIQ-003-05
- **関連企業:** Glean, Zhipu (GLM)
- **要約:** Gleanが企業ワークロードの過半数をOSSモデルにルーティング開始。2026年半ばにGLM 5.2が登場してから移行が加速。OSSモデルの企業本番環境での実用性を示す事例。
- **キーファクト:**
  - Glean: 企業ワークロードの過半数をOSSモデルに移行
  - 2026年半ばのGLM 5.2登場で移行加速
  - OSSモデルの企業本番環境での実証例
  - 「チームは小さくならず大きくなる」反直観的見解
- **引用URL:** https://finance.biggo.com/podcast/0cad524edbf7f771
- **Evidence ID:** EVD-20260714-0017

---

## KIQ-001-01: 各社のAgent SDK/APIの機能拡張ロードマップ

### INFO-018
- **タイトル:** OpenAI Multi-agent API beta and Programmatic Tool Calling in Responses API
- **ソース:** OpenAI Developer Docs
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがResponses APIでMulti-agent（ベータ）とProgrammatic Tool Callingを導入。モデルが並列サブエージェントを起動・協調し結果を統合。Assistants APIは非推奨化。Chat Completions APIは継続サポートするが、組み込みツール・MCP・状態管理はResponses APIのみ。
- **キーファクト:**
  - Multi-agent: 単一リクエストで並行サブエージェント起動・統合
  - Programmatic Tool Calling: モデルがインメモリでツール調整プログラムを記述・実行
  - Assistants API非推奨化、Responses APIへ移行
  - MCP・状態管理・組み込みツールはResponses APIのみ
- **引用URL:** https://developers.openai.com/api/docs/guides/responses-multi-agent
- **Evidence ID:** EVD-20260714-0018

### INFO-019
- **タイトル:** Claude Agent SDK TypeScript active development — frequent releases
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-07-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScript版が活発に開発中。2-3日前にリリース。Agent toolの構造化結果にAgentToolCompletedOutputを追加。Python版も改名され、コーディング以外の全領域のエージェント構築を反映。Lenny's NewsletterでClaude Agent SDKを使ったharness構築が紹介。
- **キーファクト:**
  - TypeScript SDK: 直近2-3日前にリリース（頻繁な更新）
  - AgentToolCompletedOutput追加で構造化結果強化
  - Python版SDKがコーディング特化から汎用エージェントに改名
  - Sentry バグデバッグharness構築の実例あり
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260714-0019

### INFO-020
- **タイトル:** Gemini Enterprise Agent Platform — Google's unified agent platform
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** GoogleがGemini Enterprise Agent Platformを展開。コード実行、パッケージインストール、ファイル管理を単一エンドポイントで処理。Live APIで低レイテンシリアルタイム音声・ビデオ相互作用を提供。Grokモデルもパートナーモデルとして統合。
- **キーファクト:**
  - Gemini Enterprise Agent Platformで統合エージェント基盤
  - 単一エンドポイントで推論・コード実行・パッケージ管理
  - Live API: 連続ストリーム音声・ビデオ・テキスト処理
  - サードパーティモデル（Grok等）もパートナーモデルとして統合
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start
- **Evidence ID:** EVD-20260714-0020

### INFO-021
- **タイトル:** Grok Build changelog — terminal coding agent with agent connection hooks
- **ソース:** xAI Build Documentation
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** xAI (SpaceX子会社)
- **要約:** Grok Build 0.2.62をリリース。エージェント接続経由でhooks登録可能に（オンディスクファイルのみから拡張）。/usage警告の修正。Responses API、OAuth、エージェントツール、マルチエージェント対応。
- **キーファクト:**
  - Grok Build 0.2.62リリース
  - エージェント接続経由のhooks登録機能追加
  - Responses API・OAuth・エージェントツール・マルチエージェント対応
  - ターミナルベースのコーディングエージェント
- **引用URL:** https://x.ai/build/changelog
- **Evidence ID:** EVD-20260714-0021

### INFO-022
- **タイトル:** ByteDance Doubao & Alibaba Qwen agent features going offline July 15
- **ソース:** SCMP / Facebook
- **公開日:** 2026-07-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-002-05
- **関連企業:** ByteDance, Alibaba
- **要約:** ByteDanceのDoubaoとAlibabaのQwenがユーザーに「エージェント機能が7月15日にオフラインになる」ことを通知。「製品機能調整」のため。中国の主要コンシューマー向けAIアプリのエージェント戦略転換を示唆。
- **キーファクト:**
  - Doubao（ByteDance）とQwen（Alibaba）のエージェント機能が7/15に停止
  - 「製品機能調整」を理由
  - 中国主要コンシューマーAIアプリの戦略転換シグナル
- **引用URL:** https://www.facebook.com/scmp/posts/1427163516126363/
- **Evidence ID:** EVD-20260714-0022

### INFO-023
- **タイトル:** Microsoft Agent Framework — multi-language agent platform (AutoGen + Semantic Kernel)
- **ソース:** Microsoft Learn
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Agent Frameworkが.NET, Python, Goでマルチエージェントワークフロー構築をサポート。Microsoft Foundry, Anthropic, Azure OpenAI, OpenAI等を統合。4つのランタイム（LangGraph, CrewAI, AutoGen, WayFlow）で精度・レイテンシ・挙動に有意差を確認。
- **キーファクト:**
  - .NET, Python, Goでのマルチエージェントワークフロー構築
  - Microsoft Foundry / Anthropic / Azure OpenAI / OpenAI統合
  - フレームワーク間で精度・レイテンシ・挙動に有意差
  - Open Agent Specificationでクロスフレームワーク相互運用性を推進
- **引用URL:** https://learn.microsoft.com/en-us/agent-framework/overview/
- **Evidence ID:** EVD-20260714-0023

### INFO-024
- **タイトル:** 2026 State of AI Security: 56% deployed agents in production, security gaps
- **ソース:** Orca Security
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-001-02, KIQ-002-03
- **関連企業:** （業界一般）
- **要約:** Orca Security調査: AI採用組織の56%がエージェントフレームワークを本番展開済み。セキュリティは追いついていない。Bedrockエージェントが数百件監視対象で稼働。OpenAIがCodexエージェントのエンタープライズ化に$4.5億を投入。
- **キーファクト:**
  - 56%のAI採用組織がエージェントフレームワークを本番展開
  - セキュリティの追いつき不足
  - Bedrockエージェント数百件が監視下で稼働
  - OpenAI: Codexエージェントのエンタープライズ化に$4.5億投資
- **引用URL:** https://orca.security/resources/blog/2026-state-of-ai-security-report-summary/
- **Evidence ID:** EVD-20260714-0024

---

## KIQ-001-02: エンタープライズ展開（セキュリティ認証、SLA、専用サポート）

### INFO-025
- **タイトル:** Okta integrates with Anthropic Claude for enterprise security visibility
- **ソース:** Okta / Anthropic
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic, Okta
- **要約:** OktaがAnthropic Claude EnterpriseとClaude Platformに統合。セキュリティ・コンプライアンスチームにClaudeの利用状況の一元的可視性を提供。AnthropicはSOC 2 Type II認証を保有。
- **キーファクト:**
  - Okta-Claude統合: エンタープライズセキュリティ可視性
  - Claude Enterprise: SOC 2 Type II / ISO認証準拠
  - データはモデル訓練に不使用（エンタープライズ分離）
  - Compliance APIで監査ログ提供
- **引用URL:** https://www.facebook.com/NetMonInfo/posts/1427455136070955/
- **Evidence ID:** EVD-20260714-0025

### INFO-026
- **タイトル:** Vertex AI becomes part of Gemini Enterprise Agent Platform with 24/7 SLA
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Google CloudがVertex AIをGemini Enterprise Agent Platformに統合。エンタープライズ版は24/7サポートとSLAを提供（Google AI StudioにはSLAなし）。Gemini 3.1 Flash-LiteをVertex AI経由でプレビュー提供。
- **キーファクト:**
  - Vertex AI → Gemini Enterprise Agent Platformに統合
  - エンタープライズ版: 24/7サポート + SLA
  - Google AI Studio: エンタープライズSLA/サポートなし
  - Gemini 3.1 Flash-Lite企業向けプレビュー開始
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/migrate-google-ai
- **Evidence ID:** EVD-20260714-0026

---

## KIQ-001-03: 開発者エコシステム（MCP、マーケットプレイス、連携）

### INFO-027
- **タイトル:** MCP 2026 Specification Release Candidate — stateless core, Extensions, Tasks
- **ソース:** Model Context Protocol Blog
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-003-05
- **関連企業:** （標準化団体）
- **要約:** MCP仕様の次期リリース候補（RC）が公開。ステートレスプロトコルコア、Extensions フレームワーク、Tasks 機能を含む。MCPはAIアプリと外部システムを接続するオープン標準として急速に普及中。
- **キーファクト:**
  - ステートレスプロトコルコア導入
  - Extensions フレームワーク + Tasks 機能追加
  - MCP採用が爆発的に拡大中
  - 単一の設定ミスが壊滅的影響を持ちうるセキュリティリスク
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260714-0027

### INFO-028
- **タイトル:** AAIF introduces MCPA — first official MCP certification; CData joins AAIF
- **ソース:** Agentic AI Foundation / CData
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** AAIF (Linux Foundation)
- **要約:** AAIF（Linux Foundation、2025年12月設立）がMCPの初の公式認定資格MCPAを発表。Claude、ChatGPT、その他プラットフォームにまたがる標準化を推進。CDataがAAIFに加盟。
- **キーファクト:**
  - MCPA: MCP初の公式認定資格
  - AAIF: Linux Foundation傘下、2025年12月設立
  - Claude/ChatGPT等を横断する標準化を推進
  - CDataがAAIF加盟、データコネクタ提供
- **引用URL:** https://aaif.io/blog/introducing-the-mcpa-the-first-official-certification-for-the-model-context-protocol/
- **Evidence ID:** EVD-20260714-0028

### INFO-029
- **タイトル:** Databricks introduces Omnigent — open-source meta-harness for AI agents
- **ソース:** Databricks Community
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-003-05, KIQ-003-03
- **関連企業:** Databricks
- **要約:** DatabricksがOmnigent（OSS メタハーネス）を発表。複数のAIエージェントを組み合わせ、制御し、共有する統合レイヤー。エンタープライズ向けのオープンなエージェント統合基盤。
- **キーファクト:**
  - Omnigent: OSSメタハーネス
  - 複数エージェントの統合・制御・共有レイヤー
  - エンタープライズ向けオープン基盤
  - ベンダーロックイン回避への貢献
- **引用URL:** https://community.databricks.com/t5/mvp-articles/databricks-introduces-omnigent-a-new-meta-harness-for-building/td-p/160171
- **Evidence ID:** EVD-20260714-0029

### INFO-030
- **タイトル:** Microsoft Agent 365 ecosystem partner agents at launch
- **ソース:** Microsoft Learn
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Microsoft
- **要約:** MicrosoftがAgent 365で事前統合されたエコシステムパートナーエージェントを公開。サードパーティエージェントがMicrosoft 365環境で即座に動作。
- **キーファクト:**
  - Agent 365: 事前統合パートナーエージェント
  - Microsoft 365環境で即座利用可能
  - エコステム拡大の新たな形態
- **引用URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/third-party-agents
- **Evidence ID:** EVD-20260714-0030

### INFO-031
- **タイトル:** NVIDIA publishes AI agent skills on GitHub — portable instruction sets
- **ソース:** GitHub (NVIDIA/skills)
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** NVIDIA
- **要約:** NVIDIAがAIエージェントスキルをGitHubで公開。CUDA-Xライブラリ、AI Blueprints、プラットフォームツールの最適な使用方法をエージェントに教えるポータブル指示セット。
- **キーファクト:**
  - スキル: ポータブル指示セット
  - CUDA-X/AI Blueprints/プラットフォームツールに最適化
  - GitHub公開でコミュニティ貢献
  - スキル配布の標準化の一端
- **引用URL:** https://github.com/nvidia/skills
- **Evidence ID:** EVD-20260714-0031

---

## KIQ-001-04: マルチモーダルAgent統合

### INFO-032
- **タイトル:** GPT-5.6 multimodal capabilities — OSWorld 62.6%, BrowseComp 92.2%, MMMU Pro 84.6%
- **ソース:** OpenAI GPT-5.6 Blog
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** OpenAI
- **要約:** GPT-5.6 Solがマルチモーダル評価で新SOTA達成。OSWorld 2.0 62.6%（コンピューター使用）、BrowseComp 92.2%（ブラウジング）、MMMU Pro 84.6%。強化されたデザイン判断でUIの検査・修正が可能。Computer Use機能はChatGPT Workで実装済み。
- **キーファクト:**
  - OSWorld 2.0: 62.6%（Opus 4.8超、85%少ないトークン）
  - BrowseComp: 92.2%（Sol Ultra、新SOTA）
  - MMMU Pro (no tools): 83%, (with tools): 84.6%
  - Computer Use: デスクトップアプリでクリック・タイピング・ファイル操作
  - Atlas ブラウザの段階的廃止→ChatGPTに統合
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260714-0032

### INFO-033
- **タイトル:** Gemini Enterprise Computer Use sandbox — browser/terminal automation
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** Gemini Enterprise Agent PlatformにComputer Useサンドボックスが実装。エージェントがクリック、サイトナビゲーション、スクリーンショット取得など人間の操作を模倣。AWSもComputer-use agentsの処方箋を公開し、業界標準化が進む。
- **キーファクト:**
  - Gemini Enterprise Computer Use: 人間操作模倣のサンドボックス
  - クリック・ナビゲーション・スクリーンショット自動化
  - AWSもComputer-use agentsの処方箋を公開
  - 業界標準化の進展
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use
- **Evidence ID:** EVD-20260714-0033

### INFO-034
- **タイトル:** Claude Fable 5 ECI 161 — first Anthropic lead on Epoch AI Engineering Capability Index
- **ソース:** Epoch AI Benchmarks
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** Epoch AIベンチマークでClaude Fable 5がECI 161を達成、GPT-5.5 Proを1ポイント上回る。Anthropicが初めてECI首位を獲得。ただしGPT-5.6 SolのCoding Agent Index 80がFable 5の77.2を上回る。
- **キーファクト:**
  - Claude Fable 5 ECI: 161（GPT-5.5 Pro比+1pt）
  - Anthropic初のECI首位（一時的）
  - GPT-5.6 Sol Coding Agent Index: 80（Fable 5の77.2を上回る）
  - ベンチマーク首位が激しく入れ替わる競争状態
- **引用URL:** https://epoch.ai/benchmarks
- **Evidence ID:** EVD-20260714-0034

---

## KIQ-001-05: スキル配布と実行環境、ロックイン

### INFO-035
- **タイトル:** OpenAI Skills in ChatGPT — SKILL.md portable instruction format
- **ソース:** OpenAI Help Center / ChatGPT Learn
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI SkillsがChatGPT/Codexで展開中。SKILL.md形式でタスク固有の指示・リソース・スクリプトをパッケージ化。ワークスペース管理者がスキルを管理。NVIDIA、コミュニティがスキルを公開するエコシステム形成中。
- **キーファクト:**
  - SKILL.md: ポータブル指示形式
  - Codexのタスク固有能力を拡張
  - ワークスペース管理者によるスキル管理
  - エージェントスキルマーケットプレイス形成中
- **引用URL:** https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- **Evidence ID:** EVD-20260714-0035

### INFO-036
- **タイトル:** Claude Cowork sessions run remotely on Anthropic servers — sandbox execution
- **ソース:** Anthropic Support
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude CoworkセッションはAnthropicのサーバー上でリモート実行（ベータ）。ファイル・ブラウザ・アプリへのアクセスはClaude Desktopアプリ経由。実行環境がベンダーサーバー上に構築され、ロックインの構造的要素となる。
- **キーファクト:**
  - Claude Cowork: Anthropicサーバー上でリモート実行
  - ファイル/ブラウザ/アプリアクセスはDesktop経由
  - 実行環境のベンダー依存
  - MCPツール経由で外部システム接続
- **引用URL:** https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- **Evidence ID:** EVD-20260714-0036

---

## KIQ-002-01: クラウドプロバイダーのAI Agent統合

### INFO-037
- **タイトル:** AWS Bedrock Agents renamed to "Classic" and put in maintenance mode — replaced by AgentCore
- **ソース:** AWS Plain English
- **公開日:** 2026-07-01
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** 2026年6月30日、AWSがBedrock Agentsを「Classic」に改名しメンテナンスモードに移行。新規顧客は参加不可。後継はAgentCore。サーバーレス画像編集エージェントの構築チュートリアルがAgentCore向けに公開済み。
- **キーファクト:**
  - Bedrock Agents → "Bedrock Agents Classic"に改名（2026-06-30）
  - メンテナンスモード移行、新規顧客参加不可
  - 後継: AgentCore
  - AgentCore向けハーネスチュートリアル公開済み
- **引用URL:** https://aws.plainenglish.io/aws-just-retired-its-flagship-ai-agent-product-it-launched-in-2023-add395ae3fe8
- **Evidence ID:** EVD-20260714-0037

### INFO-038
- **タイトル:** Azure AI Foundry Agent Service with Logic Apps enterprise integration
- **ソース:** LITS / Microsoft
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Azure AI Foundry Agent ServiceがAzure Logic Apps経由でDynamics 365、SAP、Salesforce等のエンタープライズシステムにセキュア接続。Microsoft Foundry + Agent Frameworkで設計・構築・評価・展開の統合プラットフォームを提供。
- **キーファクト:**
  - Azure Logic Apps経由でエンタープライズシステム接続
  - Dynamics 365 / SAP / Salesforce統合
  - Microsoft Foundry + Agent Frameworkの統合プラットフォーム
  - .NET / Python / Goサポート
- **引用URL:** https://www.lits.services/azure-ai-foundry-agent-service-microsoft-business-applications/
- **Evidence ID:** EVD-20260714-0038

### INFO-039
- **タイトル:** Vertex AI Agent Builder documentation — build, scale, govern AI agents
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Vertex AI Agent Builderがエージェントの構築・スケール・ガバナンスのためのスイート製品として提供。データウェアハウス等との統合。Code ExecutionサンドボックスでVertex AI Agent Engine上でコード実行可能。
- **キーファクト:**
  - Agent Builder: 構築・スケール・ガバナンスのスイート
  - データウェアハウス統合
  - Code Executionサンドボックス搭載
  - Vertex AI Agent Engine上で動作
- **引用URL:** https://docs.cloud.google.com/agent-builder
- **Evidence ID:** EVD-20260714-0039

---

## KIQ-002-02: エンタープライズAI Agent採用率とユースケース

### INFO-040
- **タイトル:** Okta AI Agents at Work 2026: 91% using AI agents, only 10% have NHI strategy
- **ソース:** Okta
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界一般）
- **要約:** Okta調査: 組織の91%がAIエージェントを使用中だが、非人間アイデンティティ（NHI）管理戦略を持つのはわずか10%。McKinsey調査では88%の組織がAIを定期使用（前年78%から上昇）。
- **キーファクト:**
  - 91%の組織がAIエージェント使用中
  - NHI管理戦略を持つのは10%のみ
  - McKinsey: 88%がAI定期使用（前年78%→上昇）
  - セキュリティとガバナンスの大幅な遅れ
- **引用URL:** https://www.okta.com/en-gb/newsroom/articles/ai-agents-at-work-2026-agentic-enterprise-security/
- **Evidence ID:** EVD-20260714-0040

### INFO-041
- **タイトル:** Enterprise AI ROI: Only 5% see real returns; PwC only 12.5% of CEOs report both savings and growth
- **ソース:** Master of Code / PwC / IntuitionLabs
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界一般）
- **要約:** AI ROI分析: エンタープライズのわずか5%が実際のリターンを確認。平均1.7倍のリターン、26-31%のコスト削減。PwC調査ではCEOの12.5%のみがコスト削減と収益成長の両方を報告。Fortune 500のSierraパイロットは1.5年でようやく本番接近。
- **キーファクト:**
  - エンタープライズの5%のみが実際のAI ROIリターン
  - 平均ROI 1.7倍、コスト削減26-31%
  - PwC: CEOの12.5%のみがコスト+収益両方を報告
  - Sierra Fortune 500パイロット: 1.5年で本番接近
  - 財務決算クローズが最高ROIユースケース
- **引用URL:** https://masterofcode.com/blog/ai-roi
- **Evidence ID:** EVD-20260714-0041

---

## KIQ-002-03: 規制環境のエンタープライズAI採用への影響

### INFO-042
- **タイトル:** EU AI Act August 2026 enforcement: compliance costs $8-15M for large enterprises
- **ソース:** Responsible AI Labs
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （業界一般）
- **要約:** EU AI Actの大部分が2026年8月2日に施行。大企業のコンプライアンス費用は$800-1500万。AIガバナンスプラットフォーム市場の支出は2026年に$4.92億と予想。企業のAIインタラクションの47%が個人アイデンティティ経由で発生。
- **キーファクト:**
  - EU AI Act: 2026年8月2日施行
  - 大企業コンプライアンス費用: $800-1500万
  - AIガバナンス市場支出: $4.92億（2026年）
  - 47%のAIインタラクションが個人アカウント経由
- **引用URL:** https://responsibleailabs.ai/knowledge-hub/articles/eu-ai-act-august-2026-compliance
- **Evidence ID:** EVD-20260714-0042

### INFO-043
- **タイトル:** China tightens AI regulation: overseas access limits, user-generated agents, companion chatbots
- **ソース:** Reuters / Lexology / CaptainCompliance
- **公開日:** 2026-07-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-002-05
- **関連企業:** ByteDance, Alibaba
- **要約:** Reuters報道: 北京が中国のトップAIモデルへの海外アクセス制限を検討。AI漏洩・盗難は国家保安法で処罰の可能性。中国が4分野でAI規制: 総合AI法、ネガティブリスト、ユーザー生成AIエージェント規則、AIコンパニオン/感情的チャットボット規制。7月15日にDoubao/Qwenエージェント機能停止。
- **キーファクト:**
  - 北京: 中国トップAIモデルへの海外アクセス制限を検討
  - AI漏洩/盗難=国家保安法で処罰の可能性
  - ユーザー生成AIエージェントの新規制
  - AIコンパニオン/感情チャットボット規制（未成年・高齢者保護）
  - 国内AIスタートアップへの新規資金制限
- **引用URL:** https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/
- **Evidence ID:** EVD-20260714-0043

### INFO-044
- **タイトル:** US AI regulation: Trump executive order, state preemption, Senate AI bills
- **ソース:** SecurePrivacy / Congress.gov / InsideGlobalTech
- **公開日:** 2026-07-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （政府一般）
- **要約:** トランプAI大統領令による州法の先占権問題。NY州Hochul知事が規制リセットの大統領令を発令。Rounds上院議員が5つのAI法案を8月休会後に提出予定。AIサイバーセキュリティ情報交換所の創設を指示。
- **キーファクト:**
  - トランプ大統領令: 州法先占権で州レベルAI規制を制限
  - NY州: 規制リセット大統領令
  - 上院議員Rounds: 5つのAI法案を提案予定
  - AIサイバーセキュリティ情報交換所の創設
- **引用URL:** https://secureprivacy.ai/blog/trump-ai-executive-order-and-state-law-preemption-what-to-do-now
- **Evidence ID:** EVD-20260714-0044

---

## KIQ-002-06: 政府・軍によるAI企業への経済的圧力

### INFO-045
- **タイトル:** Warren demands Pentagon and 7 AI companies disclose full military AI contracts
- **ソース:** NBC News / Federal News Network / Meritalk
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Google, NVIDIA, Microsoft, Amazon, SpaceXAI, Reflection, Oracle
- **要約:** Warren上院議員が国防総省と7社のテック企業（OpenAI/Google/Meta/Amazon/MS/Nvidia/Apple）にAI契約の完全開示を要求。5月に国防総省はSpaceXAI、OpenAI、Google、NVIDIA、Microsoft、AWS、Reflection、Oracleと契約。Pentagonは分類されたAI契約の急速拡大中。
- **キーファクト:**
  - Warren: Pentagon + 7テック企業にAI契約開示要求
  - DoD契約企業: SpaceXAI/OpenAI/Google/NVIDIA/MS/AWS/Reflection/Oracle
  - Warren対象（Anthropicは含まず）: OpenAI/Google/Meta/Amazon/MS/Nvidia/Apple
  - 分類されたAI契約の急速拡大
- **引用URL:** https://www.nbcnews.com/tech/security/warren-elizabeth-pentagon-ai-companies-release-full-military-contracts-rcna352662
- **Evidence ID:** EVD-20260714-0045

### INFO-046
- **タイトル:** Anthropic designated "supply chain risk" by Pentagon — unprecedented for US company
- **ソース:** Federal News Network / Reuters / SCMP
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** 国防総省がAnthropicを「サプライチェーンリスク」に指定。AnthropicがDoD契約の2つの制限条項の削除を拒否したため。この指定は以前Huaweiにのみ使用された。Anthropicはトランプ政権を相手取り訴訟を提起。テック企業がAnthropicを支持。OpenAIは$2億のPentagon契約を獲得し「all lawful use」条項を含む。
- **キーファクト:**
  - Anthropic: Pentagonにより「supply chain risk」指定
  - 理由: DoD契約の2つの制限条項削除要求を拒否
  - この指定はHuawei以来、米国企業として初
  - Anthropicがトランプ政権を提訴、シリコンバレーが支持
  - OpenAI: $2億Pentagon契約、「all lawful use」条項付き
- **引用URL:** https://federalnewsnetwork.com/congress/2026/07/senate-lawmaker-presses-dod-tech-firms-to-disclose-ai-contract-terms/
- **Evidence ID:** EVD-20260714-0046

### INFO-047
- **タイトル:** Pentagon's AI strategy funding problem — private capital <1% of Pentagon contracts
- **ソース:** War on the Rocks
- **公開日:** 2026-07-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** （軍事産業一般）
- **要約:** PentagonのAI戦略に資金問題。民間資本は防衛技術に歴史的コミットメントを示したが、Pentagon契約総額の1%未満。調達市場でのAI企業にとって、政府契約の構造が競争環境を歪めている。
- **キーファクト:**
  - 民間防衛技術投資は歴史的規模
  - だがPentagon契約総額の1%未満
  - 調達構造がAI企業の競争環境を歪める
  - 「安全性重視企業が罰せられ、順応企業が報われる」構造
- **引用URL:** https://warontherocks.com/cogs-of-war/the-pentagons-ai-strategy-has-a-funding-problem/
- **Evidence ID:** EVD-20260714-0047

### INFO-048
- **タイトル:** AI procurement displacing rulemaking — Anthropic-Pentagon standoff policy implications
- **ソース:** Lawfare / AI Frontiers
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, 政府
- **要約:** Lawfare分析: Anthropic-Pentagon対立は政府調達契約がnotice-and-commentルールメイキングや議会を代替する場所として機能していることを暴露。AIモデル選択は単なるソフトウェア調達ではなく価値観の選択である。調達契約が政策形成の主要会場となっている。
- **キーファクト:**
  - 調達契約がルールメイキングを代替する構造
  - AIモデル選択=価値観の選択
  - 調達が政策形成の主要会場に
  - 政府によるAI価値観の非民主的決定リスク
- **引用URL:** https://www.facebook.com/Lawfareblog/posts/1629577552509110/
- **Evidence ID:** EVD-20260714-0048

---

## KIQ-002-04: AI業務自律化の進展

### INFO-049
- **タイトル:** Klarna 22% workforce reduction, 700 CS agents replaced by AI — quality reversal
- **ソース:** KTLA / ABC News / LinkedIn
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaが2024年に従業員22%削減、CS 700人をAIエージェントで代替。その後品質低下で方針転換。Duolingoも「AI first」へ移行したが品質低下で反発。IBM、Amazon、McDonald'sもAI自動化を調整。Forrester調査: 55%の企業が解雇を後悔。WEF: 41%がAIによる人員削減を検討。
- **キーファクト:**
  - Klarna: 従業員22%削減（5000→2000人）、CS 700人をAIで代替
  - その後品質問題で方針転換
  - Duolingo: 「AI first」で品質低下・反発
  - Forrester: 55%が解雇を後悔
  - WEF: 41%がAIによる人員削減を検討
  - IBM/Amazon/McDonald'sもAI自動化方針を調整
- **引用URL:** https://www.facebook.com/ktla5/posts/1634537544928856/
- **Evidence ID:** EVD-20260714-0049

### INFO-050
- **タイトル:** Enterprise AI agents deliver 33 hours/person/week productivity gains for early adopters
- **ソース:** Innovative Human Capital
- **公開日:** 2026-07-10
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04
- **関連企業:** （業界一般）
- **要約:** AIエージェントを人間協調基盤と統合した組織が1人週33時間の生産性向上を実現。McKinsey: AIは文書作成・データ分析・レポート準備・CS・意思決定支援で特に効率化。ハンガリーでは2030年までに€150億の生産性向上（GDPの6-7%）を予測。
- **キーファクト:**
  - 早期導入者: 1人週33時間の生産性向上
  - 高い採用ユースケース: 高ボリューム・非構造化入力・明確な正解基準
  - McKinsey: 文書作成/データ分析/CSで特に効率化
  - ハンガリー: 2030年に€150億の生産性向上予測
- **引用URL:** https://www.innovativehumancapital.com/article/ai-agents-and-the-future-of-work-how-early-adopters-are-building-insurmountable-competitive-advanta
- **Evidence ID:** EVD-20260714-0050

---

## KIQ-002-05: プラットフォーマーのAI統合と中間事業者の侵食

### INFO-051
- **タイトル:** AI agents wiped $2 trillion from SaaS stocks in 2026 — Gartner predicts $234B SaaS spending disruption
- **ソース:** ZenVanRiel / Gartner / SaaSRise
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** （SaaS業界一般）
- **要約:** AIエージェントが2026年にSaaS株から$2兆を抹消。Gartner予測: 年間$2340億のSaaS支出がエージェント型AIによって破壊される。座席ベース課金モデルの陳腐化。SAPは「自律的エンタープライズ」への進化を推進。
- **キーファクト:**
  - SaaS株から$2兆抹消（2026年）
  - Gartner: $2340億のSaaS支出破壊を予測
  - 座席ベース課金の陳腐化
  - AIエージェントが複数SaaSツールを代替
  - SAP: 「自律的エンタープライズ」へ進化
- **引用URL:** https://zenvanriel.com/ai-engineer-blog/saaspocalypse-ai-agents-enterprise-disruption/
- **Evidence ID:** EVD-20260714-0051

### INFO-052
- **タイトル:** Advertising holding company revenues fell 1.2% while global ad spend grew 8.6% — disintermediation accelerates
- **ソース:** The Rank Masters
- **公開日:** 2026-07-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Google
- **要約:** 2025年に世界広告支出が8.6%成長した一方、広告ホールディングカンパニーの収益は1.2%減少。プラットフォーム（Meta/Google）のAI自動化が中間事業者を侵食。広告代理店の「論理作業」が最もコモディティ化しやすい領域。
- **キーファクト:**
  - 世界広告支出+8.6% vs ホールディング収益-1.2%
  - 市場成長と代理店収益の乖離拡大
  - プラットフォームAIが中間層を侵食
  - 「論理作業」が最もコモディティ化
- **引用URL:** https://www.therankmasters.com/insights/benchmarks/ai-reshaping-professional-services-marketing
- **Evidence ID:** EVD-20260714-0052

---

## KIQ-003-01: API料金改定の頻度・方向性

### INFO-053
- **タイトル:** AI price war intensifies — GPT-5.6 three-tier pricing, Claude Fable 5 premium $10/$50, Chinese models cheapest
- **ソース:** OpenAI / Wired / BenchLM
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, DeepSeek
- **要約:** GPT-5.6は3階層（Sol $5/$30, Terra $2.50/$15, Luna $1/$6）。Claude Fable 5は$10/$50とプレミアム価格。DeepSeekは$0.28-$2.19で最安。OpenAIはGPT-4o API入力50%・出力33%値下げ。OpenAIは$0.05〜$180の600倍の価格帯を持つ。
- **キーファクト:**
  - GPT-5.6: Sol $5/$30, Terra $2.50/$15, Luna $1/$6 (per 1M tokens)
  - Claude Fable 5: $10/$50（プレミアム価格設定）
  - DeepSeek: $0.28-$2.19（最安）
  - OpenAI: $0.05〜$180の600倍価格スプレッド
  - Codex価格: 2026年4月にメッセージ単価からAPIトークン使用量ベースに移行
- **引用URL:** https://www.mindstudio.ai/blog/ai-model-pricing-2026-gpt-5-6-grok-4-5-muse-spark-fable-5
- **Evidence ID:** EVD-20260714-0053

---

## KIQ-003-02: ベンチマーク性能推移

### INFO-054
- **タイトル:** GPT-5.6 Sol sets SOTA on ARC-AGI-3 at 7.78%, Coding Index 80, FrontierMath Tier 4 83%
- **ソース:** OpenAI GPT-5.6 System Card / Epoch AI
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** GPT-5.6 Solの主要ベンチマーク: ARC-AGI-3 7.78%（初の有意義進歩）、Coding Agent Index 80（新SOTA）、GPQA Diamond 94.6%、FrontierMath Tier 4 83%、Terminal-Bench 2.1 88.8%。Claude Fable 5はSWE-Bench Pro 80%で首位、GeneBench Proは拒否により評価不可。Gemini 3.1 Pro PreviewはGPQA 94.3%。
- **キーファクト:**
  - GPT-5.6 Sol: ARC-AGI-3 7.78%（GPT-5.5の0.43%から大幅向上）
  - Coding Agent Index: 80（新SOTA）
  - GPQA Diamond: GPT-5.6 Sol 94.6%, Fable 5 92.6%, Gemini 3.1 Pro 94.3%
  - SWE-Bench Pro: Claude Mythos 5 80.3%首位、GPT-5.6 Sol 64.6%
  - Claude Fable 5: 生物学的質問を拒否、GeneBench Pro評価不可
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260714-0054

---

## KIQ-003-03: オープンソースと商用モデルの性能ギャップ

### INFO-055
- **タイトル:** Meta replaces Llama with Muse Spark — OSS vs commercial gap narrowing
- **ソース:** Wikipedia / MindStudio
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, Mistral, DeepSeek
- **要約:** MetaがLlamaをMuse Sparkに置換（2026年4月）。Muse Spark 1.1はGPT-5.5と同等レベル。CNBC報道: 中国のOSSモデル（DeepSeek/Z.ai）が複雑でないタスクで性能競争力を示す。Metaの戦略はモデル層のコモディティ化を通じてコンピュート基盤で価値捕捉。
- **キーファクト:**
  - Meta Muse Spark 1.1: GPT-5.5同等レベル（テスト領域）
  - Llama → Muse Sparkに置換（2026年4月）
  - 中国OSSモデル: 複雑でないタスクで競争力
  - Meta戦略: モデル層コモディティ化→コンピュート層で価値捕捉
  - DeepSeek V4-Flash: $0.14で実用的性能
- **引用URL:** https://www.mindstudio.ai/blog/what-is-meta-muse-spark-1-1-explained
- **Evidence ID:** EVD-20260714-0055

---

## KIQ-003-04: 資金調達・投資動向

### INFO-056
- **タイトル:** SambaNova valued $11B, Anthropic IPO target $1T, AI VC $131.5B up 52% YoY
- **ソース:** CNBC / Fortune / Qubit Capital
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** SambaNova, Anthropic, OpenAI
- **要約:** SambaNovaが$10億調達で評価額$110億。AnthropicはIPO評価額$1兆を目標（2026年後半）。AIスタートアップVC投資$1315億（前年比52%増）。2025年にAIが全世界のスタートアップ資金調達の50%近くを獲得（$2023億）。但し70-90%のAIスタートアップが18ヶ月以内に倒産・買収される予測。
- **キーファクト:**
  - SambaNova: $10億調達、評価額$110億（General Atlantic主導）
  - Anthropic: IPO評価額$1兆目標（2026年後半）
  - AI VC: $1315億（YoY +52%）
  - 2025年AIがスタートアップ資金の50%、$2023億
  - 70-90%のAIスタートアップが18ヶ月以内に倒産予測
- **引用URL:** https://www.cnbc.com/2026/07/08/sambanova-ai-chip-funding-valuation.html
- **Evidence ID:** EVD-20260714-0056

### INFO-057
- **タイトル:** Meta Louisiana data center reaches $50 billion — 5GW Hyperion supercluster
- **ソース:** CNBC / Fox Business / Yahoo Finance
- **公開日:** 2026-07-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Meta
- **要約:** MetaのルイジアナHyperionデータセンターが5GW規模・$500億超に拡大。稼働時に1000人以上の雇用を支える。新政権は$5000億のインフラ投資目標を設定、多くがAIデータセンターに向けられる。ByteDanceはブラジルに$390億のデータセンターを建設中。
- **キーファクト:**
  - Meta Hyperion: 5GW、$500億超（ルイジアナ）
  - 稼働時1000人以上の雇用
  - 政権: $5000億インフラ投資目標
  - ByteDance: ブラジルに$390億データセンター
- **引用URL:** https://www.cnbc.com/2026/07/13/meta-louisiana-data-center-investment-reaches-50-billion-amid-ai-push.html
- **Evidence ID:** EVD-20260714-0057

---

## KIQ-003-05: スイッチングコストとベンダーロックイン

### INFO-058
- **タイトル:** HBR: "You Outsourced the AI but You Still Own the Risk" — AI vendor lock-in highest-risk decision
- **ソース:** Harvard Business Review
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** （業界一般）
- **要約:** HBR分析: AIベンダーロックインはエンタープライズソフトウェアの伝統的ロックインとは異なる。単一プロバイダーが価格・可用性・モデル挙動を同時に制御し、独自のスケジュールで変更可能。542社調査で「ポータブルと思っているシステム」と「実際のポータビリティ」に大きなギャップ。AIモデル市場の分断が急速に進み、ロックインがエンタープライズテックの最高リスク決定に。
- **キーファクト:**
  - AIロックイン: 価格/可用性/モデル挙動の三者同時制御
  - 542社調査: 知覚ポータビリティと実際のギャップ
  - モデル市場の急速分断でロックインが最高リスク
  - 企業のアウトソーシングでもリスクは残存
- **引用URL:** https://hbr.org/2026/07/you-outsourced-the-ai-but-you-still-own-the-risk
- **Evidence ID:** EVD-20260714-0058

---

## KIQ-004-02: コーディング能力の市場価値変化

### INFO-059
- **タイトル:** GitHub Copilot 82% enterprise adoption, Claude Code 53% overall; junior dev postings down 34%
- **ソース:** Uvik / HowToGeek / Techmeme
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft, Anthropic
- **要約:** GitHub Copilot: Fortune 100の90%導入、大企業82%採用、470万人有料ユーザー。Claude Code: 全体採用率53%で首位（大企業では18%でCopilotの29%に次ぐ）。ジュニア開発者求人は34%減少。ソフトウェアエンジニアリングの求人は2020年比35%減、2022年ブーム比3.5分の1。但しBLSは15%成長を予測。
- **キーファクト:**
  - GitHub Copilot: Fortune 100の90%、大企業82%、470万人有料
  - Claude Code: 全体53%（首位）、大企業18%
  - Cursor: 470万人+有料、エンタープライズ採用強い
  - ジュニア開発者求人: -34%（投稿数）
  - ソフトウェアエンジニア求人: 2020年比-35%、2022年比1/3.5
  - BLS: ソフトウェア開発者15%成長予測（矛盾）
- **引用URL:** https://uvik.net/blog/ai-coding-assistant-statistics/
- **Evidence ID:** EVD-20260714-0059

---

## KIQ-004-03: AI代替困難な能力の市場価値

### INFO-060
- **タイトル:** Skills centered on judgment, design, accountability proving most durable in AI era
- **ソース:** Business Insider / WEF
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界一般）
- **要約:** AI時代に最も耐久性のあるスキルは「判断力・設計力・説明責任」。WEF 2030年に最も重要となる4スキルはいずれも技術的でない。AIプルーフ職業: 医療、熟練トレード、セラピスト、教育者、クリエイティブディレクター、法務、サイバーセキュリティ。
- **キーファクト:**
  - 最耐久スキル: 判断力・設計力・説明責任
  - WEF 2030重要4スキル: 全て非技術的
  - AIプルーフ職業: 医療/トレード/セラピスト/教育/クリエイティブ/法務/セキュリティ
  - メタスキルへの統合が進む（複数職務を1メタスキルに集約）
- **引用URL:** https://www.facebook.com/businessinsider/posts/1398334792164801/
- **Evidence ID:** EVD-20260714-0060

---

## KIQ-005-01: AGI到達度のベンチマーク指標と能力進展

### INFO-061
- **タイトル:** Recursive self-improvement research advances — arxiv paper, RSI Index 57.9%
- **ソース:** arXiv / Anthropic / OpenAI
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI, Anthropic
- **要約:** Recursive Self-Improvement (RSI)の学術研究が進展。arXiv論文: LLMが自己出力の批判・修正、自己生成データでの訓練、エージェント足場の書き直しを実行。GPT-5.6 Sol RSI Index 57.9%（GPT-5.5比+16.2pt）。AnthropicのRSI研究がAGI議論を再活性化。但し「ソフトペース」のRSIで人間が追いつけるという見方も。
- **キーファクト:**
  - arXiv論文: LLMによる自己批判/修正/足場書き直しの実行
  - GPT-5.6 Sol RSI Index: 57.9%（+16.2pt vs GPT-5.5）
  - 内部研究推論コンピュート6ヶ月で100倍増
  - Anthropic RSI研究がAGI議論を再活性化
  - 2028年にRSI能力が出現との予測あり
- **引用URL:** https://arxiv.org/html/2607.07663
- **Evidence ID:** EVD-20260714-0061

---

## KIQ-005-02: 主要CEO/研究者のAGIタイムライン予測

### INFO-062
- **タイトル:** WEF 2026 AGI debate — Hassabis 50% by 2030, Amodei 50-100 years of biology in 5-10 years
- **ソース:** WEF 2026 / Washington Stand / Genesis Human Experience
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Anthropic, Google DeepMind
- **要約:** WEF 2026でAGIタイムライン議論: AGIは2030年までに出現の可能性、リスクで人類を永続的に破壊しうる。Hassabis: 10年以内にAGIの約50%確率を再確認。Amodei: 強力なAIが50-100年の生物学的進歩を5-10年に圧縮。Altman: AGIリスクを警告。CEO間でタイムライン予測が分裂中。
- **キーファクト:**
  - WEF 2026: AGIは2030年までに出現可能性
  - Hassabis: 10年以内AGI約50%確率（再確認）
  - Amodei: 50-100年の生物学的進歩を5-10年に圧縮予測
  - Altman: AGIリスク警告
  - CEO間のタイムライン予測分裂
- **引用URL:** https://www.facebook.com/perfology/posts/1559154725945562/
- **Evidence ID:** EVD-20260714-0062

---

## KIQ-005-03: AGI安全性とガバナンスの政策議論

### INFO-063
- **タイトル:** AI Data Center Moratorium Act debate, AI Safety Institutes expanding globally
- **ソース:** Federal Debate / Future of Life / Canadian AISI
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** （政府・規制団体一般）
- **要約:** AIデータセンター猶予法の連邦議論が技術進歩とリスク管理の深い対立を顕在化。Future of Life AI Safety Index: 業界の軍事AI転向を「現状リスク」と指摘、政府ガイダンスへの完全委譲は「妥協」と評価。カナダ・豪州・英国のAI Safety Instituteが世界最先端モデルのテストを開始。政府主導プロジェクトで国際的連携テストを実施。
- **キーファクト:**
  - AI Data Center Moratorium Act: 連邦議論で深い対立
  - AI Safety Index: 軍事AI転向を現状リスクと分類
  - カナダ/豪州/英国のAI Safety Instituteが最先端モデルテスト
  - 政府ガイダンスへ完全委譲は「妥協」と評価
  - 国際的連携テストを実施
- **引用URL:** https://futureoflife.org/ai-safety-index-summer-2026/
- **Evidence ID:** EVD-20260714-0063

---

## BYTEDANCE-CHINESE: ByteDance/Doubao/Seed中国語一次情報

### INFO-064
- **タイトル:** ByteDance Seedream 5.0 Pro released — multimodal image creation with design understanding
- **ソース:** ByteDance Seed公式ブログ
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがSeedream 5.0 Pro（多モーダル画像作成モデル）を発表。テキスト一致・構造妥当性・テキストレンダリング・画質の基礎能力を全面的に向上。インタラクティブ精準編集（点選/圏選/スケッチレンダリング/色素材材替换/图层分离）、10以上の言語の直接入力と高品質レンダリングをサポート。火山方舟体験センターで提供開始。
- **キーファクト:**
  - Seedream 5.0 Pro: 多モーダル画像作成モデル
  - ピクセル級編集: 点選/圏選/スケッチ/色彩材質置換/图层分離
  - 10以上の言語の直接入力と高品質レンダリング
  - 火山方舟体験センターで提供開始
- **引用URL:** https://seed.bytedance.com/zh/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro
- **Evidence ID:** EVD-20260714-0064

### INFO-065
- **タイトル:** ByteDance Seedance 2.5 — native 30-second cinematic video, 50 multimodal references
- **ソース:** ByteDance Volcano Engine Conference
- **公開日:** 2026-07-11
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがVolcano EngineカンファレンスでSeedance 2.5を発表。ネイティブ30秒のシネマティックAI動画生成、最大50のマルチモーダル参照（画像/音声/動画/3D）をサポート。ネイティブ2K、30fps。Dreamina（CapCut AI）経由で提供。グローバル展開を開始。
- **キーファクト:**
  - Seedance 2.5: ネイティブ30秒動画生成
  - 最大50のマルチモーダル参照アセット
  - ネイティブ2K、30fps
  - Dreamina（CapCut AI）経由で提供
  - グローバル早期アクセス開始
- **引用URL:** https://www.instagram.com/reel/Dar9OwPt3zA/
- **Evidence ID:** EVD-20260714-0065

### INFO-066
- **タイトル:** ByteDance $39 billion Brazil data center — AI infrastructure mega investment
- **ソース:** Inc Magazine
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** ByteDanceがブラジルの単一データセンターに$390億を投資。AIインフラ融資構造は「直接融資」が主流。SeedanceはByteDanceの内部エコシステムと深く統合されており、独立分社化の可能性は低い。
- **キーファクト:**
  - ブラジルデータセンター: $390億投資
  - AIインフラ融資は直接融資が主流
  - Seedance: 内部エコシステム深く統合、独立分社化可能性低
  - ByteDanceのグローバルインフラ拡大
- **引用URL:** https://www.facebook.com/Inc/posts/1382038257121898/
- **Evidence ID:** EVD-20260714-0066

### INFO-067
- **タイトル:** 可灵 (Kling) AI独立後拿下$30億融資 — 中国AI動画競争下半場
- **ソース:** EastMoney / Moomoo
- **公開日:** 2026-07-13
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** 快手 (Kuaishou), ByteDance
- **要約:** 快手の可霊AI業務が独立後、初回増資で約138億元（約$20億）を調達、追加投資家15社と契約で総額約$30億に達する見通し。BAT（Baidu/Alibaba/Tencent）が歴史的に同時に可霊AIに投資。ByteDanceのSeedanceとの競争が激化。SeedanceはByteDance内部生態系と深度結合、独立分社化可能性低。
- **キーファクト:**
  - 可霊AI: 初回約138億元（約$20億）、追加投資家15社
  - 総額約$30億見通し
  - BAT（Baidu/Alibaba/Tencent）が同時に投資（歴史的）
  - 中国AI動画競争の「連盟時代」突入
- **引用URL:** https://caifuhao.eastmoney.com/news/20260713113846350717830
- **Evidence ID:** EVD-20260714-0067

### INFO-068
- **タイトル:** ByteDance EdgeBench — measuring real-world environment learning, new scaling law discovered
- **ソース:** ByteDance Seed Research Blog
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-005-01
- **関連企業:** ByteDance
- **要約:** ByteDanceが真世界環境学習を測定する超長期評価セットEdgeBenchを発表。新しいScaling Lawを発見。412のオープンソースリポジトリを公開、長期間自律エージェントハーネスを含む。
- **キーファクト:**
  - EdgeBench: 真世界環境学習の超長期評価セット
  - 新しいScaling Lawの発見
  - 412のオープンソースリポジトリ公開
  - 長期間自律エージェントハーネス（SuperAgent）
- **引用URL:** https://seed.bytedance.com/zh/blog/edgebench-measuring-real-world-environment-learning-and-discovering-a-new-scaling-law
- **Evidence ID:** EVD-20260714-0068

---

## KIQ-002-03 (補完): AIエージェント規制・安全基準

### INFO-069
- **タイトル:** China introduces AI agent and anthropomorphic AI rules; Illinois enacts AI Safety Measures Act; EU AI Act enforcement begins
- **ソース:** IAPP / Foley & Lardner
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （政府・規制団体一般）
- **要約:** 中国がAI倫理・AIエージェント・ヒューマノイドAIに関する3つの新規制を導入、幅広いAI規制から特定領域への移行を示す。イリノイ州がAI Safety Measures Actを制定。EU AI Actはリスクレベル別のAIシステム分類とコンプライアンス義務を課す。グローバル規制の執行フェーズが本格化。
- **キーファクト:**
  - 中国: AIエージェント・ヒューマノイドAIの3新規制導入
  - イリノイ州: AI Safety Measures Act制定
  - EU AI Act: リスク分類別コンプライアンス義務の執行開始
  - AIエージェントの非人間アクセス管理が新たなコンプライアンス課題
- **引用URL:** https://iapp.org/news/a/china-s-new-ai-rules-ethics-ai-agents-and-anthropomorphic-ai
- **Evidence ID:** EVD-20260714-0069

---

## KIQ-004-01 (補完): CyberAgent AI自動化

### INFO-070
- **タイトル:** CyberAgent proprietary advertising LLM streamlines ad copy, banners, videos; internet ad revenue ¥468B
- **ソース:** note.com / SimplyWallSt
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgentが広告特化の独自LLMを発表、広告コピー・バナー・動画の作成プロセスを大幅に合理化。インターネット広告収入は¥4682億、ゲーム¥2592億、メディア&IPが続く。広告事業のAI自動化が収益の主要ドライバー。
- **キーファクト:**
  - CyberAgent広告特化LLM: コピー/バナー/動画作成の自動化
  - インターネット広告収入: ¥4682億
  - ゲーム収入: ¥2592億
  - 広告AI自動化が収益の主要ドライバー
- **引用URL:** https://note.com/bunsekiya_tech/n/n056ba6caa597
- **Evidence ID:** EVD-20260714-0070

---

## KIQ-005-02 (補完): LeCun/Bengio/Hinton AGI観

### INFO-071
- **タイトル:** LeCun: LLMs not enough for AGI, new architectures needed; Bengio AI for Good keynote; Hinton warns of "new species"
- **ソース:** AI for Good Summit 2026 / Lifeboat
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** （学術一般）
- **要約:** Yann LeCun: 現在のLLMは強力だがAGIには不十分、次単語予測を超える新アーキテクチャが必要。モデルに過度な自律性を与えることは危険。Yoshua Bengio: AI for Good Summit 2026で基調講演。Geoffrey Hinton: 「新種が現れており、止められない」と警告。3人のチューリング賞受賞者の間でAGI観が分裂。
- **キーファクト:**
  - LeCun: LLMはAGIに不十分、新アーキテクチャ必要、過度な自律性は危険
  - Bengio: AI for Good Summit 2026基調講演
  - Hinton: 「新種が出現、停止不可」
  - 3チューリング賞受賞者間でAGI観が分裂
- **引用URL:** https://lifeboat.com/blog/2026/07/the-godfather-of-ai-a-new-species-is-emerging-and-we-cant-stop-it-geoffrey-hinton-nobel
- **Evidence ID:** EVD-20260714-0071

---

## KIQ-005-03 (補完): AIアライメント研究資金動向

### INFO-072
- **タイトル:** UN Independent International Scientific Panel releases AI preliminary report; UC Berkeley CHAI fully-funded fellowship; federal AI degree funding +18%
- **ソース:** United Nations / UC Berkeley CHAI
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** （政府・学術一般）
- **要約:** 国連独立国際科学パネルがAIの暫定報告書を公表、能力・機会・リスクの科学的評価を実施。UC Berkeley CHAIがAIアライメント研究の完全資金付きフェローシップを提供（MATS 12週間）。連邦AI学位資金援助は18%増加。アライメント研究への投資は拡大するが、能力向上のペースには追いつかない。
- **キーファクト:**
  - 国連: AI暫定科学的評価報告書公表
  - UC Berkeley CHAI: 完全資金付きアライメント研究フェローシップ
  - MATS: 12週間のAIアライメント/制御/セキュリティ/ガバナンス研究プログラム
  - 連邦AI学位資金: 18%増（2026年）
- **引用URL:** https://www.un.org/independent-international-scientific-panel-ai/sites/default/files/2026-07/en_Preliminary%20Report_.pdf
- **Evidence ID:** EVD-20260714-0072

---

## KIQ-003-03 (補完): Mistral/OSS企業導入

### INFO-073
- **タイトル:** Mistral 8 fully open-source for enterprise; OSS models match closed on benchmarks but 80% of spend still goes to paid
- **ソース:** Layer3Labs / Medium / SecondTalent
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral, Meta, Google
- **要約:** Mistral 8がエンタープライズ向け完全オープンソースモデルとして発表。2026年にOSS LLMはほぼ全ベンチマークでクローズドモデルに追いついたが、企業支出の80%は依然有料モデルへ。Mistral Large 3は$2/$6（入力/出力 per 1M tokens）。企業はデプロイ・スケーラビリティ・セキュリティで評価し、性能以外の要因でクローズドを選択。
- **キーファクト:**
  - Mistral 8: エンタープライズ向け完全OSS
  - 2026年: OSSがほぼ全ベンチマークでクローズドに追いつく
  - 企業支出の80%は依然有料モデルへ
  - Mistral Large 3: $2/$6 per 1M tokens
  - 選択理由: 性能以外にデプロイ/スケーラビリティ/セキュリティ
- **引用URL:** https://medium.com/@mayhemcode/open-source-llms-caught-up-in-2026-so-why-are-companies-still-paying-for-ai-df75d866c657
- **Evidence ID:** EVD-20260714-0073

---

## BYTEDANCE-CHINESE (補完): 豆包ユーザー数・収益

### INFO-074
- **タイトル:** 豆包月活3.45亿、日活1.4亿、日均Token 120万亿 — 但日营收不足100万元
- **ソース:** 凤凰网 / 36氪 / 新浪
- **公開日:** 2026-07-13
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 豆包App: 2026年Q1月活3.45亿（国内C端AI首位）、日活約1.4亿（春節後に2亿突破）。日均Token使用量120万亿（不到2ヶ月で60%増）。但し日营收不足100万元、日烧数千万元。豆包の後は千問1.66亿月活、DeepSeek 1.27亿月活。字节は数十名の従業員を集め豆包ナビゲーション機能を開発中。
- **キーファクト:**
  - 豆包月活: 3.45亿（2026 Q1、国内C端AI首位）
  - 日活: 約1.4亿（春節後に2亿突破歴史あり）
  - 日均Token: 120万亿（2ヶ月未満で60%増）
  - 日营收: 不足100万元（日烧数千万元との大差）
  - 競合: 千問1.66亿月活、DeepSeek 1.27亿月活
  - 字节: 数十名を集め豆包ナビゲーション開発中
- **引用URL:** https://view.inews.qq.com/a/20260707A0BGN800
- **Evidence ID:** EVD-20260714-0074

---

## KIQ-002-05 (補完): プラットフォームAI内製化・スマイルカーブ

### INFO-075
- **タイトル:** Brands in-house ad production via AI (Midjourney/Stable Diffusion); Meta Muse Image AI to Advantage+; smile curve middle layer compressed
- **ソース:** okoone / AdAge / LinkedIn
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Midjourney, Stability AI
- **要約:** グローバルブランドがAIで広告制作を内製化、タイムライン短縮とコスト削減を実現。MetaはMuse Image AIをAdvantage+に統合、ブランドは商品画像と予算だけで広告作成・ターゲティングが可能に（年末ローンチ目標）。かつてフォトグラファーや代理店に依頼していた製品写真をMidjourney/Stable Diffusionで内製化。「情報を上下に伝達する中間層」がAIにより不要になり、スマイルカーブ中間層が圧縮される。
- **キーファクト:**
  - 広告制作内製化: AI でタイムライン短縮・コスト削減
  - Meta Muse Image AI: Advantage+統合、商品画像+予算だけで広告作成
  - Midjourney/Stable Diffusion: 製品写真の内製化
  - スマイルカーブ中間層: 「情報伝達の中間層」がAIで不要化
  - AI賃金圧縮・富集中リスク（Harari指摘）
- **引用URL:** https://www.okoone.com/spark/marketing-growth/how-ai-is-bringing-ad-production-back-inside-companies/
- **Evidence ID:** EVD-20260714-0075

---

## Step 4: ディープスクレイプ（重要記事詳細取得）

### INFO-076 [DEEP SCRAPE]
- **タイトル:** AI Safety Index Summer 2026 — Full scorecard: Anthropic C+ (2.66), OpenAI C (2.28), Google C (2.01), Meta D+ (1.32), xAI F (0.65), DeepSeek F (0.47), Mistral F (0.33)
- **ソース:** Future of Life Institute (FLI)
- **公開日:** 2026-07-01
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-03, KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google DeepMind, Meta, xAI, DeepSeek, Mistral, Z.ai, Alibaba
- **要約:** FLI第3回AI Safety Index（7名の専門家パネル、37指標・6ドメイン）。全体ランキング: Anthropic C+ (2.66) > OpenAI C (2.28) > Google DeepMind C (2.01) > Meta D+ (1.32) > Z.ai D- (0.88) > Alibaba D- (0.87) > xAI F (0.65) > DeepSeek F (0.47) > Mistral F (0.33)。主要発見: (1) 業界全体の軍事AI転向を「新興現状リスク」と指摘、Anthropicはミナブ学校空爆との関連で批判、(2) 安全枠組みの後退: 一時停止コミットメントの放棄が業界全体に波及、(3) Existential Safetyは全業界で最弱ドメイン（最高でもC-）、(4) 安全レトリックが実際の行動を上回る、(5) Metaは6位→4位に改善、xAIは4位→7位に悪化。
- **キーファクト:**
  - Anthropic: C+ 2.66（首位、6ドメイン中5つで首位、RSP3.0の一時停止コミットメント後退で信頼性低下）
  - OpenAI: C 2.28（Risk Assessment首位、安全諮問グループの経営層オーバーライドリスク）
  - Google DeepMind: C 2.01（Frontier Safety Framework更新も一時停止コミットメント後退）
  - Meta: D+ 1.32（6位→4位改善、非毀損契約の強制執行で内部告発抑制）
  - xAI: F 0.65（4位→7位悪化、安全チームの存在証拠なし、危険能力評価に重大な欠落）
  - DeepSeek: F 0.47（安全枠組みなし、政府ガイダンスへの完全委譲）
  - Mistral: F 0.33（最下位、フロンティアリスクを一貫して軽視）
  - Existential Safety: 全社C-以下、detection≠preventionの指摘
  - 軍事AI転向: 2024-2026でAnthropic/OpenAI/Google/Metaが軍事応用禁止を撤回
  - データ収集期限: 2026年6月3日
- **引用URL:** https://futureoflife.org/ai-safety-index-summer-2026/
- **Evidence ID:** EVD-20260714-0076

### INFO-077 [DEEP SCRAPE]
- **タイトル:** HBR "You Outsourced the AI but You Still Own the Risk" — 4 hidden exposure areas: upstream opacity, customization boomerang, illusion of off-switch, fragmentation fallacy
- **ソース:** Harvard Business Review
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-05, KIQ-002-03
- **関連企業:** （業界一般）, OpenAI, Anthropic
- **要約:** HBR分析（Harvard Kennedy School上級フェロー執筆）: AIサプライチェーンは3層構造（フロンティアラボ→エンタープライズ→エンドユーザー）、中間層（エンタープライズ）に責任が集中。4つの隠れたリスク曝露領域: (1) 上流ブラックボックス: AIシステムは確率論的でドリフトする、ベンダーのモデルカードは研究コミュニティ向けで企業コンプライアンス不十分、(2) カスタマイズブーメラン: ファインチューニングでEU AI Act第25条下で「deployer」から「provider」に再分類される可能性、(3) オフスイッチの幻想: AIデプロイは「Jenga」のようなもの、モデルは耐力部品、(4) 分断の罠: 同一システムがEU/AAPC/各州で異なる要件。Peloton/iTutorGroup/Workday/Cignaの訴訟事例。MCPは接続層を標準化するがオーケストレーション/プロンプト/評価/ガバナンスは移行不可。
- **キーファクト:**
  - 4リスク: 上流不透明性/カスタマイズ責任/ベンダー依存/規制分断
  - AIサプライチェーン3層: ラボ→エンタープライズ→ユーザー（中間層に責任集中）
  - Peloton判例: 第三者ベンダーのチャットボットでも企業が責任
  - iTutorGroup: EEOCがAIプロバイダー而非企業を提訴
  - Workday: エージェント理論で雇用差別責任
  - EU AI Act 第25条: カスタマイズでdeployer→provider再分類
  - MCP: 接続層のみ標準化、ロックイン解消せず
  - 推奨: NIST AI RMF/ISO 42001をベースライン採用
- **引用URL:** https://hbr.org/2026/07/you-outsourced-the-ai-but-you-still-own-the-risk
- **Evidence ID:** EVD-20260714-0077

### INFO-078 [DEEP SCRAPE]
- **タイトル:** MIT Sloan research: OSS models reach 90% of closed performance, but 80% of token spend still goes to paid models
- **ソース:** Medium (citing MIT Sloan Frank Nagle / Georgia Tech Daniel Yue)
- **公開日:** 2026-07-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek, Meta, Alibaba, Anthropic, OpenAI
- **要約:** MIT SloanのFrank NagleとGeorgia TechのDaniel Yueによる研究: OSSモデルは公開時にクローズドモデルの約90%の性能に到達し、数ヶ月以内に残差を埋める。それでもクローズドモデルが全世界トークン使用量の約80%を占める。OSSランドスケープは2年前と別物: Meta Llamaに加えDeepSeek/Qwen/Kimi/GLM/Gemma/Phiが多数世代をリリース、リリース間隔は短縮中。2026年1月にSOTAだったモデルが6月には陳腐化。Anthropicの経済データ: コーディングタスクがAPI使用の大部分を占め、コーディングはOSSが最大の飛躍を遂げた領域。
- **キーファクト:**
  - OSS性能: クローズドの約90%（公開時）、数ヶ月で残差埋める
  - トークン使用量: クローズド80%、OSS20%
  - OSSプレイヤー: DeepSeek/Qwen/Kimi/GLM/Gemma/Phi + Meta Llama
  - リリース間隔: 急速に短縮、1月SOTA→6月陳腐化
  - コーディング: API使用の大部分、OSS最大飛躍領域
  - 価格差: OSSはクローズドの極小コスト
- **引用URL:** https://medium.com/@mayhemcode/open-source-llms-caught-up-in-2026-so-why-are-companies-still-paying-for-ai-df75d866c657
- **Evidence ID:** EVD-20260714-0078
