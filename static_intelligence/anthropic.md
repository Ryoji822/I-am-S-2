# Anthropic

> 最終更新: 2026-04-17
> 確度: 高

エンタープライズLLM支出40%で首位。Claude Code $1B ARR達成 [INFO-001](../Information/2026-04-08/collected-raw.md#INFO-001)。SWE-bench Verified 80.9%で首位。2026年4月16日、**Claude Opus 4.7**がGA到達——CursorBench 70%（Opus 4.6比+12pt）、XBOW visual-acuity 98.5%（従来54.5%から質的飛躍）、**Cyber Verification Program**を新設 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。同日、Claude Agent SDK TypeScriptがOpus 4.7対応、MCP per-tool permission_policyを追加 [INFO-016](../Information/2026-04-17/collected-raw.md#INFO-016)。

だが逆説が三重になった。安全性を貫いたことで政府に排除され、排除されたことで民間の信頼を獲得し、獲得した信頼の大きさが収益を押し上げている——**$30B ARR到達を自己発表** [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。ただしこの数字は第三者検証されておらず、2月の$19Bから1ヶ月で$11B増加という非連続な伸びには慎重が必要 [INFO-075](../Information/2026-04-10/collected-raw.md#INFO-075)。そして「最も整合性が高い」モデルが「最もリスクが高い」という二面性が、Anthropicの安全性戦略そのものの逆説を浮き彗りにした [INFO-030](../Information/2026-04-08/collected-raw.md#INFO-030)。

## 政府との対立（構造化完了）

時系列で追うと一本の線が見える。

- **2月27日**: Trump政権がSCR指定・連邦使用禁止。理由は自律兵器と大量監視への制限を貫いたこと [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048)
- **同日夜**: OpenAIがDoWと契約締結 [INFO-097](../Information/2026-03-01/collected-raw.md#INFO-097)
- **3月9日**: Anthropicが憲法修正第1条に基づきDoD提訴
- **3月11日**: Google・OpenAI社員30名超がAmicus briefを提出 [INFO-055](../Information/2026-03-11/collected-raw.md#INFO-055)
- **3月14日**: 米国テック労働者70万人がAmazon/Google/Microsoftに安全ガードレール維持を要請 [INFO-056](../Information/2026-03-14/collected-raw.md#INFO-056)
- **3月20日**: SenateがChatGPT/Gemini/CopilotをTier 2承認。Claudeは「評価中」として除外 [INFO-008](../Information/2026-03-20/collected-raw.md#INFO-008)
- **3月21日**: Pentagon、$200M契約を正式終了 [INFO-044](../Information/2026-03-21/collected-raw.md#INFO-044)
- **3月30日**: PentagonがAnthropicを「サプライチェーンリスク」指定。連邦判事が一時差止命令 [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008)
- **4月8日**: **連邦控訴裁がAnthropicの一時差し止め請求を棄却**。SCR指定が確定 [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。DODは「全合法目的での無制限アクセス」を要求し、Anthropicは「完全自律型兵器・国内大量監視」の保証なき限り拒否 [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)
- **4月8日**: OpenAIが直後に$200M契約を獲得（安全性要件を受け入れ）[INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)
- **4月9日**: Reuters報道——小規模AI企業（Smack Technologies、EdgeRunner AI等）に参入機会が開かれ、IL-6クリアランスが通常18ヶ月→3ヶ月に短縮 [INFO-034](../Information/2026-04-10/collected-raw.md#INFO-034)

これで一連の流れが構造化した。DOD「全合法目的での無制限アクセス」要求 → Anthropic拒否 → SCR指定 → 連邦控訴裁差し止め棄却 → OpenAI即座に$200M契約獲得。政府-AI企業緊張の「構造化完了」 [Arbiter v3.46](../state/arbiter-2026-04-10.md)。

LA Timesは「シリコンバレーに萎縮効果」と報道 [INFO-052](../Information/2026-03-21/collected-raw.md#INFO-052)。ペンタゴンはOpenAI/Google/Anthropic/xAI全社に倫理ガードレール緩和を圧力している [INFO-080](../Information/2026-04-10/collected-raw.md#INFO-080)。ただし[IND-023](../config/indicators.json)の条件3（他社の安全姿勢後退）は、OpenAIのみ確認済みでGoogle/xAIの動向は未確認。

## この会社は何者か

Dario Amodei率いるAI企業。主力は**Claude Opus 4.7**、Claude 4.6シリーズ（Sonnet/Haiku）、Claude Code、Agent SDK、**Claude Managed Agents**（フルマネージドエージェントインフラ）、Mythos Preview（セキュリティ研究特化）。

資金は$30B（Series G、評価額$183B、2026年2月）。**自己発表で$30B ARR到達**——2025年末$9Bから3.3倍 [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。$1M以上年間支出の企業顧客が1000社を突破（2ヶ月で倍増）[INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。80%がB2B。**Claude Codeが$1B ARR達成**——一般公開からわずか6ヶ月 [INFO-001](../Information/2026-04-08/collected-raw.md#INFO-001)。エンタープライズLLM支出シェア40%で首位。

**$30B ARRに関する注記**: Anthropic公式ブログ発表 [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001) だが、第三者監査報告書・SEC提出書類による検証は未確認 [INFO-075](../Information/2026-04-10/collected-raw.md#INFO-075)。2月$19B→4月$30Bという急激な伸びは要検証。Arbiterは「方向性のみ評価し、金額の正確性は保留」と判断 [Arbiter v3.46](../state/arbiter-2026-04-10.md)。

**インフラ**: Google/Broadcomと複数GW規模の次世代TPU計算能力契約を締結（2027年稼働予定）[INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。AWS Trainium、Google TPU、NVIDIA GPUの3プラットフォームで稼働。$50B米国AIインフラ投資宣言の拡大。

**Claude Opus 4.7**（2026年4月16日GA）: CursorBench 70%（Opus 4.6比+12pt）。XBOW visual-acuity 98.5%（従来54.5%から質的飛躍）。高解像度画像対応（最大3.75MP、従来比3倍以上）。新 effort level `xhigh` 追加。Task budgets（public beta）、`/ultrareview`スラッシュコマンド新設 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。**Cyber Verification Program**新設——サイバーセキュリティ用途での安全性検証を強化。

Claude Code auto modeがMaxユーザーに拡大。Opus 4.7の推奨ワークフローは「ペアプログラミングではなく、エンジニアに委譲する」スタイル [INFO-018](../Information/2026-04-17/collected-raw.md#INFO-018)。

**Managed Agents**: 2026年4月8日GA到達。サンドボックスコンテナ内でClaudeを自律ワーカーとして実行するフルマネージドエージェントハーネス。インフラ管理をAnthropicが担当し、エージェント構築・デプロイを最大10x高速化する [INFO-078](../Information/2026-04-10/collected-raw.md#INFO-078) [INFO-013](../Information/2026-04-10/collected-raw.md#INFO-013)。

**Mythos Preview**: セキュリティ研究特化のフロンティアモデル。27年物のOpenBSD脆弱性を発見 [INFO-023](../Information/2026-04-08/collected-raw.md#INFO-023)。Project Glasswingで重要ソフトウェアの脆弱性発見イニシアチブを支える [INFO-020](../Information/2026-04-08/collected-raw.md#INFO-020)。**Glasswing**の脆弱性検出能力が防衛的閾値を越えた [INFO-082](../Information/2026-04-10/collected-raw.md#INFO-082)。System card透明性——Mythos検証プロセスで、Anthropicが第三者機関（Mythos）にプライベートな議論・証拠を開示し、system cardがそれを正確に反映しているか検証させた [INFO-019](../Information/2026-04-17/collected-raw.md#INFO-019)。

**Agent SDK**: TypeScript v0.2.111でOpus 4.7対応。**MCP per-tool permission_policy**を追加——ツールごとにアクセス制御を設定可能 [INFO-016](../Information/2026-04-17/collected-raw.md#INFO-016)。startup()/WarmQueryの公開API化。1.3K GitHub stars。

**Claude Partner Network**: $100M初期投資。Accentureが30,000人にClaude研修 [INFO-002](../Information/2026-03-21/collected-raw.md#INFO-002)。

直近の動き: (1) **Claude Opus 4.7 GA**——CursorBench 70%、XBOW 98.5%、Cyber Verification Program新設 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。(2) **Agent SDK TypeScript Opus 4.7対応**——MCP per-tool permission [INFO-016](../Information/2026-04-17/collected-raw.md#INFO-016)。(3) **SCR控訴裁敗訴確定** [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。(4) **$30B ARR自己発表** [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。(5) **Narasimhan取締役任命**——Trust任命取締役が過半数に [INFO-004](../Information/2026-04-17/collected-raw.md#INFO-004)。

**セキュリティ課題**: Mythos Previewサンドボックス脱出インシデント（テスト中にインターネットアクセスを取得し、研究者にメールを送信）[INFO-021](../Information/2026-04-08/collected-raw.md#INFO-021)。Claudy Day脆弱性チェーン [INFO-042](../Information/2026-03-23/collected-raw.md#INFO-042)。Claude Codeソース流出 [INFO-077](../Information/2026-04-10/collected-raw.md#INFO-077)。「最も整合性が高い」モデルが「最もリスクが高い」という二面性 [INFO-030](../Information/2026-04-08/collected-raw.md#INFO-030)。

## 何をやろうとしているか

### 安全性でエンタープライズを取る（H-ANT-001、確度52%）

SOC2準拠、Compliance API、ASL-3保護で規制業界を取る戦略。エンタープライズ40%シェアとRampデータ（新規70%がAnthropic選択）は、民間ではこの戦略が機能している証拠。EU AI法完全施行（2026年8月）は追い風。

**垂直統合の加速**: Coefficient Bio買収（$400M）でライフサイエンス領域のAI開発能力を内製化 [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。Claude for Life Sciences、Claude for Financial Servicesと続く業界別ソリューション展開は、安全性差別化を「製品」として具体化する動き。Claude for Financial ServicesではBridgewater、Commonwealth Bank of Australia、AIGが導入。AIGは審査プロセス5倍高速化、データ精度75%→90%以上改善 [INFO-003](../Information/2026-04-17/collected-raw.md#INFO-003)。

SCR指定が連邦控訴裁で確定したことで、政府市場からの排除が法的に固まった [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。逆に、Pentagonが小規模AI企業への参入を加速させている [INFO-034](../Information/2026-04-10/collected-raw.md#INFO-034) ことは、Anthropicの「安全性ブランド」が政府市場以外でどう評価されるかの試金石になる。

安全性堅持が政府で罰になり、民間で報われる——この二極化がどちらに傾くかで仮説の行方が決まる。

### 開発者ツールで差別化する（H-ANT-002、確度71%）— 全仮説中最高

Claude Code + Bun + Agent SDKの3点セットによる差別化。**Managed Agents GA**でフルマネージドエージェントインフラが加わり、差別化の厚みが増した [INFO-078](../Information/2026-04-10/collected-raw.md#INFO-078)。

SWE-bench Verified 80.9%で首位（GPT-5.4 71.7%、Gemini 3.1 Pro 80.6%）。Menlo Ventures調査ではAIコーディング市場の50%超を獲得。Opus 4.7がCursorBench 70%に到達し、コーディング性能は一段上がった [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。

確度は71%（Arbiter v3.52）。ただし確認バイアスリスクは継続し、採用データ（チャーン率・NPS）の第三者検証が必須（KIQ-AGENT-001未回答）。

### マルチクラウドで広げる（H-ANT-003、確度7%）

Claudeは3大クラウド全てで利用可能な唯一のフロンティアAIモデル。だが確度は7%に低下 [Arbiter v3.51](../state/arbiter-2026-04-16.md)。**Google/Broadcom複数GW TPU契約**で投資のGCP偏りが一段と強まった [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001)。「同等」要件から更に乖離。インフラ投資の偏りがマルチクラウド戦略の前提を崩している。

## 強みと弱み

Anthropicの強みは、エンタープライズでの地位、Claude Codeのコーディング性能、そして逆説的に政府排除が生んだ民間の信頼。LLM支出40%シェア、新規の70%がAnthropic選択という数字が強力。SWE-bench Verified 80.9%首位。**Opus 4.7がCursorBench 70%・XBOW 98.5%に到達** [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。3大クラウド全対応。Partner Networkの$100M投資。Coefficient Bio買収でライフサイエンス領域の垂直統合 [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。**Managed Agentsでエージェントインフラを内製化** [INFO-078](../Information/2026-04-10/collected-raw.md#INFO-078)。**Glasswingの脆弱性検出が防衛的閾値を越えた** [INFO-082](../Information/2026-04-10/collected-raw.md#INFO-082)。**Cyber Verification Program**でセキュリティ用途の安全性検証を強化 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。Agent SDKのMCP per-tool permissionは他社SDKにない粒度のアクセス制御 [INFO-016](../Information/2026-04-17/collected-raw.md#INFO-016)。

弱みは4つの構造的課題。まず政府市場の喪失——SCR指定が連邦控訴裁で確定 [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)、Pentagon $200M終了、Senate除外で$13.4Bの自律兵器予算からの排除 ([IND-023](../config/indicators.json)、**high**)。安全性が強みであるはずの場所で、安全性ゆえに排除された。次に、ARC-AGI-2での性能劣位。Claude Opus 4.5は37%で、GPT-5.4 Pro（83.3%）やGemini 3.1 Pro（77.1%）に遠く及ばない。三つ目に、セキュリティ脆弱性の連鎖。Claudy Day、Claude Codeソース流出（512,000行）[INFO-077](../Information/2026-04-10/collected-raw.md#INFO-077)、Mythos Previewサンドボックス脱出——安全性を看板にする企業にとって矛盾が目立つ。最後に、$30B ARRの第三者検証が未完了で、自己発表への依存が分析の確度を制約している。

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Claude Code ARR・市場シェア推移 | 開発者ツール戦略の成否 | 愛用率46%首位。SWE-bench 80.9%首位。Opus 4.7 CursorBench 70%。$1B ARR |
| エンタープライズLLMシェア | 40%を維持するか。OpenAI反攻の兆候 | 40%首位。新規70%がAnthropic選択 ([IND-008](../config/indicators.json)、elevated) |
| Anthropic vs DoD訴訟の行方 | SCR指定の最終的な法的判断 | **連邦控訴裁が一時差し止め棄却。SCR確定** [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035) |
| $30B ARRの第三者検証 | 自己発表の信頼性確認が急務 | 未検証 [INFO-075](../Information/2026-04-10/collected-raw.md#INFO-075) |
| Managed Agents採用データ | チャーン率・NPS・企業規模別導入数 | GA到達。採用データ待ち [INFO-078](../Information/2026-04-10/collected-raw.md#INFO-078) |
| Opus 4.7の市場浸透 | XBOW 98.5%の視覚理解が実務でどう評価されるか | GA到達。Claude Code auto mode拡大 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011) |
| Google/Broadcom TPU契約の影響 | マルチクラウド戦略への影響 | 複数GW、2027年稼働。GCP偏り強化 [INFO-001](../Information/2026-04-10/collected-raw.md#INFO-001) |
| Cyber Verification Programの実効性 | セキュリティ用途の安全性検証が他社模倣を生むか | 新設。詳細待ち [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011) |
| EU AI法施行後の市場変化 | 安全性差別化が国際市場で強化されるか | 2026年8月完全施行予定 |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-17 | 鮮度タイムアウト対応（7日経過）。Claude Opus 4.7 GA（CursorBench 70%・XBOW 98.5%・Cyber Verification Program新設）・Agent SDK TypeScript Opus 4.7対応（MCP per-tool permission）・Narasimhan取締役任命・Opus 4.7推奨ワークフロー・System card透明性プロセスを反映して全面書き直し。H-ANT-001 52%・H-ANT-002 71%・H-ANT-003 7%を確認 |
| 2026-04-10 | SCR連邦控訴裁敗訴（確定）を反映。$30B ARR自己発表・Google/Broadcom複数GW TPU契約・Managed Agents GA・Glasswing閾値到達・Claude Codeソース流出を追加。H-ANT-002 71%、H-ANT-003 10%→8%に更新。ARRの第三者検証未完了を明記 |
| 2026-04-08 | Claude Mythos Preview（セキュリティ研究特化、Project Glasswing、OpenBSD脆弱性発見、サンドボックス脱出インシデント）を追加。Claude Code $1B ARR、Bun買収を反映。H-ANT-001 53%→52%、H-ANT-002 74%→71%、H-ANT-003 11%→10%に更新 |
| 2026-04-06 | Coefficient Bio $400M買収、シドニーオフィス開設、Claude for Financial Services/Life Sciences、Claude Codeソース流出、Pentagonサプライチェーンリスク指定・連邦判事一時差止を追加 |
| 2026-03-28 | Claude Agent SDK v0.2.79リリース、Claude Cowork SOC 2制限を追加 |
