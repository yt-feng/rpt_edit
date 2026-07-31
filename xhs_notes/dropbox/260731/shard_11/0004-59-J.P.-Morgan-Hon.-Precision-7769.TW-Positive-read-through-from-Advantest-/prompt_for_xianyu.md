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
# JPM

## Hon. Precision

Positive read-through from Advantest's FY1Q26 earnings call - better, diversified AI demand and faster SoC tester capacity builds; OW

\- Advantest's relevant commentary. 1) Advantest sees the rapid adoption of inference AI driving semiconductor demand across ASICs, CPUs and DRAM - the three are growing faster than expected. GPU market is still the largest and also enjoys strong demand. 2) Advantest raised its FY26 outlook and expects the SoC and memory tester markets in 2026 to be larger than its previous expectations as of April. 3) Advantest is accelerating its capacity expansion plans. Its prior annual capacity targets for V93K testers were 5,000 units by Mar 2027 and 10,000 units by late 2028 or early 2029. The company expects to exceed the 5,000 unit target by Mar 2027 and to pull in the 10,000 unit target earlier. 4) Multiple layers of drivers for Advantest's SoC testers include chip unit growth and test content increase generation to generation (i.e. longer test times and additional test insertions). 5) Customer demand visibility for Advantest has extended to 18 months for a lot of cases, vs historically 6-month forecasts from customers. 6) CPU volumes are growing a lot and driving some of the SoC tester TAM increase. On the final test (FT) stage, the test time for CPU is quite a bit lower than that for the accelerators, given the difference in chip complexities.

Advantest (6857 JT) is covered by JPM analyst Mio Shikanai, see her FY1Q26 results note here.

## Read-throughs to Hon. Precision

\- In FT, the-tester-to-handler relationship is 1:1; Hon dominates in AI & HPC handlers. Advantest's upward revisions to the SoC tester market size in 2026, along with its accelerating near- and mid-term capacity expansion plans, create a positive read-through for Hon's test handler demand. Hon is the global No.1 player in semiconductor test handlers and holds a dominant share in final test (FT) handlers for AI and HPC applications (GPUs, ASICs, CPUs, etc.).

\- Better-than-expected demand from CPUs and ASICs supports Hon's fundamentals and stock narrative. A few investors still view Hon as primarily exposed to NV GPUs and therefore over-correlate Hon's share price outlook with NV GPU progress. Hon has been diversifying into ASICs and CPUs and has guided that its AI GPU vs. ASIC demand mix will shift from \~75–80% / \~25–30% in 2025 to \~50% / \~50% in 2026. In addition, within the system-level test (SLT) handler business, Hon also has a dominant share in AI ASICs and CPUs, by supplying to MediaTek TPUs and AMD Venice CPUs.

\- Advantest's \~18-month customer demand visibility underpins Hon's prior growth guidance. Hon has guided that its equipment shipment value (reflecting both units and pricing) will grow by $>40\%$ YoY in 2026 and $>50\%$ YoY in 2027, with continued rapid expansion beyond that. Hon remains in supply tightness for handlers. If Hon can secure more production sites timely,

## Overweight

7769.TW, 7769 TT
Price (29 Jul 26):NT\$5,175.00
Price Target (Jun-27):NT\$8,000.00

## Technology

Jimmy Huang AC
(886-2) 2725-9865
jimmy.huang@JPM.com
JPM Securities (Taiwan) Limited

Jerry Tsai AC
(886-2) 2725-9867
jerry.tsai@JPM.com
JPM Securities (Taiwan) Limited

Josie Yu
(886-2) 2725-9877
josie.yu@JPM.com
JPM Securities (Taiwan) Limited

Gokul Hariharan
(852) 2800-8564
gokul.hariharan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 4 for analyst certification and important disclosures, including non-US analyst disclosures.

there remains upside potential to its growth guidance.

\- Hon benefits from the same multi-layer demand drivers for units and grows ASP on spec upgrades. Chip unit growth, longer test times, and additional test insertions shall continue to drive Hon's handler shipments. We also highlight that Hon's ATC handler ASP could grow at a teens CAGR, reflecting critical value-add features such as thermal capability upgrades (a roadmap to 2028), integration of optical inspection functions into the handler, CPO test insertion 4 optical-electrical co-test, a new platform for very large packages (120×150 mm and above), etc.

\- Hon will report on Jul 30 and hold its earnings call at 2:30pm Taiwan time on Jul 30. See our Jul 12 note for recent updates.

# Investment Thesis, Valuation and Risks

Hon. Precision (Overweight; Price Target: NT\$8,000.00)

## Investment Thesis

We are OW Hon. Precision (Hon). Hon is the global No.1 player in semiconductor test handlers, with a 35%+ market share, with an 80% revenue mix from AI & HPC. Given volume and spec uptrends for AI & HPC chips, we model 38%/15% CAGRs for handler shipments/ASP in 2025-28, driving 61% CAGRs for both revenue and EPS. We believe the Street underestimates its multi-year ASP expansion potential amid rapid test spec upgrades. Hon is also a CPO enabler/beneficiary and is becoming a handler total solution provider. We like Hon's EPS power, re-rating potential and enabler role in future AI chip tests.

## Valuation

Our Jun-27 PT of NT\$8,000 is based on a 38x 2027E P/E, slightly higher than its average of plus 2 STDs of 34x since Nov-24, when the company started trading on the Emerging Board.

We see a potential bull scenario in which Hon's share price could challenge the NT\$10,000 level if and when the Street rolls forward to 2028E EPS and assigns a P/E of 35-40x (see our discussion here).

## Risks to Rating and Price Target

Key downside risks include an AI demand slowdown, test density declines, growing competition and slow progress in new advanced packaging technologies.

Key upside catalysts include global AI/AI semi capex hikes, stronger and longer AI demand, accelerating AP tech migrations and key project wins.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Hon. Precision or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Hon. Precision or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Hon. Precision (7769.TW, 7769 TT) Price Chart  
![](images/018f4cac212e2f8c8fbc92b0aec33e4f0eaa38423c87137d1dfb3a45c152fc90.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (NT$)</td><td>Price Target(NT$)</td></tr><tr><td>04-May-26</td><td>OW</td><td>4945.00</td><td>6,700</td></tr><tr><td>13-May-26</td><td>OW</td><td>6870.00</td><td>8,000</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends.  
Initiated coverage May 04, 2026. All share prices are as of market close on the previous business day.  
The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period.  
JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Huang, Jimmy : ACM Research (ACMR), ACM Research (Shanghai) (688082.SS), All Ring Tech (6187.TW), GlobalWafers Co., Ltd (6488.TWO), Grand Process Technology (3131.TW), Hon. Precision (7769.TW), Macronix (2337.TW), NCE Power - A (605111.SS), SICC - A (688234.SS), Scientech (3583.TW), StarPower Semiconductor - A (603290.SS), United Nova - A (688469.SS), Winbond (2344.TW)Tsai, Jerry : Chicony Power Technology (6412.TW), Chroma ATE (2360.TW), Chunghwa Precision Test Tech (6510.TWO), E Ink (8069.TWO), Elite Material Co (2383.TW), Flexium Interconnect Inc (6269.TW), Radiant Opto-Electronics Corp. (6176.TW), Sunonwealth (2421.TW), Taiwan Surface Mount Tech (6278.TW), Tripod Technology Corp (3044.TW), Unimicron (3037.TW), WIN Semiconductors Corp (3105.TWO), YAGEO (2327.TW)

JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

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

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance 

[中间内容因长度限制已省略]

 market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and

should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
