# AI市場の現在地
> 最終更新: 2026-04-22

安いAIは誰でも使える。だが最先端を作れるのは3社だけ——市場はその構造に向かっている（SCN-002、40%）。同時に、インフラの物理的限界が投資効率を押し下げ始めた。DC約50%が遅延・中止、接続キュー2,100GWが総グリッド容量を超過 [INFO-016](../Information/2026-04-22/collected-raw.md#INFO-016)（[IND-029](../config/indicators.json)、**high**）。

2026年4月第3週は「エンタープライズ決戦クラスター」だった。全社同時にエンタープライズへ集中した——OpenAIがCodex Labs + GSI 7社提携、Anthropicが$30B確認 + 欧州銀行Mythos、Googleが27%シェア + $240Bバックログ + Pentagon契約交渉 [Arbiter v3.57](../state/arbiter-2026-04-22.md)。エージェント技術がエンタープライス実用の臨界点を通過した可能性を示唆する。

## プレイヤー一覧

| 企業 | 主力 | 資金 | 今の位置 |
|------|------|------|---------|
| OpenAI | GPT-5.4シリーズ、Codex（desktop control・browser・memory・90+ plugins・heartbeats）、**Codex Labs + GSI 7社**、Agents SDK（MCP統合・7社サンドボックスパートナー） | $122B調達（$852B評価額、$13.1B ARR） | ベンチマーク首位（ARC-AGI-2 83.3%、マルチモーダル暫定1位）。WAU 4M。**GSI 7社提携でB2Bチャネル質的転換** [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001) |
| Anthropic | **Claude Opus 4.7**、Claude Code、Managed Agents、Mythos Preview | $30B調達（$183B評価額、**$30B ARR A-1確認**） | エンタープライズLLM支出40%首位。**Amazon提携拡大（5GW Trainium・$100B AWS投資）** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。欧州銀行Mythos提供計画 [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008) |
| Google | Gemini 3.1シリーズ、Vertex AI、**Deep Research Max**、Gemma 4 | 自己資金 | **MMMU-Pro 88.21%首位** [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。**27%トラフィックシェア** [INFO-014](../Information/2026-04-22/collected-raw.md#INFO-014)。**$240B Cloudバックログ** [INFO-013](../Information/2026-04-22/collected-raw.md#INFO-013)。**Pentagon契約交渉** [INFO-027](../Information/2026-04-22/collected-raw.md#INFO-027) |
| xAI | Grok 4.20シリーズ、**Grok STT/TTS API** | $20B Series E（SpaceX $1.25兆合算） | STT WER 6.9%業界最良。H-XAI-004（汎用AI基盤）55%で最有力仮説 |
| ByteDance | Seed 2.0、Doubao、Seedance 2.0、Seeduplex | 非公開（評価額$520B） | 価格1/10。日次トークン120兆。**2025年純利益70%+減少** [INFO-055](../Information/2026-04-22/collected-raw.md#INFO-055) |
| Meta | Llama 4、スーパーインテリジェンスチーム | 自己資金 + CoreWeave $21B契約 | OSS性能ギャップ閉じる方向 |

## 今、市場で何が起きているか

### エンタープライズ決戦クラスターが形成された

2026年4月第3週、全社が同時にエンタープライス市場に殺到した:

- **OpenAI**: Codex Labs + GSI 7社提携（Accenture/PwC/Capgemini等）でB2Bチャネル構築の質的転換 [INFO-001](../Information/2026-04-22/collected-raw.md#INFO-001)
- **Anthropic**: $30B ARR A-1確認 + 欧州銀行Mythos提供計画で安全性差別化の市場的証明 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032) [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008)
- **Google**: 27%トラフィックシェア + $240Bバックログ + Pentagon契約交渉で定量・市場両面突破 [INFO-014](../Information/2026-04-22/collected-raw.md#INFO-014) [INFO-027](../Information/2026-04-22/collected-raw.md#INFO-027)

エージェント技術がエンタープライス実用の臨界点を通過したことを示唆する構造的転換 [Arbiter v3.57](../state/arbiter-2026-04-22.md)。

### インフラ過熱と物理的制約の確定的化

資本は限界なく流入している——**Q1 2026でAIが$242Bを吸収**、2025年全体を超過 [INFO-052](../Information/2026-04-22/collected-raw.md#INFO-052)。だが物理的制約が追いつかない。DC約50%が遅延・中止 [INFO-016](../Information/2026-04-22/collected-raw.md#INFO-016)。Amazon $200Bは需要先行から供給先行型への転換 [INFO-053](../Information/2026-04-22/collected-raw.md#INFO-053)。IEA報告でDC電力消費が2025年に17%急増 [INFO-054](../Information/2026-04-22/collected-raw.md#INFO-054)。接続キュー2,100GWが総グリッド容量を超過。

資本流入（$242B）vs物理的制約（50%遅延）の構造的ギャップが**確定的**になった。（[IND-029](../config/indicators.json)、**high**）

### AI代替の「品質の壁」が顕在化した

Klarnaが700人AI削減を誇示した後、「低品質」で静かに再採用 [INFO-039](../Information/2026-04-22/collected-raw.md#INFO-039)。Deloitte調査で54%が40%+のAI実験本番移行を計画するが、実際は25%のみ [INFO-037](../Information/2026-04-22/collected-raw.md#INFO-037)。**Reset to Zero問題**——エージェントが予告なく致命的に失敗——がエンタープライズ信頼性の構造的課題として浮上 [INFO-070](../Information/2026-04-22/collected-raw.md#INFO-070)。

理論的可能性と実際の品質ギャップが構造的障壁として認識され始めた。

### Anthropic-Pentagon-Google三角関係が新変数に

SCR指定→Pentagon Google転向→NSA黙的使用→裁判所介入の多層構造が浮上 [INFO-028](../Information/2026-04-22/collected-raw.md#INFO-028) [INFO-029](../Information/2026-04-22/collected-raw.md#INFO-029) [INFO-031](../Information/2026-04-22/collected-raw.md#INFO-031)。安全性企業を排除し、商業企業を優遇する政府の選別的介入が構造化した。（[IND-023](../config/indicators.json)、high）

### 導入は爆発的——成果は二極化

Stanford AI Index 2026: AIエージェント成功率が20%→77%に急上昇 [INFO-036](../Information/2026-04-22/collected-raw.md#INFO-036)。79%の組織がagentic AI導入中。

だが**54%計画vs25%実績**のギャップ [INFO-037](../Information/2026-04-22/collected-raw.md#INFO-037)。Klarna再採用 [INFO-039](../Information/2026-04-22/collected-raw.md#INFO-039)。Reset to Zero問題 [INFO-070](../Information/2026-04-22/collected-raw.md#INFO-070)。普及>品質成熟の構造が継続。

### 「書く」から「評価する」への大転換

AIスキル要件がエントリーレベルで3倍増 [INFO-066](../Information/2026-04-22/collected-raw.md#INFO-066)。Copilot 4.7M有料・84%開発者採用 [INFO-044](../Information/2026-04-22/collected-raw.md#INFO-044)。ジュニア開発者採用27.5-78%減 [INFO-043](../Information/2026-04-22/collected-raw.md#INFO-043) [INFO-045](../Information/2026-04-22/collected-raw.md#INFO-045)。（[IND-022](../config/indicators.json)、high）

## 寡占と分散のどちらに向かうか

**集中に向かう力**: Q1 $242BがAIに集中 [INFO-052](../Information/2026-04-22/collected-raw.md#INFO-052)。エンタープライス3社で88%シェア。政府が特定企業を選別。M&A（Anthropic-Amazon $33B、OpenAI $122B）。スイッチングコスト15-20%。

**分散に向かう力**: AAIF標準化。Gemma 4（Apache 2.0）。ByteDance価格破壊。DeepSeek V4プレビュー [INFO-062](../Information/2026-04-22/collected-raw.md#INFO-062)。MCP全社対応。

現時点では「技術は開くが、性能トップは集中する」（SCN-002、40%）が最有力。SCN-002が4割に到達し、最も支持されるシナリオとして確定的になった。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | 前世代比30%超の性能向上 | GPT-5.4 Pro ARC-AGI-2 83.3%・マルチモーダル暫定1位。Gemini MMMU-Pro 88.21% | **high approaching** |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | Q1 AI投資$242B。上位4社$190B超 | **high** |
| [IND-013](../config/indicators.json) AI安全性事故 | 大規模なAI関連事故 | 97%インシデント予期。Cowork監査ギャップ。Reset to Zero問題 | **high** rising |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理にシフト | 84%開発者採用。スキル要件3倍増。ジュニア採用27.5-78%減 | **high** rising |
| [IND-026](../config/indicators.json) エージェント本番環境到達率 | エージェントの本番稼働成功率 | Stanford 77%成功率 vs 54%計画/25%実績。Reset to Zero | elevated rising |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | MCP/A2A等のオープンスタンダード採用率 | Deep Research Max MCP対応。Agents SDK MCP。Cloudflare参照アーキテクチャ | **high** rising |
| [IND-028](../config/indicators.json) AGI到達度指標 | 主観-客観乖離 | ARC-AGI-3全0%。Amodei 6-12ヶ月予測。主観-客観乖離最大水準 | elevated rising |
| [IND-029](../config/indicators.json) AIインフラ制約 | 計算能力投資の物理的限界 | **DC約50%遅延**。Q1 $242B。Amazon $200B供給先行。IEA 17%。接続キュー2,100GW | **high** rising |
| [IND-030](../config/indicators.json) AI能力とリスクの二面性 | 高性能モデルが「最も整合性高い」同時に「最もリスク高い」 | Stanford 77%。97%インシデント予期。Reset to Zero。能力-リスク同時進行 | elevated rising |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-22 | エンタープライズ決戦クラスター・インフラ過熱-制約確定的化（IND-029 elevated→high）・AI代替品質の壁・Anthropic-Pentagon-Google三角関係・スキル要件3倍増・Q1 $242Bを反映して全面書き直し。SCN-002 37→40%に更新 |
| 2026-04-17 | 鮮度タイムアウト対応（7日経過）。72時間4社同時エージェントリリース・Codex進化・Opus 4.7 GAを反映 |
| 2026-04-10 | Anthropic $30B ARR・SCR確定・スイッチングコスト定量データを反映 |
| 2026-04-08 | シナリオ順位入れ替わり・MCP二面性を追加 |
| 2026-04-06 | Gemma 4、Doubao日次トークン120兆を追加 |
