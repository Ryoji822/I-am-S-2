# AI市場：仕事を実行する仕組みと、利益を受け取る場所の競争

基準日：2026年9月21日。9月22日に一次資料を再調査して再構成。仕様を後日確認した箇所は確認日を明記します。対象は主要5社と、それらを支える供給・制度・労働市場です。世界の全事業者を網羅した市場シェア調査ではありません。

## 現在の市場構造

**競争の対象は、モデルが回答できることから、顧客のデータを使って仕事を実行し、その利用を継続してもらうことへ広がっています。** OpenAI の Agents API、Anthropic の Claude Code／Cowork、Google の Antigravity と企業向け基盤、xAI の Grok Build、ByteDance の TRAE／Coze は、形は異なっても作業の実行に関わる製品です。[OpenAI](https://openai.com/index/introducing-the-agents-api/)、[Anthropic](https://www.anthropic.com/news/claude-sonnet-5)、[Google](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/)、[xAI](https://x.ai/news/grok-build-open-source)、[ByteDance](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity)。

顧客にとって重要なのは、モデル単体の試験点数に加え、必要なデータを読めるか、権限を守って操作できるか、失敗を検出できるか、監督込みで安くなるかです。供給企業にとっては、その仕事の入口、実行環境、計算資源のどこを売上にできるかが争点です。

| 層 | 提供するもの | 主な位置にいる企業 | 競争と利益の論点 |
|---|---|---|---|
| 計算資源 | GPU・TPU、電力、設備、クラウド | Google、Microsoft、AWS、Oracle等。xAIも自社設備 | 大きな固定費を稼働と契約で回収できるか |
| モデル | 言語・画像・音声・動画の能力 | 本資料の5社など | 品質を保った仕事当たり費用と供給条件 |
| 実行と管理 | 複数段階の作業、権限、監督、接続 | Agents API、Claude、Googleの企業基盤、Build、Coze等 | 運用負担を減らす対価と、移行の難しさ |
| 顧客の仕事場 | 開発、法務、広告、社内業務、制作 | 自社サービスとCursor・Harvey等の提携先 | 顧客関係・業務データ・成果の責任を誰が持つか |
| 消費者への配信 | 検索、対話、SNS、動画、商取引 | ChatGPT、Google、X、ByteDanceの各サービス | 発見される場所と需要を作る力 |

同じ会社が複数の層にいます。モデルを別会社へ替えられても、顧客データや監督の手順を別の実行環境へ移す費用が残ることがあります。逆に、外部モデルを選べる顧客接点はモデル供給者に対する交渉力を持ちます。

## 5社を同じ軸で比較する

| 企業 | 既にある資産・販売経路 | 直近の方向 | 事業上の制約 |
|---|---|---|---|
| OpenAI | ChatGPTの利用基盤、API、Codex、企業・専門業種への販売 | Astra、Agents API、法務への展開 | 実行の安全性、監督費、パートナーとの利益配分 |
| Anthropic | Claude、Code、Cowork、主要クラウドでの提供 | 企業の仕事と研究の実行、用途別の利用条件 | 能力向上と安全管理の両立、供給契約の実現 |
| Google | 検索・YouTube・Workspace・Cloud、TPU | モデル・仕事場・管理・計算資源を統合 | 巨額投資、製品間の条件差、既存事業との採算配分 |
| xAI | Grok、X、Build、Colossus、SpaceXへの所属 | 低めのモデル価格、外部開発ツール、公開コード | AI部門の大きな損失、設備の回収、継続利用 |
| ByteDance | Doubao、TRAE、制作製品、動画・広告・商取引の接点 | Seed2.1、Seedance2.5、企業向け基盤 | 市場別の提供差、権利処理、海外投資の費用 |

各行の根拠と経緯は [OpenAI](openai.md)、[Anthropic](anthropic.md)、[Google](google.md)、[xAI](xai.md)、[ByteDance](bytedance.md) にあります。これは売上順位ではなく、各社が利益を得ようとしている場所の比較です。

## 需要は拡大しているが、数字の意味は異なる

OpenAI は3月31日に月間売上20億ドル、企業向けが売上の40%超と説明しました。Anthropic は5月28日に年換算売上ペース470億ドルを公表しました。前者の月次値と後者の年換算値は、期間も測定方法も違い、そのまま年間売上ランキングにはできません。[OpenAIの資金・事業説明](https://openai.com/index/accelerating-the-next-phase-ai/)、[Anthropicの資金調達発表](https://www.anthropic.com/news/series-h)。

Google の7月決算説明では Cloud の前年同期比成長率82%、Gemini Enterprise は Fortune 100 の約90%が利用としています。法人需要を示す材料ですが、Cloudには他社モデル用の計算資源等も含まれ、導入企業数は全社員の有料利用率ではありません。[第2四半期の説明](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/)。

この3社には需要拡大の具体的な公表があります。一方で、利用企業側の利益や新人採用が増えたことまでは示しません。AI供給者の売上、導入企業の利益、働く人の所得を分けて追う必要があります。

## 価格競争と、実務で支払う費用

Sonnet 5 は8月10日の公式訂正で100万トークン当たり入力2ドル・出力10ドルを恒久化しました。Grok 4.6 は8月12日の発表で入力2ドル・出力6ドルからです。モデル間でトークンの切り方、思考量、品質、速度、キャッシュ条件が異なるため、出力単価だけで順位を決められません。[Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)、[Grok 4.6](https://x.ai/news/grok-4-6)。

同品質の仕事当たり費用は、モデル利用料、外部ツール、再試行、人の確認・修正、接続と運用、失敗時のやり直しを含みます。例えば安いモデルで3回やり直す仕事と、高いモデルで1回で終わる仕事では単価の優劣が逆転します。これは計算の考え方であり、本資料で各社の業務費用を実測した結果ではありません。

利用者が得られる利益は、安くなった分を販売価格に渡すか、粗利に残すか、新しい仕事を受けるかでも変わります。広告・制作・開発では、生成量が増えても顧客の予算や注意が同じなら、成果物単価だけ下がる可能性があります。需要が増えたかを、処理量とは別に測る理由です。

## 資本、供給、回収の制約

OpenAI の3月の調達はコミット済み資本1,220億ドル、Anthropic の5月の調達は650億ドルで既公表分を含みます。調達額は営業収益や利益ではありません。Google は6月の投資家説明で2026年設備投資1,800〜1,900億ドルを見込みました。資金の確保と設備が稼働する時期の間には距離があります。[OpenAI](https://openai.com/index/accelerating-the-next-phase-ai/)、[Anthropic](https://www.anthropic.com/news/series-h)、[Google](https://blog.google/alphabet/investor-presentation-june-2026/)。

SpaceX の6月5日目論見書では、Xの事業を含むAI部門の2026年1〜3月営業損失は24.69億ドルです。大規模な能力・供給の獲得が、そのまま黒字の証拠にならない例です。[目論見書 §5.4.4.3](https://content.spacex.com/cms-assets/FINAL_Documents%20and%20Updates/SpaceX%20-%20EU%20Prospectus%20%28Approved%20by%20Bafin%29%20-%20June%205%2C%202026.pdf)。

ByteDance については9月4日に Reuters が296億ドルの融資を関係者情報で報じています。契約原文で確認した確定値とは分けます。[Reuters配信記事](https://uk.marketscreener.com/news/bytedance-secures-29-6-billion-loan-in-ai-push-sources-say-ce785bdad189f22c)。資金調達、設備発注、受電、稼働、課金利用、利益回収を順番に追わなければ、供給能力を過大評価します。

## 安全と制度が変える提供条件

Anthropic の8月31日の説明は、7〜8月の事案を受けた実験・評価環境の見直しです。9月17日の Life Sciences Verification Program は、確認済みの組織に用途に応じた利用条件を設ける制度です。安全のための制約が全市場で一律に強まるというより、用途・組織・接続先に応じて細かくなる例です。[安全対応](https://www.anthropic.com/news/improving-alignment-security-efforts)、[LSVP](https://www.anthropic.com/news/life-sciences-verification-program)。

カリフォルニア州は9月18日、独立検証・監査制度の実施を早め、専門家に2か月以内の提案を求める州知事の行政命令を公表しました。常駐評価や緊急停止機能等は検討対象を含み、全てがこの日に全事業者の実施義務になったわけではありません。[州政府の説明](https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-executive-order-to-accelerate-independent-oversight-and-advance-the-creation-of-an-ai-kill-switch/)。

含意は、権限、ログ、評価、停止と復旧が、導入時の付随作業から製品選択の条件へ近づいていることです。ただし規制に対応できる大手が有利になる面と、共通の検証で新規事業者への信頼が高まる面があり、一方向の独占強化と決めつけません。

## 仕事と所得について既に分かること

Stanford の8月12日改訂研究は、米国ADPの給与データを2026年6月まで分析し、AIへの露出が高い職種の22〜25歳の雇用が、露出の低い同年代と同じ伸びをした場合より19%少ないと報告しました。主に採用減であり、経済全体の大量失業を確認したという結論ではありません。教育を考慮すると差が縮むなどの限界があり、著者も因果効果の推定と区別しています。[研究概要](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/)。

日本のJILPT調査は、2024年に雇用者2.2万人へ行ったWeb調査を2025年5月に公表したものです。AI利用者では仕事の質について改善の回答が悪化を上回り、訓練や労使の対話との関連も示しました。自己申告の過去の調査であり、2026年の全国の雇用効果ではありません。[調査No.256](https://www.jil.go.jp/institute/research/2025/256.html)。

両者は矛盾とは限りません。既に職に就く利用者の仕事が改善しながら、新人の入口が狭まることはあり得ます。企業の生産性だけを見ていると、この違いを見逃します。日本の広告・開発・管理業務については、新人求人、採用、総労働時間、実質賃金、転職後所得を別々に確認すべき段階です。

## 期間別の判断と見直し条件

短期1〜3か月は、業務ごとの品質・確認時間・供給条件を比較します。実行基盤の機能が増えたため試す価値はありますが、顧客データと手順の移行費用まで契約前に測ることが重要です。中期3か月超〜1年は、試験から本番への移行、顧客維持、利益、採用を追います。利用量増加だけで利益が残らない場合、需要拡大という評価を「処理量の拡大」に限定し直します。

長期1年超〜3年では、時間短縮が需要と所得に届くか、顧客接点・計算資源の所有者へ利益が偏るかが分岐です。若年採用の回復と実質賃金の上昇が広がれば補完の説明が強まり、採用減と利益集中が続けば分配と移行の問題が大きくなります。個人については非公開の所得実績がないため、本人の改善・悪化を代入していません。

[シナリオ別の検討](scenario-tracker.md)・[元の資料](../archive/pre-learning-2026-09-22/static_intelligence/market-overview.md)。以前の確率や断定は原本に残し、今回の判断と混ぜません。
