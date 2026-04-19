# Google / DeepMind

> 最終更新: 2026-04-19
> 確度: 高

GPQA Diamond 94.3%で評価首位を保ちつつ、ARC-AGI-2ではGPT-5.4 Proの83.3%に6.2pt差で敗れた。**Gemini 3.1 Proがマルチモーダル&グラウンデッドリーダーボードで95.0%を記録し、この領域で首位に立った** [INFO-023](../Information/2026-04-13/collected-raw.md#INFO-023)。Gemma 4（Arena Elo 1452）でオープンモデルの新基準を打ち立て、Gemini 3.1 Flash-Lite/Flash Liveでエッジとリアルタイム音声の両面を制した。ただしSWE-benchではClaude Opus 4.6（80.8%）に首位を明け渡し、80.6%で2位に後退 [INFO-025](../Information/2026-04-13/collected-raw.md#INFO-025)。

2026年4月中旬、3つの動きが同時に進んだ。**Gemini 3.1 Flash TTS**がArtificial Analysis TTSリーダーボードでElo 1,211を達成、70+言語対応 [INFO-009](../Information/2026-04-19/collected-raw.md#INFO-009)。**Chrome Skills**がGeminiプロンプトをワンクリックツールとして保存・再利用できる機能を追加 [INFO-008](../Information/2026-04-19/collected-raw.md#INFO-008)。そして**GrokモデルがVertex AIで提供開始**——競合モデルを自社プラットフォームに載せるという、プラットフォーム戦略の成熟を示す動き [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。ベンチマーク単独首位よりも「AIをどこにでも埋め込む」戦略の実行に軸足がある。

## この会社は何物か

Sundar Pichai率いるテクノロジー企業。主力はGemini 3.1シリーズ（Pro/Flash/Flash-Lite/Flash Live/Flash TTS）、Vertex AI、Google Workspace、Google Cloud、Gemma 4。従業員180,000人以上。

他のAI専業企業と根本的に違う点が2つある。外部の資金調達が不要なこと。そして検索・Gmail・Drive・Workspace・Android・Chromeという20億人規模のユーザーベースがそのまま配布チャネルになること。開発競争が長期化するほど、この2つが効いてくる。

Gemini 3.1 ProはARC-AGI-2で77.1%（前世代31.1%から146%向上）だが、GPT-5.4 Proの83.3%に6.2pt劣後 [INFO-043](../Information/2026-03-08/collected-raw.md#INFO-043)。Gemini 3 Deep ThinkはARC-AGI-2で84.6%を記録しており推論特化では最高水準。GPQA Diamond 94.3%で首位。ScreenSpot-Pro 72.7%（7倍改善）でコンピュータ操作でも急進。2Mコンテキスト対応で$2/$12の価格設定。

**2026年4月の新製品・機能**:
- **Gemini 3.1 Flash TTS**: Artificial Analysis TTSリーダーボード Elo 1,211。70+言語対応、ネイティブマルチスピーカー対話、オーディオタグ精密制御、SynthID透かし [INFO-009](../Information/2026-04-19/collected-raw.md#INFO-009)
- **Chrome Skills**: Geminiプロンプトをワンクリックツールとして保存・再利用。「/」または「+」で呼び出し、複数タブコンテキストで実行。Mac/Windows/ChromeOS、英語US向け [INFO-008](../Information/2026-04-19/collected-raw.md#INFO-008)
- **Grok on Vertex AI**: xAI Grokモデル（Grok 4.20/4.1 Fast）をマネージドAPIで提供開始 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)
- **Gemini 3.1 Flash-Lite**: 最速・最安価モデル。エッジデバイス向け [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)
- **Gemini 3.1 Flash Live**: リアルタイム音声対話でComplexFuncBench Audio 90.8%達成 [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)
- **Gemma 4**: Gemini 3研究技術ベースのオープンモデル群。Arena Elo 1452、AIME 2026 89.2%、LiveCodeBench 80.0%。Apache 2.0 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)
- **Lyria 3 Pro**: 3分曲生成、段落レベル制御 [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)

直近の動き: (1) **Gemini 3.1 Flash TTS Elo 1,211/70+言語** [INFO-009](../Information/2026-04-19/collected-raw.md#INFO-009)。(2) **Chrome Skills**でGemini配布の新チャネル [INFO-008](../Information/2026-04-19/collected-raw.md#INFO-008)。(3) **Grok on Vertex AI**でプラットフォーム戦略の成熟 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。(4) **Gemini 3.1 Pro multimodal 95.0%首位** [INFO-023](../Information/2026-04-13/collected-raw.md#INFO-023)。(5) SWE-bench 80.6%→Claude Opus 4.6に首位明け渡し [INFO-025](../Information/2026-04-13/collected-raw.md#INFO-025)。(6) Project Maven再参入——2018年の社員抗議で撤退した軍事AIに6年ぶりに復帰 [INFO-044](../Information/2026-03-21/collected-raw.md#INFO-044)。

## 何をやろうとしているか

### 全プロダクトにGeminiを溶かし込む（H-GOO-001、確度55%）

Geminiを検索、Gmail、Drive、Workspace、Android、Chromeすべてに統合する戦略。方向性は一貫しているが、実行品質に課題が残る。

Search Liveが200カ国以上に拡大し、AI Mode利用可能地域が大幅に増加 [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)。**Chrome Skills**は新たな配布チャネル——Chrome内でプロンプトをツール化し、複数タブのコンテキストで実行 [INFO-008](../Information/2026-04-19/collected-raw.md#INFO-008)。これはGeminiの利用を日常化する動きだが、同時にChrome独自統合による囲い込み（H-GOO-002のI証拠）でもある。Workspace CLI MCP統合でGmail/DriveがAIエージェントから直接操作可能 [INFO-025](../Information/2026-03-08/collected-raw.md#INFO-025)。

確度は55%に低下 [Arbiter v3.54](../state/arbiter-2026-04-19.md)。11R連続I=0で10R仮説見直し閾値到達。Chrome Skills・Vertex AIはCだが、I証拠の体系的探索不足の累積的意味。市場シェア定量データ不在による上限キャップ継続。Thele v. Google LLC集団訴訟（Geminiを無断でGmail/Chat/Meetに有効化）は未解決。

### Vertex AIでクラウド市場を追い上げる（H-GOO-002、確度52%）

Vertex AI + GeminiでAWS・Azureとのクラウドシェア差を縮める。$2/$12の価格設定は2Mコンテキスト込みで競争力がある。ADK統合エコシステムは25以上のパートナーに拡大 [INFO-014](../Information/2026-03-07/collected-raw.md#INFO-014)。**Grok on Vertex AI**は競合モデルを自社プラットフォームに載せる戦略の成熟を示す [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。Google Cloudの既存認証・IAMインフラでアクセス可能。

確度は52%で維持。Chrome Skills（独自統合）とVertex AI Agent Builder（Vertex依存）はI蓄積継続。MCP採用はCだがI証拠探索不足の累積的意味。

### 研究ブレークスルーで新カテゴリを作る（H-GOO-003、確度53%）

DeepMindの研究力でAIの応用領域そのものを広げる。

**Gemini 3.1 Proがマルチモーダル&グラウンデッドリーダーボードで95.0%を記録**し、この領域で首位を獲得 [INFO-023](../Information/2026-04-13/collected-raw.md#INFO-023)。**Gemini 3.1 Flash TTSがElo 1,211で音声生成でも首位に** [INFO-009](../Information/2026-04-19/collected-raw.md#INFO-009)。70+言語対応、ネイティブマルチスピーカー対話、SynthID透かしによるAI生成音声の識別。

**Gemma 4**はこの方向性のもう一つの成果 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。Arena Elo 1452はオープンモデルとして最高水準。31BモデルがMRCR v2 128Kで66.4%（前世代13.5%から大幅改善）[INFO-026](../Information/2026-04-13/collected-raw.md#INFO-026)。

確度は53%に低下 [Arbiter v3.54](../state/arbiter-2026-04-19.md)。11R連続I=0で10R閾値到達。確証バイアス警告の実効性なき累積を是正。市場シェア定量データ不在による上限キャップ継続。

## 強みと弱み

Googleの強みはベンチマーク性能、配布規模、自己資金力、研究深度の4つが同時にある点。ARC-AGI-2は2位だがGPQA Diamond 94.3%で首位。**Gemini 3.1 Proがマルチモーダル95.0%で首位** [INFO-023](../Information/2026-04-13/collected-raw.md#INFO-023)。**Gemini 3.1 Flash TTSがElo 1,211で音声生成首位** [INFO-009](../Information/2026-04-19/collected-raw.md#INFO-009)。Gemini MAU 6.5億は競合の到達できない配布規模。外部調達が不要で長期戦に耐える。DeepMindの研究力はロボティクス、数学推論、AGIフレームワークと幅広い。**Gemma 4**でオープンモデル領域でも主導権を握った [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。**Chrome Skills**で配布チャネルの新たな層を開拓 [INFO-008](../Information/2026-04-19/collected-raw.md#INFO-008)。**Grok on Vertex AI**でプラットフォームの包括性を強化 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。

弱みは、ARC-AGI-2で首位を失ったこと（83.3% vs 77.1%、6.2pt差）。SWE-benchでもClaude Opus 4.6（80.8%）に首位を明け渡した [INFO-025](../Information/2026-04-13/collected-raw.md#INFO-025)。コード生成系ベンチマークでの優位性が揺らいでいる。統合の実行品質が追いついていないこと（幻覚率76.7%、移行延期、集団訴訟）。確証バイアスリスク（全仮説の支持証拠がI=0で反証不在、11R連続）。エンタープライズ直接営業力がOpenAIやAnthropicに劣る点。

## I&W監視ポイント

この企業に関連するI&W指標の状況:

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | Gemini 3.1 Pro multimodal 95.0%首位、ARC-AGI-2 77.1%。Gemma 4 Arena Elo 1452 |
| [IND-004](../config/indicators.json) OSS性能到達 | elevated | approaching | Gemma 4 31B IT Thinking: Arena Elo 1452、MRCR v2 128K 66.4% |
| [IND-006](../config/indicators.json) エージェントスタック競争 | elevated | rising | Gemini 3.1 Flash TTS Elo 1,211。Chrome Skills。Grok on Vertex AI。ADK 25+パートナー |
| [IND-025](../config/indicators.json) マルチモーダル信頼性 | elevated | stable | Gemini Flash TTS Elo 1,211/70+言語。Opus 4.7 Vision 3x。音声・視覚双方で性能向上 |

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| ARC-AGI-2でのGPT-5.4 Proとの差 | 首位奪還するか、さらに引き離されるか | 77.1% vs 83.3%、6.2pt差 ([IND-001](../config/indicators.json), high) |
| SWE-benchでのClaude Opus 4.6との差 | コード生成系で首位を取り戻せるか | 80.6% vs 80.8%、0.2pt差で2位 [INFO-025](../Information/2026-04-13/collected-raw.md#INFO-025) |
| Chrome Skillsのユーザー定着 | Gemini配布の新チャネルが定着するか | 英語US向けロールアウト開始 [INFO-008](../Information/2026-04-19/collected-raw.md#INFO-008) |
| Gemini 3.1 Flash TTSの市場浸透 | 音声生成首位が製品差別化に直結するか | Elo 1,211、70+言語。Google AI Studio/Vertex AI/Vidsで利用可能 [INFO-009](../Information/2026-04-19/collected-raw.md#INFO-009) |
| Grok on Vertex AIの意味 | 競合モデル搭載がプラットフォーム優位にどう貢献するか | Grok 4.20/4.1 Fast提供開始 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020) |
| Gemma 4の開発者採用 | オープンモデル戦略が定着するか | Arena Elo 1452。Apache 2.0 |
| Thele v. Google LLC訴訟の進展 | 集団訴訟化すれば統合戦略に法的制約 | 2025年11月提訴 |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-19 | Gemini 3.1 Flash TTS（Elo 1,211/70+言語）・Chrome Skills（ワンクリックツール化）・Grok on Vertex AI（競合モデル提供開始）を追加。H-GOO-001 57→55%（11R I=0・10R閾値到達）・H-GOO-002 53→52%・H-GOO-003 54→53%に更新 |
| 2026-04-13 | Gemini 3.1 Pro multimodal 95.0%首位・SWE-bench首位喪失を追加 |
| 2026-04-06 | Gemma 4、Gemini 3.1 Flash-Lite/Flash Live、Search Live 200カ国を追加 |
| 2026-03-28 | Gemini 3.1 Pro/Flash Liveリリース反映。SWE-bench 80.6%、ARC-AGI-2 77.1%を追加 |
| 2026-03-24 | GPQA Diamond 94.3%首位・6エージェントプロトコル・Project Maven再参入を追加 |
