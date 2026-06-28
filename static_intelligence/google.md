# Google / DeepMind

> 最終判断更新: 2026-06-28
> 全体確信度: 低
> 情報非対称性: Workspace / Gemini 統合の DAU/MAU 非公開。TPU 対 NVIDIA の電力効率が外部から測れない。KIQ-GOO-001がGCP +63% vs Azure +40% vs AWS +28%で初充足されたが、B-2品質かつ低ベース効果（GCPシェア14% vs AWS 28%）の排除が未解決。围い込みI 33件の品質別内訳未開示。Vertex AIからGemini Enterprise Agent Platformへの移行影響範囲が非公開。Gemini 3.5 Flashコンピュータ使用の性能がGoogle自家測定であり独立検証未完了。Gemini Robotics-ERの実環境性能データが不在。Google最大$40B Anthropic投資の最終額・戦略的意図が未確定。Jumper移籍のDeepMind研究体制への定量的影響が不明
> 主参照: [H-GOO-001](../config/hypotheses.json) [H-GOO-002](../config/hypotheses.json) [H-GOO-003](../config/hypotheses.json) [IND-001](../config/indicators.json) [IND-006](../config/indicators.json) [IND-025](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

GoogleがGemini製品ラインを3方向に拡張した。Gemini 3.5 Flashにコンピュータ使用機能を組み込み [INFO-022](../Information/2026-06-28/collected-raw.md#INFO-022)（A-3）、Gemini Robotics-ER（Embodied Reasoning）モデルの商用提供を開始し [INFO-023](../Information/2026-06-28/collected-raw.md#INFO-023)（A-3）、Vertex AIを「Gemini Enterprise Agent Platform」にリブランディングしてトークン/秒レイテンシSLAを追加した [INFO-013](../Information/2026-06-28/collected-raw.md#INFO-013)（A-3）。これらはエージェント実行・物理AI・エンタープライズ基盤の3層でのプラットフォーム深化を示す。[H-GOO-001](../config/hypotheses.json) は50% low・[H-GOO-002](../config/hypotheses.json) は23% low・[H-GOO-003](../config/hypotheses.json) は48% mediumで、いずれも±0%。

[H-GOO-001](../config/hypotheses.json) のlow維持理由は変わらない。Interactions API GA・Gemini Enterprise Agent Platform・Gemini 3.5 Flashコンピュータ使用・Robotics-ERの4件はエコシステム統合の証拠（強める方向）だが、Arbiter v4.13条件（コアエンタープライズAI定量データA-2+）は未達成。Forrester「Google > OpenAI」代理店逆転 [INFO-037](../Information/2026-06-23/collected-raw.md#INFO-037)（B-2）は広告領域でのみ部分充足。GCP +63% YoY [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055)（B-2）は低ベース効果の排除が未解決。もしWorkspace内GeminiのDAU/MAUが3四半期連続で頭打ちを示すか、围い込み証拠が35件を超えれば、コア判断が変わる。

## 1. コア判断

GoogleのGeminiプラットフォーム戦略が3層で同時に深化した。エージェント実行層では、Gemini 3.5 Flashにコンピュータ使用機能がネイティブに組み込まれた [INFO-022](../Information/2026-06-28/collected-raw.md#INFO-022)（A-3）。開発者はブラウザ、モバイル、デスクトップインターフェースで見て推論し行動するエージェントを構築できる。物理AI層では、Gemini Robotics-ER（Embodied Reasoning）がGemini API Pricingページに記載され、商用提供が開始された [INFO-023](../Information/2026-06-28/collected-raw.md#INFO-023)（A-3）。Vision-Language-Actionモデルで物理的推論とマルチステップロボット操作を実現する。エンタープライズ基盤層では、Vertex AIが「Gemini Enterprise Agent Platform」にリブランディングされ、Provisioned Throughputにトークン/秒レイテンシSLAが追加された [INFO-013](../Information/2026-06-28/collected-raw.md#INFO-013)（A-3）。Developer APIとEnterprise Agent Platform APIの2層構造が定義された。

これら3件は[H-GOO-001](../config/hypotheses.json)のC蓄積（エコシステム統合の証拠・強める方向）に加わる。前回の7件（Interactions API・Gemini Enterprise・gpt-ossホスト・Antigravity・Forrester逆転・$40B投資・Vertex統合）と合わせて10件の多面的蓄積になる。ただしlow維持の理由は3点変わらない。第一に、Arbiter v4.13が設定した条件（コアエンタープライズAI定量データA-2+）が未達成。第二に、利用可能な最高品質がB-2（Forrester逆転・GCP成長率）であり、A-2+でない。第三に、GCP +63% YoYの低ベース効果（GCPシェア14% vs AWS 28%）の排除が未解決。Gemini 3.5 Flash・Robotics-ER・Enterprise Agent Platformの3件はA-3品質の製品証拠であり、C蓄積の幅を拡げたが、コアエンタープライズAI領域での定量採用データ（シェア・収益・利用率）ではない。

[H-GOO-003](../config/hypotheses.json) は48% mediumで±0%。Gemini Robotics-ERの商用提供開始は、Boston Dynamics提携 [INFO-010](../Information/2026-06-16/collected-raw.md#INFO-010)（B-3）とGemini Robotics On-Device [INFO-011](../Information/2026-06-16/collected-raw.md#INFO-011)（B-3）の延長線上にある物理AI能力の製品化であり、研究卓越性から製品競争力への変換を示す。但し実環境性能データが不在であり、Jumper流出 [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066)（B-2）のI方向（弱める方向）と相殺する。

[H-GOO-002](../config/hypotheses.json) は23% lowで±0%。Vertex AIのGemini Enterprise Agent Platformへのリブランディングは、エコシステム深化の側面（強める方向）とプラットフォーム固有化の側面（弱める方向）を同時に持つ。围い込みI 33件の蓄積に新規追加の品質判別はできていない。開放証拠（Interactions API GA・Agent Skills標準）の蓄積は継続するが、围い込み蓄積速度を上回る決定的証拠はない。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Gemini 3.5 Flashネイティブコンピュータ使用: ブラウザ・モバイル・デスクトップでエージェント構築可能 | [H-GOO-001](../config/hypotheses.json) エコシステム統合の証拠（強める方向）。エージェント実行層の深化 | A-3 | [INFO-022](../Information/2026-06-28/collected-raw.md#INFO-022) |
| 高 | Gemini Robotics-ER商用提供開始: Vision-Language-Action・物理的推論・マルチステップロボット操作 | [H-GOO-003](../config/hypotheses.json) 研究卓越性から製品化（強める方向）。物理AI新モデルライン | A-3 | [INFO-023](../Information/2026-06-28/collected-raw.md#INFO-023) |
| 高 | Vertex AI → Gemini Enterprise Agent Platform リブランディング・トークン/秒SLA追加 | [H-GOO-001](../config/hypotheses.json) エンタープライズ基盤深化。[H-GOO-002](../config/hypotheses.json) プラットフォーム固有化の側面 | A-3 | [INFO-013](../Information/2026-06-28/collected-raw.md#INFO-013) |
| 高 | Interactions API GA: モデル+エージェント+ツール統合の単一エンドポイント | [H-GOO-001](../config/hypotheses.json) C蓄積。インフラ成熟。但しGA≠市場奪取 | A-3 | [INFO-005](../Information/2026-06-28/collected-raw.md#INFO-005) |
| 高 | Google最大$40B Anthropic投資・G7でAmodei+Hassabisが米国主導AI連合提唱 | [H-GOO-001](../config/hypotheses.json) C蓄積。戦略的意図（インフラ依存・影響力・OpenAI対策）は未確定 | B-2 | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) |
| 高 | Forrester「Google > OpenAI」代理店優先パートナー逆転 | [H-GOO-001](../config/hypotheses.json) C蓄積。19R代替説明への定量証拠。但し広告領域のみ部分充足 | B-2 | [INFO-037](../Information/2026-06-23/collected-raw.md#INFO-037) |
| 高 | GCP +63% YoY（15Q最高）vs Azure +40% vs AWS +28%。市場シェア: AWS 28% / Azure 21% / GCP 14% | [H-GOO-001](../config/hypotheses.json) KIQ-GOO-001初充足。19R代替説明への初の定量的反証。但しB-2品質・低ベース効果 | B-2 | [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055) |
| 高 | DeepMind「AI Control Roadmap」: 高度AIエージェントを「内部脅威」と扱う | [H-GOO-003](../config/hypotheses.json) 研究卓越性証拠。[IND-030](../config/indicators.json) critical文脈 | A-1 | [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) |
| 中 | ノーベル賞John JumperがDeepMindからAnthropicに移籍 | [H-GOO-003](../config/hypotheses.json) I方向。研究卓越性の維持力に疑問。安全チーム離職と合わせて構造的 | B-2 | [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| 中 | 围い込みI 33件蓄積・開放証拠蓄積継続（非対称性継続） | [H-GOO-002](../config/hypotheses.json) 23%。Vertex AI改名で新規围い込みの可能性あるが品質判別不能 | A-3 | [H-GOO-002](../config/hypotheses.json) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| GCP成長率が低ベース効果で説明可能と判明し、絶対顧客増加数がAWS/Azureと同等以下になる | [H-GOO-001](../config/hypotheses.json) のC蓄積（GCP固有成長）が崩れる | 60日 | [IND-006](../config/indicators.json) |
| Workspace内GeminiのDAU/MAUまたは利用率が3四半期連続で頭打ちを示す | 「エコシステム統合優位」のコア判断と[H-GOO-001](../config/hypotheses.json)が崩れる | 180日 | [IND-006](../config/indicators.json) |
| 囲い込み証拠が35件を超え、規制当局が介入する | [H-GOO-002](../config/hypotheses.json)が棄却水準に到達。現在33件で接近中 | 120日 | [IND-027](../config/indicators.json) |
| DeepMindのAI Control RoadmapがGemini製品に統合されない状態が4四半期続く | [H-GOO-003](../config/hypotheses.json)の「研究卓越性から製品競争力」因果が崩れる | 180日 | [IND-001](../config/indicators.json) |
| Jumper級の研究者流出が更に2件以上発生する | [H-GOO-003](../config/hypotheses.json) 48% mediumからの低下。研究卓越性の構造的弱体化 | 180日 | [IND-028](../config/indicators.json) |
| Google $40B Anthropic投資の最終額・ガバナンス条件が開示され、戦略的意図が判別可能になる | [H-GOO-001](../config/hypotheses.json) C蓄積の質的評価の確定 | 90日 | [IND-006](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-GOO-001](../config/hypotheses.json) | Gemini統合でエコシステム収益を拡大する | 50% low | ±0%。10件多面的C蓄積（Interactions API GA・Gemini 3.5 Flash コンピュータ使用・Robotics-ER・Enterprise Agent Platform改名・Forrester逆転B-2・$40B投資・Antigravity・gpt-ossホスト・GCP +63%）。Arbiter v4.13条件（コアエンタープライズ定量データA-2+）は広告領域で部分充足のみ。B-2品質・低ベース効果・Google固有定量分解未達成でlow維持 | [INFO-022](../Information/2026-06-28/collected-raw.md#INFO-022) [INFO-013](../Information/2026-06-28/collected-raw.md#INFO-013) [INFO-005](../Information/2026-06-28/collected-raw.md#INFO-005) [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055) | [INFO-025](../Information/2026-05-18/collected-raw.md#INFO-025) |
| [H-GOO-002](../config/hypotheses.json) | 囲い込み回避で開放維持 | 23% low | ±0%。Vertex AI改名でプラットフォーム固有化の可能性あるが品質判別不能。围い込み33件・開放証拠蓄積の非対称性継続。low帯深化 | [INFO-044](../Information/2026-06-12/collected-raw.md#INFO-044) [INFO-010](../Information/2026-06-06/collected-raw.md#INFO-010) | [INFO-016](../Information/2026-06-06/collected-raw.md#INFO-016) [INFO-013](../Information/2026-06-28/collected-raw.md#INFO-013) |
| [H-GOO-003](../config/hypotheses.json) | DeepMind統合シナジーで競争力を維持する | 48% medium | ±0%。Gemini Robotics-ER商用提供開始(INFO-023)・DeepMind AI Control Roadmap A-1・AGI→ASI論文・Hassabis AGI 2030・Boston Dynamics提携のC蓄積。Jumper流出はI方向。Robotics-ERの実環境性能データ不在。medium維持 | [INFO-023](../Information/2026-06-28/collected-raw.md#INFO-023) [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) [INFO-072](../Information/2026-06-16/collected-raw.md#INFO-072) [INFO-046](../Information/2026-06-16/collected-raw.md#INFO-046) | [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能 | +5pt以上/期でhigh | Gemini 3.5 Flashコンピュータ使用(INFO-022)・Gemini Robotics-ER(INFO-023)・Gemini 3 Pro Deep Thinkマルチモーダル#1・Gemini Omni動画生成。Flash・Robotics-ERの性能はGoogle自家測定。独立ベンチマーク検証未完了 | 2026-06-28 |
| [IND-006](../config/indicators.json) | エージェントスタック競争 | elevated維持で継続監視 | GCP +63% YoY最速 + Interactions API GA + Gemini Enterprise Agent Platform(Vertex AI改名) + Gemini 3.5 Flashコンピュータ使用 + Antigravityクロス互換 + Google $40B Anthropic投資 | 2026-06-28 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated / stable | Gemini 3.5 Flashコンピュータ使用・Gemini Robotics-ER・Gemini 3 Pro Deep Thinkマルチモーダル#1・Seedance 2.5。量的向上継続。「真の理解」未解決 | 2026-06-28 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | high / rising | Interactions API GA・Agent Skills標準・MCP RC 2026-07-28・AAIF・Sandbox OSS。標準化臨界点通過後の定着加速 | 2026-06-28 |
| [IND-028](../config/indicators.json) | AGI到達度・RSI具体化 | high / rising | Hassabis AGI ~2030「種レベル移行」・DeepMind AGI→ASI 4経路・RSI具体化とベンチマーク限界同時進行 | 2026-06-28 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | （critical到達済み） | **critical/rising**。GPT-5.6政府制限(A-2)・Operation Epic Fury複数独立再確認・DPA検討・中国AIラベリング・EU AI Act第50条。DeepMind AI Control Roadmapで高度AIを「内部脅威」認定。Google安全チーム離職・Jumper流出・NSF資金削減で安全インフラ後退 | 2026-06-28 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-28 | 全面書き直し。Gemini 3.5 Flashコンピュータ使用（[INFO-022](../Information/2026-06-28/collected-raw.md#INFO-022) A-3）・Gemini Robotics-ER商用提供開始（[INFO-023](../Information/2026-06-28/collected-raw.md#INFO-023) A-3）・Vertex AI → Gemini Enterprise Agent Platform改名（[INFO-013](../Information/2026-06-28/collected-raw.md#INFO-013) A-3）を反映。新規フロンティアモデルライン（Robotics-ER）とプラットフォーム改名による構造変化。仮説確度は全て±0%据え置き | [INFO-022](../Information/2026-06-28/collected-raw.md#INFO-022) [INFO-023](../Information/2026-06-28/collected-raw.md#INFO-023) [INFO-013](../Information/2026-06-28/collected-raw.md#INFO-013) | H-GOO-001 50%(±0%)・H-GOO-002 23%(±0%)・H-GOO-003 48%(±0%) |
| 2026-06-23 | 全面書き直し。Google最大$40B Anthropic投資報道・Jumper DeepMind流出・NSF基礎科学20-30%削減を反映。[H-GOO-001](../config/hypotheses.json) 49→50% | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) | H-GOO-001 49→50% low |
| 2026-06-21 | 全面書き直し。[IND-030](../config/indicators.json) high→critical移行。DeepMind AI Control Roadmap・Google安全チーム離職・NSF AI資金削減を反映 | [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) [INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052) | IND-030 critical |
| 2026-06-16 | H-GOO-001 +1%（KIQ-GOO-001初充足）・物理AI・研究リーダーシップ・Google従業員公開書簡を反映 | 2026-06-16複数INFO | H-GOO-001 48% low |
| 2026-06-15 | Gemini Omni・3.5 Flash・Interactions API / Managed Agents APIを新規製品証拠として組み込み | 2026-06-15複数INFO | |
| 2026-06-12 | H-GOO-001 medium→low移行・Gemini 3.1 Pro・DiffusionGemma・Agentic Gemini era宣言を反映 | 2026-06-12複数INFO | |

## 7. ブラインドスポット

- Google最大$40B Anthropic投資の最終額とガバナンス条件が未確定。「最大$40B」であり実際の投資額はこれより少ない可能性がある。戦略的意図（インフラ依存強化・影響力確保・OpenAI対策）の判別には取締役席や戦略提携条件の開示が必要。
- Gemini Robotics-ERの実環境性能データが不在。Boston Dynamics提携とGemini Robotics FM基盤はデモ段階であり、商用スケールでの信頼性・精度が未検証。API Pricingページへの記載は商用提供の開始を示すが、実際のデプロイ件数・成功率は非公開。
- Gemini 3.5 Flashコンピュータ使用の性能がGoogle自家測定。ブラウザ・モバイル・デスクトップでの実行成功率・レイテンシ・エラー率が独立ベンチマークで検証されていない。
- Jumper移籍のDeepMind研究体制への定量的影響が不明。個人の移籍は象徴的意義は大きいが、組織能力の量的評価には直結しない。Jumper級の追加流出が発生した場合、[H-GOO-003](../config/hypotheses.json) のmedium維持が困難になる。
- Vertex AIからGemini Enterprise Agent Platformへのリブランディングが既存エンタープライズ顧客に与える影響が不透明。SLA追加は品質保証の強化だが、API仕様変更や移行コストの発生可能性がある。
- 囲い込みI 33件の品質別内訳が未開示。A-1/A-2品質の独立性「高」件数がいくつあるか不明。Vertex AI改名による新規囲い込み効果の判別も不能。
- H-GOO-001 +1%はB-2品質中心のC蓄積。低ベース効果（GCPシェア14% vs AWS 28%）の排除が未解決。Forrester逆転は広告領域のみの部分充足。
- Workspace内GeminiのDAU/MAUが公開されていない。エコシステム統合の実際の利用率・定着率を外部から測る手段がない。
- H-GOO-003の評価指標が不十分。「エコシステム深度・研究卓越性・インフラ統合」の3軸それぞれについて独立評価する定量指標を持っていない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-022](../Information/2026-06-28/collected-raw.md#INFO-022) | Gemini 3.5 Flashネイティブコンピュータ使用: ブラウザ・モバイル・デスクトップ(A-3) |
| [INFO-023](../Information/2026-06-28/collected-raw.md#INFO-023) | Gemini Robotics-ER: 身体化推論・Vision-Language-Action・商用提供開始(A-3) |
| [INFO-013](../Information/2026-06-28/collected-raw.md#INFO-013) | Vertex AI → Gemini Enterprise Agent Platform リブランディング・SLA追加(A-3) |
| [INFO-005](../Information/2026-06-28/collected-raw.md#INFO-005) | Interactions API GA: モデル+エージェント+ツール統合(A-3) |
| [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) | Google最大$40B Anthropic投資報道・G7 Amodei+Hassabis米国主導AI連合要請(B-2) |
| [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) | Jumper DeepMind流出・NSF基礎科学20-30%削減・Anthropic $1Tセカンダリ(B-2) |
| [INFO-037](../Information/2026-06-23/collected-raw.md#INFO-037) | Forrester「Google > OpenAI」代理店優先パートナー逆転(B-2) |
| [INFO-048](../Information/2026-06-21/collected-raw.md#INFO-048) | DeepMind AI Control Roadmap: 高度AIエージェントを「内部脅題」(A-1) |
| [INFO-052](../Information/2026-06-21/collected-raw.md#INFO-052) | Google安全チーム離職・NSF AI資金3分の1削減(B-2) |
| [INFO-055](../Information/2026-06-16/collected-raw.md#INFO-055) | Cloud成長率比較: GCP +63% vs Azure +40% vs AWS +28%・KIQ-GOO-001初充足(B-2) |
| [INFO-010](../Information/2026-06-16/collected-raw.md#INFO-010) | Boston Dynamics × DeepMind: ヒューマノイドロボットAI提携(B-3) |
| [INFO-011](../Information/2026-06-16/collected-raw.md#INFO-011) | Gemini Robotics On-Device: 完全オフライン動作・Gemma 4 E2Bローカル実行(B-3) |
| [INFO-046](../Information/2026-06-16/collected-raw.md#INFO-046) | Hassabis AGI予測: 2030年（±1年）・準備警告(A-2) |
| [INFO-072](../Information/2026-06-16/collected-raw.md#INFO-072) | DeepMind 60ページ論文: AGI→ASIマッピング(A-2) |
| [INFO-029](../Information/2026-06-16/collected-raw.md#INFO-029) | 560+ Google従業員公開書簡: 米政府AI使用拒否要請(A-2) |
| [INFO-006](../Information/2026-06-15/collected-raw.md#INFO-006) | Gemini Omni: 動画生成・会話型編集・Gemini 3.5 Flash: フロンティア級(A-3) |
| [INFO-014](../Information/2026-06-15/collected-raw.md#INFO-014) | Interactions API + Managed Agents API: Agent Platform機能拡張(A-3) |
