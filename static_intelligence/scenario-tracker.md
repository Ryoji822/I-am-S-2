# シナリオ分析 — 4つの未来のどれに向かっているか

> 最終更新: 2026-02-21

**AI市場が今後どう展開するかを、2つの軸（技術の開放度 × 性能の格差）で4つのシナリオに分けて追跡している。現在最も確からしいのは「技術は開くが勝者は出る」（SCN-002, 32%）。オープン標準は広がるが、フロンティア性能は一部企業に集中する構造。直近4日間でSCN-002が一貫して上昇（27%→32%）し、「静かな囲い込み」（SCN-003）は一貫して下降（33%→26%）。転換点は2/20のGemini 3.1 Pro性能躍進で、「性能が縮まる」前提のSCN-003が揺らぎ、「開放だが格差はある」SCN-002が台頭した。**

## 現在の確率

| シナリオ | 確率 | 象限 | 4日間の動き |
|---------|------|------|------------|
| SCN-001 囲い込みの勝者 | 22% | 閉鎖 × 格差拡大 | 22→22→20→22（横ばい） |
| **SCN-002 技術は開くが勝者は出る** | **32%** | **開放 × 格差拡大** | **27→28→31→32（上昇）** |
| SCN-003 静かな囲い込み | 26% | 閉鎖 × 収斂 | 33→31→29→26（下降） |
| SCN-004 誰でもAI | 20% | 開放 × 収斂 | 18→19→20→20（微増） |

| ブラックスワン | 確率 | 影響度 |
|--------------|------|--------|
| SCN-BS-001 AI安全性大事故 | 6% | 壊滅的 |
| SCN-BS-002 量子×AI融合 | 3% | 根本的変化 |

## 2つの軸の意味

4つのシナリオは、2つの根本的な問いの組み合わせで作られている。

**X軸: AIは囲い込まれるか、開放されるか？**
AIエージェントの実行環境・データ・ツール接続がベンダーごとにバラバラで移行しにくい「閉鎖」の世界か、MCPのようなオープン標準で自由に行き来できる「開放」の世界か。

**Y軸: トップ企業と後発の性能差は広がるか、縮まるか？**
Geminiのような最先端モデルが他社を大きく引き離す「格差拡大」の世界か、OSSを含めて性能差がなくなる「収斂」の世界か。

## 各シナリオの詳細

### SCN-001 囲い込みの勝者（22%）— 閉鎖 × 格差拡大

**どういう世界か:** 1-2社が技術力で圧倒しつつ、実行環境・ツール配布・データでエコシステムを囲い込む。一度あるプラットフォームに入ると抜け出せなくなり、後発はプラットフォーム依存を強いられる。

**今ある証拠:** OpenAIのSkills/Shell/Compaction [INFO-038](../Information/2026-02-21/collected-raw.md#INFO-038) は明確な囲い込みの動き。OpenClaw買収 [INFO-015](../Information/2026-02-21/collected-raw.md#INFO-015) でワークフローを押さえ、NVIDIA $300億投資 [INFO-102](../Information/2026-02-21/collected-raw.md#INFO-102) でハードウェア依存からの脱却も狙う。ただし「囲い込みを試みている」と「囲い込みに成功している」は違う。

**確率が上がる条件:** Skills/Shellが開発者に定着する、エンタープライズ顧客のベンダー集中が進む、性能リードが持続しGoogle製品ロックインが強化。
**確率が下がる条件:** MCPが広く採用されロックイン解消、OSSがフロンティアに近づく、反トラスト規制介入。

**監視指標:** [IND-001](../config/indicators.json), [IND-002](../config/indicators.json), [IND-003](../config/indicators.json), [IND-015](../config/indicators.json), [IND-016](../config/indicators.json), [IND-018](../config/indicators.json), [IND-019](../config/indicators.json), [IND-020](../config/indicators.json), [IND-021](../config/indicators.json)

### SCN-002 技術は開くが勝者は出る（32%）— 開放 × 格差拡大 ★現在最有力★

**どういう世界か:** MCPのようなオープン標準で相互運用性は高まる。AIエージェントは自由にツールと接続でき、ベンダーの切り替えも技術的には可能。しかしトップ性能はGoogleやOpenAIのような資金力のある企業に集中し、「最先端を使いたければ特定企業に頼むしかない」状態になる。

**なぜ今これが最有力か:**
- MCP標準化が進んでいる: Chrome/OWASP/Oracle対応 [INFO-024](../Information/2026-02-21/collected-raw.md#INFO-024) [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035)、Linux Foundation寄贈、10,000+サーバー → **開放**方向
- しかし性能差は拡大中: Gemini 3.1 Pro ARC-AGI-2 77.1%（前世代比146%向上）[INFO-008](../Information/2026-02-20/collected-raw.md#INFO-008)、Claude Opus 4.6を4ptリード [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028) → **格差拡大**方向
- 価格下落も開放を支持: 年10倍ペース [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)。安いAIは誰でも使える

つまり「安いAIは自由に使えるが、最高のAIは一部の企業しか作れない」という構造。

**確率が上がる条件:** MCP採用率の定量データが高い、OSSが向上するがフロンティアには及ばない、価格下落継続。
**確率が下がる条件:** OpenAI Skills/Shellが支配的になりMCPが廃れる（→SCN-001）、OSSがフロンティアに追いつく（→SCN-004）。

**監視指標:** [IND-004](../config/indicators.json), [IND-005](../config/indicators.json), [IND-006](../config/indicators.json), [IND-018](../config/indicators.json)

### SCN-003 静かな囲い込み（26%）— 閉鎖 × 収斂

**どういう世界か:** モデルの性能差は小さくなる（どこのAIもだいたい同じ）が、一度使い始めたプラットフォームから抜け出せなくなる。Googleの検索・Gmail・DriveにGeminiが深く統合されていたり、OpenAIのSkills/Shellでワークフローが固定化されていたりして、技術的にはどこでも良いのに「乗り換えコスト」が高すぎて動けない状態。

**今ある証拠:** Gemini $1.6/M最安 [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090) という価格競争は「性能で差がつかないから価格勝負」を示唆。Fortune 500の80%がエージェント使用開始 [INFO-070](../Information/2026-02-18/collected-raw.md#INFO-070) で使い始めると乗り換えが難しくなる。

**しかし直近で下降傾向（33%→26%）。** Gemini 3.1 Proの性能躍進は「収斂」ではなく「格差拡大」であり、このシナリオの前提（性能差が小さい）と矛盾している。

**監視指標:** [IND-007](../config/indicators.json), [IND-008](../config/indicators.json), [IND-009](../config/indicators.json), [IND-015](../config/indicators.json), [IND-016](../config/indicators.json), [IND-017](../config/indicators.json), [IND-019](../config/indicators.json), [IND-020](../config/indicators.json), [IND-021](../config/indicators.json), [IND-022](../config/indicators.json)

### SCN-004 誰でもAI（20%）— 開放 × 収斂

**どういう世界か:** AIの性能差がなくなり、オープン標準で自由に行き来できる。どの会社のAIを使っても同じような結果が出せ、差別化は業種・機能特化に集中する。AIの民主化が最も進んだ世界。

**今ある証拠:** OSS台頭（Llama 4 85.5%、GLM5トップ）[INFO-099](../Information/2026-02-21/collected-raw.md#INFO-099) [INFO-100](../Information/2026-02-21/collected-raw.md#INFO-100)、最安$0.05/Mから最高$30/Mまで600倍の価格差 [INFO-087](../Information/2026-02-21/collected-raw.md#INFO-087) で安いAIは十分使える。GitHub Copilot 2,000万人到達 [INFO-025](../Information/2026-02-20/collected-raw.md#INFO-025) でコーディングAIは既に民主化が進む。

**しかし最も確率が低い（20%）。** Gemini 3.1 Proの性能躍進はフロンティアの格差拡大を示しており、「誰でも同じ」にはまだ遠い。

**監視指標:** [IND-004](../config/indicators.json), [IND-010](../config/indicators.json), [IND-011](../config/indicators.json), [IND-012](../config/indicators.json), [IND-017](../config/indicators.json), [IND-020](../config/indicators.json), [IND-022](../config/indicators.json)

## ブラックスワン（低確率・高影響）

### SCN-BS-001 AI安全性大事故（6%）

AIエージェントの暴走やフェイク情報による社会混乱が起き、厳格な規制が導入されて市場が凍結するシナリオ。Agent Skills Registryへの攻撃リスク [INFO-025](../Information/2026-02-21/collected-raw.md#INFO-025) やOpenClawの700スキルマーケットプレイスの審査リスク [INFO-043](../Information/2026-02-21/collected-raw.md#INFO-043) が指摘され5%→6%に上昇。ただし実際の重大事故はまだ発生していない。

### SCN-BS-002 量子コンピューティング×AI融合（3%）

量子コンピュータが突然実用化され、AI訓練・推論のコスト構造が根本から変わるシナリオ。関連する新情報なし。

## 確率推移データ

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|---------|---------|---------|---------|--------|--------|
| 2026-02-21 | 22% | 32% | 26% | 20% | 6% | 3% |
| 2026-02-20 | 20% | 31% | 29% | 20% | 5% | 3% |
| 2026-02-19 | 22% | 28% | 31% | 19% | 5% | 3% |
| 2026-02-18 | 22% | 27% | 33% | 18% | 5% | 3% |

大きなトレンド: SCN-002が4日間で+5%上昇（27%→32%）し首位に。SCN-003が-7%下降（33%→26%）。転換点は2/20のGemini 3.1 Pro性能躍進で、「性能が縮まる」前提のSCN-003が揺らぎ、「開放×格差拡大」のSCN-002が台頭した。
