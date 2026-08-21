# Google / DeepMind

> 最終判断更新: 2026-08-21
> 全体確信度: 測定不能（H-GOO-001 indeterminate維持）
> 情報非対称性: Geminiアプリ月間10億ユーザー突破をGoogle自身が公表した（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1・初出[INFO-009](../Information/2026-08-15/collected-raw.md#INFO-009) A-3）。ただしGemini固有のエンタープライズ定量採用データ（シェア・収益・利用率の直接定量A-2+）は57R超にわたり構造的に不在（[H-GOO-001](../config/hypotheses.json) v4.73時点）。MAUは消費者指標でありエンタープライズ採用シェアではない。Alphabetの開示セグメントにGemini固有の採用・収益は含まれず、Google Cloud収益成長とGemini固有需要の分離は不可能。Vertex AIは「Gemini Enterprise Agent Platform（GEAP）」へ統合・改名され、Model Garden経由でオープンモデルのセルフデプロイを統合（[INFO-080](../Information/2026-08-17/collected-raw.md#INFO-080) A-2）。組織再編はKoray Kavukcuogluがフロンティア研究からGeminiアプリまでを統括し、Demis HassabisはAGI・科学発見に専任する形で確定（[INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) B-1）。ベンチマークの多くが自家測定かC品質で、独立検証は限られる。
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-001](../config/indicators.json) [IND-006](../config/indicators.json) [IND-025](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はGoogleを「消費者AIアプリとして月間10億ユーザー到達を公式公表しながら、エンタープライズAI採用の固有定量データが57ラウンド超にわたり構造的に見えない企業」と読んでいる。Gemini月間10億ユーザー（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1）は消費者リーチとして最大級のシグナルで、史上最速成長との報道もある（[INFO-140](../Information/2026-08-17/collected-raw.md#INFO-140) C-2）。ただしMAUはエンタープライズ採用シェアの代理指標ではなく、この区別が[H-GOO-001](../config/hypotheses.json)のindeterminate分類を支える。Gemini固有の定量採用データ（A-2+品質のシェア・収益・利用率）が初めて公表されれば、この判断は変わる。

08-15〜08-19バッチ（本ファイルには未反映だった分）で観測が3層動いた。第一にI/O 2026でSundar Pichaiが「agentic Gemini era」を宣言し、Managed Agents（3.6 Flash・hooks・予算制御）とInteractions APIがGemini APIに加わった（[INFO-008](../Information/2026-08-15/collected-raw.md#INFO-008) A-3・[INFO-003](../Information/2026-08-19/collected-raw.md#INFO-003) A-1）。第二にVertex AIがGEAPへ統合・改名され、オープンモデルのセルフデプロイとgpt-oss 120BのMaaS提供が始まった（[INFO-018](../Information/2026-08-17/collected-raw.md#INFO-018) A-3・[INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) A-3）。第三にGemini 3.7 Flashの価格設計が、2026年末まで$0.75/$3.75、2027年1月1日から$1.50/$7.50への倍増予約、Standard/Batch/Flex/Priority（1.8x）の4推論ティア制と確定した（[INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) A-1）。いずれもavailability（利用可能であること）の拡張であって、adoption（採用されていること）の定量ではない。

## 1. コア判断

全体確信度は測定不能に置く。[H-GOO-001](../config/hypotheses.json)はindeterminate/50%で±0%（v4.73。DEGRADED 2R連続ラウンドで更新根拠なし）。Gemini固有の定量採用データが57R超にわたり構造的に不在である以上、10億MAUという消費者規模の追加だけでは確度ラベルを動かさない。これが本ファイルの座標軸であり、今回の更新で変わっていない。

### 10億MAUと採用データの分離

Geminiアプリの月間ユーザーが10億人を突破した（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1・Google公式ブログ）。08-12時点の9.5億（[INFO-005](../Information/2026-08-12/collected-raw.md#INFO-005) B-2）からの更新であり、消費者AIアプリとしてChatGPTに並ぶ規模との報道がある（[INFO-140](../Information/2026-08-17/collected-raw.md#INFO-140) C-2）。この数字が[H-GOO-001](../config/hypotheses.json)に与える影響は消費者リーチのC方向に限られる。無料消費利用から有料エンタープライズ契約への転換率、Gemini固有の収益寄与、企業での利用率。この3種の定量が不在のままである。Google Cloud Q2 2026収益$248億・YoY+81.8%（[INFO-059](../Information/2026-07-29/collected-raw.md#INFO-059) B-2）とGCPシェア14%（[INFO-033](../Information/2026-07-29/collected-raw.md#INFO-033) B-2）の成長は続くが、いずれもcloud-levelでありGemini固有ではない。

### プラットフォーム統合: GEAP改名とマルチモデルの両義

Vertex AIが「Gemini Enterprise Agent Platform」へ統合・改名された（[INFO-018](../Information/2026-08-17/collected-raw.md#INFO-018) A-3）。GEAPはModel Garden経由でオープンモデル・パートナーモデル・カスタムモデルのセルフデプロイを提供し（[INFO-080](../Information/2026-08-17/collected-raw.md#INFO-080) A-2・[INFO-096](../Information/2026-08-15/collected-raw.md#INFO-096) A-2）、企業デプロイの主潮流がAPI専用からクローズドAPIとオープンウェイトの併用へ移りつつある。OpenAIのgpt-oss 120B（Apache 2.0）をMaaSで提供し（[INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) A-3）、Claude Code向けに100以上の公式Agent Skillsを配布し（[INFO-032](../Information/2026-08-16/collected-raw.md#INFO-032) B-2）、gemini-skills公式リポジトリも公開した（[INFO-032](../Information/2026-08-17/collected-raw.md#INFO-032) A-3）。マルチモデルとスキル配布は[H-GOO-002](../config/hypotheses.json)（囲い込み回避23% low）の開放C方向の材料である。他方でGEAPへのブランド統合はスタック全体の単一化であり、Trusted Agentic AI Landscape Q3 2026の「Trusted+Captured」分類（[INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) A-2・単一ソース）と同じ方向の観察でもある。開放と統合のどちらに重心があるかは、旧Vertex顧客の移行とGEAP固有の採用定量が出るまで判別できない。

### 組織再編の確定とガバナンス

08-12報道段階では早期とされた組織再編の全体像が確定した。Koray Kavukcuogluがフロンティアモデル研究からGeminiアプリまで全製品・研究を統括し、Demis HassabisはAGI実現と科学発見に役割を特化する。「AGI・科学発見」が独立ミッションとして切り出された初の組織設計である（[INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) B-1）。Hassabisは退任前にトランプ政権へIAEA型のAGI監視機関を提案していたことがWSJ報道で明らかになった（[INFO-120](../Information/2026-08-17/collected-raw.md#INFO-120) A-2・[INFO-106](../Information/2026-08-16/collected-raw.md#INFO-106) A-2）。HassabisのAGI到達予測は2030年まで50%（[INFO-116](../Information/2026-08-17/collected-raw.md#INFO-116) B-2）で、フロンティアCEO中最も保守的な位置を維持する。組織面のこの確定は[H-GOO-003](../config/hypotheses.json)（DeepMind統合シナジー48% medium）の組織的裏付けだが、研究卓越性のA-2+定量としては計上できない。

### 政府面: ペンタゴン移管の受取側と研究者流失

ペンタゴンがAnthropicを軍事システムからほぼ100%除去し（[INFO-053](../Information/2026-08-19/collected-raw.md#INFO-053) B-2）、ワークロードの3分の2以上をOpenAI・Google・Microsoftへ移管したと報じられた（[INFO-054](../Information/2026-08-19/collected-raw.md#INFO-054) B-3）。Googleはこの移管の受取側であり、政府B2BのC方向の観察である。ただし移管先3社の内訳定量は不在で、品質もB-3中心のため確度変更の根拠にしない。元DeepMind研究者Alex Turnerが退職し、「軍はGoogleの先進モデルを法的制約なく利用可能」と述べたとの報道がある（[INFO-056](../Information/2026-08-17/collected-raw.md#INFO-056) C-3）。AI軍事契約起因の研究者流失は2人目（1人目は07-22の[INFO-050](../Information/2026-07-22/collected-raw.md#INFO-050) B-3）で、§3のトリガー（3人以上）には未到達。ホワイトハウスとMeta・Anthropic・Google・OpenAIの自発的安全テスト枠組みも報じられた（[INFO-139](../Information/2026-08-17/collected-raw.md#INFO-139) C-2・N=1問題の抑止効果代替解釈の候補）。

### 性能と価格: 3.7 Flashの位置

Gemini 3.1 Pro（Preview）がARC-AGI-1で98%（人間パネルと同等）・GPQA 94.1%に到達したとの報道がある（[INFO-090](../Information/2026-08-15/collected-raw.md#INFO-090) B-2）。Gemini 3.7 FlashはDeepSWE v1.1で65.3%（3.6 Flashの49.0%から+16.3pt・[INFO-137](../Information/2026-08-19/collected-raw.md#INFO-137) B-1）、出力340.1 tok/sで186モデル中1位の速度首位（[INFO-072](../Information/2026-08-16/collected-raw.md#INFO-072) B-2）であり、$0.75/$3.75の紹介価格と合わせて低価格・高速・高エージェント性能の組み合わせを持つ。Gemini 3 Deep ThinkのHumanity's Last Exam 41%はC-3品質（SNS経由）のため計上外とする。価格面では2027年1月1日への倍増予約が公式料金ページで明示されており（[INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) A-1）、値上げの事前告知という価格権力の行使がSCN-003（静かな囲い込み）側の材料として蓄積している。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Gemini固有定量採用データ（A-2+品質のシェア・収益・利用率）が57R超にわたり構造的不在 | [H-GOO-001](../config/hypotheses.json) indeterminateの核心根拠。10億MAU存在下でも解消されず | 構造的 | [H-GOO-001](../config/hypotheses.json) |
| 高 | Geminiアプリ月間10億ユーザー突破（Google公式・08-12の9.5億から更新・史上最速成長との報道） | 消費者規模のC方向。availability≠adoptionの制約付き | A-1/C-2 | [INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) [INFO-140](../Information/2026-08-17/collected-raw.md#INFO-140) |
| 高 | Vertex AI→GEAP統合・改名。Model Gardenでオープンモデル・セルフデプロイ提供 | プラットフォーム統合の進行。マルチモデル開放とスタック単一化の両義 | A-2/A-3 | [INFO-080](../Information/2026-08-17/collected-raw.md#INFO-080) [INFO-018](../Information/2026-08-17/collected-raw.md#INFO-018) [INFO-096](../Information/2026-08-15/collected-raw.md#INFO-096) |
| 高 | I/O 2026「agentic Gemini era」宣言・Managed Agents（3.6 Flash・hooks）・Interactions API・外部アプリ接続拡大 | エージェント層の製品化。[H-GOO-001](../config/hypotheses.json) プラットフォーム深化C方向 | A-3/A-1 | [INFO-008](../Information/2026-08-15/collected-raw.md#INFO-008) [INFO-003](../Information/2026-08-19/collected-raw.md#INFO-003) [INFO-014](../Information/2026-08-19/collected-raw.md#INFO-014) |
| 高 | Gemini 3.7/3.6 Flash価格設計: 2026年末まで$0.75/$3.75→2027年1月1日から$1.50/$7.50・4推論ティア制（Standard/Batch/Flex/Priority 1.8x） | 価格権力の事前告知。SCN-003材料として蓄積（[IND-027](../config/indicators.json) 監視中） | A-1 | [INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) [INFO-067](../Information/2026-08-16/collected-raw.md#INFO-067) |
| 高 | 組織再編確定: Koray Kavukcuogluが研究〜Geminiアプリ統括・HassabisはAGI・科学発見専任（独立ミッションとして初の切り出し） | [H-GOO-003](../config/hypotheses.json) 統合シナジーの組織的裏付け。研究卓越性の定量ではない | B-1 | [INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) |
| 高 | Google $150B+ Anthropicチップファイナンス契約網・$15B DCローン裏書き・約10%持分 | インフラ金融者への位置移行。Cloud収益とGemini固有需要の分離不能性が拡大 | A-2 | [INFO-049](../Information/2026-08-05/collected-raw.md#INFO-049) |
| 高 | Google Cloud Q2 2026収益$248億・YoY+81.8%・GCPシェア14%（年間最速成長） | cloud-level成長の継続。Gemini固有の採用シェアではない | B-2 | [INFO-059](../Information/2026-07-29/collected-raw.md#INFO-059) [INFO-033](../Information/2026-07-29/collected-raw.md#INFO-033) |
| 高 | Trusted Agentic AI Landscape Q3 2026: Google=Trusted+Captured | [H-GOO-002](../config/hypotheses.json) 囲い込みI方向。単一ソースで独立検証保留 | A-2 | [INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) |
| 中 | 3.1 Pro ARC-AGI-1 98%・GPQA 94.1%・3.7 Flash DeepSWE v1.1 65.3%（+16.3pt）・出力340.1 tok/s速度首位（186モデル中1位） | 性能軸のC方向。自家測定中心で独立検証は限定的 | B-2/B-1 | [INFO-090](../Information/2026-08-15/collected-raw.md#INFO-090) [INFO-137](../Information/2026-08-19/collected-raw.md#INFO-137) [INFO-072](../Information/2026-08-16/collected-raw.md#INFO-072) |
| 中 | ペンタゴンのAnthropic排除（ほぼ100%）の受取側としてOpenAI/Google/Microsoftへワークロード2/3以上移管 | 政府B2BのC方向。移管先3社の内訳定量は不在 | B-2/B-3 | [INFO-053](../Information/2026-08-19/collected-raw.md#INFO-053) [INFO-054](../Information/2026-08-19/collected-raw.md#INFO-054) |
| 中 | gpt-oss 120B（Apache 2.0）のGEAP MaaS提供・Claude Code向け100+公式Agent Skills・gemini-skills公式リポジトリ | [H-GOO-002](../config/hypotheses.json) 開放C方向（クロスベンダー配布） | A-3/B-2 | [INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) [INFO-032](../Information/2026-08-16/collected-raw.md#INFO-032) [INFO-032](../Information/2026-08-17/collected-raw.md#INFO-032) |
| 中 | Hassabisが退任前にIAEA型AGI監視機関を政権へ提案（WSJ）・AGI到達予測は2030年まで50% | [H-GOO-003](../config/hypotheses.json) ガバナンス関与。[IND-028](../config/indicators.json) 保守的予測の維持 | A-2/B-2 | [INFO-120](../Information/2026-08-17/collected-raw.md#INFO-120) [INFO-116](../Information/2026-08-17/collected-raw.md#INFO-116) |
| 中 | 元DeepMind研究者Alex Turner退職（「軍はGoogleの先進モデルを法的制約なく利用可能」） | 研究者流失2人目。[H-GOO-003](../config/hypotheses.json) §3トリガー（3人以上）未到達 | C-3 | [INFO-056](../Information/2026-08-17/collected-raw.md#INFO-056) [INFO-050](../Information/2026-07-22/collected-raw.md#INFO-050) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Gemini固有の定量採用データ（A-2+品質のシェア・収益・利用率）が初めて公表される | [H-GOO-001](../config/hypotheses.json) indeterminate状態が解消し、low/mediumのいずれかに復帰する | 次回 | [H-GOO-001](../config/hypotheses.json) |
| Google Cloud収益成長のGemini固有寄与分が定量分離される | 復帰条件の一部充足。Q2 +81.8%のGemini寄与が定量で示されればC方向の確度上昇根拠 | 90日 | [H-GOO-001](../config/hypotheses.json) |
| GEAP（旧Vertex AI）移行後の既存Vertex顧客の移行率・解約率・GEAP固有の採用数が定量で観測される | プラットフォーム統合の採用実態が初めて測定され、開放と統合のどちらに重心があるかの判別が始まる | 90日 | [IND-006](../config/indicators.json) |
| Trusted+Captured分類が独立第2ソースで確認される、または囲い込み訴訟・ベンダーロックイン苦情が観測される | [H-GOO-002](../config/hypotheses.json) のlow帯が棄却方向に移動する | 120日 | [IND-027](../config/indicators.json) |
| Gemini 3.x系の価格が2027年1月1日に実際に倍増する、または期間延長・撤回が発表される | 価格権力の事前告知が実行に移るかの検証。SCN-003材料の確定または失効 | 135日 | [IND-027](../config/indicators.json) |
| Gemini Robotics 2の性能が独立ベンチマークで検証される、または競合ロボティクスモデルが同等性能に到達する | [H-GOO-003](../config/hypotheses.json) の研究卓越性C方向が強化または弱体化する | 180日 | [IND-001](../config/indicators.json) |
| DeepMindの研究者流失が3人以上に増加し、安全性チームの体制変更が観測される | [H-GOO-003](../config/hypotheses.json) の研究卓越性から製品競争力への因果が揺らぐ（現在2人） | 180日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かし、エンタープライズAI市場でシェアを拡大する | 50% indeterminate | ±0%（v4.73・DEGRADED 2Rで更新根拠なし。前回変更はv4.01の再定式化以来±0%）。Gemini固有定量採用データが57R超構造的不在（v4.70計上・以降のDEGRADED帰因ラウンドは分母不算入）。10億MAU（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1）・I/O 2026・GEAP統合はC方向だがavailability≠adoptionで確度ラベル変更の根拠にならない。「Cのみ」状態は確証而非観測限界 | [INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) [INFO-008](../Information/2026-08-15/collected-raw.md#INFO-008) [INFO-059](../Information/2026-07-29/collected-raw.md#INFO-059) | Gemini固有採用定量の構造的不在継続 |
| [H-GOO-002](../config/hypotheses.json) | GoogleはGemini Tools & Agentsでオープン標準とのDay 0サポートを維持し囲い込みを回避する | 23% low | ±0%（v4.01以来・v4.73も±0%）。Trusted+Captured分類（[INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) A-2・単一ソース）とGEAPへのスタック統合が囲い込みI方向、gpt-oss MaaS（[INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) A-3）・100+公式Skills（[INFO-032](../Information/2026-08-16/collected-raw.md#INFO-032) B-2）・セルフデプロイ（[INFO-080](../Information/2026-08-17/collected-raw.md#INFO-080) A-2）が開放C方向。品質調整後は実質均衡で、囲い込みIのA-2以上品質による再カウントが次回条件 | [INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) [INFO-032](../Information/2026-08-16/collected-raw.md#INFO-032) [INFO-080](../Information/2026-08-17/collected-raw.md#INFO-080) | [INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) [INFO-018](../Information/2026-08-17/collected-raw.md#INFO-018) |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% medium | ±0%（v4.06の48%到達以来・v4.73も±0%）。A-2+品質の研究卓越性定量が20R連続未達成の累積ペナルティ継続で、48%以下継続ならmedium→low移行検討の条件が付帯。組織再編確定（Koray統括・[INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) B-1）は統合シナジーの組織的裏付けだが、研究卓越性の定量としては計上できない。Gemini Robotics 2（[INFO-023](../Information/2026-08-12/collected-raw.md#INFO-023) A-3）は自家測定のまま | [INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) [INFO-023](../Information/2026-08-12/collected-raw.md#INFO-023) | A-2+研究卓越性定量の20R連続未達成・研究者流失2人目（[INFO-056](../Information/2026-08-17/collected-raw.md#INFO-056) C-3） |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt以上/期でhigh | Gemini 3.1 Pro ARC-AGI-1 98%（人間パネル並）・GPQA 94.1%（[INFO-090](../Information/2026-08-15/collected-raw.md#INFO-090) B-2）。3.7 Flash DeepSWE v1.1 65.3%（3.6 Flash比+16.3pt・[INFO-137](../Information/2026-08-19/collected-raw.md#INFO-137) B-1）・出力340.1 tok/sで186モデル中1位（[INFO-072](../Information/2026-08-16/collected-raw.md#INFO-072) B-2）。ARC-AGI-3はGPT-5.6 Sol 40%に対しGemini 3.1 Pro 30.2%。Deep Think HLE 41%はC-3で計上外。Robotics 2の公開ベンチマーク検証なし。elevated/stable | 2026-08-21 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated維持で継続監視 | GEAP（旧Vertex AI）統合・改名（[INFO-018](../Information/2026-08-17/collected-raw.md#INFO-018) A-3）。Managed Agents（3.6 Flash・hooks・予算制御・[INFO-003](../Information/2026-08-19/collected-raw.md#INFO-003) A-1）・Interactions API・gemini-skills公式リポジトリ（[INFO-032](../Information/2026-08-17/collected-raw.md#INFO-032) A-3）・Agent Plugins 1.0.0 6社共同（[INFO-043](../Information/2026-08-15/collected-raw.md#INFO-043) C-2）。24/7エンタープライズSLA（[INFO-027](../Information/2026-08-19/collected-raw.md#INFO-027) A-3）。プラットフォーム機能は充填済みだが採用定量不在で評価不能。elevated/rising | 2026-08-21 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | Intelligence Index Opus 5(63.1)>GPT-5.6 Sol(60.9)>Kimi K3(59.7)の3-4pt差。3.7 FlashはDeepSWE 65.3%と速度首位でコストパレート最前線（BenchLM系でオープンウェイトは専有比80%安・最安フロンティア帯）。天井効果継続。08-20/21はDEGRADEDで新規観測なし。期限付き審査（ARC-AGI-3他ラボ再現・[INFO-127](../Information/2026-08-19/collected-raw.md#INFO-127)は単一ラボ×単一ベンチ家族で再現性未充足）は自動延長条項1回目を記録（形式審査「閾値維持」）。elevated/stable | 2026-08-21 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | AAIF 57新メンバー加入で計247社（Visa・Wells Fargo・Alibaba・[INFO-032](../Information/2026-08-19/collected-raw.md#INFO-032) B-2）・Agent Plugins 1.0.0（Google/OpenAI/Amazon/Microsoft/Cursor/Vercel・[INFO-043](../Information/2026-08-15/collected-raw.md#INFO-043) C-2）・MCP RC stateless・Google AP2 60+パートナー・AWS AgentCore MCPゲートウェイ。GEAP階層化と価格権力（2027年1月倍増予約・抽傭18%等）の事前告知蓄積はSCN-003側C候補として監視継続。high/rising | 2026-08-21 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | Hassabis「2030年まで50%」（[INFO-116](../Information/2026-08-17/collected-raw.md#INFO-116) B-2）でフロンティアCEO中最も保守的。IAEA型AGI監視機関の政権提案（[INFO-120](../Information/2026-08-17/collected-raw.md#INFO-120) A-2）。ARC-AGI-3機能依存性（同一モデル13.3%→38.3%・[INFO-127](../Information/2026-08-19/collected-raw.md#INFO-127) B-1）による測定基盤汚染の注記継続。RSI概念の具体化と限界の同時進行。high/rising | 2026-08-21 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | critical/rising。ペンタゴンAnthropic排除ほぼ100%（[INFO-053](../Information/2026-08-19/collected-raw.md#INFO-053) B-2）・ワークロード2/3以上のOpenAI/Google/Microsoft移管（[INFO-054](../Information/2026-08-19/collected-raw.md#INFO-054) B-3）・ホワイトハウス×Meta/Anthropic/Google/OpenAIの自発的安全テスト枠組み（[INFO-139](../Information/2026-08-17/collected-raw.md#INFO-139) C-2・N=1問題の抑止効果代替解釈候補）。Googleは2025年にAI兵器使用禁止を解除済み。EU AI法執行権限発動・Trump大統領令14409は継続。critical解消条件3基準いずれも未到達 | 2026-08-21 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-08-21 | 鮮度タイムアウト更新（7日経過）。08-15〜08-19バッチのGoogle関連情報（Phase 5 SKIP期間に本ファイルへ未集計だった分）を統合: Gemini月間10億ユーザー（[INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) A-1）・I/O 2026「agentic Gemini era」・GEAP（旧Vertex AI）統合改名・組織再編確定（Koray統括・Hassabis AGI/科学発見専任）・3.7 Flash価格設計（2027年1月倍増予約・4推論ティア制）・ペンタゴン移管受取側・Turner退職（研究者流失2人目）を新規反映。コア判断不変（測定不能・availability≠adoption）。仮説確度は全件±0%（v4.73・DEGRADED 2R）。§5指標6件の現在値と最終確認日を更新 | 鮮度タイムアウト（7日）+ 未監査バッチの解消 | H-GOO-001 50% indeterminate（±0%）・H-GOO-002 23% low（±0%）・H-GOO-003 48% medium（±0%） |
| 2026-08-14 | ターゲット編集（構造的変化: フロンティアモデル新規リリース）。Gemini 3.7 Flashリリース（[INFO-001](../Information/2026-08-14/collected-raw.md#INFO-001) A-3）を新規反映。3.6 Flashの3週間後・GDP.pdf 34.0%(+12pt)・半額$0.75/$3.75・Gemini Spark即時展開。H-GOO-001 indeterminate/50% ±0%・H-GOO-002 23% low ±0%・H-GOO-003 48% medium ±0%（全件v4.66）。KIQ-GOO-001 46R/47R→48R/49R。コア判断不変（測定不能・availability≠adoption） | [INFO-001](../Information/2026-08-14/collected-raw.md#INFO-001) | KIQ-GOO-001 46R/47R→48R/49R・H-GOO-001 50%(±0%) |
| 2026-08-12 | 全面書き直し（7日freshness timeout + 構造的変化: CEO交代・新モデル群）。Gemini月間9.5億MAU（[INFO-005](../Information/2026-08-12/collected-raw.md#INFO-005) B-2）・Hassabis CEO→会長退任/Koray新CEO（[INFO-005](../Information/2026-08-12/collected-raw.md#INFO-005) B-2）・Gemini 3.1 Pro/Antigravity Agent/Deep Research Max（[INFO-010](../Information/2026-08-12/collected-raw.md#INFO-010) A-3）・Enterprise Agent Platform SLA（[INFO-016](../Information/2026-08-12/collected-raw.md#INFO-016) A-3）・Gemini Robotics 2（[INFO-023](../Information/2026-08-12/collected-raw.md#INFO-023) A-3）を新規反映。KIQ-GOO-001 44R/45R→46R/47R | [INFO-005](../Information/2026-08-12/collected-raw.md#INFO-005) [INFO-010](../Information/2026-08-12/collected-raw.md#INFO-010) [INFO-016](../Information/2026-08-12/collected-raw.md#INFO-016) [INFO-023](../Information/2026-08-12/collected-raw.md#INFO-023) | KIQ-GOO-001 44R/45R→46R/47R・H-GOO-001 50%(±0%) |
| 2026-08-05 | 全面書き直し（7日freshness timeout）。$150B Anthropicチップファイナンス契約網（[INFO-049](../Information/2026-08-05/collected-raw.md#INFO-049) A-2）でインフラ金融者への位置移行を新規構造的観察として記録。Gemini Robotics ER 2・Trusted+Captured分類・Enterprise Agent Platform更新を統合 | [INFO-049](../Information/2026-08-05/collected-raw.md#INFO-049) [INFO-020](../Information/2026-08-05/collected-raw.md#INFO-020) [INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) | KIQ-GOO-001 37R/38R→44R/45R |
| 2026-07-29 | 全面書き直し（7日freshness timeout）。Google Cloud Q2 +81.8%/$248億・GCP 14%最速成長・Managed Agents・Genesis Mission $40M DOE・AlphaEvolveを統合 | [INFO-059](../Information/2026-07-29/collected-raw.md#INFO-059) [INFO-033](../Information/2026-07-29/collected-raw.md#INFO-033) [INFO-008](../Information/2026-07-29/collected-raw.md#INFO-008) | KIQ-GOO-001 29R+→37R/38R |
| 2026-07-22 | 全面書き直し。フロンティアモデル新規リリース（Gemini 3.6 Flash・3.5 Flash-Lite）+ Gemini 4事前学習開始。「競争力低下確定」を「性能回復だが採用データ不在」に修正 | [INFO-003](../Information/2026-07-22/collected-raw.md#INFO-003) [INFO-004](../Information/2026-07-22/collected-raw.md#INFO-004) | 方向性偏り「下方」→「中間」 |

## 7. ブラインドスポット

- Gemini月間10億ユーザーは消費者アプリの指標であり、エンタープライズAI採用シェアの直接的定量データではない。無料利用から有料契約への転換率が測定不能なままである。Koray新CEOの戦略方向の判別も早期段階では不能で、Hassabis専任化が研究卓越性に与える影響は未測定である。
- Gemini固有定量データが57R超にわたり構造的に不在。indeterminate分類は分析の誠実さを保つ措置だが、「情報が来るまで待つ」希望的駐車にならないよう、復帰条件の明文化と下位命題分解が必須で、下位命題の個別評価設計が未完成のままである。
- Google Cloud Q2 +81.8%のGemini固有寄与分の分離が不可能。$150B Anthropicチップファイナンス契約網の発見で、Cloud収益成長の一部がGemini以外のAI需要に牽引されている可能性が高まり、この分離不能性は拡大する一方である。
- GEAP（旧Vertex AI）への統合・改名後、既存Vertex顧客の移行率・解約率・GEAP固有の採用数が取れていない。プラットフォーム統合の規模を実態として測定する手段がなく、開放（マルチモデル・セルフデプロイ）と囲い込み（スタック単一化）の判別が困難なままである。
- Trusted+Captured分類が単一ソース（kai-waehner.de）の分析である。独立した第2ソースでの確認がない状態で、Googleの囲い込み程度を確定できない。
- 性能データの自家測定占有率が高い。DeepSWE 65.3%・ARC-AGI-1 98%はいずれもGoogle提示値か単一報道で、Gemini 3 Deep Think HLE 41%はC-3品質（SNS経由）で計上外。独立ベンチマークでの検証がRobistics 2含め未完了である。
- Genesis Mission（278チーム・DOE国立研究所）が商用エンタープライズ採用の代理指標として意味を持つかが不明。政府・科学分野での利用は特定の採用シグナルだが、市場シェアの定量的指標ではない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-013](../Information/2026-08-19/collected-raw.md#INFO-013) | Geminiアプリ月間10億ユーザー突破・Google公式ブログ(A-1) |
| [INFO-003](../Information/2026-08-19/collected-raw.md#INFO-003) | Gemini API Managed Agents: 3.6 Flash・hooks・予算制御(A-1) |
| [INFO-066](../Information/2026-08-19/collected-raw.md#INFO-066) | 3.7/3.6 Flash価格$0.75/$3.75（年末まで）→2027年1月1日$1.50/$7.50・4推論ティア制(A-1) |
| [INFO-137](../Information/2026-08-19/collected-raw.md#INFO-137) | 3.7 Flash DeepSWE v1.1 65.3%（3.6 Flash比+16.3pt）・$0.75/$3.75ワークホース(B-1) |
| [INFO-022](../Information/2026-08-19/collected-raw.md#INFO-022) | GEAP公開・Interactions APIでエージェント統合(A-3) |
| [INFO-027](../Information/2026-08-19/collected-raw.md#INFO-027) | GEAP: 24/7エンタープライズSLAを差別化(A-3) |
| [INFO-053](../Information/2026-08-19/collected-raw.md#INFO-053) | Pentagon Anthropic排除「ほぼ完了」・軍事システムから100%近く除去(B-2) |
| [INFO-054](../Information/2026-08-19/collected-raw.md#INFO-054) | ペンタゴン、ワークロード2/3以上をOpenAI/Google/Microsoftへ移管(B-3) |
| [INFO-032](../Information/2026-08-19/collected-raw.md#INFO-032) | AAIF 57新メンバーで計247社・Visa/Wells Fargo/Alibaba(B-2) |
| [INFO-127](../Information/2026-08-19/collected-raw.md#INFO-127) | ARC-AGI-3機能依存性（同一モデル13.3%→38.3%）・測定基盤汚染の注記材料(B-1) |
| [INFO-080](../Information/2026-08-17/collected-raw.md#INFO-080) | GEAP（旧Vertex AI）改名・Model Gardenセルフデプロイ・ハイブリッド企業展開(A-2) |
| [INFO-018](../Information/2026-08-17/collected-raw.md#INFO-018) | Vertex AI→GEAP統合・改名(A-3) |
| [INFO-120](../Information/2026-08-17/collected-raw.md#INFO-120) | Hassabis退任前にIAEA型AGI監視機関を政権へ提案・WSJ(A-2) |
| [INFO-116](../Information/2026-08-17/collected-raw.md#INFO-116) | CEO予測の分化: Hassabis「2030年まで50%」(B-2) |
| [INFO-140](../Information/2026-08-17/collected-raw.md#INFO-140) | Gemini月間10億人到達・Google史上最速成長(C-2) |
| [INFO-056](../Information/2026-08-17/collected-raw.md#INFO-056) | 元DeepMind研究者Alex Turner退職・Google軍事合意の法的制約なし(C-3) |
| [INFO-032](../Information/2026-08-17/collected-raw.md#INFO-032) | gemini-skills公式リポジトリ・Gemini Enterpriseスキル管理(A-3) |
| [INFO-139](../Information/2026-08-17/collected-raw.md#INFO-139) | ホワイトハウス×Meta/Anthropic/Google/OpenAI自発的安全テスト枠組み(C-2) |
| [INFO-032](../Information/2026-08-16/collected-raw.md#INFO-032) | Google 100+公式Agent SkillsをClaude Code向けに提供・クロスベンダー化(B-2) |
| [INFO-072](../Information/2026-08-16/collected-raw.md#INFO-072) | 3.7 Flash出力340.1 tok/s・186モデル中1位の速度首位(B-2) |
| [INFO-106](../Information/2026-08-16/collected-raw.md#INFO-106) | HassabisのIAEA型AGI監視機関提案・WSJ報道(A-2) |
| [INFO-067](../Information/2026-08-16/collected-raw.md#INFO-067) | 2026年末まで半額・2027年1月1日倍増の移行価格構造(A-3) |
| [INFO-008](../Information/2026-08-15/collected-raw.md#INFO-008) | I/O 2026「agentic Gemini era」宣言(A-3) |
| [INFO-009](../Information/2026-08-15/collected-raw.md#INFO-009) | Gemini月間10億ユーザー突破の初出(A-3) |
| [INFO-133](../Information/2026-08-15/collected-raw.md#INFO-133) | 組織再編: Korayが研究〜Geminiアプリ統括・HassabisはAGI/科学発見専任(B-1) |
| [INFO-042](../Information/2026-08-15/collected-raw.md#INFO-042) | gpt-oss 120B（Apache 2.0）をGEAP MaaSで提供(A-3) |
| [INFO-096](../Information/2026-08-15/collected-raw.md#INFO-096) | GEAP Model Gardenでオープンモデル・セルフデプロイ(A-2) |
| [INFO-090](../Information/2026-08-15/collected-raw.md#INFO-090) | 3.1 Pro ARC-AGI-1 98%（人間パネル並）・GPQA 94.1%(B-2) |
| [INFO-043](../Information/2026-08-15/collected-raw.md#INFO-043) | Agent Plugins 1.0.0・6社共同のスキル+MCPパッケージ標準(C-2) |
| [INFO-001](../Information/2026-08-14/collected-raw.md#INFO-001) | Gemini 3.7 Flash: GDP.pdf 34.0%(+12pt)・半額$0.75/$3.75・Gemini Spark即時展開(A-3) |
| [INFO-005](../Information/2026-08-12/collected-raw.md#INFO-005) | Gemini月間9.5億MAU・Hassabis CEO→会長退任・Koray新CEO・Gemini 4示唆(B-2) |
| [INFO-010](../Information/2026-08-12/collected-raw.md#INFO-010) | Gemini 3.1 Pro/Flash・Antigravity Agent・Deep Research Max・新モデル群展開(A-3) |
| [INFO-016](../Information/2026-08-12/collected-raw.md#INFO-016) | GEAP SLA導入・Vertex AI preview・Production Agent Checklist(A-3) |
| [INFO-023](../Information/2026-08-12/collected-raw.md#INFO-023) | Gemini Robotics 2: 全身制御・器用さ・チームワーク3モデル・ER 1.6(A-3) |
| [INFO-049](../Information/2026-08-05/collected-raw.md#INFO-049) | Google $150B+ Anthropicチップファイナンス・$15B DCローン・10%持分(A-2) |
| [INFO-080](../Information/2026-08-05/collected-raw.md#INFO-080) | Trusted Agentic AI Landscape Q3 2026: Google=Trusted+Captured(A-2) |
| [INFO-013](../Information/2026-08-05/collected-raw.md#INFO-013) | Vertex AI→GEAP統合: ERP/CRMグラウンディング(A-3) |
| [INFO-059](../Information/2026-07-29/collected-raw.md#INFO-059) | Google Cloud Q2 2026: 収益$248億・YoY+81.8%(B-2) |
| [INFO-033](../Information/2026-07-29/collected-raw.md#INFO-033) | GCP市場シェア14%・年間最速成長12%→14%(B-2) |
| [INFO-050](../Information/2026-07-22/collected-raw.md#INFO-050) | DeepMind研究者辞任（1人目）・AI Safety Index軍事AIピボット指摘(B-3) |
