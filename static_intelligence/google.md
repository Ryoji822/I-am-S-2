# Google／DeepMind：検索・業務ソフト・クラウドを通じて AI を供給する

基準日：2026年9月21日。再調査・改稿：9月22日（日本時間）。決算説明の数値はその対象期間の値です。更新型の仕様・料金は確認日を別記します。

## 会社と事業の全体像

Google の AI 事業は、Gemini という一つのアプリに閉じていません。検索・YouTube の広告、Workspace の業務利用、Google Cloud の計算資源と企業向けサービス、Gemini の直接利用にまたがります。Google DeepMind のモデル開発を、既存の顧客接点とクラウドに配る構造です。[2026年7月22日の CEO 決算説明](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/)

**現在の評価は、既存事業の規模と AI の供給網を同時に持つことが強みであり、AI を売る収入と、既存製品を AI で強くする収入を分けて見る必要がある、というものです。** 「Gemini の企業採用データがないので何も分からない」という旧版の整理は誤りでした。利用と事業成長を示す資料はあり、分からないのは主に Gemini 単独の利益・市場シェア・利用企業の成果です。

確度は、製品の配置と公表された利用規模について高く、AI 投資が長期の利益率を高めるという判断について中程度です。自社の決算説明と顧客数の公表を使っていますが、各製品への利益配分までは開示されていません。

## 製品と顧客の対応

| 領域 | 主な製品・機能 | 顧客と対価 |
|---|---|---|
| 消費者・検索 | Gemini アプリ、AI Mode、検索の AI 機能、YouTube 内の AI | 利用者の継続利用と広告接点、個人向け契約 |
| 従業員の仕事 | Workspace と Gemini Enterprise | 社内データを検索し、資料作成・調査・業務を行う企業 |
| 開発と実行管理 | Gemini API、AI Studio、Antigravity、Gemini Enterprise Agent Platform | モデルを組み込み、エージェントを動かす開発者と企業 |
| 音声 | Gemini 3.8 Live、Extended Thinking、3.5 Transcribe | 会話しながら作業する窓口・支援・文字起こし |
| 計算資源・周辺機能 | TPU を含む基盤、データ、セキュリティ、クラウド | 自社・他社モデルを運用する組織 |
| 公開モデル | Gemma 系 | 自分で動かせるモデルを必要とする開発者 |

[決算説明](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/)、[Gemini Enterprise の導入時の説明](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-enterprise-sundar-pichai/)、[9月15日の音声モデル発表](https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/)。同じ Gemini という名称でも、個人アプリ、API、従業員向け契約、クラウド基盤は別の購入対象です。

## 規模、成長、投資

7月22日の第2四半期決算説明では、Alphabet 全体の売上成長率は前年同期比24%、Search and Other は17%、YouTube Ads は13%、Cloud は82%と公表しています。Cloud の受注残は5,140億ドルです。受注残は将来の契約収入に関わる指標で、その四半期の売上や現金とは異なります。[CEO 決算説明](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/)

同資料の利用規模は、Gemini アプリ月間9.5億人、Antigravity 週間240万人超、モデル API 毎分約220億トークン、Gemini Enterprise は Fortune 100 の約90%が利用というものです。アプリの人数、開発ツールの人数、処理量、企業数は別の母集団なので足し合わせられません。企業数だけでは全従業員への展開や有料利用の深さも分かりません。[同説明](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/)

6月3日の投資家向け説明では、第1四半期 Cloud 売上約200億ドル、営業利益約70億ドル、利益率約33%、2026年の設備投資見込み1,800〜1,900億ドルを説明しました。これらは6月時点の対象期間・予算で、9月の更新値と混ぜません。[投資家説明](https://blog.google/alphabet/investor-presentation-june-2026/)

読み取れるのは、AI は既に売上を持つ事業の中で拡大しており、投資規模も大きいことです。Cloud 売上には計算資源、他社モデル、データや業務サービスも含まれるため、Cloud 成長率を Gemini 単独のシェア上昇率に置き換えることはできません。一方で、顧客の企業数と API の利用量を無視し、全てを他社モデル向けのインフラ需要と決めつけることもできません。

## 直近の技術・製品の状態

Gemini 3.8 Flash の公式説明は、長いソフトウェア開発、複数段階のエージェント、複雑な企業業務を対象としています。Managed Agents の Antigravity エージェントと SDK の既定モデルにも位置付けています。新しいモデルを出すだけでなく、そのモデルを使って仕事を進める仕組みまで揃えています。[Gemini 3.8 Flash の説明](https://ai.google.dev/gemini-api/docs/latest-model?hl=en)

9月15日の音声発表は、3.8 Live と Extended Thinking、文字起こし用の3.5 Transcribe を区別しています。会話を継続しながら裏でツールや API を使う方向であり、音声をテキストに変換するだけの機能とは異なります。窓口対応や社内支援にとっては、回答品質だけでなく、処理が終わったことをどう確認するかが導入条件になります。[開発者向け発表](https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/)

Gemini Enterprise の Skills は、仕事の指示や補助資料を再利用する機能です。管理者が作成・共有を有効にする必要があり、Standard／Plus／従量課金と Frontline で作成可否が異なります。確認した文書では、assistant では使える一方、agents では使えないという制約があります。「スキルに対応したので全ての実行環境で同じ手順を使える」とは読めません。[9月22日確認の仕様](https://docs.cloud.google.com/gemini/enterprise/docs/skills)

## 価格と導入の費用

9月22日に確認した Gemini 3.8 Flash の導入価格は、100万トークン当たり入力 $0.75、出力 $3.75。公式文書は2026年12月31日までとし、2027年1月1日から入力 $1.50、出力 $7.50 と説明しています。出力には思考トークンを含み、キャッシュ等は別料金です。[モデル説明](https://ai.google.dev/gemini-api/docs/latest-model?hl=en)、[公式料金表](https://ai.google.dev/gemini-api/docs/pricing)

長期契約や顧客向け価格を設計する際は、期間限定の単価だけで採算を決められません。今の価格で試験し、予定価格でも粗利が残るかを確認する必要があります。逆に、この値上げ予定だけから Google 全体の価格支配力が確立したとまでは言えません。割引継続、競合への移行、少ないトークンで同じ仕事を処理できる改善も結果を変えます。

企業の導入費用には既存データの接続、権限の整理、ログ・監督、手直しが含まれます。Google の利点はこれらを既存の Cloud や Workspace の運用に寄せられることですが、複数の製品で提供条件が違うことは確認負担になります。

## 競争の強みと制約

Google は利用者との接点、モデル開発、独自の計算基盤、法人販売を同時に持ちます。AI が検索の利用を増やすなら広告にも利益が及び、企業が Gemini 以外を選んでも Cloud の資源が使われる可能性があります。この複数の収益経路は、モデル API を売る事業だけとは異なる強みです。

ただし、既存事業を持つことは調整の難しさも生みます。検索体験の改善が広告や外部サイトへの送客とどう両立するか、モデル性能の更新を全製品へどう配るか、膨らむ設備投資の回収をどう進めるかが論点です。利用者数が増えても、利益の増え方を同時に見る必要があります。

| 説明 | 支える事実 | 反対の材料・未確定部分 |
|---|---|---|
| 既存製品への AI 統合が成長を増幅する | 検索・Cloud の売上成長、Gemini と Antigravity の利用 | 同じ顧客群の因果効果や Gemini 単独利益は未開示 |
| Cloud の需要全体が伸び、Gemini の成功とは一部別に進む | Cloud は多様な基盤・サービスを含む | Gemini Enterprise の導入や自社 API 利用もあり、他社需要だけでは説明できない |
| 管理機能の統合で企業の移行費用が上がる | 業務データ、権限、実行管理が同じ環境へ集まる | 公開モデルや共通形式もあり、顧客が依存箇所を減らせる余地はある |

現在は一番目と二番目を分けて追うのが妥当です。売上と利用の観測があることは確かですが、そこから一つのモデルが企業市場を独占すると結論づける材料はありません。

## 経緯と次に判断を変える観測

| 時点 | 出来事 | 事業上の意味 |
|---|---|---|
| 2025年10月9日 | Gemini Enterprise 発表 | 企業の情報・仕事への入口を整備 |
| 2026年6月3日 | 投資家向けに Cloud と設備投資を説明 | 成長と供給投資を同じ資料で確認できる |
| 7月22日 | 第2四半期の成長・利用規模を説明 | 「採用の観測がない」という見方を修正する根拠 |
| 9月15日 | 3.8 Live／3.5 Transcribe 発表 | 音声と作業実行を結び付ける |
| 9月の確認状態 | 3.8 Flash、Skills、管理機能 | モデル単体から企業での運用へ広がる |

短期は Flash の導入価格と予定価格で仕事の採算が残るか、音声や Skills の提供条件が対象業務に合うかを見ます。中期は Gemini Enterprise の契約更新、部署への展開、Cloud の利益と投資回収を確認します。長期は検索・Workspace・Cloud を通じた顧客接点が、AI 利用の標準的な入口として残るかが争点です。

継続仮説は H-GOO-001（企業利用と収益）、H-GOO-002（移行の自由度）、H-GOO-003（研究と計算設備が品質を保った総費用の改善につながるか）です。同じ企業群で利用が縮む、予定価格で他社へ移る、性能改善が利用に届かないという結果があれば、統合の優位という評価を弱めます。

## 残る情報ギャップ

Gemini の単独利益率、企業の有料利用深度、利用企業の成果を揃えた比較は不足しています。旧版にあった Hassabis の組織離脱報道や、Cloud の売上を特定2社へ帰属させる推計は、今回一次資料で確定していないため、経営体制や顧客構成の事実にはしていません。

[旧版](../archive/pre-learning-2026-09-22/static_intelligence/google.md)の Antigravity 管理 API の細部は保存された収集資料へ戻れますが、今回 AI Studio の記事本文を再取得できなかったため、確定仕様は現行の開発者文書で確認できた範囲に限定しました。資料の取得不足と、会社に製品・顧客が存在しないことは区別します。
