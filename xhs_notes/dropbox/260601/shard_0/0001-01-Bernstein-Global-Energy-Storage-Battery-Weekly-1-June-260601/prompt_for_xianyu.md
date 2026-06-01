你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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

# Battery Weekly 1 June

# America

- LG Energy Solution Signs \$1.6 Billion ESS Supply Deal With DTE Energy.- thelec.net LG Energy Solution signed a \$1.6 billion ESS battery supply agreement with U.S. utility DTE Energy, covering 6 GWh of batteries over about two years. The batteries will support eight grid projects in Michigan, including an AI data center development, and will be produced at LGES's Holland, Michigan facility. The deal highlights growing demand for ESS in grid stabilization and AI infrastructure, while reinforcing LGES's strategy to expand its North American production footprint, targeting over 60 GWh global ESS capacity by year-end.   
- LG Energy Solution sells Honda JV battery plant assets.- pulse.mk. LG Energy Solution has completed the sale of building assets from its U.S. battery joint venture with Honda for KRW 3.74 trillion (USD 2.48 billion), securing additional liquidity amid a slowdown in EV demand. The assets, located at the Ohio battery plant, were sold to Honda's U.S. unit but will continue to be used through lease arrangements, ensuring operational continuity. The move reduces LGES's short-term capital burden while improving cash flow, with the proceeds expected to support the joint venture's efficiency. The plant is set to begin full-scale operations this year, supplying batteries for Honda and Acura EVs in North America, with potential expansion into hybrid vehicles and ESS.

# Asia

\- SK Innovation to Sell Loss-Making Chinese Separator Business to Semcorp for USD69 Million.- yicaiglobal SK Innovation will sell its loss-making China battery separator business (SK Hi-Tech Materials) to Semcorp for about CNY 400 million (USD \~59 million) as part of its restructuring. The Changzhou plant has \~940 million sqm capacity but has struggled with low utilization and losses due to limited customers. The acquisition allows Semcorp to quickly expand capacity and improve efficiency using its scale, customer network, and cost advantages, while SK shifts its separator operations toward Poland and other core regions.
- China's Tinci Gains on Plan to Build Lithium Battery Material Plant for Up to USD310 Million.- yicaiglobal Tinci Materials Technology plans to invest up to CNY 2.1 billion (\~USD 310 million) to build a new LFP cathode material plant in Zhejiang, China, with annual capacity of 160,000 tonnes. The project focuses on high-compaction LFP materials, which offer higher energy density, better fast-charging, and longer cycle life, targeting both high-end EV batteries and large-scale energy storage systems. The expansion is part of Tinci's strategy to move beyond electrolytes into integrated battery materials, strengthening its supply chain position for customers such as CATL, BYD, and Gotion.

\- China opens first truck battery swap station using Bosch BaaS.-electrive.com A new electric truck battery-swapping station has been launched in Chizhou, China, using a Battery-as-a-Service (BaaS) solution from the Bosch–Mitsubishi joint venture Bosch MC Battery Service Innovations. The station, developed with Shanghai Lingzhou, can serve over 100 trucks per day and combines swapping with AI-based battery monitoring and cloud analytics to track battery health and optimize performance. The project demonstrates growing adoption of BaaS models in commercial fleets, helping reduce downtime, manage battery degradation, and improve total cost of ownership as China accelerates electrification of heavy-duty transport.

\- CATL launches battery-swapping network for light electric trucks in southern China.- elective.com CATL has partnered with logistics provider DST to launch its first standardized battery-swapping network for light electric trucks in China's Greater Bay Area. The project currently operates 31 swap stations and plans to expand to 140 sites by the end of 2026, supporting around 5,000 electric trucks. Using CATL's Choco-SEB battery-swapping system, the network enables fully automated battery swaps in about 2 minutes, reducing refueling time and cutting operating costs by roughly $50\%$ compared to diesel trucks. The rollout is part of CATL's broader strategy to build a nationwide network of 3,000 swap stations and accelerate electrification of commercial transport.

- POSCO Future M to Build LFP Cathode Plant in Pohang.- thelec.net POSCO Future M, through its joint venture CNP New Material Technology, is building a new LFP cathode materials plant in Pohang, South Korea, with production set to begin in 2027 and capacity expanding to 50,000 tonnes annually. The move reflects rising demand for cost-efficient LFP batteries, particularly for energy storage systems and AI-driven power demand. In parallel, POSCO Future M is also converting part of its existing ternary cathode lines to LFP production, starting pilot runs this year. The investment supports the company's strategy to diversify its cathode portfolio beyond high-nickel materials and strengthen competitiveness in global battery markets.   
- Hyosung Heavy Industries Wins 11 Billion Won ESS Order in Japan.- thelec.net Hyosung Heavy Industries has secured an ESS EPC contract worth about KRW 11 billion in Japan to build 10 MW / 40 MWh grid-connected energy storage systems across five regions. The company will also provide up to 20 years of maintenance services, strengthening its long-term presence in Japan's ESS market. Including this deal, Hyosung has secured around KRW 64 billion in orders in its first year in Japan, following a larger project in Hokkaido earlier this year.   
- China's SINVO Starts Full Operations at Korea Plant for Tesla Battery Equipment.- thelec.net SINVO (Shenzhen Sinvo Automation) has established a battery equipment manufacturing plant in Gumi, South Korea, to supply LG Energy Solution, with equipment ultimately destined for LG's LFP battery production lines at its Lansing, Michigan plant for Tesla's Megapack ESS. The factory focuses on stacking process equipment, a critical and technically demanding step in battery manufacturing that affects performance and energy density. Most of the current workforce consists of Chinese staff, with plans to scale operations as demand increases. The move reflects a broader trend of Chinese battery equipment makers expanding into Korea, supporting global battery supply chains tied to large-scale ESS projects and Tesla-related production.   
- JR Energy Solution Partners With Factorial on Solid-State Drone Batteries.- thelec.net JR Energy Solution (JRES) has partnered with U.S.-based Factorial Energy to commercialize solid-state and lithium-metal batteries for drones, aiming to improve energy density, range, and performance. JRES will handle battery manufacturing across the Asia-Pacific region, leveraging its full in-house capabilities from electrodes to battery packs, while Factorial contributes next-generation battery technology. The collaboration is part of a global three-region strategy (U.S., Europe, Asia) and reflects growing demand for advanced batteries in drones, robotics, and industrial mobility.   
- From Tesla to BYD, Chinese-made EVs capture one-third of Korea's market.- korea joongang daily Chinese-made EVs are rapidly gaining market share in South Korea, rising to 33.9% of new EV registrations in 2025 from just 1.1% in 2021, while domestic brands fell to 57.2%. Much of the growth is driven by Tesla's China-built vehicles, but Chinese brands like BYD are also expanding quickly with lower-priced models. The surge highlights growing competition driven by cost advantages, as Korea maintains relatively low tariffs, making it harder for domestic automakers and battery suppliers to compete.   
- Zeron Raises USD200 Million as China's Electric Heavy Truck Race Heats Up.-yicaiglobal Chinese electric heavy-duty truck startup Zeron has raised USD 200 million in a new funding round, bringing its total fundraising to USD 400 million in just two months, as competition intensifies in the electric commercial vehicle market. The round attracted major industrial investors such as Zijin Mining, Shandong Energy Group, and Sanhua, along with global investors including Temasek. Founded in 2022, Zeron has rapidly scaled sales of its electric truck models and achieved positive operating cash flow, with the new funding aimed at accelerating large-scale deployment, autonomous driving development, and global expansion in the heavy-duty EV sector.   
- NR Electric Delivers World's Largest Grid-Forming Energy Storage Cluster in Saudi Arabia (2.5 GW). - cn.solarbe. NR Electric has delivered and commissioned a 2.5 GW grid-forming energy storage project for Saudi Electricity Company (SEC), now the largest grid-scale grid-forming ESS cluster in the world. The project spans five major regions—Riyadh, Rabigh, Dawadmi, Al-Jouf, and Qaisumah—and includes more than 2,000 power conversion systems (PCS). It supports advanced grid functions such as frequency regulation, voltage control, black start capability, and weak-grid stabilization, playing a key role in strengthening Saudi Arabia's power system. Despite a tight delivery timeline of less than four months, NR Electric completed system design in one week and dispatched the first integrated storage units within 53 days, highlighting rapid execution and large-scale deployment capability in utility-scale ESS projects.

# Europe

\- Orbia secures £1.4 million UK grant for graphite recycling pilot.- elective.com Orbia Fluor & Energy Materials has secured £1.4 million in UK government funding to develop a graphite recycling pilot project in Runcorn, aimed at strengthening the domestic EV battery supply chain. The project will demonstrate graphite recovery technology at a small scale before potential industrial expansion, helping reduce reliance on imports—particularly from China, which dominates global graphite supply. Backed by the UK’s DRIVE35 program, the initiative supports building a local, circular battery materials ecosystem and advancing sustainable battery production.

- DHL Supply Chain opens battery logistics hub in the Netherlands.- elective.com DHL Supply Chain is building a dedicated high-voltage battery logistics hub in Holtum, Netherlands, with operations expected to begin in early 2027. The 17,000 m² facility will focus exclusively on batteries for electric vehicles and energy storage systems (BESS), forming part of a broader European electromobility logistics campus. The center will offer end-to-end battery lifecycle services, including storage, testing, charging, maintenance, reverse logistics, and recycling preparation, strengthening supply chain support for the growing EV and ESS markets.   
- Basquevolt launches lithium-metal battery cell.- elective.com Basquevolt has launched its new BQV400L lithium-metal battery cell, marking its first commercially available high-energy-density product. The cell combines an NMC cathode, lithium-metal anode, and hybrid polymer electrolyte, delivering around 402 Wh/kg, positioning it among the highest-performance cells produced in Europe. Designed as a “drop-in” solution compatible with existing gigafactory production lines, the battery aims to accelerate industrial adoption without major additional investment. The technology represents a step toward next-generation solid-state batteries and targets applications in EVs, aerospace, and industrial sectors, with partners such as Renault supporting further development.

EXHIBIT 1: Key commodities price performance 

<table><tr><td></td><td>Price29-May</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Metal prices (US$/tonne)</td></tr><tr><td>LiCO (spot)</td><td>25,629</td><td></td><td></td><td></td><td></td><td>1.3%</td><td>-2%</td><td>2%</td><td>206%</td><td></td></tr><tr><td>LiOH (spot)</td><td>24,521</td><td></td><td></td><td></td><td></td><td>0.1%</td><td>-3%</td><td>1%</td><td>180%</td><td></td></tr><tr><td>LiCO (contract)</td><td>20,250</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-7%</td><td>8%</td><td>108%</td><td></td></tr><tr><td>LiOH (contract)</td><td>20,000</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>1%</td><td>10%</td><td>135%</td><td></td></tr><tr><td>Cobalt (spot)</td><td>55,858</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>68%</td><td></td></tr><tr><td>Nickel (spot)</td><td>19,101</td><td></td><td></td><td></td><td></td><td>0.8%</td><td>1%</td><td>-2%</td><td>24%</td><td></td></tr><tr><td colspan="11">Component prices</td></tr><tr><td>Cathode NMC811</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>4%</td><td>53%</td><td></td></tr><tr><td>Cathode LFP</td><td></td><td></td><td></td><td></td><td></td><td>1.2%</td><td>0%</td><td>2%</td><td>92%</td><td></td></tr><tr><td>Precursor NMC811</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>37%</td><td></td></tr><tr><td>Precursor LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.4%</td><td>0%</td><td>8%</td><td>30%</td><td></td></tr><tr><td>Artificial Graphite</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>4%</td><td></td></tr><tr><td>Natural Graphite</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>-6%</td><td></td></tr><tr><td>Electrolyte NMC</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-3%</td><td>23%</td><td></td></tr><tr><td>Electrolyte LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-3%</td><td>43%</td><td></td></tr><tr><td>Separator</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>2%</td><td>5%</td><td>10%</td><td></td></tr><tr><td colspan="11">Spot battery cell cost (US$/kWh)</td></tr><tr><td>LFP</td><td>62</td><td></td><td></td><td></td><td></td><td>0.3%</td><td>0%</td><td>0%</td><td>19%</td><td></td></tr><tr><td>NMC532</td><td>91</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>3%</td><td>31%</td><td></td></tr><tr><td>NMC622</td><td>89</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>3%</td><td>28%</td><td></td></tr><tr><td>NMC811</td><td>88</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>25%</td><td></td></tr><tr><td colspan="11">Spot battery pack cost (US$/kWh)</td></tr><tr><td>LFP</td><td>76</td><td></td><td></td><td></td><td></td><td>0.3%</td><td>0%</td><td>-1%</td><td>3%</td><td></td></tr><tr><td>NMC532</td><td>122</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>21%</td><td></td></tr><tr><td>NMC622</td><td>122</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>19%</td><td></td></tr><tr><td>NMC811</td><td>121</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>1%</td><td>17%</td><td></td></tr></table>

Source: Bloomberg, Baiinfo, Bernstein analysis and estimates (cell and pack cost)

EXHIBIT 2: Key companies price performance and valuation 

<table><tr><td></td><td>Price29-May</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Cell makers</td></tr><tr><td>LGES</td><td>457,500</td><td>KRW</td><td>71.3</td><td>720.5x</td><td>18.8x</td><td>2.9%</td><td>14%</td><td>-2%</td><td>59%</td><td></td></tr><tr><td>Samsung SDI</td><td>683,000</td><td>KRW</td><td>36.6</td><td>178.0x</td><td>23.8x</td><td>1.5%</td><td>6%</td><td>1%</td><td>292%</td><td><

[中间内容因长度限制已省略]

erein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
