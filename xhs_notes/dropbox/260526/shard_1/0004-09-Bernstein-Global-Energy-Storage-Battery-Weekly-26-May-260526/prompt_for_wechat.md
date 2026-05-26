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

# Battery Weekly 26 May

# America

- Chinese Equipment Replaces Korean Suppliers at BlueOvalSK Kentucky Plant After JV Split.- thelec.net Ford is replacing Korean battery equipment at the former BlueOvalSK Kentucky plant with Chinese technology after taking control of the facility following the SK On–Ford JV split. The plant is being converted from pouch-type NCM battery production to prismatic LFP batteries using CATL technology, mainly for the ESS market under Ford Energy. As a result, equipment orders from Korean suppliers such as Hana Technology, MPLUS, Toptec, Yunsung F&C, PNT, and others have been cancelled or left without use. Meanwhile, SK On's newly controlled Tennessee plant remains uncertain, with production delayed to 2028 and future utilization depending on new EV, HEV, or ESS orders.   
- Stellantis Plans \$70 Billion Comeback With LFP Batteries And A Tesla FSD Challenger.- insideevs.com Stellantis has announced a major USD 60 billion turnaround plan to revive its EV strategy with cheaper batteries, new software, and advanced autonomy features. The company plans to launch 29 new EVs, 15 plug-in hybrid or extended-range models, and more hybrids by 2030 using a new scalable platform called STLA One. The EV version will use 800V architecture, LFP batteries, and a cell-to-body battery design to reduce cost, improve efficiency, and simplify production. Stellantis will also deepen cooperation with Qualcomm for infotainment and ADAS technology, while working with Wayve on hands-free supervised automated driving. The plan reflects Stellantis' effort to catch up in EVs, software-defined vehicles, and AI-based autonomy after weak U.S. EV launches and slowing momentum.

# Asia

\- China's Putailai to Invest USD823.3 Million to Boost Battery Separator Film Output.- yicaiglobal Putailai New Energy Technology plans to invest CNY 5.6 billion / USD 823.3 million to expand its lithium battery separator film capacity in Qionglai, Sichuan. The project will add 16 production lines with total annual capacity of 7.2 billion square meters, built in two phases: Phase I will start trial production in 2027, while Phase II is expected to begin operation in Q1 2028. The expansion aims to improve Putailai's self-sufficiency in base films, reduce production bottlenecks, and strengthen its integrated separator supply chain amid rising demand from lithium battery makers.

\- Ganfeng starts pilot production of 500 Wh/kg solid-state batteries.- elective.com Ganfeng Lithium has started small-batch production of a 10Ah lithium-metal solid-state battery with energy density of 500 Wh/kg, positioning it as a key step toward commercializing next-generation high-energy batteries. The company also said its 400 Wh/kg solid-state battery has exceeded 1,100 charge cycles and completed engineering validation. Ganfeng is developing both silicon-carbon and lithium-metal solid-state routes, targeting applications such as premium EVs, drones, eVTOL aircraft, robotics, and consumer electronics. The progress follows earlier pilot production of higher-energy semi-solid-state batteries and supports Ganfeng's broader push into advanced battery technologies for electric mobility.

\- SVOLT to start semi-solid-state battery production in September.- Electrive.com SVOLT plans to begin series production of semi-solid-state batteries in September 2026, earlier than its previous 2027 target. The batteries are expected to be integrated into multiple vehicle models soon after launch, with a 100 kWh battery version also moving toward large-scale production. SVOLT's first-generation semi-solid-state cells are expected to reach around 300 Wh/kg, with a second-generation version targeting 360 Wh/kg. CEO Yang Hongxin said semi-solid-state batteries could become the main near-term technology path because they offer better safety, energy density, and lifespan than conventional lithium-ion batteries, while fully solid-state batteries remain far from commercialization.

- Xiaomi sets up subsidiary for battery and electric motor production.- elective.com Xiaomi has established a new subsidiary, Beijing Xiaomi Jingxu Technology, to support production of key EV components including batteries, electric motors, and electronic control systems. The move aims to strengthen Xiaomi's control over its EV supply chain, after previously relying on partners such as CATL and BYD FinDreams Battery for battery solutions. Chinese media also report that Xiaomi is involved in a 15 GWh battery factory joint venture with CATL, BAIC, and Jingneng, located near Xiaomi's Yizhuang EV plant, with production expected to begin later this year. The expansion supports Xiaomi Auto's rapid growth and its 2026 delivery target of 550,000 vehicles.   
- POSCO Future M Secures Mass Production Technology for Silicon Anodes.- thelec.net POSCO Future M has secured mass production technology for silicon anode materials and aims to begin commercial production and supply in 2028 after pilot operations in Pohang, South Korea. Its silicon anode can store more than four times the energy of conventional graphite anodes, and tests showed batteries with over 20% silicon content retained more than 80% capacity after 1,000 cycles. The company reduced silicon expansion issues using nanostructuring and carbon composite technologies. POSCO Future M expects demand from premium EVs, fast-charging batteries, humanoid robots, UAM, and solid-state batteries, including cooperation with Factorial.   
- Sungrow Wins 7.5 GWh Energy Storage Order for Masdar's UAE RTC Project Sungrow signed an agreement with Masdar to supply 7.5 GWh of PowerTitan 3.0 liquid-cooled energy storage systems and 2.6 GW of PV inverter solutions for the UAE's gigascale Round-the-Clock renewable energy project, developed by Masdar and EWEC. The full project combines 5.2 GW solar PV with a 19 GWh battery energy storage system to provide reliable clean power around the clock, with operation expected in 2027. Sungrow's system will deploy over 1,000 PowerTitan 3.0 units, using an 8-hour charge / 16-hour discharge cycle, and is designed for harsh Middle East conditions, operating at up to $55^{\circ}\mathrm{C}$ without derating. The deal strengthens Sungrow's position in the Middle East utility-scale ESS market following its earlier 7.8 GWh Saudi storage project. [linkedin.com], [sunwiz.com.au]   
- Xiaomi EV reportedly taps new battery suppliers for second brand to target EREV market.-cnevpost.com Xiaomi EV is reportedly adding Sunwoda and CALB as battery suppliers for the first model under its new sub-brand Skynomad, reducing reliance on existing suppliers CATL and BYD. The model, internally codenamed Kunlun N3, is expected to launch in H2 2026 as a full-size extended-range SUV with a battery pack above 70 kWh and 400–500 km pure-electric range. Sunwoda is expected to supply around 60% of the battery quota and CALB 40%. The move helps Xiaomi lower supply-chain risk, improve cost control, and target China's competitive family EREV SUV market at around CNY 200,000, competing with models from Li Auto and Aito.   
- LG Energy Solution Moves to Secure Core LMR Battery Patents.- thelec.net LG Energy Solution is strengthening its next-generation battery patent strategy, especially around lithium manganese-rich (LMR) batteries. The company recognized 12 employees at its 2026 Inventor King and Patent King Awards, with the top inventor honored for building patents combining LMR cathodes and silicon anodes. LMR batteries are seen as promising because they use more manganese to improve cost competitiveness and energy density, and LGES is working with GM to mass-produce prismatic LMR batteries for future electric trucks and large SUVs. The company also highlighted patents related to battery-pack cooling and safety design, emphasizing that intellectual property will be key to maintaining global competitiveness.   
- Hanjung NCS Emerges as Major ESS Parts Supplier After ICE Business Shift.- thelec.net Hanjung NCS has successfully shifted from internal combustion vehicle parts to ESS components, becoming a key supplier for Samsung SDI's Samsung Battery Box. The company provides major cooling and safety parts such as cooling plates, chillers, HVAC systems, and fire-suppression components. Its ESS pivot has boosted results, with Q1 revenue up 65% year-on-year to KRW 54.7 billion and ESS now making up 97% of sales.   
- LG Energy Solution, Honda Launch Electric Two-Wheeler Battery Swapping Pilot in Vietnam.- thelec.net LG Energy Solution, Honda, and the Hanoi city government signed an MOU to launch an electric two-wheeler battery swapping pilot in Vietnam. Starting in Q3 2026, the partners plan to deploy around 50 battery swapping stations and 500 electric motorcycles across Hanoi. LG Energy Solution will supply 2170 cylindrical batteries and manage battery safety systems, while Honda will provide battery packs, swapping systems, and electric two-wheelers. The project supports Hanoi's push to reduce motorcycle emissions as the city prepares restrictions on internal combustion motorcycles, and it could help accelerate Vietnam's electric two-wheeler transition.   
- L&F Completes LFP Cathode Plant in Daegu.-thelec.net L&F has completed its new LFP cathode materials plant in Daegu, South Korea, and plans to begin mass production in Q3 2026 with annual capacity of 30,000 tonnes. The company aims to expand capacity to 60,000 tonnes by H1 2027, using its third-generation high-density LFP platform to improve energy density versus conventional LFP materials. The plant supports L&F's move beyond high-nickel cathodes into LFP materials for ESS, AI data centers, power grids, and mass-market EVs, while also working to internalize iron phosphate precursor technology currently dominated by Chinese suppliers.   
- Vitzrocell Eyes AI Data Center Market With Lithium-Ion Capacitors.- thelec.net Vitzrocell is targeting the AI data center power market with lithium-ion capacitors (LICs), which combine battery-like energy storage with capacitor-like fast charge/discharge performance. The company is in talks with U.S. and Taiwanese EMS firms and expects commercialization in H2 2027. LICs are seen as useful for AI servers because they can handle sudden 30–50% power surges from GPU workloads, improving power stability and extending PSU lifespan. If

successful, Vitzrocell's LIC business could generate over KRW 600 billion in orders by 2029–2030, becoming a major new growth driver beyond its existing defense, smart meter, and oil-and-gas battery businesses.

# Europe

\- Gotion receives €92 million for two battery projects in Spain.- elective.com Gotion High-Tech has been provisionally awarded €92 million under Spain's PERTE VEC funding program to support two battery projects in Valladolid, Spain. The projects include a battery cathode material production facility and a battery recycling plant focused on recovering black mass for reuse in new battery cells. Total investment for the two facilities is expected to reach €944.3 million. The projects strengthen Gotion's European battery materials and recycling footprint and are expected to support its planned 20 GWh battery cell plant in Morocco.

# Austraila

- Renewable Metals secures Series A funding.- elective.com Renewable Metals, an Australian battery recycling startup, has raised AUD 12 million in an oversubscribed Series A funding round to advance its battery recycling technology. The funding will support a prototype recycling plant in Kewdale, Western Australia, expected to begin operations in mid-2026 and scale to process up to 2,000 tonnes of batteries per year, equivalent to around 4,000 EV batteries. The company's process can recycle multiple battery chemistries, including NMC, LCO, and LFP, on a single line without pre-sorting or dismantling, helping reduce costs and improve flexibility. Renewable Metals will also use the funding to design its first commercial-scale facility in Hunter, New South Wales, based on a modular, lower-capital approach aimed at supporting local and global battery recycling markets.   
- GoodWe Leads Australia's Residential Energy Storage Market with Three No.1 Rankings.- solarbe.com. GoodWe has strengthened its position in Australia's home battery market, ranking No.1 in three categories based on SunWiz April 2026 market data: fastest-growing ESS manufacturer in 2026, top battery market share in Queensland, South Australia, and Tasmania, and No.1 overall market share for 0–30 kWh residential storage systems. The growth was supported by rising Australian home battery demand after the federal Cheaper Home Batteries Program, with GoodWe's ESA All-in-One Energy Storage System and Lynx F G2 battery series gaining traction due to modular design, backup capability, smart energy management, and suitability for local household needs

EXHIBIT 1: Key commodities price performance 

<table><tr><td></td><td>Price22-May</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Metal prices (US$/tonne)</td></tr><tr><td>LiCO (spot)</td><td>26,265</td><td></td><td></td><td></td><td></td><td>-0.5%</td><td>-6%</td><td>6%</td><td>203%</td><td></td></tr><tr><td>LiOH (spot)</td><td>25,162</td><td></td><td></td><td></td><td></td><td>0.1%</td><td>-6%</td><td>6%</td><td>179%</td><td></td></tr><tr><td>LiCO (contract)</td><td>21,874</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>17%</td><td>120%</td><td></td></tr><tr><td>LiOH (contract)</td><td>19,800</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>8%</td><td>124%</td><td></td></tr><tr><td>Cobalt (spot)</td><td>55,863</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>68%</td><td></td></tr><tr><td>Nickel (spot)</td><td>18,727</td><td></td><td></td><td></td><td></td><td>-1.1%</td><td>1%</td><td>3%</td><td>21%</td><td></td></tr><tr><td colspan="11">Component prices</td></tr><tr><td>Cathode NMC811</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>5%</td><td>53%</td><td></td></tr><tr><td>Cathode LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-5%</td><td>4%</td><td>89%</td><td></td></tr><tr><td>Precursor NMC811</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>3%</td><td>37%</td><td></td></tr><tr><td>Precursor LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>1%</td><td>8%</td><td>29%</td><td></td></tr><tr><td>Artificial Graphite</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>2%</td><td>2%</td><td>4%</td><td></td></tr><tr><td>Natural Graphite</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>0%</td><td>-6%</td><td></td></tr><tr><td>Electrolyte NMC</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-3%</td><td>20%</td><td></td></tr><tr><td>Electrolyte LFP</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>-3%</td><td>42%</td><td></td></tr><tr><td>Separator</td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>8%</td><td></td></tr><tr><td colspan="11">Spot battery cell cost (US$/kWh)</td></tr><tr><td>LFP</td><td>62</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>1%</td><td>18%</td><td></td></tr><tr><td>NMC532</td><td>91</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>3%</td><td>30%</td><td></td></tr><tr><td>NMC622</td><td>90</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>4%</td><td>28%</td><td></td></tr><tr><td>NMC811</td><td>89</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>2%</td><td>25%</td><td></td></tr><tr><td colspan="11">Spot battery pack cost (US$/kWh)</td></tr><tr><td>LFP</td><td>78</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-1%</td><td>1%</td><td>5%</td><td></td></tr><tr><td>NMC532</td><td>122</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>21%</td><td></td></tr><tr><td>NMC622</td><td>122</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>3%</td><td>19%</td><td></td></tr><tr><td>NMC811</td><td>121</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0%</td><td>2%</td><td>17%</td><td></td></tr></table>

Source: Bloomberg, Baiinfo, Bernstein analysis and estimates (cell and pack cost)

EXHIBIT 2: Key companies price performance and valuation 

<table><tr><td></td><td>Price22-May</td><td>Ccy</td><td>Mkt cap$bn</td><td>P/E26E</td><td>EV/EBITDA26E</td><td>%1D</td><td>%1W</td><td>%1M</td><td>%1Y</td><td>1Y pxchart</td></tr><tr><td colspan="11">Cell makers</td></tr><tr><td>LGES</td><td>399,500</td><td>KRW</td><td>61.7</td><td>860.4x</td><td>16.1x</td><td>2.3%</td><td>-5%</td><td>-18%</td><td>46%</td><td></td></tr><tr><td>Samsung SDI</td><td>648,000</td><td>KRW</td><td>34.5</td><td>173.7x</td><td>22.4x</td><td>6.2%</td><td>5%</td><td>1%</td><td>297%</td><td></td></tr><tr><td>CATL</td><td>411.2</td><td>CNY</td><td>285.8</td><td>19.7x</td><td>13.9x</td><td>-0.1%</td><td>-3%</td><td>-8%</td><td>52%</td><td></td></tr><tr><td>CALB</td><td>29.5</td><td>HKD</td><td>7.2</td><td>17.6x</td><td>5.1x</td><td>-0.1%</td><td>-3%</td><td>-18%</td><td>69%</td><td></td></tr><tr><td>EVE Energy</td><td>64.4</td><td>CNY</td><td>20.6</td><td>19.0x</td><td>12.4x</td><td>0.7%</td><td>-2%</td><td>-11%</td><td>35%</td><td></td></tr><tr><td>Gotion</td><td>35.3</td><td>CNY</td><td>9.4</td><td>28.7x</td><td>8.5x</td><td>1.3%</td><td>-2%</td><td>-13%</td><td>36%</td><td></td></tr><tr><td>Sunwoda</td><td>24.5</td><td>CNY</td><td>6.7</td><td>17.5x</td><td>6.7x</td><td>0.6%</td><td>-3%</td><td>-17%</td><td>27%</td><td></td></tr><tr><td>Farasis</td><td>14.7</td><td>CNY</td><td>2.6</td><td>n.a.</td><td>n.a.</td><td>1.4%</td><td>10%</td><td>6%</td><td>13%</td><td></td></tr><tr><td colspan="11">Lithium Miners/Refiners</td></tr><tr><td>Albemarle</td><td>169.9</td><td>USD</td><td>20.0</td><td>15.4x</td><td>7.7x</td><td>-0.2%</td><td>-6%</td><td>-14%</td><td>193%</td><td></td></tr><tr><td>SQM</td><td>79.3</td><td>USD</td><td>21.8</td><td>13.4x</td><td>6.8x</td><td>-2.6%</td><td>-6%</td><td>-9%</td><td>138%</td><td></td></tr><tr><td>Pilbara Minerals</td><td>6.3</td><td>AUD</td><td>14.6</td><td>38.0x</td><td>18.8x</td><td>2.9%</td><td>5%</td><td>8%</td><td>368%</td><td></td></tr><tr><td>Ganfeng Lithium</td><td>68.2</td><td>HKD</

[中间内容因长度限制已省略]

 learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
