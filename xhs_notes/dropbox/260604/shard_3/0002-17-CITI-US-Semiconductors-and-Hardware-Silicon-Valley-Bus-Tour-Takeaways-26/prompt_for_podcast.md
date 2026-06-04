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
02 Jun 2026 11:16:54 ET | 13 pages

# US Semiconductors and Hardware

Silicon Valley Bus Tour Takeaways

# CITI'S TAKE

We hosted investor meetings with AMD, AMAT, ALAB, NVMI, STX, WDC, and SMCI as part of Citi's annual Silicon Valley bus tour yesterday. Please see detailed notes inside.

# Atif Malik $^{AC}$

+1-415-951-1892

atif.malik@citi.com

# Asiya Merchant, CFA

+1-415-951-1752

asiya.merchant@citi.com

James Bowlin

+1-415-951-1790

james.bowlin@citi.com

Michael Cadiz

+1-415-951-1671

michael.cadiz@citi.com

# Silicon Valley Bus Tour Notes AMD

Jean Hu, CFO & Treasurer | Matt Ramsay, CVP Financial Strategy & IR | Prabh Gowrisankaran, Director, IR

■ Server growth. Inflection of Agentic AI and rise of CPU demand was noticeable last year. AMD articulated the 3 segments of server CPUs at investor day last November and was preparing for a significant ramp. Now AMD is seeing an explosion of demand and is working to expand supply. AMD grew server revenue >50% in Q1. TSMC 3nm has long lead times, but they feel good about 2026 and 2027. They are seeing enterprises adopting agentic AI. AMD is seeing the industry shift towards inference and the shift from chatbot inference towards agentic inference. AMD believes their agentic share could exceed their general server CPU share.

ARM vs X86 debate. AMD wants to build the best server platform for different applications and workloads. Turin has a breadth of 8 cores to 192 cores to support different workloads. General purpose CPU, AI head nodes, and Agentic all have different requirements. Agentic AI is multiple workloads, orchestration, data base retrieval, agent management and more. AMD's investments for more than a decade allows them to address all these workloads. AMD is in every workload for servers besides NVL head nodes. Venice CPU is the head node for Helios. AMD believes Venice will be a leadership performance product and Venice will have Verano to compete with ARM CPUs. Verano was closely designed with Meta. X86 security features are strong compared to ARMs.

\- Pricing power. AMD wants to be strategic to manage long-term relationships with customers in the future. They will share memory cost increases with customers. They have good gross margins in servers. 70% to 75% of AMD server growth would predict to be from units. ASP expansion will come from a greater mix of Turin, and higher core count products. Mandate from AMD management isn't on pushing on X86, it's about building the best CPU and having SKUs to target the whole market.

■ Software. Largest AI frontier companies are using NVDA, AMD, and different ASICs. AMD is seeing Claude code internally to shorten software deployments. AMD believes the CUDA moat will get diminished given the velocity of software. On the CPU side, its more about the architecture of the platform.

■ Agentic adoption spiked in February. Model capability increased, and agentic adoption increased when they saw the capability increase. By January of this year, all major hyperscale companies significantly increased their demand on the CPU side. Agentic is happening much faster than AMD expected. Orchestration and execution are all driven by CPUs. 95% of AMD token spending is for software engineering. If AMD believes their customers bottom-up forecast, their \$120bn TAM estimate is too low.

Intel competition. Diamond Rapids doesn't have multithreading and ARM AGI does not have multithreading. AMD's enterprise share shift accelerated rapidly in 1Q and one thesis is because customers know Intel doesn't have 8 channel.

■ Networking. AMD feels good where they are at as they will rely on partners for scale across. Infinity Fabric will be used for scale up. AMD donated UAL to the industry body. Astera and Marvell will be building ethernet switching technology with AMD. Copper and Optics will coexist for a few generations.

\- AI-driven PC Refresh. AMD isn't seeing signs yet, but there are different types of tokens that need to be optimized. You can in theory lower your enterprise token budget by running them on a notebook.

# AMAT

Prabu Raja, PhD, President, Semiconductor Products Group

■ DRAM/HBM growth. AMAT continues to see strong demand for DRAM. They did see some absorption of HBM last year and now its opening up. Systems will grow >30% this year, NAND/DRAM leading edge will be growing faster than that.   
■ Cyclicality. PC/Phones people bought every two years in a cycle. Now demand is not following a cycle. The number of steps are growing for logic and DRAM.   
■ Industry dynamics. AMAT has been talking about inflections for some time. Logic is going to GAA and Backside Power. CPUs to GPUs connects a lot more transistors and connects a lot more wiring layers. DRAM is really following the Logic roadmap. Chips are a lot more complex. Wiring has CVD, PVD, and CMP. CPU chip goes from 17 layers to 21 layers for GPU.   
■ Advanced packaging. AMAT started investing more than 10 years back. Bonding is the next inflection, and wafer level panel. AMAT is not strong in plating and that is an opportunity for AMAT. Moreover, display business is synergistic with panels.   
- Terafab. AMAT can't talk about specific customers. There is broadening of demand that is good for the industry. AMAT has doubled its manufacturing footprint, Singapore has a lot of space to fill tools. Scaling AMAT's manufacturing is very doable in this environment.   
■ Lead times. The biggest focus is supply chain readiness. The other area of focus is tool startup, is AMAT hiring people early enough and are they trained well enough. AMAT can increase their manufacturing capacity easily right now.   
■ ICAPs. They are seeing this market improve. ICAPs should grow mid to high single digits long term, but they see more growth in direct AI data center.   
NAND capacity increase timing. Customers are spending on NAND and NAND will grow this year off a lower base. Demand is good, customers do buy technology upgrades today. NAND fabs were converted to DRAM. AMAT doesn't see new NAND fabs coming up right now, but they believe it will happen.

# ALAB

Des Lynch, CFO | Mike Tate, Strategic Advisor

■ ALAB primer. The company solves connectivity. They cited a 2030 opportunity of \$25 billion. The largest opportunity is switching and their Scorpio P-Series (scale out) and X-Series (scale up) which is a 10 billion opportunity. They expect Scorpio will be largest product family by end of the year. One of key products was the retimer family under Gen 5, now they are transitioning to gen 6, typically moving from one generation gives you 25-30% ASP benefit. AEC is 10-15% of sales, and the company has grown their 200G and 400G solutions, and they see a transition to 800G occurring later this year. CXL is also having growing interest with KV Kache, more of a 2027/2028 impact for the model.

■ NVDA PCIE Gen 6. Moving to Gen 6 is favorable for ALAB as they are shipping in volume for this technology. Nvidia uses a proprietary scale up technology, and they use Scorpio for scale out.   
■ CXL. \$4 billion opportunity by 2030, the company is encouraged by recent engagements, but AI has pushed some of this right. CXL is used by general purpose servers, it enables an expansion of memory.   
■ Scorpio P and X engagements. Scorpio P is driven by ALAB's lead customer, they expect to see two hyperscalers convert to revenue later this year and into next year. Scorpio X has 10 engagements across hyperscalers and AI platform providers. They expect to convert some of these into design wins and revenue.   
■ Content. Aries less than \$100 per XPU, Aries plus a few hundred dollars, w/Scorpio P \$500, and w/Scorpio X over \$1000 per XPU. Dollar content continues to grow and content varies on customers: Google has a proprietary technology and NVDA has their own.   
■ Photonics. Rack to rack connectivity will be first to use optics. 2027 will use NPO and NPO will be dominate in 2028. May see CPO in 2028 depending on how it works. Next generation of XPUs will be optical, CPO won’t be primetime yet. People want to stay on copper as long as possible.   
■ ALAB growth drivers. Customer position will drive a lot of growth. ALAB is engaged with all the hyperscalers, and merchant GPU providers like AMD/NVDA. Volumes are more material when you do scale out and scale up. They see continued growth beyond just Amazon.   
■ \$10 billion Scale Up. This was a bottom-up exercise to come up with the \$10 billion estimate. Amazon and AMD are the two main endorsers of UAL.   
■ Market Share. Historically had 90% share in retimers, only loss is from China. In Gen 6, AVGO announced theirs, but ALAB hasn't seen them shipping or MRVL. 1/3rd of ALAB revenue in Q1 was retimers and they feel like they have a good lead. On switching, this will be a competitive environment. On AEC, Credo has larger market share today. MRVL is also making a play in AEC ethernet as well.   
■ M&A. ALAB will continue to look to enhance their portfolio, they did some smaller acquisitions and one at the end of last year. They look to do these acqui-hires as well.   
■ Automotive opportunity. Auto has been very tempting for ALAB, there is a lot of opportunity in PCIE retimers, but now they are focused on AI. ALAB was close to entering this market a few times.   
■ Target Model. They want to grow faster than the market. They talked about 70% gross margins, Q1 was 76%. Some products are accretive and some are dilutive to this margin profile. They target 40% operating income. By growing faster than the market they mean growing faster than hyperscaler capex growth.   
Equity investments. Amazon has been doing this since 2014 and only with strategic partners. They signed up for \$6.5 billion which shows the revenue opportunity for ALAB. Given ALAB's balance sheet they aren't looking for investments right now.   
■ TSMC. They use TSMC in their front end. On back end they have diversified supply chains.

■ Cosmos Software. This is very differentiated software and used for two main use cases: design and fleet management software.

# NVMI

Gaby Waisman, President & CEO | Guy Kizner, CFO | Adrian Wilson, President & General Manager, Material Metrology Division

■ Key Metrics. Revenue last year was \$881M, up 31% YoY with EPS of \$8.62, up 29% YoY. The company has over 7300 active systems with over 400 customer sites. From 2020-2025 CAGR, Nova outperformed WFE growth by 96%.   
■ TCO. TCO is mostly driven by increased throughput. If a Nova tool has a 20% higher price, it needs to come with a 20-25% throughput to win in the market.   
■ Q1 Results. Nova had record revenues in Q1 driven by memory device demand for HBM and DRAM and expects strong growth in 2H26 and 2027 as well. Nova is being more conservative versus other peers because of visibility. Nova's goal is to outgrow WFE.   
■ Growth drivers. GAA is a tailwind, and backside power is one. 3D DRAM, 3D NAND, Hybrid bonding and advanced packaging are all positives for Nova. The more complicated the process, the better it is for a company like Nova.   
■ Challenges. Logic, Memory, and Packaging all have dimension, material, and chemical challenges. Nova will invest now to address the challenges down the road.   
■ Strategy. The company invests more than 15% of sales into R&D to maintain tech leadership, fund new growth engines, and path finding and incubation.   
■ Target model. Operating margin of 28-33% and EPS of \$10. Revenue of >\$1 billion with gross margins of 57-60%. The company will release a new target model when they reach their current targets.   
■ Growth rates. Advanced packaging is growing faster than front end. Nova has 100% market share in advanced packaging metrology today.   
■ Hybrid bonding opportunity. It is introducing more complexity, and the company sees market share gains moving from one architecture to another in advanced packaging and in hybrid bonding. Hybrid bonding is an inflection point and an opportunity to improve their competitive position.   
■ Services. 21% of Nova revenue is in services, within the range of 20-25%. This will fluctuate alongside with tool purchases.   
■ Memory price pressure. Memory prices are going up and is a challenge. The company will work with customers, but they see pricing going up dramatically.

# SMCI

Michael Staiger, SVP of Corporate Development | Krishna Shankar, VP Finance | Ian Tolle, Sr. Manager, IR

■ Agentic AI is seeing broad adoption and underpinning demand momentum across enterprises/sovereigns/neoclouds.

A variety of chipset offerings that can be customized to suit client needs and delivering a full stack of datacenter building block solutions (server, storage, switching with software and services attach) is a meaningful driver for SMCI's profitability.   
■ DCBBS is expected to be 15-20% of profits from low single digits and a higher mix of DCBBS should also help reduce revenue volatility.   
■ Customer diversification will occur over time though near term can be impacted by some large orders from larger customers that need to be fulfilled.   
- Demand from neoclouds has diversified beyond a handful of customers to several others internationally.   
■ Enterprises are much more focused on getting access to systems (vs focused on price) especially in certain industries like financial industries, oil and gas   
■ SMCI's vertical integration enables us to alleviate some of the supply constraints and meet customer demand.   
■ Focus is on optimizing working capital so capital raise is not a requirement to meet growth expectations.

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

# Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings ar

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a

subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
