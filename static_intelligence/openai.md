# OpenAI インテリジェンス・プロファイル

> 最終更新: 2026-02-21
> 確度: 中

## エグゼクティブ・サマリー

OpenAIはエンタープライズAgent市場での展開を加速させている。エンタープライズAI利用がYoY 8倍成長、推論モデル利用が300倍増加。**[更新: 2026-02-21] OpenClaw買収（Peter Steinberger雇用）でクロスプラットフォームワークフローオーケストレーションを強化。Skills/Shell/Compactionで開発者環境の囲い込みを推進中。GPT-5.3-Codex-Spark（15倍高速生成、128kコンテキスト）をリリース。** Agents SDK v0.8.4でホスト型コンテナツールとSkills bundles追加。AGI優先戦略は棄却確定、商業化路線が確定的に。GPT-4o廃止に対する21,900件の署名は消費者市場の不満を示唆するが、0.1%利用率は移行妥当性を裏付ける。

## 基本情報

- 本社: 米国カリフォルニア州サンフランシスコ
- CEO: Sam Altman
- 主力製品: ChatGPT、GPT-5シリーズ、OpenAI Agents SDK、Frontier
- 推定従業員数: 非公開（急拡大中）
- 直近の資金調達: Microsoft他（詳細非公開）

## 戦略方向性

### 現在の主力仮説

**H-OAI-001: エンタープライズB2B展開加速戦略**（確度: 52%、~~51%~~ → **52%**）[更新: 2026-02-21]
OpenAIは2026年内にAgent機能を全面的にエンタープライズ向けに特化させ、B2B市場での展開を加速させる。**Frontier Platform開始・OpenClaw買収がB2B集中を支持（+1%）。** [INFO-013](../Information/2026-02-21/collected-raw.md#INFO-013) [INFO-015](../Information/2026-02-21/collected-raw.md#INFO-015)。「支配」の用語は過剰だが方向性は正しい（Arbiter判断）。

### 代替仮説

**H-OAI-002: 開発者エコシステム囲い込み**（確度: 52%）[更新: 2026-02-21]
OpenAIは開発者エコシステムの囲い込みを最優先し、プラットフォーム戦略でAgent市場を支配する。**Skills/Shell/Compactionは囲い込みの証拠だが、OpenClaw買収はオーケストレーション層での開放の可能性。囲い込み成功と失敗の双方の証拠が存在（±0%）。** [INFO-038](../Information/2026-02-21/collected-raw.md#INFO-038) [INFO-015](../Information/2026-02-21/collected-raw.md#INFO-015)。Arbiter判断。

**H-OAI-003: AGI優先戦略**（確度: 15%、~~棄却候補~~ → **棄却確定**）
~~OpenAIはAGI達成を最優先とし、商業化よりも研究開発に資源を集中する~~。5件の商業化証拠により棄却確定 [INFO-014](../Information/2026-02-19/collected-raw.md#INFO-014) [INFO-015](../Information/2026-02-19/collected-raw.md#INFO-015) [INFO-016](../Information/2026-02-19/collected-raw.md#INFO-016) [INFO-004](../Information/2026-02-19/collected-raw.md#INFO-004) [INFO-051](../Information/2026-02-19/collected-raw.md#INFO-051)。[更新: 2026-02-19] Arbiter判断でrejected確定。

## 主要動向タイムライン

| 日付 | イベント | 信頼性 | 引用 |
|------|---------|-------|------|
| 2026-02-21 | OpenClaw買収、Peter Steinberger雇用（ワークフローオーケストレーション強化） | B-3 | [INFO-015](../Information/2026-02-21/collected-raw.md#INFO-015) |
| 2026-02-21 | GPT-5.3-Codex-Spark、15倍高速生成、128kコンテキスト | A-3 | [INFO-032](../Information/2026-02-21/collected-raw.md#INFO-032) |
| 2026-02-21 | Agents SDK v0.8.4、ホスト型コンテナツールとSkills bundles追加 | B-3 | [INFO-005](../Information/2026-02-21/collected-raw.md#INFO-005) |
| 2026-02-21 | Codexマルチエージェントワークフロー（専門エージェント並列起動） | A-3 | [INFO-031](../Information/2026-02-21/collected-raw.md#INFO-031) |
| 2026-02-19 | Codexスキル評価ガイド（Evals活用）公開 | A-3 | [INFO-001](../Information/2026-02-20/collected-raw.md#INFO-001) |
| 2026-02-19 | The Alignment Projectに$7.5M助成金提供 | A-3 | [INFO-021](../Information/2026-02-20/collected-raw.md#INFO-021) |
| 2026-02-05 | Frontierプラットフォーム開始、HP/Intuit/Oracle/Uber採用 | A-3 | [INFO-013](../Information/2026-02-21/collected-raw.md#INFO-013) |
| 2026-02-17 | エンタープライズAI利用8倍成長、推論モデル300倍増 | B-3 | [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020) |
| 2026-02-13 | GPT-4o、GPT-4.1シリーズ、o4-miniをChatGPTから廃止 | A-3 | [INFO-008](../Information/2026-02-18/collected-raw.md#INFO-008) |
| 2026-02-12 | OpenAIエンジニアの95%がCodex使用、10-20並列エージェント管理 | C-3 | [INFO-013](../Information/2026-02-18/collected-raw.md#INFO-013) |

[更新: 2026-02-21] OpenClaw買収、GPT-5.3-Codex-Spark、Agents SDK v0.8.4、マルチエージェントワークフロー追加

**重要なAPI変更・新機能:** [更新: 2026-02-21]
- **OpenClaw買収**: クロスプラットフォームワークフローオーケストレーション強化 [INFO-015](../Information/2026-02-21/collected-raw.md#INFO-015)
- **Skills/Shell/Compaction**: エージェントプリミティブで開発者環境囲い込み [INFO-038](../Information/2026-02-21/collected-raw.md#INFO-038)
- **Assistants API 8月廃止予定**: Responses APIへ移行 [INFO-019](../Information/2026-02-20/collected-raw.md#INFO-019)
- **CrewAI 10万人以上認定デベロッパー**: LangGraph比5.76x高速実行を主張 [INFO-019](../Information/2026-02-20/collected-raw.md#INFO-019)

## 強み・弱み・機会・脅威（SWOT）

### 強み
- エンタープライズ市場での先発優位（YoY 8倍成長）
- Microsoft提携による企業ルート確保
- 推論モデル利用300倍増による技術的リーダーシップ
- 自社エンジニアの95%がCodex使用（内部dogfooding成功）

### 弱み
- GPT-4o廃止に対する消費者不満（21,900件署名）
- API互換性の維持プレッシャー（Enterprise延長措置）
- Claude/MCP標準化動きへの対抗策不明確

[更新: 2026-02-18]
- 高努力設定でDeep Research精度低下の指摘（低努力0.496→高努力0.481、コスト55%増） [INFO-083](../Information/2026-02-18/collected-raw.md#INFO-083)
- Gemini 3 Deep ThinkにARC-AGI-2で劣位 [INFO-082](../Information/2026-02-18/collected-raw.md#INFO-082)

[更新: 2026-02-20]
- **Gemini 3.1 ProがArtificial Analysis指数で4ptリード、技術優位性が揺らぐ可能性** [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028)
- **Assistants API廃止による開発者混乱リスク** [INFO-019](../Information/2026-02-20/collected-raw.md#INFO-019)

### 機会
- ServiceNow等とのエンタープライズ統合拡大
- Frontierプラットフォームでの垂直統合
- 推論モデル価格プレミアムでの収益最大化

### 脅威
- Anthropic MCP標準化によるエコシステム囲み込み
- ByteDance Seed 2.0のコスト競争（約1桁低価格）
- Claude Opus 4.6のエージェント性能優位

## I&W監視ポイント

| 指標 | ステータス | 傾向 | 現在値 |
|------|-----------|------|--------|
| IND-008 大手契約集中 | elevated | rising | Uber/Thermo Fisher/Intuit等がFrontier採用 |
| IND-009 AI投資持続増大 | elevated | rising | 組織平均AI支出$1.2M、前年比108%増 |

## 変更履歴

| 日付 | 変更内容 | 根拠 |
|------|---------|------|
| 2026-02-21 | H-OAI-001確度51%→52%、H-OAI-002確度52%（±0%） | Arbiter判断（OpenClaw買収、囲い込み成功/失敗双方の証拠） |
| 2026-02-21 | タイムラインにOpenClaw/GPT-5.3-Codex-Spark/SDK v0.8.4/マルチエージェント追加 | INFO-005, INFO-015, INFO-031, INFO-032 |
| 2026-02-21 | API変更セクションにSkills/Shell/Compaction追加 | INFO-038 |
| 2026-02-20 | H-OAI-001確度49%→51%、H-OAI-002確度50%→52% | Arbiter判断（Frontier Platform開始、Assistants API廃止） |
| 2026-02-20 | タイムラインにFrontier/Codex/$7.5M助成金/Assistants API廃止追加 | INFO-001, INFO-013, INFO-019, INFO-021 |
| 2026-02-20 | 弱みにGemini 3.1 Pro技術優位リスク追加 | INFO-028 |
| 2026-02-19 | H-OAI-001確度53%→49%、用語「B2B市場支配」→「B2B展開加速」に修正 | Arbiter判断（「支配」用語不当、Red指摘妥当） |
| 2026-02-19 | H-OAI-003棄却確定、確度20%→15% | Arbiter判断（5件商業化証拠） |
| 2026-02-18 | 高努力設定での精度低下指摘追加 | INFO-083 |
| 2026-02-18 | Gemini 3 Deep Think劣位追加 | INFO-082 |
| 2026-02-18 | 初版作成 | Arbiter判断に基づく統合分析 |
