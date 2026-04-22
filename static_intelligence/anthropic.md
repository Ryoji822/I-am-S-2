# Anthropic

> 最終更新: 2026-04-22
> 確度: 高

エンタープライズLLM支出40%で首位。Claude Code $1B ARR達成 [INFO-001](../Information/2026-04-08/collected-raw.md#INFO-001)。SWE-bench Verified 80.9%で首位。2026年4月16日、**Claude Opus 4.7**がGA到達——CursorBench 70%（Opus 4.6比+12pt）、XBOW visual-acuity 98.5%（従来54.5%から質的飛躍）、**Cyber Verification Program**を新設 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。Claude Designがデザイン→実装のワークフローをClaudeエコシステム内に閉じ込める [INFO-004](../Information/2026-04-19/collected-raw.md#INFO-004)。

だが逆説が三重になった。安全性を貫いたことで政府に排除され、排除されたことで民間の信頼を獲得し、獲得した信頼の大きさが収益を押し上げている——**$30B ARR到達がA-1（公式確認）で検証された** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。Penn Mutual AM Bloomberg引用の第三者確認。ただしPitchBookは「Big Four監査に耐えられない」と指摘し、$30B vs $22Bの乖離観測も残る [INFO-012](../Information/2026-04-22/collected-raw.md#INFO-012)。

## 政府との対立（構造化完了、新局面へ）

時系列で追くと一本の線が見える。

- **2月27日**: Trump政権がSCR指定・連邦使用禁止。理由は自律兵器と大量監視への制限を貫いたこと [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048)
- **3月9日**: Anthropicが憲法修正第1条に基づきDoD提訴
- **4月8日**: **連邦控訴裁がAnthropicの一時差し止め請求を棄却**。SCR指定が確定 [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。OpenAIが直後に$200M契約を獲得
- **4月中旬**: **新たな対立の多層化** — PentagonがAnthropicを供給チェーンリスク指定し連邦システムから排除 [INFO-028](../Information/2026-04-22/collected-raw.md#INFO-028)。だが**NSAはPentagon対立にもかかわらずMythos Previewを使用中**と報道 [INFO-029](../Information/2026-04-22/collected-raw.md#INFO-029)。Steve BannonがAnthropicのPentagon拒否を支持し、跨党的な倫理支持が形成された [INFO-030](../Information/2026-04-22/collected-raw.md#INFO-030)。**裁判所がPentagonのAnthropic禁止を審査中**——政府側勝訴の場合、新たな形態の政治的報復が正当化されると指摘 [INFO-031](../Information/2026-04-22/collected-raw.md#INFO-031)。同時に**Trump大統領がAnthropic-DoD契約は「可能」と発言** [INFO-009](../Information/2026-04-22/collected-raw.md#INFO-009)
- **4月20日**: Anthropic公式ブログでAmazon提携拡大を発表——最大5GW Trainium計算能力確保、10年間$100B以上AWS投資、追加$5B即時投資＋最大$20B追加 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。100,000+顧客がBedrockでClaude利用

DOD「全合法目的での無制限アクセス」要求 → Anthropic拒否 → SCR指定 → 控訴裁差し止め棄却 → OpenAI $200M契約 → Pentagon排除 → NSA矛盾的使用 → 裁判所審査 → Trump「可能」発言。政府-AI企業緊張が「構造化完了」から「多層化」に移行している。

## この会社は何物か

Dario Amodei率いるAI企業。主力は**Claude Opus 4.7**、Claude 4.6シリーズ（Sonnet/Haiku）、Claude Code、Agent SDK、**Claude Managed Agents**（フルマネージドエージェントインフラ）、**Claude Design**（ビジュアルデザインツール）、Mythos Preview（セキュリティ研究特化）。

資金は$30B（Series G、評価額$183B、2026年2月）。**$30B ARR到達がA-1で確認**——2025年末$9Bから3.3倍 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。Penn Mutual AM Bloomberg引用。$1M以上年間支出の企業顧客が1000社を突破。80%がB2B。Claude Codeが$1B ARR達成——一般公開から6ヶ月 [INFO-001](../Information/2026-04-08/collected-raw.md#INFO-001)。エンタープライズLLM支出シェア40%で首位。

**$30B ARRに関する注記**: Anthropic公式ブログ発表がPenn Mutual AM Bloomberg引用でA-1第三者確認された [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。ただしPitchBookは「Big Four監査に耐えられない」と指摘 [INFO-012](../Information/2026-04-22/collected-raw.md#INFO-012)。SEC提出書類・監査報告書による検証は未確認。$30B vs $22B乖離観測が残る。

**Amazon提携拡大**（2026年4月20日）: 最大5GWのTrainium計算能力確保（Trainium2 Q2 + Trainium3年末）。10年間$100B以上のAWS投資コミットメント。Amazonが$5B即時投資＋最大$20B追加（合計最大$33B投資）。100,000+顧客がBedrockでClaude利用。1M+ Trainium2チップ現在使用中。Claude Platform on AWS近日提供。アジア・欧州への推論拡張 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。

**インフラ**: Google/Broadcomと複数GW規模の次世代TPU計算能力契約（2027年稼働予定）。AWS Trainium、Google TPU、NVIDIA GPUの3プラットフォームで稼働。

**Claude Opus 4.7**（2026年4月16日GA）: CursorBench 70%。XBOW visual-acuity 98.5%。高解像度画像対応（最大3.75MP、従来比3倍以上）。Cyber Verification Program新設。BenchLM 94/100 (#3) [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。

**Claude Design**: Opus 4.7搭載ビジュアルデザインツール。Claude Codeへのワンクリックハンドオフがデザイン→実装のワークフローをClaude内に閉じ込める [INFO-004](../Information/2026-04-19/collected-raw.md#INFO-004)。

**Managed Agents**: 2026年4月8日GA到達。フルマネージドエージェントハーネス [INFO-078](../Information/2026-04-10/collected-raw.md#INFO-078)。

**Mythos Preview**: セキュリティ研究特化のフロンティアモデル。**欧州銀行向けMythos提供を計画**——金融規制対応のエンタープライズ展開加速 [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008)。NSAがPentagon対立にもかかわらず使用中 [INFO-029](../Information/2026-04-22/collected-raw.md#INFO-029)。

**Agent SDK**: TypeScript v0.2.111-112でOpus 4.7対応。MCP per-tool permission_policy追加 [INFO-015](../Information/2026-04-19/collected-raw.md#INFO-015)。12リリース/週（毎日更新ペース）。1.3K GitHub stars。

**Claude for Financial Services**: S&P Global、FactSet、PitchBook、Morningstar等のデータプロバイダーとMCP統合 [INFO-006](../Information/2026-04-19/collected-raw.md#INFO-006)。

**Enterprise価格シフト**: Claude Enterpriseのシートベース価格設定から**使用量ベース課金に移行**。コンピュート需要急増に対応。ヘビーユーザーのコスト上昇 [INFO-033](../Information/2026-04-22/collected-raw.md#INFO-033)。

**AAR（Automated Alignment Researcher）**: Claudeが自律的アライメント研究者として機能。自身のアイデアを開発・テストする能力を実証 [INFO-049](../Information/2026-04-22/collected-raw.md#INFO-049)。AI再帰的改善のマイルストーン。

**Amodei予測**: Dario Amodei CEOがソフトウェアエンジニアリングは6-12ヶ月以内に大部分自動化されると予測 [INFO-050](../Information/2026-04-22/collected-raw.md#INFO-050)。Anthropic内部でもエンジニアのモデル依存が進行。

**セキュリティ課題**: CoworkアクティビティがAudit Logs・Compliance API・Data Exportsで捕捉されない [INFO-022](../Information/2026-04-22/collected-raw.md#INFO-022)。消費者成長がピーク時の信頼性に影響 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。

## 何をやろうとしているか

### 安全性でエンタープライスを取る（H-ANT-001、確度52%）

SOC2準拠、Compliance API、ASL-3保護で規制業界を取る戦略。エンタープライズ40%シェアとRampデータ（新規70%がAnthropic選択）は、民間ではこの戦略が機能している証拠。EU AI法完全施行（2026年8月）は追い風。

**垂直統合の加速**: Claude for Financial ServicesでBridgewater、Commonwealth Bank of Australia、AIGが導入 [INFO-006](../Information/2026-04-19/collected-raw.md#INFO-006)。**欧州銀行向けMythos提供計画**は規制金融市場への本格参入 [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008)。

SCR指定が連邦控訴裁で確定したことで政府市場からの排除が法的に固まった。だが**NSAがPentagon対立にもかかわらずMythosを使用** [INFO-029](../Information/2026-04-22/collected-raw.md#INFO-029)、**裁判所がPentagon禁止を審査中** [INFO-031](../Information/2026-04-22/collected-raw.md#INFO-031)、**Trump大統領がAnthropic-DoD契約を「可能」** [INFO-009](../Information/2026-04-22/collected-raw.md#INFO-009) と、政府内部の分裂が顕在化している。$30B A-1確認は安全性が民間市場で報われている証拠 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。

確度は52%に上昇 [Arbiter v3.57](../state/arbiter-2026-04-22.md)。安全性堅持が政府で罰になり、民間で報われる——この二極化が民間側に傾いている。

### 開発者ツールで差別化する（H-ANT-002、確度70%）— 全仮説中最高

Claude Code + Bun + Agent SDKの3点セットによる差別化。Managed Agents GAでフルマネージドエージェントインフラが加わり差別化の厚みが増した。Claude Designがデザイン→実装のワークフローに新たな接点を作った。

SWE-bench Verified 80.9%で首位（GPT-5.4 71.7%、Gemini 3.1 Pro 80.6%）。Opus 4.7がCursorBench 70%に到達 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。

確度は70%（Arbiter v3.55）。Agent SDK 12リリース/週はCだが多義的（安定性の欠如の可能性も）。KIQ-AGENT-001（チャーン率/NPS）が未回答で検証可能性に疑義。

### マルチクラウドで広げる（H-ANT-003、確度7%）

Claudeは3大クラウド全てで利用可能な唯一のフロンティアAIモデル。だが確度は7%に低下。**Amazon提携拡大（5GW Trainium・$100B AWS投資）**でAWS依存がさらに深まった [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。Google/Broadcom TPU契約と合わせてインフラ投資の偏りが一段と強まった。「同等」要件からの乖離拡大。

## 強みと弱み

Anthropicの強みは、エンタープライスでの地位、Claude Codeのコーディング性能、そして逆説的に政府排除が生んだ民間の信頼。LLM支出40%シェア。SWE-bench Verified 80.9%首位。Opus 4.7 CursorBench 70%・XBOW 98.5% [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。3大クラウド全対応。Partner Networkの$100M投資。**$30B ARR A-1確認** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。**Amazon提携拡大（5GW・$100B・100K+Bedrock顧客）** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。**欧州銀行Mythos提供計画**で規制金融市場参入 [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008)。Claude for Financial Services MCP統合 [INFO-006](../Information/2026-04-19/collected-raw.md#INFO-006)。AAR自律的アライメント研究 [INFO-049](../Information/2026-04-22/collected-raw.md#INFO-049)。Agent SDK MCP per-tool permission [INFO-016](../Information/2026-04-17/collected-raw.md#INFO-016)。

弱みは4つの構造的課題。まず政府市場の喪失——SCR指定確定、Pentagon供給チェーンリスク指定、Senate除外。ただしNSA使用矛盾・裁判所審査・Trump「可能」発言で閉じきっていない。次に、ARC-AGI-2での性能劣位。Claude Opus 4.5は37%でGPT-5.4 Pro（83.3%）に遠く及ばない。三つ目に、セキュリティとコンプライアンスのギャップ。Cowork監査ログギャップ [INFO-022](../Information/2026-04-22/collected-raw.md#INFO-022)、Claude Codeソース流出、Mythosサンドボックス脱出。最後に、PitchBook「Big Four監査耐えられない」指摘 [INFO-012](../Information/2026-04-22/collected-raw.md#INFO-012) が残り、$30Bの完全な第三者検証にはSEC書類/監査報告書が必要。Enterprise使用量課金移行でヘビーユーザーのコスト上昇も顧客離れリスク [INFO-033](../Information/2026-04-22/collected-raw.md#INFO-033)。

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Claude Code ARR・市場シェア推移 | 開発者ツール戦略の成否 | 愛用率46%首位。SWE-bench 80.9%首位。$1B ARR |
| エンタープライズLLMシェア | 40%を維持するか | 40%首位。新規70%がAnthropic選択 ([IND-008](../config/indicators.json)) |
| Anthropic vs DoD訴訟の行方 | SCR指定の最終的な法的判断 | **多層化**: SCR確定 + NSA矛盾使用 + 裁判所審査 + Trump「可能」 [INFO-029](../Information/2026-04-22/collected-raw.md#INFO-029) [INFO-031](../Information/2026-04-22/collected-raw.md#INFO-031) |
| $30B ARRの完全検証 | A-1確認済み、Big Four監査・SEC書類待ち | **A-1確認** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。PitchBook懐疑残る [INFO-012](../Information/2026-04-22/collected-raw.md#INFO-012) |
| 欧州銀行Mythos展開 | 安全性差別化が規制金融市場で通じるか | 提供計画報道 [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008) |
| Enterprise使用量課金の影響 | ヘビーユーザー離れのリスク | 移行開始 [INFO-033](../Information/2026-04-22/collected-raw.md#INFO-033) |
| Agent SDK安定性 | 12リリース/週が成熟の証か不安定性か | KIQ-AGENT-001未回答継続 |
| AAR再帰的改善 | AIがAIを改善するループの実効性 | 初期実証 [INFO-049](../Information/2026-04-22/collected-raw.md#INFO-049) |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-22 | $30B ARR A-1第三者確認（Penn Mutual AM Bloomberg引用）・Amazon提携拡大（5GW Trainium・$100B AWS投資）・欧州銀行Mythos提供計画・Pentagon/NSA矛盾・裁判所審査・Trump DoD契約「可能」発言・Enterprise使用量課金移行・AAR自律的アライメント研究・Amodei 6-12ヶ月予測を反映して全面書き直し。H-ANT-001 51→52%に更新。政府対立セクションを多層化に対応 |
| 2026-04-19 | Claude Design・Claude for Financial Services MCP統合・Agent SDK 12リリース/週詳細を追加。H-ANT-001 52→51%に更新 |
| 2026-04-17 | 鮮度タイムアウト対応（7日経過）。Claude Opus 4.7 GAを反映して全面書き直し |
| 2026-04-10 | SCR連邦控訴裁敗訴（確定）・$30B ARR自己発表・Managed Agents GAを追加 |
| 2026-04-08 | Claude Mythos Preview・Claude Code $1B ARR・Bun買収を反映 |
