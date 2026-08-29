# Google / DeepMind

> 最終判断更新: 2026-08-29
> 全体確信度: 測定不能（H-GOO-001 indeterminate維持）
> 情報非対称性: Geminiアプリ月間10億ユーザー突破をGoogle自身が公表した（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1）が、Gemini固有のエンタープライズ定量採用データ（シェア・収益・利用率の直接定量A-2+）は57R超にわたり構造的に不在（v4.70計上・以降のDEGRADED帰因ラウンドは分母不算入）。MAUは消費者指標でありエンタープライズ採用シェアではない。UBS試算はGoogle Cloud収益の27%（2026）→48%超（2027・$124B超）がOpenAI+Anthropicの2社依存と定量化し（[INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067) B-2）、Cloud収益成長とGemini固有需要の分離不能性が拡大した。Vertex AIは「Gemini Enterprise Agent Platform（GEAP）」へ吸収統合されブランドを後退（[INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012) A-2）、Vertex AI Extensionsは2026-11-26以降シャットダウン（[INFO-010](../Information/2026-08-23/collected-raw.md#INFO-010) A-3）。3.7 Flash価格は$0.75/$3.75紹介→2027年1月1日倍増（[INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) A-1）と半額$0.38/$1.88報道（[INFO-045](../Information/2026-08-23/collected-raw.md#INFO-045) B-2）が併存し定義が未統一。ベンチマークの多くが自家測定かC品質。
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はGoogleを「消費者AIアプリとして月間10億ユーザーを公表しながら、エンタープライズAI採用の固有定量が構造的に見えない企業」と読む枠組みを維持する。08-22〜08-29の観測はこの枠組みの両側を同時に強めた。プラットフォーム側ではVertex AIブランドの後退とGEAPへの吸収統合が完了し（Agent Builder/ADK/Agent Engineの統合・[INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012) A-2）、Grok 4.6の公式提供でマルチモデル配給が拡張された（[INFO-002](../Information/2026-08-24/collected-raw.md#INFO-002) A-3）。標準側ではA2A v1.0がAAIF（Linux Foundation）へ移管され150以上の組織が採用した（[INFO-019](../Information/2026-08-25/collected-raw.md#INFO-019) B-2）。

他方、成長の質を疑う材料が初めて定量化された。UBS試算ではGoogle Cloud収益の27%（2026年）から48%超（2027年・$124B超）がOpenAIとAnthropicの2社依存となる（[INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067) B-2）。Cloud収益成長の駆動がGemini採用ではなくAIラボのインフラ需要である可能性が数字で示され、availability（利用可能であること）とadoption（採用）の分離構造が深まった。[H-GOO-001](../config/hypotheses.json)は50% indeterminate（±0%）。

[H-GOO-002](../config/hypotheses.json)は24% low（+1%・v4.76で23→24%）。self-deployオープンモデル経路等の開放C証拠の純増を認定した一方、v4.77は更なる+1%を「解釈で確度が積み上がる構造」の制度化リスクで却下した。[H-GOO-003](../config/hypotheses.json)は48% medium（±0%）。

## 1. コア判断

全体確信度は測定不能に置く。Gemini固有の定量採用データが構造的に不在である以上、10億MAUという消費者規模の追加だけでは確度ラベルを動かさない。この座標軸は今回の更新でも変わっていない。変わったのは、Cloud成長の駆動力がGemini以外の要因（2社のAIラボ需要）へ帰属する可能性が定量化された点である。

### GEAPへの吸収統合完了とマルチモデル配給

Vertex AIは「Gemini Enterprise Agent Platform」へ吸収統合された。Agent Builder/ADK/Agent Engineを統合し、Agent Engineは改称される（[INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012) A-2・公式リリースノート系）。Vertex AI Extensionsは2026-11-26以降シャットダウンが確定し、ブランド再編に強制移行スケジュールが付随する（[INFO-010](../Information/2026-08-23/collected-raw.md#INFO-010) A-3）。AntigravityベースのGemini Agents API（リモート実行環境）も新設された（[INFO-008](../Information/2026-08-25/collected-raw.md#INFO-008)）。Grok 4.6がGEAPのModel Gardenで公式提供され（入力$2/M・キャッシュ入力$0.50/M・出力$6/M・500kコンテキスト・ロングランニングエージェント向け）、BedrockでのGPT-5.6提供と対称的なマルチクラウド標準化が進む（[INFO-002](../Information/2026-08-24/collected-raw.md#INFO-002) A-3）。gpt-oss 120B（Apache 2.0）のMaaS提供（[INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) A-3）と合わせて[H-GOO-002](../config/hypotheses.json)の開放C方向である。他方でVertexブランドの後退とスタックの単一化は囲い込みI方向の観察でもあり、開放と統合のどちらに重心があるかは旧Vertex顧客の移行率とGEAP固有の採用定量が出るまで判別できない。

### A2A v1.0のAAIF移管と標準の中立化

Google主導のA2Aプロトコルがv1.0に到達し、Agentic AI Foundation（2025年12月Linux Foundation設立）へ移管された。主要クラウドと150以上の組織が採用し、MCPと同じ中立ガバナンスの傘下に入った（[INFO-014](../Information/2026-08-23/collected-raw.md#INFO-014) B-2、[INFO-019](../Information/2026-08-25/collected-raw.md#INFO-019) B-2）。AAIFへの新規加盟（計247社・[INFO-032](../Information/2026-08-19/collected-raw.md#INFO-032) B-2）と併せ、プロトコルの中立化は特定ベンダーロックイン回避の業界潮流として[H-GOO-002](../config/hypotheses.json)の開放C側に置く。Okta XAAのGA等、エージェント認証層の標準化も3層で並走する（v4.77記録）。

### 2社依存の定量化と価格の分裂

UBS試算は、OpenAIとAnthropicの2社でGoogle Cloud収益の27%（2026年）が、2027年には48%超（$124B超・Anthropic単独$76B）になると試算する。「2つの赤字企業のためにインフラを建設」との批判（Zitron）や、エージェント市場84%集中へのフランスのロックイン警告も同報告群にある（[INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067) B-2）。$150B超のAnthropicチップファイナンス契約網（[INFO-049](../Information/2026-08-05/collected-raw.md#INFO-049) A-2）と接続すれば、Googleのインフラ金融者化がCloud成長の実態である可能性が高まる。価格面では公式系の$0.75/$3.75紹介価格（2027年1月1日に$1.50/$7.50へ倍増予約・[INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) A-1、[INFO-037](../Information/2026-08-27/collected-raw.md#INFO-037) B-2）に対し、08-23バッチは「3.6 Flashの半額$0.38/$1.88」と報じる（[INFO-045](../Information/2026-08-23/collected-raw.md#INFO-045) B-2）。ティア・集計差の可能性があるが実効価格は確定できない。コンシューマー側はAI Plus $4.99/AI Pro $19.99/AI Ultra $99.99+の3段階に再編された。値上げ予約はSCN-003（静かな囲い込み）側の材料として蓄積を続ける。Gemini Enterpriseの契約条件批判（SLAなし・IP補償なし・PHI不可・責任上限$25,000）は単一個人分析ソース（[INFO-008](../Information/2026-08-27/collected-raw.md#INFO-008) D-3）で、24/7エンタープライズSLAを差別化する公式発言系報道（[INFO-027](../Information/2026-08-19/collected-raw.md#INFO-027) A-3）と緊張する。一次契約書確認まで計上外とする。

### 組織・政府面の継続観察

Koray Kavukcuogluがフロンティア研究からGeminiアプリまでを統括し、Demis HassabisはAGI・科学発見に専任する組織再編は維持されている（[INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) B-1）。HassabisのAGI到達予測は2030年まで50%でフロンティアCEO中最も保守的な位置を保つ（[INFO-116](../Information/2026-08-17/collected-raw.md#INFO-116) B-2）。政府面ではDoD 4社$200M同一2年契約（Anthropic/OpenAI/xAI/Google）の一角として参加し（[INFO-035](../Information/2026-08-23/collected-raw.md#INFO-035) C-2）、ペンタゴンのAnthropic排除（ほぼ100%）に伴うワークロード移管の受取側である（[INFO-054](../Information/2026-08-19/collected-raw.md#INFO-054) B-3）。移管先3社の内訳定量は不在のまま。AI軍事契約起因のDeepMind研究者流失は2人目で、§3のトリガー（3人以上）には未到達。Gemini Robotics ER 2（ビデオ入力でヒューマノイド/非ヒューマノイドの全身制御・産業/医療/物流展開）は研究軸の持続を示すが自家測定である（[INFO-023](../Information/2026-08-25/collected-raw.md#INFO-023) A-3）。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Vertex AI→GEAP吸収統合（Agent Builder/ADK/Agent Engine統合・Vertexブランド後退） | プラットフォーム単一化の実施。[H-GOO-002](../config/hypotheses.json) 囲い込みI方向とマルチモデル開放の両義 | A-2/A-3 | [INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012) [INFO-015](../Information/2026-08-24/collected-raw.md#INFO-015) |
| 高 | Vertex AI Extensions 2026-11-26以降シャットダウン（強制移行スケジュール付随） | 主力機能の終了。[H-GOO-002](../config/hypotheses.json) 囲い込みI方向の構造材料 | A-3 | [INFO-010](../Information/2026-08-23/collected-raw.md#INFO-010) |
| 高 | UBS試算: Google Cloud収益の27%（2026）→48%超（2027・$124B超）がOpenAI+Anthropic依存 | [H-GOO-001](../config/hypotheses.json) 分離不能性の定量化。成長の質への疑義 | B-2 | [INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067) |
| 高 | Grok 4.6 GEAP公式提供（$2/$6・500k ctx）+ gpt-oss 120B MaaS + EAP Model Garden self-deploy | マルチモデル配給の拡張。[H-GOO-002](../config/hypotheses.json) 開放C | A-3/B-2 | [INFO-002](../Information/2026-08-24/collected-raw.md#INFO-002) [INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) [INFO-065](../Information/2026-08-25/collected-raw.md#INFO-065) |
| 高 | A2A v1.0がAAIF（Linux Foundation）へ移管・150+組織採用・AAIF計247社 | 標準の中立化。[H-GOO-002](../config/hypotheses.json) 開放C。[IND-027](../config/indicators.json) | B-2 | [INFO-019](../Information/2026-08-25/collected-raw.md#INFO-019) [INFO-014](../Information/2026-08-23/collected-raw.md#INFO-014) [INFO-032](../Information/2026-08-19/collected-raw.md#INFO-032) |
| 高 | 3.7 Flash価格の分裂: $0.75/$3.75紹介→2027年1月1日倍増予約 vs 半額$0.38/$1.88報道 | 価格情報の定義未統一。値上げ予約はSCN-003材料として蓄積 | A-1/B-2 | [INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) [INFO-045](../Information/2026-08-23/collected-raw.md#INFO-045) [INFO-037](../Information/2026-08-27/collected-raw.md#INFO-037) |
| 高 | Gemini固有定量採用データ（A-2+品質のシェア・収益・利用率）が57R超構造的不在 | [H-GOO-001](../config/hypotheses.json) indeterminateの核心根拠。10億MAU存在下でも解消されず | 構造的 | [H-GOO-001](../config/hypotheses.json) |
| 中 | Gemini Enterprise契約批判: SLAなし・IP補償なし・PHI不可・責任上限$25,000 | エンタープライズ条件の弱さ指摘。D-3単一ソースで一次確認要・計上外 | D-3 | [INFO-008](../Information/2026-08-27/collected-raw.md#INFO-008) |
| 中 | 3.7 Flash $0.25/task vs Fable 5 $5.45・Vision上位30位中Google 8モデル | コストパフォーマンスとマルチモーダル配信の広さ | B-2 | [INFO-038](../Information/2026-08-27/collected-raw.md#INFO-038) [INFO-040](../Information/2026-08-27/collected-raw.md#INFO-040) |
| 中 | DoD 4社$200M同一2年契約の一角・ペンタゴン移管（2/3以上）の受取側 | 政府B2BのC方向。移管先3社の内訳定量は不在 | C-2/B-3 | [INFO-035](../Information/2026-08-23/collected-raw.md#INFO-035) [INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) [INFO-054](../Information/2026-08-19/collected-raw.md#INFO-054) |
| 中 | Gemini Robotics ER 2: ビデオ入力の全身制御・産業/医療/物流展開 | [H-GOO-003](../config/hypotheses.json) 研究軸の持続（自家測定） | A-3 | [INFO-023](../Information/2026-08-25/collected-raw.md#INFO-023) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Gemini固有の定量採用データ（A-2+品質のシェア・収益・利用率）が初めて公表される | [H-GOO-001](../config/hypotheses.json) indeterminate状態が解消し、low/mediumのいずれかに復帰する | 次回 | [H-GOO-001](../config/hypotheses.json) |
| 旧Vertex顧客の移行率・解約率・GEAP固有の採用数が定量で観測される | プラットフォーム統合の採用実態が初めて測定され、開放と統合の重心判別が始まる | 90日 | [IND-026](../config/indicators.json) |
| Extensions EOL（2026-11-26）までの移行完了率・機能ギャップ報告が観測される | 強制移行の実害が判定され、[H-GOO-002](../config/hypotheses.json) の囲い込みI側の確定または失効が始まる | 2026-11-26 | [H-GOO-002](../config/hypotheses.json) |
| Trusted+Captured分類が独立第2ソースで確認される、または囲い込み訴訟・ベンダーロックイン苦情が観測される | [H-GOO-002](../config/hypotheses.json) のlow帯が棄却方向に移動する | 120日 | [IND-027](../config/indicators.json) |
| Gemini 3.x系の価格が2027年1月1日に実際に倍増する、または期間延長・撤回が発表される | 価格権力の事前告知の検証。SCN-003材料の確定または失効 | 135日 | [IND-027](../config/indicators.json) |
| Google Cloud収益の対AIラボ依存度（UBS試算の27%→48%）が四半期開示等で検証される | [H-GOO-001](../config/hypotheses.json) のCloud-level成長解釈が変わり、分離不能性の実態判定が始まる | 90日 | [H-GOO-001](../config/hypotheses.json) |
| DeepMindの研究者流失が3人以上に増加し、安全性チームの体制変更が観測される | [H-GOO-003](../config/hypotheses.json) の研究卓越性から製品競争力への因果が揺らぐ（現在2人） | 180日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かし、エンタープライズAI市場でシェアを拡大する | 50% indeterminate | ±0%（v4.70のindeterminate維持以来・直近のDEGRADED帰因ラウンドは更新根拠なし）。Gemini固有定量採用データが57R超構造的不在（v4.70計上・以降のDEGRADED帰因ラウンドは分母不算入）。10億MAU（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1）・GEAP統合・Grok 4.6配給はavailabilityの拡張でadoptionの定量ではない。「Cのみ」状態は確証而非観測限界で、強制再評価条件の本章への拡張（駐車化対処）が検討事項として記録済み | [INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) [INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012) [INFO-059](../Information/2026-07-29/collected-raw.md#INFO-059) | Gemini固有採用定量の構造的不在継続・[INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067)（2社依存の定量化） |
| [H-GOO-002](../config/hypotheses.json) | GoogleはGemini Tools & Agentsでオープン標準（LangChain等）とのDay 0サポートを維持し、囲い込みを回避する | 24% low | +1%（23→24%・v4.76）。開放C側の新規証拠の純増（consistent_evidence配列新設・記録欄欠落の構造的是正）を認定。v4.77は更なる+1%を却下: 「hyperscaler 2社のOSS第一級市民化」の実質は1.5社（Google self-deployのみ中立経路）で、B-2解釈的優位で積み上げる構造は制度化リスク。Okta XAA（A-3）は表記訂正付きC。再評価条件はGCP公式self-deploy利用定量またはA-2以上品質の開放C出現時（v4.01枠組み継続）。囲い込みI側: GEAP統合・Extensions EOL・Trusted+Captured（単一ソース）。開放C側: Grok 4.6・gpt-oss MaaS・A2A/AAIF移管・gemini-skills | [INFO-002](../Information/2026-08-24/collected-raw.md#INFO-002) [INFO-019](../Information/2026-08-25/collected-raw.md#INFO-019) [INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) [INFO-032](../Information/2026-08-16/collected-raw.md#INFO-032) | [INFO-010](../Information/2026-08-23/collected-raw.md#INFO-010) [INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012) [INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% medium | ±0%（v4.06の48%到達以来）。A-2+品質の研究卓越性定量が20R連続未達成の累積ペナルティ継続で、48%以下継続ならmedium→low移行検討の条件が付帯。組織再編確定（Koray統括・Hassabis専任・[INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) B-1）は統合シナジーの組織的裏付けだが、研究卓越性の定量としては計上できない。Gemini Robotics ER 2（[INFO-023](../Information/2026-08-25/collected-raw.md#INFO-023) A-3）は自家測定のまま | [INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) [INFO-023](../Information/2026-08-25/collected-raw.md#INFO-023) | A-2+研究卓越性定量の20R連続未達成・研究者流失2人目（[INFO-056](../Information/2026-08-17/collected-raw.md#INFO-056) C-3） |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 複数ベンチマーク×複数ラボで再現ならhigh | elevated/stable（v4.81維持）。AVO・DeepSeek V4-Proとも閾値（複数ベンチ×複数ラボ再現）不充足でhigh移行候補2件はBlue在庫維持。Vision上位30位中Google 8モデル（[INFO-040](../Information/2026-08-27/collected-raw.md#INFO-040)）。3.7 Flashは$0.25/task（[INFO-038](../Information/2026-08-27/collected-raw.md#INFO-038)）。天井効果継続 | 2026-08-29 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率（スタック競争） | P(B)固有B-2+品質の採用定量出現で再評価 | high/rising（v4.81維持）。GEAP吸収統合・Grok 4.6配給・Gemini Agents APIでプラットフォーム機能は充填済みだが採用定量は不在。JetBrains調査（週次90%/日次68%・A-1）はsurvey-usage≠production-standardization注記付き | 2026-08-29 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度（MCP等オープン標準の採用） | 囲い込み側の制度化逆流で再評価 | high/rising（v4.81維持）。A2A v1.0/AAIF+Okta XAA GA+JetBrains ACPの3層標準化とAgentCore/Doubao配給（囲い込み側）の並走（v4.77記録）。価格権力（Google 2027年倍増予約・プレミアムシート$100-125/月）のKIQ-MONETIZATION監視継続 | 2026-08-29 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | high/rising（v4.81維持）。Hassabis「2030年まで50%」でフロンティアCEO中最も保守的（[INFO-116](../Information/2026-08-17/collected-raw.md#INFO-116) B-2）。予測分裂の新規データ点（OpenAI Astra申告系）と測定基盤汚染注記が継続 | 2026-08-29 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | critical/rising（v4.81維持・N=1実質28R）。ペンタゴンSCNリスク指定の継続報道（EVD-20260827-0078）。DoD 4社$200M契約の一角。EU AI法執行・EO 14409継続。critical解消条件3基準いずれも未到達 | 2026-08-29 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-08-29 | 全面書き直し（8日freshness timeout + 重要情報の未集積解消: GEAP吸収統合完了・Vertex AI Extensions 2026-11-26 EOL・A2A v1.0 AAIF移管・Grok 4.6 GEAP提供・UBS 2社依存定量化・Gemini Enterprise契約批判（D-3）を新規反映）。H-GOO-002 23→24%（v4.76）を遅って反映。廃止済み指標参照（IND-001/006）を現行指標（IND-025/026/027/028/030）へ更新。コア判断不変（測定不能・availability≠adoption） | 鮮度タイムアウト（8日）+ Arbiter v4.76〜v4.81 | H-GOO-001 50%（±0%）・H-GOO-002 23→24%・H-GOO-003 48%（±0%） |
| 2026-08-21 | 鮮度タイムアウト更新（7日経過）。08-15〜08-19バッチのGoogle関連情報（Phase 5 SKIP期間に本ファイルへ未集計だった分）を統合: Gemini月間10億ユーザー（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1）・I/O 2026「agentic Gemini era」・GEAP（旧Vertex AI）統合改名・組織再編確定（Koray統括・Hassabis AGI/科学発見専任）・3.7 Flash価格設計（2027年1月倍増予約・4推論ティア制）・ペンタゴン移管受取側・Turner退職（研究者流失2人目）を新規反映。コア判断不変（測定不能・availability≠adoption）。仮説確度は全件±0%（v4.73・DEGRADED 2R）。§5指標6件の現在値と最終確認日を更新 | 鮮度タイムアウト（7日）+ 未監査バッチの解消 | H-GOO-001 50% indeterminate（±0%）・H-GOO-002 23% low（±0%）・H-GOO-003 48% medium（±0%） |
| 2026-08-14 | ターゲット編集（構造的変化: フロンティアモデル新規リリース）。Gemini 3.7 Flashリリース（[INFO-001](../Information/2026-08-14/collected-raw.md#INFO-001) A-3）を新規反映。3.6 Flashの3週間後・GDP.pdf 34.0%(+12pt)・半額$0.75/$3.75・Gemini Spark即時展開。H-GOO-001 indeterminate/50% ±0%・H-GOO-002 23% low ±0%・H-GOO-003 48% medium ±0%（全件v4.66）。KIQ-GOO-001 46R/47R→48R/49R。コア判断不変（測定不能・availability≠adoption） | [INFO-001](../Information/2026-08-14/collected-raw.md#INFO-001) | KIQ-GOO-001 46R/47R→48R/49R・H-GOO-001 50%(±0%) |
| 2026-08-12 | 全面書き直し（7日freshness timeout + 構造的変化: CEO交代・新モデル群）。Gemini月間9.5億MAU（[INFO-005](../Information/2026-08-12/collected-raw.md#INFO-005) B-2）・Hassabis CEO→会長退任/Koray新CEO・Gemini 3.1 Pro/Antigravity Agent/Deep Research Max・Enterprise Agent Platform SLA・Gemini Robotics 2を新規反映。KIQ-GOO-001 44R/45R→46R/47R | [INFO-005](../Information/2026-08-12/collected-raw.md#INFO-005) [INFO-010](../Information/2026-08-12/collected-raw.md#INFO-010) [INFO-016](../Information/2026-08-12/collected-raw.md#INFO-016) [INFO-023](../Information/2026-08-12/collected-raw.md#INFO-023) | KIQ-GOO-001 44R/45R→46R/47R・H-GOO-001 50%(±0%) |
| 2026-08-05 | 全面書き直し（7日freshness timeout）。$150B Anthropicチップファイナンス契約網（[INFO-049](../Information/2026-08-05/collected-raw.md#INFO-049) A-2）でインフラ金融者への位置移行を新規構造的観察として記録。Gemini Robotics ER 2・Trusted+Captured分類・Enterprise Agent Platform更新を統合 | [INFO-049](../Information/2026-08-05/collected-raw.md#INFO-049) [INFO-020](../Information/2026-08-05/collected-raw.md#INFO-020) [INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) | KIQ-GOO-001 37R/38R→44R/45R |
| 2026-07-29 | 全面書き直し（7日freshness timeout）。Google Cloud Q2 +81.8%/$248億・GCP 14%最速成長・Managed Agents・Genesis Mission $40M DOE・AlphaEvolveを統合 | [INFO-059](../Information/2026-07-29/collected-raw.md#INFO-059) [INFO-033](../Information/2026-07-29/collected-raw.md#INFO-033) [INFO-008](../Information/2026-07-29/collected-raw.md#INFO-008) | KIQ-GOO-001 29R+→37R/38R |
| 2026-07-22 | 全面書き直し。フロンティアモデル新規リリース（Gemini 3.6 Flash・3.5 Flash-Lite）+ Gemini 4事前学習開始。「競争力低下確定」を「性能回復だが採用データ不在」に修正 | [INFO-003](../Information/2026-07-22/collected-raw.md#INFO-003) [INFO-004](../Information/2026-07-22/collected-raw.md#INFO-004) | 方向性偏り「下方」→「中間」 |

## 7. ブラインドスポット

- Gemini月間10億ユーザーは消費者アプリの指標であり、エンタープライズAI採用シェアの直接的定量ではない。無料利用から有料契約への転換率が測定不能なままである。Koray新CEOの戦略方向の判別も早期段階では不能で、Hassabis専任化が研究卓越性に与える影響は未測定である。
- Gemini固有定量データが57R超にわたり構造的に不在。indeterminate分類は分析の誠実さを保つ措置だが、駐車化への対処として強制再評価条件の本章拡張が記録されたまま実施されていない。下位命題分解の評価設計も未完成である。
- UBSの2社依存試算（27%→48%）は単一試算で、Cloud収益のGemini寄与分の分離は依然不能。試算の前提（契約ベースか見込みベースか）が開示されておらず、検証手段がない。
- GEAP移行の実態（旧Vertex顧客の移行率・解約率・GEAP固有の採用数）が取れていない。開放（マルチモデル・セルフデプロイ）と囲い込み（スタック単一化・Extensions EOL）の判別が困難なままである。
- 3.7 Flashの実効価格が確定できない。$0.75/$3.75（紹介価格・公式系）と$0.38/$1.88（半額報道）の差がティア・集計差なのか価格改定なのか、一次価格ページの時系列確認なしには判別できない。
- Trusted+Captured分類は単一ソース（kai-waehner.de）の分析で、独立した第2ソースでの確認がない。Gemini Enterprise契約条件批判（SLAなし・責任上限$25,000）もD-3単一ソースであり、一次契約書確認までエンタープライズ条件の実態は不明である。
- 性能データの自家測定占有率が高い。ARC-AGI-1 98%・DeepSWE 65.3%はGoogle提示値か単一報道で、Deep Think HLE 41%はC-3品質（SNS経由）で計上外。Gemini Robotics ER 2を含め独立ベンチマークでの検証が未完了である。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-008](../Information/2026-08-27/collected-raw.md#INFO-008) | Gemini Enterprise契約批判（SLAなし・IP補償なし・PHI不可・$25,000責任上限）・D-3単一ソースで一次確認要(D-3) |
| [INFO-037](../Information/2026-08-27/collected-raw.md#INFO-037) | 3.7 Flash投入08-13: $0.75/$3.75紹介価格→2027/1/1倍増・3.6 Flash値下げ・コンシューマー3段階再編(B-2) |
| [INFO-038](../Information/2026-08-27/collected-raw.md#INFO-038) | 3.7 Flash $0.25/task vs Fable 5 $5.45(B-2) |
| [INFO-040](../Information/2026-08-27/collected-raw.md#INFO-040) | Vision Arena上位30位中Google 8モデル(B-2) |
| [INFO-012](../Information/2026-08-25/collected-raw.md#INFO-012) | Vertex AI→GEAP吸収統合: Agent Builder/ADK/Agent Engine統合・Agent Engine改称(A-2) |
| [INFO-019](../Information/2026-08-25/collected-raw.md#INFO-019) | A2A v1.0がAAIFへ移管・150+組織採用・Linux Foundation中立ガバナンス(B-2) |
| [INFO-065](../Information/2026-08-25/collected-raw.md#INFO-065) | Google EAP Model Garden self-deploy・Azure Foundry gpt-oss直接販売・OSS第一級市民化(B-2) |
| [INFO-067](../Information/2026-08-25/collected-raw.md#INFO-067) | UBS試算: OpenAI+AnthropicでGoogle Cloud収益の27%→48%超・エージェント市場84%集中と仏警告(B-2) |
| [INFO-023](../Information/2026-08-25/collected-raw.md#INFO-023) | Gemini Robotics ER 2: ビデオ入力の全身制御・産業/医療/物流展開(A-3) |
| [INFO-002](../Information/2026-08-24/collected-raw.md#INFO-002) | Grok 4.6 on GEAP: $2/$6・500k ctx・ロングランニングエージェント向け(A-3) |
| [INFO-015](../Information/2026-08-24/collected-raw.md#INFO-015) | 「Vertex AI is now part of GEAP」公式release notes・4機能統一(A-3) |
| [INFO-010](../Information/2026-08-23/collected-raw.md#INFO-010) | Vertex AI Extensions 2026-11-26以降シャットダウン・強制移行スケジュール(A-3) |
| [INFO-014](../Information/2026-08-23/collected-raw.md#INFO-014) | A2AのAAIF移管・MCPと同じ傘下・WSO2/Yugabyte加盟(B-2) |
| [INFO-045](../Information/2026-08-23/collected-raw.md#INFO-045) | 3.7 Flash $0.38/$1.88（3.6 Flashの半額）報道・Flash階層の価格破壊(B-2) |
| [INFO-035](../Information/2026-08-23/collected-raw.md#INFO-035) | DoD 4社$200M同一2年契約の正式発表(C-2) |
| [INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) | Geminiアプリ月間10億ユーザー突破・Google公式ブログ(A-1) |
| [INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) | 3.7/3.6 Flash価格$0.75/$3.75→2027年1月1日$1.50/$7.50・4推論ティア制(A-1) |
| [INFO-137](../Information/2026-08-19/collected-raw.md#INFO-137) | 3.7 Flash DeepSWE v1.1 65.3%（+16.3pt）(B-1) |
| [INFO-054](../Information/2026-08-19/collected-raw.md#INFO-054) | ペンタゴン、ワークロード2/3以上をOpenAI/Google/Microsoftへ移管(B-3) |
| [INFO-032](../Information/2026-08-19/collected-raw.md#INFO-032) | AAIF 57新メンバーで計247社・Visa/Wells Fargo/Alibaba(B-2) |
| [INFO-027](../Information/2026-08-19/collected-raw.md#INFO-027) | GEAP: 24/7エンタープライズSLAを差別化(A-3) |
| [INFO-080](../Information/2026-08-17/collected-raw.md#INFO-080) | GEAP（旧Vertex AI）改名・Model Gardenセルフデプロイ(A-2) |
| [INFO-116](../Information/2026-08-17/collected-raw.md#INFO-116) | Hassabis「AGI到達は2030年まで50%」・最も保守的(B-2) |
| [INFO-056](../Information/2026-08-17/collected-raw.md#INFO-056) | 元DeepMind研究者Alex Turner退職（研究者流失2人目）(C-3) |
| [INFO-032](../Information/2026-08-16/collected-raw.md#INFO-032) | Google 100+公式Agent SkillsをClaude Code向けに提供・クロスベンダー化(B-2) |
| [INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) | 組織再編: Korayが研究〜Geminiアプリ統括・HassabisはAGI/科学発見専任(B-1) |
| [INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) | gpt-oss 120B（Apache 2.0）をGEAP MaaSで提供(A-3) |
| [INFO-090](../Information/2026-08-15/collected-raw.md#INFO-090) | 3.1 Pro ARC-AGI-1 98%（人間パネル並）・GPQA 94.1%(B-2) |
| [INFO-049](../Information/2026-08-05/collected-raw.md#INFO-049) | Google $150B+ Anthropicチップファイナンス・$15B DCローン・10%持分(A-2) |
| [INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) | Trusted Agentic AI Landscape Q3 2026: Google=Trusted+Captured(A-2・単一ソース) |
| [Arbiter v4.76/v4.77](../state/arbiter-2026-08-25.md) | H-GOO-002 +1%（23→24%・開放C純増認定）とv4.77の+1%却下（制度化リスク・1.5社判定） |
| [Arbiter v4.81](../state/arbiter-2026-08-29.md) | 全仮説±0%・指標全件維持（DEGRADED形式×Blue復帰初回・本日観測ゼロ） |
