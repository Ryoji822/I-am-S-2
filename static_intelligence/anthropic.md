# Anthropic

> 最終更新: 2026-02-21

**安全性を最大の武器にして、規制が厳しいエンタープライズ市場を狙っている。同時にMCPというオープン標準で業界の接続方式を握り、Claude Codeで開発者を繋ぎ止める二面戦略。$300億調達、年間収益$14B（3年連続10倍以上成長）。Claude Codeは開始6ヶ月で年間$1B収益に到達。ベンチマーク首位ではなくなった（Geminiに4pt差）が、安全性と開発者体験では他社に真似しにくいポジションを持つ。**

## この会社は何者か

Dario Amodei率いるAI企業。主力はClaude 4.6シリーズ（Opus/Sonnet/Haiku）とClaude Agent SDK。

資金面では、Series Gで$300億を調達（評価額$380B、GIC/Coatue主導）[INFO-015](../Information/2026-02-18/collected-raw.md#INFO-015)。年間収益$14Bで、過去3年間毎年10倍以上の成長を維持 [INFO-001](../Information/2026-02-18/collected-raw.md#INFO-001)。Claude Codeは提供開始6ヶ月で年間$1B収益に到達しており、プロダクトが市場にフィットしている証拠 [INFO-001](../Information/2026-02-18/collected-raw.md#INFO-001)。2025年12月にBunを買収し、JavaScript開発者ツールチェーンに進出。Claude Codeを軸に開発者ツールのエコシステムを作ろうとする動き。

直近の動きは4つ。(1) Claude Agent SDKへの名称変更でエージェント開発の軸であることを明示 [INFO-007](../Information/2026-02-21/collected-raw.md#INFO-007)。(2) Computer Use Agentsの構築パターンを公開し、AIにパソコンを操作させる方法を標準化 [INFO-036](../Information/2026-02-21/collected-raw.md#INFO-036)。(3) SOC2準拠のエンタープライズグレードセキュリティを確立 [INFO-016](../Information/2026-02-21/collected-raw.md#INFO-016)。(4) Infosysとの直販提携で通信・金融・製造向けに直接売り込みを開始 [INFO-001](../Information/2026-02-21/collected-raw.md#INFO-001)。

価格は、Sonnet 4.6が$3/$15 [INFO-079](../Information/2026-02-18/collected-raw.md#INFO-079)、Opus 4.6は$15/$75→$5/$25に67%値下げ済み [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)。

## 何をやろうとしているか

Anthropicの戦略は「安全性」と「MCP」の2つの武器を使い分ける二面作戦として読める。

**方向1: 安全性でエンタープライズを取る（H-ANT-001, 確度55%）**

Anthropicの最大の差別化は安全性。SOC2準拠 [INFO-016](../Information/2026-02-21/collected-raw.md#INFO-016)、Compliance API、ASL-3保護の有効化、サボタージュリスク評価の公開 [INFO-022](../Information/2026-02-18/collected-raw.md#INFO-022) など、「安全性で一歩先を行く」ポジションは他社が簡単には真似できない。金融や政府のように規制が厳しい業界では、この安全性の実績が決定的な差になる。

Infosysとの直販提携 [INFO-001](../Information/2026-02-21/collected-raw.md#INFO-001) は通信・金融・製造に直接売り込む動き。AWS経由だけでなく自前の販路を作ろうとしている（これはAWS依存仮説H-ANT-003の反証でもある）。

この方向が正しければ、FedRAMPなどの追加認証取得や政府・金融機関との大型契約が見えてくる。間違いなら、安全性の制約が開発者体験を損ね、競合がセキュリティでキャッチアップしてくる。

**方向2: MCPで入口を開き、Claude Codeで出口を押さえる（H-ANT-002, 確度52%）**

MCP（Model Context Protocol）というオープン標準でAIエージェントとツールの接続方式を業界標準にし、同時にClaude Codeで顧客を繋ぎ止める。「入口はオープン、出口はAnthropic」という二面戦略。

MCPの広がりは確か。Chrome、OWASP、Oracle、Cloudflareが対応 [INFO-024](../Information/2026-02-21/collected-raw.md#INFO-024) [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035)。Linux Foundation AAIFへの寄贈も完了し、10,000以上のMCPサーバーが公開されている。

ただし重要な注意点がある。「対応した」と「実際に業務で使っている」は別物。MCPの対応企業数は増えているが、実際の採用率の定量データはまだない。MCPが「名前だけ対応」で終わるか「本当の業界標準」になるかで、この仮説の強さが全く変わる。

**弱まっている読み: AWSに乗る（H-ANT-003, 確度30%, 棄却候補）**

AWS経由でエンタープライズに浸透する戦略。しかしInfosysとの直販提携 [INFO-001](../Information/2026-02-21/collected-raw.md#INFO-001) がAWS依存と矛盾しており、棄却に近い。

## 強みと弱み

**強み:**
- **成長速度**: 年間収益$14B、3年連続10倍以上。Claude Code $1Bは「製品が売れる」証明 [INFO-001](../Information/2026-02-18/collected-raw.md#INFO-001)
- **安全性リーダーシップ**: SOC2準拠、ASL-3保護。規制業界で武器になる [INFO-016](../Information/2026-02-21/collected-raw.md#INFO-016) [INFO-022](../Information/2026-02-18/collected-raw.md#INFO-022)
- **MCPの広がり**: Chrome/OWASP/Oracle/Cloudflare対応。業界標準を取れれば巨大な競争優位 [INFO-024](../Information/2026-02-21/collected-raw.md#INFO-024)
- **ベンチマーク実力**: GPQA Diamond新標準でリーダーポジション [INFO-081](../Information/2026-02-18/collected-raw.md#INFO-081)
- **価格戦略**: Sonnet 4.6が$3/$15で性能と価格のバランスが良い [INFO-079](../Information/2026-02-18/collected-raw.md#INFO-079)。Opus 4.6は67%値下げで$5/$25 [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)

**弱み:**
- **ベンチマーク首位ではない**: Gemini 3.1 ProにArtificial Analysis指数で4ptリードされている [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028)
- **MCP標準化の不確実性**: 標準は「推す」ことはできるが「採用を強制」はできない。対応数と実採用率は別物
- **OpenAI独自路線との競争**: OpenAIがSkills/Shell路線を成功させればMCPの意味が薄れる [INFO-038](../Information/2026-02-21/collected-raw.md#INFO-038)
- **価格競争の激化**: 業界全体で年10倍の価格下落。安全性だけで価格プレミアムを維持できるかが問題

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| MCP採用率の定量データ | 「対応」数でなく実際の「採用」率がわかれば仮説の強度が判定できる | 10,000+サーバー公開、定量データなし（IND-012, elevated） |
| 安全性認証の追加取得 | FedRAMP等が取れれば安全性差別化が決定的に強化される | SOC2取得済み |
| OpenAIの囲い込み進捗 | Skills/Shellが定着すればMCPの意味が薄れる | SDK v0.8.4リリース（IND-015, elevated） |
| 資金集中の帰結 | $1300億が2社に集中。ただし資金≠市場支配 | IND-003, high |
