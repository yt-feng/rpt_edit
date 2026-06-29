你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Energy Storage

Neil Beveridge, Ph.D. +852 2123 2648 neil.beveridge@bernsteinsg.com

Brian Ho, CFA +852 2123 2615 brian.ho@bernsteinsg.com

Kelvin Yuan, Ph.D., CFA +852 2123 2612 kelvin.yuan@bernsteinsg.com

## Battery Weekly 29 June

## America

\- Samsung Joins With US Battery Startup Seeking Pentagon Cash.- BNEF. Samsung SDI will invest USD 20 million in U.S. battery startup Forge Nano and provide engineering support to help scale battery cell production at a new factory in North Carolina. The partnership includes a long-term agreement for Samsung to purchase 250 MWh of battery cells annually starting in 2028, while helping the company secure a more localized, China-free supply chain for U.S. defense and aerospace applications. Forge Nano is also seeking up to USD 275 million in Pentagon financing, highlighting growing U.S. efforts to build a domestic battery manufacturing ecosystem and reduce dependence on foreign battery materials and components.

\- Lyten to pay €60 million for Northvolt site in Heide.- elective.com U.S. battery company Lyten has agreed to acquire Northvolt's unfinished battery factory site in Heide, Germany, for approximately €60 million, paving the way for a new battery manufacturing project after Northvolt's bankruptcy halted development. Unlike Northvolt's original plan, Lyten intends to build a smaller battery cell factory, alongside a large-scale energy storage system and data center, creating around 1,000 jobs. The acquisition helps preserve strategic battery manufacturing capacity in Germany while reducing potential losses from public funding previously allocated to the Northvolt project.

\- QuantumScape signs Honda as solid-state battery partner.- elective.com QuantumScape and Honda R&D have entered a multi-year research partnership to accelerate the development of solid-state battery technology and manufacturing processes. Following a successful evaluation of QuantumScape's solid-state platform, Honda will collaborate on advancing the company's QSE-5 lithium-metal battery, which promises higher energy density, faster charging, and improved safety compared with conventional lithium-ion batteries. The agreement further validates QuantumScape's technology and expands its network of automotive partners as the company moves toward commercialization of solid-state batteries.

\- Ford to produce first LFP cells this year – thanks to CATL.-electrive.com Ford is on track to begin production of LFP (lithium iron phosphate) battery cells at its BlueOval Battery Park Michigan facility, with mass-production-ready cells currently undergoing final validation. Using CATL-licensed technology, the plant will supply batteries for Ford's upcoming affordable EV platform, including a next-generation electric pickup planned for 2027. The move marks Ford's strategic shift toward lower-cost battery chemistries, with LFP expected to complement future LMR (lithium manganese-rich) batteries as the company seeks to reduce EV costs and strengthen its domestic battery manufacturing footprint.

\- This Ex-Rental Tesla's Battery Was Heavily Degraded. Then The Decline Slowed.- insideevs.com A high-mileage 2022 Tesla Model 3 Long Range that lost about $20\%$ of its battery capacity during its first two years as a rental vehicle showed a much slower degradation rate afterward. Battery health declined from $80\%$ to $76\%$ in the first year under private ownership, but fell only 1 percentage point to $75\%$ over the following 14 months despite continued use. The case suggests that EV battery degradation is often non-linear, with the most significant capacity loss occurring early in a battery's life before stabilizing into a slower aging curve, highlighting the long-term durability of EV batteries even after heavy early use.

\- CSIQ Secures 381MWh Energy Storage Project in Michigan.-solarbe.com CSIQ's e-STORAGE division has been selected by Apex Clean Energy to supply a 75MW/381MWh battery energy storage system (BESS) for the Coldwater Solar Project in Michigan, USA. The project will utilize e-STORAGE's SolBank 3.0 LFP battery system, along with integrated PCS and EMS solutions, with deliveries expected to begin in early 2027 and commercial operation targeted for mid-2027. The project supports Michigan's energy transition goals, including the deployment of additional energy storage capacity and the retirement of coal-fired generation, while enhancing grid flexibility and renewable energy

## Asia

\- CATL Speeds up Global Expansion of Battery Swapping Business With Hong Kong Launch.- yicaiglobal CATL is accelerating the global rollout of its battery-swapping business, expanding its Choco-Swap passenger EV network into Hong Kong while also advancing plans for a heavy-duty truck battery-swapping network in Europe. The company has already opened its first two swapping stations in Hong Kong and delivered the region's first battery-swappable taxis, with plans to build around 36 stations by 2030. The move follows CATL's recent partnership with Octopus Energy to deploy more than 30 truck battery-swapping stations across Europe by 2035, underscoring the company's strategy to scale battery swapping as a key solution for urban mobility and commercial transportation worldwide.

\- Hina and FAW conclude long-term test of sodium-ion electric truck battery.- elective.com Hina Battery and FAW Jiefang have successfully completed a seven-month, 15,000-km field test of a 339 kWh sodium-ion battery in an electric heavy-duty truck, demonstrating strong performance in extreme cold-weather conditions. The battery retained more than 90% of its usable capacity at -40°C, while supporting 20–25 minute fast charging and a lifespan of over 8,000 fast-charge cycles. The results highlight the potential of sodium-ion technology for commercial vehicles operating in cold regions, offering advantages in safety, durability, and resource availability, although lower energy density remains a key challenge compared with conventional lithium-ion batteries.

\- Volvo's EX30 battery woes spread to China with new recall.- cnevpost.com Volvo Cars is recalling 2,501 China-built EX30 electric SUVs due to a potential battery defect that could lead to internal short circuits, overheating, smoke generation, and, in rare cases, thermal runaway. The affected vehicles were manufactured between April and December 2024, and owners are advised to limit charging to $70\%$ until repairs are completed. The recall follows a broader global EX30 battery safety campaign and highlights ongoing quality concerns surrounding battery cells reportedly supplied by Sunwoda, underscoring the importance of battery safety and quality control in the EV industry.

\- CATL teams with Galbot to scale humanoid robots in battery factories.- cnevpost.com CATL has partnered with Chinese robotics company Galbot to accelerate the deployment of humanoid robots in battery manufacturing, marking a new step in factory automation. The collaboration centers on the Galbot S1, a heavy-load humanoid robot powered by CATL batteries and capable of handling up to 50 kg with dual robotic arms. Already operating on CATL's production lines, the robot performs tasks such as material handling and component picking in battery module and pack manufacturing. Beyond production, the two companies also plan to develop maintenance and service standards for industrial humanoid robots, highlighting the growing convergence of advanced batteries, AI, and intelligent manufacturing.

\- CATL Launches World's First Utility-Scale Sodium-Ion Energy Storage System.-solarbe.com CATL has unveiled Tener Sodium, the world's first utility-scale sodium-ion energy storage solution, marking a major milestone in the commercialization of sodium-ion batteries for large-scale ESS applications. The modular system supports more than 30 MWh per installation, offers flexible storage durations from 1 to 8 hours, and delivers up to 15,000 cycles with strong performance across extreme temperatures. CATL highlighted key innovations including a dedicated sodium-ion BMS, a Bi-DC power control system that improves round-trip efficiency, and a millisecond-level self-healing architecture that enhances grid reliability and safety. With commercial readiness confirmed across both the technology and supply chain, CATL plans to begin deliveries in China in September 2026, followed by global deployment in 2027, signaling the start of GWh-scale sodium-ion energy storage adoption.

\- Natrium Technology Breaks Ground on 10GWh Sodium-Ion Battery Project in Ningxia.-solarbe.com Natrium Technology has commenced construction of a 10GWh sodium-ion battery project in Yanchi County, Ningxia, with a total investment of CNY 3.03 billion. The project will be developed in two phases, covering the full sodium-ion battery value chain, including cathode and anode materials, battery cell manufacturing, PACK assembly, and energy storage applications. Once completed, the facility is expected to support growing demand for energy storage systems and electric vehicles, further strengthening China's push toward large-scale commercialization of sodium-ion battery technology.

\- Guyi New Energy Launches 2.2GWh Solid-State Battery Project in Inner Mongolia.-solarbe.com Guyi New Energy (Inner Mongolia) has received approval to develop a 2.2GWh solid-state battery manufacturing project in Hohhot, Inner Mongolia, with a total investment of CNY 800 million. The project includes a 2.2GWh production line, an R&D pilot line, and supporting facilities such as manufacturing, research, office, and warehouse buildings. Scheduled for completion between June 2026 and June 2027, the project reflects continued investment in high-safety solid-state battery technology as China accelerates development of next-generation battery manufacturing capabilities.

\- Hyundai steps up localization as ASEAN emerges as EV growth market.- pulse.mk Hyundai Motor Group is accelerating its expansion in Southeast Asia (ASEAN) by strengthening local EV production and battery manufacturing capabilities as the region emerges as a key growth market for electric vehicles. Through its joint venture with LG Energy Solution, Hyundai operates the HLI Green Power battery plant in Indonesia, supplying batteries for locally produced EVs such as the Kona Electric. The company is also expanding manufacturing capacity in Vietnam, positioning itself to capture rising EV demand across ASEAN as growth in more mature markets such as China and the U.S. begins to slow.

\- PNT Completes Cathode Material and Battery Cell Plant in Gumi.- thelec.net South Korea's PNT has completed construction of its fourth manufacturing facility in Gumi, following an investment of KRW 150 billion. The new plant will produce cathode active materials and battery cells, marking PNT's expansion beyond its traditional battery equipment business into battery materials and cell manufacturing. The facility spans 66,050 square meters and is expected to create around 200 jobs, supporting the company's strategy to evolve from a battery equipment specialist into a provider of comprehensive battery solutions.

\- Lotte Energy Materials Secures National Certification for Solid-State Battery Material Technology.- thelec.net Lotte Energy Materials has received South Korea's New Excellent Technology (NET) certification for its sulfide-based solid electrolyte particle-sizing technology, a key process for all-solid-state battery materials. The technology enables the production of sub-micron solid electrolyte particles while preserving ionic conductivity and minimizing material degradation during manufacturing. The certification validates Lotte's capabilities in next-generation battery materials and strengthens its position in the development of solid-state battery technologies, which are widely viewed as a critical future battery platform.

\- SK On Completes Stake Swap With EVE Energy, Takes Full Control of Yancheng Plant.- thelec.net SK On has completed a stake swap with Chinese battery maker EVE Energy, gaining 100% ownership of its battery manufacturing facility in Yancheng, China, three months ahead of schedule. As part of the transaction, SK On transferred its stake in a Huizhou joint venture to EVE Energy and acquired EVE's remaining stake in the Yancheng operation, while receiving CNY 200 million to balance the equity exchange. The move is part of SK On's broader strategy to streamline its global manufacturing footprint, improve operational efficiency, and strengthen its financial position as it prepares the Yancheng plant for upgraded battery production beginning in 2027.

## Europe

\- BYD Rejects Claims It Violated Hungary's Environmental Rules.- BNEF BYD has rejected allegations that it violated environmental regulations during construction of its EV manufacturing plant in Szeged, Hungary, stating that the claims are unfounded and are being addressed through legal channels. Despite an ongoing investigation related to the handling of soil at the construction site, BYD said it remains focused on ramping up production at its first European vehicle plant and is continuing to evaluate locations for a second European manufacturing facility. The case highlights increasing regulatory scrutiny of the EV and battery industry in Europe as automakers expand local production.

\- CATL, Octopus Plan 30-Plus Truck Battery-Swapping Stations Across Europe by 2035.- yicaiglobal.com CATL and Octopus Energy have formed a joint venture, Swaptopus, to deploy more than 30 battery-swapping stations for electric heavy-duty trucks across Europe by 2035. The first demonstration stations are expected to launch in the UK in 2027, leveraging CATL's proven truck battery-swapping technology and Octopus's energy and software expertise. The network could support over 300,000 electric trucks, accelerate freight electrification, reduce dependence on imported fossil fuels, and attract more than €30 billion in private investment, marking CATL's first overseas expansion of its Qiji Energy truck battery-swapping business.

\- Rock Tech struggles with financing for lithium converter in Guben-electrive.com Rock Tech Lithium is facing financing hurdles for its planned lithium hydroxide converter in Guben, Germany, one of the largest proposed battery materials projects in Europe. The company is seeking funding for the €750 million facility, which is designed to produce 24,000 tonnes of battery-grade lithium hydroxide annually, enough for roughly 500,000 EVs per year. While permits are already in place, the lack of private investment has delayed a final investment decision, pushing expected production startup from the original 2027 target to 2029 or later. The project highlights the financing challenges facing Europe's battery supply chain despite strong long-term demand for locally sourced battery materials.

\- CATL sources battery components from China instead of Debrecen.-electrive.com CATL's battery factory in Debrecen, Hungary, has fallen behind schedule, with battery cell production yet to begin despite earlier plans to start mass production in 2026. While CATL has commenced battery module production at the site, key customers such as Mercedes-Benz are currently sourcing batteries for new EV models from China, with CATL reportedly covering the additional logistics costs. The delays are linked to pending regulatory approvals and stricter environmental oversight, although CATL continues expanding local operations and ultimately plans to scale the facility to 100 GWh of annual capacity, making it one of Europe's largest battery manufacturing hubs.

\- Hyundai Establishes Battery Assembly for the loniq 3 in Turkey.- elective.com Hyundai is investing €715 million to expand production of its upcoming loniq 3 EV in İzmit, Turkey, including a new battery pack assembly facility developed with Hyundai Mobis. The battery plant, backed by a €55 million investment, will use automated production lines and create more than 300 jobs, supporting Hyundai's broader localization strategy in Europe. Scheduled to begin production in August, the Ioniq 3 will become Hyundai's first battery-electric passenger vehicle manufactured in Turkey, strengthening regional EV supply chains and reducing reliance on imported battery systems.

\- LG Energy Solution to Showcase AI Data Center Power Solutions at ees Europe 2026.- thelec.net LG Energy Solution (LGES) will showcase a range of AI data center and energy storage solutions at ees Europe 2026 in Germany, highlighting its strategy to expand beyond EV batteries into power infrastructure. Key products include the JF2S DC LINK 5.0 utility-scale ESS, powered by LFP cells produced in Poland, as well as next-generation UPS and battery backup unit (BBU) systems designed for AI servers and data centers. LGES will also demonstrate its battery passport platform and regulatory compliance capabilities, reinforcing its focus on localized European supply chains and the growing intersection of AI, energy storage, and grid infrastructure.

\- Sunwoda Completes EU Battery Passport System Integration Test.-solarbe.com Sunwoda has successfully completed system integration testing with the EU Battery Passport Digital Product Passport (DPP) registry, becoming one of the first Chinese battery companies to achieve end-to-end validation of the platform. The milestone prepares the company for the EU's Battery Regulation, which will require EV, light mobility, and industrial batteries above 2 kWh sold in Europe to carry a digital battery passport starting in February 2027. By establishing full lifecycle data traceability—from raw materials and manufacturing to recycling—Sunwoda strengthens its regulatory readiness and competitiveness in the European battery market while positioning itself ahead of upcoming compliance requirements.

\- Sungrow Secures 260MWh Energy Storage Project in Italy.-solarbe.com. Sungrow has signed a strategic agreement with ENGIE Italia to supply a 65MVA/260MWh battery energy storage system (BESS) in Pisa, Italy. The project, scheduled for delivery in Q1 2027 and commercial operation in Q3 2027, will utilize Sungrow's PowerTitan 2.0 storage platform, medium-voltage converters, EMS, and a 20-year long-term service agreement. The project supports Italy's rapidly growing energy storage market and renewable energy integration efforts, while expanding ENGIE's Italian BESS portfolio to 300MW/1,108MWh and further strengthening Sungrow's position in the European utility-scale storage market.

EXHIBIT 1: Key commodities price performance

<table><tr><td></td><td>Price26-Jun</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>E

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
