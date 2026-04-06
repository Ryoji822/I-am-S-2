# Google / DeepMind

> 最終更新: 2026-04-06
> 確度: 高

GPQA Diamond 94.3%で評価首位を保ちつつ、ARC-AGI-2ではGPT-5.4 Proの83.3%に6.2pt差で敗れた。だがGemma 4（Arena Elo 1452）でオープンモデルの新基準を打ち立て、Gemini 3.1 Flash-Lite/Flash Liveでエッジとリアルタイム音声の両面を制した。ベンチマーク単独首位よりも「AIをどこにでも埋め込む」戦略の実行に軸足がある。

## この会社は何者か

Sundar Pichai率いるテクノロジー企業。主力はGemini 3.1シリーズ（Pro/Flash/Flash-Lite/Flash Live）、Vertex AI、Google Workspace、Google Cloud、Gemma 4。従業員180,000人以上。

他のAI専業企業と根本的に違う点が2つある。外部の資金調達が不要なこと。そして検索・Gmail・Drive・Workspace・Android・Chromeという20億人規模のユーザーベースがそのまま配布チャネルになること。開発競争が長期化するほど、この2つが効いてくる。

Gemini 3.1 ProはARC-AGI-2で77.1%（前世代31.1%から146%向上）だが、GPT-5.4 Proの83.3%に6.2pt劣後 [INFO-043](../Information/2026-03-08/collected-raw.md#INFO-043)。Gemini 3 Deep ThinkはARC-AGI-2で84.6%を記録しており推論特化では最高水準。GPQA Diamond 94.3%で首位。ScreenSpot-Pro 72.7%（7倍改善）でコンピュータ操作でも急進。2Mコンテキスト対応で$2/$12の価格設定。

**2026年4月の新製品**:
- **Gemini 3.1 Flash-Lite**: 最速・最安価モデル。エッジデバイス向け [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)
- **Gemini 3.1 Flash Live**: リアルタイム音声対話でComplexFuncBench Audio 90.8%達成 [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)
- **Gemma 4**: Gemini 3研究技術ベースのオープンモデル群。Arena Elo 1452、AIME 2026 89.2%、LiveCodeBench 80.0%。140言語対応、128Kコンテキスト。Apache 2.0ライセンス [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)
- **Lyria 3 Pro**: 3分曲生成、段落レベル制御 [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)

直近の動き: (1) Search Liveを200カ国以上に拡大 [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)。(2) Personal IntelligenceをAI Mode、Chrome、Geminiアプリに拡張。(3) 6つのエージェントプロトコル同時公開（ADK、A2A、Vertex AI Agent Builder等）。(4) Project Maven再参入——2018年の社員抗議で撤退した軍事AIに6年ぶりに復帰 [INFO-044](../Information/2026-03-21/collected-raw.md#INFO-044)。(5) Gemini Robotics + Boston Dynamics Atlas統合、Hyundaiと2028年量産目標 [INFO-028](../Information/2026-03-07/collected-raw.md#INFO-028)。(6) Google AI Edge GalleryでAgent Skills体験可能 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。(7) **Gemini 3.1 Pro SWE-bench 80.6%で首位獲得** [INFO-053](../Information/2026-03-28/collected-raw.md#INFO-053)。

## 何をやろうとしているか

### 全プロダクトにGeminiを溶かし込む（H-GOO-001、確度57%）

Geminiを検索、Gmail、Drive、Workspace、Android、Chromeすべてに統合する戦略。方向性は一貫しているが、実行品質に課題が残る。

Search Liveが200カ国以上に拡大し、AI Mode利用可能地域が大幅に増加 [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)。Personal IntelligenceがAI Mode、Chrome、Geminiアプリに拡張。Workspace CLI MCP統合でGmail/DriveがAIエージェントから直接操作可能 [INFO-025](../Information/2026-03-08/collected-raw.md#INFO-025)。

ただし確度は57%で維持。Arbiterの確証バイアス警告が継続。反証証拠なしで確度上昇を停止。Thele v. Google LLC集団訴訟（Geminiを無断でGmail/Chat/Meetに有効化）。Assistant→Gemini移行延期。金融タスクでの幻覚率76.7%（ChatGPTの約4倍）。統合を急ぐあまり品質が追いつかないリスクが残る。

### Vertex AIでクラウド市場を追い上げる（H-GOO-002、確度53%）

Vertex AI + GeminiでAWS・Azureとのクラウドシェア差を縮める。$2/$12の価格設定は2Mコンテキスト込みで競争力がある。ADK統合エコシステムは25以上のパートナーに拡大 [INFO-014](../Information/2026-03-07/collected-raw.md#INFO-014)。**Gemini APIに新価格ティア「Flex」「Priority」を導入** [INFO-010](../Information/2026-04-06/collected-raw.md#INFO-010)。FlexはStandard APIの50%価格（レイテンシ増加許容）、Priorityは高信頼性・低レイテンシ向け。

確度は53%で維持。確証バイアス警告継続。クラウドAI市場でのAnthropic（Bedrock経由）やOpenAI（Azure経由）との直接比較データが不足。

### 研究ブレークスルーで新カテゴリを作る（H-GOO-003、確度54%）

DeepMindの研究力でAIの応用領域そのものを広げる。3つの仮説の中で最も確度が高い。

**Gemma 4**はこの方向性の最新の成果 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。Arena Elo 1452はオープンモデルとして最高水準。AIME 2026 89.2%、LiveCodeBench 80.0%、τ2-bench（エージェントツール使用）86.4%。140言語対応、128Kコンテキスト。LiteRT-LMでRaspberry Pi 5で動作（133 prefill tokens/s）。エッジからPCまでカバーする製品群。

Gemini Robotics + Boston Dynamics Atlas統合が物理世界AIの商用化に最も近い事例。Hyundaiとの2028年量産目標は研究フェーズから事業フェーズへの移行を意味する。IMO-ProofBench 90%、Erdős問題4問解決は数学推論での突出した能力。AGI Cognitive Frameworkの公開は、AGI研究のフレーム設定で主導権を取る動き。

## 強みと弱み

Googleの強みはベンチマーク性能、配布規模、自己資金力、研究深度の4つが同時にある点。ARC-AGI-2は2位だがGPQA Diamond 94.3%で首位。Gemini MAU 6.5億は競合の到達できない配布規模。外部調達が不要で長期戦に耐える。DeepMindの研究力はロボティクス、数学推論、AGIフレームワークと幅広い。**Gemma 4**でオープンモデル領域でも主導権を握った [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。

弱みは、ARC-AGI-2で首位を失ったこと（83.3% vs 77.1%、6.2pt差）。統合の実行品質が追いついていないこと（幻覚率76.7%、移行延期、集団訴訟）。確証バイアスリスク（全仮説の支持証拠がI=0で反証不在）。エンタープライズ直接営業力がOpenAIやAnthropicに劣る点。Project Maven復帰が技術者採用や企業ブランドに与える影響は未知数。

## I&W監視ポイント

この企業に関連するI&W指標の状況:

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | Gemini 3.1 Pro SWE-bench 80.6%、ARC-AGI-2 77.1%。Gemma 4 Arena Elo 1452 |
| [IND-004](../config/indicators.json) OSS性能到達 | elevated | approaching | Gemma 4 31B IT Thinking: Arena Elo 1452、AIME 89.2% |
| [IND-006](../config/indicators.json) エージェントスタック競争 | elevated | rising | Gemini 3.1 Flash Live、ADK 25+パートナー、Gemma 4 Agent Skills |

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| ARC-AGI-2でのGPT-5.4 Proとの差 | 首位奪還するか、さらに引き離されるか | 77.1% vs 83.3%、6.2pt差 ([IND-001](../config/indicators.json), high) |
| Gemma 4の開発者採用 | オープンモデル戦略が定着するか | Arena Elo 1452。Apache 2.0ライセンス。Google AI Edge #8 (iOS productivity) |
| Gemini 3.1 Flash-Lite/Flash Liveの浸透 | エッジとリアルタイム音声で差別化 | Flash-Lite最速最安価、Flash Live 90.8% Audio |
| Thele v. Google LLC訴訟の進展 | 集団訴訟化すれば統合戦略に法的制約 | 2025年11月提訴 |
| Project Maven再参入の影響 | 技術者の離職や世論の反発が起きるか | 6年ぶり復帰、社内の反応は未報告 |
| Gemini Robotics量産化 | 2028年Hyundai目標に向けた進捗 | Atlas統合完了、量産は未開始 |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-06 | Gemma 4（Arena Elo 1452、AIME 89.2%）、Gemini 3.1 Flash-Lite/Flash Live、Search Live 200カ国、Gemini API Flex/Priorityティアを追加。H-GOO-001/002/003確度57%/53%/54%に更新。I&W監視ポイント更新 |
| 2026-03-28 | Gemini 3.1 Pro / Flash Liveリリース反映。SWE-bench 80.6%、ARC-AGI-2 77.1%、ComplexFuncBench Audio 90.8%を追加。H-GOO-001/002/003確度54%/52%/54%に更新。I&W監視ポイント表追加 |
| 2026-03-24 | 2週間分統合。GPQA Diamond 94.3%首位追加。6エージェントプロトコル同時公開。Project Maven再参入。Gemini Robotics+Hyundai 2028年量産目標 |
| 2026-03-09 | GPT-5.4 Pro（83.3%）にベンチマーク首位を奪われた事実を反映 |
| 2026-02-23 | 初版作成 |
