# xAI

> 最終更新: 2026-04-27
> 確度: 中

SpaceX完全子会社として$1.25兆の合算評価額を持つ「物理世界AI」企業に変貌した。Grok APIは$2/M入力と業界最安水準。Tesla全車種にGrok統合済み。2026年3月のgrok-4.20-multi-agentで200万トークンコンテキストと4〜16エージェント協調 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)。

2026年4月下旬、xAIは想定外の入口を見つけた。PentagonのGenAI.milプラットフォームが**120万ユーザー・10万エージェント**に到達し、Grokが正式に統合されている [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022)。xAIは軍事Grok利用について「**白紙小切手**」を与えられた [INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023)。Anthropicが安全性制約でPentagonから排除された間隙を、xAIが埋めた形だ。これはH-XAI-004（汎用AI基盤）を強く支持する——GrokはXデータにもSpaceX統合にも依存せず、政府市場で採用されている。

だが中核の2仮説は崩れ続けている。Xデータ活用差別化（H-XAI-001）は**25日以上**証拠不在で45%に低下。SpaceX統合AI（H-XAI-003）も**25日以上**C証拠不在で42%に低下、low再分類の確約ライン（40%）まであと2%。**汎用AI基盤（H-XAI-004、55%）**が最有力仮説を維持する。

## この会社は何物か

Elon Musk率いるAI企業。主力はGrok 4.20シリーズ（Standard/Heavy）、Grok 4.1 Fast、Grok Business/Enterprise、**Grok STT/TTS API**。

2026年2月2日にSpaceXがxAIを完全子会社として買収（全株式交換、合算評価額$1.25兆）。史上最大の合併取引。「軌道データセンター」構想で2-3年以内に宇宙ベースAI計算を最低コストにする計画。

価格は確認済みの強み。Grok 4.20 Multi Agent 0309は$2.00/M入力・$6.00/M出力で200万トークンコンテキスト対応 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)。キャッシュ入力$0.20/M。バッチAPIは50%割引。

**Grok STT/TTS API**（2026年4月中旬）: STT全体WER 6.9%、電話エンティティWER 5.0%（競合最強）。TTS $4.20/1M文字。25+言語対応、話者分離・マルチチャンネル対応。REST API + WebSocket API（リアルタイムストリーミング）。スピーカータグ（[laugh], [whisper], <emphasis>等）による表現制御。Tesla/Starlinkと同じオーディオスタック [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020)。

**Grok 4.20 Heavy**: 16エージェント版。Enterprise APIで利用可能。金融モデリング・法務分析・複雑推論に対応 [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020)。Vertex AIでも提供開始。

**Grok on Vertex AI**: Grok 4.20（Reasoning/Non-Reasoning）、Grok 4.1 Fast（Reasoning/Non-Reasoning）の4モデル。Google Cloudの既存認証・IAMインフラでアクセス可能 [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020)。

**Grok 4.1 Fast**: Oracle Cloud Infrastructureで提供開始。2Mトークンコンテキスト。幻覚約3分の1削減 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)。

**Pentagon GenAI.mil統合**: 120万ユーザー・10万エージェント作成のプラットフォームにGrokが統合。Google Geminiが先行した後、OpenAIとxAI Grokが続いた [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022)。xAIは軍事Grok利用について「blank check」を与えられ、用途制限なしで展開可能 [INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023)。AnthropicのSCR指定で生じた政府市場の間隙をxAIが埋めている。

## 何をやろうとしているか

### 汎用AI基盤としてエンタープライズ市場を獲得する（H-XAI-004、確度55%）★現在最有力★

xAIはGrokをXデータ依存なしでエンタープライズ市場に展開し、金融・法務・医療・政府等の多業種でシェアを獲得しつつある。25日間にわたり指摘され続けた仮説の正式化 [Arbiter v3.55](../state/arbiter-2026-04-20.md)。

**Pentagon GenAI.mil**はこの仮説を最も強く支持する新証拠だ。120万ユーザー・10万エージェントの政府プラットフォームでGrokが採用されたことは、Xデータとは無関係な汎用用途での競合力を実証する [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022)。軍事利用の「blank check」は政府からの信頼の証 [INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023)。

**Shift4 Payments**: 大手決済処理会社がChatGPTからGrokに全面移行 [INFO-016](../Information/2026-04-20/collected-raw.md#INFO-016)。戦略的転換。

**Grok 4.20 Heavy**: 金融モデリング・法務分析向け16エージェント版は、Xデータとは無関係なエンタープライズ用途での競合力を示す [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020)。

**JAMA臨床推論**: Grok 4が0.78を記録 [INFO-076](../Information/2026-04-20/collected-raw.md#INFO-076)。医療領域での汎用性能を示す第三者検証。

**Grok on Vertex AI**: Google Cloud経由でエンタープライズ配布を開始 [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020)。Xデータ非依存の配布チャネル。

確度55% [Arbiter v3.62](../state/arbiter-2026-04-27.md)。市場シェア定量データ不在で上限キャップ適用継続。Pentagon統合が新規Cだが、定量シェアデータが出るまでは+1%の条件を満たさない。

### Xデータでリアルタイム特化（H-XAI-001、確度45%）

X（Twitter）のリアルタイムデータを独占活用し、ニュース・時事対応で差別化する。x_search内蔵がXデータ独占活用の具体的な製品機能 [INFO-007](../Information/2026-03-25/collected-raw.md#INFO-007)。Grok STT/TTS APIにもx_searchが組み込まれている。

確度は52%→45%に低下（7日間で-7%）。**25日以上**連続でXリアルタイムデータ活用の新規証拠が不在。Pentagon Grok統合・blank check等の新規証拠は全て代替仮説（H-XAI-004 汎用AI基盤）を支持し、H-XAI-001とは無関係。時間減衰継続。40%到達時にlow再分類検討 [Arbiter v3.62](../state/arbiter-2026-04-27.md)。

### 価格競争でシェアを獲得（H-XAI-002、確度65%）

Colossusクラスタの計算資源とSpaceXインフラを武器に、モデル性能と価格の両面でTier 1に挑戦する。**Grok on Vertex AI**でGoogle Cloud経由のエンタープライズ配布が始まったことは、価格戦略の新たな配布チャネル獲得を意味する [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020)。Grok 4.1 Fastで幻覚1/3削減 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)。

確度は65% [Arbiter v3.62](../state/arbiter-2026-04-27.md)。新規価格データなし。DeepSeek V4 $0.30/MTok（[INFO-034](../Information/2026-04-27/collected-raw.md#INFO-034)）はxAI価格優位への潜在的脅威だが、Grok価格自体の変更なし。価格≠市場シェアの因果関係は依然として未検証。

### 物理世界Agent統合（H-XAI-003、確度42%）

Tesla、SpaceX、XとGrokを統合し、ソフトウェアだけでなく物理世界で動くAIを実現する。

3つの直接的な証拠がある:
1. **SpaceX合併完了**（2026年2月2日）
2. **Tesla車両にGrok統合済み**: NA 2025年7月、EU 2026年2月
3. **Optimus V3にGrok音声AI統合確認**

確度は49%→42%に低下（7日間で-7%）。**25日以上**連続SpaceX統合証拠不在。Pentagon Grok blank check（[INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023)）は政府軍事利用のCだがSpaceX統合とは無関係。40%まであと2%。low再分類確約継続（[Arbiter v3.54](../state/arbiter-2026-04-17.md)から）。Grok STT/TTS APIの「Tesla/Starlink同じスタック」は弱Cだが、汎用API製品の性質上、物理世界特化の決定的証拠とは言えない。

## 強みと弱み

xAIの強みは、物理世界統合の実績（Tesla車両統合は「出荷済み製品」）、SpaceX合併による構造変化（$1.25兆の資源アクセス）、価格競争力（$2/M入力で2Mコンテキスト）、Xのリアルタイムデータ、grok-4.20-multi-agentの200万トークンコンテキストと4〜16エージェント協調 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)、**Grok STT WER 6.9%で音声認識首位** [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020)、**Grok on Vertex AIでエンタープライズ配布開始** [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020)、Grok 4.1 Fastの幻覚1/3削減 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)、**Shift4 Payments全面移行でエンタープライズ顧客獲得** [INFO-016](../Information/2026-04-20/collected-raw.md#INFO-016)、**JAMA臨床推論0.78で医療領域での競合力示す** [INFO-076](../Information/2026-04-20/collected-raw.md#INFO-076)、**Pentagon GenAI.mil統合（120万ユーザー・blank check）** [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) [INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023)。

弱みは4つ。主要ベンチマークでOpenAI/Anthropic/Googleの後塵を拝すること。エンタープライズ後発で大企業向けの実績がTier 1と比べて少ないこと。中核仮説の確度低下が7日間で加速していること——H-XAI-001が52%→45%（25日+証拠不在・40%到達時にlow再分類検討）、H-XAI-003が49%→42%（25日+証拠不在・40%まで2%・low再分類確約）。そしてMusk個人リスク——事業群が一人の経営者に依存し、規制当局による事業統合への介入リスクもある。

## I&W監視ポイント

| 指標 | 何を見ているか | 今の状態 |
|------|--------------|---------|
| [IND-017](../config/indicators.json) データ優位の囲い込み | Xデータ独占活用が市場優位に直結するか | x_search内蔵・STT/TTS API対応。**25日+新規証拠不在**。市場優位への直結は未検証 |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | grok-4.20-multi-agent・STT/TTS APIの採用状況 | 4〜16エージェント協調。STT WER 6.9%首位。Vertex AI提供開始。**Pentagon GenAI.mil 10万エージェント** [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) |
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | Grokのベンチマーク性能がフロンティアに追いつくか | 主要ベンチマークでTier 1後塵 |
| [IND-025](../config/indicators.json) マルチモーダル信頼性 | 音声認識での競合優位 | Grok STT WER 6.9%（ElevenLabs 9.0%凌駕）[INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020) |
| [IND-030](../config/indicators.json) AI能力とリスクの二面性 | 軍事利用のblank checkがリスク評価に与える影響 | Pentagon Grok blank check [INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023)。用途制限なし |

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| H-XAI-004（汎用AI基盤）の検証 | 最有力仮説。エンタープライス+政府採用の広がりを確認 | 55%。Pentagon GenAI.mil + Shift4移行 + JAMA 0.78 + Vertex AI配布がC |
| Pentagon GenAI.milでのGrok実績 | 政府市場での定着度。120万ユーザー中Grok利用率 | 統合開始 [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022)。利用率データ待ち |
| H-XAI-001の45%低下 | Xデータ活用差別化の妥当性 | 25日+証拠不在。40%到達でlow再分類検討 |
| H-XAI-003の42%低下 | 40%到達時にlow再分類確約 | 25日+証拠不在。40%まで2% |
| Grok STT/TTS APIの採用 | 音声APIが市場に受け入れられるか | リリース済み。WER 6.9%競合最強 [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020) |
| Grok on Vertex AIの実績 | エンタープライズ配布の成否 | 提供開始 [INFO-020](../Information/2026-04-20/collected-raw.md#INFO-020) |
| SpaceX軌道データセンターの進展 | 長期計算コスト優位の成否 | 構想段階（2-3年計画） |
| Tesla全車種Grok統合の評価 | 車載AIの品質がxAI製品力の最初の大規模テスト | NA/EU展開済み。ユーザー評価データ待ち |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-27 | 鮮度タイムアウト対応（7日経過）。Pentagon GenAI.mil Grok統合（120万ユーザー・10万エージェント）・軍事利用blank check [INFO-022](../Information/2026-04-27/collected-raw.md#INFO-022) [INFO-023](../Information/2026-04-27/collected-raw.md#INFO-023) を反映してエグゼクティブサマリー・基本情報・戦略方向性・強みと弱み・I&W・監視ポイントを書き直し。H-XAI-001 52→45%（25日+証拠不在）・H-XAI-003 49→42%（25日+証拠不在・40%まで2%）・H-XAI-004 55%維持（Pentagon C）・H-XAI-002 65%維持に更新 |
| 2026-04-20 | H-XAI-004（汎用AI基盤としての成長、初期確度55%）を新設仮説として追加。Shift4 Payments全面移行・JAMA臨床推論0.78を反映。H-XAI-001 53→52%（18日+証拠不在）・H-XAI-003 50→49%（18日+証拠不在）に更新。エグゼクティブサマリーをH-XAI-004追加に伴い書き直し |
| 2026-04-19 | Grok STT/TTS API（WER 6.9%競合最強・$4.20/1M文字・25+言語・Tesla/Starlink同じスタック）・Grok on Vertex AI（4モデル提供開始）を追加。H-XAI-001 55→53%（17日+証拠不在・時間減衰）・H-XAI-003 52→50%（17日+証拠不在・medium下限到達）に更新 |
| 2026-04-17 | Voice Agent API・H-XAI-001 62→55%・H-XAI-003 58→52%に更新 |
| 2026-04-08 | Grok 3 Beta・Grok 4.1 Fastを追加。鮮度タイムアウト対応 |
