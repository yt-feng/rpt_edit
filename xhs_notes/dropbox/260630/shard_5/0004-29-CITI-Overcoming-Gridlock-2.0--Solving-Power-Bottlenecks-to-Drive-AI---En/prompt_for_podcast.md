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
![](images/711d0988ded6cb318cc865c1716c2e8aaa70e60c83a58a676033aeedab351a5a.jpg)

# Overcoming Gridlock 2.0

# Solving Power Bottlenecks to Drive AI & Energy Security

Citi

Commodities Strategy

Anthony Yuen
Xiaodan Zhu
Maggie Lin
Maximilian Layton

Equity Research
Pierre Lau, CFA
Bella Tian
Air Ma
Andrew Kaplowitz
Vladimir Bystricky
Kyle Menges
Scott Gruber
Jack Shang
Cynthia D Wu
Vikram Bagri
Spiro Dounis

Charles Bryant
Ryan Levine
Xinru Yin
Amber Zhao
Jenny Ping
Chris McDonagh
Suraj Nebhani, CFA
Tom Wallington

Guest Contributors

Ashwani Khubani
Global Head of Power
Citi Corporate Banking

Cathy Shepherd
Global Head of Energy
Citi Corporate Banking

JP Coviello
Head of Portfolio Strategy
Chief Investment Office, Citi Wealth

Hobey Kuhn
Macro Portfolio Strategist
Chief Investment Office, Citi Wealth

June 29, 2026

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

Citi is a division of Citi Global Markets Inc. (the “Firm”), which does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the Firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Certain products (not inconsistent with the author’s published research) are available only on Citi’s portals.

![](images/986b5fafa57fdf970e095fa57914ae280c347f5e27c5ba5819d3161c760481df.jpg)

## Contents

Executive Summary 3
A conversation with Citi Banking 4
AI & Energy Security 7
Overcoming Gridlock 9
The drivers: AI and energy security 9
Complications: Not just about supplying power 12
Power infrastructure equipment: Opportunities and supply-chain bottlenecks 18
Power infrastructure equipment prospects — a focus on transformers 19
Power generation equipment: Opportunities and supply-chain bottlenecks 26
Natural gas infrastructure: Why the U.S. needs more 37
Regional power market views: U.S., Europe, China, Australia 40
Actionable ideas 51
A conversation with Citi Wealth 53

## Executive Summary

Slowly, then suddenly. Demand for power, infrastructure, and generation equipment continues to rise, driven primarily by the U.S.-focused AI data center buildout. The Middle East conflict has sharpened focus on energy security. As countries seek to reduce import dependence and limit exposure to price spikes, the reaccelerated adoption of renewables, batteries, and electric vehicles (EVs) will also raise power equipment demand. However, grid expansion appears unable to keep pace with strong demand and supply growth, constrained by equipment supply-chain challenges and well-meaning permitting frameworks in many regions. Thus, speed-to-power is driving a shift from centralized networks toward more distributed systems that bypass grid-connection delays. "Bring-your-own-generation" (BYOG), particularly U.S. natural gas-based supply, continues to gain traction. This report examines global power markets and explores solutions to ease grid constraints and accelerate AI deployment and energy security transitions.

AI is transformational and needs substantial power capex. Some caution that certain aspects of AI look like a bubble. Our stance is that power is still very much needed as the Jevons Paradox (Fortune, April 28) takes hold, and we see the related capex being utilized in the future.

Moreover, energy security is now top-of-mind for many countries. This is the top concern in the latest International Energy Agency report on Southeast Asia. Unlike imported oil and natural gas, renewable energy sources are typically domestically located. But relying on imported equipment for renewables introduces its own set of national security considerations. Expanding the share of electric vehicles (EVs), which are powered largely by domestically generated power, helps to cut oil imports. Even if AI power growth were to slow, renewables, EVs and distributed generation still require more of certain types of infrastructure equipment.

And yet, the power grids needed to facilitate the AI and energy security transformations are typically enormous and slow to improve after decades of electrification and economic growth. Speed-to-power is pushing the evolution of the grid. Our prior study, Overcoming Gridlock: Powering Our Future (May 2024), had explored solutions, but power demand growth has materialized much stronger than expected. The demand surge in power infrastructure equipment has strained supply chains and extended the wait time. Grids will still expand, but consumers of power cannot wait.

Thus, speed-to-power concerns drive demand for power generation equipment: from more efficient combined cycle gas turbines; to smaller, less efficient reciprocating engines, aeroderivative turbines and fuel cells; to the use of renewables and energy storage systems. Much of the above-listed generation equipment demanded in the U.S. requires natural gas supply, which could lead to a further boom in the U.S. midstream space.

This report draws on experts across the firm to examine this megatrend — Research (global commodities, utilities, industrials, materials and U.S. midstream), and Q&As with Banking and Wealth — for a holistic study.

## Anthony Yuen

Head of Energy Strategy
Commodities Research

# A Conversation with Citi Banking

Citi Banking personnel are not research analysts, and the information presented herein is not intended to constitute “research,” as that term is defined by applicable regulations. Unless otherwise indicated, any reference to a research report or research recommendation is not intended to represent the whole report and is not in itself considered a recommendation or research report.

![](images/d237ab7dcfece25294950f7d545896b494d318b066dcee7c616139a9ea9a3d4c.jpg)

Ashwani Khubani is Citi's Global Head of Power Corporate Banking. He is responsible for the firm's senior client relationships across the Power, Utilities, and Renewables sectors. Ashwani's counsel is focused on the defining themes shaping the global energy landscape: Energy Transition, Energy Security, Sustainability, Clean Energy, and the rapid expansion of Power for AI & Data Centers.

There is strong demand for power equipment, driven by strong growth in data center power demand and the reacceleration of renewables and electric vehicles in parts of the world, partly due to energy security needs.

What do you see as key supply-chain bottlenecks in the equipment space?

The supply chain of Transmission & Distribution and Gas Generation is most constrained. Gas Turbines are costing 2-3x what they used to cost and there is a shortage of substations/transformers and switchgear equipment.

Do you think the market underestimates the scale and duration of these supply-chain bottlenecks?

We believe the market has not understood the real issues with the supply chain and there is general ambiguity around the whole supply chain of actual backlog/delivery timelines.

With power grid improvements not necessarily keeping pace with power demand, more project developers opt for “bring your own generation” (BYOG) $^{1}$ . Yet, order books of gas turbines are very strong now that newer-generation ideas have emerged.

As OEMs have historically been cautious about adding too much capacity, are turbine and engine manufacturers and their suppliers confident in AI-driven power demand growth that justifies capacity expansion?

The demand is real, but for adding capacity the OEMs have to take a much longer view for ensuring they meet hurdle rates. As such the decision making is slower, causing buyers to focus on other sources of supply.

How are newer distributed generation ideas — say aero-derivative turbines, recip engines or others — looking like substitutes?

They are re-purposing the gensets/engines from original use in oil fields/aviation to provide behind-the-meter (BTM) solutions to data centers. $^{2}$ The use-case value is strong, but supply is limited and the solution is more nuanced and complicated.

Some data center developments are delayed or canceled. What does a typical development cycle of data centers look like and what are key aspects that affect their timing?

A typical data center build-out is two years, while the power needed for these if new generation is required could take 3-5 years, leaving a period of gap. The lack of power and complications in interconnect is pushing developers to prioritize places where interconnect and power supply has more visibility.

![](images/f1bf35e8f44656034a4b675c2fe0c43ca127531dcd5a3d6d13c50aa4c1a578cc.jpg)

Cathy Shepherd is Citi's Global Head of Energy Corporate Banking. She is responsible for strategy and capital allocation for Energy clients globally. Cathy has over 20 years of banking experience in the US and Europe with a specialty in working with our Energy and Clean Energy clients across a range of transactions including debt, equity, acquisition finance, derivatives and other credit related products.

U.S. data centers are increasingly powered by generation equipment that uses natural gas. This has implications for the outlook on gas in the U.S. and globally.

How are energy companies in the U.S. responding to the expected increase in natural gas demand to fuel AI data center growth?

The AI data center boom has become one of the biggest drivers of new electricity demand forecasts, and natural gas is expected to be a key part of the power supply to meet this demand. Energy clients are directly working with developers and hyperscalers to find locations to colocate data centers next to existing natural gas resources and infrastructure, leading to the BYOG trend. In addition, our clients are actively pursuing data center contracts, especially in key regions like Virginia, Texas, Georgia and Ohio to support additional infrastructure investment including new pipeline connections, additional compression and storage infrastructure, etc.

Is data center gas demand large enough and contracted enough to justify new pipeline infrastructure?

The industry is in the early stages of addressing this infrastructure question. If we see growth and corresponding demand rise to levels projected, it's hard to imagine a world where we will not need development of gigawatts of new gas-fired power plants and corresponding natural gas infrastructure to meet this demand. Today the focus is on quick access to markets leveraging existing infrastructure. Developers and hyperscalers are increasingly colocating data centers near existing gas resources, thereby leveraging established infrastructure. This is a key factor behind the significant project concentration in Texas, which benefits from proximity to the Permian Basin.

How much could gas for data centers be a short-term, 5-year bridge, or a longer term, 20-year baseload opportunity, or more like a backup/flexibility product?

It's really all of the above. Natural gas plays a multifaceted role in powering the data center expansion. For developers prioritizing speed, it is the essential fuel for "bridge-to-grid" projects, where on-site generation provides baseload power while awaiting grid connection. This has led to a strategy of building on-site generation near existing gas infrastructure. However, this approach is severely hampered by gas turbine backlogs of up to five years. Looking ahead, as the grid expands, natural gas will remain a cornerstone of the baseload power mix alongside nuclear and renewables, ensuring sustained demand growth across all time horizons.

Which geographical areas or shale plays are garnering the most interest?

As power availability is quickly becoming a key constraint to data center growth, developers are bypassing grid constraints by building new power generation directly where the fuel is, leading to a strategic concentration of projects in Texas, near the Permian Basin, and we're increasingly seeing demand grow in the Marcellus-Utica shale region of Pennsylvania and Ohio.

How much can gas-fired power generation serving data centers run during more extreme weather situations, such as cold weather peaks when heating demand would be very high? What are potential mitigating measures?

I think this is less about natural gas and more about need to build hybrid systems that pair grid connections with captive power, battery storage, etc. Developers are acutely focused on continuous baseload power. We are increasingly seeing developers agree to curtail usage during peak hours to secure faster grid connections. Where captive generation is fed by natural gas this adds a layer of security for the power generation. The use of hybrid systems that pair gas with battery storage provides a mitigating measure. Batteries can be dispatched to handle short-term needs, reducing the immediate strain on the grid or on-site gas generation during peak events.

To what degree do you think gas would be used elsewhere globally in power data centers? Or is it more of a U.S. phenomenon?

That will vary by region. In countries and regions with meaningful natural gas resources and infrastructure we would expect trends to be similar to the U.S. For example, in Alberta, Canada where we are already seeing similar colocation trends emerging. For countries that import natural gas, they will take an all-energy approach based on local needs and economics to build out additional power to meet rising AI-driven data center demand growth.

# AI & Energy Security

AI Drives Data Center Growth
AI is the dominant source of tracked data center demand increasing from 4.3 GW (\~12% share) in 2023 to approximately 110 GW (70% share) by 2030.

![](images/65ecd2d679fcc83568596ac46293abe531e09cc4999d154dc3b7251fbc6270fb.jpg)

Lower PUE, Higher Computing Efficiency
Declining PUE reflects ongoing efficiency gains that help ease power constraints while supporting AI-driven growth.

![](images/92411838d01b870daa277a1b4fa6aba9ddb0b59094aaea3f9fa696db36341189.jpg)

Sizeable Growth of In-Service Data Center Capacity
U.S. data center capacity exceeded 50 GW in 2025, growing at a 24% CAGR since 2020. Growth was led by MISO (43% CAGR), with ERCOT, SPP, and SE also experiencing strong expansion as AI-driven demand accelerates.

![](images/94c9d1697cd5f52c4d38739c1ec649c2ada47ffec9f496dd5d6323bd20d5fb5e.jpg)

Opportunities in the equipment space are vast as numerous industries all need similar electrical hardware. More than 2,500-GW of renewable, storage, and large-load projects are already stalled in grid queues worldwide requiring annual grid investment, expansion of grid supply chains, and workforce capacity.

Meeting electricity demand through 2030 requires

annual
grid investment to rise about

\~\$400 billion

Large Power Transformers

![](images/5fa3809c317c16596e299fa195e36f72f7f70a454560b395fd3bfdfb97d4f28d.jpg)

Used in utility substations, data center substations, and transmission networks

![](images/80c6769bf74bb5a1a9b32d5d88c36292f167a1aa3042f8b54b94f2d102b2cb04.jpg)

Large Unit Lead Times = 24 - 48 months

Electrical Equipment Market

![](images/c29b347cbc6941cdedf81a2e1889db6f6299b3037e8bf932c0a97d123712ea4a.jpg)

Market expected to grow to \$65 billion by 2030

![](images/d1d7754f58f4ce2ccaddd33b64e8348cf29023e731524e2a195055910f218751.jpg)

Critical Component Lead Times = 18-36 months

Medium/High-Voltage Switchgear & Breakers

![](images/b9107f03dbba4078c90946b89d11e71ec44891dfbaee43c0ceb1559f83da82f1.jpg)

Used in data center electrical rooms, substations, and grid interconnects

![](images/b7affda0c1d4c2935100468efd58b4faf8344a4cf18fc494f501376335c0855b.jpg)

Unit Lead Times = 12 - 30+ months

Generator Step-Up Transformers

![](images/c1e7414a9f13d5a7f2c9bedebf9e783af08acdda22fb4a0d153fede9555c5d50.jpg)

Used in natural gas-fired power plants, solar/wind/storage plants and BYOG facilities

![](images/aeb22b99786f2c3fbe99b61c0d7269449d682e6b23787648e32ccf429b7006cc.jpg)

Demand increased more than 270% since 2019

![](images/c5447e638c281c3b790e268426dae1b4e6e6ed170c7abbedf5ff66dad3881f5e.jpg)

Large Unit Lead Times = up to 3 - 4 years

Substation Transformers

![](images/bf869cc68cece2a2bab8b77d6393413f16612b41e46658964579dd833d72fad0.jpg)

Demand up by more than 110% since 2019

![](images/83bbccab18ab164ae6dbe619bfbab8505e8ddfa4877529406ebdd2a6241a6373.jpg)

Prices are about 80% higher over the last five years

## Global EV Demand Reaccelerates

Global EV sales surpassed 20 million units in 2025, rising \~20% year-over-year, led by strong growth in Europe, China and emerging markets.

## Europe

![](images/d475d88e15eb44d90b285f8f14f9a19e45ebfcd516c71638aeddba400e6150c3.jpg)

China  
![](images/639f6b548f8bc964945abfb69bf39105ee045926bf07f59b5a8b6213c56545c1.jpg)

• EV Sales rose \~30% in 2025 (4.2 million)

• EV Production rose \~30% to \~3.2 million

• EVs accounted for \~55% of new car sales (13 million+)

\- Produced \~75% of global EV output (\~16 million)

## Southeast Asia

![](images/fc21fc3a4e8b3ae8d01de2bd868e7d6882ba32b28aee53e0d1a16ca86f39e6f0.jpg)

• EVs represented \~ 40% of new car sales in Vietnam

• EV penetration approached 25% in Thailand

## Middle East

![](images/d80a6753a313350d209342da7373a1616d73f9c316fa2cda749a9d484befe143.jpg)  
\~30% increase

\- EV sales reached \~75K units in 2025

\- \~40% growth y/y

Global Demand for Energy Security Boosts Chinese Clean-Tech

Rising energy security concerns are accelerating investment in renewables and energy storage, driving record demand for Chinese clean-tech exports.

Batteries EVs Solar

![](images/b4451b9f3b23d6b58533d1e8fe4856f9e555c10479f5dd79d21ef0f4a7a954b9.jpg)

# Overcoming Gridlock

## The drivers: AI and energy security

## Commodities Strategy Views

## 1. What the AI market is telling us about power scarcity

The AI market signals that power access is a revenue and cost constraint in addition to being an infrastructure concern. Frontier model providers continue to strike bespoke compute-and-power deals with infrastructure owners, while hyperscalers are using their balance sheets to reserve capacity ahead of demand. Major model providers are making significant capacity-reservation moves in a scarce power-and-compute environment with the goal of substantially increasing capacity.

Figure 1. Global data center capacity to rise non-linearly, particularly as demand climbs and deliveries of power infrastructure and generation equipment rise in the years ahead  
![](images/235ebbb7b60cca22dcba27e937caa35154282b8940974097e2fce46cdcd7a472.jpg)

More broadly, data center electricity demand rose 17% in 2025, with AI-focused facilities growing even faster, and that

[中间内容因长度限制已省略]

situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.</td></tr><tr><td colspan="2">Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.</td></tr><tr><td colspan="2">Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data &amp; Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information &lt;(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.</td></tr><tr><td colspan="2">The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.</td></tr><tr><td colspan="2">© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the "Product"), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.</td></tr><tr><td colspan="2">ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST</td></tr></table>
"""
