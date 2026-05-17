# Anthropic

> 最終判断更新: 2026-05-17
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが40R連続非公開。中国市場との競合観測は手薄
> 主参照: hypotheses.json#H-ANT-001/002/003, hypotheses.json#H-GOV-001, indicators.json#IND-008/013/023/027/030

## 0. 一文要約

我々はAnthropicを、**安全性の維持にコストを払いながら、それが商業的優位性に直結するか未証明の企業**と読んでいる。Enterprise JV(Blackstone/H&F/Goldman Sachs)は商業的動機の表れであり、安全性への市場評価の証明ではない [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001)。SDK分離課金(6月15日施行)はClaude Code最頻ユーザーにコスト増を課す事実であり [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038)、H-ANT-002「開発者標準ツール化」と論理的に矛盾する。Pentagon SCR指定+DPA脅迫による構造的抑圧は継続 [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027)。Claude Code WAUが定量開示される、または安全性が商業的優位性に転化された直接証拠が出る、またはSDK分離課金が撤回される、のいずれかで判断の前提が変わる。

## 1. コア判断

Anthropicの構図は「安全性のコスト」と「安全性の優位性」の区別にある。安全性を維持する代償(Pentagon除外、SCR指定、DPA脅迫)は観測可能だが [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-17/collected-raw.md#INFO-029)、その安全性が顧客獲得に直接寄与した証拠は乏しい。Enterprise JVは金融界との商業提携であり [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001)、Sonnet 4.6のSWE-bench 80.2%は技術的性能の証明であり [INFO-002](../Information/2026-05-17/collected-raw.md#INFO-002)、Claude for SMBは市場拡大策である [INFO-003](../Information/2026-05-17/collected-raw.md#INFO-003)。いずれも「安全性が商業的成功の要因」という因果を立証しない。

SDK分離課金はH-ANT-002に直接矛盾する事実だ。6月15日からClaude有料サブスクのプログラマティック使用(SDK/CLI)を通常使用から分離し、API価格で課金する [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038)。Claude Code最頻ユーザー(スタートアップ33%)が最も影響を受ける [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059)。Kimi K2.6がSWE-bench Pro 58.6%でOpus 4.6 53.4%を上回り [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065)、性能面での競合圧力も増している。

H-ANT-001は49%(-1%)。安全性コストと安全性優位の区別導入で、Enterprise JVを安全性Cから除外。49%上限条件: 安全性が商業的優位性に転化された直接証拠が必要。H-ANT-002は63%(-1%)。SDK分離課金が既発の事実としてH-ANT-002と矛盾。H-GOV-001は50%(+1%)。Pentagon除外、DeepMind労組、チリング効果、1200+AI法案、中国AI国家戦略の5重C蓄積 [H-GOV-001](../config/hypotheses.json)。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | SDK分離課金: 6月15日からSDK/CLI使用をAPI価格で課金・Pro $20/Max 5x $100/Max 20x $200 Agent SDK Credit | Claude Code高頻度ユーザーにコスト増。H-ANT-002「開発者標準ツール化」と直接矛盾。既発の事実(A-3) | A-3 | [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) |
| 高 | Enterprise JV: Blackstone/H&F/Goldman Sachs合弁・中堅企業向け・Applied AI常駐 | 商業的動機の表れ。安全性Cとしては不当(「安全性コスト≠安全性優位」)。H-ANT-001の確度上限を圧下 | A-3 | [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001) |
| 高 | Kimi K2.6 SWE-bench Pro 58.6% > Claude Opus 4.6 53.4%・300並列サブエージェント | 中国ベンダーが性能指標でAnthropicを上回る。H-ANT-002の性能前提を侵食 | B-3 | [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) |
| 高 | Claude Code: スタートアップ33% vs エンタープライズ13%・Anthropic SMB市場参入 | 開発者採用に偏り。エンタープライズ13%はH-ANT-002「標準ツール化」の制約。SDK分離課金がスタートアップ層に直撃 | B-2 | [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059) |
| 高 | Pentagon SCR指定+7社契約Anthropic除外+DPA脅迫+チリング効果 | 政府関係の構造的抑圧が継続。「安全性コスト」の直接証拠。H-GOV-001のC | A-3/B-2 | [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-17/collected-raw.md#INFO-029) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DPAが実際に発動され、Anthropicが強制的に政府契約に組み込まれる | H-GOV-001「政府圧力による萎縮効果」が確定。H-ANT-001の根拠も崩れる | 90日 | [IND-030](../config/indicators.json) |
| Pentagon SCR指定が司法で無効化され、Anthropicが連邦調達に復帰 | 「構造的抑圧」の前提が崩れ、H-GOV-001を大幅に下方修正 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示され、Codex比で1/5以下だった場合 | H-ANT-002「標準ツール化」63%の根拠が崩れ、確度を大幅に下げる | 30日 | [IND-027](../config/indicators.json) |
| SDK分離課金が6月15日以降に撤回または緩和される | H-ANT-002のコスト増Iが消滅。確度上方修正の根拠 | 60日 | [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) |
| 安全性を明示的選定理由とするFortune 500契約が3件以上確認される | H-ANT-001の「安全性優位」が初めて直接証明される。49%上限条件の解除 | 180日 | [IND-008](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 49% | 「安全性コスト≠安全性優位」区別導入。INFO-001(Enterprise JV)は商業動機で安全性C除外。INFO-027/029は「安全性コスト」のCで「安全性優位」のCではない。49%上限条件: 安全性が商業的優位性に転化された直接証拠が必要 | [INFO-002](../Information/2026-05-17/collected-raw.md#INFO-002) [INFO-003](../Information/2026-05-17/collected-raw.md#INFO-003) | [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001) [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) [INFO-029](../Information/2026-05-17/collected-raw.md#INFO-029) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 63% | SDK分離課金(INFO-038 A-3)は既発の事実で高頻度ユーザーにコスト増。Kimi K2.6 SWE-bench Pro 58.6% > Opus 4.6 53.4%(INFO-065 B-3)。スタートアップ33% vs エンタープライズ13%(INFO-059 B-2)。40R連続WAU非公開のI累積 | [INFO-002](../Information/2026-05-17/collected-raw.md#INFO-002) [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059) | [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | SpaceXAI Colossus+$300億資金調達協議でインフラ集中が深化。棄却候補継続 | [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001) | Colossus全容量契約で二重集中加速 |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 50% | Pentagon除外(INFO-027)+DeepMind労組(INFO-028)+チリング効果(INFO-029)+1200+AI法案(INFO-025)+中国AI国家戦略(INFO-026)の5重C蓄積。50%上限条件付き(次回A-2以下証拠のみで+1%なし) | [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) [INFO-029](../Information/2026-05-17/collected-raw.md#INFO-029) [INFO-025](../Information/2026-05-17/collected-raw.md#INFO-025) [INFO-026](../Information/2026-05-17/collected-raw.md#INFO-026) | Anthropic提訴+Sanders法案 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | $300億ARR・Fortune 10中8社。安全性C除外後は直接関連减弱 | 2026-05-17 |
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt以上/期で high | Sonnet 4.6 SWE-bench Verified 80.2% [INFO-002](../Information/2026-05-17/collected-raw.md#INFO-002)。Kimi K2.6 SWE-bench Pro 58.6% > Opus 4.6 53.4% [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) | 2026-05-17 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | npmマルウェア14倍+Bitwarden供給チェーン攻撃 [INFO-012](../Information/2026-05-17/collected-raw.md#INFO-012)。high水準 | 2026-05-17 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 定量改善の停滞で elevated | Gemini 3 Pro 100%+Grok 4.1 97.8% [INFO-018](../Information/2026-05-17/collected-raw.md#INFO-018)。Claude Mythos Preview SWE-bench Multimodal 59%首位。elevated水準 | 2026-05-17 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | TikTok MCP server+Boomi-Guru MCP Registry+SDK統合ミドルウェア崩壊 [INFO-056](../Information/2026-05-17/collected-raw.md#INFO-056) [INFO-014](../Information/2026-05-17/collected-raw.md#INFO-014)。high水準 | 2026-05-17 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入vs物理制約で high | $800B-$1T収益ギャップ [INFO-048](../Information/2026-05-17/collected-raw.md#INFO-048)+Enterprise JV+Anthropic $300億協議。high水準 | 2026-05-17 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で high | 1200+AI法案 [INFO-025](../Information/2026-05-17/collected-raw.md#INFO-025)+中国AI国家戦略 [INFO-026](../Information/2026-05-17/collected-raw.md#INFO-026)+Pentagon 7社契約 [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027)。規制三極分岐深化。elevated水準 | 2026-05-17 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-17 | 「安全性コスト≠安全性優位」区別導入・SDK分離課金反映で全面書き直し | [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001) [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059) [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) | 「Enterprise JV+Claude for SMB+Sonnet 4.6でH-ANT-001 50%medium境界復帰」→「安全性C除外+SDK分離課金IでH-ANT-001 49%。H-ANT-002 63%(-1%)。H-GOV-001 50%(+1%)」 |
| 2026-05-15 | Enterprise JV・Claude for SMB・Sonnet 4.6 Claude Code 70% preferredを反映して全面書き直し | [INFO-006](../Information/2026-05-15/collected-raw.md#INFO-006) [INFO-007](../Information/2026-05-15/collected-raw.md#INFO-007) [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) | 「Pentagon SCR+DPAで政府関係が構造的対立に深化。H-ANT-001 49%low帯」→「Enterprise JV+Claude for SMB+Sonnet 4.6 70% preferredでH-ANT-001 50%medium境界復帰。民間側強化」 |
| 2026-05-14 | Pentagon SCR指定+DPA脅迫・Claude Mythos Preview・Sandbox Runtime OSSを反映 | 2026-05-14複数INFO | 「DeployCo競合圧力で50%境界」→「Pentagon SCR+DPAで政府関係が構造的対立に深化」 |
| 2026-05-12 | Claude Design + Opus 4.7・Sonnet 4.6 OSWorld改善・DeployCo競合圧力を反映 | 2026-05-12複数INFO | 「民間で報われ政府で係争」 → 「DeployCo競合圧力で50%境界到達」 |
| 2026-05-08 | $15B JV + Claude Sonnet 4.6 + JetBrains 46% を反映 | 複数INFO | 「政府排除確定」→「民間で報われ政府で係争中。JVで金融次元追加」 |

### 6.1 政府対立の時系列 (Anthropic 固有)

| 日付 | 事象 | 参照 |
|:-:|---|---|
| 2025-07 | Pentagon と $200M 契約締結 | (前回情報) |
| 2025-09 | GenAI.mil 展開交渉で決裂 | (前回情報) |
| 2026-02-27 | Trump 政権が SCR 指定・連邦使用禁止 | (前回情報) |
| 2026-03-05 | DOD が Anthropic を「サプライチェーンリスク」指定 | (前回情報) |
| 2026-04-08 | 連邦控訴裁が一時差し止め請求を棄却。SCR 指定が一時確定 | (前回情報) |
| 2026-04-24 | 連邦裁判所が SCR 指定の仮差し止めを認可 | (前回情報) |
| 2026-05-04 | Pentagon 7社契約締結、Anthropic 除外。$200M契約拒否 | [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) |
| 2026-05-04 | AnthropicがBlackstone/H&F/Goldman Sachsと新AIサービス会社設立 | [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001) |
| 2026-05-12 | Anthropic-Pentagon対立のチリング効果が市民機関に波及と報道 | [INFO-029](../Information/2026-05-17/collected-raw.md#INFO-029) |
| 2026-05-13 | Claude for SMB発表(15ワークフロー・10都市ツアー) | [INFO-003](../Information/2026-05-17/collected-raw.md#INFO-003) |
| 2026-05-13 | SDK分離課金発表(6月15日施行・SDK/CLI使用をAPI価格で課金) | [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) |
| 2026-05-14 | Sonnet 4.6リリース(SWE-bench 80.2%・Claude Code 70% preferred) | [INFO-002](../Information/2026-05-17/collected-raw.md#INFO-002) |

## 7. ブラインドスポット

- Claude Code WAU/MAUが40R連続で非公開。Codex 12倍ダウンロード差やCursor 47%採用と比較した相対的市場シェアが外部から測れない。SDK分離課金後のユーザー離脱率も観測不能。
- 「安全性が商業的優位性に直結する」直接証拠が存在しない。Fortune 10中8社採用は安全性が理由なのか、性能・価格・ロックイン他要因なのか判別不能。
- DPA発動の実際の可能性が評価できない。脅迫が実行されるか交渉カードとして使われているかの判別が不可能。
- SDK分離課金のユーザー行動への影響が未観測。6月15日施行後のClaude Code使用量変化を追跡する指標を持っていない。
- 中国市場での競合動向(Kimi K2.6等)がClaude API価格と開発者採用に与える圧力を定量化する指標を持っていない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-05-17/collected-raw.md#INFO-001) | Enterprise JV(Blackstone/H&F/Goldman Sachs・中堅企業向け)・安全性Cとしては除外 |
| [INFO-002](../Information/2026-05-17/collected-raw.md#INFO-002) | Sonnet 4.6(SWE-bench 80.2%・1M context・Claude Code 70% preferred) |
| [INFO-003](../Information/2026-05-17/collected-raw.md#INFO-003) | Claude for SMB(15WF・QuickBooks/PayPal/HubSpot/Canva/Docusign) |
| [INFO-038](../Information/2026-05-17/collected-raw.md#INFO-038) | SDK分離課金(6月15日施行・SDK/CLI使用をAPI価格で課金) [Arbiter v3.80] |
| [INFO-059](../Information/2026-05-17/collected-raw.md#INFO-059) | Claude Codeユーザー分布(スタートアップ33% vs エンタープライズ13%) |
| [INFO-065](../Information/2026-05-17/collected-raw.md#INFO-065) | Kimi K2.6 SWE-bench Pro 58.6% > Claude Opus 4.6 53.4% |
| [INFO-027](../Information/2026-05-17/collected-raw.md#INFO-027) | Pentagon SCR指定・7社契約Anthropic除外・$200M契約拒否 |
| [INFO-029](../Information/2026-05-17/collected-raw.md#INFO-029) | Anthropic-Pentagon対立のチリング効果 |
| [INFO-025](../Information/2026-05-17/collected-raw.md#INFO-025) | 米国1200+AI法案・連邦州規制矛盾 |
| [INFO-026](../Information/2026-05-17/collected-raw.md#INFO-026) | 中国AIエージェント国家戦略 |
| [INFO-028](../Information/2026-05-17/collected-raw.md#INFO-028) | Google DeepMind労組設立(軍事AI契約への懸念) |
