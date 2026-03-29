# OpenAI

> 最終更新: 2026-03-29
> 確度: 中

史上最大の$120B調達を完了し、評価額は$730Bに到達した。だが収益は$13.1Bで黒字化未達。エンタープライズLLMシェアは27%でAnthropic（40%）に劣後したまま。動画生成Soraを15ヶ月で終了し、競合のSeeDance 2.0とVeoに市場を明け渡した。技術と資金では圧倒的だが、市場では追いついていない。

## この会社は何者か

Sam Altman率いるAI企業。主力はChatGPT、GPT-5.4シリーズ（Pro/mini/nano）、Agents SDK、Frontierプラットフォーム、Codex、Operator（CUA）。

資金力はAI業界最大。$120B調達が完了（評価額$730B）[INFO-006](../Information/2026-03-29/collected-raw.md#INFO-006)。年間収益$13.1B、消費者60%・エンタープライズ40% [INFO-006](../Information/2026-03-29/collected-raw.md#INFO-006)。ChatGPT週間アクティブユーザー9億人。H2 2026にIPOを検討中。従業員は年末までに8,000人に倍増予定。ただし黒字化は未達。

GPT-5.4 ProはARC-AGI-2で83.3%を記録し人間（72.4%）を超えた [INFO-015](../Information/2026-03-08/collected-raw.md#INFO-015)。GPQA Diamond 92.8%。OSWorld-Verified 75.0%。GPT-5.4 miniは$0.75/$4.50で400Kコンテキスト、GPT-5.4 nanoは$0.20/$1.25でサブエージェント最適化 [INFO-026](../Information/2026-03-22/collected-raw.md#INFO-026)。nanoはCodexクオータの30%しか消費しない。

エンタープライズAI利用はYoY 8倍。ただしLLM支出シェアは27%でAnthropic（40%）に逆転されたまま。Rampデータでは34.4%のビジネスがOpenAIに支払っているが、2月にOpenAIは-1.5%（過去最大の月間減少）を記録 [INFO-033](../Information/2026-03-22/collected-raw.md#INFO-033)。

直近の動き: (1) **Sora終了**——2024年12月公開から約15ヶ月で動画生成サービスを終了 [INFO-005](../Information/2026-03-29/collected-raw.md#INFO-005)。競合のByteDance SeeDance 2.0、Google Veoが市場拡大中。Disneyの$1B投資契約（200キャラクターライセンス）の行方が不透明。Fidji Simo CFOは「ビジネス・生産性ユースケースへの再集中」を理由に挙げた。(2) **$120B調達完了**——当初目標$100Bを超過。新規投資家: a16z、D.E. Shaw、MGX、TPG、T. Rowe Price、Microsoft [INFO-006](../Information/2026-03-29/collected-raw.md#INFO-006)。(3) GPT-5.4 mini/nanoリリース。(4) Agents SDK v0.7.2（WebSocket、computer-use GA）。(5) Promptfoo買収（AI評価・レッドチーミング）[INFO-006](../Information/2026-03-18/collected-raw.md#INFO-006)。(6) Codex自律コーディングエージェント。(7) 政府向けAWS提携で機密・非機密の両方をカバー [INFO-023](../Information/2026-03-20/collected-raw.md#INFO-023)。(8) Assistants API 2026年8月26日廃止、Responses APIに一本化。

## 何をやろうとしているか

### 大企業向けAIプラットフォームになる（H-OAI-001、確度64%）

Frontierプラットフォーム（HP、Intuit、Oracle、Uber採用）とResponses API一本化でエンタープライズ基盤を固める。$120Bと$13.1B年間収益が資金基盤。GPT-5.4 mini/nanoの積極的な価格設定（$0.20〜$0.75/M入力）は、サブエージェント層でのコスト競争力を確保する動き。

DoW契約でAnthropic SCR指定の間隙を突き政府市場に参入。AWS提携で機密業務にも拡大 [INFO-023](../Information/2026-03-20/collected-raw.md#INFO-023)。ただしDoW契約後にChatGPTアンインストールが295%急増 [INFO-037](../Information/2026-03-07/collected-raw.md#INFO-037)。Greg Brockman（社長）のMAGA Super PAC $25M寄付も報じられ [INFO-020](../Information/2026-03-20/collected-raw.md#INFO-020)、政府に近づくほど一部ユーザーが離れる構造が見えている。

Sora終了は「ビジネス・生産性ユースケースへの再集中」という戦略的判断として読める。動画生成市場でByteDance・Googleに後れを取ったことを認め、エンタープライズAIに経営資源を集中する選択。

### MCP上に独自実行環境を構築して囲い込む（H-OAI-002、確度59%）

Skills/ShellはMCPに対抗するものではなく、MCP上に構築された独自の上位レイヤー。Skillsはエージェント機能パッケージ（SKILL.mdマニフェスト付き、OpenAI独自形式）。Shellはクラウド実行環境で、Claude Codeのローカル実行と対照的。OpenClaw Skills Registryは5,400超に成長。

Agents SDK v0.7.2はPython月間1470万DL、TypeScript 150万DL [INFO-006](../Information/2026-03-12/collected-raw.md#INFO-006)。GitHub Stars 2,500はClaude SDK（992）の2.5倍。.NET対応も追加。ただしAWS提携（Bedrockへのstateful runtime展開）[INFO-039](../Information/2026-03-07/collected-raw.md#INFO-039) は囲い込みと矛盾する開放的側面でもある。

### AGI/スーパーインテリジェンス（H-OAI-003、確度1%、棄却候補）

Altmanは「2028年早期にASI」と公言 [INFO-106](../Information/2026-03-21/collected-raw.md#INFO-106) するが、$120B調達、8,000人増員、政府契約拡大——経営行動はすべて商業化に向いている。OpenAI Foundationが$1B以上を生命科学・雇用・AIレジリエンスに投資 [INFO-004](../Information/2026-03-29/collected-raw.md#INFO-004) するが、これはAGI研究というより社会的影響緩和とPR施策に近い。言っていることと、やっていることが違う。確度1%で棄却候補。

## 強みと弱み

OpenAIの強みは圧倒的な資金力（$120B、$730B評価額）と多層的なモデルラインナップ。GPT-5.4 Proで人間超えベンチマーク、mini/nanoで低価格帯もカバー。政府向けAWS提携で機密市場に参入。Agents SDKのGitHub Stars 2,500とNPM dependents 124はオープンソースでの訴求力を示す。Promptfoo買収でAI評価能力を内製化。ChatGPT週間アクティブユーザー9億人は圧倒的な消費者リーチ。

弱みは、技術的優位が市場シェアに転換できていない点。エンタープライズ27%はAnthropicの40%に劣後し、Rampデータでも2月に-1.5%と過去最大の月間減少。$13.1B年間収益で黒字化未達。Sora終了は動画生成市場での敗北を意味し、Disney $1B投資契約の行方は不透明。ChatGPTアンインストール295%急増と政治的論争（Brockman MAGA寄付）が消費者ブランドを傷つけている。Assistants API 8月廃止は開発者離れのリスク。GitHub Copilotは2000万ユーザーだが満足度9%——「使っている」と「好んで使っている」の差が大きい。

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| ARC-AGI-2の90%閾値 | AGI転換点指標の鍵。o3で87.5%まで到達 | 83.3%（Pro）/ 87.5%（o3）。あと2.5pt ([IND-001](../config/indicators.json), high approaching) |
| エンタープライズLLMシェア | 27%から回復するか。Rampでの-1.5%減少が続くか | Anthropic首位 ([IND-008](../config/indicators.json), elevated) |
| GPT-5.4 mini/nanoの浸透 | 低価格帯モデルがサブエージェント市場を取るか | $0.20/M入力。Codexクオータ30%消費 |
| Skills/Shell開発者定着 | MCP上の囲い込みレイヤーが受け入れられるか | OpenClaw 5,400+スキル ([IND-015](../config/indicators.json), elevated) |
| Assistants API廃止後の動向 | 8月の強制移行で開発者が残るか離れるか | 8月26日廃止確定 |
| IPO動向 | H2 2026に検討中。公開企業としての透明性要件 | $730B評価額、8,000人増員計画 |
| Sora終了後の動画市場 | ByteDance/Googleが市場を独占するか | SeeDance 2.0、Veoが拡大中 |

## 変更履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-03-29 | $120B調達完了（評価額$730B）、Sora終了を反映。収益$13.1B、ChatGPT週間アクティブユーザー9億人を更新。OpenAI Foundation $1B投資追加。H-OAI-003確度2%→1%に低下 |
| 2026-03-24 | 2週間分統合。GPT-5.4 mini/nano、Agents SDK v0.7.2、Promptfoo買収を追加。H-OAI-001 63%に微増。H-OAI-003 2%棄却候補。評価額$840Bに更新。政府向けAWS提携（機密対応）追加。Rampデータ（OpenAI -1.5%月間減少）追加。8,000人増員・IPO検討。o3 ARC-AGI 87.5%追加。GitHub Copilot 20M/満足度9%データ |
| 2026-03-09 | GPT-5.4 Proリリース（ARC-AGI-2 83.3%）、$110B調達完了 |
| 2026-02-23 | 初版作成
