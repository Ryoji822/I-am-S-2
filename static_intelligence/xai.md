# xAI → SpaceXAI

> 最終判断更新: 2026-07-19
> 全体確信度: 測定不能（H-XAI-004 indeterminate再分類）
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Cursor統合の詳細・Grok Gov Modelのガードレール内容も非公開。DL/API呼び出し量の時系列データが途絶状態。KIQ-MIL-001は27R連続完全不在。SpaceX-Pentagon数十億ドルAIデータセンター協議中（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）。エンタープライズ採用定量データ19R以上完全不在。H-XAI-004はindeterminate/52%維持（v4.40 DEGRADED・復帰条件未到達）
> 主参照: [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

FLI AI Safety Index Summer 2026がxAIにF評価（0.65点）を下した（[INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) A-1）。全9社中7位、前回4位からの転落であり、存在的安全性は全社最弱ドメインに固定された。Grok 4.5の詳細公開（[INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) A-3）とGrok BuildのOSS化（[INFO-014](../Information/2026-07-17/collected-raw.md#INFO-014) A-3）は技術的速度を示すが、コミュニティコンセンサスはGrokを「真剣な作業」の議論からほぼ除外している（[INFO-058](../Information/2026-07-17/collected-raw.md#INFO-058) C-2）。

[H-XAI-004](../config/hypotheses.json) はindeterminate/52%で±0%（v4.40 DEGRADED）。エンタープライズ採用定量データ（WAU/DAU・F500導入率・企業契約数）が19R以上完全不在であり、復帰条件（定量データ観測）未到達のためindeterminate維持。SpaceXがペンタゴンに数十億ドル規模のAIデータセンター容量提供を協議中である（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）。xAIはAnthropicが拒否した軍事利用に同意済みであり、連邦調達市場でのxAI優位が構造化しつつある。但し政府/軍事次元の地位強化はエンタープライズ採用の直接定量証拠ではない。[H-XAI-002](../config/hypotheses.json) は59% mediumで±0%。もしCursor統合後にGrok系コーディングツールの採用が定量で回復するか、DL減少傾向が3ヶ月以上継続すれば、コア判断が変わる。

## 1. コア判断

確信度は測定不能に置く。H-XAI-004のindeterminate再分類は、エンタープライズ採用定量データが19R以上完全不在である構造的制約を正直に反映したものである。FLIのF評価は、安全性が測定可能な競争次元として浮上した局面でxAIが米国主要ラボ中最下位に位置づけられたことを意味する。Grok 4.5とGrok Build OSSで開発速度は維持されているが、市場認知と安全評価の両面で構造的な遅れが確認された。

Grok 4.5はコーディング・エージェントタスク・知識作業に特化し、Cursorと共同トレーニングされた初のモデルとして7月8日にリリースされた（[INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) A-3）。価格は$2/M入力トークン。Grok Build（コーディングエージェント・CLI/TUI）はGitHubでOSS化され、1コマンドでインストール可能になった（[INFO-014](../Information/2026-07-17/collected-raw.md#INFO-014) A-3）。但し全リポジトリ（プライベートコード・シークレット含む）をGoogle Cloudバケットにアップロードするセキュリティ設計が指摘されており、ZDRモードの存在は一部緩和するが攻撃面拡大の事実は残る。ArenaエージェントリーダーボードでGrok 4.5は#13であり（[INFO-006](../Information/2026-07-17/collected-raw.md#INFO-006) C-2）、Codex 7Mユーザーとの乖離が鮮明である。

FLI AI Safety Index Summer 2026の完全スコアカード（9社・6ドメイン37指標）で、xAIはF評価（0.65点）を受けた（[INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) A-1）。前回4位から7位への転落であり、Anthropic C+（2.66）・OpenAI C（2.28）・DeepMind C（2.01）・Meta D+（1.32）との格差が拡大した。存在的安全性は全社最弱ドメインで、最高でもC-に留まる。FLIは別の報告書で「安全レトリックが実際行動を上回る」と指摘し、xAIをDeepMind/OpenAIと同列に扱った（[INFO-108](../Information/2026-07-17/collected-raw.md#INFO-108) A-1）。全社が軍事利用禁止の方針を転換した中で、xAIの位置づけは「レトリックを行動が下回る」事例として記録された。

SpaceXがペンタゴンにAIモデル実行向けデータセンター容量を数十億ドル規模で提供する協議中である（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）。WSJ/Reutersが2026年7月17日に報じた。SpaceXはxAIの親会社（2026年2月合併）であり、xAIはAnthropicが拒否した軍事利用に同意済みである。ペンタゴンの「AIファースト」戦闘態勢への移行で軍産複合体がテック/AI企業を急速統合しており、連邦調達市場でのxAI優位が構造化している。これは[H-XAI-004](../config/hypotheses.json)の政府/軍事次元での地位強化を示すが、エンタープライズ採用の直接定量証拠ではない。IND-030 critical条件2充実の独立因果チェーンの一つとして記録された。

[H-XAI-004](../config/hypotheses.json) はindeterminate/52%で±0%（v4.40 DEGRADED）。前回v4.39でmedium/52%からindeterminate/52%に再分類された（H-GOO-001と同一構造問題の一貫適用・二重基準是正）。v4.40はindeterminate運用ルール下（下位命題分解・方向性偏り記録・復帰条件明文化）で復帰条件未到達のため±0%。Grok 4.5性能証拠はavailability≠adoption制約付きで評価済みであり、SpaceX-Pentagonデータセンター協議（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）は政府/軍事次元での地位強化を示すがエンタープライズ採用定量データの構造的不在を覆さない。コミュニティコンセンサスでGrokが「真剣な作業」の議論から除外されている事実（[INFO-058](../Information/2026-07-17/collected-raw.md#INFO-058) C-2）は、技術性能の向上と市場認知の乖離を示す。availability≠adoptionの警告は7R以上継続している。

[H-XAI-002](../config/hypotheses.json) は59% mediumで±0%。Grok 4.5の$2/M入力トークン価格はC方向の材料だが、GLM-5.2がオープンウェイト#1・全体4位（[INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) B-3）で示される通り、中国OSS品質の向上が「低価格」独自性を侵食し続けている。DL 60%減（1月20M→4月8.3M）は未解決。59%以下が続けば次ラウンドでmedium→low審査がトリガーされる。

[H-XAI-001](../config/hypotheses.json)（Xデータ差別化）と [H-XAI-003](../config/hypotheses.json)（宇宙・製造業特化）は引き続き棄却（35%）で、新たな支持証拠は観測されていない。

## 2. 判断の重心 (Load-Bearing Reasoning)

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | FLI AI Safety Index: xAI F評価(0.65)・全9社中7位(4位→7位悪化)・存在的安全性は全社最弱ドメイン(最高C-) | [H-XAI-004](../config/hypotheses.json) 安全性次元での構造的劣位がA-1品質で確定。差別化次元の欠落が市場認知に影響 | A-1 | [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) |
| 高 | FLI報告書: 安全レトリック > 実際行動(DeepMind/OpenAI/xAI)・全社が軍事利用禁止方針を転換 | [IND-030](../config/indicators.json) critical強化。xAIの安全姿勢が第三者機関によって「レトリック超過」と評定された | A-1 | [INFO-108](../Information/2026-07-17/collected-raw.md#INFO-108) |
| 高 | Grok 4.5詳細: $2/M入力・Cursor共同トレーニング初・7/8リリース・「3番目の選択肢」位置づけ | [H-XAI-004](../config/hypotheses.json) フロンティア技術力の継続(C方向)。但しavailability≠adoption | A-3 | [INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) |
| 高 | Grok Build OSS化: GitHub公開・1コマンドインストール・全リポジトリCloudバケットアップロード問題 | [H-XAI-004](../config/hypotheses.json) エコシステム開放(C方向)とセキュリティ攻撃面拡大(I方向)の同時観測 | A-3 | [INFO-014](../Information/2026-07-17/collected-raw.md#INFO-014) |
| 高 | モデル比較コンセンサス: Fable 5/Opus 4.8/GPT-5.6 Solがトップティア・Gemini/Grokは「真剣な作業」でほぼ不在 | [H-XAI-004](../config/hypotheses.json) 技術性能向上と市場認知の乖離。ベンチマーク→実用性比較への移行でGrok劣位 | C-2 | [INFO-058](../Information/2026-07-17/collected-raw.md#INFO-058) |
| 高 | Grok 4.5 Arenaエージェント#13・Codex 7Mユーザーとの乖離 | [H-XAI-004](../config/hypotheses.json) エージェント領域での採用格差。Cursor統合後の固有採用データ不在 | C-2 | [INFO-006](../Information/2026-07-17/collected-raw.md#INFO-006) |
| 高 | SpaceX-Cursor $60B Q3クローズ確認・xAI $20B Series E・xAI評価額$230B(Series E) | [H-XAI-004](../config/hypotheses.json) 資本基盤確定。但しCursor成長はClaude/GPT由来の価値。Grok固有採用分離不能 | B-2 | [INFO-058](../Information/2026-07-10/collected-raw.md#INFO-058) |
| 高 | Warren開示要求7社(SpaceX含む): DoD-7社AI統合協定(2026年5月)・競争入札法案 | KIQ-MIL-001文脈強化。SpaceXがAI軍事契約主要対象。[IND-030](../config/indicators.json) critical強化 | A-2 | [INFO-044](../Information/2026-07-10/collected-raw.md#INFO-044) |
| 高 | SpaceX-Pentagon数十億ドルAIデータセンター協議: AIモデル実行向け容量提供・xAI軍事利用同意済み・「AIファースト」戦闘態勢 | [H-XAI-004](../config/hypotheses.json) 政府/軍事次元地位強化。但しエンタープライズ採用定量証拠ではない。[IND-030](../config/indicators.json) critical独立因果チェーン | B-2 | [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) |
| 中 | GLM-5.2オープンウェイト#1・全体4位・$1.40/$4.40・MMLU全社>90%で飽和 | [H-XAI-002](../config/hypotheses.json) I方向。中国OSS品質向上で「低価格」独自性希薄化 | B-3 | [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) [INFO-060](../Information/2026-07-10/collected-raw.md#INFO-060) |
| 中 | DL 60%減(1月20M→4月8.3M)未解決・Cursor 41%→26%下落 | [H-XAI-002](../config/hypotheses.json) の停滞。59%以下でmedium→low審査トリガー | B-2 | 前回確認 [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |

## 3. 反証の閾値 (Falsification Triggers)

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| KIQ-MIL-001が完全回答に到達する（人間却下比率・誤標的率の公開） | 標的選定への直接関与度が確定する。partial→full回答転移で判断全面改訂。現在は27R連続完全不在 | 90日 | [IND-030](../config/indicators.json) |
| Cursor統合後にGrok系コーディングツールの採用（DL/API呼び出し量）が定量で回復する | [H-XAI-004](../config/hypotheses.json) のエンタープライズ獲得読みが上方修正される。90日で回復しなければ読みは弱まる | 90日 | [IND-027](../config/indicators.json) |
| エンタープライズ採用定量データ（WAU/DAU・F500導入率・企業契約数）が初めて公開される | [H-XAI-004](../config/hypotheses.json) の核心パラメータ不在（19R+）が解消し、確度評価の基盤が変わる | 次回 | [IND-027](../config/indicators.json) |
| DL減少傾向が3ヶ月以上継続する（1月→4月→7月） | [H-XAI-002](../config/hypotheses.json) の59%根拠が崩れ、medium→low移行が確定する | 90日 | [IND-013](../config/indicators.json) |
| Grokが次期AAIIで上位3社以内に上昇する、またはコミュニティコンセンサスでトップティア入りする | フロンティア差別化の残存が強化され、[H-XAI-002](../config/hypotheses.json) のC方向確定。「真剣な作業」からの除外が覆る | 90日 | [IND-025](../config/indicators.json) |
| FLI次回評価でxAIがD以上に改善する、または安全チーム設置・危険能力評価の公開 | [H-XAI-004](../config/hypotheses.json) の安全性次元での劣位が緩和される | 180日 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説 (Active Hypotheses)

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-XAI-002](../config/hypotheses.json) | 価格競争力でシェアを獲得する | 59% medium | ±0%。Grok 4.5 $2/M入力(INFO-004 A-3)はC方向。但しGLM-5.2 OSS#1全体4位(INFO-057 B-3)で中国OSS品質向上継続。API価格高値から約20%下落(INFO-052 A-2)で「低価格」独自性更に希薄化。DL 60%減未解決。59%以下が続けば次ラウンドでmedium→low審査 | [INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) | [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) [INFO-052](../Information/2026-07-10/collected-raw.md#INFO-052) 前回 [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤として展開し、Xデータ依存なしでエンタープライズ市場シェアを獲得する | 52% indeterminate | ±0%（v4.40 DEGRADED）。前回v4.39でmedium→indeterminate再分類（H-GOO-001と同一構造問題の一貫適用）。復帰条件（定量データ観測）未到達のためindeterminate維持。SpaceX-Pentagon数十億ドルAIデータセンター協議(INFO-043 B-2)は政府/軍事次元C方向。FLI F評価0.65(A-1)・CLIセキュリティ問題(A-3)がI方向。Grok 4.5技術詳細(INFO-004 A-3)・Grok Build OSS(INFO-014 A-3)はC方向。コミュニティコンセンサスで「真剣な作業」除外(INFO-058 C-2)。エンタープライズ採用定量データ19R以上完全不在・I=0継続 | [INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) [INFO-014](../Information/2026-07-17/collected-raw.md#INFO-014) [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) [INFO-108](../Information/2026-07-17/collected-raw.md#INFO-108) [INFO-058](../Information/2026-07-17/collected-raw.md#INFO-058) (エンタープライズ採用定量データ19R不在) |
| [H-XAI-001](../config/hypotheses.json) | （棄却）Xデータ活用でリアルタイム特化を差別化する | 35% | 42R以上にわたりXデータ活用の直接証拠不在。xAI→SpaceXAI統合で観測の意義自体が低下 | （なし） | 42R以上の証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | （棄却）SpaceX統合で宇宙・製造業特化AIを展開する | 35% | 43R以上にわたり直接的特化AI製品証拠不在。Colossusは汎用インフラ扱い | （なし） | 43R以上の特化製品証拠不在 |

## 5. 監視指標 (Watch List)

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度・Grok API/DL動向 | 実被害A-2報告でcritical | high/rising。Grok Build CLI全リポジトリアップロード問題(INFO-022 C-3)。CSA 10件インシデント7週間(INFO-019 B-3)。DL 60%減は未解決(1月→4月)。新規A-2実被害なし。critical移行条件未到達 | 2026-07-19 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・フロンティア性能差 | 性能差ベンダー間5%未満でhigh | elevated/stable。GPT-5.6 Sol ARC-AGI-3 7.78%(INFO-085 C-3)。Grok 4.5 Cursor共同トレーニング(INFO-004 A-3)だがコミュニティコンセンサスで「真剣な作業」除外(INFO-058 C-2)。量的向上継続・「真の理解」未解決 | 2026-07-19 |
| [IND-026](../config/indicators.json) | エージェント本番到達率 | 3ソース以上で完了率<10% | high/rising。70%マーケティング本番(INFO-026 B-2)・BCG 84%/30%(INFO-027 B-2)・LeanData 93%/31%(INFO-029 B-3)・165Kレイオフ(INFO-073 C-3)。24+独立ソース。期待-実態ギャップ維持 | 2026-07-19 |
| [IND-027](../config/indicators.json) | エコシステム標準化・Grokスタック採用 | 囲い込み反転 | high/rising。MCP 2026-07-28 RC(INFO-014 A-3)・AAIF MCPA(INFO-015 A-3)・Grok Build OSS GitHub公開(INFO-014 A-3)。Cursor統合後の本番到達は未計測 | 2026-07-19 |
| [IND-028](../config/indicators.json) | AGI到達度 | 主観-客観乖離 | high/rising。Hassabis 2029-2031(INFO-086 B-2)・Kokotajlo 50% by 2029(INFO-087 C-3)・UN科学パネル予備報告(INFO-107 A-2)。RSI具体化と客観ベンチマーク限界の同時進行 | 2026-07-19 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 物理的制約の顕在化 | high/rising。AI=全スタートアップ資金50%($2023億)(INFO-060 B-2)・Meta $50B DC(INFO-062 B-2)・NY州DC凍結(INFO-110 B-2)。資本流入加速・物理的制約ギャップ確定的 | 2026-07-19 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 | （critical到達済み） | **critical/rising**。SpaceX-Pentagon数十億ドルAIデータセンター協議（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）・米初の自律型戦闘攻撃実行（[INFO-002](../Information/2026-07-19/collected-raw.md#INFO-002) B-3）・Pentagon移行期間6ヶ月確認(INFO-072 B-1)・FLI軍事AI転動(INFO-038 A-1)・Warren 7社照会・DoD $134億予算・中国AI agent規制7/15施行(INFO-038 B-1)。「安全レトリック > 実際行動」(INFO-108 A-1)。KIQ-MIL-001 27R不在。条件2充実史上最大水準 | 2026-07-19 |

## 6. 変化履歴 (Decision History)

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-19 | ターゲット編集。SpaceX-Pentagon数十億ドルAIデータセンター協議（[INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) B-2）を新規反映。xAI軍事利用同意・連邦調達市場でのxAI優位構造化。[H-XAI-004](../config/hypotheses.json) indeterminate/52% ±0%（v4.40 DEGRADED・復帰条件未到達）。KIQ-MIL-001 26R→27R。IND-030 critical強化（自律型戦闘攻撃初確認・SpaceX-Pentagon協議・SCR指定米国企業初）。Arbiter v4.40 DEGRADED | [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 59%（±0%） |
| 2026-07-18 | ターゲット編集。[H-XAI-004](../config/hypotheses.json) medium→indeterminate再分類（H-GOO-001と同一構造問題の一貫適用・二重基準是正・Arbiter独自判断）。KIQ-MIL-001 25R→26R。IND-030 criticalにPentagon移行期間確認(INFO-072 B-1)・中国AI agent規制7/15施行を追加反映。Arbiter v4.39 COMPLETE | [Arbiter v4.39](../state/arbiter-2026-07-18.md) | H-XAI-004 medium→indeterminate/52% |
| 2026-07-17 | 全面書き直し（7日freshness timeout）。FLI F評価0.65・4位→7位悪化(INFO-107 A-1)・安全レトリック>実際行動(INFO-108 A-1)・Grok 4.5詳細(INFO-004 A-3)・Grok Build OSS(INFO-014 A-3)・モデルコンセンサスでGrok除外(INFO-058 C-2)を新規反映。H-XAI-004 54→52%(v4.34-v4.35適用分を修正) | [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) [INFO-108](../Information/2026-07-17/collected-raw.md#INFO-108) [INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) [INFO-014](../Information/2026-07-17/collected-raw.md#INFO-014) | H-XAI-002 59%(±0%)・H-XAI-004 54→52% |
| 2026-07-10 | 全面書き直し。Grok 4.5発表(INFO-018 A-3)・AAII 4位・Snorkel最強29%(INFO-056 A-2)・SpaceX-Cursor $60B Q3クローズ確認(INFO-058 B-2)・Warren開示要求7社含む(INFO-044 A-2)を反映 | [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) [INFO-056](../Information/2026-07-10/collected-raw.md#INFO-056) | H-XAI-002 59%(±0%)・H-XAI-004 54%(±0%) |
| 2026-07-07 | ターゲット編集。Grok in Project Maven統合確認(A-1)・Carnegie詳細レポート(A-1)・Cursor $2B ARR(B-2)・Voice Agent Builder(C-3)・GLM 5.2 OSS#1を反映。[H-XAI-004](../config/hypotheses.json) 57→54% | [INFO-064](../Information/2026-07-07/collected-raw.md#INFO-064) [INFO-067](../Information/2026-07-07/collected-raw.md#INFO-067) | H-XAI-004 57→54%・H-XAI-002 59%(±0%) |
| 2026-06-29 | 全面書き直し。KIQ-MIL-001部分回答転移・11共同創業者退社・選択的執行受益者 | [INFO-004](../Information/2026-06-29/collected-raw.md#INFO-004) [INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058) | H-XAI-002 59% ±0%・H-XAI-004 57% ±0% |
| 2026-06-24 | 全面書き直し。SpaceX Cursor $60B買収のA-1品質確定。[H-XAI-004](../config/hypotheses.json) 55→57% | [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) | H-XAI-004 55→57%・H-XAI-002 59%据え置き |
| 2026-06-18 | 全面書き直し。SpaceX-Cursor $60B買収・Grok 4.3 GA・Grok Gov Model軍事展開の二軸再編 | [INFO-054](../Information/2026-06-18/collected-raw.md#INFO-054) | H-XAI-002 59%・H-XAI-004 55%据え置き |

## 7. ブラインドスポット (Known Unknowns)

- KIQ-MIL-001の人間却下比率が27R連続完全不在。27Rの不在は「中立」ではなく「構造的に非対称」と評価する基準（v4.31策定）が適用されている。AI推奨の却下率そのものが不在である以上、観測されていないリスクを不在と断定する正常性バイアスの逆方向リスクがある。
- FLIのF評価（0.65）は、存在的安全性・ガバナンス・現在の危害・安全フレームワーク・情報共有の全ドメインで低評価であることを示す。但し「検出は防止ではない」（FLI報告書）という制約があり、評価の低さと事故確率の間の因果関係は直接的ではない。
- Grok 4.5の技術性能向上（Cursor共同トレーニング・$2/M入力）とコミュニティコンセンサスでの除外（「真剣な作業」でほぼ不在）の乖離が、何に起因するかが判明していない。ベンチマーク成績と実用性のギャップなのか、ブランド・エコシステム・信頼の問題なのか。
- Grok Build OSS化のセキュリティ設計（全リポジトリをCloudバケットにアップロード）が、エンタープライズ採用にどう影響するかが未測定。ZDRモードの存在は一部緩和するが、初期印象としてのセキュリティ懸念は残る。
- Cursor $2B ARRの成長がGrok固有の価値によるものか、Claude/GPT APIへのアクセスによるものかの分離が不可能。買収完了後のGrok統合戦略が未公開。
- エンタープライズ採用定量データが19R以上完全不在。この不在を「不在=不採用」と解釈するか「非公開=戦略的」と解釈するかで確度評価が大きく変わる。累積ペナルティ論理の妥当性自体が検証不能。
- DL 60%減（1月→4月）が、Cursor買収前のCursor市場シェア下落とどう関係するか不明。7月データでの更新が必要だが入手できていない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) | FLI AI Safety Index完全スコアカード: xAI F(0.65)・4位→7位悪化・存在的安全性全社最弱(A-1) |
| [INFO-108](../Information/2026-07-17/collected-raw.md#INFO-108) | FLI報告書: 安全レトリック>実際行動(DeepMind/OpenAI/xAI)・全社軍事利用禁止転換(A-1) |
| [INFO-004](../Information/2026-07-17/collected-raw.md#INFO-004) | Grok 4.5詳細: $2/M入力・Cursor共同トレーニング初・7/8リリース(A-3) |
| [INFO-014](../Information/2026-07-17/collected-raw.md#INFO-014) | Grok Build OSS: GitHub公開・CLI/TUI・全リポジトリCloudバケットアップロード問題(A-3) |
| [INFO-058](../Information/2026-07-17/collected-raw.md#INFO-058) | モデル比較コンセンサス: Fable/Opus/GPT-5.6 Solトップティア・Gemini/Grok除外(C-2) |
| [INFO-006](../Information/2026-07-17/collected-raw.md#INFO-006) | Codex 7Mユーザー・Grok 4.5 Arena #13(C-2) |
| [INFO-058](../Information/2026-07-10/collected-raw.md#INFO-058) | SpaceX-Cursor $60B Q3クローズ確認・xAI $20B Series E(B-2) |
| [INFO-044](../Information/2026-07-10/collected-raw.md#INFO-044) | Warren開示要求7社(SpaceX含む): DoD-7社AI統合協定・競争入札法案(A-2) |
| [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) | GLM-5.2: オープンウェイト#1・全体4位・OSS-クローズドギャップ縮小(B-3) |
| [INFO-052](../Information/2026-07-10/collected-raw.md#INFO-052) | AI API価格崩壊: トークン指数高値から約20%下落(A-2) |
| [INFO-060](../Information/2026-07-10/collected-raw.md#INFO-060) | 2026年重要7ベンチマーク: MMLU 90%超で飽和(C-3) |
| [INFO-085](../Information/2026-07-17/collected-raw.md#INFO-085) | AI Safety Index概要: Anthropic最高・5/6首位・GPT-5.6リリース(A-1) |
| [INFO-043](../Information/2026-07-19/collected-raw.md#INFO-043) | SpaceX-Pentagon数十億ドルAIデータセンター協議・xAI軍事利用同意・「AIファースト」戦闘態勢(B-2) |
| [INFO-002](../Information/2026-07-19/collected-raw.md#INFO-002) | 米初の自律型戦闘攻撃: シー・ドローン対イラン潜水艦基地・DoD 3000.09は禁止ではなく「適切な人間の判断」要求のみ(B-3) |
| [Arbiter v4.40](../state/arbiter-2026-07-19.md) | 確度評価の完全根拠 |
