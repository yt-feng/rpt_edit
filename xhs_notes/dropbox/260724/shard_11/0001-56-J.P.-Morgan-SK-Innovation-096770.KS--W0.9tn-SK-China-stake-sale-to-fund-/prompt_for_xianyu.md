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
## SK Innovation

W0.9tn SK China stake sale to fund growing AI energy demand? ROE on track to reach 9yr high on lubricant/refining strength; stay OW

We see SK Inno's reported W0.9tn SK China stake sale as further affirmation of the company's commitment to continue downsizing its non-core assets and free up cash for shareholder returns and AI-centric growth. Local media cited the potential for SK Innovation to participate in the power infrastructure buildout linked to the Honam semiconductor fab (link), though this remains unverified by the company. SK Inno has underperformed Asia energy peers over the past five years (Figure 6) due to an EV battery drag, and we see potential for the company to catch up after its battery “rightsizing” and pivot to become SK group's AI energy provider. We forecast strong 2Q OP of W1.8tn (BBGe W1tn), with SK Inno likely delivering the highest NP to shareholders among the K-battery trio in FY26-27. Reiterate OW.

\- What's new: According to local media reports on 21 July, SK Inno will receive W0.9tn from the sale of its 20% stake in SK China. SK China is the entity overseeing SK Group's business in China, comprising mostly non-core operations including real estate, logistics and venture investments. SK Inno and its subsidiaries currently hold a total 33% stake in SK China (SK Inno 21.7%, SK Geocentric 9.5%, SK Energy 1%, SK On 1%), while SK Telecom/SK Inc hold 27%/28%. Post-transaction, SK Inno+subsidiary's combined stake in the entity will reportedly decline to \~10%, while the effective stake for the remaining SK sister companies will increase. Capex needed to build the Honam Semi complex power infrastructure is quoted as a likely motivation behind the stake disposal.

\- Liquidity boost for Honam Semi complex power capex need? Korea’s President Lee unveiled the Honam Semiconductor Complex ambition on 29 June, targeting >W800tn in investments by 2030 to build a chip manufacturing hub in the southwestern city. The project is part of the the Won-quadrillion-level “Great Leap Forward: 3 Mega Projects” national investment initiative. Initial industry estimates suggest that the Hoham hub alone will require >6GW of power, while Reuters estimates that the four planned fabs will eventually consume 70-80% of the electricity consumed in the southwestern provinces. SKI has been serving as the energy infrastructure solution provider to SK Group’s “AI Full Stack” ambition, as highlighted by the Chairman’s earlier comments, saying “Companies that possess a full stack—from the memory needed in the AI era to data center infrastructure and the energy and electrification capabilities to support it—are rare.” We see SK as uniquely positioned to capture growing market share in the domestic energy solution market, with a holistic offering across gas power gen (SK E&S), SK On (ESS battery) and SMR innovation (deep dive on SK Inno’s Terrapower stake here).

\- SKI's growing traction as energy solution provider for SK's AI initiative: Prior to the Honam mega project launch, SKI and SK Telecom (SKT) had already partnered with AWS to build a 103MW AI Data Center (AIDC) in Ulsan (60,000 GPUs), with ultimate ambitions to scale to 1GW. This campus will be strategically co-located with SKI's LNG combined-cycle power plant. Internationally, SKI has signed an MOU with Vietnam's Nghe An province to

## Overweight

096770.KS, 096770 KS  
Price (22 Jul 26):W119,600  
Price Target (Jun-27):W170,000

Head of Asia Energy & Chemicals | Asia EV Battery

Parsley Ong AC (65) 6882-8578 parsley.rh.ong@JPM.com JPM Securities Singapore Private Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Michelle Wong  
(852) 2800 8556  
michelle.wong@JPM.com  
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Vicky Hsia  
(852) 2800 3752  
vicky.hsia@JPM.com  
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 7 for analyst certification and important disclosures, including non-US analyst disclosures.

develop an AIDC linked to the Quynh Lap LNG Power Project (developed by SKI), replicating the “power plant + data center” model offshore as the first overseas expansion of the SK consortium’s “Korean-style AI full-stack” approach. For next-generation AIDC technologies, SK Enmove and SK Telecom are collaborating to deploy Precision Liquid Cooling using SK Enmove’s thermal fluid at SKT’s AI Data Center Testbed. We also see potential for SK On to supply ESS to SKT’s AIDCs; SK On looks set to start LFP battery production in 2H26 and has already won >1.7 Gwh of domestic ESS orders and a 7.2 Gwh US ESS contract.

\- Portfolio re-balancing on track; ROE to reach nine-year high in FY26E. As noted in our recent initiation report, we see an attractive risk/reward in SK Inno following its portfolio optimization, stabilized balance sheet and expected record-high earnings from lubricants/refining in 2026. We continue to see SK printing the highest NP among the Korean battery trio in 2026E/27E and reaching a nine-year-high ROE of $11\%$ for this year vs. loss-making in FY25. Reiterate OW.

Figure 1: Korea energy earnings preview
Won bn

<table><tr><td>Company</td><td>Result</td><td>JPM OP</td><td>OP % q/q</td><td>OP % y/y</td><td>Cons OP</td><td>Cons NP</td><td>JPM v Cons OP*</td><td>Interim DPS</td></tr><tr><td>LGES</td><td>30 July</td><td>113</td><td>155%</td><td>-77%</td><td>177</td><td>(5)</td><td>-36%</td><td></td></tr><tr><td>S-Oil</td><td>3-7 Aug</td><td>1,077</td><td>-13%</td><td>413%</td><td>911</td><td>535</td><td>18%</td><td>1,400</td></tr><tr><td>LG Chem</td><td>31 July</td><td>315</td><td>733%</td><td>-34%</td><td>410</td><td>131</td><td>-23%</td><td></td></tr><tr><td>HSC</td><td>29 July</td><td>203</td><td>119%</td><td>99%</td><td>187</td><td>72</td><td>8%</td><td></td></tr><tr><td>Kumho</td><td>Early Aug</td><td>96</td><td>61%</td><td>47%</td><td>122</td><td>148</td><td>-22%</td><td></td></tr><tr><td>Lotte Chem</td><td>7 Aug</td><td>110</td><td>50%</td><td>145%</td><td>94</td><td>14</td><td>17%</td><td>1,000</td></tr><tr><td>SK Inno</td><td>30 July</td><td>1,797</td><td>-17%</td><td>530%</td><td>1,003</td><td>586</td><td>79%</td><td>Potential</td></tr></table>

Source: Company data, JPM estimates.

Figure 2: SK China shareholding mix (%)  
![](images/dc82946865c092a8a4c4da090e1d0a113811528509b10236e9fd0330407621b4.jpg)  
Source: Company data, media reports.

Figure 3: Sharp drop in SK Innovation capex as battery spend falls (Won tn)  
![](images/fedb7cfedcffb73eee0879615a9bee06965e9867bbfe0262019359cdc271d642.jpg)  
Source: Company data, JPM estimates.

Figure 4: FY25-27E NP of K-battery names (W tn)  
![](images/314ee28e37351ba7b0257613740e445d571a0973a393ecf8ff60b03b0845deee.jpg)  
Source: JPM estimates.

Figure 5: K-battery sector FY15-25 ROE trend  
![](images/02f2b4e1b4b0c30c96efc45baceb01c99042903ec8fe5ff2cd188e07fa9199f9.jpg)  
Source: Company data, JPM estimates.

Figure 6: Global refiners' share price performance  
![](images/bba4f5b377e38814858e14faaf6c1ad5ae0f9714b34b0cf768b60ebf59c8f8a3.jpg)  
Source: Bloomberg Finance L.P., JPM Asia Energy.

## Related research

Korea Battery: LGES wins 2.9GWh Google ESS project; SK On wins 13% of Korea AI ESS tender (17 July 2026)

Korea Energy: 2Q likely to beat on lubricants, with W4.2trn refiner compensation fund a 4Q tailwind; retain OW, but change pecking order to SK Inno > S-Oil (12 July 2026)

Korea Battery: Share prices +10-26% on hopes of accelerated US AIDC infrastructure buildout; raise US ESS demand estimate by 52% (29 June 2026)

SK Innovation: The Power of Atoms – TerraPower Wyoming SMR site visit takeaways (4 June 2026)

SK Innovation: Battery overhang priced in; one of Asia's most undervalued integrated energy platforms; initiate at OW (14 May 2026)

# Investment Thesis, Valuation and Risks

SK Innovation (Overweight; Price Target: W170,000)

## Investment Thesis

We are OW on SK Innovation. In our view, the market continues to be anchored on the 2023-25 narrative, dominated by battery-related losses, a deteriorating balance sheet/heavy capex burden, and a weak refining/chemical business. While these concerns are valid, we believe much of the downside is already reflected in valuations. Following SK Innovation's restructuring, we believe the company is no longer a Korean refiner with a cash-draining battery subsidiary, but increasingly an integrated Asia energy platform with a stabilized balance sheet, with 2027 capex falling $>20\%$ to the pre-2022 level.

## Valuation

Our Jun-27 PT of W170,000 is based on a one-year forward P/B of 1x (peak cycle P/B), +1SD vs. the historical average to reflect SKI's improved ROE outlook (averaging 8% in 2026E-28E vs. the 2021-25 average of -2.5%).

## Risks to Rating and Price Target

Downside risks include: (1) a delayed recovery in US/Europe battery utilization due to weak EV demand or select OEM customers' EV production cadence; (2) crude oil supply disruptions or more stringent domestic oil product price/export controls amid the Middle East conflict; and (3) a spike in LNG import costs due to supply disruptions or extreme weather.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to SK Innovation or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: SK Innovation or related entities.

\- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: SK Innovation or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: SK Innovation or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: SK Innovation or related entities.

\- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from SK Innovation or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from SK Innovation or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from SK Innovation or related entities.

\- Debt Position: JPM may hold a position in the debt securities of SK Innovation or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Initiated coverage Oct 05, 2007. All share prices are as of market close on the previous business day.

SK Innovation (096770.KS, 096770 KS) Price Chart  
![](images/3d81bffd07f93e8d5b90377ab9b491a1a31689811857afb88b4ea5a42403f538.jpg)  
Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends.

<table><tr><td>Date</td><td>Rating</td><td>Price (W)</td><td>Price Target (W)</td></tr><tr><td>03-Nov-23</td><td>OW</td><td>127600</td><td>180,000</td></tr><tr><td>07-Feb-24</td><td>OW</td><td>120800</td><td>145,000</td></tr><tr><td>23-Apr-24</td><td>OW</td><td>110600</td><td>120,000</td></tr><tr><td>05-Sep-24</td><td>NR</td><td>107000</td><td>--</td></tr><tr><td>14-May-26</td><td>OW</td><td>129600</td><td>165,000</td></tr><tr><td>12-Jul-26</td><td>OW</td><td>103900</td><td>170,000</td></tr></table>

Break in coverage Apr 24, 2026 - May 14, 2026.  
The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be fo

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 22 Jul 2026 11:53 PM HKT

Disseminated 22 Jul 2026 11:53 PM HKT
"""
