# ByteDance

> 最終判断更新: 2026-08-29
> 全体確信度: 中
> 情報非対称性: 収益・コストの内部数値は外部検証不可能。豆包DAUは同一出所（QuestMobile系）内で「2億超」（晚点系報道）と「1.4億超」（QuestMobile 6月測定）の不整合が未解決で、ベースラインは無検験のまま（[INFO-071](../Information/2026-08-27/collected-raw.md#INFO-071) B-1）。1.78億は专业版ローンチ翌日の急騰値として再特徴づけされ、旧来の「6月2億超から8月系1.78億への約11%減」解釈は出典混同の可能性が指摘された（v4.77遡及監査登録）。国聯民生証券の赤字試算（単日1.32〜2.4億元・年間損失数百億元）は証券会社推計で一次確認待ち（[INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) B-2）。$30B超銀団の価格条件は期限後も確定報道なし（127検索0ヒット）で「非公開データ」注記へ移行済み。非上場・外部監査なし・中国情報源限定の構造は不変。
> 主参照: [H-BTD-001](../config/hypotheses.json) [H-BTD-002](../config/hypotheses.json) [H-BTD-003](../config/hypotheses.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はByteDanceを「億級DAUの消費者規模とその貨幣化不在が同時に観測され、虧損を知り尽くした上でスーパーアプリ集約による集中戦略に転換した企業」と読んでいる。8月25日、TRAE（コーディング基盤）とCoze（Agent構築）を豆包へ統合したワークスペースAIエージェント「豆包工作（Doubao Work）」が正式公開された。タスクの自律分解とツール展開で複雑業務を実行し、200以上の技能と連結器、遠隔PC制御やWindows仮想デスクトップを密集更新した上の投入である（[INFO-004](../Information/2026-08-27/collected-raw.md#INFO-004) B-2、[INFO-072](../Information/2026-08-27/collected-raw.md#INFO-072) A-2）。中国のオフィスAgent大戦では半年で10以上の有名AI製品（TRAE・Coze・飛書Aily・悟空・MuleRun・QoderWork・QClaw・dodo等）が消滅した（[INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) B-2）。

[H-BTD-002](../config/hypotheses.json)は32% low（±0%・v4.81）。仮説文が国聯民生証券の試算（単日総合コスト1.32〜2.4億元・年間損失数百億元）ベースに書き換えられた（一次確認待ち注記付き）。晚点LatePost系は日活2億超・単日収入100万元未満・算力コスト毎日数千万元と報じ、構造的赤字の輪郭がB-1品質の複数一次報道で裏付けられた（[INFO-071](../Information/2026-08-27/collected-raw.md#INFO-071) B-1）。経済的持続性への懸念が加重される場面では、[H-BTD-001](../config/hypotheses.json)（64% medium）に事前登録された対決評価条件（独立第2推計または一次決算で年間損失数百億元が確認された時点で引き下げ審査を発火）が処理を担う。

資本面では年間CAPEXが1,600億元から2,000億元超へ増額され（[INFO-074](../Information/2026-08-27/collected-raw.md#INFO-074) B-2）、華泰証券は2026〜2030年の中国AI建設累計融資需要を1.27〜3.5兆元と試算する（[INFO-075](../Information/2026-08-27/collected-raw.md#INFO-075) B-2）。9月1日に開始するS-1ゲート開示窓が、銀団価格条件を含むAI債務観測の次の実質的機会となる（[IND-029](../config/indicators.json)）。

## 1. コア判断

全体確信度は中。「消費者AIの規模優位を企業インフラの収益化に転換する組織的基盤を構築中」という読みを維持するが、その重心が「基盤の構築」から「虧損認識に基づく防御的集中」へ動いた。ArbiterはDoubao統合を根拠とする確度引き上げ（+1%）を2ラウンド連続で却下し（v4.77）、豆包工作公開を「統合の実行」の両義注記付きCとして計上した（v4.81）。統合の実行は確認されたが、商業的定着はいまだ未測定である。

### 豆包工作公開とスーパーアプリ集約

Bloomberg報道が「統合計画」から「ローンチ実施」へ更新された。ByteDanceはTraeとCozeをDoubaoへ統合した上でワークスペースAIエージェント「豆包工作」を投入し、Tencent WorkBuddyに対抗する（[INFO-004](../Information/2026-08-27/collected-raw.md#INFO-004) B-2、Tech in Asia複数情報源確認付き）。36kr独占報道によればCozeチームは豆包に整体編入され、豆包工作は200以上の技能と連結器を上架、リモートパソコン制御・Windows仮想デスクトップ・クラウドPC・サイドワークベンチを密集更新した（[INFO-072](../Information/2026-08-27/collected-raw.md#INFO-072) A-2）。淘汰の駆動要因は外部にもある。AnthropicのARRが2025年末$9Bから2026年7月末に$65B超へ伸び（申告値・未監査）、Agentで本物の収益が上がる証明として中国各社の統合・淘汰ラッシュを加速した（[INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) B-2）。Coze敗因の本質は「Workflowは過程を交付するが結果を交付しない」と整理され、DeepSeek系の「一切皆插件（すべてはプラグイン）」理念が業界に波及している。

### 構造的赤字の定量と仮説文の更新

晚点LatePost系報道（B-1）が豆包の規模と赤字の実態を定量化した。日活2億超・月活約3.8億・単日収入100万元未満・計算資本コストは毎日数千万元で、日次で数千万元規模の損失となる。有料転換は不調で（「伝統的ネット効果の神話が算力コストで崩壊」との指摘）、収益模索としてホテル推薦での佣金徴収（抽傭）も始まった（推薦信頼性のジレンマ付き）。QuestMobile 2026年6月値は月活3.82億・日活1.4億超で国内AI原生アプリ最大、专业版ローンチ翌日のDAUは1.78億に急騰した（[INFO-071](../Information/2026-08-27/collected-raw.md#INFO-071) B-1）。国聯民生証券は字節の単日総合コストを1.32〜2.4億元、年間損失を数百億元と試算し、豆包专业版は68元/月（最高年5,088元）でC端課金に抵抗があるとする（[INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) B-2、一次確認待ち）。v4.81は[H-BTD-002](../config/hypotheses.json)の仮説文をこの試算ベースに更新し（旧「日次赤字数千万元」表記の置換）、[H-BTD-001](../config/hypotheses.json)側には対決評価条件を事前登録した。独立第2推計または一次決算で年間損失数百億元が確認されれば、規模Cと経済Iの対決評価（引き下げ審査）が発火する。

### DAUベースライン汚染と遡及監査

1.78億の位置づけが「专业版ローンチ翌日の急騰値」に変わったことで、08-19裁定の「6月2億超から8月系1.78億・約11%減」という方向根拠は不安定化した。6月値が1.4億であれば系列内では+27%増に反転する。同一出所内30%乖離（2億超 vs 1.4億超）の解消が[H-BTD-001](../config/hypotheses.json)引き上げの先行条件であり、過去裁定の遡及監査とQuestMobile 7〜8月値の収集が次ラウンド課題として登録されている（v4.77）。追加加重（-1〜2%）は独立ソース×同一定義の時系列出現時に限定する枠組みを維持する（v4.74/76で却下理由を明確化済み）。

### 資本戦略: CAPEX増額・債務・S-1ゲート

年間CAPEXが1,600億元から2,000億元超へ増額された（メモリ価格上昇要因。Microsoftの1,900億ドル中250億ドルが部品価格対応との同型）。具身智能（ロボット）投資として「未来不远机器人」に入股（半年3轮・累計10億元）、Seed世界モデルチーム（周畅）が自動運転探索・VLA 2.0・AIVAを進める（[INFO-074](../Information/2026-08-27/collected-raw.md#INFO-074) B-2）。華泰証券は中国AI建設の2026〜2030年累計融資需要を1.27〜3.5兆元（主に銀行貸出と社債）と試算し（[INFO-075](../Information/2026-08-27/collected-raw.md#INFO-075) B-2）、[IND-029](../config/indicators.json)の債務駆動インフラ文脈を補強する。$30B超銀団の価格条件はコミット期限（8/19）後も確定報道がなく、searched-absence 3ラウンドを消費した後「非公開データ（pricingは報道されないまま確定するのが通例の場合がある）」注記へ移行した（v4.78）。期限後沈黙の継続は「再価格・組み入れ難航」読みの重みを漸増させる。9月1日開始のS-1ゲート窓が銀団価格条件・AI DC債務開示の一括再評価機である（[IND-029](../config/indicators.json)）。

### 規制とH-BTD-003

[H-BTD-003](../config/hypotheses.json)は40% medium（±0%・v4.74以来）。中国AIコンパニオン規制（7/15発効）の実害報道と豆包・千問の擬人機能停止速報は規制インフラの蓄積だが（[INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) B-2、[INFO-136](../Information/2026-08-17/collected-raw.md#INFO-136) C-3）、核心命題（著作権によるグローバル展開の制限）への新規A-2以上の証拠は不在のままである。Seedance 2.0（業界初の4モダリティ同時入力・豆包無料全面搭載）と後継2.5は製品力の維持を示すが、自家測定・API仕様ベースで独立検証は完了していない。BytePlus ModelArk APIでの動画生成提供（海外展開）も進む（[INFO-073](../Information/2026-08-27/collected-raw.md#INFO-073) B-2）。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 豆包工作8/25正式公開: TRAE・Coze・飛書Ailyの豆包統合・200+技能/連結器・遠隔PC制御・WorkBuddy対抗 | [H-BTD-001](../config/hypotheses.json) 両義注記付きC（スーパーアプリ集約の実行。商業的定着は未測定）。[IND-026](../config/indicators.json)/[IND-027](../config/indicators.json) | B-2/A-2 | [INFO-004](../Information/2026-08-27/collected-raw.md#INFO-004) [INFO-072](../Information/2026-08-27/collected-raw.md#INFO-072) [INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) |
| 高 | 国聯民生試算: 豆包単日総合コスト1.32〜2.4億元・年間損失数百億元・专业版68元/月（最高年5,088元）でC端課金に抵抗 | [H-BTD-002](../config/hypotheses.json) 仮説文更新の根拠（一次確認待ち注記付き）。[H-BTD-001](../config/hypotheses.json) 対決評価条件の対象 | B-2 | [INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) |
| 高 | 晚点系: 日活2億超・単日収入<100万元・算力コスト毎日数千万元・有料転換不調。QuestMobile 6月MAU3.82億・DAU1.4億超・专业版翌日DAU1.78億急騰 | 構造的赤字のB-1品質裏付け。DAUベースライン不整合（同一出所内30%乖離）は未解決 | B-1 | [INFO-071](../Information/2026-08-27/collected-raw.md#INFO-071) |
| 高 | 年間CAPEX 1,600億→2,000億元超増額（メモリ価格上昇）・未来不远机器人入股（半年3轮累計10億元）・Seed世界モデル（VLA 2.0/AIVA） | [IND-029](../config/indicators.json) 債務駆動インフラの拡大。$30B銀団と併せ資本強度の上昇 | B-2 | [INFO-074](../Information/2026-08-27/collected-raw.md#INFO-074) |
| 高 | 華泰証券: 中国AI建設の2026〜2030累計融資需要1.27〜3.5兆元（主に銀行貸出・社債） | [IND-029](../config/indicators.json) 債務駆動インフラの産業水準文脈 | B-2 | [INFO-075](../Information/2026-08-27/collected-raw.md#INFO-075) |
| 高 | Anthropic ARR $9B（25年末）→$65B超（26年7月末・申告値・未監査）がAgent収益の証明としてオフィスAgent大戦を駆動 | 淘汰・統合ラッシュの外部駆動要因。「約1.5〜8倍更新」枠で解釈（分母分子に選択幅） | B-2 | [INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) |
| 中 | 半年で10以上の有名AI製品消滅: TRAE/Coze/Aily/悟空/MuleRun/QoderWork/QClaw/dodo等。WorkBuddy DAU「1,300万」は実際は月活2,000万超のデマ | 中国AI製品統合・淘汰フェーズの確定。利用数字の流動性への注意 | B-2 | [INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) |
| 中 | CEO梁汝波年次全員会「大LLM格差拡大」自認・自研堅持（継続計上） | [H-BTD-002](../config/hypotheses.json) 技術競争力軸の反証として継続 | B-2 | [INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) |
| 中 | Seedance 2.0/2.5: 4モダリティ同時入力・豆包無料搭載・ModelArk APIで海外展開 | [H-BTD-001](../config/hypotheses.json) 製品力の維持（自家測定系・独立検証なし） | B-2 | [INFO-073](../Information/2026-08-27/collected-raw.md#INFO-073) |
| 中 | 中国AIコンパニオン規制7/15発効の実害報道・擬人機能停止速報（継続計上） | [H-BTD-003](../config/hypotheses.json) 規制インフラ蓄積。DAU減少規制実害仮説の判別は未了 | B-2/C-3 | [INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) [INFO-136](../Information/2026-08-17/collected-raw.md#INFO-136) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 国聯民生試算の一次確認（原報告書または字節側一次開示）が出る | 試算の信頼性が確定し、[H-BTD-002](../config/hypotheses.json) 仮説文の「一次確認待ち」注記が外れ、[H-BTD-001](../config/hypotheses.json) 対決評価の発火判定が始まる | 30日 | [H-BTD-002](../config/hypotheses.json) |
| QuestMobile等の独立ソース×同一定義のDAU時系列（7〜8月値）が出現する | 事前登録済み追加加重（-1〜2%）が行使され、同一出所内30%乖離の解消が始まる | 次回 | [H-BTD-002](../config/hypotheses.json) |
| 銀団価格条件（スプレッド・コベナント・割当）の確定報道、またはS-1ゲート（9/1）でのAI DC債務開示 | [IND-029](../config/indicators.json) とSCN-BS-003の材料区分が再検討され、AI信用リスクの市場価格が観測される | 9/1以降 | [IND-029](../config/indicators.json) |
| 豆包工作の採用定量（利用企業数・定着率・ARPA）が出る | 「統合の実行」と「商業的定着」の判別が始まり、両義注記付きCの注記が判定される | 90日 | [IND-026](../config/indicators.json) |
| 抽傭18%（8/10発効）のGMV・リピート4〜6週データが観測される | 貨幣化転換の実効性が判定され、赤字構造の評価が変わる | 60日 | [H-BTD-002](../config/hypotheses.json) |
| 中国の海外AIモデルアクセス制限が実施されオープンソース配布が停止される | [H-BTD-001](../config/hypotheses.json) のグローバル展開前提が崩壊し、確度を大幅に下方修正する | 90日 | [H-BTD-001](../config/hypotheses.json) |
| 著作権関連の新規A-2以上の証拠が出現する | [H-BTD-003](../config/hypotheses.json) の核心命題が初めて直接検証される | 90日 | [H-BTD-003](../config/hypotheses.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-BTD-001](../config/hypotheses.json) | ByteDanceはTikTok/Douyinのデータ活用で中国市場で圧倒的優位を維持し、グローバル展開を図る | 64% medium | ±0%（v4.81）。Blue ±0%支持・Red条件2件を採用した。(1)「桁更新」表記は「約1.5〜8倍更新」（Anthropic ARR $9B→$65B申告・未監査）へ修正。(2)経済I側再評価条件を事前登録: 独立第2推計または一次決算で年間損失数百億元（国聯民生試算）が確認された場合、対決評価（引き下げ審査）を発火。豆包工作公開（EVD-20260827-0004・0072・0081内）は両義注記付きC計上。v4.77はDoubao統合+1%を却下（統合≠商業的定着・ミラーイメージング・[H-BTD-002](../config/hypotheses.json)測定基盤安定が先行条件）。海外AIモデルアクセス制限協議が障壁で、DAU測定分裂で絶対値の確定は不可 | [INFO-004](../Information/2026-08-27/collected-raw.md#INFO-004) [INFO-072](../Information/2026-08-27/collected-raw.md#INFO-072) [INFO-071](../Information/2026-08-27/collected-raw.md#INFO-071) [INFO-073](../Information/2026-08-27/collected-raw.md#INFO-073) | 国聯民生試算の一次確認（対決評価発火）・[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084)・DAU測定の分裂 |
| [H-BTD-002](../config/hypotheses.json) | ByteDanceは消費者基盤（豆包DAU: QuestMobile同一出所系列内で1.4億超/2億超の不整合未解決・無検験ベースライン）と企業インフラ（火山方舟・Coze・Seed Audio）の相乗的並行拡大を展開している。消費者DAUと企業Token経済が同時に成長する構造であり、消費者から企業への『移行』ではない。但し単日総合コスト1.32〜2.4億元・年間損失数百億元試算（国聯民生証券・EVD-20260827-0081内・証券会社試算で一次決算書非開示・一次確認待ち）が消費者ビジネスの経済的持続性に懸念を呈している。反証条件: 消費者DAUが減少に転じる、または企業Token経済の成長が停止する場合、本フレームの再評価が必要 | 32% low | ±0%（v4.81）。仮説文修正を承認: 「日次赤字（数千万元）」を国聯民生試算（単日1.32〜2.4億元・年間損失数百億元）ベースの表記へ更新（一次確認待ち注記付き）。DAUベースライン不整合（同一出所内1.4億超 vs 2億超）は未解決継続。経済側Iの重量化は[H-BTD-001](../config/hypotheses.json)対決評価条件で処理。v4.77は「約11%減」の方向根拠が6月値1.4億なら+27%増に反転し得るベースライン汚染を指摘し遡及監査を登録。追加加重（-1〜2%）は独立ソース×同一定義の時系列出現時に限定（v4.74/76で却下理由を明確化） | [INFO-092](../Information/2026-08-07/collected-raw.md#INFO-092) [INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) [INFO-072](../Information/2026-08-27/collected-raw.md#INFO-072) | [INFO-071](../Information/2026-08-27/collected-raw.md#INFO-071) [INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) [INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) |
| [H-BTD-003](../config/hypotheses.json) | ByteDanceは著作権問題で法的制約を受け、グローバル展開が制限される | 40% medium | ±0%（v4.74以来）。コンパニオン規制7/15発効の実害報道・擬人機能停止速報・FCC中国製ロボット輸入禁止で規制インフラは蓄積するが、核心命題（著作権）への新規A-2以上の証拠は不在。v4.74は「和解路線」読みに基づく-1%提案を判別データ不在で却下（両立する複数の読みが可能で診断的価値不十分） | [INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) [INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) [INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) | (著作権領域の新規A-2+証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-026](../config/indicators.json) | エージェント本番環境到達率（中国オフィスAgent大戦の帰結） | P(B)固有B-2+品質の採用定量出現で再評価 | high/rising（v4.81維持・本日観測ゼロ）。豆包工作公開・龍蝦熱（OpenClaw設置代行500元・Mac mini品薄）が中国Agent普及の起点（[INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081)）。JetBrains調査（週次90%/日次68%・A-1）はsurvey-usage≠production-standardization注記付きで記録。期待-実態ギャップ構造不変 | 2026-08-29 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度（囲い込みと開放の並走） | 囲い込み側の制度化逆流で再評価 | high/rising（v4.81維持）。AgentCore/Doubao配給（囲い込み側）とA2A/AAIF・Okta XAA（開放側）の並走をv4.77が記録。豆包体系統合・200+技能/連結器は配給の集約例。価格権力（抽傭18%等）のKIQ-MONETIZATION監視継続 | 2026-08-29 |
| [IND-029](../config/indicators.json) | AIインフラ制約（債務駆動インフラの拡大） | 信用収縮の観測で発火審査 | high/rising（v4.81維持）。S-1ゲート窓開始（9/1）まで3日: 銀団価格条件・AI DC債務開示の一括再評価窓。searched-absence R3/3消費済みでS-1開示が次の実質観測機。CAPEX 2,000億元超（[INFO-074](../Information/2026-08-27/collected-raw.md#INFO-074)）・華泰1.27〜3.5兆元（[INFO-075](../Information/2026-08-27/collected-raw.md#INFO-075)）・$30B超銀団（価格条件は非公開データ注記） | 2026-08-29 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性（規制・政治リスク） | （critical到達済み） | critical/rising（v4.81維持・N=1実質28R）。中国AIコンパニオン規制7/15発効・実害報道（[INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043)）・EU AI Act執行・海外AIモデルアクセス制限協議（[INFO-084](../Information/2026-07-10/collected-raw.md#INFO-084) A-2）。critical解消条件3基準いずれも未到達 | 2026-08-29 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-08-29 | 全面書き直し（10日freshness timeout + 構造的変化: 主力製品の発表＝豆包工作8/25正式公開 + H-BTD-002仮説文のv4.81書き換え反映）。豆包工作公開・TRAE/Coze/飛書Aily統合と半年10+製品淘汰・国聯民生試算（単日1.32〜2.4億元・年間損失数百億元）・晚点B-1赤字定量・1.78億の再特徴づけ（专业版翌日急騰）・CAPEX 2,000億元超・華泰1.27〜3.5兆元・銀団価格条件の非公開データ注記移行を新規反映。廃止済み指標参照（IND-010/011）を現行指標（IND-026/027/029/030）へ更新。仮説確度は全件±0% | Arbiter v4.81・[INFO-004](../Information/2026-08-27/collected-raw.md#INFO-004) [INFO-071](../Information/2026-08-27/collected-raw.md#INFO-071) [INFO-072](../Information/2026-08-27/collected-raw.md#INFO-072) [INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) | H-BTD-001 64%（±0%）・H-BTD-002 32%（±0%）・H-BTD-003 40%（±0%） |
| 2026-08-19 | 全面書き直し（7日freshness timeoutと判別条件充足）。H-BTD-002 -2%を反映（34→32%: 08-17はDAU表記分裂の反証蓄積、本ラウンドは[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118)で同一出所系列内時系列が出現し判別条件が充足・非対称証拠基準の是正・反証3件で全仮説最多）。貨幣化の乖離定量（有料数十万・日次コスト数千万元 vs 日収百万元未満）・AI取引佣金最高18%の8/10発効・$30B超銀団申込（負債側注記付き）・Seedance 2.0/2.5・中国コンパニオン規制の実害報道を新規反映。全4指標last_checked更新 | Arbiter v4.69/v4.71・[INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) [INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) [INFO-121](../Information/2026-08-19/collected-raw.md#INFO-121) | H-BTD-001 64%（±0%）・H-BTD-002 34→32%・H-BTD-003 40%（±0%） |
| 2026-08-12 | ターゲット編集。H-BTD-002 -1%（35→34%・CEO梁汝波「大LLM格差拡大」自認=技術競争力軸初のI証拠・AND条件「相乗的」否定・ミラー・イメージング是正・Red反証強度「中-強」採用・v4.64強制再評価メカニズム）を反映。CEO年次全員会([INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) B-2)・10兆パラメータモデル訓練/$230億投資([INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) B-2)・OpenRouter三極体制収束を新規反映。全4指標last_checked更新。Arbiter v4.64 COMPLETE | Arbiter v4.64・[INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) [INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) | H-BTD-001 64%（±0%）・H-BTD-002 35→34%・H-BTD-003 40%（±0%） |
| 2026-08-09 | ターゲット編集。H-BTD-002 -1%（36→35%・Red反証強度「中-強」採用・張一鳴宣言検証不可能性・可霊AI二重性・I=0人工性・財務/TikTokリスク評価不在）を反映。全4指標last_checked更新。Arbiter v4.61 COMPLETE | Arbiter v4.61 | H-BTD-001 64%（±0%）・H-BTD-002 36→35%・H-BTD-003 40%（±0%） |
| 2026-08-07 | 鮮度タイムアウト更新（7日経過）。Tesla中国での豆包AI音声配信・Seedance 2.5 SeedRealtime統合モデル・8月1日組織再編発効・MAU/CAPEXソース間乖離の明示を追加。Arbiter v4.59のH-BTD-002 3条件（I=0人工性・中国語ソース品質・TikTok損失矛盾）を§4に反映。仮説確度は全件±0%据え置き | [INFO-092](../Information/2026-08-07/collected-raw.md#INFO-092) [INFO-091](../Information/2026-08-07/collected-raw.md#INFO-091) [INFO-094](../Information/2026-08-07/collected-raw.md#INFO-094) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-31 | 構造的変化反映。7/30組織再編（豆包・飛書・火山エンジン統合）を新規反映。中国3社エージェントマーケットプレイス削除・ByteDance維持・FCC中国製ロボット輸入禁止を追加 | [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-30 | 豆包MAU 5.28億・過去最高・$700億AI投資計画・DAU差異技術的説明初確認 | [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) | H-BTD-001 64%(±0%)・H-BTD-002 36%(±0%)・H-BTD-003 40%(±0%) |
| 2026-07-28 | Seed 2.0 Code 256K・豆包MAU 3.82億/+172% YoYのA-1品質確認 | [INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) | H-BTD-002 37→36% |
| 2026-07-23 | H-BTD-002ステートメント修正: 「移行過程」→「相乗的並行拡大」。$186B売上・豆包DAU 2億/日次赤字・Seed Audio 1.0を新規反映 | [INFO-060](../Information/2026-07-23/collected-raw.md#INFO-060) | H-BTD-002 38→37% |

## 7. ブラインドスポット

- DAU系列が汚染されている。同一出所内で1.4億超と2億超が併存し、どちらがベースラインか外部から判別できない。1.78億の位置づけも「专业版ローンチ翌日の急騰」に再特徴づけされ、過去の「約11%減」裁定は遡及監査対象である。中国情報源の限定により独立裏付けが得られない。
- 国聯民生試算は単一証券会社の推計で、算定根拠（ユーザー数・ユニットコスト・償却前提）が未開示。単日1.32〜2.4億元の幅が広く、一次報告の確認まで仮説文の注記は外せない。
- 豆包工作の採用実態（利用企業数・定着率・ARPA）がすべて取れていない。公開ローンチと本番採用は別物である。WorkBuddy DAU「1,300万」が実際は月活2,000万超のデマだった例（[INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081)）が示すとおり、中国AI利用数字の流動性は高い。
- 銀団価格条件が非公開のまま確定しうる（v4.78注記）。$30B超という規模の大きさ自体は当座の金融条件の観測であって投資持続性の証明ではなく、規模をユーフォリア材料と混同する誤りはv4.71が是正済みである。
- CAPEX増額（1,600億→2,000億元超）の内訳分解（メモリ価格要因の大きさ）と、既存の投資計画系列（$230億・$280億・$700億）との対応関係が不明のまま。
- ミラーイメージングのリスクが残る。「赤字=持続不能」という財務基準を、広告・抖音シナジーでクロス収益化する中国の消費者アプリにそのまま当てはめるとモデルの優位を見落とす可能性があり、逆に過大に考慮すると赤字の実相を過小評価する。v4.77は統合の読みに規制誘導・商業的失敗・効率化の代替説明が対等に立つと指摘した。判別手段がない。
- Seedance 2.0/2.5やVLA 2.0等の能力主張は自家測定・API仕様ベースで独立ベンチマークの検証が未完了。MPAとのIP合意の内容（適用範囲・執行メカニズム）も一次文書待ちで、[H-BTD-003](../config/hypotheses.json)の著作権軸への影響評価には一次文書が要る。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-004](../Information/2026-08-27/collected-raw.md#INFO-004) | Doubao Workローンチ: Bloomberg報道が統合計画から実施へ更新・Trae/Coze統合・WorkBuddy対抗(B-2) |
| [INFO-071](../Information/2026-08-27/collected-raw.md#INFO-071) | 【KIQ-BTD-DAU核心】晚点: 日活2億超・単日収入<100万元・算力コスト毎日数千万元。QuestMobile 6月MAU3.82億・DAU1.4億超・专业版翌日DAU1.78億急騰・有料転換不調(B-1) |
| [INFO-072](../Information/2026-08-27/collected-raw.md#INFO-072) | TRAE+Coze→豆包統合: 36kr独占+Bloomberg整合・豆包工作200+技能/連結器・「大廠Agent混戦が10+のAI名品を殺す」(A-2) |
| [INFO-073](../Information/2026-08-27/collected-raw.md#INFO-073) | Seedance 2.0: 4モダリティ同時入力（業界初）・豆包無料全面搭載・2.5登場・ModelArk API海外展開(B-2) |
| [INFO-074](../Information/2026-08-27/collected-raw.md#INFO-074) | CAPEX 1,600億→2,000億元超増額（メモリ価格上昇）・未来不远机器人入股（半年3轮累計10億元）・Seed世界モデルVLA 2.0/AIVA(B-2) |
| [INFO-075](../Information/2026-08-27/collected-raw.md#INFO-075) | 華泰証券: 中国AI建設2026-2030累計融資需要1.27〜3.5兆元・主に銀行貸出と社債(B-2) |
| [INFO-081](../Information/2026-08-27/collected-raw.md#INFO-081) | 【36kr詳細】中国オフィスAgent大戦: 豆包工作8/25正式公開・国聯民生試算（単日1.32〜2.4億元・年損失数百億元）・半年10+製品消滅・专业版68元/月(B-2) |
| [INFO-118](../Information/2026-08-19/collected-raw.md#INFO-118) | 豆包DAU 1.78億の出典特定（旧計上）・貨幣化乖離の定量。1.78億の再特徴づけにより遡及監査対象(C-2) |
| [INFO-119](../Information/2026-08-19/collected-raw.md#INFO-119) | $20B想定銀団に$30B超申込・Citi/JPMorgan主幹事・AI投資原資・負債側注記の対象(Bloomberg・B-1) |
| [INFO-121](../Information/2026-08-19/collected-raw.md#INFO-121) | AI取引佣金最高18%が8/10発効・GEO産業の即時発生・携程経由の迂回(C-2) |
| [INFO-113](../Information/2026-08-19/collected-raw.md#INFO-113) | 米国の「Pax Silica」協定: 同盟国に側の選択を要求(Reuters・B-1) |
| [INFO-126](../Information/2026-08-17/collected-raw.md#INFO-126) | 豆包MAU 3.45億・DAU表記の分裂（2億超/1.4億）・日均180兆トークン(B-2) |
| [INFO-043](../Information/2026-08-17/collected-raw.md#INFO-043) | 中国AIコンパニオン規制7/15発効・感情操作禁止・「サービス消失」の実害報道(B-2) |
| [INFO-136](../Information/2026-08-17/collected-raw.md#INFO-136) | 中国新規制で豆包・千問が擬人エージェント機能を停止との速報・規制主体・条文は要確認(C-3) |
| [INFO-058](../Information/2026-08-12/collected-raw.md#INFO-058) | CEO梁汝波年次全員会: 大LLM格差拡大自認・自研堅持・短期的劣位受容(B-2) |
| [INFO-012](../Information/2026-08-12/collected-raw.md#INFO-012) | 10兆パラメータモデル訓練中・$230億AIインフラ投資・Cozeオープンソース版(B-2) |
| [INFO-092](../Information/2026-08-07/collected-raw.md#INFO-092) | 8月1日組織再編発効・Tesla中国豆包AI音声配信・QuestMobile値 |
| [INFO-068](../Information/2026-07-31/collected-raw.md#INFO-068) | 7/30組織再編: 豆包・飛書・火山エンジン統合・新設「創造力サービスプラットフォーム部」(A-2) |
| [INFO-042](../Information/2026-07-31/collected-raw.md#INFO-042) | FCC: 中国製ヒューマノイド・四足ロボット新規輸入禁止(B-2) |
| [INFO-068](../Information/2026-07-30/collected-raw.md#INFO-068) | 豆包MAU 5.28億・2026年6月過去最高・DAUピーク1.45億 vs 持続的~8000万(A-2) |
| [INFO-087](../Information/2026-07-28/collected-raw.md#INFO-087) | Seed 2.0 Code 256Kコンテキスト・Seedance 2.0(A-1) |
| [Arbiter v4.77](../state/arbiter-2026-08-25.md) | Doubao統合+1%却下（統合≠商業的定着・ミラーイメージング）・「約11%減」ベースライン汚染指摘・遡及監査登録 |
| [Arbiter v4.81](../state/arbiter-2026-08-29.md) | H-BTD-001 ±0%（桁更新→約1.5〜8倍更新表記修正・対決評価条件事前登録）・H-BTD-002 ±0%（仮説文の国聯民生試算ベース更新） |
