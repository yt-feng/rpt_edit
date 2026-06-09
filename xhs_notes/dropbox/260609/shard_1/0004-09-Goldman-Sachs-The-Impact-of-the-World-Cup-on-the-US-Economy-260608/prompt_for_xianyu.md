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
# US ECONOMICS ANALYST

# The Impact of the World Cup on the US Economy

The 2026 World Cup will take place in the US, Mexico, and Canada from June 11 to July 19. An estimated 5-6 million fans will attend 78 matches in the US. More matches will occur in June, but the audience for each match is likely to be much larger during the knockout stage that mostly occurs in July. The matches in the US will be hosted by 11 metropolitan areas that together account for roughly one third of US GDP and one quarter of US employment and the CPI index.

We use historical data from the 1994 US World Cup, 20 years of Super Bowls, and the Olympic Games in Los Angeles, Atlanta, and Salt Lake City to estimate the impact on upcoming economic data releases including payrolls, retail sales, consumer spending, GDP, and CPI and PCE inflation.

The effects of major sporting events tend to be short-lived, reversing in the months following the event. Even so, having a sense of the magnitude of their impact will be useful for distinguishing temporary World Cup effects from changes in underlying economic trends in coming months.

Payroll employment rose 80k above trend in host cities during the 1994 US World Cup and 40k during past Summer Olympics in the event months, before mostly reverting to trend thereafter. The increases were concentrated in leisure and hospitality, retail trade, and transportation around the event, while business services saw earlier hiring in the preceding months for support activities. Scaling to the size of the current World Cup and allowing for some impact already, we estimate a 40k boost to payroll growth in June, a 10k boost in July, a 15k drag after the Cup ends in August, and further gradual reversals in subsequent months as temporary positions end.

GDP should also get a small boost concentrated in consumer spending and exports of services to foreign tourists, an extra $1/2 - 1mn$ of whom are likely to arrive in June and July. We use tourist spending data from the 1994 World Cup and state-level GDP during past Super Bowls to estimate the impact on activity, rescaling to the larger size of the current World Cup. We estimate a boost of 0.3pp in June and 0.1pp in July to retail sales growth, which does not distinguish between spending by residents and foreigners. We expect modest boosts of 0.1pp in Q2 and 0.05pp in Q3 to annualized GDP growth, which should then give way to a small drag in Q4.

■ Prices for hotels have already spiked, and city-level CPI data show that prices for

## Pierfrancesco Mei

+1(212)902-8809

pierfrancesco.mei@gs.com

GS & Co. LLC

## David Mericle

+1(212)357-2619

david.mericle@gs.com

GS & Co. LLC

restaurant meals and transportation also tend to jump in host cities around major sporting events. But the effects of past events on inflation have varied widely, which makes the impact of the World Cup more uncertain. We estimate that it will provide a boost in June of 0.03pp to core CPI inflation and 0.04pp to core PCE, which includes restaurant services, unlike core CPI. We expect a 1bp incremental boost in July, followed by a drag of 1bp in August that continues in later months.

## The Impact of the World Cup on the US Economy

The 2026 FIFA World Cup will take place in the US, Mexico, and Canada from June 11 to July 19. An estimated 5-6 million fans will attend 78 matches in the US. More matches will occur in June, but the audience for each match is likely to be much larger during the knockout stage that mostly occurs in July. As Exhibit 1 shows, the matches in the US will be hosted by 11 metropolitan statistical areas (MSAs) that together account for roughly one third of US GDP and one quarter of US employment and the CPI index.

Exhibit 1: World Cup Matches Will Take Place in 11 Metropolitan Areas Representing One Third of US GDP

<table><tr><td colspan="2">2026 FIFA World Cup in the US</td></tr><tr><td colspan="2">Basic Facts</td></tr><tr><td>US Metropolitan Areas Hosting the Matches*</td><td>11</td></tr><tr><td>Dates</td><td>June 11 - July 19</td></tr><tr><td>Number of Matches</td><td>78</td></tr><tr><td>Estimated Number of Match Attendees</td><td>5-6 Million</td></tr><tr><td colspan="2">Economic Facts About the 11 Host Metropolitan Areas</td></tr><tr><td>Share of US GDP</td><td>32%</td></tr><tr><td>Share of Total US Employment</td><td>23%</td></tr><tr><td>Weight in the CPI Index</td><td>26%</td></tr></table>

\* Matches will be played in the following metropolitan areas: Atlanta, Boston, Dallas, Houston, Kansas City, Los Angeles, Miami, New York City/New Jersey, Philadelphia, San Francisco Bay Area, and Seattle.  
Source: GS Global Investment Research, Bureau of Economic Analysis, US Bureau of Labor Statistics, FIFA

In this week's Analyst, we draw on historical data from the 1994 US World Cup, two decades of Super Bowls, and the Summer Olympic Games held in Los Angeles (1984), Atlanta (1996), and Salt Lake City (2002) to estimate the tournament's impact on upcoming economic data releases, including payrolls, retail sales, consumer spending, GDP, and CPI and PCE inflation.

The economic effects of major sporting events tend to be short-lived, largely reversing in the months following the event. Even so, knowing the rough size of these effects will be important for distinguishing temporary World Cup-related distortions from shifts in underlying economic trends in the months ahead.

## Impact on Payrolls

Payroll employment rose 80k above trend in host cities during the 1994 US World Cup and 40k on average during past Summer Olympics in the event months, before largely reverting to trend in the following months (Exhibit 2). Job gains during the events were concentrated in leisure and hospitality, retail trade, and transportation, while professional and business services hiring tended to accelerate in the months preceding the event to support logistics and operations. Consistent with this pattern, business services employment in the 11 host metropolitan areas rose about 20k in each of March and April, while it was little changed in the rest of the US. While city-level data are not yet available for May, some of the strength in May payroll growth might also have reflected hiring ahead of the World Cup.

Exhibit 2: Payroll Employment Rose More Than 80k Above Trend in Host Cities During the 1994 World Cup, With Job Gains Largely Concentrated in the Leisure & Hospitality, Trade, and Business Services Sectors  
![](images/49a68f07475d0be59ddf1330bd7ef9e9a75e3aac1a990dc2d4718fac93c4a8e1.jpg)

<details>
<summary>line chart</summary>

Deviation of Payrolls from Pre-Trend in Host Metropolitan Statistical Areas (MSAs)
| Months Since Start of the Event | World Cup 1994 (Thousand) | Los Angeles 1984 (Thousand) | Atlanta 1996 (Thousand) | Salt Lake City 2002 (Thousand) |
|---|---|---|---|---|
| -6 | 0 | 0 | 0 | 0 |
| -5 | 15 | 10 | -5 | 0 |
| -4 | 25 | 8 | -5 | 0 |
| -3 | 30 | 5 | -5 | 0 |
| -2 | 35 | 10 | -5 | 0 |
| -1 | 45 | 15 | 10 | 0 |
| 0 | 80 | 45 | 50 | 10 |
| 1 | 85 | 50 | 10 | 5 |
| 2 | 75 | 35 | -10 | 0 |
| 3 | 70 | 30 | -15 | 0 |
| 4 | 65 | 25 | -15 | 0 |
| 5 | 60 | 20 | -15 | 0 |
| 6 | 40 | 15 | -15 | 0 |
</details>

Note: Deviation from 12-month trend of nonfarm payrolls calculated up to 6 months before the start of the event. Data for the 1994 World Cup include all nine host MSAs.

![](images/eed1cf866d8abf323609f2ce29fd961b07c916a8d480f38260fe3b6be4d936ed.jpg)

<details>
<summary>stacked bar chart</summary>

Deviation of Payrolls from Pre-Trend in Host MSAs During the Months of the Event, by Selected Sectors
| Event | Trade and Transportation (Thousand) | Professional and Business Services (Thousand) | Leisure and Hospitality (Thousand) |
|---|---|---|---|
| World Cup 1994 | 27 | 18 | 23 |
| Atlanta 1996 | 6 | 25 | 20 |
| Salt Lake City 2002 | 0 | 2 | 6 |
</details>

Note: Deviation from 12-month trend of nonfarm payrolls calculated up to 6 months before the start of the event. Sector-level payrolls not available for the 1984 LA Olympic Games.  
Source: GS Global Investment Research, US Bureau of Labor Statistics

To estimate the impact of the 2026 World Cup on payrolls, we scale up the trajectory of job gains observed around the 1994 tournament by roughly $30\%$ to reflect the larger number of matches and attendees. Accounting for some hiring that has likely already occurred through May, we estimate a boost to monthly payroll growth of 40k in June and 10k in July, followed by a 15k drag in August as temporary positions wind down, with further gradual reversals throughout the rest of the year.

## Impact on GDP

Economic activity should receive a modest boost from the tournament. Spending on food and beverages by foreign tourists, domestic tourists, and locals will boost retail sales, which does not distinguish between spending by residents and foreigners. In the GDP statistics, all spending by domestic fans will boost consumer spending, and spending by foreign fans will boost exports of tourist services.

Drawing on estimates from the US State Department, FIFA, and Tourism Economics, and assuming that roughly two-thirds of World Cup-associated arrivals represent net additive inflows—with the remaining one-third displacing other tourism due to capacity constraints and elevated prices in host cities $^{1}$ —we estimate that foreign arrivals will run $\frac{1}{2}$ -1mn above trend in June and July (Exhibit 3).

Exhibit 3: The World Cup Should Provide a Tailwind to Foreign Tourism into the US in June and July  
![](images/3588c01b26736ae39c8d7d5ae41cd24f382e434b25ce42085bac9f9b0fd7ffd8.jpg)

<details>
<summary>line chart</summary>

| Month     | US State Department | FIFA  | Tourism Economics |
| --------- | ------------------- | ----- | ----------------- |
| Jul/2026  | 7.1                 | 6.5   | 6.3               |
</details>

Note: We assume that two thirds of World Cup-associated inbound visitors represent additive demand, with one third displacing alternative tourism due to capacity constraints and price effects in host cities.  
Source: GS Global Investment Research, US State Department, FIFA, Tourism Economics

The left side of Exhibit 4 shows that spending by foreign tourists rose about $5\%$ during the 1994 World Cup. To estimate spending by foreign and domestic tourists in coming months, we combine estimates of the expected number of foreign and domestic attendees with US Travel Association estimates of per-traveler spending across transport, lodging, food, and match-related expenditures. We estimate spending by locals by scaling up estimates of spending on Super Bowl entertainment for a typical household from the National Retail Federation by an estimate that the average American watched 2-3 matches during recent World Cups. We supplement these bottom-up estimates with a top-down approach where possible by looking at, for example, food and beverage retail sales during prior events.

The right side of Exhibit 4 shows our estimates based on this approach. We expect a boost to retail sales of 0.3pp in June and 0.1pp in July followed by a drag of 0.1pp in August, a boost to consumer spending of 0.05pp in Q2 and 0.02pp in Q3 followed by a drag of 0.03pp in Q4, and a boost to exports of 0.2pp in Q2 and 0.1pp in Q3 followed by a drag of 0.1pp in Q4.

Exhibit 4: We Estimate That Spending by Foreign and Domestic World Cup Fans Should Provide a Peak Boost to Retail Sales Growth of 0.3pp in June and to Consumer Spending of 0.05pp in Q2  
![](images/739eff5b0807a101220120563d40940f8182b3894694502ffc8eecadcde3bb3f.jpg)

<details>
<summary>line chart</summary>

Real Consumption Expenditure by Foreign Travelers to the US in 1994
| Month | Real Consumption Expenditure (Billions, 2017 USD) |
|---|---|
| January | 91.5 |
| February | 94.5 |
| March | 107.2 |
| April | 98.8 |
| May | 97.6 |
| June | 103.1 |
| July | 102.8 |
| August | 97.2 |
| September | 96.3 |
| October | 96.0 |
| November | 103.5 |
| December | 103.2 |
World Cup period indicated by arrow between May and June.
</details>

![](images/9780ffac55d6673735e5371fa2a3887af26809ff6840d99c451e42a6a5645654.jpg)

<details>
<summary>bar chart</summary>

Impact of Additional Foreign and Domestic Spending During the 2026 World Cup on Retail Sales, PCE and Exports
| Category | June (%) | July (%) | August (%) |
|---|---|---|---|
| Retail Sales | 0.28 | 0.14 | -0.12 |
| Impact on PCE | 0.06 | 0.02 | -0.01 |
| Impact on Exports | 0.23 | 0.13 | -0.11 |
</details>

Note: Our estimates assume a $40\%$ international fan share, that about two-thirds of World Cup-related travel spending represents net new activity, and allocates the impact across June (Q2) and July (Q3) based on the matches played in each month.  
Source: GS Global Investment Research, Census Bureau, Bureau of Economic Analysis

Even after imposing the 1.5 multiplier effect estimate from the Bureau of Economic Analysis's Travel and Tourism Satellite Accounts, these fan spending estimates are unlikely to capture the full impact on GDP, which will also include other effects such as government spending on security.

We therefore also consider a top-down estimate of the impact on GDP by estimating the effects of past Super Bowls using Gross State Product data. We then rescale the estimated effect of the Super Bowl to a World Cup effect by assuming that the ratio of the events' GDP effects will be the same as the ratio of their cumulative effects on employment. Exhibit 5 shows that this approach implies a boost to annualized GDP growth of 0.1pp in Q2 and 0.05pp in Q3, which should then give way to a modest drag in Q4. These figures are close to but a bit larger than the bottom-up estimates above, as one would expect.

Exhibit 5: Scaling Up the GDP Impact of Past Super Bowls Using the Estimated Effects on Employment Suggests That the 2026 World Cup Could Add 0.1pp to Annualized GDP Growth in 2026Q2  
![](images/61f311ec94305663af48e02468e46aa8f16faacbdf27063835fe25a7570ad11e.jpg)

<details>
<summary>line chart</summary>

| Quarters Since Start of the Event | Super Bowls Impact (left) | Estimated 2026 World Cup GDP Impact, Based on Expected Employment Path (right) |
| --------------------------------- | ------------------------- | ------------------------------------------------------------------ |
| -2                                | 0.00                      | 0.03                                                               |
| -1                                | 0.01                      | 0.04                                                               |
| 0                                 | 0.02                      | 0.12                                                               |
| 1                                 | 0.01                      | 0.08                                                               |
| 2                                 | -0.01                     | -0.04                                                              |
</details>

Note: Super Bowl GDP effects are estimated using state-level quarterly GDP data from 2005. The 2026 World Cup GDP impact is derived by scaling the Super Bowl effect by the ratio of employment gains estimated for the 2026 World Cup to those associated with Super Bowls.

Source: GS Global Investment Research, Bureau of Economic Analysis, US Bureau of Labor Statistics

One downside risk to our estimate is that many World Cup matches, unlike the Super Bowl, will take place during work hours and could reduce the productivity of distracted workers.

## Impact on Inflation

Prices for hotel rooms on match nights have already spiked, as Exhibit 6 shows. We assume that prices will increase by half as much on each of the two nights before and after the match night, and by a quarter as much on the two nights before and after those nights. Accounting 

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
