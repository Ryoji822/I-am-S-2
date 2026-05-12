# シナリオ追跡 — 静的インテリジェンス

> 最終判断更新: 2026-05-12
> 全体確信度: 中
> 主参照: scenarios.json, indicators.json#IND-001/004/007/008/009/011/015/017/018/019/020/022/023/024/027

---

## 確率推移サマリ

過去20日の確率推移。主軸 4シナリオ + Black Swan 2件。

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|:-------:|:-------:|:-------:|:-------:|:------:|:------:|
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
| 2026-04-27 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-26 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-25 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-24 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-23 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-22 | 23% | 40% | 25% | 12% | 16% | 3% |
| 2026-04-17 | 24% | 37% | 27% | 12% | 16% | 3% |

過去20日の変動: SCN-002は44%(04-29)→33%(05-12)で-11pt。SCN-003は24%(04-29)→33%(05-12)で+9pt。SCN-001は24%(04-17)→20%(05-12)で-4pt。SCN-004は12%(04-13)→14%(05-12)で+2pt。SCN-002/003が33%同率(0%差)でQHG軸区別能力消失確定。10R連続同一方向シフトを記録。QHG再定義が次回Arbiter最優先必須条件。

---

## 2つの軸の意味

X軸(開放/閉鎖)は、AIの実行環境・データ・標準がどれだけ可搬かを問う。Azure排他性終了 [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) や OpenAI SDK provider-agnostic [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) は「開放」方向。Gemini Enterprise統合スタック [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) や Doubao有料化エコシステム [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009) は「閉鎖」方向。Y軸(性能差広/縮)は、フロンティアモデルと後続モデルの能力差が顧客の意思決定を変えるほど大きいかを問う。OSS/クローズド性能ギャップほぼ消滅 [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) は現在「縮小」方向にある。

---

## SCN-001: 囲い込みの勝者 (現在確率: 20%)

> 象限: 閉鎖 × 性能差拡大

### §0 一文要約

1-2社が技術力で後続を引き離しつつ実行環境・データ・ガバナンスで囲い込む世界を指すが、現在確率は20%で3位。Azure排他性終了+OpenAI SDK provider-agnostic+157K OpenCode移行の6重I蓄積で围い込み困難化が観測されている [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015)。

### §1 コア判断

このシナリオは「技術独占と生態系封鎖が同時に起きる」という条件に依存する。現在、その両条件は欠けている。

技術側では、OSS/クローズド性能ギャップがほぼ消滅した [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037)。「1-2社が圧倒」する性能差には達していない。封鎖側では、Azure排他性が終了しGPT-5.5がAWS Bedrockで即座に利用開始された [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003)。Gemini Enterprise統合スタック [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) は围い込み方向だが、围い込み形態が技術的から契約的・エコシステム的へ変化している可能性がある。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | Azure排他性終了+GPT-5.5 on AWS Bedrock | 封鎖の前提が崩れる最も具体的な観測 | B-2 | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) |
| 高 | OSS/クローズド性能ギャップほぼ消滅 | 技術独占に必要な差が存在しない | C-3 | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) |
| 中 | 157K開発者OpenCode移行 | モデル非依存ツールへの需要が围い込みに対抗 | C-3 | [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) |
| 中 | Pentagon 7社契約(複数社分散) | 政府が独占ではなく分散を選んでいる | A-2 | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLM上位1社と2位以下の差が20pt以上に拡大 | 技術独占の前提が成立し始める | 90日 | [IND-001](../config/indicators.json) |
| 有力2社がクロスクラウド撤退し自社基盤のみに移行 | 相互依存構造が解体され封鎖化が進む | 180日 | [IND-018](../config/indicators.json) |
| 政府・規制当局がAI市場での独占を認める判断を下す | 競争法的制約が外れ围い込みに外部制動がなくなる | 180日 | [IND-023](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-001-A | フロンティア技術差が顧客ロックインの主因になる | 20% | OSS/クローズドギャップ消滅で技術差の診断的価値が低下。BenchLM上位差6-7ptは「意思決定を変える差」の閾値に届かず | (なし) | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) |
| H-SCN-001-B | 1-2社がエコシステムを垂直統合し他社の参入を封じる | 18% | 6重I蓄積(Azure終了+provider-agnostic+OpenCode等)で封鎖の兆候がない | (なし) | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク非連続ジャンプ | +10pt以上/期で高 | OSS/クローズドギャップほぼ消滅 | 2026-05-12 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | Azure排他性終了+provider-agnostic SDK+OpenCode移行。high水準 | 2026-05-12 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-11 | 確率 20%据え置き | 6重I蓄積(Azure終了+provider-agnostic+OpenCode等)で围い込み困難化。Gemini Enterprise围い込みはC。相殺 | 「围い込みI蓄積中」→「围い込み困難化のI蓄積が優勢。Gemini围い込みはCだが非独占的」 |
| 2026-05-06 | 確率 22%→20% | MCP全社対応と7社Pentagon契約で封鎖・独占の前提が弱まった | 「3位維持」→「JVで围い込みシグナルはあるが非独占的」 |

### §7 ブラインドスポット

- 围い込み形態変化(技術的→契約的・エコシステム的)が起きている場合、技術指標(IND-001等)では捉えきれない。
- 中国市場(DeepSeek/ByteDance)での独占形成度は観測できていない。米国市場の判断が中国市場に適用できるかは不明。

---

## SCN-002: 技術は開く但勝者は出る (現在確率: 33%)

> 象限: 開放 × 性能差拡大

### §0 一文要約

AAIF/MCP等の相互運用標準で移行の自由度は確保されるが、フロンティア性能はTier 1に集中する構造を指す。現在33%でSCN-003と同率。直近10ラウンドで-1pt/ラウンドのペースで低下。QHG軸の区別能力が消失し、再定義が必須。

### §1 コア判断

「開放されているが勝者がいる」という世界は、標準化が進む一方で性能差が維持される場合に成立する。現在の観測は開放側を強く支持するが、性能差側の根拠が薄れている。

Azure排他性終了+OpenAI SDK provider-agnostic+157K OpenCode移行 [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) は開放方向の構造証拠だ。OSS/クローズド性能ギャップがほぼ消滅した [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) ことは、「格差拡大」前提を直接弱体化する。NVIDIA中国シェアゼロ [INFO-014](../Information/2026-05-11/collected-raw.md#INFO-014) も地政学的格差の変容を示す。

10R連続で同一方向にシフトしていることは、このシナリオの「格差拡大」前提が観測と整合していないことを示す。SCN-002/003が33%同率(0%差)でQHG象限の区別能力が消失した。再定義が次回Arbiter最優先必須条件。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | Azure排他性終了+GPT-5.5 on AWS Bedrock | 開放軸を支える最も強い構造証拠 | B-2 | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) |
| 高 | OSS/クローズド性能ギャップほぼ消滅 | 「格差拡大」前提を直接弱体化する | C-3 | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) |
| 高 | SCN-002/003確率33%同率(0%差)。10R連続同一方向シフト | 分析方法論の区別能力に重大な懸念 | B-3 | scenarios.json |
| 中 | OpenAI SDK provider-agnostic + 157K OpenCode移行 | 開放方向の追加証拠 | B-3 | [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) |
| 中 | NVIDIA中国シェアゼロ | 地政学的格差の変容 | C-3 | [INFO-014](../Information/2026-05-11/collected-raw.md#INFO-014) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| QHG象限再検討でSCN-002/003が統合または再区分される | 確率推移の連続性が失われ、過去9Rのシフトの意味が変わる | 30日 | scenarios.json |
| OSS(Mistral/DeepSeek)のエンタープライズ採用が3社で10%以上のシェアを取る | 「勝者集中」前提が崩れSCN-004が上昇する | 90日 | [IND-004](../config/indicators.json) |
| BenchLM上位3社差が3pt以内に収束する | 「勝者格差」の根拠が消え、SCN-004方向の根拠が立つ | 90日 | [IND-001](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-002-A | AAIF/MCP標準でAI間相互運用が確立する | 58% | Azure排他性終了+provider-agnostic SDK+OpenCode移行はgenuine C。標準競合が出た場合に崩れる | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) | (標準競合の可能性) |
| H-SCN-002-B | Tier 1の3社がフロンティア性能を維持し続ける | 38% | OSS/クローズドギャップ消滅で維持の根拠が急速に弱まっている。BenchLM上位差6-7ptは残るが診断的価値低下 | [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) [INFO-014](../Information/2026-05-11/collected-raw.md#INFO-014) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で高 | OSS/クローズドギャップほぼ消滅 | 2026-05-12 |
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライズ採用10%超で高 | DeepSeek V4 Pro 75%オフ [INFO-012](../Information/2026-05-11/collected-raw.md#INFO-012) | 2026-05-12 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | high水準 | 2026-05-12 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-12 | 確率 34→33%(-1pt) | DeployCo展開インフラ围い込み+Google AI Search围い込み深化。10R連続同一方向シフト。SCN-002/003同率33%でQHG軸区別能力消失確定 | 「9R連続低下」→「10R連続低下。QHG軸区別能力消失。同率33%」 |
| 2026-05-11 | 確率 35→34%(-1pt) | OSS/クローズドギャップ消滅+NVIDIA中国シェアゼロで「格差拡大」前提弱体化。Azure排他性終了は開放C。9R連続同一方向シフト。SCN-002/003差2% | 「8R連続低下」→「9R連続低下。格差拡大根拠がさらに薄れた。分析方法論に重大な懸念」 |
| 2026-05-08 | 確率 38→37%(-1pt) | 三社均質化制度化+価格二極化で「勝者」前提侵食継続 | 「7R連続低下」→「8R連続低下」 |
| 2026-05-06 | 確率 44→38%(-6pt) | 囲い込みシグナル4重蓄積と3社均質化 | 「開放×格差拡大の最有力」→「格差拡大の根拠が薄れてきた」 |

### §7 ブラインドスポット

- QHG象限の区別能力が低下している可能性。SCN-002/003が33%同率(0%差)でQHG軸の区別能力が消失した。次回Arbiterでの再定義が必須。
- 「開放」の観測が標準化(Azure排他性終了等)に集中しているが、围い込み形態変化(技術的→契約的)を観測する指標が不十分。
- 政府市場(Pentagon)の調達判断が民間市場の「開放」動向に及ぼす影響を定量化していない。

---

## SCN-003: 静かな囲い込み (現在確率: 33%)

> 象限: 閉鎖 × 性能差収斂

### §0 一文要約

モデル性能差は小さくなるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界を指す。現在33%でSCN-002と同率。直近10ラウンドで+1pt/ラウンドで推移。围い込み+収斂の8重C蓄積が観測されている。QHG軸の区別能力が消失。

### §1 コア判断

このシナリオの構造は「性能差が消えても離れられない」という顧客固定化にある。現在の観測はその方向に強く動いている。

収斂側の証拠は確定的だ。OSS/クローズド性能ギャップがほぼ消滅した [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037]。围い込み側も9重C蓄積: DeployCo展開インフラ围い込み [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001)、Google AI Search围い込み深化 [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005)、Gemini Enterprise統合スタック [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019)、Doubao有料化3段階 [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009)、Coze Agent World [INFO-021](../Information/2026-05-11/collected-raw.md#INFO-021)、エンタープライズメモリー唯一の堀 [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042)、EU AI Act延期 [INFO-032](../Information/2026-05-11/collected-raw.md#INFO-032)、SaaSpocalypse中間層排除 [INFO-041](../Information/2026-05-11/collected-raw.md#INFO-041)、パートナー非媒介化 [INFO-040](../Information/2026-05-11/collected-raw.md#INFO-040)。

モデル性能差の差別化価値が低下すれば、エコシステム围い込みの重要性が相対的に増すという構造的論理が強化されている。Azure排他性終了+provider-agnostic SDKは围い込みに対する反証として機能するが、「開放的な見た目の閉鎖」(MCPが相互運用を可能にしながらもSaaSワークフロー統合の深さが移行コストを決める)が同時に成立する。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | OSS/クローズド性能ギャップほぼ消滅 | 収斂軸を支える最も強い証拠 | C-3 | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) |
| 高 | 围い込み9重C蓄積(DeployCo+AI Search围い込み+Gemini Enterprise+Doubao+Coze+メモリー堀+EU延期+SaaSpocalypse+非媒介化) | 围い込みが配布・エコシステム・データ・規制の4次元で同時進行 | B-2 | [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009) [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042) |
| 高 | SCN-002/003確率33%同率 | 分析方法論の区別能力に重大な懸念 | B-3 | scenarios.json |
| 中 | Azure排他性終了+OpenAI SDK provider-agnostic | 反証として機能する開放シグナル | B-2 | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) |
| 中 | エンタープライズAI採用11%→42%(1年) | 围い込みが有効に働く最も重要なタイミング | B-3 | [INFO-035](../Information/2026-05-11/collected-raw.md#INFO-035) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| QHG象限再検討でSCN-002/003が統合または再区分される | 確率推移の連続性が失われる | 30日 | scenarios.json |
| 主要企業がMCP上でクロスベンダー切り替えを実証する事例が3件以上公表される | スイッチングコストが低いことが実証され、固定化シナリオへの根拠が薄まる | 90日 | [IND-017](../config/indicators.json) |
| 围い込みシグナル7重のうち3件以上が逆転する | 围い込みの構造的蓄積が止まり、確率上昇が止まる | 60日 | [IND-009](../config/indicators.json) [IND-022](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-003-A | モデル性能収斂でベンダー差別化は機能から围い込みに移行する | 52% | OSS/クローズドギャップ消滅は収斂の確定的証拠。围い込み9重C蓄積。但し「開放的な見た目の閉鎖」が成立するかは未実証 | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) |
| H-SCN-003-B | エコシステム統合深度が顧客の移行コストを決定する | 48% | エンタープライズメモリー堀宣言 [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042) は理論的C。実際の移行実績は未観測 | [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042) | [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-009](../config/indicators.json) | AI利用規約の制限強化 | 月3件超の制限追加で高 | Doubao有料化+Gemini Enterprise围い込み | 2026-05-12 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | OSS gap 3%以内で高 | OSS gapほぼゼロ | 2026-05-12 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全社採用で高(反証指標) | high水準 | 2026-05-12 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-12 | 確率 32→33%(+1pt)。SCN-002と同率33% | 围い込み9重C蓄積(DeployCo+AI Search追加)。10R連続同一方向シフト。QHG軸区別能力消失確定 | 「9R連続+1pt」→「10R連続。QHG軸区別能力消失。同率33%」 |
| 2026-05-11 | 確率 32%(SCN-002差2%に縮小) | 围い込み7重C蓄積+OSSギャップ消滅で構造的論理強化。QHG象限再検討必須条件化 | 「8R連続+1pt」→「9R連続。SCN-002差2%に縮小。分析方法論に重大な懸念」 |
| 2026-05-10 | 確率 31%(+1pt) | 围い込み+収斂の蓄積継続 | 「7R連続+1pt」→「8R連続+1pt」 |
| 2026-05-06 | 確率 24→28%(+4pt) | 囲い込みシグナル4重蓄積 | 「3R連続+1pt」→「4重Cで+4ptに加速」 |

### §7 ブラインドスポット

- SCN-002/003が33%同率(0%差)でQHG軸の区別能力が消失した。次回Arbiterでの再定義が必須。
- 「スイッチングコストが高い」という観測が、実際に顧客が離れられないことの実証ではない。
- 「静かな围い込み」が起きているとすれば顧客はそれを認識していないはずで、認識していない事象をシグナルとして観測することは構造的に困難だ。

---

## SCN-004: 誰でもAI (現在確率: 14%)

> 象限: 開放 × 性能差収斂

### §0 一文要約

性能差がなくなりオープン標準で自由に行き来できる世界を指す。現在14%で4位。OSSギャップ消滅 [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) は収斂方向の強いシグナルだが、VC $2,672億+ByteDance 2,000億元+SpaceX $3,500億の資本集中が二層市場構造を維持している。

### §1 コア判断

SCN-004は「モデルがコモディティ化し、価格も移行コストも消える」という条件が揃う場合に成立する。収斂方向の証拠は強い。OSSギャップ消滅、DeepSeek V4 Pro 75%オフ [INFO-012](../Information/2026-05-11/collected-raw.md#INFO-012)、157K OpenCode移行は下層の適合性を高める。

ただしQ1 2026 VC $2,672億、ByteDance 2,000億元CAPEX、SpaceX $3,500億評価額、Anthropic $3,800億評価額の資本集中は、インフラ集中で二層市場構造が継続することを示す。SCN-004は下層のみ部分的に成立するにとどまる。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | OSS/クローズド性能ギャップほぼ消滅 | コモディティ化の最も直接的な証拠 | C-3 | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) |
| 高 | Q1 2026 VC $2,672億+ByteDance 2,000億元+SpaceX $3,500億+Anthropic $3,800億 | 資本集中が二層市場構造を維持 | C-3 | [IND-029](../config/indicators.json) |
| 中 | DeepSeek V4 Pro 75%オフ+157K OpenCode移行 | 下層の適合性を高める | C-3 | [INFO-012](../Information/2026-05-11/collected-raw.md#INFO-012) [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLMの全層間差が5pt以内に収束する | フロンティアの優位性が消えSCN-004が現実的な主シナリオになる | 180日 | [IND-001](../config/indicators.json) |
| OSSモデルのエンタープライズ採用シェアが20%を超える | 二層市場の下層だけでなく上層も侵食が起きたとみなせる | 180日 | [IND-004](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-004-A | OSSモデルがエンタープライズの主流になる | 18% | OSSギャップ消滅は能力面の証拠だが、エンタープライズ実採用のデータがなく確度が低い | [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) | [IND-029](../config/indicators.json) 資本集中 |
| H-SCN-004-B | オープン標準でAIプロバイダー間の移行がほぼコストゼロになる | 24% | Azure排他性終了+provider-agnostic SDKは基盤だが、ワークフロー統合深度が移行コストを左右する | [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) | [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライズ採用20%超で高 | OSSギャップほぼゼロ(能力)。採用率は別途 | 2026-05-12 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | OSS gap 3%以内で高 | ほぼゼロ(高水準) | 2026-05-12 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-11 | 確率 14%据え置き | OSSギャップ消滅+DeepSeek 75%オフ+OpenCode移行はC。資本集中$3,672億+はI。相殺 | 「下層のみ部分的適合」→「下層の適合性は高まったが資本集中が天井」 |

### §7 ブラインドスポット

- 二層市場(大規模フロンティアユーザーと中小企業のOSSユーザー)が分離した形でSCN-004とSCN-002が共存するシナリオを、単一の確率に集約していることで精度が落ちている。
- 中国市場でのOSSダイナミクス(DeepSeek等)が西側市場に与えるコモディティ圧力を観測できていない。

---

## ブラックスワン: BS-001 AI安全性大事故 (現在確率: 16%)

> 低確率・高影響

### §0 一文要約

AIエージェントの本番障害・大規模セキュリティ事故が複合的に起き、業界全体に規制強化と信頼失墜をもたらす事象を指す。現在16%。新規大規模脆弱性なし。Agent SDK高頻度リリースは防御側強化だが、CEO 83%エージェント導入予定+91%$300K+/時間ダウンタイムの環境で自律実行は単一障害点影響を増幅。

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| AIエージェントによる金融・インフラへの大規模実害インシデントが公表される | 確率が急上昇し、全シナリオの再評価が必要になる | 常時 | [IND-013](../config/indicators.json) |
| 主要国でAIエージェントの本番使用を一時停止させる行政命令が出る | 業界構造が短期に変わり、SCN-001〜004の全確率に波及する | 90日 | [IND-030](../config/indicators.json) |

### §7 ブラインドスポット

- CEO 83%導入予定 vs CIO 25%監視可能のギャップは、監視できていないリスクが大半であることを示す。
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
| [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) | DeployCo設立(围い込みC) |
| [INFO-005](../Information/2026-05-12/collected-raw.md#INFO-005) | AI Search围い込み深化 |
| [INFO-006](../Information/2026-05-12/collected-raw.md#INFO-006) | GTIG AI開発ゼロデイ初検出 |
| [INFO-003](../Information/2026-05-11/collected-raw.md#INFO-003) | Azure排他性終了・GPT-5.5 on AWS Bedrock |
| [INFO-017](../Information/2026-05-11/collected-raw.md#INFO-017) | OpenAI SDK provider-agnostic |
| [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) | 157K開発者OpenCode移行 |
| [INFO-037](../Information/2026-05-11/collected-raw.md#INFO-037) | OSS/クローズド性能ギャップほぼ消滅 |
| [INFO-019](../Information/2026-05-11/collected-raw.md#INFO-019) | Gemini Enterprise Agent Platform |
| [INFO-009](../Information/2026-05-11/collected-raw.md#INFO-009) | Doubao有料版3段階 |
| [INFO-021](../Information/2026-05-11/collected-raw.md#INFO-021) | Coze 2.5 Agent World |
| [INFO-042](../Information/2026-05-11/collected-raw.md#INFO-042) | エンタープライズメモリー唯一の堀 |
| [INFO-041](../Information/2026-05-11/collected-raw.md#INFO-041) | SaaSpocalypse |
| [INFO-032](../Information/2026-05-11/collected-raw.md#INFO-032) | EU AI Act延期 |
| [INFO-014](../Information/2026-05-11/collected-raw.md#INFO-014) | NVIDIA中国シェアゼロ |
| [INFO-012](../Information/2026-05-11/collected-raw.md#INFO-012) | DeepSeek V4 Pro 75%オフ |
| [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) | Pentagon 7社契約 |
| [INFO-035](../Information/2026-05-11/collected-raw.md#INFO-035) | エンタープライズAI採用11%→42% |
| [Arbiter v3.75](../state/arbiter-2026-05-12.md) | 確度評価の完全根拠(付録のみ参照) |
