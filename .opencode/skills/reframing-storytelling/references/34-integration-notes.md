# Integration Notes for API-driven Use

## 目次
- 基本方針
- Responses API での使い方
- Claude Agent SDK での使い方
- 推奨 input contract
- one-call mode
- staged mode
- state 管理
- 実装時の注意

## 基本方針

Responses API と Claude Agent SDK のどちらでも、次を守る。

- skill を `巨大な system prompt` として扱わない
- 必要な reference だけを選ぶ（prompt-rag 方式）
- 長文は staged mode で作る
- source 全文と assembled instruction を毎回丸ごと再注入しない

## Responses API での使い方

### system prompt の構成

```
[base block]           ← 01-core-model の要約
[audience block]       ← 選んだ audience module の要約
[task block]           ← 選んだ task module の要約
[anti-slop block]      ← 30-anti-slop の要約
[evaluation block]     ← 31-evaluation-rubric の quick gate
[style block]          ← 必要時のみ
```

### 実行フロー

1. input contract を受け取る
2. router の判定ロジックで module を選択する
3. 選択した module の要約を system prompt に組み立てる
4. source text を user message として渡す
5. one-call または staged mode で実行する

### tool use との組み合わせ

Responses API の tool use を使う場合、次の tool 定義が有用。

- `select_modules`: audience / task / output の選択を返す
- `create_working_brief`: working brief を構造化して返す
- `evaluate_output`: rubric に基づく自己評価を返す

## Claude Agent SDK での使い方

### system prompt の構成

Claude Agent SDK では、skill の reference files を tool として公開し、agent が必要に応じて読み込む設計が可能。

```python
# 参考構成
tools = [
    read_reference_tool,    # references/ の file を読む
    evaluate_output_tool,   # rubric による自己評価
]

system_prompt = """
あなたは、読み手の理解経路を設計する編集者である。
reframing-storytelling skill の references/ にあるモジュールを必要に応じて読み、
指示を動的に組み立てて実行する。

最初に 00-router.md を読み、task に合うモジュールを選択せよ。
必ず 01-core-model.md, 30-anti-slop.md, 31-evaluation-rubric.md を読め。
"""
```

### multi-turn での staged execution

```
Turn 1: route → working_brief + selected_modules + throughline
Turn 2: design → section plan + must_preserve + risky_defaults
Turn 3+: draft → section ごとに展開
Final: gate → rubric 検査 + 修正
```

## 推奨 input contract

次のような contract を外側で持つと扱いやすい。

```json
{
  "source": "...",
  "goal": "rewrite | summarize | explain | propose | decide | teach | market | ux-copy",
  "audience": "cyberace | cyberagent-senior | ai-beginner-general | general | mixed",
  "medium": "memo | article | training-note | proposal | slide-script | chat | document | microcopy | landing-page",
  "output_length": "short | medium | long | staged",
  "output_language": "ja | en",
  "must_keep": ["..."],
  "avoid": ["..."],
  "needs_design_notes": false
}
```

## one-call mode

source が短く、output も短いなら one-call mode でよい。

流れ:
1. router で module を選ぶ
2. selected_modules を内部で固定する
3. draft
4. anti-slop pass
5. rubric gate
6. final

## staged mode

source が長い、または output が長いなら staged mode を使う。

### stage 1: route
- working_brief
- selected_modules
- throughline
- section plan

### stage 2: build
- section ごとに draft
- section 間の接続を残す

### stage 3: diverge
- lead / body / ending の平均解を壊す

### stage 4: gate
- rubric で点検
- 必要なら section 単位で再生成

## state 管理

外側のアプリ側で、最低限次を保持する。

```json
{
  "selected_modules": ["..."],
  "throughline": "...",
  "tension_axis": "...",
  "must_preserve": ["..."],
  "completed_sections": ["..."],
  "remaining_sections": ["..."],
  "quality_findings": ["..."],
  "situation_model_check": {
    "time": true,
    "space": true,
    "causation": true,
    "motivation": true,
    "protagonist": true
  }
}
```

## 実装時の注意

- source の重要部分が文書中央にある場合は、先に抽出してから route する（Lost in the Middle 問題への対策）
- `continue` のたびに全文再生成しない
- `summary` を依頼されても、先に `compression target` を定義する
- skill の file 構造を壊さず、router と assembly の二枚看板で運用する
- 日本語出力では style overlay を忘れない
- theory modules は実行時にはロードせず、品質問題の診断時にのみ参照する
