你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

Prices for hotel rooms on match nights have already spiked, as Exhibit 6 shows. We assume that prices will increase by half as much on each of the two nights before and after the match night, and by a quarter as much on the two nights before and after those nights. Accounting for the fact that the official price statistics measure hotel prices at the time of reservation and for the weight of the host MSAs in the CPI, we estimate that the World Cup will boost national average hotel prices by about $1\%$ in June, following increases in April and May. We expect hotel prices to begin to normalize slightly by July, a bit ahead of other prices, because most hotel reservations for the World Cup will already have been made by June and because the smaller number of matches is likely to outweigh the effect of a larger per-match impact, whereas the opposite is likely to be true for activity and prices at bars and restaurants.

Exhibit 6: Sharply Higher Hotel Prices in Host Cities Around Match Days Imply a World Cup Boost to Average US Hotel Prices of About 1% in June  
![](images/218b3537fe5092b5c91b25096da413a51c45e92ea36ec432dcd3c2b044668001.jpg)

<details>
<summary>bar chart</summary>

Hotel Room Price Difference from Regular Prices on Match Nights in Host Cities in June/July 2026 and Impact on US Hotel CPI
| City | Difference from Regular Prices (left) (%) | Impact on US Hotel CPI MoM Growth (right) (%) |
|---|---|---|
| Kansas City | 160 | |
| Miami | 75 | |
| Philadelphia | 73 | |
| Houston | 69 | |
| Dallas | 68 | |
| SF/Bay Area | 42 | |
| New York | 39 | |
| Boston | 37 | |
| Atlanta | 35 | |
| Seattle | 31 | |
| Los Angeles | 15 | |
| June US Average | - | 1.0 |
| July | - | -0.5 |
| August | - | -1.0 |
</details>

Note: Hotel room price premiums for each host city are based on estimates provided by the New York Times, derived from data on major hotel chains. We assign the price premiums to June and July based on the number of matches played and obtain average effects using the CPI weights for each MSA.  
Source: GS Global Investment Research, US Bureau of Labor Statistics, New York Times

MSA-level CPI data show that prices for food away from home and transportation also tend to jump in host cities around major sporting events, as shown in Exhibit 7. These data also show that while some payback appears to occur in the months following the event, it is less than complete. This seems plausible—restaurant price increases sparked by the event might not fully reverse immediately after and might instead be undone only gradually and undetectably by smaller price increases well after the event.

Exhibit 7: Past Sporting Events Drove Temporary Prices Hikes for Restaurants and Transportation Services  
![](images/46bdfd9ec9759ac287867f6c7b43d60fbe7b5a03813bdccb87ffa96831f40b09.jpg)

<details>
<summary>line chart</summary>

Difference Between Food Away from Home CPI MoM Growth in Host MSAs vs. Rest of the US
| Months Since Start of the Event | Olympic Games (Percentage points) | Super Bowls (Percentage points) | 1994 World C

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
