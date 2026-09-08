# Anthropic PBC — 攻撃的投資仮説 (static_intelligence)

- **最終判断更新:** 2026-09-08 (前回 2026-09-07)
- **全体確信度:** 中 (公式一次の覆盖が価格面で前進・収益面はS-1待ち)
- **情報非対称性:** 価格は公式pricingページのライブ検証でSonnet 5現行$2/$10が確定し$3/$15は4.x世代価格と判明したが、9/7 INFO-057出所ページ (models/overview) との矛盾が未解決で台帳訂正は条件付き。調達系列は3変種並存注記 (台帳G$30B+H$65B=$95B / 9/7注記G$32B+H$27.5B=$59.5B / Bloomberg ET見出し$65B説) となり$59.5B説の出所特定が残件。$15BリボルバーとIPO提出が「枠確定待ち」で直列である構造は判明したが、監査財務はS-1本文まで不在。判決は8/27・Judge Rita F. Linが2ソース一致したがドケット正規一次は未取得。Claude Code 39%は集約業者経由のまま。
- **主参照:** [config/hypotheses.json](../config/hypotheses.json) · [config/indicators.json](../config/indicators.json) · [state/arbiter-2026-09-08.md](../state/arbiter-2026-09-08.md) · [Information/2026-09-08/collected-raw.md](../Information/2026-09-08/collected-raw.md)

## §0 一文要約

我々はAnthropicを「司法勝利の経済的果実が意図的な調達除外で得られない構造が確定しつつ、価格と資本の両面で公式一次が揃い始めた企業」と読む。公式pricingページのライブ検証 ([INFO-088](../Information/2026-09-08/collected-raw.md#INFO-088)・A-2) でSonnet 5現行価格$2/$10が確定し、$3/$15はSonnet 4.6/4.5/4の価格と判明した (v4.88「値上げ復帰」前提の反転・ただしmodels/overview再取得まで条件付き)。Fable 5.1/Mythos 5.1は同一モデルでセーフガードのみ相違する公開設計 ([INFO-091](../Information/2026-09-08/collected-raw.md#INFO-091)・A-2) で、キャッシュ読取75%値下げ・EFS・LSVPが公式確定した。調達面は$15Bリボルバー (Morgan Stanley主導・14行超・段階制コミット) の確定を待ってIPO提出が進む構造 ([INFO-082](../Information/2026-09-08/collected-raw.md#INFO-082)/[INFO-087](../Information/2026-09-08/collected-raw.md#INFO-087)) が判明し、IPOは10月中旬視野。仮説確度は全件±0% (v4.89)。もし10月中旬の公的S-1が監査財務を開示すれば、収益と評価額の系列分裂は一斉に解消に向かう。

## §1 コア判断

価格判断は公式一次で書き換わった。platform.claude.com公式docsのライブ取得 ([INFO-088](../Information/2026-09-08/collected-raw.md#INFO-088)・A-2) により、Sonnet 5は$2/MTok入力・$10/MTok出力が現行で、$3/$15はSonnet 4.6/4.5/4世代の価格と確定した。9/7のINFO-047矛盾検出からStep 4公式ライブ検証への格上げチェーンが模範的に完走した形で、v4.88裁定4「$3/$15復帰」の前提は反転した。ただし台帳訂正の確定は9/7 INFO-057出所ページ (models/overview) のライブ再取得まで条件付きで、両ページが現行も矛盾する場合は公示不整合系列として扱う (Arbiter v4.89裁定2)。全価格体系はFable 5.1/Mythos 5.1が$10/$50、Opus 5が$5/$25、Haiku 4.5が$1/$5、Fast mode (Opus 5/4.8) が$10/$50の2倍速research preview、Claude Managed Agentsがトークン+セッション実行時間$0.08/時の2軸課金と判明した。Mythos SKUの階層分離 ($25/$125 Preview・限定と$10/$50 5.1・limited availability) は監視在庫化され要追証とする。

Fable 5.1/Mythos 5.1の公式発表全文 ([INFO-091](../Information/2026-09-08/collected-raw.md#INFO-091)・A-2) は同一モデル・異なるセーフガードという設計思想の公式開示である。キャッシュ読取を75%値下げ ($0.25/MTok・他モデルの0.1xに対し0.025x) して典型的ワークロード約25%、高度エージェント用途で最大約45%のコスト削減と主張する。Enterprise Frontier Safeguards (EFS) は顧客管理クラウドでZDR同等を両立 (100+顧客共同開発・AWS/GCP/Azure・今秋段階提供)、LSVPで米政府生命科学提携も継続する。科学面は蛋白質バインダー設計で12標的ヒット率約50% (業界標準10-15%・外部2機関の実験検証付き) と金星の新地形図 (NASA Magellan-derived・CC公開) で、性能主張と異なり実測検証を伴う信頼構造を持つ。整列面は承認・auto-mode分類器を時々バイパス可能と公式に認識し、アンチ蒸留 (thinking付き文脈編集不可) も導入した。Claude Managed Agents (INFO-088) とxAI Haggle Bot ([INFO-090](../Information/2026-09-08/collected-raw.md#INFO-090)) の同週登場で、エージェント課金と企業ワークフロー統合の競争が始まっている。

資本と司法の構造が判明した。$15Bリボルバーは8月目標$10Bの1.5倍で、段階制コミット ($1.25B IPO主幹事4行Anchor・$1B・$750M超) のMorgan Stanley主導14行超シンジケート ([INFO-087](../Information/2026-09-08/collected-raw.md#INFO-087)・B-2)。各行がIPO役割確保を目当てにコミットし、Anthropicは枠確定を待ってIPO提出を遅延させる ([INFO-082](../Information/2026-09-08/collected-raw.md#INFO-082)・B-2)。IPO観測機は「10月中旬以降・S-1本文監査財務のみ」に構造化され、評価額$2T到達可能性が報じられている。資本系列は台帳のG$30B (2月・$380B) +H$65B (5/28・$965B)=$95Bに対し、9/7 raw注記の$59.5B説とBloomberg ET見出しの$65B説が並存し、3変種注記として$59.5B説の出所特定がKIQ-ANT-002-CAPに追加された (Arbiter v4.89裁定6)。司法は2026-08-27・カリフォルニア北区連邦地裁Judge Rita F. LinがAnthropic側に大部分支持と2ソース一致 ([INFO-085](../Information/2026-09-08/collected-raw.md#INFO-085)・B-2) で事実命題の精度が向上したが、正規一次不在のためB天井を維持する。

需要側の警告は強まり続ける。IND-013 (critical/rising) はCVSS 10のMCP脆弱性の能動的悪用と、OSV/GHSA掲載の18悪性npmパッケージによるAIコーディングエージェント遠隔制御 ([INFO-084](../Information/2026-09-08/collected-raw.md#INFO-084)・C-2・dev.to単一出所) を計上し、Claude Code/.mcp.json系列への需要側接続の初実装形候補となった。P-7 (需要側接続初実装形) の確度は「中-高」から「中」へ修正された (Arbiter v4.89裁定7)。CVE/GHSA個別識別子は6日目も未特定で、初回掲載日と規模測定が収集指示化されている。

## §2 判断の重心

| 重心 | 主張 | 判断根拠 | 信頼度 | 証拠 |
|---|---|---|---|---|
| 高 | Sonnet 5現行$2/$10確定・$3/$15は4.x価格。Fable/Mythos 5.1=$10/$50・Opus 5=$5/$25・Managed Agents $0.08/時 | 公式pricingページのライブ検証。v4.88前提の反転 (台帳訂正はmodels/overview再取得まで条件付き) | A-2 | [INFO-088](../Information/2026-09-08/collected-raw.md#INFO-088) |
| 高 | Fable 5.1/Mythos 5.1は同一モデル・セーフガード相違。キャッシュ75%値下げ・EFS・LSVP・蛋白質50%・金星地図 | 公式発表全文。実測検証付きの差別化事例 (外部2機関) | A-2 | [INFO-091](../Information/2026-09-08/collected-raw.md#INFO-091) |
| 高 | $15Bリボルバー (段階制コミット・MS主導14行超) 確定待ちでIPO提出遅延・10月中旬・評価$2T可能性 | S-1観測機の構造判明。H-ANT-002資本基盤の新柱候補 (監査財務は依然不在) | B-2 | [INFO-082](../Information/2026-09-08/collected-raw.md#INFO-082) [INFO-087](../Information/2026-09-08/collected-raw.md#INFO-087) |
| 高 | 資本系列3変種並存 ($95B台帳/$59.5B 9/7注記/$65B Bloomberg ET見出し) | 定量的錨は台帳G+H=$95Bのまま。$59.5B説出所特定が残件 (裁定6) | B-2 | [INFO-087](../Information/2026-09-08/collected-raw.md#INFO-087) |
| 中 | 判決2026-08-27・Judge Rita F. Lin・Anthropic側に大部分支持・控訴継続中 | H-GOV-001の事実命題精度向上 (v4.88「≈8/31」→確定値)。正規一次不在でB天井維持 | B-2 | [INFO-085](../Information/2026-09-08/collected-raw.md#INFO-085) |
| 中 | ペンタゴン300万人展開でOpenAI/SpaceXAI各最大$200M・Anthropicは意図的除外 (Hegseth批判公言化) | H-GOV-002 C側の事象単位6度目のC計上 (純新規は命名のみ) | B-2 | [INFO-035](../Information/2026-09-08/collected-raw.md#INFO-035) |
| 低 | CVSS 10 MCP脆弱性の能動的悪用+18悪性npmがAIコーディングエージェントを遠隔制御 | IND-013需要側系列。P-7確度「中」 (dev.to単一出所・識別子未特定) | C-2 | [INFO-084](../Information/2026-09-08/collected-raw.md#INFO-084) |

## §3 反証の閾値

| 監査点 | 反証内容 | タイムボックス | 接続先 |
|---|---|---|---|
| models/overviewページのライブ再取得 | $2/$10と$3/$15の矛盾の判別。反転確定か公示不整合系列かが確定し台帳訂正の取消/変質が判定される | 次回収集 (最優先) | SCN-004 [IND-027](../config/indicators.json) |
| Mythos SKU階層・配給判別データ (資格要件・拒否事例・Fast mode可用性) | 管理配給の実質判定。SCN-001 vs SCN-004配分審査の発火 (裁定8事前登録) | 90日 | SCN-001 H-ANT-001 |
| $59.5B説の出所特定 (9/7 raw注記の系譜) | 資本系列3変種の解消。正しければG/H 2独立ラウンド構造自体の再検証 | 次回収集 | H-ANT-002 [KIQ-ANT-002-CAP] |
| 公的S-1の監査財務 (収益・評価額の単一確定値) | 収益系列分裂 (消費者$1.6B/run-rate $6-10B/2026年$26B/2027年$52-66B) の一斉解消または特定系列の棄却 | 2026-10-31 | H-ANT-002 [IND-026](../config/indicators.json) |
| ドケット3:26-cv-1996正規一次の取得 | 判決正文と控訴状況の公式確認。B天井解除または判決内容の修正 | 継続 | H-GOV-001 |
| $15B枠の最終確定とIPO提出の実行 | 観測機構造 (枠確定待ち→提出の直列) の検証 | 2026-10-31 | H-ANT-002 [IND-029](../config/indicators.json) |
| CVE/GHSA識別子と18悪性npmの規模測定 | IND-013需要側系列の規模判定とP-7確度の再評価 | 次回収集 | [IND-013](../config/indicators.json) |
| Claude Code直接定量 (公式文書由来の39%検証) | 集約業者系列の解消 | 継続 | [IND-026](../config/indicators.json) |

## §4 アクティブ仮説 (v4.89)

| ID | 仮説 | 確度 | v4.89根拠 |
|---|---|---|---|
| H-ANT-001 | 未整備状態の主要モデルが市場を支配する | 35% low | INFO-091のバイパス可能認識とGray Swan外部テストは両義材料。確度不変 (v4.89±0%) |
| H-ANT-002 | 2030年までにAnthropicは最初の上場フロンティアラボになる | 52% low | S-1観測機の構造判明 ($15B枠確定待ち→IPO 10月中旬)。資本3変種注記追加。C-only警告カウンター制度化 (裁定4)。±0% |
| H-ANT-003 | Claude Code型CLIはフォークされず定着する | 6% low | 新規材料なし。±0% |
| H-GOV-001 | 現行司法判決は供給制限の事実上の恒久化である | 46% medium | 判決日8/27・Lin判事2ソース一致で精度向上・正規一次不在B天井・N=1実質35R。±0% |
| H-GOV-002 | フロンティアモデルの政府调達は30%以上が単一政党に依存する | 24% low | C側累積 (国際認知・利益相反・交換構造) は全てB/C級で「B系一次なし変更却下」。$200M×2は6度目のC計上。±0% |
| H-CAR-001 | フロンティアAI労働市場は中間層の構造的欠落に収束する | 36% low | C側 (WPP 18,000職) とI側 (再雇用・16%整備・ROI 8ヶ月摩擦) が同日釣り合い・NY連銀本文8日目未取得。±0% |
| H-CAR-002 | 2030年までに主要経済はフィジカル制約を実質ゼロにする | 58% medium | P(B)固有B-2と不在継続。C-only警告カウンター制度化 (裁定4)。±0% |
| H-CAR-003 | 非コンサル型中間シェルは2031年までに主要企業層へ波及する | 57% medium | 中間工程の新規定量なし。±0% |

## §5 関連指標 (v4.89)

| 指標 | 現在値 | 解釈 |
|---|---|---|
| [IND-013](../config/indicators.json) | critical / rising | CVSS 10 MCP能動悪用+18悪性npm (INFO-084・C-2)。需要側接続の初実装形候補・P-7確度「中」 (裁定7)。識別子6日目未特定 |
| [IND-025](../config/indicators.json) | elevated / stable | OSS追従2件 (Qwen3.8 Max 1.3pt・GLM 5 0.3pt) は不充足。交叉確認ガード(A)はARC-AGI-3公式値も同一ベンチ家族自己申告で不充足 |
| [IND-026](../config/indicators.json) | high / rising | 収益系列分裂とClaude Code直接定量不在が継続 (調達G/Hは解消・3変種注記) |
| [IND-027](../config/indicators.json) | high / rising | Sonnet 5 $2/$10標準化を公式ライブ検証で床側確認 (INFO-088)。$3/$15は4.x価格。反転確定は再取得まで条件付き (裁定2) |
| [IND-028](../config/indicators.json) | high / rising | 現行週の予測分裂 (AGI era vs 数十年先) +素数ギャップ証明公開 (外部検証待ちの一次級適合例) |
| [IND-029](../config/indicators.json) | high / rising | 第1観測機=OpenAI銀団3値強制判定・観測窓閉鎖≈2026-09-09 (機械的執行義務)。Anthropic $15Bリボルバー1.5倍増額 (INFO-082/087) |
| [IND-030](../config/indicators.json) | critical / rising | N=1実質35R。Astra「監視可能性低下」公式自己開示 (INFO-089・A-2)。Anthropic S-1観測機は10月中旬 |

## §6 変化履歴

| 日付 | 変更内容 | きっかけ | 確度変動 |
|---|---|---|---|
| 2026-09-08 | 台帳訂正に伴う全面書き直し。公式pricingライブ検証 (INFO-088) でSonnet 5 $2/$10現行確定 ($3/$15=4.x価格・v4.88前提の条件付き反転)。Fable/Mythos 5.1公式全文 (同一モデル・EFS・LSVP) と$15Bリボルバー/IPO構造・資本3変種注記・判決日8/27確定を新規計上。§5をv4.89値に更新 | Arbiter v4.89裁定2/6 + [INFO-088](../Information/2026-09-08/collected-raw.md#INFO-088)/[091](../Information/2026-09-08/collected-raw.md#INFO-091) | 全件±0% |
| 2026-09-07 | 収益系列分裂とClaude Code 39%出所注記。調達系列のG/H文字逆転解消 (Series G=2月$30B@$380B・H=5/28 $65B@$965B) | Arbiter v4.88 + INFO-075 | 全件±0% |
| 2026-09-06 | Sonnet 5 $3/$15復帰検証とDaybreak社内SNS投稿の無期化/一段階化集計 | Arbiter v4.87 | 全件±0% |
| 2026-09-05 | $2T IPO報道初出・H-GOV-001 45→46% (判決あり報道2ソース) | Arbiter v4.86 | H-GOV-001 +1% |
| 2026-09-03 | Claude Opus 5発表・蛋白質・セーフガード差し替え構造を§1/§2に反映 | Arbiter v4.84 | - |

## §7 既知の限定とブラインドスポット

1. pricingページとmodels/overviewページの矛盾が未解決である。台帳訂正の取消確定は再取得まで条件付きで、両ページが現行も矛盾すれば公示不整合系列として第2事例は取消でなく変質存続となる (裁定2)。
2. Mythos SKU階層 ($25/$125 Preview vs $10/$50 5.1) が要追証のまま。配給の資格・拒否事例・Fast mode可用性の判別データがSCN-001分岐審査の発火条件 (裁定8)。
3. 資本系列3変種並存 ($95B/$59.5B/$65B)。$59.5B説が正しければ2独立ラウンド構造自体の再検証が必要で、出所特定は次回収集の残件。
4. ドケット3:26-cv-1996正規一次と控訴審状況が未達。判決解釈はB-2報道2ソースに依存している。
5. Claude Code 39% ($2B+ ARR) は集約業者経由で、公式文書による直接検証が不在。
6. C-only警告の連続ラウンド数が機械記録化された (裁定4) が、これは陳腐化検出の制度化であって警告自体の解消ではない。H-ANT-002は52%で±0%継続。

## 付録A 直近30日の参照Evidence

| 日付 | 証拠 | 信用 | 事項 |
|---|---|---|---|
| 2026-09-08 | [INFO-088](../Information/2026-09-08/collected-raw.md#INFO-088) | A-2 | 公式pricingライブ検証: Sonnet 5=$2/$10確定・$3/$15は4.x価格 (裁定2の条件付き台帳訂正) |
| 2026-09-08 | [INFO-091](../Information/2026-09-08/collected-raw.md#INFO-091) | A-2 | Fable 5.1/Mythos 5.1公式全文: 同一モデル・EFS・LSVP・蛋白質50%・金星地図 |
| 2026-09-08 | [INFO-082](../Information/2026-09-08/collected-raw.md#INFO-082) [INFO-087](../Information/2026-09-08/collected-raw.md#INFO-087) | B-2 | $15Bリボルバー14行超・段階制コミット・IPO提出遅延 (10月中旬・$2T可能性) |
| 2026-09-08 | [INFO-085](../Information/2026-09-08/collected-raw.md#INFO-085) | B-2 | 判決2026-08-27・Judge Rita F. Lin・Anthropic側大部分支持 (2ソース一致) |
| 2026-09-08 | [INFO-035](../Information/2026-09-08/collected-raw.md#INFO-035) | B-2 | ペンタゴン300万人展開・OpenAI/SpaceXAI各$200M・Anthropic意図的除外 (6度目C計上) |
| 2026-09-08 | [INFO-084](../Information/2026-09-08/collected-raw.md#INFO-084) | C-2 | CVSS 10 MCP能動悪用+18悪性npm (IND-013・P-7確度「中」) |
| 2026-09-07 | [INFO-075](../Information/2026-09-07/collected-raw.md#INFO-075) | A-2 | Series G (2月$30B@$380B) / Series H (5/28 $65B@$965B) の文字逆転解消 |
| 2026-09-07 | INFO-057 | A-2申立 | models/overviewの$3/$15表示 (INFO-088と矛盾・再取得待ち) |
| 2026-09-06 | INFO-064 | B-2 | $2T IPO評価額報道 (後のINFO-082/087で構造確定) |
| 2026-09-05 | INFO-065 | B-1 | GenAI.mil 300万人展開本体 (H-GOV-002 C側) |
