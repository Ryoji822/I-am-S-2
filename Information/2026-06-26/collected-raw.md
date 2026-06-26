# 収集データ: 2026-06-26

## メタデータ
- 収集日時: 2026-06-26 00:00 UTC
- 実行クエリ数: 122 / 117 (計画117件 + 動的追加5件)
- scrape実行数: 6件 (Anthropic公式4件 + Fable/Mythos停止1件 + 検索スクレイピング多数)
- 収集情報数: 55件
- Evidence ID 採番範囲: EVD-20260626-0001 〜 EVD-20260626-0055
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 動的追加クエリ: KIQ-MIL-001 ✓ (Grok標的選定関与度), KIQ-OAI-001 ✓ (OpenAI収益内訳), H-ANT-002 DAU ✓ (該当なし7R継続), 調達強制実効性 ✓, AI spending wall ✓
- 企業カバレッジ: OpenAI ✓, Anthropic ✓, Google ✓, xAI ✓, ByteDance ✓, AWS ✓, Azure ✓, Meta ✓, DeepSeek ✓, Mistral ✓, Alibaba ✓, Qualcomm ✓
- 品質フラグ: NORMAL

## 収集結果

### INFO-001
- **タイトル:** 2028: Two scenarios for global AI leadership
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06, KIQ-002-03, KIQ-005-01
- **関連企業:** Anthropic, Google, ByteDance, DeepSeek
- **要約:** Anthropicが米中AI競争に関する政策論文を発表。計算資源(compute)の優位性を民主主義国家が維持するため、輸出規制の抜け穴閉鎖・蒸留攻撃(distillation attacks)対策・アメリカAI輸出促進の3本柱を提案。Mythos Previewモデルの威力（Firefoxが2025年全年分以上のセキュリティバグを1ヶ月で修正）を実例として挙げ、2026年が民主主義国家のAI優位を固定する決定的窓口と位置づけた。
- **キーファクト:**
  - Huaweiは2026年にNVIDIA総合計算能力の4%、2027年には2%しか生産しない見込み
  - 米国が規制を強化すれば中国に対し約11倍のcompute格差を確保可能
  - DeepSeek R1-0528は脱獄技術で94%の悪意ある要求に応じた（米国参照モデル8%）
  - Mythos Previewは自律的セキュリティ脆弱性発見能力で「機関銃に対して刀を研いでいる」状態を中国にもたらした
  - PRCラボは蒸留攻撃を「バックドア」としてAI開発の中核に依存
  - 議会下院は369-22でデータセンター海外アクセス規制法案を可決（上院未通過）
- **引用URL:** https://www.anthropic.com/news/2028-ai-leadership
- **Evidence ID:** EVD-20260626-0001

### INFO-002
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropic LabsがClaude Designを発表。Claude Opus 4.7のビジョンモデルを活用し、デザイン・プロトタイプ・スライド・ワンポスター等の視覚的成果物をClaudeと共同作成できるツール。Pro/Max/Team/Enterprise向けにリサーチプレビュー提供。ブランドデザインシステムの自動適用、Canva/PPTX/HTMLエクスポート、Claude Codeへのハンドオフ機能を搭載。Canva、Brilliant、Datadogがパートナーとして言及。
- **キーファクト:**
  - Claude Opus 4.7（最強ビジョンモデル）で駆動
  - コードベース・デザインファイルを読み込んでブランドシステムを自動構築
  - Claude Codeへのワンクリック・ハンドオフでデザイン→実装パイプラインを統合
  - Datadog: 「1週間のやり取りが1回の会話で完了」
  - Enterpriseはデフォルトオフ、管理者が明示的に有効化が必要
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260626-0002

### INFO-003
- **タイトル:** Anthropic appoints Irina Ghose as Managing Director of India
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-01-16
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Anthropicがインド・ベンガルール初オフィス開設に先立ち、元Microsoft IndiaマネージングディレクターのIrina Ghoseをインド代表として採用。Claude.aiのインドは世界第2位の市場。Anthropic第4回経済指数でインドユーザーの約半数がコンピュータ・数学タスクに集中。
- **キーファクト:**
  - 元Microsoft India MD、30年以上のテクノロジービジネス経験
  - インドはClaude.ai世界第2位市場
  - インドユーザーの約50%がコンピュータ・数学タスクに集中（Anthropic経済指数）
- **引用URL:** https://www.anthropic.com/news/anthropic-appoints-irina-ghose-as-managing-director-of-india
- **Evidence ID:** EVD-20260626-0003

### INFO-004
- **タイトル:** Anthropic's Long-Term Benefit Trust appoints Vas Narasimhan to Board of Directors
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-04-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Novartis CEOのVas NarasimhanがAnthropic取締役会にLTBT指名で就任。Trust指名取締役が過半数を占める構造が確認された。35以上の新薬開発・承認を監督した医療・ライフサイエンス専門家として、規制産業での安全な技術展開経験をもたらす。
- **キーファクト:**
  - Trust指名取締役が取締役会の過半数（ガバナンス構造確認）
  - 35以上の新薬開発・承認監督経験
  - 現在の取締役: Dario Amodei, Daniela Amodei, Yasmin Razavi, Jay Kreps, Reed Hastings, Chris Liddell, Vas Narasimhan
- **引用URL:** https://www.anthropic.com/news/narasimhan-board
- **Evidence ID:** EVD-20260626-0004

### INFO-005
- **タイトル:** Statement on the US government directive to suspend access to Fable 5 and Mythos 5
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06, KIQ-005-03, KIQ-005-01
- **関連企業:** Anthropic, OpenAI
- **要約:** 米国政府が国家安全保障権限に基づき、全外国籍ユーザー（米国内・外を問わず、Anthropicの外国籍従業員を含む）のFable 5・Mythos 5へのアクセスを停止する輸出管理指令を発出。効果として全顧客のアクセスを停止。政府はFable 5の脱獄(jailbreak)手法を発見したと主張するが、Anthropicは「狭い非普遍的脱獄」でありOpenAI GPT-5.5でも同等能力が利用可能と反論。他モデルには影響なし。
- **キーファクト:**
  - 政府からの指令受領: 2026-06-12 17:21 ET、即時全面停止
  - 政府は具体的な国家安全保障懸念の詳細を提示せず
  - 脱獄手法は「コードベースを読んでバグを修正するよう依頼する」程度の能力
  - Anthropic: 「この基準を業界全体に適用すれば全フロンティアモデルの新規展開が停止する」
  - 30日間データ保持ポリシー（顧客コストあり）を防御の深さ戦略として採用済み
  - 汎用脱獄(universal jailbreak)はまだ発見されていない
- **引用URL:** https://www.anthropic.com/news/fable-mythos-access
- **Evidence ID:** EVD-20260626-0005

### INFO-006
- **タイトル:** OpenAI and Broadcom Unveil LLM-Optimized Intelligence Processor "Jalapeño"
- **ソース:** TechCrunch / Broadcom公式プレスリリース
- **公開日:** 2026-06-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-04, KIQ-005-01
- **関連企業:** OpenAI, Broadcom
- **要約:** OpenAIがBroadcomと共同開発した初のカスタム推論プロセッサ「Jalapeño」を発表。LLM推論に最適化された設計で、OpenAIのAIインフラの自立化を加速。推論コスト削減とパフォーマンス向上が期待される。
- **キーファクト:**
  - OpenAI初の自社設計推論チップ
  - Broadcomとの共同設計・製造
  - インフラ自立化の次段階（Google TPU/Amazon Trainiumに続く垂直統合）
- **引用URL:** https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/
- **Evidence ID:** EVD-20260626-0006

### INFO-007
- **タイトル:** White House asks OpenAI to stagger release of GPT 5.6 over security concerns
- **ソース:** Reuters / The Information / KTEN
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** トランプ政権がOpenAIに対し、次期GPT 5.6モデルのリリースを段階的にずらすよう要請。高度な能力に対する安全保障懸念を理由に、政府承認パートナー少数への限定リリースを求めている。Fable 5/Mythos 5停止に続く政府によるフロンティアモデル規制の連鎖。KIQ-002-06（政府によるAI企業への経済的圧力）の中核事例。
- **キーファクト:**
  - GPT 5.6のリリースを政府が直接的に制限する要請
  - Fable 5/Mythos 5停止（INFO-005）と同時期の別アクション
  - 政府承認パートナーのみへの限定リリースを要求
  - 複数メディア（Reuters, The Information, KTEN）で確認
- **引用URL:** https://www.reuters.com/business/trump-administration-asks-openai-stagger-release-new-model-information-reports-2026-06-25/
- **Evidence ID:** EVD-20260626-0007

### INFO-008
- **タイトル:** OpenAI leans toward waiting until next year for IPO, targeting up to $1 trillion valuation
- **ソース:** Reuters (NYT報道引用)
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIがIPOを来年まで見送る方向で検討中。最大1兆ドルの評価額をターゲット。Anthropicの$965B評価額に迫る水準。政府規制の不確実性（GPT 5.6リリース制限・Jalapeño発表）がIPOタイミングに影響している可能性。
- **キーファクト:**
  - IPO見送り（2027年見込み）
  - ターゲット評価額: 最大$1T（兆ドル）
  - NYT報道をReutersが確認
- **引用URL:** https://www.reuters.com/business/trump-administration-asks-openai-stagger-release-new-model-information-reports-2026-06-25/
- **Evidence ID:** EVD-20260626-0008

### INFO-009
- **タイトル:** Google's Gemini 3.5 Pro Release Slips to July
- **ソース:** Business Insider
- **公開日:** 2026-06-24
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01
- **関連企業:** Google / DeepMind
- **要約:** Googleの次期フロンティアAIモデルGemini 3.5 Proのリリースが6月から7月に延期。計画通り6月に展開予定だったが、何らかの理由でずれ込んだ。Gemini OmniおよびGemini 3.5 FlashはI/O 2026で発表済み。
- **キーファクト:**
  - Gemini 3.5 Pro: 6月予定→7月延期
  - Gemini Omni・Gemini 3.5 FlashはI/O 2026で発表済み
  - フロンティア競争でのGoogleの遅れリスク
- **引用URL:** https://www.businessinsider.com/google-3-5-pro-july-release-tokens-ai-agents-model-2026-6
- **Evidence ID:** EVD-20260626-0009

### INFO-010
- **タイトル:** SpaceX initiates first bond sale; xAI faces Colossus integration issues
- **ソース:** Yahoo Finance
- **公開日:** 2026-06-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, KIQ-001-01
- **関連企業:** xAI, SpaceX
- **要約:** SpaceXが初の債券発行を開始。xAIがGrokとColossus 1/2の統合に課題を抱えているとの報道。xAIの計算インフラ統合の技術的困難が浮上。IPO後のSpaceX/株価調整の文脈。
- **キーファクト:**
  - SpaceX初の債券発行
  - xAI: Grok-Colossus統合の技術的課題
  - 株価がIPO後利益を失いつつある
- **引用URL:** https://finance.yahoo.com/video/spacex-initiates-first-bond-sale-while-the-stock-sheds-post-ipo-gains-195906531.html
- **Evidence ID:** EVD-20260626-0010

---

## 動的追加クエリ（Arbiterフィードバック Step 1.5）
- KIQ-MIL-001: "Grok AI autonomous targeting weapons military human override decision"
- KIQ-OAI-001: "OpenAI revenue breakdown API enterprise consumer ChatGPT subscription 2026"
- H-ANT-002 DAU: "Claude Code daily active users DAU install numbers metrics 2026"
- KIQ-002-06 調達強制: "Anthropic federal procurement revenue SCR designation impact 2026"
- AI spending wall: "AI spending wall ROI diminishing returns enterprise 2026"

### INFO-011
- **タイトル:** Pentagon Declares Grok AI Helped Fire 2,000 Missiles at Iran in Operation Epic Fury
- **ソース:** Yahoo News / Pentagon声明
- **公開日:** 2026-06 (過去1週間)
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001（動的追加）, KIQ-002-06, KIQ-005-03
- **関連企業:** xAI, SpaceX, 米国防総省
- **要約:** ペンタゴンが「Operation Epic Fury」でxAIのGrok Gov Modelが96時間で2,000発の弾薬の誘導を支援したことを確認。Grokが自律的に標的を決定したかは不明。「公的に入手可能な情報はGrokが自律的に標的を決定した、あるいはミサイル発射を直接制御したことを示していない」。軍事意思決定サイクル(OODA)を人間アナリストを超える速度に圧縮した効果。
- **キーファクト:**
  - Grok Gov Model: 96時間・2,000標的の弾薬誘導支援
  - 人間の最終決定権: 「軍の指揮官が自律的/半自律的システムの最終決定を保持する」必要
  - Grokが自律的に標的選定・ミサイル発射を直接制御した証拠は「公表情報では示されていない」
  - OODAループ全体を人間アナリストを超える速度に圧縮
- **引用URL:** https://www.yahoo.com/news/politics/articles/pentagon-declares-grok-ai-helped-005214359.html
- **Evidence ID:** EVD-20260626-0011

### INFO-012
- **タイトル:** OpenAI Statistics 2026: Enterprise 40%+ of revenue, targeting parity with consumer by end 2026
- **ソース:** Panto AI (OpenAI公式データ引用)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-OAI-001（動的追加）, KIQ-003-04, KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIの収益構造データ。Enterpriseが収益の40%以上を占め、2026年末までにConsumer収益と同額に達する見込み。ARRは$1B(2025年1月)→$9B(2025年末)→$30Bターゲット。300,000+のビジネス顧客(Q1 2026)、収益の80%がエンタープライズ契約。2025年に$3.9Bの損失。
- **キーファクト:**
  - Enterprise: 収益の40%+、2026年末にConsumerと同額を目標
  - ARR: $1B(2025年1月) → $9B(2025年末) → $30B(ターゲット)
  - 300,000+ビジネス顧客（Q1 2026）
  - 収益の80%がエンタープライズ契約
  - 2025年損失: $3.9B
  - 収益は2025年に$3.7B→$13.1Bに3倍増
- **引用URL:** https://www.getpanto.ai/blog/openai-statistics
- **Evidence ID:** EVD-20260626-0012

### INFO-013
- **タイトル:** Anthropic's Claude winning over paid consumers; Claude revenue up 75% since January 2026
- **ソース:** TechCrunch
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001（動的追加）, KIQ-003-04, KIQ-003-01
- **関連企業:** Anthropic, OpenAI
- **要約:** AnthropicのClaudeが有料コンシューマー市場でChatGPTからシェアを奪っている。Claudeの有料コンシューマーと収益が月ごとに成長、2026年1月から約75%増。Anthropicは2026年初頭に$9Bのランレート収益で開始。ChatGPTが長年支配していた市場での初のシェア奪取。
- **キーファクト:**
  - Claude有料コンシューマー収益: 2026年1月から75%増
  - Anthropicランレート収益: $9B（2026年初頭）
  - ChatGPT支配市場での初のシェア奪取
- **引用URL:** https://techcrunch.com/2026/06/25/anthropics-claude-is-winning-over-paid-consumers-a-market-owned-by-chatgpt/
- **Evidence ID:** EVD-20260626-0013

### INFO-014
- **タイトル:** Claude Code DAU metrics — 該当データなし（7R連続不在継続）
- **ソース:** 検索結果該当なし
- **公開日:** 2026-06-26
- **信頼性コード:** F-4
- **関連KIQ:** H-ANT-002（動的追加・Arbiter優先）, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude CodeのDAU（日次アクティブユーザー）またはインストール数の具体的な公開データは発見できず。Arbiter警告の「7R連続不在」が継続。AnthropicのUsage Analyticsページは存在するがTeam/Enterprise向けのみで、公開DAU/インストール数は非開示。次回ラウンドでmedium→low移行検討の正式リスクが高まる。
- **キーファクト:**
  - Claude Code DAU公開データ: 該当なし（7R連続継続）
  - Anthropic Usage Analytics: Team/Enterprise向けのみ、公開指標なし
  - Arbiter警告: 7R連続不在でmedium→low移行検討必須
- **引用URL:** 該当なし
- **Evidence ID:** EVD-20260626-0014

### INFO-015
- **タイトル:** "AI Spending Wall" — ROI逓減の定量データ複数確認
- **ソース:** HBR / LinkedIn / Gary Gensler発言
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04（Arbiter優先：spending wall独立検証）, SCN-002/004
- **関連企業:** OpenAI, Uber
- **要約:** AI投資のROI逓減（"spending wall"）を裏付ける複数の定量データ。HBR: 95%のエンタープライズAIパイロットが測定可能なROIを生み出さない。81%の企業がAI ROIを定量化できない。AI支出は2026年に$2.52T（前年比44%増）。Uberが2026年AI予算全体を4ヶ月で使い切り。Sam Altman: 「AIコストは今や巨大な問題」。
- **キーファクト:**
  - 95%のエンタープライズAIパイロットがROIを生み出さない（HBR）
  - 81%の企業がAI ROIを定量化できない
  - AI支出: $2.52T（2026年・前年比44%増）
  - Uber: 2026年AI予算全体を4ヶ月で消費
  - Sam Altman: 「2026年初頭にはAIコストはほとんど話題にならなかったが、今は巨大な問題」
  - Gary Gensler: AI投資正当化には「投資に見合う収益」と「明確なROI」が必要
- **引用URL:** https://www.facebook.com/HBR/posts/1375345297793994/
- **Evidence ID:** EVD-20260626-0015

---

## KIQ-001-01: 各社のAgent SDK/APIの機能拡張ロードマップ

### INFO-016
- **タイトル:** OpenAI shipped 30+ models/features in 6 months; new agents research paper published
- **ソース:** OpenAI LinkedIn / openai.com
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIが過去6ヶ月で30以上のモデル・機能を出荷。APIで12以上のモデルを提供（GPTメインライン、リアルタイム音声、画像）。Agent SDK（openai-agents-python）でマルチエージェントワークフロー構築が可能。コスト・レイテンシ最適化のためのモデルバリエーション展開。「How agents are transforming work」研究論文発表。
- **キーファクト:**
  - 過去6ヶ月で30+モデル/機能出荷
  - API: 12以上のモデル（GPT、リアルタイム音声、画像）
  - Agents SDK: openai-agents-python、マルチエージェントワークフロー対応
  - ツール永続化・セッション履歴・専門家ハンドオフ機能
  - エージェントがより長く複雑なタスクを処理する能力を示す研究論文
- **引用URL:** https://openai.com/index/how-agents-are-transforming-work/
- **Evidence ID:** EVD-20260626-0016

### INFO-017
- **タイトル:** Google Interactions API GA — unified endpoint for Gemini models and agents
- **ソース:** Google公式ブログ
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Google / DeepMind
- **要約:** GoogleがGeminiモデルとエージェントのための統一エンドポイント「Interactions API」をGA提供開始。サーバーサイド状態保持、バックグラウンド実行、ツール組み合わせ、マルチモーダル生成を単一インターフェースで提供。Gemini SkillsとDeep Research Agentも展開。
- **キーファクト:**
  - Interactions API: Geminiモデル/エージェントの統一エンドポイント（GA）
  - サーバーサイド状態保持で会話状態をGoogle側で管理
  - バックグラウンド実行・ツール組み合わせ・マルチモーダル生成
  - Gemini Deep Research Agent: 自律的に複数ステップの研究を実行・統合
  - Gemini Skills: GitHub公開、テキスト生成/チャット/関数呼び出し/構造化出力/画像対応
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/
- **Evidence ID:** EVD-20260626-0017

### INFO-018
- **タイトル:** xAI Grok Voice Agent API and Grok Build 0.1 coding model launched
- **ソース:** xAI公式ドキュメント/ニュース
- **公開日:** 2026-05-29
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIがGrok Voice Agent API（OpenAI Realtime API互換）とコーディングモデル「Grok Build 0.1」を公開ベータで提供開始。関数呼び出し、OAuth認証、Hermes Agent統合をサポート。
- **キーファクト:**
  - Grok Voice Agent API: OpenAI Realtime API互換（ベースURL変更で移行可能）
  - Grok Build 0.1: 最速のコーディングモデル、xAI APIで公開ベータ
  - Function Calling: データベース・API・外部システム統合
  - Hermes Agent: xAI Grok OAuth・ネイティブweb_search/x_search対応
- **引用URL:** https://docs.x.ai/developers/model-capabilities/audio/voice-agent
- **Evidence ID:** EVD-20260626-0018

### INFO-019
- **タイトル:** ByteDance open-sources DeerFlow 2.0 and UI-TARS multimodal agent
- **ソース:** Facebook / GitHub / X
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceがDeerFlow 2.0（LangGraphベースのAI研究アシスタント・エージェントフレームワーク）をオープンソース化。UI-TARS Desktop + Agent TARS（画面認識・クリック・フォーム入力で人間のように操作するマルチモーダルエージェント）も発表。Cozeプラットフォームは最大8並列エージェントに対応（2026年2月アップデート）。
- **キーファクト:**
  - DeerFlow 2.0: LangGraphベース、サブエージェント調整（研究・コード実行・Web閲覧）
  - UI-TARS Desktop + Agent TARS: 完全マルチモーダル（画面認識・UI操作・フォーム入力）
  - Coze: 最大8並列エージェント対応（2026年2月アップデート）
  - ByteDance: 自社用AIチップ設計でCoze等のエージェント製品をサポート
- **引用URL:** https://www.facebook.com/datasciencedojo/posts/1034772602406224/
- **Evidence ID:** EVD-20260626-0019

### INFO-020
- **タイトル:** Agent SDK comparison 2026: LangGraph leads state control, vendor SDKs maturing
- **ソース:** Requesty / Reddit / madebyagents.com
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** 2026年のエージェントSDK比較: LangGraphが状態制御で首位、CrewAIが迅速なプロトタイピングで首位。ベンダーSDK（OpenAI Agents SDK、Anthropic、Google）は本番展開向けに成熟。Neurolinkは12+プロバイダー統合でマルチベンダー対応。標準化が進む中、ベンダーロックイン回避がテーマ。
- **キーファクト:**
  - LangGraph: 状態管理ワークフローで首位
  - CrewAI: ロール/タスク・迅速プロトタイピングで首位
  - ベンダーSDK（OpenAI/Anthropic/Google）: 本番展開向けに成熟
  - Neurolink: 12+プロバイダー統合（マルチベンダー戦略）
  - 9つの主要AIエージェントプラットフォーム: Salesforce, Microsoft, Google, Domo, AWS, Kore.ai, Vellum AI等
- **引用URL:** https://www.requesty.ai/blog/best-ai-agent-sdks-compared-2026-langchain-crewai-openai-anthropic-google
- **Evidence ID:** EVD-20260626-0020

---

## KIQ-001-02: エンタープライズ向けAgent展開（セキュリティ認証・SLA）

### INFO-021
- **タイトル:** OpenAI GPT-5.5/Codex on AWS Bedrock with Bedrock Managed Agents layer
- **ソース:** Cloudelligent
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI, Amazon (AWS)
- **要約:** AWSがOpenAI旗艦モデル（GPT-5.5、GPT-5.4、Codex）をAmazon Bedrockに追加。新エージェント展開レイヤー「Bedrock Managed Agents」も提供。OpenAI Enterprise: SOC 2準拠、FedRAMP対応は限定的。SOC 2 Type II、ISO 27001、PCI DSS、FedRAMP、GDPRが主要エンタープライズ認証フレームワーク。
- **キーファクト:**
  - GPT-5.5・GPT-5.4・CodexがAWS Bedrockに追加
  - Bedrock Managed Agents: 新エージェント展開レイヤー
  - OpenAI Enterprise: SOC 2準拠、FedRAMP対応は限定的
  - 50%以上のエンタープライズチームがAIエージェントをパイロット中
- **引用URL:** https://cloudelligent.com/blog/openai-models-on-aws-smb-guide/
- **Evidence ID:** EVD-20260626-0021

### INFO-022
- **タイトル:** Claude Enterprise: SOC 2 Type II, ISO 27001, HIPAA achievable at Enterprise tier
- **ソース:** Truefoundry / IntuitionLabs / Strac
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude EnterpriseはSOC 2 Type II・ISO 27001に準拠。HIPAAコンプライアンスはEnterprise tierのみで達成可能（AnthropicデフォルトではHIPAA非対応）。Security Controls Assurance Leadを採用中で、SOC 2、ISO 27001/42001、HIPAA、公共部門向けのグローバルコンプライアンスを強化。
- **キーファクト:**
  - SOC 2 Type II・ISO 27001準拠
  - HIPAA: Enterprise tierのみで達成可能（デフォルトは非対応）
  - Security Controls Assurance Lead採用中（SOC 2, ISO 27001/42001, HIPAA, 公共部門）
  - Claude Code/Coworkのエンタープライズガバナンス: SSO、6つの制御レイヤー
- **引用URL:** https://www.truefoundry.com/blog/claude-enterprise-security
- **Evidence ID:** EVD-20260626-0022

### INFO-023
- **タイトル:** Google Vertex AI → Gemini Enterprise Agent Platform rebrand with latency SLA
- **ソース:** Google Cloud公式 / TechnologyMatch
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** GoogleがVertex AIを「Gemini Enterprise Agent Platform」にリブランド。Provisioned Throughputにトークン/秒のレイテンシSLAを追加（最初のトークンから最後まで計測）。エンタープライズ向けエージェントオーケストレーション層を提供。Developer APIとEnterprise Agent Platform APIの2製品構成。
- **キーファクト:**
  - Vertex AI → Gemini Enterprise Agent Platformリブランド
  - Tokens-per-second latency SLA on Provisioned Throughput
  - エンタープライズグレードのエージェントオーケストレーション層
  - 2製品構成: Developer API / Enterprise Agent Platform API
- **引用URL:** https://cloud.google.com/vertex-ai/generative-ai/sla
- **Evidence ID:** EVD-20260626-0023

---

## KIQ-001-03: Agent開発者エコシステムの拡大状況

### INFO-024
- **タイトル:** MCP specification 2026-07-28 release candidate with stateless protocol core and Extensions framework
- **ソース:** MCP公式ブログ / Microsoft Learn / Stacklok
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic, Microsoft (Azure)
- **要約:** Model Context Protocol（MCP）の次期仕様リリース候補が公開。ステートレスプロトコルコア、Extensions framework、Tasks機能を追加。シンプルなサーバーは数百行で実装可能という低参入障壁が普及の主因。Azure MCP Serverも提供開始。
- **キーファクト:**
  - MCP 2026-07-28 RC: ステートレスプロトコルコア・Extensions framework・Tasks追加
  - 低参入障壁: シンプルサーバーは数百行で実装可能
  - Azure MCP Server: Microsoft提供でAzureリソース統合
  - MCPサーバー: 外部コンテキスト・能力をAIアプリに公開する標準インターフェース
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260626-0024

### INFO-025
- **タイトル:** AAIF (Agentic AI Foundation) under Linux Foundation advancing open standards — MCP, Goose, AGENTS.md
- **ソース:** AAIF公式 / LinkedIn / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Linux Foundation (中立的)
- **要約:** Agentic AI Foundation（AAIF）がLinux Foundationの一部として、エージェントAI時代のオープン標準を推進。MCP、Goose、AGENTS.md等の標準・プロトコル・オープンソースプロジェクトを統合。中立的でオープンな基盤として、グローバルなエージェントシステムの設計・実装・採用を加速。
- **キーファクト:**
  - AAIF: Linux Foundation傘下、中立的・オープンな基盤
  - 標準: MCP, Goose, AGENTS.md等を推進
  - ミッション: 標準・プロトコル・OSSプロジェクトの統合によるエージェントAI普及
- **引用URL:** https://aaif.io/staff/
- **Evidence ID:** EVD-20260626-0025

### INFO-026
- **タイトル:** Adobe expands agentic AI ecosystem through partnerships with Accenture, Omnicom, WPP, Microsoft
- **ソース:** Martech360 / Ecommerce News
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-05
- **関連企業:** Adobe, Microsoft, Accenture, Omnicom, WPP
- **要約:** AdobeがエージェントAIエコシステムを拡大。Accenture、Omnicom、Stagwell's Code and Theory、WPP、Microsoftと新たなパートナーシップ。Photoshop、Premiere Pro、Illustrator、Adobe Express、AcrobatにAIエージェントを統合しタスク自動化を推進。Cognizant + ServiceNow AI Agent相互運用性も発表。
- **キーファクト:**
  - パートナー: Accenture, Omnicom, Stagwell, WPP, Microsoft
  - 対象アプリ: Photoshop, Premiere Pro, Illustrator, Adobe Express, Acrobat
  - Cognizant Neuro AI Multi-Agent Accelerator × ServiceNow AI Agents相互運用性
- **引用URL:** https://martech360.com/news/quick-byte/adobe-expands-agentic-ai-ecosystem-through-new-agency-and-technology-partnerships/
- **Evidence ID:** EVD-20260626-0026

---

## KIQ-001-04: マルチモーダルAgent統合の進捗

### INFO-027
- **タイトル:** Alibaba Qwen3.7-Plus for multimodal agent execution — GUI interaction, tool use, coding
- **ソース:** Alibaba Cloud Facebook/Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Alibaba
- **要約:** Alibaba CloudがQwen3.7-Plusを発表。マルチモーダルエージェント実行（GUI操作、ツール使用、コーディング）に最適化。視覚入力からコード生成・実際のタスク実行まで、長時間実行の実世界エージェントタスク向けに設計。
- **キーファクト:**
  - Qwen3.7-Plus: マルチモーダルエージェント実行に最適化
  - GUI操作・ツール使用・コーディング統合
  - 視覚入力→コード生成→実際のタスク実行パイプライン
  - 長時間実行の実世界エージェントタスク向け設計
- **引用URL:** https://www.facebook.com/alibabacloud/posts/1462379839267437/
- **Evidence ID:** EVD-20260626-0027

### INFO-028
- **タイトル:** Google Gemini 1.6 RoboticsER model and Deep Research Agent available
- **ソース:** Google AI / CloudPrice
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** GoogleのGemini 1.6 RoboticsERモデルがロボティクス応用向けに提供開始（$1.00/1M入力、$5.00/1M出力）。Gemini Deep Research Agentが自律的に複数ステップの研究を計画・実行・統合。Managed Agents機能でGoogle側がロボットブレーンを管理。
- **キーファクト:**
  - Gemini 1.6 RoboticsER: ロボティクス応向け、$1.00/1M入力・$5.00/1M出力
  - Deep Research Agent: 自律的マルチステップ研究の計画・実行・統合
  - Managed Agents: サーバーサイド状態管理・バックグラウンド実行
- **引用URL:** https://ai.google.dev/gemini-api/docs/deep-research
- **Evidence ID:** EVD-20260626-0028

### INFO-029
- **タイトル:** Claude Mythos Preview leads SWE-Bench Multimodal leaderboard (0.590)
- **ソース:** LLM Stats / Arena AI / arXiv
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic, Google, OpenAI, Meta, Moonshot
- **要約:** Claude Mythos PreviewがSWE-Bench Multimodalリーダーボードで0.590スコアで首位。2026年のトップマルチモーダルモデル: Gemini 3.5 Flash, GPT-5, Claude 4.5 Sonnet, Moonshot Kimi K2, Meta Llama 4。MMGist包括的マルチモーダルベンチマークが評価項目を69%削減し、クロスモデル識別を78%改善。
- **キーファクト:**
  - Claude Mythos Preview: SWE-Bench Multimodal首位 (0.590)
  - 2026年トップ5マルチモーダル: Gemini 3.5 Flash, GPT-5, Claude 4.5 Sonnet, Kimi K2, Llama 4
  - MMGist: 評価項目69%削減・クロスモデル識別78%改善
- **引用URL:** https://llm-stats.com/benchmarks/swe-bench-multimodal
- **Evidence ID:** EVD-20260626-0029

---

## KIQ-001-05: スキル配布と実行環境の設計・ロックイン

### INFO-030
- **タイトル:** Anthropic Sandbox Runtime open-sourced — OS-level isolation for Claude Code agents
- **ソース:** GitHub / Claude API Docs
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Codeの安全なAIエージェント実行のためのSandbox Runtimeをオープンソースプレビューとして公開。デフォルトでManaged Agentsがクラウドサンドボックス内でツール・コード実行。セルフホストサンドボックスでオーケストレーションをAnthropic側に維持しつつ実行を自社インフラに分離可能。OSレベルのファイルシステム・ネットワーク隔離。
- **キーファクト:**
  - Sandbox Runtime (srt): OSS preview、Claude Code向け安全なエージェント実行
  - Managed Agents: デフォルトでAnthropic管理クラウドサンドボックス
  - セルフホストサンドボックス: 実行を自社インフラに分離可能
  - OSレベル: ファイルシステム・ネットワーク隔離（権限プロンプト以上の実効性）
- **引用URL:** https://github.com/anthropic-experimental/sandbox-runtime
- **Evidence ID:** EVD-20260626-0030

### INFO-031
- **タイトル:** VoltAgent awesome-agent-skills: 1000+ cross-vendor skills compatible with Claude Code, Codex, Gemini CLI, Cursor
- **ソース:** GitHub / Reddit
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03, KIQ-003-05
- **関連企業:** OpenAI, Anthropic, Google (クロスベンダー)
- **要約:** VoltAgentのawesome-agent-skillsコレクションが1000以上のエージェントスキルを収録。Claude Code、Codex、Gemini CLI、Cursor等の主要ツール間で互換性を提供。OpenClaw/ClawHubマーケットプレースはサプライチェーンリスクが指摘される（Palo Alto Unit42）。セキュリティチェック付きverified badge + ワンクリックバンドルインストールが差別化要素。
- **キーファクト:**
  - 1000+クロスベンダースキル: Claude Code, Codex, Gemini CLI, Cursor対応
  - OpenClaw/ClawHub: サプライチェーンリスク指摘（Palo Alto Unit42）
  - セキュリティ: verified badge + ワンクリックインストール
  - クロスベンダー互換性が標準化進行でロックイン回避に寄与
- **引用URL:** https://github.com/VoltAgent/awesome-agent-skills
- **Evidence ID:** EVD-20260626-0031

### INFO-032
- **タイトル:** Gartner: AI agent software spending $206.5B in 2026 (+139% YoY); vendor lock-in dynamics shifting
- **ソース:** Gartner (HamzaAutomates引用) / Computerworld
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05, KIQ-003-04
- **関連企業:** (業界全体)
- **要約:** Gartner予測: AIエージェントソフトウェア支出が2026年に$206.5B（2025年$86.4Bから+139%増）。ベンダーロックインの動態が変化: 無料トークンオファーでロックイン創出、spec-driven developmentでエンジン切替コスト最小化。「AIエンジンの切替がスタックで最もコストが低い」との見方も。スイッチングコストは行動的コスト（ユーザー学習）が最大要因。
- **キーファクト:**
  - AIエージェント支出: $206.5B（2026年・前年比+139%）
  - 2025年: $86.4B
  - 無料トークンオファーでプロプライエタリLLM/エージェントへのロックイン創出
  - Spec-driven development: AIエンジン切替コストが最小
  - 最大スイッチングコスト: 行動的コスト（ユーザー学習・ワークフロー変更）
- **引用URL:** https://hamzaautomates.com/blog/gartner-just-confirmed-what-we-already-knew-ai-agent-spending-is-up-139-in-a-single-year-here-s-how-to-actually-capture-that-growth
- **Evidence ID:** EVD-20260626-0032

---

## KIQ-002-01: 主要クラウドプロバイダーのAI Agent統合状況

### INFO-033
- **タイトル:** AWS Bedrock AgentCore with Web Search; Azure Foundry Agent Service with Hosted Agents
- **ソース:** AWS公式ブログ / Microsoft Learn
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon (AWS), Microsoft (Azure), Google
- **要約:** AWS Bedrock: Web Search on AgentCore追加（エージェントが現在のWeb知識で回答をグラウンディング）。Azure: Foundry Agent Service（プレビュー）でHosted Agents提供、Connected Agentsでエージェント間委任。Azure Agent Skillsキュレーションコレクション公開。9つの主要AIエージェントプラットフォーム2026年比較: Salesforce, Microsoft, Google, Domo, AWS, Kore.ai, Vellum AI等。Nebius AI Cloud 3.6が自然言語でのクラウド管理エージェントを提供。
- **キーファクト:**
  - AWS Bedrock AgentCore: Web Search機能追加（継続更新インデックス）
  - Azure Foundry Agent Service: Hosted Agents・Connected Agents（エージェント間委任）
  - Azure Agent Skills: Azure開発向けキュレーション済みスキルコレクション
  - Microsoft Copilot Studio: Teams/Power Platform内エージェント構築
  - Nebius AI Cloud 3.6: 自然言語クラウド管理エージェント
- **引用URL:** https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore/
- **Evidence ID:** EVD-20260626-0033

---

## KIQ-002-02: エンタープライズ顧客のAI Agent採用率とユースケース

### INFO-034
- **タイトル:** Fortune 500: 68% AI agent adoption in production; Gartner forecasts 15→150,000 agents per F500 by 2028
- **ソース:** FrontierNews AI / LinkedIn / Gartner
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** (業界全体)
- **要約:** Fortune 500企業の68%が本番環境でAIエージェントを採用（2025年23%から急増）。マルチエージェントシステムが初年度40%のROIを達成。Gartner予測: 平均Fortune 500企業のAIエージェント数が2025年の15から2028年に150,000に増加。85%のFortune 500が公式文書でAIに言及。ただしガバナンスは大幅に遅延: 5社中1社のみがガバナンス体制を整備。
- **キーファクト:**
  - Fortune 500 AIエージェント本番採用率: 68%（2025年23%→2026年68%）
  - マルチエージェント初年度ROI: 40%
  - Gartner予測: F500企業のエージェント数 15(2025)→150,000(2028)
  - 85%のF500が公式文書でAI言及（3年前は約30%）
  - ガバナンス: 5社中1社のみが体制整備
  - 41%の組織がエージェントAIを定期使用、監視能力ありは27%のみ
- **引用URL:** https://www.frontiernews.ai/news/article/why-68-of-fortune-500-companies-are-moving-ai-agen-ed3f1d0a
- **Evidence ID:** EVD-20260626-0034

### INFO-035
- **タイトル:** Customer service AI agent adoption 39%→66%; 70% see ROI; KPMG multi-agent orchestration doubled
- **ソース:** ZDNet (Salesforce調査) / CFO Dive (KPMG調査)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** Salesforce, KPMG
- **要約:** Salesforce調査(3,075名): カスタマーサービスAIエージェント採用が2025年39%から2026年66%に成長。70%がROIを達成。KPMG調査: 複数AIエージェントをワークフロー全体でオーケストレーションする組織が9%から18%に倍増。AIコスト課題がエージェント利用の複雑化に伴い増大。
- **キーファクト:**
  - CS AIエージェント採用: 39%(2025)→66%(2026)
  - 70%がROI達成
  - マルチエージェントオーケストレーション組織: 9%→18%（倍増）
  - AIコスト課題がエージェント利用複雑化で増大
- **引用URL:** https://www.zdnet.com/article/agentic-ai-in-customer-service/
- **Evidence ID:** EVD-20260626-0035

---

## KIQ-002-03: 規制環境がエンタープライズAI採用への影響

### INFO-036
- **タイトル:** EU AI Act Article 50 transparency rules effective August 2026; Trump signs AI executive order
- **ソース:** BlackFog / EDUCAUSE / Brookings
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (規制当局)
- **要約:** EU AI Act: Article 50透明性ルールが2026年8月に施行。企業はAIシステム（チャットボット等）との対話をユーザーに開示義務。リスク分類・透明性・非コンプライアンスへの財務罰が規定。2026年末までにエンタープライズアプリの40%がAIエージェント統合予定。米国: トランプ大統領がAIイノベーション・サイバーセキュリティに関する大統領令に署名。州レベルAI規制を削減しイノベーション促進。中国: 首相がAIガバナンスによる「制御喪失」回避を訴え、国際協力推進。
- **キーファクト:**
  - EU AI Act Article 50: 2026年8月施行（AI対話の透明性開示義務）
  - リスク分類・透明性・非コンプライアンス財務罰
  - 2026年末までにエンタープライズアプリ40%がAIエージェント統合予定
  - 米国大統領令: AIイノベーション・サイバーセキュリティ、州規制削減
  - 中国: AIガバナンス国際協力・「中核的社会主義価値」堅持要件
- **引用URL:** https://www.blackfog.com/eu-ai-act-compliance-requirements-2026-and-beyond/
- **Evidence ID:** EVD-20260626-0036

---

## KIQ-002-06: 政府・軍によるAI企業への経済的圧力（Arbiter優先KIQ）

### INFO-037
- **タイトル:** CRITICAL: Government's triple coercion system against Anthropic — SCR designation, DPA threat, export control directive
- **ソース:** Lawfare / DW / ProgrammableMutter / Atlantic Council / Quartz / Fareed Zakaria / The Atlantic
- **公開日:** 2026-02〜06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, OpenAI, xAI, 米国防総省/政府
- **要約:** 米国政府によるAnthropicへの三重強制システムが明確化: (1)供給チェーンリスク(SCR)指定—本来は外国敵対者向けのツールを米国企業に適用、(2)国防生産法(Defense Production Act)でAI提供を強制しようとした試み、(3)Fable 5/Mythos 5輸出管理指令による全面アクセス停止。Anthropicは「完全自律型兵器・国内大量監視」をレッドラインとして拒否し、政府と対立。OpenAIは政府の要請を受け入れた。Anthropicは連邦政府を提訴。Sam AltmanはSCR指定を「極めて恐ろしい前例」と批判。
- **キーファクト:**
  - **SCR指定**: 国防総省がAnthropicを供給チェーンリスク指定（本来は外国敵対者向け）
  - **DPA強制の試み**: 冷戦時代の国防生産法でAI提供強制を試行、Anthropicは提訴
  - **輸出管理指令**: Fable 5/Mythos 5の全面アクセス停止（2026-06-12、INFO-005）
  - **Anthropicレッドライン**: 完全自律型兵器・国内大量監視を拒否
  - **ペンタゴン拒絶**: 「軍は商業AIを自由に使えるべき」と制限を拒否
  - **Sam Altman**: SCR指定を「極めて恐ろしい前例」と批判（OpenAIのペンタゴン契約と同時期）
  - **政府内AI利用**: 150万国防総省職員が軍の生成AIを毎日使用
  - **冷却効果**: 競合ラボが「政府資金のためにAI安全性原則を放棄している」と研究者が非難
  - **ホワイトハウス×Anthropic**: AIセキュリティリスク評価の共同フレームワーク開発中
  - **Fareed Zakaria**: 「政府は市民のAI利用を制限するが、ペンタゴンには何も言わない構造」
- **引用URL:** https://www.lawfaremedia.org/article/voluntary--until-the-government-is-your-customer
- **Evidence ID:** EVD-20260626-0037

### INFO-038
- **タイトル:** OpenAI Pentagon deal announced hours after Anthropic SCR ban; competitive displacement confirmed
- **ソース:** StartupFortune / Quartz / Stocktwits / LinkedIn
- **公開日:** 2026-02〜03
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, Anthropic, xAI
- **要約:** トランプ政権がAnthropicを連邦使用禁止にした数時間後、OpenAIがペンタゴン契約を発表。この順序は「ワシントンがAI勝者を選ぶ」構造を露呈。Anthropicは倫理的懸念でペンタゴン要請を拒否しSCR指定、OpenAIは受諾して契約獲得。xAIはGrok Govで2,000標的の弾薬誘導を実行。2社が同じオファーを受け、反対の回答をした結果。Anthropicの商業的成功($965B評価額)は「調達強制の実効性が限定的」ことを示す（Arbiter H-GOV-001核心矛盾）。
- **キーファクト:**
  - Anthropic SCR指定 → 数時間後 → OpenAIペンタゴン契約発表
  - ペンタゴン要請: 大量監視・完全自律型兵器 → OpenAI受諾・Anthropic拒否
  - xAI Grok Gov: 96時間・2,000標的の弾薬誾導（Operation Epic Fury）
  - NSA: Anthropic Mythos AIを攻撃的サイバー作戦に配備（レッドライン合意あり）
  - Anthropic商業的成功($965B) vs SCR指定: 「調達強制の実効性限界」を示す
  - Polymarket: Anthropicが6月30日までにペンタゴンと取引する確率55%
- **引用URL:** https://startupfortune.com/openais-pentagon-deal-the-morning-after-anthropics-ban-signals-how-washington-now-picks-ai-winners/
- **Evidence ID:** EVD-20260626-0038

### INFO-039
- **タイトル:** Anthropic-Trump truce talks: joint framework for AI security risk assessment after 90-minute shutdown
- **ソース:** CyberCenter.space / Instagram / Fareed Zakaria
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, 米国政府
- **要約:** 政府がAnthropicの最强AIを90分でシャットダウンした事件後、ホワイトハウスとAnthropicがAIセキュリティリスク評価の共同フレームワークを開発中と報道。Anthropicは国防生産法での強制提供を拒否し政権を提訴、その後停戦協議へ。Fareed Zakaria: 「ワシントンとAnthropicの争いは一つの企業についてではなく、誰がフロンティアAIの利用を決定するかについて」。ICRC: 「AIは軍事意思決定を支援できるが、人間の責任を置き換えられない。核指揮統制システムや人間を標的とする自律型兵器システムは禁止されるべき」。
- **キーファクト:**
  - 90分でAnthropic最强AIシャットダウン
  - ホワイトハウス×Anthropic: AIセキュリティリスク共同評価フレームワーク開発中
  - 連邦裁判所: 仮差し止め命令付与後に取り消し
  - 争いの本質: 単一企業の問題ではなく「誰がフロンティアAI利用を決定するか」
  - ICRC立場: 人間を標的とする自律型兵器は禁止対象
- **引用URL:** https://cybercenter.space/2026/06/19/terms-of-engagement-what-the-anthropic-trump-truce-talks-reveal-about-the-future-of-ai-cybersecurity-governance/
- **Evidence ID:** EVD-20260626-0039

---

## KIQ-002-04: AI業務自律化の業界・職種別進捗

### INFO-040
- **タイトル:** AI replacement rollback: Klarna, Duolingo, Starbucks reverse AI headcount cuts; 39% execs made reductions
- **ソース:** MindStudio / HeroHunt.ai / Instagram
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo, Starbucks, McDonalds, IBM
- **要約:** AI代替の「ブーメラン効果」が複数企業で確認。Klarna、Duolingo、Starbucks、McDonaldsがAI人員削減を撤回・縮小。39%の経営者がAI能力を期待して低-中程度の人員削減を実施、21%が大規模削減を実施。Duolingoは契約者作業をAI生成コンテンツに置き換えたが、後にロールバック開始。エントリーレベル職（カスタマーサービス・データ入力・ジュニアアナリスト）のAI代替が加速、McKinseyは作業時間の30%が自動化可能と試算。ただし「エントリーレベルの代替は将来のリーダーを失うこと」の指摘も。
- **キーファクト:**
  - AI代替ロールバック: Klarna、Duolingo、Starbucks、McDonaldsが撤回/縮小
  - 39%の経営者が低-中人員削減、21%が大規模削減（AI能力期待）
  - Duolingo: 契約者→AI生成コンテンツ置換→ロールバック開始
  - McKinsey: 作業時間の30%が自動化可能
  - エントリーレベル職のAI代替加速（将来リーダー育成断絶リスク）
- **引用URL:** https://www.mindstudio.ai/blog/ai-replacement-rollback-starbucks-klarna-mcdonalds
- **Evidence ID:** EVD-20260626-0040

### INFO-041
- **タイトル:** AI agents for advertising automation and SaaS disruption accelerating
- **ソース:** BetterCloud / Reddit / Adobe Enterprise
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-002-05
- **関連企業:** Adobe, BetterCloud
- **要約:** SaaS産業が「人間を支援するツール」から「作業を実行し結果を所有するAIネイティブアプリ・自律エージェント」へシフト中。AIエージェントのタスク完了率目標は85%+（well-defined tasks）。AIエージェントがALEベンチマーク最難関ティアで0%スコア（人間テスト不合格）。広告運用: AIが広告コピー作成・テスト・監視・最適化を自動化。エンタープライズエージェント評価指標の標準化が進む。
- **キーファクト:**
  - SaaS: 人間支援ツール→AIネイティブ自律エージェントへのシフト
  - AIエージェントタスク完了率目標: 85%+（well-defined tasks）
  - ALEベンチマーク最難関ティア: AIエージェント0%（人間テスト不合格）
  - 広告運用AI自動化: コピー作成・テスト・監視・最適化
  - エージェント評価指標: タスク完了率・ツール使用精度・ステップ効率
- **引用URL:** https://www.bettercloud.com/monitor/saas-industry/
- **Evidence ID:** EVD-20260626-0041

---

## KIQ-002-05: プラットフォーマーのAI統合による中間事業者のバリューチェーン侵食

### INFO-042
- **タイトル:** Meta Business Agent: "It's not innovation, it's disintermediation" for advertising agencies
- **ソース:** ConversationEDU / Yahoo Finance / LinkedIn (WPP)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, WPP
- **要約:** MetaがBusiness Agentを発表。広告代理店にとって「これはイノベーションでなく非中介化(disintermediation)。存亡の瞬間」との評価。WPP（年間$64Bの広告支出を管理）はAI検索広告市場が5年で$301M→$100Bに成長すると予測。MetaはすでにAI搭載ツールで広告キャンペーン・顧客対応・運用タスクの自動化を提供。ZuckerbergがQ1決算で「最も大胆なAI約束」を発表。プラットフォーマーの中間事業者への直接のバリューチェーン侵食が加速。
- **キーファクト:**
  - Meta Business Agent: 代理店にとって「非中介化・存亡の瞬間」
  - WPP予測: AI検索広告市場 $301M→$100B（5年・約333倍）
  - WPP広告支出管理額: 年間$64B
  - Meta AI搭載ツール: 広告キャンペーン・顧客対応・運用自動化
  - Zuckerberg Q1決算: 「最も大胆なAI約束」
- **引用URL:** https://www.facebook.com/ConversationEDU/posts/1448307113994349/
- **Evidence ID:** EVD-20260626-0042

---

## KIQ-003-01: API料金改定の頻度・方向性

### INFO-043
- **タイトル:** AI pricing war: GPT-4-level capability from $30/M to <$1/M; Gartner warns AI coding costs will exceed developer salary by 2028
- **ソース:** LLM Stats / Gartner / LinkedIn
- **公開日:** 2026-06-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01, KIQ-004-02
- **関連企業:** OpenAI, DeepSeek, MiniMax
- **要約:** AI API価格の急激な下落: GPT-4レベル能力が2023年初頭$30/M tokensから現在<$1/M tokensに。DeepSeek V4 Flash $0.10/M・MiniMax M3 $0.20/Mで価格競争激化。しかしGartner警告: 2028年までにLLMトークン消費急増でAIコーディングコストが平均開発者給与を超える予測。「トークンあたり安くてもジョブあたり高く」: thinking tokensが総出力コストの80%+を占め、安価なモデルが実際には高コストになるパラドックス。OpenAI Codexはメッセージ単価→APIトークン使用量ベースに移行（2026年4月）。
- **キーファクト:**
  - GPT-4レベル: $30/M(2023) → <$1/M(2026) — 30分の1以下
  - DeepSeek V4 Flash: $0.10/M blended tokens
  - MiniMax M3: $0.20/M
  - Gartner予測: 2028年にAIコーディングコストが開発者給与超過（トークン消費急増）
  - パラドックス: 安価なモデルが「thinking tokens」でジョブあたり高コストに（総出力の80%+）
  - OpenAI Codex: per-message → API token usage pricing移行（2026年4月2日）
- **引用URL:** https://www.gartner.com/en/newsroom/press-releases/2026-06-24-gartner-predicts-ai-coding-costs-will-surpass-average-developer-salary-by-2028-as-token-consumption-surges
- **Evidence ID:** EVD-20260626-0043

---

## KIQ-003-02: 主要ベンチマークの性能推移

### INFO-044
- **タイトル:** BenchPress finding: 84 models × 133 benchmarks is essentially rank-2 — two numbers predict ~90% of scores
- **ソース:** Reddit (machinelearningnews) / arXiv / LLM Stats
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** (学術研究)
- **要約:** 84モデル×133ベンチマークの行列が本質的にrank-2であるとの研究結果。たった2つの数字で全モデルスコアの約90%を予測可能。これは「モデル間の性能差が構造的に小さい」=フロンティア差別化の薄化を示す（SCN-004コモディティ化支持証拠）。5プローブセット{GPQA-D, MMLU-Pro, ARC-AGI-1}でMedAE 3.93ポイントでモデル全体を復元可能。2026年初頭、全フロンティアモデルがMMLUで90%超、GPQA DiamondでGPT-5.4(94.4%)とGemini 3.1 Pro(94.3%)が実質同点。
- **キーファクト:**
  - 84モデル×133ベンチマーク: rank-2構造（2つの数字で~90%予測可能）
  - モデル間性能差の構造的縮小 = コモディティ化支持（SCN-004）
  - MMLU: 全フロンティアモデル90%超（2026年初頭）
  - GPQA Diamond: GPT-5.4 94.4% vs Gemini 3.1 Pro 94.3%（実質同点）
  - ARC-AGI-1: Gemini 3.1 Pro 77.1%, Claude Opus 4.6 68.8%
  - 5プローブセット: GPQA-D, MMLU-Pro, ARC-AGI-1でMedAE 3.93
- **引用URL:** https://www.reddit.com/r/machinelearningnews/comments/1uel4eo/a_new_paper_finds_the_matrix_of_84_models_133_ai/
- **Evidence ID:** EVD-20260626-0044

### INFO-045
- **タイトル:** No single best model: Grok 4/Claude Opus 4.6 lead coding, Gemini 3.1 Pro leads reasoning, GPT-5.4 strong overall
- **ソース:** Arena AI / GuruSup / OpenLM / TeamAI
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** 2026年6月現在、単一の最良モデルは存在しない。コーディング: Grok 4とClaude Opus 4.6が首位。推論: Gemini 3.1 Proが首位。自然な文章: Claudeが首位。総合力: GPT-5.4。Chatbot Arena（600万+ユーザー投票）とAAII v3インデックスが主要ランキング。Microsoft MAI-Image-2.5がText-to-Imageで#2、Image Editingで#3。
- **キーファクト:**
  - コーディング首位: Grok 4, Claude Opus 4.6
  - 推論首位: Gemini 3.1 Pro
  - 自然な文章: Claude首位
  - 総合力: GPT-5.4
  - Chatbot Arena: 600万+ユーザー投票・Eloレーティング
  - AAII v3: 10の難易評価を統合するArtificial Analysis Intelligence Index
- **引用URL:** https://arena.ai/leaderboard/text
- **Evidence ID:** EVD-20260626-0045

---

## KIQ-003-03: OSS vs 商用モデルの性能ギャップ変化

### INFO-046
- **タイトル:** DeepSeek V4-Pro: near-frontier at fraction of price; open-source outperforms Sonnet 4.6 on coding
- **ソース:** LinkedIn / TechJackSolutions / Reddit / Panto AI
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** DeepSeek, Meta, Alibaba, Mistral
- **要約:** オープンソースモデルが商用フロンティアに急速に接近。DeepSeek V4-Proはフロンティアに近いコーディング・長文脈性能を価格の一部で提供。DeepSeek V4: 671Bパラメータ、37B/トークン活性化、14.8Tトークンで学習。OSSモデルがSonnet 4.6をコーディングタスクで上回る事例も。「トップでのギャップが非常に小さくなっている」。ただし「クリーンなノックアウトではない」: 安価だが一部でフロンティアに後れ。Meta: 2026年4月にLlamaを「Muse Spark」に置換（Meta Superintelligence Labs）。Qwen 3.6 27Bがコンシューマハードウェアで総合首位。
- **キーファクト:**
  - DeepSeek V4-Pro: フロンティアに近い性能・価格の一部
  - DeepSeek V4: 671B params・37B active・14.8T tokens training
  - OSSがSonnet 4.6をコーディングで上回る（ギャップ縮小確認）
  - 「DeepSeekは安いが完全な勝利ではない」（一部でフロンティアに後れ）
  - Meta: Llama 4(2025/4) → Muse Spark(2026/4) に置換（Meta Superintelligence Labs）
  - Qwen 3.6 27B: コンシューマハードウェアで総合首位
- **引用URL:** https://techjacksolutions.com/ai-tools/deepseek/deepseek-v4-vs-frontier-models/
- **Evidence ID:** EVD-20260626-0046

---

## KIQ-003-04: 資金調達・投資動向

### INFO-047
- **タイトル:** SpaceX acquires Cursor/Anysphere for $60B; Qualcomm acquires Modular for $4B; big tech $725B AI capex
- **ソース:** Facebook / Beamstart / PwC / Metaintro / Yahoo Finance
- **公開日:** 2026-06-24
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** SpaceX (xAI), Qualcomm, Anysphere (Cursor), Modular, Alphabet, Amazon, Meta, Microsoft, OpenAI, Anthropic
- **要約:** 大規模AI M&Aとインフラ投資が加速。SpaceXがAIコーディングスタートアップCursor（Anysphere親会社）を$60Bで完全買収（6月16日確定、4月のオプション契約から）。QualcommがAIソフトウェアスタートアップModularを$4Bで買収（6月24日発表）。Alphabet, Amazon, Meta, Microsoftが2026年にAIインフラで$700B+支出予定。ビッグテック全体の資本支出は$725B（史上最大の企業支出ラッシュの一つ）。Anthropicは豪州・日本でAIデータセンターロール採用中。グローバルAIデータセンター支出: 2025年>$300B(+60% YoY)。
- **キーファクト:**
  - SpaceX → Cursor/Anysphere買収: $60B（2026年6月16日確定）
  - Qualcomm → Modular買収: $4B（2026年6月24日、ストック取引）
  - Alphabet/Amazon/Meta/Microsoft: AIインフラ$700B+支出予定（2026年）
  - ビッグテック全体資本支出: $725B（2026年）
  - Anthropic: 豪州・日本でデータセンター拡張採用中
  - グローバルAIデータセンター支出: >$300B(2025)、$27.5B追加(2026)
- **引用URL:** https://beamstart.com/news/cursor-deal-puts-us-on-17823852553131
- **Evidence ID:** EVD-20260626-0047

---

## KIQ-003-05: エコシステム離脱コスト（スイッチングコスト）

### INFO-048
- **タイトル:** "AI dependency is the new Microsoft lock-in, but worse" — vendor lock-in deepens
- **ソース:** jeromeroussin.com / MLflow / LinkedIn / IntuitionLabs
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** OpenAI, Anthropic, Google, Mistral
- **要約:** AI依存は「新しいMicrosoftロックイン、しかしより悪い」との分析。OpenAIの関数呼び出しはAnthropicと異なり、Googleの構造化出力はMistralと異なる制約を持つ。モデル切替でシステムが破損する実リスク。マルチベンダー戦略はポートフォリオ管理として機能（タスクタイプ・レイテンシ・リスク階層でプロバイダー選択）。「ベンダーのAI戦略を自社の戦略にするな」の警告。88%の企業がAI使用するが39%のみがビジネスインパクト、70-85%のAIプロジェクトが失敗。
- **キーファクト:**
  - ベンダー間API非互換性: function calling/structured outputが異なり切替で破損
  - 「AI依存は新しいMicrosoftロックイン、より悪い」
  - マルチベンダー戦略: タスク/レイテンシ/リスクでプロバイダー選択
  - 88%がAI使用・39%のみがビジネスインパクト
  - AIプロジェクト失敗率: 70-85%
- **引用URL:** https://jeromeroussin.com/en/articles/lock-in-ia.html
- **Evidence ID:** EVD-20260626-0048

---

## KIQ-004-02: コーディング能力の市場価値変化

### INFO-049
- **タイトル:** Junior developer demand down 20%; "coding will become a useless commodity"; 84% use AI but only 29% trust it
- **ソース:** Medium / Business Insider / Stack Overflow survey / Stanford Digital Economy Lab
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02, KIQ-004-01
- **関連企業:** AWS (Garman発言), GitHub, Cursor, Anthropic
- **要約:** ジュニア開発者需要が約20%減少。AWS CEOのGarmanが「破滅的」と警告。Stanford Digital Economy Lab: ソフトウェア開発者(22歳以上)の雇用が約20%減少。ジュニアテック求人が2023-2024で67%急減。60%の「エントリーレベル」がミッドレベル経験を要求。84%の開発者がAIツール使用するが信頼するのは29%のみ(2024年40%から低下)。「コーディングは無価値なコモディティになる近い将来」。AI時代の最も価値あるスキルは「コーディングでなく、どの問題を解くべきかを知ること」。CursorがContinue(オープンソース)を買収し$60B評価でSpaceXに買収。
- **キーファクト:**
  - ジュニア開発者需要: ~20%減少（AWS CEO「破滅的」）
  - Stanford: ソフトウェア開発者雇用~20%減（22歳+）
  - ジュニアテック求人: 67%急減（2023-2024）
  - 84%がAIツール使用・29%のみ信頼（2024年40%から低下）
  - 「コーディングは無価値なコモディティになる」
  - AI時代の価値あるスキル: 問題定義・AI出力検証・倫理
  - AIキャリアの~50%が非エンジニアリング職
- **引用URL:** https://medium.com/predict/the-industry-is-quietly-eliminating-its-own-future-the-data-proves-it-235d5cdd3e18
- **Evidence ID:** EVD-20260626-0049

---

## KIQ-004-03: AI代替困難な能力の価値上昇と新職種シグナル

### INFO-050
- **タイトル:** WEF: AI reshaping entry-level work; new AI roles emerging; Anthropic hiring Creative Director at $400K-570K
- **ソース:** WEF / Facebook / MediaBistro / TESS Group
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** Anthropic, WEF
- **要約:** WEFが「AI and the Future of Entry-Level Work」レポート発表。AIがエントリーレベル採用・育成・昇進を最も可視的に変革。新興AI職種: AI Automation Consultant, AI Content Operator, Cybersecurity専門家等。AnthropicがExecutive Creative Directorを$400K-570Kで採用中—AI概念をビジネス目標に翻訳するクリエイティブ戦略。「2030年に存在する仕事の85%はまだ発明されていない」。AI防止困難な基準: 感情的知性・批判的思考・人間相互作用・創造性。「AIは仕事より速く新しい仕事を創造している」。
- **キーファクト:**
  - WEF: AIがエントリーレベル仕事を最も可視的に変革
  - 2030年の仕事の85%は未発明
  - 新興職種: AI Automation Consultant, AI Content Operator, Cybersecurity
  - Anthropic Creative Director: $400K-570K（AI概念のクリエイティブ翻訳）
  - AI防止困難基準: 感情的知性・批判的思考・人間相互作用・創造性
  - 「AIは仕事より速く新しい仕事を創造」
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-is-transforming-entry-level-work-how-can-companies-redesign-jobs-to-keep-opportunity-alive/
- **Evidence ID:** EVD-20260626-0050

---

## KIQ-004-04: AI時代に勝つ企業の条件

### INFO-051
- **タイトル:** HBR: 5 types of AI investment; Walmart equips 1.5M associates, reskills 50,000; 80% workforce needs AI reskilling by 2027
- **ソース:** HBR / Disco.co / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** Walmart, (業界全体)
- **要約:** HBRが「5 types of AI investment」を発表。Walmartが1.5M店舗従業員にAIツール(Element platform)を提供、同時に50,000フロントライン従業員をリスキリング。AI導入成功企業は内部プロセスを再構築。AI能力を証明した組織がより大きな契約・強い価格決定力・長期顧客コミットメントを獲得。2027年までに労働力の80%がAIリスキリング必要。リスキリングは「コストでなく投資」との認識。
- **キーファクト:**
  - Walmart: 1.5M従業員にAIツール提供・50,000人リスキリング
  - AI導入成功企業: 内部プロセス再構築が鍵
  - AI能力証明組織: 大規模契約・価格決定力・長期コミットメント獲得
  - 80%の労働力が2027年までにAIリスキリング必要
  - リスキリングは投資（非コスト）
- **引用URL:** https://hbr.org/2026/06/the-5-types-of-ai-investment-and-how-to-capture-their-value
- **Evidence ID:** EVD-20260626-0051

---

## KIQ-005-01: AGI到達度ベンチマークと能力進展

### INFO-052
- **タイトル:** DeepMind CEO: AGI ~2030; "The AI Scientist" published in Nature; ARC-AGI-2 led by Seed 2.1 Pro (0.625)
- **ソース:** ZME Science / Nature / Instagram / LLM Stats / Reddit
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Google / DeepMind, ByteDance
- **要約:** DeepMind CEO Demis HassabisがAGIは2030年頃に到来可能と予測。「The AI Scientist」がNatureに発表—研究ライフサイクルの自動化。ARC-AGI-2リーダーボード: ByteDance Seed 2.1 Proが0.625で首位。3BパラメータモデルがARC-AGI-1で44.6%達成（671Bモデルの15.8%を圧倒）—効率性のブレークスルー。Anthropic: 「ベンチマーク供給がボトルネック。IQの普遍的メトリックが存在しない」。Recursive self-improvementは「まだ起きておらず、必然でもない」が技術が社会の管理能力より速く進む可能性。
- **キーファクト:**
  - Hassabis: AGI ~2030年予測
  - "The AI Scientist": Nature発表、研究ライフサイクル自動化
  - ARC-AGI-2首位: Seed 2.1 Pro (0.625)
  - 効率ブレークスルー: 3B params → ARC-AGI-1 44.6%（vs 671Bの15.8%）
  - Anthropic: 「ベンチマーク供給がボトルネック・IQ普遍メトリック不在」
  - RSI: 「まだ起きていない・必然でない」が技術 > 社会管理のリスク
- **引用URL:** https://www.zmescience.com/future/deepmind-ceo-agi-2030/
- **Evidence ID:** EVD-20260626-0052

---

## KIQ-005-03: AGI安全性とガバナンスの政策議論

### INFO-053
- **タイトル:** Science.org: Researchers "caught in the crossfire" after Fable 5 takedown; AOC introduces AI Data Center Moratorium Act
- **ソース:** Science.org / POLITICO / Instagram / Fareed Zakaria / Virginia Law Review
- **公開日:** 2026-06-19
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-06
- **関連企業:** Anthropic, 米国政府/議会
- **要約:** Science.org: Fable 5撤去後、科学者が「交差砲火」に巻き込まれ、AI安全ルールがオープン研究を変革する恐れ。AOCがAIデータセンター・モラトリアム法を下院に提出（環境・経済・安全問題解決まで禁止）。Ted Cruzが来月AI立法マークアップを計画。「Managing extreme AI risks amid rapid progress」論文: より能力の高いモデルにより厳しい要件を課す段階的安全フレームワーク推奨。「AI Rights for Human Safety」(Virginia Law Review): AI権利が人間安全を促進する可能性。連邦政府が州のAI規制権を奪う脅威。
- **キーファクト:**
  - Fable 5撤去: 科学界の「交差砲火」・オープン研究変革の恐れ
  - AOC AIデータセンター・モラトリアム法: 環境/経済/安全法制定まで禁止
  - Ted Cruz: 来月AI立法マークアップ計画
  - 段階的安全フレームワーク: より能力あるモデルに厳しい要件
  - AI Rights for Human Safety: AI権利で人間安全促進の可能性
  - 連邦vs州: 連邦政府が州AI規制権を奪う脅威
- **引用URL:** https://www.science.org/content/article/researchers-caught-crossfire-companies-and-government-grapple-over-ai-safety
- **Evidence ID:** EVD-20260626-0053

---

## BYTEDANCE-CHINESE: ByteDance/Doubao/Seed中国語一次情報

### INFO-054
- **タイトル:** Doubao reaches 345M MAU (Q1 2026), surpassing Qwen + DeepSeek combined; ByteDance launches paid subscriptions
- **ソース:** Pandaily / The Star / QuestMobile / People's Daily / Economic Times
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance, Alibaba (Qwen), DeepSeek
- **要約:** ByteDanceのDoubaoがQ1 2026で345M MAUに到達。Alibaba Qwen(166M)とDeepSeekの合計MAUを超える規模。中国最大のAIチャットボット。2023年ローンチ以来300M+ MAU。ByteDanceがDoubao Pro有料サブスクリプション（最大500元）を開始。Doubao ProはSeed 2.1 Proモデルとエージェント機能（コンピュータ操作・Web使用・タスク自律実行）を提供。DeepSeekは無料を維持する中、初の大手国内AIチャットボットの有料化。
- **キーファクト:**
  - Doubao MAU: 345M（Q1 2026・QuestMobile）
  - Qwen MAU: 166M・DeepSeekも下回る（Doubaoが合計を超える）
  - Doubao Pro: 有料サブスク最大500元・Seed 2.1 Proモデル
  - エージェント機能: コンピュータ操作・Web使用・自律タスク実行
  - 中国初の大手AIチャットボット有料化（DeepSeekは無料維持）
- **引用URL:** https://x.com/thePandaily/article/2069979224564281351
- **Evidence ID:** EVD-20260626-0054

### INFO-055
- **タイトル:** Seedance 2.5 breaks 30-second barrier for AI video; Seed 2.1 leads ARC-AGI-2; Seed3D 2.0 and Protenix-v1 released
- **ソース:** ByteDance Seed公式 / CNET / The Decoder / Instagram
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-005-01, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDance Seedファミリーの包括的アップデート: (1)Seedance 2.5: AI動画生成で30秒の壁を突破（継ぎ目なし、シーン変更・テンポ変化付き）。最大50のマルチモーダル参照（画像/音声/動画/3D）。「ハリウッド水準」。(2)Seed 2.1: Pro/Turbo版、汎用エージェント能力大幅強化。Seed-2.1-Pro-PreviewがARC-AGI-2リーダーボード首位(0.625)。(3)Seed3D 2.0: 高忠実度3Dコンテンツ生成。(4)Protenix-v1: 高精度オープンソースタンパク質構造予測。
- **キーファクト:**
  - Seedance 2.5: 30秒バリア突破・50マルチモーダル参照・継ぎ目なし
  - Seed 2.1 Pro: ARC-AGI-2首位(0.625)・汎用エージェント能力大幅強化
  - Seed3D 2.0: 高忠実度シミュレーション対応3D生成（2026年4月22日）
  - Protenix-v1: オープンソースタンパク質構造予測（2026年2月6日）
  - ByteDance Seed研究ブログで公開
- **引用URL:** https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity
- **Evidence ID:** EVD-20260626-0055
