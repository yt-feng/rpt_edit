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
# Japan Economic Flash: Raising Our FY2027 Inflation Forecasts Due to Weaker Yen, Higher Memory Chip Prices, and Rebound in Food Prices

We raise our inflation forecasts for FY2027. Our forecasts for new core CPI (excludes fresh food and energy) in FY2026 and FY2027 are 2.1% (unchanged from previous forecast) and 2.3% (+0.3pp), respectively.

Tomohiro Ota
+81(3)4587-9984 |
tomohiro.ota@gs.com
GS Japan Co., Ltd.

The upward revision to our FY2027 forecasts reflect our forex research team's revised forecast (12-month forecast: from ¥155/US\$ to ¥165/US\$), a significant rise in memory chip prices, and higher food prices partly due to weather factors. While these factors will accelerate inflation not only in FY2027 but also in FY2026, our FY2026 inflation forecast remains unchanged, since the rise in private services prices is tracking below our forecast. Naphtha-flation (the rise in naphtha-related product prices) took a breather in the June corporate goods price index (CGPI, goods-PPI equivalent) print. This is consistent with our forecast that the margin of price increases will narrow as pass-through progresses downstream. We expect some price increases from June, mainly in non-durable goods, but the margin of increase in retail prices, which are the farthest downstream in the supply chain, is likely to be small.

Meanwhile, our core CPI (excludes fresh food) forecasts for FY2026 and FY2027 are also revised to be $2.1\%$ (-0.2pp from our previous forecast) and $2.3\%$ (+0.2pp), respectively. The downward revision for FY2026 reflects crude oil prices trending at levels below our previous forecast, as well as the government's price control measures exceeding our initial assumptions in scale. Our commodities research team has also revised down its crude oil price forecast for FY2027, and reflecting this, the upward revision for FY2027 is smaller than that of the new core CPI.

This forecast revision does not incorporate the upcoming CPI base-year revision in August as well as the potential consumption tax cut which the government may implement from April 2027. While the impact of the CPI base-year revision to our forecast is unclear, inflation rate could decline significantly with the start of the tax cut, from April 2027.

## Raising Our FY2027 Inflation Forecasts Due to Weaker Yen, Higher Memory Chip Prices, and Rebound in Food Prices

## Upward Revisions to New Core CPI Outlook, Mainly in FY2027

We revise our inflation forecasts mainly to incorporate changes in our forex forecasts and higher memory chip prices (Exhibit 1). Our new core CPI (excludes fresh food and energy) forecasts for FY2026 and FY2027 are 2.1% (unchanged vs. previous forecast) and 2.3% (+0.3pp).

The upward revisions to the new core CPI are concentrated in FY2027, driven mainly by our forex research team's revised USD/JPY forecast toward a weaker yen (12-month forecast: from ¥155/US\$ to ¥165/US\$), the expected impact of higher memory chip prices on the CPI from fall 2026 through H1 2027, and higher food prices in 2026-2027. Of these, higher memory chip and food prices are also upside factors for the FY2026 inflation rate. However, as discussed later, they are offset by the increase in private services prices tracking below our expectations, leaving the new core CPI outlook for FY2026 unchanged. In this note, we examine each price fluctuation factor.

We also note that in the upcoming once-every-five-year base year revision for the CPI on August 7, the CPI inflation rate for January-June 2026 is subject to retroactive revision and could also impact the future inflation rate (we estimate a small upward revision to January-June 2026 inflation rate, while the new base year could exert downward pressure on the future CPI, although uncertainty is high). We plan to review our inflation forecast once the new CPI series is officially released.

In addition, we currently do not incorporate a potential consumption tax cut in our base-case forecasts. Therefore, our core CPI inflation forecasts from April 2027, the expected starting period for a possible tax cut, could decline by 1.3pp with a tax cut.

Exhibit 1: Inflation Outlook Raised, Mainly for FY2027  
![](images/5bf0af08488e4c3927ab146d0ed862a68b1a5bef56e069fc880b2bed4e064687.jpg)  
Source: Ministry of Internal Affairs and Communications, BoJ, JCER, GS Global Investment Research

## Forex: Upside Risk to Prices From Further Yen Depreciation of Around ¥5 Is Small, but Impact on Monetary Policy Cannot Be Ignored

One reason for the upside in the FY2027 inflation rate shown in Exhibit 1 is that our forex research team revised its 12-month USD/JPY forecast from ¥155/US\$ to ¥165/US\$. In our model, a ¥10 depreciation of the yen (a weaker yen of just over 6% in terms of rate of change) pushes up the new core CPI by 0.25pp 12 months later.

The rate of change in the forex rate is what affects the inflation rate (Exhibit 2). Therefore, given that the yen has already depreciated to a level exceeding ¥160, even if the yen were to weaken by several yen beyond our team's forecast of ¥165/US\$, we would expect upside to the inflation rate to be limited. However, the Bank of Japan (BOJ) is becoming increasingly vigilant against the risk of underlying inflation rising above 2%, and some of BOJ's indicators of underlying inflation are approaching 2%. Consequently, even a relatively modest upside surprise to prices could heighten BOJ concerns over the risk of underlying inflation exceeding 2%.

Exhibit 2: Compared to When the USD/JPY Rate Was Around ¥100/US\$, the Impact of a ¥10 Fluctuation on the Inflation Rate Is Smaller
Impact of USD/JPY Fluctuations on New Core CPI  
![](images/5ea58602301533d003a998ee2996d5bbbfde94553fd5e4f6eba5974bca6e113e.jpg)  
Source: Ministry of Internal Affairs and Communications, GS Global Investment Research

## AI-Related: The CPI-Boosting Effect of Higher Memory Chip Prices

Along with the rapid surge in demand related to AI servers, memory chip prices have skyrocketed since H2 2025, with spot prices reportedly up seven-fold yoy (Nikkei, June 29). Reflecting this movement, B2B prices for PCs have already soared since April. In light of this, we expect PC prices in the CPI, which tend to lag B2B prices by several months, to rise going forward (Exhibit 3). However, since retail prices are also influenced by logistics costs and labor costs at the retail level, it is unlikely that PC retail prices will be hiked as much as the increase in B2B prices. Furthermore, since the weighting of PCs and tablets in the CPI is only just over 0.3%, the resulting boost to the CPI could be limited to a cumulative c.0.05pp.

Mobile phones have a larger impact on the CPI since they account for about 1% of the

CPI weight (Exhibit 4). $^{1}$ While retail prices have been raised for some models on soaring component prices, the iPhone, which has about a 50% share of the mobile phone market in Japan, will reportedly see the launch of new products in two stages this fall and next spring, and price hikes are anticipated. If prices are raised by nearly 20% as reported, the iPhone price hike alone would push up next year's CPI by about 0.1pp, an impact that cannot be ignored.

Exhibit 3: PC Prices in the PPI, Which Leads the CPI by Several Months, Surged in April
Domestic Corporate Goods Prices and CPI PC Prices  
![](images/79fb307a1c956b762402b85cea171b963ea99a810db1cc44e7da194c1a3fb9e9.jpg)  
Source: BoJ, Ministry of Internal Affairs and Communications

Exhibit 4: Mobile Phone Price Hikes Reflecting Surging Memory Prices Have Just Begun
Mobile Phone Prices in CPI  
![](images/1b12b71cc998f911fd06a4e63dd3cd1bc61b9f0b268bd536ff1128a24e23bf94.jpg)  
Source: Ministry of Internal Affairs and Communications

## Food Inflation: A Third Wave Arrives, but Lower Rice Prices Serve as a Dampening Factor

Food prices, which rose significantly in 2024-25 driven primarily by rice prices, have seen relatively limited price increases since the end of 2025, becoming the main driver of the inflation rate slowdown over the past half-year. Rice prices, which drove food inflation in 2024-25, are likely to continue declining due to increased inventories (Exhibit 5).

However, according to a Teikoku Databank survey, the number of food items subject to price hikes is expected to increase again from July, making it likely that a third wave of food inflation will push up the CPI going forward (Exhibit 5). On this point, micro-level information from the BOJ's July Branch Managers' Meeting also indicated that many companies are considering price hikes from the summer onward. This is partly due to much higher packaging film prices driven by higher naphtha prices, but the contribution from prices for imported food ingredients, which continue to rise mainly for meat prices, is also seen as significant.

In addition, wheat planting in the US and Australia is declining due to weather conditions and other factors, and the import price of meat, which accounts for 20% of food import value, continues to rise. Thus, the rise in related food prices is likely to continue next year as well.

Number of Food Items Subject to Price Hikes and Food CPI  
Exhibit 5: Rice Prices Likely to Continue Declining
Rice Price Outlook DI and CPI Rice Prices  
![](images/50fa69ab1418348d8e213b772f691222da8f9ccc460722b57cd072a65e836f25.jpg)  
The DI is an index of the difference between the percentage of dealers answering that “rice prices over the next three months will rise compared to current prices” and the percentage answering that they will “decline.”

## Exhibit 6: Food Prices Expected to Rise Again From the Summer

![](images/0c4da90e609452af9842f2b36c5424bb3f1c9ac82245d01a9816288b7a91a2d1.jpg)  
Source: Teikoku Data Bank, Ministry of Internal Affairs and Communications, Data compiled by GS Global Investment Research  
Source: Ministry of Internal Affairs and Communications, Japan Rice Stable Supply Support Organization, Data compiled by GS Global Investment Research

## Naphtha-flation: Impact on CPI Likely to Remain Small

We have previously expected the cumulative impact of soaring naphtha prices on the CPI to remain at +0.2-0.3pp, and we make no change to this forecast at this point. The CGPI (goods PPI equivalent) rose further in June, but no notable acceleration was seen in prices of naphtha-related items (naphtha, chemicals, plastic products, and rubber products), as Exhibit 7 indicates. As we pointed out before, this is likely because the margin of price increases shrinks as pass-through moves downstream. If the scale of pass-through downstream continues to lessen in this manner, the margin of increase in retail prices, which are the farthest downstream, is likely to remain small.

However, moves to raise B2B prices have been observed in July, mainly for construction material-related products (derived by increases in naphtha prices), posing upside risks to the July CGPI. $^{2}$ Furthermore, retail price hikes, seemingly stemming from surging naphtha prices, are scheduled from July onward for detergents, automobile tires, apparel, and other items, so we expect some positive contribution centered on non-durable goods prices.

The acceleration in the June CGPI was almost entirely due to higher fuel prices (such as jet fuel, kerosene, and heavy fuel oil; Exhibit 7). If fuel prices continue to rise, they could broadly push up import prices. However, the rate of fuel price increase is only about half the 2021 level.

Exhibit 7: Acceleration of Naphtha-flation Pauses in June B2B Prices
CGPI YoY Growth Rate and Contributions  
![](images/3406d499e088a7cc83b35fd88fc87e93945f025217ec6cb1436fd1c12d7d5176.jpg)  
Source: BoJ, Data compiled by GS Global Investment Research

## Private Services Prices: Pass-Through of Wage Hikes Remains Sluggish in Labor Intensive Sectors

In recent years, the pass-through of increased production costs has become more visible in goods prices, such as food products. In the service industries, however, the pace of increase in final demand prices (the majority of which are retail prices) remains sluggish compared to price increases upstream in the supply chain. Exhibit 8 shows a weighted average of various B2B service prices grouped by stage of the supply chain (the most upstream B2B service prices belong to Stage 1, with prices positioned progressively downstream classified into Stages 2, 3, and 4, while the most downstream prices, which are predominantly B2C, are grouped under final demand). The chart indicates that the lag in price increases is observed only at the final demand stage.

This trend is particularly pronounced in labor-intensive B2C services industries. The BOJ's labor-intensive corporate services (services with a high labor cost ratio) prices are rising in tandem with the wage growth rate, indicating that the pass-through of personnel costs in B2B prices is progressing smoothly. However, the labor-intensive private services CPI, our estimate using a similar methodology, remains at a low growth rate (Exhibit 9).

We had expected services prices to also rise to some extent in April—a month when private services price revisions are concentrated—reflecting the high wage growth rate, but the actual margin of increase in April-May was smaller than expected.

Exhibit 8: In the Services Industry, Pass-Through to Final Demand Prices Lags Price Increases Upstream in the Supply Chain

B2B and B2C Service Prices Grouped by Stage of the Supply Chain (FD-ID Price Index)

![](images/21126b0b6b1b17aeecbf802f4f8f0eae2dbaca02493357fdb93b0543a9954db0.jpg)  
For final demand services prices, we have removed special factors such as free high school tuition.

Exhibit 9: Despite Accelerating Wage Growth, No Signs of Acceleration Apparent in Labor-Intensive Retail Services Prices
Basic Wage Growth and Services Prices

![](images/34c19f562dbe376ab93e41e86ec51f2ce6a662cd7fc7e047d14f80fc1bc23269.jpg)  
Source: BoJ, Ministry of Health, Labour and Welfare  
Source: BoJ, Data compiled by GS Global Investment Research

FY2026 Core CPI Outlook Revised Down, FY2027 Revised Up
We revise our core CPI (excludes fresh food) forecasts to 2.1% (-0.2pp from previous forecast) for FY2026 and 2.3% (+0.2pp) for FY2027. In contrast to the new core CPI forecast for FY2026, which is unchanged from our previous forecast, we lower our core CPI forecast mainly because crude oil prices are below our forecast as of April, and the electricity and gas price control measures for the summer of 2026 exceeded our initial assumptions in scale (Exhibit 10).

Exhibit 10: Core CPI Expected to Turn Up in the Summer and Accelerate in November
Core CPI Forecast and Factor Decomposition  
![](images/b92c74f659b45881bd0f7c4c885a363f54a5c68ef8d78cbcb5787f06b5d79ce5.jpg)  
To avoid complicating the exhibit, only factors other than energy price control measures are listed as special factors (energy prices include the impact of policy factors).  
Source: Ministry of Internal Affairs and Communications, GS Global Investment Research

Regarding FY2027 as well, we raise our core CPI forecast by less than the new core CPI, reflecting the downward revision to the crude oil price forecast by our commodities research team (whereas their forecast as of April 2026 was for the Brent price to remain at US\$80/bbl throughout 2027, the team has now revised this to a decline to US\$70 by the end of 2027).

Energy Prices: Price Risks Are Two-Sided Amid Fluid Middle East Situation, but Government Price Control Measures Likely to Suppress Core CPI Volatility
We assume that crude oil prices will return to US\$70/bbl, the level before the deterioration of the Middle East situation, by the end of 2027. As a result, gasoline prices would fall below ¥170/liter in 2027, and the fuel price control measures, which are designed to ke

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
