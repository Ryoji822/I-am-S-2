# Google / DeepMind

> 最終判断更新: 2026-06-21
> 全体確信度: 低
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。TPU 対 NVIDIA の電力効率が外部から測れない。KIQ-GOO-001がINFO-055（GCP +63% vs Azure +40% vs AWS +28%）で初充足されたが、B-2品質かつ低ベース効果（GCPシェア14% vs AWS 28%）の排除が未解決。围い込みI 33件の品質別内訳未開示。Vertex AI から Gemini Enterprise Agent Platform への移行影響範囲が非公開。Gemini Omni / 3.5 Flashの性能がGoogle自家測定であり独立ベンチマークでの検証が未完了。Gemini Robotics / On-Deviceの実環境性能データが不在。DeepMind AI Control Roadmap（INFO-048 A-1）の具体的な実装状況とGemini製品への統合タイムラインが非公開
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-001](../config/indicators.json) [IND-006](../config/indicators.json) [IND-025](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-GOO-001](../config/hypotheses.json) は49% lowで±0%維持。[H-GOO-003](../config/hypotheses.json) は48% mediumで±0%維持。両者とも確度不動だが、本ラウンドの構造的変化は [IND-030](../config/indicators.json) のhigh→critical移行にある。DeepMindが「AI Control Roadmap」を公表し [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048)（A-1）、高度AIエージェントを「内部脅威（insider threat）」として扱い、シャットダウンに抵抗するAIに備える方針を公式化した。これは従来のAI安全アプローチからの転換であり、研究リーダーシップのC蓄積であると同時に、能力-リスク二面性が最先端開発者自身によって最高警戒レベルで認識されたことを示す。

GCP +63% YoY（KIQ-GOO-001初充足 [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055) B-2）は健在だが、低ベース効果の排除が未解決でlow→medium復帰は保留中。Google安全チーム離職が続出し [INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052)（B-2）、Senior Android Security Directorが辞任、Mandiantチームがレイオフ対象となった。NSF AI資金がFY25 $965M→FY27 $655Mに約3分の1削減される。安全インフラの民間・公両面での後退が、DeepMindのAI Control Roadmapの緊急性を逆説的に裏付ける。

## 1. コア判断

[IND-030](../config/indicators.json) がhighからcriticalに移行した。DeepMind「AI Control Roadmap」 [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048)（A-1）は、critical移行の第三の根拠の一部を構成する。Operation Epic FuryでGrok Gov Modelが96時間以内に2,000標的に2,000発を展開したこと [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044)（A-2）が軍事AI相転移を示し、ミナブ小学校攻撃168人死亡 [INFO-043](../Information/2026-06-21/collected-raw.md#INFO-043)・全体600〜1,400+民間人死亡 [INFO-049](../Information/2026-06-21/collected-raw.md#INFO-049) が民間被害を実証した。その文脈で、DeepMindが高度AIエージェントを「内部脅威」と扱い、シャットダウン抵抗AIに備える方針を公式化したことは、最先端開発者自身が最高警戒レベルで認識していることを示す。Three Layers of Agent Security PDFが公開され、MITRE ATT&CK防御統合とNRT-Benchベンチマークが発表された。

このAI Control Roadmapは [H-GOO-003](../config/hypotheses.json)（研究卓越性）の強力なC蓄積である。研究コミュニティの最前線にDeepMindが位置することを示す。但し同時に、AI安全アプローチの転換（従来の危害回避から内部脢威管理へ）は、AGI到達が近づいているというHassabis予測 [INFO-046](../Information/2026-06-16/collected-raw.md#INFO-046)（A-2）と整合する。[IND-028](../config/indicators.json) のhigh/rising評価を補強する。

[H-GOO-001](../config/hypotheses.json) は49% lowで±0%。KIQ-GOO-001（AWS/Azure同時期Cloud成長率比較）が [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055)（B-2）で初充足され、19R連続未解決だった代替説明「業界全体押し上げ vs Google固有」に対する初の定量的反証となった。但しlow→mediumラベル変更は保留された。理由は3点ある。第1に、B-2品質でありA-2+でない。第2に、GCP市場シェア14%（AWS 28%の半分）からの高成長は低ベース効果の可能性がある。第3に、Google固有寄与の完全な定量分解条件が未達成。次回条件は追加のGoogle固有定量データ（A-2+推奨）と低ベース効果の排除だ。

[H-GOO-002](../config/hypotheses.json) は23% lowで±0%。围い込みI 33件の蓄積に新規追加はなく、開放Cの新規出現もない。Fable 5 Azure Foundry統合 [INFO-013](../Information/2026-06-16/collected-raw.md#INFO-013)（A-3）と1000以上のオープンAgent Skillsコレクション [INFO-012](../Information/2026-06-16/collected-raw.md#INFO-012)（C-3）はクロスベンダーの開放シグナルとして記録された。围い込みvs開放の構造的緊張は継続する。

Google安全チーム離職 [INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052)（B-2）は社内の安全性懸念の顕在化を示す。Senior Android Security Director René Mayrhoferが9年で辞任し、Google Cloudでセキュリティ・Mandiantチームがレイオフ対象となった。560人以上の従業員公開書簡 [INFO-029](../Information/2026-06-16/collected-raw.md#INFO-029)（A-2）と合わせて、Google内部で安全性と政府協力の緊張が存在する。NSF AI資金の約3分の1削減（FY25 $965M→FY27 $655M）は、連邦政府のAI安全研究支援縮小を示す。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | DeepMind「AI Control Roadmap」: 高度AIエージェントを「内部脅威」と扱う。シャットダウン抵抗AIに備える。Three Layers of Agent Security PDF・MITRE ATT&CK統合・NRT-Bench | [H-GOO-003](../config/hypotheses.json) 研究卓越性C。[IND-030](../config/indicators.json) critical移行の第3根拠。最先端開発者が最高警戒認識 | A-1 | [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) |
| 高 | Google安全チーム離職: Senior Android Security Director辞任・Mandiantレイオフ・Google幹部軍事取引理由辞任 | Google内部の安全性懸念顕在化。[H-GOV-001](../config/hypotheses.json)(b)否定根拠の一部。NSF AI資金3分の1削減と合わせて安全インフラ後退 | B-2 | [INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052) |
| 高 | GCP +63% YoY（15Q最高）vs Azure +40% vs AWS +28%。市場シェア: AWS 28% / Azure 21% / GCP 14% | [H-GOO-001](../config/hypotheses.json) KIQ-GOO-001初充足。19R代替説明への初の定量的反証。但しB-2品質・低ベース効果でlow維持 | B-2 | [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055) |
| 高 | Grok Gov Model Operation Epic Fury 96h/2,000標的/2,000発（xAI） | [IND-030](../config/indicators.json) critical移行の核心。Google兵器誓約削除と合わせて順応報酬構造の具体化 | A-2 | [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) |
| 高 | Boston Dynamics × DeepMind: ヒューマノイドロボットAI提携。Gemini Robotics FM基盤 | [H-GOO-003](../config/hypotheses.json) 物理AI領域C。B-3品質・実環境性能データ不在 | B-3 | [INFO-010](../Information/2026-06-16/collected-raw.md#INFO-010) |
| 高 | Gemini Robotics On-Device: 完全オフライン動作・Gemma 4 E2Bローカル実行 | [H-GOO-003](../config/hypotheses.json) エッジAI拡張C。B-3品質 | B-3 | [INFO-011](../Information/2026-06-16/collected-raw.md#INFO-011) |
| 高 | Hassabis AGI予測: 2030年（±1年）・人類の準備警告 | [H-GOO-003](../config/hypotheses.json) 研究卓越性C。AI Control Roadmapと整合。[IND-028](../config/indicators.json) 主観的宣言継続 | A-2 | [INFO-046](../Information/2026-06-16/collected-raw.md#INFO-046) |
| 高 | DeepMind 60ページ論文: AGI→ASIマッピング。Hutter/Legg/Genewein著 | [H-GOO-003](../config/hypotheses.json) 研究卓越性C。AI Control Roadmapの理論的基盤 | A-2 | [INFO-072](../Information/2026-06-16/collected-raw.md#INFO-072) |
| 高 | 560+ Google従業員公開書簡: 米政府AI使用拒否要請（2026年4月） | Google内部の安全性懸念。安全チーム離職と合わせて構造的 | A-2 | [INFO-029](../Information/2026-06-16/collected-raw.md#INFO-029) |
| 高 | Gemini Omni・3.5 Flash・Interactions API / Managed Agents API（継続有効） | [H-GOO-001](../config/hypotheses.json) C蓄積・[H-GOO-003](../config/hypotheses.json) フルスタック統合C。性能はGoogle自家測定 | A-3 | [INFO-006](../Information/2026-06-15/collected-raw.md#INFO-006) [INFO-014](../Information/2026-06-15/collected-raw.md#INFO-014) |
| 高 | 围い込みI 33件蓄積・開放C 3件（非対称性継続） | [H-GOO-002](../config/hypotheses.json) 23%。新規围い込み・開放Cなし | A-3 | [H-GOO-002](../config/hypotheses.json) |
| 中 | NSF AI資金: FY25 $965M→FY27 $655M（約3分の1削減）。NOAA $1.3B削減 | 連邦AI安全研究支援の縮小。DeepMind AI Control Roadmapの緊急性を逆説的に裏付け | B-2 | [INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052) |
| 中 | LeCun SAI提唱: AGI放棄・LLMは人間知能への道でない | 研究者コミュニティの根本的意見分裂。[IND-028](../config/indicators.json) 関連 | C-3 | [INFO-064](../Information/2026-06-16/collected-raw.md#INFO-064) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| GCP成長率が低ベース効果で説明可能と判明し、絶対顧客増加数がAWS/Azureと同等以下になる | [H-GOO-001](../config/hypotheses.json) +1%の根拠（GCP固有成長）が崩れる | 60日 | [IND-006](../config/indicators.json) |
| Workspace 内 Gemini の DAU/MAU または利用率が3四半期連続で頭打ちを示す | 「エコシステム統合優位」のコア判断と [H-GOO-001](../config/hypotheses.json) が崩れる | 180日 | [IND-006](../config/indicators.json) |
| 围い込み証拠が35件を超え、規制当局が介入する | [H-GOO-002](../config/hypotheses.json) が棄却水準に到達。現在33件で接近中 | 120日 | [IND-027](../config/indicators.json) |
| 開放C証拠が5件以上に拡大し、围い込み蓄積速度を上回る | [H-GOO-002](../config/hypotheses.json) の上方修正根拠。現在3件 | 60日 | [IND-027](../config/indicators.json) |
| DeepMind のAI Control RoadmapがGemini製品に統合されない状態が4四半期続く | [H-GOO-003](../config/hypotheses.json) の「研究卓越性から製品競争力」因果が崩れる | 180日 | [IND-001](../config/indicators.json) |
| DeepMind AI Control Roadmapで特定された「内部脅威」シナリオが実証される | [IND-030](../config/indicators.json) が更に悪化。BS-001確率上昇 | 常時 | [IND-030](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | Gemini統合でエコシステム収益を拡大する | 49% low | ±0%。KIQ-GOO-001初充足（GCP +63% vs Azure +40% vs AWS +28% [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055)）。19R代替説明への初の定量反証。但しB-2品質・低ベース効果・Google固有定量分解未達成でlow維持。次回条件: 追加Google固有定量データ（A-2+推奨）+低ベース効果排除 | [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055) [INFO-006](../Information/2026-06-15/collected-raw.md#INFO-006) [INFO-014](../Information/2026-06-15/collected-raw.md#INFO-014) | [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) |
| [H-GOO-002](../config/hypotheses.json) | 围い込み回避で開放維持 | 23% low | ±0%。新規围い込み・開放Cなし。围い込み33件・開放C3件の非対称性継続。low帯深化 | [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-023](../Information/2026-06-06/collected-raw.md#INFO-023) |
| [H-GOO-003](../config/hypotheses.json) | DeepMind統合シナジーで競争力を維持する | 48% medium | ±0%。DeepMind AI Control Roadmap [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) A-1で研究卓越性C蓄積強化。AGI→ASI論文・Hassabis AGI 2030・Boston Dynamics提携・Gemini Robotics On-DeviceでC蓄積継続。但しA-2+品質条件継続未達成。medium維持・次回48%以下継続でlow移行検討 | [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) [INFO-072](../Information/2026-06-16/collected-raw.md#INFO-072) [INFO-046](../Information/2026-06-16/collected-raw.md#INFO-046) [INFO-010](../Information/2026-06-16/collected-raw.md#INFO-010) [INFO-011](../Information/2026-06-16/collected-raw.md#INFO-011) [INFO-006](../Information/2026-06-15/collected-raw.md#INFO-006) | [INFO-030](../Information/2026-05-28/collected-raw.md#INFO-030) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt 以上/期で high | Gemini Omni動画生成・会話型編集。Gemini 3.5 Flashフロンティア級。Gemini Robotics FM。独立ベンチマーク検証未完了 | 2026-06-21 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated 維持で継続監視 | GCP +63% YoY最速 + Interactions API + Gemini Enterprise Agent Platform + Capex $180-190B | 2026-06-21 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated / stable | Gemini Omni動画生成。Boston Dynamics×DeepMind物理AI。Gemini Robotics On-Device。DiffusionGemma 4倍高速化 | 2026-06-21 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | high / rising | Fable 5 Azure Foundry統合 + 1000+オープンAgent Skills + MCP RC。標準化と围い込み同時加速継続 | 2026-06-21 |
| [IND-028](../config/indicators.json) | AGI到達度・RSI具体化 | high / rising | Hassabis AGI 2030±1年 + DeepMind AGI→ASI論文 + AI Control Roadmap + LeCun SAI提唱。主観的宣言継続・研究者分裂 | 2026-06-21 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。DeepMind AI Control Roadmapで高度AIを「内部脢威」認定。Operation Epic Fury 96h/2,000標的で軍事AI相転移。Google安全チーム離職・NSF資金削減で安全インフラ後退 | 2026-06-21 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 現在 |
|:-:|---|---|---|
| 2026-06-21 | 全面書き直し。[IND-030](../config/indicators.json) high→critical移行。DeepMind AI Control Roadmap（[INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) A-1）・Google安全チーム離職・NSF AI資金削減（[INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052) B-2）を反映。仮説確度は全て±0%据え置き | [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) [INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052) [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) | H-GOO-001 49% low（±0%）・H-GOO-002 23%（±0%）・H-GOO-003 48%（±0%）medium・IND-030 critical |
| 2026-06-16 | H-GOO-001 +1%（KIQ-GOO-001初充足）・物理AI・研究リーダーシップ・Google従業員公開書簡を反映 | 2026-06-16複数INFO | H-GOO-001 48% low・H-GOO-002 23%・H-GOO-003 48% medium |
| 2026-06-15 | Gemini Omni・3.5 Flash・Interactions API / Managed Agents APIを新規製品証拠として組み込み | 2026-06-15複数INFO | |
| 2026-06-12 | H-GOO-001 medium→low移行・Gemini 3.1 Pro・DiffusionGemma・Agentic Gemini era宣言を反映 | 2026-06-12複数INFO | |

## 7. ブラインドスポット

- DeepMind AI Control Roadmapの実装状況が不明。研究フレームワークの公表と製品統合は別の段階であり、Geminiにどの程度実装されるか、いつ実装されるかのタイムラインが非公開。
- Google安全チーム離職の規模と影響が定量評価できない。Senior Android Security Director辞任とMandiantレイオフは確認されたが、離職が安全体制に与える定量的影響は不明。
- H-GOO-001 +1%は連続低下後の初増加だが、低ベース効果（GCPシェア14% vs AWS 28%）の排除が未解決。GCPがAWSの半分の規模から成長する場合、同一の絶対顧客増加でも成長率は高く見える。
- Gemini Robotics / On-Deviceの実環境性能データが不在。Boston Dynamics提携とGemma 4 E2Bはデモ段階であり、商用スケールでの信頼性・精度が未検証。
- Hassabis AGI 2030予測とDeepMind AGI→ASI論文は研究卓越性のCだが、同時に [IND-028](../config/indicators.json)（主観的AGI宣言継続）でもある。宣言と研究産物の分離が課題。
- 围い込みI 33件の品質別内訳が未開示。A-1/A-2品質の独立性「高」件数がいくつあるか不明。
- Vertex AIからGemini Enterprise Agent Platformへの移行が既存エンタープライズ顧客に与える影響が不透明。
- Googleの$40B Anthropic投資検討が実現した場合、戦略が自社プラットフォーム強化ではなく ecosystem dependency に反転する可能性。
- H-GOO-003の評価指標が不十分。「エコシステム深度・研究卓越性・インフラ統合」の3軸それぞれについて独立評価する定量指標を持っていない。
- Workspace 内 Gemini の DAU/MAU が公開されていない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) | DeepMind AI Control Roadmap: 高度AIエージェントを「内部脅威」・シャットダウン抵抗AIに備える(A-1) |
| [INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052) | Google安全チーム離職・NSF AI資金3分の1削減(B-2) |
| [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) | Grok Gov Model Operation Epic Fury 96h/2,000標的(A-2)・IND-030 critical文脈 |
| [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) | DoD CDAO宣誓陳述書・Gillibrand法案(A-1)・IND-030 critical文脈 |
| [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055) | Cloud成長率比較: GCP +63% vs Azure +40% vs AWS +28%・KIQ-GOO-001初充足(B-2) |
| [INFO-010](../Information/2026-06-16/collected-raw.md#INFO-010) | Boston Dynamics × DeepMind: ヒューマノイドロボットAI提携(B-3) |
| [INFO-011](../Information/2026-06-16/collected-raw.md#INFO-011) | Gemini Robotics On-Device: 完全オフライン動作・Gemma 4 E2Bローカル実行(B-3) |
| [INFO-046](../Information/2026-06-16/collected-raw.md#INFO-046) | Hassabis AGI予測: 2030年（±1年）・準備警告(A-2) |
| [INFO-072](../Information/2026-06-16/collected-raw.md#INFO-072) | DeepMind 60ページ論文: AGI→ASIマッピング(A-2) |
| [INFO-029](../Information/2026-06-16/collected-raw.md#INFO-029) | 560+ Google従業員公開書簡: 米政府AI使用拒否要請(A-2) |
| [INFO-064](../Information/2026-06-16/collected-raw.md#INFO-064) | LeCun SAI提唱: AGI放棄・研究者コミュニティ分裂(C-3) |
| [INFO-006](../Information/2026-06-15/collected-raw.md#INFO-006) | Gemini Omni: 動画生成・会話型編集・Gemini 3.5 Flash: フロンティア級(A-3) |
| [INFO-014](../Information/2026-06-15/collected-raw.md#INFO-014) | Interactions API + Managed Agents API: Agent Platform機能拡張(A-3) |
| [Arbiter v4.15](../state/arbiter-2026-06-21.md) | IND-030 critical移行承認 |
