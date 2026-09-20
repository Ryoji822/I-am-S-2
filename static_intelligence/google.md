# Google / DeepMind

> 最終判断更新: 2026-09-20 (前回 2026-09-15)
> 全体確信度: 測定不能 (H-GOO-001 indeterminate維持)
> 情報非対称性: Gemini固有のエンタープライズ定量採用データ (シェア・収益・利用率の直接定量A-2+) は60R超にわたり構造的に不在。MAUは消費者指標でありエンタープライズ採用シェアではない。UBS試算 (Google Cloud収益の27% (2026) →48%超 (2027) がOpenAI+Anthropicの2社依存) の分離不能性は拡大したまま。Interactions APIはv1betaのdocs層でGA・課金単位・採用条件は未公告 ([INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006) A-3)。AntigravityのマネージドエージェントはAI Studio公式docs ([INFO-009](../Information/2026-09-20/collected-raw.md#INFO-009) A-3) だが利用定量は不在。Hassabis「もはやDeepMindを率いない」報道は要追証 ([INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) B-2)。Flash系3.6〜3.8の期限付き価格と2027/1/1倍額移行は公式公示済み ([INFO-073](../Information/2026-09-20/collected-raw.md#INFO-073) A-3・9/15 INFO-066と同一内容の再確認)。
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はGoogleを「Antigravityのマネージドエージェント提供という自社管理の実行環境層を docs で整備し、音声層 (3.8 Live・3.5 Transcribe) とエージェント階層 (3.8 Flash/3.5 Flash-Lite) で供給面の拡張を続ける一方、固有の採用定量だけが現れ続けない企業」と読む。Gemini APIのManaged Agents Updateはantigravity-preview-09-2026ベースでagents.create()によるハーネス設定の保存・Files API・管理Credentials API・隔離Linuxサンドボックスを提供する ([INFO-009](../Information/2026-09-20/collected-raw.md#INFO-009) A-3)。Antigravity×Gemini 3.7 Flashのマルチエージェント問題解決事例 ([INFO-006](../Information/2026-09-20/collected-raw.md#INFO-006) A-3) とGemini 3.8 Live/3.5 Transcribe ([INFO-005](../Information/2026-09-20/collected-raw.md#INFO-005) A-3) が同じ週に公式博客で確認された。3社 (OpenAI/Anthropic/Google) の安全協業協議は公認スポークスマン確認済みのB-1に強化された ([INFO-084](../Information/2026-09-20/collected-raw.md#INFO-084) B-1・独禁法免除文脈)。仮説確度は3件とも±0% (v4.96)。

## 1. コア判断

### マネージドエージェントという管理実行環境層の実体化

AntigravityがAI Studioの公式docsでマネージドエージェント提供を実体化させた。base_agentはantigravity-preview-09-2026で、agents.create()でハーネス設定を保存しIDで呼び出す専有API導管としての構造、単一API呼び出しで隔離Linuxサンドボックス内のコード実行・ファイル管理・Web閲覧を行うGeminiエージェント、Files APIと管理Credentials API (MCPサーバー・サードパーティAPIの安全な利用)、max_total_tokensによる予算制御とリモートMCP対応が明記された ([INFO-009](../Information/2026-09-20/collected-raw.md#INFO-009) A-3)。v4.95が観測した管理ランタイム構造 (ハーネス5社=管理4社+OSS 1社) のGoogle側実体である。この材料は形式層 (Interactions API・A2A) でなく実行環境層の管理提供であり、[H-GOO-002](../config/hypotheses.json) (囲い込み回避) の次回+1%条件に事前登録された「GCP公式self-deploy利用定量または同等のデプロイ実体の開放定量」は充足しない。Antigravity×Gemini 3.7 Flashのマルチエージェント協調事例 (数学・工学問題) も公式ブログで提示され ([INFO-006](../Information/2026-09-20/collected-raw.md#INFO-006) A-3)、ハーネス/開発環境としての位置づけが強化された。

### 音声層とモデル編成の拡張

Gemini 3.8 Live (リアルタイム音声) と3.5 Transcribe (書き起こし) でリアルタイム音声アプリ構築が提供された ([INFO-005](../Information/2026-09-20/collected-raw.md#INFO-005) A-3)。Interactions API (v1beta) と3.8 Flash (長時間SWE/自律エージェント)・3.5 Flash-Lite (サブエージェント) の階層設計 ([INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006) A-3) に音声層が加わり、オーケストレータ・ワーカー・音声の多層編成がdocs上で揃った。価格は3.8 Flash $0.75/$3.75 (2027-01-01に$1.50/$7.50へ倍額)・3.1 Pro $2/$12が公式料金頁で再確認された ([INFO-073](../Information/2026-09-20/collected-raw.md#INFO-073) A-3・9/15 INFO-066と同一内容の再観測)。

### 規制・協調環境の更新

3社 (OpenAI/Anthropic/Google) の安全性協業協議は数週間継続し公認スポークスマンの確認する報道 (B-1) に強化された。独禁法免除 (antitrust waiver) が必要な協業形式とAI安全への$2B投資案の文脈を伴い、規制強化が小規模競合のコストを引き上げる批判も同時に報じられた ([INFO-084](../Information/2026-09-20/collected-raw.md#INFO-084) B-1)。9/15計上のINFO-079 (3社標準団体協議) の延長線で、民間標準化の制度設計が具体化しつつある。政府系列ではPentagonのAIワークロード移管先報道 ([INFO-060](../Information/2026-09-20/collected-raw.md#INFO-060) B-2) が9/15 INFO-052の同一事象再報道として再観測された (v4.96裁定2-2・H-GOV-002本日Cから除外)。

### 継続監視事項 (前回から不変)

Hassabis「もはやDeepMindを率いない」報道 ([INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) B-2・要追証) は[H-GOO-003](../config/hypotheses.json)の前提条件変数として監視在庫。フィンランド€130億投資の履行率・上院duty of care法案の条文提出・Extensions EOL (2026-11-26) 移行も前回登録のまま観測機を待つ。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Managed Agents Update: antigravity-preview-09-2026・agents.create()でのハーネス設定保存・Files/Credentials API・隔離サンドボックス | 実行環境層の管理提供 (専有API導管)。[H-GOO-002](../config/hypotheses.json)囲い込み側材料。self-deploy定量の+1%条件は不充足 | A-3 | [INFO-009](../Information/2026-09-20/collected-raw.md#INFO-009) |
| 高 | 3社安全協業協議のB-1化 (公認スポークスマン確認・独禁法免除文脈・$2B安全投資案) | [H-GOV-002](../config/hypotheses.json)環境材料。[SCN-005](../config/scenarios.json)文脈の民間標準化進展 | B-1 | [INFO-084](../Information/2026-09-20/collected-raw.md#INFO-084) |
| 中 | Antigravity×Gemini 3.7 Flashのマルチエージェント問題解決事例 (数学・工学) | ハーネス/開発環境の位置づけ強化。管理4社+OSS 1社構造のGoogle側材料 | A-3 | [INFO-006](../Information/2026-09-20/collected-raw.md#INFO-006) |
| 中 | Gemini 3.8 Live・3.5 Transcribe (リアルタイム音声) | 音声層の供給拡張。採用定量は不在 | A-3 | [INFO-005](../Information/2026-09-20/collected-raw.md#INFO-005) |
| 中 | 3.8 Flash $0.75/$3.75→2027-01-01倍額の公式再確認 | 9/15 INFO-066と同一内容の再観測 (二重計上禁止・価格層の維持確認) | A-3 | [INFO-073](../Information/2026-09-20/collected-raw.md#INFO-073) |
| 低 | Pentagon移管先報道 (OpenAI/Google/Microsoft・any lawful use) | 9/15 INFO-052の同一事象再報道 (v4.96で本日Cから除外) | B-2 | [INFO-060](../Information/2026-09-20/collected-raw.md#INFO-060) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|---|---|
| マネージドエージェント (Antigravity) のGA公告・課金単位・利用定量 | 専有API導管の商モデルが確定し形式層と実行層の重心判別が始まる | 90日 | [IND-027](../config/indicators.json) |
| GCP公式self-deploy利用定量または同等のデプロイ実体の開放定量 | [H-GOO-002](../config/hypotheses.json)次回+1%審査の必須条件 (v4.84事前登録) が充足される | 90日 | [H-GOO-002](../config/hypotheses.json) |
| Interactions APIのGA公告 (課金単位・採用条件・v1betaからの移行) | エージェント対話単位の商モデルが確定する | 90日 | [IND-027](../config/indicators.json) |
| Hassabisの組織離脱/残留の一次確認 (Google公式・組織公告) | [H-GOO-003](../config/hypotheses.json)の前提 (DeepMind統合シナジー) の再審査が発火する | 次回収集 | [H-GOO-003](../config/hypotheses.json) |
| Gemini固有の定量採用データ (A-2+品質のシェア・収益・利用率) の初公表 | [H-GOO-001](../config/hypotheses.json)のindeterminateが解消し新条件も発火する | 2026-12-31 | [H-GOO-001](../config/hypotheses.json) |
| 3.x系価格が2027-01-01に実際に倍増、または期間延長・撤回 | 価格権力の事前告知の検証。[SCN-003](../config/scenarios.json)材料の確定または失効 | 2027-01-01 | [IND-027](../config/indicators.json) |
| Extensions EOL (2026-11-26) までの移行完了率・機能ギャップ報告 | 強制移行の実害が判定される | 2026-11-26 | [H-GOO-002](../config/hypotheses.json) |
| 上院法案の条文提出とGoogle対象条項の確定 | duty of careの実質が判定される | 条文提出時 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | GoogleはGemini統合で検索・Workspace・Cloudのデータ優位を活かし、エンタープライズAI市場でシェアを拡大する | 50% (indeterminate) | v4.96 ±0% (最終内容評価基盤2026-09-20収集)。60R超の採用定量不在は継続。マネージドエージェント (INFO-009) と音声層 (INFO-005) は供給面の拡張で採用定量でない。C-only不定状態の駐車化注記継続 | Gemini固有の採用定量 (シェア・収益・利用率のA-2+) | UBS試算 (2社依存48%超) の四半期開示による検証 |
| [H-GOO-002](../config/hypotheses.json) | GoogleはGemini Tools & Agentsでオープン標準 (LangChain等) とのDay 0サポートを維持し、囲い込みを回避する | 25% (low) | v4.96 ±0%。マネージドエージェント (agents.create()の専有API導管・INFO-009) は実行環境層の管理提供で囲い込み側材料だが、次回+1%の必須条件 (self-deploy利用定量) は不充足。層区別原則 (形式層×実行層×価格層) 維持 | self-deploy利用定量・デプロイ実体の開放 | Extensions EOL移行の実害・専有API導管の採用拡大 |
| [H-GOO-003](../config/hypotheses.json) | GoogleはDeepMind統合シナジーでエコシステム深度・研究卓越性・インフラ統合を通じて競争力を維持する | 48% (medium) | v4.96 ±0% (本日評価なし)。Hassabis報道 (INFO-093・B-2・要追証) は監視在庫。Antigravity×3.7 Flashの問題解決事例 (INFO-006) は研究・開発環境側のC材料。新条件 (採用定量出現時または2026-12-31の再審査) は不変 | DeepMind指揮系統の一次確認・A-2+研究卓越性定量の連続出現 | Hassabis離脱の確定・研究者流失の累積 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・測定慣行 | 複数ベンチマーク×複数ラボで再現ならhigh | elevated/stable (v4.96・状態変更なし)。首位不同4R連続・ベンチ毎の分裂 (総合首位不存在) は継続 | 2026-09-20 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 期待-実態ギャップの定量蓄積 | high/rising (v4.96・状態変更なし)。Gemini固有の採用定量は不在継続。マネージドエージェントはdocs層で到達率の直接材料でない | 2026-09-20 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度 | 攻撃表面の標準化進行 | high/rising (v4.96・状態変更なし)。マネージドエージェント (INFO-009) で実行環境層の管理提供が一次確認。2027-01-01倍額移行はKIQ-MONETIZATION監視継続 | 2026-09-20 |
| [IND-028](../config/indicators.json) | AGI到達度 (予測分裂) | 分裂の深化・法制化圧力 | high/rising (v4.96・状態変更なし) | 2026-09-20 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | critical解消3基準 | critical/rising (v4.96・N=1実質37R)。GoogleはDoD 4社契約の一角 (INFO-060≡9/15 INFO-052の再観測扱い) | 2026-09-20 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-09-20 | ターゲット編集。Antigravityマネージドエージェントの実体化 (INFO-009・A-3) とAntigravity×3.7 Flash (INFO-006)・3.8 Live/3.5 Transcribe (INFO-005)・3社安全協業のB-1化 (INFO-084) を新規計上。§4/§5をv4.96値に更新 | 鮮度タイムアウト (5日) + [INFO-009](../Information/2026-09-20/collected-raw.md#INFO-009)/[006](../Information/2026-09-20/collected-raw.md#INFO-006)/[005](../Information/2026-09-20/collected-raw.md#INFO-005)/[084](../Information/2026-09-20/collected-raw.md#INFO-084) | H-GOO-001 50% (±0%)・H-GOO-002 25% (±0%)・H-GOO-003 48% (±0%) |
| 2026-09-15 | 全面書き直し (鮮度タイムアウト8日)。Interactions APIとモデル階層化・期限付き価格の公示・Hassabis報道・フィンランド€13B・上院法案の対象指定・3社標準団体を新規計上 | 鮮度タイムアウト + INFO-006/066/081/093 | H-GOO-001 50% (±0%)・H-GOO-002 25% (±0%)・H-GOO-003 48% (±0%) |
| 2026-09-07 | ターゲット編集。Flashキャンペーン価格の公式確認 (INFO-059・A-3)・antigravity統合 (INFO-013・A-2) を計上 | Arbiter v4.88（裁定2(d)/裁定9） | H-GOO-001 50% (±0%)・H-GOO-002 25% (±0%)・H-GOO-003 48% (±0%) |
| 2026-09-05 | §0〜§7書き直し (鮮度タイムアウト7日)。H-GOO-002 +1%とH-GOO-003条件入替を反映 | 鮮度タイムアウト + Arbiter v4.86 | H-GOO-002 24→25%・H-GOO-003 48% (条件入替) |

## 7. ブラインドスポット

- マネージドエージェントはdocs層の観察で、利用企業数・セッション数・料金収益の定量がない。専有API導管という構造読みが実態と異なる可能性は残る。
- Interactions APIとマネージドエージェントの関係 (同じ実行層か別系統か) がdocs上で明示されておらず、形式層・実行層の区別が完全でない。
- Gemini固有定量データが60R超構造的に不在。indeterminate分類の駐車化対処 (強制再評価条件の拡張) が記録されたまま実施されていない。
- Hassabis報道は単一報道で要追証である。8/15組織再編との差分 (完全離脱か役割変更か) を区別できていない。
- 3.8 Flash価格の再確認は同一頁の再取得で、頁の改訂履歴は取得していない。倍額移行の撤回・延長は2027年まで検証できない。
- UBSの2社依存試算 (27%→48%) は単一試算で前提が開示されていない。Cloud収益のGemini寄与分の分離は四半期開示でも残る可能性がある。

---

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-009](../Information/2026-09-20/collected-raw.md#INFO-009) | Managed Agents Update: antigravity-preview-09-2026・専有API導管・Files/Credentials API (A-3・実行環境層の管理提供) |
| [INFO-006](../Information/2026-09-20/collected-raw.md#INFO-006) | Antigravity×Gemini 3.7 Flashのマルチエージェント問題解決事例 (A-3) |
| [INFO-005](../Information/2026-09-20/collected-raw.md#INFO-005) | Gemini 3.8 Live・3.5 Transcribe (A-3・音声層の供給拡張) |
| [INFO-084](../Information/2026-09-20/collected-raw.md#INFO-084) | 3社安全協業協議のB-1化 (独禁法免除文脈・$2B安全投資案) |
| [INFO-073](../Information/2026-09-20/collected-raw.md#INFO-073) | 3.8 Flash期限付き価格の公式再確認 (A-3・INFO-066と同一内容の再観測) |
| [INFO-060](../Information/2026-09-20/collected-raw.md#INFO-060) | Pentagon移管先報道 (B-2・9/15 INFO-052の同一事象再報道・v4.96除外) |
| [INFO-006](../Information/2026-09-15/collected-raw.md#INFO-006) | Interactions API新設・モデル階層化 (A-3・前回計上の基盤) |
| [INFO-066](../Information/2026-09-15/collected-raw.md#INFO-066) | 3.8 Flash期限付き価格の初回公示 (A-3・前回計上の基盤) |
| [INFO-093](../Information/2026-09-15/collected-raw.md#INFO-093) | Hassabis「DeepMindを率いない」報道 (B-2・要追証・H-GOO-003の変数) |
| [INFO-081](../Information/2026-09-15/collected-raw.md#INFO-081) | フィンランド€130億投資・履行ギャップ (B-2・IND-029文脈) |
| [INFO-079](../Information/2026-09-15/collected-raw.md#INFO-079) | 3社安全共通標準団体創設協議 (B-2・INFO-084の前段) |
| [Arbiter v4.96](../state/arbiter-2026-09-20.md) | 全仮説±0%・INFO-060再観測除外 (裁定2-2) |
| [Arbiter v4.91](../state/arbiter-2026-09-15.md) | Blue失敗6日連続・全仮説±0% (前回更新の基盤) |
