# Evidence Record v1 仕様

Phase 1 (Agentic Intelligence Redesign §11 Phase 1) の **Evidence ID + raw/processed 分離** 導入に伴う、Evidence Record の正式仕様。

## 目的

`Information/YYYY-MM-DD/collected-raw.md` の INFO-NNN セクションは人間可読だが、機械的な参照整合検査・重複検知・引用追跡には不向き。Phase 1 では INFO-NNN 形式を**残したまま**、機械可読な Evidence Record (JSONL) を並行生成し、安定したIDで根拠を逆引き可能にする。

## ファイル配置

| パス | 役割 | 単一書き手 |
|---|---|---|
| `Information/raw/<date>/firecrawl.jsonl` | Firecrawl由来の Evidence Record | `scripts/build-evidence-index.py` |
| `Information/raw/<date>/x_posts.jsonl` | X投稿由来の Evidence Record | `scripts/fetch-x-posts.py` (pending) → `build-evidence-index.py` (mint) |
| `Information/raw/<date>/_meta.json` | 当日収集メタ (件数、スキーマ版、劣化状態) | `build-evidence-index.py` |
| `Information/processed/<date>.jsonl` | raw を統合・重複除去した正本 | `build-evidence-index.py` |
| `Information/evidence_index.json` | 全期間横断の Evidence ID 索引 (URL/ハッシュ/raw_path) | `build-evidence-index.py` |

`collected-raw.md` (INFO-NNN形式) と `processed.md` (Blue Agent出力) は変更なし。**後方互換のため Phase 1 では並走させる**。

## ID 採番規則

```
EVD-YYYYMMDD-NNNN
```

- `YYYYMMDD`: その Evidence が初めて取得された日 (JST)
- `NNNN`: 当日内の連番 (4桁ゼロ埋め、1〜9999)
- INFO-NNN との対応は `legacy_info_id` フィールドで保持

例: `EVD-20260508-0042` ↔ `INFO-042` (2026-05-08のrunで取得)

**single-writer 原則**: ID採番は `build-evidence-index.py` のみが行う。`fetch-x-posts.py` は `pending_evidence_id: null` を埋めて記録し、後続の Phase 1.6 で実IDが採番される。

## 必須フィールド (Phase 1, 6項目)

| フィールド | 型 | 説明 |
|---|---|---|
| `evidence_id` | string | `EVD-YYYYMMDD-NNNN` 形式 |
| `source_url` | string | `http(s)://` で始まる原文URL |
| `retrieved_at` | string | ISO 8601 (JST、秒精度) |
| `content_hash` | string | `sha256:<64hex>` 形式、原文ブロックのハッシュ |
| `quotable_excerpt` | string | 原文からの引用 (240字以内、判断を含めない) |
| `raw_path` | string | この Evidence が記録されている JSONL パス (リポジトリ相対) |

## オプションフィールド

| フィールド | 型 | 説明 |
|---|---|---|
| `schema_version` | string | スキーマバージョン (現在 "1.0") |
| `run_date` | string | YYYY-MM-DD |
| `legacy_info_id` | string | 対応する INFO-NNN ID (INFO ↔ EVD 双方向逆引き用) |
| `source_title` | string | 記事/投稿タイトル |
| `source_type` | string | `official` / `news` / `social` / `github` / `regulatory` / `research` / `other` |
| `retrieval_method` | string | `firecrawl` / `rsshub` / `manual` / `fallback_copy` |
| `language` | string | `ja` / `en` / `other` |
| `summary_for_indexing` | string | 判断を含まない短い要約 (500字以内) |
| `kiq_hint` | string[] | 関連 KIQ-ID / PIR-ID のヒント |
| `reliability_admiralty` | string | アドミラルティ・コード (例: `A-3`) |
| `degraded` | bool | DEGRADED 経路で生成されたか |
| `previous_run_evidence` | bool | 前日のデータをコピーした記録か (DEGRADED時) |
| `pending_evidence_id` | null | fetch-x-posts.py が書く placeholder。build-evidence-index で削除 |

未知のフィールドは validator がエラーにする (将来の拡張は `OPTIONAL_FIELDS` に追加してから使う)。

## 後方互換ポリシー

1. **INFO-NNN を消さない**: `collected-raw.md` の人間可読フォーマットは Phase 6 が引き続き引用する。後方互換のため少なくとも Phase 4 (Arbiter state_update_plan化) までは並走。
2. **過去日は遡及採番しない**: Phase 1 が有効化された日以降にだけ Evidence Record を生成する。過去日の INFO-NNN は INFO-NNN のまま。
3. **DEGRADED 時はスキップ**: Phase 1 が前日のデータをコピーした (DEGRADEDマーカーあり) 日は、phantom evidence を防ぐため Phase 1.6 をスキップする。
4. **再実行は冪等**: 同じ `--date` で `build-evidence-index.py` を再実行すると、その日のエントリだけが index から削除→再生成される。他の日には影響しない。

## 機械検証 (validate-output.sh)

`scripts/validate-output.sh` は以下を WARN レベル (Phase 1 段階) で確認:

1. `firecrawl.jsonl` / `x_posts.jsonl` の各行が JSON パース可能で、必須6フィールドが揃う
2. `evidence_index.json` が valid JSON で、当日の `raw_path` が実在する
3. `processed/<date>.jsonl` 内に `content_hash` 重複がない (循環報告の事前検知)
4. `collected-raw.md` の INFO-NNN セクションに `Evidence ID:` 行がある (新規収集分)

WARN は1週間安定後に FAIL に昇格する想定 (`docs/agentic-intelligence-redesign/README.md` §11 Phase 1 推奨運用)。

## 有効化 (env ガード)

Phase 1.6 はデフォルト無効。有効化は `run-pipeline.sh` を以下で起動:

```bash
ENABLE_EVIDENCE_PHASE1=1 ./ias2 run
```

GitHub Actions で常時有効化する場合は workflow yml の `env:` に `ENABLE_EVIDENCE_PHASE1: "1"` を追加。何かあれば env を外せば即旧パスにロールバック可能。

## ロールバック

完全ロールバックする場合:

```bash
# 環境変数を外す or workflow から削除
unset ENABLE_EVIDENCE_PHASE1

# 生成データを除去 (任意)
git rm -r Information/raw/ Information/processed/ Information/evidence_index.json

# プロンプト・スクリプト・検証は無害な追加なので残置可能
```

`collected-raw.md` 内に追記された `- **Evidence ID:** EVD-...` 行は無害なメタデータなので残しても問題ない。

## CLI

```bash
# Build for today
python3 scripts/build-evidence-index.py

# Build for specific date
python3 scripts/build-evidence-index.py --date 2026-05-08

# Dry-run (no writes)
python3 scripts/build-evidence-index.py --date 2026-05-08 --dry-run

# Validate a JSONL file
python3 -m scripts.lib.evidence_schema validate Information/raw/2026-05-08/firecrawl.jsonl

# Compute hash for a string
python3 -m scripts.lib.evidence_schema hash "some text"

# Mint an Evidence ID
python3 -m scripts.lib.evidence_schema mint-id 2026-05-08 42
# → EVD-20260508-0042
```

## 移行ロードマップ (`docs/agentic-intelligence-redesign/README.md` §11)

| Phase | 状態 | 内容 |
|---:|---|---|
| **1** | **本仕様** | Evidence ID + raw/processed 分離 (INFO-NNN 後方互換) |
| 2 | 未着手 | Screening + Quality Gate (`screened_information.json`, `quality_matrix.json`) |
| 3 | 未着手 | ACH/Assumptions/QualityMatrix の状態化 |
| 4 | 未着手 | Arbiter `state_update_plan` 方式、INFO-NNN 廃止検討 |
| 5 | 未着手 | GitHub Actions Job 分割 (1 → 11 ジョブ) |
| 6 | 未着手 | Weekly Review + Forecast Scorecard |
