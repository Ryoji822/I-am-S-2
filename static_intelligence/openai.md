# OpenAI

> 最終更新: 2026-04-22
> 確度: 中

$122B調達を完了し評価額$852Bに到達した [INFO-016](../Information/2026-04-07/collected-raw.md#INFO-016)。だが収益$13.1Bで黒字化未達、エンタープライズLLMシェア27%でAnthropic（40%）に劣後したまま。

2026年4月半ばのCodex大幅アップデートから一週間で、OpenAIはB2Bチャネルを一気に開いた。**Codex Labs**を発表し、OpenAIの専門家が直接企業に入るハンズオンワークショップを開始 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)。同時に**GSI 7社**（Accenture、PwC、Capgemini、CGI、Cognizant、Infosys、TCS）と提携し、従来のIT巨大企業のB2Bチャネル経由でエンタープライス市場を獲得する新パターンを確立した [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)。Codex週間アクティブユーザーが2週間で3M→4Mに急増（33%増）。Virgin Atlantic、Ramp、Notion、Cisco、Rakuten等が採用。

Codex自体も「コーディングアシスタント」から**自律型開発プラットフォーム**に変貌した。デスクトップアプリ操作、インアプリブラウザ、メモリ機能、90以上のプラグイン、マルチターミナル、SSH、画像生成・編集、heartbeatsを一挙追加 [INFO-002](../Information/2026-04-22/collected-raw.md#INFO-002)。Agents SDKはネイティブサンドボックス実行、MCP・Skills・AGENTS.md統合、7社サンドボックスプロバイダー対応に大幅アップデート [INFO-003](../Information/2026-04-22/collected-raw.md#INFO-003)。

そして**GPT-Rosalind**でドメイン特化モデルに乗り出した。ライフサイエンス研究向け推論モデルでBixBench Pass@1 0.751——人間専門家の95%タイルを超えた [INFO-003](../Information/2026-04-19/collected-raw.md#INFO-003)。GPT-5.4-Cyberに続く2つ目のドメイン特化モデルで、汎用→垂直展開の戦略が形になりつつある。

## 基本情報

- **本社**: サンフランシスコ
- **CEO**: Sam Altman
- **主力製品**: ChatGPT、GPT-5.4シリーズ（Pro/mini/nano）、Agents SDK、Frontierプラットフォーム、**Codex**（desktop control・browser・memory・90+ plugins・heartbeats・multi-terminal・SSH・画像生成）、**Codex Labs**（エンタープライズハンズオン）、Operator（CUA）、GPT-5.4-Cyber（サイバー防御特化）、**GPT-Rosalind**（ライフサイエンス特化）
- **推定従業員数**: 4,000人（年末までに8,000人に倍増予定）
- **直近の資金調達**: $122B（評価額$852B）。SoftBank、Amazon（$50B）、Nvidia（$30B）、Microsoftが主要投資家

資金力はAI業界最大。年間収益$13.1B、月間収益$2B。ChatGPT週間アクティブユーザー9億人、5000万以上のサブスクライバー。H2 2026にIPOを検討中。

GPT-5.4 ProはARC-AGI-2で83.3%を記録し人間（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。GPQA Diamond 92.8%。OSWorld-Verified 75.0%。**GPT-5.4 Proはマルチモーダルリーダーボード暫定1位**（weighted 100.0%）[INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。GPT-5.4 miniは2x以上高速 [INFO-061](../Information/2026-04-22/collected-raw.md#INFO-061)。$100/月プランはPlus比5x Codex使用量 [INFO-064](../Information/2026-04-22/collected-raw.md#INFO-064)。

**GPT-5.4-Cyber**: サイバー防御特化モデル。Trusted Access for Cyber（TAC）プログラムを数千人の防御者に拡大。Codex Securityが3,000件以上のCritical/High脆弱性修正に貢献 [INFO-006](../Information/2026-04-16/collected-raw.md#INFO-006)。

**Codex App大幅アップデート**（2026年4月16日）: desktop control（マウス・キーボード制御）でGUIを人間と同じ速度で操作 [INFO-027](../Information/2026-04-17/collected-raw.md#INFO-027)。インアプリブラウザ追加。メモリ機能（preview）でセッション間コンテキスト維持 [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014)。90+プラグイン統合（Atlassian Rovo、CircleCI、CodeRabbit、GitLab等）。Enterprise向けpay-as-you-go価格設定。multi-terminal、SSH into devboxes対応。heartbeats（automations）で同一スレッド内でコンテキストを維持 [INFO-022](../Information/2026-04-17/collected-raw.md#INFO-022)。画像生成・編集・GIF作成 [INFO-021](../Information/2026-04-17/collected-raw.md#INFO-021)。gpt-image-1.5による画像生成統合 [INFO-002](../Information/2026-04-22/collected-raw.md#INFO-002)。

**Codex Labs**（2026年4月21日発表）: OpenAI専門家が直接組織に入るハンズオンワークショップ。**GSI 7社**（Accenture、Capgemini、CGI、Cognizant、Infosys、PwC、TCS）と提携し企業展開を加速 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)。コーディング以外のタスク（briefs、plans、checklists）にも拡張。WAU 3M→4M（2週間で33%増）。

**GPT-5.3-Codex**: 25時間連続稼働で30K行コード生成をMETRが検証。約7ヶ月の倍増期間を確認 [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)。

エンタープライズAI利用はYoY 8倍。**100万以上のビジネス顧客**、**400万週間アクティブCodexユーザー**に到達 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)。API処理は150億トークン/分。ただしLLM支出シェアは27%でAnthropic（40%）に劣後。Rampデータでは2月に-1.5%（過去最大の月間減少）を記録 [INFO-033](../Information/2026-03-22/collected-raw.md#INFO-033)。

**Agents SDK大幅アップデート**（2026年4月15日）: ネイティブサンドボックス実行、MCP・Skills・AGENTS.md・Shell・Apply Patch等の業界標準プリミティブ統合。Blaxel、Cloudflare、Daytona、E2B、Modal、Runloop、Vercelの7社サンドボックスプロバイダー対応 [INFO-003](../Information/2026-04-22/collected-raw.md#INFO-003)。Manifest抽象化でローカル→本番の移植性を実現。スナップショット・リハイドレーションによる耐久実行 [INFO-018](../Information/2026-04-22/collected-raw.md#INFO-018)。

**GPT-Rosalind**（2026年4月16日発表）: ライフサイエンス研究向け専門推論モデル。BixBench Pass@1: 0.751でGemini 3.1 Pro（0.550）を上回る [INFO-003](../Information/2026-04-19/collected-raw.md#INFO-003)。Amgen、Moderna、Allen Institute、Thermo Fisher等と提携。Codex用Life Sciencesプラグイン（50+科学データベース接続）をOSS公開。

## 主要動向タイムライン

| 日付 | イベント | 信頼性 | 引用 |
|------|---------|-------|------|
| 2026-04-21 | **Codex Labs**発表 + **GSI 7社提携**（Accenture/PwC/Capgemini等）+ WAU 3M→4M | A-3 | [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001) |
| 2026-04-21 | **Deep Research Max**（Google、Gemini 3.1 Pro搭載MCP対応自律リサーチ） | A-3 | [INFO-004](../Information/2026-04-22/collected-raw.md#INFO-004) |
| 2026-04-16 | Codex for (almost) everything — バックグラウンドコンピューター使用・90+新規プラグイン・画像生成・メモリ | A-3 | [INFO-002](../Information/2026-04-22/collected-raw.md#INFO-002) |
| 2026-04-16 | **GPT-Rosalind**発表（ライフサイエンス特化、BixBench 0.751、人間専門家95%tile超え） | A-3 | [INFO-003](../Information/2026-04-19/collected-raw.md#INFO-003) |
| 2026-04-16 | **Codex App大幅アップデート**（desktop control・browser・memory・111 plugins・heartbeats・SSH） | A-2 | [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014) [INFO-025](../Information/2026-04-17/collected-raw.md#INFO-025) |
| 2026-04-15 | Agents SDK大幅アップデート（ネイティブサンドボックス+MCP統合+7社パートナー） | A-3 | [INFO-003](../Information/2026-04-22/collected-raw.md#INFO-003) [INFO-018](../Information/2026-04-22/collected-raw.md#INFO-018) |
| 2026-04-14 | GPT-5.4-Cyber発表、TACプログラム拡大 | A-3 | [INFO-006](../Information/2026-04-16/collected-raw.md#INFO-006) |
| 2026-04-14 | Codex価格改定（トークン使用量ベース）、$100/月Pro Tier新設 | A-3 | [INFO-034](../Information/2026-04-22/collected-raw.md#INFO-034) [INFO-064](../Information/2026-04-22/collected-raw.md#INFO-064) |
| 2026-04-07 | $122B調達完了（評価額$852B） | A-3 | [INFO-016](../Information/2026-04-07/collected-raw.md#INFO-016) |
| 2026-04-07 | #QuitGPT運動（250万ユーザー削除、アンインストール295%急増） | A-3 | [INFO-014](../Information/2026-04-07/collected-raw.md#INFO-014) |

## 戦略方向性

### 現在の主力仮説

#### エンタープライズ開発プラットフォームになる（H-OAI-001、確度62%）

Codexの包括的アップデートは「コーディングアシスタント」から「自律型エンタープライズ開発プラットフォーム」への質的転換を実証した。そして**Codex Labs + GSI 7社提携**は、その次の段階——B2Bチャネルの構築——を開いた [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)。

Accenture、PwC、Capgemini等のGSI（グローバルシステムインテグレーター）との提携は、これまでRed Agentが指摘し続けた「Codex≠エンタープライズB2B」への直接の回答だ [Arbiter v3.57](../state/arbiter-2026-04-22.md)。OpenAIが自前のエンタープライズ営業力を構築する代わりに、既存のIT巨大企業のチャネルを活用するという戦略。WAU 3M→4M（2週間33%増）は製品-市場適合の定量確認 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)。

Frontierプラットフォーム（HP、Intuit、Oracle、Uber採用）とResponses API一本化でエンタープライス基盤を固める。DoW契約でAnthropic SCR指定の間隙を突き政府市場に参入。Snowflake $200Mパートナーシップでエンタープライズデータ層への組み込みを加速。GPT-Rosalindでライフサイエンス特化に進出 [INFO-003](../Information/2026-04-19/collected-raw.md#INFO-003)。

ただし**十分条件**（実際の市場シェアデータ・エンタープライス契約数）は依然として不完全。**Reset to Zero問題**——マルチステップワークフローが予告なく致命的に失敗する——はエンタープライズ信頼性の構造的課題として蓄積している [INFO-070](../Information/2026-04-22/collected-raw.md#INFO-070)。確度は62% [Arbiter v3.57](../state/arbiter-2026-04-22.md)。

#### MCP上に独自実行環境を構築して囲い込む（H-OAI-002、確度56%）

Skills/ShellはMCPに対抗するものではなく、MCP上に構築された独自の上位レイヤー。Agents SDKはPython月間1470万DL、TypeScript 150万DL [INFO-006](../Information/2026-03-12/collected-raw.md#INFO-006)。

2026年4月、この仮説は新たな矛盾に直面した。Agents SDKにネイティブサンドボックス実行を追加し、7社を公式パートナーに組み込んだ [INFO-003](../Information/2026-04-22/collected-raw.md#INFO-003)。MCP・Skills・AGENTS.md・Shell等の業界標準プリミティブへの対応は囲い込み否定の強力なI証拠。[MCPが業界標準として臨界量を突破した](../config/indicators.json)（[IND-027](../config/indicators.json)、high）。

Codex価格をメッセージ単位→トークン使用量ベースに変更した点も逆方向の動き [INFO-034](../Information/2026-04-22/collected-raw.md#INFO-034)。Batch APIは50%価格カット。囲い込みシグナル（サンドボックス独自化・Codex desktop control）と開放性シグナル（MCP標準化・価格競争・7社マルチプラットフォームパートナー）が相殺している。

確度は56%で維持。

### 代替仮説

#### AGI/スーパーインテリジェンス（H-OAI-003、確度1%、棄却候補）

Altmanは「2028年早期にASI」と公言するが、$122B調達、8,000人増員、Codex Labs、GSI提携、政府契約拡大——経営行動はすべて商業化に向いている。OpenAIがイリノイ州法案を支持——AI企業のモデルハーム責任を制限 [INFO-040](../Information/2026-04-16/collected-raw.md#INFO-040)。安全性よりも商業責任の軽減を優先する姿勢は商業化軸足を補強する。確度1%で棄却候補。

## 強み・弱み・機会・脅威（SWOT）

### 強み

- 圧倒的な資金力（$122B、$852B評価額）
- 多層的なモデルラインナップ（GPT-5.4 Pro/mini/nano + Cyber + Rosalind特化）
- GPT-5.4 ProでARC-AGI-2人間超え（83.3%）、o3で87.5%、**マルチモーダル暫定1位**
- **100万ビジネス顧客・400万週間アクティブCodexユーザー** [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)
- ChatGPT週間アクティブユーザー9億人の消費者リーチ
- **Codex Labs + GSI 7社提携**でB2Bチャネル構築の質的転換 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)
- Codexが自律型開発プラットフォームに進化——desktop control・browser・memory・90+ plugins・heartbeats [INFO-002](../Information/2026-04-22/collected-raw.md#INFO-002)
- GPT-5.3-Codex 25hr連続稼働でCursor評価「OpenAIモデルが長時間自律作業で明確に優秀」[INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)
- GPT-5.4-Cyberでサイバー防御、GPT-Rosalindでライフサイエンス——垂直特化2製品 [INFO-003](../Information/2026-04-19/collected-raw.md#INFO-003)
- Agents SDK MCP統合 + 7社サンドボックスパートナー [INFO-003](../Information/2026-04-22/collected-raw.md#INFO-003)

### 弱み

- 技術的優位が市場シェアに転換できていない——エンタープライズ27%でAnthropic（40%）に劣後
- $13.1B年間収益で黒字化未達
- **#QuitGPT運動**で250万ユーザーがChatGPTを削除 [INFO-014](../Information/2026-04-07/collected-raw.md#INFO-014)
- Sora終了で動画生成市場から撤退
- **Reset to Zero問題**がエンタープライズ信頼性の構造的課題 [INFO-070](../Information/2026-04-22/collected-raw.md#INFO-070)
- Codex desktop controlが新たなセキュリティ攻撃表面を生む ([IND-013](../config/indicators.json)、high)。97%の企業が12ヶ月以内にAIエージェントインシデントを予期 [INFO-021](../Information/2026-04-22/collected-raw.md#INFO-021)
- 43%のAI生成コード変更が本番でデバッグ必要 [INFO-019](../Information/2026-04-19/collected-raw.md#INFO-019)

### 機会

- Anthropic SCR指定の間隙を突く政府市場（DoW契約・AWS提携）
- GSI 7社チャネルでエンタープライス営業力を借用 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)
- Codex従量課金モデルがエンタープライス開発にフィットする可能性
- GPT-5.4-Cyberでサイバー防御、GPT-Rosalindでライフサイエンスという新市場
- H2 2026 IPOが透明性と資金調達の新段階に
- METR約7ヶ月倍増期間——2026年末には1-2週間の自律稼働が可能になる可能性 [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)

### 脅威

- Anthropicのエンタープライズ猛追（40%シェア、Opus 4.7 GA、Managed Agents GA、$30B ARR確認）
- MCP標準化がOpenAI独自実行環境の囲い込みを無効化する可能性
- EU AI法全面執行（2026年8月）がコンプライアンスコストを増大 [INFO-051](../Information/2026-04-22/collected-raw.md#INFO-051)
- DeepSeek V4プレビューがコーディングベンチマークでGPT-5.5/Opus 4.7超えを目標 [INFO-062](../Information/2026-04-22/collected-raw.md#INFO-062)
- Reset to Zero問題がエンタープライズ導入の信頼性障壁に [INFO-070](../Information/2026-04-22/collected-raw.md#INFO-070)

## I&W監視ポイント

この企業に関連するI&W指標の状況:

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | GPT-5.4 Pro ARC-AGI-2 83.3%、o3 87.5%。マルチモーダル暫定1位。90%閾値まで2.5pt |
| [IND-015](../config/indicators.json) スキル再定義 | elevated | rising | Agents SDK MCP統合。Codex 90+ plugins。Codex Labs + GSI 7社 |
| [IND-008](../config/indicators.json) 大企業の集中 | elevated | — | LLM支出27%。Anthropic 40%に劣後 |
| [IND-013](../config/indicators.json) セキュリティ侵害頻度 | high | rising | Codex desktop control新攻撃表面。97%企業インシデント予期。Reset to Zero問題 [INFO-021](../Information/2026-04-22/collected-raw.md#INFO-021) [INFO-070](../Information/2026-04-22/collected-raw.md#INFO-070) |
| [IND-026](../config/indicators.json) エージェント本番環境到達率 | elevated | rising | Codex Labs GSI 7社 + Stanford 77%成功率 vs 54%計画/25%実績ギャップ + Reset to Zero |

## 変更履歴（直近5件のみ。詳細は git log を参照）

| 日付 | 変更内容 |
|------|---------|
| 2026-04-22 | Codex Labs + GSI 7社提携（B2Bチャネル質的転換）・WAU 3M→4M・Codex "for almost everything"90+ plugins・Agents SDK MCP統合・GPT-5.4 Proマルチモーダル暫定1位・GPT-5.4 mini/nano・$100/月プラン・Reset to Zero問題を反映して戦略方向性・基本情報・タイムライン・SWOTを書き直し。H-OAI-001 61→62%に更新 |
| 2026-04-19 | GPT-Rosalind（ライフサイエンス特化）を新製品として追加。Codex大幅アップデート・Agents SDK詳細を反映。セキュリティ指標更新 |
| 2026-04-17 | Codex App大幅アップデート・GPT-5.3-Codex 25hr連続稼働・7社サンドボックスパートナーを反映して全面書き直し。H-OAI-001 60→61%に更新 |
| 2026-04-16 | 鮮度タイムアウト対応（9日経過）。Agents SDK・GPT-5.4-Cyber・Codex価格改定を反映して全面書き直し |
| 2026-04-07 | $122B調達完了（評価額$852B）、#QuitGPT運動を反映 |
