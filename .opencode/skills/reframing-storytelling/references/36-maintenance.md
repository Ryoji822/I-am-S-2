# Maintenance

## この skill をどう伸ばすか

この skill は、最初から完成版にしない。新しい用途が出るたびに、module を増やす前提で設計する。

## 追加の原則

- SKILL.md を knowledge dump にしない
- 新しい audience は新しい audience file に分ける
- 新しい task は新しい task file に分ける
- router と prompt assembly を同時に更新する
- anti-slop と evaluation は共通のまま使う

## 新しい module を足すとき

1. 実際の失敗例を1つ以上集める
2. 何が足りなかったかを言語化する
3. その差分だけを新 file に書く
4. router に選択条件を足す
5. eval scenario を1つ足す

## 増やしすぎを防ぐ

同じことを別 file に重複して書かない。次の役割を守る。

- core model: 全体原理
- audience: 読み手差分
- task: 実行差分
- output: 型
- anti-slop: default 破壊
- eval: 品質確認
- source files: 厚い理論背景

## 変更時の確認

- 1レベル深い参照を守っているか
- 新 file が router から直接見えるか
- 既存 module と役割が衝突していないか
- 追加前より平均的な文章に戻っていないか
