# Anthropic

> 最終判断更新: 2026-08-02
> 全体確信度: 中
> 情報非対称性: Claude Code固有DAU/WAU絶対値が38R/39R連続不在（KIQ-ANT-002 部分打破継続・周辺データ豊富化と核心データ不在の併存）。収益内訳はAPI/Enterprise/Consumerセグメント非公開。Anthropic ARRが$47B（2026年5月）（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2）に到達。前回「$47BはOpenAI誤帰属」とした構造的不確実性は解消された。$965B評価額・Series H $65B調達（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2・[INFO-063](../Information/2026-08-02/collected-raw.md#INFO-063) B-2）で世界最高値スタートアップ。Claude Code $8B ARR・AIコーディング市場54%シェア・公開GitHubコミットの4%（[INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) B-2）。BenchLM Claude top-3独占: Mythos 5 #1 82.98・Opus 5 #2 82.78・Fable 5 #3 82.73（[INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061) B-2）。ペンタゴン8社契約から除外（[INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) A-2）。SCR指定・連邦差し止め命令（[INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) A-1）。DPA強制検討（[INFO-053](../Information/2026-08-02/collected-raw.md#INFO-053) B-1）。上院自律型兵器規則承認・「最大化」推奨（[INFO-019](../Information/2026-08-02/collected-raw.md#INFO-019) B-2）。Claude for Financial Services（[INFO-009](../Information/2026-08-02/collected-raw.md#INFO-009) A-3）・Claude Design（[INFO-008](../Information/2026-08-02/collected-raw.md#INFO-008) A-3）・Trust Center SOC 2/ISO 27001+42001/HIPAA（[INFO-029](../Information/2026-08-02/collected-raw.md#INFO-029) A-3）。H-GOV-001 49% medium ±0%（7R連続固定）・H-ANT-002 52% low ±0%（条件緩和A-2→B-1+部分承認）・H-GOV-002 24% low ±0%（絶対条件40R/41R不在）・H-CAR-002 59% medium -1%（60→59%・AND条件P(A)加速×P(B)定量不在）。KIQ-MIL-001 40R/41R不在・KIQ-ANT-002 38R/39R部分打破継続。Arbiter v4.54 COMPLETE
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はAnthropicを「$965B評価額と$47B ARRが示す爆発的商業成長と、ペンタゴン8社契約からの除外・DPA強制検討が示す政府排除の深化が同時に進行する企業」と読んでいる。最大の変化は3つある。第一に、Claude Codeの年次収益が$2.5B（2月）から$8B（5月）に到達し、AIコーディング市場の54%を獲得、公開GitHubコミットの4%を占めるに至った（[INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) B-2）。Arbiter v4.54はこれを「エンタープライズ史上最速成長」と認定し、KIQ-ANT-002の初の部分打破と判定した。第二に、AnthropicのARRが$47B（5月）、評価額が$965B（Series H・$65B調達・5月）に到達し、世界最高値のスタートアップとなった（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2・[INFO-063](../Information/2026-08-02/collected-raw.md#INFO-063) B-2）。直前ラウンドで「$47BはOpenAIの誤帰属」とされた構造的不確実性は、本日データでAnthropic自身のARRとして確認され、解消された。第三に、ペンタゴンが8社と分類環境AI展開契約を締結し（[INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) A-2）、Anthropicのみが除外された。SCR指定に対する連邦裁判所の差し止め命令が出され（[INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) A-1）、DPAを用いた安全制限の強制除去が検討されている（[INFO-053](../Information/2026-08-02/collected-raw.md#INFO-053) B-1）。もしAnthropicが政府契約に復帰すれば、この「民間爆発・政府排除」の読みは変わる。

[H-GOV-001](../config/hypotheses.json) は49% mediumで±0%（7R連続固定）。政府排除の次元は拡大し続けている。上院パネルが自律型兵器の導入を「最大化」する規則を承認し（[INFO-019](../Information/2026-08-02/collected-raw.md#INFO-019) B-2）、ペンタゴンが8社と契約を締結した一方でAnthropicのみが除外された。SCR指定に対する連邦差し止め命令とDPA強制検討は、介入手段の多様性（N=4: SCR/DPA/上院規則/調達除外）を示すが、対象は依然としてAnthropic単独（N=1）であり、因果チェーンの独立性问题は未解決である。Arbiter v4.54は仮説を支持する証拠のA-1品質（SCR連邦差し止め）と仮説を弱める証拠のB-2品質（商業的成功$965B）の非対称性を構造的制約として記録した。

直前ラウンドの最大の構造的不確実性であった「$47B ARRの誤帰属」問題は解消された。$47BはAnthropic自身のARR（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2）として確認され、ARR軌跡は$1B（2025年初）から$14B（2026年2月）を経て$30B超（2026年4月）に至り、$47B（2026年5月）に到達している。但しGAAP財務開示は依然として不在であり、B-2品質の情報に基づく確度階層である点は不変である。

## 1. コア判断

全体確信度は中。本ラウンドの最重要判断は3つある。第一に、$47B ARR確定と$965B評価額到達による商業的軌道の爆発的加速の確認。第二に、ペンタゴン8社契約からの除外・SCR連邦差し止め・DPA強制検討による政府排除の次元拡大の継続。第三に、H-CAR-002段階的引き下げ（60→59%）とBenchLM top-3独占の同時観測。

### $47B ARR確定・$965B評価額・Claude Code $8B到達

直前ラウンドで「Anthropic $47B ARR」として中核証拠扱いされた数値がOpenAIの誤帰属である可能性が高いと判断された構造的不確実性は、本日データで解消された。$47BはAnthropic自身のARR（2026年5月）として確認された（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2）。ARR軌跡は$1B（2025年初）から$14B（2026年2月）を経て$30B超（2026年4月）に至り、$47B（2026年5月）に到達している。Series Hで$65Bを調達し、評価額$965Bに到達した（[INFO-063](../Information/2026-08-02/collected-raw.md#INFO-063) B-2）。世界最高値のスタートアップである。Claude MAUは2億4500万、1日あたり100万超の新規サインアップを記録している。

Claude Codeの成長はArbiter v4.54が「最も重要な発見」と認定した。年次収益が$2.5B（2月）から$8B（5月）に到達し（[INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) B-2）、3ヶ月で3.2倍に急増した。AIコーディング市場シェアは54%、エンタープライズ顧客の50%超が利用し、年初からWAUが2倍、エンタープライズサブスクリプションが4倍、全公開GitHubコミットの4%をClaude Codeが占める。Arbiterはこの6つのデータポイントが複数指標の相互確認構造を持ち、形式的なB-2品質を超える統合的重量を有する可能性を認め、[H-ANT-002](../config/hypotheses.json)の条件緩和（A-2→B-1+）を部分承認した。但し、出所独立性（同一ソースクラスタの複数指標 vs 複数独立ソース）の検証が次回の優先条件であり、+1%の確度変更は出所独立性確認後に保留されている。ArbiterはBlue Agentの二重ヘッジ構造（±0%提案と条件緩和申し送りの並行）を分析責任の先送りとして構造的に記録した。

### 政府排除の次元拡大: ペンタゴン8社除外・SCR連邦差し止め・DPA強制検討

政府排除は次元を拡大し続けている。ペンタゴンがSpaceX・OpenAI・Google・NVIDIA等8社と分類環境でのAI展開契約を締結した（[INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) A-2）。Anthropicのみが除外された。SCR指定に対しては連邦裁判所が差し止め命令を出し（[INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) A-1）、政権は全連邦機関にAnthropic製品の使用停止を命じた。ペンタゴンはDefense Production Actを用いて安全制限の強制除去を検討している（[INFO-053](../Information/2026-08-02/collected-raw.md#INFO-053) B-1）。上院パネルは自律型兵器の導入を「最大化」する規則を承認した（[INFO-019](../Information/2026-08-02/collected-raw.md#INFO-019) B-2）。executiveとlegislativeの2枝が同時に圧力をかけている。

[H-GOV-001](../config/hypotheses.json) は49% mediumで±0%（7R連続固定）。介入手段の多様性（SCR指定・DPA脅迫・上院規則・調達除外、N=4）は確認されるが、対象はAnthropic単独（N=1）であり、因果チェーンの独立性问题は未解決である。Arbiterは仮説を支持する証拠のA-1品質（SCR連邦差し止め）と仮説を弱める証拠のB-2品質（商業的成功$965B）の非対称性を記録し、第2のAI企業への同種介入出現を優先収集条件とした。[H-GOV-002](../config/hypotheses.json)（順応報酬構造の業界全体波及）は24% lowで±0%。絶対条件（全主要AI企業の安全性研究予算の経時的減少A-2確認）が40R/41R連続不在である。

### BenchLM top-3独占とフロンティア製品層の拡張

BenchLMランキングでAnthropicモデルがtop-3を独占した（[INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061) B-2）。Claude Mythos 5が82.98で首位、Opus 5が82.78で2位、Fable 5が82.73で3位であり、GPT-5.6 Sol（81.36）を上回る。フロンティア性能の優位が維持されている。

製品層の拡張も継続している。Claude for Financial Services（[INFO-009](../Information/2026-08-02/collected-raw.md#INFO-009) A-3）はBridgewater・AIG・Commonwealthと提携し、Vals AI benchmarkでトップ評価を獲得した。Claude Design（[INFO-008](../Information/2026-08-02/collected-raw.md#INFO-008) A-3）はOpus 4.7を基盤とするデザインコラボレーションツールである。Anthropic Trust Center（[INFO-029](../Information/2026-08-02/collected-raw.md#INFO-029) A-3）はSOC 2・ISO 27001/42001・HIPAA・NIST 800-171準拠を開示し、エンタープライズ向けコンプライアンス基盤を強化した。Code Execution ToolとSandbox Runtime（[INFO-040](../Information/2026-08-02/collected-raw.md#INFO-040) A-3）はエージェントの自律コード実行環境を提供する。

[H-ANT-002](../config/hypotheses.json) は52% lowで±0%。Claude Code $8B ARR・54%シェア・4% GitHubコミット（[INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) B-2）は統合的重量を持つが、出所独立性検証が次回条件であり、+1%は保留されている。KIQ-ANT-002（Claude Code固有DAU/WAU）は38R/39R連続不在だが、周辺データの豊富化により初の部分打破が認定された。

[H-CAR-002](../config/hypotheses.json) は59% medium（-1%・60→59%）。Arbiter v4.54はRed反証強度「強」を採用し、AND条件P(A∩B)においてP(A)方向性加速（KPMG 64%・3.6倍急増）とP(B)固有定量データ不在（KIQ-CAR-002-OPS技術的不充足継続）の論理的帰結として引き下げを実行した。品質格下げ（A-2→B-2）を「停止根拠」とする両方向回避メカニズムを却下した。低下軸は引き続き圧倒的であり、上昇軸の定量データ不在が累積している。次回も上昇軸定量不在で58%引き下げ再検討となる。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Claude Code $8B ARR・54%市場シェア・公開GitHub 4%・enterprise >50%・WAU 2x・サブスク4x | [H-ANT-002](../config/hypotheses.json) 統合的証拠重量・条件緩和部分承認。KIQ-ANT-002初の部分打破。出所独立性検証が次回条件 | B-2 | [INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) |
| 高 | $47B ARR確定（5月）・$965B評価額・Series H $65B調達・245M MAU・世界最高値スタートアップ | $47B誤帰属の構造的不確実性解消。[H-GOV-001](../config/hypotheses.json) 商業的成功パラドックスで確度を弱める方向。[IND-029](../config/indicators.json) high/rising強化 | B-2 | [INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) [INFO-063](../Information/2026-08-02/collected-raw.md#INFO-063) |
| 高 | ペンタゴン8社契約・Anthropicのみ除外 | [H-GOV-001](../config/hypotheses.json) 政府排除の次元拡大。介入手段多様性N=4・対象N=1。[IND-030](../config/indicators.json) critical強化 | A-2 | [INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) |
| 高 | SCR指定・連邦裁判所差し止め命令・全連邦機関使用停止命令 | [H-GOV-001](../config/hypotheses.json) 仮説を支持する方向のA-1品質。7R連続固定の構造的制約 | A-1 | [INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) |
| 高 | DPA強制検討: 安全制限の強制除去 | [H-GOV-001](../config/hypotheses.json) 介入手段の多様化。DPA（朝鮮戦争時代法）のAI安全制限への適用 | B-1 | [INFO-053](../Information/2026-08-02/collected-raw.md#INFO-053) |
| 高 | 上院パネル自律型兵器規則承認・「最大化」推奨 | [IND-030](../config/indicators.json) critical強化。executive+legislative 2枝圧力。KIQ-MIL-001 40R/41R不在 | B-2 | [INFO-019](../Information/2026-08-02/collected-raw.md#INFO-019) |
| 高 | BenchLM Claude top-3独占: Mythos 5 #1(82.98)・Opus 5 #2(82.78)・Fable 5 #3(82.73) | [H-ANT-002](../config/hypotheses.json) フロンティア性能優位の継続。[IND-025](../config/indicators.json) elevated/stable | B-2 | [INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061) |
| 中 | Claude for Financial Services・Claude Design・Trust Center(SOC 2/ISO 27001+42001/HIPAA)・Code Execution Tool | [H-ANT-002](../config/hypotheses.json) エンタープライズ製品層の拡張。コンプライアンス基盤の強化 | A-3 | [INFO-009](../Information/2026-08-02/collected-raw.md#INFO-009) [INFO-008](../Information/2026-08-02/collected-raw.md#INFO-008) [INFO-029](../Information/2026-08-02/collected-raw.md#INFO-029) [INFO-040](../Information/2026-08-02/collected-raw.md#INFO-040) |
| 中 | Klarna再雇用・Duolingo撤回・PwC 56%プレミアム | [H-CAR-002](../config/hypotheses.json) 低下軸強化（-1%）。上昇軸部分進展だが固有定量不在 | B-2 | [INFO-027](../Information/2026-07-21/collected-raw.md#INFO-027) [INFO-050](../Information/2026-07-21/collected-raw.md#INFO-050) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Anthropicが政府契約に復帰する | 「民間爆発・政府排除」のコア判断が崩れ、H-GOV-001の制度基盤が弱体化する | 365日 | [IND-030](../config/indicators.json) |
| Claude Code $8B ARRの6データポイントの出所独立性が確認される（複数独立ソースか同一クラスタか） | H-ANT-002 52%の+1%検討条件が確定し、条件緩和の完全承認か部分承認継続かが判定される | 次回 | [H-ANT-002](../config/hypotheses.json) |
| Anthropic-Pentagon以外のAI企業に対する同種の政府介入が観測される | 因果チェーンの独立性问题が解消し、H-GOV-001の「先例」一般化が可能になる | 180日 | [IND-030](../config/indicators.json) |
| Anthropicの公式GAAP開示/IPO目論見書が到達する | B-2品質ベースの確度階層の構造的脆弱性が解消または確定する | 180日 | [H-ANT-002](../config/hypotheses.json) |
| KIQ-CAR-002-OPS（設計・評価能力固有プレミアム）の定量データが公表される | 「新スキル上昇」軸の確証有無が判定され、H-CAR-002 59%の妥当性が確定する | 90日 | [H-CAR-002](../config/hypotheses.json) |
| [H-GOV-001](../config/hypotheses.json) が45%を割る | 介入の実効性が棄却水準に接近し、mediumからlow帯へ移行する | 180日 | [H-GOV-001](../config/hypotheses.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性の制度化は差別化の消失ではなく次元の変化を意味し、規制捕獲戦略の側面も評価が必要 | 38% low | ±0%（v4.54 COMPLETE）。Pentagon対立の核心確認だが因果分離不能（KIQ-FLI-001不在）。安全性制度化の進行（Trust Center SOC 2/ISO 42001・[INFO-029](../Information/2026-08-02/collected-raw.md#INFO-029) A-3）と軍事排除の拡大の二面性。38%はlow帯上限 | [INFO-025](../Information/2026-07-21/collected-raw.md#INFO-025) [INFO-029](../Information/2026-08-02/collected-raw.md#INFO-029) | (軍事排除が差別化逆転の兆候か判別不能) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code・Claude Agent SDKが開発者エコシステムで急成長しエンタープライズAI開発の標準ツールになる | 52% low | ±0%（v4.54 COMPLETE）・条件緩和(A-2→B-1+)部分承認。Claude Code $8B ARR・54%シェア・4% GitHub・enterprise >50%・WAU 2x・サブスク4x（[INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) B-2）=統合的重量・複数指標の相互確認構造。BenchLM top-3独占（[INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061) B-2）。但し出所独立性検証が次回優先条件・+1%は保留。KIQ-ANT-002 38R/39R部分打破継続 | [INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) [INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061) | 出所独立性未検証 |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% low | ±0%（v4.54 COMPLETE）。マルチクラウド展開の直接証拠不在。棄却候補継続 | (該当なし) | (マルチクラウド証拠不在) |
| [H-GOV-001](../config/hypotheses.json) | 政府が経済的手段（SCR指定・調達禁止・DPA脅迫）で特定AI企業（Anthropic）の安全性姿勢に対する圧力をかける先例が確立された | 49% medium | ±0%（v4.54 COMPLETE・7R連続固定・構造的制約記録）。SCR連邦差し止め（[INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) A-1）・ペンタゴン8社除外（[INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) A-2）・DPA強制検討（[INFO-053](../Information/2026-08-02/collected-raw.md#INFO-053) B-1）・上院規則（[INFO-019](../Information/2026-08-02/collected-raw.md#INFO-019) B-2）=介入手段多様性N=4。但し対象N=1。$965B評価額（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2）は商業的成功パラドックスで確度を弱める方向。支持証拠A-1 vs 弱体化証拠B-2の非対称性記録 | [INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) [INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) | [INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) |
| [H-GOV-002](../config/hypotheses.json) | 政府のAnthropic圧力先例がAI業界全体に波及し、順応報酬構造を通じて安全性研究の戦略的価値が構造的に低下する | 24% low | ±0%（v4.54 COMPLETE）。絶対条件40R/41R連続不在。介入手段多様性N=4（SCR/DPA/上院規則/調達除外）は確認されるが、業界全体への波及は観測されず | [INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) | [INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 36% low | ±0%（v4.49 COMPLETE）。Klarna再雇用・Duolingo撤回（[INFO-027](../Information/2026-07-21/collected-raw.md#INFO-027)）でAI代替の可逆性が実証され定義ギャップ未解決。30%自動化達成の変換は未解決 | [INFO-027](../Information/2026-07-21/collected-raw.md#INFO-027) | (因果ギャップ未解決) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及でコーディング能力の市場価値は、直接実装スキルの構造的価値低下と設計・評価・方向付け能力への新スキル需要の二極化が同時進行する | 59% medium | -1%（v4.54 COMPLETE・60→59%）。AND条件P(A∩B)でP(A)方向性加速（KPMG 64%・3.6倍急増）×P(B)固有定量データ不在（KIQ-CAR-002-OPS技術的不充足継続）=引き下げ論理的帰結。Red反証強度「強」採用。両方向回避メカニズム却下。AI Boomerang Effect（N=3限界）の過大評価是正。Klarna/Duolingoリバーサル（[INFO-027](../Information/2026-07-21/collected-raw.md#INFO-027) B-2）。PwC 56%プレミアム（[INFO-050](../Information/2026-07-21/collected-raw.md#INFO-050) B-2）は上昇軸部分進展だが固有定量不在。次回も上昇軸定量不在で58%引き下げ再検討・medium維持 | [INFO-027](../Information/2026-07-21/collected-raw.md#INFO-027) [INFO-039](../Information/2026-07-21/collected-raw.md#INFO-039) | [INFO-050](../Information/2026-07-21/collected-raw.md#INFO-050) |
| [H-CAR-003](../config/hypotheses.json) | スマイルカーブの中間圧縮によりバリューチェーン中間工程のビジネス職は3年以内に大規模再編され価値は上流と下流に集中する | 57% medium | ±0%（v4.49 COMPLETE）。方向性支持・速度不確定。WEF 2030年まで主要スキル39%変化・1億7000万新職（[INFO-039](../Information/2026-07-21/collected-raw.md#INFO-039) A-2）。FT「変容」分析（[INFO-028](../Information/2026-07-21/collected-raw.md#INFO-028)） | [INFO-039](../Information/2026-07-21/collected-raw.md#INFO-039) | (新規弱める証拠なし) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上でelevated | Claude Code $8B ARR・AIコーディング市場54%シェア・enterprise >50%（[INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) B-2）・Anthropic ARR $47B（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2）・BenchLM Claude top-3独占（[INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061) B-2）・Claude for Financial Services Bridgewater/AIG提携（[INFO-009](../Information/2026-08-02/collected-raw.md#INFO-009) A-3）。high/rising | 2026-08-02 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントでcritical | v4.54状態変更なし。critical移行条件[A-2品質実被害報告]未到達。ISACA AAISM初のAI中心セキュリティ管理認証開始(C-2)・Code Execution Tool+サンドボックス(A-3)・過去1週間SLAインシデント報道なし(F)。high/rising | 2026-08-02 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | v4.54状態変更なし。ベンチマーク多軸化・単一指標比較困難化。BenchLM Claude top-3独占(82.98/82.78/82.73)（[INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061) B-2）・HLE 64.7%(B-2)・MMMU-Pro飽和・Video-MME Gemini 3支配(C-2)。elevated/stable | 2026-08-02 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | v4.54状態変更なし。期待と実態のギャップが更に深化。80%採用/<10%スケール/95%パイロット財務リターンなし(B-2)・平均ROI 171%だが期待通り25%のみ(B-2)。ROI 171% vs 95%リターンなし矛盾の調停を次回監視項目。high/rising | 2026-08-02 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | v4.54状態変更なし。MCP標準化確定・スキルエコシステム出現。MCP AAIF寄贈・全社採用(A-2)・OpenAI Skills API(A-3)・Google Gemini CLI Skills(A-3)・エンタープライズエージェント市場プレイス(B-2)。high/rising | 2026-08-02 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | v4.54状態変更なし。RSI概念具体化と限界の同時進行。arXiv「From AGI to ASI」(B-2)・Claude Code AI研究自律実証(B-2)・AGIタイムライン予測分裂(Altman 2025/Amodei 2027/Hassabis 5-10年)(B-2)。high/rising | 2026-08-02 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | v4.54状態変更なし。資本流入加速とインフラ制約ギャップ確定的。Anthropic $965B評価（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2）・Amazon OpenAI $50B+Anthropic $25B投資(B-2)・ByteDance CapEx $280億(B-2)。high/rising | 2026-08-02 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。上院自律型兵器規則承認・「最大化」推奨（[INFO-019](../Information/2026-08-02/collected-raw.md#INFO-019) B-2）・Pentagon 8社契約・Anthropic除外（[INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) A-2）・SCR指定・連邦差し止め（[INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) A-1）・DPA検討（[INFO-053](../Information/2026-08-02/collected-raw.md#INFO-053) B-1）・調達ガバナンス限界(B-1)。KIQ-MIL-001 40R/41R不在。条件2充実史上最大水準継続・executive+legislative 2枝圧力。critical解消条件3基準いずれも未到達 | 2026-08-02 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-08-02 | 全面書き直し（企業の基本情報に事実変更: $65B Series H調達）。$47B ARR確定（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2・誤帰属懸念解消）・$965B評価額・Claude Code $8B ARR・54%シェア・4% GitHub（[INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) B-2）・BenchLM top-3独占（[INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061)）・ペンタゴン8社除外（[INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) A-2）・SCR連邦差し止め（[INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) A-1）・DPA強制検討（[INFO-053](../Information/2026-08-02/collected-raw.md#INFO-053) B-1）を新規反映。H-ANT-001 39→38%・H-ANT-002 53→52%（条件緩和部分承認）・H-CAR-002 63→59%（段階的引き下げ継続）。KIQ-ANT-002 33R/34R→38R/39R（部分打破）・KIQ-MIL-001 35R/36R→40R/41R。全件Arbiter v4.54 COMPLETE | [INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) [INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) [INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) | H-ANT-001 39→38%・H-ANT-002 53→52%・H-CAR-002 63→59% |
| 2026-07-28 | ターゲット編集（freshness 7d + H-CAR-002 63%）。Opus 5 GPQA 92.0% / Sonnet 5リリース（[INFO-064](../Information/2026-07-28/collected-raw.md#INFO-064) A-3）・SWE-bench Verified Claude Opus 4.5 90.0%（[INFO-069](../Information/2026-07-28/collected-raw.md#INFO-069) B-1）を新規反映。H-CAR-002 66→63%（v4.45-v4.49段階的引き下げ・KIQ-CAR-002-OPS定量不在累積）。H-GOV-002 23→24%。KIQ-ANT-002 26R→33R/34R・KIQ-MIL-001 28R→35R/36R。全件±0%（v4.49 COMPLETE） | [INFO-064](../Information/2026-07-28/collected-raw.md#INFO-064) [INFO-069](../Information/2026-07-28/collected-raw.md#INFO-069) | H-GOV-001 49%(±0%)・H-ANT-002 53%(±0%)・H-GOV-002 23→24%(±0%)・H-CAR-002 66→63%(±0%) |
| 2026-07-21 | 全面書き直し。「$47B ARR」誤帰属補正（[INFO-051](../Information/2026-07-21/collected-raw.md#INFO-051)・Arbiter v4.41構造的不確実性#1）・Anthropic ARR $30B+（[INFO-053](../Information/2026-07-21/collected-raw.md#INFO-053) B-1）・Fable 5リリース（[INFO-002](../Information/2026-07-21/collected-raw.md#INFO-002) A-3）・Claude Code $2.5Bランレート（[INFO-047](../Information/2026-07-21/collected-raw.md#INFO-047)）・国際アクセス禁止（[INFO-044](../Information/2026-07-21/collected-raw.md#INFO-044)）・SCR異議申し立て「報復的」（[INFO-024](../Information/2026-07-21/collected-raw.md#INFO-024)）を新規反映。仮説確度は全件±0%（v4.41 DEGRADED）。KIQ-ANT-002 24R→26R・KIQ-MIL-001 26R→28R | [INFO-053](../Information/2026-07-21/collected-raw.md#INFO-053) [INFO-002](../Information/2026-07-21/collected-raw.md#INFO-002) [INFO-044](../Information/2026-07-21/collected-raw.md#INFO-044) | H-GOV-001 49%(±0%)·H-ANT-002 53%(±0%)·H-CAR-002 66%(±0%) |
| 2026-07-18 | 全面書き直し（7日freshness timeout）。Pentagon移行期間6ヶ月確認・Claude Opus 4.8リリース・BenchLM Claude Mythos 5首位独占・Claude Code全体採用53%首位・Klarna CEO「うまくいかなかった」・McKinsey 88%/6%を新規反映 | [INFO-072](../Information/2026-07-18/collected-raw.md#INFO-072) [INFO-001](../Information/2026-07-18/collected-raw.md#INFO-001) | H-GOV-001 49%(±0%)·H-CAR-002 66%(±0%) |
| 2026-07-11 | 全面書き直し。H-CAR-002 69→68%（ステートメント修正後の同一確度論理矛盾）。Anthropic-SpaceX計算パートナーシップ・KPMG 276K統合を反映 | [INFO-001](../Information/2026-07-11/collected-raw.md#INFO-001) | H-CAR-002 69→68% |
| 2026-07-10 | 全面書き直し。H-GOV-001 53→50%（連邦政府全体禁止・SCR指定・DPA脅迫確認）。H-CAR-002 71→69% | [INFO-046](../Information/2026-07-10/collected-raw.md#INFO-046) | H-GOV-001 53→50%·H-CAR-002 71→69% |

## 7. ブラインドスポット

- 直前ラウンドの最大の構造的不確実性であった「$47B ARRの誤帰属」は解消されたが、GAAP財務開示は依然として不在である。$47B ARR（[INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) B-2）と$965B評価額（[INFO-063](../Information/2026-08-02/collected-raw.md#INFO-063) B-2）はいずれもB-2品質であり、公式財務報告に基づかない確度階層である点は不変である。公式GAAP開示またはIPO目論見書が到達するまで、収益絶対値に依拠する確度判定の信頼性は本質的に制約される。
- $965B評価額・$47B ARR・Claude Code $8Bという商業的爆発と、ペンタゴン8社除外・SCR連邦差し止め・DPA強制検討という政府排除が「別ストーリー」として並行し、両者を結ぶ核心命題（順応報酬構造の波及）が更に見えにくくなっている。$965Bの商業的成功は政府排除を補って余りあるが、因果連関をどう評価するかの基準が[H-GOV-002](../config/hypotheses.json) 24%の判断に直接響く。
- [H-GOV-001](../config/hypotheses.json) 49%は7R連続固定であり、構造的麻痺が深化している。仮説を支持する証拠のA-1品質（SCR連邦差し止め）と仮説を弱める証拠のB-2品質（商業的成功$965B）の非対称性、およびN=1の繰り返し使用（介入手段の多様性N=4 vs 対象N=1区別不在）が記録された。第2のAI企業への同種介入が出現しない限り、49%の自然的ドリフト方向が判定不能である。
- Claude Code $8B ARR（[INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) B-2）は4R連続で「最も重要な発見」を支えるシステムクリティカル証拠の集中構造を示している（INFO-007→INFO-088→INFO-084/097→INFO-017）。証拠が変わってもClaude Code ARRが中核判定を支え続ける構造は、単一証拠クラスタへの過度依存リスクを示唆する。6データポイント（$8B ARR・enterprise >50%・WAU 2x・54% share・サブスク4x・4% commits）の出所独立性検証が次回最優先である。
- [H-ANT-002](../config/hypotheses.json) 52%の条件緩和（A-2→B-1+）は部分承認にとどまり、+1%確度変更は出所独立性確認後に保留されている。Blue Agentの二重ヘッジ構造（±0%提案と条件緩和申し送りの並行）は分析責任の先送りとして記録された。条件緩和認可後、次回同水準継続で+1%検討という条件付けが機能するかの監視が必要である。
- [H-CAR-002](../config/hypotheses.json) 59%の段階的引き下げ（66→65→64→63→60→59%）はKIQ-CAR-002-OPS定量不在の累積に基づくが、一方通行ドリフトのリスクが記録されている。Arbiter v4.54は品質格下げ（A-2→B-2）を「停止根拠」とする両方向回避メカニズムを却下し、P(A)方向性加速を核心として引き下げを実行した。次回も上昇軸定量不在で58%引き下げ再検討であり、medium帯（40-69%）の下方移動が継続する可能性がある。
- ウクライナ実戦LAWS（人間オーバーライド不能・[INFO-048](../Information/2026-07-21/collected-raw.md#INFO-048) B-2）は民間A-2事故到達前の軍事版前駆状態だが、SCN-BS-001のcritical移行条件（A-2実被害報告）は技術的安全性事故を対象とし、軍事LAWS実戦展開を「枠外」に分類する形式主義が継続している。上院が自律型兵器導入の「最大化」を承認し（[INFO-019](../Information/2026-08-02/collected-raw.md#INFO-019) B-2）、ペンタゴンが8社と契約を締結した現状で、形式定義の妥当性自体が問われている。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-017](../Information/2026-08-02/collected-raw.md#INFO-017) | Claude Code $8B ARR・54%シェア・4% GitHub・enterprise >50%・WAU 2x・サブスク4x(B-2) |
| [INFO-018](../Information/2026-08-02/collected-raw.md#INFO-018) | Anthropic $965B評価額・Series H $65B調達・$47B ARR・245M MAU・世界最高値スタートアップ(B-2) |
| [INFO-019](../Information/2026-08-02/collected-raw.md#INFO-019) | 上院パネル自律型兵器規則承認・「最大化」推奨(B-2) |
| [INFO-029](../Information/2026-08-02/collected-raw.md#INFO-029) | Anthropic Trust Center: SOC 2/ISO 27001+42001/HIPAA/NIST 800-171(A-3) |
| [INFO-040](../Information/2026-08-02/collected-raw.md#INFO-040) | Code Execution Tool・Sandbox Runtime(A-3) |
| [INFO-046](../Information/2026-08-02/collected-raw.md#INFO-046) | ペンタゴン8社契約(SpaceX/OpenAI/Google/NVIDIA等)・Anthropic除外(A-2) |
| [INFO-047](../Information/2026-08-02/collected-raw.md#INFO-047) | SCR指定・連邦裁判所差し止め命令・全連邦機関使用停止(A-1) |
| [INFO-053](../Information/2026-08-02/collected-raw.md#INFO-053) | ペンタゴンDPA検討: 安全制限強制除去(B-1) |
| [INFO-061](../Information/2026-08-02/collected-raw.md#INFO-061) | BenchLM Claude top-3独占: Mythos 5 #1(82.98)・Opus 5 #2(82.78)・Fable 5 #3(82.73)(B-2) |
| [INFO-063](../Information/2026-08-02/collected-raw.md#INFO-063) | Anthropic $965B評価額・$65B Series H調達確認(B-2) |
| [INFO-009](../Information/2026-08-02/collected-raw.md#INFO-009) | Claude for Financial Services・Bridgewater/AIG/Commonwealth提携・Vals AI top(A-3) |
| [INFO-008](../Information/2026-08-02/collected-raw.md#INFO-008) | Claude Design・Opus 4.7基盤デザインコラボレーション(A-3) |
| [INFO-064](../Information/2026-07-28/collected-raw.md#INFO-064) | Claude Opus 5 GPQA 92.0%・Sonnet 5リリース(A-3) |
| [INFO-069](../Information/2026-07-28/collected-raw.md#INFO-069) | SWE-bench Verified: Claude Opus 4.5 90.0%・GPT-5.6 Sol 96.2% SOTA(B-1) |
| [INFO-023](../Information/2026-07-21/collected-raw.md#INFO-023) | OpenAI分類NW配備合意・Anthropic完全自律ストライク拒否で契約切断・xAI承諾(B-3) |
| [INFO-024](../Information/2026-07-21/collected-raw.md#INFO-024) | Anthropic SCR異議申し立て「報復的」・SCR数時間後にOpenAIペンタゴン契約(B-3) |
| [INFO-027](../Information/2026-07-21/collected-raw.md#INFO-027) | Klarna 700人AI置換後再雇用・Duolingo AI-first撤回・2026年5月AI削減38579件(B-2) |
| [INFO-044](../Information/2026-07-21/collected-raw.md#INFO-044) | 米国Anthropic最新モデル国際アクセス禁止(B-2) |
| [INFO-047](../Information/2026-07-21/collected-raw.md#INFO-047) | Claude Code $2.5Bランレート・WAU2倍・エンタープライズサブスク4倍(B-2) |
| [INFO-048](../Information/2026-07-21/collected-raw.md#INFO-048) | ウクライナ実戦LAWS: AIドローン人間オーバーライド不能追跡攻撃(B-2) |
| [INFO-050](../Information/2026-07-21/collected-raw.md#INFO-050) | PwC 2026: AIスキル56%賃金プレミアム・設計評価メタスキルプレミアム顕著(B-2) |
| [INFO-051](../Information/2026-07-21/collected-raw.md#INFO-051) | OpenAI $47Bランレート（「$47B」帰属問題の原因・現在解消）(B-2) |
| [INFO-053](../Information/2026-07-21/collected-raw.md#INFO-053) | Anthropic ARR $1B→$14B(2月)→$30B+(4月)・$30B Series G・$380B評価額(B-1) |
| [INFO-072](../Information/2026-07-18/collected-raw.md#INFO-072) | Pentagon移行期間全容: Anthropic拒否2条件・6ヶ月移行期間(B-1) |
| [INFO-032](../Information/2026-07-11/collected-raw.md#INFO-032) | 上院議員AI契約条項開示要求: SCR指定因果関係公式明文化(A-2) |
| [Arbiter v4.54](../state/arbiter-2026-08-02.md) | 確度評価の完全根拠・H-CAR-002引き下げメカニズム・H-ANT-002条件緩和部分承認・出所独立性検証条件 |
