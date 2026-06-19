# OpenAI

> 最終判断更新: 2026-06-19
> 全体確信度: 中低
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-OAI-001](../config/hypotheses.json) は50%（medium帯中央）。v4.06の56%から6ポイント低下した。最大の根拠はAnthropic年間収益ランレート$470億がOpenAI $330億を逆転した事実 [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011)（C-2）と、17ラウンド連続でOpenAI劣位を示す証拠が蓄積したパターンだ。但しArbiterは「Anthropic成功＝OpenAI劣位」というゼロサム仮定を未検証とし、拡大市場では両社同時成長が可能と指摘する。Pentagon GenAI.mil契約で300万人職員向けChatGPT提供を予定する事実 [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) は政府系B2Bチャネルの獲得であり、順応報酬構造（安全性制約解除と引換えに政府市場にアクセス）への参加を示す。OpenAI収益内訳（API/Enterprise/Consumer）の時系列データ、または市場シェア（支出ベース）が35%を下回るのいずれかが観測されたら判断が変わる。

## 1. コア判断

[H-OAI-001](../config/hypotheses.json) は50%（medium）。v4.06で56%、v4.07〜v4.12で51〜52%を推移し、v4.13で50%に至った。低下圧力の主因は二つある。

第一に、収益逆転の定量化だ。Anthropicの年間収益ランレートが2026年5月に$470億に到達し、OpenAIの$330億を12カ月未満で追い抜いた [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011)。地球上の最大10社のうち8社がAnthropic有料顧客とされる。Claude Code採用はJetBrains 1万人調査で9カ月に3%から24%（米国）・18%（世界）へ急拡大し [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012)、開発者エコシステムでもAnthropicが追い上げている。これらが17ラウンド連続でOpenAI劣位を示すパターンを形成し、機械的ペナルティとして確度を押し下げた。

第二に、価格面での支配力欠如だ。Jevons paradoxがA-2品質で確認された [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058)。トークン価格が90%安価化しても使用量が倍増する現象は、コモディティ化の強力な定量証拠であると同時に、コスト優位企業による支配強化の可能性も開く。OpenAIは$1,220億調達の資本力でコスト優位を武器にするシナリオが成立するが、これは「コモディティ化＝支配否定」というH-OAI-001の暗黙前提と矛盾する。Red Agentの指摘通り、標準的経済理論（規模の経済による支配）では、コモディティ化は支配否定ではなく支配強化を導く場合がある。

但し、Arbiterは「Anthropic成功＝OpenAI劣位」というゼロサム仮定を未検証とした。AI市場は拡大市場であり、両社同時成長が可能だ。値下げ＝弱者シグナルという解釈も単一的であり、predatory pricing（掠食的価格設定）の代替解釈が存在する。-1%（v4.12の51%→v4.13の50%）は方向圧力（17R連続 I>C）を認めつつ、これらの代替解釈の妥当性を尊重した保守的調整。次回の確度変更条件はOpenAI収益$330億の内訳（API/Enterprise/Consumer）時系列と、市場シェア（支出ベース）の時系列データの収集にある。

[H-OAI-002](../config/hypotheses.json) は44%（low）。围い込み否定証拠の累積は継続している。Partner Network $150M投資 [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) はエンタープライズチャネル拡大だが排他性言及なし。Apps SDK更新 [INFO-019](../Information/2026-06-19/collected-raw.md#INFO-019) はMCP統合完全対応を維持。上位レイヤーでの開放標準準拠の観測が蓄積し続けている。[H-OAI-003](../config/hypotheses.json) は3%（low）。商業化規模（IPO準備・Codex・Daybreak）が圧倒的で、AGI最優先を支持するA-2+証拠は不在。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Anthropic ARR $470億 vs OpenAI $330億。12カ月未満で$40億→$470億。最大10社中8社がAnthropic有料顧客 | H-OAI-001のI。収益逆転の定量化。但しゼロサム仮定は未検証（拡大市場で両社成長可能） | C-2 | [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) |
| 高 | Jevons paradox: トークン90%安価化で使用量倍増。トークン価格下落が業界全体現象 | H-OAI-001の二面性I。コモディティ化圧力（支配否定）と同時にコスト優位企業の支配強化可能性（predatory pricing代替解釈） | A-2 | [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) |
| 高 | Pentagon GenAI.mil 2026年7月上旬提供予定・職員最大300万人。Pentagon 5月2日6社同時AI合意署名 | H-OAI-001のC（政府系B2Bチャネル）。順応報酬構造への参加。Anthropicが排除された条件を受諾 | C-3 | [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) |
| 高 | Claude Code採用 9カ月で3%→24%（米国）・18%（世界）。JetBrains 1万人調査 | H-OAI-001の競争圧力I。開発者エコシステムでのAnthropic追い上げの第三者定量証拠 | B-3 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) |
| 中 | Partner Network立ち上げ・$150M投資。エンタープライズAI採用加速が目的 | H-OAI-001のC。チャネル拡大。排他性なしはH-OAI-002围い込み否定と整合 | A-3 | [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) |
| 中 | 17R連続 I>Cパターン。OpenAI劣位を示す証拠がI（不一致）として継続蓄積 | H-OAI-001の機械的ペナルティ要因。但し循環論法リスク（Anthropic成功→OpenAI劣位）を含む | (内部) | [arbiter-2026-06-19](../state/arbiter-2026-06-19.md) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-OAI-001](../config/hypotheses.json) が45%を割る | 「B2B支配的地位確立」仮説が棄却水準に接近する | 180日 | [H-OAI-001](../config/hypotheses.json) |
| OpenAI収益内訳でAPI収益がEnterprise収益を下回り差が拡大する | 「B2B支配」の収益的裏付けが変質する。API依存度低下＝エンタープライズ直接販売の成功かAPI競争力低下かの判別が必要 | 90日 | [IND-027](../config/indicators.json) |
| OpenAI市場シェア（支出ベース）が35%を下回る | 「支配」の定義自体が成立しなくなる。AnthropicまたはGoogle個別シェアがOpenAI超過 | 180日 | [IND-027](../config/indicators.json) |
| Anthropic ARRが$200億以上のリードを90日間維持する | 収益逆転が一時的でなく構造的と判定され、H-OAI-001の下方圧力が確定的になる | 90日 | [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) |
| Pentagon GenAI.mil契約が延期または取消となる | 政府系B2Bチャネル獲得の因果チェーンが崩れる | 365日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 50% medium | 17R連続 I>Cで機械的下方圧力。Anthropic ARR $470億 vs $330億(INFO-011 C-2)とClaude Code採用3%→24%(INFO-012 B-3)がI。Jevons paradox(INFO-058 A-2)はコモディティ化Iだがpredatory pricing代替解釈でC/I二面性。Pentagon GenAI.mil(INFO-010 C-3)とPartner Network $150M(INFO-003 A-3)がC。ゼロサム仮定未検証・「B2B支配」定義未解決 | [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) | [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) [IND-026](../config/indicators.json) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放の上にプロプライエタリ上位レイヤーで围い込む | 44% low | 围い込み否定累積34件+。Partner Network(INFO-003)・Apps SDK MCP統合(INFO-019)の排他性なしは围い込み否定と整合。上位レイヤー開放標準準拠が継続蓄積。low帯確定度増加 | (新規围い込み肯定Cなし) | [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) [INFO-019](../Information/2026-06-19/collected-raw.md#INFO-019) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% low | 商業化規模（IPO準備・Codex・Daybreak・Partner Network $150M）が圧倒的。Phase 3宣言はAGI研究自動化を目標に含むが3目標中2つは商業ロードマップ。AGI最優先を支持するA-2+証拠不在 | [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントでcritical | OpenBSD 27年脆弱性AI発見・GitHub月19件障害・MCP Gateway中央集権化。新規A-2実被害なし。high・rising | 2026-06-19 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | Gemini 3.1 Pro動画推論55.63%・ARC-AGI-3全フロンティア0.37%。量的向上継続・真の理解未解決。elevated・stable | 2026-06-19 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | ALE完遂<5%・95%失敗・96%ROI vs 74%ロールバック矛盾。期待-実態ギャップ構造的パターン化確定。high・rising | 2026-06-19 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | MCP月間1.1億DL・AAIF 170社・OpenShell OSS。標準化爆発的加速・围い込み同時進行。high・rising | 2026-06-19 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | DeepMind AGI 2029-2030・ARC-AGI-3 0.37%・LeCun退社。RSI具体化と客観ベンチマーク限界の同時進行。high・rising | 2026-06-19 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | Dallas Fed $3-5T・ByteDance 2000億元・Q1 $3000億・Anthropic $650億。資本流入加速・物理的制約ギャップ確定的。high・rising | 2026-06-19 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | 技術的安全事故A-2でcritical | Grok軍事96h/2,000弾薬・Google兵器誓約削除・OpenAI Pentagon GenAI.mil。能力-リスク二面性極大化。high・rising | 2026-06-19 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-19 | §0〜§5・付録を全面書き直し。鮮度タイムアウト（7日）+ H-OAI-001 50%（medium帯中央）到達。Anthropic ARR $470億 vs $330億逆転・Jevons paradox A-2・Pentagon GenAI.mil・Claude Code採用24%を反映。ゼロサム仮定未検証・predatory pricing代替解釈を明記 | [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) | H-OAI-001 51→50%・H-OAI-002 44%維持・H-OAI-003 3%維持 |
| 2026-06-12 | §0-§2・§4・§5・付録を全面書き直し。S-1提出・Phase 3宣言・Ona買収・価格引き下げ検討を反映。H-OAI-001 56% | [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001) [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019) | H-OAI-001 58→56%・H-OAI-002 45→44%・H-OAI-003 3%維持 |
| 2026-06-01 | Anthropic逆転3重確認+Codex Tax Agent+Rosalind+Frontier Governance+SKILL.md cross-agentを反映して全面書き直し | [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005) [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003) | H-OAI-001 60→58% |
| 2026-05-29 | Pentagon 7社契約+Anthropic評価額逆転+围い込み否定6件追加を反映して全面書き直し | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) | H-OAI-001 62→60% |
| 2026-05-22 | Pentagon契約+Erdős反証+-67%価格下落+IPO $730Bを反映して全面書き直し | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) | H-OAI-001 63→62% |

## 7. ブラインドスポット

- OpenAI収益$330億の内訳（API/Enterprise/Consumer）が非公開。どのセグメントが成長し、どのセグメントがAnthropicに侵食されているかの判別が不能。S-1提出済みだが機密提出であり財務内容が不明。
- 「Anthropic成功＝OpenAI劣位」というゼロサム仮定が検証されていない。AI市場が拡大市場の場合、両社同時成長が可能であり、収益逆転がOpenAIの構造的劣位を意味するとは限らない。この区別がつかない限り、17R連続 I>Cパターンの機械的ペナルティは過大評価のリスクを持つ。
- Jevons paradoxがOpenAIにとってコモディティ化圧力（I）なのか、$1,220億資本力を活かしたコスト優位による支配強化（C）なのかの判別ができない。価格戦略の意図（掠食的価格設定 vs 単なる競争対応）が不明。
- Pentagon GenAI.mil契約の実効性と収益寄与が不明。2026年7月上旬提供予定だが、実際の利用率・政府要件の変更可能性・契約更新確度の判別が不能。
- Claude Code採用24%（米国）はJetBrains調査（B-3）であり、OpenAI Codex採用との直接比較データが不在。開発者エコシステムでの相対的地位の変化を定量化する共通基準がない。
- 確証バイアス蓄積のリスク。H-OAI-001が56%→51%→50%と低下し続ける中で、下方バイアスの自己強化に注意が必要。Anthropic逆転の各指標が相互に依存している可能性があり、独立証拠としての過大評価リスクがある。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-003](../Information/2026-06-19/collected-raw.md#INFO-003) | OpenAI Partner Network立ち上げ・$150M投資(A-3) |
| [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) | OpenAI Pentagon GenAI.mil 300万人・順応報酬構造参加(C-3) |
| [INFO-011](../Information/2026-06-19/collected-raw.md#INFO-011) | Anthropic ARR $470億 vs OpenAI $330億逆転(C-2) |
| [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) | Claude Code採用3%→24%・JetBrains 1万人調査(B-3) |
| [INFO-019](../Information/2026-06-19/collected-raw.md#INFO-019) | OpenAI Apps SDK更新・MCP統合完全対応(A-3) |
| [INFO-058](../Information/2026-06-19/collected-raw.md#INFO-058) | Jevons paradox・トークン90%安価化・支出倍増(A-2) |
| [INFO-001](../Information/2026-06-12/collected-raw.md#INFO-001) | OpenAI Ona買収・Codex永続的クラウド実行環境統合(A-3) |
| [INFO-003](../Information/2026-06-12/collected-raw.md#INFO-003) | OpenAI S-1提出・IPO準備公式確認(A-3) |
| [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | OpenAI Phase 3宣言・2028年3月AI研究自動化目標(A-3) |
| [INFO-005](../Information/2026-06-12/collected-raw.md#INFO-005) | OpenAI Codex全職種拡大・6役掛別プラグイン(A-3) |
| [INFO-019](../Information/2026-06-12/collected-raw.md#INFO-019) | OpenAI価格引き下げ検討・Anthropic競争背景(B-3) |
| [INFO-029](../Information/2026-06-12/collected-raw.md#INFO-029) | OpenAI IPO $730B vs Anthropic $965B評価額(B-3) |
| [INFO-002](../Information/2026-06-12/collected-raw.md#INFO-002) | OpenAI Oracle Cloud提携・排他性なし(A-3) |
| [INFO-028](../Information/2026-06-12/collected-raw.md#INFO-028) | Visa-OpenAI提携・Agentic Commerce決済(B-3) |
| [INFO-038](../Information/2026-06-12/collected-raw.md#INFO-038) | BCG「大半の企業がAI投資から意味ある収益を得られず」(B-3) |
| [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) | GitHub Copilot定額→従量制移行(A-2) |
| [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | Pentagon SCR指定・Anthropic除外(A-1) |
| [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005) | OpenAI Codex Tax Agent・97%精度(A-3) |
| [INFO-004](../Information/2026-06-01/collected-raw.md#INFO-004) | OpenAI Frontier Governance Framework(A-3) |
| [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) | Pentagon 7社契約・Dell $9.7B(A-2) |
| [Arbiter v4.13](../state/arbiter-2026-06-19.md) | 確度変更の完全根拠(付録のみ参照) |
