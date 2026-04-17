# AI市場の現在地
> 最終更新: 2026-04-17

安いAIは誰でも使える。だが最先端を作れるのは3社だけ——市場はその構造に向かっている（SCN-002、37%）。同時に、エコシステムのロックインが「静かな囲い込み」（SCN-003、27%）を押し上げている。スイッチングコスト15-20%、74%の企業がAIベンダー喪失時に業務混乱を予想——囲い込みの定量証拠が揃った [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089) [INFO-097](../Information/2026-04-10/collected-raw.md#INFO-097)。

2026年4月15-17日、72時間の間にOpenAI（Agents SDK/Codex）、Anthropic（Opus 4.7/Agent SDK）、Google（Gemini CLI subagents）、xAI（Voice Agent API）が次々とエージェントインフラをリリースした。エージェントSDK競争が臨界質量に到達した可能性を示唆する出来事 [Arbiter v3.52](../state/arbiter-2026-04-17.md)。

GPT-5.4 ProがARC-AGI-2で83.3%を記録し、AIとして初めて人間（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。Anthropicが$30B ARR到達でOpenAI $25Bを逆転したと自己発表 [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。Gemma 4がArena Elo 1452でオープンモデルの新基準 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)、Doubaoが日次トークン120兆を処理 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。

導入と成果の間にある断崖。埋まっていない。92%の企業が正のROIを達成（2.8x平均）[INFO-038](../Information/2026-03-29/collected-raw.md#INFO-038) する一方で、40%のプロジェクトが2027年までにキャンセルのリスク [INFO-021](../Information/2026-03-29/collected-raw.md#INFO-021)。

## プレイヤー一覧

| 企業 | 主力 | 資金 | 今の位置 |
|------|------|------|---------|
| OpenAI | GPT-5.4シリーズ、Codex（desktop control・browser・memory・111 plugins・heartbeats）、Agents SDK（7社サンドボックスパートナー） | $122B調達（$852B評価額、$13.1B ARR） | ベンチマーク首位（ARC-AGI-2 83.3%）。Codexが自律型開発プラットフォームに進化。エンタープライズLLMシェア27%。**GPT-5.3-Codex 25hr連続稼働** [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006) |
| Anthropic | **Claude Opus 4.7**、Claude Code、Managed Agents、Mythos Preview | $30B調達（$183B評価額、**$30B ARR**※自己発表） | エンタープライズLLM支出40%首位。**Opus 4.7 GA**（CursorBench 70%・XBOW 98.5%）[INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。SWE-bench 80.9%首位。SCR確定。Managed Agents GA。$1M+顧客1000社突破 |
| Google | Gemini 3.1シリーズ、Vertex AI、Gemma 4 | 自己資金 | GPQA Diamond 94.3%首位。Gemini 3.1 Pro multimodal 95.0%首位。Gemma 4 Arena Elo 1452。Gemini CLI subagents追加 [INFO-012](../Information/2026-04-17/collected-raw.md#INFO-012)。Gemini 3.1 Flash TTS Elo 1,211 [INFO-008](../Information/2026-04-17/collected-raw.md#INFO-008) |
| xAI | Grok 4.20シリーズ、Grok 3 Beta、**Voice Agent API** | $20B Series E（SpaceX $1.25兆合算） | Voice Agent API（MCP・x_search・OpenAI Realtime API互換）[INFO-013](../Information/2026-04-17/collected-raw.md#INFO-013)。マルチエージェント（4/16体協調）。H-XAI-001 55%低下・H-XAI-003 52%低下 |
| ByteDance | Seed 2.0、Doubao、Seedance 2.0、Seeduplex | 非公開（評価額$520B） | 価格1/10。日次トークン120兆（2年で1000倍）。DAU 1.45億。Coze MCP対応 |
| Meta | Llama 4、スーパーインテリジェンスチーム | 自己資金 + **CoreWeave $21B契約** | スーパーインテリジェンスチーム初のAIモデル発表。OSS性能ギャップ閉じる方向 |

3社（OpenAI、Anthropic、Google）がフロンティアを形成し、xAIとByteDanceが異なる角度から挑む構図。Metaがスーパーインテリジェンスチームと$21B CoreWeave契約で新たな変数として台頭。各社の詳細は個別ファイルを参照。

## 今、市場で何が起きているか

### 72時間でエージェント競争が臨界質量に達した

2026年4月15-17日、4社が72時間以内に重大なエージェント機能をリリースした:

- **4月15日**: OpenAI Agents SDK大幅アップデート（7社サンドボックスパートナー）[INFO-010](../Information/2026-04-17/collected-raw.md#INFO-010)。Google Gemini CLI subagents追加 [INFO-012](../Information/2026-04-17/collected-raw.md#INFO-012)
- **4月16日**: Anthropic Claude Opus 4.7 GA + Claude Agent SDK TypeScript Opus 4.7対応 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011) [INFO-016](../Information/2026-04-17/collected-raw.md#INFO-016)。OpenAI Codex App大幅アップデート [INFO-014](../Information/2026-04-17/collected-raw.md#INFO-014)
- **4月17日**: xAI Voice Agent API [INFO-013](../Information/2026-04-17/collected-raw.md#INFO-013)。OpenAI Codex画像生成・heartbeats追加 [INFO-021](../Information/2026-04-17/collected-raw.md#INFO-021) [INFO-022](../Information/2026-04-17/collected-raw.md#INFO-022)

これはSCN-002（開放×格差拡大）を最も強く支持する観察。MCP全主要プレイヤー対応が継続し、エコシステム標準が事実上確定している。ただし確率変更を正当化するほどの質的変化ではなく、現状の確率分布を補強するに留まる [Arbiter v3.52](../state/arbiter-2026-04-17.md)。

### AIが初めて人間を超えた——ただし単一ベンチマークで

GPT-5.4 ProがARC-AGI-2で83.3%を出し、人間のベースライン（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。o3モデルも87.5%を記録し、90%閾値まで2.5ポイントに迫っている。

ベンチマーク首位は測定する対象によって変わる。GPQA DiamondではGemini 3.1 Proが94.3%で首位。SWE-bench VerifiedではClaude Opus 4.7がCursorBench 70%で首位。Gemma 4はArena Elo 1452でオープンモデルとして最高水準 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。単一ベンチマークへの過度な依存は判断を歪める。

### 自律型エージェントが長時間稼働の壁を突破した

GPT-5.3-Codexが25時間連続稼働で約30K行コードを生成。METRの時間地平線ベンチマークで約7ヶ月の倍増期間を確認 [INFO-006](../Information/2026-04-17/collected-raw.md#INFO-006)。このペースが続けば、2026年末には1-2週間の自律稼働が可能になる。Cursorは「OpenAIモデルは長時間自律作業で明確に優秀」と評価。

これはエージェントの本番信頼性が転換点に達したことを示唆する ([IND-026](../config/indicators.json)、elevated rising)。ただし単一事例であり、他のエージェント（Claude Code・Gemini CLI）での再現性検証が必須 [Arbiter v3.52](../state/arbiter-2026-04-17.md)。

### 企業の導入は爆発的——成果は二極化

エンタープライズAI利用はYoY 8倍、推論モデル利用は300倍に成長。80%のFortune 500がAIエージェントを展開している。

だが実態は「成功組」と「失敗組」に二極化している。

**成功組**: 92%の企業が正のROI達成、平均2.8x（IDC調査）。49%の職業でタスクの25%以上がClaudeで実行。

**失敗組**: Gartnerは40%超のエージェントAIプロジェクトが2027年末までにキャンセルされると予測。PwC調査では56%が「売上増にも費用削減にもなっていない」。MIT: 95%のgenAIパイロットが失敗。88%のAIエージェントプロジェクトが本番前に失敗 [INFO-064](../Information/2026-04-10/collected-raw.md#INFO-064)。

### 資金が3社に集中し、K字型市場が形成されている

**Q1 2026北米AI投資が$221Bに到達**——前年同期比6倍 [INFO-047](../Information/2026-04-10/collected-raw.md#INFO-047)。全ステージ（Seed〜Late Stage）で急増。

OpenAI $122B、Anthropic $30B、xAI $20B、Meta CoreWeave $21B——上位4社だけで$190B超が集中。[IND-003](../config/indicators.json)はhigh維持。

### 価格は年10倍のペースで下がり続けている

GPT-4相当が3年前$60/Mだったのが今$0.75/M。98%の下落。GPT-5.4 nanoは$0.20/$1.25。ByteDance Seed 2.0 Pro $0.47/M。Gemini 3.1 Proは$2/$12で2Mコンテキスト。

**DeepSeek V3.2がGPT-5レベル性能を$0.014/Mで提供**——GPT-4 Turboの700分の1 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。

### 囲い込みが定量化された

**スイッチングコストが年間AI支出の15-20%**（$2M/年なら$300K-$400K）。Azure AI価格15-22%値上げ、GCP "premium inference"3倍価格 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。

**74%の企業がAIベンダー喪失時に業務混乱を予想** [INFO-097](../Information/2026-04-10/collected-raw.md#INFO-097)。

### エコシステム標準化が臨界質量を突破した

AAIFが**170+メンバー**に到達 [INFO-021](../Information/2026-04-10/collected-raw.md#INFO-021)。MCP SDKは月間9700万ダウンロード。**全主要AIプレイヤーがMCPに対応**——OpenAI Agents SDK、Anthropic Agent SDK（per-tool permission）、xAI Voice Agent API、Google Gemini API Docs MCP。([IND-027](../config/indicators.json)、high) [Arbiter v3.52](../state/arbiter-2026-04-17.md)。

### セキュリティが最大の企業懸念に浮上

AI securityがクラウドを抜いて企業の最優先課題になった（ETR調査）。

Codex desktop control（マウス・キーボード制御）が新たな攻撃表面を生んだ。OpenAIは**Cyber Verification Program**を新設、AnthropicはMythos限定ロールアウトで対応——開発企業自身がリスクを認識している [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。([IND-013](../config/indicators.json)、high rising)

### 政府の選別的介入が構造化した

SCR連邦控訴裁敗訴でAnthropic排除が確定。DOD「全合法目的での無制限アクセス」要求 → Anthropic拒否 → SCR指定 → 控訴裁差し止め棄却 → OpenAI $200M契約。

ペンタゴンは全主要AI企業に倫理ガードレール緩和を圧力 [INFO-080](../Information/2026-04-10/collected-raw.md#INFO-080)。

## 寡占と分散のどちらに向かうか

市場には2つの正反対の力が同時に働いている。

**集中に向かう力:** 資金$190B超が上位4社に集中。エンタープライズ3社で88%シェア。各社のSDK/スキル形式は非互換。政府が特定企業を選別。M&Aによる垂直統合。スイッチングコスト15-20%。74%の企業がベンダー依存不安。

**分散に向かう力:** AAIF標準化（170+メンバー）。Gemma 4オープンモデル（Apache 2.0）。ByteDanceの価格破壊。DeepSeek V3.2がGPT-5レベル性能を700分の1コストで提供。193カ国グローバルAIアコード。全主要プレイヤーのMCP対応。

現時点では「技術は開くが、性能トップは集中する」（SCN-002、37%）が最有力。だが「静かな囲い込み」（SCN-003、27%）が定量証拠を得て迫っている。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | 前世代比30%超の性能向上 | o3 ARC-AGI 87.5%。Gemma 4 Arena Elo 1452 | **high approaching** |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | 上位4社$190B超。Q1 AI投資$221B | **high** |
| [IND-004](../config/indicators.json) OSS性能到達 | OSSが商用モデルの90%性能に達するか | Gemma 4 Arena Elo 1452。Veracity AI「性能ギャップは閉じた」 | elevated approaching |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | 実行環境・オーケストレーション競争 | 72時間4社同時リリース。Codex desktop control。Opus 4.7 GA | elevated rising |
| [IND-008](../config/indicators.json) 大企業の集中 | Fortune 500のAI導入先が2-3社に集中するか | Anthropic 40%、OpenAI 27%、Google 21%（合計88%） | elevated |
| [IND-013](../config/indicators.json) AI安全性事故 | 大規模なAI関連事故 | Codex desktop control新攻撃表面。Cyber Verification Program対抗投資 | **high** rising |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理にシフト | 82%採用率。Codex 111 plugins。Opus 4.7 CursorBench 70% | **high** rising |
| [IND-023](../config/indicators.json) 政府のAI強制力 | 経済的手段でAI安全姿勢を抑圧 | SCR連邦控訴裁敗訴で確定。全社ガードレール緩和圧力 | **high** rising |
| [IND-026](../config/indicators.json) エージェント本番環境到達率 | エージェントの本番稼働成功率 | Codex 25hr連続稼働・heartbeats信頼性転換点 | elevated rising |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | MCP/A2A等のオープンスタンダード採用率 | AAIF 170+メンバー。全主要プレイヤーMCP対応 | **high** rising |
| [IND-028](../config/indicators.json) AGI自己改善速度 | 再帰的自己改善の進展 | METR約7ヶ月倍増期間。ARC-AGI-3依然0%。主観-客観乖離過去最大 | elevated rising |
| [IND-029](../config/indicators.json) AIインフラ投資規模 | 計算能力投資の集中と規模 | OpenClaw GPU H200価格25-30%上昇。インフラ需要加速 | elevated rising |
| [IND-030](../config/indicators.json) AI能力とリスクの二面性 | 高性能モデルが「最も整合性高い」同時に「最もリスク高い」 | Codex 25hr自律稼働。Cyber Verification Program。能力向上とリスク管理の同時進行 | elevated rising |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-17 | 鮮度タイムアウト対応（7日経過）。72時間4社同時エージェントインフラリリース・Codex自律型開発プラットフォーム進化・Opus 4.7 GA・GPT-5.3-Codex 25hr連続稼働・Voice Agent APIを反映。SCN-002 36→37%・SCN-003 28→27%に更新。IND-026/027/028/029/030を最新値に更新 |
| 2026-04-10 | Anthropic $30B ARR自己発表・SCR連邦控訴裁敗訴確定・Managed Agents GA・Google/Broadcom TPU契約を反映。Meta台頭を追加。SCN-002 36%・SCN-003 28%に更新。スイッチングコスト定量データ・Q1 AI投資$221B・AAIF 170+メンバーを追加 |
| 2026-04-08 | シナリオ順位の入れ替わりを反映（SCN-003 2位上昇、SCN-001 3位後退）。MCP二面性、Mythos Preview、AI Agent Drift問題を追加 |
| 2026-04-06 | Gemma 4、Gemini 3.1 Flash-Lite/Flash Live、Doubao日次トークン120兆、Coze MCP対応を追加 |
| 2026-03-29 | OpenAI $120B調達、Sora終了を反映 |
