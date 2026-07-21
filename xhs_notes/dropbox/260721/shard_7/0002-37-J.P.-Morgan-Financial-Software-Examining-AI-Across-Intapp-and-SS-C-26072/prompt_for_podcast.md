你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Financial Software

## Examining AI Across Intapp and SS&C

In this note we take a closer look at how both INTA and SSNC are utilizing AI. We focus on what is changing in their product stacks, how governance and data foundations shape real-world deployability, and where AI is already showing up in bookings (INTA) versus cost savings/margin expansion (SSNC). Both companies are aggressively transitioning towards “agentic AI” strategies, though they approach the market from different structural positions. Intapp is focused on a “Firm AI” concept, providing a governed agentic platform specifically for the unique compliance and conflict-of-interest requirements of professional services firms. In contrast, SS&C leverages its massive scale as “Customer Zero”, deploying AI agents internally across its own business process outsourcing (BPO) operations to drive margin expansion before commercializing these solutions for its 23,000+ global clients. We continue to like INTA (OW) and remain relatively more cautious on SSNC (N) vs. the rest of our Vertical SaaS coverage.

\- INTA vs. SSNC: different starting points, same destination (agentic AI). INTA is approaching agentic AI from a cloud-native vertical SaaS posture (Celeste as a firmwide agentic platform), while SSNC is approaching it from scaled “intelligent automation” and systems-of-record/BPO operations (WorkHQ as orchestration on top of Blue Prism). Should these companies succeed with their strategic plans, they would likely win in different ways: INTA via faster product-led SaaS adoption, SSNC via operational leverage and proven-at-scale deployments.

\- INTA + SSNC: governance as the monetizable control layer. Both companies are positioning themselves as the infrastructure that regulated customers must route AI through to keep deployments permissioned, auditable, and safe—INTA via ethical walls/conflicts/MNPI-aware controls for professional firms, and SSNC via enterprise guardrails and compliance-first governance for regulated financial and healthcare workflows. The takeaway is that governance is not a “feature”; it’s the adoption bottleneck, and both are trying to own that choke point.

\- INTA's AI-defensibility looks structural; SSNC's looks execution-dependent. INTA's differentiation is a tighter “context + governance + workflow embedment” story (firm institutional memory plus broader data context, wrapped in always-on policy enforcement and distributed through day-to-day workflows), which supports scalable multi-tenant rollout. SSNC's moat is deep proprietary data and scale, but its AI upside depends on packaging internal “Customer Zero” wins into a unified external platform despite portfolio complexity and an outsourcer perception—so the actionable watch-items are cohesion of the product suite, clarity of go-to-market, and consistency of client experience.

• We are establishing our Dec-27 PTs for both names: INTA PT of \$47/sh and

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap($ mn)</td><td rowspan="2">Price ($)</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>Intapp</td><td>INTA US</td><td>2,356.40</td><td>29.12</td><td>OW</td><td>n/c</td><td>47.00</td><td>Dec-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>SS&amp;C Technologies</td><td>SSNC US</td><td>16,854.90</td><td>69.56</td><td>N</td><td>n/c</td><td>87.00</td><td>Dec-27</td><td>94.00</td><td>Dec-26</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 17 Jul 26.

See page 14 for analyst certification and important disclosures.

## Vertical SaaS & HealthTech

Alexei Gogolev AC
(1-212) 622-9391
alexei.gogolev@JPM.com

Isabella A Camaj

(1-212) 834-2379

bella.camaj@JPM.com

Ella Smith
(1-212) 622-2451
ella.smith@jpmchase.com

Destiny Jackson

(1-212) 622-4360

destiny.jackson@JPM.com

JPM Securities LLC

SSNC PT of \$87/sh. We are making modest housekeeping changes to our INTA forecasts, and as a result, keep our new end-27 INTA PT unchanged at \$47/sh (similar to end-26E previously). At our PT, INTA would trade at 20x 2027 EV/EBITDA, which we view as reasonable for a relatively balanced Rule of 40 company. For SSNC, we have trimmed our mid-term revenue growth and margin expectations as we view recent de-emphasizing of traditional tech budgets as a mid-term risk for demand. As a result, we are establishing a Dec-27 PT of \$87/sh (vs. a Dec-26 PT of \$94/sh prior). At our PT, SSNC would trade at 10x 2027E EV/EBITDA, which reflects lukewarm organic revenue growth outlook - an arguably reasonable multiple for a rule of 20 company.

## Overview

Table 1: CY27 Financial and Valuation Summary

<table><tr><td>CY2027</td><td>SSNC</td><td>INTA</td></tr><tr><td>MCap</td><td>$17B</td><td>$2B</td></tr><tr><td>JPM Rating</td><td>N</td><td>OW</td></tr><tr><td>JPM 27E PT</td><td>$87</td><td>$47</td></tr><tr><td>Revenue Growth</td><td>5%</td><td>14%</td></tr><tr><td colspan="3">As % of Revenue</td></tr><tr><td>S&amp;M</td><td>8%</td><td>26%</td></tr><tr><td>R&amp;D</td><td>7%</td><td>21%</td></tr><tr><td>G&amp;A</td><td>6%</td><td>11%</td></tr><tr><td>Capex</td><td>4%</td><td>2%</td></tr><tr><td>FCF</td><td>22%</td><td>29%</td></tr><tr><td>FCF (as % of EBITDA)</td><td>56%</td><td>115%</td></tr><tr><td colspan="3">Valuation</td></tr><tr><td>EV/EBITDA (27E/5YR Average)</td><td>8x / 11x</td><td>12x / 74x</td></tr><tr><td>EV/FCF (27E/5YR Average)</td><td>15x / 22x</td><td>14x / 61x</td></tr></table>

Source: JPM estimates, Bloomberg Finance L.P.

Architectural starting points. INTA and SSNC are converging on agentic AI, but from fundamentally different bases: Intapp is a cloud-native vertical SaaS platform for professional firms, while SS&C is a scaled, software-enabled services and systems-of-record provider that is layering AI orchestration onto an automation (RPA) foundation built around Blue Prism.

Both are essential from a governance perspective. Both SSNC and INTA are positioning themselves as critical governance layers in the transition to agentic AI, aiming to make LLM adoption auditable, permissioned, and safe in highly regulated workflows. Intapp frames governance through ethical walls, conflicts, and MNPI-aware access controls for “Firm AI,” while SS&C emphasizes enterprise-grade controls (guardrails, data protection, explainability, and human-in-the-loop) for regulated financial services and healthcare use cases.

How AI is operationalized (platform vs. proving ground). Intapp is productizing agentic AI primarily through Celeste and adjacent workflow modules that embed AI directly into BD, deal execution, and compliance processes, with monetization tied to SaaS expansion and (increasingly) AI activity. SS&C's model is “Customer Zero” first—deploying digital workers and agents internally to drive measurable cost savings and margin expansion—then commercializing those production-tested patterns via WorkHQ, AI Gateway, and vertical product embeds.

What ultimately differentiates outcomes. Intapp's edge is a unified “context + governance” story (firm institutional memory plus an industry graph, wrapped in policy enforcement) that supports scalable, multi-tenant agent deployment across firms. SS&C's edge is operational scale and deep systems-of-record data in core processing domains, but its AI narrative has to overcome portfolio complexity and an outsourcer perception by presenting a more unified, technology-led platform experience to clients.

## Intapp

Intapp's AI strategy centers on governed, model-agnostic agentic workflows for professional services, where ethical walls and confidentiality controls are core product requirements. It is positioning itself as the control plane for adopting frontier-model capabilities safely—combining deep AI partnerships with governance features like Walls for AI. That strategy is increasingly embodied in Celeste (its flagship agentic platform launch), alongside Assist and AI-enabled workflow modules, and is reinforced by recent acquisitions that expand workflow coverage and deepen Microsoft 365 integration—supporting a defensibility thesis rooted in compliance-grade deployment and embedded distribution.

AI partnerships. Intapp has strategically positioned itself at the center of the agentic AI shift by forming deep partnerships with leading frontier model providers and technology platforms. Intapp has collaborated with OpenAI to allow users to access its D&B Commercial Graph within ChatGPT and Codex via MCP servers. This integration is primarily focused on finance workflows, enabling professionals to bring verified business identity, credit, and risk data directly into natural language prompts. Intapp has also integrated with Anthropic to make its business data available within the Claude platform ecosystem. Additionally, Intapp established a strategic partnership with Harvey, a leading generative AI platform for legal professionals, to provide a governed and compliant framework for AI deployment in the legal industry. Harvey is standardizing on Intapp's Walls for AI and the Celeste platform to power its confidentiality controls. This integration ensures that interactions within Harvey's tools — including Assistant, Vault, and Workflows — automatically respect existing firm policies and professional responsibility obligation.

Core AI Products and Features. Collectively, Intapp's AI product suite is built around a single theme: embedding agentic automation into day-to-day professional workflows while keeping governance, confidentiality, and policy enforcement “always on.”

\- Recently launched: Celeste. Intapp has recently launched Celeste, which it characterizes as the most significant product launch in its history. Celeste is a model-agnostic, governed agentic AI platform designed to automate core workflows in business development, deal management, and compliance while strictly adhering to professional responsibility standards like ethical walls.

\- Intapp Assist: A generative AI add-on that provides summarization, email outreach assistance, and narrative generation

\- Walls for AI: A governance layer that extends Intapp's ethical wall protections to third-party AI tools like Microsoft 365 Copilot, preventing the “ungoverned co-mingling” of sensitive client data.

\- Intapp Time (New Release): An AI-enabled timekeeping solution that captures billable hours automatically, which has served as a primary catalyst for cloud migrations.

\- Intapp DealCloud Activator: A research-backed growth platform that uses AI to embed business development coaching and prioritized “next-best actions” into professional workflows.

AI Monetization. Intapp is transitioning from traditional per-seat licensing toward new consumption-based models for its agentic AI platform, moving quickly to establish direct monetization through specific product SKUs and a major architectural shift toward agentic AI. The company has launched products such as Intapp Assist as monetized offerings where existing clients can purchase the functionality for a specific price with a unique SKU, rather than it being a free upgrade. More recently with the launch of its Celeste platform, Intapp is introducing a model that includes a platform fee plus consumption-based pricing. This model charges based on the value created by expert agents and the volume of business activity flowing through the platform.

Recent AI-Enabling Acquisitions. Intapp's M&A strategy is a deliberate vertical-first “land & expand” playbook: acquiring niche, industry-specific assets that deepen its pre-built workflow “blueprints” and expand TAM/SAM by pulling Intapp into adjacent subverticals (particularly within financial services and real assets). The company has prioritized targets that add differentiated data/context or compliance-grade workflow depth—capabilities that are difficult for horizontal platforms to replicate—and that can be distributed across the broader Intapp installed base through cross-sell and tighter platform integration.

\- TermSheet (2025): Acquired to create a unified operating system for real assets, incorporating “Applied AI” to automate underwriting and investment lifecycles in the commercial real estate market.

\- delphai (2024): A Berlin-based AI company specializing in structuring firmographic data from public sources to provide validated intelligence with direct source citations

\- Transform Data International (TDI) (2024): A partner that builds enterprise collaboration technology, acquired to deepen AI integration with Microsoft 365 tasks

## Celeste in Action: Management-Led Product Demonstration

Last Wednesday morning, in a session led by Thad Jampol (Co-Founder and Chief Product Officer), Intapp overviewed the main use cases for its recently launched Celeste tool. Celeste supports hundreds of business workflows across professional firms, and management underlined it as more than a “specialized copilot” — the advantage isn’t the model, but what’s built on top (workflows, integrations, permissions, and playbooks). Management repeatedly framed Celeste’s proprietary value as being grounded in a firm’s own institutional context (deals, clients, relationships, prior work product, and judgment) rather than operating as a generic layer trained on broadly-available internet data. Amid the ongoing AI proliferation debate within Vertical SaaS, we walked away from the webinar further encouraged by Intapp’s AI defensibility moat and the value offered to firms by Celeste.

\- Deal sourcing and relationship building. Celeste was positioned as compressing time-consuming origination work—especially mapping who knows whom—into fast, decision-oriented outputs (e.g., board intelligence/outreach maps) that blend the firm’s relationship graph with external enrichment, then rank outreach paths so teams can spend time on angle development and relationship deepening rather than stitching inputs together.

\- AI defensibility highlighted by a client: “The intelligence is ours, and not something generic tied to Hg Capital." Intapp featured a customer, Shirin Veeran (Data & AI at Hg Capital). The client highlighted the real AI-defensibility piece Intapp emphasizes: the compounding advantage of a firm's own structured institutional data and workflows (i.e., screening and recommendations grounded in the firm's mandates, criteria, and historical experience rather than generic heuristics). Importantly, Celeste sources information from multiple sources: i) proprietary firm data already contained within DealCloud, ii) publicly available data online, and iii) third-party data providers enabled through Intapp's ecosystem/ connectors (e.g., MCP-style connectors and existing data partnerships). While pulling insights from the web to augment a firm's internal data, the data returned is tailored to a firm's configured terminology and operating model—and constrained by firm permissioning/ethical walls (so users only see what they are entitled to see).

\- Differentiation vs. generic models / “what’s built on top.” Intapp’s core claim was that access to foundation models is increasingly commoditized, so the durable differentiation is (1) native system-of-record integration and “day-one inheritance” of firm configuration (data structures, definitions, nomenclature, permissions), and (2) playbooks that encode repeatable firm procedures (e.g., deal screening gates like mandate/criteria/preferences) so outputs are grounded in process logic with clearer lineage back to the system of record. This framing carried through demos that chained workflows (screening → modeling → IC materials and reporting) and emphasized reliability via structured historical data plus user-enabled connectors (rather than uncontrolled external retrieval).

\- BakerHostetler: governance is the adoption requirement. Katherine Lowry, current Intapp customer and Chief Information Officer at BakerHostetler, described adoption anchored on pillars across growth, compliance, and profitability, with near-term focus on conflicts and intake. She emphasized that implementation has moved beyond generic productivity discussion into a sandbox phase with live teams, and that governance is central—enabling broader sharing of workflows/playbooks while maintaining secure, structured, permission-based controls over who can use what and what data can be accessed.

\- Bottom line. Across investment and legal workflows, Celeste was positioned as “firm AI” (AI for the business of the firm) rather than a generic copilot: grounded in proprietary firm intelligence, enriched via ecosystem data when enabled, and governed with guardrails for professional-firm obligations (e.g., MNPI controls, ethical walls, confidentiality, and independence). The strategic message was a compounding advantage flywheel: as firms use Celeste to execute and document decisions through playbooks, institutional memory deepens—benefiting early adopters as each quarter adds more proprietary context for future workflows.

AI defensibility is strong. Intapp's moat comes from serving as the governance and compliance control plane that professional services firms need before they can deploy AI agents at scale. By enforcing ethical walls, conflicts, and MNPI restrictions at the architecture layer, Intapp ensures AI tools inherit the same access constraints as humans —reducing inadvertent data co-mingling and regulatory risk and helping firms move from pilots to production. Just as importantly, Intapp has a “data context” moat: Celeste can ground models in a firm’s proprietary institutional memory (transactional, compliance, and relationship history) while also enriching outputs with Intapp’s broader data ecosystem and structured intelligence (e.g., firmographic data), creating a context engine horizontal AI providers can’t easily replicate. This combination protects and activates proprietary knowledge in a secure environment, while embedding compliance early in the engagement lifecycle to defend realization and margins as AI accelerates

workflow velocity.

## SS&C

SS&C's AI strategy is rooted in “Intelligent Automation”, primarily driven by its \$1.65B acquisition of Blue Prism. SSNC utilizes its scale — 29,000 employees and 23,000 clients — as a testing ground, and then aims to deliver production-tested AI solutions that meet the rigorous security and compliance standards of the financial services and healthcare industries.

Core AI Products and Features. SS&C's AI product stack is unified by a

[中间内容因长度限制已省略]

tes is distributed in the U.S. by JPMS who accepts responsibility for its content.

General: Additional information is available upon request. The information in this material has been obtained from sources believed to be reliable. While all reasonable care has been taken to ensure that the facts stated in this material are accurate and that the forecasts, opinions and expectations contained herein are fair and reasonable, JPM Chase & Co. or its affiliates and/or subsidiaries (collectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in
"""
