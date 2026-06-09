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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Energy Storage

Neil Beveridge, Ph.D. +852 2123 2648 neil.beveridge@bernsteinsg.com

Brian Ho, CFA +852 2123 2615 brian.ho@bernsteinsg.com

Kelvin Yuan, Ph.D., CFA +852 2123 2612 kelvin.yuan@bernsteinsg.com

# Battery Weekly 8 June

# America

- SK On Unveils Next-Generation 'GRIDON' ESS in US.- thelec.net SK On unveiled its next-generation ESS platform "GRIDON Gen2" at CLEANPOWER 2026, targeting mass production in Q3 2027. The new system supports both DC and AC configurations, with around $15\%$ higher energy capacity per container and enhanced safety features, including EIS monitoring and liquid-based fire suppression. Leveraging its $\sim 100$ GWh U.S. production capacity, SK On aims to secure more than 20 GWh of ESS orders in 2026, with over 10 GWh already under discussion with U.S. customers, strengthening its push into the North American ESS market.   
- Rocket Battery Maker Sebang Battery to Invest 100 Billion Won in US ESS Business.- thelec.net Sebang Battery plans to invest KRW 100 billion (\~USD 72 million) to expand into the U.S. energy storage (ESS) market, by funding its new subsidiary Sebang Lithium Battery America. The investment—supported by the founding family through a capital increase—will establish a dedicated North American ESS business unit. The move aligns with Sebang's strategy to pivot from traditional lead-acid batteries toward ESS and eco-friendly energy solutions, while leveraging favorable U.S. policies and strong projected growth in the ESS market.   
- Old Waymo Batteries Will Get A Second Life As Stationary Energy Storage.- insideevs.com Waymo has partnered with B2U Storage Solutions to repurpose its retired robotaxi batteries into grid-scale energy storage systems. The project will deploy hundreds of megawatts of second-life battery capacity, starting in Texas and California, to store excess renewable energy and support grid demand. The initiative reflects a growing industry trend where used EV batteries are reused for stationary storage, extending their lifecycle and reducing the need for immediate recycling while supporting renewable energy integration.   
- Moment Energy opens new second-life facility in Vancouver.- elective.com Moment Energy is launching a second-life battery facility in Vancouver to repurpose used EV batteries into stationary energy storage systems (BESS), with expected annual capacity of 1 GWh. Instead of recycling for raw materials, the company reuses batteries from sources such as Mercedes-Benz, extending their lifecycle for applications like data centers, industrial users, and utilities. The facility, supported by over USD 100 million in total funding, reflects growing demand for second-life battery solutions to support grid storage and renewable integration.   
- Graphite deal with Tesla: Syrah reports resolution in delivery dispute.- elective.com Syrah Resources has resolved a key dispute with Tesla over a graphite supply agreement, with Tesla withdrawing its termination notice after accepting that Syrah is now producing compliant battery-grade anode material. The deal involves supplying 8,000 tonnes of graphite annually from Syrah's Vidalia, Louisiana plant, but final contract approval remains pending as qualification tests are still ongoing. The development reduces short-term uncertainty but highlights ongoing risks in non-Chinese battery material supply chains, as Syrah aims to become a major global graphite supplier.

# Asia

\- China's Tinci Inks New Deal With Major Client to Double Battery Materials Order.- yicaiglobal Tinci Materials has signed an expanded agreement with Cornex New Energy to supply over 1.01 million tons of battery electrolytes and chemicals by 2030, nearly doubling the original contract. The deal reflects strong growth in energy storage battery demand, as Cornex rapidly expands capacity to 180 GWh annually, including a new 50 GWh ESS-focused plant. The agreement strengthens Tinci's position as a leading global electrolyte supplier and highlights accelerating scale-up across the battery supply chain.

- China's AI Computing Boom Tests the Limits of Green Power, Experts Say- yicaiglobal China's rapid growth in AI computing demand is exceeding the pace of renewable energy deployment, creating challenges in aligning clean power supply with data center needs. Experts warn that despite strict efficiency and renewable targets, 24/7 green power matching remains difficult, with gaps between reported renewable usage and actual grid conditions. Rising AI workloads are driving sharp increases in electricity demand and power instability risks, highlighting the need for better coordination between computing workloads, grid infrastructure, and energy storage solutions such as multi-hour batteries and flexible load management.   
- EcoPro to Pursue Company-Wide AI Transformation by 2028.- thelec.net EcoPro plans to implement a company-wide AI transformation (AX), aiming to become a fully AI-driven enterprise by 2028. The strategy includes deploying AI across R&D, manufacturing, and operations, reducing product development time by up to 50%, improving productivity by 30%, and enhancing defect detection accuracy to 95%. The company also plans to build autonomous factories and laboratories, using AI and robotics to optimize efficiency, lower energy consumption, and enable 24/7 automated operations.   
- ITM Semiconductor Joins Government Project to Develop Battery Thermal Runaway Delay Technology.- thelec.net ITM Semiconductor is participating in a South Korea government-backed project (2026–2030) to develop technologies that delay thermal runaway propagation in pouch-type batteries. The project focuses on combining pressure pad structures and graphene-based thermal management to suppress heat spread and improve safety. ITM will be responsible for heat dissipation design, fire propagation prevention, and system validation, with applications across EVs, ESS, robotics, and defense.   
- Mintech Launches 'Mintech Ionics' for Next-Generation Battery Development.- thelec.net Mintech has established a new subsidiary, Mintech Ionics, to focus on next-generation energy materials, including solid-state battery electrolytes, anodes, fuel cell components, and solar materials. Leveraging its expertise in battery diagnostics (EIS technology), the company aims to accelerate material development and improve ion transport performance. The move expands Mintech's role from diagnostics into core material supply, positioning it for growth in solid-state batteries, hydrogen, and solar energy markets.   
- IBK to launch new fund to promote renewable-energy equipment.- pulse.mk IBK (Industrial Bank of Korea) plans to launch a KRW 250 billion (\~USD 167 million) fund to support the use of locally produced renewable energy equipment and strengthen domestic supply chains. The fund will provide low-interest loans and equity support to projects using Korean-made technologies, helping local manufacturers compete with imports. It is part of IBK's broader strategy to expand energy infrastructure financing, including BESS, grid, and data center projects, as the bank targets KRW 8 trillion in energy investments over five years.   
- HyperStrong Secures Over 1 GWh of Energy Storage Orders in Southeast Europe.-solarbe.com HyperStrong has secured over 1 GWh of energy storage orders in Southeast Europe, including more than 900 MWh of large-scale grid storage projects in Romania and an additional 75 MWh of utility-scale and commercial & industrial (C&I) systems in Croatia and Serbia, supporting applications such as grid stability, renewable energy integration, and power demand management. The deals mark a significant step in the company's European expansion, strengthening its presence in rapidly growing Balkan markets where demand for large-scale and diversified energy storage solutions is accelerating.   
- Wasion Energy Storage Secures First EU Battery Regulation Certification for Containerized ESS.-solarbe.com Wasion Energy Storage has become the first company globally to receive the EU Battery Regulation (EU 2023/1542) NB certification for its GridUltra liquid-cooled containerized energy storage system, marking a key milestone for entering the European market. The certification confirms compliance with stringent EU requirements on battery safety, lifecycle management, and environmental standards, effectively serving as a “passport” for Europe. The GridUltra system (3.3–5.0 MWh) features advanced liquid-cooling and integrated safety design, highlighting Wasion’s capability to meet high regulatory standards and strengthening its competitiveness in the European utility-scale ESS market.   
- Xingchen Energy and Chuneng Sign 10 GWh Battery Strategic Partnership.-solarbe.com Xingchen Energy and Chuneng New Energy have signed a 10 GWh lithium-ion battery strategic cooperation agreement to strengthen collaboration across supply chain coordination, product integration, quality control, and project delivery. The partnership aims to support Xingchen's rapid expansion in large-scale energy storage projects by improving supply reliability, production capacity alignment, and delivery efficiency. Leveraging Chuneng's manufacturing and scaling capabilities, the deal enhances Xingchen's ability to execute multi-region, multi-project ESS deployments, reinforcing its industrial ecosystem as the market shifts from capacity expansion toward operational efficiency and value creation.

# Europe

\- Cylib and Vianode im to Close the Battery Graphite Loop.- elective.com Cylib and Vianode have signed a collaboration agreement to develop recycled graphite for next-generation battery anodes, aiming to strengthen Europe's circular battery supply chain. Cylib will use its OLiC recycling technology to recover high-purity graphite from used batteries, while Vianode will integrate and test the material in anode production and pilot projects. The partnership aims to reduce reliance on imported raw materials and lower $\mathrm{CO}_{2}$ emissions, supporting Europe's push for a more sustainable and locally sourced battery ecosystem.

- Honda invests in battery materials manufacturer Nexeon.- elective.com Nexeon, a UK-based developer of silicon anode materials, has received a new investment from Honda through its Honda Xcelerator Ventures program to support further growth and commercialization. The funding will accelerate development of silicon-based anodes, which can significantly improve energy density and charging performance compared to traditional graphite. Nexeon is scaling production at its Gunsan, South Korea facility, targeting large-scale output and supplying customers such as Panasonic, highlighting growing industry interest in next-generation battery materials.   
- ProLogium targets SPAC merger to fund French battery plant.- elective.com ProLogium plans to merge with SPAC TDAC (Translational Development Acquisition Corp.) to raise at least USD 250 million and accelerate the commercialization of its solid-state batteries. The deal will enable ProLogium to list on Nasdaq (ticker: PRLG) and fund construction of its gigafactory in Dunkirk, France, which is scheduled to start production in 2028 with initial capacity of 0.8 GWh, expanding to 12 GWh by 2032. The move provides faster access to capital markets and supports scale-up of its next-generation lithium-ceramic solid-state technology for EVs and other applications such as data centers and aerospace.   
- Samsung SDI reportedly to supply battery cells to Volkswagen.- elective.com Samsung SDI is reportedly set to become a new supplier for Volkswagen's standardized "Unified Cell" battery platform, alongside PowerCo and Gotion. Samsung SDI is expected to convert production lines at its Hungary plant to manufacture the prismatic cells, with mass production starting around 2027 and capacity reaching double-digit GWh levels. The move would strengthen Volkswagen's battery supply chain in Europe and support its flexible platform strategy, which can use multiple chemistries such as LFP, NMC, and future solid-state batteries.   
- Europe's Largest Flow Battery Project (800 MW/1.6 GWh) Begins Construction.- solarbe.com Flexbase has started building an 800 MW / 1.6 GWh flow battery project in Switzerland, the largest in Europe, located at a key cross-border grid hub. The project combines long-duration energy storage, an AI data center, and district heating, forming a zero-carbon energy system where renewable power is stored, used for computing, and waste heat is reused for heating. It is expected to start operation in 2028 and significantly support grid stability and decarbonization.

EXHIBIT 1: Key commodities price performance 

<table><tr><td></td><td>Price5-Jun</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Metal prices (US$/tonne)</td></tr><tr><td>LiCO (spot)</td><td>24,580</td><td></td><td></td><td></td><td></td><td>-2.9%</td><td>-4%</td><td>-3%</td><td>193%</td><td></td></tr><tr><td>LiOH (spot)</td><td>24,506</td><td></td><td></td><td></td><td></td><td>0.1%</td><td>0%</td><td>1%</td><td>186%</td><td></td></tr><tr><td>LiCO (contract)</td><td>20,250</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>8%</td><td>108%</td><td></td></tr><tr><td>LiOH (contract)</td><td>20,000</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>8%</td><td>135%</td><td></td></tr><tr><td>Cobalt (spot)</td><td>55,858</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>68%</td><td></td></tr><tr><td>Nickel (spot)</td><td>18,689</td><td></td><td></td><td></td><td></td><td>-1.0%</td><td>-2%</td><td>-5%</td><td>20%</td><td></td></tr><tr><td colspan="11">Component prices</td></tr><tr><td>Cathode NMC811</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>3%</td><td>53%</td><td></td></tr><tr><td>Cathode LFP</td><td></td><td></td><td></td><td></td><td></td><td>#N/A</td><td>#N/A</td><td>#N/A</td><td>#N/A</td><td></td></tr><tr><td>Precursor NMC811</td><td></td><td></td><td></td><td></td><td></td><td>#N/A</td><td>#N/A</td><td>#N/A</td><td>#N/A</td><td></td></tr><tr><td>Precursor LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>2%</td><td>8%</td><td>32%</td><td></td></tr><tr><td>Artificial Graphite</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>4%</td><td></td></tr><tr><td>Natural Graphite</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>-6%</td><td></td></tr><tr><td>Electrolyte NMC</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-3%</td><td>23%</td><td></td></tr><tr><td>Electrolyte LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-3%</td><td>43%</td><td></td></tr><tr><td>Separator</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>5%</td><td>17%</td><td></td></tr><tr><td colspan="11">Spot battery cell cost (US$/kWh)</td></tr><tr><td>LFP</td><td>44</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>4%</td><td></td></tr><tr><td>NMC532</td><td>90</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>30%</td><td></td></tr><tr><td>NMC622</td><td>89</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>27%</td><td></td></tr><tr><td>NMC811</td><td>88</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>1%</td><td>25%</td><td></td></tr><tr><td colspan="11">Spot battery pack cost (US$/kWh)</td></tr><tr><td>LFP</td><td>59</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-2%</td><td>-9%</td><td></td></tr><tr><td>NMC532</td><td>122</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>21%</td><td></td></tr><tr><td>NMC622</td><td>121</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>19%</td><td></td></tr><tr><td>NMC811</td><td>121</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>1%</td><td>17%</td><td></td></tr></table>

Source: Bloomberg, Baiinfo, Bernstein analysis and estimates (cell and pack cost)

EXHIBIT 2: Key companies price performance and valuation 

<table><tr><td></td><td>Price5-Jun</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Cell makers</td></tr><tr><td>LGES</td><td>408,000</td><td>KRW</td><td>61.8</td><td>755.5x</td><td>16.7x</td><td>-1.2%</td><td>-11%</td><td>-13%</td><td>40%</td><td></td></tr><tr><td>Samsung SDI</td><td>559,000</td><td>KRW</td><td>29.2</td><td>144.5x</td><td>19.3x</td><td>-5.1%</td><td>-19%</td><td>-20%</td><td>221%</td><td></td></tr><tr><td>CATL</td><td>408.2</td><td>CNY</td><td>285.8</td><td>19.6x</td><td>13.9x</td><td>-4.3%</td><td>-4%</td><td>-6%</td><td>62%</td><td></td></tr><tr><td>CALB</td><td>28.7</td><td>HKD</td><td>7.0</td><td>17.2x</td><td>5.1x</td><td>-6.1%</td><td>-2%</td><td>-19%</td><td>71%</td><td></td></tr><tr><td>EVE Energy</td><td>59.7</td><td>CNY</td><td>19.1</td><td>17.6x</td><td>11.3x</td><td>-5.3%</td><td>-6%</td><td>-18%</td><td>29%</td><td></td></tr><tr><td>Gotion</td><td>30.7</td><td>CNY</td><td>8.2</td><td>25.7x</td><td>7.5x</td><td>-3.7%</td><td>-7%</td><td>-17%</td><td>23%</td><td></td></tr><tr><td>Sunwoda</td><td>21.2</td><td>CNY</td><td>5.8</td><td>15.2x</td><td>5.8x</td><td>-2.9%</td><td>-7%</td><td>-23%</td><td>14%</td><td></td></tr><tr><td>Farasis</td><td>12.1</td><td>CNY</td><td>2.2</td><td>n.a.</td><td>n.a.</td><td>-2.7%</td><td>-7%</td><td>-13%</td><td>-8%</td><td></td></tr><tr><td colspan="11">Lithium Miners/Refiners</td></tr><tr><td>Albemarle</td><td>165.7</td><td>USD</td><td>19.5</td><td>13.3x</td><td>6.8x</td><td>-1.6%</td><td>-6%</td><td>-15%</td><td>182%</td><td></td></tr><tr><td>SQM</td><td>77.7</td><td>USD</td><td>21.3</td><td>11.1x</td><td>6.3x</td><td>-1.1%</td><td>-10%</td><td>-16%</td><td>141%</td><td></td></tr><tr><td>Pilbara Minerals</td><td>5.9</td><td>AUD</td><td>13.6</td><td>34.5x</td><td>17.4x</td><td>-3.3%</td><td>-8%</td><td>-2%</td><td>340%</td><td></td></tr><tr><td>Ganfeng Lithium</td><td>57.6</td><td>HKD</td><td>19.5</td><td>13.9x</td><td>12.1x</td><td>-4.9%</td><td>-10%</td><td>-33%</td><td>188%</td><td></td></tr><tr><td>Tianqi Lithium</td><td>59.5</td><td>CNY</td><td>14.3</td><td>16.1x</td><td>5.4x</td><td>-2.5%</td><td>-5%</td><td>-26%</td><td>96%</td><td></td></tr><tr><td colspan="11">Cathode</td></tr><tr><td>LG Chem</td><td>331,500</td><td>KRW</td><td>15.1</td><td>145.8

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
