# OpenAI

> 最終更新: 2026-03-09

**$110B調達完了（評価額$730B）でAI業界最大の資金力を確立。GPT-5.4 ProがARC-AGI-2で83.3%を達成し、初めて人間（72.4%）を超過——フロンティア性能でGemini 3.1 Pro（77.1%）を6.2pt引き離しベンチマーク首位を奪還 [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。年間収益$25Bだが黒字化見通しは立たず [INFO-022](../Information/2026-03-08/collected-raw.md#INFO-022)。Frontierプラットフォームでエンタープライズを取りつつ、Skills/Shell/CompactionでMCP上に独自の実行環境レイヤーを構築する二層戦略は継続。DoW契約締結 [INFO-002](../Information/2026-03-08/collected-raw.md#INFO-002) でAnthropic SCR指定の「漁夫の利」を獲得したが、ChatGPTアンインストール295%急増 [INFO-037](../Information/2026-03-07/collected-raw.md#INFO-037) で消費者ブランドに傷。エンタープライズLLM支出シェアは27%でAnthropic（40%）に劣後のまま。**

## この会社は何者か

Sam Altman率いるAI企業。主力はChatGPT、GPT-5.4シリーズ（GPT-5.4 Pro含む）、OpenAI Agents SDK、Frontierプラットフォーム、Operator（CUA）。

$110Bの調達が完了（2026年3月、評価額$730B） [INFO-009](../Information/2026-03-08/collected-raw.md#INFO-009)。年間収益$25B [INFO-022](../Information/2026-03-08/collected-raw.md#INFO-022)。AI業界最大の資金力。Anthropicの$30Bの約3.7倍。

GPT-5.4 Proは2026年3月にリリースされ、ARC-AGI-2で83.3%を達成——人間ベースライン（72.4%）を初めて超過した [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。前世代GPT-5.2からの明確な性能向上で、Gemini 3.1 Pro（77.1%）を6.2pt引き離しベンチマーク首位を奪還。AGI転換点指標（[IND-001](../config/indicators.json)）の90%閾値まで6.7pt。

エンタープライズAI利用がYoY 8倍、推論モデル利用は300倍に増加 [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020)。ただしエンタープライズLLM支出シェアは27%でAnthropic（40%）に首位を奪われたまま（Menlo Ventures調査）。

直近の重要な動き: (1) GPT-5.4 / GPT-5.4 Proリリース（ARC-AGI-2人間超え） [INFO-001](../Information/2026-03-08/collected-raw.md#INFO-001)。(2) DoWと機密ネットワーク展開契約を締結（国内監視禁止条項付き） [INFO-002](../Information/2026-03-08/collected-raw.md#INFO-002)。(3) AWS提携でBedrockにStateful Runtime展開 [INFO-039](../Information/2026-03-07/collected-raw.md#INFO-039)。(4) Assistants API 2026年8月26日廃止決定、Responses APIに一本化。(5) Skills/Shell/Compactionの3要素をMCP上に構築。

## 何をやろうとしているか

OpenAIの動きから、2つの戦略と1つの野望が同時に読み取れる。

**方向1: 大企業向けAIプラットフォームになる（H-OAI-001, 確度61%）**

Frontierプラットフォームを立ち上げ、HP、Intuit、Oracle、Uberが初期顧客として採用済み [INFO-013](../Information/2026-02-21/collected-raw.md#INFO-013)。Assistants API 2026年8月廃止→Responses API一本化。$110B調達と$25B年間収益がこの戦略の資金基盤。

エンタープライズLLMシェア27%はAnthropicの40%に対して劣位だが、DoW契約はAnthropic SCR指定の隙間を突いた政府市場参入（「漁夫の利」構造 [H-GOV-001](../config/hypotheses.json)）。一方でChatGPTアンインストール295%急増 [INFO-037](../Information/2026-03-07/collected-raw.md#INFO-037) は消費者ブランドへの逆風。

**方向2: MCP上に独自実行環境を構築し囲い込む（H-OAI-002, 確度59%）**

重要な事実: OpenAIはMCPを採用しAAIF共同創設に参加した（2025年12月、Linux Foundation）。Skills/ShellはMCPの「対抗」ではなく、**MCP上に構築された独自の上位レイヤー**。

- **Skills**: エージェントに機能を追加するパッケージ（SKILL.md マニフェスト付き）。OpenAI独自形式
- **Shell**: エージェントが動くホスト型サーバー環境。クラウド依存（AnthropicのClaude Codeローカル実行との対比）
- **Compaction**: 長時間実行のコンテキスト圧縮技術

ただしAWS提携（Bedrockへのstateful runtime展開） [INFO-039](../Information/2026-03-07/collected-raw.md#INFO-039) はOpenClawの囲い込みと矛盾する開放的側面も見せており、確度は59%に微減。

**弱まった野望: AGI/スーパーインテリジェンス（H-OAI-003, 確度7%, low）**

Altmanが「2年以内にスーパーインテリジェンスの初期版」と公言するが、$110B調達・$25B年間収益（黒字化未達）・DoW契約は商業化への全力投資を示す。「商業化よりR&D優先」は確度7%まで低下。GPT-5.4 ProのARC-AGI-2 83.3%はAGI接近の技術的証拠だが、経営行動は商業化優先が明白。

## 強みと弱み

**強み:**
- **圧倒的な資金力**: $110B調達完了（$730B評価額）。開発競争で息切れしない
- **ベンチマーク首位奪還**: GPT-5.4 Pro ARC-AGI-2 83.3%で人間超え。Gemini 3.1 Proを6.2ptリード [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)
- **政府市場参入**: DoW契約でAnthropic SCR指定の隙間を突き参入 [INFO-002](../Information/2026-03-08/collected-raw.md#INFO-002)
- **Microsoftとの販路**: 企業へのセールスチャネルが確保済み
- **Operator/CUA**: ブラウザ操作エージェントの先行投入。DoorDash/Uber等との提携

**弱み:**
- **エンタープライズシェア後退**: 27%でAnthropicの40%に逆転されたまま（Menlo Ventures）
- **消費者ブランド毀損**: DoW契約後にChatGPTアンインストール295%急増 [INFO-037](../Information/2026-03-07/collected-raw.md#INFO-037)
- **黒字化未達**: $25B年間収益でも黒字化見通しが立っていない [INFO-022](../Information/2026-03-08/collected-raw.md#INFO-022)
- **Assistants API廃止リスク**: 2026年8月の強制移行で開発者離れの可能性
- **Skills/Shell囲い込みの不確実性**: MCP上の上位レイヤーが開発者に受け入れられるか未知数。AWS提携は囲い込みと矛盾

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| ARC-AGI-2 90%閾値への接近 | AGI転換点指標の鍵。83.3%から6.7pt | 83.3%（[IND-001](../config/indicators.json), high approaching） |
| エンタープライズLLMシェア推移 | 27%→回復するか。Anthropic 40%への対抗策の効果 | Anthropic首位（[IND-008](../config/indicators.json), elevated） |
| DoW契約の規模と影響 | 政府市場での収益化がエンタープライズ戦略を補完するか | 契約締結済み。消費者反発との両立が課題 |
| Skills/Shell開発者定着度 | MCP上の囲い込みレイヤーが受け入れられるか。AWS提携との整合性 | OpenClaw拡大中（[IND-015](../config/indicators.json), elevated） |
| Assistants API廃止後の動向 | 8月の強制移行で開発者が残るか離れるか | 8月26日廃止確定 |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-03-09 | GPT-5.4 Proリリース（ARC-AGI-2 83.3%人間超え）、$110B調達完了（$730B評価額）、$25B年間収益、DoW契約締結を反映。ベンチマーク首位奪還と消費者ブランド毀損の両面を記録 |
| 2026-02-23 | 初版作成（$100B+調達・Skills/Shell戦略・MCP採用の三面分析）
