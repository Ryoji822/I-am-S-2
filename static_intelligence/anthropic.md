# Anthropic

> 最終更新: 2026-04-24
> 確度: 高

エンタープライズLLM支出40%で首位。Claude Code $1B ARR達成 [INFO-001](../Information/2026-04-08/collected-raw.md#INFO-001)。SWE-bench Verified 80.9%で首位。2026年4月16日、**Claude Opus 4.7**がGA到達——CursorBench 70%（Opus 4.6比+12pt）、XBOW visual-acuity 98.5%（従来54.5%から質的飛躍）、**Cyber Verification Program**を新設 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。Claude Designがデザイン→実装のワークフローをClaudeエコシステム内に閉じ込める [INFO-004](../Information/2026-04-19/collected-raw.md#INFO-004)。

だが逆説が三重になった。安全性を貫いたことで政府に排除され、排除されたことで民間の信頼を獲得し、獲得した信頼の大きさが収益を押し上げている——**$30B ARR到達がA-1（公式確認）で検証された** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。Penn Mutual AM Bloomberg引用の第三者確認。ただしOpenAI CRO流出メモは実際は$22Bと主張 [INFO-046](../Information/2026-04-24/collected-raw.md#INFO-046)、PitchBookも「Big Four監査に耐えられない」と指摘 [INFO-045](../Information/2026-04-24/collected-raw.md#INFO-045)。$30B vs $22Bの$8B乖離が未解決。

そして**Mythosが世界的警報を引き起こした**。NYTがA-1記事で報じた——中央銀行と情報機関が緊急対応に動き出した [INFO-050](../Information/2026-04-24/collected-raw.md#INFO-050)。誰が強力なモデルにアクセスできるかをAnthropicが決定する事態に至っている。「セキュリティ研究特化のフロンティアモデル」の枠を超え、国家規模のリスク評価を触発する存在になった。

## 政府との対立（構造化完了、新局面へ）

時系列で追くと一本の線が見える。

- **7月**: Pentagonと$200M契約を締結 [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068)
- **9月**: GenAI.mil展開交渉で決裂。DODが「全合法目的での無制限アクセス」を要求、Anthropicが「自律兵器・国内大量監視への不使用保証」で拒否 [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068)
- **2月27日**: Trump政権がSCR指定・連邦使用禁止。理由は自律兵器と大量監視への制限を貫いたこと [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048)
- **3月5日**: DODがAnthropicを「サプライチェーンリスク」指定。TrumpがTruth Socialで「全連邦機関でAnthropic使用即時中止」を宣言 [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068)
- **3月9日**: Anthropicが憲法修正第1条に基づきDoD提訴
- **4月8日**: **連邦控訴裁がAnthropicの一時差し止め請求を棄却**。SCR指定が確定 [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035)。OpenAIが直後に$200M契約を獲得
- **4月中旬**: PentagonがAnthropicを供給チェーンリスク指定し連邦システムから排除 [INFO-028](../Information/2026-04-22/collected-raw.md#INFO-028)。だが**NSAはPentagon対立にもかかわらずMythos Previewを使用中** [INFO-029](../Information/2026-04-22/collected-raw.md#INFO-029)。Steve BannonがAnthropicのPentagon拒否を支持 [INFO-030](../Information/2026-04-22/collected-raw.md#INFO-030)。**裁判所がPentagonのAnthropic禁止を審査中** [INFO-031](../Information/2026-04-22/collected-raw.md#INFO-031)。**Trump大統領がAnthropic-DoD契約は「可能」** [INFO-029](../Information/2026-04-24/collected-raw.md#INFO-029)。イラン戦争中もペンタゴンはClaude使用継続
- **4月17日**: AmodeiとWhite Houseで「生産的・建設的」会談（Susie Wiles、Scott Bessent出席）[INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068)
- **4月20日**: Anthropic公式ブログでAmazon提携拡大を発表——最大5GW Trainium計算能力確保、10年間$100B以上AWS投資 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)

$200M契約→交渉決裂→SCR指定→排除→NSA矛盾的使用→White House会談→Trump「可能」発言。政府-AI企業緊張が「構造化完了」から「多層化」に移行している。重要な転換点は、**PentagonがAnthropicの安全性制約を拒絶した**という事実そのものにある。これは政府が「安全性堅持」を市場から排除する要因にした初の大規模事例だ。

## この会社は何物か

Dario Amodei率いるAI企業。主力は**Claude Opus 4.7**、Claude 4.6シリーズ（Sonnet/Haiku）、Claude Code、Agent SDK、**Claude Managed Agents**（フルマネージドエージェントインフラ）、**Claude Design**（ビジュアルデザインツール）、**Mythos**（世界的警報を引き起こしたフロンティアモデル）。

資金は$30B（Series G、評価額$183B、2026年2月）。**$30B ARR到達がA-1で確認**——2025年末$9Bから3.3倍 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。Penn Mutual AM Bloomberg引用。$1M以上年間支出の企業顧客が1000社を突破。80%がB2B。Claude Codeが$1B ARR達成——一般公開から6ヶ月 [INFO-001](../Information/2026-04-08/collected-raw.md#INFO-001)。エンタープライズLLM支出シェア40%で首位。

**$30B ARRに関する注記**: A-1第三者確認済み [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。ただしOpenAI CRO流出メモは実際は$22B（$8B水増し）と主張 [INFO-046](../Information/2026-04-24/collected-raw.md#INFO-046)。PitchBook分析官も「両社のARR報告はBig Four監査を通らない」と指摘 [INFO-045](../Information/2026-04-24/collected-raw.md#INFO-045)。SEC提出書類・監査報告書による検証は未確認。$30B vs $22B乖離が未解決。

**Amazon提携拡大**（2026年4月20日）: 最大5GWのTrainium計算能力確保（Trainium2 Q2 + Trainium3年末）。10年間$100B以上のAWS投資コミットメント。Amazonが$5B即時投資＋最大$20B追加（合計最大$33B投資）。100,000+顧客がBedrockでClaude利用 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。

**インフラ**: Google/Broadcomと複数GW規模の次世代TPU計算能力契約（2027年稼働予定）。AWS Trainium、Google TPU、NVIDIA GPUの3プラットフォームで稼働。

**Claude Opus 4.7**（2026年4月16日GA）: CursorBench 70%。XBOW visual-acuity 98.5%。高解像度画像対応（最大3.75MP、従来比3倍以上）。Cyber Verification Program新設。BenchLM 94/100 (#3) [INFO-035](../Information/2026-04-22/collected-raw.md#INFO-035)。BenchLMファクチュアリティ: Opus 4.7 46.9% (#2) [INFO-024](../Information/2026-04-24/collected-raw.md#INFO-024)。

**Claude Design**: Opus 4.7搭載ビジュアルデザインツール。Claude Codeへのワンクリックハンドオフがデザイン→実装のワークフローをClaude内に閉じ込める [INFO-004](../Information/2026-04-19/collected-raw.md#INFO-004)。

**Managed Agents**: 2026年4月8日GA到達。フルマネージドエージェントハーネス [INFO-078](../Information/2026-04-10/collected-raw.md#INFO-078)。

**Mythos**: セキュリティ研究特化のフロンティアモデル。**NYTがA-1記事で「世界的警報を引き起こした」と報道**——中央銀行と情報機関が緊急対応に動いた [INFO-050](../Information/2026-04-24/collected-raw.md#INFO-050)。BenchLMファクチュアリティで56.8%（Opus 4.7 46.9%を10pt上回る）[INFO-024](../Information/2026-04-24/collected-raw.md#INFO-024)。**欧州銀行向けMythos提供を計画** [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008)。NSAがPentagon対立にもかかわらず使用中 [INFO-029](../Information/2026-04-22/collected-raw.md#INFO-029)。誰が強力なモデルにアクセスできるかをAnthropicが決定する事態に。Amodeiは5年以内にエントリーレベルホワイトカラーの50%がAIに代替される可能性を警告 [INFO-053](../Information/2026-04-24/collected-raw.md#INFO-053)。

**Agent SDK**: TypeScript v0.2.111-112でOpus 4.7対応。MCP per-tool permission_policy追加 [INFO-015](../Information/2026-04-19/collected-raw.md#INFO-015)。12リリース/週（毎日更新ペース）。1.3K GitHub stars。

**Claude for Financial Services**: S&P Global、FactSet、PitchBook、Morningstar等のデータプロバイダーとMCP統合 [INFO-006](../Information/2026-04-19/collected-raw.md#INFO-006)。

**Enterprise価格シフト**: Claude Enterpriseのシートベース価格設定から**使用量ベース課金に移行**。コンピュート需要急増に対応 [INFO-033](../Information/2026-04-22/collected-raw.md#INFO-033)。

**Claude Code品質低下と回復**（2026年4月23日ポストモーテム）: AnthropicがA-1品質で完全原因究明を公開。3つの独立した問題: (1)3月4日、デフォルト推論努力をhigh→mediumに変更→4月7日修正;(2)3月26日、キャッシュ最適化バグで毎ターン思考履歴を削除→4月10日修正;(3)4月16日、冗長性削減プロンプトでコーディング品質3%低下→4月20日修正 [INFO-069](../Information/2026-04-24/collected-raw.md#INFO-069)。全加入者の使用量制限リセット実施。Opus 4.7がCode Reviewで問題(2)のバグを発見（Opus 4.6は発見不能）——新モデルの品質改善を自ら実証。API・推論レイヤーは無影響。今後: 広範なeval Suite、soak期間、段階的ロールアウト。

**コンピュート不足**: 4月21日に$20/月ProプランからClaude Codeを一時削除、反発後に復帰 [INFO-033](../Information/2026-04-24/collected-raw.md#INFO-033)。計算投資不足で需要に応えられない状況が継続 [INFO-034](../Information/2026-04-24/collected-raw.md#INFO-034)。

**AAR（Automated Alignment Researcher）**: Claudeが自律的アライメント研究者として機能 [INFO-049](../Information/2026-04-22/collected-raw.md#INFO-049)。

**セキュリティ課題**: MCPにクリティカルRCE脆弱性——全SDK（Python/TypeScript/Java/Rust）で検証なしの任意コマンド実行 [INFO-019](../Information/2026-04-24/collected-raw.md#INFO-019) [INFO-044](../Information/2026-04-24/collected-raw.md#INFO-044)。CVSS 9.4。Anthropicは「期待される動作」と回答。CoworkアクティビティがAudit Logs・Compliance API・Data Exportsで捕捉されない [INFO-022](../Information/2026-04-22/collected-raw.md#INFO-022)。

## 何をやろうとしているか

### 安全性でエンタープライスを取る（H-ANT-001、確度52%）

SOC2準拠、Compliance API、ASL-3保護で規制業界を取る戦略。エンタープライズ40%シェアとRampデータ（新規70%がAnthropic選択）は、民間ではこの戦略が機能している証拠。EU AI法完全施行（2026年8月）は追い風。

**垂直統合の加速**: Claude for Financial ServicesでBridgewater、Commonwealth Bank of Australia、AIGが導入 [INFO-006](../Information/2026-04-19/collected-raw.md#INFO-006)。**欧州銀行向けMythos提供計画**は規制金融市場への本格参入 [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008)。

**Mythosがこの仮説に与える影響は二面性がある**。中央銀行が緊急対応するほどの能力は、安全性の重要性を裏付けるCだ。同時に、国家規模のリスク評価を触発するモデルを制御できる企業として、Anthropicの市場的評価が変質した——「安全性ベンダー」から「最も強力なAIの管理者」へ [INFO-050](../Information/2026-04-24/collected-raw.md#INFO-050)。

SCR指定が連邦控訴裁で確定したことで政府市場からの排除が法的に固まった。だが$200M契約キャンセルの全容が明らかになり [INFO-029](../Information/2026-04-24/collected-raw.md#INFO-029) [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068)、**NSAがPentagon対立にもかかわらずMythosを使用**、**裁判所がPentagon禁止を審査中**、**Trump大統領がAnthropic-DoD契約を「可能」** と、政府内部の分裂が顕在化している。AmodeiとWhite Houseの会談は「生産的・建設的」[INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068)。$30B A-1確認は安全性が民間市場で報われている証拠 [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。ただし$22B説 [INFO-046](../Information/2026-04-24/collected-raw.md#INFO-046) が正しければ、成長の見え方が変わる。

確度は52%で維持 [Arbiter v3.59](../state/arbiter-2026-04-24.md)。安全性堅持が政府で罰になり、民間で報われる——この二極化が民間側に傾いている。ただしI蓄積（ARR水増し疑義・compute shortage・MCP RCE・Claude Code一時削除）が今後数ラウンドで重みを増す可能性。

### 開発者ツールで差別化する（H-ANT-002、確度69%）— 全仮説中最高

Claude Code + Bun + Agent SDKの3点セットによる差別化。Managed Agents GAでフルマネージドエージェントインフラが加わり差別化の厚みが増した。Claude Designがデザイン→実装のワークフローに新たな接点を作った。

SWE-bench Verified 80.9%で首位（GPT-5.4 71.7%、Gemini 3.1 Pro 80.6%）。Opus 4.7がCursorBench 70%に到達 [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。

**Claude Codeポストモーテム**（2026年4月23日、A-1品質）は、この仮説に複雑な影響を与える [INFO-069](../Information/2026-04-24/collected-raw.md#INFO-069)。3つの独立した問題を完全特定し全修正済み——透明性とエンジニアリング品質の強いC。特にOpus 4.7が自社のバグを発見した点は、新モデルの品質改善を実証する。だが問題(3)（冗長性削減プロンプト）がOpus 4.7 GA当日に発生したことは、リリース管理の弱さも示す。全加入者の使用量制限リセットは顧客対応の誠実さを示すが、$20 ProプランからのClaude Code一時削除 [INFO-033](../Information/2026-04-24/collected-raw.md#INFO-033) と合わせて、コンピュート不足が開発者体験を圧迫している構造が見える。

確度は69% [Arbiter v3.59](../state/arbiter-2026-04-24.md)。ポストモーテム透明性C vs compute shortage I3件が相殺。KIQ-AGENT-001（チャーン率/NPS）が17ラウンド連続未回答で検証可能性に疑義。

### マルチクラウドで広げる（H-ANT-003、確度7%）

Claudeは3大クラウド全てで利用可能な唯一のフロンティアAIモデル。だが確度は7%に低下。**Amazon提携拡大（5GW Trainium・$100B AWS投資）**でAWS依存がさらに深まった [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。Google/Broadcom TPU契約と合わせてインフラ投資の偏りが一段と強まった。「同等」要件からの乖離拡大。

## 強みと弱み

Anthropicの強みは、エンタープライスでの地位、Claude Codeのコーディング性能、そして逆説的に政府排除が生んだ民間の信頼。LLM支出40%シェア。SWE-bench Verified 80.9%首位。Opus 4.7 CursorBench 70%・XBOW 98.5% [INFO-011](../Information/2026-04-17/collected-raw.md#INFO-011)。3大クラウド全対応。Partner Networkの$100M投資。**$30B ARR A-1確認** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。**Amazon提携拡大（5GW・$100B・100K+Bedrock顧客）** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。**欧州銀行Mythos提供計画**で規制金融市場参入 [INFO-008](../Information/2026-04-22/collected-raw.md#INFO-008)。Claude for Financial Services MCP統合 [INFO-006](../Information/2026-04-19/collected-raw.md#INFO-006)。AAR自律的アライメント研究 [INFO-049](../Information/2026-04-22/collected-raw.md#INFO-049)。Agent SDK MCP per-tool permission [INFO-016](../Information/2026-04-17/collected-raw.md#INFO-016)。**MythosがBenchLM 56.8%でOpus 4.7を10pt上回る**——性能面でも独自位置にある [INFO-024](../Information/2026-04-24/collected-raw.md#INFO-024)。**ポストモーテム完全公開（A-1品質）**で透明性を実証 [INFO-069](../Information/2026-04-24/collected-raw.md#INFO-069)。

弱みは5つの構造的課題。まず政府市場の喪失——SCR指定確定、$200M契約キャンセル、Pentagon供給チェーンリスク指定。ただしNSA使用矛盾・裁判所審査・White House会談・Trump「可能」発言で閉じきっていない [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068)。次に、ARC-AGI-2での性能劣位。Claude Opus 4.5は37%でGPT-5.4 Pro（83.3%）に遠く及ばない。三つ目に、セキュリティとコンプライアンスのギャップ。**MCP RCE Critical脆弱性（全SDK・CVSS 9.4）**に「期待される動作」と回答 [INFO-044](../Information/2026-04-24/collected-raw.md#INFO-044)。Cowork監査ログギャップ [INFO-022](../Information/2026-04-22/collected-raw.md#INFO-022)。四つ目に、**$30B vs $22B ARR乖離**——OpenAI CRO流出メモ [INFO-046](../Information/2026-04-24/collected-raw.md#INFO-046) とPitchBook指摘 [INFO-045](../Information/2026-04-24/collected-raw.md#INFO-045) が完全な第三者検証の必要性を示している。最後に、**コンピュート不足**——ProプランからのClaude Code一時削除 [INFO-033](../Information/2026-04-24/collected-raw.md#INFO-033)、クォータ厳格化 [INFO-034](../Information/2026-04-24/collected-raw.md#INFO-034)、Enterprise使用量課金移行でヘビーユーザーのコスト上昇も顧客離れリスク。

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Claude Code ARR・市場シェア推移 | 開発者ツール戦略の成否 | 愛用率46%首位。SWE-bench 80.9%首位。$1B ARR |
| エンタープライズLLMシェア | 40%を維持するか | 40%首位。新規70%がAnthropic選択 ([IND-008](../config/indicators.json)) |
| Anthropic vs DoD訴訟の行方 | SCR指定の最終的な法的判断 | **多層化**: $200M契約キャンセル全容判明 + NSA矛盾使用 + White House会談 + Trump「可能」 [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| $30B ARRの完全検証 | A-1確認済みだが$22B説が併記される | **A-1確認** [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032)。OpenAI CRO $22B主張 [INFO-046](../Information/2026-04-24/collected-raw.md#INFO-046)。PitchBook懐疑 [INFO-045](../Information/2026-04-24/collected-raw.md#INFO-045) |
| Mythosの国家規模影響 | 中央銀行・情報機関の対応が政策を変えるか | **NYT A-1報道**。中央銀行・情報機関緊急対応 [INFO-050](../Information/2026-04-24/collected-raw.md#INFO-050) |
| コンピュート不足の解消 | Pro削除・クォータ厳格化が成長を阻害するか | 継続中 [INFO-033](../Information/2026-04-24/collected-raw.md#INFO-033) [INFO-034](../Information/2026-04-24/collected-raw.md#INFO-034) |
| MCP RCE脆弱性の対応 | 全SDK影響のCVSS 9.4。業界標準プロトコルの信頼性 | Anthropic「期待される動作」回答 [INFO-044](../Information/2026-04-24/collected-raw.md#INFO-044) |
| Agent SDK安定性 | 12リリース/週が成熟の証か不安定性か | KIQ-AGENT-001未回答継続（17ラウンド） |
| AAR再帰的改善 | AIがAIを改善するループの実効性 | 初期実証 [INFO-049](../Information/2026-04-22/collected-raw.md#INFO-049) |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-24 | **Mythos世界的警報**（NYT A-1・中央銀行・情報機関緊急対応・BenchLM 56.8%）・**ペンタゴン$200M契約キャンセル全容**（7月契約→9月決裂→3月SCR→White House会談）・**Claude Codeポストモーテム完全原因究明**（A-1・3問題全修正）・**$30B vs $22B ARR乖離**（OpenAI CRO流出メモ）・コンピュート不足（Pro一時削除・クォータ厳格化）・MCP RCE Critical（全SDK・CVSS 9.4）を反映して全面書き直し。H-ANT-001 52%・H-ANT-002 69%維持 |
| 2026-04-22 | $30B ARR A-1第三者確認（Penn Mutual AM Bloomberg引用）・Amazon提携拡大（5GW Trainium・$100B AWS投資）・欧州銀行Mythos提供計画・Pentagon/NSA矛盾・裁判所審査・Trump DoD契約「可能」発言・Enterprise使用量課金移行・AAR自律的アライメント研究・Amodei 6-12ヶ月予測を反映して全面書き直し。H-ANT-001 51→52%に更新。政府対立セクションを多層化に対応 |
| 2026-04-19 | Claude Design・Claude for Financial Services MCP統合・Agent SDK 12リリース/週詳細を追加。H-ANT-001 52→51%に更新 |
| 2026-04-17 | 鮮度タイムアウト対応（7日経過）。Claude Opus 4.7 GAを反映して全面書き直し |
| 2026-04-10 | SCR連邦控訴裁敗訴（確定）・$30B ARR自己発表・Managed Agents GAを追加 |
