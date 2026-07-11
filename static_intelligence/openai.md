# OpenAI

> 最終判断更新: 2026-07-11
> 全体確信度: 中低
> 情報非対称性: 収益内訳（API/Enterprise/Consumerセグメント・政府vs民間）が非公開（KIQ-OAI-001未回答継続・19R連続不在）。Q2収益$10.9Bは確認（[INFO-058](../Information/2026-07-11/collected-raw.md#INFO-058) B-3）だがセグメント内訳は不変。H1 2025で収入$4.3Bに対し純損失$13.5B（構造的赤字）。MicrosoftがOpenAI Group PBCの約27%を所有（評価額$135B）。ChatGPT 1Bユーザー到達（[INFO-053](../Information/2026-07-11/collected-raw.md#INFO-053) B-2）。GPT-5.6がMicrosoft 365 Copilot優先モデルとして選定（[INFO-065](../Information/2026-07-11/collected-raw.md#INFO-065) A-3）。RSI Index 57.9%（+16.2pt）・内部推論計算100倍・エージェント的トークン22倍（[INFO-068](../Information/2026-07-11/collected-raw.md#INFO-068) A-3）。GPT-Live音声モード発表（[INFO-005](../Information/2026-07-11/collected-raw.md#INFO-005) A-3）。Arbiter v4.32は全OpenAI仮説±0%。Arbiter v4.32 COMPLETE
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-OAI-001](../config/hypotheses.json) は49%（medium）で±0%。KIQ-OAI-001（収益内訳: API/Enterprise/Consumer・政府vs民間）が19R連続不在であり、確度変更の根拠が形成できない。Q2収益$10.9Bは量的成長を示すが、セグメント内訳が不明である限りB2B支配地位の収益的裏付けを質的に評価できず、確度の上下いずれの変更も根拠不足となる。

本ラウンドの3つの重要展開は、第一にGPT-5.6がMicrosoft 365 Copilotの優先モデルとして選定されたこと（[INFO-065](../Information/2026-07-11/collected-raw.md#INFO-065) A-3）である。エンタープライズデプロイ規模でのGPT-5.6採用は[H-OAI-001](../config/hypotheses.json)のC方向（B2B支配）の直接証拠である。第二に、RSI Index 57.9%（前年比+16.2pt）・内部推論計算100倍・エージェント的トークン22倍の具体化である（[INFO-068](../Information/2026-07-11/collected-raw.md#INFO-068) A-3）。推論スケーリングの産業指標として初の定量化である。第三に、ChatGPT 1Bユーザー到達とQ2収益$10.9Bの同時確認である（[INFO-053](../Information/2026-07-11/collected-raw.md#INFO-053) B-2・[INFO-058](../Information/2026-07-11/collected-raw.md#INFO-058) B-3）。コンシューマー規模と収益成長が同時に観測された。

GPT-5.6の三段階価格体系（Sol $5/$15・Terra $2.50/$10・Luna $1/$4 per M token）が公開された（[INFO-045](../Information/2026-07-11/collected-raw.md#INFO-045) B-2）。下位モデル（Luna）は$1/M inputであり、DeepSeek V4 Pro $1.74/Mに接近する。コモディティ化圧力と差別化戦略の同時進行を示す。GPT-Live音声モードが発表され（[INFO-005](../Information/2026-07-11/collected-raw.md#INFO-005) A-3）、リアルタイム双方向音声対話を可能にする。SkillCloakがOpenAI Skillsの全静的スキャナを突破し（[INFO-026](../Information/2026-07-11/collected-raw.md#INFO-026) B-2）、エージェントプラットフォームのセキュリティリスクが具体化した。

[H-OAI-002](../config/hypotheses.json) は44%（low）で±0%。Agent SDKのプロバイダー非依存性・Microsoft Foundry→M365 Copilot移行で囲い込み否定証拠の累積が継続。[H-OAI-003](../config/hypotheses.json) は3%（low）で±0%。商業化規模（Q2収益$10.9B・ChatGPT 1Bユーザー）が圧倒的継続。

## 1. コア判断

全体確信度は中低。H-OAI-001 49% ±0%の根拠は前回と同じく核心パラメータ不在にある。収益内訳（KIQ-OAI-001）が19R連続不在であり、確度変更の根拠が形成できない。

### GPT-5.6 M365 Copilot優先モデル選定とRSI 57.9%

GPT-5.6がMicrosoft 365 Copilotの優先モデルとして選定された（[INFO-065](../Information/2026-07-11/collected-raw.md#INFO-065) A-3）。Microsoft FoundryがMicrosoft 365 Copilotにリブランドされ、エージェント的AIプラットフォームとして統合された（[INFO-029](../Information/2026-07-11/collected-raw.md#INFO-029) A-3）。GPT-5.6 Sol/Terra/Lunaの3モデルがGA済みの状況で、M365 CopilotがデフォルトでGPT-5.6を使用することは、エンタープライズデプロイ規模でのB2B支配を示す。

RSI（Reasoning Scaling Index）が57.9%に到達し、前年比+16.2ptである（[INFO-068](../Information/2026-07-11/collected-raw.md#INFO-068) A-3）。内部推論計算量が100倍に増加し、エージェント的トークン生成が22倍になった。RSIは推論スケーリングの産業指標として初めて定量化された。この結果は2つの含意を持つ。第一に、フロンティア差別化の残存を示す。SCN-004（コモディティ化）が33%であるが、RSI 57.9%は推論能力での差別化が進行中であることを示す。第二に、IND-028（AGI到達度）のhigh/rising評価を強化する。RSI具体化と客観ベンチマーク（ARC-AGI-3 7.8%）の限界が同時進行している。

### Q2収益$10.9BとChatGPT 1Bユーザー

OpenAIのQ2 2026収益が$10.9Bに達した（[INFO-058](../Information/2026-07-11/collected-raw.md#INFO-058) B-3）。年率$43.6Bのペースであり、前四半期比で加速している。ChatGPTが1Bユーザーに到達した（[INFO-053](../Information/2026-07-11/collected-raw.md#INFO-053) B-2）。コンシューマー規模の成長と収益成長が同時に観測された。

但し、収益内訳（KIQ-OAI-001 19R連続不在）の制約は不変である。$10.9BのうちAPI/Enterprise/Consumerの構成比が不明であり、B2B支配の収益的裏付けを質的に評価できない。H1 2025で収入$4.3Bに対し純損失$13.5Bの構造的赤字が継続しているかも不明。収益絶対値の成長は確認できるが、収益性の改善・セグメント別寄与の評価は不可能である。

### GPT-5.6価格体系とコモディティ化圧力

GPT-5.6の三段階価格体系が公開された（[INFO-045](../Information/2026-07-11/collected-raw.md#INFO-045) B-2）。Sol $5/$15・Terra $2.50/$10・Luna $1/$4 per M token。Lunaの$1/M inputはDeepSeek V4 Pro $1.74/Mに接近する。OpenAIが価格競争に参加していることを示す。一方でSolの$5/$15はフロンティア価格を維持しており、差別化と価格競争の二層構造が鮮明である。

コモディティ化圧力は量的に深化している。AI API価格が高値から約20%下落した。GLM-5.2がオープンウェイト#1・全体4位にランクイン。MMLUは全社90%超で飽和。これらはH-OAI-001のI方向（コモディティ化）の証拠である。一方で、GPT-5.6 M365 Copilot優先モデル選定・RSI 57.9%・Multi-agent APIはC方向の証拠である。C/I均衡構造は不変。

### SkillCloakとエージェントセキュリティ

SkillCloakマルウェアがOpenAI Skillsの全静的スキャナを突破した（[INFO-026](../Information/2026-07-11/collected-raw.md#INFO-026) B-2）。ポリモーフィック難読化で検出回避率100%を実証した。OpenAI Skillsは2026年7月23日からEnterpriseでデフォルト有効化される予定。エージェントプラットフォームのセキュリティリスクが具体化している。Friendly Fire攻撃で防御型AIがハイジャック可能なことも確認された（[INFO-027](../Information/2026-07-11/collected-raw.md#INFO-027) B-2）。IND-013（セキュリティ侵害頻度）high/risingの評価を強化するが、critical移行条件（実被害A-2報告）は未到達。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | GPT-5.6 M365 Copilot優先モデル選定: Microsoft Foundry→M365 Copilotリブランド・エージェント的AI統合 | [H-OAI-001](../config/hypotheses.json) C方向。エンタープライズデプロイ規模でのB2B支配の直接証拠 | A-3 | [INFO-065](../Information/2026-07-11/collected-raw.md#INFO-065) [INFO-029](../Information/2026-07-11/collected-raw.md#INFO-029) |
| 高 | RSI Index 57.9%（+16.2pt）: 内部推論計算100倍・エージェント的トークン22倍・推論スケーリング初の産業定量化 | [H-OAI-001](../config/hypotheses.json) C方向。[IND-028](../config/indicators.json) high/rising強化。フロンティア差別化残存 | A-3 | [INFO-068](../Information/2026-07-11/collected-raw.md#INFO-068) |
| 高 | Q2収益$10.9B・年率$43.6Bペース: 収益加速確認。但しセグメント内訳19R不在 | [H-OAI-001](../config/hypotheses.json) C方向（量的）だが質的評価不能。KIQ-OAI-001 19R不在 | B-3 | [INFO-058](../Information/2026-07-11/collected-raw.md#INFO-058) |
| 高 | ChatGPT 1Bユーザー到達: コンシューマー規模史上最大 | [H-OAI-001](../config/hypotheses.json) C方向（間接）。プラットフォーム規模の優位性 | B-2 | [INFO-053](../Information/2026-07-11/collected-raw.md#INFO-053) |
| 高 | GPT-5.6価格体系: Sol $5/$15・Terra $2.50/$10・Luna $1/$4。Luna $1/M inputでDeepSeek V4 Pro $1.74に接近 | [H-OAI-001](../config/hypotheses.json) I方向。価格競争参加・コモディティ化圧力。差別化と価格競争の二層構造 | B-2 | [INFO-045](../Information/2026-07-11/collected-raw.md#INFO-045) |
| 高 | SkillCloak: OpenAI Skills全静的スキャナ突破・ポリモーフィック難読化100%検出回避・7/23 Enterprise デフォルト有効化 | [IND-013](../config/indicators.json) high/rising強化。エージェントプラットフォームセキュリティリスク具体化。critical未到達 | B-2 | [INFO-026](../Information/2026-07-11/collected-raw.md#INFO-026) |
| 高 | API価格崩壊: トークン指数高値から約20%下落・DeepSeek V4 Pro $1.74/M | [H-OAI-001](../config/hypotheses.json) I方向。コモディティ化の経済的次元深化 | A-2 | [INFO-052](../Information/2026-07-11/collected-raw.md#INFO-052) |
| 中 | GPT-Live音声モード: リアルタイム双方向音声対話・電話発着信機能 | [H-OAI-001](../config/hypotheses.json) C方向（コンシューマー）。マルチモーダル拡張 | A-3 | [INFO-005](../Information/2026-07-11/collected-raw.md#INFO-005) |
| 中 | Microsoft所有比率約27%（評価額$135B）・PBC移行完了 | [H-OAI-001](../config/hypotheses.json) 企業構造確定。Microsoft依存関係の定量化 | B-3 | [INFO-011](../Information/2026-07-10/collected-raw.md#INFO-011) |
| 中 | OpenAI Agents SDK: プロバイダー非依存（AWS Bedrock対応） | [H-OAI-002](../config/hypotheses.json) 囲い込み否定累積。排他性なし | A-3 | [INFO-015](../Information/2026-07-11/collected-raw.md#INFO-015) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-OAI-001](../config/hypotheses.json) が45%を割る | 「B2B支配的地位確立」仮説が棄却水準に接近。medium→low帯移行 | 180日 | [H-OAI-001](../config/hypotheses.json) |
| KIQ-OAI-001が回答されAPI/Enterprise/Consumer収益内訳が公表される | 49%の凍結が解消し、B2B支配の収益的裏付けの質的評価が可能になる | 90日 | [IND-027](../config/indicators.json) |
| 企業AI採用率39.5%が更に低下し、35%を下回る | 「支配」の定義が成立しなくなる。Anthropic 41%との差が構造化する | 180日 | [IND-008](../config/indicators.json) |
| OSSモデルのエンタープライズ採用シェアが10%を超える | 「勝者集中」前提が崩れ、SCN-004が上昇する。H-OAI-001のI方向確定 | 90日 | [IND-027](../config/indicators.json) |
| API価格下落トレンドが反転しフロンティア価格が上昇に転じる | コモディティ化の不可逆的加速判断が崩れる | 180日 | [IND-025](../config/indicators.json) |
| SkillCloak系マルウェアによる実被害（A-2品質）が報告される | IND-013がcriticalに移行し、エージェントプラットフォーム信頼性が構造的課題化する | 90日 | [IND-013](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 49% medium | ±0%（5R連続±0%）。核心パラメータ不在（KIQ-OAI-001 19R）による確度変更保留。GPT-5.6 M365 Copilot優先モデル選定（INFO-065 A-3）・RSI 57.9%（INFO-068 A-3）・Q2収益$10.9B（INFO-058 B-3）・ChatGPT 1Bユーザー（INFO-053 B-2）=C方向。GPT-5.6 Luna $1/M input（INFO-045 B-2）・API価格崩壊・SkillCloak（INFO-026 B-2）=I方向。C/I均衡構造不変。medium維持 | [INFO-065](../Information/2026-07-11/collected-raw.md#INFO-065) [INFO-068](../Information/2026-07-11/collected-raw.md#INFO-068) [INFO-058](../Information/2026-07-11/collected-raw.md#INFO-058) | [INFO-045](../Information/2026-07-11/collected-raw.md#INFO-045) [INFO-026](../Information/2026-07-11/collected-raw.md#INFO-026) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放の上にプロプライエタリ上位レイヤーで囲い込む | 44% low | ±0%。囲い込み否定累積継続。Agent SDKプロバイダー非依存（INFO-015 A-3）・Microsoft Foundry→M365 Copilot移行（INFO-029 A-3）・排他性なし。low帯確定度増加 | (新規囲い込み肯定Cなし) | [INFO-015](../Information/2026-07-11/collected-raw.md#INFO-015) [INFO-029](../Information/2026-07-11/collected-raw.md#INFO-029) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% low | ±0%。商業化規模（Q2収益$10.9B・ChatGPT 1Bユーザー・IPO準備・PBC移行）圧倒的。G7でAltman自身の在任中AGI到達可能と主張だが、行動は商業化優先。AGI最優先支持A-2+証拠不在 | (該当なし) | [INFO-058](../Information/2026-07-11/collected-raw.md#INFO-058) [INFO-053](../Information/2026-07-11/collected-raw.md#INFO-053) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントでcritical | SkillCloak全静的スキャナ突破（INFO-026 B-2）・Friendly Fire防御型AIハイジャック（INFO-027 B-2）・Claude Code CLI RCE PoC（INFO-069 B-2）・OpenAI Skills 7/23 Enterpriseデフォルト有効化（INFO-026）。攻撃面拡大継続。critical移行条件（実被害A-2報告）未到達。構造的バイアス記録: 実被害A-2報告の不在≠実被害の不在。high/rising | 2026-07-11 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | GPT-5.6 Sol ARC-AGI-3 7.8%・RSI 57.9%（+16.2pt）・内部推論計算100倍（INFO-068 A-3）・MMLU全社>90%飽和・GLM-5.2 OSS#1全体4位・GPT-5.6 Luna $1/M input（INFO-045 B-2）。コモディティ化圧力と差別化の二層構造継続。elevated/stable | 2026-07-11 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | 米国企業AI採用率4%（FRB・INFO-020 B-3）・EU 4.03%（Eurostat）・88%パイロット停滞・97%コミット/18%デプロイ・Gartner 40%+プロジェクト廃棄予測（INFO-060 B-2）・McKinsey「悪いプロセスを増幅」（INFO-070 B-2）。期待-実態ギャップ更に強化（15+独立ソース）。high/rising | 2026-07-11 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | MCP 2026 RCステートレスコア（INFO-024 B-2）・AAIF/Linux Foundation寄贈（INFO-025 B-2）・OpenAI Agents SDK provider-agnostic（INFO-015 A-3）・MS Foundry→M365 Copilot（INFO-029 A-3）・Google Gemini Enterprise Agent Platform（INFO-030 A-3）・MCP/A2A切り替えコスト19-34%削減（INFO-048 B-3）。標準化加速と囲い込み否定の同時進行。high/rising | 2026-07-11 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | RSI Index 57.9%（+16.2pt）・内部推論計算100倍・エージェント的トークン22倍（INFO-068 A-3）・DeepMind論文AGI 2030年警告（INFO-052 B-2）・UN独立科学パネル予備報告（INFO-080 A-1）・AGI定義コンセンサス不在。RSI具体化と客観ベンチマーク限界の同時進行。high/rising | 2026-07-11 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | ビッグテック4社CapEx $725B（INFO-047 B-2）・$130B+ AI DCブロック/遅延（INFO-047）・Anthropic-SpaceX Colossus 1全容量300MW+/220K GPU（INFO-001 A-3）。資本流入加速・物理的制約ギャップ確定的。high/rising | 2026-07-11 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。SCR指定因果関係公式明文化（INFO-032 A-2）・国連事務総長LAWS禁止宣言（INFO-034 A-2）・完全自律AIドローン人間殺害初確認・Epistemic Delegation（INFO-039 B-3）・ウォーレン開示要求（INFO-033 A-2）・EO 14409+FTC AI正確性規制（INFO-023 A-2）。KIQ-MIL-001 19R不在。条件2充実史上最大水準 | 2026-07-11 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-11 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% medium ±0%（核心パラメータ不在19R）。GPT-5.6 M365 Copilot優先モデル選定（INFO-065 A-3）・RSI 57.9%（+16.2pt・INFO-068 A-3）・Q2収益$10.9B（INFO-058 B-3）・ChatGPT 1Bユーザー（INFO-053 B-2）・GPT-5.6三段階価格体系（INFO-045 B-2）・GPT-Live音声モード（INFO-005 A-3）・SkillCloak（INFO-026 B-2）を新規反映。KIQ-OAI-001 19R・KIQ-MIL-001 19R。Arbiter v4.32 COMPLETE | [INFO-065](../Information/2026-07-11/collected-raw.md#INFO-065) [INFO-068](../Information/2026-07-11/collected-raw.md#INFO-068) [INFO-058](../Information/2026-07-11/collected-raw.md#INFO-058) | H-OAI-001 49%（±0%） |
| 2026-07-10 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% medium ±0%（核心パラメータ不在18R）。GPT-5.6（Sol/Terra/Luna）GA・ARC-AGI-3 7.8%（INFO-093 A-2）・ChatGPT Work Agent（INFO-010 B-2）・Multi-agent API・企業AI採用率39.5%横ばい（INFO-064 B-3）・Microsoft 27%所有（INFO-011 B-3）・API価格崩壊（INFO-052 A-2）を反映。Arbiter v4.31 COMPLETE | [INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) [INFO-010](../Information/2026-07-10/collected-raw.md#INFO-010) [INFO-064](../Information/2026-07-10/collected-raw.md#INFO-064) | H-OAI-001 49%（±0%） |
| 2026-07-03 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% medium ±0%。根拠を「C/I均衡」から「核心パラメータ不在による確度変更保留」に修正 | [INFO-051](../Information/2026-07-03/collected-raw.md#INFO-051) | H-OAI-001 48→49%（v4.24）・根拠修正 |
| 2026-06-29 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 48% ±0% | [INFO-043](../Information/2026-06-29/collected-raw.md#INFO-043) | H-OAI-001 48%（±0%） |
| 2026-06-27 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49→48% | [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) | H-OAI-001 49→48% |

## 7. ブラインドスポット

- 収益内訳（API/Enterprise/Consumer・政府vs民間）が非公開（KIQ-OAI-001 19R連続不在）。Q2収益$10.9Bの成長は確認できるが、セグメント別寄与が判明しない限り49%の確度変更は根拠不足。情報不足を認めることと同義の状態が19R連続で継続している。
- RSI Index 57.9%（+16.2pt）は推論スケーリングの産業定量化として初の事例だが、この指標がB2B市場での支配にどう直結するかの因果チェーンが不明。技術的性能向上とエンタープライズ採用率横ばい（39.5%）の乖離が継続する。
- GPT-5.6 M365 Copilot優先モデル選定は強力なC証拠だが、Microsoft依存関係の深化を意味する。Microsoft所有比率27%が確定済みの状況で、M365 Copilot統合は独立性強化と依存関係深化の二面性を持つ。
- $13.5B純損失（H1 2025）とQ2収益$10.9Bの乖離がいつ解消するか不明。収益成長が赤字構造を改善しているか、規模拡大で赤字が増幅しているかの判別が不能。
- GPT-5.6の三段階価格体系は、Sol $5/$15で差別化を維持しつつLuna $1/$4で価格競争に参加する二層構造を示す。この戦略がH-OAI-001のC/Iどちらに効くかは、エンタープライズ顧客がどのティアを選択するかに依存するが、そのデータが不在。
- SkillCloakがOpenAI Skillsの全静的スキャナを突破した。7/23 Enterpriseデフォルト有効化前に実被害（A-2品質）が報告された場合、IND-013がcriticalに移行し、エージェントプラットフォーム信頼性が構造的課題化する。
- G7でAltmanが自身の在任中AGI到達可能と主張したが、行動はQ2収益$10.9B・ChatGPT 1Bユーザー・GPT-Live・PBC移行・IPO準備と商業化一辺倒。発言と行動の乖離をどう評価するかの基準が不在。H-OAI-003 3%の妥当性は揺るがない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-005](../Information/2026-07-11/collected-raw.md#INFO-005) | GPT-Live: リアルタイム双方向音声対話・電話発着信機能(A-3) |
| [INFO-015](../Information/2026-07-11/collected-raw.md#INFO-015) | OpenAI Agents SDK: プロバイダー非依存・AWS Bedrock対応・MCP/A2A(A-3) |
| [INFO-026](../Information/2026-07-11/collected-raw.md#INFO-026) | SkillCloak: OpenAI Skills全静的スキャナ突破・ポリモーフィック難読化100%回避・7/23 Enterprise デフォルト有効化(B-2) |
| [INFO-027](../Information/2026-07-11/collected-raw.md#INFO-027) | Friendly Fire: 防御型AIハイジャック・LLM統合アプリ80%対象(B-2) |
| [INFO-029](../Information/2026-07-11/collected-raw.md#INFO-029) | Microsoft Foundry→M365 Copilotリブランド・エージェント的AIプラットフォーム(A-3) |
| [INFO-033](../Information/2026-07-11/collected-raw.md#INFO-033) | ウォーレン上院議員: 7社AI契約開示要求・政府vs民間セグメント不透明(A-2) |
| [INFO-045](../Information/2026-07-11/collected-raw.md#INFO-045) | GPT-5.6三段階価格体系: Sol $5/$15・Terra $2.50/$10・Luna $1/$4 per M token(B-2) |
| [INFO-047](../Information/2026-07-11/collected-raw.md#INFO-047) | $130B+ AI DCブロック/遅延・ビッグテック4社CapEx $725B(B-2) |
| [INFO-053](../Information/2026-07-11/collected-raw.md#INFO-053) | ChatGPT 1Bユーザー到達(B-2) |
| [INFO-058](../Information/2026-07-11/collected-raw.md#INFO-058) | OpenAI Q2 2026収益$10.9B・年率$43.6Bペース(B-3) |
| [INFO-065](../Information/2026-07-11/collected-raw.md#INFO-065) | GPT-5.6 M365 Copilot優先モデル選定・エンタープライズデプロイ規模(A-3) |
| [INFO-068](../Information/2026-07-11/collected-raw.md#INFO-068) | RSI Index 57.9%（+16.2pt）・内部推論計算100倍・エージェント的トークン22倍(A-3) |
| [INFO-011](../Information/2026-07-10/collected-raw.md#INFO-011) | Microsoft所有比率約27%・評価額$135B・PBC移行完了(B-3) |
| [INFO-093](../Information/2026-07-10/collected-raw.md#INFO-093) | GPT-5.6（Sol/Terra/Luna）GA: ARC-AGI-3 7.8%・Terminal-Bench 91.9%(A-2) |
| [Arbiter v4.32](../state/arbiter-2026-07-11.md) | 確度評価の完全根拠 |
