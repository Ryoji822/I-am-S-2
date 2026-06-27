# OpenAI

> 最終判断更新: 2026-06-27
> 全体確信度: 中低
> 主参照: [H-OAI-001](../config/hypotheses.json) [H-OAI-002](../config/hypotheses.json) [H-OAI-003](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-OAI-001](../config/hypotheses.json) は48%（medium）で-1%。v4.15で一時停止したペナルティ機構を再開した。再開条件「新たなB2B直接不一致証拠の発見」が充足されたためである。企業LLM支出に占めるOpenAIのシェアが2023年の50%から27%に低下し [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008)（B-3）、Anthropicが40%・Googleが21%に拡大した。同時にエンタープライズ顧客がコスト膨張からOpenAIを離れ、安価な代替への切替を開始している [INFO-027](../Information/2026-06-27/collected-raw.md#INFO-027)（B-3）。これらはB2B市場での支配的地位の構造的侵食を直接的に示す。

OpenAIの絶対的成長は依然として強力である。GPT-5.6 SolがTerminal-Bench 2.1で新SOTAを記録し [INFO-002](../Information/2026-06-27/collected-raw.md#INFO-002)（A-3）、Jalapeño推論チップがBroadcomとの協業でLLM推論専用の完全白紙設計を実現した [INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001)（A-3）。月収益$2B（年率$25B超）・企業収益が全体の40%超・Codex週次500万ユーザー [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008)。フルスタック戦略は差別化要因の維持を示す。但しSora事業が「財政的持続不可能」を理由に撤退し [INFO-046](../Information/2026-06-27/collected-raw.md#INFO-046)（B-2）、製品ポートフォリオの限界が露呈した。IPOは評価額維持のため2027年へ延期し [INFO-042](../Information/2026-06-27/collected-raw.md#INFO-042)（A-2）、評価額$852B・収益~$13B・純損失$21Bの財務構造が明らかになった。

[IND-030](../config/indicators.json) はcriticalを維持。Pentagonが標的選定ドクトリンを改訂しAIが軍事標的設定に広く関与する道を開放した [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018)（A-2）。OpenAIはPentagonと機密環境向けAI配備契約を締結し、White HouseがGPT-5.6ロールアウト遅延を要請した [INFO-002](../Information/2026-06-27/collected-raw.md#INFO-002)。順応報酬構造への参加が確定した。企業支出シェアが20%を下回るか、API収益がEnterprise収益を下回り差が拡大すれば判断が変わる。

## 1. コア判断

[H-OAI-001](../config/hypotheses.json) は48%（medium）で-1%。v4.15で一時停止したペナルティ機構を再開した。本ラウンドの確度変更は、v4.15が設定した「ペナルティ再開には新たなB2B直接不一致証拠が必要」という条件を充足した。

企業LLM支出シェア（Menlo Ventures調べ）でOpenAIのシェアが2023年の50%から27%に低下した [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008)（B-3）。Anthropicが40%・Googleが21%に拡大する中、OpenAIの企業市場での相対的地位の後退が定量化された。同時にエンタープライズ顧客がコスト膨張からOpenAIやAnthropicを離れ、安価なモデルへの切替を始めている [INFO-027](../Information/2026-06-27/collected-raw.md#INFO-027)（B-3）。API非互換性（OpenAIのfunction callingがAnthropicと挙動が異なる）で技術的ロックインは存在するが、オープン標準の代替が利用可能になりつつある。これらはB2B支配的地位の侵食を直接的に示す証拠であり、ペナルティ再開の条件を満たす。両証拠ともB-3品質であり、-2%の変更は過大である。DEGRADED制約で確度変更を±1%に制限したため、-1%を適用した。

OpenAIの絶対的成長は依然として強力である。月収益$2B（年率$25B超）・企業収益が全体の40%超・Codex週次500万ユーザー・ChatGPT 9億WAU [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008)。GPT-5.6 SolはTerminal-Bench 2.1で新SOTAを記録し [INFO-002](../Information/2026-06-27/collected-raw.md#INFO-002)、JalapeñoチップはBroadcomとの協業でLLM推論専用の完全白紙設計を実現した [INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001)。OpenAIモデル自身がチップ設計プロセスを加速させるAIによるAIインフラ改善ループも報告されている。フルスタック戦略（モデルから製品、インフラまで自前化）は差別化の維持を示す。これらの成長証拠は相対的地位の後退と同時に観測されており、市場全体の拡大速度がOpenAIのシェア低下を上回る構造が継続している。

Sora事業の撤退は [INFO-046](../Information/2026-06-27/collected-raw.md#INFO-046)（B-2）、OpenAIの製品ポートフォリオが全領域で支配的でないことを示す。「財政的持続不可能」を理由とした動画生成モデルの廃止は、Alibaba動画AIの全球2位浮上と同時に起きた。技術的評価は高かったが商業化に失敗した。IPOは評価額維持のため2027年への延期を検討しており [INFO-042](../Information/2026-06-27/collected-raw.md#INFO-042)（A-2）、SpaceX上場の低迷が慎重姿勢に影響している。評価額$852B・年収~$13B・純損失$21Bの財務構造は、成長と赤字が同時に存在することを示す。

[H-OAI-002](../config/hypotheses.json) は44%（low）。围い込み否定証拠の累積は継続している。Agent SDKはプロバイダ非依存で30以上のモデルをサポートし [INFO-009](../Information/2026-06-27/collected-raw.md#INFO-009)（B-3）、排他性の言及はない。Jalapeñoチップは推論経済ロックインの新たな層を形成する可能性があるが、現時点ではインフラ層での自前化であり、顧客の围い込みとは異なる。[H-OAI-003](../config/hypotheses.json) は3%（low）。IPO延期・Codex週次500万・月収益$2B等の商業化規模の圧倒的証拠が継続し、AGI最優先を支持するA-2以上の証拠は不在。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | 企業LLM支出シェアOpenAI 27%（2023年50%→27%）・Anthropic 40%・Google 21% | [H-OAI-001](../config/hypotheses.json) I方向。B2B支配的地位の構造的侵食の定量化。ペナルティ再開の直接根拠 | B-3 | [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) |
| 高 | GPT-5.6 Sol新SOTA（Terminal-Bench 2.1）・White Houseが段階的ロールアウト要請 | [H-OAI-001](../config/hypotheses.json) C方向。技術優位の継続・政府配備契約の確定 | A-3 | [INFO-002](../Information/2026-06-27/collected-raw.md#INFO-002) |
| 高 | Jalapeño推論チップ（Broadcom協業・完全白紙設計）・AI自身が設計加速 | [H-OAI-001](../config/hypotheses.json) C方向。フルスタック戦略・推論経済の自前化 | A-3 | [INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001) |
| 高 | Sora事業撤退（財政的持続不可能）・Alibaba動画AI全球2位浮上 | [H-OAI-001](../config/hypotheses.json) I方向。製品ポートフォリオの限界・コモディティ化圧力 | B-2 | [INFO-046](../Information/2026-06-27/collected-raw.md#INFO-046) |
| 高 | IPO延期2027・評価額$852B・収益~$13B・純損失$21B | [H-OAI-001](../config/hypotheses.json) 二面性。構造的成長の継続だが評価額下方修正・赤字構造露呈 | A-2 | [INFO-042](../Information/2026-06-27/collected-raw.md#INFO-042) |
| 高 | Pentagon標的選定ドクトリン改訂・OpenAI機密環境AI配備契約 | [H-OAI-001](../config/hypotheses.json) C方向（政府系B2B）。順応報酬構造参加確定。[IND-030](../config/indicators.json) critical文脈 | A-2 | [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) |
| 高 | エンタープライズ顧客のコスト離れ・安価なモデルへの切替開始 | [H-OAI-001](../config/hypotheses.json) I方向。B2B直接証拠・ペナルティ再開条件充足 | B-3 | [INFO-027](../Information/2026-06-27/collected-raw.md#INFO-027) |
| 中 | Agent SDK プロバイダ非依存・30以上のモデルサポート・排他性なし | [H-OAI-002](../config/hypotheses.json) 围い込み否定。[H-OAI-001](../config/hypotheses.json) I方向（囲い込み戦略不在） | B-3 | [INFO-009](../Information/2026-06-27/collected-raw.md#INFO-009) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-OAI-001](../config/hypotheses.json) が45%を割る | 「B2B支配的地位確立」仮説が棄却水準に接近する。medium→low帯移行 | 180日 | [H-OAI-001](../config/hypotheses.json) |
| 企業LLM支出シェアが20%を下回る | 「支配」の定義自体が成立しなくなる。27%から更に低下で構造的劣位確定 | 180日 | [IND-027](../config/indicators.json) |
| OpenAI収益内訳でAPI収益がEnterprise収益を下回り差が拡大する | 「B2B支配」の収益的裏付けが変質する | 90日 | [IND-027](../config/indicators.json) |
| Sora撤退に続きCodexまたはEnterprise製品の撤退・統合が発生する | 製品ポートフォリオの構造的弱さが確定する | 180日 | [IND-025](../config/indicators.json) |
| Pentagon契約が延期または取消となる | 政府系B2Bチャネル獲得の因果チェーンが崩れる | 365日 | [IND-030](../config/indicators.json) |
| IPOが更に延期または評価額が$500Bを下回る | 構造的成長の外部検証が失敗する | 365日 | [IND-029](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | Agent機能でB2B支配的地位を確立する | 48% medium | -1%。ペナルティ機構再開。v4.15条件充足。企業LLM支出シェア27%(INFO-008 B-3)・エンタープライズ顧客コスト離れ(INFO-027 B-3)がB2B直接I証拠。GPT-5.6 Sol(INFO-002 A-3)・Jalapeño(INFO-001 A-3)・Pentagon契約(INFO-018 A-2)がC方向。DEGRADED ±1%制約。48%はmedium帯下限 | [INFO-002](../Information/2026-06-27/collected-raw.md#INFO-002) [INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001) [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) | [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) [INFO-027](../Information/2026-06-27/collected-raw.md#INFO-027) [INFO-046](../Information/2026-06-27/collected-raw.md#INFO-046) [INFO-042](../Information/2026-06-27/collected-raw.md#INFO-042) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放の上にプロプライエタリ上位レイヤーで围い込む | 44% low | 围い込み否定累積継続。Agent SDK プロバイダ非依存(INFO-009 B-3)・30以上モデルサポート・排他性なし。Jalapeñoはインフラ自前化であり顧客围い込みとは異なる。low帯確定度増加 | (新規围い込み肯定Cなし) | [INFO-009](../Information/2026-06-27/collected-raw.md#INFO-009) [INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とする | 3% low | 商業化規模（月収益$2B・Codex 500万・IPO準備）圧倒的。Phase 3宣言はAGI研究自動化を含むが3目標中2つは商業ロードマップ。AGI最優先A-2+証拠不在 | [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) [INFO-042](../Information/2026-06-27/collected-raw.md#INFO-042) [INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントでcritical | 新規A-2実被害なし。high/rising維持 | 2026-06-27 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・性能コモディティ化 | 性能差ベンダー間5%未満でhigh | GPT-5.6 Sol新SOTA・Sora撤退（コモディティ化）・Alibaba動画AI全球2位。性能差は縮小傾向だが一部領域でSOTA更新。elevated/stable | 2026-06-27 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | 期待-実態ギャップ構造的継続。high/rising | 2026-06-27 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | Agent SDK プロバイダ非依存・30以上モデルサポート。標準化加速・围い込み同時進行。high/rising | 2026-06-27 |
| [IND-028](../config/indicators.json) | AGI到達度（客観ベンチマーク vs 主観宣言） | 主観-客観乖離拡大でhigh | GPT-5.6 Sol新SOTA・ARC-AGI-2 Seed 2.1 Pro 0.625。RSI具体化と客観ベンチマーク限界同時進行。high/rising | 2026-06-27 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | $725B資本支出予測・ByteDance $20B融資・Jalapeño推論チップ。資本流入加速・物理的制約ギャップ確定的。high/rising | 2026-06-27 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。Pentagon標的選定ドクトリン改訂・OpenAI機密環境AI配備契約・White House GPT-5.6遅延要請。軍事AIが個別実験から構造的実践に相転移 | 2026-06-27 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-27 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49→48%（-1%・ペナルティ機構再開）。企業LLM支出シェア27%（[INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) B-3）・GPT-5.6 Sol新SOTA（[INFO-002](../Information/2026-06-27/collected-raw.md#INFO-002) A-3）・Jalapeñoチップ（[INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001) A-3）・Sora撤退（[INFO-046](../Information/2026-06-27/collected-raw.md#INFO-046) B-2）・IPO延期2027（[INFO-042](../Information/2026-06-27/collected-raw.md#INFO-042) A-2）を反映 | [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) [INFO-002](../Information/2026-06-27/collected-raw.md#INFO-002) [INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001) [INFO-046](../Information/2026-06-27/collected-raw.md#INFO-046) [INFO-042](../Information/2026-06-27/collected-raw.md#INFO-042) | H-OAI-001 49→48%（ペナルティ再開）・H-OAI-002 44%維持・H-OAI-003 3%維持・IND-030 critical維持 |
| 2026-06-21 | 全面書き直し。[H-OAI-001](../config/hypotheses.json) 49% ±0%（ペナルティ機構一時停止）。Q1収益$5.7B 3倍成長・IPO $1T・ChatGPT 50%割れを反映。[IND-030](../config/indicators.json) high→critical | [INFO-045](../Information/2026-06-21/collected-raw.md#INFO-045) [INFO-050](../Information/2026-06-21/collected-raw.md#INFO-050) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | H-OAI-001 49%（±0%・ペナルティ停止）・H-OAI-002 44%維持・H-OAI-003 3%維持・IND-030 critical |
| 2026-06-19 | §0〜§5全面書き直し。Anthropic ARR逆転・Jevons paradox・Pentagon GenAI.mil・Claude Code採用24%を反映 | 2026-06-19複数INFO | H-OAI-001 51→50% |
| 2026-06-12 | §0-§2・§4・§5全面書き直し。S-1提出・Phase 3宣言・Ona買収・価格引き下げ検討を反映 | 2026-06-12複数INFO | H-OAI-001 58→56% |
| 2026-06-01 | Anthropic逆転3重確認+Codex Tax Agent+Rosalind+Frontier Governance+SKILL.mdを反映して全面書き直し | 2026-06-01複数INFO | H-OAI-001 60→58% |

## 7. ブラインドスポット

- 企業LLM支出シェア27%がMenlo Venturesの単一ソースである。他ソースでの追認が必要。27%という数値が一時的か構造的かの判別も不能。
- ペナルティ再開後のH-OAI-001 48%が適正水準かの検証手段がない。B-3品質証拠による-1%はDEGRADED制約の産物であり、COMPLETE状態であれば-2%が適用された可能性がある。
- OpenAIの月収益$2B（年率$25B超）とIPO資料の収益~$13Bの乖離。異なる会計基準・時点・定義の可能性があるが、真の成長率の判別が不能。
- Sora撤退が動画生成に特化した事象か、より広範な製品戦略の限界を示すシグナルかの判別ができない。CodexやEnterprise製品への波及可能性が不明。
- Jalapeñoチップが推論経済のロックイン層を形成するか、汎用GPUエコシステムとの互換性維持にとどまるかの判別ができない。Broadcomとの協業長期安定性も不明。
- Pentagon機密環境AI配備契約の実効性・収益寄与・政府要件変更可能性が不明。White HouseのGPT-5.6遅延要請が技術的懸念か政治的交渉材料かの判別も不能。
- IPO延期2027が評価額維持のための戦略的選択か、市場環境悪化による強制かの判別ができない。$852B評価額と$21B純損失の乖離が持続可能か不明。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) | OpenAI 9億WAU・月収益$2B・企業40%+・企業LLM支出シェア27%（2023年50%→）(B-3) |
| [INFO-002](../Information/2026-06-27/collected-raw.md#INFO-002) | GPT-5.6 Sol新SOTA・White House段階的ロールアウト要請(A-3) |
| [INFO-001](../Information/2026-06-27/collected-raw.md#INFO-001) | Jalapeño推論チップ・Broadcom協業・完全白紙設計(A-3) |
| [INFO-046](../Information/2026-06-27/collected-raw.md#INFO-046) | Sora事業撤退・財政的持続不可能(B-2) |
| [INFO-042](../Information/2026-06-27/collected-raw.md#INFO-042) | IPO延期2027・評価額$852B・収益~$13B・純損失$21B(A-2) |
| [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) | Pentagon標的選定ドクトリン改訂・OpenAI機密環境AI配備契約(A-2) |
| [INFO-027](../Information/2026-06-27/collected-raw.md#INFO-027) | エンタープライズ顧客コスト離れ・安価なモデルへの切替(B-3) |
| [INFO-009](../Information/2026-06-27/collected-raw.md#INFO-009) | Agent SDK プロバイダ非依存・30以上モデルサポート(B-3) |
| [Arbiter v4.21](../state/arbiter-2026-06-27.md) | ペナルティ機構再開・DEGRADED制約±1% |
| [INFO-045](../Information/2026-06-21/collected-raw.md#INFO-045) | OpenAI Q1 2026収益$5.7B 3倍成長・エンタープライズ40%+(C-2) |
| [INFO-050](../Information/2026-06-21/collected-raw.md#INFO-050) | OpenAI IPO秘密提出・評価額最大$1T(B-2) |
| [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | ChatGPT市場シェア初の50%割れ(A-1) |
| [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) | Grok Gov Model Operation Epic Fury 96h/2,000標的(A-2) |
| [INFO-010](../Information/2026-06-19/collected-raw.md#INFO-010) | Pentagon GenAI.mil 300万人・順応報酬構造参加(C-3) |
| [INFO-004](../Information/2026-06-12/collected-raw.md#INFO-004) | OpenAI Phase 3宣言・2028年3月AI研究自動化目標(A-3) |
