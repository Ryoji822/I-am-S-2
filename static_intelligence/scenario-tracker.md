# シナリオ追跡 — 静的インテリジェンス

> 最終判断更新: 2026-05-19
> 全体確信度: 中
> 主参照: scenarios.json, indicators.json#IND-001/004/007/008/009/011/015/017/018/019/020/022/023/024/027

---

## 確率推移サマリ

過去20日の確率推移。主軸 4シナリオ + Black Swan 2件。

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|:-------:|:-------:|:-------:|:-------:|:------:|:------:|
| 2026-05-19 | 20% | 30% | 35% | 15% | 16% | 3% |
| 2026-05-18 | 20% | 30% | 35% | 15% | 16% | 3% |
| 2026-05-17 | 20% | 31% | 35% | 14% | 16% | 3% |
| 2026-05-16 | 20% | 32% | 35% | 14% | 16% | 3% |
| 2026-05-15 | 20% | 32% | 34% | 14% | 16% | 3% |
| 2026-05-14 | 20% | 33% | 34% | 14% | 16% | 3% |
| 2026-05-12 | 20% | 33% | 33% | 14% | 16% | 3% |
| 2026-05-11 | 20% | 34% | 32% | 14% | 16% | 3% |
| 2026-05-10 | 20% | 35% | 31% | 14% | 16% | 3% |
| 2026-05-09 | 20% | 36% | 30% | 14% | 16% | 3% |
| 2026-05-08 | 20% | 37% | 29% | 14% | 16% | 3% |
| 2026-05-06 | 20% | 38% | 28% | 14% | 16% | 3% |
| 2026-05-05 | 20% | 39% | 27% | 14% | 16% | 3% |
| 2026-05-04 | 20% | 40% | 26% | 14% | 16% | 3% |
| 2026-05-03 | 20% | 41% | 26% | 13% | 16% | 3% |
| 2026-05-02 | 20% | 42% | 25% | 13% | 16% | 3% |
| 2026-05-01 | 20% | 43% | 24% | 13% | 16% | 3% |
| 2026-04-30 | 20% | 43% | 24% | 13% | 16% | 3% |
| 2026-04-29 | 20% | 44% | 24% | 12% | 16% | 3% |
| 2026-04-28 | 21% | 42% | 25% | 12% | 16% | 3% |

過去20日の変動: SCN-002は44%(04-29)→30%(05-19)で-14pt。SCN-003は24%(04-29)→35%(05-19)で+11pt。SCN-001は21%(04-28)→20%(05-19)で-1pt。SCN-004は12%(04-28)→15%(05-19)で+3pt。SCN-002/003の差が5%(30% vs 35%)に拡大。QHG再定義が14R連続未実行。次回Arbiter最初の議題として強制実行。

---

## 2つの軸の意味

X軸(開放/閉鎖)は、AIの実行環境・データ・標準がどれだけ可搬かを問う。7サンドボックス統合 [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) や DeepSeek R2 OSS GPT-4oマッチ [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) は「開放」方向。Gemini Enterprise Agent Platform [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011) や Googlebook [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006) は「閉鎖」方向。Y軸(性能差広/縮)は、フロンティアモデルと後続モデルの能力差が顧客の意思決定を変えるほど大きいかを問う。DeepSeek R2 OSS GPT-4oマッチは現在「縮小」方向にある。

---

## SCN-001: 囲い込みの勝者 (現在確率: 20%)

> 象限: 閉鎖 × 性能差拡大

### §0 一文要約

1-2社が技術力で後続を引き離しつつ実行環境・データ・ガバナンスで囲い込む世界を指すが、現在確率は20%で3位。围い込み否定15件蓄積+OSS性能ギャップ消滅で技術独占と生態系封鎖の両条件が同時に欠けている [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031)。

### §1 コア判断

このシナリオは「技術独占と生態系封鎖が同時に起きる」という条件に依存する。現在、その両条件は欠けている。

技術側では、DeepSeek R2がOSSでGPT-4oの9ベンチマークにマッチした [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031)。「1-2社が圧倒」する性能差には達していない。封鎖側では、OpenAI Agents SDKが7つのホスト型サンドボックスプロバイダーと統合し [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009)、GPT-5.5がAWS Bedrockで利用可能になった [INFO-014](../Information/2026-05-19/collected-raw.md#INFO-014)。围い込み否定が15件に蓄積している。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | DeepSeek R2 OSS GPT-4oマッチ。V3.2 $0.27/M input | 技術独占の前提が崩れる最も具体的な観測 | C-2 | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) |
| 高 | 围い込み否定15件蓄積: 7サンドボックス+AWS Bedrock GPT-5.5+マルチクラウド | 封鎖の前提が崩れる構造的証拠 | A-3 | [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-014](../Information/2026-05-19/collected-raw.md#INFO-014) |
| 中 | Pentagon 7社契約(複数社分散) | 政府が独占ではなく分散を選んでいる | A-2 | [INFO-016](../Information/2026-05-19/collected-raw.md#INFO-016) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLM上位1社と2位以下の差が20pt以上に拡大 | 技術独占の前提が成立し始める | 90日 | [IND-001](../config/indicators.json) |
| 有力2社がクロスクラウド撤退し自社基盤のみに移行 | 相互依存構造が解体され封鎖化が進む | 180日 | [IND-018](../config/indicators.json) |
| 政府・規制当局がAI市場での独占を認める判断を下す | 競争法的制約が外れ围い込みに外部制動がなくなる | 180日 | [IND-023](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-001-A | フロンティア技術差が顧客ロックインの主因になる | 20% | DeepSeek R2 OSS GPT-4oマッチで技術差の診断的価値が低下。BenchLM上位差3-4ptは「意思決定を変える差」の閾値に届かず | (なし) | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) |
| H-SCN-001-B | 1-2社がエコシステムを垂直統合し他社の参入を封じる | 18% | 围い込み否定15件蓄積で封鎖の兆候がない | (なし) | [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-014](../Information/2026-05-19/collected-raw.md#INFO-014) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク非連続ジャンプ | +10pt以上/期で高 | OSS性能ギャップ消滅確定 | 2026-05-19 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | 7サンドボックス+Grok Build ACP+DeerFlow 2.0。high水準 | 2026-05-19 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-19 | 確率20%据え置き。全面更新(鮮度タイムアウト7日) | 围い込み否定15件+OSSギャップ消滅確定で両条件欠如継続 | 「围い込み困難化」→「围い込み困難化継続。技術独占・生態系封鎖ともに前提不成立」 |

### §7 ブラインドスポット

- 围い込み形態変化(技術的→契約的・エコシステム的)が起きている場合、技術指標(IND-001等)では捉えきれない。
- 中国市場(DeepSeek/ByteDance)での独占形成度は観測できていない。

---

## SCN-002: 技術は開く但勝者は出る (現在確率: 30%)

> 象限: 開放 × 性能差拡大

### §0 一文要約

AAIF/MCP等の相互運用標準で移行の自由度は確保されるが、フロンティア性能はTier 1に集中する構造を指す。現在30%で2位。QHG凍結14R目。DeepSeek R2 OSS GPT-4oマッチで「格差拡大」前提が17R連続で弱体化し、Arbiter推奨-2%だが凍結中。QHG再定義14R目必須。

### §1 コア判断

「開放されているが勝者がいる」という世界は、標準化が進む一方で性能差が維持される場合に成立する。現在の観測は開放側を強く支持するが、性能差側の根拠が消滅に近い。

7サンドボックス統合+AWS Bedrock GPT-5.5 [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-014](../Information/2026-05-19/collected-raw.md#INFO-014) は開放方向の構造証拠だ。しかしDeepSeek R2がOSSでGPT-4oの9ベンチマークにマッチし [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031)、「格差拡大」前提を直接弱体化する。17R連続の収束方向はこのシナリオの前提と整合していない。

QHG再定義が14R連続で未実行であり、Arbiter推奨は-2%(30→28%)だが凍結中。次回Arbiter最初の議題として強制実行される。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | DeepSeek R2 OSS GPT-4oマッチ+V3.2 $0.27/M input | 「格差拡大」前提を直接弱体化する最も強い証拠 | C-2 | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) |
| 高 | 7サンドボックス+AWS Bedrock GPT-5.5+マルチクラウド | 開放軸を支える構造証拠 | A-3 | [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-014](../Information/2026-05-19/collected-raw.md#INFO-014) |
| 高 | QHG凍結14R。Arbiter推奨-2%(30→28%) | 格差拡大前提17R連続弱体化が決定的。確率体系妥当性に疑義 | B-3 | scenarios.json |
| 中 | Mistral $2.3B調達・open weights戦略継続 | 開放方向の追加証拠 | B-3 | [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| QHG象限再検討でSCN-002/003が統合または再区分される | 確率推移の連続性が失われる | 30日 | scenarios.json |
| OSS(Mistral/DeepSeek)のエンタープライス採用が3社で10%以上のシェアを取る | 「勝者集中」前提が崩れSCN-004が上昇する | 90日 | [IND-004](../config/indicators.json) |
| BenchLM上位3社差が3pt以内に収束する | 「勝者格差」の根拠が消え、SCN-004方向の根拠が立つ | 90日 | [IND-001](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-002-A | AAIF/MCP標準でAI間相互運用が確立する | 58% | 7サンドボックス+AWS Bedrock GPT-5.5+Grok Build ACPはgenuine C | [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-19/collected-raw.md#INFO-010) | (標準競合の可能性) |
| H-SCN-002-B | Tier 1の3社がフロンティア性能を維持し続ける | 35% | DeepSeek R2 OSS GPT-4oマッチで維持の根拠が急速に弱まっている。BenchLM上位差3-4ptは残るが診断的価値低下 | (BenchLM上位差残存) | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で高 | OSS性能ギャップ消滅確定 | 2026-05-19 |
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用10%超で高 | DeepSeek R2 OSS GPT-4oマッチ [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) | 2026-05-19 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | 7サンドボックス+Grok Build ACP+DeerFlow 2.0。high水準 | 2026-05-19 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-19 | 確率30%据え置き(QHG凍結)。全面更新(鮮度タイムアウト7日)。Arbiter推奨-2% | DeepSeek R2 OSS GPT-4oマッチ+围い込み否定15件で格差拡大前提17R連続弱体化が決定的 | 「QHG凍結13R」→「QHG凍結14R。Arbiter推奨-2%だが凍結。次回強制実行」 |

### §7 ブラインドスポット

- QHG象限の区別能力が低下している可能性。SCN-002/003の差が5%に拡大したが、QHG軸の区別能力は消失している。14R連続で未実行。
- 「開放」の観測が標準化に集中しているが、围い込み形態変化(技術的→契約的)を観測する指標が不十分。
- 政府市場(Pentagon)の調達判断が民間市場の「開放」動向に及ぼす影響を定量化していない。

---

## SCN-003: 静かな囲い込み (現在確率: 35%)

> 象限: 閉鎖 × 性能差収斂

### §0 一文要約

モデル性能差は小さくなるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界を指す。現在35%で最高確率。围い込み14件蓄積+開放C 14R不在+OSSギャップ消滅確定。QHG凍結14R目。

### §1 コア判断

このシナリオの構造は「性能差が消えても離れられない」という顧客固定化にある。現在の観測はその方向に強く動いている。

収斂側の証拠は確定的だ。DeepSeek R2がOSSでGPT-4oにマッチし [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031)、V3.2-SpecialeがIMO/IOIで金レベルを達成した。围い込み側も14件蓄積: Gemini Enterprise Agent Platform [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011)、Googlebook [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006)、AI pointer [INFO-005](../Information/2026-05-19/collected-raw.md#INFO-005)、Codex Dell提携 [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004)、DeerFlow 2.0 WeChat/Feishu/DingTalk統合 [INFO-008](../Information/2026-05-19/collected-raw.md#INFO-008)、Mistral $2.3B open weights [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033) 等。

モデル性能差の差別化価値が低下すれば、エコシステム围い込みの重要性が相対的に増すという構造的論理が強化されている。開放的なプロトコル(MCP/ACP)が相互運用を可能にしながらも、SaaSワークフロー統合の深さが移行コストを決める「開放的な見た目の閉鎖」が同時に成立する。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | DeepSeek R2 OSS GPT-4oマッチ+V3.2 Speciale金レベル | 収斂軸を支える最も強い証拠 | C-2 | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) |
| 高 | 围い込み14件蓄積: Gemini Enterprise+Googlebook+AI pointer+Codex Dell+DeerFlow+Mistral open weights等 | 围い込みが配布・エコシステム・データ・ハードウェアの多次元で同時進行 | A-3 | [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011) [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006) [INFO-005](../Information/2026-05-19/collected-raw.md#INFO-005) |
| 高 | 開放C 14R連続不在 | 围い込みの非対称性が構造的に拡大 | A-3 | scenarios.json |
| 中 | 7サンドボックス+Grok Build ACP+DeerFlow 2.0 | 開放プロトコルは進展するが、エコシステム深度の差は埋まらない | A-3 | [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-19/collected-raw.md#INFO-010) |
| 中 | $1TNデータセンター投資+米国680施設 | 資本集中が围い込みの物理的基盤を強化 | B-2 | [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| QHG象限再検討でSCN-002/003が統合または再区分される | 確率推移の連続性が失われる | 30日 | scenarios.json |
| 主要企業がMCP上でクロスベンダー切り替えを実証する事例が3件以上公表される | スイッチングコストが低いことが実証され、固定化シナリオへの根拠が薄まる | 90日 | [IND-017](../config/indicators.json) |
| 围い込みシグナル14件のうち4件以上が逆転する | 围い込みの構造的蓄積が止まり、確率上昇が止まる | 60日 | [IND-009](../config/indicators.json) [IND-022](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-003-A | モデル性能収斂でベンダー差別化は機能から围い込みに移行する | 55% | DeepSeek R2 OSS GPT-4oマッチは収斂の確定的証拠。围い込み14件蓄積。「開放的な見た目の閉鎖」が成立するかは未実証 | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011) | [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-19/collected-raw.md#INFO-010) |
| H-SCN-003-B | エコシステム統合深度が顧客の移行コストを決定する | 48% | Googlebook+Gemini Enterprise+Codex Dellの围い込み蓄積は理論的C。実際の移行実績は未観測 | [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006) [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004) | (クロスベンダー移行事例不在) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-009](../config/indicators.json) | AI利用規約の制限強化 | 月3件超の制限追加で高 | 围い込み14件蓄積+開放C 14R不在 | 2026-05-19 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | OSS gap 3%以内で高 | DeepSeek R2 OSS GPT-4oマッチで消滅確定 | 2026-05-19 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全社採用で高(反証指標) | 7サンドボックス+Grok Build ACP+DeerFlow 2.0。high水準 | 2026-05-19 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-19 | 確率35%据え置き(QHG凍結)。全面更新(鮮度タイムアウト7日)。Arbiter推奨+1% | 围い込み14件蓄積+OSSギャップ消滅確定+性能差価値低下。Arbiter推奨+1%だが凍結 | 「QHG凍結13R」→「QHG凍結14R。围い込み14件。Arbiter推奨+1%だが凍結。次回強制実行」 |

### §7 ブラインドスポット

- QHG象限の区別能力が低下している。SCN-002/003の差が5%に拡大したが、QHG軸の区別能力は消失している。14R連続で未実行。次回Arbiterでの再定義が必須(強制実行対象)。
- 「スイッチングコストが高い」という観測が、実際に顧客が離れられないことの実証ではない。
- 「静かな围い込み」が起きているとすれば顧客はそれを認識していないはずで、認識していない事象をシグナルとして観測することは構造的に困難だ。

---

## SCN-004: 誰でもAI (現在確率: 15%)

> 象限: 開放 × 性能差収斂

### §0 一文要約

性能差がなくなりオープン標準で自由に行き来できる世界を指す。現在15%で4位。DeepSeek R2 OSS GPT-4oマッチ [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) + Mistral $2.3B [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033) は収斂方向の強いシグナルだが、$1TN CAPEX [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) の資本集中が二層市場構造を維持している。

### §1 コア判断

SCN-004は「モデルがコモディティ化し、価格も移行コストも消える」という条件が揃う場合に成立する。収斂方向の証拠は史上最強だ。DeepSeek R2 OSS GPT-4oマッチ、V3.2 $0.27/M input、Mistral $2.3B open weightsは下層の適合性を高める。

ただし$1TN CAPEX過剰投資と米国680データセンター計画 [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) は、インフラ集中で二層市場構造が継続することを示す。Arbiter推奨+1%(15→16%)だが凍結中。SCN-004は下層のみ部分的に成立するにとどまる。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | DeepSeek R2 OSS GPT-4oマッチ+V3.2 $0.27/M input | コモディティ化の最も直接的な証拠 | C-2 | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) |
| 高 | $1TNデータセンター投資+米国680施設+IPO $8,520億 | 資本集中が二層市場構造を維持 | B-2 | [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) [INFO-024](../Information/2026-05-19/collected-raw.md#INFO-024) |
| 中 | Mistral $2.3B調達・open weights戦略 | 下層の適合性を高める | B-3 | [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLMの全層間差が5pt以内に収束する | フロンティアの優位性が消えSCN-004が現実的な主シナリオになる | 180日 | [IND-001](../config/indicators.json) |
| OSSモデルのエンタープライス採用シェアが20%を超える | 二層市場の下層だけでなく上層も侵食が起きたとみなせる | 180日 | [IND-004](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-004-A | OSSモデルがエンタープライスの主流になる | 18% | DeepSeek R2 OSS GPT-4oマッチは能力面の証拠だが、エンタープライス実採用のデータがなく確度が低い | [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) | [IND-029](../config/indicators.json) 資本集中 |
| H-SCN-004-B | オープン標準でAIプロバイダー間の移行がほぼコストゼロになる | 24% | 7サンドボックス+AWS Bedrock GPT-5.5は基盤だが、ワークフロー統合深度が移行コストを左右する | [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) [INFO-014](../Information/2026-05-19/collected-raw.md#INFO-014) | 围い込み14件蓄積 |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用20%超で高 | DeepSeek R2 OSS GPT-4oマッチ(能力)。採用率は別途 | 2026-05-19 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | OSS gap 3%以内で高 | DeepSeek R2 GPT-4oマッチで消滅確定 | 2026-05-19 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-19 | 確率15%据え置き(QHG凍結)。全面更新(鮮度タイムアウト7日)。Arbiter推奨+1% | DeepSeek R2 OSS GPT-4oマッチ+Mistral $2.3BはC。$1TN CAPEXはI。Arbiter推奨+1%だが凍結 | 「下層のみ部分的適合」→「OSSギャップ消滅確定だが$1TN資本集中が天井。Arbiter推奨+1%だが凍結」 |

### §7 ブラインドスポット

- 二層市場(大規模フロンティアユーザーと中小企業のOSSユーザー)が分離した形でSCN-004とSCN-002が共存するシナリオを、単一の確率に集約していることで精度が落ちている。
- 中国市場でのOSSダイナミクス(DeepSeek等)が西側市場に与えるコモディティ圧力を観測できていない。

---

## ブラックスワン: BS-001 AI安全性大事故 (現在確率: 16%)

> 低確率・高影響

### §0 一文要約

AIエージェントの本番障害・大規模セキュリティ事故が複合的に起き、業界全体に規制強化と信頼失墜をもたらす事象を指す。現在16%。MCP token theft+TanStack npm攻撃+AgentTrap 141タスク [INFO-017](../Information/2026-05-19/collected-raw.md#INFO-017) で攻撃面拡大が加速している。新規大規模実被害のA-2+報告なし。

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| AIエージェントによる金融・インフラへの大規模実害インシデントが公表される | 確率が急上昇し、全シナリオの再評価が必要になる | 常時 | [IND-013](../config/indicators.json) |
| 主要国でAIエージェントの本番使用を一時停止させる行政命令が出る | 業界構造が短期に変わり、SCN-001〜004の全確率に波及する | 90日 | [IND-030](../config/indicators.json) |

### §7 ブラインドスポット

- IND-030 high移行で能力-リスク二面性が新段階に到達したが、大事故への直接的連鎖は不確定。
- 大事故が起きたとき、どのシナリオに収束するかの分析を持っていない。

---

## ブラックスワン: BS-002 量子×AI融合 (現在確率: 3%)

> 低確率・根本的変化

### §0 一文要約

量子コンピューティングとAIの融合が既存の計算パラダイムを変える根本的変化を指す。現在3%。関連する新情報なし。

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| 量子プロセッサを使ったLLM推論がクラシカル計算比で10倍以上の速度を実証する | 確率が段階的に上昇し、全シナリオの前提が再評価される | 常時 | (新規IND要) |

### §7 ブラインドスポット

- 量子×AIの進捗を追う指標がない。新規IND設定が要る。
- 3%という確率の根拠が弱い(「関連情報なし」は「確率ゼロに近い」とは異なる)。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-031](../Information/2026-05-19/collected-raw.md#INFO-031) | DeepSeek R2 OSS GPT-4oマッチ・V3.2 Speciale金レベル(SCN-002/003/004根拠) |
| [INFO-009](../Information/2026-05-19/collected-raw.md#INFO-009) | OpenAI Agents SDK 7サンドボックス統合(開放C) |
| [INFO-011](../Information/2026-05-19/collected-raw.md#INFO-011) | Gemini Enterprise Agent Platform(围い込みC) |
| [INFO-006](../Information/2026-05-19/collected-raw.md#INFO-006) | Googlebook(围い込みC) |
| [INFO-005](../Information/2026-05-19/collected-raw.md#INFO-005) | AI搭載マウスポインタ(围い込みC) |
| [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004) | Codex + Dell提携(围い込みC) |
| [INFO-008](../Information/2026-05-19/collected-raw.md#INFO-008) | DeerFlow 2.0 68K stars(围い込みC+開放C) |
| [INFO-010](../Information/2026-05-19/collected-raw.md#INFO-010) | Grok Build ACP(開放C) |
| [INFO-014](../Information/2026-05-19/collected-raw.md#INFO-014) | AWS Bedrock GPT-5.5(開放C) |
| [INFO-026](../Information/2026-05-19/collected-raw.md#INFO-026) | $1TNデータセンター投資(資本集中I) |
| [INFO-033](../Information/2026-05-19/collected-raw.md#INFO-033) | Mistral $2.3B調達(開放C) |
| [INFO-016](../Information/2026-05-19/collected-raw.md#INFO-016) | Pentagon報酬構造(分散C) |
| [INFO-017](../Information/2026-05-19/collected-raw.md#INFO-017) | AgentTrap 141タスク(BS-001根拠) |
| [Arbiter v3.82](../state/arbiter-2026-05-19.md) | 確度評価の完全根拠(付録のみ参照) |
