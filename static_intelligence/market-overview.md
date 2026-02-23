# AI市場の現在地

> 最終更新: 2026-02-23

**2026年2月時点で、AI市場は「技術はオープンになるが、性能トップは一握り」という方向に向かっている（SCN-002「技術は開くが勝者は出る」33%が最有力）。プロトコル層の標準化戦争は2025年12月のAAIF設立で実質終結し、MCP+A2AがLinux Foundation傘下の業界標準になった。競争の焦点は実行環境・データ・ガバナンスの上位レイヤーに移行。Anthropicがエンタープライズ LLM支出40%で首位に立ち、OpenAI 27%に逆転。$1300億+が上位2社に集中（OpenAI $100B+、Anthropic $30B）。価格は年10倍ペースで下落中だが、Gemini 3.1 ProのARC-AGI-2 77.1%のようなフロンティア性能は一部企業に集中。ROIを出せているのはわずか5%。**

## プレイヤー一覧

| 企業 | 主力 | 資金 | 一言で |
|------|------|------|--------|
| OpenAI | GPT-5シリーズ、Frontier Platform | $100B+調達（$850B+評価額） | Skills/Shellで実行環境囲い込み。エンタープライズLLMシェア27%に後退 |
| Anthropic | Claude 4.6シリーズ、Claude Code | $30B調達（$380B評価額、$14B ARR） | エンタープライズ LLM支出40%で首位。Claude Code $2.5B ARR |
| Google | Gemini 3シリーズ、Vertex AI | 自己資金 | ベンチマーク首位。統合戦略は訴訟・幻覚率・移行延期の逆風 |
| xAI | Grok 3/4シリーズ | SpaceX子会社（$1.25兆合算） | 物理世界AI。Tesla車両統合済み。API $0.20-$3/Mで業界最安水準 |
| ByteDance | Seed 2.0、Doubao、Seedance 2.0 | 非公開 | 価格1/10で攻める。Doubao DAU 1億超。品質の独立検証は未完了 |

OpenAI・Anthropic・Googleの3社がフロンティアを形成し、xAIとByteDanceがそれぞれ異なる角度から挑んでいる。詳細は各社のファイルを参照。

## 今、市場で何が起きているか

### 1. エンタープライズAgent市場が爆発的に伸びている

企業のAIエージェント導入が急加速している。エンタープライズAI利用はYoY 8倍成長し、推論モデルの利用は300倍に増えた [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020)。Fortune 500の80%以上がエージェントを構築済み [INFO-070](../Information/2026-02-18/collected-raw.md#INFO-070)。Anthropicがエンタープライズ LLM支出40%でOpenAI（27%）を逆転し首位（Menlo Ventures調査）。

**しかし「使い始めた」と「成果が出ている」は全く別の話。** 本格的なリターンを出せているのはわずか5% [INFO-047](../Information/2026-02-19/collected-raw.md#INFO-047)。Gartner予測では40%のエージェントAIプロジェクトが2027年末までにキャンセルされる。「転換点に接近中だが未到達」の段階。

### 2. 資金が上位2社に集中している

OpenAIが$100B+（Amazon $50B、SoftBank $30B、NVIDIA $20B参加、$850B+評価額）、Anthropicが$30B（GIC/Coatue主導、$380B評価額）。合計$1300億+がこの2社に集中。[IND-003](../config/indicators.json) はhighだが、**資金調達と市場支配は同じではない**。

### 3. 価格が年10倍のペースで下がっている

GPT-4相当の品質が3年前$60/Mだったのが今$0.75/M、98%削減 [INFO-036](../Information/2026-02-18/collected-raw.md#INFO-036)。具体的には、Anthropic Opus 4.6が67%値下げで$5/$25 [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)、Gemini $1.6/M [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090)、xAI Grok 4.1 Fast $0.20/M（旧報告$30/Mは誤り、訂正済み）、ByteDance Seed 2.0 Pro $0.47/M。

### 4. プロトコル標準化は決着し、競争は上位レイヤーへ

**v2.0の最大の構造変化。** プロトコル層の標準化戦争は2025年12月のAAIF（Agentic AI Foundation、Linux Foundation傘下）設立で実質終結した。Anthropic（MCP）、Google（A2A）、OpenAI（AGENTS.md）、Block（goose）が共同で創設。Platinum会員にAmazon、Bloomberg、Cloudflare、Microsoftも参加。MCP SDK月間9700万ダウンロード、10,000+サーバー公開。

**競争の焦点は上位レイヤーに移行:**
- **実行環境層**: OpenAI Shell（クラウド依存、囲い込み方向）vs Anthropic Claude Code（ローカル実行可、開放方向）vs E2B/Modal（独立）
- **オーケストレーション層**: LangGraph vs CrewAI vs Microsoft Agent Framework（AutoGen+Semantic Kernel統合）
- **ガバナンス層**: EU AI法2026年8月完全施行が規制面での競争を形作る

セキュリティ面ではMCP実装の43%にコマンドインジェクション脆弱性（Equixly調査）。OpenClaw ClawHubで341の悪意あるスキル検出（12%汚染率）。標準が広がるほどセキュリティリスクも拡大。

### 5. セキュリティ・規制・データ主権が追いついていない

58%の企業がAIを業務に統合しているのにガバナンスの枠組みを持つのは19% [INFO-026](../Information/2026-02-18/collected-raw.md#INFO-026)。EU AI法は2026年8月に完全施行（罰則: 最大€3500万または売上7%）。Gartner予測では2027年までに35%の国が地域固有AIプラットフォームにロックイン（現在5%）。Thele v. Google LLC集団訴訟（Gemini Gmail無断統合）は規制リスクの具体例。[IND-023](../config/indicators.json) を新設。

### 6. オープンソースが追い上げている

OSSのAIモデルが商用モデルとの性能差を急速に縮めている。Llama 4 85.5%、GLM-5がOSSトップ [INFO-099](../Information/2026-02-21/collected-raw.md#INFO-099)。ただしARC-AGI-2 77.1%のような突出した性能はまだOSSでは実現できていない。商用最上位の90%性能到達閾値（[IND-004](../config/indicators.json)）も未達。

## どこが不確実か

市場は「寡占に向かう力」と「分散に向かう力」の両方が同時に働いている。

**寡占に向かう力:** $1300億+が2社に集中、エンタープライズ3社で88%シェア、実行環境の囲い込み（[IND-015](../config/indicators.json)）、規制コストが参入障壁に。

**分散に向かう力:** AAIF標準化完了、ByteDance Seed 2.0の価格破壊、OSSの性能追い上げ、EU規制によるデータ主権。

現時点の判断は**「開放×格差拡大」（SCN-002, 33%）が最も確からしい**。プロトコルは標準化されたが、トップ性能は一部企業に集中する構造。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | ベンチマークで前世代比30%超の性能向上 | Gemini 3.1 Pro ARC-AGI-2 77.1%（146%向上） | **high** |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | $1300億+が2社に集中。ただし資金≠市場構造変化 | **high** |
| [IND-004](../config/indicators.json) OSS性能到達 | OSSが商用モデルの90%性能に達するか | Llama 4 85.5%、GLM5トップ。90%閾値は未達 | elevated |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | プロトコル層決着後の実行環境・オーケストレーション競争 | AAIF標準化完了。Shell vs Claude Code vs 独立の三つ巴 | elevated |
| [IND-008](../config/indicators.json) 大企業の集中 | Fortune 500のAI導入先が2-3社に集中するか | Anthropic 40%、OpenAI 27%、Google 21%（合計88%） | elevated |
| [IND-011](../config/indicators.json) 性能収斂 | Tier 1各社のスコア差が5%以内に縮まるか | Seed 2.0がフロンティア追い上げ。ただし自己報告値 | elevated |
| [IND-015](../config/indicators.json) 実行環境の囲い込み | 実行環境・スキル形式がベンダー固有か標準か | 3社のスキル形式は相互非互換。Assistants API 8月廃止 | elevated |
| [IND-018](../config/indicators.json) AGI兆候 | AGI到達を示す複合的な兆候 | ARC-AGI-2 77.1%。Altman「2年以内にスーパーインテリジェンス」 | elevated |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理能力にシフト | 82%がAIツール使用。エントリー技術職73.4%減 | **high** |
| [IND-023](../config/indicators.json) 規制・データ主権 | EU AI法・反トラスト・データ主権の市場構造影響 | EU AI法8月施行、Google訴訟、35%の国がロックイン予測 | elevated |
