# Anthropic

> 最終判断更新: 2026-05-12
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが38R連続非公開。中国市場との競合観測は手薄
> 主参照: hypotheses.json#H-ANT-001/002/003, hypotheses.json#H-GOV-001, indicators.json#IND-008/013/023/027/030

## 0. 一文要約

我々はAnthropicを、**安全性堅持で民間市場を獲得しながら、DeployCo(OpenAI)の展開インフラ围い込みと38R連続ユーザー数非公開の間で確度上限が圧下され続ける企業**と読んでいる。最大の根拠は、Fortune 10中8社顧客と$300億年次化収益が示す民間市場での圧倒的集中 [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) と、Claude Design(Opus 4.7)が設計→実装のハンドオフを実現した事実 [INFO-004](../Information/2026-05-12/collected-raw.md#INFO-004)。ただしDeployCoのMcKinsey/Bain等19パートナーは安全性差別化を迂回する展開能力を持ち [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001)、コンサルティング大手のOpenAI選択は安全性が「選択理由」から「排除理由」に格下げされた可能性がある。Claude Code WAUが定量開示される、またはDeployCoの実効性が確認または否定される、のいずれかが観測されたら、判断の前提が変わる。

## 1. コア判断

Anthropicの構図は「安全性が民間市場では報われ、政府市場では代償を伴う」という二極化にある。この基本的読みに変更はない。ただし民間市場での競争構造が変わりつつある。

民間側は依然として強い。年次化収益$300億、Fortune 10中8社顧客、$100万超年間支出顧客500社超 [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006)。Claude DesignはOpus 4.7を搭載したビジュアルデザインツールで、Canva統合とClaude Codeへの直接ハンドオフを実現した [INFO-004](../Information/2026-05-12/collected-raw.md#INFO-004)。Databricks/Brilliant/Datadogが初期採用している。設計→実装のシームレス移行はAnthropicエコシステム内での围い込みを強める機能だ。Sonnet 4.6はコーディング・コンピューター使用・長文脈推論でOpus 4.5を59%の割合で上回り、1Mコンテキストウィンドウ(ベータ)を搭載した [INFO-007](../Information/2026-05-12/collected-raw.md#INFO-007)。SWE-bench 80.2%は首位を維持している。

ただしOpenAIのDeployCoが競争構造を変える可能性がある。McKinsey & Company、Bain & Companyなど19社のコンサルティング・投資パートナーが参加した$40億+の展開サービス会社は [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001)、エンタープライズAI導入の選択基準を「モデルの安全性」から「展開パートナーの実行力」にシフトさせる可能性がある。コンサルティング大手がOpenAIを選択したことは、安全性が「選択理由」から「排除理由」(安全性は必要条件だが選択理由ではなくなった)に格下げられた兆候として読める。6R連続でH-ANT-001の閾値に到達せず、50%境界(ICD 203下限)に達した。

開発者エコシステムには強材料と弱材料が混在する。Claude Design→CodeハンドオフとSonnet 4.6の改善はgenuine Cだが、38R連続でClaude Code WAU/MAUが非公開であることはH-ANT-002(62%)の根拠として重大な欠陥だ。Codex npmダウンロードは8,610万/週に対してClaude Codeは720万/週で12倍差が開いている [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008)。DeployCo FDEモデルは開発者ツール標準化の前提(開発者がツールを選択する)がFDE常駐(企業がパートナーを選択する)に市場構造が変化する可能性を示している。

政府側はPentagon除外の因果チェーンが「可能性高いが未確認」のまま。除外の事実(A-2)は確かだが、除外→安全性制度の確定という因果解釈の信頼性は別途評価が必要である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 年次化収益$300億、Fortune 10中8社、$100万超顧客500社超 | 安全性が民間市場で報われている直接の収益証拠 | C-2 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) |
| 高 | DeployCo(McKinsey/Bain等19パートナー・$40億+) | 展開能力+コンサルティングネットワークで安全性差別化を迂回可能に。H-ANT-001のgenuine I | A-3 | [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) |
| 高 | Pentagon 7社契約除外(因果は「可能性高いが未確認」) | 政府市場での代償。除外の事実はA-2だが因果確定ではない | A-2 | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) |
| 高 | Claude Design + Opus 4.7: Canva統合・Claude Codeハンドオフ | 設計→実装のシームレス移行でエコシステム围い込み強化。新フロンティアモデル | A-3 | [INFO-004](../Information/2026-05-12/collected-raw.md#INFO-004) |
| 中 | Sonnet 4.6: Opus 4.5を59%好まれる・1M context・SWE-bench 80.2%・OSWorld大幅改善 | 性能パリティの維持。価格はSonnet価格据え置き($3/$15) | A-3 | [INFO-007](../Information/2026-05-12/collected-raw.md#INFO-007) |
| 中 | SpaceX Colossus 1(300MW超)の全容量提供契約 | コンピュート供給の第3経路。Google/Amazon依存の低減 | A-2 | [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) |
| 中 | Codex npm 12倍差・Cursor 47%採用・38R連続WAU非公開 | 定量ユーザー数不在の中で競合圧力の重みが増す | C-3 | [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) |
| 低 | Agent SDK v0.2.138/v0.1.80・金融向け10種エージェント | 開発速度は速いがv0.xは安定性に課題 | A-3 | [INFO-018](../Information/2026-05-11/collected-raw.md#INFO-018) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Pentagon除外理由が公式確認され、倫理的拒否以外の理由(性能要件・ビジネス判断等)だった場合 | 「安全性の代償」の因果チェーンが崩れ、H-ANT-001とH-GOV-001の根拠が根本的に変わる | 90日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示され、Codex比で1/5以下だった場合 | H-ANT-002「標準ツール化」62%の根拠が崩れ、確度を大幅に下げる | 30日 | [IND-027](../config/indicators.json) |
| Anthropicがlawful use条項を受諾して政府契約に回帰 | コア判断(民間優先・政府放棄)とH-ANT-001が同時に崩れる | 90日 | [IND-030](../config/indicators.json) |
| DeployCo FDE常駐モデルがエンタープライス展開で成功し、安全性差別化が「選択理由」から完全に「排除理由」に格下げされる | H-ANT-001(50%)がlow帯に移行し、安全性戦略の市場有効性が根本的に疑われる | 180日 | [IND-026](../config/indicators.json) |
| $3,800億評価額での資金調達が不調に終わる | コンピュート拡張の資金基盤が崩れ、成長速度の鈍化が現実化する | 180日 | [IND-029](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 50% | 民間で機能($300億ARR・Fortune 10の8社)。DeployCo競合圧力+6R連続閾値未到達で代償蓄積重み増。50%境界(ICD 203下限)。次回low帯移行検討条件。Pentagon除外因果「未確認」継続 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) [INFO-023](../Information/2026-05-11/collected-raw.md#INFO-023) | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 62% | $25億ランレート・Claude Design→Codeハンドオフ・Sonnet 4.6改善はgenuine C。38R連続未回答沈黙の証拠累積増。Codex 12x差+Cursor 47%+DeployCo FDE競合でI蓄積。定量ユーザー数不在で確度上限圧下継続 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) [INFO-004](../Information/2026-05-12/collected-raw.md#INFO-004) [INFO-007](../Information/2026-05-12/collected-raw.md#INFO-007) | [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | SpaceX Colossus契約+Amazon数十億ドルコンピュート契約でAWS+SpaceX二重インフラ依存深化。マルチクラウド(均衡)から二重集中へ。棄却候補継続 | [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) | [INFO-004](../Information/2026-05-11/collected-raw.md#INFO-004) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 46% | Pentagon 7社契約は萎縮Cだが因果チェーン「未確認」。DeepMind union 98%は二面性。EU延期+中国裁判所判決のI蓄積。C/I均衡 | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) | [INFO-032](../Information/2026-05-11/collected-raw.md#INFO-032) [INFO-046](../Information/2026-05-11/collected-raw.md#INFO-046) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | $300億ARR・Fortune 10中8社 | 2026-05-12 |
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt以上/期で high | SWE-bench 80.2%首位。Sonnet 4.6 OSWorld大幅改善 [INFO-007](../Information/2026-05-12/collected-raw.md#INFO-007)。ARC-AGI-2 60.4% | 2026-05-12 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | GTIG AI開発ゼロデイ初検出。検出≠被害。high水準 | 2026-05-12 |
| [IND-023](../config/indicators.json) | 政府のAI企業介入 | 直接介入で high | Pentagon 7社契約・除外。因果チェーン「未確認」 | 2026-05-12 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | DeployCo 19パートナー部分開放+Azure排他性終了+OpenCode移行。high水準 | 2026-05-12 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入vs物理制約で high | $3,800億評価額・Colossus 1リース・$300億ARR。high水準 | 2026-05-12 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で elevated | AI開発ゼロデイ+GPT-5.5-Cyber防御。二面性深化。elevated水準 | 2026-05-12 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-12 | Claude Design + Opus 4.7・Sonnet 4.6 OSWorld改善・DeployCo競合圧力・38R連続未回答を反映して全面書き直し | [INFO-004](../Information/2026-05-12/collected-raw.md#INFO-004) [INFO-007](../Information/2026-05-12/collected-raw.md#INFO-007) [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) | 「民間で報われ政府で係争。因果チェーン未確認」 → 「民間で報われ政府で係争。DeployCo競合圧力で50%境界に到達。Claude Design設計→実装ハンドオフ追加」 |
| 2026-05-11 | Pentagon因果チェーン「確定」→「可能性高いが未確認」。Sonnet 4.6・Colossus 1・$3,800億評価額を反映 | [INFO-001](../Information/2026-05-11/collected-raw.md#INFO-001) [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) | 「民間で報われ政府で制度確定」→「民間で報われ政府で係争。因果チェーン未確認」 |
| 2026-05-08 | $15B JV + Claude Sonnet 4.6 + JetBrains 46% を反映 | 複数INFO | 「政府排除確定の企業」→「民間で報われ政府で係争中。JVで金融次元追加」 |

### 6.1 政府対立の時系列 (Anthropic 固有)

| 日付 | 事象 | 参照 |
|:-:|---|---|
| 2025-07 | Pentagon と $200M 契約締結 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2025-09 | GenAI.mil 展開交渉で決裂。DOD「全合法目的での無制限アクセス」要求、Anthropic「自律兵器・国内大量監視への不使用保証」で拒否 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-02-27 | Trump 政権が SCR 指定・連邦使用禁止 | [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048) |
| 2026-03-05 | DOD が Anthropic を「サプライチェーンリスク」指定 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-04-08 | 連邦控訴裁が一時差し止め請求を棄却。SCR 指定が一時確定 | [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035) |
| 2026-04-17 | Amodei と White House が「生産的・建設的」会談 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-04-23 | Trump 大統領が「Anthropic-DoD 契約は可能」と発言 | [INFO-029](../Information/2026-04-24/collected-raw.md#INFO-029) |
| 2026-04-24 | 連邦裁判所が SCR 指定の仮差し止めを認可 | [INFO-043](../Information/2026-04-28/collected-raw.md#INFO-043) |
| 2026-05-04 | Pentagon 7社契約締結、Anthropic 除外。DC回路裁判所「chilling effect」支持。除外理由は報道によるが公式確認なし | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) |
| 2026-05-06 | SpaceX Colossus 1 のAnthropic向け全容量提供契約を発表 | [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-11/collected-raw.md#INFO-004) |

## 7. ブラインドスポット

- Claude Code WAU/MAUが38R連続で非公開。$25億ランレートは金額的裏付けだが、Codexの12倍ダウンロード差 [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) やCursor 47%採用 [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) と比較した相対的市場シェアが外部から測れない。
- DeployCoの展開インフラ围い込みが安全性差別化に与える構造的影響を定量できていない。コンサルティング大手がOpenAIを選択した理由(安全性 vs 実行力)が判別不能。
- Pentagon除外の因果チェーン(除外理由→SCR指定理由→7社契約条項→Scale AI $5億の位置づけ)の各段階が未確認。公式確認が最優先の収集ギャップである。
- Claude Design→Codeハンドオフの围い込み効果が外部から測れない。Databricks/Brilliant/Datadogの初期採用はあるが、使用頻度やワークフロー定着度が不明。
- 中国市場での競合動向(DeepSeek V4等)がClaude API価格($3/$15)に与える圧力を観測する指標を持っていない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-004](../Information/2026-05-12/collected-raw.md#INFO-004) | Claude Design(Opus 4.7・Canva統合・Claude Codeハンドオフ) |
| [INFO-007](../Information/2026-05-12/collected-raw.md#INFO-007) | Sonnet 4.6(OSWorld大幅改善・1M context・SWE-bench 80.2%) |
| [INFO-001](../Information/2026-05-12/collected-raw.md#INFO-001) | DeployCo($40億+・Tomoro買収・19パートナー) - 競合圧力として |
| [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) | Anthropic統計: $300億ARR・Fortune 10中8社・$3,800億評価額 |
| [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) | Codex 12xダウンロード差・Claude Codeバグ・Grok Build |
| [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) | 157K開発者OpenCode移行 |
| [INFO-018](../Information/2026-05-11/collected-raw.md#INFO-018) | Agent SDK v0.2.138/v0.1.80・金融向け10種エージェント |
| [INFO-023](../Information/2026-05-11/collected-raw.md#INFO-023) | Enterprise 99.99% SLA |
| [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) | Pentagon 7社契約・Anthropic除外 |
| [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) | DeepMind union 98%・従業員抗議 |
| [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) | Cursor 47%採用・Claude Code $10億ランレート到達 |
| [Arbiter v3.75](../state/arbiter-2026-05-12.md) | 確度評価の完全根拠(付録のみ参照) |
