# AI市場の現在地

> 最終更新: 2026-03-29

安いAIは誰でも使える。だが最先端を作れるのは3社だけ——市場はその構造に向かっている（SCN-002、39%）。同時に、エコシステムのロックインと政府の選別的介入が「静かな囲い込み」（SCN-003、22%）を押し上げている。

GPT-5.4 ProがARC-AGI-2で83.3%を記録し、AIとして初めて人間（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。フロンティア性能の格差拡大は事実になった。一方で、導入と成果の間にある断崖は埋まっていない。92%の企業が正のROIを達成（2.8x平均）[INFO-038](../Information/2026-03-29/collected-raw.md#INFO-038) する一方で、40%のプロジェクトが2027年までにキャンセルのリスク [INFO-021](../Information/2026-03-29/collected-raw.md#INFO-021)。成功組と失敗組の二極化が鮮明になっている。

**安全性をめぐる分断が深まっている。** 2026年2月27日、Trump政権がAnthropicをSCR指定し連邦使用を禁止。3月21日にはPentagonが$200M契約を正式終了し、同日Googleは2018年のProject Maven撤退を覆して再参入した [INFO-044](../Information/2026-03-21/collected-raw.md#INFO-044)。一方で193カ国がジュネーブでグローバルAIアコードに署名し、自律型致死兵器の禁止やAGIキルスイッチの義務化で合意。米国の「安全性を妥協した企業が利益を得る」構造と、国際社会の「安全性を規範にする」動きが正面衝突している。

## プレイヤー一覧

| 企業 | 主力 | 資金 | 今の位置 |
|------|------|------|---------|
| OpenAI | GPT-5.4シリーズ、Frontier Platform | $120B調達（$730B評価額、$13.1B ARR） | ベンチマーク首位（ARC-AGI-2 83.3%）。政府向けAWS提携で機密業務にも拡大。だがエンタープライズLLMシェアは27%でAnthropicに負けている。Sora終了で動画生成市場から撤退 [INFO-005](../Information/2026-03-29/collected-raw.md#INFO-005) |
| Anthropic | Claude 4.6シリーズ、Claude Code | $30B調達（$380B評価額、$14B ARR） | エンタープライズLLM支出40%で首位。Claude Code愛用率46%。SWE-bench Verified 80.9%で首位 [INFO-013](../Information/2026-03-08/collected-raw.md#INFO-013)。だがPentagon契約$200M正式終了、Senate承認からも除外 |
| Google | Gemini 3.1シリーズ、Vertex AI | 自己資金 | GPQA Diamond 94.3%で首位。Gemini 3.1 Flash Live、Search Live 200カ国展開 [INFO-009](../Information/2026-03-29/collected-raw.md#INFO-009)。外部資金不要で長期戦に強い。Project Maven再参入 |
| xAI | Grok 4.20シリーズ | $20B Series E（SpaceX $1.25兆合算） | マルチエージェント（4/16体協調、2Mコンテキスト）。x_search内蔵 [INFO-007](../Information/2026-03-25/collected-raw.md#INFO-007)。DoD契約確保済み |
| ByteDance | Seed 2.0、Doubao、Seedance 2.0 | 非公開（評価額$520B） | 価格1/10で攻める。豆包MAU 2.26億でグローバル2位。ただしSeedance 2.0グローバル展開が著作権訴訟で停止 |

3社（OpenAI、Anthropic、Google）がフロンティアを形成し、xAIとByteDanceが異なる角度から挑む構図。各社の詳細は個別ファイルを参照。

## 今、市場で何が起きているか

### AIが初めて人間を超えた——ただし単一ベンチマークで

GPT-5.4 ProがARC-AGI-2で83.3%を出し、人間のベースライン（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。o3モデルも87.5%を記録し [INFO-030](../Information/2026-03-20/collected-raw.md#INFO-030)、90%閾値まで2.5ポイントに迫っている。Gemini 3.1 Proは77.1%で2位。

ベンチマーク首位は測定する対象によって変わる。GPQA DiamondではGemini 3.1 Proが94.3%で首位 [INFO-048](../Information/2026-03-22/collected-raw.md#INFO-048)。SWE-bench VerifiedではClaude Opus 4.6が80.9%で首位。ARC-AGI-2ではGPT-5.4 Proが首位。単一ベンチマークへの過度な依存は判断を歪める（[KIQ-RED-007](../config/indicators.json)として未解決）。

### 企業の導入は爆発的——成果は二極化

エンタープライズAI利用はYoY 8倍、推論モデル利用は300倍に成長 [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020)。Databricksではマルチエージェント採用が4ヶ月で327%増。80%のFortune 500がAIエージェントを展開している。

だが実態は「成功組」と「失敗組」に二極化している。

**成功組**: 92%の企業が正のROI達成、平均2.8x（IDC調査）[INFO-038](../Information/2026-03-29/collected-raw.md#INFO-038)。49%の職業でタスクの25%以上がClaudeで実行 [INFO-028](../Information/2026-03-29/collected-raw.md#INFO-028)。

**失敗組**: Gartnerは40%超のエージェントAIプロジェクトが2027年末までにキャンセルされると予測 [INFO-021](../Information/2026-03-29/collected-raw.md#INFO-021)。PwCの2026年CEO調査では56%が「売上増にも費用削減にもなっていない」[INFO-030](../Information/2026-03-23/collected-raw.md#INFO-030)。McKinseyでは23%しかスケーリングに成功していない。

この乖離は「AIをどう導入するか」で成否が分かれることを示唆している。KIQ-RED-005（AI ROI定量データ・成功要因分析）が最優先課題。

### 資金が3社に集中し、K字型市場が形成されている

2025年AI関連スタートアップはCarta上の$128Bの41%を占めた。Q4 2025にはAI/MLがグローバルVC deal valueの52%に達し、初めて過半数を超えた。

OpenAI $120B、Anthropic $30B、xAI $20B——上位3社だけで$170B超が集中。[IND-003](../config/indicators.json)はhigh維持。

### 価格は年10倍のペースで下がり続けている

GPT-4相当が3年前$60/Mだったのが今$0.75/M。98%の下落 [INFO-036](../Information/2026-02-18/collected-raw.md#INFO-036)。GPT-5.4 nanoは$0.20/$1.25、GPT-5.4 miniは$0.75/$4.50。ByteDance Seed 2.0 Pro $0.47/M。Gemini 3.1 Proは$2/$12で2Mコンテキスト。

価格下落は基本的なAIを誰の手にも届かせた。だが同時に、価格では差がつかなくなった。差別化は性能・ツール・エコシステム・安全性に移っている。

### エージェントSDK戦争が一斉に始まった

2026年3月、7社（OpenAI、Anthropic、Google、xAI、ByteDance、NVIDIA、Apple）が同時にAgent SDK/APIをアップデートした [INFO-012](../Information/2026-03-29/collected-raw.md#INFO-012) - [INFO-018](../Information/2026-03-29/collected-raw.md#INFO-018)。これはエージェント層での最大の同時競争。

- OpenAI Apps SDK（Plugin distribution、Codex統合）[INFO-013](../Information/2026-03-29/collected-raw.md#INFO-013)
- Claude Agent SDK v0.2.86（getContextUsage機能追加）[INFO-012](../Information/2026-03-29/collected-raw.md#INFO-012)
- Google Gemini API Skills（117プロンプト評価で96.6%改善）[INFO-014](../Information/2026-03-29/collected-raw.md#INFO-014)
- xAI Grok 4.20（2M context、マルチエージェント）[INFO-016](../Information/2026-03-29/collected-raw.md#INFO-016)
- ByteDance Feishu Aily（OpenClaw型エージェント）[INFO-017](../Information/2026-03-29/collected-raw.md#INFO-017)
- NVIDIA NemoClaw（オープンソース実行環境）[INFO-036](../Information/2026-03-25/collected-raw.md#INFO-036)
- Apple Siri刷新（Gemini統合契約）[INFO-032](../Information/2026-03-29/collected-raw.md#INFO-032)

AAIF（Linux Foundation傘下）は146メンバーに成長。MCP SDKは月間9700万ダウンロード。スキルレジストリは66,000超に到達。

### セキュリティが最大の企業懸念に浮上

AI securityがクラウドを抜いて企業の最優先課題になった（ETR調査）[INFO-051](../Information/2026-03-22/collected-raw.md#INFO-051)。

理由は具体的な事件の連鎖にある。OpenClawで135,000超のインスタンスが認証なしで露出（63%が脆弱）[INFO-050](../Information/2026-03-29/collected-raw.md#INFO-050)。Claude.aiの「Claudy Day」脆弱性ではURLパラメータ経由のプロンプトインジェクション→Files APIでのデータ窃取チェーンが発見された [INFO-042](../Information/2026-03-23/collected-raw.md#INFO-042)。MCP Shadow ITとして10,000超のサーバーが53%静的シークレット依存で公開されている [INFO-031](../Information/2026-03-22/collected-raw.md#INFO-031)。MetaでSev-1インシデント（AIエージェントが権限外アクセス誘発）[INFO-050](../Information/2026-03-29/collected-raw.md#INFO-050)。

### 規制は米国と世界で正反対に動いている

**米国**: White Houseが「ライトタッチ」規制フレームワークを発表。州政府のAI規制を連邦法で上書きする方針。AI開発者を第三者の悪用から免責する方向 [INFO-012](../Information/2026-03-23/collected-raw.md#INFO-012)。GSA連邦AI調達条項案は「American AI Systems」のみ許可 [INFO-015](../Information/2026-03-23/collected-raw.md#INFO-015)。EU AI法は2026年8月に完全施行 [INFO-024](../Information/2026-03-29/collected-raw.md#INFO-024)。

**国際**: ジュネーブで193カ国がグローバルAIアコードに署名。AGIレベルAIのハードウェアキルスイッチ義務化、自律型致死兵器の禁止、C2PA透かし必須化、0.5%オートメーション税、AI判断への人間介入権 [INFO-026](../Information/2026-03-23/collected-raw.md#INFO-026)。

中国は2026-2030五カ年計画でAI世界リーダーシップを最優先に。AIデータ適正性システムとAI生成コンテンツのラベリングを義務化 [INFO-057](../Information/2026-03-20/collected-raw.md#INFO-057)。

### 労働市場が変わり始めている

WEF Future of Jobs Report 2026: 2030年までに9200万の仕事が消え、1億7000万の新しい仕事が生まれる [INFO-034](../Information/2026-03-23/collected-raw.md#INFO-034)。米国でエントリーレベル求人が18ヶ月で35%減少 [INFO-049](../Information/2026-03-29/collected-raw.md#INFO-049)。22-25歳のジュニア開発者採用は14-73%減（ソースにより幅がある）[INFO-028](../Information/2026-03-20/collected-raw.md#INFO-028)。

一方でCognizantは2025年に25,000人の新卒を採用、2026年はさらに増加予定 [INFO-049](../Information/2026-03-29/collected-raw.md#INFO-049)。AIスキルを持つ新卒は即座に価値を提供可能。仕事の性質が「タスク実行」から「判断」へ変化している。

### OSSが追い上げている——だがフロンティアには届かない

Llama 4 Maverickが400Bパラメータ、1Mコンテキスト [INFO-034](../Information/2026-03-29/collected-raw.md#INFO-034)。DeepSeek V4が1Tパラメータ、1Mコンテキストで$0.14/$0.28のAPI価格で登場予定。DeerFlow 2.0がGitHub 39,000+ starsでオープンソースエージェントとして急成長 [INFO-018](../Information/2026-03-29/collected-raw.md#INFO-018)。性能差は縮まっているが、ARC-AGI-2 83.3%やGPQA 94.3%のフロンティアにはまだ届かない。

## 寡占と分散のどちらに向かうか

市場には2つの正反対の力が同時に働いている。

**集中に向かう力:** 資金$170B超が上位3社に集中。エンタープライズ3社で88%シェア。各社のSDK/スキル形式は非互換。政府が特定企業を選別（SCR指定・DoW契約・Senate承認の選択的付与）。エコシステムのスイッチングコストが上昇中。

**分散に向かう力:** AAIF標準化（146メンバー）。ByteDanceの価格破壊。OSSの性能追い上げ（DeepSeek V4、Llama 4、DeerFlow 2.0）。193カ国グローバルAIアコード。EU規制によるデータ主権。NVIDIAのNemoClaw（オープンソース実行環境）。

現時点では「技術は開くが、性能トップは集中する」（SCN-002、39%）が最有力。だが「静かな囲い込み」（SCN-003、22%）が並んでおり、政府の選別的介入とエコシステムロックインの深化がこの方向を押している。詳細は `scenario-tracker.md` を参照。

## 主要な監視指標（I&W）

| 指標 | 何を見ているか | 今の状態 | レベル |
|------|--------------|---------|--------|
| [IND-001](../config/indicators.json) 性能の非連続ジャンプ | 前世代比30%超の性能向上 | o3 ARC-AGI 87.5%。90%閾値まで2.5pt | **high approaching** |
| [IND-003](../config/indicators.json) 資金集中 | 上位3社が業界調達額の80%超を占めるか | 上位3社$170B超。K字型市場が形成 | **high** |
| [IND-004](../config/indicators.json) OSS性能到達 | OSSが商用モデルの90%性能に達するか | Llama 4、DeepSeek V4追い上げ中 | elevated approaching |
| [IND-006](../config/indicators.json) エージェントスタック上位レイヤー | 実行環境・オーケストレーション競争 | 7社同時SDK更新。NVIDIA NemoClaw登場 | elevated rising |
| [IND-008](../config/indicators.json) 大企業の集中 | Fortune 500のAI導入先が2-3社に集中するか | Anthropic 40%、OpenAI 27%、Google 21%（合計88%） | elevated |
| [IND-013](../config/indicators.json) AI安全性事故 | 大規模なAI関連事故 | OpenClaw 135K暴露、Claudy Day、MCP Shadow IT、Meta Sev-1 | elevated rising |
| [IND-015](../config/indicators.json) 実行環境の囲い込み | 実行環境がベンダー固有か標準か | 非互換SDK乱立。NVIDIA NemoClawが標準化の動き | elevated rising |
| [IND-018](../config/indicators.json) AGI兆候 | AGI到達の複合的兆候 | o3 87.5%。各社CEO予測（バイアスフラグ付き） | elevated approaching |
| [IND-022](../config/indicators.json) スキル再定義 | コーディングの価値がAI管理にシフト | 82%採用率。ジュニア採用14-73%減。AIスキル56%高給与 | **high** rising |
| [IND-023](../config/indicators.json) 政府のAI強制力 | 経済的手段でAI安全姿勢を抑圧 | Pentagon契約終了、Senate除外、Google Maven再参入。条件3（他社萎縮）は未確認 | **high** rising |
| [IND-024](../config/indicators.json) AI実効性 | 実際のROI・品質 | 92%正のROI（2.8x）。40%キャンセルリスク。二極化兆候明確 | elevated rising |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-03-29 | OpenAI $120B調達、Sora終了を反映。AI ROI二極化（92%正 vs 40%キャンセルリスク）を追加。7社SDK同時更新を記録。セキュリティ事件連鎖（OpenClaw 135K暴露、Meta Sev-1）を追加。労働市場データ更新（Cognizant新卒採用増）。IND-024 monitoring→elevated昇格反映 |
| 2026-03-24 | 2週間分のインテリジェンスを統合。SCN-003 21%に上昇。SCN-BS-001 11%に倍増。セキュリティ事件連鎖（OpenClaw/Claudy Day/MCP Shadow IT）を追加。エージェントSDK戦争の同時進行を記録。労働市場データ更新。193カ国ジュネーブAIアコード追加。ROI乖離の追加データ（PwC/BCG/McKinsey）。ベンチマーク多面化（GPQA/SWE-bench/ARC-AGI各社首位が異なる事実）。DeepSeek V4/NVIDIA OpenShell追加 |
| 2026-03-09 | GPT-5.4 Pro人間超え（ARC-AGI-2 83.3%）を反映。SCN-002 42%に更新。資金集中$195.1B |
| 2026-03-01 | IND-023 high昇格と政府介入の質的変化を追記 |
| 2026-02-23 | 初版作成（AAIF設立後の市場構造再定義）
