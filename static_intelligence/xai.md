# xAI → SpaceXAI

> 最終判断更新: 2026-06-11
> 全体確信度: 低
> 情報非対称性: SpaceXAIはSpaceXの内部組織であり、独立企業としての財務・戦略・ロードマップ情報が構造的に入手不可。Colossus貸与条件も非公開
> 主参照: hypotheses.json#H-XAI-001/002/003/004, indicators.json#IND-013/025/026/027/028/029/030

## 0. 一文要約

我々はxAIを、**SpaceXAIとしてGrok製品群を画像生成・音楽・音声エージェント・コーディングに拡大しつつ、エンタープライズ市場で構造的苦戦に直面しH-XAI-002が59%でmedium→low移行審査を控える組織**と読んでいる。最大の根拠は、Gopuff Go agent [INFO-013](../Information/2026-06-11/collected-raw.md#INFO-013), Grok Imagine 1.5 Preview [INFO-014](../Information/2026-06-11/collected-raw.md#INFO-014), Composer 2.5 [INFO-016](../Information/2026-06-11/collected-raw.md#INFO-016), Grok Build 0.1 on API [INFO-017](../Information/2026-06-11/collected-raw.md#INFO-017) が示す製品幅の急拡大と、それにもかかわらずReuters報道によるxAI開発者ログ(DL)が1月20Mから4月8.3Mへ60%減少した定量証拠 [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) が未解決であることの乖離だ。Arbiter v4.05(2026-06-11)はH-XAI-002を59%(±0%)で据え置き、新規I追加なしとしたが、59%以下が継続すれば次ラウンドでmedium→low移行審査が触发される。H-XAI-004も55%(±0%)で据え置き、C蓄積は安定するが構造的変化なし。API価格コモディティ化はLLM API価格$30→$1-5/MTokへの95%以上下落 [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) とGitHub Copilot従量制移行 [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) で継続加速中。SCN-004(30%)が初めてトップシナリオに浮上し、コモディティ化圧力がxAIの戦略的前提を侵食している。Grok VoiceのVapi統合 [INFO-015](../Information/2026-06-11/collected-raw.md#INFO-015) は音声エージェント分野への外部プラットフォーム展開を示すが、H-XAI-002/H-XAI-004へのC評価には至っていない。もしH-XAI-002が次ラウンドで59%以下に低下する、DL減少傾向が3ヶ月以上継続する、Colossus貸与がAnthropic以外にも拡大する、またはGrok API提供が終了または大幅縮小する、のいずれかが観測されたら、判断を再構築する。

## 1. コア判断

SpaceXAIの製品幅が急速に拡大している。Gopuff Go agentはGrokのテキスト・音声・画像モデルを統合したショッピングアシスタントで、13年分の需要インテリジェンスに基づくパーソナライズドカート構築を実現した [INFO-013](../Information/2026-06-11/collected-raw.md#INFO-013)。Grok Imagine 1.5 Previewは画像生成品質の向上を示し [INFO-014](../Information/2026-06-11/collected-raw.md#INFO-014)、IND-025の更新材料となる。Composer 2.5は音楽生成のアップグレード [INFO-016](../Information/2026-06-11/collected-raw.md#INFO-016)、Grok Build 0.1 on APIは$1/MTokでコーディングエージェントのAPIアクセスを提供する [INFO-017](../Information/2026-06-11/collected-raw.md#INFO-017)。Grok VoiceのVapi統合 [INFO-015](../Information/2026-06-11/collected-raw.md#INFO-015) は音声AIプラットフォームへの外部展開を示す。これらはテキスト、画像、音声、音楽、コーディング、ショッピングにまたがる製品幅の拡大を示す。

しかしエンタープライズ市場での苦戦が構造化したままである。Reuters報道によるxAI開発者ログ(DL)の1月20Mから4月8.3Mへの60%減少 [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) は未解決であり、DL回復データは不在のままだ。H-XAI-002(価格競争力でシェア獲得)はArbiter v4.05で59%(±0%)と据え置かれたが、新規I追加なしの条件下での据え置きであり、59%以下が継続すれば次ラウンドでmedium→low移行審査が触发される。製品幅の拡大はC蓄積に寄与するが、製品発表のみの評価はメソドロジー(5)で制約される。

価格環境の悪化は継続している。LLM API価格が$30→$1-5/MTokへ95%以上下落し [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038)、GitHub Copilotが定額から従量制へ移行した [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039)。DeepSeek V4 ProがGPT-5.5 Proを精度で上回り75%値下げで同等以上の精度を提供する状況 [INFO-051](../Information/2026-06-11/collected-raw.md#INFO-051) は、コモディティ化圧力が更に強まっている。この構造的圧力がSCN-004を30%に押し上げ、初めてトップシナリオとした。

H-XAI-004(汎用AI基盤としてエンタープライズ獲得)は55%(±0%)で据え置き。C蓄積は安定するが、エンタープライズ採用との乖離が解消されておらず、構造的変化は観測されない。$20B Series E [INFO-042](../Information/2026-05-28/collected-raw.md#INFO-042) はColossus拡充の資基盤を維持し、Grok 4.1のマルチモーダルベンチマーク97.8% [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016) は性能面のCを蓄積するが、性能とエンタープライズ採用の乖離がH-XAI-004の構造的課題として残る。Colossus 1(220K GPU)のAnthropic貸与 [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) も継続し、SpaceXAIの「モデル開発兼インフラ提供」の二面性は維持されている。H-XAI-001(Xデータ活用差別化)とH-XAI-003(宇宙・製造業特化AI)は引き続き棄却済み(35%)。

## 2. 判断の重心

| 重要度 | 観測した事実 | この判断との関係 | 信頼度 | 参照 |
|:-:|---|---|:-:|---|
| 高 | Gopuff Go agent: Grok text/audio/image統合ショッピングアシスタント。13年分の需要データ活用 | 製品幅拡大の直接証拠。コーディング以外のエージェント適用領域拡大。H-XAI-004のC候補 | A-3 | [INFO-013](../Information/2026-06-11/collected-raw.md#INFO-013) |
| 高 | H-XAI-002 59%据え置き: 新規I追加なし。59%以下継続で次ラウンドmedium→low移行審査 | 価格競争力仮説の信頼度が低下傾向。DL回復データ不在が根拠 | A-3 | [Arbiter v4.05](../state/arbiter-2026-06-11.md) |
| 高 | DL 60%減少: xAI開発者ログ1月20M→4月8.3M。未解決 | H-XAI-002への定量I。エンタープライズ苦戦の直接証拠として継続蓄積 | B-2 | [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| 高 | LLM API価格$30→$1-5/MTok: 95%+下落継続。DeepSeek V4 Proが75%値下げで同等精度 | 価格コモディティ化の加速。H-XAI-002の「低価格」独自性の更なる希薄化。SCN-004支援 | C-3 | [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) [INFO-051](../Information/2026-06-11/collected-raw.md#INFO-051) |
| 高 | Grok Build 0.1 on API: $1/MTokでコーディングエージェントAPI提供 | 低価格API戦略の継続。IND-027標準化潮流と整合 | A-3 | [INFO-017](../Information/2026-06-11/collected-raw.md#INFO-017) |
| 高 | Grok Imagine 1.5 Preview: 画像生成品質向上 | マルチモーダル信頼性指標(IND-025)更新材料。製品幅のC蓄積 | A-3 | [INFO-014](../Information/2026-06-11/collected-raw.md#INFO-014) |
| 高 | SCN-004 30%でトップシナリオ浮上: API価格コモディティ化でxAI戦略的前提侵食 | 価格競争力仮説が市場構造変化で損なわれる方向への決定的なシフト | A-3 | [Arbiter v4.05](../state/arbiter-2026-06-11.md) |
| 高 | Colossus 1(220K GPU)全容量をAnthropicに貸与(継続) | SpaceXAIが「AIインフラ提供者」側面を持つ。競合に計算資源を貸す構造は不変 | A-3 | [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) |
| 中 | Grok Voice Vapi統合: 音声AIエージェントの外部プラットフォーム展開 | 音声エージェント分野への進出。H-XAI-004のC候補だが単独では不十分 | A-3 | [INFO-015](../Information/2026-06-11/collected-raw.md#INFO-015) |
| 中 | Composer 2.5: 音楽生成アップグレード | 製品幅拡大の補強材料。IND-026更新の文脈 | A-3 | [INFO-016](../Information/2026-06-11/collected-raw.md#INFO-016) |
| 中 | GitHub Copilot定額→従量制移行 | API価格コモディティ化がエージェント製品層に波及。SCN-004方向への圧力 | A-2 | [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) |

## 3. 反証の閾値

| 反証指標 | 観測したら何が崩れるか | 期限 | 監視先 |
|---|---|:-:|---|
| H-XAI-002が次ラウンドで59%以下に低下する | medium→low移行が確定し、価格競争力仮説の根本的見直しが必要となる | 次ラウンド | [IND-013](../config/indicators.json) |
| DL減少傾向が3ヶ月以上継続する | H-XAI-002の59%根拠が崩れ、価格競争力仮説の根本的見直しが必要となる | 90日 | [IND-013](../config/indicators.json) |
| Colossus貸与がAnthropic以外にも拡大し、SpaceXAIが「AIインフラプロバイダー」として定着する | 現在の「モデル開発兼インフラ提供」の二面性が「インフラ提供中心」に移行する | 90日 | [IND-029](../config/indicators.json) |
| GrokのAPI提供が終了または大幅に縮小される | SpaceXAIが外部市場から撤退し内部利用に特化する場合、H-XAI-002とH-XAI-004が同時に崩れる | 90日 | [IND-013](../config/indicators.json) |
| Grok Buildのユーザー定着率が低迷し、Codex/Claude Code比で測定可能な差が開く | H-XAI-004の55%根拠が崩れ、コーディングエージェント市場での競争力に疑問 | 90日 | [IND-027](../config/indicators.json) |
| API価格コモディティ化が更に進行し、Grok独自の価格優位が消滅する | H-XAI-002の根拠が「価格競争」から「コモディティ化での生き残り」に再定義される | 60日 | [IND-013](../config/indicators.json) |
| SpaceXAIが宇宙・製造業特化AI機能を具体的に発表する | H-XAI-003の棄却が見直される | 180日 | [IND-013](../config/indicators.json) |

## 4. 進行中の仮説

| 仮説ID | 一文 | 確度 | 確度の根拠 | 強める証拠 | 弱める証拠 |
|---|---|:-:|---|---|---|
| [H-XAI-002](../config/hypotheses.json) | 価格競争力でシェアを獲得する | 59% | Grok Build低価格はgenuine CだがDL数回復データ不在。API価格95%+下落の構造的I蓄積中。DeepSeek V4 Proが75%値下げで同等精度。59%以下継続で次ラウンドmedium→low移行審査。DL回復観測までは上昇根拠なし | [INFO-017](../Information/2026-06-11/collected-raw.md#INFO-017) $1/MTok API [INFO-042](../Information/2026-05-28/collected-raw.md#INFO-042) $20B資基盤 | [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) DL 60%減 [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) API価格下落 [INFO-051](../Information/2026-06-11/collected-raw.md#INFO-051) DeepSeek V4 Pro |
| [H-XAI-004](../config/hypotheses.json) | 汎用AI基盤としてエンタープライズ市場を獲得する | 55% | Gopuff Go・Grok Imagine 1.5・Composer 2.5・Vapi統合で製品幅拡大のC蓄積。しかしDL 60%減のエンタープライズ苦戦Iが直撃。C蓄積は安定するが構造的変化なし | [INFO-013](../Information/2026-06-11/collected-raw.md#INFO-013) [INFO-014](../Information/2026-06-11/collected-raw.md#INFO-014) [INFO-015](../Information/2026-06-11/collected-raw.md#INFO-015) [INFO-016](../Information/2026-06-11/collected-raw.md#INFO-016) [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) | [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) エンタープライズ苦戦 |
| [H-XAI-001](../config/hypotheses.json) | (棄却) Xデータ活用でリアルタイム特化を差別化する | 35% | 37R+Xデータ活用証拠不在。xAI→SpaceXAI統合で観測の意義自体が低下 | (なし) | 37R+証拠不在 |
| [H-XAI-003](../config/hypotheses.json) | (棄却) SpaceX統合で宇宙・製造業特化AIを展開する | 35% | 38R+直接的特化AI製品証拠不在 | (なし) | 38R+特化製品証拠不在 |

## 5. 監視指標

| 指標ID | 何を見るか | 閾値 | 現在値 | 最終確認 |
|---|---|---|---|:-:|
| [IND-013](../config/indicators.json) | Grok API採用・DL動向 | DL回復で elevated | DL 60%減未解決 [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058)。H-XAI-002 59%でmedium→low移行審査注視 | 2026-06-11 |
| [IND-025](../config/indicators.json) | マルチモーダル信頼性 | elevated/stable | Grok Imagine 1.5 Preview [INFO-014](../Information/2026-06-11/collected-raw.md#INFO-014)。量的向上継続。「真の理解」検証未解決 | 2026-06-11 |
| [IND-026](../config/indicators.json) | 製品幅拡張度 | high/rising | Gopuff Go agent [INFO-013](../Information/2026-06-11/collected-raw.md#INFO-013), Composer 2.5 [INFO-016](../Information/2026-06-11/collected-raw.md#INFO-016), Vapi統合 [INFO-015](../Information/2026-06-11/collected-raw.md#INFO-015)。テキスト・画像・音声・音楽・コーディング・ショッピングに拡大 | 2026-06-11 |
| [IND-027](../config/indicators.json) | Grokエージェントスタック採用状況 | high/rising | Grok Build 0.1 on API($1/MTok) [INFO-017](../Information/2026-06-11/collected-raw.md#INFO-017)。ACP対応。DL 60%減で採用動向注意 | 2026-06-11 |
| [IND-028](../config/indicators.json) | AGI到達度指標 | high/rising | RSI「定義された実験ではほぼ超人」 [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046)。Hassabis AGI ~2030 [INFO-047](../Information/2026-06-07/collected-raw.md#INFO-047)。条件付high移行承認済み | 2026-06-11 |
| [IND-029](../config/indicators.json) | AIインフラ制約 | high/rising | xAI $20B Series E(Q1 2026最大) [INFO-042](../Information/2026-05-28/collected-raw.md#INFO-042)。Colossus 220K GPU Anthropic貸与 [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) | 2026-06-11 |
| [IND-030](../config/indicators.json) | AI能力とリスクの二面性 | high/rising | Pentagon Task Force [INFO-049](../Information/2026-05-22/collected-raw.md#INFO-049)。SCR指定 [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018)。能力向上とリスク増大の同時進行が新段階 | 2026-06-11 |

## 6. 変化履歴

| 日付 | 変更 | きっかけ |
|:-:|---|---|
| 2026-06-11 | Arbiter v4.05反映。H-XAI-002 59%(±0%)据え置き、次ラウンドmedium→low移行審査注記。H-XAI-004 55%(±0%)据え置き。Gopuff Go(INFO-013)・Grok Imagine 1.5(INFO-014)・Vapi統合(INFO-015)・Composer 2.5(INFO-016)・Grok Build 0.1 API(INFO-017)で製品幅拡大反映。SCN-004 30%でトップシナリオ浮上。IND-013/026追加、IND-025にImagine 1.5反映 | [Arbiter v4.05](../state/arbiter-2026-06-11.md) |
| 2026-06-07 | Arbiter v4.01反映。全xAI仮説±0%据え置き。GitHub Copilot従量制移行でコモディティ化圧力追加。SCN-004 27%に上昇。IND-028条件付high移行。SCR指定がxAI政府ポジショニングへの影響監視追加 | [Arbiter v4.01](../state/arbiter-2026-06-07.md) |
| 2026-06-01 | Arbiter v3.95反映。全xAI仮説±0%据え置き。SCN-004(26%)>SCN-002(24%)順位交代 | [Arbiter v3.95](../state/arbiter-2026-06-01.md) |
| 2026-05-28 | Grok Build正式リリース・DL 60%減少・$20B Series E確認・API価格95%+下落・Grok 4.1 97.8%反映。H-XAI-002 63→61%(-2%)・H-XAI-004 56→55%(-1%) | [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) |
| 2026-05-22 | Grok Build 0.1ベータ・Pentagon Task Force参加・$20B調達・API価格-67%反映 | [INFO-010](../Information/2026-05-22/collected-raw.md#INFO-010) [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) |
| 2026-05-15 | Grok Build CLI新規参入・OpenClaw連携で全面書き直し | [INFO-004](../Information/2026-05-15/collected-raw.md#INFO-004) [INFO-010](../Information/2026-05-15/collected-raw.md#INFO-010) |
| 2026-05-14 | H-XAI-001/003正式棄却 + Grok 5製品連続リリース + Colossus Anthropic提携反映 | 2026-05-14複数INFO |
| 2026-05-09 | xAI→SpaceXAI統合・Colossus Anthropic貸与・Grok 4.3リリース反映 | 2026-05-09複数INFO |

## 7. ブラインドスポット

- SpaceXAIの内部戦略が外部から観測不能。Gopuff Go・Vapi統合・Composer 2.5の製品展開は観測できるが、その背景にある意思決定(SpaceX本体の投資判断なのか、SpaceXAI内部の戦略なのか)が判別不能。
- Colossus 1をAnthropicに貸与した理由が不明。「第1世代クラスタの余剰活用」「Anthropicとの関係構築」「企業金融的動機」のいずれか、または複合。
- Grok Buildの外部利用データが限定的。DL 60%減少は定量証拠だが、Grok Build発売直後の短期的データ可能性が指摘されている。実際のユーザー数、API呼び出し量、エンタープライズ契約数は引き続き確認できない。
- API価格95%+下落がGrok API収益モデルに与える圧力を定量できていない。全プロバイダ一律下落はGrok固有の問題ではないが、$20B調達の回収スケジュールとの整合性が不透明。
- H-XAI-002のmedium→low移行審査が次ラウンドで触发される場合の、判定基準と影響範囲が未定義。59%→58%でも移行するのか、複数ラウンドの傾向を見るのか不明。
- H-XAI-001/003の棄却後、SpaceXAIとしての新しい仮説フレーム(H-XAI-005)の定義が継続未実行。Colossus貸与の拡大、軌道コンピューティングの進展、Grok製品群の戦略的方向性を統合する枠組みが不在。
- 性能向上(Grok 4.1 97.8%)とエンタープライズ採用(DL 60%減)の乖離の原因が不明。製品幅の急拡大(Gopuff・Vapi・Composer・Imagine)がこの乖離を解消するのか、逆にリソース分散で悪化させるのかも未検証。

## 付録: 直近30日の参照Evidence

| Evidence | 用途 |
|---|---|
| [Arbiter v4.05](../state/arbiter-2026-06-11.md) | H-XAI-002 59%(±0%)据え置き。H-XAI-004 55%(±0%)据え置き。SCN-004 30%トップ |
| [INFO-013](../Information/2026-06-11/collected-raw.md#INFO-013) | Gopuff Go agent: Grok統合ショッピングアシスタント(A-3) |
| [INFO-014](../Information/2026-06-11/collected-raw.md#INFO-014) | Grok Imagine 1.5 Preview: 画像生成品質向上(A-3) |
| [INFO-015](../Information/2026-06-11/collected-raw.md#INFO-015) | Grok Voice Vapi統合: 音声エージェント外部展開(A-3) |
| [INFO-016](../Information/2026-06-11/collected-raw.md#INFO-016) | Composer 2.5: 音楽生成アップグレード(A-3) |
| [INFO-017](../Information/2026-06-11/collected-raw.md#INFO-017) | Grok Build 0.1 on API: $1/MTokコーディングエージェント(A-3) |
| [INFO-051](../Information/2026-06-11/collected-raw.md#INFO-051) | DeepSeek V4 Pro精度超過・75%値下げ: コモディティ化加速(B-3) |
| [INFO-054](../Information/2026-06-11/collected-raw.md#INFO-054) | GPT-5.5 vs Claude Opus 4.7 vs Grok 4.3比較: 各社差別化軸(C-3) |
| [Arbiter v4.01](../state/arbiter-2026-06-07.md) | 全xAI仮説±0%据え置き判定。SCN-004 27%。IND-028条件付high移行 |
| [INFO-039](../Information/2026-06-07/collected-raw.md#INFO-039) | GitHub Copilot定額→従量制移行: エージェント層コモディティ化(A-2) |
| [INFO-046](../Information/2026-06-07/collected-raw.md#INFO-046) | RSI「定義された実験ではほぼ超人」: AGI到達度(A-1) |
| [INFO-018](../Information/2026-06-07/collected-raw.md#INFO-018) | Pentagon SCR指定: 政府調達環境再編(A-1) |
| [INFO-006](../Information/2026-05-28/collected-raw.md#INFO-006) | Grok Build正式リリース: ACP対応コーディングエージェント(A-3) |
| [INFO-016](../Information/2026-05-28/collected-raw.md#INFO-016) | Grok 4.1マルチモーダルベンチマーク97.8%第2位(C-3) |
| [INFO-038](../Information/2026-05-28/collected-raw.md#INFO-038) | LLM API価格$30→$1-5/MTok 95%+下落(C-3) |
| [INFO-042](../Information/2026-05-28/collected-raw.md#INFO-042) | xAI $20B Series E(Q1 2026最大)(B-3) |
| [INFO-058](../Information/2026-05-28/collected-raw.md#INFO-058) | DL 60%減少(1月20M→4月8.3M)・エンタープライズ苦戦(B-2) |
| [INFO-048](../Information/2026-05-22/collected-raw.md#INFO-048) | Pentagon代替AIモデルテスト・xAI参加(A-2) |
| [INFO-003](../Information/2026-05-15/collected-raw.md#INFO-003) | Colossus 1-Anthropic コンピューティング提携(220K+ GPU) |
