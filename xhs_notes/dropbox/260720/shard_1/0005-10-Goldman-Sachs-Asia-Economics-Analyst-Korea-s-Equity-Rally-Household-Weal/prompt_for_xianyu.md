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
ASIA ECONOMICS ANALYST

# Korea's Equity Rally: Household Wealth Gains amid Consumption Constraints

Despite the recent correction in July, the KOSPI remains up around 60% year to date and more than 110% from a year ago, boosting household equity wealth by an estimated 17% of GDP. While Korean households continue to hold some of the most property-concentrated balance sheets among major economies, the sharp equity rally has narrowed the gap in equity assets relative to GDP with Japan and Europe.

\- Korean household equity ownership is heavily skewed toward the top income and asset quintiles, which account for 64% and 72% of total equity assets respectively, while investors aged 50 and above hold 73% of total household equity wealth. Older investors also maintain significantly higher allocations to domestic equities, implying that they have benefited the most from the recent rally.

Several structural factors are likely to constrain the pass-through from equity wealth gains to consumption. Korean households continue to face elevated leverage and debt-service burdens, particularly among higher-income and higher-asset groups. At the same time, older households continue to exhibit persistently high saving rates relative to their peers abroad, suggesting a limited propensity to convert capital gains into current spending. Finally, the volatility of equity returns and the recent market correction may lead households to perceive stock-market gains as transitory.

■ Taken together, the consumption boost from the historic equity rally could overall be modest. Based on a panel regression, we estimate that a KRW100 increase in equity wealth is associated with roughly KRW1.6 of additional consumption, broadly consistent with results from a recent BOK study. Our finding implies that the increase in household equity wealth this year could lift consumption by roughly 0.3% of GDP. However, part of this modest boost could be offset by higher debt-servicing costs given the start of a new BOK rate hike cycle.

Irene Choi
+82(2)3788-1722 | irene.choi@gs.com
GS (Asia) L.L.C., Seoul Branch

Goohoon Kwon, CFA
+852-2978-0048 |
goohoon.kwon@gs.com
GS (Asia) L.L.C.

Andrew Tilton
+852-2978-1802 |
andrew.tilton@gs.com
GS (Asia) L.L.C.

## Backdrop: Korea's historic equity rally

The unprecedented rally in Korean equities has important implications for household balance sheets and private consumption. Despite the recent correction in July of some 20%, the KOSPI remains up around 60% year to date and more than 110% compared to the same time last year, marking one of the strongest performances in the region and among major global equity markets. These sharp gains have generated substantial increases in household financial wealth and raised questions about the extent to which these gains could support broader economic activity. In this report, we examine the implications of the rally for household balance sheets and assess the extent to which equity gains could boost consumption given structural constraints.

## Measuring the Boost to Korean Household Wealth in 2026

Prior to the equity rally that began late last year, Korean households had some of the most property-heavy balance sheets among major economies. Based on the latest available household wealth data from 2024, non-financial assets accounted for 76% of total household net wealth in Korea (Exhibit 1), higher even than those in Australia (72%) and the Euro Area (65%). Notably, Taiwan's ratio stood at less than half that level at 33%. Conversely, households' net financial assets remain relatively small at just 1.2 times GDP—the lowest among major economies, even compared to those of the UK and the Euro Area at 1.5–1.6 times, and only about one-fourth the size observed in Taiwan.

Exhibit 1: Korean household wealth was still heavily concentrated in non-financial assets in 2024  
![](images/7eca0c4e9c634dd0227dfdc90ef5816cc4a2356c658debc91a3f7255d14d2a22.jpg)  
Source: Haver Analytics, BOK, DGBAS, ECB

The historic equity rally has led to a substantial increase in Korean household financial wealth. Even after the July correction of roughly 20%, we estimate that household equity assets have increased by an amount equivalent to roughly 15% of GDP since end-2024 (Exhibit 2). Around 80% of the gains came from direct holdings of domestic equities, while investment funds accounted for about 15%, and foreign equities for the remainder. The increase has been large enough to materially alter Korean households' balance-sheet composition: by our estimates, household equity assets relative to GDP could now be approaching the levels seen in Japan and the Euro Area (Exhibit 3).

Exhibit 2: Korean households' equity assets could have risen by $15\%$ of GDP from the end of last year

Percent of GDP

![](images/a49bb8f3422db5a6c343d0d4e75249eff402b5a5f06e055fc70f3deb114fb8bb.jpg)  
Note: For last columns, based on mid-July levels  
Source: Haver Analytics, GS Global Investment Research

Exhibit 3: After a notable increase in 2026, Korean households' equity assets relative to GDP could approach levels seen in Europe and Japan  
![](images/80acf2ac12ebf30b3538c1216dfb11d93b1cb8f7ed65d72938e4d148ea5cc83f.jpg)  
Source: Haver Analytics, GS Global Investment Research

Korean households have relatively limited indirect exposure to equity gains through their occupational and personal pension savings. According to the OECD's Global Pension Statistics, cash and deposits accounted for around $40\%$ of Korean pension providers' (excluding public pension reserve funds such as the National Pension Service) assets at end-2024—the highest share among major economies in our comparison—while only around $20\%$ were held through collective investment schemes that include equity funds (Exhibit 4). $^{1}$ Given the relatively conservative investment allocation of personal pensions, we estimate that the equity rally could have raised household retirement balances by 2% of GDP.

Exhibit 4: Korean pension assets are concentrated in cash and deposits

![](images/e9ff4e2e8545a606382f400bda6d2625eda04357155454040191186e89530714.jpg)  
Source: OECD

## Consumption Constraints from Korean Household Balance Sheets and Equity Market Volatility

The impact of the recent equity rally on domestic consumption is likely to depend not only on the size of the gains, but also on the distribution of equity ownership across households. Equity assets in Korea are concentrated among high-income and high-asset households, with the top income and asset quintiles accounting for 64% and 72% of total household equity holdings, respectively (Exhibit 5). Equity ownership is also skewed toward older households: investors aged 50 and above hold 73% of total equity assets and are likely to have benefited the most from the recent market rally, given their relatively high exposure to domestic equities (Exhibit 6). Investors in their fifties and older allocate three-fourths of their equity portfolios to domestic stocks, compared to around 50% for younger investors, allowing them to capture a larger share of the gains generated by the strong performance of the domestic market.

Exhibit 5: Korean equity assets are heavily concentrated in high-income and high-asset households

![](images/8073bc33b048656428cccf0b4704b091b88f3b0460df65b1ff89f19b86bf0153.jpg)  
Source: Ministry of Data and Statistics

Exhibit 6: The domestic equity rally likely benefited older investors (aged 50 and above) the most, given their higher exposure to domestic equities  
![](images/1e9da64280cf0ede5e3bbae529a5407179422776c2455b8b3d5534d0a7b4468b.jpg)  
Source: Korea Securities Depository, Korea Capital Market Institute

While the concentration of equity assets among higher-income households and older investors is not unique to Korea, the country's relatively high level of household leverage and debt-service burdens may constrain the pass-through from equity gains to consumption. In Korea, financial liabilities are also concentrated among high-income and high-asset households, with the top quintile accounting for roughly $45\%$ of total household debt. Debt-service costs (including principal repayments) are elevated across the household sector, averaging slightly above $20\%$ of disposable income, while the burden is highest for households in the top asset quintile, at around $27\%$ (Exhibit 7). Compared to other major economies, Korean households carry relatively large financial liabilities relative to their asset holdings, particularly at the upper end of the income and wealth distributions (Exhibit 8), reflecting the prominent role of property assets in household balance sheets. As a result, a greater share of equity gains may be directed toward mortgage servicing, debt reduction or balance-sheet management rather than consumption.

Exhibit 7: The debt-service burden is highest for high-asset households, amounting to 27% of disposable income  
![](images/5beb1445cb3a720e4dff2136b15a6614a981d5683bd02dde60ba4111519ff10c.jpg)  
Source: MODS

![](images/286132b02a6a8677be041131181873b6f7e36a62cf72cea58c950e65a172bbb6.jpg)

Exhibit 8: Korean households have high financial liabilities relative to assets, particularly among higher income households relative to other countries  
![](images/55ed133240a9463e5c4e394edc9003b7da902f15c19e7171f48f75bade186fd4.jpg)  
Source: MODS, ABS, BLS, DGBAS, Japan Statistics Bureau

Persistently high savings rates among older Korean households, which have benefited the most from the recent equity rally, may further weaken the pass-through from equity gains to consumption. Korea's household savings rate remains elevated, notably among older households. The savings rate rises to $37\%$ for households headed by someone in their sixties and those aged 70 and above—more than 7 percentage points higher than in other major economies in our comparison (Exhibit 9). Savings rates among younger Korean households are broadly comparable to those in the U.S. and Taiwan, suggesting that Korea's distinct feature may be the limited drawdown of income and wealth after retirement. This could reflect precautionary savings as well as lower pension holdings among Korean households (Exhibit 3). Given that older households also hold a disproportionate share of equity assets, their continued preference for saving suggests that even substantial capital gains may be retained in household balance sheets rather than translated quickly into current consumption.

Exhibit 9: Korea's household savings rate remains elevated notably among older households  
![](images/09f52df2c53754bd3e3bc1d0b72b799b6b7b3081c6580fe9757008630b9f0111.jpg)  
For Taiwan and the US, data is for 2024 and age groups are for below 39 (below 35 for the US), 40-45,45-55,55-65 and over 65; for Korea and Japan, data is for 2025.  
Source: MODS, ABS, BLS, DGBAS, Japan Statistics Bureau

The wealth effect from equities may be further muted because equity gains are often perceived as less stable and permanent. Since 2018, property in Seoul has consistently delivered stronger risk-adjusted returns than Korean equities, with the five-year rolling Sharpe ratio for Seoul housing peaking above 6 in 2022. Although the risk-adjusted performance of housing has deteriorated meaningfully since, with the Sharpe ratio falling to around 0.5 in recent months, it has remained above that of Korean equities for most of the period since 2018 (Exhibit 10). The risk-adjusted return on the KOSPI has historically been considerably weaker, remaining below 0.5, although it has recently improved to around 0.7–0.8, helped by the sharp rally since last year.

Exhibit 10: Residential property in Seoul has consistently delivered stronger risk-adjusted returns than Korean equities  
![](images/9fbab15a4c263ae59a04c9eb7a513fafca0156d7ec894119ef49b94ec595d0e9.jpg)  
\*Based on weekly prices

## Source: Haver Analytics, GS Global Investment Research

Recent market developments could have reinforced the perception of equity wealth as volatile and possibly transitory. Assets under management in domestic leveraged ETFs have risen sharply since the beginning of the year to above KRW30trn—nearly three times the level at end-2025—driven in large part by the launch of single-stock leveraged ETFs in May 2026 (Exhibit 11). However, the subsequent correction in equity markets and the large price swings experienced, including those for leveraged products, may have highlighted the risks associated with equity investments. Increases in leveraged investments, as evidenced by sharp increases in margin loans at securities firms, also point to potentially significant losses for households that entered the market later in the rally. While these leveraged exposures overall remain modest relative to total market capitalization and investor deposits, losses incurred on leveraged positions could at least partially offset earlier capital gains, further limiting the boost to household consumption.

Exhibit 11: Leveraged ETFs and the margin loan balance have picked up sharply in 2026  
![](images/205f0228d810c8e787f9b2f15c46d8f0994b8e57a0a1093c7b8daab80558d997.jpg)  
Source: Quantiwise

![](images/28ae04e56c94e1c186234216cc98c02032a6701b62fd6cdee46a4992f6d8ab46.jpg)

## Modest Consumption Boost Offset by BOK Tightening

Overall, we expect the boost from this year's equity rally to remain moderate. Based on a panel regression using quarterly household survey data on consumption and equity holdings by income quintile from 2013 to 2026 Q1, we estimate that a KRW100 increase in equity wealth is associated with roughly KRW1.63 of additional annual consumption, after controlling for disposable incomes and household characteristics such as household size and the age of household head. This estimate is broadly consistent with results from a recent BOK study, which suggests that a KRW100 increase in equity wealth leads to roughly KRW1.3 of additional consumption. Our estimate implies that the increase in household equity wealth—equivalent to roughly $17\%$ of GDP since the end of last year—could lift private consumption by around $0.3\%$ of GDP.

However, the positive wealth effect may be offset by higher debt-servicing costs as the monetary easing cycle reverses. While Korean households have undergone significant deleveraging since 2021, household loans still amount to 83% of GDP and more than half of outstanding loans remain linked to floating interest rates (Exhibit 12). By our estimates, a cumulative 75bp increase in the BOK policy rate as we currently expect would reduce household disposable income by around 0.3% of GDP on a gross basis, or by roughly 0.06% of GDP after netting out interest income on household deposits.

Exhibit 12: Household loans still amount to 83% of GDP and more than half of outstanding loans remain linked to floating interest rates  
![](images/122eb559f795bc7adbb5aacd0f8d2f643cc7af15245134922918a9468c5c7773.jpg)  
\*Note: BOK reclassified loans with interest rates fixed for five years or longer from floating-rate to fixe-rate loans

## Source: Haver Analytics

Taken together, Korea's equity rally has delivered a significant boost to household wealth, but the implications for private consumption are likely to be modest given several structural constraints, including the concentration of equity gains, elevated household leverage, high savings rates, and the volatile nature of stock-market returns. At the same time, the unprecedented scale of the current rally raises the possibility that the historical relationship between wealth and consumption may underestimate the upside potential for consumption. Whether a larger wealth effect ultimately materializes will depend on the durability and breadth of the equity rally, as well as the extent to which corporate earnings eventually translate i

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
