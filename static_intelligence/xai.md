# xAI

> 最終更新: 2026-04-19
> 確度: 中

SpaceX完全子会社として$1.25兆の合算評価額を持つ「物理世界AI」企業に変貌した。Grok APIは$2/M入力と業界最安水準。Tesla全車種にGrok統合済み。2026年3月のgrok-4.20-multi-agentで200万トークンコンテキストと4〜16エージェント協調 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)。

2026年4月中旬、2つの動きが同時に起きた。**Grok STT/TTS API**が発表——STT全体WER 6.9%（ElevenLabs 9.0%を凌駕）、TTS $4.20/1M文字、25+言語対応 [INFO-007](../Information/2026-04-19/collected-raw.md#INFO-007)。Tesla車両・Starlinkカスタマーサポートと同じオーディオスタックを使う。同時に**GrokモデルがVertex AIでマネージドAPI提供開始**——Grok 4.20/4.1 Fastの4モデルがGoogle Cloudの既存認証・IAMインフラでアクセス可能 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。

だが中核仮説の確度は下がり続けている。Xデータ活用差別化（H-XAI-001）は17日以上証拠不在で53%に低下。SpaceX統合AI（H-XAI-003）は17日以上C証拠不在で50%に低下、medium下限到達。価格優位（H-XAI-002）の65%だけが安定的。

## この会社は何物か

Elon Musk率いるAI企業。主力はGrok 4.20シリーズ、Grok 4.1 Fast、Grok Business/Enterprise、**Grok STT/TTS API**。

2026年2月2日にSpaceXがxAIを完全子会社として買収（全株式交換、合算評価額$1.25兆）。史上最大の合併取引。「軌道データセンター」構想で2-3年以内に宇宙ベースAI計算を最低コストにする計画。

価格は確認済みの強み。Grok 4.20 Multi Agent 0309は$2.00/M入力・$6.00/M出力で200万トークンコンテキスト対応 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)。キャッシュ入力$0.20/M。バッチAPIは50%割引。

**Grok STT/TTS API**（2026年4月17日）: STT全体WER 6.9%、電話エンティティWER 5.0%（競合最強）。TTS $4.20/1M文字。25+言語対応、話者分離・マルチチャンネル対応。REST API + WebSocket API（リアルタイムストリーミング）。スピーカータグ（[laugh], [whisper], <emphasis>等）による表現制御。Tesla/Starlinkと同じオーディオスタック [INFO-007](../Information/2026-04-19/collected-raw.md#INFO-007)。

**Grok on Vertex AI**（2026年4月17日）: Grok 4.20（Reasoning/Non-Reasoning）、Grok 4.1 Fast（Reasoning/Non-Reasoning）の4モデル。Grok 4.20は「業界最低のハルシネーション率」を特徴とし長期エージェントツール呼び出しに優れる。SSEストリーミング対応 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。

**Grok 4.1 Fast**（2026年4月）: Oracle Cloud Infrastructureで提供開始。2Mトークンコンテキスト。幻覚約3分の1削減 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)。

## 何をやろうとしているか

### Xデータでリアルタイム特化（H-XAI-001、確度53%）

X（Twitter）のリアルタイムデータを独占活用し、ニュース・時事対応で差別化する。x_search内蔵がXデータ独占活用の具体的な製品機能 [INFO-007](../Information/2026-03-25/collected-raw.md#INFO-007)。Grok STT/TTS APIにもx_searchが組み込まれている [INFO-007](../Information/2026-04-19/collected-raw.md#INFO-007)。

確度は62%→53%に低下。17日以上連続でXリアルタイムデータ活用の新規証拠が不在。時間減衰継続。INFO-007（音声API）・INFO-020（Vertex AI）は汎用AI基盤拡張でありXデータ活用とは無関係。代替仮説「汎用AI基盤としての成長」の仮説レジストリ追加を次回最優先 [Arbiter v3.54](../state/arbiter-2026-04-19.md)。

### 価格競争でシェアを獲得（H-XAI-002、確度65%）

Colossusクラスタの計算資源とSpaceXインフラを武器に、モデル性能と価格の両面でTier 1に挑戦する。**Grok on Vertex AI**でGoogle Cloud経由のエンタープライズ配布が始まったことは、価格戦略の新たな配布チャネル獲得を意味する [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。Grok 4.1 Fastで幻覚1/3削減 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)。

確度は65%（Arbiter v3.54）。新規価格データなし。価格≠市場シェアの因果関係は依然として未検証。

### 物理世界Agent統合（H-XAI-003、確度50%）

Tesla、SpaceX、XとGrokを統合し、ソフトウェアだけでなく物理世界で動くAIを実現する。

3つの直接的な証拠がある:
1. **SpaceX合併完了**（2026年2月2日）
2. **Tesla車両にGrok統合済み**: NA 2025年7月、EU 2026年2月
3. **Optimus V3にGrok音声AI統合確認**

確度は58%→50%に低下。17日以上連続SpaceX統合証拠不在。時間減衰継続。50%到達でmedium下限境界。Grok STT/TTS APIの「Tesla/Starlink同じスタック」は弱Cだが、汎用API製品の性質上、物理世界特化の決定的証拠とは言えない。代替仮説再定式化を最優先 [Arbiter v3.54](../state/arbiter-2026-04-19.md)。

## 強みと弱み

xAIの強みは、物理世界統合の実績（Tesla車両統合は「出荷済み製品」）、SpaceX合併による構造変化（$1.25兆の資源アクセス）、価格競争力（$2/M入力で2Mコンテキスト）、Xのリアルタイムデータ、grok-4.20-multi-agentの200万トークンコンテキストと4〜16エージェント協調 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)、**Grok STT WER 6.9%で音声認識首位** [INFO-007](../Information/2026-04-19/collected-raw.md#INFO-007)、**Grok on Vertex AIでエンタープライズ配布開始** [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)、Grok 4.1 Fastの幻覚1/3削減 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)。

弱みは4つ。主要ベンチマークでOpenAI/Anthropic/Googleの後塵を拝すること。エンタープライズ後発で大企業向けの実績がTier 1と比べて少ないこと。中核仮説の確度低下が続いていること——H-XAI-001が53%、H-XAI-003が50%に低下し、代替仮説再定式化が迫られている。そしてMusk個人リスク——事業群が一人の経営者に依存し、規制当局による事業統合への介入リスクもある。

## I&W監視ポイント

| 指標 | 何を見ているか | 今の状態 |
|------|--------------|---------|
| [IND-017](../config/indicators.json) データ優位の囲い込み | Xデータ独占活用が市場優位に直結するか | x_search内蔵・STT/TTS API対応。市場優位への直結は未検証 |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | grok-4.20-multi-agent・STT/TTS APIの採用状況 | 4〜16エージェント協調。STT WER 6.9%首位。Vertex AI提供開始 |
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | Grokのベンチマーク性能がフロンティアに追いつくか | 主要ベンチマークでTier 1後塵 |
| [IND-025](../config/indicators.json) マルチモーダル信頼性 | 音声認識での競合優位 | Grok STT WER 6.9%（ElevenLabs 9.0%凌駕）[INFO-007](../Information/2026-04-19/collected-raw.md#INFO-007) |

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Tesla全車種Grok統合の評価 | 車載AIの品質がxAI製品力の最初の大規模テスト | NA/EU展開済み。ユーザー評価データ待ち |
| Grok STT/TTS APIの採用 | 音声APIが市場に受け入れられるか | リリース済み。WER 6.9%競合最強 [INFO-007](../Information/2026-04-19/collected-raw.md#INFO-007) |
| Grok on Vertex AIの実績 | エンタープライズ配布の成否 | 提供開始 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020) |
| H-XAI-001代替仮説の定式化 | 17日+証拠不在で仮説見直し必須 | 53%。代替仮説「汎用AI基盤としての成長」追加を最優先 |
| H-XAI-003の50%到達 | 代替仮説再定式化の判断 | 50%。medium下限到達 |
| SpaceX軌道データセンターの進展 | 長期計算コスト優位の成否 | 構想段階（2-3年計画） |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-19 | Grok STT/TTS API（WER 6.9%競合最強・$4.20/1M文字・25+言語・Tesla/Starlink同じスタック）・Grok on Vertex AI（4モデル提供開始）を追加。H-XAI-001 55→53%（17日+証拠不在・時間減衰）・H-XAI-003 52→50%（17日+証拠不在・medium下限到達）に更新 |
| 2026-04-17 | Voice Agent API・H-XAI-001 62→55%・H-XAI-003 58→52%に更新 |
| 2026-04-08 | Grok 3 Beta・Grok 4.1 Fastを追加。鮮度タイムアウト対応 |
| 2026-03-25 | grok-4.20-multi-agent（4〜16エージェント協調・x_search内蔵）を追加 |
| 2026-02-23 | 初版作成 |
