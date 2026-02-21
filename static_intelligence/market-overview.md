# AI市場の現在地

> 最終更新: 2026-02-21

**2026年2月時点で、AI市場は「技術はオープンになるが、性能トップは一握り」という方向に向かっている（SCN-002「技術は開くが勝者は出る」32%が最有力）。MCPのようなオープン標準が広がる一方、Gemini 3.1 ProがARC-AGI-2で77.1%を記録し性能面で頭一つ抜けた。つまり「安いAIは誰でも使える。しかし最高のAIは一部の企業しか作れない」という構造が浮かび上がっている。$1300億がOpenAI・Anthropicの2社に集中し、AIの価格は年10倍のペースで下落中。エンタープライズ市場は爆発的に伸びているが、実際にROIを出せているのはわずか5%で、残り95%はパイロット段階で停滞している。**

## プレイヤー一覧

AI市場には、モデルとプラットフォームの両方を持つ大手（Tier 1）と、特定の強みで挑む挑戦者がいる。

| 企業 | 主力 | 資金 | 一言で |
|------|------|------|--------|
| OpenAI | GPT-5シリーズ、Frontier Platform | $1000億調達 | AGIから大企業向けに転身。開発者囲い込みも進行中 |
| Anthropic | Claude 4.6シリーズ、MCP | $300億調達（年収$14B） | 安全性でエンタープライズを取る。MCPで業界標準を狙う |
| Google | Gemini 3シリーズ、Vertex AI | 自己資金（外部調達不要） | ベンチマーク首位。全プロダクトにAIを溶かし込む横断戦略 |
| xAI | Grok 3シリーズ | $20B調達 | SpaceX買収で物理世界を狙うが、製品統合はまだゼロ |
| ByteDance | Seed 2.0、Doubao | 非公開 | 価格1/10で攻める挑戦者。品質の第三者検証は未完了 |

OpenAI・Anthropic・Googleの3社がフロンティアを形成し、xAIとByteDanceがそれぞれ異なる角度から挑んでいる。詳細は各社のファイルを参照。

## 今、市場で何が起きているか

### 1. エンタープライズAgent市場が爆発的に伸びている

企業のAIエージェント導入が急加速している。エンタープライズAI利用はYoY 8倍成長し、推論モデルの利用は300倍に増えた [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020)。組織あたりのAI支出は平均$1.2Mで前年比108%増 [INFO-037](../Information/2026-02-18/collected-raw.md#INFO-037)。Fortune 500の80%以上がローコード/ノーコードツールでエージェントを構築済み [INFO-070](../Information/2026-02-18/collected-raw.md#INFO-070)。営業チームの87%がAIを使い、54%はエージェントを実戦投入している [INFO-072](../Information/2026-02-18/collected-raw.md#INFO-072)。全企業が2026年にAIエージェント採用拡大を計画している [INFO-069](../Information/2026-02-18/collected-raw.md#INFO-069)。

**しかし「使い始めた」と「成果が出ている」は全く別の話。** HBR調査では74%が1年以内のROI達成を報告しているが [INFO-023](../Information/2026-02-18/collected-raw.md#INFO-023)、本格的なリターンを出せているのはわずか5%。残り95%はパイロット段階から先に進めていない [INFO-047](../Information/2026-02-19/collected-raw.md#INFO-047)。Snowflake 6,000ユーザー展開（5x ROI、92% NPS）[INFO-014](../Information/2026-02-20/collected-raw.md#INFO-014) のような成功例はあるが例外的。100%が拡大計画→74%が優先→5%が成功。この数字の乖離に注目すべきで、エンタープライズAIはまだ「転換点に接近中だが未到達」の段階にある。

### 2. 資金が2社に集中している

OpenAIが$1000億（NVIDIA $300億、Amazon、SoftBank、Microsoft参加）[INFO-102](../Information/2026-02-21/collected-raw.md#INFO-102)、Anthropicが$300億（GIC/Coatue主導）[INFO-015](../Information/2026-02-18/collected-raw.md#INFO-015)。合計$1300億がこの2社に集中している。これだけ見ると寡占化のシグナルに見えるが、**資金調達と市場支配は同じではない**。SoftBank Vision FundがWeWork等に巨額投資して失敗した前例がある。お金が集まったことは投資家が賭けたという意味であって、市場を取ったという意味ではない。[IND-003](../config/indicators.json)はhighだが、critical昇格はこの理由で却下されている。

### 3. 価格が年10倍のペースで下がっている

AIの利用コストは劇的に下がり続けている。GPT-4相当の品質が3年前$60/Mだったのが今$0.75/M、98%削減 [INFO-036](../Information/2026-02-18/collected-raw.md#INFO-036)。同等品質での価格は年間約10倍のペースで下落中 [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)。

具体的には、Claude Opus 4.6が$15/$75→$5/$25に67%値下げ [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)、Geminiが$1.6/Mという業界最安水準 [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090)、ByteDance Seed 2.0がTier 1の約1/10を主張 [INFO-017](../Information/2026-02-18/collected-raw.md#INFO-017)。ハードウェア面でもNVIDIA Blackwellが最大10倍のコスト削減を実現し [INFO-078](../Information/2026-02-18/collected-raw.md#INFO-078)、推論コスト自体が年間5-10倍で下がっている [INFO-080](../Information/2026-02-18/collected-raw.md#INFO-080)。

この価格下落には矛盾がある。価格が下がれば誰でもAIを使える（収斂方向）はずだが、Gemini 3.1 Proの性能突出は格差拡大を示す。「安いAIは誰でも手に入る。しかし最高のAIは一部の企業しか提供できない」状態が生まれつつある。

### 4. 標準化をめぐる争いが始まっている

AIエージェントが他のツールやサービスと接続するための標準プロトコルをめぐる争いが始まった。AnthropicのMCP（Model Context Protocol）がリード中で、OWASP、Cloudflare、Demandbase [INFO-029](../Information/2026-02-18/collected-raw.md#INFO-029) [INFO-030](../Information/2026-02-18/collected-raw.md#INFO-030) [INFO-032](../Information/2026-02-18/collected-raw.md#INFO-032)、Chrome、Oracle [INFO-024](../Information/2026-02-21/collected-raw.md#INFO-024) [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035) が対応。Linux Foundation AAIFへの寄贈も完了し10,000以上のサーバーが公開されている。

一方でOpenAIはSkills/Shell/Compactionという独自の仕組みを推進 [INFO-038](../Information/2026-02-21/collected-raw.md#INFO-038)、GoogleもGemini Interactionsを持つ。現在3つ以上の標準が共存中（[IND-006](../config/indicators.json), elevated）。ここが「開放」に収まるか「各社バラバラの囲い込み」になるかで、シナリオの方向が大きく変わる。

注意すべきは「対応した」と「実際に業務で使っている」は違うということ。MCPの対応企業数は増えているが、実際の採用率の定量データはまだない。またCloudflareが「Shadow MCP」（非公式・未検証のMCPサーバー）のセキュリティリスクを警告しており [INFO-032](../Information/2026-02-18/collected-raw.md#INFO-032)、標準が広がるほどセキュリティの穴も広がる問題がある。

### 5. セキュリティとガバナンスが追いついていない

AIを導入する企業は増えているが、管理体制が追いついていない。58%の企業がAIを業務に統合しているのに、ガバナンスの枠組みを持っているのはわずか19% [INFO-026](../Information/2026-02-18/collected-raw.md#INFO-026)。過剰な権限を与えられたAIエージェントではセキュリティ事故の発生率が4.5倍になる [INFO-027](../Information/2026-02-18/collected-raw.md#INFO-027)。

規制は3地域で異なるアプローチ。EUはAI法を2026年8月に完全施行し高リスクAIに厳格な義務を課す [INFO-073](../Information/2026-02-18/collected-raw.md#INFO-073)。米国は大統領令14365で統一国家基準の確立を目指す [INFO-074](../Information/2026-02-18/collected-raw.md#INFO-074)。中国はEU型包括法を持たず市場主導型 [INFO-075](../Information/2026-02-18/collected-raw.md#INFO-075)。EU AI法施行は安全性を武器にするAnthropicに追い風、規制コストが高い新興企業には参入障壁になる。

### 6. オープンソースが追い上げている

OSSのAIモデルが商用モデルとの性能差を急速に縮めている。定型的なユースケースではOSSが商用モデルと同等の性能を発揮できるようになった [INFO-086](../Information/2026-02-18/collected-raw.md#INFO-086)。Llama 4が85.5%、GLM-5がオープンソースLLMのトップ [INFO-099](../Information/2026-02-21/collected-raw.md#INFO-099) [INFO-084](../Information/2026-02-18/collected-raw.md#INFO-084)。GitHub Copilotは2,000万人到達でコーディングAIの民主化が進んでいる [INFO-025](../Information/2026-02-20/collected-raw.md#INFO-025)。

ただしGemini 3.1 ProのARC-AGI-2 77.1%のような突出した性能はまだOSSでは実現できていない。商用最上位の90%性能到達の閾値（[IND-004](../config/indicators.json)）も未達成。「普通の用途なら十分」だが「最先端が必要なら商用モデルが必要」という状況は変わっていない。

## どこが不確実か

市場は「寡占に向かう力」と「分散に向かう力」の両方が同時に働いている。

**寡占に向かう力:** $1300億が2社に集中、大企業契約がTier 1に集まる傾向、規模の経済で後発の参入障壁が上昇。

**分散に向かう力:** ByteDance Seed 2.0の価格破壊 [INFO-017](../Information/2026-02-18/collected-raw.md#INFO-017)、MCPなどのオープン標準の広がり [INFO-024](../Information/2026-02-21/collected-raw.md#INFO-024)、OSSモデルの性能追い上げ [INFO-086](../Information/2026-02-18/collected-raw.md#INFO-086)。

現時点の判断は**「開放×格差拡大」（SCN-002, 32%）が最も確からしい**。技術やプロトコルは開放的になるが、トップ性能を出せる企業は限られる構造。ただしOpenAIのSkills/Shell路線が成功すれば「囲い込みの勝者」（SCN-001）に、価格下落がさらに進めば「誰でもAI」（SCN-004）に振れる可能性がある。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | ベンチマークで前世代比30%超の性能向上 | Gemini 3.1 Pro ARC-AGI-2 77.1%（146%向上）。30%閾値大幅超過 | **high** |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | $1300億が2社に集中。ただし資金調達≠市場構造変化 | **high** |
| [IND-004](../config/indicators.json) OSS性能到達 | OSSが商用モデルの90%性能に達するか | Llama 4 85.5%、GLM5トップ。90%閾値は未達 | elevated |
| [IND-006](../config/indicators.json) 標準乱立 | 3つ以上のAgent標準が競合するか | MCP、OpenAI Skills、Gemini Interactionsが共存中 | elevated |
| [IND-008](../config/indicators.json) 大企業の集中 | Fortune 500のAI導入先が2-3社に集中するか | 80%がエージェント使用開始。ただし「使用」≠「1社に集中」 | elevated |
| [IND-009](../config/indicators.json) AI投資持続 | 年間投資が前年比50%超成長を維持するか | 17社$100M超調達、CAPEX増加。ROI実現は5%のみ | elevated |
| [IND-011](../config/indicators.json) 性能収斂 | Tier 1各社のスコア差が5%以内に縮まるか | Gemini 4ptリード。価格下落は収斂圧力だが性能差は拡大中 | elevated |
| [IND-018](../config/indicators.json) AGI兆候 | AGI到達を示す複合的な兆候 | ARC-AGI-2 77.1%（閾値90%に13.9%不足）。Hassabis予測5-8年 | elevated |
| [IND-019](../config/indicators.json) AI業務自律化 | AIが人間の業務を自律的に代替しているか | 80%「使用」開始だが2.5%のみ人間品質完了。「浸透」≠「成功」 | elevated |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理能力にシフト | ジュニア開発者雇用20%減、AIスキル給与+$15-25K | **high** |
