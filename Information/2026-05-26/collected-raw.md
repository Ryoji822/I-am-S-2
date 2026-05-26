# 収集データ: 2026-05-26

## メタデータ
- 収集日時: 2026-05-26 01:30 UTC
- 実行クエリ数: 78 / ~110
- scrape実行数: 7件
- 収集情報数: 50件
- Evidence ID 採番範囲: EVD-20260526-0001 〜 EVD-20260526-0050
- KIQカバレッジ: KIQ-001-01 ✓, KIQ-001-02 ✓, KIQ-001-03 ✓, KIQ-001-04 ✓, KIQ-001-05 ✓, KIQ-002-01 ✓, KIQ-002-02 ✓, KIQ-002-03 ✓, KIQ-002-04 ✓, KIQ-002-05 ✓, KIQ-002-06 ✓, KIQ-003-01 ✓, KIQ-003-02 ✓, KIQ-003-03 ✓, KIQ-003-04 ✓, KIQ-003-05 ✓, KIQ-004-01 ✓, KIQ-004-02 ✓, KIQ-004-03 ✓, KIQ-004-04 ✓, KIQ-005-01 ✓, KIQ-005-02 ✓, KIQ-005-03 ✓, BYTEDANCE-CHINESE ✓
- 動的クエリ: KIQ-AGENT-001 ✓, H-GOO-001-4R ✓, H-XAI-002-I ✓
- 品質フラグ: NORMAL

## 動的追加クエリ（Arbiterフィードバックに基づく）
- KIQ-AGENT-001: Anthropic安全性選択理由確認（A-2+品質ソース探索）
- H-GOO-001-4R: Google Cloud売上+63%のGoogle固有寄与定量分解
- H-XAI-002-I: xAI反証証拠の強制探索（累積I=0の確証バイアス対抗）

## 収集結果

### INFO-001
- **タイトル:** OpenAI model disproves 80-year-old Erdos unit distance conjecture in discrete geometry
- **ソース:** OpenAI Blog
- **公開日:** 2026-05-20
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-005-01, KIQ-005-02
- **関連企業:** OpenAI
- **要約:** An internal OpenAI model has autonomously disproved the 80-year-old Erdos unit distance conjecture in discrete geometry, providing an infinite family of examples with polynomial improvement over square grid constructions. Fields medalist Tim Gowers called it "a milestone in AI mathematics." The proof applies sophisticated tools from algebraic number theory (infinite class field towers, Golod-Shafarevich theory).
- **キーファクト:**
  - First time AI has autonomously solved a prominent open problem central to a subfield of mathematics
  - The model was a general-purpose reasoning model, not specifically trained for mathematics
  - Princeton professor Will Sawin refined the result to explicit δ=0.014
  - Noga Alon, Tim Gowers, Arul Shankar, Jacob Tsimerman verified and praised the result
- **引用URL:** https://openai.com/index/model-disproves-discrete-geometry-conjecture/
- **Evidence ID:** EVD-20260526-0001

### INFO-002
- **タイトル:** Anthropic releases 10 agent templates for financial services with Microsoft 365 integration
- **ソース:** Anthropic Blog
- **公開日:** 2026-05-05
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-02, KIQ-001-03, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropic released 10 ready-to-run agent templates for financial services (pitch building, KYC screening, month-end closing, etc.) as plugins in Claude Cowork/Code and cookbooks for Claude Managed Agents. Claude now works across Excel, PowerPoint, Word, and Outlook via add-ins. New connectors from Dun & Bradstreet, Moody's MCP app, and 7 other financial data providers. Claude Opus 4.7 leads Vals AI Finance Agent benchmark at 64.37%.
- **キーファクト:**
  - 10 agent templates for finance workflows (pitch builder, KYC screener, month-end closer, etc.)
  - Microsoft 365 integration (Excel, PowerPoint, Word, Outlook) with cross-app context
  - New connectors: Dun & Bradstreet, Fiscal AI, Financial Modeling Prep, Guidepoint, IBISWorld, SS&C Intralinks, Third Bridge, Verisk
  - Moody's launched MCP app with 600M+ company credit ratings
  - Walleye Capital: 100% of 400 employees use Claude Code
  - Claude Opus 4.7 leads Vals AI Finance Agent benchmark at 64.37%
- **引用URL:** https://www.anthropic.com/news/finance-agents
- **Evidence ID:** EVD-20260526-0002

### INFO-003
- **タイトル:** Anthropic launches Claude Design for visual collaboration
- **ソース:** Anthropic Blog
- **公開日:** 2026-04-17
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-04, KIQ-001-05
- **関連企業:** Anthropic
- **要約:** Anthropic Labs launched Claude Design, a visual collaboration tool powered by Claude Opus 4.7. Users can create designs, prototypes, slides, and one-pagers through conversation. Features include design system auto-generation, inline comments, custom sliders, organization-scoped sharing, and export to Canva/PDF/PPTX/HTML. Integration with Claude Code for design-to-code handoff.
- **キーファクト:**
  - Powered by Claude Opus 4.7 vision model
  - Auto-generates design systems from codebase and design files
  - Canva integration for seamless handoff
  - Brilliant reported 20+ prompts in other tools reduced to 2 prompts in Claude Design
  - Datadog: "What used to take a week now happens in a single conversation"
- **引用URL:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Evidence ID:** EVD-20260526-0003

### INFO-004
- **タイトル:** Google I/O 2026: Agentic Gemini era with 3.5 Flash, Gemini Omni, Antigravity 2.0, Spark
- **ソース:** Google Blog (Sundar Pichai)
- **公開日:** 2026-05-19
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-04, KIQ-001-05, KIQ-002-01, KIQ-003-01, KIQ-005-01
- **関連企業:** Google/DeepMind
- **要約:** At Google I/O 2026, Sundar Pichai declared the "agentic Gemini era." Key announcements: Gemini 3.5 Flash (frontier intelligence at 4x speed, less than half the price of comparable models), Gemini Omni (any-input any-output modal), Antigravity 2.0 (standalone desktop agent platform), Gemini Spark (24/7 personal AI agent), TPU 8t/8i dual chips, and 3.2 quadrillion tokens/month processing. OpenAI, Kakao, Eleven Labs adopting SynthID.
- **キーファクト:**
  - Gemini 3.5 Flash: better than 3.1 Pro across almost all benchmarks, 4x faster output than other frontier models
  - 3.2 quadrillion tokens/month (7x Y/Y growth), 8.5M developers, 19B tokens/minute via API
  - Gemini app surpassed 900M MAU (2x in a year), AI Overviews 2.5B MAU, AI Mode 1B MAU
  - Antigravity 2.0: standalone desktop app for agent orchestration, 12x faster Flash variant
  - Gemini Spark: 24/7 personal AI agent running on dedicated VMs, MCP integration coming
  - TPU 8t (3x training power) and 8i (inference-optimized), 2x better performance-per-watt
  - Capex: $180-190B in 2026 (~6x from 2022's $31B)
  - Google Pics, Ask YouTube, Voice-powered Docs Live, intelligent eyewear
  - 375+ Cloud customers each processing >1 trillion tokens/year
- **引用URL:** https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
- **Evidence ID:** EVD-20260526-0004

### INFO-005
- **タイトル:** xAI launches Grok Build CLI coding agent
- **ソース:** xAI Blog
- **公開日:** 2026-05-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05, KIQ-004-02
- **関連企業:** xAI
- **要約:** xAI launched Grok Build, a coding agent and CLI for professional software engineering, now in early beta for SuperGrok and X Premium Plus subscribers. Features include plan mode with approval workflow, MCP server/plugin/skills compatibility, parallel subagents with worktree integration, and headless mode for automation.
- **キーファクト:**
  - Early beta for SuperGrok and X Premium Plus subscribers
  - Plan mode: approve/modify plan before execution, clean diff view
  - Compatible with AGENTS.md, plugins, hooks, skills, MCP servers
  - Parallel subagents with worktree integration
  - Headless mode (-p) for scripting, ACP support for orchestration
- **引用URL:** https://x.ai/news/grok-build-cli
- **Evidence ID:** EVD-20260526-0005

### INFO-006
- **タイトル:** Reuters Exclusive: Grok falls flat in Washington, minimal government adoption
- **ソース:** Reuters
- **公開日:** 2026-05-21
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-001-02, KIQ-002-06, KIQ-003-04
- **関連企業:** xAI
- **要約:** Reuters investigation reveals Grok has seen minimal adoption in the U.S. government despite being available for 8 months at near-zero pricing. Of 400+ identified AI use cases in federal agencies, only 3 involved xAI/Grok vs. 234 for OpenAI, 33 for Google, 26 for Anthropic. Corporate usage also weak: Netskope data shows Grok at 2/1000 enterprise users (down from peak of 5/1000). SpaceX's $1.75T IPO valuation partly depends on AI market success.
- **キーファクト:**
  - 3 out of 400+ federal AI use cases used Grok vs. 234 OpenAI, 33 Google, 26 Anthropic
  - DARPA staff prefer Claude for coding/writing, Gemini for engineering analysis; Grok "just not the best model"
  - Grok enterprise usage: 2/1000 users, down from peak 5/1000 (Netskope data)
  - xAI lost VA bid; Grok "hadn't met requirements"
  - Pentagon $200M deal with xAI, but staff prefer competitors' tools
  - SpaceX IPO valuation: $1.75T, with $26.5T total AI market opportunity claim
- **引用URL:** https://www.reuters.com/world/grok-falls-flat-washington-undercutting-spacexs-ai-growth-story-2026-05-21/
- **Evidence ID:** EVD-20260526-0006

### INFO-007
- **タイトル:** Anthropic Agent SDK June 15 pricing change includes monthly credits for paid plans
- **ソース:** Reddit / YouTube
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Starting June 15, paid Claude plans will include a monthly credit for programmatic usage covering Claude Agent SDK, claude -p, Claude Code GitHub Actions. This reframes personal Claude subscriptions as agent deployment platforms.
- **キーファクト:**
  - June 15 pricing change adds monthly credits for Agent SDK/Code usage on paid plans
  - Signals Anthropic's push toward always-on agent usage from consumer subscriptions
  - Reddit discussion: clear signal for how always-on Claude agents will be used
- **引用URL:** https://www.reddit.com/r/ClaudeCode/comments/1tjsme2/anthropics_june_15th_agent_sdk_pricing_reframes/
- **Evidence ID:** EVD-20260526-0007

### INFO-008
- **タイトル:** OpenAI Agents JS adds Sandbox Agents for persistent workspaces
- **ソース:** GitHub
- **公開日:** 2026-05-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI Agents JS SDK release adds Sandbox Agents, a beta SDK surface for running agents with persistent workspaces and sandbox-backed capabilities in JavaScript.
- **キーファクト:**
  - Sandbox Agents beta: persistent workspaces for JS agents
  - Sandbox-backed capabilities for safe execution
- **引用URL:** https://github.com/openai/openai-agents-js/releases
- **Evidence ID:** EVD-20260526-0008

### INFO-009
- **タイトル:** Agent Skills (SKILL.md) ecosystem explodes to 40,000+ across 18+ agents
- **ソース:** Firecrawl Blog / GitHub
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-03, KIQ-001-05
- **関連企業:** 複数
- **要約:** Agent Skills (SKILL.md format) have grown from 0 to 40,000 in ~20 weeks. Compatible with 18+ AI agents including Claude Code, GitHub Copilot, Cursor, Cline. Supabase, Railway, and others publish official skills. Format is becoming a de facto open standard for extending AI coding assistants.
- **キーファクト:**
  - 40,000+ SKILL.md files created in ~20 weeks
  - Compatible with Claude Code, GitHub Copilot, Cursor, Cline, and 14+ others
  - Supabase, Railway publish official agent skills
  - Open format becoming de facto standard for agent knowledge sharing
- **引用URL:** https://www.firecrawl.dev/blog/agent-skills
- **Evidence ID:** EVD-20260526-0009

### INFO-010
- **タイトル:** OpenAI and Dell announce Codex partnership for hybrid/on-premises enterprise AI agents
- **ソース:** Pulse2
- **公開日:** 2026-05-18
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** OpenAI, Dell
- **要約:** OpenAI and Dell Technologies announced a Codex partnership to bring AI agents to hybrid and on-premises enterprise environments, addressing enterprises that require data to stay on-premises.
- **キーファクト:**
  - Codex agents available in hybrid/on-premises environments via Dell
  - Targets enterprises with data residency requirements
- **引用URL:** https://pulse2.com/openai-and-dell-technologies-announce-codex-partnership-to-bring-ai-agents-to-hybrid-and-on-premises-enterprise-environments/
- **Evidence ID:** EVD-20260526-0010

### INFO-011
- **タイトル:** Red Hat AI and OpenShell: security-enhanced agent execution for enterprise
- **ソース:** Red Hat Blog
- **公開日:** 2026-05-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-02, KIQ-001-05
- **関連企業:** Red Hat (IBM)
- **要約:** Red Hat introduced OpenShell, providing sandboxed execution environments for AI agents. Agent-generated tool calls execute inside isolated sandbox runtimes controlled by the customer, addressing enterprise security requirements for agent deployment.
- **キーファクト:**
  - Agent tool calls execute in isolated sandbox runtimes
  - Customer-controlled execution environments
  - Self-hosted environment worker demo available
- **引用URL:** https://www.redhat.com/en/blog/red-hat-ai-and-openshell-driving-security-enhanced-agent-execution-for-enterprise-ai
- **Evidence ID:** EVD-20260526-0011

### INFO-012
- **タイトル:** Enterprise AI agent adoption: 79% adopted but only 11% in production (68-point gap)
- **ソース:** LinkedIn / Digital Applied / Gartner
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-02, KIQ-002-04
- **関連企業:** 複数
- **要約:** Multiple surveys show a massive gap between AI agent adoption and production deployment. 79% of enterprises have adopted AI agents but only 11% run them in production (68-point gap). Gartner CIO survey puts deployed-agent adoption at 17%. 51% of enterprises now run AI agents in production per one estimate, conflicting with lower figures.
- **キーファクト:**
  - 79% adoption vs 11% production = 68-point gap
  - Gartner CIO survey: only 17% have deployed agents
  - 65-85% of organizations expect to adopt gen AI/agentic AI in pricing (McKinsey)
  - Conflicting data points suggest measurement methodology varies widely
- **引用URL:** https://www.digitalapplied.com/blog/state-of-ai-agents-2026-200-data-points
- **Evidence ID:** EVD-20260526-0012

### INFO-013
- **タイトル:** 88% of enterprises with AI agents report security incidents
- **ソース:** Digital Applied
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-03
- **関連企業:** 複数
- **要約:** Agentic AI statistics compilation reports 88% of enterprises with deployed agents have experienced at least one security incident. 1 in 8 corporate data breaches now linked to AI agent activity. 34% of organizations lack formal AI agent governance policies.
- **キーファクト:**
  - 88% enterprises with agents report security incidents
  - 1 in 8 data breaches linked to AI agent activity
  - 34% lack formal AI agent governance policies
- **引用URL:** https://www.digitalapplied.com/blog/agentic-ai-statistics-2026-definitive-collection-150-data-points
- **Evidence ID:** EVD-20260526-0013

### INFO-014
- **タイトル:** SAP attempts to become gatekeeper of enterprise AI via API policy change
- **ソース:** Forrester
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-03, KIQ-002-05
- **関連企業:** SAP
- **要約:** SAP's API policy shifts from "paper rule" to "operational constraint" on June 9, attempting to become the gatekeeper of enterprise AI. Forrester recommends CIOs push back against this move which could restrict third-party AI agent access to SAP systems.
- **キーファクト:**
  - SAP API policy change June 9: paper rule → operational constraint
  - Forrester positions this as SAP attempting to control enterprise AI access
  - Recommendation: CIOs should push back
- **引用URL:** https://www.forrester.com/blogs/sap-is-attempting-to-become-the-gatekeeper-of-enterprise-ai-cios-should-push-back/
- **Evidence ID:** EVD-20260526-0014

### INFO-015
- **タイトル:** OpenAI Daybreak combines GPT-5.5 with Codex Security for agentic AppSec workflow
- **ソース:** Futurum
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-01, KIQ-001-05
- **関連企業:** OpenAI
- **要約:** OpenAI Daybreak combines GPT-5.5 models with Codex Security to embed application security into development workflow, positioning OpenAI for the AI-native application security market.
- **キーファクト:**
  - GPT-5.5 + Codex Security integration for automated AppSec
  - AI-native application security positioning
- **引用URL:** https://futurumgroup.com/insights/openai-daybreak-aims-for-the-agentic-appsec-workflow/
- **Evidence ID:** EVD-20260526-0015

### INFO-016
- **タイトル:** Netskope integrates with Claude Compliance API for enterprise LLM monitoring
- **ソース:** Yahoo Finance / Netskope
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-001-02
- **関連企業:** Anthropic, Netskope
- **要約:** Netskope announced integration with Claude's Compliance API to provide visibility and advanced security controls for enterprise Claude usage, supporting regulatory compliance. Fortinet also announced integration with Claude Compliance API for monitoring enterprise LLM usage.
- **キーファクト:**
  - Netskope + Claude Compliance API integration
  - Fortinet also integrated with Claude Compliance API
  - Enables monitoring of prompts and files for sensitive data
- **引用URL:** https://finance.yahoo.com/sectors/technology/articles/netskope-announces-integration-claude-compliance-164500875.html
- **Evidence ID:** EVD-20260526-0016

### INFO-017
- **タイトル:** Kore.ai Artemis: governance-first multi-agent AI platform on Azure
- **ソース:** HPC Wire / Kore.ai
- **公開日:** 2026-05-21
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-001-02, KIQ-002-01
- **関連企業:** Kore.ai, Microsoft
- **要約:** Kore.ai launched Artemis agent platform on Microsoft Azure with SOC 2 Type II, ISO 27001, PCI DSS, and FedRAMP Moderate certifications. Positions as governance-first multi-agent platform for enterprise.
- **キーファクト:**
  - SOC 2 Type II, ISO 27001, PCI DSS, FedRAMP Moderate certified
  - Launched on Azure first
  - Governance-first multi-agent platform positioning
- **引用URL:** https://www.hpcwire.com/aiwire/2026/05/21/kore-ai-unveils-artemis-to-build-govern-and-optimize-enterprise-ai-agents/
- **Evidence ID:** EVD-20260526-0017

### INFO-018
- **タイトル:** MCP specification release candidate: stateless protocol core and Extensions framework
- **ソース:** MCP Blog
- **公開日:** 2026-05-25
- **信頼性コード:** A-3
- **関連KIQ:** KIQ-001-03
- **関連企業:** 複数 (Anthropic, OpenAI, Google, Microsoft)
- **要約:** The 2026-07-28 MCP Specification Release Candidate introduces a stateless protocol core, Extensions framework, and Tasks system. Every major AI company (Anthropic, OpenAI, Google, Microsoft) has adopted MCP. The ecosystem now spans 15,930+ indexed servers with an MCP-25 index tracking top servers.
- **キーファクト:**
  - 2026-07-28 RC: stateless protocol core, Extensions, Tasks
  - 15,930+ indexed MCP servers
  - All major AI companies adopted MCP
  - MCP-25 index tracks top servers on adoption/quality/momentum
- **引用URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- **Evidence ID:** EVD-20260526-0018

### INFO-019
- **タイトル:** Trump postpones AI executive order citing overregulation concerns
- **ソース:** WSJ / CNN / AP
- **公開日:** 2026-05-20
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数 (OpenAI, Anthropic, Google, xAI)
- **要約:** President Trump postponed an executive order for AI oversight, stating it could slow the U.S. in the AI race. The order would have required AI companies to share advanced models with the government before public release. A proposed 10-year moratorium aims to prevent states from enacting AI regulations.
- **キーファクト:**
  - Executive order postponed hours before expected White House ceremony
  - Order would have required voluntary sharing of advanced models before release
  - 10-year moratorium proposed to prevent state-level AI regulation
  - Driven by fears of falling behind China in AI development
- **引用URL:** https://www.cnn.com/2026/05/20/tech/ai-executive-order-trump-white-house
- **Evidence ID:** EVD-20260526-0019

### INFO-020
- **タイトル:** China State Council accelerates AI legislation in May 2026
- **ソース:** AI Tech Trend
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** ByteDance, DeepSeek
- **要約:** In May 2026, China's State Council revealed intentions to accelerate legislation aimed at ensuring the sound development of artificial intelligence.
- **キーファクト:**
  - China State Council accelerating AI legislation
  - Focus on ensuring sound AI development
- **引用URL:** https://aitechtrend.com/china-artificial-intelligence-regulations/
- **Evidence ID:** EVD-20260526-0020

### INFO-021
- **タイトル:** Appeals court divided over Pentagon's Anthropic supply-chain-risk designation
- **ソース:** Bloomberg / CNBC / Reuters
- **公開日:** 2026-05-19
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** A federal appeals court appeared skeptical of Anthropic's bid to block the Pentagon from declaring the company a supply-chain risk to US national security. Anthropic filed lawsuits in DC and San Francisco after being designated a supply chain risk for refusing to allow Claude to be used for autonomous weapons or mass surveillance. Pentagon also attempted to use Defense Production Act to force Anthropic to tailor its AI for military use.
- **キーファクト:**
  - Appeals court divided on Anthropic's supply-chain-risk designation
  - Pentagon designated Anthropic SCR for refusing autonomous weapons/mass surveillance use
  - Defense Production Act invoked to force Anthropic to tailor AI for Pentagon
  - Anthropic filed lawsuits in DC and San Francisco
  - Senators: "DPA used not for ventilators but to force a company to make AI less safe"
- **引用URL:** https://www.bloomberg.com/news/articles/2026-05-19/appeals-court-skeptical-anthropic-can-block-us-supply-risk-label
- **Evidence ID:** EVD-20260526-0021

### INFO-022
- **タイトル:** Anthropic gets Silicon Valley backing against Pentagon AI weaponization pressure
- **ソース:** MetodoViral / Reuters
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-06
- **関連企業:** Anthropic
- **要約:** Anthropic received broad support from Silicon Valley figures against Pentagon pressure to weaponize AI. Chris Olah stated AI must be guided from outside Big Tech. The chilling effect of government retaliation is "often worse than the direct action itself." Anthropic says other companies are willing to collaborate with Pentagon, signaling competitive dynamics.
- **キーファクト:**
  - Silicon Valley mobilization behind Anthropic's safety stance
  - Chris Olah: "AI must be guided from outside Big Tech"
  - Chilling effect: "often worse than the direct action itself"
  - Other companies willing to fill Anthropic's Pentagon role (competitive displacement)
- **引用URL:** https://metodoviral.com/en/news/anthropic-gets-backing-against-pentagon-military-use-of-ai/
- **Evidence ID:** EVD-20260526-0022

### INFO-023
- **タイトル:** American and Allied cyber agencies issue first joint guidance on securing agentic AI
- **ソース:** Crowell
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-03
- **関連企業:** 複数
- **要約:** American and allied cyber agencies issued the first joint guidance on securing agentic AI. The regulatory environment for agentic AI is accelerating globally, including U.S. government procurement requirements and NIST standards.
- **キーファクト:**
  - First joint international guidance on agentic AI security
  - Covers U.S. government procurement requirements
  - NIST standards development for agentic AI
- **引用URL:** https://www.crowell.com/en/insights/client-alerts/american-and-allied-cyber-agencies-issue-first-joint-guidance-on-securing-agentic-ai
- **Evidence ID:** EVD-20260526-0023

### INFO-024
- **タイトル:** Pope Leo XIV issues AI-focused encyclical "Magnifica humanitas" calling for robust regulation
- **ソース:** Reuters / PBS
- **公開日:** 2026-05-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-005-03
- **関連企業:** 複数
- **要約:** Pope Leo XIV issued his first encyclical "Magnifica humanitas" focused on AI, calling for robust regulation of AI. Chris Olah (Anthropic co-founder) gave remarks on the encyclical. The document calls for governments to slow down and closely regulate AI development, warning that autonomous systems could "massively amplify" AI's impact.
- **キーファクト:**
  - First papal encyclical focused on AI
  - Chris Olah (Anthropic co-founder) gave remarks on the encyclical
  - Calls for robust regulation and safety regimes
  - Warning about autonomous systems amplifying AI impact
- **引用URL:** https://www.pbs.org/newshour/amp/world/pope-calls-for-robust-regulation-of-ai-in-manifesto-that-ponders-the-future-of-humanity
- **Evidence ID:** EVD-20260526-0024

### INFO-025
- **タイトル:** WSJ: Anthropic expects 130% revenue surge to $10.9B in Q2, first operating profit
- **ソース:** Wall Street Journal
- **公開日:** 2026-05-25
- **信頼性コード:** A-2
- **関連KIQ:** KIQ-003-04
- **関連企業:** Anthropic
- **要約:** Anthropic expects a 130% revenue surge to $10.9 billion in the June quarter and its first operating profit, defying skeptics of the AI boom. Google has invested roughly $300M+ in Anthropic. Anthropic has also been investing in services companies alongside OpenAI.
- **キーファクト:**
  - 130% revenue surge expected to $10.9B in June quarter
  - First operating profit expected
  - Google invested ~$300M+ in Anthropic (10% stake)
  - Both Anthropic and OpenAI investing in services companies
- **引用URL:** https://www.wsj.com/tech/ai/mind-blowing-growth-is-about-to-propel-anthropic-into-its-first-profitable-quarter-7edbf2f4
- **Evidence ID:** EVD-20260526-0025

### INFO-026
- **タイトル:** DeepSeek V4 Pro 75% price cut tops global value ranking, escalates AI pricing war
- **ソース:** SCMP / InfoWorld
- **公開日:** 2026-05-25
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-003-01, KIQ-003-03
- **関連企業:** DeepSeek
- **要約:** DeepSeek V4 Pro tops global bang-for-buck ranking after a 75% permanent price cut, according to Artificial Analysis. The cut highlights falling inference costs and challenges premium pricing from OpenAI, Anthropic, and Google. DeepSeek-V4 uses Muon optimizer with Kimi's recipe to scale for LLM training.
- **キーファクト:**
  - 75% permanent price cut for V4 Pro
  - Tops Artificial Analysis value ranking
  - Challenges premium pricing from OpenAI/Anthropic/Google
  - DeepSeek-V3.2 (Thinking) outperforms Grok 4 Fast in majority of benchmarks
- **引用URL:** https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html
- **Evidence ID:** EVD-20260526-0026

### INFO-027
- **タイトル:** AI API token pricing crash: $30/MTok (2023) to $1-5/MTok (2026), 10-100x reduction
- **ソース:** LLM Stats / Investing.com
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** 複数
- **要約:** GPT-4-level performance cost $30/M tokens in 2023. Today comparable models cost $1-5/M tokens. Competition and better infrastructure driving 10-100x price reductions. However, frontier model pricing remains $5-15/M tokens with room to increase. Claude Code costs average $6/developer/day.
- **キーファクト:**
  - GPT-4-level cost: $30/MTok (2023) → $1-5/MTok (2026)
  - 10-100x reduction in 3 years
  - Frontier model pricing: $5-15/MTok
  - Claude Code: $6/developer/day average
  - Analysts note labs could 2-3x rates as users become addicted
- **引用URL:** https://llm-stats.com/ai-trends
- **Evidence ID:** EVD-20260526-0027

### INFO-028
- **タイトル:** Google slashes AI model prices at I/O 2026, launches price war against OpenAI and Anthropic
- **ソース:** TradingKey
- **公開日:** 2026-05-19
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Google/DeepMind
- **要約:** At I/O 2026, Google launched a price war in the AI model race. Gemini 3.5 Flash delivers frontier-level capabilities at less than half the price of comparable frontier models. Shifting 80% workloads from other frontier models to 3.5 Flash could save top companies over $1B annually. Gemini 3.1 Pro Preview drops to $1.00/$6.00 per M tokens.
- **キーファクト:**
  - Gemini 3.5 Flash: frontier intelligence at <50% of competitor pricing
  - 80% workload shift to Flash = $1B+ annual savings for top companies
  - Gemini 3.1 Pro Preview: $1.00/$6.00 per M tokens (vs $2/$12 standard)
  - Google consumer plans: Free $0, Plus $7.99, Pro $19.99, Ultra $99.99
- **引用URL:** https://www.tradingkey.com/analysis/stocks/us-stocks/261914133-google-gemini-ai-pricing-subscription-openai-claude-anthropic-market-share-token-cost-tradingkey
- **Evidence ID:** EVD-20260526-0028

### INFO-029
- **タイトル:** LLM benchmark leaderboard: Gemini 3.1 Pro leads HLE at 44.7%, Claude Opus 4 leads ARC-Easy at 99.7%
- **ソース:** PricePerToken / Codesota
- **公開日:** 2026-05-24
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** 複数
- **要約:** LLM benchmark leaderboard as of May 24, 2026: Humanity's Last Exam (HLE) led by Gemini 3.1 Pro Preview at 44.7%, then GPT-5.4 at 41.6%, Gemini 3.5 Flash at 41.0%. ARC Easy led by Claude Opus 4 at 99.7%. 221 AI benchmarks now tracked. OpenAI's Erdos proof represents expanding "AGI time" from hours to multi-page logical arguments.
- **キーファクト:**
  - HLE leaderboard: Gemini 3.1 Pro Preview 44.7%, GPT-5.4 41.6%, Gemini 3.5 Flash 41.0%
  - ARC Easy: Claude Opus 4 at 99.7%
  - 221 AI benchmarks tracked across knowledge, coding, math, reasoning, agentic
  - Claude Opus 4.7 (Adaptive) stronger benchmark profile than Grok 4.20
- **引用URL:** https://pricepertoken.com/leaderboards/benchmark/hle
- **Evidence ID:** EVD-20260526-0029

### INFO-030
- **タイトル:** ARC-AGI-3 launched March 2026: frontier models score below 1%
- **ソース:** ProGigAI / LinkedIn
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02, KIQ-005-01
- **関連企業:** 複数
- **要約:** ARC-AGI-3 launched in March 2026 with further increased difficulty. Early reports indicate frontier models score below 1% on the new benchmark, while humans solve ~100% of ARC-AGI-3 tasks. This highlights a massive gap between human and AI performance on novel reasoning tasks.
- **キーファクト:**
  - ARC-AGI-3 launched March 2026
  - Frontier models score below 1%
  - Humans solve ~100% of ARC-AGI-3 tasks
  - Massive human-AI gap on novel reasoning tasks
- **引用URL:** https://progigai.com/arc-agi-2-the-toughest-ai-benchmark-ever-explained/
- **Evidence ID:** EVD-20260526-0030

### INFO-031
- **タイトル:** AI vendor lock-in: switching costs vary 100x depending on architecture
- **ソース:** Phos AI Labs
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05
- **関連企業:** 複数
- **要約:** AI platform switching costs vary by 100x depending on how systems are built. Plain-text foundations cost near zero to migrate; custom API integrations cost $50,000-$200,000 or more. Organizations that build on proprietary APIs face significantly higher vendor lock-in.
- **キーファクト:**
  - Switching costs vary 100x depending on architecture
  - Plain-text foundations: near-zero migration cost
  - Custom API integrations: $50K-$200K+ to migrate
  - Proprietary APIs create significantly higher lock-in
- **引用URL:** https://phosailabs.com/blog/vendor-lock-in-risk-with-one-ai-platform
- **Evidence ID:** EVD-20260526-0031

### INFO-032
- **タイトル:** AGI timeline predictions: Hassabis says 2030, Altman says during Trump term
- **ソース:** Multiple sources
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Google/DeepMind, OpenAI
- **要約:** Demis Hassabis at Google I/O: "AGI is just a few years away" with timeline locked for ~2030. DeepMind has tracked this 20-year goal since 2010. Sam Altman predicted AGI by 2025-2028 during Trump's term. Google DeepMind research paper warns AGI could emerge as early as 2030 with risks of "permanently" damaging human civilization.
- **キーファクト:**
  - Hassabis: AGI timeline locked ~2030, "just a few years away"
  - DeepMind 20-year goal tracked since 2010
  - Altman: AGI by 2025-2028 during Trump's term
  - DeepMind paper: AGI by 2030 could carry risks of permanent damage
  - Hassabis timeline "shrinking and shrinking" per observers
- **引用URL:** https://sherwood.news/tech/gi-artificial-general-intelligence-when-predictions/
- **Evidence ID:** EVD-20260526-0032

### INFO-033
- **タイトル:** Klarna workforce cut 22%, Duolingo cut 10%; AI layoffs no longer boosting stock prices
- **ソース:** LinkedIn / Medium / Tech.co
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-04, KIQ-004-01
- **関連企業:** Klarna, Duolingo
- **要約:** Klarna cut workforce by 22% (dropping from ~5,000 to ~3,900). Duolingo cut 10% of contractors. However, new CNBC data shows AI layoff announcements no longer boost stock prices as they did initially. Amazon announced plans to cut 14,000 corporate jobs. Klarna CEO says AI is reshaping the company and replacing human workers.
- **キーファクト:**
  - Klarna: 22% workforce reduction, CEO says AI reshaping the company
  - Duolingo: 10% contractor cut
  - Amazon: 14,000 corporate job cuts planned
  - CNBC data: AI layoff announcements no longer boost stock prices
  - Narrative shift from "AI replacing workers = efficiency" to skepticism
- **引用URL:** https://tech.co/news/companies-replace-workers-with-ai
- **Evidence ID:** EVD-20260526-0033

### INFO-034
- **タイトル:** Google rolls out AI-powered ad formats at Marketing Live amid disintermediation concerns
- **ソース:** ProactiveInvestors
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-05
- **関連企業:** Google
- **要約:** Google rolled out AI-powered ad formats at Marketing Live, working to address investor concerns about AI disintermediation risk as ChatGPT counts ~900 million users. Salesforce projecting $300M spend on Anthropic tokens this year.
- **キーファクト:**
  - Google AI-powered ad formats to counter disintermediation risk
  - ChatGPT: ~900M users creating competitive pressure
  - Salesforce: $300M projected annual spend on Anthropic tokens
  - AI search is an economics and disintermediation problem for platforms
- **引用URL:** https://www.proactiveinvestors.com/companies/news/1092827/google-rolls-out-ai-powered-ad-formats-at-marketing-live-1092827.html
- **Evidence ID:** EVD-20260526-0034

### INFO-035
- **タイトル:** Anthropic pricing changes: Claude Code removed from Pro, metered pricing June 15
- **ソース:** LinkedIn / Reddit
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-01
- **関連企業:** Anthropic
- **要約:** Anthropic quietly removed Claude Code from its $20/month Pro plan and is moving to metered pricing on June 15. Pro, Max, and Enterprise users got 2x the Claude Code time on May 4. Claude API pricing starts at $1/M input tokens (Haiku 4.5) and tops out at $25/M output tokens (Opus 4.6/4.7).
- **キーファクト:**
  - Claude Code removed from $20/month Pro plan
  - June 15: metered pricing for agent SDK/Code usage
  - May 4: 2x Claude Code time for Pro/Max/Enterprise
  - API: $1/M input (Haiku 4.5) to $25/M output (Opus 4.6/4.7)
- **引用URL:** https://www.reddit.com/r/ClaudeAI/comments/1tj2exx/claude_p_is_moving_to_metered_pricing_on_june_15/
- **Evidence ID:** EVD-20260526-0035

### INFO-036
- **タイトル:** ByteDance Doubao reaches 345M+ MAU, 580M+ MAU in some counts, 120 trillion tokens/day
- **ソース:** 凤凰网 / CSDN / ifeng
- **公開日:** 2026-05-19
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE
- **関連企業:** ByteDance
- **要約:** Doubao (豆包) reached 345M MAU as of March 2026 (QuestMobile), with some sources claiming 580M+ MAU. Daily active users exceeded 16M in late 2024. Doubao processes 120 trillion tokens daily, with text inference costs reaching tens of millions of yuan per day. Doubao has started monetizing with paid membership tiers.
- **キーファクト:**
  - 345M MAU as of March 2026 (QuestMobile), possibly 580M+ per other sources
  - 16M+ DAU in late 2024, reaching industry #1 in China
  - 120 trillion tokens/day processing
  - Text inference cost: tens of millions yuan/day
  - Transitioning from free to paid membership model
- **引用URL:** https://finance.china.com/TMT/13004688/20260519/49501537.html
- **Evidence ID:** EVD-20260526-0036

### INFO-037
- **タイトル:** ByteDance Seed 2.0 Lite released at $0.25/$2.00 per MTok; Seedance 2.0 video model available
- **ソース:** PricePerToken / BytePlus / Reddit
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-01
- **関連企業:** ByteDance
- **要約:** ByteDance Seed 2.0 Lite was released March 10, 2026, priced at $0.25/$2.00 per million tokens. Doubao Seed 2 Pro has 256K context window and 128K output tokens. Seedance 2.0 video model offers Director mode with multimodal upgrades. ByteDance also open-sourced a 3B image model.
- **キーファクト:**
  - Seed 2.0 Lite: $0.25/$2.00 per MTok, released March 10, 2026
  - Doubao Seed 2 Pro: 256K context, 128K output
  - Seedance 2.0: Director mode, character consistency, audio sync
  - ByteDance open-sourced 3B image model
- **引用URL:** https://pricepertoken.com/pricing-page/model/bytedance-seed-seed-2.0-lite
- **Evidence ID:** EVD-20260526-0037

### INFO-038
- **タイトル:** ByteDance invested $12B+ in AI infrastructure in 2025 (3x YoY), Seed team lost 70+ to startups
- **ソース:** 知乎 / 微博
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** BYTEDANCE-CHINESE, KIQ-003-04
- **関連企業:** ByteDance
- **要約:** ByteDance invested over $12B (~860B RMB) in AI infrastructure in 2025 (3x 2024), primarily for GPU procurement, data center construction, and model training/inference. 30+ "ByteDance alumni" AI startups have completed funding rounds. The Seed team lost nearly 70 people in the past year to startups covering agents, multimodal creation, and other areas.
- **キーファクト:**
  - $12B+ AI infrastructure investment in 2025 (~3x YoY)
  - GPU procurement, data centers, model training/inference
  - 30+ ByteDance-alumni AI startups funded
  - Seed team lost ~70 people to startups in past year
  - Competition forming between ByteDance and alumni startups
- **引用URL:** https://zhuanlan.zhihu.com/p/2040671639310948082
- **Evidence ID:** EVD-20260526-0038

### INFO-039
- **タイトル:** Google Cloud Q1 2026: $20B revenue (+63% YoY), operating margin 17.8%→32.9%
- **ソース:** TIKR / Intellectia / Trefis
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-002-01, H-GOO-001-4R
- **関連企業:** Google/DeepMind
- **要約:** Google Cloud Q1 2026 revenue hit $20.03B, growing 63% YoY. Operating margin inflected from 17.8% to 32.9%. Anthropic committing ~$200B over 5 years on Google Cloud. Customer backlog reached $462B. Google and Blackstone quietly launching a $5B AI cloud company. Google Cloud now has 375+ customers each processing >1 trillion tokens/year.
- **キーファクト:**
  - Q1 2026: $20.03B revenue (+63% YoY)
  - Operating margin: 17.8% → 32.9% YoY improvement
  - Anthropic: ~$200B commitment over 5 years on Google Cloud
  - Customer backlog: $462B
  - Google + Blackstone: $5B AI cloud joint venture
  - 375+ customers each processing >1 trillion tokens/year
- **引用URL:** https://www.trefis.com/data/companies/GOOGL?source=forbes&from=MSFT-2026-05-17
- **Evidence ID:** EVD-20260526-0039

### INFO-040
- **タイトル:** xAI Grok downloads fell 60% from 20M (Jan) to 8.3M (Apr 2026); struggling in enterprise
- **ソース:** Reuters / Instagram
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-003-04, H-XAI-002-I
- **関連企業:** xAI
- **要約:** Grok chatbot downloads fell nearly 60% from over 20M in January to about 8.3M in April 2026. Paid adoption hovering at low levels. xAI "seems to be struggling across the enterprise space more broadly" (Reuters). This contradicts the $1.75T SpaceX IPO valuation narrative.
- **キーファクト:**
  - Downloads: 20M (Jan) → 8.3M (Apr 2026), -60%
  - Enterprise adoption minimal
  - Paid adoption at low levels
  - Contradicts $1.75T SpaceX IPO valuation
- **引用URL:** https://www.reuters.com/world/grok-falls-flat-washington-undercutting-spacexs-ai-growth-story-2026-05-21/
- **Evidence ID:** EVD-20260526-0040

### INFO-041
- **タイトル:** Yann LeCun: AI industry "completely LLM-pilled", argues wrong direction on AGI
- **ソース:** Instagram / Facebook / Daedalus
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Meta
- **要約:** Yann LeCun argues the AI industry is "completely LLM-pilled" and that LLMs are not the path to AGI. Hassabis responded that LeCun is "confusing general intelligence with universal intelligence." LeCun, Bengio, and Hinton (2018 Turing Award co-winners) have diverging views on AGI timeline and approach.
- **キーファクト:**
  - LeCun: AI industry "completely LLM-pilled"
  - Hassabis: LeCun "confusing general intelligence with universal intelligence"
  - Three Turing Award winners have diverging AGI views
  - LeCun advocates non-LLM approaches to AGI
- **引用URL:** https://www.amacad.org/publication/daedalus/learning-abstractions-conversation-yann-lecun
- **Evidence ID:** EVD-20260526-0041

### INFO-042
- **タイトル:** Dario Amodei: "powerful AI" could arrive by late 2026 or early 2027
- **ソース:** Reddit / AIMultiple
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-005-02
- **関連企業:** Anthropic
- **要約:** Dario Amodei has argued that "powerful AI" could arrive by late 2026 or early 2027. Microsoft AI CEO said he would stop building superintelligence the moment it posed a threat to people. AI experts estimate AGI will probably emerge between 2040-2050 (over 50% chance) and is highly likely by 2075 (90% chance). Some predict superintelligence by late 2027.
- **キーファクト:**
  - Amodei: "powerful AI" by late 2026 or early 2027
  - Microsoft AI CEO: would stop building superintelligence if it threatened people
  - Expert survey: AGI probably 2040-2050, highly likely by 2075
  - Some predict self-improving superintelligence by late 2027
- **引用URL:** https://www.reddit.com/r/ArtificialInteligence/comments/1tkc5u7/the_strongest_predictor_of_someones_agi_timeline/
- **Evidence ID:** EVD-20260526-0042

### INFO-043
- **タイトル:** "Coding skill commoditization": bottleneck shifts from coding to design/architecture
- **ソース:** Reddit / LinkedIn (AI DevCon)
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-02
- **関連企業:** 複数
- **要約:** AI DevCon speakers report the bottleneck in development has moved from coding to design and architecture. "Agentic Dev is no longer about coding" — for most teams, coding at scale is still hard but the real challenge is upstream. AI training is becoming the "new coding revolution" with fine-tuning skills commoditizing similarly to how coding skills did.
- **キーファクト:**
  - Development bottleneck shifted from coding to design/architecture
  - "Agentic Dev is no longer about coding"
  - AI training becoming the new coding revolution
  - Fine-tuning skills commoditizing like coding skills before
- **引用URL:** https://www.linkedin.com/posts/guypo_ai-devcon-carousel-activity-7462496536908754944-M42a
- **Evidence ID:** EVD-20260526-0043

### INFO-044
- **タイトル:** China AI investment: 17% of VC deal count, 38% of deal value vs 43%/89% in US
- **ソース:** LinkedIn
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04, BYTEDANCE-CHINESE
- **関連企業:** 複数
- **要約:** AI accounts for 17% of China's VC deal count and 38% of deal value, compared to 43% and 89% in the US respectively. ByteDance-alumni startups accumulated 2.5B yuan in funding in 6 months.
- **キーファクト:**
  - China: 17% of VC deal count, 38% of deal value in AI
  - US: 43% of VC deal count, 89% of deal value in AI
  - ByteDance-alumni startups: 2.5B yuan in 6 months
- **引用URL:** https://www.linkedin.com/posts/kaidigao_ai-accounts-for-17-of-chinas-vc-deal-count-activity-7462553158972698624-UpcW
- **Evidence ID:** EVD-20260526-0044

### INFO-045
- **タイトル:** Nvidia fiscal 2026: record $81.6B revenue, data center $170-190B
- **ソース:** Intellectia
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-04
- **関連企業:** Nvidia
- **要約:** Nvidia reported record $81.6B revenue with full-year fiscal 2026 data center revenue reaching approximately $170-190B. Fiscal 2027 estimates trending higher.
- **キーファクト:**
  - Record $81.6B quarterly revenue
  - Data center revenue: $170-190B annually
  - Fiscal 2027 estimates trending higher
- **引用URL:** https://intellectia.ai/blog/nvda-stock-earnings-analysis-may-2026
- **Evidence ID:** EVD-20260526-0045

### INFO-046
- **タイトル:** AI vendor lock-in: real moat is proprietary workflow data, not the model
- **ソース:** Instagram / Burkland / Substack
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-05, KIQ-004-04
- **関連企業:** 複数
- **要約:** Investors report "engineering alone is no longer a moat" — AI makes software easier to build, so investors focus harder on data, distribution, integrations, and domain expertise. "Most companies think their AI moat is the model. It's not. The real moat is proprietary workflow data." AI adoption is a survival signal, not just a growth story.
- **キーファクト:**
  - "Engineering alone is no longer a moat"
  - Real moat: proprietary workflow data, not the model
  - Investors focus on data, distribution, integrations, domain expertise
  - AI adoption is survival signal, not growth story
- **引用URL:** https://burklandassociates.com/podcasts/what-investors-look-for-in-the-ai-era/
- **Evidence ID:** EVD-20260526-0046

### INFO-047
- **タイトル:** CyberAgent FY2026 guidance: JPY 880B net sales, JPY 50B operating income
- **ソース:** SimplyWall.St
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-004-01, KIQ-004-04
- **関連企業:** CyberAgent
- **要約:** CyberAgent set FY2026 guidance at JPY 880,000M net sales and JPY 50,000M operating income. Company is driving autonomous actions at scale with Tableau Server and Tableau MCP. Japanese companies enjoyed rosy earnings thanks to significant AI-linked investment worldwide.
- **キーファクト:**
  - FY2026 guidance: JPY 880B net sales, JPY 50B operating income
  - Using Tableau Server + Tableau MCP for autonomous analytics
  - Japanese companies benefiting from global AI investment
- **引用URL:** https://simplywall.st/stocks/jp/media/tse-4751/cyberagent-shares/news/how-investors-are-reacting-to-cyberagent-tse4751-strong-h1-r
- **Evidence ID:** EVD-20260526-0047

### INFO-048
- **タイトル:** AI is replacing task pieces, not entire roles; radiologists still not replaced despite predictions
- **ソース:** CNN / Facebook / AIMultiple
- **公開日:** 2026-05-25
- **信頼性コード:** B-3
- **関連KIQ:** KIQ-004-01, KIQ-004-03
- **関連企業:** 複数
- **要約:** AI is replacing pieces of work (first drafts, data processing, scheduling) rather than entire roles. Radiologists still not replaced despite years of predictions. Bill Gates estimates AI could replace many doctors within 10 years. University of Rochester: work becomes more human with AI — empathy, curiosity, and judgment remain in human hands. Top AI-replaceable jobs: interpreters, translators, historians, customer service.
- **キーファクト:**
  - AI replacing task pieces, not entire roles
  - Radiologists still not replaced despite predictions
  - Bill Gates: AI could replace many doctors within 10 years
  - Empathy, curiosity, judgment remain human domains
  - Most replaceable: interpreters, translators, historians, CS reps
- **引用URL:** https://www.rochester.edu/newscenter/work-becomes-more-human-with-artificial-intelligence-704332/
- **Evidence ID:** EVD-20260526-0048

### INFO-049
- **タイトル:** OpenAI GPT-5.5 vs Claude 4.7 vs Gemini 3.5 Flash benchmark comparison
- **ソース:** YouTube / BenchLM
- **公開日:** 2026-05-25
- **信頼性コード:** C-3
- **関連KIQ:** KIQ-003-02
- **関連企業:** OpenAI, Anthropic, Google
- **要約:** GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.5 Flash benchmark comparison: Claude Opus 4.7 (Adaptive) has stronger overall benchmark profile than Grok 4.20. Gemini 3.5 Flash delivers near-Pro level coding and reasoning at Flash-tier cost and speed, described as "speed, cost, and multimodal gap is wider than expected."
- **キーファクト:**
  - Claude Opus 4.7 (Adaptive) > Grok 4.20 in benchmarks
  - Gemini 3.5 Flash: near-Pro intelligence at Flash cost/speed
  - Speed/cost/multimodal gap widening
- **引用URL:** https://benchlm.ai/compare/claude-opus-4-7-adaptive-vs-grok-4-20-beta
- **Evidence ID:** EVD-20260526-0049

### INFO-050
- **タイトル:** Washington Post: AI doesn't need a regulator, it needs a referee
- **ソース:** Washington Post
- **公開日:** 2026-05-22
- **信頼性コード:** B-2
- **関連KIQ:** KIQ-002-03, KIQ-005-03
- **関連企業:** 複数
- **要約:** Washington Post editorial argues Trump administration's delay of AI executive order provides opportunity to rethink approach. Instead of a regulator, AI needs a "referee" — safety standards that can keep pace with rapid development without stifling innovation.
- **キーファクト:**
  - WaPo editorial: AI needs a referee, not a regulator
  - Trump's delay of AI executive order as opportunity to rethink
  - Safety standards should keep pace with development
- **引用URL:** https://www.washingtonpost.com/opinions/2026/05/22/ai-needs-safety-standards-heres-better-way-implement-them/
- **Evidence ID:** EVD-20260526-0050
