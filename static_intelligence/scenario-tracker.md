# シナリオ分析 — 4つの未来のどれに向かっているか

> 最終更新: 2026-04-10

AI市場の展開を、2つの軸（技術の開放度 × 性能の格差）で4つのシナリオに分けて追跡している。

最有力は引き続き「技術は開くが勝者は出る」（SCN-002、36%）。プロトコル標準化は進み（AAIF 170+メンバー）[INFO-021](../Information/2026-04-10/collected-raw.md#INFO-021)、フロンティア性能は3社に集中している。

だが「静かな囲い込み」（SCN-003、28%）が定量証拠を得た。スイッチングコスト15-20% [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)、74%の企業がベンダー喪失時に業務混乱を予想 [INFO-097](../Information/2026-04-10/collected-raw.md#INFO-097)、Azure AI価格15-22%値上げ、GCP "premium inference"3倍価格 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)、エージェントコンテキスト蓄積が法的スイッチングコストを形成 [INFO-029](../Information/2026-04-10/collected-raw.md#INFO-029)。SCN-003の4前提全てを支持する証拠が揃った [Arbiter v3.46](../state/arbiter-2026-04-10.md)。

## 現在の確率

| シナリオ | 確率 | 象限 | 前回(4/8)比 |
|---------|------|------|------------|
| **SCN-002 技術は開くが勝者は出る** | **36%** | **開放 × 格差拡大** | **-2%** |
| **SCN-003 静かな囲い込み** | **28%** | 閉鎖 × 収斂 | **+1%** |
| SCN-001 囲い込みの勝者 | 23% | 閉鎖 × 格差拡大 | ±0% |
| SCN-004 誰でもAI | 13% | 開放 × 収斂 | +1% |

| ブラックスワン | 確率 | 前回比 | 影響度 |
|--------------|------|--------|--------|
| SCN-BS-001 AI安全性大事故 | 16% | ±0% | 壊滅的 |
| SCN-BS-002 量子×AI融合 | 3% | ±0% | 根本的変化 |

## 2つの軸の意味

4つのシナリオは、2つの根本的な問いの組み合わせで作られている。

**X軸: AIは囲い込まれるか、開放されるか？**

プロトコル層はAAIF（MCP+A2A、Linux Foundation傘下）で標準化が完了した。AAIFが**170+メンバー**に到達 [INFO-021](../Information/2026-04-10/collected-raw.md#INFO-021)。Gemini API Docs MCP提供 [INFO-012](../Information/2026-04-10/collected-raw.md#INFO-012)。しかしその上のレイヤー——実行環境、データ/コンテキスト、ガバナンス——では囲い込みが進行している。

**スイッチングコストの定量化**が新たな証拠。年間AI支出の15-20%。Azure 15-22%値上げ。GCP 3倍価格。74%の企業がベンダー喪失時に業務混乱を予想 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089) [INFO-097](../Information/2026-04-10/collected-raw.md#INFO-097)。プロトコルは開いても、コストとデータ層で囲い込みが進む構造が数値で裏付けられた。

SCR連邦控訴裁敗訴で政府による囲い込みが確定した側面もある [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。ただし、小規模AI企業への参入加速 [INFO-034](../Information/2026-04-10/collected-raw.md#INFO-034) は分散方向の証拠でもある。

**Y軸: トップ企業と後発の性能差は広がるか、縮まるか？**

GPT-5.4 ProのARC-AGI-2 83.3%（人間72.4%超え）とo3の87.5%が格差拡大の証拠。だがGemma 4がArena Elo 1452 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)、**Veracity AIが「性能ギャップは閉じた」と評価** [INFO-094](../Information/2026-04-10/collected-raw.md#INFO-094)、DeepSeek V3.2がGPT-5レベル性能を700分の1コストで提供 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。収斂方向の証拠も厚い。

## 各シナリオの詳細

### SCN-001 囲い込みの勝者（23%）— 閉鎖 × 格差拡大

1-2社が技術力で圧倒しつつ、実行環境・データ・ガバナンスで囲い込む世界。

23%で維持（3位）。OpenAI $122B調達完了、xAI-SpaceX $1.25兆統合、Meta CoreWeave $21Bで資金集中は継続。Anthropic Coefficient Bio $400M買収は垂直統合による囲い込みの深化。

ただしSCR確定は政府による囲い込みの確定でもあるが、同時に小規模AI企業への参入加速は分散方向。Mythos Previewサンドボックス脱出は単一企業集中リスクの reminder。

確率が上がる条件: Skills/Shellが開発者に定着、エンタープライズのベンダー集中が進む、垂直統合が加速。
確率が下がる条件: 実行環境の標準化が進む、反トラスト規制介入、政府選別に法的歯止め。

監視指標: [IND-001](../config/indicators.json)、[IND-002](../config/indicators.json)、[IND-003](../config/indicators.json)、[IND-015](../config/indicators.json)、[IND-018](../config/indicators.json)、[IND-019](../config/indicators.json)、[IND-020](../config/indicators.json)、[IND-024](../config/indicators.json)

### SCN-002 技術は開くが勝者は出る（36%）— 開放 × 格差拡大 ★現在最有力★

AAIF標準で相互運用性は確保されるが、フロンティア性能はTier 1の3社に集中する世界。

36%で低下（1位維持）。OpenAI Stateful Runtime囲い込み・GCP 3倍価格・Anthropic GCP依存深化で開放性が浸食。AAIF標準化は進展するが、データ・コスト層での囲い込みが部分無効化している [Arbiter v3.46](../state/arbiter-2026-04-10.md)。

このシナリオを支持する証拠は依然として最も厚い。AAIF 170+メンバー。MCP SDK月間9,700万DL。193カ国のジュネーブAI合意。EU AI法2026年8月完全施行。年10倍ペースの価格下落。Gemini API Docs MCP [INFO-012](../Information/2026-04-10/collected-raw.md#INFO-012)。DeepSeek V3.2の700分の1コスト [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。これらは「安いAIは自由に使えるが、最高のAIは一部の企業しか作れない」構造を補強する。

だがスイッチングコスト15-20%と74%ベンダー依存不安は、このシナリオの「開放性」に疑問を投げかける。

確率が上がる条件: AAIF標準の実効的採用率が高い、フロンティア性能格差が維持、規制コストが新規参入を阻害。
確率が下がる条件: 上位レイヤーの囲い込みが支配的に（→SCN-001/SCN-003）、価格破壊+品質検証でフロンティア追いつき（→SCN-004）。

監視指標: [IND-004](../config/indicators.json)、[IND-006](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-018](../config/indicators.json)、[IND-023](../config/indicators.json)、[IND-027](../config/indicators.json)

### SCN-003 静かな囲い込み（28%）— 閉鎖 × 収斂

モデル性能差は小さくなるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界。

28%で上昇（2位維持）。**スイッチングコストの定量化**が決定的な証拠になった:

1. **スイッチングコスト15-20%**: 年間AI支出の15-20%。エンジニアリング$200K-$600K + モデル再訓練$100K-$300K + データ移行$50K-$200K [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)
2. **74%ベンダー依存**: 企業の74%がAIベンダー喪失時に業務混乱または完全依存を予想 [INFO-097](../Information/2026-04-10/collected-raw.md#INFO-097)
3. **価格上昇15-22%**: Azure AI価格値上げ、GCP "premium inference"3倍価格 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)
4. **エージェントコンテキスト蓄積**: 512,000行の漏洩コードで確認されたコンテキスト依存が、6ヶ月の蓄積で法的スイッチングコストに [INFO-029](../Information/2026-04-10/collected-raw.md#INFO-029)

SCN-003の4前提（性能差縮小、エコシステム統合のスイッチングコスト、データ/コンテキスト層のロックイン、価格上昇による囲い込み）全てに定量証拠が揃った [Arbiter v3.46](../state/arbiter-2026-04-10.md)。

**OSS性能ギャップの閉鎖**も収斂方向の証拠。Veracity AI「性能ギャップは閉じた」[INFO-094](../Information/2026-04-10/collected-raw.md#INFO-094)。DeepSeek V3.2がGPT-5レベル性能を700分の1コストで [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。

確率が上がる条件: Agent SDK間の非互換性が固定化、垂直統合が加速、エコシステム依存の深化。
確率が下がる条件: Agent SDKの標準化が進む、反トラスト規制介入、ベンダー切り替えツールの出現。

監視指標: [IND-007](../config/indicators.json)、[IND-008](../config/indicators.json)、[IND-009](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-015](../config/indicators.json)、[IND-017](../config/indicators.json)、[IND-019](../config/indicators.json)、[IND-020](../config/indicators.json)、[IND-022](../config/indicators.json)、[IND-024](../config/indicators.json)

### SCN-004 誰でもAI（13%）— 開放 × 収斂

性能差がなくなりオープン標準で自由に行き来できる世界。

13%で上昇（4位）。OSS性能ギャップがほぼ閉じた [INFO-094](../Information/2026-04-10/collected-raw.md#INFO-094)。DeepSeek V3.2がGPT-5レベル性能を700分の1コストで提供 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。Qwen3 235Bが10分の1コスト。Gemma 4 Arena Elo 1452。

だし88%のAIエージェントプロジェクトが本番前に失敗 [INFO-064](../Information/2026-04-10/collected-raw.md#INFO-064)。インフラコスト障壁と運用品質の壁が、OSS性能追いつきの恩恵を相殺している。

確率が上がる条件: OSSモデルがフロンティアと同等性能に到達、価格破壊が品質検証と組み合わさる。
確率が下がる条件: フロンティア性能格差が維持・拡大、エコシステム囲い込みが深化。

監視指標: [IND-004](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-017](../config/indicators.json)、[IND-020](../config/indicators.json)、[IND-022](../config/indicators.json)、[IND-023](../config/indicators.json)

## ブラックスワン（低確率・高影響）

### SCN-BS-001 AI安全性大事故（16%）

AIエージェントの暴走やセキュリティ事故で社会的混乱が起き、厳格な規制が導入されて市場が凍結するシナリオ。

16%で維持。**Mythos Cybench 100%自律解決**で能力が質的転換点に到達 [INFO-009](../Information/2026-04-10/collected-raw.md#INFO-009)。OpenAIサイバー製品限定リリース、Anthropic Mythos限定ロールアウト——開発企業自身がリスクを懸念してリリースを制限する異例の事態。Glasswing防衛的閾値到達 [INFO-082](../Information/2026-04-10/collected-raw.md#INFO-082)。Bedrock新攻撃面 [INFO-032](../Information/2026-04-10/collected-raw.md#INFO-032)。

個々のインシデントは修正済みだが、パターンが見える。最も能力の高いモデルが最もリスクが高いという構造が確定 [IND-030](../config/indicators.json)。大規模AI攻撃インシデント確認時にcriticalへの上昇が必要。

### SCN-BS-002 量子コンピューティング×AI融合（3%）

量子コンピュータが実用化され、AI訓練・推論のコスト構造が根本から変わるシナリオ。関連する新情報なし。

## 確率推移データ

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|---------|---------|---------|---------|--------|--------|
| 2026-04-10 | 23% | 36% | 28% | 13% | 16% | 3% |
| 2026-04-08 | 23% | 38% | 27% | 12% | 16% | 3% |
| 2026-04-06 | 24% | 37% | 26% | 13% | 14% | 3% |
| 2026-04-05 | 24% | 37% | 25% | 14% | 14% | 3% |
| 2026-03-29 | 22% | 39% | 22% | 17% | 11% | 3% |
| 2026-03-24 | 20% | 41% | 21% | 18% | 11% | 3% |
| 2026-03-08 | 23% | 42% | 17% | 18% | 6% | 3% |
| 2026-03-07 | 24% | 41% | 17% | 18% | 6% | 3% |
| 2026-03-06 | 25% | 40% | 17% | 18% | 6% | 3% |
| 2026-03-01 | 26% | 37% | 19% | 18% | 6% | 3% |
| 2026-02-28 | 24% | 39% | 19% | 18% | 6% | 3% |
| 2026-02-27 | 25% | 38% | 20% | 17% | 6% | 3% |

大きなトレンド: SCN-002は36%で最有力維持だが、開放性浸食で低下傾向。SCN-003が28%で2位を維持し、スイッチングコスト定量証拠で押し上げられた。SCN-004は13%でOSS性能ギャップ閉鎖の恩恵を受けるも、インフラコスト障壁で上昇限定的。

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-10 | スイッチングコスト定量データ（15-20%・74%ベンダー依存・価格上昇15-22%）をSCN-003に反映。AAIF 170+メンバー、DeepSeek V3.2、OSS性能ギャップ閉鎖を追加。SCN-002 38%→36%、SCN-003 27%→28%、SCN-004 12%→13%に更新 |
| 2026-04-08 | シナリオ順位の入れ替わりを反映（SCN-003 2位上昇、SCN-001 3位後退）。MCP二面性、Mythos Previewサンドボックス脱出を追加 |
| 2026-04-06 | 鮮度タイムアウト対応。Gemma 4、Coze MCP対応、Doubao日次トークン120兆を反映 |
| 2026-03-29 | OpenAI $120B調達、xAI-SpaceX $1.25兆統合を反映 |
| 2026-03-24 | 2週間分統合。SCN-003 17%→21%（+4pt、最大上昇） |
