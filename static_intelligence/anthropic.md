# Anthropic

> 最終更新: 2026-03-24

エンタープライズLLM支出40%で首位。Claude Code愛用率46%。SWE-bench Verified 80.9%で首位。だがPentagonは$200M契約を正式終了し、Senateは3大AIツールの承認からClaudeだけを除外した。

逆説的に、政府排除が民間市場を押し上げている。ビジネスサブスクリプションシェアは24.4%（+4.9pt）で、新規AI導入企業の70%がAnthropicを選んでいる [INFO-033](../Information/2026-03-22/collected-raw.md#INFO-033)。安全性を貫いたことで政府に排除され、排除されたことで民間の信頼を獲得する——この矛盾した構造がAnthropicの現在地。

## 政府との対立（進行中）

時系列で追うと構造が見える。

- **2月27日**: Trump政権がSCR指定・連邦使用禁止。理由は自律兵器と大量監視への制限を貫いたこと [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048)
- **同日夜**: OpenAIがDoWと契約締結 [INFO-097](../Information/2026-03-01/collected-raw.md#INFO-097)
- **3月9日**: Anthropicが憲法修正第1条に基づきDoD提訴
- **3月11日**: Google・OpenAI社員30名超がAmicus briefを提出 [INFO-055](../Information/2026-03-11/collected-raw.md#INFO-055)
- **3月14日**: 米国テック労働者70万人がAmazon/Google/Microsoftに安全ガードレール維持を要請 [INFO-056](../Information/2026-03-14/collected-raw.md#INFO-056)
- **3月20日**: SenateがChatGPT/Gemini/CopilotをTier 2承認。Claudeは「評価中」として除外 [INFO-008](../Information/2026-03-20/collected-raw.md#INFO-008)。提訴翌日のタイミングは政治的
- **3月21日**: Pentagon、$200M契約を正式終了 [INFO-044](../Information/2026-03-21/collected-raw.md#INFO-044)。同日Googleが2018年のProject Maven撤退を覆し再参入

LA Timesは「シリコンバレーに萎縮効果」と報道 [INFO-052](../Information/2026-03-21/collected-raw.md#INFO-052)。ただし[IND-023](../config/indicators.json)の条件3（他社の安全姿勢後退）は明確に確認されていない。

## この会社は何者か

Dario Amodei率いるAI企業。主力はClaude 4.6シリーズ（Opus/Sonnet/Haiku）、Claude Code、Agent SDK。

資金は$30B（Series G、$380B評価額、2026年2月）。年間収益$14B、80%がB2B（$11.2B）。$100K以上支出の企業は前年比7倍。エンタープライズLLM支出シェアは40%で首位（2023年の12%から急成長、OpenAIの27%に逆転）。Rampデータでは24.4%のビジネスがAnthropicに支払っており、1年前の「25社に1社」から「4社に1社」に [INFO-033](../Information/2026-03-22/collected-raw.md#INFO-033)。

**Claude Code**: 開発者愛用率46%でCursor（19%）、GitHub Copilot（9%）を大きく引き離す [INFO-013](../Information/2026-03-08/collected-raw.md#INFO-013)。v2.1.76でMCP elicitation対応、1Mコンテキスト標準化、SOC2 Type II準拠 [INFO-012](../Information/2026-03-18/collected-raw.md#INFO-012)。長文コンテキストの価格サーチャージ撤廃（Opus/Sonnet 4.6） [INFO-020](../Information/2026-03-23/collected-raw.md#INFO-020)。70%のFortune 100が採用との報告があるが、ソースはLinkedIn（B-2）で要確認。

**Agent SDK**: TypeScript v0.2.81でforkSession、cancel_async_message、MCP elicitation hooks対応。GitHub Stars 992（OpenAIの2,500に対して弱い）。

**Claude Partner Network**: $100M初期投資。Accentureが30,000人にClaude研修 [INFO-001](../Information/2026-03-21/collected-raw.md#INFO-001)。Claude Certified Architect認定プログラム開始。

直近の動き: Vercept買収でOSWorld 72.5%達成 [INFO-002](../Information/2026-03-10/collected-raw.md#INFO-002)。Sydney開設（APAC 4拠点目）。インド#2市場、元Microsoft India MDのIrina Ghoseを起用。Coworkに永続エージェントスレッド追加（Pro/Max）。Claude Opus 4.6がFirefox脆弱性22件を発見（14件が高深刻度）[INFO-012](../Information/2026-03-12/collected-raw.md#INFO-012)。

**セキュリティ課題**: 「Claudy Day」脆弱性チェーン（OASIS Security発見）——URLパラメータ経由プロンプトインジェクション→Files APIデータ窃取→claude.comオープンリダイレクト。Google Ads経由の攻撃ベクトル。Anthropicは責任ある開示で修正済み [INFO-042](../Information/2026-03-23/collected-raw.md#INFO-042)。Coworkプロンプトインジェクション脆弱性（悪意ファイル→隠しプロンプト注入→ファイル窃取）も報告 [INFO-036](../Information/2026-03-23/collected-raw.md#INFO-036)。

## 何をやろうとしているか

### 安全性でエンタープライズを取る（H-ANT-001、確度51%）

SOC2準拠、Compliance API、ASL-3保護で規制業界を取る戦略。エンタープライズ40%シェアとRampデータ（新規70%がAnthropic選択）は、民間ではこの戦略が機能している証拠。EU AI法完全施行（2026年8月）は追い風。NBIM（ノルウェー年金基金）が生産性20%向上、AIG引受時間5倍短縮と具体的な成果も出始めている [INFO-003](../Information/2026-03-20/collected-raw.md#INFO-003)。

しかし確度は60%→51%に急落した。Pentagon $200M契約終了とSenate除外で、政府市場（推定$100B超）の扉が閉まりつつある。Pentagon交渉再開の報 [INFO-024](../Information/2026-03-08/collected-raw.md#INFO-024) も、契約終了で実質的に上書きされた。

安全性堅持が政府で罰になり、民間で報われる——この二極化がどちらに傾くかで仮説の行方が決まる。

### 開発者ツールで差別化する（H-ANT-002、確度73%）— 全仮説中最高

Claude Code + Bun + Agent SDKの3点セットによる差別化。Claude Codeはターミナルで直接動き、ローカル実行が可能な点でクラウド依存のOpenAI Shellと対照的。

SWE-bench Verified 80.9%で首位（GPT-5.4 71.7%、Gemini 3.1 Pro 63.8%）はコーディング性能での優位を示す。Menlo Ventures調査ではAIコーディング市場の50%超を獲得。

ただし確度は78%→73%に低下。GitHub Stars（992 vs OpenAI 2,500）、SDK dependents（Claude少 vs OpenAI 124 NPM）の差はオープンソースコミュニティでの訴求力の弱さを示す。Pragmatic Engineer調査は早期採用者に偏ったC-3ソース。「愛用率46%」と「エンタープライズ標準」の間には因果の飛躍がある。

この仮説が正しければ、Fortune 500での標準採用とAgent SDK外部開発者の急増が見える。間違いなら、Copilot/Cursor/Codexへの流出が見える。

### マルチクラウドで広げる（H-ANT-003、確度10%、watch）

Claudeは唯一、3大クラウド（AWS、GCP、Azure）全てで利用可能なフロンティアAIモデル [INFO-003](../Information/2026-03-20/collected-raw.md#INFO-003)。主戦略ではないが、配布チャネルとしての意味はある。

## 強みと弱み

Anthropicの強みは、エンタープライズでの地位、Claude Codeのコーディング性能、そして逆説的に政府排除が生んだ民間の信頼。LLM支出40%シェア、新規の70%がAnthropic選択という数字は強力。SWE-bench Verified 80.9%首位はコーディングツールとしての実力の裏付け。3大クラウド全対応は配布面での優位。Partner Networkの$100M投資とAccenture 30,000人研修はエコシステム構築が進んでいる証拠。

弱みは3つの構造的課題。まず政府市場の喪失——Pentagon $200M終了、Senate除外、$13.4Bの自律兵器予算からの排除 ([IND-023](../config/indicators.json), **high**)。安全性が強みであるはずの場所で、安全性ゆえに排除された。次に、ARC-AGI-2での性能劣位。Claude Opus 4.5は37%で、GPT-5.4 Pro（83.3%）やGemini 3.1 Pro（77.1%）に遠く及ばない（ただしGPQAやSWE-benchでは競争力あり）。最後に、セキュリティ脆弱性の連鎖。Claudy Day、Coworkプロンプトインジェクション、サンドボックス脱出——安全性を看板にする企業にとって矛盾が目立つ。

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Claude Code ARR・市場シェア推移 | 開発者ツール戦略の成否 | 愛用率46%首位。SWE-bench 80.9%首位。ただしGitHub Stars 992はOpenAI 2,500に劣後 |
| エンタープライズLLMシェア | 40%を維持するか。OpenAI反攻の兆候は | 40%首位。新規70%がAnthropic選択 ([IND-008](../config/indicators.json), elevated) |
| Anthropic vs DoD訴訟の行方 | 安全性方針が法的に支持されるか | 憲法修正第1条に基づき提訴中 |
| 他社の安全姿勢の変化 | 萎縮効果（[IND-023](../config/indicators.json)条件3）が確認されるか | 70万人請願。Google Maven再参入は部分的な証拠 |
| EU AI法施行後の市場変化 | 安全性差別化が国際市場で強化されるか | 2026年8月完全施行予定 |
| セキュリティ脆弱性の改善 | Claudy Day等の修正後、新たな問題が出ないか | 修正済みだが、安全性ブランドへの影響は残る |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-03-24 | 2週間分統合。Pentagon $200M契約正式終了、Senate Claude除外を反映。H-ANT-001 51%に低下、H-ANT-002 73%に低下。Rampデータ（24.4%シェア、新規70%選択）追加。Claudy Day/Cowork脆弱性追加。SWE-bench 80.9%首位。Partner Network $100M。Agent SDK v0.2.81。APAC展開（Sydney/India）。マルチクラウド全対応を記録 |
| 2026-03-09 | Claude Code愛用率46%首位。H-ANT-002 78%。Pentagon交渉再開でH-ANT-001 60%に下降 |
| 2026-03-01 | SCR指定・連邦使用禁止イベントを追記 |
| 2026-02-23 | 初版作成
