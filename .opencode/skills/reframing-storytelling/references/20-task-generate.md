# Task Module: Generate New Content

## 使いどころ

白紙から本文を作るときに使う。source が無い場合だけでなく、複数のノートや論点から新しい一本を組み上げるときにも使う。

## 手順

1. 読み手と読後 action を一文で置く
2. throughline を15語以内で置く
3. 何を緊張軸にするか決める
4. どの構造にするか決める
5. 根拠を3束以内に整理する
6. draft を section ごとに作る
7. anti-slop pass をかける
8. rubric で検査する

## よく使う緊張軸

- 現状認識と現実の差
- 表面上の効率化と本当のボトルネックの差
- できることと再現できることの差
- 導入期待と運用コストの差
- 速さと品質の差

## よく使う構造

### explain
- 何が問題か
- なぜ起きるか
- どう考えればよいか
- どう使うか
- どこで失敗するか

### decide
- 今の問題
- 選択肢
- 比較軸
- 推奨案
- リスクと次の判断

### propose
- 現状
- 障害
- 解き方
- 根拠
- 実行と判断依頼

### teach
- 誤解
- 正しい見方
- 例
- 例の意味
- 小さく試す方法

## source が薄いとき

source にない事実を足すな。足すのは次だけにする。

- 橋渡しの論理
- audience に合わせた framing
- 明示化された不確実性
- 例示だと分かる短い例

## 長文生成のルール

長くなるときは、最初に blueprint を作る。

```yaml
blueprint:
  throughline: ...
  sections:
    - title: ...
      role: background | tension | reframe | evidence | action
      must_cover: []
```

そのあと section 単位で展開する。1回で全部を書き切ろうとしない。
