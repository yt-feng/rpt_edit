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
# China Consumer

Sequentially Improved China Retail Sales in Jun; Reiterate Upside ST View on Li Ning & Haidilao

## CITI'S TAKE

We expect sequentially improved China retail sales in Jun (total retail sales: +1.0% YoY; consumer goods sales: +0.9% YoY; restaurant sales: +1.2% YoY, Fig 1) vs May (total retail sales: -0.6% YoY; consumer goods sales: -0.7% YoY; restaurant sales: +0.6% YoY) to result in further positive sentiment on the China consumer sector, especially amid investors' recent sector rotations after the government's newly approved pro-consumption policy (see Citi's July 13 note: China Consumer - Implication of newly approved "15th Five-Year Plan to Boost Consumption". Citi newly opened upside Short-Term View on Haidilao (see July 14 note: Haidilao - Adding Upside 30-Day Short-Term View) and Li Ning (see July 14 note: Li Ning - Expect investor pessimism to abate; Open a ST positive view). Citi's preferred 10 big-cap China consumer stocks with attractive valuation: Midea, Anta, Li Ning, CTF, Mengniu, Haidilao, Tsingtao, Bosideng, CR Beer, WH Group (detailed in Citi's July 2 sector note).

Citi's newly opened upside ST View on Li Ning — Since Citi's preview on Li Ning's 2Q retail sales on July 1 (see note: Li Ning - 2Q26 retail sales preview; sequentially more challenges for 26E topline guidance), we have observed the market's substantially lowered expectations for Li Ning's 2H26 outlook (incl a possible cut of mgmt's 2026 topline guidance), per our investor communication. On the positive side, we have seen investors' recent sector rotation to seek value in the China consumer discretionary space (incl YUMC). We expect incrementally positive sentiment on China sportswear stocks (whose share prices have largely reflected weakened the China retail environment of late, in our view), especially after the government's approval of a new pro-consumption policy (see Citi's July 13 note: China Consumer - Implication of newly approved "15th Five-Year Plan to Boost Consumption"). Li Ning is among Citi's preferred 10 big-cap China consumer stocks with attractive valuation (see detailed discussion in Citi's July 2 sector note). We also see neutral to positive implications for Li Ning from Nike's 4QFY26 narratives (see Citi's July 1 note: China Sportswear - Nike's 4QFY26 narratives: Positive for Topsports, neutral to positive for Anta and Li Ning). Currently, Citi's NP estimates for Li Ning are $8\% / 10\%$ below Visible Alpha consensus forecasts. Fundamentally, we continue to relatively prefer Anta (Buy) to Li Ning (Buy) in the China sportswear sector (see Citi's Jun 22 note: China Sportswear: Takeaways from Citi Consumer Corp Day; Updated sector pecking order).

Citi's newly opened upside ST View on Haidilao — Thanks to its strong table-turn in 4M26 (+MSD YoY), we expect HDL's 1H26 table-turn to rise by LSD YoY, better than the market expectation of being flattish YoY. HDL's overall table-turn in June declined $1 - 2\%$ YoY, in line with softened datapoints of most China retailers (see

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Xiaopo Wei, CFA $^{AC}$ +852-2501-2472
xiaopo.wei@citi.com

Vincent Young $^{AC}$ +852-2501-2738
vincent.young@citi.com

Tiffany Feng
+852-2501-2759
tiffany.feng@citi.com

Lydia Ling
+852-2501-2475
lydia.w.ling@citi.com

Brian Cho
+852-2501-2712
brian.cho@citi.com

Citi's July 13 note: Haidilao - 1H table-turn +LSD YoY; Expect more positive sentiments post 2Q results of Li Ning/Anta/YUMC). Given YUMC's (YUMC.N) likely strong 2Q26 results (on July 30), we expect more positive market sentiment on the China restaurant sector and open an upside Short-Term View on HDL, which is also one of the 10 big-cap China consumer stocks with attractive valuations (see details in Citi's July 2 sector note).

Figure 1. YoY change of China total restaurant sales  
![](images/559c73100dd2c52eecbb441ad8dd06b5b1d83745f9786ac908564a0234458a4d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
\*Jan-Feb data were reported on combined basis  
Source: NBS, Citi

Figure 2. YoY change of China total consumer goods retail sales  
![](images/9a9fef46bd98ef28e3a2ac8f584461ef9d674bfb441c09c643851c468be0a16c.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
\*Jan-Feb data were reported on combined basis  
Source: NBS, Citi

Figure 3. YoY change of China total retail sales by category

<table><tr><td>%YoY</td><td>Jan-Feb 26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td>Total Retail Sales</td><td>2.8</td><td>1.7</td><td>0.2</td><td>(0.6)</td><td>1.0</td></tr><tr><td>Restaurants</td><td>4.8</td><td>2.9</td><td>2.2</td><td>0.6</td><td>1.2</td></tr><tr><td>- Above designated size</td><td>2.5</td><td>1.2</td><td>(4.9)</td><td>(5.2)</td><td>(2.2)</td></tr><tr><td>Consumer Goods</td><td>2.5</td><td>1.5</td><td>(0.1)</td><td>(0.7)</td><td>0.9</td></tr><tr><td>- Beverage</td><td>6.0</td><td>8.2</td><td>3.6</td><td>6.1</td><td>5.8</td></tr><tr><td>- Apparel&amp;footwear</td><td>10.4</td><td>7.0</td><td>3.6</td><td>3.8</td><td>3.9</td></tr><tr><td>- Jewelry</td><td>13.0</td><td>11.7</td><td>(21.3)</td><td>(8.9)</td><td>(3.4)</td></tr><tr><td>- Home Appliances</td><td>3.3</td><td>(5.0)</td><td>(15.1)</td><td>(15.6)</td><td>(8.7)</td></tr><tr><td>- Comestics</td><td>4.5</td><td>8.3</td><td>4.7</td><td>2.5</td><td>12.6</td></tr><tr><td>- Tobacco &amp; Liquor</td><td>19.1</td><td>7.7</td><td>11.7</td><td>4.8</td><td>12.1</td></tr><tr><td>- Household goods</td><td>6.6</td><td>4.6</td><td>3.5</td><td>1.6</td><td>3.9</td></tr><tr><td>- Auto</td><td>(7.3)</td><td>(11.8)</td><td>(15.3)</td><td>(16.1)</td><td>(16.1)</td></tr><tr><td>- Grains and food</td><td>10.2</td><td>9.5</td><td>4.1</td><td>1.9</td><td>7.9</td></tr><tr><td>- Telecom equipment</td><td>17.8</td><td>27.3</td><td>6.2</td><td>0.7</td><td>16.5</td></tr><tr><td>- Furniture</td><td>8.8</td><td>(8.7)</td><td>(10.4)</td><td>(8.7)</td><td>(6.6)</td></tr><tr><td>- Cultural and office</td><td>5.8</td><td>15.0</td><td>(6.9)</td><td>(1.5)</td><td>12.7</td></tr><tr><td>- Energy &amp; fuel</td><td>(9.7)</td><td>0.1</td><td>(6.5)</td><td>(3.2)</td><td>(5.1)</td></tr><tr><td>- Sports equipment</td><td>4.1</td><td>(2.0)</td><td>(8.0)</td><td>(8.0)</td><td>(2.2)</td></tr><tr><td>- Home decoration</td><td>(2.2)</td><td>(9.0)</td><td>(13.8)</td><td>(13.6)</td><td>(10.5)</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Citi

## Companies Mentioned:

Anta Sports Products (2020.HK; HK\$73.9; 1; 14 Jul 26; 16:10) | Bosideng International (3998.HK; HK\$4.76; 1; 14 Jul 26; 16:10) | China Resources Beer (0291.HK; HK\$22.94; 1; 14 Jul 26; 16:10) | Chow Tai Fook Jewellery Group (1929.HK; HK\$11.79; 1; 14 Jul 26; 16:10) | Haidilao International Holding Ltd (6862.HK; HK\$11.15; 1; 14 Jul 26; 16:10) | Li Ning (2331.HK; HK\$14.9; 1; 14 Jul 26; 16:10) | Mengniu (2319.HK; HK\$17.25; 1; 14 Jul 26; 16:10) | Midea Group (000333.SZ; Rmb81.18; 1; 14 Jul 26; 15:00) | Tsingtao Brewery (0168.HK; HK\$43.7; 1; 14 Jul 26; 16:10) | WH Group Ltd (0288.HK; HK\$8.11; 1; 14 Jul 26; 16:10) | YUM China Holdings INC (YUMC.N; US\$43.3; 1; 14 Jul 26; 16:00)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>The Firm has made a market in the publicly traded equity securities of Chow Tai Fook Jewellery Group Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of ANTA Sports Products Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Li Ning Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of China Mengniu Dairy Company Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Midea Group Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of China Resources Beer Holdings Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Haidilao International Holding Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Mengniu.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Anta Sports Products,Mengniu,Midea Group,WH Group Ltd.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Anta Sports Products,Bosideng International,Chow Tai Fook Jewellery Group,Haidilao International Holding Ltd,Li Ning,Mengniu,Midea Group,WH Group Ltd,YUM China Holdings INC in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Anta Sports Products,Mengniu,Midea Group,WH Group Ltd.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Anta Sports Products,Chow Tai Fook Jewellery Group,Haidilao International Holding Ltd,Mengniu,Midea Group,WH Group Ltd,YUM China Holdings INC.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Anta Sports Products,Bosideng International,Chow Tai Fook Jewellery Group,Haidilao International Holding Ltd,Li Ning,Mengniu,Midea Group,WH Group Ltd,YUM China Holdings INC.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Anta Sports Products,Midea Group,WH Group Ltd,YUM China Holdings INC. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr></table>

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutr

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
