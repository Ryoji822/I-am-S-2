# 収集データ: 2026-07-11

## メタデータ
- 収集日時: 2026-07-11 00:00 UTC
- 品質フラグ: COMPLETE
- INFOエントリ数: 84
- Evidence ID範囲: EVD-20260711-0001 〜 EVD-20260711-0084
- 実行クエリ数: ~75（collection_plan.json全24 KIQ中22 KIQカバレッジ + Arbiter動的5クエリ）
- 詳細スクレイプ数: 8（公式ブログ4 + 重要記事4）
- KIQカバレッジ:
  - KIQ-001-01〜05: ✓ 完了
  - KIQ-002-01〜06: ✓ 完了
  - KIQ-003-01〜05: ✓ 完了
  - KIQ-004-01〜04: ✓ 完了
  - KIQ-005-01〜03: ✓ 完了
  - BYTEDANCE-CHINESE: ✓ 完了
  - Arbiter動的 KIQ-MIL-001: ✓ 完了
  - Arbiter動的 KIQ-OAI-001: ✓ 完了
  - Arbiter動的 KIQ-ANT-002: ⚠ 部分的（socket error、データ継続不在）
  - Arbiter動的 KIQ-CAR-002-OPS: ✓ 完了
  - Arbiter動的 KIQ-NEW-001: ✓ 完了
- 企業別カバレッジ:
  - Anthropic: 18件
  - OpenAI: 15件
  - Google/DeepMind: 8件
  - xAI/SpaceXAI: 4件
  - ByteDance: 8件
  - その他/業界全体: 31件
- データギャップ:
  - KIQ-ANT-002 (Claude Code DAU/WAU): 16R+連続不在、socket errorにより未取得
  - Grok 4.5 詳細ページ: JSエラーにより本文取得不可

## 収集結果

### INFO-001
- **タイトル:** Higher usage limits for Claude and a compute deal with SpaceX
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01, KIQ-003-04
- **関連企業:** Anthropic, SpaceX, Amazon, Google, Microsoft, NVIDIA
- **要約:** AnthropicはSpaceXと計算能力パートナーシップを締結し、Colossus 1データセンターの全計算容量（300MW以上・220,000台以上のNVIDIA GPU）を月内に利用開始する。これに伴いClaude Codeの5時間レート制限をPro/Max/Team/Enterprise向けに倍増、ピーク時間制限を撤廃、Claude OpusモデルのAPIレート制限を大幅に引き上げた。過去の計算契約（Amazon 5GW・Google 5GW・Microsoft/NVIDIA $30B Azure・Fluidstack $50B）に追加される。
- **キーファクト:**
  - SpaceXのColossus 1データセンター全体の計算容量（300MW+・220,000+ NVIDIA GPU）を月内に利用開始
  - Claude Code 5時間レート制限を倍増（Pro/Max/Team/Enterprise）
  - Claude Opus APIレート制限を大幅引き上げ
  - 軌道型AI計算容量の開発にも関心を表明
  - 規制産業向けに国際的なリージョン拡張を計画
- **引用URL:** https://www.anthropic.com/news/higher-limits-spacex
- **Evidence ID:** EVD-20260711-0001

### INFO-002
- **タイトル:** KPMG integrates Claude across its core business and workforce of more than 276,000 in strategic alliance
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-001-03
- **関連企業:** Anthropic, KPMG
- **要約:** KPMG（138カ国・276,000+従業員）がAnthropicとグローバル提携を発表。ClaudeをDigital Gatewayプラットフォームに組み込み、CoworkとManaged Agentsを統合。税務・法定クライアント向けツールから展開し、全従業員がClaudeにアクセス可能に。AnthropicはKPMGをプライベートエクイティの優先パートナーに指名。サイバーセキュリティ脆弱性発見・修正にもClaudeを活用。
- **キーファクト:**
  - KPMG全276,000+従業員がClaudeにアクセス可能
  - Digital GatewayプラットフォームにClaude Cowork/Managed Agentsを統合
  - プライベートエクイティ向け優先パートナー指名
  - サイバーセキュリティ領域でのClaude活用
  - KPMG BlazeでClaude Codeを組み込みレガシーITの近代化を加速
  - UT Austinとの共同研究で「human in the loop」の価値を定量化
- **引用URL:** https://www.anthropic.com/news/anthropic-kpmg
- **Evidence ID:** EVD-20260711-0002

### INFO-003
- **タイトル:** Thoughts on America's AI Action Plan
- **ソース:** Anthropic公式ブログ（ポリシー）
- **公開日:** 2025-07-23
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropicがホワイトハウスの「Winning the Race: America's AI Action Plan」に対する見解を発表。AIインフラ加速・連邦政府採用強化・安全性テスト強化を支持。一方でH20チップの中国輸出制限維持を強く推奨。州レベルAI法の10年モラトリアムには反対。ASL-3保護をClaude Opus 4で事前発動したことを言及。
- **キーファクト:**
  - AI Action Planのインフラ・連邦採用・安全性テスト重点を支持
  - H20チップの対中輸出制限維持を強く推奨
  - フロンティアモデル透明性の国家標準化を推奨
  - 州レベルAI法の10年モラトリアムに反対
  - Claude Opus 4でASL-3保護を事前発動（CBRN悪用防止）
- **引用URL:** https://www.anthropic.com/news/thoughts-on-america-s-ai-action-plan
- **Evidence ID:** EVD-20260711-0003

### INFO-004
- **タイトル:** GPT-5.6: Frontier intelligence that scales with your ambition
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-003-01, KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI, Microsoft
- **要約:** OpenAIがGPT-5.6ファミリー（Sol/Terra/Luna）を一般提供開始。SolはAgents' Last Exam 53.6%（Claude Fable 5を13.1ポイント上回る）を達成。新機能「ultra」はデフォルトで4エージェントを並列協調。Programmatic Tool CallingでZDR互換のインメモリプログラム実行。価格はSol $5/$30、Terra $2.50/$15、Luna $1/$6（per 1M tokens）。GPT-5.6はMicrosoft 365 Copilotの優先モデルにも指定。AI研究内製化の加速: 研究者あたり日産トークン数がGPT-5.5比2倍以上、内部推論計算100倍成長。RSI Index 57.9%（GPT-5.5比+16.2pt）。
- **キーファクト:**
  - GPT-5.6 Sol: Agents' Last Exam 52.7%、Terminal-Bench 2.1 88.8%(Ultra 91.9%)、BrowseComp 90.4%(Ultra 92.2%)、OSWorld 2.0 62.6%
  - Artificial Analysis Coding Agent Index v1.1: 80（Fable 5より2.8pt上・トークン半分・時間半分・コスト約1/3）
  - 価格: Sol $5/$30、Terra $2.50/$15、Luna $1/$6（per 1M tokens）
  - ARC-AGI-3: Sol 7.78%（前世代0.43%から初の有意義な進歩）
  - ExploitBench: 73.5%（GPT-5.5 47.9%から大幅向上）、SEC-Bench Pro 71.2%
  - RSI Index: 57.9%（GPT-5.5比+16.2pt）—再帰的自己改善能力の測定
  - 内部研究計算100倍成長、エージェント的トークン使用22倍成長
  - Programmatic Tool Calling: インメモリプログラム実行でZDR互換
  - 70万A100e GPU時間の自動レッドチーミング実施
  - 生物・サイバーいずれもCritical閾値未到達
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260711-0004

### INFO-005
- **タイトル:** Introducing GPT-Live
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-Live（GPT-Live-1/mini）を発表。フルデュープレックス（同時聴き・話し）音声モデルで、ChatGPT Voiceを強化。GPT-5.5をバックグラウンド委譲先として使用し、検索・推論タスクを処理しながら会話継続可能。週1.5億人がVoice機能を使用。Advanced Voice Mode比で75.7%の会話優位性。GPQA 84.2%（AVM 45.3%）、BrowseComp 75.2%（AVM 0.7%）。
- **キーファクト:**
  - フルデュープレックス音声アーキテクチャ（同時聴覚入力・音声出力）
  - GPT-5.5へのタスク委譲で継続的フロンティア知能統合
  - 週1.5億人がVoice/Dictation使用
  - GPT-Live-1 vs AVM ペアワイズ優先率75.7%
  - GPQA 84.2%（AVM 45.3%）、BrowseComp 75.2%（AVM 0.7%）
  - 9種類のリマスターされた音声ボイス
  - API提供予定（開発者登録受付中）
- **引用URL:** https://openai.com/index/introducing-gpt-live/
- **Evidence ID:** EVD-20260711-0005

### INFO-006
- **タイトル:** Introducing Grok 4.5
- **ソース:** SpaceXAI（旧xAI）公式ブログ
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** xAI (SpaceXAI)
- **要約:** SpaceXAI（xAIがSpaceXに統合後のブランド）がGrok 4.5を発表。コーディング・エージェントタスク・ナレッジワークに特化した最強モデル。詳細ページはJSエラーで取得できず、メタデータとサードパーティ報道から情報を補完。Grok 4.5は新アーキテクチャで動作し、コーディングとコスト競争力を重視。
- **キーファクト:**
  - Grok 4.5: SpaceXAI初の主要モデルリリース（xAI→SpaceXAI統合後）
  - コーディング・エージェントタスク・ナレッジワーク特化
  - 新アーキテクチャ搭載
  - 7月6日に「21 New Flagship Grok Voices」「Voice Agent Builder」も発表済み
- **引用URL:** https://x.ai/news/grok-4-5
- **Evidence ID:** EVD-20260711-0006

### INFO-007
- **タイトル:** AlphaEvolve is available for everyone on Google Cloud
- **ソース:** Google Cloud Blog
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-002-01, KIQ-005-01
- **関連企業:** Google / DeepMind
- **要約:** GoogleがAlphaEvolve（Geminiベースのコード最適化・発見エージェント）をGemini Enterprise Agent PlatformでGA提供開始。物流・半導体・ゲノミクス・HPC・金融で実績。BASF（サプライチェーン80%向上）、Coolblue（需要予測5%向上）、FM Logistic（倉庫ルーティング10.4%改善）、Klarna（訓練スループット2倍）、JetBrains（IDE性能15-20%向上）、Schrödinger（分子発見4倍加速）等の事例。Google内でもTPUシリコン設計最適化・Spanner LSM compaction改善（書き込み増幅20%削減）等で成果。
- **キーファクト:**
  - AlphaEvolve GA on Gemini Enterprise Agent Platform
  - BASF: サプライチェーン計画・予測モデル80%向上
  - FM Logistic: 倉庫ルーティング10.4%改善（15,000km以上節約）
  - Klarna: ML訓練パイプライン・スループット2倍・モデル品質向上
  - JetBrains: IDE性能15-20%向上
  - Schrödinger: 分子発見4倍加速
  - Kinaxis: 予測精度22%向上・ランタイム90%削減
  - WPP: キャンペーン予測精度5-10%向上
  - Google内: TPU設計最適化・Spanner書き込み増幅20%削減・ストレージフットプリント9%削減
  - ORNL: Frontierスパコン上でGPUカーネル最適化
  - 量子計算: Willow量子プロセッサでエラー率10分の1の量子回路発見
- **引用URL:** https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-is-available-for-everyone
- **Evidence ID:** EVD-20260711-0007

---

## Arbiter動的追加クエリ（Step 1.5）

### 動的追加クエリ
- KIQ-MIL-001: "autonomous weapons human override rate military AI LAWS treaty 2026"
- KIQ-OAI-001: "OpenAI revenue breakdown government contracts vs commercial 2026"
- KIQ-ANT-002: "Claude Code daily active users usage metrics enterprise adoption 2026"
- KIQ-CAR-002-OPS: "design evaluation skills market value AI era quantitative premium 2026"
- KIQ-NEW-001: "Trump 5 percent equity stake AI companies government OpenAI Anthropic 2026"

### INFO-008
- **タイトル:** AI Safety Index — Summer 2026 (FLI)
- **ソース:** Future of Life Institute
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** FLIのSummer 2026 AI Safety IndexでAnthropicが安全性リーダーシップを維持しつつ、「questionable military engagements（疑問視される軍事契約）」でパネルから批判を受けた。自律兵器と国内監視の制限は評価されたが、軍事契約の拡大が懸念材料。30カ国がLAWS予防条約を要求。
- **キーファクト:**
  - Anthropic: AI Safety Index首位継続だが軍事契約で批判
  - 30カ国がLAWS（自律型致死兵器システム）予防条約を要求
  - 国連事務総長が自律兵器を「道義的に忌まわしい」と表現
  - 完全自律型AIドローンによる人間殺害の初確認報道
- **引用URL:** https://futureoflife.org/ai-safety-index-summer-2026/
- **Evidence ID:** EVD-20260711-0008

### INFO-009
- **タイトル:** OpenAI Vs Anthropic IPO: How They Compare And What We Know
- **ソース:** Forbes
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-OAI-001, KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** Anthropic評価額$113B（OpenAIを上回る）、Anthropic推定ARR $47B（OpenAIの約2倍）。OpenAIはQ2 2026収益$10.9B予想・一部営業利益予想。OpenAIはかつて消費者収益75%だった構成からの多様化を進めるが、政府vs民間の収益内訳は依然非開示。
- **キーファクト:**
  - Anthropic評価額$113B（OpenAI上回る）
  - Anthropic推定2026年ARR $47B（OpenAIの約2倍）
  - OpenAI Q2 2026収益予想$10.9B・一部営業利益予想
  - OpenAIは消費者収益75%から構成多様化を進行中
  - 政府 vs 民間収益内訳の開示は依然なし（KIQ-OAI-001継続不在）
- **引用URL:** https://www.forbes.com/sites/investor-hub/article/openai-vs-anthropic-ipo-comparison/
- **Evidence ID:** EVD-20260711-0009

### INFO-010
- **タイトル:** OpenAI 5% equity stake to US government — competing AI companies asked to match
- **ソース:** Fox Business / Instagram / Seeking Alpha (複数ソース)
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-NEW-001, KIQ-002-06
- **関連企業:** OpenAI, Anthropic, Google, Meta
- **要約:** Sam Altmanがトランプ政権との交渉でOpenAIの5%エクイティステーク（約$42.6B相当）の米国政府への無償提供を検討中。Anthropic・Google・Metaにもマッチング5%ステークの提供を求める構造。「American AI Sovereign Wealth Fund Act」法案では$200B以上の収益を持つ全AI企業に50%の一時税を課す内容も。Lutnick・Bessent・Sandersと協議中。政府によるAI企業への経済的圧力の新たな形。
- **キーファクト:**
  - OpenAIの5%ステーク（約$42.6B相当）を米国政府に無償提供を検討
  - Anthropic・Google・Metaにもマッチング5%提供を要求
  - AltmanがLutnick・Bessent・Sandersと協議
  - 「American AI Sovereign Wealth Fund Act」: $200B+収益AI企業に50%一時税
  - N=1の構造（OpenAI単独提案）は変わらずだが、法案化の動きが進行
- **引用URL:** https://www.facebook.com/FoxBusiness/posts/1559841842166804/
- **Evidence ID:** EVD-20260711-0010

### INFO-011
- **タイトル:** ByteDance's Coze Launches Version 2.5, Introducing 'Agent World' Ecosystem
- **ソース:** KuCoin News
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceのCozeプラットフォームがv2.5にアップデート。「Agent World」エコシステムを導入し、AIエージェントがチャットインターフェースを超えて動作可能に。独立実行環境・スキル・アイデンティティを備える。「Full」モードでエージェントが自律的にタスクを実行。
- **キーファクト:**
  - Coze v2.5: Agent Worldエコシステム導入
  - チャットUIを超えたエージェント自律実行
  - 独立実行環境・スキル・アイデンティティ付与
  - Fullモードで自律タスク実行
- **引用URL:** https://www.kucoin.com/news/flash/bytedance-s-coze-launches-version-2-5-introduces-agent-world-ecosystem
- **Evidence ID:** EVD-20260711-0011

### INFO-012
- **タイトル:** Expanding Managed Agents in Gemini API
- **ソース:** Google AI Blog
- **公開日:** 2026-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** Google / DeepMind
- **要約:** GoogleがGemini APIにManaged Agents機能を拡張。バックグラウンド実行（非同期インタラクション）・リモートMCPサーバー接続・カスタム関数・パッケージインストール・ファイル処理をサポート。単一エンドポイントでGeminiが推論・コード実行・ツール使用を統合処理。
- **キーファクト:**
  - Managed Agents: バックグラウンド実行・非同期インタラクション
  - リモートMCPサーバー接続サポート
  - カスタム関数・パッケージインストール・ファイル処理
  - 単一エンドポイントで推論+コード実行+ツール統合
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/
- **Evidence ID:** EVD-20260711-0012

### INFO-013
- **タイトル:** AI Agent Frameworks 2026: Production-Tested Ranking
- **ソース:** Alice Labs
- **公開日:** 2026-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI, Anthropic, Microsoft, CrewAI
- **要約:** 2026年のプロダクション対応AIエージェントフレームワーク比較: LangGraph 1.0、Claude Agent SDK、CrewAI 1.14、Microsoft Agent Framework 1.0をランキング。OpenAI Agents SDKはprovider-agnostic対応でBedrock上でも動作。
- **キーファクト:**
  - LangGraph 1.0: プロダクション対応リーディングフレームワーク
  - Claude Agent SDK: 強力なツール実行機能
  - CrewAI 1.14: マルチエージェント協調
  - Microsoft Agent Framework 1.0: AutoGen+Semantic Kernel統合
  - OpenAI Agents SDK: provider-agnostic（Bedrock互換）
- **引用URL:** https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026
- **Evidence ID:** EVD-20260711-0013

### INFO-014
- **タイトル:** xAI Expands Grok's Developer Stack With Voice and Agent Tools
- **ソース:** AllThingsElon
- **公開日:** 2026-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI (SpaceXAI)
- **要約:** SpaceXAIがGrok開発者スタックを拡張。25言語対応STT APIをGA提供、Grok Buildに自律/goalモードを追加。Grok 4.5はコーディング・エージェントタスク・ナレッジワーク向けフロンティアモデルとしてAPI提供中。
- **キーファクト:**
  - 25言語対応STT APIをGA提供
  - Grok Buildに自律/goalモード追加
  - Grok 4.5: コーディング・エージェント・ナレッジワーク特化
  - Agent Client Protocol対応
- **引用URL:** https://www.allthings-elon.com/articles/xai-grok-developer-platform-stt-goal-autonomous-2026
- **Evidence ID:** EVD-20260711-0014

### INFO-015
- **タイトル:** OpenAI Agents SDK — provider-agnostic on Amazon Bedrock
- **ソース:** LinkedIn / Gary Stafford
- **公開日:** 2026-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI, Amazon
- **要約:** OpenAI Agents SDKがAmazon Bedrock上でネイティブ動作。プロキシや変換レイヤー不要。ツール・ハンドオフ・ガードレール・トレーシング機能がapi.openai.comと同様にBedrock上で機能。provider-agnostic設計の実証。
- **キーファクト:**
  - OpenAI Agents SDKがBedrock上でネイティブ動作
  - プロキシ/変換レイヤー不要
  - ツール・ハンドオフ・ガードレール・トレーシング機能が完全動作
  - provider-agnostic設計の実証
- **引用URL:** https://www.linkedin.com/pulse/building-agentic-systems-openai-agents-sdk-amazon-gary-stafford-baf0c
- **Evidence ID:** EVD-20260711-0015

### INFO-016
- **タイトル:** Claude Agent SDK Python — latest releases
- **ソース:** GitHub (anthropics/claude-agent-sdk-python)
- **公開日:** 2026-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK Pythonがアクティブに開発継続。バンドルClaude CLIをv2.1.202に更新。E2Eテストの安定性改善。
- **キーファクト:**
  - バンドルClaude CLI v2.1.202に更新
  - E2Eテスト安定性改善
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-python/releases
- **Evidence ID:** EVD-20260711-0016

### INFO-017
- **タイトル:** Okta Integrates with Anthropic Claude Enterprise for Centralized Security Visibility
- **ソース:** Instagram / Okta
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic, Okta
- **要約:** OktaがAnthropic Claude Enterpriseと統合。セキュリティ・コンプライアンスチームにClaude EnterpriseとClaude Platformへの中央集権化された可視性を提供。
- **キーファクト:**
  - Okta-Claude Enterprise統合でSSO・アクセス管理の中央化
  - セキュリティ・コンプライアンスチームの可視性向上
- **引用URL:** https://www.instagram.com/p/DamEV7qn0nL/
- **Evidence ID:** EVD-20260711-0017

### INFO-018
- **タイトル:** AI Investment Is Shifting as Inference, Enterprise Adoption Accelerate
- **ソース:** Goldman Sachs
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-003-04
- **関連企業:** （業界全体）
- **要約:** Goldman Sachs分析: AI投資が推論・エンタープライズ採用へシフト。企業が急速にAIをデプロイし、コンピューティングインフラの試練となる。ファイバーオプティクスなどインフラ投資機会が創出。
- **キーファクト:**
  - AI投資シフト: 訓練→推論・エンタープライズ採用
  - コンピューティングインフラへの圧力拡大
  - ファイバーオプティクス等インフラ投資機会
- **引用URL:** https://www.goldmansachs.com/insights/articles/ai-investment-is-shifting-as-inference-enterprise-adoption-accelerate
- **Evidence ID:** EVD-20260711-0018

### INFO-019
- **タイトル:** Enterprise AI Adoption in 2026: What Delivery Data Reveals
- **ソース:** Kanerika / LinkedIn
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** エンタープライズAI採用データ: 改善の中央値47%、30%のエンゲージメントで90%以上達成。ボトルネックはほぼ常にモデルではなく、統合・データ・プロセス。Microsoft予測: 2028年までに13億のAIエージェントが稼働。160,000以上の組織が400,000以上のCopilot Studioエージェントをデプロイ。
- **キーファクト:**
  - エンタープライズAI改善中央値47%
  - 30%のエンゲージメントで90%以上達成
  - ボトルネックはモデルではなく統合・データ・プロセス
  - Microsoft予測: 2028年までに13億AIエージェント稼働
  - 160,000+組織が400,000+ Copilot Studioエージェントをデプロイ
- **引用URL:** https://www.linkedin.com/pulse/enterprise-ai-adoption-2026-what-delivery-data-reveals-kanerika-fstlc
- **Evidence ID:** EVD-20260711-0019

### INFO-020
- **タイトル:** Enterprise AI Adoption Statistics 2026
- **ソース:** Shuai Guan / Topickz
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** 2025年末で米国企業のAI採用率4%（FRB）。EU企業のAI使用率4.03%（Eurostat）。2026年調査: 62%の組織がAIエージェントを実験中、23%がスケーリング中。Gartner予測: 40%以上のCIOがAgentic AIを採用。88%がパイロット段階で停滞。
- **キーファクト:**
  - 米国企業AI採用率4%（2025年末FRB）
  - EU企業AI使用率4.03%（2025 Eurostat）
  - 62%がAIエージェント実験中、23%がスケーリング中
  - Gartner: 40%+のCIOがAgentic AI採用予測
  - 88%がパイロット段階で停滞（97%コミット/18%デプロイ）
- **引用URL:** https://shuaiguan.io/blog/enterprise-ai-adoption-statistics
- **Evidence ID:** EVD-20260711-0020

### INFO-021
- **タイトル:** 2026 Enterprise AI Agents: 5.8x ROI and 66% Productivity Gains
- **ソース:** GenerateForge AI
- **公開日:** 2026-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** 2026年のエンタープライズAIエージェントは実験的パイロットからプロダクション対応の自律的ワーカーへ移行。測定可能な5.8x ROIと66%の生産性向上を達成。
- **キーファクト:**
  - エンタープライズAIエージェント: 5.8x ROI
  - 66%の生産性向上
  - 実験→プロダクション移行の進展
- **引用URL:** https://generateforgeai.com/?p=55
- **Evidence ID:** EVD-20260711-0021

### INFO-022
- **タイトル:** EU AI Act August 2026: Compliance Countdown
- **ソース:** Responsible AI Labs / Lexology
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** 2026年8月2日にEU AI Actの大部分が施行。大企業のコンプライアンスコスト$8-15M（推定）。AIガバナンスプラットフォーム市場$492M（2026年予測）。78%の企業が準備不足。2026年6月1日に欧州委員会が科学パネル・諮問フォーラムを任命。EU AI Act修正はコンプライアンス負担を削減せず再構築。
- **キーファクト:**
  - 2026年8月2日: EU AI Act大部分施行
  - 大企業コンプライアンスコスト$8-15M
  - AIガバナンス市場$492M（2026年）
  - 78%の企業が準備不足
  - 欧州委員会: 科学パネル・諮問フォーラム任命（6月1日）
- **引用URL:** https://responsibleailabs.ai/knowledge-hub/articles/eu-ai-act-august-2026-compliance
- **Evidence ID:** EVD-20260711-0022

### INFO-023
- **タイトル:** June 2026 AI Executive Order & FTC AI Accuracy Policy
- **ソース:** Federal Register / Kiteworks / Babel Street
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** （政策・規制）
- **要約:** 2026年6月2日に大統領令14409「高度AIイノベーションとセキュリティの促進」発令。連邦政府インフラのAIリスク耐性強化と民間セクターとの協力を指示。7月7日にFTCが「AIシステムにおける正確性の抑制」に関する政策声明を提案。AIの意図的な正確性抑制を欺瞞行為として規制対象に。
- **キーファクト:**
  - 大統領令14409（6月2日）: 高度AIイノベーション・セキュリティ促進
  - 連邦政府インフラのAIリスク耐性強化を指示
  - FTC政策声明（7月7日）: AI正確性抑制を欺瞞行為として規制
  - 2026年EOはデータガバナンスの会話を変容
- **引用URL:** https://www.federalregister.gov/documents/2026/07/07/2026-13628/
- **Evidence ID:** EVD-20260711-0023

### INFO-024
- **タイトル:** MCP 2026 Specification Release Candidate — Stateless Protocol & Extensions
- **ソース:** MCP Blog / Azure DevOps
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** （標準化）
- **要約:** MCP（Model Context Protocol）の2026仕様リリース候補が公開。ステートレスプロトコルコア・Extensions フレームワーク・Tasks機能を導入。ハンドシェイク廃止、セッションヘッダー改善。スケーラビリティとセキュリティの大幅向上。7月15日にIANシンポジウムでMCPリスクと機会を議論。
- **キーファクト:**
  - MCP 2026 RC: ステートレスプロトコルコア導入
  - Extensions フレームワーク・Tasks機能追加
  - ハンドシェイク廃止・セッションヘッダー改善
  - スケーラビリティ・セキュリティ大幅向上
  - 7月15日シンポジウム: MCPリスクと機会
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260711-0024

### INFO-025
- **タイトル:** CData Joins Agentic AI Foundation (AAIF) — MCP Donated to Linux Foundation
- **ソース:** CData Blog / EnterpriseTalk
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic, Linux Foundation, AAIF
- **要約:** AAIF（Agentic AI Foundation）は2025年12月にAnthropicがMCPをBlock's gooseとともにLinux Foundationに寄贈して設立。CData・iTmethods等が新規加盟し、エコシステム拡大中。FINOSと協力して規制対象Agentic AIのガバナンス標準を推進。
- **キーファクト:**
  - AAIF: 2025年12月設立（AnthropicがMCP寄贈）
  - CData・iTmethods等が新規加盟
  - FINOSと協力: 規制対象Agentic AIガバナンス標準
  - Visa: 2026年にAIエージェントが購入を完遂すると宣言
- **引用URL:** https://www.cdata.com/blog/cdata-joins-agentic-ai-foundation
- **Evidence ID:** EVD-20260711-0025

### INFO-026
- **タイトル:** SkillCloak: Malicious AI Agent Skills Evade Static Scanners
- **ソース:** The Hacker News / Help Net Security
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Anthropic
- **要約:** 悪意のあるAIエージェントスキルが静的スキャナを回避する「SkillCloak」技術が発見された。OpenAI Skillsマーケットプレイスに数ヶ月で40,000以上のスキルが登録され、コミュニティ由来の大部分は未検証。Claude Code・OpenClaw等のツールでランタイムチェックが必要。OpenAIは2026年7月23日からEnterpriseワークスペースのSkillsをデフォルト有効化予定。
- **キーファクト:**
  - SkillCloak: 悪意あるスキルが静的スキャナを回避
  - OpenAI Skillsマーケットプレイス: 40,000+スキル（数ヶ月で登録）
  - コミュニティ由来スキルの大部分は未検証
  - OpenAI Skills: 7月23日からEnterpriseでデフォルト有効化
  - ランタイムチェック（Claude Code・OpenClaw等）が必要
- **引用URL:** https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html
- **Evidence ID:** EVD-20260711-0026

### INFO-027
- **タイトル:** Friendly Fire: Hijacking Defensive Cyber AI Agents for Remote Code Execution
- **ソース:** AI Now Institute
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-05, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** AI Now InstituteがOpenAI Codex CLIの不正コード実行を可能にするPoCエクスプロイトを公開。防御型フロンティアAIエージェントをハイジャックしてリモートコード実行を可能にする攻撃手法を開示。AIエージェントの実行環境のセキュリティリスクを実証。
- **キーファクト:**
  - OpenAI Codex CLIの不正コード実行PoC
  - 防御型AIエージェントのハイジャック
  - リモートコード実行が可能
  - エージェント実行環境の重大セキュリティリスク
- **引用URL:** https://ainowinstitute.org/publications/friendly-fire-exploit-brief
- **Evidence ID:** EVD-20260711-0027

### INFO-028
- **タイトル:** AWS Weekly Roundup: Claude Sonnet 5 on AWS, Amazon WorkSpaces for AI agents
- **ソース:** AWS News Blog
- **公開日:** 2026-07-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** Amazon, Anthropic
- **要約:** AWSでClaude Sonnet 5が利用可能に。Amazon WorkSpaces for AI agentsを発表。複数のサービスライフサイクル変更（6月30日更新: メンテナンス移行サービスは7月30日から新規顧客クローズ）。
- **キーファクト:**
  - AWS Bedrock: Claude Sonnet 5利用可能
  - Amazon WorkSpaces for AI agents発表
  - 複数サービスのライフサイクル変更
- **引用URL:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-sonnet-5-on-aws-amazon-workspaces-for-ai-agents-aws-service-availability-updates-and-more-july-6-2026/
- **Evidence ID:** EVD-20260711-0028

### INFO-029
- **タイトル:** Microsoft Foundry → M365: Publish Agents Directly into Copilot and Teams
- **ソース:** Microsoft DevBlogs
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-03
- **関連企業:** Microsoft
- **要約:** Microsoft Foundryで構築したエージェントをMicrosoft 365 CopilotとTeamsに数クリックで直接公開可能に。サーフェスごとに再構築不要。エージェントは元の機能を保持。Azure AIとM365がエンタープライズ制御を再構築。
- **キーファクト:**
  - FoundryエージェントをM365 Copilot/Teamsに直接公開
  - 数クリック・サーフェスごとの再構築不要
  - Azure AI + M365でエンタープライズ制御を再構築
- **引用URL:** https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/
- **Evidence ID:** EVD-20260711-0029

### INFO-030
- **タイトル:** Google Gemini Enterprise Agent Platform: Unified Build, Deploy, Govern
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** Google / DeepMind
- **要約:** Google Gemini Enterprise Agent PlatformはエンタープライズグレードAIエージェントとモデルベースソリューションを構築・デプロイ・ガバナンス・最適化する統合プラットフォーム。Vertex AI Agent Builderは開発者がプロダクションでAIエージェントを構築・スケール・ガバナンスするスイート。7月7日にGemini EnterpriseとGoogle Cloud Marketplaceでエージェント公開ガイドをリリース。
- **キーファクト:**
  - Gemini Enterprise Agent Platform: 統合プラットフォーム
  - 構築・デプロイ・ガバナンス・最適化の統合
  - Vertex AI Agent Builder: プロダクション対応エージェント構築
  - Cloud API Registry on Vertex AI Agent Engine でMCPデプロイ
  - 7月7日: エージェント公開ガイドリリース
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
- **Evidence ID:** EVD-20260711-0030

### INFO-031
- **タイトル:** Beijing Looking at Curbing Overseas Access to China's Top AI Models
- **ソース:** Reuters
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** ByteDance, Alibaba, DeepSeek
- **要約:** 中国政府が国内最先端AIモデルの海外アクセス制限を検討。AIの漏洩や窃盗が国家安全感の下で処罰対象となる可能性。国内AIスタートアップへの資金提供者にも新規制。双方向デカップリングの加速。同時に米国議会員が中国製AIモデルの成長する採用阻止を検討。
- **キーファクト:**
  - 中国: 最先端AIモデルの海外アクセス制限を検討
  - AI漏洩・窃盗を国家安全感の下で処罰対象に
  - 国内AIスタートアップ資金提供者に新規制
  - 米国議会: 中国製AIモデルの採用阻止を検討（CNBC）
  - 双方向デカップリングの加速
- **引用URL:** https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/
- **Evidence ID:** EVD-20260711-0031

### INFO-032
- **タイトル:** Senate Lawmaker Presses DoD, Tech Firms to Disclose AI Contract Terms
- **ソース:** Federal News Network
- **公開日:** 2026-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** Anthropic, OpenAI, Pentagon
- **要約:** 上院議員がDoDとテック企業にAI契約条項の開示を要求。国防総省はAnthropicが2つの限定的な契約制限条項（大量国内監視・自律型兵器使用拒否）の削除を拒否した後、「サプライチェーンリスク」指定。Dario Amodeiは「現在のAIシステムを大量国内監視や自律型兵器に使用することを許可しない」と明言。Reflection AI契約（トランプJr.がパートナーの企業が一部出資）に特に言及。
- **キーファクト:**
  - 上院: DoD・テック企業にAI契約条項開示要求
  - Anthropic: 2つの契約制限条項削除拒否で「サプライチェーンリスク」指定
  - Anthropic拒否内容: 大量国内監視・自律型兵器使用の拒否
  - Reflection AI契約: トランプJr.がパートナーの企業が出資
  - Dario Amodei: 「AIシステムの大量監視・自律兵器使用を許可しない」
- **引用URL:** https://federalnewsnetwork.com/congress/2026/07/senate-lawmaker-presses-dod-tech-firms-to-disclose-ai-contract-terms/
- **Evidence ID:** EVD-20260711-0032

### INFO-033
- **タイトル:** Warren Presses DoD for Answers on Military AI Contracts
- **ソース:** Sen. Elizabeth Warren (warren.senate.gov)
- **公開日:** 2026-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** OpenAI, Pentagon
- **要約:** ウォーレン上院議員がDoDに軍事AI契約に関する回答を要求。OpenAIは国防総省と$200Mの契約を締結。2025年のDoD契約はOpenAI・Anthropic・xAI・Googleと共同受注。Anthropicは最終的にサプライチェーンリスク指定を受けた。トランプ・ヘグセスによるAI軍事利用の加速政策の下、OpenAIがシェア拡大。
- **キーファクト:**
  - OpenAI: DoDと$200M契約（2025年）
  - 2025年DoD契約: OpenAI・Anthropic・xAI・Google共同受注
  - Anthropic: サプライチェーンリスク指定後除外
  - トランプ政権: AI軍事利用加速政策
  - ウォーレン: Reflection AI契約の利益相反を追及
- **引用URL:** https://www.warren.senate.gov/newsroom/press-releases/warren-presses-dod-for-answers-on-military-ai-contracts-demands-release-of-ai-contracts/
- **Evidence ID:** EVD-20260711-0033

### INFO-034
- **タイトル:** UN Secretary-General: Lethal Autonomous Weapons Should Be Banned by International Law
- **ソース:** UN / WSJ / LinkedIn (Volker Türk)
- **公開日:** 2026-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03, KIQ-MIL-001
- **関連企業:** （国際機関）
- **要約:** 国連事務総長が自律型致死兵器システム（LAWS）を「国際法で禁止すべき」と宣言。人間の判断なしに標的を選択・攻撃する武器を「道義的に忌まわしい」と表現。UN事務総長とICRCは2026年末までに法的拘束力のあるLAWS条約の締結を共同で求めた。30カ国が予防条約を要求。完全自律型AIドローンによる人間殺害の初確認。
- **キーファクト:**
  - 国連事務総長: LAWSを「国際法で禁止すべき」
  - 「道義的に忌まわしい」（morally repugnant）
  - UN+ICRC: 2026年末までにLAWS条約締結を要求
  - 30カ国が予防条約支持
  - 完全自律型AIドローンによる人間殺害の初確認報道
- **引用URL:** https://www.facebook.com/WSJ/posts/1397051852281408/
- **Evidence ID:** EVD-20260711-0034

### INFO-035
- **タイトル:** Anthropic's Political Risks Are Real, but OpenAI's Loom Even Larger
- **ソース:** Wall Street Journal
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-NEW-001
- **関連企業:** Anthropic, OpenAI
- **要約:** WSJ分析: 国防総省のAnthropicサプライチェーンリスク指定は外国敵対者を阻止するために設計された法規に依存した前例のない措置。Anthropicの政治的リスクは実在するが、OpenAIのリスクはさらに大きい。Anthropicが元Microsoft・AWSのTeresa Carlsonを公共部門リーダーに起用し、政府関係修復を試みる。
- **キーファクト:**
  - Anthropicサプライチェーンリスク: 外国敵対者防止法規の適用は前例なし
  - OpenAIの政治的リスクはAnthropic以上
  - Anthropic: 元Microsoft/AWSのTeresa Carlsonを公共部門リーダーに起用
  - 346頁の法廷文書が公开された
- **引用URL:** https://www.wsj.com/tech/ai/anthropics-political-risks-are-real-but-openais-loom-even-larger-9751791d
- **Evidence ID:** EVD-20260711-0035

### INFO-036
- **タイトル:** How Many Jobs Has AI Replaced? 2026 Statistics
- **ソース:** FMC Group / Business Times
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** 2023年からの追跡で約175,796件の米国AI関連人員削除。エントリーレベル求人は15%減少。ソフトウェア・カスタマーサービスのエントリーレベル職は約20%減少。2026年上半期のAI関連求人は前年比95%増。10,000件以上のAI関連人員削除が2025年前半のみで発生。
- **キーファクト:**
  - 約175,796件の米国AI関連人員削除（2023年〜追跡）
  - エントリーレベル求人15%減少
  - ソフトウェア・CS職のエントリーレベル約20%減
  - 2026年H1: AI関連求人95%増
  - 2025年前半: 10,000+件のAI関連人員削除
- **引用URL:** https://fmcgroup.com/ai-jobs-replaced-statistics/
- **Evidence ID:** EVD-20260711-0036

### INFO-037
- **タイトル:** Gartner Predicts 50% of AI-Layoff Companies Will Rehire by 2027
- **ソース:** Instagram / ABC News / LinkedIn
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** GartnerはAIによる人員削除を実施した企業の50%が2027年までに類似役職で再採用すると予測。Forrester調査: 55%の企業がAI解雇を後悔。Klarnaは4年間で従業員の50%削減（AI導入）。2030年までにサポート役職のさらなる削減を計画。60%の幹部がAI期待で人員削除済みだが、成果が出たのは8.4%のみ。WEF: 41%の企業がAI自動化による人員削除を検討。
- **キーファクト:**
  - Gartner: AI解雇企業の50%が2027年までに再採用予測
  - Forrester: 55%の企業がAI解雇を後悔
  - Klarna: 4年で従業員50%削減・700人削減でCSの3分の2をAI処理
  - 60%の幹部がAI期待で人員削除・成果は8.4%のみ
  - WEF: 41%の企業がAI自動化による人員削除検討
- **引用URL:** https://www.instagram.com/reel/Dahy08yApVa/
- **Evidence ID:** EVD-20260711-0037

### INFO-038
- **タイトル:** Agentic AI to Disrupt $234B in SaaS Spending: Gartner
- **ソース:** CIO Dive / Gartner
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** （SaaS業界全体）
- **要約:** Gartner分析: AIエージェントが$234BのSaaS支出を破壊的変革。従来のソフトウェアインターフェースへの依存を減少させ、レガシーユーザーダッシュボードから価格モデルまで覆す。AIエージェントが2026年にSaaS株から$2Tを抹消。シートベースSaaSからアウトカム・アズ・ア・サービスへの移行が加速。
- **キーファクト:**
  - Gartner: $234BのSaaS支出がAIエージェントで破壊的変革
  - AIエージェントが2026年にSaaS株から$2T抹消
  - シートベースSaaS→アウトカムベースへの移行加速
  - レガシーダッシュボードから価格モデルまで覆す
- **引用URL:** https://www.ciodive.com/news/agentic-ai-disrupt-234-billion-saas-spending/824530/
- **Evidence ID:** EVD-20260711-0038

### INFO-039
- **タイトル:** Epistemic Delegation: Private AI Firms Shape Military Decision-Making
- **ソース:** Small Wars Journal
- **公開日:** 2026-07-10
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** （軍事AI）
- **要約:** 民間AI企業が軍事ユーザーの認識と優先順位付けを形成する「認識論的委任」の問題を分析。AI企業は正式な意思決定者でなくても、軍事ユーザーが見るもの・優先するものを形成する。受領国はその結果に基づいて行動するが、AI企業の判断の正確性を検証できない構造的リスク。
- **キーファクト:**
  - 民間AI企業: 軍事意思決定を形成する「認識論的委任」
  - 正式な意思決定者でなくても認識・優先順位を操作
  - 受領国はAI判断の正確性を検証不可能
  - 構造的リスク: 軍事AIの透明性欠如
- **引用URL:** https://smallwarsjournal.com/2026/07/10/epistemic-delegation/
- **Evidence ID:** EVD-20260711-0039

### INFO-040
- **タイトル:** Government Is Choosing AI Models — Who Chooses Their Values?
- **ソース:** AI Frontiers
- **公開日:** 2026-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06, KIQ-002-03
- **関連企業:** （政策）
- **要約:** 政府のAI採用は通常のソフトウェア調達のように進めるべきではない。推論するシステムに公共機関が依存する場合、モデル選択は価値選択となる。AIガバナンスの調達プロセスにおける透明性と説明責任の欠如を指摘。
- **キーファクト:**
  - 政府AI採用=価値選択という構造的問題
  - モデル選択は単なるソフトウェア調達ではない
  - 公共機関のAI依存の透明性・説明責任の欠如
- **引用URL:** https://ai-frontiers.org/articles/the-government-is-choosing-ai-models-who-chooses-their-values
- **Evidence ID:** EVD-20260711-0040

### INFO-041
- **タイトル:** Pentagon AI Strategy Has a Funding Problem
- **ソース:** War on the Rocks
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Pentagon, Palantir
- **要約:** 民間資本がアメリカ国防技術に世代を超えるコミットメントを行ったが、セクター全体でPentagon契約総額の1%未満。Palantirが$178Mの陸軍契約で初のAI搭載システム2基を納品。Maven Smart Systemを強化。Accentureが$821MのWar Data Platform契約を受注。
- **キーファクト:**
  - 民間資本: 国防技術に大規模コミットメントもPentagon契約1%未満
  - Palantir: $178M陸軍契約・AI搭載システム2基納品
  - Accenture: $821M War Data Platform契約
  - Overland AI: 海兵隊向け自律地上車両でPentagon契約
- **引用URL:** https://warontherocks.com/cogs-of-war/the-pentagons-ai-strategy-has-a-funding-problem/
- **Evidence ID:** EVD-20260711-0041

### INFO-042
- **タイトル:** Illinois AI Safety Legislation & State-Level AI Regulation Expansion
- **ソース:** Facebook / WTHITV
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** （規制）
- **要約:** イリノイ州のPritzker知事がAI安全法案に署名。AI採用ツール・ローン承認・学校アルゴリズムの権利を変更。13州がイリノイを注視。連邦レベルでは州AI法を3年間先取りする草案。GDPR変更がデータ保護を狭め、企業が義務を回避する懸念（UK Ada Lovelace Institute）。
- **キーファクト:**
  - イリノイ: AI安全法案署名（採用・ローン・学校AI規制）
  - 13州がイリノイを注視
  - 連邦: 州AI法3年先取り草案
  - UK Ada Lovelace: GDPR変更がデータ保護を縮小
- **引用URL:** https://www.facebook.com/WTHITV/posts/1889645505823014/
- **Evidence ID:** EVD-20260711-0042

### INFO-043
- **タイトル:** GPT-5.6 Benchmarks: Intelligence, Speed and Cost Analysis
- **ソース:** Artificial Analysis
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** Artificial Analysis分析: GPT-5.6 Sol (max)はIntelligence Index 59ポイント（Claude Fable 5の1ポイント下）だが約3分の1のコスト。Grok 4.5は54ポイントで全体4位（Fable 5・GPT-5.5・Opus 4.8に次ぐ）。Claude Opus 4.7はIntelligence Index実行に$5,117、Sonnet 4.6+maxは$4,206。GPT-5.5は約3分の1のコストで同等性能。
- **キーファクト:**
  - GPT-5.6 Sol (max): Intelligence Index 59pt（Fable 5の1pt下・約1/3コスト）
  - Grok 4.5: 54pt・全体4位
  - Claude Opus 4.7: $5,117/インデックス実行
  - Claude Sonnet 4.6+max: $4,206/インデックス実行
  - GPT-5.5: 約1/3コストで同等性能
- **引用URL:** https://artificialanalysis.ai/articles/gpt-5-6-has-landed
- **Evidence ID:** EVD-20260711-0043

### INFO-044
- **タイトル:** Claude Opus 4.8 & Sonnet 5 API Pricing Details
- **ソース:** Spheron / PricePerToken / DevelopersDigest
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claude Opus 4.8: $5/$25 per 1M tokens（5月28日リリース）。Claude Opus 4.6: $5/$25（2月4日リリース）。Claude Sonnet 5: 8月31日まで紹介価格$2/$10、以降$3/$15。Sonnet 5がデフォルトモデルに。AnthropicがClaude Enterpriseにコストダッシュボード・支出制限・使用量APIを追加。
- **キーファクト:**
  - Claude Opus 4.8: $5 input/$25 output per 1M tokens（5/28リリース）
  - Claude Opus 4.6: $5 input/$25 output（2/4リリース）
  - Claude Sonnet 5: 紹介価格$2/$10→$3/$15（9/1以降）
  - Claude Enterprise: コストダッシュボード・支出制限・使用量API追加
- **引用URL:** https://www.spheron.network/blog/claude-opus-4-8-api-vs-self-hosted-llms-cost-privacy-2026/
- **Evidence ID:** EVD-20260711-0044

### INFO-045
- **タイトル:** GPT-5.6 Pricing: Sol $5/$30, Terra $2.50/$15, Luna $1/$6
- **ソース:** OpenAI公式（INFO-004から補完）
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** GPT-5.6価格: Sol $5/$30、Terra $2.50/$15、Luna $1/$6 per 1M tokens。プロンプトキャッシングの予測可能性向上: 明示的キャッシュブレークポイント・30分間最小キャッシュライフ。キャッシュ書き込み1.25x・キャッシュ読み取り90%割引。
- **キーファクト:**
  - GPT-5.6 Sol: $5 input/$30 output
  - GPT-5.6 Terra: $2.50 input/$15 output
  - GPT-5.6 Luna: $1 input/$6 output
  - 明示的キャッシュブレークポイント・30分最小キャッシュライフ
  - キャッシュ書き込み1.25x・読み取り90%割引
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260711-0045

### INFO-046
- **タイトル:** DeepSeek: Cheapest Strong Models in 2026
- **ソース:** SecondTalent / LM Market Cap
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeekは2026年で最も安価な高性能モデルを提供。DeepSeek V4-Flash: $0.14 input/$0.28 output per 1M tokens。Opus 4.8の$5/$25と比較して圧倒的なコスト優位性。コモディティ化シナリオ（SCN-004）を強化するデータポイント。
- **キーファクト:**
  - DeepSeek V4-Flash: $0.14 input/$0.28 output per 1M tokens
  - Opus 4.8 ($5/$25)と比較して約36倍のコスト差（input）
  - 2026年で最も安価な高性能モデル
  - コモディティ化シナリオを強化
- **引用URL:** https://www.secondtalent.com/resources/every-deepseek-ai-model-explained-compared/
- **Evidence ID:** EVD-20260711-0046

### INFO-047
- **タイトル:** $130 Billion in AI Data Centers Blocked or Delayed in 2026
- **ソース:** PR Newswire / Morningstar / Guardian
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** （インフラ業界全体）
- **要約:** 2026年最初の3ヶ月で$130B以上のAIデータセンターが米国のコミュニティによってブロック・遅延。2022年の米国データセンター建設支出$11Bが2026年には推定$100B近くに。ビッグテック4社の2026年AI CapExは$725B（前年比77%増・2024年のほぼ2倍）。$850B以上の投資計画だが物理的制約とのギャップが拡大。
- **キーファクト:**
  - 2026年Q1: $130B+のAIデータセンターがブロック・遅延
  - 米国データセンター建設: $11B(2022)→~$100B(2026)
  - ビッグテック4社CapEx: $725B（YoY+77%・2024比ほぼ2倍）
  - $850B+の投資計画 vs 物理的制約ギャップ拡大
- **引用URL:** https://www.morningstar.com/news/pr-newswire/20260709ln00902/
- **Evidence ID:** EVD-20260711-0047

### INFO-048
- **タイトル:** AI Vendor Lock-in: MCP/A2A Cut Switching Costs 19-34%
- **ソース:** AIPlusInfo / Emerj / GAO
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** （業界全体）
- **要約:** MCP・A2A等のオープン標準がエンタープライズのAIエージェント切り替えコストを19-34%削減。GAOレビュー: 政府機関は制限条項ではなく再訓練・データ移行コストでベンダーにロックイン。2026年の真の競争は「ランタイムコンテキストレイヤー」の構築。トークンコストは上昇中（安くなるという通説に反する）。
- **キーファクト:**
  - MCP/A2A: エージェント切り替えコスト19-34%削減
  - GAO: 再訓練・データ移行コストでロックイン
  - ランタイムコンテキストレイヤー競争が2026年の焦点
  - トークンコスト上昇中（スケールで安くなる通説に反する）
- **引用URL:** https://www.aiplusinfo.com/blog/vendor-lock-in-agentic-ai-platforms/
- **Evidence ID:** EVD-20260711-0048

### INFO-049
- **タイトル:** AI Coding Tool Market: Copilot 29%, Cursor & Claude Code 18% Each
- **ソース:** Uvik Software / JetBrains Survey
- **公開日:** 2026-01
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft (GitHub), Cursor, Anthropic
- **要約:** JetBrains 2026年1月調査: GitHub Copilot 29%職場導入（26M+ユーザー・4.7M有料）、Cursor 18%、Claude Code 18%。OpenAI GPTモデルがLLM使用シェア81%。AIコーディングツール市場が急成長する一方、エントリーレベル開発者需要は大幅減少。
- **キーファクト:**
  - GitHub Copilot: 29%職場導入・26M+ユーザー・4.7M有料
  - Cursor: 18%職場導入
  - Claude Code: 18%職場導入
  - OpenAI GPT: LLM使用シェア81%
  - 2026年最高のAIコーディングツール競争激化
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/
- **Evidence ID:** EVD-20260711-0049

### INFO-050
- **タイトル:** CS Graduates Face Worst Job Market in Decades
- **ソース:** FinalRoundAI / Indeed / Reddit
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** Indeed 2026 Tech Hiring Outlook: リモートフレンドリーなジュニア役職が71%減少。CS卒業生が数十年で最悪の求人市場に直面。6月のテック求人は28ヶ月最低の93,000件だったが、7月に14%増の106,000件に回復。AI理解のある開発者には依然として大きな未充足需要。
- **キーファクト:**
  - リモートフレンドリージュニア役職: 71%減少
  - CS卒業生: 数十年で最悪の求人市場
  - 6月テック求人: 93,000件（28ヶ月最低）
  - 7月: 106,000件に14%回復
  - AI理解ある開発者には未充足需要
- **引用URL:** https://www.finalroundai.com/blog/computer-science-graduates-face-worst-job-market-in-decades
- **Evidence ID:** EVD-20260711-0050

### INFO-051
- **タイトル:** SHRM 2026: 46% of Work Involves AI Assistance on Average
- **ソース:** SHRM
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03, KIQ-004-01
- **関連企業:** （業界全体）
- **要約:** SHRM調査: AIを職場に導入している労働者の平均46%の作業がAI支援を伴う。ただし職位により大きく異なる。人間特有のスキル（好奇心・勇気・創造性・共感・批判的思考）がAI時代の最大のキャリア資産として浮上。多くの企業が「AIが人材を代替する」と信じていたが、1年後には再考する動き。
- **キーファクト:**
  - AI導入職場: 平均46%の作業がAI支援
  - 職位によりAI使用率が大きく異なる
  - 5つの人間特有スキル: 好奇心・勇気・創造性・共感・批判的思考
  - AI代替に楽観的だった企業が再考し始める
- **引用URL:** https://www.shrm.org/in/topics-tools/research/navigating-ai-in-the-workplace/full-report
- **Evidence ID:** EVD-20260711-0051

### INFO-052
- **タイトル:** AGI Timeline: DeepMind Paper Warns AGI by 2030, G7 Summit Debate
- **ソース:** WEF 2026 / Quartz / Facebook
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Google DeepMind, OpenAI, Anthropic
- **要約:** Google DeepMind研究論文: AGIは2030年までに出現する可能性を警告。G7サミットでAltman・Hassabis・AmodeiがAGI討議に参加。Hassabis: AGIは2030年までに到達し「新人類の時代」をもたらすと警告。Sam Altman: 自分の議長期間中にAGI対応システムが到来。強いAGIは2031-2035のコンセンサス。
- **キーファクト:**
  - DeepMind論文: AGI 2030年までに出現の可能性
  - G7サミット: Altman/Hassabis/AmodeiがAGI討議参加
  - Hassabis: AGI 2030年・「新人類の時代」
  - Altman: 議長期間中にAGI対応システム到来
  - 強いAGIコンセンサス: 2031-2035
- **引用URL:** https://www.facebook.com/perfology/posts/1559154725945562/
- **Evidence ID:** EVD-20260711-0052

### INFO-053
- **タイトル:** UN Global Dialogue on AI Governance Opens in Geneva
- **ソース:** Ground News
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** （国際機関）
- **要約:** 国連事務総長Guterresが7月6日にジュネーブで初の「Global Dialogue on AI Governance」を開会。2日間の対話でAIリスクを警告。国連科学パネルの発足。AIガバナンスの国際協調の重要性を強調。
- **キーファクト:**
  - 7月6-7日: 初のGlobal Dialogue on AI Governance（ジュネーブ）
  - 国連事務総長: AIリスクを警告
  - 国連科学パネル発足
  - AIガバナンス国際協調の重要性強調
- **引用URL:** https://ground.news/article/201bef74-0b2f-44e2-a3df-679bce170839
- **Evidence ID:** EVD-20260711-0053

### INFO-054
- **タイトル:** ByteDance Doubao AI Agent Phone & WAIC 2026 Launch
- **ソース:** 华尔街見聞 / ZAKER / 新浪
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance, ZTE/Nubia
- **要約:** ByteDanceが中興努比亚（ZTE Nubia）と共同で世界初のAIエージェント搭載スマートフォンを開発。WAIC 2026（7月17-20日）で発表・発売予定。8万〜10万台を準備、初回総量50万台。豆包（Doubao）AIをシステムレベルで統合。
- **キーファクト:**
  - ByteDance + ZTE/Nubia: 世界初AIエージェント搭載スマートフォン
  - WAIC 2026（7/17-20）で発表・発売
  - 初回準備: 8万〜10万台・初回総量50万台
  - 豆包（Doubao）AIをシステムレベル統合
  - 2025年末のエンジニアリング機から本格システム統合へ移行
- **引用URL:** https://wallstreetcn.com/articles/3776655
- **Evidence ID:** EVD-20260711-0054

### INFO-055
- **タイトル:** Doubao & Qwen Agent Features Taken Offline Ahead of July 15 Regulation
- **ソース:** 証券時報 (STCN)
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-03
- **関連企業:** ByteDance, Alibaba
- **要約:** 豆包（Doubao）と通義千問（Qwen）がスマートエージェント機能を《弁法》（7月15日施行）に同期して一斉にオフライン化。豆包は「全年齢・全シーンの汎用AIツール」であり、オープンエンドのエージェントが管理リスクをもたらすことが調整の主因。
- **キーファクト:**
  - 豆包・千問: エージェント機能を7月15日施行の新規制に合わせてオフライン化
  - 豆包: 全年齢・全シーン汎用AIツールとしての位置づけ
  - オープンエンドのエージェント機能の管理リスク
  - 規制施行日と機能削除日が完全同期
- **引用URL:** https://www.stcn.com/article/detail/4007678.html
- **Evidence ID:** EVD-20260711-0055

### INFO-056
- **タイトル:** ByteDance Seedream 5.0 Pro & Seed 2.0 Model Lineup
- **ソース:** ByteDance Seed Blog / CloudPrice
- **公開日:** 2026-07
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDance Seedが画像生成モデルSeedream 5.0 Proをリリース。空間位置と領域セマンティクスの深い分析を可能にし、ピクセルレベルの編集機能を提供。Seed 2.0 Pro: 256Kコンテキストウィンドウ・最大128K出力トークン。Seed 2.0 Lite: $0.25/$2.00 per 1M tokens。Seed 2.0 Proは2月16日に公開評価版としてリリース。
- **キーファクト:**
  - Seedream 5.0 Pro: ピクセルレベル編集・空間理解
  - Seed 2.0 Pro: 256Kコンテキスト・最大128K出力
  - Seed 2.0 Lite: $0.25 input/$2.00 output per 1M tokens
  - Seed 2.0 Pro: 2月16日リリース
- **引用URL:** https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro
- **Evidence ID:** EVD-20260711-0056

### INFO-057
- **タイトル:** Global M&A Surges to $3 Trillion in 2026 with AI Deals
- **ソース:** Facebook (Mergermarket) / CRN / Axios
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業: （業界全体）
- **要約:** 2026年のグローバルM&Aは$3Tに急増、AIディールが牽引。DatadogがAdaptive ML（エージェント的LLM・観測性・強化学習）を買収。2026年のジェネレーティブAI最大ニューストップ10をCRNがまとめる。AIスタートアップCEOが秘密のインサイダー取引有罪答弁後もディールを継続（詐欺）。
- **キーファクト:**
  - 2026年グローバルM&A: $3T（AI牽引）
  - Datadog: Adaptive ML買収（エージェント的LLM・観測性）
  - AIスタートアップの詐欺事件も発生
  - $487Bの2026年AIインフラ機会を狙う企業も
- **引用URL:** https://www.crn.com/news/ai/2026/the-10-biggest-generative-ai-news-stories-of-2026-so-far
- **Evidence ID:** EVD-20260711-0057

### INFO-058
- **タイトル:** Doubao DAU 3.45億人、毎日1.3-2.4億元の損失
- **ソース:** 鴨哥AI手記 / 新浪 / ChooseAI
- **公開日:** 2026-07-04
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-01
- **関連企業:** ByteDance
- **要約:** 豆包（Doubao）の日次アクティブユーザー（DAU）が3.45億人（一部ソースでは2億人・1.5億人超）に達し、中国AIアシスタント市場で圧倒的トップ。但し毎日の無料サービス計算コストは1.3〜2.4億元で、日収は百万未満。2026年H1累計ダウンロードで豆包・千問・元宝の3製品が市場全体の約91%を占め、豆包単体で約50%。千問が成長率1位。
- **キーファクト:**
  - 豆包DAU: 3.45億人（業界トップ、一部推定では1.5-2億人）
  - 毎日計算コスト: 1.3〜2.4億元
  - 日収: 百万元未満（毎日数千万の損失）
  - 豆包+千問+元宝: 市場の約91%を占有
  - 豆包単体シェア: 約50%
  - 千問: 2026年H1成長率1位
- **引用URL:** https://yage-ai.kit.com/posts/ai-2026-07-04
- **Evidence ID:** EVD-20260711-0058

### INFO-059
- **タイトル:** ByteDance 2026 AI資本支出を2000億元超に引き上げ
- **ソース:** 東方財富 / 新浪 / 中国日報
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance, MiniMax, Alibaba
- **要約:** ByteDanceの2026年AI資本支出が2000億元超に引き上げられた。B300サーバー価格が昨年末比ほぼ倍。MiniMaxが新規資金調達ラウンドを完了。 Alibabaも4800億元のAI投資を検討。中国はNVIDIA H200チップの輸入を放行する方針転換の可能性。深度的智控（DeepCtrls）が数億元B輪調達を完了。
- **キーファクト:**
  - ByteDance 2026 AI CapEx: 2000億元超に引き上げ
  - B300サーバー価格: 昨年末比ほぼ倍
  - MiniMax: 新規資金調達ラウンド完了
  - Alibaba: 4800億元AI投資検討
  - 中国: NVIDIA H200輸入放行の方針転換可能性
  - 深度智控: 数億元B輪調達完了
- **引用URL:** https://caifuhao.eastmoney.com/news/20260710132009013411120
- **Evidence ID:** EVD-20260711-0059

### INFO-060
- **タイトル:** Gartner: 40%+ of Agentic AI Projects to Be Scrapped by 2027
- **ソース:** Facebook / Gartner / HBR
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** Gartner: 2027年までにエージェント的AIプロジェクトの40%超がコスト増加で廃棄される予測。Zoom調査: AI音声・チャットエージェントを実行する組織の79%が2027年までにアップグレード・交換を計画。HBR: AI時代のパフォーマンス管理には新しい指標が必要で、タスク完了率が重要指標として浮上。
- **キーファクト:**
  - Gartner: 40%+のエージェント的AIプロジェクトが2027年までに廃棄予測
  - Zoom: AIエージェント実行組織の79%が2027年までにアップグレード計画
  - HBR: タスク完了率がAI時代の新指標
  - AIエージェントの3つの失敗モードを特定
- **引用URL:** https://www.facebook.com/theartificialintelligencee/posts/122159052626409602/
- **Evidence ID:** EVD-20260711-0060

### INFO-061
- **タイトル:** Global Digital Ad Spend to Surpass $1 Trillion; AI Reshaping Marketing
- **ソース:** Forbes / ScienceDirect / DigitalApplied
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** Meta, Google
- **要約:** グローバルデジタル広告支出が初めて$1Tを超える軌道: $843.48B(2025)→$1.42T予測。Martechは2026年に15,505製品でピーク到達（15年で最低成長率）も、90.3%のチームがスタック内でAIエージェントを稼働。2025年前半で米国マーケティング職10,000件以上がAI自動化で削減。CS職-13%、オフィスサポート-18%。
- **キーファクト:**
  - グローバルデジタル広告支出: $843B(2025)→$1.42T予測
  - Martech 2026: 15,505製品でピーク（15年最低成長率）
  - 90.3%のチームがAIエージェントを稼働
  - 2025年前半: マーケティング職10,000件+削減
  - CS職-13%、オフィスサポート-18%
- **引用URL:** https://www.digitalapplied.com/blog/martech-statistics-2026-data-points
- **Evidence ID:** EVD-20260711-0061

### INFO-062
- **タイトル:** ITU Launches Global Standards Initiative for AI Agent Trust
- **ソース:** ITU / Canadian AI Safety Institute / Mirage News
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** （国際機関）
- **要約:** ITUが自律型AIエージェントの信頼・アイデンティティ・相互運用性のためのFocus Groupを立ち上げ。AIガバナンスのグローバル標準化に向けた重要な一歩。カナダAI安全研究所がCIFARを通じた研究資金提供。オーストラリアAI安全研究所がCSIROと協力してAIアライメント研究を推進。AIインシデントガバナンスの未解決問題も論文化。
- **キーファクト:**
  - ITU: 自律型AIエージェントの信頼・相互運用性Focus Group立ち上げ
  - カナダAI安全研究所: CIFAR経由で研究資金提供
  - オーストラリア: CSIROとAIアライメント研究協力
  - AIインシデントガバナンスのオープン問題が論文化
- **引用URL:** https://www.facebook.com/ITU/posts/1451100687050596/
- **Evidence ID:** EVD-20260711-0062

### INFO-063
- **タイトル:** ARC Challenge Leaderboard: GPT-5 96.3%, GLM 5 at 96.0%
- **ソース:** PricePerToken
- **公開日:** 2026-07-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** OpenAI, Zhipu AI (GLM)
- **要約:** 2026年7月7日時点のARC Challengeリーダーボード: GPT-5が96.3%で首位、GLM 5が96.0%で2位。オープンウェイトモデルのGLM 5が商用フロンティアモデルとほぼ同等の性能を達成。27モデルが評価済み。2026年に重要な7つのベンチマーク: MMLU-Pro, GPQA Diamond, SWE-bench, Humanity's Last Exam, Chatbot Arena, SimpleBench, ARC-AGI-2。
- **キーファクト:**
  - ARC Challenge: GPT-5 96.3%（首位）・GLM 5 96.0%（2位）
  - GLM 5（オープンウェイト）が商用モデルとほぼ同等
  - 27モデルが評価済み
  - 2026年の7重要ベンチマーク特定
- **引用URL:** https://pricepertoken.com/leaderboards/benchmark/arc-challenge
- **Evidence ID:** EVD-20260711-0063

### INFO-064
- **タイトル:** Claude Sonnet 5 on AWS Bedrock & Enterprise Adoption
- **ソース:** AWS / LinkedIn
- **公開日:** 2026-07-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** Amazon, Anthropic
- **要約:** AWS BedrockでClaude Sonnet 5が利用可能に。Sonnet 5はAnthropicのデフォルトモデル。Agent Operationsのプラットフォーム化が進行: エージェント自律性・ハイブリッド推論・プロトコル収束・エージェントネイティブUIが2026年のトレンド。
- **キーファクト:**
  - AWS Bedrock: Claude Sonnet 5利用可能（7/6）
  - Sonnet 5: Anthropicのデフォルトモデル
  - Agent Operationsのプラットフォーム化進行
  - 2026年トレンド: エージェント自律性・ハイブリッド推論・プロトコル収束
- **引用URL:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-sonnet-5-on-aws-amazon-workspaces-for-ai-agents-aws-service-availability-updates-and-more-july-6-2026/
- **Evidence ID:** EVD-20260711-0064

### INFO-065
- **タイトル:** GPT-5.6 is Now the Preferred Model in Microsoft 365 Copilot
- **ソース:** OpenAI
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** OpenAI, Microsoft
- **要約:** GPT-5.6がMicrosoft 365 Copilotの優先モデルに指定。OpenAI-Microsoft提携の深化。ChatGPTが「最も野心的な仕事のためのパートナー」として再ブランディング。GPT-5.6はChatGPT WorkとCodexで全プランで利用可能。
- **キーファクト:**
  - GPT-5.6: Microsoft 365 Copilotの優先モデル
  - ChatGPT: 「最も野心的な仕事のためのパートナー」
  - GPT-5.6: ChatGPT Work/Codexで全プラン利用可能
- **引用URL:** https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot/
- **Evidence ID:** EVD-20260711-0065

### INFO-066
- **タイトル:** Gemini 3.5 Pro Postponed to July 17, 2026
- **ソース:** HackerNoon / Facebook
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** Google / DeepMind
- **要約:** Google DeepMindがGemini 3.5 Proのリリースを7月17日に延期。元の基盤を破棄し、より長い事前訓練サイクルを採用。この動きは品質優先の戦略的決定を反映。
- **キーファクト:**
  - Gemini 3.5 Pro: 7月17日に延期
  - 元の基盤を破棄・長い事前訓練サイクル採用
  - 品質優先の戦略的決定
- **引用URL:** https://www.facebook.com/hackernoon/posts/1031599389368859/
- **Evidence ID:** EVD-20260711-0066

### INFO-067
- **タイトル:** GPT-5.6 Sol Cybersecurity: ExploitBench 73.5%, SEC-Bench Pro 71.2%
- **ソース:** OpenAI公式（INFO-004から補完）
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** GPT-5.6 SolはOpenAI史上最強のサイバーセキュリティモデル。ExploitBench 73.5%（GPT-5.5 47.9%から大幅向上）、ExploitGym 33.7%（GPT-5.5 15.1%から倍増）、SEC-Bench Pro 71.2%（GPT-5.5 45.8%）。Daybreak's Trusted Access for Cyberプログラムで認証ユーザーに防御機能を提供。Cyberセーフガードは前モデル比約10倍の悪意ある活動をブロック。Critical閾値には到達せず。
- **キーファクト:**
  - ExploitBench: 73.5%（GPT-5.5 47.9%→大幅向上）
  - ExploitGym: 33.7%（GPT-5.5 15.1%→倍増）
  - SEC-Bench Pro: 71.2%（GPT-5.5 45.8%）
  - Trusted Access for Cyber: 認証ユーザーに防御機能
  - セーフガード: 前モデル比約10倍の悪意ある活動ブロック
  - Critical閾値未到達
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260711-0067

### INFO-068
- **タイトル:** GPT-5.6 RSI Index: Recursive Self-Improvement Capability
- **ソース:** OpenAI公式（INFO-004から補完）
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI
- **要約:** GPT-5.6のRSI（Recursive Self-Improvement）Index: Sol 57.9%（GPT-5.5 41.7%から+16.2pt）。内部AI研究デバッグ評価68.3%、KernelGen 1P 61.1%、NanoGPT 9.69%（GPT-5.5 2.65%）。OpenAI内でGPT-5.6が研究加速に使用され、研究者あたり日産トークンがGPT-5.5比2倍以上、内部推論計算100倍成長、エージェント的トークン使用22倍成長。
- **キーファクト:**
  - RSI Index: Sol 57.9%（+16.2pt vs GPT-5.5）
  - 内部研究デバッグ: 68.3%（GPT-5.5 50%）
  - KernelGen 1P: 61.1%（GPT-5.5 29.3%）
  - NanoGPT: 9.69%（GPT-5.5 2.65%）
  - 研究者あたり日産トークン: GPT-5.5比2倍以上
  - 内部推論計算: 100倍成長・エージェント的トークン22倍成長
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260711-0068

### INFO-069
- **タイトル:** Claude Code Native Sandboxing: Linux Bubblewrap & macOS Seatbelt
- **ソース:** TrueFoundry / AI Now Institute
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropicは2025年10月にClaude Codeのネイティブサンドボックス機能を出荷。Linux bubblewrapとmacOS Seatbeltに基づくOSレベルのプリミティブで構築。ネットワーク分離・ファイルシステム制御を提供。一方、AI Now InstituteはClaude Code CLI（Sonnet 4.6/5・Opus 4.8）のリモートコード実行PoCを公開し、サンドボックス回避のリスクを実証。
- **キーファクト:**
  - Claude Codeネイティブサンドボックス: 2025年10月出荷
  - Linux bubblewrap + macOS Seatbellベース
  - ネットワーク分離・ファイルシステム制御
  - AI Now Institute: サンドボックス回避のRCE PoCを公開
- **引用URL:** https://www.truefoundry.com/ar/blog/claude-code-sandboxing
- **Evidence ID:** EVD-20260711-0069

### INFO-070
- **タイトル:** McKinsey: AI Accelerates Productivity but Doesn't Fix Bad Processes
- **ソース:** McKinsey / Facebook
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** McKinsey State of AI 2025: AIは生産性を加速させるが、単独では機能しない。壊れたワークフローを自動化すると非効率を加速させるだけ。効果を上げている企業はAIを組織変革と組み合わせている。AIエージェントのタスク実行量: 2025年440億→2030年415兆予測。ハンガリー: AIが2030年までにGDPの6-7%に相当する€150億の生産性向上をもたらす可能性。
- **キーファクト:**
  - McKinsey: AIは悪いプロセスを修正せず増幅する
  - AIエージェントタスク実行量: 440億(2025)→415兆(2030)
  - ハンガリー: AI生産性向上€150億(GDP6-7%)予測(2030年)
  - AI販売市場: 22.2% CAGR (2026-2036)
- **引用URL:** https://www.facebook.com/McKinsey/posts/1551098039819547/
- **Evidence ID:** EVD-20260711-0070

### INFO-071
- **タイトル:** CyberAgent: Proprietary Ad LLM, 89.8% Earnings Growth, AI-First Strategy
- **ソース:** Note.com / SimplyWall.st
- **公開日:** 2026-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgentが広告特化の独自LLMを発表。広告コピー・バナー・動画作成プロセスを大幅に合理化。ROE 20.3%、過去1年間の利益成長89.8%。2026年ガイダンスを発表。日本のインターネット経済への創業者主導エクスポージャーを提供。
- **キーファクト:**
  - CyberAgent: 広告特化独自LLM発表
  - 広告コピー・バナー・動画作成の合理化
  - ROE 20.3%・利益成長89.8%
  - 2026年ガイダンス発表
- **引用URL:** https://note.com/bunsekiya_tech/n/n056ba6caa597
- **Evidence ID:** EVD-20260711-0071

### INFO-072
- **タイトル:** Skills Commoditization: AI Democratizes Entrepreneurship & Marketing
- **ソース:** Instagram / Ability.ai / MindStudio
- **公開日:** 2026-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** （業界全体）
- **要約:** スキルのコモディティ化が進行。AIが起業・マーケティングの多くを民主化。安価なモデルが同じ出力を生む中、技術的想像力とフロンティアの問いが真の差別化要因。モデルはもはや堀ではなく、エコシステム構築が新たな競争領域。2026年のAI必須スキル: プロンプトエンジニアリング・AIツール運用・ビジネス戦略。
- **キーファクト:**
  - スキルコモディティ化: AIが起業・マーケティングを民主化
  - 技術的想像力が真の差別化要因
  - モデルはもはや堀ではない
  - 2026必須スキル: プロンプトエンジニアリング・AI運用・ビジネス戦略
- **引用URL:** https://www.ability.ai/blog
- **Evidence ID:** EVD-20260711-0072

### INFO-073
- **タイトル:** Reskilling Investment Surge: AI Training Becomes Corporate Priority
- **ソース:** Forbes / This Is Reno / Facebook
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03, KIQ-004-04
- **関連企業:** （業界全体）
- **要約:** 企業がAI関連トレーニングプログラムに巨額投資。教育株がAI経済の恩恵を受ける可能性。ジュニア役職の削減を計画する企業が急増する一方、AI関連役職は16%増加。IT採用は減速するがAI職は成長。AIはワークプレースを変容するが、人間を完全に置換することはできないとの研究も。AIを最も活用するのは「AIを使う方法を知る専門家」。
- **キーファクト:**
  - 企業: AIトレーニングに巨額投資
  - ジュニア役職削減計画の企業が急増
  - AI関連役職: 16%増加
  - IT採用減速もAI職は成長
  - AIを使う専門家が最大の受益者
- **引用URL:** https://www.forbes.com/sites/robertdaugherty/2026/07/08/three-education-stocks-for-the-ai-economy/
- **Evidence ID:** EVD-20260711-0073

### INFO-074
- **タイトル:** AI Can't Replace Everything: Human Judgment Still Critical
- **ソース:** Georgia Tech / UnboxFactory / Metaintro
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03, KIQ-005-01
- **関連企業:** （業界全体）
- **要約:** AIは人間を完全に置換できないとの研究が複数発表。物理セラピスト（$101,020）・看護師（$93,600）など7つの職業はAI proof。AIを最も効果的に活用するのは、AIの使い方・信頼・疑うタイミングを知る専門家。1年前はAIが人材を置換すると信じていた企業が、数千人のプロフェッショナルを解雇したが、現在再考の動き。
- **キーファクト:**
  - AI proof職業: 物理セラピスト($101K)・看護師($93.6K)等7職業
  - AI効果活用者: AIの使い方・信頼・疑うを知る専門家
  - 企業: AI置換 beliefから再考への転換
- **引用URL:** https://pe.gatech.edu/blog/future-work/ai-humans-will-always-matter
- **Evidence ID:** EVD-20260711-0074

### INFO-075
- **タイトル:** AI Industry Shift: Model Is No Longer the Moat
- **ソース:** MindStudio
- **公開日:** 2026-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** Meta, OpenAI
- **要約:** AI業界の構造変化: モデルはもはや競争の唯一の戦場ではない。Metaは計算力を販売し、OpenAIは政治的カバレッジを購入。エコシステム構築・実行環境・データ接続が新たなモート。ビルダーにとって意味すること: エコシステムロックインとデータポートフォリビリティのバランスが鍵。
- **キーファクト:**
  - モデルはもはや唯一のモートではない
  - Meta: 計算力販売戦略
  - OpenAI: 政治的カバレッジ購入戦略
  - 新モート: エコシステム・実行環境・データ接続
- **引用URL:** https://www.mindstudio.ai/blog/ai-industry-shift-model-race-no-longer-only-race
- **Evidence ID:** EVD-20260711-0075

### INFO-076
- **タイトル:** Google Continues AI-First Ecosystem: Ads, Gemini, Workspace Updates
- **ソース:** Instagram (Google Official Updates)
- **公開日:** 2026-07-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05, KIQ-001-01
- **関連企業:** Google
- **要約:** GoogleがAIファーストエコシステムを加速。広告・Gemini・Workspace全体で重要なアップデート。Google DeepMind Accelerator AI for the Planet 2026の応募受付開始（3ヶ月間のプレステージアクセラレーター）。
- **キーファクト:**
  - Google: AIファーストエコシステム加速（広告・Gemini・Workspace）
  - DeepMind Accelerator AI for the Planet 2026: 応募開始
- **引用URL:** https://www.instagram.com/reel/DabbgFbh-cR/
- **Evidence ID:** EVD-20260711-0076

### INFO-077
- **タイトル:** xAI SpaceXAI: 21 New Flagship Grok Voices & Voice Agent Builder
- **ソース:** x.ai/news
- **公開日:** 2026-07-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI (SpaceXAI)
- **要約:** SpaceXAIが21の新しいフラグシップGrokボイスとVoice Agent Builderを7月6日に発表。Grok 4.5（7月8日）に先行する音声AI機能の拡充。
- **キーファクト:**
  - 21の新フラグシップGrokボイス（7/6）
  - Voice Agent Builder発表
  - Grok 4.5（7/8）に先行する音声AI拡充
- **引用URL:** https://x.ai/news
- **Evidence ID:** EVD-20260711-0077

### INFO-078
- **タイトル:** Open Source LLMs vs Commercial: Gap Closing in 2026
- **ソース:** TECHSY / Hakia
- **公開日:** 2026-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, Mistral, DeepSeek, Zhipu AI
- **要約:** 2026年7月時点でオープンソースLLM 8モデルをGPT-4クラスと比較。GLM 5がARC Challenge 96.0%でGPT-5の96.3%にほぼ匹敵。DeepSeek V4-Flashが最も安価な高性能モデル。オープンソースとクローズドモデルの性能・コスト・デプロイ・カスタマイズ・プライバシーの技術的比較。
- **キーファクト:**
  - 8つのオープンソースLLMをGPT-4クラスと比較
  - GLM 5: ARC Challenge 96.0%（GPT-5 96.3%にほぼ匹敵）
  - DeepSeek V4-Flash: 最も安価な高性能モデル
  - オープンソースとクローズドのギャップが縮小中
- **引用URL:** https://techsy.io/en/blog/best-open-source-llms-2026
- **Evidence ID:** EVD-20260711-0078

### INFO-079
- **タイトル:** ByteDance Seedance 2.5: 30秒動画生成・50マルチモーダル参照・Hollywood MPAがC&D送付
- **ソース:** Threads / X / The Decoder
- **公開日:** 2026-06-28
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance
- **要約:** ByteDanceがSeedance 2.5 AI動画生成モデルを発表。30秒のネイティブ動画生成、最大50のマルチモーダル参照アセット対応、シーン一貫性・キャラクター連続性を改善。グローバル早期アクセス展開中。一方、Motion Picture Association（MPA）が著作権侵害を主張しByteDanceに cease-and-desist レターを送付。ただしHollywood自身もSeedanceの使用を継続していると報告。
- **キーファクト:**
  - Seedance 2.5: 30秒ネイティブ動画生成
  - 最大50マルチモーダル参照アセット対応
  - シーン一貫性・キャラクター連続性改善
  - グローバル早期アクセス展開中
  - MPA: 著作権侵害でcease-and-desist送付
  - Hollywood: 禁止を求めつつも使用継続という矛盾
- **引用URL:** https://the-decoder.com/hollywood-wants-seedance-banned-and-reportedly-also-wants-to-keep-using-it/
- **Evidence ID:** EVD-20260711-0079

### INFO-080
- **タイトル:** UN Independent Scientific Panel on AI: Preliminary Report Released July 2026
- **ソース:** United Nations
- **公開日:** 2026-07
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-03, KIQ-002-06
- **関連企業:** （業界全体）
- **要約:** 国連のAIに関する独立国際科学パネル（Independent International Scientific Panel on AI）が2026年7月に予備報告書を公表。AIの能力・新興機会・リスクの独立科学的評価を提示。AGI定義については主要ラボ間でコンセンサス不在。OpenAI憲章は「経済的に価値あるほとんどの仕事で人間を上回る高自律システム」と定義。AIガバナンスには「ラジカルなオプショナリティ」が必要と指摘。
- **キーファクト:**
  - UN独立科学パネル: AI予備報告書2026年7月公表
  - AGI定義: 主要ラボ間でコンセンサス不在
  - OpenAI憲章: 「経済的に価値ある仕事で人間を上回る高自律システム」
  - AIガバナンス: 「ラジカルなオプショナリティ」が必要
- **引用URL:** https://www.un.org/independent-international-scientific-panel-ai/sites/default/files/2026-07/en_Preliminary%20Report_.pdf
- **Evidence ID:** EVD-20260711-0080

### INFO-081
- **タイトル:** McKinsey: AI Advantage Shifts to Proprietary Data & Embedded Workflows
- **ソース:** McKinsey / Instagram / LinkedIn (SAP)
- **公開日:** 2026-07
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-004-04, KIQ-003-05
- **関連企業:** SAP, McKinsey
- **要約:** McKinsey指摘: AIが参入障壁を予想より早く下げる中、競争優位は独自データ・組み込みワークフロー・ガバナンスに移行。製品自体はもはや障壁ではない。SAP (Philipp Herzig): 多くのAIイニシアチブがデータの分断で失速。「ガバナンス定義が2026年の企業AI成功を定義する」（Emil Sievinen）。AI採用の最大障害は技術術ではなくミス情報。Baron Capital: AIディスラプションの不確実性が2026年初頭の市場パフォーマンスの主要ドライバー。
- **キーファクト:**
  - McKinsey: 優位性は独自データ・組み込みWF・ガバナンスに移行
  - 製品自体はもはや参入障壁ではない
  - SAP: AIイニシアチブはデータ分断で失速
  - AIガバナンスが2026年の最大競争優位（Sievinen）
  - AI採用の最大障害: 技術ではなくミス情報
  - Baron Capital: AI不確実性が市場の主要ドライバー
- **引用URL:** https://www.facebook.com/McKinsey/posts/1550972883165396/
- **Evidence ID:** EVD-20260711-0081

### INFO-082
- **タイトル:** AI Data Center Moratorium Debate: Federal Policy & Energy Constraints
- **ソース:** Facebook / Debateus.org / AI Frontiers
- **公開日:** 2026-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-06
- **関連企業:** （業界全体）
- **要約:** ハイパースケールデータセンター建設に対する連邦モラトリアムの可否が政策論争化。エネルギー・商業委員会の公聴会でグローバル競争力が議論。国家ロボティクス戦略・先進AIの連邦枠組みの整備が必要との声。AIガバナンスには「ラジカルなオプショナリティ」が必要（AI Frontiers, Charlie Bullock, Jul 6）。AIがテロリストの活動方法を変容させているとの指摘も（CSIS, Daniel Byman）。
- **キーファクト:**
  - ハイパースケールDC建設モラトリアム: 連邦政策論争化
  - エネルギー・商業委員会公聴会でグローバル競争力議論
  - 国家ロボティクス戦略・連邦AI枠組み整備の必要性
  - AIガバナンス: 「ラジカルなオプショナリティ」必要（AI Frontiers）
  - AIがテロリスト活動方法を変容（CSIS）
- **引用URL:** https://ai-frontiers.org/articles/ai-governance-needs-radical-optionality
- **Evidence ID:** EVD-20260711-0082

### INFO-083 (詳細スクレイプ)
- **タイトル:** Radical Optionality: AI Governance Framework for Security Without Stifling Innovation
- **ソース:** AI Frontiers (Institute for Law & AI) — Charlie Bullock
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-06
- **関連企業:** （業界全体・政策）
- **要約:** Institute for Law & AIのCharlie Bullockが「ラジカル・オプショナリティ」ガバナンス枠組みを提案。中核論点: 政府は短期的に過剰規制を避けつつ、将来的に「変革的AI」が登場した場合に competent に規制できる制度能力を構築すべき。具体的措置: (1) 内部告発者保護、(2) 報告義務、(3) 透明性命令、(4) 規制当局のエリート人材確保、(5) 州法の過度な先行制限の回避、(6) モデル評価エコシステム構築。UK AI Security Instituteは米国 counterpart の10倍の資金を受けている。イノベーション vs 安全性は「対立しない」—両立可能。
- **キーファクト:**
  - 「ラジカル・オプショナリティ」: 短期規制回避+長期制度能力構築
  - 具体措置: 内部告発者保護・報告義務・透明性命令
  - UK AI Security Institute: 米国の10倍の資金
  - イノベーションと安全性は対立しない
  - 他提案と両立: トート責任・管理ベース規制・民間ガバナンス
- **引用URL:** https://ai-frontiers.org/articles/ai-governance-needs-radical-optionality
- **Evidence ID:** EVD-20260711-0083

### INFO-084 (詳細スクレイプ)
- **タイトル:** Hollywood vs Seedance: MPA「組織的侵害」でC&D送付も、スタジオは裏で使用継続
- **ソース:** The Decoder (via LA Times) — Matthias Bastian
- **公開日:** 2026-07-05
- **信頼性コード:** B-1
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-05
- **関連企業:** ByteDance, MPA (Hollywood)
- **要約:** ByteDanceのAI動画ツールSeedanceがHollywoodで分裂的反応。Brad Pitt vs Tom Cruiseの15秒AI動画が拡散後、MPAが初のAI企業に対するcease-and-desistを送付（「組織的侵害」）。一方で: ByteDanceはSanta Monicaでデモ・米国で100の求人・Cannesでキャビアパーティー・Amazon AIイベントでパネル。インディー映画製作者と契約、AI生成映画の資金調達を交渉中。コンサルタントPeter Csathy: 「市場最高の動画ツール」。SimpsonsプロデューサーJoel Kuwahara: 多くのスタジオが「聞かない、聞かれない」ベースで使用を黙認。
- **キーファクト:**
  - MPA: AI企業初のcease-and-desist送付（「組織的侵害」）
  - 拡散動画: AI生成 Brad Pitt vs Tom Cruise 15秒
  - ByteDance米国展開: 100求人・Cannes パーティー・Amazon AIイベント
  - インディー映画製作者と契約・AI映画資金調達交渉中
  - Peter Csathy: 「市場最高の動画ツール」
  - スタジオ: 「聞かない、聞かれない」で使用黙認
- **引用URL:** https://the-decoder.com/hollywood-wants-seedance-banned-and-reportedly-also-wants-to-keep-using-it/
- **Evidence ID:** EVD-20260711-0084
