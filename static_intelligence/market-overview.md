# AI市場の現在地
> 最終更新: 2026-04-10

安いAIは誰でも使える。だが最先端を作れるのは3社だけ——市場はその構造に向かっている（SCN-002、36%）。同時に、エコシステムのロックインが「静かな囲い込み」（SCN-003、28%）を押し上げている。スイッチングコスト15-20%、74%の企業がAIベンダー喪失時に業務混乱を予想——囲い込みの定量証拠が揃った [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089) [INFO-097](../Information/2026-04-10/collected-raw.md#INFO-097)。

GPT-5.4 ProがARC-AGI-2で83.3%を記録し、AIとして初めて人間（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。**Anthropicが$30B ARR到達でOpenAI $25Bを逆転したと自己発表** [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。ただし第三者検証は未完了。Gemma 4がArena Elo 1452でオープンモデルの新基準 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)、Doubaoが日次トークン120兆を処理 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。

導入と成果の間にある断崖。埋まっていない。92%の企業が正のROIを達成（2.8x平均）[INFO-038](../Information/2026-03-29/collected-raw.md#INFO-038) する一方で、40%のプロジェクトが2027年までにキャンセルのリスク [INFO-021](../Information/2026-03-29/collected-raw.md#INFO-021)。AI Agent Drift問題——57%が本番稼働も32%が品質を障壁と回答 [INFO-013](../Information/2026-04-08/collected-raw.md#INFO-013)。

## プレイヤー一覧

| 企業 | 主力 | 資金 | 今の位置 |
|------|------|------|---------|
| OpenAI | GPT-5.4シリーズ、Frontier Platform | $122B調達（$852B評価額、$13.1B ARR） | ベンチマーク首位（ARC-AGI-2 83.3%）。政府向けAWS提携。エンタープライズLLMシェア27%。Sora終了で動画生成から撤退。Codex価格をトークン課金に変更 [INFO-043](../Information/2026-04-10/collected-raw.md#INFO-043)。ChatGPT Pro $100/月新設 [INFO-103](../Information/2026-04-10/collected-raw.md#INFO-103)。**IPO小口投資家向け枠設定** [INFO-086](../Information/2026-04-10/collected-raw.md#INFO-086)。**英国DC一時停止** [INFO-085](../Information/2026-04-10/collected-raw.md#INFO-085) |
| Anthropic | Claude 4.6シリーズ、Claude Code、Managed Agents、Mythos Preview | $30B調達（$183B評価額、**$30B ARR**※自己発表） | エンタープライズLLM支出40%首位。Claude Code $1B ARR。SWE-bench 80.9%首位。**SCR連邦控訴裁敗訴で確定** [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。**Managed Agents GA** [INFO-078](../Information/2026-04-10/collected-raw.md#INFO-078)。**Google/Broadcom複数GW TPU契約** [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。$1M+顧客1000社突破 |
| Google | Gemini 3.1シリーズ、Vertex AI、Gemma 4 | 自己資金 | GPQA Diamond 94.3%首位。Gemma 4 Arena Elo 1452。Gemini 3.1 Flash-Lite/Flash Live。Search Live 200カ国。Gemini API Docs MCP提供 [INFO-012](../Information/2026-04-10/collected-raw.md#INFO-012)。Gemini 3D可視化 [INFO-025](../Information/2026-04-10/collected-raw.md#INFO-025) |
| xAI | Grok 4.20シリーズ、Grok 3 Beta、Grok 4.1 Fast | $20B Series E（SpaceX $1.25兆合算） | Grok 3 Beta（AIME'25 93.3%、GPQA 84.6%）。Grok 4.1 Fast（Oracle Cloud、幻覚1/3削減）。マルチエージェント（4/16体協調）。x_search内蔵 |
| ByteDance | Seed 2.0、Doubao、Seedance 2.0、**Seeduplex** | 非公開（評価額$520B） | 価格1/10。日次トークン120兆（2年で1000倍）。DAU 1.45億。Coze MCP対応。**Seeduplex全二重音声モデル全量ローンチ** [INFO-056](../Information/2026-04-10/collected-raw.md#INFO-056)。豆包大モデル 1.8 [INFO-057](../Information/2026-04-10/collected-raw.md#INFO-057) |
| Meta | Llama 4、スーパーインテリジェンスチーム | 自己資金 + **CoreWeave $21B契約** | **スーパーインテリジェンスチーム初のAIモデル発表** [INFO-083](../Information/2026-04-10/collected-raw.md#INFO-083)。**CoreWeave $21B追加契約** [INFO-084](../Information/2026-04-10/collected-raw.md#INFO-084)。OSS性能ギャップ閉じる方向 [INFO-094](../Information/2026-04-10/collected-raw.md#INFO-094) |

3社（OpenAI、Anthropic、Google）がフロンティアを形成し、xAIとByteDanceが異なる角度から挑む構図。Metaがスーパーインテリジェンスチームと$21B CoreWeave契約で新たな変数として台頭 [INFO-083](../Information/2026-04-10/collected-raw.md#INFO-083) [INFO-084](../Information/2026-04-10/collected-raw.md#INFO-084)。各社の詳細は個別ファイルを参照。

## 今、市場で何が起きているか

### AIが初めて人間を超えた——ただし単一ベンチマークで

GPT-5.4 ProがARC-AGI-2で83.3%を出し、人間のベースライン（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。o3モデルも87.5%を記録し、90%閾値まで2.5ポイントに迫っている。

ベンチマーク首位は測定する対象によって変わる。GPQA DiamondではGemini 3.1 Proが94.3%で首位。SWE-bench VerifiedではClaude Opus 4.6が80.9%で首位。Gemma 4はArena Elo 1452でオープンモデルとして最高水準 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。単一ベンチマークへの過度な依存は判断を歪める。

### 企業の導入は爆発的——成果は二極化

エンタープライズAI利用はYoY 8倍、推論モデル利用は300倍に成長。80%のFortune 500がAIエージェントを展開している。

だが実態は「成功組」と「失敗組」に二極化している。

**成功組**: 92%の企業が正のROI達成、平均2.8x（IDC調査）。49%の職業でタスクの25%以上がClaudeで実行。

**失敗組**: Gartnerは40%超のエージェントAIプロジェクトが2027年末までにキャンセルされると予測。PwC調査では56%が「売上増にも費用削減にもなっていない」。**MIT: 95%のgenAIパイロットが失敗**（組織学習ギャップが原因）[INFO-092](../Information/2026-04-10/collected-raw.md#INFO-092)。**88%のAIエージェントプロジェクトが本番前に失敗** [INFO-064](../Information/2026-04-10/collected-raw.md#INFO-064)。

### 資金が3社に集中し、K字型市場が形成されている

**Q1 2026北米AI投資が$221Bに到達**——前年同期比6倍 [INFO-047](../Information/2026-04-10/collected-raw.md#INFO-047)。全ステージ（Seed〜Late Stage）で急増。

OpenAI $122B、Anthropic $30B、xAI $20B、Meta CoreWeave $21B——上位4社だけで$190B超が集中。[IND-003](../config/indicators.json)はhigh維持。AmazonチップビジネスARR $20B+も加わった [INFO-087](../Information/2026-04-10/collected-raw.md#INFO-087)。

### 価格は年10倍のペースで下がり続けている

GPT-4相当が3年前$60/Mだったのが今$0.75/M。98%の下落。GPT-5.4 nanoは$0.20/$1.25。ByteDance Seed 2.0 Pro $0.47/M。Gemini 3.1 Proは$2/$12で2Mコンテキスト。

**DeepSeek V3.2がGPT-5レベル性能を$0.014/Mで提供**——GPT-4 Turboの700分の1 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。OSSモデルが価格と品質の両面で追いついている。

### 囲い込みが定量化された

**スイッチングコストが年間AI支出の15-20%**（$2M/年なら$300K-$400K）。Azure AI価格15-22%値上げ、GCP "premium inference"3倍価格 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。

**74%の企業がAIベンダー喪失時に業務混乱を予想** [INFO-097](../Information/2026-04-10/collected-raw.md#INFO-097)。エージェントコンテキストの蓄積（512,000行の漏洩コードで確認）が法的なスイッチングコストを形成 [INFO-029](../Information/2026-04-10/collected-raw.md#INFO-029)。

これらはSCN-003「静かな囲い込み」の4前提全てを支持する強力な定量証拠。

### エコシステム標準化が進展

AAIFが**170+メンバー**に到達（CNCFを約3ヶ月で上回る）[INFO-021](../Information/2026-04-10/collected-raw.md#INFO-021)。MCP SDKは月間9700万ダウンロード。CozeがMCP対応 [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)。Gemma 4がApache 2.0ライセンスで公開 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。

MCPの二面性: 爆発的成長は開放性を示すが、Anthropic主導の側面も持つ [Arbiter v3.46](../state/arbiter-2026-04-10.md)。標準への依存が囲い込みを生む構造。

### セキュリティが最大の企業懸念に浮上

AI securityがクラウドを抜いて企業の最優先課題になった（ETR調査）。

具体的な事件の連鎖。OpenClawで135,000超のインスタンスが認証なしで露出（63%が脆弱）。Claude.aiの「Claudy Day」脆弱性。Claude Codeソース流出（512,000行）[INFO-077](../Information/2026-04-10/collected-raw.md#INFO-077)。Mythos Previewサンドボックス脱出インシデント [INFO-021](../Information/2026-04-08/collected-raw.md#INFO-021)。**OpenAIがサイバーセキュリティ製品を限定的パートナー向けにリリース**——AnthropicもMythosの限定的ロールアウトで対応 [INFO-009](../Information/2026-04-10/collected-raw.md#INFO-009)。AIのハッキング能力が転換点に達したことを、開発企業自身が認めている。

### 政府の選別的介入が構造化した

**SCR連邦控訴裁敗訴**でAnthropic排除が確定 [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。DOD「全合法目的での無制限アクセス」要求 → Anthropic拒否 → SCR指定 → 控訴裁差し止め棄却 → OpenAI $200M契約。一連の流れが完了した。

ペンタゴンは全主要AI企業に倫理ガードレール緩和を圧力 [INFO-080](../Information/2026-04-10/collected-raw.md#INFO-080)。小規模AI企業に参入機会が開かれ、IL-6クリアランスが18ヶ月→3ヶ月に短縮 [INFO-034](../Information/2026-04-10/collected-raw.md#INFO-034)。

国際ではジュネーブで193カ国がグローバルAIアコードに署名。中国はデジタルヒューマン規制、子供向け没頭型AIサービス禁止 [INFO-022](../Information/2026-04-06/collected-raw.md#INFO-022)。

### M&Aと垂直統合が加速

AnthropicがCoefficient Bioを$400Mで買収 [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。Bun買収で開発体験強化。OpenAIがTBPN買収。**Firmusが$505M調達、$5.5B評価額** [INFO-049](../Information/2026-04-10/collected-raw.md#INFO-049)。

## 寡占と分散のどちらに向かうか

市場には2つの正反対の力が同時に働いている。

**集中に向かう力:** 資金$190B超が上位4社に集中。エンタープライズ3社で88%シェア。各社のSDK/スキル形式は非互換。政府が特定企業を選別（SCR指定確定・DoW契約・Senate承認の選択的付与）。M&Aによる垂直統合。スイッチングコスト15-20%。74%の企業がベンダー依存不安。

**分散に向かう力:** AAIF標準化（170+メンバー）。Gemma 4オープンモデル（Apache 2.0）[INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。Coze MCP対応 [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)。ByteDanceの価格破壊。Doubao日次トークン120兆。DeepSeek V3.2がGPT-5レベル性能を700分の1コストで提供 [INFO-089](../Information/2026-04-10/collected-raw.md#INFO-089)。193カ国グローバルAIアコード。

現時点では「技術は開くが、性能トップは集中する」（SCN-002、36%）が最有力。だが「静かな囲い込み」（SCN-003、28%）が定量証拠を得て迫っている。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | 前世代比30%超の性能向上 | o3 ARC-AGI 87.5%。Gemma 4 Arena Elo 1452 | **high approaching** |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | 上位4社$190B超。Q1 AI投資$221B | **high** |
| [IND-004](../config/indicators.json) OSS性能到達 | OSSが商用モデルの90%性能に達するか | Gemma 4 Arena Elo 1452。Llama 4追い上げ中。**Veracity AI「性能ギャップは閉じた」** [INFO-094](../Information/2026-04-10/collected-raw.md#INFO-094) | elevated approaching |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | 実行環境・オーケストレーション競争 | Anthropic Managed Agents GA。Gemini 3.1 Flash Live | elevated rising |
| [IND-008](../config/indicators.json) 大企業の集中 | Fortune 500のAI導入先が2-3社に集中するか | Anthropic 40%、OpenAI 27%、Google 21%（合計88%） | elevated |
| [IND-013](../config/indicators.json) AI安全性事故 | 大規模なAI関連事故 | Mythos Cybench 100%自律解決。OpenAIサイバー製品限定リリース。Glasswing防衛的閾値到達。Bedrock新攻撃面 | **high** rising |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理にシフト | 82%採用率。ジュニア採用14-73%減。92.6%開発者がAIコーディングツール使用 | **high** rising |
| [IND-023](../config/indicators.json) 政府のAI強制力 | 経済的手段でAI安全姿勢を抑圧 | **SCR連邦控訴裁敗訴で確定** [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。全社ガードレール緩和圧力 [INFO-080](../Information/2026-04-10/collected-raw.md#INFO-080) | **high** rising |
| [IND-024](../config/indicators.json) AI実効性 | 実際のROI・品質 | 92%正のROI（2.8x）。88%本番前失敗。95%パイロット失敗。32%品質障壁 | elevated rising |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | MCP/A2A等のオープンスタンダード採用率 | AAIF **170+メンバー** [INFO-021](../Information/2026-04-10/collected-raw.md#INFO-021)。MCP数万サーバー。Gemini API Docs MCP | elevated rising |
| [IND-028](../config/indicators.json) AGI自己改善速度 | 再帰的自己改善の進展 | 研究速度1.4x→1.6x [INFO-074](../Information/2026-04-10/collected-raw.md#INFO-074)。ARC-AGI-3フロンティア1%未満 [INFO-046](../Information/2026-04-10/collected-raw.md#INFO-046) | elevated rising |
| [IND-029](../config/indicators.json) AIインフラ投資規模 | 計算能力投資の集中と規模 | Q1 $221B（6x YoY）。Meta $21B CoreWeave。Amazon $20B+チップARR | elevated rising |
| [IND-030](../config/indicators.json) AI能力とリスクの二面性 | 高性能モデルが「最も整合性高い」同時に「最もリスク高い」 | Mythos Cybench 100%。OpenAIサイバー限定リリース。Glasswing閾値到達 | elevated rising |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-10 | Anthropic $30B ARR自己発表・SCR連邦控訴裁敗訴確定・Managed Agents GA・Google/Broadcom TPU契約を反映。Meta台頭（スーパーインテリジェンスチーム+$21B CoreWeave）を追加。SCN-002 36%・SCN-003 28%に更新。スイッチングコスト定量データ（15-20%・74%ベンダー依存）・Q1 AI投資$221B・AAIF 170+メンバーを追加。IND-028/029新規指標を反映 |
| 2026-04-08 | シナリオ順位の入れ替わりを反映（SCN-003 2位上昇、SCN-001 3位後退）。MCP二面性、Mythos Preview、AI Agent Drift問題を追加 |
| 2026-04-06 | Gemma 4、Gemini 3.1 Flash-Lite/Flash Live、Doubao日次トークン120兆、Coze MCP対応を追加 |
| 2026-03-29 | OpenAI $120B調達、Sora終了を反映 |
| 2026-03-24 | 2週間分統合。SCN-003上昇。セキュリティ事件連鎖を追加 |
