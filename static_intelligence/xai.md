# xAI → SpaceXAI

> 最終判断更新: 2026-09-05
> 全体確信度: 測定不能（[H-XAI-004](../config/hypotheses.json) indeterminate維持）
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。SpaceXのCursor（Anysphere）$60bn全株式買収が2026-08-14に発効済み（[INFO-098](../Information/2026-08-15/collected-raw.md#INFO-098) B-1）。買収完了後のCursorモデルルーティング・F500解約率・維持率は未公開のままで、Grok Bot（9/4発表・[INFO-005](../Information/2026-09-05/collected-raw.md#INFO-005) A-1）の配布・販売がCursorチャネル（api2.cursor.sh・cursor.com）経由であることだけが動作確認済みである。ダウンロード数・利用量・Bot稼働数は一切公開されない。エンタープライズ採用定量データ（WAU/DAU・F500導入率・Grok固有の企業契約数）は57R以上連続完全不在（v4.72観測不能負債台帳「発効以来データゼロ」登録から継続）。DL/API呼び出し量の時系列データは途絶状態。KIQ-MIL-001は66R/67R連続不在。Grok Gov Modelのガードレール内容も非公開。Grok 4.6のLMSpeed・Vision Arenaスコアは依然未公開（9月AA指数60・[INFO-032](../Information/2026-09-05/collected-raw.md#INFO-032) B-1）。H-XAI-004 indeterminate/52% ±0%・H-XAI-002 58% low（ともにv4.86）
> 主参照: [H-XAI-001](../config/hypotheses.json) [H-XAI-002](../config/hypotheses.json) [H-XAI-003](../config/hypotheses.json) [H-XAI-004](../config/hypotheses.json) [IND-013](../config/indicators.json) [IND-025](../config/indicators.json) [IND-026](../config/indicators.json) [IND-027](../config/indicators.json) [IND-028](../config/indicators.json) [IND-029](../config/indicators.json) [IND-030](../config/indicators.json)

## 0. 一文要約

我々はxAIを「Cursor買収の流通チャネル統合が実行段階に入った一方、Grok固有の採用定量証拠が依然として欠落したままの企業」と読んでいる。Grok Bot（9/4発表・[INFO-005](../Information/2026-09-05/collected-raw.md#INFO-005) A-1）は専用コンピュータを持ちツールにサインインして24/7稼働する常駐型AIチームメイトで、ダウンロード配布がapi2.cursor.sh経由、販売窓口がcursor.comである。SpaceX-Cursor買収（8/14発効）が想定した配チャネル統合の最初の動作確認である。H-XAI-004 52% indeterminateは±0%維持で、v4.86はGrok Botを汎用基盤命題への最強級Cと評価しつつ、本日増分がC-only（確証バイアス警告）であることを明記した。

観測窓（8/28開始）は初期段階である。ルーティング・解約率・維持率の窓内定量が出るまで不定構造は変わらない。並行してOpenAIがCursorのGPTアクセスを遮断したとの報道（[INFO-046](../Information/2026-09-05/collected-raw.md#INFO-046) C-2）は、Cursorのモデル選択肢がGrok方向に狭まる可能性を示し、ルーティング観測の解像度を上げる。政府面ではGenAI.mil拡大（170万→300万人）でGrok for GovernmentがOpenAIと並ぶ最大$200M契約を得て（[INFO-018](../Information/2026-09-05/collected-raw.md#INFO-018) B-2）、Anthropic除外の順応報酬構造の受益側に位置した。X Ads MCPの指定クライアントにGrokが選ばれた（[INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025) B-2）。Grok 4.6 API（8/29）とgrok-build公開（[INFO-006](../Information/2026-09-05/collected-raw.md#INFO-006) A-2）で配給層の整備は続くが、9月AA指数ではGrok 4.6は60でSolより1ポイント下（[INFO-032](../Information/2026-09-05/collected-raw.md#INFO-032) B-1）、フロンティア首位群（Fable 5.1 66・Astra 61）には及ばない。

## 1. コア判断

全体確信度は測定不能に置く。エンタープライズ採用の定量データが57R以上連続で完全に不在だからである。この不在を「不採用の証拠」と断定することも「戦略的非公開」と charitable に解釈することもできない。判断の軸は3本である。Cursorチャネル統合の実行確認、政府調達での受益側固定、そして配給整備と性能位置の乖離である。

### Grok BotとCursorチャネル統合の実行

Grok Botのローンチ（[INFO-005](../Information/2026-09-05/collected-raw.md#INFO-005) A-1）は、買収完了から3週間での最初の統合実行である。各Botは専用コンピュータを持ち、Zendesk等のツールに人間と同じようにサインインして操作し、承認が必要な時だけ人間に戻る。ワークフローを1回見せるとルーチンとして保存し次回以降を自動実行する（teach a task）。複数Botを同一スレッドに接続して作業をパスする（Research→Comms→Chief of Staff等）。価格はCursor Pro $20/月・SuperGrok Plus $30/月（Grok 4.6同梱）・Cursor Teams $40/シート/月で、既存Cursor/SuperGrok/Teams契約者にはGrok Botが込みである。デスクトップ（Linux .deb/AppImage/.rpm）とiOSに対応し、Enterprise向けFAQが存在する（詳細は要確認）。v4.86はこれを汎用基盤命題への最強級Cと評価した。ただし配布の動作確認と採用の定量は別次元である。ルーティング・解約率・維持率の観測窓（8/28開始）内の定量が出るまで、indeterminate構造は不変である。対抗斟定も添付する。Cursor愛好率19% vs Claude Code 46%（v4.84・B-2）という逆データが残存し、チャネルの保有が選好の獲得を意味しない。

### 政府調達での受益側固定

GenAI.mil拡大（ChatGPT Mil+Grok for Government・170万→300万人・IL5）で、OpenAIとSpaceXAIが各最大$200M契約を得て、Claudeのみが除外された（[INFO-018](../Information/2026-09-05/collected-raw.md#INFO-018) B-2）。xAIはAnthropic判決（8/27）の直後に、順応報酬構造の受益側として金額つきで位置づけられた。軍事利用への同意が政府市場での報酬に接続した構図である。ただし政府調達での地位はエンタープライズ（民間）採用の直接定量ではない。人間却下比率の定量データは66R/67R連続不在（KIQ-MIL-001）のままである。広告エコシステムでも、X Ads MCPの本番書き込み10ツール（activate_campaign含む・ブレーキ付き・OAuth2 2時間トークン）の指定クライアントにGrokとClaude Codeが選ばれた（[INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025) B-2）。Xデータ資産（広告API）とエージェント（Grok）の接続が本番書き込み権限で実装された点は、旧H-XAI-001（Xデータ活用のリアルタイム特化）が棄却された後の、X資産の別経路での活用例として記録する。

### 配給整備と性能位置の乖離

Grok 4.6がxAI APIで利用可能になり（8/29リリースノート・500kコンテキスト・テキスト+画像入力）、GitHubでgrok-build（ターミナルベースのコーディングエージェントharness/TUI）が公開された（[INFO-006](../Information/2026-09-05/collected-raw.md#INFO-006) A-2）。Grok Buildの$1/$2帯の低価格は継続するが、業界全体のコスト崩壊の中で独自性は不変であり、v4.76のmedium→low移行判定の根拠は崩れていない（H-XAI-002 58% low・±0%）。性能面では9月の第三者指数でGrok 4.6は60であり（[INFO-032](../Information/2026-09-05/collected-raw.md#INFO-032) B-1）、Sol（61）より1ポイント低く、Fable 5.1（66）・Arena上位3枠を独占するOpus系（1505/1504/1503）には及ばない。AA II 61のSol同点確認（[INFO-178](../Information/2026-08-15/collected-raw.md#INFO-178) B-1）から横ばいであり、LMSpeed・Vision Arenaの未公開も続く。実測$0.84/taskのパレート最前線（性能/コスト最適点）という位置づけは変わらない。製品出荷速度（Grok Bot・grok-build・API）と性能首位不在・採用定量不在の三面乖離が、この企業の観測構造である。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Grok Bot発表（9/4）: 専用コンピュータ・ツールサインイン・24/7・teach-a-task・複数Bot連携。配布api2.cursor.sh・販売cursor.com・Cursor Pro $20/SuperGrok Plus $30/Cursor Teams $40/シート。既存契約者には込み | [H-XAI-004](../config/hypotheses.json) 最強級C（v4.86・C-only警告付き）。買収チャネル統合の最初の動作確認。採用定量は依然不在 | A-1 | [INFO-005](../Information/2026-09-05/collected-raw.md#INFO-005) |
| 高 | Grok 4.6 API（8/29）: 500kコンテキスト・text+image入力・coding/agentic特化。grok-build（TUI harness）GitHub公開 | [H-XAI-004](../config/hypotheses.json) 配給C。[H-XAI-002](../config/hypotheses.json) C*（$1/$2帯の低価格継続するが独自性不変） | A-2 | [INFO-006](../Information/2026-09-05/collected-raw.md#INFO-006) |
| 高 | GenAI.mil拡大: Grok for GovernmentがOpenAIと並び各最大$200M・170万→300万人・Claudeのみ除外 | 順応報酬構造の受益側固定（[H-GOV-002](../config/hypotheses.json)文脈）。政府地位は民間採用定量でない | B-2 | [INFO-018](../Information/2026-09-05/collected-raw.md#INFO-018) |
| 高 | X Ads MCP本番書き込み10ツールの指定クライアントがGrokとClaude Code | X資産（広告API）とGrokの本番接続。旧H-XAI-001棄却後の別経路活用例。[IND-027](../config/indicators.json) | B-2 | [INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025) |
| 高 | 9月AA指数: Grok 4.6は60（Sol-1pt・Fable 5.1 66・Arena上位3枠はAnthropic独占） | 性能首位群に及ばない位置の確認。AA II 61同点（8月）から横ばい | B-1 | [INFO-032](../Information/2026-09-05/collected-raw.md#INFO-032) |
| 高 | OpenAIがCursorのGPTアクセスを遮断（「最も明白な例だが孤立していない」） | Cursorのモデル選択肢がGrok方向へ狭まる可能性。ルーティング観測（H-XAI-004観測窓）の解像度向上 | C-2 | [INFO-046](../Information/2026-09-05/collected-raw.md#INFO-046) |
| 高 | JetBrains公式一次データ（5〜7月・15,000人超）: Cursor職場利用18%→12%（中国28%→16%）・Claude Code 39%首位。同一情報のRampデータ: Cursor企業内採用95%・スイッチ先第1位41%・ARR $4B | 買収後チャネルの利用動向の最初のA-1データ。両方向併存で判別不能のまま | A-1 | [INFO-112](../Information/2026-08-25/collected-raw.md#INFO-112) [INFO-084](../Information/2026-08-22/collected-raw.md#INFO-084) |
| 高 | SpaceX-Cursor $60B全株式買収完了（8/14発効）・Cursor収益$100M→$2B+（13ヶ月）・買収額は推定ARR $4Bの約15倍 | [H-XAI-004](../config/hypotheses.json) 最初の構造的C（Cursor 5万社・F500 64%配チャネル）。Cognition買収打診も判明 | B-1 | [INFO-098](../Information/2026-08-15/collected-raw.md#INFO-098) [INFO-180](../Information/2026-08-15/collected-raw.md#INFO-180) [INFO-053](../Information/2026-08-22/collected-raw.md#INFO-053) |
| 高 | Grok 4.6独立確認: AA II 61=Sol同点3位タイ・実測$0.84/task・SWE-bench Verified 95.60%（4位）・Grok 4.20 Beta 2 IFBench #1（Opus費用8%） | 性能面C方向の独立検証。但し首位でなくLMSpeed/Vision Arena未公開 | B-1/B-2 | [INFO-178](../Information/2026-08-15/collected-raw.md#INFO-178) [INFO-063](../Information/2026-08-24/collected-raw.md#INFO-063) [INFO-049](../Information/2026-08-22/collected-raw.md#INFO-049) |
| 高 | Grok 4.6価格$2/$6は出力/入力比率3倍（競合主流5〜6倍）で構造的安さ・キャッシュ75%割引。DeepSeek V4 Pro $0.435/$0.87が価格フロア | [H-XAI-002](../config/hypotheses.json) 58% lowの構造不変。絶対フロアはOSS側で「低価格」独自性は中間帯の位置問題 | B-2 | [INFO-046](../Information/2026-08-22/collected-raw.md#INFO-046) [INFO-060](../Information/2026-08-24/collected-raw.md#INFO-060) |
| 高 | エンタープライズ採用定量データ57R以上連続完全不在（WAU/DAU・F500導入率・企業契約数いずれも非公開） | [H-XAI-004](../config/hypotheses.json) indeterminate維持の核心根拠。復帰条件未到達 | 構造的 | [H-XAI-004](../config/hypotheses.json) |
| 中 | FLI AI Safety Index: xAI F評価(0.65)・全9社中7位・存在的安全性は全社最弱ドメイン | 安全性次元での構造的劣位（A-1品質）。Astra/Anthropicの開示競争に対する位置 | A-1 | [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) |
| 中 | AIコーディング3強$1B ARR突破: Copilot 29%/4.7M有料・Cursor 18%/$2B・Claude Code 18%。Grok固有採用データは不在 | 競合の定量公開とGrokの非公開の対比 | B-2 | [INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| エンタープライズ採用定量データ（WAU/DAU・F500導入率・企業契約数）が初めて公開される | [H-XAI-004](../config/hypotheses.json)の核心パラメータ不在（57R以上）が解消し、indeterminateから確度評価に復帰する | 次回 | [IND-027](../config/indicators.json) |
| 観測窓（8/28開始）内でCursorのモデルルーティング・F500解約率・Grok Bot稼働定量が観測される | チャネル統合の採用転換が初めて測定される。OpenAIのCursor GPT遮断（[INFO-046](../Information/2026-09-05/collected-raw.md#INFO-046)）後はGrok優先化の観測解像度が上がる。窓内（〜11月中旬）でシグナルが出なければ「最強級C」の評価は弱まる | 90日 | [IND-027](../config/indicators.json) |
| Grok 4.6がLMSpeed/Vision Arena等の独立ランキングで上位に入る、またはAA指数で首位群（66超）に達する | 「真剣な作業」からの除外構造の解除が始まる。現在は9月AA 60・IFBench #1（B-3単一）の部分充足 | 90日 | [IND-025](../config/indicators.json) |
| Grok for Governmentの利用実績（ユーザー数・却下比率・誤標的率）が公開される | KIQ-MIL-001（66R/67R不在）が解消に向かい、政府面での地位強化の実態が測定される | 90日 | [IND-030](../config/indicators.json) |
| 価格差からシェアへの転換を示す直接定量証拠（Grok固有API呼び出し量・grok-build利用数・Grok Bot稼働数）が公開される | [H-XAI-002](../config/hypotheses.json) 58% lowの帯内再評価 | 90日 | [IND-025](../config/indicators.json) |
| Grokが$2帯での値下げに追随する、またはLuna級の価格フロアに接触する | [H-XAI-002](../config/hypotheses.json)の更なる低下。「低価格」前提自体の陳腐化確定 | 90日 | [IND-025](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:---:|---|---|---|
| [H-XAI-004](../config/hypotheses.json) | xAIはGrokを汎用AI基盤として展開し、Xデータ依存なしでエンタープライズ市場シェアを獲得する | 52% indeterminate | v4.86 ±0%。Grok Bot発表（[INFO-005](../Information/2026-09-05/collected-raw.md#INFO-005) A-1・Cursorチャネル配布実行）は最強級Cで観測窓（8/28開始）初期データとして蓄積。Grok 4.6 API+grok-build（[INFO-006](../Information/2026-09-05/collected-raw.md#INFO-006) A-2）・GenAI.mil $200M（[INFO-018](../Information/2026-09-05/collected-raw.md#INFO-018) B-2）・X Ads MCP指定（[INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025) B-2）もC側。C-only警告付き（Cursor愛好率19% vs Claude Code 46%〔v4.84・B-2〕を対抗斟定）。過去C: Cursor $60B買収完了（[INFO-098](../Information/2026-08-15/collected-raw.md#INFO-098)）・AA II 61 Sol同点（[INFO-178](../Information/2026-08-15/collected-raw.md#INFO-178)）・SWE-V 95.60%（[INFO-063](../Information/2026-08-24/collected-raw.md#INFO-063)）。I側: 採用定量57R以上完全不在・Meta-Manus 8ヶ月放棄（[INFO-103](../Information/2026-08-15/collected-raw.md#INFO-103) B-2）・JetBrains 12%後退（[INFO-112](../Information/2026-08-25/collected-raw.md#INFO-112) A-1・Ramp両方向併存）。ルーティング・解約率・維持率の窓内定量が出るまで不定構造不変 | [INFO-005](../Information/2026-09-05/collected-raw.md#INFO-005) [INFO-006](../Information/2026-09-05/collected-raw.md#INFO-006) [INFO-018](../Information/2026-09-05/collected-raw.md#INFO-018) [INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025) | [INFO-112](../Information/2026-08-25/collected-raw.md#INFO-112) [INFO-103](../Information/2026-08-15/collected-raw.md#INFO-103) |
| [H-XAI-002](../config/hypotheses.json) | xAIはGrokを低価格で提供し、価格競争で市場シェアを獲得する | 58% low | v4.86 ±0%（v4.76 -1%+medium→low移行執行・v4.77以来±0%）。grok-buildの$1/$2帯低価格継続（[INFO-006](../Information/2026-09-05/collected-raw.md#INFO-006)・C*注記: 業界全体コスト崩壊の中で独自性不変・移行判定の根拠は崩れていない）。C方向残存: 出力/入力比率3倍の構造的安さ（[INFO-046](../Information/2026-08-22/collected-raw.md#INFO-046)）・$0.84/taskパレート最前線（[INFO-178](../Information/2026-08-15/collected-raw.md#INFO-178)）。I方向: DeepSeek V4 Proフロア・価格差からシェアへの転換定量の長期不在 | [INFO-046](../Information/2026-08-22/collected-raw.md#INFO-046) [INFO-178](../Information/2026-08-15/collected-raw.md#INFO-178) | [INFO-060](../Information/2026-08-24/collected-raw.md#INFO-060) [INFO-058](../Information/2026-08-25/collected-raw.md#INFO-058) |
| [H-XAI-001](../config/hypotheses.json) | （棄却）Xデータ活用でリアルタイム特化を差別化する | 35% rejected | 42R以上のXデータ活用直接証拠不在のまま。X Ads MCPのGrok指定（[INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025)）は広告API経由の別命題で棄却判定は覆らない | （なし） | 42R以上の証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | （棄却）SpaceX統合で宇宙・製造業特化AIを展開する | 35% rejected | 特化AI製品証拠の不在継続。Colossusは汎用インフラ扱い | （なし） | 特化製品証拠不在 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | セキュリティ侵害頻度 | 実被害A-2報告でcritical | **critical/rising**（v4.86・業界指標値）。xAI固有の新規A-2実被害はなし。Grok Botのツールサインイン自律操作（Zendesk等・[INFO-005](../Information/2026-09-05/collected-raw.md#INFO-005)）は攻撃表面の文脈で監視材料化。DL 60%減は未解決 | 2026-09-05 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性・測定慣行 | 複数ベンチマーク×複数ラボで再現ならhigh | elevated/stable（v4.86）。9月AA指数でGrok 4.6は60（Sol-1pt・[INFO-032](../Information/2026-09-05/collected-raw.md#INFO-032) B-1）。ARC-AGI-3標準62.7% vs Provider 99.9%の37.2pt差（[INFO-030](../Information/2026-09-05/collected-raw.md#INFO-030) A-1）で測定慣行依存が一次立証され、AA II 61同点の意味も測定家族依存の文脈で読み直す | 2026-09-05 |
| [IND-026](../config/indicators.json) | エージェント本番環境到達率 | 期待-実態ギャップの定量蓄積 | high/rising（v4.86）。三次定量: 配備26-50体→76-100体/四半期 vs 成熟ガバナンス21%・採用84% vs 信頼33%。Grok Botの常駐型24/7稼働は配備形態の新類型（定量なし） | 2026-09-05 |
| [IND-027](../config/indicators.json) | エコシステム標準化進展度 | 攻撃表面の標準化進行 | high/rising（v4.86）。X Ads MCP指定クライアントGrok+Claude Code（[INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025)）・grok-build公開・クロスエージェント4,500スキル（[INFO-014](../Information/2026-09-05/collected-raw.md#INFO-014)）。フレームワーク比較13種でGrok Build主要枠外は不変 | 2026-09-05 |
| [IND-028](../config/indicators.json) | AGI到達度（予測分裂） | 分裂の深化・法制化圧力 | high/rising（v4.86）。Brockman「AGI時代」vs Chollet「定義には同意しない」・Sanders超知能禁止法案（[INFO-052](../Information/2026-09-05/collected-raw.md#INFO-052)）。xAI側の新規主観宣言は本日なし | 2026-09-05 |
| [IND-029](../config/indicators.json) | AIインフラ制約（債務構造） | 3値強制判定の観測 | high/rising（v4.86）。OpenAI銀団3値強制判定≈09-09（最優先監視）。capex $700-900B/+36%・ECB $142B警告（[INFO-036](../Information/2026-09-05/collected-raw.md#INFO-036)/[INFO-037](../Information/2026-09-05/collected-raw.md#INFO-037)）。Nvidia循環ファイナンス監視継続 | 2026-09-05 |
| [IND-030](../config/indicators.json) | AI能力-リスク二面性 | critical解消3基準 | critical/rising（v4.86）。N=1実質32R。GenAI.mil拡大でGrok for Governmentが$200M契約（[INFO-018](../Information/2026-09-05/collected-raw.md#INFO-018)）・判決後もPentagon指定維持の新ブランチ。KIQ-MIL-001 66R/67R不在継続。xAIは軍事利用同意済み。critical解消3基準いずれも未到達 | 2026-09-05 |

## 6. 変更履歴

| 日付 | 変更 | きっかけ | 過去 → 現在 |
|:-:|---|---|---|
| 2026-09-05 | §0〜§7書き直し（鮮度タイムアウト11日）。Grok Bot発表（9/4・A-1・Cursorチャネル配布実行）を[H-XAI-004](../config/hypotheses.json)最強級Cとして反映（C-only警告・愛好率逆データ対抗斟定付き）。Grok 4.6 API+grok-build公開・GenAI.mil Grok for Government $200M・X Ads MCP指定Grok・9月AA指数60を新規計上。KIQ-MIL-001 66R/67R・採用定量不在57R以上に更新。§5全指標をv4.86値に更新 | Grok Bot発表（フロンティアエージェント製品リリース） | H-XAI-004 indeterminate/52%（±0%）・H-XAI-002 58% low（±0%） |
| 2026-08-25 | ターゲット編集。H-XAI-002 59% medium→58% low（v4.76帯移行執行）を反映。08-24〜25バッチ（Grok Build CLI・GEAP展開・SWE-V 95.60%・Responses API互換・JetBrains一次データ）を計上 | [Arbiter v4.76](../state/arbiter-2026-08-24.md) | H-XAI-002 59% medium→58% low |
| 2026-08-22 | ターゲット編集。買収後初の独立採用系データ（JetBrains/Ramp両方向併存）・Cognition買収打診・IFBench #1を計上 | [INFO-084](../Information/2026-08-22/collected-raw.md#INFO-084) | H-XAI-004 indeterminate/52%（±0%） |
| 2026-08-15 | ターゲット編集。SpaceX-Cursor $60B買収完了（8/14発効）・AA II 61 Sol同点独立確認を反映 | [INFO-098](../Information/2026-08-15/collected-raw.md#INFO-098) | H-XAI-004 indeterminate/52%（±0%） |
| 2026-08-14 | ターゲット編集。Grok 4.6リリース・Grok Bot新製品（ベータ）を反映 | [INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) | H-XAI-004 indeterminate/52%（±0%） |

## 7. ブラインドスポット

- Grok Botの配布がCursorチャネル経由であることは公式製品ページで確認できたが、ダウンロード数・稼働Bot数・teach-a-taskの実利用頻度は一切公開されない。「配布の動作確認」と「採用の定量」の間に観測不能の壁が残る。
- Enterprise向けFAQの詳細（価格・契約条件・ガバナンス）が要確認のまま。Grok Botのエンタープライズ展開がウェイティングリスト段階から進んだかの判別ができない。
- OpenAIのCursor GPTアクセス遮断（C-2）がGrok Bot配布と同じ週に起きた因果は推定でしかない。遮断がGrok優先化の結果か、買収前からの契約終了かは非公開である。
- Cursor愛好率19% vs Claude Code 46%という逆データが、チャネル保有の価値をどれだけ毀損するかの定量化手段がない。JetBrains利用データ（12%後退）とRamp支出データ（企業内採用95%）の両方向併存も解消されていない。
- Grok 4.6の性能プロファイルの全域検証は依然不可能。LMSpeed・Vision Arena未公開・会計等の専門ベンチの4.6版スコア不在・9月AA 60が測定家族依存の中でどう読めるか（ARC 37.2pt差の文脈）の整理も未完了である。
- KIQ-MIL-001の人間却下比率が66R/67R連続不在。Grok for Governmentの$200M契約で利用規模は拡大するのに、運用実態の検証手段が増えない構造は、AI推奨の却下率が観測されないリスクを累積させる。
- Grok Botがツールにサインインして自律操作する設計は、エージェント権限の攻撃表面を消費者・エンタープライズ双方に拡張する。xAI固有のインシデント報告体制（FLI F評価・存在的安全性全社最弱）との組み合わせで、初動事例の観測重要性が高い。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 | 出典 |
|---|---|---|
| [INFO-005](../Information/2026-09-05/collected-raw.md#INFO-005) | Grok Bot: 常駐AIチームメイト・専用コンピュータ・teach-a-task・複数Bot連携・Cursorチャネル配布・$20-40/月(A-1・H-XAI-004最強級C) | x.ai/bot公式 |
| [INFO-006](../Information/2026-09-05/collected-raw.md#INFO-006) | Grok 4.6 API（500k ctx・text+image）+grok-build GitHub公開(A-2) | docs.x.ai / GitHub |
| [INFO-018](../Information/2026-09-05/collected-raw.md#INFO-018) | GenAI.mil拡大300万人・SpaceXAI各最大$200M・Claude除外(B2・順応報酬の受益側) | DefenseScoop等 |
| [INFO-025](../Information/2026-09-05/collected-raw.md#INFO-025) | X Ads MCP本番書き込み10ツール・指定クライアントGrok+Claude Code(B2) | PPC Land |
| [INFO-032](../Information/2026-09-05/collected-raw.md#INFO-032) | 9月第三者指数: Grok 4.6 60（Sol-1pt）・Fable 5.1 66・Arena Anthropic 3枠独占(B1) | modelgrep/BenchLM等 |
| [INFO-046](../Information/2026-09-05/collected-raw.md#INFO-046) | OpenAIのCursor GPTアクセス遮断・供給遮断型ロックイン・コンテキスト層移行コスト(C2) | PE Collective等 |
| [INFO-036](../Information/2026-09-05/collected-raw.md#INFO-036) | capex $700-900B/+36%・評価額ランキング(C2・IND-029分母) | 市場統計 |
| [INFO-112](../Information/2026-08-25/collected-raw.md#INFO-112) | JetBrains公式一次: Cursor職場利用18→12%・Claude Code 39%首位(A-1・Rampデータと両方向併存) | JetBrains Research |
| [INFO-009](../Information/2026-08-25/collected-raw.md#INFO-009) | grok-4.6 Responses API互換・grok-4.20-multi-agent-0309（1M ctx・$1.25/M帯）(A-3) | docs.x.ai |
| [INFO-063](../Information/2026-08-24/collected-raw.md#INFO-063) | SWE-bench Verified: Grok 4.6 95.60%初掲載・4位(B-2) | vals.ai |
| [INFO-002](../Information/2026-08-24/collected-raw.md#INFO-002) | Grok 4.6 GEAP Model Garden提供（$2/$6・500k ctx）(A-3) | Google Cloud |
| [INFO-046](../Information/2026-08-22/collected-raw.md#INFO-046) | Grok 4.6出力比率3x・キャッシュ75%割引 vs DeepSeekフロア・3極化(B-2) | LLM Pricing Tracker |
| [INFO-084](../Information/2026-08-22/collected-raw.md#INFO-084) | JetBrains調査+Ramp支出データ（Cursor 95%・ARR $4B）(A-3・両方向併存) | JetBrains / Ramp |
| [INFO-049](../Information/2026-08-22/collected-raw.md#INFO-049) | Grok 4.20 Beta 2 IFBench #1（83・Opus費用8%）(B-3・単一ランキング) | Veso Research |
| [INFO-053](../Information/2026-08-22/collected-raw.md#INFO-053) | SpaceX-Cursor $60B買収完了再確認・Cognition買収打診(B-2) | TechCrunch等 |
| [INFO-098](../Information/2026-08-15/collected-raw.md#INFO-098) | SpaceX-Cursor $60B全株式買収完了・8/14発効(B-1) | Bloomberg |
| [INFO-180](../Information/2026-08-15/collected-raw.md#INFO-180) | Cursor収益$100M→$2B+（13ヶ月）・買収額15倍ARR(B-1) | Forbes |
| [INFO-177](../Information/2026-08-15/collected-raw.md#INFO-177) | Grok 4.6公式: AA II 61・GDPval-AA 1753・$2/$6・SpaceXAIブランド統一(A-1) | x.ai |
| [INFO-178](../Information/2026-08-15/collected-raw.md#INFO-178) | AA分析: 61 Sol同点3位タイ・$0.84/taskパレート最前線(B-1) | artificialanalysis.ai |
| [INFO-103](../Information/2026-08-15/collected-raw.md#INFO-103) | Meta-Manus支配8ヶ月放棄・M&A統合限界前例(B-2・I側採録) | Computerworld |
| [INFO-089](../Information/2026-08-14/collected-raw.md#INFO-089) | Grok 4.6詳細: agentic RL・長時間エージェント・Grok 4.20 variant(A-1) | x.ai |
| [INFO-107](../Information/2026-07-17/collected-raw.md#INFO-107) | FLI Safety Index: xAI F評価0.65・9社中7位(A-1) | FLI |
| [INFO-075](../Information/2026-08-03/collected-raw.md#INFO-075) | AIコーディング3強定量比較・Grok固有採用不在(B-2) | uvik.net |
| [Arbiter v4.86](../state/arbiter-2026-09-05.md) | H-XAI-004 52%不定維持（Grok Bot最強級C・C-only警告・観測窓初期データ）・H-XAI-002 58%維持 | 内部参照 |
| [Arbiter v4.76](../state/arbiter-2026-08-24.md) | H-XAI-002 59→58%帯移行執行の根拠 | 内部参照 |
