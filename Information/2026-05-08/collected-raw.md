# 収集データ: 2026-05-08

## メタデータ
- 収集日時: 2026-05-08 01:30 UTC
- 実行クエリ数: 72 / 115（collection_plan.json全24KIQ + 動的7KIQ）
- scrape実行数: 7件（公式ブログ2件、検索結果から主要記事5件）
- 収集情報数: 85件
- Evidence ID 採番範囲: EVD-20260508-0001 〜 EVD-20260508-0085
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓, KIQ-AGENT-001 ✓（動的）, KIQ-BTD-PRICE ✓（動的）, H-GOO-003 ✓（動的）, H-CAR-002 ✓（動的）, H-GOO-001 ✓（動的）, Pattern B JV ✓（動的）, H-GOO-002 ✓（動的）
- 品質フラグ: NORMAL

## 動的追加クエリ（Arbiterフィードバックに基づく）
- KIQ-AGENT-001: Claude Code WAU/MAU定量データ（collection_plan.jsonに存在しないKIQ）
- KIQ-BTD-PRICE: DeepSeek API価格持続可能性（collection_plan.jsonに存在しないKIQ）
- H-GOO-003構造的再検討: Google強み領域定量比較
- H-CAR-002 BLS確認: BLS職業分類変更影響
- H-GOO-001収集: Google Cloud エンタープライズAI収益
- Pattern B JV追跡: JV成果・FDE展開規模
- H-GOO-002 I探索: Google围い込み指標

## 収集結果

### INFO-001
- **タイトル:** Claude Sonnet 4.6: フル機能アップグレードモデル
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-02-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-003-02
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Sonnet 4.6をリリース。コーディング・コンピュータ使用・長文脈推論・エージェント計画・ナレッジワーク全般でOpus級性能を実現。1Mトークンコンテキストウィンドウ（ベータ）搭載。価格はSonnet 4.5と同一（$3/$15 per million tokens）。
- **キーファクト:**
  - Claude Codeユーザーの70%がSonnet 4.5よりSonnet 4.6を好む
  - OSWorldベンチマークで大幅改善、人間レベルのコンピュータ使用能力に接近
  - SWE-bench Verified 80.2%（プロンプト修正時）
  - ARC-AGI-2 max effortで高スコア
  - Replit/Cursor/GitHub/Databricks等からの推薦コメント
  - Claude in ExcelがMCPコネクタサポート追加
- **引用URL:** https://www.anthropic.com/news/claude-sonnet-4-6
- **Evidence ID:** EVD-20260508-0001

### INFO-002
- **タイトル:** GPT-5.5 Instantリリース: より賢く正確でパーソナライズされたデフォルトモデル
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-003-02, KIQ-003-01
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPTのデフォルトモデルをGPT-5.5 Instantに更新。ハルシネーション52.5%削減、GPQA 85.6%、AIME 2025 81.2%。パーソナライゼーション強化とメモリソース機能追加。
- **キーファクト:**
  - 高リスクプロンプトでのハルシネーション52.5%削減
  - GPQA 78.5%→85.6%、AIME 2025 65.4%→81.2%、MMMU-Pro 69.2%→76.0%
  - Memory Sources機能でパーソナライゼーション根拠を可視化
  - APIでは`chat-latest`として提供
  - 30.2%少ない語数で同等以上の回答品質
- **引用URL:** https://openai.com/index/gpt-5-5-instant/
- **Evidence ID:** EVD-20260508-0002

### INFO-003
- **タイトル:** OpenAI ChatGPTにTrusted Contact安全機能を追加
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPTにTrusted Contact機能をロールアウト。成人ユーザーが信頼する連絡先を登録でき、自傷行為の懸念がある場合に通知。APA等の臨床専門家と協力して開発。
- **キーファクト:**
  - 自動モニタリング+訓練された人間レビューの二段階審査
  - 通知は1時間以内に審査
  - 260人以上の医師からなるGlobal Physicians Networkと協力
  - プライバシー保護のためチャット詳細は通知に含まれない
- **引用URL:** https://openai.com/index/introducing-trusted-contact-in-chatgpt/
- **Evidence ID:** EVD-20260508-0003

### INFO-004
- **タイトル:** OpenAIがGPT-5.5-Cyberをサイバーセキュリティチーム向けに提供開始
- **ソース:** CNBC
- **公開日:** 2026-05-07
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAIが審査済みサイバーセキュリティチーム向けに新モデルGPT-5.5-Cyberをロールアウト。AnthropicのMythosデビューから1ヶ月後の対応。
- **キーファクト:**
  - Anthropic Mythosのセキュリティ特化モデルに対抗
  - 審査済みチームのみアクセス可能
- **引用URL:** https://www.cnbc.com/2026/05/07/openai-rolls-out-new-gpt-5point5-cyber-to-vetted-cybersecurity-teams.html
- **Evidence ID:** EVD-20260508-0004

### INFO-005
- **タイトル:** Google April 2026 AI最新情報: Cloud Next・Gemma 4・第8世代TPU
- **ソース:** Google公式ブログ
- **公開日:** 2026-05-04
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-01, KIQ-001-04, KIQ-003-03
- **関連企業:** Google
- **要約:** GoogleがApril 2026のAI最新情報をまとめて公開。Gemini Enterprise Agent Platform、第8世代TPU、Gemma 4オープンモデル、Google Vids無料化、Deep Research Max、Colab Learn Mode等を発表。Cloud Next '26では260以上の発表。
- **キーファクト:**
  - 75%のCloud顧客がGoogle Cloud AIを利用済み
  - 330組織が年間1兆トークン以上を処理
  - Gemma 4はバイト当たり最も高性能なオープンモデル
  - Gemma累計5億回以上ダウンロード
  - 第8世代TPUはAgent時代向けに設計
  - Google Vids: 無料で月10本まで動画生成可能
- **引用URL:** https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-april-2026/
- **Evidence ID:** EVD-20260508-0005

### INFO-006
- **タイトル:** Grok 4.3: サイレントリリースの新モデル
- **ソース:** YouTube (Julian Goldie SEO)
- **公開日:** 2026-05-02
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-003-02
- **関連企業:** xAI
- **要約:** xAIがGrok 4.3を4月17日に告知なしでリリース。PDF/スプレッドシート/スライド生成、ネイティブ動画理解、Grok Computer統合強化、音声API新機能を追加。ただしハルシネーション増加と永続メモリ欠如の課題あり。
- **キーファクト:**
  - 4月17日に告知なしでリリース（サイレントローンチ）
  - チャット内でPDF・スプレッドシート・スライドデッキ作成機能
  - ネイティブ動画理解機能追加
  - Grok Computer自律タスク統合深化
  - 音声STT/TTS API新規提供
  - XChat暗号化メッセージアプリ
  - 永続メモリ機能なし（主要欠落）
  - 前バージョンより安価に運用可能
- **引用URL:** https://www.youtube.com/watch?v=nLkyFv4Cm08
- **Evidence ID:** EVD-20260508-0006

### INFO-007
- **タイトル:** OpenAIがChatGPTで広告テスト開始
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-002-05
- **関連企業:** OpenAI
- **要約:** OpenAIがChatGPT内で広告のテストを開始。ビジネスモデルの新たな展開。
- **キーファクト:**
  - ChatGPT Freeユーザー向けに広告テスト開始
  - 新たな収益化戦略の模索
- **引用URL:** https://openai.com/index/testing-ads-in-chatgpt/
- **Evidence ID:** EVD-20260508-0007

### INFO-008
- **タイトル:** Google AI Overviews更新: 購読出版物リンク強調表示
- **ソース:** Nieman Journalism Lab
- **公開日:** 2026-05-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05, KIQ-001-04
- **関連企業:** Google
- **要約:** GoogleがAI OverviewsとAI Modeで、ユーザーが購読している出版物からの情報を強調表示する新機能を導入。出版業界のGoogleトラフィック激減（Chartbeat: 小規模出版社で60%減）に対応する措置。
- **キーファクト:**
  - 「Subscribed」ラベルで購読出版物を強調
  - テストでクリック率が「大幅に」上昇
  - 小規模出版社のGoogle参照トラフィック2年間で60%減少
  - 「Further Exploration」「Expert Advice」パネル新設
  - Redditコンテンツの直接表示（年間$60M契約）
- **引用URL:** https://www.niemanlab.org/2026/05/google-highlights-links-from-subscribed-publications-in-new-ai-overviews-update/
- **Evidence ID:** EVD-20260508-0008

### INFO-009
- **タイトル:** OpenAI x Microsoft次期パートナーシップフェーズ
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-04-27
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** OpenAI, Microsoft
- **要約:** OpenAIとMicrosoftのパートナーシップの次フェーズに関する発表。
- **キーファクト:**
  - Microsoft-OpenAI提携の新段階
- **引用URL:** https://openai.com/index/next-phase-of-microsoft-partnership/
- **Evidence ID:** EVD-20260508-0009

### INFO-010
- **タイトル:** OpenAIがB2Bシグナル公開: フロンティア企業の差別化要因
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAIが「How frontier firms are pulling ahead」としてB2Bシグナルを公開。エンタープライズAI導入の先行企業の特徴を分析。
- **キーファクト:**
  - エンタープライズAI導入の先行企業分析
  - B2B向け新シグナル機能
- **引用URL:** https://openai.com/index/introducing-b2b-signals/
- **Evidence ID:** EVD-20260508-0010

### INFO-011
- **タイトル:** OpenAI音声インテリジェンス新モデルAPI提供
- **ソース:** OpenAI公式ブログ
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがAPIで新しい音声インテリジェンスモデルを提供開始。
- **キーファクト:**
  - API経由での新音声モデル提供
  - GPT-Realtime-2の可能性
- **引用URL:** https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
- **Evidence ID:** EVD-20260508-0011

### INFO-012
- **タイトル:** Anthropic: 次期エンタープライズAIサービス会社設立（Blackstone/H&F/GS）
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがBlackstone、Hellman & Friedman、Goldman Sachsと共同で新エンタープライズAIサービス会社を設立。Palantir型FDEモデル採用（Pattern B JV）。
- **キーファクト:**
  - Blackstone/H&F/Goldman SachsとのJV設立
  - Palantir型FDE（Forward Deployed Engineer）モデル
  - Arbiter v3.70で「構造的深化」と評価されたPattern B
- **引用URL:** https://www.anthropic.com/news/enterprise-ai-services-company
- **Evidence ID:** EVD-20260508-0012

### INFO-013
- **タイトル:** Anthropic: 金融サービス向けエージェント発表
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Anthropicが金融サービス・保険向けに10の新Cowork/Claude Codeプラグイン、Microsoft 365統合、新コネクタ、MCPアプリをリリース。
- **キーファクト:**
  - 10の新プラグイン（Cowork/Claude Code）
  - Microsoft 365スイート統合
  - 金融・保険向けMCPアプリ
  - 新コネクタ追加
- **引用URL:** https://www.anthropic.com/news/finance-agents
- **Evidence ID:** EVD-20260508-0013

### INFO-014
- **タイトル:** Anthropic: 使用量上限引き上げ・SpaceXコンピュート提携
- **ソース:** Anthropic公式ブログ
- **公開日:** 2026-05-07
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-003-04, KIQ-001-01
- **関連企業:** Anthropic, SpaceX
- **要約:** AnthropicがClaudeの使用量上限を引き上げ、SpaceXと新たなコンピュートパートナーシップを締結。
- **キーファクト:**
  - Claude使用量上限引き上げ
  - SpaceXとのコンピュート提携
  - 短期的なキャパシティ大幅増加
- **引用URL:** https://www.anthropic.com/news/higher-limits-spacex
- **Evidence ID:** EVD-20260508-0014

### INFO-015
- **タイトル:** Google Marketing Live 2026: AI時代の成長
- **ソース:** Google公式ブログ
- **公開日:** 2026-05-06
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-05, KIQ-002-04
- **関連企業:** Google
- **要約:** Google Marketing Live 2026でAI時代のマーケティング成長戦略を発表。データ主導の意思決定とAI広告自動化がテーマ。
- **キーファクト:**
  - Google Marketing Live 2026開催
  - AI駆動マーケティングの強化
  - 広告自動化プラットフォームの進展
- **引用URL:** https://blog.google/products/ads-commerce/google-marketing-live-2026-turn-your-data-into-decisions/
- **Evidence ID:** EVD-20260508-0015

### INFO-016
- **タイトル:** OpenAI Agents SDKアップデート: エージェント安全性と機能強化
- **ソース:** MSN
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** OpenAIがAgents SDKをアップデートし、エンタープライズ向けエージェント安全性と機能を改善。標準API価格で全顧客に提供開始。
- **キーファクト:**
  - 新しいエージェント安全機能を追加
  - 標準API価格（トークン・ツール使用ベース）で提供
  - エンタープライズ向け機能強化
- **引用URL:** https://www.msn.com/en-us/news/technology/openai-updates-agents-sdk-to-improve-agent-safety-and-capability-for-enterprises/ar-AA20YD9F
- **Evidence ID:** EVD-20260508-0016

### INFO-017
- **タイトル:** Claude Agent SDK活発開発継続: v0.2.131リリース
- **ソース:** GitHub (anthropics/claude-agent-sdk-typescript)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** AnthropicのClaude Agent SDK（TypeScript）がv0.2.131に到達。高頻度リリースサイクル継続。Python版もclaude-agent-sdk-pythonとして提供。
- **キーファクト:**
  - TypeScript版 v0.2.131リリース（7時間以内）
  - Python版も活発に開発中
  - Claude Codeから抽出された上位レベルエージェントハーネス
  - プロプライエタリライセンスで提供
- **引用URL:** https://github.com/anthropics/claude-agent-sdk-typescript/releases
- **Evidence ID:** EVD-20260508-0017

### INFO-018
- **タイトル:** Anthropic Developer Platform: マルチエージェントセッションとwebhook追加
- **ソース:** Releasebot
- **公開日:** 2026-05-06
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Anthropic Developer Platformにマルチエージェントセッション・アウトカムのパブリックベータサポートと、Claude Managed Agents向けwebhookサポートを追加。
- **キーファクト:**
  - マルチエージェントセッション機能パブリックベータ
  - マルチエージェントアウトカム機能
  - Claude Managed Agents向けwebhook新規サポート
- **引用URL:** https://releasebot.io/updates/anthropic
- **Evidence ID:** EVD-20260508-0018

### INFO-019
- **タイトル:** Gemini Enterprise Agent Platform: エンタープライズAIエージェント構築プラットフォーム
- **ソース:** Google Cloud Documentation
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-002-01
- **関連企業:** Google
- **要約:** Google CloudがGemini Enterprise Agent Platformを提供開始。自律エージェントの構築・スケーリング・ガバナンス・最適化を統合プラットフォームで実現。
- **キーファクト:**
  - エンタープライズ向け自律エージェント構築・管理プラットフォーム
  - Cloud Next '26で導入
  - 複数ガイドで本番対応エージェント構築手法を提供
  - Deep Research AgentもAPI経由で利用可能
- **引用URL:** https://docs.cloud.google.com/gemini-enterprise-agent-platform
- **Evidence ID:** EVD-20260508-0019

### INFO-020
- **タイトル:** xAI Grok 4.3: 攻撃的低価格で新ボイスクローンスイート提供
- **ソース:** VentureBeat
- **公開日:** 2026-05-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** xAI
- **要約:** xAIがGrok 4.3を攻撃的低価格でリリース。Voice Agent APIは$3/時間（$0.05/分）。Google Cloud経由でもGrokモデル利用可能に。
- **キーファクト:**
  - Grok 4.3低価格でリリース
  - Voice Agent API（grok-voice-think-fast-1.0）$3/時間
  - Google Cloud Gemini Enterprise Agent Platform経由でGrok利用可能
  - Grok 4.20 Multi-AgentモデルもVercel経由で提供
  - OpenRouter経由でもAPI提供
- **引用URL:** https://venturebeat.com/technology/xai-launches-grok-4-3-at-an-aggressively-low-price-and-a-new-fast-powerful-voice-cloning-suite
- **Evidence ID:** EVD-20260508-0020

### INFO-021
- **タイトル:** ByteDance DeerFlow 2.0: スーパーエージェントフレームワーク
- **ソース:** GitHub (bytedance/deer-flow)
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-03
- **関連企業:** ByteDance
- **要約:** ByteDanceのDeerFlow 2.0がオープンソースの長期タスクSuperAgentハーネスとして展開。研究・コーディング・コンテンツ作成をサンドボックス・メモリ・ツール・サブエージェントで協調実行。AstraNL協調プロトコルも構築。
- **キーファクト:**
  - 長期タスクSuperAgentハーネス
  - サンドボックス・メモリ・ツール・スキル・サブエージェント統合
  - AstraNL協調プロトコル（実世界タスク管理、1%手数料）
  - Lark (Feishu) プラットフォームで154の実タスクシナリオでベンチマーク
  - 豆包の有料版ティーザー（App Store説明文更新）
- **引用URL:** https://github.com/bytedance/deer-flow/issues/2719
- **Evidence ID:** EVD-20260508-0021

### INFO-022
- **タイトル:** 2026年マルチエージェントフレームワーク比較: LangGraph・CrewAI・OpenAI Agents SDK等
- **ソース:** GuruSup
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** 複数
- **要約:** 2026年の主要マルチエージェントフレームワーク比較。OpenAI Agents SDK、LangGraph、CrewAI、AutoGen/AG2、Google ADKの6フレームワークを機能・適用領域別に比較。
- **キーファクト:**
  - LangGraph: 複雑なステートフルエージェントグラフに最適
  - CrewAI: マルチエージェント調整に最適
  - OpenAI Agents SDK: OpenAIエコシステム統合
  - Google ADK: Googleエコシステム向け
  - Microsoft AutoGen/AG2: エンタープライズ向け
- **引用URL:** https://gurusup.com/blog/best-multi-agent-frameworks-2026
- **Evidence ID:** EVD-20260508-0022

### INFO-023
- **タイトル:** Forbes: Anthropicへの全面依存に注意喚起
- **ソース:** Forbes
- **公開日:** 2026-05-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** ForbesのPatrick Moorheadが「Anthropicへの全面依存に注意」と記事。Anthropicの強力なAIモデルを認めつつ、恐怖戦術・セキュリティインシデント・サービス障害を指摘。
- **キーファクト:**
  - Anthropicのセキュリティインシデント懸念
  - サービス障害リスク指摘
  - 企業の単一ベンダー依存リスク警告
- **引用URL:** https://www.forbes.com/sites/patrickmoorhead/2026/05/05/enterprises-need-to-be-careful-before-they-go-all-in-on-anthropic/
- **Evidence ID:** EVD-20260508-0023

### INFO-024
- **タイトル:** Google Gemini API File Searchがマルチモーダル対応
- **ソース:** Google Blog
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04
- **関連企業:** Google
- **要約:** GoogleがGemini API File Searchをマルチモーダル対応に更新。カスタムメタデータとページレベル引用機能も追加。効率的で検証可能なRAG構築を支援。
- **キーファクト:**
  - マルチモーダルFile Search（画像・文書対応）
  - カスタムメタデータ機能
  - ページレベル引用機能
  - RAG精度向上
- **引用URL:** https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/
- **Evidence ID:** EVD-20260508-0024

### INFO-025
- **タイトル:** OpenAIがFedRAMP Moderate認証取得
- **ソース:** LinkedIn
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** OpenAI
- **要約:** OpenAIがFedRAMP Moderate認証を取得。連邦政府機関がFedRAMP認証環境内でGPT-5.5にアクセス可能に。
- **キーファクト:**
  - FedRAMP Moderate認証取得
  - 連邦政府機関向けGPT-5.5アクセス環境整備
  - エンタープライズセキュリティ要件の充足
- **引用URL:** https://www.linkedin.com/posts/ajongbloed_the-privacy-paradox-why-openai-is-building-activity-7455919851132497920-ReCg
- **Evidence ID:** EVD-20260508-0025

### INFO-026
- **タイトル:** EYがエンタープライズスケールAgentic AI OS構築
- **ソース:** EY
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** EY
- **要約:** EYがGenAIの成果をエンタープライズスケールのAgentic AIプラットフォームに統合。グローバルでの働き方変革とクライアントのAI加速を実現。
- **キーファクト:**
  - グローバルAgentic AIプラットフォーム構築
  - 働き方変革とクライアントAI加速の統合
- **引用URL:** https://www.ey.com/en_gl/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system
- **Evidence ID:** EVD-20260508-0026

### INFO-027
- **タイトル:** Agentic AI企業導入2026: 72%が本番稼働も60%ガバナンスギャップ
- **ソース:** Agentic AI Institute
- **公開日:** 2026-05-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-02, KIQ-001-02
- **関連企業:** 複数
- **要約:** Agentic AIの企業導入率が72%に到達（本番環境）。しかし60%のガバナンスギャップが存在し、リーダー向けフレームワーク構築が必要。
- **キーファクト:**
  - Agentic AI企業本番稼働率72%
  - 60%のガバナンスギャップ
  - ガバナンスフレームワーク構築の必要性
- **引用URL:** https://agenticaiinstitute.org/agentic-ai-enterprise-adoption-2026-governance-gap/
- **Evidence ID:** EVD-20260508-0027

### INFO-028
- **タイトル:** KPMG: エンタープライズAIエージェント戦略
- **ソース:** KPMG
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-02
- **関連企業:** KPMG
- **要約:** KPMGがCIO向けにAIエージェント戦略を発表。エージェントが価値を創出する領域とリスクを導入する領域を分析し、安全な運用方法を提示。
- **キーファクト:**
  - CIOのAIエージェントスケール圧力増大
  - 価値創出領域とリスク領域の分析
  - 安全な運用フレームワーク
- **引用URL:** https://kpmg.com/us/en/articles/2026/enterprise-ai-agents-strategy.html
- **Evidence ID:** EVD-20260508-0028

### INFO-029
- **タイトル:** Microsoft: エージェント・人間のエージェンシー・組織の機会
- **ソース:** Microsoft WorkLab
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-02, KIQ-004-01
- **関連企業:** Microsoft
- **要約:** MicrosoftがAIエージェントと人間のエージェンシーに関するレポート公開。エージェントが実行を担う中で人間のエージェンシーは拡大するが、組織がそれを捉えられるかが課題。
- **キーファクト:**
  - AIエージェントが実行を担当する構造
  - 人間のエージェンシー拡大の可能性
  - 組織設計の課題
- **引用URL:** https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
- **Evidence ID:** EVD-20260508-0029

### INFO-030
- **タイトル:** OracleがISO/IEC 42001:2023認証取得でAI信頼性向上
- **ソース:** Oracle Blog
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-03, KIQ-001-02
- **関連企業:** Oracle
- **要約:** OracleがISO/IEC 42001:2023認証を複数のAI管理システムで取得。AI管理の信頼性基準を引き上げ。
- **キーファクト:**
  - ISO/IEC 42001:2023認証取得
  - 複数のOracleサービスにまたがる認証
  - AI管理システムの信頼性基準設定
- **引用URL:** https://blogs.oracle.com/cloud-infrastructure/raising-the-bar-for-trustworthy-ai-at-oracle
- **Evidence ID:** EVD-20260508-0030

### INFO-031
- **タイトル:** Google Vertex AIがGemini Enterpriseへ進化
- **ソース:** AI CERTs
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** Google
- **要約:** GoogleがVertex AIからGemini Enterpriseへの転換を進行中。マイグレーションガイダンスと新機能を提供。
- **キーファクト:**
  - Vertex AIからGemini Enterpriseへの移行
  - エンタープライズAIプラットフォームの統合
  - Provisioned Throughput機能提供
- **引用URL:** https://www.aicerts.ai/news/google-pivot-vertex-ai-evolves-into-gemini-enterprise/
- **Evidence ID:** EVD-20260508-0031

### INFO-032
- **タイトル:** Linux FoundationがMCPをAgentic AI Foundation (AAIF)に統合
- **ソース:** The New Stack
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03
- **関連企業:** Anthropic, Linux Foundation
- **要約:** Linux FoundationがAnthropicから寄贈されたMCPをAgentic AI Foundation (AAIF)に統合。AAIFはMCP、Goose、AGENTS.mdの3プロジェクトを管理。Red HatがGold Memberとして参加。
- **キーファクト:**
  - AAIFは3プロジェクトを管理（MCP, Goose, AGENTS.md）
  - Anthropicが2025年12月にMCPをAAIFに寄贈
  - Red HatがGold Memberとして参加
  - MCPの採用が標準プロトコル以上の速度で進行
- **引用URL:** https://thenewstack.io/agentic-ai-foundation-launch/
- **Evidence ID:** EVD-20260508-0032

### INFO-033
- **タイトル:** Red Hat MCP Gateway: エンタープライズAIエージェントトラフィック制御
- **ソース:** Red Hat Blog
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Red Hat
- **要約:** Red HatがOpenShift向けMCP Gatewayをテクノロジープレビューとして提供。AIエージェントとMCPサーバー間のトラフィック制御をインフラ層で実現。
- **キーファクト:**
  - MCP Gateway for Red Hat OpenShift提供（テクノロジープレビュー）
  - AIエージェントとMCPサーバー間のインフラ層制御
  - トラフィックスケーリング機能
  - AAIF Gold Memberとしての貢献
- **引用URL:** https://www.redhat.com/en/blog/control-your-ai-agent-traffic-scale-model-context-protocol-gateway-red-hat-openshift-now-technology-preview
- **Evidence ID:** EVD-20260508-0033

### INFO-034
- **タイトル:** Visual StudioでMCP Server構築・利用が可能に
- **ソース:** Visual Studio Magazine
- **公開日:** 2026-05-05
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** Microsoft
- **要約:** Visual StudioでMCP Serverの構築と利用が可能に。LLMが外部データ（データベース・ファイル・API・ツール）にアクセスするためのユニバーサル標準。
- **キーファクト:**
  - Visual StudioでMCP Server構築・利用機能
  - データベース・ファイル・API・外部ツールへのアクセス標準化
- **引用URL:** https://visualstudiomagazine.com/articles/2026/05/05/building-and-using-mcp-servers-in-visual-studio.aspx
- **Evidence ID:** EVD-20260508-0034

### INFO-035
- **タイトル:** OpenAI Skills/Codexエコシステム展開
- **ソース:** GitHub (vercel-labs/skills)
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** OpenAI, Vercel
- **要約:** OpenAI Codexが.agents/skills/ディレクトリからスキルを読み込む標準規格。Vercelがオープンエージェントスキルツールを提供。Claude Codeプラグインマーケットプレイスとの互換性あり。
- **キーファクト:**
  - OpenAI Codexが.agents/skills/ディレクトリ標準を採用
  - Vercelがオープンエージェントスキルツール公開
  - Claude Codeプラグインマーケットプレイスとの互換性
  - Upskill: 10K+インデックスのスキルレジストリ（オープンソース）
  - KalturaがAI Agent Skillsスイートをオープンソース化
- **引用URL:** https://github.com/vercel-labs/skills
- **Evidence ID:** EVD-20260508-0035

### INFO-036
- **タイトル:** ServiceNow Build Agentが全主要AIコーディングツールで動作可能に
- **ソース:** ServiceNow Newsroom
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-001-01
- **関連企業:** ServiceNow
- **要約:** ServiceNow Build Agentが全主要AIコーディングツールで動作可能に。自然言語プロンプトで本番対応アプリとAIエージェントを構築。デフォルトでガバナンス適用。
- **キーファクト:**
  - 全主要AIコーディングツール対応
  - 自然言語プロンプトでの本番アプリ構築
  - デフォルトガバナンス適用
  - ServiceNow Studio内で完結
- **引用URL:** https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Build-Agent-now-works-inside-every-major-AI-coding-tool-governed-by-default/default.aspx
- **Evidence ID:** EVD-20260508-0036

### INFO-037
- **タイトル:** Anthropicのウォールストリート深化: Blackstone/H&F/GS JV $15億
- **ソース:** Fortune
- **公開日:** 2026-05-05
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-03, KIQ-003-04, KIQ-001-02
- **関連企業:** Anthropic
- **要約:** AnthropicがBlackstone、Hellman & Friedman、Goldman Sachsと$15億JVを設立し金融業界向けAIエージェント展開を強化。Jamie Dimonも注目。
- **キーファクト:**
  - $15億JV設立（Blackstone/H&F/Goldman Sachs）
  - 金融業界向けAIエージェント特化
  - Jamie Dimon（JPMorgan CEO）も注目
  - 製品発表の前日にJV発表
- **引用URL:** https://fortune.com/2026/05/05/anthropic-wall-street-financial-services-agents-jamie-dimon/
- **Evidence ID:** EVD-20260508-0037

### INFO-038
- **タイトル:** ServiceNow-Microsoft統合: AIエージェントガバナンス拡大
- **ソース:** ServiceNow Newsroom
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03, KIQ-002-01
- **関連企業:** ServiceNow, Microsoft
- **要約:** ServiceNowがMicrosoftとの統合でAIエージェントガバナンスを拡大。ServiceNow AI Control TowerとMicrosoft Agent間の深い統合を実現。
- **キーファクト:**
  - ServiceNow AI Control TowerとMicrosoft Agentの深統合
  - エンタープライズAIエージェントガバナンス拡大
- **引用URL:** https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-expands-AI-agent-governance-through-deeper-integration-with-Microsoft/default.aspx
- **Evidence ID:** EVD-20260508-0038

### INFO-039
- **タイトル:** AIエージェント市場2033年に$1829.7億規模予測（CAGR 49.6%）
- **ソース:** TechAhead
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-02
- **関連企業:** 複数
- **要約:** AIエージェント市場が2026-2033年にCAGR 49.6%で成長し、2033年に$1829.7億に到達予測。92%のリーダーがAIエージェントがビジネスに影響と回答。
- **キーファクト:**
  - 市場規模予測: 2033年$1829.7億
  - CAGR 49.6%（2026-2033）
  - 92%のリーダーがビジネス影響を認識
- **引用URL:** https://www.techaheadcorp.com/blog/top-use-cases-of-agentic-ai-in-2026-across-industries/
- **Evidence ID:** EVD-20260508-0039

### INFO-040
- **タイトル:** BenchLMマルチモーダルベンチマーク: Gemini 3 Pro Deep Think 100%で首位
- **ソース:** BenchLM
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** Google, xAI
- **要約:** 2026年5月時点のマルチモーダルベンチマークでGemini 3 Pro Deep Thinkが加重スコア100.0%で首位。Grok 4.1が97.8%で2位。
- **キーファクト:**
  - Gemini 3 Pro Deep Think: 100.0%（マルチモーダル&グラウンデッド首位）
  - Grok 4.1: 97.8%
  - MMMU, OfficeQA, CharXiv等の複合評価
- **引用URL:** https://benchlm.ai/multimodal-grounded
- **Evidence ID:** EVD-20260508-0040

### INFO-041
- **タイトル:** GPT-5.5がTerminal-Bench 2.0で82.7%、DeepSeek V4が1Mコンテキスト圧縮
- **ソース:** The Living Edge
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-04, KIQ-003-02
- **関連企業:** OpenAI, DeepSeek
- **要約:** GPT-5.5がTerminal-Bench 2.0で82.7%を達成。DeepSeek V4が1MトークンコンテキストをKVキャッシュの10%に圧縮。マルチモーダルAIのエージェント化が進行。
- **キーファクト:**
  - GPT-5.5: Terminal-Bench 2.0で82.7%
  - DeepSeek V4: 1Mトークンコンテキストを10%に圧縮
  - Nemotron 3 Nano Omni: マルチモーダル統合
- **引用URL:** https://thelivingedge.substack.com/p/last-week-in-multimodal-ai-55-the
- **Evidence ID:** EVD-20260508-0041

### INFO-042
- **タイトル:** Google "Remy" AIエージェントをGemini内でテスト中
- **ソース:** AI News
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-04, KIQ-001-01
- **関連企業:** Google
- **要約:** GoogleがGemini内でコードネーム"Remy"のAIエージェントをテスト。ユーザーのためにアクションを実行し、関連情報を監視、嗜好を学習。
- **キーファクト:**
  - Gemini内で"Remy" AIエージェントテスト中
  - ユーザー嗜好学習機能
  - 情報監視・自動アクション実行
  - Google DeepMind Gemini Roboticsも展開（物理世界AI）
- **引用URL:** https://www.artificialintelligence-news.com/news/google-remy-ai-agent-gemini-user-control/
- **Evidence ID:** EVD-20260508-0042

### INFO-043
- **タイトル:** NVIDIA OpenShell: 自律AIエージェント向け安全ランタイム
- **ソース:** GitHub (NVIDIA/OpenShell)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05, KIQ-001-01
- **関連企業:** NVIDIA, ServiceNow
- **要約:** NVIDIAがOpenShellをオープンソース公開。自律AIエージェント向けの安全・プライベートなサンドボックス実行環境。ServiceNowとの提携でProject Arcとして展開。
- **キーファクト:**
  - サンドボックス実行環境でデータ・資格情報保護
  - ServiceNowとの提携（Project Arc）
  - ポリシーガバナンス付き環境
  - ホスト型コンテナまたは独自ランタイムで動作
- **引用URL:** https://github.com/NVIDIA/OpenShell
- **Evidence ID:** EVD-20260508-0043

### INFO-044
- **タイトル:** Anthropic Sandbox Runtime: Claude Code向け安全実行環境
- **ソース:** GitHub (anthropic-experimental/sandbox-runtime)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-05
- **関連企業:** Anthropic
- **要約:** AnthropicがClaude Code向けSandbox Runtimeを研究プレビューとしてオープンソース公開。安全なAIエージェント実行を支援。
- **キーファクト:**
  - Claude Code向けサンドボックスランタイム
  - 早期オープンソースプレビュー
  - ファイルシステム・ネットワーク・プロセス実行の制御
- **引用URL:** https://github.com/anthropic-experimental/sandbox-runtime
- **Evidence ID:** EVD-20260508-0044

### INFO-045
- **タイトル:** 200,000のMCPサーバーにコマンド実行脆弱性
- **ソース:** VentureBeat
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** 複数
- **要約:** OX Securityが6つのライブプラットフォームで任意コマンド実行を確認。推定200,000のMCPサーバーが露出。MCPのエコシステム急拡大に伴うセキュリティリスク。
- **キーファクト:**
  - MCP STDIO脆弱性で任意コマンド実行可能
  - 6つのライブプラットフォームで確認
  - 推定200,000サーバーが露出
  - エコシステム急拡大に伴う品質リスク
- **引用URL:** https://venturebeat.com/security/mcp-stdio-flaw-200000-ai-agent-servers-exposed-ox-security-audit
- **Evidence ID:** EVD-20260508-0045

### INFO-046
- **タイトル:** Claude Code MCP Token Theft: 中間者攻撃の脆弱性
- **ソース:** Mitiga Labs
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Mitiga LabsがClaude Code MCP設定変更によるOAuthトラフィックリダイレクト攻撃を実証。SaaSトークンの露出リスク。
- **キーファクト:**
  - MCP設定変更でOAuthトラフィックリダイレクト
  - ローテーション後もSaaSトークン露出
  - 中間者攻撃ベクトル
- **引用URL:** https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm
- **Evidence ID:** EVD-20260508-0046

### INFO-047
- **タイトル:** Claude Skills Marketplace: 16→900,000+に爆発的成長
- **ソース:** X (Twitter)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-05, KIQ-001-03
- **関連企業:** Anthropic
- **要約:** Claude Skills Marketplaceが2025年10月の16公式スキルから2026年5月に900,000+コミュニティスキルに爆発的成長。ただし大部分はノイズ。
- **キーファクト:**
  - 2025年10月: 16公式スキル
  - 2026年5月: 900,000+コミュニティスキル
  - 大部分はノイズ（品質課題）
- **引用URL:** https://x.com/josephfounder/status/2051732230934872403
- **Evidence ID:** EVD-20260508-0047

### INFO-048
- **タイトル:** Agentic AIがエンタープライズソフトウェア経済を変革
- **ソース:** arXiv
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-05, KIQ-003-05
- **関連企業:** 複数
- **要約:** arXiv論文「How Agentic AI Changes the Economics of Enterprise Software」で、ベンダーロックインメカニズムが全提供モデルで継続し、AI機能の組み込みでスイッチングコストが追加的に深化していると分析。
- **キーファクト:**
  - ベンダーロックインが全デリバリーモデルで継続
  - AI機能の組み込みでスイッチングコストが深化
  - エンタープライズソフトウェア経済への構造的影響
- **引用URL:** https://arxiv.org/html/2604.26482v2
- **Evidence ID:** EVD-20260508-0048

### INFO-049
- **タイトル:** $570Kのカナリア: AIコーディングエージェントが示すエンタープライズAIのギャップ
- **ソース:** CIO
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-05, KIQ-004-02
- **関連企業:** 複数
- **要約:** CIO記事でAIコーディングエージェントが示すエンタープライズAIの実際のギャップを分析。エンジニアリング外ではAIエージェントの意思決定が不透明で監査証跡がない。
- **キーファクト:**
  - エンジニアリング外のAIエージェント意思決定の不透明性
  - 顧客対応エージェントの監査証跡欠如
  - $570Kの事例で実態を提示
- **引用URL:** https://www.cio.com/article/4166029/the-570k-canary-what-ai-coding-agents-reveal-about-enterprise-ais-real-gaps.html
- **Evidence ID:** EVD-20260508-0049

### INFO-050
- **タイトル:** AWS Bedrock AgentCore: 決済・ファイルシステム・Identity機能追加
- **ソース:** AWS Blog
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01
- **関連企業:** Amazon
- **要約:** AWSがBedrock AgentCoreに決済機能（Coinbase/Stripe提携）、BYOファイルシステム（S3/EFS）、Identity（スタンドアロンサービス）を追加。AIエージェントの取引・アクセス管理を強化。
- **キーファクト:**
  - AgentCore Payments: API/MCPサーバーへの自律的アクセス・支払い（プレビュー）
  - AgentCore Runtime: BYOファイルシステム対応
  - AgentCore Identity: スタンドアロン提供
  - Coinbase/Stripeと共同構築
  - WorkSpacesでレガシーデスクトップアプリにAIエージェント操作を可能に（IAM認証+MCP）
- **引用URL:** https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview
- **Evidence ID:** EVD-20260508-0050

### INFO-051
- **タイトル:** Microsoft Agent 365 GA: エンタープライズAIエージェント管理プラットフォーム
- **ソース:** Microsoft Security Blog
- **公開日:** 2026-05-01
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-002-01, KIQ-001-02
- **関連企業:** Microsoft
- **要約:** Microsoft Agent 365が一般提供開始。AIエージェントのスケーリング・ガバナンス・エンタープライズセキュリティを統合管理。Microsoft Foundryとして統合プラットフォームも展開。
- **キーファクト:**
  - Agent 365がGA（一般提供開始）
  - エンタープライズグレードのセキュリティとコントロール
  - AIエージェントのガバナンスとスケーリング
  - Microsoft Foundry: 統合Azure PaaS
  - Azure AI Foundry: エージェント構築・デプロイ・ガバナンス
- **引用URL:** https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/
- **Evidence ID:** EVD-20260508-0051

### INFO-052
- **タイトル:** GPT-5.5価格2倍に上昇: 入力$5/M、出力$30/M
- **ソース:** OpenRouter
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** OpenAI
- **要約:** GPT-5.5の価格がGPT-5.4比2倍に上昇。入力トークン$2.50/M→$5.00/M、出力$15/M→$30/M。一方でGPT-5.5 Instantはデフォルトモデルとして追加料金なし。
- **キーファクト:**
  - GPT-5.5: 入力$5.00/M（GPT-5.4比2倍）
  - 出力$30/M（GPT-5.4比2倍）
  - 同等テキストで最大35%トークン増加の報告
  - GPT-5.5 Instantはデフォルトで追加料金なし
- **引用URL:** https://openrouter.ai/announcements/gpt55-cost-analysis
- **Evidence ID:** EVD-20260508-0052

### INFO-053
- **タイトル:** ベンチマーク性能と実運用性能の乖離が拡大
- **ソース:** Reddit
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** 複数
- **要約:** AIコミュニティでベンチマーク性能と実際のデプロイ性能の乖離が議論。MMLU/GPQA/SWE-bench/ARC-AGI等の指標が実用性を反映しなくなっている。
- **キーファクト:**
  - ベンチマークと実運用のパフォーマンス乖離拡大
  - MMLU/GPQA/SWE-bench/ARC-AGIの限界
  - 実用性を反映しない指標への懸念
- **引用URL:** https://www.reddit.com/r/ArtificialInteligence/comments/1t48g84/benchmark_performance_and_deployed_performance/
- **Evidence ID:** EVD-20260508-0053

### INFO-054
- **タイトル:** Hermesモデル: GPQA Diamond 94.1%、ARC-AGI-2 77.1%で最高スコア
- **ソース:** Hermes
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** 複数
- **要約:** HermesモデルがGPQA Diamond 94.1%、ARC-AGI-2 77.1%で両最難関推論ベンチマークの最高スコアを達成。AIMEでも完璧に近いスコア。
- **キーファクト:**
  - GPQA Diamond: 94.1%（最高）
  - ARC-AGI-2: 77.1%（最高）
  - AIME: ほぼ完璧
- **引用URL:** https://get-hermes.ai/models/
- **Evidence ID:** EVD-20260508-0054

### INFO-055
- **タイトル:** Moonshot AIが$20億調達、評価額$200億超え
- **ソース:** Yahoo Finance
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Moonshot AI
- **要約:** 中国AI企業Moonshot AIが最新ラウンドで$20億を調達。評価額が$200億を超過。中国AIへの投資家の食欲継続を示す信号。
- **キーファクト:**
  - $20億調達
  - 評価額$200億超
  - 中国AIチャレンジャーへの投資家食欲継続
- **引用URL:** https://finance.yahoo.com/sectors/technology/articles/moonshot-ai-raises-2-billion-184456897.html
- **Evidence ID:** EVD-20260508-0055

### INFO-056
- **タイトル:** Sierra（Bret Taylor）が$9.5億 Series E調達
- **ソース:** CNBC
- **公開日:** 2026-05-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Sierra
- **要約:** Bret TaylorのSierraがSeries Eで$9.5億を調達。TigerとGoogle GVがリード。Benchmark、Sequoia、Greenoaks等も参加。
- **キーファクト:**
  - $9.5億 Series E
  - Tiger/GVリード
  - Benchmark/Sequoia/Greenoaks参加
- **引用URL:** https://www.cnbc.com/2026/05/04/bret-taylor-sierra-fundraise-openai.html
- **Evidence ID:** EVD-20260508-0056

### INFO-057
- **タイトル:** Perplexity AI評価額$180億に上昇、$1億調達
- **ソース:** Facebook/Bloomberg
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Perplexity AI
- **要約:** Perplexity AIの評価額が$180億に上昇。$1億の追加調達を完了。
- **キーファクト:**
  - 評価額$180億
  - $1億追加調達
- **引用URL:** https://www.facebook.com/bloombergbusiness/posts/brazilian-ai-legal-startup-enter-has-tripled-its-valuation-to-12-billion-in-a-ne/1391170289535727/
- **Evidence ID:** EVD-20260508-0057

### INFO-058
- **タイトル:** 中国がMetaのManus買収（$20億）を解散命令
- **ソース:** OMM Law
- **公開日:** 2026-04-27
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-002-03
- **関連企業:** Meta
- **要約:** 中国国家発展改革委員会（NDRC）がMetaのAIスタートアップManus買収（$20億）の解散を命令。クロスボーダーAI取引への規制介入。
- **キーファクト:**
  - NDRCが解散命令（4月27日）
  - Meta $20億買収の巻き戻し
  - クロスボーダーAI取引への規制リスク
  - 中国のAI資産保護姿勢
- **引用URL:** https://www.omm.com/insights/alerts-publications/china-unwinds-meta-s-acquisition-of-manus-implications-for-cross-border-ai-transactions/
- **Evidence ID:** EVD-20260508-0058

### INFO-059
- **タイトル:** MetaがロボティクススタートアップARIを買収、ヒューマノイドAI強化
- **ソース:** TechCrunch
- **公開日:** 2026-05-01
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04, KIQ-001-04
- **関連企業:** Meta
- **要約:** MetaがヒューマノイドスタートアップAssured Robot Intelligence (ARI)を買収。ロボット向けAIモデルの強化が目的。
- **キーファクト:**
  - ARI買収（ヒューマノイドスタートアップ）
  - ロボット向けAIモデル強化
- **引用URL:** https://techcrunch.com/2026/05/01/meta-buys-robotics-startup-to-bolster-its-humanoid-ai-ambitions/
- **Evidence ID:** EVD-20260508-0059

### INFO-060
- **タイトル:** NebiusがAIスタートアップEigen AIを$6.43億で買収合意
- **ソース:** Bloomberg Law
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Nebius
- **要約:** クラウドプロバイダーNebius GroupがAIスタートアップEigen AIを$6.43億で買収合意。AIタスク向けチップ性能向上技術を獲得。
- **キーファクト:**
  - $6.43億買収
  - AIチップ性能向上技術獲得
  - クラウドAIインフラ強化
- **引用URL:** https://news.bloomberglaw.com/mergers-and-acquisitions/cloud-provider-nebius-agrees-to-buy-ai-startup-for-615-million
- **Evidence ID:** EVD-20260508-0060

### INFO-061
- **タイトル:** 製品未発売のAIスタートアップが$10億シード調達
- **ソース:** Puck News
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Ineffable Intelligence
- **要約:** Ineffable Intelligenceが製品なしで$10億シードラウンドを調達。AIシンギュラリティの懸念が投資競争を加速。
- **キーファクト:**
  - 製品未発売で$10億シード調達
  - AI投資バブルの極端な事例
  - シンギュラリティ懸念が投資を加速
- **引用URL:** https://puck.news/inside-the-ai-startups-worth-billions-before-launch/
- **Evidence ID:** EVD-20260508-0061

### INFO-062
- **タイトル:** EU AI Act: 2026年8月2日施行に向けた準備課題
- **ソース:** IAPP
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** EU AI Actの2026年8月2日施行に向け、SMEの証拠ギャップや遵守体制の不備が課題に。違反時の罰金は最大1500万ユーロまたは世界年商の3%。
- **キーファクト:**
  - 2026年8月2日施行（変更なし）
  - 罰金: 最大1500万ユーロまたは年商3%
  - SMEの証拠ギャップ課題
  - 欧州委員会が実装緩和策を発表
- **引用URL:** https://iapp.org/news/a/eu-ai-act-deployer-evidence-gaps-smes-will-miss-before-2-aug-2026
- **Evidence ID:** EVD-20260508-0062

### INFO-063
- **タイトル:** 中国が未成年者向けAIパートナー禁止、AIエージェント安全規格を発表
- **ソース:** AI Safety China
- **公開日:** 2026-05-08
- **信頼性コード:** C-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** 中国の主要規格策定機関がAIエージェント安全に関する90ページの報告書を公開。11の脅威を分類し8つの新規格を提案。
- **キーファクト:**
  - 未成年者向けAIパートナー禁止
  - AIエージェント安全報告書（90ページ）
  - 11の脅威分類・8つの新規格提案
  - 暫定的対応から体系的規格への移行
- **引用URL:** https://aisafetychina.substack.com/p/china-bans-ai-partners-for-minors
- **Evidence ID:** EVD-20260508-0063

### INFO-064
- **タイトル:** ペンタゴン7社AI契約: SpaceX/Google/OpenAI等
- **ソース:** The Guardian
- **公開日:** 2026-05-01
- **信頼性コード:** B-1
- **関連KIQ:** KIQ-002-06
- **関連企業:** SpaceX, OpenAI, Google, Nvidia
- **要約:** ペンタゴンがSpaceX、OpenAI、Google、Nvidia、Reflection他7社と機密軍事AI契約を締結。米軍の「AI-first」戦力化方針。
- **キーファクト:**
  - 7社と機密軍事AI契約
  - 米軍「AI-first」戦力化宣言
  - SpaceX/OpenAI/Google/Nvidia/Reflection参加
  - 2026年4月30日発表
- **引用URL:** https://www.theguardian.com/us-news/2026/may/01/pentagon-us-military-pairs-with-spacex-google-openai
- **Evidence ID:** EVD-20260508-0064

### INFO-065
- **タイトル:** ペンタゴンがScale AIに$5億契約（Meta 49%出資）
- **ソース:** Forbes
- **公開日:** 2026-05-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Scale AI, Meta
- **要約:** ペンタゴンがMeta 49%出資のScale AIに$5億契約を授与。前年比5倍。データ分析・意思決定支援。
- **キーファクト:**
  - $5億契約（前年比5倍）
  - Meta 49%出資のScale AI
  - データ分析・意思決定支援
- **引用URL:** https://www.forbes.com/sites/aliciapark/2026/05/06/pentagon-hands-meta-backed-scale-ai-500-million-contract-5-times-last-years-deal-report-says/
- **Evidence ID:** EVD-20260508-0065

### INFO-066
- **タイトル:** Google従業員がペンタゴンAI契約に反対の公開書簡
- **ソース:** Fortune
- **公開日:** 2026-05-04
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Google
- **要約:** GoogleのペンタゴンAI契約に対し、数百人の従業員が反対の公開書簡に署名。2018年Project Maven抗議の再来。経営陣は当初動揺も最終的に契約継持。
- **キーファクト:**
  - 数百人のGoogle従業員が公開書簡で反対
  - Project Maven（2018年）の再来
  - 経営陣は動揺後も契約継持
  - 従業員の発言力がProject Maven時より低下
- **引用URL:** https://fortune.com/2026/05/04/google-employee-backlash-pentagon-ai-contract-power-waned-since-project-maven/
- **Evidence ID:** EVD-20260508-0066

### INFO-067
- **タイトル:** AIがエントリーレベルの雇用を消滅させる可能性
- **ソース:** Forbes
- **公開日:** 2026-05-04
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01, KIQ-004-02
- **関連企業:** 複数
- **要約:** AIがエントリーレベルの雇用（マーケティング・法務・ソフトウェア開発・CS）を急速に再構築。2026年クラスの卒業生の89%がAI/自動化による代替に懸念（2025年64%から上昇）。MIT専門家は若年層雇用の自動化がバックファイアする可能性を警告。
- **キーファクト:**
  - 2026年クラス卒業生の89%が代替に懸念（前年64%）
  - マーケティング・法務・SWE・CSで特に影響
  - MIT Andrew McAfee: タレントパイプラインリスク警告
  - AI企業自体は積極的に新卒採用
  - 5年以内にエントリーホワイトカラー50%消失の予測
- **引用URL:** https://www.forbes.com/sites/bernardmarr/2026/05/04/ai-could-wipe-out-entry-level-jobs-and-that-should-terrify-business-leaders/
- **Evidence ID:** EVD-20260508-0067

### INFO-068
- **タイトル:** AIコーディングツール三極: GitHub Copilot・Cursor・Claude Code
- **ソース:** 複数
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** Microsoft, Anthropic
- **要約:** 2026年のAIコーディングツール市場でGitHub Copilot（エンタープライズ採用首位・47%）、Cursor（開発者選好）、Claude Code（Anthropic）が三極。GitHub Copilotは従量課金への移行を発表。
- **キーファクト:**
  - GitHub Copilot: 47%採用・エンタープライズ首位
  - Cursor: 開発者選好で急成長
  - Claude Code: Anthropic提供の競合
  - GitHub Copilotの従量課金移行
- **引用URL:** https://dancumberlandlabs.com/blog/best-ai-coding-tools/
- **Evidence ID:** EVD-20260508-0068

### INFO-069
- **タイトル:** Hassabis: 2020年代末までにAGI到達50%確率
- **ソース:** Medium
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google DeepMind
- **要約:** DeepMind CEO Demis HassabisがDavos 2026で2020年代末までのAGI到達確率を約50%と予測。最も正直なAGIテストを提案。
- **キーファクト:**
  - Hassabis: 2020年代末AGI確率約50%
  - 最も正直なAGIテストを提案
  - Dario Amodei: 2026年中に強力なAI予測
  - Sam Altman: レベル3 AGI到達近いと予測
  - Altman/Amodeiへの信頼性にコミュニティ懐疑
- **引用URL:** https://medium.com/predict/deepminds-ceo-proposed-the-most-honest-agi-test-anyone-has-suggested-and-he-says-today-s-systems-45e23f18b57c
- **Evidence ID:** EVD-20260508-0069

### INFO-070
- **タイトル:** ASIモラトリアムは自己利益から可能: ゲーム理論分析
- **ソース:** arXiv
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** arXiv論文がゲーム理論を用いて、ASI（人工超知能）モラトリアムが自己利益から実現可能であると論証。通念に反する結論。
- **キーファクト:**
  - ゲーム理論でASIモラトリアムの可能性を論証
  - 通念に反する結論（モラトリアムは自己利益と両立）
  - AGI arms raceの文脈設定
- **引用URL:** https://arxiv.org/pdf/2605.01297
- **Evidence ID:** EVD-20260508-0070

### INFO-071
- **タイトル:** ByteDance DeerFlow/Coze/豆包中国語最新動向
- **ソース:** 複数
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** ByteDance DeerFlow 2.0が長期タスクSuperAgentとして展開。Cozeは179 RMB/月のノーコードエージェント、豆包は有料版ティーザー（App Store説明文更新）。DeepSeek V4-Proは最安価格競争力の低下に直面。
- **キーファクト:**
  - DeerFlow 2.0: 研究・コーディング・作成SuperAgent
  - Coze: 179 RMB/月ノーコードエージェント
  - 豆包: 有料版ティーザー（App Store更新）
  - Seed 2.0/3D+有料版追加
  - DeepSeek V4-Pro価格競争力低下
- **引用URL:** https://github.com/bytedance/deer-flow
- **Evidence ID:** EVD-20260508-0071

### INFO-072
- **タイトル:** Claude Code: JetBrains調査で46%が最も好まれるAIコーディングツール
- **ソース:** ByteIota/Releasebot
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-AGENT-001（動的追加）
- **関連企業:** Anthropic
- **要約:** JetBrains April 2026調査で開発者の46%がClaude Codeを最も好まれるAIコーディングツールと評価（Copilot 9%）。Anthropic Enterprise Analytics APIでDAU/WAU/MAU追跡可能に。ただし定量ユーザー数は非公開。
- **キーファクト:**
  - JetBrains調査: Claude Code 46%、Copilot 9%
  - Enterprise Analytics APIでDAU/WAU/MAU提供開始
  - Cursorが$20億評価額
  - CodexがClaude Codeとの差を急速に縮小（4月16日リローンチ）
  - 定量WAU/MAU数値は依然非公開（KIQ-AGENT-001 30R連続未回答継続）
- **引用URL:** https://byteiota.com/claude-cowork-enterprise-rbac-and-analytics-without-the-paywall/
- **Evidence ID:** EVD-20260508-0072

### INFO-073
- **タイトル:** DeepSeek $500億評価額で中国政府系ファンドが主導
- **ソース:** WSJ/Reuters
- **公開日:** 2026-05-06
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-BTD-PRICE（動的追加）
- **関連企業:** DeepSeek
- **要約:** DeepSeekが中国政府系投資家からの資金調達を進行中。評価額$450-500億。中国チップセクター投資ファンドが主導。DeepSeek V4価格はOpenAI比97%安、V4 Proは75%オフ（5月31日まで）。中国政府補助金の依存が指摘される。
- **キーファクト:**
  - 評価額$450-500億で初の外部資金調達
  - 中国政府系チップファンドが主導
  - V4価格: OpenAI比97%安
  - V4 Pro: 75%オフ（5/31まで）
  - Hacker News: 「中国政府に補助金されている」との指摘
  - 価格持続可能性に重大な疑問（政府依存度）
- **引用URL:** https://www.wsj.com/tech/ai/china-to-invest-in-deepseek-at-50-billion-valuation-045041d0
- **Evidence ID:** EVD-20260508-0073

### INFO-074
- **タイトル:** OpenAI $100億JV（Goldman Sachs/Blackstone）: FDEモデルの展開
- **ソース:** Yahoo Finance/Michael Parekh
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** Pattern B JV追跡（動的追加）
- **関連企業:** OpenAI
- **要約:** OpenAIがGoldman Sachs/Blackstone等のPEファームと$100億JVを設立。FDEモデル（Palantir型）でエンタープライズ展開。Anthropicも同週にBlackstone/H&F/GS JV設立。
- **キーファクト:**
  - $100億JV（OpenAI + Goldman Sachs/Blackstone）
  - Palantir型FDE（Forward Deployed Engineer）モデル
  - PEポートフォリオ企業へのAI展開
  - Anthropicも同週に$15億JV設立（統計的非随意性）
- **引用URL:** https://michaelparekh.substack.com/p/ais-forward-deployment-fdes-go-from
- **Evidence ID:** EVD-20260508-0074

### INFO-075
- **タイトル:** ServiceNow-Accenture FDEプログラム開始: Agentic AIの本番スケール
- **ソース:** ServiceNow/Accenture
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** Pattern B JV追跡（動的追加）
- **関連企業:** ServiceNow, Accenture
- **要約:** ServiceNowとAccentureがForward Deployed Engineeringプログラムを開始。Agentic AIのエンタープライズ展開を本番スケールで推進。
- **キーファクト:**
  - ServiceNow-Accenture共同FDEプログラム
  - Agentic AI本番ワークロードへの移行
  - 相互顧客のビジネス目標を価値生成に変換
- **引用URL:** https://newsroom.accenture.com/news/2026/servicenow-and-accenture-launch-forward-deployed-engineering-program-to-scale-agentic-ai-across-the-enterprise
- **Evidence ID:** EVD-20260508-0075

### INFO-076
- **タイトル:** Google Workspace Gemini: 無料組み込みで囲い込み強化
- **ソース:** 複数
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** H-GOO-002 I探索（動的追加）
- **関連企業:** Google
- **要約:** GoogleがWorkspace加入者向けにGeminiを追加コストなしで提供し囲い込み強化。Gemini Enterprise AppにProjects（エージェント専用ワークスペース）とSkills機能を追加。無料層ですぐ利用可能。
- **キーファクト:**
  - Workspace加入者向けGemini無料提供
  - Gemini Enterprise App: Projects + Skills追加
  - エージェント専用ワークスペース（スコープ付きメモリ）
  - Google Cloud Next '26で25の主要発表
  - 囲い込み指標: Workspace統合→Vertex深結合→Android組み込み
- **引用URL:** https://medium.com/google-cloud/google-cloud-next-26-top-25-announcements-that-actually-matter-9d92beb3376f
- **Evidence ID:** EVD-20260508-0076

### INFO-077
- **タイトル:** BLS産業分類改定で約10%の雇用が再分類
- **ソース:** Reuters
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** H-CAR-002 BLS確認（動的追加）
- **関連企業:** 複数
- **要約:** BLSが産業分類システムを改定し、約10%の雇用が異なる産業に再分類。プログラマー→SE呼称変更の影響は直接確認できず。3R連続未解決継続。
- **キーファクト:**
  - BLS産業分類改定で約10%再分類
  - プログラマー→SE呼称変更影響の直接確認なし
  - 3R連続未解決継続（KIQ条件）
- **引用URL:** https://www.facebook.com/Reuters/posts/-the-us-labor-market-is-holding-firm-despite-the-oil-shock-to-learn-why-hiring-h/1540042961319764/
- **Evidence ID:** EVD-20260508-0077

### INFO-078
- **タイトル:** Google DeepMind AI Co-Clinician: GPT-5.4に63%対30%で勝利
- **ソース:** MindStudio
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** Google
- **要約:** Google DeepMindのAI Co-ClinicianがGPT-5.4に63%対30%で勝利。98クエリ中97でクリティカルエラーなし。140の診療次元の68で医師と同等。
- **キーファクト:**
  - GPT-5.4対比63%対30%で勝利
  - 98クエリ中97でクリティカルエラーなし
  - 140診療次元の68で医師と同等
- **引用URL:** https://www.mindstudio.ai/blog/google-deepmind-ai-co-clinician-4-benchmark-results-surprised-evaluators/
- **Evidence ID:** EVD-20260508-0078

### INFO-079
- **タイトル:** Andrej Karpathy: 「Vibe Coding」から「Agentic Engineering」へ移行宣言
- **ソース:** SD Times/Medium
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-02, KIQ-001-01
- **関連企業:** 複数
- **要約:** Andrej Karpathyが「vibe coding」の1周年に「agentic engineering」への移行を宣言。「思考は外注できるが理解は外注できない」と強調。Vibe codingは床を上げるが天井は上げない。
- **キーファクト:**
  - Vibe Coding → Agentic Engineering移行宣言
  - 「思考は外注できるが理解は外注できない」
  - Vibe codingは床を上げるが天井は上げない
  - Software 3.0はpromptingでありcodingではない
- **引用URL:** https://sdtimes.com/ai/andrej-karpathy-has-renamed-vibe-coding-heres-what-engineering-leaders-need-to-do-about-it/
- **Evidence ID:** EVD-20260508-0079

### INFO-080
- **タイトル:** Omnicom: 広告テクノロジー中間業者の排除を宣言
- **ソース:** The State of Streaming
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Omnicom
- **要約:** OmnicomがAIマーケティングプラットフォーム「Omni」でad-tech中間業者の排除を宣言。Acxiomのファーストパーティデータ層を使用しAIエージェントが取引。
- **キーファクト:**
  - Omni AIプラットフォームで中間業者排除
  - Acxiomファーストパーティデータ活用
  - AIエージェントによる自動取引
  - Agentic Commerceモデルの展開
- **引用URL:** https://thestateofstreaming.com/advertising-adtech/2026/05/omnicom-ai-agent-adtech-disintermediation/
- **Evidence ID:** EVD-20260508-0080

### INFO-081
- **タイトル:** Klarna労働力40%削減、AIが700 CS役割相当を処理
- **ソース:** LinkedIn
- **公開日:** 2026-05-08
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** Klarna CEOが労働力を40%削減（7400→3400）。AIアシスタントが700 CS役割相当を処理。Duolingoは「AI-first」宣言。2026年4月、AI実装が2ヶ月連続でレイオフ理由の首位に。
- **キーファクト:**
  - Klarna: 労働力40%削減（7400→3400）
  - AIアシスタント: 700 CS役割相当を処理
  - Duolingo: AI-first宣言
  - 2026年4月: AI実装がレイオフ理由首位（2ヶ月連続）
  - 882テック職/日が消失中
- **引用URL:** https://www.thecscafe.com/p/cs-org-defense-ai-headcount-review
- **Evidence ID:** EVD-20260508-0081

### INFO-082
- **タイトル:** NVIDIA $21億投資: IREN AIデータセンター契約
- **ソース:** Reuters
- **公開日:** 2026-05-07
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** NVIDIA
- **要約:** NVIDIAがデータセンター運営IRENに最大$21億を投資。5GWのインフラ展開。Goldman SachsはAIインフラ投資が数兆ドル規模に達すると分析。
- **キーファクト:**
  - NVIDIA: IRENに最大$21億投資
  - 5GWインフラ展開計画
  - Goldman Sachs: AIインフラ投資は数兆ドル規模
  - 電力はシリコン・DC建設に比べて相対的に小規模
- **引用URL:** https://www.reuters.com/business/nvidia-invest-up-21-billion-iren-part-ai-data-center-deal-2026-05-07/
- **Evidence ID:** EVD-20260508-0082

### INFO-083
- **タイトル:** 豆包（Doubao）有料版ローンチ: 68-500元/月の3段階
- **ソース:** 新京報/新浪財経
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** 豆包が5月に3段階有料版をローンチ（標準版68元/月、強化版200元/月、専門版500元/月）。Coze（扣子）は2024年から開発者向け有料化済み、2026年1月に個人版19.9-99元/月追加。Seedance 2.0動画生成モデルを豆包に無料統合。
- **キーファクト:**
  - 有料版3段階: 68/200/500元/月
  - Coze: 開発者向け有料化済み（2024年）、個人版19.9-99元/月
  - Seedance 2.0動画生成を無料統合
  - Doubao-Seed-2.0-lite: 初の全モダリティ理解モデル
  - 動画・画像・音声・テキストの統一処理
- **引用URL:** https://www.bjnews.com.cn/detail/1778131853129431.html
- **Evidence ID:** EVD-20260508-0083

### INFO-084
- **タイトル:** KKR $100億AIデータセンター企業設立（元AWS CEO主導）
- **ソース:** Data Center Dynamics
- **公開日:** 2026-05-08
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** KKR
- **要約:** KKRが$100億規模のAIデータセンター企業Helix Digital Infrastructureを設立。元AWS CEOがトップに。
- **キーファクト:**
  - $100億規模AI DC企業設立
  - 元AWS CEOが主導
  - データセンター・関連インフラ開発
- **引用URL:** https://www.datacenterdynamics.com/en/news/helix-digital-infrastructure-kkr-plans-10bn-ai-data-center-firm-headed-by-former-aws-ceo-report/
- **Evidence ID:** EVD-20260508-0084

### INFO-085
- **タイトル:** Llama 4 vs商用モデル: 価格23584%安いが性能ギャップ縮小
- **ソース:** 複数
- **公開日:** 2026-05-08
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-03
- **関連企業:** Meta
- **要約:** Llama 4 ScoutがClaude Opus 4と比較して23584%安いが、RAGベンチマークでGemini 3 Pro Previewが首位（89.8% MMLU-Pro）。OSS-商用ギャップは縮小傾向。
- **キーファクト:**
  - Llama 4 Scout: Claude Opus 4比23584%安価
  - 入力$0.08/M vs $15/M、出力$0.3/M vs $75/M
  - RAG首位: Gemini 3 Pro Preview（89.8% MMLU-Pro）
  - Qwen 3.6 Max preview: 256Kコンテキスト
- **引用URL:** https://pricepertoken.com/leaderboards/rag
- **Evidence ID:** EVD-20260508-0085


## X (Twitter) 投稿データ（ローカルRSSHub経由）

### INFO-086
- **タイトル:** @AnthropicAI (Anthropic) のX投稿
- **ソース:** X (Twitter) - @AnthropicAI (公式アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** We’re donating Petri, our open-source alignment tool, to @meridianlabs_ai, so its development can continue independently.

Working with Meridian Labs, we’ve also released a major update that improves the adaptability, realism, and depth of Petri’s tests.

https://www.anthropic.com/research/donating-open-source-petri
- **引用URL:** https://x.com/AnthropicAI/status/2052494460966019137

### INFO-087
- **タイトル:** @AnthropicAI (Anthropic) のX投稿
- **ソース:** X (Twitter) - @AnthropicAI (公式アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** Our security bug bounty program is now public on HackerOne. 

We've run the program privately within the security research community, and their findings have strengthened our products. Now anyone can report vulnerabilities and get rewarded. 

Read more: http://hackerone.com/anthropic
- **引用URL:** https://x.com/AnthropicAI/status/2052466175540629965

### INFO-088
- **タイトル:** @janleike (Jan Leike) のX投稿
- **ソース:** X (Twitter) - @janleike (Alignment Scienceリーダー)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** I'm really excited about this as a new tool in our interpretability tool kit

Samuel Marks: In a new paper, we present NLAs, an unsupervised method for converting an LLM's internal state into human-readable text.

I've personally been astonished by our results. I think NLAs substantively advance our ability to understand what LLMs are thinking and audit them for safety
- **引用URL:** https://x.com/janleike/status/2052445574969102612

### INFO-089
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Max Nadeau
It's not yet visible from the outside (though it will be soon), but CG has shifted gears recently and is making some very big plays. E.g. the new "short timelines" team.

If you have creative ideas for using millions of dollars to prevent AI catastrophes, you should apply.

Coefficient Giving: We're hiring grantmakers and senior generalists across our Global Catastrophic Risks teams.

Right now, our biggest constraint is people, not funding, which means every strong hire directly t...
- **引用URL:** https://x.com/sleepinyourhat/status/2052505940864507945

### INFO-090
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Kai Fronsdal
Very happy to share what I've been working on the last couple of months! Petri moving to Meridian gives it a neutral home and a dedicated maintainer. We desperately need more alignment evals, and sustained open tooling helps make this possible. Lots more to do here

Anthropic: We’re donating Petri, our open-source alignment tool, to @meridianlabs_ai, so its development can continue independently.

Working with Meridian Labs, we’ve also released a major update that improves the ad...
- **引用URL:** https://x.com/sleepinyourhat/status/2052498111478870337

### INFO-091
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** 🧫 Petri, our open-source interactive behavioral-evals tool for alignment testing, is now a freestanding project living with Meridian!

Try it out, and consider contributing!

Anthropic: We’re donating Petri, our open-source alignment tool, to @meridianlabs_ai, so its development can continue independently.

Working with Meridian Labs, we’ve also released a major update that improves the adaptability, realism, and depth of Petri’s tests.

https://www.anthropic.com/research/donating-open-source-pe...
- **引用URL:** https://x.com/sleepinyourhat/status/2052494961564893317

### INFO-092
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Meridian Labs
Petri has a new home. The automated alignment auditing tool, originally built at Anthropic, is now developed and maintained at Meridian Labs. 3.0 ships today.
- **引用URL:** https://x.com/sleepinyourhat/status/2052503523628351853

### INFO-093
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Helen Toner
One of the things that made the Mythos release hard to interpret is that Anthropic held back details on most vulns they found, to give defenders time to patch.

1 month later, info from orgs with access to Mythos is starting to trickle out, e.g. this post from Mozilla today:
- **引用URL:** https://x.com/sleepinyourhat/status/2052503610576302253

### INFO-094
- **タイトル:** @sleepinyourhat (Sam Bowman) のX投稿
- **ソース:** X (Twitter) - @sleepinyourhat (技術安全性)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Neel Nanda
Very cool work! This seems a strong new tool for hypothesis generation about weird model behaviors

Anthropic: New Anthropic research: Natural Language Autoencoders.

Models like Claude talk in words but think in numbers. The numbers—called activations—encode Claude’s thoughts, but not in a language we can read.

Here, we train Claude to translate its activations into human-readable text.
- **引用URL:** https://x.com/sleepinyourhat/status/2052498169930690726

### INFO-095
- **タイトル:** @EthanJPerez (Ethan Perez) のX投稿
- **ソース:** X (Twitter) - @EthanJPerez (Research scientist)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Anthropic
- **要約:** RT Alex Albert
With the help of Claude Mythos Preview, the Firefox team fixed more security bugs in April than in the past 15 months combined.
- **引用URL:** https://x.com/EthanJPerez/status/2052479292672782685

### INFO-096
- **タイトル:** @GoogleDeepMind (Google DeepMind) のX投稿
- **ソース:** X (Twitter) - @GoogleDeepMind (公式アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Algorithms are part of nearly every aspect of life, from the physics of the natural world to planning shipping routes.

Our Gemini-powered coding agent AlphaEvolve has been accelerating progress over the last year - from quantum and biotechnology to logistics and @Google’s AI infrastructure. ↓ https://goo.gle/4uzfe0C
- **引用URL:** https://x.com/GoogleDeepMind/status/2052403306257940967

### INFO-097
- **タイトル:** @demishassabis (Demis Hassabis) のX投稿
- **ソース:** X (Twitter) - @demishassabis (共同創業者・CEO)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** RT Google DeepMind
Algorithms are part of nearly every aspect of life, from the physics of the natural world to planning shipping routes.

Our Gemini-powered coding agent AlphaEvolve has been accelerating progress over the last year - from quantum and biotechnology to logistics and @Google’s AI infrastructure. ↓ https://goo.gle/4uzfe0C
- **引用URL:** https://x.com/demishassabis/status/2052491899110391888

### INFO-098
- **タイトル:** @pushmeet (Pushmeet Kohli) のX投稿
- **ソース:** X (Twitter) - @pushmeet (研究リーダー)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** Google/DeepMind
- **要約:** Over the last few months, our team @GoogleDeepMind  and @googlecloud has been putting  our Gemini-powered algorithm discovery agent AlphaEvolve to work across a wide variety of important applications. The results are amazing!

We're seeing major improvements in everything from chip design and genomics to logistics, electric grid optimization, and earth sciences. And this impact will only grow once it's used on more problems! 🚀 A perfect example of how AI agents will shape the world. 

Read more ...
- **引用URL:** https://x.com/pushmeet/status/2052507929153294387

### INFO-099
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Artificial Analysis
OpenAI has released GPT-Realtime-2, achieving 96.6% in our Speech Reasoning benchmark, Big Bench Audio, and #1 in our Conversational Dynamics benchmark

Released today, GPT-Realtime-2 is OpenAI's new flagship native Speech to Speech model, introducing adjustable reasoning effort levels from minimal through to xHigh. The high variant achieves a Big Bench Audio result of 96.6% equal to Gemini 3.1 Flash Live Preview - High. GPT-Realtime-2 continues to lead our Conversational ...
- **引用URL:** https://x.com/OpenAIDevs/status/2052521826774057015

### INFO-100
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT dominik kundel
One of the coolest things with Codex for Chrome is combining it with subagents so you can test things like multiplayer games! 

Available for both macOS and Windows.

Happy Codexing
- **引用URL:** https://x.com/OpenAIDevs/status/2052487869655343427

### INFO-101
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** Codex can now take on more of your browser dev work.

With the new Chrome plugin in the Codex app, it can test web apps, gather context across tabs, use web DevTools efficiently in parallel, and keep results organized without taking over your browser.
- **引用URL:** https://x.com/OpenAIDevs/status/2052481136971125158

### INFO-102
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Andrew Ambrosino
new: Codex can now drive tabs in Chrome, working in background tabs alongside you. Get the new Chrome extension today.

also: we shipped a ton of performance improvements in the app. should feel a lot better.

happy codexing!
- **引用URL:** https://x.com/OpenAIDevs/status/2052493576026911228

### INFO-103
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Scale Labs
Congrats to @OpenAI for taking the top spot on our Audio MultiChallenge S2S leaderboard with the release of GPT‑Realtime‑2 🥇

GPT-Realtime-2 more than doubles GPT-Realtime-1.5 on instruction retention, rising from 36.7% to 70.8% APR, and also stands out on voice editing, especially when users repair or revise what they are saying in real time – crucial for voice agent use cases.

Excited to see the pace of progress as voice AI accelerates.
- **引用URL:** https://x.com/OpenAIDevs/status/2052454371729031300

### INFO-104
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Vimeo
Dubbing for live events… in real time? 😮

Here’s OpenAI’s new GPT-Realtime-Translate model in action in Vimeo.

Those translations are happening completely live. No pre-loaded captions.

Live dubbing is one of the many features we’re exploring this year...

(Hopefully) more soon.

But in the meantime, we just had to show you!

Bravo @OpenAIDevs  👏
- **引用URL:** https://x.com/OpenAIDevs/status/2052446813597380936

### INFO-105
- **タイトル:** @OpenAIDevs (OpenAI Developers) のX投稿
- **ソース:** X (Twitter) - @OpenAIDevs (公式開発者アカウント)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT Glean
Taking talking shop to a whole new level.

We just shipped Glean’s real-time voice capability, powered by @OpenAI’s newest speech model GPT-Realtime-2.

Grounded in the context across your org, it feels like a real AI coworker and can keep up with how work gets finished.

In internal evals, GPT-Realtime-2 delivered a 42.9% relative increase in helpfulness over its previous version.

Give it a try. It speaks for itself.

@OpenAIDevs
- **引用URL:** https://x.com/OpenAIDevs/status/2052442307031609541

### INFO-106
- **タイトル:** @sama (Sam Altman) のX投稿
- **ソース:** X (Twitter) - @sama (CEO)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** way cooler to help software developers pokemon-evolve into superheroes than to try to replace them

it is insane what one really good person can do now
- **引用URL:** https://x.com/sama/status/2052485051812909530

### INFO-107
- **タイトル:** @sama (Sam Altman) のX投稿
- **ソース:** X (Twitter) - @sama (CEO)
- **公開日:** 2026-05-08
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** RT OpenAI
Codex now works directly in Chrome on macOS and Windows.

It’s even better at working with apps and sites in Chrome, and now works in parallel across tabs in the background without taking over your browser.

To get started, install the Chrome plugin in the Codex app.
- **引用URL:** https://x.com/sama/status/2052482715010949288

### INFO-108
- **タイトル:** @gdb (Greg Brockman) のX投稿
- **ソース:** X (Twitter) - @gdb (共同創業者)
- **公開日:** 2026-05-08
- **信頼性コード:** D-3
- **関連KIQ:** KIQ-001-01
- **関連企業:** OpenAI
- **要約:** have been excited for realtime voice-to-voice translation as an AI application since we started OpenAI. extremely cool to see it now available in the API for anyone to build with:

jason liu: 新しいリアルタイム翻訳モデルを発表できることをうれしく思います。ぜひ本日よりAPIでお試しください。
- **引用URL:** https://x.com/gdb/status/2052480998668206262

