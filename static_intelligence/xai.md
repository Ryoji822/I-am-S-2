# xAI → SpaceXAI

> 最終判断更新: 2026-06-29
> 全体確信度: 低
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Cursor統合の詳細・Grok Gov Modelのガードレール内容も非公開。DL/API呼び出し量の時系列データが途絶状態。KIQ-MIL-001は部分回答に転移したが、人間却下比率・誤標的率は依然非公開
> 主参照: [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

SpaceXAIは基盤モデル（Grok）+コーディング（Cursor）+軍事（Operation Epic Fury・$200M契約）+インフラ（Colossus 2）の垂直統合を完了した。前回更新（2026-06-24）から5日が経過し、3つの構造的変化が観測された。

第一に、KIQ-MIL-001（Grok AIの標的選定関与度）が9R連続の完全未回答から部分回答に転移した。Pentagon上級AI担当官の法廷宣誓陳述書で [INFO-004](../Information/2026-06-29/collected-raw.md#INFO-004)（B-3）、Grokがイラン作戦で2,000発以上の標的指定に使用されたことが初めて定量的に確認された。「human-in-the-loopからhuman-on-the-loopへの移行」という発言が記録され、人間の監視形態が質的に変化している。Maven Smart SystemとGrokの統合で初24時間に1,000標的が特定された [INFO-005](../Information/2026-06-29/collected-raw.md#INFO-005)（B-3）。§3反証の閾値に「KIQ-MIL-001が回答される」と明記されており、部分回答はこの閾値を部分的にトリガーする。標的選定への直接関与度は定量的に示されたが、人間却下比率・誤標的率は非公開のままである。

第二に、xAIオリジナル共同創業者11名全員が2026年3月までに退社した [INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058)（B-2）。DeepMind/OpenAI/GoogleからxAIを設立した全創業メンバーの離脱は、トップAI人材の定着不全を示す。LeCunがxAIを「一種の失敗」と評した発言の文脈で報告された。

第三に、xAIが選択的執行の受益者として位置づけられた [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067)（B-2）。GPT-5.5とClaude Fable 5/Mythos 5に同じ脆弱性が存在するにもかかわらずOpenAIには無措置である事実と並んで、xAI・OpenAI・Google・Amazon・Microsoft・Nvidiaは5月までに全社軍事協定に署名した。Anthropicが拒否してサプライチェーンリスク指定を受けたのと対照的に、xAIは順応報酬構造の受益側にある。PentagonがAnthropic Claudeの置換を目的にOpenAI・Googleのテストを開始した [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064)（B-3）は、xAIの軍事チャネルの持続性を裏付ける。

[H-XAI-002](../config/hypotheses.json) は59%（medium）で±0%維持。[H-XAI-004](../config/hypotheses.json) は57%（medium）で±0%維持。両仮説とも確度変更なし。KIQ-MIL-001の部分回答は IND-030 の文脈を強化するが、仮説確度の直接ドライバーではない。11共同創業者退社は [H-XAI-004](../config/hypotheses.json)（エンタープライズ獲得）のI方向圧力だが、±0%の範囲内に留まった。

## 1. コア判断

確信度は低のまま置く。垂直統合の外観は完成し、軍事統合の深度は前回更新から更に増した。だがSpaceXAIの内部戦略とCursor統合の結果が外部から読めない。エンタープライズ採用という核心課題が解消していない。

KIQ-MIL-001の部分回答は、本ラウンドの最大の構造的変化である。Pentagon上級AI担当官の宣誓陳述書（[INFO-004](../Information/2026-06-29/collected-raw.md#INFO-004) B-3）で、Grokがイラン作戦で2,000発以上の標的指定に使用されたことが定量的に確認された。9R連続で「完全未回答」だったKIQが、部分回答に転移した。前回の [INFO-033](../Information/2026-06-24/collected-raw.md#INFO-033)（B-1）がOperation Epic Furyの事実を記録していたのとは異なり、今回の新規要素は3つある。第一に、法廷宣誓陳述書という公的制度文脈での確認である。第二に、「human-in-the-loopからhuman-on-the-loopへの移行」という発言が明示的に記録されたことである。human-in-the-loopが各判断に人間が介在する枠組みであるのに対し、human-on-the-loopは人間が監視しつつ介入せず、AIの判断を実行に委ねる枠組みである。第三に、Maven Smart System（Project Maven由来・Palantir運営）とGrokの統合が確認され（[INFO-005](../Information/2026-06-29/collected-raw.md#INFO-005) B-3）、初24時間で1,000標的が特定された。衛星画像・レーダー・信号情報の統合プラットフォーム上でGrokが標的特定に寄与した。ただし、Grokが標的を提案して人間が承認したのか、Grokが直接標的を決定したのかの区別は依然として不明である。人間却下比率・誤標的率も非公開である。

11共同創業者全員の退社は、xAIの組織基盤に対する構造的懸念である（[INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058) B-2）。DeepMind/OpenAI/GoogleからxAIを設立した11名が2026年3月までに全員退社した事実は、Musk氏のトップAI人材定着困難を直接的に示す。LeCunがxAIを「一種の失敗」と評し、AMI Labs（$1.03B）を設立した事実と合わせると、xAIのLLM中心アプローチに対する学術的・人材的な二重の懐念が構造化している。ただし、この退社が製品開発や性能に直ちに影響しているかの定量証拠は不在である。Colossus 2の稼働・Grok 4.3のGA・Cursor買収（Q3 2026クローズ予定）は、組織の対外拡大が継続していることを示す。

選択的執行の受益者としてのxAI位置づけは、国家安保基盤軸の持続性を強化する（[INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) B-2）。xAIは5月までに全社軍事協定に署名し、Anthropicが拒否してサプライチェーンリスク指定を受けたのと対照的な位置にある。PentagonがAnthropic Claudeの置換テストを開始した（[INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) B-3）ことは、xAIの軍事チャネルが一時的でなく構造的に選好されていることを示す。xAIの軍事システム統合契約は最大$200M（[INFO-034](../Information/2026-06-24/collected-raw.md#INFO-034) B-2）であり、Pentagonが4社（Anthropic/OpenAI/Google/xAI）に各$200Mを配布した枠組み [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064)（B-3）の中で、Anthropicの排除が進めばxAIの相対的地位は上昇する。

[IND-030](../config/indicators.json) はcritical/risingを維持する。KIQ-MIL-001の部分回答は、条件2（A-2品質の技術的安全事故報告）には到達していないが、「設計通りの利用」と「技術的安全リスク」の境界がhuman-on-the-loop移行で更に曖昧化している。ICRCが自律型兵器の新条約を要求し（[INFO-057](../Information/2026-06-29/collected-raw.md#INFO-057) B-2）、「AIは軍事意思決定を支援できるが人間の責任を代替できない」原則を非交渉可能とした。Grok 2,000標的事例との対比で条約要求が急増している。Sen. Gillibrand法案（人間監視なしLLM武力行使禁止）の動向も引き続き監視対象である。

商用面では、Cursor自身がRamp支出データで市場シェアを2025年6月の41%から2026年5月の約26%に落とし、コーディングカテゴリの半数をAnthropicに奪われている（[INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061) A-2）。$60Bで買った資産が買収時点ですでに下落坂にある。DL 60%減（1月20M→4月8.3M）も未解決である。DeepSeek V3.2がGrok 4 Fastの大半のベンチマークで勝利し（[INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) B-2）、1.1倍安価に動作する。コモディティ化圧力は継続している。

[H-XAI-001](../config/hypotheses.json)（Xデータ差別化）と [H-XAI-003](../config/hypotheses.json)（宇宙・製造業特化）は引き続き棄却（35%）で、新たな支持証拠は観測されていない。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Pentagon宣誓陳述書: Grokがイラン作戦で2,000+標的指定に使用・human-on-the-loop移行発言 | KIQ-MIL-001部分回答。9R完全未回答→部分回答転移。[IND-030](../config/indicators.json) critical強化 | B-3 | [INFO-004](../Information/2026-06-29/collected-raw.md#INFO-004) |
| 高 | xAIオリジナル共同創業者11名全員が2026年3月までに退社 | [H-XAI-004](../config/hypotheses.json) I方向。人材定着不全の直接証拠。組織基盤の構造的懸念 | B-2 | [INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058) |
| 高 | Maven Smart System + Grok統合・初24hで1,000標的特定 | KIQ-MIL-001部分回答の補完。Palantir統合で軍事AI基盤の深度化 | B-3 | [INFO-005](../Information/2026-06-29/collected-raw.md#INFO-005) |
| 高 | 選択的執行: xAIは5月までに全社軍事協定署名・受益者位置 | [H-XAI-004](../config/hypotheses.json) C方向（政府チャネル持続性）。Anthropic排除→xAI相対的地位上昇可能性 | B-2 | [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) |
| 高 | SpaceXがCursorを$60B全株式で買収・評価額$1.25兆 | コーディングエージェント軸。[H-XAI-004](../config/hypotheses.json) の前提。但しM&A≠adoption | A-1 | [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) |
| 高 | DeepSeek V3.2がGrok 4 Fast大半で勝利（1.1倍安価） | [H-XAI-002](../config/hypotheses.json) I方向。価格優位の侵食 | B-2 | [INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) |
| 高 | Cursor市場シェア41%(2025-06)→26%(2026-05)・Anthropic半数掌握 | 買収対象が下落坂。[H-XAI-004](../config/hypotheses.json) 矛盾材料 | A-2 | [INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061) |
| 高 | xAI軍事$200M契約・Pentagon 4社各$200M枠組み | 国家安保基盤軸の制度化。Anthropic排除で相対的地位上昇可能性 | B-2 | [INFO-034](../Information/2026-06-24/collected-raw.md#INFO-034) [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) |
| 中 | ICRC自律型兵器新条約要求・Grok 2,000標的との対比 | [IND-030](../config/indicators.json) 文脈強化。国際的規範圧力 | B-2 | [INFO-057](../Information/2026-06-29/collected-raw.md#INFO-057) |
| 中 | LeCun「xAIは失敗」・AMI Labs設立$1.03B | LLM中心アプローチへの学術的懐念。11共同創業者退社と合わせて二重の懐念構造化 | B-2 | [INFO-051](../Information/2026-06-24/collected-raw.md#INFO-051) |
| 中 | Grok Build /goal自律実行・Voice Agent API・Databricks/Bedrock GA | 製品幅拡大。エンタープライズ到達範囲。但し採用の定量裏付け不在 | A-3 | [INFO-009](../Information/2026-06-24/collected-raw.md#INFO-009) [INFO-015](../Information/2026-06-24/collected-raw.md#INFO-015) [INFO-010](../Information/2026-06-24/collected-raw.md#INFO-010) |
| 中 | DL 60%減（1月20M→4月8.3M）未解決 | [H-XAI-002](../config/hypotheses.json) の停滞。59%以下でmedium→low審査トリガー | B-2 | [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| KIQ-MIL-001が完全回答に到達する（人間却下比率・誤標的率の公開） | 標的選定への直接関与度が確定する。partial→full回答転移で判断全面改訂。現在は部分回答（標的数・human-on-the-loop移行は確認、却下比率・誤標的率は非公開） | 90日 | [IND-030](../config/indicators.json) |
| Gillibrand法案（人間監視なしLLM使用禁止）が可決・成立する | 軍事利用の制度化フレームが変わり、国家安保基盤軸の前提が変わる | 180日 | [IND-030](../config/indicators.json) |
| 技術的安全事故（Agent暴走・誤目標）が軍事領域でA-2品質で報告される | [IND-030](../config/indicators.json) の条件2が解消され、リスク評価が全面改訂される | 180日 | [IND-030](../config/indicators.json) |
| Cursor統合後にGrok系コーディングツールの採用（DL/API呼び出し量）が定量で回復する | [H-XAI-004](../config/hypotheses.json) のエンタープライズ獲得読みが上方修正される。90日で回復しなければ読みは弱まる | 90日 | [IND-027](../config/indicators.json) |
| DL減少傾向が3ヶ月以上継続する（1月→4月→7月） | [H-XAI-002](../config/hypotheses.json) の59%根拠が崩れ、medium→low移行が確定する。現在4月までの60%減が確認済み | 90日 | [IND-013](../config/indicators.json) |
| DeepSeek等中国OSSモデルがGrok全系で全面的に勝利する | [H-XAI-002](../config/hypotheses.json) 価格競争力仮説の前提が崩壊する | 90日 | [IND-025](../config/indicators.json) |
| 11共同創業者退社に続き現場中核人材の退社が複数報告される | 組織基盤の構造的劣化が確定し、[H-XAI-004](../config/hypotheses.json) の前提が問われる | 180日 | [IND-028](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-XAI-002](../config/hypotheses.json) | 価格競争力でシェアを獲得する | 59% medium | ±0%。Grok 4.3低価格・Databricks/Bedrock GAはC方向。但しDeepSeek V3.2がGrok 4 Fast大半で勝利・1.1倍安価。DL 60%減未解決（1月→4月）。API価格95%+下落で「低価格」の独自性が希薄化。59%以下が続けば次ラウンドでmedium→low審査 | [INFO-010](../Information/2026-06-24/collected-raw.md#INFO-010) [INFO-009](../Information/2026-06-24/collected-raw.md#INFO-009) | [INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| [H-XAI-004](../config/hypotheses.json) | 汎用AI基盤としてエンタープライズ市場を獲得する | 57% medium | ±0%。SpaceX Cursor $60B買収（A-1）・軍事$200M契約・選択的執行受益者位置（全社軍事協定署名）はC方向。但し核心命題（Grok有機的エンタープライズ採用・X非依存）への診断的適合度は3重の概念飛躍（M&A≠adoption・Cursor価値はClaude/GPT由来・X非依存に無関係）。11共同創業者全員退社はI方向。Cursor 26%下落坂・DL 60%減で相殺 | [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) [INFO-034](../Information/2026-06-24/collected-raw.md#INFO-034) [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) | [INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061) [INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058) [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| [H-XAI-001](../config/hypotheses.json) | （棄却）Xデータ活用でリアルタイム特化を差別化する | 35% | 41R以上にわたりXデータ活用の直接証拠不在。xAI→SpaceXAI統合で観測の意義自体が低下 | （なし） | 41R以上の証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | （棄却）SpaceX統合で宇宙・製造業特化AIを展開する | 35% | 42R以上にわたり直接的特化AI製品証拠不在。Colossusは汎用インフラ扱い | （なし） | 42R以上の特化製品証拠不在 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度・Grok API/DL動向 | 実被害A-2報告でcritical | high/rising。Grok Gov Model稼働・KIQ-MIL-001部分回答。新規A-2脆弱性報告なし。DL 60%減は未解決（1月→4月） | 2026-06-29 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | 「真の理解」の検証 | elevated/stable。Grok 4.3最低ハルシネーション率。但しDeepSeek V3.2が大半で勝利。量的向上継続 | 2026-06-29 |
| [IND-026](../config/indicators.json) | エージェント本番到達率 | 3ソース以上で完了率<10% | high/rising。Gartner 40%導入/40%キャンセル・DataRobot 71%困難。Cursor統合後の本番到達は未計測 | 2026-06-29 |
| [IND-027](../config/indicators.json) | エコシステム標準化・Grokスタック採用 | 围い込み反転 | high/rising。Grok 4.3 Databricks/Bedrock GA・/goal・Voice Agent API。1000+スキル。MCP RC 2026-07-28 | 2026-06-29 |
| [IND-028](../config/indicators.json) | AGI到達度 | 主観-客観乖離 | high/rising。LeCun AMI Labs設立・11共同創業者退社でLLM中心アプローチへの懐念構造化。ARC-AGI-1 Qwen3 96% | 2026-06-29 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | 物理的制約の顕在化 | high/rising。Colossus 2「国家安保不可欠」・SpaceX $1.25兆+Cursor $60B+xAI $20B。資本流入加速 | 2026-06-29 |
| [IND-030](../config/indicators.json) | 能力-リスク二面性 | （critical到達済み） | **critical/rising**。KIQ-MIL-001部分回答（INFO-004 B-3: 2,000標的・human-on-the-loop移行）。Maven統合（INFO-005 B-3）。選択的執行受益者（INFO-067 B-2）。ICRC新条約要求（INFO-057 B-2）。条件2（A-2技術的安全事故）は未到達 | 2026-06-29 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-06-29 | 全面書き直し。KIQ-MIL-001部分回答転移（[INFO-004](../Information/2026-06-29/collected-raw.md#INFO-004) B-3: 2,000標的・human-on-the-loop移行）。Maven統合（[INFO-005](../Information/2026-06-29/collected-raw.md#INFO-005) B-3）。11共同創業者全員退社（[INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058) B-2）。選択的執行受益者位置（[INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) B-2）。ICRC新条約要求（[INFO-057](../Information/2026-06-29/collected-raw.md#INFO-057) B-2）。[H-XAI-002](../config/hypotheses.json) 59% ±0%・[H-XAI-004](../config/hypotheses.json) 57% ±0%維持 | [INFO-004](../Information/2026-06-29/collected-raw.md#INFO-004) [INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058) [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) | H-XAI-002 59% ±0%・H-XAI-004 57% ±0% |
| 2026-06-24 | 全面書き直し。SpaceX Cursor $60B買収のA-1品質確定。[H-XAI-004](../config/hypotheses.json) 55→57%（+2%） | [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) | H-XAI-004 55→57%・H-XAI-002 59%据え置き |
| 2026-06-21 | [IND-030](../config/indicators.json) high→critical。Operation Epic Fury A-2品質確定 | [INFO-044](../Information/2026-06-21/collected-raw.md#INFO-044) | IND-030 critical |
| 2026-06-18 | 全面書き直し。SpaceX-Cursor $60B買収・Grok 4.3 GA・Grok Gov Model軍事展開の二軸再編 | [INFO-054](../Information/2026-06-18/collected-raw.md#INFO-054) | H-XAI-002 59%・H-XAI-004 55%据え置き |
| 2026-06-11 | Gopuff Go・Grok Imagine 1.5・Vapi統合・Composer 2.5・Grok Build 0.1 APIで製品幅拡大 | 2026-06-11複数INFO | |
| 2026-05-28 | Grok Build正式リリース・DL 60%減・$20B Series E・API価格95%+下落 | 2026-05-28複数INFO | |

## 7. ブラインドスポット

- KIQ-MIL-001の部分回答は、標的数（2,000+）と監視形態（human-on-the-loop移行）を確認したが、人間却下比率・誤標的率は非公開のままである。「Grokが標的を提案し人間が承認した」のか「Grokが直接標的を決定した」のかの区別が不明。human-on-the-loopという概念自体が、人間の実効的介入能力に疑問を投げかけるが、その実効性を独立的に検証する手段がない。
- 11共同創業者全員退社の影響が、製品開発・性能・組織執行力にどのように現れるかの定量評価がない。退社のタイミング（2026年3月まで）と現在のGrok 4.3 GA・Cursor買収の継続が矛盾して見える。後任者の質・チームの再編状況が非公開である。
- SpaceXAIの内部戦略が外部から観測不能。Cursor買収とGrok軍事展開は観測できても、SpaceX本体の投資判断なのかSpaceXAI内部の戦略なのか、Colossus 2の軍民分担がどうなっているかが判別不能。
- Cursor統合の成果が測れない。買収はQ3 2026クローズ予定で、統合後のGrok-Cursor連携・コーディング採用の回復・DL回復はすべて未計測。買収時点でCursorがシェア26%に下落中という出発点の悪さも未消化。
- DeepSeek V3.2がGrok 4 Fastの大半で勝利した事実が [H-XAI-002](../config/hypotheses.json) の前提を直接侵食している。Grokの「低価格」が中国OSSモデルの極低価格に対して差別化要因として機能し得るかの定量評価がない。
- 選択的執行の受益者位置が持続するか不確定。政権変動・司法判断・Anthropicの訴訟結果で、xAIの「恩恵」が逆転する可能性がある。全社軍事協定署名は現時点ではC方向証拠だが、恒久的な構造ではなく政治的均衡の産物かもしれない。
- 軍事利用のリスク評価で「設計通りの軍事利用」と「技術的安全事故」の区別が実質的に崩れつつある。2,000標的/96hテンポでは意味ある人間監査が物理的に困難だが、この境界の崩壊を定量的に監視する枠組みが未整備。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-004](../Information/2026-06-29/collected-raw.md#INFO-004) | Pentagon宣誓陳述書: Grok 2,000+標的・human-on-the-loop移行・KIQ-MIL-001部分回答(B-3) |
| [INFO-005](../Information/2026-06-29/collected-raw.md#INFO-005) | Maven Smart System + Grok統合・初24h 1,000標的(B-3) |
| [INFO-058](../Information/2026-06-29/collected-raw.md#INFO-058) | LeCun「xAI失敗」・共同創業者11名全員退社(B-2) |
| [INFO-067](../Information/2026-06-29/collected-raw.md#INFO-067) | 選択的執行タイムライン・xAI全社軍事協定署名(B-2) |
| [INFO-064](../Information/2026-06-29/collected-raw.md#INFO-064) | Pentagon置換テスト・4社各$200M契約(B-3) |
| [INFO-057](../Information/2026-06-29/collected-raw.md#INFO-057) | ICRC自律型兵器新条約要求(B-2) |
| [INFO-051](../Information/2026-06-29/collected-raw.md#INFO-051) | Grok Build /goal自律実行・Grok 4.20 APIエイリアス(A-3) |
| [Arbiter v4.23](../state/arbiter-2026-06-29.md) | H-XAI-002 59% ±0%・H-XAI-004 57% ±0%維持 |
| [INFO-041](../Information/2026-06-24/collected-raw.md#INFO-041) | SpaceX-Cursor $60B買収・評価額$1.25兆(A-1) |
| [INFO-044](../Information/2026-06-24/collected-raw.md#INFO-044) | xAI $20B Series E(B-2) |
| [INFO-033](../Information/2026-06-24/collected-raw.md#INFO-033) | Operation Epic Fury 96h/2,000標的/2,000発(B-1) |
| [INFO-034](../Information/2026-06-24/collected-raw.md#INFO-034) | xAI軍事$200M契約・DoJ確認(B-2) |
| [INFO-045](../Information/2026-06-24/collected-raw.md#INFO-045) | DeepSeek V3.2 > Grok 4 Fast大半・1.1倍安価(B-2) |
| [INFO-051](../Information/2026-06-24/collected-raw.md#INFO-051) | LeCun「xAI失敗」・AMI Labs $1.03B設立(B-2) |
| [INFO-061](../Information/2026-06-18/collected-raw.md#INFO-061) | Cursor 41%→26%下落・Anthropic半数掌握(A-2) |
| [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) | DL 60%減少・エンタープライズ苦戦(B-2) |
