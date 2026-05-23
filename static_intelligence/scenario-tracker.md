# シナリオ追跡 — 静的インテリジェンス

> 最終判断更新: 2026-05-23
> 全体確信度: 中
> 主参照: scenarios.json, indicators.json#IND-001/004/009/011/013/017/027/030
> Arbiter: v3.86

---

## 確率推移サマリ

過去21日の確率推移。主軸4シナリオ + Black Swan 2件。v3.86でSCN-001(16%, -1)がEpoch AI価格コモディティ化(9x-900x/年) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) で围い込み価値基盤を侵食され過去最低。SCN-004(21%, +1)がSCN-001 -1%の再配分を受け、コモディティ化+開放方向の趨勢がさらに強まった。SCN-003(36%)が最高確率を維持。

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|:-------:|:-------:|:-------:|:-------:|:------:|:------:|
| 2026-05-23 | 16% | 27% | 36% | 21% | 17% | 3% |
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
| 2026-05-03 | 20% | 41% | 26% | 14% | 16% | 3% |
| 2026-05-02 | 20% | 42% | 25% | 13% | 16% | 3% |
| 2026-05-01 | 20% | 43% | 24% | 13% | 16% | 3% |

v3.86でSCN-001(16%, -1)がEpoch AI推論価格9x-900x/年下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) で围い込み価値基盤(差別化持続)を構造的に侵食。SCN-004(21%, +1)はSCN-001 -1%の再配分で上昇。Epoch AI価格データ [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065)、DeepSeek V4 OSS [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062)、MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021)、arXiv OSS商用競合 [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) がSCN-004を押し上げる四重の圧力。SCN-003(36%, ±0)は围い込み蓄積がgenuine支持だが、「10x production problem」 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) による围い込み支持は論理的飛躍(Jevons paradox歴史比較必要)とArbiterが判断。コモディティ化証拠はSCN-003/004双方に等しく支持。SCN-002(27%, ±0)はMCP 1,300+ [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) で開放は強力だが、フロンティア差別化 vs コモディティ化の矛盾で不確実性増大。BS-001(17%, ±0)は上昇圧力(88%インシデント [INFO-016](../Information/2026-05-23/collected-raw.md#INFO-016)+Pentagon武器化 [INFO-039](../Information/2026-05-23/collected-raw.md#INFO-039)+Fortune 500 10%ガバナンス [INFO-030](../Information/2026-05-23/collected-raw.md#INFO-030))vs低下圧力(RAMPART [INFO-024](../Information/2026-05-23/collected-raw.md#INFO-024)+1Password [INFO-020](../Information/2026-05-23/collected-raw.md#INFO-020)+Glasswing [INFO-003](../Information/2026-05-23/collected-raw.md#INFO-003))。相殺。

---

## 2つの軸の意味

X軸(開放/閉鎖)は、AIの実行環境・データ・標準がどれだけ可搬かを問う。MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021)、Confluent MCP GA [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023)、Chrome DevTools for Agents v1 [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022)、Hugging Face Open Agent Leaderboard [INFO-049](../Information/2026-05-23/collected-raw.md#INFO-049) は「開放」方向。Google I/O 100件「全テック企業に宣戦布告」 [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067)、ペンタゴン7社機密契約 [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038)、Anthropic-Stainless買収 [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) は「閉鎖」方向。Y軸(差別化持続/コモディティ化)は、フロンティアモデルの高付加価値が維持されるか、価格・能力の平準化でコモディティ化するかを問う(v3.84再定義)。Epoch AI推論価格9x-900x/年下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) と「10x production problem」は「コモディティ化」方向の決定的証拠。arXiv OSS商用競合 [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) は知識ベンチマークでオープン・クローズド間ギャップが事実上ゼロと報告。Goldman Sachs 66GW [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) とBig Tech $420B [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) は資本集中を示すが、差別化持続には直結しない。

---

## SCN-001: 囲い込みの勝者 (現在確率: 16%)

> 象限: 閉鎖 × 差別化持続

### §0 一文要約

1-2社がフロンティア差別化を維持しつつ実行環境・データ・ガバナンスで囲い込む世界を指すが、現在確率は16%で4位。Epoch AI推論価格9x-900x/年下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) が围い込み価値基盤(差別化持続)を構造的に侵食。MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) とarXiv OSS商用競合 [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) が封鎖・差別化の両前提をさらに弱体化。Google I/O 100件 [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) の围い込み圧力は強いが、価格破壊がその差別化根拠を蝕む構造的矛盾がある。

### §1 コア判断

このシナリオは「フロンティア差別化の持続と生態系封鎖が同時に起きる」という条件に依存する。現在、両条件はさらに弱まった。

差別化持続側では、Epoch AIが同等性能での推論価格が年9x-900x下落していると報告し [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065)、価格面での差別化が構造的に困難になった。DeepSeek V4 OSS [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) とarXiv研究によるオープンウェイトLLM商用競合 [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) がオープン層の性能を押し上げる。Erdős予想反証 [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) はフロンティアの数学的推論能力を示すが、これは汎用推論モデルによる成果であり、特定企業の持続的優位とは直結しない。

封鎖側では、MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021)、Confluent MCP GA [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023)、Chrome DevTools for Agents [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) が開放方向の構造的証拠として蓄積する。围い込み否定は継続し、開放C証拠の蓄積が進む。封鎖が進むというより標準化とOSS普及が進むと解釈すべき段階に入っている。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | Epoch AI推論価格9x-900x/年下落。同等性能での価格崩壊 | 差別化持続の前提が価格面で構造的に崩れる最も強力な観測 | B-3 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) |
| 高 | MCP 1,300本番サーバー+Confluent GA+Chrome DevTools for Agents | 開放Cの構造的蓄積。封鎖前提がさらに弱体化 | C-3 | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023) [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) |
| 高 | arXiv OSS商用API競合: 知識ベンチマークギャップ事実上ゼロ | OSS層の性能が商用層に追いつき差別化根拠が消滅 | B-3 | [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) |
| 中 | Google I/O 100件: Antigravity 2.0+Managed Agents+Spark | 围い込み方向の強い証拠だが、価格破壊と矛盾 | B-3 | [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) |
| 中 | DeepSeek V4+Gemma 4 OSSオープンモデル集中リリース | OSS性能ギャップのさらなる縮小 | B-3 | [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) |

### §3 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLM上位1社と2位以下の差が20pt以上に拡大 | 差別化持続の前提が成立し始める | 90日 | [IND-001](../config/indicators.json) |
| 有力2社がクロスクラウド撤退し自社基盤のみに移行 | 相互依存構造が解体され封鎖化が進む | 180日 | [IND-018](../config/indicators.json) |
| 政府・規制当局がAI市場での独占を認める判断を下す | 競争法的制約が外れ围い込みに外部制動がなくなる | 180日 | [IND-023](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-001-A | フロンティア差別化が顧客ロックインの主因になる | 10% | Epoch AI 9x-900x/年下落+DeepSeek V4 OSS+arXiv OSS商用競合で差別化の金銭的表現としての価値がさらに低下 | (なし) | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) |
| H-SCN-001-B | 1-2社がエコシステムを垂直統合し他社の参入を封じる | 12% | MCP 1,300+Confluent GA+Chrome DevToolsで開放C蓄積。封鎖兆候なし | (なし) | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク非連続ジャンプ | +10pt以上/期で高 | OSS性能ギャップ消滅確定 | 2026-05-23 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | MCP 1,300+Confluent GA+Chrome DevTools。high水準 | 2026-05-23 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-23 | 確率16%(-1)。Epoch AI 9x-900x/年価格下落が围い込み価値基盤を構造的に侵食 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) Epoch AI価格コモディティ化+[INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) arXiv OSS商用競合 | 17%(v3.85)→16%(v3.86) |
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

AAIF/MCP等の相互運用標準で移行の自由度は確保されるが、フロンティア差別化はTier 1に集中する構造を指す。現在27%で2位。MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) とChrome DevTools for Agents [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) は開放方向を強く支持するが、Epoch AI 9x-900x/年価格下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) は「差別化持続」前提をさらに弱体化させ、開放と差別化持続の同時成立を困難にしている。

### §1 コア判断

「開放されているが差別化は残る」という世界は、標準化が進む一方でフロンティアの高付加価値が維持される場合に成立する。開放側の証拠は史上最強だ。MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021)、Chrome DevTools for Agents [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022)、Confluent MCP GA [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023)、Hugging Face Open Agent Leaderboard [INFO-049](../Information/2026-05-23/collected-raw.md#INFO-049) が開放の構造的基盤を構築している。

差別化持続側は弱い。Epoch AI推論価格9x-900x/年下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) に加え、arXiv OSS商用競合 [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) が知識ベンチマークでオープン・クローズド間ギャップ事実上ゼロを報告。GPT-5.4 GPQA Diamond 94.5% [INFO-048](../Information/2026-05-23/collected-raw.md#INFO-048) は性能競争の存在を示すものの、OSS側の追従速度を考慮すると差別化の持続性は不確定だ。開放の強さと差別化持続の弱さが同時に観測される状況は、SCN-002からSCN-004(開放×コモディティ化)への移行圧力を意味する。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | MCP 1,300本番サーバー+Chrome DevTools+Confluent GA+Hugging Face Leaderboard | 開放軸を支える最も強い構造証拠の蓄積 | C-3 | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023) [INFO-049](../Information/2026-05-23/collected-raw.md#INFO-049) |
| 高 | Epoch AI 9x-900x/年価格下落+arXiv OSS商用API競合 | 差別化持続の前提を弱体化する価格・能力の二重圧力 | B-3 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) |
| 高 | DeepSeek V4+Gemma 4+Kimi K2.6 OSSオープンモデル集中リリース | OSS性能ギャップのさらなる縮小 | B-3 | [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) |
| 中 | GPT-5.4 GPQA Diamond 94.5%+Chatbot Arena Elo 1502 #1 | 性能競争の継続を示すが差別化持続の証拠として不十分 | C-3 | [INFO-048](../Information/2026-05-23/collected-raw.md#INFO-048) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| OSSモデルのエンタープライス採用が3社で10%以上のシェアを取る | 「勝者集中」前提が崩れSCN-004が上昇する | 90日 | [IND-004](../config/indicators.json) |
| BenchLM上位3社差が3pt以内に収束する | 「差別化持続」の根拠が消え、SCN-004方向の根拠が立つ | 90日 | [IND-001](../config/indicators.json) |
| トークン価格がさらに50%下落し主要プロバイダーの収益性が脅かされる | 差別化持続の経済的基盤が崩れる | 90日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-002-A | AAIF/MCP標準でAI間相互運用が確立する | 68% | MCP 1,300+Chrome DevTools+Confluent GA+Hugging Faceは開放の構造的蓄積。前回65%から上昇 | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023) | (標準競合の可能性) |
| H-SCN-002-B | Tier 1の3社がフロンティア差別化を維持し続ける | 22% | Epoch AI 9x-900x/年+arXiv OSSギャップゼロ+DeepSeek V4で差別化維持の経済的根拠が急速に弱まっている | [INFO-048](../Information/2026-05-23/collected-raw.md#INFO-048) | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-001](../config/indicators.json) | 性能の非連続ジャンプ | +5pt以上/期で高 | GPT-5.4 GPQA 94.5%。OSS性能ギャップ消滅方向 | 2026-05-23 |
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用10%超で高 | MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) | 2026-05-23 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で高 | MCP 1,300+Confluent GA+Chrome DevTools。high水準 | 2026-05-23 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-23 | 確率27%据え置き(±0)。MCP 1,300+で開放強力だが差別化vsコモディティ化矛盾で相殺 | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) MCP 1300+[INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) Epoch AI価格下落で相殺 | 27%(v3.85)→27%(v3.86) |
| 2026-05-22 | 確率27%(-1)。価格破壊が「差別化持続」をさらに弱体化 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) -67%価格下落+[INFO-037](../Information/2026-05-22/collected-raw.md#INFO-037) METRギャップが差別化の実務的価値に疑問 | 28%(v3.84)→27%(v3.85) |
| 2026-05-21 | 確率28%(-2)。Y軸再定義による再評価 | QHG Y軸再定義で「差別化持続」が厳格に評価 | 30%(v3.83)→28%(v3.84) |

### §7 ブラインドスポット

- 「差別化持続」の判定がベンチマークと価格に偏っている。ユーザー体験・信頼性・コンプライアンス等の非価格差別化を観測する指標が不十分。
- 開放エコシステムの拡大(MCP 1,300等)が「開放」を意味するか、標準主導者による新しい围い込みを意味するかの区別が困難。
- Tier 1企業の戦略転換(差別化追求から規模追求)が起きた場合、SCN-002からSCN-004への急速な移行を捉えられない可能性がある。
- Epoch AI 9x-900x/年データの信頼性と測定方法の確認が不十分(参考値として扱い)。

---

## SCN-003: 静かな囲い込み (現在確率: 36%)

> 象限: 閉鎖 × コモディティ化

### §0 一文要約

モデル差別化は薄れるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界を指す。現在36%で最高確率。Epoch AI推論価格9x-900x/年下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) でコモディティ化が確定的。围い込み蓄積(Google I/O 100件 [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067)+ペンタゴン7社機密契約 [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038)+Anthropic-Stainless [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004))はgenuine支持。ただし「10x production problem」 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) (トークン価格下落でもエンタープライス請求増)による围い込み支持は論理的飛躍とArbiterが判断。コモディティ化証拠はSCN-003/004双方に等しく支持する。

### §1 コア判断

このシナリオの構造は「差別化が消えても離れられない」という顧客固定化にある。現在の観測はその方向に動いているが、コモディティ化証拠の帰属先に注意が必要。

コモディティ化側の証拠は確定的だ。Epoch AIが同等性能での推論価格が年9x-900x下落と報告し [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065)、DeepSeek V4 OSS [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) がオープン層の性能を押し上げる。arXiv研究 [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) は知識ベンチマークでオープン・クローズド間ギャップが事実上ゼロと報告する。ただしこれらのコモディティ化証拠はSCN-003(閉鎖×コモディティ化)とSCN-004(開放×コモディティ化)の双方に等しく支持する。

围い込み側は蓄積が続く。Google I/O 100件による「全テック企業に宣戦布告」的エコシステム深耕 [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067)、ペンタゴン7社機密契約 [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038)、Anthropic-Stainless買収 [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) が围い込みの多次元同時進行を示す。Goldman Sachs 66GW [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) とBig Tech $420B [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) は資本集中を示し、围い込みの物理的基盤を強化する。

「10x production problem」 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) はトークン価格が67%下落してもエンタープライス請求額が増加する現象を指す。これは围い込み(使用量増による固定化)の支持証拠とも解釈できるが、ArbiterはJevons paradoxの歴史比較が必要と判断。論理的飛躍として扱い、確率上昇には寄与させなかった。MCP 1,300 [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) が示す「開放的な見た目の閉鎖」という構造は継続。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | Epoch AI 9x-900x/年+DeepSeek V4 OSS+arXiv OSS商用競合 | コモディティ化を支える価格・能力の三重証拠。但しSCN-003/004双方に等しく支持 | B-3 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) |
| 高 | 围い込み蓄積: Google I/O 100件+ペンタゴン7社機密契約+Anthropic-Stainless買収 | 围い込みが配布・エコシステム・データ・ハードウェア・政府の多次元で同時進行 | A-3 | [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038) [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) |
| 高 | 「10x production problem」: トークン価格-67%でもエンタープライス請求増 | 围い込み支持の可能性だが論理的飛躍(Jevons paradox比較必要) | B-3 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) |
| 中 | Goldman Sachs 66GW+Big Tech $420B | 資本集中が围い込みの物理的基盤を強化 | A-2 | [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) |
| 中 | MCP 1,300本番サーバー | 開放プロトコルは進展するが、エコシステム深度の差は埋まらない | C-3 | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| 主要企業がMCP上でクロスベンダー切り替えを実証する事例が3件以上公表される | スイッチングコストが低いことが実証され、固定化シナリオへの根拠が薄まる | 90日 | [IND-017](../config/indicators.json) |
| 围い込みシグナル蓄積のうち4件以上が逆転する | 围い込みの構造的蓄積が止まり、確率上昇が止まる | 60日 | [IND-009](../config/indicators.json) [IND-022](../config/indicators.json) |
| トークン価格が底打ちし主要プロバイダーの価格競争が収束する | コモディティ化圧力が減退し、SCN-001/002の確率が上昇する | 120日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-003-A | モデルコモディティ化でベンダー差別化は機能から围い込みに移行する | 62% | Epoch AI 9x-900x/年+DeepSeek V4+arXiv OSSはコモディティ化の確定的証拠。围い込み蓄積はgenuine。「開放的な見た目の閉鎖」が成立するかは未実証 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) |
| H-SCN-003-B | エコシステム統合深度が顧客の移行コストを決定する | 55% | Google I/O 100件+ペンタゴン7社契約+Anthropic-Stainlessの蓄積は理論的C。「10x production problem」は支持証拠だが論理的飛躍 | [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038) [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) | (クロスベンダー移行事例不在) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-009](../config/indicators.json) | AI利用規約の制限強化 | 月3件超の制限追加で高 | 围い込み蓄積継続 | 2026-05-23 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | トークン価格50%以上下落で高 | Epoch AI 9x-900x/年で消滅確定 | 2026-05-23 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全社採用で高(反証指標) | MCP 1,300+Confluent GA+Chrome DevTools。high水準 | 2026-05-23 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-23 | 確率36%据え置き(±0)。围い込み蓄積はgenuineだが「10x production problem」支持は論理的飛躍。コモディティ化証拠はSCN-003/004双方に等しく支持 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) 10x problem+[INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) Google I/O+Arbiter判断 | 36%(v3.85)→36%(v3.86) |
| 2026-05-22 | 確率36%(+1)。围い込み16件蓄積+METRギャップ+資本集中で構造的論理が強化 | [INFO-007](../Information/2026-05-22/collected-raw.md#INFO-007) Google I/O+[INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) ペンタゴン+[INFO-052](../Information/2026-05-22/collected-raw.md#INFO-052) $2.52T支出 | 35%(v3.84)→36%(v3.85) |
| 2026-05-21 | 確率35%据え置き。Y軸再定義で象限名変更(性能差収斂→コモディティ化) | 围い込み15件蓄積+トークン価格75%下落+OSSギャップ消滅 | 35%(v3.83)→35%(v3.84) |

### §7 ブラインドスポット

- 「スイッチングコストが高い」という観測が、実際に顧客が離れられないことの実証ではない。
- 「静かな围い込み」が起きているとすれば顧客はそれを認識していないはずで、認識していない事象をシグナルとして観測することは構造的に困難だ。
- コモディティ化が進行する中で围い込みの価値(囲い込む対象の差別化)自体が低下する矛盾を十分に分析できていない。
- API価格下落が围い込み戦略(高付加価値で囲う)を矛盾させるか、逆に価格破壊からの逃避先として围い込みを加速させるかの判断が不確定。
- 「10x production problem」が围い込み支持か、単なる使用量増大(Jevons paradox)かの区別が不十分。Jevons paradoxの歴史比較が必要。
- コモディティ化証拠がSCN-003とSCN-004の双方に等しく支持するため、アトラクター効果(現在の最高確率シナリオへの認知バイアス)に注意が必要。

---

## SCN-004: 誰でもAI (現在確率: 21%)

> 象限: 開放 × コモディティ化

### §0 一文要約

差別化が薄れオープン標準で自由に行き来できる世界を指す。現在21%で3位。Epoch AI 9x-900x/年価格下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) + DeepSeek V4 OSS [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) + MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) + arXiv OSS商用競合 [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) がコモディティ化+開放の四重の圧力として働く。ただしGoldman Sachs 66GW [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) とBig Tech $420B [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) の資本集中が二層市場構造を維持し、完全な平準化には至っていない。

### §1 コア判断

SCN-004は「モデルがコモディティ化し、価格も移行コストも消える」という条件が揃う場合に成立する。コモディティ化+開放方向の証拠はv3.86でさらに強まった。Epoch AI推論価格9x-900x/年下落 [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065)、DeepSeek V4 OSS [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062)、MCP 1,300本番サーバー [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021)、arXiv OSS商用API競合(知識ベンチマークギャップゼロ) [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) は価格・能力・標準・エコシステムの四重の圧力。Chrome DevTools for Agents [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) はブラウザベースエージェントの相互運用を促進し、Hugging Face Open Agent Leaderboard [INFO-049](../Information/2026-05-23/collected-raw.md#INFO-049) はオープン評価基盤を提供する。

ただしGoldman Sachs 66GW [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) とBig Tech $420B [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) はインフラ集中を示し、二層市場構造の完全解消には至っていない。ペンタゴン7社機密契約 [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038) も政府調達における選別を示す。围い込み蓄積は、コモディティ化が進んでもエコシステム深度による差別化が残る可能性(SCN-003)を示唆する。ArbiterのRed指摘SCN-004過小評価を部分採用し、SCN-001 -1%を再配分。

### §2 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:------:|---|---|:------:|---|
| 高 | Epoch AI 9x-900x/年推論価格下落 | コモディティ化の最も包括的な価格証拠 | B-3 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) |
| 高 | arXiv OSS商用API競合: 知識ベンチマークギャップ事実上ゼロ | 能力面でのコモディティ化証拠 | B-3 | [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) |
| 高 | MCP 1,300本番サーバー+Chrome DevTools+Confluent GA | 開放方向の構造的証拠。移行コスト低下を促進 | C-3 | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023) |
| 高 | DeepSeek V4+Gemma 4 OSSオープンモデル集中リリース | 能力面でのコモディティ化証拠。OSS層の性能押し上げ | B-3 | [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) |
| 中 | Goldman Sachs 66GW+Big Tech $420B | 資本集中が二層市場構造を維持(反証) | A-2 | [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) |
| 中 | ペンタゴン7社機密契約 | 政府調達での選別(反証)。完全な「誰でも」から遠い | B-3 | [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038) |

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| BenchLMの全層間差が5pt以内に収束する | フロンティアの優位性が消えSCN-004が現実的な主シナリオになる | 180日 | [IND-001](../config/indicators.json) |
| OSSモデルのエンタープライス採用シェアが20%を超える | 二層市場の下層だけでなく上層も侵食が起きたとみなせる | 180日 | [IND-004](../config/indicators.json) |
| 主要フロンティア企業が価格引き上げに成功する | コモディティ化圧力が需要側の抵抗で減退する | 90日 | [IND-017](../config/indicators.json) |

### §4 仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| H-SCN-004-A | OSSモデルがエンタープライスの主流になる | 30% | Epoch AI 9x-900x/年+DeepSeek V4+arXiv OSS商用競合は能力・価格の証拠だが、エンタープライスシェアデータが不足 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) | [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) 資本集中 |
| H-SCN-004-B | オープン標準でAIプロバイダー間の移行がほぼコストゼロになる | 38% | MCP 1,300+Chrome DevTools+Confluent GAは基盤だが、ワークフロー統合深度が移行コストを左右する | [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) | 围い込み蓄積 [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) |

### §5 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:---:|
| [IND-004](../config/indicators.json) | OSS/オープンモデル採用率 | エンタープライス採用20%超で高 | DeepSeek V4+Gemma 4 [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062)。実採用率は別途 | 2026-05-23 |
| [IND-017](../config/indicators.json) | AIコモディティ化速度 | トークン価格50%以上下落で高 | Epoch AI 9x-900x/年で確定 | 2026-05-23 |

### §6 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:---:|---|---|---|
| 2026-05-23 | 確率21%(+1)。SCN-001 -1%再配分。Epoch AI+DeepSeek V4+MCP 1300+arXiv OSSが四重の圧力 | [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) Epoch AI+[INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) DeepSeek V4+[INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) arXiv OSS | 20%(v3.85)→21%(v3.86) |
| 2026-05-22 | 確率20%(+1)。四重の圧力でSCN-001との差が3ptに拡大 | [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) -67%価格下落+[INFO-039](../Information/2026-05-22/collected-raw.md#INFO-039) DeepSeek V4+[INFO-051](../Information/2026-05-22/collected-raw.md#INFO-051) Cohere OSS | 19%(v3.84)→20%(v3.85) |
| 2026-05-21 | 確率19%(+4)。Y軸再定義による再評価。SCN-001を逆転し3位に浮上 | QHG Y軸再定義でコモディティ化方向が直接評価対象に | 15%(v3.83)→19%(v3.84) |

### §7 ブラインドスポット

- 二層市場(大規模フロンティアユーザーと中小企業のOSSユーザー)が分離した形でSCN-004とSCN-003が共存する可能性を、単一の確率に集約していることで精度が落ちている。
- 中国市場でのOSSダイナミクス(DeepSeek等)が西側市場に与えるコモディティ圧力を観測できていない。
- API価格下落が一時的な供給過剰によるものか、構造的なコモディティ化によるものかの区別が不十分。
- $420B CAPEXが供給過剰で価格破壊を加速するか、インフラ集中で围い込みを強化するかの二面性を十分に分析できていない。
- arXiv研究 [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) が「オープンウェイトと商用APIのギャップゼロ」と報告する一方で、LMSYSは「substantial gap」依然と報告しており、評価基準の違いを整理できていない。

---

## ブラックスワン: BS-001 AI安全性大事故 (現在確率: 17%)

> 低確率・高影響

### §0 一文要約

AIエージェントの本番障害・大規模セキュリティ事故が複合的に起き、業界全体に規制強化と信頼失墜をもたらす事象を指す。現在17%。88%エンタープライスインシデント [INFO-016](../Information/2026-05-23/collected-raw.md#INFO-016)、Pentagon武器化計画 [INFO-039](../Information/2026-05-23/collected-raw.md#INFO-039)、Fortune 500 150K+ Agentで10%のみガバナンス [INFO-030](../Information/2026-05-23/collected-raw.md#INFO-030) が上昇圧力。RAMPART [INFO-024](../Information/2026-05-23/collected-raw.md#INFO-024)+1Password [INFO-020](../Information/2026-05-23/collected-raw.md#INFO-020)+Glasswing 10,000件脆弱性発見 [INFO-003](../Information/2026-05-23/collected-raw.md#INFO-003) が低下圧力。相殺。Anthropic安全性拒否→SCR指定因果チェーン [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) はA-2品質で確認。新規大規模実被害のA-2+報告なし。

### §3 反証の閾値

| 反証指標 | 観測したら何が変わるか | 期限 | 監視先 |
|---|---|:---:|---|
| AIエージェントによる金融・インフラへの大規模実害インシデントが公表される | 確率が急上昇し、全シナリオの再評価が必要になる | 常時 | [IND-013](../config/indicators.json) |
| 主要国でAIエージェントの本番使用を一時停止させる行政命令が出る | 業界構造が短期に変わり、SCN-001〜004の全確率に波及する | 90日 | [IND-030](../config/indicators.json) |
| METR相当の調査でAIコード本番障害率が60%を超える | 攻撃面の拡大が閾値を超え、BS-001確率が25%以上に跳ね上がる | 180日 | [IND-013](../config/indicators.json) |

### §7 ブラインドスポット

- 88%セキュリティインシデント [INFO-016](../Information/2026-05-23/collected-raw.md#INFO-016) は頻度を示すが深刻度の分布が不明。
- 大事故が起きたとき、どのシナリオに収束するかの分析を持っていない。
- Pentagon武器化 [INFO-039](../Information/2026-05-23/collected-raw.md#INFO-039) が国家安全保障上のAI事故リスクをどう変化させるかの評価が不十分。
- Anthropic安全性拒否→SCR指定 [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) の因果チェーンはA-2品質で確認されたが、Red指摘「対策存在≠対策有効性」が記録されている。

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
| [INFO-065](../Information/2026-05-23/collected-raw.md#INFO-065) | Epoch AI推論価格9x-900x/年下落+「10x production problem」(SCN-001/003/004コモディティ化根拠) |
| [INFO-021](../Information/2026-05-23/collected-raw.md#INFO-021) | MCP 1,300本番サーバー(開放C。SCN-002/004根拠) |
| [INFO-050](../Information/2026-05-23/collected-raw.md#INFO-050) | arXiv OSS商用API競合: 知識ベンチマークギャップゼロ(コモディティ化C。SCN-004根拠) |
| [INFO-062](../Information/2026-05-23/collected-raw.md#INFO-062) | DeepSeek V4+Gemma 4 OSSリリース(コモディティ化C。SCN-004根拠) |
| [INFO-067](../Information/2026-05-23/collected-raw.md#INFO-067) | Google I/O 100件「全テック企業に宣戦布告」(围い込みC+開放C。SCN-001/003根拠) |
| [INFO-038](../Information/2026-05-23/collected-raw.md#INFO-038) | ペンタゴン7社機密契約(围い込みC。SCN-003根拠) |
| [INFO-039](../Information/2026-05-23/collected-raw.md#INFO-039) | Pentagon武器化計画(BS-001上昇圧力+SCN-003围い込み) |
| [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) | Anthropic安全性拒否→SCR指定因果チェーンA-2(BS-001+SCN-003围い込み) |
| [INFO-004](../Information/2026-05-23/collected-raw.md#INFO-004) | Anthropic-Stainless買収(围い込みC。SCN-003根拠) |
| [INFO-054](../Information/2026-05-23/collected-raw.md#INFO-054) | Goldman Sachs 66GW(資本集中I。SCN-003根拠) |
| [INFO-060](../Information/2026-05-23/collected-raw.md#INFO-060) | Big Tech $420B AI資本支出(資本集中I。SCN-003根拠) |
| [INFO-016](../Information/2026-05-23/collected-raw.md#INFO-016) | 88%エンタープライスセキュリティインシデント(BS-001上昇圧力) |
| [INFO-030](../Information/2026-05-23/collected-raw.md#INFO-030) | Fortune 500 150K+ Agent・10%ガバナンス(BS-001上昇圧力) |
| [INFO-022](../Information/2026-05-23/collected-raw.md#INFO-022) | Chrome DevTools for Agents v1(開放C。SCN-002/004根拠) |
| [INFO-023](../Information/2026-05-23/collected-raw.md#INFO-023) | Confluent MCP GA(開放C。SCN-002/004根拠) |
| [INFO-049](../Information/2026-05-23/collected-raw.md#INFO-049) | Hugging Face Open Agent Leaderboard(開放C+評価基盤) |
| [INFO-003](../Information/2026-05-23/collected-raw.md#INFO-003) | Glasswing 10,000件脆弱性発見(BS-001低下圧力) |
| [INFO-024](../Information/2026-05-23/collected-raw.md#INFO-024) | Microsoft RAMPART+Clarity(BS-001低下圧力) |
| [INFO-020](../Information/2026-05-23/collected-raw.md#INFO-020) | 1Password+OpenAI認証情報漏洩防止(BS-001低下圧力) |
| [INFO-009](../Information/2026-05-23/collected-raw.md#INFO-009) | Erdős予想反証(フロンティア能力C。SCN-001/002参考) |
| [INFO-048](../Information/2026-05-23/collected-raw.md#INFO-048) | GPT-5.4 GPQA Diamond 94.5%(性能競争C。SCN-002参考) |
| [INFO-046](../Information/2026-05-23/collected-raw.md#INFO-046) | OpenAI API価格体系2026(SCN-001/002/004価格参考) |
| [Arbiter v3.86](../state/arbiter-2026-05-23.md) | 確率更新の完全根拠(付録のみ参照) |
