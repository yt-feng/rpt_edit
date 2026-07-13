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

# Tracking Inflation Risks from the Middle East Conflict

The US and Iran each carried out new attacks over the last week. A serious re-escalation of the conflict would threaten to revive the key upside risk to inflation and raise the odds of rate hikes.

Oil prices have risen only moderately so far during the latest escalation and remain roughly $30\%$ below the levels reached in late April and early May. Gasoline prices have declined $15\%$ , jet fuel prices have fallen $35\%$ , prices of other Persian Gulf exports are down sharply from their wartime peaks, and while shipping costs have kept rising, the increase so far should have only a modest impact on consumer prices. Oil flows from Gulf countries dipped last week but remain above their lows, and total oil inventories have not been replenished but are not strikingly low.

A key question for upcoming inflation reports and for the Fed is how much impact further disruptions caused by the conflict are likely to have on consumer prices. We approach this question using two statistical tools. The first is our model of passthrough from commodity prices to consumer prices, which suggests that the monthly impact peaked in Q2 and should decline noticeably in Q3 and further in Q4, assuming there is no re-escalation of the conflict that raises energy prices again. The second tool uses measures of shortages and supply chain pressures to estimate the broader effects of conflict-related disruptions beyond energy and also suggests that, barring further escalation, these effects should decline substantially in Q3 and Q4.

A major concern for Fed officials is that the lengthy series of supply shocks that has kept inflation elevated for a long time could pose a risk to inflation expectations. So far, measures of inflation expectations send mixed signals but do not look concerning overall: market-based measures are more subdued and seem to be receiving more attention from Fed officials, while some consumer measures are higher but increasingly subject to doubts about their reliability. Our composite indicator of persistent inflation risks suggests that absent re-escalation, the inflation shock from the war was probably not severe or long-lasting enough to spark lasting inflation contagion.

\- Like the effects of the war and oil price spike, the incremental effects of tariffs and AI demand on month-over-month inflation should fade in coming months. We expect core PCE inflation to come in at 24bp in June and to remain in a 20-23bp range in the months that follow. We expect methodological changes

David Mericle +1(212)357-2619 | david.mericle@gs.com GS & Co. LLC

Pierfrancesco Mei +1(212)902-8809 | pierfrancesco.mei@gs.com GS & Co. LLC

implemented in August to lower the year-over-year rate by 0.2pp to $3.2\%$ , but it will likely fall only a touch further ahead of the Fed's remaining meetings this year. This path should keep the Fed on hold for the rest of 2026, but it leaves little margin for error.

\- Our models suggest that a potential re-escalation that pushed oil prices back up to \$100 per barrel would boost monthly core inflation by 3-4bp in coming months. But the impact of yet another supply shock on the monetary policy debate could be more significant than the passthrough math alone suggests because it would add to the fear that further shocks might still be ahead of us and could eventually become enough to unanchor inflation expectations.

## Tracking Inflation Risks from the Middle East Conflict

The US and Iran each carried out new attacks over the last week, renewing concerns about disruptions to shipping through the Strait of Hormuz. A more serious re-escalation of the conflict would threaten to revive the key upside risk to inflation and consequently raise the odds of the Fed raising the funds rate.

We take stock of how much of the inflationary pressure caused by the conflict had reversed before the latest attacks, how much passthrough to consumer prices is still in the pipeline, how much the latest in a long series of supply shocks has influenced inflation expectations, and how the effects of the conflict are likely to shape the monthly inflation path ahead of upcoming Fed meetings in both a de-escalation scenario and a scenario where the conflict restarts and sparks further inflationary pressure.

## Much of the Commodity Price Shock from the War Has Reversed

Oil prices have risen only moderately during the latest escalation and remain roughly 30% below the levels reached in late April and early May. Retail gasoline prices have declined 15%, which should contribute to a decline in headline CPI in June, and jet fuel prices have fallen 35%, which should weigh on airfares in coming months.

Exhibit 1: Oil Prices Have Risen Only Moderately During the Latest Attacks and Remain Roughly 30% Below Their Wartime Peak; Gasoline Prices Are Down 15%, and Jet Fuel Is Down 35%  
![](images/ef3c4863440e673a38eebda59eb55af8be0c23c0899615e6dc97e0874bbb0bc7.jpg)

![](images/2c8989d481223db188b0295859fcc2e5aafdd32b40bd7260fa0e28d78318af94.jpg)  
Source: GS Global Investment Research, Department of Energy, EIA

The prices of other Persian Gulf exports such as methanol, polyethylene, and nitrogen have also declined after spiking at the start of the war. Most are now close to their pre-war levels, though the prices of sulfur and ammonia remain elevated.

Air and ocean shipping costs have kept rising, reflecting both war-related effects such as fuel surcharges and reduced network efficiency as well as unrelated forces such as limited capacity growth, an earlier start to the peak shipping season for ocean freight, and strong semiconductor shipments driving up air cargo rates. But the increases remain much smaller than in 2021-22, and their impact on consumer prices should be modest because international shipping costs only amount to $1 - 2\%$ of the cost of US consumer goods imports.

Exhibit 2: Prices of Other Gulf Exports Are Down Substantially from Their Wartime Peaks; Shipping Costs Have Kept Rising, but the Moderate Increase to Date Should Have a Modest Impact on Consumer Prices  
![](images/d8c2a86349721724622ffbdc153112765061ed8f309ecd2bb490d8f3d15b8927.jpg)  
Source: GS Global Investment Research, Bloomberg, Drewry

![](images/e211262292e48e7b83579d926dd5a9d96aa2f08f62b856f96a6cf37ddf954956.jpg)

Oil flows from Gulf countries began to dip after the first reported attack on a crude tanker on June 27 but remain above their lows on a 7-day average basis. Our commodities strategists' measure of total global visible oil stocks bottomed in mid-June and had increased gradually since then, suggesting that oil inventories have not been meaningfully replenished but are not strikingly low either.

Exhibit 3: Oil Flows from Persian Gulf Countries Have Dipped but Remain Well Above Wartime Lows; Aggregate Oil Inventories Have Not Yet Been Meaningfully Replenished but Are Not Especially Low Either  
![](images/62c079635fb0ebce613ab4b20497b965fa18fd4cf01d1b7a427938230f8e1144.jpg)  
Source: GS Global Investment Research, Kpler, S&P Global Commodities at Sea, IEA, DOE

![](images/1035c5ea61894b8736b674fed73a2dab5646da186fe49fcd19918f6c7473da68.jpg)

## A Bit More Pressure on Consumer Prices in the Pipeline but a Fading Impact on Monthly Inflation

A key question for upcoming inflation reports and for the Fed is how much further impact disruptions caused by the conflict will have on consumer prices. We approach this question using two statistical tools.

The first is our model of passthrough from commodity prices to consumer prices, which incorporates our strategists' latest commodity price forecasts, refined product spreads, effects on transportation costs, and spillover effects via imports from other economies hit harder by the shocks to both oil and natural gas prices. In our baseline, we assume that refined product spreads gradually normalize over the next couple of months and that transportation costs evolve in line with their usual relationship with oil. The model suggests that the incremental effects on month-over-month core PCE inflation peaked in Q2 and should decline noticeably in Q3 and further in Q4, assuming there is no re-escalation of the conflict that pushes energy prices higher again.

Exhibit 4: Our Model of Passthrough from Commodity Prices to Consumer Prices Suggests That the Incremental Effects Peaked in Q2 and Should Decline a Bit in Q3 and More Substantially Beyond That  
![](images/c96cc970b1905b6b28428dc87f95901abdf67a5fb1351cf72e627581f9ba95eb.jpg)  
Source: GS Global Investment Research

The second tool uses measures of shortages and supply chain pressures constructed by Fed Board and New York Fed economists to estimate the broader effects of conflict-related disruptions beyond energy and the timing of their impact. These measures rose much less during the war with Iran than during the pandemic and had reversed meaningfully from their peaks before the attacks last week.

Exhibit 5: Measures of Shortages and Supply Chain Pressures Rose Much Less Than During the Pandemic and Had Begun to Reverse Before the Attacks Last Week  
![](images/024cd7f41678041f458ecb743fdfd0821f7665047248561d77ed8b24c76dbba2.jpg)  
Note: Shortage index originally introduced in Caldara, Iacoviello and Yu (2025), "Measuring Shortages Since 1900," Fed International Finance Discussion Papers.  
Source: GS Global Investment Research, Federal Reserve Board, New York Fed

![](images/3a0cc77f4e44d039432475acea6bb5ad0a6adbaa323e18e3606dc53056f6cf6b.jpg)

We first estimate the historical relationships between these measures, energy prices, and consumer prices and the persistence of shocks to each; then estimate the series of shocks to the shortage and supply chain pressure measures that produce the realized paths since the start of the war shown above; and then finally estimate the impact of those series of shocks on consumer prices, controlling for the effect of changes in oil prices. This model also suggests that, barring further escalation, the impact on monthly inflation peaked in May and June and should decline substantially in Q3 and Q4.

We treat these results as a second opinion on the timing of the impact of the conflict on monthly inflation rather than as additive to the effects of commodity price passthrough and the predictions of our bottom-up inflation model because there is likely substantial overlap.

Exhibit 6: Our Models of the Impact on Consumer Prices of Shortages and Supply Chain Pressures Beyond Those Connected to Energy Price Moves Also Implies That the Effects Should Decline Quickly in Q3 and Q4  
![](images/4da5e9e644bcea9ad5098a1e0442a18b56d46935666fc4960e8e51bc38f930e4.jpg)  
Source: GS Global Investment Research, Federal Reserve Board, New York Fed

## The War Shock Has Not Been Severe or Long-lasting Enough to Unanchor Inflation Expectations

A major concern for Fed officials is that the lengthy series of supply shocks that has kept inflation elevated for a long time could pose a risk to inflation expectations. Despite the abundance of data on inflation expectations available today, assessing this risk has proven less straightforward than one might assume because the measures send mixed messages and some have become less reliable.

As Chairman Warsh highlighted recently, market-based measures of inflation compensation remain subdued. Some measures of consumer inflation expectations, in particular the Michigan measure, are higher but are increasingly subject to doubts because consumer survey responses have become more politicized and less connected to macroeconomic outcomes.

Taken together, these trends imply that the Fed's aggregate Index of Common Inflation Expectations will remain in its recent range in Q2 and then moderate a bit, as long as there is no further escalation of the conflict and upward pressure on oil prices. This overall message would not be particularly concerning.

Exhibit 7: With Market-Based Measures Still Subdued but Some Consumer Survey Measures Higher, the Fed's Composite Measure of Inflation Expectations Is Likely to Fall a Bit and Remain in Its Recent Range  
![](images/2c8b607a58a3c1d70f6797efbcbd1ab2aec8ce5c23c7119ec2415fe3a24994ee.jpg)  
\* Scenario where oil prices increase to \$100 by the end of August and remain at that level through year-end.  
Source: GS Global Investment Research, Federal Reserve

Our composite indicator of persistent inflation risks sends a similar message. It captures ways in which the initial shock could give rise to self-perpetuating high inflation, namely by making larger-than-usual price increases seem normal to businesses, by raising inflation expectations, or by putting a wage-price feedback loop into motion. It also suggests that the inflation shock from the war has probably not been severe or long-lasting enough to spark inflation contagion, absent further escalation.

Exhibit 8: Our Composite Indicator of Persistent Inflation Risk Suggests That, Absent Re-escalation, the War Shock Was Probably Not Severe or Long-Lasting Enough to Spark Lasting Inflation Contagion  
![](images/b3bb1a92a95a5264e3b462534512d14b8c6d0a706daebd50829cca4ce580bb16.jpg)  
Note: We exclude our estimates of the effects of tariffs on each PCE category, as well as the computer software and accessories component (see "US Economics Analyst: AI and (Measured) Inflation: Up Then Down," May 2026).  
Source: GS Global Investment Research

A Softer Monthly Inflation Path in Coming Months Should Keep the Fed on Hold Where will all of this leave the inflation path over the next several months? Like the effects of the war and the oil price spike, the incremental effects of tariffs and (mismeasured and overstated) AI demand on month-over-month inflation should fade going forward, though the precise monthly path of AI effects is quite uncertain. The combined impact of these three forces on month-over-month core PCE inflation is likely to remain modestly positive but fade sharply in the back half of the year, while the impact on year-over-year inflation is likely to remain roughly steady through year-end.

Exhibit 9: Temporary Pressure from Mismeasured AI Effects, Higher Energy Prices, and Tariffs Should Have a Fading Impact on Monthly Inflation but a Steady Impact on Year-over-Year Inflation in the Rest of 2026  
![](images/90f66b02c64690980736ad8ee0767e4f22d0507e265dd7643c8db1d711f02880.jpg)  
Source: GS Global Investment Research

Incorporating these effects into our bottom-up inflation model suggests that monthly core PCE inflation will come in at about 24bp in June and remain in a 20-23bp range in the months that follow. The year-over-year rate is likely to decline by about 0.2pp to

3.2% in August, we estimate, when the Bureau of Economic Analysis will incorporate methodological changes to inflation measurement that will affect previous months as well. Beyond that point, we expect it to fall only slightly further ahead of the Fed's remaining meetings in 2026, before falling more substantially in 2027.

We think that our forecasted inflation path would keep the Fed on hold for the rest of 2026, but it leaves little margin for error and could lead to some disagreement among FOMC participants.

Exhibit 10: We Expect the Upcoming Inflation News to Be Soft Enough to Keep the Fed on Hold This Year  
![](images/20813027af091c78f4af23e36950ecf90d018878f6eeb506fcf509c09c1def6e.jpg)  
\* See "US Daily: Upcoming Methodological Changes Will Likely Lower Measured Core PCE Inflation," June 2026.  
Source: GS Global Investment Research

<table><tr><td colspan="5">Upcoming FOMC Meetings and GS Inflation Forecasts</td></tr><tr><td>FOMC Meeting</td><td>July</td><td>September</td><td>October</td><td>December</td></tr><tr><td>Latest Data</td><td>June CPI and implied PCE

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
