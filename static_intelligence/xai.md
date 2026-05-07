# xAI

> 最終判断更新: 2026-05-02
> 全体確信度: 中
> 情報非対称性: Grok の正確性ベンチマークは他社比較で未公開。X データと AI 学習の寄与が分離できない
> 主参照: hypotheses.json#H-XAI-001/002/003/004, indicators.json#IND-017/006/001/025/030

## 0. 一文要約

我々は xAI を、**価格優位と政府採用で汎用 AI 基盤の地位を固めつつある企業**と読んでいる。最大の根拠は Pentagon GenAI.mil への統合 (120万ユーザー・10万エージェント) と Grok 4.3 の $1.25/$2.50 per M tokens という価格水準だ。ただし当初の差別化軸だった X データ活用仮説 (H-XAI-001) は29日以上証拠不在で確度 42% に低下しており、物理世界統合仮説 (H-XAI-003) はすでに low に再分類された。もし Grok の価格優位が他社追随で消えるか、X データアクセスポリシーが制限される観測が出れば、現在の読みは根本から見直す。

## 1. コア判断

xAI の現状を一言で言えば、**当初の差別化軸が証拠不在で劣化しながら、別の軸が台頭している企業**だ。

X (Twitter) データを独占活用してリアルタイム性で差別化するという当初の仮説は、29日以上新規証拠が観測されないまま確度 42% に沈んだ。SpaceX との物理世界統合も同様で、29日以上支持証拠が途絶え、確度 40% で low に再分類された。これらの劣化が示すのは、仮説が崩れたという確定ではなく、「監視しているが答えが出ていない」状態が続いているという事実だ。

その間に台頭したのが、汎用 AI 基盤として政府・企業市場を取るという仮説 (H-XAI-004、55%) と、純粋な価格競争での差別化 (H-XAI-002、65%) だ。Pentagon GenAI.mil でのGrok統合は、国防省が120万ユーザー規模のプラットフォームで実際に使い始めたことを意味する。Grok 4.3 は CaseLaw v2 首位・CorpFin 首位という業種特化の実績を示し、法律・金融でのエンタープライズ競争力はXデータと無関係に成立しつつある。

ただし、この読みにはまだ穴がある。エンタープライズ市場シェアの定量データが手元にない。価格の強さは DeepSeek V4 ($1.74/$3.48) が侵食しつつある。Musk 一人が Tesla・SpaceX・Neuralink・xAI を束ねる集中リスクも継続している。H-XAI-004 の確度が 55% 止まりなのは、「取りつつある」という方向性は見えるが、「取った」という確定が出ていないからだ。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Pentagon GenAI.mil に Grok が統合、120万ユーザー・10万エージェント。軍事 Grok 利用に「blank check」 | 汎用 AI 基盤仮説 (H-XAI-004) の最強支持証拠。政府が規模で採用したことの確認 | A-2 | [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) [INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023) |
| 高 | Grok 4.3: $1.25/$2.50 per M tokens。GPT-5.5 ($5/$30) の約1/4。Grok 4.2 比で入力 40%・出力 60% 安い | 価格競争仮説 (H-XAI-002) の直接根拠。構造コストがSpaceXインフラで担保されている | A-3 | [INFO-006](../Information/2026-05-02/collected-raw.md#INFO-006) |
| 高 | Grok 4.3: CaseLaw v2 #1 (79.3%) · CorpFin #1。GDPval-AA Elo 1500 | X データ依存なしでの業種特化競争力。エンタープライズ取得の方向性を裏付ける | A-3 | [INFO-006](../Information/2026-05-02/collected-raw.md#INFO-006) |
| 中 | Shift4 Payments が ChatGPT から Grok へ全面移行。JAMA 臨床推論 0.78 | 民間企業・医療の第三者採用実績。Pentagon 以外の汎用化証拠 | B-2 | [INFO-016](../Information/2026-04-20/collected-raw.md#INFO-016) [INFO-076](../Information/2026-04-20/collected-raw.md#INFO-076) |
| 中 | H-XAI-001 が29日以上証拠不在で 42% に低下。H-XAI-003 が同様に 40% で low 再分類 | 当初の差別化軸が「観測限界」状態にある。H-XAI-004 が最有力に浮上した理由の裏 | B-3 | [INFO-007](../Information/2026-03-25/collected-raw.md#INFO-007) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| H-XAI-001 が次の30日 (2026-06-01 まで) でも新規証拠なし | X データ活用差別化が観測可能な差別化軸として機能していないことが確定し、low 再分類を実施する | 30日 | [IND-017](../config/indicators.json) |
| Grok の価格優位が他社追随で消える (DeepSeek V4 等が $1.00/$2.00 以下で提供) | H-XAI-002 (価格競争) が崩れ、価格以外の差別化軸が単独で成立するかを再検証する | 90日 | [IND-001](../config/indicators.json) |
| X のデータアクセスポリシー変更または API 課金強化で Grok の優先アクセスが消える | H-XAI-001 の観測根拠が構造ごと消え、差別化の前提が失われる | 60日 | [IND-017](../config/indicators.json) |
| Pentagon が Grok との契約を縮小・終了、または他社に切り替え | H-XAI-004 (汎用 AI 基盤) の最強支持証拠が崩れ、確度を大幅に引き下げる | 90日 | [IND-030](../config/indicators.json) |
| エンタープライズ市場シェア定量データで Grok が上位5社に入らないことが確認される | 「取りつつある」という方向性が否定され、H-XAI-004 の確度を 40% 以下に引き下げる | 180日 | [IND-006](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-XAI-004](../config/hypotheses.json) | 汎用 AI 基盤としてエンタープライズ・政府市場を獲得する | 55% | Pentagon統合・Shift4全面移行・JAMA 0.78・Grok 4.3業種特化首位が収束するが、市場シェア定量データ不在で上限キャップ継続 | [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) [INFO-006](../Information/2026-05-02/collected-raw.md#INFO-006) [INFO-016](../Information/2026-04-20/collected-raw.md#INFO-016) | 市場シェア定量データの不在、エンタープライズ後発の実績差 |
| [H-XAI-002](../config/hypotheses.json) | 価格競争力でシェアを獲得する | 65% | Grok 4.3 が $1.25/$2.50 で GPT-5.5 の約1/4。Colossus+SpaceX インフラが構造コストを担保。ただし価格と市場シェアの因果が未検証 | [INFO-006](../Information/2026-05-02/collected-raw.md#INFO-006) [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008) | [INFO-036](../Information/2026-05-02/collected-raw.md#INFO-036) DeepSeek V4 が $1.74/$3.48 で追随 |
| [H-XAI-001](../config/hypotheses.json) | X データ活用でリアルタイム特化を差別化する | 42% | x_search 内蔵が唯一の具体的証拠だが、29日以上連続で新規支持証拠が観測されない。40% 到達で low 再分類必須 (あと 2pt) | [INFO-007](../Information/2026-03-25/collected-raw.md#INFO-007) | 29日以上の証拠不在。Grok 4.3 の新証拠はすべて H-XAI-004 を支持し H-XAI-001 とは無関係 |
| [H-XAI-003](../config/hypotheses.json) | Tesla/SpaceX/X を統合して物理世界 AI を実現する | 40% | SpaceX合併・Tesla車両統合・Optimus V3統合という直接証拠が存在するが、29日以上 SpaceX統合の新規証拠が途絶え low 再分類実施済み | [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020) (STT/TTSの弱い傍証) | 29日以上の新規統合証拠不在。Pentagon SpaceX選出は政府軍事利用であり物理世界統合とは別軸 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-017](../config/indicators.json) | X データ独占活用が市場優位に直結するか | 新規証拠で elevated | x_search 内蔵のみ確認。29日以上新規証拠不在 | 2026-05-02 |
| [IND-006](../config/indicators.json) | Grok エージェントスタック採用状況 | 政府・企業の大規模採用で high | Pentagon GenAI.mil 10万エージェント稼働 | 2026-05-02 |
| [IND-001](../config/indicators.json) | Grok のベンチマーク性能がフロンティアに追いつくか | +5pt/期で high | GDPval-AA Elo 1500。ProofBench 11%、Vending-Bench 2 は回帰 | 2026-05-02 |
| [IND-025](../config/indicators.json) | 音声認識・ボイスクローニングでの競合優位 | WER 5% 以下で high | STT WER 6.9%。Custom Voices $3.00/時間 | 2026-05-02 |
| [IND-030](../config/indicators.json) | 軍事利用の blank check がリスク評価に与える影響 | 直接介入で high | Pentagon blank check 確認済み。用途制限なし | 2026-05-02 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-02 | H-XAI-001 42% に低下。H-XAI-003 low 再分類。H-XAI-004 最有力確定 | [INFO-006](../Information/2026-05-02/collected-raw.md#INFO-006) Grok 4.3 リリース。[INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) Pentagon 7社契約 SpaceX 選出 | 「X データ差別化が中核」 → 「証拠不在で劣化継続。汎用 AI 基盤が最有力」 |
| 2026-04-27 | H-XAI-001 45→42%。H-XAI-003 42→40% | [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) Pentagon GenAI.mil 統合確認 | 「差別化軸が複数あり評価中」 → 「政府採用で H-XAI-004 が急浮上」 |
| 2026-04-20 | H-XAI-004 (汎用 AI 基盤) を新設仮説として追加 | [INFO-016](../Information/2026-04-20/collected-raw.md#INFO-016) Shift4 全面移行。[INFO-076](../Information/2026-04-20/collected-raw.md#INFO-076) JAMA 0.78 | 「4仮説等重み」 → 「H-XAI-004 が新軸として台頭」 |
| 2026-04-17 | H-XAI-001 62→55%。H-XAI-003 58→52% | 複数連続での証拠不在で鮮度タイムアウト発動 | 「差別化仮説が半数超の確度」 → 「証拠劣化で確度低下開始」 |

## 7. ブラインドスポット

- Grok の正確性ベンチマークが他社比較で公開されていない。CaseLaw v2 首位・GDPval-AA Elo 1500 は xAI 発信のデータであり、独立第三者の再現確認がない。
- X からのデータ取得量と AI 学習への寄与が外部から分離できない。H-XAI-001 が「証拠不在」なのか「証拠が取れない構造」なのかが判別できず、観測限界と仮説棄却が混同するリスクがある。
- Elon Musk の経営優先度が Tesla・SpaceX・Neuralink・X・xAI に分散することの影響を定量化する手段がない。どの事業が優先されているかは発言から類推するしかなく、実際のリソース配分は不透明だ。
- SpaceX 軌道データセンター構想の進捗が外部から追跡できない。「2-3年以内に宇宙ベース計算を最低コストに」という主張が H-XAI-002 の長期コスト優位を支えているが、構想段階であることを超えた公開情報がない。
- Pentagon の「blank check」が実際の軍事利用でどこまで実行されているかが不明。利用量・用途・成果の開示がないため、政府採用の深さを評価できない。

## 付録: 直近30日の参照 Evidence

| Evidence | 用途 |
|---|---|
| [INFO-006](../Information/2026-05-02/collected-raw.md#INFO-006) | Grok 4.3 リリース詳細 (価格・ベンチマーク・弱点・Custom Voices) |
| [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) | Pentagon GenAI.mil 統合 (120万ユーザー・10万エージェント) |
| [INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023) | 軍事 Grok 利用の blank check 確認 |
| [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) | Pentagon 7社 AI 契約での SpaceX 選出 |
| [INFO-016](../Information/2026-04-20/collected-raw.md#INFO-016) | Shift4 Payments が ChatGPT から Grok へ全面移行 |
| [INFO-076](../Information/2026-04-20/collected-raw.md#INFO-076) | JAMA 臨床推論 Grok 4: 0.78 |
| [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020) | Grok STT/TTS API (WER 6.9%)、Grok 4.20 Heavy、Vertex AI |
| [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008) | Grok 4.20 Multi Agent 0309 価格・コンテキスト仕様 |
| [INFO-036](../Information/2026-05-02/collected-raw.md#INFO-036) | DeepSeek V4 $1.74/$3.48 — 価格優位への構造侵食リスク |
| [INFO-007](../Information/2026-03-25/collected-raw.md#INFO-007) | x_search 内蔵 — H-XAI-001 の現存する唯一の具体的支持証拠 |
| [Arbiter v3.66](../state/arbiter-2026-05-02.md) | 確度評価の完全根拠 (付録のみ参照) |
