# OpenAI

> 最終更新: 2026-02-21

**かつて「AGIを作る」と言っていた会社が、大企業向けAIプラットフォームの会社に変わった。$1000億を調達し、Frontierプラットフォームで大企業を取り込みつつ、Skills/Shell/Compactionで開発者環境も押さえようとしている。ベンチマーク性能ではGemini 3.1 Proに4pt差をつけられているが、エンタープライズ市場での先行者利益は大きい。最大の不確実性は、独自の囲い込み路線がAnthropicのMCPオープン標準に勝てるかどうか。**

## この会社は何者か

Sam Altman率いるAI企業。主力はChatGPT、GPT-5シリーズ、OpenAI Agents SDK、大企業向けのFrontierプラットフォーム。

資金調達が$1000億と巨額で、NVIDIA $300億、Amazon、SoftBank、Microsoftが参加 [INFO-102](../Information/2026-02-21/collected-raw.md#INFO-102)。Anthropicの$300億の3倍以上で、AI業界最大の調達額。

事業の勢いは強い。エンタープライズAI利用がYoY 8倍、推論モデル利用は300倍に増加 [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020)。社内では95%のエンジニアがCodexを使い、一人あたり10-20の並列エージェントを管理する体制を確立している [INFO-013](../Information/2026-02-18/collected-raw.md#INFO-013)。自分たちが売る製品を自分たちが一番使っている（dogfooding）のは、製品品質を裏付ける強い証拠。

直近の動きは3つ。(1) OpenClaw買収でPeter Steinbergerを雇い、クロスプラットフォームのワークフロー連携を強化 [INFO-015](../Information/2026-02-21/collected-raw.md#INFO-015)。(2) GPT-5.3-Codex-Sparkをリリースし、15倍の高速生成と128kコンテキストを実現 [INFO-032](../Information/2026-02-21/collected-raw.md#INFO-032)。(3) Agents SDK v0.8.4でホスト型コンテナツールとSkills bundlesを追加 [INFO-005](../Information/2026-02-21/collected-raw.md#INFO-005)。

OpenAIの方向転換を象徴する出来事がある。ChatGPTからGPT-4o、GPT-4.1シリーズ、o4-miniを廃止した [INFO-008](../Information/2026-02-18/collected-raw.md#INFO-008)。21,900件の反対署名があったが、廃止モデルの利用率はわずか0.1%。消費者の声よりエンタープライズにリソースを集中する判断を選んだ。この一件がOpenAIの変質を最もよく表している。

## 何をやろうとしているか

OpenAIの動きから、2つの戦略が同時に読み取れる。どちらも確度52%で甲乙つけがたい。

**方向1: 大企業向けAIプラットフォームになる（H-OAI-001, 確度52%）**

Frontierプラットフォームを立ち上げ、HP、Intuit、Oracle、Uberが初期顧客として採用済み [INFO-013](../Information/2026-02-21/collected-raw.md#INFO-013)。古いAssistants APIを2026年8月に廃止予定で [INFO-019](../Information/2026-02-20/collected-raw.md#INFO-019)、旧アーキテクチャを捨てて新しいResponses APIに一本化する。OpenClaw買収もワークフロー連携強化の一環で、大企業の業務に入り込むための基盤作り。

この方向が正しければ、Fortune 500との大型契約がさらに増え、SOC2/FedRAMP認証を取得していく。間違いなら、消費者向け新機能への投資再開やAPI料金の大幅引き下げが見える。

**方向2: 開発者環境を囲い込む（H-OAI-002, 確度52%）**

Skills/Shell/Compaction [INFO-038](../Information/2026-02-21/collected-raw.md#INFO-038) で開発者の実行環境を押さえようとしている。Skillsはエージェントに機能を追加するパッケージ、Shellはエージェントが動くサーバー環境、Compactionは長いやり取りを圧縮する技術。全部OpenAI独自の形式で、一度このエコシステムに入ると他社に移りにくくなる。

ただし矛盾もある。OpenClaw買収はクロスプラットフォーム志向（囲い込みの逆）であり、OpenAI自身もまだどちらに振り切るか決めきれていない可能性がある。

この囲い込み路線の最大の敵がAnthropicのMCP。MCPはオープン標準としてChrome/OWASP/Oracle/Cloudflareが対応済みで、業界標準になればOpenAI独自のSkills/Shellは「ガラパゴス」になるリスクがある。

**棄却済み: AGI優先戦略（H-OAI-003, 確度15%）**

かつてのOpenAIの看板「AGI最優先」路線は、5件の商業化証拠（Frontier Platform、Assistants API廃止、Codexスキルシステム等）により棄却された [INFO-014](../Information/2026-02-19/collected-raw.md#INFO-014)。OpenAIはもうAGIの会社ではなく、エンタープライズAIプラットフォームの会社になった。

## 強みと弱み

**強み:**
- **エンタープライズ先行者利益**: YoY 8倍成長は製品が実際に使われている証拠 [INFO-020](../Information/2026-02-18/collected-raw.md#INFO-020)
- **圧倒的な資金力**: $1000億はAnthropicの3倍以上。開発競争で息切れしない [INFO-102](../Information/2026-02-21/collected-raw.md#INFO-102)
- **Microsoftとの販路**: 企業へのセールスチャネルが確保済み
- **dogfoodingの強さ**: 社内95%がCodex使用。製品品質の裏付け [INFO-013](../Information/2026-02-18/collected-raw.md#INFO-013)
- **初期顧客の質**: HP/Intuit/Oracle/Uberの採用実績 [INFO-013](../Information/2026-02-21/collected-raw.md#INFO-013)

**弱み:**
- **ベンチマーク性能で後退中**: Gemini 3.1 ProにArtificial Analysis指数で4ptリードされている [INFO-028](../Information/2026-02-20/collected-raw.md#INFO-028)。技術力アピールが必要な営業で不利
- **Deep Researchの品質問題**: 高努力設定で精度が低下する報告 [INFO-083](../Information/2026-02-18/collected-raw.md#INFO-083)
- **消費者の不満蓄積**: GPT-4o廃止に21,900件の反対署名 [INFO-008](../Information/2026-02-18/collected-raw.md#INFO-008)
- **MCP vs Skills/Shellの標準争い**: MCPがChrome/OWASP/Oracle/Cloudflare対応済み [INFO-024](../Information/2026-02-21/collected-raw.md#INFO-024) [INFO-035](../Information/2026-02-21/collected-raw.md#INFO-035)。MCPが標準化すればOpenAI独自路線は孤立する
- **戦略の矛盾**: OpenClaw買収（開放志向）とSkills/Shell（囲い込み志向）が同居

## 何を監視すべきか

| 何を | なぜ | 今の状態 |
|------|------|---------|
| Frontier大企業契約数 | B2B仮説の成否が直接わかる | HP/Intuit/Oracle/Uber採用済み（[IND-008](../config/indicators.json), elevated） |
| Skills/Shell開発者定着度 | 囲い込み成否の鍵。定着すればMCPの対抗軸に | SDK v0.8.4リリース、CrewAI 10万人認定（[IND-015](../config/indicators.json), elevated） |
| Assistants API廃止後の動向 | 8月の強制移行で開発者が残るか離れるか | 8月廃止予定 |
| エンタープライズAI投資の持続性 | YoY 8倍が続くか。ROI達成は5%のみ | 組織平均$1.2M、前年比108%増（[IND-009](../config/indicators.json), elevated） |
