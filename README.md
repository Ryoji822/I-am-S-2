# I-am-S-2

AIの変化が、**社会の仕事と所得・会社の顧客と利益・個人の選択肢**にどう影響するかを調べます。仮説を残し、期限を決めて予想し、実績が出たら外れた理由まで見直します。

最初に読む資料は[市場の見取り図](static_intelligence/market-overview.md)、[五つの未来](static_intelligence/scenario-tracker.md)、[9月15〜21日の振り返り](reviews/weekly/2026-09-21.md)です。

## どう使うか

| 期間 | 確かめること | 見直す間隔 |
|---|---|---|
| 短期：1〜3か月 | 利用条件、同品質の費用、人の確認時間 | 毎週 |
| 中期：3か月超〜1年 | 継続利用、利益、顧客維持、採用 | 毎月 |
| 長期：1年超〜3年 | 雇用、実質所得、利益の分配 | 四半期 |

先に発行した予測と実績を比べます。正しかったものだけを残さず、外れ・未判定・判定不能も表示します。短期の結果を長期の成績へ数えません。精度改善は将来の同条件の予測で確かめます。

現在は測定対象と基準値を準備している段階です。新方式の成績は未評価です。[予測候補](config/forecast_candidates.json)には、不足と次の確認日を記載しています。

過去のInformationは原本を保持しています。新しい日次処理からの検索・自動取り込みは未実装で、旧資料を使うための変換・索引の追加が必要です。

## 実行

Python 3.11以上とOpenCode 1.18.31を使用します。GLM_API_KEYを環境変数または実行環境のSecretsに設定してください。キーをファイルへ書き込みません。

```bash
./ias2 validate
./ias2 run
./ias2 status
./ias2 score
```

初期設定は14日間の試行（shadow）です。出力は`state/shadow/`、実行結果は`state/runs/`です。ローカル実行では公開・通知しません。失敗後の再試行は`./ias2 run --run-id retry-20260922-1`のように別のIDを付けます。同じIDは処理を重複させません。

過去日を指定した新規予測や、モデル単独での正式更新はできません。判定案だけを見るには`./ias2 resolve`、明示的な変更案を検証して追記するには`./ias2 apply --plan PATH`を使います。

毎朝08:00 JSTのGitHub Actionsは、一つの処理内で週・月・四半期・半年のレビューを作ります。生成物だけを指定したパスで保存し、全ファイルの一括追加やSlack送信はしません。モデル費用の金額上限は未設定で、時間・件数に上限を置き、返された実測費用を記録します。

## ファイルの見方

- [日報](Intelligence/2026-09-21.md)：わかったこと、仮説への影響、次の確認。
- [Static Intelligence](static_intelligence/market-overview.md)：背景と継続して検証する問い。
- [仮説](config/hypotheses.json)：21の問いと、支持・反証になる観測。
- `data/forecast_ledger/transactions/`：正式な発行・実績・判定・見直しの追記専用履歴。
- `state/runs/<ID>/manifest.json`：成功・一部不足・失敗、使用モデル、費用。
- [運用設計](docs/learning-system.md)：記録、採点、失敗時の扱い、移行。
- [改修と検証の記録](docs/learning-redesign-plan.md)：今回の変更と確認結果。

9月15〜21日の日報7本とStatic 7本は、9月22日に原資料を照合して再編集しました。当時の予測を後から作ったものではありません。[旧版とハッシュ](archive/pre-learning-2026-09-22/manifest.json)を残しています。

## 検証

```bash
python3 -m unittest discover -s tests -v
bash -n ias2 scripts/run-pipeline.sh scripts/validate-output.sh
```

テストは一時ディレクトリと模擬モデルを使い、外部APIを呼びません。過去の書き換え、未来情報、欠測、統計訂正、条件付き予測、採点、失敗と再実行を確認します。

## RSSHubとX投稿

既存の`scripts/fetch-x-posts.sh`と保存済み`X_posts/`は残しています。RSSHubは外部のローカルサービスです。投稿は調査の入口として扱い、現在の日次処理へ無検証で取り込んだり、投稿件数を仮説の確率へ換算したりしません。Evidence v1の資料も保持しますが、新方式への自動採点移行はしません。
