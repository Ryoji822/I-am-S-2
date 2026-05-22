# シナリオ追跡 — 静的インテリジェンス

> 最終判断更新: 2026-05-22
> 全体確信度: 中
> 主参照: scenarios.json, indicators.json#IND-001/004/007/009/011/015/017/018/019/020/022/023/024/027/030
> Arbiter: v3.85

---

## 確率推移サマリ

過去20日の確率推移。主軸4シナリオ + Black Swan 2件。v3.85で全4シナリオが±1%変動し、SCN-004(20%)がSCN-001(17%)との差を3ptに拡大。SCN-003(36%)が最高確率を維持。

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|:-------:|:-------:|:-------:|:-------:|:------:|:------:|
| 2026-05-22 | 17% | 27% | 36% | 20% | 17% | 3% |
| 2026-05-21 | 18% | 28% | 35% | 19% | 17% | 3% |
| 2026-05-20 | 20% | 30% | 35% | 15% | 17% | 3% |
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

v3.85でSCN-004(20%, +1)がSCN-001(17%, -1)との差を3ptに拡大し、コモディティ化+開放方向の趨勢が強まった。API価格-67%下落 [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031)、Cohere Command A+ OSSエンタープライズモデル [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051)、MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) がSCN-004を押し上げる三重の圧力として働いた。SCN-003(36%, +1)は围い込み16件蓄積と$2.52T世界AI支出 [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) で最高確率を維持。SCN-002(27%, -1)はMCP 1300とWebMCP [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) で開放側は強いが、価格破壊が「差別化持続」前提をさらに蝕む。SCN-001(17%, -1)はGoogle I/O 100件発表 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) の围い込みは強いものの、価格破壊が差別化の持続性を根本から損なう。

---

## 2つの軸の意味

X軸(開放/閉鎖)は、AIの実行環境・データ・標準がどれだけ可搬かを問う。MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015)、Cohere Command A+ OSS [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051)、DeepSeek V4 [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039)、WebMCP標準提案 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) は「開放」方向。Google I/O 100件発表のエコシステム深耕 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007)、ペンタゴンOpenAI契約 [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048)、Anthropic-Stainless買収 [INFO-009](../Information/2026-05-22/collected-raw.md#INFO-009) は「閉鎖」方向。Y軸(差別化持続/コモディティ化)は、フロンティアモデルの高付加価値が維持されるか、価格・能力の平準化でコモディティ化するかを問う(v3.84再定義)。API価格-67%下落 [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) は「コモディティ化」方向の確定的証拠。Gemini 3.5 Flash AIME 73.3% [INFO-030](../Information/2026-05-22/collected-raw.md#INFO-030) とErdős予想反証 [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) は性能競争の継続を示すが、差別化持続には不十分。METR現実世界ギャップ [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) はベンチマークと実務の乖離を示し、フロンティア差別化の実際的価値に疑問を呈する。

---

## SCN-001: 囲い込みの勝者 (現在確率: 17%)

> 象限: 閉鎖 × 差別化持続

### §0 一文要約

1-2社がフロンティア差別化を維持しつつ実行環境・データ・ガバナンスで囲い込む世界を指すが、現在確率は17%で4位。API価格-67%下落 [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) が差別化の持続可能性を根本から損ない、MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) とCohere Command A+ OSS [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) が封鎖の前提をさらに弱体化させている。Google I/O 100件 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) の围い込み圧力は強いが、価格破壊がその差別化根拠を蝕む構造的矛盾がある。

### §1 コア判断

このシナリオは「フロンティア差別化の持続と生態系封鎖が同時に起きる」という条件に依存する。現在、両条件はさらに弱まった。

差別化持続側では、API価格が全主要プロバイダーで-67%下落し [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031)、価格面での差別化が困難になった。DeepSeek R2がOSSでGPT-4oにマッチし [INFO-031](../Information/2026-05-20/collected-raw.md#INFO-031)、DeepSeek V4がさらにオープン層の性能を押し上げる [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039)。Erdős予想反証 [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) はフロンティアの数学的推論能力を示すが、これは汎用推論モデルによる成果であり、特定企業の持続的優位とは直結しない。

封鎖側では、MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015)、Cohere Command A+ OSSエンタープライズモデル [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051)、WebMCP標準提案 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) が開放方向の構造的証拠として蓄積する。围い込み否定は15件を超え、開放C証拠の連続不在もCohere OSS(A-3)とWebMCP(A-3)で破れた。封鎖が進むというより標準化とOSS普及が進むと解釈すべき段階に入っている。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | API価格-67%下落。全主要プロバイダー対象 | 差別化持続の前提が価格面で崩れる最も具体的な観測 | C-3 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) |
| 高 | 围い込み否定15件超蓄積: MCP 1300+Cohere OSS+WebMCP等 | 封鎖の前提が崩れる構造的証拠。開放C証拘連続不在が破れた | A-3 | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) |
| 中 | Google I/O 100件: Gemini 3.5 Flash+Antigravity 2.0+Managed Agents+Spark | 围い込み方向の強い証拠だが、価格破壊と矛盾 | A-3 | [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) |
| 中 | DeepSeek V4+Gemma 4+Kimi K2.6 オープンモデル集中リリース | OSS性能ギャップのさらなる縮小 | C-3 | [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) |

### §3 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLM上位1社と2位以下の差が20pt以上に拡大 | 差別化持続の前提が成立し始める | 90日 | [IND-001](../config/indicators.json) |
| 有力2社がクロスクラウド撤退し自社基盤のみに移行 | 相互依存構造が解体され封鎖化が進む | 180日 | [IND-018](../config/indicators.json) |
| 政府・規制当局がAI市場での独占を認める判断を下す | 競争法的制約が外れ围い込みに外部制動がなくなる | 180日 | [IND-023](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-001-A | フロンティア差別化が顧客ロックインの主因になる | 12% | API価格-67%下落+DeepSeek V4 OSSリリースで差別化の金銭的表現としての価値がさらに低下。価格破壊が進む中、性能差の経済的意味が希薄化 | (なし) | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) |
| H-SCN-001-B | 1-2社がエコシステムを垂直統合し他社の参入を封じる | 15% | 围い込み否定15件超蓄積で封鎖の兆候がない。MCP 1300本番サーバー+Cohere OSSが相互運用を促進。開放C証拠連続不在が破れた | (なし) | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク非連続ジャンプ | +10pt以上/期で高 | OSS性能ギャップ消滅確定 | 2026-05-22 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | MCP 1300本番サーバー+WebMCP標準提案。high水準 | 2026-05-22 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-22 | 確率17%(-1)。API価格-67%下落が差別化持続をさらに弱体化 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) -67%価格下落+Cohere OSS+MCP 1300が封鎖・差別化の両前提を侵食 | 18%(v3.84)→17%(v3.85) |
| 2026-05-21 | 確率18%(-2)。Y軸再定義による再評価。SCN-004に逆転され4位に転落 | QHG Y軸再定義(差別化持続/コモディティ化)で「差別化持続」前提が厳格に評価 | 20%(v3.83)→18%(v3.84) |

### §7 ブラインドスポット

- 围い込み形態変化(技術的→契約的・エコシステム的)が起きている場合、技術指標(IND-001等)では捉えきれない。
- 中国市場(DeepSeek/ByteDance)での独占形成度は観測できていない。
- API価格下落が一時的な供給過剰か、構造的なコモディティ化かの区別が不十分。価格回復すればSCN-001の条件が再び成立する余地がある。

---

## SCN-002: 技術は開く但勝者は出る (現在確率: 27%)

> 象限: 開放 × 差別化持続

### §0 一文要約

AAIF/MCP等の相互運用標準で移行の自由度は確保されるが、フロンティア差別化はTier 1に集中する構造を指す。現在27%で2位。MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) とWebMCP標準提案 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) は開放方向を強く支持するが、API価格-67%下落 [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) は「差別化持続」前提をさらに弱体化させ、開放と差別化持続の同時成立を困難にしている。

### §1 コア判断

「開放されているが差別化は残る」という世界は、標準化が進む一方でフロンティアの高付加価値が維持される場合に成立する。開放側の証拠は史上最強だ。MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015)、WebMCP標準提案 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007)、Cohere Command A+ OSS [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051)、DeepSeek V4 [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) が開放の構造的基盤を構築している。

差別化持続側は弱い。API価格-67%下落 [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) に加え、DeepSeek R2 OSSがGPT-4oにマッチし [INFO-031](../Information/2026-05-20/collected-raw.md#INFO-031)、Gemini 3.5 Flash AIME 73.3% [INFO-030](../Information/2026-05-22/collected-raw.md#INFO-030) は性能競争の存在を示すものの、OSS側の追従速度を考慮すると差別化の持続性は不確定だ。METR現実世界ギャップ [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) も、ベンチマーク上の差別化が実務上の差別化に直結しないことを示唆する。開放の強さと差別化持続の弱さが同時に観測される状況は、SCN-002からSCN-004(開放×コモディティ化)への移行圧力を意味する。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | MCP 1300本番サーバー+WebMCP標準提案 | 開放軸を支える最も強い構造証拠 | C-3 | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) |
| 高 | API価格-67%下落+DeepSeek R2 OSS GPT-4oマッチ | 差別化持続の前提を弱体化する価格・能力の二重圧力 | C-3 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-031](../Information/2026-05-20/collected-raw.md#INFO-031) |
| 高 | Cohere Command A+ OSSエンタープライズモデル | 開放エコシステムのエンタープライス層への浸透 | A-3 | [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) |
| 中 | Gemini 3.5 Flash AIME 73.3%+GPQA Diamond 74.2% | 性能競争の継続を示すが差別化持続の証拠として不十分 | A-3 | [INFO-030](../Information/2026-05-22/collected-raw.md#INFO-030) |
| 中 | METR現実世界ギャップ: エージェントのベンチマーク乖離 | ベンチマーク上の差別化が実務上の価値に直結しない | A-3 | [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| OSSモデルのエンタープライス採用が3社で10%以上のシェアを取る | 「勝者集中」前提が崩れSCN-004が上昇する | 90日 | [IND-004](../config/indicators.json) |
| BenchLM上位3社差が3pt以内に収束する | 「差別化持続」の根拠が消え、SCN-004方向の根拠が立つ | 90日 | [IND-001](../config/indicators.json) |
| トークン価格がさらに50%下落し主要プロバイダーの収益性が脅かされる | 差別化持続の経済的基盤が崩れる | 90日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-002-A | AAIF/MCP標準でAI間相互運用が確立する | 65% | MCP 1300本番サーバー+WebMCP標準提案+Cohere OSSは開放の構造的蓄積。前回62%から上昇 | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) | (標準競合の可能性) |
| H-SCN-002-B | Tier 1の3社がフロンティア差別化を維持し続ける | 25% | API価格-67%下落+DeepSeek V4 OSSで差別化維持の経済的根拠が急速に弱まっている。METRギャップもベンチマーク差別化の実務価値に疑問 | [INFO-030](../Information/2026-05-22/collected-raw.md#INFO-030) | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で高 | OSS性能ギャップ消滅確定 | 2026-05-22 |
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用10%超で高 | MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) | 2026-05-22 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | MCP 1300+WebMCP標準提案。high水準 | 2026-05-22 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-22 | 確率27%(-1)。価格破壊が「差別化持続」をさらに弱体化 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) -67%価格下落+[INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) METRギャップが差別化の実務的価値に疑問 | 28%(v3.84)→27%(v3.85) |
| 2026-05-21 | 確率28%(-2)。Y軸再定義による再評価 | QHG Y軸再定義で「差別化持続」が厳格に評価 | 30%(v3.83)→28%(v3.84) |

### §7 ブラインドスポット

- 「差別化持続」の判定がベンチマークと価格に偏っている。ユーザー体験・信頼性・コンプライアンス等の非価格差別化を観測する指標が不十分。
- 開放エコシステムの拡大(MCP 1300等)が「開放」を意味するか、標準主導者による新しい围い込みを意味するかの区別が困難。
- Tier 1企業の戦略転換(差別化追求から規模追求)が起きた場合、SCN-002からSCN-004への急速な移行を捉えられない可能性がある。
- METRギャップが示す「ベンチマークと実務の乖離」は、差別化の実務的価値を過大評価している可能性を示唆するが、定量化が不十分。

---

## SCN-003: 静かな囲い込み (現在確率: 36%)

> 象限: 閉鎖 × コモディティ化

### §0 一文要約

モデル差別化は薄れるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界を指す。現在36%で最高確率。围い込み16件蓄積、API価格-67%下落 [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) でコモディティ化が確定的、METR現実世界ギャップ [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) がベンチマーク差別化の実務的限界を補強。$2.52T世界AI支出 [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) が資本集中を加速させ、围い込みの物理的基盤を強化する。

### §1 コア判断

このシナリオの構造は「差別化が消えても離れられない」という顧客固定化にある。現在の観測はその方向にさらに強く動いている。

コモディティ化側の証拠は確定的だ。API価格が全主要プロバイダーで-67%下落し [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031)、DeepSeek V4 [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) とCohere Command A+ OSS [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) がオープン層の性能とエンタープライス対応を押し上げる。METR現実世界ギャップ [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) は、ベンチマーク上の性能差が実際の業務では縮小・消失することを示唆し、フロンティア差別化の実務的価値に疑問を呈する。

围い込み側は16件に増加した。Google I/O 100件発表によるエコシステム深耕 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007)、ペンタゴンOpenAI契約による政府围い込み [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048)、Anthropic-Stainless買収による開発者エコシステム統合 [INFO-009](../Information/2026-05-22/collected-raw.md#INFO-009) が新規蓄積分。$2.52T世界AI支出(44% YoY) [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) は資本集中を示し、围い込みの物理的基盤を強化する。

差別化価値の低下が围い込みの重要性を相対的に増す構造的論理は、MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) が示す「開放的な見た目の閉鎖」という一見矛盾した動向と整合する。プロトコルは開放されるが、SaaSワークフロー統合の深さが移行コストを決める構造だ。ペンタゴンのAnthropic排除→OpenAI選定 [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) は、围い込みの主体が複数(単一企業ではなく業界全体)であることを示し、「静かな围い込み」の範囲が拡大している。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | API価格-67%下落+DeepSeek V4 OSS+Cohere Command A+ OSS | コモディティ化を支える価格・能力・エンタープライスの三重証拠 | C-3 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) |
| 高 | 围い込み16件蓄積: Google I/O 100件+ペンタゴンOpenAI契約+Anthropic-Stainless買収等 | 围い込みが配布・エコシステム・データ・ハードウェア・政府の多次元で同時進行 | A-3 | [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-009](../Information/2026-05-22/collected-raw.md#INFO-009) |
| 高 | METR現実世界ギャップ: ベンチマークと実務の乖離 | フロンティア差別化の実務的価値に疑問。コモディティ化の補強 | A-3 | [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) |
| 中 | $2.52T世界AI支出(44% YoY) | 資本集中が围い込みの物理的基盤を強化 | A-2 | [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) |
| 中 | MCP 1300本番サーバー | 開放プロトコルは進展するが、エコシステム深度の差は埋まらない | C-3 | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| 主要企業がMCP上でクロスベンダー切り替えを実証する事例が3件以上公表される | スイッチングコストが低いことが実証され、固定化シナリオへの根拠が薄まる | 90日 | [IND-017](../config/indicators.json) |
| 围い込みシグナル16件のうち4件以上が逆転する | 围い込みの構造的蓄積が止まり、確率上昇が止まる | 60日 | [IND-009](../config/indicators.json) [IND-022](../config/indicators.json) |
| トークン価格が底打ちし主要プロバイダーの価格競争が収束する | コモディティ化圧力が減退し、SCN-001/002の確率が上昇する | 120日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-003-A | モデルコモディティ化でベンダー差別化は機能から围い込みに移行する | 62% | API価格-67%下落+DeepSeek V4 OSS+Cohere OSSはコモディティ化の確定的証拠。围い込み16件蓄積。「開放的な見た目の閉鎖」が成立するかは未実証 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) |
| H-SCN-003-B | エコシステム統合深度が顧客の移行コストを決定する | 55% | Google I/O 100件+ペンタゴンOpenAI契約+Anthropic-Stainless買収の蓄積は理論的C。実際の移行実績は未観測 | [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) | (クロスベンダー移行事例不在) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-009](../config/indicators.json) | AI利用規約の制限強化 | 月3件超の制限追加で高 | 围い込み16件蓄積 | 2026-05-22 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | トークン価格50%以上下落で高 | API価格-67%下落で消滅確定 | 2026-05-22 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全社採用で高(反証指標) | MCP 1300+WebMCP標準提案。high水準 | 2026-05-22 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-22 | 確率36%(+1)。围い込み16件蓄積+METRギャップ+資本集中で構造的論理が強化 | [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) Google I/O+[INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) ペンタゴン+[INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) $2.52T支出 | 35%(v3.84)→36%(v3.85) |
| 2026-05-21 | 確率35%据え置き。Y軸再定義で象限名変更(性能差収斂→コモディティ化) | 围い込み15件蓄積+トークン価格75%下落+OSSギャップ消滅 | 35%(v3.83)→35%(v3.84) |

### §7 ブラインドスポット

- 「スイッチングコストが高い」という観測が、実際に顧客が離れられないことの実証ではない。
- 「静かな围い込み」が起きているとすれば顧客はそれを認識していないはずで、認識していない事象をシグナルとして観測することは構造的に困難だ。
- コモディティ化が進行する中で围い込みの価値(囲い込む対象の差別化)自体が低下する矛盾を十分に分析できていない。
- API価格下落が围い込み戦略(高付加価値で囲う)を矛盾させるか、逆に価格破壊からの逃避先として围い込みを加速させるかの判断が不確定。
- ペンタゴンのAnthropic排除→OpenAI選定は围い込みの「主体多元化」を示すが、単一企業围い込みか業界全体围い込みかの区別ができていない。

---

## SCN-004: 誰でもAI (現在確率: 20%)

> 象限: 開放 × コモディティ化

### §0 一文要約

差別化が薄れオープン標準で自由に行き来できる世界を指す。現在20%で3位。API価格-67%下落 [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) + DeepSeek V4 OSS [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) + MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) + Cohere Command A+ OSS [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) がコモディティ化+開放の四重の圧力として働く。ただし$2.52T世界AI支出 [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) の資本集中が二層市場構造を維持し、完全な平準化には至っていない。

### §1 コア判断

SCN-004は「モデルがコモディティ化し、価格も移行コストも消える」という条件が揃う場合に成立する。コモディティ化+開放方向の証拠はv3.85で史上最強になった。API価格-67%下落 [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031)、DeepSeek V4 OSS [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039)、MCP 1300本番サーバー [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015)、Cohere Command A+ OSSエンタープライズモデル [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) は価格・能力・標準・エンタープライスの四重の圧力として働く。WebMCP標準提案 [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) はブラウザベースエージェントの相互運用を促進し、移行コストの低下を加速する。

ただし$2.52T世界AI支出(44% YoY) [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) はインフラ集中を示し、二層市場構造の完全解消には至っていない。ペンタゴンOpenAI契約 [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) も政府調達における選別を示し、完全な「誰でも」の条件からは遠い。围い込み16件蓄積は、コモディティ化が進んでもエコシステム深度による差別化が残る可能性(SCN-003)を示唆する。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | API価格-67%下落 | コモディティ化の最も直接的な価格証拠 | C-3 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) |
| 高 | DeepSeek V4 OSS+Gemma 4+Kimi K2.6 オープンモデル集中リリース | 能力面でのコモディティ化証拠。OSS層の性能押し上げ | C-3 | [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) |
| 高 | MCP 1300本番サーバー+WebMCP標準提案 | 開放方向の構造的証拠。移行コスト低下を促進 | C-3 | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) |
| 高 | Cohere Command A+ OSSエンタープライズモデル | エンタープライス層でのOSS選択肢の出現 | A-3 | [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) |
| 中 | $2.52T世界AI支出(44% YoY) | 資本集中が二層市場構造を維持(反証) | A-2 | [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) |
| 中 | ペンタゴンOpenAI契約: Anthropic排除→OpenAI選定 | 政府調達での選別(反証)。完全な「誰でも」から遠い | A-2 | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLMの全層間差が5pt以内に収束する | フロンティアの優位性が消えSCN-004が現実的な主シナリオになる | 180日 | [IND-001](../config/indicators.json) |
| OSSモデルのエンタープライス採用シェアが20%を超える | 二層市場の下層だけでなく上層も侵食が起きたとみなせる | 180日 | [IND-004](../config/indicators.json) |
| 主要フロンティア企業が価格引き上げに成功する | コモディティ化圧力が需要側の抵抗で減退する | 90日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-004-A | OSSモデルがエンタープライスの主流になる | 28% | API価格-67%下落+DeepSeek V4+Cohere Command A+ OSSは能力・価格・エンタープライス対応の証拠だが、実際のエンタープライスシェアデータが不足 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) | [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) 資本集中 |
| H-SCN-004-B | オープン標準でAIプロバイダー間の移行がほぼコストゼロになる | 35% | MCP 1300+WebMCPは基盤だが、ワークフロー統合深度が移行コストを左右する。围い込み16件蓄積は反証 | [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) | 围い込み16件蓄積 |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用20%超で高 | Cohere Command A+ OSS [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051)。実採用率は別途 | 2026-05-22 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | トークン価格50%以上下落で高 | API価格-67%下落で確定 | 2026-05-22 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-22 | 確率20%(+1)。四重の圧力でSCN-001との差が3ptに拡大 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) -67%価格下落+[INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) DeepSeek V4+[INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) Cohere OSS | 19%(v3.84)→20%(v3.85) |
| 2026-05-21 | 確率19%(+4)。Y軸再定義による再評価。SCN-001を逆転し3位に浮上 | QHG Y軸再定義でコモディティ化方向が直接評価対象に | 15%(v3.83)→19%(v3.84) |

### §7 ブラインドスポット

- 二層市場(大規模フロンティアユーザーと中小企業のOSSユーザー)が分離した形でSCN-004とSCN-003が共存する可能性を、単一の確率に集約していることで精度が落ちている。
- 中国市場でのOSSダイナミクス(DeepSeek等)が西側市場に与えるコモディティ圧力を観測できていない。
- API価格下落が一時的な供給過剰によるものか、構造的なコモディティ化によるものかの区別が不十分。
- $2.52T CAPEXが供給過剰で価格破壊を加速するか、インフラ集中で围い込みを強化するかの二面性を十分に分析できていない。
- Cohere Command A+の「OSSエンタープライズモデル」という位置づけが、実際にエンタープライスでのOSS採用を引き起こすかは未実証。

---

## ブラックスワン: BS-001 AI安全性大事故 (現在確率: 17%)

> 低確率・高影響

### §0 一文要約

AIエージェントの本番障害・大規模セキュリティ事故が複合的に起き、業界全体に規制強化と信頼失墜をもたらす事象を指す。現在17%。METR現実世界ギャップ [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) でエージェントのベンチマーク乖離が確認され、攻撃面拡大の懸念が持続。エージェント展開企業の88%がセキュリティインシデント報告 [INFO-011](../Information/2026-05-22/collected-raw.md#INFO-011)、企業データ漏洩の8分の1がAIエージェント起因。ペンタゴンAI Task ForceがCyber Command/NSAへのAI展開を決定 [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049) し、高リスク環境でのAI利用が加速。新規大規模実被害のA-2+報告なし。

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| AIエージェントによる金融・インフラへの大規模実害インシデントが公表される | 確率が急上昇し、全シナリオの再評価が必要になる | 常時 | [IND-013](../config/indicators.json) |
| 主要国でAIエージェントの本番使用を一時停止させる行政命令が出る | 業界構造が短期に変わり、SCN-001〜004の全確率に波及する | 90日 | [IND-030](../config/indicators.json) |
| METR相当の調査でAIコード本番障害率が60%を超える | 攻撃面の拡大が閾値を超え、BS-001確率が25%以上に跳ね上がる | 180日 | [IND-013](../config/indicators.json) |

### §7 ブラインドスポット

- METR現実世界ギャップが大事故への直接的連鎖を意味するかは不確定。率そのものより影響度(金額・人命)の観測が必要。
- 大事故が起きたとき、どのシナリオに収束するかの分析を持っていない。
- ペンタゴンCyber Command/NSA展開 [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049) が国家安全保障上のAI事故リスクをどう変化させるかの評価が不十分。
- 88%セキュリティインシデント報告 [INFO-011](../Information/2026-05-22/collected-raw.md#INFO-011) は頻度を示すが深刻度の分布が不明。

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
- 量子進展が急激に起きた場合、全シナリオの前提(計算コスト・資本集中の意味)が同時に崩れる可能性がある。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) | API価格-67%下落(SCN-001/002/003/004コモディティ化根拠) |
| [INFO-015](../Information/2026-05-22/collected-raw.md#INFO-015) | MCP 1300本番サーバー(開放C。SCN-002/004根拠) |
| [INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) | Cohere Command A+ OSSエンタープライズモデル(開放C。SCN-004根拠) |
| [INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) | DeepSeek V4+Gemma 4 OSSリリース(コモディティ化C。SCN-004根拠) |
| [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) | Google I/O 100件発表(围い込みC+WebMCP開放C。SCN-001/003根拠) |
| [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) | ペンタゴンOpenAI契約(围い込みC。SCN-003根拠) |
| [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049) | ペンタゴンAI Task Force Cyber Command/NSA(BS-001根拠) |
| [INFO-009](../Information/2026-05-22/collected-raw.md#INFO-009) | Anthropic-Stainless買収(围い込みC。SCN-003根拠) |
| [INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) | $2.52T世界AI支出44% YoY(資本集中I。SCN-003根拠) |
| [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) | Erdős予想反証(フロンティア能力C。SCN-001/002参考) |
| [INFO-030](../Information/2026-05-22/collected-raw.md#INFO-030) | Gemini 3.5 Flash AIME 73.3%(性能競争C。SCN-002参考) |
| [INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) | METR現実世界ギャップ(SCN-003コモディティ化+BS-001攻撃面) |
| [INFO-011](../Information/2026-05-22/collected-raw.md#INFO-011) | エージェント展開企業88%セキュリティインシデント(BS-001根拠) |
| [INFO-031](../Information/2026-05-20/collected-raw.md#INFO-031) | DeepSeek R2 OSS GPT-4oマッチ(SCN-002/003/004過去根拠) |
| [INFO-001](../Information/2026-05-20/collected-raw.md#INFO-001) | Codex 4M WAU + Dell提携(围い込みC。SCN-003根拠) |
| [Arbiter v3.85](../state/arbiter-2026-05-22.md) | 確率更新の完全根拠(付録のみ参照) |
