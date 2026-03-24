# Task Module: Rewrite and Reframe Existing Content

## 使いどころ

既存の原稿、メモ、記事、提案文、説明文を、別の読み手や別の用途向けに組み替えるときに使う。

## preservation ladder

### 絶対に守る
- 主張
- 根拠
- 条件つきの留保
- 重要な actor
- 因果の橋
- 最終的な判断や依頼

### 変えてよい
- 順番
- 抽象度
- 段落構成
- lead
- 見出し
- 例
- 語り口

### 追加してよい
- audience に必要な bridge
- 誤解を防ぐ caveat
- 短い例
- 論理の接続語

## 手順

1. 原稿の failure mode を診断する
2. 読み手差分を明文化する
3. 何を守り、何を変えるか書く
4. 新しい構造を置く
5. rewrite する
6. 元原稿と照合する
7. anti-slop pass をかける

## よくある failure mode

- 情報が均質で山がない
- 結論を急ぎすぎる
- 抽象語が続く
- 読み手が主役になっていない
- 事実はあるが意味がない
- かっこいい言い換えで内容が薄くなっている

## rewrite delta の書き方

```yaml
rewrite_delta:
  from_audience: ...
  to_audience: ...
  keep: []
  reduce: []
  add_bridges: []
  add_examples: []
  replace_opening_with: ...
  replace_closing_with: ...
```

## compare step

rewrite 後に次を確認する。

- 元の主張が変質していないか
- 不確実性が断定に変わっていないか
- audience に不要な前提が残っていないか
- 元よりも理解しやすい順番になったか
