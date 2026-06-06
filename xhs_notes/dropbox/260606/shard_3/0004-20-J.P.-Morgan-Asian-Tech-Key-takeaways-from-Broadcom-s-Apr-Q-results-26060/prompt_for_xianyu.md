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
## Asian Tech

Key takeaways from Broadcom's Apr-Q results

\- 2H26 AI revenue double versus 1H and to surpass \$100bn in FY27: Broadcom's AI revenue reached \$10.8bn in 2Q26, up 143% YoY and representing 49% of total revenue. Management guided for 2H AI revenue to double versus 1H, implying FY26 AI semiconductor revenue of \~US\$56bn, and reiterated its FY27 target of exceeding US\$100bn, with further substantial growth into FY28. On program cadence, management highlighted multi-year, multi-GW ramps across Google (multi-generation TPUs plus AI networking under a long-term agreement), Anthropic (additional TPU-based compute beginning 2027), OpenAI (production in late 2026 with contractual deployments in 2027), and Meta (MTIA XPU partnership; initial 1GW order with deliveries starting 2H27). Management also referenced another two customers (ByteDance and SoftBank/ARM, based on our supply chain checks) with shipments starting in late 2026 and accelerating into 2027, with purchase orders to date cited at \~US\$6bn. Broadcom's lack of numerical upside to 2027 guidance, while TPU ests have moved up and Mediatek pulling in its ASIC guidance ahead by a year is likely to be seen as a concession of meaningful share loss within the TPU program, in our view.

\- TPU supply diversification acknowledged by the management; positive for Mediatek: Management acknowledged that, despite a very substantial long-term commitment under the Google agreement, Google is likely to maintain some diversity of sources for its TPU/AI compute stack. This is consistent with MediaTek's collaboration with Google on TPU (v8t Zebrafish and upcoming v9 Humufish) and the potential for Marvell to cooperate with Google on an LPU-like chip. Longer term, we believe it could become the norm for large CSPs to engage 2–3 back-end design service vendors, driven by: (1) a broader set of product types (AI accelerators, AI CPUs, LPU-like, etc.); and (2) customers experimenting with different commercial structures (e.g., semi-CoT vs. full CoT) as their front-end design capabilities mature. In this context, we see MediaTek and Alchip as key potential beneficiaries as CSPs move towards CoT / semi-CoT models, given their structurally lower margin profiles (40%+/teens% GM for MediaTek/ Alchip) versus turnkey service vendors with front-end design services (60+% GM).

\- AI bookings >\$30bn; visibility extended into 2028: Management disclosed AI semiconductor bookings of over US\$30bn in the quarter, noting customers are pulling orders forward due to long lead times—not only for wafers and memory (HBM/DRAM), but also for power readiness. Importantly, management said visibility now extends into 2028, adding that Broadcom is comfortable securing supply for 2026–27 and is already working on 2028–29. This aligns with our Asia supply-chain checks that 3–5Y LTAs are increasingly in place across key bottlenecks such as substrates, HBM, and CCL, while leading-edge wafers still remain on annual negotiation cycles. We therefore have higher confidence that key supply constraints could persist through 2027 and potentially into 2028. Key beneficiaries, in our view, will be TSMC, ASE, SK Hynix, Samsung, Unimicron, Ibiden, and EMC.

## Technology and Telecoms

## Gokul Hariharan AC

(852) 2800-8564

gokul.hariharan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Jennifer Hsieh

(886-2) 2725-9868

jennifer.hsieh@JPM.com

JPM Securities (Taiwan) Limited

## David Chou

(886-2) 2725-9618

david.chou@JPM.com

JPM Securities (Taiwan) Limited

## Jason Chen

(886-2) 2725-9864

jason.bh.chen@JPM.com

JPM Securities (Taiwan) Limited

## Subham Singhania

(91-22) 6157-3801

subham.singhania@JPM.com

JPM India Private Limited

\- Strong Networking performance (now \~40% of AI revenue): Networking/interconnect is a key theme at 2026 Computex Taipei (June 2-5), supported by strong demand for high-bandwidth data transmission as agentic AI drives larger scale-up, scale-out domains. Broadcom indicated networking represented nearly 40% of 2Q AI revenue, reflecting strong attach of switching/SerDes/connectivity content across both its custom XPU and non-XPU products. That said, management suggested the \~40% mix is likely elevated and could normalize closer to \~30% over time as XPUs ramp faster in the next few quarters. On products, management emphasized leadership in scale-up copper/SerDes and switching, including over 1 year shipments of the 100Tb Ethernet switch (Tomahawk 6), and highlighted optics/CPO building blocks (1.6T DSPs, CW/EML lasers) positioning Broadcom as the industry standard. Management also noted that the next-generation 200Tb switch is planned to tape out this quarter. We expect networking to remain an increasingly important investor focus. While CPO is a key long-term topic as copper approaches its limits, Broadcom appears to be still more conservative on CPO ramp, aligned with the ramp schedule for ASIC customers (likely two years later than NVDA, in our view).

\- Non-AI semi improving; margins are mix-driven while operating leverage holds: Outside AI, management highlighted non-AI semiconductor revenue of US\$4.2bn (+6% YoY) and bookings above US\$6bn as early signs of a cyclical recovery, and guided for 3Q non-AI semiconductor revenue to improve sequentially to \~US\$4.5bn (+12% YoY). Our Asia supply-chain checks echo Broadcom's commentary, with mainstream seeing some momentum supported by: (1) a gradual recovery in auto and industrial; (2) an AI crowd-out effect that is tightening capacity in mainstream; and (3) rising AI-adjacent demand (e.g., PMIC). We believe the latter two drivers could support stronger momentum as pricing improves under tighter S/D, benefiting mature foundries such as VIS, OSATs such as ASE, and passive component vendors such as YAGEO and Murata.

Broadcom (AVGO US, OW) is covered by JPM US analyst Harlan Sur:

Companies Discussed in This Report (all prices in this report as of market close on 04 June 2026, unless otherwise indicated) ASE Technology Holding Co Ltd(3711.TW/NT\$593.00/OW), Alchip Technologies(3661.TW/NT\$4,340.00/OW), Broadcom Inc(AVGO/\$479.23[03 June 2026]/OW), Elite Material Co(2383.TW/NT\$4,830.00/OW), Ibiden (4062)(4062.T/¥21,940[03 June 2026]/OW), MediaTek Inc.(2454.TW/NT\$4,430.00/OW), Murata Manufacturing (6981)(6981.T/¥10,420[03 June 2026]/OW), SK hynix(000660.KS/W2,295,000/OW), Samsung Electronics(005930.KS/W355,500/OW), TSMC(2330.TW/NT\$2,385.00/OW), Unimicron(3037.TW/NT\$971.00/OW), Vanguard International Semiconductor Corp.(5347.TWO/NT\$163.00/OW), YAGEO(2327.TW/NT\$743.00/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Ibiden (4062), Murata Manufacturing (6981), Samsung Electronics, SK hynix or related entities.  
- Manager or Co-manager: JPM acted as manager or co-manager in a public offering of securities or financial instruments (as such term is defined in Directive 2014/65/EU) of/for Samsung Electronics or related entities within the past 12 months.  
- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of Ibiden (4062), Samsung Electronics, SK hynix or related entities.  
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Ibiden (4062), Murata Manufacturing (6981), Samsung Electronics, SK hynix or related entities.  
- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: Samsung Electronics or related entities.  
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Ibiden (4062), Murata Manufacturing (6981), Samsung Electronics, SK hynix or related entities.  
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Samsung Electronics, SK hynix or related entities.  
- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from Samsung Electronics or related entities.  
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Ibiden (4062), Murata Manufacturing (6981), Samsung Electronics, SK hynix or related entities.  
• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Ibiden (4062), Murata Manufacturing (6981), Samsung Electronics, SK hynix or related entities.  
- Debt Position: JPM may hold a position in the debt securities of Ibiden (4062), Murata Manufacturing (6981), Samsung Electronics, SK hynix or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the

Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Hariharan, Gokul : ASE Technology Holding Co Ltd (3711.TW), ASMPT Ltd (0522) (0522.HK), Alchip Technologies (3661.TW), Chipbond Technology (6147.TWO), GDS Holdings (GDS), GUC (3443.TW), Hon Hai Precision (2317.TW), MediaTek Inc. (2454.TW), Novatek Microelectronics Corp. (3034.TW), Powerchip Semiconductor Manufacturing Corp. (6770.TWO), SMIC (0981) (0981.HK), Silicon Motion (SIMO), TSMC (2330.TW), UMC (2303.TW), Vanguard International Semiconductor Corp. (5347.TWO), Xiaomi (1810) (1810.HK)

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to $100\%$ because of rounding.  
\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation:The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accura

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 04 Jun 2026 02:41 PM HKT

Disseminated 04 Jun 2026 02:41 PM HKT
"""
