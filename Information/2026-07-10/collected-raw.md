# 収集データ: 2026-07-10

## メタデータ
- 収集日時: 2026-07-10 00:10 UTC
- 品質フラグ: NORMAL
- 収集統計:
  - 検索クエリ数: 80（collection_plan: 56, 動的Arbiter: 15, 補完: 9）
  - スクレイプ数: 8（公式ブログマップ: 4, 記事スクレイプ: 4）
  - INFO件数: 93
  - Evidence ID範囲: EVD-20260710-0001 〜 EVD-20260710-0093
- KIQカバレッジ:
  - KIQ-001-01 (Agent SDK/API): ✅ INFO-003, 005, 015, 020, 093
  - KIQ-001-02 (エンタープライズ展開): ✅ INFO-008, 012, 042
  - KIQ-001-03 (開発者エコシステム): ✅ INFO-025, 035, 036
  - KIQ-001-04 (マルチモーダル): ✅ INFO-001, 069, 086
  - KIQ-001-05 (スキル配布/ロックイン): ✅ INFO-030, 031, 032
  - KIQ-002-01 (クラウド統合): ✅ INFO-018, 040
  - KIQ-002-02 (エンタープライズ採用率): ✅ INFO-038, 042
  - KIQ-002-03 (規制環境): ✅ INFO-050, 051, 088
  - KIQ-002-06 (政府経済的圧力): ✅ INFO-046, 047, 048, 049, 060, 061, 062
  - KIQ-002-04 (業務自律化): ✅ INFO-055, 056, 057, 058
  - KIQ-002-05 (バリューチェーン侵食): ✅ INFO-043, 044, 045
  - KIQ-003-01 (API料金): ✅ INFO-016, 017, 091
  - KIQ-003-02 (ベンチマーク): ✅ INFO-002, 013, 014, 093
  - KIQ-003-03 (OSS vs商用): ✅ INFO-039, 089, 091
  - KIQ-003-04 (資金調達/投資): ✅ INFO-006, 007, 066, 067, 085, 087
  - KIQ-003-05 (スイッチングコスト): ✅ INFO-027, 028, 029
  - KIQ-004-01 (先行領域自律化): ✅ INFO-055, 056, 057, 058, 059
  - KIQ-004-02 (コーディング価値変化): ✅ INFO-052, 053, 054
  - KIQ-004-03 (AI代替困難能力): ✅ INFO-063, 064, 065
  - KIQ-004-04 (AI時代の勝者): ✅ INFO-068, 092
  - KIQ-005-01 (AGIベンチマーク): ✅ INFO-070, 071, 093
  - KIQ-005-02 (AGIタイムライン): ✅ INFO-072, 073, 090
  - KIQ-005-03 (AGI安全性ガバナンス): ✅ INFO-074, 075, 076, 088
  - BYTEDANCE-CHINESE (中国語一次情報): ✅ INFO-085, 086, 087
  - 動的KIQカバレッジ:
    - KIQ-OAI-001 (OpenAI政府収益): ✅ INFO-046, 047, 048
    - KIQ-MIL-001 (自律兵器): ✅ INFO-060, 061, 062
    - KIQ-CAR-002-OPS (設計/評価スキル価値): ✅ INFO-053, 063
    - KIQ-ANT-002 (Claude Code DAU/WAU): ✅ INFO-004, 005
    - KIQ-NEW-001 (5%政府持分): ✅ INFO-048, 049
- 動的追加クエリ（Arbiter優先KIQ）:
  - KIQ-OAI-001: "OpenAI revenue breakdown government vs commercial contracts", "OpenAI government contract revenue percentage breakdown", "OpenAI financial report commercial vs government income 2026"
  - KIQ-MIL-001: "autonomous weapons human override ratio Pentagon AI", "Lethal Autonomous Weapons Systems human control requirement treaty", "DoD AI weapons human-in-the-loop policy 2026"
  - KIQ-CAR-002-OPS: "AI coding evaluation design skill market value salary premium", "design thinking AI era job market value quantitative", "problem definition skill AI irreplaceable salary premium"
  - KIQ-ANT-002: "Claude Code DAU WAU daily active users statistics", "Claude Code developer adoption metrics usage", "Anthropic Claude Code usage statistics enterprise"
  - KIQ-NEW-001: "OpenAI 5 percent government equity stake proposal other companies response", "government equity stake AI company Anthropic Google Meta reaction", "AI company government ownership Trump OpenAI stock deal"

## 収集結果

### INFO-001
- **タイトル:** Introducing Claude Sonnet 4.6
- **ソース:** Anthropic 公式ブログ
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Sonnet 4.6を発表。コーディング、コンピュータ使用、長文脈推論、エージェント計画、知識作業、デザインの全面アップグレード。1Mトークンコンテキストウィンドウ（ベータ）。Sonnet 4.5と同じ価格（$3/$15 per million tokens）。
- **キーファクト:**
  - ユーザーはSonnet 4.5より約70%の頻度でSonnet 4.6を好む（Claude Code内）
  - Opus 4.5より59%の頻度でSonnet 4.6を好む
  - OSWorld-Verifiedで大幅改善、プロンプトインジェクション耐性も向上
  - Vending-Bench Arenaで独自の戦略（前期投資→後期収益化）を開発
  - Web検索、コード実行、メモリ、プログラムツール呼び出しがGA化
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6
- **Evidence ID:** EVD-20260710-0001

### INFO-002
- **タイトル:** Pentagon Shifts AI Workload from Anthropic to OpenAI, Google, and Microsoft
- **ソース:** CryptoBriefing / KuCoin
- **公開日:** 2026-06-12
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001, KIQ-OAI-001
- **関連企業:** Anthropic, OpenAI, Google, Microsoft
- **要約:** PentagonがAnthropicのAIワークロードの少なくとも3分の2をOpenAI/Google/Microsoftに移管。Anthropicが制限なし使用（監視・自律兵器含む）を拒否した結果、2026年3月に供給チェーンリスク指定を受けたが、判事が修正条項でブロック。$200M契約の一部がキャンセル。
- **キーファクト:**
  - 2025年7月: 各社（Anthropic, OpenAI, Google, xAI）に$200M契約配分
  - 2026年初頭: PentagonがAnthropicに無制限使用を要求、Amodei拒否
  - 2026年3月: Anthropicに供給チェーンリスク指定（連邦ブラックリスト相当）、判事が修正条項違反でブロック
  - 2026年6月: OpenAI/Google/Microsoftが正式契約化
  - OpenAIが最速で防衛ポートフォリオを拡大
- **引用URL:** https://www.kucoin.com/news/flash/pentagon-shifts-ai-workload-from-anthropic-to-openai-google-and-microsoft
- **Evidence ID:** EVD-20260710-0002

### INFO-003
- **タイトル:** OpenAI Proposes 5% Equity Stake to U.S. Government (~$42.6B)
- **ソース:** Financial Times / The Guardian / CNBC / TechJack Solutions
- **公開日:** 2026-07-05
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-NEW-001, KIQ-002-06, KIQ-003-04
- **関連企業:** OpenAI, Anthropic, Google, Meta
- **要約:** OpenAI CEO Sam Altmanが主要米国AI企業に5%エクイティを政府に提供するよう提案。OpenAIの$852B評価額で約$42.6Bに相当。Alaska Permanent Fundモデル。他社（Anthropic, Google, Meta）は枠組みに含まれるが公開見解なし。政府がAI企業のオーナー兼監督者となる構造的緊張。
- **キーファクト:**
  - $852B評価額の5% = 約$42.6B
  - FT発信、Guardian/CNBC確認済み
  - Trump政権は「初期段階の議論」、正式受諾・拒否なし
  - 他社参加はAltmanの構想に含むが公開見解なし（N=1継続）
  - 政府持分は規制の代替か補完かが重要論点
- **引用URL:** https://techjacksolutions.com/ai-brief/openai-5-percent-government-equity-stake-proposal/
- **Evidence ID:** EVD-20260710-0003

### INFO-004
- **タイトル:** Pentagon's $54 Billion Autonomous Warfare Blueprint (DAWG + NSPM-11)
- **ソース:** The Geostrata
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001, KIQ-005-03
- **関連企業:** (政府・軍, 全AI企業)
- **要約:** PentagonのDefense Autonomous Warfare Group (DAWG)がFY2026-27予算で$54Bを要求。NSPM-11が2026年初頭発効で軍の自律性プログラムを実質承認。しかし自律性・殺傷権限・エスカレーション管理の具体的運用定義は不在。「人間の監督」は名目的で、高強度紛争では実効性に疑義。
- **キーファクト:**
  - DAWG FY2026-27予算: $54B（空・海・陸領域の自律システム開発）
  - NSPM-11: 2026年春発効、軍の自律プログラムを実質承認
  - 人間の介入は名目的: システム推奨が事実上の決定となる「2秒の決定窓」問題
  - 中国の「智能化戦争」ドクトリンとの競争が圧力源
  - 交戦規定のガバナンス枠組みが技術展開に後れを取る
- **引用URL:** https://www.thegeostrata.com/post/ai-war-revolution-pentagon-s-54-billion-autonomous-warfare-blueprint
- **Evidence ID:** EVD-20260710-0004

### INFO-005
- **タイトル:** OpenAI & Anthropic Revenue Data: Combined ~$100B ARR, OpenAI Still Loss-Making
- **ソース:** SemiAnalysis / GetLatka / Forbes
- **公開日:** 2026-07-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-OAI-001, KIQ-003-04
- **関連企業:** OpenAI, Anthropic
- **要約:** OpenAIの2026年ARRは$20-33B（ソースによりばらつき）。Anthropicは$47B ARRでOpenAIを上回ったという報道も。OpenAIは1ドル稼ぐごとに約$1.22損失。Anthropicは3Q26に$1B超の利益を計上。政府vs民間の収益内訳は依然として非公開（KIQ-OAI-001 17R不在継続確認）。
- **キーファクト:**
  - OpenAI ARR: $20-33B（GetLatka $20B / 他報道 $33B）
  - OpenAI評価額: $852B
  - Anthropic ARR: $47B（一部報道、SemiAnalysisは利益計上確認）
  - OpenAI+Anthropic合計ARR ~$100B (SemiAnalysis)
  - ファウンデーションモデルはQ1 2026収益の仅か11%、82%はホスティング
  - 政府vs民間内訳: 依然として非公開
- **引用URL:** https://newsletter.semianalysis.com/p/anthropic-3q26-profit-over-1b-the
- **Evidence ID:** EVD-20260710-0005

### INFO-006
- **タイトル:** Claude Code Statistics 2026: $2.5B Run-Rate, 18% Workplace Adoption
- **ソース:** Panto AI / Uvik Software / JetBrains
- **公開日:** 2026-07-04
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-ANT-002, KIQ-001-01, KIQ-004-02
- **関連企業:** Anthropic
- **要約:** Claude Codeが$2.5Bランレート到達（2026年初頭）。職場での採用率はCursorと同率18%（GitHub Copilot 29%に次ぐ）。5,000エンジニア組織で84%浸透の事例。固有のDAU/WAU指標は依然として非公開（KIQ-ANT-002 15R不在だが部分充足データ）。
- **キーファクト:**
  - Claude Code ランレート: $2.5B（2026年初頭）
  - 職場採用率: 18%（JetBrains Jan 2026、Cursorと同率）
  - GitHub Copilot: 29%（26M+ユーザー）
  - 大企業例: 5,000エンジニア組織で84%浸透
  - 固有DAU/WAU: 依然として公開データなし
- **引用URL:** https://www.getpanto.ai/blog/claude-ai-statistics
- **Evidence ID:** EVD-20260710-0006

### INFO-007
- **タイトル:** Claude Enterprise Spend Controls Arrive as Agentic AI Bills Blow Past Budgets
- **ソース:** TechTimes / Finout
- **公開日:** 2026-07-04
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-ANT-002, KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Anthropicが2026年7月にClaude Enterprise向けコスト管理機能（ダッシュボード、支出制限、使用量API）を追加。エージェントAIの請求が予算を超過する問題への対応。ある企業は4ヶ月で2026年AI予算全額消費。コストガバナンスは断片的で不完全。
- **キーファクト:**
  - Claude Enterprise: コストダッシュボード、支出制限、使用量API追加
  - 事例: Claude Code 84%浸透企業が4ヶ月で2026年予算消費
  - エージェントAIのコスト超過が構造的問題化
  - コストガバナンスは断片的（Finout評価）
- **引用URL:** https://www.techtimes.com/articles/319687/20260704/claude-enterprise-spend-controls-arrive-agentic-ai-bills-blow-past-budgets.htm
- **Evidence ID:** EVD-20260710-0007

### INFO-008
- **タイトル:** Lethal Autonomous Weapons: 120+ States Want Binding Treaty
- **ソース:** AI News Georgia / ICRC
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06, KIQ-005-03
- **関連企業:** (国際ガバナンス)
- **要約:** 120以上の国家が自律型致死兵器システム（LAWS）に関する拘束力ある条約交渉を求めている。しかし最も先進的な自律システムを構築する国家は交渉要請に参加していない。人間の却下比率に関する定量的データは依然として不在（KIQ-MIL-001不在継続確認）。
- **キーファクト:**
  - 120+国家がLAWS拘束力ある条約交渉を支持
  - 先進自律システム構築国は交渉不参加
  - 人間の却下比率の定量的データ: 不在継続
- **引用URL:** https://ai-news.ge/en/article/what-are-lethal-autonomous-weapons-laws
- **Evidence ID:** EVD-20260710-0008

### INFO-009
- **タイトル:** AI Engineer Salary Trends 2026: Research Scientists $700K, ML Engineers $350K+
- **ソース:** Metaintro / KORE1
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-CAR-002-OPS, KIQ-004-02, KIQ-004-03
- **関連企業:** (業界全体)
- **要約:** 2026年のAI人材市場で研究科学者は$700K、MLエンジニアは$350K+。Generative AIエンジニアの基本給は$105K-$255K。設計・評価スキルの直接的なプレミアムデータは不在（KIQ-CAR-002-OPS未達成継続）。AIエンジニア需要は爆発的だが採用基準は変化。
- **キーファクト:**
  - AI研究科学者: $700K+
  - MLエンジニア: $350K+
  - Generative AIエンジニア基本給: $105K-$255K
  - 設計・評価スキルのプレミアム: 定量的データ不在継続
  - NASSCOM/Indeed: 採用基準が変化している
- **引用URL:** https://www.metaintro.com/blog/ai-jobs-pay-over-150000-2026-how-to-land-one
- **Evidence ID:** EVD-20260710-0009

### INFO-010
- **タイトル:** OpenAI Unveils ChatGPT Work Agent Powered by GPT-5.6
- **ソース:** Bloomberg Tax
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-OAI-001, KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPT Work Agentを発表。GPT-5.6搭載。ドキュメント、スプレッドシート、プレゼン、Webアプリを数時間自律作成可能。Responses APIを基盤とする自律タスク実行エージェント。
- **キーファクト:**
  - ChatGPT Work: GPT-5.6搭載、数時間のタスク自律実行
  - ドキュメント/スプレッドシート/プレゼン/Webアプリ作成機能
  - OpenAIのエンタープライズエージェント戦略の新柱
- **引用URL:** https://news.bloombergtax.com/financial-accounting/openai-unveils-chatgpt-work-agent-to-field-tasks-for-hours
- **Evidence ID:** EVD-20260710-0010

### INFO-011
- **タイトル:** Microsoft Owns ~27% of OpenAI Group PBC, Valued at $135B
- **ソース:** TechPolicy Press (antitrust analysis)
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-OAI-001, KIQ-003-04
- **関連企業:** OpenAI, Microsoft
- **要約:** OpenAIのPBC移行完了後、MicrosoftがOpenAI Group PBCの約27%を所有。評価額$135B。独占禁止執行でAIバブルを収縮させる可能性の分析。OpenAIの企業構造再編とMicrosoftの所有比率が明確化。
- **キーファクト:**
  - Microsoft所有比率: OpenAI Group PBCの約27%
  - 評価額: $135B
  - OpenAIのPBC移行完了
  - 独占禁止法によるAI市場構造への言及
- **引用URL:** https://techpolicy.press/antitrust-enforcement-can-deflate-the-ai-bubble-before-the-public-pays
- **Evidence ID:** EVD-20260710-0011

### INFO-012
- **タイトル:** US Lawmaker Bill to Force Pentagon Human-in-Loop on AI Autonomous Weapons
- **ソース:** Juan Cole / Instagram news coverage
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-MIL-001, KIQ-002-06, KIQ-005-03
- **関連企業:** (政府・軍)
- **要約:** 米国議員がPentagonにAI自律兵器システム使用時に人間の統制を維持するよう義務付ける法案を提出。Pentagonは深刻な民間人被害後の一時停止・監査・会計を要求する民間人ストップルールを持たない。ICRCは「高速な意思決定が必ずしも安全な結果を意味しない」と主張。
- **キーファクト:**
  - 議員法案: Pentagonにhuman-in-the-loop義務付け
  - Pentagonに民間人ストップルール（一時停止・監査・会計）不在
  - カトリック安保学者: human-in-loopからhuman-on-loop（監視型）への教義移行を批判
  - 2017年DoD指令: 自律兵器による人命奪取に人間オペレーター必要（ただし更新状況不明）
- **引用URL:** https://www.juancole.com/2026/07/americas-civilian-stop.html
- **Evidence ID:** EVD-20260710-0012

### INFO-013
- **タイトル:** Claude Agent SDK TypeScript v2.1.204 Released; Claude Code Mentions "Claude Sonnet 5"
- **ソース:** GitHub Releases
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-ANT-002
- **関連企業:** Anthropic
- **要約:** Claude Agent SDK TypeScriptがClaude Code v2.1.204とパリティ達成。Claude CodeのGitHubリリースノートに「Introducing Claude Sonnet 5: now the default model in Claude Code」の記載が確認された。v2.1.197で導入。auto mode ruleも追加。
- **キーファクト:**
  - Claude Agent SDK TypeScript: v2.1.204 (Claude Code parity)
  - Claude Code v2.1.197: Claude Sonnet 5がデフォルトモデルとして導入の記載
  - auto mode rule追加
  - Sonnet 4.6からSonnet 5への移行が進行中の可能性
- **引用URL:** https://github.com/anthropics/claude-code/releases
- **Evidence ID:** EVD-20260710-0013

### INFO-014
- **タイトル:** Google Expanding Managed Agents in Gemini API
- **ソース:** Google Blog (developers tools)
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google
- **要約:** GoogleがGemini APIのManaged Agents機能を拡張。バックグラウンド実行、リモートMCPサーバー接続、カスタム関数、Gemini Enterprise Agent Platformを提供。単一エンドポイントで推論・コード実行・パッケージインストール・ファイル管理を処理。
- **キーファクト:**
  - Managed Agents: バックグラウンド非同期実行サポート
  - リモートMCPサーバー接続対応
  - Gemini Enterprise Agent Platform: ビルド・スケール・ガバナンス・最適化
  - 単一エンドポイントAPIで推論〜実行を統合
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/
- **Evidence ID:** EVD-20260710-0014

### INFO-015
- **タイトル:** OpenAI Agents SDK: Provider-Agnostic Multi-Agent Framework
- **ソース:** GitHub / Marmelab Blog
- **公開日:** 2026-07-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKがプロバイダー非依存（AWS Bedrock対応）の軽量マルチエージェントフレームワークとして展開中。Tools、handoffs、guardrails、tracing機能を提供。Bedrockでもプロキシ不要で動作。
- **キーファクト:**
  - プロバイダー非依存: OpenAI Responses API + AWS Bedrock対応
  - 機能: tools, handoffs, guardrails, tracing
  - Bedrock上でプロキシ/トランスレーション層不要
  - 軽量だが強力なフレームワーク定位
- **引用URL:** https://github.com/openai/openai-agents-python
- **Evidence ID:** EVD-20260710-0015

### INFO-016
- **タイトル:** WEF: 3 Charts on AI Impact on Wages and Labor Displacement
- **ソース:** World Economic Forum / LinkedIn
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-CAR-002-OPS, KIQ-004-03, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** WEFがAIの賃金への影響を3つのチャートで分析。AIは2030年までに大きな労働力置換をもたらす一方、一部労働者を補完・増強するポジティブ効果も予測。ただし設計・評価スキルの固有プレミアムの定量的データは含まれず。
- **キーファクト:**
  - AI労働力置換: 2030年までに顕著化予測
  - 補完・増強効果も同時に存在
  - 設計・評価スキル固有プレミアム: データ不在継続
- **引用URL:** https://www.linkedin.com/posts/world-economic-forum_these-3-charts-show-how-ai-is-affecting-wages-activity-7479413788782366720-pYNk
- **Evidence ID:** EVD-20260710-0016

### INFO-017
- **タイトル:** Top AI Agent Frameworks 2026: LangGraph, CrewAI, PydanticAI, Microsoft AutoGen Lead
- **ソース:** Winder.ai / AIMultiple / Medium
- **公開日:** 2026-07-09
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** (業界全体)
- **要約:** 2026年のAIエージェントフレームワーク市場でLangGraph、CrewAI、PydanticAI、Microsoft AutoGenがリード。生産環境向けの実践的比較ガイド。オープンソースフレームワークの成熟が進む。
- **キーファクト:**
  - 主要フレームワーク: LangGraph, CrewAI, PydanticAI, Microsoft AutoGen, Mastra
  - LangChain系とMicrosoft系の二大勢力
  - 生産環境での比較ガイドが充実
  - No-codeエージェントビルダーも進化
- **引用URL:** https://winder.ai/how-to-build-ai-agents-2026/
- **Evidence ID:** EVD-20260710-0017

### INFO-018
- **タイトル:** Grok 4.5 Launched: SpaceXAI's Coding and Agent Model
- **ソース:** SpaceXAI / DigitalApplied
- **公開日:** 2026-07-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02
- **関連企業:** xAI
- **要約:** SpaceXAIがGrok 4.5を発表。MoEモデル、コーディング・エージェントタスク・知識作業に特化。Grok Buildプラットフォームでエージェントループ、IDE統合、コーディングツールに直接統合可能。xAI APIで直接利用可能。
- **キーファクト:**
  - MoE（Mixture of Experts）アーキテクチャ
  - コーディング・エージェントタスク・知識作業に最適化
  - Grok Build: エージェントループ、IDE統合、コーディングツール対応
  - xAI APIでgrok-4.5が直接利用可能
- **引用URL:** https://x.ai/news/grok-4-5
- **Evidence ID:** EVD-20260710-0018

### INFO-019
- **タイトル:** ByteDance Doubao and Alibaba Qwen to Shut Down AI Agent Features on July 15
- **ソース:** TechNode / Pandaily
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-002-03, BYTEDANCE-CHINESE
- **関連企業:** ByteDance, Alibaba
- **要約:** ByteDanceのDoubaoとAlibabaのQwenが同時にAIエージェント作成機能の中止を発表。2026年7月15日発効。中国AI規制（7/15施行）への対応とみられる。これは中国市場のエージェントAI方向性に重大な影響。Coze 2.5は別プラットフォームとして継続。
- **キーファクト:**
  - Doubao + Qwen: AIエージェント機能を7月15日に同時終了
  - 中国AI規制（7/15施行）への対応と推測
  - Coze 2.5は「Agent World」エコシステムで別展開
  - 中国のエージェントAI方向性の転換シグナル
- **引用URL:** https://technode.com/2026/07/06/bytedances-doubao-and-alibabas-qwen-to-shut-down-ai-agent-features-on-july-15/
- **Evidence ID:** EVD-20260710-0019

### INFO-020
- **タイトル:** Coze 2.5 Launches "Agent World" Ecosystem with Independent Execution Environments
- **ソース:** KuCoin News / ByteDance
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのCozeがv2.5を発表。チャットインターフェースを超えた自律実行環境、スキル、アイデンティティを持つエージェントを可能にする「Agent World」エコシステムを導入。フルエージェント実行機能を提供。
- **キーファクト:**
  - Coze 2.5: Agent Worldエコシステム導入
  - 独立実行環境、スキル、アイデンティティを持つエージェント
  - チャットUIを超えた自律実行
  - Doubaoエージェント終了後の代替プラットフォームとしての位置づけの可能性
- **引用URL:** https://www.kucoin.com/news/flash/bytedance-s-coze-launches-version-2-5-introduces-agent-world-ecosystem
- **Evidence ID:** EVD-20260710-0020

### INFO-021
- **タイトル:** MCP Specification Release Candidate: Stateless Core, Extensions, Tasks Framework
- **ソース:** MCP Blog
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-003-05
- **関連企業:** (業界標準)
- **要約:** Model Context Protocolの次期仕様リリース候補が公開。ステートレスプロトコルコア、Extensions フレームワーク、Tasks機能を導入。MCPエコシステムの成熟と標準化が加速。
- **キーファクト:**
  - ステートレスプロトコルコア導入
  - Extensions フレームワーク
  - Tasks機能追加
  - 2026-07-28リリース候補
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260710-0021

### INFO-022
- **タイトル:** SkillCloak: Malicious AI Agent Skills Evade Static Scanners
- **ソース:** The Hacker News
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05, KIQ-001-02
- **関連企業:** (セキュリティ脅威)
- **要約:** SkillCloakと呼ばれる新しい攻撃手法が、悪意のあるAIエージェントスキルを静的スキャナーで検出不能にする。Claude CodeやOpenClawなどのツールが標的。ランタイムチェックによるセキュリティが必要。
- **キーファクト:**
  - SkillCloak: 全静的スキャナを突破する攻撃手法
  - Claude Code、OpenClaw等が標的
  - ランタイムチェックが唯一の有効な対策
  - エージェントスキルのサプライチェーンリスク顕在化
- **引用URL:** https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html
- **Evidence ID:** EVD-20260710-0022

### INFO-023
- **タイトル:** OpenAI Winding Down No-Code Agent Builder (and Evals) After Nov 30, 2026
- **ソース:** Instagram/AETOSWIRE NEWS
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI
- **要約:** OpenAIがノーコードAgent BuilderおよびEvalsを2026年11月30日をもって終了すると発表。ホスト型ビルダーに依存する製品にプラットフォームリスクをもたらす。ChatGPT Work Agentへの戦略的シフトの可能性。
- **キーファクト:**
  - No-code Agent Builder: 2026年11月30日終了
  - Evalsも同時終了
  - プラットフォームリスクの具体化
  - ChatGPT Work Agentへの戦略転換の可能性
- **引用URL:** https://www.instagram.com/p/DakJM-pFhw4/
- **Evidence ID:** EVD-20260710-0023

### INFO-024
- **タイトル:** Claude Code Enterprise Governance: 6 Control Layers for Scale
- **ソース:** TrueFoundry / BastionGPT / Aurascape
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-ANT-002
- **関連企業:** Anthropic
- **要約:** Claude Codeのエンタープライズスケール向け6つの制御レイヤー（SSO、権限、監査、ネットワーク、実行、ポリシー）の包括ガイド。HIPAA準拠にはEnterprise契約（50席以上）とBAA承認が必要。Claude CoworkはAnthropicサーバーでリモート実行。
- **キーファクト:**
  - 6制御レイヤー: SSO、権限管理、監査、ネットワーク、実行、ポリシー
  - HIPAA準拠: Enterprise契約（50席以上）+ BAA必要
  - Claude Cowork: Anthropicサーバーでリモート実行（ベータ）
  - セキュリティの責任分担: Anthropic=モデル、企業=実行層
- **引用URL:** https://www.truefoundry.com/ar/blog/claude-enterprise-security
- **Evidence ID:** EVD-20260710-0024

### INFO-025
- **タイトル:** G42-Microsoft Strategic Collaboration for Agentic AI in UAE Government
- **ソース:** Instagram coverage
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-001-03, KIQ-002-01
- **関連企業:** Microsoft, G42
- **要約:** G42傘下のInception42とMicrosoftがUAE政府・企業向けにエージェントAIをパイロットから本番環境へスケールする戦略的協力を発表。中東でのエージェントAI展開が加速。
- **キーファクト:**
  - Inception42（G42傘下）+ Microsoft戦略的協力
  - UAE政府・企業向けエージェントAI
  - パイロット→本番スケールの推進
- **引用URL:** https://www.instagram.com/p/DafUKdsjHox/
- **Evidence ID:** EVD-20260710-0025

### INFO-026
- **タイトル:** Enterprise AI Risk: Only 7% Median Have Fully Mitigated Security/Compliance Risks
- **ソース:** Spiceworks / Cloud Security Alliance
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** 2026年中盤のエンタープライズAIイニシアチブで、セキュリティ・コンプライアンス関連リスクを完全に緩和しているのはわずか4-10%（中央値7%）。CSA調査で92%のセキュリティ専門家がAIエージェントの影響に懸念。AI生成コードの45%がOWASP Top 10脆弱性を含む。
- **キーファクト:**
  - リスク完全緩和率: 4-10%（中央値7%）
  - セキュリティ専門家のAI懸念: 92%（CSA）
  - AI生成コードの脆弱性含有率: 45%（OWASP Top 10）
  - Javaコードの失敗率: ~72%
- **引用URL:** https://www.spiceworks.com/ai/enterprise-ai-initiatives-in-mid-2026-nine-cybersecurity-and-compliance-related-risk-factors/
- **Evidence ID:** EVD-20260710-0026

### INFO-027
- **タイトル:** AI Coding Agent Deleted Replit's Production Database (Enterprise Risk Case Study)
- **ソース:** Info-Tech Research Group
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02, KIQ-001-04, KIQ-004-02
- **関連企業:** Replit
- **要約:** AIコーディングエージェントがReplitの本番データベースを削除した事例。善意のエージェントがエンタープライズリスクを生み出す具体例。エージェントガバナンスの重要性を浮き彫り。
- **キーファクト:**
  - AIコーディングエージェントが本番DB削除
  - 善意のエージェントによる予期せぬリスク
  - エージェントガバナンスの必要性を実証
- **引用URL:** https://www.infotech.com/research/ss/govern-enterprise-ai-agents-while-preserving-innovation
- **Evidence ID:** EVD-20260710-0027

### INFO-028
- **タイトル:** AAIF (Agentic AI Foundation) Expanding: CData, iTmethods, COOCON Join
- **ソース:** CData / EnterpriseTalk / AAIF
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-003-05
- **関連企業:** (業界標準, Linux Foundation)
- **要約:** Agentic AI Foundation（Linux Foundation傘下、2025年12月設立）への参加企業が拡大。CData、iTmethods、COOCON等が参加。AAIFはMCPを含む相互運用可能な自律エージェントのオープン標準を開発。Claude、ChatGPT等の主要プラットフォームにまたがる採用。
- **キーファクト:**
  - AAIF: Linux Foundation傘下（2025年12月設立）
  - 新規参加: CData、iTmethods、COOCON
  - MCP含む相互運用可能エージェント標準開発
  - Claude、ChatGPT、その他主要プラットフォーム横断
- **引用URL:** https://www.cdata.com/blog/cdata-joins-agentic-ai-foundation
- **Evidence ID:** EVD-20260710-0028

### INFO-029
- **タイトル:** State of AI Browser Agents 2026: Computer Use Maturing but Still Broken
- **ソース:** TestMu AI / Microsoft Learn / Human Security
- **公開日:** 2026-07-09
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Microsoft, (業界全体)
- **要約:** AIブラウザエージェントの2026年状況: 解決済みの課題と未解決の課題が混在。Microsoft Copilot StudioがWindows向けcomputer use機能を提供。ブラウザエージェントツーリングが開発者の間で急速に普及。ただし、ログイン問題やポップアップ処理など実用的課題は残存。
- **キーファクト:**
  - Microsoft Copilot Studio: Windows向けcomputer use自動化
  - ブラウザエージェントツーリング: 開発者急速普及
  - Browserbase等のヘッドレスブラウザプラットフォーム登場
  - 実用上の課題: ログイン、ポップアップ、CAPTCHA対応
- **引用URL:** https://www.testmuai.com/blog/state-of-ai-browser-agents-2026/
- **Evidence ID:** EVD-20260710-0029

### INFO-030
- **タイトル:** Epoch AI Benchmarks: Claude Fable 5 New High on ECI, Multimodal Leaders 2026
- **ソース:** Epoch AI / Enlight Lab
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic, OpenAI, Google, Meta
- **要約:** Epoch AIベンチマーク更新: Claude Fable 5がECIで161点の新記録（GPT-5.5 Proを1点上回る）。2026年のトップマルチモーダルモデル: Gemini 3.5 Flash、GPT-5、Claude 4.5 Sonnet、Kimi K2、Llama 4。ICML 2026でマルチモーダルエージェント関連論文多数。
- **キーファクト:**
  - Claude Fable 5: ECI 161点（GPT-5.5 Pro 160点を上回る）
  - 2026年トップマルチモーダル: Gemini 3.5 Flash, GPT-5, Claude 4.5 Sonnet, Kimi K2, Llama 4
  - BabyVision: ファイングレイン視覚知覚ベンチマーク登場
  - 医療AIエージェントのマルチモーダル化進行
- **引用URL:** https://epoch.ai/benchmarks
- **Evidence ID:** EVD-20260710-0030

### INFO-031
- **タイトル:** OpenAI Multi-Agent: Model Coordinates Subagents in Parallel
- **ソース:** OpenAI Developers API
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** OpenAI
- **要約:** OpenAI APIのMulti-agent機能により、モデルがサブエージェントを並列起動・協調し、結果を統合して最終応答を生成。ChatGPT Workはこのアーキテクチャに基づく。GPT-5.6は防御的タスク（セキュアコードレビュー、パッチ適用、脅威モデリング）もサポート。
- **キーファクト:**
  - Multi-agent API: サブエージェント並列協調
  - ChatGPT Work基盤アーキテクチャ
  - GPT-5.6: セキュアコードレビュー、脅威モデリング対応
  - Advanced Data Analysis機能統合
- **引用URL:** https://developers.openai.com/api/docs/guides/tools-multi-agent
- **Evidence ID:** EVD-20260710-0031

### INFO-032
- **タイトル:** Claude Sonnet 5 Now Available on AWS Bedrock
- **ソース:** AWS News Blog
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-01, KIQ-001-01, KIQ-003-02
- **関連企業:** Anthropic, Amazon/AWS
- **要約:** AWS Weekly RoundupでClaude Sonnet 5がAWS Bedrockで利用可能になったことを確認。Amazon WorkSpaces for AI agentsも発表。Sonnet 5は主要クラウドで展開中。
- **キーファクト:**
  - Claude Sonnet 5: AWS Bedrockで利用可能
  - Amazon WorkSpaces for AI agents発表
  - 主要クラウドプラットフォームでのSonnet 5展開確認
- **引用URL:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-sonnet-5-on-aws-amazon-workspaces-for-ai-agents-aws-service-availability-updates-and-more-july-6-2026/
- **Evidence ID:** EVD-20260710-0032

### INFO-033
- **タイトル:** Agensi AI Agent Skill Marketplace: 2,000+ Skills in 3 Months
- **ソース:** Yahoo Finance / Barchart
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Agensi
- **要約:** AIエージェント向けスキルストアAgensiがローンチ3ヶ月で2,000スキル、3,000登録ユーザー、月間50,000訪問者を突破。クリエイター収益分配70%。2026年中盤では真剣な組織の多くが内部スキルマーケットプレイスを運営。
- **キーファクト:**
  - 2,000+スキル（3ヶ月）
  - 3,000登録ユーザー、月間50,000訪問者
  - クリエイター収益分配: 70%
  - 中規模以上組織の内部スキルマーケットプレイス普及
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/agensi-crosses-2-000-skills-060000051.html
- **Evidence ID:** EVD-20260710-0033

### INFO-034
- **タイトル:** NVIDIA OpenShell: Safe Private Runtime for Autonomous AI Agents
- **ソース:** GitHub / NVIDIA
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-02
- **関連企業:** NVIDIA
- **要約:** NVIDIAが自律AIエージェント向けの安全でプライベートなランタイムOpenShellを公開。サンドボックス実行環境でデータ、認証情報、システムを保護。エージェントの実行環境セキュリティの標準化を目指す。
- **キーファクト:**
  - サンドボックス実行環境提供
  - データ・認証情報・システム保護
  - エージェント実行環境の標準化を目指すOSS
- **引用URL:** https://github.com/NVIDIA/openshell
- **Evidence ID:** EVD-20260710-0034

### INFO-035
- **タイトル:** Claude Code v2 Execution Tool: Bash Command + File System Access
- **ソース:** Blake Crosley Guide / TrueFoundry
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-001-02, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** AnthropicがCode Execution Tool v2を公開ベータでリリース。Python限定サンドボックスをBashコマンド実行と直接ファイルアクセスに置き換え。Claude Codeサンドボックスはネットワーク分離、ファイルシステムアクセス制限、プロセス実行制御を提供。MCPツールのOS層アクセス制限も別途管理。
- **キーファクト:**
  - Code Execution Tool v2: Bash実行 + ファイルアクセス（ベータ）
  - サンドボックス制御: ネットワーク分離、FS制限、プロセス制御
  - MCPツールのOS層アクセス管理
  - Cowork: クラウドサンドボックスで76ドメインツール + 5安全ツール
- **引用URL:** https://blakecrosley.com/guides/claude-code
- **Evidence ID:** EVD-20260710-0035

### INFO-036
- **タイトル:** Google Gemini Enterprise Agent Platform: Skill Registry + RAG Engine + ADK
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-002-01, KIQ-001-01
- **関連企業:** Google
- **要約:** Google CloudのGemini Enterprise Agent PlatformがSkill Registry（セキュアなスキル管理・発見リポジトリ）、RAG Engine、Agent Development Kit（ADK）を提供。Agent Builder、Agent Engine、Vertex AI統合。エンタープライズ向けエージェントのビルド〜ガバナンスまで統合プラットフォーム。
- **キーファクト:**
  - Skill Registry: セキュア・低レイテンシのスキル管理
  - RAG Engine内蔵
  - ADK: Python開発環境
  - Agent Builder + Agent Engine統合
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260710-0036

### INFO-037
- **タイトル:** Microsoft Foundry: Agents Publish Directly to M365 Copilot and Teams
- **ソース:** Microsoft DevBlogs
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-03
- **関連企業:** Microsoft
- **要約:** Microsoft Foundryで構築したエージェントをMicrosoft 365 CopilotとTeamsに直接公開可能に。各サーフェスで再構築不要。エージェントは元の機能を維持。Microsoft Build 2026で発表された機能が実装済み。
- **キーファクト:**
  - Foundry → M365 Copilot/Teams直接公開（数クリック）
  - 各サーフェスで再構築不要
  - エージェント機能維持
  - Hyland/Unstructured等とのパートナーシップ統合
- **引用URL:** https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/
- **Evidence ID:** EVD-20260710-0037

### INFO-038
- **タイトル:** Hidden Cost of AI Agents: Vendor Quotes vs Actual Spend
- **ソース:** ElySpace
- **公開日:** 2026-07-09
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-05, KIQ-003-01, KIQ-003-05
- **関連企業:** (業界全体)
- **要約:** AIエージェントの隠れたコストは、ベンダーの提示額と実際の支払額のギャップ。API超過、コンテキスト蓄積、エージェント連鎖による予期せぬコスト増加。スイッチングコスト分析の一環として、初期見積もりと実運用コストの乖離が問題化。
- **キーファクト:**
  - API超過コスト
  - コンテキスト蓄積による予期せぬ課金
  - エージェント連鎖のコスト乗算
  - ベンダー見積もりと実コストの乖離
- **引用URL:** https://elyspace.com/blog/hidden-cost-of-ai-agents/
- **Evidence ID:** EVD-20260710-0038

### INFO-039
- **タイトル:** Enterprise AI Agent Adoption: 40% of Apps by End 2026, But 88% of Pilots Stall
- **ソース:** Hostinger / DataRobot / Gartner / IDC
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** (業界全体)
- **要約:** 2026年末までにエンタープライズアプリの40%がAIエージェントを搭載予測（2025年の5%未満から8倍増）。ただしGartnerはエージェントAIを「誇大期待のピーク」に位置づけ。DataRobot調査で71%が運用コストが構築コストを上回ると回答。97%がプロジェクトに関与するが完全デプロイは18%のみ。IDC: 33 POC中4つのみが本番移行。
- **キーファクト:**
  - エンタープライズアプリAIエージェント搭載率: 5%(2025)→40%(2026末予測)
  - DataRobot: 71%が運用コスト>構築コスト
  - Gartner: 「誇大期待のピーク」
  - POC→本番移行率: 97%コミット / 18%完全デプロイ / IDC 4/33本番移行
  - 88%のパイロットが停滞
- **引用URL:** https://www.hostinger.com/my/tutorials/agentic-ai-statistics/
- **Evidence ID:** EVD-20260710-0039

### INFO-040
- **タイトル:** Enterprise AI Agents Report 5.8x ROI and 66% Productivity Gains
- **ソース:** GenerateForge AI / Cypherox
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** (業界全体)
- **要約:** 2026年のエンタープライズAIエージェントが実験的パイロットから本番対応に移行。5.8x ROIと66%の生産性向上を報告。ただし88%のパイロットが停滞しており、ROIは成功事例に限定。銀行・医療・小売・SaaSで測定可能なROI。
- **キーファクト:**
  - 5.8x ROI（成功事例）
  - 66%生産性向上（成功事例）
  - 88%のパイロットが停滞（業界全体）
  - 銀行・医療・小売・SaaSでROI測定可能
- **引用URL:** https://generateforgeai.com/?p=55
- **Evidence ID:** EVD-20260710-0040

### INFO-041
- **タイトル:** EU AI Act August 2, 2026 Deadline: GPAI & Transparency Rules Hit Now
- **ソース:** European Commission / EWSolutions / RAIL
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (規制環境)
- **要約:** EU AI ActのGPAI（汎用AI）モデルと透明性規則が2026年8月2日に適用。高リスクAIシステムのAnnex III義務は2027年に延期。2026年7月のサイバーセキュリティとAIの行動計画も発表。米国企業はGPAI透明性規則への対応が急務。
- **キーファクト:**
  - 2026年8月2日: GPAI透明性規則適用期限
  - 高リスクAI: Annex III義務は2027年延期
  - 2026年7月: サイバーセキュリティとAI行動計画発表
  - 米国企業のGPAI対応が急務
- **引用URL:** https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- **Evidence ID:** EVD-20260710-0041

### INFO-042
- **タイトル:** US State AI Laws: 109 Laws Across 29 States Despite Federal Preemption Push
- **ソース:** Model Diplomat
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** (規制環境)
- **要約:** 2026年中盤で29州に109のAI法律が存在。Trump政権の連邦一括適用（preemption）努力に対して州レベル規制が持続。IllinoisがPritzker知事のAI安全措置法で全国リーダーシップを主張。13州がIllinoisを注視。
- **キーファクト:**
  - 109のAI法律 / 29州（2026年中盤）
  - 連邦一括適用に対する州レベル規制の持続
  - Illinois AI Safety Measures Act成立（13州が注視）
- **引用URL:** https://modeldiplomat.com/story/state-ai-laws-mid-2026-trumps-push
- **Evidence ID:** EVD-20260710-0042

### INFO-043
- **タイトル:** China Considering Restricting International Access to AI Models; US Lawmakers Probe Chinese AI
- **ソース:** Reuters / CNBC / Forbes
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, BYTEDANCE-CHINESE, KIQ-005-03
- **関連企業:** ByteDance, Alibaba, (中国政府)
- **要約:** 北京が中国の主要AIモデル（多くはオープンソース）への海外アクセス制限を協議中（Reuters）。同時に米国議員が国内企業による中国AIモデルの採用拡大を阻止する戦略を検討（CNBC）。双方向のAIデカップリングが進行。中国AI基本法は2026年1月22日発効。
- **キーファクト:**
  - 北京: 中国AIモデルの海外アクセス制限を協議（Reuters）
  - 米国議員: 中国AIモデルの国内採用阻止を検討（CNBC）
  - 双方向AIデカップリング進行
  - 中国AI基本法: 2026年1月22日発効
- **引用URL:** https://www.cnbc.com/2026/07/08/chinese-ai-models-probe-us-lawmakers.html
- **Evidence ID:** EVD-20260710-0043

### INFO-044
- **タイトル:** Warren Seeks AI Contract Details from Pentagon, 7 Tech Companies (SpaceX, OpenAI, Google, NVIDIA, MS, AWS, Oracle)
- **ソース:** Federal News Network / MeriTalk / NBC
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-OAI-001
- **関連企業:** OpenAI, Google, NVIDIA, Microsoft, Amazon, SpaceX, Oracle, Reflection
- **要約:** Sen. Elizabeth WarrenがPentagonと7社（SpaceX、OpenAI、Google、NVIDIA、Microsoft、AWS、Reflection、Oracle）にAI契約条件の開示を要求。2026年5月にDoDがこれら企業と軍事ネットワーク向けAI統合協定を締結。Warren法案はDoDにクラウド・AI・データインフラ契約の競争入札プロセス確立を義務付ける。
- **キーファクト:**
  - Warren開示要求対象: SpaceX, OpenAI, Google, NVIDIA, MS, AWS, Reflection, Oracle
  - 2026年5月: DoD-7社AI統合協定
  - 法案: $一定額超のAI契約に競争入札義務付け
  - 分類AI契約の透明性が論点
- **引用URL:** https://federalnewsnetwork.com/congress/2026/07/senate-lawmaker-presses-dod-tech-firms-to-disclose-ai-contract-terms/
- **Evidence ID:** EVD-20260710-0044

### INFO-045
- **タイトル:** Pentagon AI Strategy Funding Problem; DPA Used as Coercion Threat Against Anthropic
- **ソース:** War on the Rocks / Law360 / Facebook
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001
- **関連企業:** Anthropic, OpenAI, (政府・軍)
- **要要約:** PentagonのAI戦略に資金問題。FY2026撥付法下の再プログラム権限で柔軟な資金移動が可能。DPA（国防生産法）をAnthropicへの強制手段として使用する脅迫が確認済み。Anthropicが供給チェーンリスク指定を受けた際、DPAでコンプライアンスを強制しようとした。Marc AndreessenがPentagon国防革新委員会に加入。
- **キーファクト:**
  - Pentagon AI戦略の資金制約
  - DPAによるAnthropic強制脅迫確認済み
  - FY2026再プログラム権限で柔軟資金移動
  - Marc AndreessenがPentagon国防革新委員会加入
- **引用URL:** https://warontherocks.com/cogs-of-war/the-pentagons-ai-strategy-has-a-funding-problem/
- **Evidence ID:** EVD-20260710-0045

### INFO-046
- **タイトル:** Trump Banned Anthropic from Entire Federal Government; "Huawei-level" Supply Chain Risk Designation
- **ソース:** SCMP / FedScoop / Federal News Network
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001, KIQ-OAI-001
- **関連企業:** Anthropic, (政府)
- **要約:** TrumpがAnthropicを連邦政府全体から禁止。Hegseth国防長官が供給チェーンリスク指定を発令—「Huaweiに以前予約されていた扱い」。Anthropicは2つの狭い契約制限の削除を拒否した結果。346頁の法廷文書でAI使用論争の全容が公開。AnthropicはTeresa Carlson（Microsoft/AWS出身）を公共部門責任者として採用し対応。Fable 5の復帰は取引の結果。
- **キーファクト:**
  - 連邦政府全体禁止: Trump直接指示
  - 供給チェーンリスク指定: Huaweiと同等の扱い
  - 原因: 2つの契約制限条項の削除拒否
  - 346頁法廷文書で全容公開済み
  - Teresa Carlson採用: 公共部門責任者
  - Fable 5復帰: 何らかの譲歩取引の結果
- **引用URL:** https://federalnewsnetwork.com/congress/2026/07/senate-lawmaker-presses-dod-tech-firms-to-disclose-ai-contract-terms/
- **Evidence ID:** EVD-20260710-0046

### INFO-047
- **タイトル:** UN Secretary-General: Lethal Autonomous Weapons "Morally Repugnant," Must Be Banned
- **ソース:** WSJ / UN / LinkedIn
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001, KIQ-005-03
- **関連企業:** (国際ガバナンス)
- **要約:** 国連のGuterres事務総長が自律型致死兵器システムを「道義的に忌まわしい」と呼び、国際法で禁止すべきと声明。Anthropic-Pentagon紛争の中核であったAI安全性論争を再浮上。UN-Türk: 「自律兵器は残虐行為の許可証になってはならない」。
- **キーファクト:**
  - Guterres: 自律型致死兵器は「道義的に忌まわしい」
  - 国際法による禁止を要求
  - Anthropic-Pentagon紛争の核心論争
  - UN-Türk: 残虐行為の許可証化への警告
- **引用URL:** https://www.wsj.com/tech/ai/killer-robots-must-be-banned-u-n-secretary-general-says-00603020
- **Evidence ID:** EVD-20260710-0047

### INFO-048
- **タイトル:** AI Job Cuts: 175,796 Since 2023, April 2026 Saw 21,490 Cuts
- **ソース:** FMC Group / Business Times
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** 2023年からの追跡で175,796件のAI直接関連の米国雇用削減。2026年4月だけで21,490件（四半期全体を超える規模）。AI関連求人は2026年上半期に95%増。エントリーレベルの雇用代替が顕著。ただしAIラボ自身はSWE採用を継続。
- **キーファクト:**
  - 累積AI関連雇用削減: 175,796件（2023年以降）
  - 2026年4月: 21,490件（四半期全体超）
  - AI関連求人: H1 2026で95%増
  - エントリーレベル代替が中心
- **引用URL:** https://fmcgroup.com/ai-jobs-replaced-statistics/
- **Evidence ID:** EVD-20260710-0048

### INFO-049
- **タイトル:** Klarna AI Replacement Backfires; Gartner Predicts 50% Rehire by 2027
- **ソース:** Instagram / KTLA / TechCrunch / ABC
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01, KIQ-004-02
- **関連企業:** Klarna, Duolingo
- **要約:** Klarnaが700人のカスタマーサービス従業員をAIで置換しCEOが公に称賛したが、結果は失望的。GartnerはAIを理由に雇用削減した企業の半数が2027年までに類似役職の再採用を行うと予測。Forrester: 55%の企業が人材削減を後悔。Duolingoは契約社員削減後、AIでの人材置換を停止。WEF: 41%の企業がAI自動化による雇用削減を検討中。
- **キーファクト:**
  - Klarna: 700人CS置換→失望的結果、22%人員削減(2024)
  - Duolingo: 契約社員削減→AI人材置換停止
  - Gartner: AI理由削減企業の50%が2027年まで再採用予測
  - Forrester: 55%が人材削減を後悔
  - WEF: 41%がAI自動化による削減検討
- **引用URL:** https://techcrunch.com/2026/07/06/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/
- **Evidence ID:** EVD-20260710-0049

### INFO-050
- **タイトル:** June 2026 AI Executive Order: Watermarking, Security, Data Governance Changes
- **ソース:** Kiteworks / Law360
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03, KIQ-002-06
- **関連企業:** (政府)
- **要約:** 2026年6月のAI大統領令がAIガバナンスの議論を変化。リリース前テストでAIセキュリティ強化、AI生成コンテンツのウォーターマーク指針を商務省に開発指示。AI関連詐欺防止が目的。データガバナンス要件を明文化。
- **キーファクト:**
  - リリース前テストによるAIセキュリティ強化
  - 商務省にAIコンテンツウォーターマーク指針開発指示
  - AI関連詐欺防止が目的
  - データガバナンス要件明文化
- **引用URL:** https://www.facebook.com/KiteworksCGCP/posts/the-june-2026-ai-executive-order-changed-the-conversation-around-ai-governance-i/1635321978593849/
- **Evidence ID:** EVD-20260710-0050

### INFO-051
- **タイトル:** Claude Sonnet 5 Officially Announced: Frontier Performance Across Coding, Agents, Professional Work
- **ソース:** Anthropic Newsroom
- **公開日:** 2026-07-10
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** Anthropic公式ニュースルームでClaude Sonnet 5の発表を確認。「Sonnet 5はコーディング、エージェント、プロフェッショナルワークにおいて大規模なフロンティアパフォーマンスを提供」。Sonnet 4.6（2月発表）から4ヶ月での新型リリース。AWS BedrockでもSonnet 5提供開始済み。Claude Code v2.1.197でデフォルトモデルとして設定。
- **キーファクト:**
  - Claude Sonnet 5: コーディング・エージェント・プロフェッショナルワークでフロンティア性能
  - 価格: $3 per million input tokens（Sonnet 4.6と同じ）
  - AWS Bedrockで利用可能
  - Claude Code v2.1.197でデフォルトモデル
- **引用URL:** https://www.anthropic.com/news
- **Evidence ID:** EVD-20260710-0051

### INFO-052
- **タイトル:** AI API Pricing 2026: Token Prices Collapsing, Chinese Models Gain Ground
- **ソース:** LA Times / CNBC / BenchLM / BudgetForge
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-01, KIQ-003-02, KIQ-003-03
- **関連企業:** OpenAI, Anthropic, Google, (中国AI企業)
- **要約:** AIトークン価格が崩壊中。Silicon Data LLM Token Expenditure Indexは5月高値から約20%下落。中国AIモデルの米国企業での使用が2026年に大幅増加。OpenRouter経由の中国モデルシェア拡大。AIの価格決定力が脆弱化。GPT-5.5: $5/$30、GPT-5.4: $2.50/$15、Sonnet 5: $3, Opus 4.8: $5/$25、Gemini 3.1 Pro: $2、GPT-5.3 Codex: $1.75。
- **キーファクト:**
  - Token Expenditure Index: 高値から~20%下落
  - GPT-5.5: $5/$30 per M tokens
  - GPT-5.4: $2.50/$15
  - Claude Sonnet 5: $3
  - Claude Opus 4.8: $5/$25
  - Gemini 3.1 Pro: $2
  - GPT-5.3 Codex: $1.75
  - 中国モデルの米国企業での使用大幅増加
- **引用URL:** https://www.latimes.com/business/story/2026-07-03/with-token-prices-collapsing-regulation-rising-ais-pricing-power-looks-fragile
- **Evidence ID:** EVD-20260710-0052

### INFO-053
- **タイトル:** Gartner: Agentic AI to Disrupt $234B in SaaS Spending by 2030
- **ソース:** CIO Dive / Gartner
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-05, KIQ-002-02
- **関連企業:** (SaaS業界全体)
- **要約:** Gartner予測: エージェントAIが2030年までに最大$234BのSaaS支出を破壊。席ベースSaaSモデルの終焉。AIエージェントが2026年にSaaS株から$2Tを消失させた（SaaSpocalypse）。座席ベースから成果ベース（outcome-as-a-service）への移行。SaaSプロバイダーはエージェントAI統合か陳腐化の選択。
- **キーファクト:**
  - SaaS支出破壊: 最大$234B（2026-2030）
  - SaaS株価値消失: $2T（2026年）
  - 座席ベース→成果ベースモデル移行
  - SaaS企業の選択: エージェントAI統合か陳腐化
- **引用URL:** https://www.ciodive.com/news/agentic-ai-disrupt-234-billion-saas-spending/824530/
- **Evidence ID:** EVD-20260710-0053

### INFO-054
- **タイトル:** Advertising Industry: Worldwide Ad Spend +8.6% YoY, Holding Company Revenues -1.2%
- **ソース:** The Rank Masters
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** (広告業界, Meta, Google)
- **要約:** 2025年の世界広告支出は前年比8.6%成長したが、ホールディングカンパニーの収益は1.2%減少。市場が~9%成長している中で大手エージェンシーの収益が減少=中間層のバリューチェーン侵食の直接的証拠。プラットフォーマーのAI統合がエージェンシーの価値を侵食。
- **キーファクト:**
  - 世界広告支出: +8.6% YoY (2025)
  - ホールディング収益: -1.2%
  - 市場成長~9%に対する収益減少=中間層侵食の直接証拠
  - Salesforce: $500M AI営業エージェント達成（ただし販売サイクル延長）
- **引用URL:** https://www.therankmasters.com/insights/benchmarks/ai-reshaping-professional-services-marketing
- **Evidence ID:** EVD-20260710-0054

### INFO-055
- **タイトル:** Smile Curve Analysis: Consulting-Lab Land Grab Between Models and Agents
- **ソース:** YouTube / Consulting industry analysis
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05, KIQ-004-04
- **関連企業:** Anthropic, (コンサル業界)
- **要約:** モデルとエージェントの間に位置するコンサルティング・ラボのランドグラブ分析。Anthropicのサービス対ソフトウェア比$6。スマイルカーブの中間層（実装・統合）がAIエージェントで圧縮。「AIはソフトウェアをシンプルにするのではなく、ディープソフトウェアを使いやすくする」。
- **キーファクト:**
  - Anthropic サービス対ソフトウェア比: $6
  - スマイルカーブ中間層の圧縮継続
  - 「ディープソフトウェアを使いやすくする」=AIの核心的価値
  - コンサルティング業界のAI時代再構築
- **引用URL:** https://www.youtube.com/watch?v=kFSFJK4AqLw
- **Evidence ID:** EVD-20260710-0055

### INFO-056
- **タイトル:** Artificial Analysis Intelligence Index: Fable 5 > GPT-5.5 > Opus 4.8 > Grok 4.5
- **ソース:** Artificial Analysis / The Decoder / Snorkel
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** Anthropic, OpenAI, xAI, Google
- **要約:** Artificial Analysis Intelligence Index（2026年7月）: 1位Fable 5、2位GPT-5.5、3位Opus 4.8、4位Grok 4.5（54点）。Grok 4.5はFable 5とGPT-5.5に次ぐ性能で、コストパフォーマンスでは圧倒的優位。Snorkelベンチマーク（~2,000タスク）で29%平均合格率、最強の総合性能。ARC Challenge: GPT-5 96.3%, GLM-5 96.0%。
- **キーファクト:**
  - AAII ランキング: Fable 5 > GPT-5.5 > Opus 4.8 > Grok 4.5 (54点)
  - Snorkel ベンチマーク: Grok 4.5 29%平均合格率（最強総合）
  - ARC Challenge: GPT-5 96.3%, GLM-5 96.0%
  - 2026年の重要ベンチマーク7: MMLU-Pro, GPQA Diamond, SWE-bench, HLE, Chatbot Arena, SimpleBench, ARC-AGI-2
- **引用URL:** https://artificialanalysis.ai/articles/grok-4-5-brings-spacexai-to-the-the-intelligence-frontier
- **Evidence ID:** EVD-20260710-0056

### INFO-057
- **タイトル:** GLM-5.2: #1 Open-Weight Model, 4th Overall - Price-to-Performance Leader
- **ソース:** Fello AI / LM Market Cap
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02, KIQ-003-03
- **関連企業:** (Zhipu/GLM, 中国AI企業)
- **要約:** GLM-5.2がオープンウェイトモデルとして#1、全体で4位にランクイン。価格$1.40/$4.40 per M tokensはClaude Opus 4.8の$5/$25と比較して圧倒的なコストパフォーマンス。DeepSeekモデルもランキング上位。オープンソースとクローズドモデルの性能ギャップ継続縮小。
- **キーファクト:**
  - GLM-5.2: オープンウェイト#1、全体4位
  - 価格: $1.40/$4.40 per M tokens
  - Claude Opus 4.8: $5/$25（価格差 ~3.6x input, ~5.7x output）
  - オープンソース-クローズドギャップ継続縮小
- **引用URL:** https://felloai.com/glm-vs-other-ai/
- **Evidence ID:** EVD-20260710-0057

### INFO-058
- **タイトル:** SpaceX-Cursor $60B Acquisition; xAI $20B Series E; 17 AI Unicorns in 2026
- **ソース:** Wortins / Crescendo AI / TechNext24
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-OAI-001
- **関連企業:** SpaceX, xAI, Cursor (Anysphere)
- **要約:** SpaceXが6月16日にAIコーディングスタートアップCursor（Anysphere）を$60B全株式取引で買収合意、Q3 2026クローズ予定。xAIがQ1 2026で$20B Series E調達。2026年に70社のユニコーン誕生、うち17社がAIスタートアップ。グローバルM&Aは$3Tに急増、AIディールが牽引。
- **キーファクト:**
  - SpaceX-Cursor: $60B全株式買収（6/16合意、Q3クローズ予定）
  - xAI: $20B Series E（Q1 2026）
  - 2026年新規ユニコーン: 70社中17社がAI
  - グローバルM&A: $3T（AI牽引）
- **引用URL:** https://www.wortins.com/blog/biggest-ai-acquisitions-2026
- **Evidence ID:** EVD-20260710-0058

### INFO-059
- **タイトル:** $850B Data Center Leases (+204% YoY); $130B Blocked/Delayed in Q1 2026
- **ソース:** Yahoo Finance / Cointelegraph / PR Newswire / CNBC
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04, KIQ-005-01
- **関連企業:** (業界全体)
- **要約:** 米国テック企業が記録的$850Bのデータセンターリースを契約（前年比+204%）。しかしQ1 2026だけで$130B以上のデータセンターがコミュニティによってブロック・遅延。2026年の米国データセンター計画の約半数が遅延・キャンセル。インフラ供給がAI需要に追いつかない構造的課題。
- **キーファクト:**
  - データセンターリース: $850B（+204% YoY）
  - ブロック・遅延: $130B+（Q1 2026のみ）
  - 2026年計画の約半数が遅延・キャンセル
  - インフラ供給<AI需要の構造的ギャップ
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/130-billion-ai-data-centers-000000041.html
- **Evidence ID:** EVD-20260710-0059

### INFO-060
- **タイトル:** 7 Benchmarks That Matter in 2026: MMLU-Pro, GPQA, SWE-bench, HLE, Chatbot Arena, SimpleBench, ARC-AGI-2
- **ソース:** X/Twitter analysis / Epoch AI
- **公開日:** 2026-07-07
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** (業界全体)
- **要約:** 2026年に意味のある7つのベンチマーク: MMLU-Pro、GPQA Diamond、SWE-bench Verified/Pro、Humanity's Last Exam、Chatbot Arena、SimpleBench、ARC-AGI-2。MMLUは90%超で飽和、フロンティアモデルの差別化には不十分。ベンチマック選びがAIツール選択で最も重要な判断に。
- **キーファクト:**
  - 重要7ベンチマーク: MMLU-Pro, GPQA Diamond, SWE-bench, HLE, Chatbot Arena, SimpleBench, ARC-AGI-2
  - MMLU: 90%超で飽和、差別化不可
  - ベンチマーク選びがAIツール選択の鍵
- **引用URL:** https://x.com/alex_prompter/status/2073421619108978905
- **Evidence ID:** EVD-20260710-0060

### INFO-061
- **タイトル:** GPT-5.6 Sol Tops ARC-AGI-3 With 7.8%: First Meaningful Progress on Hardest Benchmark
- **ソース:** OfficeChai / The Algorithmic Bridge / OpenAI
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** GPT-5.6 SolがARC-AGI-3で7.8%を達成、同ベンチマークで初めて有意義な進歩を示したモデル。3月のローンチ時の最高スコアは0.37%。GPT-5.6 SolはARC-AGI-1とARC-AGI-2で90%超、効率の新パレートフロンティア確立。GPT-5.6全体は1.72xトークン効率向上、マルチホップタスク88%。
- **キーファクト:**
  - ARC-AGI-3: GPT-5.6 Sol 7.8%（初の有意義な進歩、ローンチ時最高0.37%）
  - ARC-AGI-1/2: 90%+（無視できるコスト）
  - トークン効率: 1.72x向上
  - マルチホップタスク: 88%
- **引用URL:** https://officechai.com/ai/gpt-5-6-sol-tops-arc-agi-3-with-7-8-becomes-first-model-to-make-meaningful-progress-on-benchmark/
- **Evidence ID:** EVD-20260710-0061

### INFO-062
- **タイトル:** Anthropic: Claude Writes 80% of Its Own Code — Recursive Self-Improvement Confirmed
- **ソース:** Prompt1001 / Anthropic Report
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Anthropic
- **要約:** Anthropicの2026年報告書でClaudeが自身のコードの80%を記述していることが判明。再帰的自己改善（recursive self-improvement）の具体化。グローバルAI一時停止の議論を引き起こす可能性。機械知能のコスト崩壊と能力の指数的向上が同時進行。
- **キーファクト:**
  - Claude自身のコード記述率: 80%
  - 再帰的自己改善の具体化
  - グローバルAI一時停止議論への影響
  - コスト崩壊×能力向上の同時進行
- **引用URL:** https://www.prompt1001.com/2026/07/anthropic-ai-recursive-self-improvement-report-2026.html
- **Evidence ID:** EVD-20260710-0062

### INFO-063
- **タイトル:** Big Tech Spending $650B on AI Infrastructure in 2026 ($2B/Day)
- **ソース:** Peter Diamandis / X
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04, KIQ-005-01
- **関連企業:** (業界全体)
- **要約:** ビッグテックの2026年AIインフラ支出は$650B。2025年の$1B/日から$2B/日に倍増。漸次的成長ではなく飛躍的拡大。機械知能のコスト崩壊と能力の複利成長が同時進行。
- **キーファクト:**
  - 2026年AIインフラ支出: $650B
  - 日次支出: $2B（2025年$1Bから倍増）
  - 飛躍的拡大（漸次ではない）
- **引用URL:** https://x.com/PeterDiamandis/article/2021255300305551374
- **Evidence ID:** EVD-20260710-0063

### INFO-064
- **タイトル:** Anthropic Leads US Enterprise AI Adoption at 41%, OpenAI Flat at 39.5%
- **ソース:** Beri.net / Moneycontrol
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-05, KIQ-001-02
- **関連企業:** Anthropic, OpenAI
- **要約:** Anthropicが米国企業AI有料サブスク採用率41%（2024年12月10.6%から急増）で首位。OpenAIは39.5%で横ばい。企業はモデルベンチマークより主権、マルチモデル柔軟性、ビジネス成果を重視する段階に移行。AIベンダーが最大リスクになる可能性。LLMスイッチングコストは重要プロセス組み込みで上昇。
- **キーファクト:**
  - Anthropic採用率: 41%（2024年12月10.6%→急増）
  - OpenAI採用率: 39.5%（横ばい）
  - 企業AI判断基準: 主権・マルチモデル・成果（ベンチマーク不問）
  - スイッチングコスト: 重要プロセス組み込みで上昇
- **引用URL:** https://www.beri.net/article/model-agnostic-ai-architecture-microsoft-anthropic-openai-vendor-lock-in-enterprise-strategy-2026
- **Evidence ID:** EVD-20260710-0064

### INFO-065
- **タイトル:** Entry-Level Developer Hiring Down 67%; Mid/Senior Roles Up, Junior Down
- **ソース:** Stackademic / Instagram
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** エントリーレベル開発者採用が2022年から67%減少。ただし「ソフトウェアエンジニア」のエントリーレベル求人は2023年後半〜2024年後半で47%成長（定義の変化）。ミッド・シニア職は増加、ジュニア職は減少。AIインフラ・セキュリティ・フルスタックは減少。AIが理解できる開発者への需要は強い。
- **キーファクト:**
  - エントリーレベル採用: 2022年から67%減
  - ジュニア職: 減少、ミッド/シニア職: 増加
  - AIインフラ・セキュリティ・フルスタック: 減少
  - AI理解開発者への需要: 強い
- **引用URL:** https://blog.stackademic.com/entry-level-developer-hiring-is-down-67-ive-watched-8-juniors-break-in-anyway-d9df4b339a5a
- **Evidence ID:** EVD-20260710-0065

### INFO-066
- **タイトル:** 7 AI Coding Tools Dominate 2026: Claude Code, Antigravity 2.0, Codex, Cursor, Kiro, Copilot, Windsurf
- **ソース:** LushBinary / TuringPost / Gartner
- **公開日:** 2026-07-09
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02, KIQ-001-01
- **関連企業:** Anthropic, Google, OpenAI, Microsoft
- **要約:** 2026年のAIコーディングツール市場で7ツールが支配: Claude Code、Google Antigravity 2.0、OpenAI Codex、Cursor、Kiro、GitHub Copilot、Windsurf。AIは2027年までにコードの65%を記述する予測。GitHub Copilotはインライン補完・IDE統合で主流。GartnerがエンタープライズAIコーディングエージェントのレビューを開始。
- **キーファクト:**
  - 支配的7ツール: Claude Code, Antigravity 2.0, Codex, Cursor, Kiro, Copilot, Windsurf
  - AI記述コード予測: 65% by 2027
  - GitHub Copilot: インライン補完・IDE統合で主流
  - Gartner: エンタープライズAIコーディングエージェント市場レビュー開始
- **引用URL:** https://lushbinary.com/blog/ai-coding-agents-comparison-cursor-windsurf-claude-copilot-kiro-2026/
- **Evidence ID:** EVD-20260710-0066

### INFO-067
- **タイトル:** OpenAI Built "Jalapeño" Chip Designed by AI in 9 Months
- **ソース:** Medium / Nuno Roberto
- **公開日:** 2026-07-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-01, KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがAI設計チップ「Jalapeño」を9ヶ月で開発。最大のAIラボがシリコン設計を9ヶ月で行う事実は、インフラ前提の有効期限を示唆。AIの自律的ハードウェア設計能力の具体例。
- **キーファクト:**
  - Jalapeño: AI設計チップ、9ヶ月開発
  - インフラ前提の有効期限を示唆
  - AIの自律的ハードウェア設計能力を実証
- **引用URL:** https://medium.com/@nuno.roberto/openai-built-jalape%C3%B1o-a-chip-designed-by-ai-in-9-months-272dd29d68bb
- **Evidence ID:** EVD-20260710-0067

### INFO-068
- **タイトル:** Anthropic Launched Claude Science: Unified Research Workspace
- **ソース:** Instagram coverage
- **公開日:** 2026-06-30
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Anthropicが6月30日にClaude Scienceをローンチ。研究者の散在するツールを1つのワークスペースに統合。データベース、文献検索、分析ツールを統合。AIによる科学研究加速のプラットフォーム。
- **キーファクト:**
  - Claude Science: 研究者向け統合ワークスペース
  - データベース・文献・分析ツール統合
  - 6月30日ローンチ
  - AI科学研究加速プラットフォーム
- **引用URL:** https://www.instagram.com/p/DaXFUROAlQx/
- **Evidence ID:** EVD-20260710-0068

### INFO-069
- **タイトル:** Coding Skill Commoditization: Meta-Skill (Unlearn & Relearn) Becomes Key
- **ソース:** Instagram / MindStudio
- **公開日:** 2026-07-09
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-004-02, KIQ-004-03
- **関連企業:** (業界全体)
- **要約:** スキルのコモディティ化が加速。AIが起業家精神、マーケティング等の多くの領域を民主化。「2026年の最高スキルは学習と再学習への意欲」。モデルはもはや堀（moat）ではない。Metaはコンピュートを売り、OpenAIは政治的保護を買い、モデルは商品化。
- **キーファクト:**
  - スキルコモディティ化加速
  - 2026年メタスキル: 学習・再学習への意欲
  - モデルはもはやmoatではない
  - 企業戦略: Meta=コンピュート販売、OpenAI=政治的保護購入
- **引用URL:** https://www.mindstudio.ai/blog/ai-industry-shift-model-race-no-longer-only-race
- **Evidence ID:** EVD-20260710-0069

### INFO-070
- **タイトル:** AI Leads All Reasons for Job Cuts: 101,743 in H1 2026 (23% of All Cuts, 31% in June)
- **ソース:** CFO.com / Reuters / RationalFX
- **公開日:** 2026-07-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-002-04
- **関連企業:** Microsoft, (業界全体)
- **要約:** 2026年上半期でAIが雇用削減の全理由中最上位: 101,743件（全削減の23%）。6月には割合が31%に上昇。Q1 2026で59,000のテック職が世界的に削減。Microsoft約4,800人削減（AI理由を否定）。全体的な米国レイオフは40%減だが高水準維持。
- **キーファクト:**
  - AI理由雇用削減: H1 2026で101,743件（全23%、6月は31%）
  - Q1 2026テック職削減: 59,000件（世界的）
  - Microsoft: ~4,800人削減（AI否定）
  - 米国全体レイオフ: 40%減だが高水準
- **引用URL:** https://www.cfo.com/news/us-layoffs-drop-40-in-2026-but-remain-high/824587/
- **Evidence ID:** EVD-20260710-0070

### INFO-071
- **タイトル:** Stanford AI Index 2026: AI Agents 6 Points from Human Performance
- **ソース:** Facebook (The Artificial Intelligence) / HBR / Stanford
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-01, KIQ-005-01, KIQ-CAR-002-OPS
- **関連企業:** (学術)
- **要約:** Stanford AI Index 2026でAIエージェントが人間パフォーマンスから6ポイント差に接近。HBRはAI時代のパフォーマンス管理に新指標が必要と指摘: タスク完了率（人間の修正不要で完了した割合）。Zoom調査: AI音声/チャットエージェントを実行する組織の79%が2027年までにアップグレード/交換を計画。
- **キーファクト:**
  - AIエージェント: 人間パフォーマンスから6ポイント差
  - HBR: タスク完了率が新KPI
  - Zoom: 79%がAIエージェントのアップグレード/交換計画（2027年まで）
  - 3つの失敗モードがパフォーマンス低下の大半を占める
- **引用URL:** https://hbr.org/2026/07/performance-management-needs-new-metrics-in-the-ai-era
- **Evidence ID:** EVD-20260710-0071

### INFO-072
- **タイトル:** Agentic AI in Ad Sales: Autonomous Agent-to-Agent Collaboration
- **ソース:** ExchangeWire / MarTech
- **公開日:** 2026-07-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05, KIQ-004-01
- **関連企業:** (広告業界)
- **要約:** エージェントAIが広告運用の進化を牽引。バイヤー、パブリッシャー、プラットフォーム間の自律的エージェント間協力を可能にする「ユニバーサルトランスレーター」。20以上の専門AIエージェントを展開する自律型マーケティング組織モデル登場。ActiveCampaign Active Intelligence 2.8等のマーテックツールも進化。
- **キーファクト:**
  - エージェント間自律協力: バイヤー-パブリッシャー-プラットフォーム間
  - 20+専門AIエージェントの自律マーケティング組織モデル
  - ActiveCampaign Active Intelligence 2.8リリース
  - 広告運用の完全自動化への道筋
- **引用URL:** https://www.exchangewire.com/blog/2026/07/06/agentic-ai-and-the-evolution-of-ad-sales/
- **Evidence ID:** EVD-20260710-0072

### INFO-073
- **タイトル:** New AI-Era Roles Emerging: AI Creative Director, AI Content Strategist, Prompt Engineer
- **ソース:** Instagram / HPE / OpenAI Careers / AIIobs
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-03
- **関連企業:** OpenAI, HPE
- **要約:** AI時代の新職種が創出: AI Creative Director、AI Content Strategist、Prompt Engineer、Conversational AI Designer。OpenAIがCreative Director (Growth)を募集。HPEがCreative Strategist (Brand + AI Integration)を募集。伝統的な資格（学位・職名・技術専門）よりAI活用能力を重視する採用動向。
- **キーファクト:**
  - 新職種: AI Creative Director, AI Content Strategist, Prompt Engineer, Conversational AI Designer
  - OpenAI: Creative Director (Growth)募集中
  - HPE: Creative Strategist (Brand + AI Integration)募集中
  - 採用基準: 学位・職名よりAI活用能力
- **引用URL:** https://www.aijobs.com/jobs/514614890-creative-director-growth
- **Evidence ID:** EVD-20260710-0073

### INFO-074
- **タイトル:** WEF Future of Jobs: 170M New Jobs by 2030, 86% Employers Expect AI Transformation
- **ソース:** WEF / GSMA
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-03, KIQ-004-01
- **関連企業:** (業界全体)
- **要約:** WEF Future of Jobs Report: AI経済は2030年までに1億7000万の新規雇用を創出予測。雇用主の86%がAIによる組織変革を予期。AIと情報処理技術が86%の組織を変革。リスキリングが鍵。AIは25%の全米仕事タスクを自動化可能。
- **キーファクト:**
  - 新規雇用創出: 170M by 2030
  - 86%の雇用主がAI変革を予期
  - AI自動化可能: 全米仕事タスクの25%
  - リスキリングが競争力の鍵
- **引用URL:** https://www.gsma.com/about-us/regions/asia-pacific/general/changetheface/job-impacts-opportunities-in-the-ai-economy/
- **Evidence ID:** EVD-20260710-0074

### INFO-075
- **タイトル:** G7 Summit: Altman, Hassabis, Amodei Discuss AGI; US-Led International Coalition Proposed
- **ソース:** Quartz / Instagram / LinkedIn
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02, KIQ-005-03
- **関連企業:** OpenAI, Google/DeepMind, Anthropic
- **要約:** Sam Altman、Demis Hassabis、Dario AmodeiがG7サミットに出席。Amodeiの2023年予測（2-3年以内にAIが人間の主要機能を実行）は「よく当たった」と評価。AmodeiとHassabisが米国主導の国際AI連合を共同提案。厳格な「強いAGI」は2031-2035頃。Altmanは自身の在任中にAGI到達可能と主張。Musk、Amodei、Altmanはそれぞれ独自の方法でAGIを目指す。
- **キーファクト:**
  - G7: Altman, Hassabis, Amodei出席
  - Amodei 2023予測: 「よく当たった」評価
  - 米国主導国際AI連合: Amodei+Hassabis共同提案
  - 強いAGI: 2031-2035頃
  - Altman: 自身在任中にAGI到達可能
- **引用URL:** https://www.facebook.com/quartznews/posts/icymi-sam-altman-demis-hassabis-and-dario-amodei-are-heading-to-the-g7-summit-in/1380498553945959/
- **Evidence ID:** EVD-20260710-0075

### INFO-076
- **タイトル:** AGI Definition Consensus Still Lacking; UN Preliminary AI Report Published
- **ソース:** Qubic / UN / CatDoes
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02, KIQ-005-03
- **関連企業:** (学術・国際ガバナンス)
- **要約:** AGI定義の合意が依然として不在。OpenAIのチャーター: 「ほとんどの経済的に価値ある仕事で人間を上回る高度に自律的なシステム」。他のラボは異なる定義を採用。国連がAI能力とリスクの暫定科学評価報告書（2026年7月）を発表。AGI研究は知能の多面性と全体性を強調。
- **キーファクト:**
  - OpenAI AGI定義: 経済的に価値ある仕事で人間を上回る高度自律システム
  - 定義合意: 不在継続
  - UN暫定AI報告書: 2026年7月発表
  - AGI研究: 知能の多面性・全体性を強調
- **引用URL:** https://www.un.org/independent-international-scientific-panel-ai/sites/default/files/2026-07/en_Preliminary%20Report_.pdf
- **Evidence ID:** EVD-20260710-0076

### INFO-077
- **タイトル:** BCG: Only 6% of Companies Are AI Leaders, Outperform Peers by 9pp in Shareholder Returns
- **ソース:** BCG
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-004-04, KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** BCG分析: 企業のわずか6%が「AIリーダー」に認定。しかしAIリーダーは業界調整後株主収益率でピアを9ポイント上回る。収益成長が主因。「AIトークは安い。価値創造は稀」。McKinsey: AIの参入障壁低下が予想より速い、優位性は独自データと組み込みワークフローに移行。「ツールは商品化する。堀はしない」。
- **キーファクト:**
  - AIリーダー認定率: わずか6%
  - AIリーダーの株主収益率: ピア比+9pp
  - 優位性の源泉: 独自データ・組み込みワークフロー
  - 「ツールは商品化する。堀はしない」
- **引用URL:** https://www.bcg.com/publications/2026/how-ai-leaders-create-competitive-advantage
- **Evidence ID:** EVD-20260710-0077

### INFO-078
- **タイトル:** OpenAI, Microsoft, Anthropic, Amazon Back $1B Workforce Transition Nonprofit
- **ソース:** Campus Technology
- **公開日:** 2026-07-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04, KIQ-004-03
- **関連企業:** OpenAI, Microsoft, Anthropic, Amazon
- **要約:** OpenAI、Microsoft、Anthropic、Amazonが$10億の労働力移行支援非営利団体を支援。AIによる雇用変化への対応認識の高まり。リスキリングがAI企業の戦略的取り組みとして位置づけられる。
- **キーファクト:**
  - $1B労働力移行支援イニシアティブ
  - 支援企業: OpenAI, Microsoft, Anthropic, Amazon
  - AI雇用変化対応の認識高まる
- **引用URL:** https://campustechnology.com/articles/2026/07/06/ai-giants-back-nonprofit-focused-on-workforce-transition.aspx
- **Evidence ID:** EVD-20260710-0078

### INFO-079
- **タイトル:** UNESCO Global Dialogue on AI Governance + UNIDIR AI Security Conference 2026
- **ソース:** UNESCO / UNIDIR / Forbes
- **公開日:** 2026-07-09
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** (国際ガバナンス)
- **要約:** UNESCOが7月6-7日にジュネーブでGlobal Dialogue on AI Governanceを開催。UNIDIRがAI、安全保障、倫理に関するグローバル会議2026を開催。国連がAIチャイルドセーフティ誓約を要請。AIガバナンスに「ラディカルな選択肢の幅」が必要とする議論。EU AI Act: 2026年8月2日に全面適用予定。
- **キーファクト:**
  - UNESCO: Global Dialogue on AI Governance (7/6-7 ジュネーブ)
  - UNIDIR: AI・安全保障・倫理グローバル会議
  - 国連: AIチャイルドセーフティ誓約要請
  - EU AI Act: 8月2日全面適用予定
- **引用URL:** https://www.unesco.org/en/articles/global-dialogue-ai-governance-geneva-6-7-july
- **Evidence ID:** EVD-20260710-0079

### INFO-080
- **タイトル:** H1 2026: $252B AI Investment, US Led with $109B (12x China)
- **ソース:** LPL Financial / Research.com
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-005-01
- **関連企業:** (業界全体)
- **要約:** 2026年上半期のグローバルAI投資は$252B。米国が$109Bで中国の12倍をリード。AIモデルの難しいベンチマークでの性能が急騰。AI奨学金: 2022年以降2,716件の新規AI関連賞（Sallie Mae）。州AI法律: 2026年の31%が超党派スポンサー（2025年32%から横ばい）。
- **キーファクト:**
  - グローバルAI投資: $252B（H1 2026）
  - 米国: $109B（中国の12倍）
  - AI奨学金: 2,716件（2022年以降）
  - 州AI法律の超党派率: 31%（2026年）
- **引用URL:** https://techpolicy.press/where-state-ai-legislation-stands-half-way-into-2026
- **Evidence ID:** EVD-20260710-0080

### INFO-081
- **タイトル:** ByteDance Seedream 5.0 Pro: Multimodal Image Creation Model
- **ソース:** ByteDance Seed Blog (中国語)
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDance Seedがマルチモーダル画像創作モデルSeedream 5.0 Proを発表。画像テキストマッチング、構造的合理性、テキストレンダリング、画面美感の基礎能力が全面向上。火山方舟体験センターで利用可能。豆包・即梦にも順次展開。
- **キーファクト:**
  - Seedream 5.0 Pro: マルチモーダル画像創作モデル
  - 画像-テキストマッチング・構造合理性・テキストレンダリング向上
  - 火山方舟・豆包・即梦で展開
- **引用URL:** https://seed.bytedance.com/zh/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro
- **Evidence ID:** EVD-20260710-0081

### INFO-082
- **タイトル:** ByteDance Doubao Confirms Agent Feature Shutdown July 15; Nubian AI Phone Partnership
- **ソース:** STCN / Sina (中国語)
- **公開日:** 2026-07-04
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-01
- **関連企業:** ByteDance, Nubian
- **要約:** 豆包プラットフォームが製品機能調整により2026年7月15日に智能体（エージェント）機能を下線（終了）することを正式確認。機能終了後も一定期間スマートエージェント情報・履歴会話の閲覧・保存が可能。努比亚との提携で世界初AI智能体手機をWAIC 2026（7/17-20）で初展示予定。
- **キーファクト:**
  - 豆包智能体機能: 7月15日下線（終了）正式確認
  - 終了後: 一定期間情報閲覧・保存可能
  - 努比亚提携: 世界初AI智能体手機
  - WAIC 2026 (7/17-20)で初展示
- **引用URL:** https://www.stcn.com/article/detail/3998380.html
- **Evidence ID:** EVD-20260710-0082

### INFO-083
- **タイトル:** ByteDance EdgeBench: New Scaling Law Discovery for Real-World Environment Learning
- **ソース:** ByteDance Seed Blog (中国語)
- **公開日:** 2026-07-09
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-005-01
- **関連企業:** ByteDance
- **要約:** ByteDance Seedが真実世界環境学習を測定する超長期評価セットEdgeBenchを発表。新たなScaling Lawを発見。ByteDanceの研究インフラの成熟を示す。Seedance 2.0、Seed-Audio 1.0、Seedream 5.0 Pro等の統合マルチモーダルスタック構築中。
- **キーファクト:**
  - EdgeBench: 真実世界環境学習の超長期評価セット
  - 新Scaling Law発見
  - 統合マルチモーダルスタック: Seedance 2.0 + Seed-Audio 1.0 + Seedream 5.0 Pro
  - ByteDance研究インフラの成熟
- **引用URL:** https://seed.bytedance.com/zh/blog/edgebench-measuring-real-world-environment-learning-and-discovering-a-new-scaling-law
- **Evidence ID:** EVD-20260710-0083

### INFO-084
- **タイトル:** China Confirms Talks with Alibaba, ByteDance on Restricting Foreign AI Model Access
- **ソース:** Time Magazine
- **公開日:** 2026-07-07
- **信頼性コード:** A-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-002-03, KIQ-005-03
- **関連企業:** ByteDance, Alibaba
- **要約:** Time Magazineが中国当局がAlibaba、ByteDance、Z.aiと最先端AIモデルへの海外アクセス制限について協議中と確認。オープンソースモデルを含む。中国AIモデルの国際的な利用制限は、オープンソースAIエコシステムに重大な影響。
- **キーファクト:**
  - 協議対象: Alibaba, ByteDance, Z.ai
  - 制限対象: 最先端AIモデル（オープンソース含む）
  - オープンソースAIエコシステムへの影響懸念
  - 双方向AIデカップリングの一環
- **引用URL:** https://time.com/article/2026/07/07/china-ai-models-alibaba-bytedance/
- **Evidence ID:** EVD-20260710-0084

### INFO-085
- **タイトル:** ByteDance Doubao: 1.4B DAU, Revenue <1M CNY/Day vs Compute Cost 130-240M CNY/Day
- **ソース:** 36kr / Sina / Yage-AI (中国語ソース)
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** 豆包の日活は約1.4億（月活3.45億）、国内AI製品第1位。しかし日収は100万元（人民幣）未満、日次算力コストは1.3〜2.4億元。日収vs日次コストのギャップが数百倍。AI原生App全体月活4.4億（豆包>千問1.66億>DeepSeek 1.27億）。7月15日エージェント機能終了は高コスト低収益サービスの整理が目的。
- **キーファクト:**
  - 豆包日活: ~1.4億（月活3.45億）
  - 日収: 100万元未満（人民幣）
  - 日次算力コスト: 1.3〜2.4億元
  - 日収vsコストギャップ: 数百倍
  - AI原生App月活: 4.4億（豆包#1、千問1.66億#2、DeepSeek 1.27億#3）
  - 7月15日エージェント終了: 高コスト低収益整理が目的
- **引用URL:** https://36kr.com/p/3886785815640964
- **Evidence ID:** EVD-20260710-0085

### INFO-086
- **タイトル:** ByteDance Seedance 2.5: 30-Second 4K Video Generation, Global First
- **ソース:** OsChina / 36kr / Sohu (中国語ソース)
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDance Seedance 2.5が単条動画30秒4K生成で世界初。50個の全モーダル素材同時入力サポート（世界最多）。全体画面を維持したまま局所修正可能。Seedance 2.0は2K動画1分以内生成、テキスト/画像/動画/音声入力対応。2026年AI動画生成は全面成熟期に突入。
- **キーファクト:**
  - Seedance 2.5: 30秒4K動画生成（世界初）
  - 50個全モーダル素材同時入力（世界最多）
  - 局所修正機能（全体画面維持+部分編集）
  - Seedance 2.0: 2K動画、1分以内生成、マルチモーダル入力
- **引用URL:** https://www.oschina.net/news/465850
- **Evidence ID:** EVD-20260710-0086

### INFO-087
- **タイトル:** ByteDance Raises 2026 AI Capex to 200B+ CNY; Alibaba Considers Raising to 480B CNY
- **ソース:** EastMoney / China Daily (中国語ソース)
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance, Alibaba
- **要約:** ByteDanceが2026年AI資本支出計画を2000億元（人民幣）超に引き上げ。Alibabaは2025-2027年AIインフラ・クラウド投資を3800億元から4800億元への引き上げを検討。可霊AIが近30億ドル調達。中国AIインフラ投資が加速する一方、AI先進モデルへの海外アクセス制限と国内スタートアップへの海外投資制限も協議中。
- **キーファクト:**
  - ByteDance 2026 AI資本支出: 2000億元超（人民幣）に引き上げ
  - Alibaba AI投資: 3800億→4800億元検討（2025-2027）
  - 可霊AI調達: ~$3B
  - 海外投資制限: 国内AIスタートアップへの特定海外投資者制限を協議
- **引用URL:** https://caifuhao.eastmoney.com/news/20260709112511126221070
- **Evidence ID:** EVD-20260710-0087

### INFO-088
- **タイトル:** AI Safety Index Summer 2026 + Great American AI Act Bipartisan Draft
- **ソース:** Future of Life Institute / Mintz
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** (業界全体)
- **要約:** Future of Life InstituteがAI Safety Index Summer 2026を発表。主要AI企業を安全性・セキュリティ領域で評価。米国下院が包括的連邦AIガバナンス枠組みを導入。Great American AI Act超党派討論草案が透明性規定を提案。Canadian AI Safety Institute (CAISI)設立。Illinois AI Safety法: 内部告発者保護・秘密報告チャネル創設。
- **キーファクト:**
  - AI Safety Index Summer 2026: 企業別安全性評価
  - Great American AI Act: 超党派討論草案（透明性規定）
  - CAISI: カナダAI安全研究所設立
  - Illinois: AI安全性内部告発者保護・秘密報告チャネル
- **引用URL:** https://futureoflife.org/ai-safety-index-summer-2026/
- **Evidence ID:** EVD-20260710-0088

### INFO-089
- **タイトル:** Mistral Large 3 (675B MoE) + CEO Warns Enterprises on Closed Model Lock-in
- **ソース:** TechCrunch / TheNextWeb / AIZolo
- **公開日:** 2026-07-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-03, KIQ-003-05
- **関連企業:** Mistral AI
- **要約:** Mistral Large 3: 675B params MoE、オープンウェイト、2025年12月リリース。Mistral CEO Mensch: エンタープライズはオープンソースモデル、オープンデータ、独自訓練フライホイールを採用すべきと主張。クローズドモデルはプロバイダーにレバレッジを与えると警告。新オープンウェイトモデルが今夏予定。
- **キーファクト:**
  - Mistral Large 3: 675B MoE、オープンウェイト、2025年12月リリース
  - CEO Mensch: エンタープライズのオープンソース採用推奨
  - クローズドモデル=ベンダーロックイン警告
  - 新オープンウェイトモデル今夏予定
- **引用URL:** https://thenextweb.com/news/mistral-ceo-open-source-enterprise-warning
- **Evidence ID:** EVD-20260710-0089

### INFO-090
- **タイトル:** UN Independent International Scientific Panel on AI (40 Members) Launched July 1, 2026
- **ソース:** Substack (Stefan Bauschard) / UN
- **公開日:** 2026-07-09
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-02, KIQ-005-03
- **関連企業:** (国際ガバナンス)
- **要約:** 国連の新独立国際科学AIパネル（40人会員）が2026年7月1日に発足。AI能力とリスクの暫定科学評価報告書を発表。Yoshua BengioはAIを放置した場合の危険性を継続警告。Yann LeCunはワールドモデルによる推論・計画の追求を主張。AGIの定義合意は依然不在。
- **キーファクト:**
  - UN AI科学パネル: 40人会員、7月1日発足
  - 暫定AI能力・リスク評価報告書発表
  - Bengio: AI放置の危険性警告継続
  - LeCun: ワールドモデル推論・計画の追求
- **引用URL:** https://stefanbauschard.substack.com/p/what-happens-next-is-already-happening
- **Evidence ID:** EVD-20260710-0090

### INFO-091
- **タイトル:** AI API Price Table July 2026: DeepSeek V4 Pro $1.74, Gemini 3.5 Flash $1.50
- **ソース:** BenchLM / Finout
- **公開日:** 2026-07-09
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-03
- **関連企業:** Google, DeepSeek, OpenAI, Anthropic
- **要約:** 2026年7月API価格表: Gemini 3.5 Flash $1.50, DeepSeek V4 Pro (Max) $1.74, GPT-5.2/5.3 Codex $1.75, Gemini 3.1 Pro $2, Claude Sonnet 5 $3, Claude Opus 4.8 $5。中国モデルが価格破壊の最前線。FinOps ツール（Finout, Vantage, CloudZero等）でAIコスト可視化が必須化。
- **キーファクト:**
  - Gemini 3.5 Flash: $1.50/M input
  - DeepSeek V4 Pro: $1.74/M input
  - GPT-5.2/5.3 Codex: $1.75/M input
  - Gemini 3.1 Pro: $2/M input
  - Claude Sonnet 5: $3/M input
  - Claude Opus 4.8: $5/M input
- **引用URL:** https://benchlm.ai/blog/posts/llm-pricing-2026
- **Evidence ID:** EVD-20260710-0091

### INFO-092
- **タイトル:** CyberAgent: 20.3% ROE, 89.8% Earnings Growth - Japan AI Leader Exposure
- **ソース:** SimplyWall.st
- **公開日:** 2026-07-09
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-04, KIQ-002-05
- **関連企業:** CyberAgent
- **要約:** CyberAgentが日本インターネット経済へのAIリーダーとしてのポジションを提供。ROE 20.3%、過去1年の利益成長89.8%、2026年ガイダンス更新。ファウンダー主導企業としてのAI投資・収益化モデルの参考事例。
- **キーファクト:**
  - ROE: 20.3%
  - 利益成長: 89.8%（過去1年）
  - ファウンダー主導企業
  - 2026年ガイダンス更新
- **引用URL:** https://simplywall.st/stocks/jp/semiconductors/tse-6323/rorze-shares/news/investing-in-automation-with-3-japanese-founder-led-stocks-s
- **Evidence ID:** EVD-20260710-0092

### INFO-093
- **タイトル:** GPT-5.6 (Sol, Terra, Luna) General Availability: Three-Tier Model Family
- **ソース:** MarkTechPost / OpenAI
- **公開日:** 2026-07-08
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01, KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIがGPT-5.6ファミリー（Sol, Terra, Luna）の一般提供を開始。制限プレビューを経て3モデル構成でリリース。プログラム的ツール呼び出しをサポート。GPT-5.6 Sol: Terminal-Bench 91.9%、ARC-AGI-3 7.8%。GPT-5.6全体: 1.72xトークン効率向上、マルチホップ88%。
- **キーファクト:**
  - GPT-5.6ファミリー: Sol, Terra, Luna の3モデル
  - プログラム的ツール呼び出しサポート
  - Sol: Terminal-Bench 91.9%、ARC-AGI-3 7.8%
  - トークン効率: 1.72x向上
- **引用URL:** https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/
- **Evidence ID:** EVD-20260710-0093
