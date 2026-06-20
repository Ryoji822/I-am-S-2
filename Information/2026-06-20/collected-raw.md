# 収集データ: 2026-06-20

## メタデータ
- 収集日時: 2026-06-20 00:15 UTC（開始）〜 01:30 UTC（完了）
- 品質フラグ: NORMAL
- 実行クエリ数: 約139件（計画121件 + 動的18件）
- 詳細スクレイプ数: 4件（Anthropic TCS提携, Anthropic Fable公告, futuresearch.ai予測, builtin.com紛争タイムライン）
- 収集情報数: 112件（INFO-001 〜 INFO-112）
- Evidence ID 採番範囲: EVD-20260620-0001 〜 EVD-20260620-0112
- KIQカバレッジ: 全24計画KIQ ✓ + 5動的KIQ ✓（KIQ-MIL-001, KIQ-GOV-002, KIQ-OAI-001, KIQ-BTD-001, KIQ-GOV-001）
- Tier 1企業カバレッジ: OpenAI(51件言及), Anthropic(76件), Google(77件), xAI(19件), ByteDance(13件)
- 重複Evidence ID: なし（検証済み）
- 動的追加クエリ（Arbiter優先KIQより生成）: KIQ-MIL-001, KIQ-GOV-002, KIQ-OAI-001, KIQ-BTD-001, KIQ-GOV-001

## 収集結果

### INFO-001
- **タイトル:** Anthropic、TCSと提携し規制産業へClaude展開（50,000従業員・56カ国）
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic, TCS
- **要約:** AnthropicがTata Consultancy Services（TCS）と提携。TCSは自社50,000従業員にClaudeを提供し、金融・医療・公共部門など規制産業向けClaude搭載製品を構築。Claude Partner Networkに参加。インド（第2の市場）展開を強化。
- **キーファクト:**
  - Diligenta（TCSの英国生命年金事業）が2,200万以上の契約者向け顧客体験向上にClaude使用
  - TCSバンキングチームがClaude Codeでソフトウェアエンジニアリング生産性向上
  - TCS iONが年間7,500万件の評価を1,500都市で実施、Claude訓練・認証を提供
  - Dario Amodei「インドは我々の第2の市場」
- **引用URL:** https://www.anthropic.com/news/tcs-anthropic-partnership
- **Evidence ID:** EVD-20260620-0001

### INFO-002
- **タイトル:** 米政府、AnthropicのFable 5/Mythos 5への全外国籍アクセス停止を輸出管理指令
- **ソース:** Anthropic公式 / BBC / Al Jazeera / Time / InfoQ
- **公開日:** 2026-06-12
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-001
- **関連企業:** Anthropic
- **要約:** 米政府が国家安全保障懸念を理由に、Anthropicの最新最強モデル「Claude Fable 5」および「Mythos 5」への外国人による全アクセス停止を命じる輸出管理指令を発出。公開わずか数日後の停止で、同盟関係に緊張をもたらす。
- **キーファクト:**
  - Claude Fable 5は「Mythos-class」と呼ぶ新能力レベルの初の公開モデル（6月9日リリース）
  - 公開直後に国家安全保障懸念で外国籍アクセス全面停止
  - 同盟国関係に悪影響（Al Jazeera報道）
  - Fable 5はSWFTE 100/100首位の報告あり（Arbiter v4.13参照）
- **引用URL:** https://www.anthropic.com/news/fable-mythos-access
- **Evidence ID:** EVD-20260620-0002

### INFO-003
- **タイトル:** Google I/O 2026：Gemini 3.5 Flash・Spark・Antigravity・Gemini Omni Flash発表、アジェンティックAIへの転換
- **ソース:** MediaPost / ppc.land / Google Cloud Blog
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** Google I/O 2026でDemis Hassabisが「Gemini Omni Flash」（ビデオ・画像・音声を統合する新モデルファミリーの初号機）を発表。Gemini 3.5 Flash、Spark、Antigravityが生産性・コーディング・検索の未来を再構築中。アジェンティックAI転換を強調。
- **キーファクト:**
  - Gemini Omni Flash: 動画・画像・音声統合の新モデルファミリー初号機
  - Gemini 3.5 Flash: 英国データレジデンシー対応（国内処理）
  - Spark/Antigravity: コーディング・生産性・検索領域のアジェンティック再構築
  - Google Cloud London Summit: 英国のアジェンティックエンタープライズAI主導を強調
- **引用URL:** https://ppc.land/inside-google-i-o-2026-the-agentic-ai-shift-no-one-saw-coming/
- **Evidence ID:** EVD-20260620-0003

### INFO-004
- **タイトル:** DeepMind、英国住宅建設AI加速計画プロトタイプ（Gemini）で処理時間半減を目指す
- **ソース:** DeepMind公式ブログ
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-005-01
- **関連企業:** Google / DeepMind, 英国政府
- **要約:** DeepMindが英国政府と協力し、住宅所有者申請処理時間を半減させるAI計画プロトタイプを構築。Geminiベースの政府向けAI適用事例。
- **キーファクト:**
  - 英国政府AI計画プロトタイプをGeminiで構築
  - 住宅申請処理時間を半減目標
  - 政府×フロンティアAI企業の協同事例
- **引用URL:** https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/
- **Evidence ID:** EVD-20260620-0004

### INFO-005
- **タイトル:** Google Home Speaker for Gemini発表、Geminiネイティブのスマートホームハブ
- **ソース:** Google公式ブログ
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google
- **要約:** Geminiネイティブ設計のGoogle Home Speaker発表。スマートホーム機器制御・ルーティン管理・自然言語応答を統合したマルチモーダル consumer agent。
- **キーファクト:**
  - Gemini専用設計のハードウェア
  - スマートホーム制御・ルーティン・自然言語応答
  - consumer向けマルチモーダルagent展開
- **引用URL:** https://blog.google/products-and-platforms/devices/google-nest/google-home-speaker-gemini-features/
- **Evidence ID:** EVD-20260620-0005

---

## KIQ-MIL-001（動的追加: Operation Epic Fury / Grok軍事展開の民間被害・ガードレール・人間監視）

### INFO-006
- **タイトル:** ペンタゴン、イラン作戦「Operation Epic Fury」でGrok AIにより96時間で2,000発のミサイル発射を確認
- **ソース:** The Independent / Novara Media / AOL
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06
- **関連企業:** xAI, Pentagon (米国防総省)
- **要約:** ペンタゴンの高官が、イラン軍事資産を標的とする「Operation Epic Fury」（2026年2月28日開始の米・イスラエル共同キャンペーン）でElon MuskのGrokチャットボットが使用され、96時間で2,000発の弾薬が発射されたと公表。AIが目標を特定し人間が承認するkill chain構造。LLMがキルチェーンに組み込まれた初の文書化事例。
- **キーファクト:**
  - Operation Epic Fury: 2026年2月28日開始、米イスラエル共同の対イラン空爆・ミサイルキャンペーン
  - Grok AIがProject MavenでAI支援目標特定に配備
  - 96時間で2,000発発射、1日に数百件の攻撃を調整
  - 50,000人以上の米軍部隊展開
  - ペンタゴンは民間人被害の報告を認識・認める
- **引用URL:** https://www.the-independent.com/news/world/americas/us-politics/elon-musk-grok-ai-iran-missiles-pentagon-b2997321.html
- **Evidence ID:** EVD-20260620-0006

### INFO-007
- **タイトル:** 米軍調査: イラン・ミナブの女子校攻撃で少なくとも175人死亡、米軍の関与が濃厚
- **ソース:** The Independent
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001
- **関連企業:** 米軍, xAI
- **要約:** 米軍調査官が、イラン・ミナブの女子校に対する攻撃（少なくとも175人死亡）で米軍の関与が濃厚と判断。Operation Epic FuryにおけるAI支援目標特定に関連する民間人被害の具体例。
- **キーファクト:**
  - ミナブの女子校攻撃: 少なくとも175人死亡
  - 米軍の関与が「likely（濃厚）」と判断
  - AI支援目標特定に関連する可能性のある民間被害の文書化事例
- **引用URL:** https://www.the-independent.com/news/world/americas/us-politics/elon-musk-grok-ai-iran-missiles-pentagon-b2997321.html
- **Evidence ID:** EVD-20260620-0007

### INFO-008
- **タイトル:** ペンタゴンがAI企業にガードレール除去を金曜期限で要求、軍事利用禁止条項の撤去
- **ソース:** Fox 8 News / AOL
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06
- **関連企業:** xAI, 米国防総省
- **要約:** ペンタゴンがAI企業に対し、米軍のAI利用を妨げるガードレール（安全条項）を除去するよう金曜午後5時までの期限で要求。「非常に強力なAI技術を常識的なガードレールなしに配備すれば壊滅的結果になり得る」との懸念。
- **キーファクト:**
  - ペンタゴンがAI企業に軍事利用防止ガードレールの除去を期限付き要求
  - Grokとペンタゴンの契約: 全「合法な政府目的」(情報分析・戦略計画等)でクリア
  - 「ガードレールなき強力なAI配備＝壊滅的結果」の警告
- **引用URL:** https://www.aol.com/articles/pentagon-ai-chief-musk-grok-162254167.html
- **Evidence ID:** EVD-20260620-0008

### INFO-009
- **タイトル:** 上院議員Mark Kelly、国防授权法案にAI kill chainへの人間の「究極の権限」確保条項を追加
- **ソース:** Cronkite News (AZPBS)
- **公開日:** 2026-06-15
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06
- **関連企業:** 米議会
- **要約:** Mark Kelly上院議員が年次国防権限法案に、致死性武力の行使に人間が権限を保持することを保証する条項を追加。軍事AI利用の拡大に対応する立法的ガードレール。Gillibrand法案（Arbiter参照）と並ぶ議会レベルの対応。
- **キーファクト:**
  - Mark Kelly修正条項: 致死性武力行使への人間の権限確保
  - 年次国防権限法案（NDAA）に組み込み
  - 軍事でのAIモデル利用拡大への立法対応
- **引用URL:** https://cronkitenews.azpbs.org/2026/06/15/mark-kelly-amendment-defense-bill-ai-powered-kill-chain
- **Evidence ID:** EVD-20260620-0009

### INFO-010
- **タイトル:** Human Rights Watch、Operation Epic FuryでPalantir AIを含む複数AIの軍事依存を指摘
- **ソース:** Human Rights Watch
- **公開日:** 2026-06-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001
- **関連企業:** Palantir, xAI, 米軍
- **要約:** HRW報告: Operation Epic Fury（2月28日開始の対イランキャンペーン）で米軍はPalantirのAIを含む複数システムに依存。致死性自律兵器システムのリスクを協議中。AIの軍事領域での利用拡大への国際的懸念。
- **キーファクト:**
  - Operation Epic FuryでPalantir AIへの依存報告
  - 致死性自律兵器システム(LAWS)のリスク協議中
  - 複数AI企業が軍事キルチェーンに統合
- **引用URL:** https://www.hrw.org/news/2026/06/14/addressing-artificial-intelligence-in-the-military-domain
- **Evidence ID:** EVD-20260620-0010

## KIQ-GOV-002（動的追加: 順応企業の政府契約ガードレール条項の定量比較）

### INFO-011
- **タイトル:** OpenAI・Googleも国防AI契約（各約$200M+）に参加、軍事利用を広く許容する条項
- **ソース:** Instagram/LinkedIn報道引用
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-GOV-002, KIQ-002-06
- **関連企業:** OpenAI, Google, xAI
- **要約:** OpenAIとGoogleも国防AI契約（各最大約$200M+）の一部であり、軍事利用を広く許容する条項を含む。ただし安全性条項の正確な度合いは異なる。全AI企業が「ガードレールを除去するか政府契約を失うか」の選択に直面しているとの指摘。
- **キーファクト:**
  - OpenAI/Google: 国防AI契約各最大約$200M+
  - 契約条項は軍事利用を広く許容
  - ペンタゴンが$200M契約を授与
  - 「ガードレール除去か契約喪失か」の二択構造
- **引用URL:** https://www.linkedin.com/posts/lyndal-lane_if-you-have-ever-built-a-workflow-automation-activity-7472030312940613632-opwQ
- **Evidence ID:** EVD-20260620-0011

## KIQ-OAI-001（動的追加: OpenAI収益内訳 API/Enterprise/Consumer）

### INFO-012
- **タイトル:** OpenAI Q1 2026収益$57億・現金バーン$37億、2026年$240億年率目標
- **ソース:** Gradually AI / Softonic / Quartz
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001, KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIのQ1 2026収益は$57億（年率$240億ペース）だが、現金バーンは$37億。有料ユーザー5,000万人（うち企業900万人）。収益源は開発者/企業のAPI利用＋消費者・企業製品の急拡大。IPO準備中だが損失拡大。市場シェアは50%割れ。
- **キーファクト:**
  - Q1 2026収益: $57億、現金バーン$37億
  - 2026年$240億年率、2027年目標$294億
  - 有料ユーザー5,000万人（企業900万人）
  - 収益源: API（開発者/企業）+ Consumer + Enterprise製品
  - 2025年純損失$390億予想、IPO準備
  - 市場シェア50%割れ
- **引用URL:** https://www.gradually.ai/en/openai-statistics/
- **Evidence ID:** EVD-20260620-0012

## KIQ-BTD-001（動的追加: 豆包ARPU・有料コンバージョン率）

### INFO-013
- **タイトル:** QuestMobile: 豆包APP 1.47億MAU・抖音APP 3.3億、EC占81.1%
- **ソース:** 36kr (QuestMobile 2026 AI E-commerce)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-BTD-001, KIQ-002-05
- **関連企業:** ByteDance
- **要約:** QuestMobile 2026 AI EC調査: 豆包APP MAU 1.47億、抖音APP 3.3億。収益化価値のうちECが最大81.1%を占め、豆包の直接収益だけでなく抖音シナジー・EC手数料が収益化の主力。
- **キーファクト:**
  - 豆包APP MAU: 1.47億
  - 抖音APP MAU: 3.3億
  - 収益化の81.1%がEC経由（豆包直接収益以外の収益化が主力）
  - Arbiter v4.11の操作化再定義（Freemium維持）を支持するデータ
- **引用URL:** https://eu.36kr.com/en/p/3855204672574728
- **Evidence ID:** EVD-20260620-0013

## KIQ-GOV-001（動的追加: 連邦裁判所予備的差止・次政権AI政策）

### INFO-014
- **タイトル:** 連邦判事がAnthropic側に予備的差止を認可、政府措置を「Orwellian」と評（Anthropic PBC v. 米国国防省）
- **ソース:** FutureSearch / Nextgov
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-GOV-001, KIQ-002-06
- **関連企業:** Anthropic, 米国政府
- **要約:** Anthropicが米政府を提訴し、連邦判事が予備的差止を認可。判事は政府のFable 5/Mythos 5アクセス停止措置を「Orwellian（オーウェル的）」と評した（Anthropic PBC v. U.S. Department of War）。H-GOV-001の60%移行判断の核心材料。
- **キーファクト:**
  - Anthropicが提訴、連邦判事が予備的差止認可
  - 判事が政府措置を「Orwellian」と評
  - 事件名: Anthropic PBC v. U.S. Department of War
  - 法的帰趗がH-GOV-001確度60%移行の決定要因
- **引用URL:** https://futuresearch.ai/claude-fable-ban-forecast/
- **Evidence ID:** EVD-20260620-0014

## KIQ-001-01: 各社のAgent SDK/APIの機能拡張ロードマップはどうなっているか？

### INFO-015
- **タイトル:** Anthropic、Claude Agent SDKのサブスクリプション変更（6月15日別クレジット分離）を公開当日に一時停止
- **ソース:** The New Stack / Reddit / Helply
- **公開日:** 2026-06-15
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Anthropicが5月13日に、自動化Agent SDK利用を6月15日から別の月次クレジットに移行すると発表したが、公開当日に一時停止。現在は変更なし。サブスクリプション上のプログラム的/非対話的利用を通常制限と分離する計画が開発者反発で保留。
- **キーファクト:**
  - 6月15日変更を「pausing」: Agent SDK/claude -p利用は従来通り
  - 計画: 月次Agent SDKクレジットへ分離（プログラム的利用と通常サブスク分離）
  - 開発者コミュニティの混乱と反発で一時停止
- **引用URL:** https://thenewstack.io/anthropic-pauses-claude-agent-sdk-subscription-change/
- **Evidence ID:** EVD-20260620-0015

### INFO-016
- **タイトル:** xAI、Grok BuildにAgent DashboardとVoice Agent APIを追加、Agent Client Protocol対応
- **ソース:** xAI Docs / x.ai公式
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIがGrok Build（拡張可能なコーディングagent）にAgent Dashboardを追加し、全セッションを1画面で並列実行・介入可能に。Grok Voice Agent API（ツール設定可能な音声agent）も提供。Agent Client Protocol経由でヘッドレス実行対応。
- **キーファクト:**
  - Agent Dashboard: 全Grok Buildセッションを1画面、並列実行・必要時のみ介入
  - Grok Build: TUI・ヘッドレス・Agent Client Protocol経由で動作
  - Voice Agent API: ツール設定可能な音声agent
  - Grok 4でLLMがAPIからプラットフォームネイティブなマルチagent推論システムへ
- **引用URL:** https://x.ai/news/agent-dashboard
- **Evidence ID:** EVD-20260620-0016

### INFO-017
- **タイトル:** Google、Gemini Enterprise Agent Platformとgemini-skills公開、1Mコンテキストのagent API
- **ソース:** Google Cloud Docs / GitHub
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Google
- **要約:** GoogleがGemini Enterprise Agent Platform（APIキー認証・Agent Platform APIでリソース管理）とgemini-skills（Interactions API・関数呼び出し・構造化出力・画像生成をカバー）を公開。第2世代ワークホースモデルは1Mトークンコンテキスト・ネイティブツール使用。
- **キーファクト:**
  - Gemini Enterprise Agent Platform: APIキー認証・Agent Platform API
  - gemini-skills: Interactions API・関数呼び出し・構造化出力・画像生成
  - 第2世代モデル: 1Mトークンコンテキスト・ネイティブツール使用・高速
  - Firebase AI Logic SDKでGemini API直接呼び出し
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest
- **Evidence ID:** EVD-20260620-0017

### INFO-018
- **タイトル:** OpenAI Agents SDKがMCP統合完全対応、Responses APIで高度agent構築
- **ソース:** Composio / OpenAI Developers
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKがMCP統合を完全サポート（構造化ツール呼び出し・メッセージ履歴・モデルオーケストレーション）。新Responses APIで高速Web検索・文書スキャン・カスタムagent構築。Apps SDKで接続アプリの権限管理（常に/変更前/重要変更前）。
- **キーファクト:**
  - Agents SDK: MCP完全統合・構造化ツール呼び出し
  - Responses API: 高速Web検索・文書スキャン
  - Apps SDK: 接続アプリ権限を常に/変更前/重要変更前で選択
  - LangGraph/CrewAI比較で「分で構築できるが天井が早い」評価
- **引用URL:** https://composio.dev/toolkits/share_point/framework/open-ai-agents-sdk
- **Evidence ID:** EVD-20260620-0018

### INFO-019
- **タイトル:** 2026年のAI agentフレームワーク群雄: LangGraph/OpenAI Agents SDK/CrewAI/AutoGen/Google ADK等
- **ソース:** Atlan / Substack / Truefoundry
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** 複数
- **要約:** 2026年のagent FW景観はLangGraph・OpenAI Agents SDK・CrewAI・AutoGen・Microsoft Agent Framework・Google ADK・Pydantic AI・Smol Agents・Mastra・Vercel AI SDK等が乱立。エンタープライズ選定は5大手(LangGraph/CrewAI/MS/Google ADK/OpenAI)の評価が必要。
- **キーファクト:**
  - 主要FW: LangGraph, OpenAI Agents SDK, CrewAI, AutoGen, MS Agent Framework, Google ADK
  - エンタープライズ選定5大局: 上記+比較軸
  - 標準化(MCP)進行とFW乱立の同時進行
- **引用URL:** https://atlan.com/know/ai-agent/how-to-choose-agentic-framework-enterprise/
- **Evidence ID:** EVD-20260620-0019

### INFO-020
- **タイトル:** GitHub AI agent危機: 2026年5月に9件・4月に10件のサービス低下障害
- **ソース:** Waxell
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** GitHub (Microsoft)
- **要約:** GitHubが2026年5月に9件、4月に10件のサービス低下インシデントを記録。AI agent基盤のSLA/安定性問題を浮き彫り。Arbiter v4.13のIND-013「GitHub月19件障害」を補強。
- **キーファクト:**
  - 2026年5月: 9件のサービス低下インシデント
  - 2026年4月: 10件
  - agent基盤のSLA/信頼性への構造的懸念
- **引用URL:** https://www.waxell.ai/blog/github-ai-agent-crisis-infrastructure-enforcement-2026
- **Evidence ID:** EVD-20260620-0020

## KIQ-001-02: 各社のAgent製品のエンタープライズ向け展開（セキュリティ認証、SLA、専用サポート）の進捗は？

### INFO-021
- **タイトル:** ChatGPT Enterprise vs Claude Enterprise比較: FedRAMP対応はAzure経由が優位
- **ソース:** IntuitionLabs
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI, Anthropic, Microsoft
- **要約:** ChatGPT Enterpriseは標準的エンタープライズセキュリティ要件を満たすが、FedRAMP対応デプロイはMicrosoft Azure経由が限定的優位。Claude Enterpriseとの機能マトリクス比較。Okta等がOWASP Top 10 for Agentic Applications・HIPAA・FedRAMP・SOC2へのアライメントを掲げAI agentセキュリティ人材を募集。
- **キーファクト:**
  - ChatGPT Enterprise: 標準エンタープライズセキュリティ要件対応
  - FedRAMP対応: Azure経由が限定的優位（OpenAI直接は制限的）
  - OWASP Top 10 for Agentic Applications登場（agent特化セキュリティ基準）
  - SOC2/HIPAA/FedRAMPへの需要拡大
- **引用URL:** https://intuitionlabs.ai/articles/chatgpt-vs-claude-enterprise-comparison
- **Evidence ID:** EVD-20260620-0021

### INFO-022
- **タイトル:** Google Cloud、Gemini Enterprise Agent Platformで非技術者向けagent構築＋スタートアップに$350kクレジット
- **ソース:** Google Cloud / Facebook
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google
- **要約:** Gemini Enterpriseは非技術従業員がカスタムAI agentを構築・デプロイ・管理できるオールインワンプラットフォーム。Vertex AI Agent Engineでスタートアップに$350kクレジット提供。Fetcherrが同プラットフォーム+BigQueryで市場構築事例。ただしクラウド依存agentは遅延・コスト変動で本番SLA維持が困難との指摘。
- **キーファクト:**
  - Gemini Enterprise: 非技術者向けagent構築プラットフォーム
  - Vertex AI Agent Engine: スタートアップ$350kクレジット
  - Fetcherr事例: BigQuery統合で市場構築
  - 課題: クラウド依存agentの遅延変動・コスト急騰で本番SLA困難
- **引用URL:** https://www.facebook.com/googlecloud/posts/fetcherr-used-gemini-enterprise-agent-platform-and-bigquery-to-build-the-market-/
- **Evidence ID:** EVD-20260620-0022

### INFO-023
- **タイトル:** Microsoft Dynamics 365にAI agent統合が最大の変化、ワークフロー自動化・意思決定支援を実行
- **ソース:** Reddit (r/Dynamics365)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Microsoft
- **要約:** Microsoft Dynamics 365へのAI agent統合が同製品最大の変化と評価。agentはデータ分析・ワークフロー自動化・レポート生成・ルーティンタスク処理・意思決定支援まで実行可能。エンタープライズSaaSへのagent組み込み加速。
- **キーファクト:**
  - Dynamics 365: AI agent統合が史上最大の変化
  - agent実行領域: データ分析・自動化・レポート・意思決定支援
  - エンタープライズSaaSへのagent組み込み加速
- **引用URL:** https://www.reddit.com/r/Dynamics365/comments/1u3lwgv/are_ai_agents_the_biggest_change_to_microsoft/
- **Evidence ID:** EVD-20260620-0023

## KIQ-001-03: 各社のAgent開発者エコシステム（サードパーティ連携、マーケットプレイス）の拡大状況は？

### INFO-024
- **タイトル:** AAIF（Agentic AI Foundation）170社到達、43新規メンバー追加・AGENTS.mdをオープン標準化
- **ソース:** AAIF公式 / Beam AI
- **公開日:** 2026-05-18
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-003-05
- **関連企業:** Anthropic, OpenAI, Google, AWS, Microsoft（共同設立）
- **要約:** AAIFが170社到達（5月18日に43新規メンバー追加）。Anthropic/OpenAI/Google/AWS/Microsoftが共同設立。2025年12月にAGENTS.mdをツール非依存オープン標準として採用。MCP・Goose・AGENTS.md・agentgatewayを推進。中立的ガバナンスでアジェンティック技術採用加速。
- **キーファクト:**
  - 170社到達（43新規: 5月18日）
  - 共同設立5社: Anthropic/OpenAI/Google/AWS/Microsoft
  - AGENTS.md: 2025年12月オープン標準化
  - 推進標準: MCP, Goose, AGENTS.md, agentgateway
  - 中立的ガバナンス体制確立
- **引用URL:** https://beam.ai/ar/agentic-insights/aaif-agentic-ai-foundation-170-members-enterprise-adoption
- **Evidence ID:** EVD-20260620-0024

### INFO-025
- **タイトル:** MCP採用拡大: Google Gemini Enterprise・AWS MCP Gateway・MDN公式MCP server
- **ソース:** Google Cloud / AWS / MDN
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-003-05
- **関連企業:** Google, AWS, Mozilla (MDN)
- **要約:** MCP標準の採用が加速。Google Gemini Enterprise Agent PlatformがリモートMCP server提供、AWSがMCP Gateway & RegistryでAI資産ガバナンス、MDNが公式MCP server公開（ドキュメント・ブラウザ互換データをagent/IDEに直接統合）。Arbiter v4.13「MCP月間1.1億DL」を補強するプラットフォーム層統合。
- **キーファクト:**
  - Google Gemini Enterprise: リモートMCP server提供
  - AWS MCP Gateway & Registry: 3カテゴリAI資産(MCP server含む)ガバナンス
  - MDN公式MCP server: ドキュメント・互換性データをagent/IDEへ
  - MCPがプロトコル層デファクト標準として定着
- **引用URL:** https://aws.amazon.com/blogs/opensource/governing-ai-assets-at-scale-with-mcp-gateway-and-registry/
- **Evidence ID:** EVD-20260620-0025

### INFO-026
- **タイトル:** Salesforce×Databricks提携: AI agentが信頼できるデータを信頼できる行動へ変換
- **ソース:** Salesforce公式
- **公開日:** 2026-06-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** Salesforce, Databricks
- **要約:** SalesforceとDatabricksが提携拡大。AI agentが信頼できるデータを行動に変換する基盤構築。エンタープライズデータレイク×agent連携の標準化。
- **キーファクト:**
  - Salesforce×Databricks提携拡大（6月16日）
  - データ→行動変換のagent基盤
  - エンタープライズデータレイク統合
- **引用URL:** https://www.salesforce.com/news/stories/salesforce-databricks-shared-foundation-of-human-agent-work-announcement/
- **Evidence ID:** EVD-20260620-0026

### INFO-027
- **タイトル:** Yahoo DSPがAgent Network開設、広告主とAI agent直接接続のオープン枠組み
- **ソース:** Yahoo Inc.
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-05
- **関連企業:** Yahoo
- **要約:** Yahoo DSPがAgent Networkを開設。広告主と主要テクノロジーパートナーのAI agentを直接接続するオープン枠組み。広告業界へのagent統合の新チャネル。
- **キーファクト:**
  - Yahoo DSP Agent Network開設
  - 広告主とAI agentの直接接続オープン枠組み
  - 広告業界へのagent統合チャネル新設
- **引用URL:** https://www.yahooinc.com/press/yahoo-dsp-launches-agent-network-opening-the-ai-ecosystem-for-advertisers
- **Evidence ID:** EVD-20260620-0027

### INFO-028
- **タイトル:** Zendeskがメール向けアジェンティックAI agentをGA、完全生成AI駆動
- **ソース:** Zendesk Support
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-04
- **関連企業:** Zendesk
- **要約:** ZendeskがアドバンスドメールAI agent向けアジェンティックAIを一般提供(GA)開始。完全生成AI駆動でメールAI agentが自律処理。カスタマーサポート領域のagent自律化進展。
- **キーファクト:**
  - メールAI agent向けアジェンティックAI GA
  - 完全生成AI駆動・自律処理
  - CS領域のagent自律化事例
- **引用URL:** https://support.zendesk.com/hc/en-us/articles/10563281043738-Announcing-agentic-AI-for-advanced-email-AI-agents
- **Evidence ID:** EVD-20260620-0028

## KIQ-001-04: 各社のマルチモーダルAgent（音声・視覚・コード実行）統合の進捗は？

### INFO-029
- **タイトル:** 音声agentオーケストレーション標準化: STT→LLM→TTSのミリ秒パイプライン＋3統合パターン
- **ソース:** AssemblyAI / DeepLearning.AI
- **公開日:** 2026-06-16
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04
- **関連企業:** 複数（Vocal Bridge等）
- **要約:** 音声AI agentはSTT→LLM→TTSの3部構成ミリ秒パイプラインをオーケストレーション層で実行。DeepLearning.AI新コースで3統合パターン（組込音声・既存agentへの音声レイヤー・呼出可能ツールとしての音声）を提示。マルチモーダルagentへの音声統合がコード書き換え不要に。
- **キーファクト:**
  - 音声agent 3部パイプライン: STT→LLM→TTS（ミリ秒実行）
  - 3統合パターン: 組込/レイヤー/ツールとしての音声
  - ノーコードオムニチャネルagent builder（音声・チャット・メール統合）
- **引用URL:** https://www.assemblyai.com/blog/orchestration-tools-ai-voice-agents
- **Evidence ID:** EVD-20260620-0029

### INFO-030
- **タイトル:** NVIDIA XR AI: ARグラス・XRデバイス向けインテリジェントagent構築、視覚グラウンディング統合
- **ソース:** NVIDIA Developer
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** NVIDIA
- **要約:** NVIDIAがXR AIでARグラス・XRデバイス向けインテリジェントagent構築を支援。視覚グラウンディング（NVIDIA技術）を組み合わせたマルチモーダル物理世界agent。空間コンピューティング×agent統合。
- **キーファクト:**
  - XR AI: ARグラス/XRデバイス向けagent構築
  - 視覚グラウンディング統合
  - 空間コンピューティング×マルチモーダルagent
- **引用URL:** https://developer.nvidia.com/blog/building-ai-agents-for-ar-glasses-and-xr-devices-with-nvidia-xr-ai/
- **Evidence ID:** EVD-20260620-0030

### INFO-031
- **タイトル:** オムニモーダル長時間動画推論ベンチマーク: Gemini 3.1 Pro Preview 55.63%が最高・全モデルに大幅改善余地
- **ソース:** arXiv
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google / DeepMind
- **要約:** オムニモーダル長時間動画推論ベンチマークで、最強のクローズドソースGemini 3.1 Pro Previewが55.63%に留まり、全システムに substantial な改善余地。「真の理解」未解決を示す定量データ。Arbiter v4.13 IND-025と整合。
- **キーファクト:**
  - Gemini 3.1 Pro Preview: 55.63%（クローズド最高）
  - 全モデルに substantial headroom（改善余地）
  - オムニモーダル長時間動画推論の限界を示す定量化
- **引用URL:** https://arxiv.org/html/2512.16978v2
- **Evidence ID:** EVD-20260620-0031

### INFO-032
- **タイトル:** MLPerf Training v6.0: 初のアジェンティックAIインフラベンチマーク導入・MoE新ベンチマーク2件
- **ソース:** MLCommons / NVIDIA
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** MLCommons, NVIDIA, 複数
- **要約:** MLCommonsがMLPerf Training v6.0結果公開。初のアジェンティックAIインフラベンチマーク（1agentが数十タスクを連鎖）とMoE新ベンチマーク2件導入。24組織・13ハードウェアアクセラレータから95システム。Arbiter v4.13「初エージェント型」を確認。
- **キーファクト:**
  - 初のアジェンティックAIインフラベンチマーク導入
  - MoE新ベンチマーク2件
  - 24組織・13アクセラレータ・95システム
  - agentが数十タスクを連鎖する性能評価
- **引用URL:** https://mlcommons.org/2026/06/mlperf-training-v6-0-results/
- **Evidence ID:** EVD-20260620-0032

## KIQ-001-05: 各社の「スキル配布と実行環境」はどう設計され、ロックインをどこで作っているか？

### INFO-033
- **タイトル:** NVIDIA OpenShell: 自律AI agent向けセキュア・プライベートサンドボックス実行ランタイム（OSS）
- **ソース:** GitHub (NVIDIA/OpenShell)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** NVIDIA
- **要約:** NVIDIAがOpenShell（自律AI agent向けセキュア・プライベートランタイム）をOSS公開。データ・資格情報・システムを保護するサンドボックス実行環境を提供。実行環境層のオープン化で囲い込みに対抗。Arbiter v4.13「OpenShell OSS」確認。
- **キーファクト:**
  - OpenShell: 自律agent向けセキュア・プライベートランタイム
  - サンドボックス実行でデータ/資格/システム保護
  - OSS公開で実行環境層のオープン化
- **引用URL:** https://github.com/NVIDIA/OpenShell
- **Evidence ID:** EVD-20260620-0033

### INFO-034
- **タイトル:** agentスキルマーケットプレイス乱立: VoltAgent/Awesome Claude Skills/Promptfoo、価格は無料〜$200/月
- **ソース:** GitHub / remoteopenclaw / Promptfoo
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** 複数
- **要約:** agentスキルのキュレーション・マーケットプレイスが乱立（VoltAgent awesome-agent-skills・Awesome Claude Skills・Promptfoo red-team skills等）。価格はOSS自己ホスト無料〜$200/月以上。スキル配布層の標準化未成熟で分散競争。
- **キーファクト:**
  - 主要ディレクトリ: VoltAgent, Awesome Claude Skills, Promptfoo
  - 価格帯: OSS無料〜$200+/月
  - スキル配布層は標準化未成熟・分散競争
- **引用URL:** https://www.remoteopenclaw.com/blog/ai-agent-pricing-compared-2026
- **Evidence ID:** EVD-20260620-0034

### INFO-035
- **タイトル:** アジェンティックcommerceのロックイン研究: 早期委託決定が不可逆化、カード決済/ステーブルコイン
- **ソース:** ResearchGate
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** 複数
- **要約:** 研究論文: AI agentが消費者の資金を支出するアジェンティックcommerceで、スイッチングコストが早期の委託決定を不可逆化しロックインを創出。カード決済レール・ステーブルコインが決済インフラ。消費者レベルの囲い込みメカニズム。
- **キーファクト:**
  - アジェンティックcommerce: 早期委託決定の不可逆化でロックイン
  - 決済インフラ: カードレール・ステーブルコイン
  - 消費者レベルのスイッチングコスト創出
- **引用URL:** https://www.researchgate.net/publication/407138018_When_AI_Agents_Spend_Your_Money_Card_Rails_Stablecoins_and_the_Coming_Lock-In_of_Agentic_Commerce
- **Evidence ID:** EVD-20260620-0035

### INFO-036
- **タイトル:** アジェンティックAIがERPベンダーロックインメカニズム化、製造業選定に影響
- **ソース:** Kai Waehner Blog
- **公開日:** 2026-06-15
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** 複数（ERPベンダー）
- **要約:** アジェンティックAIがERP（製造業）ベンダーロックインの新メカニズムとして機能。ベンダーブリーフィング以上の鋭い分析が必要。クラウドエグレス費用がエンタープライズクラウド請求の10-15%を消費（Gartner）。
- **キーファクト:**
  - アジェンティックAI = ERPロックイン新メカニズム
  - エグレス費用: クラウド請求の10-15%（Gartner）
  - ベンダーロックイン6カテゴリの費用
- **引用URL:** https://www.kai-waehner.de/blog/2026/06/15/choosing-an-erp-for-manufacturing-how-ai-is-reshaping-the-vendor-landscape/
- **Evidence ID:** EVD-20260620-0036

## KIQ-002-01: 主要クラウドプロバイダー（AWS, Azure, GCP）のAI Agent統合状況はどうか？

### INFO-037
- **タイトル:** AWS Bedrock AgentCore大幅アップグレード: SharePoint/Drive/S3横断推論＋Web検索ツール
- **ソース:** AWS News Blog / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** Amazon / AWS
- **要約:** AWSがBedrock AgentCoreの全agentに大幅アップグレード。SharePoint・Drive・S3のエンタープライズ知識を横断して推論可能に。Web Search on Bedrock AgentCore（引用付きWeb知識で根拠化、ゼロ設定）を新ツールとして導入。会話型agentビルダー・ナレッジベース権限管理強化。
- **キーファクト:**
  - 全agentがSharePoint/Drive/S3横断推論に対応
  - Web Search on AgentCore: 引用付き・ゼロ設定
  - 会話型agentビルダー・KB権限(IAM)管理
- **引用URL:** https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/
- **Evidence ID:** EVD-20260620-0037

### INFO-038
- **タイトル:** Azure AI Foundry Agent Service + Copilot Studio: ホステッドagent・ERP/CRM統合・MCP相互運用
- **ソース:** Microsoft Learn / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-03
- **関連企業:** Microsoft
- **要約:** Azure AI Foundry Agent Serviceでagent構築・管理、Azure API Managementをセキュアゲートウェイに。ホステッドagent（プレビュー）でコンテナ化agentの管理ホスティング・スケーリング・観測性。Copilot Studio vs Foundryの使い分け（検索/タスクagent・Azure AI Search統合）。ERP/CRM/文書リポジトリ統合。MCP相互運用性。
- **キーファクト:**
  - Foundry Agent Service + Azure API Management ゲートウェイ
  - ホステッドagent（preview）: コンテナ化・スケーリング・観測性
  - Copilot Studio: 検索/タスクagent・Azure AI Search統合
  - ERP/CRM/KB統合・MCP相互運用
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents
- **Evidence ID:** EVD-20260620-0038

### INFO-039
- **タイトル:** Google Cloud Vertex AI Agent Builder: Antigravity→AI Studio→本番agentのフルパイプライン
- **ソース:** Google Cloud Docs / thebestblogever
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Google
- **要約:** Vertex AI Agent Builderでagent構築・スケール・ガバナンス。Antigravity（vibeコーディング）→AI Studio→Vertex AI Agent Builder→Cloud Runで本番デプロイのフルパイプライン。Google Cloudがスタートアップ向け本番グレードagent技術ガイド公開。
- **キーファクト:**
  - Vertex AI Agent Builder: 構築/スケール/ガバナンススイート
  - Antigravity→AI Studio→Vertex→Cloud Run パイプライン
  - スタートアップ向け本番グレードagent技術ガイド
- **引用URL:** https://docs.cloud.google.com/agent-builder
- **Evidence ID:** EVD-20260620-0039

### INFO-040
- **タイトル:** AI agent構築コスト格差: DIY無料(ChatGPT+Zapier) vs 代理店$5-25K(12週) vs エンタープライズ$25K+
- **ソース:** Reddit (r/AI_Agents)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-01, KIQ-002-02
- **関連企業:** 複数
- **要約:** AI agent構築の価格格差が顕著化。DIY(ChatGPT+Zapier)は無料、代理店はマルチagentセットアップ$5-25K（12週）、エンタープライズは$25K+。同一機能で価格が3層に分断。Arbiter v4.13「96%ROI vs CX74%ロールバック矛盾」のコスト側面。
- **キーファクト:**
  - DIY: ChatGPT+Zapier無料
  - 代理店: マルチagent $5-25K（12週）
  - エンタープライズ: $25K+
  - 同一機能で3層価格分断
- **引用URL:** https://www.reddit.com/r/AI_Agents/comments/1u6xnri/been_running_my_businesses_on_ai_agents_for/
- **Evidence ID:** EVD-20260620-0040

## KIQ-002-02: エンタープライズ顧客のAI Agent採用率と主要ユースケースは？

### INFO-041
- **タイトル:** Gartner: 17%組織がagent展開済・60%+が2年内展開計画、40%のプロジェクトは2027年にキャンセル予測
- **ソース:** LinkedIn (Greg Buzek) / Izertis
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** Gartner予測: 現在17%の組織のみがAI agent展開済だが、60%超が2年内展開を計画。同時に40%のアジェンティックAIプロジェクトが2027年までにキャンセルされると予測。50%の失敗が不十分なガバナンスと相互運用性問題に起因。Arbiter v4.13「Gartner 17%展開済60%+計画」を確認。
- **キーファクト:**
  - 展開済: 17%の組織
  - 2年内計画: 60%超
  - 2027年までに40%のプロジェクトキャンセル予測
  - 50%の失敗要因: ガバナンス・相互運用性不足
  - アジェンティックAIは2年連続#1戦略技術トレンド
- **引用URL:** https://www.linkedin.com/pulse/gartner-predicts-40-agentic-ai-projects-canceled-2027-greg-buzek-cnjwe
- **Evidence ID:** EVD-20260620-0041

### INFO-042
- **タイトル:** Gartner: 平均Fortune 500は2年以内に150,000 agent稼働・40%エンタープライズアプリがagent埋め込み(2026末)
- **ソース:** Instagram引用 / Gravitee
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-01
- **関連企業:** 複数（Fortune 500）
- **要約:** Gartner予測: 平均Fortune 500は2年以内に150,000 agentを稼働。2026年末までにエンタープライズアプリの40%がタスク特化AI agentを埋め込み。agentフリートは2025年12月から約2倍に拡大（Gravitee State of AI Agent Security 2026）。
- **キーファクト:**
  - Fortune 500平均: 2年以内に150,000 agent稼働
  - 2026末: エンタープライズアプリ40%がagent埋め込み
  - agentフリート: 2025年12月から約2倍
- **引用URL:** https://www.gravitee.io/state-of-ai-agent-security
- **Evidence ID:** EVD-20260620-0042

### INFO-043
- **タイトル:** 本番agentの静かな失敗: LangChain agentが2週間30%セッション失敗・$2,400損失で可視性ゼロ
- **ソース:** Reddit (r/SideProject)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** クライアント向けデプロイしたLangChain agentが2週間にわたり30%のセッションを静かに失敗し$2,400損失。トレース・コスト可視性ゼロ。観測性レイヤー不足が本番agentの隠れた失敗率を示す事例。Arbiter v4.13「期待-実態ギャップ」の生の証拠。
- **キーファクト:**
  - LangChain agent: 30%セッション静かな失敗（2週間）
  - $2,400損失・可視性ゼロ
  - 観測性不足で隠れた失敗率
- **引用URL:** https://www.reddit.com/r/SideProject/comments/1u6hf2b/i_built_an_observability_layer_for_ai_agents/
- **Evidence ID:** EVD-20260620-0043

## KIQ-002-03: 規制環境（EU AI Act、米国大統領令、中国AI規制）がエンタープライズAI採用にどう影響するか？

### INFO-044
- **タイトル:** EU AI Act: 高リスク・透明性義務が2026年8月2日施行（47日後）、AI Omnibusで単一枠組みへ
- **ソース:** Reddit (r/AI_Agents) / LinkedIn / Snowflake
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** EU AI Actの高リスク・透明性義務が2026年8月2日に施行対象（施行47日後）。欧州ユーザー向けagent構築に影響。新「AI Omnibus」は複数規制当局の競合ルールを解消し単一枠組み化。リスクティア別義務・罰金設定。
- **キーファクト:**
  - 高リスク・透明性義務: 2026年8月2日施行
  - AI Omnibus: 単一枠組み・規制競合解消
  - リスクティア（受容不可/高/有限/最小リスク）別義務
  - 欧州向けagent構築に直接影響
- **引用URL:** https://www.reddit.com/r/AI_Agents/comments/1u8betp/eu_ai_act_compliance_hits_in_47_days_heres_what/
- **Evidence ID:** EVD-20260620-0044

### INFO-045
- **タイトル:** 中国、AIと消費統合の17施策発表＋AI「技術バブル」投機を規制当局が取り締まり
- **ソース:** Reuters / CNBC
- **公開日:** 2026-06-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 中国政府, ByteDance（関連）
- **要約:** 中国商務部が家庭・企業全国でのAI統合強化17施策を発表（Reuters 6月18日）。同時に証券規制当局(CSRC)が技術テーマに乗じた「技術バブル」投機・AI株式選別を取り締まる方針。G7で中国がグローバルAI安全リーダーシップを主張。
- **キーファクト:**
  - 17施策: 家庭・企業でのAI統合促進
  - CSRC: AI技術バブル投機・株式選び取り締まり
  - 中国: G7でグローバルAI安全リーダーシップ主張
  - 2022年から有害コンテンツ/プライバシー/データセキュリティ規制の先駆
- **引用URL:** https://www.reuters.com/business/media-telecom/china-announces-measures-promote-ai-integration-with-consumption-2026-06-18/
- **Evidence ID:** EVD-20260620-0045

### INFO-046
- **タイトル:** エンタープライズAIセキュリティ「常時稼働」義務化: 2026年6月が規制リスク担当者の転換点
- **ソース:** Fifth Row
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** 2026年6月以降、エンタープライズAIセキュリティコンプライアンスは常時稼働・自動化された統制を要求。規制リスク担当者向けマンドレート・フレームワーク・プラットフォームソリューションが登場。
- **キーファクト:**
  - 常時稼働・自動化統制が2026年6月以降必須
  - 規制リスク担当者の転換点
  - ガバナンスフレームワーク需要拡大
- **引用URL:** https://www.fifthrow.com/blog/enterprise-ai-security-s-always-on-mandate-why-june-2026-changed-compliance-for-regulatory-risk-leaders-forever
- **Evidence ID:** EVD-20260620-0046

## KIQ-002-06: 政府・軍によるAI企業への経済的圧力（契約排除・制裁指定・調達禁止）はAI業界の安全性姿勢と開発方向性にどう影響しているか？

### INFO-047
- **タイトル:** Anthropic vs ペンタゴン: $200M契約で「制限なき全合法利用」要求に拒否・大量監視と自律兵器の2項目で拒絶
- **ソース:** Built In / Deutsche Welle / Boston Globe
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-002
- **関連企業:** Anthropic, 米国防総省
- **要約:** ペンタゴンと米国防総省がAnthropic（と競合AI企業）に$200M・2年契約を授与。ペンタゴンは「任意の合法利用・制限なし・フルアクセス」を要求。Anthropicは大量国内監視と完全自律兵器の2項目で合意を拒否し$200M契約から離脱。Dario Amodeiの安全性堅持姿勢。
- **キーファクト:**
  - 契約: $200M・2年（Anthropic+競合AI企業）
  - ペンタゴン要求: 「任意の合法利用」・制限なし・フルアクセス
  - Anthropic拒否2項目: 大量国内監視・完全自律兵器
  - Anthropicが$200M契約から離脱
- **引用URL:** https://builtin.com/articles/anthropic-pentagon-claude-dispute
- **Evidence ID:** EVD-20260620-0047

### INFO-048
- **タイトル:** トランプ政権、Anthropicを「サプライチェーンリスク」指定（外敵企業向け制度の転用）・全連邦使用停止命令
- **ソース:** CNN / Bloomberg / NYT Opinion / LinkedIn (LawSnap)
- **公開日:** 2026-06-13
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-001
- **関連企業:** Anthropic, 米国政府
- **要約:** トランプ政権が全米機関にAnthropic AI技術の使用停止を命令。「サプライチェーンリスク」指定を付与（通常は外国の敵対企業向け・国内企業への適用は前例なし）。Anthropicが安全性ガードレール除去を拒否したことへの報復。MicrosoftがAnthropicを支援しリスク指定阻止を試みる。Arbiter v4.13のH-GOV-001/002核心証拠。
- **キーファクト:**
  - 全連邦機関にAnthropic使用停止命令
  - 「サプライチェーンリスク」指定（通常は外敵企業向け・国内企業適用は前例なし）
  - 安全性ガードレール拒否への報復
  - MicrosoftがAnthropic支援・リスク指定阻止試み
  - 200+団体が軍事AI禁止を求める声明
- **引用URL:** https://www.cnn.com/2026/06/13/business/anthropic-mythos-model-national-security
- **Evidence ID:** EVD-20260620-0048

### INFO-049
- **タイトル:** 防衛生産法（DPA）発動でAI企業に国家安全保障目的でのサービス提供を強制・「殺人スイッチ」懸念
- **ソース:** Washington Post / Firstpost / Cairo Review / Eternally Radical Idea
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-001
- **関連企業:** Anthropic, 米国政府
- **要約:** 防衛生産法（1950年DPA）を発動しAI企業に国家安全保障目的でのサービス提供を実質強制。論説: 政府がAIシステムへの「殺人スイッチ」——政権の好みに反する・官僚を恥かせるモデルを抑圧する権力——を主張。2023年バイデンAI大統領令もDPA権限で強力な基盤モデル開発者に要件を課した前例。
- **キーファクト:**
  - DPA発動で国家保障目的のサービス提供を強制
  - 「殺人スイッチ」: 政権好みに反するモデル抑圧権力
  - 2023年バイデン令もDPA権限で基盤モデル開発者に要件
  - 国有化リスク議論（Washington/Beijing両者）
- **引用URL:** https://www.thecairoreview.com/essays/will-washington-and-beijing-nationalize-ai-labs/
- **Evidence ID:** EVD-20260620-0049

### INFO-050
- **タイトル:** OpenAI、Anthropic排除と同日にペンタゴンと「技術的セーフガード」付き契約締結（順応報酬構造）
- **ソース:** MSU Exponent / Washington Post
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, 米国防総省
- **要約:** トランプ政権がAnthropicのAIを禁止・「サプライチェーンリスク」指定した同日、OpenAIのSam Altmanがペンタゴンと「技術的セーフガード」付き（Anthropicと類似の赤線）で契約を発表。安全性堅持企業が罰せられ、順応企業が報われる構造（Pattern P-3）の具体化。
- **キーファクト:**
  - OpenAI: Anthropic排除同日にペンタゴン契約
  - 「技術的セーフガード」付き（Anthropicと類似の赤線）
  - 順応報酬構造: 安全性拒否企業が排除・順応企業が契約獲得
  - Pattern P-3「3社同時具体化」の核心事例
- **引用URL:** https://www.msuexponent.com/news/national/openai-strikes-pentagon-deal-with-safeguards-as-trump-dumps-anthropic/article_acb67662-ddc1-5f29-a07d-ed3298a6d057.html
- **Evidence ID:** EVD-20260620-0050

### INFO-051
- **タイトル:** Google、従業員反発を押し切りペンタゴンAI契約（機密作業）・150万国防職員が軍AI使用
- **ソース:** Reddit (r/technology) / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Google, 米国防総省
- **要約:** Googleが従業員の反発を押し切りペンタゴンAI契約締結（米軍が機密作業にGoogle AIモデル使用を許可）。150万国防省職員が軍のAIを使用中。OpenAI/GoogleとAnthropic排除の対比で「順応3社」構造を補強。
- **キーファクト:**
  - Google: 従業員反発を押し切りペンタゴン契約（機密作業許可）
  - 150万国防省職員が軍AI使用中
  - 順応企業陣営: OpenAI/Google（Anthropic排除との対比）
- **引用URL:** https://www.reddit.com/r/technology/comments/1u7vuwn/15_million_defense_department_workers_are_now/
- **Evidence ID:** EVD-20260620-0051

### INFO-052
- **タイトル:** xAI Grok、最大$200M契約で軍事システム統合・司法省ブリーフが確認
- **ソース:** Instagram / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** xAI, 米国防総省
- **要約:** ペンタゴンが最大$200M契約でElon MuskのxAI製Grokを軍事システムに統合すると発表。司法省(DoJ)ブリーフがxAIツールの軍事統合を確認。Operation Epic FuryでのGrok使用（INFO-006）と整合。安全性ガードレール最少の順応企業の軍事化事例。
- **キーファクト:**
  - xAI Grok: 最大$200M契約で軍事システム統合
  - 司法省ブリーフが軍事統合確認
  - Operation Epic Furyでの実戦使用と整合
  - ガードレール最少の順応企業軍事化
- **引用URL:** https://www.instagram.com/p/DZrgOjGmWo-/
- **Evidence ID:** EVD-20260620-0052

### INFO-053
- **タイトル:** 超党派下院議員団がトランプ政権に回答要求・DoD $97億Microsoft契約が異議申し立てで白紙
- **ソース:** Washington Post / Federal News Network
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-001
- **関連企業:** 米議会, Microsoft, 米国防総省
- **要約:** 超党派の下院議員団がトランプ政権のAnthropic排除措置に回答要求。併せて国防総省の$97億Microsoft製品契約がMinburn Technologyの異議申し立て（入札者への事前通知なしで募集要項変更＝競争契約法違反）で白紙化。政府AI調達の法的不確実性。
- **キーファクト:**
  - 超党派下院議員団が政権に回答要求
  - DoD $97億Microsoft契約が異議申し立てで白紙
  - 競争契約法違反の主張
  - 政府AI調達の法的不確実性
- **引用URL:** https://federalnewsnetwork.com/contractsawards/2026/06/dods-9-7b-award-for-microsoft-products-derailed-by-protest/
- **Evidence ID:** EVD-20260620-0053

## KIQ-002-04: AIエージェントによる業務自律化は、どの業界・職種で最も速く進んでいるか？

### INFO-054
- **タイトル:** Agent's Last Exam: AI agentが55職種1,500+タスクで完遂率<5%・人間+agentで最大70%向上
- **ソース:** The New Stack / HCAMag / Medium
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-005-01
- **関連企業:** 複数
- **要約:** Agent's Last Examベンチマーク: 55職種1,500+実世界タスクで最先端AI agentの完遂率は5%未満。だが専門人間とのペアリングで完遂率最大70%向上。METR計測でagentが50%信頼性で完了するタスクの時間ホライズンが約7ヶ月毎に倍増。Arbiter v4.13「ALE完遂<5%」確認。短期はagent置換ではなく人間+agent。
- **キーファクト:**
  - 完遂率<5%（55職種1,500+タスク）
  - 人間+agentで最大70%完遂率向上
  - METR: タスク時間ホライズン約7ヶ月毎に倍増
  - 短期レシピ: agent置換ではなく人間+agent
- **引用URL:** https://www.hcamag.com/ca/news/general/your-ai-agent-isnt-as-capable-as-you-think-research-finds/579144
- **Evidence ID:** EVD-20260620-0054

### INFO-055
- **タイトル:** Claude大規模利用ログ分析: 幅広いタスクで80%時間節約・KPMGは10年で$3兆生産性向上予測
- **ソース:** arXiv / Hymalaia (KPMG)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04
- **関連企業:** Anthropic, Meta, KPMG
- **要約:** arXiv研究が大規模Claude利用ログから直接生産性向上を推計、幅広いタスクで80%時間節約。KPMG予測: アジェンティックAIが向こう10年で$3兆の生産性向上を創出。Meta Business Agentは10X〜100X生産性を実証。ただしALE完遂<5%との矛盾（部分タスク効率化≠全タスク自律完遂）。
- **キーファクト:**
  - Claude利用ログ: 80%時間節約（幅広いタスク）
  - KPMG: 10年で$3兆生産性向上予測
  - Meta Business Agent: 10X-100X実証
  - 部分タスク効率化≠全タスク自律完遂の区別必要
- **引用URL:** https://arxiv.org/html/2606.07489v2
- **Evidence ID:** EVD-20260620-0055

### INFO-056
- **タイトル:** Klarnaが700人CSをAIで置換後に人間回帰（「訓練補助輪」）・Duolingoは請負業者削減
- **ソース:** Instagram / LinkedIn / Business Today
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaが2024年に700人CSをAIで置換しCEOが公に称賛したが、後に人間を回帰（「AIは仕事を全部奪ったのではなく訓練補助輪を奪った」）。Duolingoは請負労働者削減し人間のAI置換を停止。あるテックCEOは従業員の80%を解雇。AI効率化→18ヶ月以内に人員削減のパターン。
- **キーファクト:**
  - Klarna: 700人CS AI置換→人間回帰（補助輪比喩）
  - Duolingo: 請負業者削減・人間AI置換停止
  - テックCEO: 従業員80%解雇事例
  - AI効率化→18ヶ月以内人員削減のパターン
- **引用URL:** https://www.instagram.com/reel/DZpkANIozjZ/
- **Evidence ID:** EVD-20260620-0056

### INFO-057
- **タイトル:** HR領域のagent採用ギャップ: 65%企業が「AI agent使用」主張も<15%のみ真の自律agent展開
- **ソース:** Instagram (2024 Deote調査引用)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-04, KIQ-002-02
- **関連企業:** 複数
- **要約:** 2024 Deote調査: 大企業の65%がHRでAI agent使用を主張するが、真の自律agent展開は15%未満。主張と実態のギャップ。Arbiter v4.13「期待-実態ギャップ構造的パターン化」のHR領域具体例。
- **キーファクト:**
  - HR agent主張: 65%の大企業
  - 真の自律agent展開: <15%
  - 主張-実態ギャップ
- **引用URL:** https://www.instagram.com/reel/DZsRF-nuByg/
- **Evidence ID:** EVD-20260620-0057

## KIQ-002-05: プラットフォーマー（Meta/Google等）のAI統合は、中間事業者（広告代理店・SaaS等）のバリューチェーンをどの程度侵食しているか？

### INFO-058
- **タイトル:** McKinsey「アジェンティック広告経済」: 消費者が発見する方法変化で広告価値が何を見られ選ばれ買われるかを形作る企業へ移行
- **ソース:** McKinsey
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-05, KIQ-003-04
- **関連企業:** Google, Meta
- **要約:** McKinsey分析: AIが消費者の製品発見方法を変える中、広告価値は「何を見られ・選ばれ・購入されるかを形作れる企業」へ移行。Google/Meta優位を示唆。Arbiter v4.13 H-GOO-001のMcKinsey A-2証拠と一致。アテンション経済からアクション経済への転換。
- **キーファクト:**
  - 広告価値移行先: 視認/選択/購入を形作る企業
  - アテンション経済→アクション経済転換
  - Google/Meta優位示唆
- **引用URL:** https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-agentic-advertising-economy-from-attention-to-action
- **Evidence ID:** EVD-20260620-0058

### INFO-059
- **タイトル:** Google Ads・Meta Adsがマイクロ秒単位でAI販売/ターゲティング/配置、メディアバイヤーの非効率抑制へ
- **ソース:** exchange4media (Marketing AI Institute引用)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google, Meta
- **要約:** Google AdsとMeta Adsは「AIでマイクロ秒単位で広告を販売・ターゲット・配置」。AIはメディアバイヤーを置換しないが、メディアバイイングの非効率を抑制する。プラットフォーマーAIの自動化が代理店中間層の付加価値を圧縮。
- **キーファクト:**
  - Google/Meta Ads: マイクロ秒AI販売/ターゲティング/配置
  - メディアバイヤー置換ではなく非効率抑制
  - 代理店中間層付加価値圧縮
- **引用URL:** https://www.facebook.com/exchange4media/posts/ai-wont-replace-media-buyers-but-will-curb-media-buying-inefficiencies-rajkumar-/
- **Evidence ID:** EVD-20260620-0059

### INFO-060
- **タイトル:** アジェンティックAIが組織高さを圧縮: 下位職員減→中間管理職縮小・バリューチェーン中間層圧縮
- **ソース:** Instagram (Helena Chao) / Wipro
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** 複数
- **要約:** アジェンティックAIで下位レベル従業員が減少すると中間管理職要件が縮小し、組織全体の高さが圧縮。バリューチェーン中間層の圧縮が進行。スミルカーブ（半導体: Goldman Sachsが2026 DRAM需給ギャップ4.9%・15年最大）もAIで再構築。
- **キーファクト:**
  - 下位職員減→中間管理職縮小→組織高さ圧縮
  - バリューチェーン中間層圧縮
  - 半導体スミルカーブ再構築（DRAM需給ギャップ4.9%）
- **引用URL:** https://www.instagram.com/p/DZrs_XKGg2x/
- **Evidence ID:** EVD-20260620-0060

### INFO-061
- **タイトル:** Adweek: 「AIでコスト削減」はもはや差別化点でない・SaaS倍率圧縮リスク
- **ソース:** Adweek / Instagram
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05, KIQ-004-02
- **関連企業:** 広告代理店, SaaS企業
- **要約:** Adweek分析: 「AIでコスト削減」はもはや差別化点ではなくなった。AIは代理店運営を変えマージン改善・人員増なしの成長を可能に。ミッションクリティカルSaaS企業は停滞できず——AIがコードを書けばソフトウェアは死に、機能がコピーできればSaaS倍率は圧縮、copilot/agentがワークフローを自動化すれば。
- **キーファクト:**
  - 「AIコスト削減」は差別化点でない
  - 代理店マージン改善・人員増なし成長
  - SaaS倍率圧縮リスク（AIコード生成/機能コピー）
- **引用URL:** https://www.adweek.com/dealroom/dealroom-hidden-variable-killing-margins/
- **Evidence ID:** EVD-20260620-0061

## KIQ-003-01: 各社のAPI料金改定の頻度・方向性はどうなっているか？

### INFO-062
- **タイトル:** AnthropicがAgent SDKトークン課金変更を発効直前に一時停止、サブスク維持で開発者混乱
- **ソース:** Ars Technica
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Agent SDKのトークン課金変更を発効直前に突然一時停止。Agent SDKユーザーは従来通り継続利用可能に。課金変更の頻繁な改定・撤回が開発者エコシステムに混乱。INFO-015と同一事象の Ars Technica確認。
- **キーファクト:**
  - トークン課金変更を発効直前に一時停止
  - 従来利用継続可能
  - 課金改定の頻繁な改定/撤回で開発者混乱
- **引用URL:** https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk/
- **Evidence ID:** EVD-20260620-0062

### INFO-063
- **タイトル:** Claude API料金体系: Claude Max $100/月・API per-token・V4 Flash $0.14/M・V4 Pro $0.435/M
- **ソース:** CostGoat / Amnic / YouTube
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Claude API料金: Claude Maxは$100/月（5x/20xティア）。APIは月額無料・per-token。Claude Fable 5/Mythos 5/Opus 4.8/Sonnet 4.6/Haiku 4.5。代替エンドポイントで最大95%安価化可能（V4 Flash $0.14/M入力・V4 Pro $0.435/M）。
- **キーファクト:**
  - Claude Max: $100/月（5x/20xティア）
  - API: per-token・月額無料
  - モデル群: Fable 5, Mythos 5, Opus 4.8, Sonnet 4.6, Haiku 4.5
  - V4 Flash $0.14/M入力・V4 Pro $0.435/M
- **引用URL:** https://costgoat.com/pricing/claude-api
- **Evidence ID:** EVD-20260620-0063

### INFO-064
- **タイトル:** AIコスト急騰: サブスクが価格壁に衝突・企業は中国LLM/オープンソースへ予算シフト
- **ソース:** Tom's Hardware
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-03
- **関連企業:** 複数, ByteDance, DeepSeek
- **要約:** AIサブスク提供コストが企業にとって持続的に上昇。per-tokenコスト減少が使用量増に追いつかず。企業は予算を延ばすため中国LLM（ByteDance/DeepSeek）やオープンソースモデルへシフト。ArbiterのJevons paradox（トークン90%安価化で使用爆発）と整合。
- **キーファクト:**
  - サブスク提供コスト持続上昇
  - per-token減少が使用量増に追いつかず
  - 企業は中国LLM/オープンソースへ予算シフト
- **引用URL:** https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-costs-spike-as-subscriptions-hit-pricing-wall-firms-turn-towards-chinese-llms-open-source-models-to-extend-budget
- **Evidence ID:** EVD-20260620-0064

### INFO-065
- **タイトル:** LLMトークン支出指数が$1.67に下落（5月比-20%）・思考トークンが総出力コスト80%超
- **ソース:** LinkedIn (Charles-Henry Monchau) / Facebook (vibecodinglife)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01, KIQ-005-01
- **関連企業:** 複数
- **要約:** LLM Token Expenditure Indexが$1.67に下落（4月中旬以来最低・5月ピーク比20%下）。AI価格は崩壊中。だが同一クエリでモデルにより思考トークンが900%多く消費されるケースも。思考トークンが総出力コストの80%超を占める。per-token安価化≠総コスト安価化の罠。
- **キーファクト:**
  - LLM Token Expenditure Index: $1.67（5月比-20%）
  - 思考トークン: 総出力コストの80%超
  - 同一クエリでモデル間900%の思考トークン差
  - per-token安価化≠総コスト安価化
- **引用URL:** https://www.linkedin.com/posts/charles-henry-monchau-cfa-cmt-caia-4003096_the-price-of-ai-is-collapsing-the-llm-activity-7473060650609524736-YAzu
- **Evidence ID:** EVD-20260620-0065

## KIQ-003-02: 主要ベンチマーク（MMLU, HumanEval, GPQA等）における各社モデルの性能推移は？

### INFO-066
- **タイトル:** SWE-bench比較: Grok 4 75%・GPT-5.4 74.9%・Claude 74%+・Gemini 63.8%（コーディング）
- **ソース:** GuruSup / DianApps
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02, KIQ-004-02
- **関連企業:** xAI, OpenAI, Anthropic, Google
- **要約:** コーディングベンチマーク(SWE-bench)でGrok 4 75%・GPT-5.4 74.9%・Claude 74%+・Gemini 63.8%。2026年に「単一最良モデル」は存在せず、Claude Opus 4.8とGPT-5が推論/コード、Gemini 2.5がマルチモーダル/長文脈、Grok 4が特定領域でリード。
- **キーファクト:**
  - SWE-bench: Grok 4 75% > GPT-5.4 74.9% > Claude 74%+ > Gemini 63.8%
  - 単一最良モデルなし（領域別リード）
  - Claude Opus 4.8/GPT-5: 推論/コード、Gemini 2.5: マルチモーダル、Grok 4: 特定領域
- **引用URL:** https://gurusup.com/blog/grok-vs-chatgpt-claude-gemini
- **Evidence ID:** EVD-20260620-0066

### INFO-067
- **タイトル:** Artificial Analysis: Grok 4が知能指数73で#1・Claude Fable 5はSWFTE 100/100首位
- **ソース:** Facebook (Artificial Analysis引用) / swfte.com
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** xAI, Anthropic
- **要約:** Artificial AnalysisがGrok 4を知能指数73で「総合#1最知的モデル」と評価（$6/Mトークン）。swfte.comリーダーボードではClaude Fable 5が357+モデル中100/100で首位。Arbiter v4.13「Claude Fable 5 SWFTE 100/100首位」確認。
- **キーファクト:**
  - Artificial Analysis: Grok 4 知能指数73で総合#1（$6/M）
  - swfte.com: Claude Fable 5 100/100首位（357+モデル）
  - ベンチマーク首位が複数指標で分散
- **引用URL:** https://www.swfte.com/ai/leaderboard
- **Evidence ID:** EVD-20260620-0067

### INFO-068
- **タイトル:** ARC-AGI-2: トップモデルも新問題への適応・効率的推論に苦戦・MGB医療BRIDGE 44.8%
- **ソース:** Facebook / Healthcare IT News
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** 複数
- **要約:** ARC-AGI-2で現代のトップAIモデルは依然として新問題への適応・効率的推論に苦戦。MGB（Mass General Brigham）リーダーボード: LLMは標準化医学試験92%だがBRIDGE（患者ケア）は44.8%のみ。試験スコア≠実世界性能の乖離。
- **キーファクト:**
  - ARC-AGI-2: トップモデルも適応/効率推論に苦戦
  - 医学試験92% vs 患者ケアBRIDGE 44.8%
  - 試験スコア≠実世界性能
- **引用URL:** https://www.healthcareitnews.com/news/mgb-online-leaderboard-tracks-llm-patient-care-performance
- **Evidence ID:** EVD-20260620-0068

### INFO-069
- **タイトル:** lmcouncil.ai包括ベンチマーク(Jun 2026): GPT-5.5/Claude Opus/Gemini 3/Grok 4・30+フロンティア比較
- **ソース:** lmcouncil.ai (Epoch AI/Scale AI)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** 複数
- **要約:** lmcouncil.aiがEpoch AI/Scale AIの包括的ベンチマーク(Jun 2026)を公開。GPT-5.5/Claude Opus/Gemini 3/Grok 4など30+フロンティアモデルをキュレーション済みベンチマークで比較。
- **キーファクト:**
  - 30+フロンティアモデル比較（Epoch AI/Scale AI）
  - 対象: GPT-5.5, Claude Opus, Gemini 3, Grok 4
  - キュレーション済みベンチマーク
- **引用URL:** https://lmcouncil.ai/benchmarks
- **Evidence ID:** EVD-20260620-0069

## KIQ-003-03: オープンソースモデル（Meta Llama, Mistral等）と商用モデルの性能ギャップはどう変化しているか？

### INFO-070
- **タイトル:** Llama 4 Scout 17B-16EがサイズクラスでSOTA・Llama 4は1000万トークンコンテキスト主張
- **ソース:** Google Cloud (Llama partner models) / Facebook
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta, Google (ホスティング)
- **要約:** Llama 4 Scout 17B-16Eがサイズクラスでstate-of-the-art、先行Llama世代とオープン/プロプライエタリモデルを上回る。Llama 4は1000万トークンコンテキスト（主張）・GPT-4oを粉砕（主張）。Llama 3.3 70BはLlama 3.1 405Bと同等性能（効率化進展）。Google Gemini Enterprise Agent Platformでフルマネージド提供。
- **キーファクト:**
  - Llama 4 Scout 17B-16E: サイズクラスSOTA
  - Llama 4: 1000万トークンコンテキスト主張
  - Llama 3.3 70B ≈ Llama 3.1 405B（効率化）
  - Google Gemini EnterpriseでフルマネージドLlama提供
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama
- **Evidence ID:** EVD-20260620-0070

### INFO-071
- **タイトル:** Mistral 119Bオープンウェイトモデル公開・約100人エンジニアで18ヶ月に4つのSOTAオープンモデル構築
- **ソース:** LinkedIn / Panto AI / Reddit
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral AI
- **要約:** Mistral AIが119Bパラメータオープンウェイトモデル公開。約100人のエンジニアで18ヶ月に4つのSOTAオープンモデルを構築（米国スタートアップよりリーン・高速）。オープンウェイトモデルと広範なAPIサーフェスでエンタープライズ導入拡大。欧州AI主権の象徴。
- **キーファクト:**
  - Mistral 119B オープンウェイト公開
  - 約100人エンジニア・18ヶ月で4 SOTAモデル
  - オープンウェイト+APIでエンタープライズ導入
  - 欧州AI主権象徴
- **引用URL:** https://www.linkedin.com/posts/faizan170_analyzing-mistral-small-4-119b-the-new-heavyweight-activity-7471093889400033281-JP2o
- **Evidence ID:** EVD-20260620-0071

### INFO-072
- **タイトル:** Gemma 3 4B vs Llama 3.1 8B: ベンチマーク互角・小型オープンモデルの台頭
- **ソース:** LLM Stats
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** Google (Gemma), Meta (Llama)
- **要約:** Gemma 3 4BとLlama 3.1 8Bがベンチマックで互角（Gemma 3 4BがGPQA/IFEvalで勝、Llama 3.1 8BがHumanEval/MMLU-Proで勝）。小型オープンモデル（4B/8B）が実用域に到達。エッジ/ローカルデプロイの現実味向上。
- **キーファクト:**
  - Gemma 3 4B vs Llama 3.1 8B: 互角
  - Gemma優位: GPQA, IFEval
  - Llama優位: HumanEval, MMLU-Pro
  - 小型オープンモデル(4-8B)が実用域到達
- **引用URL:** https://llm-stats.com/models/compare/gemma-3-4b-it-vs-llama-3.1-8b-instruct
- **Evidence ID:** EVD-20260620-0072

## KIQ-003-04: 各社の資金調達・投資動向は何を示唆しているか？

### INFO-073
- **タイトル:** Anthropic Series H: $650億調達・評価額$9,650億（OpenAI超え最多価値スタートアップ）・Googleが最大$400億投資
- **ソース:** Yahoo Finance / World ORT / Instagram
- **公開日:** 2026-06-19
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic, Google
- **要約:** AnthropicがSeries Hで$650億調達、評価額$9,650億（OpenAIを超え最多価値スタートアップ）。Googleが最大$400億を投資（データセンター拡大を後押し）。GoogleがAnthropic支援でOpenAIに圧力をかける構造。Arbiter v4.13「Anthropic $650億$965億評価」確認。
- **キーファクト:**
  - Series H: $650億調達
  - 評価額: $9,650億（OpenAI超え最多価値スタートアップ）
  - Google: 最大$400億投資（データセンター後押し）
  - Google→OpenAI圧力構造
- **引用URL:** https://finance.yahoo.com/sectors/technology/articles/anthropic-turns-google-back-massive-193024074.html
- **Evidence ID:** EVD-20260620-0073

### INFO-074
- **タイトル:** OpenAI年率収益$250億超・$66億従業員持株売却で評価額$5,000億
- **ソース:** Forbes AI 50 / Prof Scott Galloway
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-OAI-001
- **関連企業:** OpenAI
- **要約:** OpenAIは2月末時点で年率収益$250億超（Forbes AI 50）。$66億の従業員持株売却で評価額$5,000億（SpaceXを抜く）。ただしAnthropic $9,650億評価に抜かれる。Scott Galloway「OpenAI/AnthropicはSpaceXに比べればバリュー株に見える」。
- **キーファクト:**
  - 年率収益: $250億超（2月末）
  - $66億持株売却・評価額$5,000億
  - Anthropic $9,650億に抜かれる
  - SpaceX $2.546兆と比較
- **引用URL:** https://www.forbes.com/lists/ai50/
- **Evidence ID:** EVD-20260620-0074

### INFO-075
- **タイトル:** AI企業の時価総額ランキング(2026/6/17): NVIDIA $5.014兆・Alphabet $4.422兆・Apple $4.385兆
- **ソース:** Instagram
- **公開日:** 2026-06-17
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** NVIDIA, Alphabet, Apple, Microsoft, SpaceX, Tesla
- **要約:** AI企業時価総額(2026/6/17): NVIDIA $5.014兆・Alphabet $4.422兆・Apple $4.385兆・Microsoft $2.859兆・SpaceX $2.546兆・Tesla。NVIDIAが2025年に$5兆初突破。インフラ層（NVIDIA）の圧倒的優位。
- **キーファクト:**
  - NVIDIA $5.014兆（2025年に$5兆初突破）
  - Alphabet $4.422兆・Apple $4.385兆
  - Microsoft $2.859兆・SpaceX $2.546兆
  - インフラ層(NVIDIA)の圧倒的優位
- **引用URL:** https://www.instagram.com/p/DZuu4YkID4P/
- **Evidence ID:** EVD-20260620-0075

### INFO-076
- **タイトル:** AIデータセンター投資ブーム: Adani×Jabil印度提携・サプライヤー(NVIDIA)が借入で建設
- **ソース:** Jabil / Investors.com / Forbes
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** NVIDIA, Adani, Jabil
- **要約:** AIデータセンター投資が爆発。Adani EnterprisesとJabilが印度でGW規模AIラック製造の戦略提携。AIデータセンター/ハードウェアサプライヤー(NVIDIA等)が建設資金として借入拡大。AIワークロードが計算/ストレージ需要を急増。
- **キーファクト:**
  - Adani×Jabil: 印度でGW規模AIラック製造提携
  - サプライヤーが借入でインフラ建設
  - AIワークロードで計算/ストレージ需要急増
  - データセンターがAIの「戦略的要地」（West Point）
- **引用URL:** https://investors.jabil.com/news/news-details/2026/Adani-Enterprises-and-Jabil-Target-a-Strategic-Alliance-to-Build-AI-Data-Center-Infrastructure-Platform-in-India/default.aspx
- **Evidence ID:** EVD-20260620-0076

## KIQ-003-05: 各社のエコシステムからの離脱コスト（スイッチングコスト）はどう変化しているか？

### INFO-077
- **タイトル:** AIコスト管理は「スイッチ」ではなく「ゲートウェイ」: Meta/Amazon/Uberが過支出→ハードキャップに1四半期で振子
- **ソース:** Truefoundry
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** Meta, Amazon, Uber
- **要約:** AIコスト制御はベンダー切り替え（スイッチ）ではなくゲートウェイ（ダイヤル）アプローチが適切。Meta/Amazon/Uberが過支出からハードキャップへ1四半期で振子移動（両極端は非理想的）。FinOpsゲートウェイで複数モデル間の動的ルーティング。多ベンダー戦略を可能にする中間層の台頭。
- **キーファクト:**
  - ゲートウェイ（ダイヤル）≠ スイッチ（2値）
  - Meta/Amazon/Uber: 過支出→ハードキャップに1四半期
  - FinOpsゲートウェイで動的ルーティング
  - 多ベンダー戦略を可能にする中間層台頭
- **引用URL:** https://www.truefoundry.com/pt/blog/field-notes-ai-cost-gateway-not-a-switch
- **Evidence ID:** EVD-20260620-0077

### INFO-078
- **タイトル:** compareai.today移行ガイド: プロバイダー間互換性スコア・コードスニペットで切替摩擦を定量化
- **ソース:** compareai.today
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** compareai.todayがAIプロバイダー間（OpenAI/Anthropic/Google等）のステップバイステップ移行ガイドを提供。コードスニペット・互換性スコア・移行の落とし穴を定量化。スイッチングコストの可視化・低減ツール。Arbiter v4.13「AI-ERP移行コスト半減」を補強。
- **キーファクト:**
  - プロバイダー間移行ガイド提供
  - 互換性スコア・コードスニペットで摩擦定量化
  - スイッチングコスト可視化/低減ツール
- **引用URL:** https://compareai.today/migration-guides
- **Evidence ID:** EVD-20260620-0078

### INFO-079
- **タイトル:** 中国スタートアップがOpenAI API遮断通知受領・強制ベンダー切替発生
- **ソース:** Yicai Global
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05, KIQ-002-03
- **関連企業:** OpenAI, 中国スタートアップ
- **要約:** 中国スタートアップがOpenAI APIでアプリ構築していたが、アクセス遮断の通知を受領開始。強制的なベンダー切替が発生。地政学的要因によるスイッチングコスト強制実現の事例。
- **キーファクト:**
  - 中国スタートアップがOpenAI API遮断通知受領
  - 強制ベンダー切替発生
  - 地政学的スイッチングコスト強制実現
- **引用URL:** https://www.facebook.com/yicaiglobal/posts/shares-of-knowledge-atlas-technology-joint-stock-a-chinese-ai-startup-better-kno/1439506311554031/
- **Evidence ID:** EVD-20260620-0079

### INFO-080
- **タイトル:** IDC: AI革新がエンタープライズ採用を上回る・ベンダーがパイロット→本番ギャップ解決の鍵
- **ソース:** IDC
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05, KIQ-002-02
- **関連企業:** 複数
- **要約:** IDC分析: AI革新がエンタープライズ採用のペースを上回る。AIソフト構築・販売ベンダーのみがパイロット→本番ギャップを解決する立場。Arbiter v4.13「マルチベンダー戦略普及（IDC）」と整合。
- **キーファクト:**
  - AI革新 > エンタープライズ採用ペース
  - パイロット→本番ギャップ
  - ベンダーがギャップ解決の鍵
- **引用URL:** https://www.idc.com/resource-center/blog/ai-is-ready-enterprises-are-not-vendors-need-to-fix-it/
- **Evidence ID:** EVD-20260620-0080

## KIQ-004-01: 広告運用・コーディング・CS等の先行領域で、AI業務自律化はどの段階まで進んでいるか？

### INFO-081
- **タイトル:** WSJ/PwC A-2: ソフト開発者求人が2022ピーク比70%減・22-25歳20%減（2024比）
- **ソース:** WSJ / PwC AI Jobs Barometer / 2026 AI Index
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** 複数
- **要約:** WSJ報道: ソフト開発者求人が2022ピーク比70%減（5月末時点・昨春の低値から若干改善）。GitHub Copilot等で1人がかつてのチーム業務を処理。2026 AI Index: 22-25歳ソフト開発者雇用が2024比20%減。PwC: AI高曝露セクターで初期キャリア募集が横ばい化、だが「シニア化」エントリーレベル職は2019比35%成長。Arbiter v4.13 H-CAR-002 A-2証拠確認。
- **キーファクト:**
  - ソフト開発者求人: 2022ピーク比70%減
  - 22-25歳ソフト開発者: 2024比20%減
  - 初期キャリア募集: AI高曝露セクターで横ばい
  - シニア化エントリー職: 2019比35%成長
- **引用URL:** https://www.wsj.com/lifestyle/careers/changing-careers-cutting-expenses-software-engineers-contend-with-ai-3889ce73
- **Evidence ID:** EVD-20260620-0081

### INFO-082
- **タイトル:** KPMG: AIがエントリーレベル（徒弟制度）タスクを自動化・次世代育成の完全再考を迫る
- **ソース:** KPMG / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** KPMG
- **要約:** KPMG分析: AIがかつてプロの徒弟制度として機能したエントリーレベルタスクを自動化、次世代育成の完全な再考を迫る。CFOはボラティリティ対応と市場逆風管理の中で人材モデル転換に直面。ただ41%の組織のみが生成AI利用ポリシーを保有（シャドーAIギャップ）。
- **キーファクト:**
  - AIがエントリーレベル徒弟タスクを自動化
  - 次世代育成モデルの完全再考が必要
  - 41%組織のみ生成AIポリシー保有
- **引用URL:** https://kpmg.com/us/en/articles/2026/cfo-navigate-volatility-while-managing-market-headwinds.html
- **Evidence ID:** EVD-20260620-0082

### INFO-083
- **タイトル:** NBER予測: 2026年に約50万2,000件のAI関連人員削減（2025年比9倍）
- **ソース:** Improvado (NBER引用) / WIONews
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01
- **関連企業:** 複数
- **要約:** NBER予測: 2026年に約50万2,000件のAI関連人員削減（2025年の約55,000件の9倍）。2025年に米国労働者の5人に1人のみが自分の仕事が安全と感じた。企業は議論中に既に削減決定を実行（AIレイオフ vs AIウォッシングの議論）。
- **キーファクト:**
  - 2026年AI関連削減: 約502,000件（2025比9倍）
  - 2025年: 約55,000件
  - 5人に1人のみ仕事が安全と回答
  - AIレイオフ vs AIウォッシング議論
- **引用URL:** https://improvado.io/blog/ai-job-loss-employment-impact
- **Evidence ID:** EVD-20260620-0083

### INFO-084
- **タイトル:** CyberAgentがAI広告クリエイティブ制作＋配信プラットフォーム構築・Seven-Eleven広告でAI生成時代
- **ソース:** note.com / Alibaba Cloud
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-002-05
- **関連企業:** CyberAgent, Seven-Eleven, Alibaba Cloud
- **要約:** CyberAgentがAIによる広告クリエイティブ制作と配信プラットフォーム開発を担当。Seven-Eleven広告でAI生成コンテンツ時代に突入。最適広告を自動配信。Alibaba Cloudと持続可能なGenAI採用で戦略対話。広告運用のAI自律化の先行事例。
- **キーファクト:**
  - CyberAgent: AI広告クリエイティブ制作+配信プラットフォーム
  - Seven-Eleven広告: AI生成コンテンツ時代
  - 最適広告の自動配信
  - Alibaba CloudとGenAI採用戦略対話
- **引用URL:** https://note.com/mugimugi92/n/n437629fc3f02?hl=en
- **Evidence ID:** EVD-20260620-0084

## KIQ-004-02: コーディング能力の市場価値はどう変化しているか？

### INFO-085
- **タイトル:** JetBrains 1万人調査: Claude Code採用3%→24%(米国)・18%(世界)・9ヶ月で・「最も愛される」46%
- **ソース:** Fleapo / Pick Right / Gradually AI
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Anthropic (Claude Code), JetBrains
- **要約:** JetBrains世界開発者調査(10,000+人): Claude Code採用が9ヶ月で3%→18%(世界)・24%(米国)に急拡大。JetBrains 2026年4月調査で「最も愛される」AIコーディングツール46%。Cursorは18%(企業採用・JetBrains Jan 2026)。Arbiter v4.13 H-ANT-002 B-3証拠確認。
- **キーファクト:**
  - Claude Code採用: 3%→18%(世界)/24%(米国)・9ヶ月
  - 「最も愛される」: 46%（JetBrains Apr 2026）
  - Cursor: 18%企業採用（JetBrains Jan 2026）
  - SpaceXがCursorをAIモデル訓練で買収
- **引用URL:** https://www.facebook.com/fleapo/posts/as-per-jetbrains-global-developer-survey-of-10000-developers-claude-code-went-fr/1434664075346463/
- **Evidence ID:** EVD-20260620-0085

### INFO-086
- **タイトル:** エンタープライズAIコーディングagent市場: $98億-110億年率(2026年4月)・コード補完を超越
- **ソース:** Instagram引用 / WindowsForum
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02, KIQ-003-04
- **関連企業:** 複数
- **要約:** エンタープライズAIコーディングagent市場は2026年4月時点で$98億-110億年率。コード補完を超えて急速進化。79%企業がAI agent採用するが本番稼働は11%のみ（$108億市場）。採用-本番ギャップが継続。
- **キーファクト:**
  - コーディングagent市場: $98億-110億年率(2026年4月)
  - 79%企業採用 vs 11%本番稼働
  - $108億市場・高失敗率
  - コード補完を超越
- **引用URL:** https://windowsforum.com/threads/agentic-ai-in-2026-from-copilots-to-autonomous-enterprise-workflow-agents.427936/
- **Evidence ID:** EVD-20260620-0086

### INFO-087
- **タイトル:** 「コードを書くのが仕事→AI agentチームを率いるのが仕事」・メタスキル(設計/評価)への移行
- **ソース:** Instagram / O'Reilly / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** 複数
- **要約:** 「コードを書くのが仕事だった→今はAI agentチームを率いるのが仕事」。Sean GoedeckeはAIコーディングagentは既にコモディティ化と主張。メタスキル（設計・評価・3つの基本メタスキル）への焦点移行が進行。8年経験のソフトウェアエンジニアが3月に解雇。Arbiter v4.13「価値低下→価値変容」修正を支持。
- **キーファクト:**
  - 「コードを書く→AI agentチームを率いる」転換
  - AIコーディングagent既にコモディティ化（Goedecke）
  - メタスキル（設計/評価）への移行
  - 8年経験エンジニア解雇事例
- **引用URL:** https://www.instagram.com/reel/DZtJPP5PKUe/
- **Evidence ID:** EVD-20260620-0087

### INFO-088
- **タイトル:** AIコーディングROI: 開発者の月額支出が$29→$750・$50→$3,000に急増
- **ソース:** DX (getdx.com)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02, KIQ-003-01
- **関連企業:** 複数
- **要約:** AIコーディングアシスタント使用で開発者の月額支出が急増（$29→$750、$50→$3,000）。コーディング能力の価値変容と共に、ツール利用のコスト管理が新課題。企業はROI測定に苦慮。
- **キーファクト:**
  - 開発者支出: $29→$750/月、$50→$3,000/月
  - コーディングROI測定の難しさ
  - ツール利用コスト管理が新課題
- **引用URL:** https://getdx.com/blog/ai-coding-assistant-pricing/
- **Evidence ID:** EVD-20260620-0088

## KIQ-004-03: AI代替が困難な能力（課題定義・対人関係・異領域統合）の市場価値は上昇しているか？

### INFO-089
- **タイトル:** WEF: 2030年までに1.7億新規雇用創出・9,200万消失・AI技能が人材不足リスト首位
- **ソース:** World Economic Forum
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** WEF予測: 2030年までに1億7,000万の新規雇用創出だが9,200万も消失。72%の雇用主が求める人材発見に困難、AI関連スキルが人材不足リスト首位。AIは人間の能力を増強し置換しない——学習/効率/規模を支援するが、アイデンティティ/価値観/関係性は複製不能。
- **キーファクト:**
  - 新規雇用創出: 1.7億（2030年まで）
  - 消失雇用: 9,200万
  - 72%雇用主が人材発見困難・AI技能が不足首位
  - AIは増強・アイデンティティ/価値観/関係性は複製不能
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-workforce-hiring-fix-skills-mismatch/
- **Evidence ID:** EVD-20260620-0089

### INFO-090
- **タイトル:** 新AI職種の出現: AIアートディレクター($95+/時)・生成AIスペシャリスト・アジェンティック検索ディレクター
- **ソース:** TEKsystems / Mediabistro / labasaddesign
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** AI時代の新職種が出現: AIアートディレクター/デザイナー($95.00-/時)、AIクリエイティブデザイナー、クリエイティブテクノロジスト、生成AIスペシャリスト、アジェンティック検索ディレクター、デジタル戦略。AIはクリエイティブ専門家を置換ではなく採用基準を再定義。
- **キーファクト:**
  - AIアートディレクター: $95+/時
  - 新職種: 生成AIスペシャリスト・アジェンティック検索ディレクター
  - AIは置換ではなく採用基準再定義
- **引用URL:** https://careers.teksystems.com/us/en/job/JP-006099331/AI-Art-Director-Designer
- **Evidence ID:** EVD-20260620-0090

### INFO-091
- **タイトル:** PwC 2026 Global AI Jobs Barometer: AIが2極化労働市場創出・TMTセクター新規役職8件に1件がAI関連
- **ソース:** PwC
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** PwC 2026 Global AI Jobs Barometer（6大陸10億件超の求人広告分析）: AIが2極化労働市場を創出。テクノロジー・メディア・通信(TMT)セクターがAI採用強度で全セクター首位、新規役職8件にほぼ1件がAI関連。
- **キーファクト:**
  - 10億件超求人広告分析
  - AIが2極化労働市場創出
  - TMTセクター: 新規役職8件に1件がAI関連
- **引用URL:** https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html
- **Evidence ID:** EVD-20260620-0091

### INFO-092
- **タイトル:** AIリスキリング格差: 80%+従業員参加組織はわずか6%・人間の準備度が差別化要因
- **ソース:** Aon / ManpowerGroup
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** 複数
- **要約:** Aon分析: AI自体が差別化要因ではなく労働力準備度が差別化要因。過去1年に80%超の従業員がAIリスキリング/アップスキリングに参加した組織はわずか6%。企業はAI統合向け訓練プログラムに巨額投資。
- **キーファクト:**
  - 差別化要因: AIではなく労働力準備度
  - 80%+参加組織: わずか6%
  - 企業がAI訓練に巨額投資
- **引用URL:** https://www.aon.com/en/insights/articles/ai-isnt-the-differentiator-workforce-readiness-is
- **Evidence ID:** EVD-20260620-0092

## KIQ-004-04: 「AI時代に勝つ企業」の条件を満たす企業はどこか？

### INFO-093
- **タイトル:** エンタープライズAI展開95%失敗: 勝者は顧客関係/独自データ/重要ワークフローの「所有」で差別化
- **ソース:** LinkedIn (Lachlan Fogarty)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-04, KIQ-002-02
- **関連企業:** 複数
- **要約:** エンタープライズAIプロジェクトの95%が失敗。勝者を分けるのは顧客関係・独自データ・重要ワークフローの「所有」——AIが市場の摩擦を除去する中で。Arbiter v4.13「エンタープライズAI展開95%失敗(INFO-076)」確認。文脈の堀（context moat）がAI時代の競争優位源泉。
- **キーファクト:**
  - エンタープライズAI展開95%失敗
  - 勝者条件: 顧客関係/独自データ/重要ワークフロー所有
  - 文脈の堀（context moat）が競争優位
- **引用URL:** https://www.linkedin.com/posts/lachlan-fogarty_the-context-moat-why-95-of-ai-projects-activity-7471144941168078848-DULd
- **Evidence ID:** EVD-20260620-0093

### INFO-094
- **タイトル:** AlibabaがRMB 3,800億のAI/クラウド投資発表・CyberAgentはAIクリエイティブBPOで国内首位パートナー
- **ソース:** Alibaba Cloud / note (lire_marketing)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** Alibaba, CyberAgent
- **要約:** AlibabaがAI/クラウド技術にRMB 3,800億の投資を発表。CyberAgentはAIクリエイティブBPOサービスで国内デジタル広告のトップパートナー、クライアントのマーケティング効率/成果を最大化。ChatGPT広告日本展開（電通/CyberAgentが配置支援）。CyberAgent×Alibaba Cloud戦略対話。
- **キーファクト:**
  - Alibaba: RMB 3,800億AI/クラウド投資
  - CyberAgent: AIクリエイティブBPO国内首位パートナー
  - ChatGPT広告日本（電通/CyberAgent配置支援）
  - CyberAgent×Alibaba Cloud戦略対話
- **引用URL:** https://www.facebook.com/alibabacloud/posts/we-are-pleased-to-announce-a-strategic-dialogue-between-alibaba-cloud-and-cybera/1456869966485091/
- **Evidence ID:** EVD-20260620-0094

### INFO-095
- **タイトル:** データ堀（データモート）が企業価値を左右・クリーンデータと防御可能AIが評価を引き上げ
- **ソース:** Capital Riesgo (M&A分析) / ScienceDirect
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** 複数
- **要約:** M&A分析: データ堀（競合が容易に複製できない独自データ）が企業価値を左右。クリーンデータと防御可能なAIがエンタープライズ価値を引き上げ。AIモデルは伝統的ソフトより同質的に機能するが、周囲の技術エコシステムへの依存がより高い。
- **キーファクト:**
  - データ堀: 競合が複製困難な独自データ
  - クリーンデータ+防御可能AI=企業価値向上
  - AIモデルは技術エコシステム依存が高い
- **引用URL:** https://capital-riesgo.es/en/articles/ai-driven-m-a-how-artificial-intelligence-is-reshaping-every-stage-of-the-deal-cycle/
- **Evidence ID:** EVD-20260620-0095

## KIQ-005-01: AGI到達度を示すベンチマーク指標と能力の進展はどう変化しているか？

### INFO-096
- **タイトル:** ARC-AGI段階的困難化: ARC-1 93%・ARC-2 68.8%・ARC-3 0.37%（GPT-5.4は0.26% vs 人間100%）
- **ソース:** Level Up (gitconnected) / AISafety Turkiye
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** OpenAI, 複数
- **要約:** ARC-AGI段階別スコア: ARC-AGI-1 フロンティア93%・ARC-AGI-2 68.8%（2025年末最高24%から上昇）・ARC-AGI-3 0.37%（GPT-5.4は0.26%・人間100%）。ARC-2→ARC-3の急落は「適応・効率的推論」の根本的欠如を示す。Arbiter v4.13 IND-025/028確認。
- **キーファクト:**
  - ARC-AGI-1: 93%・ARC-AGI-2: 68.8%・ARC-AGI-3: 0.37%
  - GPT-5.4: ARC-AGI-3で0.26%（人間100%）
  - ARC-2→ARC-3の急落=適応/効率推論の根本欠如
- **引用URL:** https://levelup.gitconnected.com/gpt-5-4-scored-0-26-humans-scored-100-the-gap-is-not-a-bug-jean-piaget-proved-it-in-1971-0ce31d0be896
- **Evidence ID:** EVD-20260620-0096

### INFO-097
- **タイトル:** SingularityNET研究者がARC-AGI-3で33%+達成（LLM+手続き型世界モデル+検証）、トップLLM単独を大幅上回る
- **ソース:** X (Ben Goertzel)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01
- **関連企業:** SingularityNET
- **要約:** SingularityNET研究者がLLM+手続き型世界モデル+検証の組み合わせでARC-AGI-3に33%+を達成（トップLLM単独の0.37%を大幅上回る）。ハイブリッド手法で推論能力を補強可能。Arbiter v4.13「SingularityNET ARC-AGI-3 33%+」確認。
- **キーファクト:**
  - ARC-AGI-3 33%+（ハイブリッド: LLM+世界モデル+検証）
  - トップLLM単独0.37%を大幅上回る
  - 手続き型世界モデルで推論補強
- **引用URL:** https://x.com/bengoertzel/article/2053072200987545755
- **Evidence ID:** EVD-20260620-0097

### INFO-098
- **タイトル:** DeepMind「From AGI to ASI」レポート公開・AGIが投機から現実へ・2028年50%で知識移転/広域推論
- **ソース:** LinkedIn (Matija Franklin) / Medium
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Google / DeepMind
- **要約:** DeepMind「From AGI to ASI」レポート公開。過去10年で人間レベルAGI構築が遠い投機から現実へ。2028年までにAIが知識移転・広域推論のマイルストーンを達成する50%の確率。Arbiter v4.13「DeepMind From AGI to ASI AGI 2029-2030」確認。
- **キーファクト:**
  - 「From AGI to ASI」レポート公開
  - AGIが投機から現実へ
  - 2028年50%で知識移転/広域推論マイルストーン
- **引用URL:** https://www.linkedin.com/posts/matijafranklin_our-report-from-agi-to-asi-is-out-over-activity-7471172615995514882-iqwc
- **Evidence ID:** EVD-20260620-0098

### INFO-099
- **タイトル:** Anthropic認識: ベンチマーク供給がボトルネック・「IQ」の普遍的指標不在
- **ソース:** Instagram
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** Anthropicがフロンティア問題を認識: ベンチマーク供給がボトルネック。「IQ」の普遍的指標がなく、モデルはvibeコーディングで勝てるが抽象推論で負ける。客観的AGI到達度測定の限界。
- **キーファクト:**
  - ベンチマーク供給がボトルネック
  - 「IQ」普遍的指標不在
  - vibeコーディング勝利≠抽象推論勝利
- **引用URL:** https://www.instagram.com/reel/DZoF9AWEVRu/
- **Evidence ID:** EVD-20260620-0099

### INFO-100
- **タイトル:** Databricks「AGIモーメント」: Lake TAP新アーキテクチャでagentが運用/分析ワークロードへ統合アクセス
- **ソース:** SiliconANGLE
- **公開日:** 2026-06-16
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** Databricks
- **要約:** Databricksが新アーキテクチャ「Lake Transactional/Analytical Processing (Lake TAP)」を公開、AI agentが運用・分析ワークロードに統合アクセス可能に。「AGI実現の重要マイルストーン」と評価。agentの本番サポート/デプロイに焦点。
- **キーファクト:**
  - Lake TAP新アーキテクチャ公開
  - agentが運用/分析ワークロード統合アクセス
  - 「AGI実現の重要マイルストーン」評価
- **引用URL:** https://siliconangle.com/2026/06/16/agi-moment-databricks-new-releases-zero-support-deployment-ai-agents/
- **Evidence ID:** EVD-20260620-0100

## KIQ-005-02: 主要CEO/研究者のAGIタイムライン予測はどう変化しているか？

### INFO-101
- **タイトル:** Kalshi予測市場: OpenAIが2030年までにAGI到達55%・Amodeiは2027年可能性
- **ソース:** Delos / Kalshi (April 2026)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Anthropic
- **要約:** Kalshi予測市場(2026年4月): OpenAIが2030年までにAGI到達する確率55%。Dario Amodeiは2027年に可能性。Amodeiは6-12ヶ月以内にAIがソフトウェアエンジニアのほぼ全業務をこなす可能性と予測。Sam Altmanは2025年にAGI到達・機械が「人間のように思考」すると主張（前倒し予測）。
- **キーファクト:**
  - Kalshi: OpenAI AGI 2030年到達55%
  - Amodei: 2027年可能性・6-12ヶ月でエンジニア業務ほぼ全自動
  - Altman: 2025年AGI到達主張（前倒し）
  - 主要CEOが basics で不一致
- **引用URL:** https://www.delos.so/en/blog/agi-myth-or-reality-state-of-the-art-2026
- **Evidence ID:** EVD-20260620-0101

### INFO-102
- **タイトル:** 研究者根本的意見分裂: LeCunがAMI Labs設立($10.3億シード)・「AGIは単一イベントでない」
- **ソース:** Bloomberg / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** AMI Labs (Yann LeCun)
- **要約:** Yann LeCunが「LLMはAGIをもたらさない」「AGIは近づいていない」と主張しAMI Labsを設立（$10.3億シード・$35億評価額）。AGIは「カレンダーに印をつけられる単一イベントではない」「AGI前日/翌日はない」と主張。Muskは今年中超知能到達、Hassabisは5-10年、研究者間で根本的分裂。Arbiter v4.13「LeCun退社AMI Labs」確認。
- **キーファクト:**
  - LeCun: AMI Labs設立（$10.3億シード・$35億評価）
  - 「LLMはAGIをもたらさない」「AGIは近づいていない」
  - 「AGI前日/翌日はない」単一イベント否定
  - Musk: 今年中超知能・Hassabis: 5-10年・研究者根本分裂
- **引用URL:** https://www.facebook.com/bloombergbusiness/posts/ami-labs-executive-chairman-yann-lecun-says-the-future-of-ai-depends-on-systems-/1429002592419163/
- **Evidence ID:** EVD-20260620-0102

### INFO-103
- **タイトル:** Microsoft AI CEO Suleyman: AIが自己改善できる時点が危険の始まり・明確なシャットダウンポイント必要
- **ソース:** Instagram
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-02, KIQ-005-03
- **関連企業:** Microsoft (Mustafa Suleyman)
- **要約:** Microsoft AI CEO Mustafa Suleyman: AIが自己を改善できる能力に達した時点が危険の始まり、明確なシャットダウンポイントが存在すべきと主張。超知能構築と安全性の両論を提示。再帰的自己改善(RSI)の具体的脅威認識。
- **キーファクト:**
  - AI自己改善能力到達=危険の始まり
  - 明確なシャットダウンポイント必要
  - RSIの具体的脅威認識
- **引用URL:** https://www.instagram.com/reel/DZvp7TGDvQc/
- **Evidence ID:** EVD-20260620-0103

## KIQ-005-03: AGI安全性とガバナンスの政策議論はどう進展しているか？

### INFO-104
- **タイトル:** トランプ法案: 州レベルAI規制に10年禁止・「AI脱獄(jailbreak)懸念」で政府行動・激しい反発
- **ソース:** WIONews / Instagram / InterestingThingsAroundWorld
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** 米国政府
- **要約:** トランプ政権の最新法案に州レベルAI規制の10年禁止が含まれ激しい反発。「AI脱獄(jailbreak)懸念」を理由に政府がフロンティアAI規制を強化。論争: 連邦か州か誰が規制すべきか。一部は「オンライン安全」規則が合法的言論の過剰削除を圧力化すると批判。
- **キーファクト:**
  - 州AI規制10年禁止法案（トランプ）
  - 「AI脱獄」懸念で政府行動
  - 連邦 vs 州規制権限論争
  - オンライン安全規則の過剰削除リスク批判
- **引用URL:** https://www.facebook.com/WIONews/posts/us-tightens-grip-on-frontier-aiai-jailbreak-fears-trigger-government-actiondiksh/1366374182268419/
- **Evidence ID:** EVD-20260620-0104

### INFO-105
- **タイトル:** 豪州AI安全研究所に哲学者が就任・英国「AI Scenarios 2030」で政策計画支援
- **ソース:** Daily Nous / UK Gov
- **公開日:** 2026-06-15
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** 豪州政府, 英国政府
- **要約:** 豪州政府のAI安全研究所に哲学者がトップとして就任（AI能力/リスクの監視/テスト/情報共有が目的）。英国政府が更新版「AI Scenarios 2030」を公開、全政策分野で政策担当者のAI将来計画を支援。各国でAI安全制度構築進展。
- **キーファクト:**
  - 豪州AI安全研究所: 哲学者がトップ就任
  - 目的: AI能力/リスク監視/テスト/情報共有
  - 英国: AI Scenarios 2030（全政策分野向け）
  - 各国でAI安全制度構築進展
- **引用URL:** https://dailynous.com/2026/06/15/philosopher-to-head-australian-governments-ai-safety-institute/
- **Evidence ID:** EVD-20260620-0105

### INFO-106
- **タイトル:** Science: Fable 5の回答拒否が「隠蔽から可視化」へ方針更新・研究者が企業/政府の板挟み
- **ソース:** Science.org
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-GOV-001
- **関連企業:** Anthropic
- **要約:** Science報道: Fable 5の回答拒否(refusals)が隠蔽ではなく可視化されるよう方針更新。だが「息抜きは短命」だった。AI安全研究者が企業と政府の板挟みに。Anthropicモデルの安全性ポリシー変動が観察可能。
- **キーファクト:**
  - Fable 5: 回答拒否を隠蔽から可視化へ方針更新
  - 息抜きは短命（一時的）
  - 安全研究者が企業/政府の板挟み
- **引用URL:** https://www.science.org/content/article/researchers-caught-crossfire-companies-and-government-grapple-over-ai-safety
- **Evidence ID:** EVD-20260620-0106

### INFO-107
- **タイトル:** 中南米AI法案は全件EU AI Actをテンプレート化・国境を越えたAI安全協議の模索
- **ソース:** EA Forum / GMFUS
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** 中南米各国, EU
- **要約:** 中南米の全AI法案がEU AI Actをテンプレートに採用（コロンビアPL 043/2025等リスクティア別）。包括的AI政策合意が困難な中、公共利益AIでの集合的強み活用を実務的アプローチとして模索（米欧越境協力）。
- **キーファクト:**
  - 中南米AI法案: 全件EU AI Actテンプレート
  - コロンビアPL 043/2025（リスクティア別）
  - 公共利益AIで越境協力模索
- **引用URL:** https://forum.effectivealtruism.org/posts/3sL6iB6WzKHJciwta/latin-america-in-search-of-its-stake-in-ai-safety-a-map
- **Evidence ID:** EVD-20260620-0107

## BYTEDANCE-CHINESE: ByteDance/Doubao/Seed中国語一次情報の収集

### INFO-108
- **タイトル:** 豆包DAU 2億超・日収入<100万元(主にEC手数料)・日コスト数千万元（火山引擎API推算）
- **ソース:** 新浪財経 / Yahoo香港 / 搜狐 / Zhihu
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-BTD-001, KIQ-002-05
- **関連企業:** ByteDance
- **要約:** 晩点Latepost報道: 豆包の今年上半期DAUが2億人超。だが日収入は100万元人民幣不足（主にEC手数料）。5月時点で日コスト数千万元（火山引擎API価格・モデル毛利率・ユーザー行動から推算）。Arbiter v4.13 H-BTD-002核心証拠（日収入<$140K/日コスト数千万元）を中国語一次ソースで確認。
- **キーファクト:**
  - 豆包DAU: 2億人超（上半期）
  - 日収入: <100万元人民幣（主にEC手数料）
  - 日コスト: 数千万元（火山引擎API推算）
  - DAU 2億は「最も価値の低い無料ユーザー」
- **引用URL:** https://cj.sina.com.cn/articles/view/5952915705/162d248f9067034ids?froms=ggmp
- **Evidence ID:** EVD-20260620-0108

### INFO-109
- **タイトル:** 火山引擎が中国agent開発プラットフォーム市場で双首位・Coze(扣子)3.0へアップグレード
- **ソース:** Zhihu / Volcengine
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance (火山引擎)
- **要約:** 火山引擎が中国agent開発プラットフォーム市場で双首位を獲得。Coze(扣子)は2025年に企業向け零コードAgent開発デプロイを提供し、2026年6月に新3.0バージョンへアップグレード。企業級AI agent開発の中国市場リーダー。
- **キーファクト:**
  - 火山引擎: 中国agent開発プラットフォーム市場双首位
  - Coze(扣子): 2025年零コードAgent開発
  - 2026年6月: 新3.0バージョンへアップグレード
- **引用URL:** https://zhuanlan.zhihu.com/p/2050221892016067387
- **Evidence ID:** EVD-20260620-0109

### INFO-110
- **タイトル:** Seedance 2.0: ByteDance SEED研究所のマルチモーダル動画生成（1080p・4-15秒・音声同期）
- **ソース:** Atlas Cloud / mcpservers.org
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance (SEED Lab)
- **要約:** Seedance 2.0はByteDance傘下SEED研究所開発のマルチモーダルAI動画生成モデル。テキスト・参照画像・音声を入力に単一統一生成で高画質動画を出力。文生動画/図生動画/参考生動画対応・最高1080p・4-15秒・音声同期。即夢(Jimeng)経由＋agent skillとしてCLI利用可能。
- **キーファクト:**
  - Seedance 2.0: SEED研究所マルチモーダル動画生成
  - 対応: 文生/図生/参考生動画・1080p・4-15秒・音声同期
  - 即夢(Jimeng)経由＋agent skill(CLI)で利用
- **引用URL:** https://www.atlascloud.ai/zh-TW/blog/guides/seedance-2.0-complete-guide
- **Evidence ID:** EVD-20260620-0110

---

## Step 4 詳細スクレイピング追補

### INFO-111
- **タイトル:** FutureSearch詳細予測: Fable 5米国復帰中央値7月12日・4シナリオ(政治43%/アクセス23%/誤解20%/能力14%)・外国人アクセス2026中に不可
- **ソース:** FutureSearch（詳細スクレイプ）
- **公開日:** 2026-06-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-GOV-001, KIQ-002-06
- **関連企業:** Anthropic, 米国政府, Amazon
- **要約:** FutureSearch詳細シナリオ予測。6月11日AmazonのAndy Jassyが財務長官Scott Bessentへセキュリティ発見をエスカレート→NSA査査→国家サイバー局長Sean Cairncross→6月12日17:21ET商務省「is-informed」書簡(ECRA)。トリガーは「狭い非普遍的脱獄」(コード読んで欠陥修正するプロンプト)。100+サイバー研究者が公開書簡(freefable.org)・Alex Stamos「スピード違反への死刑」。ホワイトハウス要求: Project Glasswing(50-150組織)の完全開示+jailbreak-proofガードレール(技術的に不可能)。G7(6/16-17)で同盟国例外を「完全に非論理的」と拒否。予測: Fable米国復帰中央値7月12日・外国人は2026年不可の可能性大。他社への波及12%(2026末)。
- **キーファクト:**
  - 6月11日: Amazon Jassy→財務長Bessentエスカレート
  - 6月12日17:21ET: 商務省ECRA「is-informed」書簡
  - 100+サイバー研究者が公開書簡・Stamos「スピード違反への死刑」
  - 4シナリオ: 政治43%/アクセス23%/誤解20%/能力14%
  - Fable復帰中央値7月12日・外国人2026年不可の可能性
  - 他社波及12%(2026末)
- **引用URL:** https://futuresearch.ai/claude-fable-ban-forecast/
- **Evidence ID:** EVD-20260620-0111

### INFO-112
- **タイトル:** Built In詳細タイムライン: ペンタゴンがマドゥロ(Venezuela)捕縛でClaude使用→赤線拒否→SCR指定→裁判所Rita Linが「処罰・言論侵害」評→連邦控訴裁はSCR維持
- **ソース:** Built In（詳細スクレイプ）
- **公開日:** 2026-06-17
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-001, KIQ-GOV-002
- **関連企業:** Anthropic, 米国防総省, OpenAI, Google, xAI, Palantir
- **要約:** 詳細タイムライン: 2025年7月$200M契約→2026年1月DoDが更なるアクセス要求→ペンタゴンがPalantir経由でClaudeをマドゥロ捕縛に使用→2月24日赤線撤廃期限→3月5日SCR指定→3月9日Anthropic提訴→3月Rita Lin判事が予備的差止(「処罰・言論の自由侵害」)→4月DOJ控訴→4月連邦控訴裁がAnthropic救済却下(SCR維持)→6月輸出管理。OpenAI/Google/xAIは全ガードレール撤廃・Anthropicのみ拒否。Hegseth「軍と取引する全契約者はAnthropicと商業活動禁止」。DoD40頁準備書面: Anthropicが「赤線越え時に技術を無効化/事前改変」する恐れ。数百人のOpenAI/Google従業員がAnthropic姿勢の模倣を求める請願。
- **キーファクト:**
  - ペンタゴンがマドゥロ(Venezuela)捕縛でClaude使用
  - Anthropicは機密利用を提供した唯一のAI企業(Palantir経由)
  - OpenAI/Google/xAIはガードレール撤廃・Anthropicのみ拒否
  - 判事Rita Lin: 政府行動=処罰・言論侵害
  - 連邦控訴裁はSCR指定維持(救済却下)
  - Hegseth: 軍契約者のAnthropic商業活動禁止
  - 数百人のOpenAI/Google従業員がAnthropic模倣請願
  - ペンタゴンはGoogle/xAI/Amazon/Microsoft/Nvidiaと同様契約
- **引用URL:** https://builtin.com/articles/anthropic-pentagon-claude-dispute
- **Evidence ID:** EVD-20260620-0112
