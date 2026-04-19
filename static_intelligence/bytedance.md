# ByteDance

> 最終更新: 2026-04-19
> 確度: 中

価格破壊でAI市場を揺さぶり、Doubao MAU 2.26億でグローバル2位を達成した。日次トークン使用量が120兆超——2年で1000倍増加。DAUは1.45億で国内AIアプリ首位 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。Seeduplexで原生全二重音声モデルを豆包App全ユーザーに展開 [INFO-056](../Information/2026-04-10/collected-raw.md#INFO-056)。Seedance 2.0のグローバル展開は透かし/IPガードレール実装で再開。**DeerFlow 2.0**がMITライセンスでオープンソース化——LangGraph/LangChainベースのスーパーエージェントハーネスで、Dockerサンドボックス・MCP対応・Claude Code統合スキルを含む [INFO-016](../Information/2026-04-19/collected-raw.md#INFO-016)。「安くて速い」は確認済みだが、「グローバルで使える」にはまだ壁がある。

## この会社は何物か

Liang Rubo率いる。主力はDoubao（豆包）2.0シリーズ、Seed 2.0シリーズ（Pro/Lite/Mini/Code）、**Seeduplex**（全二重音声）、Cozeプラットフォーム、Seedance 2.0。従業員150,000人以上。TikTok/Douyinの基盤を持つ。

価格は確認済みの強み。Seed 2.0 Pro $0.47/M入力、$2.37/M出力。Claude Opus比で約10倍安、GPT-5.2比で3.7-5.9倍安。Doubao 2.0は¥3.2/¥16（百万トークンあたり）。

**使用量が爆発的成長**: 日次トークン使用量120兆超（2年で1000倍）。DAU 1.45億で国内AIアプリ首位 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。

**Seeduplex**（2026年4月9日）: 原生全二重音声モデル。「边听边说」（聞きながら話す）設計。豆包Appで全量ローンチ [INFO-056](../Information/2026-04-10/collected-raw.md#INFO-056)。

**DeerFlow 2.0**（2026年4月11日）: v1から全面書き直しのオープンソース（MIT）スーパーエージェントハーネス。LangGraph/LangChainベース。スキル・サブエージェント・Docker/Kubernetesサンドボックス実行・ファイルシステムアクセス・長期メモリ・MCP・Slack/Telegramメッセージングを統合。Claude Code統合スキルあり。推奨モデル: Doubao-Seed-2.0-Code、DeepSeek v3.2、Kimi 2.5 [INFO-016](../Information/2026-04-19/collected-raw.md#INFO-016)。SkillClaw（マルチユーザースキル進化フレームワーク）のコミュニティ貢献も進行。

**豆包大モデル 1.8**: マルチモーダルAgentシーン向けに最適化 [INFO-057](../Information/2026-04-10/collected-raw.md#INFO-057)。

Seedance 2.0は2K映画画質、原生音画同期、API公開テスト中。

ベンチマークは自己報告値のまま。AIME 2025で98.3%、SWE-Bench Verified 76.5%、GPQA Diamond 88.9%、Codeforces 3020。いずれもByteDance発表で、独立第三者検証は完了していない。

規模は評価額$520B。Moonton（ゲーム事業）を~$60Bで売却し、AI投資に経営資源集中。

## 何をやろうとしているか

### 低価格で市場を揺さぶる（H-BTD-002、確度70%）

圧倒的なコスト優位性で新興市場を席巻し、Tier 1全体の価格を押し下げる。Seed 2.0 Proの$0.47/Mは確認済みで、実際にAnthropic Opus 4.6の67%値下げ、Geminiの$1.6/M低下を引き起こした。

日次トークン120兆は低価格戦略が市場を獲得している証拠 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。DAU 1.45億は中国国内での圧倒的優位を示す。ただし自己発表データであり、第三者検証が必要。

確度は70%（Arbiter v3.54）。Coze 2.5・DeerFlow 2.0 OSSは価格戦略継続のC。新規価格比較データなし。

### 中国から世界へ（H-BTD-001、確度66%）

Doubao/Cozeで中国市場を支配し、東南アジア、そしてグローバルに展開する。MAU 2.26億でグローバル2位は強力な基盤。

**DeerFlow 2.0の意味**: MITライセンスでオープンソース化されたスーパーエージェントハーネスは、技術力の対外展示として機能する [INFO-016](../Information/2026-04-19/collected-raw.md#INFO-016)。Claude Code統合スキルを含むことは、国境を超えた技術エコシステムへの参加を示唆する。ただし推奨モデルにDeepSeek v3.2、Kimi 2.5等の競合中国モデルが含まれている点は、DeerFlow自体がByteDance囲い込みツールではないことを示す。

Seedance 2.0グローバル再開: 透かし/IPガードレール実装で著作権問題に対応 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。Disney/Netflix/Paramount訴訟後の再開は法的リスクへの対応が進んだことを示す。

Coze MCP対応: 標準MCPプロトコルで企查查等と接続 [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)。

確度は66%（Arbiter v3.54）。中国国内基盤の強化が主因。グローバル展開の障壁（TikTok問題、規制リスク）は継続。ミラー・イメージング警告を尊重。

### クリエイターエコノミー特化（H-BTD-003、確度40%）

TikTok/Douyinのコンテンツ制作AIとAgent技術を融合する。CapCut（MAU 300M超、モバイル動画編集シェア81%）が配布チャネルとして機能。

確度は40%（Arbiter v3.54）。Seedance 2.0の透かし/IPガードレール実装は著作権制約への対応進展。中国規制（子供向け没頭型AI禁止、デジタルヒューマン規制）[INFO-022](../Information/2026-04-06/collected-raw.md#INFO-022)は新たな制約。

## 強みと弱み

ByteDanceの強みは、確認済みの価格競争力（10倍安）、中国市場の圧倒的基盤（日次トークン120兆、DAU 1.45億、MAU 2.26億）[INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)、Seeduplexによる音声AIの質的転換 [INFO-056](../Information/2026-04-10/collected-raw.md#INFO-056)、**DeerFlow 2.0 MIT OSSで技術力の対外展示** [INFO-016](../Information/2026-04-19/collected-raw.md#INFO-016)、動画生成+配布チャネルの組み合わせ（Seedance + CapCut）、CozeのMCP対応 [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)。Moonton売却でAIへの経営資源集中を明確にした。

弱みは4つ。品質の独立検証が未完了で、エンタープライズ採用の障壁が残る。Seedance 2.0著作権訴訟（透かし/IPガードレールで対応進展）。TikTok問題の波及によるグローバル展開リスク。中国企業としての透明性の限界で、分析の確度自体が中程度にとどまる。中国規制（子供向け没頭型AI禁止、デジタルヒューマン規制）[INFO-022](../Information/2026-04-06/collected-raw.md#INFO-022)が新たな制約。

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Doubao使用量の推移 | 日次トークン120兆が維持・拡大するか | 2年で1000倍増加。DAU 1.45億 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024) |
| DeerFlow 2.0の開発者採用 | MIT OSSがグローバル開発者コミュニティに定着するか | LangGraph/LangChainベース・MCP対応・Claude Code統合 [INFO-016](../Information/2026-04-19/collected-raw.md#INFO-016) |
| Seed 2.0の独立第三者ベンチマーク | 品質同等が確認されれば価格破壊確定 | 自己報告のみ ([IND-011](../config/indicators.json)、elevated) |
| Seedance 2.0グローバル展開 | 透かし/IPガードレールで再開後の進捗 | API公開テスト中 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024) |
| Coze MCP対応の成果 | エコシステム拡張が定着するか | 企查查等と標準MCP接続 [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025) |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-19 | 鮮度タイムアウト対応（9日経過）。DeerFlow 2.0（MIT OSS・LangGraph/LangChain・Dockerサンドボックス・MCP対応・Claude Code統合）詳細を追加。H-BTD-001 66%・H-BTD-002 70%・H-BTD-003 40%を確認（変更なし） |
| 2026-04-10 | Seeduplex・豆包大モデル 1.8を追加。H-BTD-001 64→66%、H-BTD-002 69→70%、H-BTD-003 41→39%に更新 |
| 2026-04-06 | Doubao日次トークン120兆・Seedance 2.0 API・Coze MCP対応を追加 |
| 2026-03-24 | Seedance 2.0著作権訴訟・AI眼鏡中断・Moonton売却を追加 |
| 2026-03-09 | 豆包DAU 1.03億（+40%）・グローバルMAU 2位を反映 |
