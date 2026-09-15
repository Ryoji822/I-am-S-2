# Google / DeepMind

> 最終判断更新: 2026-09-15
> 全体確信度: 測定不能（H-GOO-001 indeterminate維持）
> 情報非対称性: Gemini固有のエンタープライズ定量採用データ（シェア・収益・利用率の直接定量A-2+）は60R超にわたり構造的に不在。MAUは消費者指標でありエンタープライズ採用シェアではない。UBS試算はGoogle Cloud収益の27%（2026）→48%超（2027）がOpenAI+Anthropicの2社依存と定量化し、Cloud収益成長とGemini固有需要の分離不能性が拡大したまま。Interactions APIはv1betaのdocs層でGA・課金単位・採用条件は未公告（[INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006) A-3）。Hassabis「もはやDeepMindを率いない」報道は要追証（[INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) B-2）。フィンランド€13B投資は報道ベース（[INFO-081](../Information/2026-09-15/collected-raw.md#INFO-081) B-2）。Flash系3.6〜3.8の期限付き価格と2027/1/1倍額移行は公式公示済み（[INFO-066](../Information/2026-09-15/collected-raw.md#INFO-066) A-3）。
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はGoogleを「Interactions APIというエージェント対話単位の新API形状とサブエージェント階層を想定したモデル編成で開発者面の供給を広げながら、固有の採用定量だけが現れ続けない企業」と読む。Gemini API公式docsにInteractions API（v1beta/interactions・generateContentと別系統）が登場し、Gemini 3.8 Flashは長時間ソフトウェアエンジニアリングと自律エージェント向け、3.5 Flash-Liteはサブエージェント向けと明記された ([INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006) A-3)。価格面では3.8 Flashの導入価格$0.75/$3.75と2027-01-01からの倍額移行が期限付きで公示された ([INFO-066](../Information/2026-09-15/collected-raw.md#INFO-066) A-3)。HassabisがDeepMindを率いないと報じられ減速提案を支持した一方 ([INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) B-2・要追証)、上院duty of care法案の対象はGoogle等の最先端モデルである ([INFO-107](../Information/2026-09-15/collected-raw.md#INFO-107) A-2)。仮説確度は3件とも±0% (v4.91・Blue失敗6日連続による保留) である。

## 1. コア判断

### API形状とモデル編成の拡張

Interactions APIはgenerateContent系統と別の、エージェントインタラクション単位の新しいAPI形状である ([INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006) A-3・docs最終更新9/10)。モデル編成はエージェント階層を前提にした設計を見せる。Gemini 3.8 Flashは「最も知的なFlash」として長時間ソフトウェアエンジニアリング・自律エージェント・複雑なエンタープライズワークフロー向けと位置付けられ、Gemini 3.5 Flash-Liteは低レイテンシ高スループットのサブエージェント向けと明記された。オーケストレータに3.8 Flash、ワーカーに3.5 Flash-Liteというマルチエージェント階層の価格階層設計である。Gemini 3.1 Pro（マルチモーダル理解で世界最高）・Nano Banana 2/Pro・Omni Flash・3.5 Transcribe・Roboticsが同じdocs族で確認できる。ただしInteractions APIはv1betaの文書層であり、GA時期・課金単位・採用条件は未公告である。9/8 INFO-011のGemini 3.8示唆（fairwind画像URL）が公式docsで実体化した。

### 期限付き価格の明示

3.8 FlashのAPI価格は入力$0.75・出力$3.75/100万トークンの導入価格で、2027-01-01に$1.50/$7.50へ上昇する ([INFO-066](../Information/2026-09-15/collected-raw.md#INFO-066) A-3・9/2発効)。3.7 Flash（8/13発効）と同額に統一され、3.6 Flashは出力$9から$7.50へ値下げした。Pro系は200K超のロングコンテキストで$2/$12から$4/$18へ倍増する。割引を先遣し期限を明示する価格設計は異例で、導入期の囲い込みと期限後の値上げを同じ仕組みに載せた形である。コンシューマー側はAI Plus $4.99/Pro $19.99/Ultra $99.99+の階層が確認された。

### 資本とインフラの展開

フィンランドへの€130億（約$150億）投資（3新設+1拡張+エネルギー支援・原子力協定）は欧州最大の単一投資である ([INFO-081](../Information/2026-09-15/collected-raw.md#INFO-081) B-2)。2026年の世界AIインフラ投資は$1兆超（Goldman・前年比+42%）・米国企業が58%という文脈で、Googleは欧州側の最大級プレーヤーになる。一方で2027年目標データセンターの約60%がまだ着工していないという「発表と実施のギャップ」が同じ報告群にある。履行率は次期検証点である。

### DeepMind指揮系統の変数

HassabisがAmodei減速提案を「正しい進路」と支持した発言とともに、「もはやDeepMindを率いない」との報道が副次的に確認された ([INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) B-2・要追証)。8/15の組織再編（Koray統括・Hassabis専任）の延長線だが、統合シナリーの指揮系統が移ったなら[H-GOO-003](../config/hypotheses.json)（DeepMind統合シナジー）の前提条件が変わる。研究卓越性の指標面は分裂したままである。MMLU-Pro単体はGemini 3 Proが90%で首位（269モデル中）、AA Intelligence Indexの更新版では3.8 Flashの急上昇が話題化し ([INFO-071](../Information/2026-09-15/collected-raw.md#INFO-071) C-2)、FACTS Grounding（文書忠実度）はGemini系が系統的に強い ([INFO-073](../Information/2026-09-15/collected-raw.md#INFO-073) C-2)。ただしBenchLMマルチモーダル総合では3.5 Flashが86.9で6位・3.8 Flashは82.8に留まり ([INFO-029](../Information/2026-09-15/collected-raw.md#INFO-029) C-2)、Code Arena WebDevの人間投票上位5社にはGeminiが入っていない ([INFO-070](../Information/2026-09-15/collected-raw.md#INFO-070) C-2)。ベンチ毎の首位が全く異なる「総合首位の不存在」がGoogleでも例外でない。

### 規制環境と業界構造

上院交渉団のAI法案はAI開発者に注意義務を創設し、米政府に危険と判断されたモデルのリリース阻止権を与える構造で、対象は最先端モデル（Google/Anthropic/OpenAI等）である ([INFO-107](../Information/2026-09-15/collected-raw.md#INFO-107) A-2)。州法先行排除条項はトランプEO（州規制封じ・[INFO-046](../Information/2026-09-15/collected-raw.md#INFO-046) B-2）と同じ連邦集中化の方向である。GoogleはAnthropic・OpenAIと7月からAI安全の共通標準団体創設を協議していると報じられ ([INFO-079](../Information/2026-09-15/collected-raw.md#INFO-079) B-2)、Anthropicへの$20億出資も「代理戦争」構造の一部として報じられた ([INFO-078](../Information/2026-09-15/collected-raw.md#INFO-078) B-2)。規制と資本の両面で、Googleは3社協調の中心にいる。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Interactions API新設（v1beta/interactions・generateContentと別系統）+ モデル編成の階層化（3.8 Flash=長時間SWE/自律エージェント・3.5 Flash-Lite=サブエージェント） | エージェント階層を想定した供給面の拡張。GA・課金単位は未公告で文書層の域 | A-3 | [INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006) |
| 高 | 3.8 Flash導入価格$0.75/$3.75（2026-12-31まで）→2027-01-01に倍額。3.6/3.7/3.8 Flash同額統一・Pro系ロングコンテキスト2倍 | 期限付き割引の明示は異例。[H-GOO-002](../config/hypotheses.json)価格層と[SCN-003](../config/scenarios.json)材料の一次確定 | A-3 | [INFO-066](../Information/2026-09-15/collected-raw.md#INFO-066) |
| 高 | Hassabis「もはやDeepMindを率いない」報道・減速提案支持 | [H-GOO-003](../config/hypotheses.json)（DeepMind統合シナジー）の前提条件に関わる変数。要追証 | B-2 | [INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) |
| 高 | フィンランド€130億投資（3新設+1拡張+エネルギー支援・原子力協定）= 欧州最大単一投資 | インフラ統合の実体。[IND-029](../config/indicators.json)文脈。2027年対象DCの60%未着工という履行ギャップが対にある | B-2 | [INFO-081](../Information/2026-09-15/collected-raw.md#INFO-081) |
| 高 | 上院duty of care法案（リリース阻止権+連邦地裁チャレンジ・州法先行排除）の対象は最先端モデル（Google/Anthropic/OpenAI等） | 規制リスクの構造化。条文提出時の検証が残る | A-2 | [INFO-107](../Information/2026-09-15/collected-raw.md#INFO-107) |
| 中 | MMLU-Pro Gemini 3 Pro 90%首位（269モデル中）・AA更新版で3.8 Flash急上昇・FACTS GroundingはGemini系が系統的に強い | [H-GOO-003](../config/hypotheses.json)の研究卓越性材料。ただし単一ベンチ毎の分裂（総合首位不存在）は不変 | C-2 | [INFO-071](../Information/2026-09-15/collected-raw.md#INFO-071) [INFO-073](../Information/2026-09-15/collected-raw.md#INFO-073) |
| 中 | BenchLMマルチモーダル総合で3.5 Flash 86.9（6位）・3.8 Flash 82.8・Code Arena WebDev上位5社にGemini不在 | 部分指標首位と総合中位の併存。自家選択リスクの対抗データ | C-2 | [INFO-029](../Information/2026-09-15/collected-raw.md#INFO-029) [INFO-070](../Information/2026-09-15/collected-raw.md#INFO-070) |
| 中 | 3社（Google/Anthropic/OpenAI）が7月からAI安全共通標準団体創設を協議 | 業界主導の民間標準化。[H-GOV-002](../config/hypotheses.json)の代替統制構造 | B-2 | [INFO-079](../Information/2026-09-15/collected-raw.md#INFO-079) |
| 中 | GoogleのAnthropicへの$20億出資報道（Amazon/Microsoft/Googleが双方に出資する「代理戦争」構造） | 資本面での3社協調と競争の同居。[SCN-005](../config/scenarios.json)文脈 | B-2 | [INFO-078](../Information/2026-09-15/collected-raw.md#INFO-078) |
| 低 | トランプEOで州独自AI規制を封じ（連邦単一アプローチ・業界の規制強化要請を事実上拒否） | 規制権限の連邦集中。EO番号未確認・FB経由で一次確認待ち | B-2 | [INFO-046](../Information/2026-09-15/collected-raw.md#INFO-046) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Interactions APIのGA公告（課金単位・採用条件・v1betaからの移行） | エージェント対話単位の商モデルが確定し、形式層と実行層の重心判別が始まる | 90日 | [IND-027](../config/indicators.json) |
| Hassabisの組織離脱/残留の一次確認（Google公式・組織公告） | [H-GOO-003](../config/hypotheses.json)の前提（DeepMind統合シナジー）の再審査が発火する | 次回収集 | [H-GOO-003](../config/hypotheses.json) |
| Gemini固有の定量採用データ（A-2+品質のシェア・収益・利用率）の初公表 | [H-GOO-001](../config/hypotheses.json)のindeterminateが解消し、[H-GOO-003](../config/hypotheses.json)新条件も発火する | 2026-12-31 | [H-GOO-001](../config/hypotheses.json) |
| GCP公式self-deploy利用定量または同等のデプロイ実体の開放定量 | [H-GOO-002](../config/hypotheses.json)次回+1%審査の必須条件（v4.84事前登録）が充足される | 90日 | [H-GOO-002](../config/hypotheses.json) |
| 3.x系価格が2027-01-01に実際に倍増、または期間延長・撤回 | 価格権力の事前告知の検証。[SCN-003](../config/scenarios.json)材料の確定または失効 | 2027-01-01 | [IND-027](../config/indicators.json) |
| Extensions EOL（2026-11-26）までの移行完了率・機能ギャップ報告 | 強制移行の実害が判定され、[H-GOO-002](../config/hypotheses.json)囲い込み側の確定または失効が始まる | 2026-11-26 | [H-GOO-002](../config/hypotheses.json) |
| 上院法案の条文提出とGoogle対象条項の確定 | duty of careの実質（リスク緩和義務の範囲）が判定される | 条文提出時 | [IND-030](../config/indicators.json) |
| フィンランド投資の着工進捗と2027年対象DCの履行率 | 発表と実施のギャップの定量。[IND-029](../config/indicators.json)の観測点 | 2027-06-30 | [IND-029](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かし、エンタープライズAI市場でシェアを拡大する | 50% (indeterminate) | v4.88以来±0%（本日Blue評価なし・60R超の採用定量不在継続）。Interactions APIとモデル階層化（INFO-006・A-3）は供給面の拡張だが採用定量でない。フィンランド€13B（INFO-081）はインフラ文脈で採用診断力なし。C-only不定状態の駐車化注記継続 | Gemini固有の採用定量（シェア・収益・利用率のA-2+） | UBS試算（2社依存48%超）の四半期開示による検証 |
| [H-GOO-002](../config/hypotheses.json) | GoogleはGemini Tools & Agentsでオープン標準（LangChain等）とのDay 0サポートを維持し、囲い込みを回避する | 25% (low) | v4.84 +1%（24→25%）以降±0%。次回+1%には「GCP公式self-deploy利用定量または同等のデプロイ実体の開放定量」を要求（事前登録済み）。Interactions API（INFO-006）は形式層の拡張でこの条件を充足しない。期限付き価格の明示（INFO-066）は価格層の材料で形式層命題の反証から除外（層区別原則） | self-deploy利用定量・デプロイ実体の開放 | Extensions EOL移行の実害・価格倍増の執行 |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% (medium) | v4.86条件入替以降±0%（本日評価なし）。Hassabis「DeepMindを率いない」報道（INFO-093・B-2・要追証）は統合シナジー前提の変数として監視在庫。研究卓越性はMMLU-Pro首位・FACTS強さ（INFO-071/073・C-2）と総合中位（INFO-029/070・C-2）が併存。新条件（採用定量出現時または2026-12-31の再審査）は不変 | DeepMind指揮系統の一次確認・A-2+研究卓越性定量の連続出現 | Hassabis離脱の確定・研究者流失の累積 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・測定慣行 | 複数ベンチマーク×複数ラボで再現ならhigh | elevated/stable（v4.91・状態変更なし）。MMLU-Pro Gemini 3 Pro 90%首位・FACTS Gemini系強さ（INFO-071/073・C-2）は単一ベンチ毎の観測で閾値不充足。ベンチ毎の首位分裂（総合首位不存在）が測定慣行問題の継続実態 | 2026-09-15 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 期待-実態ギャップの定量蓄積 | high/rising（v4.91・状態変更なし）。Gemini固有の採用定量は不在継続。Interactions APIは文書層で到達率の直接材料でない | 2026-09-15 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度 | 攻撃表面の標準化進行 | high/rising（v4.91・状態変更なし）。Interactions API（INFO-006・A-3）と期限付き価格の公示（INFO-066・A-3）で供給・価格両層が一次確認された。2027-01-01倍額移行はKIQ-MONETIZATION監視継続 | 2026-09-15 |
| [IND-028](../config/indicators.json) | AGI到達度（予測分裂） | 分裂の深化・法制化圧力 | high/rising（v4.91・状態変更なし）。CEO公式レンジは2027（Amodei）〜2030（Altman）に収束（INFO-094・C-2）。Hassabisは減速側に明確化（INFO-093） | 2026-09-15 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | critical解消3基準 | critical/rising（v4.91・状態変更なし）。N=1実質35R。上院duty of care法案（INFO-107・A-2）は条文提出時の再審査発火を事前登録。GoogleはDoD 4社$200M契約の一角（INFO-052移行先） | 2026-09-15 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-09-15 | 全面書き直し（鮮度タイムアウト8日）。Interactions APIとモデル階層化（INFO-006・A-3）・期限付き価格の公示（INFO-066・A-3）・Hassabis報道（INFO-093・要追証）・フィンランド€13B（INFO-081）・上院法案の対象指定（INFO-107）・3社標準団体（INFO-079）を新規計上。§5をv4.91値に更新 | 鮮度タイムアウト + [INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006)/[066](../Information/2026-09-15/collected-raw.md#INFO-066)/[081](../Information/2026-09-15/collected-raw.md#INFO-081)/[093](../Information/2026-09-15/collected-raw.md#INFO-093) | H-GOO-001 50%（±0%）・H-GOO-002 25%（±0%）・H-GOO-003 48%（±0%） |
| 2026-09-07 | ターゲット編集。Flashキャンペーン価格の公式確認（INFO-059・A-3）・antigravity統合（INFO-013・A-2）を計上。§5をv4.88値に更新 | Arbiter v4.88（裁定2(d)/裁定9） | H-GOO-001 50%（±0%）・H-GOO-002 25%（±0%）・H-GOO-003 48%（±0%） |
| 2026-09-05 | §0〜§7書き直し（鮮度タイムアウト7日）。H-GOO-002 +1%とH-GOO-003条件入替を反映。Gemini 3.8 Flash DeepSWE勝利・GEAP公式docs等を新規計上 | 鮮度タイムアウト + Arbiter v4.86 | H-GOO-002 24→25%・H-GOO-003 48%（条件入替） |
| 2026-08-29 | 全面書き直し（8日freshness timeout）。GEAP吸収統合・Extensions EOL・A2A v1.0 AAIF移管・UBS 2社依存定量化を新規反映 | 鮮度タイムアウト + Arbiter v4.76〜v4.81 | H-GOO-002 23→24% |

## 7. ブラインドスポット

- Interactions APIはv1betaの文書層である。課金単位（インタラクション単位かトークン換算か）・GA時期・採用条件が公告されるまで、エージェント対話単位の商モデルについての判断は先走りうる。
- Hassabis「DeepMindを率いない」報道は単一報道で要追証である。8/15組織再編（専任）との差分（完全離脱か役割変更か）を区別できていない。
- Gemini固有定量データが60R超構造的に不在。indeterminate分類の駐車化対処（強制再評価条件の拡張）が記録されたまま実施されていない。
- MMLU-Pro首位・FACTS強さは部分指標で、総合系（BenchLMマルチモーダル・Code Arena WebDev）では中位に留まる。部分指標の選択性がGoogle自家選択か集計側か読めないのは不変である。
- フィンランド€13Bは報道ベースで、着工スケジュール・原子力協定の条項は未確認。2027年対象DCの60%未着工というギャップのGoogle側の該当分も不明である。
- UBSの2社依存試算（27%→48%）は単一試算で前提が開示されていない。Cloud収益のGemini寄与分の分離は四半期開示でも残る可能性がある。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006) | Interactions API新設・Gemini 3.8 Flash（長時間SWE/自律エージェント）・3.5 Flash-Lite（サブエージェント）(A-3・docs最終更新9/10) |
| [INFO-066](../Information/2026-09-15/collected-raw.md#INFO-066) | 3.8 Flash期限付き価格$0.75/$3.75→2027/1/1倍額・Pro系ロングコンテキスト2倍 (A-3・価格層の一次確定) |
| [INFO-081](../Information/2026-09-15/collected-raw.md#INFO-081) | フィンランド€130億投資・欧州最大単一投資・2027年対象DC60%未着工 (B-2・IND-029文脈) |
| [INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) | Hassabis「DeepMindを率いない」報道・減速提案支持 (B-2・要追証・H-GOO-003の変数) |
| [INFO-107](../Information/2026-09-15/collected-raw.md#INFO-107) | 上院duty of care法案全文（リリース阻止権・州法排除・最先端モデル対象）(A-2) |
| [INFO-071](../Information/2026-09-15/collected-raw.md#INFO-071)/[INFO-073](../Information/2026-09-15/collected-raw.md#INFO-073) | MMLU-Pro Gemini 3 Pro 90%首位・AA更新版3.8 Flash急上昇・FACTS Gemini系強さ (C-2) |
| [INFO-029](../Information/2026-09-15/collected-raw.md#INFO-029)/[INFO-070](../Information/2026-09-15/collected-raw.md#INFO-070) | BenchLM総合で3.5 Flash 86.9（6位）・Code Arena WebDev上位5社にGemini不在 (C-2・自家選択リスクの対抗データ) |
| [INFO-079](../Information/2026-09-15/collected-raw.md#INFO-079) | 3社安全共通標準団体創設協議 (B-2・民間標準化) |
| [INFO-078](../Information/2026-09-15/collected-raw.md#INFO-078) | GoogleのAnthropic $20億出資報道・「代理戦争」構造 (B-2) |
| [INFO-046](../Information/2026-09-15/collected-raw.md#INFO-046) | トランプEO州規制封じ (B-2・EO番号未確認) |
| [INFO-059](../Information/2026-09-07/collected-raw.md#INFO-059) | Flash系キャンペーン価格の公式公示・2027/1/1倍額移行 (A-3・前回更新の基盤) |
| [INFO-013](../Information/2026-09-07/collected-raw.md#INFO-013) | antigravity→Gemini Enterpriseガバナンス統合 (A-2・ソース形態注記) |
| [INFO-021](../Information/2026-09-01/collected-raw.md#INFO-021) | google/skills+google/agents-cli公開 (A-1・H-GOO-002 +1%の直接根拠・v4.84) |
| [INFO-047](../Information/2026-09-05/collected-raw.md#INFO-047) | Gemini 3.8 Flash DeepSWE 73.8%>Astra 73.3% (B-1・H-GOO-003条件入替の材料) |
| [INFO-008](../Information/2026-09-05/collected-raw.md#INFO-008) | GEAP公式ドキュメント (A-2・H-GOO-001 C-only材料) |
| [INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) | Gemini月間10億ユーザー・Google公式 (A-1) |
| [INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067) | UBS試算: 2社依存27%→48%超 (B-2) |
| [Arbiter v4.91](../state/arbiter-2026-09-15.md) | Blue失敗6日連続・rawパススルー・全仮説±0%（保留維持） |
| [Arbiter v4.86](../state/arbiter-2026-09-05.md) | H-GOO-003条件入替（プロセス負債解消）・指標全件維持 |
