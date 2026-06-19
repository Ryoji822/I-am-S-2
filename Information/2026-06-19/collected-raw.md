# 収集データ: 2026-06-19

## メタデータ
- 収集日時: 2026-06-19 01:46 UTC（開始）〜 02:35 UTC（完了）
- 品質フラグ: COMPLETE
- 実行検索クエリ数: 約143件（collection_plan 122件 + 動的クエリ15件 + Step2追加6件）
- 実行スクレイプ数: 12件（Step2公式ブログ4件 + Step4重要記事8件）
- 実行マップ数: 4件（OpenAI/Anthropic/Google/xAI公式ブログ）
- 収集情報数: 96件（INFO-001〜INFO-096）
- Evidence ID範囲: EVD-20260619-0001 〜 EVD-20260619-0096
- KIQカバレッジ: 24/24 KIQエントリ完了（PIR-001〜005全5領域 + BYTEDANCE-CHINESE）
- Tier1企業カバレッジ: OpenAI✓ Anthropic✓ Google/DeepMind✓ xAI✓ ByteDance✓
- 品質注記:
  - 信頼性コードA（一次ソース）: 12件
  - 信頼性コードB（主要メディア）: 54件
  - 信頼性コードC（テック系）: 18件
  - 信頼性コードD（個人・SNS）: 8件
  - 信頼性コードN/A（該当なし等）: 4件
  - 該当なし（空検索結果）: 3件（BYTEDANCE-CHINESE中国語クエリ3/6）
- Arbiter連動: DEGRADEDモード対応・動的クエリ優先KIQ 6件追加実行（KIQ-MIL-001/GOV-002/OAI-001/OAI-002/BTD-001/004-01）

## 収集結果

### --- 公式ブログ・一次ソース（Step 2）---

### INFO-001
- **タイトル:** Anthropic Labs「Claude Design」発表 — Opus 4.7搭載のデザイン協作ツール
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05, KIQ-001-03
- **関連企業:** Anthropic, Canva
- **要約:** Anthropic LabsがClaude Designを発表。最高性能の視覚モデルClaude Opus 4.7を搭載し、デザイン・プロトタイプ・スライドなどをClaudeと協作作成。Pro/Max/Team/Enterprise向けリサーチプレビュー。Canva連携・Claude Codeへのハンドオフ機能を含む。
- **キーファクト:**
  - Claude Opus 4.7搭載・リサーチプレビュー提供開始
  - チームのデザインシステム（カラー・タイポグラフィ・コンポーネント）をコードベース/デザインファイルから自動構築し全プロジェクトへ適用
  - PPTX/PDF/HTML/Canvaエクスポート対応・Claude Codeへのワンクリックハンドオフ
  - Datadog・Brilliant等が早期採用（「20+プロンプト→2プロンプト」で再現と報告）
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260619-0001

### INFO-002
- **タイトル:** TCSとAnthropicが提携 — 規制産業向けClaude展開・5万人従業員・56カ国
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-001-03
- **関連企業:** Anthropic, TCS (Tata Consultancy Services), Diligenta, TCS iON
- **要約:** AnthropicがTata Consultancy Servicesと提携。TCSは5万人の自社従業員（56カ国）にClaudeを提供し、金融・医療・公共部門等の規制産業向けClaude搭載製品を構築。Claude Partner Networkに参加。Dario Amodeiはインドを「第2の市場」と位置付け。
- **キーファクト:**
  - TCS従業員5万人・56カ国でClaude展開（「customer zero」として自社適用）
  - 規制産業（金融・公共・ライフサイエンス・医療・航空・通信・医療機器）向け業界別オファリング（請求処理・融資アドバイザリ等）
  - Diligenta（TCSの英国生命年金事業）が2,200万以上の契約者向けにClaude適用
  - TCS iONが年間7,500万件以上のアセスメント（1,500都市）でClaude訓練・認証を提供
  - TCSのエンジニアリングチームがClaude Codeエコシステムに再利用可能スキル/プラグインを追加（請求裁定・融資アドバイザリから開始）
- **引用URL:** https://www.anthropic.com/news/tcs-anthropic-partnership
- **Evidence ID:** EVD-20260619-0002

### INFO-003
- **タイトル:** OpenAI Partner Network発表 — エンタープライズAI採用加速へ$150M投資
- **ソース:** OpenAI公式
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05, KIQ-002-02
- **関連企業:** OpenAI
- **要約:** OpenAIがPartner Networkを発表。グローバルパートナーがエンタープライズAIの採用・デプロイ・変革を加速するため$150Mを投資。
- **キーファクト:**
  - Partner Network立ち上げ・$150M投資
  - エンタープライズAI採用・デプロイ・変革支援が目的
- **引用URL:** https://openai.com/index/introducing-openai-partner-network/
- **Evidence ID:** EVD-20260619-0003

### INFO-004
- **タイトル:** OpenAIがOnaを買収 — 長時間実行エージェントのセキュア実行・オーケストレーション強化
- **ソース:** AI News Briefs Bulletin Board (Radical Data Science)
- **公開日:** 2026-06-12
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-003-04
- **関連企業:** OpenAI, Ona
- **要約:** OpenAIがOnaの買収を発表。セキュアなクラウド実行とオーケストレーション機能を持ち込み、長時間実行エージェント（long-running agents）を強化する狙い。
- **キーファクト:**
  - OpenAIがOnaを買収（6/12/2026）
  - 目的: セキュアクラウド実行・オーケストレーションで長時間実行エージェント強化
- **引用URL:** https://radicaldatascience.wordpress.com/2026/06/17/ai-news-briefs-bulletin-board-for-june-2026/
- **Evidence ID:** EVD-20260619-0004

### INFO-005
- **タイトル:** DeepMind・英国政府 — Gemini活用AI加速計画プロトタイプで住宅申請処理を半減目標
- **ソース:** Google DeepMindブログ
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-002-01, KIQ-002-03
- **関連企業:** Google / DeepMind, 英国政府
- **要約:** 英国政府向けにGeminiで構築したAI計画プロトタイプが住宅所有者の申請処理時間を半減させることを目指す。政府部門でのAIエージェント適用の具体例。
- **キーファクト:**
  - Gemini活用の英国政府AI計画プロトタイプ
  - 住宅申請処理時間半減目標
  - 政府部門でのAI適用実例
- **引用URL:** https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/
- **Evidence ID:** EVD-20260619-0005

### INFO-006
- **タイトル:** Google Cloud London Summit 2026 — 英国のエンタープライズエージェントAIを牽引・Gemini 3.5 Flash国内データ居住性
- **ソース:** Google Cloudブログ
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02, KIQ-002-03
- **関連企業:** Google / DeepMind, Google Cloud
- **要約:** Google Cloud London Summit 2026で英国のAIポテンシャルからエージェント現実への転換を強調。英国データ居住性コミットメントを強化し、Gemini 3.5 Flashの国内（in-country）提供を含む。
- **キーファクト:**
  - Gemini 3.5 Flashの英国国内データ居住性提供
  - エンタープライズエージェントAI・インフラ・データクラウド強調
  - UKデータ居住性コミットメント強化
- **引用URL:** https://cloud.google.com/blog/topics/inside-google-cloud/london-summit-2026-uk-leads-agentic-enterprise-ai-infrastructure-data-cloud
- **Evidence ID:** EVD-20260619-0006

### INFO-007
- **タイトル:** June Pixel Drop — Gemini Omni搭載テキストtoビデオ・クリエイター向け新機能
- **ソース:** Google公式ブログ (Pixel Drop)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Google
- **要約:** 6月のPixel Dropでクリエイター向け新機能を提供。Gemini Omniによるテキストtoビデオツール、画面録画機能、マルチタスキング改善を含む。
- **キーファクト:**
  - Gemini Omni搭載テキストtoビデオ
  - 画面録画機能・マルチタスキング改善
- **引用URL:** https://blog.google/products-and-platforms/devices/pixel/june-2026-pixel-drop/
- **Evidence ID:** EVD-20260619-0007

### --- 動的追加クエリ（Arbiterフィードバック Step 1.5）---

### INFO-008 [KIQ-MIL-001: 新規推奨]
- **タイトル:** 米国防総省のチーフAI責任者がGrok使用を認定 — イランOperation Epic Furyで96時間に2,000目標・2,000発弾薬展開
- **ソース:** Common Dreams / Times of Israel
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06
- **関連企業:** xAI (SpaceX子会社), Pentagon (DoD), Project Maven
- **要約:** 国防総省のチーフAI責任者が、米軍がイラン作戦「Operation Epic Fury」（米イスラエル合同）でGrokモデルを使用し「2,000の異なる目標に2,000発以上の弾薬を展開」する支援を行ったと認定。AI支援Mavenシステムが96時間以内にストライクを実行。xAIのColossusデータセンターが軍事AIに不可欠と位置付けられた。前日INFO-013の追証かつ詳細化。
- **キーファクト:**
  - Grok Gov Modelが96時間以内に2,000目標・2,000発弾薬展開を支援（Operation Epic Fury・米イスラエル合同イラン攻撃）
  - AI支援Project Maven標的システムがストライク実行
  - xAI Colossusデータセンターが「軍事AIに不可欠」と位置付け
  - DoJ法廷文書（データセンター汚染問題の弁護）で判明
  - 「AIは補助ツールではなくキルチェーン自体に組み込まれた」複数報道
- **引用URL:** https://www.commondreams.org/news/us-military-grok-iran
- **Evidence ID:** EVD-20260619-0008

### INFO-009 [KIQ-MIL-001: 新規推奨]
- **タイトル:** 上院議員Gillibrand・Slotkin法案 — PentagonのAI核発射・国内監視・完全自律兵器使用禁止
- **ソース:** AIHub / AAAI presidential panel
- **公開日:** 2026-06-15
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-MIL-001, KIQ-005-03, KIQ-002-03
- **関連企業:** 米国政府 (Gillibrand, Slotkin), Pentagon
- **要約:** 上院議員GillibrandとSlotkinが、PentagonがAIを核発射・国内監視・完全自律兵器に使用することを禁止する法案を提出。Gillibrandは「Pentagonは現在、常識的なガードレールなしに非常に強力なAI技術を展開しようとしている。破滅的な結果をもたらしうる」と声明。法案はAIが核兵器や攻撃的自律兵器を「なぜ・どのように・いつ・どこで」使用するかを決定することを禁止するハードリミットを設定。
- **キーファクト:**
  - Gillibrand・Slotkin法案: Pentagonの核発射・国内監視・完全自律兵器でのAI使用禁止
  - AIが「なぜ・どのように・いつ・どこで」核/自律兵器を使用するかの決定を禁止（ハードリミット）
  - Gillibrand「非常識なガードレールなしに強力なAIを展開・破滅的結果」
- **引用URL:** https://aihub.org/2026/06/15
- **Evidence ID:** EVD-20260619-0009

### INFO-010 [KIQ-GOV-002]
- **タイトル:** OpenAI・ChatGPTが2026年7月上旬にGenAI.milでPentagon職員300万人へ提供予定
- **ソース:** WindowsForum / 業界報道
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-GOV-002, KIQ-002-06, KIQ-001-02
- **関連企業:** OpenAI, Pentagon
- **要約:** OpenAIは2026年7月上旬にChatGPTをGenAI.milで利用可能にする準備中。Pentagonの文民・軍人職員最大300万人にアクセスを提供。Pentagonは5月2日にOpenAI・Google・NVIDIA・AWS・Microsoft等6社と同時にAI合意に署名。OpenAIはPentagonの条件を受け入れ（Anthropicが排除されたのと同じ赤線をOpenAIは越えた）。
- **キーファクト:**
  - ChatGPTがGenAI.milで2026年7月上旬提供予定・Pentagon職員最大300万人アクセス
  - Pentagon 5月2日に6社（OpenAI・Google・NVIDIA・AWS・Microsoft等）と同時AI合意署名
  - OpenAIはPentagonの条件（Anthropicが排除された赤線）を受け入れ
  - Bloomberg報道: 「OpenAIは条件を交渉し、PentagonはOpenAIの条件を受け入れた」
- **引用URL:** https://windowsforum.com/threads/chatgpt-on-genai-mil-how-early-july-2026-brings-secure-ai-to-the-pentagon.427137/
- **Evidence ID:** EVD-20260619-0010

### INFO-011 [KIQ-OAI-001/002]
- **タイトル:** Anthropic年間収益2026年5月に$470億到達・OpenAIを逆転継続 — B2B契約主導
- **ソース:** LinkedIn / Stackademic分析
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-OAI-001, KIQ-OAI-002, KIQ-003-04
- **関連企業:** Anthropic, OpenAI
- **要約:** Anthropicの年間収益ランレートが2026年5月に$470億に到達し、OpenAI（$330億）の逆転を継続。12カ月未満で$40億→$470億に成長。B2B契約が主導。地球上の最大10社のうち8社が有料顧客。OpenAIは年$140億を燃やしている。一方でAnthropicは2028年に黒字化予想・OpenAIは2030年代。
- **キーファクト:**
  - Anthropic年間収益ランレート: 2026年4月$300億→5月$470億（12カ月未満で$40億→$470億）
  - OpenAI: 中期2026 $330億（Anthropicが逆転継続）
  - 地球上の最大10社のうち8社がAnthropic有料顧客
  - OpenAIは年$140億燃焼・Anthropicも現金燃焼中だが収益成長率高
  - Anthropic 2028年黒字化予想 vs OpenAI 2030年代
- **引用URL:** https://www.linkedin.com/posts/ritveekgrover_ritveek-grover-marketing-systems-that-turn-activity-7471753023032164352-47Uo
- **Evidence ID:** EVD-20260619-0011

### INFO-012 [KIQ-OAI-001/002]
- **タイトル:** Claude Code採用9カ月で3%→全米24%・世界18% — JetBrains開発者調査1万人
- **ソース:** JetBrains Global Developer Survey (via Fleapo)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-OAI-001, KIQ-004-02, KIQ-001-01
- **関連企業:** Anthropic, JetBrains
- **要約:** JetBrainsの1万人以上の開発者を対象としたグローバル調査で、Claude Codeの採用が9カ月で3%→18%（世界）・24%（米国）に急拡大。ClaudeのMAUは2026年3月に1.8億に急増。Cursorのエンタープライズ収益シェアは2024年の個人中心から2026年に60%に成長（ボトムアップ採用）。第三者調査機関によるClaude Code採用の定量化。
- **キーファクト:**
  - Claude Code採用: 9カ月で3%→18%（世界）・24%（米国）— JetBrains調査1万人
  - Claude MAU 2026年3月に1.8億へ急増
  - Cursorエンタープライズ収益シェア: 2024年個人中心→2026年60%（ボトムアップ）
  - Claude Codeエンタープライズ平均コスト: $13/開発者/アクティブ日・$150-250/開発者/月
- **引用URL:** https://www.facebook.com/fleapo/posts/as-per-jetbrains-global-developer-survey-of-10000-developers-claude-code-went-fr/1434664075346463/
- **Evidence ID:** EVD-20260619-0012

### INFO-013 [KIQ-BTD-001]
- **タイトル:** 豆包APPと抖音APPの重複ユーザー3.3億人に到達 — QuestMobile 2026年5月
- **ソース:** QuestMobile (36kr)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-BTD-001, BYTEDANCE-CHINESE
- **関連企業:** ByteDance (豆包/Doubao, 抖音/Douyin)
- **要約:** QuestMobileデータで2026年5月時点、豆包APPと抖音APPの重複ユーザーが3.3億人に到達。千問APPと淘宝APPの重複は1.47億人。ByteDanceのエコシステム内での豆包（Doubao）の浸透が抖音との連携で拡大中。
- **キーファクト:**
  - 豆包×抖音重複ユーザー: 3.3億人（2026年5月・QuestMobile）
  - 千問×淘宝重複ユーザー: 1.47億人
  - ByteDanceエコシステム内浸透拡大（抖音連携）
- **引用URL:** https://eu.36kr.com/en/p/3855204672574728
- **Evidence ID:** EVD-20260619-0013

### INFO-014 [KIQ-004-01]
- **タイトル:** NVIDIAがArtificial Analysis AgentPerf初のエージェント型コーディングベンチマークで首位 — AWS Agent-EvalKitと並ぶ評価基盤
- **ソース:** Develeap / Search Marketing Italia
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-01, KIQ-001-01, KIQ-003-02
- **関連企業:** NVIDIA, AWS, Allen AI
- **要約:** NVIDIAがArtificial Analysis AgentPerf（初のマルチエージェント型ベンチマーク）で首位のエージェント型コーディング性能を達成。AWS Agent-EvalKit（Apache 2.0 OSS）は実行パス・ツール呼び出し・完全トレースを評価するエージェント評価インフラ。NVIDIA・Allen AI・AWSが異なるエージェントベンチマークを提案し、比較の妥当性リスクが指摘される。
- **キーファクト:**
  - NVIDIA: Artificial Analysis AgentPerf（初のマルチエージェント型ベンチマーク）で首位
  - AWS Agent-EvalKit: Apache 2.0 OSS・実行パス・ツール呼び出し完全トレースで評価
  - NVIDIA・Allen AI・AWSの3者が異なるエージェントベンチマーク提案・比較妥当性リスク
- **引用URL:** https://www.develeap.com/news/agent-bricks-data-ai-summit-2026-f8bddf26/
- **Evidence ID:** EVD-20260619-0014

### INFO-015 [KIQ-GOV-002]
- **タイトル:** Google倫理ポリシー変更 — AIの兵器・監視使用拒否誓約を削除
- **ソース:** Facebook/John Daly (G7報道引用)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-GOV-002, KIQ-002-06, KIQ-005-03
- **関連企業:** Google
- **要約:** Googleが倫理ポリシーを更新し、AIを兵器や監視に使用しないという既存の誓約を削除。G7首脳がAIの未来と米国産業支配を議論する中で判明。これはAnthropic排除後の「順応報酬」構造の一環として、主要プレイヤーが安全性制約を解除した具体的事例。
- **キーファクト:**
  - GoogleがAI兵器・監視使用拒否誓約を倫理ポリシーから削除
  - G7首脳会議でAI未来・米国産業支配議論と同時期
  - 順応報酬構造の具体例（安全性制約解除）
- **引用URL:** https://www.facebook.com/johndalyfanpage/posts/live-updates-trump-and-g7-leaders-will-discuss-contentious-future-of-ai-and-us-d/1626344966159784/
- **Evidence ID:** EVD-20260619-0015

### --- KIQ-001-01: 各社のAgent SDK/APIの機能拡張ロードマップ ---

### INFO-016
- **タイトル:** AnthropicがAgent SDKサブスクリプション変更を当日に一時停止 — 6月15日予定の独立クレジット移行を保留
- **ソース:** The New Stack / Reddit
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Anthropicは5月13日に、自動化Agent SDK使用量を6月15日から独立した月次クレジットに移行すると発表したが、その当日に変更を一時停止（pause）。現在は何も変わらず: Agent SDK・claude -p使用量は従来のサブスクリプション制限から引き出される。開発者コミュニティで混乱が生じていた。
- **キーファクト:**
  - 5/13発表: 6/15からAgent SDK自動使用量を独立月次クレジットへ移行
  - 当日一時停止（pause）・「現状維持・何も変わらず」
  - プログラマティック/非インタラクティブ使用量を通常サブスクから分離する計画
  - 開発者コミュニティで「新Agent SDKクレジット構造」理解に混乱
- **引用URL:** https://thenewstack.io/anthropic-pauses-claude-agent-sdk-subscription-change/
- **Evidence ID:** EVD-20260619-0016

### INFO-017
- **タイトル:** xAI「Agent Dashboard」in Grok Build — 全セッションを1画面で並列実行・介入
- **ソース:** xAI公式 / xAI Docs
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI (SpaceX子会社)
- **要約:** xAIがGrok BuildにAgent Dashboardを追加。各Grok Buildセッションを1画面に集約し、並列実行・入力が必要な時のみ介入可能。Grok BuildはインタラクティブTUI・ヘッドレス・Agent Client Protocol経由で利用可能なコーディングエージェント。Voice Agent API（ツール設定可能な音声エージェント）も提供。
- **キーファクト:**
  - Agent Dashboard: 全Grok Buildセッション1画面集約・並列実行・要時介入
  - Grok Build: TUI・ヘッドレス・Agent Client Protocol経由のコーディングエージェント
  - Voice Agent API: ツール設定可能な音声エージェント
  - Grok 4でプラットフォームネイティブ・マルチエージェント推論システム化
- **引用URL:** https://x.ai/news/agent-dashboard
- **Evidence ID:** EVD-20260619-0017

### INFO-018
- **タイトル:** Google「Gemini Enterprise Agent Platform」API・Agent Platform API公開
- **ソース:** Google Cloud Documentation / Google AI for Developers
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Google CloudがGemini Enterprise Agent Platformを公開。APIキー認証でAgent Platformリソース管理。Gemini APIは第2世代ワークホースモデルでネイティブツール使用・1Mトークンコンテキスト対応。gemini-skills（GitHub）でテキスト生成・関数呼び出し・構造化出力等のスキル提供。Firebase AI Logic SDKでクライアントから直接Gemini API呼び出し。
- **キーファクト:**
  - Gemini Enterprise Agent Platform: APIキー認証・Agent Platformリソース管理
  - 第2世代モデル: ネイティブツール使用・1Mトークンコンテキスト
  - gemini-skills (GitHub): テキスト生成・マルチターン・関数呼び出し・構造化出力
  - Firebase AI Logic SDK: アプリから直接Gemini API呼び出し
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest
- **Evidence ID:** EVD-20260619-0018

### INFO-019
- **タイトル:** OpenAI Apps SDK更新 — 接続アプリの権限リクエスト粒度制御（常時/変更前/重要変更前のみ）
- **ソース:** OpenAI Developers Changelog
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI Apps SDKのchangelog更新。接続アプリが権限を求めるタイミングをChatGPTユーザーが選択可能に: 常時・変更を加える前・重要な変更の前のみ。Responses APIで高速Web検索・ドキュメントスキャン等のカスタムエージェント作成を支援。OpenAI Agents SDKは4プリミティブ・MCP統合完全対応。
- **キーファクト:**
  - Apps SDK: 接続アプリの権限タイミングをユーザー選択（常時/変更前/重要変更前のみ）
  - Responses API: 高速Web検索・ドキュメントスキャン・カスタムエージェント作成
  - OpenAI Agents SDK: 4プリミティブ・MCP統合完全対応・最小APIサーフェス
- **引用URL:** https://developers.openai.com/apps-sdk/changelog
- **Evidence ID:** EVD-20260619-0019

### INFO-020
- **タイトル:** GitHub AIエージェント危機 — 2026年4月10件・5月9件のサービス劣化インシデント
- **ソース:** Waxell
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-004-01
- **関連企業:** Microsoft (GitHub), GitHub Copilot
- **要約:** GitHubが2026年5月に9件・4月に10件のサービス劣化インシデントを記録。エンタープライズAIエージェントのSLA/信頼性問題の具体例。エージェントSDKのエンタープライズ展開における稼働率課題を浮き彇うりに。
- **キーファクト:**
  - GitHub: 2026年5月9件・4月10件のサービス劣化インシデント
  - エンタープライズAIエージェントSLA/信頼性問題の具体例
- **引用URL:** https://www.waxell.ai/blog/github-ai-agent-crisis-infrastructure-enforcement-2026
- **Evidence ID:** EVD-20260619-0020

### INFO-021
- **タイトル:** エージェントフレームワーク乱立 — OpenAI Agents SDK・LangGraph・CrewAI・Claude Agent SDK・Google ADK・Mastra等
- **ソース:** Atlan / Substack / Reddit
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI, Anthropic, Google, Microsoft (LangChain)
- **要約:** 2026年のエージェントフレームワーク landscapeは「騒がしい」。主要5選手: LangGraph・CrewAI・Microsoft Agent Framework (AutoGen+Semantic Kernel)・Google ADK・OpenAI Agents SDK。OpenAI Agents SDKは分単位で構築可能だが天井に到達が早い。フレームワーク間比較はストリーミング挙動・ツール呼び出しエルゴノミクス・ソース検査で差異化。
- **キーファクト:**
  - 主要エージェントフレームワーク5: LangGraph・CrewAI・MS Agent Framework・Google ADK・OpenAI Agents SDK
  - OpenAI Agents SDK: 分単位構築・最小APIサーフェス・天井到達早い
  - 比較軸: ストリーミング挙動・ツール呼び出しエルゴノミクス・ソース検査
- **引用URL:** https://atlan.com/know/ai-agent/how-to-choose-agentic-framework-enterprise/
- **Evidence ID:** EVD-20260619-0021

### --- KIQ-001-02: 各社のAgent製品エンタープライズ展開（セキュリティ・SLA・専用サポート）---

### INFO-022
- **タイトル:** ChatGPT Enterprise vs Claude Enterprise機能比較 — FedRAMP対応はMicrosoft Azureが優位
- **ソース:** IntuitionLabs
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI, Anthropic, Microsoft
- **要約:** ChatGPT Enterpriseは標準エンタープライズセキュリティ要件を満たすが、FedRAMP対応デプロイはMicrosoft Azureオファリングより限定的。SOC 2・HIPAA・FedRAMPは規制産業で主要要件。エンタープライズAIガバナンス（監査・権限・アクセスポリシー）がエージェント到達前に組み込まれる。
- **キーファクト:**
  - ChatGPT Enterprise: 標準エンタープライズセキュリティ対応だがFedRAMPはAzureより限定的
  - OWASP Agentic Applications Top 10・HIPAA・FedRAMP・SOC 2が規制要件
  - エンタープライズAIガバナンス（監査・権限・顧客データ境界）がエージェント前段で組み込み
- **引用URL:** https://intuitionlabs.ai/articles/chatgpt-vs-claude-enterprise-comparison
- **Evidence ID:** EVD-20260619-0022

### INFO-023
- **タイトル:** Google Cloud 6月 — スタートアップ向けVertex AI Agent Engine $350kクレジット・Gemini Enterprise全社員エージェント構築
- **ソース:** Google Cloud / Facebook
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Google Cloudが6月にスタートアップ向けプロダクション級AIエージェント構築の技術ガイドを公開。Vertex AI Agent Engineで$350kクレジット提供。Gemini Enterpriseは非技術者でもカスタムAIエージェントを構築・デプロイ・管理できるオールインワンプラットフォーム。FetcherrがGemini Enterprise Agent Platform + BigQueryで市場予測システム構築。
- **キーファクト:**
  - Vertex AI Agent Engine: スタートアップ向け$350kクレジット
  - Gemini Enterprise: 非技術者向けエージェント構築・デプロイ・管理プラットフォーム
  - クラウド依存エージェントはレイテンシ分散・コストスパイクで本番SLA防御困難（エンタープライズ課題）
- **引用URL:** https://www.facebook.com/GoogleCloudIN/posts/its-been-a-massive-month-of-june-for-ai-at-google-cloud-and-we-want-to-make-sure/1330400559276692/
- **Evidence ID:** EVD-20260619-0023

### --- KIQ-001-03: 各社のAgent開発者エコシステム（サードパーティ連携・マーケットプレイス）---

### INFO-024
- **タイトル:** AAIF 170社到達 — Anthropic/OpenAI/Google/AWS/Microsoft共同設立のエージェント標準化財団
- **ソース:** AAIF公式 / Beam AI
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** AAIF (Anthropic, OpenAI, Google, AWS, Microsoft), Vstorm
- **要約:** Agentic AI Foundation (AAIF)が170社に到達。Anthropic・OpenAI・Google・AWS・Microsoftが共同設立。2025年12月にAGENTS.mdをツール非依存のオープン標準として採用。オープン標準群: MCP・Goose・AGENTS.md・agentgateway。エンタープライズと政府のオープンエージェント標準採用が加速中。43新規メンバー追加（5月18日）。中立的ガバナンスで開発者に安定環境提供。
- **キーファクト:**
  - AAIF 170社到達・共同設立5社: Anthropic/OpenAI/Google/AWS/Microsoft
  - AGENTS.md: 2025年12月ツール非依存オープン標準採用（エコシステム単一収束点）
  - オープン標準群: MCP・Goose・AGENTS.md・agentgateway
  - 43新規メンバー追加（5/18）・エンタープライズ・政府採用加速
  - 中立ガバナンス・技術卓越賞でオープン標準推進を評価
- **引用URL:** https://aaif.io/author/aaif/
- **Evidence ID:** EVD-20260619-0024

### INFO-025
- **タイトル:** MCP月間1.1億ダウンロード到達・GitHub/AWS/Docker等公式サーバー — だが本番利用は多数チームで未達
- **ソース:** GitConnected / Medium
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic (MCP), GitHub, AWS, Docker, HashiCorp, Datadog, Google
- **要約:** MCP（Model Context Protocol）が月間1.1億ダウンロードに到達。2026年初頭までにGitHub・AWS・Docker・HashiCorp・Datadog全てが公式MCPサーバーを提供。コミュニティレジストリは数百サーバー。「Anthropicの実験」から業界標準へ移行。だが本番利用はセキュリティ・ガバナンス不足で多数チームが困難。MCP Gateway + AI Registry（OSS）が認証・ガバナンス・自己サービス開発者レジストリで中央集権化。Google Gemini Enterprise Agent PlatformもリモートMCPサーバー提供。
- **キーファクト:**
  - MCP月間1.1億ダウンロード
  - 公式MCPサーバー: GitHub・AWS・Docker・HashiCorp・Datadog（全て提供）
  - コミュニティレジストリ: 数百サーバー・「Anthropic実験」→業界標準へ
  - 本番利用ハードル: 認証・ガバナンス・セマンティック検索不足
  - MCP Gateway + AI Registry (OSS): 中央集権化・認証・ガバナンス
  - Claude MCP Registry: MCPサーバー探索レイヤー（アプリストア的）
- **引用URL:** https://levelup.gitconnected.com/mcp-has-110-million-downloads-a-month-most-teams-still-cant-use-it-in-production-b39b709a3760
- **Evidence ID:** EVD-20260619-0025

### INFO-026
- **タイトル:** Databricks Agent Bricks発表 + SpaceX提携でGrokをDatabricksにネイティブ提供 (Data + AI Summit 2026)
- **ソース:** Databricks公式ブログ
- **公開日:** 2026-06-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-003-04, KIQ-002-01
- **関連企業:** Databricks, SpaceX (xAI)
- **要約:** DatabricksがData + AI Summit 2026でAgent Bricksを発表。SpaceXと提携しGrokモデルをDatabricks上にネイティブ提供。前日報道のSalesforce×Databricks提携（オープンMCP駆動統合・エージェント検索）と並ぶエコシステム拡大。
- **キーファクト:**
  - Agent Bricks発表（Data + AI Summit 2026・6/16）
  - SpaceX提携: GrokモデルをDatabricksにネイティブ提供
  - Salesforce×Databricks提携: オープンMCP駆動統合・エージェント検索（2026年H2以降展開）
- **引用URL:** https://www.databricks.com/blog/agent-bricks-dais-2026
- **Evidence ID:** EVD-20260619-0026

### INFO-027
- **タイトル:** Yahoo DSPがAgent Network立ち上げ — 広告主とAIエージェントを直接接続するオープンフレームワーク
- **ソース:** Yahoo Press
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-05, KIQ-004-01
- **関連企業:** Yahoo, 広告業界
- **要約:** Yahoo DSPがAgent Networkを立ち上げ。主要テクノロジーパートナーのAIエージェントと広告主をYahoo DSP内で直接接続するオープンフレームワーク。広告運用領域でのプラットフォームAI統合・中間事業者侵食の具体例。
- **キーファクト:**
  - Yahoo DSP Agent Network: 広告主とAIエージェントを直接接続するオープンフレームワーク
  - 広告運用のエージェント化・プラットフォーム統合の具体例
- **引用URL:** https://www.yahooinc.com/press/yahoo-dsp-launches-agent-network-opening-the-ai-ecosystem-for-advertisers
- **Evidence ID:** EVD-20260619-0027

### INFO-028
- **タイトル:** Cresta × TELUS Digital提携 — 顧客体験AIエージェント・人間とAIエージェントの統合プラットフォーム
- **ソース:** Cresta Press
- **公開日:** 2026-06-15
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-004-01
- **関連企業:** Cresta, TELUS Digital
- **要約:** Cresta（人間とAIエージェントの統合顧客体験AIプラットフォーム）がTELUS Digital（グローバルデジタル顧客体験技術会社）と提携。AIエージェントと人間担当者の増強を提供。カスタマーサポート領域のAI自律化の具体例。
- **キーファクト:**
  - Cresta × TELUS Digital提携（6/15）
  - 人間とAIエージェント統合の顧客体験プラットフォーム
  - カスタマーサポート領域AI自律化事例
- **引用URL:** https://cresta.com/press/cresta-telus-digital-partnership
- **Evidence ID:** EVD-20260619-0028

### --- KIQ-001-04: 各社のマルチモーダルAgent（音声・視覚・コード実行）統合 ---

### INFO-029
- **タイトル:** マルチモーダル音声エージェントのオーケストレーション層成熟 — STT→LLM→TTSをミリ秒で実行
- **ソース:** AssemblyAI / DeepLearning.AI
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** AssemblyAI, NVIDIA, DeepLearning.AI
- **要約:** AI音声エージェントは音声toテキスト・LLM・テキストto音声の3部構成パイプラインをミリ秒で実行し、オーケストレーション層が調整。DeepLearning.AIが「既存AIエージェントへの音声追加」短期コースを公開（3統合パターン: 組み込み音声・既存エージェントへの音声レイヤー・呼び出し可能ツールとしての音声）。オムニチャネルエージェントビルダーが1設定で音声・チャット・メールに同一エージェント展開。NVIDIA XR AIはARグラス/XRデバイス向け視覚グラウンディング統合エージェントを提供。
- **キーファクト:**
  - 音声エージェント3部パイプライン: STT→LLM→TTS・ミリ秒実行・オーケストレーション層
  - DeepLearning.AI音声追加短期コース（3統合パターン）
  - オムニチャネルビルダー: 1設定で音声・チャット・メール展開
  - NVIDIA XR AI: ARグラス/XRデバイス向け視覚グラウンディングエージェント
- **引用URL:** https://www.assemblyai.com/blog/orchestration-tools-ai-voice-agents
- **Evidence ID:** EVD-20260619-0029

### INFO-030
- **タイトル:** MLCommons MLPerf Training v6.0 — 初のエージェント型AIインフラベンチマーク・2つの新MoEベンチマーク
- **ソース:** MLCommons / NVIDIA
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** MLCommons, NVIDIA
- **要約:** MLCommonsがMLPerf Training v6.0結果を公開。2つの新MoE（Mixture-of-Experts）ベンチマークと初のエージェント型AIインフラベンチマークを導入。24組織・13ハードウェアアクセラレータ・95固有システム。AIエージェントが数十のツールを連鎖するハードウェア/ソフトウェア速度を評価。
- **キーファクト:**
  - MLPerf Training v6.0: 2つの新MoEベンチマーク + 初のエージェント型AIインフラベンチマーク
  - 24組織・13ハードウェアアクセラレータ・95固有システム
  - エージェント型インフラ: AIエージェントが数十ツールを連鎖する速度評価
- **引用URL:** https://mlcommons.org/2026/06/mlperf-training-v6-0-results/
- **Evidence ID:** EVD-20260619-0030

### INFO-031
- **タイトル:** オムニモーダル長動画推論ベンチマーク — Gemini 3.1 Pro Preview最高でも55.63%・大幅な改善余地
- **ソース:** arXiv
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02, KIQ-005-01
- **関連企業:** Google / DeepMind
- **要約:** オムニモーダル長動画推論ベンチマークで、最強のクローズドソースGemini 3.1 Pro Previewでも55.63%にとどまり、全モデルで大幅な改善余地を示す。マルチモーダル統合（音声・視覚）の客観的限界を示すデータ。
- **キーファクト:**
  - オムニモーダル長動画推論ベンチマーク: Gemini 3.1 Pro Preview（最高クローズド）でも55.63%
  - 全モデルで大幅改善余地・マルチモーダル統合の客観的限界
- **引用URL:** https://arxiv.org/html/2512.16978v2
- **Evidence ID:** EVD-20260619-0031

### INFO-032
- **タイトル:** LMCouncil AIモデルベンチマーク2026年6月 — GPT-5.5・Claude Opus・Gemini 3・Grok 4 + 30フロンティアモデル比較
- **ソース:** LMCouncil / Epoch AI / Scale AI
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** LMCouncilがEpoch AI・Scale AIデータでGPT-5.5・Claude Opus・Gemini 3・Grok 4と30以上のフロンティアモデルを横断比較する包括的ベンチマーク集を公開。2026年6月時点のフロンティアモデル性能比較の統合的リソース。
- **キーファクト:**
  - 30+フロンティアモデル横断比較（GPT-5.5・Claude Opus・Gemini 3・Grok 4含む）
  - Epoch AI・Scale AIデータ活用
- **引用URL:** https://lmcouncil.ai/benchmarks
- **Evidence ID:** EVD-20260619-0032

### --- KIQ-001-05: 各社の「スキル配布と実行環境」設計・ロックイン ---

### INFO-033
- **タイトル:** NVIDIA「OpenShell」— 自律AIエージェント向けセーフ・プライベート実行ランタイム（サンドボックス）
- **ソース:** NVIDIA GitHub (OpenShell)
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-01
- **関連企業:** NVIDIA
- **要約:** NVIDIAがOpenShellを公開。自律AIエージェント向けのセーフ・プライベート実行ランタイム。サンドボックス実行環境でデータ・資格情報・システムを保護。OpenAI Skills/Shellの実行環境アプローチに対する中立・OSS対抗。エージェント実行環境のベンダーロックイン回避手段。
- **キーファクト:**
  - OpenShell: 自律AIエージェント向けセーフ・プライベート実行ランタイム
  - サンドボックス実行環境・データ/資格情報/システム保護
  - OSS・中立実行環境（OpenAI Skills/Shellロックインへの対抗）
- **引用URL:** https://github.com/NVIDIA/OpenShell
- **Evidence ID:** EVD-20260619-0033

### INFO-034
- **タイトル:** エージェントスキルマーケットプレイス乱立 — VoltAgent・Awesome Claude Skills・Promptfoo Red Teaming
- **ソース:** GitHub / Promptfoo / RemoteOpenClaw
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Anthropic, VoltAgent, Promptfoo, Replicate
- **要約:** エージェントスキルのマーケットプレイス/ディレクトリが乱立。VoltAgent awesome-agent-skills（キュレーション集）・Awesome Claude Skills（Claude Agent Skills ディレクトリ）・Promptfoo（評価・レッドチーミング用Agent Skills）。Google gemini-skillsはエージェントにコンテキスト追加する軽量技術。AIエージェント価格は2026年でOSS自己ホスト無料〜$200+/月の幅。クロスプラットフォーム標準化（AAIF/AGENTS.md）とベンダー固有スキルの対立構造。
- **キーファクト:**
  - スキルディレクトリ乱立: VoltAgent・Awesome Claude Skills・Promptfoo Agent Skills
  - Google gemini-skills: エージェントへコンテキスト追加の軽量技術
  - AIエージェント価格幅: OSS自己ホスト無料〜$200+/月
  - クロスプラットフォーム標準（AAIF/AGENTS.md）vs ベンダー固有スキルの対立
- **引用URL:** https://github.com/VoltAgent/awesome-agent-skills
- **Evidence ID:** EVD-20260619-0034

### INFO-035
- **タイトル:** エージェント型コマースのロックイン — 切替コストが初期委任決定を不可逆化（研究論文）
- **ソース:** ResearchGate / Gartner / Kai Waehner Blog
- **公開日:** 2026-06-15
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** (業界横断)
- **要約:** エージェント型コマースでの切替コストが初期の消費者委任決定を逆転困難にし、ロックインを作るという研究。Gartnerデータでエグレス料金がエンタープライズクラウド請求の10-15%を消費。Model Control Layer（Divyam.AI等）が単一モデル/ベンダーへの依存に対するレジリエンス提供。ERP領域で「アジェンティックAIがベンダーロックインメカニズムとして機能」。
- **キーファクト:**
  - エージェント型コマース: 切替コストが初期委任決定を不可逆化・ロックイン創出
  - エグレス料金: エンタープライズクラウド請求の10-15%消費（Gartner）
  - Model Control Layer: 単一モデル/ベンダー依存へのレジリエンス・コスト削減
  - ERP領域: アジェンティックAIがベンダーロックインメカニズムとして機能
- **引用URL:** https://www.researchgate.net/publication/407138018_When_AI_Agents_Spend_Your_Money_Card_Rails_Stablecoins_and_the_Coming_Lock-In_of_Agentic_Commerce
- **Evidence ID:** EVD-20260619-0035

### --- KIQ-002-01: 主要クラウドプロバイダー（AWS, Azure, GCP）のAI Agent統合 ---

### INFO-036
- **タイトル:** AWS Bedrock AgentCore大幅アップグレード — Web検索ツール・SharePoint/Drive/S3横断エンタープライズ知識推論
- **ソース:** AWS News Blog / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01
- **関連企業:** Amazon / AWS
- **要約:** AWSがAmazon Bedrock AgentCoreの全エージェントに大幅アップグレード。エージェントがSharePoint・Drive・S3上のエンタープライズ知識を横断して推論可能に。Web Search on Bedrock AgentCore（完全マネージドツール・引用付きWeb知識で根拠付け）を導入。会話型ビルダーでエージェント構成・ナレッジベースIAM権限管理。
- **キーファクト:**
  - Bedrock AgentCore: 全エージェント大幅アップグレード
  - SharePoint/Drive/S3横断エンタープライズ知識推論
  - Web Search on AgentCore: 完全マネージド・引用付き根拠付け（ゼロ設定）
  - 会話型ビルダー・ナレッジベースIAM権限管理
- **引用URL:** https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/
- **Evidence ID:** EVD-20260619-0036

### INFO-037
- **タイトル:** Azure AI Foundry Agent Service — MCP統合・ホステッドエージェント（プレビュー）でコンテナ化エージェント管理
- **ソース:** Microsoft Learn / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-03
- **関連企業:** Microsoft
- **要約:** Azure AI Foundry Agent Serviceがエージェント構築・管理環境を提供。Azure API Managementがエージェントアクセスのセキュアゲートウェイ。ホステッドエージェント（プレビュー）でコンテナ化エージェントをマネージドホスティング・スケーリング・観測性でデプロイ。MCP・Agentforce 3でエージェント相互運用性が焦点。Copilot Studio（検索/タスクエージェント・Azure AI Search統合）vs Azure AI Foundry（エンタープライズDB/ERP/CRM/ナレッジベース統合）の役割分担。
- **キーファクト:**
  - Azure AI Foundry Agent Service: MCP統合・エージェント構築/管理
  - ホステッドエージェント（プレビュー）: コンテナ化エージェント・マネージドホスティング/スケーリング/観測性
  - Azure API Management: セキュアゲートウェイ
  - Copilot Studio vs Foundry役割分担（検索/タスク vs エンタープライズシステム統合）
- **引用URL:** https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents
- **Evidence ID:** EVD-20260619-0037

### INFO-038
- **タイトル:** Gartner 2026 Hype Cycle — AIエージェント展開は17%のみ・60%以上が2年内展開予定
- **ソース:** MightyBot (Gartner引用)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01, KIQ-002-02
- **関連企業:** Gartner
- **要約:** Gartnerの2026 Agentic AI Hype Cycleで、現在AIエージェントをデプロイ済みの組織は17%のみだが、60%以上が2年以内にデプロイ予定。AIエージェント市場マップが全カテゴリで急拡大。エンタープライズ採用の期待-実態ギャップ（前日IND-026参照）の定量化。
- **キーファクト:**
  - Gartner 2026: AIエージェント展開済み組織17%のみ・60%以上が2年内展開予定
  - 期待-実態ギャップの定量化
- **引用URL:** https://mightybot.ai/blog/ai-automation-agents-market-maps-gone-wild/
- **Evidence ID:** EVD-20260619-0038

### INFO-039
- **タイトル:** AIコーディングエージェント2026年比較 — OpenAI Codex 83.4%・Claude Code 78.9% (Terminal-Bench 2.1)
- **ソース:** MorphLLM
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-01, KIQ-003-02, KIQ-004-02
- **関連企業:** OpenAI, Anthropic
- **要約:** 12のAIコーディングエージェントをベンチマーク+価格で比較ランキング。OpenAI Codex（CLI+IDE+Cloud）がTerminal-Bench 2.1で83.4%、Claude Code（CLI+IDE+Desktop）が78.9%。AgentPerf（Artificial Analysis・業界初エージェント型AIベンチマーク）で開発者/エンタープライズ/インフラ提供者が比較可能。
- **キーファクト:**
  - OpenAI Codex: Terminal-Bench 2.1 83.4%（CLI+IDE+Cloud）
  - Claude Code: Terminal-Bench 2.1 78.9%（CLI+IDE+Desktop）
  - AgentPerf (Artificial Analysis): 業界初エージェント型AIベンチマーク
- **引用URL:** https://www.morphllm.com/best-ai-coding-agents-2026
- **Evidence ID:** EVD-20260619-0039

### --- KIQ-002-02: エンタープライズ顧客のAI Agent採用率とユースケース ---

### INFO-040
- **タイトル:** 96%の組織がアジェンティックAI展開でROI期待を達成・上回る — 2026年調査（54%達成・42%上回る）
- **ソース:** Globe and Mail (調査リリース)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-004-04
- **関連企業:** (業界横断)
- **要約:** アジェンティックAIをアクティブ展開する組織の96%が、ROI期待を達成（54%）または上回る（42%）と報告。従業員生産性向上が主な成果。ただしCX領域では74%のロールバック率との矛盾データも（Gspann）。AIエージェントフリートは2025年12月からほぼ倍増（Gravitee）。セキュリティ信頼は上昇したが監視カバレッジ・説明責任構造・事前デプロイレビューにギャップ。
- **キーファクト:**
  - 96%がROI期待達成(54%)・上回る(42%) — アジェンティックAIアクティブ展開組織
  - CX領域: 74%ロールバック率（ROI vs ロールバックの二面性）
  - AIエージェントフリート: 2025年12月からほぼ倍増
  - セキュリティ信頼上昇だが監視/説明責任/事前デプロイレビューにギャップ
  - Microsoft Security統合: 124% ROI（Forrester・侵害確率最大30%削減）
- **引用URL:** https://www.theglobeandmail.com/investing/markets/stocks/SOUN/pressreleases/2537079/research-finds-96-of-organizations-report-that-agentic-ai-deployments-met-or-exceeded-roi-expectations-in-2026/
- **Evidence ID:** EVD-20260619-0040

### --- KIQ-002-03: 規制環境（EU AI Act・米国・中国）のエンタープライズ影響 ---

### INFO-041
- **タイトル:** G7首脳会議 — Altman・Amodei・Hassabisがボット/エージェント責任・AI真偽議論・Anthropic制限で同盟国間緊張
- **ソース:** Bloomberg Business / Instagram
- **公開日:** 2026-06-17
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03, KIQ-002-06
- **関連企業:** OpenAI, Anthropic, Google / DeepMind, G7各国
- **要約:** G7サミットでSam Altman（OpenAI）・Dario Amodei（Anthropic）・Demis Hassabis（Google DeepMind）がAIワーキングランチに参加。ボット/エージェントの責任・AIが真実と虚偽をどう提示するかを議論。米国がAnthropicの最先端モデルへのアクセスを制限した決定が同盟国間で緊張を引き起こし、議論の焦点に。
- **キーファクト:**
  - G7 AIワーキングランチ: Altman・Amodei・Hassabis参加
  - 議題: ボット/エージェント責任・AI真偽提示
  - 米国のAnthropic最先端モデルアクセス制限が同盟国間緊張の焦点
- **引用URL:** https://www.instagram.com/reel/DZsKat8FHal/
- **Evidence ID:** EVD-20260619-0041

### INFO-042
- **タイトル:** EU AI Act高リスク期限延期 — 2026年8月2日→2027年12月2日（信用スコア・保険料金・顧客関連システム）
- **ソース:** Rasa / Bates Zv6ze (LinkedIn)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** EU
- **要約:** EU AI Actの高リスクシステム（信用スコアリング・保険料金・特定の顧客関連システム等のユースベースシステム）期限が2026年8月2日から2027年12月2日に延期。ただし2026年5月の合意は暫定的政治合意であり、最終公布修正法ではない。複数の要約がテキスト未確定を指摘。
- **キーファクト:**
  - EU AI Act高リスク期限: 2026/8/2→2027/12/2に延期（信用スコア・保険料金・顧客関連）
  - 2026年5月合意は暫定政治合意・最終公布修正法ではない
  - テキスト未確定・複数要約が注意喚起
- **引用URL:** https://rasa.com/blog/what-the-eu-ai-act-update-means-for-european-data-sovereign-organizations
- **Evidence ID:** EVD-20260619-0042

### INFO-043
- **タイトル:** 中国CSRC「テクノロジーハイプ」投機取り締まり強化・杭州裁判所「AI代替のための解雇不可」判決
- **ソース:** CNBC / Instagram
- **公開日:** 2026-06-17
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-004-01
- **関連企業:** 中国 (CSRC), 中国裁判所
- **要約:** 中国証券監督管理委員会（CSRC）がテクノロジーテーマに便乗した違法な市場活動・株価ハイプを取り締まる方針を表明・AI株選びを非難。一方、2026年4月に杭州の裁判所が「企業はAIで置き換えるためだけに従業員を解雇できない」と判決（AI使用は…）。労働保護とAI規制の交差点。
- **キーファクト:**
  - CSRC: テクノロジーハイプ投機取り締まり強化・AI株選び非難
  - 杭州裁判所(2026/4): AI代替目的のみの解雇不可判決
  - 労働保護×AI規制の交差点
- **引用URL:** https://www.cnbc.com/2026/06/17/china-securities-regulator-csrc-artificial-intelligence-investing-stocks-.html
- **Evidence ID:** EVD-20260619-0043

### INFO-044
- **タイトル:** AIガバナンスの法的基盤変化 — エージェントは時間経過で行動・コンテキスト保持・下流結果誘発→静的モデル監査から継続レビューへ
- **ソース:** Epstein Becker Green / OECD Digital Government Outlook
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** OECD各国
- **要約:** エージェントは時間経過で行動し・コンテキストを保持し・下流の結果を誘発するため、ガバナンスは静的モデルの監査から継続的レビューへ移行する必要がある（法的見解）。OECD 36カ国中35カ国（97%）が政府の少なくとも1領域でAI使用・内部プロセスと公共サービスで最強の取り組み。SOC 2・ISO 27001・EU AI Act・NIST AI RMFが主要コンプライアンス枠組み。
- **キーファクト:**
  - エージェント特性: 時間経過行動・コンテキスト保持・下流結果誘発→継続レビュー必要
  - OECD: 36カ国中35カ国(97%)が政府でAI使用
  - 主要枠組み: SOC 2・ISO 27001・EU AI Act・NIST AI RMF
- **引用URL:** https://www.ebglaw.com/insights/publications/ai-governance-is-the-legal-foundation-what-employers-and-boards-need-to-know-in-2026
- **Evidence ID:** EVD-20260619-0044

### --- KIQ-002-06: 政府・軍のAI企業への経済的圧力と萎縮効果 ---

### INFO-045
- **タイトル:** Anthropic-Pentagon対立の核心 — Pentagonが「いかなる合法的使用」無制限アクセス要求・Anthropicは大量監視・自律兵器の赤線維持を拒否
- **ソース:** Built In / DW / Boston Globe
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, Pentagon (DoD), Microsoft
- **要約:** PentagonはAnthropicのAIツールの「いかなる合法的使用（any lawful use）」を求め、無制限アクセスを要求。Anthropicは2点（大量国内監視・自律兵器）の赤線削除を拒否し、$200M/2年契約から撤退。CEO Amodeiは安全性原則を優先。MicrosoftがAnthropicを支援し供給 chain risk指定を阻止しようとした。Boston Globeは「殺人のビジネスから脱却すべき」と評。
- **キーファクト:**
  - Pentagon要求: 「いかなる合法的使用」無制限アクセス・制限なし
  - Anthropic拒否赤線: 大量国内監視・自律兵器（2点）
  - $200M/2年契約から撤退・Amodeiが安全性原則優先
  - MicrosoftがAnthropic支援・供給 chain risk指定阻止試み
  - Boston Globe「殺人のビジネスから脱却すべき」
- **引用URL:** https://builtin.com/articles/anthropic-pentagon-claude-dispute
- **Evidence ID:** EVD-20260619-0045

### INFO-046
- **タイトル:** Trump政権がAnthropicに「供給 chain risk」指定 — 米国企業への前例なき適用・全連邦機関に使用停止命令
- **ソース:** CNN / Washington Post / Bloomberg / NY Times Opinion
- **公開日:** 2026-06-13
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, 米国政府 (Trump政権), Microsoft
- **要約:** Trump政権は全米連邦機関にAnthropic AI技術の使用停止を命じ、重大な制裁を課した。「供給 chain risk」指定は通常外国敵対国家関連企業に reserved されるものだが、Anthropicに適用（米国企業への前例なき適用）。NY Timesは「以前は外国企業を排除するためだけに使われたラベル」と指摘。Anthropicは最先端モデルFable 5/Mythos 5の全外国人へのアクセスを政府命令で停止。超党派の下院議員グループがTrump政権に回答を要求。
- **キーファクト:**
  - 「供給 chain risk」指定: 外国敵対企業向け→米国企業(Anthropic)に前例なき適用
  - 全連邦機関にAnthropic AI使用停止命令
  - Fable 5/Mythos 5: 全外国人アクセス停止（政府命令・国家安全保障理由）
  - MicrosoftがAnthropic支援・指定阻止試み
  - 超党派下院議員がTrump政権に回答要求
- **引用URL:** https://www.cnn.com/2026/06/13/business/anthropic-mythos-model-national-security
- **Evidence ID:** EVD-20260619-0046

### INFO-047
- **タイトル:** Defense Production Act発動検討 — AI企業に国家安全保障のためのサービス提供を強制
- **ソース:** Washington Post / Firstpost / Cairo Review
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** 米国政府 (Trump政権), Anthropic
- **要約:** 防衛生産法（DPA・1950年制定）を発動し、実質的に企業に国家安全保障のためのサービス提供を強制する動き。2023年Biden大統領令はDPA権限で強力な基盤モデル開発者に共有を要求した前例。「矛盾」: Amodeiが安全性を主張する一方でDPAで強制される構造。WashingtonとBeijingがAIラボを国有化するかの議論。
- **キーファクト:**
  - DPA(1950年)発動検討: 企業に国家安全保障サービス提供を強制
  - 2023年Biden令: DPA権限で基盤モデル開発者に共有要求の前例
  - Amodei安全性主張 vs DPA強制の「矛盾」
  - Washington/BeijingのAIラボ国有化可能性議論
- **引用URL:** https://www.facebook.com/washingtonpost/posts/a-bipartisan-group-of-house-lawmakers-demanded-answers-from-the-trump-administra/1379440637381141/
- **Evidence ID:** EVD-20260619-0047

### INFO-048
- **タイトル:** OpenAIがAnthropic排除と同日にPentagon契約 — 類似の赤線だが「技術的セーフガード」で受諾・競合排除の漁夫の利
- **ソース:** MSU Exponent / Washington Post
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-OAI-001
- **関連企業:** OpenAI, Anthropic, Pentagon
- **要約:** OpenAIのSam Altmanは、政権がAnthropicのAIツールを禁止し「供給 chain risk」と指定した同じ日にPentagonと契約。Anthropicと類似の赤線だが「技術的セーフガード」を使用して受諾。PentagonはAnthropicの条件（OpenAIが受け入れた）を受け入れた。これは「順応企業が報われる・安全性堅持企業が罰せられる」構造の典型例。150万の国防総省職員が軍のAIを使用中。
- **キーファクト:**
  - OpenAI-Pentagon契約: Anthropic排除・SCR指定と同日
  - 類似赤線だが「技術的セーフガード」で受諾
  - PentagonはOpenAIの条件を受諾（Bloomberg「彼はPentagonと取引し、PentagonはOpenAIの条件を受け入れた」）
  - 150万国防総省職員が軍のAI使用中
  - 順応報酬構造の典型例
- **引用URL:** https://www.msuexponent.com/news/national/openai-strikes-pentagon-deal-with-safeguards-as-trump-dumps-anthropic/article_acb67662-ddc1-5f29-a07d-ed3298a6d057.html
- **Evidence ID:** EVD-20260619-0048

### INFO-049
- **タイトル:** GoogleがPentagonとAI契約 — 従業員反発にも関わらず分類作業で使用・200団体がAI兵器禁止要求
- **ソース:** Reddit / New Scientist / ControlProblem
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Google, Pentagon
- **要約:** GoogleがPentagonとAI契約を締結（従業員の反発にもかかわらず）。米軍が分類作業でGoogleのAIモデルを使用可能に。同時に200以上の団体がAIの（軍事）使用禁止を要求。Trump大統領はAI企業を州規制からブロックする大統領令に署名。New Scientistは「完全自律兵器の脅威を無視できなくなった」と警告。
- **キーファクト:**
  - Google-Pentagon AI契約: 従業員反発も分類作業で使用許可
  - 200+団体がAI軍事使用禁止要求
  - Trump大統領令: AI企業を州規制からブロック
  - New Scientist「完全自律兵器脅威無視不可」
- **引用URL:** https://www.reddit.com/r/technology/comments/1u7vuwn/15_million_defense_department_workers_are_now/
- **Evidence ID:** EVD-20260619-0049

### INFO-050
- **タイトル:** 政府「キルスイッチ」懸念 — AIシステムを抑圧する権力・安全性主張企業への萎縮効果
- **ソース:** Eternally Radical Idea / Federal News Network
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** 米国政府
- **要約:** 政府がAIシステムに対する「キルスイッチ」を主張 — 政府の好みの見解に矛盾する・政府職員を恥かせる・政府権限を脅かすモデルを抑圧する権力。これは安全性姿勢を持つ企業への萎縮効果を生む。連邦職員は「ルールが変われば働き方が変わる」— 問題のある行動に対して声を上げることを躊躇させる可能性。
- **キーファクト:**
  - 政府「キルスイッチ」: 好みの見解に矛盾するAIモデル抑圧権力
  - 安全性主張企業への萎縮効果
  - 連邦職員: 問題行動への声上げ躊躇リスク
- **引用URL:** https://eternallyradicalidea.com/p/the-online-safety-trap
- **Evidence ID:** EVD-20260619-0050

### --- KIQ-002-04: AIエージェント業務自律化の進展業界・職種 ---

### INFO-051
- **タイトル:** AIエージェントは実世界プロ業務の5%未満しか完遂不可 — Agent's Last Exam 1,500タスク55職種・専門家とのペアで70%向上
- **ソース:** HCAMag / The New Stack / Medium
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01, KIQ-005-01
- **関連企業:** METR, Agent's Last Exam
- **要約:** 最先端AIエージェントでも実世界のプロフェッショナル業務を端から端まで完遂できるのは5%未満（研究）。Agent's Last Examは55職種・1,500以上の実世界タスクでベンチマーク。だが専門家とのペアリングで完了率が最大70%向上 — 近未来の処方は人間+エージェントであって代替ではない。METRは50%信頼性で完了するタスクの時間ホライゾンが約7カ月ごとに倍増と測定。大企業の65%がHRでAIエージェント使用を主張するが、真の自律エージェント展開は15%未満。
- **キーファクト:**
  - AIエージェント: 実世界プロ業務端から端まで完遂5%未満
  - Agent's Last Exam: 55職種・1,500+実世界タスク
  - 専門家+エージェントペアリング: 完了率最大70%向上（代替でなく協調）
  - METR: 50%信頼性完了タスク時間ホライゾン約7カ月毎倍増
  - 大企業65%がHR AIエージェント主張だが真の自律展開15%未満
- **引用URL:** https://www.hcamag.com/ca/news/general/your-ai-agent-isnt-as-capable-as-you-think-research-finds/579144
- **Evidence ID:** EVD-20260619-0051

### INFO-052
- **タイトル:** KPMG「アジェンティックAIで10年間に$3兆生産性向上」・Meta Business Agent 10X-100X・Claude使用ログ80%時間短縮
- **ソース:** Hymalaia / arXiv
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-04
- **関連企業:** KPMG, Meta, Anthropic
- **要約:** KPMG予測: アジェンティックAIが今後10年間で$3兆の生産性向上を生成。Meta Business Agentは10X-100Xの生産性を実証。大規模Claude使用ログから直接推定した生産性向上で、より広範なタスクセットで80%の時間短縮を発見。人間-エージェントワークフローがエンタープライズ運用を再構築。
- **キーファクト:**
  - KPMG: アジェンティックAIで10年間$3兆生産性向上予測
  - Meta Business Agent: 10X-100X生産性実証
  - Claude使用ログ: 広範タスクで80%時間短縮
- **引用URL:** https://www.hymalaia.com/blog/why-enterprises-adopt-autonomous-ai-agents-in-2026-en
- **Evidence ID:** EVD-20260619-0052

### INFO-053
- **タイトル:** Klarna 700人CS置換→「訓練補助輪を取っただけ」・AI実装18カ月内に人員削減パターン
- **ソース:** Instagram / Business Today / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaは2024年に700人のカスタマーサービス担当者をAIで置換しCEOが公に祝賀。だが「AIは全仕事を奪ったのではなく訓練補助輪を取っただけ」— 人間を呼び戻し。Duolingoは請負労働力を削減し人間のAI置換を停止。AI実装の結果18カ月以内に労働力削減が起こる（リーダーシップが効率向上をコスト削減として扱うため）。
- **キーファクト:**
  - Klarna: 700人CS担当者をAI置換・CEO祝賀→人間呼び戻し
  - Duolingo: 請負削減・人間AI置換停止
  - AI実装→18カ月内人員削減パターン（効率＝コスト削減扱い）
- **引用URL:** https://www.instagram.com/reel/DZpkANIozjZ/
- **Evidence ID:** EVD-20260619-0053

### --- KIQ-002-05: プラットフォーマーAI統合による中間事業者バリューチェーン侵食 ---

### INFO-054
- **タイトル:** McKinsey「アジェンティック広告経済」— 広告価値が見せる・選ぶ・買うを形作るプレイヤーへ移行
- **ソース:** McKinsey
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** Google, Meta, McKinsey
- **要約:** AIが消費者の製品発見方法を変えるにつれ、広告価値は見せる・選ばれる・購入されるものを形作るプレイヤーへ移行する。Google AdsとMeta Adsは「AIでマイクロ秒単位で広告を販売・ターゲット・配置」。アジェンティック広告経済でプラットフォームのバリューチェーン支配が強化。広告バイヤーは代替されないが広告購入の非効率は抑制される。
- **キーファクト:**
  - 広告価値シフト: 見せる/選ぶ/買うを形作るプレイヤーへ
  - Google Ads/Meta Ads: AIでマイクロ秒単位販売/ターゲット/配置
  - 広告バイヤー代替でなく非効率抑制
- **引用URL:** https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-agentic-advertising-economy-from-attention-to-action
- **Evidence ID:** EVD-20260619-0054

### INFO-055
- **タイトル:** SaaS→Service-as-Software移行 — AIがソフト自ら仕事を行う・SaaSマルチプル圧縮懸念
- **ソース:** LinkedIn (Holden Spaht) / Instagram
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-05, KIQ-004-02
- **関連企業:** (SaaS業界横断), SAP, Publicis Sapient
- **要約:** SaaSは20年間人々の仕事を助けるツールを販売したが、AIはソフト自ら仕事を行うことを可能に。業界は「Service-as-Software」へ移行中。「AIがコードを書けるならソフトは死んだ。機能がコピーできるならSaaSマルチプルは圧縮される」。SAP自律サプライチェーン・Publicis Sapient AI主導IT運用等でアジェンティックAIがオペレーティングモデルを書き換え。
- **キーファクト:**
  - SaaS→Service-as-Software移行（AIがソフト自ら仕事実行）
  - 「AIがコード書ける→ソフト死亡・SaaSマルチプル圧縮」論
  - SAP自律サプライチェーン・Publicis Sapient AI主導IT運用
- **引用URL:** https://www.linkedin.com/posts/holden-spaht_ive-spent-the-last-week-in-board-meetings-activity-7471313215449219072-l-kB
- **Evidence ID:** EVD-20260619-0055

### --- KIQ-003-01: 各社API料金改定の頻度・方向性 ---

### INFO-056
- **タイトル:** OpenAIが大幅トークン値下げ検討 — 繰返プロンプト価格引下・入力50%割引・$25/100万トークン
- **ソース:** Entrepreneur / CostGoat / PricePerToken
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-OAI-001
- **関連企業:** OpenAI
- **要約:** OpenAIはAnthropicとのユーザー獲得競争で大幅値下げを検討（前日INFO-004 WSJ報道の追証）。繰返プロンプトの価格引下・入力コスト50%割引・100万トークン$25。GPT-5.5現行価格$5/$30（入出力・CostGoat）・Short Context $12.50/$75（PricePerToken）。新エンタープライズ支出管理・使用分析機能も提供。値下げは弱者シグナル（Altman「コストが巨大な問題」）。
- **キーファクト:**
  - OpenAI大幅値下げ検討: 繰返プロンプト引下・入力50%割引・$25/100万トークン
  - GPT-5.5: $5/$30 per MTok（CostGoat）・Short Context $12.50/$75（PricePerToken）
  - Anthropic獲得競争が動機・Altman「コストが巨大な問題」（弱者シグナル）
  - 新エンタープライズ支出管理・使用分析機能
- **引用URL:** https://www.facebook.com/Entrepreneur/posts/openai-is-weighing-drastic-cuts-to-what-it-charges-for-ai-tokens-it-expects-anth/1379683450696530/
- **Evidence ID:** EVD-20260619-0056

### INFO-057
- **タイトル:** AnthropicがAgent SDKトークン課金変更を一時停止 — 重度ユーザー大幅コスト増を回避・6/15モデル廃止
- **ソース:** Ars Technica / IT-Connect / The New Stack
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Anthropicは自動化重点Claude Agent SDKの重度ユーザーに実質コスト増をもたらす課金変更を発表後、一時停止。Vibe Coding「Claude Unlimited API」は6/15終了予定だったが保留。月次含まれるクレジット（$20-$200プラン依存）。6/15に2つのClaudeモデル廃止。Claude Opus 4.6は$5/$25 per MTok。Max 20x $200/月はAPI課金より実質安価（API同等で$600-$1,500/月）。
- **キーファクト:**
  - Agent SDKトークン課金変更一時停止（重度ユーザーコスト増回避）
  - Vibe Coding「Claude Unlimited API」6/15終了予定→保留
  - 月次クレジット$20-$200（プラン依存）・6/15に2モデル廃止
  - Claude Opus 4.6: $5/$25 per MTok
  - Max 20x $200/月 vs API同等$600-$1,500/月
- **引用URL:** https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk/
- **Evidence ID:** EVD-20260619-0057

### INFO-058
- **タイトル:** トークンは2023年比90%安価化もAI支出は倍増 — ジェボンズパラドックス・エージェントがコスト急増
- **ソース:** Fortune / Business Insider / Economist
- **公開日:** 2026-06-17
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01, KIQ-002-02
- **関連企業:** NVIDIA, (業界横断)
- **要約:** 単一トークン価格は2023年から90%以上下落したが、LLM支出は昨年末から倍増（ジェボンズパラドックス）。NVIDIA Blackwellシステムが安価なAIトークンで市場を溢れさせコスト低下を加速する可能性。一方でエージェントがトークン多消費アプリ・自動推論モデルで企業コストを急増させ、企業は急増するAIコスト削減に奔走。Gartner予測: 2026年末までにエンタープライズアプリの40%がタスク固有AIエージェント埋め込み（前年<5%から）。
- **キーファクト:**
  - トークン価格2023年比90%+下落・LLM支出は昨年末から倍増（ジェボンズパラドックス）
  - NVIDIA Blackwell: 安価トークンで市場溢れ・コスト低下加速可能性
  - エージェント・自動推論で企業AIコスト急増・削減に奔走
  - Gartner: 2026年末エンタープライズアプリ40%がAIエージェント埋め込み（前年<5%）
- **引用URL:** https://fortune.com/2026/06/17/why-is-ai-spending-increasing-as-tokens-get-cheaper-jevons-paradox/
- **Evidence ID:** EVD-20260619-0058

### --- KIQ-003-02: 主要ベンチマーク（MMLU, HumanEval, GPQA等）性能推移 ---

### INFO-059
- **タイトル:** Artificial Analysis Intelligence Index v4.1 — Claude Fable 5が60点で首位も米輸出規制で利用不可・Grok 4は総合#1（73点）
- **ソース:** Artificial Analysis / WindowsForum
- **公開日:** 2026-06-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01, KIQ-002-06
- **関連企業:** Anthropic, xAI, Google, DeepSeek, Z.ai (GLM)
- **要約:** Artificial Analysisが改訂Intelligence Index v4.1を公開（6/16）。Claude Fable 5が60点で首位だが、米輸出規制後（全外国人アクセス停止）で利用不可。GLM-5.2（Z.ai）がオープンウェイト首位51点・パレートフロンティア。DeepSeek R1-0528が#2に急上昇・Gemini 2.5 Proと同等。Index構成: 34%エージェント・24%コーディング・24%科学推論・18%一般知識。Grok 4は総合#1（73点・$6/100万）。
- **キーファクト:**
  - Intelligence Index v4.1: Claude Fable 5首位(60点)・米輸出規制で利用不可
  - GLM-5.2 (Z.ai): オープンウェイト首位51点・パレートフロンティア
  - DeepSeek R1-0528: #2急上昇・Gemini 2.5 Pro同等
  - Index構成: 34%エージェント・24%コーディング・24%科学推論・18%一般知識
  - Grok 4: 総合#1・Intelligence Index 73・$6/100万トークン
- **引用URL:** https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index
- **Evidence ID:** EVD-20260619-0059

### INFO-060
- **タイトル:** SWE-bench比較 — Grok 4 75%・GPT-5.4 74.9%・Claude 74%+・Gemini 63.8%・Fable 5 SWFTE 100/100首位
- **ソース:** GuruSup / SWFTE Leaderboard
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01
- **関連企業:** xAI, OpenAI, Anthropic, Google
- **要約:** コーディングベンチマークSWE-bench: Grok 4 75%・GPT-5.4 74.9%・Claude 74%+・Gemini 63.8%。Claude Fable 5はSWFTE複合品質指数100/100で首位（357+モデル中）。2026年は単一最良モデルなし: Claude Opus 4.8/GPT-5が推論/コード首位、Geminiがマルチモーダル/長コンテキスト首位、Grok 4が…。汎用LLMが医療ベンチマークで専門臨床AIツールを上回る（Nature 6/12）。
- **キーファクト:**
  - SWE-bench: Grok 4(75%)・GPT-5.4(74.9%)・Claude(74%+)・Gemini(63.8%)
  - Claude Fable 5: SWFTE 100/100首位(357+モデル中)
  - 単一最良なし: Claude/GPT推論コード・Geminiマルチモーダル・Grok 4...
  - 汎用LLMが医療ベンチで専門臨床AI上回る（Nature 6/12）
- **引用URL:** https://gurusup.com/blog/grok-vs-chatgpt-claude-gemini
- **Evidence ID:** EVD-20260619-0060

### INFO-061
- **タイトル:** ARC-AGI-2でフロンティアモデル苦戦 — 適応・効率的推論能力不足・QAGI検証枠組みv2.0登場
- **ソース:** Facebook / OpenLM Chatbot Arena
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** (フロンティアモデル各社)
- **要約:** ARC-AGI-2は現在のトップAIモデルが強力でも適応・効率的推論能力が不足し新問題で苦戦することを示す。AAII v3は10評価（MMLU-Pro・Humanity's Last Exam等）を組み込み。QAGI Validation Framework v2.0が、AIシステムがより自律・アジェンティック・量子化につれて「真のAGI到達」を検証する新枠組みとして登場。ARC-AGI-3（対話環境付き）も登場。
- **キーファクト:**
  - ARC-AGI-2: トップモデル適応・効率推論不足・新問題で苦戦
  - AAII v3: 10評価組み込み（MMLU-Pro・Humanity's Last Exam等）
  - QAGI Validation Framework v2.0: 量子化AI時代の真のAGI検証枠組み
  - ARC-AGI-3: 対話環境付き推論ベンチマーク登場
- **引用URL:** https://openlm.ai/chatbot-arena/
- **Evidence ID:** EVD-20260619-0061

### --- KIQ-003-03: OSSモデル（Meta Llama, Mistral等）と商用モデルの性能ギャップ ---

### INFO-062
- **タイトル:** Mistral Small 4 119Bオープンウェイト発表 — 約100人エンジニアで18カ月に4つのSOTAオープンモデル構築
- **ソース:** LinkedIn / Panto AI / Reddit
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Mistral AI, NVIDIA
- **要約:** Mistral AIが119Bパラメータのオープンウェイトモデルを発表し、アクセス可能なOSSの期待を再定義。Mistralは約100人のエンジニアで18カ月に4つのSOTAオープンモデルを構築（米国スタートアップよりリーン・高速）。NVIDIA AI Podcastでオープンモデルのエンタープライズ導入を議論。エンタープライズトラクション拡大・オープンウェイトモデル+広範なAPIサーフェスで開発者エコシステム構築。
- **キーファクト:**
  - Mistral Small 4 119B: オープンウェイト・アクセス可能OSS期待再定義
  - 約100人エンジニアで18カ月・4つのSOTAオープンモデル構築（米国よりリーン）
  - エンタープライズトラクション拡大・オープンウェイト+広範API
- **引用URL:** https://www.linkedin.com/posts/faizan170_analyzing-mistral-small-4-119b-the-new-heavyweight-activity-7471093889400033281-JP2o
- **Evidence ID:** EVD-20260619-0062

### INFO-063
- **タイトル:** Meta Llama 4 — 1,000万トークンコンテキスト・ScoutがGPT-4o超え・Gemini Enterpriseで完全管理提供
- **ソース:** Google Cloud Docs / Facebook
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-03, KIQ-001-04
- **関連企業:** Meta, Google
- **要約:** Meta Llama 4は1,000万トークンの驚異的コンテキストウィンドウを持ち、GPT-4oを凌駕するベンチマークを示す。Llama 4 Scout 17B-16EはサイズクラスでSOTA・前世代および他のオープン/プロプライエタリモデルを上回る。Gemini Enterprise Agent Platformで完全管理Llamaモデル提供。OSSが商用フロンティアに追いつく（前日INFO-042の3モデルGPT-4超えと整合）。
- **キーファクト:**
  - Llama 4: 1,000万トークンコンテキスト・GPT-4o超えベンチマーク
  - Llama 4 Scout 17B-16E: サイズクラスSOTA・前世代+プロプライエタリ超え
  - Gemini Enterpriseで完全管理Llama提供
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama
- **Evidence ID:** EVD-20260619-0063

### --- KIQ-003-04: 各社の資金調達・投資動向 ---

### INFO-064
- **タイトル:** Anthropicが$650億調達・評価額$9,650億到達・IPO秘密申請（$1兆目標）— OpenAI($5,000億)・SpaceX抜き最多価値AIスタートアップ
- **ソース:** Yahoo Finance / Zacks / Benzinga / GlobalX
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-OAI-001
- **関連企業:** Anthropic, OpenAI, SpaceX
- **要約:** Anthropicが$650億の民間資金調達を完了し評価額$9,650億に到達。IPOを秘密申請（$1兆以上の評価額目標）。評価額は2026年2月の$3,800億からほぼ3倍。OpenAIは$1,220億調達後$8,520億評価。Anthropicは世界で最も価値あるAIスタートアップに。Reuters報道: AI企業が最大$1兆評価額・$600億以上調達目標で公募予定。OpenAIはSpaceXを抜き世界最多価値スタートアップ($5,000億)。
- **キーファクト:**
  - Anthropic: $650億調達・評価額$9,650億・IPO秘密申請($1兆目標)
  - 評価額2月$3,800億→ほぼ3倍
  - OpenAI: $1,220億調達・$8,520億評価・世界最多価値スタートアップ($5,000億・SpaceX抜き)
  - Reuters: AI企業最大$1兆評価・$600億+調達公募予定
- **引用URL:** https://finance.yahoo.com/personal-finance/investing/article/anthropic-ipo-what-to-know-before-you-buy-the-stock-170741665.html
- **Evidence ID:** EVD-20260619-0064

### INFO-065
- **タイトル:** Q1 2026 AIスタートアップ資金調達$3,000億・4メガラウンド(OpenAI $1,220億・Anthropic $300億・xAI $200億・Waymo $160億)
- **ソース:** Flairius News / Forbes AI 50
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic, xAI, Waymo
- **要約:** Q1 2026のAIスタートアップ資金調達は$3,000億。4つのメガラウンドが四半期を定義: OpenAI $1,220億・Anthropic $300億・xAI $200億・Waymo $160億。Forbes 2026 AI 50リストが有望AI企業をスポットライト。資本集中が極大化。
- **キーファクト:**
  - Q1 2026 AI資金調達$3,000億
  - 4メガラウンド: OpenAI $1,220億・Anthropic $300億・xAI $200億・Waymo $160億
  - 資本集中極大化
- **引用URL:** https://flairiusnews.com/global-ai-startup-funding-300-billion-q1-2026-analysis-founders/
- **Evidence ID:** EVD-20260619-0065

### INFO-066
- **タイトル:** Dallas Fed推計: 今後3-5年で$3-5兆のAIデータセンター投資・ハイパースケーラー主導
- **ソース:** Perspective on Risk / Dallas Fed
- **公開日:** 2026-06-18
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-005-01
- **関連企業:** (ハイパースケーラー各社)
- **要約:** ダラス連銀は今後3-5年で約$3-5兆のAIデータセンター投資を推計。ハイパースケーラーが主導。物理的制約（電力・冷却・土地）と資本流入のギャップが確定的（前日IND-029参照のGoldman $5.3T/2030と整合）。資本流入加速と物理的制約の同時進行。
- **キーファクト:**
  - Dallas Fed: 今後3-5年で$3-5兆AIデータセンター投資推計
  - ハイパースケーラー主導
  - 物理的制約（電力・冷却・土地）と資本流入ギャップ確定的
- **引用URL:** https://perspectiveonrisk.substack.com/p/perspective-on-risk-june-18-2026
- **Evidence ID:** EVD-20260619-0066

### --- KIQ-003-05: エコシステム離脱コスト（スイッチングコスト）の変化 ---

### INFO-067
- **タイトル:** AI支援ERP移行でコスト・期間半減（McKinsey） — スイッチングコスト溶解・ただし無料でなく半額
- **ソース:** ctaio.dev (McKinsey引用) / Glean
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-05, KIQ-001-05
- **関連企業:** McKinsey
- **要約:** McKinsey 2025分析でAI支援ERP移行プログラムがコスト・期間を2倍削減。これは無料のスイッチングではなく「半額」スイッチング。AIがERPスイッチングコストを溶解させることが「ゲーム全体」。Claude等からの移行コストは統合再構成・ユーザー再訓練・含む。AIがベンダーロックインを弱める方向。
- **キーファクト:**
  - McKinsey: AI支援ERP移行でコスト/期間2倍削減（半額・無料でない）
  - AIがERPスイッチングコスト溶解＝「ゲーム全体」
  - 移行コスト: 統合再構成・ユーザー再訓練含む
  - AIがベンダーロックイン弱化方向
- **引用URL:** https://ctaio.dev/en/labs/ai-erp-switching-costs/
- **Evidence ID:** EVD-20260619-0067

### INFO-068
- **タイトル:** IDC「AIは準備済み・エンタープライズは未準備」— パイロット→本番ギャップをベンダーが解決必要・マルチベンダーAWS環境
- **ソース:** IDC / Endava / Box
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-05, KIQ-002-02
- **関連企業:** IDC, AWS
- **要約:** IDC分析: AIイノベーションはエンタープライズ採用を上回り、AIソフトウェア構築・販売ベンダーのみが解決可能。パイロット→本番ギャップが核心課題。複数AIベンダーと個別統合する代わりに、AWSネイティブ環境で主要モデルを試行可能（Endava）。マルチベンダー戦略でロックイン回避。エンタープライズAI戦略は組織全体の構造的計画が必要（Box）。
- **キーファクト:**
  - IDC: AI準備済み・エンタープライズ未準備・ベンダーがパイロット→本番ギャップ解決必要
  - マルチベンダー: AWSネイティブ環境で主要モデル試行（個別統合回避）
  - ロックイン回避方向・組織全体構造的AI戦略必要
- **引用URL:** https://www.idc.com/resource-center/blog/ai-is-ready-enterprises-are-not-vendors-need-to-fix-it/
- **Evidence ID:** EVD-20260619-0068

### --- KIQ-004-01: 業務自律化の進展業界・人員配置転換シグナル ---

### INFO-069
- **タイトル:** AIが2026年1-5月で米国88,000人解雇の原因（前年通年54,000人超）・ServiceNow数百人削減
- **ソース:** Metaintro (Challenger) / Intellizence
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** ServiceNow, (業界横断)
- **要約:** 雇用主は2026年1-5月で約88,000人の米国解雇をAIのせいとした（前年通年54,000人を既に超える）。ServiceNowはAI使用増加に伴い数百人を解雇(6/12)。企業はチーム統合・部門再編・管理階層フラット化・AI関連投資へシフト。調査でCEOの99%が2年以内に労働者を解雇しAIで置換する準備と回答。「AI解雇」vs「AIウォッシング」の議論。
- **キーファクト:**
  - AI原因解雇: 2026年1-5月88,000人（前年通年54,000人超）
  - ServiceNow: AI使用増加で数百人解雇(6/12)
  - チーム統合・部門再編・管理フラット化・AI投資シフト
  - CEO 99%が2年内AI置換解雇準備（調査）
  - 「AI解雇」vs「AIウォッシング」議論
- **引用URL:** https://www.metaintro.com/blog/ai-88000-us-job-cuts-2026-challenger
- **Evidence ID:** EVD-20260619-0069

### INFO-070
- **タイトル:** ChatGPTが日本でターゲット広告開始 — 電通・博報堂DY ONE・サイバーエージェントが広告配置管理
- **ソース:** SQ Magazine
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-01, KIQ-002-05
- **関連企業:** OpenAI, CyberAgent, 電通 (Dentsu Digital), 博報堂 (Hakuhodo DY ONE)
- **要約:** OpenAIがChatGPTでターゲット広告を日本開始。日本企業の電通デジタル・博報堂DY ONE・サイバーエージェントが広告配置管理を支援。OpenAIのChatGPTマネタイズ推進の具体例。CyberAgent×Alibaba Cloudの戦略対話も進行。広告運用のAI自律化が日本市場で具体化。
- **キーファクト:**
  - ChatGPT日本でターゲット広告開始
  - 電通デジタル・博報堂DY ONE・サイバーエージェントが広告配置管理
  - CyberAgent×Alibaba Cloud戦略対話
  - OpenAIマネタイズ推進・広告運用AI自律化の日本具体化
- **引用URL:** https://sqmagazine.co.uk/chatgpt-targeted-ads-japan-launch/
- **Evidence ID:** EVD-20260619-0070

### INFO-071
- **タイトル:** KPMG「エントリーレベル任務の自動化が職業的徒弟制度を破壊・次世代育成の完全再考を強制」
- **ソース:** KPMG / Engadget / PwC
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** KPMG, PwC
- **要約:** KPMG CFO分析: エントリーレベル任務の自動化がプロフェッショナルな徒弟制度を破壊し、次世代の育成方法の完全な再考を強制。KPMG調査: 従業員の41%のみが組織にgenAIポリシーあると回答（シャドーAIのギャップ）。PwC 2026 AI Jobs Barometer: AI暴露エントリーレベル職はシニアスキル要求が7倍likely。初期キャリアはフラット化だが「シニア化」エントリーレベルは2019年から35%成長。
- **キーファクト:**
  - KPMG: エントリーレベル自動化が徒弟制度破壊・次世代育成完全再考
  - KPMG調査: 従業員41%のみがgenAIポリシー回答（シャドーAIギャップ）
  - PwC: AI暴露エントリーレベル職はシニアスキル要求7倍likely
  - 初期キャリアフラット化・「シニア化」エントリーレベル35%成長(2019年比)
- **引用URL:** https://kpmg.com/us/en/articles/2026/cfo-navigate-volatility-while-managing-market-headwinds.html
- **Evidence ID:** EVD-20260619-0071

### --- KIQ-004-02: コーディング能力の市場価値変化 ---

### INFO-072
- **タイトル:** ソフトウェア開発者求人が2022年ピーク比70%減・22-25歳雇用20%減(2024年比) — WSJ/PwC
- **ソース:** WSJ / PwC AI Jobs Barometer
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-02, KIQ-002-04
- **関連企業:** (業界横断)
- **要約:** WSJ: 5月下旬までのソフトウェア開発者求人は2022年ピーク比で約70%減（昨春の低水準からわずかに改善）。PwC 2026 AI Jobs Barometer: 22-25歳のソフトウェア開発者雇用が2024年から約20%減少。Forrester 2026予測: 悪化する雇用市場信号に対応しCS入学希望が20%減少。コーディング能力のコモディティ化が構造的。
- **キーファクト:**
  - ソフトウェア開発者求人: 2022年ピーク比約70%減(WSJ)
  - 22-25歳ソフト開発者雇用: 2024年から約20%減(PwC)
  - Forrester 2026: CS入学希望20%減少予測
  - コーディング能力コモディティ化の構造的進行
- **引用URL:** https://www.wsj.com/lifestyle/careers/changing-careers-cutting-expenses-software-engineers-contend-with-ai-3889ce73
- **Evidence ID:** EVD-20260619-0072

### INFO-073
- **タイトル:** 「コードを書くのが仕事だった・今はAIエージェントチームを率いること」・プログラミングスキル一晩でコモディティ化
- **ソース:** Instagram / DX
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02, KIQ-001-01
- **関連企業:** Google, Anthropic
- **要約:** 「コードを書くのが仕事だった。今はAIエージェントのチームを率いること」。Google CEO Sundar Pichai: ソフトウェア開発の未来は異なり、AIがルーチンコーディングを自動化し開発者が複雑・創造的側面に集中。プログラミング言語のスキルセットが一晩でコモディティ化。DX: AIコーディングアシスタント費用が一部開発者で$29→$750/月・$50→$3,000/月に急増。「書ける」から「AIに書かせて評価できる」への移行進行。
- **キーファクト:**
  - 「コード書く→AIエージェントチーム率いる」へ移行
  - Pichai: AIがルーチンコーディング自動化・複雑創造的側面へ集中
  - プログラミングスキル一晩でコモディティ化
  - DX: AIコーディング費用$29→$750/月・$50→$3,000/月に急増
  - 「書ける」→「AIに書かせて評価できる」移行
- **引用URL:** https://www.instagram.com/reel/DZnWV3PpUrX/
- **Evidence ID:** EVD-20260619-0073

### --- KIQ-004-03: AI代替困難能力の市場価値・新職種 ---

### INFO-074
- **タイトル:** WEF「2030年までに1.7億新規雇用創出・9,200万変動」・PwC「AIは二極化労働市場創出・広範解雇でなく再形成」
- **ソース:** WEF / PwC 2026 AI Jobs Barometer
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03, KIQ-004-01
- **関連企業:** WEF, PwC
- **要約:** WEF: 2030年までに1.7億新規雇用創出だが9,200万も変動。PwC 2026 AI Jobs Barometer（10億以上の求人広告分析）: AIは広範な雇用喪失でなく二極化労働市場を創出・雇用市場を再形成。新興スキル需要が40-70%増加。最強の成果を出す組織は仕事を再設計。BCG(2026/4): 今後2-3年で米国の50-55%の雇用がAIで再形成。
- **キーファクト:**
  - WEF: 2030年まで1.7億新規雇用創出・9,200万変動
  - PwC: AIは広範解雇でなく二極化労働市場創出・再形成
  - 新興スキル需要40-70%増加
  - BCG(2026/4): 今後2-3年で米国雇用50-55%がAI再形成
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-workforce-hiring-fix-skills-mismatch/
- **Evidence ID:** EVD-20260619-0074

### INFO-075
- **タイトル:** 新AI職種の出現 — AI Art Director・Director of SEO & Agentic Search・メタスキルの時代
- **ソース:** TEKsystems / Mediabistro / WEF
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03, KIQ-002-05
- **関連企業:** TEKsystems, Mediabistro
- **要約:** 新AI職種が出現: AI Art Director/Designer・Director of SEO and Agentic Search・AI Strategist。WEF: スキルが加速的に陳腐化する中、メタスキル（新しい能力を構築する包括的能力）がAI搭載仕事の未来を準備。ヒューマンスキル（共感・批判的思考・倫理的意思決定・コミュニケーション・適応力）がAI代替困難能力として価値上昇。ManpowerGroup: 企業がAI関連従業員訓練に多大投資。
- **キーファクト:**
  - 新AI職種: AI Art Director・Director of SEO & Agentic Search・AI Strategist
  - WEF: メタスキル（新能力構築の包括的能力）がAI時代準備の鍵
  - ヒューマンスキル価値上昇: 共感・批判的思考・倫理・コミュニケーション・適応力
  - ManpowerGroup: AI関連訓練に多大投資
- **引用URL:** https://www.weforum.org/stories/2026/06/meta-skills-continual-learning-workplace-ai-era/
- **Evidence ID:** EVD-20260619-0075

### --- KIQ-004-04: AI時代に勝つ企業の条件 ---

### INFO-076
- **タイトル:** エンタープライズAI展開の95%が失敗 — 勝者は顧客関係・プロプライエタリデータ・重要ワークフローの「所有」で差別化
- **ソース:** LinkedIn (Lachlan Fogarty)
- **公開日:** 2026-06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-04, KIQ-002-02
- **関連企業:** (業界横断)
- **要約:** エンタープライズAI展開の95%が失敗。勝者を分けるのは顧客関係・プロプライエタリデータ・重要ワークフローの「所有」— AIが市場から摩擦を除去するにつれて。データモート（競合が容易に複製できないプロプライエタリデータ）が企業価値を引き上げ（M&A視点）。クリーンなデータと防御可能AIが価値創出。広告代理店の最大の脅威はAIでなくビジネスモデル — 実行の販売をやめる者が生き残る。
- **キーファクト:**
  - エンタープライズAI展開95%失敗
  - 勝者条件: 顧客関係・プロプライエタリデータ・重要ワークフローの「所有」
  - データモート: 競合が複製困難なプロプライエタリデータが企業価値向上
  - 広告代理店: 最大脅威はAIでなくビジネスモデル（実行販売停止者が生存）
- **引用URL:** https://www.linkedin.com/posts/lachlan-fogarty_the-context-moat-why-95-of-ai-projects-activity-7471144941168078848-DULd
- **Evidence ID:** EVD-20260619-0076

### --- KIQ-005-01: AGI到達度ベンチマーク指標と能力進展 ---

### INFO-077
- **タイトル:** ARC-AGI階層の開示 — ARC-AGI-3でフロンティア0.37%（GPT-5.4は0.26%・人間100%）・LLLM+手続き型世界モデルで33%+
- **ソース:** GitConnected / Ben Goertzel (X) / AI Safety Türkiye
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** SingularityNET, OpenAI
- **要約:** ARC-AGIベンチマーク階層の性能格差が開示: ARC-AGI-1でフロンティア93%・ARC-AGI-2で68.8%（当初<5%・2025年末24%）・ARC-AGI-3で0.37%（GPT-5.4は0.26%・人間100%）。ARC-2→ARC-3の段差は極大。SingularityNET研究者がLLM+手続き型世界モデル+検証でARC-AGI-3 33%+を達成。Anthropicはベンチマーク供給がボトルネックと認識。「IQ」の普遍的指標不存在でバイブコーディング勝利でも抽象推論敗北可能。
- **キーファクト:**
  - ARC-AGI-1: フロンティア93%・ARC-AGI-2: 68.8%（当初<5%→2025末24%）・ARC-AGI-3: 0.37%
  - GPT-5.4: ARC-AGI-3で0.26%（人間100%）
  - SingularityNET: LLM+手続き型世界モデル+検証でARC-AGI-3 33%+
  - Anthropic: ベンチマーク供給ボトルネック認識・「IQ」普遍指標不存在
- **引用URL:** https://levelup.gitconnected.com/gpt-5-4-scored-0-26-humans-scored-100-the-gap-is-not-a-bug-jean-piaget-proved-it-in-1971-0ce31d0be896
- **Evidence ID:** EVD-20260619-0077

### INFO-078
- **タイトル:** DeepMind「From AGI to ASI」レポート公開 — AGIは推測から現実へ・2026年時点で特定領域で専門家超越
- **ソース:** LinkedIn (Matija Franklin) / UK Gov AI Scenarios 2030
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Google / DeepMind
- **要約:** DeepMind「From AGI to ASI」レポートが公開。過去10年で人間レベルAGI構築が遠い推測から現実へ移行。2026年2月GPT-5.3-Codexが自律コーディングで新マイルストーン。OpenAIが2030年までにAGI到達する確率55%。UK政府AI Scenarios 2030: 2026年時点でAIシステムは高い自律性で動作し特定領域で専門家を超越。2030年までにさらに自律的に。AIはタスクを代替するが役割ではなく（計算機/DB/手順追従者としての人間は崩壊・意味創造者としての人間は残存）。
- **キーファクト:**
  - DeepMind「From AGI to ASI」公開・AGI推測→現実へ
  - GPT-5.3-Codex: 2026年2月自律コーディング新マイルストーン
  - OpenAI 2030年AGI到達確率55%
  - UK AI Scenarios: 2026年時点AI特定領域で専門家超越・2030年までさらに自律化
  - AIはタスク代替（役割でなく）・意味創造者としての人間残存
- **引用URL:** https://www.linkedin.com/posts/matijafranklin_our-report-from-agi-to-asi-is-out-over-activity-7471172615995514882-iqwc
- **Evidence ID:** EVD-20260619-0078

### --- KIQ-005-02: 主要CEO/研究者のAGIタイムライン予測 ---

### INFO-079
- **タイトル:** AGIタイムライン予測 — Hassabis 2029年・Amodei 2027年・Kalshi予測市場OpenAI 2030年AGI 55%
- **ソース:** Delos / Faster Please / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google / DeepMind, Anthropic, OpenAI
- **要約:** Demis HassabisがAGIタイムラインを短縮し人間レベル知能は2029年に到達可能と予測（従来5-10年）。Dario Amodeiは2027年までにAGIがlikelyと発言。Kalshi予測市場(2026/4): OpenAIが2030年までにAGI到達する確率55%。Sam Altmanは「AIテイクオフが公式に開始」・2026年までにAIが真に新規創造的アイデアを生成と主張。主要CEO全員が数年内AGIに楽観。
- **キーファクト:**
  - Hassabis: AGI人間レベル2029年到達（タイムライン短縮）
  - Amodei: 2027年までAGI likely
  - Kalshi予測市場(2026/4): OpenAI 2030年AGI到達55%
  - Altman: 「AIテイクオフ公式開始」・2026年までに創造的アイデア生成
- **引用URL:** https://www.delos.so/en/blog/agi-myth-or-reality-state-of-the-art-2026
- **Evidence ID:** EVD-20260619-0079

### INFO-080
- **タイトル:** Yann LeCunがMeta退社・AMI Labs設立で$11億調達 — 「LLMは人間レベル知能への道でない」・世界モデル推進
- **ソース:** Bloomberg Business / The AI Innovator / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02, KIQ-005-01
- **関連企業:** AMI Labs, Meta, OpenAI
- **要約:** Yann LeCunがMetaを退社しAMI Labsのエグゼクティブチェアマンに就任・世界モデル構築で$11億調達。「LLMは人間レベル知能への道でない」・シリコンバレーはLLM-to-AGI列車に飛び乗り「催眠されている」と主張。AIの未来は次に何が起きるかを予測するシステムに依存すると主張。xAI批判は1社の問題でなくフロンティアAIの創業技術チームの重要性。Q1 2026でAIがVCドルの約80%を獲得（前年比+55%）。
- **キーファクト:**
  - LeCun: Meta退社・AMI Labs設立・$11億調達（世界モデル）
  - 「LLMは人間レベル知能への道でない」・シリコンバレー「催眠」批判
  - AI未来は「次に何が起きるか予測するシステム」に依存
  - Q1 2026: AIがVCドル約80%獲得（前年比+55%）
- **引用URL:** https://theaiinnovator.com/yann-lecun-llms-are-not-a-path-to-human-level-intelligence/
- **Evidence ID:** EVD-20260619-0080

### --- KIQ-005-03: AGI安全性とガバナンスの政策議論 ---

### INFO-081
- **タイトル:** フロンティアAIモデルがOpenBSDの27年間未発見の脆弱性を発見・AI安全性基盤としての能力示唆
- **ソース:** LinkedIn (Adam Leon Smith) / James Gealy
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03, KIQ-005-01
- **関連企業:** OpenBSD
- **要約:** フロンティアAIモデルが27年間未発見だったOpenBSDの脆弱性を発見。これはAIの安全保障能力（脆弱性発見）の具体例であり、フロンティアAI安全性基盤の議論でJames Gealyと共にunpacking。能力-リスク二面性の具体例。
- **キーファクト:**
  - フロンティアAI: OpenBSD 27年未発見脆弱性を発見
  - AI安全性能力の具体例・能力-リスク二面性
- **引用URL:** https://www.linkedin.com/posts/adamleonsmith_james-gealy-on-ai-safety-standards-for-frontier-activity-7472918673532395521-T8fA
- **Evidence ID:** EVD-20260619-0081

### INFO-082
- **タイトル:** 欧州「米国のAI警告ショットにどう対応すべきか」— AI中堅国が連合でフロンティアAIアクセス確保交渉
- **ソース:** The Economist (By Invitation)
- **公開日:** 2026-06-18
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03, KIQ-002-06
- **関連企業:** 欧州各国, 米国
- **要約:** Economist寄稿: 欧州は米国のAI警告ショット（Anthropic制限等）にどう対応すべきか。AI中堅国が連合して行動することでより強い交渉地位を獲得し、それをフロンティアAIシステムへのアクセス確保に利用可能。新クラスのAIモデルが政府に外国アクセスルールの再考を強いる。最先端モデル層へのエクスポージャー管理が焦点（AI全体アクセス除去でなく）。
- **キーファクト:**
  - 欧州対応論: AI中堅国連合で交渉地位強化・フロンティアAIアクセス確保
  - 新AIモデルクラスが外国アクセスルール再考を強制
  - 最先端モデル層エクスポージャー管理が焦点
- **引用URL:** https://www.economist.com/by-invitation/2026/06/18/how-europe-must-respond-to-americas-ai-warning-shot
- **Evidence ID:** EVD-20260619-0082

### INFO-083
- **タイトル:** Anthropic AI Safety Fellowship 2026($15,000)・MATS 12週間完全資助アライメント研究 — AI安全性人材・資金強化
- **ソース:** Instagram / Anthropic Fellows / Startup Genome
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-03, KIQ-004-03
- **関連企業:** Anthropic, MATS
- **要約:** AnthropicがAI Safety Fellowship 2026を$15,000資金で立ち上げ。MATSは12週間の完全資助研究フェローシップでアライメント・制御・セキュリティ・ガバナンス研究志望者向け。AI-Native企業への資金が2024-2025で17%増加し$150億到達（他テックは全球で4%縮小）。UNIDIRがGlobal Conference on AI Security and Ethics 2026開催。AI安全性人材・資金の強化基調。
- **キーファクト:**
  - Anthropic AI Safety Fellowship 2026: $15,000資金
  - MATS: 12週間完全資助アライメント/制御/セキュリティ/ガバナンス研究
  - AI-Native資金: 2024-2025で17%増・$150億到達（他テック4%縮小）
  - UNIDIR Global Conference on AI Security and Ethics 2026開催
- **引用URL:** https://www.facebook.com/opportunitiesforyouth/posts/-anthropic-fellows-program-2026-fully-funded-artificial-intelligence-research-fe/1452179973606018/
- **Evidence ID:** EVD-20260619-0083

### INFO-084
- **タイトル:** 米国AI規制2026 — 連邦法不在も実効執行あり・Trump大統領令で州AI規制10年禁止・FTCが罰金
- **ソース:** VerifyWise / WIONews / Cato
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** 米国政府, OpenAI, Anthropic
- **要約:** 米国に連邦AI法はないが実効執行が存在。Colorado・California・Texas・IllinoisがアクティブなAI法を保有。FTCが企業に罰金。Trump最新法案は州AI規制の10年禁止を含み激しい反発を引き起こし nationwide debate。Great American AI ActはフロンティアAI開発者にOSSメンテナーへのモデルアクセス提供を求める。OpenAIとAnthropicは米国政府と合意しフロンティアモデルのテスト・安全性研究を提供。ジェイルブレイク懸念で政府行動誘発。
- **キーファクト:**
  - 米国: 連邦AI法不在も実効執行（FTC罰金）
  - 州法: Colorado・California・Texas・Illinoisがアクティブ
  - Trump法案: 州AI規制10年禁止・激しい反発
  - Great American AI Act: フロンティア開発者にOSSメンテナーへのモデルアクセス要求
  - OpenAI/Anthropic: 政府と合意でフロンティアモデルテスト・安全性研究提供
- **引用URL:** https://verifywise.ai/blog/state-of-ai-governance-regulations-united-states-2026
- **Evidence ID:** EVD-20260619-0084

### --- KIQ-BYTEDANCE-CHINESE: ByteDance/Doubao/Seed中国語一次情報の収集 ---

### INFO-085
- **タイトル:** 豆包DAU 2億人突破・日収入100万元未満・日コスト数千万元 — 収益化課題顕在化・Seedance企業転換
- **ソース:** 知乎 / 新浪财经 / Yahoo Finance HK / BossMind
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-BTD-001, KIQ-002-01
- **関連企業:** ByteDance
- **要約:** ByteDanceのAI助手「豆包」が2026年上半年に日次アクティブユーザー2億人を突破。しかし日収入は100万元（約2,000万円）未満で主にEC手数料。一方、火山引擎API価格・モデル毛利率・ユーザー行為から推算すると日コスト数千万元。Seedanceは企業客獲得に転換して収益化を図る。巨大ユーザー基数と深刻な収益化ギャップが表面化。
- **キーファクト:**
  - 豆包DAU: 2億人突破（2026 H1）
  - 日収入: 100万元（約2,000万円）未満・EC手数料中心
  - 日コスト: 数千万元（火山引擎API価格推算）
  - Seedance: 企業客獲得に転換・収益化模索
- **引用URL:** https://hk.finance.yahoo.com/news/ai%E7%AB%B6%E8%B3%BD-%E5%AD%97%E7%AF%80%E8%B1%86%E5%8C%85%E6%97%A5%E6%B4%BB%E9%80%BE2%E5%84%84-%E5%82%B3%E6%AF%8F%E6%97%A5%E6%94%B6%E5%85%A5%E4%B8%8D%E8%B6%B3%E7%99%BE%E8%90%AC-seedance%E8%BD%89%E6%94%BB%E4%BC%81%E6%A5%AD%E5%AE%A2%E7%8D%B2%E5%88%A9-063932035.html
- **Evidence ID:** EVD-20260619-0085

### INFO-086
- **タイトル:** 扣子(Coze) v3.0リリース・火山引擎が中国智能体開発プラットフォーム市場ダブル1位 — 企業向けゼロコードAgent
- **ソース:** 知乎 / 火山引擎 / CSDN / Taobao
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-01
- **関連企業:** ByteDance, 火山引擎
- **要約:** ByteDance系のCoze(扣子)が2026年6月にv3.0にアップグレード・企業向けゼロコードAgent開発デプロイ機能を提供。火山引擎が中国の智能体(エージェント)開発プラットフォーム市場で能力・市場シェア両方で1位(ダブル1位)を獲得。リアルタイム音声対話StartVoiceChat API提供。Cozeは低コード/ノーコード可視化プラットフォーム(LLMOps)として中国Agent生態系の中核的位置づけ。
- **キーファクト:**
  - Coze(扣子): 2026年6月 v3.0アップグレード
  - 火山引擎: 中国智能体開発プラットフォーム市場ダブル1位（能力・シェア）
  - 企業向けゼロコードAgent開発デプロイ提供
  - StartVoiceChat API: リアルタイム音声対話AI
- **引用URL:** https://zhuanlan.zhihu.com/p/2050221892016067387
- **Evidence ID:** EVD-20260619-0086

### INFO-087
- **タイトル:** Seedance 2.0 — ByteDance SEED研究所のマルチモーダルAI動画生成モデル・最大1080p 4-15秒・同期音声
- **ソース:** Atlas Cloud / MCPServers / App Store / Google Play
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-02, KIQ-BTD-001
- **関連企業:** ByteDance, SEED Lab
- **要約:** ByteDance系SEED研究所開発のSeedance 2.0がマルチモーダルAI動画生成モデルとして稼働中。テキストプロンプト・参照画像・音声断片を入力とし統一生成で高品質動画を出力。テキスト→動画・画像→動画・参照→動画を統一モデルでサポート、同期音声付き、最大1080p・4-15秒。inference.sh CLI経由で利用可能・プロ版・クイック版提供。即夢(Jimeng)プラットフォームで一般利用可。
- **キーファクト:**
  - Seedance 2.0: ByteDance SEED研究所開発マルチモーダル動画生成
  - 統一モデル: テキスト→動画・画像→動画・参照→動画対応
  - 最大1080p・4-15秒・同期音声
  - inference.sh CLI・即夢(Jimeng)プラットフォーム経由
  - プロ版・クイック版提供
- **引用URL:** https://www.atlascloud.ai/zh-TW/blog/guides/seedance-2.0-complete-guide
- **Evidence ID:** EVD-20260619-0087

### INFO-088
- **タイトル:** 【該当なし】「字节跳动 豆包 AI 最新」「ByteDance Seed 2.0 模型 发布」「字节跳动 AI 投资 融资」の3クエリで結果なし
- **ソース:** Firecrawl Search（web空配列）
- **公開日:** N/A
- **信頼性コード:** N/A
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 中国語クエリ6件のうち3件（「字节跳动 豆包 AI 最新」「ByteDance Seed 2.0 模型 发布」「字节跳动 AI 投资 融资」）がFirecrawl検索で結果空配列。tbs:qdr:w（1週間以内）制約と中国語検索インデックスカバレッジ制限が原因と推測。豆包DAU・Coze・Seedanceクエリからは有効データ取得済み。
- **キーファクト:**
  - 結果空: 「字节跳动 豆包 AI 最新」「Seed 2.0 模型 发布」「AI 投资 融资」
  - 有効取得: 豆包日活(Coze)・Seedance各1件ずつ
  - 原因推測: qdr:w制約 + 中国語インデックスカバレッジ制限
- **引用URL:** N/A
- **Evidence ID:** EVD-20260619-0088

### --- Step 4: 重要記事の詳細スクレイピング ---

### INFO-089 [KIQ-005-01] [Step4詳細]
- **タイトル:** AGI 2026年の実態 — DeepMind 5レベル枠組み・現状はLevel 1「Emerging」・予測市場2030年AGI 55%
- **ソース:** Delos (Louis Paul-Petit) (詳細スクレイピング)
- **公開日:** 2026-06-15
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI, Anthropic, Google / DeepMind, Microsoft
- **要約:** AGI到達状況の包括的分析。DeepMindの5レベル枠組み（Level 1 Emerging〜Level 5 Superhuman）に基づくと、2026年の最先端モデル（GPT-5.3, Claude Opus 4.6）は依然Level 1「Emerging」止まり。特定タスク（コーディング等）ではLevel 3-4に達するが汎用化が不十分。OpenAI: GPT-5(2025年8月)→GPT-5.3-Codex(2026年2月)・5原則AGI開発方針(2026年4月)。Anthropic: Claude Opus 4.6(2026年2月)→Sonnet 4.6(上位モデルの4分の1価格)・Claude CodeをMicrosoftが内部採用（GitHub Copilotの競合にも関わらず）。DeepMind: Hassabis「科学的・慎重アプローチ」・「レベル」で語る。Yann LeCun引用: 「AGIに取り組むならLLMに取り組むな」。
- **キーファクト:**
  - DeepMind 5レベル: L1 Emerging（現状）→L2 Competent（未到達）→L3 Expert→L4 Virtuoso→L5 Superhuman(ASI)
  - 現在の最先端モデル: 特定タスクでL3-4だが汎用化不足で総合L1
  - OpenAI: GPT-5(2025/8)→GPT-5.3-Codex(2026/2)・5原則AGI開発方針(2026/4)
  - Anthropic: Opus 4.6(2026/2)・Sonnet 4.6(4分の1価格)・Claude Code Microsoft内部採用
  - Kalshi予測市場(2026/4): OpenAI 2030年AGI到達55%
  - Amodei: 2027年までに「データセンター内の天才の国」likely
  - LeCun: 「AGIに取り組むならLLMに取り組むな」
  - 欠落: 幻覚・永続記憶なし・物理世界理解なし・意図・意識なし
- **引用URL:** https://www.delos.so/en/blog/agi-myth-or-reality-state-of-the-art-2026
- **Evidence ID:** EVD-20260619-0089

### INFO-090 [KIQ-005-01] [Step4詳細]
- **タイトル:** Yann LeCunがVivaTech会議でAMI Labs構想を全面解説 — JEPA・Project Tapestry・Meta退社経緯
- **ソース:** The AI Innovator (Deborah Yao) (詳細スクレイピング)
- **公開日:** 2026-06-17
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02, KIQ-001-01
- **関連企業:** AMI Labs, Meta, OpenAI, Anthropic, Google
- **要約:** VivaTech会議(パリ)でのLeCunインタビュー詳細。2025年11月Meta退社→AMI Labs設立の経緯を初公開。Meta内FAIR研究所のAMIプロジェクトが起源だが、MetaがLLM追従に方針転換したことで研究環境が悪化・長期研究に不適となった。JEPA(Joint Embedding Predictive Architecture): 全ピクセル/全単語予測でなく抽象表現学習→行動結果予測。信頼できるエージェントには「自身の行動の結果を予測する能力が不可欠」。Project Tapestry: 連合学習(federated training)でグローバル分散オープンAI基盤モデル構築・国家・大学・組織がデータ共有なしで知識貢献。少数企業寡占は文化的多様性と民主的アクセスを脅かすと警告。Llama 2公開がスタートアップ生態系立ち上げに貢献したと評価。
- **キーファクト:**
  - LeCun: 2025年11月Meta退社→AMI Labs設立（Meta FAIR内AMIプロジェクトが起源）
  - Meta方針転換: LLM追従のため長期研究環境悪化・公開制限議論
  - JEPA: 抽象表現学習→行動結果予測（全ピクセル/全単語予測の非採用）
  - エージェント信頼性: 「自身の行動結果を予測する能力が不可欠」
  - Project Tapestry: 連合学習でグローバル分散オープンAI基盤モデル
  - AI主権: 少数企業寡占は文化的多様性・民主的アクセスを脅かす
  - Llama 2: 公開がスタートアップ生態系立ち上げに貢献
  - 「ピルを飲んで催眠状態」: シリコンバレーのLLM monoculture批判
- **引用URL:** https://theaiinnovator.com/yann-lecun-llms-are-not-a-path-to-human-level-intelligence/
- **Evidence ID:** EVD-20260619-0090

### INFO-091 [KIQ-002-03] [Step4詳細]
- **タイトル:** 米国AI規制2026完全解説 — 連邦法不在も執行実態・州法カオス・Trump大統領令の州法挑戦・FTC「AIウォッシング」取締
- **ソース:** VerifyWise (詳細スクレイピング)
- **公開日:** 2026-05-15 (2026-06-12更新)
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-GOV-002, KIQ-005-03
- **関連企業:** 米国政府, FTC, NIST
- **要約:** 米国AI規制の包括的解説。連邦包括法不在でも複数の執行チャネル稼働中。Trump大統領令2本: (1)2025年1月EO 14179 - Biden AI安全命令撤回・AI導入障壁除去、(2)2025年12月 - 州AI法に挑戦するAI訴訟タスクフォース創設・州法が「過酷」なら連邦資金停止脅迫。ただし大統領令自体は連邦AI基準を創設せず・既存州法は無効化しない。3 exempt領域: 児童安全・AIコンピュート/データセンター・州政府AI調達。Colorado: AI法(SB 24-205)を廃止→SB 26-189(狭いADMT法)に代替(2027年1月1日発効)。California: Frontier AI Act(SB 53, 10^26 FLOPS超)・Training Data Transparency(AB 2013)・AI Transparency Act(SB 942)。Texas: TRAIGA(2026/1発効)・主に政府利用規制。FTC: Operation AI Comply・Workado(53%精度を98%と虚偽)・DoNotPay。NIST AI RMFがde facto標準化・財務省230管理目標にマッピング。
- **キーファクト:**
  - Trump EO 14179(2025/1): Biden AI安全命令撤回
  - Trump EO(2025/12): AI訴訟タスクフォース・州法挑戦メカニズム創設
  - Exempt領域: 児童安全・コンピュートインフラ・州政府調達
  - Colorado: SB 24-205廃止→SB 26-189(ADMT法)代替(2027/1/1)
  - California SB 53: 10^26 FLOPS超モデルにリスク枠組み公開義務・最大$1M罰金
  - California AB 2013: 訓練データ透明性・データセット公開義務
  - Texas TRAIGA: 政府利用中心・民間義務最小限
  - FTC Operation AI Comply: Workado(98%虚偽→実際53%)・DoNotPay・Growth Cave
  - NIST AI RMF: de facto標準・財務省230管理目標マッピング
  - House共和党(2025/5): 州AI法10年禁止条項を予算法案に挿入試みるも失敗
- **引用URL:** https://verifywise.ai/blog/state-of-ai-governance-regulations-united-states-2026
- **Evidence ID:** EVD-20260619-0091

### INFO-092 [KIQ-BTD-001] [Step4詳細]
- **タイトル:** 豆包2億DAUの収益化危機詳細 — 日コスト数千万元・ByteDance 2026年資本支出2000億元超・NVIDIA需要逼迫
- **ソース:** 新浪财经 / 晚点LatePost (詳細スクレイピング)
- **公開日:** 2026-06-17
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-BTD-001, KIQ-002-01
- **関連企業:** ByteDance, NVIDIA
- **要約:** 晚点LatePost報道による豆包収益化の詳細。2026年上半年にDAU 2億人突破も日収入100万元（約2,000万円）未満・EC手数料中心。日コスト数千万元（火山引擎API価格推算）。テキストチャットは1人日数銭だが、画像認識・音声/動画チャット等マルチモーダル機能のコンピュートコストは数十倍。訓練用智算センター建設コスト別途（数万枚AIチップ+データセンター+電力+冷却）。ByteDance 2026年資本支出を2000億元超（2025年利益の約6割）に上方修正。NVIDIAカード・国産推論カードがさらに確保できれば消費リソースは更に増大。巨大ユーザー規模と深刻な赤字構造の二面性。
- **キーファクト:**
  - DAU 2億人・日収入100万元未満(EC手数料中心)
  - 日コスト数千万元（火山引擎API推算）
  - テキストチャット: 1人日数銭(15-20分使用)・マルチモーダルは数十倍コスト
  - 智算センター: 数万枚AIチップ+インフラ（訓練コスト別途）
  - ByteDance 2026年資本支出: 2000億元超（2025年利益の約6割）
  - 制約: NVIDIA/国産推論カード調達が制限要因
- **引用URL:** https://cj.sina.com.cn/articles/view/5952915705/162d248f9067034ids
- **Evidence ID:** EVD-20260619-0092

### INFO-093 [KIQ-002-06] [Step4詳細]
- **タイトル:** The Economist: トランプ政権のAnthropic制限措置の詳細 — Fable 5・Mythos 5の非米国人アクセス遮断が史上初の強制フロンティアAI撤回
- **ソース:** The Economist (Judith Dada) (詳細スクレイピング)
- **公開日:** 2026-06-18
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-GOV-001, KIQ-GOV-002, KIQ-005-03
- **関連企業:** Anthropic, 米国政府, 欧州各国
- **要約:** Economist寄稿(Judith Dada)。トランプ政権のAnthropic命令はFable 5とMythos 5への非米国人アクセス遮断を命じたもので、政府が公開済みフロンティアAIモデルを強制的に撤回させた史上初の事例。欧州はこれを技術的大激変・地政学的硬化・生活根本変容の時代における早期の警告ショットと受け取るべき。欧州はAI主権構築のための資本改革・コンピュート拡大・労働柔軟性を含む平時で最も野心的な政治課題が必要。AI中堅国が連合で交渉地位を強化しフロンティアAIアクセスを確保する戦略を提唱。（※Economist誌は有料登録制のため本文は限定的）
- **キーファクト:**
  - Anthropic制限対象モデル: Fable 5・Mythos 5（非米国人アクセス遮断）
  - 史上初: 政府が公開済みフロンティアAIを強制撤回
  - 欧州対応: AI主権構築（資本改革・コンピュート拡大・労働柔軟性）
  - 提言: AI中堅国連合でフロンティアAIアクセス確保
  - 筆者: Judith Dada（La Famiglia/General Catalyst）
- **引用URL:** https://www.economist.com/by-invitation/2026/06/18/how-europe-must-respond-to-americas-ai-warning-shot
- **Evidence ID:** EVD-20260619-0093

### INFO-094 [KIQ-001-02] [Step4詳細]
- **タイトル:** Seedance 2.0完全ガイド — ByteDance SEED研究所の統一マルチモーダル動画生成・テキスト/画像/参照→動画・同期音声・1080p
- **ソース:** Atlas Cloud (詳細スクレイピング)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-02, KIQ-BTD-001
- **関連企業:** ByteDance, SEED Lab
- **要約:** Seedance 2.0の技術仕様詳細。ByteDance系SEED研究所が開発したマルチモーダルAI動画生成モデル。テキストプロンプト・参照画像・音声断片を入力とし単一の統一生成プロセスで高品質動画を出力。3モード対応: テキスト→動画・画像→動画・参照→動画。すべて同期音声付き・最大1080p解像度・4-15秒。inference.sh CLI経由で利用可能・プロ版（高品質）・クイック版（高速）の2ティア。即夢(Jimeng)プラットフォーム経由で一般ユーザーもアクセス可能。App Store/Google Playアプリ（绘影字幕）にも組み込み済み。
- **キーファクト:**
  - 入力: テキスト・参照画像・音声断片 → 統一生成で高品質動画
  - 3モード: テキスト→動画・画像→動画・参照→動画
  - 同期音声付き・最大1080p・4-15秒
  - 2ティア: プロ版(高品質)・クイック版(高速)
  - アクセス: inference.sh CLI・即夢(Jimeng)プラットフォーム・モバイルアプリ
  - 開発: ByteDance SEED Lab
- **引用URL:** https://www.atlascloud.ai/zh-TW/blog/guides/seedance-2.0-complete-guide
- **Evidence ID:** EVD-20260619-0094

### INFO-095 [KIQ-002-03] [Step4詳細]
- **タイトル:** Great American AI Actプライマー — フロンティア開発者にOSSメンテナーへのモデルアクセス提供要求・州能力構築目標
- **ソース:** Cato Institute (Juan Londoño) (詳細スクレイピング)
- **公開日:** 2026-06-17
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-GOV-002, KIQ-005-03
- **関連企業:** 米国政府, OpenAI, Anthropic
- **要約:** Cato InstituteによるGreat American AI Actの分析。法案は大規模フロンティアAI開発者に広く使用される重要OSSメンテナーへのモデルアクセス提供を求める点が注目。州の能力構築とAI時代への効果的適応準備を政策優先とすべきと評価。ただしCato本文はスクレイピング制限で限定的。
- **キーファクト:**
  - Great American AI Act: フロンティアAI開発者にOSSメンテナーへのモデルアクセス提供を要求
  - 州能力構築・AI時代適応準備を政策優先と評価
  - Cato Institute: リバタリアン系シンクタンク
- **引用URL:** https://www.cato.org/blog/primer-great-american-artificial-intelligence-act
- **Evidence ID:** EVD-20260619-0095

### INFO-096 [KIQ-005-03] [Step4詳細]
- **タイトル:** UK政府「AI Scenarios 2030」 — 政策立案者向け未来シナリオ・2023年開発→2025年4月公開→2026年更新
- **ソース:** UK Government Office for Science (GO-Science) (詳細スクレイピング)
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03, KIQ-GOV-002
- **関連企業:** UK Government, OECD
- **要約:** 英国Government Office for Science(GO-Science)が政策立案者向けにAI 2030シナリオを公開。2023年に開発・2025年4月に初版公開→2026年更新版。Our World in Data(2026)の外部資金データを活用（$150万以上調達の非上場AI企業）。OECD Digital Government Outlook 2026と連動: クラウドコンピューティング基盤は solidifying するが他のデジタルインフラは未成熟。AI-Native企業への資金が2024-2025で17%増加し$150億到達。UNIDIR Global Conference on AI Security and Ethics 2026(AISE26)が開催予定。
- **キーファクト:**
  - UK GO-Science: AI 2030シナリオ(2023開発→2025/4公開→2026更新)
  - データソース: Our World in Data(2026)・AI企業外部資金($150万+)
  - OECD Digital Government Outlook 2026: クラウドはsolidifying・他インフラ未成熟
  - AI-Native資金: 2024-2025で17%増・$150億到達
  - UNIDIR AISE26: Global Conference on AI Security and Ethics 2026
- **引用URL:** https://www.gov.uk/government/publications/ai-scenarios-2030-helping-policymakers-plan-for-the-future-of-ai/ai-scenarios-2030-helping-policymakers-plan-for-the-future-of-ai
- **Evidence ID:** EVD-20260619-0096
