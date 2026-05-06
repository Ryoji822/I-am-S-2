# シナリオ分析 — 4つの未来のどれに向かっているか

> 最終更新: 2026-05-06

AI市場の展開を、2つの軸（技術の開放度 × 性能の格差）で4つのシナリオに追跡している。

最有力は「技術は開くが勝者は出る」（SCN-002、38%）。だが3ラウンド連続で確率が下がっている。「静かな囲い込み」（SCN-003、28%）が3ラウンド連続で確率を上げ、差は10ptに縮まった。围い込みシグナルの構造的蓄積が続けば、SCN-003がSCN-002を逆転する可能性が現実的になる [Arbiter v3.70](../state/arbiter-2026-05-06.md)。

## 現在の確率

| シナリオ | 確率 | 象限 | 前回(04-29)比 |
|---------|------|------|-------------|
| **SCN-002 技術は開くが勝者は出る** | **38%** | **開放 × 格差拡大** | **-6%** |
| **SCN-003 静かな囲い込み** | **28%** | **閉鎖 × 収斂** | **+4%** |
| SCN-001 囲い込みの勝者 | 20% | 閉鎖 × 格差拡大 | ±0% |
| SCN-004 誰でもAI | 14% | 開放 × 収斂 | +2% |

| ブラックスワン | 確率 | 前回比 | 影響度 |
|--------------|------|--------|--------|
| SCN-BS-001 AI安全性大事故 | 16% | ±0% | 壊滅的 |
| SCN-BS-002 量子×AI融合 | 3% | ±0% | 根本的変化 |

## 2つの軸の意味

**X軸: AIは囲い込まれるか、開放されるか？**

MCP全社サポート（OpenAI/Google/Microsoft/Block）[INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015)。Red Hat MCP Gateway（エンタープライズ規模トラフィック制御）[INFO-016](../Information/2026-05-06/collected-raw.md#INFO-016)。MCP in Visual Studio [INFO-019](../Information/2026-05-06/collected-raw.md#INFO-019)。開放潮流は構造的に強い。

だし围い込みシグナルも蓄積している。MSFT Agent 365 GA [INFO-026](../Information/2026-05-06/collected-raw.md#INFO-026)。Copilot credit system [INFO-050](../Information/2026-05-06/collected-raw.md#INFO-050)。ベンダーロックイン深化 [INFO-033](../Information/2026-05-06/collected-raw.md#INFO-033)。**Anthropic+OpenAIの同週JV設立**で围い込みに「金融次元」が追加 [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)。

**Y軸: トップ企業と後発の性能差は広がるか、縮まるか？**

BenchLM総合: Claude Mythos Preview 99、Gemini 3.1 Pro 93、GPT-5.4 Pro 92 [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。上位3社の差は6-7pt。「勝者」格差として限界的。

OSS gap 8%→1.7%に縮小 [INFO-051](../Information/2026-05-06/collected-raw.md#INFO-051)。収斂方向の証拠も存在する。

## 各シナリオの詳細

### SCN-001 囲い込みの勝者（20%）— 閉鎖 × 格差拡大

1-2社が技術力で圧倒しつつ、実行環境・データ・ガバナンスで囲い込む世界。

20%で維持（3位）。Pentagon 7社（非1-2社）[INFO-073](../Information/2026-05-06/collected-raw.md#INFO-073)。OpenAI on AWS。xAI on Google。MCP全社対応。JVは围い込みCだが複数金融パートナーで非独占的。相殺。

監視指標: [IND-001](../config/indicators.json)、[IND-002](../config/indicators.json)、[IND-003](../config/indicators.json)、[IND-015](../config/indicators.json)、[IND-018](../config/indicators.json)、[IND-019](../config/indicators.json)、[IND-020](../config/indicators.json)、[IND-024](../config/indicators.json)

### SCN-002 技術は開くが勝者は出る（38%）— 開放 × 格差拡大 ★現在最有力★

AAIF標準で相互運用性は確保されるが、フロンティア性能はTier 1の3社に集中する世界。

38%に低下（1位維持だが3R連続-1%）。3社均質化（Agent Platform三社鼎立）が「勝者」前提を侵食。BenchLM上位3社の差は6-7ptで「勝者」格差として限界的 [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。Pattern 2確度「中」継続。

監視指標: [IND-004](../config/indicators.json)、[IND-006](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-018](../config/indicators.json)、[IND-023](../config/indicators.json)、[IND-027](../config/indicators.json)

### SCN-003 静かな囲い込み（28%）— 閉鎖 × 収斂

モデル性能差は小さくなるが、データ・ワークフロー・エコシステムのスイッチングコストで顧客が固定化する世界。

28%に上昇（2位維持、3R連続+1%）。MSFT Agent 365 GA [INFO-026](../Information/2026-05-06/collected-raw.md#INFO-026) + Copilot credit system [INFO-050](../Information/2026-05-06/collected-raw.md#INFO-050) + ベンダーロックイン深化 [INFO-033](../Information/2026-05-06/collected-raw.md#INFO-033) + **JV围い込み（金融次元新規追加）** [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) の4重C。4R目も同方向の場合、SCN-002を逆転する可能性が現実的になる。

監視指標: [IND-007](../config/indicators.json)、[IND-008](../config/indicators.json)、[IND-009](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-015](../config/indicators.json)、[IND-017](../config/indicators.json)、[IND-019](../config/indicators.json)、[IND-020](../config/indicators.json)、[IND-022](../config/indicators.json)、[IND-024](../config/indicators.json)

### SCN-004 誰でもAI（14%）— 開放 × 収斂

性能差がなくなりオープン標準で自由に行き来できる世界。

14%で上昇（4位）。OSS gap 8%→1.7%はC [INFO-051](../Information/2026-05-06/collected-raw.md#INFO-051)。だがBenchLM上位12pt差はI [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。$14B損失+$900B評価額で資本集中加速。二層市場下層にのみ部分的適合。

監視指標: [IND-004](../config/indicators.json)、[IND-011](../config/indicators.json)、[IND-017](../config/indicators.json)

## ブラックスワン（低確率・高影響）

### SCN-BS-001 AI安全性大事故（16%）

AIエージェント本番DB削除 [INFO-009](../Information/2026-05-06/collected-raw.md#INFO-009)。24.4%のみAI完全可視性 [INFO-036](../Information/2026-05-06/collected-raw.md#INFO-036)。MCP Shadow IT継続 [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015)。攻撃面拡大継続。複合リスク蓄積。大規模AI攻撃インシデント未到達。

### SCN-BS-002 量子コンピューティング×AI融合（3%）

関連する新情報なし。

## 確率推移データ

| 日付 | SCN-001 | SCN-002 | SCN-003 | SCN-004 | BS-001 | BS-002 |
|------|---------|---------|---------|---------|--------|--------|
| 2026-05-06 | 20% | 38% | 28% | 14% | 16% | 3% |
| 2026-05-05 | 20% | 39% | 27% | 14% | 16% | 3% |
| 2026-05-04 | 20% | 40% | 26% | 14% | 16% | 3% |
| 2026-05-03 | 20% | 41% | 26% | 13% | 16% | 3% |
| 2026-05-02 | 20% | 42% | 25% | 13% | 16% | 3% |
| 2026-05-01 | 20% | 43% | 24% | 13% | 16% | 3% |
| 2026-04-30 | 20% | 43% | 24% | 13% | 16% | 3% |
| 2026-04-29 | 20% | 44% | 24% | 12% | 16% | 3% |
| 2026-04-28 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-27 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-26 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-25 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-24 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-23 | 21% | 42% | 25% | 12% | 16% | 3% |
| 2026-04-22 | 23% | 40% | 25% | 12% | 16% | 3% |
| 2026-04-21 | 23% | 39% | 26% | 12% | 16% | 3% |
| 2026-04-20 | 24% | 38% | 26% | 12% | 16% | 3% |
| 2026-04-19 | 24% | 38% | 26% | 12% | 16% | 3% |
| 2026-04-17 | 24% | 37% | 27% | 12% | 16% | 3% |
| 2026-04-13 | 24% | 37% | 27% | 12% | 16% | 3% |
| 2026-04-11 | 23% | 37% | 28% | 13% | 16% | 3% |
| 2026-04-08 | 23% | 38% | 27% | 12% | 16% | 3% |
| 2026-04-06 | 24% | 37% | 26% | 13% | 14% | 3% |
| 2026-03-29 | 22% | 39% | 22% | 17% | 11% | 3% |
| 2026-03-24 | 20% | 41% | 21% | 18% | 11% | 3% |
| 2026-03-08 | 23% | 42% | 17% | 18% | 6% | 3% |

大きなトレンド: SCN-002は44%（04-29）から38%（05-06）へ3R連続で-1%ずつ減少。SCN-003は24%（04-29）から28%（05-06）へ3R連続で+1%ずつ増加。围い込みシグナルの構造的蓄積（Agent 365 GA+Copilot credit+lock-in+JV金融次元）が連続シフトの主因。4R目も同方向の場合、SCN-003がSCN-002を逆転する可能性が現実的になる。

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-05-06 | **鮮度タイムアウト対応（7日経過）**。围い込みシグナル4重蓄積（Agent 365 GA+Copilot credit+lock-in+JV金融次元）・3社均質化（BenchLM上位差6-7pt）・OSS gap 8%→1.7%を反映。SCN-002 44→38%（-6%）・SCN-003 24→28%（+4%）・SCN-004 12→14%（+2%）に更新。確率推移データに04-30〜05-06分を追加 |
| 2026-04-29 | 鮮度タイムアウト対応。三大クラウドAgent Platform同一週リリース・Microsoft-OpenAI提携改訂を反映 |
| 2026-04-22 | エンタープライズ決戦クラスターを反映 |
| 2026-04-17 | 鮮度タイムアウト対応 |
| 2026-04-08 | シナリオ順位入れ替わりを反映 |
