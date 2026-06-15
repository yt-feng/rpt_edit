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

## Battery Weekly 15 June

## America

- Cypress Creek Secures \$3.5 Billion Financing for Major U.S. Solar + Storage Project.- BNEF.com Cypress Creek Energy has secured \$3.5 billion in financing for the first phases of the Steel River Energy Center in Arkansas, one of the largest renewable energy projects in the U.S. The project will combine 1.63 GW of solar power with 1.9 GWh of battery storage, with electricity to be supplied to a large technology company amid rising AI and data center power demand. The deal highlights continued strong investor support for solar and battery storage infrastructure despite shifting U.S. clean energy policies.  
- GM Pivots to Energy Storage on AI Demand, Following Ford's Lead.- BNEF.com General Motors (GM) is expanding into the stationary energy storage market through partnerships with Peak Energy and Redwood Materials, targeting rising electricity demand from AI data centers and grid infrastructure. GM plans to develop sodium-ion batteries for grid storage, citing advantages such as lower cost, improved safety, and abundant raw materials compared to lithium-ion batteries. The company is also advancing vehicle-to-grid (V2G) capabilities that allow EVs to supply power back to the grid, following a broader industry shift where automakers increasingly leverage EV battery expertise for the rapidly growing energy storage sector.  
- GM and Redwood expand partnership with second-life battery storage project.- elective.com General Motors and Redwood Materials are expanding their battery partnership with a second-life energy storage project in Michigan, using around 100 retired GM EV battery packs to provide 1.5 MW / 7.2 MWh of stationary storage at a GM manufacturing plant. The system is expected to lower electricity costs and improve grid resilience, while demonstrating how used EV batteries can be repurposed before final recycling. The project strengthens GM and Redwood's collaboration across the full battery lifecycle, including recycling, second-life deployment, and material recovery for future batteries.  
- POSCO Holdings to Demonstrate Direct Lithium Extraction in US.- thelec.net POSCO Holdings has partnered with Australia's Anson Resources to build a direct lithium extraction (DLE) demonstration plant in Utah, U.S., marking the first such project by a Korean company in the country. Scheduled to begin operation in 2027, the project aims to validate DLE technology using real lithium brine by 2028 and lay the groundwork for commercialization. Compared with traditional evaporation methods, DLE offers higher lithium recovery rates and faster production, supporting POSCO's strategy to strengthen its position in the global lithium supply chain and North American battery materials market.

## Asia

\- China's Lopal Plans USD160 Million Indonesia Expansion to Add 120,000 Tons of LFP Capacity.- yicaiglobal Lopal Tech plans to invest USD 160 million to expand its Indonesia LFP cathode materials plant, adding 120,000 tons of annual capacity for EV and energy storage batteries. The expansion supports rising overseas demand and long-term supply agreements with major customers including LG Energy Solution and CATL. Located in Central Java, the project strengthens Lopal's international manufacturing footprint and highlights Indonesia's growing role in the global battery materials supply chain.

\- CATL Places Big Order for Lithium Battery Electrolyte With China's Capchem.- yicaiglobal CATL has signed a major multi-year agreement with Chinese electrolyte supplier Capchem, covering purchases of 50,000 tons in 2026, 100,000 tons in 2027, and 150,000 tons in 2028. Based on current market prices, the deal could be worth around CNY 8.1 billion (USD 1.2 billion). The agreement strengthens long-term supply chain cooperation between the two companies and reflects growing demand for battery electrolytes driven by rapid expansion in EV and energy storage markets.

- Toptec Wins First Direct Supply Deal With Indian Automaker Group.- thelec.net South Korea's Toptec has secured its first direct overseas battery equipment contract with a major Indian automaker group, supplying pouch-type battery module and pack assembly equipment for a new production line in Pune, India. The deal, worth about KRW 13 billion, marks Toptec's expansion into India's rapidly growing EV and ESS market and strengthens its position as a global battery manufacturing equipment supplier. The company continues diversifying beyond display equipment into battery production technologies, including advanced inspection and assembly systems..  
- CK Solution Develops Dehumidifier for Solid-State Battery Production.- thelec.net South Korea's CK Solution has developed a new industrial dehumidifier system, "Dry Monster (CDHL-4500)," designed for solid-state battery manufacturing, where ultra-low humidity conditions are critical. The system delivers up to 115,000 m³/h airflow, about 2.4× larger than existing models, enabling battery makers to reduce equipment installations and lower facility space requirements by up to 30%. The technology supports the growing shift toward sulfide-based solid-state batteries, which require much stricter moisture control than conventional lithium-ion battery production.  
- Korea accelerates battery recycling efforts amid rising critical mineral prices.- pulse.mk South Korea is accelerating efforts to strengthen its battery recycling industry as prices for critical minerals such as lithium, nickel, cobalt, and manganese continue to rise. State-run agency KOMIR has launched a new initiative to build a comprehensive recycling supply-chain database and develop strategies for recovering battery materials from used batteries, manufacturing scrap, and mining byproducts. The project aims to improve domestic supply security for key battery materials used by companies such as LG Energy Solution, Samsung SDI, and SK On, while supporting the growth of a circular battery economy.  
- LG Energy Solution settles patent dispute with Sunwoda.- pulse.mk LG Energy Solution and Chinese battery maker Sunwoda have reached a patent licensing agreement, ending a battery technology dispute that lasted nearly two years. Under the deal, both parties will withdraw ongoing legal actions, while LGES emphasized the importance of fair compensation for intellectual property and technology innovation. The settlement highlights the growing importance of patent protection and licensing in the increasingly competitive global battery industry and may encourage similar agreements across the sector.  
- SPIC's 60MW/163MWh Clements Gap Battery Storage Project Enters Full Commercial Operation in Australia.-solarbe.com State Power Investment Corporation (SPIC) has officially commenced full commercial operation of its 60MW/163MWh Clements Gap Battery Energy Storage System (BESS) in South Australia, after receiving approval from AEMO and grid operator ElectraNet. Located near the existing Clements Gap Wind Farm, the project is one of the first battery projects awarded under Australia's Capacity Investment Scheme (CIS) and the first CIS storage project to enter operation. The system will participate in Australia's electricity and ancillary services markets, helping improve grid flexibility, renewable energy integration, and regional energy transition efforts.  
- EVE Energy Secures Over 67 GWh Orders at SNEC 2026 With 6.9+ MWh ESS System.-solarbe.com At SNEC 2026 in Shanghai, EVE Energy showcased its 6.9+ MWh containerized energy storage system and secured more than 67 GWh of strategic orders through partnerships with multiple industry players. The system features high energy density, long cycle life (10,000 cycles), advanced thermal management, and AI-based fire protection, targeting large-scale utility storage applications. EVE also highlighted its growing manufacturing scale, with over 3.7 million large ESS cells delivered, an operational 60 GWh mega factory, and plans for an additional 230 GWh of capacity expansion, reinforcing its leadership in the global energy storage market.  
- Ningxia Zhiyao Signs 2 GWh Sodium-Ion Battery Project in China.-solarbe.com Ningxia Zhiyao New Energy Technology has signed an agreement to build a 2 GWh sodium-ion battery manufacturing project in Lingwu, Ningxia, with total investment of CNY 1.06 billion (\~USD 147 million). The project will include production, R&D, storage, and supporting facilities, aiming to strengthen the regional energy storage battery supply chain and support growth in upstream materials and downstream logistics services. The investment reflects accelerating momentum in sodium-ion battery development as China expands alternative battery technologies for large-scale energy storage applications.

## Europe

\- ProLogium and OPmobility to integrate solid-state cells into modules.- elective.com ProLogium and French automotive supplier OPmobility have signed a cooperation agreement to explore integrating solid-state battery cells into EV battery modules and packs. ProLogium will supply its lithium-ceramic solid-state cells for testing, while OPmobility will develop module designs aimed at future EV platforms. The partnership focuses on accelerating system-level validation and commercialization of solid-state batteries, supporting growing demand for next-generation EV technologies with higher energy density, faster charging, and improved safety.

- EcoPro BM Begins Mass Production of High-Nickel Cathodes in Hungary.- thelec.net EcoPro BM has begun mass production of high-nickel NCA cathode materials at its Debrecen, Hungary plant, marking its first shipments to a European automotive OEM. The facility has annual capacity of 54,000 tons, enough to support around 600,000 EVs, and forms part of EcoPro's broader European battery materials hub. The company plans to expand production, add NCM cathode lines, and deepen partnerships with major European automakers as demand for localized battery supply chains grows.  
- Philenergy Wins UK Battery Project.- thelec.net Philenergy has secured battery manufacturing equipment orders for Agratas' gigafactories in India and the UK, including a UK contract worth KRW 14.8 billion. The company will supply its proprietary integrated slitting-notching equipment, which combines multiple electrode processing steps into a single platform to improve efficiency, reduce material loss, and increase processing speed. The deal strengthens Philenergy's position in the global battery equipment market as it expands beyond Samsung SDI and targets next-generation battery manufacturing technologies.  
- Nissan collaborates with partners on sulphur-based solid-state battery research.- elective.com Nissan, the University of Oxford, and UK battery materials company Gelion have launched the CoRe-SoLiS research project to develop solid-state lithium-sulfur batteries with higher energy density, faster charging, and longer lifespan. The project will integrate Gelion's nano-encapsulated sulfur (NES) cathode technology into Nissan's future solid-state battery platforms, aiming to reduce battery cost while improving durability. Backed by UK government funding, the initiative targets next-generation EV batteries and seeks to overcome key commercialization challenges of lithium-sulfur technology.

EXHIBIT 1: Key commodities price performance

<table><tr><td></td><td>Price12-Jun</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Metal prices (US$/tonne)</td></tr><tr><td>LiCO (spot)</td><td>23,687</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-3%</td><td>-19%</td><td>179%</td><td></td></tr><tr><td>LiOH (spot)</td><td>22,949</td><td></td><td></td><td></td><td></td><td>-2.2%</td><td>-4%</td><td>-18%</td><td>170%</td><td></td></tr><tr><td>LiCO (contract)</td><td>20,000</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>7%</td><td>104%</td><td></td></tr><tr><td>LiOH (contract)</td><td>20,250</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>1%</td><td>9%</td><td>128%</td><td></td></tr><tr><td>Cobalt (spot)</td><td>55,857</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>70%</td><td></td></tr><tr><td>Nickel (spot)</td><td>17,693</td><td></td><td></td><td></td><td></td><td>0.1%</td><td>-5%</td><td>-7%</td><td>17%</td><td></td></tr><tr><td colspan="11">Component prices</td></tr><tr><td>Cathode NMC811</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-2%</td><td>53%</td><td></td></tr><tr><td>Cathode LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>2%</td><td>-11%</td><td>84%</td><td></td></tr><tr><td>Precursor NMC811</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-1%</td><td>37%</td><td></td></tr><tr><td>Precursor LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>5%</td><td>10%</td><td>40%</td><td></td></tr><tr><td>Artificial Graphite</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>6%</td><td></td></tr><tr><td>Natural Graphite</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>0%</td><td></td></tr><tr><td>Electrolyte NMC</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>23%</td><td></td></tr><tr><td>Electrolyte LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>43%</td><td></td></tr><tr><td>Separator</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>5%</td><td>17%</td><td></td></tr><tr><td colspan="11">Spot battery cell cost (US$/kWh)</td></tr><tr><td>LFP</td><td>61</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-3%</td><td>18%</td><td></td></tr><tr><td>NMC532</td><td>90</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-1%</td><td>31%</td><td></td></tr><tr><td>NMC622</td><td>89</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-1%</td><td>28%</td><td></td></tr><tr><td>NMC811</td><td>88</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-1%</td><td>26%</td><td></td></tr><tr><td colspan="11">Spot battery pack cost (US$/kWh)</td></tr><tr><td>LFP</td><td>76</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-4%</td><td>2%</td><td></td></tr><tr><td>NMC532</td><td>121</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-1%</td><td>21%</td><td></td></tr><tr><td>NMC622</td><td>121</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-1%</td><td>19%</td><td></td></tr><tr><td>NMC811</td><td>121</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-1%</td><td>18%</td><td></td></tr></table>

Source: Bloomberg, Baiinfo, Bernstein analysis and estimates (cell and pack cost)

EXHIBIT 2: Key companies price performance and valuation

<table><tr><td></td><td>Price12-Jun</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Cell makers</td></tr><tr><td>LGES</td><td>402,500</td><td>KRW</td><td>61.9</td><td>624.8x</td><td>16.7x</td><td>4.0%</td><td>-2%</td><td>-9%</td><td>32%</td><td></td></tr><tr><td>Samsung SDI</td><td>562,000</td><td>KRW</td><td>29.8</td><td>132.7x</td><td>19.5x</td><td>10.8%</td><td>-1%</td><td>-10%</td><td>222%</td><td></td></tr><tr><td>CATL</td><td>390.6</td><td>CNY</td><td>273.2</td><td>18.7x</td><td>13.3x</td><td>2.2%</td><t

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
