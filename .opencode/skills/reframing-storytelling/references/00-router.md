# Router

## 目次
- 基本方針
- working brief の作り方
- audience module の選び方
- task module の選び方
- output module の選び方
- style overlay の選び方
- theory module を追加で読む条件
- source file を追加で読む条件
- module selection examples
- build state テンプレート

## 基本方針

この skill は、最初から全部の reference を読ませない。

常に読むのは次の4つだけでよい。

1. `01-core-model.md`
2. `30-anti-slop.md`
3. `31-evaluation-rubric.md`
4. audience / task / output から必要なものを各1つ以上

theory modules と source files は、深掘りや境界ケースが必要なときだけ読む。

## working brief の作り方

まず、次の brief を作る。

```yaml
working_brief:
  source_kind: existing-draft | research-pack | notes | no-source | mixed
  goal: explain | persuade | decide | teach | summarize | reframe | market | ux-copy
  audience:
    primary: cyberace | cyberagent-senior | ai-beginner-general | general | mixed | unknown
    secondary: optional
  medium: memo | article | training-note | proposal | slide-script | chat | document | microcopy | landing-page
  action_after_reading: understand | decide | approve | try | discuss | align | operate | purchase
  output_length: short | medium | long | staged
  constraints:
    must_keep: []
    avoid: []
    tone: []
  uncertainty:
    source_gaps: []
    claims_to_keep_qualified: []
```

brief が曖昧でも止まらない。最小の仮説を置いて先に進める。

## audience module の選び方

| 条件 | 読むファイル | 主な効き方 |
|---|---|---|
| 若手運用者、実務導入、異業界転職者、用語の段差が大きい | `10-audience-cyberace.md` | 実務接続、平易化、小さな次の一歩 |
| 経営向け、提案向け、戦略・組織・競争優位の判断が主 | `11-audience-cyberagent-senior.md` | 事業課題起点、判断材料、リスク、トレードオフ |
| audience が混在、AI 初学者が共通項、教育色が強い | `12-audience-ai-beginner.md` | AI 説明順序、過大期待の抑制、human-in-the-loop |
| 特定組織に属さない汎用的な読み手 | `13-audience-general.md` | 読み手の事前知識推定、目的適合、スキーマ活性化 |
| audience の仮説が立たない | `source-audience-context.md` | audience モデルを先に立てる |

## task module の選び方

| 条件 | 読むファイル | 主な効き方 |
|---|---|---|
| 白紙から作る | `20-task-generate.md` | throughline 設計、構造選択、section build |
| 原稿の順番と意味を組み替える | `21-task-rewrite.md` | preservation ladder、delta 設計 |
| 要約だが意味を潰したくない | `22-task-summarize-compress.md` | reduction ではなく compression |
| 長い調査結果や deepresearch の変換 | `23-task-deepresearch-transform.md` | core/support/develop、証拠維持、論点整理 |
| 概念解説・説明記事を書く | `24-task-explain-article.md` | 結論先出し→定義→理由→例→まとめ→次の手 |
| 教育コンテンツ・研修資料を作る | `25-task-education.md` | 課題提示→既知活性→見本→練習→振り返り |
| マーケティングコンテンツを作る | `26-task-marketing.md` | 状況→困りごと→変化→根拠→次の一歩 |
| UXマイクロコピーを作る | `27-task-ux-microcopy.md` | 状態→何が起きた→どう直す、最短表現 |

## output module の選び方

| 条件 | 読むファイル | 主な効き方 |
|---|---|---|
| 人が読む本文の型が必要 | `32-output-patterns.md` | memo / explainer / proposal / staged output |
| prompt-rag 的にモジュールを束ねたい | `33-prompt-assembly.md` | selected_modules と prompt bundle |
| api で多段実行したい | `34-integration-notes.md` | staged execution、state 管理 |
| 将来の加筆修正を前提にしたい | `36-maintenance.md` | file 分割ルール、拡張時の作法 |

## style overlay の選び方

| 条件 | 読むファイル | 主な効き方 |
|---|---|---|
| 日本語で、読みやすさ・平易さ・業界語の抑制が重要 | `35-style-japanese-plain.md` | 平易化、事実と意見の分離、名詞の連打防止 |
| テキスト出力の改行・段落設計を制御したい | `38-style-readable-breaks.md` | 段落設計、禁則処理、見出し・箇条書きの使い分け |

## theory module を追加で読む条件

次の条件に当てはまるときだけ theory modules を読む。

| 条件 | 読むファイル |
|---|---|
| 圧縮と削減の区別で迷う、要約の質を上げたい | `40-theory-meaning-compression.md` |
| 読み手の前提知識の推定で迷う、省略の判断基準が要る | `41-theory-common-ground.md` |
| AI slop の破壊が足りない、なぜ収束するかの理論根拠が要る | `42-theory-distributional-convergence.md` |
| 余白や省略の設計で迷う、「行間を読む」の理論が要る | `43-theory-cognitive-complement.md` |
| 4次元の具体的な理論背景・50理論との対応が要る | `44-theory-storytelling-4d.md` |
| 特定の理論名で検索したい | `45-theory-50-catalog.md` |
| AI出力のよくある失敗パターンの診断と処方が要る | `46-theory-antipatterns.md` |
| 「なぜ理解できないか」の5層分析が要る | `47-theory-failure-5layers.md` |
| 理解度の測定方法・テスト設計が要る | `48-theory-evaluation-methods.md` |

## source file を追加で読む条件

- 理論上の根拠や原理の厚みが必要
- anti-slop の判断で迷う
- deepresearch の構造変換で論点が多い
- summarization と storytelling の理論を明示したい
- audience context の差分を精密に扱いたい

## module selection examples

### 例1: deepresearch を CyberACE 向け研修資料に変える

読むもの:
- `01-core-model.md`
- `10-audience-cyberace.md`
- `12-audience-ai-beginner.md`
- `23-task-deepresearch-transform.md`
- `30-anti-slop.md`
- `31-evaluation-rubric.md`
- `32-output-patterns.md`
- `35-style-japanese-plain.md`

### 例2: 経営向け AI 提案メモに改稿する

読むもの:
- `01-core-model.md`
- `11-audience-cyberagent-senior.md`
- `12-audience-ai-beginner.md`
- `21-task-rewrite.md`
- `30-anti-slop.md`
- `31-evaluation-rubric.md`
- `32-output-patterns.md`
- `35-style-japanese-plain.md`

### 例3: 要約だが理解可能性を落としたくない

読むもの:
- `01-core-model.md`
- `22-task-summarize-compress.md`
- `30-anti-slop.md`
- `31-evaluation-rubric.md`
- `35-style-japanese-plain.md`
- audience module 1つ

### 例4: 汎用的な説明記事を作る（Responses API経由）

読むもの:
- `01-core-model.md`
- `13-audience-general.md`
- `24-task-explain-article.md`
- `30-anti-slop.md`
- `31-evaluation-rubric.md`
- `33-prompt-assembly.md`
- `35-style-japanese-plain.md`

### 例5: UXマイクロコピーを作る

読むもの:
- `01-core-model.md`
- `13-audience-general.md`
- `27-task-ux-microcopy.md`
- `30-anti-slop.md`
- `31-evaluation-rubric.md`

### 例6: 教育コンテンツを API 駆動で段階生成する

読むもの:
- `01-core-model.md`
- `13-audience-general.md`
- `25-task-education.md`
- `30-anti-slop.md`
- `31-evaluation-rubric.md`
- `32-output-patterns.md`
- `33-prompt-assembly.md`
- `34-integration-notes.md`

## build state テンプレート

`max_output_tokens` が厳しい場合は、本文より前に次の state を作る。

```yaml
build_state:
  selected_modules:
    core:
      - 01-core-model
      - 30-anti-slop
      - 31-evaluation-rubric
    audience:
      - ...
    task:
      - ...
    output:
      - ...
    theory:
      - ... (必要時のみ)
  throughline: "15語以内で書く"
  tension_axis: "何と何の差分を読ませるか"
  must_preserve:
    - claim
    - cause
    - evidence
    - action
    - uncertainty
  risky_defaults:
    - generic opener
    - bullet dump
    - safe middle conclusion
  situation_model_check:
    - time
    - space
    - causation
    - motivation
    - protagonist
  next_step: design | draft | diverge | gate
```

この state を固定してから本文を展開する。
