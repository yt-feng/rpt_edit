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
# US Autos, Auto Parts and Auto-tech

# 800V: From EV to DC (and BESS)

Seeking auto companies with non-auto opportunities. Investors continue to search for AI data center (AIDC) and battery energy storage systems (BESS) exposure. Auto companies may offer unique ways to gain exposure and screen less expensive than other industrial AI names. While other industrial companies have a larger exposure today and meaningful orders/backlogs, auto companies have capabilities and emerging opportunities, particularly around 800V. These opportunities are nearly 100% incremental. As we wrote in early May, auto companies have deep specialization skills (many with relevance to other areas), run lean manufacturing, and manage complex supply chains. These skills can lead to opportunities in energy generation/storage, robotics and space. Modine holds the light for the auto to industrial "transition dream".

Party like it's 2018? The amount of new group interest on AI exposure from auto and non-auto investors hasn't been this high since 2018, near the peak of AV/EV mania. The difference could be that EVs demand were dependent on consumer adoption, regulation and tech that was further out whereas AIDC/BESS is based on real demand and economic return. While BWA and F have been the poster children within auto for what could be and still get interest, the next most common question is: who's next? In this note, we take a deep look at each company's portfolio and their applicability towards 800V AIDC and BESS. In our view, BWA, APTV and ST seem best positioned. BWA already announced their TurboCell product, BESS and a bi-directional microgrid inverter. But we also see other inverter/converter potential. Further, while it may be difficult and likely require investment, they also have capabilities needed for solid-state transformers (SSTs). APTV has competencies in HV connectors and busbars, which could make the market more comfortable with their $8 - 10\%$ non-auto annual growth target. While APH and TEL should also benefit from higher power connectors content, they already have some AI power content (whereas we believe it's nearly all incremental for APTV), and APH/TEL may lose content on the copper data connector side (APTV no presence). ST can get more sensor content as AIDCs move from air to liquid cooled, but ST also has contactors for 800V EVs that can be used for new 800V applications.

800V presents interesting opportunities. Recall, the tech path for BEVs was to move to 800V (from mostly 400V), so suppliers invested in tech particularly around power electronics. Suppliers already manage complex supply chains and know how to manufacture at scale with high tolerances. That becomes important because next-gen AIDCs are switching to 800V, changing the electrical infrastructure. As GPU clusters increase in density, the shift to 800V becomes necessary for physics, thermal, efficiency, cost and footprint reasons. This opens up an opportunity for auto suppliers with capabilities in areas such as inverters/converters, high voltage power connectors and busbars, among others. Further, there are also 800V opportunities on BESS.

Capabilities + opportunity + inexpensive valuations = suppliers getting a look. It's clear that data center capex and BESS demand are growing. UBS Evidence Lab analysis (>Access Dataset) shows 181 GW of global data center power capacity that is planned or under construction in addition to the 121 GW in operation today. Globally, UBS estimates BESS demand will grow from \~334GWh in 2025 to \~1.6TWh in 2030. The TAM for some products we mention in this report is unclear because the 800V DC is still very early stage development and architectures can vary/evolve over time. For certain key products, we do make (admittedly wide range) estimates, but for now, we see value in identifying products that can find new use cases. In an industry that has been viewed as growth challenged, the hope for a new growth avenue could cause a re-rating (e.g. BWA and F). Inside, please find our detailed portfolio review of APTV, BWA, DAN, LEA, MGA, PHIN, ST, VC, VGNT, QS.

# Equities

Americas

Automobiles

Joseph Spak, CFA

Analyst

joseph.spak@ubs.com

+1-212-713 3089

Robert Saltzman

Analyst

robert.saltzman@ubs.com

+1-212-713 2992

Gabriel Gonzales, CFA

Associate Analyst

gabriel.gonzales@ubs.com

+1-212-713 4866

Alejandro Nuno

Associate Analyst

alejandro.nuno@ubs.com

+1-212-713 3886

# 800V opportunities in new end markets

If 800V sounds familiar to auto investors, it should. The voltage was what BEVs were thought to (and what many still will) evolve to, even if most mass market vehicles are still 400V today. As such, the automotive supply chain has built up capabilities to support 800V. That may make them well positioned to benefit from other 800V use cases such as in the AI data center (AIDC) but also in battery energy storage systems (BESS).

800V distribution in AIDC vs. traditional architectures: As computing power steps up for next-generation AI data centers, power architecture is shifting toward 800V (800VDC). Traditional data centers move electricity through a complex chain where power arrives as alternating current (AC) is converted multiple times, and is delivered at lower voltages (higher current), requiring thicker cables, generating more heat, and losing energy along the way. In contrast, an 800V architecture simplifies this flow. Electricity still comes from the grid as AC, but it's converted early into high-voltage (direct current) DC using large AC/DC inverters (rectifiers) or, in advanced designs, solid-state transformers (SSTs) that can directly produce DC.

This high-voltage DC (lower current) is then distributed efficiently across the facility using busbars, high-voltage wiring, and specialized connectors, essentially heavy-duty pathways that move large amounts of power, while high-voltage contactors act as smart switches to safely control and protect the flow. Near the servers, the voltage is stepped down to a lower level (utilizing DC-DC converters) for use by the equipment. Because the power travels at a higher voltage, it needs less current to deliver the same energy, which reduces heat, allows for smaller cables, and enables denser compute hardware. In simple terms, the newer system replaces a multi-step, inefficient delivery process with a more direct and streamlined path that gets more usable power to the rack. Some opportunities we see with the shift to 800V:

- With power distributed as high-voltage DC, the role of AC/DC conversion (inverters) is centralized (now only on grid edge), and distribution within the data center relies more heavily on high-efficiency DC-DC converters to step voltage down closer to the usable load (companies like BWA have inverter and converter capability).   
- Legacy connectors designed for lower voltage and simpler power profiles must be replaced with high voltage connectors that can manage greater electrical stress and optimize efficiency (APTV has high voltage connectors and busbars for EVs and the capabilities seem portable).   
- Greater compute density drives higher thermal loads, which drives the need for stronger, liquid-cooled HVAC solutions. Within these systems, pressure, temperature, and flow sensors become critical components to monitor operations. 800V contactors are needed (ST can participate).

While adoption is currently quite limited, major hyperscalers have indicated the necessity for data centers to transform architectures given compute/power requirements. For instance, NVIDIA has indicated 800 volts direct current (VDC) will be "the essential foundation for the next generation of intelligence". They expect an initial rollout of 800V architecture will coincide with next-gen rack-scale systems (Kyber) in 2027 and acceleration of adoption late decade.

Note, the architecture is still in its nascent stages, so while what we detailed above is a reasonable way the architecture could evolve, a lot can still change.

800V in BESS: In traditional BESS, stored battery power is repeatedly converted between DC and AC through centralized uninterrupted power supply (UPS) and inverter systems, adding complexity and energy loss. In contrast, 800V architectures keep power in high-voltage DC form for longer, allowing batteries to deliver energy more directly with fewer conversions, improving efficiency and reducing system size. As a result, there is reduced reliance on multiple conversion stages and centralized backup systems, while new components like high-voltage battery packs and DC-native power electronics replace them, making systems more efficient and scalable.

Conceptually, many auto companies have a legitimate entry point into 800V in both areas given their early leadership and expertise in 800V EV architectures, where they have already developed capabilities and their ability to industrialize, manufacture, manage supply chains and produce to a higher quality standard (they had to learn to produce to "auto grade"). We don't see a lack of technical capability, but there of course needs to be some investment and understanding of how to translate their expertise to new end-markets as well as a sales effort. But, net we believe there are auto companies with the 800V know-how that are well positioned to extended into 800V infrastructure as architectures converge.

In this note, we walk through each company's portfolio to evaluate how and if they have a right to participate in these new markets. That said, 800VDC is still very early stage/development and pre-mass deployment. It will also likely evolve over time. This does make TAM estimates difficult. We will continue to do work here on the potential opportunity, but the important piece for now is that anything these companies get is incremental, a new growth avenue, and potentially tied to a less cyclical market.

Figure 1: Summary of Capabilities by Company 

<table><tr><td></td><td>APTV</td><td>BWA</td><td>DAN</td><td>LEA</td><td>MGA</td><td>PHIN</td><td>ST</td><td>VC</td><td>VGNT</td><td>QS</td></tr><tr><td>Battery Backup Units (BBUs)</td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Battery Disconnect Units (BDUs)</td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Battery Enclosure Systems</td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Battery Management Systems (BMS)</td><td></td><td>●</td><td>●</td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td></tr><tr><td>Bidirectional DC Fast Chargers</td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Busbars</td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Circuit Breakers</td><td>●</td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td></tr><tr><td>Cooling Plates</td><td></td><td>●</td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Generator Battery Solutions (GBS)</td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>High-Energy Battery Systems</td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>High-Pressure Diesel Fuel Injection Systems</td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td><td></td></tr><tr><td>High-Voltage Connectors</td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>High-Voltage Contactors</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td></tr><tr><td>High-Voltage Coolant Heaters (HVCH)</td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>High-Voltage DC/DC Converters</td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td></tr><tr><td>High-Voltage Fuses</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td></tr><tr><td>High-Voltage Inverters</td><td></td><td>●</td><td>●</td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>High-Voltage Power Distribution Units (PDUs)</td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td></tr><tr><td>High-Voltage Wire Harnesses</td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td><td></td><td>●</td><td></td></tr><tr><td>Insulation Monitoring Devices (IMDs)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td></tr><tr><td>Onboard Battery Chargers (OBCs)</td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td></tr><tr><td>Pressure, Temperature, and Flow Sensors</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td></tr><tr><td>Signal and Data Wire Harnesses</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td></tr><tr><td>Smart Battery Junction Box</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td></tr><tr><td>Smart Fuse Boxes</td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Solid-State Battery</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td></tr><tr><td>Turbine Generator</td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Uninterruptible Power Supply (UPS)</td><td></td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company websites, UBSe

# Framing high level BESS and AIDC market opportunities

While many of the products discussed in this report, as they relate to BESS and AI data center applications, are highly specialized, we note that sizing the individual total addressable market (TAM) for every product remains inherently difficult. First, we outline below our estimates for the broader TAM across both AI data centers and BESS over time, which we believe better illustrates the overall market opportunity available for automotive suppliers seeking to expand into these adjacencies.

AI Data Center: UBS Evidence Lab analysis shows 181 GW of global data center power capacity that is planned or under construction in addition to the 121 GW of power capacity in operation today. However, we believe the opportunity for auto companies is more limited in China. That said, UBS Evidence Lab still shows 172 GW of global ex-China data center power capacity planned or under construction.

Figure 2: UBS Evidence Lab's monitor of Global Data Centers shows 181 GW of capacity that is planned or under construction   
![](images/1b85170f545e58db83018f5232ea14d823831403d372929bb13cea994837e4d2.jpg)

<details>
<summary>bar</summary>

Global Data Center Capacity (GW)
| Category | 31-Mar-24 | 30-Jun-24 | 30-Sep-24 | 31-Dec-24 | 31-Mar-25 | 30-Jun-25 | 30-Sep-25 | 31-Dec-25 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Operational | 76 | 80 | 84 | 93 | 99 | 108 | 113 | 121 |
| Under Construction | 22 | 21 | 21 | 22 | 25 | 26 | 30 | 35 |
| Planned | 61 | 64 | 79 | 76 | 77 | 96 | 129 | 146 |
</details>

Source: UBS Evidence Lab, includes content supplied by S&P Global; Copyright © S&P Global Market Intelligence 2025. All rights reserved (>Access Dataset). Note: Facilities are considered 'under construction' if they are expected to become operational within a year. Facilities labeled 

[中间内容因长度限制已省略]

legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/4d62d32ca05b9729e2d90a5cc438c16d97c2ffd53922f522855669d87513ddb2.jpg)
"""
