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
# Global Energy Storage

Neil Beveridge, Ph.D. +852 2123 2648 neil.beveridge@bernsteinsg.com

Brian Ho, CFA +852 2123 2615 brian.ho@bernsteinsg.com

Kelvin Yuan, Ph.D., CFA +852 2123 2612 kelvin.yuan@bernsteinsg.com

## Battery Weekly 22 June

## America

\- HyVISION System Wins 95 Billion-Won ESS Battery Pack Equipment Order in North America.- thelec.net South Korea's HyVISION System has secured a KRW 95 billion (\~USD 69 million) order for ESS battery pack assembly equipment in North America, with the contract value increasing nearly fivefold as the customer expanded its U.S. production plans through 2028. The equipment is expected to support production of LG Energy Solution's grid-scale ESS products at a facility in Ohio, with three assembly lines planned. The deal strengthens HyVISION's position in the rapidly growing North American ESS supply chain and highlights rising investment in localized battery manufacturing infrastructure.

\- Yujin Technology Expands Supply of Key Components for North American ESS Production Lines.- thelec.net South Korea's Yujin Technology is expanding shipments of precision notching presses and cutter sets for prismatic battery production lines used in North American ESS manufacturing. The company is supplying equipment to facilities in the U.S., Canada, and Poland, with cumulative first-half orders reaching about KRW 6.9 billion. The expansion strengthens Yujin's position in the global battery equipment supply chain, while its recurring business model for maintenance and consumable replacement supports long-term growth alongside rising ESS battery production demand.

\- GM advances LMR battery cells as LFP plans fade.- elective.com General Motors (GM) is reconsidering its EV battery roadmap and may prioritize lithium manganese-rich (LMR) batteries over LFP for future vehicles. GM says LMR chemistry could offer similar costs to LFP but around 33% higher energy density, making it more suitable for larger EVs such as pickups and SUVs. While GM's Tennessee plant will still begin producing LFP cells, those batteries are now expected to target stationary energy storage systems rather than EVs. GM and LG Energy Solution have been jointly developing LMR technology for years, aiming for commercialization around 2028, as automakers continue searching for lower-cost, high-performance battery chemistries.

\- SK On Sole Battery Supplier for Hyundai Motor Group's U.S. Metaplant.- thelec.net SK On has been confirmed as the exclusive battery supplier for Hyundai Motor Group Metaplant America (HMGMA) in Georgia, providing all batteries for EVs and hybrid vehicles produced at the facility, including the Ioniq 5, Ioniq 9, and Sportage Hybrid. The batteries are supplied from SK On's Georgia plant using a non-China supply chain that complies with U.S. FEOC requirements. Rising sales of Hyundai and Kia EVs in the U.S. are expected to improve utilization at SK On's American battery operations, while the company further expands local production with new ESS and joint-venture capacity.

\- Sebang Lithium Battery to Partner With LGES on North American ESS Supply Worth 1.8 Trillion Won.- thelec.net Sebang Lithium Battery will partner with LG Energy Solution (LGES) to manufacture battery modules for LGES's JF2 Link grid-scale ESS platform at a new facility in Ohio, targeting the fast-growing North American energy storage market. The project is expected to generate cumulative orders worth KRW 1.8 trillion (\~USD 1.3 billion) by 2028, with first shipments scheduled for the fourth quarter of 2026. Supported by major investments from Sebang Group, the partnership strengthens LGES's local ESS supply chain and expands Sebang's presence beyond traditional automotive batteries into large-scale energy storage manufacturing.

\- This Dodge Charger EV Prototype Packs An Experimental Semi-Solid-State Battery.- insideevs.com Stellantis has begun real-world testing of a semi-solid-state battery developed with U.S. startup Factorial Energy, using a Dodge Charger Daytona EV prototype. The battery features an energy density of 375 Wh/kg, significantly higher than conventional lithium-ion cells, and can reportedly charge from 15% to 90% in 18 minutes. The project aims to validate the technology's performance, safety, and durability under real driving conditions, while advancing Stellantis' broader strategy toward next-generation batteries with longer range, faster charging, and lower costs.

\- Far East Battery Launches 5MWh Solar-Plus-Storage Project in Silicon Valley to Expand North American AIDC ESS Ecosystem.-solarbe.com Far East Battery has begun installation of a 5MWh solar-plus-storage project in Silicon Valley, marking another milestone in its North American expansion following previous commercial ESS deployments in Southern California. The project includes an 860kVA PCS and 5MWh containerized storage system, designed to meet U.S. UL and IEEE standards for grid and safety compliance. Targeting the rapidly growing AI data center (AIDC) energy storage market, the system will provide services including peak shaving, demand management, and backup power, helping customers optimize energy costs and improve renewable energy utilization. The project strengthens Far East Battery's strategy to deepen its presence in the global ESS market across North America, Europe, and the Middle East.

\- 2026 FIFA World Cup Signals the Rise of “Event-Grade ESS 2.0”.-solarbe.com The 2026 FIFA World Cup is emerging as a showcase for a new era of “Event-Grade ESS 2.0”, where battery energy storage evolves from a simple backup power source into an intelligent microgrid hub supporting zero-carbon stadium operations. With most host venues across the U.S., Canada, and Mexico integrating solar power systems, energy storage has become essential for shifting daytime renewable energy into nighttime match operations, powering lighting, broadcasting, cooling, and digital systems. The next generation of stadium ESS requires high safety, high reliability, and AI-driven energy management, while also creating long-term value through virtual power plants (VPPs), EV charging, grid services, and emergency backup applications after the tournament, highlighting how large sporting events are accelerating the commercialization of advanced clean energy infrastructure.

\- DARPA Launches Next-Generation Military Battery Program Targeting 10× Energy Density.-thedefensepost.com The U.S. Defense Advanced Research Projects Agency (DARPA) has launched a new program to develop next-generation rechargeable military batteries capable of delivering 5–10 times higher energy density than current technologies. The initiative will focus on advancing battery chemistry, materials, and cell architecture to support future battlefield systems requiring significantly greater endurance and power output, highlighting growing strategic interest in advanced energy storage technologies for defense applications.

## Asia

\- China to Require Heavy Truck Charging Stations on Highways to Boost EV Truck Use, Cut Emissions.- yicaiglobal China has introduced a national plan requiring charging and battery swapping infrastructure for electric heavy-duty trucks to be integrated into highway development projects, aiming to accelerate freight transport decarbonization. By 2030, the country plans to build 3,000 heavy-truck charging and swapping stations across a 30,000-km zero-carbon freight corridor, while expanding grid infrastructure and green fuel networks. The policy targets raising new energy heavy-truck penetration to 40% and reflects growing efforts to support large-scale electrification of commercial transport through coordinated energy and transportation infrastructure development.

\- Eve Energy Soars After Chinese Battery Giant Says First-Half Profit to More Than Double.-yicaiglobal Chinese battery maker EVE Energy saw its shares surge after forecasting that first-half net profit will more than double year-over-year to about CNY 3.4 billion (USD 500 million), supported by strong growth in both EV and energy storage battery demand. The company also expects revenue to rise around $60\%$ , driven by expanding battery installations, rising exports, and improved supply-chain management. EVE Energy continues to gain market share in China's battery industry as demand for ESS and electric vehicles remains strong.

\- China's Lithium Carbonate Futures Snap One-Month Drop to Rise on Energy Storage, AI Demand.- yicaiglobal China's lithium carbonate futures rebounded sharply after nearly a month of declines, supported by strong demand growth from energy storage systems (ESS), electric vehicles (EVs), and AI data center infrastructure. Analysts say the lithium market is shifting from being driven mainly by EVs to a broader demand base that includes ESS and AI computing power, improving long-term supply-demand dynamics. Rising energy storage deployment and AI-related electricity demand are also expected to increase demand for high-performance lithium batteries and battery materials, supporting a recovery across the lithium battery supply chain.

\- CATL tempers near-term expectations for solid-state Batteries.- Electrive.com CATL said large-scale commercialization of solid-state batteries is still unlikely before 2030, citing unresolved manufacturing and cost challenges. CEO Robin Zeng noted that early solid-state batteries will likely appear first in premium EVs, while the company continues laboratory validation and prototype development of its sulfide-based solid-state technology. Although CATL aims to begin limited production around 2027, the company emphasized that current solid-state cells remain significantly more expensive than conventional lithium-ion batteries, highlighting the long development path for next-generation battery technologies.

\- Huawei HIMA brings in battery suppliers beyond CATL in cost-cutting push.- cnevpost.com Huawei's HIMA (Harmony Intelligent Mobility Alliance) is expanding its battery supplier network beyond CATL, adding companies including Gotion High-Tech, CALB, and Sunwoda to support lower-cost EV production. The move aims to reduce battery costs as HIMA pushes deeper into the mass-market EV segment, with smaller battery makers reportedly offering prices about 10% lower than CATL. The strategy reflects intensifying competition in China's EV market and growing efforts by automakers to diversify supply chains while balancing cost, scale, and performance requirements.

\- MaiTian Energy Partners With ByteDance Feishu on AI-Driven Digital Transformation.-solarbe.com MaiTian Energy has signed a strategic partnership with ByteDance Feishu (Lark) to accelerate AI-driven digital transformation in the clean energy sector. The collaboration will focus on AI capability sharing and integration across business operations, helping improve global coordination, operational efficiency, and organizational competitiveness. The partnership highlights growing adoption of AI and digital management platforms within the residential energy storage industry.

\- China's ESS Industry Faces Three Major Policy Shifts in H2 2026.-solarbe.com China's energy storage industry is entering a major transition phase in H2 2026 as new policies shift the market away from policy-driven installations toward a more market- and compliance-focused model. Key regulations including Document No. 114, Order No. 41, and the new DL/T 2041-2025 grid connection standard are introducing capacity-based payments, stricter safety and grid compliance requirements, and new rules that increasingly make storage essential for distributed renewable integration. As a result, the industry is expected to consolidate, favoring companies with strong capabilities in grid integration, compliance, EMS/software optimization, and asset operation, while low-cost hardware-focused players may struggle in the more performance-driven market environment.

## Europe

\- Farasis Energy Partners With Germany's WLF Energy on AI-Driven ESS.- solarbe.com Farasis Energy has signed a strategic cooperation agreement with Germany's WLF Energy to jointly develop next-generation battery and energy storage solutions for global markets. The partnership combines Farasis's expertise in battery technology and manufacturing with WLF Energy's AI-driven energy management platform and digital energy systems. The collaboration will focus on utility-scale, commercial & industrial, and distributed energy storage applications, while also exploring virtual power plants, renewable integration, and smart grid technologies. The agreement marks an important step in Farasis Energy's global expansion strategy and highlights growing convergence between AI, energy management, and advanced battery systems.

\- Pylontech Connects 13.2MWh ESS Project in Slovakia.- solarbe.com Pylontech has successfully connected and launched a 6.6MW/13.2MWh energy storage project at an industrial park in Slovakia, with expansion already underway. The project uses four L3300-OMNI liquid-cooled ESS containers and was completed in just six months from planning to operation. Designed for high efficiency, long cycle life, and enhanced safety, the project strengthens local renewable energy infrastructure and highlights Pylontech's growing presence in the European energy storage market.

\- BYD expands battery assembly in Brazil.- elective.com BYD plans to expand its battery assembly operations in Brazil as part of its strategy to increase the local content of vehicles produced in the country to 50% by 2027. While battery cells will continue to be manufactured in China, BYD will localize module and pack assembly for EVs at its Camaçari facility, where it already produces the Dolphin Mini. The company is also considering local production of stationary energy storage systems (BESS) in Brazil, supporting both its automotive and energy storage ambitions in Latin America while reducing reliance on imports and improving local supply-chain integration.

\- €3,000 for battery defects: Aviloo converts battery diagnostics into a Purchase Guarantee.- elective.com Aviloo is expanding its EV battery diagnostics business by introducing a one-year battery warranty program for used electric vehicles in Europe. Using its independent battery health testing and certification system, the company will offer buyers up to €3,000 compensation if a battery's condition falls below a calculated health threshold within the warranty period. Integrated into its new Aviloo Connect platform, the service aims to improve transparency and trust in the growing used EV market by making battery condition and risk easier to evaluate for dealers, fleets, and consumers.

\- BYD energy storage powers Hungary's largest battery project online.- cnevpost.com BYD Energy Storage has supplied a 288.6 MWh battery storage system for Hungary's largest battery energy storage project, developed by Greenvolt Power. The 99.8 MW / 288.6 MWh project uses BYD's MC Cube storage platform and is designed to support grid frequency regulation, peak shaving, and renewable energy integration across Hungary and Central Europe. The project marks another step in BYD's expansion in the European ESS market, as the company continues deploying large-scale storage systems globally.

\- The 2027 BMW iX5's Monster Battery Pack Dwarfs The Competition.- insideevs.com BMW's upcoming iX5 electric SUV will feature one of the largest battery packs in its segment, with up to 144 kWh usable capacity for the U.S. market, positioning it as a potential 400+ mile range EV. The model combines elements of BMW's new Neue Klasse technology, including 800V architecture and sixth-generation cylindrical cells, while remaining on the existing Cluster Architecture platform. Despite its large battery and heavy weight, 

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
