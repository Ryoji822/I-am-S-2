# OpenAI

> 最終更新: 2026-02-23

**$100B+調達（史上最大、$850B+評価額）でAI業界最大の資金力を持つ。Frontierプラットフォームでエンタープライズを取りつつ、Skills/Shell/CompactionでMCP上に独自の実行環境レイヤーを構築する二層戦略。注目すべきはOpenAIがMCPを採用しAAIF共同創設に参加した事実——Skills/ShellはMCPの「対抗」ではなくMCP上に構築された「囲い込みの上位レイヤー」。エンタープライズLLM支出ではAnthropicに首位を奪われ27%に後退。ベンチマークでもGemini 3.1 Proに4pt差。しかしAltmanは「2年以内にスーパーインテリジェンスの初期版」と公言し、R&D投資と商業化の両輪推進を明確化した。**

## この会社は何者か

Sam Altman率いるAI企業。主力はChatGPT、GPT-5シリーズ、OpenAI Agents SDK、Frontierプラットフォーム、Operator（CUA）。

$100B+の調達が最終段階（2026年2月、Bloomberg/TechCrunch報道）。Amazon $50B、SoftBank $30B、NVIDIA $20B、Microsoft参加。評価額$850B+。AI業界最大の資金力。Anthropicの$30Bの3倍以上。

エンタープライズAI利用がYoY 8倍、推論モデル利用は300倍に増加 [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020)。社内では95%のエンジニアがCodexを使い、一人あたり10-20の並列エージェントを管理する体制 [INFO-013](../Information/2026-02-18/collected-raw.md#INFO-013)。ただしエンタープライズLLM支出シェアは27%でAnthropic（40%）に首位を奪われた（Menlo Ventures調査）。

直近の重要な動き: (1) Assistants API 2026年8月26日廃止決定。Responses APIに一本化（OpenAI公式）。(2) OperatorがChatGPTの「エージェントモード」として統合（CUAモデル搭載、DoorDash/Instacart/Uber等と提携）。(3) Skills/Shell/Compactionの3要素をMCP上に構築（MCPを採用した上で独自レイヤーを追加）。

## 何をやろうとしているか

OpenAIの動きから、2つの戦略と1つの野望が同時に読み取れる。

**方向1: 大企業向けAIプラットフォームになる（H-OAI-001, 確度52%）**

Frontierプラットフォームを立ち上げ、HP、Intuit、Oracle、Uberが初期顧客として採用済み [INFO-013](../Information/2026-02-21/collected-raw.md#INFO-013)。Assistants API 2026年8月廃止→Responses API一本化。古いアーキテクチャを捨てて新しいインターフェースに移行する。

エンタープライズLLMシェア27%はAnthropicの40%に対して劣位だが、CIO予測では2026年にOpenAIが53%回復を見込むとする調査もある。$100B+の資金力で巻き返しを図る。

**方向2: MCP上に独自実行環境を構築し囲い込む（H-OAI-002, 確度55%）**

**v2.0で再定義。** 重要な事実: OpenAIはMCPを採用しAAIF共同創設に参加した（2025年12月、Linux Foundation）。Skills/ShellはMCPの「対抗」ではなく、**MCP上に構築された独自の上位レイヤー**。

- **Skills**: エージェントに機能を追加するパッケージ（SKILL.md マニフェスト付き）。OpenAI独自形式
- **Shell**: エージェントが動くホスト型サーバー環境。クラウド依存（AnthropicのClaude Codeローカル実行との対比）
- **Compaction**: 長時間実行のコンテキスト圧縮技術

OpenClawマーケットプレイス（700スキル）での配布囲い込みも進行中。プロトコル層は開放（MCP）だが実行環境層で囲い込むという戦略。

**復帰した野望: AGI/スーパーインテリジェンス（H-OAI-003, 確度25%, active復帰）**

**v2.0で棄却を撤回。** Altmanが「2年以内にスーパーインテリジェンスの初期版に到達しうる」「2028年末までにデータセンター内の知的能力が外部を超える」と公言（TIME誌）。ただし$100B調達・Operator商用化・Skills展開は商業化への全力投資を同時に示す。「商業化よりR&D優先」ではなく「両輪推進」が実態。

## 強みと弱み

**強み:**
- **圧倒的な資金力**: $100B+はAnthropicの3倍以上。開発競争で息切れしない
- **エンタープライズ先行者利益**: YoY 8倍成長は製品が実際に使われている証拠
- **Microsoftとの販路**: 企業へのセールスチャネルが確保済み
- **dogfoodingの強さ**: 社内95%がCodex使用。製品品質の裏付け
- **Operator/CUA**: ブラウザ操作エージェントの先行投入。DoorDash/Uber等との提携

**弱み:**
- **エンタープライズシェア後退**: 27%でAnthropicの40%に逆転された（Menlo Ventures）
- **ベンチマーク性能で後退中**: Gemini 3.1 ProにArtificial Analysis指数で4ptリード
- **Assistants API廃止リスク**: 2026年8月の強制移行で開発者離れの可能性
- **消費者の不満蓄積**: GPT-4o廃止に21,900件の反対署名 [INFO-008](../Information/2026-02-18/collected-raw.md#INFO-008)
- **Skills/Shell囲い込みの不確実性**: MCP上の上位レイヤーが開発者に受け入れられるか未知数

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| エンタープライズLLMシェア推移 | 27%→回復するか。Anthropic 40%への対抗策の効果 | Anthropic首位（[IND-008](../config/indicators.json), elevated） |
| Skills/Shell開発者定着度 | MCP上の囲い込みレイヤーが受け入れられるか | SDK v0.8.4リリース（[IND-015](../config/indicators.json), elevated） |
| Assistants API廃止後の動向 | 8月の強制移行で開発者が残るか離れるか | 8月26日廃止確定 |
| $100B調達の完了と使途 | 資金がR&Dと商業化にどう配分されるか | 最終段階（[IND-003](../config/indicators.json), high） |
