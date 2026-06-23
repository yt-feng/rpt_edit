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
# Power Tracker: US Markets Tightening Into Summer, Only Marginally Eased by Coal Power Policy

■ Regional divergence in focus as summer starts. June 1 marks the rollover of 1-month forward contracts across regional power markets from trading June contracts to trading July contracts. This transition reveals market expectations on peak summer power market tightness, along with generation fuel costs. We see contrasting trends between PJM (Mid-Atlantic) and ERCOT (Texas) power markets:

□ PJM (Mid-Atlantic): The power price increased significantly more during this year's May-to-June rollover compared to the historical average in the past decade, both in terms of the absolute price level (+28 USD/MWh in 2026 vs +15 USD/MWh in 2016-2025) and the percentage change (+44% vs +30%, Exhibit 1), despite prices of marginal generation fuels, natural gas and coal, increasing much less. This larger price increase into the summer, combined with its upward trend since 2020 (Exhibit 1), is consistent with our view of a tightening power market in the region: PJM hosts 39% of US data center power demand capacity, where power demand growth has continued to outpace power supply growth.

☐ ERCOT (Texas): While the ERCOT market also experienced its typical seasonal price increase rolling over into June, the absolute price rise of \$24/MWh was smaller than the previous decade's average of \$30/MWh and the percentage increase was just above the historical average (61% versus 56%, Exhibit 1). In addition, the price levels in both May and June have been lower than in 2024/2025, driven by the recent softening in the Texas market $^{1}$ .

☐ Regional divergence: This rollover contrast between these two regional markets is consistent with our regional divergence view that ERCOT has entered a softening path since late-2025 with substantial expansion in power supply, while we expect PJM to remain critically tight in the next few years.

We expect federal support for coal power to offer marginal relief. To alleviate power market tightness, the US administration refreshed its support for coal power following President Trump's advocacy for "Beautiful Clean Coal Power" earlier this year. Earlier this month, the president announced a new plan to allocate nearly \$700 million to support coal power (and coal exports), mainly by

Hongcen Wei  
+1(212)934-4691 |  
hongcen.wei@gs.com  
GS & Co. LLC

Laura Cyr
+1(212)902-3435 | laura.x.cyr@gs.com
GS & Co. LLC

Daan Struyven +1(212)357-4172 | daan.struyven@gs.com GS & Co. LLC

Samantha Dart +1(212)357-9428 | samantha.dart@gs.com GS & Co. LLC

2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 financing delaying/canceling scheduled coal power retirements. While we expect this plan to effectively add incremental power supply relative to previous schedules, along with emergency orders of US Department of Energy (DOE) that direct coal power plants to remain online, we believe the overall impact on resolving market tightness could be marginal in 2026-2028 and after 2028 for the following reasons:

☐ Increasing difficulties for more retirement delays: A significant amount of scheduled coal retirements have already been delayed in the past year after the first DOE emergency order in May 2025, which pushed 2025/2026 retirements out to 2026-2029 (Exhibit 2). Remaining scheduled retirements could be subject to physical/financial constraints: already delayed retirements may face a higher bar to be delayed again and most coal plants are old, both lacking extensive maintenance given the original retirement schedules which could drive the cumulative maintenance costs beyond the scope of the \$700-million fund.

☐ Longer-term policy uncertainty: Coal power plants and coal producers continue to face regulatory and policy uncertainty beyond 2028, which disincentivizes significant capex to upgrade or even expand capacity. One example is the coal power retirement delays in the TVA (Tennessee) power market, where a total of 4.1 GW coal power generation capacity, all originally scheduled for retirement by the end of 2028, has been delayed, while retirement schedules beyond that window remain unchanged.

## Featured Charts

Exhibit 1: The rollover of power forward contracts show a higher-than-average June price level and May-to-June price increase in PJM vs lower-than-average in ERCOT

![](images/c2e167417cd3312dc65a17de29cfb9c8b26fdb9cf48b4b3d90904e8e11dab329.jpg)  
2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

![](images/c1ea60ee14881c617ce23175fcd597ab1d58735ab88de89c5376a8a042f1683b.jpg)  
Source: Bloomberg, GS Global Investment Research  
Prices of PJM in 2022 and of ERCOT in 2018 and 2022 are above 100 \$/MWh and not shown in the charts, but are counted in historical average calculations.

Exhibit 2: Coal retirement delays since 2025 have effectively increased power supply in the next few years, but are more constrained going forward

![](images/e05e152e7870313ce2cec552e3632e9d97e4556772e59de0f0d93d590c8ab35e.jpg)  
Based on EIA generator schedules released in late May 2026, which do not include some recent announcements/DOE orders that adjust the timeline of coal power plants' retirements  
Source: EIA, GS Global Investment Research

## Prices

Exhibit 3: ERCOT (Texas) early summer power price remains weak yoy, remaining below 60 USD/MWh
ERCOT North 345kV Hub peak load prices

![](images/ab299c38297e3dadf17930a48b991fecd488d335cce229edb6eb766ceafbcba2.jpg)  
Source: Bloomberg

Exhibit 4: Power prices in PJM (Mid-Atlantic) rally into the 90 USD/MWh range with the forward contract rollover  
PJM western hub peak power swap prices  
![](images/9806dd7310c67e57078c6c109561170459571f60514eb8b5d020821a60f92277.jpg)  
Source: Bloomberg

## Market Tightness

Exhibit 5: The PJM (Mid-Atlantic) power market was tightened by heatwaves into June  
![](images/3070667604d074edfc67ea56ed9593e7ff22363ec56ee0d5583b7962b4969b81.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below 15%. Not showing in the chart if above 100% (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

Exhibit 6: The MISO (Mid-Continental) power market also turned tighter into June before softening this week  
![](images/b49771764ccb7c4402b9d0ef15a998a98c03519a88e8c64339a2d0a9cab7d09a.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below $15\%$ . Not showing in the chart if above $100\%$ (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

Exhibit 7: The ERCOT (Texas) power market maintained a soft balance with mild weather  
![](images/9f0dd1cab75a3e6f3389f83559deb65227839c441e3bbf369d91c8470e98ff3f.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below 15%. Not showing in the chart if above 100% (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

## Demand

## Aggregate Power Demand

Exhibit 8: Total US yoy power demand growth strengthens to $2.3\%$ in March, but still below the annual yoy growth rate of $2.4\%$ in 2025  
![](images/af37a60079237c5818e66cc8de7c3793f082a67a36d0c5f6aa0a76764a2e0d1b.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 9: After weather adjustment, US total power demand growth in Jan-Mar2026 was $1.2\%$ , also below last year's growth  
![](images/84b760673f903218b32c04d0eb5aceea954ac5835815dbb5ae6470c385bd98dc.jpg)  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 10: The commercial sector continues to be the strongest sector in power demand growth in Jan-Mar2026 with a $2.7\%$ yoy growth rate  
![](images/d5492a00368d668451b86fb6729bb229405627d50af138779ae83c48741badfc.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research  
Exhibit 11: After a weak start of the year in Jan2026, US residential power demand remained flattish yoy in Feb-Mar

![](images/3da694ddda0497cf13cf2b39055a4417efa629b76941b8d9d2ca6445c027e25d.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 12: Industrial power demand strengthened into March after Jan-Feb2026 yoy weakness  
![](images/346a3b205ee2994b145659aa9058c0fb3c7c61e8b52eaad5bd79102bd73d8395.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 13: US power demand growth remained below US GDP growth through Apr2026 Weather-adjusted US total power demand (including small-scale solar power use) and US real GDP yoy, monthly  
![](images/57d0776233a3a3e176a85409043ae37e8baf4f50e9bf1192c70f1e2f282a2e9e.jpg)  
To avoid underestimating power demand, we include all small-scale solar power generation in US total power demand  
Source: EIA, Bloomberg, Haver, GS Global Investment Research

## Data Center Power Demand

Exhibit 14: Estimated data center power demand in Virginia continued to edge higher  
![](images/07e92786bf926dff23e039832a2225ec017ac06d0bdd4a5bb576f655412e9c8c.jpg)  
Not weather adjusted  
Source: Haver, GS Global Investment Research

Exhibit 15: US data center capacity continued to grow, which we expect to accelerate in June and also in 2H2026  
![](images/6b1c91082ce9eedc28f80b5146ab9d22562fcceadbc0d3cad30df57d72ed7874.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 16: Texas and Virginia led data center expansions in the past year, along with Arizona, Indiana, Ohio and Georgia

YoY Data Center Capacity Additions Across US States  
![](images/dd789f4dcf91d82b5f2253faa3d5c0f19d9f805386c7f530310075e8b39dae04.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 17: Ohio, Texas, and Virginia are leading data center development in 2026Q2  
Data Center Capacity Additions Across US States in 2026Q2  
![](images/5cb0228835929fa7d17c31b7500c9194d1757a2053ad67c97d4dd81b239bc4ec.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 18: We expect significant data center growth acceleration in both the US national and key regional power markets in 2026/27  
![](images/963da2565e7851c38a30516f46e4081924b5852d280aa9744e756f61969df124.jpg)  
Source: Aterio, GS Global Investment Research  
Exhibit 19: Construction employment related to US data center expansion continued its growing trend

![](images/90f8bc473a1d9b76d9af7c36740f4cf4ba91e4f50cbc76b128362bd9b28d768b.jpg)  
Source: Haver, GS Global Investment Research

## Supply

## Generation and Stack

Exhibit 20: US total power generation stayed in line in most of May before gaining strength into early-summer  
![](images/ef46e5db392563636b239b5346aa96b5485455c3e328f1d5bbddc4fa3b0c2306.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 21: After adjusting for weather, US total power generation holds in line with early-summer year-ago levels  
![](images/57fbe89e1b17f1415cda0a3d4ec34dadc383a25a86554e944b09c2a7f4e4e35a.jpg)  
Source: EIA, Bloomberg, GS Global Investment Research

Source: EIA, GS Global Investment Research

Exhibit 22: The thermal (natural gas and coal) share in US power supply continues to increase from mid-April given yoy weaker hydro and nuclear  
![](images/d1414fb2f5bffb43f72aa071e10145ab4b75e6ab3118c1955228ecd99411fa99.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research  
Exhibit 23: Within thermal power generation, the natural gas share remained higher yoy given price competitiveness

![](images/f450376b1b30cb0700c7b8a3f88ab2df1d5163d3359d3d3e168e7a2478fdf8d5.jpg)  
Not weather adjusted

Exhibit 24: US power transmission and distribution losses continued to increase into 2026, though marginally lower in Apr/May  
![](images/332014f4fc4e47bf67319b81682a1ddc4b09aeee3fbf6430849e73a40317a350.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

## Generation by Fuels

Exhibit 25: YoY growth in natural gas-fired generation has moved sequentially lower June-to-date vs March and April but remains positive  
![](images/19c49822b6fa3f16834a01af61ab4ef77a997b55b8c562086022f7e252e54d3d.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 26: Higher gas competitiveness keeps coal power generation lower yoy most of the time from mid-Feb to Jun  
![](images/8142b1fa897b29b78bf166a31c33d4ef34af7e7754880476a36cd683599b9451.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 27: Nuclear power generation turns higher yoy into May and June following April maintenance  
![](images/d5829aa3dcad6ba18543826ef790a06a60c900d434a1e0269309371a7f781628.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 28: Wind generation moves higher yoy in May and June  
![](images/9352110195c734270a012ca5d8ff8ae795a11e58eb0c647fe7c607e9793d4813.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 29: Solar generation has continued to seasonally ramp up, driven by yoy capacity additions of over 30 GW  
![](images/431f80d368ed93a940a7ac62a37621f36e4eadb160d111d9dafe15d190754549.jpg)  
Source: EIA, GS Global Investment Research

Exhibit 30: Hydro power generation remains weak yoy due to droughts in more than half of the country  
![](images/77b3b2c21f1fc4085e3040fa6bc143fe4a2e0649e3d91e818fe32f9362e80483.jpg)  
Source: EIA, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Hongcen Wei, Laura Cyr, Daan Struyven and Samantha Dart, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Hongcen Wei GS & Co. LLC, Laura Cyr GS & Co. LLC, Daan Struyven GS & Co. LLC, Samantha Dart GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and there

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
