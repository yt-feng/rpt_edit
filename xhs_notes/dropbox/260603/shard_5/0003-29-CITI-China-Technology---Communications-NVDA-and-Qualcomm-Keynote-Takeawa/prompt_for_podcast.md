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
# China Technology & Communications

NVDA and Qualcomm Keynote Takeaways

## CITI'S TAKE

NVDA CEO Jensen Huang delivered a GTC keynote today where he noted: (1) Vera Rubin has reached full commercial production, seemingly confirming the 2H26 ramp for the NVDA supply chain (FII, VGT, WUS). (2) NVDA has evolved from being a GPU-focused system company into a full-stack AI infrastructure company, which may extend its partnerships to power/cooling supply chains including Chinese players. (3) With the introduction of the Vera CPU specifically for the "Agentic AI" era and reinforcement learning, we see positive implications for Lenovo, which is also one of ecosystem partners set to benefit from the new GPU server platform and Nvidia Windows-based laptops with higher ASPs. We also watch for the long-term potential demand impact to Montage's memory interface chips given Nvidia's shift toward SOCAMM/LPDDR5. (4) Qualcomm's new data center portfolio Dragonfly may provide an additional source to China ASIC datacenter solutions.

Key highlights from Nvidia GTC keynote — (1) Software should be presented as an agent; tokens are for revenue/profit generation. We see many Chinese software/ICT companies migrating to agent's provider and token-based business model. (2) Vera Rubin has reached full commercial production, which likely confirms the 2H26 ramp for the NVDA supply chain (FII, VGT, WUS); TFC was highlighted twice in the video presentation. (3) Nvidia is now a full-stack AI infrastructure company and implied it would expand its supply chain control beyond L10 to include L11 (rack) and L12 (cluster). (4) All about CPU—Nvidia sees Vera CPU as the next growth driver not only for its data center business but also edge devices with the launch of the RTX Spark laptop and new lines of PCs. (5) Agentic AI and Physical AI—The company highlighted autonomous driving and industrial and humanoid robotics.

Key highlights from Qualcomm Computex keynote — (1) Qualcomm launched Dragonfly, its new product brand dedicated to data center environments. (2) Snapdragon platforms are evolving into native execution layers for third-party AI agents. (3) Qualcomm is extending edge silicon into high-growth mobility and industrial automation frameworks like vehicles, robotics, and 6G wireless.

Implications — Vera Rubin has reached full commercial production, which should be positive to the NVDA supply chain, i.e., FII, VGT, WUS on 2H26 ramp. We also see positive implications to Lenovo, which is also an ecosystem partner set to benefit from the new GPU server platform and the Nvidia Windows-based laptop with higher ASP contribution. That said, we watch for the long-term potential demand impact to Montage's memory interface chips given that Nvidia's Vera CPU and Spark platform adopt the SOCAMM/LPDDR5X memory architecture instead of RDIMM and hence could erode DIMM chip opportunities should Nvidia CPU claim a larger share of server processors. We believe Qualcomm's new datacenter portfolio Dragonfly could provide an additional source to China ASIC datacenter solutions. NVIDIA's and Qualcomm's keynotes both signal that the industry has transitioned from the foundational LLM paradigm—characterized by static prompt-and-response interactions—into the agentic AI and physical AI era, suggesting a potentially faster-than-expected pace of AI edge proliferation in China.

## Kyna Wong $^{AC}$

+852-2868-7820

kyna.wong@citi.com

## Kevin Chen

+852-2501-2125

kevin.y.chen@citi.com

## Karen Huang

+852-2501-2755

karen.xw.huang@citi.com

## Key takeaways from Nvidia and Qualcomm keynote speeches

From standalone GPU acceleration toward engineering of integrated and pod-scale systems — Nvidia emphasized that it is a full-stack AI infrastructure company. The centerpiece of its next-generation AI infrastructure is the Vera Rubin platform, a multi-rack supercomputing system that has reached full commercial production. Built on an advanced 3nm process, the platform integrates seven specialized chips. The system utilizes next-generation HBM4 memory architectures to overcome memory bandwidth bottlenecks. Large scale-out and scale-up capabilities are driven by the unified integration of NVLink 72, CX9 SuperNICs, and Bluefield-4 DPUs. To sustain operational power requirements exceeding 5,000 amps, the Rubin architecture implements advanced 45°C liquid cooling loops. It also features a cable-less midplane design, removing physical connectivity failure points and increasing systemic resiliency. The Nvidia Vera Rubin DSX AI Factory reference design outlines how to design, build, and operate the entire AI factory infrastructure stack including NVL rack, Vera GPU rack, spectrum-6 SPX switch, Groq 3 LPX rack, and Vera BlueField-4 STX storage rack.

NVDA's first host processor Vera CPU designed specifically for autonomous AI workloads — Built on the Olympus Core, the Vera CPU achieves the industry's highest instructions per clock (IPC), capable of decoding 10 instructions per cycle. It is the first enterprise CPU to adopt LPDDR5 memory to deliver an ultra-wide 1.2TB/s of memory bandwidth. The chip features an 88-core monolithic mesh topology. By avoiding a modular chiplet architecture, it eliminates inter-die communication delays. Real-world architectural benchmarks indicate that the Vera CPU runs 3x faster in complex SQL database tasks and 6x faster in real-time data stream processing compared to x86 counterparts, removing the primary bottlenecks in agentic tool-calling pipelines.

RTX Spark platform to bring agentic capabilities directly to local workstations and laptops — NVIDIA, in collaboration with Microsoft, introduced the RTX Spark platform. These Windows-compatible, CUDA-enabled machines feature the N1X chip (co-developed with MediaTek), combining a Blackwell-architecture RTX GPU containing over 6,000 cores with a 20-core Grace CPU. Delivering 1 petaflop of localized AI compute performance and 128GB of unified memory, this platform enables complex, multi-modal autonomous agents to execute natively on end-user devices without relying on constant cloud connectivity.

Qualcomm Dragonfly for Data Center Portfolio Expansion — To establish a continuous computing pipeline from consumer devices to backend infrastructure, Qualcomm launched Dragonfly, its new product brand dedicated to data center environments. This portfolio expansion allows Qualcomm to offer a seamless compute continuum, matching high-performance cloud processing with low-power edge devices under a unified architecture. More detail will be unveiled on 24 June.

Snapdragon platforms evolving into native execution layers for third-party AI agents — AI orchestration frameworks like Open Claw and Hermes run directly on Snapdragon silicon, while applications like Claude Desktop operate natively on Snapdragon-powered PCs. Google is embedding Gemini Intelligence natively into the Android stack on Snapdragon hardware, mirrored by Microsoft's integration of core agentic features into Windows on Snapdragon. Simultaneously, hardware partners like Humain are deploying complete generative operating systems built from the ground up for Snapdragon architectures.

Qualcomm extending edge silicon into high-growth mobility and industrial automation frameworks – (1) AI-Defined Vehicles—The automotive platform separates vehicular intelligence into two distinct layers: an adaptive, personalized agent inside the digital cockpit, and a dedicated physical AI system processing radar and camera inputs for real-time autonomous path planning. (2) Robotics Platforms—A comprehensive computing platform tailored for Autonomous Mobile Robots (AMRs), industrial arms, humanoids, and drones. It features a hierarchical compute model that segregates low-latency operations (e.g., balancing and grip adjustments) from high-level reasoning and action grounding. (3) 6G Wireless as an AI Catalyst—Qualcomm views upcoming 6G standards as a network

architecture built fundamentally for AI. The framework relies on high-definition video uplinks for wearable devices, distributed computing nodes embedded directly into cellular infrastructure, and RF signal processing used as physical AI input to construct real-time digital twins of physical environments.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Apr 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>8%</td><td>37%</td><td>47%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>41%</td><td>28%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign “Rating Suspended” status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned “Under Review” status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

## Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day period. The Catalyst Watch will also be automatically removed if share price performance (calculated at market close) exceeds 15% against the direction of the call (unless over-ridden by the analyst). The analyst may also remove a Catalyst Watch or STV call prior to the end of the specified period in a published research note. A Catalyst Watch/STV Upside or Downside call may be different from and does not affect a stock's fundamental equity rating, which reflects a longer-term total absolute return expectation. For purposes of FINRA ratings-distribution-disclosure rules, a Catalyst Watch/STV Upside call corresponds to a buy recommendation and a Catalyst Watch/STV Downside call corresponds to a sell recommendation. Any stock not assigned to a Catalyst Watch Upside, Catalyst Watch Downside, STV Upside, or STV Downside call is considered Catalyst Watch/STV No View. For purposes of FINRA ratings distribution-disclosure rules, we correspond Catalyst Watch/STV No View to Hold in our ratings distribution table for our Catalyst Watch/STV Upside/Downside rating system. However, we reiterate that we do not consider No View to be a recommendation. For all Catalyst Watch/STV Upside/Downside calls, risk exists that the catalyst(s) and associated share-price movement will not materialize as expected.

## RESEARCH ANALYST AFFILIATIONS / NON-US RESEARCH ANALYST DISCLOSURES

The legal entities employing the authors of this report are listed below (and their regulators are listed further herein). Non-US research analysts who have prepared this report (i.e., all research analysts listed below other than those identified as employed by Citi Global Markets Inc.) are not registered/qualified as research analysts with FINRA. Such research analysts may not be associated persons of the member organization (but are employed by an affiliate of the member organization) and therefore may not be subject to the FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Citi Global Markets Asia Limited

Karen Huang; Kevin Chen; Kyna Wong

## OTHER DISCLOSURES

Any price(s) of instruments mentioned in recommendations are as of the prior day's market close on the primary market for the instrument, unless otherwise stated.

The completion and

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
