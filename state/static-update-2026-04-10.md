# Static Intelligence 更新記録: 2026-04-10

## 更新判定

**更新あり**（4ファイル更新、3ファイル更新なし）

## 更新したファイル

### 1. static_intelligence/anthropic.md
**トリガー**: 基本情報の事実変更（SCR連邦控訴裁敗訴で確定・$30B ARR自己発表）+ 製品発表（Managed Agents GA）+ インフラ変更（Google/Broadcom複数GW TPU契約）

**変更内容**:
- 政府との対立セクション: 4/8連邦控訴裁敗訴（SCR確定）・DOD「全合法目的での無制限アクセス」要求・OpenAI $200M契約獲得・小規模AI企業参入加速を追加。対立の「構造化完了」を記録
- 基本情報: ARRを$14B→$30Bに更新（自己発表・第三者検証未完了を明記）。Google/Broadcom複数GW TPU契約・$1M+顧客1000社突破を追加
- 製品: Managed Agents GA（4/8）・Glasswing脆弱性検出閾値到達を追加
- セキュリティ課題: Claude Codeソース流出（512,000行）を追加
- 仮説: H-ANT-002 70%→71%（Managed Agents GA）、H-ANT-003 10%→8%（GCP依存深化）に更新
- 監視ポイント: SCR確定・$30B ARR検証・Managed Agents採用データ・Google/Broadcom TPU影響を更新

### 2. static_intelligence/bytedance.md
**トリガー**: 新モデルリリース（Seeduplex・豆包大モデル 1.8）+ 仮説確度変更（H-BTD-001 64%→66%、H-BTD-002 69%→70%、H-BTD-003 41%→39%）

**変更内容**:
- 製品: Seeduplex（原生全二重音声モデル・豆包App全量ローンチ）・豆包大モデル 1.8（マルチモーダルAgent最適化）を追加
- 仮説: H-BTD-001 64%→66%、H-BTD-002 69%→70%、H-BTD-003 41%→39%に更新
- 強み: Seeduplexによる音声AIの質的転換を追加

### 3. static_intelligence/market-overview.md
**トリガー**: 企業基本情報変更（Anthropic $30B ARR）+ 政府介入の構造化完了 + Meta台頭 + 囲い込みの定量証拠

**変更内容**:
- プレイヤー表: Anthropic $30B ARR（自己発表）・Managed Agents GA・SCR確定・Google/Broadcom TPU契約を更新。Meta行を追加（スーパーインテリジェンスチーム+$21B CoreWeave）。OpenAI IPO枠・英国DC一時停止・ChatGPT Pro $100/月を追加
- 囲い込み定量化セクション新設: スイッチングコスト15-20%・74%ベンダー依存・価格上昇15-22%・DeepSeek V3.2の700分の1コストを追加
- Q1 2026 AI投資$221B（6x YoY）を追加
- AAIF 170+メンバーに更新
- I&W指標: IND-028/029新規追加。IND-013/023/027を更新
- シナリオ確率: SCN-002 38%→36%、SCN-003 27%→28%、SCN-004 12%→13%

### 4. static_intelligence/scenario-tracker.md
**トリガー**: 確率データ更新 + SCN-003の新規定量証拠

**変更内容**:
- 確率表: SCN-002 38%→36%（-2%）、SCN-003 27%→28%（+1%）、SCN-004 12%→13%（+1%）に更新
- SCN-003セクション: スイッチングコスト4つの定量証拠を追加（15-20%・74%・価格上昇15-22%・コンテキスト蓄積）
- SCN-004セクション: OSS性能ギャップ閉鎖（Veracity AI）・DeepSeek V3.2を追加
- 確率推移データ: 2026-04-10行を追加

## 更新しなかったファイル

### static_intelligence/openai.md
**理由**: 構造変化トリガーなし。H-OAI-001 62%→60%（±10%以内）・H-OAI-002 57%→56%（±10%以内）。新モデルリリースなし。Codex価格変更・ChatGPT Pro $100/月は製品マイナーアップデート。最終更新から3日（鮮度タイムアウトなし）

### static_intelligence/google.md
**理由**: 構造変化トリガーなし。全仮説±0%。新モデルリリースなし。Gemini API Docs MCP・Colab Learn Mode・3D可視化は製品マイナーアップデート。最終更新から4日（鮮度タイムアウトなし）

### static_intelligence/xai.md
**理由**: 構造変化トリガーなし。H-XAI-001 62%→60%（時間減衰のみ）。新規証拠なし。最終更新から2日（鮮度タイムアウトなし）

## 判断根拠

本日の更新は以下の構造変化に基づく:
1. **SCR連邦控訴裁敗訴**（INFO-035/036）— 政府-企業対立の構造化完了（Arbiter v3.46所見）
2. **Anthropic $30B ARR自己発表**（INFO-001）— 基本情報の事実変更（第三者検証未完了につき注記付き）
3. **Seeduplex新モデルローンチ**（INFO-056）— 新モデル名を伴う製品発表
4. **Managed Agents GA**（INFO-078）— 製品発表
5. **スイッチングコスト定量データ**（INFO-089/097）— SCN-003の4前提を支持する新規構造的証拠
