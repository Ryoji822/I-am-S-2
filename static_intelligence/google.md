# Google / DeepMind

> 最終更新: 2026-04-23
> 確度: 高

GPQA Diamond 94.3%で評価首位。**Gemini 3.1 ProがMMMU-Pro 88.21%で首位**に立ち [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)、マルチモーダル&グラウンデッドリーダーボードでも95.0%を維持 [INFO-023](../Information/2026-04-13/collected-raw.md#INFO-023)。ただしSWE-benchではClaude Opus 4.7に首位を明け渡し [INFO-025](../Information/2026-04-13/collected-raw.md#INFO-025)、ARC-AGI-2ではGPT-5.4 Proの83.3%に6.2pt差で敗れている。

2026年4月下旬、Googleは3つの層で同時に動いた。**Deep Research Max**がGemini 3.1 Pro搭載の自律リサーチエージェントとしてMCP対応で登場——FactSet、S&P Global、PitchBookとMCPサーバー提携 [INFO-004](../Information/2026-04-22/collected-raw.md#INFO-004)。**Geminiのトラフィックシェアが27%に到達**——2025年8月の13.8%から約2倍 [INFO-014](../Information/2026-04-22/collected-raw.md#INFO-014)。そして**PentagonがGemini AIモデルの機密設定での展開を交渉中**——Anthropic排除後の軍事AI再構築でGoogleが台頭 [INFO-027](../Information/2026-04-22/collected-raw.md#INFO-027)。ベンチマーク首位よりも「AIをどこにでも埋め込む」戦略の実行に軸足がある。

Cloud Next 2026でその戦略が定量的裏付けを得た——顧客の**75%がAI製品を使用**、330社が年間1兆トークン以上を処理、API経由で毎分**160億トークン** [INFO-017](../Information/2026-04-23/collected-raw.md#INFO-017)。**$750Mパートナーファンド**と**Gemini Enterprise Agent Platform**でエンタープライズAIを体系化 [INFO-010](../Information/2026-04-23/collected-raw.md#INFO-010)。**TPU 8t（訓練）**と**TPU 8i（推論）**の次世代チップも発表した [INFO-015](../Information/2026-04-23/collected-raw.md#INFO-015)。

## この会社は何物か

Sundar Pichai率いるテクノロジー企業。主力はGemini 3.1シリーズ（Pro/Flash/Flash-Lite/Flash Live/Flash TTS）、Vertex AI、Google Workspace、Google Cloud、Gemma 4。従業員180,000人以上。

他のAI専業企業と根本的に違う点が2つある。外部の資金調達が不要なこと。そして検索・Gmail・Drive・Workspace・Android・Chromeという20億人規模のユーザーベースがそのまま配布チャネルになること。開発競争が長期化するほど、この2つが効いてくる。

Gemini 3.1 ProはARC-AGI-2で77.1%（前世代31.1%から146%向上）だが、GPT-5.4 Proの83.3%に6.2pt劣後。**MMMU-Pro 88.21%で首位** [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。Gemini 3 Deep ThinkはARC-AGI-2で84.6%を記録。GPQA Diamond 94.3%で首位。2Mコンテキスト対応で$2/$12の価格設定。Gemini 3.1 ProはARC-AGI-2で77.1% [INFO-047](../Information/2026-04-22/collected-raw.md#INFO-047)。

**2026年4月の新製品・機能**:
- **Gemini Enterprise Agent Platform**: エンタープライズ向けエージェントプラットフォーム。Cloud Next 2026で発表 [INFO-010](../Information/2026-04-23/collected-raw.md#INFO-010)
- **$750M AIパートナーファンド**: エコシステム構築への大規模投資 [INFO-010](../Information/2026-04-23/collected-raw.md#INFO-010)
- **TPU 8t/8i**: 次世代TPU。8tは訓練向け、8iは推論向け [INFO-015](../Information/2026-04-23/collected-raw.md#INFO-015) [INFO-016](../Information/2026-04-23/collected-raw.md#INFO-016)
- **Deep Research Max**: Gemini 3.1 Pro搭載自律リサーチエージェント。MCP対応、ネイティブチャート・インフォグラフィック生成。FactSet、S&P Global、PitchBookとMCPサーバー提携。Google Finance、NotebookLM、Google Searchにも搭載 [INFO-004](../Information/2026-04-22/collected-raw.md#INFO-004)
- **Gemini 3.1 Flash TTS**: Artificial Analysis TTSリーダーボード Elo 1,211。70+言語対応、SynthID透かし [INFO-005](../Information/2026-04-22/collected-raw.md#INFO-005)
- **Chrome Skills**: Geminiプロンプトをワンクリックツールとして保存・再利用 [INFO-006](../Information/2026-04-22/collected-raw.md#INFO-006)
- **Gemini Robotics-ER 1.6**: 視覚・空間・物理的推論の強化。計器読取93%等の実績 [INFO-060](../Information/2026-04-22/collected-raw.md#INFO-060)
- **Grok on Vertex AI**: xAI Grokモデル（Grok 4.20/4.1 Fast）をマネージドAPIで提供 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)
- **Gemini CLI subagents**: 複雑・反復・大量タスクを専門エージェントに委任 [INFO-057](../Information/2026-04-22/collected-raw.md#INFO-057)
- **Gemma 4**: Arena Elo 1452。Apache 2.0 [INFO-065](../Information/2026-04-22/collected-raw.md#INFO-065)

**市場データ**: Geminiトラフィックシェア27%（2025年8月の13.8%から約2倍）[INFO-014](../Information/2026-04-22/collected-raw.md#INFO-014)。Cloud顧客の**75%がAI製品を使用**、330社が年間1T+トークン処理、35社が10T+到達、API毎分**160億トークン** [INFO-017](../Information/2026-04-23/collected-raw.md#INFO-017)。Google Cloud売上バックログ$240B（2025年、前年比倍増）[INFO-013](../Information/2026-04-22/collected-raw.md#INFO-013)。Google Cloud Q4 2025過去最高$17.7B（YoY 48%増収）[INFO-015](../Information/2026-04-22/collected-raw.md#INFO-015)。

**Pentagon契約交渉**: Anthropic排除後、PentagonがGemini AIモデルの機密設定での展開を評価中 [INFO-027](../Information/2026-04-22/collected-raw.md#INFO-027) [INFO-028](../Information/2026-04-22/collected-raw.md#INFO-028)。2018年のProject Maven社員抗議で撤退した軍事AIに6年ぶりに復帰する可能性。

**DeepMind研究**: 10次元AGI認知フレームワーク発表 [INFO-048](../Information/2026-04-22/collected-raw.md#INFO-048)。AGI進捗の定量評価試み。

直近の動き: (1) **Cloud Next 2026**: 75%顧客AI使用・16B tokens/分・$750Mパートナーファンド・**Enterprise Agent Platform**・**TPU 8t/8i** [INFO-010](../Information/2026-04-23/collected-raw.md#INFO-010) [INFO-015](../Information/2026-04-23/collected-raw.md#INFO-015) [INFO-017](../Information/2026-04-23/collected-raw.md#INFO-017)。(2) **Deep Research Max**（Gemini 3.1 Pro搭載MCP対応自律リサーチ）[INFO-004](../Information/2026-04-22/collected-raw.md#INFO-004)。(3) **Gemini 27%トラフィックシェア** [INFO-014](../Information/2026-04-22/collected-raw.md#INFO-014)。(4) **Pentagon Gemini契約交渉** [INFO-027](../Information/2026-04-22/collected-raw.md#INFO-027)。(5) **MMMU-Pro 88.21%首位** [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。

## 何をやろうとしているか

### 全プロダクトにGeminiを溶かし込む（H-GOO-001、確度57%）

Geminiを検索、Gmail、Drive、Workspace、Android、Chromeすべてに統合する戦略。**27%のトラフィックシェア**に続き、Cloud Next 2026で**75%の顧客がAI製品を使用**、毎分**160億トークン**を処理——「AIをどこにでも埋め込む」戦略の定量裏付けが揃った [INFO-017](../Information/2026-04-23/collected-raw.md#INFO-017)。

Chrome Skillsは新たな配布チャネル——Chrome内でプロンプトをツール化 [INFO-006](../Information/2026-04-22/collected-raw.md#INFO-006)。**Enterprise Agent Platform**でエンタープライズ向けエージェントを体系化 [INFO-010](../Information/2026-04-23/collected-raw.md#INFO-010)。Workspace CLI MCP統合でGmail/DriveがAIエージェントから直接操作可能。**Pentagon契約交渉**は政府市場への新たな参入経路 [INFO-027](../Information/2026-04-22/collected-raw.md#INFO-027)。$240B Cloudバックログは長期的な収益基盤 [INFO-013](../Information/2026-04-22/collected-raw.md#INFO-013)。

確度は57%に上昇 [Arbiter v3.58](../state/arbiter-2026-04-23.md)。27%シェア+75%AI使用+16B tokens/分で定量面突破。但しトラフィック≠収益の注意継続。**確証バイアス硬い条件**: 次回I証拠を最低1件明示的に探索しない限り+1%不可。

### Vertex AIでクラウド市場を追い上げる（H-GOO-002、確度52%）

Vertex AI + GeminiでAWS・Azureとのクラウドシェア差を縮める。$2/$12の価格設定は2Mコンテキスト込みで競争力がある。**Grok on Vertex AI**は競合モデルを自社プラットフォームに載せる戦略の成熟 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。ADK統合エコシステムは25以上のパートナーに拡大。**Deep Research Max**のMCP対応で企業データ統合が加速 [INFO-004](../Information/2026-04-22/collected-raw.md#INFO-004)。

確度は52%で維持。Chrome Skills（独自統合）とVertex AI Agent Builder（Vertex依存）はI蓄積継続。

### 研究ブレークスルーで新カテゴリを作る（H-GOO-003、確度54%）

DeepMindの研究力でAIの応用領域そのものを広げる。**Deep Research MaxはDeepMind研究→Gemini製品パイプラインの最も直接的例示** [INFO-004](../Information/2026-04-22/collected-raw.md#INFO-004)。

**MMMU-Pro 88.21%で首位** [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。Gemini Flash TTS Elo 1,211で音声生成首位 [INFO-005](../Information/2026-04-22/collected-raw.md#INFO-005)。**Robotics-ER 1.6**でロボティクス実世界タスク性能が向上 [INFO-060](../Information/2026-04-22/collected-raw.md#INFO-060)。**10次元AGI認知フレームワーク**でAGI進捗の定量評価試み [INFO-048](../Information/2026-04-22/collected-raw.md#INFO-048)。Gemma 4はArena Elo 1452でオープンモデル最高水準 [INFO-065](../Information/2026-04-22/collected-raw.md#INFO-065)。

確度は54%に上昇 [Arbiter v3.57](../state/arbiter-2026-04-22.md)。Deep Research Maxが研究→製品の直接変換例として最も診断的。2連続+1%だが各回とも新規かつ独立した証拠。確証バイアス警告継続（GPT-5.4 Pro暫定マルチモーダル1位は潜在I）。

## 強みと弱み

Googleの強みはベンチマーク性能、配布規模、自己資金力、研究深度の4つが同時にある点。GPQA Diamond 94.3%首位。**MMMU-Pro 88.21%首位** [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。マルチモーダル95.0%首位 [INFO-023](../Information/2026-04-13/collected-raw.md#INFO-023)。Flash TTS Elo 1,211音声生成首位 [INFO-005](../Information/2026-04-22/collected-raw.md#INFO-005)。**27%トラフィックシェア** [INFO-014](../Information/2026-04-22/collected-raw.md#INFO-014)。**75%顧客AI使用・毎分160億トークン処理** [INFO-017](../Information/2026-04-23/collected-raw.md#INFO-017)。Gemini MAU 6.5億は競合の到達できない配布規模。外部調達不要。**Deep Research Maxで研究→製品直接変換を実証** [INFO-004](../Information/2026-04-22/collected-raw.md#INFO-004)。**$240B Cloudバックログ** [INFO-013](../Information/2026-04-22/collected-raw.md#INFO-013)。**$750Mパートナーファンド + Enterprise Agent Platform**でエンタープライズAIを体系化 [INFO-010](../Information/2026-04-23/collected-raw.md#INFO-010)。**TPU 8t/8i**で自社チップ世代交代 [INFO-015](../Information/2026-04-23/collected-raw.md#INFO-015)。Gemma 4でオープンモデル主導権。**Pentagon契約交渉**で政府市場参入の可能性 [INFO-027](../Information/2026-04-22/collected-raw.md#INFO-027)。Grok on Vertex AIでプラットフォーム包括性 [INFO-020](../Information/2026-04-19/collected-raw.md#INFO-020)。Robotics-ER 1.6でロボティクス実世界性能 [INFO-060](../Information/2026-04-22/collected-raw.md#INFO-060)。

弱みは、ARC-AGI-2で首位を失ったこと（83.3% vs 77.1%、6.2pt差）。SWE-benchでもClaude Opus 4.7に首位を明け渡した [INFO-025](../Information/2026-04-13/collected-raw.md#INFO-025)。**ARC-AGI-3で全フロンティアモデル0%**（人間100%）は推論の根本的限界示唆 [INFO-047](../Information/2026-04-22/collected-raw.md#INFO-047)。統合の実行品質に課題（幻覚率76.7%、集団訴訟）。トラフィックシェア≠収益の変換が未検証。確証バイアスリスク（2連続+1%、I=0蓄積）。

## I&W監視ポイント

この企業に関連するI&W指標の状況:

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | Gemini 3.1 Pro MMMU-Pro 88.21%首位、ARC-AGI-2 77.1%。GPT-5.4 Pro暫定マルチモーダル1位 |
| [IND-004](../config/indicators.json) OSS性能到達 | elevated | approaching | Gemma 4 Arena Elo 1452 |
| [IND-006](../config/indicators.json) エージェントスタック競争 | elevated | rising | **Enterprise Agent Platform**。Deep Research Max MCP。Chrome Skills。Grok on Vertex AI。CLI subagents |
| [IND-025](../config/indicators.json) マルチモーダル信頼性 | elevated | stable | Flash TTS Elo 1,211/70+言語。Robotics-ER 1.6。ARC-AGI-3全0%は推論限界示唆 |

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| 27%トラフィックシェア→収益変換 | トラフィック≠収益。Cloud収益シェアへの変換係数 | **75%顧客AI使用・16B tokens/分**で定量裏付け強化 [INFO-017](../Information/2026-04-23/collected-raw.md#INFO-017) |
| Pentagon Gemini契約の行方 | 軍事AI復帰が実現するか。社員反発の可能性 | 交渉中 [INFO-027](../Information/2026-04-22/collected-raw.md#INFO-027) |
| Deep Research Maxの市場浸透 | 研究→製品直接変換がビジネスになるか | MCP対応。FactSet/S&P Global/PitchBook提携 [INFO-004](../Information/2026-04-22/collected-raw.md#INFO-004) |
| ARC-AGI-2でのGPT-5.4 Proとの差 | 首位奪還するか | 77.1% vs 83.3%、6.2pt差 |
| SWE-benchでのClaude Opus 4.7との差 | コード生成系で首位を取り戻せるか | 80.6% vs 80.9%（Opus 4.7 B-1ベース値） |
| Chrome Skillsのユーザー定着 | Gemini配布の新チャネル | 英語US向けロールアウト開始 [INFO-006](../Information/2026-04-22/collected-raw.md#INFO-006) |
| Gemma 4の開発者採用 | オープンモデル戦略が定着するか | Arena Elo 1452。Apache 2.0 |
| Robotics-ER 1.6の応用範囲 | 実世界ロボティクス性能の事業化 | 計器読取93%等 [INFO-060](../Information/2026-04-22/collected-raw.md#INFO-060) |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-23 | Cloud Next 2026定量データ（75%顧客AI使用・330社1T+トークン・16B tokens/分）・$750Mパートナーファンド・Enterprise Agent Platform・TPU 8t/8iを反映してエグゼクティブサマリー・新製品・市場データ・強み・戦略方向性・I&Wを書き直し。H-GOO-001 56→57%に更新 |
| 2026-04-22 | Deep Research Max（Gemini 3.1 Pro搭載MCP対応自律リサーチ）・27%トラフィックシェア（初の定量マイルストーン）・$240B Cloudバックログ倍増・Pentagon Gemini契約交渉・MMMU-Pro 88.21%首位・Robotics-ER 1.6・10次元AGI認知フレームワーク・Gemini CLI subagentsを反映して全面書き直し。H-GOO-001 55→56%・H-GOO-003 53→54%に更新 |
| 2026-04-19 | Gemini 3.1 Flash TTS・Chrome Skills・Grok on Vertex AIを追加。H-GOO-001 57→55%・H-GOO-003 54→53%に更新 |
| 2026-04-13 | Gemini 3.1 Pro multimodal 95.0%首位・SWE-bench首位喪失を追加 |
| 2026-04-06 | Gemma 4、Gemini 3.1 Flash-Lite/Flash Live、Search Live 200カ国を追加 |
| 2026-03-28 | Gemini 3.1 Pro/Flash Liveリリース反映 |
