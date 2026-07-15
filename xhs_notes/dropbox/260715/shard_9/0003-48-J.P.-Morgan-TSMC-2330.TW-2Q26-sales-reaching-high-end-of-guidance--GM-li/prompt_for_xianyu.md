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

Asia Pacific Equity Research 13 July 2026

## TSMC

## 2Q26 sales reaching high-end of guidance; GM likely to beat

TSMC's June revenue reached NT\$443bn, up 6% MoM and 68% YoY. Preliminary 2Q26 sales came in at NT\$1,270bn, up 12% QoQ and 36% YoY, largely in line with JPMe/Consensus and reaching the high end of 2Q26 USD guidance (US\$39.0-40.2bn). The strong 2Q top-line was primarily driven by sustained datacenter AI momentum. As a result, we expect 2Q26 GM to exceed the high end of guidance (JPMe 69.5% vs guided 65.5-67.5%), supported by elevated UTR (N3/N5 likely continue running at over 100% UTR), hot-run/super-hot-run orders (carrying 50%/100% price premiums), and continued efficiency gains. We expect GMs to remain at a high level (67%+) in coming quarters despite dilution from the N2 ramp and overseas fabs, underpinned by the sustained S/D imbalance (likely persisting into 2028). Overall, we forecast TSMC's revenue to grow 37%/34%/23% YoY in USD terms in 2026/27/28, respectively. Key fundamental drivers include: 1) larger die sizes; 2) adoption of chiplet configurations; and 3) faster growth in ASICs. Meanwhile, CPUs emerge as a new fast-growth driver, given rising agentic AI demand.

\- Near-term GMs remain solid on high UTR and firm pricing, despite dilution from N2 and overseas expansion: We expect TSMC's 2Q26 GM to reach $69.5\%$ (up 3.3ppts QoQ), driven primarily by: 1) strong utilization (N3 and N5 remain at $120 + \%$ UTR), 2) increased ASPs from hot run/ super hot run orders (carrying $50\% / 100\%$ price premium), and 3) improved overall efficiency. As for 3Q, we expect revenue to grow $\sim 10\%$ QoQ, with GM at $67.6\%$ . While the N2 ramp and rising overseas capacity contribution could dilute margins in 2H, we expect GM to hold at $67 - 68\%$ in coming quarters, underpinned by improving N3 GMs (set to surpass the corporate average in 2H26) and a richer mix (continuing rising HPC contribution). In addition, we expect another round of price hikes in 2027 ( $\sim 8 - 10\%$ for N3 and N2, with a milder uplift for N5, N7, and CoWoS) to provide further GM support.

\- Accelerated capacity build on leading-edge nodes and advanced packaging: Given strong AI demand and a persistent S/D imbalance at leading-edge nodes (especially N3/N2), TSMC has been more proactive in accelerating build-out plans since early 2026. We raised our capex expectations for 2026/27/28 to US\$58bn/\$78bn/\$84bn respectively in our previous note (see our TSMC preview note), and expect the company to revise up or highlight upside to its 2026 capex guidance (previously guided at the upper range of US\$52-56bn), with only qualitative commentary on 2027-28 capex likely at this point. For N3, we are seeing accelerated cross-fab collaboration (utilizing N7/N12/28nm fabs to support wafer processing for N3 and N5), and expect N3 capacity to reach 167k/213k/240k wfpm by end-2026/27/28, against a current S/D gap of \~600k wafers, in our view. The N2 ramp also looks strong (eventual capacity reaching 240-250k wfpm by 2029-30), as TSMC encourages HPC customers to migrate to N2 on better yields and performance. In advanced packaging, we now expect TSMC's CoWoS capacity to reach 115k/190k wfpm by YE26/27 (up 95%/65% YoY), but S/D is likely to remain tight given recent upside in CPU demand (NVIDIA Vera and AMD Venice will start adopting CoWoS, with more ASIC CPUs potentially following).

## Overweight

2330.TW, 2330 TT
Price (13 Jul 26):NT\$2440.0
Price Target (Jun-27):NT\$3100.0

## Technology and Telecoms

Gokul Hariharan AC (852) 2800-8564 gokul.hariharan@JPM.com JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Jennifer Hsieh  
(886-2) 2725-9868  
jennifer.hsieh@JPM.com  
JPM Securities (Taiwan) Limited

David Chou  
(886-2) 2725-9618  
david.chou@JPM.com  
JPM Securities (Taiwan) Limited

Jason Chen  
(886-2) 2725-9864  
jason.bh.chen@JPM.com  
JPM Securities (Taiwan) Limited

See page 4 for analyst certification and important disclosures, including non-US analyst disclosures.

Subham Singhania (91-22) 6157-3801 subham.singhania@JPM.com JPM India Private Limited

\- Key topics for the upcoming earnings meeting: Looking ahead to TSMC's 2Q26 earnings call, we expect company to share: 1) a strong message on near-term GM strength (2Q approaching the $70\%$ level; 3Q guided to the $67 - 68\%$ range); 2) qualitative commentary on demand and capacity dynamics; 3) a potential upward revision to 2026 revenue guidance towards mid-to-high $30\%$ YoY growth in USD terms (previously "above $30\%$ "); 4) reassurances dismissing concerns over competition in both leading-edge and mature-node; 5) commentary addressing potential upside to capex; and 6) possible updates on the Datacenter AI TAM, given accelerating demand for AI accelerators and the emergence of CPUs as a new growth driver.

# Investment Thesis, Valuation and Risks

TSMC (Overweight; Price Target: NT\$3100.0)

## Investment Thesis

We expect TSMC's structural growth drivers to remain very strong as leading-edge supply (N4, N3, and N2) stays tight well into 2027 or early 2028, given accelerating AI demand, continued growth in N3, N2 and advanced back-end revenues, and long lead time for capacity build despite accelerated capex. Near-term, we believe GMs are also likely to remain strong, nudging $70\%$ levels, given N3 improvement, high UTR and decent pricing, despite N2 and overseas dilution. We expect broader price hikes in 2027, given the widening supply-demand gap and a stronger Datacenter AI CAGR (we now estimate $69\%$ CAGR from 2024-29E, driven by both higher accelerator estimates and a surge in AI CPU numbers).

## Valuation

Our Jun-27 PT of NT\$3,100 is based on \~20x 12-month forward P/E and reflects stronger near-term profitability, better visibility on AI demand, stronger capacity build and firmer pricing into 2028. Our target multiple is higher than TSMC's five-year average historical multiple.

## Risks to Rating and Price Target

Key downside risks to our rating and price target include: (1) the debate on the duration of the AI capex growth cycle and (2) any negative impact from weak PC/Smartphone demand in 2H26.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to TSMC or related entities.

\- Analyst Position: An analyst on the Equity or Credit coverage team, non-fundamental analyst who may produce trade recommendations, or a member of their respective household(s) has a financial interest in the debt or equity securities of TSMC or related entities.

\- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of TSMC or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: TSMC or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: TSMC or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: TSMC or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from TSMC or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from TSMC or related entities.

\- Debt Position: JPM may hold a position in the debt securities of TSMC or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

![](images/7201e45f40070a4b1cf859dc8ead051da6760f1e88adcc0c851d2951d836d266.jpg)  
Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Apr 28, 2002. All share prices are as of market close on the previous business day.  
The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Hariharan, Gokul : ASE Technology Holding Co Ltd (3711.TW), ASMPT Ltd (0522) (0522.HK), AirTAC (1590.TW), Alchip Technologies (3661.TW), BizLink (3665.TW), Chipbond Technology (6147.TWO), GDS Holdings (GDS), GUC (3443.TW), Hiwin (2049.TW), Hon Hai Precision (2317.TW), MediaTek Inc. (2454.TW), Nien Made (8464.TW), Novatek Microelectronics Corp. (3034.TW), Powerchip Semiconductor Manufacturing Corp. (6770.TWO), SMIC (0981) (0981.HK), Silicon Motion (SIMO), Sinbon (3023.TW), TSMC (2330.TW), Teco Electric & Machinery (1504.TW), UMC (2303.TW), Vanguard International Semiconductor Corp. (5347.TWO), Voltronic Power Technology (6409.TW), Xiaomi (1810) (1810.HK)

## JPM Equity Research Ratings Distribution, as of July 04, 2026

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

J

[中间内容因长度限制已省略]

cements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or

Completed 13 Jul 2026 09:30 PM HKT
"""
