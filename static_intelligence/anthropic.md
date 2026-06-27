# Anthropic

> 最終判断更新: 2026-06-27
> 全体確信度: 中
> 情報非対称性: Claude Code WAU/MAUが非公開。Claude Code DAU/日常利用者データ8R連続不在（v4.16到達から4R経過・medium→low移行条件倍加・DEGRADED制約でラベル変更保留）。収益内訳はQ2営業利益$559M/ARR $47Bで部分的解明。安全性が選択理由上位3要因以内かはA-2品質で未確認（Kano再定式化実行済み）。CVE-8.7が安全性差別化仮説に継続的矛盾。H-GOV-001(a)は54% medium・方向転換確認（3R連続-1%後2R連続+1%）・Pentagon標的選定ドクトリン改訂(INFO-018 A-2)が質的新次元・先例確立第2核心要件（実効性）に直結。Anthropic Q2 $559M利益(INFO-043 A-2)はI（先例確立≠実効性確認）だがDEGRADEDでI解釈変更保留。(b)はH-GOV-002として分離（21% low）。Fable 5/Mythos 5アクセス停止継続（6日目）。企業LLM支出シェア40%（Menlo・INFO-008 B-3）。Google $40B投資(INFO-045 B-2)は「最大$40B」であり最終額は未確定。IPO自己選択バイアスの除外が未完了。Arbiter v4.21はDEGRADED状態（Red Agent失敗・2R連続）
> 主参照: [H-ANT-001](../config/hypotheses.json) [H-ANT-002](../config/hypotheses.json) [H-ANT-003](../config/hypotheses.json) [H-GOV-001](../config/hypotheses.json) [H-GOV-002](../config/hypotheses.json) [H-CAR-001](../config/hypotheses.json) [H-CAR-002](../config/hypotheses.json) [H-CAR-003](../config/hypotheses.json) [IND-008](../config/indicators.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

[H-GOV-001](../config/hypotheses.json) は54%（medium）で方向転換を確認した。3ラウンド連続の-1%低下（54→53→52%）の後、2ラウンド連続の+1%上昇（52→53→54%）に転じた。方向転換の触媒はPentagon標的選定ドクトリン改訂である [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018)（A-2）。AIが軍事標的設定に広く関与する道を開放したこの改訂は、政府のAI政策が規制から積極的活用へ質的に転換したことを示す。先例確立の第2核心要件（実効性）に直結する質的新次元である。同時にAnthropic Q2営業利益$559M・ARR $47B [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043)（A-2）は、介入の実効性に疑問を呈すI方向証拠（先例確立≠実効性確認）である。介入能力の拡大と商業的成功の不均衡が新たな形で継続している。

[H-ANT-002](../config/hypotheses.json) は58%（medium）で4ラウンド連続-1%（62→58%）。Claude Code DAU/日常利用者データが8ラウンド連続不在となり、medium→low移行条件は初期設定（4R）から倍加した。企業LLM支出シェア40%（Menlo Ventures [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) B-3）・Anthropic AI 80%自コード生成 [INFO-049](../Information/2026-06-27/collected-raw.md#INFO-049)（B-2）がC方向だが、DAU不在のI方向が上回る。DEGRADED制約でラベル変更は保留。58%はFable 5 #1・Opus 4.8 SWE-bench #1技術リーダーシップへの依存が深まっている。

[IND-030](../config/indicators.json) はcriticalを維持。Pentagon標的選定ドクトリン改訂 [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) で、軍事AIが個別実験からドクトリンに組込まれた。DOJ法廷文書 [INFO-006](../Information/2026-06-27/collected-raw.md#INFO-006)（A-2）で政府の法的追求が継続している。条件2（A-2品質技術的安全事故報告）は未到達。H-GOV-001が60%を超えるか、次回COMPLETEでH-ANT-002 medium→lowが実行されるかで判断が変わる。

## 1. コア判断

全体確信度は中。本ラウンドの最大の構造的変化は [H-GOV-001](../config/hypotheses.json) の方向転換である。

前回更新（2026-06-23）から4ラウンド経過した。H-GOV-001は54→53→52%と3ラウンド連続で-1%低下した後、v4.20（2026-06-26）で52→53%に転じ、v4.21（2026-06-27）で53→54%に至った。方向転換の触媒はPentagon標的選定ドクトリン改訂 [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018)（A-2）である。この改訂は、政府がAIを単なる規制対象としてではなく、軍事標的設定に広く関与する手段として位置付けたことを示す。Operation Epic Fury（96h/2,000標的）が個別実験であったのに対し、ドクトリン改訂は構造的実践への制度化を意味する。先例確立の第2核心要件（実効性）に直結する質的新次元である。政府の介入能力がAnthropic規制にとどまらず、AIの積極的軍事活用に拡大したことで、政府圧力の先例確立というH-GOV-001の核心命題の妥当性が強化された。

同時に、Anthropic Q2営業利益$559M・ARR $47B [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043)（A-2）は、介入の実効性に疑問を呈す証拠である。政府がSCR指定・連邦使用停止・輸出管理指令・DOJ提訴を行使しても、Anthropicが営業利益を記録する規模に成長したことは「先例確立≠実効性確認」の不均衡を示す。但しDEGRADED状態では、このI方向証拠の質的再解釈（先例確立の実効性再定義）は保留された。54%はC方向の質的新次元とI方向の商業的成功の間の暫定均衡である。

DOJ法廷文書 [INFO-006](../Information/2026-06-27/collected-raw.md#INFO-006)（A-2）は、政府の法的追求が継続していることを示すC方向証拠である。SCR指定に関連する法的手続きが進行中であり、判事Rita Linの法院令 [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046)（A-2）による一時阻止の帰趗が確定していない。介入能力の拡大（C蓄積）は12件に達した。

[H-ANT-002](../config/hypotheses.json) は62→58%（4ラウンド連続-1%）。Claude Code DAU/日常利用者データ8R連続不在がI方向の主要因である。企業LLM支出シェア40%（Menlo Ventures [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) B-3）・Anthropic AI 80%自コード生成 [INFO-049](../Information/2026-06-27/collected-raw.md#INFO-049)（B-2）はC方向だが、DAU不在の定量欠損が上回る。medium→low移行はv4.16（4R連続到達）から検討中だが、DEGRADED制約でRed交差検証後に保留されている。8R連続到達で移行条件は倍化した。58%はFable 5 #1・Opus 4.8 SWE-bench #1技術リーダーシップへの依存が深まっている。Fable 5/Mythos 5アクセス停止が継続（6日目）し、技術リーダーシップの活用可能性が制限されている。

[H-ANT-001](../config/hypotheses.json) は37%で±0%維持。Kano再定式化後の上限条件未達成が継続する。企業LLM支出シェア40%はAnthropicの企業市場での地位を示すが、安全性が選択理由かコスト性能かの判別はA-2品質で未確認である。[H-GOV-002](../config/hypotheses.json) は21%で±0%維持。業界全体萎縮効果の定量証拠は不在のままである。[H-CAR-002](../config/hypotheses.json) は70%で±0%維持。[H-CAR-003](../config/hypotheses.json) は58%で±0%維持。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Pentagon標的選定ドクトリン改訂: AIが軍事標的設定に広く関与する道を開放 | [H-GOV-001](../config/hypotheses.json) C方向・質的新次元。方向転換の触媒。先例確立第2核心要件（実効性）に直結。[IND-030](../config/indicators.json) critical文脈 | A-2 | [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) |
| 高 | Anthropic Q2営業利益$559M・ARR $47B | [H-GOV-001](../config/hypotheses.json) I方向（先例確立≠実効性確認）。[H-ANT-002](../config/hypotheses.json) C方向（商業的成功） | A-2 | [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) |
| 高 | 企業LLM支出シェアAnthropic 40%（OpenAI 27%・Google 21%） | [H-ANT-002](../config/hypotheses.json) C方向。企業市場での支配的地位。Menlo Ventures | B-3 | [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) |
| 高 | DOJ法廷文書・SCR指定関連の法的手続き継続 | [H-GOV-001](../config/hypotheses.json) C方向。政府の法的追求が継続。C蓄積12件 | A-2 | [INFO-006](../Information/2026-06-27/collected-raw.md#INFO-006) |
| 高 | Anthropic AI 80%自コード生成・RSI具体化 | [IND-028](../config/indicators.json) RSI。[H-ANT-002](../config/hypotheses.json) C方向（自社でのClaude Code実証） | B-2 | [INFO-049](../Information/2026-06-27/collected-raw.md#INFO-049) |
| 高 | Claude Code DAU/日常利用者データ8R連続不在 | [H-ANT-002](../config/hypotheses.json) I方向。medium→low移行条件倍加・DEGRADED制約で保留 | (内部) | [arbiter-2026-06-27](../state/arbiter-2026-06-27.md) |
| 高 | 判事Rita Lin「違法な報復」判断・法院令でAnthropic連邦禁止阻止 | [H-GOV-001](../config/hypotheses.json) I方向。政府介入の持続性への最初のA-2否定的証拠 | A-2 | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) |
| 高 | 全連邦政府Anthropic使用停止命令・SCR指定（Huawei級・米国企業初） | [H-GOV-001](../config/hypotheses.json) C方向。(a)分割後の中核証拠。但しRita Lin判事が「違法な報復」と判断 | A-2 | [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) |
| 高 | Google最大$40B投資・Anthropic $1T評価+Jumper移籍 | [H-GOV-001](../config/hypotheses.json) I方向。民間資本が政府圧力を上回る勢い | B-2 | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| 高 | Claude Code採用3%→24%（米国）・JetBrains 1万人調査 | [H-ANT-002](../config/hypotheses.json) C方向。DAU/日常利用者データは8R連続不在 | B-3 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) |
| 高 | CVE-8.7 CVSS 8.7 RCE脆弱性がClaude Codeで発見 | [H-ANT-001](../config/hypotheses.json) I方向。安全性差別化企業の主力製品のRCE | A-3 | [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) |
| 中 | 商務省がFable 5/Mythos 5全外国人アクセス禁止（輸出管理指令） | [H-GOV-001](../config/hypotheses.json) C方向A-1品質。政府介入の具体的手法 | A-1 | [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) |
| 中 | トークンコスト$30→<$1/MTok（2023年初→2026年6月） | SCN-004 コモディティ化C蓄積。围い込み価値の侵食圧力 | A-3 | [INFO-025](../Information/2026-06-10/collected-raw.md#INFO-025) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| [H-GOV-001](../config/hypotheses.json) が60%を超える | 方向転換が構造的トレンドと確認される。介入効果の実効性解釈が強化 | 180日 | [H-GOV-001](../config/hypotheses.json) |
| [H-GOV-001](../config/hypotheses.json) が45%を割る | 先例確立仮説が棄却水準に接近する。方向転換が一時的と判定 | 180日 | [H-GOV-001](../config/hypotheses.json) |
| 判事Rita Linの法院令が上訴裁判所で覆る | [H-GOV-001](../config/hypotheses.json) のI側A-2証拠が弱体化。54%から再上昇 | 180日 | [IND-030](../config/indicators.json) |
| 次回COMPLETEラウンドでH-ANT-002 medium→low移行が実施される | DAU 8R連続不在で移行条件倍加。ラベル変更確定 | 次回 | [H-ANT-002](../config/hypotheses.json) |
| Fable 5/Mythos 5のアクセス停止が60日以上継続する | [H-ANT-002](../config/hypotheses.json) 58%の技術リーダーシップ根拠が弱まる | 54日 | [IND-027](../config/indicators.json) |
| 安全性がA-2品質でエンタープライズ選択理由第1位と確認される | [H-ANT-001](../config/hypotheses.json) 上限条件解除。37%下限宣言の無効化 | 180日 | [IND-008](../config/indicators.json) |
| CVE-8.7が深刻な実被害（エンタープライズ環境での悪用確認）に至る | [H-ANT-001](../config/hypotheses.json) 37%から更なる下方。[IND-013](../config/indicators.json) critical移行 | 90日 | [IND-013](../config/indicators.json) |
| SCR指定が恒久化し上訴裁判所も合憲と判断する | [H-GOV-001](../config/hypotheses.json) 54%から再上昇。政府介入の不可逆化 | 180日 | [IND-030](../config/indicators.json) |
| エンタープライズ解約率が二桁に達する | 収益基盤（80%エンタープライズ依存）の前提が崩れる | 90日 | [IND-008](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性の制度化は差別化の消失ではなく次元の変化を意味し、規制捕獲戦略の側面も評価が必要 | 37% (low) | ±0%。Kano再定式化実行済み。企業LLM支出シェア40%(INFO-008 B-3)は企業市場地位を示すが安全性選択理由かの判別不能。CVE-8.7継続的矛盾。並存≠因果継続 | [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) [INFO-047](../Information/2026-06-15/collected-raw.md#INFO-047) [INFO-054](../Information/2026-06-15/collected-raw.md#INFO-054) | [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDKで開発者市場を取る | 58% (medium) | -4%（62→58%・4R連続-1%）。Claude Code採用24%(INFO-012 B-3)・企業LLM支出シェア40%(INFO-008 B-3)・AI 80%自コード(INFO-049 B-2)のC蓄積だが、DAU/日常利用者データ8R連続不在(v4.16条件到達から倍加)がI方向。medium→low移行検討・DEGRADED制約でラベル変更保留。58%はFable 5 #1・Opus 4.8 SWE-bench #1に依存 | [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) [INFO-049](../Information/2026-06-27/collected-raw.md#INFO-049) [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) | [arbiter-2026-06-27](../state/arbiter-2026-06-27.md) [INFO-010](../Information/2026-06-15/collected-raw.md#INFO-010) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% (low) | ±0%。棄却候補継続。Google $40B投資でインフラ二重集中更に加速 | (該当なし) | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-003](../Information/2026-06-10/collected-raw.md#INFO-003) |
| [H-GOV-001](../config/hypotheses.json) | 政府が経済的手段でAnthropicの安全性姿勢に圧力をかける先例が確立された。(a)命題に特化。(b)はH-GOV-002として分離 | 54% (medium) | ±0%（54→53→52→53→54%・方向転換）。Pentagon標的選定ドクトリン改訂(INFO-018 A-2)が質的新次元・先例確立第2核心要件（実効性）に直結。DOJ法廷文書(INFO-006 A-2)でC蓄積12件。Anthropic Q2 $559M利益(INFO-043 A-2)はI（先例確立≠実効性確認）だがDEGRADEDで解釈変更保留。2R連続+1%で方向転換確認 | [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) [INFO-006](../Information/2026-06-27/collected-raw.md#INFO-006) [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| [H-GOV-002](../config/hypotheses.json) | 政府のAnthropic圧力先例がAI業界全体に波及し、順応報酬構造を通じて安全性研究の戦略的価値が構造的に低下する | 21% (low) | ±0%。絶対条件（他社安全性方針定量変化データ）20R連続未達成。Pentagon標的ドクトリン改訂で順応報酬構造の妥当性は強化だが、業界全体への波及は定量証拠不在 | [INFO-051](../Information/2026-06-17/collected-raw.md#INFO-051) [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) | [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) |
| [H-CAR-001](../config/hypotheses.json) | AI業務自律化が3年以内に中堅企業の業務プロセスを30%以上自動化し、中間層雇用が大幅に削減される | 36% (low) | ±0%。「79%導入」≠「30%自動化達成」の定義ギャップ未解決 | [INFO-020](../Information/2026-06-10/collected-raw.md#INFO-020) | [INFO-028](../Information/2026-06-10/collected-raw.md#INFO-028) |
| [H-CAR-002](../config/hypotheses.json) | AIコーディングツール普及で「書く能力」の価値が変容し、「設計・評価・方向付けする能力」の価値が上昇する | 70% (medium) | ±0%。ステートメント修正実行済み。METR 43%本番破損が上限制約として継続。Anthropic AI 80%自コード(INFO-049)で支持強化 | [INFO-029](../Information/2026-06-10/collected-raw.md#INFO-029) [INFO-049](../Information/2026-06-27/collected-raw.md#INFO-049) | (METR 43%本番破損) |
| [H-CAR-003](../config/hypotheses.json) | バリューチェーン中間工程のビジネス職は3年以内に大規模再編され、価値は上流と下流に集中する | 58% (medium) | ±0%。方向性支持・速度不確定 | [INFO-024](../Information/2026-06-10/collected-raw.md#INFO-024) [INFO-023](../Information/2026-06-10/collected-raw.md#INFO-023) | [INFO-056](../Information/2026-05-28/collected-raw.md#INFO-056) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | 企業LLM支出シェア40%（Menlo）。Q2営業利益$559M/ARR $47B。high/rising | 2026-06-27 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 大規模インシデントで critical | CVE-8.7はI重み「高」。新規A-2実被害なし。high/rising | 2026-06-27 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」検証突破で elevated→high | Fable 5/Mythos 5アクセス停止継続・Seedance 2.5・ARC-AGI-2 Seed 2.1 Pro 0.625。量的向上継続。「真の理解」未解決。elevated/stable | 2026-06-27 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達で high | 期待-実態ギャップ構造的継続。high/rising | 2026-06-27 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 全主要プレイヤー採用で high | Agent SDK プロバイダ非依存・標準化加速。Fable 5/Mythos 5アクセス停止で利用制限。high/rising | 2026-06-27 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | 広範なタスクでのRSI再現・外部検証で critical | Anthropic AI 80%自コード生成=RSI具体化(INFO-049 B-2)。CEO3氏AGI 5-10年合意。high/rising | 2026-06-27 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 | 資本流入 vs 物理制約で high | $725B資本支出予測・Google $40B投資・Anthropic $1T評価。資本流入加速確定的。high/rising | 2026-06-27 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | （critical到達済み） | **critical/rising**。Pentagon標的選定ドクトリン改訂・DOJ法廷文書・OpenAI機密環境AI配備契約。軍事AIがドクトリンに組込まれた。条件2（A-2技術的安全事故）は未到達。判事Rita Lin判断・Gillibrand法案・DeepMind AI Control Roadmapは緩和要因 | 2026-06-27 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-27 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 54% ±0%（方向転換: 54→53→52→53→54%・3R連続-1%後2R連続+1%）。[H-ANT-002](../config/hypotheses.json) 62→58%（4R連続-1%・DAU 8R連続不在）。Pentagon標的選定ドクトリン改訂（[INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) A-2）・Anthropic Q2 $559M利益（[INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) A-2）・企業LLM支出シェア40%（[INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) B-3）を反映。全§5最終確認日更新 | [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) [INFO-006](../Information/2026-06-27/collected-raw.md#INFO-006) [INFO-049](../Information/2026-06-27/collected-raw.md#INFO-049) | H-GOV-001 54%（方向転換）・H-ANT-002 62→58% |
| 2026-06-23 | 全面書き直し。Google最大$40B投資報道・Anthropic $1Tセカンダリ+Jumper移籍・NSF予算削減を反映。[H-GOV-001](../config/hypotheses.json) 56→54%（2R連続-1%）。[H-ANT-002](../config/hypotheses.json) 64→62%（DAU 4R連続不在・medium→low移行検討起動）。[H-CAR-003](../config/hypotheses.json) 57→58% | [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) | H-GOV-001 56→54%・H-ANT-002 64→62%・H-CAR-003 57→58% |
| 2026-06-21 | 全面書き直し。[H-GOV-001](../config/hypotheses.json) 58→56%（判事Rita Lin「違法な報復」判断 A-2）。[H-ANT-002](../config/hypotheses.json) 65→64%。[IND-030](../config/indicators.json) high→critical | [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | H-GOV-001 58→56%・H-ANT-002 65→64%・IND-030 high→critical |
| 2026-06-17 | H-GOV-001(a)/(b)分割実行。(a)39→55% low→medium・(b)H-GOV-002新規20% low | 2026-06-17複数INFO | H-GOV-001 39→55%・H-GOV-002新規20% |
| 2026-06-15 | H-ANT-001 ±0%(37%)・Kano再定式化実行・ステートメント更新 | 2026-06-15複数INFO | |

## 7. ブラインドスポット

- [H-GOV-001](../config/hypotheses.json) 54%は方向転換直後の暫定均衡である。Pentagon標的選定ドクトリン改訂（質的新次元・C方向）とAnthropic Q2 $559M利益（先例確立≠実効性確認・I方向）の力関係が次回COMPLETEラウンドでRed交差検証される。方向転換が持続的か一時的かの判別は今後2-3ラウンドが必要。
- Pentagon標的選定ドクトリン改訂がH-GOV-001に与える影響の解釈が二項対立的である。「政府のAI活用拡大＝介入能力の強化」（C方向）と「政府のAI活用拡大≠Anthropic安全性姿勢への圧力」（I方向）のいずれが妥当か、DEGRADED制約で保留中。
- Anthropic Q2営業利益$559Mが政府介入の無効性を示すのか、介入がまだ効果発現前であることを示すのかの判別が不能。政府の法的手段（SCR指定・DOJ提訴）の帰趗が確定していない段階での営業利益は、介入効果の最終評価材料として不十分。
- [H-ANT-002](../config/hypotheses.json) 58%は過渡期の値。DAU 8R連続不在でmedium→low移行条件が倍加した。次回COMPLETEラウンドでのRed交差検証後にラベル変更が実施される可能性が高い。58%と45%（medium/low境界）の距離が縮小している。
- Fable 5/Mythos 5アクセス停止が6日目。技術リーダーシック（Fable 5 #1・Opus 4.8 SWE-bench #1）の活用可能性が制限されたままである。停止が長期化すればH-ANT-002 58%の維持根拠が弱まる。
- 企業LLM支出シェア40%（Menlo Ventures）が単一ソースである。Anthropicが企業市場で支配的である事実はC方向だが、安全性選択理由かコスト性能かの判別がA-2品質で未確認。
- Google $40B投資は「最大$40B」であり最終額が未確定。Google自身がGeminiを展開する中での競合大型投資の戦略的意図の判別が不完全。
- CVE-8.7が未解決であり、安全性差別化仮説に継続的な矛盾を提示する。
- IPO S-1秘密提出は情報開示の機会だが、安全性研究への資金コミットメントがIPO自己選択バイアスか真のコミットメントかの判別が困難。
- 判事Rita Linの判断が「政府介入=違法」を意味するのか「手続き的瑕疵」を意味するのかの技術的判別が不完全。前者ならH-GOV-001の前提そのものが揺らぐ。後者なら手続きの修正で政府の介入権限自体は維持される。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-018](../Information/2026-06-27/collected-raw.md#INFO-018) | Pentagon標的選定ドクトリン改訂・AIが軍事標的設定に広く関与(A-2) |
| [INFO-043](../Information/2026-06-27/collected-raw.md#INFO-043) | Anthropic Q2営業利益$559M/ARR $47B(A-2) |
| [INFO-008](../Information/2026-06-27/collected-raw.md#INFO-008) | 企業LLM支出シェアAnthropic 40%・OpenAI 27%(B-3) |
| [INFO-006](../Information/2026-06-27/collected-raw.md#INFO-006) | DOJ法廷文書・SCR指定関連法的手続き継続(A-2) |
| [INFO-049](../Information/2026-06-27/collected-raw.md#INFO-049) | Anthropic AI 80%自コード生成・RSI具体化(B-2) |
| [Arbiter v4.21](../state/arbiter-2026-06-27.md) | H-GOV-001方向転換確認・H-ANT-002 58%・DEGRADED 2R連続 |
| [INFO-045](../Information/2026-06-23/collected-raw.md#INFO-045) | Google最大$40B Anthropic投資報道(B-2) |
| [INFO-066](../Information/2026-06-23/collected-raw.md#INFO-066) | Anthropic $1Tセカンダリ/Jumper移籍・NSF予算削減(B-2) |
| [INFO-031](../Information/2026-06-23/collected-raw.md#INFO-031) | DPA行使検討(B-2) |
| [INFO-046](../Information/2026-06-21/collected-raw.md#INFO-046) | 判事Rita Lin「違法な報復」判断・Fable 5/Mythos 5アクセス停止(A-2) |
| [INFO-054](../Information/2026-06-21/collected-raw.md#INFO-054) | 輸出管理指令全容(A-1) |
| [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) | Grok Gov Model Operation Epic Fury 96h/2,000標的(A-2) |
| [INFO-012](../Information/2026-06-19/collected-raw.md#INFO-012) | Claude Code採用3%→24%(B-3) |
| [INFO-043](../Information/2026-06-17/collected-raw.md#INFO-043) | 全連邦政府Anthropic使用停止・SCR指定(A-2) |
| [INFO-001](../Information/2026-06-14/collected-raw.md#INFO-001) | Fable 5/Mythos 5 SOTA維持(A-3) |
| [INFO-034](../Information/2026-06-10/collected-raw.md#INFO-034) | CVE-8.7 CVSS 8.7 RCE脆弱性(A-3) |
