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
# Silicon carbide sector

# Updates on AI and auto applications - AI a positive factor but how meaningful?

We provide our latest thoughts on the SiC sector, based on our industry research. We believe the data center power supply build and upcoming architecture migration from AC to HVDC (high voltage direct current) are bringing positive developments to the SiC sector. Although AI is generating strong sentiments for SiC-related stocks, we caution that expectations shall remain grounded on the contribution level. We think data centers could contribute a \$400-500mn or fewer to the SiC device TAM in 2028 or outer years. As the SiC device TAM was already built up by EV and could reach \$4.0-4.5bn in 2026, we think data center contribution could rise from current LSD to MSD to HSD within two to three years. AI will be a critical driver for the SiC sector, but its contribution level to the SiC device TAM could fall short of the bullish camp's expectations of 20-30%, in our view.

- Data center SiC MOS - long lead time and high price. Our industry research indicates that the lead time for AI SiC MOS has increased to 52 weeks. Additionally, prices for AI SiC MOS (high spec ones) are now at least twice as high as those for auto inverter SiC MOS, when comparing identical die size and Rds(On) specs. This encouraging dynamic is driven by exceptionally strong and urgent orders from AI customers, while qualified production capacity is temporarily limited to meet the surge in demand. Looking ahead, we think price reductions for AI SiC MOS could be much smaller than in the auto market, despite more qualified capacity.   
- Data centers potentially \$400-500mn or fewer to the SiC device TAM in 2028 or outer years. The push towards higher rack power densities is forcing upgrades of data center power architecture from AC to HVDC, and SiC enables more efficient, compact conversion at both the infra level (UPS and SST) and the server level (PSU). Our industry research suggests 1MW HVDC data center power build could have SiC content value of \$5.0-6.0k or slightly higher, based on its power module topology and device price. JPM teams have forecast an 80GW AI data center power new installment in 2028, implying a \$400-480mn contribution to the SiC device TAM, if HVDC penetration is 100%. Yet, the data center SiC TAM shall be smaller than this range, considering the mix between AC and HVDC.   
- SiC device TAM already built up by EV; data center contribution potentially rising to MSD to HSD in 2028 or outer years. Although AI is generating strong sentiment for SiC-related stocks, we caution that expectations should remain grounded on the contribution level. The Yole Group forecasts (link) that the global SiC device TAM will grow from \~\$3.7bn in 2025 to \~\$4.6bn in 2026, up 25% YoY due mainly to the accelerating 800V migration in EVs. In our view, SiC is already benefiting significantly from EV adoption, and we think the global SiC device TAM could be \$4.0-4.5bn in 2026. Data center contribution to the SiC device TAM could grow from currently low single digits to mid-to-high-single digits two to three years out. We believe data centers will be a very important driver for the SiC sector, but we suspect its contribution level could fall short of the bullish camp's

# Technology

# Jimmy Huang AC

(886-2) 2725-9865

jimmy.huang@JPM.com

JPM Securities (Taiwan) Limited

# Akinori Kanemoto

(81-3) 6736 8628

akinori.kanemoto@JPM.com

JPM Securities Japan Co., Ltd.

# Gokul Hariharan

(852) 2800-8564

gokul.hariharan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

expectations of 20-30% (of the TAM).

- SiC substrate prices - 6" stabilized but 8" dropping. Prices for 6" SiC substrates have stabilized at \~Rmb1.5k since early 2026, vs Rmb3.0k in early 2025 and Rmb4.5k in early 2024. Some suppliers have shut down capacity given prices are below their production cash cost (Rmb1.5-2.0k, depending on scale). China's top 2 SiC substrate suppliers are operating at nearly full utilization rates for 6", but industry over-capacity prevents any meaningful price recovery. Prices for 8" SiC substrates have been in constant decline: \~Rmb7.0k in early 2025, Rmb5.5-6.0k in mid 2025, \~Rmb4.5k in early 2026 and \~Rmb4.0k in mid 2026. We expect 8" SiC substrate prices to further decline to Rmb 3.0-4.0k at end 2026 and Rmb2.5-3.5k in 2027. Customers request the pricing gap between 6" and 8" SiC substrates to be below 1.7x, based on wafer area difference. Even considering the production efficiency gain from 6" to 8", the price gap should be capped at 2.0x. Key triggers for the 8" price decline include improvements in yield and efficiency, as well as more effective supply from Chinese suppliers. The above prices are based on our industry research and refer to those offered by Chinese suppliers to large customers. A leading SiC substrate supplier talked about raising 8" prices. We believe it will be quite challenging to raise prices to major, important customers, if a supplier aims for market share. Our industry studies over the past four years and most recent industry discussions do not support the price hike expectation.   
- Auto inverter SiC MOS - ongoing price declines but increasing lead times. Prices for auto inverter SiC MOS also continue to decline rapidly in the China market. Prices from international IDMs could fall from \$6.0-6.5 in 2024 and \$5.0-5.5 in 2025 to \$3.0-3.5 in 2026 and potentially \$2.5 in 2027. Chinese suppliers could quote 15-30% lower, depending on product competency. On the positive side, lead time for auto SiC MOS has increased from 26 weeks (the basic manufacturing time) to 39 weeks, with some specs lengthening to 52 weeks, given the AI crowd-out effect. Pricing negotiation frequency has been reduced from quarterly to semi-annual for some cases, amid the lead time increase. However, whether prices for auto SiC MOS could stabilize into 2027 is not clear, as it depends on supply-side competition. If more Chinese SiC MOS suppliers are qualified for auto inverters, prices for SiC MOS will remain under pressure into 2027.   
- Fast-rising SiC penetration in China EVs. Ongoing SiC price declines drive SiC adoption to EV models priced \~Rmb150k. We think China's SiC EV shipments (excl. Tesla) reached 2.5mn units in 2025 and could rise to 4.0mn units or more in 2026, up 60% YoY or more. This would lift the SiC penetration rate from the mid-teens in 2025 to the low twenties in 2026. Additionally, SiC product iterations are improving on-resistance (Rds(On)), enabling a reduction in the number of SiC MOS dies per module in some EV models (i.e., 1200V modules from 48 to 42/36 dies, and 750V modules from 36 to 30/24 dies). Net-net, we believe the auto SiC device TAM will grow moderately in 2026.   
- Implications for A-share stocks. United Nova (UNT) is the leading Chinese supplier for SiC MOS, and it has mentioned the potential to increase SiC MOS (chip and module) revenue from Rmb1.5bn in 2025 to Rmb3.0bn in 2026 (implying a revenue mix of 18% and 28% in 2025 and 26) (JPM note). We believe UNT remains a key beneficiary of strong SiC MOS demand. UNT has sampled its 8” SiC MOS to an international AI server custoemr for qualification, which we believe is a CSP ASIC company. If UNT can pass qualification, we believe it would help ease the current supply tightness as UNT has mass production capabilities and UNT can ramp up more 8” SiC capacity in a timely manner. SICC is the most leading Chinese supplier for 6” and 8” SiC substrates and could benefit from increasing SiC adoption in datacenters and potentially advanced packaging in the mid to long term. SICC is ramping up its 8” SiC substrates meaningfully this year (i.e. potentially doubling YoY). However, we see continued pricing pressure for 8” SiC substrates through 2026 and we remain cautious on SICC stock, as we sense certain wrong expectations on SiC substrate pricing outlook.   
• Implications for Rohm (covered by Akinori Kanemoto). Against FY25 revenue of just

over JPY 40bn (JPM estimate; +14% YoY, with SiC devices/modules +41% YoY), the company is planning FY26 revenue of just under JPY 55bn (JPM estimate; +30% YoY, with devices/modules +55% YoY). In FY26, management plans to offset the loss of its external 6-inch wafer sales business with growth in device/module revenue. For xEV inverter applications, China accounts for more than half of FY25 sales, but toward FY28 the China mix is expected to decline while Japan/Korea/Europe/US increase. SiC MOSFETs for AI servers have already ramped in FY25, and the company plans to lift the revenue mix to 10% in FY26. On the technology front, mass production of 8-inch wafers is scheduled to start in FY26 - initially deployed in its 4th-generation platform, followed by the rollout of 5th-generation MOS to improve yields and productivity. Including the impact of the impairment taken at FY25 year-end, the company is targeting a return to profitability by FY28.

# Bookshelf – (China) SiC sector reports

- Sep 2025 - Silicon Carbide Sector - Our takes on CoWoS SiC carrier / thermal interface material; GlobalWafers at SEMICON Taiwan - Report link   
- Sep 2025 - Silicon Carbide Sector - News reports on CoWoS SiC interposer; we view this as only a concept and R&D direction, without further visibility - Report link   
- May 2025 - China Silicon Carbide Sector - Renesas abandons plan to produce SiC chips, with Chinese overproduction being one key reason - Report link   
- Apr 2025 - China Silicon Carbide Sector - Key takeaways from our SiC substrate expert call; solid SiC EV model pipeline at the Shanghai Auto Show - Report link   
- Apr 2025- China Silicon Carbide Sector - Increased competition; Updating views on substrates, device, equipment, applications and stocks - Report link   
- Dec 2024 - China Tech - Geopolitical dynamics on mature node semis: US Section 301 investigation and international IDMs' local-for-local strategies - Report link   
- Dec 2024 - China Silicon Carbide Sector - 2024 recap: A tough year for 6" substrates. 2025 outlook: Industry focusing on ramp of 8" substrates & auto SiC MOS; robust growth for China SiC EV - Report link   
- Nov 2024 - China Silicon Carbide Sector - Key takeaways from Axcelis 3Q24 earnings call; China SiC device capacity build dynamics - Report link   
- Nov 2024 - Silicon Carbide Sector - Recent industry dynamics on SiC/Si hybrid modules for EV inverters - Report link   
- Sept 2024 - Silicon Carbide Sector - 8" SiC partnership of Episil Tech and VIS - Report link   
- Aug 2024 - China Silicon Carbide Sector - Read-through from Silan Micro's 1H24 print and earnings call - Report link   
- Jul 2024 - China Silicon Carbide Sector - China auto market landscape and substrate/device 8" transition as focal points; better demand in 2H24 - Report link   
- Jun 2024 - China Silicon Carbide Sector - China auto SiC MOS: Hyper demand growth, rising competition and green shoots of localization - Report link   
- Jun 2024 - United Nova - Chinese leader in auto SiC MOS; Solid revenue growth but lingering profitability pressure; Initiate at Neutral - Report link   
- Mar 2024 - China Silicon Carbide Sector - China substrate competitive landscape updates from TanKeBlue and implications for SICC - Report link   
- Feb 2024 - China Silicon Carbide Sector - Post-CNY checks: ‘Materials’ a back-end loaded 2024 and initial sign of over-supply; implications for Device Equipment - Report link   
- Jan 2024 - China Silicon Carbide Sector - Chinese SiC epi maker EpiWorld IPO prospectus; implications for SICC and SiC industry - Report link   
- Nov 2023 - China Silicon Carbide Sector - On-the-ground checks and key themes for 2024 - Report link   
- Aug 2023 - China Silicon Carbide Sector - Implications from three global SiC power device makers' earnings calls - Report link   
- Jun 2023 - Silicon Carbide Sector - Our views on Chinese progress in substrates, device and equipment; OW SICC and Rohm - Report link

- Apr 2023 - Japan Electronic Components - Power semiconductor industry and position of Japanese manufacturers - Report link   
- Apr 2023 - Silicon Carbide Sector - Asian SiC foundries riding on strong market demand and localization benefits; HANA & Episil Tech - Report link   
- Feb 2023 - First Principles - Silicon Carbide: Key growth driver for European semi device makers - Report link   
- Feb 2023 - Networking & Hardware: The Silicon Carbide (SiC) Cheat Sheet - Report link   
- Feb 2023 - Silicon Carbide Deep Dive: Substrate and Asia focus; positive about the SiC sector and OW WOLF, COHR, Rohm and SICC - Report link   
- Feb 2023 - SICC - Initiate pure China SiC substrate play at OW, on TAM expansion, localization and power SiC ramp - Report link

Companies Discussed in This Report (all prices in this report as of market close on 25 May 2026, unless otherwise indicated) Rohm (6963)(6963.T/¥5,030/OW), United Nova - A(688469.SS/Rmb8.25/N)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

# Important Disclosures

• Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Rohm (6963), United Nova - A or related entities.   
- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of Rohm (6963) or related entities.   
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Rohm (6963) or related entities.   
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Rohm (6963) or related entities.   
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Rohm (6963) or related entities.   
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Rohm (6963) or related entities.   
• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Rohm (6963) or related entities.   
- Debt Position: JPM may hold a position in the debt securities of Rohm (6963), United Nova - A or related entities, if any.

Company-Specific Disclosur

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 25 May 2026 11:15 PM HKT

Disseminated 25 May 2026 11:15 PM HKT
"""
