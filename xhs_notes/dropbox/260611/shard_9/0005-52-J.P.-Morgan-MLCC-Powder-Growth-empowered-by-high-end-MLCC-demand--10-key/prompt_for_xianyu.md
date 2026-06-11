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
## MLCC Powder

Growth empowered by high-end MLCC demand: 10 key takeaways from fireside chat with Sinocera

JPM View: We hosted Sinocera's senior management for a virtual fireside chat yesterday (8 June) in conjunction with our MLCC zoom series. The key takeaways from the event were that MLCC is being fueled by strong demand for AI servers and automotive electronics, and the MLCC powder industry entered a robust upward cycle in 1H26, exceeding both market and company expectations. Sinocera's MLCC business is well-positioned to deliver over $20\%$ annual revenue growth, supported by thriving, newly completed, high-end MLCC product lines. Capacity has ramped up for high-end MLCC powders, which boast higher selling prices and gross margins. Meanwhile, its portfolio of AI-related new materials is progressing steadily. Backed by sound R&D systems and rational capital arrangements, the company is poised for sustainable long-term development.

Global MLCC manufacturers are shifting production capacity to high-end products, leading to capacity spillover and a notable rise in the utilization rate of Sinocera's conventional MLCC powder lines. The company's AI and automotive-grade products have completed qualification at Samsung and will enter mass production in Q3. We believe such initiatives could materialize the company's earnings growth in 2H26 and onwards. In the long run, China's stringent controls on rare earth exports will create lasting advantages for domestic suppliers. Multiple new material projects including ceramic substrates, spherical silicon and satellite packaging components are in the client validation stage, with clear timelines for volume production ahead.

- 1. Industry Trend & Annual Growth Target. The MLCC sector had much stronger momentum in 1H26 than expected, as AI server demand drove robust consumption growth of high-end MLCC components. Capacity reallocation by overseas players lifted the operating rate of low-end MLCC producers. With dual growth drivers from conventional and high-end MLCC products, Sinocera stated that its full-year earnings growth target of $20 + \%$ would be highly achievable amid current tailwinds.  
- 2. Product Pricing & Profit Margin Structure. There is a clear tiered pricing and profitability across product lines. Conventional MLCC powder is priced at Rmb60k-70k/t, with a gross margin of $33 + \%$ . Automotive-grade products sell for Rmb80k-90k/t, while AI server-grade powder exceeds Rmb100k/t. High-end varieties deliver gross margins of $45\%$ to $50\%$ , substantially lifting overall profitability levels.  
- 3. Capacity Planning for MLCC Powders. Sinocera has built a well-structured capacity framework. Its stable production capacity for consumer-grade MLCC powder stands at 10,000 tons, which operated at a $70 + \%$ utilization rate last year. A 2,000-ton high-end production line was launched at end-2025, and another 3,000-ton expansion will be finished by year-end 2026. Total capacity will reach 15,000 tons, and the firm expects to sell over 1,000 tons of high-end products in 2026.  
- 4. Market Share & Key Customer Profile. Sinocera dominates the domestic MLCC powder market, holding more than 80% market share and around 20% of the global market. Domestically, it is the largest supplier for major client Fenghua, alongside other key partners. Internationally, Samsung is its core high-

## Asia Oils

Lei Mu AC

(86-21) 6106 6319

lei.mu@JPM.com

SAC Registration Number: S1730521050002

JPM Securities (China) Company

Limited

end customer. After a nearly one-year qualification process, the premium products will be shipped in large volumes starting from 3Q26.

- 5. Rare Earth Policy & Long-term Competitive Edge. China supplies $80\%$ to $95\%$ of global rare earth resources essential for MLCC powder production. Japanese manufacturers hold strategic inventories covering one to two years of usage, so there is no immediate supply pressure. Nevertheless, continuous strict export controls on rare earths would constrain overseas production capacity in the long term, bringing sustained order transfers to domestic players including Sinocera.  
- 6. Technical Threshold & Product Qualification. High-end MLCC powder requires stricter technical standards: particle size ranges from 100–150nm for domestic AI clients and 200nm for Samsung, with higher requirements on uniformity and dispersion. The yield rate of finished high-end MLCC powder may only reach 80%, versus over 95% for conventional products. With proven qualified products, subsequent client qualification cycles will be greatly shortened.  
- 7. Progress of New Material Businesses. Sinocera's new material projects are moving forward on schedule. Spherical Silicon will pass qualification at Taiwanese clients in 2H26, generating tens of millions RMB in revenue, with 2,000 tons of new capacity to be added by end of this year. Low-orbit satellite ceramic casings are projected to achieve $30\% - 40\%$ annual growth. Ceramic substrates and TEC components are under client testing and will contribute revenue starting in 2027.  
- 8. Industrial Strategy & Downstream Layout. The company adopts a differentiated industrial expansion strategy. It focuses on upstream ceramic powder materials for mature downstream MLCC markets with established giants. For high-end downstream sectors monopolized by overseas enterprises and still in early stages domestically, Sinocera may extend to finished products. Centered on domestic substitution, this strategy lowers operational risks and improves the success rate of industrial layout.  
- 9. Development Model: R&D plus M&A. Sinocera sticks to a dual growth model combining in-house R&D and external M&A. Annual R&D investment accounts for roughly $7\%$ of revenue with no spending cap for key projects. Two-tier R&D teams undertake long-term cutting-edge research and existing product upgrades respectively. Targeted M&As in medical and fine ceramic sectors complement technological strengths and accelerate business expansion.  
- 10. Capital Allocation & Shareholder Returns. The company strikes a balance between long-term investment and shareholder returns. It maintains steady spending on R&D and M&A, while actively implementing annual and semi-annual dividends as well as share repurchases. The proportion of overseas shareholders has fallen from a peak of 28% to current 5%–6%. Sinocera remains open to global investors and optimizes corporate governance to support its overseas business expansion.

Companies Discussed in This Report (all prices in this report as of market close on 09 June 2026, unless otherwise indicated)

Shandong Sinocera - A(300285.SZ/Rmb66.40/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Shandong Sinocera - A or related entities.  
- Debt Position: JPM may hold a position in the debt securities of Shandong Sinocera - A or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Shandong Sinocera - A (300285.SZ, 300285 CH) Price Chart  
![](images/2d02e2cb9448a869a9729876670e79bbcade0804a66dfb7e1a40c5565c8518c7.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(Rmb) |
| ---------- | ---------- |
| Jan 24     | OW Rmb28   |
| May 24     | OW Rmb25   |
| Jan 25     | OW Rmb26   |
| May 25     | OW Rmb28.547 |
| May 26     | OW Rmb60.4 |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>19-Feb-24</td><td>OW</td><td>20.10</td><td>28</td></tr><tr><td>07-Aug-24</td><td>OW</td><td>17.63</td><td>25</td></tr><tr><td>26-Feb-25</td><td>OW</td><td>19.15</td><td>26</td></tr><tr><td>30-Oct-25</td><td>OW</td><td>23.21</td><td>28.547</td></tr><tr><td>27-May-26</td><td>OW</td><td>49.65</td><td>60.4</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends.  
Initiated coverage Dec 06, 2022. All share prices are as of market close on the previous business day.

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period.

JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Mu, Lei : COSL - A (601808.SS), COSL - H (2883.HK), LB Group - A (002601.SZ), Offshore Oil Engineering - A (600583.SS), Shandong Sinocera - A (300285.SZ), Sinopec Engineering (2386.HK), Sinopec Oilfield Service Corp - A (600871.SS), Sinopec Oilfield Service Corp - H (1033.HK), Sinopec Shanghai Petrochemical - A (600688.SS), Sinopec Shanghai Petrochemical - H (0338.HK), Skshu Paint Co., LTD - A (603737.SS), Yantai Jereh - A (002353.SZ)

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.  
\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.  
For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on releva

[中间内容因长度限制已省略]

ties discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
