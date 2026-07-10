# xAI → SpaceXAI

> 最終判断更新: 2026-07-10
> 全体確信度: 低
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Cursor統合の詳細・Grok Gov Modelのガードレール内容も非公開。DL/API呼び出し量の時系列データが途絶状態。KIQ-MIL-001は部分回答に転移したが、人間却下比率・誤標的率は依然非公開。エンタープライズ採用定量データ12R以上完全不在
> 主参照: [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

SpaceXAIがGrok 4.5を発表した（[INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) A-3）。MoEアーキテクチャでコーディング・エージェントタスク・知識作業に特化し、Grok Buildプラットフォームでエージェントループ・IDE統合・コーディングツールに直接統合可能である。Artificial Analysis Intelligence IndexでGrok 4.5は4位（54点）だが、Snorkelベンチマークでは29%平均合格率で最強の総合性能を記録した（[INFO-056](../Information/2026-07-10/collected-raw.md#INFO-056) A-2）。フロンティアモデル市場の第4席への到達は技術的存在感を示す。但し[H-XAI-004](../config/hypotheses.json) の核心命題（エンタープライズ市場獲得）の直接証拠ではない。

[H-XAI-002](../config/hypotheses.json) は59% mediumで±0%。[H-XAI-004](../config/hypotheses.json) は54% mediumで±0%。エンタープライズ採用定量データ（WAU/DAU・F500導入率・企業契約数）が12R以上完全に不在であり、Arbiter v4.31は±0%を維持した。もしCursor統合後にGrok系コーディングツールの採用が定量で回復するか、DL減少傾向が3ヶ月以上継続すれば、コア判断が変わる。

## 1. コア判断

確信度は低のまま置く。Grok 4.5の発表でフロンティアモデル市場への技術的到達が確認されたが、エンタープライズ採用という核心課題が解消していない。

Grok 4.5はMoEアーキテクチャでコーディング・エージェントタスク・知識作業に最適化された（[INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) A-3）。Grok Buildプラットフォームでエージェントループ、IDE統合、コーディングツールに直接統合可能であり、xAI APIでgrok-4.5が直接利用可能である。Artificial Analysis Intelligence IndexでGrok 4.5はFable 5・GPT-5.5・Opus 4.8に次ぐ4位（54点）にランクインした（[INFO-056](../Information/2026-07-10/collected-raw.md#INFO-056) A-2）。但しSnorkelベンチマーク（~2,000タスク）では29%平均合格率で「最強の総合性能」を示し、特定領域での技術的競争力を裏付けた。この結果は2つの含意を持つ。第一に、フロンティア差別化の残存を示し、SCN-004完全コモディティ化の反証となる。第二に、コストパフォーマンスでは圧倒的優位と報じられており、[H-XAI-002](../config/hypotheses.json) の価格競争力仮説を支持する。

SpaceX-Cursor $60B買収のQ3 2026クローズ予定が再確認された（[INFO-058](../Information/2026-07-10/collected-raw.md#INFO-058) B-2）。xAIがQ1 2026で$20B Series E調達を完了した事実も確認された。2026年に70社のユニコーン誕生のうち17社がAIであり、グローバルM&Aは$3Tに急増している。SpaceXAIの資本基盤（$1.25兆評価額+Cursor $60B+xAI $20B）が確定した。但しCursorの成長がClaude/GPT由来の価値であり、Grok固有のエンタープライズ採用を分離する定量データは不在である。

Sen. WarrenがPentagonと7社（SpaceXを含む）にAI契約条件の開示を要求した（[INFO-044](../Information/2026-07-10/collected-raw.md#INFO-044) A-2）。2026年5月にDoDがこれら企業と軍事ネットワーク向けAI統合協定を締結したことが判明した。SpaceXがAI軍事契約の主要対象に含まれていることは、KIQ-MIL-001の文脈を強化する。Warren法案はDoDにクラウド・AI・データインフラ契約の競争入札プロセス確立を義務付ける。

[H-XAI-002](../config/hypotheses.json) は59% mediumで±0%。Grok 4.5のSnorkel最強はC方向だが、GLM-5.2がオープンウェイト#1・全体4位（[INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) B-3）であり、OSSモデルの品質向上が「低価格」差別化を侵食し続けている。DL 60%減（1月20M→4月8.3M）は未解決である。59%以下が続けば次ラウンドでmedium→low審査がトリガーされる。

[H-XAI-004](../config/hypotheses.json) は54% mediumで±0%。Grok 4.5の発表はフロンティア技術力の証拠だが、エンタープライズ採用定量データ（WAU/DAU・F500導入率・企業契約数）が12R以上完全不在でありI=0の状態が継続している。累積ペナルティ論理（[H-ANT-002](../config/hypotheses.json) と対称適用）で前回-3%が適用済みであり、本ラウンドは新規確度変更材料なしとして±0%とした。

[H-XAI-001](../config/hypotheses.json)（Xデータ差別化）と [H-XAI-003](../config/hypotheses.json)（宇宙・製造業特化）は引き続き棄却（35%）で、新たな支持証拠は観測されていない。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Grok 4.5発表: MoE・コーディング/エージェント/知識作業特化・Grok Build統合・xAI API直接利用 | [H-XAI-004](../config/hypotheses.json) フロンティア技術力向上（C方向）。但しavailability≠adoption | A-3 | [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) |
| 高 | AAII: Grok 4.5 4位(54点)・Snorkel 29%平均合格率（最強総合）・コストパフォーマンス圧倒的 | [H-XAI-002](../config/hypotheses.json) 価格競争力支持（C方向）。[IND-025](../config/indicators.json) フロンティア差別化残存 | A-2 | [INFO-056](../Information/2026-07-10/collected-raw.md#INFO-056) |
| 高 | SpaceX-Cursor $60B Q3クローズ確認・xAI $20B Series E・2026年17社AIユニコーン・M&A $3T | [H-XAI-004](../config/hypotheses.json) 資本基盤確定。但しClaude/GPT由来の価値。Grok固有採用分離不能 | B-2 | [INFO-058](../Information/2026-07-10/collected-raw.md#INFO-058) |
| 高 | Warren開示要求7社（SpaceX含む）: DoD-7社AI統合協定(2026年5月)・競争入札法案 | KIQ-MIL-001文脈強化。SpaceXがAI軍事契約主要対象。[IND-030](../config/indicators.json) critical強化 | A-2 | [INFO-044](../Information/2026-07-10/collected-raw.md#INFO-044) |
| 高 | Grok in Project Maven: 米政府法廷文書で統合確認（前回確認） | 軍事AI基盤の制度化。政府チャネル持続性のA-1品質確定。但しエンタープライズ≠政府 | A-1 | 前回確認 [INFO-064](../Information/2026-07-07/collected-raw.md#INFO-064) |
| 高 | GLM-5.2オープンウェイト#1・全体4位・$1.40/$4.40・MMLU全社>90%で飽和 | [H-XAI-002](../config/hypotheses.json) I方向。中国OSS品質向上で「低価格」独自性希薄化 | B-3 | [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) [INFO-060](../Information/2026-07-10/collected-raw.md#INFO-060) |
| 高 | DL 60%減（1月20M→4月8.3M）未解決・Cursor 41%→26%下落 | [H-XAI-002](../config/hypotheses.json) の停滞。59%以下でmedium→low審査トリガー | B-2 | 前回確認 [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| 中 | Carnegie: 初の公表LLMサイバー攻撃・1オペレーター90エージェント（前回確認） | [IND-030](../config/indicators.json) critical妥当性更に強化。人間統制のスパン問題の定量化 | A-1 | 前回確認 [INFO-067](../Information/2026-07-07/collected-raw.md#INFO-067) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| KIQ-MIL-001が完全回答に到達する（人間却下比率・誤標的率の公開） | 標的選定への直接関与度が確定する。partial→full回答転移で判断全面改訂。現在は部分回答（16R連続不在） | 90日 | [IND-030](../config/indicators.json) |
| Cursor統合後にGrok系コーディングツールの採用（DL/API呼び出し量）が定量で回復する | [H-XAI-004](../config/hypotheses.json) のエンタープライズ獲得読みが上方修正される。90日で回復しなければ読みは弱まる | 90日 | [IND-027](../config/indicators.json) |
| エンタープライズ採用定量データ（WAU/DAU・F500導入率・企業契約数）が初めて公開される | [H-XAI-004](../config/hypotheses.json) の核心パラメータ不在（12R+）が解消し、確度評価の基盤が変わる | 次回 | [IND-027](../config/indicators.json) |
| DL減少傾向が3ヶ月以上継続する（1月→4月→7月） | [H-XAI-002](../config/hypotheses.json) の59%根拠が崩れ、medium→low移行が確定する | 90日 | [IND-013](../config/indicators.json) |
| Grok 4.5がAAIIで上位3社以内に上昇する | フロンティア差別化の残存が強化され、[H-XAI-002](../config/hypotheses.json) のC方向確定 | 90日 | [IND-025](../config/indicators.json) |
| DeepSeek等中国OSSモデルがGrok全系で全面的に勝利する | [H-XAI-002](../config/hypotheses.json) 価格競争力仮説の前提が崩壊する | 90日 | [IND-025](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-XAI-002](../config/hypotheses.json) | 価格競争力でシェアを獲得する | 59% medium | ±0%。Grok 4.5 Snorkel最強29%（INFO-056 A-2）はC方向。但しGLM-5.2 OSS#1全体4位（INFO-057 B-3）で中国OSS品質向上継続。API価格高値から約20%下落（INFO-052 A-2）で「低価格」独自性更に希薄化。DL 60%減未解決。59%以下が続けば次ラウンドでmedium→low審査 | [INFO-056](../Information/2026-07-10/collected-raw.md#INFO-056) [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) | [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) [INFO-052](../Information/2026-07-10/collected-raw.md#INFO-052) 前回 [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| [H-XAI-004](../config/hypotheses.json) | 汎用AI基盤としてエンタープライズ市場を獲得する | 54% medium | ±0%。Grok 4.5発表（INFO-018 A-3）でフロンティア技術力向上。AAII 4位・Snorkel最強（INFO-056 A-2）。SpaceX-Cursor $60B Q3クローズ確認（INFO-058 B-2）。Warren開示要求でSpaceXがAI軍事契約主要対象に含まれる（INFO-044 A-2）。但しエンタープライズ採用定量データ12R以上完全不在・I=0継続。availability≠adoption確証バイアス警告継続 | [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) [INFO-056](../Information/2026-07-10/collected-raw.md#INFO-056) [INFO-058](../Information/2026-07-10/collected-raw.md#INFO-058) | (エンタープライズ採用定量データ12R不在) |
| [H-XAI-001](../config/hypotheses.json) | （棄却）Xデータ活用でリアルタイム特化を差別化する | 35% | 42R以上にわたりXデータ活用の直接証拠不在。xAI→SpaceXAI統合で観測の意義自体が低下 | （なし） | 42R以上の証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | （棄却）SpaceX統合で宇宙・製造業特化AIを展開する | 35% | 43R以上にわたり直接的特化AI製品証拠不在。Colossusは汎用インフラ扱い | （なし） | 43R以上の特化製品証拠不在 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度・Grok API/DL動向 | 実被害A-2報告でcritical | high/rising。Grok Gov Model稼働・KIQ-MIL-001部分回答。Warren開示要求でSpaceX含む7社AI契約文脈（INFO-044 A-2）。DL 60%減は未解決（1月→4月）。新規A-2実被害なし。critical移行条件未到達 | 2026-07-10 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 性能差ベンダー間5%未満でhigh | elevated/stable。Grok 4.5 AAII 4位・Snorkel最強29%（INFO-056 A-2）。但しGLM-5.2 OSS#1全体4位（INFO-057）・MMLU全社>90%で飽和（INFO-060）・API価格約20%下落（INFO-052）。量的向上継続・「真の理解」未解決 | 2026-07-10 |
| [IND-026](../config/indicators.json) | エージェント本番到達率 | 3ソース以上で完了率<10% | high/rising。88%パイロット停滞（INFO-039 B-2）・97%コミット/18%デプロイ（INFO-026 B-2）。期待-実態ギャップ更に深化（13+独立ソース） | 2026-07-10 |
| [IND-027](../config/indicators.json) | エコシステム標準化・Grokスタック採用 | 囲い込み反転 | high/rising。MCP RC（INFO-021 A-3）・Grok 4.5 Grok Build統合（INFO-018 A-3）・OpenAI Agents SDK provider-agnostic（INFO-015 A-3）。Cursor統合後の本番到達は未計測 | 2026-07-10 |
| [IND-028](../config/indicators.json) | AGI到達度 | 主観-客観乖離 | high/rising。G7 Altman AGI討議（INFO-075 B-2）・AGI定義不合継続（INFO-076 B-2）・UN科学パネル発足（INFO-090 B-3）。RSI具体化と客観ベンチマーク限界の同時進行 | 2026-07-10 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 物理的制約の顕在化 | high/rising。DC $850Bリース+204% YoY（INFO-059 A-2）・ビッグテック$650B/$2B/day（INFO-063 B-3）・SpaceXAI評価額$1.25兆+Cursor $60B+xAI $20B（INFO-058 B-2）。資本流入加速 | 2026-07-10 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 | （critical到達済み） | **critical/rising**。Warren開示要求7社含む（INFO-044 A-2）・DPA脅迫確認・国連事務総長LAWS禁止要求（INFO-047 A-2）・human-in-loop法案（INFO-012 B-3）・June 2026 EO（INFO-050 A-2）。KIQ-MIL-001 16R不在。Carnegie 1オペレーター90エージェント問題（前回確認 A-1） | 2026-07-10 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-10 | 全面書き直し。Grok 4.5発表（INFO-018 A-3）・AAII 4位・Snorkel最強29%（INFO-056 A-2）・SpaceX-Cursor $60B Q3クローズ確認（INFO-058 B-2）・Warren開示要求7社含む（INFO-044 A-2）を新規反映。仮説確度は全て±0%据え置き。Arbiter v4.31 COMPLETE | [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) [INFO-056](../Information/2026-07-10/collected-raw.md#INFO-056) [INFO-058](../Information/2026-07-10/collected-raw.md#INFO-058) [INFO-044](../Information/2026-07-10/collected-raw.md#INFO-044) | H-XAI-002 59%(±0%)・H-XAI-004 54%(±0%) |
| 2026-07-07 | ターゲット編集。Grok in Project Maven統合確認(A-1)・Carnegie詳細レポート(A-1)・Cursor $2B ARR(B-2)・Voice Agent Builder(C-3)・GLM 5.2 OSS#1を反映。[H-XAI-004](../config/hypotheses.json) 57→54% | [INFO-064](../Information/2026-07-07/collected-raw.md#INFO-064) [INFO-067](../Information/2026-07-07/collected-raw.md#INFO-067) | H-XAI-004 57→54%・H-XAI-002 59%(±0%) |
| 2026-06-29 | 全面書き直し。KIQ-MIL-001部分回答転移・11共同創業者退社・選択的執行受益者 | [INFO-004](../Information/2026-06-29/collected-raw.md#INFO-004) [INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058) | H-XAI-002 59% ±0%・H-XAI-004 57% ±0% |
| 2026-06-24 | 全面書き直し。SpaceX Cursor $60B買収のA-1品質確定。[H-XAI-004](../config/hypotheses.json) 55→57% | [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) | H-XAI-004 55→57%・H-XAI-002 59%据え置き |
| 2026-06-18 | 全面書き直し。SpaceX-Cursor $60B買収・Grok 4.3 GA・Grok Gov Model軍事展開の二軸再編 | [INFO-054](../Information/2026-06-18/collected-raw.md#INFO-054) | H-XAI-002 59%・H-XAI-004 55%据え置き |

## 7. ブラインドスポット

- KIQ-MIL-001の人間却下比率が16R連続完全不在。Carnegie「1オペレーター90エージェント」は人間統制のスパン・オブ・コントロール問題を示唆するが、AI推奨の却下率そのものは不在。観測されていないリスクを不在と断定する正常性バイアスの逆方向リスクがある。
- Grok 4.5のAAII 4位・Snorkel最強29%が、エンタープライズ採用にどう結びつくかの因果チェーンが不在。技術性能の向上が自動的に市場採用に直結しないことは、39.5%横ばいのOpenAI企業採用率（INFO-064）でも確認されている。
- Project MavenへのGrok統合が、商業エンタープライズ市場でのGrok採用とどう関係するかが不明。政府チャネルの強化が商業チャネルを補完するのか、代替するのか、独立しているのかの判別ができない。
- Cursor $2B ARRの成長がGrok固有の価値によるものか、Claude/GPT APIへのアクセスによるものかの分離が不可能。買収完了後のGrok統合戦略が未公開。
- エンタープライズ採用定量データが12R以上完全不在。この不在を「不在=不採用」と解釈するか「非公開=戦略的」と解釈するかで確度評価が大きく変わる。累積ペナルティ論理の妥当性自体が検証不能。
- DL 60%減（1月→4月）が、Cursor買収前の Cursor市場シェア下落とどう関係するか不明。7月データでの更新が必要だが入手できていない。
- SpaceXAIの内部戦略が外部から観測不能。Cursor買収とGrok軍事展開は観測できても、SpaceX本体の投資判断なのかSpaceXAI内部の戦略なのか、Colossus 2の軍民分担がどうなっているかが判別不能。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-018](../Information/2026-07-10/collected-raw.md#INFO-018) | Grok 4.5発表: MoE・コーディング/エージェント/知識作業特化・Grok Build統合(A-3) |
| [INFO-056](../Information/2026-07-10/collected-raw.md#INFO-056) | AAII: Fable 5 > GPT-5.5 > Opus 4.8 > Grok 4.5(54点)・Snorkel最強29%・ARC Challenge GPT-5 96.3%(A-2) |
| [INFO-058](../Information/2026-07-10/collected-raw.md#INFO-058) | SpaceX-Cursor $60B Q3クローズ確認・xAI $20B Series E・2026年17社AIユニコーン(B-2) |
| [INFO-044](../Information/2026-07-10/collected-raw.md#INFO-044) | Warren開示要求7社(SpaceX含む): DoD-7社AI統合協定・競争入札法案(A-2) |
| [INFO-052](../Information/2026-07-10/collected-raw.md#INFO-052) | AI API価格崩壊: トークン指数高値から約20%下落・中国モデル米国企業使用増(A-2) |
| [INFO-057](../Information/2026-07-10/collected-raw.md#INFO-057) | GLM-5.2: オープンウェイト#1・全体4位・$1.40/$4.40・OSS-クローズドギャップ縮小(B-3) |
| [INFO-060](../Information/2026-07-10/collected-raw.md#INFO-060) | 2026年重要7ベンチマーク: MMLU 90%超で飽和・GPQA/SWE-bench/HLE/SimpleBench/ARC-AGI-2(C-3) |
| [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) | 企業AI採用率: Anthropic 41%首位・OpenAI 39.5%横ばい(B-3) |
| [INFO-075](../Information/2026-07-10/collected-raw.md#INFO-075) | G7: Altman/Hassabis/Amodei AGI討議・強いAGI 2031-2035(B-2) |
| [Arbiter v4.31](../state/arbiter-2026-07-10.md) | 確度評価の完全根拠 |
