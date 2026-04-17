# xAI

> 最終更新: 2026-04-17
> 確度: 中

SpaceX完全子会社として$1.25兆の合算評価額を持つ「物理世界AI」企業に変貌した。Grok APIは$2/M入力と業界最安水準。Tesla全車種にGrok統合済み（北米2025年7月、欧州2026年2月）。2026年3月のgrok-4.20-multi-agentで200万トークンコンテキストと4〜16エージェント協調 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)。**2026年4月、Voice Agent API**をリリース——WebSocketベースのリアルタイム音声対話。MCP・x_search・カスタム関数ツール対応で、OpenAI Realtime APIと互換 [INFO-013](../Information/2026-04-17/collected-raw.md#INFO-013)。

だが中核仮説の確度は下がり続けている。Xデータ活用差別化（H-XAI-001）は12日以上証拠不在で55%に低下。SpaceX統合AI（H-XAI-003）は15日以上C証拠不在で52%に低下し、medium下限に接近している。価格優位（H-XAI-002）の65%だけが安定的。

## この会社は何者か

Elon Musk率いるAI企業。主力はGrok 4.20シリーズ、Grok 4.1 Fast、Grok Business/Enterprise、**Voice Agent API**。

2026年2月2日にSpaceXがxAIを完全子会社として買収（全株式交換、合算評価額$1.25兆、Bloomberg/CNBC/Fortune報道)。史上最大の合併取引。「軌道データセンター」構想で2-3年以内に宇宙ベースAI計算を最低コストにする計画を掲げている。

価格は確認済みの強み。Grok 4.20 Multi Agent 0309は$2.00/M入力・$6.00/M出力で200万トークンコンテキスト対応 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)。キャッシュ入力$0.20/M。1,800 RPM,10M TPM。新規ユーザーには$25クレジット、データ共有プログラムで月$150利用可能。バッチAPIは50%割引。

**Grok 3 Beta**（2026年2月）: 10倍の計算量で訓練。AIME'25 93.3%、GPQA 84.6%、LiveCodeBench 79.4%。100万トークンコンテキスト（従来の8倍）。DeepSearchエージェント（リアルタイム検索・推論統合）。Chatbot Arena Elo 1402（コードネームchocolateで1位）[INFO-006](../Information/2026-02-19/collected-raw.md#INFO-006)。

**Grok 4.1 Fast**（2026年4月）: Oracle Cloud Infrastructureで提供開始。2Mトークンコンテキスト。Reasoning/Non-Reasoningモード。幻覚約3分の1削減、ツール呼び出し改善、並列処理対応 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)。

**Voice Agent API**（2026年4月）: WebSocketベースのリアルタイム音声対話。file_search、web_search、x_search、MCP、カスタム関数ツール対応。OpenAI Realtime APIと互換（ベースURL変更で移行可能）。5音声（eve, ara, rex, sal, leo）。20+言語ネイティブ対応 [INFO-013](../Information/2026-04-17/collected-raw.md#INFO-013)。

**2026年3月の新機能**: grok-4.20-multi-agent-0309で200万トークンコンテキスト・Function calling・Structured outputs・Reasoning対応 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)。4〜16エージェント協調が可能。Web検索（web_search）、X検索（x_search）、コード実行（code_execution）を組み込みツールとして提供。

## 何をやろうとしているか

### Xデータでリアルタイム特化（H-XAI-001、確度55%）

X（Twitter）のリアルタイムデータを独占活用し、ニュース・時事対応で差別化する。x_search内蔵がXデータ独占活用の具体的な製品機能 [INFO-007](../Information/2026-03-25/collected-raw.md#INFO-007)。Voice Agent APIにもx_searchが組み込まれている [INFO-013](../Information/2026-04-17/collected-raw.md#INFO-013)。

確度は62%→55%に低下。12日以上連続でXリアルタイムデータ活用の新規証拠が不在。構造見直しトリガーが発動している。仮説文の妥当性再評価とlow再分類の可能性が次回以降の課題。代替仮説「汎用AI基盤として成長」の再定式化が推奨されている [Arbiter v3.51](../state/arbiter-2026-04-16.md)。

この方向が正しければ、ニュース・時事クエリでのGrok優先利用率が上昇する。間違いなら、競合のリアルタイムデータ取得（Reddit等）やXデータ活用の規制強化で差別化が崩れる。

### 価格競争でシェアを獲得（H-XAI-002、確度65%）

Colossusクラスタの計算資源とSpaceXインフラを武器に、モデル性能と価格の両面でTier 1に挑戦する。**Grok 4.1 Fast**で幻覚1/3削減、価格品質バランスが改善 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)。Grok 4.20 Multi Agent 0309は$2.00/M入力で200万トークンコンテキストを提供し、Gemini 3.1 Proの$2/M（2Mコンテキスト）と同等価格、GPT-5.4の$10/Mより大幅に安い [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)。SpaceX合併で「軌道データセンター」構想が具体化し、長期的な計算コスト優位を目指している。

確度は65%（Arbiter v3.52）。新規価格データなし。価格≠市場シェアの因果関係は依然として未検証。

### 物理世界Agent統合（H-XAI-003、確度52%）

Tesla、SpaceX、XとGrokを統合し、ソフトウェアだけでなく物理世界で動くAIを実現する。3つの直接的な証拠がある:

1. **SpaceX合併完了**（2026年2月2日）: 全株式交換、xAIはSpaceX完全子会社。軌道データセンター構想
2. **Tesla車両にGrok統合済み**: 北米は2025年7月（ソフトウェア2025.26）、欧州は2026年2月14日（2026.2.6）にロールアウト。Model S/3/X/Y/Cybertruck対応
3. **Optimus V3にGrok音声AI統合確認**: MuskがGrokをOptimusの「声と頭脳」にすると公式発表

確度は58%→52%に低下。SpaceX統合成果の外部シグナルが15日以上連続不在。時間減衰が継続。52%到達でmedium下限（50%±10%）に接近。50%到達でlow再分類を検討 [Arbiter v3.52](../state/arbiter-2026-04-17.md)。

Voice Agent APIはMCP対応を含む [INFO-013](../Information/2026-04-17/collected-raw.md#INFO-013) が、これは汎用的な機能拡張でありSpaceX/物理世界特化の証拠ではない。

## 強みと弱み

xAIの強みは、物理世界統合の実績（Tesla車両統合は「出荷済み製品」）、SpaceX合併による構造変化（$1.25兆の資源アクセス、軌道データセンター構想）、価格競争力（Grok 4.20 Multi Agent $2/M入力は2Mコンテキスト込みでGemini同等）、Xのリアルタイムデータ、grok-4.20-multi-agent-0309の200万トークンコンテキストと4〜16エージェント協調機能 [INFO-008](../Information/2026-04-01/collected-raw.md#INFO-008)、**Voice Agent APIのMCP・x_search対応** [INFO-013](../Information/2026-04-17/collected-raw.md#INFO-013)、Grok 4.1 Fastの幻覚1/3削減 [INFO-010](../Information/2026-04-08/collected-raw.md#INFO-010)。

弱みは4つ。主要ベンチマークでOpenAI/Anthropic/Googleの後塵を拝すること。エンタープライス後発で大企業向けの実績がTier 1と比べて少ないこと。中核仮説の確度低下が続いていること——H-XAI-001が55%、H-XAI-003が52%に低下し、構造見直しが迫られている。そしてMusk個人リスク——事業群が一人の経営者に依存し、規制当局による事業統合への介入リスクもある。エンタープライスセキュリティ（SOC2/FedRAMP等の認証状況）も不明。

## I&W監視ポイント

| 指標 | 何を見ているか | 今の状態 |
|------|--------------|---------|
| [IND-017](../config/indicators.json) データ優位の囲い込み | Xデータ独占活用が市場優位に直結するか | x_search内蔵・Voice Agent API対応。ただし市場優位への直結は未検証 |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | grok-4.20-multi-agentとVoice Agent APIの採用状況 | 4〜16エージェント協調。Voice Agent API新規リリース。MCP対応 |
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | Grokのベンチマーク性能がフロンティアに追いつくか | 主要ベンチマークでTier 1後塵 |

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Tesla全車種Grok統合の評価 | 車載AIの品質がxAI製品力の最初の大規模テスト | NA/EU展開済み。ユーザー評価データ待ち |
| Optimus V3量産開始 | ロボティクスAIの実用化でH-XAI-003が決定的に | Grok音声AI統合確認済み |
| Voice Agent APIの採用 | MCP対応音声エージェントが市場に受け入れられるか | リリース済み。OpenAI Realtime API互換 [INFO-013](../Information/2026-04-17/collected-raw.md#INFO-013) |
| SpaceX軌道データセンターの進展 | 長期計算コスト優位の成否 | 構想段階（2-3年計画） |
| H-XAI-001構造見直しの判断 | 50%到達でlow再分類か代替仮説再定式化か | 55%。構造見直しトリガー発動中 |
| H-XAI-003の50%到達 | 50%到達でlow再分類検討 | 52%。medium下限に接近 |
| エンタープライズ顧客獲得 | 価格是正後の市場浸透度 | Business/Enterprise提供開始済み |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-17 | 鮮度タイムアウト対応（9日経過）。Voice Agent API（MCP・x_search・OpenAI Realtime API互換）を追加。H-XAI-001 62→55%（構造見直しトリガー発動）・H-XAI-002 66→65%・H-XAI-003 58→52%（15日+C証拠不在・medium下限接近）に更新。代替仮説再定式化の必要性を追記 |
| 2026-04-08 | Grok 3 Beta（AIME'25 93.3%、GPQA 84.6%、100万トークンコンテキスト）、Grok 4.1 Fast（Oracle Cloud、2Mコンテキスト、幻覚1/3削減）を追加。H-XAI-001 61→62%、H-XAI-002 65→66%、H-XAI-003 60→58%に更新。鮮度タイムアウト対応（7日以上未更新） |
| 2026-03-25 | 1ヶ月分統合。grok-4.20-multi-agent（4〜16エージェント協調、x_search内蔵）を追加。H-XAI-001 60→61%、H-XAI-003 61→60%。構造維持、新規証拠を統合 |
| 2026-02-23 | 初版作成。SpaceX合併、Tesla統合、価格訂正を反映 |
