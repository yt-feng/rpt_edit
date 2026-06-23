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
# AMERICAS TECHNOLOGY: HARDWARE

# Traditional & accelerated servers: An industry primer

This report serves as a comprehensive primer on the server industry, designed for both seasoned technology investors and those new to the hardware sector. It provides a foundational analysis of the market's technological evolution over the last 70 years, current competitive dynamics, and the financial frameworks governing the industry. By grounding our analysis in historical trends and current unit economics, this report aims to equip investors with the necessary tools to navigate the near-term volatility and long-term shifts within the global server ecosystem.

## Key areas of focus in this primer include:

2026-30 server market forecast: 650 Group forecasts the global server market to grow at a +38% 5-yr CAGR to \$1.4 tr by 2030, driven by +13% growth in traditional servers (\$164 bn in 2030) and +45% growth in accelerated servers (\$1.2 tr in 2030). Both the traditional server and accelerated server markets should see double digit growth across all customer verticals, with strength in hyperscaler & neocloud driven by continuous AI infrastructure build outs, while enterprise demand should benefit from data center modernization efforts in support of agentic AI adoption & broader technology refresh. Also includes a summary of the role of a CPU and GPU within AI infrastructure deployments.

■ Market structure and vendor dynamics: An examination of the server vendor landscape, where market share varies meaningfully based on the customer vertical. Enterprise market is highly concentrated and dominated by branded OEMs, including Dell, HPE, Lenovo, and IBM, while the hyperscale opportunity is primarily addressed by white box vendors; neoclouds currently use a mix of both OEMs and ODMs.

Unit economics and impacts of changing commodity costs: A detailed breakdown of traditional and AI server bill of materials (BOM). We estimate that server OEMs typical earn 15% gross margins and 5-7% operating margins on a CPU server sale. DRAM & NAND historically represented \~30% of the bill of materials for a traditional server, but under current industry expectations price increases in 2026/27, memory could represent >60% of the bill of materials for a traditional server by the end of calendar 2026, assuming no offsetting actions.

## Katherine Murphy

Katherine Murphy
+1(212)902-1151 |
katherine.a.murphy@gs.com
GS & Co. LLC

Michael Ng, CFA
+1(212)902-8618 | michael.ng@gs.com
GS & Co. LLC

Zorayda Montemayor
+1(212)357-6403 |
zorayda.montemayor@gs.com
GS & Co. LLC

## Table of Contents

Traditional Servers 5
Accelerated Servers 15
How do higher commodity costs impact the server market? 23
Disclosure Appendix 27

## Defining the server market

Servers are specialized computers that run application-specific services for clients. While PCs & servers share similar architecture, servers are typically designed with more CPU/GPU sockets, memory, and redundancies around power supplies/network interfaces to ensure availability for mission-critical workloads. In the enterprise, servers are used to address the edge or front end of the network for applications such as collaborative business software, web serving, file serving, and email. Cloud providers deploy servers in data centers in massive quantities (on the magnitude of hundreds of thousands) to run applications for cloud computing, search, video delivery, social networking, and more recently - generative AI workloads.

The total server market was \~\$284 bn in annual revenue in 2025, up +45% yoy driven by robust growth in AI server demand & higher ASPs. All server market estimates (both market share & forecasts) in this primer are based on 650 Group data unless otherwise noted. 650 Group expects the overall server market to grow at a 38% CAGR over the next five years to \~\$1.4 tr 2030, driven by growth driver by AI server demands. While the server market has historically been driven by new technology adoption & infrastructure refresh cycles, the robust AI driven growth realized in 2023 and 2024 marks a significant inflection from historical growth trends. As such, for the purposes of this report, we examine the traditional server (i.e., general purpose, non-accelerated servers) markets and accelerated server (i.e., high performance server with added GPUs or other custom accelerators) separately.

Exhibit 1: The total server market was \~\$284 bn in annual revenue in 2025, up +45% yoy driven by robust growth in AI server demand & higher ASPs
Industry server revenue (\$, mn) and growth (%)  
![](images/9aa6df197e368ca345ec3bd8c0e0c352658623e5bc797f2edc508a344ed93a4f.jpg)  
Source: 650 Group

Exhibit 2: Industry server units were down 13% yoy in 2025 driven by AI server demand that was more than offset by a decline in traditional servers; both traditional and AI server units are expected to grow in 2026
Industry server shipments (units, 000s) and growth (%)

![](images/871941a204d3d8ebf737fe3a5c6e69c41040c1278996962c39e4e184919533f2.jpg)  
Source: 650 Group

Exhibit 3: Vendor market share differs significantly by vertical & product (AI v. traditional)
Server segment summary

![](images/63ea49b3cd3e2d634af75488e96cc780eb1f6166a29178cc35f36772ad057349.jpg)

![](images/079de5a853a8d3f92bc22e40a020a497cad96322c6e318c475fc3e5966d2cf77.jpg)

Source: 650 Group

## Traditional Servers

The traditional server market was \~\$89 bn in annual revenue in 2025 (+10% yoy) with approximately 8.4 mn units sold (-18%) at an average selling price of \~\$10,500 (+35% yoy), based on 650 Group. Traditional servers, also referred to as general purpose servers, are deployed across various environments ranging from on-premise server rooms to data centers, often used for more general purpose workloads like web hosting, databases management, file sharing, or application servers (v. specialized workloads like AI/ML). For AI inference and training, non-accelerated servers are used for orchestration and control plane layers. A traditional server includes a CPU, memory, storage, etc. Unlike AI servers, traditional servers do not have an embedded accelerator card (i.e., GPU).

Exhibit 4: The traditional server market was \~\$89 bn in annual revenue in 2025 (+10% yoy)...
Industry traditional server revenue (\$, mn) and annual growth rate (%)  
![](images/04f4c246c96216516fad23de54a4ac89ee7f38e4738678592bd813e2da26b53e.jpg)  
Source: 650 Group  
Exhibit 5: ... with approximately 8.4 mn units sold at an average selling price of \~\$10,500
Traditional server shipments (units, mn) and ASP (\$)

![](images/8ec8f4a740bc893636a53cced7ad5e9c78f28426fe6a4a841e4b2ced259a8568.jpg)  
Source: 650 Group  
2024 traditional (non-accelerated) server shipments by CPU architecture

Exhibit 6: Industry standard servers are based on the x86 CPU architecture

![](images/cfccf8e0abc61b7f00637ff0304accb453005a3681b5fc9465f6a04ccef9c9e9.jpg)

Exhibit 7: The majority of traditional servers are rack-mounted or modular
2024 traditional (non-accelerated) server shipments by form factor  
![](images/a2096af53a83a4df60cffe064e6d32a0cf9892564ae7ab3ab85a51575d41641e.jpg)  
Source: IDC, Data compiled by GS Global Investment Research  
Source: IDC

The earliest servers introduced in the 1950s were mainframe computers, which are high-performance, highly reliable computing systems. Mainframes employ a centralized architecture with large processors and memory capacity, and most importantly, with multiple layers of redundancy which helps guarantee high availability. Although mainframe only represents a minor share of server volumes by unit shipments, mainframes represents a significant share of mission critical workloads for industries that require continuous operations like financial institutions, healthcare companies, and government agencies (IBM reports that 90% of the top 50 banks run on IBM Z, its Mainframe solution). Rack-mounted servers were introduced in the 1990s to address the growing demands of internet infrastructure. Rack-mounted servers are built in standardized units (called rack units (“U”), each 1.75” tall and 19” tall) and installed in a chassis or rack (standard server racks are 42U tall). This standardization allows for increased efficiency, scalability, and easier management; rack-mount servers are typically the more cost-effective compute solutions. Servers come in a variety of form factors but standard CPU servers are typically 1U or 2U, which means up to \~20-40 servers fit on each rack when leaving space for other appliances like power, cooling, networking, and storage. Each rack-mount servers typically contains all of the

components needed to operate as a standalone system (e.g., compute, memory, power, storage, etc), as compared to blade servers that are designed in a more modular style to increase density & therefore processing power. Each blade includes critical components for a server like a CPU and memory & is installed within a specialized chassis which provides shared infrastructure like networking, power, and cooling. Blade server chassis are designed to fit within industry standard server racks. Similarly, multi-node servers are similar to blade servers in their modular design & share resources, except they do not share network fabrics. Tower servers are standalone upright server cabinets - similar in form factor to a traditional desktop computer- but with upgraded components (e.g., compute, memory), typically used by SMBs.

## Exhibit 8: Servers are available in several form factors including mainframe, rack-mounted, blade, and tower

![](images/5586f7b8eff58b8ea6419210989cf98862d0e491a5e7c61d1e69c24f9b9b1966.jpg)  
Source: Company data, GS Global Investment Research

Industry standard servers are based on the x86 CPU architecture, which is the most commonly deployed CPU architecture across network infrastructure, data centers, and cloud providers, representing \~85% of units deployed in 2025, per Gartner. x86 architectures (e.g., Intel Xeon, AMD Epyc) support a wide range of instructions & is compatible with a wide range of software and operating systems. ARM (15% and growing) architectures are designed to compute simpler instructions, which results in a more power efficient solutions that are more cost-effective. Custom silicon designed by hyperscalers (e.g., AWS Graviton, Google Axion) & Nvidia's Grace CPU use ARM-based architectures. Because different CPU architectures have unique instruction sets, software complied for one architecture cannot typically run on another architecture without recompiling, which can be a significant lift for enterprise organizations. Other

CPU architectures include RISC, CISC, and EPIC. GS Semiconductor Analyst James Schneider expects that the x86 instruction set will maintain a majority share of the server CPU market, particularly in enterprise, with some share gains for ARM server CPUs, especially at hypercscalers who are building custom hardware focused on lowering power consumption.

We estimate that there are \~70 mn traditional servers in the global installed base, with an average life of 5.7 years. We estimate the server installed base by assuming an average life for each server in each year (based on Lawrence Berkeley National Lab estimates) and then summing the server shipments for the corresponding number of years prior. Our server shipments estimates are based on a blended average of IDC, 650 Group, and Gartner traditional server forecast (i.e. non accelerated).

We estimate that average life of servers has been extended from 4.4 years (2003-2019) to 5.7 years today, driven by (1) hyperscalers extending the useful life/depreciation for their servers from 3 years to 5-6 years over the last few years, citing efficiency gains from improved processes and maintenance; and (2) enterprises running their equipment “hot” (i.e., at higher than desirable utilization rates) in a time of increased IT budget pressure from an uncertain macro environment & competing demands (i.e., AI). As a result, we estimate that 32% of the global server installed base in 5+ years old as of 2025, up meaningfully from 8% a decade ago. Note that this portion of the installed base (2019-2020) was put into data centers prior to many of the requirements for AI-infrastructure, which requires significantly more power that traditional servers. DELL reported on their F1Q27 (3 months ending April 30, 2026) earnings that the majority of their installed base of traditional servers were 14th generation, which was first introduced in 2017, or older.

Exhibit 9: We estimate that there are \~70 mn traditional servers in the global installed base, with an average life of 5.7 years.

Global traditional server installed base (units, mn) and average usable life assumption (years)

![](images/66323cbad1257ea9fecace2d658d93948f1b4113bb89eeaea3f6da99731e1df7.jpg)  
Source: GS Global Investment Research, Lawrence Berkeley National Lab  
Exhibit 10: We estimate that 32% of the global server installed base is 5+ years old as of 2025, up meaningfully from 8% a decade ago...  
Global server installed by age (units, mn) and % of servers aged 5 years and older

![](images/c3017979cd28d8acf7afcf00925568b4edc08799c3d51da009f604ba997db053.jpg)  
Source: GS Global Investment Research, Lawrence Berkeley National Lab

Exhibit 11: ... driven in large part by extended useful lives of servers at major hyperscalers
Useful life of servers (for accounting/depreciation purposes) at major US hyperscalers  
![](images/d15bfabf8f65af91c8992a8342359acb9a2e8a682dbf2b8a7db2e4bdbbfc47ea.jpg)  
Source: Company data, GS Global Investment Research

We expect traditional server shipments should normalize to \~10 million units annually (v. 13 mn average in 2018-22) as (1) refresh to newer systems increase efficiency (i.e., densification) and (2) agentic AI drives demand drives expanded server estates.

How will server consolidation impact the installed base over the long term? HPE has reported that a single Gen12 server can replace 7 Gen11 servers or 14 Gen10 servers while reducing power by 65%. DELL has reported that its 17G consolidates old servers at a 3:1 ratio (15G) or 7:1 ratio (14G), with over 70% of its installed base is still running on 14G servers or older (as of November 2025). In a simplified scenario analysis where all legacy servers are replaced with next-gen, assuming a 3:1 or 6:1 replacement rate on 14G older servers, Dell could shrink its server installed base by up to 60%. We note that this does not account for any growth in workloads, which would necessitate incremental compute capacity being brought online (a partial offset to this consolidation headwind). That said, the consolidation of traditional servers today may lead to a structurally smaller installed base of servers in the medium term, which could limit potential upside in future refresh cycles. If significantly fewer server units ship each year, ASPs & profit margins need to be up significantly to maintain a stable profit pool.

Exhibit 12: DELL has reported that its 17G converts old 14G servers at a 6:1 ratio
Illustrative comparison of 14G and 17G Dell servers specs

<table><tr><td></td><td>PowerEdge R540</td><td>PowerEdge R470</td><td>17G v. 14G</td></tr><tr><td>Generation</td><td>14th Generation</td><td>17th Generation</td><td></td></tr><tr><td>Year Released</td><td>2017</td><td>2024</td><td></td></tr><tr><td>Form Factor</td><td>1U</td><td>1U</td><td></td></tr><tr><td>Processor</td><td>Intel Xeon Silver</td><td>Intel Xeon 6 E</td><td></td></tr><tr><td># of Cores</td><td>8</td><td>64</td><td>8X</td></tr><tr><td>Memory</td><td>16 GB DDR4</td><td>32 GB DDR5</td><td>2X</td></tr><tr><td>Storage</td><td>2 TB SATA HDD</td><td>960 GB SSD</td><td></td></tr><tr><td>Input Power</td><td>143 watts</td><td>316 watts</td><td>2X</td></tr><tr><td>Starting Price</td><td>$4,677</td><td>$10,000</td><td>2.1X</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 13: Assuming a 3:1 or 7:1 replacement rate on 14G older servers, Dell could shrink its server installed base by up to 60% in our illustrative scenario analysis
Dell traditional server installed base scenario analysis  
![](images/1ca15a39bf2da5a635c87d23843067bae4625b9669eab1905479f578d61316c4.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 14: If significantly fewer server units ship each year, ASPs & profit margins need to be up significantly to maintain a stable profit pool
Industry traditional server installed based scenario analysis

<table><tr><td></td><td>Current industry(2020-25 avg)</td><td>3:1 replacement ratio</td><td>7:1 replacement ratio</td></tr><tr><td>Annual unit shipments (mn)</td><td>11.9</td><td>4.0</td><td>1.7</td></tr><tr><td></td><td></td><td>Assume 3:1</td><td>Assume 7:1</td></tr><tr><td>ASPs ($)</td><td>$8,036</td><td>$14,063</td><td>$20,090</td></tr><tr><td></td><td></td><td>Assume +75%</td><td>Assume 150%</td></tr><tr><td>Total Industry Value ($, bn)</td><td>$96</td><td>$56</td><td>$34</td></tr><tr><td>EBIT margins (GSe)</td><td>7%</td><td>12%</td><td>20%</td></tr><tr><td></td><td>GS estimate</td><td colspan="2">Implied if profit pool unchanged</td></tr><tr><td>Industry profit pool</td><td>$6.7</td><td>$6.7</td><td>$6.7</td></tr></table>

Source: GS Global Investment Research, IDC, Company data

What is the role of traditional servers in AI deployments? While GPU servers represent the majority of net-new AI infrastructure spend to date, traditional CPU also play a critical role in AI deployments. First, in massive GPU clusters designed for AI training, CPU servers serve as the head nodes/orchestration layers. While GPUs handle the heavy lifting of parallel processing required for model training (i.e., worker nodes), CPU servers manage the cluster, schedule jobs, route data, and monitor resource allocation. Without traditional servers orchestrating the workflow, the high-performance GPUs would be unable to function efficiently, making CPU infrastructure a key component of any training cluster. Second, agentic AI requires a hybrid approach that blends the probabilistic reasoning of GPUs (statistical pattern recognition and generating tokens) with the deterministic execution of CPUs (rule-based logic, API tool calls, and strict workflow orchestration). Because agentic workflows are heavily tool-dominated and require constant, predictable orchestration, CPUs are better suited to handle these deterministic tasks to prevent latency bottlenecks. This architectural shift will have an impact on hardware configurations; wh

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
