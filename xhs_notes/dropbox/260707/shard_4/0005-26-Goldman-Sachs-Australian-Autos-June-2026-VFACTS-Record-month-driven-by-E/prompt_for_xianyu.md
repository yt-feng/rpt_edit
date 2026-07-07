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
# Australian Autos: June 2026 VFACTS: Record month driven by EV/China vehicles

GS take: June new vehicle sales have bucked the downward trend to deliver a record month with 140k (+10%) sales with BYD marginally below Toyota (243 units) for top brand in the month, while Tesla Model Y was again the top selling vehicle. Key indicators for ARB/AOV continued to soften (GS index -16%; LCVs -13%; EVs +147%; China +85%). We expect elevated interest rates, fuel security concerns and supply constraints (e.g. Toyota) to continue to support the consumer shift to low-cost China/EVs, to which ARB/AOV have lower relative exposure, and which have lower take-up/spend rates for aftermarket accessories. Amotiv (Buy), ARB Corp (Neutral).

Elijah Mayr  
+61(2)9321-8995 | elijah.mayr@gs.com  
GS Australia Pty Ltd

Elise Bailey  
+61(3)9679-1344 | elise.bailey@gs.com  
GS Australia Pty Ltd

## Key takeaways:

GS key model index down 16% in June 2026. Our GS Index tracking across a composite of 10 key models, based on estimated 4x4 accessory take-up/spend, was down 16% YoY in June driven by Toyota supply constraints and the shift towards EV/China models. Toyota Hilux -16% YoY (-1,020 units), Ford Ranger -5% YoY (-294 units) and Toyota Prado -21% YoY (-447 units).

■ Total new vehicle growth +10%, led by small/medium SUVs as large SUV/4x4 decline. Total vehicle sales +10% YoY with SUV +23% (small/medium/large +18%/+55%/-15%), LCV -13% (4x4s -14%) and Passenger -5%.

Fuel security and shifting consumer preferences accelerating EV demand. Tesla topped the chart for the second consecutive month in Australia with EV sales +147% to 32.6k, Petrol -29% to 34.7k and Diesel -18% to 31.8k.

China brands accelerate share gains, led by BYD. China vehicles (Chery, GWM, MG, BYD) +85% YoY to 55.5k units and 40% new vehicle sales, a material increase from 8% in July 2021. The BYD Shark also posted a record month +13% to 3.4k units and was 16% of 4x4 sales.

■ Upcoming releases. Toyota HiLux (9th Gen) in late-2025/early-2026 (volumes impacted by supply/transition); Nissan Navara (D27) in March 2026; Ford Ranger Super Duty mass market release in mid-2026; Toyota RAV4 (6th Gen) in 2HCY26; Nissan Patrol (Y63) in late-2026/early-2027.

## Key charts

Exhibit 1: GS key model index declined in June, down $16\%$ , as consumer preference shifts to EVs  
Key model volume (#) and growth $(\%)$  
![](images/3cb1b146eb7c9debb277c0d6f52cdc8c71e59fc6a8e9655ed15c52dada01d0a1.jpg)  
Source: FCAI, GS Global Investment Research

Exhibit 3: Growth in SUV (+23%) more than offset the declines in LCV (-13%) and Passenger (-5%)
YoY growth of monthly vehicle sales by type (%)  
![](images/5cbf93bb00bdc48795e3bf539af5b414b8f4e0924940aaf78f12afa92ca0da9f.jpg)  
Source: FCAI, Data compiled by GS Global Investment Research

Exhibit 5: Tesla topped the chart for the second consecutive month in Australia with EV sales +148% Monthly new vehicle sales by category (#)  
Exhibit 2: ARB's Aus Aftermarket highly correlated with LCV growth (0.8) and GS Index (0.7), both declined in 2H26 ARB Aus Aftermarket sales growth (%) vs volume growth (%)  
![](images/ebca914fddfb6f2986909cae5d47844bef103c5d3e91521ff1629f3423774b48.jpg)  
Source: FCAI, Data compiled by GS Global Investment Research, Visible Alpha Consensus Data

Exhibit 4: June is the highest volume month for LCV and 4x4 vehicle sales with 2026 well-below 2025 LCV vehicle sales by FY (#)  
![](images/17bdede43926eaee2b5ab47d48278444ed29e2315b5c58941980600f0e89f968.jpg)

![](images/494e260514cc41e82bc90c46ca083961ff1cda65e777e677dcd0061f36f8da59.jpg)  
Source: FCAI, Data compiled by GS Global Investment Research  
Source: FCAI, Data compiled by GS Global Investment Research

Exhibit 6: Volume share of China EVs has increased from $2\%$ in October 2019 to $40\%$ in June 2026 Monthly new vehicle sales by country of origin (#)  
![](images/4ef36794e53b0b9f41f05873a22ce1325b2d2aa13f367c0e632767bb8e9834a4.jpg)  
Source: FCAI, Data compiled by GS Global Investment Research

Exhibit 7: June 2026 represented a breakout/record month in a challenging market
Monthly Australian vehicle sales by type (#)

![](images/844dd1eb2393ba687b27d9db8f57048e350423f622607add14b4e43c383fce20.jpg)  
Source: FCAI, Data compiled by GS Global Investment Research

Exhibit 8: New vehicle sales remain below pre-Covid trends Rolling 12m of Australian vehicle unit sales (#)  
![](images/9395d2733801f3f285f9035fc35fdc9fa8c19eec4387b03c675d5df48e01ce57.jpg)  
Source: FCAI, Data compiled by GS Global Investment Research

Valuation methodology (ARB): Our 12m TP of A\$22.30 is based off a blended (50/50) DCF (WACC 9.2%; TGR +2.5%; RfR 3.5%) and PE multiple (20x weighted FY26/27E) valuation methodology to best represent the company's short- and long-term prospects as well as reflect how investors value the stock. Our 20x weighted multiple (vs 10-year average of 25x) reflects the lower growth outlook for ARB with our FY25-28E Npat cagr of +1.1% below its historical (pre-Covid) average of +6.5%. Key risks: 1) New vehicle sales; 2) Cost inflation; 3) Production and supply chain; 4) People and culture; 5) Reputation; 6) Distribution disruption; 7) Disruptive technology; 8) Slowdown in consumer discretionary spending.

Valuation methodology (AOV): We are Buy-rated on Amotiv (AOV.AX) with our 12m of A\$10.70 based on a blended (50/50) DCF (WACC 9.7%; TGR +1.5%; RfR +3.5%) and P/E methodology (13x weighted FY26/27E) to best represent Amotiv's short- and long-term prospects as well as reflect how investors value the stock. Our 13x P/E multiple is broadly in line with Amotiv's 10-year average and reflects a normalization in the operating environment and a stabilization in internal operations post Amotiv's strategic restructure. Downside risks (-): (1) Production and supply chain risk; (2) product technology obsolescence; (3) over-reliance on a single customer, or new entrants; (4) labour shortages; (5) acquisition and integration risk impacting operations.

## Disclosure Appendix

## Reg AC

We, Elijah Mayr and Elise Bailey, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Elijah Mayr GS Australia Pty Ltd, Elise Bailey GS Australia Pty Ltd.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for ARB Corp. and Amotiv Ltd. is/are relative to the other companies in its/their coverage universe: ARB Corp., Amotiv Ltd., Bapcor Ltd., Catapult, Chrysos Corp., Codan, Collins Food Ltd., Cuscal, Data#3 Ltd., Dicker Data Ltd., Domino's Pizza Enterprises, Duratec, Guzman y Gomez, IDP Education Ltd., Imdex, Inghams Group, Life360 Inc., Navigator Global Investments, PWR Holdings, Pinnacle Investment Management, SRG Global, Service Stream, Supply Network Ltd., Ventia

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the second most recent month end: ARB Corp. (A\$18.17)

There are no company-specific disclosures for: Amotiv Ltd. (A\$6.50)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/e7aed4fdeb7f608ff46e4cf8c5401480fbf8d66dad94fe72203d0e753662b81d.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/ecc15219d02711e6790b40f0d70d4bbae23ccbe2c46f227478d04d6880051693.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## Amotiv Ltd. (AOV.AX)

## ARB Corp. (ARB.AX)

<table><tr><td>Date of report</td><td>Target price (A$)</td><td>Closing price (A$)</td><td>Date of report</td><td>Target price (A$)</td><td>Closing price (A$)</td></tr><tr><td>11-Feb-26</td><td>10.70</td><td>8.07</td><td>25-Feb-26</td><td>22.30</td><td>24.36</td></tr><tr><td>07-Apr-25</td><td>11.00</td><td>6.83</td><td>19-Aug-25</td><td>37.10</td><td>39.49</td></tr><tr><td>12-Feb-25</td><td>12.20</td><td>9.87</td><td>18-Feb-25</td><td>38.00</td><td>39.88</td></tr><tr><td>29-Jul-24</td><td>13.00</td><td>10.61</td><td>11-Nov-24</td><td>39.20</td><td>41.75</td></tr><tr><td></td><td></td><td></td><td>20-Aug-24</td><td>40.00</td><td>42.32</td></tr><tr><td></td><td></td><td></td><td>29-Jul-24</td><td>38.50</td><td>40.15</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
