# Google / DeepMind

> 最終判断更新: 2026-07-10
> 全体確信度: 低
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。KIQ-GOO-001がGCP +63% vs Azure +40% vs AWS +28%で初充足されたが、B-2品質かつ低ベース効果（GCPシェア14% vs AWS 28%）の排除が未解決。围い込みI 33件の品質別内訳未開示。Gemini Enterprise Agent PlatformのSkill Registry/RAG Engine/ADKが新規追加。Gemini 3.5 Flashのコンピュータ使用がGoogle自家測定。Google固有定量データ不在継続。Arbiter v4.31 COMPLETE
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-001](../config/indicators.json) [IND-006](../config/indicators.json) [IND-025](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

GoogleがGemini APIのManaged Agents機能を拡張し、Gemini Enterprise Agent PlatformでSkill Registry（セキュアなスキル管理・発見リポジトリ）、RAG Engine、Agent Development Kit（ADK）を提供開始した（[INFO-014](../Information/2026-07-10/collected-raw.md#INFO-014) A-3・[INFO-036](../Information/2026-07-10/collected-raw.md#INFO-036) A-3）。バックグラウンド非同期実行、リモートMCPサーバー接続、カスタム関数をサポートし、単一エンドポイントで推論・コード実行・パッケージインストール・ファイル管理を処理する。これらはエージェント実行層とエンタープライズ基盤層でのプラットフォーム深化を示す。[H-GOO-001](../config/hypotheses.json) は50% lowで±0%。Google固有定量データ不在が継続。もしWorkspace内GeminiのDAU/MAUが3四半期連続で頭打ちを示すか、围い込み証拠が35件を超えれば、コア判断が変わる。

## 1. コア判断

GoogleのGeminiプラットフォーム戦略がエンタープライズ基盤層で更に深化した。Gemini Enterprise Agent PlatformがSkill Registry（セキュア・低レイテンシのスキル管理・発見リポジトリ）、RAG Engine内蔵、Agent Development Kit（Python開発環境）を提供する（[INFO-036](../Information/2026-07-10/collected-raw.md#INFO-036) A-3）。Agent Builder + Agent Engine + Vertex AI統合により、エンタープライズ向けエージェントのビルドからガバナンスまでを統合プラットフォームで提供する。

Managed Agents機能の拡張では、バックグラウンド非同期実行、リモートMCPサーバー接続、カスタム関数がサポートされた（[INFO-014](../Information/2026-07-10/collected-raw.md#INFO-014) A-3）。単一エンドポイントAPIで推論・コード実行・パッケージインストール・ファイル管理を統合処理する。これらは[H-GOO-001](../config/hypotheses.json)のC蓄積（エコシステム統合の証拠）に加わる。

low維持の理由は3点変わらない。第一に、Arbiter v4.13が設定した条件（コアエンタープライズAI定量データA-2+）が未達成。第二に、利用可能な最高品質がB-2（Forrester逆転・GCP成長率）であり、A-2+でない。第三に、GCP +63% YoYの低ベース効果（GCPシェア14% vs AWS 28%）の排除が未解決。Gemini Enterprise Agent PlatformのSkill Registry/RAG Engine/ADKはA-3品質の製品証拠であり、C蓄積の幅を拡げたが、コアエンタープライズAI領域での定量採用データ（シェア・収益・利用率）ではない。

G7サミットでHassabisとAmodeiが米国主導の国際AI連合を共同提案した（[INFO-075](../Information/2026-07-10/collected-raw.md#INFO-075) B-2）。Amodeiの2023年予測（2-3年以内にAIが人間の主要機能を実行）は「よく当たった」と評価された。強いAGIは2031-2035頃とされている。国連の新独立国際科学AIパネル（40人会員）が7月1日に発足し、暫定科学評価報告書を発表した（[INFO-090](../Information/2026-07-10/collected-raw.md#INFO-090) B-3）。AGI定義の合意は依然不在（[INFO-076](../Information/2026-07-10/collected-raw.md#INFO-076) B-2）。

[H-GOO-002](../config/hypotheses.json) は23% lowで±0%。围い込みI 33件の蓄積に新規追加の品質判別はできていない。開放証拠（Interactions API GA・Agent Skills標準・MCP RC）の蓄積は継続するが、围い込み蓄積速度を上回る決定的証拠はない。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Gemini Enterprise Agent Platform: Skill Registry・RAG Engine・ADK・Agent Builder+Agent Engine+Vertex AI統合 | [H-GOO-001](../config/hypotheses.json) エンタープライズ基盤深化（C方向）。[H-GOO-002](../config/hypotheses.json) プラットフォーム固有化の側面 | A-3 | [INFO-036](../Information/2026-07-10/collected-raw.md#INFO-036) |
| 高 | Managed Agents機能拡張: バックグラウンド非同期実行・リモートMCPサーバー接続・カスタム関数 | [H-GOO-001](../config/hypotheses.json) エージェント実行層深化（C方向）。単一エンドポイント統合 | A-3 | [INFO-014](../Information/2026-07-10/collected-raw.md#INFO-014) |
| 高 | G7: Hassabis+Amodei米国主導国際AI連合共同提案・強いAGI 2031-2035 | [H-GOO-003](../config/hypotheses.json) 戦略的地位強化（C方向）。DeepMindリーダーの国際舞台での存在感 | B-2 | [INFO-075](../Information/2026-07-10/collected-raw.md#INFO-075) |
| 高 | GCP +63% YoY（15Q最高）vs Azure +40% vs AWS +28%。市場シェア: AWS 28% / Azure 21% / GCP 14% | [H-GOO-001](../config/hypotheses.json) KIQ-GOO-001初充足。19R代替説明への初の定量的反証。但しB-2品質・低ベース効果 | B-2 | 前回確認（2026-06-16 INFO-055） |
| 高 | Google最大$40B Anthropic投資 | [H-GOO-001](../config/hypotheses.json) C蓄積。戦略的意図（インフラ依存・影響力・OpenAI対策）は未確定 | B-2 | 前回確認（2026-06-23 INFO-045） |
| 高 | Gemini 3.5 Flashコンピュータ使用: ブラウザ・モバイル・デスクトップでエージェント構築 | [H-GOO-001](../config/hypotheses.json) エコシステム統合（C方向）。但し自家測定・独立検証未完了 | A-3 | 前回確認（2026-06-28 INFO-022） |
| 中 | Forrester「Google > OpenAI」代理店優先パートナー逆転 | [H-GOO-001](../config/hypotheses.json) C蓄積。但し広告領域のみ部分充足 | B-2 | 前回確認（2026-06-23 INFO-037） |
| 中 | DeepMind「AI Control Roadmap」: 高度AIエージェントを「内部脅威」と扱う | [H-GOO-003](../config/hypotheses.json) 研究卓越性証拠。[IND-030](../config/indicators.json) critical文脈 | A-1 | 前回確認（2026-06-21 INFO-048） |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| GCP成長率が低ベース効果で説明可能と判明し、絶対顧客増加数がAWS/Azureと同等以下になる | [H-GOO-001](../config/hypotheses.json) のC蓄積（GCP固有成長）が崩れる | 60日 | [IND-006](../config/indicators.json) |
| Workspace内GeminiのDAU/MAUまたは利用率が3四半期連続で頭打ちを示す | 「エコシステム統合優位」のコア判断と[H-GOO-001](../config/hypotheses.json)が崩れる | 180日 | [IND-006](../config/indicators.json) |
| 囲い込み証拠が35件を超え、規制当局が介入する | [H-GOO-002](../config/hypotheses.json)が棄却水準に到達。現在33件で接近中 | 120日 | [IND-027](../config/indicators.json) |
| DeepMindのAI Control RoadmapがGemini製品に統合されない状態が4四半期続く | [H-GOO-003](../config/hypotheses.json)の「研究卓越性から製品競争力」因果が崩れる | 180日 | [IND-001](../config/indicators.json) |
| Google $40B Anthropic投資の最終額・ガバナンス条件が開示され、戦略的意図が判別可能になる | [H-GOO-001](../config/hypotheses.json) C蓄積の質的評価の確定 | 90日 | [IND-006](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | Gemini統合でエコシステム収益を拡大する | 50% low | ±0%。12件多面的C蓄積（Managed Agents・Enterprise Agent Platform Skill Registry/RAG Engine/ADK・Interactions API GA・Gemini 3.5 Flash・Robotics-ER・Forrester逆転B-2・$40B投資・Antigravity・gpt-ossホスト・GCP +63%）。Arbiter v4.13条件（コアエンタープライズ定量データA-2+）は広告領域で部分充足のみ。B-2品質・低ベース効果・Google固有定量分解未達成でlow維持 | [INFO-036](../Information/2026-07-10/collected-raw.md#INFO-036) [INFO-014](../Information/2026-07-10/collected-raw.md#INFO-014) | (代替説明未解決) |
| [H-GOO-002](../config/hypotheses.json) | 囲い込み回避で開放維持 | 23% low | ±0%。Enterprise Agent PlatformのSkill Registryでプラットフォーム固有化の可能性あるが品質判別不能。围い込み33件・開放証拠蓄積の非対称性継続。low帯深化 | [INFO-037](../Information/2026-07-10/collected-raw.md#INFO-037) (MS Foundry→M365) | [INFO-036](../Information/2026-07-10/collected-raw.md#INFO-036) (Skill Registry) |
| [H-GOO-003](../config/hypotheses.json) | DeepMind統合シナジーで競争力を維持する | 48% medium | ±0%。G7 Hassabis AI連合共同提案・Robotics-ER商用提供・DeepMind AI Control Roadmap A-1・AGI→ASI論文・Hassabis AGI 2030のC蓄積。Jumper流出はI方向。Robotics-ERの実環境性能データ不在。medium維持 | [INFO-075](../Information/2026-07-10/collected-raw.md#INFO-075) | Jumper流出（前回確認） |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt以上/期でhigh | Gemini 3.5 Flashコンピュータ使用・Robotics-ER・Enterprise Agent Platform Skill Registry/RAG Engine/ADK。Gemini 3.5 Flashの性能はGoogle自家測定。独立ベンチマーク検証未完了 | 2026-07-10 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated維持で継続監視 | GCP +63% YoY最速 + Enterprise Agent Platform + Managed Agents拡張 + Gemini 3.5 Flashコンピュータ使用 + Google $40B Anthropic投資 | 2026-07-10 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated / stable | Gemini 3.5 Flash・Sonnet 5・Fable 5 ECI 161・Seedance 2.5 30秒4K。量的向上継続。「真の理解」未解決 | 2026-07-10 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | high / rising | MCP RC 2026-07-28・AAIF拡大・Google Enterprise Agent Platform・MS Foundry→M365・OpenAI Agents SDK provider-agnostic・NVIDIA OpenShell。標準化臨界点通過後の定着加速 | 2026-07-10 |
| [IND-028](../config/indicators.json) | AGI到達度・RSI具体化 | high / rising | G7 Hassabis+Amodei AI連合・強いAGI 2031-2035・UN科学パネル発足・AGI定義不合・Claude自コード80% | 2026-07-10 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。連邦政府全体禁止・Huawei級指定・DPA脅迫・国連事務総長LAWS禁止・Warren開示要求7社含む・human-in-loop法案・June 2026 EO。KIQ-MIL-001 18R不在。DeepMind AI Control Roadmapで高度AIを「内部脅威」認定 | 2026-07-10 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-07-10 | 全面書き直し。Gemini Enterprise Agent Platform（Skill Registry/RAG Engine/ADK）（[INFO-036](../Information/2026-07-10/collected-raw.md#INFO-036) A-3）・Managed Agents機能拡張（[INFO-014](../Information/2026-07-10/collected-raw.md#INFO-014) A-3）を新規反映。G7 Hassabis+Amodei AI連合共同提案を反映。仮説確度は全て±0%据え置き。Arbiter v4.31 COMPLETE | [INFO-036](../Information/2026-07-10/collected-raw.md#INFO-036) [INFO-014](../Information/2026-07-10/collected-raw.md#INFO-014) [INFO-075](../Information/2026-07-10/collected-raw.md#INFO-075) | H-GOO-001 50%(±0%)・H-GOO-002 23%(±0%)・H-GOO-003 48%(±0%) |
| 2026-06-28 | 全面書き直し。Gemini 3.5 Flashコンピュータ使用・Gemini Robotics-ER商用提供・Vertex AI → Gemini Enterprise Agent Platform改名を反映 | [INFO-022](../Information/2026-06-28/collected-raw.md#INFO-022) [INFO-023](../Information/2026-06-28/collected-raw.md#INFO-023) | H-GOO-001 50%(±0%)・H-GOO-002 23%(±0%)・H-GOO-003 48%(±0%) |
| 2026-06-23 | 全面書き直し。Google最大$40B Anthropic投資報道・Jumper DeepMind流出を反映。[H-GOO-001](../config/hypotheses.json) 49→50% | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) | H-GOO-001 49→50% low |
| 2026-06-21 | 全面書き直し。[IND-030](../config/indicators.json) high→critical移行。DeepMind AI Control Roadmapを反映 | [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) | IND-030 critical |

## 7. ブラインドスポット

- Google固有定量データが継続して不在。Arbiter v4.13条件（コアエンタープライズAI定量データA-2+）が未達成。12件の多面的C蓄積があるが、全てA-3品質の製品証拠またはB-2品質の間接証拠であり、シェア・収益・利用率の直接的定量データではない。
- GCP +63% YoYの低ベース効果（GCPシェア14% vs AWS 28%）の排除が未解決。絶対顧客増加数がAWS/Azureと同等以上であるかの確認が必要。
- Workspace内GeminiのDAU/MAUが公開されていない。エコシステム統合の実際の利用率・定着率を外部から測る手段がない。
- Gemini Enterprise Agent PlatformのSkill Registryが、プラットフォーム固有化（围い込み）の新メカニズムなのか、セキュリティ向上の正当な機能なのかの判別が困難。
- Google $40B Anthropic投資の最終額とガバナンス条件が未確定。「最大$40B」であり実際の投資額はこれより少ない可能性がある。戦略的意図の判別には取締役席や戦略提携条件の開示が必要。
- Gemini 3.5 Flashコンピュータ使用の性能がGoogle自家測定。ブラウザ・モバイル・デスクトップでの実行成功率・レイテンシ・エラー率が独立ベンチマークで検証されていない。
- 囲い込みI 33件の品質別内訳が未開示。A-1/A-2品質の独立性「高」件数がいくつあるか不明。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-014](../Information/2026-07-10/collected-raw.md#INFO-014) | Google Managed Agents機能拡張: バックグラウンド実行・リモートMCP・カスタム関数・Gemini Enterprise Agent Platform(A-3) |
| [INFO-036](../Information/2026-07-10/collected-raw.md#INFO-036) | Gemini Enterprise Agent Platform: Skill Registry・RAG Engine・ADK・Agent Builder+Agent Engine統合(A-3) |
| [INFO-037](../Information/2026-07-10/collected-raw.md#INFO-037) | MS Foundry: エージェントをM365 Copilot/Teamsに直接公開・再構築不要(A-3) |
| [INFO-075](../Information/2026-07-10/collected-raw.md#INFO-075) | G7: Altman/Hassabis/Amodei AGI討議・Hassabis+Amodei米国主導国際AI連合共同提案・強いAGI 2031-2035(B-2) |
| [INFO-076](../Information/2026-07-10/collected-raw.md#INFO-076) | AGI定義不合継続・UN暫定AI報告書・OpenAI AGI定義「経済的に価値ある仕事で人間を上回る」(B-2) |
| [INFO-090](../Information/2026-07-10/collected-raw.md#INFO-090) | UN独立国際科学AIパネル（40人）7/1発足・暫定AI能力・リスク評価報告書・Bengio危険性警告(B-3) |
| [Arbiter v4.31](../state/arbiter-2026-07-10.md) | 確度評価の完全根拠 |
