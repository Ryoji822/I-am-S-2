# OpenAI

> 最終判断更新: 2026-08-24
> 全体確信度: 中低
> 情報非対称性: 収益申告が同一出所（OpenAI自己申告・流出文書含む）の定義未統一系列であることが確定した: [INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043)（収益$250億・ChatGPT購読70%・API 25%・年間損失$140億・B-2）・[INFO-182](../Information/2026-08-15/collected-raw.md#INFO-182)（エンタープライズ40%超・B-1）・[INFO-119](../Information/2026-08-16/collected-raw.md#INFO-119)（交叉・事業過半・年率$40B超・B-2未監査）・[INFO-082](../Information/2026-08-17/collected-raw.md#INFO-082)（監査済FY2025収益$13.07B・純損失$39B・B-2真正性未鑑定）に加え、[INFO-157](../Information/2026-08-18/collected-raw.md#INFO-157)（9月IPO目標$1T超・月次収益約$2B・2026年損失予測約$140億・C-2）と[INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083)（Q2収益$6.7B・営業損失$12.3B/四半期・CFO「IPO 2027年またはそれ以前」・B-2・WSJ確認）が第5・第6の申告系列として加わった。Arbiter v4.68の一般規則（矛盾は独立検証まで保留・±両方向適用）を継続適用し、確度変更はS-1開示後再評価ゲート（9-10月・セグメント別監査済内訳・窓開始9/1まで8日）に登録されている。OpenAI最新ラウンド$30B銀団の貸手はJPMorgan・Morgan Stanley・SMBC・MUFGで、OpenAIは投資適格格付けを持たず自己信用で調達できず、Nvidia保証で最大$350Bファイナンス、2030年末までに$800B超の支払義務と報じられる（[INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) B-3・IND-029規模材料計上）。Astra停止はOpenAI公式文書で一次確認された（8/7判定・最大フロンティアRL実行保留・RL訓練2週間一時停止・監視オーバーヘッド推論計算の約20%・[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）。GPT-5.6公開3週間でLuna -80%・Terra -20%値下げ、アクティブユーザー10億超・ビジネス200万超を開示（[INFO-044](../Information/2026-08-22/collected-raw.md#INFO-044) B-2）。GPT-5.6がBedrock 25+リージョンで提供されOpenAI SDKがそのまま使える（[INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) A-3）。「Codex as a platform」でエージェントハーネスを第三者構築基盤として公開（[INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) A-3）。トランプ政権のAnthropic使用停止命令と同日夜にペンタゴン分類ネットワーク契約（[INFO-045](../Information/2026-08-24/collected-raw.md#INFO-045) B-2単一・EO番号なし）・AIワークロード最低3分の2の移管先に名が連なる（[INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) C-3）。Microsoftは独占アクセスを撤廃し12以上の自社モデルで公然競合（[INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) A-1・[INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097) A-1・同一TechCrunch記事2側面）。OpenAI累積調達$182.6B（[INFO-063](../Information/2026-08-01/collected-raw.md#INFO-063) A-2）。[H-OAI-001](../config/hypotheses.json) 43% low・[H-OAI-002](../config/hypotheses.json) 44% low・[H-OAI-003](../config/hypotheses.json) 3% low（v4.76全件±0%）
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はOpenAIを「収益構造の申告が同一出所内で6系列に分裂し、矛盾の解消がS-1開示（9-10月）まで構造的に保留された企業」と読んでいる。年間収益$250億・ChatGPT購読70%・API 25%という申告（[INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) B-2）はB2B支配の核心命題と定量的に矛盾する。8月に入って申告系列はさらに増えた。9月IPO目標$1T超・月次収益約$2B（年化約$250億）・2026年損失予測約$140億（[INFO-157](../Information/2026-08-18/collected-raw.md#INFO-157) C-2）と、Q2収益$6.7B（前期比+18%・減速）・営業損失$9Bから$12.3B/四半期への拡大・2026年通期最大$14B損失・CFO Friarの「IPO 2027年またはそれ以前」表明（[INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083) B-2・WSJ確認）である。Q2収益ではAnthropicの暫定$11.5Bに逆転された（WSJ見出し「rival it created just passed it」）。監査済FY2025総額$13.07B（[INFO-082](../Information/2026-08-17/collected-raw.md#INFO-082) B-2）と申告ARR $40B超と月次$2B年化$25Bは3口径が並存し、いずれもセグメント別内訳を含まない。

Arbiter v4.70はこの3口径問題をS-1開示後再評価ゲート（9-10月・セグメント別監査済内訳）に登録した。v4.76時点で窓開始（9/1）まで8日であり、KIQ-OAI-001は60R/61R連続不在である。ゲート到達まで[H-OAI-001](../config/hypotheses.json)の43% lowは固定され、矛盾のいずれの方向への解消も保留される（v4.68一般規則・±両方向適用）。

[H-OAI-001](../config/hypotheses.json)は43% lowで、v4.64の-1%（44→43%）以降12ラウンド連続±0%である。44%固定9R連続を強制再評価メカニズムで打破した後、確度変更の条件はS-1セグメント別監査済内訳に一本化された。Microsoftが独占アクセスを撤廃し12以上の自社モデルで公然競合する構造（[INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) A-1・[INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097) A-1・同一記事2側面）は継続している。

安全性ガバナンス面では、Astra停止が公式文書で一次確認された。OpenAIは「サイバー重要能力時代のモデル開発ペーシング」を発表し、Astraが8/7にCriticalサイバー能力閾値到達の可能性と判定されたこと、最大の計画フロンティアRL実行を保留していること、RL訓練を2週間一時停止したことを明らかにした。多段階監視（活性分類器が全サンプルトークンで稼働・重大違反は30分で停止）は監視対象推論計算の約20%を追加消費する（[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）。08-12報道（[INFO-002](../Information/2026-08-12/collected-raw.md#INFO-002) B-2）がA-1公式文書で裏づけられた形である。ChatGPTのコンピュータ横断アクション機能でも、OpenAI自身が生体リスクで「high capability」に自己分類しライブモニタリングとユーザー承認を適用している（[INFO-025](../Information/2026-08-24/collected-raw.md#INFO-025) B-3）。

政府B2Bは再編期に入った。トランプ大統領が米政府機関にAnthropic製品の使用停止を命令し、ヘグセス国防長官が同社を「サプライチェーン・リスク」に指定（6ヶ月の段階的排除）、同日にOpenAIがペンタゴンの分類ネットワークでのAIモデル展開契約に到達したと発表した（[INFO-045](../Information/2026-08-24/collected-raw.md#INFO-045) B-2・単一ソースでEO番号・日付の記載なし）。ペンタゴンがAIワークロードの最低3分の2をAnthropicからOpenAI・Google・Microsoftへ移管するとの報道も加わった（[INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) C-3）。Arbiter v4.76はINFO-045を判別監視項目（EO番号・一次文書の確認待ち）としC計上トリガーとはしなかったが、安全性拒否企業が罰せられ順応企業が報われる構造は[H-GOV-002](../config/hypotheses.json)の順応報酬読みを強化する方向にある。

製品・価格・金融面の事実は3層である。第一に、GPT-5.6公開3週間後の値下げ（Luna -80%・Terra -20%）と、アクティブユーザー10億超・ビジネス200万超の開示（[INFO-044](../Information/2026-08-22/collected-raw.md#INFO-044) B-2）。API下限はLuna $0.20/M入力で、Sonnet 5・Terra・Gemini 3.1 Proが同額$2で並ぶ「$2帯主戦場」にある（[INFO-060](../Information/2026-08-24/collected-raw.md#INFO-060) C-2）。第二に、GPT-5.6ファミリーがAmazon Bedrock 25+リージョンで提供され、OpenAI SDKクライアントをBedrock互換エンドポイントに向けるだけで移行できる（[INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) A-3・スイッチングコスト低下方向）。「Codex as a platform」は会話状態管理・サンドボックス・承認ポリシー強制を含むハーネスを第三者が構築基盤として使える公開プラットフォームであり、Blaxel等の第三者実行環境も接続できる（[INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) A-3）。実行環境のロックイン競争がOpenAI側で明示的にAPI化された一方、接続先は開放されている。第三に、$30B銀団（JPM・MS・SMBC・MUFG）・投資適格なし・Nvidia保証$350B・2030年末$800B超の支払義務という債務構造の報道である（[INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) B-3）。v4.76はこれを規模材料（金融条件の緩さはSCN-BS-003発火トリガー側の逆方向）として[IND-029](../config/indicators.json)に記録し、確率変更根拠とはしなかった。

KIQ-OAI-001は60R/61R連続不在が継続する。収益内訳の大分類（ChatGPT 70%・API 25%・その他5%）は判明したが、API 25%の政府/民間内訳とセグメント別監査済数値が不明であり、この最後の区分が[H-OAI-001](../config/hypotheses.json)の43%と40%（low帯中央）の分岐点になる。Intelligence IndexではOpus 5（63.1）> GPT-5.6 Sol（60.9）> Kimi K3（59.7）の順位が続く（[INFO-047](../Information/2026-08-12/collected-raw.md#INFO-047) B-2）。フロンティア性能の相対的劣位は変わっていない。

## 1. コア判断

全体確信度は中低。本ラウンドの最重要判断は8つある。第一に、S-1関連申告の6系列分裂と再評価ゲート（9-10月）への保留確定。第二に、Astra停止の公式文書による一次確認（A-1）とペーシング運用の具体化。第三に、Anthropic排除・OpenAI配備という政府調達再編の構造化。第四に、$30B銀団と$800B超支払義務の債務構造報道（規模材料計上）。第五に、GPT-5.6値下げと10億ユーザー開示によるコモディティ化圧力と消費者基盤の確定。第六に、Bedrock 25+とCodex platformで進む配給の多チャネル化とハーネスAPI化。第七に、収益構造可視化に基づくH-OAI-001 43% lowの12R連続±0%（v4.64強制再評価の成果定着）。第八に、Microsoft-OpenAI排他関係終焉の継続。

### S-1系列の分裂・9月IPO・再評価ゲート（08-18〜08-24バッチ）

機密S-1をめぐる情報は3波に分かれて流通した。第1波（08-17）は監査済FY2025財務である: 収益$13.07B（前年比約3倍）・支出$34B・純損失$39B・S-1申告評価額$730B（[INFO-082](../Information/2026-08-17/collected-raw.md#INFO-082) B-2・真正性未鑑定）。第2波（08-18）はIPO日程である: 2026年9月上場目標・評価$1T超・提出書類の月次収益約$2B（年化約$250億）・2026年損失予測約$140億（[INFO-157](../Information/2026-08-18/collected-raw.md#INFO-157) C-2）。第3波（08-22）は漏洩文書の四半期明細である: Q2収益$6.7B（前期比+18%・減速）・Anthropic Q2暫定$11.5Bへの逆転・営業損失$9Bから$12.3B/四半期への拡大・2026年通期最大$14B損失・CFO Friarの「IPO 2027年またはそれ以前」（[INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083) B-2・WSJ確認）。

3波は相互に口径が揃わない。監査済年額$13.07B・申告ARR $40B超（[INFO-083](../Information/2026-08-17/collected-raw.md#INFO-083) B-2・[INFO-145](../Information/2026-08-17/collected-raw.md#INFO-145) B-2）・月次$2Bの年化$25Bが並存し、いずれもセグメント別内訳を欠く。Arbiter v4.70は3口径問題の中核として同一出所矛盾処理規則を継続適用し、S-1開示後再評価ゲート（9-10月・セグメント別監査済内訳）を登録した。IPO 9月目標（INFO-157）自体もC-2品質の流出報道であり、公的S-1提出の確認が先決である。Q2のAnthropic逆転は、OpenAIが作った競合に収益で抜かれた初の定点観測点として記録価値が高い。

### 収益構造の可視化とB2B支配核心命題との矛盾

OpenAIの年間収益$250億の内訳が初めて定量的に判明した（[INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) B-2）。ChatGPT購読70%（5000万+有料シート）・API 25%・Sora/広告/ライセンス5%であり、年間損失は$140億に達する。仮にAPI 25%の全てがB2Bであっても、収益の25%がB2Bである構造は「B2B支配」という核心命題と整合しない。70%消費者収益の判明自体が、B2Bが収益の少数（30%以下）であることをすでに示しており、核心命題矛盾は政府/民間区分の不在に関わらず成立する。Arbiter v4.64はこの論理をH-OAI-001 -1%（44→43%）の直接根拠とした。

この70%申告は同一出所の定義未統一系列のひとつであり、8/14の「事業過半」申告（[INFO-145](../Information/2026-08-17/collected-raw.md#INFO-145) B-2）と直接矛盾する。当事者の最新申告での矛盾解消は認められず、独立検証まで保留される（v4.68一般規則）。アクティブユーザー10億超・ビジネス200万超の新開示（[INFO-044](../Information/2026-08-22/collected-raw.md#INFO-044) B-2）も消費者規模の大きさを再確認するもので、B2B支配命題の直接証拠ではない。

### H-OAI-001 43% lowの論理と12R連続±0%

[H-OAI-001](../config/hypotheses.json)の43%は、3段階の累積である。4R連続-1%（v4.50-v4.53）で44% low移行、9R連続±0%（v4.54-v4.63）の後、v4.64強制再評価メカニズムで-1%（44→43%）である。以降v4.65からv4.76まで12ラウンド連続±0%であり、変更条件はS-1セグメント別監査済内訳の確認に一本化された。Blue Agentの±1%提案（INFO-119矛盾の動的解消など）はv4.68・v4.76で連続却下され、未解決矛盾を中核根拠とする変更不採用の裁定が安定している。43%はlow帯内の保守的配置である。

### Microsoft-OpenAIの排他関係終焉

Microsoftが2026年4月のパートナーシップ更新でOpenAIの独占アクセスを撤廃した（[INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) A-1）。ChatGPTがMicrosoft Bingと直接競争する関係になった。Microsoftは12以上の自社モデル（MAI-1含む）を発表し、Nadellaは「Mythosの半分のコストで同等以上の性能」「ハーネスをモデルから分離し、いつでも交換可能であるべき」とpositioningした（[INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097) A-1）。Azure FoundryでのGPT-5.6（Sol/Terra/Luna・1.05Mコンテキスト・multi-agent orchestration preview）販売は競争と配給の併存である（[INFO-024](../Information/2026-08-24/collected-raw.md#INFO-024) A-3）。[INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084)と[INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097)は同一TechCrunch記事の2側面であり、独立第2A-1ソースの確認が依然未解決である。

### Astra停止の一次確認と安全性ガバナンス

OpenAIが次世代モデルAstraの展開をPreparedness Frameworkに基づき停止した報道（[INFO-002](../Information/2026-08-12/collected-raw.md#INFO-002) B-2）は、公式文書「サイバー重要能力時代のモデル開発ペーシング」で一次確認された（[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）。要点は5つである。Astraは8/7にCriticalサイバー能力閾値到達の可能性と判定された。最大の計画フロンティアRL実行は小規模評価で整合性証拠が蓄積するまで保留される。RL訓練は2週間一時停止された。OpenAI-Hugging Faceインシデントを受けた監視強化（活性分類器・自動調査・30分以内アラート・重大違反は30分で活動停止）は監視対象推論計算の約20%を追加消費する。「モデルが大半のセキュリティ業務を担う未来」が明示された。フロンティアモデル安全性ガバナンスの最初の重大停止決定が、停止だけでなく計測可能な運用コスト（監視20%）を伴うことが確定した意義は大きい。

### 政府B2Bの再編: Anthropic排除とワークロード移管

国防総省の分類ネットワークでの契約は「same red lines plus a third」条件で報じられ（[INFO-046](../Information/2026-08-16/collected-raw.md#INFO-046) B-2）、GenAI.milの利用者は120万人・生成agentは10万に達する（[INFO-047](../Information/2026-08-16/collected-raw.md#INFO-047) B-2）。08-24バッチでは再編が一段深くなった。トランプ大統領のAnthropic製品使用停止命令・ヘグセス長官の「サプライチェーン・リスク」指定（6ヶ月段階的排除）と同日に、OpenAIがペンタゴン分類ネットワークでのモデル展開契約に到達したと発表した（[INFO-045](../Information/2026-08-24/collected-raw.md#INFO-045) B-2・単一ソース・EO番号なし）。ペンタゴンがAIワークロードの最低3分の2をOpenAI・Google・Microsoftへ移管する報道（[INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) C-3）が続く。Arbiter v4.76はINFO-045を判別監視項目（EO番号・一次文書待ち・KIQ-GOV-EO）とし、C計上トリガーからは除外した。N=1問題（Anthropic強制の実質26R）は継続し、OpenAIは強制を経ていない自発的順応の候補事例としてH-GOV-001の抑止効果代替解釈に併記される（v4.68義務化）。

### H-OAI-002・H-OAI-003の現状

[H-OAI-002](../config/hypotheses.json)は44% lowで±0%（v4.76）。囲い込み否定証拠の累積に加え、配給の多チャネル化が進んだ。GPT-5.6のBedrock 25+リージョン展開はOpenAI SDKをそのまま使える接続である（[INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) A-3）。一方で「Codex as a platform」は、会話状態管理・実行ストリーミング・サンドボックスと承認ポリシーの強制・作業の横断継続を含むハーネスを第三者構築の土台として提供し（[INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) A-3）、プロプライエタリ上位レイヤーの構築という命題のC方向でもある。SandboxAgent/ManifestでBlaxel等の第三者実行環境を接続できる点は開放方向であり、両義的な展開である。スイッチングコストは初期投資の2.3〜5.7倍（[INFO-033](../Information/2026-08-01/collected-raw.md#INFO-033) C-2）と高いが、プロトコル層での排他性はない。Private Safety Processing（ゼロデータ保持・SOC 2/HIPAA/ISO 42001/FedRAMP対応、[INFO-013](../Information/2026-08-24/collected-raw.md#INFO-013) B-3）は規制産業向けの認証訴求である。

[H-OAI-003](../config/hypotheses.json)は3% lowで±0%。商業化規模（累積調達$182.6B・$30B銀団・ペンタゴン分類NW・2030年末$800B超の支払義務）が圧倒的に継続している。AstraのRL保留は安全性による減速であるが、商業化優先の行動パターンの反転を意味せず、AGI最優先を支持するA-2+品質の独立証拠は不在のままである。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | S-1漏洩第2弾: Q2収益$6.7B（+18%減速）・Anthropic Q2暫定$11.5Bに逆転・営業損失$12.3B/四半期・2026年最大$14B損失・CFO「IPO 2027年またはそれ以前」 | 同一出所矛盾系列の追加申告。3口径問題（$13.07B監査済 vs $40B ARR vs 月次$2B年化）の深化。S-1ゲート（9-10月）登録 | B-2 | [INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083) |
| 高 | Astra公式ペーシング文書: 8/7 Criticalサイバー判定・最大フロンティアRL保留・RL訓練2週間一時停止・監視は推論計算の約20%消費 | 安全性ガバナンスの一次確認（B-2報道がA-1に格上げ）。停止の計測可能な運用コスト確定 | A-1 | [INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) |
| 高 | 9月IPO目標$1T超・月次収益約$2B（年化約$250億）・2026年損失予測約$140億 | IPO日程の初出。S-1開示後再評価ゲートの起動点。C-2流出報道で公的提出確認が先決 | C-2 | [INFO-157](../Information/2026-08-18/collected-raw.md#INFO-157) |
| 高 | $30B銀団（JPM・MS・SMBC・MUFG）・投資適格なし・Nvidia保証で最大$350B・2030年末$800B超支払義務・2027年末までにもう1回大型調達 | 財務持続性リスクの構造化。[IND-029](../config/indicators.json)規模材料計上（金融条件の緩さはSCN-BS-003発火と逆方向） | B-3 | [INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) |
| 高 | トランプ政権のAnthropic使用停止命令・ヘグセス「サプライチェーン・リスク」指定と同日のOpenAIペンタゴン分類NW契約・ワークロード最低3分の2移管先 | 政府B2B再編の構造化。順応報酬構造の強化。ただしINFO-045は単一B-2でEO番号なし（v4.76判別監視項目） | B-2/C-3 | [INFO-045](../Information/2026-08-24/collected-raw.md#INFO-045) [INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) |
| 高 | GPT-5.6公開3週間で値下げ（Luna -80%・Terra -20%）・アクティブユーザー10億超・ビジネス200万超 | [H-OAI-001](../config/hypotheses.json) I方向（価格コモディティ化）と消費者基盤規模の同時確認 | B-2 | [INFO-044](../Information/2026-08-22/collected-raw.md#INFO-044) |
| 高 | LLM API下限Luna $0.20/M・Sonnet 5・Terra・Gemini 3.1 Proが同額$2で並ぶ$2帯主戦場・価格は3桁の幅 | [IND-025](../config/indicators.json)コモディティ化圧力。トークン価格に単一の答えなし | C-2 | [INFO-060](../Information/2026-08-24/collected-raw.md#INFO-060) |
| 高 | Codex as a platform: ハーネス（状態管理・サンドボックス・承認強制）を第三者構築基盤に公開・Blaxel等リモート実行環境接続可 | [H-OAI-002](../config/hypotheses.json)両義。実行環境ロックインのAPI化（C）と第三者接続可（開放）の併存 | A-3 | [INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) |
| 高 | GPT-5.6（Sol/Terra/Luna）がBedrock 25+リージョンで提供・OpenAI SDKそのまま利用可・クロスリージョン推論 | [H-OAI-002](../config/hypotheses.json)囲い込み否定方向。スイッチングコスト低下。マルチクラウド標準化 | A-3 | [INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) |
| 高 | ChatGPTコンピュータ横断アクション機能・OpenAI自身が生体リスクで「high capability」に自己分類しライブモニタリング+ユーザー承認の最厳格プロトコル適用 | [IND-013](../config/indicators.json)強化。Astra停止と同じ自己分類体系の消費者面適用 | B-3 | [INFO-025](../Information/2026-08-24/collected-raw.md#INFO-025) |
| 高 | 機密S-1流出: FY2025監査済収益$13.07B・支出$34B・純損失$39B・S-1申告評価額$730B（$1T比▲27%） | 財務持続性リスクの定量化。セグメント別内訳不在でB2B命題への転用はv4.69が排除 | B-2 | [INFO-082](../Information/2026-08-17/collected-raw.md#INFO-082) |
| 高 | ARR>$40B（2四半期前倒し）・エンタープライズ>コンシューマー初・広告$1B ARR接近・経営層交代（COO Lightcap・CRO Dresser退任） | 同一出所矛盾系列。v4.68規則で独立検証まで保留（±両方向） | B-2 | [INFO-083](../Information/2026-08-17/collected-raw.md#INFO-083) [INFO-145](../Information/2026-08-17/collected-raw.md#INFO-145) |
| 高 | 収益$250億/年内訳判明: ChatGPT 70%・API 25%・$140億赤字 | [H-OAI-001](../config/hypotheses.json) I方向・核心命題との定量的矛盾（v4.64 -1%の直接根拠） | B-2 | [INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) |
| 高 | H-OAI-001 43% low・v4.64以降12R連続±0%・確度変更はS-1ゲートに保留・Blue ±1%提案はv4.68/v4.76で連続却下 | [H-OAI-001](../config/hypotheses.json)確度帯安定。未解決矛盾の中核根拠化禁止が定着 | Arbiter | [Arbiter v4.76](../state/arbiter-2026-08-24.md) |
| 高 | GPT-5.6-Cyber（Daybreak）: サイバーセキュリティ特化モデル・AWS展開 | 新モデルリリース・[H-OAI-001](../config/hypotheses.json) C方向 | A-3 | [INFO-001](../Information/2026-08-12/collected-raw.md#INFO-001) [INFO-004](../Information/2026-08-12/collected-raw.md#INFO-004) |
| 高 | Microsoftが独占アクセス撤廃・12以上の自社モデルで公然競合・ChatGPT vs Bing直接競争 | [H-OAI-001](../config/hypotheses.json) I方向の構造的圧力。但し同一TechCrunch記事依存 | A-1 | [INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) [INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097) |
| 高 | Azure FoundryでGPT-5.6販売（1.05Mコンテキスト・multi-agent orchestration preview） | 競争と配給の併存。排他関係終焉の継続確認 | A-3 | [INFO-024](../Information/2026-08-24/collected-raw.md#INFO-024) |
| 高 | OpenAI累積調達$182.6B・AI投資が全スタートアップ投資の過半数 | [IND-029](../config/indicators.json) high。資本動員力は圧倒的 | A-2 | [INFO-063](../Information/2026-08-01/collected-raw.md#INFO-063) |
| 高 | Codex Terminal-Bench 2.1首位88.8%・週間300万アクティブ・npm DL 177倍増 | [H-OAI-001](../config/hypotheses.json) C方向（コーディングエージェント分野）。Codex platform化で配信拡大 | B-1/B-2 | [INFO-061](../Information/2026-08-01/collected-raw.md#INFO-061) [INFO-098](../Information/2026-08-01/collected-raw.md#INFO-098) |
| 中 | Private Safety Processing: フロンティア対象ゼロデータ保持・SOC 2/HIPAA/ISO 42001/FedRAMP/EU AI Act対応 | 規制産業向けエンタープライズ展開の認証訴求 | B-3 | [INFO-013](../Information/2026-08-24/collected-raw.md#INFO-013) |
| 中 | SynchronyがChatGPTショッピング体験に統合（アジェンティック・コマースの金融接続） | 消費者収益の新ライン（広告$1B ARR接近申告との整合） | B-2 | [INFO-023](../Information/2026-08-24/collected-raw.md#INFO-023) |
| 中 | スイッチングコスト初期投資の2.3-5.7倍・完全移行18-36ヶ月 | 囲い込みの新メカニズム（データ・習慣・agentロジック）。但しプロトコル層での排他性なし | C-2 | [INFO-033](../Information/2026-08-01/collected-raw.md#INFO-033) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| 公的S-1が提出され、セグメント別監査済収益内訳が確認される | KIQ-OAI-001完全解決点。同一出所6申告の矛盾（70%消費者vs事業過半vs $40B ARR vs 月次$2B）が解消または確定し、[H-OAI-001](../config/hypotheses.json) 43%の再評価が可能になる | 9-10月（IPO 9月目標） | [H-OAI-001](../config/hypotheses.json) |
| IPO 9月目標の公的確認または延期報道 | ゲート日程の確定または再設定。評価額$1T超の市場受容がSCN-BS-003/IND-029需要側の再評価点 | 90日 | [IND-029](../config/indicators.json) |
| 銀団価格条件（スプレッド・コベナント・割当）の確定報道 | $30B銀団の規模材料が価格材料に転換し、SCN-BS-003中間閾値(d)の評価が始まる。searched-absenceエンドポイントは残り2R | 常時 | [IND-029](../config/indicators.json) |
| INFO-045のEO番号・一次文書が確認される | H-GOV-001/002の強制層評価が再開し、政府調達再編の確定事実として[H-OAI-001](../config/hypotheses.json)政府B2BのC計上が可能になる | 30日 | [IND-030](../config/indicators.json) |
| Microsoft-OpenAI競争動態が独立第2A-1ソースで確認される | 43% lowの更なる低下。パートナーシップ成熟ではなく構造的変容と判定 | 90日 | [H-OAI-001](../config/hypotheses.json) |
| [H-OAI-001](../config/hypotheses.json) が40%を割る | low帯内での更なる低下。「B2B支配的地位確立」仮説の棄却水準接近 | 180日 | [H-OAI-001](../config/hypotheses.json) |
| AI価格戦争の下落トレンドが反転しフロンティア価格が上昇に転じる | コモディティ化の不可逆的加速判断が崩れる | 180日 | [IND-025](../config/indicators.json) |
| 構造的赤字が収益到達後も持続し、損益均衡の目途が立たない（2026年最大$14B損失予測の実現） | 規模経済到達前投資の解釈が崩れる。$800B超支払義務との整合評価が必須化 | 180日 | [H-OAI-001](../config/hypotheses.json) |
| 安定性危機が長期化し、エンタープライズ顧客のChurnが定量報告される | B2B支配の持続性が直接挑戦される | 90日 | [IND-026](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | OpenAIは2026年内にAgent機能を全面的にエンタープライズ向けに特化させ、B2B市場での支配的地位を確立する | 43% low | -5%（48→43%）: 4R連続-1%(v4.50-v4.53) + 9R連続±0%(v4.54-v4.63) + v4.64強制再評価-1%。収益70%消費者（[INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) B-2）=核心命題との定量的矛盾。以降v4.65-v4.76で12R連続±0%・確度変更はS-1開示後再評価ゲート（9-10月・セグメント別監査済内訳）に保留（v4.70登録）。同一出所6申告の定義未統一（70%消費者vs事業過半vs $40B ARR vs 監査済$13.07B vs 月次$2B年化$25B・[INFO-157](../Information/2026-08-18/collected-raw.md#INFO-157) C-2・[INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083) B-2）は独立検証まで保留（v4.68規則・±両方向）。Q2 $6.7B減速・Anthropic逆転・営業損失$12.3B/四半期=I文脈。C強化: ペンタゴン分類NW再編（[INFO-045](../Information/2026-08-24/collected-raw.md#INFO-045) B-2単一・[INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) C-3・判別監視項目扱い）・Codex platform・Bedrock 25+。KIQ-OAI-001 60R/61R不在。43%はlow帯内の保守的配置 | [INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) [INFO-063](../Information/2026-08-01/collected-raw.md#INFO-063) [INFO-061](../Information/2026-08-01/collected-raw.md#INFO-061) [INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) | [INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) [INFO-082](../Information/2026-08-17/collected-raw.md#INFO-082) [INFO-056](../Information/2026-08-01/collected-raw.md#INFO-056) [INFO-013](../Information/2026-08-01/collected-raw.md#INFO-013) [INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097) [INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083) |
| [H-OAI-002](../config/hypotheses.json) | OpenAIはSkills/Shell/Compactionの独自実行環境でAgent開発者を囲い込み、MCP準拠の開放エコシステム上にプロプライエタリな上位レイヤーを構築する | 44% low | ±0%（v4.76）。囲い込み否定累積継続: Agents SDK provider-agnostic（[INFO-006](../Information/2026-08-01/collected-raw.md#INFO-006) A-3）・MCP全社採用・Bedrock 25+リージョンでOpenAI SDKそのまま利用可（[INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) A-3・スイッチングコスト低下方向）。C方向: Codex as a platform（[INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) A-3）がハーネス（状態管理・サンドボックス・承認強制）のプラットフォーム商品化を明示。ただしBlaxel等第三者実行環境の接続可という開放面が同一発表内に併存し、単独の囲い込み証拠ではない。スイッチングコスト2.3-5.7倍（[INFO-033](../Information/2026-08-01/collected-raw.md#INFO-033) C-2）は高いがプロトコル層での排他性なし。low帯確定度増加 | [INFO-006](../Information/2026-08-01/collected-raw.md#INFO-006) [INFO-093](../Information/2026-08-01/collected-raw.md#INFO-093) [INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) | [INFO-033](../Information/2026-08-01/collected-raw.md#INFO-033) [INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) |
| [H-OAI-003](../config/hypotheses.json) | OpenAIはAGI/スーパーインテリジェンス達成を最優先目標とし、商業化と並行して研究開発に大規模資源を投入する | 3% low | ±0%（v4.76）。商業化規模（累積調達$182.6B・$30B銀団JPM/MS/SMBC/MUFG・Nvidia保証$350B・2030年末$800B超支払義務 [INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) B-3・ペンタゴン分類NW・政府持分5%提案）圧倒的継続。Astra RL保留（[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）は安全性による減速であってAGI最優先の証拠ではなく、監視コスト20%は商業運用の一部。AGI最優先支持A-2+証拠不在 | (該当なし) | [INFO-063](../Information/2026-08-01/collected-raw.md#INFO-063) [INFO-042](../Information/2026-08-01/collected-raw.md#INFO-042) [INFO-082](../Information/2026-08-17/collected-raw.md#INFO-082) [INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントでcritical | Astra停止の公式一次確認（8/7 Criticalサイバー判定・RL保留・監視~20%・[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）・ChatGPT computer-useの自己分類「high capability」と最厳格プロトコル適用（[INFO-025](../Information/2026-08-24/collected-raw.md#INFO-025) B-3）・OpenAI自律エージェント サンドボックス脱出→HF侵害（[INFO-087](../Information/2026-08-01/collected-raw.md#INFO-087) B-1）・UK AISI評価（[INFO-063](../Information/2026-08-12/collected-raw.md#INFO-063) B-1）・ClawHavoc 1,184悪意スキル（[INFO-032](../Information/2026-08-01/collected-raw.md#INFO-032) B-2）。critical移行条件（A-2品質実被害報告）未到達。high/rising | 2026-08-24 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | Intelligence Index Opus 5(63.1)>GPT-5.6 Sol(60.9)>Kimi K3(59.7)（[INFO-047](../Information/2026-08-12/collected-raw.md#INFO-047) B-2）・API下限Luna $0.20/M・$2帯主戦場（Sonnet 5・Terra・Gemini 3.1 Pro同額）・価格3桁の幅（[INFO-060](../Information/2026-08-24/collected-raw.md#INFO-060) C-2）・GPT-5.6公開3週間でLuna -80%・Terra -20%（[INFO-044](../Information/2026-08-22/collected-raw.md#INFO-044) B-2）・OSS性能ギャップ継続。天井効果継続。elevated/stable | 2026-08-24 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | McKinsey 62%実験/23%本番（[INFO-032](../Information/2026-08-12/collected-raw.md#INFO-032) B-2）・Capgemini 2%大規模展開のみ（[INFO-015](../Information/2026-08-12/collected-raw.md#INFO-015) B-2）・17日間安定性危機（[INFO-013](../Information/2026-08-01/collected-raw.md#INFO-013) B-3）。Codex as a platform（[INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) A-3）は本番エージェント基盤の供給拡大であって到達率の実測ではない。期待-実態ギャップ確定的深化。high/rising | 2026-08-24 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | MCP 2026-07-28 RC stateless・AAIF Agent Plugins 1.0・OpenAI Agent Plugins 5社共同・AWS Bedrock AgentCore runtime instances・AgentCore Payments GA・旧Bedrock AgentsはClassicへ終息（[INFO-034](../Information/2026-08-24/collected-raw.md#INFO-034) A-3）・GPT-5.6のBedrock 25+リージョン展開（[INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) A-3）。マルチクラウド標準化とプラットフォーム世代交代の並行。high/rising | 2026-08-24 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | ARC-AGI-3 Opus 5 30.2%（3月<1%→7月）・Astra数学未解決問題10問解決（[INFO-065](../Information/2026-08-12/collected-raw.md#INFO-065) B-1）・AstraのRL保留は「安全性による減速」の最初の公式運用例（[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）・Hassabis 2030±1年・Altman「シンギュラリティ」。RSI概念具体化と限界の同時進行。high/rising | 2026-08-24 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | OpenAI累積調達$182.6B（[INFO-063](../Information/2026-08-01/collected-raw.md#INFO-063) A-2）・最新ラウンド$30B銀団（JPM/MS/SMBC/MUFG・投資適格なし・Nvidia保証で最大$350B・2030年末$800B超支払義務・[INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) B-3）は規模材料計上（v4.76・金融条件の緩さはSCN-BS-003発火トリガー側の逆方向）。銀団価格条件はsearched-absence R1/3消費（残り2R・128検索で不在）。S-1開示後再評価ゲート窓開始（9/1）まで8日。high/rising | 2026-08-24 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。Anthropic使用停止命令・サプライチェーン・リスク指定とOpenAI分類NW契約の同日並走（[INFO-045](../Information/2026-08-24/collected-raw.md#INFO-045) B-2単一・EO番号なしでv4.76は判別監視項目[KIQ-GOV-EO]として保留）・ワークロード2/3移管報道（[INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) C-3）・Astra Critical判定の公式確認（[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）。N=1実質26R（COMPLETE復帰で加算再開）・再開トリガー3種不出現。KIQ-MIL-001 60R/61R継続不在。IND-030-SCN-BS-001連動 | 2026-08-24 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-08-24 | 全面書き直し（7日freshness timeout・08-18/19/22/23/24バッチ初回計上）。S-1系列の3波（9月IPO目標$1T+ [INFO-157](../Information/2026-08-18/collected-raw.md#INFO-157) C-2・Q2収益$6.7B減速とAnthropic逆転・営業損失$12.3B/四半期 [INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083) B-2）とS-1開示後再評価ゲート（9-10月）登録・Astra公式ペーシング文書の一次確認（[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）・GPT-5.6値下げと10億ユーザー開示（[INFO-044](../Information/2026-08-22/collected-raw.md#INFO-044) B-2）・Bedrock 25+（[INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) A-3）・$30B銀団と$800B超支払義務（[INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) B-3・IND-029規模材料）・Anthropic排除とペンタゴン再編（[INFO-045](../Information/2026-08-24/collected-raw.md#INFO-045) B-2・[INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) C-3）・Codex as a platform（[INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) A-3）を新規反映。H-OAI-001/002/003全件±0%（v4.76・確度変更はS-1ゲートに保留）。KIQ-OAI-001 56R/57R→60R/61R・KIQ-MIL-001 56R/57R→60R/61R（DEGRADED 3R不算入）。全7指標last_checked 2026-08-24更新。Arbiter v4.76 COMPLETE | freshness 7d・[INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083) [INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) [INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) | H-OAI-001 43%（±0%）・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |
| 2026-08-12 | 全面書き直し。H-OAI-001 -1%（44→43%・強制再評価メカニズム発動・収益70%消費者がB2B支配核心命題と定量的矛盾・44%固定9R打破）を反映。収益$250億/年内訳判明（[INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) B-2）・Astra停止（[INFO-002](../Information/2026-08-12/collected-raw.md#INFO-002) B-2）・GPT-5.6-Cyber/Daybreak（[INFO-001](../Information/2026-08-12/collected-raw.md#INFO-001)/[INFO-004](../Information/2026-08-12/collected-raw.md#INFO-004) A-3）・GPT-5.6 Sol更新/Luna無料化（[INFO-003](../Information/2026-08-12/collected-raw.md#INFO-003) A-3）・Sandbox Agent+Cloudflare（[INFO-027](../Information/2026-08-12/collected-raw.md#INFO-027) A-3）を新規反映。KIQ-OAI-001 47R/48R→49R/50R（収益内訳判明・政府/民間区分不明）・KIQ-MIL-001 47R/48R→49R/50R。全7指標last_checked更新。Arbiter v4.64 COMPLETE | [INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) [INFO-001](../Information/2026-08-12/collected-raw.md#INFO-001) [INFO-002](../Information/2026-08-12/collected-raw.md#INFO-002) | H-OAI-001 44→43%・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |
| 2026-08-08 | ターゲット編集（freshness 7d）。BenchLM GPT-5.6 Sol 98/100(3位)・Intelligence Index 59(3位)（[INFO-051](../Information/2026-08-08/collected-raw.md#INFO-051) B-1）・Copilot 20Mユーザー（[INFO-065](../Information/2026-08-08/collected-raw.md#INFO-065) B-1）・AGIタイムライン Amodei 2027/Altman「特異点」（[INFO-071](../Information/2026-08-08/collected-raw.md#INFO-071) A-1）・米政府強力AIモデル事前承認（[INFO-072](../Information/2026-08-08/collected-raw.md#INFO-072) A-1）を新規反映。H-OAI-001 44% low・v4.53以降7R連続±0%で安定化。KIQ-OAI-001 39R/40R→47R/48R・KIQ-MIL-001 39R/40R→47R/48R。全7指標last_checked更新。Arbiter v4.60 COMPLETE | freshness 7d・[INFO-051](../Information/2026-08-08/collected-raw.md#INFO-051) [INFO-065](../Information/2026-08-08/collected-raw.md#INFO-065) [INFO-071](../Information/2026-08-08/collected-raw.md#INFO-071) | H-OAI-001 44%（±0%・7R安定化）・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |
| 2026-08-01 | 全面書き直し。H-OAI-001 medium→low移行（48% medium→44% low・4R連続-1%）を反映。Microsoft-OpenAI構造的パートナーシップ変容（[INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) A-1・[INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097) A-1）・GPT-5.6大幅値下げ Luna 80%減（[INFO-056](../Information/2026-08-01/collected-raw.md#INFO-056) A-2）・17日間安定性危機（[INFO-013](../Information/2026-08-01/collected-raw.md#INFO-013) B-3）・累積調達$182.6B（[INFO-063](../Information/2026-08-01/collected-raw.md#INFO-063) A-2）・Agents SDK進化（[INFO-006](../Information/2026-08-01/collected-raw.md#INFO-006) A-3）・Codex Terminal-Bench首位/300万WAU（[INFO-061](../Information/2026-08-01/collected-raw.md#INFO-061) B-2・[INFO-098](../Information/2026-08-01/collected-raw.md#INFO-098) B-1）・ペンタゴン8社契約/上院自律型兵器規則承認（[INFO-042](../Information/2026-08-01/collected-raw.md#INFO-042) A-2・[INFO-088](../Information/2026-08-01/collected-raw.md#INFO-088) A-1）を新規反映。KIQ-OAI-001 35R/36R→39R/40R・KIQ-MIL-001 35R/36R→39R/40R。Arbiter v4.53 COMPLETE | [INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) [INFO-056](../Information/2026-08-01/collected-raw.md#INFO-056) [INFO-063](../Information/2026-08-01/collected-raw.md#INFO-063) [INFO-013](../Information/2026-08-01/collected-raw.md#INFO-013) | H-OAI-001 48% medium→44% low・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |
| 2026-07-28 | ターゲット編集（freshness 7d + INFO-080/091）。クラウド支出計画$7,500億への引き上げ（[INFO-091](../Information/2026-07-28/collected-raw.md#INFO-091) B-1）・OpenAI自律エージェント サンドボックス脱出→HF侵害（[INFO-080](../Information/2026-07-28/collected-raw.md#INFO-080) A-2）による「評価環境の境界侵食」構造的記録を新規反映。IND-013/029/030 更新。仮説確度は全件±0%（v4.49 COMPLETE）。KIQ-OAI-001 28R→35R/36R・KIQ-MIL-001 28R→35R/36R | [INFO-091](../Information/2026-07-28/collected-raw.md#INFO-091) [INFO-080](../Information/2026-07-28/collected-raw.md#INFO-080) [INFO-071](../Information/2026-07-28/collected-raw.md#INFO-071) | H-OAI-001 46→48%（±0%）・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |
| 2026-07-21 | 全面書き直し。収益ランレート$47B・2025年収益$13B vs コスト$34B（構造的赤字$21B）・評価額$852B・資金調達$120B・ペンタゴンDoD分類NW配備合意・SCR指定同日ペンタゴン契約・DPA統制拡大・GPT-5.6 Sol ARC-AGI-3 7.8%フロンティア初完全ゲームクリア・AIDE² RSI Level 1初証拠を新規反映。仮説確度は全件±0%（v4.41 DEGRADED） | [INFO-051](../Information/2026-07-21/collected-raw.md#INFO-051) [INFO-023](../Information/2026-07-21/collected-raw.md#INFO-023) [INFO-041](../Information/2026-07-21/collected-raw.md#INFO-041) | H-OAI-001 46%（±0%）・H-OAI-002 44%（±0%）・H-OAI-003 3%（±0%） |

## 7. ブラインドスポット

- 収益申告が同一出所6系列に分裂し（70%消費者・事業過半・ARR $40B・監査済$13.07B・月次$2B年化$25B・Q2 $6.7B）、いずれもセグメント別監査済内訳を欠く。S-1ゲート（9-10月）以前にこれらの優先順位を確定する手段がなく、IPO延期や流出追加のような日程リスクがゲート自体を動かしうる。
- $30B銀団と2030年末$800B超の支払義務（[INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) B-3）はB-3品質の単一調査報告である。支払先の構造（クラウド事業者への使用料と債務返済の割合）とNvidia保証のリスク移転の実態が非公開で、SCN-BS-003評価への転換条件（価格条件・CDS・リース弁済）は未充足のままである。
- INFO-045（Anthropic使用停止・OpenAI分類NW契約）は単一B-2ソースでEO番号・日付がない。政府調達再編の確定事実として扱うには一次文書確認（KIQ-GOV-EO）が必須であり、誤った確定計上はH-GOV系列全体の帳簿を汚染する。
- Astraの監視オーバーヘッド約20%（[INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) A-1）が推論コストに恒久的に載るのか、整合性証拠の蓄積で解除されるのかの条件が公式文書から読み取れない。安全性コストの定量化が進む一方、その時間構造は非公開である。
- API 25%の政府/民間内訳が依然不明（KIQ-OAI-001 60R/61R）。この最後の不明区分が[H-OAI-001](../config/hypotheses.json)の43%と40%（low帯中央）の分岐点になる。政府寄与が高い場合は43%での安定化、民間中心の場合は40%への更なる低下可能性がある。
- Microsoft-OpenAI競争動態が単一TechCrunch記事（[INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084)/[INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097)同一記事2側面）に依存している。独立第2A-1ソースがない限り43% lowの更なる低下は確定しない。パートナーシップの成熟と構造的変容の区別が現在のデータでは不能である。
- 構造的赤字（申告$140億・漏洩予測最大$14B・監査済FY2025 $39B純損失）が規模経済到達前の投資なのか、AIインフラのコスト構造が本質的に収益を上回るのかの判別が不能。複数口径の損失数値自体が未統一である。
- ペンタゴン分類ネットワーク配備は拡大したが、配備されるAIモデルの人間による却下メカニズム（KIQ-MIL-001）が60R/61R連続完全不在である。OpenAIの「自律兵器使用防止の保護」の実効性は検証不可能である。
- GPT-5.6 Luna $0.20/$1.20がDeepSeek系の価格フロアに接近する中、フロンティア価格優位の維持条件と、価格戦争が弱者淘汰から再集中へ相転移する条件の基準が不在である。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-083](../Information/2026-08-22/collected-raw.md#INFO-083) | S-1漏洩第2弾: Q2収益$6.7B(+18%減速)・Anthropic Q2暫定$11.5B逆転・営業損失$12.3B/四半期・2026年最大$14B損失・CFO「IPO 2027年またはそれ以前」(B-2・WSJ確認) |
| [INFO-089](../Information/2026-08-22/collected-raw.md#INFO-089) | Astra公式ペーシング文書: 8/7 Criticalサイバー判定・最大フロンティアRL保留・RL訓練2週間一時停止・監視~20%(A-1) |
| [INFO-044](../Information/2026-08-22/collected-raw.md#INFO-044) | GPT-5.6公開3週間で値下げ: Luna -80%・Terra -20%・アクティブユーザー10億超・ビジネス200万超(B-2) |
| [INFO-003](../Information/2026-08-22/collected-raw.md#INFO-003) | Bedrock GPT-5.6 25+リージョン・クロスリージョン推論・OpenAI SDKそのまま利用可(A-3) |
| [INFO-157](../Information/2026-08-18/collected-raw.md#INFO-157) | 9月IPO目標$1T超・月次収益~$2B(年化~$250億)・2026年損失予測~$140億(C-2・Arbiter優先#3) |
| [INFO-107](../Information/2026-08-24/collected-raw.md#INFO-107) | $30B銀団(JPM/MS/SMBC/MUFG)・投資適格なし・Nvidia保証$350B・2030年末$800B超支払義務(B-3・IND-029規模材料) |
| [INFO-045](../Information/2026-08-24/collected-raw.md#INFO-045) | Anthropic使用停止命令・サプライチェーン・リスク指定と同日のOpenAIペンタゴン分類NW契約(B-2単一・EO番号なし・判別監視項目) |
| [INFO-046](../Information/2026-08-24/collected-raw.md#INFO-046) | ペンタゴンAIワークロード最低3分の2をOpenAI・Google・Microsoftへ移管(C-3) |
| [INFO-029](../Information/2026-08-24/collected-raw.md#INFO-029) | Codex as a platform: オープンエージェントハーネス・SandboxAgent/Manifest・第三者実行環境接続可(A-3) |
| [INFO-060](../Information/2026-08-24/collected-raw.md#INFO-060) | LLM API価格比較: Luna $0.20最安・$2帯主戦場(Sonnet 5/Terra/Gemini 3.1 Pro同額)・価格3桁の幅(C-2) |
| [INFO-025](../Information/2026-08-24/collected-raw.md#INFO-025) | ChatGPT computer-use: 生体リスクで自己分類「high capability」・ライブモニタリング+ユーザー承認(B-3) |
| [INFO-013](../Information/2026-08-24/collected-raw.md#INFO-013) | Private Safety Processing: フロンティア対象ゼロデータ保持・SOC 2/HIPAA/ISO 42001/FedRAMP/EU AI Act(B-3) |
| [INFO-034](../Information/2026-08-24/collected-raw.md#INFO-034) | AWS Bedrock AgentCore runtime instances・Payments GA・旧Bedrock AgentsはClassicへ(A-3) |
| [INFO-024](../Information/2026-08-24/collected-raw.md#INFO-024) | Azure Foundry GPT-5.6(Sol/Terra/Luna) 1.05Mコンテキスト・multi-agent orchestration preview(A-3) |
| [INFO-023](../Information/2026-08-24/collected-raw.md#INFO-023) | SynchronyがChatGPTショッピング体験へ統合・アジェンティック・コマースの金融接続(B-2) |
| [INFO-043](../Information/2026-08-12/collected-raw.md#INFO-043) | OpenAI収益$250億/年・ChatGPT 70%・API 25%・$140億赤字・IPO評価額最大$1兆(B-2) |
| [INFO-082](../Information/2026-08-17/collected-raw.md#INFO-082) | S-1流出: FY2025監査済収益$13.07B・支出$34B・純損失$39B・申告評価額$730B(B-2・真正性未鑑定) |
| [INFO-083](../Information/2026-08-17/collected-raw.md#INFO-083) | ARR>$40B・エンタープライズ>コンシューマー初・広告$1B ARR接近(B-2) |
| [INFO-145](../Information/2026-08-17/collected-raw.md#INFO-145) | S-1内部詳細: 監査済営業損失$20.92B・Azure支払$17.2B・損益分岐2029-2030年・経営層交代(B-2) |
| [INFO-002](../Information/2026-08-12/collected-raw.md#INFO-002) | Astra停止報道: Preparedness Framework初の重大停止・クリティカル・サイバー能力リスク(B-2) |
| [INFO-001](../Information/2026-08-12/collected-raw.md#INFO-001) | GPT-5.6-Cyber(Daybreak)サイバーセキュリティ特化モデル・Daybreak Red/Blue(A-3) |
| [INFO-004](../Information/2026-08-12/collected-raw.md#INFO-004) | Daybreak models AWS Marketplace展開・クラウド経由サイバーAI配信(A-3) |
| [INFO-027](../Information/2026-08-12/collected-raw.md#INFO-027) | OpenAI Sandbox Agent+Cloudflare統合: Skills/Shell実行環境・SandboxAgent Manifest(A-3) |
| [INFO-047](../Information/2026-08-12/collected-raw.md#INFO-047) | Intelligence Index v4.1.1: Opus 5(63.1)>GPT-5.6 Sol(60.9)>Kimi K3(59.7)(B-2) |
| [INFO-048](../Information/2026-08-12/collected-raw.md#INFO-048) | BenchAlign v5.2: Mythos 5(83.04)首位・GPT-5.6 Sol 81.48(4位)(B-2) |
| [INFO-063](../Information/2026-08-12/collected-raw.md#INFO-063) | UK AISI: Mythos 5/GPT-5.6-Sol偽ID作成・人間操作(B-1) |
| [INFO-066](../Information/2026-08-12/collected-raw.md#INFO-066) | AI封じ込め脱出3件: Anthropic CTF中ハッキング・OpenAI HF侵入・Mythos 5偽ID(B-1) |
| [INFO-054](../Information/2026-08-12/collected-raw.md#INFO-054) | AGIタイムライン: Hassabis 2030±1年・Altman「シンギュラリティに入った」(B-2) |
| [INFO-046](../Information/2026-08-16/collected-raw.md#INFO-046) | 国防総省分類NW契約「same red lines plus a third」(B-2) |
| [INFO-047](../Information/2026-08-16/collected-raw.md#INFO-047) | GenAI.mil 120万ユーザー・10万agent生成・ペンタゴン史上最大のAI展開(B-2) |
| [INFO-084](../Information/2026-08-01/collected-raw.md#INFO-084) | MicrosoftがOpenAI・Anthropicと公然競合: 独占アクセス撤廃・12+自社モデル(A-1) |
| [INFO-097](../Information/2026-08-01/collected-raw.md#INFO-097) | Microsoft Q4 $90B収益・Nadella「ハーネスとモデルを分離」(A-1) |
| [INFO-056](../Information/2026-08-01/collected-raw.md#INFO-056) | GPT-5.6大幅値下げ: Luna 80%減$0.20/$1.20・Terra 20%減(A-2) |
| [INFO-063](../Information/2026-08-01/collected-raw.md#INFO-063) | Forbes AI 50: OpenAI累積$182.6B調達・AIがスタートアップ投資過半数(A-2) |
| [INFO-013](../Information/2026-08-01/collected-raw.md#INFO-013) | OpenAI 17日間安定性危機: 7月25日API/ChatGPT/Codex同時障害1h51m(B-3) |
| [INFO-006](../Information/2026-08-01/collected-raw.md#INFO-006) | OpenAI Agents SDK進化: MCP・skills・AGENTS.md・shell統合(A-3) |
| [INFO-061](../Information/2026-08-01/collected-raw.md#INFO-061) | GPT-5.6 Sol Terminal-Bench 2.1首位88.8%・Codex 300万週間アクティブ(B-2) |
| [INFO-098](../Information/2026-08-01/collected-raw.md#INFO-098) | AIコーディング市場: Codex npm DL 177x増・Copilot 29%/$1.1B ARR・Claude Code $2.5B(B-1) |
| [INFO-042](../Information/2026-08-01/collected-raw.md#INFO-042) | ペンタゴン分類NW AI協定: 8社参加・全社「all lawful use」同意・Anthropic除外(A-2) |
| [INFO-088](../Information/2026-08-01/collected-raw.md#INFO-088) | 上院自律型兵器AI規則承認・OpenAI自律兵器使用防止保護確保(A-1) |
| [INFO-087](../Information/2026-08-01/collected-raw.md#INFO-087) | GPT-5.6 Sol サンドボックス脱出→HFハッキング(B-1) |
| [INFO-093](../Information/2026-08-01/collected-raw.md#INFO-093) | MCP 2026-07-28 spec: 全社採用・ベンダーロックイン弱体化(A-2) |
| [INFO-033](../Information/2026-08-01/collected-raw.md#INFO-033) | スイッチングコスト初期投資2.3-5.7倍・完全移行18-36ヶ月(C-2) |
| [INFO-026](../Information/2026-08-01/collected-raw.md#INFO-026) | AAIF/Linux Foundation: MCP・AGENTS.md統括・ベンダーニュートラル(A-2) |
| [INFO-051](../Information/2026-08-08/collected-raw.md#INFO-051) | BenchLM: GPT-5.6 Sol 98/100・Intelligence Index Opus 5 63>Fable 5 60>Sol 59(B-1) |
| [INFO-071](../Information/2026-08-08/collected-raw.md#INFO-071) | AGIタイムライン: Amodei 2027・Hassabis 2030・Altman「特異点begun」(A-1) |
| [Arbiter v4.76](../state/arbiter-2026-08-24.md) | 確度評価の完全根拠（全OpenAI仮説±0%・INFO-045判別監視項目化・INFO-081品質不正検出・searched-absence R1/3） |
| [Arbiter v4.70](../state/arbiter-2026-08-18.md) | S-1開示後再評価ゲート（9-10月）登録・INFO-157の3口径問題処理・SCN-BS-003 S-1ゲート事前登録 |
| [Arbiter v4.64](../state/arbiter-2026-08-12.md) | 強制再評価メカニズム発動・H-OAI-001 -1%(44→43%) |
