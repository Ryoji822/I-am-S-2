# Anthropic

> 最終更新: 2026-02-23

**エンタープライズLLM支出シェア40%で業界首位に立ったAI企業。Claude Code $2.5B ARR（ローンチ9ヶ月で達成）、年間収益$14B、$30B Series G（評価額$380B）。MCPは2025年12月にLinux Foundation AAIFに寄贈し業界標準となった——もはやAnthropicの競争武器ではなく共有インフラ。新たな差別化軸はClaude Code + Bun買収（2025年12月）+ Agent SDKの開発者ツールエコシステムと、安全性による規制業界での優位性。**

## この会社は何者か

Dario Amodei率いるAI企業。主力はClaude 4.6シリーズ（Opus/Sonnet/Haiku）、Claude Code、Claude Agent SDK。

資金面では、Series Gで$30Bを調達（評価額$380B、2026年2月）。年間収益$14Bで、過去3年間毎年10倍以上の成長を維持。80%がエンタープライズ直販、$100K以上支出企業が前年比7倍成長。エンタープライズLLM支出シェア40%で首位（Menlo Ventures調査、2023年12%→2026年40%、OpenAI 27%に逆転）。

**Claude Codeが最大の成長ドライバー。** ローンチ6ヶ月で$1B ARR到達、2026年2月時点で$2.5B ARR（1月1日から倍増）。ビジネスサブスクリプションは2026年初頭から4倍成長。エンタープライズが収益の50%超。GitHub Copilotに並ぶAIコーディング3大ツールの一つ。

2025年12月にBun（JavaScriptランタイム）を買収。Claude Codeの基盤インフラを内製化する戦略的動き。Bunはオープンソース（MIT）を維持。

直近の動き: (1) Claude Agent SDKへの名称変更でエージェント開発の軸であることを明示 [INFO-007](../Information/2026-02-21/collected-raw.md#INFO-007)。(2) Computer Use Agentsの構築パターンを公開 [INFO-036](../Information/2026-02-21/collected-raw.md#INFO-036)。(3) SOC2準拠のエンタープライズグレードセキュリティを確立 [INFO-016](../Information/2026-02-21/collected-raw.md#INFO-016)。(4) Infosysとの直販提携で通信・金融・製造向けに直接営業 [INFO-001](../Information/2026-02-21/collected-raw.md#INFO-001)。

価格は、Sonnet 4.6が$3/$15 [INFO-079](../Information/2026-02-18/collected-raw.md#INFO-079)、Opus 4.6は$15/$75→$5/$25に67%値下げ済み [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)。

## 何をやろうとしているか

Anthropicの戦略は「安全性」と「開発者ツール」の2つの武器を使い分ける構造。MCPはもはやAnthropicの武器ではなく業界の共有インフラとなった。

**方向1: 安全性でエンタープライズを取る（H-ANT-001, 確度62%）**

Anthropicの最大の差別化は安全性。SOC2準拠、Compliance API、ASL-3保護。金融や政府のように規制が厳しい業界では、この安全性の実績が決定的な差になる。EU AI法完全施行（2026年8月）は安全性重視企業に追い風。

エンタープライズLLM支出40%シェアはこの戦略が機能している証拠。Infosysとの直販提携は通信・金融・製造に直接売り込む動き。

**方向2: 開発者ツールエコシステムで差別化する（H-ANT-002, 確度68%）★全社仮説中最高★**

**v2.0で全面再定義。** 旧仮説「MCP二面戦略」はMCPのAAIF寄贈（2025年12月）により無効化された。MCPはAnthropic、OpenAI、Google、Microsoft、AWSが共同創設したLinux Foundation傘下のオープン標準であり、もはや特定企業の競争武器ではない。

新たな差別化軸はClaude Code + Bun + Agent SDKの開発者ツールエコシステム:
- **Claude Code $2.5B ARR**: ターミナルで直接動作、ファイルシステム・CLIアクセスが特徴。ローカル実行可能でOpenAI Shell（クラウド依存）との対比を形成
- **Bun買収（2025年12月）**: Claude Codeの基盤インフラを内製化。$1B+ 製品が依存するOSSを自社管理にする戦略的合理性
- **Agent SDK**: エージェント開発の標準SDKとしてポジショニング

この方向が正しければ、Claude Code利用者のさらなる急増やAgent SDKの外部開発者採用が見える。間違いなら、GitHub CopilotやCursorへの利用者流出が見える。

**弱まっている読み: AWSに乗る（H-ANT-003, 確度25%, 棄却候補）**

AWS経由でエンタープライズに浸透する戦略。しかし$14B ARRの80%がエンタープライズ直販であり、$30B Series Gの$380B評価額でAWS出資比率も相対的に低下。「主戦略」ではなく「一チャネル」にすぎない。

## 強みと弱み

**強み:**
- **エンタープライズ首位**: LLM支出40%シェア。2023年12%→2026年40%の急成長（Menlo Ventures）
- **Claude Code**: $2.5B ARR。9ヶ月で$0→$2.5Bは異常な成長速度。製品市場適合の決定的証拠
- **安全性リーダーシップ**: SOC2準拠、ASL-3保護。EU AI法施行で追い風
- **Bun買収**: 開発者ツール基盤の内製化で長期的な競争優位を構築
- **価格と性能のバランス**: Sonnet 4.6 $3/$15は性能対価格で優秀

**弱み:**
- **ベンチマーク首位ではない**: Gemini 3.1 ProにArtificial Analysis指数で4ptリード [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028)
- **MCP寄贈の代償**: 標準化は業界全体に利益をもたらしたが、Anthropic独自の競争優位にはならなくなった
- **価格競争の激化**: 業界全体で年10倍の価格下落。安全性だけで価格プレミアムを維持できるかが問題
- **OpenAI Skills/Shellとの実行環境競争**: OpenAIがSkills/Shellで囲い込みに成功すれば、Claude Codeのローカル実行モデルが不利になる可能性

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Claude Code ARR推移 | 開発者ツール戦略の成否を直接示す | $2.5B ARR（2026年2月）、1月から倍増 |
| エンタープライズLLMシェア推移 | 40%が持続するか。OpenAI反攻の兆候はないか | 40%首位（[IND-008](../config/indicators.json), elevated） |
| OpenAI Skills/Shell囲い込み進捗 | 成功すればClaude Codeモデルの脅威に | SDK v0.8.4リリース（[IND-015](../config/indicators.json), elevated） |
| EU AI法施行後の市場変化 | 安全性差別化が決定的に強化されるか | 2026年8月完全施行予定（[IND-023](../config/indicators.json), elevated） |
