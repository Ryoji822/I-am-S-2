# Anthropic インテリジェンス・プロファイル

> 最終更新: 2026-02-21
> 確度: 高

## エグゼクティブ・サマリー

Anthropicは爆発的成長を遂げている。$30B Series G調達（評価額$380B）、年間収益$14B、過去3年で毎年10倍以上成長。Claude Codeが6ヶ月で$1B年間収益達成。**[更新: 2026-02-21] Infosysと提携し通信・金融・製造向けエージェント構築。SOC2準拠のエンタープライズグレードセキュリティで規制業界戦略を強化。Claude Code SDKがClaude Agent SDKに名称変更。Computer Use Agents構築パターン公開。** MCP標準化がChrome/OWASP/Oracle対応で加速。Bun買収で開発者ツールチェーン統合中。ASL-3保護有効化とサボタージュリスク公開で安全性リーダーシップを強化。

## 基本情報

- 本社: 米国カリフォルニア州サンフランシスコ
- CEO: Dario Amodei
- 主力製品: Claude 4.6シリーズ（Opus/Sonnet/Haiku）、Claude Code、Claude Agent SDK
- 推定従業員数: 非公開（急拡大中）
- 直近の資金調達: Series G $30B（評価額$380B）、GIC/Coatue主導 [INFO-015](../Information/2026-02-18/collected-raw.md#INFO-015)

## 戦略方向性

### 現在の主力仮説

**H-ANT-001: 安全性差別化エンタープライズ戦略**（確度: 55%、~~54%~~ → **55%**）[更新: 2026-02-21]
Anthropicは安全性を差別化要因として、規制準拠が求められるエンタープライズ市場で優位に立つ。**SOC2準拠・Compliance API・Infosys提携が規制業界戦略を支持（+1%）。** [INFO-001](../Information/2026-02-21/collected-raw.md#INFO-001) [INFO-003](../Information/2026-02-21/collected-raw.md#INFO-003) [INFO-016](../Information/2026-02-21/collected-raw.md#INFO-016)。競合比較不在だが方向性は正しい（Arbiter判断）。

### 代替仮説

**H-ANT-002: MCP標準化エコシステム戦略**（確度: 52%、~~51%~~ → **52%**）[更新: 2026-02-21]
AnthropicはMCP（Model Context Protocol）を通じてAgent間連携の標準を確立し、エコシステム戦略で勝つ。**MCP採用拡大継続（Chrome/OWASP/Oracle対応）（+1%）。** [INFO-024](../Information/2026-02-21/collected-raw.md#INFO-024) [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035)。Arbiter判断: 「対応」と「採用」の区別必要。

**H-ANT-003: AWS提携深化戦略**（確度: 30%、~~33%~~ → **30%**）[更新: 2026-02-21]
~~AnthropicはAmazonとの戦略的提携を深化させ、AWS経由でのエンタープライズ浸透を主戦略とする~~。**Infosys直販提携はAWS依存戦略と矛盾（-3%）。** [INFO-001](../Information/2026-02-21/collected-raw.md#INFO-001)。棄却候補として監視継続（Arbiter判断）。

## 主要動向タイムライン

| 日付 | イベント | 信頼性 | 引用 |
|------|---------|-------|------|
| 2026-02-21 | Claude Code SDK → Claude Agent SDKに名称変更 | A-3 | [INFO-007](../Information/2026-02-21/collected-raw.md#INFO-007) |
| 2026-02-21 | Computer Use Agents構築パターン公開 | B-3 | [INFO-036](../Information/2026-02-21/collected-raw.md#INFO-036) |
| 2026-02-21 | Claude Code SOC2準拠（エンタープライズグレードセキュリティ） | B-3 | [INFO-016](../Information/2026-02-21/collected-raw.md#INFO-016) |
| 2026-02-17 | Infosys提携、通信・金融・製造向けエージェント構築 | A-3 | [INFO-001](../Information/2026-02-21/collected-raw.md#INFO-001) |
| 2026-02-19 | Claude Agent SDK v0.2.47リリース、高頻度更新継続 | A-3 | [INFO-006](../Information/2026-02-20/collected-raw.md#INFO-006) |
| 2026-02-17 | Claude Agent SDK v0.2.45リリース、Sonnet 4.6対応 | A-3 | [INFO-014](../Information/2026-02-18/collected-raw.md#INFO-014) |
| 2026-02-17 | Claude Sonnet 4.6 Bedrock提供開始 | A-3 | [INFO-063](../Information/2026-02-18/collected-raw.md#INFO-063) |
| 2026-02-17 | GPQA Diamond新標準、Claude Opusが上位 | A-3 | [INFO-081](../Information/2026-02-18/collected-raw.md#INFO-081) [INFO-085](../Information/2026-02-18/collected-raw.md#INFO-085) |
| 2026-02-12 | $30B Series G調達完了、評価額$380B、年間収益$14B | A-3 | [INFO-015](../Information/2026-02-18/collected-raw.md#INFO-015) |
| 2026-02-05 | Claude Opus 4.6発表、エージェントコーディング性能トップ | A-3 | [INFO-016](../Information/2026-02-18/collected-raw.md#INFO-016) |
| 2026-02-05 | サボタージュリスク評価公開、「非常に低いが無視できない」 | A-3 | [INFO-022](../Information/2026-02-18/collected-raw.md#INFO-022) |
| 2025-12-03 | Bun買収、Claude Code $1B年間収益達成 | A-3 | [INFO-001](../Information/2026-02-18/collected-raw.md#INFO-001) |

[更新: 2026-02-21] Claude Agent SDK名称変更、Computer Use Agents、SOC2準拠、Infosys提携追加

## 強み・弱み・機会・脅威（SWOT）

### 強み
- 圧倒的成長率（過去3年毎年10倍以上）
- $30B調達による圧倒的資金力
- Claude Code 6ヶ月で$1B収益達成（製品市場適合性確認）
- 安全性リーダーシップ（ASL-3、サボタージュリスク評価公開）
- エージェントコーディング・コンピュータ使用性能トップ

[更新: 2026-02-18]
- GPQA Diamond新標準でのリーダーシップ（Gemini 3と並ぶ上位） [INFO-081](../Information/2026-02-18/collected-raw.md#INFO-081)
- Claude Sonnet 4.6価格据え置き戦略（$3/$15） [INFO-079](../Information/2026-02-18/collected-raw.md#INFO-079)

### 弱み
- OpenAIとのエンタープライズ市場直接競争激化
- MCP標準化の成功不確実性
- AWS依存脱却後のインフラ構築コスト

### 機会
- Bun買収による開発者ツールチェーン統合
- 規制準拠企業（金融・政府）での安全性優位
- OWASP/Cloudflare等のMCP対応による標準化加速

### 脅威
- OpenAI Frontierのエンタープライズ統合
- ByteDance Seed 2.0のコスト競争
- 価格競争激化（Claude高価格ポジション）

[更新: 2026-02-20]
- **Gemini 3.1 ProがArtificial Analysis指数で4ptリード、性能競争激化** [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028)
- **価格年間10倍下落傾向、Claude Opus 4.6も$15/$75→$5/$25に値下げ対応** [INFO-022](../Information/2026-02-20/collected-raw.md#INFO-022)

## I&W監視ポイント

| 指標 | ステータス | 傾向 | 現在値 |
|------|-----------|------|--------|
| IND-003 資金集中 | high | approaching | Anthropic $30B + xAI $20B = $50Bが2社に集中。上位3社シェア80%閾値接近 | [更新: 2026-02-19] elevated→high昇格。注意: 資金調達≠市場支配
| IND-006 標準形成 | elevated | rising | MCP関連情報急増、Cloudflare/OWASP/Demandbase対応 |
| IND-012 MCP採用 | elevated | rising | OWASP/Cloudflare/Demandbase等がMCP対応 |

## 変更履歴

| 日付 | 変更内容 | 根拠 |
|------|---------|------|
| 2026-02-21 | H-ANT-001確度54%→55%（SOC2準拠・Infosys提携）、H-ANT-002確度51%→52%（MCP採用拡大）、H-ANT-003確度33%→30%（Infosys直販がAWS依存と矛盾） | Arbiter判断 |
| 2026-02-21 | タイムラインにClaude Agent SDK名称変更、Computer Use Agents、SOC2準拠追加 | INFO-007, INFO-016, INFO-036 |
| 2026-02-20 | H-ANT-003確度38%→33%、Infosys直販提携がAWS依存と矛盾 | Arbiter判断 |
| 2026-02-20 | エグゼクティブ・サマリーにClaude Opus値下げ、Infosys提携追加 | INFO-003, INFO-022 |
| 2026-02-20 | タイムラインに値下げ、Infosys提携、SDK v0.2.47追加 | INFO-003, INFO-006, INFO-022 |
| 2026-02-20 | 脅威にGemini性能リード、価格競争激化追加 | INFO-022, INFO-028 |
| 2026-02-19 | H-ANT-001確度58%→54%、H-ANT-002確度53%→51% | Arbiter判断（競合比較不在、MCP対応≠採用） |
| 2026-02-19 | IND-003 elevated→high昇格 | Arbiter判断 |
| 2026-02-18 | GPQA Diamond新標準での位置づけ追加 | INFO-081, INFO-085 |
| 2026-02-18 | 価格据え置き戦略追加（$3/$15） | INFO-079 |
| 2026-02-18 | Bedrock提供開始追加 | INFO-063 |
| 2026-02-18 | 初版作成 | Arbiter判断に基づく統合分析 |
