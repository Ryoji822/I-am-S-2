# AI市場の現在地

> 最終更新: 2026-04-06

安いAIは誰でも使える。だが最先端を作れるのは3社だけ——市場はその構造に向かっている（SCN-002、37%）。同時に、エコシステムのロックインと政府の選別的介入が「静かな囲い込み」（SCN-003、25%）を押し上げている。

GPT-5.4 ProがARC-AGI-2で83.3%を記録し、AIとして初めて人間（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。フロンティア性能の格差拡大は事実になった。**Gemma 4がArena Elo 1452でオープンモデルの新基準を打ち立て** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)、**Doubaoが日次トークン120兆（2年で1000倍）を処理** [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。価格と性能の両面で市場が動いている。

導入と成果の間にある断崖は埋まっていない。92%の企業が正のROIを達成（2.8x平均）[INFO-038](../Information/2026-03-29/collected-raw.md#INFO-038) する一方で、40%のプロジェクトが2027年までにキャンセルのリスク [INFO-021](../Information/2026-03-29/collected-raw.md#INFO-021)。成功組と失敗組の二極化が鮮明になっている。

## プレイヤー一覧

| 企業 | 主力 | 資金 | 今の位置 |
|------|------|------|---------|
| OpenAI | GPT-5.4シリーズ、Frontier Platform | $120B調達（$730B評価額、$13.1B ARR） | ベンチマーク首位（ARC-AGI-2 83.3%）。政府向けAWS提携。エンタープライズLLMシェア27%。Sora終了で動画生成から撤退。Codex価格をトークン課金に変更 [INFO-009](../Information/2026-04-06/collected-raw.md#INFO-009) |
| Anthropic | Claude 4.6シリーズ、Claude Code | $30B調達（$183B評価額、$5B ARR） | エンタープライズLLM支出40%首位。Claude Code愛用率46%。SWE-bench 80.9%首位。**Coefficient Bio $400M買収** [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。シドニーオフィス開設 [INFO-001](../Information/2026-04-06/collected-raw.md)。Pentagonサプライチェーンリスク指定・連邦判事一時差止 [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008) |
| Google | Gemini 3.1シリーズ、Vertex AI、Gemma 4 | 自己資金 | GPQA Diamond 94.3%首位。**Gemma 4 Arena Elo 1452** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。**Gemini 3.1 Flash-Lite/Flash Live** [INFO-005](../Information/2026-04-06/collected-raw.md#INFO-005)。Search Live 200カ国。Gemini API Flex/Priorityティア [INFO-010](../Information/2026-04-06/collected-raw.md#INFO-010)。Project Maven再参入 |
| xAI | Grok 4.20シリーズ | $20B Series E（SpaceX $1.25兆合算） | マルチエージェント（4/16体協調、2Mコンテキスト）。x_search内蔵。DoD契約確保済み |
| ByteDance | Seed 2.0、Doubao、Seedance 2.0 | 非公開（評価額$520B） | 価格1/10。**Doubao日次トークン120兆（2年で1000倍）、DAU 1.45億** [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。**Coze MCP対応** [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)。Seedance 2.0 API公開テスト中 |

3社（OpenAI、Anthropic、Google）がフロンティアを形成し、xAIとByteDanceが異なる角度から挑む構図。各社の詳細は個別ファイルを参照。

## 今、市場で何が起きているか

### AIが初めて人間を超えた——ただし単一ベンチマークで

GPT-5.4 ProがARC-AGI-2で83.3%を出し、人間のベースライン（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。o3モデルも87.5%を記録し、90%閾値まで2.5ポイントに迫っている。

ベンチマーク首位は測定する対象によって変わる。GPQA DiamondではGemini 3.1 Proが94.3%で首位。SWE-bench VerifiedではClaude Opus 4.6が80.9%で首位。**Gemma 4はArena Elo 1452でオープンモデルとして最高水準** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。単一ベンチマークへの過度な依存は判断を歪める。

### 企業の導入は爆発的——成果は二極化

エンタープライズAI利用はYoY 8倍、推論モデル利用は300倍に成長。80%のFortune 500がAIエージェントを展開している。

だが実態は「成功組」と「失敗組」に二極化している。

**成功組**: 92%の企業が正のROI達成、平均2.8x（IDC調査）。49%の職業でタスクの25%以上がClaudeで実行。

**失敗組**: Gartnerは40%超のエージェントAIプロジェクトが2027年末までにキャンセルされると予測。PwC調査では56%が「売上増にも費用削減にもなっていない」。

### 資金が3社に集中し、K字型市場が形成されている

2025年AI関連スタートアップはCarta上の$128Bの41%を占めた。Q4 2025にはAI/MLがグローバルVC deal valueの52%に達し、初めて過半数を超えた。

OpenAI $120B、Anthropic $30B、xAI $20B——上位3社だけで$170B超が集中。[IND-003](../config/indicators.json)はhigh維持。

### 価格は年10倍のペースで下がり続けている

GPT-4相当が3年前$60/Mだったのが今$0.75/M。98%の下落。GPT-5.4 nanoは$0.20/$1.25、GPT-5.4 miniは$0.75/$4.50。ByteDance Seed 2.0 Pro $0.47/M。Gemini 3.1 Proは$2/$12で2Mコンテキスト。

**Gemini APIに新価格ティア**: Flex（Standard APIの50%価格、レイテンシ増加許容）、Priority（高信頼性・低レイテンシ）[INFO-010](../Information/2026-04-06/collected-raw.md#INFO-010)。**Codexもトークン課金に移行** [INFO-009](../Information/2026-04-06/collected-raw.md#INFO-009)。価格体系が複雑化しつつ、全体としての下落トレンドは継続。

### 使用量が爆発的成長

**ByteDance Doubao**: 日次トークン使用量120兆超（2年で1000倍）。DAU 1.45億で中国国内AIアプリ首位 [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。価格破壊が実際の使用量増加に直結している証拠。

### エコシステム標準化が進展

**CozeがMCPプロトコル対応**——企查查等と標準MCPで接続 [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)。**Gemma 4がApache 2.0ライセンスで公開**——オープンモデルの標準化が加速 [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。AAIF（Linux Foundation傘下）は146メンバーに成長。MCP SDKは月間9700万ダウンロード。

### セキュリティが最大の企業懸念に浮上

AI securityがクラウドを抜いて企業の最優先課題になった（ETR調査）。

理由は具体的な事件の連鎖にある。OpenClawで135,000超のインスタンスが認証なしで露出（63%が脆弱）。Claude.aiの「Claudy Day」脆弱性。**Claude Codeソース流出（512,000行）** [INFO-007](../Information/2026-04-06/collected-raw.md#INFO-007)。

### 規制は米国と世界で正反対に動いている

**米国**: PentagonがAnthropicを「サプライチェーンリスク」指定。**連邦判事が一時差止命令を発行** [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008)。White Houseが「ライトタッチ」規制フレームワークを発表。

**国際**: ジュネーブで193カ国がグローバルAIアコードに署名。AGIレベルAIのハードウェアキルスイッチ義務化、自律型致死兵器の禁止。

**中国**: デジタルヒューマン規制、子供向け没頭型AIサービス禁止 [INFO-022](../Information/2026-04-06/collected-raw.md#INFO-022)。AI生成コンテンツのラベリング義務（4月1日発効）。

### M&Aで垂直統合が加速

**AnthropicがCoefficient Bioを$400Mで買収**——ライフサイエンス領域の垂直統合 [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。Claude for Financial Services、Claude for Life Sciencesと続く業界別ソリューション展開が、買収で加速する。

## 寡占と分散のどちらに向かうか

市場には2つの正反対の力が同時に働いている。

**集中に向かう力:** 資金$170B超が上位3社に集中。エンタープライズ3社で88%シェア。各社のSDK/スキル形式は非互換。政府が特定企業を選別（SCR指定・サプライチェーンリスク指定・DoW契約・Senate承認の選択的付与）。M&Aによる垂直統合（Coefficient Bio買収）。

**分散に向かう力:** AAIF標準化（146メンバー）。**Gemma 4オープンモデル（Apache 2.0）** [INFO-006](../Information/2026-04-06/collected-raw.md#INFO-006)。**Coze MCP対応** [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)。ByteDanceの価格破壊。**Doubao日次トークン120兆** [INFO-024](../Information/2026-04-06/collected-raw.md#INFO-024)。193カ国グローバルAIアコード。EU規制によるデータ主権。

現時点では「技術は開くが、性能トップは集中する」（SCN-002、37%）が最有力。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | 前世代比30%超の性能向上 | o3 ARC-AGI 87.5%。Gemma 4 Arena Elo 1452 | **high approaching** |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | 上位3社$170B超。K字型市場が形成 | **high** |
| [IND-004](../config/indicators.json) OSS性能到達 | OSSが商用モデルの90%性能に達するか | **Gemma 4 Arena Elo 1452**。Llama 4追い上げ中 | elevated approaching |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | 実行環境・オーケストレーション競争 | Gemini 3.1 Flash Live、Gemma 4 Agent Skills | elevated rising |
| [IND-008](../config/indicators.json) 大企業の集中 | Fortune 500のAI導入先が2-3社に集中するか | Anthropic 40%、OpenAI 27%、Google 21%（合計88%） | elevated |
| [IND-013](../config/indicators.json) AI安全性事故 | 大規模なAI関連事故 | OpenClaw 135K暴露、Claudy Day、Claude Codeソース流出 | elevated rising |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理にシフト | 82%採用率。ジュニア採用14-73%減 | **high** rising |
| [IND-023](../config/indicators.json) 政府のAI強制力 | 経済的手段でAI安全姿勢を抑圧 | Pentagonサプライチェーンリスク指定。**連邦判事一時差止** [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008) | **high** rising |
| [IND-024](../config/indicators.json) AI実効性 | 実際のROI・品質 | 92%正のROI（2.8x）。40%キャンセルリスク | elevated rising |
| [IND-027](../config/indicators.json) エコシステム標準化進展度 | MCP/A2A等のオープンスタンダード採用率 | **Coze MCP対応** [INFO-025](../Information/2026-04-06/collected-raw.md#INFO-025)。AAIF 146メンバー | elevated rising |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-06 | Gemma 4（Arena Elo 1452）、Gemini 3.1 Flash-Lite/Flash Live、Gemini API Flex/Priorityティア、Codexトークン課金、Doubao日次トークン120兆、Coze MCP対応、Anthropic Coefficient Bio $400M買収、Pentagonサプライチェーンリスク指定・連邦判事一時差止、中国規制（子供向け没頭型AI禁止・デジタルヒューマン規制）、Claude Codeソース流出を追加。IND-027新規指標を反映 |
| 2026-03-29 | OpenAI $120B調達、Sora終了を反映。AI ROI二極化を追加。7社SDK同時更新を記録 |
| 2026-03-24 | 2週間分統合。SCN-003上昇。セキュリティ事件連鎖を追加 |
| 2026-03-09 | GPT-5.4 Pro人間超え（ARC-AGI-2 83.3%）を反映 |
| 2026-03-01 | IND-023 high昇格と政府介入の質的変化を追記 |
| 2026-02-23 | 初版作成（AAIF設立後の市場構造再定義） |
