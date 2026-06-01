# OpenAI

> 最終判断更新: 2026-06-01
> 全体確信度: 中低
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-OAI-001](../config/hypotheses.json) は58%に低下(v3.93: 59%, v3.94: 58%, v3.95: 58%)。Anthropic逆転3重確認(Ramp 34.4% vs 32.3%, Designer Fund 78% vs 65%, 評価額$965B vs $852B)と価格体系混乱が-2%の主因。Codex Tax Agent [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005) はgenuine Cだが相殺範囲。Rosalind Biodefense [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003)・Frontier Governance Framework [INFO-004](../Information/2026-06-01/collected-raw.md#INFO-004)・GPT-5.4 Computer Use [INFO-021](../Information/2026-06-01/collected-raw.md#INFO-021) は製品・統治面で肯定材料。SKILL.md cross-agent support [INFO-020](../Information/2026-06-01/collected-raw.md#INFO-020) が围い込み否定を追加蓄積。[H-OAI-002](../config/hypotheses.json) は45%でlow帯維持, [H-OAI-003](../config/hypotheses.json) は3%不変。[H-OAI-001](../config/hypotheses.json) が50%を割る, またはOpenAI市場シェアが40%を下回るのいずれかが観測されたら読みが変わる。

## 1. コア判断

[H-OAI-001](../config/hypotheses.json) は58%(medium lower bound)。v3.93で59%, v3.94で58%に低下, v3.95は±0%。低下の主因はAnthropic逆転3重確認。Ramp採用率34.4% vs OpenAI 32.3%, Designer Fund配分78% Anthropic vs 65% OpenAI, 評価額$965B vs $852B。価格体系混乱も加わり, 構造的逆転が単発事象ではなく趨勢であることを示している。他方でCodex Tax Agent [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005)(7,000件税務申告, 97%精度, 92%時間削減, A-3)は本番環境でのAgent機能成熟を示すgenuine C。Rosalind Biodefense [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003)(LLNL/JHU APL/CEPI協力, A-3)は政府系B2B足場の追加C。Frontier Governance Framework [INFO-004](../Information/2026-06-01/collected-raw.md#INFO-004)(California/EU AI Act適合, A-3)は統治面の前進。GPT-5.4 Computer Use [INFO-021](../Information/2026-06-01/collected-raw.md#INFO-021)(B-2)は製品進化の継続。これらC群がある程度相殺するためv3.95は±0%とした。SCN-002が25%から24%に低下(MMLU飽和+コモディティ化), SCN-004が25%から26%に上昇しSCN-004がSCN-002を初めて超過した点も, 競争環境の構造変化を示唆する。

[H-OAI-002](../config/hypotheses.json) は45%でlow帯維持。SKILL.md cross-agent support [INFO-020](../Information/2026-06-01/collected-raw.md#INFO-020)(C-3)が围い込み否定の追加蓄積。前回33件以上の围い込み否定蓄積に1件追加。上位レイヤーでの開放標準準拠の観測事実が継続的に蓄積しており, low帯の確定度が増している。

[H-OAI-003](../config/hypotheses.json) は3%で変化なし。Rosalind Biodefense [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003) は安全保障向け応用でありAGI研究優先とは矛盾しないが, AGI最優先を支持するA-2+証拠は依然不在。商業化規模(IPO $730B・Daybreak・Codex Tax Agent)の圧倒的継続。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Anthropic逆転3重確認。Ramp 34.4% vs 32.3%, Designer Fund 78% vs 65%, 評価額$965B vs $852B。価格体系混乱も加わり構造的逆転が趨勢化 | H-OAI-001の強力I。v3.93/v3.94での-2%低下の主因。市場シェア・投資家信認・開発者採用の3軸で逆転が確認され「支配的地位」に直接矛盾 | A-2 | [IND-027](../config/indicators.json) |
| 高 | Codex Tax Agent。7,000件税務申告, 97%精度, 92%時間削減。本番環境Agent成熟の直接証拠 | H-OAI-001のgenuine C。v3.95で±0%を維持した主なC要因。但し単一事例であり汎化には限界 | A-3 | [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005) |
| 高 | Rosalind Biodefense(LLNL/JHU APL/CEPI協力)+Frontier Governance Framework(California/EU AI Act適合) | H-OAI-001のC。政府系B2B足場拡大+統治面前進。Pentagon 7社契約に続く政府系関係の深化 | A-3 | [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003) [INFO-004](../Information/2026-06-01/collected-raw.md#INFO-004) |
| 高 | SKILL.md cross-agent support。围い込み否定追加蓄積。前回33件+1 | H-OAI-002围い込み否定の累積的証拠の継続。上位レイヤーでの開放標準準拠が更に確認 | C-3 | [INFO-020](../Information/2026-06-01/collected-raw.md#INFO-020) |
| 中 | GPT-5.4 Computer Use capability。製品進化の継続 | H-OAI-001の限界的C。B-2品質で診断的価値に上限 | B-2 | [INFO-021](../Information/2026-06-01/collected-raw.md#INFO-021) |
| 中 | SCN-002: 25→24%(MMLU飽和+コモディティ化), SCN-004: 25→26%(SCN-004 > SCN-002初) | 競争環境の構造変化。コモディティ化シナリオ低下, 分散型シナリオ上昇。H-OAI-001のI方向と整合 | A-1 | [SCN-002](../config/scenarios.json) [SCN-004](../config/scenarios.json) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-OAI-001](../config/hypotheses.json) が50%を割る | 「支配的地位確立」仮説が棄却水準に到達する | 180日 | [H-OAI-001](../config/hypotheses.json) |
| OpenAI市場シェアが40%を下回る(AnthropicまたはGoogle個別シェアがOpenAI超過) | 「支配」の定義自体が成立しなくなる | 180日 | [IND-027](../config/indicators.json) |
| Pentagon評価でOpenAIが選択されない, または契約更新が不調 | Pentagon Cの因果チェーンが崩れる | 365日 | [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003) |
| gpt-oss/open weightモデルのエンタープライス採用が20%を超える | 围い込み否定が更に蓄積し[H-OAI-002](../config/hypotheses.json)棄却確定 | 180日 | [IND-027](../config/indicators.json) |
| OpenAI Skills/Shellの独自拡張がMCP/SKILL.md互換を破壊する | 围い込み否定蓄積の前提が崩れ[H-OAI-002](../config/hypotheses.json)上方修正の必要 | 365日 | [INFO-020](../Information/2026-06-01/collected-raw.md#INFO-020) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 58% medium | Anthropic逆転3重確認(Ramp/Designer Fund/評価額)+価格体系混乱でv3.93-94に-2%。Codex Tax Agent(A-3)+Rosalind(A-3)+Frontier Governance(A-3)はgenuine Cだが相殺範囲。v3.95は±0%。SCN-004 > SCN-002初達成で競争環境構造変化。累積I依然優勢 | [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005) [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003) [INFO-004](../Information/2026-06-01/collected-raw.md#INFO-004) [INFO-021](../Information/2026-06-01/collected-raw.md#INFO-021) | [IND-027](../config/indicators.json) [IND-026](../config/indicators.json) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放の上にプロプライエタリ上位レイヤーで围い込む | 45% low | 围い込み否定累積34件。SKILL.md cross-agent support(C-3)が追加。上位レイヤーでの開放標準準拠観測が継続蓄積。low帯確定度増加 | (新規Cなし) | [INFO-020](../Information/2026-06-01/collected-raw.md#INFO-020) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% low | 商業化規模(IPO $730B・Daybreak・Codex Tax Agent・Rosalind)が圧倒的。AGI最優先を支持する新規A-2+証拠不在。v3.77以降±0%継続 | [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003)(Rosalind: 安全保障応用でありAGI研究とは限定的) | [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005) [INFO-004](../Information/2026-06-01/collected-raw.md#INFO-004) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントで critical | OWASP+97%+AIUC-1+TELUS。攻撃面拡大基調継続。high・rising | 2026-06-01 |
| [IND-025](../config/indicators.json) | AI性能コモディティ化率 | 性能差がベンダー間5%未満で high | Gemini 3 Pro Deep Think+GPT-5.4+NVIDIA Nemotron。多極化進行。elevated・stable | 2026-06-01 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | 95% ROI未達+49%停滞+Goldman Sachs 24倍。構造的固定化継続。high・rising | 2026-06-01 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用で high | SKILL.md+agents-cli OSS+Grok Build。標準化進展継続。high・rising | 2026-06-01 |
| [IND-028](../config/indicators.json) | AGI到達度指標(客観ベンチマーク vs 主観宣言) | 主観-客観乖離拡大で high | Hassabis 2029+RSI+Bengio。主観-客観乖離継続。high・rising | 2026-06-01 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限り high | Anthropic $65B+Snowflake $6B+EY $1B+ByteDance独自CPU。資本流入加速継続。high・rising | 2026-06-01 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | 能力向上とリスク治理後退の同時進行で high | Rosalind+Illinois+大統領令廃止+NIST改名+AIUC-1。9重蓄積加速。high・rising | 2026-06-01 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-01 | Anthropic逆転3重確認+Codex Tax Agent+Rosalind+Frontier Governance+SKILL.md cross-agentを反映して全面書き直し | [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005) [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003) [INFO-004](../Information/2026-06-01/collected-raw.md#INFO-004) [INFO-020](../Information/2026-06-01/collected-raw.md#INFO-020) [INFO-021](../Information/2026-06-01/collected-raw.md#INFO-021) | H-OAI-001 60→58%・H-OAI-002 45%維持・H-OAI-003 3%維持・「Pentagon 7社契約Cだが累積I 22件優勢」→「Anthropic逆転3重確認でv3.93-94に-2%, Codex Tax Agent+Rosalindはgenuine Cだが相殺。58% medium lower bound」 |
| 2026-05-29 | Pentagon 7社契約(A-2)+Anthropic評価額逆転(A-2)+围い込み否定6件追加を反映して全面書き直し | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) | H-OAI-001 62→60%・H-OAI-002 46→45%・H-OAI-003 3%維持・「Pentagon C最强だが累積I 18件で打破過大」→「Pentagon 7社契約はCだが評価額逆転+コモディティ化で累積I 22件優勢。围い込み否定33件蓄積でlow帯確定」 |
| 2026-05-22 | Pentagon契約(A-2)+Erdős反証(A-3)+-67%価格下落(C-3)+IPO $730B(B-3)を反映して全面書き直し | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-005](../Information/2026-05-22/collected-raw.md#INFO-005) | H-OAI-001 63→62%・H-OAI-002 46%維持・H-OAI-003 3%維持・「市場シェア初逆転でI>C」→「Pentagon C最强だが累積I 18件で打破過大」 |
| 2026-05-19 | 市場シェア初逆転+Microsoft離反+Dell提携+IPO $8,520億を反映して全面書き直し | [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004) | H-OAI-001 64→63%・H-OAI-002 48→46%・「围い込み否定8重蓄積」→「市場シェア初逆転でI>C初ラウンド」 |

## 7. ブラインドスポット

- Anthropic逆転3重確認の各指標(Ramp採用率, Designer Fund配分, 評価額)が異なるサンプルと方法論に基づく。Rampは企業支出パネル, Designer Fundはデザイン業界特化, 評価額は私募市場と上場前の混在比較。3軸の一致は趨勢を示唆するが, 各指標の誤差範囲が不明。
- Codex Tax Agent(7,000件, 97%精度, 92%時間削減)の品質等级がA-3であり, OpenAI自身の発表に基づく。第三者検証が不在で, 精度・時間削減の測定手法が不明。本番環境成熟のCとして扱っているが, 選択的提示の可能性がある。
- Rosalind Biodefense(LLNL/JHU APL/CEPI協力)が政府系B2B足場のCとして機能するかは, プログラムの継続性と規模に依存。Pentagon 7社契約と同様に, 複数機関との協力体制におけるOpenAI固有の位置づけが不明。
- SKILL.md cross-agent support [INFO-020](../Information/2026-06-01/collected-raw.md#INFO-020) がC-3品質であり, 围い込み否定の診断的価値に上限がある。SKILL.md準拠の表明と実際の相互運用性の間にギャップがある可能性。
- SCN-004がSCN-002を初めて超過した(26% vs 24%)が, この逆転が一時的か趨勢的かの判別が不能。SCN-002の低下(MMLU飽和+コモディティ化)とSCN-003の停滞ペナルティ撤回が同時に起きており, シナリオ間の相互作用が複雑化している。
- 確証バイアス蓄積のリスク。H-OAI-001が64%→63%→62%→60%→59%→58%と5R連続で低下しており, 下方バイアスの自己強化に注意が必要。Anthropic逆転の各指標が相互に依存している可能性(同じ市場環境下での観測)があり, 独立証拠としての過大評価リスクがある。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-005](../Information/2026-06-01/collected-raw.md#INFO-005) | OpenAI Codex Tax Agent・7,000件税務申告・97%精度・92%時間削減(A-3) |
| [INFO-003](../Information/2026-06-01/collected-raw.md#INFO-003) | OpenAI Rosalind Biodefense program・LLNL/JHU APL/CEPI協力(A-3) |
| [INFO-004](../Information/2026-06-01/collected-raw.md#INFO-004) | OpenAI Frontier Governance Framework公開・California/EU AI Act適合(A-3) |
| [INFO-021](../Information/2026-06-01/collected-raw.md#INFO-021) | GPT-5.4 Computer Use capability(B-2) |
| [INFO-020](../Information/2026-06-01/collected-raw.md#INFO-020) | SKILL.md cross-agent support(C-3) |
| [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) | Pentagon 7社契約・Dell $9.7B・Anthropic SCR除外(CNBC A-2) |
| [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) | Anthropic評価額$965BがOpenAI $730B超過(NYT A-2) |
| [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) | GPT-5.5 Instant更新・o3/GPT-4.5引退・GPT-5.4 Thinking(OpenAI A-1) |
| [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) | OpenAI Skills Beta・Agent Skills open standard準拠(OpenAI A-1) |
| [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) | gpt-oss-120b/20b open weight推論モデル(OpenAI A-1) |
| [INFO-042](../Information/2026-05-29/collected-raw.md#INFO-042) | GPT-5.3-Codex ~25%高速化・Codex+GPT-5統合スタック(OpenAI A-1) |
| [INFO-039](../Information/2026-05-29/collected-raw.md#INFO-039) | Codex価格 per-messageからAPI token pricingへ移行(OpenAI A-1) |
| [INFO-007](../Information/2026-05-29/collected-raw.md#INFO-007) | MCP 97M+ SDK DL・9,652サーバー・41%本番運用(Digital Applied B-2) |
| [INFO-009](../Information/2026-05-29/collected-raw.md#INFO-009) | Agent Skills 40,285・SKILL.md 26+ツール採用・18.5倍成長(B-2) |
| [INFO-040](../Information/2026-05-29/collected-raw.md#INFO-040) | Microsoft Agent Framework OSS・.NET/Python・他社モデルスワップ可能(GitHub A-1) |
| [INFO-028](../Information/2026-05-29/collected-raw.md#INFO-028) | Model-agnostic orchestration・スイッチングコスト低下・CompareAI(Augment Code C-3) |
| [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021) | エンタープライスAIエージェント88%失敗・ROI現在マイナス(C-3) |
| [INFO-020](../Information/2026-05-29/collected-raw.md#INFO-020) | Fortune 500平均<15エージェント・Gartner 150K予測(B-3) |
