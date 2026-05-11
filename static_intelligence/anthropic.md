# Anthropic

> 最終判断更新: 2026-05-11
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが37R連続非公開。中国市場との競合観測は手薄
> 主参照: hypotheses.json#H-ANT-001/002/003, hypotheses.json#H-GOV-001, indicators.json#IND-008/013/023/027/030

## 0. 一文要約

我々はAnthropicを、**安全性堅持で民間市場を獲得しながら、政府市場からの除外理由が「確定」から「可能性高いが未確認」に格下げされた企業**と読んでいる。最大の根拠は、Fortune 10中8社顧客と$300億年次化収益が示す民間市場での圧倒的集中 [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) と、Pentagon 7社契約から除外された事実 [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) だ。ただし除外の因果チェーン(除外→倫理的拒否→SCR指定→他社報酬→制度確定)は4段階推論で各段階が未確認であり、「制度確定」という読み自体が修正を受けた。Claude Codeの定量ユーザー数が37ラウンド連続で非公開であることも、開発者市場獲得(H-ANT-002)の確度上限を圧下し続けている。Pentagon除外理由が公式確認される、またはClaude Code WAUが定量開示される、のいずれかが観測されたら、判断の前提が変わる。

## 1. コア判断

Anthropicの構図は「安全性が民間市場では報われ、政府市場では代償を伴う」という二極化にある。この基本的読みに変更はないが、二極化の因果を巡る確信度が今回下がった。

民間側は強い。年次化収益$300億 [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006)、Fortune 10中8社顧客、$100万超年間支出顧客500社超、Claude App MAU 1,248万。Claude Codeランレート収益$25億超は開発者市場での金額的裏付けとしては強力だ [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006)。Sonnet 4.6はコーディング・コンピューター使用・長文脈推論でOpus 4.5を59%の割合で上回り [INFO-001](../Information/2026-05-11/collected-raw.md#INFO-001)、1Mコンテキストウィンドウをベータ搭載した。SWE-bench 80.2%は首位を維持している。Enterprise 99.99% SLA [INFO-023](../Information/2026-05-11/collected-raw.md#INFO-023) もインフラ信頼性の指標として機能する。

政府側で重要な修正があった。Pentagon 7社契約からの除外について、我々はこれまで「Anthropicがlawful use条項を拒否したため除外された」という因果チェーンを「確定」として扱ってきた。今回のArbiter判定は、この因果チェーンを「可能性高いが未確認」に格下げした [H-GOV-001](../config/hypotheses.json)。理由は4段階推論の各段階(除外理由、SCR指定理由、7社契約条項、Scale AI $5億の位置づけ)が確認不足だからだ。除外の事実(A-2)は確かだが、除外→安全性制度の確定という因果解釈の信頼性は別途評価が必要である。

コンピュート面では第3の供給経路が加わった。SpaceXがColossus 1(300MW超)の全コンピュート容量をAnthropicに提供する契約を締結した [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-11/collected-raw.md#INFO-004)。Google最大$400億投資 [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) とAmazon数十億ドル規模コンピュート契約に次ぐ第3の柱で、コンピュート逼迫の緩和に寄与する。評価額$3,800億での資金調達協議中 [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) も、成長資金需要の大きさを示す。

開発者エコシステムには強材料と弱材料が混在する。Agent SDKがTypeScript v0.2.138、Python v0.1.80と高頻度で更新され [INFO-018](../Information/2026-05-11/collected-raw.md#INFO-018)、Managed Agentsにdreaming/outcomes/multiagent orchestrationが追加された。金融向け10種の即時利用可能エージェントもリリースされた。一方で、Claude Code WAU/MAUの定量ユーザー数が37ラウンド連続で非公開であることは「開発者標準ツール化」仮説(63%)の根拠として重大な欠陥だ [H-ANT-002](../config/hypotheses.json)。Codex npmダウンロードは8,610万/週に対してClaude Codeは720万/週で12倍差 [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008)。Cursorは47%のエンジニア採用率を記録している [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038)。Agent SDK v0.xの高頻度更新は開発速度を示すが、安定性の裏返しでもある。エンタープライズ標準には安定性が前提になる。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 年次化収益$300億、Fortune 10中8社、$100万超顧客500社超 | 安全性が民間市場で報われている直接の収益証拠 | C-2 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) |
| 高 | Pentagon 7社契約除外(因果は「可能性高いが未確認」) | 政府市場での代償。除外の事実はA-2だが因果確定ではない | A-2 | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) |
| 高 | SpaceX Colossus 1(300MW超)の全容量提供契約 | コンピュート供給の第3経路。Google/Amazon依存の低減 | A-2 | [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-11/collected-raw.md#INFO-004) |
| 高 | 評価額$3,800億での資金調達協議、Google最大$400億投資 | 成長資金需要と外部投資家の評価の両方を示す | C-2 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) |
| 中 | Sonnet 4.6: Opus 4.5を59%好まれる、1M context、SWE-bench 80.2% | 性能パリティの維持。価格はSonnet価格据え置き($3/$15) | A-3 | [INFO-001](../Information/2026-05-11/collected-raw.md#INFO-001) |
| 中 | Claude Codeランレート$25億超、ビジネスサブスク4倍増 | 開発者市場の金額的裏付け。ただしWAU定量値は非公開 | C-2 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) |
| 中 | Codex npm 12倍差、Cursor 47%採用 | Claude Codeの定量ユーザー数不在の中で競合圧力の重みが増す | C-3 | [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) |
| 中 | 157K開発者がOpenCodeに移行(サードパーティブロック後) | Anthropicの囲い込み姿勢に対する開発者のヘッジ行動 | C-3 | [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) |
| 低 | Agent SDK v0.2.138/v0.1.80、金融向け10種エージェント | 開発速度は速いがv0.xは安定性に課題 | A-3 | [INFO-018](../Information/2026-05-11/collected-raw.md#INFO-018) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Pentagon除外理由が公式確認され、倫理的拒否以外の理由(性能要件・ビジネス判断等)だった場合 | 「安全性の代償」の因果チェーンが崩れ、H-ANT-001とH-GOV-001の根拠が根本的に変わる | 90日 | [IND-030](../config/indicators.json) |
| Claude Code WAU/MAUが定量開示され、Codex比で1/5以下だった場合 | H-ANT-002「標準ツール化」63%の根拠が崩れ、確度を大幅に下げる | 30日 | [IND-027](../config/indicators.json) |
| Anthropicがlawful use条項を受諾して政府契約に回帰 | コア判断(民間優先・政府放棄)とH-ANT-001が同時に崩れる | 90日 | [IND-030](../config/indicators.json) |
| $3,800億評価額での資金調達が不調に終わる、または条件が大幅に悪化する | コンピュート拡張の資金基盤が崩れ、成長速度の鈍化が現実化する | 180日 | [IND-029](../config/indicators.json) |
| Claude Codeの「バカ化」問題(INFO-008)が解消されず、重大な品質問題に発展する | 安全性ブランドと製品信頼性が同時に傷つく | 60日 | [IND-013](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 51% | 民間で機能($300億ARR・Fortune 10の8社)するが、C/I二面性の閾値監視が5R連続未到達。Pentagon除外因果を「未確認」に格下げ。代償蓄積(市場機会喪失+$3,800億評価額資金需要)の重み増 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) [INFO-023](../Information/2026-05-11/collected-raw.md#INFO-023) | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 63% | $25億ランレート・Agent SDK高頻度リリース・Sonnet 4.6はgenuine C。37R連続未回答の沈黙の証拠累積。Codex 12x差+Cursor 47%がgenuine I。定量ユーザー数不在で確度上限圧下継続 | [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) [INFO-001](../Information/2026-05-11/collected-raw.md#INFO-001) [INFO-018](../Information/2026-05-11/collected-raw.md#INFO-018) | [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | SpaceX Colossus契約+Amazon数十億ドルコンピュート契約でAWS+SpaceX二重インフラ依存深化。マルチクラウド(均衡)から二重集中へ | [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) | [INFO-004](../Information/2026-05-11/collected-raw.md#INFO-004) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 46% | Pentagon 7社契約は萎縮Cだが因果チェーン「確定」→「未確認」。DeepMind union 98%は二面性。EU延期+中国裁判所判決のI蓄積。C/I均衡 | [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) | [INFO-032](../Information/2026-05-11/collected-raw.md#INFO-032) [INFO-046](../Information/2026-05-11/collected-raw.md#INFO-046) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | $300億ARR・Fortune 10中8社 | 2026-05-11 |
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt以上/期で high | SWE-bench 80.2%首位。Sonnet 4.6 OSWorld大幅改善。ARC-AGI-2 60.4% | 2026-05-11 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | サードパーティブロック+Claude Codeバグは品質問題。新規大規模脆弱性なし。high水準 | 2026-05-11 |
| [IND-023](../config/indicators.json) | 政府のAI企業介入 | 直接介入で high | Pentagon 7社契約・除外。因果チェーン「未確認」。DC裁判所支持 | 2026-05-11 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | Azure排他性終了+OpenAI SDK provider-agnostic+157K OpenCode移行。標準化加速。high水準 | 2026-05-11 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入vs物理制約で high | $3,800億評価額・Colossus 1リース・$300億ARR。high水準 | 2026-05-11 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で elevated | Pentagon 7社+DeepMind union 98%+EU延期+中国裁判所。規制二方向深化。elevated水準 | 2026-05-11 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-11 | Pentagon因果チェーン「確定」→「可能性高いが未確認」。Sonnet 4.6・Colossus 1リース・$3,800億評価額・37R連続未回答を反映して全面書き直し | [INFO-001](../Information/2026-05-11/collected-raw.md#INFO-001) [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) [INFO-004](../Information/2026-05-11/collected-raw.md#INFO-004) [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) | 「民間で報われ政府で制度確定」→「民間で報われ政府で係争。因果チェーン未確認。開発者市場は強材料と弱材料の混在」 |
| 2026-05-08 | $15B JV + Claude Sonnet 4.6 + JetBrains 46% を反映 | [INFO-037](../Information/2026-05-08/collected-raw.md#INFO-037) [INFO-001](../Information/2026-05-08/collected-raw.md#INFO-001) [INFO-072](../Information/2026-05-08/collected-raw.md#INFO-072) | 「政府排除確定の企業」→「民間で報われ政府で係争中。JVで金融次元追加」 |
| 2026-05-02 | コア判断を「政府排除確定」から「民間収益・政府係争の二極化」へ | Pentagon 7社契約とDC裁判所支持の同時報道 | 「政府市場から完全排除された企業」→「民間で報われ政府で係争中の企業」 |

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

- Claude Code WAU/MAUが37R連続で非公開。$25億ランレートは金額的裏付けだが、Codexの12倍ダウンロード差 [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) やCursor 47%採用 [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) と比較した相対的市場シェアが外部から測れない。
- Pentagon除外の因果チェーン(除外理由→SCR指定理由→7社契約条項→Scale AI $5億の位置づけ)の各段階が未確認。報道ソースによる推定に依存しており、公式確認が最優先の収集ギャップである。
- $3,800億評価額での資金調達が成長資金なのかコンピュート拡張資金なのかが不明。Colossus 1リースは容量確保だが、永続的な供給契約なのか一時的な措置なのかも非公開。
- Anthropicのサードパーティアクセスブロック [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) が開発者エコシステムに与える長期影響を定量できていない。157K人のOpenCode移行は「ヘッジ行動」の証拠だが、これが一時的か恒常的かの判別ができない。
- 中国市場での競合動向(DeepSeek V4等)がClaude API価格($5/$30)に与える圧力を観測する指標を持っていない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-001](../Information/2026-05-11/collected-raw.md#INFO-001) | Claude Sonnet 4.6リリース(1M context・SWE-bench 80.2%・Opus 59%好まれる) |
| [INFO-002](../Information/2026-05-11/collected-raw.md#INFO-002) | SpaceX Colossus 1 Anthropic提供契約 |
| [INFO-004](../Information/2026-05-11/collected-raw.md#INFO-004) | SpaceXAI統合・xAI解散。Colossus 1リース |
| [INFO-006](../Information/2026-05-11/collected-raw.md#INFO-006) | Anthropic統計: $300億ARR・Fortune 10中8社・$3,800億評価額 |
| [INFO-008](../Information/2026-05-11/collected-raw.md#INFO-008) | Codex 12xダウンロード差・Claude Codeバグ・Grok Build |
| [INFO-015](../Information/2026-05-11/collected-raw.md#INFO-015) | 157K開発者OpenCode移行 |
| [INFO-018](../Information/2026-05-11/collected-raw.md#INFO-018) | Agent SDK v0.2.138/v0.1.80・金融向け10種エージェント |
| [INFO-023](../Information/2026-05-11/collected-raw.md#INFO-023) | Enterprise 99.99% SLA |
| [INFO-025](../Information/2026-05-11/collected-raw.md#INFO-025) | Pentagon 7社契約・Anthropic除外 |
| [INFO-026](../Information/2026-05-11/collected-raw.md#INFO-026) | DeepMind union 98%・従業員抗議 |
| [INFO-038](../Information/2026-05-11/collected-raw.md#INFO-038) | Cursor 47%採用・Claude Code $10億ランレート到達 |
| [Arbiter v3.74](../state/arbiter-2026-05-11.md) | 確度評価の完全根拠(付録のみ参照) |
