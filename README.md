# I-am-S-2: インテリジェンス駆動型AI Agent

FM 2-0（米陸軍インテリジェンス・ドクトリン）に基づく日次インテリジェンス分析システム。

## 目的

Tier 1 AI企業（OpenAI, Anthropic, Google, xAI, ByteDance）がどんな未来世界を構想しているかを、FM 2-0のインテリジェンス・サイクルに基づいて日次で分析・追跡する。

## アーキテクチャ

```
GitHub Actions (cron 06:00 JST daily)
  └── scripts/run-pipeline.sh
       ├── Phase 1: COLLECT  (glm-4-plus, Firecrawl) → Information/YYYY-MM-DD/
       ├── Phase 2: ANALYZE  (glm-5, Blue Agent)     → Information/YYYY-MM-DD/processed.md
       ├── Phase 3: RED TEAM (glm-4-plus)            → state/red-team-*.md
       ├── Phase 4: ARBITER  (glm-5)                 → state/arbiter-*.md + config/ 更新
       ├── Phase 5: STATIC   (glm-4-plus)            → static_intelligence/*.md
       ├── Phase 6: REPORT   (glm-5, 日本語)         → Intelligence/YYYY-MM-DD.md
       └── Phase 7: git commit & push
```

### Blue / Red / Arbiter 3エージェント構成

- **Blue Agent**: 主分析。ACH更新、シナリオ確率更新、I&W評価
- **Red Agent**: 反証探索。確証バイアスの構造的排除（悪魔の代弁者）
- **Arbiter Agent**: Blue/Red統合。最終判断、config更新

## 分析手法

| 手法 | 出典 | 用途 |
|------|------|------|
| PIR/KIQ | FM 2-0 | 問い駆動の収集計画 |
| アドミラルティ・コード | NATO | 情報源信頼性の2軸評価 |
| ACH（競合仮説分析） | Pherson | 仮説の反証ベース評価 |
| QHG 4象限シナリオ | NotebookLM | 将来シナリオの構造化 |
| I&W（兆候・警告） | FM 2-0 | 変化の早期検知 |
| ICD 203 確度基準 | ICD 203 | 判断の確度レベル |

## ディレクトリ構造

```
I-am-S-2/
├── Intelligence/          # 日次インテリジェンス・レポート（日本語）
│   └── YYYY-MM-DD.md
├── Information/           # 日次収集データ（生情報）
│   └── YYYY-MM-DD/
│       ├── collected-raw.md
│       └── processed.md
├── static_intelligence/   # 企業分析・未来予測（日付非依存）
│   ├── openai.md
│   ├── anthropic.md
│   └── ...
├── state/                 # パイプライン中間状態
│   ├── red-team-YYYY-MM-DD.md
│   ├── arbiter-YYYY-MM-DD.md
│   └── arbiter-latest.md
├── config/                # 設定・状態ファイル
│   ├── pirs.json          # PIR定義
│   ├── companies.json     # 監視対象企業
│   ├── collection_plan.json # 収集計画
│   ├── hypotheses.json    # ACH仮説レジストリ
│   ├── scenarios.json     # シナリオセット
│   └── indicators.json    # I&W指標
├── prompts/               # Phase別プロンプト
├── scripts/               # パイプラインスクリプト
├── .opencode/             # OpenCode設定
├── .github/workflows/     # GitHub Actions
└── opencode.json          # OpenCode設定
```

## セットアップ

### 1. GitHub Secrets の設定

| Secret | 説明 |
|--------|------|
| `GLM_API_KEY` | Zhipu AI (GLM) APIキー |
| `FIRECRAWL_API_KEY` | Firecrawl APIキー |
| `SLACK_BOT_TOKEN` | Slack Bot Token（static_intelligence更新通知用、任意） |

### 2. ローカル実行

```bash
export GLM_API_KEY="your-glm-api-key"
export FIRECRAWL_API_KEY="your-firecrawl-api-key"
export SLACK_BOT_TOKEN="your-slack-bot-token"  # 任意

bash scripts/run-pipeline.sh
```

### 3. 出力検証

```bash
bash scripts/validate-output.sh $(date +%Y-%m-%d)
```

### 4. GitHub Actions

- 自動実行: 毎日 06:00 JST
- 手動実行: Actions → Daily Intelligence Pipeline → Run workflow

## 技術スタック

- **LLM**: Zhipu AI GLM-5 (分析/レポート), GLM-4-Plus (収集/処理)
- **ツール**: OpenCode CLI, Firecrawl MCP
- **CI/CD**: GitHub Actions
- **通知**: Slack Bot API

## ライセンス

Private
