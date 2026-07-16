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
U.S. Restaurants

# Best of Times, Worst of Times: US Restaurants - A Tale of Two Diners

![](images/2c8e4db9b82c590978cdbdfbc14657dee9a192eb5aa4eed1f2c8bda5edc1ae52.jpg)  
Danilo Gargiulo  
+1 917 344 8475  
danilo.gargiulo@bernsteinsg.com

"It was the best of times, it was the worst of times". The famous opening line of Charles Dickens' 'A Tale of Two Cities' captures a period of contradiction: the French aristocracy indulging in opulence and privilege, the peasantry experiencing poverty and oppression. While 2026 is thankfully not $18^{\text{th}}$ century France, shifting class dynamics remain more topical than ever, from the US K-shaped economy to the squeezed Chinese middle class. In this note, we examine to what extent the consumption has shifted also across restaurants - a sector notoriously resilient through the cycles - and we explore which brands have been most exposed to the K-shaped dynamic.

Restaurant demand is increasingly being driven by affluent diners, while lower-income diners continue to exit the category. Credit card data show affluent consumers (>\$100k income) increasing both spending and visit frequency since 2022, while lower-income consumers (<\$45k) have lost share across virtually every major restaurant concept. Importantly, we think the divergence is primarily traffic-driven rather than check-driven. Brands such as Cava, Chipotle, Starbucks, and LongHorn Steakhouse exhibit particularly high exposure to higher-income households, and appear to be among the largest beneficiaries of affluent customer growth. Other things being equal, this suggests that restaurant demand is increasingly being supported by consumers who remain relatively insulated from inflation and macroeconomic pressures.

At the same time, every brand in our analysis lost exposure to consumers earning less than \$45k between 2Q22 and 2Q25, with the largest declines occurring at Wingstop, Chipotle, Taco Bell, and Starbucks. Broadening the perspective to the entire sector, we think the results are consistent with a combination of cumulative menu price inflation (FAFH inflation +35% since 2019 vs +25% CPI) and a trade-down toward grocery spending, and suggest that industry-wide value promotions have had sporadic success in rebuilding lower-income traffic.

A key takeaway from the analysis is that income-related differences are driven more by frequency than ticket size. We find that average spend per transaction is relatively similar across income cohorts at most brands, while spend per user rises much more meaningfully with income. This leads us to believe that affluent consumers are not necessarily spending materially more per visit, but rather visiting more often and generating a disproportionate share of industry growth.

We expect companies that have demonstrated proficiency in offering a barbell menu strategy to emerge more resilient. This means, offering premium innovation, scarcity value (LTOs and merch) and enhanced convenience to attract consumers willing to pay a premium, while establishing disciplined pricing, targeted promotions, and sharp, consistent entry price points to entice low income consumers to return to visit restaurants.

Ultimately we don't expect the dynamics of the K-shaped economy to reverse any time soon, and, other things being equal, we would therefore continue to prefer companies with high income consumer exposure (SBUX, CAVA, CMG) .....Continued on pg 2

or those that appear to be more insulated from these dynamics (DRI, PFGC, USFD, SYY). Conversely, a rebound of low income consumers would likely disproportionately benefit MCD, DPZ, QSR, YUM and WING.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">14 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>CAVA (Cava)</td><td>O</td><td>USD</td><td>69.97</td><td>95.00</td><td>(42.5)%</td><td>USD</td><td>0.54</td><td>0.60</td><td>0.86</td><td>129.8</td><td>117.3</td><td>81.1</td></tr><tr><td>CMG (Chipotle)</td><td>O</td><td>USD</td><td>36.43</td><td>50.00</td><td>(53.9)%</td><td>USD</td><td>1.19</td><td>1.21</td><td>1.43</td><td>31.2</td><td>32.2</td><td>26.0</td></tr><tr><td>DRI (Darden)</td><td>O</td><td>USD</td><td>195.74</td><td>230.00</td><td>(26.9)%</td><td>USD</td><td>10.64</td><td>11.30</td><td>12.24</td><td>18.9</td><td>17.4</td><td>16.0</td></tr><tr><td>DPZ (Domino&#x27;s)</td><td>M</td><td>USD</td><td>309.85</td><td>390.00</td><td>(54.8)%</td><td>USD</td><td>17.57</td><td>18.79</td><td>20.94</td><td>17.6</td><td>16.5</td><td>14.8</td></tr><tr><td>MCD (McDonald&#x27;s)</td><td>M</td><td>USD</td><td>268.94</td><td>310.00</td><td>(31.3)%</td><td>USD</td><td>12.20</td><td>12.47</td><td>13.47</td><td>22.0</td><td>21.6</td><td>20.0</td></tr><tr><td>PFGC (PFG)</td><td>O</td><td>USD</td><td>112.99</td><td>130.00</td><td>(4.2)%</td><td>USD</td><td>4.48</td><td>5.23</td><td>6.32</td><td>25.2</td><td>21.6</td><td>17.9</td></tr><tr><td>QSR (QSR)</td><td>O</td><td>USD</td><td>74.61</td><td>95.00</td><td>(9.5)%</td><td>USD</td><td>3.70</td><td>4.17</td><td>4.51</td><td>20.2</td><td>17.9</td><td>16.5</td></tr><tr><td>SBUX (Starbucks)</td><td>O</td><td>USD</td><td>106.17</td><td>110.00</td><td>(6.7)%</td><td>USD</td><td>2.13</td><td>2.36</td><td>3.05</td><td>65.0</td><td>57.6</td><td>34.7</td></tr><tr><td>SYY (Sysco)</td><td>M</td><td>USD</td><td>82.85</td><td>85.00</td><td>(13.7)%</td><td>USD</td><td>4.46</td><td>4.58</td><td>4.85</td><td>18.6</td><td>18.1</td><td>17.1</td></tr><tr><td>USFD (US Foods)</td><td>O</td><td>USD</td><td>101.00</td><td>106.00</td><td>2.9%</td><td>USD</td><td>3.98</td><td>4.77</td><td>5.61</td><td>25.4</td><td>21.2</td><td>18.0</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.68</td><td>5.66</td><td></td><td></td><td></td></tr><tr><td>WEN (Wendy&#x27;s )</td><td>M</td><td>USD</td><td>7.42</td><td>9.00</td><td>(52.3)%</td><td>USD</td><td>0.90</td><td>0.59</td><td>0.82</td><td>8.7</td><td>14.9</td><td>9.6</td></tr><tr><td>WING (Wingstop)</td><td>O</td><td>USD</td><td>148.41</td><td>220.00</td><td>(73.7)%</td><td>USD</td><td>4.12</td><td>4.77</td><td>5.40</td><td>36.0</td><td>31.1</td><td>27.5</td></tr><tr><td>YUM (Yum! )</td><td>M</td><td>USD</td><td>158.18</td><td>170.00</td><td>(12.9)%</td><td>USD</td><td>6.06</td><td>6.53</td><td>7.28</td><td>28.3</td><td>23.9</td><td>22.4</td></tr><tr><td>SPX</td><td></td><td></td><td>7,543.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended CAVA, CMG, DRI, SBUX, WEN, YUM valuation is Reported P/E (x); DRI base year is 2026; Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate 8 companies as Outperform: CAVA, CMG, DRI, QSR, SBUX, WING, USFD, and PFGC. We rate 5 companies as Market-Perform: DPZ, MCD, WEN, YUM, and SYY.

## DETAILS

## OVERVIEW

The US consumer backdrop has become increasingly K-shaped. Wealth concentration has risen steadily over the past several decades, with the top 1% now controlling roughly 25% of household wealth versus 17% in 1990, while the middle class accounts for a shrinking share of national wealth. At the same time, income growth has disproportionately accrued to higher-income households, leaving lower-income consumers more exposed to inflation in essential categories and increasingly constrained in their discretionary spending.

Consumer expenditure data show that lower-income households devote materially larger portions of their budgets to necessities, while higher-income consumers allocate a greater share toward savings and investments. Importantly, consumer confidence has weakened across all income cohorts but remains lowest among lower-income households, reinforcing the growing bifurcation in spending behavior.

Bernstein's K-shaped spending index ranks food away from home among the most income-skewed consumer categories, with the highest-income households spending 4.6x more than the lowest-income households in 2024. Moreover, restaurant spending has become more K-shaped since the pandemic, as the spending gap between affluent and lower-income consumers has widened. Food-away-from-home spending contracted sharply in 2020 and has only partially recovered. While higher-income consumers have largely resumed restaurant spending, lower-income households continue to allocate a meaningfully lower share of wallet to restaurants than before COVID. Over the last two decades, lower-income cohorts have reduced restaurant spending as a share of expenditures by roughly 40bps, with the most pronounced decline occurring in the past five years as inflation and affordability pressures intensified. Meanwhile, spending on food at home has increased, particularly among lower-income consumers.

Higher-income households continue to sustain dining frequency and, in some cases, trade up, while lower-income consumers are trading down, reducing visits or shifting spending toward groceries. We think this dynamic helps explain the ongoing outperformance of concepts exposed to middle- and upper-income consumers, while value-oriented and lower-income-focused restaurant operators remain more vulnerable to pressured discretionary budgets.

EXHIBIT 1: The top 1% in terms of households by income account for 25% of US wealth today vs. 'just' 17% in 1980

Share of Household Wealth (Net Worth) by Income Quintile  
![](images/01478fdab811c037263c5e1cb467d4b78efa65f415b0a2a73d1e40c0ae30b36a.jpg)  
Source: Federal Reserve, Bernstein analysis

EXHIBIT 2: The lowest 20% spend disproportionately more of their income on shelter, utilities/fuel food at home and health care  
Share of expenditure, by type & income (2024)  
![](images/e221bcc86e518b7875793c6beb013aa50e9b741b843948afb57ba8e608e8dfa0.jpg)  
Source: US Bureau of Labor Statistics' Consumer Expenditure Survey, Bernstein analysis

CARS, :shaped sectors, with tobacco and food at home being the least

Bernstein K-Shaped index (annual expenditure ratio top 20% earner to bottom 20% earners, 2024)

![](images/c943a00dcb0489d02b677cf4d7f3311af703a35d5dc34e7d236389b4bd2c6817.jpg)  
Source: US Bureau of Labor Statistics' Consumer Expenditure Survey, Bernstein analysis

EXHIBIT 3: Food away from home spending declined modestly as a % of total annual expenditures pre pandemic, followed by a sharp contraction in 2020 and a partial recovery thereafter. The recovery remains incomplete, particularly for lower-income cohorts.

FOOD AWAY FROM HOME
Average share of annual expenditure  
![](images/206c8142b870f74986b706f97a68e43db12c9ae2a415282dfdd6597a5406063a.jpg)  
Source: US Bureau of Labor Statistics' Consumer Expenditure Survey, Bernstein analysis  
EXHIBIT 5: The ratio of spending on food away from home between top earners and bottom earners compressed over the long term through the mid-2010s, but has re-expanded after the pandemic only to dip again in 2024  
EXHIBIT 4: The decline and subsequent recovery in food away from home spending has been uneven across income groups, with lower-income households seeing the largest sustained reduction in share of wallet

FOOD AWAY FROM HOME
Change in average share of annual
expenditure (2004-2024)  
![](images/56cb140348422d77cdd82aeee1fd4c73f237ea62648d1bc99aebcb203bec3f69.jpg)  
Source: US Bureau of Labor Statistics' Consumer Expenditure Survey, Bernstein analysis

FOOD AWAY FROM HOME
Bernstein K-Shaped index (annual expenditure ratio top 20% earner to bottom 20% earners)  
![](images/437179f89d470933d2bc5c675605eeb6401181ae1afbe9dcef12c960e9adecd6.jpg)  
Source: US Bureau of Labor Statistics' Consumer Expenditure Survey, Bernstein analysis  
EXHIBIT 6: Food away from home has become more K-shaped in recent years. While the long-term trend showed mild compression (2004–2019), the top-to bottom spending ratio has widened by \~0.4x since 2019

FOOD AWAY FROM HOME
Change in Bernstein K-Shaped index  
![](images/ff01f31d66447edf828cb43057b4d2fffba1aa7b7c88ebd164ce56e2c8cf8957.jpg)  
Source: US Bureau of Labor Statistics' Consumer Expenditure Survey, Bernstein analysis

## CREDIT CARD DATA ANALYSIS

The analysis in this note is derived from aggregated credit card transaction data between 2022 and 2Q 2025. Credit card data excludes cash payments, debit card transactions, and importantly, stored card value (e.g. Starbucks Rewards with its 35 million active users) that may not route through a standard card network. Lower-income cohorts (where cash usage remains proportionally higher) are likely underrepresented in both user counts and spend figures relative to their true share of restaurant traffic. Note that the data below is also not adjusted for inflation, but we think the directional findings and relative brand rankings are consistent with third-party survey data, and management commentary across earnings calls.

The US restaurant sector is also bifurcating along income lines, consistent with the broader economy. Credit card transaction data across 13 major chains reveals a structurally segmented consumer base: affluent households ( $>\$100k$ annual income) dominate spending at virtually every chain, including fast food, while lower-income consumers ( $<\$45k$ ) have meaningfully reduced their share of restaurant transactions over the past three years. We believe that this bifurcation is driven by several factors.

1. Lower disposable income availability. With the lapsing of the Covid-related benefits, low-income consumers have become more discerning with their marginal dollar, reflecting greater caution as the earnings and spending behaviors normalized

2. Relative inflation of restaurants vs other discretionary goods. Following labor shortages, supply chain disruptions, rising commodity costs and increasing minimum wages (especially in California, following the implementation of the FAST Act in April 2024, restaurants have taken an opportunity to increase the prices to protect their margins that were under significant pressure. As a result, the ‘excess pricing’ of restaurants (defined as restaurant pricing above CPI inflation) rose from the historical average of 60bps per year (1960 to 2019) to 110+ bps annually (2020-2026). Low income consumers, that tend to display higher price elasticity, likely responded to price increases with lower frequency of transaction.

3. Trade-down to grocery. We believe that especially low income consumer have traded down to grocery not only as the budget constraints have tightened but also because the relative inflation of grocery has been far lower than restaurant inflation - resulting in improving value positioning for grocery relative to restaurants. Again, a dynamic that impacts more low income consumers not only for the lower income availability but also for the greater price elasticity.

Our analysis of credit card data shows that:

\- High-income ( $>$ 100K in annual income): Overall increased total spending by $\sim 70\%$ since 2022 and transactions by $55\%$ , compounding growth in both occasions and check size.

\- Middle-income (\~\$45K–\$100K): Broadly flat consumption levels, with modest recent softening - especially in transactions.

\- Low-income (<\$45K): A deteriorating trajectory from 2023, reducing transactions and spend by 25%-35% from the 2022 baseline. With spend per transaction remaining fairly constant, we think this means that the divergence is traffic-driven rather than solely driven by average check - which could be harder to rebuild once the 

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
