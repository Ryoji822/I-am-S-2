# xAI → SpaceXAI

> 最終判断更新: 2026-05-09
> 全体確信度: 低
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Colossus貸与条件も非公開
> 主参照: hypotheses.json#H-XAI-001/002/003/004, indicators.json#IND-017/006/001/025/029/030

## 0. 一文要約

我々はxAIを、**独立企業として解散しSpaceXの内部AI部門(SpaceXAI)に再編された元フロンティアプレイヤー**と読んでいる。最大の根拠は、2026年2月にxAIが$250BでSpaceXと合併した事実 [INFO-072](../Information/2026-05-09/collected-raw.md#INFO-072) と、Colossus 1(220K GPU)の全容量を競合のAnthropicに貸与した事実 [INFO-076](../Information/2026-05-09/collected-raw.md#INFO-076) だ。Grok 4.3の83%価格カット [INFO-020](../Information/2026-05-09/collected-raw.md#INFO-020) は価格競争力を示すが、独立企業としての価格戦略とSpaceX内部リソースの価格設定では意味が違う。SpaceXAIとしての戦略(Grokの宇宙・製造業展開、Colossus貸与の意図、Cursor $60B取得オプションの用途)が具体的に観測されたら、判断を再構築する。

## 1. コア判断

xAIの章は終わった。我々の確信度は「低」にとどめる。

2026年2月、xAIは$250B評価額でSpaceXと合併し、SpaceXAIとして再編された [INFO-072](../Information/2026-05-09/collected-raw.md#INFO-072)。この事実は、我々が蓄積してきた4つのxAI仮説の前提(独立企業としての戦略的行動)を根底から変える。合併前の観測は参照価値があるが、その意味付けをやり直す必要がある。

合併前のxAIは、価格競争力と政府採用で存在感を示していた。Grok 4.3は出力価格を83%カット($1.25/$2.50 per M tokens)し、1Mトークンコンテキストとネイティブ動画入力を全API開発者に公開した [INFO-020](../Information/2026-05-09/collected-raw.md#INFO-020)。$200MのPentagon契約で連邦政府機関にGrokを提供していた [INFO-062](../Information/2026-05-09/collected-raw.md#INFO-062)。GenAI.milでは120万ユーザー・10万エージェント規模での採用実績があった [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022)。

合併後の観測は、独立企業の戦略とは異なる文脈で読む必要がある。最も特徴的なのはColossus 1(220K GPU、300MW超)の全容量をAnthropicに貸与した事実 [INFO-076](../Information/2026-05-09/collected-raw.md#INFO-076) だ。元々Grok訓練用に構築された第1世代クラスタを直接競合に貸す。空き容量の有効活用、Anthropicとの関係構築、企業金融的動機のいずれかが考えられるが、外部から区別できない。第2世代Colossus 555K GPU [INFO-073](../Information/2026-05-09/collected-raw.md#INFO-073) はSpaceXAI自身がGrok訓練に使っていると推測される。

SpaceXがCursor(Anysphere)の$60B取得オプションを確保した [INFO-051](../Information/2026-05-09/collected-raw.md#INFO-051) ことも、AIへの投資意欲を示すが、これがSpaceXAIの戦略なのかSpaceX本体の投資なのかが判別不能だ。Gro​k 4.3の価格戦略も、「市場シェア獲得のための攻撃的価格設定」なのか「SpaceXインフラの余剰コストを埋めるための価格設定」なのかが分からない。

当初の差別化軸だったXデータ活用(H-XAI-001)は34R以上証拠不在で37%に低下し、棄却候補。物理世界統合(H-XAI-003)も35%で保留・再定義中。統合直後で時間不足のargument from ignoranceを避けるため、棄却ではなく保留としている。Arbiterは次回、SpaceXAIとしての新仮説フレーム(H-XAI-005)の定義を最優先課題としている [H-XAI-003](../config/hypotheses.json)。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | xAI解散、SpaceXに統合(SpaceXAI)。2月に$250Bで合併 | 仮説群の前提(独立企業)が崩壊。全仮説の再定義が必要 | B-1 | [INFO-072](../Information/2026-05-09/collected-raw.md#INFO-072) |
| 高 | Colossus 1(220K GPU、300MW)の全容量をAnthropicに貸与 | SpaceXAIが「AIインフラ提供者」としての側面を持つ。競合に計算資源を貸す構造は独立企業の仮説枠組みでは説明困難 | B-1 | [INFO-076](../Information/2026-05-09/collected-raw.md#INFO-076) |
| 高 | Grok 4.3: 出力価格83%カット($1.25/$2.50)、1M context、全API開発者公開 | 価格競争力は genuine C。ただし統合後の価格意図(市場シェア獲得か余剰活用か)が不明 | B-3 | [INFO-020](../Information/2026-05-09/collected-raw.md#INFO-020) |
| 中 | $200M Pentagon契約でGrokを連邦政府機関に提供 | 独立企業時代の政府市場実績。統合後も有効かは未確認 | B-3 | [INFO-062](../Information/2026-05-09/collected-raw.md#INFO-062) |
| 中 | Colossus第2世代: 555K GPU、2GW目標。$20B Series E、$230B評価額 | SpaceXAIの計算規模。第2世代はGrok訓練に使用中と推測 | C-3 | [INFO-073](../Information/2026-05-09/collected-raw.md#INFO-073) |
| 中 | Grok 4.3はマルチモーダル・推論改善もOpenAI/Anthropic/Googleに遅れ | 価格優位はあるが性能首位ではない。ベンチマーク戦争を避ける戦略 | B-3 | [INFO-074](../Information/2026-05-09/collected-raw.md#INFO-074) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| SpaceXAIが宇宙・製造業特化AI機能を具体的に発表する | H-XAI-003が「保留」から「支持」に転じる | 90日 | [IND-006](../config/indicators.json) |
| Grokの価格が$1.00/$2.00以下に引き下げられ、SpaceXがインフラコストを補填していることが確認される | H-XAI-002が「価格競争」から「内部補填」に再定義される | 60日 | [IND-001](../config/indicators.json) |
| Colossus貸与がAnthropic以外にも拡大し、SpaceXAIが「AIインフラプロバイダー」として定着する | H-XAI-005(新仮説フレーム)の定義が確定する | 90日 | [IND-029](../config/indicators.json) |
| H-XAI-001が次の30日でもXデータ活用の新規証拠なし | Xデータ活用差別化が観測可能な軸として機能していないことが確定し、low再分類を実施する | 30日 | [IND-017](../config/indicators.json) |
| GrokのAPI提供が終了または大幅に縮小される | SpaceXAIが外部市場から撤退し内部利用に特化する場合、H-XAI-002とH-XAI-004が同時に崩れる | 90日 | [IND-006](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-XAI-002](../config/hypotheses.json) | 価格競争力でシェアを獲得する | 65% | Grok 4.3 $1.25/$2.50はgenuine C。ただし統合後の価格意図(市場シェア獲得かSpaceX余剰活用か)が不明で、独立企業の価格戦略とは意味が異なる | [INFO-020](../Information/2026-05-09/collected-raw.md#INFO-020) | [INFO-072](../Information/2026-05-09/collected-raw.md#INFO-072) 統合で戦略前提変更 |
| [H-XAI-004](../config/hypotheses.json) | 汎用AI基盤としてエンタープライズ・政府市場を獲得する | 55% | $200M Pentagon契約とGrok 4.3全API公開はC。ただし統合で独立企業終了、市場シェア定量データ不在で上限キャップ | [INFO-062](../Information/2026-05-09/collected-raw.md#INFO-062) [INFO-020](../Information/2026-05-09/collected-raw.md#INFO-020) | [INFO-072](../Information/2026-05-09/collected-raw.md#INFO-072) 統合 |
| [H-XAI-001](../config/hypotheses.json) | Xデータ活用でリアルタイム特化を差別化する | 37% | 34R以上連続でXデータ活用の新規証拠不在。時間減衰で棄却候補。xAI→SpaceXAI統合で観測の意義自体が低下 | (なし) | 34R以上の証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | SpaceX統合で宇宙・製造業特化AIを展開する | 35% | 35%到達だが統合直後のargument from ignoranceを避けるため棄却ではなく保留・再定義。宇宙・製造業特化の展開には数ヶ月〜年単位の時間が必要 | (なし) | 34R以上証拠不在。Colossus Anthropic貸与は特化不在の追加I [INFO-076](../Information/2026-05-09/collected-raw.md#INFO-076) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-017](../config/indicators.json) | Xデータ独占活用の有無 | 新規証拠で elevated | 34R以上新規証拠不在 | 2026-05-09 |
| [IND-006](../config/indicators.json) | Grokエージェントスタック採用状況 | 政府・企業の大規模採用で high | $200M Pentagon契約 [INFO-062](../Information/2026-05-09/collected-raw.md#INFO-062) | 2026-05-09 |
| [IND-001](../config/indicators.json) | Grokのベンチマーク性能 | +5pt/期で high | BenchLM Grok 4.1: 90(4位)。Grok 4.3は改善も首位不在 [INFO-074](../Information/2026-05-09/collected-raw.md#INFO-074) | 2026-05-09 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入 vs 物理制約で high | Colossus 555K GPU/$230B評価 [INFO-073](../Information/2026-05-09/collected-raw.md#INFO-073)。Colossus 1 220K GPU Anthropic貸与 [INFO-076](../Information/2026-05-09/collected-raw.md#INFO-076) | 2026-05-09 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 直接介入で high | Pentagon $200M契約 [INFO-062](../Information/2026-05-09/collected-raw.md#INFO-062)。米国安全性テスト対象 [INFO-059](../Information/2026-05-09/collected-raw.md#INFO-059) | 2026-05-09 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-09 | xAI→SpaceXAI統合・Colossus Anthropic貸与・Grok 4.3リリースを反映して全面書き直し | [INFO-072](../Information/2026-05-09/collected-raw.md#INFO-072) [INFO-076](../Information/2026-05-09/collected-raw.md#INFO-076) [INFO-020](../Information/2026-05-09/collected-raw.md#INFO-020) | 「価格優位と政府採用で汎用AI基盤を固める独立企業」 → 「独立企業解散。SpaceXAIとして再編。全仮説の前提変更」 |
| 2026-05-02 | H-XAI-001 42%に低下。H-XAI-003 low再分類。H-XAI-004 最有力確定 | [INFO-006](../Information/2026-05-02/collected-raw.md#INFO-006) Grok 4.3リリース | 「Xデータ差別化が中核」 → 「証拠不在で劣化継続。汎用AI基盤が最有力」 |
| 2026-04-27 | H-XAI-001 45→42%。H-XAI-003 42→40% | [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) Pentagon GenAI.mil統合確認 | 「差別化軸が複数あり評価中」 → 「政府採用でH-XAI-004が急浮上」 |

## 7. ブラインドスポット

- SpaceXAIの内部戦略が外部から観測不能。Grokの価格設定、Colossusの貸与判断、Cursor $60B取得オプションの用途はすべてSpaceX内部の意思決定であり、独立企業のような公開情報や競合分析から推定できない。SpaceXは上場前であり、内部のAI戦略に関する開示義務がない。
- Colossus 1をAnthropicに貸与した理由が不明。「第1世代クラスタの余剰活用」「Anthropicとの関係構築」「純粋な企業金融的動機」のいずれか、または複合だが、外部から区別できない。貸与期間や料金体系も非公開。
- Xデータ活用の観測限界と仮説棄却が混同するリスクが、統合前に比べてさらに深刻化している。SpaceXAIがXデータを内部で活用していても、それが外部から確認される手段がない。
- Grok 4.3のベンチマーク自己報告(xAI発信)の独立性が確認できない。CaseLaw v2首位等の成果は競合他社の独立検証がない。BenchLM 4位(Grok 4.1: 90)は第三者評価だが、4.3の独立評価はまだない。
- SpaceXAIが「AIインフラプロバイダー」としてColossusを他社に貸与する事業を拡大する場合、現在の「AIモデル開発企業」枠組みでは捉えきれない。H-XAI-005の定義が急務だが、枠組み設計にはSpaceXAIの戦略方向性の確認が前提になる。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-072](../Information/2026-05-09/collected-raw.md#INFO-072) | xAI解散、SpaceX統合(SpaceXAI)。$250B合併 |
| [INFO-076](../Information/2026-05-09/collected-raw.md#INFO-076) | Colossus 1(220K GPU)Anthropic貸与 |
| [INFO-020](../Information/2026-05-09/collected-raw.md#INFO-020) | Grok 4.3: 83%価格カット、1M context、全API公開 |
| [INFO-073](../Information/2026-05-09/collected-raw.md#INFO-073) | Grok AI統計: 555K GPU、$230B評価額 |
| [INFO-074](../Information/2026-05-09/collected-raw.md#INFO-074) | Grok 4.3マルチモーダル改善・トップモデルに遅れ |
| [INFO-062](../Information/2026-05-09/collected-raw.md#INFO-062) | $200M Pentagon契約 |
| [INFO-051](../Information/2026-05-09/collected-raw.md#INFO-051) | SpaceX Cursor $60B取得オプション |
| [INFO-037](../Information/2026-05-09/collected-raw.md#INFO-037) | Pentagon 7社契約SpaceX選出 |
| [INFO-085](../Information/2026-05-09/collected-raw.md#INFO-085) | クラウド実行収束(3社同一週移行) |
| [INFO-059](../Information/2026-05-09/collected-raw.md#INFO-059) | 米国安全性テスト対象(Google/Microsoft/xAI) |
| [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) | Pentagon GenAI.mil統合(120万ユーザー・10万エージェント) |
| [Arbiter v3.72](../state/arbiter-2026-05-09.md) | 確度評価の完全根拠(付録のみ参照) |
