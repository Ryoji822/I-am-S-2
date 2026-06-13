# シナリオ追跡 — 静的インテリジェンス

> 最終判断更新: 2026-06-13
> 全体確信度: 中
> 主参照: [scenarios.json](../config/scenarios.json), [indicators.json](../config/indicators.json)
> Arbiter: v4.07

---

## 確率推移サマリ

過去20日の確率推移。主軸4シナリオ + Black Swan 2件。v4.07でSCN-004(30%)がSCN-003(29%)を逆転し1位に浮上。06-08から06-10の3日間でSCN-003は32%→29%(-3%)、SCN-004は27%→30%(+3%)の順位逆転が起きた。コモディティ化証拠の蓄積(価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071)・LLM API 600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041)・OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062))がSCN-004を押し上げ、围い込み蓄積の減速とQHG 33R+連続未実行による統計的是正がSCN-003を押し下げた。Fable 5/Mythos 5 [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) の政府/インフラ向け二層リリースモデルは新規围い込みパターンだが、現フレームワークでの捕捉が不十分。SCN-001(17%)・SCN-002(24%)・BS-001(17%)・BS-002(3%)は06-08以降±0%で凍結。SCN-003/004の差は1%で誤差範囲内、事実上識別不能。

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|:-------:|:-------:|:-------:|:-------:|:------:|:------:|
| 2026-06-13 | 17% | 24% | 29% | 30% | 17% | 3% |
| 2026-06-12 | 17% | 24% | 29% | 30% | 17% | 3% |
| 2026-06-11 | 17% | 24% | 29% | 30% | 17% | 3% |
| 2026-06-10 | 17% | 24% | 29% | 30% | 17% | 3% |
| 2026-06-09 | 17% | 24% | 30% | 29% | 17% | 3% |
| 2026-06-08 | 17% | 24% | 31% | 28% | 17% | 3% |
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

v4.07でSCN-004(30%, +3)がSCN-003(29%, -3)を逆転した。06-08から06-10の3日間で1日1ptずつSCN-003が下がりSCN-004が上がった構造的順位逆転。コモディティ化証拠(価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061)・[INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071)・600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041)・OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062))はSCN-003とSCN-004の双方に支持されるが、围い込み蓄積の減速(Fable 5 Glasswing [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) とNSA Mythos carve-out [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) は围い込み証拠だが量的蓄積は鈍化)とQHG 33R+連続未実行による統計的是正がSCN-003を押し下げた。MCP RC [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) はSCN-002/004の開放方向を強化。Fable 5/Mythos 5の公開+政府二層モデルは围い込みの新パターンだが現フレームワークの围い込み指標で未分類。Google $35Bチップ契約 [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037)・OpenAI IPO急ぎ [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038)・China $295B計画 [INFO-040](../Information/2026-06-13/collected-040) は資本集中の加速を示すが、SCN-003の围い込み構造への直結は不確定。Claude Code 80%+コード [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) はRSI証拠(BS-001)だが、Fable 5セーフガード [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) とNSPM-11制度化 [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) が抑制要因。

---

## 2つの軸の意味

X軸(開放/閉鎖)はAIの実行環境・データ・標準がどれだけ可搬かを問う。MCP RC [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016)・AAIF 6ヶ月レビュー・ADK OSS [INFO-011](../Information/2026-06-13/collected-raw.md#INFO-011) は開放方向。Fable 5 Glasswing政府/インフラアクセス [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001)・NSA Mythos carve-out [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001)・Google $35Bチップ契約 [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) は閉鎖方向。Y軸(差別化持続/コモディティ化)はフロンティアモデルの高付加価値が維持されるか、価格・能力の平準化でコモディティ化するかを問う。価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061)・[INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071)・LLM API 600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041)・OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) はコモディティ化方向の構造的証拠。Fable 5/Mythos 5 SOTA [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) はフロンティア差別化の維持を示すが、コモディティ化圧力が差別化の経済的価値を侵食する矛盾が深まっている。Google $35B [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037)・OpenAI IPO [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038)・China $295B [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) は国家・市場レベルでの資本集中の加速を示すが、差別化持続には直結しない。

---

## SCN-001: 囲い込みの勝者 (現在確率: 17%)

> 象限: 閉鎖 × 差別化持続

### §0 一文要約

1-2社がフロンティア差別化を維持しつつ実行環境・データ・ガバナンスで囲い込む世界を指す。現在17%で4位。Fable 5/Mythos 5のGlasswing政府/インフラアクセス [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) は围い込みの新次元(公的部門専用モデル層)。Google $35Bチップ契約 [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) はハードウェア資本围い込み。但しMCP RC [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016)・AAIF・ADK OSSが開放方向を継続。「勝者」の確定には至っていない。06-08以降±0%。QHG 33R+連続未実行で凍結。

### §1 コア判断

このシナリオは「フロンティア差別化の持続と生態系封鎖が同時に起きる」という条件に依存する。围い込み側は新次元を獲得した。Fable 5 Glasswing [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) は政府・インフラ向け専用アクセス層を提供し、公的部門での围い込みを具体化する。Google $35Bチップ契約 [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) はハードウェアサプライチェーンの垂直統合を加速させる。

差別化持続側は依然として弱い。LLM API 600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) は価格面での差別化が困難であることを示す。OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) はオープン層の性能がフロンティアに肉薄する証拠。围い込みの形態は多様化したが、MCP RC [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) が開放標準の制度化を進め、封鎖前提を弱体化させる。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | Fable 5 Glasswing政府/インフラアクセス | 围い込みの新次元。公的部門専用モデル層 | A-3 | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) |
| 高 | Google $35Bチップ契約 | ハードウェア資本围い込みの加速 | A-3 | [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) |
| 高 | MCP RC+ADK OSS+AAIF | 開放方向の構造的蓄積。封鎖前提の弱体化 | A-3 | [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) [INFO-011](../Information/2026-06-13/collected-raw.md#INFO-011) |
| 高 | LLM API 600倍価格格差+OSS 3モデルGPT-4超え | 差別化持続の前提を価格・能力面で侵食 | B-2 | [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) |

### §3 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLM上位1社と2位以下の差が20pt以上に拡大 | 差別化持続の前提が成立し始める | 90日 | [IND-001](../config/indicators.json) |
| 有力2社がクロスクラウド撤退し自社基盤のみに移行 | 相互依存構造が解体され封鎖化が進む | 180日 | [IND-018](../config/indicators.json) |
| 政府・規制当局がAI市場での独占を認める判断を下す | 競争法的制約が外れ围い込みに外部制動がなくなる | 180日 | [IND-023](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-001-A | フロンティア差別化が顧客ロックインの主因になる | 12% | 围い込み蓄積はあるがAPI価格下落+OSS追従で金銭的価値が低下 | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) | [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) |
| H-SCN-001-B | 1-2社がエコシステムを垂直統合し他社の参入を封じる | 14% | MCP RC+ADK OSSで開放蓄積。封鎖兆候は次元拡大のみ | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) | [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) [INFO-011](../Information/2026-06-13/collected-raw.md#INFO-011) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク非連続ジャンプ | +10pt以上/期で高 | OSS性能ギャップ消滅方向 | 2026-06-13 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | MCP RC+ADK OSS+AAIF。high水準 | 2026-06-13 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-06-13 | ±0%。QHG 33R+連続未実行で凍結。Fable 5 Glasswingは围い込み新次元だが統計的是正対象外 | QHG 33R+連続目 | 17%(v4.01)→17%(v4.07) |
| 2026-06-07 | ±0%。QHG再定義32R連続未実行。围い込み蓄積は継続するが統計的是正対象外 | QHG再定義32R目 | 17%(v4.00)→17%(v4.01) |
| 2026-06-06 | +1%。围い込みI 32件蓄積+次元拡大(ハードウェア: Googlebook・決済: Daybreak予告・SaaS: Workday統合) | 围い込み蓄積分散分析 | 16%(v3.99)→17%(v4.00) |
| 2026-06-05 | +1%。围い込み蓄積初期認定+NSA継続利用で围い込み構造強化 | [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) | 15%(v3.94)→16%(v3.99) |

### §7 ブラインドスポット

- 围い込み形態変化(技術的→契約的・エコシステム的)が起きている場合、技術指標では捉えきれない。
- Fable 5/Mythos 5の公開+政府二層リリースモデルは新規围い込みパターンだが、現フレームワークの围い込み指標で未分類。
- 中国市場(DeepSeek/ByteDance)での独占形成度は観測できていない。
- API価格下落が一時的な供給過剰か構造的なコモディティ化かの区別が不十分。
- 围い込み多次元分散が「围い込みの強化」か「围い込みの薄化」かの判定が困難。

---

## SCN-002: 技術は開くが勝者は出る (現在確率: 24%)

> 象限: 開放 × 差別化持続

### §0 一文要約

AAIF/MCP等の相互運用標準で移行の自由度は確保されるが、フロンティア差別化はTier 1に集中する構造を指す。現在24%で3位。MCP RC [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) は開放方向を強く支持。AAIF 6ヶ月レビューで開放標準の制度化が進行。但し価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061)・[INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071) とLLM API 600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) が「差別化持続」前提を弱体化。Fable 5 SOTA [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) はフロンティア差別化の維持を示すが経済的価値は圧縮中。06-08以降±0%。QHG凍結。

### §1 コア判断

「開放されているが差別化は残る」という世界は、標準化が進む一方でフロンティアの高付加価値が維持される場合に成立する。開放側の証拠は史上最強だ。MCP RC [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) は相互運用プロトコルの正式リリース候補であり、開放の制度化を確定させる。AAIF 6ヶ月レビューは標準の継続的改善を示す。ADK OSSがエコシステムの開放基盤を維持する。

差別化持続側はさらに弱まった。価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061)・[INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071) はAPI価格の構造的破壊を示す。LLM API 600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) はプロバイダー間の価格離散が極大化しており、最安値への収束圧力が強い。OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) はオープン層の性能がフロンティアに肉薄する証拠。Fable 5 SOTA [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) は性能競争の存在を示すが、価格破壊とOSS追従の速度を考慮すると差別化の持続性は不確定だ。開放の強さと差別化持続の弱さが同時に観測される状況は、SCN-002からSCN-004への移行圧力を意味する。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | MCP RC+AAIF 6ヶ月レビュー+ADK OSS | 開放軸を支える最も強い構造証拠の蓄積。制度化が確定 | A-3 | [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) [INFO-011](../Information/2026-06-13/collected-raw.md#INFO-011) |
| 高 | 価格戦争+600倍価格格差+OSS 3モデルGPT-4超え | 差別化持続の前提を弱体化する価格・能力の三重圧力 | B-2 | [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) |
| 中 | Fable 5/Mythos 5 SOTA | 性能競争の継続を示すが差別化持続の経済的証拠として不十分 | B-2 | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| OSSモデルのエンタープライズ採用が3社で10%以上のシェアを取る | 「勝者集中」前提が崩れSCN-004が上昇する | 90日 | [IND-004](../config/indicators.json) |
| BenchLM上位3社差が3pt以内に収束する | 「差別化持続」の根拠が消えSCN-004方向の根拠が立つ | 90日 | [IND-001](../config/indicators.json) |
| トークン価格がさらに50%下落し主要プロバイダーの収益性が脅かされる | 差別化持続の経済的基盤が崩れる | 90日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-002-A | AAIF/MCP標準でAI間相互運用が確立する | 75% | MCP RC+AAIF+ADK OSSは開放の構造的蓄積。制度化が確定 | [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) | (標準競合の可能性) |
| H-SCN-002-B | Tier 1の3社がフロンティア差別化を維持し続ける | 15% | 価格戦争+600倍格差+OSS追従で差別化維持の経済的根拠が急速に弱まっている | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) | [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で高 | Fable 5 SOTAだがOSS性能ギャップ消滅方向 | 2026-06-13 |
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用10%超で高 | OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) | 2026-06-13 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | MCP RC+ADK+AAIF。high水準 | 2026-06-13 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-06-13 | ±0%。QHG 33R+連続未実行で凍結。MCP RCは開放強化だが価格戦争で差別化弱化。相殺 | QHG 33R+連続目 | 24%(v4.01)→24%(v4.07) |
| 2026-06-07 | ±0%。QHG再定義32R連続未実行。開放強固だが差別化持続弱化で相殺 | QHG再定義32R目 | 24%(v3.95)→24%(v4.01) |
| 2026-06-05 | -1%。Copilot定額→従量制+API価格下落で「勝者」価値プレミアム圧縮 | API価格破壊 | 25%(v3.94)→24%(v3.95) |
| 2026-05-31 | ±0%。MCP 97M+AAIF 43新メンバーで開放強力。差別化vsコモディティ化矛盾で相殺 | AAIF拡大 | 25%(v3.94)→25%(v3.94) |

### §7 ブラインドスポット

- 「差別化持続」の判定がベンチマークと価格に偏っている。ユーザー体験・信頼性・コンプライアンス等の非価格差別化を観測する指標が不十分。
- 開放エコシステムの拡大(MCP等)が「開放」を意味するか、標準主導者による新しい围い込みを意味するかの区別が困難。
- Tier 1企業の戦略転換(差別化追求から規模追求)が起きた場合、SCN-002からSCN-004への急速な移行を捉えられない可能性がある。

---

## SCN-003: 静かな囲い込み (現在確率: 29%)

> 象限: 閉鎖 × コモディティ化

### §0 一文要約

モデル差別化は薄れるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界を指す。現在29%で2位。06-08から06-10の3日間で32%→29%に低下しSCN-004に逆転された。QHG 33R+連続未実行で統計的是正が06-08から06-10に毎日-1%を適用。Fable 5 Glasswing政府/インフラアクセス [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) とNSA Mythos carve-out [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) は围い込み証拠。Google $35Bチップ契約 [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) は資本围い込み。但しコモディティ化証拠(価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061)・[INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071)・600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041))はSCN-003とSCN-004の双方に等しく支持され、围い込み蓄積の減速と合わせてSCN-004方向への圧力が強まっている。

### §1 コア判断

このシナリオの構造は「差別化が消えても離れられない」という顧客固定化にある。围い込み側は新次元を獲得した。Fable 5 Glasswing [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) は政府・インフラ向け専用アクセス層という新围い込みパターン。NSA Mythos carve-outは政府調達での围い込み継続。Google $35Bチップ契約 [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) はインフラの垂直統合を加速。OpenAI IPO急ぎ [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038) も資本集中の一環。

コモディティ化側の証拠は確定的だ。価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061)・[INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071)、LLM API 600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041)、OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) は価格・能力の多重的コモディティ化圧力。ただしこれらはSCN-003(閉鎖×コモディティ化)とSCN-004(開放×コモディティ化)の双方に等しく支持する。围い込み蓄積がSCN-003特有の支持要因として機能する限りSCN-004との差は維持されるが、围い込み蓄積の量的鈍化とQHG統計的是正がSCN-003を押し下げた。現在SCN-004との差は1%で誤差範囲内。事実上識別不能。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | 価格戦争+600倍価格格差+OSS 3モデルGPT-4超え | コモディティ化を支える価格・能力の多重的証拠。SCN-003/004双方に支持 | B-2 | [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) |
| 高 | Fable 5 Glasswing+NSA Mythos carve-out+Google $35Bチップ | 围い込みの新次元(公的部門専用層)と資本集中の加速 | A-3 | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) |
| 高 | QHG 33R+連続未実行 | ±0%固定化の根本原因。統計的是正で毎ラウンド-1% | (内部) | [scenarios.json](../config/scenarios.json) |
| 中 | OpenAI IPO急ぎ+China $295B計画 | 資本集中は围い込みを強化するが、コモディティ化圧力との矛盾が深まる | A-3 | [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| 主要企業がMCP上でクロスベンダー切り替えを実証する事例が3件以上公表される | スイッチングコストが低いことが実証され固定化シナリオの根拠が薄まる | 90日 | [IND-017](../config/indicators.json) |
| 围い込みシグナル蓄積のうち4件以上が逆転する | 围い込みの構造的蓄積が止まり確率上昇が止まる | 60日 | [IND-009](../config/indicators.json) [IND-022](../config/indicators.json) |
| トークン価格が底打ちし主要プロバイダーの価格競争が収束する | コモディティ化圧力が減退しSCN-001/002の確率が上昇する | 120日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-003-A | モデルコモディティ化でベンダー差別化は機能から围い込みに移行する | 55% | 価格戦争+OSS追従はコモディティ化の確定的証拠。围い込み蓄積はgenuineだが量的鈍化 | [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) | [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) |
| H-SCN-003-B | エコシステム統合深度が顧客の移行コストを決定する | 48% | Fable 5 Glasswing+Google $35Bの蓄積は理論的根拠。QHG 33R+未実行で確度判定が保留 | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) | (クロスベンダー移行事例不在) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-009](../config/indicators.json) | AI利用規約の制限強化 | 月3件超の制限追加で高 | 围い込み蓄積継続だが量的鈍化 | 2026-06-13 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | トークン価格50%以上下落で高 | 価格戦争+600倍格差で確定 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) | 2026-06-13 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全社採用で高(反証指標) | MCP RC+ADK+AAIF。high水準 | 2026-06-13 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-06-13 | ±0%。QHG 33R+連続未実行。围い込み新次元あるがコモディティ化証拠がSCN-004方向へ。06-10以降凍結 | QHG 33R+連続目 | 29%(v4.04)→29%(v4.07) |
| 2026-06-10 | -1%。QHG統計的是正3日連続。围い込み蓄積鈍化+コモディティ化証拠蓄積でSCN-004に逆転される | QHG統計的是正+围い込み鈍化 | 30%(v4.03)→29%(v4.04) |
| 2026-06-09 | -1%。QHG統計的是正2日連続。コモディティ化証拠がSCN-004に片寄り | QHG統計的是正 | 31%(v4.02)→30%(v4.03) |
| 2026-06-08 | -1%。QHG統計的是正開始。围い込み蓄積鈍化+コモディティ化証拠蓄積 | QHG 33R目統計的是正 | 32%(v4.01)→31%(v4.02) |
| 2026-06-07 | -1%。QHG再定義32R連続未実行で統計的是正継続 | QHG再定義32R目 | 33%(v4.00)→32%(v4.01) |

### §7 ブラインドスポット

- 「スイッチングコストが高い」という観測が実際に顧客が離れられないことの実証ではない。
- 「静かな围い込み」が起きているとすれば顧客はそれを認識していないはずで、認識していない事象をシグナルとして観測することは構造的に困難だ。
- コモディティ化が進行する中で围い込みの価値(囲い込む対象の差別化)自体が低下する矛盾を十分に分析できていない。
- コモディティ化証拠がSCN-003とSCN-004の双方に等しく支持するため、アトラクター効果(元最高確率シナリオへの認知バイアス)に注意が必要。
- QHG 33R+連続未実行は確率更新プロセスの構造的欠陥であり、シナリオ自体の妥当性とは独立した問題。
- SCN-003/004の差が1%で誤差範囲内。事実上識別不能なのに順位付けしていること自体が分析的限界を示す。

---

## SCN-004: 誰でもAI (現在確率: 30%)

> 象限: 開放 × コモディティ化

### §0 一文要約

差別化が薄れオープン標準で自由に行き来できる世界を指す。現在30%で1位。06-08から06-10の3日間で27%→30%に上昇しSCN-003を逆転した。価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061)・[INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071) + LLM API 600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) + OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) + MCP RC [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) がコモディティ化+開放の五重の直接支持。但しGoogle $35Bチップ契約 [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) + OpenAI IPO [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038) + China $295B計画 [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) の資本集中が二層市場構造を維持し、完全な平準化には至っていない。

### §1 コア判断

SCN-004は「モデルがコモディティ化し、価格も移行コストも消える」という条件が揃う場合に成立する。v4.07でSCN-003を逆転し1位に浮上。コモディティ化+開放方向の証拠はv4.01以降さらに強まった。価格戦争 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061)・[INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071)、LLM API 600倍価格格差 [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041)、OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) は価格・能力の多重的圧力。MCP RC [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) は移行コスト低下の制度化を確定させる。

ただしGoogle $35Bチップ契約 [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) とOpenAI IPO [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038) はインフラ集中を示し、二層市場構造の完全解消には至っていない。China $295B計画 [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) は国家レベルでの資本投入であり、完全な「誰でも」の阻害要因。Fable 5 Glasswing [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) は政府/インフラでの围い込みを示し、一部セグメントでのコモディティ化抵抗を意味する。SCN-004が1位になったものの、SCN-003との差は1%で誤差範囲内。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | 価格戦争+600倍価格格差 | コモディティ化の包括的な価格証拠 | B-2 | [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071) [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) |
| 高 | OSS 3モデルGPT-4超え | 能力面でのコモディティ化証拠。フロンティア差別化の客観的基盤を侵食 | B-2 | [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) |
| 高 | MCP RC | 開放方向の制度化。移行コスト低下を促進 | A-3 | [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) |
| 中 | Google $35Bチップ+OpenAI IPO+China $295B | 資本集中が二層市場構造を維持(反証) | B-2 | [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038) [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) |
| 中 | Fable 5 Glasswing政府/インフラアクセス | 政府・インフラセグメントでの围い込み(反証)。「誰でも」の境界限定 | A-3 | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLMの全層間差が5pt以内に収束する | フロンティアの優位性が消えSCN-004が現実的な主シナリオになる | 180日 | [IND-001](../config/indicators.json) |
| OSSモデルのエンタープライス採用シェアが20%を超える | 二層市場の上層も侵食が起きたとみなせる | 180日 | [IND-004](../config/indicators.json) |
| 主要フロンティア企業が価格引き上げに成功する | コモディティ化圧力が需要側の抵抗で減退する | 90日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-004-A | OSSモデルがエンタープライスの主流になる | 38% | 価格戦争+OSS GPT-4超えは能力・価格の証拠。エンタープライスシェアデータが不足 | [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) | [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) 資本集中 |
| H-SCN-004-B | オープン標準でAIプロバイダー間の移行がほぼコストゼロになる | 45% | MCP RCは制度化の確定。ワークフロー統合深度が移行コストを左右する | [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) | [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) 围い込み新次元 |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用20%超で高 | OSS 3モデルGPT-4超え [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) | 2026-06-13 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | トークン価格50%以上下落で高 | 価格戦争+600倍格差で確定 [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) | 2026-06-13 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-06-13 | ±0%。QHG 33R+連続未実行で凍結。コモディティ化証拠蓄積だが資本集中も維持。06-10以降±0% | QHG 33R+連続目 | 30%(v4.04)→30%(v4.07) |
| 2026-06-10 | +1%。SCN-003逆転達成。QHG統計的是正3日目+コモディティ化証拠蓄積。SCN-003と同率→超え | QHG統計的是正+コモディティ化蓄積 | 29%(v4.03)→30%(v4.04) |
| 2026-06-09 | +1%。QHG統計的是正2日連続。コモディティ化証拠が蓄積。SCN-003に1pt差まで接近 | QHG統計的是正 | 28%(v4.02)→29%(v4.03) |
| 2026-06-08 | +1%。QHG統計的是正開始。コモディティ化証拠蓄積でSCN-003からの再配分開始 | QHG 33R目統計的是正 | 27%(v4.01)→28%(v4.02) |
| 2026-06-07 | +1%。API価格下落+Nemotron OSS+コーディング40%陳腐化+142Kレイオフの四重直接支持 | コモディティ化四重証拠 | 26%(v4.00)→27%(v4.01) |

### §7 ブラインドスポット

- 二層市場(大規模フロンティアユーザーと中小企業のOSSユーザー)が分離した形でSCN-004とSCN-003が共存する可能性を、単一の確率に集約していることで精度が落ちている。
- 中国市場でのOSSダイナミクス(DeepSeek/ByteDance)が西側市場に与えるコモディティ圧力を観測できていない。
- API価格下落が一時的な供給過剰によるものか構造的なコモディティ化によるものかの区別が不十分。
- SCN-003/004の差が1%で誤差範囲内。事実上識別不能なのに順位付けしていること自体が分析的限界を示す。
- 資本集中($35Bチップ・IPO・$295B国家計画)が二層市場構造を維持する場合、SCN-004の「誰でも」は実質的に「コモディティ層の誰でも」に限定される可能性がある。

---

## ブラックスワン: BS-001 AI安全性大事故 (現在確率: 17%)

> 低確率・高影響

### §0 一文要約

AIエージェントの本番障害・大規模セキュリティ事故が複合的に起き、業界全体に規制強化と信頼失墜をもたらす事象を指す。現在17%。RSI部分的加速 [INFO-059](../Information/2026-06-13/collected-raw.md#INFO-059)・Claude Code 80%+コード [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) はRSI証拠。Fable 5セーフガード [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001)・NSPM-11制度化 [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) は抑制要因。新規A-2大規模実被害報告なし。critical移行条件未到達。

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| AIエージェントによる金融・インフラへの大規模実害インシデントが公表される | 確率が急上昇し全シナリオの再評価が必要になる | 常時 | [IND-013](../config/indicators.json) |
| 主要国でAIエージェントの本番使用を一時停止させる行政命令が出る | 業界構造が短期に変わりSCN-001〜004の全確率に波及する | 90日 | [IND-030](../config/indicators.json) |
| METR相当の調査でAIコード本番障害率が60%を超える | 攻撃面の拡大が閾値を超えBS-001確率が25%以上に跳ね上がる | 180日 | [IND-013](../config/indicators.json) |

### §7 ブラインドスポット

- RSI部分的加速 [INFO-059](../Information/2026-06-13/collected-raw.md#INFO-059) とClaude Code 80%+ [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) は能力向上を示すが、完全自律ではない。FOOM未到来でも漸進的能力向上がリスクを高める経路の分析が不十分。
- 大事故が起きたときどのシナリオに収束するかの分析を持っていない。
- Fable 5セーフガード [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) とNSPM-11制度化 [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) は安全投資の前進だが、ペンタゴン围い込み構造が安全性堅持企業への経済的制裁の前例を示す点でインセンティブ構造の矛盾が続く。

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
| [INFO-001](../Information/2026-06-13/collected-raw.md#INFO-001) | Fable 5/Mythos 5 SOTA+Glasswing政府/インフラアクセス(SCN-001/003围い込み A-3) |
| [INFO-016](../Information/2026-06-13/collected-raw.md#INFO-016) | MCP RC(SCN-002/004開放支持 B-3) |
| [INFO-037](../Information/2026-06-13/collected-raw.md#INFO-037) | Google $35Bチップ契約(SCN-001/003資本围い込み A-3) |
| [INFO-038](../Information/2026-06-13/collected-raw.md#INFO-038) | OpenAI IPO急ぎ(SCN-003資本集中 A-3) |
| [INFO-040](../Information/2026-06-13/collected-raw.md#INFO-040) | China $295B計画(SCN-003国家围い込み A-3) |
| [INFO-041](../Information/2026-06-13/collected-raw.md#INFO-041) | LLM API 600倍価格格差(SCN-004直接支持 C-3) |
| [INFO-059](../Information/2026-06-13/collected-raw.md#INFO-059) | RSI部分的加速(BS-001 A-3) |
| [INFO-061](../Information/2026-06-13/collected-raw.md#INFO-061) | 価格戦争(SCN-004直接支持 B-3) |
| [INFO-062](../Information/2026-06-13/collected-raw.md#INFO-062) | OSS 3モデルGPT-4超え(SCN-004直接支持 B-2) |
| [INFO-071](../Information/2026-06-13/collected-raw.md#INFO-071) | 価格戦争詳細(SCN-004直接支持 B-3) |
| [INFO-073](../Information/2026-06-13/collected-raw.md#INFO-073) | Claude Code 80%+コード(BS-001 RSI証拠 A-3) |
| [INFO-026](../Information/2026-06-13/collected-raw.md#INFO-026) | NSPM-11制度化(BS-001抑制要因 A-2) |
| [INFO-011](../Information/2026-06-13/collected-raw.md#INFO-011) | Google ADK OSS(SCN-002/004開放支持 A-3) |
| [INFO-021](../Information/2026-06-06/collected-raw.md#INFO-021) | MCP 97M SDK DL(SCN-001/002開放支持 A-2) |
| [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) | agents-cli クロスエージェント(SCN-002/004開放支持 A-3) |
| [INFO-039](../Information/2026-06-06/collected-raw.md#INFO-039) | Anthropic $965B評価額(SCN-003資本集中 A-1) |
| [INFO-008](../Information/2026-06-07/collected-raw.md#INFO-008) | NVIDIA Nemotron OSS(SCN-004直接支持 A-3) |
| [INFO-030](../Information/2026-06-07/collected-raw.md#INFO-030) | API価格下落トレンド(SCN-004直接支持 B-2) |
| [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | ペンタゴンAnthropic指定(SCN-003围い込み+BS-001 A-1) |
| [INFO-019](../Information/2026-06-07/collected-raw.md#INFO-019) | NSA継続利用(SCN-003围い込み A-1) |
| [Arbiter v4.07](../state/arbiter-2026-06-13.md) | 確率更新の完全根拠(付録のみ参照) |
