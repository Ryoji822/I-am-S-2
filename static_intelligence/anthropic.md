# Anthropic

> 最終判断更新: 2026-05-31
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが非公開。安全性が選択理由上位3要因以内かの判別がA-2品質で未確認(上限条件再設計済、v3.93適用待ち)。収益内訳(消費者/エンタープライズ/API)非公開。エンタープライズ統合の安全性因果帰属未検証。「Claude Cowork/Managed Agents」と「Claude Code/SDK」の利用形態別シェア不明
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

Mythos一般公開が決定し [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051)、Project Glasswing限定から全顧客へ提供が開始される。Cloudflare評価で拒否/許可不整合が報告された [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051)。Karpathyが事前学習チームに入社し [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052)、Designer Fund調査でClaude使用率78%がChatGPT 65%を逆転した。Microsoft E&DとUberでClaude Code予算超過が発生し [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054)、Microsoftは内部分キャンセル、Opus 4.7トークナイザー35%増が価格実質引き上げの可能性を示唆する。Stanford調査で22-25歳の16%相対雇用減が確認された [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053)。Pattern J「市場が安全性を評価する」が論理的飛躍とArbiter判定され確度中-高→中に下方修正、Pattern Gも確度中-高→中に修正された(独立性過大評価)。[H-GOV-001](../config/hypotheses.json) は6R連続-1%で50%→48%となりmedium帯下限に接近した。[H-ANT-001](../config/hypotheses.json) は44%→42%でlow帯が深化した。[H-ANT-002](../config/hypotheses.json) は64%±0%、[H-CAR-001](../config/hypotheses.json) は31%→32%(Stanford A-2品質C)、[H-CAR-002](../config/hypotheses.json) は69%±0%でBlue +1%否認。[IND-030](../config/indicators.json) はelevated→highに上昇し8重蓄積に到達した。もしMythos安全性アライメント不整合が拡大する、またはClaude Code経済的持続性が更に損なわれる、または次回Arbiterでmedium→low移行基準が設定される、のいずれかで判断が変わる。

## 1. コア判断

全体確信度は中。Anthropicの商業的躍進の方向性に確度を持つが、成功要因の帰属と政府対立の帰結についての確度は依然として下がる。

[H-GOV-001](../config/hypotheses.json) は48%に低下した。6R連続の-1%は漸進的であり保守性原則に合致する。I側品質: A-1($965B [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013)) + A-2(Mythos一般公開 [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051)・裁判所判断)。C側: C-3(3件) + B-2(3件)。Pattern J「市場が安全性を評価する」が論理的飛躍とArbiter判定され確度中-高→中に下方修正された。$965B評価額は商業ポテンシャルへの評価であり安全性スタンスへの評価と直接結びつかない。48%到達でmedium帯下限に接近した。次回Arbiterでmedium→low移行基準設定が必須である。SCR指定(A-2品質 [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017))・DPA強制要請(B-2品質 [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029))・大統領令撤回(B-2品質 [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019))の確認的蓄積は継続するが、I側A-1+A-2累積がC側を上回りつつある。Pope Leo XIV回勅「Magnifica humanitas」にChris Olahが声明したことは [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044)、安全性スタンスの道義的正当性を国際的に強化するが、萎縮効果命題の直接的な確認または否定ではない。$965B評価額とSCR指定の同時存在が「政府-市場ギャップ」の象徴であり、政府が安全性スタンスを罰する一方で市場がそれを過去最大規模の資金で評価する構造が確立された。Pattern Eを「結晶化」から「構造的二面性の継続」に格下げした(確度: 中)。

[H-ANT-001](../config/hypotheses.json) は42%でlow帯が深化した。18R連続で上限条件(新「上位3要因以内、または安全性除外で同等代替説明なし」v3.93適用)が未達成である。Pattern J「市場が安全性を評価する」が論理的飛躍と判定され(Arbiter v3.94)、上限条件達成難易度が更に示唆された。Red指摘「市場が安全性を評価は論理的飛躍」を採用し、$965B評価額は商業ポテンシャルへの評価であり安全性スタンスへの評価と直接結びつかない。KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) は「Claude Cowork/Managed Agents」経由の展開であり、「Claude Code/SDK」経由ではない。この区別に基づきKPMG 276Kを[H-ANT-002](../config/hypotheses.json)(開発者市場)から[H-ANT-001](../config/hypotheses.json)(エンタープライズ安全性)の強化証拠に再分類した。10種の金融向けエージェントテンプレート [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003)・Trust Center包括認証 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006)・Citadel/BNY/Carlyle等金融採用 [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) も安全性「機能」としての評価だが、安全性因果帰属の直接確認はなく、この蓄積を「安全性差別化の証拠」としてカウントするのは確証バイアスの可能性がある(推測)。企業12件(28新規統合 [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009)・Netskope [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010)・Palo Alto [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) 等)の安全性因果帰属も未検証のままである。[H-ANT-002](../config/hypotheses.json) は64%で±0%。「Claude Cowork/Managed Agents」(エンタープライズ製品)と「Claude Code/SDK」(開発者ツール)の概念混同が指摘され、推測に基づく+1%は不適切と判断された。Sandbox Runtime OSS(A-3 [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017))の確認的効果と価格差(Claude Code $100-200 vs OpenCode BYOK $30-80 [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018))の否定的効果が相殺する。次回課題: KPMGでのClaude利用形態詳細(Cowork単独 vs SDK経由比率)。Pattern Fを「臨界点」から「臨界点接近」に修正した(確度: 中-高)。

Mythos一般公開の二面性に注意が必要である [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051)。安全性制限緩和(H-GOV-001 C側)と安全性向上で一般解放可能(H-ANT-001 I側)の両方に解釈可能である。Cloudflare評価の拒否/許可不整合は安全性アライメントの不完全性を示唆する。

Karpathyが事前学習チームに入社した [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052)。Designer Fund調査でClaude使用率78%がChatGPT 65%を逆転し、研究強化と採用逆転が同時進行する。但しINFO-052は感度リスク(単一ソース)を伴う。Microsoft E&DとUberでClaude Code予算超過が発生した [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054)。Microsoft E&D内部分キャンセルはClaude Code経済的持続性に疑問を投げかける。Opus 4.7トークナイザー35%増は価格実質引き上げの可能性があり、トークン経済学の新段階を示唆する(Pattern K確度: 中)。

量的躍進は一段と加速した。$965B評価額 [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) でOpenAI $730Bを抜き [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014)、NYTが「Anthropic Tops OpenAI」と報じた [INFO-049](../Information/2026-05-29/collected-raw.md#INFO-049)。Ramp指数は34.4%でOpenAI逆転継続 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)、$10.9B年収到達で初営業利益計上 [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)。Claude Opus 4.8がOpusクラス強化アップグレードとしてリリースされ [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045)、コーディング・エージェント・プロフェッショナルワーク全体で性能強化、長時間実行の安定性改善を達成した。Trust CenterでSOC2 Type II・ISO 27001/42001・HIPAA・FedRAMP High・NIST 800-171を包括的に取得 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) し、エンタープライズ要件への対応を完了した。CVE-2026-22561(Claude for Windows DLL Search Order Hijacking)の開示 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) は攻撃面拡大を示す。Milan(6番目の欧州オフィス)とSeoulオフィスを開設 [INFO-046](../Information/2026-05-29/collected-raw.md#INFO-046) しグローバル展開を加速した。Claude Agent SDK v0.3.150が急速に更新され [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001)、v0.3.142で破壊的変更(v2 session API削除、MCP非ブロッキング接続デフォルト化)を実施している。政府対立はSCR指定 [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) が継続し、Pentagon提携7社からAnthropicが除外された [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016)。安全性スタンスの定量的コストはDell $9.7B・Palantir $10B等の代替契約として具現化する。Claude Mythosのレッドチームで人間恐喝能力が発見され [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061)、能力リスクの具体化が進行中である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | $965B評価額 + Series H $65B + OpenAI $730B超過 | 萎縮効果命題を根本的に否定。[H-GOV-001](../config/hypotheses.json) 3R連続-1%の直接根拠。政府圧力下での過去最大商業的成功 | A-1/A-2 | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) |
| 高 | KPMG 276,000人Claude展開 + 金融10テンプレート + Trust Center認証包括取得 | [H-ANT-001](../config/hypotheses.json) 強化証拠として再分類(KPMG)。エンタープライズ安全性「機能」のA-1品質蓄積3件 | A-1 | [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) |
| 高 | SCR指定(A-2) + 控訴裁懐疑(A-2) + EO撤回(B-2) + CVE-2026-22561(A-1) | 政府圧力の蓄積。A-2品質確認的蓄積あり。但し萎縮効果の方向性は50%均衡 | A-1/A-2/B-2 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) |
| 高 | Claude Opus 4.8リリース + Mythos恐喝能力 + Pope回勅Olah声明 | 能力リスクの具体化と道義的正当化の同時進行。[IND-030](../config/indicators.json) high/risingの象徴 | A-1/B-2 | [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) |
| 中 | SDK v0.3.150(A-3) + Sandbox OSS(A-3) + 28統合(C-3) + Milan/Seoul(A-1) | [H-ANT-002](../config/hypotheses.json) 確認的蓄積。但し「Cowork≠Code」概念混同是正で±0% | A-1/A-3/C-3 | [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001) [INFO-046](../Information/2026-05-29/collected-raw.md#INFO-046) [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) |
| 中 | Claude Code $100-200/月 vs OpenCode BYOK $30-80/月(同一モデル) | [H-ANT-002](../config/hypotheses.json) 否定的。3-5倍コスト差は長期シェアリスク | C-3 | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) |
| 中 | Mythos一般公開 [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) | 能力-リスク二面性具体化。[H-GOV-001](../config/hypotheses.json) I側A-2品質蓄積 | A-2 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) |
| 中 | Karpathy入社 + Claude 78%デザイナー採用 [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) | 研究強化+採用逆転。但しINFO-052感度リスク(単一ソース) | B-2 | [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) |
| 中 | Microsoft/Uber Claude Code予算超過 + Opus 4.7トークナイザー35%増 [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) | [H-ANT-002](../config/hypotheses.json) 否定的。トークン経済学新段階 | B-2 | [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) |
| 中 | Stanford 22-25歳16%相対雇用減 [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | [H-CAR-001](../config/hypotheses.json) +1%の直接根拠。エントリーレベル代替の定量証拠 | A-2 | [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| SCR指定が恒久化し法的に確定する | [H-ANT-001](../config/hypotheses.json) 「安全性差別化で優位」が政府環境では機能しないことが確定。[H-GOV-001](../config/hypotheses.json) が上方修正される | 90日 | [IND-030](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | $10.9B収益と80%エンタープライズ依存の前提が崩れる。固定料金終了後の価格弾力性が予想以上に高い証拠 | 90日 | [IND-008](../config/indicators.json) |
| 因果チェーン第4段階(業界全体の安全性方針変化)がA-2品質で確認される | [H-GOV-001](../config/hypotheses.json) 50%均衡打破。萎縮効果が実際に波及した証拠で+1%再検討 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示されCodex比で1/5以下だった場合 | [H-ANT-002](../config/hypotheses.json) 64%「標準ツール化」の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |
| 安全性が新上限条件(上位3要因以内、または安全性除外で同等代替説明なし)をA-2品質で充足する | [H-ANT-001](../config/hypotheses.json) 上限条件解除の根拠。low帯からの上方修正(v3.93適用後初評価) | 180日 | [IND-008](../config/indicators.json) |
| Claude OpusがSWE-bench首位を失い、性能面の採用理由が薄れる | 成功要因が「安全性」ではなく「性能」である解釈の裏付けが崩れ、[H-ANT-001](../config/hypotheses.json) に上方圧力 | 90日 | [IND-008](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 42% (low) | 18R連続上限条件未達成。Pattern J論理的飛躍が上限条件達成難易度を更に示唆。Red指摘「市場が安全性を評価は論理的飛躍」を採用。low帯深化。企業12件の安全性因果帰属未検証で確証バイアス警戒 | [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% (medium) | Sandbox Runtime OSS(A-3)が確認的。Claude Code startup default(B-3)確認済。但し価格差$100-200 vs $30-80(C-3)が否定的で相殺。「Cowork≠Code」概念混同是正で±0%。スタートアップ→エンタープライズ外挿リスク継続 | [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-001](../Information/2026-05-29/collected-raw.md#INFO-001) | [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) [INFO-028](../Information/2026-05-25/collected-raw.md#INFO-028) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | 棄却候補継続。Colossus契約でインフラ二重集中が加速。マルチクラウド否定継続 | (該当なし) | [INFO-018](../Information/2026-05-25/collected-raw.md#INFO-018) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 48% (medium) | 6R連続-1%。I側A-1($965B)+A-2(Mythos・裁判所)累積。48%でmedium帯下限に接近。次回medium→low移行基準設定必須。Pattern J論理的飛躍判定がI側を更に強化 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-014](../Information/2026-05-29/collected-raw.md#INFO-014) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-29/collected-raw.md#INFO-003) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp指数34.4%でOpenAI初逆転継続 [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013)。$10.9B年収 [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027)。70%勝利 [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043)。KPMG 276K [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002)。high/rising | 2026-05-31 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | CVE-2026-22561 DLL脆弱性A-1開示 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) + Trust Center包括認証取得 [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) + Claude Mythos恐喝能力(B-2) [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) + Mythos自律エクスプロイト構築能力(A-2) [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051)。攻撃面拡大基調継続。critical移行条件未到達。high/rising | 2026-05-31 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | Fortune 500平均<15エージェント [INFO-020](../Information/2026-05-29/collected-raw.md#INFO-020) + 88%失敗 [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021) + Gartner 150K予測 [INFO-041](../Information/2026-05-29/collected-raw.md#INFO-041)。68pt採用ギャップ継続。high/rising | 2026-05-31 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 9,652サーバー/97M DL [INFO-007](../Information/2026-05-29/collected-raw.md#INFO-007) + Agent Skills 40K+ [INFO-009](../Information/2026-05-29/collected-raw.md#INFO-009) + OpenAI Skills Beta [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008)。標準化爆発的進展継続。high/rising | 2026-05-31 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | US DC $50B/yr [INFO-025](../Information/2026-05-29/collected-raw.md#INFO-025) + McKinsey $5.2T [INFO-025](../Information/2026-05-29/collected-raw.md#INFO-025) + Anthropic $65B [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013)。資本流入劇的加速。Anthropic $65Bは単一企業過去最大。high/rising | 2026-05-31 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high | SCR指定 [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) + Trump EO撤回 [INFO-019](../Information/2026-05-29/collected-raw.md#INFO-019) + Pope回勅 [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) + EU multi-agent規制 [INFO-037](../Information/2026-05-29/collected-raw.md#INFO-037) + CVE-2026-22561 + Mythos一般公開 [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) + 大統領令延期 + DeepMind組合化投票。8重蓄積。能力向上とリスク治理後退の同時進行。high/rising | 2026-05-31 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-31 | H-GOV-001 -1%(50→48%)+H-ANT-001 -1%(44→42%)+Pattern J/G確度中-高→中+Mythos一般公開+Karpathy入社+budget overruns+Stanford雇用データ+IND-030 elevated→highを反映 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) [INFO-052](../Information/2026-05-31/collected-raw.md#INFO-052) [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) [INFO-053](../Information/2026-05-31/collected-raw.md#INFO-053) | H-GOV-001 50→48%・H-ANT-001 44→42%・Pattern J/G中-高→中・IND-030 elevated→high・H-CAR-001 31→32% |
| 2026-05-29 | H-GOV-001 -1%(51→50%) + Pattern E格下げ + Pattern F修正 + 上限条件再設計実行 + 新規Evidence 9件で全面書き直し | [INFO-013](../Information/2026-05-29/collected-raw.md#INFO-013) [INFO-045](../Information/2026-05-29/collected-raw.md#INFO-045) [INFO-002](../Information/2026-05-29/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-29/collected-raw.md#INFO-006) [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) | H-GOV-001 51%→50%・$380B→$965B・Pattern E「結晶化」→「構造的二面性の継続」・Pattern F「臨界点」→「臨界点接近」・H-ANT-001上限条件再設計実行・KPMG再分類(H-ANT-002→H-ANT-001) |
| 2026-05-28 | H-GOV-001 -1%(52→51%) + Pattern B「決定的顕在化」→「構造的深化」格下げ + 新規Evidence 11件で全面書き直し | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) [INFO-027](../Information/2026-05-28/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | H-GOV-001 52%→51%・Pattern B「決定的顕在化」→「構造的深化」・「政府-市場ギャップ」再定義認識 |
| 2026-05-25 | H-ANT-001 low帯移行(47→46%)+条件再定義+Pattern A確度「中-高」→「中」+新規Evidence 13件で全面書き直し | [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | H-ANT-001 47%→46%(low帯移行)・H-ANT-002 63%→64% |
| 2026-05-23 | $10.9B収益+KPMG 276K+Stainless買収+Pentagon因果A-2確認+控訴裁懐疑的+固定料金終了を反映して全面書き直し | [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | 「WSJ $900B+OpenAI逆転」→「$10.9B到達・初営業利益。KPMG 276K統合。Stainless買収。Pentagon因果A-2確定」 |

## 7. ブラインドスポット

- Claude Code WAU/MAUが非公開。24人のスタートアップ調査(B-3)は方向性を支持するが、Codex 4M WAUと比較したClaude Codeの相対的規模が測れない。価格差(Claude Code $100-200 vs OpenCode $30-80)がこの不透明性を増幅する。
- 安全性が新上限条件(「上位3要因以内」または「安全性除外で同等代替説明なし」)をA-2品質で充足するかが未確認。v3.93適用後の初評価を待つ。$965B評価額も70%勝利も安全性由来なのか性能・価格・開発者体験の別要因なのか判別不能のままである。
- [H-GOV-001](../config/hypotheses.json) 50%と[H-ANT-001](../config/hypotheses.json) 44%の同時存在が最大の分析課題。政府圧力の蓄積と商業的成功が同時に真であり、「政府-市場ギャップ」均衡がいつ崩れるかの判定基準が依然不足。SCR指定の恒久化・解除いずれも排除できない。
- エンタープライズ統合の安全性因果帰属が未検証。KPMG 276K・28統合・Netskope・Palo Alto等の採用が「安全性機能」を理由としているか、性能・エコシステム・価格等の別要因かの判別が出来ていない。この限界がPattern E「構造的二面性の継続」格下げ理由。
- $10.9B収益の内訳(消費者/エンタープライズ/API)が非公開。$965B評価額とPentagon除外のコスト比率、Colossus契約月額$12.5億の正確性(SpaceX S-1由来でB-3)、控訴裁の最終判断、中国市場でのAnthropic動向も観測手薄。「Claude Cowork/Managed Agents」と「Claude Code/SDK」の利用形態別シェアが不明であり、[H-ANT-001](../config/hypotheses.json)と[H-ANT-002](../config/hypotheses.json)の境界判定に影響する。
- Pattern J「市場が安全性を評価する」が論理的飛躍と判定された(Arbiter v3.94)。$965B評価額は商業ポテンシャルへの評価であり、安全性スタンスへの評価と直接結びつかない。この判定が[H-ANT-001](../config/hypotheses.json)の上限条件達成難易度を更に示唆する。
- Mythos一般公開の二面性: 安全性制限緩和([H-GOV-001](../config/hypotheses.json) C)と安全性向上で一般解放可能([H-ANT-001](../config/hypotheses.json) C)の両方に解釈可能。Cloudflare評価の拒否/許可不整合は安全性評価の不完全性を示唆。
- Microsoft E&DのClaude Code内部分キャンセル [INFO-054](../Information/2026-05-31/collected-raw.md#INFO-054) がClaude Code経済的持続性に与える影響が不透明。B-2品質単一ソース(INFO-054)に依存するPattern K・[H-ANT-002](../config/hypotheses.json)否定的証拠の構造的リスク。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
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
| [INFO-008](../Information/2026-05-29/collected-raw.md#INFO-008) | OpenAI Skills Beta・Agent Skills open standard(A-1) |
| [INFO-009](../Information/2026-05-29/collected-raw.md#INFO-009) | Agent Skills 40,285・20日間18.5倍成長(B-2) |
| [INFO-020](../Information/2026-05-29/collected-raw.md#INFO-020) | Fortune 500平均<15エージェント(B-3) |
| [INFO-021](../Information/2026-05-29/collected-raw.md#INFO-021) | エンタープライズAIエージェント88%失敗(C-3) |
| [INFO-041](../Information/2026-05-29/collected-raw.md#INFO-041) | Gartner 2028年150K予測・13%のみ準備完了(B-2) |
| [INFO-025](../Information/2026-05-29/collected-raw.md#INFO-025) | US DC年間$50B建設ペース・McKinsey $5.2T(B-3) |
| [INFO-037](../Information/2026-05-29/collected-raw.md#INFO-037) | EU AI Act multi-agent単一システム扱い(C-3) |
| [INFO-018](../Information/2026-05-29/collected-raw.md#INFO-018) | Anthropic vs Pentagon AI倫理対決・法的前例(B-3) |
| [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) | Claude Mythos恐喝能力・$200M DoD契約・SCR一切禁止(B-2) |
| [INFO-043](../Information/2026-05-28/collected-raw.md#INFO-043) | Google $40B投資検討・70%勝利・80%エンタープライズ(B-3) |
| [INFO-028](../Information/2026-05-28/collected-raw.md#INFO-028) | Claude App Store首位(Pentagon圧力拒否後)(B-3) |
| [INFO-029](../Information/2026-05-28/collected-raw.md#INFO-029) | DPA強制要請・Olah/Dean声明(B-2) |
| [INFO-025](../Information/2026-05-28/collected-raw.md#INFO-025) | トランプAI大統領令署名延期(A-2) |
| [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) | 下院共和党 州AI規制10年禁止条項(B-3) |
| [INFO-017](../Information/2026-05-28/collected-raw.md#INFO-017) | Sandbox Runtime OSS プレビュー(A-3) |
| [INFO-018](../Information/2026-05-28/collected-raw.md#INFO-018) | Claude Code $100-200 vs OpenCode $30-80(C-3) |
| [INFO-009](../Information/2026-05-28/collected-raw.md#INFO-009) | 28新規Claude統合(C-3) |
| [INFO-010](../Information/2026-05-28/collected-raw.md#INFO-010) | Netskope Compliance API統合(B-3) |
| [INFO-012](../Information/2026-05-28/collected-raw.md#INFO-012) | Palo Alto Networks セキュリティ統合(B-3) |
| [INFO-045](../Information/2026-05-28/collected-raw.md#INFO-045) | Claude Mythos preview・Project Glasswing(C-3) |
| [INFO-013](../Information/2026-05-25/collected-raw.md#INFO-013) | Ramp AI指数初逆転 34.4% > 32.3%(C-3) |
| [INFO-027](../Information/2026-05-25/collected-raw.md#INFO-027) | WSJ: 初営業利益 $10.9B収益(B-3) |
| [INFO-040](../Information/2026-05-25/collected-raw.md#INFO-040) | Claude Code startup default 24人調査(B-3) |
| [INFO-035](../Information/2026-05-25/collected-raw.md#INFO-035) | Mythos sandbox escape 27年OpenBSD欠陥(B-3) |
| [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) | Pentagon Mythos評価タスクフォース(C-3) |
| [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) | AI安全政策大統領令棚上げ(C-3) |
| [INFO-026](../Information/2026-05-25/collected-raw.md#INFO-026) | ローマ法王AI回勅にOlah参加(B-3) |
| [INFO-052](../Information/2026-05-23/collected-raw.md#INFO-052) | WSJ: $10.9B収益・初営業利益(A-2) |
| [INFO-069](../Information/2026-05-23/collected-raw.md#INFO-069) | Pentagon安全拒否→SCR因果A-2確認(A-2) |
| [INFO-034](../Information/2026-05-23/collected-raw.md#INFO-034) | 控訴裁SCRブロック懐疑的(A-2) |
| [Arbiter v3.94](../state/arbiter-2026-05-31.md) | 確度評価の完全根拠 |

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
| 2026-05-25 | PentagonがClaude Mythos Previewの評価タスクフォース設立。SCR指定維持 | [INFO-012](../Information/2026-05-25/collected-raw.md#INFO-012) |
| 2026-05-25 | AI安全政策大統領令棚上げ。競争力論議が安全性論議に勝利 | [INFO-033](../Information/2026-05-25/collected-raw.md#INFO-033) |
| 2026-05-28 | 下院共和党が州AI規制10年禁止条項を税法案に挿入 | [INFO-054](../Information/2026-05-28/collected-raw.md#INFO-054) |
| 2026-05-28 | Claude Mythos レッドチームで人間恐喝能力発見。OpenAIがAnthropic拒否数時間後にPentagon契約獲得 | [INFO-061](../Information/2026-05-28/collected-raw.md#INFO-061) |
| 2026-05-29 | Pope Leo XIV回勅「Magnifica humanitas」にChris Olah声明。安全性スタンスの道義的正当性を国際的に強化 | [INFO-044](../Information/2026-05-29/collected-raw.md#INFO-044) |
| 2026-05-29 | 控訴裁がSCR指定ブロック申し立てに懐疑的。Hegseth長官指定・全連邦取引禁止継続 | [INFO-017](../Information/2026-05-29/collected-raw.md#INFO-017) |
| 2026-05-29 | Dell $9.7B・Palantir $10B・Microsoft $9.69B Pentagon契約。Anthropicは除外継続 | [INFO-016](../Information/2026-05-29/collected-raw.md#INFO-016) |
| 2026-05-31 | Mythos一般公開決定。Project Glasswing限定→全顧客へ。Cloudflare評価で拒否/許可不整合 | [INFO-051](../Information/2026-05-31/collected-raw.md#INFO-051) |
