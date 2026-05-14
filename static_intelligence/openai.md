# OpenAI

> 最終判断更新: 2026-05-14
> 全体確信度: 中
> 主参照: hypotheses.json#H-OAI-001/002/003, indicators.json#IND-001/IND-013/IND-026/IND-027/IND-029

## 0. 一文要約

我々はOpenAIを、**製品ポートフォリオの大胆な整理(ファインチューニングAPI縮小・Sora 2終了)と音声3モデル新規展開を同時に進めながら、DeployCo($40億+)でエンタープライズ展開インフラの支配を狙う企業**と読んでいる。最大の根拠は、製品の刈り取りと新規投入が並走する点にあり、これは資源集中の意思決定速度が市場予想を上回っていることを示唆する [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005)。ただしファインチューニングAPI縮小が開発者コミュニティの反発を招いており [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043)、Sora 2終了の計算資源ロボティクス転用が実効性を持つかは未検証である。DeployCoのFDE常駐モデルが12ヶ月以内に解約か縮小に至る、または開発者離反がAPI収益の5%以上に影響する、のいずれかが観測されたら、この読みは変わる。

## 1. コア判断

OpenAIの戦略が二つの相反する動きの同時実行という新しい段階に入った。一方で製品の大胆な整理断行、他方で新領域への集中的投入である。

ファインチューニングAPIの段階的縮小は [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043)、開発者コミュニティから強い反発を受けている。価格改定(GPT-5 Pro $15/$120 per 1M tokens)も同時に発表され、開発者エコシステムとの関係悪化リスクが具体的になった。Sora 2の終了と計算資源のロボティクス転用 [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) は、映像生成市場からの撤退を意味する。これら「刈り取り」の一方で、GPT-Realtime-2($32/$64 per 1M audio tokens)とGPT-Realtime-Translate(70+入力言語→13出力言語、$0.034/min)とGPT-Realtime-Whisper($0.017/min)の3モデルを同時投入した [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005)。コンテキスト32K→128Kへの拡張も含めて音声AI市場への本格参入を示す。

DeployCoは引き続き中核的戦略的位置にある。TPG主導、Advent/Bain Capital/Brookfield共同主導で$40億以上の初期投資を集め、Tomoro買収で約150名のFDEを獲得した [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004)。McKinsey & Company、Bain & Companyなど19社のパートナーが参加する。CodexのWindowsサンドボックス実装は [INFO-001](../Information/2026-05-14/collected-raw.md#INFO-001) SID + write-restricted token + firewall rulesによる昇格サンドボックスで、4層セキュリティ(サンドボックス・承認ポリシー・ネットワークプロキシ・agent-nativeテレメトリー)を構成する [INFO-002](../Information/2026-05-14/collected-raw.md#INFO-002)。低リスク操作の自動レビューモードも導入され、エンタープライズ導入の摩擦低減を図る。

GPT-5.5-Cyberは [INFO-006](../Information/2026-05-14/collected-raw.md#INFO-006) 限定プレビュー段階で、Cisco/Intel/SentinelOne/Snykがパートナーとして参加する。3段階アクセスレベル(GPT-5.5→GPT-5.5+TAC→GPT-5.5-Cyber)は機関別セキュリティ要件に応じた差別化を示す。ChatGPT広告は英国・メキシコ・ブラジルに加え日本・韓国へ展開を拡大し、Free/Go層のみを対象とする [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008)。

確証バイアス警告が3R連続で発出されている。Blueが各ラウンドの新証拠を常に「最も強力なC」と評価するパターンが3期連続で継続しており、H-OAI-001の63%が過大評価されている可能性が増している。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | DeployCo設立: $40億+初期投資・Tomoro買収・19パートナー・FDE常駐モデル | API提供から展開サービス会社への戦略的飛躍。競争軸の転換可能性 | A-3 | [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004) |
| 高 | ファインチューニングAPI段階的縮小 + 開発者価格改定(GPT-5 Pro $15/$120) | 開発者エコシステムとの関係悪化リスク。H-OAI-002围い込みの逆効果 | B-3 | [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) |
| 高 | Sora 2終了・計算資源ロボティクス転用 | 映像生成市場撤退。資源集中の意思決定速度 | A-3 | [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) |
| 高 | GPT-Realtime 3モデル同時投入(Realtime-2/Translate/Whisper)・コンテキスト128K | 音声AI市場への本格参入。新収益柱の構築 | A-3 | [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) |
| 高 | Codex Windowsサンドボックス(4層セキュリティ)・自動レビューモード | エンタープライズ導入摩擦の低減。H-OAI-001のC | A-3 | [INFO-001](../Information/2026-05-14/collected-raw.md#INFO-001) [INFO-002](../Information/2026-05-14/collected-raw.md#INFO-002) |
| 中 | GPT-5.5-Cyber限定プレビュー・TAC・Cisco/Intel/SentinelOne/Snyk | 政府・金融市場参入基盤。セキュリティ要件への差別化 | A-3 | [INFO-006](../Information/2026-05-14/collected-raw.md#INFO-006) |
| 中 | ChatGPT広告日本・韓国展開(Free/Go層) | 収益多様化の継続。消費者層の貨幣化 | A-3 | [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DeployCoのFDE常駐モデルが12ヶ月以内に解約または大幅縮小に至る | 「展開能力が競争軸になる」という読みとH-OAI-001の根拠が崩れる | 365日 | [IND-029](../config/indicators.json) |
| ファインチューニングAPI縮小による開発者離反がAPI収益の5%以上に影響する | H-OAI-002围い込み戦略の限界が露呈し、下層開放圧力が上層围い込みを無効化する | 180日 | [IND-027](../config/indicators.json) |
| $14B損失が2026・2027と連続し、Altman or SoftBankが損失許容の打ち止めを示唆 | 赤字走行のコア判断が崩れ、リストラ/縮小フェーズへの移行が現実化する | 180日 | [IND-029](../config/indicators.json) |
| LLM支出シェアが27%から20%以下に下落(Anthropic・Google双方に侵食) | H-OAI-001(エンタープライズ支配的地位の確立)が棄却水準に達する | 90日 | [IND-026](../config/indicators.json) |
| Sora 2終了後のロボティクス転用が6ヶ月以内に具体的成果を出さない | 資源集中の意思決定が撤退でなく単なる縮小だった可能性が高まる | 180日 | [IND-001](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 63% | DeployCo $40億+・Codex 4M WAU・FedRAMP・GPT-5.5-CyberでC蓄積。$14B損失とLLMシェア27%が同数I。確証バイアス警告3R連続発出。Blueの「最も強力なC」反復パターンは確証バイアス指標 | [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004) [INFO-001](../Information/2026-05-14/collected-raw.md#INFO-001) [INFO-006](../Information/2026-05-14/collected-raw.md#INFO-006) | [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放エコシステム上にプロプライエタリ上位レイヤーを構築する | 49% | Skills/Shell/Compaction围い込みはC。MCP de facto 7x I蓄積。Codex独自サンドボックスはCだが下層開放圧力が上層围い込みの有効性を構造的に制約。49%はlow帯域 | [INFO-001](../Information/2026-05-14/collected-raw.md#INFO-001) [INFO-002](../Information/2026-05-14/collected-raw.md#INFO-002) | [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% | 「棄却確定」から「確度極低」に修正。非営利支配構造で商業収益の研究還流を制度的保証。DeployCo収益のAGI再投資はC。商業化規模・速度が研究出力を凌駕する事実はI | [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004) | [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能の非連続ジャンプ | +5pt以上/期で high | BenchLM 92(3位)。ARC-AGI-2 83.3%。Terminal-Bench 82.7% | 2026-05-14 |
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントで critical | Codex 4層防御で防御強化継続。新たな脆弱性なし。high水準 | 2026-05-14 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | CEO 83%導入予定 vs CIO 25%監視可能。期待-実態ギャップ拡大。elevated水準 | 2026-05-14 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用で high | DeployCo 19パートナー + Azure排他性終了 + provider-agnostic SDK。標準化加速。high水準 | 2026-05-14 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限り high | DeployCo $40億+ + $122B調達 + $100B JV + VC $2,672B Q1 2026。資本流入加速。high水準 | 2026-05-14 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-14 | ファインチューニングAPI縮小・Sora 2終了・GPT-Realtime 3モデル・ChatGPT広告日本展開を反映して全面書き直し | [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) | 「DeployCoで展開インフラ支配に飛躍」→「製品ポートフォリオ整理(FT API縮小+Sora 2終了)と音声3モデル新規展開が同時進行。H-OAI-002 49%low帯」 |
| 2026-05-12 | DeployCo + GPT-5.5-Cyber + Trusted Contact + H-OAI-003「棄却確定」→「確度極低」を反映して全面書き直し | [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) [INFO-002](../Information/2026-05-12/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-12/collected-raw.md#INFO-003) | 「損失走行継続中。二重JVで金融次元二重化」 → 「DeployCoで展開インフラ支配に飛躍。確証バイアス警告2R連続。H-OAI-003撤回」 |
| 2026-05-11 | §4 §5 更新(H-OAI-002 50%・IND値最新化) | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) | H-OAI-002 53→50%・IND-027 high水準反映 |
| 2026-05-08 | GPT-5.5 Instant/Cyber/Realtime-2 + $100B JV + FedRAMP + 広告 + 価格2倍 | 複数INFO | 「評価額で損失を走らせる企業」 → 「損失走行継続。二重JVで金融次元二重化」 |
| 2026-05-06 | コア判断を「エンタープライズ開発プラットフォーム化」から「赤字走行の賭け」へ | $14B損失 + JV + BenchLM 3位の同時観測 | 「全クラウド展開でエンタープライズを取る」 → 「評価額で損失を走らせながら市場支配を狙う」 |

## 7. ブラインドスポット

- DeployCo $40億+の実質額(コミットメント vs 実調達)と19パートナーの排他性が未確認。全証拠がA-3(公式発表)でB-tier以上の独立確認が0件。公式発表だけで「構造的転換」を評価する分析方法論的限界を認識している。
- ファインチューニングAPI縮小の開発者離反インパクトが定量把握できない。API収益に占めるファインチューニング利用の割合が非公表であり、反発が一時的か構造的かの判別ができない。
- Sora 2終了後のロボティクス転用がどの程度の計算資源を確保できるか不明。ロボティクス分野でのOpenAIの競争力も未検証。
- Codex WAUの収益転換率が非公表。400万WAUが月次ARRにいくら寄与しているかを外部から追跡できない。DeployCoのFDE常駐モデルがCodex WAUとどう関係するかも不明。
- 確証バイアス警告が3R連続で発出されている。各ラウンドの新証拠が常に「最も強力なC」と評価される構造自体が確証バイアスの指標であり、H-OAI-001の63%が過大評価されている可能性が高い。
- ChatGPT広告の日本・韓国展開による収益寄与が予測不能。Free/Go層のみ対象でARPUが低く、広告単価の市場別差異も不明。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-05-14/collected-raw.md#INFO-001) | Codex Windowsサンドボックス(SID + write-restricted token + firewall rules) |
| [INFO-002](../Information/2026-05-14/collected-raw.md#INFO-002) | Codex 4層セキュリティ(サンドボックス・承認ポリシー・ネットワークプロキシ・テレメトリー) |
| [INFO-003](../Information/2026-05-14/collected-raw.md#INFO-003) | Parameter Golf Challenge(1000+参加者・Codexトリアージボット) |
| [INFO-004](../Information/2026-05-14/collected-raw.md#INFO-004) | DeployCo設立($40億+・Tomoro買収・19パートナー・FDEモデル) |
| [INFO-005](../Information/2026-05-14/collected-raw.md#INFO-005) | GPT-Realtime-2/Translate/Whisper 3モデル(コンテキスト128K) |
| [INFO-006](../Information/2026-05-14/collected-raw.md#INFO-006) | GPT-5.5-Cyber限定プレビュー(TAC・Cisco/Intel/SentinelOne/Snyk) |
| [INFO-008](../Information/2026-05-14/collected-raw.md#INFO-008) | ChatGPT広告英国・メキシコ・ブラジル・日本・韓国展開 |
| [INFO-009](../Information/2026-05-14/collected-raw.md#INFO-009) | WebSocket execution mode for Responses API |
| [INFO-023](../Information/2026-05-14/collected-raw.md#INFO-023) | Sora 2終了・計算資源ロボティクス転用 |
| [INFO-043](../Information/2026-05-14/collected-raw.md#INFO-043) | ファインチューニングAPI縮小・開発者価格改定・GPT-5 Pro $15/$120 |
