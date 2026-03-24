# Google / DeepMind

> 最終更新: 2026-03-09

**GPT-5.4 Pro（ARC-AGI-2 83.3%）にベンチマーク首位を奪われ、Gemini 3.1 Proは77.1%で6.2pt差の2位に後退 [INFO-043](../Information/2026-03-08/collected-raw.md#INFO-043)。ただしGemini 3 Deep ThinkはARC-AGI-2 84.6%でGPT-5.4 Proを上回る非公式記録を持つ。統合戦略（H-GOO-001）は確証バイアス警告を受けて54%に下降——全証拠がconsistent（I=0）で反証探索が構造的に不十分 [Arbiter v3.7-3.8]。ADK統合エコシステムが25以上のパートナーに拡大 [INFO-014](../Information/2026-03-07/collected-raw.md#INFO-014)、Workspace CLI MCP統合 [INFO-025](../Information/2026-03-08/collected-raw.md#INFO-025) で開放的エコシステムは進展。Gemini RoboticsがBoston Dynamics Atlasに統合 [INFO-028](../Information/2026-03-07/collected-raw.md#INFO-028)。**

## この会社は何者か

Sundar Pichai率いるテクノロジー企業。主力はGemini 3.1シリーズ、Vertex AI、Google Workspace、Google Cloud。従業員180,000人以上。

他のAI企業と根本的に違うのは、外部の資金調達が要らないこと。開発競争が長引くほど有利になる構造的な強み。

性能面では依然として高水準だが首位ではなくなった。Gemini 3.1 ProがARC-AGI-2で77.1%（前世代31.1%から146%向上）[INFO-008](../Information/2026-02-20/collected-raw.md#INFO-008) だが、GPT-5.4 Proの83.3%に6.2pt劣後 [INFO-043](../Information/2026-03-08/collected-raw.md#INFO-043)。Gemini 3 Deep ThinkはARC-AGI-2で84.6% [INFO-082](../Information/2026-02-18/collected-raw.md#INFO-082) だが推論特化モデルであり、汎用Proラインとは位置付けが異なる。MMMU-Pro 1位 [INFO-033](../Information/2026-02-21/collected-raw.md#INFO-033)。GPQA Diamondリーダー [INFO-081](../Information/2026-02-18/collected-raw.md#INFO-081)。価格は$1.6/Mと業界最安水準 [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090)。

直近の展開: (1) Gemini 3.1 Pro Preview [INFO-008](../Information/2026-02-21/collected-raw.md#INFO-008)。(2) Workspace CLI MCP統合でGmail/DriveがAIエージェントから直接操作可能に [INFO-025](../Information/2026-03-08/collected-raw.md#INFO-025)。(3) ADK統合エコシステムが25以上のパートナーに拡張 [INFO-014](../Information/2026-03-07/collected-raw.md#INFO-014)。(4) Gemini RoboticsがBoston Dynamics Atlasに統合 [INFO-028](../Information/2026-03-07/collected-raw.md#INFO-028)。(5) Chrome Web MCPでAIエージェントがブラウザ操作可能に [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035)。

A2A（Agent2Agent Protocol）はLinux Foundation AAIFに寄贈されたが、MCP主導のエコシステムに対して採用は失速気味。

## 何をやろうとしているか

Googleの動きは一貫性が高いが、統合戦略の実行品質と確証バイアスリスクの両面で課題がある。

**本命: 全プロダクトにGeminiを溶かし込む（H-GOO-001, 確度54%）**

v2.0で71%→55%に大幅下降し、さらに確証バイアス警告で54%に微減。方向性は変わらないが、深刻な反証と構造的リスクがある:

1. **プライバシー集団訴訟**: Thele v. Google LLC（2025年11月、北カリフォルニア連邦地裁）。Geminiを2025年10月にGmail/Chat/Meetユーザーに無断で有効化
2. **Assistant→Gemini移行延期**: 当初2025年完了予定が2026年に延期。Geminiが基本タスクを処理できない機能不足
3. **幻覚率の問題**: 金融タスクでGeminiの幻覚率76.7%、ChatGPTの約4倍
4. **確証バイアス警告**: Arbiter v3.7-3.8で全証拠がconsistent（I=0）であり反証探索が構造的に不十分と指摘。反証不在で確度を上昇させることは論理的に矛盾

一方、Workspace CLI MCP統合 [INFO-025](../Information/2026-03-08/collected-raw.md#INFO-025) は統合戦略の具体的進展であり、開放性と統合を両立させる可能性を示す。

**もう一つの読み: Vertex AIでクラウド市場を追い上げる（H-GOO-002, 確度54%）**

Vertex AI + Geminiの組み合わせでクラウドAI市場を拡大する。$1.6/Mの価格競争力が武器。ADK統合エコシステム25以上パートナー [INFO-014](../Information/2026-03-07/collected-raw.md#INFO-014) は開放的アプローチの証拠。ただし確証バイアス警告（全I=0）で54%に微減。

**もう一つの読み: 研究ブレークスルーで新カテゴリを作る（H-GOO-003, 確度56%）**

DeepMindの研究ブレークスルーでAI応用先を創出する。Gemini RoboticsのBoston Dynamics Atlas統合 [INFO-028](../Information/2026-03-07/collected-raw.md#INFO-028) は物理世界AI研究の商用化の兆し。IMO-ProofBench 90%、Erdős問題4問解決 [INFO-011](../Information/2026-02-18/collected-raw.md#INFO-011)。ベンチマーク首位はGPT-5.4 Proに奪われたが、Deep Think（84.6%）は推論領域でのリードを維持。

## 強みと弱み

**強み:**
- **高水準のベンチマーク性能**: ARC-AGI-2 77.1%は2位。Deep Think 84.6%は推論特化で最高。MMMU-Pro 1位
- **プロダクト規模**: 検索・Gmail・Drive・Workspaceの既存ユーザーベース（Gemini MAU 6.5億）
- **自己資金**: 外部調達不要で長期戦に強い
- **価格競争力**: $1.6/Mは業界最安水準
- **開放的エコシステム**: ADK 25+パートナー、Workspace CLI MCP統合、AAIF共同創設

**弱み:**
- **ベンチマーク首位喪失**: GPT-5.4 Pro（83.3%）に6.2pt差で2位に後退 [INFO-043](../Information/2026-03-08/collected-raw.md#INFO-043)
- **確証バイアスリスク**: 仮説の全証拠がI=0で反証探索が構造的に不十分
- **プライバシー訴訟リスク**: Thele v. Google LLCの集団訴訟発展の可能性
- **統合の実行品質**: Assistant→Gemini移行延期、金融タスク幻覚率76.7%
- **エンタープライズ直接営業力**: OpenAI（Microsoft）やAnthropic（Infosys）に対して弱い

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| ARC-AGI-2でのGPT-5.4 Proとの差 | 首位奪還するか、さらに引き離されるか | 77.1% vs 83.3%、6.2pt差（[IND-001](../config/indicators.json), high） |
| Thele v. Google LLC訴訟の進展 | 集団訴訟化すれば統合戦略に法的制約 | 2025年11月提訴 |
| Google I/O 2026（5/19-20） | プロダクト統合の全貌が発表される可能性 | 開催決定 [INFO-010](../Information/2026-02-18/collected-raw.md#INFO-010) |
| Workspace CLI MCP統合の採用状況 | 開放×統合の両立モデルが機能するか | リリース済み [INFO-025](../Information/2026-03-08/collected-raw.md#INFO-025) |
| Gemini幻覚率の改善 | 76.7%→50%以下にしないとエンタープライズ信頼を得られない | 76.7% |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-03-09 | GPT-5.4 Pro（83.3%）にベンチマーク首位を奪われた事実を反映。ADK 25+パートナー、Workspace CLI MCP統合、Gemini Robotics+Boston Dynamics統合を追記。確証バイアス警告で全仮説確度を微減 |
| 2026-02-23 | 初版作成（Gemini 3.1 Pro性能突出・統合戦略の実行品質課題）
