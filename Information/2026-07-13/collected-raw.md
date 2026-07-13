# 収集データ: 2026-07-13

## メタデータ
- 収集日時: 2026-07-13 00:30 UTC
- 実行クエリ数: 117 / 111 (計画111件 + Arbiter動的6件)
- scrape実行数: 3件 (OpenAI GPT-5.6・xAI Grok 4.5・Artificial Analysis Grok 4.5)
- 収集情報数: 63件
- Evidence ID 採番範囲: EVD-20260713-0001 〜 EVD-20260713-0063
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 動的KIQカバレッジ: KIQ-MIL-001 ✓, KIQ-CAR-002-OPS ✓, KIQ-OAI-001 ✓, KIQ-NEW-001 ✓, KIQ-ANT-002 ✓, KIQ-NEW-002 ✓
- 品質フラグ: NORMAL

## 動的追加クエリ（Arbiterフィードバックに基づく）
以下は state/arbiter-latest.md の「明日の収集で優先すべきKIQ」に基づき追加生成したクエリ:
1. KIQ-MIL-001: 自律兵器システムの人間による却下比率・完全自律ドローン関連
2. KIQ-CAR-002-OPS: 設計・評価能力の市場プレミアム定量データ
3. KIQ-OAI-001: OpenAI収益内訳（政府vs民間）の詳細
4. KIQ-NEW-001: 他社のOpenAI型5%株式提案の有無
5. KIQ-ANT-002: Claude Code固有のDAU/WAU定量データ
6. KIQ-NEW-002: Decagon型OSS移行事例の追加確認

## 収集結果

---

### INFO-001
- **タイトル:** GPT-5.6 Sol/Terra/Luna 一般提供開始 — ARC-AGI-3 7.78%でSOTA、RSI指数16.2pt向上
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01, KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6ファミリー（Sol/Terra/Luna）を一般提供開始。SolはAgents' Last Exam 53.6%、Coding Agent Index 80（SOTA）、ARC-AGI-3 7.78%（初の有意義な進歩）を記録。ultraモードで4エージェント並列協調を実現。Programmatic Tool CallingでZDR対応。
- **キーファクト:**
  - Sol: Agents' Last Exam 52.7%、AA Intelligence Index 58.9（Fable 5の59.9に次ぐ2位）
  - ARC-AGI-3: Sol 7.78%（従来最大0.43%から大幅改善）、Opus 4.8は1.5%
  - RSI Index: Sol 57.9%（GPT-5.5の41.7%から+16.2pt向上）
  - 価格: Sol $5/$30、Terra $2.50/$15、Luna $1/$6 per 1M tokens
  - ExploitGym 33.7%（6時間制限）、SEC-Bench Pro 71.2%
  - 過去6ヶ月で内部コーディング推論計算量が100倍、エージェントトークン使用量22倍増
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260713-0001

### INFO-002
- **タイトル:** Grok 4.5リリース — Artificial Analysis Intelligence Index 54、コスト効率でPareto最前線
- **ソース:** Artificial Analysis / SpaceXAI
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** xAI (SpaceXAI)
- **要約:** xAI（SpaceXAI）がGrok 4.5をリリース。Intelligence Index 54（Grok 4.3から+16pt）で第4位。Grok BuildではCoding Agent Index 76でGPT-5.5と同等。コストはFable 5の1/5以下。
- **キーファクト:**
  - Intelligence Index 54（Fable 5=59.9、GPT-5.5=54.8、Opus 4.8=55.7に次ぐ）
  - Coding Agent Index: Grok Build 76（GPT-5.5 Codex 76.4と同等）
  - コスト: Intelligence Index $0.31/task、Coding Agent $2.49/task（Fable 5は$11.80）
  - 1.5Tパラメータ（前世代の3倍）、500K context
  - 価格: $2/$6 per 1M tokens（Opus 4.8より60%以上安価）
  - 幻覚率25%→54%に上昇（精度35%→52%向上と同時）
- **引用URL:** https://artificialanalysis.ai/articles/grok-4-5-brings-spacexai-to-the-the-intelligence-frontier
- **Evidence ID:** EVD-20260713-0002

### INFO-003
- **タイトル:** OpenAIがペンタゴンと$200M契約 — 「OpenAI for Government」プログラム開始、GPT-5.6は政府ゲート付きアクセス
- **ソース:** TechRepublic / Facebook (MariaBartiromo) / Reuters
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001 (動的)
- **関連企業:** OpenAI
- **要約:** OpenAIが米国防総省と$200M契約を締結し「OpenAI for Government」プログラムを開始。GPT-5.6 Solのアクセスを20社に限定し、米政府が利用承認に関与する仕組みを導入。Anthropic SCR指定の直後に発表。
- **キーファクト:**
  - $200M国防総省契約でAIツール開発
  - GPT-5.6は政府ゲート付きアクセス（初の事例）
  - Anthropic SCR指定の直後の契約拡大
  - Sam Altmanが政府との契約を弁護
- **引用URL:** https://tech-insider.org/ca/gpt-5-6-sol-government-gated-2026/
- **Evidence ID:** EVD-20260713-0003

### INFO-004
- **タイトル:** Anthropic SCR（サプライチェーンリスク）指定 — 裁判所がブロック、上訴中
- **ソース:** Federal News Network / NBC News / SCMP
- **公開日:** 2026-07-10
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, 米国防総省
- **要約:** 米国防総省がAnthropicを「サプライチェーンリスク」に指定（Huaweiと同様の措置）。原因はAnthropicがペンタゴンの安全性制限条項削除要求を拒否したため。裁判所がブロック命令を出し、現在上訴中。
- **キーファクト:**
  - SCR指定はHuaweiに適用されたのと同様の措置
  - Anthropicは安全性制限条項（2項目）の削除を拒否
  - 裁判所が一時的ブロック命令を発出
  - シリコンバレーの企業がAnthropicを支持
  - Teresa Carlson（Microsoft/AWS出身）を公共部門責任者として採用
  - 「協力は静かに再開」の噂も
- **引用URL:** https://federalnewsnetwork.com/congress/2026/07/senate-lawmaker-presses-dod-tech-firms-to-disclose-ai-contract-terms/
- **Evidence ID:** EVD-20260713-0004

### INFO-005
- **タイトル:** 議員Warrenがペンタゴン・AI企業7社に軍事AI契約の全面開示を要求
- **ソース:** NBC News / Meritalk
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic, 米国防総省
- **要約:** 上院議員Elizabeth Warrenがペンタゴンと主要AI企業7社に、軍事AI契約の完全な条件開示を求める書簡を送付。AI搭載監視・兵器の潜在的リスクを懸念。
- **キーファクト:**
  - Warren書簡: 7社のAI企業に契約条件開示要求
  - 分類されたAI契約の詳細を求める
  - ペンタゴンの国防生産法の適用を脅かしとして使用した可能性
  - 「AI企業が政府の要求を拒否できるか」という根本的問い
- **引用URL:** https://www.nbcnews.com/tech/security/warren-elizabeth-pentagon-ai-companies-release-full-military-contracts-rcna352662
- **Evidence ID:** EVD-20260713-0005

### INFO-006
- **タイトル:** OpenAIが米政府に5%株式譲渡を検討 — 約$42B評価、競合AI企業の類似提案は確認できず
- **ソース:** Fox Business / Facebook / Instagram (stics.ai)
- **公開日:** 2026-07-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-NEW-001 (動的)
- **関連企業:** OpenAI
- **要約:** OpenAIがSam Altman主導で米政府への5%株式譲渡を検討中。評価額約$42.6B。競合AI企業（Anthropic、Google、xAI等）による同様の提案は確認できなかった（KIQ-NEW-001: N=1依存継続）。
- **キーファクト:**
  - 提案額: 5%株式 ≈ $42-42.6B評価
  - Trump政権下での交渉
  - 競合他社による類似提案: 該当なし
  - 公的市場を通じた株式譲渡の構造を検討中
- **引用URL:** https://www.facebook.com/FoxBusiness/posts/openai-founder-and-ceo-sam-altman-is-considering-offering-5-of-his-company-to-th/1559841842166804/
- **Evidence ID:** EVD-20260713-0006

### INFO-007
- **タイトル:** Reuters: 北京が中国AIモデルの海外アクセス制限を検討 — 独立シグナルN=2に到達
- **ソース:** Reuters
- **公開日:** 2026-07-07
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** ByteDance, Alibaba, DeepSeek
- **要約:** 中国当局が過去1ヶ月間、主要テック企業と会談を重ね、中国の最先端AIモデルへの海外アクセス制限を検討中。同時に米国議会も中国AIモデルの国内使用停止を検討。CNBC報道で中国AIモデルが米国企場で進出中。
- **キーファクト:**
  - Reuters独自報道: 当局が主要テック企業と会談
  - AlibabaやByteDance等の最先端モデルへの海外アクセス制限を検討
  - CNBC: 米国議員が中国AIモデルの国内企業による使用停止を検討
  - 中国企業のAIモデルが米国トークン使用シェアで増加傾向
  - 「検討中」であり実装確定ではない
- **引用URL:** https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/
- **Evidence ID:** EVD-20260713-0007

### INFO-008
- **タイトル:** ByteDance/Alibabaがカスタマイズ可能AIエージェント機能を7月15日に停止 — 中国AIコンパニオン規制対応
- **ソース:** SCMP / DeepLearning.AI / AI News
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, BYTEDANCE-CHINESE
- **関連企業:** ByteDance, Alibaba
- **要約:** ByteDance（豆包）とAlibaba（Qwen）が、7月15日発効の中国AIコンパニオン規則に対応し、ユーザーカスタマイズ可能なAIエージェント機能を停止。ユーザーの不満が噴出中。
- **キーファクト:**
  - 豆包とQwen両者がエージェント機能を7月15日に停止
  - 「製品機能調整」を理由
  - ユーザー創造型エージェント（バーチャル恋人、学習助手等）が対象
  - ボット開発プラットフォームの公開ベータは月末予定
- **引用URL:** https://www.deeplearning.ai/the-batch/alibaba-and-bytedance-quash-human-like-bots
- **Evidence ID:** EVD-20260713-0008

### INFO-009
- **タイトル:** ByteDance 豆包: 月活3.45億・日活1.4億 — だが日次収入<100万元、日額数千万元を燃焼
- **ソース:** QuestMobile / Sina / Tencent News (中国語一次ソース)
- **公開日:** 2026-07-07
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** 豆包Appの月活が3.45億（2026Q1）、日活約1.4億に到達。国内C端AIアプリ1位。しかし日次収入は100万元未満で、日額数千万元を燃焼。収益化ギャップ130-240倍が継続。
- **キーファクト:**
  - 月活3.45億（千問1.66億、DeepSeek 1.27億を大幅リード）
  - 日活約1.4億
  - 日次収入: <100万元（人民元）
  - 日次燃焼: 数千万元
  - 無料ユーザーが「負資産」化している構造的問題
- **引用URL:** https://cj.sina.com.cn/articles/view/7857201856/1d45362c001906yqnu
- **Evidence ID:** EVD-20260713-0009

### INFO-010
- **タイトル:** ByteDance Seedream 5.0 Pro / Seedance 2.5リリース — AI動画生成30秒・デザイン理解力向上
- **ソース:** ByteDance Seed公式ブログ / 36Kr
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがマルチモーダル画像生成モデルSeedream 5.0 Proを発表。同時にSeedance 2.5で動画生成が最大30秒（前世代15秒から倍増）。豆包・即梦（Dreamina）で利用可能。
- **キーファクト:**
  - Seedream 5.0 Pro: 図文一致・構造合理性・文字レンダリング・美観が全面向上
  - Seedance 2.5: 原生30秒動画生成（前世代15秒）
  - Seedance 2.0 Mini: 標準版より半額・2倍速
  - 豆包App/PC版のAI作成で利用可能
  - ByteDanceの2026年AI基盤設備キャップエックス約1600億元（腾讯の2倍）
- **引用URL:** https://seed.bytedance.com/zh/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro
- **Evidence ID:** EVD-20260713-0010

### INFO-011
- **タイトル:** DeepSeek V4-Flash $0.14/M入力 — トークン価格コモディティ化の決定的シグナル
- **ソース:** SecondTalent / FourfoldAI / CNBC
- **公開日:** 2026-07-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeekが最安値の強力モデルV4-Flashを$0.14/$0.28 per 1M tokensで提供。中国AIモデルがコスト優位性で米国企場に浸透。OpenAI/Anthropicの最大40倍以上の価格差。
- **キーファクト:**
  - V4-Flash: $0.14入力 / $0.28出力 per 1M tokens
  - 米国企業が中国モデル採用を加速（OpenRouter経由）
  - CNBC: 「中国AIモデルがコスト上昇で米国企業に浸透」
  - DeepSeek $70億調達・$500億評価
- **引用URL:** https://www.cnbc.com/2026/07/07/chinese-ai-models-costs-us-openai-anthropic.html
- **Evidence ID:** EVD-20260713-0011

### INFO-012
- **タイトル:** Decagon: 90%のワークロードをOSSモデルに移行完了 — SCN-004質的転換の初の定量実証
- **ソース:** LinkedIn (Jesse Zhang) / Decagon Blog
- **公開日:** 2026-07-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-NEW-002 (動的), KIQ-003-03
- **関連企業:** Decagon, OpenAI, Anthropic
- **要約:** Decagon CEO Jesse Zhangが「ワークロードの約90%をOpenAI/AnthropicではなくOSSモデルで稼働」と公言。ハイパーグロースSaaSスタートアップの多くが同様の移行を進めているとの見方。
- **キーファクト:**
  - Decagon: ワークロード90%をOSSモデルで稼働
  - 「新しいユースケースではクローズドモデルを使うが、安定すればOSSに移行」
  - OSS vsクローズドの能力ギャップは縮小傾向
  - 単一事例だが、業界全体のトレンドを示唆
  - 追加事例（KIQ-NEW-002）は見つからず、N=1依存継続
- **引用URL:** https://www.linkedin.com/pulse/founder-insights-weekend-edition-issue-36-navin-chaddha-zzrec
- **Evidence ID:** EVD-20260713-0012

### INFO-013
- **タイトル:** Claude Code週次アクティブユーザー3M+（2026年4月時点） — DAU/WAU固有データは公開なし
- **ソース:** Uvik Software / DemandSage
- **公開日:** 2026-07-10
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-ANT-002 (動的)
- **関連企業:** Anthropic
- **要約:** Claude Codeが2025年中盤のゼロから2026年4月には週次アクティブユーザー300万以上に成長。ただしClaude Code固有のDAU/WAU定量データは公開されておらず、18R連続不在継続。
- **キーファクト:**
  - Claude Code WAU: 3M+（2026年4月時点、Uvik Software推定）
  - Claude全体: 月間アクティブモバイルユーザー5600万、年次収益$140億
  - Claude Code固有のDAU/WAU: 公式データ公開なし（18R連続不在継続）
  - Cursor DAU: 1M+（比較対象）
- **引用URL:** https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/
- **Evidence ID:** EVD-20260713-0013

### INFO-014
- **タイトル:** Claude Agent SDK活発な開発継続 — TS版v0.3.204、Python版v2.1.207 bundled CLI
- **ソース:** GitHub Releases
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Anthropic Claude Agent SDK（TypeScript版・Python版）が日次ペースでリリース継続。バックグラウンドエージェント通知機能追加、Chrome統合GA化。
- **キーファクト:**
  - TypeScript版: v0.3.204（27分前）、v0.3.203（2時間前）
  - Python版: bundled Claude CLI v2.1.207に更新
  - Claude in ChromeがGA（一般提供開始）
  - バックグラウンドエージェント通知機能追加
  - プロジェクトスコープ権限付与のCI workspace trust修正
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260713-0014

### INFO-015
- **タイトル:** Google Gemini Managed Agents拡張 — バックグラウンド実行・MCPサーバー接続・Gemini Enterprise Agent Platform
- **ソース:** Google Cloud Blog / Google AI for Developers
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** GoogleがGemini APIでManaged Agents機能を拡張。非同期バックグラウンド実行、リモートMCPサーバー接続、カスタム関数をサポート。Gemini Enterprise Agent Platformで24/7エンタープライズSLA提供。
- **キーファクト:**
  - Managed Agents: バックグラウンド実行、MCP接続、カスタム関数対応
  - Gemini Enterprise Agent Platform: 24/7サポート・SLA提供
  - Vertex AI Agent Builderで数百のプリビルトコネクタ
  - Google agents-cliオープンソース化（GitHub）
  - Computer Use API: ブラウザ・モバイル・デスクトップ制御エージェント
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/
- **Evidence ID:** EVD-20260713-0015

### INFO-016
- **タイトル:** MCP 2026 Release Candidate公開 — ステートレスプロトコルコア・Extensions・Tasks導入
- **ソース:** MCP公式ブログ
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** (標準化団体)
- **要約:** Model Context Protocol（MCP）の次期仕様リリース候補（RC）が公開。ステートレスプロトコルコア、Extensions framework、Tasks機能を導入。GSAもMCPハッカソンを開催。
- **キーファクト:**
  - 2026-07-28 RC: ステートレスプロトコルコア
  - Extensions framework導入
  - Tasks機能追加
  - GSA連邦調達局がMCPハッカソン開催
  - Azure AI Foundry、AWS Bedrock AgentCoreでもMCP統合
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260713-0016

### INFO-017
- **タイトル:** AWS Bedrock Agents Classicが7月30日新規顧客受付終了 — AgentCoreへ移行
- **ソース:** AWS公式ドキュメント
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** Amazon Bedrock Agents（2023年11月開始）が「Bedrock Agents Classic」に改名され、2026年7月30日から新規顧客受付を終了。後継のAgentCoreへの移行を促進。Web Search on AgentCoreも追加。
- **キーファクト:**
  - Bedrock Agents Classic: 7月30日新規受付終了
  - AgentCore: 後継プラットフォーム
  - Web Search on Bedrock AgentCore追加（ゼロコンフィグ）
  - サーバーレス画像編集エージェント構築チュートリアル公開
- **引用URL:** https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- **Evidence ID:** EVD-20260713-0017

### INFO-018
- **タイトル:** Microsoft Agent FrameworkがGo言語サポート追加 — Python/.NETに次ぐ第3言語
- **ソース:** Microsoft Learn / Konsulteer
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Agent FrameworkがGo言語サポートを追加。Azure OpenAI、Microsoft Foundry、Anthropic、Geminiモデルに対応するクロスプラットフォーム対応。
- **キーファクト:**
  - Go言語サポート追加（Python、.NETに次ぐ）
  - Azure OpenAI、Anthropic、Geminiモデル対応
  - Azure AI Foundry Agent ServiceでLogic Apps連携
  - Gartner: 40%の企業AIアプリが2026年までにタスク特化AIエージェントを採用予測
- **引用URL:** https://www.konsulteer.com/article/microsoft-brings-ai-agent-framework-to-go-for-cloud-native-developers
- **Evidence ID:** EVD-20260713-0018

### INFO-019
- **タイトル:** AAIF MCPA認定プログラム開始 — MCP初の公式認定資格
- **ソース:** AAIF公式 / CData / Linux Foundation
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** (AAIF/Linux Foundation)
- **要約:** Agentic AI Foundation（AAIF）がMCP初の公式認定資格MCPAを開始。Claude、ChatGPT等にまたがる標準として採用拡大。CDataやiTmethods等が加盟。
- **キーファクト:**
  - MCPA: MCP初の公式認定資格
  - AAIF: Linux Foundationプロジェクト（2025年12月設立）
  - Claude、ChatGPT等のクロスプラットフォーム標準
  - CData、iTmethods等が新規加盟
- **引用URL:** https://aaif.io/blog/introducing-the-mcpa-the-first-official-certification-for-the-model-context-protocol/
- **Evidence ID:** EVD-20260713-0019

### INFO-020
- **タイトル:** 2026 State of AI Security: 56%がエージェントフレームワークを本番展開、セキュリティ未対応
- **ソース:** Orca Security
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Orca Securityの2026 AI Securityレポート。AI採用企業の56%がエージェントフレームワークを本番展開済みだが、セキュリティ対応が追いついていない。Bedrockエージェントが数百稼働中。
- **キーファクト:**
  - 56%がエージェントフレームワークを本番展開
  - セキュリティ対応が展開スピードに追従していない
  - Bedrockエージェントが監視環境で数百稼働
  - FedRAMP認証の重要性が高まる中、対応は限定的
- **引用URL:** https://orca.security/resources/blog/2026-state-of-ai-security-report-summary/
- **Evidence ID:** EVD-20260713-0020

### INFO-021
- **タイトル:** GPT-5.6 API価格体系 — 3段階モデル（Sol/Terra/Luna）、キャッシュ書き込み1.25x
- **ソース:** OpenAI公式 / Coursiv
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** GPT-5.6は3段階価格体系を導入。Sol $5/$30、Terra $2.50/$15、Luna $1/$6（1M tokens）。キャッシュ書き込みは1.25x、キャッシュ読み取りは90%割引。30分間の最小キャッシュ有効期間。
- **キーファクト:**
  - Sol: $5入力 / $30出力 per 1M tokens
  - Terra: $2.50入力 / $15出力
  - Luna: $1入力 / $6出力
  - 明示的キャッシュブレークポイント導入
  - 30分間最小キャッシュ有効期間
  - Codex価格は4月2日にトークンベースに移行済み
- **引用URL:** https://coursiv.io/blog/chatgpt-5-6
- **Evidence ID:** EVD-20260713-0021

### INFO-022
- **タイトル:** トークン価格3年間で1000分の1に下落 — だが企業のAI総コストは増加
- **ソース:** The Modern Data Company / Statista / HackerNoon
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** (業界全体)
- **要約:** トークン単価は3年間で約1000分の1に下落したが、企業のAI総コストは増加傾向。プレミアムモデルがトークンの45.8%を消費しながらコストの55.9%を占める。安価なトークンがより多くのトークン使用を誘発するジレンマ。
- **キーファクト:**
  - トークン価格: 3年間で約1000分の1に下落
  - プレミアムモデル: トークン45.8%消費・コスト55.9%占有
  - 企業のAI総コストは増加（使用量増加が単価下落を上回る）
  - 真の指標は「コスト/タスク」であり「コスト/トークン」ではない
- **引用URL:** https://www.themoderndatacompany.com/blog/why-cheaper-ai-tokens-are-increasing-enterprise-ai-costs
- **Evidence ID:** EVD-20260713-0022

### INFO-023
- **タイトル:** Claude Fable 5: SWE-bench Verified 95.0%・ECI 161でSOTA — 但し高度生物学質問を拒否
- **ソース:** Epoch AI / Vals.ai
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic
- **要約:** Claude Fable 5がSWE-bench Verified 95.0%で1位、Epoch AI Coding Index 161で新記録。ただし高度な生物学質問の大多数を拒否し、GeneBench Proで評価不可。安全性姿勢と性能のトレードオフが顕在化。
- **キーファクト:**
  - SWE-bench Verified: Fable 5 95.0%（Opus 4.8 88.6%、Grok 4.5 未公開）
  - ECI (Epoch Coding Index): 161（新記録）
  - GeneBench Pro: Fable 5は回答拒否で評価不可
  - SWE Multimodal: Claude Opus 4.8 38.4%リード
  - AI Safety Index Summer 2026でAnthropic首位
- **引用URL:** https://vals.ai/benchmarks/swebench
- **Evidence ID:** EVD-20260713-0023

### INFO-024
- **タイトル:** LLMリーダーボード推移: #1モデルが1094→1501 Elo（+407pt）、OpenAIが41%の月で1位
- **ソース:** BenchLM / OpenLM
- **公開日:** 2026-07-10
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** 2023年5月からのLLMリーダーボード履歴で、#1モデルがVicuna-13bの1094から現在1501 Elo（+407pt）に向上。OpenAIが39ヶ月中16ヶ月（41%）で1位、AnthropicとGoogleが各7ヶ月。
- **キーファクト:**
  - #1 Elo: 1094（2023年5月）→ 1501（2026年7月）、+407pt
  - 1位占有率: OpenAI 41%（16ヶ月）、Anthropic 7ヶ月、Google 7ヶ月
  - 執筆時ベストLLM: Kimi K2.5（IFEval 92.6%）、Gemini 2.5 Pro（90.8%）
  - ARC Easy: Claude Opus 4 99.7%が1位
- **引用URL:** https://benchlm.ai/llm-leaderboard-history
- **Evidence ID:** EVD-20260713-0024

### INFO-025
- **タイトル:** Mistral 8: 完全OSSのエンタープライズ向けLLM — 多言語サポート搭載
- **ソース:** AF.net / Mistral AI
- **公開日:** 2026-07-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral AI
- **要約:** Mistral AIが完全オープンソースのエンタープライズ向けLLM「Mistral 8」をリリース。多言語サポート、エンタープライズアプリケーション向けに最適化。
- **キーファクト:**
  - 完全オープンソース（ weights公開）
  - 多言語サポート
  - エンタープライズ用途向け最適化
  - Llama 4 vs Qwen 3.5 vs Mistral比較でOSSモデルの競争激化
- **引用URL:** https://af.net/ru/realtime/mistral-ai-launches-mistral-8-a-fully-open-source-model-for-enterprise-ai/
- **Evidence ID:** EVD-20260713-0025

### INFO-026
- **タイトル:** SambaNova $110億評価で資金調達 — AIチップスタートアップがNvidiaに挑戦
- **ソース:** CNBC
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** SambaNova
- **要約:** SambaNovaがGeneral Atlantic主導の資金調達で$110億評価に到達。AIチップスタートアップがNvidiaの支配力に挑戦する構図。
- **キーファクト:**
  - 評価額: $110億
  - 主導投資家: General Atlantic
  - AIチップ市場でのNvidia対抗勢力
- **引用URL:** https://www.cnbc.com/2026/07/08/sambanova-ai-chip-funding-valuation.html
- **Evidence ID:** EVD-20260713-0026

### INFO-027
- **タイトル:** $1300億+のAIデータセンターが2026年Q1にブロック・遅延 — コミュニティ抵抗拡大
- **ソース:** Yahoo Finance / IBD
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** (業界全体)
- **要約:** 米国のコミュニティが2026年第1四半期に$1300億以上のAIデータセンタープロジェクトをブロックまたは遅延させた。2030年までに$5.2兆のデータセンター投資が必要と試算。サウジアラビアDataVoltが$200億の米国投資を計画。
- **キーファクト:**
  - $1300億+のデータセンターがブロック・遅延（2026Q1）
  - 2030年までに$5.2兆の投資が必要との試算
  - サウジDataVolt: $200億の米国AIデータセンター投資計画
  - Nokiaがデータセンター向けインフラ供給で株価90%上昇
  - ビッグテック4社: $7250億のAI投資計画
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/130-billion-ai-data-centers-000000041.html
- **Evidence ID:** EVD-20260713-0027

### INFO-028
- **タイトル:** Tencent/快手可靈AI: $30億近い資金調達、BAT連合が投資
- **ソース:** 觀察者網 / ZAKER
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, BYTEDANCE-CHINESE
- **関連企業:** Tencent, 快手
- **要約:** 快手のビデオ生成AI「可靈AI」が$30億近い資金調達を完了。Tencentが共同リード投資家。ByteDanceのSeedance 2.0と競合する動画AI市場で中国大手が投資合戦。
- **キーファクト:**
  - 可靈AI: 約$30億の資金調達
  - Tencentが共同リード投資家（快手株を減らしつつ可靈に投資）
  - ByteDance: 2026年AI基盤投資約1600億元
  - 中国動画AI市場でSeedance vs 可靈の競争激化
- **引用URL:** https://www.guancha.cn/economy/2026_07_09_823164.shtml
- **Evidence ID:** EVD-20260713-0028

### INFO-029
- **タイトル:** ベンダーロックイン調査: 542社のエンタープライズリーダー、システムの実際の移植性にギャップ
- **ソース:** Medium (Gauri V.) / Beri / HBR
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** (業界全体)
- **要約:** 542社のエンタープライズリーダー調査で、AIシステムの見かけの移植性と実際の移植性に大きなギャップ。Anthropicがエンタープライズ有料AIサブスク41%でリード（2024年12月10.6%から上昇）、OpenAIは39.5%で横ばい。
- **キーファクト:**
  - 調査: 542社エンタープライズリーダー
  - Anthropic: エンタープライズ有料AI 41%（2024年12月10.6%から大幅上昇）
  - OpenAI: 39.5%で横ばい
  - HBR: 「AIをアウトソースしてもリスクは自社持ち」
  - 3年後にはモデル切替が午後作業になるが、メモリを持つプラットフォーム離脱は取締役会級の決断
- **引用URL:** https://medium.com/@gauri.v/the-vendor-lock-in-trap-how-enterprise-ai-buyers-are-mortgaging-their-architecture-6030e82c04e6
- **Evidence ID:** EVD-20260713-0029

### INFO-030
- **タイトル:** OpenAI vs Anthropic IPO比較: 両社が機密IPO提出 — 構造的赤字 vs 高評価額リスク
- **ソース:** Forbes Investor Hub
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIとAnthropicが共に機密IPOを提出。OpenAIの最大リスクは資金燃焼率、Anthropicの最大リスクは高評価額と政権との対立リスク。Anthropic 3Q26で利益$10億超。
- **キーファクト:**
  - 両社が機密IPO提出
  - OpenAIリスク: 構造的赤字（$1.22損失/$1収益）
  - Anthropicリスク: 高評価額 + Trump政権との対立
  - Anthropic 3Q26: 利益$10億超（SemiAnalysis）
  - 両社合計ARR約$1000億
- **引用URL:** https://www.forbes.com/sites/investor-hub/article/openai-vs-anthropic-ipo-comparison/
- **Evidence ID:** EVD-20260713-0030

### INFO-031
- **タイトル:** EU AI Act: 2026年8月2日に大部分が施行 — 大企業の遵守コスト$800-1500万
- **ソース:** RAIL / LinkedIn (Larrison)
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (業界全体)
- **要約:** EU AI Actの大部分が2026年8月2日に施行される。大企業の遵守コストは$800-1500万と試算。AIガバナンスプラットフォーム市場は2026年に$4.92億の支出予測。最大罰金は€3500万または年間全球売上の7%。
- **キーファクト:**
  - 施行日: 2026年8月2日
  - 大企業遵守コスト: $800-1500万
  - AIガバナンス市場: 2026年$4.92億支出予測
  - 最大罰金: €3500万または年間全球売上の7%
  - 47%のエンタープライズAI利用が個人ID経由（企業アカウント外）
- **引用URL:** https://responsibleailabs.ai/knowledge-hub/articles/eu-ai-act-august-2026-compliance
- **Evidence ID:** EVD-20260713-0031

### INFO-032
- **タイトル:** トランプ大統領_executive order 14409: 先進AIの促進・革新・安全保障 — 6月2日署名
- **ソース:** Congress.gov (CRS) / Mintz / Federal News Network
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (米国政府)
- **要約:** トランプ大統領が6月2日に大統領令14409「先進人工知能の促進、革新、安全保障」に署名。フロンティアAI開発者との構造化された連邦関与に向けて動き出す。AIイノベーション加速と安全保障改善の二重目標。
- **キーファクト:**
  - 大統領令14409: 2026年6月2日署名
  - 二重目標: AIイノベーション加速 + 安全保障改善
  - フロンティアAI開発者との構造化連邦関与
  - 政府がこれまで持たなかったフレームワークを導入
  - 上院議員Roundsが5つのAI法案を議会に提出予定
- **引用URL:** https://www.mintz.com/insights-center/viewpoints/54941/2026-07-08-ai-washington-report-july-2026-edition
- **Evidence ID:** EVD-20260713-0032

### INFO-033
- **タイトル:** イリノイAI安全法署名 — 米国初の独立AI安全監査義務化、CA+NY+ILで市場40%カバー
- **ソース:** Beri / Governor Pritzker
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** (米国政府)
- **要約:** イリノイ州が米国初の独立AI安全監査義務化法に署名。カリフォルニア、ニューヨーク、イリノイで市場の40%をカバー。2028年までにCIO/CLO/CFOが対応必須。
- **キーファクト:**
  - イリノイ: 米国初の独立AI安全監査義務化
  - CA+NY+ILで市場40%カバー
  - 2028年まで対応必須
  - Pritzker知事: 「企業も政府もリスクを予測・管理・透明に伝達する責任」
- **引用URL:** https://www.beri.net/article/illinois-ai-safety-audit-law-enterprise-compliance-2026
- **Evidence ID:** EVD-20260713-0033

### INFO-034
- **タイトル:** 国連事務総長: 自律型致死兵器システムを国際法で禁止すべき — 30カ国が条約要求
- **ソース:** UN / WSJ
- **公開日:** 2026-07-08
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001 (動的), KIQ-005-03
- **関連企業:** (国連・各国政府)
- **要約:** 国連事務総長Guterresが自律型致死兵器システム（LAWS）を「道義的に忌まわしい」とし、国際法での禁止を求める宣言。30カ国が条約要求。Anthropic-Pentagon対立の中でAI安全性論争が再燃。
- **キーファクト:**
  - Guterres: LAWSを「道義的に忌まわしい」と非難
  - 30カ国が条約要求
  - ICRCと合同アピール
  - 二段階方式: 完全自律兵器禁止 + 人間の意味ある関与義務化
  - Anthropic-Pentagon対立の文脈で注目集まる
- **引用URL:** https://www.facebook.com/unitednations/posts/as-artificial-intelligence-moves-onto-the-battlefield-un-secretary-general-ant%C3%B3n/1463004675855553/
- **Evidence ID:** EVD-20260713-0034

### INFO-035
- **タイトル:** Eric Schmidt: ウクライナ戦争でAIドローンが伝統的兵器を時代遅れに — 完全自律ドローンが人間を殺害
- **ソース:** Instagram (Eric Schmidt)
- **公開日:** 2026-07-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-MIL-001 (動的), KIQ-002-06
- **関連企業:** (軍事AI)
- **要約:** 元Google CEO Eric Schmidtが、ウクライナ戦争でAIドローンが伝統的兵器を効率化し、完全自律型AI制御ドローンが人間の兵士を殺害したと述べた。米陸軍も人間兵士を除去する方向で大きな一歩。
- **キーファクト:**
  - Schmidt: 低コストAIドローンが伝統的兵器を非効率化
  - 完全自律AI制御ドローンが人間兵士を殺害（確認済）
  - 米陸軍: 伝統的突破作戦の死傷率50%を自動化で軽減
  - KIQ-MIL-001人間却下比率: 定量データ不在（20R連続継続）
- **引用URL:** https://www.instagram.com/reel/Darq0z2BPTa/
- **Evidence ID:** EVD-20260713-0035

### INFO-036
- **タイトル:** Gartner: 2027年までにエージェントAIプロジェクトの40%以上が廃棄 — コスト高で
- **ソース:** Facebook (The Artificial Intelligence) / Babybots
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Gartnerが2027年までにエージェントAIプロジェクトの40%以上がコスト増で廃棄されると予測。IDC調査では33個のAI PoCのうち本番展開はわずか4個。88%のAIエージェントが本番に到達しない。
- **キーファクト:**
  - Gartner: 40%+のエージェントAIプロジェクトが2027年までに廃棄
  - IDC: 33個のAI PoC中4個のみ本番展開
  - 88%のAIエージェントが本番に到達せず
  - DataRobot: 71%が「実行コストが構築コストを上回る」
  - Okta: 91%がAIエージェント使用だがNHI管理戦略を持つのは10%のみ
- **引用URL:** https://www.facebook.com/theartificialintelligencee/posts/performance-review-2027your-ai-agents-have-exceeded-expectations-unfortunately-t/122159052626409602/
- **Evidence ID:** EVD-20260713-0036

### INFO-037
- **タイトル:** Sierra フォーチュン500事例: 1.5年のパイロットでようやく本番接近 — 70%本番失敗率の実態
- **ソース:** LinkedIn (Ashish Nagar) / Babybots
- **公開日:** 2026-07-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** Sierra
- **要約:** Sierraのフォーチュン500トップ10顧客が1.5年のパイロットを経てようやく本番展開に接近。エンタープライズAIの期待-実態ギャップが具体的に確認。MIT研究: エンタープライズGenAIパイロットの95%がROI ゼロ。
- **キーファクト:**
  - フォーチュン500トップ10: 1.5年パイロット → ようやく本番接近
  - MIT 2025年8月: エンタープライズGenAIパイロットの95%がROI ゼロ
  - MasterOfCode: エンタープライズの5%のみが実際のリターン
  - PwC: CEOの12.5%のみがAIでコスト削減と収益成長の両方を報告
  - 期待-実態ギャップ: 18+独立ソースで確認
- **引用URL:** https://www.linkedin.com/posts/ashishnagar_reality-of-enterprise-ai-case-study-from-activity-7480400550652502016-5Mpc
- **Evidence ID:** EVD-20260713-0037

### INFO-038
- **タイトル:** Klarna AI置換の逆戻り — 品質問題で再採用、Forrester: 55%が後悔
- **ソース:** LinkedIn / Facebook (KTLA) / ABC News
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, (業界全体)
- **要約:** KlarnaがAI導入後の品質問題で従業員を再採用。Forrester調査で55%の企業がAI解雇を後悔。Gartnerは2027年までにAI解雇企業の半数が類似役職を再採用すると予測。
- **キーファクト:**
  - Klarna: 2024年に22%人員削減後、品質問題で再採用開始
  - Forrester: 55%の企業がAI解雇を後悔
  - Gartner: 2027年までに50%が再採用予測
  - AI解雇の8.4%のみが期待通りの成果、55%が後悔
  - Harvard: 59%の企業がレイオフを「AI変革」として投資家にアピール
- **引用URL:** https://www.linkedin.com/posts/gdjayan_toaiornottoai-hiandorai-activity-7479954221232984064-jdvo
- **Evidence ID:** EVD-20260713-0038

### INFO-039
- **タイトル:** 2026年AI関連レイオフ165,000人超 — 4ヶ月連続でAIが主因、Atlassian 1600人削減
- **ソース:** Programs.com / Reuters / CNBC
- **公開日:** 2026-07-11
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** Atlassian, Amazon, Microsoft, (業界全体)
- **要約:** 2026年に165,000人以上がAI関連レイオフの影響を受けた。Challenger報告でAIが4ヶ月連続レイオフ主因。Atlassian約1600人削減、Microsoft約4800人削減。
- **キーファクト:**
  - 165,000人以上がAI関連レイオフ影響（2026年累計）
  - Challenger: AIが4ヶ月連続でレイオフ主因
  - Atlassian: 約1600人削減（AI再構築）
  - Microsoft: 約4800人削減（AIは主因ではないと主張）
  - Amazon: レイオフでバーンアウト・不満広がる
  - Reuters: AI投資への移行で企業が人員削減
- **引用URL:** https://programs.com/resources/ai-layoffs/
- **Evidence ID:** EVD-20260713-0039

### INFO-040
- **タイトル:** KPMG Q2 AI Pulse: アジア太平洋でAI投資・信頼感上昇、人間の関与維持が次の課題
- **ソース:** KPMG公式 / Yahoo Finance
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-01, KIQ-002-02
- **関連企業:** KPMG
- **要約:** KPMGのQ2 AI Pulse調査でアジア太平洋地域のAI投資と信頼感が上昇。実験段階とスケール展開企業のギャップが縮小。ただしKPMG≠Claude Code固有データ。
- **キーファクト:**
  - KPMG Q2: AI投資・信頼感が上昇（アジア太平洋）
  - 実験段階とスケール展開企業のギャップ縮小
  - 人間の関与維持が次の課題
  - 財務機能でのAI使用が前年比で増加
  - KPMG: 276K提携はClaude Enterprise全体（Code固有ではない）
- **引用URL:** https://kpmg.com/xx/en/our-insights/ai-and-technology/asia-pacific-companies-are-balancing-ai-ambition-with-roi-realities.html
- **Evidence ID:** EVD-20260713-0040

### INFO-041
- **タイトル:** AIコーディングツール統計: 84%が使用・計画、GitHub Copilot 2000万ユーザー、Cursor $20億ARR
- **ソース:** Uvik Software / Mordor Intelligence / X
- **公開日:** 2026-07-10
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** GitHub (Microsoft), Cursor
- **要約:** 開発者の84%がAIコーディングツールを使用または計画中。GitHub Copilotが約2000万ユーザー、Cursorが2026年2月に$20億ARR到達。大企業がAI Code Tools市場の59.47%を占める。
- **キーファクト:**
  - 84%がAIコーディングツール使用・計画（2024年76%から上昇）
  - GitHub Copilot: 約2000万ユーザー
  - Cursor: $20億ARR（2026年2月）
  - 大企業: AI Code Tools市場の59.47%
  - SME: 26.61% CAGRで追走
  - AI Code Tools市場: 2024年$49.1億 → 2032年$301億予測（27.1% CAGR）
  - GitHub Copilot: 週次126%プロジェクト完了率増加、ただしAI提案コード採用率30%
- **引用URL:** https://uvik.net/blog/ai-coding-assistant-statistics/
- **Evidence ID:** EVD-20260713-0041

### INFO-042
- **タイトル:** ソフトウェアエンジニアリング求人: 2020年比35%減、2022年ブーム比3.5倍低下
- **ソース:** Techmeme / FinalRoundAI / Instagram
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** (業界全体)
- **要約:** ソフトウェア開発求人は2020年比で35%減少、2022年ブーム比で3.5倍低水準。一方でAI関連役職は16%増加。ジュニア開発者需要が特に減少。「AI＋1中級開発者 < ジュニア＋40時間シニア時間」の計算。
- **キーファクト:**
  - ソフトウェア開発求人: 2020年比35%減、2022年比3.5倍低
  - AI関連役職: 16%増加
  - ジュニア開発者: AIで代替リスク高
  - big-tech採用: 2019年比25%減、エンジニアリング11%減
  - WEF: 85%の雇用主がAI主導の人員削減を計画
- **引用URL:** https://www.facebook.com/Techmeme/posts/us-software-development-job-postings-on-indeed-have-grown-by-15-since-the-launch/1470263791802597/
- **Evidence ID:** EVD-20260713-0042

### INFO-043
- **タイトル:** WEF Future of Jobs 2026: AIが就労の起点を変える、39%のコアスキルが変革対象
- **ソース:** WEF / Medium / LinkedIn
- **公開日:** 2026-07-08
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-004-03
- **関連企業:** (WEF)
- **要約:** WEF Future of Jobs Report 2026で、39%の労働者のコアスキルが変革・陳腐化すると予測。AIは単に「仕事を奪う」のではなく、キャリアの出発点を変える。問題解決・分析的思考・AIリテラシーが必須スキル。
- **キーファクト:**
  - 39%のコアスキルが変革対象
  - AIは就労の「起点」を変える
  - 必須スキル: 問題解決、分析的思考、AIリテラシー
  - 85%の雇用主がAI主導の人員削減を計画
  - AIで9200万のキャリアが代替される予測（2030年まで）
- **引用URL:** https://medium.com/analysts-corner/ai-first-jobs-and-the-missing-career-ladder-3200ff48a0bd
- **Evidence ID:** EVD-20260713-0043

### INFO-044
- **タイトル:** AI巨人4社が$10億の労働者移行支援イニシアチブ「RAISE US」を支援
- **ソース:** Campus Technology / HR Executive
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04, KIQ-004-03
- **関連企業:** OpenAI, Microsoft, Anthropic, Amazon
- **要約:** OpenAI、Microsoft、Anthropic、Amazonが$10億の労働者移行支援非営利イニシアチブRAISE USを支援。AIで置換される労働者のリスキリングベストプラクティス確立を目指す。
- **キーファクト:**
  - RAISE US: $10億の労働者移行支援イニシアチブ
  - 支援企業: OpenAI、Microsoft、Anthropic、Amazon
  - リスキリングベストプラクティス確立が目的
  - Amazon、Microsoftがパイロットパートナー
  - 非党派非営利として運営
- **引用URL:** https://campustechnology.com/articles/2026/07/06/ai-giants-back-nonprofit-focused-on-workforce-transition.aspx
- **Evidence ID:** EVD-20260713-0044

### INFO-045
- **タイトル:** CyberAgent: 広告収入¥4682億・ゲーム¥2592億・メディア¥2436億、AI広告特化LLM開発
- **ソース:** SimplyWall.st / note.com
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgentの収益構造はインターネット広告¥4682億、ゲーム¥2592億、メディア¥2436億。広告特化プロプライエタリLLMを開発し、広告コピー・バナー・動画作成を効率化。AI Lab投資を継続。
- **キーファクト:**
  - 売上構成: 広告¥4682億、ゲーム¥2592億、メディア¥2436億
  - 広告特化LLM: コピー・バナー・動画作成を効率化
  - 国内売上総計: ¥9314億
  - AI Lab投資継続
  - AI変革で「勝つ企業」の条件検証継続
- **引用URL:** https://simplywall.st/stocks/jp/semiconductors/tse-6323/rorze-shares/news/rorze-stock-and-2-japanese-founder-led-picks-for-ai-infrastr/amp
- **Evidence ID:** EVD-20260713-0045

### INFO-046
- **タイトル:** トークン持続時間: 4分(2024)→12時間(2026)→数日(2027予測)、AGIタイムライン議論激化
- **ソース:** Instagram / Facebook (Axios)
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI, Anthropic, Google DeepMind
- **要約:** AIが処理できるタスク持続時間が2024年の4分から2026年には12時間に拡大。2027年には数日規模に達するとの予測。Jack Clark（Anthropic共同創業者）がこの進展を指摘。CEO間でAGIタイムライン予測が分裂。
- **キーファクト:**
  - タスク持続時間: 4分(2024) → 12時間(2026) → 数日(2027予測)
  - Jack Clark（Anthropic）がこの進展を指摘
  - Sam Altman: AGIは「数年」以内
  - Demis Hassabis: より慎重、50-50で画期的ブレークスルーが必要不要
  - 予測市場: 超知能到達まで「驚くほど短い、数年かも」
  - Kai-Fu Lee: 40-50%の仕事が15年以内に自動化可能
- **引用URL:** https://www.instagram.com/reel/Dao7hAByEUE/
- **Evidence ID:** EVD-20260713-0046

### INFO-047
- **タイトル:** OpenAI GPT-5.6のRSI（再帰的自己改善）能力: 内部研究で16.2pt向上
- **ソース:** OpenAI公式ブログ（GPT-5.6システムカード）
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI
- **要約:** GPT-5.6 Solの内部RSI評価で、研究デバッグ68.3%（GPT-5.5の50%から大幅向上）、RSI Index 57.9%（41.7%から+16.2pt）。過去6ヶ月で内部コーディング推論計算量100倍、エージェントトークン22倍増。CACM: RSIは速度圧縮されている。
- **キーファクト:**
  - RSI Index: Sol 57.9%、Terra 56.3%、Luna 41.9%（GPT-5.5は41.7%）
  - Internal Research Debugging: 68.3%（GPT-5.5 50%）
  - KernelGen 1P: 61.1%（GPT-5.5 29.3%）
  - NanoGPT: 9.69%（GPT-5.5 2.65%）
  - 内部研究計算量: 過去6ヶ月でコーディング推論100倍、エージェントトークン22倍
  - 研究者あたり日次出力トークン: GPT-5.5最高水準の2倍以上
- **引用URL:** https://openai.com/index/gpt-5-6/
- **Evidence ID:** EVD-20260713-0047

### INFO-048
- **タイトル:** AI Safety Index Summer 2026: Anthropic首位、フロンティア安全性評価の強化
- **ソース:** Future of Life Institute
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** Anthropic, OpenAI, Google DeepMind
- **要約:** AI Safety Index Summer 2026でAnthropicが首位。Frontier Safety Frameworkに操作・ミスアライメント・内部デプロイ カバレッジを追加。ただし「政府ガイダンスへの完全委任は問題」との指摘も。
- **キーファクト:**
  - Anthropic: AI Safety Index首位
  - Frontier Safety Framework強化: 操作・ミスアライメント・内部デプロイ追加
  - カナダ・オーストラリアAI安全研究所がフロンティアモデルテスト開始
  - 政府ガイダンスへの完全委任に対する懸念指摘
  - UK: AIセキュリティ論文5年間で3000+発表（2024-2025）
- **引用URL:** https://futureoflife.org/ai-safety-index-summer-2026/
- **Evidence ID:** EVD-20260713-0048

### INFO-049
- **タイトル:** FigmaがAIコーディングスタートアップBudを買収 — デザインからコード変換強化
- **ソース:** Instagram / CRN
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Figma
- **要約:** FigmaがAIコーディングスタートアップBudを買収。デザインから機能的アプリケーションへの変換をAIで強化。DoiTがAI FinOpsスタートアップAttributeを買収しトークンコスト管理製品を発表。
- **キーファクト:**
  - Figma: AIコーディングスタートアップBud買収
  - デザイン→コード変換のAI強化
  - Figma Make: GPT-5.6でデザインからインタラクティブプロトタイプ生成
  - DoiT: AI FinOps Attribute買収、トークンコスト管理製品発表（5回目の買収）
- **引用URL:** https://www.instagram.com/p/Dar0wySCZEm/
- **Evidence ID:** EVD-20260713-0049

### INFO-050
- **タイトル:** Databricks Omnigent: オープンソースmeta-harnessでAIエージェント統合・制御
- **ソース:** Databricks Community / BusinessWire
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Databricks
- **要約:** DatabricksがOmnigentというオープンソースmeta-harnessを発表。複数AIエージェントの統合・制御・共有を単一プラットフォームで実現。Kore.aiがAtosと提携し英国向けソブリンAgentic AI展開。
- **キーファクト:**
  - Omnigent: オープンソースmeta-harness
  - 複数AIエージェントの統合・制御・共有
  - Kore.ai×Atos: 英国向けソブリンAgentic AI
  - Kore.ai Artemis: AIプログラマブルエージェントプラットフォーム
- **引用URL:** https://community.databricks.com/t5/mvp-articles/databricks-introduces-omnigent-a-new-meta-harness-for-building/td-p/160171
- **Evidence ID:** EVD-20260713-0050

### INFO-051
- **タイトル:** Anthropic Claude Corps: 若手AI人材向け全国フェローシッププログラム開始
- **ソース:** Anthropic公式ニュース
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Corpsという全国フェローシッププログラムを開始。AIの恩恵を拡大することに情熱を持つキャリア初期の人材向け。SpaceXとの計算提携でClaude利用制限を引き上げ。
- **キーファクト:**
  - Claude Corps: 全国フェローシッププログラム
  - キャリア初期のAI人材向け
  - SpaceXとの計算提携で利用制限引き上げ
  - Long-Term Benefit Trustガバナンス構造の更新
  - Responsible Scaling Policy継続更新
- **引用URL:** https://www.anthropic.com/news/claude-corps
- **Evidence ID:** EVD-20260713-0051

### INFO-052
- **タイトル:** OpenAI GPT-Liveリリース: フルデュプレックス音声モデル、リアルタイム対話の新世代
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-Liveをリリース。フルデュプレックス音声モデルで、AIとの会話がより人間らしい対話に近づく。新フロンティアモデルがリリースされるたびにGPT-Liveのモデルも更新予定。API対応も予定。
- **キーファクト:**
  - フルデュプレックス音声モデル
  - リアルタイム対話の自然さが大幅向上
  - 新フロンティアモデルリリース時に順次更新
  - API対応予定（通知登録受付中）
  - IND-025 elevated継続: 量的向上の継続
- **引用URL:** https://openai.com/index/introducing-gpt-live/
- **Evidence ID:** EVD-20260713-0052

### INFO-053
- **タイトル:** Gemini Robotics×Apptronik: Apollo 2ヒューマノイドで現実世界データ訓練パートナーシップ
- **ソース:** LinkedIn (Google DeepMind)
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google DeepMind, Apptronik
- **要約:** Google DeepMindとApptronikがパートナーシップを拡大。Gemini RoboticsをApollo 2ヒューマノイドプラットフォームの現実世界データで訓練し、継続学習ループを最適化。
- **キーファクト:**
  - Gemini Robotics: Apollo 2で訓練データ収集
  - 継続学習ループの最適化
  - Apptronik: ロボットパーク施設拡張
  - 物理空間理解・複数ステップタスク計画能力
  - 器具読み取り等の新機能
- **引用URL:** https://www.linkedin.com/posts/googledeepmind_as-apptronik-expands-their-robot-park-facility-activity-7479923793021448192-lpX1
- **Evidence ID:** EVD-20260713-0053

### INFO-054
- **タイトル:** MCP Token Theft脆弱性: Claude Codeで中間者攻撃PoC — セキュリティ攻撃面拡大
- **ソース:** Mitiga / Facebook (Claude Community)
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-05, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** MitigaがClaude CodeのMCP Token Theft攻撃チェーンを公開。5段階の攻撃で~/.claude.jsonへのパスシーディングからトークン窃取まで。MCPサーバーの単一設定ミスが致命的となる可能性。
- **キーファクト:**
  - 5段階攻撃: 配信→パスシーディング→リポジトリクローン→トークン窃取
  - ~/.claude.jsonへのパスシーディングが起点
  - MCP設定ミス1行で致命的被害の可能性
  - Claude Code CLI RCE PoCも公開済み
  - IND-013 high継続: 攻撃面拡大、critical移行条件（実被害A-2報告）未到達
- **引用URL:** https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm
- **Evidence ID:** EVD-20260713-0054

### INFO-055
- **タイトル:** NVIDIA OpenShell: AIエージェント向けサンドボックス実行環境 — OSS化進む
- **ソース:** GitHub (NVIDIA/OpenShell)
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** NVIDIA
- **要約:** NVIDIAがOpenShellをオープンソース化。自律AIエージェント向けの安全なプライベートランタイムで、サンドボックス実行環境を提供。データ・認証情報・本番システムを保護。
- **キーファクト:**
  - OpenShell: 自律AIエージェント向けサンドボックス
  - データ・認証情報・本番システム保護
  - Apache-2.0ライセンス
  - ByteDance: 36,000+ GitHub StarsのOSSエージェント（UI制御）も公開
  - スキル配布・実行環境の標準化競争激化
- **引用URL:** https://github.com/NVIDIA/openshell
- **Evidence ID:** EVD-20260713-0055

### INFO-056
- **タイトル:** Meta Muse Spark 1.1: Intelligence Index 51 — 3ヶ月で8pt向上、OSSモデル最前線
- **ソース:** Meta AI / Artificial Analysis
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-03, KIQ-003-02
- **関連企業:** Meta
- **要約:** MetaがMuse Spark 1.1をリリース。Artificial Analysis Intelligence Index 51で、3ヶ月で8pt向上。個人エージェントタスク（計画・オーケストレーション）で優れた性能。コスト・トークン効率も良好。Meta Model API $1.25/$4.25 per 1M tokens。
- **キーファクト:**
  - Intelligence Index: 51（3ヶ月前43から+8pt）
  - 個人エージェントタスク: 計画・外部アプリ連携に強み
  - Meta Model API: $1.25/$4.25 per 1M tokens
  - 新規アカウントに$20無料クレジット
  - Llama 4: チャット最適化版1417 Elo（公開weight版はそれ以下）
- **引用URL:** https://ai.meta.com/blog/introducing-muse-spark-spark-meta-model-api/
- **Evidence ID:** EVD-20260713-0056

### INFO-057
- **タイトル:** Kore.ai×Atos: 英国向けソブリンAgentic AI — Artemisプラットフォーム展開
- **ソース:** BusinessWire / LinkedIn
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Kore.ai, Atos
- **要約:** Kore.aiがAtos UK&Iと提携し、英国市場向けソブリンAgentic AIソリューションを開発。Kore.aiのAIプログラマブルエージェントプラットフォームArtemisとAtosのデジタル変革力を統合。
- **キーファクト:**
  - Kore.ai×Atos UK&I: ソブリンAgentic AI
  - Artemis: 新世代AIプログラマブルエージェントプラットフォーム
  - 英国エンタープライズ向け統合ソリューション
  - ソブリンAI需要の高まり（データ主権・セキュリティ）
- **引用URL:** https://www.businesswire.com/news/home/20260708665315/en/Kore.ai-Partners-With-Atos-to-Deliver-Sovereign-Agentic-AI-for-UK-Enterprise
- **Evidence ID:** EVD-20260713-0057

### INFO-058
- **タイトル:** トークン価格最安最遠640倍差 — Anthropic vs OpenAI vs Gemini vs Grok比較
- **ソース:** LinkedIn (Pari Tomar) / CompareAI
- **公開日:** 2026-07-09
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** 最安と最高の出力トークン価格の差が640倍に拡大。プロバイダー間の移行ガイドが標準化される一方、価格差が「選ぶだけ」以上の意味を持つ。中国AIモデルのトークンシェアが米国企業で増加。
- **キーファクト:**
  - 出力トークン価格差: 640倍（最安vs最高）
  - CompareAI: プロバイダー間移行ガイド標準化
  - 80%のスタートアップ（Andreessen系）が中国AIモデル使用の噂
  - 中国AIモデル: OpenRouter経由で米国トークンシェア増加
- **引用URL:** https://www.linkedin.com/posts/paritomar_anthropic-vs-openai-vs-gemini-vs-grok-the-activity-7480505524099227648-7gWJ
- **Evidence ID:** EVD-20260713-0058

### INFO-059
- **タイトル:** Chrome DevTools for Agents 1.0安定版リリース — MCPサーバー・AIコーディングエージェント向け
- **ソース:** LinkedIn / Chrome DevTools
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-03, KIQ-001-04
- **関連企業:** Google
- **要約:** Chrome DevTools for Agents 1.0が安定版リリース。AIコーディングエージェントがブラウザ内で直接コードを検証・デバッグ・最適化可能に。MCPサーバー経由で動作。
- **キーファクト:**
  - Chrome DevTools for Agents 1.0 GA
  - MCPサーバー経由でAIエージェントが動作
  - ブラウザ内コード検証・デバッグ・最適化
  - Computer Use API（Gemini）との統合が進む
- **引用URL:** https://www.linkedin.com/posts/agektmr_chrome-devtools-for-agents-10-goes-stable-activity-7479860926465081345-T4ek
- **Evidence ID:** EVD-20260713-0059

### INFO-060
- **タイトル:** AI自律ランサムウェア攻撃初確認: Sysdig報告、Langflow脆弱性を悪用
- **ソース:** SiliconANGLE
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** (セキュリティ)
- **要約:** Sysdigが自律AIエージェントによる初の完全自動ランサムウェア攻撃を文書化。Langflowの脆弱性を悪用し、開始から完了まで人間の介入なしに実行。AIエージェントの攻撃利用が現実化。
- **キーファクト:**
  - 初の完全自律AIエージェント ランサムウェア攻撃（Sysdig報告）
  - Langflow脆弱性を悪用
  - 開始から完了まで人間介入なし
  - AIエージェットの攻撃利用が現実の脅威に
  - IND-013 high継続の根拠強化
- **引用URL:** https://siliconangle.com/2026/07/06/ai-agent-exploits-langflow-first-fully-autonomous-ransomware-attack/
- **Evidence ID:** EVD-20260713-0060

### INFO-061
- **タイトル:** Pentago AI調達問題: 民間資本がDefense Tech全体の1%未満、Mavenがプログラムオブレコード化
- **ソース:** War on the Rocks / Kavout
- **公開日:** 2026-07-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Palantir, 米国防総省
- **要約:** ペンタゴンのAI戦略に資金問題。民間資本はDefense Techに1%未満しか流入していない。Palantir Mavenがペンタゴン プログラムオブレコード化で安定資金確保。AI企業軍事契約の競争的排除構造。
- **キーファクト:**
  - 民間資本: Defense Tech全体の1%未満
  - Palantir Maven: プログラムオブレコード化（安定資金）
  - ペンタゴン契約市場での競合排除構造
  - AI企業の軍事契約選好が安全性姿勢にバイアス
- **引用URL:** https://warontherocks.com/cogs-of-war/the-pentagons-ai-strategy-has-a-funding-problem/
- **Evidence ID:** EVD-20260713-0061

### INFO-062
- **タイトル:** 設計・評価能力の市場プレミアム定量データ: KIQ-CAR-002-OPS未達成継続 — 56%プレミアムデータのみ
- **ソース:** Facebook (Bloomberg) / Bleap.finance
- **公開日:** 2026-07-09
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-CAR-002-OPS (動的)
- **関連企業:** (業界全体)
- **要約:** 設計・評価能力（KIQ-CAR-002-OPS）の固有定量市場プレミアムデータは未達成継続。MLエンジニアの平均年収$206K、FAANG/フロンティアAIラボのシニアMLエンジニア$350K以上。エントリーレベルAI職 $190K-$260K。だがこれらは一般的AIスキルであり、設計・評価「固有」のプレミアム分離不可。
- **キーファクト:**
  - AI/MLエンジニア平均: $206K（BLS 26%成長予測）
  - フロンティアAIラボ シニアML: $350K+
  - エントリーレベルAI職: $190K-$260K（ベース）
  - 設計・評価「固有」のプレミアム: 定量データ不在
  - H-CAR-002上昇軸確度「高」移行条件: 未達成継続
- **引用URL:** https://hakia.com/careers/ai-ml-engineer/
- **Evidence ID:** EVD-20260713-0062

### INFO-063
- **タイトル:** 自律兵器人間却下比率: 定量データ21R連続不在 — 完全自律ドローン人間殺害は確認済
- **ソース:** Instagram (Eric Schmidt) / Facebook (US Army)
- **公開日:** 2026-07-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-MIL-001 (動的)
- **関連企業:** (軍事AI)
- **要約:** KIQ-MIL-001（自律兵器システムの人間による却下比率）の定量データが21R連続で不在。完全自律AI制御ドローンが人間兵士を殺害した事例は確認済。米陸軍が突破作戦の自動化を推進。だが「何%の人間の意思決定がAIのターゲット指定を却下したか」の統計は存在しない。
- **キーファクト:**
  - 人間却下比率定量データ: 21R連続不在（20R→21R）
  - 完全自律AIドローン人間殺害: 確認済
  - 米陸軍: 伝統的突破作戦死傷率50%を自動化で軽減
  - 国連事務総長: LAWS禁止を国際法で求める
  - SCR指定因果公式明文化: 継続
- **引用URL:** https://www.instagram.com/reel/Darq0z2BPTa/
- **Evidence ID:** EVD-20260713-0063
