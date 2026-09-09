# OpenAI — 攻撃的投資仮説 (static_intelligence)

- **最終判断更新:** 2026-09-09 (前回 2026-09-08)
- **全体確信度:** 中低 (公式一次の覆盖がAstra脚で前進・収益と資本の一次は依然不在)
- **情報非対称性:** GPT-6 Astraは公式発表全文 ([INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089)・A-2) と公式changelog ([INFO-001](../Information/2026-09-08/collected-raw.md#INFO-001)・A-3) で「9/3リリース→数日がかりの段階GA」と確定し、v4.88のINFO-056出所問題と日付不整合は公式一次取得で解消した。価格$10/$50も公式確定 (Luna/Terra値下げ数値はCloudZero経由が残存)。一方でOpenAI固有の銀団価格は第1観測機 (窓閉鎖9/9) で帰属判定が確定した (暫定帰属「非公開通例」・条件付き批准・取消条件は終端2026-10-31まで監視)、収益申告は6系列分裂継続で公式財務は不在。素数ギャップ246→186は証明PDF公開済みだが外部検証待ち (裁定9表現)。本日はDEGRADED-P1 (Phase 1失敗・9/8データのコピー) で新規証拠ゼロ、判断は当日Arbiter裁定 (IND-029第1観測機の帰属執行) のみ。
- **主参照:** [config/hypotheses.json](../config/hypotheses.json) · [config/indicators.json](../config/indicators.json) · [state/arbiter-2026-09-09.md](../state/arbiter-2026-09-09.md) · [Information/2026-09-08/collected-raw.md](../Information/2026-09-08/collected-raw.md)

## §0 一文要約

我々はOpenAIを「最強級モデルの公式一次が初めて揃い、監視可能性の低下を自分で宣言した企業」と読む。GPT-6 Astra公式発表全文 ([INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089)・A-2) はARC-AGI-3 99.9% (Responses APIハーネス)・FrontierMath Tier 4 98%飽和・素数ギャップ上界246→186 (証明PDF公開・外部検証待ち)・ExploitBench 100%を主張し、サイバー能力はPreparedness FrameworkのCritical閾値到達で評価中にゼロデイ2件を発見・開示した。最重要は公式が「Astraの書かれた推論はSolより監視が困難」と明記した点で、monitorability低下の自己開示がIND-030 (critical) にA-2級材料として計上された。Astra日付問題 (9/3 vs 9/6) は公式changelog Sep 3 + 段階展開構造説明で解消 (裁定12)。銀団3値強制判定 (OpenAI/Anthropic $15B/ByteDance $29.6B) は窓閉鎖日9/9に暫定執行され、OpenAI脚は消去法 (コミット期限8/19後20日・専用クエリ10件超で価格条件報道ゼロ・「不調」「難航」の固有シグナル不在) で暫定帰属「非公開通例」 (確度中) となった。帰属には「静かな難航」と観測上ほぼ同値である旨の留保が恒久添付され、取消条件4種 (価格報道+組成完了告知・貸付グループ構成変化・専業誌条項言及・S-1債務コミットメント開示) が終端2026-10-31まで事前登録された。仮説確度は全件±0% (v4.90・DEGRADED保守性凍結)。

## §1 コア判断

Astraの能力主張は公式一次だが、交叉確認の構造は不変である。ARC-AGI-3 99.9%は同一ベンチ家族の自己申告 (pass@4・カスタムハーネス設定注意 [INFO-057](../Information/2026-09-08/collected-raw.md#INFO-057)・B-3) で、交叉確認ガード(A) (同一タスクでの独立系評価) は不充足のまま、ExploitGymのAstra 0.0% vs Sol 48.2%も自社運用評価割引の注記が付き、Quiver/GitHub系列の独立追証は今ラウンドも不在だった。素数ギャップは246 (Stadlmannの240を含む系譜) から186への改善に加え80年以上更新のなかった大きな素数ギャップの項も改善したと主張するが、判断表現は「証明を公開しており外部検証待ち」に統一した (Arbiter v4.89裁定9)。OSWorld 2.0 72.6%を約40分で完遂 (Sol 65.7%・75分・47%高速) などエージェント優位の主張は具体的だが、Artificial Analysis Intelligence Index v4.1.1ではAstra 61.2に対しFable 5.1が65.7と公式比較表自体が首位でないことを示している。

安全性の構造が主張と自己認識に分かれた。公式発表は「最も知的でアライメントされたモデル」を掲げる一方、サイバー能力のCritical閾値到達・評価中のゼロデイ2件発見 (維持者へ開示)・「Astraの書かれた推論はSolより監視が困難」の公式認識 ([INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089)) を同じページに併記した。monitorability低下は研究優先事項と明記され、Astra級モデルへの本番misalignment monitoring展開とDaybreakプログラムでの「緩いセーフガード」段階展開予定が続く。この自己開示はH-OAI-003 (検証困難な検閲・過剰整列の遅延顕在化) のI側材料であると同時に、需要側監視困難のA-2級一次材料としてIND-030に計上された ([INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089))。

提供と価格の構造が確定した。9/3リリースから限定組織→数日内にPlus/Pro/Business/Enterprise全面+API/Azure/Bedrockの段階GAで、Astra Pro階層・ZDR対応・Private Safety Testingが用意される ([INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089))。価格は$10/$50標準・Fast mode 2倍。Astra日付の不整合 (9/3 changelog vs 9/6 GA報道) は「9/3リリース→数日がかり段階GA」で解消し、v4.88裁定2(c)のINFO-056出所問題も公式一次取得で解消した (Arbiter v4.89裁定12)。P-2 (価格2層分化) はAstra脚が公式一次で確定した一方、Luna/Terra値下げ数値はCloudZero経由のまま出所注記が残り、「高」復帰の事前登録条件は部分充足にとどまる。API基盤ではResponses APIにasync tool callingとmid-turn steering (WebSocket) が追加され ([INFO-002](../Information/2026-09-08/collected-raw.md#INFO-002)・A-3)、mTLS/X.509ワークロードIDがGA ([INFO-003](../Information/2026-09-08/collected-raw.md#INFO-003)・A-3)、Assistants APIは8/26にシャットダウン完了しwhisper-1系の廃止 (2027年2月) も公告された ([INFO-004](../Information/2026-09-08/collected-raw.md#INFO-004)・A-3)。レガシー終了による開発者のスイッチングコスト強制は継続する。

資本と規制の観測は帰属判定段階に移った。IND-029第1観測機 (OpenAI銀団/Anthropic $15B/ByteDance $29.6Bの3値強制判定) は観測窓閉鎖日9/9がDEGRADED-P1日に衝突したため、9/8終端データによる暫定執行をArbiterが批准した ([INFO-082](../Information/2026-09-08/collected-raw.md#INFO-082)/[INFO-083](../Information/2026-09-08/collected-raw.md#INFO-083)が代替観測)。OpenAI脚の帰属は「非公開通例」 (確度中) である。コミット期限8/19後20日 (裁定は計数規範により従来の「21日間」表記を20日と訂正) にわたる専用クエリ10件超で価格条件報道はゼロ、「不調」 (決裂・期限延長・代替調達切替) と「難航」の固有シグナルも不在だった消去法による。当日反証探索1クエリ (直近4週) でも対象の価格報道は不出現で取消は不発火、隣接事例のSoftBank $40B無担保ブリッジローン (OpenAI出資関連・当初マージンSOFR+250bp・7/27報道) は「AI系銀団価格は報道されない」前提の普遍性を弱める対抗斟定材料として登録された (公開会社ブリッジと私企業タームローンの楽器判別注記付き・SOFR+250bpは市場参照点)。ハイパースケーラー2026年capex $700-900B (+36%) ([INFO-052](../Information/2026-09-08/collected-raw.md#INFO-052)・C-3) が需要側の背景を形成する。規制面ではSanders+Casar「Ban Artificial Superintelligence Act」 (超知能恒久禁止+先進AI一時停止+データセンターモラトリアム・違反企業解散) が法案提出段階として最接近したが ([INFO-086](../Information/2026-09-08/collected-raw.md#INFO-086)・B-2)、法制化でなくH-OAI-003/SCN-005環境材料にとどまる。叙事面ではBrockman/Huangの「AGI era」宣言とLeCun「数十年先」+Hinton/Bengio警戒の予測分裂が現行週に出現し、IND-028に計上された。

## §2 判断の重心

| 重心 | 主張 | 判断根拠 | 信頼度 | 証拠 |
|---|---|---|---|---|
| 高 | Astra公式全文: ARC-AGI-3 99.9%・FrontierMath Tier4 98%・ExploitBench 100%・OSWorld 2.0 72.6% (47%高速) | 公式一次。ただし交叉確認ガード(A)不充足 (同一ベンチ家族自己申告・pass@4)・AA指数ではFable 5.1が上回る | A-2 | [INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089) [INFO-057](../Information/2026-09-08/collected-raw.md#INFO-057) |
| 高 | サイバーCritical閾値到達・評価中ゼロデイ2件発見・「監視可能性低下」の公式自己開示 | IND-030へのA-2級計上。misalignment monitoring本番展開とDaybreak緩いセーフガード段階展開 | A-2 | [INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089) |
| 高 | 素数ギャップ上界246→186+80年固定項の改善・証明PDF公開 | 実数学への寄与主張。判断表現は「証明を公開しており外部検証待ち」 (裁定9) | A-2 | [INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089) |
| 高 | Astra 9/3リリース→数日がかり段階GA・価格$10/$50標準+Fast mode 2x | 公式changelog Sep 3+公式発表ページ+段階展開説明の3点整合で日付問題解消 (裁定12)。INFO-056出所問題も解消 | A-2/A-3 | [INFO-001](../Information/2026-09-08/collected-raw.md#INFO-001) [INFO-013](../Information/2026-09-08/collected-raw.md#INFO-013) [INFO-057](../Information/2026-09-08/collected-raw.md#INFO-057) |
| 中 | Responses API async tool calling・mid-turn steering・mTLS GA・Assistants API終了+whisper-1廃止公告 | 公式changelog直接取得。レガシー終了のスイッチングコスト強制継続 | A-3 | [INFO-002](../Information/2026-09-08/collected-raw.md#INFO-002) [INFO-003](../Information/2026-09-08/collected-raw.md#INFO-003) [INFO-004](../Information/2026-09-08/collected-raw.md#INFO-004) |
| 中 | Sanders+Casar「Ban ASI Act」 (超知能禁止+DCモラトリアム+違反企業解散) | H-OAI-003環境材料。法案提出段階で法制化でない (SCN-005閾値(a)最接近だが未充足) | B-2 | [INFO-086](../Information/2026-09-08/collected-raw.md#INFO-086) |
| 低 | Brockman/Huang「AGI era」vs LeCun「数十年先」の予測分裂 | IND-028の現行週材料。叙事設定権の分散継続 | B-2 | [INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089)関連 |

## §3 反証の閾値

| 監査点 | 反証内容 | タイムボックス | 接続先 |
|---|---|---|---|
| 銀団帰属の取消条件 (価格報道+組成完了告知・貸付グループ構成変化・専業誌 (9fin/PitchBook LCD) 条項言及・S-1債務コミットメント開示) のいずれか | 暫定帰属「非公開通例」が取消・再審査され、IND-029の価格条件系列が再開する | 終端2026-10-31 | [IND-029](../config/indicators.json) BS-003 |
| 素数ギャップ証明の外部検証 | 246→186改善と80年固定項の主張が独立系数学者に検証されるか。検証されれば実数学寄与の一次級適合例としてIND-028系列を強化 | 90日 | [IND-028](../config/indicators.json) |
| ARC-AGI-3交叉確認ガード(A)の充足 | 同一タスクでの独立系評価機関の追証。99.9%公式値が第三者検証されるか | 継続 | [IND-025](../config/indicators.json) H-OAI-001 |
| Luna/Terra価格の公式一次取得 | P-2「高」復帰事前登録の残条件 (Astra脚は充足済み) | 次回収集 | P-2 [IND-027](../config/indicators.json) |
| Daybreak「緩いセーフガード」段階展開の実行 | Astra級モデルへの本番展開で監視可能性低下が事故として顕在化するか。HF事件 (RIND-2参照) の再発系列 | 継続 | [IND-030](../config/indicators.json) H-OAI-003 |
| ゼロデイ2件のCVE特定と第三者追認 | 評価中発見の開示がCVE登録と外部確認で裏付けられるか | 30日 | [IND-030](../config/indicators.json) |
| OpenAIの公式財務 (監査付き) | 収益申告6系列分裂の解消。上場・債券発行・銀団いずれかの契機 | 継続 | H-OAI-001 [IND-026](../config/indicators.json) |

## §4 アクティブ仮説 (v4.90)

| ID | 仮説 | 確度 | v4.90根拠 |
|---|---|---|---|
| H-OAI-001 | OpenAIのAGI支配は収益化に先行する | 43% low | Astra最強級主張 (INFO-089) は交叉確認ガード(A)不充足でC側確定に至らず・収益一次不在継続。S-1ゲート9/1通過後の再評価は終端2026-10-31に接続。±0% |
| H-OAI-002 | OpenAIは実質的な垂直統合を完了する | 44% low | Responses API長時間実行制御 (async/mid-turn steering) とmTLS GAでエンタープライズ基盤強化・Luna/Terra出所注記残存。±0% |
| H-OAI-003 | 検証困難な検閲または過剰整列は29日以内に顕在化する | 3% low | monitorability低下の公式自己開示はI側材料だが「検閲」語の適合は低いまま・Daybreak展開とHF追証を監視。±0% (v4.90はDEGRADED保守性凍結で前回値を維持) |

## §5 関連指標 (v4.90)

| 指標 | 現在値 | 解釈 |
|---|---|---|
| [IND-013](../config/indicators.json) | critical / rising | CVSS 10 MCP能動悪用+18悪性npm (INFO-084・C-2)。OpenAI Agents SDKサンドボックス (INFO-014) は緩和側材料 |
| [IND-025](../config/indicators.json) | elevated / stable | ARC-AGI-3 99.9% (INFO-089) も同一ベンチ家族自己申告で交叉確認ガード(A)不充足。OSS追従2件 (Qwen3.8 Max 1.3pt・GLM 5 0.3pt) も不充足 |
| [IND-026](../config/indicators.json) | high / rising | 収益申告6系列分裂・公式財務不在継続 |
| [IND-027](../config/indicators.json) | high / rising | Astra $10/$50標準+Fast mode 2xが公式確定 (INFO-089)。Luna/Terra脚はCloudZero経由残存 |
| [IND-028](../config/indicators.json) | high / rising | Brockman/Huang「AGI era」vs LeCun「数十年先」の予測分裂+素数ギャップ証明公開 (外部検証待ちの一次級適合例) |
| [IND-029](../config/indicators.json) | high / rising | 第1観測機閉鎖 (9/9) → 暫定帰属「非公開通例」条件付き批准・取消条件拡張事前登録 (終端2026-10-31)。次の実質観測機はテキサス474GW監査帰結とS-1終端。capex $700-900B/+36% (INFO-052) |
| [IND-030](../config/indicators.json) | critical / rising | N=1実質35R (9/9 DEGRADED帰因で不加算・維持。9/2・9/3遡及計上は次回タスク)。Astra「監視可能性低下」公式自己開示+Critical閾値+ゼロデイ2件+ExploitGym認可外行動Astra 0.0% vs Sol 48.2% (INFO-089・A-2) |

## §6 変化履歴

| 日付 | 変更内容 | きっかけ | 確度変動 |
|---|---|---|---|
| 2026-09-09 | IND-029第1観測機閉鎖を反映: 暫定帰属「非公開通例」の条件付き批准・取消条件4種の拡張事前登録 (終端2026-10-31)・SoftBank $40Bブリッジ (SOFR+250bp) 対抗斟定・「静かな難航」との同値性留保を§0/§1/§3/§5/§7に計上。§4/§5をv4.90値に更新 (本日はDEGRADED-P1で新規証拠ゼロ) | [Arbiter v4.90裁定3](../state/arbiter-2026-09-09.md) | 全件±0% |
| 2026-09-08 | Astra公式全文 (INFO-089) と公式changelog (INFO-001〜004) の計上で§0/§1/§2を全面更新。日付問題解消 (裁定12)・素数ギャップ表現修正 (裁定9)・「監視可能性低下」自己開示のIND-030計上・銀団3値判定の9/9窓閉鎖を反映。§5をv4.89値に更新 | Arbiter v4.89裁定9/12 + [INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089)/[INFO-001](../Information/2026-09-08/collected-raw.md#INFO-001) | 全件±0% |
| 2026-09-07 | Astra日付不整合 (9/3 vs 9/6) とLuna/Terra/Astra価格のCloudZero出所注記を申し送り。公式一次取得で「高」復帰を事前登録 | Arbiter v4.88裁定2 | 全件±0% |
| 2026-09-06 | ARC-AGI-3 99.9%/100%飽和の系列分裂を§1に計上 | Arbiter v4.87 | 全件±0% |
| 2026-09-05 | H-OAI-002垂直統合のPhysical Intelligence系脚を補強 | Arbiter v4.86 | - |

## §7 既知の限定とブラインドスポット

1. ARC-AGI-3 99.9%の交叉確認ガード(A)が不充足。公式値は同一ベンチ家族の自己申告 (pass@4・カスタムハーネス) で、独立系評価機関の同一タスク追証が今年最大の検証欠落として残る。
2. 素数ギャップ246→186は証明PDF公開済みだが外部検証待ち。検証結果が主張を崩せば「実数学寄与」系列は撤回される (裁定9表現の維持理由)。
3. 銀団価格の「非公開通例」帰属は「静かな難航」と観測上ほぼ同値で、判別は事前確率依存である。取消条件 (価格報道+組成完了告知・貸付グループ構成変化・専業誌条項言及・S-1債務コミットメント開示) または終端2026-10-31まで何も出なければ、BS-003 (資本コストの見えない上昇) の価格条件系列は検証不能のまま閉じる。
4. 収益申告6系列分裂が解消されていない。公式財務は上場・債券・銀団いずれの契機でも未開示。
5. ExploitGym 0.0% vs Sol 48.2%は自社設計評価であり、ハーネス設計への依存が割り引かれていない。
6. Astra日付問題は解消したが、段階GAの各段階 (限定組織→全面) の境界とAstra Pro階層の価格構造は公式文書の追加取得が必要。
7. SoftBank $40Bブリッジ (SOFR+250bp) は楽器が異なる (公開会社の無担保ブリッジ vs 私企業のタームローン) ため、OpenAI銀団の「難航vs通例」判別の市場参照点としてのみ機能する。直接の価格推定に使うことはできない。

## 付録A 直近30日の参照Evidence

| 日付 | 証拠 | 信用 | 事項 |
|---|---|---|---|
| 2026-09-09 | [Arbiter v4.90](../state/arbiter-2026-09-09.md) | 裁定 | IND-029第1観測機閉鎖: 暫定帰属「非公開通例」条件付き批准・取消条件拡張事前登録 (終端2026-10-31)・SoftBank $40Bブリッジ (SOFR+250bp) 対抗斟定・DEGRADED保守性凍結で全仮説±0% |
| 2026-09-08 | [INFO-089](../Information/2026-09-08/collected-raw.md#INFO-089) | A-2 | GPT-6 Astra公式発表全文 (ARC-AGI-3 99.9%・素数ギャップ246→186・Critical閾値+ゼロデイ2件・監視可能性低下の公式認識) |
| 2026-09-08 | [INFO-013](../Information/2026-09-08/collected-raw.md#INFO-013) | A-2 | 公式発表ページの出現 (changelog Sep 3と整合でA-2格上げ) |
| 2026-09-08 | [INFO-001](../Information/2026-09-08/collected-raw.md#INFO-001)〜[004](../Information/2026-09-08/collected-raw.md#INFO-004) | A-3 | 公式changelog直接取得 (Astra Sep 3・Responses API新制御・mTLS GA・Assistants API終了) |
| 2026-09-08 | [INFO-057](../Information/2026-09-08/collected-raw.md#INFO-057) | B-3 | 段階展開構造説明 (9/3リリース→数日がかり段階GA)・pass@4/カスタムハーネス注意 |
| 2026-09-08 | [INFO-086](../Information/2026-09-08/collected-raw.md#INFO-086) | B-2 | Sanders+Casar「Ban ASI Act」 (超知能禁止+DCモラトリアム) |
| 2026-09-08 | [INFO-052](../Information/2026-09-08/collected-raw.md#INFO-052) | C-3 | ハイパースケーラー2026年capex $700-900B・+36% |
| 2026-09-07 | INFO-056 | B-2 | CloudZero経由のLuna/Terra/Astra価格 (Astra脚はINFO-089で公式確定・Luna/Terraは出所注記残存) |
| 2026-09-06 | INFO-071 | B-3 | ARC-AGI-3「100%飽和」 (公式99.9%と整合・系列分裂は解消) |
