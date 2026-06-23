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
US ECONOMICS ANALYST

# Mid-Year Inflation Outlook: Oil and AI vs. Wages and Rent

Core PCE inflation has reaccelerated this year, partly reflecting a combination of energy price passthrough, AI-related price pressures amplified by measurement issues, and financial services inflation driven by higher equity prices. In this week's Analyst, we take stock of the inflation outlook.

The US-Iran agreement has reduced upside risks to inflation from higher energy prices. Our commodity strategists lowered their oil forecasts to \$80 on average in 2026Q4 and \$75 in 2027 (vs. \$90 and \$80 previously), which implies about 0.2pp and 0.05pp less upward pressure on headline and core PCE inflation this year than our previous assumptions. In the near term, lower gasoline prices will translate into soft headline inflation prints in June, and our preliminary headline CPI and PCE estimates for June stand at -0.13% and 0.07%, respectively. The prices of several other non-oil Gulf exports have also declined meaningfully in recent days. We now estimate that commodity prices will deliver a roughly 0.4pp boost to year-over-year core PCE inflation through 2026Q4.

AI-related pressure on memory prices has pushed up computer software and accessories inflation, generating an especially large boost to core PCE because of measurement distortions. We expect monthly software and accessories inflation to slow from about 4-5% in recent months to about 0.6% by 2026Q4, reflecting a sharp slowdown in memory price inflation in recent months. We also expect higher memory prices to increase phone and computer inflation throughout 2026, though with smaller contributions to overall core PCE than software and accessories. Taken together, we estimate that AI-related price pressures will boost year-over-year core PCE inflation by about 0.4pp in December 2026 (with a peak of 0.6pp earlier in 2026H2, vs. 0.25pp already realized) and core CPI inflation by about 0.1pp.

We continue to have a benign outlook for underlying core inflation outside AI-related components and energy price passthrough. We expect rent growth to slow to below its pre-pandemic pace, reflecting soft new-tenant rent growth. We also expect slow nominal wage growth to put downward pressure on core nonhousing services inflation, though we expect healthcare inflation to remain around its current pace as prices continue to catch up to costs. Our indicators of persistent inflation risk and pipeline inflation pressures suggest that underlying inflation risk rose slightly in recent months but remains modest.

We forecast year-over-year core PCE inflation of 3.2% in December 2026,

Manuel Abecasis
+1(212)902-8357 |
manuel.abecasis@gs.com
GS & Co. LLC

followed by a slowdown to 2.2% by December 2027 as the AI and energy effects wane. In the near term, we expect strong increases in lagged equity prices to boost monthly core PCE inflation by 0.10pp in May and 0.05pp in June. We expect core CPI—which is less affected by AI measurement issues and stock market swings—to slow to 2.6% year-over-year by December 2026 and 2.2% by December 2027. We see risks to our forecast skewed to the upside on net, particularly if the situation in the Middle East deteriorates or if higher inflation expectations cause businesses to raise prices beyond increases in their input costs.

## Mid-Year Inflation Outlook: Oil and AI vs. Wages and Rent

Core PCE inflation has reaccelerated this year, partly reflecting a combination of energy price passthrough, AI-related price pressures amplified by measurement issues, and higher equity prices. In this week's Analyst, we take stock of the inflation outlook.

## Relief From the US-Iran Agreement

The US-Iran agreement and recent decline in oil prices have reduced upside risks to inflation. Our commodity strategists lowered their oil forecasts to \$80 on average in 2026Q4 and \$75 in 2027 (vs. \$90 and \$80 previously). In an upside scenario where the Strait of Hormuz remains disrupted through 2027, they expect Brent would rise to \$130 in 2026 and average \$105 in 2027. In a downside scenario with greater flows and stronger supply, they expect Brent would average just under \$70 in 2026Q4 and just under \$60 in 2027 (Exhibit 1).

Our strategists' new forecasts imply about 0.2pp and 0.05pp less upward pressure on headline and core PCE inflation by year-end than our previous assumptions. In the meantime, the recent decline in Brent and gasoline prices will translate into soft headline inflation prints in June, and our preliminary headline CPI and PCE estimates for the month stand at -0.13% and 0.07%, respectively.

Exhibit 1: Our Oil Strategists Now Expect Brent to Average \$80 in 2026Q4 and \$75 in 2027 (vs. \$90 and \$80 Previously)  
![](images/3d76d783d00cfafc1770818ab9a1376dafb75679579a4036f5f157af3af9c031.jpg)  
Source: GS Global Investment Research, Department of Energy

Beyond oil, we incorporate two other developments related to the conflict in the Middle East. First, the prices of non-oil Gulf exports like nitrogen and polyethylene have declined after rising sharply after the start of the war. Several products' prices are now close to their pre-war levels, though others remain elevated—particularly sulfur and ammonia (left side of Exhibit 2). Second, margins on refined oil products like jet fuel and gasoline rose significantly in May in the US, though they have since retraced some of their earlier increases (right side of Exhibit 2). Goods transportation costs also rose meaningfully in May, with the relevant PPI increasing a bit more than its typical relationship with oil prices would imply. Going forward, we expect refined product

spreads and goods transportation costs to normalize gradually as supply conditions in the Middle East improve.

Exhibit 2: Beyond Oil, the Prices of Several Gulf Exports Have Retraced From Their Recent Peaks, and Some Are Now Close to Pre-War Levels; US Refined Product Spreads Rose Sharply in May  
![](images/dd75a87d8e4289357c3616645fc3cd93100438fbf8dfa44a808b09b0415babdc.jpg)  
Source: GS Global Investment Research, Bloomberg

![](images/cd425e1d6e0d9e86e265494047d3575b1dbbbae95e9b588a51fc1655f97f2c98.jpg)  
Note: Weighted average refined product cash prices of gasoline, diesel, jet fuel, fuel oil, and naphtha. Weights based on relative demand for each product in 2025.

In Exhibit 3, we update our commodity price passthrough framework, including our oil strategists' latest forecasts, changes in goods transportation costs, and refined product spreads. We assume that refined product spreads gradually normalize over the next couple of months and that transportation costs behave in line with their usual relationship with oil. Taken together, we estimate that commodity prices will deliver a roughly 0.4pp boost to year-over-year core PCE inflation this year, with a smaller sequential boost in 2026H2.

Exhibit 3: We Estimate That Higher Commodity Prices Will Deliver a Roughly 0.4pp Boost to Year-over-Year Core PCE Inflation This Year, Which We Expect to Fade in 2027  
![](images/6feb997f83b7d953f1754026bcb66083526d3af736754b09d341aa6042a58191.jpg)  
Source: GS Global Investment Research

Exhibit 4 shows the implications of our commodity strategists' updated oil price scenarios for headline and core PCE inflation. In our baseline forecast, we expect year-over-year headline PCE inflation to start normalizing in June. In their upside scenario, we estimate a boost to core PCE inflation of 0.2pp and to headline PCE inflation of 1.1pp relative to our baseline. In their downside scenario, we estimate a drag on core PCE inflation of 0.1pp and on headline PCE inflation of 0.4pp relative to our baseline.

Exhibit 4: We Expect Headline Inflation to Slow From Here; Our Strategists' Upside Scenario Would Add Another 1.1pp to Headline PCE and 0.2pp to Core PCE, While Their Downside Scenario Would Subtract 0.4pp and 0.1pp  
![](images/792d3a13f2d822ba438eb7e3e6efa3605fe15760ee18d121944f0d34b7c37ef2.jpg)

![](images/39a6944898ab371fd96a773662c74443c59ef67e0347b7740804603046bf93e3.jpg)  
Note: Includes GS estimate for May PCE based on CPI, PPI, and import prices. Baseline assumes oil prices average \$88 in June and \$86 in July before declining to \$80 by 2026Q4. Downside scenario assumes oil prices average \$88 in June and \$84 in July before declining to \$70 by 2026Q4. Upside scenario assumes oil prices average \$88 in June and peak at \$130 in 2026 before declining to \$105 on average in 2027.  
Source: GS Global Investment Research, Department of Commerce

## The Inflationary Impulse From AI: Larger for PCE Than for CPI

The AI infrastructure boom led to a spike in memory prices as companies sought to buy chips to equip data centers. Prices for some types of memory rose 10-15x in a few months between 2025Q4 and 2026Q1 (left side of Exhibit 5). More recently, spot memory prices have remained very high relative to pre-2025Q4, but the pace of increases has slowed significantly. Contract prices faced by electronics manufacturers can lag spot prices by a few months, but the pace of increases has slowed for those too.

Higher memory prices have pushed up computer software and accessories inflation, generating an especially large boost to core PCE because of measurement distortions. While this component measures both software and accessories prices, in practice most of its variation can be explained by changes in memory prices that largely affect accessories costs (right side of Exhibit 5). We model computer software and accessories inflation using high-frequency memory prices, data from memory manufacturers, and our equity analysts' forecasts. Our model suggests that software and accessories inflation will slow from about 4–5% month-over-month in recent months to about 0.6% by year-end, reflecting the recent slowdown in memory price inflation.

![](images/788794d59e19c9b51df45b1840bfd5b9fe3d00759fec788a66d57a368a8992d2.jpg)  
Exhibit 5: Memory Prices Rose Sharply in 2025Q4 and 2026Q1 but Have Stalled Since; As a Result, We Expect Computer Software and Accessories Inflation to Slow in Coming Months  
Source: GS Global Investment Research, Trendforce, Department of Commerce

Computer software and accessories prices were flat in the May CPI report, suggesting that some of this slowdown is already underway. That said, this component is not seasonally adjusted by the BLS, and it has slowed by about 3pp relative to its prior trend in each of the last three Mays (reversing consistent accelerations earlier in the year), so much of the slowdown this May was likely residual seasonality. Going forward, we expect software prices to increase by 2-3% for the next couple of months and to slow further for the rest of the year.

We also expect higher memory prices to boost phone and computer inflation throughout 2026 as manufacturers pass through higher production costs. That said, the boost to core PCE should be smaller than that of software and accessories, in part because these categories receive smaller weights in PCE. Taken together, we estimate that AI-related pressure will boost year-over-year core PCE inflation by about 0.4pp in December 2026 (vs. 0.25pp so far, and a 0.6pp peak in 2026H2). We estimate a much smaller boost to core CPI inflation, of about 0.1pp, largely because CPI does not suffer from the same methodological issues as PCE.

Exhibit 6: We Expect AI-Related Price Pressures to Boost Year-over-Year Core PCE Inflation by 0.4pp by December 2026, With a 0.6pp Peak Earlier in H2; We Expect AI-Related Price Pressures to Boost Core CPI by About 0.1pp by December 2026

![](images/2a4f1815e00fc6c5f5cd2bb00bb77c2de6d32c3fb2b2da7185e90b97793d994c.jpg)  
Source: GS Global Investment Research, Department of Commerce, Department of Labor

## Disinflation From Rent and Wages

We continue to see a relatively benign outlook for core inflation outside of AI pressure and energy passthrough. We expect rent growth to slow to below its pre-pandemic pace, reflecting continued softness in new-lease rent growth (Exhibit 7). Monthly housing inflation has been volatile recently, spiking in April as the negative bias from last year's government shutdown unwound. Housing prices also rose at an above-trend pace in May, but most of the acceleration relative to the prior trend was concentrated in the Northeast, which we suspect reflected statistical noise. Going forward, we continue to expect housing inflation to slow and to settle at a pace roughly $1 - 1\frac{1}{2}$ pp below the pre-pandemic pace.

\*Average of Costar, Yardi, and Zillow measures of rent growth.

Exhibit 7: We Expect Housing Inflation to Continue to Slow This Year, Reflecting Soft New-Tenant Rent Inflation  
![](images/2a517b62ef30e3566ba76a8dd69928b39ea539e3e235d4b2f45e146683606ae7.jpg)  
Source: GS Global Investment Research, Department of Commerce, CoStar, Yardi, Zillow

We also expect slower wage growth to put downward pressure on nonhousing services inflation, excluding airfares—which are largely driven by oil price changes—and portfolio management—which are driven by equity prices. Wage growth has continued to slow this year, and we expect wage-sensitive PCE services to follow suit over the next several months. We think that the World Cup has likely temporarily boosted hotel prices but expect that to fade as the reservation window moves past the tournament’s end.

Exhibit 8: Slower Wage Growth in Labor-Intensive Services Should Provide an Additional Disinflationary Impulse This Year  
![](images/df0b0fc8953c97e2785c9eedd2f2ec48c6ee41d0ae8ba4896b7533cfe2fa2670.jpg)  
\* Includes food services, hotels and casinos, other recreational services, nursing homes, motor vehicle services, personal services, social services, household maintenance.

## Source: GS Global Investment Research, Department of Commerce

One exception within nonhousing services is the healthcare services category, which we expect to remain elevated this year. Healthcare services costs, as measured by the Centers for Medicare & Medicaid Services' Medicare Economic Index, have increased by 26% since 2020Q1, while consumer prices have increased 18%, making healthcare the last major remaining example of “catch-up inflation.” At the same time, we expect slowing wage growth for healthcare workers and a smaller Medicare fee update this year—an important anchor point in negotiations between healthcare providers and insurance companies—to keep healthcare inflation around its current 3% pace, roughly 1-1½pp above the pre-pandemic pace.

With housing and healthcare receiving roughly equal weight in core PCE, we expect the overshoot in healthcare inflation to roughly offset the similarly-sized undershoot in housing inflation, leaving their combined contribution around the pre-pandemic level.

Exhibit 9: Continued Catch-Up to Costs Will Put Upward Pressure on Healthcare Inflation, Though a Smaller Medicare Fee Increase (and Slowing Wage Growth) Should Limit the Upside  
![](images/05770468dadfb512ab86244755b373e237c08deb7a6f45cef5cf25237dae64a9.jpg)  
Source: GS Global Investment Research, Department of Commerce, Department of Health and Human Services

## Broader Inflation Risk

Our indicators of persistent inflation risk and pipeline inflation pressures suggest that underlying inflation risk rose slightly in recent months but remains modest. Exhibit 10 shows that our measure of pipeline pressures based on the signal from the PPIs accelerated in recent months, but most of this reflected price increases in energy and related products.

Exhibit 10: Our Tool for Tracking Input Cost Pressures Across the Supply Chain Accelerated Somewhat in Recent Months, but This Largely Reflected Energy Passthrough

![](images/84f7ebed1e6eb0995ea78804be0f980cbafe253686f709742a8e2068fbedb0a4.jpg)  
\* Sports a

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
