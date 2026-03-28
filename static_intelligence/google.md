# Google / DeepMind
> 最終更新: 2026-03-28
> 確度: 高

GPQA Diamond 94.3%で評価首位を保ちつつ、ARC-AGI-2ではGPT-5.4 Proの83.3%に6.2pt差で敗れた。だが6つのエージェントプロトコルを同時公開し、Project Mavenに6年ぶりに復帰し、Gemini Robotics + Boston Dynamics Atlasで物理AIに本格参入した。ベンチマーク単独首位よりも「AIをどこにでも埋め込む」戦略の実行に軸足がある。

## この会社は何者か

Sundar Pichai率いるテクノロジー企業。主力はGemini 3.1シリーズ（Pro/Flash/Flash-Lite）、Vertex AI、Google Workspace、Google Cloud。従業員180,000人以上。

他のAI専業企業と根本的に違う点が2つある。外部の資金調達が不要なこと。そして検索・Gmail・Drive・Workspace・Android・Chromeという20億人規模のユーザーベースがそのまま配布チャネルになること。開発競争が長期化するほど、この2つが効いてくる。

Gemini 3.1 ProはARC-AGI-2で77.1%（前世代31.1%から146%向上）だが、GPT-5.4 Proの83.3%に6.2pt劣後 [INFO-043](../Information/2026-03-08/collected-raw.md#INFO-043)。Gemini 3 Deep ThinkはARC-AGI-2で84.6%を記録しており推論特化では最高水準。GPQA Diamond 94.3%で首位。ScreenSpot-Pro 72.7%（7倍改善）でコンピュータ操作でも急進。2Mコンテキスト対応で$2/$12の価格設定。Flash-Liteはエッジデバイス向け軽量モデル。

直近の動き: (1) 6つのエージェントプロトコル同時公開（ADK、A2A、Vertex AI Agent Builder等）。(2) Project Maven再参入——2018年の社員抗議で撤退した軍事AIに6年ぶりに復帰。Anthropic Pentagon契約終了と同日の動き [INFO-044](../Information/2026-03-21/collected-raw.md#INFO-044)。(3) Gemini RoboticsがBoston Dynamics Atlasに統合、Hyundaiと2028年量産目標 [INFO-028](../Information/2026-03-07/collected-raw.md#INFO-028)。(4) Google Colab MCP Serverで開発者エコシステム拡張。(5) ノースカロライナに$1Bデータセンター投資。(6) DeepMindがAGI Cognitive Framework発表。(7) **Gemini 3.1 Pro / Flash Liveリリース** [INFO-029](../Information/2026-03-28/collected-raw.md#INFO-029), [INFO-053](../Information/2026-03-28/collected-raw.md#INFO-053)。 SWE-bench 80.6%で首位獠得 [INFO-053]。

## 何をやろうとしているか

### 全プロダクトにGeminiを溶かし込む（H-GOO-001、確度53%）

Geminiを検索、Gmail、Drive、Workspace、Android、Chromeすべてに統合する戦略。方向性は一貫しているが、実行品質に課題が残る。

Workspace CLI MCP統合でGmail/DriveがAIエージェントから直接操作可能になった [INFO-025](../Information/2026-03-08/collected-raw.md#INFO-025)。Vertex AI Agent Builderの公開は開発者向けツールの強化。6つのプロトコル同時公開はエコシステム構築への本気度を示す。

ただし確度は54%→53%に微減。理由は3つ。Thele v. Google LLC集団訴訟（Geminiを無断でGmail/Chat/Meetに有効化）。Assistant→Gemini移行延期（2025年完了予定が2026年に）。金融タスクでの幻覚率76.7%（ChatGPTの約4倍）。統合を急ぐあまり品質が追いつかないリスクが残る。

### Vertex AIでクラウド市場を追い上げる（H-GOO-002、確度52%）

Vertex AI + GeminiでAWS・Azureとのクラウドシェア差を縮める。$2/$12の価格設定は2Mコンテキスト込みで競争力がある。ADK統合エコシステムは25以上のパートナーに拡大 [INFO-014](../Information/2026-03-07/collected-raw.md#INFO-014)。

確度は52%で維持。Arbiterの確証バイアス警告が継続しており、支持証拠ばかりで反証が見つかっていない状態（全証拠I=0）。反証がないから正しい、とは言えない。クラウドAI市場でのAnthropic（Bedrock経由）やOpenAI（Azure経由）との直接比較データが不足している。

### 研究ブレークスルーで新カテゴリを作る（H-GOO-003、確度54%）

DeepMindの研究力でAIの応用領域そのものを広げる。3つの仮説の中で最も確度が高い。

Gemini Robotics + Boston Dynamics Atlas統合が物理世界AIの商用化に最も近い事例。 Hyundainとの2028年量産目標は研究フェーズから事業フェーズへの移行を意味する。IMO-ProofBench 90%、Erdős問題4問解決は数学推論での突出した能力。AGI Cognitive Frameworkの公開は、AGI研究のフレーム設定で主導権を取る動き。

Project Maven再参入も、軍事AIという領域での研究の商用化と読める。 Anthropicが安全性で政府市場を失った翌日に復帰した事実は、GoogleがAnthropicとは逆の戦略的判断を下したことを示す。

**Gemini 3.1 Pro** はSWE-bench 80.6%を記録し、 Gemini 3.1 Flash Liveはリアルタイム音声対話でComplexFuncBench Audio 90.8%を達成 [INFO-029](../Information/2026-03-28/collected-raw.md#INFO-029)。ベンチマーク首位を取り戻す動きも加速している。

## 強みと弱み

Googleの強みはベンチマーク性能、配布規模、自己資金力、研究深度の4つが同時にある点。ARC-AGI-2は2位だがGPQA Diamond 94.3%で首位。 Gemini MAU 6.5億は競合の到達できない配布規模。外部調達が不要で長期戦に耐える。DeepMindの研究力はロボティクス、数学推論、AGIフレームワークと幅広い。

弱みは、ARC-AGI-2で首位を失ったこと（83.3% vs 77.1%、6.2pt差）。統合の実行品質が追いついていないこと（幻覚率76.7%、移行延期、集団訴訟）。確証バイアスリスク（全仮説の支持証拠がI=0で反証不在）。エンタープライズ直接営業力がOpenAI（Microsoft経由）やAnthropic（Accenture 30,000人研修経由）に劣る点。Project Maven復帰が技術者採用や企業ブランドに与える影響は未知数。

## I&W監視ポイント

この企業に関連するI&W指標の状況:

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | Gemini 3.1 Pro SWE-bench 80.6%、ARC-AGI-2 77.1%。GPQA 90.8%（GPT-5.4 92.0%が首位） |
| [IND-004](../config/indicators.json) OSS性能到達 | elevated | approaching | Llama 4 85.5%追い上げ継続 |
| [IND-006](../config/indicators.json) エージェントスタック競争 | elevated | rising | Gemini 3.1 Flash Live、ADK 25+パートナー |

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| ARC-AGI-2でのGPT-5.4 Proとの差 | 首位奪還するか、さらに引き離されるか | 77.1% vs 83.3%、6.2pt差 ([IND-001](../config/indicators.json), high) |
| Gemini 3.1 Pro / Flash Liveの市場浸透 | 新モデルがエンタープライズ採用を加速するか | SWE-bench 80.6%首位、Flash Live 90.8% Audio |
| Thele v. Google LLC訴訟の進展 | 集団訴訟化すれば統合戦略に法的制約 | 2025年11月提訴 |
| Google I/O 2026（5/19-20） | プロダクト統合の全貌が発表される可能性 | 開催決定 |
| Project Maven再参入の影響 | 技術者の離職や世論の反発が起きるか | 6年ぶり復帰、社内の反応は未報告 |
| Gemini Robotics量産化 | 2028年Hyundai目標に向けた進捗 | Atlas統合完了、量産は未開始 |
| エージェントプロトコル採用率 | 6プロトコル同時公開が開発者に浸透するか | ADK 25+パートナー |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-03-28 | Gemini 3.1 Pro / Flash Liveリリース反映。SWE-bench 80.6%、ARC-AGI-2 77.1%、ComplexFuncBench Audio 90.8%を追加。H-GOO-001/002/003確度54%/52%/54%に更新。I&W監視ポイント表追加。確度表示をヘッダーに追加 |
| 2026-03-24 | 2週間分統合。GPQA Diamond 94.3%首位追加。6エージェントプロトコル同時公開。Project Maven再参入（2018年以来6年ぶり）。Gemini Robotics+Hyundai 2028年量産目標。 Vertex AI Agent Builder. ScreenSpot-Pro 72.7%。$1B NCデータセンター.AGI Cognitive Framework. H-GOO-001 53%、H-GOO-002 52%、H-GOO-003 54%に更新 |
| 2026-03-09 | GPT-5.4 Pro（83.3%）にベンチマーク首位を奪われた事実を反映。ADK 25+パートナー、Workspace CLI MCP統合、Gemini Robotics+Boston Dynamics統合を追記 |
| 2026-02-23 | 初版作成 |
