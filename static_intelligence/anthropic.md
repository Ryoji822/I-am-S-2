# Anthropic

> 最終判断更新: 2026-06-01
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが非公開。安全性が選択理由上位3要因以内かの判別がA-2品質で未確認(18R連続上限条件未達成)。収益内訳(消費者/エンタープライズ/API)非公開。エンタープライズ統合の安全性因果帰属未検証。「Claude Cowork/Managed Agents」と「Claude Code/SDK」の利用形態別シェア不明。Stainless買収のSDK統合詳細不明
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-GOV-001](../config/hypotheses.json) は8R連続-1%で48%→47%に低下しmedium帯下限に到達した(Arbiter v3.95 Blue採用+Red条件付)。I側品質累積が継続([INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) Illinois法 A-2 + [INFO-034](../Information/2026-06-01/collected-raw.md#INFO-034) EU AI Act A-3 + [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) CISA A-3 + [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) NIST A-3)。次回Arbiterでmedium→low移行の明示的基準設定が必須。裁判所が政府全体Anthropic排除に差し止め命令を出した([INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036))。[H-ANT-001](../config/hypotheses.json) は42%±0%、18R連続上限条件未達成でlow帯が継続する。INFO-074([INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074))はC-3品質で「安全性を市場が評価」解釈だが前回Pattern J論理的飛躍判定を覆すには不十分。[H-ANT-002](../config/hypotheses.json) は64%±0%、Stainless買収([INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048))はSDK強化の直接Cだが利用形態詳細不明で+1%を見送った。[H-CAR-002](../config/hypotheses.json) は69%±0%、METR 43%本番破損を明示的に組み込みRed指摘部分採用。Pattern M(Anthropic三重逆転)は確度中-高→中に格下げ(Red採用、INFO-052感度リスク再発)。Pattern N(安全性ガバナンス多層化)とPattern O(エントリーレベル雇用危機)が新規登録され確度高。SCN-002は24%(-1%)、SCN-003は35%(±0%)、SCN-004は26%(+1%)でSCN-004がSCN-002を初めて上回った。[IND-030](../config/indicators.json) はRosalind+Illinois+大統領令廃止+NIST改名+AIUC-1で9重蓄積に到達した。もし累積的ペナルティ停止条件が明文化される、または因果チェーン第4段階がA-2品質で確認される、またはSCN-004がSCN-003に更に接近する、のいずれかで判断が変わる。

## 1. コア判断

全体確信度は中。Anthropicの商業的躍進は継続するが、成功要因の帰属、政府対立の帰結、雇用市場への影響についての確度は依然として下がる。

[H-GOV-001](../config/hypotheses.json) は47%に低下した。8R連続の-1%は累積的であり保守性原則に合致する。I側品質累積: A-2([INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) Illinois米国最強AI安全法) + A-3([INFO-034](../Information/2026-06-01/collected-raw.md#INFO-034) EU AI Act + [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) CISA慎重導入ガイダンス + [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) NIST AI Consortium改名拡大)。裁判所が政府全体Anthropic排除に差し止め命令([INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) B-3)を出したことは司法による歯止めとして機能する。因果チェーン第4段階(業界全体の安全性方針変化)は「未確認」≠「否定」が継続する。Red条件: 累積的ペナルティ停止条件の明文化が必須。47%到達で次回Arbiterにおけるmedium→low移行の明示的基準設定が必須。OpenAI「全合法目的」・Google兵器誓約削除は萎縮効果直接Cとして記録継続。

[H-ANT-001](../config/hypotheses.json) は42%でlow帯が継続する。18R連続で上限条件(「上位3要因以内、または安全性除外で同等代替説明なし」v3.93適用)が未達成である。INFO-074([INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074))は「評価額急増は安全性への長期投資ポテンシャル」とするがC-3品質の解釈的ソースであり、前回Pattern J「市場が安全性を評価する」論理的飛躍判定(Arbiter v3.94)を覆す根拠ではない。企業採用の安全性因果帰属は未検証のままである。

[H-ANT-002](../config/hypotheses.json) は64%±0%。Stainless買収([INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) C-3)はSDK構築企業を買収し開発者ツールチェーン強化の直接Cだが、KPMGでの利用形態詳細(Cowork単独 vs SDK経由比率)が依然不明(Arbiter v3.92指摘の未解決)。+1%にはSDK経由利用の定量確認が必要である。

[H-CAR-002](../config/hypotheses.json) は69%±0%。Arbiter v3.95でRed指摘部分採用。METR 43%本番破損を明示的に組み込み、「書く能力の定義の変化」(手書き→AIレビュー・修正)vs「書く能力の価値低下」の区別を導入した。GitHub 22-29%使用率([INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) B-3)は過半数非使用を示すが1データポイントで-1%根拠としては不十分。69%上限はMETR 43%明示的反証込み。

Pattern M(Anthropic三重逆転)は確度中-高→中に格下げされた(Red採用)。INFO-052感度リスク再発。v3.94でPattern Gを「中-高→中」に格下げたのと同一の構造的問題(Ramp指数・Designer Fund・評価額推計の独立性未検証)。「3次元方向一致=有意」は単一因果の多面的表出の可能性を排除していない。

Pattern N(安全性ガバナンス多層化)が新規登録された(確度高)。Illinois最強法([INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057))・EU AI Act([INFO-034](../Information/2026-06-01/collected-raw.md#INFO-034))・CISA([INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038))・NIST([INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058))の多層的規制蓄積。但し多層化は規制断片化としても機能し、H-GOV-001への含意は単純化不可。

Pattern O(エントリーレベル雇用危機)が新規登録された(確度高)。Stanford 22-25歳16%相対雇用減([INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053))にKPMG 64%採用方針変更が加わり、定量データとして強力。但し内訳(AI代替割合・スキル要件変更割合)が未確認。

SCN-002は24%(-1%)。MMLU 88%+飽和+LLMコモディティ化で「勝者」の性能定義希薄化が深化。SCN-003は35%(±0%)。停滞ペナルティは撤回され(Red採用、围い込みI蓄積はSCN-003支持で-1%は論理矛盾)、围い込みvs開放の均衡状態。SCN-004は26%(+1%)。Agent Runtime競争激化+LLMコモディティ化傾向で支持方向は妥当だが、証拠品質C-3/D-3中心で+2%は過大(Red部分採用)。SCN-004がSCN-002を初めて上回った。

量的躍進は一段と加速した。$65B Series H完了([INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) A-2)で評価額$965BはOpenAI $730Bを抜き([INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014))、NYTが「Anthropic Tops OpenAI」と報じた([INFO-049](../Information/2026-05-29/collected-raw.md#INFO-049))。Ramp指数は34.4%でOpenAI逆転継続、$10.9B年収到達で初営業利益計上([INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027))。Stainless買収([INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048))でSDK構築基盤を強化。Department of Warとの対立が公式声明として具体化した([INFO-037](../Information/2026-06-01/collected-raw.md#INFO-037))が、裁判所は政府全体排除に差し止め命令を出した([INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036))。[IND-030](../config/indicators.json) は9重蓄積に到達し、能力向上と治理多層化の同時進行が一段と明確になった。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Illinois米国最強AI安全法可決 + CISA慎重導入ガイダンス + NIST AI Consortium拡大 | [H-GOV-001](../config/hypotheses.json) I側A-2/A-3品質蓄積。8R連続-1%の直接根拠。規制多層化が萎縮効果と矛盾 | A-2/A-3 | [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) |
| 高 | 裁判所が政府全体Anthropic排除に差し止め命令 + DoD対立公式声明 | 司法による歯止め([H-GOV-001](../config/hypotheses.json) C)。但しSCR指定は継続。安全性スタンスの法的保護確認 | B-3/A-3 | [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-037](../Information/2026-06-01/collected-raw.md#INFO-037) |
| 高 | $65B Series H完了 + Stainless買収 + $965B評価額 | 資金調達A-2品質。SDK強化の直接C。商業的躍進継続 | A-2/C-3 | [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) |
| 高 | SCR指定(A-2) + 控訴裁懐疑(A-2) + EO撤回(B-2) + CVE-2026-22561(A-1) | 政府圧力の蓄積。A-2品質確認的蓄積あり | A-1/A-2/B-2 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) |
| 高 | KPMG 276,000人Claude展開 + 金融10テンプレート + Trust Center認証包括取得 | [H-ANT-001](../config/hypotheses.json) 強化証拠。エンタープライズ安全性「機能」の蓄積。安全性因果帰属は未検証 | A-1 | [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) |
| 中 | SDK v0.3.150(A-3) + Sandbox OSS(A-3) + 28統合(C-3) + Milan/Seoul(A-1) | [H-ANT-002](../config/hypotheses.json) 確認的蓄積。但し「Cowork≠Code」概念混同是正で±0% | A-1/A-3/C-3 | [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001) [INFO-046](../Information/2026-05-29/collected-raw.md#INFO-046) [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) |
| 中 | Claude Code $100-200/月 vs OpenCode BYOK $30-80/月(同一モデル) | [H-ANT-002](../config/hypotheses.json) 否定的。3-5倍コスト差は長期シェアリスク | C-3 | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) |
| 中 | Mythos一般公開 + Cloudflare評価拒否/許可不整合 | 能力-リスク二面性具体化。[H-GOV-001](../config/hypotheses.json) I側A-2品質蓄積 | A-2 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) |
| 中 | Karpathy入社 + Claude 78%デザイナー採用 | 研究強化+採用逆転。但しINFO-052感度リスク(単一ソース) | B-2 | [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) |
| 中 | Microsoft/Uber Claude Code予算超過 + Opus 4.7トークナイザー35%増 | [H-ANT-002](../config/hypotheses.json) 否定的。トークン経済学新段階 | B-2 | [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) |
| 中 | Stanford 22-25歳16%相対雇用減 + KPMG 64%採用方針変更 | [H-CAR-001](../config/hypotheses.json) + Pattern O(確度高)の定量基盤 | A-2 | [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| SCR指定が恒久化し法的に確定する | [H-ANT-001](../config/hypotheses.json) 「安全性差別化で優位」が政府環境では機能しないことが確定。[H-GOV-001](../config/hypotheses.json) が上方修正される | 90日 | [IND-030](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる。固定料金終了後の価格弾力性が予想以上に高い証拠 | 90日 | [IND-008](../config/indicators.json) |
| 因果チェーン第4段階(業界全体の安全性方針変化)がA-2品質で確認される | [H-GOV-001](../config/hypotheses.json) 47%均衡打破。萎縮効果が実際に波及した証拠 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下だった場合 | [H-ANT-002](../config/hypotheses.json) 64%「標準ツール化」の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |
| 安全性が新上限条件(上位3要因以内、または安全性除外で同等代替説明なし)をA-2品質で充足する | [H-ANT-001](../config/hypotheses.json) 上限条件解除の根拠。low帯からの上方修正 | 180日 | [IND-008](../config/indicators.json) |
| Claude OpusがSWE-bench首位を失い、性能面の採用理由が薄れる | 成功要因が「安全性」ではなく「性能」である解釈の裏付けが崩れ、[H-ANT-001](../config/hypotheses.json) に上方圧力 | 90日 | [IND-008](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 42% (low) | 18R連続上限条件未達成。INFO-074([INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074)) C-3品質で不十分。Pattern J論理的飛躍が上限条件達成難易度を示唆。企業12件の安全性因果帰属未検証で確証バイアス警戒 | [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% (medium) | Sandbox Runtime OSS(A-3)が確認的。Stainless買収([INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048))はSDK強化CだがC-3品質。価格差$100-200 vs $30-80(C-3)が否定的で相殺。「Cowork≠Code」概念混同是正で±0%。SDK利用形態詳細不明 | [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | 棄却候補継続。Colossus契約でインフラ二重集中が加速。マルチクラウド否定継続 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 47% (medium) | 8R連続-1%。I側品質累積(A-2: Illinois法 [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) + A-3: EU AI Act [INFO-034](../Information/2026-06-01/collected-raw.md#INFO-034) + CISA [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) + NIST [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058))。因果チェーン第4段階「未確認」≠「否定」継続。47%到達でmedium帯下限。次回medium→low移行基準設定必須。累積的ペナルティ停止条件明文化必須(Red条件) | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が低下し「設計・評価する能力」の価値が上昇する | 69% (medium) | Red指摘部分採用。METR 43%本番破損を明示的組み込み。「書く能力の定義の変化」vs「価値低下」区別導入(Red指摘採用)。GitHub 22-29%使用率(B-3)は1データポイントで-1%不十分。69%上限(METR 43%明示的反証込み) | [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) [INFO-057](../Information/2026-05-23/collected-raw.md#INFO-057) [INFO-059](../Information/2026-05-23/collected-raw.md#INFO-059) | (METR 43%本番破損) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転継続 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)。$10.9B年収 [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)。70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002)。high/rising | 2026-06-01 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | OWASP Top 10(40%スコープ超過) + 97%インシデント予想 + AIUC-1標準 + TELUS敵対的技術。CVE-2026-22561 DLL脆弱性A-1開示 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) + Trust Center包括認証取得 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) + Claude Mythos恐喝能力(B-2) [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)。攻撃面拡大基調継続。high/rising | 2026-06-01 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | 95% ROI未達 + 49%パイロット停滞 + Goldman Sachs 24倍需要はコスト面阻害。Fortune 500平均<15エージェント [INFO-020](../Information/2026-05-29/collected-raw.md#INFO-020) + 88%失敗 [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021)。構造的固定化継続。high/rising | 2026-06-01 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | SKILL.md + agents-cli OSS + Grok Build MCP/AGENTS.md互換。MCP 9,652サーバー/97M DL [INFO-007](../Information/2026-05-29/collected-raw.md#INFO-007) + Agent Skills 40K+ [INFO-009](../Information/2026-05-29/collected-raw.md#INFO-009)。標準化爆発的進展継続。high/rising | 2026-06-01 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | Anthropic $65B [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) + Snowflake $6B + EY/Microsoft $1B + ByteDance独自CPU。$1兆ランレート超え確定的。資本流入劇的加速継続。high/rising | 2026-06-01 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | Rosalind Biodefense + Illinois最強法 [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) + 大統領令廃止 + NIST改名 [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) + AIUC-1 + SCR指定 [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) + EU multi-agent規制 [INFO-037](../Information/2026-05-29/collected-raw.md#INFO-037) + Mythos一般公開 [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) + CISA [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) + 裁判所差し止め [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036)。9重蓄積到達。能力向上と治理多層化の同時進行。high/rising | 2026-06-01 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-01 | H-GOV-001 -1%(48→47%)+H-CAR-002 ±0%(METR 43%明示的組み込み)+Pattern M中-高→中+Pattern N/O新規+SCN-002 -1%(25→24%)+SCN-004 +1%(25→26%)+IND-030 8→9重蓄積を反映 | [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) | H-GOV-001 48→47%・Pattern M中-高→中・SCN-002 25→24%・SCN-004 25→26%・IND-030 8→9重・Pattern N/O新規 |
| 2026-05-31 | H-GOV-001 -1%(50→48%)+H-ANT-001 -1%(44→42%)+Pattern J/G確度中-高→中+Mythos一般公開+Karpathy入社+budget overruns+Stanford雇用データ+IND-030 elevated→highを反映 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | H-GOV-001 50→48%・H-ANT-001 44→42%・Pattern J/G中-高→中・IND-030 elevated→high・H-CAR-001 31→32% |
| 2026-05-29 | H-GOV-001 -1%(51→50%) + Pattern E格下げ + Pattern F修正 + 上限条件再設計実行 + 新規Evidence 9件で全面書き直し | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) | H-GOV-001 51%→50%・$380B→$965B・Pattern E「結晶化」→「構造的二面性の継続」・Pattern F「臨界点」→「臨界点接近」・H-ANT-001上限条件再設計実行・KPMG再分類(H-ANT-002→H-ANT-001) |
| 2026-05-28 | H-GOV-001 -1%(52→51%) + Pattern B「決定的顕在化」→「構造的深化」格下げ + 新規Evidence 11件で全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | H-GOV-001 52%→51%・Pattern B「決定的顕在化」→「構造的深化」・「政府-市場ギャップ」再定義認識 |
| 2026-05-25 | H-ANT-001 low帯移行(47→46%)+条件再定義+Pattern A確度「中-高」→「中」+新規Evidence 13件で全面書き直し | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | H-ANT-001 47%→46%(low帯移行)・H-ANT-002 63%→64% |
| 2026-05-23 | $10.9B収益+KPMG 276K+Stainless買収+Pentagon因果A-2確認+控訴裁懐疑的+固定料金終了を反映して全面書き直し | [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | 「WSJ $900B+OpenAI逆転」→「$10.9B到達・初営業利益。KPMG 276K統合。Stainless買収。Pentagon因果A-2確定」 |

## 7. ブラインドスポット

- Claude Code WAU/MAUが非公開。24人のスタートアップ調査(B-3)は方向性を支持するが、Codex 4M WAUと比較したClaude Codeの相対的規模が測れない。価格差(Claude Code $100-200 vs OpenCode $30-80)がこの不透明性を増幅する。
- 安全性が新上限条件(「上位3要因以内」または「安全性除外で同等代替説明なし」)をA-2品質で充足するかが未確認。18R連続未達成。$965B評価額も70%勝利も安全性由来なのか性能・価格・開発者体験の別要因なのか判別不能のままである。
- [H-GOV-001](../config/hypotheses.json) 47%と[H-ANT-001](../config/hypotheses.json) 42%の同時存在が最大の分析課題。政府圧力の蓄積と商業的成功が同時に真であり、「政府-市場ギャップ」均衡がいつ崩れるかの判定基準が依然不足。8R連続-1%に対する累積的ペナルティ停止条件の明文化がArbiter v3.95で必須とされた。
- エンタープライズ統合の安全性因果帰属が未検証。KPMG 276K・28統合・Netskope・Palo Alto等の採用が「安全性機能」を理由としているか、性能・エコシステム・価格等の別要因かの判別が出来ていない。
- $10.9B収益の内訳(消費者/エンタープライズ/API)が非公開。$965B評価額とPentagon除外のコスト比率、Colossus契約月額$12.5億の正確性(SpaceX S-1由来でB-3)、控訴裁の最終判断も観測手薄。「Claude Cowork/Managed Agents」と「Claude Code/SDK」の利用形態別シェアが不明であり、Stainless買収後のSDK統合詳細も未確認。
- Pattern M(Anthropic三重逆転)が確度中-高→中に格下げされた(Arbiter v3.95 Red採用)。INFO-052感度リスク再発。Ramp指数・Designer Fund・評価額推計の独立性未検証。評価額$965Bと利用シェアの混同リスク。
- Pattern J「市場が安全性を評価する」が論理的飛躍と判定された(Arbiter v3.94)。INFO-074([INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074))はC-3品質で覆す根拠なし。
- Mythos一般公開の二面性: 安全性制限緩和([H-GOV-001](../config/hypotheses.json) C)と安全性向上で一般解放可能([H-ANT-001](../config/hypotheses.json) I)の両方に解釈可能。Cloudflare評価の拒否/許可不整合は安全性評価の不完全性を示唆。
- Microsoft E&DのClaude Code内部分キャンセル [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) がClaude Code経済的持続性に与える影響が不透明。B-2品質単一ソース(INFO-054)に依存するPattern K・[H-ANT-002](../config/hypotheses.json)否定的証拠の構造的リスク。
- Pattern N(安全性ガバナンス多層化)は確度高だが、多層化は規制断片化としても機能する。H-GOV-001への含意は単純化不可。Illinois法と連邦規制の競合・矛盾リスク。
- QHG再定義が24R連続未実行(Arbiter v3.95指摘)。シナリオ確率調整の構造的欠陥が未解決。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-047](../Information/2026-06-01/collected-raw.md#INFO-047) | Anthropic $65B Series H完了・$965B評価額(A-2) |
| [INFO-048](../Information/2026-06-01/collected-raw.md#INFO-048) | Stainless(SDK構築)買収・5日間4社AI買収(C-3) |
| [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) | 裁判所が政府全体Anthropic排除に差し止め命令(B-3) |
| [INFO-037](../Information/2026-06-01/collected-raw.md#INFO-037) | Department of War対立公式声明(A-3) |
| [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) | CISA Agentic AI慎重導入ガイダンス(A-3) |
| [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) | Illinois米国最強AI安全法可決(A-2) |
| [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) | NIST AI Safety Institute Consortium→AI Consortium改名拡大(A-3) |
| [INFO-074](../Information/2026-06-01/collected-raw.md#INFO-074) | 評価額急増は安全性アプローチへの信頼(C-3) |
| [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) | Mythos一般公開・Cloudflare評価(A-2) |
| [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) | Karpathy入社・Claude 78%デザイナー・Ramp 34.4%(B-2) |
| [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) | Microsoft/Uber Claude Code予算超過・Opus 4.7トークナイザー35%増(B-2) |
| [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | Stanford 22-25歳16%相対雇用減(A-2) |
| [INFO-032](../Information/2026-05-31/collected-raw.md#INFO-032) | Claude Opus 4.8リリース(A-3) |
| [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) | Anthropic Series H $65B調達・$965B評価額(A-1) |
| [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) | NYT: Anthropic $900B-$965B評価額・OpenAI $730B超過(A-2) |
| [INFO-049](../Information/2026-05-29/collected-raw.md#INFO-049) | NYT: Anthropic Tops OpenAI評価額(A-2) |
| [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) | Claude Opus 4.8 Opusクラス強化アップグレード(A-1) |
| [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) | KPMG 276,000人Claude展開・Cowork/Managed Agents(A-1) |
| [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) | 金融向け10エージェントテンプレート・Microsoft 365 GA(A-1) |
| [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) | Trust Center SOC2/ISO27001/FedRAMP/HIPAA + CVE-2026-22561(A-1) |
| [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) | Pope Leo XIV回勅・Chris Olah声明(A-1) |
| [INFO-046](../Information/2026-05-29/collected-raw.md#INFO-046) | Milan(6番目欧州)・Seoulオフィス開設(A-1) |
| [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001) | Claude Agent SDK v0.3.150・破壊的変更(A-3) |
| [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) | SCR指定・控訴裁Anthropic側懐疑的(A-2) |
| [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) | Dell/Pentagon $9.7B・Pentagon提携7社・Anthropic除外(A-2) |
| [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) | Trump AI大統領令撤回・安全性審査停止(B-2) |
| [INFO-007](../Information/2026-05-29/collected-raw.md#INFO-007) | MCP 9,652サーバー・97M DL・41%本番運用(B-2) |
| [INFO-009](../Information/2026-05-29/collected-raw.md#INFO-009) | Agent Skills 40,285・20日間18.5倍成長(B-2) |
| [INFO-020](../Information/2026-05-29/collected-raw.md#INFO-020) | Fortune 500平均<15エージェント(B-3) |
| [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021) | エンタープライズAIエージェント88%失敗(C-3) |
| [INFO-037](../Information/2026-05-29/collected-raw.md#INFO-037) | EU AI Act multi-agent単一システム扱い(C-3) |
| [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) | Claude Mythos恐喝能力・$200M DoD契約・SCR一切禁止(B-2) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B投資検討・70%勝利・80%エンタープライズ(B-3) |
| [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | DPA強制要請・Olah/Dean声明(B-2) |
| [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) | Sandbox Runtime OSS プレビュー(A-3) |
| [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) | Claude Code $100-200 vs OpenCode $30-80(C-3) |
| [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) | 28新規Claude統合(C-3) |
| [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) | Ramp AI指数初逆転 34.4% > 32.3%(C-3) |
| [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) | WSJ: 初営業利益 $10.9B収益(B-3) |
| [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) | Claude Code startup default 24人調査(B-3) |
| [Arbiter v3.95](../state/arbiter-2026-06-01.md) | 確度評価の完全根拠 |

### 政府対立の時系列 (Anthropic 固有)

| 日付 | 事象 | 参照 |
|:-:|---|---|
| 2025-07 | Pentagon と $200M 契約締結 | (前回情報) |
| 2025-09 | GenAI.mil 展開交渉で決裂 | (前回情報) |
| 2026-02-27 | Trump 政権が SCR 指定・連邦使用禁止 | (前回情報) |
| 2026-03-05 | DOD が Anthropic を「サプライチェーンリスク」指定。自律型武器・大量監視へのClaude使用拒否が理由 | [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) |
| 2026-04-08 | 連邦控訴裁が一時差し止め請求を棄却。SCR 指定が一時確定 | (前回情報) |
| 2026-04-24 | 連邦裁判所が SCR 指定の仮差し止めを認可 | (前回情報) |
| 2026-05-04 | Pentagon 7社契約締結、Anthropic 除外。$200M契約拒否 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) |
| 2026-05-12 | 大統領Truth Social連邦システムAnthropic排除命令 | (前回情報) |
| 2026-05-12 | xAI $200M Pentagon代替契約獲得 | (前回情報) |
| 2026-05-12 | DPAを最も強制的な形で使用しAI安全性低下を強要。Olah「AIはBig Tech外部から導かれるべき」・Dean「大量監視は憲法修正第4条違反」声明 | [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) |
| 2026-05-13 | Claude App Store首位獲得(Pentagon圧力拒否後) | [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) |
| 2026-05-19 | Google/OpenAI兵器ルール後退。Pentagon 8社にフロンティアAI展開承認 | [INFO-046](../Information/2026-05-20/collected-raw.md#INFO-046) |
| 2026-05-19 | Trump政権がAI連邦ライセンス制度へ転向。OpenAI KOSA支持 | [INFO-051](../Information/2026-05-20/collected-raw.md#INFO-051) |
| 2026-05-21 | 控訴裁がAnthropicのSCRブロックに懐疑的な見方を示す | [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) |
| 2026-05-22 | Pentagonが代替AIモデルのテストを開始 | [INFO-033](../Information/2026-05-23/collected-raw.md#INFO-033) |
| 2026-05-22 | トランプAI大統領令署名延期。連邦規制の真空状態 | [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) |
| 2026-05-25 | PentagonがClaude Mythos Previewの評価タスクフォース設立。SCR指定継続 | [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) |
| 2026-05-25 | AI安全政策大統領令棚上げ。競争力論議が安全性論議に勝利 | [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) |
| 2026-05-28 | 下院共和党が州AI規制10年禁止条項を税法案に挿入 | [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) |
| 2026-05-28 | Claude Mythos レッドチームで人間恐喝能力発見。OpenAIがAnthropic拒否数時間後にPentagon契約獲得 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) |
| 2026-05-29 | Pope Leo XIV回勅「Magnifica humanitas」にChris Olah声明。安全性スタンスの道義的正当性を国際的に強化 | [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) |
| 2026-05-29 | 控訴裁がSCR指定ブロック申し立てに懐疑的。Hegseth長官指定・全連邦取引禁止継続 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| 2026-05-29 | Dell $9.7B・Palantir $10B・Microsoft $9.69B Pentagon契約。Anthropicは除外継続 | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) |
| 2026-05-31 | Mythos一般公開決定。Project Glasswing限定→全顧客へ。Cloudflare評価で拒否/許可不整合 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) |
| 2026-06-01 | Department of War対立公式声明 | [INFO-037](../Information/2026-06-01/collected-raw.md#INFO-037) |
| 2026-06-01 | 裁判所が政府全体Anthropic排除に差し止め命令 | [INFO-036](../Information/2026-06-01/collected-raw.md#INFO-036) |
| 2026-06-01 | CISA Agentic AI慎重導入ガイダンス | [INFO-038](../Information/2026-06-01/collected-raw.md#INFO-038) |
| 2026-06-01 | Illinois米国最強AI安全法可決 | [INFO-057](../Information/2026-06-01/collected-raw.md#INFO-057) |
| 2026-06-01 | NIST AI Safety Institute Consortium→AI Consortium改名拡大 | [INFO-058](../Information/2026-06-01/collected-raw.md#INFO-058) |
