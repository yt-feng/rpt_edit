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
EUROPE AUTOMOBILES

# China Retail Chartbook Jun-26: Broad-based volume decline, pricing more resilient; BMW M outperforms

This series tracks the retail volume and average transaction price (ATP) of domestically produced and imported vehicles from Germany's premium and luxury OEMs in China - Mercedes, BMW and Porsche - complementing our China Retail Volume Dashboard (Jun-26), which covers domestically produced vehicles only. China's vehicle import market has been shrinking at c.-11% CAGR since 2019 as foreign OEMs deepen localisation and domestic premium challengers gain ground. Yet imported models still command far higher ATPs and margins than JV products.

Mercedes sold 24,800 units through JV (R1/3/6/12M -41.8%/-32.8%/-31.2%/-28.3%) and 6,869 imported vehicles (R1/3/6/12M -17.9%/-22.3%/-24.1%/-25.0%) in Jun-26, of which Top-End Vehicles (TEV) accounted for 2,779 units, -27.6% yoy. The ATP of import declined to ¥908k, -11.6% yoy (o/w TEV at ¥1.4mn, -12.6% yoy), while JV ATP came in at ¥298k, -7.8% yoy.

☐ The S-Class sold 1,059 units in Jun-26, -38.8% yoy, with more than half being the Maybach version, though the Maybach's transaction price fell sharply during the month. Its local competitor, the Maextro S800, recorded 593 units in Jun-26, a marked step-down from its earlier peak of over 4k units. GLE performed well (+11.5% yoy) even ahead of its upcoming localisation.

□ Mercedes’ implied retail revenue from imported cars reached ¥6.2bn in Jun-26 (-27.4% yoy) and ¥18.7bn in 2Q26 (-24.9% yoy). JV implied retail revenue was ¥10.4bn (-25.0% yoy) in Jun-26 and ¥27.9bn in 2Q26 (-28.8% yoy).

BMW sold 33,073 units through JV (R1/3/6/12M -32.7%/-28.9%/-18.1%/-13.5%) and 3,725 imported vehicles in Jun-26 (R1/3/6/12M -45.6%/-43.6%/-34.4%/-20.4% yoy). By contrast, import ATP rose to ¥499k, +6.5% yoy. JV ATP remains under pressure at ¥310k, -7.0% yoy. On a consolidated basis, implied retail revenue for BMW's total car sales in China reached ¥13.2bn in Jun-26 (-34.9% yoy) and ¥36.3bn in 2Q26 (-34.6% yoy).

☐ We highlight the resilience of the M line-up, with volume of 423 units in Jun-26, +9.9% yoy, and ATP of ¥829k, +5.4% yoy. This sustained growth

Christian Frenes
+44(20)7051-8641 |
christian.frenes@gs.com
GS International

Monika Mengting Liu, CFA
+44(20)7051-7601 | monika.liu@gs.com
GS International

Shivam Kotecha
+1(332)245-7822 |
shivam.kotecha@gs.com
GS India SPL

Robert Triulzi
+44(20)7552-2281 |
robert.triulzi@gs.com
GS International

underscores the enduring appeal of M as a halo performance brand, carving out a durable niche for driving-experience focused ICE vehicles even as the broader import market softens.

Porsche sold 2,188 vehicles in China in Jun-26 (R1/3/6/12M -46.2%/-41.2%/-36.0%/-27.5% yoy). ATP came in at ¥980k, -6.2% yoy. Within the range, the 911 held up relatively well at ¥1.68mn, -5.6% yoy, whereas the Taycan was the principal drag on the blended ATP, -24.8% yoy. The implied retail revenues would be ¥2.1bn in Jun-26 (-49.5% yoy) and ¥6.5bn in 2Q26(-47.1% yoy).

<table><tr><td colspan="3">Historicals vs. recent R12M</td></tr><tr><td>FY25</td><td>104,002</td><td>14.7%</td></tr><tr><td>Max (FY21)</td><td>175,699</td><td>93.7%</td></tr><tr><td>5yr median</td><td>156,168</td><td>72.2%</td></tr></table>

<table><tr><td colspan="3">Historicals vs. recent R12M</td></tr><tr><td>Min</td><td>237,896</td><td>-36.8%</td></tr><tr><td>Max</td><td>693,720</td><td>84.2%</td></tr><tr><td>5yr median</td><td>564,339</td><td>49.8%</td></tr></table>

## Mercedes

Exhibit 1: Mercedes JV volume: 24,800 units sold in Jun-26, R1/3/6/12M at -41.8%/-32.8%/-31.2%/-28.3% yoy.

<table><tr><td colspan="3">Registrations (units) and yoy (%)</td></tr><tr><td>R1M</td><td>24,800</td><td>-41.8%</td></tr><tr><td>R3M</td><td>77,598</td><td>-32.8%</td></tr><tr><td>R6M</td><td>165,727</td><td>-31.2%</td></tr><tr><td>R12M</td><td>376,668</td><td>-28.3%</td></tr></table>

![](images/b3c60244446bf88530b226315f6e7b21872e36365d35d95d3db5d1c52338c8cb.jpg)  
Source: CPCA, GS Global Investment Research

![](images/b8a2afea2c3733069ab1bcd1030fa11a795f2806d23c2e2625cef2eb22a2e321.jpg)

![](images/d5578c6a078e140d2e39784449bfb131deadd6100d526e113ec7b865d61c281b.jpg)

Exhibit 2: Mercedes import volume: 6,869 units sold in Jun-26 (R1/3/6/12M -17.9%/-22.3%/-24.1%/-25.0%), of which TEV accounted for 2,779 units, -27.6% yoy.

<table><tr><td colspan="3">Import retail volume (units) and yoy (%)</td></tr><tr><td>R1M</td><td>6,869</td><td>-17.9%</td></tr><tr><td>R3M</td><td>19,194</td><td>-22.3%</td></tr><tr><td>R6M</td><td>41,018</td><td>-24.1%</td></tr><tr><td>R12M</td><td>90,703</td><td>-25.0%</td></tr></table>

![](images/b78dcd918045a2a5e75429983e838d51ea11325bd503aa072c9dea7a1fbf06e7.jpg)

![](images/54c280d3c828c6d4c2204fcd48b29e12da51383d4036dd76c2488a917b404c44.jpg)  
Source: Sina Auto, CPCA, GS Global Investment Research

![](images/48172b4427dfaaa92d44973307b91630a96dcdf0bcceb0aa17885ad5ea7637c6.jpg)

Exhibit 3: Mercedes import ATP declined to ¥908k, -11.6% yoy, mainly driven by GLE and E-Class. TEV ATP stood at ¥1.4mn, -12.6% yoy, due to S-Class Maybach. JV ATP declined to ¥298k, -7.8% yoy, driven by core ICE model pricing weakness such as E-Class and GLC.

![](images/dec578ff0efa7218efd326b2e9b3ab2b252c5f97e7f4a7f0e5541c3e19595a23.jpg)  
Source: Sina Auto, GS Global Investment Research  
Exhibit 4: Mercedes implied retail revenue from imported cars would reach ¥6.2bn in Jun-26 (-27.4% yoy) and ¥18.7bn in 2Q26 (-24.9% yoy). JV implied retail revenue was ¥10.4bn (-25.0% yoy) in Jun-26 and ¥27.9bn in 2Q26 (-28.8% yoy).

Mercedes implied retail revenues - import vs. JV, RMB mn  
![](images/f54c34ab11f118e15d76364e13a8e3a8a82cd8b1604ca44212b3a4a4945fa788.jpg)  
Source: Sina Auto, GS Global Investment Research

## BMW

Exhibit 5: BMW JV volume: 33,073 units sold in Jun-26, R1/3/6/12M at -32.7%/-28.9%/-18.1%/-13.5% yoy.

<table><tr><td colspan="3">Registrations (units) and yoy (%)</td></tr><tr><td>R1M</td><td>33,073</td><td>-32.7%</td></tr><tr><td>R3M</td><td>98,059</td><td>-28.9%</td></tr><tr><td>R6M</td><td>220,972</td><td>-18.1%</td></tr><tr><td>R12M</td><td>484,682</td><td>-13.5%</td></tr></table>

<table><tr><td colspan="3">Historicals vs. recent R12M</td></tr><tr><td>Min</td><td>282,000</td><td>-41.8%</td></tr><tr><td>Max</td><td>717,269</td><td>48.0%</td></tr><tr><td>5yr median</td><td>640,345</td><td>32.1%</td></tr></table>

![](images/0772aa9bde2d922815cc510763b0ec8f181991cd4ae3c3e15b73056618e72473.jpg)  
Source: CPCA, GS Global Investment Research

![](images/0eba7fc40eb0f2ecb44db15ce9bf0d14dd1b87b25016dbd02bb9fbbbd14c99ac.jpg)

![](images/3fd177836840c54343bbb6ddcff7d400a5f7c551c2ea5c54067caf9d2c94ca23.jpg)

Exhibit 6: BMW import volume: 3,725 units sold in Jun-26 (R1/3/6/12M -45.6%/-43.6%/-34.4%/-20.4% yoy). We highlight the resilience of the M line-up, with volume of 423 units, +9.9% yoy.

<table><tr><td colspan="3">Import retail volume (units) and yoy (%)</td></tr><tr><td>R1M</td><td>3,725</td><td>-45.6%</td></tr><tr><td>R3M</td><td>11,046</td><td>-43.6%</td></tr><tr><td>R6M</td><td>24,740</td><td>-34.4%</td></tr><tr><td>R12M</td><td>59,770</td><td>-20.4%</td></tr></table>

<table><tr><td colspan="3">Historicals vs. recent R12M</td></tr><tr><td>FY25</td><td>65,181</td><td>9.1%</td></tr><tr><td>Max (FY19)</td><td>172,840</td><td>189.2%</td></tr><tr><td>5yr median</td><td>102,910</td><td>72.2%</td></tr></table>

![](images/82b83524d85213475f1c425ab48ce4ce6543748e61bbad164fb59f2754a1232e.jpg)

![](images/2355341ddef3e5e472b9e602a615c408a74f93e82b8c748644333fd895fb1e25.jpg)  
Source: Sina Auto, GS Global Investment Research

![](images/4e65798c40b14673fbb6ddde16ba5fc522fbcc5e51d50f94f929c6e2e958e139.jpg)

Exhibit 7: BMW import ATP rose to ¥499k in Jun-26, +6.5% yoy, of which M ATP at ¥829k, +5.4% yoy. JV ATP remains under pressure at ¥310k, -7.0% yoy.  
![](images/f88fae9b7a9de4ca37d457ec24e12603b270e25e06b96ef80c432e8c63780239.jpg)  
Source: Sina Auto, GS Global Investment Research

Exhibit 8: On a consolidated basis, the implied retail revenues for BMW's total car sales in China would reach ¥13.2bn in Jun-26 (-34.9% yoy) and ¥36.3bn in 2Q26 (-34.6% yoy).  
![](images/6575811bd8626ec7307466aab91cdf9d59ded14b50253816598803104e4b3bf0.jpg)  
Source: Sina Auto, GS Global Investment Research

Exhibit 10: Porsche's ATP in Jun-26 in China was ¥980k, -6.2% yoy. The 911 ATP stood at ¥1.68mn, down -5.6% yoy in Jun-26, while Taycan was the main driver for the total ATP decline (-24.8% yoy).

<table><tr><td colspan="3">Import retail volume (units) and yoy (%)</td></tr><tr><td>R1M</td><td>2,188</td><td>-46.2%</td></tr><tr><td>R3M</td><td>6,796</td><td>-41.2%</td></tr><tr><td>R6M</td><td>12,808</td><td>-36.0%</td></tr><tr><td>R12M</td><td>34,734</td><td>-27.5%</td></tr></table>

## Porsche

Exhibit 9: Porsche sold 2,188 vehicles in Jun-26 (-46.2% yoy) in China. Its retail decline is accelerating, with R1/3/6/12M -46.2%/-41.2%/-36.0%/-27.5% yoy.

![](images/a9165eac07e6f4e197ea02d3f9d2c30ab24ef2b172d3ed51e7e6bf0809166e59.jpg)

![](images/22d58f02e5421758b8db1d049fc0167ecc5e004f1d828b2f8518999bd4ab2b0b.jpg)  
Source: Sina Auto, GS Global Investment Research

![](images/03af5863d5935ccfb42b2950befb3febae866640d8274a6bdba03d9327ed7c4f.jpg)

![](images/1e79655212de11f76a4e366c8dde94244d585fd895fd3a930b02b15aeae27976.jpg)  
Source: Sina Auto, GS Global Investment Research  
Exhibit 11: The implied retail revenues for Porsche in China would reach ¥2.1bn in Jun-26 (-49.5% yoy) and ¥6.5bn in 2Q26 (-47.1% yoy).

![](images/5324d4164bb711a94f54471b0f47c0f71d3feea41706fd7f53653f29cbe85518.jpg)  
Source: Sina Auto, GS Global Investment Research

## Appendix

Exhibit 12: The Mercedes S-Class sold 1,059 units in Jun-26, -38.8% yoy, of which more than half were the Maybach version (574 units).

![](images/f608954ed3c8a30a267f06a15cfd166025366ddf5331af7c450d6853746b7938.jpg)  
Source: Sina Auto, GS Global Investment Research

Exhibit 13: The S-Class' local competitor, the Maextro S800, recorded 593 units in Jun-26, a sharp decline from its peak of over 4,000 units.  
![](images/e5b9fd790880bc5abb960f6294b409d2a7aeb56dde29bd4b8cb4019462d933a2.jpg)  
Source: Sina Auto, CPCA, GS Global Investment Research

Exhibit 14: China's vehicle import market has been shrinking at c. -11% CAGR since 2019 as foreign OEMs deepen localisation and domestic premium challengers gain ground.  
![](images/6918a4fb279c7f166a94a655640a6eaa9b72e073bd0fd09e9136a2a2258429c7.jpg)  
Source: CADA, GS Global Investment Research

Exhibit 15: Within the import segment, German brands remain resilient, holding close to 50% share collectively.  
China import segment market share by brand, %  
![](images/8f9e191557a2e26c85c2358fe3d34c7a8f79a279b4e3a24b74b5bf7090dd9164.jpg)  
Source: CADA, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Christian Frenes, Monika Mengting Liu, CFA, Shivam Kotecha and Robert Triulzi, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Christian Frenes GS International, Monika Mengting Liu, CFA GS International, Shivam Kotecha GS India SPL, Robert Triulzi GS International.

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

Distribution of ratings/investment banking relationships
GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclo

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
