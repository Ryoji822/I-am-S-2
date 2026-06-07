# シナリオ追跡 — 静的インテリジェンス

> 最終判断更新: 2026-06-07
> 全体確信度: 中
> 主参照: [scenarios.json](../config/scenarios.json), [indicators.json](../config/indicators.json)
> Arbiter: v4.01

---

## 確率推移サマリ

過去20日の確率推移。主軸4シナリオ + Black Swan 2件。v4.01でSCN-003(32%)が依然最高確率だがSCN-004(27%)との差が5ptに縮小。v3.94時点の10pt差から半減。SCN-004はAPI価格下落トレンド [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) + NVIDIA Nemotron OSS [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) + コーディングスキル40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) + 142Kテックレイオフ [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) の四重の直接支持。SCN-003はQHG再定義32R連続未実行で統計的是正が継続しv3.94から-3%。SCN-001(17%)は围い込み蓄積32件で+2%回復。SCN-002(24%)は差別化持続の根拠がさらに弱まりv3.94から-1%。

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|:-------:|:-------:|:-------:|:-------:|:------:|:------:|
| 2026-06-07 | 17% | 24% | 32% | 27% | 17% | 3% |
| 2026-06-06 | 17% | 24% | 33% | 26% | 17% | 3% |
| 2026-06-05 | 16% | 24% | 34% | 26% | 17% | 3% |
| 2026-06-04 | 15% | 25% | 35% | 25% | 17% | 3% |
| 2026-06-01 | 15% | 25% | 35% | 25% | 17% | 3% |
| 2026-05-31 | 15% | 25% | 35% | 25% | 17% | 3% |
| 2026-05-30 | 15% | 26% | 36% | 23% | 17% | 3% |
| 2026-05-29 | 15% | 27% | 37% | 21% | 17% | 3% |
| 2026-05-28 | 15% | 27% | 37% | 21% | 17% | 3% |
| 2026-05-27 | 15% | 27% | 37% | 21% | 17% | 3% |
| 2026-05-25 | 15% | 27% | 37% | 21% | 17% | 3% |
| 2026-05-24 | 16% | 27% | 36% | 21% | 17% | 3% |
| 2026-05-23 | 16% | 27% | 36% | 21% | 17% | 3% |
| 2026-05-22 | 17% | 27% | 36% | 20% | 17% | 3% |
| 2026-05-21 | 18% | 28% | 35% | 19% | 17% | 3% |
| 2026-05-20 | 20% | 30% | 35% | 15% | 17% | 3% |
| 2026-05-19 | 20% | 30% | 35% | 15% | 16% | 3% |
| 2026-05-18 | 20% | 30% | 35% | 15% | 16% | 3% |
| 2026-05-17 | 20% | 31% | 35% | 14% | 16% | 3% |
| 2026-05-16 | 20% | 32% | 35% | 14% | 16% | 3% |

v4.01でSCN-003(32%, -1)とSCN-004(27%, +1)の差が5ptに縮小した。SCN-003はQHG再定義32R連続未実行で統計的是正が継続。コモディティ化証拠(API価格下落 [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030)・Nemotron OSS [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008)・コーディング40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041))はSCN-003とSCN-004の双方に支持されるが、围い込み蓄積がSCN-003特有の支持要因として機能する限りSCN-004への完全移行は起きていない。SCN-001(17%)は围い込み蓄積32件でv3.94(15%)から+2%回復したが、Google二層戦略(基盤開放・上位围い込み)の可能性が「勝者」の確定を妨げる。SCN-002(24%)は「勝者」の価値プレミアムが圧縮され続け、SCN-004との境界がさらに曖昧化。BS-001(17%, ±0%)はRSI進展 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) が能力-リスク二面性を具体化するが、大規模実被害A-2報告なし。critical移行条件未到達。

---

## 2つの軸の意味

X軸(開放/閉鎖)はAIの実行環境・データ・標準がどれだけ可搬かを問う。MCP 97M SDK DL [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021)、Google agents-cli クロスエージェント [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023)、MAF OSS [INFO-010](../Information/2026-06-05/collected-raw.md#INFO-010)、ADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) は開放方向。Gemini Enterprise Agent Platform Skill Registry/RAG Engine [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006)、Anthropic-SpaceX計算契約 [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002)、ペンタゴン围い込み構造 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) は閉鎖方向。Y軸(差別化持続/コモディティ化)はフロンティアモデルの高付加価値が維持されるか、価格・能力の平準化でコモディティ化するかを問う。142Kテックレイオフ [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038)・Copilot定額→従量制 [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039)・コーディングスキル40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) はコモディティ化方向の構造的シフト。API価格下落トレンド [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) は継続的価格破壊。NSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) は围い込み(使用量増による固定化)の支持証拠。一方でAnthropic $965B評価額 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039)・Q1 $300B投資 [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033) は資本集中の加速を示すが、差別化持続には直結しない。

---

## SCN-001: 囲い込みの勝者 (現在確率: 17%)

> 象限: 閉鎖 × 差別化持続

### §0 一文要約

1-2社がフロンティア差別化を維持しつつ実行環境・データ・ガバナンスで囲い込む世界を指す。現在17%で4位。围い込み蓄積が32件に達し次元が拡大(ハードウェア: Googlebook [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011)、決済: Daybreak予告 [INFO-004](../Information/2026-06-06/collected-raw.md#INFO-004)、SaaS: Workday統合 [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048))したが、ADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011)・Nemotron OSS [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008)・MCP 97M [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) が围い込み否定を継続。Google二層戦略(基盤開放・上位围い込み)の可能性があり「勝者」の確定を妨げる。

### §1 コア判断

このシナリオは「フロンティア差別化の持続と生態系封鎖が同時に起きる」という条件に依存する。围い込み側は強まった。KPMG 276,000人展開 [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001)、Anthropic-SpaceX 300MW計算契約 [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002)、Gemini Enterprise Agent Platform [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) が围い込みの次元拡大を実証する。

差別化持続側は弱いままだ。API価格下落トレンド [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) が価格面での差別化を困難にし、コーディングスキル40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) がスキル差別化を侵食する。Nemotron OSS [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) とADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) はオープン層の性能を押し上げ、围い込み否定の蓄積が続く。围い込みの形態は多様化(配布・エコシステム・データ・ハードウェア・決済)したが、6次元分散は集中戦略より弱く「勝者」の確定には至っていない。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | 围い込み蓄積32件・次元拡大(Googlebook/Daybreak/Workday) | 围い込みの形態多様化。但し分散=弱化リスク | A-3 | [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) |
| 高 | API価格下落トレンド+コーディングスキル40%陳腐化 | 差別化持続の前提を価格・スキル面で侵食 | B-2 | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) |
| 高 | Nemotron OSS+ADK OSS+MCP 97M | 開放方向の構造的蓄積。封鎖前提の弱体化 | A-3 | [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) |
| 中 | KPMG 276,000人Claude展開+Anthropic-SpaceX 300MW | 围い込みの強力な実証だが価格破壊と矛盾 | A-3 | [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) |

### §3 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLM上位1社と2位以下の差が20pt以上に拡大 | 差別化持続の前提が成立し始める | 90日 | [IND-001](../config/indicators.json) |
| 有力2社がクロスクラウド撤退し自社基盤のみに移行 | 相互依存構造が解体され封鎖化が進む | 180日 | [IND-018](../config/indicators.json) |
| 政府・規制当局がAI市場での独占を認める判断を下す | 競争法的制約が外れ围い込みに外部制動がなくなる | 180日 | [IND-023](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-001-A | フロンティア差別化が顧客ロックインの主因になる | 12% | 围い込み蓄積32件は強いがAPI価格下落+OSS追従で金銭的価値が低下 | [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) |
| H-SCN-001-B | 1-2社がエコシステムを垂直統合し他社の参入を封じる | 14% | MCP 97M+ADK OSS+Nemotron OSSで開放蓄積。封鎖兆候は次元拡大のみ | [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク非連続ジャンプ | +10pt以上/期で高 | OSS性能ギャップ消滅方向 | 2026-06-07 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | MCP 97M+ADK OSS+MAF OSS。high水準 | 2026-06-07 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-06-07 | ±0%。QHG再定義32R連続未実行。围い込み蓄積は継続するが統計的是正対象外 | QHG再定義32R目 | 17%(v4.00)→17%(v4.01) |
| 2026-06-06 | +1%。围い込みI 32件蓄積+次元拡大(ハードウェア: Googlebook・決済: Daybreak予告・SaaS: Workday統合)。Google二層戦略の可能性記録 | [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) [INFO-011](../Information/2026-06-06/collected-raw.md#INFO-011) [INFO-048](../Information/2026-06-06/collected-raw.md#INFO-048) | 16%(v3.99)→17%(v4.00) |
| 2026-06-05 | +1%。围い込み蓄積初期認定+NSA継続利用で围い込み構造強化 | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) | 15%(v3.94)→16%(v3.99) |
| 2026-05-31 | ±0%。SKILL.md 40K+・AAIF 43新メンバー・MCP互換で围い込み否定強力。「勝者」確定の証拠なし | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) | 15%(v3.88以降)→15%(v3.94) |

### §7 ブラインドスポット

- 围い込み形態変化(技術的→契約的・エコシステム的)が起きている場合、技術指標では捉えきれない。
- 中国市場(DeepSeek/ByteDance)での独占形成度は観測できていない。
- API価格下落が一時的な供給過剰か構造的なコモディティ化かの区別が不十分。
- 围い込み6次元分散が「围い込みの強化」か「围い込みの薄化」かの判定が困難。

---

## SCN-002: 技術は開くが勝者は出る (現在確率: 24%)

> 象限: 開放 × 差別化持続

### §0 一文要約

AAIF/MCP等の相互運用標準で移行の自由度は確保されるが、フロンティア差別化はTier 1に集中する構造を指す。現在24%で3位。MCP 97M SDK DL [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021)・agents-cli クロスエージェント [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023)・ADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) は開放方向を強く支持するが、API価格下落トレンド [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) とコーディングスキル40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) が「差別化持続」前提を弱体化。「勝者」の性能定義が希薄化しSCN-004との境界がさらに曖昧化した。

### §1 コア判断

「開放されているが差別化は残る」という世界は、標準化が進む一方でフロンティアの高付加価値が維持される場合に成立する。開放側の証拠は史上最強だ。MCP 97M [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021)、agents-cli クロスエージェント対応 [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023)、ADK OSS [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011)、MAF OSS [INFO-010](../Information/2026-06-05/collected-raw.md#INFO-010) が開放の構造的基盤を構築する。

差別化持続側はさらに弱まった。API価格下落トレンド [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) に加え、Copilot定額→従量制移行 [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) が価格破壊の浸透を示す。コーディングスキル40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) はスキル層での差別化消滅を予測する。Claude Opus 4.8 SWE-bench 88.6% [INFO-017](../Information/2026-06-04/collected-raw.md#INFO-017) は性能競争の存在を示すものの、OSS側の追従速度と価格破壊を考慮すると差別化の持続性は不確定だ。開放の強さと差別化持続の弱さが同時に観測される状況は、SCN-002からSCN-004への移行圧力を意味する。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | MCP 97M+agents-cli+ADK OSS+MAF OSS | 開放軸を支える最も強い構造証拠の蓄積 | A-3 | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) |
| 高 | API価格下落トレンド+Copilot定額→従量制+コーディング40%陳腐化 | 差別化持続の前提を弱体化する価格・スキルの三重圧力 | B-2 | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) |
| 中 | Claude Opus 4.8 SWE-bench 88.6%+Gemini 3 Pro LMArena 1501 | 性能競争の継続を示すが差別化持続の証拠として不十分 | B-2 | [INFO-017](../Information/2026-06-04/collected-raw.md#INFO-017) [INFO-020](../Information/2026-06-05/collected-raw.md#INFO-020) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| OSSモデルのエンタープライズ採用が3社で10%以上のシェアを取る | 「勝者集中」前提が崩れSCN-004が上昇する | 90日 | [IND-004](../config/indicators.json) |
| BenchLM上位3社差が3pt以内に収束する | 「差別化持続」の根拠が消えSCN-004方向の根拠が立つ | 90日 | [IND-001](../config/indicators.json) |
| トークン価格がさらに50%下落し主要プロバイダーの収益性が脅かされる | 差別化持続の経済的基盤が崩れる | 90日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-002-A | AAIF/MCP標準でAI間相互運用が確立する | 72% | MCP 97M+agents-cli+ADK OSS+MAF OSSは開放の構造的蓄積 | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) | (標準競合の可能性) |
| H-SCN-002-B | Tier 1の3社がフロンティア差別化を維持し続ける | 18% | API価格下落+コーディング40%陳腐化+Copilot従量制で差別化維持の経済的根拠が急速に弱まっている | [INFO-017](../Information/2026-06-04/collected-raw.md#INFO-017) | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で高 | Claude Opus 4.8 SWE-bench 88.6%。OSS性能ギャップ消滅方向 | 2026-06-07 |
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用10%超で高 | Nemotron OSS+ADK OSS採用拡大 [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) | 2026-06-07 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | MCP 97M+ADK+MAF。high水準 | 2026-06-07 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-06-07 | ±0%。QHG再定義32R連続未実行。開放強固だが差別化持続弱化で相殺 | QHG再定義32R目 | 24%(v3.95)→24%(v4.01) |
| 2026-06-05 | -1%。Copilot定額→従量制+API価格下落で「勝者」価値プレミアム圧縮 | [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) | 25%(v3.94)→24%(v3.95) |
| 2026-05-31 | ±0%。MCP 97M+AAIF 43新メンバーで開放強力。差別化vsコモディティ化矛盾で相殺 | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) | 25%(v3.94)→25%(v3.94) |
| 2026-05-23 | ±0%。MCP 1,300+で開放強力だが差別化vsコモディティ化矛盾で相殺 | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) | 27%(v3.85)→27%(v3.86) |

### §7 ブラインドスポット

- 「差別化持続」の判定がベンチマークと価格に偏っている。ユーザー体験・信頼性・コンプライアンス等の非価格差別化を観測する指標が不十分。
- 開放エコシステムの拡大(MCP 97M等)が「開放」を意味するか、標準主導者による新しい围い込みを意味するかの区別が困難。
- Tier 1企業の戦略転換(差別化追求から規模追求)が起きた場合、SCN-002からSCN-004への急速な移行を捉えられない可能性がある。

---

## SCN-003: 静かな囲い込み (現在確率: 32%)

> 象限: 閉鎖 × コモディティ化

### §0 一文要約

モデル差別化は薄れるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界を指す。現在32%で最高確率だがSCN-004(27%)との差が5ptに縮小。QHG再定義32R連続未実行で統計的是正が継続。ペンタゴン围い込み構造(Anthropic指定→OpenAI代替) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018)・NSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) は围い込み蓄積。コモディティ化証拠(API価格下落 [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030)・Nemotron OSS [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008))はSCN-003とSCN-004の双方に支持され、SCN-004方向への圧力が強まっている。

### §1 コア判断

このシナリオの構造は「差別化が消えても離れられない」という顧客固定化にある。围い込み側は多様化が続く。ペンタゴン7社機密契約 [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) は政府調達での围い込み。NSA継続利用 [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) は禁止令下でも技術的固定化が続くことを実証する。Anthropic $965B評価額 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) は資本集中を示し、围い込みの物理的基盤を強化する。

コモディティ化側の証拠は確定的だ。API価格下落トレンド [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030)、Nemotron OSS [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008)、コーディングスキル40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) は価格・能力・スキルの三重のコモディティ化圧力。ただしこれらはSCN-003(閉鎖×コモディティ化)とSCN-004(開放×コモディティ化)の双方に等しく支持する。围い込み蓄積がSCN-003特有の支持要因として機能する限り最高確率を維持するが、QHG再定義32R連続未実行で統計的是正が毎ラウンド-1%を適用している。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | API価格下落+Nemotron OSS+コーディング40%陳腐化 | コモディティ化を支える価格・能力・スキルの三重証拠。但しSCN-003/004双方に支持 | B-2 | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) |
| 高 | 围い込み蓄積: ペンタゴン指定+NSA継続+Anthropic $965B | 围い込みが配布・エコシステム・データ・ハードウェア・政府の多次元で進行 | A-1 | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) |
| 高 | QHG再定義32R連続未実行 | ±0%固定化の根本原因。統計的是正で毎ラウンド-1% | (内部) | [scenarios.json](../config/scenarios.json) |
| 中 | 142Kテックレイオフ+Copilot従量制 | エコシステム深度の差が埋まらない限りコモディティ化はSCN-004方向へ | A-1 | [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| 主要企業がMCP上でクロスベンダー切り替えを実証する事例が3件以上公表される | スイッチングコストが低いことが実証され固定化シナリオの根拠が薄まる | 90日 | [IND-017](../config/indicators.json) |
| 围い込みシグナル蓄積のうち4件以上が逆転する | 围い込みの構造的蓄積が止まり確率上昇が止まる | 60日 | [IND-009](../config/indicators.json) [IND-022](../config/indicators.json) |
| トークン価格が底打ちし主要プロバイダーの価格競争が収束する | コモディティ化圧力が減退しSCN-001/002の確率が上昇する | 120日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-003-A | モデルコモディティ化でベンダー差別化は機能から围い込みに移行する | 60% | API価格下落+Nemotron OSS+コーディング陳腐化はコモディティ化の確定的証拠。围い込み蓄積はgenuine | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) |
| H-SCN-003-B | エコシステム統合深度が顧客の移行コストを決定する | 52% | ペンタゴン指定+NSA継続+Anthropic $965Bの蓄積は理論的C。QHG再定義未実行で確度判定が保留 | [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) | (クロスベンダー移行事例不在) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-009](../config/indicators.json) | AI利用規約の制限強化 | 月3件超の制限追加で高 | 围い込み蓄積継続(32件) | 2026-06-07 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | トークン価格50%以上下落で高 | API価格下落トレンド確定 [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) | 2026-06-07 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全社採用で高(反証指標) | MCP 97M+ADK+MAF。high水準 | 2026-06-07 |

### §6 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-06-07 | -1%。QHG再定義32R連続未実行で統計的是正継続。围い込み蓄積はあるがコモディティ化証拠がSCN-004方向への圧力 | QHG再定義32R目+統計的是正 | 33%(v4.00)→32%(v4.01) |
| 2026-06-06 | -1%。围い込み→SCN-001シフト兆候。コモディティ化証拠はSCN-004方向への圧力。QHG再定義31R未実行 | 围い込み蓄積分散分析 | 34%(v3.99)→33%(v4.00) |
| 2026-06-05 | -1%。v3.92自動ペナルティ規則継続。QHG再定義30R未実行が±0%固定化の根本原因 | 自動ペナルティ規則 | 35%(v3.94)→34%(v3.99) |
| 2026-05-31 | -1%。7R連続±0%でv3.92自動ペナルティ規則発動。QHG再定義22R連続未実行 | 自動ペナルティ+[INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) Skill Registry/RAG Engine | 36%(v3.93)→35%(v3.94) |

### §7 ブラインドスポット

- 「スイッチングコストが高い」という観測が実際に顧客が離れられないことの実証ではない。
- 「静かな围い込み」が起きているとすれば顧客はそれを認識していないはずで、認識していない事象をシグナルとして観測することは構造的に困難だ。
- コモディティ化が進行する中で围い込みの価値(囲い込む対象の差別化)自体が低下する矛盾を十分に分析できていない。
- コモディティ化証拠がSCN-003とSCN-004の双方に等しく支持するため、アトラクター効果(現在の最高確率シナリオへの認知バイアス)に注意が必要。
- QHG再定義32R連続未実行は確率更新プロセスの構造的欠陥であり、シナリオ自体の妥当性とは独立した問題。

---

## SCN-004: 誰でもAI (現在確率: 27%)

> 象限: 開放 × コモディティ化

### §0 一文要約

差別化が薄れオープン標準で自由に行き来できる世界を指す。現在27%で2位。v4.01で+1%上昇しSCN-003との差が5ptに縮小。API価格下落トレンド [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) + NVIDIA Nemotron OSS [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) + コーディングスキル40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) + 142Kテックレイオフ [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) がフロンティア差別化の客観的基盤を侵食する四重の証拠。Copilot定額→従量制 [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) は価格破壊の浸透。ただしQ1 $300B投資 [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033) + Anthropic $965B [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) の資本集中が二層市場構造を維持し完全な平準化には至っていない。

### §1 コア判断

SCN-004は「モデルがコモディティ化し、価格も移行コストも消える」という条件が揃う場合に成立する。v4.01でSCN-003との差が5ptに縮小し、コモディティ化+開放方向の証拠はv3.94以降さらに強まった。API価格下落トレンド [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030)、Nemotron OSS [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008)、MCP 97M [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021)、コーディングスキル40%陳腐化 [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) は価格・能力・標準・スキルの四重の圧力。これに142Kテックレイオフ [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) とCopilot定額→従量制 [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) が加わる。

ただしQ1 $300B投資 [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033) とAnthropic $965B評価額 [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) はインフラ集中を示し、二層市場構造の完全解消には至っていない。ペンタゴン7社契約 [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) も政府調達における選別を示す。围い込み蓄積はコモディティ化が進んでもエコシステム深度による差別化が残る可能性(SCN-003)を示唆する。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | API価格下落トレンド+Copilot定額→従量制 | コモディティ化の包括的な価格証拠 | B-2 | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) |
| 高 | Nemotron OSS+コーディングスキル40%陳腐化+142Kレイオフ | 能力・スキル・雇用の三重のコモディティ化証拠 | B-2 | [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) |
| 高 | MCP 97M+ADK OSS+MAF OSS | 開放方向の構造的証拠。移行コスト低下を促進 | A-3 | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) [INFO-010](../Information/2026-06-05/collected-raw.md#INFO-010) |
| 中 | Q1 $300B投資+Anthropic $965B | 資本集中が二層市場構造を維持(反証) | B-2 | [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033) [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) |
| 中 | ペンタゴン7社契約 | 政府調達での選別(反証)。完全な「誰でも」から遠い | A-2 | [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLMの全層間差が5pt以内に収束する | フロンティアの優位性が消えSCN-004が現実的な主シナリオになる | 180日 | [IND-001](../config/indicators.json) |
| OSSモデルのエンタープライス採用シェアが20%を超える | 二層市場の上層も侵食が起きたとみなせる | 180日 | [IND-004](../config/indicators.json) |
| 主要フロンティア企業が価格引き上げに成功する | コモディティ化圧力が需要側の抵抗で減退する | 90日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-004-A | OSSモデルがエンタープライスの主流になる | 32% | API価格下落+Nemotron OSS+コーディング陳腐化は能力・価格の証拠。エンタープライスシェアデータが不足 | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) | [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033) 資本集中 |
| H-SCN-004-B | オープン標準でAIプロバイダー間の移行がほぼコストゼロになる | 40% | MCP 97M+ADK+MAFは基盤。ワークフロー統合深度が移行コストを左右する | [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) | 围い込み蓄積 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用20%超で高 | Nemotron OSS採用拡大(ServiceNow・Accenture・Deloitte・SAP) [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) | 2026-06-07 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | トークン価格50%以上下落で高 | API価格下落トレンド確定 [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) | 2026-06-07 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-06-07 | +1%。API価格下落+Nemotron OSS+コーディング40%陳腐化+142Kレイオフの四重直接支持。保守的上限+1% | [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) | 26%(v4.00)→27%(v4.01) |
| 2026-06-06 | +1%。Copilot定額→従量制+围い込み→SCN-001シフトの再配分 | [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039)+围い込み分散分析 | 25%(v3.94)→26%(v4.00) |
| 2026-05-31 | ±0%。Goldman Sachs $0.18+DeepSeek V4 Pro+MMLU飽和+CEOs安価モデルシフトの四重支持。SCN-002と同率に並ぶ | [INFO-029](../Information/2026-05-31/collected-raw.md#INFO-029)+[INFO-044](../Information/2026-05-31/collected-raw.md#INFO-044) | 23%(v3.93)→25%(v3.94) |
| 2026-05-23 | +1%。SCN-001 -1%再配分。Epoch AI+DeepSeek V4+MCP 1300+arXiv OSSが四重の圧力 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065)+[INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) | 20%(v3.85)→21%(v3.86) |

### §7 ブラインドスポット

- 二層市場(大規模フロンティアユーザーと中小企業のOSSユーザー)が分離した形でSCN-004とSCN-003が共存する可能性を、単一の確率に集約していることで精度が落ちている。
- 中国市場でのOSSダイナミクス(DeepSeek/ByteDance)が西側市場に与えるコモディティ圧力を観測できていない。
- API価格下落が一時的な供給過剰によるものか構造的なコモディティ化によるものかの区別が不十分。
- 豆包有料プロ版 [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) は中国市場でのマネタイズ試行だが、コモディティ化圧力の指標としての評価が不十分。

---

## ブラックスワン: BS-001 AI安全性大事故 (現在確率: 17%)

> 低確率・高影響

### §0 一文要約

AIエージェントの本番障害・大規模セキュリティ事故が複合的に起き、業界全体に規制強化と信頼失墜をもたらす事象を指す。現在17%。RSI「定義された実験ではほぼ超人」 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) が能力-リスク二面性をA-1品質で具体化。ペンタゴン围い込み構造 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) が安全性堅持企業への経済的制裁の前例を示す。142Kテックレイオフ [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) はAI急速導入の副作用。新規A-1脆弱性開示なし。critical移行条件(大規模実被害A-2+報告)未到達。

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| AIエージェントによる金融・インフラへの大規模実害インシデントが公表される | 確率が急上昇し全シナリオの再評価が必要になる | 常時 | [IND-013](../config/indicators.json) |
| 主要国でAIエージェントの本番使用を一時停止させる行政命令が出る | 業界構造が短期に変わりSCN-001〜004の全確率に波及する | 90日 | [IND-030](../config/indicators.json) |
| METR相当の調査でAIコード本番障害率が60%を超える | 攻撃面の拡大が閾値を超えBS-001確率が25%以上に跳ね上がる | 180日 | [IND-013](../config/indicators.json) |

### §7 ブラインドスポット

- RSI「定義された実験ではほぼ超人」 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) はAGI進展を示すが、完全自律ではない。FOOM未到来でも漸進的能力向上がリスクを高める経路の分析が不十分。
- 大事故が起きたときどのシナリオに収束するかの分析を持っていない。
- ペンタゴン围い込み構造 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) が安全性堅持企業を罰し順応企業を報いる構造は、安全投資のインセンティブを低下させる方向に働く。

---

## ブラックスワン: BS-002 量子×AI融合 (現在確率: 3%)

> 低確率・根本的変化

### §0 一文要約

量子コンピューティングとAIの融合が既存の計算パラダイムを変える根本的変化を指す。現在3%。関連する新情報なし。

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| 量子プロセッサを使ったLLM推論がクラシカル計算比で10倍以上の速度を実証する | 確率が段階的に上昇し全シナリオの前提が再評価される | 常時 | (新規IND要) |

### §7 ブラインドスポット

- 量子×AIの進捗を追う指標がない。新規IND設定が要る。
- 3%という確率の根拠が弱い(関連情報なしは確率ゼロに近いとは異なる)。
- 量子進展が急激に起きた場合、全シナリオの前提(計算コスト・資本集中の意味)が同時に崩れる可能性がある。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) | RSI「定義された実験ではほぼ超人」(BS-001能力-リスク二面性 A-1) |
| [INFO-038](../Information/2026-06-07/collected-raw.md#INFO-038) | 142Kテックレイオフ AI#1理由(SCN-004直接支持+BS-001 A-1) |
| [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) | GitHub Copilot定額→従量制(SCN-004直接支持 A-2) |
| [INFO-041](../Information/2026-06-07/collected-raw.md#INFO-041) | コーディングスキル40%陳腐化(SCN-004直接支持 B-2) |
| [INFO-053](../Information/2026-06-07/collected-raw.md#INFO-053) | 豆包有料プロ版(SCN-004中国市場参考 A-2) |
| [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) | NSA継続利用(SCN-003围い込み A-1) |
| [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | ペンタゴンAnthropic指定(SCN-003围い込み+BS-001 A-1) |
| [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) | NVIDIA Nemotron OSS(SCN-004直接支持 A-3) |
| [INFO-011](../Information/2026-06-07/collected-raw.md#INFO-011) | Google ADK OSS(SCN-002/004開放支持 A-3) |
| [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) | API価格下落トレンド(SCN-004直接支持 B-2) |
| [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) | MCP 97M SDK DL(SCN-001/002開放支持 A-2) |
| [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) | agents-cli クロスエージェント(SCN-002/004開放支持 A-3) |
| [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) | Anthropic $965B評価額(SCN-003資本集中 A-1) |
| [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | Google I/O 2026 基調講演(SCN-003围い込み A-3) |
| [INFO-004](../Information/2026-06-06/collected-raw.md#INFO-004) | OpenAI on AWS Bedrock(SCN-002開放支持 A-3) |
| [INFO-033](../Information/2026-06-07/collected-raw.md#INFO-033) | Q1 $300B投資(SCN-004反証 B-2) |
| [INFO-001](../Information/2026-06-07/collected-raw.md#INFO-001) | KPMG 276,000人Claude展開(SCN-001围い込み A-3) |
| [INFO-002](../Information/2026-06-07/collected-raw.md#INFO-002) | Anthropic-SpaceX 300MW契約(SCN-001围い込み A-3) |
| [INFO-006](../Information/2026-06-07/collected-raw.md#INFO-006) | Gemini Enterprise Agent Platform(SCN-003围い込み A-3) |
| [INFO-020](../Information/2026-06-07/collected-raw.md#INFO-020) | ペンタゴン7社機密契約(SCN-003围い込み A-2) |
| [Arbiter v4.01](../state/arbiter-2026-06-07.md) | 確率更新の完全根拠(付録のみ参照) |
