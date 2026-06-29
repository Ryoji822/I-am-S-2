# Anthropic

> 最終判断更新: 2026-06-29
> 全体確信度: 中
> 情報非対称性: Claude Code DAU/日常利用者データが10R連続不在（v4.20閾値8Rを2R超過・medium→low移行条件倍加・DEGRADED制約でラベル変更保留）。収益内訳はQ2営業利益$559M/ARR $47Bで部分的解明だが、API/Enterprise/Consumerセグメント内訳は非公開。安全性が選択理由上位3要因以内かはA-2品質で未確認（Kano再定式化実行済み）。CVE-8.7が安全性差別化仮説に継続的矛盾。H-GOV-001は55% mediumでArbiter v4.22凍結条件活性化（4R連続Red不在）により確度変更凍結。INFO-067選択的執行（B-2）は極めて高い診断的価値を持つが、累積ドリフト(52→56%提案=+4%)の系統的リスクがsafeguard優先。証拠は否定されず次回COMPLETE交差検証のために保全。Anthropic $30B調達・評価額$900B(INFO-043/009 A-2/B-2)でOpenAI($852B)を超越。Pentagon Anthropic置換テスト(INFO-064 B-3)は順応報酬構造の初の具体的直接証拠。Fable 5/Mythos 5アクセス停止継続（17日目・6月12日から）。企業LLM支出シェア40%（Menlo）。Claude API月間ほぼ毎日障害(INFO-013 C-3)。Arbiter v4.23 DEGRADED状態（4R連続・Red Agent失敗）
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-GOV-001](../config/hypotheses.json) は55%（medium）で凍結された。Arbiter v4.22が設定した「4R連続Red不在で確度変更凍結推奨」条件が、v4.20からv4.23で丁度4R連続到達し活性化した。Blue AgentはINFO-067選択的執行タイムライン（B-2）の診断的価値を認め+1%を提案したが、Arbiterは52→56%（提案）の+4%累積ドリフトが確証バイアスの典型的パターンと判断し、safeguard優先で凍結を決定した。証拠は否定されていない。次回COMPLETE（Red完了）での交差検証のために保全される。

選択的執行の構造化は本ラウンドの質的新次元である。[INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067)（B-2）が明らかにした「GPT-5.5とFable 5/Mythos 5に同じ脆弱性が存在するにもかかわらずOpenAIには無措置」という事実は、政府介入が「普遍的安全性懸念」ではなく「選択的コンプライアンス強制メカニズム」として機能していることを示唆する。PentagonがAnthropic Claudeの置換を目的にOpenAI・Googleのテストを開始した [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064)（B-3）は、順応企業が契約を獲得する構造を実体化する。[H-GOV-002](../config/hypotheses.json) は21%から23%に2R連続+1%で上昇した。順応報酬構造の初の具体的直接証拠として+1%を認めた。絶対条件（他社安全性方針定量変化データ）は20R連続未達成でlow維持である。

[H-ANT-002](../config/hypotheses.json) は58%から56%に2R連続-1%。DAU/日常利用者データが10R連続不在となり、Arbiter v4.20が設定した8R閾値を2R超過した。Claude Code採用率24%（米国） [INFO-006](../Information/2026-06-29/collected-raw.md#INFO-006)（C-3）・企業LLM支出シェア40%はC方向だが、核心パラメータの構造的不在が累積コストとして反映されている。Anthropic $30B調達・$900B評価 [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043)（A-2）は商業的成功の極みであるが、Fable 5/Mythos 5アクセス停止が17日目に入り、技術リーダーシップの活用可能性が制限されたままである。Claude APIの月間ほぼ毎日の障害 [INFO-013](../Information/2026-06-29/collected-raw.md#INFO-013)（C-3）は信頼性の構造的弱さを示す。

## 1. コア判断

全体確信度は中。本ラウンドの最重要判断は [H-GOV-001](../config/hypotheses.json) の確度変更凍結である。

### H-GOV-001凍結の判断根拠

Arbiter v4.22で設定されたsafeguardが本ラウンドで活性化した。「4R連続Red不在の場合はH-GOV-001確度変更凍結推奨」という条件が、v4.20（2026-06-26）からv4.23（2026-06-29）で丁度4R連続到達した。この間、H-GOV-001は52→53→54→55%と毎ラウンド+1%で推移した。Blue Agentは本ラウンドも+1%（55→56%）を提案した。

INFO-067選択的執行タイムライン（[INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) B-2）の診断的価値はArbiterも認めている。2025年7月の$200M DoD契約から2026年6月12日の90分輸出管理指令に至るタイムラインの詳細、およびGPT-5.5に同じ脆弱性がありながらOpenAIには何の措置も取られていない事実は、介入の選択性を構造化されたパターンとして初めて文書化した。だがArbiterは、52→56%（提案）の+4%累積ドリフトが確証バイアスの典型的累積パターンと判断した。各ラウンドの+1%は個別にはA-2品質新規証拠で妥当だが、4R連続で独立検証不在の下での方向的一貫性は系統的バイアスの赤信号である。

凍結は証拠の否定ではない。次回COMPLETE（Red完了）での商業成功パラドックス代替解釈交差検証を絶対必須条件化した。Anthropic $30B調達・$900B評価（[INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) A-2）は、政府がSCR指定・連邦使用停止・輸出管理指令・DOJ提訴を行使してもAnthropicが評価額$900Bに成長した事実であり、「先例確立≠実効性確認」の不均衡をさらに拡大するI方向証拠である。

### 順応報酬構造の初の直接証拠

[H-GOV-002](../config/hypotheses.json) が21%から23%に2R連続+1%で上昇した。PentagonがAnthropic Claudeの置換を目的にOpenAI・GoogleのAIモデルの正式テストを開始した（[INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) B-3）。2025年7月のAnthropic $200M・2年DoD契約後のアクセス停止（90分以内）で生じた空白を、順応企業が埋める構造が実体化した。OpenAI/Google/xAI/Amazon/Microsoft/Nvidiaは5月までに全社軍事協定に署名し（[INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) B-2）、数百人のOpenAI/Google従業員がAnthropic支持の請願を行った。

ただしC=3件中2件（INFO-064/067）は同一因果チェーン（Anthropic-Pentagon対立）からの派生であり、確証バイアスリスクを明示する。絶対条件（全主要AI企業安全性研究予算経時的減少A-2確認）は20R連続未達成で、low維持である。

### H-ANT-002の低下トレンド

[H-ANT-002](../config/hypotheses.json) は58%から56%に2R連続-1%。DAU/日常利用者データが10R連続不在となり、Arbiter v4.20閾値（8R）を2R超過した。核心パラメータの構造的不在は、Claude Code $1B ARR・企業LLM支出シェア40%・採用率24%というC方向証拠を上回るI方向の重みとして蓄積している。Cursor $60B買収（SpaceX）は競合強化であり、Claude Code 18%=Cursor 18%同率だがGitHub Copilot 29%に劣位にある（[INFO-049](../Information/2026-06-29/collected-raw.md#INFO-049) B-3）。Claude API月間ほぼ毎日の障害（[INFO-013](../Information/2026-06-29/collected-raw.md#INFO-013) C-3）は、エンタープライズのfour-nines SLAと非互換という信頼性の構造的課題を示す。

Anthropicの商業的成功は疑いない。$30B調達・$900B評価・Q2営業利益$559M・ARR $47B・企業LLM支出シェア40%。だが56%はFable 5/Mythos 5アクセス停止（17日目）とOpus 4.8 SWE-bench #1の技術リーダーシップへの依存が深まっており、その技術リーダーシップの活用可能性が政府指令で制限されている矛盾が続く。

[H-ANT-001](../config/hypotheses.json) は37%で±0%維持。[H-CAR-002](../config/hypotheses.json) は70%から72%に2R連続+1%。Stanford HAI（A-2: 22-25歳SWE雇用約20%減少）・WEF（A-2: 86%組織変革）の労働市場直接定量データが極めて診断的である。[H-CAR-003](../config/hypotheses.json) は58%で±0%維持。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 選択的執行タイムライン: GPT-5.5とFable 5/Mythos 5に同じ脆弱性だがOpenAIには無措置 | [H-GOV-001](../config/hypotheses.json) C方向・質的新次元。選択性の構造化。Arbiter v4.22凍結条件で+1%凍結。証拠は保全 | B-2 | [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) |
| 高 | Pentagon Anthropic Claude置換テスト: OpenAI/Google AIモデルの正式テスト開始 | [H-GOV-002](../config/hypotheses.json) C方向。順応報酬構造の初の具体的直接証拠。+1%の主根拠 | B-3 | [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) |
| 高 | Anthropic $30B調達・評価額$900B（OpenAI $852Bを超越） | [H-GOV-001](../config/hypotheses.json) I方向（先例確立≠実効性確認）。[IND-029](../config/indicators.json) 資本流入加速 | A-2 | [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) [INFO-009](../Information/2026-06-29/collected-raw.md#INFO-009) |
| 高 | Claude Code DAU/日常利用者データ10R連続不在 | [H-ANT-002](../config/hypotheses.json) I方向。核心パラメータ構造的不在。medium→low移行条件倍加・DEGRADED制約で保留 | (内部) | [arbiter-2026-06-29](../state/arbiter-2026-06-29.md) |
| 高 | Claude Code採用率24%（米国）・Cursor 1M+ DAUとの対比 | [H-ANT-002](../config/hypotheses.json) C方向だがDAU不在のIが上回る。GitHub Copilot 29%に劣位 | C-3 | [INFO-006](../Information/2026-06-29/collected-raw.md#INFO-006) |
| 高 | Claude API月間ほぼ毎日elevated-error incidents・Notion 12時間障害 | [IND-013](../config/indicators.json) 信頼性問題。[H-ANT-002](../config/hypotheses.json) I方向。SLA提供なし | C-3 | [INFO-013](../Information/2026-06-29/collected-raw.md#INFO-013) |
| 高 | Fable 5/Mythos 5アクセス停止継続（17日目・6月12日から） | [H-ANT-002](../config/hypotheses.json) I方向。技術リーダーシップの活用可能性制限。56%の維持根拠が弱まる | A-3 | [INFO-017](../Information/2026-06-29/collected-raw.md#INFO-017) [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) |
| 高 | Anthropic Q2営業利益$559M・ARR $47B | [H-GOV-001](../config/hypotheses.json) I方向。[H-ANT-002](../config/hypotheses.json) C方向（商業的成功） | A-2 | [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) |
| 高 | Claude Corps $150M・1000人フェローシップ（AI政策枠組みと同時発表） | [H-CAR-002](../config/hypotheses.json) C方向。労働市場変化への責任投資。Anthropicの社会的 positioning | A-3 | [INFO-003](../Information/2026-06-29/collected-raw.md#INFO-003) |
| 高 | Stanford HAI: 22-25歳SWE雇用約20%減少 | [H-CAR-002](../config/hypotheses.json) C方向・A-2品質。+1%の主根拠。「価値変容」≠「価値低下」 | A-2 | [INFO-050](../Information/2026-06-29/collected-raw.md#INFO-050) |
| 高 | RSI by 2028（Anthropic共同創業者Jared Kaplan予測） | [IND-028](../config/indicators.json) RSI具体化。AnthropicのAGI到達戦略 | B-2 | [INFO-057](../Information/2026-06-29/collected-raw.md#INFO-057) |
| 中 | Trump EO 14409/14412（AI革新・暗号攻撃安全保障） | [H-GOV-001](../config/hypotheses.json) C方向。制度的枠組み強化。GPT-5.6リリースプロセスと連動 | A-2 | [INFO-031](../Information/2026-06-29/collected-raw.md#INFO-031) |
| 中 | Anthropic Security Controls Assurance Lead採用（FedRAMP/SOC 2/ISO） | [IND-013](../config/indicators.json) 防御側強化。コンプライアンス体制整備 | A-3 | [INFO-016](../Information/2026-06-29/collected-raw.md#INFO-016) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-GOV-001](../config/hypotheses.json) が60%を超える（次回COMPLETE後） | 凍結解除後の方向転換が構造的トレンドと確認される | 次回COMPLETE | [H-GOV-001](../config/hypotheses.json) |
| [H-GOV-001](../config/hypotheses.json) が45%を割る | 先例確立仮説が棄却水準に接近する | 180日 | [H-GOV-001](../config/hypotheses.json) |
| 次回COMPLETEで商業成功パラドックス代替解釈の交差検証が実施される | H-GOV-001凍結解除の絶対必須条件。Red完了後の質的再評価 | 次回COMPLETE | [arbiter-2026-06-29](../state/arbiter-2026-06-29.md) |
| 次回COMPLETEでH-ANT-002 medium→low移行が実施される | DAU 10R連続不在で移行条件倍加。ラベル変更確定の可能性高い | 次回COMPLETE | [H-ANT-002](../config/hypotheses.json) |
| Fable 5/Mythos 5のアクセス停止が60日以上継続する | [H-ANT-002](../config/hypotheses.json) 56%の技術リーダーシップ根拠が弱まる。現在17日目 | 43日 | [IND-027](../config/indicators.json) |
| Pentagon Anthropic置換テストでOpenAI/Googleが正式採用される | [H-GOV-002](../config/hypotheses.json) の順応報酬構造が確定する。 displacementの構造化完了 | 180日 | [IND-030](../config/indicators.json) |
| SCR指定後のAnthropic連邦調達収益の定量的推移データが入手できる | H-GOV-001介入効果の実効性評価の核心パラメータ。凍結解除判定に必須 | 180日 | [IND-030](../config/indicators.json) |
| 安全性がA-2品質でエンタープライズ選択理由第1位と確認される | [H-ANT-001](../config/hypotheses.json) 上限条件解除。37%下限宣言の無効化 | 180日 | [IND-008](../config/indicators.json) |
| CVE-8.7が深刻な実被害（エンタープライズ環境での悪用確認）に至る | [H-ANT-001](../config/hypotheses.json) 37%から更なる下方。[IND-013](../config/indicators.json) critical移行 | 90日 | [IND-013](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性の制度化は差別化の消失ではなく次元の変化を意味し、規制捕獲戦略の側面も評価が必要 | 37% (low) | ±0%。Kano再定式化実行済み。企業LLM支出シェア40%(INFO-008 B-3)は企業市場地位を示すが安全性選択理由かの判別不能。CVE-8.7継続的矛盾。Security Controls Assurance Lead採用(INFO-016 A-3)はコンプライアンス体制強化 | [INFO-003](../Information/2026-06-29/collected-raw.md#INFO-003) [INFO-016](../Information/2026-06-29/collected-raw.md#INFO-016) | [INFO-013](../Information/2026-06-29/collected-raw.md#INFO-013) [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 56% (medium) | -2%（58→57→56%・2R連続-1%）。Claude Code採用24%(INFO-006 C-3)・企業LLM支出シェア40%(INFO-008 B-3)のC蓄積だが、DAU 10R連続不在(v4.20閾値8Rを2R超過)がI方向。Claude API毎日障害(INFO-013 C-3)・Cursor $60B買収は競合強化。medium→low移行検討・DEGRADED制約でラベル変更保留。56%はFable 5 #1・Opus 4.8 SWE-bench #1に依存 | [INFO-006](../Information/2026-06-29/collected-raw.md#INFO-006) [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) [INFO-012](../Information/2026-06-29/collected-raw.md#INFO-012) | [arbiter-2026-06-29](../state/arbiter-2026-06-29.md) [INFO-013](../Information/2026-06-29/collected-raw.md#INFO-013) [INFO-049](../Information/2026-06-29/collected-raw.md#INFO-049) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | ±0%。棄却候補継続。Google $40B投資でインフラ二重集中更に加速。$30B調達で独立性の財務的裏付けは強化されたがインフラ依存は不変 | (該当なし) | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) |
| [H-GOV-001](../config/hypotheses.json) | 政府が経済的手段でAnthropicの安全性姿勢に圧力をかける先例が確立された。(a)命題に特化。(b)はH-GOV-002として分離 | 55% (medium) | ±0%凍結（Arbiter v4.22条件活性化）。INFO-067選択的執行(B-2)の診断的価値は極めて高いが、累積ドリフト(52→56%提案=+4%)の系統的リスクでsafeguard優先。証拠は次回COMPLETE交差検証のために保全。Trump EO 14409/14412(INFO-031 A-2)で制度的枠組み強化。Anthropic $30B/$900B(INFO-043 A-2)はI方向（先例確立≠実効性確認） | [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) [INFO-031](../Information/2026-06-29/collected-raw.md#INFO-031) [INFO-035](../Information/2026-06-29/collected-raw.md#INFO-035) | [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) [INFO-009](../Information/2026-06-29/collected-raw.md#INFO-009) [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) |
| [H-GOV-002](../config/hypotheses.json) | 政府のAnthropic圧力先例がAI業界全体に波及し、順応報酬構造を通じて安全性研究の戦略的価値が構造的に低下する | 23% (low) | +2%（21→22→23%・2R連続+1%）。Pentagon Anthropic置換テスト(INFO-064 B-3)は順応報酬構造の初の具体的直接証拠。6社軍事協定署名(INFO-067 B-2)。但しC=3件中2件は同一因果チェーン派生で確証バイアスリスク。絶対条件20R連続未達成 | [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) [INFO-033](../Information/2026-06-29/collected-raw.md#INFO-033) | [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) [INFO-003](../Information/2026-06-29/collected-raw.md#INFO-003) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 36% (low) | ±0%。「79%導入」≠「30%自動化達成」の定義ギャップ未解決。Oracle 21K削減(INFO-036 B-2)は方向C | [INFO-036](../Information/2026-06-29/collected-raw.md#INFO-036) | [INFO-028](../Information/2026-06-24/collected-raw.md#INFO-028) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が変容し、「設計・評価・方向付けする能力」の価値が上昇する | 72% (medium) | +2%（70→71→72%・2R連続+1%）。Stanford HAI(A-2: 22-25歳SWE -20%)・WEF(A-2: 86%組織変革)・WEF/PwC(A-2: 4次元FW)の労働市場直接定量データは極診断的。C=7 vs I=1。「価値変容」≠「価値低下」区別維持 | [INFO-050](../Information/2026-06-29/collected-raw.md#INFO-050) [INFO-051](../Information/2026-06-29/collected-raw.md#INFO-051) [INFO-068](../Information/2026-06-29/collected-raw.md#INFO-068) | (METR 43%本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流と下流に集中する | 58% (medium) | ±0%。方向性支持・速度不確定。McKinsey代理店disintermediation(INFO-038 A-3)・SaaS→AaaS移行(INFO-039 B-3) | [INFO-038](../Information/2026-06-29/collected-raw.md#INFO-038) [INFO-039](../Information/2026-06-29/collected-raw.md#INFO-039) | [INFO-056](../Information/2026-05-28/collected-raw.md#INFO-056) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | 企業LLM支出シェア40%（Menlo）。Q2営業利益$559M/ARR $47B。$30B調達/$900B評価。high/rising | 2026-06-29 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | Claude API月間毎日障害(INFO-013 C-3)・Security Controls Assurance Lead採用(INFO-016 A-3)・BARR「Feds Pull Plug」(INFO-017 B-2)。新規A-2実被害なし。high/rising | 2026-06-29 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」検証突破で elevated→high | Fable 5/Mythos 5アクセス停止継続(17日目)・Seedance 2.5・ARC-AGI-1 Qwen3 96%。Anthropic 3モデルがChatbot Arena上位独占(INFO-042 B-3)。「真の理解」未解決。elevated/stable | 2026-06-29 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | Claude API毎日障害・GitHub SLA miss→AWS路由・NexGen $315K移行コスト。期待-実態ギャップ構造的継続。high/rising | 2026-06-29 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | MCP 2026-07-28 RC・Enterprise-Managed Auth for MCP・1000+スキル。Fable 5/Mythos 5アクセス停止で利用制限。high/rising | 2026-06-29 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 広範なタスクでのRSI再現・外部検証で critical | RSI by 2028 Anthropic共同創業者(INFO-057 B-2)・AI Scientist Nature掲載(INFO-061 A-3)・Hassabis AGI ~2030(INFO-054 A-2)。high/rising | 2026-06-29 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | $30B調達/$900B評価・hyperscaler capex $602-700B・JPMorgan $5.5T。資本流入加速確定的。high/rising | 2026-06-29 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | （critical到達済み） | **critical/rising**。選択的執行(INFO-067 B-2)・Pentagon置換テスト(INFO-064 B-3)・Trump EO 14409/14412(INFO-031 A-2)・KIQ-MIL-001部分回答(INFO-004 B-3)。条件2（A-2技術的安全事故）は未到達。構造的変更保留（DEGRADED制約） | 2026-06-29 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-29 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 55% ±0%凍結（Arbiter v4.22条件活性化・4R連続Red不在）。[H-GOV-002](../config/hypotheses.json) 22→23%（+1%・順応報酬構造の初の直接証拠）。[H-ANT-002](../config/hypotheses.json) 57→56%（-1%・DAU 10R連続不在）。[H-CAR-002](../config/hypotheses.json) 71→72%（+1%・Stanford HAI A-2）。選択的執行（[INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) B-2）・Pentagon置換テスト（[INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) B-3）・$30B/$900B調達（[INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) A-2）・Claude API毎日障害（[INFO-013](../Information/2026-06-29/collected-raw.md#INFO-013) C-3）を反映。全§5最終確認日更新 | [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) [INFO-013](../Information/2026-06-29/collected-raw.md#INFO-013) [INFO-050](../Information/2026-06-29/collected-raw.md#INFO-050) | H-GOV-001 55%（凍結）・H-GOV-002 22→23%・H-ANT-002 57→56%・H-CAR-002 71→72% |
| 2026-06-27 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 54% ±0%（方向転換: 54→53→52→53→54%・3R連続-1%後2R連続+1%）。[H-ANT-002](../config/hypotheses.json) 62→58%（4R連続-1%・DAU 8R連続不在）。Pentagon標的選定ドクトリン改訂（[INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) A-2）・Anthropic Q2 $559M利益（[INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) A-2）を反映 | [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) | H-GOV-001 54%（方向転換）・H-ANT-002 62→58% |
| 2026-06-23 | 全面書き直し。Google最大$40B投資報道・Anthropic $1Tセカンダリ+Jumper移籍を反映。[H-GOV-001](../config/hypotheses.json) 56→54%・[H-ANT-002](../config/hypotheses.json) 64→62% | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) | H-GOV-001 56→54%・H-ANT-002 64→62% |
| 2026-06-21 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 58→56%（判事Rita Lin「違法な報復」判断 A-2）。[IND-030](../config/indicators.json) high→critical | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | H-GOV-001 58→56%・IND-030 high→critical |
| 2026-06-17 | H-GOV-001(a)/(b)分割実行。(a)39→55% low→medium・(b)H-GOV-002新規20% low | 2026-06-17複数INFO | H-GOV-001 39→55%・H-GOV-002新規20% |

## 7. ブラインドスポット

- [H-GOV-001](../config/hypotheses.json) 55%は凍結中の暫定値である。選択的執行（INFO-067）の診断的価値は極めて高いが、4R連続Red不在下での累積ドリフトリスクがsafeguard優先された。次回COMPLETEでの商業成功パラドックス代替解釈交差検証が絶対必須条件である。この交差検証なしに凍結を解除すべきでない。
- 選択的執行の解釈が二項対立的である。「政府の選択性＝介入能力の構造化」（C方向）と「政府の選択性＝普遍的安全性懸念の否定」（I方向）のいずれが妥当か。GPT-5.5に同じ脆弱性がありながらOpenAIが無措置である事実は、介入が安全性ではなくコンプライアンスに基づいていることを示唆するが、これがH-GOV-001を強めるか弱めるかの判別が次回COMPLETEまで保留されている。
- Pentagon Anthropic置換テスト（INFO-064）が displacementの構造化を示すが、OpenAI/Googleが実際にClaudeを置換するか、テストのみで終わるかは未確定である。H-GOV-002の23%はこの不確定性地帯にある。
- [H-ANT-002](../config/hypotheses.json) 56%は過渡期の値。DAU 10R連続不在でmedium→low移行条件が倍加した。次回COMPLETEでのRed交差検証後にラベル変更が実施される可能性が高い。56%と45%（medium/low境界）の距離が縮小している。
- Fable 5/Mythos 5アクセス停止が17日目。技術リーダーシップ（Fable 5 #1・Opus 4.8 SWE-bench #1・Chatbot Arena上位独占）の活用可能性が制限されたままである。停止が長期化すればH-ANT-002 56%の維持根拠が弱まる。Chatbot ArenaではAnthropic 3モデルが上位独占（INFO-042 B-3）しているが、アクセス停止中は新規ユーザー獲得に直結しない。
- Anthropic $30B調達/$900B評価が政府介入の無効性を示すのか、介入がまだ効果発現前であることを示すのかの判別が不能。SCR指定・輸出管理指令の帰趗が確定していない段階での評価額$900Bは、介入効果の最終評価材料として不十分であると同時に、先例確立≠実効性確認の不均衡を拡大する。
- Claude APIの月間ほぼ毎日の障害（INFO-013 C-3）が、一時的インフラ問題か構造的キャパシティ不足かの判別が不能。Notionが12時間の障害後にAnthropic統合を一時無効化した事実は、エンタープライズ採用の信頼性ボトルネックを示す。
- Claude Corps $150Mフェローシップ（INFO-003 A-3）が、真の社会的責任投資かIPO前のブランディングかの判別が困難。AI政策枠組み"Policy on the AI Exponential"との同時発表は戦略的 positioningだが、安全性研究への資金コミットメントとの因果が不明。
- Google $40B投資は「最大$40B」であり最終額が未確定。Anthropic $30B調達の構成（Google参加比率・他投資家）も非公開。$900B評価額の算定根拠が複数ソースで一致しない可能性がある。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) | 選択的執行タイムライン・GPT-5.5同脆弱性だがOpenAI無措置・6社軍事協定署名(B-2) |
| [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) | Pentagon Anthropic置換テスト・OpenAI/Google順応→契約獲得(B-3) |
| [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) | OpenAI Series H $65B/$965B・Anthropic $30B/$900B(A-2) |
| [INFO-009](../Information/2026-06-29/collected-raw.md#INFO-009) | Anthropic $30B調達/$900B評価・AI予算ROI志向シフト(B-2) |
| [INFO-013](../Information/2026-06-29/collected-raw.md#INFO-013) | Claude API月間毎日障害・Notion 12時間停止(C-3) |
| [INFO-003](../Information/2026-06-29/collected-raw.md#INFO-003) | Claude Corps $150M・1000人フェローシップ(A-3) |
| [INFO-031](../Information/2026-06-29/collected-raw.md#INFO-031) | Trump EO 14409/14412・AI革新・暗号攻撃安全保障(A-2) |
| [INFO-035](../Information/2026-06-29/collected-raw.md#INFO-035) | Hegseth SCR指定・Anthropic v. DoW修正第1条提訴(B-2) |
| [INFO-050](../Information/2026-06-29/collected-raw.md#INFO-050) | Stanford HAI: 22-25歳SWE雇用約20%減少(A-2) |
| [INFO-057](../Information/2026-06-29/collected-raw.md#INFO-057) | RSI by 2028・Anthropic共同創業者予測(B-2) |
| [INFO-006](../Information/2026-06-29/collected-raw.md#INFO-006) | Claude Code採用率3%→24%・DAU公式発表不在(C-3) |
| [INFO-016](../Information/2026-06-29/collected-raw.md#INFO-016) | Security Controls Assurance Lead採用(A-3) |
| [INFO-017](../Information/2026-06-29/collected-raw.md#INFO-017) | BARR「Feds Pull Plug」Fable 5/Mythos 5停止確認(B-2) |
| [INFO-042](../Information/2026-06-29/collected-raw.md#INFO-042) | Chatbot Arena Anthropic 3モデル上位独占(B-3) |
| [Arbiter v4.23](../state/arbiter-2026-06-29.md) | H-GOV-001凍結・H-GOV-002 +1%・H-ANT-002 -1%・H-CAR-002 +1%・DEGRADED 4R連続 |
| [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) | Pentagon標的選定ドクトリン改訂(A-2) |
| [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) | Anthropic Q2営業利益$559M/ARR $47B(A-2) |
| [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) | 企業LLM支出シェアAnthropic 40%(B-3) |
| [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) | 判事Rita Lin「違法な報復」判断(A-2) |
| [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | 輸出管理指令全容(A-1) |
| [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) | Google最大$40B Anthropic投資報道(B-2) |
| [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) | CVE-8.7 CVSS 8.7 RCE脆弱性(A-3) |
