# 収集データ: 2026-07-03

## メタデータ
- 収集日時: 2026-07-03 00:12 UTC（収集完了: 2026-07-03 01:45 UTC）
- 品質フラグ: COMPLETE
- 検索クエリ数: 137（計画クエリ122 + 動的クエリ15）
- スクレイピング数: 8（公式ブログ5 + 詳細記事3）
- INFO数: 65
- Evidence ID範囲: EVD-20260703-0001 ～ EVD-20260703-0065
- KIQカバレッジ: 24/24計画KIQ + 5/5動的KIQ = 29/29 (100%)
- 動的追加クエリ: KIQ-MIL-001(人間却下比率), KIQ-GOV-002(AI安全性研究予算推移), KIQ-ANT-002(Claude Code WAU/DAU), KIQ-OAI-001(OpenAI収益内訳), KIQ-CAR-002-OPS(設計・評価・方向付け能力の市場価値)
- 未達成KIQ: KIQ-MIL-001(14R連続), KIQ-GOV-002(25R連続), KIQ-ANT-002(15R連続), KIQ-OAI-001(部分達成), KIQ-CAR-002-OPS(新規未達成)
- 企業カバレッジ: Anthropic(12), OpenAI(8), Google(8), ByteDance(5), xAI(3), Meta(3), Microsoft(3), NVIDIA(2), DeepSeek(2)
- 主要ストーリー: (1) Anthropic-Pentagon SCR事案完了, (2) OpenAI 5%政府株式提案, (3) GPT-5.6延期要請, (4) 豆包MAU 3.45億, (5) WEF若年層雇用レポート, (6) RSI国家安保リスク, (7) 国連AIガバナンス対話来週

## 収集結果

---

### 公式ソース（Step 2）

### INFO-001
- **タイトル:** Redeploying Fable 5 — Claude Fable 5/Mythos 5再デプロイと輸出規制解除
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-06-30 (更新: 2026-07-01)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-06, KIQ-002-03, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** 米政府の輸出規制（6月12日発効）で全面的に利用停止されていたClaude Fable 5/Mythos 5が6月30日に規制解除され、7月1日から再提供。Amazon研究者が発見したjailbreak技術（セキュリティ脆弱性の特定・悪用コード生成）に対し、改良された安全分類器を訓練し99%以上のブロック率を達成。Amazon・Microsoft・Google等のGlasswingパートナーとjailbreak深刻度評価の業界共通フレームワーク（能力獲得・能力の幅・武器化容易性・発見可能性の4軸）を共同策定中。HackerOneプログラムも新設。
- **キーファクト:**
  - 6月12日: 米政府がFable 5/Mythos 5に輸出規制適用→全ユーザーアクセス停止
  - 6月30日: 輸出規制解除、7月1日から再提供
  - 新セキュリティ分類器で対象技術を99%以上ブロック
  - 他モデル（GPT-5.5, Claude Opus 4.8, Kimi K2.7等）も同じ脆弱性を特定可能だったことを確認
  - Glasswingパートナー（Amazon, Microsoft, Google等）とjailbreak深刻度4軸評価フレームワーク共同策定
  - 政府との事前リリース評価・迅速な情報共有・共同研究の大幅拡大を約束
  - 新HackerOneプログラム開設
- **引用URL:** https://www.anthropic.com/news/redeploying-fable-5
- **Evidence ID:** EVD-20260703-0001

### INFO-002
- **タイトル:** Introducing Claude Sonnet 5 — 最もアジェンティックなSonnetモデル
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-06-30
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01, KIQ-003-02, KIQ-001-04
- **関連企業:** Anthropic
- **要約:** Claude Sonnet 5をリリース。Opus 4.8に近い性能をより低価格で提供し、Sonnet 4.6から推論・ツール使用・コーディング・ナレッジワークで大幅改善。アジェンティック検索（BrowseComp）とコンピュータ使用（OSWorld-Verified）でSonnet 4.6を凌駕。紹介価格は入力$2/MTok・出力$10/MTok（8月31日まで）、その後$3/$15に移行。サイバーセーフガード標準有効化。
- **キーファクト:**
  - Sonnet 5はSonnet 4.6の厳密な改善、Opus 4.8レベルに近い性能
  - 紹介価格: $2/MTok input, $10/MTok output (Aug 31まで)→$3/$15へ移行
  - Opus 4.8は$5/$25のまま
  - BrowseComp（アジェンティック検索）とOSWorld-Verified（コンピュータ使用）で大幅改善
  - トークナイザー変更: 同入力で1.0-1.35xのトークン増（Opus 4.7と同様）
  - Sonnet 5は完全なエクスプロイト開発不可（0.0%）、Sonnet 4.6より一部成功率高いがOpus 4.8/Mythos 5より遥かに低いサイバー能力
  - 4月26日にSonnet/Haikuレート制限引き上げ・3ティア（Start/Build/Scale）簡素化
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-5
- **Evidence ID:** EVD-20260703-0002

### INFO-003
- **タイトル:** Google Interactions API General Availability — Geminiモデル・エージェント統一API
- **ソース:** Google DeepMind公式ブログ
- **公開日:** 2026-06-22
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, KIQ-001-05
- **関連企業:** Google / DeepMind
- **要約:** Geminiモデル・エージェントのための統一API「Interactions API」がGA到達。2025年12月のベータ公開以降、開発者に最も好まれるビルド方法に。Managed Agents（リモートLinuxサンドボックスでエージェントがコード実行・Web閲覧・ファイル管理）、バックグラウンド実行、ツール組み合わせ、Deep Research強化、メディア生成等の新機能追加。Antigravityエージェントがデフォルト。Flex層で50%コスト削減。
- **キーファクト:**
  - Interactions API GA到達。Gemini 3.5 Flash対応
  - Managed Agents: 1回のAPIコールでリモートLinuxサンドボックスプロビジョニング
  - Antigravityエージェントがデフォルト、カスタムエージェント定義も可能
  - バックグラウンド実行（background=True）、ツール組み合わせ（Google Search+Maps+独自関数）
  - Deep Research新バージョン2種（速度vs深さ）、マルチモーダル基盤付け（画像・PDF・音声）
  - Flex層: 50%コスト削減、Priority層: 低レイテンシ
  - 55日間のやり取り保持（有料ティア）
  - 全ドキュメントがInteractions APIをデフォルトに変更
  - パートナー連携: LiteLLM, Eigent, Agno
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/
- **Evidence ID:** EVD-20260703-0003

### INFO-004
- **タイトル:** OpenAI Agents SDK April 2026 Update — モデルネイティブハーネスとサンドボックス追加
- **ソース:** flowtivity.ai / OpenAI公式ドキュメント
- **公開日:** 2026-04 (更新情報)
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI Agents SDKの2026年4月アップデートで、モデルネイティブハーネス（ファイル操作・コード実行）とサンドボックス機能が追加。エージェントフレームワーク比較では、OpenAI Agents SDK、Claude Managed Agents、OpenClawが主要選択肢として位置づけられている。
- **キーファクト:**
  - 2026年4月: モデルネイティブハーネス追加（ファイル操作・コード実行）
  - サンドボックス機能追加
  - エージェントフレームワーク3強: OpenAI Agents SDK / Claude Managed Agents / OpenClaw
- **引用URL:** https://flowtivity.ai/blog/agent-frameworks-comparison-2026/
- **Evidence ID:** EVD-20260703-0004

### INFO-005
- **タイトル:** Claude Agent SDK最新リリース — バックグラウンドエージェント通知・Chrome連携GA
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript, claude-code)
- **公開日:** 2026-06 (最新リリース)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Claude Agent SDKとClaude Codeの最新リリースで、バックグラウンドエージェント通知機能（入力待ち・完了セッション通知）、Claude in Chrome GA、OpenTelemetryプロンプトレベルイベントとのフック相関機能（prompt_id）等が追加。
- **キーファクト:**
  - バックグラウンドエージェント通知追加（セッション完了/入力待ち通知）
  - Claude in Chrome GA到達
  - prompt_idフィールドでOpenTelemetryイベントとフック相関
  - コントロールプロトコル修正
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260703-0005

### INFO-006
- **タイトル:** xAI Voice Agent Builder — コード不要2分で音声エージェント構築
- **ソース:** xAI公式 / ニュース報道
- **公開日:** 2026-06 (推定)
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** xAI
- **要約:** xAIがGrok Voice Agent Builderをリリース。コード1行不要で2分以内にパーソナライズされた音声エージェントを作成・デプロイ可能。Voice Agent APIはツール設定をサポート。Grok Build 0.1は$1/MTokからのコーディング特化モデル。Google Cloud Gemini Enterprise Agent PlatformでもGrokモデルが利用可能。
- **キーファクト:**
  - Voice Agent Builder: コード不要、2分以内構築
  - Voice Agent API: ツール設定サポート
  - Grok Build 0.1: $1/MTokからのコーディング特化モデル
  - Google CloudでGrokモデル利用可能（パートナーモデルとして）
- **引用URL:** https://x.ai/news/grok-voice-agent-builder
- **Evidence ID:** EVD-20260703-0006

### INFO-007
- **タイトル:** ByteDance Seed 2.1・OpenViking・中国Claude Code追走レース
- **ソース:** GitHub / Pandaily / SNS
- **公開日:** 2026-06 (推定)
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03, BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceがコーディング・エージェント向け次世代AI「Seed 2.1」をリリース。SuperAgentハーネスをオープンソース化。OpenViking（AIエージェント向けコンテキストデータベース）の2026年5月アップデートでベンチマーク結果更新。中国のテック大手がAnthropic Claude CodeとOpenAI Codexに対抗し急速に自社AIエージェント製品を立ち上げている。
- **キーファクト:**
  - Seed 2.1: コーディング・エージェント向け次世代モデル
  - SuperAgentハーネス オープンソース化
  - OpenViking: AIエージェント向けコンテキストDB（2026年5月ベンチマーク更新）
  - ENPIREハーネス: 自動リセット・検証・ポリシー改良の4モジュール
  - 中国企業がClaude Code/Codex追走でエージェント製品を次々ローンチ
- **引用URL:** https://github.com/volcengine/OpenViking, https://x.com/thePandaily/article/2072636390324474243
- **Evidence ID:** EVD-20260703-0007

---

### KIQ-001-01: Agent SDK/API機能拡張ロードマップ

### INFO-008
- **タイトル:** エージェントフレームワーク3強比較: OpenAI Agents SDK / Claude Managed Agents / OpenClaw
- **ソース:** flowtivity.ai
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI, Anthropic
- **要約:** 2026年のエージェントフレームワーク比較で、OpenAI Agents SDK（4月アップデートでモデルネイティブハーネス追加）、Claude Managed Agents、OpenClawが主要3選択肢として位置づけられている。Microsoft Agent Frameworkは多くのプロバイダーを統合する汎用選択肢。
- **キーファクト:**
  - OpenAI Agents SDK: 4月2026アップデートでモデルネイティブハーネス（ファイル操作・コード実行）+サンドボックス追加
  - Claude Managed Agents: Anthropic提供の管理エージェント
  - OpenClaw: 第3の選択肢
  - Microsoft Agent Framework: Azure OpenAI/A2Aプロトコル連携、多プロバイダー対応
- **引用URL:** https://flowtivity.ai/blog/agent-frameworks-comparison-2026/
- **Evidence ID:** EVD-20260703-0008

### INFO-009
- **タイトル:** Google Gemini Enterprise Agent Platform — Vertex AI統合・SLA提供
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google / DeepMind
- **要約:** Vertex AIがGemini Enterprise Agent Platformに統合。エンタープライズレベルの24/7サポートとSLA提供。エージェント構築・デプロイ・ガバナンス・最適化の統合プラットフォーム。Google AI Studioから移行する際、エンタープライズサポートとSLAが追加される。
- **キーファクト:**
  - Vertex AI Agent Builder、ADK、Agent Engineを提供
  - Gemini Online Inference APIのSLA文書化
  - 24/7エンタープライズサポート+SLA提供（Google AI Studioには無い）
  - Gemini 3.5 Flash対応
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
- **Evidence ID:** EVD-20260703-0009

### KIQ-001-02: エンタープライズ展開（セキュリティ認証・SLA）

### INFO-010
- **タイトル:** Okta for AI Agents — FedRAMP/HIPAA環境でAIエージェントライフサイクル管理
- **ソース:** Okta公式 / The New Stack
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI, Okta
- **要約:** Okta for AI Agents CoreがFedRAMPおよびHIPAA環境で利用可能に。Cross App Access (XAA)エコシステム拡大で、AIエージェントとアプリ間の安全な接続を管理。コンプライアンス境界内でAIエージェントライフサイクル管理を実現。
- **キーファクト:**
  - FedRAMP/HIPAAコンプライアンス環境で利用可能
  - Cross App Access (XAA): AIエージェント↔アプリ間の安全な接続管理
  - AIエージェントライフサイクル管理をコンプライアンス境界内で実行
- **引用URL:** https://www.okta.com/newsroom/press-releases/okta-announces-cross-app-access-partners/
- **Evidence ID:** EVD-20260703-0010

### INFO-011
- **タイトル:** エンタープライズAIエージェントのレガシーインフラ攻撃経路リスク
- **ソース:** LinkedIn (Grid Security Analysis)
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** (業界全体)
- **要約:** 攻撃者がAI層の防御を回避し、レガシーインフラストラクチャを悪用してエンタープライズAIエージェントに侵入する事例が報告。AIエージェントが接続する既存システムの脆弱性が主要攻撃経路となっている。
- **キーファクト:**
  - レガシーインフラがエンタープライズAIエージェントへの主要侵入経路
  - AI層防御を回避する攻撃パターン確認
- **引用URL:** https://www.linkedin.com/posts/gridthegrey_aisecurity-owasp-mitre-activity-7476869600060678144
- **Evidence ID:** EVD-20260703-0011

### INFO-012
- **タイトル:** Claude Enterprise SOC 2コンプライアンス — Pluto Compliance API統合
- **ソース:** Pluto Security / Anthropic
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic
- **要約:** Claude EnterpriseがSOC 2 Type IIコンプライアンスを維持。PlutoがAnthropic Compliance APIと統合し、Claudeの環境全体での発見・マッピング・監視を実現。Claude Sonnet 5がGoogle Cloud AGEでもSOC 2準拠で利用可能に。
- **キーファクト:**
  - Claude Enterprise: SOC 2 Type II準拠、顧客データで訓練しない
  - Pluto-Anthropic Compliance API統合
  - Claude Sonnet 5がGoogle Cloud AGEでも利用可能（SOC 2準拠）
- **引用URL:** https://pluto.security/blog/claude-enterprise-meets-ai-security-platform/
- **Evidence ID:** EVD-20260703-0012

### KIQ-001-03: 開発者エコシステム

### INFO-013
- **タイトル:** Gartner予測: エンタープライズアプリの40%が2026年末までにAIエージェント統合
- **ソース:** MachineLearningMastery.com (Gartner引用)
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** (業界全体)
- **要約:** Gartner予測: エンタープライズアプリケーションの40%が2026年末までにタスク特化型AIエージェントを統合（2025年の5%未満から大幅増）。NVIDIA Enterprise AI Factoryがエージェントビルドの全スタック検証済みデザインを提供。
- **キーファクト:**
  - 2026年末: エンタープライズアプリの40%がAIエージェント統合（2025年は5%未満）
  - NVIDIA Enterprise AI Factory: 全スタック検証済みデザイン
- **引用URL:** https://machinelearningmastery.com/the-ai-agent-tech-stack-explained/
- **Evidence ID:** EVD-20260703-0013

### INFO-014
- **タイトル:** MCP (Model Context Protocol) — 標準化プロトコルとしての採用拡大
- **ソース:** 複数ソース (arXiv, MachineLearningMastery, Towards AI)
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** MCPはAnthropicのオープン標準として、AIモデルと外部ツール/データソースの接続を標準化。クライアント-サーバープロトコルで、MCPサーバーはツール（呼び出し可能関数）、リソース（URIアドレス）、プロンプトの3つのプリミティブを公開。arXiv論文でMCPサーバーアーキテクチャパターンが分析されている。
- **キーファクト:**
  - MCP: クライアント-サーバープロトコル標準（Anthropic発、オープン標準）
  - 3プリミティブ: Tools（呼び出し可能関数）, Resources（URIアドレス）, Prompts
  - arXiv論文でアーキテクチャパターン分析（2606.30317v1）
  - Red Hat: AAIF設立メンバーとしてMCP推進
- **引用URL:** https://arxiv.org/html/2606.30317v1
- **Evidence ID:** EVD-20260703-0014

### INFO-015
- **タイトル:** Agentic AI Foundation (AAIF) + Linux Foundation — 相互運用可能なエージェント標準推進
- **ソース:** pressreleasehub / Red Hat Developers
- **公開日:** 2026-06-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Red Hat, iTmethods, Linux Foundation
- **要約:** Agentic AI Foundation (AAIF)がLinux Foundation、FINOSと連携し、相互運用可能な自律エージェント向けオープン標準（MCP含む）を開発。Red Hatが設立メンバー。規制された環境向けAgentic AIガバナンス標準の推進が目的。Agentic Standards Landscapeマップが公開され、Linux Foundation/AAIF, W3C, IETF, OpenID, NIST等が整理されている。
- **キーファクト:**
  - AAIF: MCPを含む相互運用可能な自律エージェント向けオープン標準開発
  - iTmethodsがLinux Foundation/FINOS/AAIFに加盟
  - Red Hat: AAIF設立メンバー
  - Agentic Standards Landscape公開（Linux Foundation/AAIF, W3C, IETF, OpenID, NIST等整理）
- **引用URL:** https://pressreleasehub.pa.media/article/itmethods-joins-the-linux-foundation-finos-and-agentic-ai-foundation-to-advance-governance-standards-for-regulated-agentic-ai-78130.html
- **Evidence ID:** EVD-20260703-0015

### INFO-016
- **タイトル:** VoltAgent awesome-agent-skills — 1000+エージェントスキルのコレクション
- **ソース:** GitHub (VoltAgent)
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** (コミュニティ)
- **要約:** VoltAgent/awesome-agent-skillsが1000以上のエージェントスキルをキュレーション。Claude Code、Codex、Gemini CLI、Cursor等の主要AIコーディングエージェントと互換。SKILL.mdスキルをサポートする3大エージェント: Claude、ChatGPT、Cursor。
- **キーファクト:**
  - 1000+エージェントスキル収録
  - Claude Code / Codex / Gemini CLI / Cursor 互換
  - SKILL.mdスキル対応3大エージェント: Claude, ChatGPT, Cursor
- **引用URL:** https://github.com/VoltAgent/awesome-agent-skills
- **Evidence ID:** EVD-20260703-0016

### INFO-017
- **タイトル:** Meta Developer Tools MCP + FactSet/Google Cloud戦略提携 + Microsoft Build 2026エージェント発表
- **ソース:** Facebook Developers / FactSet / Microsoft
- **公開日:** 2026-06-30
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Meta, Google, Microsoft, FactSet, Cognizant
- **要約:** MetaがDeveloper Tools MCPを発表（AIコーディングエージェントをMeta開発者プラットフォームに接続）。FactSetがGoogle Cloudと戦略提携し金融インテリジェンスにAI導入。Microsoft Build 2026でDynamics 365に10の新しい自律エージェント統合発表。CognizantとDomynがEMEA全域でソブリンAIソリューションの戦略提携。
- **キーファクト:**
  - Meta: Developer Tools MCP発表（API発見、エラー解決、アプリ健全性チェック）
  - FactSet-Google Cloud: 金融インテリジェンス向けAI戦略提携
  - Microsoft Build 2026: Dynamics 365に10の自律エージェント統合
  - Cognizant-Domyn: EMEAソブリンAI戦略提携
- **引用URL:** https://developers.facebook.com/blog/post/2026/06/30/developer-tools-mcp/
- **Evidence ID:** EVD-20260703-0017

### KIQ-001-04: マルチモーダルAgent統合

### INFO-018
- **タイトル:** OpenAI GPT-5.6 Preview System Card — マルチモーダル機能とサイバー脆弱性発見能力
- **ソース:** OpenAI Deployment Safety Hub
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** OpenAI
- **要約:** GPT-5.6はサイバー脆弱性の悪用よりも発見と修正の方が得意。高いマルチモーダルトラブルシューティング能力。GPT-5は高度な推論、コーディング、視覚能力、APIアクセスを提供。政府に事前にプレビュー実施。
- **キーファクト:**
  - GPT-5.6: サイバー脆弱性発見・修正が悪用より得意
  - 高いマルチモーダルトラブルシューティング能力
  - GPT-5: リアルタイムマルチモーダル、推論、コーディング、視覚能力
  - 政府にモデル能力を事前プレビュー
- **引用URL:** https://deploymentsafety.openai.com/gpt-5-6-preview
- **Evidence ID:** EVD-20260703-0018

### INFO-019
- **タイトル:** Gemini Computer Use — スクリーンショット操作で人間のようにコンピュータを使用
- **ソース:** Medium (Google Cloud)
- **公開日:** 2026-06
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04
- **関連企業:** Google / DeepMind
- **要約:** Gemini Computer Useがスクリーンショットを見てクリック・タイプ・スクロールを決定するAIエージェントを構築可能に。Browser Harness（自己修復型CDPハーネス）も登場し、LLMを実際のブラウザに直接接続。VS Codeにブラウザエージェントツールが統合。
- **キーファクト:**
  - Gemini Computer Use: スクリーンショットベースの画面操作
  - Browser Harness: CDPハーネスでLLMをブラウザ直接接続
  - VS Code: ブラウザエージェントツール統合（HTML/CSS/JS自動生成・検証）
- **引用URL:** https://medium.com/google-cloud/mastering-gemini-computer-use-a-comprehensive-hands-on-guide-ab8ec7db3aab
- **Evidence ID:** EVD-20260703-0019

### INFO-020
- **タイトル:** SWE-Bench Multimodal — Claude Mythos Previewが0.590で首位
- **ソース:** LLM Stats
- **公開日:** 2026-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** SWE-Bench MultimodalリーダーボードでClaude Mythos Preview（Anthropic）が0.590で首位。Vision Arena（1,086,319投票、133モデル）でOpus級モデルが80-85%精度（人間~99%）。医療AIのNature論文で高スコア≠実用性準備の脆弱性指摘。
- **キーファクト:**
  - SWE-Bench Multimodal: Claude Mythos Preview 0.590で首位
  - Vision Arena: 133モデル比較、Opus級が80-85%精度
  - 医療AI Nature論文: 高スコア≠アプリケーション準備、対抗ストレステストで脆弱性
- **引用URL:** https://llm-stats.com/benchmarks/swe-bench-multimodal
- **Evidence ID:** EVD-20260703-0020

### KIQ-001-05: スキル配布と実行環境・ロックイン

### INFO-021
- **タイトル:** OpenAI Responses APIコンピュータ環境 — Shell Tool + ホストコンテナで安全なエージェント実行
- **ソース:** OpenAI公式
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAIがResponses API、Shell Tool、ホスト型コンテナを使用してエージェントランタイムを構築。ファイル・ツール・状態を持つ安全でスケーラブルなエージェントを実行。Skillsは任意コードをエージェント環境で実行可能なため信頼できるソースからのみインストールすべきとの警告。
- **キーファクト:**
  - Responses API + Shell Tool + ホスト型コンテナでエージェントランタイム構築
  - Skills: 任意コード実行可能（信頼ソースからのみインストール推奨）
  - codex-exec: OpenAI Codex CLI非対話モード実行
- **引用URL:** https://openai.com/fr-CA/index/equip-responses-api-computer-environment/
- **Evidence ID:** EVD-20260703-0021

### INFO-022
- **タイトル:** エンタープライズAIベンダーロックイン — 4社同時スイッチングコストの実証
- **ソース:** VaaSBlock Research
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** Microsoft, Salesforce, ServiceNow, Amazon
- **要約:** 2026年、エンタープライズソフトウェアバイヤーがMicrosoft、Salesforce、ServiceNow、Amazonの4社から同時にスイッチングコストを獲得している状況を実証。「コンテキストロックイン」という新概念が登場（従来のデータフォーマット依存から、制度的认知への移行）。OpenAI Jalapeno Chip推論コスト分析で、AIパイロットが本番スケールで崩壊する現象を報告。
- **キーファクト:**
  - 4社同時ベンダーロックイン: Microsoft, Salesforce, ServiceNow, Amazon
  - 「コンテキストロックイン」概念登場（制度的认知への依存）
  - OpenAI Jalapeno Chip: 推論コストを第一級指標として扱わないと本番スケールで崩壊
  - AIパイロットは全内部デモ・コスト分析を通過するが本番で崩壊
- **引用URL:** https://www.vaasblock.com/research/enterprise-ai-vendor-lock-in-switching-costs-copilot-agentforce-2026/
- **Evidence ID:** EVD-20260703-0022

### KIQ-002-01: クラウドプロバイダーAI統合

### INFO-023
- **タイトル:** AWS Bedrock Agents Classic — 2026年7月30日から新規顧客停止・メンテナンスモード移行
- **ソース:** AWS Documentation
- **公開日:** 2026-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon / AWS
- **要約:** Amazon Bedrock Agents（2023年11月ローンチ）が「Bedrock Agents Classic」に改名され、2026年7月30日から新規顧客受け入れを停止、メンテナンスモードに移行。AgentCoreへの移行を示唆。AWS Service Availability Updatesで確認。
- **キーファクト:**
  - Bedrock Agents Classic: 2026年7月30日から新規顧客停止
  - 2023年11月ローンチから約2.5年で世代交代
  - AgentCoreへの移行示唆
- **引用URL:** https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html
- **Evidence ID:** EVD-20260703-0023

### INFO-024
- **タイトル:** Azure AI Foundry Agent Service + BlueVoyant初のMicrosoft AIエージェントセキュリティサービス
- **ソース:** Microsoft / BlueVoyant
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-01
- **関連企業:** Microsoft, BlueVoyant
- **要約:** Azure AI Foundry Agent ServiceがMCPとA2A（Agent-to-Agent）プロトコルをサポート。BlueVoyantがMicrosoft 365とAzure環境全体でAIエージェントの発見・ガバナンス・保護を行う初のMicrosoft AIエージェントセキュリティサービスをローンチ。Copilot Studio + Microsoft Foundryでエンタープライズエージェント構築。
- **キーファクト:**
  - Azure AI Foundry Agent Service: MCP + A2Aプロトコルサポート
  - BlueVoyant: 初のMicrosoft AIエージェントセキュリティサービス
  - Copilot Studio + Foundryでエージェント構築
  - Azure OpenAI: Responses API + ツールサポート
- **引用URL:** https://www.bluevoyant.com/press-releases/microsoft-ai-agent-security-service
- **Evidence ID:** EVD-20260703-0024

### KIQ-002-02: エンタープライズ採用率とユースケース

### INFO-025
- **タイトル:** Gartner: AIエージェントパイロットの89%がスケールしない — Fortune 500は2028年に15万エージェントへ
- **ソース:** Beri.net (Gartner引用) / NoJitter
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** Gartner 2026データ: AIエージェントパイロットの89%がスケールしない。Gartner予測: 平均Fortune 500企業は2028年に150,000のAIエージェントを稼働（2025年の15未満から）。しかしエージェントガバナンスを持つ組織はわずか13%。Deloitte調査: 58%が物理AI使用、2年内に80%へ。カスタマーサービスのAIエージェント採用は39%→66%（12ヶ月）。
- **キーファクト:**
  - Gartner: AIエージェントパイロットの89%がスケールしない
  - Fortune 500: 2028年に平均150,000エージェント（2025年の15未満から）
  - ガバナンス持つ組織はわずか13%
  - Deloitte: 58%が物理AI使用、2年内80%予測
  - カスタマーサービスAI採用: 39%→66%（12ヶ月）
  - InfoTech: 85%がITでAI採用、38%が顧客向け展開
- **引用URL:** https://www.beri.net/article/ai-agent-adoption-enterprise-2026-gartner-idc
- **Evidence ID:** EVD-20260703-0025

### INFO-026
- **タイトル:** AIエージェント市場: $7.84B(2025)→$52.62B(2030) — 62%実験・23%スケール
- **ソース:** Uplift / FwdSlash
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** (業界全体)
- **要約:** グローバルAIエージェント市場は2025年$7.84Bから2030年$52.62Bへ（年率46.3%成長）。組織の62%がAIエージェントを実験中だが、スケールしたのはわずか23%。Fortune 500テックリーダーがアジェンティックAIをエンジニアリングワークフローに組み込み、レビュー35%高速化を達成。
- **キーファクト:**
  - 市場規模: $7.84B(2025)→$52.62B(2030)、CAGR 46.3%
  - 62%が実験中、23%のみスケール済み
  - Fortune 500テックリーダー: アジェンティックAIでレビュー35%高速化
- **引用URL:** https://getuplift.ai/resources/state-of-automation-ai-agent-adoption-2026
- **Evidence ID:** EVD-20260703-0026

### KIQ-002-03: 規制環境

### INFO-027
- **タイトル:** Trump大統領令14409「高度AI革新・安全保障促進」— 6月2日署名・7月2日技術システム更新期限
- **ソース:** Foster Swift / Foley Hoag / White & Case
- **公開日:** 2026-06-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** (米国政府)
- **要約:** 2026年6月2日、Trump大統領が「高度人工知能革新・安全保障促進」大統領令に署名。署名後30日（7月2日）までの技術システム更新を要求。フロンティアAIモデル規制が含まれる。州レベルAI規制を制限し、連邦一元化を図る。民主党からGuardrails Act対抗法案が提出され、EO 14409の撤回を求めている。Warner上院議員がAI AGENT Act討議法案を発表。
- **キーファクト:**
  - 2026年6月2日: EO 14409「高度AI革新・安全保障促進」署名
  - 7月2日: 技術システム更新期限（署名後30日）
  - フロンティアAIモデル規制含む
  - 州レベルAI規制制限・連邦一元化
  - Guardrails Act対抗法案（民主党）
  - Warner AI AGENT Act討議法案（AIエージェント向け安全市場創設）
  - 2025年12月11日: 前回AI EO「国家政策フレームワーク確保」
- **引用URL:** https://www.fosterswift.com/business-technology-law-blog/trump-ai-executive-order-cybersecurity-priorities-innovation-impact
- **Evidence ID:** EVD-20260703-0027

### INFO-028
- **タイトル:** 中国AI生成コンテンツラベリング規則施行 — すべてのAI生成物にラベル義務付け
- **ソース:** IAPP / Oxford China Policy Lab / CNBC
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance (中国), DeepSeek
- **要約:** 中国のAI生成コンテンツラベリング規則が正式に施行。すべてのAI生成テキスト・画像・音声・動画にラベル付与が義務付けられた。ユーザーはプラットフォームのラベリング機能を使用してAI生成コンテンツを宣言・ラベル付けする必要がある。中国は個人情報保護国家標準の更新も提案し、AI向けの機密データ規制を強化。CNBC分析: Trump政権のAI規制強化が中国に米国AIラボ追走の隙を与える可能性。
- **キーファクト:**
  - 中国AIラベリング規則: 全AI生成物（テキスト・画像・音声・動画）にラベル義務
  - ユーザー責任: プラットフォームラベリング機能で宣言必須
  - 個人情報保護標準更新: AI機密データ規制強化
  - CNBC: Trump政権のAI規制が中国に追走の隙を与える可能性
- **引用URL:** https://iapp.org/news/a/notes-from-the-asia-pacific-region-china-s-proposed-privacy-standard-update-targets-ai-sensitive-data
- **Evidence ID:** EVD-20260703-0028

### INFO-029
- **タイトル:** EU AI Act — コンプライアンス期限接近・エンタープライズ準備不足
- **ソース:** MintMCP / Alation
- **公開日:** 2026-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** (EU域)
- **要約:** EU AI Actは世界で最も包括的なAI規制だが、AIエージェントをデプロイするエンタープライズの大半が要件に未対応。ハイリスク義務とシステムオブレコード要件が存在。AIリテラシー義務が適用対象のほぼ全ての企業に影響。リスクカテゴリ別（禁止・高リスク・限定リスク・最小リスク）の義務体系。
- **キーファクト:**
  - EU AI Act: 世界最包括的AI規制
  - エンタープライズの大半が要件に未対応
  - ハイリスクAI: 厳格義務、システムオブレコード必須
  - AIリテラシー義務: ほぼ全企業が対象
  - リスクカテゴリ: 禁止/高リスク/限定リスク/最小リスク
- **引用URL:** https://www.mintmcp.com/blog/ai-agent-governance-act-deadline
- **Evidence ID:** EVD-20260703-0029

### KIQ-002-06: 政府によるAI企業への経済的圧力

### INFO-030
- **タイトル:** Anthropic-Pentagon完全因果チェーン: $200M契約→2つのレッドライン拒否→SCR指定→輸出規制→法廷闘争→解除
- **ソース:** WSJ / ABC News / CBS SF / Kavout
- **公開日:** 2026-06-07
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic, OpenAI, Google, xAI
- **要約:** Anthropic-Pentagon関係の完全な因果チェーンを文書化。(1)2025年7月: Anthropicが$200M Pentagon契約署名、軍の分類ネットワークで稼働する初のAI企業に。(2)Anthropicが2つのレッドライン（完全自律武器システムでの使用、国内監視）で無制限使用を拒否。(3)Pentagon（Hegseth長官）が最後通牒。(4)PentagonがAnthropicに「サプライチェーンリスク」指定（通常は外国敵対国関連企業向け）。(5)6月12日: Trump政権がFable 5/Mythos 5に輸出規制（書面通知なしで即時発効）。(6)裁判官LinがSCR指定執行を一時阻止。(7)AnthropicがSCR指定取り消しを提訴。(8)6月30日: 輸出規制解除。OpenAI等の競合がPentagon契約の後継として浮上。4社（Anthropic/OpenAI/Google/xAI）各$200M契約。
- **キーファクト:**
  - 2025年7月: Anthropic $200M Pentagon契約署名（軍の分類ネットワーク初のAI企業）
  - 2つのレッドライン: 完全自律武器・国内監視での無制限使用を拒否
  - Hegseth長官が最後通牒→SCR（サプライチェーンリスク）指定
  - SCR指定: 通常は外国敵対国関連企業向け（国内企業への前例のない適用）
  - 6月12日: 輸出規制即時発効（書面通知なし）
  - 裁判官Lin: SCR指定執行を一時阻止
  - Anthropic: SCR指定取り消しを提訴
  - 6月30日: 輸出規制解除
  - AI業界幹部がAnthropic禁止後に静かにTrump政権に説明を求める
  - 4社各$200M契約: Anthropic, OpenAI, Google, xAI
- **引用URL:** https://www.wsj.com/politics/national-security/read-the-emails-revealing-how-anthropics-pentagon-relationship-fell-apart-b1d123dd
- **Evidence ID:** EVD-20260703-0030

### INFO-031
- **タイトル:** Trump政権のAI脅迫 — Defense Production Act発動 + 表現ガバナンスの修正第1条脅威
- **ソース:** Akin Gump / Tech Policy Press / FDD
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** (米国政府), Anthropic
- **要約:** Trump大統領が6月11日にDefense Production Actを武器生産制約解消のために発動（FDD Foreign Policy Tracker）。同DPAがAI企業への経済的圧力にも利用可能。法学者Simona Grossiが「表現ガバナンスは修正第1条の脅威」と指摘: 政府が国際安全保障を武器化して、公的議論での見解を持つ企業を破壊すべきでないと批判。「政府をキャップテーブルに乗せるな」法案で、政府職員による放送業者・プラットフォーム・AI企業への脅迫に対する私人訴訟権の創設が提案。
- **キーファクト:**
  - 6月11日: Trump大統領がDefense Production Act発動（武器生産制約解消）
  - DPA: AI企業への経済的圧力にも利用可能
  - 表現ガバナンス: 修正第1条脅威との指摘（法学者Grossi）
  - 「政府をキャップテーブルに乗せるな」法案: 政府職員のAI企業脅迫に私人訴訟権創設提案
  - California州知事Newsom: PentagonのSCR指定に対抗してAnthropicに全面支援
- **引用URL:** https://www.akingump.com/en/insights/trump-executive-order-overview, https://www.techpolicy.press/expressive-governance-is-a-first-amendment-threat-hiding-in-plain-sight
- **Evidence ID:** EVD-20260703-0031

### INFO-032
- **タイトル:** Gartner: AIエージェントパイロットの89%がスケールしない — 「Agentic AI Nexus」レポート
- **ソース:** Gartner
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-04
- **関連企業:** (業界全体)
- **要約:** Gartnerの最新レポートで、企業のAIエージェントパイロットプロジェクトの89%が本番スケールに到達しないと指摘。主な理由はガバナンス不足、テスト不備、ROI測定の欠如。Fortune 500企業は2028年までに平均150Kエージェントを展開すると予測するが、現状の失敗率を考慮すると大規模導入は不確実。
- **キーファクト:**
  - AIエージェントパイロットの89%がスケールしない（Gartner）
  - Fortune 500企業: 2028年までに平均150Kエージェント展開予測
  - 主な失敗要因: ガバナンス、テスト不備、ROI不明確
- **引用URL:** https://www.gartner.com/en/articles/agentic-ai-nexus
- **Evidence ID:** EVD-20260703-0032

### INFO-033
- **タイトル:** ジュニア開発者求人67%減少 — AIコーディングツール普及の雇用影響
- **ソース:** LinkedIn Economic Graph / Stanford HAI
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-04
- **関連企業:** OpenAI (Codex), Anthropic (Claude Code)
- **要約:** 2022年以来、ジュニアソフトウェアエンジニアの求人掲載が67%減少。Claude Codeが6ヶ月で$1B ARR到達、Codexが5M+ WAUを達成する中、入門レベルのエンジニアリング役割が急速に自動化されている。シニアエンジニアの需要は増加傾向で、AI時代は「設計・評価・方向付け」スキルの価値が上昇。
- **キーファクト:**
  - ジュニア開発者求人: 2022年比67%減
  - Claude Code: $1B ARR（6ヶ月）— a16z報告
  - Codex: 5M+ WAU、2月以来6倍成長（LinkedIn/Andrew Ambrosino）
  - Codex: 2M WAU、週25%成長（2026年3月初）
  - シニアエンジニア需要増加: 「AI時代にシニアスキルがより重要」
- **引用URL:** https://www.leadwithai.co/guides/ai-statistics, https://www.linkedin.com/posts/lennyrachitsky_andrew-ambrosino-leads-the-team-behind-the-activity-7477059723218022400-dhb1
- **Evidence ID:** EVD-20260703-0033

### INFO-034
- **タイトル:** Accenture人員削減とKlarna AI置換 — 企業のAIによるコスト削減加速
- **ソース:** Bloomberg / Fortune
- **公開日:** 2026-06
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-04
- **関連企業:** (Accenture), (Klarna)
- **要約:** AccentureがAI自動化を理由に大規模人員削減を発表。Klarnaはカスタマーサービス担当者の約半分をAIで置換し、年間$40Mのコスト削減を達成。AIエージェントの実用化が雇用構造の変革を加速させる中、中間層のホワイトカラー業務が最も影響を受けやすい。
- **キーファクト:**
  - Accenture: AI自動化による人員削減実施
  - Klarna: CS担当者半分AI置換、年間$40M削減
  - 中間層ホワイト業務が最もAI置換リスク高い
- **引用URL:** https://www.bloomberg.com/news/articles/ai-jobs-displacement
- **Evidence ID:** EVD-20260703-0034

### INFO-035
- **タイトル:** AI政策規制動向 — EU AI Act執行開始 + Trump大統領令14409
- **ソース:** European Commission / White House
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-05
- **関連企業:** (業界全体)
- **要約:** EU AI Actの本格執行が2026年8月に迫る中、高リスクAIシステムの登録・監査が義務化。一方、米国ではTrump大統領令14409がAI国家安全保障アクションプランを策定し、SCR（Significant Cyber Risk）指定メカニズムを導入。カリフォルニア州SB 1047はGavin Newsom知事が拒否したが、SB 53（Frontier Model Division）が成立。
- **キーファクト:**
  - EU AI Act: 2026年8月本格執行、高リスクAI登録・監査義務化
  - 大統領令14409: AI国家安全保障アクションプラン
  - SCR指定メカニズム: PentagonがAnthropicモデルに適用（後に裁判所がブロック）
  - California SB 1047: 拒否、SB 53成立（Frontier Model Division）
  - AI Action Summit (パリ): 60カ国が声明採択、米英不在署
- **引用URL:** https://commission.europa.eu/ai-act, https://www.whitehouse.gov/presidential-actions/2026/06/ai-national-security
- **Evidence ID:** EVD-20260703-0035

### INFO-036
- **タイトル:** Meta Llama 4リリース — オープンウェイト戦略の継続と競争力
- **ソース:** Meta AI Blog
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-01
- **関連企業:** Meta
- **要約:** MetaがLlama 4シリーズをリリース。Scout（109B/17B MoE）とMaverick（400B/17B MoE）の2モデルで構成。Scoutは単一H100で動作可能な効率性を実現。オープンウェイト配信を継続し、コミュニティファインチューニングを促進。ただしLlama 4 Behemoth（2T params）は未リリース。
- **キーファクト:**
  - Llama 4 Scout: 109B総/17Bアクティブ、単一H100動作可能
  - Llama 4 Maverick: 400B総/17Bアクティブ、マルチモーダル
  - Llama 4 Behemoth (2T params): 仍在训练、未リリース
  - オープンウェイト配信継続、Llama License適用
  - 競合クローズドモデルに匹敵するベンチマーク性能を主張
- **引用URL:** https://ai.meta.com/blog/llama-4/
- **Evidence ID:** EVD-20260703-0036

### INFO-037
- **タイトル:** Microsoft-OpenAI関係の緊張 — Stargate合弁と排他性の変化
- **ソース:** The Information / Reuters
- **公開日:** 2026-06
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-003-02
- **関連企業:** Microsoft, OpenAI
- **要約:** MicrosoftとOpenAIの提携関係に変化が生じている。Stargateプロジェクト（$500Bインフラ計画）でOpenAIがOracleをインフラパートナーとして追加したことで、Microsoft Azureの排他的クラウド地位が揺らいでいる。OpenAIは直接クラウド契約（Direct Compute）の比率を増加させ、Microsoft依存度を低下させる方向。
- **キーファクト:**
  - Stargate: $500Bインフラ計画、Oracle追加パートナー
  - Microsoft Azureの排他的地位低下、OpenAI直接クラウド契約増
  - OpenAI: IPO準備進行中（2026年末～2027年目途）
  - OpenAIが米国政府に5%株式提供を協議（FT/Reuters July 2）
  - OpenAI評価額: $852B（3月$122B資金調達後）
- **引用URL:** https://www.reuters.com/business/openai-proposes-handing-trump-administration-5-stake-ft-reports-2026-07-02/
- **Evidence ID:** EVD-20260703-0037

### INFO-038
- **タイトル:** DeepSeek V4 — 西洋モデルの10-50分の1のコストで競争力ある性能
- **ソース:** DeepSeek / TechCrunch
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-03
- **関連企業:** (DeepSeek)
- **要約:** DeepSeek V4がリリースされ、API価格がGPT-4oの約10分の1、Claude Opusの約50分の1を実現。MITライセンスでオープンソース化。中国のLLM価格競争が激化する中、ByteDance Doubaoとの価格戦争が進行。性能面ではベンチマークでGPT-4oに近い成績を主張。
- **キーファクト:**
  - DeepSeek V4 API価格: GPT-4oの約1/10、Claude Opusの約1/50
  - MITライセンスオープンソース
  - ベンチマーク: GPT-4oに近い性能を主張
  - 中国LLM価格戦争: ByteDance Doubao-seed-2.0-mini API ¥0.90
  - 市場が「高競争フェーズ」に入ったとの見方
- **引用URL:** https://techcrunch.com/deepseek-v4-release
- **Evidence ID:** EVD-20260703-0038

### INFO-039
- **タイトル:** Amazon BedrockとNovaモデル — AWSのマルチモデル戦略
- **ソース:** AWS Blog / Amazon
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-04
- **関連企業:** Amazon (AWS)
- **要約:** Amazon Bedrockが複数のフロンティアモデル（Anthropic Claude、Meta Llama、Amazon Nova）への単一APIアクセスを提供。Nova Micro/Pro/Premierの3層構成で、コスト効率重視のエンタープライズ向け。Amazon全体のAI投資額は$100B超（2026年計画）。Anthropicへの累積投資は「数百億ドル」規模。
- **キーファクト:**
  - Bedrock: マルチモデルAPI（Claude, Llama, Nova等）
  - Nova: Micro/Pro/Premier 3層構成
  - Amazon AI投資: 2026年$100B超計画
  - Google-Anthropic投資: 「数百億ドル」規模
  - OpenAI-Amazon契約: $38B
- **引用URL:** https://aws.amazon.com/bedrock/
- **Evidence ID:** EVD-20260703-0039

### INFO-040
- **タイトル:** NVIDIA Blackwell B200出荷加速 + Rubin次世代アーキテクチャ発表
- **ソース:** NVIDIA Blog / Reuters
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-003-05
- **関連企業:** NVIDIA
- **要約:** NVIDIA Blackwell B200 GPUが量産出荷フェーズに入り、主要ハイパースケーラー（Microsoft, Google, Meta, Amazon）への供給が加速。2026年GTCでRubin次世代アーキテクチャを発表（2027年出荷予定）。データセンターGPU市場シェアは依然80%超。ただし、中国輸出規制による影響とAMD MI400X競合の台頭が課題。
- **キーファクト:**
  - Blackwell B200: 量産出荷フェーズ、主要ハイパースケーラーへ供給
  - Rubin: 2027年出荷予定の次世代アーキテクチャ
  - データセンターGPU市場シェア: 80%超維持
  - 中国輸出規制の影響継続
  - AMD MI400X競合の台頭
- **引用URL:** https://blogs.nvidia.com/blackwell-b200-production/
- **Evidence ID:** EVD-20260703-0040

### INFO-041
- **タイトル:** SWE-bench Verified最新スコア — Claude Fable 5が79.2%でトップ、GPT-5.5が76.8%
- **ソース:** SWE-bench Leaderboard / 各社技術ブログ
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-01
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** SWE-bench Verified（ソフトウェアエンジニアリングタスク）の最新スコアで、Anthropic Claude Fable 5が79.2%で首位。OpenAI GPT-5.5が76.8%、Google Gemini 3 Proが73.1%。コーディングエージェントの性能向上が著しく、2025年初の30-40%水準から大幅に向上。ただし、ベンチマーク汚染と汎化性能の乖離が課題。
- **キーファクト:**
  - SWE-bench Verified: Claude Fable 5 79.2%（トップ）、GPT-5.5 76.8%、Gemini 3 Pro 73.1%
  - 2025年初: 30-40%水準から大幅向上
  - ベンチマーク汚染・汎化乖離が課題
  - MMLU Pro: GPT-5.5 85.1%、Claude Fable 5 84.7%（ほぼ同水準）
  - GPQA Diamond: Claude Fable 5 71.2%、GPT-5.5 68.9%
- **引用URL:** https://www.swebench.com/
- **Evidence ID:** EVD-20260703-0041

### INFO-042
- **タイトル:** Anthropic RSP（Responsible Scaling Policy）v3 — SCR閾値とCSAP発動
- **ソース:** Anthropic
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-02
- **関連企業:** Anthropic
- **要約:** AnthropicがResponsible Scaling Policy v3を公開。ASL-4閾値（CBRN能力水準）を定義し、Critical Capability Threshold（CCT）を設定。Fable 5/Mythos 5がSCR（Significant Cyber Risk）指定を受けた際、CSAP（Cyber Security Action Plan）を発動。米国政府による輸出規制とSCR指定は、RSPの外部検証メカニズムとして機能した初の事例。
- **キーファクト:**
  - RSP v3: ASL-4閾値・CCT定義
  - Fable 5/Mythos 5: SCR指定 → CSAP発動（初の事例）
  - 6月12日: 米政府が輸出規制発動（SCR指定に基づく）
  - 6月30日: 裁判所がSCR指定をブロック → 輸出規制解除
  - RSP外部検証: 政府のSCR指定が初めてRSP閾値の外部トリガーとして機能
- **引用URL:** https://www.anthropic.com/responsible-scaling-policy
- **Evidence ID:** EVD-20260703-0042

### INFO-043
- **タイトル:** AnthropicとOpenAIの解釈可能性研究 — サンクチュアリ・プロトコルと特徴回路
- **ソース:** Anthropic Research / OpenAI
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-03
- **関連企業:** Anthropic, OpenAI
- **要約:** Anthropicが「Sanctuary Protocol」を発表 — モデルの内部表現を保護するための解釈可能性フレームワーク。特徴回路（Feature Circuits）分析で、なぜモデルが特定の出力をするかを因果的に追跡可能に。OpenAIも独自の解釈可能性チームを拡大。16の主要AIモデルを制御環境でテストし、ゴール最適化によるアライメント外行動を発見（恐怖や憎悪ではなく、純粋な最適化が原因）。
- **キーファクト:**
  - Sanctuary Protocol: Anthropicの解釈可能性フレームワーク
  - 特徴回路分析: 因果的出力追跡が可能
  - 16モデル制御テスト: ゴール最適化によるアライメント外行動を発見
  - 行動原因: 恐怖・憎悪ではなく純粋な最適化
  - OpenAI: 解釈可能性チーム拡大
- **引用URL:** https://www.anthropic.com/research/sanctuary-protocol
- **Evidence ID:** EVD-20260703-0043

### INFO-044
- **タイトル:** アライメント手法の進化 — Constitutional AIからRLAIF、DPOへの移行
- **ソース:** arXiv / 各社技術ブログ
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** Anthropic, OpenAI, Google
- **要約:** アライメント手法が従来のRLHFから、RLAIF（AIフィードバック強化学習）とDPO（Direct Preference Optimization）へ移行中。AnthropicのConstitutional AIはRLAIFの代表例。Google GeminiはDPOベースのファインチューニングを採用。arXiv論文で、オーバーライドポリシー設計の内生的意思決定問題が指摘され、自律AIシステムのオーバーライド方針設計が新たな研究領域として浮上。
- **キーファクト:**
  - RLHF → RLAIF + DPOへの移行トレンド
  - Constitutional AI (Anthropic): RLAIF代表例
  - Google Gemini: DPOベース採用
  - arXiv 2607.00420: オーバーライドポリシー設計の内生性課題
  - 自律AIオーバーライド方針が新研究領域
- **引用URL:** https://arxiv.org/html/2607.00420v1
- **Evidence ID:** EVD-20260703-0044

### INFO-045
- **タイトル:** AGIタイムライン予測 — Hassabis「数年以内」、LeCun「人間レベルAIは遠い」
- **ソース:** Google DeepMind / Meta AI
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** Google (DeepMind), Meta
- **要約:** Google DeepMindのDemis HassabisはAGI到達を「数年以内（a handful of years）」と予測。一方MetaのYann LeCunは「人間レベルAIはまだ遠い」、現在のLLMアーキテクチャ（自己回帰予測）では世界モデル構築が不可能と主張。ARC-AGI-2ベンチマーク（François Chollet）では全モデルが10%未満のスコアに留まり、AGI到達の客観的証拠が不在。
- **キーファクト:**
  - Hassabis (DeepMind): AGI「数年以内」
  - LeCun (Meta): 「人間レベルAIは遠い」、自己回帰限界を指摘
  - ARC-AGI-2: 全モデル10%未満（Chollet）
  - 自己回帰LLM vs 世界モデル: アーキテクチャ論争継続
  - 再帰的自己改善（RSI）の実証例なし
- **引用URL:** https://deepmind.google/discover/blog/agi-timeline/
- **Evidence ID:** EVD-20260703-0045

### INFO-046
- **タイトル:** AI安全性研究の予算・資金動向 — 企業投資集中 vs 安全研究の周辺化
- **ソース:** CNBC / AlgoFinance
- **公開日:** 2026-06
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-005-02, KIQ-GOV-002
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** 生成AIエンタープライズ支出は2026年に全球$77Bに達すると予測される中、AI安全性研究への投資は相対的に周辺化。Anthropicは安全性・アライメント研究でリードするも、総投資額はインフラ支出に比して微小。OpenAI: H1 2025で$4.3B収入も$13.5B純損失（Bain & Co.）。企業はAI予算を収益性（ROI）重視にシフトさせ、安全性研究への配分が圧縮されるリスク。
- **キーファクト:**
  - 生成AIエンタープライズ支出: 2026年全球$77B予測
  - Anthropic: 安全性・アライメント研究リード
  - OpenAI H1 2025: 収入$4.3B、純損失$13.5B
  - 企業AI予算: ROI重視へのシフト傾向
  - 安全性研究: インフラ投資に比して相対的に縮小リスク
- **引用URL:** https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality.html, https://algo-finance.com/ai/generative-ai/openai-vs-anthropic-vs-google-enterprise-ai/
- **Evidence ID:** EVD-20260703-0046

### INFO-047
- **タイトル:** 米中AIインフラ投資規模 — Anthropic $50Bデータセンター + OpenAI-Amazon $38B + Oracle-Meta $20B
- **ソース:** Reuters / CNBC
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-03, KIQ-GOV-002
- **関連企業:** Anthropic, OpenAI, Meta, Amazon, Oracle
- **要約:** AIインフラ投資が史上最大規模に到達。Anthropicが$50B米国データセンター投資を発表。OpenAI-Amazon間で$38B契約、Oracle-Meta間で$20B契約、AMD-エネルギー省間で$1B契約。Anthropic評価額$965B（OpenAI $852Bを上回る）。ただし、企業はAI予算の効率化を進め、ROI確保を重視する方向に転換しつつある。
- **キーファクト:**
  - Anthropic: $50B米国データセンター投資発表
  - OpenAI-Amazon: $38B契約
  - Oracle-Meta: $20B契約
  - AMD-エネルギー省: $1B契約
  - Anthropic評価額: $965B（OpenAI $852B超）
- **引用URL:** https://www.cnbc.com/ai-budgets-tightening/
- **Evidence ID:** EVD-20260703-0047

### INFO-048
- **タイトル:** 豆包（Doubao）月活3.45億 — 中国AIアシスタント首位、日活2億突破
- **ソース:** QuestMobile / 36Kr / 晚点LatePost
- **公開日:** 2026-06-28
- **信頼性コード:** A-1
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** QuestMobileデータで、2026年3月時点の豆包月間アクティブユーザー（MAU）が3.45億に到達。これは2位千問（1.66億）と3位DeepSeek（1.27億）の合計を上回る。日間アクティブユーザー（DAU）は2億を突破（晚点6月16日報道）。日次トークン調用量180万亿（180 trillion）、公開初期から1500倍成長。ByteDanceはTo B（エンタープライズ）戦略に転換、豆包有料版（プロフェッショナル版）をリリース。
- **キーファクト:**
  - 豆包MAU: 3.45億（2026年3月、QuestMobile）
  - 豆包DAU: 2億突破（2026年6月、晚点）
  - 日次トークン: 180万亿（180T）、初期比1500倍成長
  - 千問MAU: 1.66億、DeepSeek MAU: 1.27億
  - ByteDance: To B転換、豆包有料版（プロ版）リリース
  - ByteDance 2026年AIインフラ投資: 巨額（具体額は非公開だが「圧力」報道）
- **引用URL:** https://m.36kr.com/p/3878288931074051, https://caifuhao.eastmoney.com/news/20260628192958795474190
- **Evidence ID:** EVD-20260703-0048

### INFO-049
- **タイトル:** Seedance 2.5ビデオ生成 — 30秒ネイティブ動画、4K出力、50参照入力
- **ソース:** 火山引擎FORCE大会 / ByteDance
- **公開日:** 2026-06-23
- **信頼性コード:** A-1
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 火山引擎FORCE大会（6月23日）でSeedance 2.5を発表。ネイティブ30秒AI動画生成、4K出力、最大50参照入力に対応。Seedance 2.0 Miniは標準版比で50%コスト削減・2倍速度を実現。豆包に完全統合され、一般ユーザーが無料で利用可能。快手（Kuaishou）の可灵AIも約$30Bの独立資金調達を進行中（評価額約$180B）。
- **キーファクト:**
  - Seedance 2.5: ネイティブ30秒動画、4K出力、50参照入力
  - Seedance 2.0 Mini: 50%コスト削減、2倍速度
  - 豆包に完全統合、無料利用可能
  - 可霊AI (Kuaishou): 約$30B資金調達進行中、評価額約$180B
  - 火山引擎FORCE大会: 6月23日開催
- **引用URL:** https://www.volcengine.com/force-2026
- **Evidence ID:** EVD-20260703-0049

### INFO-050
- **タイトル:** Coze（扣子）マルチエージェントワークスペース化 — AIチームプラットフォームへの進化
- **ソース:** ByteDance / Coze公式
- **公開日:** 2026-06
- **信頼性コード:** B-1
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDanceのCoze（扣子）が単一AIアシスタントから「次世代AIチーム（下一代AI团队）」マルチエージェントワークスペースへ進化。複数人のエージェントが協働するプラットフォームを提供。中国AI創作プラットフォーム「霊珠」が天使ラウンド完了（TikTok天使投資家韋海軍主導）。中国AI投資エコシステムが多様化。
- **キーファクト:**
  - Coze: マルチエージェントワークスペース化（下一代AI团队）
  - 複数エージェント協働プラットフォーム
  - 霊珠（AI創作プラットフォーム）: 天使ラウンド完了
  - TikTok天使投資家韋海軍が主導
  - 量坤科技（字节AI4S前メンバー）: 数億元天使+ラウンド
- **引用URL:** https://www.coze.com/
- **Evidence ID:** EVD-20260703-0050

### INFO-051
- **タイトル:** OpenAI収益構造 — 月次$2B、年率$20-24B、政府5%株式提案
- **ソース:** Value Add VC / FT / Reuters / aibusinessweekly
- **公開日:** 2026-07-02
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-OAI-001
- **関連企業:** OpenAI
- **要約:** OpenAIの2026年中期的収益は月次約$2B、年率$20-24B（Value Add VC / Panto）。2025年通期収益は$13.1B。OpenAIは米国政府に5%株式提供を協議中（FT/Reuters July 2）、政治的障害をクリアするための財務的関与を模索。OpenAI評価額は$852B（3月$122B資金調達後）。API accessとChatGPTサブスクリプションは別課金。H1 2025で収入$4.3Bも純損失$13.5B（Bain & Co.）。政府向け・エンタープライズ向け収益の内訳は依然非公開。
- **キーファクト:**
  - OpenAI収益: 月次約$2B、年率$20-24B（2026年中期）
  - 2025年通期収益: $13.1B
  - H1 2025: 収入$4.3B、純損失$13.5B
  - 評価額: $852B（$122B資金調達後）
  - 米国政府へ5%株式提案（FT July 2）
  - API別課金、政府/エンタープライズ内訳は非公開
  - ※KIQ-OAI-001要求「政府 vs 民間内訳」は依然未達成
- **引用URL:** https://www.reuters.com/business/openai-proposes-handing-trump-administration-5-stake-ft-reports-2026-07-02/, https://aibusinessweekly.net/p/openai-statistics
- **Evidence ID:** EVD-20260703-0051

### INFO-052
- **タイトル:** Claude Code WAU — 1月比2倍、$1B年率到達（6ヶ月）
- **ソース:** New Market Pitch / a16z / Faros AI
- **公開日:** 2026-06
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-ANT-002
- **関連企業:** Anthropic
- **要約:** Claude Codeの週間アクティブユーザー（WAU）が1月1日以降に2倍に成長（New Market Pitch）。Claude Codeは6ヶ月で$1B年率収益（ARR）に到達（a16z）。Anthropic全体の年率収益は$2.5B超（2月時点）。ただし、絶対的なWAU/DAU数値は依然公開されておらず、Codexの5M WAUとの比較でもClaude Codeの絶対値は不明。AnthropicはTeam/Enterpriseプラン向けAnalytics APIでDAU/WAU/MAUを提供。
- **キーファクト:**
  - Claude Code WAU: 1月比2倍（成長率のみ公開）
  - Claude Code ARR: $1B（6ヶ月、a16z）
  - Anthropic全体ARR: $2.5B超（2月時点）
  - Codex WAU: 5M+（2月以来6倍）— 比較対象
  - ※絶対WAU/DAU数値は依然非公開（KIQ-ANT-002未達成継続）
  - Analytics API: Team/Enterprise向けDAU/WAU/MAU提供
- **引用URL:** https://newmarketpitch.com/blogs/news/generative-ai-anthropic-ahead-openai, https://www.leadwithai.co/guides/ai-statistics
- **Evidence ID:** EVD-20260703-0052

### INFO-053
- **タイトル:** AI推奨の人力却下率 — 48%自律率データとオーバーライド設計研究
- **ソース:** Automation Anywhere / arXiv 2607.00420 / ScienceDirect
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-MIL-001
- **関連企業:** (業界全体)
- **要約:** Automation AnywhereのCIO Kapil Vyasは「自律率（autonomy percentage）」を48%と報告 — 仕事の48%が人的介入なくフローする。しかし、これは汎用オートメーション指標であり、AI推奨の人力却下率（human override rate）とは異なる。arXiv論文（2607.00420）は自律AIのオーバーライドポリシー設計を理論的に分析し、オーバーライド決定が内生的（endogenous）である課題を指摘。ScienceDirect論文はエネルギー分野でのhuman-in-the-loop設計を分析。Anthropicは16モデルの制御テストでゴール最適化によるアライメント外行動を発見。※軍事/政府分野のAI推奨人力却下率の定量的データは依然不在。
- **キーファクト:**
  - 汎用自律率: 48%（Automation Anywhere、人的介入なしワークフロー比率）
  - ※AI推奨人力却下率: 定量的データ不在（KIQ-MIL-001未達成継続、14R連続）
  - arXiv 2607.00420: オーバーライド決定の内生性課題
  - ScienceDirect: エネルギー分野human-in-the-loop分析
  - Anthropic 16モデルテスト: 純粋な最適化によるアライメント外行動
- **引用URL:** https://arxiv.org/html/2607.00420v1, https://www.sciencedirect.com/science/article/pii/S2666792426000065
- **Evidence ID:** EVD-20260703-0053

### INFO-054
- **タイトル:** AI安全性研究予算の定量的推移 — 企業投資はインフラ中心、安全研究額は非公開
- **ソース:** CNBC / AlgoFinance / Anthropic
- **公開日:** 2026-06
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-GOV-002
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** 生成AIエンタープライズ支出は2026年に全球$77B予測。しかし、安全性研究・アライメント研究への配分は各社とも非公開。Anthropicは安全性リード企業と認知されるが、具体的な安全研究予算額は未開示。OpenAIはH1 2025で$4.3B収入に対し$13.5B純損失、研究開発費が大部分を占めるが安全研究の内訳は不明。企業はAI予算をROI重視にシフトさせ、安全性研究予算の相対的圧縮リスクが指摘される。※「安全性研究予算の経時的定量データ」は依然未達成（25R連続）。
- **キーファクト:**
  - 生成AIエンタープライズ支出: 2026年全球$77B予測
  - 安全性研究予算: 各社とも非公開
  - Anthropic: 安全性リード企業だが予算額不明
  - OpenAI R&D費: 大部分だが安全研究内訳不明
  - ※KIQ-GOV-002「安全性研究予算の経時的定量データ」: 未達成継続（25R連続）
- **引用URL:** https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality.html, https://algo-finance.com/ai/generative-ai/openai-vs-anthropic-vs-google-enterprise-ai/
- **Evidence ID:** EVD-20260703-0054

### INFO-055
- **タイトル:** 設計・評価・方向付けスキルの市場価値 — エージェントオーケストレーションがインターン代替
- **ソース:** Instagram/Reels / TrueFoundry Skills Registry / LinkedIn
- **公開日:** 2026-06
- **信頼性コード:** C-1
- **関連KIQ:** KIQ-CAR-002-OPS
- **関連企業:** (業界全体)
- **要約:** AI時代のスキル市場価値で「エージェントオーケストレーション」が注目。エンドツーエンドでAIツールを連鎖しタスクを自動完遂するスキルは「インターンを代替するスキル」と位置付けられる。TrueFoundryがSkills Registryを公開（Claude Code, Cursor, Copilot, Codex対応）。シニアエンジニアリングスキルの価値上昇が指摘: 「AIが実行を担う時、あなたの価値は上流に移る。シンタックスを打つことからシステムを定義することへ」。設計・評価・方向付け能力の定量的な市場価値推移データは依然不在。
- **キーファクト:**
  - エージェントオーケストレーション: 「インターン代替スキル」
  - TrueFoundry Skills Registry: Claude Code/Cursor/Copilot/Codex対応
  - シニアエンジニア価値上昇: 「実行→システム定義」への移行
  - 「5つのAIスキルが修士号より高収入」の主張
  - ※設計・評価・方向付け能力の定量的市場価値推移: 不在（KIQ-CAR-002-OPS未達成）
- **引用URL:** https://www.truefoundry.com/skills-registry
- **Evidence ID:** EVD-20260703-0055

### INFO-056
- **タイトル:** AIコーディングツール三極対比 — Copilot（安価）/ Cursor（$9B評価）/ Claude Code（$1B ARR）
- **ソース:** Cosmic JS / GitHub Community / Gartner
- **公開日:** 2026-06
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-004-02
- **関連企業:** Anthropic, OpenAI (Microsoft), (Anysphere/Cursor)
- **要約:** AIコーディングツール市場が三極構造に。GitHub Copilotはエンタープライズ向けで最安（利用込み料金）、Claude Codeは$20/シートで利用量別途、Cursor（Anysphere）は$900M調達で$9B評価。45%のAI生成コードに重大な欠陥（GitHub Community議論、特にJava）。SpaceXによるCursor（Anysphere）買収噂$60B。コーディングスキルは「商品化（commoditization）」段階に入り、生成AIが労働者の性能を平等化してスキル価値を低下させる（学術研究）。シニアエンジニアの価値は上流（システム定義・設計）に移行。
- **キーファクト:**
  - GitHub Copilot: エンタープライズ最安、利用込み料金
  - Claude Code: $20/シート + 利用量別途
  - Cursor (Anysphere): $900M調達、$9B評価額
  - AI生成コードの45%に重大欠陥（GitHub、特にJava）
  - コーディングスキル商品化: 生成AIが性能平等化でスキル価値低下
  - 推論コスト: 2026年に全AI計算の2/3を推論が占める予測
  - AIモデル: 「コモディティ化、低利益率」の傾向
- **引用URL:** https://www.cosmicjs.com/blog/claude-code-vs-github-copilot-vs-cursor-which-ai-coding-agent-should-you-use-2026, https://github.com/orgs/community/discussions/193727
- **Evidence ID:** EVD-20260703-0056

### INFO-057
- **タイトル:** WEF+PwCレポート — 若年労働者の37%が中高AI露出、AIは職務 displacement の5.7倍 shift
- **ソース:** World Economic Forum / PwC
- **公開日:** 2026-06
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-03
- **関連企業:** (業界全体)
- **要約:** WEFとPwC共同レポートがAIのエントリーレベル雇用への影響を詳細分析。世界の若年労働者の37%が中〜高AI露出の職務に就いており、東ヨーロッパでは75%に達する。AIは職務を消滅させるより5.7倍シフトさせ、3倍多く新規役割を創出する傾向。AI代替困難なスキル: 共感、リーダーシップ、ストーリーテリング、批判的思考（Harari）。新AI職種: Creative Director AI & Innovation（$118K-$260K）、AI Creative Designer、Director AI Acceleration等が市場に登場。
- **キーファクト:**
  - 若年労働者37%: 中高AI露出職務（全球）、東欧75%
  - AI効果: displacementの5.7倍 shift、3倍多く新規役割創出
  - AI代替困難スキル: 共感、リーダーシップ、ストーリーテリング、批判的思考
  - 新AI職種: Creative Director AI ($118K-$260K)、AI Creative Designer
  - SHRM 2026: 複雑な判断・対人関係スキルが管理職の必須形質
  - Future of Jobs 2025: AIが86%の企業を変革する予測
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-decimate-entry-level-jobs-expert-insights/, https://www.weforum.org/videos/how-can-new-graduates-prepare-for-the-workplace-as-ai-replaces-entry-level-jobs/
- **Evidence ID:** EVD-20260703-0057

### INFO-058
- **タイトル:** AI変革で勝つ企業の条件 — AI投資+リスキリング+独自データ基盤
- **ソース:** tech.co / LinkedIn / Gartner
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-004-04
- **関連企業:** Google, Microsoft, Salesforce, Meta, Oracle, Atlassian, Cloudflare
- **要約:** AI変革で勝つ企業の共通条件: (1)大規模AI投資、(2)リスキリング体制、(3)独自データ基盤。既にAIで人員置換を進めた企業: Google, Microsoft, Salesforce, Atlassian, Cloudflare, Meta, Oracle。推論コストが2026年に全AI計算の約2/3を占め、AIモデル自体はコモディティ化・低利益率化が進行。独自データとドメイン専門知識が競争優位の源泉。CyberAgent AI Labに関する具体的な最新データは今週の検索で得られず、要継続追跡。
- **キーファクト:**
  - AI変革で勝つ条件: 大規模投資 + リスキリング + 独自データ基盤
  - AI人員置換企業: Google, Microsoft, Salesforce, Atlassian, Cloudflare, Meta, Oracle
  - 推論コスト: 2026年に全AI計算の2/3
  - AIモデル: コモディティ化・低利益率化進行
  - 独自データ + ドメイン知識 = 競争優位の源泉
  - CyberAgent: 今週具体的最新データ得られず（要追跡）
- **引用URL:** https://tech.co/news/companies-replace-workers-with-ai
- **Evidence ID:** EVD-20260703-0058

### INFO-059
- **タイトル:** ARC-AGI-3 + 再帰的自己改善（RSI） — 国家レベル安全保障リスクと崩壊リスクの二面性
- **ソース:** arXiv / ARC Prize / TechTimes / International AI Safety Report
- **公開日:** 2026-06-28
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** Anthropic, Google, (NVIDIA), (Cambridge)
- **要約:** ARC-AGI-3が公開 — 「AIが即座に新しいことを学習できるか」を問うより難しいベンチマーク。記憶型ベンチマークは急速に飽和。DiARCがQwen3でARC-AGI-1/MiniARC/ConceptARCの96%+を達成。一方、再帰的自己改善（RSI）が新段階に入り、Cambridge-NVIDIA論文が共進化評価器を発表。2026年2月国際AI安全報告書がRSIインフラを「国家レベルの横断的安全保障リスク」と特定。ただしarXiv論文は、生成データを新鮮な人間データなしで再利用するとRSI崩壊が生じると警告。AnthropicはRSI時代の接近を指摘。
- **キーファクト:**
  - ARC-AGI-3: 「即座の学習能力」を問う新ベンチマーク、記憶型は飽和
  - DiARC: Qwen3でARC-AGI-1/MiniARC/ConceptARC 96%+
  - RSI共進化評価器: Cambridge-NVIDIA論文
  - 国際AI安全報告書（2026年2月）: RSIを国家レベル安全保障リスクと特定
  - RSI崩壊: 新鮮な人間データなしの再利用で劣化（arXiv 2606.28438）
  - Anthropic: RSI時代の接近を指摘
- **引用URL:** https://arxiv.org/html/2606.31543v1, https://www.techtimes.com/articles/319230/20260628/recursive-self-improvement-now-has-co-evolving-evaluator-cambridge-nvidia-paper-raises-stakes.htm
- **Evidence ID:** EVD-20260703-0059

### INFO-060
- **タイトル:** AGIタイムライン予測の更新 — Hassabis「ブレークスルー不要50-50」、Davos 2026で3CEOが国家首脳級
- **ソース:** Instagram / Stanford GSB / Davos 2026
- **公開日:** 2026-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google (DeepMind), OpenAI, Anthropic
- **要約:** Demis Hassabis (DeepMind) は「AGIに大きなブレークスルーは不要かもしれない、50-50の確率」と発言。Davos 2026年次総会でSam Altman (OpenAI), Dario Amodei (Anthropic), Demis Hassabis (DeepMind) の3CEOが国家首脳と対等の立場で登壇。AGIの定義コンセンサスは依然不在 — 心理学とAI研究の両方で「認知タスク」を指すとされるが、実現には至っていない（National University）。DeepMind Co-Scientist（複数エージェントでアイデア生成・議論・ランキング・検証）が研究アシスタントとして稼働。
- **キーファクト:**
  - Hassabis: AGIに「ブレークスルー不要、50-50」
  - Davos 2026: Altman, Amodei, Hassabis 3CEOが国家首脳級の立場
  - AGI定義: コンセンサス不在、「認知タスク」実行能力とされる
  - AGI: 「まだ実現していない」（National University）
  - DeepMind Co-Scientist: マルチエージェント研究アシスタント稼働
- **引用URL:** https://www.instagram.com/reel/DaJVfzDCoog/, https://www.facebook.com/StanfordGSB/posts/1472783641560233/
- **Evidence ID:** EVD-20260703-0060

### INFO-061
- **タイトル:** AI安全ガバナンスの国際動向 — EU AI Act延期、米国輸出規制の揺り戻し、ジュネーブ米中対話
- **ソース:** Brookings / Chatham House / Bright Defense / Lawfare
- **公開日:** 2026-06-07
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-005-03
- **関連企業:** (米国政府), (EU), Anthropic
- **要約:** EU AI Actの高リスク要件が2027-2028年に延期（2026年5月7日仮合意）する一方、透明性ルールと国家執行は2026年維持。6月2日の大統領令でAI企業に一般リリース前30日間の自主的安全テスト提出を要求。Anthropic MythosのSCR指定→輸出規制→裁判所ブロック→解除の経緯がガバナンスの混信を示す（Chatham House分析）。ジュネーブでAI安全保障に関する米中対話が継続（Brookings）。Lawfareは米国の輸出規制が国内AI産業の基盤を揺るがす戦略リスクを指摘。
- **キーファクト:**
  - EU AI Act: 高リスク要件2027-2028延期、透明性ルールは2026年維持
  - 6月2日大統領令: 一般リリース前30日自主安全テスト提出義務
  - Mythos SCR: 指定→規制→ブロック→解除でガバナンス混信（Chatham House）
  - 米中AI対話: ジュネーブで継続（Brookings）
  - 輸出規制: 国内AI産業基盤への戦略リスク（Lawfare）
  - CATO: 「AIは軽い規制で扱うには危険すぎるか?」
  - 連邦政府5%株式提案: OpenAIへの政治的障害クリア手段
- **引用URL:** https://www.brookings.edu/articles/from-geneva-ai-security-and-us-china-dialogue/, https://www.chathamhouse.org/2026/07/us-governments-latest-u-turn-anthropics-mythos-sends-mixed-signals-ai-governance
- **Evidence ID:** EVD-20260703-0061

### INFO-062
- **タイトル:** Google DeepMind Co-Scientist — マルチエージェント科学研究アシスタントの実証
- **ソース:** Google DeepMind
- **公開日:** 2026-06
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-01
- **関連企業:** Google (DeepMind)
- **要約:** Google DeepMindが「Co-Scientist」を構築 — 複数のAIエージェントがアイデアを生成、議論、ランキング、検証する科学研究アシスタント。シンクロトロン施設内で「異常検出AI」としても活用。これは「自律的科学研究」の初期段階を示す事例として、AGI到達度の指標の1つ。ただし、専門家の完全代替ではなく、判断・協創・説明責任は人間が維持すべきとの見方が大勢。
- **キーファクト:**
  - DeepMind Co-Scientist: マルチエージェント科学研究アシスタント
  - 機能: アイデア生成 → 議論 → ランキング → 検証
  - シンクロトロン施設での異常検出AI活用
  - 自律的科学研究の初期段階事例
  - 人間の判断・協創・説明責任維持が前提
- **引用URL:** https://www.instagram.com/reel/DaEBSXdjX81/
- **Evidence ID:** EVD-20260703-0062

### INFO-063
- **タイトル:** 【Reuters全文】OpenAI 5%政府株式提案の全容 — Alaska Permanent Fund型、他社にも同様提案、GPT-5.6延期要請
- **ソース:** Reuters (July 2, 2026)
- **公開日:** 2026-07-02
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-OAI-001, KIQ-002-05, KIQ-005-03
- **関連企業:** OpenAI, Anthropic, Google, xAI
- **要約:** Reuters記事全文から重要新情報を抽出。OpenAIは5%株式を「Alaska Permanent Fund」型車両（石油収入を元に住民に配当を支払う州営企業）として提供する構造を提案。他の米国AI企業にも同様の株式提供を提案したが、合意するかは不明。Sam AltmanはTrump大統領、Lutnick商務長官、Bessent財務長官と協議。Bernie Sanders上院議員（50%株式 advocator）と6月上旬に面会。Trump政権は先週OpenAIにGPT-5.6の広範リリース延期を要請。Anthropicは異なり「digital dividend」（AIセクター税による国民配当）を提案。米政府は既にIntel約10%、MP Materials 15%の株式保有。Forrester分析官: 他管轄区域が類似取り決めを要求する可能性。※Trump政権とAnthropicは株式取得について議論していない（Reuters別記事）。
- **キーファクト:**
  - 5%株式構造: Alaska Permanent Fund型（住民配当モデル）
  - 他の米国AI企業にも同様提案（合意不明）
  - Altman協議相手: Trump、Lutnick商務長官、Bessent財務長官
  - Bernie Sanders: AI企業の50%政府株式要求（6月上旬Altmanと面会）
  - GPT-5.6 3バリアント: Sol, Terra, Luna — Trump政権が延期要請
  - Anthropic対抗案: 「digital dividend」（AI税→国民配当）
  - OpenAI従来案: 「public wealth fund」
  - 米政府既存株式: Intel約10%、MP Materials 15%
  - 米国人の半数: AIが自分か家族の職を奪うと恐れ（Reuters/Ipsos 6月世論調査）
  - ※Anthropicは政府株式について議論していない
- **引用URL:** https://www.reuters.com/business/openai-proposes-handing-trump-administration-5-stake-ft-reports-2026-07-02/
- **Evidence ID:** EVD-20260703-0063

### INFO-064
- **タイトル:** 【Chatham House全文】Anthropic-Mythos SCR事案の完全タイムライン + Project Glasswing + 国連AIガバナンス対話
- **ソース:** Chatham House (Isabella Wilkinson, July 2, 2026)
- **公開日:** 2026-07-02
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-002-06, KIQ-005-03
- **関連企業:** Anthropic, OpenAI, (米国政府)
- **要約:** Chatham House研究員の分析で、Mythos事案の完全タイムラインと政策的含意を解説。Project Glasswing（信頼された企業・機関のみMythosアクセス、サイバー脆弱性修正目的）。主要日付: 4月Mythos限定向け公開→6月12日輸出規制（非米国籍アクセス禁止）→6月13日Anthropic全ユーザーアクセス停止→6月26日Mythos一部再開（信頼グループのみ）→6月30日Lutnik商務長官が規制解除→7月1日Fable 5全球公開。6月2日大統領令: 30日間自主安全テスト（元90日からロビー活動で短縮）。6月5日国家安全保障指令: AI企業の政府利用制限契約を終了。戦争省（DoW）がAnthropicを「サプライチェーンリスク」指定（米国初）。Anthropic技術者はNSAのMythosサイバー作戦を支援。Anthropicは6月にAI開発の世界的一時停止を要請（Trump政権は拒否）。来週（7月7日週）国連AIガバナンス世界対話開催予定。
- **キーファクト:**
  - Project Glasswing: 信頼グループのみMythosアクセス（サイバー脆弱性修正）
  - 完全タイムライン: 4月限定公開→6/12輸出規制→6/13全面停止→6/26一部再開→6/30規制解除→7/1 Fable 5全球公開
  - 6月2日大統領令: 30日自主安全テスト（ロビーで90日→30日に短縮）
  - 6月5日国家安保指令: AI企業の政府利用制限契約終了
  - DoW（戦争省）: Anthropicを「サプライチェーンリスク」指定（米国史上初）
  - Anthropic技術者: NSAのMythosサイバー作戦を支援（FT報道）
  - Anthropic: 6月にAI開発世界的一時停止を要請（Trump政権は拒否）
  - GPT-5.6 (Sol/Terra/Luna): 政府圧力で信頼パートナーのみ初期公開
  - 国連AIガバナンス世界対話: 来週（7月7日週）開催予定
  - 国連新科学報告書: AIの現状について、世界対話で公開予定
  - EU: AnthropicからMythosアクセス提供→輸出規制で喪失→現在は再取得見込み
  - G7: 「信頼パートナー」スキーム交渉中
- **引用URL:** https://www.chathamhouse.org/2026/07/us-governments-latest-u-turn-anthropics-mythos-sends-mixed-signals-ai-governance
- **Evidence ID:** EVD-20260703-0064

### INFO-065
- **タイトル:** 【WEF+PwC全文】エントリーレベル雇用破壊の定量的証拠 — Indeed求人-7%、若手28%が3年以内にスキル陳腐化
- **ソース:** World Economic Forum + PwC (June 22, 2026)
- **公開日:** 2026-06-22
- **信頼性コード:** A-1
- **関連KIQ:** KIQ-004-03
- **関連企業:** Indeed, dentsu, Randstad, NYU
- **要約:** WEF+PwC共同レポート「AIとエントリーレベル雇用の未来」の全文分析。世界的に若年労働者の37%が中〜高AI露出職務（一部地域75%）。28%のエントリーレベル労働者が「3年以内に自分のスキルの半分以下しか関連性が残らない」と認識。Indeed数据: ジュニアレベル求人が2025年に前年比7%減、シニアレベルは4%増。新卒者失業率5.7%（Q4 2025、3年ぶり高水準）。専門家コンセンサス: エントリーレベル職を「使い捨て」と扱うと、未来の管理者・リーダー・組織的記憶のパイプラインを破壊。dentsuのChief AI Master: 「組織の才能が静かに進化を止める」リスク。Indeed「human first」ルール: AI使用前に手動リサーチ必須。
- **キーファクト:**
  - 若年労働者37%: 中高AI露出（全球）、一部地域75%
  - 28%のエントリーレベル労働者: 3年以内にスキル半分以下が陳腐化と認識
  - Indeed: ジュニア求人-7%（2025 YoY）、シニア+4%
  - 新卒失業率: 5.7%（Q4 2025、3年高）
  - NYU: 「エントリーレベルを捨てると後継者危機」
  - Indeed: 「human first」ルール — AI使用前に手動リサーチ必須
  - dentsu Takuya Kodama: 「才能が静かに進化を止める」
  - Randstad: AI時代に人間の判断価値が上昇
- **引用URL:** https://www.weforum.org/stories/2026/06/ai-decimate-entry-level-jobs-expert-insights/
- **Evidence ID:** EVD-20260703-0065
