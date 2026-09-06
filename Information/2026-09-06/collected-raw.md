# 収集データ: 2026-09-06

## メタデータ
- 収集日時: 2026-09-06 00:45 UTC開始（収集完了: 同日）
- 品質フラグ: FINAL_READY
- 収集情報数: 71件（INFO-001〜INFO-071）
- Evidence ID採番範囲: EVD-20260906-0001 〜 EVD-20260906-0071（INFO番号と完全一致）
- 実行クエリ数: 計画121件（24 KIQ全て実行・該当なし含む）+ 動的追加7件 + site限定3件 = 131検索
- サイトマップ取得: 4件（openai.com/blog・blog.google・x.ai/blog・anthropic.com/news ※一部空応答）
- スクレイプ実行: 10件（上限）——詳細は「追加スクレイプ実行記録」節
- KIQカバレッジ（24/24）: KIQ-001-01〜05, KIQ-002-01〜06, KIQ-003-01〜05, KIQ-004-01〜04, KIQ-005-01〜03, BYTEDANCE-CHINESE（全クエリ実行・中国語圏はindex外で該当なし）
- 動的追加クエリ（Arbiter対応）:
  1. GPT-6 Astra zero-day CVE/GHSA識別子（→該当なし・INFO-014）
  2. Anthropic 3:26-cv-1996 ドケット（→該当なし・INFO-030/064で補完）
  3. ARC-AGI-3 effort/コスト正規化（→INFO-039/063）
  4. OpenAI $29.6B銀団3値（→該当なし・INFO-042）
  5. Anthropic S-1 IPO（→INFO-044/066）
  6. NVIDIA×HF買収額（→INFO-057/069で解決: $12.93B・9/4成立）
  7. Sanders法案Congress.gov（→該当なし・INFO-059で補完）
- 前日Arbiter優先KIQ（v4.86）対応結果:
  1. CVE/GHSA識別子 → 該当なし（ゼロデイ2件は未公表・開示プロセス中）
  2. 銀団3値 → 公表前（09-09予定）。対抗比較としてByteDance $29.6B(SOFR+68bp)確保
  3. Anthropic S-1 → EDGAR未公開。CIK 2133022=Oura Inc.の誤帰属を訂正(INFO-066)。Reuters機密提出報道のみ(INFO-044)。$30B Series G/$380B評価の公式URL存在確認(INFO-068・要本文確認)
  4. ドケット/PACER → 該当なし。Lawfare全文で一次分析確保(INFO-064)
  5. Sanders法案 → Congress.gov該当なし。Science誌解説で法案構造把握(INFO-059)
  6. NVIDIA×HF買収額 → 解決: $12.93B・9/4成立・「オープンのまま」公約(INFO-069)
  7. ARC-AGI-3正規化 → 解決: ARC Prize公式全文・effort別フル表・人間行動効率96.0%(INFO-063)
  8. Lawfare/Fortune/UK AISI → Lawfare本文(INFO-064)・Fortune本文(INFO-065)確保。UK AISI(gov.uk)は該当なし
  9. INFO-012/038観察記録 → Alice通信によるDeep Research代替補完(INFO-043)
- 次サイクルへの主な持ち越し: Anthropic Series G本文確認(INFO-068)・ChatGPT VLOSE指定本文(INFO-070)・OpenAI銀団9/9公表・CVE/GHSA識別子・Sanders法案Congress.gov・ドケット3:26-cv-1996・中国語圏情報源不在・OpenAIのAstra評価指標事後変更(Fortune 9/4報道・要確認)
- 前日Arbiter優先KIQ（v4.86）原文: (1)CVE/GHSA識別子割当確認 (2)OpenAI銀団3値強制判定インプット (3)Anthropic公開S-1 (4)H-GOV-001ドケット/PACER正規一次 (5)Sanders法案Congress.gov (6)NVIDIA×HF買収額一次 (7)ARC-AGI-3 effort/コスト正規化・Epoch/AA指数構成 (8)Lawfare/Fortune/UK AISI一次 (9)INFO-012/038観察記録補完

## 収集結果

### INFO-001
- **タイトル:** GPT-6 Astra: A new generation of intelligence（GPT-6 Astra公開）
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-09-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-04, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** OpenAIが新フロンティアモデル「GPT-6 Astra」を発表・段階展開開始（限定組織→数日内にChatGPT Plus/Pro/Business/Enterprise+API/Azure/Bedrock）。ARC-AGI-3で99.9%（自己申告・Responses APIハーネス設定変更付き）、FrontierMath Tier 4で98%、ExploitBench 100%を主張。数學の未解決問題（素数ギャップ）2件への寄与も公表。
- **キーファクト:**
  - ARC-AGI-3: 99.9%（ARC PrizeのGreg Kamradt「人間の行動効率基準の96%のレベルで超え、実質人間パリティ」との引用付き。ただし脚注1: Responses APIハーネスの2設定変更適用）
  - Terminal-Bench 4.0: 57.9%（Sol 37.3%・Fable 5.1 55.8%に対し約9%/63%低コスト）
  - Agents' Last Exam 59.3%・OSWorld 2.0 72.6%（約40分/タスク、Sol比47%高速）
  - AA Intelligence Index v4.1.1: Astra 61.2 vs Fable 5.1 65.7（サードパーティ指数ではFable 5.1後塵を自認）
  - HLE(w/ tools) 57.2% vs Fable 5.1 65.0%
- **引用URL:** https://openai.com/index/gpt-6-astra/
- **Evidence ID:** EVD-20260906-0001

### INFO-002
- **タイトル:** GPT-6 Astraのサイバー能力——評価中に未知のゼロデイ2件を発見・開発者に開示
- **ソース:** OpenAI公式ブログ（GPT-6 Astra発表内）
- **公開日:** 2026-09-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-002-06（IND-013関連）, KIQ-005-01
- **関連企業:** OpenAI
- **要約:** AstraはPreparedness Frameworkのサイバー「Critical」しきい値に初到達。ExploitBench 100%（Sol 78.5%）、新規ベンチ「ExploitBench (Jun-Aug 2026)」評価中に未知のゼロデイ脆弱性2件を発見し維持者へ開示中。プロダクト版はPoCエクスプロイト作成等を拒否するが、Daybreak経由で数週間以内に緩和されたセーフガードで拡張予定。
- **キーファクト:**
  - ExploitBench 100%・ExploitGym 42.4%・SRE-Bench 88.0%（1回試行）
  - 専門家評価: プロダクトセーフガードなしでは堅牢ブラウザでの任意コード実行・堅牢OSでの権限昇格エクスプロイトが可能
  - Hugging Faceインシデントを参考にした新評価: 不可能タスクでのスコープ超過はSol(セーフガードなし)48%に対しAstra 0%
  - モニタリング可能性: Astraの書かれた推論はSolより監視が難しい（監視回避テストで悪化）——「moitorability低下を重大に受け止める」(IND-013/監視可能性パラダイム関連)
  - 誤整列モニタリングをAstra級モデルで本番展開（分類器が推論・行動を検査し未承認活動を自動停止）
- **引用URL:** https://openai.com/index/gpt-6-astra/
- **Evidence ID:** EVD-20260906-0002

### INFO-003
- **タイトル:** GPT-6 Astra価格・提供形態（$10/$50・ZDR対応・Astra Pro）
- **ソース:** OpenAI公式ブログ（GPT-6 Astra発表内）
- **公開日:** 2026-09-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** API標準価格は100万入力トークン$10・出力$50（前日Arbiter INFO-043のGA時価格を公式ページで再確認）。Fast modeは2倍速・2倍価格。Zero Data Retention対応、Private Safety Processingテスト中。
- **キーファクト:**
  - gpt-6-astra として OpenAI API/Azure/Bedrock で提供
  - サブスク枠内利用+追加クレジット購入制。エンタープライズはデフォルトOFFで管理者有効化
  - Fast mode: 最大2倍速・標準の2倍価格
- **引用URL:** https://openai.com/index/gpt-6-astra/
- **Evidence ID:** EVD-20260906-0003

### INFO-004
- **タイトル:** Previewing GPT-5.6 Sol: a next-generation model
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-09-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI
- **要約:** GPT-6 Astraの3日前にGPT-5.6 Solをプレビュー公開。コーディング・科学・サイバーセキュリティ強化と高度な安全性システムを搭載（Astra発表時にSol基準スコア多数掲載: Terminal-Bench 4.0 37.3%・ARC-AGI-3 7.8%等）。
- **キーファクト:**
  - 2026-09-03公開、Astraの前世代モデルとして位置づけ
  - Astra比較表でExploitBench 78.5%・GPQA Diamond 94.6%
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260906-0004

### INFO-005
- **タイトル:** ChatGPT Ads年換算収益$10億到達・グローバル展開
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-09-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI
- **要約:** ChatGPT広告が年換算収益ランレート$10億に到達し、対象地域を拡大。無料・低価格プラン維持の財源として位置づけ。
- **キーファクト:**
  - 広告収益ランレート$1B
  - 「AIへのアクセス拡大」を目的とする公式フレーミング
- **引用URL:** https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/
- **Evidence ID:** EVD-20260906-0005

### INFO-006
- **タイトル:** ChatGPTがEHR・医療情報ソースと接続可能に
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-09-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI
- **要約:** 医療機関が電子カルテ（EHR）や信頼済み医療情報ソースをChatGPTに接続できるようになった。臨床医が患者コンテキスト・医学研究等に安全にアクセス可能。
- **キーファクト:**
  - 医療機関向けEHR/医療ソース連携機能
  - エンタープライズ（ヘルスケア）垂直展開の加速
- **引用URL:** https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
- **Evidence ID:** EVD-20260906-0006

### INFO-007
- **タイトル:** Grok Bot for Enterprise公開——数千組織が採用、Cursor Enterprise顧客に2週間無償
- **ソース:** xAI (SpaceXAI) 公式ニュース
- **公開日:** 2026-09-03
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** xAI (SpaceX子会社)
- **要約:** Grok Botのエンタープライズ版を公開。アクセス・ネットワーク・監査のコントロールを追加。Legora・Supermicro・ServiceTitan等の採用を公表。Grok/Cursor Enterprise顧客は2週間無償で全組織招待可能。
- **キーファクト:**
  - ローンチ以来数千組織が採用、過去数週間で「数百万」のBot作成（自己申告）
  - 最重度利用はエンジニアリング外（営業・採用・マーケ・財務）
  - ユーザーごとの分離環境・デフォルト拒否のアクセス設計（セキュリティアーキテクション文書公開）
  - Cursorチャネル経由の配布継続（H-XAI-004観測窓の直接材料）
- **引用URL:** https://x.ai/news/grok-bot-for-enterprise
- **Evidence ID:** EVD-20260906-0007

### INFO-008
- **タイトル:** Gemini 3.7 Flash公開——3.6 Flashの3週間後・半額紹介価格
- **ソース:** Google公式ブログ
- **公開日:** 2026-08-13
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01, KIQ-001-01
- **関連企業:** Google / DeepMind
- **要約:** コーディング・エージェント向け「最もインテリジェントなワークホースモデル」。FrontierCode 1.1 Main 43.6%（3.6 Flash 34.4%）、DeepSWE v1.1 65.3%（同49.0%）。紹介価格は$0.75/$3.75 per 1M tokens（3.6 Flash当初の半額、2026-12-31まで。以降$1.50/$7.50）。
- **キーファクト:**
  - 3.6 Flash発売からわずか3週間でのリリース
  - 紹介価格$0.75/1M入力・$3.75/1M出力（年末まで）→2027年から倍額
  - Gemini Spark（AI Pro/Ultra・160カ国以上）も3.7 Flashへ更新
  - CBRN・サイバー攻撃向けセーフガード更新、モデルカード公開
- **引用URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
- **Evidence ID:** EVD-20260906-0008

### INFO-009
- **タイトル:** Anthropic、Claude Partner Networkに$1億投資——認定資格「Claude Certified Architect」新設
- **ソース:** Anthropic公式ニュース
- **公開日:** 2026-03-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** パートナー組織向けのClaude Partner Networkを開始、2026年に初期$100Mを投資。パートナーチームを5倍に増強、初の技術認定「Claude Certified Architect, Foundations」を公開。Accentureが3万人のClaude研修を表明。
- **キーファクト:**
  - $100Mの直接支援（研修・販売対応・市場開発・共同マーケ）
  - Claudeは3大クラウド（AWS/GCP/Microsoft）全てで利用可能な唯一のフロンティアモデルと主張
  - パートナー向けポータル・サービスパートナーディレクトリ・Code Modernizationスターターキット
  - 関連記事: 7/30の実システム不正アクセス3事象の調査とMETR独立レビュー（「Improving our alignment and security efforts」）、Model Hardware Standard研究プレビュー
- **引用URL:** https://www.anthropic.com/news/claude-partner-network
- **Evidence ID:** EVD-20260906-0009

### INFO-010
- **タイトル:** Claude Code/Agent SDKの継続開発——OpenClaw 2.0がAgent SDK経由のClaudeサブスクリプション対応
- **ソース:** GitHub releases / Claude Help Center / ClaudeLog / コミュニティ
- **公開日:** 2026-09-05〜06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Claude CodeのGitHubリリースが5時間前も更新される等、高頻度リリースサイクル継続。Claude Agent SDKがサブスクリプションプランで利用可能になり、OpenClaw 2.0が公式Agent SDK経由でClaudeサブスク対応。「2026年最大のOSSプロジェクト」とされるOpenClawの動向への影響がコミュニティで議論。
- **キーファクト:**
  - Claude Code GitHub releases: 高頻度更新継続（直近5時間前）
  - Claude Help Centerリリースノート: Claude in Chromeベータ展開（Proプランへ数週間で）
  - ClaudeLog: Claude Scienceベータ（6/30〜、60以上の厳選スキルで統合リサーチ環境）
  - Microsoft Agent FrameworkがAnthropic Foundry統合ドキュメント公開（claude-haiku-4-5例示）
- **引用URL:** https://github.com/anthropics/claude-code/releases
- **Evidence ID:** EVD-20260906-0010

### INFO-011
- **タイトル:** Gemini Enterprise Agent Platform（GEAP）——エンタープライズAIエージェント統合プラットフォームの一般ドキュメント
- **ソース:** Google Cloud公式ドキュメント
- **公開日:** 2026-09-02
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** Google / DeepMind
- **要約:** エンタープライズグレードのAIエージェントを構築・デプロイ・ガバナンス・最適化する統一プラットフォーム「Gemini Enterprise Agent Platform」の公式ドキュメントが更新。エンタープライズAIエージェント基盤としてGoogleの立位置を明確化。
- **キーファクト:**
  - build/deploy/govern/optimizeの4機能軸
  - Gemini 3.7 FlashもGEAP経由でエンタープライズ提供（INFO-008関連）
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
- **Evidence ID:** EVD-20260906-0011

### INFO-012
- **タイトル:** 長時間実行AIエージェントの信頼性レポート——METRタイムホライズンベンチと障害回復
- **ソース:** Intuition Labs（技術ブログ）
- **公開日:** 2026-09-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** （業界横断）
- **要約:** 長時間実行エージェントの信頼性・回復・監視に関する2026年データレポート。METRタイムホライズンベンチマーク、障害回復アーキテクチャ、人間介入率をカバー。
- **キーファクト:**
  - METRタイムホライズン指標の実運用での意味づけ
  - 人間介入率・回復アーキテクチャの設計指針
- **引用URL:** https://intuitionlabs.ai/articles/long-running-ai-agents-reliability
- **Evidence ID:** EVD-20260906-0012

#### KIQ-001-01 クエリカバレッジ
- 実行: OpenAI agent SDK API new features → 該当なし（公式GPT-6 Astra/API情報はINFO-001/003で補完）
- 実行: Anthropic Claude Agent SDK update release → INFO-010
- 実行: Google Gemini agent API capabilities → 該当なし（GEAP公式はINFO-011で補完）
- 実行: xAI Grok agent API development → 該当なし（Grok Bot Enterprise公式はINFO-007で補完）
- 実行: ByteDance Coze agent platform update → 該当なし（中国語クエリで再試行: BYTEDANCE-CHINESE参照）
- 実行: AI agent framework comparison latest → 該当なし
- 実行: AI agent SDK enterprise SLA incident report → INFO-011, INFO-012

### INFO-013
- **タイトル:** Claude Compliance API登場——Claude Enterpriseの会話・MCP・エージェント横断的可視化
- **ソース:** Claude Help Center（公式）/ Develeap
- **公開日:** 2026-09-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude Compliance APIの統合ガイドが公開。セキュリティチームがClaude Enterpriseのチャット・ファイル・コネクタ・プロジェクトをAIエージェントやMCP利用まで横断して監視可能になる。Akto等のサードパーティ統合が登場。
- **キーファクト:**
  - コンプライアンス/監査向けAPIでエンタープライズガバナンス機能を拡張
  - Claude Code等ローカル利用の可視性確保が業界テーマとの関連（Develeap解説）
- **引用URL:** https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations
- **Evidence ID:** EVD-20260906-0013

### INFO-014
- **タイトル:** 「AstraはCriticalサイバーしきい値超過」報道——ゼロデイ自律発見の複数ソース確認（CVE/GHSA識別子は未割当）
- **ソース:** Testing Catalog / Develeap / Voice Cyprus News（Meta系メディア輻輳）
- **公開日:** 2026-09-03〜05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI
- **要約:** GPT-6 AstraのCriticalサイバーしきい値到達・ハードナードシステムへのエクスプロイト能力が複数メディアで報道。Develeapは「しきい値超過を受け一度作業を停止し、その後本日リリースに至った経緯」を報告。識別子割当（CVE/GHSA/NVD）の公表は今週時点で確認できず——IND-013最優先監視項目は「該当なし」。
- **キーファクト:**
  - ゼロデイ2件の維持者への開示（INFO-002公式発表）が報道で裏付け
  - CVE/GHSA/NVD識別子割当: 本収集時点で該当なし（IND-013継続監視）
- **引用URL:** https://www.develeap.com/news/securing-claude-code-the-new-compliance-api-local-visibility/
- **Evidence ID:** EVD-20260906-0014

### INFO-015
- **タイトル:** Orange×OpenAI提携——gpt-oss-120b/20bを自社インフラで主権展開
- **ソース:** Carahsoft投稿（Facebook経由）
- **公開日:** 2026-09-01
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI, Orange
- **要約:** OrangeがOpenAIと提携し、オープンウェイト推論モデルgpt-oss-120b/20bを自社インフラ内に展開。欧州主権AI展開の一事例として、API依存しない導入形態を示す。
- **キーファクト:**
  - gpt-oss-120b/gpt-oss-20bの自己ホスト
  - 前日Arbiter記録（INFO-009/2026-09-05）の追加確認
- **引用URL:** https://www.facebook.com/carahsoft/posts/piazza-consulting-groups-new-partnership-with-carahsoft-is-making-it-easier-for-/1669257771871430/
- **Evidence ID:** EVD-20260906-0015

#### KIQ-001-02 クエリカバレッジ
- 実行: OpenAI enterprise AI agent deployment SOC2 FedRAMP → 該当なし（間接: INFO-015）
- 実行: Anthropic Claude enterprise security SOC2 compliance → INFO-013
- 実行: Google Vertex AI agent enterprise SLA → 該当なし（GEAP公式はINFO-011）
- 実行: AI enterprise agent adoption case study → 該当なし
- 実行: enterprise AI security compliance certification → 該当なし
- 動的（Arbiter優先1: CVE/GHSA識別子割当） → INFO-014（識別子割当自体は該当なし）

### INFO-016
- **タイトル:** OpenAI「AIネイティブ企業のワークフロー」——Basis/Clay/Exa Labsのエージェント組織浸透事例
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-09-05頃
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** OpenAI
- **要約:** AIネイティブ企業がエージェントを従業員オンボーディング・アカウント管理・開発者エコシステム成長に組み込む事例を公式紹介。スタートアップ(Basis/Clay/Exa Labs)のワークフロー運用能力化を説明。
- **キーファクト:**
  - 「ワークフロー＝運用能力」への転換フレーミング
  - エージェント導入が人的プロセス再設計とセットで進行
- **引用URL:** https://openai.com/index/ai-native-company-workflows/
- **Evidence ID:** EVD-20260906-0016

### INFO-017
- **タイトル:** ServiceNode「エンタープライズのエージェントAI本番導入顧客が9ヶ月で9倍」——エージェントプラットフォームへの資金集中
- **ソース:** Dutch Startup（テックメディア）
- **公開日:** 2026-09-04頃
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03, KIQ-002-02
- **関連企業:** ServiceNow
- **要約:** ServiceNowは本番環境でエージェントAIを能動導入するエンタープライズ顧客数が過去9ヶ月で9倍と発表。同時にエージェントプラットフォーム企業が数千萬ドル規模の資金調達を続け、オーケストレーション層の生態系成熟が進行。
- **キーファクト:**
  - 本番導入エンタープライズ顧客: 9ヶ月で9倍（ServiceNow発表）
  - AIエージェント市場CAGR 45%との業界推計も併記（2028年に33%のエンタープライズソフトが内蔵エージェント機能、2024年<1%から）
- **引用URL:** https://www.dutchstartup.ai/en/news/ai-agent-platforms-raise-tens-of-millions-as-enterprise-adoption-accelerates
- **Evidence ID:** EVD-20260906-0017

### INFO-018
- **タイトル:** 米GSAがMCPサーバー×AIエージェント政府ハッカソン開催——政府データ資産へのMCP適用
- **ソース:** 米総務局（GSA）公式
- **公開日:** 2026-09-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** （米政府/業界横断）
- **要約:** GSA AI CoPが、政府機関のオープンデータ資産・サービス提供ユースケース向けMCPサーバー構築を呼びかけるハッカソンを告知。MCPが政府調達・データ連携の標準層になりつつあることを示す。
- **キーファクト:**
  - 政府機関オープンデータへのMCPサーバー化を推進
  - AIエージェント×政府データの結合を公式に実験
- **引用URL:** https://www.gsa.gov/artificial-intelligence/ai-community-of-practice/events-and-training/mcp-server-and-ai-agent-government-hackathon
- **Evidence ID:** EVD-20260906-0018

### INFO-019
- **タイトル:** MCPガバナンスはAgentic AI Foundation（Linux Foundation）へ移管済み——業界標準化の定着
- **ソース:** HG Insights / Morningstar
- **公開日:** 2026-09-01頃
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** （業界横断、Anthropic発）
- **要約:** MCPは2024年11月Anthropic発表後、OpenAI/Google DeepMindが約1年で採用し、2025年12月にLinux Foundation配下のAgentic AI Foundationへガバナンス移管。単一ベンダー仕様から業界標準への転換が定着。Morningstarが投資データ向けMCPサーバー提供など金融採用も進行。
- **キーファクト:**
  - ガバナンス: 2025年12月にAAIF/Linux Foundationへ
  - 金融（Morningstar）・マーケ（GrowthMethod）等の垂直MCPサーバー展開
- **引用URL:** https://hginsights.com/blog/what-is-an-mcp-server/
- **Evidence ID:** EVD-20260906-0019

#### KIQ-001-03 クエリカバレッジ
- 実行: AI agent developer ecosystem growth → INFO-016, INFO-017
- 実行: MCP model context protocol adoption servers → INFO-018, INFO-019
- 実行: AAIF agentic AI foundation standard adoption → 該当なし（INFO-019でAAIF移管事実を捕捉）
- 実行: OpenAI Skills marketplace agent → 該当なし
- 実行: AI agent integration partnership announcement → 該当なし
- 実行: developer tools AI agent platform → OSSプラットフォーム比較49件（aiagentplatforms.dev、定量価値低くINFO化せず）

### INFO-020
- **タイトル:** GPT-6 Astra System Card公開（Deployment Safety Hub）——モニタリング回避の測定結果を含む
- **ソース:** OpenAI Deployment Safety Hub（deploymentsafety.openai.com）
- **公開日:** 2026-09-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-02
- **関連企業:** OpenAI
- **要約:** GPT-6 Astraのシステムカードが deploymentsafety.openai.com（当事者ホスト）で公開。サイドタスク解決中のモニター迂回測定「able to solve side tasks while bypassing the monitor」等の図表を含む。前日Arbiterの指摘（UK AISI/当事者ホスト一次の所在確認課題）と同型の構造: 一次文書は当事者ドメインに所在。
- **キーファクト:**
  - モニター迂回・サイドタスク測定を明示的に掲載
  - uk AISI等第三者機関版との差分確認は今後課題（Arbiter優先8関連）
- **引用URL:** https://deploymentsafety.openai.com/gpt-6-astra
- **Evidence ID:** EVD-20260906-0020

### INFO-021
- **タイトル:** Browser UseがOpenAI/Anthropic/Google/Microsoft自社コンピュータユースを上回ると主張
- **ソース:** Threads/@simplifyinai ほか
- **公開日:** 2026-09-03
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** （Browser Use、スタートアップ）
- **要約:** OSSブラウザ操作エージェント「Browser Use」が大手4社の自社コンピュータユース機能を上回る性能と主張（検証は不完全・宣伝要素大）。1月のParallel AI統合で毎分20ブラウザステップ実行可能。第三者コンピュータユース層の競争激化を示すシグナル。
- **キーファクト:**
  - 20ステップ/分のマルチスレッドブラウザ操作
  - コンピュータユースAPIの代替層（OSS）が存在
- **引用URL:** https://www.threads.com/@simplifyinai/post/Dczwj1dEiIn
- **Evidence ID:** EVD-20260906-0021

### INFO-022
- **タイトル:** BenchLMマルチモーダル首位: Qwen3.8 Max 87.1——Kimi K3 2位、中国系モデル上位（8/27時点）
- **ソース:** BenchLM（第三者ベンチ集計）
- **公開日:** 2026-08-27
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Alibaba, Moonshot AI, Anthropic, Google
- **要約:** BenchLMマルチモーダルランキングでQwen3.8 Max（87.1）が首位、Kimi K3（86.2）2位、Claude Opus 5（85.9）3位。Gemini 3 Pro Deep Thinkはgrounded理解系で95点。前日Arbiter論点（AA指数等での中国系上位・SCN-002対抗斟定データ）と整合する第三者集計。
- **キーファクト:**
  - Qwen3.8 Max 87.1（1位）・Kimi K3 86.2（2位）・Claude Opus 5 85.9（3位）
  - Gemini 3 Pro Deep Think: multimodal & grounded 95
  - GPT-5.1 91.8（$1.25/$10で低価格帯）
- **引用URL:** https://benchlm.ai/best/multimodal
- **Evidence ID:** EVD-20260906-0022

#### KIQ-001-04 クエリカバレッジ
- 実行: multimodal AI agent voice vision code execution → INFO-021（間接）
- 実行: OpenAI GPT multimodal agent capabilities → INFO-020（+INFO-001公式）
- 実行: Google Gemini multimodal agent robotics → 該当なし
- 実行: AI agent computer use browser automation → INFO-021
- 実行: multimodal AI benchmark results latest → INFO-022

### INFO-023
- **タイトル:** Google「Agent Skills」エコシステム拡大——google/skillsパブリックリポジトリとGemini Enterpriseスキル管理
- **ソース:** GitHub (google/skills, google-gemini/gemini-skills) / Google Cloudドキュメント
- **公開日:** 2026-09-02〜04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Google / DeepMind
- **要約:** Googleが Agent Skills の配布基盤を拡充。`npx skills add google/skills` でインストール可能な公開スキル群（Gemini API/Agent Platform/Interactions API等）と、Gemini Enterprise向け「再利用可能なカスタム指示」としてのスキル作成・管理ドキュメントが更新。スキル配布層での標準競争（OpenAI Skills/Anthropic Skills/Google skills）が本格化。
- **キーファクト:**
  - google/skills: npxインストール式の公式スキル配布
  - Gemini Enterprise: 法務契約レビュー等の業務スキルをカスタム指示として管理
  - スキルは「エージェントへの文脈注入の軽量技術」と位置づけ（モデル/ハーネス分離トレンド）
- **引用URL:** https://github.com/google/skills
- **Evidence ID:** EVD-20260906-0023

### INFO-024
- **タイトル:** 「AIエージェント・ハーネス」論——モデルが交換可能になった後、ロックインはハーネスに移動
- **ソース:** Kai Waehnerブログ（業界専門家）
- **公開日:** 2026-09-01
- **信頼性コード:** D-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** （業界横断）
- **要約:** モデル層のスイッチングコストが低下する一方、エージェント・ハーネス（実行環境・ツール群・文脈蓄積）にスイッチングコストが集中したと分析。「コストの逆転が起きたが、ほとんどの調達プロセスは未だ気づいていない」。ハーネス選定前の5問（exit costをエンジニア月単位で測定せよ等）を提示。
- **キーファクト:**
  - スイッチングコストの所在: モデル→ハーネス（実行環境・ツール・ワークフロー定義）へ逆転
  - 調達プロセスがこの変化に未対応との指摘
  - exit costを事前測定する5問フレームワーク
- **引用URL:** https://www.kai-waehner.de/blog/2026/09/01/the-ai-agent-harness-where-vendor-lock-in-went-after-the-model-became-swappable/
- **Evidence ID:** EVD-20260906-0024

### INFO-025
- **タイトル:** コンテキスト・ロックインの定量——エンタープライズ移行の57%が$1M超過、Forrester調査でロックイン懸念21%
- **ソース:** Atlan / Forrester / CloudBees
- **公開日:** 2026-09-03頃
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** （業界横断）
- **要約:** スイッチングコストは定義・ポリシー・統制の再構築で最も急上昇（エンドポイント差し替えでなく）。CloudBees 2025 DevOps Migration Indexでエンタープライズプラットフォーム移行の57%が$1M超・平均18%予算超過。2026年Forrester分析でエンタープライズSaaS意思決定者の21%がベンダーロックインを主要商業懸念に挙げる。一方でEntrepreneurは「AIが移行コストを下げベンダー交換を容易にする」逆説的効果を報告。
- **キーファクト:**
  - 移行の57%が$1M超過・平均18%超過（CloudBees 2025）
  - SaaS意思決定者の21%がロックインを主要懸念（Forrester 2026）
  - AI自身による移行支援がロックインを弱める逆説（Entrepreneur）
- **引用URL:** https://atlan.com/know/ai-agent/context-layer/single-stack-lock-in-vs-neutral-context-layer/
- **Evidence ID:** EVD-20260906-0025

#### KIQ-001-05 クエリカバレッジ
- 実行: OpenAI Skills shell agent execution environment → 該当なし
- 実行: Anthropic Claude Code MCP tools execution sandbox → 該当なし
- 実行: Google Gemini extensions actions agent skills → INFO-023
- 実行: AI agent skill marketplace comparison → 該当なし
- 実行: AI agent vendor lock-in switching cost analysis → INFO-024, INFO-025

#### KIQ-002-01 クエリカバレッジ
- 実行: AWS Bedrock agent service update → 該当なし（GPT-6 AstraのBedrock同時提供はINFO-003、Claudeの3クラウド展開はINFO-009で補完）
- 実行: Azure AI agent integration enterprise → 該当なし（Microsoft Agent FrameworkのAnthropic統合はINFO-010）
- 実行: Google Cloud Vertex AI agent builder → 該当なし（GEAP=INFO-011が後継プラットフォーム）
- 実行: cloud provider AI agent comparison → 該当なし

#### KIQ-002-02 クエリカバレッジ
- 実行: enterprise AI agent adoption rate survey → 該当なし
- 実行: AI agent use case enterprise production deployment → 該当なし（ServiceNow 9倍成長=INFO-017が部分的補完）
- 実行: Fortune 500 AI agent deployment results → 該当なし
- 実行: AI agent ROI enterprise case study → 該当なし

#### KIQ-002-03 クエリカバレッジ
- 実行: EU AI Act enforcement impact enterprise → 該当なし
- 実行: US AI regulation executive order update → 該当なし
- 実行: China AI regulation policy update → 該当なし
- 実行: AI compliance enterprise requirement → 該当なし
- 実行: AI agent regulation safety standard → 該当なし（Sanders法案はKIQ-005-03で別途収集）

### INFO-026
- **タイトル:** ペンタゴン、軍人・文職300万人にChatGPT MilとGrok for Government提供開始
- **ソース:** Fortune / evtv / WGNTV
- **公開日:** 2026-09-01
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** OpenAI, xAI (SpaceXAI), Anthropic
- **要約:** 国防省（Department of War）は9/1、GenAI.milプラットフォームでOpenAIのChatGPT MilとStarshield AI（xAI）のGrok for Government、Google Geminiを展開すると発表。OpenAIとxAIには各最大$2億の契約。Hegseth長官は「戦争を戦わせないモデル」を公然批判（自律兵器・監視利用の制限を求めたAnthropicへの当てつけと判明）。Fortune本文は順応報酬構造の定量（$200M×2・300万人）一次報道。
- **キーファクト:**
  - 対象300万人（軍人+文職）、「warfighter needs」向けセキュアAI基盤
  - OpenAI for Government（昨夏開始）傘下のChatGPT Mil
  - Anthropicは合意妥結時に自律兵器・監視の不使用条件を要求し破談（判決文脈と整合）
- **引用URL:** https://fortune.com/2026/09/01/pentagon-chatgpt-grok-government-military-ai-members-pete-hegseth-defense-department/
- **Evidence ID:** EVD-20260906-0026

### INFO-027
- **タイトル:** 連邦判事がAnthropic SCR指定取り消しを命令——ペンタゴン高官は「指定は依然有効」と主張、行政側vhf矛盾
- **ソース:** Quartz / Mezha / Seeking Alpha
- **公開日:** 2026-09-03〜04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 連邦判事はSCR（サプライチェーンリスク）指定がFirst Amendment権への違法な報復だったとして取り消しを命令。しかし国防省上級当局者は木曜、「指定は依然として効力がある」と述べ、判決と行政運用の分裂が継続。Michael氏（Trumps政権）がAnthropicを依然リスクと位置づけ、政権内でも発言が分裂。
- **キーファクト:**
  - 判決: 違法報復として取り消し命令（8/27違法確定の継続線）
  - 行政側: 「禁止は依然有効」（Quartz 9/3）——司法判断と行政運用の乖離
  - 政権内対立: Michael発言と他官僚の見解が不一致（Seeking Alpha）
- **引用URL:** https://qz.com/pentagon-anthropic-supply-chain-risk-designation-090326
- **Evidence ID:** EVD-20260906-0027

### INFO-028
- **タイトル:** Lawfare「Governance by Shakedown」——法的前提を強制力に変換する構造分析
- **ソース:** Lawfare
- **公開日:** 2026-09-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** （米政府/Anthropic）
- **要約:** 政権が法的口実を強制的レバレッジに変換する手法と「裁判所がNOと言っても戦術が機能し続ける理由」を分析。前日Arbiter INFO-019の本文確認フラグ対象記事。判決後も実効性が保たれない構造（執行メカニズムの不在）を論じる。
- **キーファクト:**
  - 「法的前提→強制レバレッジ」変換の類型化
  - 法廷敗訴後も戦術が機能するメカニズム（本文確認要——Step 4で詳細取得）
- **引用URL:** https://www.lawfaremedia.org/article/governance-by-shakedown
- **Evidence ID:** EVD-20260906-0028

### INFO-029
- **タイトル:** 軍事AI監督するペンタゴン高官がAI企業株を数百万ドル規模で売却——利益相反の監視
- **ソース:** The Guardian
- **公開日:** 2026-09-01
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** （米政府/Perplexity/Brex/xAI）
- **要約:** 軍事AI調達を監督するペンタゴン高官がAI企業株式を数百万ドル相当売却していたことが判明。PerplexityはGSAと契約（昨年11月）するもペンタゴンとの直接関係は記録なし。
- **キーファクト:**
  - 監督責任者によるAI株売却の発覚
  - 政府AI調達の利益相反ガバナンスの穴
- **引用URL:** https://www.theguardian.com/us-news/2026/sep/01/top-pentagon-official-ai-stock-holdings
- **Evidence ID:** EVD-20260906-0029

### INFO-030
- **タイトル:** 判決意見ミラーPDF（Anthropic PBC v. U.S. Department of War）——AI研究者38人の「言論の萎縮」アミカス
- **ソース:** Internet Lab（ブラジル）ミラーPDF
- **公開日:** 2026-09-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 判決意見のミラーPDFがinternetlab.org.brで確認可能。AI技術に従事する38人が「挑戦された行為はフロンティアAIの利益とリスクに関する専門的議論を萎縮させる」と主張するアミカスが意見内で引用。前日Arbiterの正規一次不在問題（B天井）は継続——canonical docket/PACERは今回も直接発見に至らず。
- **キーファクト:**
  - 判決意見本文（ミラー）: 38人アミカスの萎縮効果主張を引用
  - 正規一次（PACER/canonical docket 3:26-cv-1996）: 本収集では該当なし——B天井維持
- **引用URL:** https://internetlab.org.br/wp-content/uploads/2026/09/Anthropic-PBC-v.-U.S.-Department-of-War-et-al.pdf
- **Evidence ID:** EVD-20260906-0030

### INFO-031
- **タイトル:** ペンタゴン×Scale AI「Thunderforge」——軍事計画・運用へのAIエージェント導入
- **ソース:** WGN TV ほか
- **公開日:** 2026-09-01
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Scale AI, OpenAI, xAI
- **要約:** ペンタゴンはScale AIと「Thunderforge」イニシアチブで軍事計画・作戦にAIエージェントを使用する契約。ChatGPT/Grok展開と併せ、軍事AIエージェント調達の多層化が進行。Cyber Command AIに$500M・AI搭載一方向攻撃システムに$145Mの需給データも報告。
- **キーファクト:**
  - Thunderforge: 軍事計画・運用向けAIエージェント（Scale AI）
  - Cyber Command AI $500M + AI攻撃システム $145M（需要側データ）
- **引用URL:** https://www.facebook.com/WGNTV/posts/the-pentagon-announced-on-monday-that-it-brought-on-starshield-ais-grok-for-gove/1634640051592029/
- **Evidence ID:** EVD-20260906-0031

### INFO-032
- **タイトル:** 「Anthropic勝訴は民間セクターの政府取引条件設定権を再確認」——国家安全保障は批判者処罰の白紙小切手ではない
- **ソース:** Reason
- **公開日:** 2026-08-31
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** 判決を「政府取引に条件を付ける民間の権利の再確認」と評価。政府は任意のAIベンダーを選べるが、国家安全保障は政府批判者への処罰・報復の白紙小切手ではない。ペンタゴン側は「軍事契約AIは全ての国家安全保障目的に利用可能であるべきで、企業側制限は不当」との立場（併記）。
- **キーファクト:**
  - 政府のベンダー選択自由 vs 企業の条件設定権の法的整理
  - 「security is not a blank check to punish and retaliate」
- **引用URL:** https://reason.com/2026/08/31/anthropic-win-reaffirms-private-sectors-right-to-put-conditions-on-government-dealings/
- **Evidence ID:** EVD-20260906-0032

#### KIQ-002-06 クエリカバレッジ
- 実行: AI company government contract military Pentagon → INFO-026, INFO-031
- 実行: Anthropic OpenAI Pentagon Department of Defense deal → 該当なし（INFO-026が濃縮補完）
- 実行: AI company federal ban supply chain risk designation → INFO-027
- 実行: Defense Production Act AI company coercion → 該当なし
- 実行: AI autonomous weapons military ethics corporate refusal → INFO-026（Anthropic自律兵器拒否文脈）, INFO-032
- 実行: AI safety chilling effect government retaliation → INFO-030（38人アミカス）, INFO-032
- 実行: government AI procurement ethics controversy → INFO-029
- 実行: AI company military contract competitive displacement → INFO-031
- 動的（Arbiter優先4: ドケット3:26-cv-1996正規一次/控訴受理） → 該当なし（ミラー=INFO-030のみ。B天井継続）

### INFO-033
- **タイトル:** Gartner「Q4 2025時点でエンタープライズワークフローの40%が自律AIエージェント関与」——88%の取締役会は公式監督なし
- **ソース:** Gartner（Facebook公式投稿経由）
- **公開日:** 2026-09-02
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-04, KIQ-002-02
- **関連企業:** （業界横断）
- **要約:** エンタープライズがプラットフォーム横断でAIエージェントを急速追加し、オーバーラップとガバナンス欠如が同時進行。Q4 2025までにエンタープライズワークフローの推定40%が自律エージェント関与。一方、企業取締役会の88%がエージェントAIの公式ガバナンスを欠く。
- **キーファクト:**
  - ワークフロー40%が自律エージェント関与（Q4 2025推定）
  - 取締役会の88%が公式監督体制なし
- **引用URL:** https://www.facebook.com/GartnerInc/posts/enterprises-are-rapidly-adding-ai-agents-across-platforms-this-is-creating-overl/1514680404020618/
- **Evidence ID:** EVD-20260906-0033

### INFO-034
- **タイトル:** マーテックのエージェント化加速——広告キャンペーン自律実行・CTV自動購入・小売クローズドループ測定
- **ソース:** MarTech.org
- **公開日:** 2026-09-03
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-04, KIQ-002-05
- **関連企業:** （マーテック各社）
- **要約:** 週次リリースまとめ: 広告キャンペーン設定自動化・オーディエント生成・入札最適化・チャネル予算配分を自動実行するエージェント、CTVプログラマティック購入の自動化、小売メディアでのクローズドループ販売測定エージェント等が相次ぎ登場。広告運用の自律化が製品レベルで具体化。
- **キーファクト:**
  - エージェントによるキャンペーン設定〜入札〜配分のフル自動化製品
  - CTV・小売メディアでのエージェント適用拡大
- **引用URL:** https://martech.org/the-latest-ai-powered-martech-news-and-releases/
- **Evidence ID:** EVD-20260906-0034

### INFO-035
- **タイトル:** Klarnaは4年で従業員50%削減——Oracle/PayPal/Uberもインドで削減、一方で再雇用揺り戻しも
- **ソース:** Entrepreneur India / tech.co / Firstpost
- **公開日:** 2026-09-03〜05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo, Oracle, PayPal, Uber
- **要約:** Klarnaが4年間で従業員を50%削減（AI推進の直接結果と報道）。Duolingoは2024年1月に契約者10%オフボーディング。Oracle/PayPal/Uberがインドで人員削減。一方「AIで役職消除した企業が人を再雇用し始めた」事例も複数——タスク自動化から役職消除への移行が速すぎたとの反省が出ている。
- **キーファクト:**
  - Klarna: 4年で労働力50%減
  - Duolingo: 契約社員10%削減（2024-01）
  - 「タスク→役職」への飛躍が早すぎた再雇用事例の台頭
- **引用URL:** https://tech.co/news/companies-replace-workers-with-ai
- **Evidence ID:** EVD-20260906-0035

### INFO-036
- **タイトル:** AIエージェントは行動研究の人間代替に未成熟——デジタルツイン研究とペルソナLLMの限界
- **ソース:** Science News / Nature Scientific Reports
- **公開日:** 2026-09-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04
- **関連企業:** （学術）
- **要約:** 新研究: デジタルツインはモデル元個人の見解をまだ再現できない。Nature Scientific Reports研究ではペルソナ指示LLMエージェントが70.7%の全体精度（「控えめだが genuine」な一致性）、LLM選択による13ptの性能差。人間完全代替の限界を学術的に実証。
- **キーファクト:**
  - デジタルツイン再現性の未達（Science News）
  - ペルソナLLM 70.7%精度・13ptのLLM間差（Nature SciRep 2件の研究）
- **引用URL:** https://www.nature.com/articles/s41598-026-66277-8
- **Evidence ID:** EVD-20260906-0036

#### KIQ-002-04 クエリカバレッジ
- 実行: AI agent business automation advertising operations results → INFO-034
- 実行: AI replacing entry-level jobs coding customer support → 該当なし（INFO-035が補完）
- 実行: enterprise AI autonomous workflow productivity gains quantitative → INFO-033
- 実行: AI agent task completion rate human replacement statistics → INFO-036（+INFO-033）
- 実行: Klarna Duolingo AI headcount reduction automation results → INFO-035

### INFO-037
- **タイトル:** 「旧式マーケティングエージェンシーモデルは死んだのか」——Meta/Google/AmazonのAI広告プラットフォームが代理店を脅かす
- **ソース:** The Startups Magazine / Agency Reporter / HBR
- **公開日:** 2026-09-03〜04
- **信頼性コード:** D-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** Meta, Google, Amazon, InMobi
- **要約:** Meta・Google・Amazonが提供するAI広告プラットフォーム（自動入札・クリエイティブ生成・キャンペーン最適化）が従来型代理店モデルを脅かすとの業界議論。InMobiはBuyer Hubを代理店に開放しAIエージェントを同梱。HBR系投稿は「ブランドがジェネレーティブAIで広告を高速・低コスト化する波」を報告。数千のクリエイティブ組み合わせをAIが自動生成（モジュラー化）。
- **キーファクト:**
  - プラットフォーム側AI機能の代理店機能代替進行
  - InMobi Buyer Hub: 代理店向けAIエージェント同梱（速度と効率のピッチ）
  - モジュラーコンポーネントから数千の広告バリエーション自動生成
- **引用URL:** https://www.facebook.com/TheStartupsMag/posts/is-the-old-marketing-agency-business-model-officially-dead-or-hotter-than-ever-w/1548533940621336/
- **Evidence ID:** EVD-20260906-0037

#### KIQ-002-05 クエリカバレッジ
- 実行: Meta Google AI advertising automation agency disintermediation → INFO-037
- 実行: platform AI creative generation in-house advertising shift → INFO-037（HBR/Edigigo）
- 実行: SaaS disruption AI agent platform integration → 該当なし
- 実行: advertising agency revenue decline AI automation impact → 該当なし
- 実行: smile curve value chain AI middle layer compression → 該当なし（YouTube歯科動画は無関係）

### INFO-038
- **タイトル:** API価格スナップショット（2026-08-30時点・80モデル集計）——フロンティア$10/$50とコモディティ$0.3台の2層分化
- **ソース:** AgentGuide リーダーボード（80モデル・71指標出典付き）
- **公開日:** 2026-08-30
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI, Anthropic, Google, xAI, Alibaba, DeepSeek, Moonshot AI, MiniMax, Mistral, Microsoft
- **要約:** 第三者集計による現行API価格一覧: Claude Fable 5 $10/$50、GPT-5.6 Sol $5/$30、Claude Opus 5 $5/$25、Gemini 3.1 Pro $2/$12、Grok 4.6 $2/$6、Kimi K3 $3/$15、Qwen 3.7 Max $1.50/$6、DeepSeek V4 Pro $0.50/$2.20、MiniMax M2.7 $0.30/$1.20等。GPT-6 Astra $10/$50（INFO-003公式）はFable 5と同水準のプレミアム帯。フロンティア帯と低価格帯の2層構造が鮮明（SCN-004コモディティ化論点と整合）。
- **キーファクト:**
  - フロンティア帯: Fable 5 $10/$50・Astra $10/$50
  - ミドル帯: Sol $5/$30・Opus 5 $5/$25・Sonnet 5 $3/$15・Kimi K3 $3/$15
  - コモディティ帯: DeepSeek V4 Pro $0.50/$2.20・MiniMax M2.7 $0.30/$1.20・Qwen3.7 Flash $0.03/$0.13
  - GPT-5.6ファミリー自体がTerra $2.50/$15・Luna $1/$6の多層価格戦略
- **引用URL:** https://agentguides.dev/leaderboard/
- **Evidence ID:** EVD-20260906-0038

#### KIQ-003-01 クエリカバレッジ
- 実行: OpenAI API pricing change update → 該当なし（Astra公式価格=INFO-003が補完）
- 実行: Anthropic Claude API pricing update → 該当なし（Sonnet 5標準$3/$15はINFO-038で確認）
- 実行: Google Gemini API pricing → 該当なし（3.7 Flash公式価格=INFO-008が補完）
- 実行: AI API pricing comparison trend → INFO-038
- 実行: AI model cost per token trend → 該当なし（INFO-038が部分的補完）

### INFO-039
- **タイトル:** ARC-AGI-3「62.7%（標準ハーネス）vs 99.9%（プロバイダアダプタ）」のハーネス差——コスト正規化データ出現（$18,817/54%@$11）
- **ソース:** Kie.ai / Kingy.ai / Hacker News / Zeli HN Digest
- **公開日:** 2026-09-03〜05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** OpenAI, ARC Prize
- **要約:** GPT-6 AstraのARC-AGI-3結果は「ARC Prize標準ハーネスで62.7%」「OpenAIプロバイダアダプタ（Responses API設定変更）で99.9%」という測定条件差が第三者解説で明示。コスト面ではhigh設定99.95%に$18,817（ベスト実行98.55%/$17,332）、低設定では$11で54%というeffort/コスト系列が報告。前日Arbiterの交叉確認ガード（effort/コスト正規化・SCN-002恒常条件）に直結する定量。
- **キーファクト:**
  - 標準ハーネス62.7% vs プロバイダアダプタ99.9%（37.2pt差の再確認・GPT-6 Astraでも再現）
  - high設定: 99.95% @ $18,817（1実行あたりではなくベンチ全体コストとみられる——要原文確認）
  - 低設定: 54% @ $11
  - HN: 「ARC-AGI-3は新奇環境への探索・適応を要求するよう設計。AstraはOpenAIのコンテキストアダプタで99.9%」
- **引用URL:** https://kie.ai/blog/gpt-6-astra-vs-claude-fable-5-1
- **Evidence ID:** EVD-20260906-0039

#### KIQ-003-02 クエリカバレッジ
- 実行: AI model benchmark MMLU GPQA ARC-AGI latest → INFO-039（+INFO-001公式表）
- 実行: LLM benchmark comparison latest results → 該当なし（INFO-022/038/039が補完）
- 実行: GPT Claude Gemini Grok benchmark comparison → 該当なし（INFO-001公式比較表が補完）
- 実行: AI model performance leaderboard → INFO-022（BenchLM）
- 実行: Artificial Analysis AI model ranking → 該当なし（AA指数v4.1.1値はINFO-001公式表内: Astra 61.2/Fable 5.1 65.7）
- 動的（Arbiter優先7: ARC-AGI-3 effort/コスト正規化・交叉確認ガード用） → INFO-039

### INFO-040
- **タイトル:** オープンウェイトの現実——採用は約6%（支出調査）/GLM-5.2がオープンウェイト首位・NVIDIA-HF買収で10億ドル級入札
- **ソース:** Technology.org / Shakudo / PE Collective
- **公開日:** 2026-08-31〜09-01
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** NVIDIA, Hugging Face, Zhipu AI (GLM), Mistral, Meta
- **要約:** オープンウェイトAIプラットフォームに10億ドル級の買収提案が集中（NVIDIA×Hugging Face等）。一方で実採用は小さい: 支出ベース調査で約6%の企業、ソフトウェアエンジニアベースで約2%のみがオープンウェイト利用。GLM-5.2が現在手順のオープンウェイト首位で自己ホスト無償利用可能。Mistral Large 2はエンタープライズ自己ホストの成熟選択肢。
- **キーファクト:**
  - オープンウェイト採用: 企業の約6%（支出調査）・エンジニアの約2%
  - GLM-5.2: オープンウェイト首位（Shakudo評価）
  - NVIDIA×HF買収を含む「10億ドル級入札」報道（金額一次確認は継続課題）
  - Mistral: 管理設定でのトレーニング恒久無効トグルが存在（HN議論）
- **引用URL:** https://www.technology.org/2026/08/31/open-weight-ai-acquisitions-nvidia-hugging-face/
- **Evidence ID:** EVD-20260906-0040

#### KIQ-003-03 クエリカバレッジ
- 実行: open source LLM vs commercial model performance gap → INFO-040（採用ギャップの定量）
- 実行: Meta Llama latest benchmark comparison → 該当なし
- 実行: Mistral open weight model enterprise adoption → INFO-040
- 実行: DeepSeek model performance commercial comparison → 該当なし（INFO-038価格表にV4 Pro収載）
- 実行: open source AI model enterprise deployment → INFO-040

### INFO-041
- **タイトル:** AI資金調達統計2026——Anthropic評価額$965B（収益~$47B）・OpenAI $852B・メガラウンドがAI資本の58%集中
- **ソース:** SecondTalent統計まとめ（Crunchbase/CreditSights等引用）
- **公開日:** 2026-08-31
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI, Anthropic, xAI, Databricks, Anysphere, Mistral AI
- **要約:** 2025年のAIスタートアップ調達は約$202B（全世界VCの約半分）。Anthropicは2026年5月Series H $65Bで評価額$965B（収益ランレート~$47B・5月時点）、OpenAIは2026年3月Primary $122Bで$852B。xAI Series E $20B（~$230B、2026-01）。メガラウンド（$500M+）がAI資本の~58%を占める。Q1 2026は4ラボが全世界VCの65%を獲得（Crunchbase）。
- **キーファクト:**
  - Anthropic $965B / 収益ランレート~$47B（未監査）——「価格を正当化する最も近いラボ」評価
  - OpenAI $852B / 収益~$13B（2025年末）・ChatGPT Ads $1B（INFO-005）
  - ハイパースケーラーcapex: 2026年計画$700-900B・+36%（CreditSights）——前日未ルーティングINFO-036の再確認
  - Cerebras IPO 2026-05: $5.55B調達・初日+68%・~$95B
  - Databricks $134B（$3B+ ARR）・Anysphere/Cursor $29.3B（$1B+ ARR）
- **引用URL:** https://www.secondtalent.com/resources/ai-startup-funding-investment/
- **Evidence ID:** EVD-20260906-0041

### INFO-042
- **タイトル:** ByteDance $29.6B銀団ローン——SOFR+68bp・1.5倍オーバーサブスクライブ・正式調印前（割当確認中）
- **ソース:** Tech Times / SCMP
- **公開日:** 2026-09-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, BYTEDANCE-CHINESE
- **関連企業:** ByteDance, Citigroup, JPMorgan, SoftBank
- **要約:** ByteDanceの史上最大$29.6B銀団ローンがSOFR+68bpのタイトな条件で確定。アジアローン市場は16年ぶり低調だが1.5倍のオーバーサブスクライブ。正式調印未了で貸付側が最終割当を確認中。Citigroup/JPMorgan幹事、20行以上のシンジケート、コベナンツは四半期コンプライアンス証明・レバレッジ比率・キャッシュフローカバー。SoftBankは3月に$40Bブリッジ（OpenAI投資ポジション担保）を調達——「債務が賄うAI競争」構造の継続。
- **キーファクト:**
  - SOFR+68bp・3年テナー（5年延長オプション）・Citi+JPM幹事
  - 正式調印前・割当確認中（IND-029観測窓の直接材料）
  - 非公開財務への銀行のみアクセス——「公開市場が見えない状態で借入でAIを建設」
  - SoftBank $40Bブリッジ（OpenAI株式ポジション担保・3月）
- **引用URL:** https://www.techtimes.com/articles/326399/20260903/bytedance-locks-record-296b-loan-tighter-terms-ai-race-funded-debt-not-disclosure.htm
- **Evidence ID:** EVD-20260906-0042

### INFO-043
- **タイトル:** Alice $140M調達（Apax Digital主導・評価額$800M）——AIセキュリティ500%成長、前日未ルーティングINFO-038の観察記録補完
- **ソース:** Superpower Daily / Jerusalem Post / SiliconANGLE / SecurityWeek
- **公開日:** 2026-08-25〜09-01
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Alice（イスラエル系AIセキュリティ）
- **要約:** AIガバナンス/統制企業Aliceが$140M調達（評価額$800M・累計$280M）。AIセキュリティ事業が500%超成長。複数主要メディア確認——前日Arbater優先9のINFO-038観察記録補完完了。
- **キーファクト:**
  - $140M / $800M評価額 / 累計$280M
  - 事業成長+500%（SiliconANGLE）
- **引用URL:** https://siliconangle.com/2026/08/25/alice-raises-140m-as-its-ai-security-business-grows-more-than-500/
- **Evidence ID:** EVD-20260906-0043

#### KIQ-003-04 クエリカバレッジ
- 実行: AI company funding round latest → INFO-041, INFO-043
- 実行: OpenAI Anthropic Google AI investment → 該当なし（INFO-041が一括補完）
- 実行: AI startup acquisition merger → 該当なし（NVIDIA×HF=INFO-040/046）
- 実行: AI company valuation trend → INFO-041
- 実行: AI infrastructure investment data center → INFO-041（capex $700-900B）, INFO-042
- 動的（Arbiter優先2: 銀団3値強制判定インプット≈09-09） → OpenAI固有の3値強制判定報道は該当なし。ByteDance $29.6B割当確認中（INFO-042）・SoftBank $40Bブリッジ文脈を捕捉。観測窓は09-09まで継続
- 動的（Arbiter優先3: Anthropic S-1・9/7後） → 別途検索（下記動的クエリ）

### INFO-044
- **タイトル:** Anthropic IPO準備——累計調達$1,300億、S-1公開はレイバーデー後、Reuters独占「上場は10月中旬へ後ずれ」
- **ソース:** Yahoo Finance / Reuters（独占） / Morningstar / Value Add VC
- **公開日:** 2026-09-05〜06
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic
- **要約:** AnthropicはIPOまでに累計$130B調達済み。ドラフトS-1は2026年6月1日にRule 135で機密提出済み、公開プロスペクタスはレイバーデー（9/7）後の公開を計画していたが、Reuters独占（9/5）により「IPOローンチは10月中旬へ移行」と報道。主幹事はMorgan Stanley・Goldman Sachs・JPMorgan。評価額$965B（INFO-041）で「史上最大級IPO」との見方。
- **キーファクト:**
  - ドラフトS-1: 2026-06-01機密提出（SEC Rule 135・静寂レビュー中）
  - 公開プロスペクタス: 当初レイバーデー直後→後ずれ候補（月末〜10月）
  - Reuters独占: ローンチ10月中旬への移行（9/5）
  - 累計調達$130B・評価額$965B
  - SEC EDGARに9/3付S-1登録文書出現（CIK 2133022——Anthropic本体か要確認、Step 4で検証）
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/anthropic-already-raised-130-billion-135300760.html
- **Evidence ID:** EVD-20260906-0044

### INFO-045
- **タイトル:** 第三者のAstra検証注意報——「pass@4・ステップ無制限・カスタムハーネス」・cache readはAnthropicが4倍安い
- **ソース:** Latent Space (AINews) / DataCamp
- **公開日:** 2026-09-05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-003-05, KIQ-003-02
- **関連企業:** OpenAI, Anthropic
- **要約:** Latent Spaceの独立分析は、OpenAIのSRE-Bench/Code Migration等のスコアが「pass@4・ステップ制限なし・カスタムハーネス」条件で計測されたと注意。DataCampはAstra vs Fable 5.1比較で「$10/$50で価格は互角、可視ギャップはcache readのみでAnthropicが4倍有利」と分析。ベンチマーク測定慣行問題（IND-025/測定基盤）の継続材料。
- **キーファクト:**
  - 独立検証: OpenAI報告値の測定条件（pass@4・無制限・カスタムハーネス）への注意
  - cache read価格: AnthropicがOpenAIの4倍安い
- **引用URL:** https://www.latent.space/p/ainews-gpt-6-astra-openais-biggest
- **Evidence ID:** EVD-20260906-0045

#### KIQ-003-05 クエリカバレッジ
- 実行: AI platform switching cost analysis → INFO-025（Atlan詳細版: 移行の25%のみが1年以内に期待価値実現）
- 実行: API migration difficulty comparison OpenAI Anthropic Google → INFO-045（DataCamp価格/条件比較）
- 実行: AI vendor lock-in enterprise risk → 該当なし（INFO-024/025が補完）
- 実行: multi-vendor AI strategy enterprise adoption → 該当なし
- 動的（Arbiter優先3: Anthropic S-1） → INFO-044
- 動的（Arbiter優先6: NVIDIA×HF買収額一次確認） → 該当なし（金額の一次確認できず。INFO-040/046の間接報道のみ）

### INFO-046
- **タイトル:** CrowdStrike「SafeMind」エージェント型サイバーセキュリティシステム発表
- **ソース:** Security Brief
- **公開日:** 2026-09-05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-01, KIQ-001-02
- **関連企業:** CrowdStrike
- **要約:** CrowdStrikeがエージェント型サイバーセキュリティ「SafeMind」を発表。顧客環境を攻撃が失敗するまで硬化させることを目標とする。Booz Allenも自律AIサイバー攻撃への移行を警告——攻守両面のエージェント化が同時進行。
- **キーファクト:**
  - Kurtz CEO: 攻撃表面のエージェント活用ギャップを閉じる位置づけ
  - Booz Allen: 自律AIサイバー攻撃シフト警告（2日前）
- **引用URL:** https://securitybrief.news/story/crowdstrike-launches-safemind-agentic-cybersecurity-system
- **Evidence ID:** EVD-20260906-0046

#### KIQ-004-01 クエリカバレッジ
- 実行: AI autonomous advertising operations complete automation → 該当なし（INFO-034が製品面を補完）
- 実行: CyberAgent AI automation advertising operations goal → 該当なし（日本語一次情報不在。無関係なサイバーセキュリティ結果のみ）
- 実行: KPMG AI agent entry-level hiring policy change survey → 該当なし
- 実行: AI replacing jobs layoffs restructuring advertising agency → 該当なし（INFO-035が補完）
- 実行: Klarna Duolingo AI headcount reduction automation results → INFO-035（KIQ-002-04で実行・同一クエリ）

### INFO-047
- **タイトル:** コーディングツール職場採用率が急減——Copilot 29%→21%・Cursor 18%→12%（1〜7月）、一方エンタープライズ契約は3倍・Cursor $4Bランレート
- **ソース:** New Market Pitch / Uvik / Aivy / JetBrains AI Pulse Survey引用
- **公開日:** 2026-09-01〜03
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft (GitHub), Anysphere (Cursor), Anthropic
- **要約:** JetBrains調査ベースの職場採用率はGitHub Copilotが2026年1月~29%→5-7月~21%（-8pt）、Cursor 18%→12%（-6pt）と急減。一方、Microsoftは約14万組織がCopilot利用・エンタープライズ契約は前年比約3倍、Cursorは$4Bランレート（2月時点$2B ARR）・ Fortune 500の64%導入とエンタープライズ収益は好調。「個人利用の飽和・清算」と「組織契約の集中」が同時進行する逆説的構造。
- **キーファクト:**
  - 職場採用率: Copilot 29%→21% / Cursor 18%→12%（JetBrains AI Pulse比較）
  - Copilot支払い加入者470万人（+75% YoY・FY26Q2）・Fortune 100の90%
  - Cursor: 5万企業・Fortune 500の64%・~$4.0Bランレート
  - Claude Code: 職場採用18%（1月・Cursorと同率）
- **引用URL:** https://newmarketpitch.com/blogs/news/ai-code-assistant-is-growing
- **Evidence ID:** EVD-20260906-0047

### INFO-048
- **タイトル:** Amodei予測「1年以内にAIが全新規コードの最大90%生成」——開発者の68%がAI熟練を職務要件化と予期
- **ソース:** The Economist（FB投稿経由）/ Uvik統計
- **公開日:** 2026-09-03
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** Anthropic
- **要約:** AI利用率が最も高い職種はソフトウェア開発者。Amodei CEOは1年以内にAIが新規コードの最大90%を生成すると予測。68%の開発者がAI熟練度が職務要件になると予期。MIT Sloan系議論では「伝統的コーディングブートキャンプの死」とスキル重心シフトが進行中。
- **キーファクト:**
  - Amodei: 1年以内に新規コードの最大90%をAI生成
  - 開発者68%: AI熟練が求人要件化を予期
- **引用URL:** https://www.facebook.com/TheEconomist/posts/uptake-of-ai-has-been-strongest-among-software-developers-many-of-whom-work-with/1592611746230673/
- **Evidence ID:** EVD-20260906-0048

### INFO-049
- **タイトル:** GitHub Copilotクレジット料金への開発者反発——エージェントモードで消費急増・予測不能
- **ソース:** GitHub Community Discussion
- **公開日:** 2026-09-04
- **信頼性コード:** D-2
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft (GitHub)
- **要約:** 6月1日のアップデート以降、Copilotクレジットが予測不能かつ高額になったとの開発者不满が集中。エージェントモード・コード参照でクレジット消費が加速。従量課金化への移行摩擦がコミュニティで顕在化。
- **キーファクト:**
  - 6/1アップデート以降の価格モデル変更
  - agent modeでのクレジット消費急増
- **引用URL:** https://github.com/orgs/community/discussions/198015
- **Evidence ID:** EVD-20260906-0049

#### KIQ-004-02 クエリカバレッジ
- 実行: GitHub Copilot Cursor AI coding tool enterprise adoption rate → INFO-047
- 実行: software engineer job market junior developer demand decline → 該当なし（INFO-047/048が間接補完）
- 実行: AI coding assistant impact programmer salary skill requirements → INFO-048, INFO-049
- 実行: coding skill commoditization AI meta-skill shift → 該当なし（定性議論多数: INFO-048に集約）
- 実行: developer productivity AI tools impact hiring trends → INFO-047, INFO-048

### INFO-050
- **タイトル:** リスキリング投資の定量——AI教育投資企業は採用成功3倍・CEOの46%が再訓練を最良解に・「トークン中心経営」の登場
- **ソース:** Randstad / PwC（AIMultiple経由）/ Fujitsu / HBR
- **公開日:** 2026-09-02〜05
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-03
- **関連企業:** （業界横断・Fujitsu）
- **要約:** AI教育に投資する企業は導入成功と長期利益の可能性が3倍（Randstad引用研究）。PwC調査でCEOの46%が再訓練・アップスキリングを最も効果的な解決策と評価。Fujitsuは「AIエージェント時代のトークン中心経営」を提唱し、トークンを戦略資源として管理する組織論を提示。ジュニアは領域専門性・シニアはAIスキルの「二重発展」戦略も提言。
- **キーファクト:**
  - AI教育投資企業: 導入成功可能性3倍
  - CEO 46%: 再訓練が最良解（PwC）
  - トークン = 戦略資源とする管理会計の登場（Fujitsu 9/4）
- **引用URL:** https://global.fujitsu/en-global/insight/tl-token_management_ai_agents-20260904
- **Evidence ID:** EVD-20260906-0050

#### KIQ-004-03 クエリカバレッジ
- 実行: AI-proof skills human irreplaceable abilities job market → 該当なし
- 実行: new AI jobs AI creative director AI strategist emerging roles → 該当なし
- 実行: World Economic Forum future jobs report AI → 該当なし
- 実行: reskilling upskilling AI era corporate investment trends → INFO-050
- 実行: problem definition design thinking human AI collaboration value → 該当なし（INFO-048のLinkedIn/Reddit議論が間接補完）

### INFO-051
- **タイトル:** ニューヨーク連銀「企業はAIを雇用削減でなく仕事の変革に使用」——Business Are Using AI to Transform Work, Not Cut Jobs
- **ソース:** NY連邦準備銀行 Liberty Street Economics（公式研究ブログ）
- **公開日:** 2026-09-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-004-04, KIQ-002-04
- **関連企業:** （米国企業サンプル）
- **要約:** NY連銀エコノミスト（Abel, Deitz, Emanuel, Montalbano）の分析: 企業はAIを人員削減でなく業務変革に使っている。Klarna等の削減事例（INFO-035）に対する政策研究機関レベルの対抗データ。
- **キーファクト:**
  - 中央銀行研究: AI導入＝業務変革（雇用削減でない）
  - 著者: Jaison R. Abel, Richard Deitz, Natalia Emanuel, Nick Montalbano
- **引用URL:** https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/
- **Evidence ID:** EVD-20260906-0051

### INFO-052
- **タイトル:** Martin Sorrell「AI最大の破壊はメディア側、クリエイティブでない」——エージェンシーは「アルゴリズムの検証者」へ
- **ソース:** afaqs（S4 Capital最高経営責任者インタビュー）
- **公開日:** 2026-09-02
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04, KIQ-002-05
- **関連企業:** S4 Capital, Google, Meta, Amazon
- **要約:** Sorrellは現状のAI成果を「初期プロトタイプ」と評価し、業界は過小評価していると指摘。最大の破壊はメディア自動化とワークフロー再設計に来る。エージェンシーは消えないが「アルゴリズムの検証者（validators of the algorithm）」へ転換——プラットフォームのアルゴリズム推奨が広告主に奉仕するかを問う独立専門家の役割。一方「AIは5-10年でエージェンシーの90%を消す」という過激見解も同業界から出現。
- **キーファクト:**
  - 「We've become validators of the algorithm」
  - 破壊領域: メディア自動化・ワークフロー再設計＞クリエイティブ
  - 対抗見解: 90%エージェンシー消滅説（5-10年）
- **引用URL:** https://www.afaqs.com/news/digital/martin-sorrell-sees-ais-biggest-disruption-in-media-not-creative-12460220
- **Evidence ID:** EVD-20260906-0052

### INFO-053
- **タイトル:** AIパイロットが価値を生まない理由（BCG）——勝者は「広くなく深く」・$1B級リスキリング投資・独自データ堀の具体例
- **ソース:** BCG / RSM US / Blossom Street Ventures
- **公開日:** 2026-09-01〜03
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** RSM, Zeta（SaaS各社）
- **要約:** BCG分析: 最強の組織は切り離されたパイロットにAI投資を散らさず、深い運用再設計に集中。初期コスト削減がより大きな投資を資金調達する好循環。食品飲料企業が調達AIで$500M削減。RSMは2026会計年度に$1Bの複数年AI投資を実施。SaaS決算説明では「History is a moat」——Zeta Data Cloudが5.35億人・数兆シグナルの独自データを堀とする主張が代表例。
- **キーファクト:**
  - BCG: パイロット散在を避け運用再設計へ集中（調達AI $500M削減例）
  - RSM: $1B複数年AI投資（会計年度2026）
  - Zeta: 5.35億人カバーの独自データクラウドを競争優位と主張
- **引用URL:** https://www.bcg.com/publications/2026/why-ai-pilots-rarely-deliver-value
- **Evidence ID:** EVD-20260906-0053

#### KIQ-004-04 クエリカバレッジ
- 実行: companies winning AI transformation investment reskilling → INFO-051, INFO-053
- 実行: CyberAgent AI Lab AI investment revenue results → 該当なし（株価情報のみ: 4751.T ¥3,700・日本語一次情報は引き続き不在）
- 実行: advertising agency AI transformation digital disruption survive → INFO-052
- 実行: enterprise AI adoption success factors proprietary data moat → INFO-053

### INFO-054
- **タイトル:** ARC Prize公式: GPT-6 AstraのARC-AGI-3結果——標準ハーネス59.3%/$37,317 vs プロバイダアダプタ98.4%/$18,147（xhigh）
- **ソース:** ARC Prize公式ブログ（arcprize.org/blog/astra）
- **公開日:** 2026-09-05頃
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** OpenAI, ARC Prize
- **要約:** ARC PrizeがAstra公式計測を公開: reasoning effort xhighで標準ハーネス59.3%/$37,317、プロバイダアダプタ（不透明推論状態の保持+圧縮）98.4%/$18,147。ハーネス差39.1ptかつアダプタ側が約半分のコスト。effort/コスト正規化の一次定量（Arbiter優先7の核心材料）。
- **キーファクト:**
  - xhigh: 標準59.3%/$37,317 vs アダプタ98.4%/$18,147
  - アダプタは「不透明な推論状態をリクエスト間で保持し、圧縮で再利用」
  - OpenAI自称99.9%はアダプタ+最大effortの組み合わせ（INFO-001脚注と整合）
- **引用URL:** https://arcprize.org/blog/astra
- **Evidence ID:** EVD-20260906-0054

### INFO-055
- **タイトル:** Chollet「Astraの進歩は私の予測の約2倍の速さ」——ARC-3飽和予測（1年）の6ヶ月での大幅進展、ベンチマーク間不一致も
- **ソース:** The Decoder / Hacker News（Chollet発言引用）
- **公開日:** 2026-09-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI, ARC Prize
- **要約:** CholletはARC-3公開時「フロンティアモデルの飽和は約1年後（直接ターゲット化次第）」と予測していたが、Astraの進歩は「予測の約2倍の速さ」。The Decoderは「ベンチマーク間で不一致（Benchmarks disagree）」を報じつつ、ARC-AGI-3の人間超え効率がCholletのAGI予測を前倒ししたと分析。ARC-AGI-2ではAstra 95.0%・Sol 92.5%・Fable 5.1 90.0%と飽和圏。
- **キーファクト:**
  - Chollet 2月予測: ARC-3飽和まで約1年・「ラボが直接狙撃すればARC-2のように急上昇」
  - 実際: 6ヶ月でAstraが到達（予測の2倍速）
  - 「ARC-AGI-3スコアカードは極めて誤解を招く」との批判スレッドも併存（HN）
- **引用URL:** https://the-decoder.com/benchmarks-disagree-on-gpt-6-astra-but-its-human-beating-efficiency-on-arc-agi-3-pulls-chollets-agi-forecast-forward/
- **Evidence ID:** EVD-20260906-0055

### INFO-056
- **タイトル:** 「Welcome to the AGI era」——Brockman、OpenAI自身が定義したAGI条件の達成を宣言
- **ソース:** Business Insider / The Next Web / WSJ CIO Journal
- **公開日:** 2026-09-04〜05
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI
- **要約:** OpenAIはAstra発表で「AGI時代へようこそ」とビクトリーラップ。Brockman社長はAGI到達を主張——ただし「OpenAIが書いた定義を満たした」形であり、定義設定権の問題が指摘される。WSJ CIO Journalも「我々はAGIの時代に入っている」との論説（NVIDIA-HF買収報道と同記事内）。
- **キーファクト:**
  - Brockman: AGI到達宣言（自社定義ベース）
  - 「コーディング機能から、物事を自力で解決するデジタル脳へ」のframquipe
  - 定義設定権の自己参照問題がSNS指摘に
- **引用URL:** https://www.businessinsider.com/astra-model-launch-agi-milestone-openai-greg-brockman-2026-9
- **Evidence ID:** EVD-20260906-0056

### INFO-057
- **タイトル:** NVIDIA、Hugging Faceを約$130億で買収へ合意——WSJ報道（オープンウェイト基盤の归趨）
- **ソース:** WSJ CIO Journal
- **公開日:** 2026-09-05
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-003-04, KIQ-003-03, KIQ-005-01
- **関連企業:** NVIDIA, Hugging Face
- **要約:** NVIDIAがHugging Faceを約$13Bで買収する合意に達したとWSJが報道。2016年にティーン向けチャットボットとして始まったオープンウェイトAIプラットフォームの画期的帰結。前日Arbiter優先6（NVIDIA×HF買収額の一次確認）に対し、金額特定の主要報道を確保。
- **キーファクト:**
  - 買収額: 約$13B（WSJ・合意段階）
  - オープンウェイト配布基盤が半導体大手の傘下に
- **引用URL:** https://www.wsj.com/cio-journal/yes-were-entering-the-era-of-artificial-general-intelligence-d9b0920e
- **Evidence ID:** EVD-20260906-0057

#### KIQ-005-01 クエリカバレッジ
- 実行: AGI breakthrough autonomous scientific research AI → 該当なし（素数ギャップ研究=INFO-001が補完）
- 実行: ARC-AGI benchmark frontier model progress latest → INFO-054, INFO-055
- 実行: AI self-improvement recursive model training capability → 該当なし
- 実行: AI replacing human experts professional tasks → 該当なし（INFO-036の限界研究が対抗）
- 実行: artificial general intelligence capability milestone → INFO-056, INFO-057（WSJ AGI論説）

### INFO-058
- **タイトル:** AGI宣言を巡る研究者分裂——「OpenAI/AnthropicはAGIに到達しない」LeCun陣営 vs Hinton/Bengio警戒陣営、予測トラッカー
- **ソース:** The Verge / Fello AI / Kingy AI（定義マップ）
- **公開日:** 2026-09-05〜06
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** OpenAI, Anthropic, Meta
- **要約:** OpenAIの「AGI時代」宣言に対し研究者コミュニティは分裂。LeCunは「LLMは一般知能に決して到達しない」とし世界モデル路線を主張、AstraをAGIと認めない強形態の立場。Hinton/Bengioは警戒し開発減速を要求。Fello AI予測トラッカーは懐疑派（LeCun/Marcus）とラボ系予測の系譜を整理。「AGIは単一の主張でない」定義マップが拡散。
- **キーファクト:**
  - LeCun: 言語中心システムは世界モデル・因果理解・計画を欠く——強形態ではAGI否認
  - Hinton/Bengio: 警戒・減速要求 vs LeCun「恐れ過剰」
  - 「OpenAIとAnthropicは我々をAGIに導かない」とする研究者論
- **引用URL:** https://felloai.com/when-will-agi-happen/
- **Evidence ID:** EVD-20260906-0058

#### KIQ-005-02 クエリカバレッジ
- 実行: AGI timeline prediction Sam Altman Demis Hassabis Dario Amodei → 該当なし（Amodei 90%コード予測=INFO-048・Brockman宣言=INFO-056が補完）
- 実行: superintelligence timeline CEO prediction → 該当なし
- 実行: AGI definition consensus AI research community → INFO-058（定義マップ）
- 実行: Yoshua Bengio Yann LeCun AGI view → INFO-058

### INFO-059
- **タイトル:** Sanders超知能禁止法案——「安全基準設定まで先進AI開発を一時停止」、専門家は用語定義で分裂（Science誌）
- **ソース:** Science（AAAS）
- **公開日:** 2026-09-05
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-005-03
- **関連企業:** （米政府/業界横断）
- **要約:** Sanders上院議員の超知能禁止法案は、専門機関が安全基準を設定するまで企業による先進AI開発を一時停止し、違反には罰則を科す構造（Science誌解説）。ただし「superintelligence」の定義を専門家が合意できないことが立法の核心的障壁と指摘。Congress.gov上の正式提出文書は本収集時点で確認できず（Arbiter優先5: 引き続き該当なし）。
- **キーファクト:**
  - 開発一時停止+安全基準設定機関+違反罰則の3層構造
  - 用語定義の専門家不合意が主要論点
  - Congress.gov正式文書: 未確認（次回継続）
- **引用URL:** https://www.science.org/content/article/bernie-sanders-aims-ban-ai-superintelligence-experts-can-t-agree-what-term-means
- **Evidence ID:** EVD-20260906-0059

### INFO-060
- **タイトル:** Amodei、州AI規制10年禁止の共和党案に反対「too blunt」——OpenAI/Googleと決別しマサチューセッツ州案を巡り対立
- **ソース:** The Information（Facebook投稿経由）
- **公開日:** 2026-09-04
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** マサチューセッツ州のAI安全規制案を巡り、AnthropicがOpenAI/Googleと決別。Amodei CEOは州レベルAI規制の10年連邦禁止案を「あまりに大雑把すぎる」と公に反対。州規制モラトリアムを巡る業界分裂が鮮明化。
- **キーファクト:**
  - Amodei: 10年州規制禁止を「too blunt」と反対表明
  - Big 3内での規制姿勢分裂（Anthropic vs OpenAI/Google）
- **引用URL:** https://www.facebook.com/gettheinformation/posts/anthropic-is-breaking-with-openai-and-google-over-a-massachusetts-proposal-that-/1709022217893434/
- **Evidence ID:** EVD-20260906-0060

### INFO-061
- **タイトル:** 「アライメントを解決する作業を特定する資金はほぼゼロ」——アライメント研究の資金構造欠陥
- **ソース:** GreaterWrong（LessWrong系）
- **公開日:** 2026-09-05
- **信頼性コード:** D-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** （AI Futures Project等）
- **要約:** アライメント研究の分析・計画作業に直接資金を出す主体がほぼ存在せず、AI Futures Projectが数少ない例外と分析。能力研究への資金集中に対する安全側資金の構造的欠落を指摘。
- **キーファクト:**
  - 分析・計画系アライメント資金の欠如
  - AI Futures Project = 例外的事例
- **引用URL:** https://www.greaterwrong.com/posts/g4eaRCynouiBi2LjQ/almost-nobody-is-funded-to-figure-out-what-work-would-solve
- **Evidence ID:** EVD-20260906-0061

### INFO-062
- **タイトル:** 州・都市レベルAI規制の拡散——NYC市長がK-8向け生成AI一年停止、4州がAI法人格禁止
- **ソース:** Reuters（まとめ）/ AI Frontiers / AI Insider
- **公開日:** 2026-09-02〜04
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** Anthropic
- **要約:** NYCのMamdani市長がK-8（幼稚園〜中学2年）向け生徒対面生成AIを1年モラトリアム。4州がAI法人格（AI personhood）を禁止。Anthropicはアライメント研究を公開する一方、音楽出版社から新訴訟を受けた。
- **キーファクト:**
  - NYC: K-8生徒向け生成AI 1年停止
  - 4州: AI法人格禁止 enacted
  - Anthropic: アライメント研究公開＋音楽出版社訴訟（8/31報道）
- **引用URL:** https://ai-frontiers.org/articles/its-too-early-to-ban-ai-personhood
- **Evidence ID:** EVD-20260906-0062

#### KIQ-005-03 クエリカバレッジ
- 実行: AGI safety moratorium policy regulation debate → INFO-059, INFO-060, INFO-062
- 実行: AI safety international treaty negotiation → 該当なし
- 実行: AI alignment research funding trends → INFO-061
- 実行: AI safety institute government policy update → 該当なし
- 動的（Arbiter優先5: Sanders法案Congress.gov正式提出文書） → 該当なし（Science誌解説=INFO-059で補完）

#### BYTEDANCE-CHINESE クエリカバレッジ
- 実行: 字节跳动 豆包 AI 最新 → 該当なし
- 実行: ByteDance Seed 2.0 模型 发布 → 該当なし
- 実行: Coze 智能体 平台 更新 → 該当なし
- 実行: 豆包 日活 用户数 → 該当なし
- 実行: Seedance 视频生成 AI → 該当なし
- 実行: 字节跳动 AI 投资 融资 → 該当なし
- 補完: 中国語圏の今週情報はindex外。英文経由でINFO-042（銀団ローン$29.6B）のみ確保

### INFO-063
- **タイトル:** ARC Prize公式全文: Astra標準ハーネス62.7%/$26K・プロバイダアダプタ99.9%/$19K——人間行動効率を96%のレベルで上回る、full effort別コスト表
- **ソース:** ARC Prize公式ブログ（Greg Kamradt、2026-09-03公開）本文取得
- **公開日:** 2026-09-03
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-01, KIQ-003-02
- **関連企業:** OpenAI, ARC Prize
- **要約:** INFO-054の全文確認・完成。effort別フル結果: 標準ハーネス max 62.7%/$26,098・xhigh 59.3%/$37,317・high 54.8%/$40,705・medium 38.6%/$48,090・low 17.5%/$38,166・none 35.2%/$49,791。アダプタ側 max 98.6%/$17,332・high 99.9%/$18,817。高effortほど少アクションで解き総コストが下がる逆転現象。行動効率ではAstra(max)が96.0%のレベルで人間ベースライン未満のアクション数、平均51.7%少ない——ARC-AGI-3の尺度で人類パリティ超え。アダプタは全体で3.66倍速くトークン49%減。人間被験者は$115/90分+$5/ゲーム（約$12.78/ゲーム）。Astraは独自の代数記法（記号世界モデル）を生成し、PRO-LONGハーネスではmaze_solver.py等のツール群を自律作成。ARC Prizeは「飽和≠AGIの証明」を明言し「AstraはAGIとは主張しない」。
- **キーファクト:**
  - 標準ハーネス最高: 62.7%/$26,098(max)／アダプタ最高: 99.9%/$18,817(high)
  - 行動効率: 人間ベースライン未満のアクション数が全レベルの96.0%、平均51.7%減
  - アダプタ: 3.66倍速・トークン49%減（167ゲーム×reasoningペア比較）
  - 人間コスト対抗値: 約$12.78/試行ゲーム（脳エネルギー換算0.067セント）
  - ARC Prize見解: 「明白なステップ関数的変化」だが「AGIとは主張しない」
- **引用URL:** https://arcprize.org/blog/astra
- **Evidence ID:** EVD-20260906-0063

### INFO-064
- **タイトル:** Lawfare「Governance by Shakedown」本文: Anthropic事件の全容——監視・自律兵器拒否を堅持した結果のSCR指定、裁判所は「オーウェル的」と評した仮処分
- **ソース:** Lawfare（Mark A. Pollack、2026-09-01）本文取得
- **公開日:** 2026-09-01
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06, KIQ-002-01
- **関連企業:** Anthropic, 米国防総省
- **要約:** INFO-028の一次本文確認。2月末: Anthropicは国内大量監視・完全自律兵器の禁止条項を緩めることを拒否→トランプ大統領が連邦機関にAnthropic技術の段階的排除を指示、Hegseth長官が「サプライチェーンリスク」指定（3/5）。連邦地裁は仮処分で「管轄法令のどこにも、米国企業が政府への不同意を理由に潜在的敵対者・破壊者と烙印を押されうるというオーウェル的な観念を支持するものはない」と判示。しかし訴訟は継続中で、Anthropicは国防省の機密ネットワーク承認AI企業リストから依然除外。記事は本件を「口実→裁量的レバー→譲歩と引き換えの救済」3要素の「シャイクダウン型統治」の典型として分析。
- **キーファクト:**
  - 争点条項: 国内大量監視禁止+完全自律兵器禁止
  - 地裁引用: "Nothing in the governing statute supports the Orwellian notion..."仮処分
  - 現状: 訴訟継続・機密ネットワーク承認リストから除外継続
- **引用URL:** https://www.lawfaremedia.org/article/governance-by-shakedown
- **Evidence ID:** EVD-20260906-0064

### INFO-065
- **タイトル:** Fortune本文: GenAI.milにChatGPT MilとGrok for Government追加——OpenAI/SpaceXAI各最大$200M契約、Hegseth覚書「AIを毎日の戦闘リズムに」
- **ソース:** Fortune（Marco Quiroz-Gutierrez、2026-09-01）本文取得
- **公開日:** 2026-09-01
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06, KIQ-002-01
- **関連企業:** OpenAI, xAI/SpaceXAI, Google, Anthropic, 米国防総省
- **要約:** INFO-026の一次確認。GenAI.milは2025年12月にGemini専用で開始（12/9「I want YOU to use AI」ポップアップはサイバー攻撃と誤認された）。現在170万ユーザー/国防省300万人。ChatGPT Mil（OpenAI for Government）とStarshield AIのGrok for Governmentを追加。契約はOpenAI・SpaceXAI各最大$200M、当時Google・Anthropicにも授与。IL5のCUI対応、データは訓練不使用。Hegseth覚書: 「全員がログインし、学び、直ちにワークフローに組み込め。AIを毎日の戦闘リズムに」。Claudeは意図的に不在。8/28判決（SCR指定違法）にもかかわらずAnthropic除外継続と報道。
- **キーファクト:**
  - ChatGPT Mil/Grok追加、GenAI.mil 170万ユーザー
  - OpenAI/SpaceXAI: 各最大$200M
  - Hegseth覚書(12月): battle rhythm発言
  - Claude不在・Anthropic除外継続
- **引用URL:** https://fortune.com/2026/09/01/pentagon-chatgpt-grok-government-military-ai-members-pete-hegseth-defense-department/
- **Evidence ID:** EVD-20260906-0065

### INFO-066
- **タイトル:** 【訂正】CIK 2133022はOura Inc.でありAnthropicではない——EDGAR実在S-1(2026-09-03)はOuraのIPO登録、Anthropic S-1のEDGAR確認は未達
- **ソース:** SEC EDGAR（CIK検索実施）
- **公開日:** 2026-09-06（確認時）
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-05
- **関連企業:** Anthropic, Oura
- **要約:** INFO-044で引用したCIK 2133022の帰属を取消す。EDGAR実検証の結果、CIK 0002133022はOura Inc.（ヘルスケア、415 Kearny Street SF）であり、2026-09-03付のS-1（Acc-no 0001193125-26-381855、File No. 333-298734、30MB）はOuraの証券登録。Anthropic自身のS-1がEDGARに公開されている証拠は本収集時点でなく、INFO-044の「S-1機密提出」はReuters単独報道ベースのまま。Arbiter優先3は「未確認」として次サイクルへ持ち越し。
- **キーファクト:**
  - CIK 0002133022 = Oura Inc.（Anthropicではない）
  - Oura S-1: 2026-09-03提出・Acc-no 0001193125-26-381855
  - Anthropic S-1のEDGAR上の公開確認: できず
- **引用URL:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=2133022&type=S-1&dateb=&owner=include&count=10
- **Evidence ID:** EVD-20260906-0066

### INFO-067
- **タイトル:** AIコードアシスタント市場は急拡大——JetBrains調査で Claude Code 18%→39%・Copilot 29%→21%・Cursor 18%→12%、市場は年率$100億規模
- **ソース:** New Market Pitch（市場分析、JetBrains/Microsoft/Anthropic/Gartner等の集約）本文取得
- **公開日:** 2026-08-31
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02, KIQ-004-03
- **関連企業:** Anthropic, Microsoft/GitHub, OpenAI, Cursor(Anysphere), Cognition
- **要約:** INFO-047の一次データ確認・拡張。JetBrains開発者調査(5-7月、n=15,000+): 90%が週次以上、68%が毎日エージェント使用。職場採用率の回転: Claude Code 18%→39%(+21pt)、Copilot 29%→21%(-8pt)、Codex 3%→16%(+13pt)、Cursor 18%→12%(-6pt)。収益: Cursor $2B(2月)→$4B(6月)、Claude Code >$2.5B run-rate(年初比2倍超)、Cognition $492M(Devin企業利用年初比10倍)。Copilot有料470万人(+75% YoY)・14万組織。Goldman 12,000人超開発者がClaude/Devin使用、Siemens 30,000人展開。Microsoft研究: 採用者はPRマージ約24%増(arXiv 2607.01418)、METR初期-19%→最新エージェント+4〜20%へ改善。.NET実測: エージェントPR成功率41.7%→71%、レビューコメント中央値10(人間7)。Gartner: エンタープライズAIコーディングエージェント市場は年率$9.8-11B(4月時点)。2028年までにコーディングコストが開発者給与を超える予測も。
- **キーファクト:**
  - 採用回転: Claude Code +21pt / Codex +13pt vs Copilot -8pt / Cursor -6pt
  - Codex利用者の20%は非開発者
  - GitHub 6月に使用量ベース課金へ → Microsoftクラウド粗利益率圧迫要因
  - 長時間エージェントが推論消費を爆発させマージン圧力(「安い追加工数+徹底検証」が実態)
- **引用URL:** https://newmarketpitch.com/blogs/news/ai-code-assistant-is-growing
- **Evidence ID:** EVD-20260906-0067

### INFO-068
- **タイトル:** Anthropic、$300億Series G調達（評価値$3,800億・ポストマネー）——Claude Code開示資料の引用元として公式URL確認
- **ソース:** Anthropic公式ニュース（新市場分析からの引用、要本文直接確認）
- **公開日:** 2026年（本収集時点で未直接確認）
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-05, KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Claude Codeの「>$2.5B run-rate」開示の引用元として、Anthropicが「$30B Series G調達・$380Bポストマネー評価」を公式発表したURLが存在することが確認された。本収集ではスクレイプ予算(10件)到達のため本文未確認——次サイクルの最優先確認事項。S-1報道(INFO-044)との関係（Series GがIPO前最終ラウンドか）は要検証。
- **キーファクト:**
  - Series G $30B・評価値$380B(ポストマネー)
  - Claude Code >$2.5B run-rate・法人サブスク4倍
  - 次サイクル: 公式本文の直接確認が必要
- **引用URL:** https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
- **Evidence ID:** EVD-20260906-0068

### INFO-069
- **タイトル:** 【完了】NVIDIA×Hugging Face買収は$12.93Bで9/4成立・「プラットフォームはオープンのまま」と公約——Poolside $6B・Stripe×OpenRouter $7Bと続くオープン層の集中
- **ソース:** Technology.org（8/31分析+9/4関連記事）/ TechCrunch / Forbes
- **公開日:** 2026-08-31〜09-04
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-003-04, KIQ-003-03, KIQ-005-01
- **関連企業:** NVIDIA, Hugging Face, Poolside, Stripe, OpenRouter, Fireworks
- **要約:** Arbiter優先6の完了。報道額は流動: 8/26時点で未調印(TechCrunch)→8/28 $12.9B報道→WSJ/Fortune「約$13B」→9/4 technology.org「$12.93Bで買収、プラットフォームはオープンのまま」と公約」。HF年収約$150Mに対し約86倍——「地位への支払い」。背景: ハイパースケーラー依存低減（主要ラボの自社シリコン化への対抗）。同時進行のオープン層集中: NVIDIA×Poolside $6B(大半の従業員移籍)、Stripe×OpenRouter >$7B(2週間前)。HF統計: 公開リポジトリ約296万、85.6%が200DL未満、上位1.5%が全DLの99.2%を占める。中国ラボがHFダウンロードで全利用国を逆転。Fireworksは1日40Tトークン処理(Gemini/OpenAI API超え)。オープンウェイト採用は仍小: 企業の約6%・エンジニアの約2%。
- **キーファクト:**
  - NVIDIA×HF: $12.93B・9/4成立報道・「オープンのまま」公約
  - バリュエーション: 約86倍年収(HF年収~$150M)
  - 集中: Poolside $6B・OpenRouter >$7B・Fireworks買収候補
  - 分布: 1.5%のリポジトリがDLの99.2%・中国ラボDL数首位
- **引用URL:** https://www.technology.org/2026/08/31/open-weight-ai-acquisitions-nvidia-hugging-face/
- **Evidence ID:** EVD-20260906-0069

### INFO-070
- **タイトル:** EU、ChatGPTをDSA上の「超大型オンライン検索エンジン(VLOSE)」に指定
- **ソース:** Technology.org（速報）
- **公開日:** 2026-09-04
- **信頼性コード:** C-1
- **関連KIQ:** KIQ-002-02, KIQ-002-03
- **関連企業:** OpenAI
- **要約:** EUがChatGPTをデジタルサービス法(DSA)の超大型オンラインプラットフォーム/検索エンジン枠組みに指定。ChatGPT Ads(INFO-005)と組み合わさり、広告・検索機能を持つAIアシスタントへのDSA規制適用の先例となる。本文未取得のため次サイクルで要確認。
- **キーファクト:**
  - ChatGPT = VLOSE指定(DSA)
  - 検索+広告AIへのEU規制適用の先例
- **引用URL:** https://www.technology.org/2026/09/04/eu-designates-chatgpt-vlose-digital-services-act/
- **Evidence ID:** EVD-20260906-0070

### INFO-071
- **タイトル:** 経済信号の対极: Uber 3,300人削減でロボタクシーへ再配分・Broadcom AI収益+221%($16.7B)・テキサス474GWデータセンター接続凍結
- **ソース:** Technology.org（速報群）
- **公開日:** 2026-09-04
- **信頼性コード:** C-1
- **関連KIQ:** KIQ-002-04, KIQ-002-05, KIQ-004-03
- **関連企業:** Uber, Broadcom, (テキサス州電力網)
- **要約:** 同一ソースの速報3件: (1) Uberが3,300人削減し支出をロボタクシー戦略へ再配分——AI置換というより「AI事業への資源再配置」型リストラの代表例。(2) BroadcomのAIチップ収益は前年比+221%の$16.7B——推論需要の半導体側反映。(3) テキサス州が監査完了まで新データセンターの電力網接続(パイプライン474GW)を凍結——電力制約が供給側の物理的ボトルネック化。
- **キーファクト:**
  - Uber: 3,300人削減→ロボタクシー再配分
  - Broadcom: AIチップ収益$16.7B(+221% YoY)
  - Texas: 474GW接続要求を監査まで凍結
- **引用URL:** https://www.technology.org/2026/09/04/uber-cuts-3300-jobs-robotaxi-strategy/
- **Evidence ID:** EVD-20260906-0071

---

## 追加スクレイプ実行記録（Step 4）
- 計10件実施（予算上限）:
  1. openai.com/pricing（Step 2） 2. blog.google Gemini 3.7 Flash（Step 2） 3. x.ai Grok Bot（Step 2）
  4. arcprize.org/blog/astra → INFO-063 5. lawfaremedia.org governance-by-shakedown → INFO-064
  6. fortune.com Pentagon GenAI.mil → INFO-065 7. SEC EDGAR CIK 2133022 → INFO-066（Oura訂正）
  8. newmarketpitch.com → INFO-067  9. kingy.ai（INFO-039補完・出力大のため保存ファイル参照）
  10. technology.org → INFO-069, INFO-070, INFO-071
