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
## Global Energy Storage

Neil Beveridge, Ph.D. +852 2123 2648 neil.beveridge@bernsteinsg.com

Brian Ho, CFA +852 2123 2615 brian.ho@bernsteinsg.com

Kelvin Yuan, Ph.D., CFA +852 2123 2612 kelvin.yuan@bernsteinsg.com

## Battery Weekly 20 July

## America

\- Samsung SDI to Build Dedicated Tesla ESS Battery Line in the US.- thelec.net Samsung SDI is establishing a dedicated lithium iron phosphate (LFP) battery production line for Tesla energy storage systems (ESS) at its StarPlus Energy (SPE) joint venture facility in Indiana, USA, which is operated with Stellantis. The plant is converting part of its EV battery production capacity to ESS manufacturing, with a 200Ah LFP cell line expected to begin production in late 2026 and a 300Ah LFP cell line, intended for Tesla ESS products, scheduled to start production in Q2 2027. Industry sources estimate Samsung SDI's battery supply agreement with Tesla could be worth KRW 3–5 trillion. The project marks Samsung SDI's first major battery supply program for Tesla and reflects growing demand for utility-scale energy storage systems, particularly in North America.

\- SK On and Hyundai start battery cell production in Georgia.- elective.com SK On and Hyundai Motor Group have started mass production of battery cells at their Hyundai-SK Battery Manufacturing America (HSBMA) joint venture in Georgia, USA. Backed by an investment of approximately USD 5 billion, the facility is expected to reach an annual production capacity of 35 GWh, enough to supply batteries for around 300,000 electric vehicles per year. The plant is already supplying Hyundai's new EV manufacturing facility in Savannah, Georgia, with battery cells that will be assembled into packs for Hyundai, Kia, and Genesis electric vehicles. The project strengthens Hyundai's localized North American battery supply chain and reinforces Georgia's position as a major hub for EV and battery manufacturing in the United States.

\- LG Energy Solution likely to increase battery supply for Tesla.- elective.com LG Energy Solution (LGES) is reportedly expanding cylindrical battery production at its Nanjing, China facility to meet rising demand from Tesla, particularly for the Model Y. The company is expected to bring two new production lines online in the second half of 2026, with additional expansions planned in later phases. Each line is estimated to add 2 GWh of annual capacity, potentially increasing total output into the double-digit GWh range. LGES is a key supplier of nickel-based batteries for Tesla's Model 3 and Model Y, with batteries from Nanjing primarily serving Tesla's Shanghai Gigafactory. The expansion reflects continued growth in Tesla vehicle sales and increasing demand for cylindrical battery cells in the EV market.

\- Hyundai's \$5 Billion EV Battery Plant In Georgia Powers Up.- insideevs.com Hyundai Motor Group and SK On have begun production at their USD 5 billion Hyundai SK Battery Manufacturing America (HSBMA) facility in Georgia, USA, marking a major milestone in the localization of Hyundai's North American EV supply chain. The plant is expected to reach an annual production capacity of 35 GWh, enough to supply batteries for approximately 300,000 electric vehicles per year, and will provide battery cells for Hyundai's nearby Metaplant America in Savannah, where the Hyundai Ioniq 5, Ioniq 9, Kia EV6, and Kia EV9 are produced. The facility is expected to create around 3,500 jobs and strengthens Georgia's position as a key hub for EV and battery manufacturing, although the pace of future production expansion will depend on EV demand in the U.S. market.

\- This Tesla Model 3 Battery Chemistry Ages Better Than The Rest.- insideevs.com A long-term analysis of Tesla Model 3 vehicles conducted in Sweden found that CATL's lithium iron phosphate (LFP) battery delivered the best capacity retention among four battery variants after approximately 62,000 miles (100,000 km) of driving. The CATL-supplied LFP pack retained 93.3% of its original capacity, outperforming batteries from LG Energy Solution (91.5%) and Panasonic (89.8% and 88.2%). The results reinforce the reputation of LFP batteries for superior durability, thermal stability, and resistance to degradation, although they typically offer lower energy density than nickel-based battery chemistries. The findings highlight the growing attractiveness of LFP technology for EV owners prioritizing long-term battery health and lower ownership costs.

\- LG to power Google's biggest solar hub.-korea joongang daily LG Energy Solution (LGES) will supply battery systems for Google's largest solar-plus-storage project globally, the Steel River Energy Center in Arkansas, USA. Developed by Cypress Creek Energy, the project's first two phases will include 1.6 GW of solar generation and 1.9 GWh of battery storage, eventually expanding to 2.5 GW of solar capacity and 2.9 GWh of storage by 2029. LGES will provide its JF2 lithium iron phosphate (LFP) battery system, manufactured in North America, supporting growing electricity demand from AI data centers while meeting local supply-chain requirements. The project highlights the increasing role of large-scale battery storage in powering AI infrastructure and further strengthens LGES's position in the North American energy storage market.

## Asia

\- Huawei's \$11 Billion Clean Energy Empire Is Opening New Markets.- BNEF Huawei Digital Power, Huawei's clean-energy division, is rapidly expanding its global presence in battery energy storage, solar inverters, and EV charging infrastructure, with emerging markets such as Brazil becoming key growth areas. The company is supplying equipment for one of Latin America's largest battery storage projects on Brazil's Fernando de Noronha archipelago, helping reduce reliance on diesel-powered electricity. Huawei Digital Power generated more than USD 11 billion in revenue in 2025 and has become an increasingly important growth driver for Huawei amid ongoing restrictions on its telecommunications business. The company is also exploring further expansion opportunities in energy storage, EV charging, and renewable energy infrastructure as global investment in the energy transition continues to rise.

\- LG Chem Begins Cathode Material Shipments to Toyota.- thelec.net LG Chem has started supplying cathode materials to Toyota Motor North America under a long-term agreement valued at KRW 2.86 trillion, with deliveries continuing through 2030. The cathode materials, produced using precursors from Korea Precursor Co. (KPC), support a non-China battery materials supply chain that complies with U.S. Inflation Reduction Act (IRA) requirements. The materials will be used in batteries produced at Toyota's North Carolina battery plant for hybrid and plug-in hybrid vehicles sold in the U.S. The supply agreement marks LG Chem's first major external cathode customer beyond LG Energy Solution and reflects the company's broader strategy to expand its advanced materials business while reducing reliance on petrochemicals.

\- Samsung SDI Wins Largest Share of Korea's First AI Distribution Grid ESS Battery Project.- thelec.net Samsung SDI has secured the largest battery supply allocation in South Korea's first government-backed AI Distribution Grid Energy Storage System (ESS) program, winning orders for 420 MWh of battery capacity, equivalent to about $66\%$ of the total awarded volume. The project is designed to relieve grid congestion and support the integration of renewable energy by deploying 640 MWh of ESS capacity across 32 distribution lines. Samsung SDI will supply batteries to six of the nine selected project operators, outperforming domestic rivals LG Energy Solution and SK On. The initiative is part of South Korea's broader plan to deploy 700 MW of ESS by 2030 and enable the connection of an additional 1 GW of renewable energy capacity, while showcasing the growing role of battery storage in grid modernization and AI-driven energy management.

\- Samsung SDI's UPS batteries pass global fire-blocking test.-korea joongang daily Samsung SDI announced that its uninterruptible power supply (UPS) batteries for AI data centers have successfully passed a UL Solutions fire-blocking test, demonstrating the ability to contain a fire within a single battery module without spreading to adjacent racks. During the test, the battery module was intentionally ignited and allowed to burn completely, yet there was no fire propagation, gas venting, explosion, or rupture, and the fire extinguished itself without activating overhead sprinklers. Samsung SDI attributed the performance to its thermal propagation prevention technology and prismatic battery design using lithium manganese oxide (LMO) chemistry. The result strengthens the company's position in the growing AI data center power infrastructure market, where battery safety and reliability are becoming increasingly critical.

\- Environmentally friendly cars account for half of new registrations in first half of year.-korea joongang daily Environmentally friendly vehicles, including battery electric vehicles (EVs), hybrids, and fuel-cell vehicles, accounted for a record 50.4% of all new vehicle registrations in South Korea during the first half of 2026. According to industry data, 429,163 eco-friendly vehicles were registered out of a total 851,833 new vehicles, marking the first time the segment has surpassed the 50% threshold. The growth was driven primarily by EV demand, with EV registrations rising 112.6% year-on-year to 198,969 units, supported by an expanding model lineup and government incentives. Meanwhile, gasoline-powered vehicles fell below 40% of new registrations for the first time in a decade, highlighting the accelerating transition toward electrified transportation in South Korea.

\- Gaoneng Digital Manufacturing Launches Hybrid Wet-Dry Pilot Line for Solid-State Battery Development.-solare.com Chinese battery equipment company Gaoneng Digital Manufacturing has introduced a hybrid wet-dry pilot production line designed to accelerate the development of all-solid-state batteries following the implementation of China's first solid-state battery standard (GB/T 43568-2026). The flexible platform can switch between dry-process, wet-process, and hybrid manufacturing routes, allowing researchers to evaluate multiple solid-state battery technologies using a single production line. The company says the system helps reduce R&D costs, shorten development cycles, and improve process validation by combining in-house equipment with pre-validated process packages. Its modular design also enables future upgrades as projects scale from laboratory research to pilot production, supporting battery developers, material suppliers, and research institutions working on next-generation solid-state battery technologies.

\- Gotion High-Tech Secures More Than 10 GWh of Battery Orders From SANY Group.-solare.com Gotion High-Tech and Chinese construction equipment giant SANY Group have signed a strategic cooperation agreement covering more than 10 GWh of power battery orders through 2027, targeting the rapidly growing new energy heavy-duty truck and construction machinery market. The partnership will focus on battery supply for electric trucks, loaders, and other industrial vehicles, while also exploring technologies including CTB (Cell-to-Body) battery integration, lithium manganese iron phosphate (LMFP) batteries, and integrated mobile charging, storage, and battery-swapping solutions. The agreement strengthens Gotion's position in the commercial vehicle battery sector and supports the accelerating electrification of heavy-duty transportation and construction equipment in China.

\- Taoke New Energy Connects Grid-Scale Energy Storage Project in Gifu, Japan.-solare.com Shanghai Taoke New Energy Technology Co., Ltd. (Taoke New Energy) has successfully connected its 2 MW / 8.14 MWh grid-side battery energy storage system (BESS) in Kakamigahara City, Gifu Prefecture, Japan, to the grid. The project, commissioned on July 7, 2026, is expected to participate in Japan's primary frequency regulation market later this year, marking an important step in Taoke's overseas energy storage asset operations strategy. The company highlighted its ability to navigate Japan's complex permitting, certification, and grid-connection processes, and expects to bring three additional self-developed storage projects online in Japan within the same month. Taoke aims to leverage its experience in project development, construction, and operations to expand its energy storage business across Japan, China, and Southeast Asia.

\- Solid-State Battery Manufacturing Base Project Launched in Changzhou.-solare.com A CNY 550 million (USD \~76 million) Solid-State Battery Intelligent Manufacturing Assembly Base has been announced in Changzhou, Jiangsu Province, China. The project will be developed by Gaoneng Digital Manufacturing (Xi'an) Technology Co., Ltd., a company specializing in solid-state battery production equipment and dry-electrode manufacturing technologies. The facility will integrate component manufacturing, equipment assembly, production-line commissioning, material testing, and R&D operations, supporting the development of next-generation battery production systems. Originating from technologies developed by Xi'an Jiaotong University's Institute of Materials and Chemical Engineering, Gaoneng has supplied pilot and demonstration solid-state battery production lines to major industry players including CATL, Sunwoda, and Dongfeng Motor. The project further strengthens Changzhou's position as a key hub for advanced battery manufacturing and solid-state battery commercialization in China.

\- Envision AESC Launches World's First 100+ GWh Energy Storage Manufacturing Hub.-solare.com Envision AESC has officially commissioned its Yichang Super Factory in Hubei, China, creating what the company describes as the world's first 100+ GWh energy storage manufacturing base spanning the entire value chain from battery cells to system integration. The facility's first product is a 790 Ah energy storage cell, currently the world's largest prismatic wound battery cell, offering 440 Wh/L energy density, more than 12,000 charge-discharge cycles, and 96% round-trip efficiency. The first shipments have already been exported to Germany, with over 50% of the plant's capacity secured by overseas orders. The launch underscores Envision AESC's growing global presence in energy storage, supported by a network of 14 battery gigafactories across China, Japan, the United States, the United Kingdom, France, and Spain, and more than 100 GWh of cumulative energy storage cell deliveries worldwide.

## Europe

\- Spain Extends Welcome Mat for Chinese Carmakers to Its Workers.- BNEF Spain is strengthening its support for Chinese automotive investment, positioning itself as a key European manufacturing hub for electric vehicles and batteries. A government report highlights three major China-linked industrial projects, including the €4.1 billion CATL–Stellantis battery plant, which is expected to create more than 4,000 direct jobs and will initially rely on Chinese workers during the construction phase through 2028. The report also covers partnerships involving Chery–Ebro Motors and BAIC–Santana Motors, which together are expected to generate nearly 6,000 direct jobs. Spain’s strategy is to attract Chinese technology and investment while gradually developing local suppliers and manufacturing capabilities to support the European EV transition, although key technologies will remain licensed rather than fully transferred to Spanish ownership.

\- Zelestra Signs Output Deal for Italian Battery Storage Facility.- BNEF Spanish renewable energy developer Zelestra has signed an e

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
