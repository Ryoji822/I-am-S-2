# Anthropic

> 最終更新: 2026-03-01

**エンタープライズLLM支出シェア40%で業界首位に立ったAI企業。Claude Code $2.5B ARR（ローンチ9ヶ月で達成）、年間収益$14B、$30B Series G（評価額$380B）。MCPは2025年12月にLinux Foundation AAIFに寄贈し業界標準となった——もはやAnthropicの競争武器ではなく共有インフラ。新たな差別化軸はClaude Code + Bun買収（2025年12月）+ Agent SDKの開発者ツールエコシステムと、安全性による規制業界での優位性。2026年2月にVercept買収でComputer Use能力を強化し、UI操作エージェント分野に本格参入 [INFO-074](../Information/2026-03-01/collected-raw.md#INFO-074)。**

**【2026-02-27 政府経済的圧力イベント】** Trump政権がAnthropicの連邦政府機関での使用を全面禁止（6ヶ月以内段階的廃止） [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048)。DoWがAnthropicを「サプライチェーンリスク（SCR）」に指定——従来は中露等の敵対国企業にのみ適用された前例のない措置 [INFO-105](../Information/2026-03-01/collected-raw.md#INFO-105)。理由は自律兵器と大量監視への使用制限を堅持したこと [INFO-086](../Information/2026-03-01/collected-raw.md#INFO-086)。同日夜、OpenAIがDoWと機密ネットワーク展開契約を締結し「漁夫の利」構造が成立 [INFO-097](../Information/2026-03-01/collected-raw.md#INFO-097)。**

## この会社は何者か

Dario Amodei率いるAI企業。主力はClaude 4.6シリーズ（Opus/Sonnet/Haiku）、Claude Code、Claude Agent SDK。

資金面では、Series Gで$30Bを調達（評価額$380B、2026年2月）。年間収益$14Bで、過去3年間毎年10倍以上の成長を維持。80%がエンタープライズ直販、$100K以上支出企業が前年比7倍成長。エンタープライズLLM支出シェア40%で首位（Menlo Ventures調査、2023年12%→2026年40%、OpenAI 27%に逆転）。

**Claude Codeが最大の成長ドライバー。** ローンチ6ヶ月で$1B ARR到達、2026年2月時点で$2.5B ARR（1月1日から倍増）。ビジネスサブスクリプションは2026年初頭から4倍成長。エンタープライズが収益の50%超。GitHub Copilotに並ぶAIコーディング3大ツールの一つ。

2025年12月にBun（JavaScriptランタイム）を買収。Claude Codeの基盤インフラを内製化する戦略的動き。Bunはオープンソース（MIT）を維持。

直近の動き: (1) Vercept買収でComputer Use能力を強化 [INFO-052](../Information/2026-02-26/collected-raw.md#INFO-052)。(2) RSP v3.0公開、ASL-3セーフガード有効化、Frontier Safety Roadmap導入 [INFO-047](../Information/2026-02-26/collected-raw.md#INFO-047)。(3) Claude Agent SDK v0.2.58でClaude Code v2.1.58とパリティ達成 [INFO-005](../Information/2026-02-26/collected-raw.md#INFO-005)。(4) Coworkプラグインエコシステム拡張、Google Workspace/Salesforce/DocuSign統合 [INFO-011](../Information/2026-02-26/collected-raw.md#INFO-011)。

価格は、Sonnet 4.6が$3/$15 [INFO-079](../Information/2026-02-18/collected-raw.md#INFO-079)、Opus 4.6は$15/$75→$5/$25に67%値下げ済み [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)。

## 何をやろうとしているか

Anthropicの戦略は「安全性」と「開発者ツール」の2つの武器を使い分ける構造。MCPはもはやAnthropicの武器ではなく業界の共有インフラとなった。

**方向1: 安全性でエンタープライズを取る（H-ANT-001, 確度70%, -4%）**

Anthropicの最大の差別化は安全性。SOC2準拠、Compliance API、ASL-3保護。金融や政府のように規制が厳しい業界では、この安全性の実績が決定的な差になる。EU AI法完全施行（2026年8月）は安全性重視企業に追い風。

エンタープライズLLM支出40%シェアはこの戦略が機能している証拠。Infosysとの直販提携は通信・金融・製造に直接売り込む動き。

**ただし2026-02-27のSCR指定・連邦使用禁止は重要な逆風。** 政府市場（推定$100B+）と消費者App Store市場（~$10B）の規模非対称性を考慮すると、安全性堅持が政府市場では致命的なペナルティになる可能性。一方でNate Silver「Claudeはinfluential usersの間で#1 LLM」との評価 [INFO-114](../Information/2026-03-01/collected-raw.md#INFO-114) は消費者・開発者ブランド価値の上昇を示唆。**政府市場喪失 vs 消費者ブランド価値上昇の両義性**がH-ANT-001の解釈分岐点。

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
- **安全性リーダーシップ**: SOC2準拠、ASL-3保護、RSP v3.0。EU AI法施行で追い風
- **Bun買収**: 開発者ツール基盤の内製化で長期的な競争優位を構築
- **Vercept買収**: Computer Use（UI操作エージェント）能力の強化。Microsoft CUAに対抗 [INFO-052](../Information/2026-02-26/collected-raw.md#INFO-052)
- **価格と性能のバランス**: Sonnet 4.6 $3/$15は性能対価格で優秀

**弱み:**
- **政府による経済的報復リスク**: 2026-02-27に連邦使用禁止・SCR指定を受け、政府市場（推定$100B+）へのアクセスを喪失。消費者App Store市場（~$10B）とは規模が非対称 [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048)。安全性堅持が経済的ペナルティになる構造的リスク ([IND-023](../config/indicators.json), **high**)
- **ベンチマーク首位ではない**: Gemini 3.1 Pro ARC-AGI-2 77.1%に対しClaude Opus 4.5は37% [INFO-084](../Information/2026-03-01/collected-raw.md#INFO-084)
- **MCP寄贈の代償**: 標準化は業界全体に利益をもたらしたが、Anthropic独自の競争優位にはならなくなった
- **価格競争の激化**: 業界全体で年10倍の価格下落。安全性だけで価格プレミアムを維持できるかが問題
- **OpenAI Skills/Shellとの実行環境競争**: OpenAIがSkills/Shellで囲い込みに成功すれば、Claude Codeのローカル実行モデルが不利になる可能性

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Claude Code ARR推移 | 開発者ツール戦略の成否を直接示す | $2.5B ARR（2026年2月）、1月から倍増 |
| エンタープライズLLMシェア推移 | 40%が持続するか。OpenAI反攻の兆候はないか | 40%首位（[IND-008](../config/indicators.json), elevated） |
| Computer Use vs Microsoft CUA | Vercept買収が実効性ある差別化になるか | Vercept買収完了、製品は3/25シャットダウン予定 [INFO-106](../Information/2026-03-01/collected-raw.md#INFO-106) |
| 政府経済的圧力の他社への波及 | 萎縮効果が業界全体に広がるか（[H-GOV-001](../config/hypotheses.json)） | 条件1・2達成（経済的制裁+漁夫の利）、条件3（他社萎縮）未確認 ([IND-023](../config/indicators.json), **high**) |
| SCR指定解除・法廷闘争の行方 | 政府の報復措置が撤回されるか | Anthropicは法廷で争う意向 [INFO-105](../Information/2026-03-01/collected-raw.md#INFO-105) |
| EU AI法施行後の市場変化 | 安全性差別化が決定的に強化されるか | 2026年8月完全施行予定 |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-03-01 | SCR指定・連邦使用禁止イベントを追記。H-ANT-001確度62%→70%と市場規模非対称性を反映。IND-023 high昇格を監視項目に追加 |
| 2026-02-26 | Vercept買収（M&A）を追記。RSP v3.0・Cowork拡張を反映。直近動向を更新 |
| 2026-02-23 | 初版作成（Bun買収・MCP寄贈後の戦略再定義）
