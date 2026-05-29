# OpenAI

> 最終判断更新: 2026-05-29
> 全体確信度: 中
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

OpenAIはPentagon 7社契約 [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) で政府系B2Bの足場を維持し、GPT-5.3-Codex高速化 [INFO-042](../Information/2026-05-29/collected-raw.md#INFO-042) で製品競争力を示しているが、Anthropic評価額$965BがOpenAI $730Bを上回る構造的逆転 [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) と、MCP 97M SDK DL [INFO-007](../Information/2026-05-29/collected-raw.md#INFO-007)・SKILL.md 40K+ [INFO-009](../Information/2026-05-29/collected-raw.md#INFO-009)・gpt-oss open weight [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) が示す围い込み否定の蓄積が進行中。[H-OAI-001](../config/hypotheses.json) は60%に低下(3R連続-1%)、[H-OAI-002](../config/hypotheses.json) は45%でlow帯確定。[H-OAI-001](../config/hypotheses.json) が50%を割る、またはOpenAI市場シェアが40%を下回るのいずれかが観測されたら読みが変わる。

## 1. コア判断

[H-OAI-001](../config/hypotheses.json) は60%に低下(前回62%)。Pentagon 7社契約 [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) はOpenAIがGoogle/Microsoft/AWS/Nvidia/SpaceX/Reflectionと並ぶ7社の一角としてPentagonと合意した事実(A-2)で、政府系B2B足場のCとして機能する。但し7社の一角でありOpenAI固有の優位性に上限がある。Dell $9.7B・Microsoft $9.69Bが同枠で契約されており、Anthropic SCR除外の受益者という解釈は因果推論に過ぎない。他方で累積Iは22件に達した。Anthropic評価額$965B vs OpenAI $730B [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) は市場信認の構造的逆転として重く、コモディティ化圧力と本番ギャップ(88%失敗率 [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021))の下で「支配」の定義が一段と困難になっている。GPT-5.5 Instant更新 [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) とGPT-5.3-Codex ~25%高速化 [INFO-042](../Information/2026-05-29/collected-raw.md#INFO-042) は製品進化のgenuine Cだが、o3引退(2026年8月26日)とGPT-4.5引退(2026年6月27日)が示すポートフォリオ整理は淘汰圧力の裏返しでもある。

[H-OAI-002](../config/hypotheses.json) は45%でlow帯確定(前回46%)。OpenAI Skills BetaがAgent Skills open standard(SKILL.md)準拠 [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) で提供されたことは围い込み否定の強力な証拠。gpt-oss-120b/20b open weight公開 [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043)、Microsoft Agent Framework OSS [INFO-040](../Information/2026-05-29/collected-raw.md#INFO-040)、MCP 97M SDK DL [INFO-007](../Information/2026-05-29/collected-raw.md#INFO-007)、model-agnostic orchestration普及 [INFO-028](../Information/2026-05-29/collected-raw.md#INFO-028) が加わり、围い込み否定は累積33件以上に達した。仮説命題「開放エコシステム上にプロプライエタリ上位レイヤーを構築する」に対し、上位レイヤー(Skills)でも開放標準に準拠する観測事実が蓄積している。Codex価格のper-messageからAPI token pricingへの移行 [INFO-039](../Information/2026-05-29/collected-raw.md#INFO-039) も透明性向上として围い込み否定と整合する。

[H-OAI-003](../config/hypotheses.json) は3%で変化なし。IPO $730B・GPT-5.3-Codex・Daybreakの商業化規模が圧倒的。研究面C(Erdős予想反証)は既確認済みであり、AGI最優先を支持する新規証拠は不在。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Pentagon 7社契約(Google/Microsoft/AWS/Nvidia/OpenAI/SpaceX/Reflection)。AnthropicはSCR除外。Dell $9.7B・Microsoft $9.69Bも同枠 | H-OAI-001の今ラウンド最強C。政府系B2B足場の直接証拠。但し7社の一角でありOpenAI固有の優位性に上限。Anthropic除外受益は因果推論で診断的価値に上限 | A-2 | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) |
| 高 | Anthropic評価額$965BがOpenAI $730Bを上回る(NYT A-2)。Series H $65B調達完了。構造的逆転確定 | H-OAI-001の強力I。市場シェア・投資家信認の逆転は「支配的地位」に直接矛盾。前回IPO $730B評価額から横ばい | A-2 | [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) [INFO-049](../Information/2026-05-29/collected-raw.md#INFO-049) |
| 高 | MCP 97M+ SDK DL・SKILL.md 40K+スキル・OpenAI Skills Beta(open standard準拠)・gpt-oss-120b/20b open weight | H-OAI-002围い込み否定の累積的証拠。上位レイヤー(Skills)でも開放標準に準拠。open weight公開は围い込みと論理的に矛盾。I蓄積33件に到達 | A-1/B-2 | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-009](../Information/2026-05-29/collected-raw.md#INFO-009) [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) [INFO-007](../Information/2026-05-29/collected-raw.md#INFO-007) |
| 高 | GPT-5.5 Instant更新 + o3引退(8月26日) + GPT-4.5引退(6月27日) + GPT-5.3-Codex ~25%高速化 | ポートフォリオ進化のgenuine C。Codex+GPT-5統合スタック強化。但し旧モデル引退は淘汰圧力の裏返し。Codex価格もper-messageからtoken pricingに移行し透明性向上 | A-1 | [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) [INFO-042](../Information/2026-05-29/collected-raw.md#INFO-042) [INFO-039](../Information/2026-05-29/collected-raw.md#INFO-039) |
| 中 | Model-agnostic orchestration普及 + Microsoft Agent Framework OSS + Codex価格透明化 | H-OAI-001のI(コモディティ化)及びH-OAI-002围い込み否定の補強。スイッチングコスト低下が「支配」を困難にする方向。業界全体トレンドの可能性がありOpenAI固有影響の分離不能 | A-1/C-3 | [INFO-028](../Information/2026-05-29/collected-raw.md#INFO-028) [INFO-040](../Information/2026-05-29/collected-raw.md#INFO-040) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-OAI-001](../config/hypotheses.json) が50%を割る | 「支配的地位確立」仮説が棄却水準に到達する | 180日 | [H-OAI-001](../config/hypotheses.json) |
| OpenAI市場シェアが40%を下回る(AnthropicまたはGoogle個別シェアがOpenAI超過) | 「支配」の定義自体が成立しなくなる | 180日 | [IND-027](../config/indicators.json) |
| Pentagon評価でOpenAIが選択されない、または契約更新が不調 | Pentagon Cの因果チェーンが崩れる | 365日 | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) |
| gpt-oss/open weightモデルのエンタープライス採用が20%を超える | 围い込み否定が更に蓄積し[H-OAI-002](../config/hypotheses.json)棄却確定 | 180日 | [IND-027](../config/indicators.json) |
| OpenAI Skills/Shellの独自拡張がMCP/SKILL.md互換を破壊する | 围い込み否定蓄積の前提が崩れ[H-OAI-002](../config/hypotheses.json)上方修正の必要 | 365日 | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 60% medium | Pentagon 7社契約(A-2)+GPT-5.3-Codex高速化(A-1)はgenuine C。但し累積I 22件(Anthropic評価額逆転+コモディティ化+本番ギャップ)が依然優勢。「支配」の定義がコモディティ化下で困難。3R連続-1%で60%到達 | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) [INFO-042](../Information/2026-05-29/collected-raw.md#INFO-042) [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) | [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021) [INFO-028](../Information/2026-05-29/collected-raw.md#INFO-028) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放の上にプロプライエタリ上位レイヤーで围い込む | 45% low | 围い込み否定累積33件。OpenAI Skills Beta(open standard準拠)+gpt-oss open weight+MCP 97M+SKILL.md 40K+が今ラウンドの围い込み否定追加。上位レイヤーでも開放に傾く観測が蓄積。low帯確定 | (新規Cなし。Codex価格透明化は中性的) | [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) [INFO-007](../Information/2026-05-29/collected-raw.md#INFO-007) [INFO-009](../Information/2026-05-29/collected-raw.md#INFO-009) [INFO-040](../Information/2026-05-29/collected-raw.md#INFO-040) [INFO-028](../Information/2026-05-29/collected-raw.md#INFO-028) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% low | 商業化規模(IPO $730B・Daybreak・GPT-5.3-Codex・広告)が圧倒的。研究面C(Erdős予想反証)は既確認。AGI最優先を支持する新規A-2+証拠不在。v3.77以降±0%継続 | [INFO-036](../Information/2026-05-29/collected-raw.md#INFO-036)(Altman AGI予測:C-3品質で限界的) | [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) [INFO-042](../Information/2026-05-29/collected-raw.md#INFO-042) [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントで critical | CVE-2026-22561 DLL脆弱性A-1開示。攻撃面拡大基調継続。high・rising | 2026-05-29 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | Fortune 500 <15エージェント+88%失敗+Gartner 150K予測。68pt採用ギャップ構造的固定化。high・rising | 2026-05-29 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用で high | MCP 9,652サーバー/97M DL+Agent Skills 40K++OpenAI Skills Beta+gpt-oss open weight。標準化爆発的進展。high・rising | 2026-05-29 |
| [IND-028](../config/indicators.json) | AGI到達度指標(客観ベンチマーク vs 主観宣言) | 主観-客観乖離拡大で high | Altman 2025-2028+Hassabis ~2030。新規客観的ベンチマークなし。主観-客観乖離継続。elevated・rising | 2026-05-29 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限り high | US DC $50B/yr+McKinsey $5.2T+Anthropic $65B Series H。資本流入劇的加速。high・rising | 2026-05-29 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | 能力向上とリスク治理後退の同時進行で high | SCR維持+Trump EO撤回+EU multi-agent規制+Pope回勅。6重蓄積加速。high・rising | 2026-05-29 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-29 | Pentagon 7社契約(A-2)+Anthropic評価額逆転(A-2)+围い込み否定6件追加を反映して全面書き直し | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) [INFO-043](../Information/2026-05-29/collected-raw.md#INFO-043) [INFO-011](../Information/2026-05-29/collected-raw.md#INFO-011) | H-OAI-001 62→60%・H-OAI-002 46→45%・H-OAI-003 3%維持・「Pentagon C最强だが累積I 18件で打破過大」→「Pentagon 7社契約はCだが評価額逆転+コモディティ化で累積I 22件優勢。围い込み否定33件蓄積でlow帯確定」 |
| 2026-05-22 | Pentagon契約(A-2)+Erdős反証(A-3)+-67%価格下落(C-3)+IPO $730B(B-3)を反映して全面書き直し | [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) [INFO-006](../Information/2026-05-22/collected-raw.md#INFO-006) [INFO-031](../Information/2026-05-22/collected-raw.md#INFO-031) [INFO-005](../Information/2026-05-22/collected-raw.md#INFO-005) | H-OAI-001 63→62%・H-OAI-002 46%維持・H-OAI-003 3%維持・「市場シェア初逆転でI>C」→「Pentagon C最强だが累積I 18件で打破過大」 |
| 2026-05-19 | 市場シェア初逆転+Microsoft離反+Dell提携+IPO $8,520億を反映して全面書き直し | [INFO-030](../Information/2026-05-19/collected-raw.md#INFO-030) [INFO-023](../Information/2026-05-19/collected-raw.md#INFO-023) [INFO-004](../Information/2026-05-19/collected-raw.md#INFO-004) | H-OAI-001 64→63%・H-OAI-002 48→46%・「围い込み否定8重蓄積」→「市場シェア初逆転でI>C初ラウンド」 |

## 7. ブラインドスポット

- Pentagon 7社契約におけるOpenAIの位置づけが「7社の一角」であり排他的選択ではない。Dell・Microsoft・AWS等インフラ企業とOpenAI・Google・SpaceX・Reflectionが同枠で、AIプロバイダーとしてのOpenAI固有の優位性を分離不能。Anthropic除外がOpenAI受益の因果チェーンもSCR指定の結果であり、能力評価ではない可能性がある。
- Anthropic評価額$965B vs OpenAI $730Bの逆転が、私募市場評価(Anthropic Series H)と上場前評価(OpenAI IPO)の比較である可能性。評価額算出手法の違い(OpenAI自身が前回$8,520億→今回$730Bに変動)も未説明。評価額水準が市場環境に大きく依存する。
- gpt-oss-120b/20bのopen weight公開の戦略的意図が不明。围い込み否定として扱っているが、OSSモデルの品質がプロプライエタリモデルに近接すればコモディティ化を加速し、H-OAI-001にもIとして機能する二面性がある。意図が围い込み否定なのかコモディティ化対応なのか判別不能。
- Model-agnostic orchestrationの普及 [INFO-028](../Information/2026-05-29/collected-raw.md#INFO-028) が業界全体トレントであるため、OpenAI固有の弱点ではなく構造的環境変化の可能性がある。コモディティ化下での「支配」の定義が未解決のまま確度評価が継続されている。
- 確証バイアス蓄積のリスク。H-OAI-001が62%→61%→60%と3R連続で低下しており、下方バイアスの自己強化に注意が必要。Red指摘の「業界全体IのOpenAI固有誤分類リスク」は正当だが、誤分類指摘自体も逆方向の確証バイアスの可能性がある。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
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
| [INFO-026](../Information/2026-05-29/collected-raw.md#INFO-026) | Gemini 3.1 Flash Lite $0.25/M入力・Codex価格API token化確認(A-3) |
| [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) | Anthropic SCR指定・連邦控訴裁懐疑的見方(MSN/AP A-2) |
| [INFO-049](../Information/2026-05-29/collected-raw.md#INFO-049) | Anthropic評価額$900B pre-money・Series H $65B完了(NYT A-2) |
