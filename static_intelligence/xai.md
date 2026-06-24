# xAI → SpaceXAI

> 最終判断更新: 2026-06-24
> 全体確信度: 低
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Colossus貸与条件・Cursor統合の詳細・Grok Gov Modelのガードレール内容も非公開。DL/API呼び出し量の時系列データも途絶状態
> 主参照: [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

SpaceXAIは基盤モデル（Grok）+コーディング（Cursor）+軍事（Operation Epic Fury・$200M契約）+インフラ（Colossus 2）の垂直統合を完了した。SpaceXがCursor（Anysphere）を$60B全株式で買収し [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041)（A-1）、xAIが$20B Series Eを完了した [INFO-044](../Information/2026-06-24/collected-raw.md#INFO-044)（B-2）。SpaceX複合企業の評価額は$1.25兆に達し、世界最高値の非公開企業となった。SCN-005「地政学的AI市場分裂」の第1ブロックとして位置づけられた [scenarios.json](../config/scenarios.json)。

ただし二つの構造的圧力が観測された。第一にDeepSeek V3.2がGrok 4 Fastの大半のベンチマークで勝利し [INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045)（B-2）、1.1倍安価に動作する。Grokの性能優位が中国OSSモデルに侵食されている。第二にYann LeCunがxAIを「失敗」と呼び [INFO-051](../Information/2026-06-24/collected-raw.md#INFO-051)（B-2）、AMI Labs（$1.03B）を設立してLLM限定アプローチからの脱却を主張した。[IND-030](../config/indicators.json)（能力-リスク二面性）はcritical/risingを維持する。Operation Epic FuryでGrok Gov Modelが96時間・2,000標的・2,000発の弾薬展開を担った事実 [INFO-033](../Information/2026-06-24/collected-raw.md#INFO-033)（B-1）は、LLMがキルチェーンに組み込まれた初の文書化事例だからだ。

[H-XAI-004](../config/hypotheses.json)（汎用AI基盤としてエンタープライズ獲得）は55%から57%に上方修正された。SpaceX Cursor $60B買収（A-1）の事実の確定性が高い一方で、核心命題（Grok有機的エンタープライズ採用・X非依存）への診断的適合度は3重の概念飛躍（M&A≠adoption・Cursor価値はClaude/GPT由来・X非依存に無関係）を含む。availability≠adoptionの確証バイアス警告を継続する。もしCursor統合後にGrok系コーディングツール採用が定量で回復せず、DL減少傾向が3ヶ月以上継続し、Gillibrand法案が可決される、のいずれかが観測されたら判断を見直す。

## 1. コア判断

確信度は低のまま置く。垂直統合の外観は完成したが、SpaceXAIの内部戦略とCursor統合の結果が外部から読めない。観測根拠は蓄積するが、エンタープライズ採用という核心課題が解消していない。

二つの軸に沿って組織が再編された。一つはコーディングエージェントの軸で、SpaceXがCursorを$60B全株式で買収した（[INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) A-1）。取引の事実確定性は極めて高い。Grok Buildの/goal機能（[INFO-009](../Information/2026-06-24/collected-raw.md#INFO-009) A-3）とVoice Agent API（[INFO-015](../Information/2026-06-24/collected-raw.md#INFO-015) A-3）は、コーディングエージェントの自律化を進める。Grok on Databricks・Amazon Bedrock GA・Grok for Word（[INFO-010](../Information/2026-06-24/collected-raw.md#INFO-010) A-3）は、エンタープライズAPI到達範囲を拡大する。

もう一つは国家安保基盤の軸で、Grok Gov Modelがイラン作戦で標的選定から弾薬展開までのワークフローを担った（[INFO-033](../Information/2026-06-24/collected-raw.md#INFO-033) B-1）。DoD CDAO Cameron Stanleyは宣誓陳述書で「他のフロンティアAIモデルに見られない独自機能」と記した。xAIの軍事システム統合契約は最大$200Mに達し（[INFO-034](../Information/2026-06-24/collected-raw.md#INFO-034) B-2）、DoJ準備書面がxAI統合を確認した。Anthropicが大規模監視と完全自律兵器の使用を拒否しサプライチェーンリスク指定を受けた（[INFO-061](../Information/2026-06-24/collected-raw.md#INFO-061) B-2）のと対照的に、xAIは即座に軍事統合を受け入れた。順応報酬構造の具体化である。

[IND-030](../config/indicators.json) がcritical/risingを維持する根拠は三つある。第一に、Operation Epic Furyは軍事AIが「個別実験」から「構造的実践」に相転移した初の事象であり、96時間で2,000標的に対するテンポは設計通りの利用と技術的安全リスクの境界を実質的に消滅させる。第二に、DPA行使が検討され（[INFO-031](../Information/2026-06-24/collected-raw.md#INFO-031) B-2）、政府がAI企業にサービス提供を強制する可能性が示唆された。第三に、Sen. GillibrandがLLMを人間監視なしで武力行使に使用することを禁止する法案を提出し、立法府が最高警戒レベルで認識している。ただし条件2（A-2品質技術的安全事故報告）は未到達で、Grok AIの標的選定への直接関与度（KIQ-MIL-001）は未確定である。

二つの構造的圧力を記録する。第一に、DeepSeek V3.2がGrok 4 Fastの大半のベンチマークで勝利した（[INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) B-2）。これは[H-XAI-002](../config/hypotheses.json)（価格競争力）の前提である「Grokが低価格で優位」を直接侵食する。中国OSSモデルが同等性能で極低価格を維持する中、Grokの価格優位性自体が希薄化している。第二に、LeCunがxAIを「失敗」と呼び、AMI Labs（$1.03B）を設立した（[INFO-051](../Information/2026-06-24/collected-raw.md#INFO-051) B-2）。LLMではAGIに至れないという4年間の主張が$1.03Bで資金化された。xAIのLLM中心アプローチに対する学術的懐念の象徴である。

商用面では、買収対象のCursor自身がRamp支出データで市場シェアを2025年6月の41%から2026年5月の約26%に落とし、コーディングカテゴリの半数をAnthropicに奪われている [INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061)。$60Bで買った資産が、買収時点ですでに下落坂にある。[H-XAI-002](../config/hypotheses.json) は59%のまま、[H-XAI-004](../config/hypotheses.json) は55%から57%に上方修正された。エンタープライズ市場での採用という核心課題は解消していない。性能とエンタープライズ採用の乖離が構造課題として残る。[H-XAI-001](../config/hypotheses.json)（Xデータ差別化）と [H-XAI-003](../config/hypotheses.json)（宇宙・製造業特化）は引き続き棄却（35%）で、新たな支持証拠は観測されていない。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | SpaceXがCursorを$60B全株式で買収。SpaceX複合企業評価額$1.25兆（世界最高値非公開企業） | コーディングエージェント軸への再編。[H-XAI-004](../config/hypotheses.json) の+2%の主根拠。但しM&A≠adoptionの概念飛躍 | A-1 | [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) |
| 高 | Grok Gov ModelがOperation Epic Furyで96時間以内に2,000標的に2,000発以上展開（3独立ソース確認） | [IND-030](../config/indicators.json) critical/rising維持の核心証拠。軍事AI相転移（実験→実戦制度化） | B-1 | [INFO-033](../Information/2026-06-24/collected-raw.md#INFO-033) |
| 高 | xAI軍事システム統合契約最大$200M・DoJ準備書面確認 | 国家安保基盤軸の制度化。Anthropic拒否 vs xAI即時受諾の対比。順応報酬構造の具体化 | B-2 | [INFO-034](../Information/2026-06-24/collected-raw.md#INFO-034) |
| 高 | DeepSeek V3.2がGrok 4 Fastの大半のベンチマークで勝利（1.1倍安価） | [H-XAI-002](../config/hypotheses.json) のI。Grok性能優位の侵食。価格コモディティ化で独自性希薄化 | B-2 | [INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) |
| 高 | Cursor市場シェア41%(2025-06)→26%(2026-05)、Anthropicがカテゴリ半数掌握（Ramp支出データ） | 買収対象が下落坂。[H-XAI-004](../config/hypotheses.json) の矛盾材料。availability≠adoption | A-2 | [INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061) |
| 高 | xAI $20B Series E完了（Q1 2026最大メガディール） | 資本規模の拡大。地政学的ブロック形成の加速 | B-2 | [INFO-044](../Information/2026-06-24/collected-raw.md#INFO-044) |
| 高 | LeCun「xAIは失敗」・AMI Labs設立$1.03B・LLM→AGI不可説4年主張の資金化 | xAIのLLM中心アプローチに対する学術的懐念。AGI到達アプローチの多様化 | B-2 | [INFO-051](../Information/2026-06-24/collected-raw.md#INFO-051) |
| 中 | Grok Build /goal自律実行・Voice Agent API・Grok on Databricks/Bedrock GA | 製品幅の拡大。エンタープライズ到達範囲の拡大。但し採用の定量的裏付け不在 | A-3 | [INFO-009](../Information/2026-06-24/collected-raw.md#INFO-009) [INFO-015](../Information/2026-06-24/collected-raw.md#INFO-015) [INFO-010](../Information/2026-06-24/collected-raw.md#INFO-010) |
| 中 | Anthropic倫理制限削除拒否・ペンタゴン関係切断・サプライチェーンリスク指定 | 競合排除構造の具体化。Anthropic排除→xAI選別の政府チャネル獲得 | B-2 | [INFO-061](../Information/2026-06-24/collected-raw.md#INFO-061) [INFO-029](../Information/2026-06-24/collected-raw.md#INFO-029) |
| 中 | DL 60%減（1月20M→4月8.3M）未解決 | 価格競争力仮説の停滞。59%以下でmedium→low審査トリガー | B-2 | [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Gillibrand法案（人間監視なしLLM使用禁止）が可決・成立する | 軍事利用の制度化フレームが変わり、国家安保基盤軸の前提が変わる | 180日 | [IND-030](../config/indicators.json) |
| 技術的安全事故（Agent暴走・誤目標）が軍事領域でA-2品質で報告される | [IND-030](../config/indicators.json) の制約（条件2未到達）が解消され、リスク評価が全面改訂される | 180日 | [IND-030](../config/indicators.json) |
| KIQ-MIL-001（Grok AIの標的選定関与度）が回答される | ミナブ攻撃とAI標的特定の因果関係が確定・否認のいずれかで確定する | 90日 | [IND-030](../config/indicators.json) |
| Cursor統合後にGrok系コーディングツールの採用（DL/API呼び出し量）が定量で回復する | [H-XAI-004](../config/hypotheses.json) のエンタープライズ獲得読みが上方修正される。90日で回復しなければ読みは弱まる | 90日 | [IND-027](../config/indicators.json) |
| DL減少傾向が3ヶ月以上継続する | [H-XAI-002](../config/hypotheses.json) の59%根拠が崩れ、medium→low移行が確定する | 90日 | [IND-013](../config/indicators.json) |
| DeepSeek等中国OSSモデルがGrok全系で全面的に勝利する | [H-XAI-002](../config/hypotheses.json) 価格競争力仮説の前提が崩壊する | 90日 | [IND-025](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-XAI-002](../config/hypotheses.json) | 価格競争力でシェアを獲得する | 59% medium | ±0%。Grok 4.3入力$1.25M/MTok・Grok Build $1/MTok・Databricks/Bedrock GAは低価格C。但しDeepSeek V3.2がGrok 4 Fast大半で勝利し1.1倍安価。DL 60%減未解決。API価格95%+下落で「低価格」の独自性が薄れる。59%以下が続けば次ラウンドでmedium→low審査 | [INFO-010](../Information/2026-06-24/collected-raw.md#INFO-010) [INFO-009](../Information/2026-06-24/collected-raw.md#INFO-009) | [INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) [INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061) |
| [H-XAI-004](../config/hypotheses.json) | 汎用AI基盤としてエンタープライズ市場を獲得する | 57% medium | +2%（55→57%・2R連続+1%）。SpaceX Cursor $60B買収はA-1品質で事実の確定性が高い。コーディング+軍事+インフラ垂直統合完了。但し核心命題（Grok有機的エンタープライズ採用・X非依存）への診断的適合度は3重の概念飛躍（M&A≠adoption・Cursor価値はClaude/GPT由来・X非依存に無関係）。availability≠adoption→M&A≠adoptionの基準引き下げ警告 | [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) [INFO-010](../Information/2026-06-24/collected-raw.md#INFO-010) [INFO-034](../Information/2026-06-24/collected-raw.md#INFO-034) | [INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061) [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| [H-XAI-001](../config/hypotheses.json) | （棄却）Xデータ活用でリアルタイム特化を差別化する | 35% | 40R以上にわたりXデータ活用の直接証拠不在。xAI→SpaceXAI統合で観測の意義自体が低下 | （なし） | 40R以上の証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | （棄却）SpaceX統合で宇宙・製造業特化AIを展開する | 35% | 41R以上にわたり直接的特化AI製品証拠不在。Colossusは汎用インフラ扱い | （なし） | 41R以上の特化製品証拠不在 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度・Grok API/DL動向 | 実被害A-2報告でcritical | high/rising。Grok Gov Model稼働。新規A-2脆弱性報告なし。DL 60%減は未解決 | 2026-06-24 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」の検証 | elevated/stable。Grok 4.3最低ハルシネーション率。但しDeepSeek V3.2が大半で勝利。量的向上継続 | 2026-06-24 |
| [IND-026](../config/indicators.json) | エージェント本番到達率 | 3ソース以上で完了率<10% | high/rising。Kore.ai: 72%管理外リスク・79%取消・42%収益損失。Cursor統合後の本番到達は未計測 | 2026-06-24 |
| [IND-027](../config/indicators.json) | エコシステム標準化・Grokスタック採用 | 围い込み反転 | high/rising。Grok 4.3 Databricks/Bedrock GA・/goal・Voice Agent API。1000+スキルでCursor対応 | 2026-06-24 |
| [IND-028](../config/indicators.json) | AGI到達度 | 主観-客観乖離 | high/rising。LeCun AMI Labs設立でLLM→AGI不可説が資金化。xAI固有のAGI宣言は今ラウンド不在 | 2026-06-24 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 物理的制約の顕在化 | high/rising。Colossus 2「国家安保不可欠」。SpaceX $1.25兆+Cursor $60B+xAI $20B。資本流入加速 | 2026-06-24 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 | （critical到達済み） | **critical/rising**。Operation Epic Fury 96h/2,000標的で軍事AI相転移。DPA検討・Anthropic倫理制限削除拒否・Gillibrand法案。条件2（A-2技術的安全事故）は未到達 | 2026-06-24 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-24 | 全面書き直し。SpaceX Cursor $60B買収のA-1品質確定（[INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041)）。xAI $20B Series E・軍事$200M契約・DeepSeek V3.2 > Grok 4 Fast・LeCun「xAI失敗」AMI Labs設立・Grok Build /goal・Voice Agent API・Databricks/Bedrock GAを反映。[H-XAI-004](../config/hypotheses.json) 55→57%（+2%・2R連続+1%）。SCN-005第1ブロックとして位置づけ。[H-XAI-002](../config/hypotheses.json) 59%据え置き | [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) [INFO-044](../Information/2026-06-24/collected-raw.md#INFO-044) [INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) [INFO-051](../Information/2026-06-24/collected-raw.md#INFO-051) | H-XAI-004 55→57%・H-XAI-002 59%据え置き |
| 2026-06-21 | 全面書き直し。[IND-030](../config/indicators.json) high→critical移行。Operation Epic Fury A-2品質確定・DoD CDAO宣誓陳述書 A-1・ミナブ小学校168人死亡を反映。仮説確度は据え置き | [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) [INFO-053](../Information/2026-06-21/collected-raw.md#INFO-053) | IND-030 high→critical・H-XAI-002 59%・H-XAI-004 55%据え置き |
| 2026-06-18 | 全面書き直し。SpaceX-Cursor $60B買収・Grok 4.3 GA・Grok Gov Model軍事展開を二軸再編として反映 | [INFO-054](../Information/2026-06-18/collected-raw.md#INFO-054) | H-XAI-002 59%・H-XAI-004 55%据え置き |
| 2026-06-11 | Gopuff Go・Grok Imagine 1.5・Vapi統合・Composer 2.5・Grok Build 0.1 APIで製品幅拡大反映 | 2026-06-11複数INFO | H-XAI-002 59%・H-XAI-004 55%据え置き |
| 2026-05-28 | Grok Build正式リリース・DL 60%減・$20B Series E・API価格95%+下落・Grok 4.1 97.8%反映 | 2026-05-28複数INFO | |
| 2026-05-14 | [H-XAI-001](../config/hypotheses.json)/[H-XAI-003](../config/hypotheses.json) 正式棄却 + Grok 5製品連続リリース + Colossus Anthropic提携反映 | 2026-05-14複数INFO | |

## 7. ブラインドスポット

- SpaceXAIの内部戦略が外部から観測不能。Cursor買収（$60B）とGrok軍事展開は観測できても、SpaceX本体の投資判断なのかSpaceXAI内部の戦略なのか、Colossus 2の軍民分担はどうなっているかが判別不能。
- Cursor統合の成果が測れない。買収はQ3 2026クローズ予定で、統合後のGrok-Cursor連携、コーディング採用の回復、DL回復はすべて未計測。買収時点でCursorがシェア26%に下落中という出発点の悪さも未消化。
- DeepSeek V3.2がGrok 4 Fastの大半で勝利した事実が[H-XAI-002](../config/hypotheses.json)（価格競争力）の前提を直接侵食している。Grokの「低価格」が中国OSSモデルの極低価格に対して差別化要因として機能し得るかの定量評価がない。
- Grok Gov Modelのガードレールと人間監視の実効性が不明。宣誓陳述書は「独自機能」と記すが、人間がどこで判断を止めたか、誤報率はどの程度かが非公開。KIQ-MIL-001（標的選定関与度）も未回答。
- 軍事利用のリスク評価で「設計通りの軍事利用」と「技術的安全事故」の区別が実質的に崩れつつある。2,000標的/96hテンポでは意味ある人間監査が物理的に困難だが、この境界の崩壊を定量的に監視する枠組みが未整備。
- [H-XAI-001](../config/hypotheses.json)/[H-XAI-003](../config/hypotheses.json) の棄却後、コーディング＋国家安保の二軸を統合する新仮説フレームが未定義。Cursor買収と軍事展開を一本の筋で説明する仮説が不在。
- LeCunのAMI Labs設立が、xAIのLLM中心アプローチに対する根本的な競争替代案を提示している。AMI Labsが成功した場合、SpaceXAI全体のAGI到達戦略の前提が問われるが、この次元の競争を追跡する指標がない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [Arbiter v4.18](../state/arbiter-2026-06-24.md) | [H-XAI-004](../config/hypotheses.json) 55→57%(+2%)。[H-XAI-002](../config/hypotheses.json) 59%据え置き。SCN-005第1ブロック確定 |
| [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) | SpaceX-Cursor $60B買収・評価額$1.25兆(A-1) |
| [INFO-044](../Information/2026-06-24/collected-raw.md#INFO-044) | xAI $20B Series E(B-2) |
| [INFO-033](../Information/2026-06-24/collected-raw.md#INFO-033) | Operation Epic Fury 96h/2,000標的/2,000発(B-1) |
| [INFO-034](../Information/2026-06-24/collected-raw.md#INFO-034) | xAI軍事$200M契約・DoJ確認(B-2) |
| [INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) | DeepSeek V3.2 > Grok 4 Fast大半・1.1倍安価(B-2) |
| [INFO-051](../Information/2026-06-24/collected-raw.md#INFO-051) | LeCun「xAIは失敗」・AMI Labs $1.03B設立(B-2) |
| [INFO-061](../Information/2026-06-24/collected-raw.md#INFO-061) | Anthropic倫理制限削除拒否・ペンタゴン関係切断(B-2) |
| [INFO-029](../Information/2026-06-24/collected-raw.md#INFO-029) | 政府8社選別契約・Anthropicサプライチェーンリスク(B-2) |
| [INFO-031](../Information/2026-06-24/collected-raw.md#INFO-031) | DPA行使検討・AI企業サービス強制示唆(B-2) |
| [INFO-009](../Information/2026-06-24/collected-raw.md#INFO-009) | Grok Build /goal自律実行・Grok 4.3 API(A-3) |
| [INFO-010](../Information/2026-06-24/collected-raw.md#INFO-010) | Grok Databricks/Bedrock GA・Wordアドイン(A-3) |
| [INFO-015](../Information/2026-06-24/collected-raw.md#INFO-015) | Voice Agent API・Hermes Agent OAuth(A-3) |
| [INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061) | Cursor 41%→26%下落・Anthropic半数掌握(A-2) |
| [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) | DL 60%減少・エンタープライズ苦戦(B-2) |
