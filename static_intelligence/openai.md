# OpenAI — 企業インテリジェンス

> 最終判断更新: 2026-09-17 (前回 2026-09-09・v2形式へ全面移行)
> 全体確信度: 中低 (主力製品の公式一次がAstraとAgents APIで揃い・安全性の自己警告系列も一次化した。ただし収益と資本の監査財務は依然不在)
> 情報非対称性: 能力・実行環境・安全認識は当事者一次で覆われた。一方でOpenAI固有の定量は欠けたままである。収益申告は6系列分裂が未解決で公式財務は上場・債券・銀団いずれの契機でも未開示。銀団価格は第1観測機 (窓閉鎖9/9) で暫定帰属「非公開通例」となり取消条件4種が終端2026-10-31まで事前登録済み。9/15バッチ (112件・本日のcollected-rawはそのコピー) のOpenAI増分はv4.92評価で全ゲート不発火・確度は全件±0%のまま監視在庫化した。9/16・9/17はDEGRADED-P1×2R連続で新規証拠ゼロ。鮮度注記制度 (v4.93) により全仮説確度は「最終内容評価基盤: 2026-09-15収集 (v4.92評価)」の注記付きで管理される (9/1以来の確度変更なし9R)。
> 主参照: [config/hypotheses.json](../config/hypotheses.json) · [config/indicators.json](../config/indicators.json) · [state/arbiter-2026-09-17.md](../state/arbiter-2026-09-17.md) · [Information/2026-09-15/collected-raw.md](../Information/2026-09-15/collected-raw.md)

## 0. 一文要約

我々はOpenAIを「主力製品の公式発表が揃い、安全性で義務的規制を要請しながら自らのモデルの監視可能性低下を警告した企業」と読む。Agents API発表 ([INFO-004](../Information/2026-09-15/collected-raw.md#INFO-004)・A-2・公式) はCodexハーネスのマネージドクラウド提供であり、skillsをcapability directoriesで配布する実行環境のAPI化である。安全系列ではAltmanがAmodei減速論に原則同意し ([INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093)・B-2)、チーフサイエンティストPachockiがCoT監視依存の持続不可能性とAstra級のステガノグラフィ縁能力を警告した ([INFO-084](../Information/2026-09-15/collected-raw.md#INFO-084)・C-2)。政府系列ではFOIA取得の契約文書でペンタゴンの「軍の要求をできるだけ拒らない」ミッションモデル要求が報じられた ([INFO-051](../Information/2026-09-15/collected-raw.md#INFO-051)・B-2)。仮説確度は全件±0% (v4.93・DEGRADED保守性原則)。

## 1. コア判断

実行環境の提供構造がAPI化で一段深まった。Agents APIは「hosted Codex runtime」を基盤にクラウドエージェントの構築・起動・長時間セッション・ツール利用・オーケストレーションを管理し、multi_agent (同時サブエージェント数制御)・MCPサーバ接続・programmatic tool calling・self_hosted環境を公開した ([INFO-004](../Information/2026-09-15/collected-raw.md#INFO-004))。skills配布をcapability directoriesで行う設計は、SKILL.md配給形式の公共財化 (Microsoft Agent Framework・google/skills+agents-cli・9/1 A-1×2) と対になるOpenAI側の公式実装である。H-OAI-002の層区別原則 (API層開放×実行環境層囲い込み) は維持される。 Responses APIのasync tool callingとmid-turn steering (9/8・A-3)、mTLS/X.509ワークロードIDのGA、Assistants API終了 (8/26完了) とwhisper-1廃止公告 (2027年2月) と合わせ、レガシー終了による移行コストの強制と新実行環境への集約が同時に進む。

安全と規制の立場が発話として整列した。OpenAIは「暴走エージェント」インシデントを理由に義務的な国家AI安全要件を求め、カリフォルニア州のAI安全法案4本を支持した ([INFO-047](../Information/2026-09-15/collected-raw.md#INFO-047)・B-2)。AltmanはAmodeiのペーシング論に「原則同意・組み込み評価者受け入れ・安全が要求する複数の一時停止ポイントの予測」で応じ、2026年のIPOは否定した ([INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093))。OpenAI FoundationはPaul Christianoを理事会に迎えた ([INFO-096](../Information/2026-09-15/collected-raw.md#INFO-096)・B-2)。ただしPachocki警告 ([INFO-084](../Information/2026-09-15/collected-raw.md#INFO-084)) は能力側の実態認識であり、発話級の規制支持と行動・文書級の安全実装の間の距離は残る。v4.92はこの声明群をH-GOV-002のI側累積3件 (発話級・加重1/2以下) として台帳記録し、確度変更はしなかった。

政府調達の構造が一次文書で可視化された。The InterceptのFOIA報道では、国防総省がOpenAIにLLMの拒否率を最小化する納品物を求める条文が契約ドラフトに存在し、2/27に分類ネットワーク全軍利用の協定へ署名、両者は「最終契約に同条項なし」と反論した ([INFO-051](../Information/2026-09-15/collected-raw.md#INFO-051))。Google・xAI・Anthropicも同種の分類ネットワーク契約を持ち、4社の契約文言が「反復精錬」を共通目的とする。Anthropicの倫理拒否による調達喪失 (DOD分類ワークロード90%移行済み・10月全面移行予定・[INFO-052](../Information/2026-09-15/collected-raw.md#INFO-052)・B-2) と合わせ、「安全性制約と軍事ニーズの衝突」がOpenAIに与える需要側の構造はH-OAI-001のB2B命題と接続する。規制環境はトランプEOによる州規制封じ ([INFO-046](../Information/2026-09-15/collected-raw.md#INFO-046)・B-2・両義注記付き) と上院duty of care法案交渉 ([INFO-107](../Information/2026-09-15/collected-raw.md#INFO-107)・A-2・条文不在) が並走し、方向は未確定である。

収益構造の定量は依然欠けたままである。ChatGPT広告の年間収益$10億規模報道 ([INFO-062](../Information/2026-09-15/collected-raw.md#INFO-062)・B-2) は「インプレッションでなく消費者インテントを売る」新モデルとしてGoogle/Metaを挑発するが、二次分析単独である。収益申告6系列分裂は解消されず、Astraの能力主張 (ARC-AGI-3 99.9%・9/8公式A-2) も交叉確認ガード (A) が同一ベンチ家族自己申告のため不充足のままである ([INFO-069](../Information/2026-09-15/collected-raw.md#INFO-069)・C-2は同一事象の再流通・二重計上禁止)。H-OAI-001の確度変更はS-1開示後再評価ゲート (終端2026-10-31) に予約されたまま、9/15バッチのAgents APIは「監査財務待ちのゲート凍結」 (v4.77制度) の下でC側累積に留まった。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Agents API発表: Codexハーネスのマネージド提供・skills配布の公式実装・multi_agent/MCP接続/self_hosted | H-OAI-001のB2B命題C側累積 (ゲート凍結中)。H-OAI-002の実行環境層統制深化 | A-2 | [INFO-004](../Information/2026-09-15/collected-raw.md#INFO-004) |
| 高 | Pachocki警告: 能力急速発展・アライメント未追随・CoT監視依存の持続不可能・Astraはステガノグラフィ能力の縁 | IND-030 (critical) の供給側二面性系列。Astra「監視が困難」公式自己開示 (9/8) の能力側裏付け | C-2 | [INFO-084](../Information/2026-09-15/collected-raw.md#INFO-084) |
| 高 | FOIA契約文書: ペンタゴンの「拒らないAI」ミッションモデル要求・最終契約に同条項なしと両者反論 | H-GOV-002の行動・文書級材料 (発話級と区別)。需要側の政府結合深化 | B-2 | [INFO-051](../Information/2026-09-15/collected-raw.md#INFO-051) |
| 高 | 義務的国家AI安全規制の要請 (カリフォルニア4法案支持・「暴走エージェント」引き金) + Altman減速原則同意・Christiano理事就任 | H-GOV-002 I側発話級累積3件 (v4.92・加重1/2以下)。H-OAI-003環境材料 | B-2 | [INFO-047](../Information/2026-09-15/collected-raw.md#INFO-047) [INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) [INFO-096](../Information/2026-09-15/collected-raw.md#INFO-096) |
| 中 | ChatGPT広告年間$10億規模・インテント販売モデル (インドオークション再プライシング) | 収益多角化の方向性。B-2単独でH-OAI-001確度変更の基準外 | B-2 | [INFO-062](../Information/2026-09-15/collected-raw.md#INFO-062) |
| 中 | Altman「OpenAIは2026年にIPOしない」明言 | CFO 2027年上場明言 (8/27 A-2) と整合。S-1ゲート終端2026-10-31の観測機は債券・銀団側に残る | B-2 | [INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) |
| 中 | ARC-AGI-3 Astra 0.999 (llm-stats) | 9/8公式99.9% (A-2) と同一事象。交叉確認ガード (A) 不充足維持・二重計上禁止 | C-2 | [INFO-069](../Information/2026-09-15/collected-raw.md#INFO-069) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 銀団帰属の取消条件 (価格報道+組成完了告知・貸付グループ構成変化・専業誌条項言及・S-1債務コミットメント開示) のいずれか | 暫定帰属「非公開通例」が取消されIND-029の価格条件系列が再開する | 2026-10-31 | [IND-029](../config/indicators.json) |
| OpenAIの公式財務 (監査付き) | 収益申告6系列分裂が解消しH-OAI-001のS-1ゲート再評価が発火する | 継続 | H-OAI-001 [IND-026](../config/indicators.json) |
| ARC-AGI-3交叉確認ガード (A) の充足 (他ベンチ家族・独立系の同一タスク計測) | Astra能力主張の一次級確定または下方修正。SCN-002/004交叉確認ガード制度の初適用事例になる | 継続 | [IND-025](../config/indicators.json) |
| Agents APIの採用定量 (セッション数・エンタープライズ利用・料金収益) | 「公式発表」から「実装定量」への移行でH-OAI-001/H-OAI-002のB2B命題が判別可能になる | 90日 | H-OAI-001 [IND-026](../config/indicators.json) |
| Daybreak「緩いセーフガード」段階展開の実行・Astra級本番監視での事故顕在化 | monitorability低下が実害として出現しIND-030再評価・H-OAI-003のI側強化 | 継続 | [IND-030](../config/indicators.json) H-OAI-003 |
| ペンタゴン契約の最終条項一次確認 (国防総省文書・OpenAI開示) | 「拒らないAI」要求の有無が確定し需要側構造の解釈が固定される | 90日 | H-GOV-002 [IND-030](../config/indicators.json) |
| 素数ギャップ証明の外部検証 | 246→186主張の独立系検証でIND-028系列の一次級適合例が確定または撤回される | 90日 | [IND-028](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 43% low | v4.93 ±0% (鮮度注記: 最終内容評価基盤2026-09-15収集・v4.92評価で全ゲート不発火)。Agents API ([INFO-004](../Information/2026-09-15/collected-raw.md#INFO-004)・A-2) はC側累積だが監査財務待ちのゲート凍結 (v4.77制度) 維持。S-1ゲート終端2026-10-31。収益一次不在・交叉確認ガード (A) 不充足 | 監査付き収益のセグメント内訳・Agents API採用定量・独立系ベンチ追証 | 収益停滞の監査一次・B2Bシェアの独立定量での劣位 |
| [H-OAI-002](../config/hypotheses.json) | MCP開放上にプロプライエタリ上位レイヤーで囲い込む | 44% low | v4.93 ±0% (同上)。Agents APIのマネージド実行環境化とレガシー終了 (Assistants API・whisper-1) は実行環境層統制のC。API層はBYOキー開放継続で層区別原則不変 | 上位レイヤーでの独自機能依存の定量・レガシー移行の強制実測 | ポータビリティ標準の採用拡大・self_hosted級の実利用定量 |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンス達成を最優先とする | 3% low | v4.93 ±0%。「検閲・過剰整列の29日内顕在化」要素は不発火。Pachocki監視困難警告 ([INFO-084](../Information/2026-09-15/collected-raw.md#INFO-084)) はI側材料だが「検閲」語の適合は低いまま。Daybreak展開監視継続 | 検閲・過剰整列事象の具体的顕在化 | 商業化主導の継続 (広告事業等) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|---|
| [IND-013](../config/indicators.json) | エージェント供給チェーン攻撃 | 実害インシデントのA-2公表 | critical / rising | 2026-09-17 |
| [IND-025](../config/indicators.json) | フロンティア性能の交叉確認 | 独立系・他ベンチ家族での再現 | elevated / stable | 2026-09-17 |
| [IND-026](../config/indicators.json) | エージェント本番到達と期待-実態ギャップ | 本番到達率の反転 | high / rising | 2026-09-17 |
| [IND-027](../config/indicators.json) | 標準化と価格体系 | 価格2層分化の「高」復帰条件 | high / rising | 2026-09-17 |
| [IND-028](../config/indicators.json) | AGI叙事と実数学寄与 | 予測分裂の収束・素数ギャップ外部検証 | high / rising | 2026-09-17 |
| [IND-029](../config/indicators.json) | 資本コストと銀団価格 | 取消条件4種・テキサス監査 (終端12/10) | high / rising | 2026-09-17 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 (監視可能性) | critical解消3基準 | critical / rising | 2026-09-17 |

IND-013はCVE-2026-59176 (functype-mcp-server・Package Alias RCE) を在庫事案 (18悪性npm・[INFO-084](../Information/2026-09-08/collected-raw.md#INFO-084)) と非同一の独立事案と確定した (v4.93・確度高・在庫事案の格下げ仮説は支持材料として監視)。IND-029は第1観測機 (9/9窓閉鎖) の暫定帰属「非公開通例」条件付き批准を維持し次の実質観測機はテキサス474GW監査帰結 (終端12/10) とS-1終端。IND-030はN=1実質35R・Astra「監視が困難」自己開示にPachocki警告 ([INFO-084](../Information/2026-09-15/collected-raw.md#INFO-084)) が加わりcritical維持。

## 6. 変化履歴

| 日付 | 変更 | きっかけ |
|:---:|---|---|
| 2026-09-17 | v2形式へ全面書き直し。9/15バッチ (Agents API・減速要請・Pachocki警告・ペンタゴンFOIA・広告$1B) を初回計上。9/1のCursor供給終了 ([INFO-001](../Information/2026-09-01/collected-raw.md#INFO-001)・A-1) とv4.84裁定分も反映。§4/§5をv4.93値に更新 (9/16・17はDEGRADED-P1×2Rで新規証拠ゼロ) | 鮮度タイムアウト (8日) + 9/15バッチ未吸収 |
| 2026-09-09 | IND-029第1観測機閉鎖反映: 暫定帰属「非公開通例」条件付き批准・取消条件4種拡張事前登録 | [Arbiter v4.90](../state/arbiter-2026-09-09.md) |
| 2026-09-08 | Astra公式全文 (INFO-089) と公式changelog計上で§0〜§2全面更新。日付問題解消・「監視可能性低下」自己開示のIND-030計上 | [Arbiter v4.89](../state/arbiter-2026-09-08.md) |
| 2026-09-07 | Astra日付不整合とLuna/Terra価格出所を申し送り | Arbiter v4.88 |
| 2026-09-06 | ARC-AGI-3系列分裂を§1に計上 | Arbiter v4.87 |

## 7. ブラインドスポット

1. Agents APIの評価は公式発表文書のみに基づく。採用・利用・収益の定量が一切なく、発表と実装の乖離 (Anthropic EFS「今秋提供」前例) を割り引いて読む必要がある。
2. 減速要請・義務的規制支持・Christiano就任は発話級であり、行動・文書級 (安全を理由に獲得した契約・価格プレミアム) との加重差 (1/2以下・v4.92制度) が実際の審査で機能するか未検証である。
3. ペンタゴン契約の「拒らないAI」条項はドラフト段階のFOIA文書で、最終契約の内容は両当事者主張に依存する。需要側構造の解釈が一次確認なしに固定されるリスクがある。
4. 収益申告6系列分裂が解消されていない。広告$1B報道も二次分析単独で、収益構造の変化を測る監査一次は依然不在である。
5. 銀団「非公開通例」帰属は「静かな難航」と観測上ほぼ同値で判別は事前確率依存。取消条件が出るまでの観測は実質的に停止状態にある。
6. Pachocki警告はC-2 (ニュースレター経由) で、発言の一次文脈 (対面・文書種別) が未確認である。

## 付録: 直近30日の参照Evidence

| Evidence | 信用 | 事項 |
|---|:-:|---|
| [INFO-004](../Information/2026-09-15/collected-raw.md#INFO-004) | A-2 | Agents API発表 (公式): Codexハーネスのマネージド提供・skills配布の公式実装 |
| [INFO-047](../Information/2026-09-15/collected-raw.md#INFO-047) | B-2 | 義務的国家AI安全規制要請・カリフォルニア4法案支持 |
| [INFO-051](../Information/2026-09-15/collected-raw.md#INFO-051) | B-2 | ペンタゴンFOIA: 「拒らないAI」ミッションモデル要求の契約ドラフト |
| [INFO-052](../Information/2026-09-15/collected-raw.md#INFO-052) | B-2 | DOD分類ワークロード90%移行・Anthropic調達喪失の構造 (需要側背景) |
| [INFO-062](../Information/2026-09-15/collected-raw.md#INFO-062) | B-2 | ChatGPT広告年間$10億規模・インテント販売モデル |
| [INFO-084](../Information/2026-09-15/collected-raw.md#INFO-084) | C-2 | Pachocki警告: CoT監視依存の持続不可能・Astraのステガノグラフィ縁能力 |
| [INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) | B-2 | Altman減速原則同意・組み込み評価者・2026年IPO否定 |
| [INFO-096](../Information/2026-09-15/collected-raw.md#INFO-096) | B-2 | ChristianoのOpenAI Foundation理事就任 |
| [INFO-069](../Information/2026-09-15/collected-raw.md#INFO-069) | C-2 | ARC-AGI-3 Astra 0.999 (9/8公式99.9%と同一事象) |
| [INFO-046](../Information/2026-09-15/collected-raw.md#INFO-046) | B-2 | トランプEO州規制封じ (規制環境・両義注記) |
| [INFO-107](../Information/2026-09-15/collected-raw.md#INFO-107) | A-2 | 上院duty of care法案交渉 (条文不在・規制環境) |
| [Arbiter v4.90](../state/arbiter-2026-09-09.md) | 裁定 | 銀団第1観測機閉鎖・暫定帰属「非公開通例」条件付き批准 |
| [Arbiter v4.92](../state/arbiter-2026-09-16.md) | 裁定 | 9/15バッチ初回評価 (全ゲート不発火)・発話級/行動級2段階加重制度 |
| [Arbiter v4.93](../state/arbiter-2026-09-17.md) | 裁定 | 全仮説±0%・鮮度注記制度登録・CVE-2026-59176判定確定 |
