# Anthropic

> 最終判断更新: 2026-05-14
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが40R連続非公開。中国市場との競合観測は手薄
> 主参照: hypotheses.json#H-ANT-001/002/003, hypotheses.json#H-GOV-001, indicators.json#IND-008/013/023/027/030

## 0. 一文要約

我々はAnthropicを、**安全性堅持で民間市場を獲得しながら、政府からの構造的抑圧(Supply Chain Risk指定+国防生産法脅迫)に直面している企業**と読んでいる。最大の根拠は、PentagonがAnthropicを米企業として初めてSCR指定し [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033)、DPA発動を脅迫した事実 [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) と、それにもかかわらずClaude Mythos PreviewがSWE-bench Multimodalで59%を達標し [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026)、Opus 4.7がSWE-bench Proで64.3%を記録した事実 [INFO-055](../Information/2026-05-14/collected-raw.md#INFO-055)。民間市場では年次化収益$300億、Fortune 10中8社顧客が安全性の市場有効性を示している [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006)。GoogleがPentagonと秘密AI契約を結び [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036)、Scale AI契約が$5億に増額された [INFO-038](../Information/2026-05-14/collected-raw.md#INFO-038) ことで、Anthropicの拒否と競合の受諾という対比が明確になった。Claude Code WAUが定量開示される、またはDPAが実際に発動される、またはGoogle秘密契約の詳細が判明する、のいずれかが観測されたら判断の前提が変わる。

## 1. コア判断

Anthropicの構図は「安全性が民間市場では報われ、政府市場では構造的抑圧に直面する」という二極化にある。前回(2026-05-13)の「政府除外の因果チェーンが未確認」という評価は、Pentagon SCR指定+DPA脅迫によって「政府関係が構造的対立に深化」に更新する。

政府側は急激に悪化した。PentagonがAnthropicを米企業として初めてSCR(supply chain risk)に指定し、全連邦機関に使用停止を命じた [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033)。国防長官HegsethがDPA(Defense Production Act)発動を脅迫した [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046)。Pentagon CTOはAnthropicをDODベンダーから除外すると表明したが、Claude Mythosは既にPentagon内部で運用されているという矛盾も確認された [INFO-034](../Information/2026-05-14/collected-raw.md#INFO-034)。この対比は深刻だ。GoogleがPentagonと秘密AI契約を締結し、数百人の従業員が抗議した [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036)。Scale AI契約は$1億から$5億に増額され、Metaが49%出資している [INFO-038](../Information/2026-05-14/collected-raw.md#INFO-038)。Anthropic(拒否)とGoogle(受諾)の立場の違いが明確になった。H-GOV-001は6つのC証拠が蓄積し47%に上昇した [H-GOV-001](../config/hypotheses.json)。

民間側は強い。Claude Mythos PreviewがSWE-bench Multimodalで59%を達成し、XBOWとUK AISIの独立評価が自律的サイバーセキュリティでの飛躍的改善を確認した [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026)。Opus 4.7はSWE-bench Proで64.3%を記録し、GPT-5.4とGemini 3.1 Proを上回った [INFO-055](../Information/2026-05-14/collected-raw.md#INFO-055)。Agent SDK v0.2.131がClaude Code v2.1.131とパリティを達成し、6月15日から有料プランでAgent SDKクレジットが開始される。OpenClaw等のサードパーティエージェント利用も再開された [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010)。Sandbox Runtimeがオープンソース化され、Claude Codeの安全なエージェント実行環境が提供された [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027)。Colossus 1契約でOpus APIレート制限が30Kから500K input tokens/minに引き上げられ、約16倍の向上となった [INFO-044](../Information/2026-05-14/collected-raw.md#INFO-044)。

H-ANT-001は7R連続で閾値に到達せず、49%(low帯)に低下した [H-ANT-001](../config/hypotheses.json)。Agent SDKクレジット再開はCだが、Pentagon SCR+DPAのIが上回った。H-ANT-002は63%に上昇した。Colossus 1契約、API 16倍レート制限、Agent SDKクレジットの3つのCが寄与したが、40R連続の定量ユーザー数不在が確度上限を圧下し続けている [H-ANT-002](../config/hypotheses.json)。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Pentagon SCR指定(米企業初)+全連邦機関使用停止命令+DPA脅迫 | 政府関係が「除外」から「構造的抑圧」に悪化。H-GOV-001 6x C蓄積の主因 | B-2 | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) |
| 高 | Claude Mythos Preview: SWE-bench Multimodal 59%。XBOW+UK AISI独立評価で自律的サイバーセキュリティの飛躍確認 | 政府抑圧下でも技術的先進性を維持する直接証拠。Pentagon内部で既に運用との矛盾も | B-3 | [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026) [INFO-034](../Information/2026-05-14/collected-raw.md#INFO-034) |
| 高 | Google秘密AI契約(Pentagon)+従業員抗議 vs Anthropic拒否 | 安全性堅持と受諾の対比が産業界全体の分断を明確化 | B-3 | [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) |
| 高 | Scale AI契約$5億増額+Meta 49%出資。Pentagon CTO「AnthropicはDODベンダーでない」 | 代替インフラの構築とAnthropic排除の組み合わせ。政府調達の再編 | B-2/B-3 | [INFO-038](../Information/2026-05-14/collected-raw.md#INFO-038) [INFO-034](../Information/2026-05-14/collected-raw.md#INFO-034) |
| 高 | Opus 4.7 SWE-bench Pro 64.3%(GPT-5.4/Gemini 3.1 Pro上回る)+API価格 Haiku $1/$5, Sonnet $3/$15, Opus $5/$25 | 民間市場での競争力維持の数値証拠。Colossus 1契約でレート制限16倍 | B-3 | [INFO-055](../Information/2026-05-14/collected-raw.md#INFO-055) [INFO-044](../Information/2026-05-14/collected-raw.md#INFO-044) |
| 中 | Agent SDK v0.2.131 Claude Code パリティ+6月15日クレジット開始+Sandbox Runtime OSS | 開発者エコシステムの基盤強化。H-ANT-002の3x Cの一角 | B-3 | [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010) [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027) |
| 中 | 年次化収益$300億、Fortune 10中8社、$100万超顧客500社超 | 安全性が民間市場で報われている直接の収益証拠 | C-2 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) |
| 中 | Mythos/Glasswing脆弱性確認。XBOW+UK AISI独立評価 | セキュリティ評価の透明性。IND-013 high水準の維持要因 | D-3 | [INFO-071](../Information/2026-05-14/collected-raw.md#INFO-071) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DPAが実際に発動され、Anthropicが強制的に政府契約に組み込まれる | H-GOV-001「政府圧力による萎縮効果」が確定。「安全性の代償」が法的強制に悪化。H-ANT-001の根拠も崩れる | 90日 | [IND-030](../config/indicators.json) |
| Pentagon SCR指定が司法で無効化され、Anthropicが連邦調達に復帰 | 「構造的抑圧」の前提が崩れ、H-GOV-001を大幅に下方修正 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示され、Codex比で1/5以下だった場合 | H-ANT-002「標準ツール化」63%の根拠が崩れ、確度を大幅に下げる | 30日 | [IND-027](../config/indicators.json) |
| Claude Mythos脆弱性が深刻化し、Pentagon内部運用が停止される | 「政府抑圧下でも技術的先進性」の根拠が揺らぐ。SCR指定の正当性が高まる | 90日 | [IND-013](../config/indicators.json) |
| Anthropicがlawful use条項を受諾して政府契約に回帰 | コア判断(民間優先・政府放棄)とH-ANT-001が同時に崩れる | 90日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 49% | 民間で機能($300億ARR・Fortune 10の8社)が確証。7R連続閾値未到達+Pentagon SCR+DPAのI蓄積で49%low帯に低下。Agent SDKクレジット再開はCだが政府抑圧の重みが上回った | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010) [INFO-055](../Information/2026-05-14/collected-raw.md#INFO-055) | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 63% | Colossus 1契約+API 16倍レート制限+Agent SDKクレジットの3x Cで63%に上昇。40R連続定量ユーザー数不在のIが確度上限を圧下 | [INFO-044](../Information/2026-05-14/collected-raw.md#INFO-044) [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010) [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027) | Codex npm 12倍差+Cursor 47%採用+40R連続WAU非公開 |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | SpaceXAI Colossus+$30B資金調達協議でインフラ集中が深化。棄却候補継続 | [INFO-044](../Information/2026-05-14/collected-raw.md#INFO-044) | Colossus 1全容量契約で二重集中加速 |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 47% | Pentagon SCR+DPA脅迫+Google秘密契約+Scale AI $500M+従業員抗議=6x C蓄積で47%に上昇。Anthropic訴訟+Sanders法案はI | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) [INFO-038](../Information/2026-05-14/collected-raw.md#INFO-038) | [INFO-034](../Information/2026-05-14/collected-raw.md#INFO-034) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | $300億ARR・Fortune 10中8社 | 2026-05-14 |
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt以上/期で high | Mythos Preview SWE-bench Multimodal 59% [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026)。Opus 4.7 SWE-bench Pro 64.3% [INFO-055](../Information/2026-05-14/collected-raw.md#INFO-055) | 2026-05-14 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Codex 4層防御=防御強化。Mythos/Glasswing脆弱性確認 [INFO-071](../Information/2026-05-14/collected-raw.md#INFO-071)。新規脆弱性なし。high水準 | 2026-05-14 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 定量改善の停滞で elevated | 定量的改善継続。「真の理解」検証は未解決。elevated水準 | 2026-05-14 |
| [IND-026](../config/indicators.json) | エージェント本番運用準備度 | 成功率80%で high | 77.3%成功率 vs 74%ロールバックギャップ。elevated水準 | 2026-05-14 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP de facto+AAIF 97M SDK+Agent Skills 1000+。Agent SDK v0.2.131パリティ達成 [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010)。high水準 | 2026-05-14 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入vs物理制約で high | Q1 $255.5B+Big 4 $725B+Anthropic $30B+Stargate $500B。Colossus 1契約でレート制限16倍 [INFO-044](../Information/2026-05-14/collected-raw.md#INFO-044)。high水準 | 2026-05-14 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で high | Pentagon SCR+DPA+Google秘密契約+Scale AI $500M+EU AI Act+US Safety Institute。highに上昇 | 2026-05-14 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-14 | Pentagon SCR指定+DPA脅迫・Claude Mythos Preview・Sandbox Runtime OSS・Agent SDKクレジット再開を反映して全面書き直し | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) [INFO-034](../Information/2026-05-14/collected-raw.md#INFO-034) [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026) [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027) [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010) | 「DeployCo競合圧力で50%境界」→「Pentagon SCR+DPAで政府関係が構造的対立に深化。Mythos Preview新モデル。H-ANT-001 49%low帯」 |
| 2026-05-13 | 新AIサービス会社(Blackstone/H&F/Goldman Sachs)・Opus 4.7金融ベンチマーク・Sonnet 4.6を反映して§0〜§2書き直し | [INFO-008](../Information/2026-05-13/collected-raw.md#INFO-008) [INFO-009](../Information/2026-05-13/collected-raw.md#INFO-009) [INFO-007](../Information/2026-05-13/collected-raw.md#INFO-007) | 「DeployCo競合圧力で50%境界」→「DeployCoと新AIサービス会社で二極化競争。中堅企業向け展開参入」 |
| 2026-05-12 | Claude Design + Opus 4.7・Sonnet 4.6 OSWorld改善・DeployCo競合圧力・38R連続未回答を反映して全面書き直し | [INFO-004](../Information/2026-05-12/collected-raw.md#INFO-004) [INFO-007](../Information/2026-05-12/collected-raw.md#INFO-007) [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) | 「民間で報われ政府で係争。因果チェーン未確認」 → 「民間で報われ政府で係争。DeployCo競合圧力で50%境界に到達。Claude Design設計→実装ハンドオフ追加」 |
| 2026-05-11 | Pentagon因果チェーン「確定」→「可能性高いが未確認」。Sonnet 4.6・Colossus 1・$3,800億評価額を反映 | [INFO-001](../Information/2026-05-11/collected-raw.md#INFO-001) [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) | 「民間で報われ政府で制度確定」→「民間で報われ政府で係争。因果チェーン未確認」 |
| 2026-05-08 | $15B JV + Claude Sonnet 4.6 + JetBrains 46% を反映 | 複数INFO | 「政府排除確定の企業」→「民間で報われ政府で係争中。JVで金融次元追加」 |

### 6.1 政府対立の時系列 (Anthropic 固有)

| 日付 | 事象 | 参照 |
|:-:|---|---|
| 2025-07 | Pentagon と $200M 契約締結 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2025-09 | GenAI.mil 展開交渉で決裂。DOD「全合法目的での無制限アクセス」要求、Anthropic「自律兵器・国内大量監視への不使用保証」で拒否 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-02-27 | Trump 政権が SCR 指定・連邦使用禁止 | [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048) |
| 2026-03-05 | DOD が Anthropic を「サプライチェーンリスク」指定 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-04-08 | 連邦控訴裁が一時差し止め請求を棄却。SCR 指定が一時確定 | [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035) |
| 2026-04-17 | Amodei と White House が「生産的・建設的」会談 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-04-23 | Trump 大統領が「Anthropic-DoD 契約は可能」と発言 | [INFO-029](../Information/2026-04-24/collected-raw.md#INFO-029) |
| 2026-04-24 | 連邦裁判所が SCR 指定の仮差し止めを認可 | [INFO-043](../Information/2026-04-28/collected-raw.md#INFO-043) |
| 2026-05-04 | Pentagon 7社契約締結、Anthropic 除外。DC回路裁判所「chilling effect」支持。除外理由は報道によるが公式確認なし | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) |
| 2026-05-04 | AnthropicがBlackstone/H&F/Goldman Sachsと新AIサービス会社設立を発表 | [INFO-008](../Information/2026-05-13/collected-raw.md#INFO-008) |
| 2026-05-06 | SpaceX Colossus 1 のAnthropic向け全容量提供契約を発表 | [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-11/collected-raw.md#INFO-004) |
| 2026-05-08 | PentagonがAnthropicをSCR(supply chain risk)に指定。米企業として初。全連邦機関に使用停止命令 | [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) |
| 2026-05-10 | PentagonがDPA(Defense Production Act)発動を脅迫。HegsethがAnthropicに警告 | [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) |
| 2026-05-12 | Pentagon CTO「AnthropicはDODベンダーでない」と表明。ただしClaude Mythosは既にPentagon内部で運用中 | [INFO-034](../Information/2026-05-14/collected-raw.md#INFO-034) |

## 7. ブラインドスポット

- Claude Code WAU/MAUが40R連続で非公開。$25億ランレートは金額的裏付けだが、Codexの12倍ダウンロード差 [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) やCursor 47%採用 [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) と比較した相対的市場シェアが外部から測れない。
- DPA発動の実際の可能性が評価できない。Hegsethの脅迫が実行されるか、交渉カードとして使われているかの判別が不可能。法的要件(大統領令)と政治的計算の境界が不明。
- Google秘密AI契約の詳細(金額・適用範囲・制約条件)が非公開。Anthropic拒否との対比は明確だが、Google受諾の条件が「安全性をどこまで妥協したか」の評価をできない。
- Pentagon内部でClaude Mythosが運用されているという矛盾 [INFO-034](../Information/2026-05-14/collected-raw.md#INFO-034) の解釈が定まらない。公式除外と実態利用の乖離が何を意味するか(非公式ルート、テスト段階、部門間対立)が不明。
- 中国市場での競合動向(DeepSeek V4等)がClaude API価格(Haiku $1/$5, Sonnet $3/$15, Opus $5/$25)に与える圧力を観測する指標を持っていない [INFO-044](../Information/2026-05-14/collected-raw.md#INFO-044)。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-033](../Information/2026-05-14/collected-raw.md#INFO-033) | Pentagon SCR指定(米企業初)・全連邦機関使用停止命令 |
| [INFO-034](../Information/2026-05-14/collected-raw.md#INFO-034) | Pentagon CTO「AnthropicはDODベンダーでない」・Mythos内部運用の矛盾 |
| [INFO-046](../Information/2026-05-14/collected-raw.md#INFO-046) | Pentagon DPA脅迫・Hegseth警告 |
| [INFO-036](../Information/2026-05-14/collected-raw.md#INFO-036) | Google秘密AI契約(Pentagon)・従業員抗議 |
| [INFO-038](../Information/2026-05-14/collected-raw.md#INFO-038) | Scale AI契約$5億増額・Meta 49%出資 |
| [INFO-026](../Information/2026-05-14/collected-raw.md#INFO-026) | Claude Mythos Preview SWE-bench Multimodal 59%・XBOW+UK AISI評価 |
| [INFO-055](../Information/2026-05-14/collected-raw.md#INFO-055) | Opus 4.7 SWE-bench Pro 64.3%(GPT-5.4/Gemini 3.1 Pro上回る) |
| [INFO-010](../Information/2026-05-14/collected-raw.md#INFO-010) | Agent SDK v0.2.131パリティ・6月15日クレジット開始・サードパーティ再開 |
| [INFO-027](../Information/2026-05-14/collected-raw.md#INFO-027) | Sandbox Runtime OSS・安全なエージェント実行環境 |
| [INFO-044](../Information/2026-05-14/collected-raw.md#INFO-044) | API価格体系・Colossus 1契約(レート制限16倍) |
| [INFO-071](../Information/2026-05-14/collected-raw.md#INFO-071) | Mythos/Glasswing脆弱性・XBOW+UK AISI評価 |
| [INFO-008](../Information/2026-05-13/collected-raw.md#INFO-008) | 新AIサービス会社(Blackstone/H&F/Goldman Sachs・中堅企業向け・Applied AI常駐) |
| [INFO-009](../Information/2026-05-13/collected-raw.md#INFO-009) | 金融向けエージェント(Opus 4.7 Vals AI 64.37%・10テンプレート・Citadel/FIS採用) |
| [INFO-007](../Information/2026-05-13/collected-raw.md#INFO-007) | Sonnet 4.6(OSWorld大幅改善・1M context・SWE-bench 80.2%) |
| [INFO-004](../Information/2026-05-12/collected-raw.md#INFO-004) | Claude Design(Opus 4.7・Canva統合・Claude Codeハンドオフ) |
| [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) | DeployCo($40億+・Tomoro買収・19パートナー) - 競合圧力として |
| [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) | Anthropic統計: $300億ARR・Fortune 10中8社・$3,800億評価額 |
| [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) | Pentagon 7社契約・Anthropic除外 |
| [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) | Cursor 47%採用・Claude Code $10億ランレート到達 |
