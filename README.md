# I-am-S-2

AI企業の動きから、囲い込みと開放のどちらが進んでいるかを毎日更新し、判断材料を1枚にまとめます。

## 誰の何に効くか

- **プロダクト戦略**: どのAIプラットフォームに乗るべきか？ロックインリスクはどこにあるか？
- **技術投資判断**: OSS vs 商用、マルチベンダー vs 一本化の判断根拠
- **提携・依存リスク評価**: 各社のエコシステムからの離脱コスト（スイッチングコスト）の変化

## 出力例

> **今日のポイント（300字）**
>
> OpenAIがSkills配布の審査強化を発表し、実行環境の囲い込みが一段進んだ（確度: 中）。
> Anthropic MCPは新たに5社が対応を表明したが、「対応」と「実採用」の乖離に注意が必要。
> 全体として「静かな囲い込み」シナリオ（SCN-003, 31%）が引き続き最有力。

## クイックスタート

```bash
# 環境変数を設定
export GLM_API_KEY="your-glm-api-key"
export FIRECRAWL_API_KEY="your-firecrawl-api-key"

# 全フェーズ実行
./ias2 run

# 収集だけ実行
./ias2 run collect

# 日付を指定して実行
./ias2 run --date 2026-02-18

# 出力を検証
./ias2 validate

# 今日の進捗確認
./ias2 status
```

## 監視対象

**Tier 1（日次監視）**: OpenAI, Anthropic, Google/DeepMind, xAI, ByteDance
**Tier 2（週次監視）**: Meta AI, Microsoft, Amazon/AWS, Mistral AI, DeepSeek

## シナリオ枠組み

2つの不確実軸で4つの将来を描きます:

| | 閉鎖（囲い込み） | 開放（相互運用） |
|---|---|---|
| **格差拡大** | SCN-001: 囲い込みの勝者 | SCN-002: 技術は開くが勝者は出る |
| **収斂** | SCN-003: 静かな囲い込み | SCN-004: 誰でもAI |

## アーキテクチャ

```
GitHub Actions (cron 08:00 JST daily) or ./ias2 run
  └── scripts/run-pipeline.sh
       ├── Phase 1: 収集      (Firecrawl MCP)  → Information/YYYY-MM-DD/
       ├── Phase 1.5: X投稿注入 (ローカル)       → collected-raw.mdに追記
       ├── Phase 2: Blue Agent  (GLM-5, 分析)    → processed.md
       ├── Phase 3: Red Agent   (GLM-5, 反証)    → state/red-team-*.md
       ├── Phase 4: Arbiter     (GLM-5, 統合)    → state/arbiter-*.md + config更新
       ├── Phase 5: 静的更新    (GLM-5)          → static_intelligence/*.md
       ├── Phase 6: レポート    (GLM-5, 日本語)   → Intelligence/YYYY-MM-DD.md
       └── Phase 7-9: 検証・git push・Slack通知
```

### Blue / Red / Arbiter 3エージェント構成

FM 2-0（米陸軍インテリジェンス・ドクトリン）の手法を用いた分析パイプライン:

- **Blue Agent**: 主分析。ACH（複数の仮説を証拠で比較する手法）更新、シナリオ確率更新、I&W（兆候・警告）評価
- **Red Agent**: 反証探索。確証バイアスの構造的排除（悪魔の代弁者）
- **Arbiter Agent**: Blue/Red統合。最終判断、config更新

### 分析手法

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
├── ias2                      # CLIエントリポイント
├── Intelligence/              # 日次レポート（日本語）
├── Information/               # 日次収集データ
├── static_intelligence/       # 企業分析（日付非依存）
├── state/                     # パイプライン中間状態
├── config/                    # 設定ファイル
│   ├── pirs.json              # PIR定義
│   ├── companies.json         # 監視対象企業
│   ├── collection_plan.json   # 収集計画
│   ├── hypotheses.json        # ACH仮説レジストリ
│   ├── scenarios.json         # シナリオセット
│   ├── indicators.json        # I&W指標
│   ├── notification.json      # Slack通知設定
│   └── providers.json         # 収集・LLMプロバイダー設定
├── skills/                    # Phase定義ファイル
├── prompts/                   # Phase別プロンプト
├── scripts/                   # パイプラインスクリプト
└── X_posts/                   # X投稿データ（ローカル収集）
```

## セットアップ

### GitHub Secrets

| Secret | 説明 |
|--------|------|
| `GLM_API_KEY` | Zhipu AI (GLM) APIキー |
| `FIRECRAWL_API_KEY` | Firecrawl APIキー |
| `SLACK_BOT_TOKEN` | Slack通知用（任意） |

### GitHub Actions

- 自動実行: 毎日 08:00 JST
- 手動実行: Actions → Daily Intelligence Pipeline → Run workflow（日付指定可）

## 技術スタック

- **LLM**: Zhipu AI GLM-5
- **ツール**: OpenCode CLI, Firecrawl MCP
- **CI/CD**: GitHub Actions
- **通知**: Slack Bot API
