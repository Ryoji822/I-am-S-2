# Static Intelligence Update: 2026-04-19

## 更新判定: 更新あり（構造変化5件・鮮度タイムアウト1件）

### 更新したファイル

| ファイル | トリガー | 変更内容 |
|---------|---------|---------|
| `static_intelligence/openai.md` | フロンティアモデル新規リリース | GPT-Rosalind（ライフサイエンス特化、BixBench 0.751、人間専門家95%tile超え）を追加。Codex "for almost everything"アップデート・Agents SDK詳細を反映。H-OAI-001 61%・H-OAI-002 56%確認 |
| `static_intelligence/anthropic.md` | 主力製品発表 | Claude Design（Opus 4.7搭載ビジュアルデザインツール、Claude Code handoff）・Claude for Financial Services MCP統合・Agent SDK 12リリース/週詳細を追加。H-ANT-001 52→51%（$30B自己発表信頼性条件付き化）・H-ANT-002 71→70%（8R I=0）に更新 |
| `static_intelligence/google.md` | フロンティアモデル新規リリース + 主力製品発表 | Gemini 3.1 Flash TTS（Elo 1,211/70+言語）・Chrome Skills（ワンクリックツール化）・Grok on Vertex AI（競合モデル提供開始）を追加。H-GOO-001 57→55%・H-GOO-002 53→52%・H-GOO-003 54→53%に更新 |
| `static_intelligence/xai.md` | 主力製品発表 | Grok STT/TTS API（WER 6.9%競合最強・$4.20/1M文字・25+言語）・Grok on Vertex AI（4モデル提供開始）を追加。H-XAI-001 55→53%（17日+証拠不在）・H-XAI-003 52→50%（medium下限到達）に更新 |
| `static_intelligence/bytedance.md` | 鮮度タイムアウト（9日経過） | DeerFlow 2.0詳細（MIT OSS・LangGraph/LangChain・Dockerサンドボックス・MCP対応・Claude Code統合）を追加。H-BTD-001 66%・H-BTD-002 70%・H-BTD-003 40%確認（変更なし） |

### 更新しなかったファイル

| ファイル | 理由 |
|---------|------|
| `static_intelligence/market-overview.md` | 最終更新4/17（2日前）。シナリオ確率変更なし・順位変更なし。新製品は個別ファイルで対応済み。市場構造に変化なし |
| `static_intelligence/scenario-tracker.md` | 最終更新4/17（2日前）。シナリオ確率0件変更・順位変更なし。確率推移データへの追記不要 |

### 構造変化の判定根拠

1. **GPT-Rosalind**（OpenAI）: 新モデル名のフロンティアモデルリリース。「既存トレンドの延長」と分類してはならない（ルール明記）。BixBench 0.751で人間専門家95%tile超え。ドメイン特化2番目のモデル（Cyberに続く）
2. **Claude Design**（Anthropic）: 新製品発表。Opus 4.7搭載のビジュアルデザインツール。Claude Code handoff機能がエコシステム囲い込みの新たな接点
3. **Gemini 3.1 Flash TTS**（Google）: 新モデル名のリリース。Elo 1,211で音声生成首位。70+言語対応
4. **Chrome Skills**（Google）: 新製品機能。Geminiプロンプトのワンクリックツール化。配布戦略の新層
5. **Grok STT/TTS API**（xAI）: 新製品発表。WER 6.9%で音声認識首位。Tesla/Starlinkと同じオーディオスタック
6. **ByteDance**: 鮮度タイムアウト（9日）。DeerFlow 2.0新情報あり。事実再検証の結果、追加情報を反映
