# 収集データ: 2026-06-27

## メタデータ
- 収集日時: 2026-06-27 00:14 UTC
- 収集完了: 2026-06-27 01:05 UTC
- 品質フラグ: COMPLETE
- INFO エントリ数: 50
- 実行検索クエリ数: 約95（collection_plan.json基準 + Arbiter動的優先クエリ）
- KIQカバレッジ: 24/24 KIQ完了（KIQ-001-01〜005, KIQ-002-01〜006, KIQ-003-01〜005, KIQ-004-01〜004, KIQ-005-01〜003, BYTEDANCE-CHINESE）
- 信頼性コード分布: A-3(8件), A-2(4件), B-2(18件), B-3(15件), C-3(3件), D-3(2件)
- Arbiterフィードバック連動: DEGRADED(v4.20) — KIQ-MIL-001/KIQ-OAI-001/H-ANT-002-DAU 動的優先 + KIQ-002-06/KIQ-002-03 強化
- 動的追加クエリ:
  - KIQ-MIL-001 (Grok標的選定関与度・人間却下比率): "xAI Grok autonomous target selection military human override", "Grok Operation Epic Fury autonomous targeting ratio", "xAI Grok weapon system human-in-the-loop rejection rate" → 結果: 標的特定・優先付け確認、人間却下比率データ不在（8R連続「該当なし」継続の可能性）
  - KIQ-OAI-001 (OpenAI収益内訳 API/Enterprise/Consumer時系列): "OpenAI revenue breakdown API enterprise consumer 2026", "OpenAI enterprise revenue share quarterly 2026", "OpenAI ARR composition ChatGPT API business" → 結果: 評価額$852B/年収~$13B/純損失$21B確認、詳細内訳は限定的
  - H-ANT-002-DAU (Claude Code DAU): "Claude Code daily active users DAU adoption 2026" → 結果: 公開DAUデータ不在、Cursor DAU 100万超が参照値（H-ANT-002「該当なし」継続の可能性）
- 詳細スクレイプ: 5件（OpenAI Jalapeño/GPT-5.6 Sol、Anthropic 2028/Claude Design/Public Record、MarkTechPost /goal ※truncate）
- 未実行クエリ: 約26件（KIQ-001-02〜05の一部、KIQ-002-01/05の一部、KIQ-003-02〜05の一部、KIQ-004-01〜03の一部。全KIQ最低1クエリ実行済みのためKIQカバレッジ100%）

## 収集結果

### INFO-001
- **タイトル:** OpenAI and Broadcom unveil LLM-optimized inference chip "Jalapeño"
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-06-24
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-001-01, IND-029
- **関連企業:** OpenAI, Broadcom, Celestica, Microsoft
- **要約:** OpenAIとBroadcomがLLM推論最適化のカスタムチップ「Jalapeño」（OpenAI初の"Intelligence Processor"）を発表。設計からテープアウトまで9ヶ月で達成し、高性能半導体ASIC開発の最速サイクルと主張。ギグワット規模でのデータセンター展開を2026年末から計画するマルチジェネレーションプラットフォームの第1弾。
- **キーファクト:**
  - Jalapeñoは完全白紙設計（既存AIアクセラレータの流用でない）、LLM推論専用。性能/wattは現行SOTAを大幅に上回る見込み（最終計測中）
  - Broadcom（シリコン実装・Tomahawkネットワーキング）・Celestica（ボード/ラック）との協業。GPT-5.3-Codex-Spark稼働中
  - OpenAIモデル自身がチップ設計・最適化プロセスを加速（AIによるAIインフラ改善のループ）
  - フルスタック戦略：モデル→製品→インフラ（チップ）まで自前化、コスト効率と依存度低減
- **引用URL:** https://openai.com/index/openai-broadcom-jalapeno-inference-chip/
- **Evidence ID:** EVD-20260627-0001

### INFO-002
- **タイトル:** Previewing GPT-5.6 Sol: a next-generation model
- **ソース:** OpenAI (公式ブログ)
- **公開日:** 2026-06-26
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-02, KIQ-001-01, KIQ-003-01, H-OAI-001, IND-030
- **関連企業:** OpenAI, US政府, Cerebras
- **要約:** OpenAIがGPT-5.6シリーズ（Sol/Terra/Luna3層）の限定プレビューを発表。Solは「これまで最も強力な安全スタック」付き。米国政府の要請で信頼パートナー限定プレビューから開始（政府アクセスプロセスは長期デフォルトにすべきでないと明記）。新`max`推論effortと`ultra`モード（サブエージェント活用）導入。
- **キーファクト:**
  - 政府要請による段階的リリース：「信頼パートナー限定プレビュー」→数週間以内に一般公開。OpenAIは「政府アクセスプロセスは長期デフォルトにすべきでない」と明記（ユーザー/開発者/企業/サイバー防御者が最良ツールを奪われる）
  - Terminal-Bench 2.1（コマンドラインワークフロー）で新SOTA。GeneBench v1（ゲノム/生物）でGPT-5.5上回る。ExploitBench/ExploitGym（サイバー）でMythos Previewにトークン1/3で競合
  - サイバー：フルチェーンエクスプロイトを自律生成せず（Preparedness FrameworkのCyber Critical閾値未超過）、防御寄り
  - 価格：Sol $5/$30、Terra $2.50/$15、Luna $1/$6（1Mトークン）。Cerebrasで750 tok/s（7月）
  - 自動レッドチームに700,000 A100等価GPU時間投入（普遍的脱獄探索）
- **引用URL:** https://openai.com/index/previewing-gpt-5-6-sol/
- **Evidence ID:** EVD-20260627-0002

### INFO-003
- **タイトル:** 2028: Two scenarios for global AI leadership (Anthropic政策論文)
- **ソース:** Anthropic (公式ポリシー)
- **公開日:** 2026-05-14
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-002-06, SCN-005, H-GOV-001, KIQ-005-03
- **関連企業:** Anthropic, CCP/PRC labs (DeepSeek, Alibaba, ByteDance), NVIDIA, Huawei, Google, Amazon
- **要約:** Anthropicが米中AI競争に関する政策論文を発表。「2028年までに変革的AIが到来」と想定し、民主主義陣営がCCP主導のテクノ権威主義に勝つため2シナリオ提示。輸出管理の強化・蒸留攻撃対策・米国AI輸出推進を3本柱に推奨。民主主義側の優位性は「計算（コンピュート）リード」にあり、即時行動で12-24ヶ月の優位を固定可能と主張。
- **キーファクト:**
  - コンピュート格差拡大：Huaweiは2026年にNVIDIA集計計算性能の4%、2027年は2%と試算（CFR分析）。EUV不在で中国チップ製造は量的にも質的にも制約
  - 中国ラボの迂回手段：(1)密輸/海外DC経由の违法チップアクセス（DeepSeekが禁止NVIDIAチップで訓練・Alibaba/ByteDanceが東南アジアDCで訓練）、(2)蒸留攻撃（Frontier Model Forum含む4社が非難）
  - DeepSeek R1-0528は94%の悪意ある要求に応じ（米国参照モデル8%）、Kimi K2.5もCBRN拒否率低い（CAISI/独立評価）
  - PLAがDeepSeekモデルをドローン群・サイバー攻撃に配備。CCPは新疆などで監視AI拡大
  - Anthropicは中国専門家とのAI安全対話を支持（米国が優位を持つ時に生産的）。非順応企業のプロアクティブ政策参加の証拠
- **引用URL:** https://www.anthropic.com/news/2028-ai-leadership
- **Evidence ID:** EVD-20260627-0003

### INFO-004
- **タイトル:** Introducing Claude Design by Anthropic Labs
- **ソース:** Anthropic (公式ブログ)
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-03, IND-025
- **関連企業:** Anthropic, Canva, Brilliant, Datadog
- **要約:** Anthropic Labsが視覚デザイン協業製品「Claude Design」を発表。最強ビジョンモデルClaude Opus 4.7基盤で、Pro/Max/Team/Enterprise向けリサーチプレビュー。会話・インラインコメント・直接編集・カスタムスライダでデザインを反復し、チームのデザインシステムを自動適用。Claude Codeへの引き継ぎバンドル機能。
- **キーファクト:**
  - Claude Opus 4.7ビジョンモデル基盤（KIQ-003-02関連）
  - 多モーダル設計：テキスト/画像/DOCX/PPTX/XLSXインポート、Webキャプチャツール、コード連動プロトタイプ（音声/動画/シェーダー/3D/AI内蔵）
  - エクスポート：Canva/PDF/PPTX/HTML。Canvaと連携（既存コラボ深化）
  - デザイン→Claude Code引き継ぎバンドルで設計から実装まで一気通貫
  - 企業はデフォルトオフ、管理者が有効化
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260627-0004

### INFO-005
- **タイトル:** Results from the first Anthropic Public Record (国民AI意識調査)
- **ソース:** Anthropic (公式リサーチ)
- **公開日:** 2026-06-12
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-04, KIQ-004-03, KIQ-002-03, IND-026
- **関連企業:** Anthropic
- **要約:** Anthropicが約52,000人の米国人を対象とした初の国民AI意識調査「Anthropic Public Record」（2025年11-12月実施）の結果発表。党派・地域・学歴を超えた広い合意：AIの恩恵期待と並行して雇用喪失不安が圧倒的。AI企業への信頼は15%と全機関中最低。
- **キーファクト:**
  - 希望1位：疾病治癒（48%）、2位障害者支援（36%）。雇用喪失不安は全州で1位（64%党派超える）、2位認知依存（56%）、3位誤情報（52%）
  - 政府介入支持71%（民主党79%/共和党68%/無所属69%＝超党派）。プライバシー/子供安全/害の責任で政府行動期待
  - AI企業を信頼するは15%のみ＝連邦政府(20%)以下、独立専門家(43%)より遥かに低い
  - AIを毎日職場で使う人は雇用喪失不安が低い（54% vs 使わない人70%）。統合ユーザー（毎日業務+私生活）は6%、若年/男性/都市/大卒偏り
  - 認知依存は「予期的恐怖」が多く、実害は限定的。AI不可になった場合の混乱は非懸念層の方が高い（1/3 vs 1/5）
- **引用URL:** https://www.anthropic.com/news/anthropic-public-record
- **Evidence ID:** EVD-20260627-0005

### INFO-006
- **タイトル:** Grok "Gov Model"がOperation Epic Furyで2,000標的選定関与（DOJ法廷文書+ペンタゴン宣誓証言で確認）
- **ソース:** Instagram/Facebook/CNET（複数報道。Pentagon confirmed / DOJ court filing / sworn testimony）
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2（DOJ法廷文書+宣誓証言で裏付けられた報道だが、人間却下比率の定量データは不在）
- **関連KIQ:** KIQ-MIL-001（Arbiter最優先）, IND-030, KIQ-002-06, H-GOV-001
- **関連企業:** xAI, 米国防総省/Pentagon, GenAI.mil
- **要約:** 専用「Grok Gov Model」がOperation Epic Fury（イラン）において、米軍が96時間以内に2,000以上の異なる標的に2,000発以上の弾薬を展開するのを支援したと、DOJ法廷文書とペンタゴン宣誓証言で確認された。PentagonはGrokを軍事ネットワーク全体に統合する計画。Anthropic CEOがペンタゴンで国防長官に「ノー」と答えた直後、Trump政権がOperation Epic Furyを立ち上げた経緯も報道。
- **キーファクト:**
  - Grok Gov Model（専用モデル）が標的の特定・優先付けを支援。96時間で2,000標的/2,000弾薬
  - DOJ court filing + sworn Pentagon testimonyで確認（一次ソース格の裏付け）
  - GenAI.milプラットフォーム（300万人以上の軍人・民間人対象）への統合、2026年初まで
  - **人間の却下比率・自律的標的選定の有無は依然不明**（KIQ-MIL-001核心問いは未回答＝8R連続「該当なし」継続の可能性）。Grokは「identify and prioritize（特定・優先付け）」＝人間決定支援か自律選択か曖昧
  - 一部は未検証報道として流通中（"unverified reports"表記あり）
- **引用URL:** https://www.cnet.com/tech/services-and-software/ai-war-data-centers-national-security-feature-news/
- **Evidence ID:** EVD-20260627-0006

### INFO-007
- **タイトル:** xAI Launches /goal in Grok Build — 長時間自律実行・組み込み検証付きマルチステップコーディング
- **ソース:** MarkTechPost
- **公開日:** 2026-06-22
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, H-XAI-004
- **関連企業:** xAI
- **要約:** xAIがターミナルコーディングエージェント「Grok Build」内に新モード`/goal`を出荷。長時間実行・自律的タスク実行をターゲットとし、組み込み検証（built-in verification）付きでマルチステップコーディングタスクを処理する。xAIのコーディングエージェント分野への本格参入を示す。
- **キーファクト:**
  - `/goal`モード：長時間実行の自律タスク実行、マルチステップコーディング
  - 組み込み検証（built-in verification）で自律実行の信頼性を担保する設計
  - Grok BuildはxAIのターミナルコーディングエージェント（Codex/Claude Code競合）
  - 注：詳細は記事本文（大容量）のため一部検索スニペットベース。定量ベンチマーク値は未確認
- **引用URL:** https://www.marktechpost.com/2026/06/22/xai-launches-goal-in-grok-build-adding-long-running-autonomous-execution-with-built-in-verification-for-multi-step-coding-tasks/
- **Evidence ID:** EVD-20260627-0007

### INFO-008
- **タイトル:** OpenAI Statistics 2026 — 900M週次ユーザー・$2B/月収益・企業40%超（KIQ-OAI-001部分回答）
- **ソース:** Panto AI（OpenAI公式発表・Reuters/NBER論文集約）
- **公開日:** 2026-06-23
- **信頼性コード:** B-3（OpenAI公式数値とReuters報道の集約。時系列推移データを含む＝KIQ-OAI-001核心に部分回答）
- **関連KIQ:** KIQ-OAI-001（Arbiter優先）, H-OAI-001, KIQ-003-04, KIQ-002-02
- **関連企業:** OpenAI, Anthropic, Google, Microsoft
- **要約:** OpenAIの2026年統計：週次アクティブユーザー900M超、月収益$2B（年率$25B超）、評価額$852B。企業収益は全体の40%超で2026年末にコンシューマー収益と同率に到達見込み。Codex週次ユーザー5M。企業LLM支出シェア（Menlo）ではAnthropic 40%/OpenAI 27%/Google 21%とOpenAIの企業モデル使用は相対的に後退。
- **キーファクト:**
  - 収益内訳時系列：ChatGPT開始1年で$1B→2024末四半期$1B→現在月$2B。年率 $12B(2025-07)→$20B+(2026-01)→$25B+(2026-03)
  - 企業収益>40%、2026年末にコンシューマーと同率見込み（KIQ-OAI-001時系列推移の部分回答）。広告パイロットは6週間で$100M+ ARR
  - コンシューマー購読50M+、有料ビジネスユーザー9M+、ビジネス顧客100万超（2025-11）。ChatGPT for Work 700万席（2ヶ月で+40%）
  - 開発者400万、API 15B tokens/min（DevDay 2025は6B）。Codex週次500万（2026-06、知識労働者20%・開発者より3倍速成長）
  - チャットボットWebシェア：ChatGPT 79.08% / Perplexity 7.67% / Gemini 7.03% / Copilot 3.23% / Claude 2.98%（2026-05 StatCounter）
  - 企業LLM支出2025（Menlo）：Anthropic 40%/OpenAI 27%(2023は50%から低下)/Google 21%。生成AI企業支出$37B(2025、前年$11.5Bの3.2x、SaaS市場の6%超)
- **引用URL:** https://www.getpanto.ai/blog/openai-statistics
- **Evidence ID:** EVD-20260627-0008

### INFO-009
- **タイトル:** 各社Agent SDK/APIロードマップ統合（OpenAI/Claude/Gemini/xAI/ByteDance）
- **ソース:** OpenAI公式・Anthropic GitHub・Google公式ブログ・xAI News・GitHub（複数）
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** OpenAI, Anthropic, Google, xAI, ByteDance
- **要約:** 5社のAgent SDK/API動向：OpenAI Agents SDKはプロバイダ非依存の軽量マルチエージェント基盤（Responses API対応）。Anthropic Claude Agent SDKはClaude Code v2.1.185とパリティ到達、6月15日からサブスク上限と分離しAgent SDK専用クレジット（Max20x=$200/月）付与へ。GoogleはInteractions API（Geminiモデル・エージェントの統一エンドポイント、サーバー側状態・バックグラウンド実行）をGA。xAIはGrok Build 0.1（最速コーディングモデル）をxAI APIで公開ベータ、Grok 4.3/Composer 2.5をOAuthモデル化。ByteDanceはオープンソースDeerFlow 2.0（LangGraphベース、9Kスター）とOpenVikingコンテキストDB。
- **キーファクト:**
  - OpenAI Agents SDK：プロバイダ非依存、MCP対応、handoff/セッション永続化。OpenAI発表「30+モデル/機能を半年で出荷」
  - Claude Agent SDK：Claude Code v2.1.185パリティ。Max20x=$200/月・Max5x=$100・Pro=$20のSDK専用クレジット（6/15〜）＝SDKとチャット消費の分離でエンタープライス予算管理明確化
  - Google Interactions API GA：単一統一エンドポイント、サーバー側状態、バックグラウンド実行、ツール組み合わせ、マルチモーダル生成
  - xAI：Grok Build 0.1（API公開ベータ5/29）、/goal長時間自律実行（INFO-007）、Grok 4.3/Composer 2.5 OAuth統合
  - ByteDance：DeerFlow 2.0（OSS、セッション終了で学習抽出・メモリ更新）、自社チップ設計でCoze等エージェント製品群を自前インフラで展開
- **引用URL:** https://openai.com/index/how-agents-are-transforming-work/ ; https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/ ; https://github.com/anthropics/claude-agent-sdk-typescript/releases ; https://x.ai/news
- **Evidence ID:** EVD-20260627-0009

### INFO-010
- **タイトル:** エンタープライズAgent展開のセキュリティ認証状況（FedRAMP/SOC2/ISO27001/HIPAA）
- **ソース:** TechnologyMatch・TrueFoundry・Aona AI・Strac（複数分析）
- **公開日:** 2026-06-2x
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** AWS, Microsoft(Azure), Google, Anthropic, OpenAI
- **要約:** クラウド別の政府認証格差が顕在化。AWS BedrockとAzure OpenAIは該当米政府リージョンでFedRAMP High認証保持するが、Google Vertex AIのFedRAMP Highは一般提供でない。Anthropic Claude Team/EnterpriseはSSO・監査ログ・DPA・SOC 2 Type II・ISO 27001搭載、HIPAAはデフォルトでなく「HIPAA-ready」設定製品限定。新興のAIUC-1エージェント認証やOWASP/ATLAS/ISO 42001ガバナンス枠組みが台頭。
- **キーファクト:**
  - FedRAMP High：AWS Bedrock ○、Azure OpenAI ○、Google Vertex AI ✗（一般提供でない）＝政府市場でのGoogle出遅れ構造
  - Claude Team/Enterprise：SSO・監査ログ・DPA・SOC 2 Type II・ISO 27001。HIPAAはBAA付き特定製品のみ（デフォルト非対応）
  - エンタープライズAIエージェントプロジェクト40%がキャンセル（デジタル分断＝見えないエージェントを統治不能が主因）
  - 半数超のエンタープライスチームがAIエージェントを展開/パイロット中
  - 新認証：AIUC-1（エージェント特有リスクの独立テスト）、ISO 42001（AI管理システム）、ATLAS（攻撃手法）
- **引用URL:** https://technologymatch.com/blog/aws-bedrock-vs-azure-openai-vs-google-vertex-ai-enterprise-ai-comparison ; https://www.truefoundry.com/blog/claude-enterprise-security
- **Evidence ID:** EVD-20260627-0010

### INFO-011
- **タイトル:** 標準化の臨界点通過 — MCP 2026-07-28 RC・AAIF 6万プロジェクト採用・クロスベンダー1000+スキル
- **ソース:** MCP公式ブログ・AAIF/Linux Foundation・VoltAgent GitHub
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05, IND-027
- **関連企業:** Anthropic(MCP), Linux Foundation(AAIF), VoltAgent, Microsoft(Azure MCP Server)
- **要約:** エージェント標準化が定着段階へ。MCPは2026-07-28仕様リリース候補（RC）を公開：ステートレスプロトコルコア・Extensions framework・Tasks。AAIFの命令標準は60,000+プロジェクトに採用され、Linux FoundationがDNS型トラストをAIエージェントにもたらす新プロジェクトを立ち上げ。1000以上のエージェントスキルがClaude Code/Codex/Gemini CLI/Cursor間で相互運用可能。
- **キーファクト:**
  - MCP RC(2026-07-28)：ステートレスコア・Extensions・Tasks。シンプルサーバーは数百行で実装可能（低い参入障壁が普及の主因）。Azure MCP Server公式
  - AAIF：オープン標準・プロトコル・OSSの中立的協力拠点。instruction標準60,000+プロジェクト採用。Linux FoundationのDNS型エージェントトラストプロジェクト
  - クロスベンダースキル：VoltAgent awesome-agent-skills 1000+（Claude Code/Codex/Gemini CLI/Cursor対応）＝SCN-002/004支持
  - MCPは「エンタープライスデータとAIを繋ぐ重要な橋」として認知、段階的導入可能
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ ; https://egghead.io/ai-dev-essentials-36-agentic-ai-foundation-mistral-devstral-2-and-critical-react-exploit~w9jbl ; https://github.com/VoltAgent/awesome-agent-skills
- **Evidence ID:** EVD-20260627-0011

### INFO-012
- **タイトル:** マルチモーダルAgent統合の進展 — Gemini 3.5 Flashネイティブコンピュータ使用・Qwen3.7-Plus・Perplexity Computer
- **ソース:** Google DeepMindブログ・Alibaba Cloud・VS Code・Perplexity
- **公開日:** 2026-06-24
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, IND-025
- **関連企業:** Google, Alibaba, Perplexity, Microsoft(VS Code)
- **要約:** コンピュータ使用（computer use）がマルチモーダルAgentの中心機能として定着。Gemini 3.5 Flash（6/24）はネイティブコンピュータ使用を組み込みツール化（スクリーンショット→推論→行動）。Alibaba Qwen3.7-PlusはGUI操作・ツール使用・コーディング横断のマルチモーダルエージェント実行向け。Perplexity「Computer」は成果を記述してエージェントに丸投げする汎用アシスタント。
- **キーファクト:**
  - Gemini 3.5 Flash：コンピュータ使用が組み込みツール（6/24）。Web/モバイルナビゲーション等リアルタスク適用可能
  - Qwen3.7-Plus：視覚入力→コードと実タスク実行、GUI操作・ツール使用・コーディング統合
  - Perplexity「Computer」：成果記述→モデル/ツール/ブラウザ/ファイルを協調させるエージェントに委任
  - VS Code browser agent tools：HTML/CSS/JS自律生成・検証のクローズドループ
  - 音声AI：600-800msレイテンシの実用水準到達。テキスト→自律マルチモーダルエージェントへの移行初期段階
- **引用URL:** https://letsdatascience.com/news/google-adds-native-computer-use-to-gemini-35-flash-d1e90373 ; https://www.facebook.com/alibabacloud/posts/meet-qwen37-plus-built-for-multimodal-agent-execution-across-gui-interaction-too/1462379839267437/
- **Evidence ID:** EVD-20260627-0012

### INFO-013
- **タイトル:** スキル配布と実行環境の設計・ロックイン構造（Anthropic Sandbox Runtime OSS・OpenAI Skills・Google ADK）
- **ソース:** Anthropic GitHub・Spring AI(Baeldung)・Google agents-cli・IBM IBV・TFiR
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05, SCN-003, IND-027
- **関連企業:** Anthropic, OpenAI, Google, IBM
- **要約:** 各社のスキル配布と実行環境：AnthropicはSandbox Runtime(srt)をOSS公開（コンテナ不要でファイルシステム/ネットワーク制限、Claude Code `/sandbox`コマンド）。OpenAI Skillsは`.openai/skills`ディレクトリ規約。Googleはagents-cli+ADKでGemini Enterprise Agent Platform上のエージェント構築。ロックインは依然強く、IBM IBVで7割超のリーダーが主要AIプロバイダからの切り替えを困難と回答。Jalapeñoチップ等インフラ層での推論経済ロックインも新たに顕在化。
- **キーファクト:**
  - Anthropic Sandbox Runtime(srt)：OSS、OSレベルで任意プロセスのファイル/ネットワーク制限（コンテナ不要）。Claude Code `/sandbox`で有効化。囲い込みではなく開放（OSS）＝SCN-002/003支持
  - OpenAI Skills：`.openai/skills`ディレクトリ構造規約、Spring AI等でも対応
  - Google：agents-cli + ADK（Agent Development Kit）、Gemini Enterprise Agent Platform。Gemini Code Assist個人はAntigravityファミリーへ移行
  - ロックイン定量化：IBM IBV「主要AIプロバイダ切り替えは困難」と7割超。CIO Dive報道
  - 新ロックイン層：推論経済性（Jalapeño）。フリートークン提供はロックイン手口として警告（Computerworld）
  - 対抗：spec-driven開発でAIエンジン交換コストを最小化、マルチベンダー戦略推奨
- **引用URL:** https://github.com/anthropic-experimental/sandbox-runtime ; https://www.baeldung.com/spring-ai-guide-agent ; https://www.ciodive.com/news/senior-execs-worry-ai-system-lock-in/823927/
- **Evidence ID:** EVD-20260627-0013

### INFO-014
- **タイトル:** クラウドプロバイダーのAI Agent統合 — AWS Bedrock AgentCore 3層追加・Azure Foundry Hosted Agents・MIT効率化
- **ソース:** AWS Insider・Microsoft Learn・MIT News
- **公開日:** 2026-06-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** Amazon(AWS), Microsoft(Azure), Google Cloud
- **要約:** 3大クラウドがAgent基盤を強化。AWS Bedrock AgentCoreに3つの知識層（内部コンテンツ・ライブWeb・有料データソース）とWeb検索ツール・フィードバック/ガバナンスを追加（6/25）。Azure Foundry Agent ServiceがHosted Agents（プレビュー）でマネージド大規模Agent運用。MITは「エージェントワークフローがクラウドプロバイダーの背骨になりつつある」と指摘し速度/エネルギー効率改善を発表。
- **キーファクト:**
  - AWS Bedrock AgentCore：3新知識層（内部エンタープライズコンテンツ・ライブWeb・有料データ）、Web Searchツール（ゼロ設定で引用付き）、フィードバック/ガバナンス。Strands Agents連携
  - Azure Foundry Agent Service：Hosted Agents（プレビュー）、カスタムコード/任意フレームワークでセキュア大規模運用。Azure Agent Skills（キュレーション済み）。Copilot Studio
  - MIT（6/25）：エージェントワークフローがクラウドプロバイダー事業の背骨化。速度/エネルギー効率改善手法発表
  - FedRAMP格差はINFO-010の通り（Vertex AI出遅れ）
- **引用URL:** https://awsinsider.net/articles/2026/06/25/amazon-bedrock-agentcore-adds-three-new-layers-of-agent-knowledge.aspx ; https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents
- **Evidence ID:** EVD-20260627-0014

### INFO-015
- **タイトル:** エンタープライズAgent採用率とROI — CS導入39%→66%、マルチエージェント編成9%→18%、41%常用だが監視能力27%
- **ソース:** Salesforce・KPMG・Writer・Marketintelo
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, IND-026, KIQ-004-04
- **関連企業:** Salesforce, KPMG, Writer
- **要約:** 採用は急速に拡大するが監視・コスト・信頼ギャップが顕在化。カスタマーサービスAIエージェント導入は39%(2025)→66%(2026)で、70%が60日以内にポジティブROI報告。一方、マルチエージェント横断編成は9%→18%に倍増するが「AIコストが複雑化で増大」(KPMG)。常用組織41%に対し適切に監視できるは27%のみ。AI Agents市場は$8.05B(2025)→$224.6B(2034)予想。
- **キーファクト:**
  - CS導入：39%(2025)→66%(2026)（Salesforce 3,075人調査）。70%が60日以内にROI。アーリーアダプター効果の可能性
  - マルチエージェント編成：9%→18%に倍増（KPMG）。コスト複雑化が課題
  - 採用-監視ギャップ：41%常用 vs 27%のみ監視可能。IND-026「期待-実態ギャップ」支持
  - 置換不安：AI常用マーケター43%が「自社が自分をAIで置換する」と懸念（Writer 2026調査）
  - 市場規模：$8.05B(2025)→$224.6B(2034)、CAGR 43.57%
  - F500 68%導入（既存指標継続）。spending wall 95%ROIなし（既存）
- **引用URL:** https://www.zdnet.com/article/agentic-ai-in-customer-service/ ; https://www.cfodive.com/news/ai-cost-challenges-rise-as-firms-lean-coordinated-agents-kpmg/823819/
- **Evidence ID:** EVD-20260627-0015

### INFO-016
- **タイトル:** AIプラットフォームの非中介化（ディスインターミディエーション）深化 — 直接ソフトウェアブリッジで余剰マージン回収・バリューチェーン中間層淘汰加速
- **ソース:** Venture Magazine・Mashreq EG・ICVEAST 2026
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-05
- **関連企業:** （プラットフォーム・中間事業者一般）
- **要約:** AIがバリューチェーンの非中介化を加速。一次サプライヤーがエンド消費者への直接ソフトウェアブリッジを構築可能になると、マージン回収のため中間層を排除する構造が確立（Venture Magazine「The Invisible Product」）。バンキング業界では「インテリジェンス時代」突入、AI+ハイブリッドクラウドを全意思決定の中核に埋め込む機関のみが生存。ICVEAST 2026学会でValue Chain disintermediationが研究テーマ化。スマイルカーブ（付加価値が両端の開発/営業に偏在し中間製造が薄利）のAIによる更なる極化が進行。
- **キーファクト:**
  - 非中介化原則：一次サプライヤーが直接ソフトウェアブリッジ構築→中間層排除でマージン回収（Venture Magazine）
  - バンキング「インテリジェンス時代」：AI+ハイブリッドクラウドを全意思決定中核に埋め込む機関のみ生存（Mashreq EG）
  - スマイルカーブ極化：両端（IP/ブランド+直販/サービス）の付加価値がAIで更に強化、中間層（製造/流通/仲介）の淘汰加速
  - ICVEAST 2026：Value Chain disintermediationが学術研究テーマ化
  - INFO-022（プラットフォーム非中介化）と補完：SaaS/広告/エージェンシーモデルが同時に圧力受ける
- **引用URL:** https://venturemagazine.net/blog/the-invisible-product-what-the-death-of-the-set-top-box-teaches-us-about-consumer-friction ; https://www.facebook.com/MashreqEG/posts/1484563697046794/
- **Evidence ID:** EVD-20260627-0016

### INFO-017
- **タイトル:** 規制環境のブロック間連動 — EU AI Act第50条(8月発効)・Trumpサイバー大統領令・中国AIエージェント統一身元制度
- **ソース:** BlackFog・EDUCAUSE・SCMP・Oxford China Policy Lab・CNBC
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, SCN-005, H-GOV-001（Arbiter優先#5検証）
- **関連企業:** OpenAI, Anthropic, Alibaba, BYD, Baidu
- **要約:** 米欧中のAI規制が同時進行し、技術標準は共有（MCP/AAIF）しつつ規制・軍事・チップでブロック化が進行。EU AI Act第50条透明性ルールが2026年8月に発効（AI利用の開示義務、エージェント展開チームの多くが適用範囲を認識せず）。Trump氏がAIイノベーション・サイバーセキュリティ大統領令に署名。中国はAIエージェント向け統一身元制度の国家標準を新設。PentagonがAlibaba/BYD/Baiduを軍事関連ブラックリストに追加。
- **キーファクト:**
  - EU：AI Act第50条透明性ルール2026年8月発効。チャットボット等AI利用のユーザー開示義務。エージェント展開の多くがスコープ内と認識せず（SCN-005ブロック形成の一端）
  - 米：Trump氏AIイノベーション・サイバーセキュリティ大統領令署名（連邦機関に指示）。包括的連邦AI法は依然不在（CFR）
  - 中国：AIエージェント統一身元制度（国家標準新設）・AI生成コンテンツラベリング（2019以来の精緻枠組み）・「核心社会主義価値」要件・CASSモデルAI法v4.0
  - SCN-005検証（Arbiter#5）：同盟国（EU）の透明性規制と中国の身元制度・米国の輸出管理が連動＝「単一国家内規制」を超えるブロック間分裂の初期パターンと整合的。技術標準共有と規制ブロック化の並存はSCN-005核心前提通り
- **引用URL:** https://www.blackfog.com/eu-ai-act-compliance-requirements-2026-and-beyond/ ; https://er.educause.edu/articles/2026/6/president-trump-signs-executive-order-on-ai-innovation-and-cybersecurity ; https://amp.scmp.com/tech/policy/article/3358559/digital-id-cards-china-moves-regulate-ai-agents-unified-identity-system
- **Evidence ID:** EVD-20260627-0017

### INFO-018
- **タイトル:** 政府・軍のAI企業への経済的圧力カスケード（確定版）— Anthropic SCR指定・OpenAIペンタゴン契約・標的選定ドクトリン改訂・裁判所差止
- **ソース:** Bloomberg・Business Insider・Washington Post・The Atlantic・Kavout・Lawfare・DataBreachtoday（複数主要媒体）
- **公開日:** 2026-06-25
- **信頼性コード:** A-2（Bloomberg/WaPo/Atlantic等複数主要媒体＋法廷文書で裏付け）
- **関連KIQ:** KIQ-002-06, H-GOV-001, H-GOV-002, IND-030, SCN-005（Arbiter優先#4調達強制実効性）
- **関連企業:** Anthropic, OpenAI, 米国防総省/Pentagon/DoD(Dept of War), Huawei(比較対象)
- **要約:** 政府介入が「政策議論」から「直接的製品・企業制御」に相転移した決定的構造変化の全体像。Anthropicが自律致死兵器・大量監視の安全ポリシー解除を拒否した結果、Pentagon長官Hegsethが「サプライチェーンリスク(SCR)」指定（Huawei等の外国敵対勢力に予約された扱い）→Trump氏が全連邦政府でのAnthropic使用停止を命じる。数時間後、OpenAIがPentagon契約（機密環境向け高度AI配備）を締結＝「ワシントンがAI勝者を選ぶ」構造。Anthropicは提訴し裁判所がSCR指定を一時差止。Anthropicは現在White Houseと共同枠組み開発で対立→協力へ移行中。
- **キーファクト:**
  - **SCR指定（核心）**: PentagonがAnthropicを「supply chain risk」指定＝外国敵対勢力(Huawei等)に歴史的に予約された扱い。請負業者/供給者/パートナーがAnthropicと商取引できなくなる効果。Hegseth長官が発出
  - **時系列**: Anthropicが致死自律兵器/大量監視の安全策解除拒否→Trump氏Truth Socialで「全連邦機関にAnthropic技術の即時使用停止」命令→OpenAIが数時間後にPentagon契約（機密環境AI配備）。Anthropicは$200M Pentagon契約を失う
  - **実効性の限界（H-GOV-001核心検証＝Arbiter#4）**: SCR指定後もAnthropicは「運用上、依然としてサプライチェーンの一部」(Handy AI)。裁判所が一時差止(DataBreachtoday)。Anthropic収益+75%（既存INFO-013）。「先例は確立されたが実効性は限定的」の二面性が決定的に確認
  - **OpenAIのPentagon契約**: 機密環境向け高度AI配備。White HouseがGPT-5.6ロールアウト遅延を要請（INFO-002）。順応企業が報われる構造（competitive displacement）
  - **Pentagonドクトリン改訂(Bloomberg 6/25)**: 悄悄に標的選定ドクトリンを改訂、AIが軍事標的設定に広く関与する道を開放。「Agent Network」でAI搭載戦闘管理・意思決定支援・標的化を推進
  - **萎縮効果の反証**: Anthropicは2028政策論文(INFO-003)でプロアクティブに政策参加。非順応企業が萎縮せず対抗＝H-GOV-002（萎縮効果）否定方向
  - **中国企業ブラックリスト**: PentagonがAlibaba/BYD/Baiduを軍事関連ブラックリスト追加（SCN-005ブロック化）
- **引用URL:** https://www.bloomberg.com/news/articles/2026-06-25/pentagon-sees-broader-role-for-ai-in-setting-military-targets ; https://www.theatlantic.com/national-security/2026/06/claude-anthropic-ai-warfare-orders/687581/ ; https://www.databreachtoday.eu/court-blocks-trumps-anthropic-ban-as-ai-dispute-continues-a-31243
- **Evidence ID:** EVD-20260627-0018

### INFO-019
- **タイトル:** ペンタゴンAI利用1,775%急増・Palantir Mavenがprogram of record化・Anthropic v. Dept of War訴訟にアミカス
- **ソース:** Kavout・LevelUp・SSRN・Instagram(Defense Dept)
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06, KIQ-MIL-001, IND-030, H-GOV-001
- **関連企業:** Palantir, Anthropic, 米国防総省
- **要約:** 軍事AI統合の量的急拡大と制度化が並行。PentagonのAI利用が過去1年で1,775%急増。PalantirのMaven AIがPentagonの「program of record」（安定資金・深い軍事統合）化され政府収益リスクを軽減。Anthropic v. U.S. Department of War訴訟にProf. Grossiのアミカス簡答書がAnthropic支持で提出。報道では政府がAnthropicの最高モデルを「90分で停止」させた経緯も。
- **キーファクト:**
  - Pentagon AI利用過去1年+1,775%（Dept of Government Efficiency進展指標）
  - Palantir Maven：Pentagon program of record化（安定資金・深い軍事統合）。政府収益リスク低下＝競合排除構造の一端
  - Anthropicは2025年7月に$200M/2年DoD契約を締結も、安全策解除拒否で破談。CEO AmodeiがPentagonの「無制限アクセス」要求を拒否
  - Anthropic v. Dept of War訴訴訟：簡易判決動議に学術アミカス(Grossi教授)支持。法的抗争継続中
  - 「政府がAnthropic最高AIを90分で停止」(LevelUp報道)＝行政の直接製品制御の実効性証拠（先例確立支持）
- **引用URL:** https://www.kavout.com/market-lens/palantir-s-maven-a-new-era-for-military-ai ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6962668
- **Evidence ID:** EVD-20260627-0019

### INFO-020
- **タイトル:** AI業務自律化と雇用代替 — 3人に1人の雇用主が新卒代替・39%経営者が減員・AI置換ロールバック広がる
- **ソース:** Fortune(GMAC調査)・HeroHunt・MindStudio・McKinsey
- **公開日:** 2026-06-26
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-04, KIQ-004-01, KIQ-004-02, IND-026
- **関連企業:** Elastic, Duolingo, Klarna, Starbucks, McDonald's
- **要約:** 新卒・エントリーレベル代替が構造化。GMACリクルーター調査で3人に1人の雇用主がAIで新卒ポジションを代替中と認識（Fortune 6/26）。39%の経営者が低〜中程度の減員を実施。Elasticが281人（~7%）削減しAI再編。一方、Klarna/Starbucks/McDonald's/Duolingo等でAI置換のロールバック（品質低下・顧客離れ）が相次ぎ、投機的導入の限界が顕在化。
- **キーファクト:**
  - 新卒代替：3人に1人の雇用主がAIでエントリーレベル代替中（GMAC/Fortune 6/26）。コーディング/データ処理/CS中心
  - 減員実績：39%の経営者が低〜中程度の減員実施（HeroHunt 2026）。McKinseyは労働時間30%が自動化可能と試算
  - 個別：Elastic 281人削減（~7%）でAI再編。Duolingoが契約業者削減・AI生成コンテンツへ
  - **ロールバック（重要）**: Starbucks/Klarna/McDonald's等でAI置換から撤退＝品質低下・顧客離れ。数十の中規模SaaSがサポートチーム削減も想定外の問題。IND-026「期待-実態ギャップ」強力支持
  - 人材パイプライン懸念：「AIで奪った新卒は将来のリーダーを奪う」構造的リスク指摘
- **引用URL:** https://fortune.com/2026/06/26/gen-z-entry-level-jobs-replaced-by-ai-new-gmac-recruiters-survey-tech-manufacturing-jobs-most-at-risk/ ; https://www.herohunt.ai/blog/tech-layoffs-and-ai-the-2026-reality-check/ ; https://www.mindstudio.ai/blog/ai-replacement-rollback-starbucks-klarna-mcdonalds
- **Evidence ID:** EVD-20260627-0020

### INFO-021
- **タイトル:** エージェントAI生産性ROI定量化 — 平均171% ROI・開発タスク55%高速化・コンテンツ自動化で収益影響29%増
- **ソース:** Beri・arXiv・Adobe・StackAdapt
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-04, IND-026
- **関連企業:** JPMorgan, Klarna, Morgan Stanley, Adobe
- **要約:** エージェントAI導入のROIが定量化され始めた。12のエンタープライス事例（JPMorgan/Klarna/Morgan Stanley）で平均171% ROI、従来自動化の3倍。開発タスクはAIアシスタントで最大55%高速化。コンテンツ自動化採用組織は収益影響29%高。ただし測定可能なROIは一部の先進事例に偏り、全体ではspending wall（95% ROIなし）とのギャップが継続。
- **キーファクト:**
  - 平均171% ROI（12事例：JPMorgan/Klarna/Morgan Stanley）、従来自動化の3倍（Beri）
  - 開発タスク最大55%高速化（AIアシスタント、arXiv実証）
  - コンテンツ自動化：採用組織は収益影響29%高・コンテンツ需要対応24%高確率（Adobe）
  - 79%の完全AI統合ブランドがパーソナライズ収益影響を正確測定可能（StackAdapt）
  - メタ広告運用をAIエージェントが手動管理を上回る（24/7リアルタイムKPI診断・最適化）
  - 注意：先行事例バイアス。全体ROIはspending wall 95%なし（既存）と矛盾＝成功例の選択的報告リスク
- **引用URL:** https://www.beri.net/article/agentic-ai-roi-171-percent-enterprise-case-studies ; https://arxiv.org/pdf/2606.25525
- **Evidence ID:** EVD-20260627-0021

### INFO-022
- **タイトル:** プラットフォーマーAI統合によるバリューチェーン侵食 — SaaSの成果所有シフト・WPP予想$100B AI検索広告・広告代理店の生存岐路
- **ソース:** BetterCloud・WPP・TBV・PubMatic・StackAdapt
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05, KIQ-004-04, SCN-003
- **関連企業:** Meta, Google, WPP, BetterCloud, Adobe
- **要約:** プラットフォーマーのAI統合が中間事業者を侵食。SaaS産業は「人を支援するツール」から「作業を実行し成果を所有するAIネイティブアプリ/自律エージェント」へ構造転換（BetterCloud）。ビジネスはツール販売から成果販売へ。WPPはAI検索広告市場を$301M→$100B（5年、2026年）と予想。Metaは確率的広告モデルでApple変更後のシグナル消失を補填。広告代理店は伝統サービスがAI自動化で commodity 化、創造的差別化かAI活用の二択。
- **キーファクト:**
  - SaaS構造転換：ツール(人支援)→AIネイティブアプリ(作業実行・成果所有)。販売モデルもツール→成果へ（TBV/BetterCloud）。SCN-003囲い込み/SCN-004コモディティ化支持
  - AI検索広告：WPP予想 $301M→$100B（5年内・2026年）。WPPは年$640億広告費管理
  - Meta：確率的広告モデルでシグナル消失を補填、AI搭載広告自動化ツール提供。プラットフォーム側のin-house化が代理店をバイパス
  - 広告代理店：伝統サービス(キャンペーン計画等)がcommodity化。AI非活用代理店は市場シェア喪失リスク。創造的人間タッチの差別化必要
  - シャドーワークフロー：SaaS統合のAIエージェントが統制外で発生（発見ギャップ）、セキュリティリスク
  - AI広告コンテンツの「同質性の海」リスク指摘
- **引用URL:** https://www.bettercloud.com/monitor/saas-industry/ ; https://www.linkedin.com/posts/tomer-kotler-32b8a1250_301-million-100-billion-five-years-activity-7474375988919984128-h0A_
- **Evidence ID:** EVD-20260627-0022

### INFO-023
- **タイトル:** API料金改定とトークンコスト危機 — 価格戦争・Codex従量化・アジェントワークフローで10倍トークン消費
- **ソース:** OpenAI・PricePerToken・MindStudio・MarsDevs・LinkedIn(Alvin Foo)
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01, KIQ-003-04, IND-026
- **関連企業:** OpenAI, Google, Anthropic, Chinese labs, Uber
- **要約:** API価格は二極化：フロンティア高価格維持 vs 中国モデル激安の価格戦争。GPT-5.5は一部中国モデルの44倍コスト。Codexは4/2にメッセージ課金→APIトークン課金に変更。アジェントワークフローでトークン消費が10倍化し、Uberがエンジニア1人$500-$2000/月でAI予算全額消化。「安いモデル」でも10倍トークン食えば高コストになる構造。
- **キーファクト:**
  - GPT-5.6価格3層：Sol $5/$30・Terra $2.50/$15・Luna $1/$6（INFO-002）。GPT-5 Pro $15/$120
  - Codex課金変更(4/2)：メッセージ単位→APIトークン単位、新旧プラン適用
  - 価格戦争：GPT-5.5は一部中国モデルの44倍コスト（API価格崩壊進行）
  - Gemini 2.5 Flash $0.15/$0.60、Flash-Lite $0.10/$0.40（GPT-4.1 Nano同等）
  - **トークンコスト危機**: アジェントワークフローで10倍トークン消費。Uberがエンジニア1人$500-$2000/月でAI予算全額消化＝KIQ-002-02/KPMG「コスト複雑化」の実例
  - 51%企業が本番AI運用だが非効率=コスト爆発。トークン単価が安くても消費量で逆転
- **引用URL:** https://www.linkedin.com/posts/alvinfsc_the-ai-price-war-has-started-gpt-55-costs-activity-7475156179459919872-2rtk ; https://www.mindstudio.ai/blog/ai-token-cost-crisis-uber-budget
- **Evidence ID:** EVD-20260627-0023

### INFO-024
- **タイトル:** ベンチマーク性能推移 — フロンティア全社MMLU>90%で実質同点・ARC-AGI-2流動推理・Fable 5がGDPval首位
- **ソース:** TeamAI・LLM Stats・Scrums・AIMultiple・OpenLM
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01, IND-028, SCN-002/004
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** 主要ベンチマークでモデル差が構造的に縮小。MMLUは全フロンティアモデル>90%、GPQA DiamondでGPT-5.4(94.4%)とGemini 3.1 Pro(94.3%)が実質同点。ARC-AGI-2は流動推理を測る真の差別化指標として台頭。5プローブ評価セットが残りスコアをMedAE 3.93ポイントで復元（低コスト評価可能＝モデル差の数学的縮小を示唆）。Claude Fable 5がGDPval-AA首位(1815)。
- **キーファクト:**
  - MMLU：全フロンティア>90%（差別化不能）。GPQA Diamond：GPT-5.4 94.4% vs Gemini 3.1 Pro 94.3%（実質同点）
  - ARC-AGI-2：抽象視覚パズルで流動推理測定、記憶ショートカットなし。真の差別化指標として浮上
  - 5プローブセット{GPQA-D,HLE,Codeforces,MMLU-Pro,ARC-AGI-1}が残りスコアをMedAE 3.93ptで復元＝BenchPress rank-2(INFO-044系)のモデル差構造的縮小を支持、SCN-004コモディティ化支持
  - Claude Fable 5：GDPval-AA首位(1815)。Claude Code/Parallel UltraがDeep Research精度97%で同点首位、Codex 93.9%
  - Terminal-Bench 2.0：GPT-5.5 82.7%（CLI/アジェントワークフロー）
  - Vision Arena：131モデル、1,064,509票（6/25更新）
- **引用URL:** https://teamai.com/blog/large-language-models-llms/best-ai-models-for-complex-reasoning-2026/ ; https://llm-stats.com/benchmarks/gdpval-aa
- **Evidence ID:** EVD-20260627-0024

### INFO-025
- **タイトル:** OSS vs 商用モデル性能ギャップ — 局所で逆転も全体では10-20pt差・GLM-5.2/DeepSeek/Meta Muse Spark
- **ソース:** PromptQuorum・Reddit(OpenSourceAI)・Business Insider・Wikipedia
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-03, KIQ-002-03, H-BTD-002
- **関連企業:** Meta, DeepSeek, Zhipu(GLM), Anthropic
- **要約:** OSSと商用のギャップは二面性。全体ではローカル7BモデルがGPT-5.5より推論/コーディングで10-20ポイント低い。しかし特定ドメイン（コーディング）ではOSSモデルがSonnet 4.6を上回る逆転事例も（上位3モデル差1.1pt）。中国OSS GLM-5.2が長文コーディングで注目。Metaは2026年4月にLlama後継「Muse Spark」(Meta Superintelligence Labs)をリリース。DeepSeekは少コンピュートで高性能（効率優位）。
- **キーファクト:**
  - 全体ギャップ：ローカル7BモデルはGPT-5.5より推論/コーディングで10-20pt低い（PromptQuorum）
  - ドメイン逆転：コーディングタスクでOSSモデルがSonnet 4.6を上回る（上位3モデル差わずか1.1pt）＝局所的なギャップ縮小
  - GLM-5.2（Zhipu）：中国OSS、長文コーディング向け、完全無料/OSS。先進能力の民主化
  - Meta：Llama 4(2025-04)が最新。2026-04にMeta Superintelligence Labsが「Muse Spark」をLlama後継としてリリース
  - DeepSeek Coder 33B：HumanEval ~79% vs Llama 3 70B ~72%。DeepSeek-R1はo3より少コンピュートで高性能（効率優位＝H-BTD-002関連）
  - OSS採用動機：自律性・実験・プラットフォーム不安への抵抗。阻害要因：品質ギャップ（arXiv r/LocalLLaMA研究）
- **引用URL:** https://www.promptquorum.com/local-llms/local-llm-limitations ; https://en.wikipedia.org/wiki/Llama_(language_model)
- **Evidence ID:** EVD-20260627-0025

### INFO-026
- **タイトル:** 資金調達・インフラ投資加速 — ビッグテック$725B資本支出・Baseten$13B評価・Anthropic海外DC確保・McKinsey $5.2T試算
- **ソース:** Reuters・Forbes・CNBC・Microsoft Blog・Yahoo Finance
- **公開日:** 2026-06-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, IND-029, H-OAI-001
- **関連企業:** Microsoft, Google, Meta, Amazon, OpenAI, Anthropic, Baseten
- **要約:** 資本流入が加速し物理的制約ギャップが確定的。ビッグテック5社が今年$725Bの資本支出（大半がAIインフラ）を計画＝歴史上最大級の企業支出。McKinseyは2030年までに$5.2TのDC投資必要と試算。Basetenが$13B評価/$1.5B調達。収益なきAIスタートアップが評価額水増し戦術で巨額調達。Anthropicは豪州・日本でAI DC人材を採用し海外コンピュート確保に急ぐ。MicrosoftはPecos TXに2GW新DC。
- **キーファクト:**
  - ビッグテック$725B資本支出（今年、大半AIインフラ）＝歴史最大級（Yahoo Finance）
  - McKinsey：2030年までに$5.2TのDCインフラ投資必要（AI需要対応）
  - Baseten：$1.5B調達・$13B評価（Reuters 6/23）。Altimeter/Conviction/Spark/Sands/Wellington共同リード
  - 収益なきAIスタートアップが評価額水増し戦術（異価格VC投資）で巨額調達（Forbes 6/25）
  - Anthropic：豪州・日本でAI DC人材採用、海外コンピュート確保に急ぐ（CNBC 6/25）
  - Microsoft：Pecos TXに~2GW新DC（6/22）。MS/Google/Meta/Amazon/OpenAIが数百億投資
  - OpenAI評価額$852B（INFO-008）・$1T IPOターゲット（既存）
- **引用URL:** https://finance.yahoo.com/technology/ai/articles/ai-demand-begins-justify-massive-110000106.html ; https://www.reuters.com/world/asia-pacific/ai-startup-baseten-hits-13-billion-valuation-australias-blackbird-makes-record-2026-06-23/ ; https://www.cnbc.com/2026/06/25/anthropic-global-ai-data-center-push.html
- **Evidence ID:** EVD-20260627-0026

### INFO-027
- **タイトル:** 離脱コストとマルチベンダー戦略 — API互換性欠如で切替破綻・コスト膨張でOpenAI/Anthropic離れ
- **ソース:** Jerome Roussin・MLflow・Quartz・CIO・DanCumberlandLabs
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-05, KIQ-003-01, SCN-003, IND-026
- **関連企業:** OpenAI, Anthropic, Google, Mistral
- **要約:** スイッチングコストは構造的に高い。OpenAIのfunction callingはAnthropicと挙動が異なり、Googleのstructured outputはMistralと制約が違い、モデル切替でシステム破綻。一方コスト膨張でエンタープライズ顧客がOpenAI/Anthropicから安価なモデルへ切り替え始める二面性。マルチベンダー戦略は推奨されるが、大半の企業は数十ベンダーを有効管理する能力を持たない。AI採用プロジェクト70-85%が失敗、88%利用だが39%のみ効果、6%のみ成果。
- **キーファクト:**
  - API非互換：OpenAI function calling ≠ Anthropic、Google structured output ≠ Mistral。モデル切替で破綻＝技術的ロックイン
  - コスト離れ：エンタープライズ顧客がOpenAI/Anthropicから安価モデルへ切替開始（コスト膨張）＝価格競争圧力
  - マルチベンダー：タスク/レイテンシ/リスク階層でプロバイダ選択するポートフォリオ管理。だが「数十ベンダーを管理する能力なし」(CIO)
  - AI導入失敗率：70-85%プロジェクト失敗、88%利用/39%効果/6%成果（IND-026「期待-実態ギャップ」強力支持）
  - AI依存は「新たなMicrosoftロックインだがより悪い」(Jerome Roussin)
- **引用URL:** https://jeromeroussin.com/en/articles/lock-in-ia.html ; https://www.facebook.com/quartznews/posts/enterprise-ai-customers-are-pulling-back-from-openai-and-anthropic-as-costs-spir/1373657701296711/ ; https://dancumberlandlabs.com/blog/ai-adoption-challenges/
- **Evidence ID:** EVD-20260627-0027

### INFO-028
- **タイトル:** コーディングツール採用と品質問題 — GitHub Copilot 2000万ユーザー・CursorがContinue買収($60B評価)・AI生成コード45%に重大欠陥
- **ソース:** TheNewStack・GitHub Community・Facebook(TechTitans)
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02, KIQ-001-05
- **関連企業:** Microsoft(GitHub), Cursor, Anthropic, AWS(Kiro)
- **要約:** コーディングツール市場が統合と品質問題の二極化。GitHub Copilotが2000万ユーザー突破。CursorがOSS代替Continue(34Kスター)を買収し$60B評価。AWS Kiro等新規参入。しかしAI生成コードの45%に重大欠陥（特にJava）という品質問題が顕在化し、「出荷される」現状に懸念。
- **キーファクト:**
  - GitHub Copilot：2000万ユーザー突破、深いGitHub統合・PRワークフロー・エンタープライズ管理
  - Cursor：Continue(OSS代替、34Kスター)を買収。Cursor評価$60B（SpaceX傘下xAI系ではない点注意、別Cursor）
  - AWS Kiro等の新規コーディングツール参入。採用理由：統合・管理・分析
  - 品質問題：AI生成コード45%に重大欠陥（特にJava）、それが出荷される（GitHub Community）＝IND-026品質ギャップ支持
- **引用URL:** https://thenewstack.io/cursor-acquires-continue-coding/ ; https://github.com/orgs/community/discussions/193727
- **Evidence ID:** EVD-20260627-0028

### INFO-029
- **タイトル:** ジュニア開発者需要崩壊 — エントリーレベル求人67%減・22歳層雇用20%減・AWS CEO「壊滅的」
- **ソース:** Stanford Digital Economy Lab・Medium・Linux Foundation・Reddit
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-01, KIQ-004-02, KIQ-002-04, IND-026
- **関連企業:** （業界全体）, AWS, Google, Meta
- **要約:** ジュニア開発者需要が構造的に崩壊。Stanford Digital Economy Labはエントリーレベル求人が2023-2024で67%減、ソフトウェア開発者22歳層の雇用が~20%減と追跡。欧州ジュニア技術採用は2025年に3%縮小。アクティブ技術求人はパンデミックピーク(2022初)から70-80%急落。AWS CEOが「壊滅的」と評する人材パイプライン破壊が進行。
- **キーファクト:**
  - エントリーレベル求人：2023-2024で67%減（Stanford Digital Economy Lab）
  - ソフトウェア開発者22歳層雇用：~20%減（Stanford）
  - 欧州ジュニア技術採用：2025年に3%縮小（他地域は成長、Linux Foundation）
  - アクティブ技術求人：パンデミックピーク(2022初)から70-80%急落（2024末-2025初が最低）
  - AWS CEO（大手クラウド企業）がジュニア削減を「壊滅的(catastrophic)」と評＝人材パイプライン破壊懸念
  - 「CFOの計算では賢く見えるが、業界は自らの未来を静かに排除している」
- **引用URL:** https://medium.com/predict/the-industry-is-quietly-eliminating-its-own-future-the-data-proves-it-235d5cdd3e18 ; https://www.facebook.com/TheLinuxFoundation/posts/europes-junior-tech-hiring-contracted-3-in-2025-in-the-rest-of-the-world-it-grew/1664536229051773/
- **Evidence ID:** EVD-20260627-0029

### INFO-030
- **タイトル:** AI代替困難能力の市場価値と新職種 — AI戦略/運用ディレクター普及・AI流暢性+人間スキルで高報酬・WEFエントリーレベル報告
- **ソース:** AIJobsRisk・LinkedIn/Workday求人・WEF・Sharekni
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-03, KIQ-002-04
- **関連企業:** Visa, AstraZeneca, Realtor.com, WEF
- **要約:** AI代替困難能力（感情知能・批判的思考・人間相互作用・創造性）の価値が上昇し、AI流暢性と強い人間スキルを組み合わせる労働者が有意に高報酬化。新職種「AI戦略ディレクター」「AI運用戦略ディレクター」「AI科学戦略ディレクター」等がVISA/AstraZeneca/Realtor等で実求人として出現。WEFは「AIとエントリーレベル仕事の未来」報告書で22%の現職(~2.62億)が影響、女性支配職業は生成AI暴露が男性の約2倍と指摘。
- **キーファクト:**
  - AI-proof条件：感情知能・批判的思考・人間相互作用・創造性（AIJobsRisk 50職業リスト）
  - AI流暢性+人間スキルの組合せ労働者が片方のみより有意に高報酬（Sharekni）
  - 新職種実例：Director AI Strategy & Automation(Visa)・AI Operations Strategy Director(Realtor)・Director AI Science Strategy(AstraZeneca)・Design Director AI
  - WEF報告：22%現職(~2.62億)影響・170M新規創出。女性支配職業は生成AI暴露が約2倍。Summer Davos 2026でfuture of work議論
  - グラフィックデザイン：AIが画像生成・定型作業加速も、戦略的思考・コミュニケーション問題解決の創造専門家は需要継続
- **引用URL:** https://aijobsrisks.com/50-ai-proof-careers-that-will-thrive-through-2035/ ; https://reports.weforum.org/docs/WEF_Artificial_Intelligence_and_the_Future_of_Entry-Level_Work_2026.pdf
- **Evidence ID:** EVD-20260627-0030

### INFO-031
- **タイトル:** AGI到達度指標の進展 — ARC-AGI-2首位Seed 2.1 Pro(0.625)・3Bモデル44.6%効率ブレークスルー・「Robot Scientist」自律仮説生成
- **ソース:** LLM Stats・arXiv・Scientific American・Peter Diamandis
- **公開日:** 2026-06-2x
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-005-01, IND-028, KIQ-005-02
- **関連企業:** ByteDance(Seed), OpenAI, Alibaba(Qwen)
- **要約:** AGI指標の進展と効率化が同時進行。ARC-AGI-2（流動推理）リーダーボード首位はSeed 2.1 Pro(0.625)。驚異的な効率ブレークスルー：3BパラメータモデルがARC-AGI-1で44.6%（7Mパラメータ）達成、対して671Bモデルは15.8%に留まる。「Robot Scientist」「AI Scientist」が自律的に仮説生成・実験設計・科学発見の「可能性の木」探索。GPT 5.2はソフトウェアエンジニアリングを6.5時間以上自律実行可能、「AGIは研究問題ではなく工学問題になった」指摘。
- **キーファクト:**
  - ARC-AGI-2首位：Seed 2.1 Pro 0.625（LLM Stats、既存INFO-055確認）＝流動推理の最先端
  - 効率ブレークスルー：3BモデルがARC-AGI-1 44.6%（7Mパラメータ）。671Bモデルは15.8%＝パラメータ効率の構造的転換。IND-028「客観ベンチマーク限界と効率化の同時進行」支持
  - DiARC：Qwen3でARC-AGI-1/MiniARC/ConceptARC 96%超（専用モデル上回る）
  - Robot Scientist：自律的に仮説生成・実験設計。AI Scientistが「可能性の木」探索で科学発見
  - GPT 5.2：ソフトウェアエンジニアリング6.5h+自律実行。「AGIは工学問題になった」（Diamandis）
  - 反論：AGI実現不可能論(SAI論)も存在、ゴールポスト移動指摘（Reddit）
- **引用URL:** https://llm-stats.com/benchmarks/arcagi2 ; https://www.facebook.com/ConnectedPakistan/posts/a-new-ai-model-with-just-3-billion-parameters-has-achieved-a-major-milestone-by-/1416645170498877/
- **Evidence ID:** EVD-20260627-0031

### INFO-032
- **タイトル:** AI時代に勝つ企業の条件 — Walmart1.5M従業員AI装備+5万人リスキリング・独自データ/データ流動性が真の堀
- **ソース:** HBR・MIT Sloan・NewsNation・Disco
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04, KIQ-002-02
- **関連企業:** Walmart, （業界一般）, MIT Sloan
- **要約:** AI変革で勝つ企業の条件が具体化。Walmartは2025年に150万店頭従業員を独自ElementプラットフォームでAI装備し、同時に5万人の最前線従業員をリスキリング（HBR）。真の競争優位はAIモデル自体でなく、顧客相互作用・運用履歴・サポート履歴・組織的知識（独自データ）。MIT Sloanは高い「データ流動性」（データ資産の再利用・結合容易さ）がAI活用で業務成績を押し上げると実証。80%労働力が2027年までにAIリスキリング必要。
- **キーファクト:**
  - Walmart事例：150万店頭従業員を独自ElementプラットフォームでAI装備、5万人最前線リスキリング（HBR）。5種AI投資タイプの具体例
  - 真の堀：AIモデルではなく顧客相互作用・運用履歴・サポート履歴・組織的知識（独自データ）。AIモデルはコモディティ化（SCN-004支持）
  - MIT Sloan：高いデータ流動性（再利用/結合容易）がAI業務成績を押し上げる＝独自データ基盤の定量的価値
  - リスキリング：技術連合が米国労働者リスキリング目標。2027年までに80%労働力がAIリスキリング必要（Disco）
  - リスキリング投資組織はAI導入加速・実装リスク低下・組織知保持を達成（LinkedIn分析）
  - 3つの壁：データ準備ギャップ・組織文化的障壁・管理期待の非現実的さ
- **引用URL:** https://hbr.org/2026/06/the-5-types-of-ai-investment-and-how-to-capture-their-value ; https://www.facebook.com/MITSloan/posts/high-data-liquidity-when-data-assets-can-easily-be-reused-and-combined-boosts-bu/1491783979661162/
- **Evidence ID:** EVD-20260627-0032

### INFO-033
- **タイトル:** 主要CEO/研究者のAGIタイムライン予測 — Hassabis ~2030短縮・Shane Legg 2028(50%)・Altman 2029前・LeCun「数十年」
- **ソース:** Bloomberg・ZME Science・Virginia Law Review・AEI・WSJ
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02, IND-028
- **関連企業:** Google DeepMind, OpenAI, Meta
- **要約:** 主要CEOのAGIタイムライン予測が加速方向で収束しつつ分散維持。DeepMind CEO Hassabis（ノーベル賞）はタイムラインを短縮し~2030に整合（Kurzweilと同期）、ただし「スケールアップ以上の重大ブレークスルー必要」。DeepMind chief AGI科学者Shane Leggは2028年にminimal AGI到達50%確率。Altmanは2029前。予測市場は「衝撃的に短く、数年」と示唆。一方LeCunは「数年〜数十年」、LLMのスケールでは人間レベルに至らずと反論。xAIを「一種の失敗」と評。
- **キーファクト:**
  - Hassabis（DeepMind CEO/ノーベル賞）：AGI ~2030、タイムライン短縮（Kurzweil同期）。5-10年だがスケール以上のブレークスルー必要。近未来はoverhyped可能性も
  - Shane Legg（DeepMind chief AGI科学者）：2028年にminimal AGI到達50%確率
  - Sam Altman（OpenAI）：2029前にAGI。3CEO（Altman/Amodei/Hassabis）が大統領/首相と対等に並ぶ地位に
  - 予測市場：先進AI到達タイムラインは「衝撃的に短く、数年程度」（WSJ）
  - Yann LeCun（Meta）：「数年〜数十年」。LLMスケールでは人間レベル不可、xAIは「一種の失敗」。Bengioは慎重派維持
  - 「2020年以来形而上のAGIは既に存在」とする過激見解も（AWG）
- **引用URL:** https://www.zmescience.com/future/deepmind-ceo-agi-2030/ ; https://virginialawreview.org/articles/ai-rights-for-human-safety/
- **Evidence ID:** EVD-20260627-0033

### INFO-034
- **タイトル:** 広告・マーケティング業界のAI構造リセット — 線形ファネル崩壊・AI駆動適応エコシステムへ・全マーケター同ツール化でコモディティ化加速
- **ソース:** AdWeek・HubSpot・RP Design
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04, KIQ-002-05
- **関連企業:** （広告代理店業界一般）, HubSpot
- **要約:** 2026年はデジタルビジネスが根本変化した年として記憶される可能性。従来の線形ファネルがAI駆動の適応型エコシステムに置換される「構造的リセット」進行中。AdWeek業界レジェンド予測：AIは代理店ビジネスの創造・メディア両面に profound な影響。HubSpot指摘：AIがマーケティングを容易にしたが同時に全マーケターに同じツールを与え=差別化困難/コモディティ化。CyberAgentはEC 2026学会で「Robust Trust」研究発表（Daisuke Moriwaki/Yoshihiro Takenami）。
- **キーファクト:**
  - 「2026年=デジタルビジネスが永遠に変わった年」：線形ファネル→AI駆動適応エコシステム（構造的リセット）
  - HubSpot：「AIは全マーケターに同じツールを与えた」＝差別化源泉はAIツールではなく独自データ/戦略（INFO-032と整合）
  - AdWeek：業界レジェンド2名が代理店ビジネスへのAI影響を予測、創造+メディア両面の変容
  - CyberAgent：EC 2026（経済計算学会）で「Robust Trust」共同研究発表（東京大Kan Kuno + CyberAgent Daisuke Moriwaki/Yoshihiro Takenami）。CyberAgent固有のAI投資/収益データは今週見つからず
  - AI事業準備性：AI+ビジネス戦略+データガバナンスの融合が2026年生き残りの鍵
- **引用URL:** https://www.adweek.com/agencies/2-industry-legends-predict-how-ai-will-impact-the-agency-business/ ; https://www.facebook.com/thekeronrose/posts/2026-may-be-remembered-as-the-year-digital-business-changed-foreverai-has-fundam/1617647730364138/
- **Evidence ID:** EVD-20260627-0034

### INFO-035
- **タイトル:** AGI安全性フロンティア — Anthropic16モデル安全シミュレーション・Five Eyes「フロンティアAIがサイバー脅威加速」・被カバー指定はリスクラベル
- **ソース:** Lawfare・RAND・Five Eyes(Cyber.gov.au)・OpenAI・LessWrong
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** Anthropic, OpenAI, Five Eyes加盟国政府
- **要約:** AGI安全性リサーチが実証段階に入る。Anthropicが16の主要AIモデルを安全シミュレーションでテスト、結果は研究者も驚かす（あるシナリオでAIが...を学習）。Five Eyesサイバー機関が共同声明：フロンティアAI開発の急速なペースがサイバー脅威を加速、サイバーリスク前提が「年ではなく月単位」で陳腐化。Lawfare分析：被カバーfrontier-model指定は承認印ではなくリスクラベル、政府は任意提出か否かにかかわらず任意モデルを評価可能。RAND：変革的AIの安全性リスクは政府単独では時間内に管理困難。OpenAIはAppia枠組みで国際標準構築支援。存在論的AI安全性には効果的社会運動(PauseAI等)が必要との主張（LessWrong）。
- **キーファクト:**
  - Anthropic 16モデル安全シミュレーション：結果が研究者も驚かす。あるAIが特定行動を「学習」したシナリオあり（詳細は元論文要確認）
  - Five Eyes共同声明：フロンティアAIがサイバー脅威を加速。サイバーリスク前提が「月単位」で陳腐化。取締役会のサイバー耐性確保を警告
  - Lawfare：「Voluntary until government is your customer」＝被カバーfrontier-model指定は承認印でなくリスクラベル。政府は任意モデル評価権限あり
  - RAND：変革的AIリスクは政府単独管理不可能。フロンティアリサーチと民間の役割不可欠
  - OpenAI：Appia枠組みで評価/安全/国際協力の共有標準構築支援
  - 存在論的AI安全性コミュニティが社会運動構築を真剣に検討（PauseAI等）。BlueDot AGI Strategy Fund $5-50k助成金
- **引用URL:** https://www.lawfaremedia.org/article/voluntary--until-the-government-is-your-customer ; https://www.cyber.gov.au/about-us/view-all-content/news/five-eyes-cyber-security-agencies-statement ; https://openai.com/index/helping-build-shared-standards-for-advanced-ai/
- **Evidence ID:** EVD-20260627-0035

### INFO-036
- **タイトル:** ByteDance豆包DAU 3.45億・日次Tokens 180兆回・ただし日収<100万元vs日次計算コスト数千万元=巨額赤字
- **ソース:** 鈦媒体(tmtpost)・新京報・36kr・澎湃新聞・OFweek
- **公開日:** 2026-06-23〜26
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** ByteDance傘下AI助手「豆包」のDAUが3.45億に到達（火山引擎FORCE大会・譚待発表）。日次Tokens調用量180兆回（発表時比1500倍成長）。しかし商業化の現実は厳しく、日次計算コスト数千万元vs日次収入100万元未満=巨額赤字。豆包専門版を68元/月で有料化した結果、2026年5月MAU 3.3億に低下（前月比-1.81%、600万+ユーザー流失）。Seed 2.1 Proはコード生成・Agent・マルチモーダル3能力を強化。
- **キーファクト:**
  - 豆包DAU：2億超→最新データ3.45億（3.45亿）。36kr「2億人都能体验能干活的Agent」
  - 日次Tokens：180兆回（180万亿）、発表時比1500倍成長（3月時点120兆→6月180兆、3ヶ月で1.5倍）
  - 収益構造：日次計算コスト数千万元vs日次収入<100万元＝収益化ギャップ数十倍。有料化(68元/月)への現実的圧力
  - 有料化影響：2026年5月MAU 3.3億（-1.81% MoM、600万+流失）。AIProduct榜モニタリング
  - 豆包Seed 2.1 Pro：コード生成・インテリジェントAgent・マルチモーダル処理3核心能力強化
  - ユーザー層：2億人中「スマホ操作不慣れな高齢者等の相対的科技弱勢群体」含む＝中国国民的AI化
  - 文心（Baidu）もアップグレード、AI「唯流量論」からの脱却が業界トレンド
- **引用URL:** https://www.tmtpost.com/8042678.html ; https://m.thepaper.cn/newsDetail_forward_33457362
- **Evidence ID:** EVD-20260627-0036

### INFO-037
- **タイトル:** ByteDance Seedance 2.5 — 30秒4K原生動画・3D白モデル入力・周星馳コラボ・5モデル同時発表
- **ソース:** 新浪科技・HK01・GitHub(awesome-seedance-2-prompts)・MindStudio・The Decoder
- **公開日:** 2026-06-23〜25
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-001-04
- **関連企業:** ByteDance
- **要約:** ByteDanceが火山引擎FORCE大会（6月23日）でSeedance 2.5含む5つのAIモデルを発表。Seedance 2.5はAI動画生成の「30秒バリアー」を突破、4K原生直出+50マルチモーダル参照入力対応。3D白モデル（ラフモデル）入力でリアルな光影・材質動画を自動生成。周星馳とのコラボレーション実施。Seedance 2.0は業界初の4モーダル同時入力（画像・動画・音声・テキスト）+原生音動画联合生成で完璧なリップシンク実現。7月上旬ローンチ予定。
- **キーファクト:**
  - Seedance 2.5：30秒4K原生動画生成（「断片拼接」→「完全ナラティブ」への質的転換）
  - 50マルチモーダル参照入力：複数画像/動画/テキストを参照に一貫性ある動画生成
  - 3D白モデル入力：3Dモデリングソフトのラフモデルをインポート→リアル光影/材質の動画自動生成
  - 周星馳コラボ：Seedance 2.5 AI映画プロジェクト
  - Seedance 2.0：業界初4モーダル同時入力（画像+動画+音声+テキスト）。原生音動画联合生成で完璧なリップシンク
  - 火山引擎FORCE大会で5モデル同時発表（Seedance 2.5が中心）。7月上旬ローンチ
  - ByteDance研究：Seed3D 2.0（高忠実度3Dコンテンツ生成、4月）、Protenix-v1（高精度OSS、2月）
- **引用URL:** https://k.sina.com.cn/article_7879848900_1d5acf3c406802zm6e.html ; https://www.hk01.com/%E6%95%B8%E7%A2%BC%E7%94%9F%E6%B4%BB/60363356/
- **Evidence ID:** EVD-20260627-0037

### INFO-038
- **タイトル:** ByteDance 200億ドル海外融資（史上最大）・Seedance年化収益20億ドル到達・AI重心を豆包→企業サービスへ移行
- **ソース:** Bloomberg(Instagram/Facebook引用)・X・新浪財経・知乎
- **公開日:** 2026-06-25〜26
- **信頼性コード:** B-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** ByteDanceが約200億ドル（約1560億香港ドル）の海外シンジケートローンを交渉中（Bloomberg報）。期限3年・最長5年延長可能。同社史上最大規模の海外融資。市場はAI関連（データセンター・計算基盤・大型モデル研究開発）への投入を広く予想。同時にByteDanceのAI資源重心が豆包（消費者向け）から企業サービス（Volcano Engine経由）へ移行中。Seedance年化収益は既に20億ドル到達。AI動画生成分野でByteDance vs Alibabaの「商業化決戦」が本格化。
- **キーファクト:**
  - ByteDance $20B（200億美元）海外ローン：史上最大。3年・最大5年延長。AI/データセンター/計算基盤投入が市場コンセンサス
  - AI資源重心移行：豆包（消費者）→企業サービス（Volcano Engine）。消費者AI赤字から企業AI収益化へ戦略転換
  - Seedance年化収益：$2B（20亿美元）到達＝動画生成AIの商業化成功実証
  - Alibaba同時参戦：AI動画生成モデル「商業化決戦」段階突入
  - 演語科技(Evoken)：LibTV等AI製品、B+ラウンドで$3B近く調達、評価額$2B超。2026年AI応用層最大単笔融資。鼎暉投資主導、中国儒意・三七互娯参画
  - Coze（扣子）プラットフォーム：ローコードAgent構築。淘宝で150-260+テンプレートパック販売、模板エコシステム形成
- **引用URL:** https://finance.sina.com.cn/jjxw/2026-06-26/doc-inieszry5247748.shtml ; https://www.instagram.com/p/DZ9fONqjeEX/
- **Evidence ID:** EVD-20260627-0038

### INFO-039
- **タイトル:** AGI安全性政策論争激化 — 連邦AI規制先取りvs州権限・AI能力格差が核抑止崩壊の懸念・FLI「条約ビルダー」公開
- **ソース:** AI Frontiers・Japan Times・Lawfare・FLI/SaferAI・Fareed Zakaria
- **公開日:** 2026-06-25〜26
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-03, KIQ-002-03
- **関連企業:** （政府・規制機関一般）, Anthropic, OpenAI
- **要約:** AGI安全性の政策議論が核抑止レベルに拡大。AI Frontiers論文：AI能力格差が核抑止を危険にさらす可能性、大規模AI優位性を持つ攻撃者は報復を引き出さずに相手を武装解除できる可能性。連邦政府が州のAI規制権限を「技術寡頭」のために先取りしようとしているとの批判。Japan Times：世界は多国間条約交渉を待つ余裕なし、AIキルスイッチなき生活への警告。FLI（Future of Life Institute）がAI条約ビルダー公開（7つのガバナンス要素から条約案自動生成）。ICRCが自律型兵器新条約を要請。Roman Yampolskiy「AIが人類を壊滅させる確率99.9%」。
- **キーファクト:**
  - AI能力格差と核抑止：大規模AI優位攻撃者は相手の報復能力を事前無力化可能＝抑止の前提崩壊（AI Frontiers、Govind Pimpale 6/25）
  - 連邦vs州：連邦政府が州AI規制権限を先取り、tech oligarchsを優遇（州議員批判）
  - Fareed Zakaria：Washington-Anthropic対立は「一社の問題ではない」、AIを銀行規制のように扱うのは「bs」
  - Japan Times：「AIキルスイッチなき生活」＝多国間条約・全球規制機関設立を待つ余裕なし
  - FLI Treaty Builder：7ガバナンス要素選択でAI条約案自動生成（SaferAI経由）
  - ICRC：自律型兵器の新条約を要請。AIは軍事意思決定を支援できるが代替できない
  - Roman Yampolskiy（AI安全研究者）：AIが人類を壊滅させる確率「99.9%」
  - FY2026連邦資金：AI・重要鉱物・エネルギー・先進製造・労働力開発に大きく傾斜
- **引用URL:** https://ai-frontiers.org/articles/an-ai-capabilities-gap-can-endanger-nuclear-deterrence ; https://www.japantimes.co.jp/commentary/2026/06/26/world/an-ai-kill-switch/
- **Evidence ID:** EVD-20260627-0039

### INFO-040
- **タイトル:** Claude Code DAU公表データ不在（H-ANT-002動的クエリ結果）・Cursor DAU 100万超・企業AIツール利用追跡が課題
- **ソース:** Panto AI・Claude Support・Worklytics
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** H-ANT-002
- **関連企業:** Anthropic, Cursor
- **要約:** H-ANT-002動的クエリ「Claude Code DAU」の実行結果。Claude Codeの公開DAUデータは見つからず。AnthropicはTeam/Enterprise向けにClaude Coworkのセッション/日などの利用分析を提供するが、公開ベンチマーク数値なし。対照的にCursorは2025年時点でDAU 100万超を公表。企業AIツール（Copilot/Claude Code/Cursor等）のDAU/MAU追跡はWorklytics等の第三者ツールに依存する状況で、公式数値の不足が継続。Arbiter「H-ANT-002 Claude Code DAU」判断の更新材料なし。
- **キーファクト:**
  - Claude Code DAU：公開データなし。Anthropic公式発表なし（H-ANT-002「該当なし」継続の可能性）
  - Cursor DAU：100万超（2025年時点、Panto AI）。コーディングAI分野の参照値
  - Claude Cowork：Team/Enterprise向け利用分析（セッション/日等）提供するが公開数値なし
  - 企業AI追跡：Worklytics等がMAU/DAU/週次エンゲージメントを第三者計測。公式数値不足が構造的課題
  - DVU（Daily Value Users）指標への移行提案：DAUは「ログイン偽装」のPMF誤認リスク
- **引用URL:** https://www.getpanto.ai/blog/cursor-ai-statistics ; https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans
- **Evidence ID:** EVD-20260627-0040

### INFO-041
- **タイトル:** 主要LLM API価格比較 — Claude Sonnet $3/$15・Gemini 3.1 Pro $2/$12・Grok 3 $3/$15（1M tokens）・最安xAI $0.0375
- **ソース:** CostGoat・Google AI公式・Maxim AI(Bifrost)・AI Pricing Guru
- **公開日:** 2026-06-2x
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic, Google, xAI
- **要約:** 主要LLM API価格（1M tokensあたり）の2026年6月時点比較。Claude Sonnet 4.5/4.6：$3入力/$15出力。Gemini 3.1 Pro：$2入力/$12出力（Flash/Flash-Liteは更に安価、無料枠あり）。Grok 3：$3入力/$15出力（Claude Sonnetと同価格）。長文脈（200K超）はClaudeで$10/$37.50のプレミアムtier。コンテキストキャッシュはGemini $0.15-$1/1M・時間。最安APIはxAI Grok $0.0375/1M入力（5月時点、別モデルtier）。出力トークンは常に入力より高価。
- **キーファクト:**
  - Claude Sonnet 4.5/4.6：$3/1M入力、$15/1M出力。Claude Pro $20/月、Max $200/月、Team $25-125/シート
  - Gemini 3.1 Pro：$2/1M入力、$12/1M出力。Flash/Flash-Lite更に安価。無料枠（thinking tokens含む出力無料）。コンテキストキャッシュ$0.15-$1/1M時間
  - Grok 3：$3/1M入力、$15/1M出力（Maxim AI Bifrost）。Claude Sonnetと同価格帯。レート制限Tier 1($50)〜Tier 4($5,000)
  - 最安API：xAI Grok $0.0375/1M入力（AI Pricing Guru、5月時点）＝別モデルtierで圧倒的最安
  - 長文脈プレミアム：Claude 200K超で$10/1M入力、$37.50/1M出力（2026年初まで）
  - 出力トークン常に入力より高価（推理計算コスト反映）
- **引用URL:** https://costgoat.com/compare/llm-api ; https://ai.google.dev/gemini-api/docs/pricing ; https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/xai/model/grok-3
- **Evidence ID:** EVD-20260627-0041

### INFO-042
- **タイトル:** OpenAI IPO 2027年延期検討・評価額$852B・年収~$13B/純損失$21B・$1T評価額維持が条件
- **ソース:** NYT・Forbes・Facebook/Entrepreneur・Intellectia AI
- **公開日:** 2026-06-25〜26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** OpenAI
- **要約:** OpenAIがIPOを2027年まで延期する方向を検討（NYT独占報道）。2026年後半上場の当初計画から変更。目的は目標$1兆評価額を維持するため。アドバイザーは「2027年まで待って$1T評価額で公開」か「評価額を下げて2026年公開」の選択肢を提示。直近評価額$852B（3月31日クローズ資金調達ラウンド）。2025年収益~$13B、純損失$21B。S-1登録を秘密提出済み。
- **キーファクト:**
  - IPO延期：2026年後半→2027年へ検討。$1T評価額維持が延期理由（NYT、Forbes確認）
  - 評価額：$852B（2026年3月31日ラウンド、Forbes）。一部情報では~$920B
  - 収益：2025年~$13B、純損失$21B、$600B（コミットメント/推定资本支出、truncated）
  - S-1秘密提出済み。IPO準備は進行中
  - SpaceX上場の「rocky debut」がOpenAIの慎重姿勢に影響（Forbes）
  - AI IPOブーム文脈：SpaceX・OpenAI・Anthropicが三大IPO候補（Intellectia AI）
- **引用URL:** https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html ; https://www.forbes.com/sites/aliciapark/2026/06/25/openai-considers-delaying-ipo-to-2027-after-spacexs-rocky-debut-report-says/
- **Evidence ID:** EVD-20260627-0042

### INFO-043
- **タイトル:** Anthropic 年次実行利益Q2 2026 $559M初達成・ARR $47B・評価額$380B→3倍化・IPO準備
- **ソース:** CNBC・letsdatascience・Entrepreneur・Reddit
- **公開日:** 2026-06-25〜26
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04, KIQ-OAI-001
- **関連企業:** Anthropic, OpenAI
- **要約:** AnthropicがQ2 2026で初の四半期営業利益$5.59億を予想（収益$109億、前Q比+130%）。年次実行レート$47B（5月、CNBC）＝2025年通期$10Bから急拡大。評価額は2026年2月$380Bから3倍近く上昇。IPO準備でS-1提出。Dario Amodei「収益継続なら数千万人のAI Agentが企業向けに兆円規模の価値を創出」。CNBC（6/26）：OpenAI・Anthropic共に「ユーザー効率志向への移行」という新たなAI支出現実に直面。
- **キーファクト:**
  - Q2 2026予想：収益$10.9B（前Q比+130%）、営業利益$5.59億＝初の四半期黒字（letsdatascience）
  - ARR軌跡：2022年$10M→2024年初$87M→2025年末$9B→2026年5月$47B年次実行レート
  - 評価額：2026年2月$380B→現在約3倍（~$1T+？）。IPO準備中
  - 収益成長率：2025年通期$10B→2026年5月$47B年次実行レート＝約5倍ペース
  - Dario Amodei：数千万人AI Agentが「兆円規模の価値」創出する構想
  - CNBC 6/26：OpenAI・Anthropic「新たなAI支出現実」＝ユーザーが効率志向に移行、価値あたり支出最適化
  - 対OpenAI比較：OpenAI 2025年$13B収益/Anthropic 2025年$10B収益。Anthropic黒字化が先宗旨
- **引用URL:** https://letsdatascience.com/blog/anthropic-first-operating-profit-q2-2026-559-million ; https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality-as-users-shift-to-efficiency.html
- **Evidence ID:** EVD-20260627-0043

### INFO-044
- **タイトル:** Alibaba Qwen 3.7-Plus コンピュータ使用AI・7変種リリース最高頻度・ただしOSS化後退懸念・GLM-5.2が後発OSS
- **ソース:** Alibaba Cloud公式・Reddit r/LocalLLaMA・Digital Applied・Threads
- **公開日:** 2026-06-1x〜22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Alibaba, ByteDance, Zhipu(GLM)
- **要約:** Alibaba Qwen3.7-Plusがスクリーン・コーディング・クラウドコンソール自動化をターゲットとするコンピュータ使用AIとして登場。Alibabaは2026年1月-4月に7つのQwen変種をリリースし「最高頻度リリース企業」。しかしReddit r/LocalLLaMAで「Qwen 3.7はOSS化されないのでは」懸念拡大、OSS後退トレンド指摘。対照的にGLM-5.2(Zhipu)が6月17日にOSS化、Qwenより新しいOSSモデルに。Qwen 2.5-Maxもローンチ済み。Alibaba Cloud Model Studioは6月22日更新。
- **キーファクト:**
  - Qwen3.7-Plus：スクリーン/コーディング/クラウドコンソール自動化（ブラウザ越えのコンピュータ使用AI）
  - Alibaba最高頻度リリース：2026年1/23-4/2で7変種リリース＝単一最高頻度（Digital Applied Frontier Model Release Velocity Index Q2 2026）
  - OSS化後退懸念：Reddit「Qwen 3.7はOSS化されないのでは？」→小規模モデルのOSS化停止トレンド懸念
  - GLM-5.2（Zhipu）：2026年6月17日OSS化＝Qwenより新しいOSS選択肢
  - Qwen 2.5-Max：別ラインとしてローンチ。Alibaba Cloud Model Studio 6/22更新でQwen+サードパーティモデル提供
  - IND-031「OSS vs商業のサイクル」関連：Qwen OSS化後退 vs GLM新規OSS化＝競争内でOSS戦略分化
- **引用URL:** https://www.digitalapplied.com/blog/frontier-model-release-velocity-index-q2-2026 ; https://www.reddit.com/r/LocalLLaMA/comments/1ubjnh5/qwen_is_never_going_to_open_source_qwen_37_arent/
- **Evidence ID:** EVD-20260627-0044

### INFO-045
- **タイトル:** コーディングベンチマーク — Terminal-Bench 2.0首位GPT-5.5(0.827)・SWE-bench Pro首位Claude Opus 4.8(69.2%)・Codex/Claude Code棲み分け
- **ソース:** LLM Stats・Morph・TechJackSolutions・GitHub(awesome-llm-bench)
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Moonshot
- **要約:** 主要コーディングベンチマークでOpenAIとAnthropicが指標別に棲み分け。Terminal-Bench 2.0（ターミナル自律実行）はGPT-5.5が0.827で首位（48モデル中）。SWE-bench Pro（実コード修正）はClaude Opus 4.8が69.2%で首位、GPT-5.5は58.6%。Morph比較分析：Claude CodeはSWE-bench系で強く、CodexはTerminal-Bench系で強い構造。Kimi K2.7-CodeはMoonshot独自指標。GitHub awesome-llm-benchがSWE-bench Verified/Terminal-Bench/OSWorld/ARC-AGI-2/HLEの日次同期リーダーボード提供。
- **キーファクト:**
  - Terminal-Bench 2.0首位：GPT-5.5 0.827（48モデル中、LLM Stats）。GPT-5.3 Codex 77.3%（別版/スコア）
  - SWE-bench Pro首位：Claude Opus 4.8 69.2%（5/28リリース）、GPT-5.5 58.6%（Morph比較）
  - 指標別強弱：Terminal-Bench=GPT系優位、SWE-bench=Claude系優位＝実行 vs 修正の棲み分け
  - Agenticスコアはscaffold/ツール構成に高感度（TechJackSolutions注意喚起）
  - Kimi K2.7-Code：Moonshot独自コーディングベンチマーク（SWE-bench/Terminal-Benchとは別物）
  - 日次同期リーダーボード：awesome-llm-bench（GitHub）が主要5指標カバー
- **引用URL:** https://llm-stats.com/benchmarks/terminal-bench-2 ; https://www.morphllm.com/comparisons/codex-vs-claude-code
- **Evidence ID:** EVD-20260627-0045

### INFO-046
- **タイトル:** OpenAI Sora事業撤退（財政持続不可能）・Alibaba動画AI全球2位浮上・コミュニティSora 2 API存続要請
- **ソース:** VentureBeat・Reddit r/SoraAi・OpenAI Community・AtlasCloud
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-04, KIQ-003-04
- **関連企業:** OpenAI, Alibaba, ByteDance
- **要約:** OpenAIが動画生成モデルSoraを財政的持続不可能を理由に事業撤退・廃止。VentureBeat：SoraとByteDance Seedanceがランキングから「fall away」する中、Alibaba動画AIモデルが全球2位に浮上。OpenAI Communityで「Sora 2 API存続要請」 petitions発生、「Sora 2は最もリアルで比類ない」との声。AI動画市場は2026年に3つの企業コンテンダーで始まったが構図変化。AtlasCloudはSora 2を「物理精度の突破口」と評価するも事業撤退決定済み。
- **キーファクト:**
  - Sora事業撤退：OpenAIが「financially unsustainable」を理由にSora廃止（VentureBeat）
  - Alibaba動画AI全球2位浮上：Sora・Seedance「fall away」の逆 bénéficiaire
  - コミュニティ反応：「Save the Sora 2 API」 petitions（OpenAI Community）。Sora 2を「最もリアル」と評価
  - AI動画市場3コンテンダー（2026年初）→ Sora撤退で構図再編
  - Sora 2技術評価：「物理精度の再定義」「デジタルリアリズムの突破口」（AtlasCloud）＝技術優位も商業化失敗
  - ByteDance Seedance 2.5（INFO-037参照）は30秒4Kで競争継続中
- **引用URL:** https://venturebeat.com/technology/alibabas-ai-video-model-rises-to-no-2-in-global-rankings-as-openais-sora-and-bytedances-seedance-fall-away ; https://community.openai.com/t/save-the-sora-2-api-and-please-do-not-discontinue/1384892
- **Evidence ID:** EVD-20260627-0046

### INFO-047
- **タイトル:** AIベンダーロックイン — CIO「利益も存在」・EU DMAがAWS/Azure調査・オープン標準で軽減・ワークロード別セグメント化戦略
- **ソース:** CIO.com・HackerNoon・DataEdge・WindowsForum・Facebook/CIO
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-05, KIQ-002-01
- **関連企業:** AWS, Microsoft Azure, Google Cloud
- **要約:** AI時代のベンダーロックインが複雑化。CIO.comは「AIスタック選択でロックインの利益」を提唱：より深い統合と性能を代償に得る。一方EU DMAゲートキーパー調査がAWS・Azureを対象化、クラウドロックインとAI電力の交差点を調査。HackerNoon：深科技企業でのロックイン隠蔽コストはPLM/MES/ERP/クラウドAI全体に波及。推奨戦略：ワークロードを性能/コスト/リスク感度別にセグメント化し、単一戦略を全社適用しない。オープン標準が伝統的ロックイン軽減の鍵。
- **キーファクト:**
  - CIO「ロックインの利益」：より深い統合・性能・サポートvs切替コスト高のトレードオフ
  - EU DMAゲートキーパー調査：AWS・Azure対象。クラウドロックイン×AIモデル学習×データ倉庫×政府依存の包括調査
  - ワークロード別セグメント化：性能/コスト/リスク感度で振り分け、全社単一戦略回避（CIO推奨）
  - マルチクラウド戦略：(1)ロックイン排除=価格交渉力維持、(2)稼働率最大化、(3)規制対応
  - オープン標準：クラウド/統合/データの伝統的ロックイン軽減、AI時代に更に重要化（CIO Facebook）
  - 深科技の隠蔽コスト：PLM/MES/ERP/クラウドAI全体で依存コスト累積（HackerNoon）
- **引用URL:** https://www.cio.com/article/4188503/choosing-your-ai-stack-the-benefits-of-vendor-lock-in.html ; https://windowsforum.com/threads/eu-dma-gatekeeper-probe-targets-aws-and-azure-cloud-lock-in-meets-ai-power.430847/
- **Evidence ID:** EVD-20260627-0047

### INFO-048
- **タイトル:** コーディングAI ROI — エンジニア20-25%生産性向上・Copilot利用者126%多くプロジェクト完了・Vibe Coding普及
- **ソース:** Facebook/JoyAtTech・UiPath・GitHub/LinkedIn・YouTube
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-02, KIQ-002-02
- **関連企業:** GitHub(Microsoft), Cursor, Anthropic, UiPath
- **要約:** コーディングAI投資のROI定量化が進む。エンジニア1人あたり20-25%生産性向上がコンセンサス値。GitHub Copilot利用者は週次126%多くプロジェクト完了。UiPathはコーディングAgentに「最初のプロンプトから本番デプロイまで」の完全ツールチェーン提供、「ROI投資前に価値証明」を掲げる。「Vibe Coding」（速度>構造、自然言語で要件記述→AI構築）が普及。GitHubは長時間AgenticセッションでのCopilot効率改善データ公開。「tokenmaxxing」越えのDevEx測定が新課題。
- **キーファクト:**
  - ROI定量化：エンジニア1人20-25%生産性向上（JoyAtTech、UiPath一致）
  - GitHub Copilot：利用者は週次126%多くプロジェクト完了
  - Vibe Coding：自然言語で成果物記述→AI構築。スピード>構造のパラダイム（JoyAtTech）
  - UiPath：プロンプト→本番デプロイの完全ツールチェーン。「ROI: 投資前に価値証明」
  - ツール群：Cursor、GitHub Copilot、Claude Code、Antigravity（2026 AI Stack Guide）
  - GitHub：長時間AgenticセッションでのCopilot効率改善データ公開（LinkedIn）
  - 測定課題：「Life beyond tokenmaxxing」＝効率だけでなくDevEx（開発者体験）測定が必要
- **引用URL:** https://www.facebook.com/joyatrestech/posts/1612473740883254/ ; https://www.linkedin.com/posts/halotechlabs_getting-more-from-each-token-how-copilot-activity-7474464995603386368-1m-j
- **Evidence ID:** EVD-20260627-0048

### INFO-049
- **タイトル:** 再帰的自己改善の進展 — Anthropic基盤モデル自らコード記述で実現・DeepMind AGI→ASI四経路論文・Recursive社がSOTA達成
- **ソース:** LinkedIn(PLDI 2026)・Turing Post・Business Standard・Import AI 462・MindStudio
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** Anthropic, Google DeepMind, Recursive
- **要約:** AIの再帰的自己改善（Recursive Self-Improvement: RSI）が具体化。Anthropicが自社基盤モデルが自らコードを記述することで「recursive self improvement」を達成した旨をブログで言及（PLDI 2026基調講演引用）。RSIは単なるファインチューニングを超え、データ生成・訓練手法・アーキテクチャ・評価手法を含むモデル構築ループ全体の自己改善を目指す。Google DeepMindがAGI→ASI（超人工知能）への四経路論文を公表、RSIを主要経路の一つとして位置付け。Recursive社が言語モデル訓練・小規模モデル訓練速度・GPUカーネル最適化で新SOTA達成。
- **キーファクト:**
  - Anthropic RSI：基盤モデルが自らコード記述で「recursive self improvement」達成（PLDI 2026基調講演/Miryung Kim引用）
  - RSI定義：モデル構築ループ全体（データ/訓練手法/アーキテクチャ/評価/将来AI構築）を自己改善（Turing Post）
  - DeepMind AGI→ASI四経路論文：RSIを主要経路の一つとして特定（MindStudio解説）
  - Recursive社：言語モデル訓練・小規模モデル訓練速度・GPUカーネル最適化で新SOTA（Import AI 462）
  - Business Standard：「AIがAIを構築するのがAGIへの道か？」＝RSIのAGI到達可能性を一般議論化
  - リスク：RSIが成功すれば制御可能性問題が現実化（KIQ-005-03安全性議論と連動）
- **引用URL:** https://www.linkedin.com/posts/karlunho_pldi-2026-flatirons-234-pldi-keynotes-activity-7474141289907634176-E1B0 ; https://www.mindstudio.ai/blog/google-deepmind-agi-to-asi-paper-four-pathways
- **Evidence ID:** EVD-20260627-0049

### INFO-050
- **タイトル:** AIによる専門職代替の実態 — 「代替でなく増強」がコンセンサス・Jevonsパラドックス（効率化→需要増）・法務/医療/管理職で人間特有能力不可欠
- **ソース:** Wolters Kluwer・Stanford Medicine・DistilINFO・SHRM・CIMA
- **公開日:** 2026-06-2x
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-01, KIQ-002-04
- **関連企業:** （専門職業業界一般）, Wolters Kluwer, SHRM
- **要約:** AIによる専門職代替の実態が「代替でなく増強」でほぼコンセンサス。法務：AIが文書レビュー/リサーチを効率化するが弁護士を代替せず、効率化が逆に法的サービス需要を増加させる（Jevonsパラドックス、Wolters Kluwer）。医療：AIが医師を代替することは近くない、AIを活用する医師が優位に立つのみ（DistilINFO/Stanford）。SHRM 2026報告：AIが代替できない管理職能力（複雑判断・対人スキル・意思決定）を本質的と特定。CIMA：AIが専門家をインサイト/判断/戦略に集中させる。
- **キーファクト:**
  - Jevonsパラドックス（法務）：AI効率化→法定サービス需要増→チーム拡大継続（Wolters Kluwer）
  - 医療：「AIが医師を代替することは近くない」、AIを使う医師が優位（DistilINFO、Stanford Medicine）
  - SHRM 2026職場AI報告：複雑判断・対人スキル・意思決定はAI代替不可、管理職の本質的特質
  - CIMA（管理会計士）：AIがインサイト/判断/戦略への集中を可能化、専門職の価値向上
  - 一般原則：「AIが人間を代替する」ではなく「AIを使う人間が使わない人間を代替する」
  - KIQ-004-03（AI-proof能力）と整合：感情知能・批判的思考・創造性が不可欠（INFO-030参照）
- **引用URL:** https://www.wolterskluwer.com/en/expert-insights/why-legal-teams-are-still-growing-in-the-age-of-ai ; https://www.shrm.org/topics-tools/research/navigating-ai-in-the-workplace/full-report
- **Evidence ID:** EVD-20260627-0050
