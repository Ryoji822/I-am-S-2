# Anthropic

> 最終判断更新: 2026-05-15
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが39R連続非公開。中国市場との競合観測は手薄
> 主参照: hypotheses.json#H-ANT-001/002/003, hypotheses.json#H-GOV-001, indicators.json#IND-008/013/023/027/030

## 0. 一文要約

我々はAnthropicを、**安全性堅持で民間市場を獲得しながら、政府からの構造的抑圧(Supply Chain Risk指定+国防生産法脅迫)に直面しつつ、Enterprise JVとClaude for SMBで市場を拡大する企業**と読んでいる。最大の根拠は、Blackstone/H&F/Goldman Sachsとのenterprise JV設立 [INFO-006](../Information/2026-05-15/collected-raw.md#INFO-006) と、Sonnet 4.6がSWE-bench Verified 80.2%を達成し [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005)、Claude CodeがSonnet 4.5より70%好まれる事実 [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) だ。PentagonがAnthropicを米企業として初めてSCR指定し [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033) DPA発動を脅迫した事実 [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033) と対比される。Claude for SMBが15のエージェントワークフローでQuickBooks/PayPal/HubSpot等と統合し [INFO-007](../Information/2026-05-15/collected-raw.md#INFO-007)、中堅企業市場への本格参入を開始した。Claude Code WAUが定量開示される、またはDPAが実際に発動される、またはEnterprise JVの収益実績が確認される、のいずれかが観測されたら判断の前提が変わる。

## 1. コア判断

Anthropicの構図は「安全性が民間市場では報われ、政府市場では構造的抑圧に直面する」という二極化にある。ただし民間側の強さがEnterprise JVとClaude for SMBで一段と強まった。

民間側は強い。Enterprise JVはBlackstone、Hellman & Friedman、Goldman Sachsとの合弁で、中堅企業向けClaude導入ソリューションを構築する [INFO-006](../Information/2026-05-15/collected-raw.md#INFO-006)。General Atlantic、Apollo、Sequoia等も出資する。Claude for SMBはQuickBooks、PayPal、HubSpot、Canva、Docusign等のツールと統合する15のエージェントワークフローを提供し [INFO-007](../Information/2026-05-15/collected-raw.md#INFO-007)、給与計算、月次決算、キャンペーン実行等を自動化する。SMBツアー(10都市)とPayPal提携のAI教育コースも発表された。Sonnet 4.6はSWE-bench Verified 80.2%を達成し、1M tokenコンテキストウィンドウ(ベータ)を備える [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005)。Claude CodeはSonnet 4.5より70%好まれる [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005)。Sandbox Runtimeがオープンソース化され [INFO-016](../Information/2026-05-15/collected-raw.md#INFO-016)、Claude Codeの安全なエージェント実行環境が提供された。OpenClaw連携も観測されている [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010)。

政府側は引き続き深刻だ。PentagonがAnthropicを米企業として初めてSCRに指定し [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033)、DPA発動を脅迫した。8社とAI契約を締結しAnthropicのみ除外された。GoogleがPentagonと秘密AI契約を締結し [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033)、Anthropic(拒否)とGoogle(受諾)の立場の違いが明確になった。

H-ANT-001は49%から50%に上昇し、low帯からmedium境界に復帰した。Enterprise JV+Sonnet 4.6+Claude for SMBの3重CがPentagon除外Iを相殺した。H-ANT-002は63%から64%に上昇した。Claude Code 70% preferredは高診断的価値の直接証拠だが、39R連続の定量ユーザー数不在が確度上限を圧下し続けている [H-ANT-002](../config/hypotheses.json)。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Enterprise JV: Blackstone/H&F/Goldman Sachs合弁・中堅企業向け・Applied AI常駐 | 民間市場での差別化深化。エンタープライズ展開インフラの構築。H-ANT-001のC | A-3 | [INFO-006](../Information/2026-05-15/collected-raw.md#INFO-006) |
| 高 | Claude for SMB: 15ワークフロー・QuickBooks/PayPal/HubSpot/Canva/Docusign統合・10都市ツアー | 中堅企業市場への本格参入。デプロイメント層での围い込み新次元 | A-3 | [INFO-007](../Information/2026-05-15/collected-raw.md#INFO-007) |
| 高 | Sonnet 4.6: SWE-bench Verified 80.2%・1M context・Claude Code 70% preferred vs Sonnet 4.5 | 技術的優位性の直接的ユーザー選好データ。高診断的価値 | A-3 | [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) |
| 高 | Pentagon SCR指定(米企業初)+DPA脅迫+8社契約Anthropic除外 | 政府関係が「除外」から「構造的抑圧」に悪化。H-GOV-001のC | B-2 | [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033) |
| 高 | Google秘密AI契約(Pentagon) vs Anthropic拒否 | 安全性堅持と受諾の対比が産業界全体の分断を明確化 | B-2 | [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033) |
| 高 | Sandbox Runtime OSS・OpenClaw連携 | 開発者エコシステムの基盤強化。H-ANT-002のC | A-3 | [INFO-016](../Information/2026-05-15/collected-raw.md#INFO-016) [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010) |
| 中 | 年次化収益$300億、Fortune 10中8社、$100万超顧客500社超 | 安全性が民間市場で報われている直接の収益証拠 | C-2 | (前回情報) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| DPAが実際に発動され、Anthropicが強制的に政府契約に組み込まれる | H-GOV-001「政府圧力による萎縮効果」が確定。H-ANT-001の根拠も崩れる | 90日 | [IND-030](../config/indicators.json) |
| Pentagon SCR指定が司法で無効化され、Anthropicが連邦調達に復帰 | 「構造的抑圧」の前提が崩れ、H-GOV-001を大幅に下方修正 | 180日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示され、Codex比で1/5以下だった場合 | H-ANT-002「標準ツール化」64%の根拠が崩れ、確度を大幅に下げる | 30日 | [IND-027](../config/indicators.json) |
| Anthropicがlawful use条項を受諾して政府契約に回帰 | コア判断(民間優先・政府放棄)とH-ANT-001が同時に崩れる | 90日 | [IND-030](../config/indicators.json) |
| Enterprise JVが12ヶ月以内に縮小または解散 | H-ANT-001の50%復帰根拠が崩れる | 365日 | [IND-029](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 50% | Enterprise JV+Sonnet 4.6+Claude for SMBの3重Cでlow帯→medium境界復帰。Pentagon SCR+DPAのIは前回反映済み。民間で機能($300億ARR・Fortune 10の8社)が確証 | [INFO-006](../Information/2026-05-15/collected-raw.md#INFO-006) [INFO-007](../Information/2026-05-15/collected-raw.md#INFO-007) [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) | [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 64% | Claude Code 70% preferred(高診断的C)+OpenClaw連携+Sandbox Runtime OSSのC蓄積。Grok Build競合はIだが単発。39R連続定量ユーザー数不在のI累積 | [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) [INFO-016](../Information/2026-05-15/collected-raw.md#INFO-016) [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010) | Grok Build CLI+39R連続WAU非公開 |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | SpaceXAI Colossus+$300億資金調達協議でインフラ集中が深化。棄却候補継続 | [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) | Colossus 1全容量契約で二重集中加速 |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 48% | Pentagon SCR+DPA+Google秘密契約+WH AI審査EO+US-China AI talksの蓄積。Anthropic提訴+Sanders法案はI | [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033) [INFO-022](../Information/2026-05-15/collected-raw.md#INFO-022) [INFO-040](../Information/2026-05-15/collected-raw.md#INFO-040) | Anthropic提訴+Sanders法案 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | $300億ARR・Fortune 10中8社 | 2026-05-15 |
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt以上/期で high | Sonnet 4.6 SWE-bench Verified 80.2% [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) | 2026-05-15 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Sandbox Runtime OSSで防御強化。新規脆弱性なし。high水準 | 2026-05-15 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 定量改善の停滞で elevated | Sonnet 4.6 1M context+OSWorld大幅改善。量的向上継続。「真の理解」検証未解決。elevated水準 | 2026-05-15 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | Sandbox Runtime OSS+OpenClaw連携+SKILL.md 300+。high水準 | 2026-05-15 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入vs物理制約で high | Enterprise JV+Anthropic $300億調達協議+Colossus 1契約。high水準 | 2026-05-15 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で high | Pentagon SCR+DPA+Google秘密契約+WH AI審査EO+US-China AI talks+EU AI Act。規制二方向深化。elevated水準 | 2026-05-15 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
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
| 2026-05-04 | Pentagon 8社契約締結、Anthropic 除外 | [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033) |
| 2026-05-04 | AnthropicがBlackstone/H&F/Goldman Sachsと新AIサービス会社設立 | [INFO-006](../Information/2026-05-15/collected-raw.md#INFO-006) |
| 2026-05-13 | Claude for SMB発表(15ワークフロー・10都市ツアー) | [INFO-007](../Information/2026-05-15/collected-raw.md#INFO-007) |
| 2026-05-14 | Sonnet 4.6リリース(SWE-bench 80.2%・Claude Code 70% preferred) | [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) |

## 7. ブラインドスポット

- Claude Code WAU/MAUが39R連続で非公開。Codex 12倍ダウンロード差やCursor 47%採用と比較した相対的市場シェアが外部から測れない。
- DPA発動の実際の可能性が評価できない。脅迫が実行されるか交渉カードとして使われているかの判別が不可能。
- Google秘密AI契約の詳細(金額・適用範囲・制約条件)が非公開。Google受諾の条件が「安全性をどこまで妥協したか」の評価をできない。
- Enterprise JVの収益寄与・顧客獲得数・FDE稼働率が未確認。全証拠がA-3(公式発表)でB-tier以上独立確認0件。
- 中国市場での競合動向(DeepSeek V4等)がClaude API価格に与える圧力を観測する指標を持っていない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-005](../Information/2026-05-15/collected-raw.md#INFO-005) | Sonnet 4.6(SWE-bench 80.2%・1M context・Claude Code 70% preferred) |
| [INFO-006](../Information/2026-05-15/collected-raw.md#INFO-006) | Enterprise JV(Blackstone/H&F/Goldman Sachs・中堅企業向け) |
| [INFO-007](../Information/2026-05-15/collected-raw.md#INFO-007) | Claude for SMB(15WF・QuickBooks/PayPal/HubSpot/Canva/Docusign) |
| [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010) | OpenClaw連携・ByteDance収益化 |
| [INFO-016](../Information/2026-05-15/collected-raw.md#INFO-016) | Sandbox Runtime OSS・安全なエージェント実行環境 |
| [INFO-033](../Information/2026-05-15/collected-raw.md#INFO-033) | Pentagon SCR指定(米企業初)・8社契約Anthropic除外 |
