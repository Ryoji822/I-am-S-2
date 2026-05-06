# Google / DeepMind

> 最終更新: 2026-05-06
> 確度: 高

Google Cloudが初の四半期$20B超えを達成した。63%の前年比増収。GenAI製品は800% YoY成長、Gemini EnterpriseはQoQ 40%成長 [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027)。だが計算能力制約でさらに成長できた可能性を示唆。バックログは$462Bに倍増した。

Gemini Enterprise Agent Platformが正式リリースされ、エージェント構築・スケール・ガバナンスの統合プラットフォームに進化した [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)。AIトークン処理は100億/分から160億/分に増加。**xAIのGrokモデルがGoogle Cloudで利用可能になり** [INFO-008](../Information/2026-05-06/collected-raw.md#INFO-008)、クロスプラットフォームの相互乗り入れが具体化した。

だがBenchLM総合でGemini 3.1 Proは93。Claude Mythos Preview（99）に6pt差をつけられている [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。H-GOO-003（フロンティア性能競争で対抗）は49%に低下し、Arbiterから**仮説修正命令**が発出された。「性能競争で対抗」という枠組みがGoogleの実際の強み（エコシステム深度・インフラ・検索統合・マルチモーダル埋め込み）を系統的に無視してきたという指摘だ。

## 基本情報

- **本社**: カリフォルニア州マウンテンビュー
- **CEO**: Sundar Pichai
- **主力製品**: Gemini 3.1シリーズ（Pro/Flash/Flash-Lite）、**Gemini Enterprise Agent Platform**、Google Workspace、Google Cloud、Gemma 4、**Agent Skillsリポジトリ** [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032)
- **推定従業員数**: 180,000人以上
- **直近の資金調達**: 外部調達不要。Anthropicに最大$40B投資（$350B評価値）

外部の資金調達が不要なこと。検索・Gmail・Drive・Workspace・Android・Chromeという20億人規模のユーザーベースがそのまま配布チャネルになること。開発競争が長期化するほど、この2つが効いてくる。

**Google Cloud Q1 2026**: $20.03B（63% YoY増）。GenAI製品800% YoY成長。Gemini Enterprise QoQ 40%成長。バックログ$462B（倍増）。AIトークン100億/分→160億/分 [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027)。

Gemini 3.1 ProはMMMU-Pro 88.21%で首位、GPQA Diamond 94.3%で首位。ARC-AGI-2では77.1%でGPT-5.4 Pro（83.3%）に6.2pt差で敗れている。2Mコンテキスト対応で$2/$12。

**Pentagon 7社契約**でGoogleが選出された [INFO-073](../Information/2026-05-06/collected-raw.md#INFO-073) [INFO-074](../Information/2026-05-06/collected-raw.md#INFO-074)。だが**Google従業員600+がCEOにPentagon契約拒否を要請**している [INFO-075](../Information/2026-05-06/collected-raw.md#INFO-075)。

## 戦略方向性

### 全プロダクトにGeminiを溶かし込む（H-GOO-001、確度56%）

Cloud顧客の**75%がAI製品を使用**。330社が年間1T+トークン処理。API毎分**160億トークン** [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)。$20B/63% YoYでCloud収益が構造的に拡大している [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027)。

Gemini Enterprise Agent Platformでエンタープライズ向けエージェントを体系化 [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)。公式Agent Skillsリポジトリを公開 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032)。$462B Cloudバックログは長期的な収益基盤。

だがAnthropic 40%>Google 21%のエンタープライズLLMシェア未解決。全Cが「投入」指標（収益・成長率）であり「シェア拡大」の成果指標ではない。

確度は56% [Arbiter v3.70](../state/arbiter-2026-05-06.md)。次回A-3以上の独立確認で+1%検討。

### Vertex AIでクラウド市場を追い上げる（H-GOO-002、確度48%）

18R+連続でI=0が継続。自己認識はあるが行動変容がない。囲い込み指標の体系的設計（Workspace/Vertex/AndroidでのGemini優位定量・AAIF/MCPでのGoogle独自拡張比率）が未達成。

MCP全社サポート [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015)、Red Hat MCP Gateway [INFO-016](../Information/2026-05-06/collected-raw.md#INFO-016)、MCP in Visual Studio [INFO-019](../Information/2026-05-06/collected-raw.md#INFO-019) は開放性のCだが、围い込み否定の診断的証拠が独立して出ていない。

確度は48% [Arbiter v3.70](../state/arbiter-2026-05-06.md)。low確定。条件付き±0%復帰: Google围い込み指標の体系的設計完了で検討。

### 研究ブレークスルーで新カテゴリを作る（H-GOO-003、確度49%）— **仮説修正命令発出**

MMMU-Pro 88.21%で首位。GPQA Diamond 94.3%で首位。だがBenchLM総合でGemini 3.1 Proは93、Claude Mythos Preview（99）に6pt差 [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。

10R連続±0%/-1%（累積55→49%）で、仮説「フロンティア性能競争で対抗」はGoogleの実際の強み（エコシステム深度・インフラ・検索統合・マルチモーダル埋め込み）を10R+捉え損ねてきた。Arbiterから**仮説修正命令**が発出され、次回までに再構成（エコシステム深度・非性能次元への修正）または棄却の決定が必要 [Arbiter v3.70](../state/arbiter-2026-05-06.md)。

確度は49% [Arbiter v3.70](../state/arbiter-2026-05-06.md)。low帯。修正未実行で更なる-1%。

## 強み・弱み・機会・脅威（SWOT）

### 強み

- 外部調達不要の自己資金力
- **$20B/63% YoY** Cloud収益、$462Bバックログ [INFO-027](../Information/2026-05-06/collected-raw.md#INFO-027)
- 20億人規模のユーザーベース（検索・Workspace・Android・Chrome）
- MMMU-Pro 88.21%首位、GPQA Diamond 94.3%首位
- **Gemini Enterprise Agent Platform**でエンタープライスAI体系化 [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)
- **公式Agent Skillsリポジトリ**公開 [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032)
- MCP全社サポート [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015)
- **xAI Grokモデル**のGoogle Cloud受け入れで相互乗り入れ実現 [INFO-008](../Information/2026-05-06/collected-raw.md#INFO-008)
- Pentagon 7社契約で選出 [INFO-073](../Information/2026-05-06/collected-raw.md#INFO-073)
- Anthropic $40B投資で二面投資構造

### 弱み

- BenchLM総合3位（93 vs Mythos 99 vs GPT-5.4 Pro 92）[INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)
- ARC-AGI-2でGPT-5.4 Proに6.2pt差（77.1% vs 83.3%）
- エンタープライズLLMシェア21%でAnthropic（40%）に劣後
- **従業員600+がPentagon契約拒否を要請** [INFO-075](../Information/2026-05-06/collected-raw.md#INFO-075)
- H-GOO-003が仮説修正命令対象（10R連続±0%/-1%）
- Anthropic $40B投資がGemini普及と矛盾する二面性
- 統合の実行品質に課題（幻覚率76.7%、集団訴訟）

### 機会

- $20B Cloud収益でエンタープライズ投資を加速
- Pentagon契約で政府市場参入
- EU AI法完全施行（2026年8月）がWorkspace統合の強みを後押し
- Agent Skillsリポジトリで開発者エコシステムを拡大

### 脅威

- Anthropicのエンタープライス猛追（40%シェア、$30B ARR）
- BenchLM首位のClaude Mythos（99）との差が拡大方向
- 従業員抗議がPentagon契約の実行リスクになる
- DeepSeek V4の価格破壊が中間層を侵食
- H-GOO-003修正命令の未実行で更なる低下

## I&W監視ポイント

| 指標 | 状態 | トレンド | 現在値 |
|------|------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | high | approaching | MMMU-Pro 88.21%首位。ARC-AGI-2 77.1%。BenchLM 93（3位）[INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) |
| [IND-006](../config/indicators.json) エージェントスタック競争 | elevated | rising | Gemini Enterprise Agent Platform [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007)。Agent Skills [INFO-032](../Information/2026-05-06/collected-raw.md#INFO-032) |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | high | rising | MCP全社サポート [INFO-015](../Information/2026-05-06/collected-raw.md#INFO-015)。Red Hat MCP Gateway [INFO-016](../Information/2026-05-06/collected-raw.md#INFO-016) |
| [IND-025](../config/indicators.json) マルチモーダル信頼性 | elevated | stable | Gemini Flash TTS。Deep Research Agent [INFO-007](../Information/2026-05-06/collected-raw.md#INFO-007) |
| [IND-030](../config/indicators.json) AI能力とリスクの二面性 | elevated | rising | Pentagon契約+従業員抗議 [INFO-075](../Information/2026-05-06/collected-raw.md#INFO-075)。CAISI事前評価 [INFO-065](../Information/2026-05-06/collected-raw.md#INFO-065) |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-05-06 | **鮮度タイムアウト対応（7日経過）**。Google Cloud $20B/63% YoY・GenAI 800%成長・Gemini Enterprise Agent Platform詳細・xAI Grok on Google Cloud・Agent Skillsリポジトリ・Pentagon契約+従業員600+抗議・BenchLM 3位（93 vs Mythos 99）・MCP全社サポート・H-GOO-003仮説修正命令発出を反映して全面書き直し。H-GOO-001 56%・H-GOO-002 48%・H-GOO-003 49%に更新 |
| 2026-04-29 | Gemini Enterprise Agent Platform・Agents CLI・Anthropic $40B投資を反映して全面書き直し |
| 2026-04-23 | Cloud Next 2026定量データを反映して書き直し |
| 2026-04-22 | Deep Research Max・$240B Cloudバックログ・Pentagon契約交渉を反映して全面書き直し |
| 2026-04-13 | Gemini 3.1 Pro multimodal 95.0%首位を追加 |
