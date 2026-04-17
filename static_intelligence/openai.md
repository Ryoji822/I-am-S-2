# OpenAI

> 最終更新: 2026-04-17
> 確度: 中

$122B調達を完了し評価額$852Bに到達した [INFO-016](../Information/2026-04-07/collected-raw.md#INFO-016)。だが収益$13.1Bで黒字化未達、エンタープライズLLMシェア27%でAnthropic（40%）に劣後したまま。

2026年4月半ば、OpenAIはCodexを「コーディングアシスタント」から**自律型開発プラットフォーム**に変えた。デスクトップアプリ操作（マウス・キーボード制御）、インアプリブラウザ、メモリ機能、111プラグイン、マルチターミナル、SSH、画像生成・編集、heartbeats（セッション間コンテキスト維持）を一挙に追加 [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014) [INFO-025](../Information/2026-04-17/collected-raw.md#INFO-025)。GPT-5.3-Codexが25時間連続稼働で30K行コードを生成し [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)、Cursorは「OpenAIモデルは長時間自律作業で明確に優秀」と評価した。同時にAgents SDKを大幅アップデートし、7つのサンドボックスプロバイダーに対応 [INFO-010](../Information/2026-04-17/collected-raw.md#INFO-010)。囲い込みと開放が同時に進む二重運動は継続しているが、Codexの質的転換は新しいレイヤーの証拠を加えた。

## 基本情報

- **本社**: サンフランシスコ
- **CEO**: Sam Altman
- **主力製品**: ChatGPT、GPT-5.4シリーズ（Pro/mini/nano）、Agents SDK、Frontierプラットフォーム、**Codex**（desktop control・browser・memory・111 plugins・heartbeats・multi-terminal・SSH・画像生成）、Operator（CUA）、GPT-5.4-Cyber（サイバー防御特化）
- **推定従業員数**: 4,000人（年末までに8,000人に倍増予定）
- **直近の資金調達**: $122B（評価額$852B）。SoftBank、Amazon（$50B）、Nvidia（$30B）、Microsoftが主要投資家

資金力はAI業界最大。年間収益$13.1B、月間収益$2B。ChatGPT週間アクティブユーザー9億人、5000万以上のサブスクライバー。H2 2026にIPOを検討中。

GPT-5.4 ProはARC-AGI-2で83.3%を記録し人間（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。GPQA Diamond 92.8%。OSWorld-Verified 75.0%。GPT-5.4 miniは$0.75/$4.50で400Kコンテキスト、GPT-5.4 nanoは$0.20/$1.25でサブエージェント最適化 [INFO-026](../Information/2026-03-22/collected-raw.md#INFO-026)。

**GPT-5.4-Cyber**: サイバー防御特化モデル。バイナリリバースエンジニアリング能力を追加。Trusted Access for Cyber（TAC）プログラムを数千人の防御者に拡大。Codex Securityが3,000件以上のCritical/High脆弱性修正に貢献 [INFO-006](../Information/2026-04-16/collected-raw.md#INFO-006)。

**Codex App大幅アップデート**（2026年4月16-17日）: desktop control（マウス・キーボード制御）でGUIを人間と同じ速度で操作 [INFO-027](../Information/2026-04-17/collected-raw.md#INFO-027)。インアプリブラウザ追加。メモリ機能（preview）でセッション間コンテキスト維持 [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014)。111プラグイン統合（CodeRabbit、GitLab Issues等）。Enterprise向けpay-as-you-go価格設定。multi-terminal、SSH into devboxes対応。heartbeats（automations）で同一スレッド内でコンテキストを維持し、次のステップを自動スケジュール [INFO-022](../Information/2026-04-17/collected-raw.md#INFO-022)。画像生成・編集・GIF作成 [INFO-021](../Information/2026-04-17/collected-raw.md#INFO-021)。書類プレビュー（スプレッドシート含む）[INFO-024](../Information/2026-04-17/collected-raw.md#INFO-024)。

**GPT-5.3-Codex**: 25時間連続稼働で30K行コード生成を METR が検証。約7ヶ月の倍増期間を確認 [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)。

エンタープライズAI利用はYoY 8倍。**100万以上のビジネス顧客**、**300万週間アクティブCodexユーザー**に到達 [INFO-007](../Information/2026-04-16/collected-raw.md#INFO-007)。API処理は150億トークン/分。ただしLLM支出シェアは27%でAnthropic（40%）に劣後。Rampデータでは2月に-1.5%（過去最大の月間減少）を記録 [INFO-033](../Information/2026-03-22/collected-raw.md#INFO-033)。

## 主要動向タイムライン

| 日付 | イベント | 信頼性 | 引用 |
|------|---------|-------|------|
| 2026-04-16 | **Codex App大幅アップデート**（desktop control・browser・memory・111 plugins・heartbeats・multi-terminal・SSH・画像生成） | A-2 | [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014) [INFO-025](../Information/2026-04-17/collected-raw.md#INFO-025) |
| 2026-04-17 | GPT-5.3-Codex 25hr連続稼働・METR約7ヶ月倍増期間検証 | A-1 | [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006) |
| 2026-04-15 | Agents SDK大幅アップデート（ネイティブサンドボックス実行+7社公式パートナー） | A-3 | [INFO-010](../Information/2026-04-17/collected-raw.md#INFO-010) |
| 2026-04-14 | GPT-5.4-Cyber発表、TACプログラム拡大 | A-3 | [INFO-006](../Information/2026-04-16/collected-raw.md#INFO-006) |
| 2026-04-14 | Codex価格改定（トークン使用量ベース）、$100/月Pro Tier新設 | A-3 | [INFO-045](../Information/2026-04-16/collected-raw.md#INFO-045) |
| 2026-04-13 | Cloudflare Agent CloudにGPT-5.4/Codex統合、GA到達 | A-3 | [INFO-007](../Information/2026-04-16/collected-raw.md#INFO-007) |
| 2026-04-09 | CyberAgent ChatGPT Enterprise利用率93%事例 | A-3 | [INFO-008](../Information/2026-04-16/collected-raw.md#INFO-008) |
| 2026-04-14 | Snowflake $200Mパートナーシップ | B-3 | [INFO-025](../Information/2026-04-16/collected-raw.md#INFO-025) |
| 2026-04-14 | OpenAIがイリノイ州AI責任制限法案を支持 | B-3 | [INFO-040](../Information/2026-04-16/collected-raw.md#INFO-040) |
| 2026-04-07 | $122B調達完了（評価額$852B） | A-3 | [INFO-016](../Information/2026-04-07/collected-raw.md#INFO-016) |
| 2026-04-07 | #QuitGPT運動（250万ユーザー削除、アンインストール295%急増） | A-3 | [INFO-014](../Information/2026-04-07/collected-raw.md#INFO-014) |

## 戦略方向性

### 現在の主力仮説

#### エンタープライズ開発プラットフォームになる（H-OAI-001、確度61%）

Codexの包括的アップデートは「コーディングアシスタント」から「自律型エンタープライズ開発プラットフォーム」への質的転換を実証した [Arbiter v3.52](../state/arbiter-2026-04-17.md)。

5つの機能がB2B市場での支配的地位の必要条件を満たす:
1. Desktop control（マウス・キーボード制御）→ 企業の内部アプリケーション操作に直結 [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014)
2. 111 plugins（CodeRabbit/GitLab等）→ エンタープライズ開発パイプライン統合 [INFO-025](../Information/2026-04-17/collected-raw.md#INFO-025)
3. Enterprise向けpay-as-you-go → 企業向け価格設定 [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014)
4. GPT-5.3-Codex 25hr連続稼働 → 企業ワークロード信頼性の実証 [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)
5. Heartbeats + memory → セッション間コンテキスト維持 [INFO-022](../Information/2026-04-17/collected-raw.md#INFO-022)

Frontierプラットフォーム（HP、Intuit、Oracle、Uber採用）とResponses API一本化でエンタープライス基盤を固める。DoW契約でAnthropic SCR指定の間隙を突き政府市場に参入 [INFO-023](../Information/2026-03-20/collected-raw.md#INFO-023)。**Snowflake $200Mパートナーシップ**でエンタープライズデータ層への組み込みを加速 [INFO-025](../Information/2026-04-16/collected-raw.md#INFO-025)。

ただし**十分条件**（実際の市場シェアデータ・エンタープライス契約数）は依然不在。Codex WAUに消費者・個人開発者が含まれる可能性は有効。確度は62%→61%→60%→61%の推移で、Arbiterは「Codex Appの機能セットはSDKレイヤーを超えたエンタープライズ開発プラットフォーム」と判断した [Arbiter v3.52](../state/arbiter-2026-04-17.md)。

#### MCP上に独自実行環境を構築して囲い込む（H-OAI-002、確度56%）

Skills/ShellはMCPに対抗するものではなく、MCP上に構築された独自の上位レイヤー。Agents SDKはPython月間1470万DL、TypeScript 150万DL [INFO-006](../Information/2026-03-12/collected-raw.md#INFO-006)。

2026年4月、この仮説は新たな矛盾に直面した。**Agents SDKにネイティブサンドボックス実行を追加**し、Blaxel、Cloudflare、Daytona、E2B、Modal、Runloop、Vercelの**7社**を公式パートナーに組み込んだ [INFO-010](../Information/2026-04-17/collected-raw.md#INFO-010)。ハーネスとコンピュートの分離アーキテクチャで、設定可能なメモリ・ファイル・ツールワークフローを実現。スナップショット＆リハイドレーションによるdurable execution。

だが同時に[MCPが業界標準として臨界量を突破した](../config/indicators.json)（[IND-027](../config/indicators.json)、high）。MCP標準化進展は囲い込み否定の強力なI証拠。さらに7社パートナーのうち複数社はマルチプラットフォーム実績がある。排他性の有無が未確認では「囲い込みの決定的証拠」ではない [Arbiter v3.51](../state/arbiter-2026-04-16.md)。

**Codex価格をメッセージ単位→トークン使用量ベースに変更**した点も逆方向の動きだ [INFO-045](../Information/2026-04-16/collected-raw.md#INFO-045)。Batch APIは50%価格カット。価格競争に踏み出すことは囲い込みとは逆方向。

確度は56%で維持。囲い込みシグナル（サンドボックス独自化・Codex desktop control）と開放性シグナル（MCP標準化・価格競争・7社マルチプラットフォームパートナー）が相殺している。

### 代替仮説

#### AGI/スーパーインテリジェンス（H-OAI-003、確度1%、棄却候補）

Altmanは「2028年早期にASI」と公言するが、$122B調達、8,000人増員、政府契約拡大——経営行動はすべて商業化に向いている。OpenAI Foundationが$1B以上を生命科学・雇用・AIレジリエンスに投資するが、これはAGI研究というより社会的影響緩和とPR施策に近い。

**OpenAIがイリノイ州法案を支持**——AI企業のモデルハーム責任を制限する法案 [INFO-040](../Information/2026-04-16/collected-raw.md#INFO-040)。安全性よりも商業責任の軽減を優先する姿勢は、商業化軸足を補強する。確度1%で棄却候補。

## 強み・弱み・機会・脅威（SWOT）

### 強み

- 圧倒的な資金力（$122B、$852B評価額）
- 多層的なモデルラインナップ（GPT-5.4 Pro/mini/nano + Cyber特化）
- GPT-5.4 ProでARC-AGI-2人間超え（83.3%）、o3で87.5%
- **100万ビジネス顧客・300万週間アクティブCodexユーザー** [INFO-007](../Information/2026-04-16/collected-raw.md#INFO-007)
- ChatGPT週間アクティブユーザー9億人の消費者リーチ
- Agents SDK GitHub Stars 2,500（Claude SDKの2.5倍）
- Promptfoo買収でAI評価能力を内製化
- **Codexが自律型開発プラットフォームに進化**——desktop control・browser・memory・111 plugins・heartbeats・SSH [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014)
- GPT-5.3-Codex 25hr連続稼働でCursor評価「OpenAIモデルが長時間自律作業で明確に優秀」[INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)
- GPT-5.4-Cyberでサイバー防御ドメインにも専門化 [INFO-006](../Information/2026-04-16/collected-raw.md#INFO-006)
- Cloudflare Agent Cloudとの統合でエッジデプロイに進出 [INFO-007](../Information/2026-04-16/collected-raw.md#INFO-007)

### 弱み

- 技術的優位が市場シェアに転換できていない——エンタープライズ27%でAnthropic（40%）に劣後
- $13.1B年間収益で黒字化未達
- **#QuitGPT運動**で250万ユーザーがChatGPTを削除、アンインストール295%急増 [INFO-014](../Information/2026-04-07/collected-raw.md#INFO-014)
- Sora終了で動画生成市場から撤退、ByteDance・Googleに後れ
- Assistants API 8月廃止は開発者離れのリスク
- 囲い込み戦略と価格競争の二重運動が戦略の方向性を不透明にしている
- Codex desktop controlが新たなセキュリティ攻撃表面を生む ([IND-013](../config/indicators.json)、high)

### 機会

- Anthropic SCR指定の間隙を突く政府市場（DoW契約・AWS提携）
- Codex従量課金モデルがエンタープライス開発にフィットする可能性
- Snowflake $200M [INFO-025](../Information/2026-04-16/collected-raw.md#INFO-025) に始まるデータプラットフォーム統合
- GPT-5.4-Cyberでサイバー防御という新市場を開拓 [INFO-006](../Information/2026-04-16/collected-raw.md#INFO-006)
- H2 2026 IPOが透明性と資金調達の新段階に
- METR約7ヶ月倍増期間——2026年末には1-2週間の自律稼働が可能になる可能性 [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)

### 脅威

- Anthropicのエンタープライズ猛追（40%シェア、Opus 4.7 GA、Managed Agents GA）
- MCP標準化がOpenAI独自実行環境の囲い込みを無効化する可能性
- EU AI法全面執行（2026年8月）がコンプライアンスコストを増大
- DeepSeek V3.2等のOSSモデルが価格破壊を加速
- OpenAI自身が支持する責任制限法案が、社会的信頼を損なう逆効果のリスク [INFO-040](../Information/2026-04-16/collected-raw.md#INFO-040)
- Codex desktop controlがセキュリティインシデントの引き金になるリスク

## I&W監視ポイント

この企業に関連するI&W指標の状況:

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | GPT-5.4 Pro ARC-AGI-2 83.3%、o3 87.5%。90%閾値まで2.5pt |
| [IND-015](../config/indicators.json) スキル再定義 | elevated | rising | OpenClaw 5,400+スキル。Agents SDKネイティブサンドボックス追加。Codex 111 plugins |
| [IND-008](../config/indicators.json) 大企業の集中 | elevated | — | LLM支出27%。Anthropic 40%に劣後 |
| [IND-013](../config/indicators.json) セキュリティ侵害頻度 | high | rising | Codex desktop control新攻撃表面。Cyber Verification Programは対抗投資 |

## 変更履歴（直近5件のみ。詳細は git log を参照）

| 日付 | 変更内容 |
|------|---------|
| 2026-04-17 | Codex App大幅アップデート（desktop control・browser・memory・111 plugins・heartbeats・multi-terminal・SSH・画像生成）・GPT-5.3-Codex 25hr連続稼働・7社サンドボックスパートナー（Blaxel/Cloudflare追加）を反映して戦略方向性・基本情報・タイムライン・SWOTを書き直し。H-OAI-001 60→61%に更新 |
| 2026-04-16 | 鮮度タイムアウト対応（9日経過）。Agents SDK大幅アップデート（ネイティブサンドボックス+E2B/Daytona/Modal/Vercel 4社パートナー）、GPT-5.4-Cyber、Codex価格改定（トークン使用量ベース+$100/月Pro Tier）、100万ビジネス顧客・300万Codex WAU、Cloudflare Agent Cloud統合、Snowflake $200Mパートナーシップ、OpenAI責任制限法案支持を反映して全面書き直し。H-OAI-001 62→60%、H-OAI-002 57→56%に更新。SWOT・I&W監視ポイント・タイムライン表を新設 |
| 2026-04-07 | $122B調達完了（評価額$852B）、#QuitGPT運動（250万削除）、Claude App Store 1位を反映。H-OAI-001 65→62%、H-OAI-002 56→57%に更新 |
| 2026-03-29 | $120B調達完了（評価額$730B）、Sora終了を反映。収益$13.1B更新。H-OAI-003確度2→1% |
| 2026-03-24 | 2週間分統合。GPT-5.4 mini/nano、Agents SDK v0.7.2、Promptfoo買収を追加 |
