# 3冊統合Doctrine知識ベース：ビジネス意思決定向けInformation→Intelligence精査プロセス

## 1. 本知識ベースの位置づけ

本知識ベースは、FM 2-0、ATP 2-22.9、ATP 2-33.4の全文読込結果を、軍事用途としてではなく、**企業・市場・競合・技術動向に関する正しい意思決定を支える情報精査プロセス**として再解釈したものである。重要なのは、用語の直訳ではなく、教範が持つ「問いに基づく収集」「情報品質の分離評価」「反証を含む分析」「判断の確信度付与」「意思決定者への適時な配布」「フィードバックによる再収集」というプロセス原理を、GitHub ActionsとOpenCodeのAgentハーネスに移植することである。

> **設計原則:** Informationは観測・報告・記事・投稿・数値・一次資料の断片であり、Intelligenceは意思決定者の問いに答えるために、関連性・信頼性・正確性・反証可能性・不確実性・行動含意を明示して統合された判断である。

| 教範 | ビジネス向けに抽出する中核 | GitHub Actions / OpenCodeへの示唆 |
|---|---|---|
| FM 2-0 | Intelligence warfighting function、指揮官のPIR、収集管理、IPB、継続的なRunning Estimate | 意思決定者のKey Intelligence Questionsを起点に、収集・分析・統合・配布・更新を一つの継続ループとして管理する。 |
| ATP 2-22.9 | OSINTの計画、収集、処理、評価、報告、法務・監督・記録管理 | Web情報をそのまま要約せず、ソース評価、検索計画、取得ログ、情報品質、引用証跡を残して扱う。 |
| ATP 2-33.4 | Screen, Analyze, Integrate, Produce、構造化分析技法、分析基準、確信度、反証・代替仮説 | Agentを機能別に分け、Screening、Quality Check、Hypothesis、Red/Devil、Fusion、Production、Reviewを品質ゲート化する。 |

## 2. 軍事用語をビジネス情報精査に置き換える対応表

軍事教範の語彙をそのままビジネスに持ち込むと、成果物が不自然になり、目的もずれる。したがって、プロセス原理だけを保持し、対象をビジネス意思決定に置き換える。

| Doctrine用語 | ビジネスアナロジー | 実装上の表現 |
|---|---|---|
| Commander | 意思決定者、経営・事業責任者、投資判断者 | human_reviewer、decision_owner、PIR owner |
| PIR / IR / EEI / SIR | 重要意思決定質問、補助質問、観測すべき具体的項目、収集タスク | `config/pirs.json`、`collection_tasks.json`、`coverage_matrix.json` |
| Threat / Enemy | 競合、代替技術、市場構造、規制、顧客行動、プラットフォームリスク | `entities.json`、`market_forces.json`、`risk_vectors.json` |
| IPB | 市場・競争環境準備、Business Environment Preparation | `environment_baseline.md`、`market_model.json`、`scenario_model.json` |
| COA | 競合・市場・顧客の取り得る行動シナリオ | `hypotheses.json`、`scenarios.json` |
| NAI / TAI | 監視すべき市場領域・企業行動・イベント領域 | `indicators.json`、`watch_areas.json` |
| HVT / HPT | 高価値な意思決定対象、高インパクト施策・監視テーマ | `priority_decisions.json`、`high_payoff_topics.json` |
| D3A | Decide / Detect / Deliver / Assessの施策選定・検知・実行・効果測定 | `decision_cycle.json`、`post_decision_assessment.md` |
| BDA | 施策・判断後の効果測定、予測精度レビュー | `assessment_after_action.md`、`forecast_scorecard.json` |
| INTSUM / INTREP | 日次サマリー、イベント速報、定期レビュー、補足分析 | `reports/daily.md`、`reports/flash.md`、`reports/periodic.md` |
| Running Estimate | 継続更新される市場・企業・仮説の現在判断 | `static_intelligence/*.md`、`config/hypotheses.json` |

## 3. 統合プロセスモデル

3冊を統合すると、ビジネス向けのInformation→Intelligence変換は、単純な「収集→要約→レポート」ではなく、以下の10段階の状態遷移として実装すべきである。

| 段階 | Doctrine由来の意味 | ビジネス向け工程 | 主な状態ファイル | 品質ゲート |
|---:|---|---|---|---|
| 0 | 指揮官の要件理解 | 意思決定質問の定義と優先順位付け | `config/pirs.json`、`decision_context.md` | 問いが意思決定に接続しているか。 |
| 1 | Collection Planning | ソース別収集計画、検索式、頻度、最小ソース数の設計 | `config/collection_plan.json`、`collection_tasks.json` | PIR/KIQごとのカバレッジ、一次情報優先度、収集ギャップ。 |
| 2 | OSINT Collection | 公式発表、IR、採用、規制、GitHub、SNS、ニュース等の取得 | `Information/raw/*.jsonl`、`collection_log.json` | 取得日時、URL、ソース種別、重複、アクセス可否。 |
| 3 | Processing / Normalization | テキスト抽出、重複排除、メタデータ付与、証拠ID化 | `Information/processed/*.jsonl`、`evidence_index.json` | Evidence ID、引用可能性、原文保存、改変防止。 |
| 4 | Screen | PIR/KIQへの関連性、信頼性、正確性の初期評価 | `screened_information.json`、`discarded_information.json` | 関連性、信頼性、正確性、鮮度、循環報告の疑い。 |
| 5 | Analyze | 構造化分析、仮説生成、指標更新、パターン抽出 | `analysis_workspace/*.json`、`hypotheses_draft.json` | 事実・仮定・判断の分離、根拠の診断性、分析技法の適合。 |
| 6 | Contrarian / Diagnostic | ACH、Key Assumption Check、Quality Check、Devil's Advocacy | `ach_matrix.json`、`assumptions.json`、`red_findings.md` | 支配的仮説への反証、情報品質、主要前提の脆弱性。 |
| 7 | Integrate / Arbiter | Blue/Red/Quality結果を統合し、既存判断を更新 | `arbiter_log.json`、`config/hypotheses.json`、`indicators.json` | 矛盾処理、確信度、変更理由、未解決ギャップ。 |
| 8 | Produce / Disseminate | 意思決定者向けレポート、Static Intelligence、速報生成 | `reports/*.md`、`static_intelligence/*.md` | 判断、根拠、不確実性、次の行動が明確か。 |
| 9 | Feedback / Retasking | 未回答KIQ、判断後評価、次回収集要求への反映 | `next_collection_requirements.json`、`forecast_scorecard.json` | 未回答理由、再収集条件、予測の検証可能性。 |

## 4. 収集計画に反映すべき原則

FM 2-0とATP 2-22.9から導かれる収集設計の中心は、**収集対象を多くすることではなく、意思決定質問に対して何が不足しているかを明示し、そのギャップを埋めるために収集すること**である。現在のパイプラインが単にRSSや検索結果を取り込むだけであれば、情報量は増えてもIntelligenceの品質は上がらない。

| 原則 | ビジネス実装での要件 | 不十分な状態の兆候 |
|---|---|---|
| 問い駆動 | すべての収集タスクがPIR/KIQに紐づく。 | 「話題だから収集」しているが、どの判断に効くか不明。 |
| ソース計画 | 公式、一次情報、専門媒体、SNS、求人、技術文書などの役割を分ける。 | ニュース記事だけに偏り、一次資料確認がない。 |
| Source / Information分離 | 情報源の信頼性と、記述内容の妥当性を別スコアにする。 | 有名媒体の記事だから内容も正しいと扱っている。 |
| Circular Reporting検知 | 同じ元ネタを複数媒体が引用していないかを識別する。 | 複数記事があるように見えて、実際は単一リーク。 |
| Timeliness | 古い情報が現在も有効かを明示する。 | 過去の前提を現在判断に無批判に持ち込む。 |
| Collection Gap | 不足情報を次回収集要求として出す。 | 確信度が低いのに追加収集計画がない。 |

## 5. 分析に反映すべき構造化技法

ATP 2-33.4が示す最重要点は、分析は「LLMに読ませて推論させる」だけでは足りず、**問題に応じた構造化分析技法を選択し、中間成果物を状態として残す**必要があるという点である。

| 技法 | 使う場面 | ビジネスでの例 | 状態ファイル |
|---|---|---|---|
| Sorting | 大量の断片をカテゴリ化する | 競合の発表を製品、価格、提携、採用、規制に分類 | `sorting_table.json` |
| Chronology | 因果と変化速度を見る | モデル発表、価格改定、提携、資金調達の時系列 | `timeline.json` |
| Matrix | 企業・仮説・証拠を比較する | 企業別AI戦略比較、収益化進度比較 | `comparison_matrix.json` |
| Weighted Ranking | 優先順位を透明に決める | 監視テーマや施策候補の優先度付け | `weighted_ranking.json` |
| Link Analysis | 関係性を可視化する | 投資、提携、人材移動、OSS依存関係 | `link_graph.json` |
| Key Assumptions Check | 判断の土台を検査する | 「大手はモデル性能で差別化できる」という前提の検証 | `assumptions.json` |
| Quality of Information Check | 情報品質を検査する | リーク、匿名情報、二次報道、公式発表の扱い分け | `quality_matrix.json` |
| Indicators / Signposts | 変化の兆候を監視する | API価格改定、採用増、規制対応、導入事例 | `indicators.json` |
| ACH | 競合仮説を反証で比較する | 「OpenAI優位継続」対「クラウド勢逆転」など | `ach_matrix.json` |
| Devil's Advocacy | 支配的結論を壊す | 最終判断に対する反証レビュー | `red_findings.md` |
| Team A / Team B | 大きな判断を複数視点で並列検討する | 強気/弱気、企業視点/顧客視点、技術視点/財務視点 | `team_a_b_results.json` |
| Outside-In Thinking | 見落とした外部要因を入れる | 規制、顧客予算、電力、半導体、流通、文化要因 | `outside_in_factors.json` |
| What If / High Impact Low Probability | 低確率高影響を検討する | 規制急変、価格崩壊、主要提携破談、重大障害 | `tail_risk_register.json` |

## 6. 品質ゲートの標準

3冊全体で一貫する品質基準は、Intelligenceにする前に、情報と推論を複数の観点で検査することである。ビジネス用途では、以下をGitHub Actions上の自動ゲートおよびOpenCodeのAgentレビューとして実装する。

| ゲート | 合格条件 | 失敗時の扱い |
|---|---|---|
| Relevance Gate | PIR/KIQに直接または間接に関係する。 | `discarded_information.json`へ理由付きで退避。 |
| Source Reliability Gate | 情報源の実績、専門性、一次性、利害関係が評価されている。 | 低信頼ソースとしてフラグ。重大判断には使わない。 |
| Information Accuracy Gate | 他ソース・一次資料・過去状態と照合されている。 | 未確認扱い。確信度を下げ、追加収集へ。 |
| Circular Reporting Gate | 複数記事が同じ一次情報に依存していないか確認済み。 | 独立裏付けとして数えない。 |
| Fact / Assumption / Judgment Gate | 事実、仮定、判断が分離されている。 | Intelligence出力不可。再整形へ戻す。 |
| Hypothesis Gate | 主要判断に少なくとも1つ以上の代替仮説がある。 | 仮説生成Agentへ差し戻し。 |
| Contradiction Gate | 反証・矛盾・弱い証拠が明示されている。 | Red/Devil Agentへ差し戻し。 |
| Confidence Gate | High/Moderate/Lowと根拠が対応している。 | Arbiterで保留またはHuman Review。 |
| Timeliness Gate | 意思決定に間に合う形式で出力される。 | 完璧な分析より速報版を出し、後追い更新。 |
| Auditability Gate | Evidence ID、引用、判断変更理由、ログが残る。 | コミット不可。監査ログ生成へ差し戻し。 |

## 7. 確信度の定義

確信度はLLMの自信ではなく、情報品質、独立裏付け、ギャップ、矛盾、欺瞞・誤情報可能性、推論の健全性から決める。ATP 2-33.4の基準をビジネス向けに置き換えると、次のようになる。

| 確信度 | ビジネス向け定義 | 必要条件 |
|---|---|---|
| High | 判断に重要な情報ギャップが少なく、独立した複数ソースが整合し、代替仮説を検討しても主判断が残る。 | 一次情報または高信頼ソース、独立裏付け、矛盾解消、ACHまたは同等の反証通過。 |
| Moderate | 判断に一部仮定や未確認点があるが、主要証拠は整合し、実務上の意思決定に使える。 | 主要証拠あり、ギャップ明示、代替仮説あり、矛盾は限定的。 |
| Low | 重要なギャップ、単一ソース依存、矛盾、鮮度不足、リーク依存などがある。 | 速報・監視対象としては使えるが、重大判断にはHuman Reviewまたは追加収集が必要。 |

## 8. Agentハーネスに必要な役割分担

現行のBlue/Red/Arbiter構成は良い骨格を持つが、3冊を踏まえると、Blue/RedだけではScreen、Quality、Collection Management、Structured Analysis、Production、Feedbackの責務が混ざりやすい。OpenCode前提では、各Agentを「人格」ではなく、**工程責務と状態更新権限**で分けるべきである。

| Agent | 主責務 | 入力 | 出力 | 更新権限 |
|---|---|---|---|---|
| Collection Planner | KIQごとの収集要件とソース計画を作る。 | `pirs.json`、前回ギャップ | `collection_tasks.json` | 収集計画のみ |
| Collector | 情報を取得しEvidence IDを付ける。 | `collection_tasks.json` | `Information/raw/*.jsonl` | raw情報のみ |
| Processor | 正規化、重複排除、引用抽出、メタデータ付与。 | raw情報 | processed情報、evidence index | processed/evidence |
| Screener | PIR関連性、ソース信頼性、情報正確性を初期判定。 | processed情報 | screened/discarded情報 | screening状態 |
| Quality Checker | SourceとInformationを分離評価し循環報告を検査。 | screened情報 | `quality_matrix.json` | 品質状態 |
| Structuring Agent | Sorting、Timeline、Matrix、Linkなどの中間分析を作る。 | screened情報 | `analysis_workspace/*.json` | 分析中間物 |
| Hypothesis Agent | 複数仮説と指標を生成・更新する。 | 中間分析、既存仮説 | `hypotheses_draft.json` | draftのみ |
| Blue Analyst | 最有力判断を構築する。 | 仮説・証拠 | `blue_assessment.md` | draftのみ |
| Red / Devil Agent | 反証、代替仮説、前提崩壊、バイアスを提示。 | Blue判断、証拠 | `red_findings.md` | reviewのみ |
| Arbiter / Fusion Agent | 事実・仮定・判断を分けて最終統合する。 | Blue/Red/Quality/既存状態 | `arbiter_log.json`、更新候補 | 判断状態の更新候補 |
| Production Agent | 読者別成果物へ変換する。 | Arbiter出力 | reports/static intelligence | 成果物のみ |
| Feedback Agent | 未回答KIQと次回収集要求を生成する。 | 最終判断、ギャップ | `next_collection_requirements.json` | 次回計画 |

## 9. Human-in-the-loopが必要な判断

自動化は、情報処理と構造化を高速化するが、教範が強調するように、重大判断・低確信度・法務/倫理/事業影響が大きい場合は人間の承認が必要である。ビジネス用途では以下を明示的な停止点にする。

| 停止点 | 理由 | 例 |
|---|---|---|
| KIQ/PIRの新設・廃止 | 何を意思決定課題とみなすかは事業判断である。 | 新規市場参入、競合監視対象の追加。 |
| High Impact / Low Confidence | 影響が大きいが根拠が弱い判断は危険である。 | 主要企業の撤退・提携破談・重大障害。 |
| Static Intelligenceの大幅更新 | 長期判断を変えるため監査と説明が必要。 | 競争構造の主判断を変更。 |
| 施策優先順位の変更 | 分析から実行へ移る判断は自動化しない。 | 注力企業、調査予算、営業戦略の変更。 |
| 矛盾未解決のまま配布 | 誤認による意思決定を防ぐ。 | 一次情報と複数報道が食い違う。 |
| 低信頼ソース依存 | 誤情報・リーク・循環報告の影響が大きい。 | 匿名X投稿や噂ベースの判断。 |

## 10. 現行システムに対する示唆

現行リポジトリには、PIR/KIQ、collection_plan、Blue/Red/Arbiter、Static Intelligence、hypotheses、indicators、scenarios、arbiter_logといった良い骨格が存在する。問題は、工程が「収集→Blue分析→Red反証→Arbiter→レポート」に圧縮され、**Screen、Processing、Source/Information Quality、Structured Analytic Techniques、Collection Gap Retasking、Confidence根拠の機械検証**が独立ゲートとして十分に表現されていない点にある。

| 現行の強み | 残すべき理由 | 強化すべき点 |
|---|---|---|
| PIR/KIQレジストリ | 問い駆動の骨格がある。 | KIQごとの収集カバレッジ、回答状態、未回答理由を機械可読化する。 |
| Blue/Red/Arbiter | 反証と統合判断の構造がある。 | Red以前にQuality/Screeningを置き、Redは「反論」ではなく診断技法担当にする。 |
| hypotheses.json | 継続判断状態がある。 | ACH matrix、assumptions、evidence diagnosticityと接続する。 |
| indicators.json | I&W的な変化監視がある。 | KIQ・仮説・シナリオと双方向リンクし、次回収集要求を自動生成する。 |
| static_intelligence | Running Estimate的な蓄積判断がある。 | 更新理由、差分、確信度変化、反証状態を明示する。 |
| arbiter_log | 監査証跡がある。 | すべての確信度・確率・主判断変更にEvidence IDと品質ゲート結果を必須化する。 |

## 11. 再設計で守るべき最終原則

本タスクで再設計するGitHub Actionsフローは、単にAgent数を増やすのではなく、InformationがIntelligenceに変換されるための**不可逆な品質ゲート**を明示する必要がある。つまり、未処理情報がいきなり分析Agentに流れたり、低品質情報が根拠として使われたり、反証を経ていない判断がStatic Intelligenceを更新したりしてはいけない。

> **最終設計原則:** 収集量ではなく、意思決定質問への回答品質を最大化する。各判断は、Evidence、Quality、Hypothesis、Contradiction、Confidence、Action Implication、Next Collection Requirementを必ず持つ。

この知識ベースをもとに、次工程ではGitHub Actionsのジョブ分割、OpenCode Agent定義、状態ファイル、品質ゲート、プロンプト構成、導入順序を具体化する。
