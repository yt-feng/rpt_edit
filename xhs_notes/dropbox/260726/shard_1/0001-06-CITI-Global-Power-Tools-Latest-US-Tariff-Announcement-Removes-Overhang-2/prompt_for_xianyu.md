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
# Global Power Tools

## Latest US Tariff Announcement Removes Overhang

## CITI'S TAKE

Per Reuters (24/7/26), the US on Thursday imposed new tariffs of up to 12.5% on imports from 60 countries, replacing temporary levies that are due to expire on 25 July after the US Supreme Court struck down earlier trade measures. We see this is as a positive development for the Global Power Tools sector as it removes the overhang of tariff uncertainty following the expiry of the temporary 10% tariff on 25 July. We like Techtronic > Great Star > Chervon > SWK in our coverage given their heavy exposure to the US market and tariff charged on their brand businesses.

Latest tariffs based on 'forced labour' concerns – The US has implemented new tariffs ranging from 10% to 12.5% on roughly 60 trading partners, replacing an expiring temporary 10% global levy. These new tariffs are based on US's claim that the trading partners have not properly tackled forced labor. The latest tariffs use Section 301 authority to build a stronger legal foundation following previous court rulings.

Tooling companies already budgeting for a higher tariff – According to the Reuters report cited above, TTI and SWK were already budgeting for the US tariff rate to revert to the reciprocal tariff level of 20% for their ASEAN production after the expiry of current temporary tariff on 25 July. We therefore see scope for consensus earnings upgrades for TTI and SWK as the new tariff rate of 10-12.5% replacing the temporary 10% tariff is lower than the 20% reciprocal tariff which was in place last year.

TTI's operating margin expansion prospects this year – We have recently received several investor requests on TTI's 1H26E preview. We summarize our key forecasts in Fig 1 with earnings growth likely to accelerate to 26% in 2H26E from 12% in 1H26E. We expect OPM expansion at TTI to be in greater focus this year than revenue growth. We model operating margin expansion of 60bp during 1H26 with a split of 30bp on tariff reduction (applicable rate reducing to 10% from 20% reciprocal tariff in VN), 20bp on absence of HART loss, and 10bp on mix upgrade towards MWK from Ryobi and consumer segment. Moreover, we see a higher degree of operating margin improvement of 130bp driven by 80bp on absence of HART loss, 40bp on the tariff reduction, and 10bp on mix upgrade toward MWK from Ryobi and consumer segment. We note that HART incurred a loss of 0.5% on sales in 2025 but most of the loss was incurred in 2H25 on account of impairment and higher promotion discount to clear the inventory before its divestment in end-2025.

Eric Lau $^{AC}$ +852-2501-2726
eric.h.lau@citi.com

Alice Cai
+852-2501-2704
alice.cai@citi.com

Andy Li
+852-2501-2597
andy.li@citi.com

## See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

© 2026 Citi Inc. No redistribution without Citi's written permission.

Techtronic (0669.HK) - Opening 30D CW on Expectation of Good 1H26 Results

Figure 1. TTI – 1H26E results preview with earnings growth acceleration in 2H26E

<table><tr><td>US$ mn</td><td>1H23</td><td>2H23</td><td>1H24</td><td>2H24</td><td>1H25</td><td>2H25</td><td>1H26E</td><td>2H26E</td></tr><tr><td>Turnover</td><td>6,879</td><td>6,852</td><td>7,312</td><td>7,310</td><td>7,833</td><td>7,426</td><td>7,990</td><td>8,038</td></tr><tr><td>YoY</td><td>-2</td><td>10.2%</td><td>6.3%</td><td>6.7%</td><td>7.1%</td><td>1.6%</td><td>2.0%</td><td>8.2%</td></tr><tr><td>COGS</td><td>-</td><td>(4,134)</td><td>(4,391)</td><td>(4,335)</td><td>(4,677)</td><td>(4,290)</td><td>(4,707)</td><td>(4,605)</td></tr><tr><td>Gross profit</td><td>-</td><td>2,718</td><td>2,921</td><td>2,975</td><td>3,156</td><td>3,136</td><td>3,283</td><td>3,432</td></tr><tr><td>Other revenue</td><td>-</td><td>25</td><td>40</td><td>48</td><td>35</td><td>39</td><td>39</td><td>39</td></tr><tr><td>Distribution cost</td><td>-</td><td>(1,160)</td><td>(1,244)</td><td>(1,259)</td><td>(1,350)</td><td>(1,369)</td><td>(1,377)</td><td>(1,452)</td></tr><tr><td>YoY</td><td>-</td><td>11.8%</td><td>4.8%</td><td>8.5%</td><td>8.5%</td><td>8.7%</td><td>2.0%</td><td>6.0%</td></tr><tr><td>Administrative cost</td><td>-</td><td>(687)</td><td>(760)</td><td>(730)</td><td>(743)</td><td>(748)</td><td>(769)</td><td>(782)</td></tr><tr><td>YoY</td><td>-</td><td>12.1%</td><td>5.6%</td><td>6.3%</td><td>-2.2%</td><td>2.5%</td><td>3.5%</td><td>4.5%</td></tr><tr><td>Research and development cost</td><td>-</td><td>(305)</td><td>(298)</td><td>(350)</td><td>(359)</td><td>(398)</td><td>(374)</td><td>(421)</td></tr><tr><td>YoY</td><td>-</td><td>20.7%</td><td>22.4%</td><td>14.8%</td><td>20.5%</td><td>13.6%</td><td>4.0%</td><td>5.9%</td></tr><tr><td>Operating profit</td><td>-</td><td>590</td><td>659</td><td>684</td><td>739</td><td>660</td><td>802</td><td>817</td></tr><tr><td>Finance cost</td><td>-</td><td>(46)</td><td>(65)</td><td>(61)</td><td>(58)</td><td>(39)</td><td>(39)</td><td>(34)</td></tr><tr><td>Associates</td><td>-</td><td>(0)</td><td>(0)</td><td>0</td><td>0</td><td>(0)</td><td>0</td><td>(0)</td></tr><tr><td>Profit before taxation</td><td>-</td><td>545</td><td>594</td><td>623</td><td>681</td><td>621</td><td>763</td><td>783</td></tr><tr><td>Taxation</td><td>-</td><td>(44)</td><td>(43)</td><td>(51)</td><td>(53)</td><td>(51)</td><td>(61)</td><td>(64)</td></tr><tr><td>Profit before minority</td><td>-</td><td>501</td><td>550</td><td>571</td><td>628</td><td>570</td><td>702</td><td>719</td></tr><tr><td>Minority interests</td><td>-</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net profit</td><td>-</td><td>501</td><td>550</td><td>571</td><td>628</td><td>570</td><td>702</td><td>719</td></tr></table>

<table><tr><td></td><td>1H23</td><td>2H23</td><td>1H24</td><td>2H24</td><td>1H25</td><td>2H25</td><td>1H26E</td><td>2H26E</td></tr><tr><td>Stock price</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Price target</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Risk-free interest rate</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Expected volatility</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Expected dividend yield</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Expected dividend price</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

## Chervon

(2285.HK; HK\$19.06; 1; 24 Jul 26; 16:10)

## Valuation

We believe the PE and discounted cash flow (DCF) methodologies are appropriate for Chervon, with PE reflecting growth momentum while the company delivers stable income streams as forecast in a DCF. We value Chervon at HK\$24 based on an 11x PE for 2027E, or a \~40–50% discount to the global comp average owing to its smaller scale of operation. We employ 11x PE for 2027E from prior 2026E due to 2026E being the first year of earnings recovery after the termination of IEEPA tariff since Feb 2026. The upcoming tariffs under Section 122 of up to 12.5% are well below IEEPA tariffs, in general. We cross-check with our DCF model, which derives a fair value of HK\$25 assuming WACC of 7.8% and terminal growth rate of 2%. In our DCF, we forecast free cash flow over a seven-year time horizon up to FY30 and then use the WACC to discount back.

## Risks

Our default risk rating for stocks such as Chervon with a short trading history (IPO in December 2021) is High Risk; however, we think a High Risk rating is not justified in this case given the company's solid financials, global leading position on OPE, strong global customer base, and long operating history since 1994.

Key downside risks to our target price include higher-than-expected new trade tariffs for the US; worse-than-expected volume growth if US sets to raise interest rate; market share loss in power tools segment which is the weakest link to the company.

Key upside risks to our target price include a relief from US reciprocal tariffs on China and Vietnam; better-than-expected demand for Chervon; and strong share win despite the tariff hike in the US.

## Hangzhou Great Star Industrial

(002444.SZ; Rmb27.95; 1; 24 Jul 26; 15:00)

## Valuation

We value Great Star at Rmb49 per share based on a \~19x 2026E PE target multiple, which is on par with mean given the return of a normal cycle from 2026E assuming no further deterioration of US reciprocal tariff policy from 2026E. We project a 3-year-forward EPS CAGR of 16% through 2028E after slower growth of 9% in 2025E under the US reciprocal tariff. Key drivers include: 1) GS is likely to deliver teens revenue growth for core hand tools on general maintenance centric in overseas markets like North America, which is quite resilient; 2) a strong \~50% revenue CAGR to over US\$1bn in 2028 for electric power tools and energy storage system for low base; and 3) plant relocation into ASEAN from China to lower production costs and tariff (versus rivals that are China production dependent) for the US/EU markets.

## Risks

Although our quant model rates GS shares as High Risk, we do not assign a High Risk rating due to removal of the overhang for logistics and materials cost pressure. Key downside risks that could cause the shares to trade below our target price include: 1) a worse-than-expected macro slowdown in the US/EU amid an interest rate upcycle; and 2) RMB appreciation versus USD as GS earnings are negatively correlated with RMB appreciation.

## Stanley Black & Decker

(SWK.N; US\$87.41; 1; 23 Jul 26; 16:00)

## Valuation

We value SWK shares at US\$100 based on a 18x 2026E PE, which is based on -0.5SD to mean from prior 19-20x PE in 2025 after release of 2025 results. We employ the -0.5SD to mean as the benchmark based on: 1) 2026 operating / gross margins would continue improving thru better efficiency and cost reduction program, 2) the industry will likely resume a normal growth from 2026, which would apply all peers, and SWK would likely surpass industry growth. In addition, the worst for profitability downcycle in 2023 should be behind us.

## Risks

Key downside risks include: 1) worse-than-expected end demand in the US/EU on an economic slowdown; 2) higher-than-expected materials costs; 3) execution error to slow the GM expansion pace; and 4) worse-than-expected trade tariff under

the Trump admin.

Key upside risks include: 1) USD weakness, which may lead to higher FX gains for its Europe and EM exposure; and 2) faster-than-expected electrification trend in the Outdoor tools segment.

Any of these risk factors could cause the shares to deviate from our target price.

## Techtronic

(0669.HK; HK\$128.1; 1; 24 Jul 26; 16:10)

## Valuation

We value TTI at HK\$150 per share based on a \~20x 2027E P/E, on par with the mean on the back of three-year forward EPS CAGR of 18% through 2028E. Our TP target rolls over to 2027E PE from 2026E after the 2025 results. TTI should accelerate revenue growth to 5-6% in 2026E from \~4% in 2025, which was slightly dragged by price inflation amid US reciprocal tariffs. From 2026E, TTI expects to completely shift China production for its US segment, mainly to Vietnam, the US, and Mexico. Separately, we expect the housing market and construction activity to be enhanced by lower funding costs amid the expected US rate downcycle through 2026E. MWK revenue growth should fall into the low-double-digit range over the next three years through 2028E. In addition, TTI's business model of maintaining high-single-digit revenue growth along with margin expansion remains intact. Our target price puts the stock at \~4.6x 2026E book value, in line with +1SD over the mean due to TTI's persistent rise in ROE.

## Risks

Downside risks that could cause the shares to fail to reach our target price include: 1) worse-than-expected US and EU macro conditions in 2026-27E; 2) worse-than-expected demand after price inflation amid US reciprocal tariffs; 3) worse-than-expected housing starts; 4) slower-than-expected economic growth in Europe amid geopolitical risk; 5) weaker-than-expected USD; and 6) worse-than-expected US tariffs in ASEAN and Mexico.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Hangzhou Great Star Industrial (002444.SZ)

Ratings and Target Price History
Fundamental Research

Analyst: Eric Lau

![](images/cc8f015cab7a9407783249d3e1257fc8d1a89eeae125998ebd09831e0abd2f09.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>24-Aug-23 12:48:11</td><td>1</td><td>*30.50</td><td>20.92</td></tr><tr><td>2</td><td>21-Sep-23 21:03:38</td><td>1</td><td>*30.00</td><td>18.58</td></tr><tr><td>3</td><td>21-Jan-24 18:31:21</td><td>1</td><td>*31.00</td><td>22.19</td></tr><tr><td>4</td><td>30-Jun-24 21:31:43</td><td>1</td><td>*34.00</td><td>24.70</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>25-Sep-24 11:10:43</td><td>1</td><td>*37.00</td><td>27.43</td></tr><tr><td>6</td><td>29-Apr-25 12:21:01</td><td>1</td><td>*35.00</td><td>22.91</td></tr><tr><td>7</td><td>29-Jun-25 19:08:46</td><td>1</td><td>*33.00</td><td>25.48</td></tr><tr><td>8</td><td>26-Aug-25 19:04:07</td><td>1</td><td>*45.00</td><td>34.70</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>30-Oct-25 12:52:40</td><td>1</td><td>*43.00</td><td>29.09</td></tr><tr><td>10</td><td>30-Nov-25 18:23:34</td><td>1</td><td>*46.00</td><td>31.42</td></tr><tr><td>11</td><td>26-May-26 12:29:48</td><td>1</td><td>*49.00</td><td>33.97</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Techtronic (0669.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Eric Lau

![](images/63369cf7a3e2ee422357f9b1b4fa01df70be38ea1c474e35d19308601263f687.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>09-Aug-23 15:07:25</td><td>1</td><td>*108.00</td><td>95.15</td></tr><tr><td>2</td><td>17-Dec-23 17:22:01</td><td>1</td><td>*118.00</td><td>88.70</td></tr><tr><td>3</td><td>20-Feb-24 13:48:01</td><td>1</td><td>*113.00</

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
