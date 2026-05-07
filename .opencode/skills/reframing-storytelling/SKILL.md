---
name: reframing-storytelling
description: reframe dense source material into audience-specific storytelling with meaning-preserving compression instead of shallow summarization. use for writing, rewriting, summarization, explanation, deepresearch transformation, proposals, training materials, executive memos, educational content, marketing copy, and ux microcopy. uses cognitive science-backed compression theory, common ground calibration, and distributional convergence destruction via modular prompt-rag architecture. designed for responses api and claude agent sdk integration.
---

# Reframing Storytelling

## Overview

この skill は、情報を「文章として成立している状態」から「読み手が理解し、判断し、次に動ける状態」へ変換する。

要約・言い換え・解説・提案・教育・マーケティング・UXコピーのどれであっても、次の3点を固定する。

1. 読み手の共通知を先に決める。
2. 因果と意味を残したまま圧縮する（削減ではなく意味圧縮）。
3. 分布的収束で生まれる無難で平均的な文章を、構造的に壊す。

この skill を使うときは、1つの巨大な指示をそのまま流し込まない。`references/` から必要なモジュールだけを読み、実行時に指示を組み立てる。

## Core Workflow

次の順で進める。

1. 依頼を `source / goal / audience / medium / action / uncertainty` の6変数で定義する。
2. 必ず `references/00-router.md` を読む。
3. 必ず `references/01-core-model.md` を読む。
4. 必ず `references/30-anti-slop.md` を読む。
5. 必ず `references/31-evaluation-rubric.md` を読む。
6. audience に応じて audience module を1つ読む。必要なら2つ読む。
7. task に応じて task module を1つ読む。
8. medium と長さに応じて `references/32-output-patterns.md` を読む。
9. 日本語出力なら `references/35-style-japanese-plain.md` を読む。
10. 日本語出力なら `references/39-humanizer-ja.md` を読む。AI文体の表層パターン検出・除去と、日本語固有のAIパターン対策に使う。
11. テキスト出力なら `references/38-style-readable-breaks.md` を読む。
12. 必要に応じて theory module を読む（`40-` 系）。
13. 実行前に `references/33-prompt-assembly.md` の方式で、選んだモジュールだけを束ねる。
14. 出力は一発で完成させず、複数パスで作る。

## Multi-pass Rule

長い出力や重要な出力では、次の5パスを使う。

1. **route**: 目的、読み手、選択モジュール、緊張軸を決める。
2. **design**: throughline、構造、残す因果、削る情報、足す橋渡しを決める。
3. **draft**: 本文を作る。
4. **diverge**: 平均的な語り口、安いまとめ、無難な中間結論を壊す。日本語出力では `39-humanizer-ja.md` のパターン A〜F でスキャンし、AI文体の表層パターンを除去する。
5. **humanize**: diverge 後の出力に対し、`39-humanizer-ja.md` の G（voice calibration）と H（soul injection）を適用する。声の調律と生気の注入。パターン除去だけで終わらせない。
6. **gate**: rubric で検査し、さらに読み込んだ全モジュール（style overlay、audience module、task module、humanizer）の最終チェック・quality gate・failure modes も検証する。humanizer の最終チェック10項目も通す。欠点があれば直す。

`max_output_tokens` が厳しい環境では、`route` と `design` を先に出し、そのあと section ごとに展開する。長文を一度に吐き切ろうとしない。

## Non-negotiables

- ストーリーテリングを、感動話や装飾だと思わない。読み手の理解経路を設計する技術として扱う。
- 要約を、削る作業だと思わない。意味を保ったまま圧縮する作業として扱う（コルモゴロフ複雑性の意味での圧縮）。
- actor、problem、cause、constraint、change、action を消さない。
- source にある矛盾、留保、条件つき主張を、安全な平均値に潰さない。
- 読み手が事業判断をする文書では、AI の仕組みから始めない。先に事業上の問題を置く。
- AI 初学者向けの文書では、専門語だけを並べない。平易な説明を先に置く。
- 冒頭から箇条書きの結論ダンプに逃げない。問い、緊張、差分、判断を設計する。
- generic な締め方で終わらせない。最後は、何をどう判断するか、何を保留するかまで書く。
- 日本語では、かっこつけた業界語や抽象名詞の連打に逃げない。
- 事実、意見、推測を混ぜない。
- 状況モデルの5次元（時間・空間・因果・動機・主体）を壊さない。
- 因果の橋渡し推論（bridging inference）を可能にする手がかりを削除しない。
- 改行は見た目の都合ではなく、意味の区切りで入れる。段落間は空行で分ける。行頭禁則・行末禁則を守る。
- 読み込んだモジュールの最終チェック・quality gate を gate pass で必ず検証する。rubric の7項目だけで gate を通過させない。

## Decision Rules

### Audience

- **CyberACE の若手運用者・若手マーケター** → `references/10-audience-cyberace.md`
- **CyberAgent 広告事業本部のシニア・経営寄りの読み手** → `references/11-audience-cyberagent-senior.md`
- **AI 初学者で、組織や職種が混在している** → `references/12-audience-ai-beginner.md`
- **上の audience 設定に迷う** → `references/source-audience-context.md` を読んで仮説を立てる。
- **汎用的な audience / 組織特定なし** → `references/13-audience-general.md`

### Task

- **新規作成** → `references/20-task-generate.md`
- **既存原稿の改稿・再整形** → `references/21-task-rewrite.md`
- **要約だが、意味と因果を潰したくない** → `references/22-task-summarize-compress.md`
- **deepresearch や長い調査結果の再構成** → `references/23-task-deepresearch-transform.md`
- **説明記事（概念解説）** → `references/24-task-explain-article.md`
- **教育コンテンツ（学習設計）** → `references/25-task-education.md`
- **マーケティングコンテンツ** → `references/26-task-marketing.md`
- **UXマイクロコピー** → `references/27-task-ux-microcopy.md`

### Output

- **説明資料、教育資料、記事、メモ、提案、話し言葉原稿** → `references/32-output-patterns.md`
- **API 駆動の multi-turn 実装** → `references/34-integration-notes.md`
- **モジュール束ねのやり方** → `references/33-prompt-assembly.md`
- **今後の増補・改修** → `references/36-maintenance.md`
- **日本語での高可読出力** → `references/35-style-japanese-plain.md`
- **AI文体の表層パターン検出・除去（日本語）** → `references/39-humanizer-ja.md`
- **テキスト出力の改行・段落設計** → `references/38-style-readable-breaks.md`

### Theory (深掘りが必要なときだけ読む)

- **意味圧縮の認知科学的原理** → `references/40-theory-meaning-compression.md`
- **共通知と語用論** → `references/41-theory-common-ground.md`
- **分布的収束の構造的理解** → `references/42-theory-distributional-convergence.md`
- **認知的補完と行間** → `references/43-theory-cognitive-complement.md`
- **ストーリーテリング4次元の理論的基盤** → `references/44-theory-storytelling-4d.md`
- **50理論カタログ（検索用）** → `references/45-theory-50-catalog.md`
- **6つのアンチパターンと認知科学的処方箋** → `references/46-theory-antipatterns.md`
- **ストーリーテリング不全の5層分析** → `references/47-theory-failure-5layers.md`
- **理解度評価の理論と手法** → `references/48-theory-evaluation-methods.md`

### Full Sources (実行時の深掘り・確認に使う)

- `references/source-01-storytelling-framework-rich.md`
- `references/source-02-storytelling-summarization-framework.md`
- `references/source-audience-context.md`

source files は control plane ではない。実行時の判断や深掘りに使う。

## Required Output Discipline

出力の前に、頭の中で次を確定する。

- 読み手は誰か。
- 読後に何が変わるべきか。
- 何を残し、何を削り、何を橋渡しとして足すか。
- この文章が平均的な AI 出力に流れた場合、どこが一番弱くなるか。
- 読み手の状況モデル（時間・空間・因果・動機・主体）が再構築できるか。
- gist 記憶を形成するのに十分な意味的骨格があるか。

ユーザーが設計メモも求めている場合だけ、`selected_modules` と `throughline` と `quality_gate` を併記する。通常は本文を優先する。

## References

### Core (必ず読む)
- [router](references/00-router.md)
- [core model](references/01-core-model.md)
- [anti slop](references/30-anti-slop.md)
- [evaluation rubric](references/31-evaluation-rubric.md)
- [output patterns](references/32-output-patterns.md)
- [prompt assembly](references/33-prompt-assembly.md)

### Audience (読み手に応じて選ぶ)
- [cyberace](references/10-audience-cyberace.md)
- [cyberagent senior](references/11-audience-cyberagent-senior.md)
- [ai beginner overlay](references/12-audience-ai-beginner.md)
- [general audience](references/13-audience-general.md)
- [audience context source](references/source-audience-context.md)

### Task (タスクに応じて選ぶ)
- [generate](references/20-task-generate.md)
- [rewrite](references/21-task-rewrite.md)
- [summarize with compression](references/22-task-summarize-compress.md)
- [deepresearch transform](references/23-task-deepresearch-transform.md)
- [explain article](references/24-task-explain-article.md)
- [education](references/25-task-education.md)
- [marketing](references/26-task-marketing.md)
- [ux microcopy](references/27-task-ux-microcopy.md)

### Integration and Maintenance
- [integration notes](references/34-integration-notes.md)
- [style: plain japanese](references/35-style-japanese-plain.md)
- [style: readable breaks](references/38-style-readable-breaks.md)
- [humanizer: AI文体パターン検出・除去（日本語版）](references/39-humanizer-ja.md)
- [maintenance](references/36-maintenance.md)
- [examples and evals](references/37-examples-and-evals.md)

### Theory (深掘り時のみ読む)
- [meaning compression theory](references/40-theory-meaning-compression.md)
- [common ground theory](references/41-theory-common-ground.md)
- [distributional convergence theory](references/42-theory-distributional-convergence.md)
- [cognitive complement theory](references/43-theory-cognitive-complement.md)
- [storytelling 4d theory](references/44-theory-storytelling-4d.md)
- [50 theory catalog](references/45-theory-50-catalog.md)
- [antipatterns theory](references/46-theory-antipatterns.md)
- [failure 5 layers](references/47-theory-failure-5layers.md)
- [evaluation methods theory](references/48-theory-evaluation-methods.md)

### Full Sources
- [storytelling theory source](references/source-01-storytelling-framework-rich.md)
- [summarization theory source](references/source-02-storytelling-summarization-framework.md)
