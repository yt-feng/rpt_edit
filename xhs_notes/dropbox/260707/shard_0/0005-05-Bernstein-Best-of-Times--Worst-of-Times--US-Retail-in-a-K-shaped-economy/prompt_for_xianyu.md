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
# US Retailing Broadlines & Hardlines

# Best of Times, Worst of Times: US Retail in a K-shaped economy

![](images/c066f06be8de721c5ba8e2190551e0038a0ffc6cc6f5cf5eac54b5278885f7cc.jpg)

Zhihan Ma, CFA

+1 917 344 8303

zhihan.ma@bernsteinsg.com

![](images/bc45b6dc3512ba9ca1925aa4e84e7bc5ddd002218d057b610b2edab74155783c.jpg)

Jeremy Miles, CFA

+1 917 344 8370

jeremy.miles@bernsteinsg.com

"It was the best of times, it was the worst of times". The famous opening line of Charles Dickens' 'A Tale of Two Cities' captures a period of contradiction: the French aristocracy indulging in opulence and privilege, the peasantry experiencing poverty and oppression. While 2026 is thankfully not $18^{\text{th}}$ century France, shifting class dynamics remain more topical than ever. In this note, we examine the US K-shaped economy and implications for Broadlines & Hardlines retailers.

In the US, the COVID period has given rise to an increasingly K-shaped economy. Prior to COVID, the growth in retail spending for different income groups had largely been clustered. Each group moved together, albeit from a different basis. Since COVID, there has been a notable decoupling of spend growth by income group. The difference is even more stark by education level. Between 2018 and mid-2024, the lowest income group had grown spend by \~8% on a cumulative basis, adjusted for inflation, vs. the highest income group growing at nearly double the rate (\~17%).

It's been a downward spiral for the low income cohort. Low income consumers are cash constrained and need to prioritize everyday essentials - food at home, housing, healthcare - with less bandwidth for entertainment, education, and savings. This was already the case before COVID in 2019. Since then, the gap has widened further. Given significant inflation in housing, energy and everyday essentials categories post COVID, the low income cohort has come under greater inflationary pressure in recent years. This has weighed on their ability to save and made them more susceptible to inflation, furthering the downward spiral.

If persistent inflationary pressure continues to exacerbate a K-shaped economy, what does it mean for retailers? Inflation is generally good news for retailers on the top line. This is especially the case for value oriented retailers. When inflation goes up and other retailers take price, value-oriented ones remain cheaper. We see WMT and COST as the best positioned to gain share in an environment with persistent inflation. Dollar stores could also benefit from higher income consumers seeking value and trading down, as we have seen over the last 12 months.

Meanwhile, inflationary pressure in essentials categories has weighed on discretionary spending. Walmart US, Target, and Costco have each seen staples mix up by +679bps, +770bps, and +118bps respectively since 2019 (as % net sales). For more discretionary-oriented retailers (e.g., TGT), this has had a negative margin mix impact. In the near term, we expect inflationary pressure to persist, which will reinforce the downward spiral for low income consumers as they continue to prioritize everyday purchases. Over time, as inflation normalizes and consumer spending power recovers, we see a path for discretionary spending to recover, led by smaller ticket items and higher income consumers first. Retailers with more discretionary exposure in our coverage (e.g., FIVE, DLTR, TGT) are better positioned in an environment when discretionary mix recovers.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">1 Jul 2026</td><td>TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td><td></td></tr><tr><td>Rating</td><td>Cur</td><td>ClosingPrice</td><td>PriceTarget</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>COST (Costco)</td><td>O</td><td>USD</td><td>924.67</td><td>1,194.00</td><td>(25.0)%</td><td>USD</td><td>18.21</td><td>20.64</td><td>23.30</td><td>50.8</td><td>44.8</td><td>39.7</td><td></td></tr><tr><td>DG (Dollar General)</td><td>O</td><td>USD</td><td>115.20</td><td>149.00</td><td>(19.4)%</td><td>USD</td><td>6.85</td><td>7.55</td><td>8.67</td><td>16.8</td><td>15.3</td><td>13.3</td><td></td></tr><tr><td>DLTR (Dollar Tree)</td><td>M</td><td>USD</td><td>121.15</td><td>124.00</td><td>(1.6)%</td><td>USD</td><td>5.75</td><td>7.00</td><td>7.82</td><td>21.1</td><td>17.3</td><td>15.5</td><td></td></tr><tr><td>FIVE (Five Below)</td><td>M</td><td>USD</td><td>182.64</td><td>247.00</td><td>19.8%</td><td>USD</td><td>6.67</td><td>9.28</td><td>9.33</td><td>27.4</td><td>19.7</td><td>19.6</td><td></td></tr><tr><td>HD (Home Depot)</td><td>M</td><td>USD</td><td>350.84</td><td>346.00</td><td>(24.8)%</td><td>USD</td><td>14.69</td><td>14.86</td><td>16.15</td><td>23.9</td><td>23.6</td><td>21.7</td><td></td></tr><tr><td>LOW (Lowe&#x27;s )</td><td>O</td><td>USD</td><td>221.92</td><td>281.00</td><td>(21.4)%</td><td>USD</td><td>12.29</td><td>12.69</td><td>14.14</td><td>18.1</td><td>17.5</td><td>15.7</td><td></td></tr><tr><td>TGT (Target)</td><td>M</td><td>USD</td><td>130.29</td><td>124.00</td><td>4.4%</td><td>USD</td><td>7.57</td><td>8.37</td><td>8.43</td><td>17.2</td><td>15.6</td><td>15.5</td><td></td></tr><tr><td>WMT (Walmart)</td><td>O</td><td>USD</td><td>108.82</td><td>145.00</td><td>(7.7)%</td><td>USD</td><td>2.64</td><td>3.09</td><td>3.60</td><td>41.2</td><td>35.2</td><td>30.2</td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,483.24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended WMT base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate COST, DG, WMT, and LOW Outperform. We rate DLTR, FIVE, TGT, and HD Market-Perform.

## DETAILS

## A K-SHAPED TRAJECTORY - DECOUPLED RETAIL SPEND BY COHORT SINCE COVID-19 PANDEMIC

In US Retail, the K-shaped economy is not a new phenomenon. Rather, its manifestation has been visible in data and analyses by major economists for years now. The COVID period coincided with an uncoupling of retail sales growth for different income cohorts, where they had previously grown together in the years prior. This is the result of a confluence of factors - the initial market shock, layoffs and furlough, lockdowns, stimulus and wealth transfers (e.g., SNAP), post-COVID inflation, and government policy. These are all structural, and will take time to reverse. The most obvious way the economy will normalize is through disinflation, and the return of purchasing power. It could also normalize “from the top” - through a market collapse and wealth destruction - but that is not desirable.

Analysis by Hacıoğlu Hoke et al. (2024) of the Federal Reserve shows, using Numerator data, how retail spending has grown off of the 2018 base (Exhibit 1 & Exhibit 2). $^{1}$ The trend is clear; prior to COVID, the growth in spending for different income groups had largely been clustered. Each group moved together, albeit from a different basis. Since COVID, there has been a decoupling of spend growth by income group. The difference is even more stark by education level. Between 2018 and mid-2024, the lowest income group has grown spend by \~8% adjusted for inflation. That is slightly above the rate of US population growth on a compounded basis (\~1%). In fact, the retail spend of the low income group barely grew in real terms on a cumulative basis between mid-2020 and mid-2024.

The second point that the chart shows is the impact of stimulus. The largest growth in income occurred in 2021 within the low income group (<\$60k); that was the effect of increases in SNAP, and the disproportionate impact of stimulus checks on the group.

The last point that comes out of the charts is the fact that the average data point hides the reality for low income groups. In other words, the low income and low education groups seem to be experiencing completely different macroeconomic circumstances than the general population.

EXHIBIT 1: COVID uncoupled retail sales growth across income groups.

Cumulative Growth of Average Retail Spending, by HH income (seasonally-adjusted and inflation-adjusted) - Indexed (Jan 2018 CPI = 0)  
![](images/9913a436f8b22244e0587073c6ca3e0659224f9f5a6cdbcb81524d3df05736e1.jpg)

EXHIBIT 2: Populations with lower levels of education have fared much worse than the graduate class.  
Cumulative Growth of Average Retail spending, by education (seasonally-adjusted and inflation-adjusted) - Indexed (Jan 2018 CPI= 0)  
![](images/ab0da0ba45de58fd95ee901bc2a536d2a268c904271720e6fb0370599779e850.jpg)

The data are monthly from January 2018 through August 2024. All series are adjusted for inflation using the chain indexed PCE deflator for goods and food services excluding motor vehicles and are shown as growth relative to January 2018. All series are seasonally adjusted using X13-ARIMA-SEATS. Based on authors' calculations using Numerator data.

Source: Federal Reserve, Bernstein analysis

## LOW INCOME IN A DOWNWARD SPIRAL - CASH CONSTRAINED, PRIORITIZE EVERYDAY ESSENTIALS

Low income consumers on average spend \~30-40% more than what they earn (Exhibit 3). Meanwhile, the wealthiest cohort has been able to save and invest (Exhibit 4).

Given the cash constraint, low income consumers need to prioritize everyday essentials - food at home, housing, healthcare - with less bandwidth for entertainment, education, and savings. This was already the case before COVID in 2019. Since then, the gap has widened further. The low income cohort has spent a greater proportion of their expenditures on food, housing and healthcare. Consumers across income cohorts have spent less on discretionary categories as a % of total expenditures, thanks to significant inflation in energy and food (Exhibit 5-Exhibit 6).

EXHIBIT 3: Low income consumers on average spend \~30-40% more than what they earn.  
Average Annual Expenditure, as % pre-tax income - by HH income group (2015-2024)  
![](images/45e8171a6e57cd78d34e1cd9a4c70442492ccbef51c2fd036577d0e326926341.jpg)  
Not adjusted for inflation.  
Source: US Bureau of Labor Statistics - Consumer Expenditure Surveys, Bernstein analysis  
EXHIBIT 4: The growth in wealth for the 5th quintile, even from a bigger base, far outstrips that of low income groups - wealthier people have been able to pay more, or obtain credit, and sustain the K-shaped economy.  
2019-2025 Change in Assets and Liabilities (%)
Difference between 5th Quintile ex Top 1% (80-99%) and 1st Quintile (0-20%)

![](images/b3fe13751b7c3d46e813fcf30a630d7317b854ce9d8d02be3d9e8a12cae82184.jpg)  
Not adjusted for inflation.  
Source: Federal Reserve, Bernstein analysis

EXHIBIT 5: In 2019, lower income groups spent more than other groups on essentials - food at home, housing, healthcare; they spend less on entertainment, education, and savings.

Average annual expenditures, % split by bucket, by income group - 2019

![](images/d132df52d45eda65035a2a9a974bf82155a1a32eb8f4e4c3ac4f7ddcf0e60d75.jpg)  
Not adjusted for inflation.  
Source: US Bureau of Labor Statistics - Consumer Expenditure Surveys, Bernstein analysis

EXHIBIT 6: From 2019 to 2024, lower income groups spent more on food, housing, and healthcare; the entire spectrum had a lower proportion of discretionary spend.

Average annual expenditures, % split by bucket, by income group - Delta 2019 to 2024

![](images/7f03565a005db3e156d540258c2e1785b47e744f4aa562665c69b141f5694743.jpg)  
Not adjusted for inflation.  
Source: US Bureau of Labor Statistics - Consumer Expenditure Surveys, Bernstein analysis

## LOW INCOME IN A DOWNWARD SPIRAL: UNDER GREATER INFLATIONARY PRESSURE

The pressure on the low income consumer is clear when we break out inflation experienced by income cohorts. Low income consumers have experienced greater inflationary pressure, exacerbated by inflation in housing and essentials categories post COVID. This has in turn weighed on their ability to save and made them more susceptible to inflation - it's been a downward spiral. In comparison, the highest income cohort has experienced below-average inflation as they spend a greater proportion of expenditures on discretionary categories, many of which were deflationary until recently (Exhibit 7-Exhibit 13).

EXHIBIT 7: On an indexed basis, since January 2019, the wealthiest income groups have experienced less inflation.  
Income-adjusted Chained CPI (R-C-CPI-I), by quintile - 2015 to 2024  
![](images/f80ff3d034029f0f917246894cd190c0797d8355a0f2acaa0763b2e5f1ee741a.jpg)  
Source: BLS (R-C-CPI-I) Consumer Price Index, Bernstein analysis

EXHIBIT 8: On a year-over-year basis, COVID proved to be the dislocation point.  
Income-adjusted Chained CPI (R-C-CPI-I), by quintile - 2015 to 2024 YoY Growth (%)  
![](images/3740aa87612b0aa2ead00dca0bbc865386504852da697a11e5486dce7fb79fc6.jpg)  
Source: BLS (R-C-CPI-I) Consumer Price Index, Bernstein analysis

EXHIBIT 9: Against headline CPI, we can see that wealthier income groups frequently saw lower inflation whereas inflation for the 1st quintile was sustained.

Income-adjusted Chained CPI (R-C-CPI-I), by quintile - 2015 to 2024 Less Headline CPI (All Items)  
![](images/ac0830d5a86a5de204fb48a13372fa099c0c38cc1d39518e8c18da36da20534b.jpg)  
Source: BLS (R-C-CPI-I) Consumer Price Index, Bernstein analysis  
EXHIBIT 10: The overwhelming driver of <\$50k HH income expenditure increases has been housing, where many are renters. Increases in staple foods, transportation, and healthcare expenditure come from inflationary pressures.

Average Annual Expenditure, 2015 to 2024 growth contribution by bucket (%) <\$50k HH income  
![](images/0ef8ab4b8893a426aa122f995f663a417a809f777796461f7b4860a67ca73993.jpg)  
Not adjusted for inflation.  
Source: US Bureau of Labor Statistics - Consumer Expenditure Surveys, Bernstein analysis

EXHIBIT 11: Analyzing expenditure growth for the <\$50k HH income group shows how much restraint low income groups have shown on discretionary categories.

Remember, inflation in this period was MSD

CAGR (YoY, %) - Pre-Tax Income and Expenditure, by bucket - 2019 to 2024 <\$50k HH Income

![](images/0dd01feb69b1abdf3f40f6155c722488c9a38da8aae62bfa7a877eba70080974.jpg)  
Not adjusted for inflation.  
Source: US Bureau of Labor Statistics - Consumer Expenditure Surveys, Bernstein analysis

EXHIBIT 12: While the same categories saw expenditure growth in the high income group, the savings category grew by +850bps relative to the low income group; the wealthy have been able to save despite inflation.

Average Annual Expenditure, 2019 to 2024 growth contribution by bucket (%) >\$100k HH income

![](images/9c94d74d91c8a40e1aa1b1805d1e7bcabbe261da6a344687c3d88aa6313079c3.jpg)  
Not adjusted for inflation.  
Source: US Bureau of Labor Statistics - Consumer Expenditure Surveys, Bernstein analysis

EXHIBIT 13: Taking the difference in CAGR between high and low income groups shows high income groups' discretionary spending power - food away from home, transport, personal care - have all been growing faster.

CAGR (YoY, %) - Pre-Tax Income and Expenditure, by bucket - 2019 to 2024
Difference between >\$100k and <\$50k HH Income

![](images/61f9c0c65348ecdbf875a714a4f2c0f7f41fe16b1708de5e3c9d19c2883f6c6b.jpg)  
Not adjusted for inflation.  
Source: US Bureau of Labor Statistics - Consumer Expenditure Surveys, Bernstein analysis

## IMPLICATIONS FOR RETAILERS - MIX AND SHARE SHIFTS

If persistent inflationary pressure continues to exacerbate a K-shaped economy, what does it mean for retailers?

Inflation is generally good news for retailers on the top line. This is especially th

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
