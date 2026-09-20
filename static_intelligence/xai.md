# xAI (SpaceXAI) — 企業インテリジェンス

> 最終判断更新: 2026-09-20 (前回 2026-09-17)
> 全体確信度: 測定不能 (公式一次の覆盖がGrok Build OSS公開と公式料金表で広がる一方、企業全体の定量 (性能交叉確認・収益・資本) は依然ほぼ不在)
> 情報非対称性: Grok BuildのOSS公開 (xai-org/grok-build) はGitHub公式由来 ([INFO-011](../Information/2026-09-20/collected-raw.md#INFO-011) A-2) だがライセンス条項・x.ai版との機能差は未確認。grok-4.20-multi-agent-0309は公式料金表掲載 ([INFO-010](../Information/2026-09-20/collected-raw.md#INFO-010) A-3) だが性能の独立交叉確認・採用定量は不在。「SpaceXAI」統合の公式発表本文は未観測のまま (統合日・法構造が要追証)。xAI固有の銀団価格・capex・収益はいずれも未観測。9/20収集のxAI増分はv4.96評価で全ゲート不発火・確度全件±0% (最終内容評価基盤: 2026-09-20収集)。
> 主参照: [config/hypotheses.json](../config/hypotheses.json) · [config/indicators.json](../config/indicators.json) · [state/arbiter-2026-09-20.md](../state/arbiter-2026-09-20.md) · [Information/2026-09-20/collected-raw.md](../Information/2026-09-20/collected-raw.md)

## 0. 一文要約

我々はxAIを「コーディングエージェントハーネスのGrok BuildをOSS公開し、マルチエージェント専用SKU (grok-4.20-multi-agent・1Mコンテキスト) を公式料金表に追加して、管理4社+OSS 1社のハーネス供給構造のOSS側に自ら位置した企業」と読む。Grok BuildはハーネスとTUIをxai-org/grok-buildで公開し ([INFO-011](../Information/2026-09-20/collected-raw.md#INFO-011) A-2・9/17)、料金表はgrok-4.3・4.20-0309-reasoning/non-reasoning・4.20-multi-agent-0309の4モデル体系で、multi-agentはショートコンテキスト$1.25/1M入力・Batch API全モデル20%割引を示す ([INFO-010](../Information/2026-09-20/collected-raw.md#INFO-010) A-3)。OSS公開は専有API導管系列と逆行する供給形態で低価格・開放系列 ([H-XAI-002](../config/hypotheses.json)) と整合するが、採用定量は不在のままである。H-XAI-004は52%・indeterminate、H-XAI-002は58%・lowを維持する (v4.96・全件±0%)。

## 1. コア判断

Grok BuildのOSS公開が供給形態の位置を明確にした。xAIはターミナルベースのコーディングエージェント (コードベース理解・ファイル編集・シェルコマンド実行) のハーネスとTUIをxai-org/grok-buildリポジトリで公開した ([INFO-011](../Information/2026-09-20/collected-raw.md#INFO-011) A-2)。v4.95が観測したハーネス5社同時供給構造 (管理ランタイム4社+OSS 1社) のうち、OpenAI (Agents API)・Google (Antigravityマネージドエージェント) が専有API導管を整備するのと対照的に、xAIはOSS側の供給事例として振る舞った。前回のRed対抗読み (管理ハーネスの専有導管化) に対する最初の構造的反例である。ただしOSS版とx.ai版の機能差・ライセンス条項は未確認で、公開が戦略の転換か周辺の放出かは判定できない。Arbiter v4.96が次回最優先に登録したAgents API配給条件 (OpenAI側) と併せ、ハーネス配給の開放/管理の判別が供給構造分析の焦点になる。

モデル体系が公式料金表で整理された。grok-4.3・grok-4.20-0309-reasoning・non-reasoning・grok-4.20-multi-agent-0309の4モデル構成で、multi-agentはコンテキスト1M・ショートコンテキスト$1.25/1M入力 (長文$0.20) で、Batch APIは全モデル20%割引である ([INFO-010](../Information/2026-09-20/collected-raw.md#INFO-010) A-3)。マルチエージェント専用SKUの登場はエージェント実行をモデル階層に組み込む方向だが、性能主張の独立系交叉確認はなく交叉確認ガード (A) は不充足のままである。表示価格は安価な層に入る一方、実質コスト (出力トークン量) の検証は従来通り不在である。

SpaceXAI統合の示唆は累積するが確定しない。9/15のchangelog title metadata「SpaceXAI」定着 ([INFO-007](../Information/2026-09-15/collected-raw.md#INFO-007) A-3) に続き、本日のINFO-011もソース表記で「SpaceXAI Docs」を使用する。ただし公式統合発表本文は依然未観測で、統合日・法構造 (合併・ブランド統合・事業部統合の別) は要追証である。H-XAI-004のゲート構造 (計数単位の区別・観測窓終端の設定・公式本文の一次取得・v4.89裁定3明文化) は不変で、モデルルーティング (1-2四半期)・F500解約率 (四半期)・維持率 (2四半期) の指標別観測窓が事前登録されたままである。OCI提供・Haggle Botに続く本日の2件も分布側Cで、採用定量は依然ゼロである。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Grok Build OSS公開 (xai-org/grok-build・ハーネス+TUI・9/17) | ハーネス5社構造のOSS側供給事例。[H-XAI-002](../config/hypotheses.json)低価格・開放系列と整合。専有導管系列への構造的反例 | A-2 | [INFO-011](../Information/2026-09-20/collected-raw.md#INFO-011) |
| 高 | 公式料金表: grok-4.20-multi-agent-0309 (1M ctx・$1.25/1M in short)・4モデル体系・Batch 20%割引 | モデル階層へのエージェント統合。性能交叉確認は不在で確度変更基準外 | A-3 | [INFO-010](../Information/2026-09-20/collected-raw.md#INFO-010) |
| 中 | ソース表記「SpaceXAI Docs」の公式使用継続 | H-XAI-004 C側蓄積の継続。公式統合本文不在のため確定材料でない | A-3 | [INFO-010](../Information/2026-09-20/collected-raw.md#INFO-010) [INFO-011](../Information/2026-09-20/collected-raw.md#INFO-011) |
| 低 | Grok 4.5ハルシネーション54% (正答52%とほぼ同率) | 品質系I側在庫 (C-2集約業者・前回計上の継続) | C-2 | [INFO-073](../Information/2026-09-15/collected-raw.md#INFO-073) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Grok Build OSS版のライセンス条項・x.ai版との機能差の確認 | 「OSS公開」が戦略的転換か周辺放出かの判別。ハーネス配給の開放/管理判別のxAI側材料 | 30日 | [H-XAI-002](../config/hypotheses.json) [IND-027](../config/indicators.json) |
| grok-4.20-multi-agentの性能独立交叉確認 (同一タスク・第三者計測) | 交叉確認ガード (A) の充足・マルチエージェントSKUの能力確定または修正 | 継続 | [IND-025](../config/indicators.json) |
| SpaceXAI公式統合発表本文の一次取得 | H-XAI-004確度判定の一次契機 (統合日・法構造・合体の定義)。計数単位区別 (文書数vs観察数) を適用 | 90日 | H-XAI-004 [IND-029](../config/indicators.json) |
| OSS公開・OCI提供の採用定量 (利用企業数・ワークロード・料金収益) | 「配信拡大」が「採用拡大」に転換したかの判別。indeterminate解除条件への接点 | 90日 | H-XAI-004 [IND-026](../config/indicators.json) |
| CursorチャネルでのGPT系遮断の真偽 (E-4品質・未再出現) | 遮断が真なら特異的選択 (SCN-003・H-OAI-002系列)・偽ならマルチベンダー基盤化説明が優位 | 30日 | H-XAI-004 H-OAI-002 |
| xAIの資金・評価額・計算基盤の定量 (銀団・capex) | Tier1稀少性が構造か収集欠陥かの判別 | 継続 | H-XAI-002 [IND-029](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-XAI-002](../config/hypotheses.json) | Grokを低価格で提供し価格競争でシェアを獲得する | 58% low | v4.96 ±0% (最終内容評価基盤2026-09-20収集)。Grok Build OSS公開 (INFO-011) とmulti-agent SKU $1.25 (INFO-010) は低価格・開放系列のC側材料。低価格戦略の独自性は業界全体コスト崩壊で決定的に希薄化 (v4.76) したまま、価格差からシェアへの転換定量は長期不在 | 低価格帯での採用シェア定量 (OCI・API・OSS利用) | 実質コスト上昇 (出力トークン+20%) の競合劣位確定 |
| [H-XAI-004](../config/hypotheses.json) | xAIとSpaceXの合体 (合併・完全統合) は2027年までに完了している | 52% indeterminate | v4.96 ±0%。C側最強級蓄積 (Haggle Bot A-2・metadata相互検証 B-2・changelog title定着 A-3・OSS公開 A-2) が継続するも、ルーティング数・解約率・維持率の採用定量不在でindeterminate構造不変。観測窓終端 (正規一次確認期限) と指標別観測窓 (ルーティング1-2四半期・解約率四半期・維持率2四半期) が事前登録済み | SpaceX/Anysphere・SEC/HSR級の正規一次・採用定量の出現 | 統合否定の一次 (契約解消・独立運営の公式表明) |

棄却済み: [H-XAI-001](../config/hypotheses.json) (35% rejected・Xデータ活用証拠不在) と [H-XAI-003](../config/hypotheses.json) (35% rejected・特化AI製品証拠不在) は再活性化証拠なし (v4.91-96維持)。

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | エージェント供給チェーン攻撃 | 実害インシデントのA-2公表 | critical / rising (v4.96・HF事件700エージェント特定で検知系列の分岐監視強化) | 2026-09-20 |
| [IND-025](../config/indicators.json) | Grok系性能の独立系交叉確認 | 第三者・同一タスク計測 | elevated / stable (v4.96・状態変更なし) | 2026-09-20 |
| [IND-026](../config/indicators.json) | エージェント本番到達 (OCI・Cursor・OSS経路) | 本番到達率の反転 | high / rising (v4.96・状態変更なし) | 2026-09-20 |
| [IND-027](../config/indicators.json) | 配信経路の標準化と価格体系 | 配給チャネル独自性・開放の定量 | high / rising (v4.96)。Grok Build OSS公開 (INFO-011) でハーネス供給の開放側材料が加わった。専有導管 (Agents API・Antigravity) との判別が次の焦点 | 2026-09-20 |
| [IND-029](../config/indicators.json) | xAI固有の資本コスト (未観測) | 銀団・capex一次の出現 | high / rising (v4.96・AI個別発行体スプレッドの新監視ライン登録) | 2026-09-20 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 | critical解消3基準 | critical / rising (v4.96・N=1実質37R) | 2026-09-20 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ |
|:---:|---|---|
| 2026-09-20 | ターゲット編集。Grok Build OSS公開 (INFO-011・A-2) とgrok-4.20-multi-agent-0309の料金表掲載 (INFO-010・A-3) を新規計上し、ハーネス5社構造でのOSS側位置づけを§0/§1に反映。§4/§5をv4.96値に更新 | [INFO-010](../Information/2026-09-20/collected-raw.md#INFO-010)/[011](../Information/2026-09-20/collected-raw.md#INFO-011) + Arbiter v4.96 |
| 2026-09-17 | v2形式へ全面書き直し。9/15バッチ (SpaceXAI title定着・OCI提供・ハルシネーション54%) を初回計上。§4/§5をv4.93値に更新 | 鮮度タイムアウト (9日) + 9/15バッチ未吸収 + v2移行 |
| 2026-09-08 | Haggle Bot公式実証 (INFO-090) とSpaceXAI相互検証 (INFO-092) を計上。ゲート構造明文化 (計数単位・観測窓終端・Cursorチャネル読み分け) | [Arbiter v4.89](../state/arbiter-2026-09-08.md) |
| 2026-09-05 | Grok Bot初出 (A-1級) とCursor買収8/14発効・api2.cursor.sh配布の初観測を計上 | Arbiter v4.86 |

## 7. ブラインドスポット

1. OSS公開の実質が不明である。ライセンス (真正のOSSか部分公開か)・x.ai版との機能差・公開範囲の確認なしに「開放の転換」と読むのは先走る。公開継続のコミットも観察されていない。
2. SpaceXAI統合の公式発表本文が未観測。metadata類の累積は強い示唆だが、統合日・法構造が確定しない限りH-XAI-004はindeterminateを維持する (観測窓終端が近づくほど「恒久的発火不能ゲート」批判が現実化する)。
3. OCI提供・OSS公開・multi-agent SKUはいずれも配信・供給的事実であって採用的事実でない。「見かけの前進」の自查を継続する。
4. ハルシネーション54%は集約業者 (C-2) 単独で、手法の同等性が独立に検証されていない。Grok系の品質劣位の確定材料として使えない。
5. モデル性能の独立系交叉確認・収益・資本コストがすべて未観游。Tier1目標の稀少性は検索収穫の構造と収集方法の欠陥の判別がつかない。

## 付録: 直近30日の参照Evidence

| Evidence | 信用 | 事項 |
|---|:-:|---|
| [INFO-011](../Information/2026-09-20/collected-raw.md#INFO-011) | A-2 | Grok Build OSS公開 (xai-org/grok-build・ハーネス+TUI・9/17) |
| [INFO-010](../Information/2026-09-20/collected-raw.md#INFO-010) | A-3 | 公式料金表: grok-4.20-multi-agent-0309 (1M ctx・$1.25/1M in)・4モデル体系・Batch 20%割引 |
| [INFO-007](../Information/2026-09-15/collected-raw.md#INFO-007) | A-3 | Grok Build v0.2.107 changelog・title metadata「SpaceXAI」定着 (前回計上の基盤) |
| [INFO-008](../Information/2026-09-15/collected-raw.md#INFO-008) | A-3 | Oracle OCIでGrok 4.6提供 (前回計上の基盤) |
| [INFO-090](../Information/2026-09-08/collected-raw.md#INFO-090) | A-2 | Haggle Bot公式実証: $100K超節約・api2.cursor.sh配布 (前回計上の継続) |
| [INFO-073](../Information/2026-09-15/collected-raw.md#INFO-073) | C-2 | ハルシネーション横断比較: Grok 4.5は54% (前回計上の継続) |
| [Arbiter v4.96](../state/arbiter-2026-09-20.md) | 裁定 | 全仮説±0%・Agents API配給条件を次回最優先 (ハーネス判別の対抗観測) |
| [Arbiter v4.93](../state/arbiter-2026-09-17.md) | 裁定 | 全仮説±0%・鮮度注記制度登録 (前回更新の基盤) |
