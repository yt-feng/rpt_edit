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

## Akeso

Ad hoc HARMONi OS update: Positive but unlikely to be fundamentally needle-moving

On 22 July, Summit released an updated, but ad hoc, overall survival (OS) analysis from its global Ph3 HARMONi trial (ivonescimab + chemo vs, chemo in 2L+ EGFR-mutated non-squamous NSCLC); the trial that underpins its FDA BLA (PDUFA date Nov. 14, 2026). With longer Western follow-up and a June 2026 data cutoff, Western patients now show an OS HR of 0.76, consistent with that of the ITT (intention-to-treat) population in this global study and consistent with that of the Chinese population in the China Ph3 trial HARMONi-A. We view this as sentiment-supportive rather than fundamentally needle-moving. The updated OS HR looks decent, but because this is an ad hoc analysis outside the original statistical plan, we cannot claim it to be statistically significant or not; there is no formal p-value, just a nominal p-value with favorable trend. Safety was clean with no new signals. We remain OW on Akeso.

\- Implications for HARMONi itself — incrementally supportive of the BLA, but not decisive. The prespecified primary OS analysis was not statistically significant (HR 0.79, p=0.057), while PFS clearly hit (HR 0.52, p<0.00001). The 22 July analysis tightens Western patients' OS HR to 0.76 and shows West/Asia convergence, helping address the two earlier concerns to some extent that 1) OS benefit was Asia-skewed; and 2) OS benefit of Asian and Western patients might not be consistent. However, this is not decisive evidence for OS benefit, given the analysis is ad hoc. We think this OS analysis plus the 2025 Sep. analysis will help with the BLA review rather than adding definitive statistical weight.

\- We also have a positive view of the trend of OS HR becoming lower with longer follow-up in HARMONi, which might suggest ivonescimab's OS benefit is similar to PD-1 mAb, continuing to improve with longer follow-up time. More specifically, in the ITT population, OS HR is 0.79/0.78/0.76 in 2025 Apr./2025 Sep./2026 Jun. analysis, respectively. Similarly, in the Western patient population, OS HR is 0.98/0.84/0.76 in 2025 Apr./2025 Sep./2026 Jun. analysis, respectively.

\- Read-through to HARMONi-3, which is the Ph3 trial investors care most about, is modestly positive with limited impact. HARMONi-3 is the global 1L NSCLC study; squamous-cohort's final PFS is due in 2H26 with interim OS, and non-squamous PFS in 1H27. A consistent West-vs-Asia OS profile in HARMONi is comforting because HARMONi-3's success rests on replicating strong China data (HARMONi-6 OS HR=0.66) in a Western-heavy population. Previously, we estimated that final PFS will hit, but the interim OS HR in HARMONi-3 needs to be around 0.72 to be statistically significant, which we believe is a high bar. But we think HARMONi-3 final OS will hit.

\- What to watch next — HARMONi-3 squamous cohort's final PFS and interim OS in 2H26 are the next key catalysts. This is the next binary event and matters more than the 22 July OS update, since the earlier interim PFS analysis did not hit, leaving interim OS as the near-term signal on whether OS efficacy holds in a Western-heavy first line NSCLC population. Also on the calendar: the Nov 14, 2026 PDUFA decision for the 2L EGFRmut NSCLC

## Overweight

9926.HK, 9926 HK

Price Target (Dec-26): HK\$162.00

## Healthcare

Yang Huang AC
(852) 2800 3812
yang.huang@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Derek Choi
(852) 2800-8744
derek.c.choi@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Eric Zhao, CFA
(86-21) 6106 6256
eric.zhao@JPM.com
SAC Registration Number: S1730524050001
JPM Securities (China) Company Limited

See page 5 for analyst certification and important disclosures, including non-US analyst disclosures.

indication, plus HARMONi-3 non-squamous PFS in 1H27.

# Investment Thesis, Valuation and Risks

Akeso (Overweight; Price Target: HK\$162.00)

## Investment Thesis

Akeso is a commercial-stage biotech in China and a leader in bispecific antibody. Despite Akeso's solid stock performance in 2024, we continue to see upside to its share price in 2025, driven by: (1) AK104 (PD-1/CTLA-4): Indication expansion into a broad range of large markets in China, which we expect should generate \~Rmb7bn in China peak sales. (2) AK112 (PD-1/VEGF): Successful inclusion in the NRDL, which should unleash solid sales momentum with >Rmb8bn peak sales in NSCLC in China alone, and its leading position in the PD-(L)1/VEGF space, as well as a highly competitive efficacy profile vs. Keytruda should support ex-China peak sales of US\$6+bn.

## Valuation

Our Dec-26 PT of HK\$162 is based on our DCF valuation. We estimate free cash flow for Akeso until 2034, assuming a terminal growth rate of 3.0% and a WACC of 9.6%.

## DCF valuation

<table><tr><td colspan="2">WACC Assumptions</td></tr><tr><td>Risk-free rate</td><td>3.8%</td></tr><tr><td>Market risk</td><td>6.6%</td></tr><tr><td>Beta</td><td>1.0</td></tr><tr><td>Cost of equity</td><td>10.4%</td></tr><tr><td>Cost of debt</td><td>3.0%</td></tr><tr><td>Liabilities as a % of EV</td><td>10%</td></tr><tr><td>WACC</td><td>9.6%</td></tr><tr><td>WACC</td><td>9.6%</td></tr><tr><td>Terminal growth rate</td><td>3.0%</td></tr><tr><td>Terminal Present Value</td><td>80,597</td></tr><tr><td>PV Cash Flow</td><td>35,486</td></tr><tr><td>Enterprise value</td><td>116,084</td></tr><tr><td>+ Cash balance</td><td>10,466</td></tr><tr><td>- LT Debt</td><td>(4,541)</td></tr><tr><td>- Minority Interest</td><td>(131)</td></tr><tr><td>Early pipeline assets</td><td>9,500</td></tr><tr><td>Akeso equity value (RMB mn)</td><td>131,640</td></tr><tr><td>+ SMMT equity value (Rmb mn)</td><td>3,911</td></tr><tr><td>Total equity value (Rmb mn)</td><td>135,551</td></tr><tr><td>Shares Outstanding (MM)</td><td>921</td></tr><tr><td>Per Share Value (RMB)</td><td>147.2</td></tr><tr><td>Per Share Value (HKD)</td><td>162</td></tr></table>

Source: JPM estimates.

Risks to Rating and Price Target

Key downside risks include: (1) pipeline development setbacks; and (2) sales of AK104 or AK112 are below our expectations.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider (Hong Kong): JPM Securities (Asia Pacific) Limited and/or JPM Broking (Hong Kong) Limited and/or an affiliate is a market maker and/or liquidity provider in the securities of Akeso or related entities and/or warrants or options thereon, which are listed or traded on The Stock Exchange of Hong Kong Limited.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Akeso or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Akeso or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Akeso or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Akeso or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Akeso or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Akeso (9926.HK, 9926 HK) Price Chart  
![](images/281d66ed6a00f41bbb3ae5495e9d7063aa5ede82ef4bf60217df6e11e700ddf5.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target(HK$)</td></tr><tr><td>14-Oct-23</td><td>OW</td><td>39.05</td><td>57</td></tr><tr><td>08-Nov-23</td><td>OW</td><td>47.90</td><td>59</td></tr><tr><td>11-Sep-24</td><td>OW</td><td>55.70</td><td>68</td></tr><tr><td>31-Oct-24</td><td>OW</td><td>65.80</td><td>74</td></tr><tr><td>08-Jan-25</td><td>OW</td><td>57.40</td><td>76</td></tr><tr><td>01-Apr-25</td><td>OW</td><td>76.20</td><td>88</td></tr><tr><td>24-Apr-25</td><td>OW</td><td>92.90</td><td>110</td></tr><tr><td>03-Jun-25</td><td>OW</td><td>75.00</td><td>99</td></tr><tr><td>28-Aug-25</td><td>OW</td><td>157.00</td><td>166</td></tr><tr><td>18-Dec-25</td><td>OW</td><td>117.10</td><td>149</td></tr><tr><td>30-Mar-26</td><td>OW</td><td>126.40</td><td>162</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage May 27, 2020. All share prices are as of market close on the previous business day.  
The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated  
Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Huang, Yang : Akeso (9926.HK), Ascentage Pharma - H (6855.HK), BeOne - A (688235.SS), BeOne - H (6160.HK), Bora Pharmaceuticals (6472.TW), DaShenLin Pharmaceutical Group - A (603233.SS), Genscript Biotech - H (1548.HK), Hansoh Pharma - H (3692.HK), Hengrui - A (600276.SS), Hengrui - H (1276.HK), Innovent Biologics (1801) (1801.HK), Kelun Biotech (6990.HK), Laobaixing Pharmacy Chain - A (603883.SS), Mindray - A (300760.SZ), RemeGen - A (688331.SS), RemeGen - H (9995.HK), Shanghai Junshi Biosciences - A (688180.SS), Shanghai Junshi Biosciences - H (1877.HK), Tigermed - A (300347.SZ), Tigermed - H (3347.HK), WuXi AppTec - A (603259.SS), WuXi AppTec - H (2359.HK), WuXi Biologics (2269.HK), WuXi XDC (2268.HK), Yifeng - A (603939.SS)

JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US 

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
