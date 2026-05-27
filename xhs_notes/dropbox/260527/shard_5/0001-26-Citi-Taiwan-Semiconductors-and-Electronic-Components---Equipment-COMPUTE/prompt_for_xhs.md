你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：约 850 字，允许上下浮动 15%。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
26 May 2026 01:00:45 ET | 12 pages

# Taiwan Semiconductors and Electronic Components & Equipment

COMPUTEX and GTC Taipei preview: From GPU Racks to AI Factories

# CITI'S TAKE

COMPUTEX 2026 is likely to mark a major shift in the AI infrastructure narrative. In the previous cycle, investor attention was concentrated on GPUs, HBM, CoWoS capacity, and Blackwell rack shipments. This year, the center of gravity is moving broader: NVIDIA is expected to emphasize not only Rubin GPUs, but also Vera CPUs, Spectrum-X networking, CMX context memory, CPO, liquid cooling, and high-voltage power architecture. The key message is that AI infrastructure is no longer just a GPU cluster. Other than Nvidia's supply chain, we expect to see more on CPU orchestration, Ethernet AI fabrics and CPO, liquid cooling and 800V DC power, BMC telemetry..etc. Computex is likely to become a full AI factory event, where CPU orchestration, GPU acceleration, memory hierarchy, networking bandwidth, cooling, and power delivery are jointly optimized.

Various rack configuration demonstration — Based on NVIDIA previous announcement during GTC in March, it appears to be defining several rack categories: GPU racks, Vera CPU racks, LPU racks, CMX context-memory racks, Spectrum networking racks, power racks, and cooling/liquid distribution infrastructure (see our report on GTC implications in Mar). This is no longer a conventional server deployment model. It is a composable AI factory model. We expect to see various different rack solutions from major ODMs including Hon Hai, Quanta, Wistron/Wiwynn, etc.

GPU rack remains the compute anchor. CPU and LPU rack to show up — Rubin NVL72 and Rubin Ultra NVL144/NVL576 extend the same logic following the GB system, but at far higher power density and network complexity. Vera Rubin Ultra NVL576 combines eight separate MGX NVL racks, each with 72 Rubin Ultra GPUs, into one 576-GPU NVLink domain using copper and direct optical connections. This suggests that the “rack” is becoming only one module inside a larger pod-scale compute domain. On CPU, we believe Vera CPU could become one of COMPUTEX 2026’s key highlights, with expected Vera CPU production preparation of about 2m units in 2026. We expect Hon Hai and Quanta to demonstrate their Vera Rack/system during Computex.

CPO, Power and Cooling Are the Next Constraints — Spectrum-X and CPO highlight that data movement is becoming as important as compute. Optical engines, FAUs, silicon photonics, switches and fiber management have become more strategic. At the same time, rack power may rise from 40–60kW in Hopper to 180–220kW+ in Rubin, pushing 800V DC, power shelves and liquid cooling adoption. We expect Hon Hai and Quanta to demonstrate their SPX rack and system and Delta to demonstrate their power solution.

Positive on Taiwan technology supply chain — Beyond TSMC and CoWoS, the opportunity increasingly includes ABF substrates, sockets, thermal modules, power shelves, busbars, optical assembly, BMC controllers, and rack integration. We believe the most important COMPUTEX 2026 message is that AI infrastructure is entering into a new system-design phase.

Laura (Chia Yi) Chen $^{AC}$

+886-2-8726-9090

laura.cy.chen@citi.com

Jack Chen

+886-2-8726-9091

jack1.chen@citi.com

Michael Hung

+886-2-8726-9092

michael.hung@citi.com

Nicholas Lai

+886-2-8726-9093

nicholas.lai@citi.com

# From GPU Racks to AI Factories

Computex 2026 will kick off on June 1 $^{st}$ next week. The keynote lineup starting from Nvidia, Qualcomm, Marvell, Intel and NXP represent four different layers of the AI buildout: edge AI, connectivity, compute platforms and industrial/automotive intelligence. We see AI performance is increasingly constrained not only by accelerator supply, but also by networking, optical interconnect, custom silicon and system-level bandwidth. COMPUTEX should confirm that the next AI cycle is moving from “more GPUs” to “better infrastructure”. Meanwhile, NVIDIA’s separate GTC Taipei presence at COMPUTEX will likely remain the main sentiment driver, as Jensen Huang’s keynote is positioned around the future of AI and new technology. The key implication is that Taiwan’s supply chain will be judged less by single-component exposure and more by its ability to deliver complete AI systems: racks, power, thermal, networking, PCB/substrate, advanced packaging, testing and manufacturing scale.

# Rack Configurations: From NVL72 to Modular AI Factory Blocks

The most important architectural transition is that NVIDIA is moving from server-level design to rack-level and eventually pod-level design. Blackwell GB200 NVL72 was the first major step in this direction, turning the rack itself into the system boundary. Rubin takes this much further. Based on NVIDIA previous announcement during GTC in March, it appears to be defining several rack categories: GPU racks, Vera CPU racks, LPU racks, CMX context-memory racks, Spectrum networking racks, power racks, and cooling/liquid distribution infrastructure. (see our report on GTC implications in Mar). This is no longer a conventional server deployment model. It is a composable AI factory model.

The GPU rack remains the compute anchor. Blackwell NVL72 combines 72 GPUs into a rack-scale NVLink domain, with direct liquid cooling and rack-level power delivery. Rubin NVL72 and Rubin Ultra NVL144/NVL576 extend the same logic, but at far higher power density and network complexity. NVIDIA's official developer blog states that Vera Rubin Ultra NVL576 combines eight separate MGX NVL racks, each with 72 Rubin Ultra GPUs, into one 576-GPU NVLink domain using copper and direct optical connections. This suggests that the "rack" is becoming only one module inside a larger pod-scale compute domain. We expect ODMs including Hon Hai, Quanta, Wistron/Wiwynn, Asustek, Inventec and Pegatron to demonstrate VR NVL72 during Computex.

Figure 1. Key highlights of Nvidia's AI demonstration during Computex 

<table><tr><td>Rack Type</td><td>Main Role</td><td>Key Components</td><td>Strategic Meaning</td></tr><tr><td>Rubin GPU rack</td><td>Main AI acceleration</td><td>GPUs, NVLink, HBM, liquid cooling</td><td>Defines rack-scale compute density</td></tr><tr><td>Vera CPU rack</td><td>Agentic AI orchestration</td><td>Vera CPUs, SOCAMM, NICs, BMC</td><td>Raises CPU content and memory bandwidth needs</td></tr><tr><td>Spectrum networking rack</td><td>Scale-out AI fabric</td><td>Spectrum-X / Spectrum-6 switches</td><td>Connects GPU, CPU, and CMX domains</td></tr><tr><td>Power rack</td><td>High-density power delivery</td><td>Power shelves, busbars, BBU</td><td>Supports 200kW–600kW rack class</td></tr><tr><td>Cooling system / CDU</td><td>Thermal infrastructure</td><td>CDU, manifolds, QDs, sensors</td><td>Enables full liquid AI factory deployment</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi

# CPU Strategy: Vera Is Not a Traditional Server CPU

Vera CPU may be one of the most important COMPUTEX themes. NVIDIA's CPU strategy does not appear to simply take on Intel and AMD in the general-purpose server market. Instead, Vera is designed to control the AI factory orchestration layer. Vera positions as optimized for high single-threaded performance and energy efficiency to complement NVIDIA GPUs, rather than as a broad general CPU lineup.

In agentic AI, the CPU workload is not just feeding GPUs. It includes request scheduling, agent workflow control, tool-call coordination, memory indexing, retrieval management, simulation, networking control, and system telemetry. The CPU becomes the “traffic controller” for AI factories. As inference workloads become longer and more persistent, CPU-side memory bandwidth and capacity also matter more. It is also important to note that SOCAMM design is important for Vera as SOCAMM gives Vera a denser, lower-power, high-bandwidth memory architecture, likely better suited for AI orchestration than conventional DIMM-heavy server designs. And with AI inference becoming more agentic and CPU-intensive, CPU demand expands alongside GPU demand instead of being cannibalized by acceleration.

During Nvidia's latest earnings call, the CEO Jensen Huang reaffirmed NVIDIA's expectation for a roughly US\$200bn CPU market opportunity, with Vera CPU positioned as part of NVIDIA's broader AI infrastructure push. We believe Vera CPU could become one of COMPUTEX 2026's key highlights, with expected Vera CPU production preparation of about 2m units in 2026. We expect Hon Hai and Quanta to demonstrate their Vera Rack/system during Computex.

# Networking and CPO: Spectrum-X Becomes the AI Fabric Layer

Networking will be another major COMPUTEX focus. As AI systems scale from single racks to pods, the bottleneck shifts from chip compute to data movement. We note that hyperscalers prefer Ethernet economics and operational familiarity, but AI requires much tighter congestion control, telemetry, routing, and workload-aware optimization. NVIDIA's Spectrum-X roadmap points toward Ethernet

becoming a specialized AI fabric rather than a generic datacenter network. We would expect ODMs including Hon Hai/Foxconn and Quanta to demonstrate its SPX rack solution and switch.

CPO will likely be one of the most debated COMPUTEX topics. NVIDIA has already positioned Spectrum-X Ethernet Photonics and Quantum-X Photonics as part of its AI factory networking roadmap. For Rubin Ultra, CPO becomes more important because the physical scale of NVL576 exceeds what copper can handle efficiently. NVIDIA's developer blog supports the idea that NVL576 uses copper and direct optical connections across eight racks. Therefore, the practical adoption curve is likely: pluggable optics and LPO/NPO in 2025–2026, switch-side CPO and direct optical links in 2026–2027, and broader optical scale-up fabrics after Rubin Ultra.

With more CPO penetration into the next 2 years, optical engines, silicon photonics PICs, FAUs, active alignment equipment, optical connectors, fiber management, and liquid-compatible photonic packaging all become more important. However, we believe that FAU and OE should not be treated as mechanically always one-to-one. One optical engine usually requires a fiber attach interface, but mapping depends on Tx/Rx layout, lane count, WDM architecture, and whether fibers are shared, split, or aggregated.

# Cooling and Power: The AI Rack Becomes an Electrical-Thermal System

Cooling and power may become the most practical bottlenecks for Rubin deployment. Rubin NVL8 server references around 24kW TDP and over 32kW TDP at the 2U system level, while Rubin NVL72 rack estimates would be roughly 180kW rack TDP to 220kW rack TDP. Recall that Hopper racks could often operate around 40–60kW with air or hybrid cooling. Blackwell NVL72 pushes into 120–180kW, making direct liquid cooling standard. Rubin pushes rack power toward 200kW and beyond, while Rubin Ultra may move toward several hundred kilowatts.

Power delivery is also shifting. At 54V, a 216kW rack implies around 4,000A current, which becomes difficult in copper, busbars, connectors, and thermal management. This explains why NVIDIA will be pushing 800V DC, power racks, 110kW power shelves, BBU support, and DC datacenter architecture. The future rack is not just a server cabinet. It is an electrical-thermal machine requiring coordinated power conversion, backup energy, liquid flow, telemetry, and safety systems. We would expect to see more of the power and thermal solutions from Delta, AVC and Auras.

Figure 2. Power and cooling structure comparison for different generation 

<table><tr><td>Generation</td><td>Approx. Rack Power Direction</td><td>Cooling Method</td><td>Power Architecture</td></tr><tr><td>Hopper</td><td>40–60kW</td><td>Air / partial liquid</td><td>Traditional AC PSU</td></tr><tr><td>Blackwell GB200</td><td>120–140kW</td><td>Direct liquid cooling</td><td>Rack power shelves / busbar emerging</td></tr><tr><td>GB300 / Blackwell Ultra</td><td>140–180kW</td><td>Full rack liquid cooling</td><td>Higher-density power shelves</td></tr><tr><td>Rubin NVL72</td><td>180–220kW+</td><td>Advanced rack liquid cooling</td><td>54V busbar near practical limits</td></tr><tr><td>Rubin Ultra</td><td>300–600kW potential</td><td>Pod/facility liquid loop</td><td>800V DC transition increasingly necessary</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

# Appendix A-1

# ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

# IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution 

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Apr 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>8%</td><td>37%</td><td>47%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>41%</td><td>28%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

# Guide t

[中间内容因长度限制已省略]

rd Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a

subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
