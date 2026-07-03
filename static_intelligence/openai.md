# OpenAI

> 最終判断更新: 2026-07-03
> 全体確信度: 中低
> 情報非対称性: 収益内訳（API/Enterprise/Consumerセグメント・政府vs民間）が非公開（KIQ-OAI-001未回答継続）。月次約$2B収益・年率$20-24B（INFO-051 A-2）は確認できたが、セグメント内訳は不変。H1 2025で収入$4.3Bに対し純損失$13.5B（構造的赤字・INFO-051 A-2）。5%政府株式提案（Alaska Permanent Fund型・INFO-063 A-1）で政治的障害クリアを模索。GPT-5.6（Sol/Terra/Luna）3バリアントの広範リリース延期をTrump政権が要請（INFO-063 A-1）。MicrosoftとのStargate合弁でOracle追加、Direct Compute比率増で排他性低下（INFO-037 B-1）。Arbiter v4.27は±0%の根拠を「C/I均衡」から「核心パラメータ不在による確度変更保留」に修正。Arbiter v4.27 COMPLETE
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-OAI-001](../config/hypotheses.json) は49%（medium）で±0%。前回更新時（2026-06-29）の48%からv4.24で+1%され、以降3R連続で±0%維持である。Arbiter v4.27は±0%の根拠を「コンプライアンス優位とコモディティ化の均衡」から「核心パラメータ不在による確度変更保留」に修正した（[INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) A-2）。収益内訳（API/Enterprise/Consumer・政府vs民間）が非公開である限り、B2B支配地位の収益的裏付けを質的に評価できず、確度の上下いずれの変更も根拠不足となる。

本ラウンドの支配的展開は、OpenAIが米国政府に5%株式を「Alaska Permanent Fund型」車両として提供する提案である（[INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) A-1）。Sam AltmanはTrump大統領・Lutnick商務長官・Bessent財務長官と協議し、Bernie Sanders上院議員（50%株式要求）と面会した。同時にTrump政権はGPT-5.6（Sol/Terra/Luna）の広範リリース延期を要請した。政府との取引的関係構築は、コンプライアンス優位の制度化というより政治的障害の財務的解消である。Anthropicは対照的に株式議論を行わず、「digital dividend」（AI税→国民配当）を対抗案として提示した。

OpenAIの財務構造は構造的赤字である。月次約$2B収益・年率$20-24Bに達する成長と、H1 2025で$13.5Bの純損失が同時に存在する（[INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) A-2）。MicrosoftとのStargate合弁でOracleがインフラパートナーとして追加され、Azureの排他的地位が低下している（[INFO-037](../Information/2026-07-03/collected-raw.md#INFO-037) B-1）。DeepSeek V4がGPT-4oレベルの性能をAPI価格10分の1で提供し（[INFO-038](../Information/2026-07-03/collected-raw.md#INFO-038) A-2）、コモディティ化圧力は量的に深化している。

[H-OAI-002](../config/hypotheses.json) は44%（low）で±0%。Agent SDKのプロバイダ非依存性で围い込み否定証拠の累積が継続する。[H-OAI-003](../config/hypotheses.json) は3%（low）で±0%。商業化規模の圧倒的証拠が継続し、AGI最優先を支持するA-2以上の証拠は不在である。

## 1. コア判断

全体確信度は中低。H-OAI-001 49% ±0%の根拠が前回から変更された。Arbiter v4.27はRedの表現修正を採用し、「C/I均衡」という framingを却下した。49%の根拠は、コンプライアンス優位とコモディティ化が均衡しているからではない。収益内訳（KIQ-OAI-001）が不在であるため、確度変更の根拠が形成できないことである。

### 核心パラメータ不在が制約する

OpenAIの収益は月次約$2B、年率$20-24Bに達する（[INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) A-2）。2025年通期収益は$13.1B。だが、API accessとChatGPTサブスクリプションは別課金であり、政府向け・エンタープライズ向け収益の内訳は非公開である。KIQ-OAI-001が要求する「政府vs民間内訳」は依然未達成である。

この不在が何を妨げているか。H-OAI-001の命題は「Agent機能でB2B支配的地位を確立する」である。収益の過半がConsumer（ChatGPT Plus等）の場合、B2B支配の収益的裏付けが質的に変質する。逆にEnterprise収益が過半の場合、コモディティ化圧力に対するB2B鞘の厚さを直接評価できる。収益内訳が公表されない限り、この判別が不可能であり、49%の上下いずれの変更も根拠不足となる。Arbiter v4.27の「核心パラメータ不在による確度変更保留」はこの構造を指す。

### 5%政府株式提案: 取引的関係の制度化

OpenAIは米国政府に5%株式をAlaska Permanent Fund型車両として提供する提案を行った（[INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) A-1）。Alaska Permanent Fundは石油収入を元に州民に配当を支払う州営企業であり、OpenAIはAI収益を元に国民に配当を支払う連邦版として構想した。他の米国AI企業にも同様の株式提供を提案したが、合意するかは不明である。Sam AltmanはTrump大統領・Lutnick商務長官・Bessent財務長官と協議した。

この提案は2つの含意を持つ。第一に、政治的障害を財務的関与でクリアする戦略である。連邦政府が既にIntel約10%・MP Materials 15%の株式を保有する前例がある。5%株式提供は、OpenAIが政府との協調関係を制度化する手段である。第二に、Anthropicとは対立的な理論に立つ。Anthropicは株式を政府に渡さず「digital dividend」（AIセクター税→国民配当）を提案した。株式か税制かは、政府-AI関係の根本的な設計選択である。

GPT-5.6（Sol/Terra/Luna）の広範リリース延期要請は、政府がリリース時期に介入する初の事例である（[INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) A-1）。政府協調プロセス（限定的信頼パートナー向けプレビューから開始）の延長線上に位置するが、5%株式提案との同時観測は、協調と従属の境界が曖昧化していることを示す。

### 構造的赤字とインフラ依存のリスク

OpenAIのH1 2025純損失は$13.5Bである（[INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) A-2）。収入$4.3Bに対して損失が3倍を超える。Arbiter v4.27はこれを一時的赤字ではなく「構造的赤字」と評価した。月次$2B収益の成長軌道が赤字をいつ吸収するかは、推論コスト低下（[INFO-038](../Information/2026-07-03/collected-raw.md#INFO-038) DeepSeek V4 API価格GPT-4oの10分の1）とインフラ投資規模に依存する。

Microsoftとの関係にも変化が生じている。Stargateプロジェクト（$500Bインフラ計画）でOracleをインフラパートナーとして追加したことで、Azureの排他的クラウド地位が低下した（[INFO-037](../Information/2026-07-03/collected-raw.md#INFO-037) B-1）。OpenAIはDirect Computeの比率を増加させ、Microsoft依存度を下げる方向にある。インフラ多角化は独立性を強化するが、同時にMicrosoftからの暗黙の補助（算入されている原油価格的支援）が縮小するリスクを伴う。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | OpenAI 5%政府株式提案: Alaska Permanent Fund型・Altman協議(Trump/Lutnick/Bessent) | [H-OAI-001](../config/hypotheses.json) 新次元。政治的障害の財務的解消。政府-AI関係の取引的構造化。[IND-030](../config/indicators.json) critical文脈 | A-1 | [INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) |
| 高 | GPT-5.6（Sol/Terra/Luna）広範リリース延期要請 by Trump政権 | [H-OAI-001](../config/hypotheses.json) C方向（政府協調）。リリース時期への政府介入初の事例。協調と従属の境界曖昧化 | A-1 | [INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) |
| 高 | 月次約$2B収益・年率$20-24B・H1 2025純損失$13.5B・構造的赤字 | [H-OAI-001](../config/hypotheses.json) 二面性。成長軌道と構造的赤字の同時存在。KIQ-OAI-001内訳非公開で評価保留 | A-2 | [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) |
| 高 | 選択的執行: GPT-5.5とFable 5/Mythos 5に同じ脆弱性だがOpenAI無措置 | [H-OAI-001](../config/hypotheses.json) C方向。順応のシールド効果構造化。[IND-030](../config/indicators.json) critical文脈 | B-2 | [INFO-030](../Information/2026-07-03/collected-raw.md#INFO-030) |
| 高 | Microsoft-OpenAI緊張: StargateでOracle追加・Direct Compute増・Azure排他性低下 | [H-OAI-001](../config/hypotheses.json) I方向の新次元。インフラ依存のリスク構造変化 | B-1 | [INFO-037](../Information/2026-07-03/collected-raw.md#INFO-037) |
| 高 | DeepSeek V4: GPT-4oレベル性能をAPI価格10分の1で提供・MIT OSS | [H-OAI-001](../config/hypotheses.json) I方向。コモディティ化の量的深化。コスト劣位の構造化 | A-2 | [INFO-038](../Information/2026-07-03/collected-raw.md#INFO-038) |
| 高 | コスト30x崩壊・MMLU全社>90%・GPQA同点・rank-2構造 | [H-OAI-001](../config/hypotheses.json) I方向。コモディティ化の経済的・技術的確認 | B-3 | [INFO-058](../Information/2026-07-03/collected-raw.md#INFO-058) |
| 中 | GPT-5.6 Sol Terminal-Bench 91.9%（Claude Mythos 5 84.3%を上回る） | [H-OAI-001](../config/hypotheses.json) C方向。技術優位の継続。だがA-3品質製品発表≠エンタープライズ採用（v4.26指摘） | A-3 | [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-OAI-001](../config/hypotheses.json) が45%を割る | 「B2B支配的地位確立」仮説が棄却水準に接近。medium→low帯移行 | 180日 | [H-OAI-001](../config/hypotheses.json) |
| KIQ-OAI-001が回答されAPI/Enterprise/Consumer収益内訳が公表される | 49%の凍結が解消し、B2B支配の収益的裏付けの質的評価が可能になる。核心パラメータ不在の制約が解除される | 90日 | [IND-027](../config/indicators.json) |
| 企業LLM支出シェアが20%を下回る | 「支配」の定義が成立しなくなる。27%から更に低下で構造的劣位確定 | 180日 | [IND-027](../config/indicators.json) |
| 5%政府株式提案が制度化され他社にも拡大する | 政府-AI関係の取引的構造が業界標準化。[IND-030](../config/indicators.json) criticalの新次元確定 | 180日 | [IND-030](../config/indicators.json) |
| 選択的執行が逆転しOpenAIにも同等の措置が発動される | コンプライアンス優位のC次元が消滅する。49%の均衡が崩れる | 365日 | [IND-030](../config/indicators.json) |
| IPOが更に延期または評価額が$500Bを下回る | 構造的成長の外部検証が失敗する。$13.5B赤字の吸収見通し恶化 | 365日 | [IND-029](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 49% medium | ±0%（v4.24で48→49%+1%後3R連続±0%）。根拠はC/I均衡ではなく核心パラメータ不在による確度変更保留（v4.27 Red表現修正採用）。月次$2B収益・5%政府株式提案・GPT-5.6延期要請・選択的執行シールドはC方向。$13.5B構造的赤字・DeepSeek V4コスト10分の1・コスト30x崩壊・MMLU収束はI方向。KIQ-OAI-001（収益内訳）不在が確度変更の制約。medium維持 | [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) [INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) | [INFO-038](../Information/2026-07-03/collected-raw.md#INFO-038) [INFO-058](../Information/2026-07-03/collected-raw.md#INFO-058) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放の上にプロプライエタリ上位レイヤーで围い込む | 44% low | ±0%。围い込み否定累積継続。Agent SDKプロバイダ非依存・30以上モデルサポート・排他性なし。low帯確定度増加 | (新規围い込み肯定Cなし) | [INFO-037](../Information/2026-07-03/collected-raw.md#INFO-037) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% low | ±0%。商業化規模（月次$2B収益・$20-24B年率・IPO準備・5%政府株式提案）圧倒的。AGI最優先支持A-2+証拠不在 | (該当なし) | [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) [INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントでcritical | 選択的執行でGPT-5.5脆弱性無措置。GPT-5.6 Sol最高安全性システム。新規A-2実被害なし。critical移行条件未到達。high/rising | 2026-07-03 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | GPT-5.6 Sol新SOTA・MMLU全社>90%・GPQA同点・rank-2構造・コスト30x崩壊・DeepSeek V4 API価格GPT-4oの10分の1（INFO-038 A-2）。コモディティ化圧力量的深化。elevated/stable | 2026-07-03 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | Gartner 89%パイロットスケールせず（INFO-032 A-1）・Forrester 55%後悔・Writer 97%展開/8%価値。期待-実態ギャップ構造的パターン結晶化。high/rising | 2026-07-03 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | MCP RC 2026-07-28・Agent SDKプロバイダ非依存・Google Interactions API GA・AWS AgentCore。標準化加速と围い込み否定の同時進行。high/rising | 2026-07-03 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | ARC-AGI-3公開（INFO-059 A-2）・Hassabis「AGI 50-50」（INFO-060 B-2）・DeepSeek V4 OSS性能向上。RSI具体化と客観ベンチマーク限界の同時進行。high/rising | 2026-07-03 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | 月次$2B収益（INFO-051 A-2）・$13.5B構造的赤字・Stargate $500B・生成AI支出$77B予測（INFO-054 B-1）。資本流入加速と赤字構造の同時存在。high/rising | 2026-07-03 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。5%政府株式提案（INFO-063 A-1）・GPT-5.6延期要請（INFO-063 A-1）・選択的執行（INFO-030 A-2）・Pentagon後継契約（INFO-030 A-2）・SCR完全因果チェーンでOpenAIが順応の受益者として位置づけ。DPA発動（INFO-031 A-2）。政府-AI取引的関係の制度化 | 2026-07-03 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-03 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% medium ±0%（v4.24で48→49%+1%後3R連続±0%）。根拠を「C/I均衡」から「核心パラメータ不在による確度変更保留」に修正（v4.27 Red表現修正採用）。5%政府株式提案（INFO-063 A-1）・GPT-5.6延期要請・月次$2B収益/$13.5B構造的赤字（INFO-051 A-2）・Microsoft緊張/Stargate Oracle追加（INFO-037 B-1）・DeepSeek V4 コスト10分の1（INFO-038 A-2）を反映。Arbiter v4.27 COMPLETE | [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) [INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) [INFO-037](../Information/2026-07-03/collected-raw.md#INFO-037) [INFO-038](../Information/2026-07-03/collected-raw.md#INFO-038) | H-OAI-001 48→49%（v4.24）・根拠修正（C/I均衡→核心パラメータ不在） |
| 2026-06-29 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 48% ±0%（コンプライアンス優位C vs コモディティ化I相殺）。Series H $65B/$965B・選択的執行の恩恵・Pentagon置換テスト・$25Bランレート/$14B赤字・コスト30x崩壊を反映 | [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) | H-OAI-001 48%（±0%） |
| 2026-06-27 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49→48%（-1%・ペナルティ機構再開） | [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) | H-OAI-001 49→48% |
| 2026-06-21 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% ±0%（ペナルティ停止）。[IND-030](../config/indicators.json) high→critical | [INFO-045](../Information/2026-06-21/collected-raw.md#INFO-045) | H-OAI-001 49%・IND-030 critical |
| 2026-06-12 | §0-§2・§4・§5全面書き直し。S-1提出・Phase 3宣言を反映 | 2026-06-12複数INFO | H-OAI-001 58→56% |

## 7. ブラインドスポット

- 収益内訳（API/Enterprise/Consumer・政府vs民間）が非公開（KIQ-OAI-001未回答）。月次$2Bの内訳が判明しない限り、49%の確度変更は根拠不足である。Arbiter v4.27が「核心パラメータ不在による確度変更保留」を正式根拠として採用したが、これは情報不足を認めることと同義である。
- 5%政府株式提案は他社にも拡大提案したが合意不明。OpenAI単独の取引か業界全体の枠組みかで、IND-030 criticalの含意が変わる。Alaska Permanent Fund型モデルが実現した場合、配当原資となるAI収益の持続性（$13.5B構造的赤字）が問われる。
- $13.5B純損失（H1 2025）と月次$2B収益の乖離がいつ解消するか不明。Arbiter v4.27は「構造的赤字」と評価したが、成長軌道が赤字を吸収する転換点の定量見積もりがない。Microsoftからの暗黙的補助が縮小する（Stargate Oracle追加・Direct Compute増）場合、赤字構造が悪化する可能性がある。
- Microsoft-OpenAI関係の変化がOpenAIの競争力にどう影響するかの評価がない。Azure排他性低下は独立性強化という正面解釈と、Microsoft支援縮小という裏面解釈が両立する。
- コモディティ化圧力（コスト30x崩壊・DeepSeek V4 API価格10分の1・MMLU収束・rank-2）がH-OAI-001のI方向にどれだけ寄与するかの定量評価がない。「性能差の縮小＝支配の低下」という因果仮定が検証されていない。
- 選択的執行（INFO-030）の持続性が不確定。政権変動・司法判断・Anthropic訴訟結果で逆転する可能性がある。GPT-5.5の同じ脆弱性が無措置である事実は、現時点ではC方向証拠だが、恒久的な構造ではなく政治的均衡の産物かもしれない。
- GPT-5.6延期要請と5%株式提案の同時観測は、政府協調の深化とも政府従属の深化とも読める。2つの解釈を区別する基準が不在である。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-037](../Information/2026-07-03/collected-raw.md#INFO-037) | Microsoft-OpenAI緊張: Stargate Oracle追加・Direct Compute増・Azure排他性低下(B-1) |
| [INFO-038](../Information/2026-07-03/collected-raw.md#INFO-038) | DeepSeek V4: GPT-4oレベル性能・API価格10分の1・MIT OSS(A-2) |
| [INFO-030](../Information/2026-07-03/collected-raw.md#INFO-030) | Pentagon-Anthropic-SCR完全因果チェーン: OpenAIが順応受益者(A-2) |
| [INFO-031](../Information/2026-07-03/collected-raw.md#INFO-031) | DPA発動・AI企業経済的圧力・表現ガバナンス(A-2) |
| [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) | OpenAI月次$2B収益・$13.5B純損失・5%政府株式提案(A-2) |
| [INFO-054](../Information/2026-07-03/collected-raw.md#INFO-054) | AI安全研究予算非公開・生成AI支出$77B・KIQ-GOV-002 25R未達成(B-1) |
| [INFO-058](../Information/2026-07-03/collected-raw.md#INFO-058) | AI変革で勝つ企業の条件・推論コスト2/3・モデルコモディティ化(B-2) |
| [INFO-059](../Information/2026-07-03/collected-raw.md#INFO-059) | ARC-AGI-3公開・RSI国家レベル安全保障リスク(A-2) |
| [INFO-060](../Information/2026-07-03/collected-raw.md#INFO-060) | Hassabis「AGI 50-50」・Davos 3CEO国家首脳級(B-2) |
| [INFO-063](../Information/2026-07-03/collected-raw.md#INFO-063) | OpenAI 5%政府株式提案・Alaska Fund型・GPT-5.6延期要請(A-1) |
| [INFO-032](../Information/2026-07-03/collected-raw.md#INFO-032) | Gartner: AIエージェントパイロット89%スケールせず(A-1) |
| [Arbiter v4.27](../state/arbiter-2026-07-03.md) | 確度評価の完全根拠 |
