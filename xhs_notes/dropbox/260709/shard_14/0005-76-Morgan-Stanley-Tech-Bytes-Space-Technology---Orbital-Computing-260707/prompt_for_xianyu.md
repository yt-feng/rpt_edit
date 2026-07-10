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
July 7, 2026 04:48 AM GMT

Tech Bytes | Europe

# Space Technology – Orbital Computing

Space technology offers a transformative solution by building compute capacity into space, leveraging abundant solar energy and radiative cooling. Advances in launch economics, thermal management, and power systems offer unique orbital infrastructure investment opportunities.

What is orbital compute? These are racks in space (not floating giant data centers) with solar arrays kept in a sun synchronous orbit and a cooling radiator behind it constantly in the shade. It is a virtual data centre where racks are linked using lasers travelling through vacuum, which are technologies widely used in modern satellites. These platforms can drive higher cost efficiencies, alleviate terrestrial constraints, reduce environmental impact, and enable new capabilities for latency-sensitive and security-critical applications.

Why put data centers in space? Nearly half of today's cost of building a 1GW AI data center is spent on infrastructure, rather than compute. As reusable launch continues to drive costs lower, orbital platforms could replace a significant portion of this terrestrial infrastructure with solar-powered systems in space, potentially bringing orbital compute economics closer to terrestrial AI infrastructure over time. The space economy is poised to reach US\$1.8tr by 2035e, according to World Economic Forum, led by the next generation of satellite networks developed by companies like SpaceX's Starlink, Amazon's Kuiper, Eutelsat's OneWeb, and China's Guowang exploring a space-based scalable AI infrastructure.

The space technology supply chain is a highly specialized ecosystem combining new compute architectures suited to the space environment with a mechanical design in which solar power collection, compute, and thermal management are tightly integrated. Its commercial mega-constellations and reusable rocket technology operates at the intersection of semiconductors, communications, aerospace, defense, and advanced AI infrastructure.

Investment implications. We curated a list of tech companies at the forefront of space technology, leading in innovation and market presence. Building orbital compute takes a tremendous amount of radiation-tested components with most of the value in (1) optical/RF, (2) power/cooling and (3) semiconductor chips. In Europe, we favour STMicro and Infineon as companies providing these enabling technologies and which stand to benefit; understanding which capabilities are advancing fastest, ecosystem readiness and adoption timelines will dictate commercial traction.

MS & CO. INTERNATIONAL PLC+

Shawn Kim
Equity Analyst
Shawn.Kim@morganstanley.com +44 20 7677-1018

MS & CO. LLC
Adam Jonas, CFA
Equity Analyst
Adam.Jonas@morganstanley.com +1 212 761-1726

MS & CO. INTERNATIONAL PLC+
Cindy Huang
Equity Analyst
Cindy.Huang@morganstanley.com +44 20 7425-2915

MS & CO. LLC
William Tackett, CFA
Research Associate
William.Tackett@morganstanley.com +1 212 761-6028

MS & CO. INTERNATIONAL PLC+

Lee Simpson
Equity Analyst
Lee.Simpson@morganstanley.com +44 20 7425-3378

Nigel van Putten
Equity Analyst
Nigel.Putten@morganstanley.com +44 20 7425-2803

Research Associate
Amelia.Scicluna@morganstanley.com +44 20 7425-6694

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Executive summary

Orbital compute is an emerging AI infrastructure theme at the intersection of semiconductors, satellite systems, launch, thermal management, optical communications and autonomous operations. We do not expect it to replace terrestrial hyperscale data centers this cycle. The more realistic near-term opportunity is orbital edge AI: satellites process imagery, sensor data and inference workloads in orbit before sending only useful outputs back to Earth. The longer-term bull case is a distributed AI infrastructure layer in space.

Why now? Four structural trends are making orbital compute increasingly credible. AI data centers are running into power, land, water and permitting constraints; reusable launch is reducing the cost of putting mass into orbit; optical satellite networking is evolving toward distributed compute architectures; and the volume of space-generated data continues to grow. Together, these trends strengthen the case for processing some workloads in orbit. However, orbital compute does not eliminate infrastructure constraints; it replaces terrestrial bottlenecks with new engineering challenges around launch cost, thermal management, radiation tolerance, optical bandwidth, orbital debris and autonomous operations.

Exhibit 1: Potential Benefits and Key Challenges

<table><tr><td>Potential Benefits</td><td>Rationale</td><td>Key Challenges</td><td>Rationale</td></tr><tr><td>Power</td><td>Near-continuous solar exposure in dawn-dusk SSO; no terrestrial grid constraints.</td><td>Radiation</td><td>Requires radiation-tolerant chips, ECC and shielding.</td></tr><tr><td>Thermal</td><td>No air or water cooling, but heat must still be rejected via heat pipes and radiators.</td><td>Repair / Refresh</td><td>On-orbit maintenance is difficult; AI hardware refresh cycles are short.</td></tr><tr><td>Latency</td><td>LEO enables low-latency connectivity (~10–30 ms RTT).</td><td>Optical networking</td><td>AI-scale distributed compute needs far higher inter-satellite bandwidth than today&#x27;s satellite networks.</td></tr><tr><td>Scalability</td><td>Reusable launch vehicles could lower deployment cost over time.</td><td>Orbital debris / security</td><td>Collision avoidance, cyber risk and physical protection become core operating requirements.</td></tr></table>

Source: MS

Where we are today? Orbital compute remains in the early stages, but it is no longer only a research concept. SpaceX Starmind is the clearest public blueprint for a scalable orbital AI infrastructure system, while Starcloud and NVIDIA are exploring compute hardware, orbital platforms and space-native AI workloads. China is also moving from concept to deployment: Adaspace reportedly launched the first 12 satellites of its “Three-Body Computing Constellation” in May 2025, with a stated long-term plan for 2,800 satellites and onboard AI processing. The near-term commercial use case remains orbital edge AI – processing satellite imagery, sensor data and inference workloads in orbit – while large-scale, space-based AI infrastructure remains a longer-term option.

Economics: We use SpaceX initiation estimates as the economics benchmark and frame orbital compute around cost per watt. In orbit, terrestrial power, land and water constraints are replaced by launch cost, satellite hardware, solar arrays, radiators, radiation tolerance and autonomous operations. Our Embodied AI/Robotics team, led by Adam Jonas, provides the most detailed benchmark: orbital compute capex/W is modeled to decline from roughly US\$60/W in 2030 to US\$32/W in 2031, US\$15/W in 2035 and US \$9/W by 2040, driven by lower launch cost, cheaper satellite hardware and improved

compute payload economics. On a five-year useful-life basis, the 2031 estimate implies roughly US\$6.5/W/year, close to the current industry Blackwell benchmark of US\$6.8/W/year. For details, please see the SpaceX initiation – “AI’s Final Frontier”.

## Stock implications

Orbital compute extends the existing AI hardware stack where additional technologies are required to enable reliable performance in space.

\- The key investment exposure sits in RF / phased-array hardware (STM, Qorvo and Amphenol), optical connectivity (Coherent/Lumentum), and power and thermal systems (GS Yuasa, Lite-On and LG Energy Solution), which form the enabling layer around the core compute payload.

\- In parallel, Infineon, Analog Devices, Microchip and Shanghai Fudan provide radiation-tolerant, high-reliability semiconductors essential for stable operation in orbit, with Infineon positioned in space-grade power management.

\- Core AI silicon remains necessary for compute payloads (NVIDIA, AMD – AMD Versal AI Core adaptive system-on-chips (SoCs) in satellites to handle critical AI processing and wireless data acceleration; Broadcom, Micron, TSMC, SK hynix and Samsung – developed specialized Exynos modem chips (Exynos 5400) that use machine learning to optimize communication with low Earth orbit satellites, particularly for their Direct to Cell networks).

Within our European Semiconductors coverage, both STMicroelectronics and Infineon stand out as key enablers. Both are key suppliers of radiation-hardened semis that are essential for power management ICs, flight computers, memory for critical systems, FPGAs controlling the spacecraft and communications and attitude-control electronics – for instance, rad hard power MOSFETs, solid state relays and space shottky diodes. STMicro recently held a specific low Earth orbit event providing more granular detail on technology positioning and the bill of materials (see our note, LEO opportunity enters orbit). The company is guiding to "well above US\$3bn cumulative sales over the next 3 years" and separates the LEO opportunity into 3 brackets: (i) Broadband, (ii) direct-to-cell and (iii) orbital data centre. User terminals were highlighted by management as the largest revenue contributor, with the company calling out its BiCMOS technology and PLP (panel level packaging) as enabling competitiveness in user terminal front-end modules. We model user terminals, satellite and gateway sales separately, estimating US\$546mn user terminal sales in FY26, 67% of LEO sales. All in, we see STM's LEO sales ramping from US \$815mn FY26 to US\$1.8bn FY28. Our sense is that this could be conservative, as satellite launches may ramp at a larger size than we are modelling, especially as more new players enter the market.

Exhibit 2: Orbital compute technology supply chain

<table><tr><td>Company</td><td>Ticker</td><td>Region</td><td>Rating</td><td>Last Close (LC)</td><td>Market Cap ($mn)</td><td>Key orbital read-through</td></tr><tr><td colspan="7">1. Al silicon, memory &amp; custom compute</td></tr><tr><td>NVIDIA</td><td>NVDA</td><td>US</td><td>OW</td><td>195</td><td>4,714,886</td><td>Space 1 / Vera Rubin, Jetson Otrn and IGX Thor make NVIDIA, the default orbital Al accelerator reference.</td></tr><tr><td>AMD</td><td>AMD</td><td>US</td><td>EW</td><td>518</td><td>844,357</td><td>Space-grade Versal adaptive SoCo and data acceleration for onboard processing payloads.</td></tr><tr><td>Cioadcom</td><td>AVGO</td><td>US</td><td>OW</td><td>360</td><td>1,714,870</td><td>Custom silicon and networking read-through for Al payloads, ground gateways and high-bandwidth systems.</td></tr><tr><td>Micron</td><td>MU</td><td>US</td><td>OW</td><td>976</td><td>1,101,788</td><td>HBM / DRAM supply exposure for Al compute payloads and resilient orbital memory.</td></tr><tr><td>TSMC</td><td>2330 TT</td><td>Taiwan</td><td>OW</td><td>2,445</td><td>1,982,637</td><td>Leading edge foundy for orbital Al silicon; any scaled compute layer ultimately depends on advanced logic supply.</td></tr><tr><td>SK hynix</td><td>000660 KS</td><td>Korea</td><td>OW</td><td>2,425,000</td><td>1,123,802</td><td>HBM is a binding constraint for any gigawatt-scale deployed compute architecture.</td></tr><tr><td>Samsung Electronics</td><td>005930 KS</td><td>Korea</td><td>OW</td><td>309,500</td><td>1,317,860</td><td>HBM / DRAM exposure; additional satellite communications optionally through modem / RF ecosystem.</td></tr><tr><td colspan="7">2. High-reliability components, PCBs, passives &amp; system integration</td></tr><tr><td>Murata</td><td>6981 JP</td><td>Japan</td><td>OW</td><td>11,080</td><td>125,051</td><td>Space-grade MLCC leader; high-reliability passives for satellites, power modules and payload electronics.</td></tr><tr><td>Taiyo Yuden</td><td>6976 JP</td><td>Japan</td><td>UW</td><td>20,560</td><td>15,953</td><td>High-reliability MLCCs and passive components for harsh-environment electronics.</td></tr><tr><td>TDK</td><td>6762 JP</td><td>Japan</td><td>OW</td><td>3,699</td><td>43,533</td><td>Passives and electronic components for space, power and satellite systems.</td></tr><tr><td>Samsung Electronics</td><td>6787 JP</td><td>Japan</td><td>EW</td><td>29,330</td><td>4,666</td><td>Strong market position in PCB antennas for LED satellite communication receivable antennas, and could potentially expand into satellite-grade PCB</td></tr><tr><td>Samsung Electro-Mechanics</td><td>009150 KS</td><td>Korea</td><td>OW</td><td>1,989,000</td><td>98,314</td><td>MLCC / substrates exposure for satellite electronics and power modules.</td></tr><tr><td>TTM Technologies</td><td>TTM</td><td>US</td><td>NC</td><td>156</td><td>16,199</td><td>PCBs for high-reliability aerospace, defense and compute payload electronics.</td></tr><tr><td>Hon Hai</td><td>2317 TT</td><td>Taiwan</td><td>OW</td><td>241</td><td>105,488</td><td>EMS / system-integration optionality plus direct LED satellite communications hardware validation through Foxconn PEARL satellites.</td></tr><tr><td>Compeq</td><td>2313 TT</td><td>Taiwan</td><td>NC</td><td>230</td><td>8,794</td><td>Advanced PCB exposure to SpaceX satellite, ground receiving stations and terminals.</td></tr><tr><td>Unitech</td><td>2367 TT</td><td>Taiwan</td><td>NC</td><td>55</td><td>1,215</td><td>Advanced PCB exposure to SpaceX user terminals/ground stations.</td></tr><tr><td colspan="7">3. Optical links, photonics &amp; terminals</td></tr><tr><td>Coherent</td><td>COHR</td><td>US</td><td>EW</td><td>333</td><td>65,218</td><td>Laser optics and photonics read-through for optical inter-satellite links and ground optical systems.</td></tr><tr><td>Lumentum</td><td>LITE</td><td>US</td><td>EW</td><td>728</td><td>56,663</td><td>Laser optics and photonics exposure to high-bandwidth optical networking.</td></tr><tr><td>CACI</td><td>CACI</td><td>US</td><td>NC</td><td>503</td><td>11,108</td><td>Optical communications terminals and space communications systems; closer to the orbital laser-link bottleneck than generic IT services.</td></tr><tr><td>Eqptolink</td><td>30050Z CH</td><td>China</td><td>OW</td><td>526</td><td>108,158</td><td>Optical transceiver read-through for high-bandwidth orbital networking.</td></tr><tr><td colspan="7">4. IR, phased-array terminals &amp; satellite communications hardware</td></tr><tr><td>STMicroelectronics</td><td>STM</td><td>Europe</td><td>NC</td><td>68</td><td>60,749</td><td>RF front-end / BICMOS and space-grade electronics exposure for Starlink-style phased-array antennas, LEO terminals and satellite communications.</td></tr><tr><td>Filtric</td><td>FTC LN</td><td>Europe</td><td>NC</td><td>2</td><td>699</td><td>High-frequency Solid State Power Amplifiers (SSPaAs) installed in ground status...</td></tr><tr><td>Gilat Satellite Networks</td><td>GILT</td><td>Israel / US</td><td>NC</td><td>13</td><td>974</td><td>Ground systems and satellite communications terminal exposure.</td></tr><tr><td>Qorvo</td><td>QRVO</td><td>US</td><td>EW</td><td>88</td><td>7,725</td><td>RF products and semis for satellite communications and phased-array systems.</td></tr><tr><td>Amphenol</td><td>APH</td><td>US</td><td>NC</td><td>165</td><td>202,484</td><td>High-reliability con

[中间内容因长度限制已省略]

 herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
