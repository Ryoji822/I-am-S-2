# AI市場の現在地

> 最終更新: 2026-03-09

**2026年3月時点で、AI市場は「技術はオープンになるが、性能トップは一握り」という方向に向かっている（SCN-002「技術は開くが勝者は出る」42%が最有力）。GPT-5.4 ProがARC-AGI-2で83.3%を達成し初めて人間（72.4%）を超過 [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)——フロンティア格差拡大を決定的に裏付けた。資金集中はさらに加速し上位3社合計$195.1B（OpenAI $110B + Anthropic $69.1B + Waymo $16B）がVC投資の83%超を占める可能性 [INFO-009](../Information/2026-03-08/collected-raw.md#INFO-009)。Claude Codeが開発者愛用率46%で首位 [INFO-013](../Information/2026-03-08/collected-raw.md#INFO-013)。ROI正報告はわずか6%で、採用加速（71%企業がQ4 2026本番運用予定）との79pt乖離が未解決。**

**【重要な構造変化: 政府介入の質的変化】** 2026-02-27、Trump政権がAnthropicをSCR指定し連邦使用を禁止——従来の「規制」フレームを超え、安全性堅持企業への経済的報復→順応企業への利益という「インセンティブ構造の歪み」が顕在化 ([IND-023](../config/indicators.json), **high**昇格)。同日夜にOpenAIがDoW契約を締結し「漁夫の利」構造が成立 ([H-GOV-001](../config/hypotheses.json), 確度55%)。**

## プレイヤー一覧

| 企業 | 主力 | 資金 | 一言で |
|------|------|------|--------|
| OpenAI | GPT-5.4シリーズ、Frontier Platform | $110B調達（$730B評価額、$25B ARR） | ARC-AGI-2 83.3%で人間超え・ベンチマーク首位奪還。DoW契約で政府市場参入。エンタープライズLLMシェア27%に後退 |
| Anthropic | Claude 4.6シリーズ、Claude Code | $30B調達（$380B評価額、$14B ARR） | エンタープライズ LLM支出40%で首位。Claude Code愛用率46% [INFO-013](../Information/2026-03-08/collected-raw.md#INFO-013) |
| Google | Gemini 3.1シリーズ、Vertex AI | 自己資金 | ARC-AGI-2 77.1%で2位に後退。ADK 25+パートナー。Workspace CLI MCP統合 |
| xAI | Grok 3/4シリーズ | SpaceX子会社（$1.25兆合算） | 物理世界AI。Tesla車両統合済み。API $0.20-$3/Mで業界最安水準 |
| ByteDance | Seed 2.0、Doubao、Seedance 2.0 | 非公開（評価額$520B） | 価格1/10で攻める。豆包DAU 1.03億でグローバルMAU 2位 [INFO-042](../Information/2026-03-08/collected-raw.md#INFO-042) |

OpenAI・Anthropic・Googleの3社がフロンティアを形成し、xAIとByteDanceがそれぞれ異なる角度から挑んでいる。詳細は各社のファイルを参照。

## 今、市場で何が起きているか

### 1. ARC-AGI-2で人間超えが実現

GPT-5.4 ProがARC-AGI-2で83.3%を達成し、人間ベースライン（72.4%）を初めて超過 [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。AGI転換点指標（[IND-001](../config/indicators.json)）の90%閾値まで6.7pt。Gemini 3.1 Proは77.1%で6.2pt差の2位。**フロンティア性能格差は拡大方向**であり、SCN-002（開放×格差拡大、42%）を強く支持。ただしARC-AGI-2は抽象推論特化の単一ベンチマークであり、過学習リスク・他ベンチマークでの確認が必要（確度: 中）。

### 2. エンタープライズAgent市場が爆発的に伸びている

企業のAIエージェント導入が急加速している。エンタープライズAI利用はYoY 8倍成長し、推論モデルの利用は300倍に増えた [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020)。71%の企業がQ4 2026までに複数AIエージェント本番運用予定 [INFO-010](../Information/2026-03-08/collected-raw.md#INFO-010)。Anthropicがエンタープライズ LLM支出40%でOpenAI（27%）を逆転し首位（Menlo Ventures調査）。Claude Codeが開発者愛用率46%で首位（Pragmatic Engineer調査） [INFO-013](../Information/2026-03-08/collected-raw.md#INFO-013)。

**しかし「使い始めた」と「成果が出ている」は全く別の話。** ROI正報告はわずか6%、ROI測定可能は10.5%のみ [INFO-023](../Information/2026-03-08/collected-raw.md#INFO-023)。採用率71%との79pt乖離が継続。Gartner予測では40%のエージェントAIプロジェクトが2027年末までにキャンセルされる。Klarna/DuolingoがAI置換を撤回 [INFO-056](../Information/2026-03-08/collected-raw.md#INFO-056) した事実もAI実効性への疑問を示唆。

### 3. 資金が上位企業に集中し臨界点に接近

OpenAIが$110B（$730B評価額、$25B ARR） [INFO-009](../Information/2026-03-08/collected-raw.md#INFO-009)、Anthropicが$30B（$380B評価額）。上位3社合計$195.1BがVC投資総額の83%超を占める可能性。[IND-003](../config/indicators.json) はhigh approachingだが、**分母（VC投資総額$189B）の定義が不明確**で、critical（80%）判定には再計算が前提。

### 4. 価格が年10倍のペースで下がっている

GPT-4相当の品質が3年前$60/Mだったのが今$0.75/M、98%削減 [INFO-036](../Information/2026-02-18/collected-raw.md#INFO-036)。具体的には、Anthropic Opus 4.6が67%値下げで$5/$25 [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)、Gemini $1.6/M [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090)、xAI Grok 4.1 Fast $0.20/M、ByteDance Seed 2.0 Pro $0.47/M。

### 5. プロトコル標準化は決着し、競争は上位レイヤーへ

プロトコル層の標準化戦争は2025年12月のAAIF（Agentic AI Foundation、Linux Foundation傘下）設立で実質終結した。MCP SDK月間9700万ダウンロード、10,000+サーバー公開。

**競争の焦点は上位レイヤーに移行:**
- **実行環境層**: OpenAI Shell（クラウド依存、囲い込み方向）vs Anthropic Claude Code（ローカル実行可、開放方向）vs E2B/Modal（独立）
- **オーケストレーション層**: LangGraph vs CrewAI vs Microsoft Agent Framework（AutoGen+Semantic Kernel統合）
- **ガバナンス層**: EU AI法2026年8月完全施行が規制面での競争を形作る

セキュリティ面ではMCP実装の43%にコマンドインジェクション脆弱性（Equixly調査）。Claude Codeのサンドボックス脱出脆弱性も報告 [INFO-031](../Information/2026-03-08/collected-raw.md#INFO-031)。

### 6. セキュリティ・規制・データ主権が追いついていない

58%の企業がAIを業務に統合しているのにガバナンスの枠組みを持つのは19% [INFO-026](../Information/2026-02-18/collected-raw.md#INFO-026)。EU AI法は2026年8月に完全施行（罰則: 最大€3500万または売上7%）。Gartner予測では2027年までに35%の国が地域固有AIプラットフォームにロックイン。

### 7. オープンソースが追い上げている

OSSのAIモデルが商用モデルとの性能差を急速に縮めている。Llama 4 85.5%、GLM-5がOSSトップ [INFO-099](../Information/2026-02-21/collected-raw.md#INFO-099)。ただしARC-AGI-2 83.3%のようなフロンティア性能はまだOSSでは実現できていない。商用最上位の90%性能到達閾値（[IND-004](../config/indicators.json)）も未達。

## どこが不確実か

市場は「寡占に向かう力」と「分散に向かう力」の両方が同時に働いている。

**寡占に向かう力:** $195B+が上位企業に集中、エンタープライズ3社で88%シェア、実行環境の囲い込み（[IND-015](../config/indicators.json)）、規制コストが参入障壁に、政府の特定企業優遇（SCR指定・DoW契約）。

**分散に向かう力:** AAIF標準化完了、ByteDance Seed 2.0の価格破壊、OSSの性能追い上げ、EU規制によるデータ主権、Workspace CLI MCP統合のような開放的動き。

現時点の判断は**「開放×格差拡大」（SCN-002, 42%）が最も確からしい**。プロトコルは標準化されたが、トップ性能は一部企業に集中する構造。GPT-5.4 Proの人間超えがこの方向を決定的に支持。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | ベンチマークで前世代比30%超の性能向上 | GPT-5.4 Pro ARC-AGI-2 83.3%で人間超え。90%閾値まで6.7pt | **high approaching** |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | 上位3社$195.1B。分母再計算でcritical到達の可能性 | **high approaching** |
| [IND-004](../config/indicators.json) OSS性能到達 | OSSが商用モデルの90%性能に達するか | Llama 4 85.5%、GLM5トップ。90%閾値は未達 | elevated |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | プロトコル層決着後の実行環境・オーケストレーション競争 | AAIF標準化完了。Shell vs Claude Code vs 独立の三つ巴 | elevated |
| [IND-008](../config/indicators.json) 大企業の集中 | Fortune 500のAI導入先が2-3社に集中するか | Anthropic 40%、OpenAI 27%、Google 21%（合計88%） | elevated |
| [IND-011](../config/indicators.json) 性能収斂 | Tier 1各社のスコア差が5%以内に縮まるか | GPT-5.4 Pro 83.3% vs Gemini 3.1 Pro 77.1%で格差拡大 | mixed |
| [IND-015](../config/indicators.json) 実行環境の囲い込み | 実行環境・スキル形式がベンダー固有か標準か | 3社のスキル形式は相互非互換。Assistants API 8月廃止 | elevated |
| [IND-018](../config/indicators.json) AGI兆候 | AGI到達を示す複合的な兆候 | ARC-AGI-2 83.3%で人間超え。90%閾値まで6.7pt。CEO発言ラッシュ | elevated approaching |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理能力にシフト | Claude Code愛用率46%首位。ジュニア採用73%減 | **high** |
| [IND-023](../config/indicators.json) 政府によるAI強制力行使 | 経済的手段でAI企業の安全性姿勢を抑圧する構造的リスク | SCR指定・連邦使用禁止・OpenAI同日DoW契約で条件1・2達成 | **high** |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-03-09 | GPT-5.4 Pro人間超え（ARC-AGI-2 83.3%）を反映。OpenAI $110B/$730B/$25B ARR更新。Claude Code愛用率46%追加。SCN-002 42%に更新。資金集中$195.1B・IND-001/003 high approaching。ROI 79pt乖離の継続を追記 |
| 2026-03-01 | IND-023 high昇格と政府介入の質的変化（規制→選別的報復）を追記。資金集中$140B、OECDデータで分母改善を反映 |
| 2026-02-23 | 初版作成（AAIF設立後の市場構造再定義）
