# OpenAI

> 最終更新: 2026-05-06
> 確度: 中

$122B調達を完了し評価額$852Bに到達した [INFO-055](../Information/2026-05-06/collected-raw.md#INFO-055)。だが2026年の損失見込みは$14Bに膨らんでいる [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048)。収益は$13.1Bで黒字化未達、エンタープライズLLMシェア27%でAnthropic（40%）に劣後したまま。

2026年5月、OpenAIはエンタープライズ戦略をもう一段階深めた。**TPG/Brookfield/Advent/BainとJV「The Development Company」を設立**した [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)。評価額$10B、$4B調達。Anthropicも同週にBlackstone/H&F/Goldman SachsとJVを設立しており [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)、二社が同時にPalantir型のFDE（Forward-Deployed Engineer）モデルを採用した。エンタープライズAIのGo-to-Marketが「API提供」から「JV+埋め込みエンジニア」に構造的に深化している。

Microsoft提携は根本改訂済み。OpenAI製品はAzure優先リリースを維持しつつ全クラウドで提供可能、MicrosoftのIPライセンスは2032年まで非排他化された [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)。OpenAI on AWSでGPT-5.5・Codex・Managed AgentsがBedrockに載る [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)。単一クラウドのロックインから解放された。

## 基本情報

- **本社**: サンフランシスコ
- **CEO**: Sam Altman
- **主力製品**: ChatGPT、**GPT-5.5**（$5/$30、400K context・Thinking/Pro変種）、GPT-5.4シリーズ（Pro/mini/nano）、Agents SDK、**Codex**（desktop control・browser・memory・90+ plugins）、**Workspace Agents**（共有エージェント・Slack連携・定期タスク）、**Symphony**（OSSエージェントオーケストレーター）、Operator（CUA）、GPT-5.4-Cyber、GPT-Rosalind（ライフサイエンス特化）、ChatGPT Images 2.0
- **推定従業員数**: 4,000人（年末までに8,000人に倍増予定）
- **直近の資金調達**: $122B（評価額$852B）。SoftBank、Amazon（$50B）、Nvidia（$30B）、Microsoftが主要投資家

資金力はAI業界最大。年間収益$13.1B、月間収益$2B。ChatGPT週間アクティブユーザー9億人、5000万以上のサブスクライバー。H2 2026にIPOを検討中。

GPT-5.4 ProはARC-AGI-2で83.3%を記録し人間（72.4%）を超えた [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。BenchLM総合ではGPT-5.4 Proが92で、Claude Mythos Preview（99）・Gemini 3.1 Pro（93）に続く3位 [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。

Codex週間ユーザーは**400万+**に到達 [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)。Agents SDKにsandboxingとネイティブハーネスを追加、persisted /goalワークフローを導入 [INFO-004](../Information/2026-05-06/collected-raw.md#INFO-004)。Codexのbrowser use機能がコンピューター制御を実現 [INFO-022](../Information/2026-05-06/collected-raw.md#INFO-022)。

エンタープライズAI利用はYoY 8倍。**100万以上のビジネス顧客**。API処理は150億トークン/分。ただしLLM支出シェアは27%でAnthropic（40%）に劣後。

## 主要動向タイムライン

| 日付 | イベント | 信頼性 | 引用 |
|------|---------|-------|------|
| 2026-05-04 | **JV「The Development Company」設立**（TPG/Brookfield/Advent/Bain・$10B評価額・$4B調達・FDEモデル採用） | B-2 | [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) |
| 2026-04-28 | **OpenAI on AWS**発表（GPT-5.5/Codex/Managed Agents on Bedrock・Codex WAU 4M+） | A-3 | [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) |
| 2026-04-27 | **Microsoft提携改訂**（非排他・全クラウド・IP非排他2032） | A-3 | [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) |
| 2026-04-27 | **Symphony** OSS化（エージェントオーケストレーター） | A-3 | — |
| 2026-04-23 | **GPT-5.5発表**（$5/$30、400K context、Thinking/Pro変種） | A-1 | — |
| 2026-04-23 | **Workspace Agents**発表（共有エージェント・Slack連携・定期タスク） | A-3 | — |
| 2026-04-21 | **Codex Labs**発表 + **GSI 7社提携**（Accenture/PwC/Capgemini等） | A-3 | — |
| 2026-04-15 | Agents SDK大幅アップデート（ネイティブサンドボックス+MCP統合） | A-3 | [INFO-004](../Information/2026-05-06/collected-raw.md#INFO-004) |
| 2026-04-07 | $122B調達完了（評価額$852B） | A-3 | [INFO-055](../Information/2026-05-06/collected-raw.md#INFO-055) |

## 戦略方向性

### エンタープライス開発プラットフォームになる（H-OAI-001、確度63%）

Microsoft提携改訂で全クラウド展開が可能になり [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)、OpenAI on AWSでGPT-5.5・Codex・Managed AgentsがBedrockに載った [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)。Codex WAUは4M到達。JV「The Development Company」でエンタープライズ浸透を加速する構えだ [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)。

Codex Labs + GSI 7社提携でB2Bチャネルを開いた。Workspace Agentsでチーム向けワークフロー自動化に進出した。

だが$14B損失見込み [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) は収益構造の不安定化を示す。BenchLM 3位（92 vs Mythos 99） [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) は技術的優位の揺らぎを示唆する。C/I均衡。

確度は63% [Arbiter v3.70](../state/arbiter-2026-05-06.md)。

### MCP上に独自実行環境を構築して囲い込む（H-OAI-002、確度53%）

囲い込み仮説は3件の独立した反証に直面した。Symphony OSS、Microsoft IP非排他2032、AAIF/MCP標準化。JVのPEパートナーポートフォリオ企業への優先販売アクセスは围い込みの新次元（金融次元）として機能する可能性がある [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)。だが下層開放蓄積が上層囲い込み有効性を構造的に制約している。

確度は53% [Arbiter v3.70](../state/arbiter-2026-05-06.md)。

### AGI/スーパーインテリジェンス（H-OAI-003、確度1%、棄却候補）

Altmanは「2028年早期にASI」と公言するが、$122B調達、8,000人増員、Codex Labs、GSI提携、JV設立、政府契約拡大——経営行動はすべて商業化に向いている。確度1%で棄却候補。

## 強み・弱み・機会・脅威（SWOT）

### 強み

- 圧倒的な資金力（$122B、$852B評価額）
- 多層的なモデルラインナップ（GPT-5.5 + GPT-5.4 Pro/mini/nano + Cyber + Rosalind）
- GPT-5.4 ProでARC-AGI-2人間超え（83.3%）
- **100万ビジネス顧客・400万週間アクティブCodexユーザー** [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)
- ChatGPT週間アクティブユーザー9億人の消費者リーチ
- **3大クラウド全対応**: Azure優先+AWS Bedrock [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) + GCP
- **GSI 7社提携**でB2Bチャネル構築
- **JV「The Development Company」**でエンタープライズ特化を加速 [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)
- Agents SDK MCP統合 + sandboxing + persisted /goal [INFO-004](../Information/2026-05-06/collected-raw.md#INFO-004)

### 弱み

- 技術的優位が市場シェアに転換できていない——エンタープライズ27%でAnthropic（40%）に劣後
- **$14B損失見込み**で収益構造が不安定化 [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048)
- BenchLM 3位（92 vs Mythos 99 vs Gemini 93）で性能首位を失った [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)
- GPT-5.5価格2倍が競合に顧客を押しやるリスク
- 43%のAI生成コード変更が本番でデバッグ必要
- Microsoft提携改訂で「排他性」を失い、Azureとの差別化が薄まる

### 機会

- **JV「The Development Company」**でPEパートナーのポートフォリオ企業に優先アクセス [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)
- Microsoft提携改訂で全クラウド展開が可能に
- Anthropic SCR指定の間隙を突く政府市場
- GSI 7社チャネルでエンタープライズ営業力を借用
- GPT-5.4-Cyber、GPT-Rosalindという垂直特化2製品
- H2 2026 IPOが透明性と資金調達の新段階に
- Skills Marketplaceでエージェント配布の新チャネル [INFO-017](../Information/2026-05-06/collected-raw.md#INFO-017) [INFO-029](../Information/2026-05-06/collected-raw.md#INFO-029)

### 脅威

- Anthropicのエンタープライズ猛追（40%シェア、$30B ARR確認）
- MCP標準化が独自実行環境の围い込みを無効化する可能性
- EU AI法全面執行（2026年8月）がコンプライアンスコストを増大
- **DeepSeek V4**が$0.0036/MTokで価格破壊
- エンタープライズ実行ギャップ: Cisco 85%パイロット/5%本番、D&B 30%のみ本番スケール [INFO-034](../Information/2026-05-06/collected-raw.md#INFO-034) [INFO-035](../Information/2026-05-06/collected-raw.md#INFO-035)
- **AIコスト単月50%急増**の事例 [INFO-049](../Information/2026-05-06/collected-raw.md#INFO-049)

## I&W監視ポイント

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | GPT-5.4 Pro ARC-AGI-2 83.3%。BenchLM 3位（92）。90%閾値まで2.5pt |
| [IND-015](../config/indicators.json) スキル再定義 | elevated | rising | Agents SDK sandboxing。Skills Marketplace [INFO-017](../Information/2026-05-06/collected-raw.md#INFO-017)。Codex 90+ plugins |
| [IND-008](../config/indicators.json) 大企業の集中 | elevated | — | LLM支出27%。Anthropic 40%に劣後 |
| [IND-013](../config/indicators.json) セキュリティ侵害頻度 | high | rising | AIエージェント本番DB削除 [INFO-009](../Information/2026-05-06/collected-raw.md#INFO-009)。24.4%のみAI完全可視性 [INFO-036](../Information/2026-05-06/collected-raw.md#INFO-036) |
| [IND-026](../config/indicators.json) エージェント本番環境到達率 | elevated | rising | D&B 30%本番スケール [INFO-034](../Information/2026-05-06/collected-raw.md#INFO-034)。パイロット→本番18%（過去最大）[INFO-035](../Information/2026-05-06/collected-raw.md#INFO-035) |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | high | rising | MCP全社サポート（OpenAI/Google/Microsoft/Block）[INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015)。Red Hat MCP Gateway [INFO-016](../Information/2026-05-06/collected-raw.md#INFO-016) |

## 変更履歴（直近5件のみ。詳細は git log を参照）

| 日付 | 変更内容 |
|------|---------|
| 2026-05-06 | **鮮度タイムアウト対応（7日経過）**。JV「The Development Company」設立（TPG/Brookfield/$10B評価額・FDEモデル採用）・$14B損失見込み・Agents SDK sandboxing + persisted /goal・Codex browser use・Skills Marketplace・BenchLM 3位（92 vs Mythos 99）・MCP全社サポート・エンタープライズ実行ギャップ新データ（D&B 30%/パイロット→本番18%）を反映して全面書き直し。H-OAI-001 63%・H-OAI-002 53%に更新 |
| 2026-04-29 | Microsoft提携改訂・OpenAI on AWS・Symphony OSS・エンタープライズ実行ギャップ5独立ソース確認を反映して全面書き直し |
| 2026-04-24 | GPT-5.5新モデルリリース・フロリダ州AG刑事調査を反映して書き直し |
| 2026-04-23 | Workspace Agents新製品発表・30GW compute by 2030計画を反映して書き直し |
| 2026-04-22 | Codex Labs + GSI 7社提携・WAU 3M→4M・Agents SDK MCP統合を反映して書き直し |
