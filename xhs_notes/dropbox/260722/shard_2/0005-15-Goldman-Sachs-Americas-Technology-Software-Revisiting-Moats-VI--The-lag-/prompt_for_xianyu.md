你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
AMERICAS TECHNOLOGY: SOFTWARE

# Revisiting Moats VI: The lag between AI spend and Security AI spend; and when to look for an inflection

In the last four months, the Security category has shifted from being viewed as at risk from AI to being a clear beneficiary, with the consensus view being: more AI spend means more Security spend, and this incremental Security budget is likely to largely accrue to today's platform leaders. We agree with this view; however, quantification and timing will matter to realizing alpha from here:

1. To date, we have yet to see a meaningful change in Security budgets for product. This creates a challenging set up into earnings because stocks have pre-traded a medium-term inflection. Our industry discussions suggest that enterprise agentic implementations are still immature and often run in isolated “sandbox” environments. While many security teams have a “blank check” strategic mandate, these incremental dollars today are being spent on more niche product POCs and on patching and hygiene management, which are not directly monetized in scale by the product companies in our coverage.

2. The question then becomes: when will the publicly-traded security companies see a more meaningful inflection in fundamentals? As a starting point, we take a look at the cloud cycle: it took 5 years for Security to inflect from $<1\%$ of cloud to spend to $2 - 5\%$ , which we view as steady state. If we count 2025 as Y0 of initial enterprise inference use cases and reconcile with our industry conversations, we expect an inflection in AI Security budgets may happen as soon as 4Q or 1H27, suggesting a 2-3 year lag. Our TAM math then supports a 2-3 pt boost to industry growth rates into 2028. Put simply, the AI Adoption cycle is happening faster than prior technology adoption cycles. The key underlying driver to watch is enterprises moving inference and agentic workloads from trials to production use cases that are not limited by sandbox implementations, which in turn is a key focus of our industry conversations into 3Q.

3. New security budget likely disproportionately accrues to today's leaders: The biggest risk in broader Software is that new AI value accrues to new entrants (AI natives, frontier models), rather than incumbents. This risk is lower in Security for two reasons: a) Security roadmaps are driven by machine learning (ML) innovation, not GenAI innovation; and this fundamental difference makes it hard

Gabriela Borges, CFA
+1(212)902-7839 |
gabriela.borges@gs.com
GS & Co. LLC

Max Gamperl +1(415)249-7311 | max.gamperl@gs.com GS & Co. LLC

Praachi Arora
+1(332)245-7970 |
praachi.arora@gs.com
GS India SPL

for new entrants to replicate the advantages of deep human re-enforcement learning feedback loops and labeled datasets; b) Security leaders are being aggressive in acquiring new technology assets from a richly-funded private company landscape (we estimate >\$2.3bn in the last 18 months).

4. Product cycles to watch: We expect the most discernible product cycles to be in a) next-gen AI detection and response for agentic runtime use cases (i.e. monitoring agents) and associated security operations center (SOC) infrastructure upgrades, where CRWD and PANW have outsized exposure; b) identity, where we think OKTA is best positioned given its cloud native back end and a renewed product cycle with Auth0 given outsized mindshare with developers; and c) select niche product cycles such as prompt engineering and data protection.

5. Blue sky scenarios for PANW and CRWD suggest both can grow into their valuations; with OKTA having the most potential to inflect from lower absolute growth rates and valuation. We are cognizant that Security stocks are expensive relative to their growth profile and history, and we now have modest upside to our revised price targets for PANW and CRWD. However, we also present blue-sky scenarios for PANW and CRWD that show the potential for CY28 FCF to be higher by as much as $30\%$ vs. our estimates. In this illustrative scenario, PANW and CRWD would be trading at implied EV/FCF/growth multiples below that of the $20\%+$ software cohort today.

Exhibit 1: Key inflection points in the past six months have driven the Security sector higher at the same time as broader Software has derated  
![](images/28a2af0aac8c07d6d4c2abb82ce51856afddd4e87a400610348c60153cbdd36a.jpg)  
Source: FactSet, Data compiled by GS Global Investment Research

Exhibit 2: Platform leaders have driven a step function higher in Security sector valuations in the last 4 months  
![](images/95daf158cd72e9dc0ad62401942b121e3f896afd69de681153b211b6a3d56ceb.jpg)  
Source: FactSet, Data compiled by GS Global Investment Research

Exhibit 3: Security fundamentals have yet to inflect higher; look for improving lead indicators (e.g. bookings) into 2HCY  
![](images/43fe144c71fdaa27e2bfc5ec1fe2482e0bda71e4cd416bb0ee675cda7f6564b0.jpg)  
Source: Company data, GS Global Investment Research

## The Cloud Security Cycle

Exhibit 4: Security Cloud revenue was de minimis into 4+ years of the IaaS ramp

Cloud security revenue as a \% of hyperscaler IaaS revenue

![](images/cb9bd10bb0ff46b88dd88672da7841a771546da561afffab1b2aade02b0aa349.jpg)  
Source: Gartner, Company data, GS Global Investment Research  
Exhibit 5: Estimated Palo Alto virtual firewall mix inflected after FY18, reaching \~30% of product revenue by FY23 and 45%+ in FY26  
Palo Alto virtual firewalls as a \% of total product revenue

![](images/a529b93a5c5574532105cf9f8b231cadb6659b6e994fa8454e148841ba31594f.jpg)  
Source: Company data, GS Global Investment Research

We benchmark the beginning of the cloud security cycle to 2015: this is when Amazon first disclosed AWS metrics at \$4.6bn in 2014 revenue and 17% operating margin, in contrast to the consensus view that cloud was a low or negative margin business. Through 2016 and 2017, our industry conversations suggested that the cloud security ecosystem was unchartered and somewhat chaotic territory: there was a fair amount of confusion amongst CISOs as to how to secure cloud workloads, there were many new point products to consider, and the hyperscalers began to embed security functionality into their PaaS offerings as a means of differentiation. In early cloud years, we believe many CISOs simply routed traffic back to their existing firewall DMZ to apply security policies, with minimal new demand for cloud-specific security products. Early cloud workloads also tended to be customer facing, which generally required less security than internal facing workloads (e.g. content streaming from Netflix and eCommerce websites did not require complex network and endpoint tooling).

There were milestones in 2016, 2017, and 2018 that illustrated a maturation in the Cloud Security Market. Several market dynamics began to converge: CISOs had a better understanding of what security building blocks were needed in the cloud, point products began to mature in the quality of their offerings to justify incremental spend beyond hyperscaler security, customers began to consider more regulated and sensitive workloads in the cloud, and multicloud architectures became more common. In parallel:

■ Gartner first published its Cloud Security Market Guide in 2016

Gartner first published its Cloud Access Security Broker (CASB) Magic Quadrant in late 2017. CASBs delivered a layer of security between enterprise users and SaaS hosted applications like Salesforce.

2018 was the first big year of Security Cloud M&A, with Palo Alto acquiring Evident.io for \~\$200mn and RedLock for \$173mn, and Check Point acquiring Dome9 for \$175mn. In 2019, Palo Alto acquired Twistlock for \$410M, PureSec for \$47M and Aporeto for \$150M in 2019. There was also roughly \$1.3B of M&A before cloud security became a major standalone revenue category.

We view 2020 as the first year when security spending inflected; we estimate from $1.3\%$ to $2.9\%$ based on Gartner cloud disclosures on cloud security category revenue as a percentage of IaaS revenue, as defined by aggregating AWS / Azure / GCP IaaS revenue. COVID was likely a catalyst, as employees essentially went to $100\%$ virtual access over a short period of time in March/April 2020. We consider both Cloud Security Posture Management and Cloud Workload Protection Platforms Gartner disclosures.

Wiz scaled from \$1mn ARR in early 2021 to \~\$100mn ARR by mid-2022 and \~\$250mn ARR by early 2024;

■ PANW disclosed Prima Cloud ARR of >\$200mn in 2021, >\$500mn in 2023 and >\$700mn in 2024

■ CRWD disclosed Falcon Cloud Security ARR of >\$400mn in FY24 and >\$600mn in FY25.

We arrive at two key observations: It took 5 years from the beginning of the IaaS cloud cycle to realize a meaningful inflection in Cloud Security revenue; and 2-5% is a reasonable benchmark for Security budgets as a % of IaaS budgets.

## The AI Security Cycle

Exhibit 6: We estimate a \~\$20bn Security AI TAM in 2031 based on the Cloud Security attach rate and a rough forecast for IaaS inference revenue
Security TAM - Base vs. AI

![](images/f2647e3862023a36022ae19af0d09e4297e067fd6e0710f0413f2f96c0348749.jpg)  
Source: GS Global Investment Research, Gartner  
Exhibit 7: AI likely drives a 3pt boost to Security TAM growth rates in the next \~12-24 months
Estimated boost to Security TAM growth rates from AI

![](images/5573e027a8b47c85c38445c6251911072e4e98ac4eb96e959e948cb726d9f0f9.jpg)  
Source: GS Global Investment Research

We benchmark the beginning of the AI enterprise cycle to 2025. This is when our industry conversations suggested a) a more meaningful shift between AI training and AI inference workloads in the enterprise; and b) more trials in agentic applications (link to last year's agent report). Based on our conversations, AI training workloads are mostly internal facing and require minimal amounts of incremental security spend, with the exception of new select sovereign data centers. In contrast, inference workloads need to be embedded in enterprise systems to be useful, and thus require a robust level of security as they move from proof of concept and sandboxing into full production.

## To date, AI disclosures from the security companies have been early and mostly directional:

\- Palo Alto: Prisma AIRS is Palo Alto's AI segment, which includes runtime threat defense, model vulnerability scanning, security posture management and red teaming tolls across AI applications and models. AIRS has 300+ customers and is approaching \$100M ARR. In our 2Q conversations, Palo Alto noted that Prisma AIRS has reached 8-10% of total AI spend in some customer scenarios, suggesting higher attach rates are possible than our baseline 2-5% assumption.

CrowdStrike: CrowdStrike's AIDR (AI detection and response) ARR grew 250%+ sequentially in the April quarter (1QFY27), with a \$50M+ pipeline. AIDR represents the company's AI security suite across model, data and agentic security, with recent acquisitions Pangea and SGNL extending coverage into AI applications and agentic identity.

Zscaler: AI Protect generated \$100M+ of bookings over the past year. This segment includes Zscaler's AI security products across AI app protection, model / data security and AI-SPM, including discovery of LLMs, workflows and MCP servers. Zscaler launched its AI broker at its Zenith conference in June; this product secures agentic communications across MCP and agent-to-agent workflows, with policy

controls around what each agent can access.

Fortinet: Fortinet has yet to disclose a standalone AI security number and generally leans toward more organic development vs. M&A. In its March quarter, Fortinet noted improving data center AI demand for firewalls and internal segmentation firewalls, in part driven by sovereign programs in the Middle East.

Check Point: Check Point has not disclosed a standalone AI security number; management has said AI security revenues are still not significant but the funnel has grown materially. Check Point's AI security push is built around Lakera, which provides runtime protection for AI applications and agents, including defenses against prompt injection, data leakage and model manipulation. Check Point is also building AI security into its broader platform through employee AI usage controls, AI factory/NVIDIA infrastructure security and Infinity AI Copilot.

Okta: New products were \~25% of bookings in 1Q, up meaningfully yoy, with \~40% ACV uplift when included in deals. AI products include Auth0 for AI Agents and Okta for AI Agents, which secure and govern AI agents across the full lifecycle, including access to third-party MCP servers and discovery/control of agent sprawl. These specific products are still small relative to total revenue, early customer traction and pipeline is strong, and AI-agent deal sizes are larger than average.

\- SailPoint: SailPoint expects AI ARR to exceed \$100mn by the end of FY27. SailPoint defines AI ARR as Agentic Fabric, Agentic Suites and agentic add-on modules, with the core product focused on governing AI agents, nonhuman identities and the access those agents have to applications and data. Nonhuman identities drove 40% of identity growth last quarter and 20% of net new ARR came from emerging products inclusive of AI, suggesting agentic identity is becoming a more visible growth driver.

SentinelOne: In our June meeting, SentinelOne acknowledged that recent AI model headlines are driving more attention to AI security conversations, but it has yet to see a material departure from steady-state spending patterns. Prompt Security is seeing the clearest AI pull-through, followed by agentic SoC and cloud runtime. Most notably, Prompt has moved from \~0% to \~20% of pipeline in a matter of weeks and ARR has close to doubled in each of the past two quarters (4Q and 1Q). S is also having more conversations around its data business for the agentic SoC as customers increasingly want a flexible approach.

In terms of actual AI security adoption, it is much clearer to us now why we have not yet seen a meaningful AI tailwind to public security companies. We spoke to many security practitioners in 2Q who told us that agentic implementations are still largely running in sandboxes, or isolated environments that are temporarily spun up and down. We also believe part of the disconnect between broader agentic AI adoption data and limited traction for security vendors is that some of this activity is happening on unmanaged and/or personal devices, where enterprise security vendors have less visibility today.

## Bridging to our AI security forecast:

■ Using company disclosures with a few rough assumptions on share between public and private vendors, we estimate about \$100-200mn in AI security revenue in 2025. We then calculate a bottom up build of AI IaaS revenue based on estimates/disclosures from Microsoft, Amazon, CoreWeave and Oracle, and we assume these disclosures together are about two thirds of the AI TAM in 2025 (with the largest undisclosed contribution from Google). We estimate that the mix between inference and training workloads in 2025 was roughly 50/50, growing to 75% this year and stabilizing at 85% of mix in the next two years.

We then forecast Security AI revenue as an attach rate on IaaS AI inference revenue. We start with our 2025 estimate of \~\$100mn Security AI revenue over an AI IaaS inference TAM of \$17bn, implying 0.6% attach rate. We then use the cloud security inflection as precedent, mapping 2019 and 2020 (Y4 and Y5 of the cloud cycle) to 2027E and 2028E (Y2 and Y3 of the AI cycle).

We arrive at a \~\$20bn AI Security TAM in 2031, implying a 2 pt boost to industry growth rates. We view this initial forecast as conservative given the potential for AI security to drive more value than cloud security; at a

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
