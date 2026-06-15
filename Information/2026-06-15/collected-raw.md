# 収集データ: 2026-06-15

## メタデータ
- 収集日時: 2026-06-15 00:18 UTC ～ 00:52 UTC
- 品質フラグ: COMPLETE
- INFO件数: 59
- Evidence ID範囲: EVD-20260615-0001 ～ EVD-20260615-0059
- 実行検索クエリ数: 約62（collection_plan.json 56 + 動的4 + ギャップ補完2）
- 詳細スクレイプ数: 13
- 動的追加クエリ: KIQ-ANT-SAFETY, KIQ-GOO-001, INFO-002-CONFIRM, H-BTD-002-QUALITY
- KIQカバレッジ: 24/24（全KIQ網羅）
  - KIQ-001-01 ✅ KIQ-001-02 ✅ KIQ-001-03 ✅ KIQ-001-04 ✅ KIQ-001-05 ✅
  - KIQ-002-01 ✅ KIQ-002-02 ✅ KIQ-002-03 ✅ KIQ-002-04 ✅ KIQ-002-05 ✅ KIQ-002-06 ✅
  - KIQ-003-01 ✅ KIQ-003-02 ✅ KIQ-003-03 ✅ KIQ-003-04 ✅ KIQ-003-05 ✅
  - KIQ-004-01 ✅ KIQ-004-02 ✅ KIQ-004-03 ✅ KIQ-004-04 ✅
  - KIQ-005-01 ✅ KIQ-005-02 ✅ KIQ-005-03 ✅
  - BYTEDANCE-CHINESE ✅
- 企業別エントリ数:
  - Anthropic: 12（INFO-001, 002, 003, 009, 010, 020, 027, 028, 043, 046, 047, 053, 054, 057）
  - OpenAI: 8（INFO-004, 005, 007, 008, 043, 044, 051, 053）
  - Google: 6（INFO-006, 014, 024, 042, 044, 053）
  - xAI: 3（INFO-011, 024, 043）
  - ByteDance: 5（INFO-012, 029, 030, 029, H-BTD-002-QUALITY）
- PIR別エントリ数:
  - PIR-2026-001（プロダクト革新）: 20+
  - PIR-2026-002（市場動向）: 20+
  - PIR-2026-003（競争環境）: 15+
  - PIR-2026-004（社会・雇用影響）: 10+
  - PIR-2026-005（安全・治理）: 15+
- 主要ストーリー: Anthropic Fable 5/Mythos 5発表→米政府アクセス停止（KIQ-002-06）、Pentagon-Anthropic対立（$200M契約取消・サプライチェーンリスク指定）、大統領令・GAAIA（連邦AI政策枠組み）、中国$295B AI投資計画、ByteDance AI製薬分離・支出増額、KPMG 276K Agent 365展開

## 収集結果

### INFO-001
- **タイトル:** Claude Fable 5 and Claude Mythos 5
- **ソース:** Anthropic（公式ブログ）
- **公開日:** 2026-06-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-04, KIQ-005-01, KIQ-002-06
- **関連企業:** Anthropic
- **要約:** AnthropicがMythos-classモデルであるClaude Fable 5（一般向け・セーフガード付き）とClaude Mythos 5（政府・信頼パートナー向け・セーフガード解除）を同時発表。Fable 5はほぼ全ベンチマークでSOTA達成。ソフトウェアエンジニアリング、知識作業、視覚、科学研究で驚異的パフォーマンス。価格は$10/M入力・$50/M出力トークン（Mythos Previewの半額以下）。
- **キーファクト:**
  - Stripe: Fable 5が数ヶ月分のエンジニアリングを数日に圧縮、5000万行Rubyコードベースの移行を1日で完遂（手作業なら2ヶ月以上）
  - Cognition FrontierCode評価で最高スコア（frontier models中）
  - 新しいセーフガード: セキュリティ/生物化学/蒸留の分類器が不適切要求を検出時、Opus 4.8にフォールバック（平均5%未満のセッションでトリガー）
  - Mythos 5: 薬物設計プロセスを約10倍加速、タンパク質設計タスクで人間専門家に匹敵
  - 新分子生物学仮説: 科学者がMythosの仮説を約80%の頻度で選好（Opus級との盲検比較）
  - 30日間データ保持ポリシーを全Mythos-classモデルに要求
  - Fable 5: 6月23日以降はsubscription planから除外、usage creditsが必要
- **引用URL:** https://www.anthropic.com/news/claude-fable-5-mythos-5
- **Evidence ID:** EVD-20260615-0001

### INFO-002
- **タイトル:** Statement on the US government directive to suspend access to Fable 5 and Mythos 5
- **ソース:** Anthropic（公式ブログ）
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06, KIQ-005-03, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** 米国政府が国家安全保障権限に基づき、Fable 5/Mythos 5への「全外国人（米国内外問わず、外国人Anthropic従業員含む）」のアクセス停止を命じる輸出管理指令を発出。実質的に全顧客へのアクセスを停止。政府はFable 5の脱獄（jailbreak）手法を特定したと主張するが、Anthropicはこれを狭い非普遍的脱獄に過ぎず、他の公開モデル（GPT-5.5含む）でも可能なレベルと反論。
- **キーファクト:**
  - 指令は6月12日午後5:21(ET)に受領、国家安全保障上の懸念を理由とするが具体的内容の開示なし
  - 政府の主張する脱獄手法: コードベースを読ませてソフトウェア欠陥を修正させる方法（非普遍的・狭い範囲）
  - Anthropic反論: この技術レベルはGPT-5.5等の公開モデルでも広く利用可能
  - Anthropicの防御戦略: 防御の深層化（defense in depth）—脱獄を狭くするか高コストにし、監視で検出
  - 外部バグバウンティ: 1000時間以上のテストで普遍的脱獄は未発見（UK AISIが初期テストで進展あり）
  - 他の全Anthropicモデルへのアクセスは影響なし
- **引用URL:** https://www.anthropic.com/news/fable-mythos-access
- **Evidence ID:** EVD-20260615-0002

### INFO-003
- **タイトル:** Results from the first Anthropic Public Record
- **ソース:** Anthropic（公式ブログ）
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-004-03, KIQ-002-06, KIQ-ANT-SAFETY
- **関連企業:** Anthropic
- **要約:** Anthropicが約52,000人の米国人を対象とした全国調査（Anthropic Public Record、2025年11-12月実施）の結果を発表。AI最大の希望は「疾病治癒」(48%)、最大の恐怖は「雇用喪失」(64%)。71%が政府のAI規制関与を支持（超党派的）。AI企業への信頼度はわずか15%で、連邦政府(20%)より低い。81,000人のClaudeユーザー定性調査との関連も言及。
- **キーファクト:**
  - 雇用喪失懸念: 64%（全州でトップ、党派横断的: 民主党67%・共和党62%）
  - 認知依存(Cognitive dependency)懸念: 56%
  - 政府規制支持: 71%（民主党79%・共和党68%・無所属69%）—超党派的超多数
  - AI企業への信頼: わずか15%（全機関中最低、連邦政府20%・独立専門家43%）
  - 「企業の法的責任」(47%)と「成長より安全」(44%)がAIガバナンスでトップ回答
  - 統合ユーザー（毎日仕事と個人でAI使用）は約6%、若い・男性・都市部・大卒に偏る
  - 81,000人Claudeユーザー定性研究（Anthropic Interviewer）との関連: 教育者が認知萎縮を目撃する可能性は平均の2.5-3倍
- **引用URL:** https://www.anthropic.com/news/anthropic-public-record
- **Evidence ID:** EVD-20260615-0003

### INFO-004
- **タイトル:** Access OpenAI models and Codex through your Oracle cloud commitment
- **ソース:** OpenAI（公式ブログ）
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02, KIQ-001-03, KIQ-002-01
- **関連企業:** OpenAI, Oracle
- **要約:** OpenAIとOracleが提携し、Oracle Cloud Infrastructure(OCI)ユーザーが既存のOracle契約・コミットメントを使ってOpenAIのフロンティアモデルとCodexにアクセス可能に。Oracle顧客はUniversal CreditsをOpenAIモデルに適用可能。数週間以内に提供開始予定。エンタープライズのAI導入における調達プロセスとガバナンスの摩擦低減が目的。
- **キーファクト:**
  - OCIユーザーがOracle Universal CreditsでOpenAIモデル/Codexにアクセス可能
  - 既存の調達ワークフローとクラウドコミットメント内での利用が可能
  - エンタープライズのガバナンス要件に合致する新しい導入経路
  - OpenAIのクラウドパートナー拡張戦略の一環（Azure、Google Cloudに続きOracle）
- **引用URL:** https://openai.com/index/openai-on-oracle-cloud/
- **Evidence ID:** EVD-20260615-0004

### INFO-005
- **タイトル:** Confidential submission of draft S-1 to the SEC
- **ソース:** OpenAI（公式ブログ）
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがSECに機密S-1登録届出書を提出したと発表。IPO準備の公式ステップ。同時に「全ての人に利益をもたらす計画」を発表し、AGIの利益分配ビジョンを示した。
- **キーファクト:**
  - SECへの機密S-1提出（IPOプロセス開始の公式合図）
  - 同時に経済研究交流フォーラム発表
  - IPOのタイミング・価格は未定（市場条件等による）
- **引用URL:** https://openai.com/index/openai-submits-confidential-s-1/
- **Evidence ID:** EVD-20260615-0005

### INFO-006
- **タイトル:** 9 demos of Gemini Omni and Gemini 3.5 in action
- **ソース:** Google（公式ブログ）
- **公開日:** 2026-05-29
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-002-01, KIQ-005-01
- **関連企業:** Google / DeepMind
- **要約:** Google I/O 2026で発表されたGemini Omni（任意の入力から高品質動画生成・会話で動画編集）とGemini 3.5 Flash（エージェント・コーディング向け、長期間タスクでfrontier性能）の9つのデモ。Gemini 3.5 FlashはGeminiアプリとSearch AI Modeのデフォルトモデルに。Antigravityハーネスと組み合わせて協調サブエージェント展開が可能。
- **キーファクト:**
  - Gemini Omni: 動画生成と会話型編集（キャラクター一貫性・物理維持・マルチターン編集）
  - Gemini 3.5 Flash: フロンティア級性能とFlash級速度のバランス、長期間エージェントタスク向け
  - Antigravityハーネス: 3.5 Flashの協調サブエージェント展を可能にする
  - Gemini Spark: 個人AIエージェント（24/7稼働）、Google AI Ultra向けに米国で提供開始
  - Search統合: 情報エージェント、生成UI、フィットネストラッカー等のカスタム体験
  - 3.5 Flash: Gemini API、Google AI Studio、Android Studio、Gemini Enterprise Agent Platformで利用可能
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-3-5-videos/
- **Evidence ID:** EVD-20260615-0006

### INFO-007
- **タイトル:** New OpenAI Academy courses for the next era of work
- **ソース:** OpenAI（公式ブログ）
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** OpenAI
- **要約:** OpenAIが「OpenAI Academy」の新しいコースを発表。次世代の仕事に向けたAIスキル向上を目的とする教育プログラム。AI導入を実践的な仕事術に焦点。
- **キーファクト:**
  - 職場でのAI適用に焦点を当てた新コース群
  - AIスキル教育のエコシステム拡大戦略の一環
- **引用URL:** https://openai.com/index/academy-courses-applying-ai-at-work/
- **Evidence ID:** EVD-20260615-0007

### INFO-008
- **タイトル:** OpenAI to acquire Ona
- **ソース:** OpenAI（公式ブログ）
- **公開日:** 2026-06-11
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがOnaの買収を発表。買収金額・詳細は未開示。人材・技術の獲得が目的と推測される。
- **キーファクト:**
  - Ona買収の発表（詳細未開示）
  - M&A戦略の一環としての人材獲得
- **引用URL:** https://openai.com/index/openai-to-acquire-ona/
- **Evidence ID:** EVD-20260615-0008

### INFO-009
- **タイトル:** Anthropic disables Fable and Mythos AI models after U.S. government bars it from giving foreigners access
- **ソース:** Fortune
- **公開日:** 2026-06-13
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-005-03, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** FortuneによるFable 5/Mythos 5アクセス停止事件の詳細報道。Anthropicは機密IPO提出済み、評価額$965B。政府の輸出管理決定はIPO投資家を冷え込ませる可能性。Dean Ballは「lawfareまたは極端な安全保障タカ派」と評。Trump政権は2月に連邦機関のAnthropic利用停止を命じ、3月に「サプライチェーンリスク」指定。Amazonからの警告がWhite HouseのMythos停止を導いたとの別報道あり。
- **キーファクト:**
  - Anthropic IPO評価額: $965B（6月初に機密提出）
  - 指令は米国内外の全外国人を含む（Anthropicの非市民従業員も含む）
  - 政府の根拠: 狭い非普遍的jailbreak技術（コードベースを読ませて欠陥修正）
  - Dean Ball（元Trump政権AI政策顧問）: 「lawfareか極端な安保タカ派か不明だが漫画的」
  - Peter Girnus（セキュリティ研究者）: 「弾薬と呼べば政府は文字通り受け取る。法的根拠を自分で書いた」
  - Gary Marcus: 中国系研究者の中国帰還を促し、米国AI企業への投資意欲を損なうと懸念
  - 別記事で「Amazonからの警告がWhite Houseの停止を導いた」との報道（別URL）
  - カナダのCarney首相: 米国規制は「米国プロバイダーへの過度な依存の危険性」を示すと警告
- **引用URL:** https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/
- **Evidence ID:** EVD-20260615-0009

### INFO-010
- **タイトル:** Anthropic Agent SDK credit pricing change June 15, 2026
- **ソース:** Prove AI / Reddit / GitHub
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Anthropicが2026年6月15日からClaude Agent SDKの課金モデルを変更。プログラマティック/非対話型使用を通常サブスクリプション制限から分離し、Agent SDK使用には専用クレジットが必要に。コミュニティで混乱が発生中。Claude Agent SDKはプロプライエタリライセンスでリリース済み。Fable 5は6月23日以降サブスクリプションプランからも除外。
- **キーファクト:**
  - Agent SDK課金分離: 6月15日からプログラマティック使用を別課金
  - Claude Agent SDK Python: GitHub changelog活発に更新中
  - Claude Agent SDK vs LangGraph比較で本番環境対応が確認
  - 開発者コミュニティで課金変更への混乱が広がる
- **引用URL:** https://proveai.com/blog/anthropics-agent-sdk-credit-june-15
- **Evidence ID:** EVD-20260615-0010

### INFO-011
- **タイトル:** xAI Grok Build 0.1 API - coding agent on xAI API
- **ソース:** xAI（公式サイト）
- **公開日:** 2026-06-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIがGrok Build 0.1（最速のコーディングモデル）をAPIで公開ベータ提供。コーディングエージェントとして実行可能。Grok 4.1 FastはEnterprise APIで利用可能、エージェントツールが適応。Files APIがGA。
- **キーファクト:**
  - Grok Build 0.1: xAI最速コーディングモデル、API公開ベータ
  - Grok 4.1 Fast: Enterprise API利用可能、エージェントツール適応・ツール価格引き下げ
  - xAI GrokモデルがGoogle Gemini Enterprise Agent Platformでも利用可能に
- **引用URL:** https://x.ai/news
- **Evidence ID:** EVD-20260615-0011

### INFO-012
- **タイトル:** Coze 2.5 - ByteDance agent platform 'Agent World' ecosystem
- **ソース:** KuCoin / Kr-Asia
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05
- **関連企業:** ByteDance
- **要約:** ByteDanceのCozeがv2.5をリリースし、「Agent World」エコシステムを導入。AIエージェントがチャットインターフェースを超えて、独立実行環境・スキル・アイデンティティを持つ。ByteDanceは2026年の4つのAI優先分野を設定。WeChatもAIエージェントプロトコルを発表し14億ユーザーへのパーソナルAI秘書提供を計画。
- **キーファクト:**
  - Coze 2.5: Agent Worldエコシステム導入、チャットUIを超えたエージェント実行
  - 独立実行環境・スキル・アイデンティティをエージェントに付与
  - ByteDance 2026年4つのAI優先分野を設定
  - WeChat: AIエージェントプロトコル発表、14億ユーザー向けパーソナルAI秘書
- **引用URL:** https://www.kucoin.com/news/flash/bytedance-s-coze-launches-version-2-5-introduces-agent-world-ecosystem
- **Evidence ID:** EVD-20260615-0012

### INFO-013
- **タイトル:** AI Agent Security: 72% piloting, only 31% production-secure
- **ソース:** Improvado / VentureBeat
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02, KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** 2026年のエンタープライズAIエージェントセキュリティ状況: 72%の企業がエージェントのパイロット/デプロイを実施するが、強固なセキュリティ管理の本番環境で実行しているのは31%のみ。エージェント失敗の根本原因は「モデルの推論能力」ではなく「ランタイム環境」の問題。Enterprise MCPコントロールプレーンの構築が課題。
- **キーファクト:**
  - エンタープライズの72%がエージェントをパイロット/デプロイ中
  - 堅牢なガバナンス環境で稼働はわずか31%
  - エージェント失敗の根本: モデル問題ではなくランタイム問題
  - Enterprise MCPコントロールプレーンでアクセス権限管理が課題
- **引用URL:** https://improvado.io/blog/ai-agent-security
- **Evidence ID:** EVD-20260615-0013

### INFO-014
- **タイトル:** Google Gemini Interactions API & Managed Agents on Agent Platform
- **ソース:** Google AI for Developers / Devoteam
- **公開日:** 2026-06-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01, KIQ-001-03
- **関連企業:** Google / DeepMind
- **要約:** GoogleがGemini APIの新しいInteractions API（サーバーサイド履歴・バックグラウンド処理・エージェントワークフロー対応）を発表。Managed Agents API on Agent Platformで開発者がGoogleホストの安全な環境でカスタムエージェントを構築・実行可能。Gemini EnterpriseでGoogle Groupsを通じたエージェント共有が可能に。
- **キーファクト:**
  - Interactions API: サーバーサイド履歴・バックグラウンド処理・エージェントワークフロー対応
  - Managed Agents API: Googleホスト環境でのカスタムエージェント構築・実行
  - Gemini Enterprise: Google Groups経由でのエージェント共有
  - Google I/O 2026で発表された企業AI向け7つの重要ポイント
- **引用URL:** https://ai.google.dev/gemini-api/docs/interactions/interactions-overview
- **Evidence ID:** EVD-20260615-0014

### INFO-015
- **タイトル:** Mastercard launches Agent Pay for Machines
- **ソース:** Mastercard（公式プレスリリース）
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05, KIQ-002-04
- **関連企業:** Mastercard
- **要約:** Mastercardが「Agent Pay for Machines」を発表。ビジネスがカード・口座・ステーブルコイン全体で安全かつ継続的なマシン決済をサポートするフレームワーク。認証されたAIエージェントが消費者の代わりに取引を実行する「Agentic Tokens」を活用。AIエージェントコマースプロトコルの基盤となる。
- **キーファクト:**
  - Agent Pay: カード・口座・ステーブルコインでのマシン決済サポート
  - Agentic Tokens: 認証AIエージェントによる代理取引
  - agentic commerceインフラの標準化
- **引用URL:** https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
- **Evidence ID:** EVD-20260615-0015

### INFO-016
- **タイトル:** White House Executive Order on Advanced AI Innovation and Security (June 2, 2026)
- **ソース:** Global Policy Watch / JD Supra
- **公開日:** 2026-06-13
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06, KIQ-005-03
- **関連企業:** （米国政府）
- **要約:** Trump政権が2026年6月2日に「Promoting Advanced Artificial Intelligence Innovation and Security」と題する大統領令を署名。AI対応サイバーセキュリティの包括的枠組みを導入し、トップAIモデルの国家安全保障リスクに関する任意の連邦審査を導入。Commerce Secretaryは90日以内に州AI法の見直し権限を持つ。
- **キーファクト:**
  - 発効日: 2026年6月2日
  - 任意の連邦ベッティング（voluntary federal vetting）: トップAIモデルの国安リスク審査
  - Commerce Secretary: 90日以内に州AI法見直し、国家単一AI政策との整合性確認
  - AI対応サイバーセキュリティの包括的枠組み導入
- **引用URL:** https://www.globalpolicywatch.com/2026/06/white-house-releases-executive-order-on-advanced-ai-innovation-and-security/
- **Evidence ID:** EVD-20260615-0016

### INFO-017
- **タイトル:** China prepares $295 billion plan to fund nationwide AI buildout
- **ソース:** Reuters / Bloomberg
- **公開日:** 2026-06-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-003-03, KIQ-002-06
- **関連企業:** ByteDance, DeepSeek
- **要約:** 中国が今後5年間で約2兆元（$295B）をかけて全国のデータセンターを構築する計画を準備中。新5カ年政策青写真でAIの積極的導入と新興技術での支配を目指す。世界第2の経済規模全体にAIを普及させる野心的計画。
- **キーファクト:**
  - 投資規模: 約2兆元（$295B）、5年間
  - 全国データセンター構築が主軸
  - 中国の新5カ年政策青写真の一部
- **引用URL:** https://www.reuters.com/world/china/china-prepares-295-billion-plan-fund-nationwide-ai-buildout-bloomberg-news-2026-06-09/
- **Evidence ID:** EVD-20260615-0017

### INFO-018
- **タイトル:** IBM Study: CIOs and CTOs Face Growing AI Control Gap as Enterprise Deployment Scales
- **ソース:** IBM（公式プレスリリース）
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** IBM
- **要約:** IBMが新調査を発表。80%の回答者がCEO主導のAI変革命令を報告する一方、2027年までにAIエージェントのデプロイ数が38%増加すると予測。AIコントロールギャップが拡大。87%がエンタープライズAIを未導入、ガバナンス要件が急務。
- **キーファクト:**
  - 2027年までにAIエージェント数38%増加予測
  - 80%がCEO主導のAI変革命令を報告
  - 87%がエンタープライズAI未導入
  - AIコントロールギャップの拡大
- **引用URL:** https://newsroom.ibm.com/2026-06-08-new-ibm-study-finds-cios-and-ctos-face-growing-ai-control-gap-as-enterprise-deployment-scales
- **Evidence ID:** EVD-20260615-0018

### INFO-019
- **タイトル:** KPMG Rolls Microsoft Agent 365 Out to 276,000 People
- **ソース:** Digital Applied / KPMG
- **公開日:** 2026-06-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-004-01, KIQ-004-03
- **関連企業:** KPMG, Microsoft
- **要約:** KPMGとMicrosoftが、KPMGがMicrosoft 365 CopilotとAgent 365を138カ国の全276,000人以上のプロフェッショナルに展開すると発表。KPMGは64%の組織がAIエージェントのために採用アプローチを変更したと報告。大手4会計事務所のエントリーレベル採用削減: KPMG 29%減、Deloitte 18%減。
- **キーファクト:**
  - KPMG: Microsoft 365 Copilot + Agent 365を276,000人全社員に展開
  - 64%の組織がAIエージェントにより採用アプローチ変更（前四半期は18%）
  - エントリーレベル採用削減: KPMG 29%減、Deloitte 18%減
  - 94%の組織が財務機能にAIを少なくとも部分的に導入
- **引用URL:** https://www.digitalapplied.com/blog/kpmg-microsoft-agent-365-deployment-2026-enterprise-governance-analysis
- **Evidence ID:** EVD-20260615-0019

### INFO-020
- **タイトル:** Pentagon reduces reliance on Anthropic, switches to competitors
- **ソース:** CryptoBriefing
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** 2026年3月、国防総省がAnthropicを「サプライチェーンリスク」として正式に指定し、事実上ブラックリスト入り。Anthropicは$200Mの軍事契約から撤退（自律型兵器・大量監視での使用拒否）。OpenAIは同じ制限付きでPentagon契約を獲得。4月8日、連邦控訴裁判所がAnthropicのサプライチェーンリスク指定の一時停止を却下。
- **キーファクト:**
  - 3月2026: 国防総省がAnthropicをサプライチェーンリスク指定
  - Anthropic $200M軍事契約から撤退: 自律型兵器・大量監視使用拒否が理由
  - OpenAI: 同じ制限条件でPentagon契約獲得
  - 4月8日: 連邦控訴裁判所がAnthropicの仮差止を却下（連邦裁判所で争い中）
- **引用URL:** https://cryptobriefing.com/pentagon-reduces-anthropic-reliance-competitors/
- **Evidence ID:** EVD-20260615-0020

### INFO-021
- **タイトル:** What Salesforce Learned from 20,000 Enterprise Agent Deployments
- **ソース:** ByteByteGo
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** Salesforce
- **要約:** Salesforceが20,000件のエンタープライズエージェントデプロイメントから得た知見。エンタープライズAIの未来は決定論的ワークフローと確率論的AIの組み合わせ。決定論的ワークフローがガードレールを設定し、確率論的AIが適応性と文脈理解を付加。
- **キーファクト:**
  - 20,000件のエンタープライズエージェントデプロイメント実績
  - 成功パターン: 決定論的ワークフロー（ガードレール）+ 確率論的AI（適応性）
  - エンタープライズ本番でのハイブリッド構成がベストプラクティス
- **引用URL:** https://blog.bytebytego.com/p/what-salesforce-learned-from-20000
- **Evidence ID:** EVD-20260615-0021

### INFO-022
- **タイトル:** ARC-AGI-3: Frontier models score below 1%, humans 100%
- **ソース:** Innovative Human Capital / Medium
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** （業界全体）
- **要約:** ARC-AGI-3（2026年3月リリース）でフロンティアAIモデルが1%未満のスコア、人間は100%成功率。ARC-AGI-2は0%から85%に1年以内に上昇。ARC-AGI-3は別リセット。Opus 4.8がARC-AGI-3で最高スコアを3倍に改善。MMLUは全フロンティアモデルが88%以上に飽和。
- **キーファクト:**
  - ARC-AGI-3: フロンティアモデル1%未満 vs 人間100%（2026年3月時点）
  - ARC-AGI-2: 0%→85%を1年で達成、ARC-AGI-3は別リセット
  - Opus 4.8: ARC-AGI-3で最高スコアを3倍に改善
  - MMLU: 全フロンティアモデル88%以上に飽和（GPT-5.3 Codexがリード）
- **引用URL:** https://www.innovativehumancapital.com/article/when-artificial-intelligence-confronts-the-unknown-arc-agi-3-and-the-future-of-adaptive-intelligenc
- **Evidence ID:** EVD-20260615-0022

### INFO-023
- **タイトル:** DeepSeek V4 Pro Wins the Precision Round
- **ソース:** FutureSearch / dev.to
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 Proが2026年4月24日にMITライセンスでリリース。V4-Proは1.6兆パラメータ。企業APIコールの中央値4.2%を獲得する予測。OpenAIはGPT-5.5 Proを$180/M出力トークンで維持、DeepSeekは1/5のコスト。コーディングリーダーボードでトップに立つ一方、企業シェアは限定的。
- **キーファクト:**
  - DeepSeek V4 Pro: 1.6兆パラメータ、MITライセンス、オープンウェイト
  - 企業APIコール予測中央値: 4.2%
  - GPT-5.5 Pro $180/M出力 vs DeepSeek 1/5コスト
  - コーディングベンチマークでトップレベルだが企業採用は限定的
- **引用URL:** https://futuresearch.ai/blog/deepseek-v4-pro-wont-move-the-market/
- **Evidence ID:** EVD-20260615-0023

### INFO-024
- **タイトル:** Claude Fable 5 Benchmark vs Gemini 3.1, GPT-5.5 and Grok 4
- **ソース:** Eden AI
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic, Google, OpenAI, xAI
- **要約:** Fable 5のベンチマーク比較。Fable 5がリード、Grok 4が約75%で最接近、GPT-5.5が58.6%、Gemini 3.1 Proが54.2%。SWE-Bench Pro等のコーディング性能でFable 5が最高。Artificial Analysis Intelligence Index: Claude Opus 4.8が61.4、GPT-5.5が60.2。
- **キーファクト:**
  - Fable 5: ベンチマーク総合リード
  - Grok 4: 約75%で最接近
  - GPT-5.5: 58.6%、Gemini 3.1 Pro: 54.2%
  - Artificial Analysis Intelligence Index: Opus 4.8 = 61.4, GPT-5.5 = 60.2
  - Vals Index: Fable 5 = 75.1%, Opus 4.8 = 70.4%
- **引用URL:** https://www.edenai.co/post/claude-fable-5-benchmark-vs-gemini-gpt-and-grok
- **Evidence ID:** EVD-20260615-0024

### INFO-025
- **タイトル:** Mistral is rumored to be raising €3B at €20B valuation
- **ソース:** TechCrunch / Bloomberg
- **公開日:** 2026-06-12
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03, KIQ-003-04
- **関連企業:** Mistral AI
- **要約:** 仏AIラボMistral AIが約€3B（$3.5B）の資金調達を協議中とBloombergが報じた。評価額€20B。オープンウェイトモデルの企業導入には不十分で、Mistralはサービス・推論・セルフホスティングを追加。オープンウェイトモデルがブランドセーフコンテンツに商用利用可能に。
- **キーファクト:**
  - 調達額: 約€3B（$3.5B）、評価額€20B
  - オープンウェイト単独では企業導入に不十分→サービス追加が必要
  - モジュラー展開・セルフホスティング・企業セキュリティに注力
- **引用URL:** https://techcrunch.com/2026/06/12/mistral-is-rumored-to-be-raising-e3b-at-e20-valuation/
- **Evidence ID:** EVD-20260615-0025

### INFO-026
- **タイトル:** AI Venture Funding Q1 2026: $242 Billion (80% of all global VC)
- **ソース:** Digital Applied / Crunchbase
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Databricks, Anthropic, xAI, Scale AI
- **要約:** 2026年Q1のAIスタートアップが$242Bを獲得、全グローバルVC資金の約80%。トップ10最資金調達企業: OpenAI、Databricks、Anthropic、xAI、Scale AI、Crusoe、Mistral、Cohere、Perplexity、Figure AI。Q2 2026のAI M&Aは156件の買収を分析、EV/Revenueマルチプルの分散が拡大。
- **キーファクト:**
  - Q1 2026 AI VC資金: $242B（全グローバルVCの80%）
  - トップ10: OpenAI, Databricks, Anthropic, xAI, Scale AI等
  - Q2 2026 AI M&A: 156件の買収を分析
- **引用URL:** https://www.digitalapplied.com/blog/ai-venture-funding-2026-where-242b-went-data-atlas
- **Evidence ID:** EVD-20260615-0026

### INFO-027
- **タイトル:** Anthropic autonomous weapons refusal and $200M Pentagon contract walk-away
- **ソース:** Fortune / Boston Globe / International Banker
- **公開日:** 2026-06-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic
- **要約:** Anthropicが完全自律型兵器や大量国内監視でのAI使用を拒否した結果、Pentagonとの$200M契約から撤退。Trump政権は2月に連邦機関へのAnthropic利用停止を命じ、3月に「サプライチェーンリスク」指定。Boston Globeは「殺人のビジネスから抜けるべき」と批判的論説。International Bankerは「誰が先進AIの配備を決定するか」の構造的対立と分析。
- **キーファクト:**
  - Anthropic: 完全自律型兵器・大量監視のAI使用を拒否
  - Pentagon $200M契約からの撤退
  - 2月: 連邦機関のAnthropic利用停止命令
  - 3月: サプライチェーンリスク指定
  - 4月8日: 連邦控訴裁判所で仮差止却下
- **引用URL:** https://www.bostonglobe.com/2026/06/14/opinion/anthropic-ai-military-weapon-pope/
- **Evidence ID:** EVD-20260615-0027

### INFO-028
- **タイトル:** Defense Production Act threat to force AI company access
- **ソース:** Jakarta Post / JustSecurity
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI
- **要約:** 国防総省が契約取消しやDefense Production Actを使ったアクセス強制を警告。AI企業が政府の利用条件に応じない場合、法的強制力でAIモデルへのアクセスを確保する可能性。構造的問題: 誰が先進AIの配備を決定するか。ECFRは欧州の対米経済的強制力への対応策を分析。
- **キーファクト:**
  - 国防総省: Defense Production ActによるAIアクセス強制の可能性を警告
  - 契約取消しや法的強制力での対応を示唆
  - 構造的問題: 企業の安全性判断 vs 政府の利用権
- **引用URL:** https://www.facebook.com/jakpost/posts/anthropics-relationship-with-the-government-ruptured-this-year-after-it-refused-/1478085784347232/
- **Evidence ID:** EVD-20260615-0028

### INFO-029
- **タイトル:** ByteDance AI pharma spin-off and Doubao monetization
- **ソース:** Sina Finance / Guandian / Sohu
- **公開日:** 2026-06-12
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, H-BTD-002-QUALITY
- **関連企業:** ByteDance
- **要約:** ByteDanceがAI製薬事業を独立企業として分離・独立資金調達を開始。コアチーム（約50人、劉凱責任者）とProtenixアルゴリズムが新会社へ。ByteDanceは過半数維持。同社は2026年AI関連資本支出を約1600億元から2000億元以上に引き上げ。Doubao大模型の有料化が進行中。
- **キーファクト:**
  - AI製薬事業分離: 独立資金調達、ByteDanceが過半数維持
  - コアチーム約50人 + Protenixアルゴリズム移管
  - 2026年AI資本支出: 1600億元→2000億元以上に増額
  - Doubao有料化進行中（商業収入の必要性）
- **引用URL:** https://finance.sina.cn/stock/med/2026-06-12/detail-iniccnfv0289064.d.html
- **Evidence ID:** EVD-20260615-0029

### INFO-030
- **タイトル:** ByteDance Seedance 2.0 video generation model
- **ソース:** GamsGo / Kinovi / Pakistan Today
- **公開日:** 2026-06-14
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのSeedance 2.0が2026年2月12日に中国でローンチ。テキストからシネマ品質のクリップを生成。マルチモーダル入力（テキスト・画像・音声・動画）から1080p動画をネイティブサウンド付きで生成。Fast/Proモード。バイラル動画が実写と見分けがつかない品質。
- **キーファクト:**
  - ローンチ: 2026年2月12日、中国
  - テキスト→シネマ品質動画、ネイティブサウンド付き
  - マルチモーダル入力: テキスト・画像・音声・動画
  - 1080p出力、Fast/Proモード
- **引用URL:** https://www.gamsgo.com/blog/seedance-price
- **Evidence ID:** EVD-20260615-0030

### INFO-031
- **タイトル:** Klarna AI Boomerang Effect: Replace humans with AI, then rehire
- **ソース:** Instagram / Prymage / Facebook
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** Klarna, Duolingo, IBM
- **要約:** IBM、Klarna、Duolingo等がAIで人員削減後に人間の再雇用を行う「AI Boomerang Effect」が発生。Klarnaは4年間で従業員を50%削減（5,500→3,400）、コスト計算は勝ったが品質で敗北。2026年初頭に人材再雇用開始。700名のカスタマーサービスをAIに置き換えた結果。
- **キーファクト:**
  - Klarna: 4年間で従業員50%削減（5,500→3,400）
  - コストは削減できたが品質で敗北
  - 2026年初頭に人材再雇用開始
  - 700名CSをAI置換後に品質問題で再雇用
  - Duolingoも外注スタッフ削減後にAI停止方針転換
- **引用URL:** https://prymage.com/insights/is-ai-saving-money-or-costing-more
- **Evidence ID:** EVD-20260615-0031

### INFO-032
- **タイトル:** AGI Timeline Predictions: Amodei 2027, Hassabis 2029-30, Clark 2028
- **ソース:** MSN / LinkedIn / Facebook
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Anthropic, Google DeepMind, OpenAI
- **要約:** AGIタイムライン予測の最新まとめ。Amodei（Anthropic CEO）は2027年、Hassabis（DeepMind CEO）は2029-30年、Clarkは2028年、Altmanは曖昧。Hassabisは臨床試験を2026年末までに目標とする。Gates、Hassabis、Amodei、Altmanが共同公開書簡を署名。
- **キーファクト:**
  - Amodei: AGI 2027年予測
  - Hassabis: AGI 2029-30年（±1年）
  - Clark: 2028年
  - Altman: 曖昧な表現
  - Hassabis: 臨床試験目標2026年末
- **引用URL:** https://www.msn.com/en-in/news/insight/google-deepmind-chief-predicts-agi-by-2030-urges-preparation/gm-GM732B702F
- **Evidence ID:** EVD-20260615-0032

### INFO-033
- **タイトル:** Germany plans AI safety institute to assess advanced model risks
- **ソース:** CADE Project
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** （ドイツ政府）
- **要約:** ドイツ政府が先進AIモデルの性能・能力・リスクを評価するAI安全研究所の創設を計画。CAISI（米国）がTrump政権下でも存続。2025 AI Action Planで再確認。英国AISIに続く欧州のAI安全インフラ整備。
- **キーファクト:**
  - ドイツ: 先進AIモデルのリスク評価機関を創設計画
  - CAISI（米国）: 2025 AI Action Planで再確認・存続
  - 欧州AI安全インフラの整備が進行
- **引用URL:** https://cadeproject.org/updates/germany-plans-ai-safety-institute-to-assess-risks-of-advanced-models/
- **Evidence ID:** EVD-20260615-0033

### INFO-034
- **タイトル:** EU AI Act high-risk requirements take effect August 2, 2026
- **ソース:** Boundless HQ / DeepInspect
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** （EU）
- **要約:** EU AI ActのハイリスクAIシステム要件が2026年8月2日に発効。違反時の罰金: 最大€35Mまたは全球売上の7%。ISO 42001認証が進行中。Fannie Mae LL-2026-04も8月6日発効。企業の準備期間が短く、コンプライアンス対応が急務。
- **キーファクト:**
  - ハイリスクAI要件: 2026年8月2日発効
  - 罰金: 最大€35M または全球売上7%
  - ISO 42001認証の普及
  - Fannie Mae LL-2026-04: 8月6日発効
- **引用URL:** https://boundlesshq.com/blog/what-is-the-eu-ai-act-everything-you-need-to-know/
- **Evidence ID:** EVD-20260615-0034

### INFO-035
- **タイトル:** Gartner: 40% of enterprise apps embed AI agents by end 2026
- **ソース:** dev.to / Appventurez
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** （業界全体）
- **要約:** Gartner予測: 2026年末までに企業アプリの40%がタスク特化AIエージェントを組み込む（前年は5%未満）。一方、Gartner（2026年5月）は2027年までに40%の企業が自律型AIエージェントを降格・廃止すると予測。ガバナンスギャップが本番後のみ表面化。
- **キーファクト:**
  - 2026年末: 企業アプリの40%がAIエージェント組み込み（前年<5%）
  - 2027年予測: 40%の企業が自律型AIエージェントを降格・廃止
  - ガバナンスギャップは本番運用後のみ表面化
- **引用URL:** https://dev.to/alexmercedcoder/the-direction-of-ai-in-2026-performance-cost-and-the-end-of-one-model-for-everything-1i6g
- **Evidence ID:** EVD-20260615-0035

### INFO-036
- **タイトル:** Federal AI vendor lock-in: "slouching toward vendor lock"
- **ソース:** Federal News Network
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05, KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** 連邦調達専門家が「AIベンダーロックインへの歩み」を警告。AIツールの「感情的・認知的現状維持（emotional and cognitive incumbency）」への依存が課題。AIベンダー選択はもはや調達決定ではなくガバナンス決定。EU AI Actのハイリスク要件(8月2日発効)が欧州でのベンダーロックインリスクを複合化。
- **キーファクト:**
  - AIツールへの「感情的・認知的現状維持」依存
  - ベンダー選択 = ガバナンス決定（調達決定ではない）
  - 欧州: EU AI Actハイリスク要件がベンダーロックインリスクを複合化
  - スイッチングコストはクラウドより高い（推論パターン再発見が必要）
- **引用URL:** https://federalnewsnetwork.com/commentary/2026/06/the-coming-ai-reckoning-slouching-toward-vendor-lock/
- **Evidence ID:** EVD-20260615-0036

### INFO-037
- **タイトル:** LLM API Pricing Comparison June 2026
- **ソース:** BenchLM
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01, KIQ-003-05
- **関連企業:** OpenAI, Anthropic, Google, xAI, Z.AI
- **要約:** 2026年6月のLLM API価格比較。GLM-5 (Reasoning) $1、Claude Haiku 4.5 $1、GPT-5.1 $1.25、Fable 5 $10/M入力・$50/M出力。DeepSeek V4 Proが1/5コストでGPT-5.5 Pro精度超過。価格戦争が常態化、600倍の価格差が存在。
- **キーファクト:**
  - GLM-5 (Reasoning): $1/M入力
  - Claude Haiku 4.5: $1/M入力
  - GPT-5.1: $1.25/M入力
  - Fable 5: $10/M入力、$50/M出力
  - 600倍の価格差が常態化
- **引用URL:** https://benchlm.ai/blog/posts/llm-pricing-2026
- **Evidence ID:** EVD-20260615-0037

### INFO-038
- **タイトル:** AI Agent Market projected to reach $182.97B by 2033
- **ソース:** SoftTeco / Grand View Research
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, KIQ-002-02
- **関連企業:** （業界全体）
- **要約:** Grand View Research予測: 全球AIエージェント市場が2033年までに$182.97Bに到達、2026年からの年成長率49.6%。2024年約$5.7Bから2030年までに$48.3Bへ。AIスタートアップがQ1 2026で$242Bを獲得（全グローバルVCの80%）。
- **キーファクト:**
  - 2033年: $182.97B予測、年成長率49.6%
  - 2024年: $5.7B → 2030年: $48.3B
  - Q1 2026 AI VC資金: $242B（全VCの80%）
- **引用URL:** https://softteco.com/blog/ai-agent-development-cost
- **Evidence ID:** EVD-20260615-0038

### INFO-039
- **タイトル:** Yann LeCun: LLMs are a dead end for superintelligence
- **ソース:** Instagram / Bulletin of Atomic Scientists
- **公開日:** 2026-06-14
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Meta AI
- **要約:** Yann LeCun（Meta AI）はLLMが汎用知能への道ではないと主張。「世界モデル」の構築が必要。Stuart Russell、Yoshua Bengio、Geoffrey Hintonの文書化した存在リスクは「人間のように考える」システムから来ない。Bulletin誌は「AGIのETAは技術的困難で再延期」と報じる。
- **キーファクト:**
  - LeCun: LLMはスーパーインテリジェンスへのデッドエンド
  - 必要なのは「世界モデル」の根本的に異なるアプローチ
  - Bengio/Russell/Hintonの存在リスク研究
  - Bulletin誌: AGI到達は技術的困難で再延期
- **引用URL:** https://thebulletin.org/2026/06/agis-eta-delayed-again-due-to-technical-difficulties/
- **Evidence ID:** EVD-20260615-0039

### INFO-040
- **タイトル:** Anthropic recursive self-improvement (RSI) exploration
- **ソース:** YouTube / SmarterX / Cloud Security Alliance
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** AnthropicがAIが自律的に自身の開発を加速する「再帰的自己改善（RSI）」の探求を進めている。Cloud Security AllianceがRSIのセキュリティ含意を分析。2026年時点で完全自律的な全スペクトラムRSIを実際に行うシステムは未観察。Claude Code生成コードの80-90%が自コードベースとの報告。
- **キーファクト:**
  - Anthropic: RSIの探求を進行中
  - CSA: RSIのセキュリティ含意分析を公表
  - 2026年時点: 完全自律RSIシステムは未観察
  - Claude Code自コードベース80-90%報告（第三者検証不在）
- **引用URL:** https://smarterx.ai/smarterxblog/exec-ai-anthropic-recursive-self-improvement
- **Evidence ID:** EVD-20260615-0040

### INFO-041
- **タイトル:** $130 Billion in AI data centers blocked or delayed in Q1 2026
- **ソース:** TechWorm / Texas Tribune
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, KIQ-002-03
- **関連企業:** （業界全体）
- **要約:** 2026年第1四半期だけで草の根・超党派的反対により少なくとも75件の米国データセンター計画がブロック・遅延。Texas Tribuneは少なくとも248件の計画データセンターを特定。電力・水資源への懸念が主要因。Goldman Sachsはアジアのデータセンター需要の成長を予測。
- **キーファクト:**
  - Q1 2026: 75件以上の米国データセンター計画がブロック・遅延
  - Texas: 248件以上の計画データセンター
  - 電力・水資源への懸念が主要反対理由
  - アジア: 伝統的クラウド + AIファースト需要で成長予測
- **引用URL:** https://www.facebook.com/techworm.in/posts/-130-billion-in-ai-data-centers-blockedthe-gold-rush-to-build-the-physical-infra/1312218164396104/
- **Evidence ID:** EVD-20260615-0041

### INFO-042
- **タイトル:** Apple unveils next generation of Apple Intelligence, Siri AI
- **ソース:** Apple Newsroom
- **公開日:** 2026-06-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** Apple
- **要約:** Appleが次世代Apple IntelligenceとSiri AIを発表。WWDC 2026基調講演でのプレビュー。iOS/macOS次期アップデートの目玉機能。GeminiモデルのApple開発者への提供も発表済み。
- **キーファクト:**
  - 次世代Apple Intelligence + Siri AI発表
  - GeminiモデルのApple開発者への提供
  - エコシステム統合の深化
- **引用URL:** https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/
- **Evidence ID:** EVD-20260615-0042

### INFO-043
- **タイトル:** OpenAI vs Anthropic IPO race: both confidentially filed
- **ソース:** Yahoo Finance / Instagram
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIとAnthropicが両方とも機密IPO提出を完了、秋の上場競争。Anthropic評価額$965B、OpenAIはそれ以上。SpaceX IPOは$135/株（評価額約$1.8T）で価格設定中。AnthropicのFable 5停止事件がIPO投資家の懸念材料。OpenAIのChatGPT Plusは4400万(2025)→900万(2026)に減少予測。
- **キーファクト:**
  - OpenAI: 機密S-1提出済み、秋上場予定
  - Anthropic: 機密IPO提出、評価額$965B
  - SpaceX: $135/株、評価額約$1.8TでIPO価格設定中
  - OpenAI ChatGPT Plus: 4400万→900万へ減少予測（The Information）
- **引用URL:** https://finance.yahoo.com/video/openai-vs-anthropic-ipo-what-sets-these-ai-companies-apart-195206256.html
- **Evidence ID:** EVD-20260615-0043

### INFO-044
- **タイトル:** OpenAI Skills marketplace, Codex skill catalogs, and Antigravity migration
- **ソース:** OpenAI Community / Cosmic / Digital Applied
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** OpenAI, Google
- **要約:** OpenAI Codex Skillsカタログが拡大、重複スキル管理が課題。ローカルシェルスクリプトをCodexにバインド可能。Codexはサンドボックス化クラウド環境で実行。Google Antigravity Skillsがオープンフォーマットで展開。Gemini CLIが6月18日に終了、Antigravityに移行。1000+エージェントスキルのコレクションがクロスプラットフォーム対応。
- **キーファクト:**
  - OpenAI Codex Skills: カタログ拡大、ローカルシェルスクリプトバインド可能
  - Codex: サンドボックス化クラウド環境で実行
  - Gemini CLI: 6月18日終了→Antigravity移行
  - Google Antigravity Skills: オープンフォーマット
  - VoltAgent: 1000+エージェントスキル、Claude Code/Codex/Gemini CLI/Cursor互換
- **引用URL:** https://www.cosmicjs.com/blog/claude-code-vs-codex-vs-cursor
- **Evidence ID:** EVD-20260615-0044

### INFO-045
- **タイトル:** Fortune 500 Agentic AI adoption: 80% adopting, JPMorgan & Walmart cases
- **ソース:** VertexPlus / CockroachDB / IDC
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** JPMorgan, Walmart
- **要約:** Fortune 500の80%が2026年にagentic AI導入。CockroachDBのケーススタディ: 50,000文書/月処理でキャッシュあり$8,000 vs なし$45,000（82%削減）。IDCはROIモデルが非線形・コストが動的と指摘。23%の企業が少なくとも1機能でAIエージェントをスケール中。
- **キーファクト:**
  - Fortune 500の80%がagentic AI導入中
  - キャッシング: 50K文書/月で$8K vs $45K（82%節約）
  - 23%の企業がAIエージェントをスケール中
  - IDC: ROIは非線形、コストは動的、継続的ROI評価が不可欠
- **引用URL:** https://www.vertexplus.com/blog/agentic-ai-adoption-trends-among-fortune-500-enterprises-in-2026
- **Evidence ID:** EVD-20260615-0045

### INFO-046
- **タイトル:** Canada PM Carney warns US AI restrictions show danger of over-reliance
- **ソース:** Fortune (AP)
- **公開日:** 2026-06-14
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-002-03, KIQ-002-01
- **関連企業:** Anthropic
- **要約:** カナダのMark Carney首相が、米国のAnthropic AIモデル制限は「米国プロバイダーへの過度な依存の危険性」を示すと警告。同盟国政府・研究者・商用顧客を含むアクセス停止は国際的なAI依存リスクの具体化。主権的AIインフラの必要性が国際的に認識。
- **キーファクト:**
  - カナダ首相: 米国AI制限は「過度な依存の危険性」を示す
  - 同盟国政府・研究者を含むアクセス停止の国際的影響
  - 主権的AIインフラの必要性への国際的認識
- **引用URL:** https://fortune.com/2026/06/14/canadian-prime-minister-mark-carney-warns-u-s-restrictions-on-new-anthropic-ai-models-show-danger-of-relying-too-much-on-american-providers/
- **Evidence ID:** EVD-20260615-0046

### INFO-047
- **タイトル:** Anthropic Policy on the AI Exponential: government authority to block deployments
- **ソース:** Anthropic（公式）
- **公開日:** 2026-06-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-002-06, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** Anthropicが「Policy on the AI Exponential」を公表。政府が最先端AIモデルの破局的リスクに対処するための提案: 独立安全テストの義務化、透明性要件、危険なAI配備のブロック・リコール権限を含む法定プロセス。透明・公平・明確・技術的事実に基づくべきと主張。Fable 5停止はこの原則に従っていないと批判。
- **キーファクト:**
  - 政府権限: 安全でないAI配備のブロック・リコール（法定プロセス）
  - 必須要件: 独立安全テスト・透明性
  - 原則: 透明・公平・明確・技術的事実に基づく
  - Fable 5停止指令はこれらの原則に違反と主張
- **引用URL:** https://www.anthropic.com/policy-on-the-ai-exponential
- **Evidence ID:** EVD-20260615-0047

### INFO-048
- **タイトル:** SHRM: Automation, AI, and Job Displacement Risk in U.S. Employment (2026)
- **ソース:** SHRM
- **公開日:** 2026-06-13
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-01, KIQ-004-02
- **関連企業:** （業界全体）
- **要約:** SHRMの2026年報告書: 平均タスク自動化が過去1年で著しく上昇。一方、雇用のうちAI変位リスクに直面する割合は限定的。約2.5%の米国雇用がAI効率化による変位リスク。87,714件の職が5ヶ月で削減された報告。HBR分析: 企業はAIの潜在力に基づいてレイオフを実施している可能性。
- **キーファクト:**
  - タスク自動化: 過去1年で著しく上昇
  - 雇用変位リスク: 約2.5%の米国雇用
  - 5ヶ月で87,714件の職削減報告
  - HBR: AIポテンシャルに基づくレイオフの可能性
- **引用URL:** https://www.shrm.org/topics-tools/research/automation-generative-ai-and-job-displacement-risk-in-u-s--employment/2026-full-report
- **Evidence ID:** EVD-20260615-0048

### INFO-049
- **タイトル:** Best AI Coding Agents 2026: Harness, Cost, and Accuracy comparison
- **ソース:** Firecrawl / MorphLLM / MarkTechPost
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-004-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** 2026年のAIコーディングエージェント比較: 12エージェントをランキング。Terminal-Bench最高スコアとクラウドタスクのfire-and-forget能力で評価。Claude Code vs Codex vs Cursor比較: Codexはサンドボックスクラウド環境で実行、Claude Codeはローカル実行。Hermes Agent（Nous Research）が自己改善型として新参入、57,000+ GitHub stars。
- **キーファクト:**
  - 12コーディングエージェントをベンチマーク価格で比較
  - Hermes Agent (Nous Research): 自己改善型、57,000+ GitHub stars
  - Claude Opus 4.7: MCP-Atlas 76.4%でコーディングリード
  - オープンウェイトモデルがコーディングギャップをほぼ解消
- **引用URL:** https://www.firecrawl.dev/blog/best-ai-coding-agents
- **Evidence ID:** EVD-20260615-0049

### INFO-050
- **タイトル:** 15 New Six-Figure Careers as AI Rewrites the Rules
- **ソース:** Forbes
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03, KIQ-004-04
- **関連企業:** （業界全体）
- **要約:** AI時代の新職種: Chief AI Officer、AI Engineer、Cloud Architect、Influencer Manager、Data Protection Officer。AI Content Strategistが需要拡大。VisaがDirector of AI Strategy & Automationを募集。AI Creative Directorが新役職として出現。BCG: AI成功はトレーニング以上、組織変革が必要。
- **キーファクト:**
  - 新6桁年収職種: Chief AI Officer、AI Engineer、Cloud Architect等
  - AI Content Strategist: 需要急増
  - Visa: Director of AI Strategy & Automationを募集中
  - AI Creative Director: 新役職として出現
- **引用URL:** https://www.forbes.com/sites/bryanrobinson/2026/06/11/15-new-six-figure-careers-worth-betting-on-as-ai-rewrites-the-rules/
- **Evidence ID:** EVD-20260615-0050

### INFO-051
- **タイトル:** OpenAI Academy courses and Economic Research Exchange
- **ソース:** OpenAI（公式ブログ）
- **公開日:** 2026-06-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-01, KIQ-004-03, KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIが「Economic Research Exchange」を発表。AIの経済的影響を研究する研究者に$25,000研究助成金 + $7,500/月のスチペンドを提供。同時にOpenAI Academy新コース群を発表。AIスキル教育エコシステムの拡大。
- **キーファクト:**
  - Economic Research Exchange: $25K助成金 + $7,500/月スチペンド
  - OpenAI Academy: 新コース群（仕事でのAI適用）
  - AIの経済的影響研究への投資
- **引用URL:** https://openai.com/index/economic-research-exchange/
- **Evidence ID:** EVD-20260615-0051

### INFO-052
- **タイトル:** Great American AI Act (GAAIA) discussion draft released
- **ソース:** Subject to Inquiry
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06, KIQ-005-03
- **関連企業:** （米国政府）
- **要約:** 2026年6月4日、Jay ObernolteとLori Trahan議員がGreat American AI Act（GAAIA）の検討草案を発表。連邦AI政策の包括的枠組み。大統領令(6月2日)と併せて、AI企業に対する政府の権限拡大が進行。State AI法との調整も焦点。
- **キーファクト:**
  - GAAIA検討草案: 2026年6月4日発表（Obernolte + Trahan議員）
  - 連邦AI政策の包括的枠組み
  - 大統領令(6/2)と併せた政府権限拡大の文脈
- **引用URL:** https://www.subjecttoinquiry.com/2026/06/the-great-american-ai-act-what-it-means-and-doesnt-mean-for-companies-using-ai/
- **Evidence ID:** EVD-20260615-0052

### INFO-053
- **タイトル:** [Deep Scrape] Pentagon Anthropic rift timeline: 2/3 workload shift, $200M cancelled, First Amendment block
- **ソース:** CryptoBriefing（詳細スクレイプ）
- **公開日:** 2026-06-12
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google, Microsoft
- **要約:** Pentagon/Anthropic対立の完全タイムライン。2025年7月: $200M契約をAnthropic/OpenAI/Google/xAIに各社付与。2026年初頭: Pentagonが無制限軍事利用（大量監視・自律型兵器含む）を要求、Amodei拒否。2026年3月: Anthropicをサプライチェーンリスク指定（連邦ブラックリスト相当）。その後判事が修正第1条（言論の自由）を根拠に指定をブロック。契約の一部は完全取消し。2026年6月までにDoDはAIワークロードの少なくとも2/3をAnthropicから他社に移行。OpenAI、Google、Microsoftが正式契約を獲得。
- **キーファクト:**
  - 2025年7月: Pentagon $200M契約（4社均等配分）
  - 2026年3月: Anthropicサプライチェーンリスク指定→判事が修正第1条でブロック
  - ワークロード2/3移行完了
  - OpenAIが最速で防血ポートフォリオ拡大、2024年初頭に軍事利用禁止条項を静かに削除済み
  - Google/Microsoft: クラウド連邦契約の深い関係で自然受益者
  - 投資家含意: サプライチェーンリスク指定が恒久解除か一時停止かが業界全体のacceptable use policyリスクを左右
- **引用URL:** https://cryptobriefing.com/pentagon-reduces-anthropic-reliance-competitors/
- **Evidence ID:** EVD-20260615-0053

### INFO-054
- **タイトル:** [Deep Scrape] Anthropic Advanced AI Framework: 10^25 FLOPs threshold, $500M revenue, block/deter authority
- **ソース:** Anthropic（公式、詳細スクレイプ）
- **公開日:** 2026-06-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-03, KIQ-002-06, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** Anthropicの「Policy on the AI Exponential」詳細。Advanced AI FrameworkとEconomic Policy Frameworkの2本柱。適用閾値: 10^25 FLOPs超で訓練、AI関連収入$500M超またはAI R&D支出$1B超の企業。4種の破局的リスク: 生物・サイバー・制御喪失・自動化R&D。政府は危険なデプロイをブロック・抑止する法定権限を持つべき。全球年収連動の民事罰金、反復違反でエスカレート。州法の先取りは連邦法が同等以上の場合のみ。Mythos Previewが全主要OS・ブラウザの高 severity 脆弱性を発見済み。
- **キーファクト:**
  - 適用閾値: 10^25 FLOPs / AI収入$500M超 / AI R&D $1B超
  - 4リスク: 生物兵器・サイバー・制御喪失・自動化R&D
  - 政府権限: 危険デプロイのブロック・抑止、全球年収連動罰金
  - 開発者義務: 透明性（テスト結果公表）・独立評価・セキュリティプログラム
  - 州法先取り制限: 連邦法が同等以上の場合のみ認める
  - Mythos Preview: 全主要OS・ブラウザの高severity脆弱性を発見
- **引用URL:** https://www.anthropic.com/policy-on-the-ai-exponential
- **Evidence ID:** EVD-20260615-0054

### INFO-055
- **タイトル:** [Deep Scrape] KPMG Agent 365 governance: $49.7M/yr control plane, "agent debt" concept
- **ソース:** Digital Applied（詳細スクレイプ）
- **公開日:** 2026-06-11
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-004-01
- **関連企業:** KPMG, Microsoft, Salesforce, Google
- **要約:** KPMG/Agent 365デプロイメントの詳細分析。Agent 365は2026年5月1日GA。コスト: $15/user/月（単体）または$99/user/月（M365 E7バンドル）。KPMG 276,000人×$15 = 約$49.7M/年（ガバナンス層単独）。ガバナンスギャップ: 72%が本番でエージェント稼働、21%のみ成熟ガバナンス。新概念「agent debt」: オーナー・期限・ID・監査証跡なしのエージェントが複利で蓄積する負債。Client Zero パターン: 自社でガバナンスを実装してから顧客に提供する戦略。Microsoft Agent 365はAWS Bedrock・Google Cloudのエージェント発見（プレビュー）を含むクロスベンダー対応が差別化要因。
- **キーファクト:**
  - Agent 365 GA: 2026年5月1日、$15/user/月 or E7バンドル$99/user/月
  - KPMG規模: ガバナンス層単独で約$49.7M/年（リスト価格）
  - ガバナンスギャップ: 72%稼働 vs 21%成熟ガバナンス
  - 「agent debt」概念: オーナー/期限/監査証跡なしエージェントの複利負債
  - クロスベンダー発見: AWS Bedrock + Google Cloud（プレビュー）
  - Client Zero パターン: 自社実装→商品化の順序
- **引用URL:** https://www.digitalapplied.com/blog/kpmg-microsoft-agent-365-deployment-2026-enterprise-governance-analysis
- **Evidence ID:** EVD-20260615-0055

### INFO-056
- **タイトル:** [Deep Scrape] White House AI Executive Order: 30-day cyber directives, voluntary frontier model review
- **ソース:** Global Policy Watch / Covington（詳細スクレイプ）
- **公開日:** 2026-06-11
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06, KIQ-005-03
- **関連企業:** （米国政府）
- **要約:** 2026年6月2日の大統領令「Promoting Advanced AI Innovation and Security」の詳細分析。2本柱: (1)「先進AI」に対するサイバー防御強化、(2)「フロンティアAIモデル」の任意ベンチマーキング・レビュー枠組み。30日以内の指令: 国家安全保障システムのサイバー防御優先化、CISAによる民間政府システムの防衛、AIサイバーセキュリティ情報交換所の設立、連邦助成金プログラムの見直し。60日以内: サイバー専門家の採用加速。法的強制力は任意（voluntary）で、ライセンス・許可・事前審査要件ではない。リリース予定の30日前までに政府への限定的アクセス提供を開発者に促す。「Department of War」という用語の使用。
- **キーファクト:**
  - 発効: 2026年6月2日
  - 30日指令: NSS/DoWシステム防御、CISA防衛指令、AIサイバー情報交換所設立
  - 60日指令: サイバー専門家採用加速
  - フロンティアモデル: リリース30日前の政府アクセス（任意）
  - 「voluntary」明記: 強制ライセンス・許可・事前審査ではない
  - 「Department of War」の用語使用（DoD改名の文脈）
- **引用URL:** https://www.globalpolicywatch.com/2026/06/white-house-releases-executive-order-on-advanced-ai-innovation-and-security/
- **Evidence ID:** EVD-20260615-0056

### INFO-057
- **タイトル:** Anthropic Recursive Self-Improvement Institute findings
- **ソース:** Anthropic（公式）
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Anthropic
- **要約:** Anthropicの再帰的自己改善（RSI）研究所の発見。AIが自身の能力向上に直接的に貢献するプロセスの証拠を報告。Claudeが自身のコードベース開発に80-90%貢献との報告だが、第三者検証不在。RSIが急速な能力向上を加速する可能性。Anthropic Policy on the AI Exponential内でautomated R&Dを4つの破局的リスクの1つとして分類。
- **キーファクト:**
  - RSI Institute: Anthropic内の専門研究部門
  - Claude: 自コードベース80-90%貢献報告（第三者検証なし）
  - automated R&D: 4つの破局的リスクの1つとして位置づけ
  - RSIが能力向上を加速するメカニズムの証拠
- **引用URL:** https://www.anthropic.com/institute/recursive-self-improvement
- **Evidence ID:** EVD-20260615-0057

### INFO-058
- **タイトル:** Drata expands Trust Management Platform for AI Agent Governance; enterprise AI security gap widens
- **ソース:** Drata（公式プレスリリース） / Orca Security / LinkedIn
- **公開日:** 2026-06-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** Drata, Orca Security, NICE
- **要約:** DrataがAIエージェントガバナンスを次のエンタープライズセキュリティ分野と宣言、Trust Management Platformを拡張。Gartner: Q1 2026に出荷・更新されたエンタープライズアプリの80%がAIエージェントを組み込み（2024年33%）。しかし企業はAI能力$750に対しAIセキュリティにわずか$1を投資（750:1比）。NICEはSOC 2 Type II、ISO 27001、PCI DSS、FedRAMP認証を維持。規制産業でのAIセキュリティベストプラクティス需要が急増。
- **キーファクト:**
  - Gartner: Q1 2026エンタープライズアプリの80%にAIエージェント（2024年33%）
  - AIセキュリティ投資比: 能力$750対セキュリティ$1（750:1）
  - Drata: AI Agent Governanceをエンタープライズセキュリティの次分野と宣言
  - NICE: SOC 2 Type II、ISO 27001、PCI DSS、FedRAMP認証維持
- **引用URL:** https://drata.com/about/news/drata-expands-trust-management-platform-to-support-governance-of-enterprise-ai-agents
- **Evidence ID:** EVD-20260615-0058

### INFO-059
- **タイトル:** AI disintermediation in advertising: programmatic automation and agentic commerce reshape value chain
- **ソース:** eMarketer / Tinuiti / FCA
- **公開日:** 2026-06-13
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-001-03
- **関連企業:** Meta, Google
- **要約:** AIがプログラマティック広告に深く組み込まれ、広告代理店・中間事業者のバリューチェーンを侵食。Tinuitiは「agentic commerce」の台頭を報告: AIエージェントが消費者の代わりに購買を行い、従来のファネルを再構築。FCA: 金融サービスにAIエージェントが消費者-企業間の主要インターフェースとなる新層が出現。MobavenueのPrsmX等のAI広告プラットフォームが新興市場で拡大。PLM市場$87.5Bに到達もAIによる業務変革が進行。
- **キーファクト:**
  - プログラマティック広告: AI自動化が深化、代理店中抜きリスク
  - Agentic commerce: AIエージェントが消費者代理で購買、ファネル再構築
  - FCA: 金融サービスでAIエージェントが新インターフェース層
  - 広告予算の配分がAI仲介により変化
- **引用URL:** https://tinuiti.com/blog/commerce/agentic-commerce/
- **Evidence ID:** EVD-20260615-0059
