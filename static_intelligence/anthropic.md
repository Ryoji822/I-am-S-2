# Anthropic

> 最終更新: 2026-04-06
> 確度: 高

エンタープライズLLM支出40%で首位。Claude Code愛用率46%。SWE-bench Verified 80.9%で首位。2026年4月、バイオテクAIスタートアップCoefficient Bioを$400Mで買収し、ライフサイエンス領域の垂直統合を加速した [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。シドニーオフィス開設でアジア太平洋4拠点体制に [INFO-001](../Information/2026-04-06/collected-raw.md#INFO-001)。Pentagonは$200M契約を正式終了し、Senateは3大AIツールの承認からClaudeだけを除外した。

逆説的に、政府排除が民間市場を押し上げている。安全性を貫いたことで政府に排除され、排除されたことで民間の信頼を獲得する——この矛盾した構造がAnthropicの現在地。

## 政府との対立（進行中）

時系列で追うと構造が見える。

- **2月27日**: Trump政権がSCR指定・連邦使用禁止。理由は自律兵器と大量監視への制限を貫いたこと [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048)
- **同日夜**: OpenAIがDoWと契約締結 [INFO-097](../Information/2026-03-01/collected-raw.md#INFO-097)
- **3月9日**: Anthropicが憲法修正第1条に基づきDoD提訴
- **3月11日**: Google・OpenAI社員30名超がAmicus briefを提出 [INFO-055](../Information/2026-03-11/collected-raw.md#INFO-055)
- **3月14日**: 米国テック労働者70万人がAmazon/Google/Microsoftに安全ガードレール維持を要請 [INFO-056](../Information/2026-03-14/collected-raw.md#INFO-056)
- **3月20日**: SenateがChatGPT/Gemini/CopilotをTier 2承認。Claudeは「評価中」として除外 [INFO-008](../Information/2026-03-20/collected-raw.md#INFO-008)
- **3月21日**: Pentagon、$200M契約を正式終了 [INFO-044](../Information/2026-03-21/collected-raw.md#INFO-044)
- **3月30日**: PentagonがAnthropicを「サプライチェーンリスク」指定。連邦判事が一時差止命令 [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008)

LA Timesは「シリコンバレーに萎縮効果」と報道 [INFO-052](../Information/2026-03-21/collected-raw.md#INFO-052)。ただし[IND-023](../config/indicators.json)の条件3（他社の安全姿勢後退）は明確に確認されていない。連邦判事Linが「オーウェル的」として一時差止を発行したことで、政府の措置に法的歯止めがかかった [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008)。

## この会社は何者か

Dario Amodei率いるAI企業。主力はClaude 4.6シリーズ（Opus/Sonnet/Haiku）、Claude Code、Agent SDK。

資金は$30B（Series G、評価額$380B→$183Bに修正報道あり、2026年2月）。年間収益$14B、80%がB2B（$11.2B）。$100K以上支出の企業は前年比7倍。エンタープライズLLM支出シェアは40%で首位。Rampデータでは24.4%のビジネスがAnthropicに支払っている [INFO-033](../Information/2026-03-22/collected-raw.md#INFO-033)。

**Claude Code**: 開発者愛用率46%でCursor（19%）、GitHub Copilot（9%）を大きく引き離す [INFO-013](../Information/2026-03-08/collected-raw.md#INFO-013)。v2.1.85でMCP elicitation対応、1Mコンテキスト標準化、SOC2 Type II準拠。長文コンテキストの価格サーチャージ撤廃。

**Agent SDK**: TypeScript v0.2.85でClaude Code v2.1.85とパリティ。GitHub Stars 992。

**Claude Partner Network**: $100M初期投資。Accentureが30,000人にClaude研修 [INFO-001](../Information/2026-03-21/collected-raw.md#INFO-001)。

直近の動き: (1) **Coefficient Bioを$400Mで買収**——ステルスバイオテクAIスタートアップ。ライフサイエンス領域の垂直統合 [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。(2) **シドニーオフィス開設**——アジア太平洋4拠点目（東京、バンガロア、ソウル、シドニー）。豪州・NZのClaude.ai使用率が人口比で世界4位・8位 [INFO-001](../Information/2026-04-06/collected-raw.md#INFO-001)。(3) **Claude for Financial Services発表**——Databricks、Snowflake、S&P Global等とMCPコネクタ統合。NBIMで20%生産性向上 [INFO-002](../Information/2026-04-06/collected-raw.md#INFO-002)。(4) **Claude for Life Sciences発表**——Benchling、PubMed、10x Genomics等とコネクタ統合。Sonnet 4.5がProtocol QA Benchmarkで0.83（人間ベースライン0.79超え）[INFO-003](../Information/2026-04-06/collected-raw.md#INFO-003)。(5) Claude Agent SDK v0.2.85リリース。(6) Claude Codeソース流出事件（npmリリースにソースマップ誤同梱、512,000行公開）[INFO-007](../Information/2026-04-06/collected-raw.md#INFO-007)。(7) Pentagonサプライチェーンリスク指定で連邦判事が一時差止 [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008)。

**セキュリティ課題**: 「Claudy Day」脆弱性チェーン（OASIS Security発見）——URLパラメータ経由プロンプトインジェクション→Files APIデータ窃取→claude.comオープンリダイレクト [INFO-042](../Information/2026-03-23/collected-raw.md#INFO-042)。Claude Codeソース流出（512,000行）はSOC2準拠確認済みとの発表 [INFO-007](../Information/2026-04-06/collected-raw.md#INFO-007)。

## 何をやろうとしているか

### 安全性でエンタープライズを取る（H-ANT-001、確度53%）

SOC2準拠、Compliance API、ASL-3保護で規制業界を取る戦略。エンタープライズ40%シェアとRampデータ（新規70%がAnthropic選択）は、民間ではこの戦略が機能している証拠。EU AI法完全施行（2026年8月）は追い風。

**垂直統合の加速**: Coefficient Bio買収（$400M）でライフサイエンス領域のAI開発能力を内製化 [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。Claude for Life Sciences、Claude for Financial Servicesと続く業界別ソリューション展開は、安全性差別化を「製品」として具体化する動き。

確度は52%→53%に微増 [INFO-001](../Information/2026-04-06/collected-raw.md#INFO-001)。評価額$183B・ARR $5B報道でエンタープライズ市場優位が強化。ただしPentagon $200M契約終了、Senate除外、サプライチェーンリスク指定で政府市場（推定$100B超）の扉は閉まりつつある。

安全性堅持が政府で罰になり、民間で報われる——この二極化がどちらに傾くかで仮説の行方が決まる。

### 開発者ツールで差別化する（H-ANT-002、確度74%）— 全仮説中最高

Claude Code + Bun + Agent SDKの3点セットによる差別化。Claude Codeはターミナルで直接動き、ローカル実行が可能な点でクラウド依存のOpenAI Shellと対照的。

SWE-bench Verified 80.9%で首位（GPT-5.4 71.7%、Gemini 3.1 Pro 80.6%）。Menlo Ventures調査ではAIコーディング市場の50%超を獲得。

確度は74%で維持。GitHub Stars（992 vs OpenAI 2,500）の差はオープンソースコミュニティでの訴求力の弱さを示す。Claude Codeソース流出（512,000行）[INFO-007](../Information/2026-04-06/collected-raw.md#INFO-007)はアーキテクチャが分析対象になったが、SOC2準拠確認済み。

### マルチクラウドで広げる（H-ANT-003、確度11%、watch）

Claudeは唯一、3大クラウド（AWS、GCP、Azure）全てで利用可能なフロンティアAIモデル。だが確度は12%→11%に低下。INFO-001でAWS依存深化がマルチクラウド戦略の反証 [INFO-001](../Information/2026-04-06/collected-raw.md#INFO-001)。シドニーオフィス開設で「現地コンピュート容量拡張を検討」とあるが、AWS依存が続いている。

## 強みと弱み

Anthropicの強みは、エンタープライズでの地位、Claude Codeのコーディング性能、そして逆説的に政府排除が生んだ民間の信頼。LLM支出40%シェア、新規の70%がAnthropic選択という数字は強力。SWE-bench Verified 80.9%首位。3大クラウド全対応は配布面での優位。Partner Networkの$100M投資。**Coefficient Bio買収でライフサイエンス領域の垂直統合** [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013)。シドニーオフィス開設でアジア太平洋4拠点体制 [INFO-001](../Information/2026-04-06/collected-raw.md#INFO-001)。

弱みは3つの構造的課題。まず政府市場の喪失——Pentagon $200M終了、Senate除外、サプライチェーンリスク指定、$13.4Bの自律兵器予算からの排除 ([IND-023](../config/indicators.json), **high**)。安全性が強みであるはずの場所で、安全性ゆえに排除された。次に、ARC-AGI-2での性能劣位。Claude Opus 4.5は37%で、GPT-5.4 Pro（83.3%）やGemini 3.1 Pro（77.1%）に遠く及ばない。最後に、セキュリティ脆弱性の連鎖。Claudy Day、Claude Codeソース流出——安全性を看板にする企業にとって矛盾が目立つ。

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Claude Code ARR・市場シェア推移 | 開発者ツール戦略の成否 | 愛用率46%首位。SWE-bench 80.9%首位。GitHub Stars 992 |
| エンタープライズLLMシェア | 40%を維持するか。OpenAI反攻の兆候は | 40%首位。新規70%がAnthropic選択 ([IND-008](../config/indicators.json), elevated) |
| Anthropic vs DoD訴訟の行方 | 安全性方針が法的に支持されるか | 連邦判事が一時差止発行 [INFO-008](../Information/2026-04-06/collected-raw.md#INFO-008) |
| Coefficient Bio統合の成果 | ライフサイエンス垂直統合が機能するか | $400M買収完了 [INFO-013](../Information/2026-04-06/collected-raw.md#INFO-013) |
| シドニーオフィス展開 | アジア太平洋拡大が進むか | 4拠点目開設。豪州・NZ使用率4位・8位 [INFO-001](../Information/2026-04-06/collected-raw.md#INFO-001) |
| EU AI法施行後の市場変化 | 安全性差別化が国際市場で強化されるか | 2026年8月完全施行予定 |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-06 | Coefficient Bio $400M買収、シドニーオフィス開設（APAC 4拠点）、Claude for Financial Services/Life Sciences、Claude Codeソース流出、Pentagonサプライチェーンリスク指定・連邦判事一時差止を追加。H-ANT-001 52%→53%、H-ANT-003 12%→11%に更新 |
| 2026-03-28 | Claude Agent SDK v0.2.79リリース、Claude Cowork SOC 2制限を追加 |
| 2026-03-24 | 2週間分統合。Pentagon $200M契約正式終了、Senate Claude除外を反映。H-ANT-001 51%、H-ANT-002 73%に更新 |
| 2026-03-09 | Claude Code愛用率46%首位。H-ANT-002 78%。Pentagon交渉再開でH-ANT-001 60%に下降 |
| 2026-03-01 | SCR指定・連邦使用禁止イベントを追記 |
| 2026-02-23 | 初版作成 |
