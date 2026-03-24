# Task Module: Transform Deep Research or Rich Research Packs

## 使いどころ

deepresearch の出力、長い調査メモ、複数ソースの束、理論群の比較メモを、人が読める一本のコンテンツに変換するときに使う。

## 原則

- 情報の多さを、そのまま本文に流し込まない
- ただし、context は捨てない。core/support/develop に分ける
- 矛盾や対立は消さず、意味のある tension として扱う
- source の多様性を、安全な平均に潰さない

## core / support / develop

### core
本文に必ず入れる。
- throughline
- 最重要の差分
- 意思決定や理解に直結する根拠

### support
本文か補論に入れる。
- 重要な補強例
- 比較軸
- 反論や制約

### develop
必要に応じて読む。
- 周辺理論
- 詳細事例
- 追加の引用

## 手順

1. source 全体の throughline を置く
2. 主要論点を cluster 化する
3. cluster ごとの中心主張と supporting evidence を分ける
4. 対立・矛盾・未解決点を抽出する
5. audience に合わせて core/support/develop に再配置する
6. 構造を選ぶ
7. 本文を書く
8. anti-slop pass と rubric gate をかける

## 構造の選び方

### explain 型
- 誤解されている見方
- なぜ誤解が起きるか
- どう見直すべきか
- 何が使える原理か

### decision 型
- 現在の判断課題
- 判断を難しくしている前提
- 重要差分
- 推奨案
- リスクと保留

### proposal 型
- 問題
- 打ち手
- 根拠
- 実装条件
- 期待値と限界

## source の矛盾を扱う

- 疑似的な consensus を作らない
- 反対論が重要なら本文に残す
- 分からないことを `分からない` と残す
- 条件で答えが変わるなら、条件を前に出す

## ありがちな失敗

- source の見出し順をそのままなぞる
- 理論の数を見せるだけで、throughline がない
- データや引用を羅列し、何を意味するかがない
- 読み手の用途に合わせた圧縮がない
