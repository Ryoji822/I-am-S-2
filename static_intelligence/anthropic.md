# Anthropic

> 最終判断更新: 2026-05-02
> 全体確信度: 高
> 情報非対称性: 中国市場 (DeepSeek/ByteDance) との競合観測は手薄
> 主参照: hypotheses.json#H-ANT-001/002/003, hypotheses.json#H-GOV-001, indicators.json#IND-008/001/013/023/027/030

## 0. 一文要約

我々はAnthropicを、**安全性堅持で民間市場を獲得しながら最大規模の政府AI契約を失った企業**と読んでいる。最大の根拠は2つ。$30B ARR が公式確認され OpenAI の $24B を逆転した可能性 [INFO-043](../Information/2026-05-02/collected-raw.md#INFO-043)、Pentagon の7社契約から「lawful use」条項拒否で除外された事実 [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030)。1社が安全性を捨てて政府契約を取りに行く、White House のガイダンスが「lawful use」を残したまま連邦利用許可を具体化する、もしくは中小AIが同様の収益伸長を出す、のいずれかが観測されたら、この読みは更新が要る。

## 1. コア判断

Anthropic の現在の構図は、**安全性が民間市場では報われ、政府市場では罰される**という二極化に集約される。

民間側の輪郭ははっきりしている。エンタープライズLLM支出シェアで40%首位、新規顧客の70%が Anthropic を選んでいる [INFO-001](../Information/2026-05-02/collected-raw.md#INFO-001)。$30B ARR は2025年末の $9B から3.3倍に伸びた [INFO-043](../Information/2026-05-02/collected-raw.md#INFO-043)。Google が $40B ($350B評価)、Amazon が最大 $25B を投じている [INFO-054](../Information/2026-04-28/collected-raw.md#INFO-054)。SOC 2 Type 2 と ASL-3 を同時に満たす企業がこの規模で他にいないことが、規制業界からの集中流入を支えている。

政府側では逆方向の事実が積み上がる。Pentagon が SpaceX / OpenAI / Google / NVIDIA / Microsoft / AWS / Reflection AI の7社と分類軍事AI契約を結び、Anthropic だけが除外された [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030)。除外の理由は「lawful use」条項、つまり自律型致死兵器と国内大量監視への利用を Anthropic が拒否したことにある。同時報道で、DC回路裁判所が「chilling effect」主張を支持し、White House が連邦利用許可ガイダンスを起草中であることも確認された。法的地位は「排除確定」から「係争中、部分的に有利」に移っている。

ここで読むべきは、二面性そのものではなく、それが普遍化できるかだ。$30B ARR の企業だから政府市場を放棄できる、というだけなら、安全性差別化は中小AIには選択肢にならない。Anthropic1社の例外として終わるか、業界の分岐モデルになるかは、今後の Pentagon 補欠契約と White House ガイダンスの内容次第になる。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | $30B ARR 公式確認、OpenAI $24B を逆転した可能性 | 安全性が民間市場で報われている直接の収益証拠 | A-3 | [INFO-043](../Information/2026-05-02/collected-raw.md#INFO-043) |
| 高 | Pentagon 7社契約での Anthropic 除外、理由は「lawful use」条項拒否 | 政府市場で罰される構造の決定的観測 | A-2 | [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) |
| 高 | Google $40B + Amazon $25B 投資コミット ($350B評価) | コンピュート不足を解く資金。安全性堅持が外部資金で支えられる | A-1 | [INFO-054](../Information/2026-04-28/collected-raw.md#INFO-054) |
| 中 | DC回路裁判所「chilling effect」支持、White House ガイダンス起草中 | 政府圧力に法的歯止めが入り始めている | A-2 | [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) |
| 中 | エンタープライズLLM 40%シェア、新規70%が Anthropic 選択 | 民間市場での集中流入の継続性 | B-2 | [INFO-001](../Information/2026-05-02/collected-raw.md#INFO-001) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| Anthropic が「lawful use」条項を受諾して政府契約に回帰 | コア判断 (民間優先・政府放棄) と H-ANT-001 が同時に崩れる | 90日 | [IND-023](../config/indicators.json) |
| 中小AI企業 (Mistral / Cohere 等) が安全性差別化で同様の収益伸長を達成 | 「$30B規模だから可能」という限定が外れ、安全性差別化の普遍性が立つ | 180日 | [IND-008](../config/indicators.json) |
| Pentagon 補欠契約で Anthropic が「lawful use」のまま採用 | 政府が Anthropic を必要とする実需を認めたことになり、二極化が崩れる | 60日 | [IND-023](../config/indicators.json) |
| White House ガイダンスが「lawful use」要件込みで連邦利用許可を具体化 | 政府市場での部分回帰が起き、二極化が緩和される | 60日 | [IND-023](../config/indicators.json) |
| Claude Code 50万行ソース漏洩から大規模なクローン製品が市場投入 | $2.5B ランレートと開発者ツール差別化 (H-ANT-002) が崩れる | 90日 | [IND-013](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-ANT-001](../config/hypotheses.json) | 安全性差別化でエンタープライズを取る | 52% | 民間で機能 (40%シェア) するが普遍化が未証明。Pentagon 除外で限界も露出 | [INFO-001](../Information/2026-05-02/collected-raw.md#INFO-001) [INFO-043](../Information/2026-05-02/collected-raw.md#INFO-043) | [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) |
| [H-ANT-002](../config/hypotheses.json) | Claude Code + Agent SDK で開発者市場を取る | 65% | $2.5B ランレートと SWE-bench 80.9% 首位は強いが、ソース漏洩・コスト47%増・Pro削除で供給リスクが顕在化 | [INFO-002](../Information/2026-05-02/collected-raw.md#INFO-002) [INFO-069](../Information/2026-04-24/collected-raw.md#INFO-069) | [INFO-049](../Information/2026-05-02/collected-raw.md#INFO-049) [INFO-037](../Information/2026-05-02/collected-raw.md#INFO-037) [INFO-047](../Information/2026-04-28/collected-raw.md#INFO-047) |
| [H-ANT-003](../config/hypotheses.json) | マルチクラウドで広げる | 6% | Amazon $100B + Google $40B で2大クラウド依存が深まり「同等機能」要件と乖離 | (なし) | [INFO-054](../Information/2026-04-28/collected-raw.md#INFO-054) |
| [H-GOV-001](../config/hypotheses.json) | 政府圧力による業界全体の萎縮効果 | 45% | Pentagon 7社契約は萎縮の最も具体的な実証だが、DC裁判所支持と White House 軟化が同時進行で純効果は未確定 | [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) | [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-008](../config/indicators.json) | エンタープライズLLM支出シェア | 35%以上で elevated | 40% (Anthropic首位) | 2026-05-02 |
| [IND-001](../config/indicators.json) | 主要ベンチマークの非連続ジャンプ | +5pt以上/期で high | SWE-bench 80.9%首位、ARC-AGI-2 37% (劣後) | 2026-05-02 |
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 月3件超で high | Claude Code 50万行漏洩、MCP RCE Critical | 2026-05-02 |
| [IND-023](../config/indicators.json) | 政府のAI企業介入 | 直接介入で high | Pentagon 7社契約・除外、DC裁判所支持 | 2026-05-02 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展 | 月80M+DLで high | MCP 110M+/月、全主要プレイヤー対応 | 2026-05-02 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | 同時進行3件で elevated | Pentagon 7社契約で同時進行が顕在化 | 2026-05-02 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-05-02 | コア判断を「政府排除確定」から「民間収益・政府係争・WH軟化の二極化」へ | [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) Pentagon 7社契約と DC裁判所支持の同時報道 | 「政府市場から完全排除された企業」 → 「民間で報われ政府で係争中の企業」 |
| 2026-04-28 | Google $40B 投資と SCR仮差し止めを反映 | [INFO-054](../Information/2026-04-28/collected-raw.md#INFO-054) [INFO-043](../Information/2026-04-28/collected-raw.md#INFO-043) | コンピュート不足が主リスク → $40B で根本解決の道が開く |
| 2026-04-24 | $30B ARR 公式確認、OpenAI 逆転の可能性を初記録 | [INFO-043](../Information/2026-04-28/collected-raw.md#INFO-043) | 「OpenAI に次ぐ規模」 → 「逆転した可能性のある規模」 |
| 2026-04-22 | Amazon 5GW Trainium 提携を反映 | [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032) | コンピュート単独依存 → AWS / Google / NVIDIA 3点供給 |

### 6.1 政府対立の時系列 (Anthropic 固有)

§6 は判断変化の節目に絞っているが、Anthropic の場合は政府対立の **政治的加速度** 自体が判断材料になる。事象の時系列を別表で残す。

| 日付 | 事象 | 参照 |
|:-:|---|---|
| 2025-07 | Pentagon と $200M 契約締結 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2025-09 | GenAI.mil 展開交渉で決裂。DOD「全合法目的での無制限アクセス」要求、Anthropic「自律兵器・国内大量監視への不使用保証」で拒否 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-02-27 | Trump 政権が SCR 指定・連邦使用禁止 | [INFO-048](../Information/2026-03-01/collected-raw.md#INFO-048) |
| 2026-03-05 | DOD が Anthropic を「サプライチェーンリスク」指定 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-03-09 | Anthropic が憲法修正第1条に基づき DoD 提訴 | (社内記録) |
| 2026-04-08 | 連邦控訴裁が一時差し止め請求を棄却。SCR 指定が一時確定。OpenAI が直後に $200M 契約を獲得 | [INFO-035](../Information/2026-04-10/collected-raw.md#INFO-035) |
| 2026-04-中旬 | Pentagon が連邦システムから排除。NSA は Mythos Preview を使用継続 | [INFO-029](../Information/2026-04-22/collected-raw.md#INFO-029) |
| 2026-04-17 | Amodei と White House が「生産的・建設的」会談 | [INFO-068](../Information/2026-04-24/collected-raw.md#INFO-068) |
| 2026-04-20 | Anthropic が Amazon 提携拡大を発表 (5GW Trainium、$100B AWS投資) | [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032) |
| 2026-04-23 | Trump 大統領が「Anthropic-DoD 契約は可能」と発言 | [INFO-029](../Information/2026-04-24/collected-raw.md#INFO-029) |
| 2026-04-24 | 連邦裁判所が SCR 指定の仮差し止めを認可。DC 回路裁判所は政府の控訴延期請求を拒否 | [INFO-043](../Information/2026-04-28/collected-raw.md#INFO-043) |
| 2026-05-01 | Pentagon 7社契約締結、Anthropic 除外。除外理由は「lawful use」条項拒否。DC 回路裁判所「chilling effect」支持。White House がガイダンス起草中。Google 従業員 600+ が CEO に Pentagon 契約拒否を要請 | [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) [INFO-031](../Information/2026-05-02/collected-raw.md#INFO-031) |

時系列で見えるのは、政府圧力が **段階的に強化** (SCR指定 → サプライチェーンリスク → Pentagon 7社契約除外) されつつ、**法的歯止め** (DC 回路裁判所支持) と **政治的軟化** (Trump 発言・White House ガイダンス) が並行しているという構造。直近4週で攻防の頻度が上がっており、判断更新の鮮度を維持する必要がある領域。

## 7. ブラインドスポット

- **Google $40B 投資の影響評価が未定**。14% 持ち分が安全性判断に介入するか、独立性が維持されるかを観測する手段がない。
- **Pentagon 除外期間の機会損失が定量化されていない**。$54B の自律兵器予算が対象だが、条項を受諾していた場合の取り分は推定不能。
- **中国市場での代替動向を追跡できていない**。DeepSeek V4 ($1.74/$3.48 per M tokens) と Claude ($5/$30) の価格差で API シェアが侵食されるシナリオの観測指標を持たない。
- **Claude Code の解約率と新規定着率が不明** (KIQ-AGENT-001、26R連続未回答)。$2.5B ランレートが定着率と新規流入のどちらに支えられているかが見えない。
- **Mythos の政府利用実態が外部から見えない**。NSA使用はリークで、公式声明ではない。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [INFO-030](../Information/2026-05-02/collected-raw.md#INFO-030) | Pentagon 7社契約・除外、DC裁判所支持、WH軟化 |
| [INFO-043](../Information/2026-05-02/collected-raw.md#INFO-043) | $30B ARR 公式確認、OpenAI 逆転可能性 |
| [INFO-054](../Information/2026-04-28/collected-raw.md#INFO-054) | Google $40B コミット、$350B 評価 |
| [INFO-001](../Information/2026-05-02/collected-raw.md#INFO-001) | エンタープライズ40%シェア、新規70% |
| [INFO-002](../Information/2026-05-02/collected-raw.md#INFO-002) | Claude Code $2.5B ランレート |
| [INFO-049](../Information/2026-05-02/collected-raw.md#INFO-049) | Claude Code 50万行ソース漏洩 |
| [INFO-069](../Information/2026-04-24/collected-raw.md#INFO-069) | Claude Code ポストモーテム完全公開 |
| [INFO-037](../Information/2026-05-02/collected-raw.md#INFO-037) | トークナイザー更新でコスト47%増 |
| [INFO-047](../Information/2026-04-28/collected-raw.md#INFO-047) | Claude Code Pro削除、Max限定化 |
| [INFO-044](../Information/2026-04-28/collected-raw.md#INFO-044) | Mythos の NSA使用 |
| [INFO-032](../Information/2026-04-22/collected-raw.md#INFO-032) | Amazon 5GW Trainium 提携 |
| [Arbiter v3.66](../state/arbiter-2026-05-02.md) | 確度評価の完全根拠 (本書から外出し) |
