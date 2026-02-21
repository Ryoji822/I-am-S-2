# Google / DeepMind

> 最終更新: 2026-02-21

**今ベンチマーク性能でいちばん強い。Gemini 3.1 ProがARC-AGI-2で77.1%を叩き出し、他社を引き離している。しかしGoogleの本当の強みはそこではなく、検索・Gmail・Drive・Workspaceという「みんなが既に使っている」プロダクトにGeminiを溶かし込めること。APIを売る競合と違い、ユーザーが意識しないうちにAIを使わせる構造を作れる。自己資金で回せるため外部調達も不要。研究・クラウド・プロダクト・ロボティクスを一社で全方位展開できるのはGoogleだけ。**

## この会社は何者か

Sundar Pichai率いるテクノロジー企業。主力はGemini 3シリーズ、Vertex AI、Google Workspace、Google Cloud。従業員180,000人以上。

他のAI企業と根本的に違うのは、外部の資金調達が要らないこと。OpenAIは$1000億、Anthropicは$300億を投資家から集めたが、Googleは自分の稼ぎでAI開発を回せる。開発競争が長引くほど有利になる構造的な強み。

性能面での実績が突出している。Gemini 3.1 ProがARC-AGI-2で77.1%（前世代Gemini 3 Pro 31.1%から146%向上）[INFO-008](../Information/2026-02-20/collected-raw.md#INFO-008)。Gemini 3 Deep ThinkはARC-AGI-2で84.6%に達しGPT-5.2/Claude Opus 4.6を上回る [INFO-082](../Information/2026-02-18/collected-raw.md#INFO-082)。Artificial Analysis指数でClaude Opus 4.6を4ptリード [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028)。数学ではGemini Deep ThinkがIMO-ProofBench 90%達成、Erdős問題4問解決 [INFO-011](../Information/2026-02-18/collected-raw.md#INFO-011)。MMMU-Pro（画像を含む複合的な理解力テスト）でも1位 [INFO-033](../Information/2026-02-21/collected-raw.md#INFO-033)。GPQA Diamond新標準でもリーダーポジション [INFO-081](../Information/2026-02-18/collected-raw.md#INFO-081)。

直近の展開が幅広い。(1) Gemini 3.1 Pro Preview（思考能力・エージェントツール使用対応）[INFO-008](../Information/2026-02-21/collected-raw.md#INFO-008)。(2) Chrome Web MCPでAIエージェントがブラウザを直接操作可能に [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035)。(3) Gemini Robotics Previewで物理空間の理解に進出 [INFO-034](../Information/2026-02-21/collected-raw.md#INFO-034)。(4) Vertex AI Agent Builderでエンタープライズ向けエージェント構築スイートを提供 [INFO-017](../Information/2026-02-21/collected-raw.md#INFO-017)。価格も$1.6/Mと業界最安水準 [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090)（xAI $30/Mの19分の1）。

研究・クラウド・プロダクト・ロボティクスの全方面を一社で同時に動かせるのは、この規模のGoogleだけ。

## 何をやろうとしているか

Googleの動きは一貫性が高く、1つの主戦略が他社より突出して明確。

**本命: 全プロダクトにGeminiを溶かし込んで囲い込む（H-GOO-001, 確度71%）**

Geminiを検索・広告・Workspace・Cloudに深く統合し、Googleプロダクト群のデータ（検索履歴/Gmail/Drive）自体をロックインとして機能させる。OpenAIやAnthropicが「APIを売る」ビジネスなのに対し、Googleは「ユーザーが既に使っているプロダクトにAIを溶かし込む」戦略。

確度71%は全仮説の中で最高。これほど高いのは、Gemini 3.1 Proの性能躍進だけでなく、Chrome Web MCP [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035)、Gemini Robotics [INFO-034](../Information/2026-02-21/collected-raw.md#INFO-034)、Vertex AI Agent Builder [INFO-017](../Information/2026-02-21/collected-raw.md#INFO-017) などプロダクト統合の証拠が多方面から出ていることによる。ただし性能が高いことと統合戦略が成功することは別問題で、単一ベンチマーク（ARC-AGI-2）への依存リスクもある。

この方向が正しければ、Google I/O 2026（5/19-20）[INFO-010](../Information/2026-02-18/collected-raw.md#INFO-010) でプロダクト統合の全貌が発表される。間違いなら、Geminiが独立ブランドとして切り出されたりAPI販売中心に転換したりする。

**もう一つの読み: Vertex AIでクラウド市場を追い上げる（H-GOO-002, 確度55%）**

Vertex AI + Geminiの組み合わせでクラウドAI市場のシェアを拡大する。Vertex AI Agent Builderの展開 [INFO-017](../Information/2026-02-21/collected-raw.md#INFO-017) と$1.6/Mの価格競争力 [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090) がこの方向を支持。Google Cloudは現在AWSの後塵を拝しているが、AIの性能と価格で巻き返しを図る。

**もう一つの読み: 研究ブレークスルーで新カテゴリを作る（H-GOO-003, 確度56%）**

DeepMindの科学研究ブレークスルー（AlphaFold後継等）でAIの応用先を新しく作り出す。ARC-AGI-2 77.1% [INFO-008](../Information/2026-02-20/collected-raw.md#INFO-008)、Gemini Robotics [INFO-034](../Information/2026-02-21/collected-raw.md#INFO-034) が研究力の証拠。最大のリスクは「研究は凄いが商用化できない」パターン。AlphaFoldは偉大だったが、直接的な収益にはなっていない。

## 強みと弱み

**強み:**
- **ベンチマーク性能トップ**: ARC-AGI-2 77.1%（146%向上）[INFO-008](../Information/2026-02-20/collected-raw.md#INFO-008)、Artificial Analysis 4ptリード [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028)、MMMU-Pro 1位 [INFO-033](../Information/2026-02-21/collected-raw.md#INFO-033)、GPQA Diamondリーダー [INFO-081](../Information/2026-02-18/collected-raw.md#INFO-081)
- **プロダクト統合力**: 検索・Gmail・Drive・Workspaceを使っている人は既にGoogleの中にいる。そこにGeminiを入れるだけ
- **自己資金**: 外部調達不要で長期戦に強い
- **価格競争力**: $1.6/Mは業界最安水準 [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090)
- **全方位展開**: 研究（DeepMind）・クラウド（Vertex AI）・プロダクト（Workspace）・ロボティクス（Gemini Robotics）を一社で同時展開

**弱み:**
- **研究→商用化の不確実性**: DeepMindの成果が収益に結びつくかは不明。AlphaFoldは偉大だったが直接的な収益にはなっていない
- **エンタープライズ直接営業力**: OpenAI（Microsoft販路）やAnthropic（Infosys提携）に対し、Google Cloudの営業力は未知数
- **無料枠の収益圧迫**: Gemini 3 Flashの無料枠は開発者獲得に有効だが、収益を圧迫するリスク
- **単一ベンチマーク依存**: ARC-AGI-2でのリードが持続するかは不明

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| ARC-AGI-2スコアの持続性 | 77.1%が一時的突出か持続的優位かで評価が変わる | IND-001, high（146%向上） |
| Google I/O 2026（5/19-20） | プロダクト統合の全貌が発表される可能性大 | 開催決定 [INFO-010](../Information/2026-02-18/collected-raw.md#INFO-010) |
| Vertex AI Agent Builder開発者数 | クラウド追い上げ仮説の検証指標 | リリース済み、採用数不明 |
| Gemini Roboticsの商用化 | Preview→プロダクトに進むかどうか | Preview公開 |
