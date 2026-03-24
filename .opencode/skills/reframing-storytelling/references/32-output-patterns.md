# Output Patterns

## 使い方

この file は、本文の型を選ぶために使う。厳密な固定 template ではなく、役割が明確な default pattern 集として使う。

## pattern 1: understanding note

向いている場面:
- AI 初学者向け説明
- 研修ノート
- 誤解を解く説明

構造:

```markdown
# title

## いま起きている誤解 or 詰まり
## その見方では足りない理由
## どう捉え直すと理解しやすいか
## 具体例
## 例が意味すること
## まず何を試すか
```

## pattern 2: decision memo

向いている場面:
- 経営向け、提案向け、判断依頼

構造:

```markdown
# title

## 判断したいこと
## いまの問題
## なぜ今重要か
## 選択肢と比較軸
## 推奨案
## リスク・保留事項
## 次の判断
```

## pattern 3: proposal narrative

向いている場面:
- 社内提案
- 新規提案のたたき台

構造:

```markdown
# title

## 現状の詰まり
## なぜ今のやり方では足りないか
## 提案の考え方
## 具体策
## 根拠
## 実装条件
## 期待値と限界
## 依頼したい判断
```

## pattern 4: rewrite with design appendix

向いている場面:
- 既存原稿の再構成を見せたい
- 本文だけでなく設計変更も残したい

構造:

```markdown
# title

## rewritten body
...

---

## design appendix
- throughline:
- selected_modules:
- kept:
- changed:
- quality_gate:
```

appendix はユーザーが求めたときだけ出す。

## pattern 5: staged longform build

向いている場面:
- `max_output_tokens` が厳しい
- 長い記事や資料原稿

出し方:

### turn 1
```yaml
build_state:
  throughline: ...
  sections:
    - ...
  selected_modules: ...
  next_sections:
    - ...
```

### turn 2+
- section を2〜3個ずつ展開する
- 各 turn の末尾に `remaining_sections` を残す
- 前の section を毎回書き直さない

## pattern 6: slide talk track

向いている場面:
- スライド本文ではなく、話す流れを作る

構造:

```markdown
# title

## slide 1: 何を問題として置くか
## slide 2: なぜ従来理解では足りないか
## slide 3: 新しい見方
## slide 4: 根拠
## slide 5: 判断と次の一歩
```
