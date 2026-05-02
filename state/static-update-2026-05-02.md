# Static Intelligence 更新判断: 2026-05-02

## 判定: 2ファイル更新

Arbiter v3.66の変更の中で、2つの構造変化トリガーが検出された。

## 更新トリガー評価

| トリガー | 評価 |
|----------|------|
| 仮説の新設・棄却・統合 | 該当なし（H-XAI-003のlow再分類は確度レベル変更であって棄却ではない） |
| シナリオ順位入れ替わり | 該当なし（SCN-002>003>001>004の順位不変） |
| 基本情報の事実変更 | **該当**: Pentagon 7社AI契約でAnthropic除外（INFO-030）→ anthropic.md更新 |
| フロンティアモデル新規リリース | **該当**: xAI Grok 4.3（常時推論・100万コンテキスト・$1.25/$2.50）→ xai.md更新 |
| I&W指標critical到達/high接近80% | 該当なし（全7指標状態変更なし） |
| Arbiter明示的更新指示 | なし |
| 鮮度タイムアウト（7日） | 該当なし（最長5日: xAI、04-27更新） |

## 更新内容

### xai.md — 更新

**トリガー**: フロンティアモデルの新規リリース（Grok 4.3、INFO-006）

主な変更:
- Grok 4.3（常時推論・100万コンテキスト・$1.25/$2.50・GDPval-AA Elo 1500・CaseLaw v2 #1・CorpFin #1・Custom Voices API）を全面反映
- H-XAI-001: 45→42%（29日+証拠不在、あと2%でlow再分類）
- H-XAI-003: 42→40% low再分類実施
- Pentagon 7社契約でSpaceX選出（INFO-030）を追加
- DeepSeek V4価格競合（INFO-036）を脅威に反映

### anthropic.md — 更新

**トリガー**: 基本情報の事実変更（Pentagon 7社契約でAnthropic除外、INFO-030）

主な変更:
- Pentagon 7社契約・Anthropic除外（SpaceX/OpenAI/Google/NVIDIA/MSFT/AWS/Reflection AI）を政府対立セクションに追加
- DC回路裁判所「chilling effect」支持・White House軟化兆しを反映
- $30B ARR公式確認（INFO-043）・Claude Code $2.5Bランレート（INFO-002）を反映
- H-GOV-001: 44→45%（+1%）
- Claude Code 50万行ソース漏洩（INFO-049）・トークナイザー47%値上げ（INFO-037）を弱みに追加
- Google従業員600+抗議（INFO-031）を反映

### 更新なしのファイル

| ファイル | 理由 |
|---------|------|
| openai.md | 新規リリースなし（GPT-5.5は既に反映済み、o4 Enterpriseは既存モデルのエンタープライズ版） |
| google.md | 新規リリースなし（Gemini 3.1 Pro SWE-bench首位はC-3信頼性で構造変化非該当） |
| bytedance.md | 新規リリースなし（豆包1.8は既に反映済み） |
| market-overview.md | 価格二極化・エンタープライズ実行ギャップは既に反映済み |
| scenario-tracker.md | シナリオ順位不変（SCN-002 -1%・SCN-003 +1%は順位を変えない変動） |

## 各ファイルの鮮度

| ファイル | 最終更新 | 経過日数 | タイムアウト |
|---------|---------|---------|------------|
| anthropic.md | **2026-05-02** | 0日 | なし |
| openai.md | 2026-04-29 | 3日 | なし |
| google.md | 2026-04-29 | 3日 | なし |
| xai.md | **2026-05-02** | 0日 | なし |
| bytedance.md | 2026-04-29 | 3日 | なし |
| market-overview.md | 2026-04-29 | 3日 | なし |
| scenario-tracker.md | 2026-04-29 | 3日 | なし |
