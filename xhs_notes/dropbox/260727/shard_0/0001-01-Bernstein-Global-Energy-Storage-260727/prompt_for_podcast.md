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
# Global Energy Storage

Neil Beveridge, Ph.D. +852 2123 2648 neil.beveridge@bernsteinsg.com

Brian Ho, CFA +852 2123 2615 brian.ho@bernsteinsg.com

Kelvin Yuan, Ph.D., CFA +852 2123 2612 kelvin.yuan@bernsteinsg.com

## Battery Weekly 27 July

## America

\- LG Energy Solution Files Patent Lawsuit Against EVE Energy in U.S.- thelec.net LG Energy Solution (LGES) has filed patent infringement lawsuits against Chinese battery maker EVE Energy with the U.S. International Trade Commission (ITC) and a U.S. federal court. The case involves five battery patents, including technologies related to cylindrical batteries and tabless battery designs. LGES is seeking to block the import and sale of products using the allegedly infringing batteries in the United States, highlighting growing competition over advanced battery technologies in the North American market.

\- Samsung-Backed Pino Seeks Capital Raise as It Prepares for US Battery Rules.- thelec.net South Korean battery materials company Pino is preparing a major capital raise to support expansion of its lithium iron phosphate (LFP) cathode business and reduce its exposure to Chinese ownership. The company may increase its fundraising capacity to as much as KRW 1.6 trillion, with proceeds expected to support a new 50,000-tonne-per-year LFP cathode plant being developed by subsidiary C&P New Material Technology. Pino is also working to lower ownership stakes held by China's CNGR Advanced Material and affiliated entities to improve compliance with potential U.S. battery sourcing and Prohibited Foreign Entity (PFE) requirements. The move reflects growing efforts by battery supply-chain companies to position themselves for North American EV and energy storage markets.

\- Sila raises \$300 million to expand US silicon anode production.- elective.com U.S. battery materials company Sila Nanotechnologies has raised USD 300 million in new funding to expand production of its Titan Silicon anode material and accelerate the next phase of its Moses Lake, Washington manufacturing facility. The company aims to scale the plant's capacity from an initial 2 GWh to as much as 250 GWh over the next five years, supporting demand from EV and battery manufacturers including Mercedes-Benz and Panasonic. Sila's silicon-carbon anode technology is designed to deliver up to 20% higher energy density and faster charging than conventional graphite-based batteries, while strengthening domestic U.S. battery supply chains.

\- Brookfield to Buy Blackstone Battery Company for \$7 Billion.-BNEF Brookfield Asset Management has agreed to acquire U.S. energy storage developer Aypa Power from Blackstone Energy Transition Partners in a deal valued at USD 7 billion, including debt. Aypa operates and develops battery energy storage and hybrid renewable energy projects across North America, with 6.5 GW of operating and contracted battery capacity and more than 20 GW under development. The acquisition reflects growing investor interest in energy storage infrastructure driven by rising electricity demand from AI data centers, grid modernization, and renewable energy integration. The transaction gives Aypa an equity valuation of approximately USD 3 billion and includes the company's project portfolio, development pipeline, and workforce.

## Asia

\- China Aims to Boost Renewable Energy Consumption 53% by 2030.- BNEF China has unveiled a new renewable energy development plan that aims to increase renewable energy consumption by 53%, from 1.18 billion tonnes of coal equivalent in 2025 to 1.8 billion tonnes by 2030. The plan targets 6 trillion kWh of renewable electricity generation, including 4 trillion kWh from wind and solar, and seeks to improve grid reliability through greater deployment of energy storage systems. By 2030, renewables supported by storage are expected to provide 20% of peak electricity demand, double the current level. The strategy also includes expanding emerging technologies such as solar thermal power and marine energy, reinforcing China's long-term transition toward a more flexible and low-carbon energy system.

\- China's Innolight Seeks USD8 Billion in Hong Kong's Largest Listing in Seven Years.-yicaiglobal.com Zhongji Innolight (Innolight), the world's leading supplier of optical interconnect solutions for AI data centers and cloud computing networks, plans to raise up to HKD 62.4 billion (USD 8 billion) through a secondary listing in Hong Kong, which would be the city's largest IPO since 2019. The company intends to use the proceeds to expand high-speed optical transceiver production, strengthen its supply chain, and accelerate R&D. Innolight holds a $21\%$ global market share in optical interconnect solutions and a $28\%$ share of the high-speed data communications optical transceiver market. The offering has attracted major cornerstone investors including Temasek, ADIA, CPP Investments, BlackRock, Alibaba, and Tencent, highlighting strong investor confidence in the AI infrastructure supply chain.

\- China Sets Aside USD3.3 Billion of Gov't Bond Proceeds for New Energy Heavy-Duty Truck Industry.- yicaiglobal.com China has allocated CNY 22 billion (USD 3.3 billion) from its ultra-long-term special government bond program to support the replacement of conventional trucks with new energy heavy-duty trucks (NEHDTs) in 2026. The funding is part of a broader effort to decarbonize the transportation sector and accelerate adoption of electric and other new energy commercial vehicles. Chinese NEHDT sales have surged over the past two years, rising 182% in 2025 and nearly 80% in the first half of 2026. The government aims for new energy models to account for 40% of new heavy-duty truck sales by 2030, supported by plans to build more than 3,000 charging and battery-swapping stations and 30,000 km of zero-carbon freight corridors nationwide.

\- China's SDIC Power Allies With CATL to Build Big Hydropower Station for USD4.9 Billion.- yicaiglobal.com CATL and Chinese state-owned utility SDIC Power have partnered to invest CNY 33.4 billion (USD 4.9 billion) in the development of the 2.4 GW Yagen II Hydropower Station in Sichuan Province. Under the agreement, CATL will hold a $10\%$ stake in the project company, while SDIC Power's subsidiary Yalong River Hydropower Development will own the remaining $90\%$ . Expected to generate 8.6 TWh of electricity annually, the project is scheduled to begin operations in 2035 and could reduce carbon emissions by approximately 4.5 million tonnes per year. The investment reflects CATL's broader strategy to expand beyond batteries and energy storage into upstream renewable power generation, strengthening its position as a comprehensive clean energy solutions provider.

\- Yujin Technology Selected for Government AI Manufacturing Platform Project.- thelec.net South Korean battery equipment manufacturer Yujin Technology has been selected for the government's 2026 AI Transformation (AX) One-Stop Voucher Program. Working with Plan I and Gabia, the consortium will develop a generative AI-based manufacturing platform for battery equipment production, supported by approximately KRW 1.1 billion in first-year government funding. The platform will initially focus on improving productivity and quality in battery equipment manufacturing before expanding to other industries, including semiconductors and precision machining.

\- EcoPro BM Targets 2027 Mass Production of Solid-State Electrolyte.- thelec.net EcoPro BM announced progress in its all-solid-state battery materials roadmap, highlighting that its proprietary sulfide-based solid electrolyte technology has successfully passed qualification tests with major battery manufacturers. The company is currently reviewing pilot-scale production with customers and expects the earliest commercial mass production to begin in 2027. In addition, EcoPro BM is developing high-nickel and lithium manganese-rich (LMR) cathode materials for solid-state batteries, as well as sodium-ion battery cathodes and silicon anode materials, strengthening its position in next-generation battery technologies.

\- LG Energy Solution to Build Sodium-Ion Battery Mother Line at Ochang Plant.- thelec.net LG Energy Solution (LGES) will establish a sodium-ion battery mother line at its Ochang Energy Plant by the end of 2026, accelerating commercialization of next-generation batteries for energy storage systems (ESS). The company plans to begin customer proof-of-concept (PoC) projects in 2027, targeting long-duration ESS applications. By leveraging its proprietary Advanced Z-Stacking (AZS) manufacturing process, LGES aims to achieve higher energy density and longer cycle life than competing sodium-ion technologies. The move positions LGES to compete with CATL in the emerging sodium-ion battery market while supporting efforts to diversify battery supply chains beyond lithium-based technologies.

\- Aulton revives Hong Kong IPO bid, seeking to become first listed battery swap specialist.- cnevpost.com. Chinese battery-swapping company Aulton New Energy has resubmitted its application for a Hong Kong IPO, aiming to become the world's first publicly listed company focused on battery-swapping services. Aulton operates an open battery-swapping ecosystem, partnering with more than 16 automakers and connecting 531 battery-swapping stations across China. While revenue has declined due to weaker equipment sales, the company has narrowed losses and recently achieved its first positive gross profit period. Aulton is increasingly focusing on higher-margin operational services and future technologies such as Vehicle-to-Station-to-Grid (V2S2G) energy management, as it seeks to compete with battery-swapping networks led by Nio and CATL.

\- CALB under pressure over GAC Aion S battery issues.- elective.com Chinese battery maker CALB is facing increased attention after reports of battery-related issues in GAC Aion's Aion S electric sedan, particularly in vehicles with 150,000–300,000 km of mileage. Reported problems include battery swelling, leakage, insulation faults, range degradation, and, in some cases, power loss while driving. While no official recall has been issued, GAC Aion and CALB have responded by extending battery warranty coverage from 150,000 km to 300,000 km and offering free inspections, repairs, and battery replacements where necessary. The development comes as CALB continues its international expansion, including construction of its first European battery factory in Portugal.

\- Sumitomo Chemical aims to make solid-state batteries more affordable.- elective.com Sumitomo Chemical is preparing to commercialize a new halide-based solid electrolyte for all-solid-state batteries, aiming to reduce manufacturing costs and accelerate adoption in electric vehicles. Developed with Kyoto University and Tottori University, the material is designed to offer performance comparable to leading sulfide-based electrolytes while being easier to manufacture and compatible with parts of existing lithium-ion battery production infrastructure. The company is currently evaluating the technology with potential customers and sees it as a promising pathway to make solid-state batteries more affordable and scalable for future EV applications.

\- Anupam Rasayan and Basquevolt Sign Potential USD 300 Million Solid-State Battery Materials Partnership.-solare.com Indian specialty chemicals manufacturer Anupam Rasayan India Ltd. and Spanish solid-state battery developer Basquevolt S.A. have signed a non-binding Letter of Intent (LOI) to collaborate on specialty materials for next-generation lithium-metal solid-state batteries. The partnership could span up to 10 years and has a potential value of approximately USD 300 million (CNY 2.0 billion). Under the agreement, Anupam Rasayan will support the development, custom synthesis, and future supply of high-performance chemical materials for Basquevolt's solid-state battery technology, which targets applications in electric vehicles, heavy transport, stationary energy storage, and aviation. The deal highlights growing momentum in the global solid-state battery supply chain and Anupam Rasayan's expansion into advanced energy materials.

\- India Launches 10 GWh Advanced Battery Manufacturing Tender for Grid Energy Storage.-solare.com India's Ministry of Heavy Industries (MHI) has launched a global tender for 10 GWh of Advanced Chemistry Cell (ACC) manufacturing capacity dedicated to grid-scale energy storage applications. The tender is part of India's Production Linked Incentive (PLI) program and represents the final allocation under the country's 50 GWh ACC manufacturing initiative. Bidders must commit to achieving at least 25% local value addition within two years and 40% within five years, while building 1-4 GWh of battery production capacity within five years. Successful bidders will be eligible for PLI incentives, supporting India's efforts to expand domestic battery manufacturing and meet growing energy storage demand driven by rapid renewable energy deployment.

## Europe

\- Hungary Crackdown on \$20 Billion EV Sector Puts China on Notice.- BNEF Hungary's new government plans to introduce stricter environmental regulations and reduce subsidies for multinational companies, increasing scrutiny of major Chinese EV and battery investments. Companies including CATL, BYD, and Semcorp are facing environmental investigations or compliance reviews, signaling a tougher regulatory environment for the country's USD 20 billion EV and battery sector while maintaining support for industrial investment.

\- Cylib acquires Bavarian EV battery recycling facility.- elective.com German battery recycling company Cylib has acquired a battery processing facility in Bavaria, Germany, with the capacity to recycle up to 10,000 tonnes of end-of-life EV batteries per year. The plant will produce black mass, which will be supplied to Cylib's hydrometallurgical recycling facility under construction in Dormagen, where valuable materials including lithium, nickel, cobalt, manganese, and graphite will be recovered. The acquisition strengthens Cylib's end-to-end battery recycling capabilities and supports the expansion of Europe's domestic battery materials supply chain.

\- CATL signs 2 GWh sodium battery storage deal with Europe's Solarpro.- cnevpost.com. CATL has signed a 2 GWh sodium-ion energy storage agreement with Eastern European renewable energy developer Solarpro, marking its second major sodium-ion battery storage deal in Europe this month. The partnership will deploy Central and Eastern Europe's first large-scale sodium-ion energy storage project and accelerate adoption of CATL's new Tener Sodium battery system. Designed for long-duration storage, the system offers up to 15,000 cycles, a 25–30 year lifespan, and strong low-temperature performance, making it well-suited for European grid applications. The agreement further strengthens CATL's push to commercialize sodium-ion technology globally and expand its presence in the European energy storage market.

\- Tianneng International and ELQ Energy to Build 5 GWh Energy Storage Assembly Base in Poland.-solare.com Chinese battery manufacturer Tianneng International has signed an agreement with Polish energy company ELQ Energy to establish a 5 GWh energy storage system (ESS) assembly facility in Częstochowa, Poland. The joint venture will combine Tianneng's battery and ESS technology with ELQ Energy's local market expertise and project development capabilities. The project will be developed in phases, starting with 100 MWh of annual assembly capacity before expanding to 1 GWh in the first year and reaching 5 GWh within three years. The investment reflects the growing trend of Chinese energy storage companies localizing production in Europe to meet increasing ESS demand, comply with EU regulations, and strengthen their position in the rapidly expanding Central and Eastern European energy storage market.

## Others

\- Zimbabwe Rejects Lithium Miners' Request to Delay Export Ban.- BNEF Zimbabwe has confirmed that its ban on lithium concentrate exports will take effect on January 1, 2027, rejecting industry requests for a delay. The government said the policy is intended to

encourage domestic lithium processing and increase the value captured from the country's mineral resources. As one of the world's fastest-growing lithium suppliers, accounting for roughly $10\%$ of global mined lithium production, Zimbabwe plays a key role in the EV battery supply chain. Several Chinese companies, including Huayou Cobalt, Sinomine Resource Group, and Chengxin Lithium, have invested in local processing facilities to comply with the shift toward higher-value lithium products.

\- Octopus-Backed MOPO Partners Nigeria in \$75 Million Battery Plan.- BNEF MOPO, an Africa-focused battery rental company backed by Octopus Energy, has signed an agreement with Nigeria's Rural Electrification Agency to support a USD 75 million expansion of its battery services by 2030. MOPO provides batteries charged at its own solar-powered stations, allowing households and businesses to access electricity without purchasing solar systems or mini-grids. The company currently rents out 1.6 million batteries per month across several African countries and sees the expansion as part of broader efforts to improve electricity access in regions where grid power remains limited.

\- EVE Energy and Akaysha Energy Partner on 4 GWh Energy Storage Projects in Australia.- solare.com Chinese battery manufacturer EVE Energy has signed a Preferred Supplier Agreement (PSPD) with leading Australian energy storage developer Akaysha Energy to support the deployment of up to 4 GWh of battery energy storage projects in Australia. Under the agreement, EVE Energy will supply large-format battery storage solutions for Akaysha's expanding project portfolio. The partnership highlights EVE Energy's growing presence in overseas energy storage markets and underscores increasing demand for grid-scale battery systems in Australia, one of the world's most active energy storage markets. The deal also follows EVE Energy's recent success in securing more than 13.5 GWh of strategic energy storage orders in Europe, further strengthening its global ESS footprint.

EXHIBIT 1: Key commodities price performance

<table><tr><td></td><td>Price24-Jul</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Metal prices (US$/tonne)</td></tr><tr><td>LiCO (spot)</td><td>20,879</td><td></td><td></td><td></td><td></td><td>-0.1%</td><td>-4%</td><td>-11

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
