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

<table><tr><td></td><td>PowerEdge R540</td><td>PowerEdge R470</td><td>17G v. 14G</td></tr><tr><td>Generation</td><td>14th Generation</td><td>17th Generation</td><td></td></tr><tr><td>Year Released</td><td>2017</td><td>2024</td><td></td></tr><tr><td>Form Factor</td><td>1U</td><td>1U</td><td></td></tr><tr><td>Processor</td><td>Intel Xeon Silver</td><td>Intel Xeon 6 E</td><td></td></tr><tr><td># of Cores</td><td>8</td><td>64</td><td>8X</td></tr><tr><td>Memory</td><td>16 GB DDR4</td><td>32 GB DDR5</td><td>2X</td></tr><tr><td>Storage</td><td>2 TB SATA HDD</td><td>960 GB SSD</td><td></td></tr><tr><td>Input Power</td><td>143 watts</td><td>316 watts</td><td>2X</

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
