# OpenAI

> 最終判断更新: 2026-05-06
> 全体確信度: 中
> 主参照: hypotheses.json#H-OAI-001/002/003, indicators.json#IND-001/IND-013/IND-026/IND-027

## 0. 一文要約

我々はOpenAIを、**$852B評価額を資本として使いながら$14Bの年間損失を走らせている企業**と読んでいる。最大の根拠は2つ。$122B調達を完了してAzure・AWS・GCPの全クラウドに展開し、Codex週間ユーザー400万でエンタープライズ浸透を実証した [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)。その一方、LLM支出シェアは27%でAnthropic（40%）に劣後したまま収益$13.1Bに対して損失$14Bが見込まれている [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048)。Microsoft提携解消、あるいは$14B損失が3期連続で続き資本市場の許容が切れる、のいずれかが観測されたら、この読みは更新が要る。

## 1. コア判断

OpenAIの現在の構図は、**スケールの正当性で赤字を走らせる賭け**に集約される。$852B評価額は「現在の利益」ではなく「市場支配を達成した場合の将来キャッシュフロー」への先払いだ。この論理が成り立つには、投資家が損失拡大に耐え続ける間に、エンタープライズ浸透が競合を引き離せるという前提が必要になる。

現時点でその前提を支える事実はある。Codex WAU 400万 [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)、100万ビジネス顧客、ChatGPT週間アクティブユーザー9億人、JV「The Development Company」によるPEパートナーポートフォリオへの直接浸透 [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056)。Microsoft提携の非排他化でAzure・AWS・GCPに同時展開できるようになり、Anthropicが持てなかった全クラウドリーチを確保した [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024)。

ただし、前提が危うい事実も同様に積み上がっている。BenchLM総合でGPT-5.4 Proは92点、Claude Mythos Preview（99点）・Gemini 3.1 Pro（93点）に続く3位で技術首位を失った [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028)。エンタープライズAI本番到達率は業界全体でCisco 85%パイロット/5%本番、D&B 30%本番スケールに留まっており [INFO-034](../Information/2026-05-06/collected-raw.md#INFO-034)、Codex 4M WAUが収益貢献まで到達しているかは確認できていない。賭けが成功するかを判断する客観的指標がまだ出そろっていない。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | $122B調達完了（評価額$852B）。SoftBank・Amazon $50B・Nvidia $30B・Microsoft が主要投資家 | 損失走行を資本で支える構造の基盤。枯渇まで最低2〜3年の余裕がある | A-3 | [INFO-055](../Information/2026-05-06/collected-raw.md#INFO-055) |
| 高 | 収益$13.1B（月$2B）に対して2026年損失見込み$14B | 赤字走行の規模を確定する。収益成長が損失拡大を上回れるかがコア判断の焦点 | B-3 | [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) |
| 高 | Microsoft提携改訂（非排他・全クラウド・IP非排他2032）+ OpenAI on AWS（Bedrock経由）| 単一クラウド依存からの解放。エンタープライズ到達範囲を構造的に拡大 | A-3 | [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) |
| 中 | Codex WAU 400万 + Agents SDK sandboxing + persisted /goal | エンタープライズ浸透の現時点の最良指標。ただし個人/法人比率・ARR換算値は非公開 | A-3 | [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) [INFO-004](../Information/2026-05-06/collected-raw.md#INFO-004) |
| 中 | BenchLM 3位（92点）。GPT-5.4 Pro ARC-AGI-2 83.3%で人間超え（72.4%）だが、Mythos 99点に7点差 | 技術首位喪失は差別化の弱体化。ただしARC-AGI-2の人間超えは具体的数値で計測可能な成果 | A-3 | [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) |
| 中 | JV「The Development Company」設立（TPG/Brookfield/Advent/Bain、評価額$10B・$4B調達・FDEモデル） | エンタープライズ浸透をGSIを通じてではなくPE直接経路で加速する新構造 | B-2 | [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| $14B損失が2026・2027と連続し、Altman or SoftBankが損失許容の打ち止めを示唆 | 「スケールで正当化された赤字走行」のコア判断が崩れ、リストラ/縮小フェーズへの移行が現実化する | 180日 | [IND-029](../config/indicators.json) |
| LLM支出シェアが27%から20%以下に下落（Anthropic・Google双方に侵食される） | H-OAI-001（エンタープライズ支配的地位の確立）が棄却水準に達する | 90日 | [IND-008](../config/indicators.json) |
| Microsoft提携が再度改訂され、AzureへのOpenAI独占が復活 | 全クラウド展開という構造的利点が消え、競合との対称性が回復しなくなる | 60日 | [IND-027](../config/indicators.json) |
| Codex WAUが3四半期連続で横ばい、かつARRへの転換率が非公表のまま | 「エンタープライズ浸透を実証中」という判断の根拠が崩れる（量=質ではないことが顕在化） | 90日 | [IND-026](../config/indicators.json) |
| GPT系モデルがBenchLM/ARC-AGI-2双方でGemini・Claude Mythosから10点以上引き離される | 性能差別化による価格維持が困難になり、DeepSeek価格帯への収束圧力が増す | 180日 | [IND-001](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-OAI-001](../config/hypotheses.json) | 2026年内にAgent機能でB2B支配的地位を確立する | 63% | JV設立・全クラウド展開・Codex 4M WAUでエンタープライズ浸透のCが積み上がるが、$14B損失とLLMシェア27%で収益構造不安定化のIも同数。C/I均衡が確度を中央付近に固定している | [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) | [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) |
| [H-OAI-002](../config/hypotheses.json) | MCP開放エコシステムの上にプロプライエタリ上位レイヤーを構築して囲い込む | 53% | 囲い込み戦略に対して Symphony OSS・Microsoft IP非排他2032・AAIF/MCP標準化の3件A-3独立反証が継続中。JVのPEポートフォリオへの優先販売アクセスは「金融次元の囲い込み」として未評価のCだが、下層開放の蓄積が上層を制約する構造は崩れていない | [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) | [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) [INFO-004](../Information/2026-05-06/collected-raw.md#INFO-004) |
| [H-OAI-003](../config/hypotheses.json) | AGI/スーパーインテリジェンスを最優先目標とし商業化と並行して大規模資源投入する（棄却候補） | 1% | $122B調達・JV $10B・8000人増員・Codex Labs・GSI 7社提携という経営行動がすべて商業化に向いており、AGI研究優先を示す行動証拠がない。Altman の「2028年早期ASI」発言は公言だが、発言と経営配分の方向が逆なのでCの価値がない | (なし) | [INFO-055](../Information/2026-05-06/collected-raw.md#INFO-055) [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-001](../config/indicators.json) | 主要ベンチマーク性能の非連続ジャンプ | +5pt以上/期で high | BenchLM 92点（3位）。ARC-AGI-2 83.3%（人間超え）。90%閾値まで約2.5pt | 2026-05-06 |
| [IND-013](../config/indicators.json) | AIエージェント関連セキュリティ侵害頻度 | 大規模インシデントで critical | AIエージェント本番DB削除 (INFO-009)。24.4%のみAI完全可視性。MCP Shadow IT継続。high水準 | 2026-05-06 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 3+独立ソースが<10%本番到達でhigh | D&B 30%本番スケール。パイロット→本番18%。elevated（Cisco 5%・Fortune <10%で2/3条件充足） | 2026-05-06 |
| [IND-027](../config/indicators.json) | MCP等オープンスタンダードの業界採用率 | 全主要プレイヤー採用でhigh | MCP全社サポート（OpenAI/Google/Microsoft/Block）。Red Hat MCP Gateway。Visual Studio統合。high水準 | 2026-05-06 |
| [IND-029](../config/indicators.json) | AIインフラ資本投入 vs 物理制約 | 資本流入が物理制約を上回り続ける限りhigh | 3社合算CapEx ~$560B。資本流入vs物理的制約ギャップ継続。high水準 | 2026-05-06 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-06 | コア判断を「エンタープライズ開発プラットフォーム化」から「スケールで正当化された赤字走行の賭け」へ改訂 | $14B損失見込み [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) + JV設立 [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) + BenchLM 3位 [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) の同時観測 | 「全クラウド展開でエンタープライズを取る企業」 → 「評価額で損失を走らせながら市場支配を狙う企業」 |
| 2026-04-29 | Microsoft提携改訂・OpenAI on AWSを反映、全クラウド展開の構造変化を記録 | [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) Microsoft提携非排他化 + Bedrock展開 | 「Azure依存・単一クラウドリスク」 → 「全クラウド対称展開」 |
| 2026-04-22 | Codex Labs + GSI 7社提携、Codex WAU 3M→4Mを反映 | Codex Labs発表 + Accenture/PwC/Capgemini等7社提携 | 「API提供中心のB2Bチャネル」 → 「GSI経由のB2B営業力借用」 |
| 2026-04-07 | $122B調達完了を反映、資本余力の評価を更新 | [INFO-055](../Information/2026-05-06/collected-raw.md#INFO-055) $122B調達完了・評価額$852B | 「資金調達中、不確定」 → 「調達完了、最低2〜3年の資本余力確保」 |

## 7. ブラインドスポット

- **Codex WAUの収益転換率が非公表**。400万WAUが月次ARRにいくら寄与しているかを外部から追跡できない。ChatGPT 9億WAUとCodex 4M WAUは桁が2つ違うが、それぞれの収益貢献比率も不明で、どちらが$13.1B収益を支えているかが見えない。
- **$14B損失の補填構造が透明でない**。$122B調達のどの部分が損失補填に充当され、どの部分がCapExに向かっているか開示がない。Microsoft・SoftBankが損失補填に合意しているのか、単なる資本参加なのかで、許容期間の試算が変わる。
- **JV「The Development Company」の実効性が未観測**。PEパートナーのポートフォリオ企業へのOpenAI製品浸透が実際にH-OAI-001を強化するか、FDEモデルがスケールするかは、設立から6ヶ月以上のデータがないと判断不能。
- **ChatGPT・Codexの解約率とリテンションが公表されていない**。9億WAU・100万ビジネス顧客はグロス数値。ネット維持率と有料転換率が不明なまま成長ストーリーに依存している。
- **AGI進捗の内部評価が外部から測れない**。ARC-AGI-2でGPT-5.4 Proが83.3%を達成したが、ARC-AGI-3ではフロンティアモデルがほぼ0%。Altmanの「2028年ASI」発言と客観ベンチマークの乖離が最大水準にある (IND-028 elevated) ため、OpenAI内部のAGI定義と外部評価の差分が判断の死角になっている。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-024](../Information/2026-05-06/collected-raw.md#INFO-024) | Microsoft提携改訂（非排他・全クラウド）、OpenAI on AWS、Codex WAU 4M+ |
| [INFO-048](../Information/2026-05-06/collected-raw.md#INFO-048) | 2026年損失見込み$14B |
| [INFO-055](../Information/2026-05-06/collected-raw.md#INFO-055) | $122B調達完了、評価額$852B |
| [INFO-056](../Information/2026-05-06/collected-raw.md#INFO-056) | JV「The Development Company」設立（TPG/Brookfield/Advent/Bain・$10B・FDEモデル） |
| [INFO-028](../Information/2026-05-06/collected-raw.md#INFO-028) | BenchLM 3位（92点）、GPT-5.4 Pro ARC-AGI-2 83.3%・人間超え |
| [INFO-004](../Information/2026-05-06/collected-raw.md#INFO-004) | Agents SDK sandboxing + persisted /goal |
| [INFO-034](../Information/2026-05-06/collected-raw.md#INFO-034) | D&B 97%活動・30%本番スケール（エンタープライズ実行ギャップ） |
| [INFO-035](../Information/2026-05-06/collected-raw.md#INFO-035) | パイロット→本番18%（業界エージェント実行ギャップ） |
| [INFO-009](../Information/2026-05-06/collected-raw.md#INFO-009) | AIエージェント本番DB削除事案 |
| [Arbiter v3.70](../state/arbiter-2026-05-06.md) | H-OAI-001/002/003確度評価の完全根拠（本書から外出し） |
