# OpenAI — 企業インテリジェンス

> 最終判断更新: 2026-09-20 (前回 2026-09-17)
> 全体確信度: 中低 (主力製品のライフサイクル公告 (新旗艦価格・旧型API終了日程) が公式一次で出揃い・縦型展開と資本協議の報道一次も加わった。ただし収益と資本の監査財務は依然不在)
> 情報非対称性: 価格・終了日程は公式Rate Card由来 (A-2) だが、$1.2T評価額協議は「現在交渉中ではない」公式コメント付きのB-1で条項は不在。収益申告6系列分裂は未解決で公式財務は上場・債券・銀団いずれの契機でも未開示。銀団価格は暫定帰属「非公開通例」のまま取消条件4種が終端2026-10-31まで事前登録済み。Agents APIは公開ベータで採用定量ゼロ。9/20収集 (123件) のOpenAI増分はv4.96評価で全ゲート不発火・確度は全件±0% (最終内容評価基盤: 2026-09-20収集)。
> 主参照: [config/hypotheses.json](../config/hypotheses.json) · [config/indicators.json](../config/indicators.json) · [state/arbiter-2026-09-20.md](../state/arbiter-2026-09-20.md) · [Information/2026-09-20/collected-raw.md](../Information/2026-09-20/collected-raw.md)

## 0. 一文要約

我々はOpenAIを「新旗艦GPT-6 Astraの定価$10/$50と旧型API終了の公告日程で主力製品のライフサイクルを明示し、評価額$1.2T超のPre-IPOラウンド協議が報じられた企業」と読む。料金体系はAstra $10/$50 (cached $1.00)・Sol割引$4/$20 (11/21まで・定価$5/$30)・o1は10/23、GPT-5/o3は12/11にAPI終了で、7月のSol以降フラッグシップ2モデル連続の実質値上げにより長年の値下げトレンドが反転した ([INFO-071](../Information/2026-09-20/collected-raw.md#INFO-071) A-2)。資本面では3月の$122B (評価額$852B) に続き評価額$1.2T超 (最大$1.5T報道) の新ラウンドを協議中と報じられた ([INFO-082](../Information/2026-09-20/collected-raw.md#INFO-082) B-1)。製品面ではAstra for Law ([INFO-004](../Information/2026-09-20/collected-raw.md#INFO-004) A-3) と広告製品 ([INFO-003](../Information/2026-09-20/collected-raw.md#INFO-003) A-3) が同週に公開された。仮説確度は全件±0% (v4.96)。

## 1. コア判断

価格とライフサイクルの公告が主力製品の構造事実を確定させた。GPT-6 Astra (9/3発売・新フラッグシップ) は入力$10・出力$50 per 1Mトークンで、コンピュータ利用・コーディング・サイバー向けと位置付けられる ([INFO-071](../Information/2026-09-20/collected-raw.md#INFO-071) A-2)。GPT-5.6 Solはプロモ価格$4/$20 (11/21まで) で定価$5/$30に戻り、Terra $2/$12・Luna $0.20/$1.20の階層が続く。旧型のAPI終了はo1が10/23、GPT-5とo3が12/11で、Fast mode (Astra 2.5倍) とデータレジデンシー (1.1倍) の追加課金がEnterprise向けrate cardとして公式化された。7月のSol以降、2モデル連続でフラッグシップ実質値上げが重なり、長年の値下げトレンドの反転が公式料金で読める。旧型終了による移行圧力はスイッチングコストの強制であり、[H-OAI-002](../config/hypotheses.json)の実行環境層統制 (レガシー終了と新実行環境への集約) のC側材料である。この上層の値上げはGemini紹介価格の2027年1月倍額化と並び、価格2層構造の上層強化として[SCN-004](../config/scenarios.json)審査材料の文脈に置かれる。

資本の次の観測機が具体化した。OpenAIは投資家と早期協議で評価額$1.2T超 (Forbes報道では最大$1.5T) の新ラウンドを検討し、3月の$122B調達 (評価額$852B) から数ヶ月で+40%超のペースで上振れする形である ([INFO-082](../Information/2026-09-20/collected-raw.md#INFO-082) B-1)。同社は現時点で交渉中ではないと説明し、条項の一次は不在である。それでも監査財務のない評価額系列の伸びはIND-029の資本コスト文脈とS-1ゲート (終端2026-10-31) の観測機を更新する。

縦型展開と製品公開が続いた。Astra for Lawは法務業界向けの縦型製品で、9/10の金融サービスに続く展開である ([INFO-004](../Information/2026-09-20/collected-raw.md#INFO-004) A-3)。広告分野向けAI製品もProduct枠で公開された ([INFO-003](../Information/2026-09-20/collected-raw.md#INFO-003) A-3・詳細本文未取得)。Agents APIは公開ベータとして提供され、managed sandboxes・subagents・プラットフォーム手数料なしを明示した ([INFO-007](../Information/2026-09-20/collected-raw.md#INFO-007) A-2・9/15発表の再観測)。Arbiter v4.96はAgents APIの配給条件 (資格審査の有無) を「安全の配給化」一般化の真の判別観測として次回収集最優先に登録した。資格審査なしを返せばLSVP一般化読みは否定される。

政府系列で行動級の材料が一段深まった。Altmanは従業員に「Pentagonが軍事作戦でAIをどう使うかを会社は制御できない」と説明し、OpenAIは分類政府ネットワークでの利用を許可する協定更新が報じられた ([INFO-061](../Information/2026-09-20/collected-raw.md#INFO-061) B-2)。DoD CTO Emil MichaelのAmodeiへの公然反論も同系列である。Pentagon移管先報道 ([INFO-060](../Information/2026-09-20/collected-raw.md#INFO-060)) は9/15 INFO-052の同一事象再報道として本日Cから除外された (v4.96裁定2-2)。GSA提携 (連邦・州・地方・部族政府向けライセンス$0・使用量50%割引) は政府市場での囲い込み構造を示す ([INFO-015](../Information/2026-09-20/collected-raw.md#INFO-015) B-3)。Arbiter v4.96はINFO-061/015を[H-GOV-002](../config/hypotheses.json)のC+2 (行動級) として計上した。安全系列ではモデル不整合 (misalignment) 報告フレームワークがResearch枠で公開された ([INFO-002](../Information/2026-09-20/collected-raw.md#INFO-002) A-3)。発話級規制支持と文書級枠組みの距離は、運用評価で埋まるかが次の観察点である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|---|---|---|:-:|---|
| 高 | GPT-6 Astra $10/$50 (cached $1.00)・Sol割引$4/$20 (定価$5/$30)・フラッグシップ2連続実質値上げ | 主力製品の価格構造の公式一次。値下げトレンド反転。[SCN-004](../config/scenarios.json)価格権力材料 ([IND-027](../config/indicators.json)) | A-2 | [INFO-071](../Information/2026-09-20/collected-raw.md#INFO-071) |
| 高 | o1は10/23・GPT-5/o3は12/11にAPI終了・Fast mode 2.5×/データレジデンシー1.1×の追加課金体系 | 旧型終了=移行コストの強制。[H-OAI-002](../config/hypotheses.json)実行環境層統制のC側。Enterprise rate card公式化 | A-2 | [INFO-071](../Information/2026-09-20/collected-raw.md#INFO-071) |
| 高 | 評価額$1.2T超 (最大$1.5T報道) のPre-IPOラウンド協議・3月$122B@$852Bから+40%超ペース | 資本系列の次の観測機。条項一次は不在で「交渉中ではない」公式コメント付き | B-1 | [INFO-082](../Information/2026-09-20/collected-raw.md#INFO-082) |
| 高 | Altman「Pentagonの使用方法は制御できない」従業員説明・分類ネットワーク横断利用の協定更新 | [H-GOV-002](../config/hypotheses.json) C+2計上 (v4.96・行動級)。DoD CTOのAmodei公然反論と同系列 | B-2 | [INFO-061](../Information/2026-09-20/collected-raw.md#INFO-061) |
| 中 | Astra for Law (9/17)・広告製品 (9/16) の公式公開 | 業界縦型展開 (金融9/10→法務) と広告本格参入。収益多角化の方向 | A-3 | [INFO-004](../Information/2026-09-20/collected-raw.md#INFO-004) [INFO-003](../Information/2026-09-20/collected-raw.md#INFO-003) |
| 中 | Agents API公開ベータ (managed sandboxes・subagents・プラットフォーム手数料なし) | 9/15発表の再観測。配給条件 (資格審査の有無) は次回最優先の判別観測 (v4.96) | A-2 | [INFO-007](../Information/2026-09-20/collected-raw.md#INFO-007) |
| 中 | モデル不整合報告フレームワーク公開 (Research枠) | 安全透明性の文書級。発話級規制支持との加重差の検証は運用評価待ち | A-3 | [INFO-002](../Information/2026-09-20/collected-raw.md#INFO-002) |
| 中 | GSA提携: 政府向けライセンス$0・使用量50%割引・サイバーセキュリティ支援 | 政府市場での囲い込み。[H-GOV-002](../config/hypotheses.json) C+2計上 (v4.96) | B-3 | [INFO-015](../Information/2026-09-20/collected-raw.md#INFO-015) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Agents API配給条件の確認 (資格審査なしを返せばLSVP一般化読み否定) | 「安全の配給化」の一般化とAnthropic固有の判別が確定する | 次回収集 (v4.96最優先) | [SCN-001](../config/scenarios.json) [H-OAI-002](../config/hypotheses.json) |
| $1.2Tラウンドの条項一次 (規模・投資家・構造) | 評価額系列のB-1報道から公式一次への置換。[IND-029](../config/indicators.json)資本コスト文脈の更新 | 継続 | [IND-029](../config/indicators.json) |
| o1終了 (10/23) とGPT-5/o3終了 (12/11) の実行・移行実測 (エラーレート・移行コスト報告) | 移行強制の実害が判定され[H-OAI-002](../config/hypotheses.json)実行環境層統制の定量が始まる | 2026-12-11 | [H-OAI-002](../config/hypotheses.json) |
| OpenAIの公式財務 (監査付き) | 収益申告6系列分裂が解消し[H-OAI-001](../config/hypotheses.json)のS-1ゲート再評価が発火する | 継続 | [H-OAI-001](../config/hypotheses.json) [IND-026](../config/indicators.json) |
| Agents APIの採用定量 (セッション数・エンタープライズ利用・料金収益) | 「公式発表」から「実装定量」への移行でB2B命題が判別可能になる | 90日 | [H-OAI-001](../config/hypotheses.json) [IND-026](../config/indicators.json) |
| Astra能力主張の交叉確認ガード (A) 充足 (他ベンチ家族・独立系の同一タスク計測) | ARC-AGI-3 99.9%の一次級確定または下方修正 | 継続 | [IND-025](../config/indicators.json) |
| ペンタゴン契約の最終条項一次確認 (国防総省文書・OpenAI開示) | 「拒らないAI」要求の有無が確定し需要側構造の解釈が固定される | 90日 | [H-GOV-002](../config/hypotheses.json) [IND-030](../config/indicators.json) |
| 銀団帰属の取消条件 (価格報道+組成完了告知・貸付グループ構成変化・専業誌条項言及・S-1債務コミットメント開示) | 暫定帰属「非公開通例」が取消されIND-029の価格条件系列が再開する | 2026-10-31 | [IND-029](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 43% low | v4.96 ±0% (最終内容評価基盤2026-09-20収集・全ゲート不発火)。Agents API公開ベータ ([INFO-007](../Information/2026-09-20/collected-raw.md#INFO-007)) とAstra for Law・金融縦型 ([INFO-004](../Information/2026-09-20/collected-raw.md#INFO-004)) はC側累積だが監査財務待ちのゲート凍結 (v4.77制度) 維持。S-1ゲート終端2026-10-31。収益一次不在・交叉確認ガード (A) 不充足 | 監査付き収益のセグメント内訳・Agents API採用定量・独立系ベンチ追証 | 収益停滞の監査一次・B2Bシェアの独立定量での劣位 |
| [H-OAI-002](../config/hypotheses.json) | MCP開放上にプロプライエタリ上位レイヤーで囲い込む | 44% low | v4.96 ±0%。旧型API終了公告 (o1 10/23・GPT-5/o3 12/11・[INFO-071](../Information/2026-09-20/collected-raw.md#INFO-071)) はレガシー終了による移行強制で実行環境層統制のC。API層はBYOキー開放継続で層区別原則不変。Agents API配給条件は次回の判別観測 | 上位レイヤーでの独自機能依存の定量・レガシー移行の強制実測 | ポータビリティ標準の採用拡大・self_hosted級の実利用定量 |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンス達成を最優先とする | 3% low | v4.96 ±0%。不整合報告フレームワーク ([INFO-002](../Information/2026-09-20/collected-raw.md#INFO-002)) は文書級の安全透明性で「検閲」系列ではない。広告・法務縦型の商業化主導が継続 | 検閲・過剰整列事象の具体的顕在化 | 商業化主導の継続 (広告・縦型製品の拡大) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | エージェント供給チェーン攻撃 | 実害インシデントのA-2公表 | critical/rising (v4.96・状態変更なし)。HF事件=約700エージェント協調攻撃・RubyGems未報告前兆 ([INFO-123](../Information/2026-09-20/collected-raw.md#INFO-123) B-1) で検知された/されなかった系列の分岐監視を強化 | 2026-09-20 |
| [IND-025](../config/indicators.json) | フロンティア性能の交叉確認 | 独立系・他ベンチ家族での再現 | elevated/stable (v4.96・状態変更なし)。Astra ARC-AGI-3 0.999の交叉確認ガード (A) は不充足継続 | 2026-09-20 |
| [IND-026](../config/indicators.json) | エージェント本番到達と期待-実態ギャップ | 本番到達率の反転 | high/rising (v4.96・状態変更なし)。Deloitte一次特定 (80%効用認識 vs 37% EBIT影響) で測定単位の方向は整合も「方向的整合」格下げ (v4.96) | 2026-09-20 |
| [IND-027](../config/indicators.json) | 標準化と価格体系 | 価格2層分化の「高」復帰条件 | high/rising (v4.96・状態変更なし)。上層はAstra $10/$50・フラッグシップ2連続値上げ・旧型終了公告 ([INFO-071](../Information/2026-09-20/collected-raw.md#INFO-071))、床側はSeed2.0約1桁安 ([INFO-117](../Information/2026-09-20/collected-raw.md#INFO-117)) で二層の分化が同週に重なった | 2026-09-20 |
| [IND-028](../config/indicators.json) | AGI叙事と到達度指標 | 予測分裂の収束・外部検証 | high/rising (v4.96・状態変更なし) | 2026-09-20 |
| [IND-029](../config/indicators.json) | 資本コストと銀団価格 | 取消条件4種・AI個別発行体スプレッド | high/rising (v4.96)。$1.2T評価額協議 ([INFO-082](../Information/2026-09-20/collected-raw.md#INFO-082)) を資本系列の観測機に追加。新監視ライン「AI個別発行体スプレッド」 (Oracle CDS>150bps初アンカー) 登録 | 2026-09-20 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 (監視可能性) | critical解消3基準 | critical/rising (v4.96・N=1実質37R・rising40R自動発火事前登録)。LSVP脅威モデルのBS-001交差計上・HF事件700エージェントの追加 | 2026-09-20 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ |
|:---:|---|---|
| 2026-09-20 | 全面書き直し。GPT-6 Astra価格と旧型API終了日程 (INFO-071・A-2) を主力製品のライフサイクル構造事実として計上。$1.2T評価額協議 (INFO-082)・Astra for Law/広告製品 (INFO-004/003)・不整合報告フレームワーク (INFO-002)・Agents API公開ベータ (INFO-007)・ペンタゴン系列 (INFO-061/015・C+2計上) を新規計上。§4/§5をv4.96値に更新 | [INFO-071](../Information/2026-09-20/collected-raw.md#INFO-071)/[082](../Information/2026-09-20/collected-raw.md#INFO-082) + Arbiter v4.96 |
| 2026-09-17 | v2形式へ全面書き直し。9/15バッチ (Agents API・減速要請・Pachocki警告・ペンタゴンFOIA・広告$1B) を初回計上。§4/§5をv4.93値に更新 | 鮮度タイムアウト (8日) + 9/15バッチ未吸収 |
| 2026-09-09 | IND-029第1観測機閉鎖反映: 暫定帰属「非公開通例」条件付き批准・取消条件4種拡張事前登録 | [Arbiter v4.90](../state/arbiter-2026-09-09.md) |
| 2026-09-08 | Astra公式全文 (INFO-089) と公式changelog計上で§0〜§2全面更新。「監視可能性低下」自己開示のIND-030計上 | [Arbiter v4.89](../state/arbiter-2026-09-08.md) |

## 7. ブラインドスポット

1. Astra価格・旧型終了日程は公式Rate Card集成由来 (A-2) で、元帳票の6系列分裂の教訓からも料金表の頁単位での再取得が価値を持つ。Fast mode 2.5×の実測コスト検証はない。
2. $1.2T評価額協議は「現在交渉中ではない」公式コメント付きのB-1で、評価額の伸びを資本調達の確定と読むのは先走る。
3. Agents API・Astra for Law・広告製品はいずれも公開文書のみで採用・利用・収益の定量がなく、発表と実装の乖離を割り引いて読む必要がある。
4. ペンタゴン系列の行動級材料 (分類ネットワーク拡大・GSA提携) は報道ベースで、最終条項の一次確認がないまま需要側構造の解釈が進むリスクがある。
5. 収益申告6系列分裂が解消されていない。広告$1B報道も二次分析単独のままである。
6. 不整合報告フレームワークは文書の公開で、報告件数・対応の運用データは未来の時点である。発話級と文書級の加重差の実運用はまだ一度も審査で使われていない。

## 付録: 直近30日の参照Evidence

| Evidence | 信用 | 事項 |
|---|:-:|---|
| [INFO-071](../Information/2026-09-20/collected-raw.md#INFO-071) | A-2 | GPT-6 Astra $10/$50・Sol割引$4/$20 (定価$5/$30)・o1 10/23・GPT-5/o3 12/11 API終了・フラッグシップ2連続値上げ |
| [INFO-082](../Information/2026-09-20/collected-raw.md#INFO-082) | B-1 | 評価額$1.2T超 (最大$1.5T) Pre-IPOラウンド協議・3月$122B@$852B |
| [INFO-004](../Information/2026-09-20/collected-raw.md#INFO-004) | A-3 | Astra for Law発表 (法務縦型・金融9/10に続き) |
| [INFO-003](../Information/2026-09-20/collected-raw.md#INFO-003) | A-3 | Reimagining advertising with AI 公開 (詳細本文未取得) |
| [INFO-002](../Information/2026-09-20/collected-raw.md#INFO-002) | A-3 | モデル不整合報告フレームワーク (Research枠・9/16) |
| [INFO-007](../Information/2026-09-20/collected-raw.md#INFO-007) | A-2 | Agents API公開ベータ (managed sandboxes・プラットフォーム手数料なし・9/15の再観測) |
| [INFO-061](../Information/2026-09-20/collected-raw.md#INFO-061) | B-2 | Altman「Pentagonの使用方法は制御できない」・分類ネットワーク拡大・DoD CTO反論 |
| [INFO-015](../Information/2026-09-20/collected-raw.md#INFO-015) | B-3 | GSA提携: 政府$0ライセンス・50%使用割引 |
| [INFO-123](../Information/2026-09-20/collected-raw.md#INFO-123) | B-1 | HF事件=約700エージェント協調攻撃・RubyGems前兆 (IND-013/BS-001文脈) |
| [INFO-004](../Information/2026-09-15/collected-raw.md#INFO-004) | A-2 | Agents API発表 (9/15・前回計上の基盤) |
| [INFO-051](../Information/2026-09-15/collected-raw.md#INFO-051) | B-2 | ペンタゴンFOIA: 「拒らないAI」ミッションモデル要求 (前回計上の継続) |
| [INFO-084](../Information/2026-09-15/collected-raw.md#INFO-084) | C-2 | Pachocki警告: CoT監視依存の持続不可能 (前回計上の継続) |
| [Arbiter v4.96](../state/arbiter-2026-09-20.md) | 裁定 | 全仮説±0%・H-GOV-002 C+2 (INFO-061/015)・Agents API配給条件を次回最優先 |
| [Arbiter v4.93](../state/arbiter-2026-09-17.md) | 裁定 | 全仮説±0%・鮮度注記制度登録 (前回更新の基盤) |
