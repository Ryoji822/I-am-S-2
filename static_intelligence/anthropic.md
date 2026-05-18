# Anthropic

> 最終判断更新: 2026-05-18
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが41R連続非公開。中国市場との競合観測は手薄
> 主参照: hypotheses.json#H-ANT-001/002/003, hypotheses.json#H-GOV-001, indicators.json#IND-008/013/023/027/030

## 0. 一文要約

我々はAnthropicを、**Pentagonとの構造的対立が制度化されながら、民間市場で初めてOpenAIを抜いた企業**と読んでいる。Ramp AI IndexでAnthropic 34.4%がOpenAI 32.3%を初逆転し [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)、Q1収益$30B run rate(80倍成長)に到達した [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。Pentagon側ではSCR指定→$200M契約取消→大統領連邦排除命令→xAI $200M代替契約→Anthropic訴訟提起の因果チェーンがA-2証拠3件(Reuters [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036), Fortune [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037), L&W [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028))で確認された [H-GOV-001](../config/hypotheses.json) 51%。SDK分離課金(6月15日施行)は継続中 [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038)。$50B追加調達交渉中で評価額$900B接近 [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。もし安全性が商業的選択理由第1位である直接証拠が出る、またはSDK分離課金が撤回される、またはDPAが実際に発動される、のいずれかで判断の前提が変わる。

## 1. コア判断

Anthropicの構図は二つの相反する動きの同時進行にある。民間市場での躍進と、政府との構造的対立の制度化だ。

民間市場の数据は強い。Ramp AI IndexでAnthropic 34.4%がOpenAI 32.3%を初めて逆転した [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。Q1 2026収益は$30B run rateに到達し、昨年の10倍成長予測に対して80倍で応えている。Claude CodeはGitHub公開コミットの4%を生成し前月比2倍、Walleye Capitalでは400人中100%の採用率を記録した [INFO-001](../Information/2026-05-18/collected-raw.md#INFO-001)。金融サービス向け10のエージェントテンプレート、Microsoft 365統合、Opus 4.7のVals AI Finance Agent benchmark 64.37%首位は、エンタープライズ深度の具体的証拠だ [INFO-001](../Information/2026-05-18/collected-raw.md#INFO-001)。$50B追加調達交渉(評価額$900B接近)は市場からの信認を示す [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。

Pentagonとの対立は「単発事案」から「制度化された構造的衝突」に移行した。SCR指定→$200M契約取消→大統領Truth Social連邦排除命令→xAI $200M代替契約→Anthropic訴訟提起の完全な因果チェーンが確認された [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038)。「安全性に妥協しない企業への経済的報復」と「妥協する企業への報酬」の構造が明示された。CDTは州・地方政府レベルへのチリング効果を警告している [INFO-039](../Information/2026-05-18/collected-raw.md#INFO-039)。H-GOV-001は51%(+1%)に上昇したが、51%上限条件として他社(Google/Meta/OpenAI)の安全性方針後退の直接証拠を要求する [H-GOV-001](../config/hypotheses.json)。

「安全性コスト≠安全性優位」の区別は継続する。Ramp逆転と$30B収益は商業的成功の証明だが、INFO-054(B-3)は初の「安全性優位」直接証拠の端緒であり [INFO-054](../Information/2026-05-18/collected-raw.md#INFO-054)、A-2+ソースでの定量確認がH-ANT-001 +1%の条件となる [H-ANT-001](../config/hypotheses.json)。SDK分離課金は6月15日施行でH-ANT-002と矛盾し続ける [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038)。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Ramp AI Index: Anthropic 34.4% vs OpenAI 32.3%。初の逆転。年間4倍成長 vs OpenAI 0.3% | 民間市場での躍進の定量証拠。H-ANT-001/H-ANT-002のC | A-2 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) |
| 高 | Q1 2026収益$30B run rate(80倍成長、予測10倍の8倍) | 商業的規模の跳躍。$50B追加調達の根拠 | A-2 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) |
| 高 | Pentagon因果チェーン制度化: SCR→$200M取消→連邦排除命令→xAI $200M→訴訟 | 「安全性妥協への報復と報酬」の構造確認。H-GOV-001 51%の直接根拠 | A-2 | [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |
| 高 | SDK分離課金: 6月15日施行。SDK/CLI使用をAPI価格で課金。Pro $20/Max 5x $100/Max 20x $200 Agent SDK Credit | H-ANT-002「開発者標準ツール化」と直接矛盾。既発の事実 | A-3 | [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |
| 高 | $50B追加調達交渉中。評価額$900B接近。$1.8B Akamai 7年クラウド契約 | 資本市場の信認とインフラ拡大 | A-2 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DPAが実際に発動され、Anthropicが強制的に政府契約に組み込まれる | H-GOV-001「政府圧力による萎縮効果」が確定。H-ANT-001の根拠も崩れる | 90日 | [IND-030](../config/indicators.json) |
| 他社(Google/Meta/OpenAI)が安全性方針を後退させる直接証拠が出る | H-GOV-001 51%上限条件が充足され、萎縮効果が業界全体に波及したと判断 | 90日 | [IND-030](../config/indicators.json) |
| A-2+ソースで安全性が商業的選択理由第1位の定量確認ができる | H-ANT-001 49%上限条件が解除され、安全性優位の直接証明となる | 180日 | [IND-008](../config/indicators.json) |
| SDK分離課金が6月15日以降に撤回または緩和される | H-ANT-002のコスト増Iが消滅。確度上方修正の根拠 | 60日 | [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |
| Claude Code WAU/MAUが定量開示され、Codex比で1/5以下だった場合 | H-ANT-002「標準ツール化」63%の根拠が崩れる | 30日 | [IND-027](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 49% | Ramp逆転(INFO-070 A-2)と$30B収益は商業的Cだが「安全性が選択理由」の因果はB-3(INFO-054)のみ。49%上限条件: A-2+での定量確認が必要 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) [INFO-054](../Information/2026-05-18/collected-raw.md#INFO-054) [INFO-001](../Information/2026-05-18/collected-raw.md#INFO-001) | [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 63% | GitHub 4%コミット(INFO-070)+Walleye 100%(INFO-001)は強力C。Grok Build Beta競合(INFO-006)+MCP脆弱性(INFO-022)が新出I。SDK分離課金未解決。安定観察 | [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) [INFO-001](../Information/2026-05-18/collected-raw.md#INFO-001) | [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006) [INFO-022](../Information/2026-05-18/collected-raw.md#INFO-022) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | SpaceXAI Colossus+$300億協議でインフラ集中深化。棄却候補継続 | [INFO-001](../Information/2026-05-18/collected-raw.md#INFO-001) | Colossus全容量契約で二重集中加速 |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 51% | A-2証拠3件(Reuters INFO-036, Fortune INFO-037, L&W INFO-028)で因果チェーン確認。萎縮効果7C蓄積。51%上限条件: 他社安全性後退の直接証拠が必要 | [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) [INFO-039](../Information/2026-05-18/collected-raw.md#INFO-039) [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028) | [INFO-054](../Information/2026-05-18/collected-raw.md#INFO-054) [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | Ramp AI Index 34.4%(初逆転) [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)。$30B ARR | 2026-05-18 |
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt以上/期で high | Opus 4.7 Vals AI Finance 64.37%首位 [INFO-001](../Information/2026-05-18/collected-raw.md#INFO-001)。Claude Mythos SWE-bench Pro 64.3% [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) | 2026-05-18 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | MCP token theft脆弱性 [INFO-022](../Information/2026-05-18/collected-raw.md#INFO-022)+AIコード48%セキュリティ脆弱性 [INFO-056](../Information/2026-05-18/collected-raw.md#INFO-056)。high水準 | 2026-05-18 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | Grok Build ACP対応 [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006)+MCP 2026ロードマップ [INFO-015](../Information/2026-05-18/collected-raw.md#INFO-015)+OSS Codex統合 [INFO-021](../Information/2026-05-18/collected-raw.md#INFO-021)。high水準 | 2026-05-18 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入vs物理制約で high | Q1 $255.5B [INFO-042](../Information/2026-05-18/collected-raw.md#INFO-042)+$50B追加調達 [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070)+$1.8B Akamai [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038)。high水準 | 2026-05-18 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で high | Pentagon saga A-2×4件 [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) [INFO-039](../Information/2026-05-18/collected-raw.md#INFO-039)+EU AI Act [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028)+Bengio LawZero [INFO-065](../Information/2026-05-18/collected-raw.md#INFO-065)。elevated水準 | 2026-05-18 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-18 | Pentagon因果チェーン制度化(A-2×3)+Ramp AI Index初逆転+$30B収益+$50B追加調達を反映して全面書き直し | [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) | 「安全性C除外+SDK分離課金IでH-ANT-001 49%。H-GOV-001 50%」→「Ramp初逆転+$30B収益で民間躍進。Pentagon因果チェーン制度化でH-GOV-001 51%。$50B追加調達」 |
| 2026-05-17 | 「安全性コスト≠安全性優位」区別導入・SDK分離課金反映で全面書き直し | [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001) [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) | 「Enterprise JV+Claude for SMB+Sonnet 4.6」→「安全性C除外+SDK分離課金I。H-GOV-001 50%(+1%)」 |
| 2026-05-15 | Enterprise JV・Claude for SMB・Sonnet 4.6 Claude Code 70% preferredを反映 | 複数INFO | 「Pentagon SCR+DPAで政府関係が構造的対立に深化」→「Enterprise JV+Claude for SMB+Sonnet 4.6 70% preferredでH-ANT-001 50%medium境界復帰」 |

## 7. ブラインドスポット

- Claude Code WAU/MAUが41R連続で非公開。GitHub 4%コミットは代理指標だが、Codex 12倍差やCursor 47%と比較した相対的市場シェアが外部から測れない。SDK分離課金後のユーザー離脱率も観測不能。
- 「安全性が商業的優位性に直結する」直接証拠がINFO-054(B-3)の端緒にとどまる。Ramp逆転が安全性由来なのか性能・価格・ロックイン他要因なのか判別不能。A-2+での定量分解が必須。
- DPA発動の実際の可能性が評価できない。脅迫が実行されるか交渉カードとして使われているかの判別が不可能。
- 他社(Google/Meta/OpenAI)の安全性方針の変化を観測する指標を持っていない。H-GOV-001 51%上限条件充足に他社の動向が必要だが、KIQ-GOV-CHILLで追跡中。
- $50B追加調達と$900B評価額の妥当性が外部から検証できない。$30B収益run rateの内訳(消費者vsエンタープライズvs API)も非公開。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-070](../Information/2026-05-18/collected-raw.md#INFO-070) | Ramp AI Index逆転(34.4% vs 32.3%)・$30B収益・$50B追加調達・Claude Code GitHub 4% |
| [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) | Pentagon SCR指定・Mythos展開・$200M契約拒否・xAI $200M (Reuters A-2) |
| [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) | FTC/Pentagon規制分析・$200M取消・連邦排除命令 (Fortune A-2) |
| [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) | Anthropic公式声明・$1.8B Akamai・SDK分離課金・Claude 80倍成長 |
| [INFO-039](../Information/2026-05-18/collected-raw.md#INFO-039) | CDT: 州・地方政府へのチリング効果波及 |
| [INFO-054](../Information/2026-05-18/collected-raw.md#INFO-054) | Anthropic価格決定力・安全性評価・Ramp逆転詳細 (B-3) |
| [INFO-069](../Information/2026-05-18/collected-raw.md#INFO-069) | Pentagon CTO Mythos「国家安保の瞬間」・Project Glasswing |
| [INFO-001](../Information/2026-05-18/collected-raw.md#INFO-001) | 金融サービス10エージェントテンプレート・Opus 4.7 Vals AI首位・Walleye 100% |
| [INFO-028](../Information/2026-05-18/collected-raw.md#INFO-028) | EU AI Act規則変更・期限延長 (L&W A-2) |
| [INFO-065](../Information/2026-05-18/collected-raw.md#INFO-065) | Recursive $650M調達・Bengio LawZero $30M |
| [INFO-022](../Information/2026-05-18/collected-raw.md#INFO-022) | Claude Code MCP Token Theft脆弱性 |
| [INFO-006](../Information/2026-05-18/collected-raw.md#INFO-006) | Grok Build Beta(ACP対応・Claude Code競合) |
| [Arbiter v3.81](../state/arbiter-2026-05-18.md) | H-ANT-001/002/003・H-GOV-001確度評価の完全根拠 |

### 政府対立の時系列 (Anthropic 固有)

| 日付 | 事象 | 参照 |
|:-:|---|---|
| 2025-07 | Pentagon と $200M 契約締結 | (前回情報) |
| 2025-09 | GenAI.mil 展開交渉で決裂 | (前回情報) |
| 2026-02-27 | Trump 政権が SCR 指定・連邦使用禁止 | (前回情報) |
| 2026-03-05 | DOD が Anthropic を「サプライチェーンリスク」指定 | (前回情報) |
| 2026-04-08 | 連邦控訴裁が一時差し止め請求を棄却。SCR 指定が一時確定 | (前回情報) |
| 2026-04-24 | 連邦裁判所が SCR 指定の仮差し止めを認可 | (前回情報) |
| 2026-05-04 | Pentagon 7社契約締結、Anthropic 除外。$200M契約拒否 | [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) |
| 2026-05-12 | Pentagon CTO「Mythos展開は国家安保の瞬間」。Anthropic利点は一時的と予測 | [INFO-069](../Information/2026-05-18/collected-raw.md#INFO-069) |
| 2026-05-12 | 大統領Truth Social連邦システムAnthropic排除命令 | [INFO-037](../Information/2026-05-18/collected-raw.md#INFO-037) |
| 2026-05-12 | xAI $200M Pentagon代替契約獲得 | [INFO-036](../Information/2026-05-18/collected-raw.md#INFO-036) |
| 2026-05-18 | Anthropic公式声明公開。$1.8B Akamai契約。Claude 80倍成長 | [INFO-038](../Information/2026-05-18/collected-raw.md#INFO-038) |
