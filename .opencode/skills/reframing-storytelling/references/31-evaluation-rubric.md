# Evaluation Rubric

## 目次
- 7項目 rubric
- quick gate
- failure signatures
- evaluation scenarios

## 7項目 rubric

各項目を 1〜5 で見る。重要なのは点数より、どこが壊れているかを見つけること。

### 1. audience fit
- 読み手の共通知に合っているか
- 読み手が知りたい順で並んでいるか

### 2. structural clarity
- 今どこにいて、どこへ向かうかが読めるか
- section 間に役割差があるか

### 3. causal continuity
- `なぜそうなるか` の橋が切れていないか
- 結果だけを飛ばしていないか

### 4. compression fidelity
- 短くしても gist が残っているか
- 条件つき主張が断定に変わっていないか

### 5. common-ground calibration
- 省略が早すぎないか
- 不要な一般論が長すぎないか

### 6. anti-slop quality
- 平均的な lead / body / ending に流れていないか
- 抽象名詞の連打や安い戦略語がないか

### 7. actionability
- 読後に何を理解し、何を判断し、何を試すかが見えるか

### 8. module checklist compliance
- 読み込んだ style overlay の最終チェック項目をすべて通過しているか
- 読み込んだ audience module の quality gate を通過しているか
- task module の failure modes に該当していないか

## quick gate

次の問いに全部 yes で通したい。

- 読み手が `要するに何か` を言い直せるか
- 読み手が `なぜそう言えるか` を追えるか
- 読み手が `自分に何が関係あるか` を感じられるか
- 最後に `で、どうするか` が残るか
- 文章が `どこかで見た AI 文` に見えないか
- 読み込んだ全モジュールの最終チェック・quality gate を通過しているか

## failure signatures

- 読んだあと gist を口頭で説明できない
- 事実はあるが、意味が残らない
- 一見整っているが、読み手が前に進まない
- 反対条件や留保が消えている
- AI 初学者向けなのに用語が置き去り
- シニア向けなのに事業判断材料がない

## evaluation scenarios

### scenario 1: CyberACE 向け AI 解説

入力条件:
- audience: cyberace
- task: explain or summarize
- topic: llm / agent / vendor difference

期待挙動:
- 用語を置き去りにしない
- 実務にどう効くかが先に来る
- 苦手と human check が残る
- 明日試す一歩がある

### scenario 2: CyberAgent シニア向け判断メモ

入力条件:
- audience: cyberagent-senior
- task: rewrite or proposal
- topic: ai 導入, 戦略, 組織実装

期待挙動:
- 事業課題から始まる
- トレードオフがある
- 推奨案と保留事項が分かれる
- tutorial tone がない

### scenario 3: deepresearch の再構成

入力条件:
- source: long research pack
- task: deepresearch transform
- audience: any

期待挙動:
- throughline が立っている
- core/support/develop が整理される
- source の矛盾や条件が消えない
- 羅列ではなく理解経路になる
