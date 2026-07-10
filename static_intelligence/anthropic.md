# Anthropic

> 最終判断更新: 2026-07-10
> 全体確信度: 中
> 情報非対称性: Claude Code固有DAU絶対値が16R連続不在（閾値8Rを8R超過）。収益内訳はAPI/Enterprise/Consumerセグメント非公開。H-GOV-001は53%から50%に-3%（「パラドックス」フレーム未修正・Huawei級供給チェーンリスク指定・C同一因果チェーン4R連続未解消）。H-CAR-002は71%から69%に-2%（段階的修正4R連続-1%・70%心理的節目アンカリング打破）。TrumpがAnthropicを連邦政府全体から禁止（INFO-046 A-2）。「Huawei級」供給チェーンリスク指定。DPA脅迫確認（INFO-045 B-2）。Claude Sonnet 5リリース（INFO-051 A-3）。Claude自身のコード80%記述（INFO-062 B-3）。エンタープライズ採用率41%首位（INFO-064 B-3）。KIQ-MIL-001人間却下比率18R連続完全不在。Arbiter v4.31 COMPLETE
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-GOV-001](../config/hypotheses.json) は53%から50%に-3%。TrumpがAnthropicを連邦政府全体から禁止し（[INFO-046](../Information/2026-07-10/collected-raw.md#INFO-046) A-2）、Hegseth国防長官が「Huaweiに以前予約されていた扱い」と同等の供給チェーンリスク指定を発令した。346頁の法廷文書で全容が公開済みである。原因はAnthropicが2つの狭い契約制限の削除を拒否したことにある。DPA（国防生産法）をAnthropicへの強制手段として使用する脅迫が確認された（[INFO-045](../Information/2026-07-10/collected-raw.md#INFO-045) B-2）。Arbiter v4.31は、これまでの政府-AI介入証拠が全て同一因果チェーン（Anthropic-Pentagon対立）に依存していること（4R連続未解消）と、Blue Agentが前回Arbiterで採用された「パラドックス」フレームを修正せず同一論理を再使用したことを-1%の根拠に記録した。50%はmedium帯の下限である。

[H-CAR-002](../config/hypotheses.json) は71%から69%に-2%。段階的修正プロセス（4R連続-1%）が同一根拠（操作化ギャップ：ステートメントは「価値変容」を測定対象とするが、証拠は「価値低下」のみを測定する）の継続にもかかわらず突然停止した。Arbiter v4.31は70%の心理的節目アンカリングを打破し、-1%を追加適用した。I証拠の質的強度（Klarnaブーメラン・Gartner 50%再採用予測・Forrester 55%後悔）の過小評価も指摘された。ステートメント修正の実行が次回ラウンドの絶対条件として位置づけられている。

[H-ANT-002](../config/hypotheses.json) は53% lowで±0%。Claude Code WAUが1月比2倍・$1B ARRに到達（前回確認）。Claude Sonnet 5がリリースされ（[INFO-051](../Information/2026-07-10/collected-raw.md#INFO-051) A-3）、AWS Bedrockで提供開始（[INFO-032](../Information/2026-07-10/collected-raw.md#INFO-032) A-2）。Claude Code v2.1.197でデフォルトモデルに設定された。Anthropicが米国企業AI有料サブスク採用率41%で首位（[INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) B-3）。OpenAIは39.5%で横ばい。ただしDAU絶対値の16R連続不在（閾値8Rを8R超過）が核心パラメータの構造的不在として確定している。availability≠adoptionの制約は不変である。

[H-ANT-001](../config/hypotheses.json) は37% lowで±0%。AI Safety Index首位（[INFO-088](../Information/2026-07-10/collected-raw.md#INFO-088) A-2）は安全性制度化の進行を示すが、Kano遷移中期の不確実性は不変。Claudeが自身のコードの80%を記述している事実（[INFO-062](../Information/2026-07-10/collected-raw.md#INFO-062) B-3）は再帰的自己改善の具体化を示す。[H-GOV-002](../config/hypotheses.json) は23% lowで±0%、絶対条件29R連続未達成。Anthropicの$47B+ ARRは決定的反証として機能継続。

## 1. コア判断

全体確信度は中。本ラウンドの最重要判断は2つある。第一に、政府-AI関係の介入がエスカレート相転移を迎えたこと。第二に、H-CAR-002の段階的修正が継続したこと。

### 連邦政府全体禁止とHuawei級供給チェーンリスク指定

TrumpがAnthropicを連邦政府全体から禁止した（[INFO-046](../Information/2026-07-10/collected-raw.md#INFO-046) A-2）。これは特定の契約停止ではなく、連邦政府の全事業領域からの排除である。Hegseth国防長官が供給チェーンリスク指定を発令し、「Huaweiに以前予約されていた扱い」と同等の措置を適用した。346頁の法廷文書でAI使用論争の全容が公開されている。Anthropicは2つの狭い契約制限条項（自律型致死兵器のhuman-in-the-loop不在・国内監視）の削除を拒否した結果、この措置を受けた。

DPAをAnthropicへの強制手段として使用する脅迫が確認された（[INFO-045](../Information/2026-07-10/collected-raw.md#INFO-045) B-2）。Anthropicが供給チェーンリスク指定を受けた際、DPAでコンプライアンスを強制しようとした。Marc AndreessenがPentagon国防革新委員会に加入した。AnthropicはTeresa Carlson（Microsoft/AWS出身）を公共部門責任者として採用し対応している。Fable 5の復帰は何らかの譲歩取引の結果と報じられている。

この事象は3つの分析的含意を持つ。第一に、介入の質が「契約停止」から「全政府排除」に跳ね上がった。第二に、供給チェーンリスク指定はHuawei級の措置であり、Anthropicを国家安保上の脅威と分類したことを意味する。第三に、DPAによる強制脅迫が確認されたことで、政府が経済的圧力の行使を本格化させている。

但し、この証拠を含めH-GOV-001の全証拠が同一因果チェーン（Anthropic-Pentagon対立）に依存している。この独立性問題が4R連続で未解消である。他のAI企業に対する同種の政府介入→安全フレームワーク起動パターンが観測されない限り、「先例」の一般化可能性は構造的に制約される。

### Claude Sonnet 5リリースとエンタープライズ首位

Claude Sonnet 5がリリースされた（[INFO-051](../Information/2026-07-10/collected-raw.md#INFO-051) A-3）。Sonnet 4.6（2月発表）から4ヶ月での新型リリース。コーディング、エージェント、プロフェッショナルワークでフロンティア性能を提供する。価格は$3 per million input tokens（Sonnet 4.6と同じ）。AWS Bedrockで利用可能（[INFO-032](../Information/2026-07-10/collected-raw.md#INFO-032) A-2）。Claude Code v2.1.197でデフォルトモデルとして設定された（[INFO-013](../Information/2026-07-10/collected-raw.md#INFO-013) A-3）。

Anthropicが米国企業AI有料サブスク採用率41%で首位に立った（[INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) B-3）。2024年12月の10.6%から急増している。OpenAIは39.5%で横ばい。企業がベンチマークより主権、マルチモデル柔軟性、ビジネス成果を重視し始めた。但し41%はAPI全体であり、Claude Code固有のDAU/WAUではない。16R連続不在の核心パラメータ問題は別次元である。

### H-CAR-002の段階的修正継続

H-CAR-002は71%から69%に-2%（2R連続-1%）。操作化検証で特定された概念不整合が未解消である。証拠は全て「従来スキルの価値低下軸」（代替率・求人減少率・コスト予測）を測定し、「新スキル価値上昇軸」（設計・評価・方向付け能力の市場価値上昇）を測定していない。Arbiter v4.31は、段階的修正プロセス（4R連続-1%）が突然停止したことを是正した。70%の心理的節目アンカリングを打破し、-1%を追加適用した。I証拠の質的強度の過小評価も指摘された。Klarnaが700人CS置換後に失望的結果となり（[INFO-049](../Information/2026-07-10/collected-raw.md#INFO-049) B-2）、GartnerはAI理由で雇用削減した企業の50%が2027年までに再採用すると予測する。Forresterは55%の企業が人材削減を後悔している。これらは「価値低下」の可逆性を示すが、「新スキル価値上昇」の定量証拠は不在である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Trump連邦政府全体禁止: 「Huawei級」供給チェーンリスク指定・346頁法廷文書 | [H-GOV-001](../config/hypotheses.json) 介入の質的飛躍。契約停止→全政府排除。供給チェーンリスク指定の新次元 | A-2 | [INFO-046](../Information/2026-07-10/collected-raw.md#INFO-046) |
| 高 | DPA脅迫確認: Anthropicへの強制手段として使用 | [IND-030](../config/indicators.json) critical妥当性強化。経済的強制力の行使確認 | B-2 | [INFO-045](../Information/2026-07-10/collected-raw.md#INFO-045) |
| 高 | Claude Sonnet 5リリース: コーディング・エージェント・プロフェッショナルワークでフロンティア | [IND-025](../config/indicators.json) 性能向上継続。Sonnet 4.6から4ヶ月。$3/M input。Claude Code v2.1.197デフォルト | A-3 | [INFO-051](../Information/2026-07-10/collected-raw.md#INFO-051) |
| 高 | Anthropic企業AI採用率41%首位（OpenAI 39.5%横ばい）。2024年12月10.6%から急増 | [H-ANT-002](../config/hypotheses.json) 強める方向（API全体）。但しClaude Code固有DAU 16R不在でavailability≠adoption制約不変 | B-3 | [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) |
| 高 | Claude自身のコード80%記述: 再帰的自己改善の具体化 | [IND-028](../config/indicators.json) RSI具体化。[H-ANT-001](../config/hypotheses.json) 技術リーダーシップの層の厚さ | B-3 | [INFO-062](../Information/2026-07-10/collected-raw.md#INFO-062) |
| 高 | AI Safety Index Summer 2026: Anthropic首位。Great American AI Act超党派草案 | [H-ANT-001](../config/hypotheses.json) 安全性制度化の進行。[IND-030](../config/indicators.json) 規制環境変化 | A-2 | [INFO-088](../Information/2026-07-10/collected-raw.md#INFO-088) |
| 高 | Klarna 700人CS置換→失望的結果。Gartner 50%再採用予測・Forrester 55%後悔 | [H-CAR-002](../config/hypotheses.json) 価値低下の可逆性を実証。操作化ギャップ継続の文脈強化 | B-2 | [INFO-049](../Information/2026-07-10/collected-raw.md#INFO-049) |
| 中 | Claude Scienceローンチ: 研究者向け統合ワークスペース（6/30） | [H-ANT-002](../config/hypotheses.json) 製品幅拡大（C方向）。研究加速プラットフォーム | B-3 | [INFO-068](../Information/2026-07-10/collected-raw.md#INFO-068) |
| 中 | Claude Code Enterprise Governance: 6制御レイヤー・HIPAA準拠Enterprise契約+ BAA | [H-ANT-002](../config/hypotheses.json) エンタープライズ統制の制度化。50席以上のEnterprise契約必要 | C-3 | [INFO-024](../Information/2026-07-10/collected-raw.md#INFO-024) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-GOV-001](../config/hypotheses.json) が45%を割る | 介入の実効性が棄却水準に接近。「先例確立」から「先例不成立」への質的転換 | 180日 | [H-GOV-001](../config/hypotheses.json) |
| 連邦政府全体禁止が解除され、Anthropicが政府契約に復帰する | 「Huawei級」指定の恒久性が否定され、H-GOV-001の制度基盤が弱体化する | 365日 | [IND-030](../config/indicators.json) |
| H-GOV-001の全証拠が同一因果チェーン依存（4R連続）から脱却する | 他のAI企業に対する同種の政府介入パターンが観測され、「先例」の一般化が可能になる | 180日 | [IND-030](../config/indicators.json) |
| Claude Code DAU/WAU絶対値が公表される | 16R連続不在が解消し、H-ANT-002 53% lowの上方・下方いずれかの確定判定が可能になる | 次回 | [H-ANT-002](../config/hypotheses.json) |
| H-CAR-002ステートメントが「価値変容」から「価値低下+新スキル需要創出の未確証」に修正される | 操作化ギャップが解消され、段階的修正プロセスの前提が変わる | 次回 | [H-CAR-002](../config/hypotheses.json) |
| 全主要AI企業の安全性研究予算が経時的定量データで確認される | [H-GOV-002](../config/hypotheses.json) 絶対条件（29R連続未達成）の充足または棄却。萎縮効果の有無が確定する | 180日 | [H-GOV-002](../config/hypotheses.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性の制度化は差別化の消失ではなく次元の変化を意味し、規制捕獲戦略の側面も評価が必要 | 37% low | ±0%。AI Safety Index首位（INFO-088 A-2）で安全性研究リード。企業LLM支出シェア40%+は企業市場地位を示すが安全性選択理由かの判別不能。Claude自コード80%（INFO-062）で技術リーダーシップ。CVE-8.7継続的矛盾 | [INFO-088](../Information/2026-07-10/collected-raw.md#INFO-088) [INFO-062](../Information/2026-07-10/collected-raw.md#INFO-062) | (判別不能) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 53% low | ±0%。DAU 16R連続不在（閾値8Rを8R超過）。Claude Sonnet 5リリース（INFO-051 A-3）・企業AI採用率41%首位（INFO-064 B-3）・Claude Code v2.1.197デフォルトはC方向。availability≠adoption制約不変。API全体採用率≠Claude Code固有DAU | [INFO-051](../Information/2026-07-10/collected-raw.md#INFO-051) [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) | DAU 16R不在 |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% low | ±0%。棄却候補継続。Google $40B投資でインフラ二重集中加速。Sonnet 5のAWS Bedrock展開（INFO-032）で依存深化 | (該当なし) | [INFO-032](../Information/2026-07-10/collected-raw.md#INFO-032) |
| [H-GOV-001](../config/hypotheses.json) | 政府が経済的手段でAnthropicの安全性姿勢に圧力をかける先例が確立された。(a)命題に特化。(b)はH-GOV-002として分離 | 50% medium | -3%（53→50%、v4.28/v4.29/v4.31で3R連続-1%）。連邦政府全体禁止・Huawei級供給チェーンリスク指定（INFO-046 A-2）は介入の質的飛躍。DPA脅迫確認（INFO-045 B-2）。但し全証拠が同一因果チェーン依存（4R連続未解消）。「パラドックス」フレーム未修正。50%はmedium帯下限。段階的修正プロセスの継続 | [INFO-046](../Information/2026-07-10/collected-raw.md#INFO-046) [INFO-045](../Information/2026-07-10/collected-raw.md#INFO-045) | (同一因果チェーン依存4R) |
| [H-GOV-002](../config/hypotheses.json) | 政府のAnthropic圧力先例がAI業界全体に波及し、順応報酬構造を通じて安全性研究の戦略的価値が構造的に低下する | 23% low | ±0%。絶対条件29R連続未達成。$47B+ ARRは安全性維持企業の圧倒的成功を示す決定的反証。連邦政府全体禁止は順応報酬構造の完全観察を可能にする（Anthropic排除→OpenAI後継）が、業界全体への波及は観測されず | [INFO-046](../Information/2026-07-10/collected-raw.md#INFO-046) | $47B+ ARR反証 |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 36% low | ±0%。「79%導入」≠「30%自動化達成」の定義ギャップ未解決。AI関連雇用削減175,796件累積・2026年4月21,490件（INFO-048 B-2）で方向性支持蓄積。変換は未解決 | [INFO-048](../Information/2026-07-10/collected-raw.md#INFO-048) | (因果ギャップ未解決) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が変容し、設計・評価・方向付けへの移行でその能力の価値が上昇する | 69% medium | -2%（71→69%、2R連続-1%）。段階的修正4R連続後の突然停止を是正。70%心理的節目アンカリング打破。操作化概念不整合継続（「価値変容」ステートメント vs 「価値低下」のみの証拠）。Klarnaブーメラン・Gartner 50%再採用・Forrester 55%後悔（INFO-049 B-2）で可逆性実証だが「新スキル上昇軸」未測定。ステートメント修正次回絶対条件 | [INFO-049](../Information/2026-07-10/collected-raw.md#INFO-049) [INFO-074](../Information/2026-07-10/collected-raw.md#INFO-074) | (操作化ギャップ不変) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流と下流に集中する | 57% medium | ±0%。方向性支持・速度不確定。AaaSがSaaS置換の趨勢継続。Gartner $234B SaaS支出破壊予測（INFO-053 A-2）。広告市場+8.6%成長 vs ホールディング収益-1.2%で中間層侵食直接証拠（INFO-054 B-3） | [INFO-053](../Information/2026-07-10/collected-raw.md#INFO-053) [INFO-054](../Information/2026-07-10/collected-raw.md#INFO-054) | (新規弱める証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | 企業AI採用率41%首位（INFO-064 B-3）。Claude Code $1B ARR継続。Sonnet 5 AWS Bedrock展開（INFO-032 A-2）。high/rising | 2026-07-10 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | SkillCloak全静的スキャナ突破（INFO-022 B-2）・AI生成コード45% OWASP脆弱性（INFO-026 B-2）・AIエージェント本番DB削除（INFO-027 B-3）。攻撃面拡大継続。critical移行条件（実被害A-2報告）未到達。high/rising | 2026-07-10 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満で high | Claude Sonnet 4.6/5（INFO-001/051 A-3）・Fable 5 ECI 161（INFO-030 A-2）・Seedream 5.0 Pro（INFO-081 A-3）。量的向上継続。「真の理解」客観的検証未到達。elevated/stable | 2026-07-10 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | 88%パイロット停滞（INFO-039 B-2）・71%運用コスト>構築（INFO-039）・97%コミット/18%デプロイ（INFO-039）・リスク完全緩和7%（INFO-026 B-2）・AI DB削除（INFO-027 B-3）。期待-実態ギャップ更に強化（13+独立ソース）。high/rising | 2026-07-10 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用で high | MCP RC（INFO-021 A-3）・AAIF拡大（INFO-028 B-2）・Google Gemini Enterprise Agent Platform（INFO-036 A-3）・MS Foundry→M365（INFO-037 A-3）・OpenAI Agents SDK provider-agnostic（INFO-015 A-3）・NVIDIA OpenShell（INFO-034 A-3）。制度化フェーズ継続。high/rising | 2026-07-10 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大で high | GPT-5.6 Sol ARC-AGI-3 7.8%（INFO-061 A-2）・Claude自コード80%（INFO-062 B-3）・G7 Altman/Hassabis/Amodei AGI討議（INFO-075 B-2）・UN科学パネル発足（INFO-090 B-3）。RSI具体化と客観ベンチマーク限界の同時進行。high/rising | 2026-07-10 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限り high | DC $850Bリース+204% YoY（INFO-059 A-2）・ビッグテック$650B/$2B/day（INFO-063 B-3）・H1 $252B投資（INFO-080 B-2）。資本流入加速・物理的制約ギャップ確定的。high/rising | 2026-07-10 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。連邦政府全体禁止・Huawei級指定（INFO-046 A-2）・DPA脅迫確認（INFO-045 B-2）・国連事務総長「道義的に忌まわしい」（INFO-047 A-2）・Warren開示要求（INFO-044 A-2）・human-in-loop法案（INFO-012 B-3）・June 2026 EO（INFO-050 A-2）。KIQ-MIL-001 18R連続不在（17R→18R）。IND-030-SCN-BS-001連動関係形式的定義実行（6R先送り停止）：criticalはBS-001確率自動上昇をトリガーしないが期待損失は上昇。条件2充実継続 | 2026-07-10 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-10 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 53→50%（連邦政府全体禁止・Huawei級供給チェーンリスク指定・DPA脅迫確認・同一因果チェーン4R連続・「パラドックス」フレーム未修正）。[H-CAR-002](../config/hypotheses.json) 71→69%（段階的修正4R後突然停止是正・70%心理的節目打破）。Claude Sonnet 5リリース・企業AI採用率41%首位・Claude自コード80%・AI Safety Index首位。KIQ-MIL-001 18R。IND-030-SCN-BS-001連動関係形式的定義実行。Arbiter v4.31 COMPLETE | [INFO-046](../Information/2026-07-10/collected-raw.md#INFO-046) [INFO-051](../Information/2026-07-10/collected-raw.md#INFO-051) [INFO-062](../Information/2026-07-10/collected-raw.md#INFO-062) [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) [INFO-088](../Information/2026-07-10/collected-raw.md#INFO-088) | H-GOV-001 53→50%・H-CAR-002 71→69% |
| 2026-07-03 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 54→53%・[H-CAR-002](../config/hypotheses.json) 72→71%。Fable 5再デプロイ/Glasswing。KIQ-MIL-001 14R | [INFO-001](../Information/2026-07-03/collected-raw.md#INFO-001) [INFO-030](../Information/2026-07-03/collected-raw.md#INFO-030) | H-GOV-001 54→53%・H-CAR-002 72→71% |
| 2026-07-02 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 55→54%・[H-ANT-002](../config/hypotheses.json) 54→53% medium→low・[H-GOV-002](../config/hypotheses.json) 24→23%・[H-CAR-002](../config/hypotheses.json) 73→72% | [INFO-039](../Information/2026-07-02/collected-raw.md#INFO-039) | H-GOV-001 55→54%・H-ANT-002 54%medium→53%low・H-GOV-002 24→23%・H-CAR-002 73→72% |
| 2026-06-29 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 55% ±0%凍結。[H-GOV-002](../config/hypotheses.json) 22→23%。[H-ANT-002](../config/hypotheses.json) 57→56%。[H-CAR-002](../config/hypotheses.json) 71→72% | [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) | H-GOV-001 55%凍結・H-GOV-002 22→23%・H-ANT-002 57→56%・H-CAR-002 71→72% |
| 2026-06-27 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 54% ±0%。[H-ANT-002](../config/hypotheses.json) 62→58% | [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) | H-GOV-001 54%・H-ANT-002 62→58% |

## 7. ブラインドスポット

- [H-GOV-001](../config/hypotheses.json) 50%は3R連続-1%の段階的修正の結果。medium帯下限に到達した。50%を割るとmedium→low移行が Trigger される。連邦政府全体禁止（INFO-046）は介入の質的強化の決定的証拠だが、同一因果チェーン依存問題（4R連続）が解消しない限り、50%以下への自然的ドリフト圧力と介入強化の方向性が対立する。
- 連邦政府全体禁止とHuawei級供給チェーンリスク指定が、Anthropicの商業的軌道（$47B+ ARR・$965B評価額）に与える影響がまだ観測されていない。346頁の法廷文書が公開済みだが、市場反応・顧客離れ・評価額変動の定量データが不在。
- 全証拠が同一因果チェーン（Anthropic-Pentagon対立）に依存している構造的問題が4R連続で未解消。この問題自体がH-GOV-001確度の上限を制約している。他社への同種介入が観測されない限り、この制約は構造的に持続する。
- [H-ANT-002](../config/hypotheses.json) 53% low移行後、DAU不在が17R、18Rと延びてもlow帯内での更なる引き下げしか起きない。企業AI採用率41%首位（API全体）とClaude Code固有DAU不在の二面性が、単一確度で表現できない構造的制約として持続する。
- [H-CAR-002](../config/hypotheses.json) 69%のステートメント修正が5R以上先送りされている。hypotheses.jsonのステートメントが未更新の場合、静的インテリジェンスの§4とconfigの間に不整合が生じる。Arbiter v4.31が次回修正を絶対条件化したが、実行タイミングと手法が未定義。
- KIQ-MIL-001（人間却下比率）が18R連続完全不在。Arbiter v4.31が「軍事文脈でのデータ不在=構造的に非対称」の評価基準を策定した。18R不在が構造的（軍事機密で非公開）か偶発的（報道されていないだけ）かの判別は依然不能だが、不在を中立と評価しない原則が制度化された。
- IND-030-SCN-BS-001連動関係の形式的定義が実行された。IND-030 criticalがBS-001確率の自動上昇をトリガーしないことが確定した。期待損失（確率×重症度）は上昇している。この定義が今後のラウンドでどう適用されるかが次の検証課題。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-07-10/collected-raw.md#INFO-001) | Claude Sonnet 4.6リリース: コーディング・エージェント・研究でフロンティア(A-3) |
| [INFO-013](../Information/2026-07-10/collected-raw.md#INFO-013) | Claude Agent SDK TypeScript v2.1.204: Claude Code parity・Claude Code v2.1.197でSonnet 5デフォルト(A-3) |
| [INFO-024](../Information/2026-07-10/collected-raw.md#INFO-024) | Claude Code Enterprise Governance: 6制御レイヤー・HIPAA・Claude Coworkリモート実行(C-3) |
| [INFO-030](../Information/2026-07-10/collected-raw.md#INFO-030) | Epoch AI Benchmarks: Claude Fable 5 ECI 161新記録・GPT-5.5 Proを1点上回る(A-2) |
| [INFO-032](../Information/2026-07-10/collected-raw.md#INFO-032) | Claude Sonnet 5 AWS Bedrock提供開始・Amazon WorkSpaces for AI agents(A-2) |
| [INFO-044](../Information/2026-07-10/collected-raw.md#INFO-044) | Warren開示要求: Pentagon+7社（SpaceX/OpenAI/Google/NVIDIA/MS/AWS/Oracle）AI契約条件(A-2) |
| [INFO-045](../Information/2026-07-10/collected-raw.md#INFO-045) | DPA脅迫確認: Anthropicへの強制手段・Marc Andreessen Pentagon国防革新委員会加入(B-2) |
| [INFO-046](../Information/2026-07-10/collected-raw.md#INFO-046) | Trump連邦政府全体禁止・Huawei級供給チェーンリスク指定・346頁法廷文書・Teresa Carlson採用(A-2) |
| [INFO-047](../Information/2026-07-10/collected-raw.md#INFO-047) | 国連事務総長: 自律型致死兵器は「道義的に忌まわしい」・国際法禁止要求(A-2) |
| [INFO-049](../Information/2026-07-10/collected-raw.md#INFO-049) | Klarna 700人CS置換→失望的結果。Gartner 50%再採用予測・Forrester 55%後悔・Duolingo置換停止(B-2) |
| [INFO-050](../Information/2026-07-10/collected-raw.md#INFO-050) | June 2026 AI Executive Order: ウォーターマーク指針・データガバナンス・リリース前テスト(A-2) |
| [INFO-051](../Information/2026-07-10/collected-raw.md#INFO-051) | Claude Sonnet 5公式発表: フロンティア性能・$3/M input・Claude Code v2.1.197デフォルト(A-3) |
| [INFO-062](../Information/2026-07-10/collected-raw.md#INFO-062) | Claude自身のコード80%記述: 再帰的自己改善の具体化・グローバルAI一時停止議論(B-3) |
| [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) | Anthropic企業AI採用率41%首位（OpenAI 39.5%横ばい）。2024年12月10.6%から急増(B-3) |
| [INFO-068](../Information/2026-07-10/collected-raw.md#INFO-068) | Claude Scienceローンチ: 研究者向け統合ワークスペース・6/30(B-3) |
| [INFO-075](../Information/2026-07-10/collected-raw.md#INFO-075) | G7: Altman/Hassabis/Amodei AGI討議・米国主導国際AI連合提案・強いAGI 2031-2035(B-2) |
| [INFO-088](../Information/2026-07-10/collected-raw.md#INFO-088) | AI Safety Index Summer 2026: Anthropic首位。Great American AI Act超党派草案・CAISI設立(A-2) |
| [Arbiter v4.31](../state/arbiter-2026-07-10.md) | 確度評価の完全根拠 |
