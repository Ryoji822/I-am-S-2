# OpenAI

> 最終更新: 2026-04-29
> 確度: 中

$122B調達を完了し評価額$852Bに到達した [INFO-016](../Information/2026-04-07/collected-raw.md#INFO-016)。だが収益$13.1Bで黒字化未達、エンタープライズLLMシェア27%でAnthropic（40%）に劣後したまま。

2026年4月下旬、OpenAIの事業構造が二つ同時に動いた。まず**Microsoft提携の根本改訂**——OpenAI製品はAzure優先リリースを維持しつつ全クラウドで提供可能になり、MicrosoftのIPライセンスは2032年まで非排他化された [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)。これでOpenAIは単一クラウドのロックインから解放された。次に**OpenAI on AWS**——GPT-5.5、Codex、Amazon Bedrock Managed Agents powered by OpenAIがAWS上で利用可能になった [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。Microsoftの傘下から出て、3大クラウド全てに自社製品を載せる構えだ。

**Symphony**をオープンソース化した [INFO-002](../Information/2026-04-29/collected-raw.md#INFO-002)。Linear等のプロジェクト管理ツールをコーディングエージェントのコントロールプレーンに変換するエージェントオーケストレーター。一部チームでPR着地数が500%増加。囲い込み仮説（H-OAI-002）に逆行する動きだ。

## 基本情報

- **本社**: サンフランシスコ
- **CEO**: Sam Altman
- **主力製品**: ChatGPT、**GPT-5.5**（$5/$30、400K context・Thinking/Pro変種・コンピューター使用拡張）、GPT-5.4シリーズ（Pro/mini/nano）、Agents SDK、Frontierプラットフォーム、**Codex**（desktop control・browser・memory・90+ plugins・heartbeats・multi-terminal・SSH・画像生成）、**Codex Labs**（エンタープライズハンズオン）、**Workspace Agents**（共有エージェント・Slack連携・定期タスク・Codex harness）、**Symphony**（OSSエージェントオーケストレーター）、Operator（CUA）、GPT-5.4-Cyber（サイバー防御特化）、**GPT-Rosalind**（ライフサイエンス特化）、ChatGPT Images 2.0
- **推定従業員数**: 4,000人（年末までに8,000人に倍増予定）
- **直近の資金調達**: $122B（評価額$852B）。SoftBank、Amazon（$50B）、Nvidia（$30B）、Microsoftが主要投資家

資金力はAI業界最大。年間収益$13.1B、月間収益$2B。ChatGPT週間アクティブユーザー9億人、5000万以上のサブスクライバー。H2 2026にIPOを検討中。

GPT-5.4 ProはARC-AGI-2で83.3%を記録し人間（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。GPQA Diamond 92.8%。OSWorld-Verified 75.0%。**GPT-5.4 Proはマルチモーダルリーダーボード暫定1位**（weighted 100.0%）[INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。GPT-5.4 miniは2x以上高速 [INFO-061](../Information/2026-04-22/collected-raw.md#INFO-061)。$100/月プランはPlus比5x Codex使用量 [INFO-064](../Information/2026-04-22/collected-raw.md#INFO-064)。

**GPT-5.5**（2026年4月23日発表）: API価格$5/M入力・$30/M出力（GPT-5.4の2倍）。キャッシュ済み入力$0.50/M。400Kコンテキストウィンドウ（Codex内）。Thinking variant（難問題高速対応）・Pro variant（高精度作業向け）・Fast mode（1.5x高速・2.5x価格）。200社の早期アクセスパートナーで評価済み。Codexでのコンピューター使用・ブラウザ操作拡張。ChatGPT Images 2.0同時発表 [INFO-032](../Information/2026-04-24/collected-raw.md#INFO-032) [INFO-070](../Information/2026-04-24/collected-raw.md#INFO-070)。**AWS Bedrock経由でも利用可能に** [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。

**Microsoft提携改訂**（2026年4月27日）: Microsoftは引き続き主要クラウドパートナー、Azure優先リリースを維持。だがOpenAIは全クラウドプロバイダーで製品提供可能になった。MicrosoftのIPライセンスは2032年まで非排他化。Microsoft→OpenAIへの収益分配支払いは終了、OpenAI→Microsoftへの収益分配は2030年まで継続（上限あり）[INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)。

**OpenAI on AWS**（2026年4月28日）: GPT-5.5等のフロンティアモデル、Codex（CLI・デスクトップ・VS Code）、Amazon Bedrock Managed Agents powered by OpenAIがAWS Bedrockで利用可能に（限定プレビュー）[INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。Codex週間ユーザーは**400万+**に到達 [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。

**Symphony**（2026年4月27日OSS化）: エージェントオーケストレーター。プロジェクト管理ボードをコーディングエージェントのコントロールプレーンに変換。全タスクにエージェントを割り当て、連続実行、人間はレビューのみ [INFO-002](../Information/2026-04-29/collected-raw.md#INFO-002)。

**GPT-5.4-Cyber**: サイバー防御特化モデル。Trusted Access for Cyber（TAC）プログラムを数千人の防御者に拡大。Codex Securityが3,000件以上のCritical/High脆弱性修正に貢献 [INFO-006](../Information/2026-04-16/collected-raw.md#INFO-006)。

**Codex Labs**（2026年4月21日発表）: OpenAI専門家が直接組織に入るハンズオンワークショップ。**GSI 7社**（Accenture、Capgemini、CGI、Cognizant、Infosys、PwC、TCS）と提携し企業展開を加速 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)。

**GPT-Rosalind**（2026年4月16日発表）: ライフサイエンス研究向け専門推論モデル。BixBench Pass@1: 0.751でGemini 3.1 Pro（0.550）を上回る [INFO-003](../Information/2026-04-19/collected-raw.md#INFO-003)。Amgen、Moderna、Allen Institute、Thermo Fisher等と提携。

エンタープライズAI利用はYoY 8倍。**100万以上のビジネス顧客**、**400万週間アクティブCodexユーザー**に到達 [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。API処理は150億トークン/分。ただしLLM支出シェアは27%でAnthropic（40%）に劣後。Rampデータでは2月に-1.5%（過去最大の月間減少）を記録 [INFO-033](../Information/2026-03-22/collected-raw.md#INFO-033)。

## 主要動向タイムライン

| 日付 | イベント | 信頼性 | 引用 |
|------|---------|-------|------|
| 2026-04-28 | **OpenAI on AWS**発表（GPT-5.5/Codex/Managed Agents on Bedrock・Codex WAU 4M+） | A-3 | [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001) |
| 2026-04-27 | **Microsoft提携改訂**（非排他・全クラウド・IP非排他2032） | A-3 | [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003) |
| 2026-04-27 | **Symphony** OSS化（エージェントオーケストレーター・PR着地500%増） | A-3 | [INFO-002](../Information/2026-04-29/collected-raw.md#INFO-002) |
| 2026-04-23 | **GPT-5.5発表**（$5/$30、400K context、Thinking/Pro変種、コンピューター使用拡張）+ ChatGPT Images 2.0 | A-1 | [INFO-032](../Information/2026-04-24/collected-raw.md#INFO-032) [INFO-070](../Information/2026-04-24/collected-raw.md#INFO-070) |
| 2026-04-23 | **Workspace Agents**発表（共有エージェント・Slack連携・定期タスク・Codex harness） | A-3 | [INFO-021](../Information/2026-04-23/collected-raw.md#INFO-021) [INFO-022](../Information/2026-04-23/collected-raw.md#INFO-022) |
| 2026-04-21 | **Codex Labs**発表 + **GSI 7社提携**（Accenture/PwC/Capgemini等）+ WAU 3M→4M | A-3 | [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001) |
| 2026-04-16 | Codex for (almost) everything — バックグラウンドコンピューター使用・90+新規プラグイン・画像生成・メモリ | A-3 | [INFO-002](../Information/2026-04-22/collected-raw.md#INFO-002) |
| 2026-04-16 | **GPT-Rosalind**発表（ライフサイエンス特化、BixBench 0.751） | A-3 | [INFO-003](../Information/2026-04-19/collected-raw.md#INFO-003) |
| 2026-04-15 | Agents SDK大幅アップデート（ネイティブサンドボックス+MCP統合+7社パートナー） | A-3 | [INFO-003](../Information/2026-04-22/collected-raw.md#INFO-003) |
| 2026-04-07 | $122B調達完了（評価額$852B） | A-3 | [INFO-016](../Information/2026-04-07/collected-raw.md#INFO-016) |

## 戦略方向性

### 現在の主力仮説

#### エンタープライズ開発プラットフォームになる（H-OAI-001、確度64%）

Microsoft提携改訂はOpenAIの事業構造を変えた。Azure優先リリースは維持しつつ、全クラウドでの製品提供が可能になった [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)。OpenAI on AWSでGPT-5.5・Codex・Managed AgentsがBedrockに載る [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)。Codex WAUは4Mに到達した。

Codex Labs + GSI 7社提携でB2Bチャネルを開き [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)、Workspace Agentsでチーム向けワークフロー自動化に進出した [INFO-021](../Information/2026-04-23/collected-raw.md#INFO-021)。GPT-5.5の価格2倍は性能への確信とエンタープライズ層の値ごねなさへの賭けだ [INFO-032](../Information/2026-04-24/collected-raw.md#INFO-032)。

Microsoftが「ほぼ全てのエンタープライズにエージェントがあるが本番で動くものはほぼない」と認めた点は、エンタープライス到達範囲の拡大と実際の本番稼働の乖離を示す [INFO-012](../Information/2026-04-29/collected-raw.md#INFO-012)。確度は64% [Arbiter v3.63](../state/arbiter-2026-04-29.md)。

#### MCP上に独自実行環境を構築して囲い込む（H-OAI-002、確度55%）

囲い込み仮説は3件の独立した反証に直面した。Symphony OSS [INFO-002](../Information/2026-04-29/collected-raw.md#INFO-002)、Microsoft IP非排他2032 [INFO-003](../Information/2026-04-29/collected-003)、AAIF/MCP標準化 [INFO-016](../Information/2026-04-29/collected-raw.md#INFO-016)。名目的開放・実質囲い込みの可能性は残る——GPT-5.5価格2倍 [INFO-033](../Information/2026-04-29/collected-raw.md#INFO-033)、Workspace Agents独自環境、Agents SDK sandbox——だが開放の潮流が蓄積として優位に立った。

確度は55% [Arbiter v3.63](../state/arbiter-2026-04-29.md)。

### 代替仮説

#### AGI/スーパーインテリジェンス（H-OAI-003、確度1%、棄却候補）

Altmanは「2028年早期にASI」と公言するが、$122B調達、8,000人増員、Codex Labs、GSI提携、OpenAI on AWS、政府契約拡大——経営行動はすべて商業化に向いている。確度1%で棄却候補。

## 強み・弱み・機会・脅威（SWOT）

### 強み

- 圧倒的な資金力（$122B、$852B評価額）
- 多層的なモデルラインナップ（GPT-5.5 + GPT-5.4 Pro/mini/nano + Cyber + Rosalind特化）
- GPT-5.4 ProでARC-AGI-2人間超え（83.3%）、o3で87.5%、マルチモーダル暫定1位
- **100万ビジネス顧客・400万週間アクティブCodexユーザー** [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)
- ChatGPT週間アクティブユーザー9億人の消費者リーチ
- **3大クラウド全対応**: Azure優先+AWS Bedrock [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001) + GCP（ Agents SDK統合）
- **GSI 7社提携**でB2Bチャネル構築 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)
- **Workspace Agents**でチーム向けワークフロー自動化 [INFO-021](../Information/2026-04-23/collected-raw.md#INFO-021)
- **Symphony OSS**でエージェントオーケストレーション層に参入 [INFO-002](../Information/2026-04-29/collected-raw.md#INFO-002)
- Agents SDK MCP統合 + 7社サンドボックスパートナー [INFO-003](../Information/2026-04-22/collected-raw.md#INFO-003)

### 弱み

- 技術的優位が市場シェアに転換できていない——エンタープライズ27%でAnthropic（40%）に劣後
- $13.1B年間収益で黒字化未達
- **Reset to Zero問題**がエンタープライズ信頼性の構造的課題 [INFO-070](../Information/2026-04-22/collected-raw.md#INFO-070)
- **フロリダ州AG刑事調査**——FSU銃撃事件容疑者のChatGPT会話を根拠に殺人罪級の責任追及 [INFO-008](../Information/2026-04-24/collected-raw.md#INFO-008)
- GPT-5.5価格2倍が競合（Anthropic/Google/DeepSeek）に顧客を押しやるリスク [INFO-033](../Information/2026-04-29/collected-raw.md#INFO-033)
- 43%のAI生成コード変更が本番でデバッグ必要 [INFO-019](../Information/2026-04-19/collected-raw.md#INFO-019)
- Microsoft提携改訂で「排他性」を失い、Azureとの差別化が薄まる可能性

### 機会

- **Microsoft提携改訂**で全クラウド展開が可能に——エンタープライズ到達範囲の構造的拡大 [INFO-003](../Information/2026-04-29/collected-raw.md#INFO-003)
- **OpenAI on AWS**でAnthropicのAWS強みに対抗 [INFO-001](../Information/2026-04-29/collected-raw.md#INFO-001)
- Anthropic SCR指定の間隙を突く政府市場
- GSI 7社チャネルでエンタープライス営業力を借用
- GPT-5.4-Cyber、GPT-Rosalindという垂直特化2製品
- H2 2026 IPOが透明性と資金調達の新段階に
- METR約7ヶ月倍増期間——2026年末には1-2週間の自律稼働が可能になる可能性 [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)

### 脅威

- Anthropicのエンタープライズ猛追（40%シェア、$30B ARR確認、Google $40B投資）
- MCP標準化がOpenAI独自実行環境の囲い込みを無効化する可能性
- EU AI法全面執行（2026年8月）がコンプライアンスコストを増大
- **DeepSeek V4**が$0.0036/MTokで価格破壊——中間層の競争激化 [INFO-035](../Information/2026-04-29/collected-raw.md#INFO-035)
- **エンタープライズ実行ギャップ**: Cisco 85%パイロット/5%本番 [INFO-030](../Information/2026-04-29/collected-raw.md#INFO-030)、Microsoft「ほぼ本番で動いていない」[INFO-012](../Information/2026-04-29/collected-raw.md#INFO-012)
- フロリダ州AG刑事調査がAI企業責任の法的先例になる可能性

## I&W監視ポイント

この企業に関連するI&W指標の状況:

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | GPT-5.4 Pro ARC-AGI-2 83.3%、o3 87.5%。GPT-5.5でコンピューター使用拡張。90%閾値まで2.5pt |
| [IND-015](../config/indicators.json) スキル再定義 | elevated | rising | Agents SDK MCP統合。Symphony OSS。Codex 90+ plugins。Codex Labs + GSI 7社 |
| [IND-008](../config/indicators.json) 大企業の集中 | elevated | — | LLM支出27%。Anthropic 40%に劣後 |
| [IND-013](../config/indicators.json) セキュリティ侵害頻度 | high | rising | Codex desktop control新攻撃表面。97%企業インシデント予期。82%企業に未知AIエージェント [INFO-033](../Information/2026-04-29/collected-raw.md#INFO-033) |
| [IND-026](../config/indicators.json) エージェント本番環境到達率 | elevated | rising | Cisco 85%パイロット/5%本番（80pt gap）[INFO-030](../Information/2026-04-29/collected-raw.md#INFO-030)。S&P 25%のみROI証明 [INFO-031](../Information/2026-04-29/collected-raw.md#INFO-031)。Microsoft「ほぼ本番で動いていない」[INFO-012](../Information/2026-04-29/collected-raw.md#INFO-012) |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | high | rising | AAIF設立（Linux Foundation）[INFO-016](../Information/2026-04-29/collected-raw.md#INFO-016)。MCP 110M+/月DL。SKILL.md 5主要ツール対応。Symphony OSS |

## 変更履歴（直近5件のみ。詳細は git log を参照）

| 日付 | 変更内容 |
|------|---------|
| 2026-04-29 | **Microsoft提携改訂**（非排他・全クラウド・IP非排他2032）・**OpenAI on AWS**（GPT-5.5/Codex/Managed Agents on Bedrock）・**Symphony OSS**・エンタープライズ実行ギャップ5独立ソース確認を反映してエグゼクティブサマリー・基本情報・タイムライン・戦略方向性・SWOT・I&Wを書き直し。H-OAI-001 63→64%・H-OAI-002 56→55%に更新 |
| 2026-04-24 | GPT-5.5新モデルリリース・フロリダ州AG刑事調査・DeepSeek V3.2-Exp>Gemini 2.5 Proを反映して書き直し |
| 2026-04-23 | Workspace Agents新製品発表・30GW compute by 2030計画・Comment and Control脆弱性を反映して書き直し |
| 2026-04-22 | Codex Labs + GSI 7社提携・WAU 3M→4M・Agents SDK MCP統合・Reset to Zero問題を反映して書き直し |
| 2026-04-19 | GPT-Rosalind（ライフサイエンス特化）を新製品として追加 |
