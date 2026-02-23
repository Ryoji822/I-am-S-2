# Google / DeepMind

> 最終更新: 2026-02-23

**ベンチマーク性能で業界トップ。Gemini 3.1 ProがARC-AGI-2で77.1%を記録し他社を引き離す。しかし「統合戦略で囲い込む」仮説（H-GOO-001）はv2.0で71%→55%に大幅下降。理由: (1) Gemini Gmail統合の無断有効化で集団訴訟（Thele v. Google LLC、2025年11月）、(2) Google Assistant→Gemini移行が2026年に延期、(3) 金融タスクで76.7%幻覚率（ChatGPTの4倍）、(4) Fortune 500のGemini運用組み込みは41%のみ。技術は凄いが統合の実行品質に深刻な疑問がある。**

## この会社は何者か

Sundar Pichai率いるテクノロジー企業。主力はGemini 3シリーズ、Vertex AI、Google Workspace、Google Cloud。従業員180,000人以上。

他のAI企業と根本的に違うのは、外部の資金調達が要らないこと。開発競争が長引くほど有利になる構造的な強み。

性能面での実績が突出している。Gemini 3.1 ProがARC-AGI-2で77.1%（前世代31.1%から146%向上）[INFO-008](../Information/2026-02-20/collected-raw.md#INFO-008)。Gemini 3 Deep ThinkはARC-AGI-2で84.6% [INFO-082](../Information/2026-02-18/collected-raw.md#INFO-082)。Artificial Analysis指数でClaude Opus 4.6を4ptリード [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028)。MMMU-Pro 1位 [INFO-033](../Information/2026-02-21/collected-raw.md#INFO-033)。GPQA Diamondリーダー [INFO-081](../Information/2026-02-18/collected-raw.md#INFO-081)。

直近の展開: (1) Gemini 3.1 Pro Preview [INFO-008](../Information/2026-02-21/collected-raw.md#INFO-008)。(2) Chrome Web MCPでAIエージェントがブラウザ操作可能に [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035)。(3) Gemini Robotics Preview [INFO-034](../Information/2026-02-21/collected-raw.md#INFO-034)。(4) Vertex AI Agent Builder [INFO-017](../Information/2026-02-21/collected-raw.md#INFO-017)。価格も$1.6/Mと業界最安水準 [INFO-090](../Information/2026-02-21/collected-raw.md#INFO-090)。

A2A（Agent2Agent Protocol）はLinux Foundation AAIFに寄贈されたが、MCP主導のエコシステムに対して採用は失速気味。

## 何をやろうとしているか

Googleの動きは一貫性が高いが、統合戦略の実行品質に疑問が生じている。

**本命: 全プロダクトにGeminiを溶かし込む（H-GOO-001, 確度55%）**

**v2.0で確度71%→55%に大幅下降。** 方向性は変わらないが、深刻な反証が4件出た:

1. **プライバシー集団訴訟**: Thele v. Google LLC（2025年11月、北カリフォルニア連邦地裁）。Geminiを2025年10月にGmail/Chat/Meetユーザーに無断で有効化。メール・添付ファイルを分析し行動プロファイルを構築。カリフォルニアプライバシー法・通信法違反。EU/UK/日本/スイスではオプトアウト方式だが米国ではオプトイン不要で有効化
2. **Assistant→Gemini移行延期**: 当初2025年完了予定が2026年に延期（Google Home CPO公式）。理由はGeminiがアラーム設定・ルーティン管理等の基本タスクを処理できない機能不足。Android Auto移行は2026年3月目標
3. **幻覚率の問題**: 金融タスクでGeminiの幻覚率76.7%、ChatGPTの約4倍の不正確さ。精密さが求められるエンタープライズ利用で致命的
4. **限定的な運用浸透**: Fortune 500のうち41%のみがGeminiを少なくとも1部門で運用に組み込み。60%はまだ検証段階

統合戦略の**方向性**は正しいが、**実行品質**に深刻な課題がある。技術の凄さとプロダクトの完成度は別問題。

**もう一つの読み: Vertex AIでクラウド市場を追い上げる（H-GOO-002, 確度55%）**

Vertex AI + Geminiの組み合わせでクラウドAI市場を拡大する。$1.6/Mの価格競争力が武器。ただしクラウド直接営業力ではMicrosoft販路を持つOpenAIやInfosys提携のAnthropicに対して不確定。

**もう一つの読み: 研究ブレークスルーで新カテゴリを作る（H-GOO-003, 確度56%）**

DeepMindの研究ブレークスルーでAI応用先を創出する。ARC-AGI-2 77.1%、Gemini Robotics Previewが研究力の証拠。IMO-ProofBench 90%、Erdős問題4問解決 [INFO-011](../Information/2026-02-18/collected-raw.md#INFO-011)。最大のリスクは「研究は凄いが商用化できない」パターン。

## 強みと弱み

**強み:**
- **ベンチマーク性能トップ**: ARC-AGI-2 77.1%（146%向上）、Artificial Analysis 4ptリード、MMMU-Pro 1位
- **プロダクト規模**: 検索・Gmail・Drive・Workspaceの既存ユーザーベース（Gemini MAU 6.5億、2025年10月）
- **自己資金**: 外部調達不要で長期戦に強い
- **価格競争力**: $1.6/Mは業界最安水準
- **全方位展開**: 研究・クラウド・プロダクト・ロボティクスを一社で同時展開

**弱み:**
- **プライバシー訴訟リスク**: Thele v. Google LLCは集団訴訟に発展の可能性。EU/各国でのデータ保護規制が統合戦略を制約
- **統合の実行品質**: Assistant→Gemini移行延期、基本タスクの機能不足は「統合が技術的に可能」≠「ユーザーが受け入れる」を示す
- **幻覚率の高さ**: 金融タスク76.7%は精密分野でのエンタープライズ利用に致命的
- **エンタープライズ直接営業力**: OpenAI（Microsoft）やAnthropic（Infosys）に対して直接営業力が弱い
- **A2A失速**: MCP主導のエコシステムに対してA2A採用は停滞気味

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Thele v. Google LLC訴訟の進展 | 集団訴訟化すれば統合戦略に法的制約 | 2025年11月提訴（[IND-023](../config/indicators.json), elevated） |
| Assistant→Gemini移行の完了 | 延期が繰り返されれば統合能力への信頼が低下 | 2026年に延期済み |
| Google I/O 2026（5/19-20） | プロダクト統合の全貌が発表される可能性 | 開催決定 [INFO-010](../Information/2026-02-18/collected-raw.md#INFO-010) |
| Gemini幻覚率の改善 | 76.7%→50%以下にしないとエンタープライズ信頼を得られない | 76.7%（[IND-001](../config/indicators.json), high） |
