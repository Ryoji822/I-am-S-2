# Examples and Evals

## example 1: CyberACE 向け AI 解説

### input
- source_kind: notes
- goal: explain
- audience: cyberace
- topic: llm vendor の違い

### selected modules
- 01-core-model
- 10-audience-cyberace
- 12-audience-ai-beginner
- 20-task-generate
- 30-anti-slop
- 31-evaluation-rubric
- 32-output-patterns

### expected shape
- 実務の詰まりから始まる
- vendor の勝ち負けではなく、用途差で整理する
- `どこで人が見るか` が残る

## example 2: 経営向け提案メモへの改稿

### input
- source_kind: existing-draft
- goal: decide
- audience: cyberagent-senior
- medium: memo

### selected modules
- 01-core-model
- 11-audience-cyberagent-senior
- 21-task-rewrite
- 30-anti-slop
- 31-evaluation-rubric
- 32-output-patterns

### expected shape
- tutorial ではなく判断材料になる
- 推奨案と保留事項が分かれる
- generic ending が消える

## example 3: deepresearch の要点変換

### input
- source_kind: research-pack
- goal: summarize
- audience: mixed
- output_length: staged

### selected modules
- 01-core-model
- 12-audience-ai-beginner
- 22-task-summarize-compress
- 23-task-deepresearch-transform
- 30-anti-slop
- 31-evaluation-rubric
- 32-output-patterns
- 34-integration-notes

### expected shape
- core/support/develop が分かれる
- gist が一文で立つ
- 矛盾が消えない
- staged build で section 単位に展開する

## example 4: 一般向け説明記事

### input
- source_kind: research-output
- goal: explain
- audience: general
- medium: article

### selected modules
- 01-core-model
- 13-audience-general
- 24-task-explain-article
- 30-anti-slop
- 31-evaluation-rubric
- 32-output-patterns

### expected shape
- 結論先出し→定義→理由→例→まとめ→次の手
- 1段落1アイデア
- 読後に「できること」が明確

## example 5: 教育コンテンツ

### input
- source_kind: training-material
- goal: teach
- audience: cyberace + ai-beginner
- medium: training-note

### selected modules
- 01-core-model
- 10-audience-cyberace
- 12-audience-ai-beginner
- 25-task-education
- 30-anti-slop
- 31-evaluation-rubric
- 32-output-patterns

### expected shape
- 課題→既知の呼び起こし→見本→練習→振り返り
- 1手順3〜5ステップ
- フロー状態設計（易→やや難）

## example 6: UX マイクロコピー

### input
- source_kind: ui-spec
- goal: ux-copy
- audience: general
- medium: microcopy

### selected modules
- 01-core-model
- 13-audience-general
- 27-task-ux-microcopy
- 30-anti-slop
- 31-evaluation-rubric

### expected shape
- 状態→何が起きた→どう直す
- 動詞中心、明確さ最優先
- 30字以内
