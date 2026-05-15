# xAI → SpaceXAI

> 最終判断更新: 2026-05-15
> 全体確信度: 低
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Colossus貸与条件も非公開
> 主参照: hypotheses.json#H-XAI-001/002/003/004, indicators.json#IND-017/006/001/025/029/030

## 0. 一文要約

我々はxAIを、**SpaceXAIとしてGrok製品群を急速に拡充し、Grok Build CLIでコーディングエージェント市場に本格参入した組織**と読んでいる。最大の根拠は、Grok BuildがターミナルベースのコーディングエージェントCLIとしてSuperGrok Heavy向けにアーリーベータでローンチされ、MCP/AGENTS.md/プラグイン/フック/スキルにネイティブ対応した事実 [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) だ。Codex・Claude Codeと同じplan→review→approveワークフローに収斂しつつ、サブエージェント並列実行とworktree統合を備える。Colossus 1(220K GPU)を競合のAnthropicに貸与した事実も [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003)、SpaceXAIの位置づけを複雑化させている。Xデータ活用差別化(H-XAI-001)と宇宙・製造業特化(H-XAI-003)は37R/38R以上の証拠不在で正式に棄却した。もしSpaceXAIがGrok製品群のAPI提供を終了または大幅縮小する、またはColossus貸与がAnthropic以外にも拡大する、のいずれかが観測されたら、判断を再構築する。

## 1. コア判断

xAIの独立企業としての章は終わった。だがSpaceXAIとしてのGrok製品展開は加速しており、Grok Build CLIの登場で新たな次元に入った。

Grok BuildはコーディングエージェントCLIとして本格的な市場参入を示す [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004)。SuperGrok Heavy向けで、プラン→レビュー→承認のワークフロー、サブエージェント並列実行、worktree統合を備える。AGENTS.md、プラグイン、フック、スキル、MCPサーバーのネイティブ対応は、CodexやClaude Codeと同じエコシステム標準への適応を示す。ヘッドレスモードとACPサポートでCI/自動化にも対応する。これは汎用AI基盤(H-XAI-004)の55%を支える高診断的価値の証拠だ。

2026年4〜5月にエンタープライズ向けGrok製品群は急速に拡充された。Grok ConnectorsはSharePoint、Outlook、OneDrive、Google Workspace等の7コネクタとBring Your Own MCPサーバー機能を提供する。STTは$0.10/時間でWER 6.9%と競合を上回る。Imagine Quality ModeはText-to-Image Arenaでトップ5にランクインした。Custom Voicesは2分以内で音声クローンを作成する。

Colossus 1(220K GPU、300MW超)の全容量をAnthropicに貸与した事実 [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) は、SpaceXAIを「AIモデル開発者」から「AIインフラ提供者兼モデル開発者」へ複雑化させている。

価格競争力(H-XAI-002)はGrok STTの$0.10/時間とGrok 4.3の$1.25/$2.50でgenuine Cだが、DeepSeek V4 Proの$0.0036/Mとの競合は継続している [INFO-025](../Information/2026-05-15/collected-raw.md#INFO-025)。エージェントCLI市場の3社鼎立(Codex・Claude Code・Grok Build)が観測されており、差別化がCLI品質からエコシステム・インフラ層にシフトする構図が鮮明になった。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Grok Build CLI: plan→review→approve・MCP/AGENTS.md対応・サブエージェント並列・worktree統合 | Codex/Claude Code対抗の本格的コーディングエージェント市場参入。H-XAI-004の高診断的C | A-3 | [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) |
| 高 | Colossus 1(220K GPU)全容量をAnthropicに貸与 | SpaceXAIが「AIインフラ提供者」側面を持つ。競合に計算資源を貸す構造 | A-3 | [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) |
| 高 | H-XAI-001正式棄却: 37R+Xデータ活用証拠不在 | 当初の差別化軸が観測可能でなくなった | A-3 | (前回情報) |
| 高 | Grok Connectors: 7コネクタ + BYO MCP | エンタープライズ向けツール統合プラットフォーム。H-XAI-004のC | A-3 | (前回情報) |
| 高 | Grok STT: WER 6.9%で競合上回る、$0.10/時間 | 価格と性能の両面で競争力。H-XAI-002とH-XAI-004の二重C | A-3 | (前回情報) |
| 中 | OpenClaw/Trae連携: Claude Code・Hermes Agent等との統合パッケージ | クロスエコシステム連携の可能性。H-XAI-004のC | B-2 | [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010) |
| 中 | H-XAI-003正式棄却: 38R+特化AI製品証拠不在 | 宇宙・製造業特化の観測可能な軸が存在しなかった | A-3 | (前回情報) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| GrokのAPI提供が終了または大幅に縮小される | SpaceXAIが外部市場から撤退し内部利用に特化する場合、H-XAI-002とH-XAI-004が同時に崩れる | 90日 | [IND-006](../config/indicators.json) |
| Colossus貸与がAnthropic以外にも拡大し、SpaceXAIが「AIインフラプロバイダー」として定着する | 現在の「モデル開発兼インフラ提供」の二面性が「インフラ提供中心」に移行する | 90日 | [IND-029](../config/indicators.json) |
| Grok Build CLIのユーザー定着率が低迷し、Codex/Claude Code比で測定可能な差が開く | H-XAI-004の55%根拠が崩れ、コーディングエージェント市場での競争力に疑問 | 90日 | [IND-027](../config/indicators.json) |
| Grokの価格が$0.50/$1.00以下に引き下げられ、SpaceXがインフラコストを補填していることが確認される | H-XAI-002が「価格競争」から「内部補填」に再定義される | 60日 | [IND-001](../config/indicators.json) |
| SpaceXAIが宇宙・製造業特化AI機能を具体的に発表する | H-XAI-003の棄却が見直される | 180日 | [IND-006](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-XAI-002](../config/hypotheses.json) | 価格競争力でシェアを獲得する | 63% | Grok STT $0.10/時間+Grok 4.3 $1.25/$2.50はgenuine C。DeepSeek V4 $0.0036/M競合は継続。価格意図(市場シェア獲得かSpaceX余剰活用か)が不明 | [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) | [INFO-025](../Information/2026-05-15/collected-raw.md#INFO-025) DeepSeek価格競合 |
| [H-XAI-004](../config/hypotheses.json) | 汎用AI基盤としてエンタープライズ市場を獲得する | 55% | Grok Build CLI(高診断的C)+Connectors 7コネクタ+STT WER首位+Imagine top5+Custom Voices+Colossus提携+OpenClaw連携のC蓄積。市場シェア定量データ不在で上限キャップ | [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010) | Colossus Anthropic貸与は独立インフラ提供 |
| [H-XAI-001](../config/hypotheses.json) | (棄却) Xデータ活用でリアルタイム特化を差別化する | 35% | 37R+Xデータ活用証拠不在。xAI→SpaceXAI統合で観測の意義自体が低下 | (なし) | 37R+証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | (棄却) SpaceX統合で宇宙・製造業特化AIを展開する | 35% | 38R+直接的特化AI製品証拠不在 | [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) 軌道コンピューティング関心(非診断的) | 38R+特化製品証拠不在 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-017](../config/indicators.json) | Xデータ独占活用の有無 | 新規証拠で elevated | 38R以上新規証拠不在。H-XAI-001棄却確定 | 2026-05-15 |
| [IND-006](../config/indicators.json) | Grokエージェントスタック採用状況 | 政府・企業の大規模採用で high | Grok Build CLI+Connectors 7コネクタ+BYO MCP [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004)。$200M Pentagon契約 | 2026-05-15 |
| [IND-001](../config/indicators.json) | Grokのベンチマーク性能 | +5pt/期で high | Grok STT WER 6.9%(競合首位)。Imagine Arena top5 | 2026-05-15 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 資本流入 vs 物理制約で high | Colossus 220K GPU Anthropic貸与 [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003)。SpaceX $3,500億評価額 | 2026-05-15 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 直接介入で high | Pentagon $200M契約。EU AI Act延期。US-China AI talks | 2026-05-15 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-15 | Grok Build CLI(コーディングエージェントCLI)新規参入・OpenClaw連携を反映して全面書き直し | [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010) | 「SpaceXAIとしてGrok製品群を急速拡充。H-XAI-001/003棄却」 → 「Grok Build CLIでコーディングエージェント市場に本格参入。3社鼎立(Codex・Claude Code・Grok Build)確定。H-XAI-004 55%」 |
| 2026-05-14 | H-XAI-001/003正式棄却 + Grok 5製品連続リリース + Colossus Anthropic提携を反映 | 2026-05-14複数INFO | 「独立企業解散」 → 「SpaceXAIとしてGrok製品群を急速拡充。H-XAI-001/003棄却」 |
| 2026-05-09 | xAI→SpaceXAI統合・Colossus Anthropic貸与・Grok 4.3リリースを反映 | 2026-05-09複数INFO | 「価格優位の独立企業」 → 「独立企業解散。SpaceXAIとして再編」 |

## 7. ブラインドスポット

- SpaceXAIの内部戦略が外部から観測不能。Grok Build CLIの連続リリースは観測できるが、その背景にある意思決定(SpaceX本体の投資判断なのか、SpaceXAI内部の戦略なのか)が判別不能。
- Colossus 1をAnthropicに貸与した理由が不明。「第1世代クラスタの余剰活用」「Anthropicとの関係構築」「企業金融的動機」のいずれか、または複合。
- Grok Build CLIの外部利用データが不在。機能面の証拠(CLI機能・MCP対応)はあるが、実際のユーザー数、API呼び出し量、エンタープライズ契約数は確認できない。
- DeepSeek V4 Proの$0.0036/Mという価格がGrok API収益モデルに与える圧力を定量できていない。
- H-XAI-001/003の棄却後、SpaceXAIとしての新しい仮説フレーム(H-XAI-005)の定義が5R連続未実行。Colossus貸与の拡大、軌道コンピューティングの進展、Grok製品群の戦略的方向性を統合する枠組みが不在。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) | Colossus 1-Anthropic コンピューティング提携(220K+ GPU) |
| [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) | Grok Build CLI(コーディングエージェント・MCP/AGENTS.md対応) |
| [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010) | OpenClaw/Coze連携(Claude Code/Trae/Hermes Agent統合) |
| [INFO-025](../Information/2026-05-15/collected-raw.md#INFO-025) | DeepSeek V4(OSS首位・フロンティア8ヶ月遅れ) |
| [Arbiter v3.78](../state/arbiter-2026-05-15.md) | 確度評価の完全根拠(付録のみ参照) |
