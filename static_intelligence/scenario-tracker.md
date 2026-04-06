# シナリオ分析 — 4つの未来のどれに向かっているか

> 最終更新: 2026-04-06

AI市場の展開を、2つの軸（技術の開放度 × 性能の格差）で4つのシナリオに分けて追跡している。

最有力は引き続き「技術は開くが勝者は出る」（SCN-002、37%）。プロトコル標準化は進み（**Coze MCP対応** [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)）、フロンティア性能は3社に集中している。**Gemma 4（Arena Elo 1452）** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006) と **Doubao日次トークン120兆** [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024) は、開放と集中が同時に進む構造を補強する。

変わったのは2つ。「囲い込みの勝者」（SCN-001）が24%で維持。資金集中は継続しているが、**連邦判事がPentagonのAnthropic指定に一時差止** [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008) を発行したことで、政府による囲い込みに歯止めがかかった。もう一つ、「静かな囲い込み」（SCN-003）が25%で維持。**Anthropic Coefficient Bio $400M買収** [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013) は垂直統合による囲い込みの深化を示す。

## 現在の確率

| シナリオ | 確率 | 象限 | 前回(4/5)比 |
|---------|------|------|------------|
| **SCN-002 技術は開くが勝者は出る** | **37%** | **開放 × 格差拡大** | **±0%** |
| SCN-003 静かな囲い込み | 25% | 閉鎖 × 収斂 | ±0% |
| SCN-001 囲い込みの勝者 | 24% | 閉鎖 × 格差拡大 | ±0% |
| SCN-004 誰でもAI | 14% | 開放 × 収斂 | ±0% |

| ブラックスワン | 確率 | 前回比 | 影響度 |
|--------------|------|--------|--------|
| SCN-BS-001 AI安全性大事故 | 14% | ±0% | 売滅的 |
| SCN-BS-002 量子×AI融合 | 3% | ±0% | 根本的変化 |

## 2つの軸の意味

4つのシナリオは、2つの根本的な問いの組み合わせで作られている。

**X軸: AIは囲い込まれるか、開放されるか？**

プロトコル層はAAIF（MCP+A2A、Linux Foundation傘下）で標準化が完了した。**CozeがMCPプロトコル対応** [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)、**Gemma 4がApache 2.0ライセンスで公開** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。しかしその上のレイヤー——実行環境、データ/コンテキスト、ガバナンス——では囲い込みが進行している。

Pentagonのサプライチェーンリスク指定は新しいタイプの囲い込みの試み。だが**連邦判事が一時差止を発行** [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008) したことで、政府による囲い込みに法的歯止めがかかった。

**Y軸: トップ企業と後発の性能差は広がるか、縮まるか？**

GPT-5.4 ProのARC-AGI-2 83.3%（人間72.4%超え）とo3の87.5%が格差拡大の証拠。だが**Gemma 4がArena Elo 1452** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006) でオープンモデルとして最高水準に到達。性能差は縮まっているが、フロンティア首位（ARC-AGI-2 83.3%、GPQA 94.3%）にはまだ届かない。

## 各シナリオの詳細

### SCN-001 囲い込みの勝者（24%）— 閉鎖 × 格差拡大

1-2社が技術力で圧倒しつつ、実行環境・データ・ガバナンスで囲い込む世界。

24%で維持。OpenAI $120B調達完了、xAI-SpaceX $1.25兆統合で資金集中は継続。**Anthropic Coefficient Bio $400M買収** [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013) は垂直統合による囲い込みの深化。

ただし**連邦判事がPentagonのAnthropic指定に一時差止** [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008) を発行したことは、政府による囲い込みへの反証。政府が特定企業を選別しようとする動きに法的制約がかかった。

確率が上がる条件: Skills/Shellが開発者に定着、エンタープライズのベンダー集中が進む、垂直統合が加速。
確率が下がる条件: 実行環境の標準化が進む、反トラスト規制介入、政府選別に法的歯止め。

監視指標: [IND-001](../config/indicators.json), [IND-002](../config/indicators.json), [IND-003](../config/indicators.json), [IND-015](../config/indicators.json), [IND-018](../config/indicators.json), [IND-019](../config/indicators.json), [IND-020](../config/indicators.json), [IND-024](../config/indicators.json)

### SCN-002 技術は開くが勝者は出る（37%）— 開放 × 格差拡大 ★現在最有力★

AAIF標準で相互運用性は確保されるが、フロンティア性能はTier 1の3社に集中する世界。

37%で維持。**CozeがMCPプロトコル対応** [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025) で標準化が進展。**Gemma 4がApache 2.0ライセンスで公開** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006) でオープンモデルの性能水準が向上。**Doubao日次トークン120兆** [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024) は低価格AIの普及を示す。

このシナリオを支持する証拠は依然として最も厚い。MCP SDK月間9,700万DL。193カ国のジュネーブAI合意。EU AI法2026年8月完全施行。年10倍ペースの価格下落。**Gemini API Flex/Priorityティア** [INFO-010](../Information/2026-04-06/collected-raw.md#INFO-010)、**Codexトークン課金** [INFO-009](../Information/2026-04-06/collected-raw.md#INFO-009) で価格体系が多様化。これらすべてが「安いAIは自由に使えるが、最高のAIは一部の企業しか作れない」構造を補強する。

確率が上がる条件: AAIF標準の実効的採用率が高い、フロンティア性能格差が維持、規制コストが新規参入を阻害。
確率が下がる条件: 上位レイヤーの囲い込みが支配的に（→SCN-001/SCN-003）、価格破壊+品質検証でフロンティア追いつき（→SCN-004）。

監視指標: [IND-004](../config/indicators.json), [IND-006](../config/indicators.json), [IND-011](../config/indicators.json), [IND-018](../config/indicators.json), [IND-023](../config/indicators.json), [IND-027](../config/indicators.json)

### SCN-003 静かな囲い込み（25%）— 閉鎖 × 収斂

モデル性能差は小さくなるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界。

25%で維持。**Anthropic Coefficient Bio $400M買収** [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013) は垂直統合による囲い込みの深化。ライフサイエンス領域でのClaude for Life Sciences、金融でのClaude for Financial Servicesと続く業界別ソリューション展開は、エコシステム依存を深める動き。

エージェントSDK乱立は「開放」に見えるが、各社のSDKは相互運用しない。一度構築すると切り替えコストが発生する。

確率が上がる条件: Agent SDK間の非互換性が固定化、垂直統合が加速、エコシステム依存の深化。
確率が下がる条件: Agent SDKの標準化が進む、反トラスト規制介入、ベンダー切り替えツールの出現。

監視指標: [IND-007](../config/indicators.json), [IND-008](../config/indicators.json), [IND-009](../config/indicators.json), [IND-011](../config/indicators.json), [IND-015](../config/indicators.json), [IND-017](../config/indicators.json), [IND-019](../config/indicators.json), [IND-020](../config/indicators.json), [IND-022](../config/indicators.json), [IND-024](../config/indicators.json)

### SCN-004 誰でもAI（14%）— 開放 × 収斂

性能差がなくなりオープン標準で自由に行き来できる世界。

14%で維持。**Gemma 4 Arena Elo 1452** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)、**Doubao日次トークン120兆** [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024) は収斂方向の証拠。だがGPT-5.4 Pro 83.3%やGPQA Diamond 94.3%が示すフロンティア格差は依然として大きい。「誰でも同じ」にはまだ距離がある。

確率が上がる条件: OSSモデルがフロンティアと同等性能に到達、価格破壊が品質検証と組み合わさる。
確率が下がる条件: フロンティア性能格差が維持・拡大、エコシステム囲い込みが深化。

監視指標: [IND-004](../config/indicators.json), [IND-011](../config/indicators.json), [IND-017](../config/indicators.json), [IND-020](../config/indicators.json), [IND-022](../config/indicators.json), [IND-023](../config/indicators.json)

## ブラックスワン（低確率・高影響）

### SCN-BS-001 AI安全性大事故（14%）

AIエージェントの暴走やセキュリティ事故で社会的混乱が起き、厳格な規制が導入されて市場が凍結するシナリオ。

14%で変動なし。**Claude Codeソース流出（512,000行）** [INFO-007](../Information/2026-04-06/collected-raw.md#INFO-007) が新たなインシデントとして追加。OpenClaw 135,000超露出、Claudy Day脆弱性、Meta Sev-1インシデントと続く事件の蓄積が継続。

個々のインシデントは修正済みだが、パターンが見える。エージェントの自律性が上がるほど攻撃面が広がり、プロトコル標準化がセキュリティレビューより速く進んでいる。

### SCN-BS-002 量子コンピューティング×AI融合（3%）

量子コンピュータが実用化され、AI訓練・推論のコスト構造が根本から変わるシナリオ。関連する新情報なし。

## 確率推移データ

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|---------|---------|---------|---------|--------|--------|
| 2026-04-06 | 24% | 37% | 25% | 14% | 14% | 3% |
| 2026-04-05 | 24% | 37% | 25% | 14% | 14% | 3% |
| 2026-03-29 | 22% | 39% | 22% | 17% | 11% | 3% |
| 2026-03-24 | 20% | 41% | 21% | 18% | 11% | 3% |
| 2026-03-08 | 23% | 42% | 17% | 18% | 6% | 3% |
| 2026-03-07 | 24% | 41% | 17% | 18% | 6% | 3% |
| 2026-03-06 | 25% | 40% | 17% | 18% | 6% | 3% |
| 2026-03-01 | 26% | 37% | 19% | 18% | 6% | 3% |
| 2026-02-28 | 24% | 39% | 19% | 18% | 6% | 3% |
| 2026-02-27 | 25% | 38% | 20% | 17% | 6% | 3% |

大きなトレンド: SCN-002は37%で最有力を維持。**Coze MCP対応** [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)、**Gemma 4オープンモデル** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)、**Doubao日次トークン120兆** [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024) が開放性を支持。一方で**Anthropic Coefficient Bio買収** [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013) は垂直統合による囲い込みの深化。**連邦判事の一時差止** [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008) は政府囲い込みへの歯止め。

BS-001は14%で維持。セキュリティインシデントの蓄積（Claude Codeソース流出追加）は継続しているが、社会的混乱に至る「大事故」には未到達。

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-06 | 鮮度タイムアウト対応。Gemma 4、Coze MCP対応、Doubao日次トークン120兆、Anthropic Coefficient Bio買収、連邦判事一時差止、Claude Codeソース流出を反映。シナリオ確率は±0%維持（Arbiter未完了のため） |
| 2026-03-29 | OpenAI $120B調達、xAI-SpaceX $1.25兆統合を反映。SCN-001 20%→22%（+2pt）、SCN-002 41%→39%（-2pt）、SCN-003 21%→22%（+1pt）、SCN-004 18%→17%（-1pt） |
| 2026-03-24 | 2週間分統合。SCN-003 17%→21%（+4pt、最大上昇）。BS-001 6%→11%（ほぼ倍増） |
| 2026-03-09 | GPT-5.4 Pro人間超え（83.3%）でSCN-002 42%に上昇 |
| 2026-02-23 | 初版作成 |
