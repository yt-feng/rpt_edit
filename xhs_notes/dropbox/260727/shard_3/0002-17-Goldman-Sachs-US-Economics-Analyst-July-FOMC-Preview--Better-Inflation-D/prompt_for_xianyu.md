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

# July FOMC Preview: Better Inflation Data, Worse Geopolitical News

The inflation data have improved but the geopolitical news has worsened in recent weeks. We expect the -2bp core CPI print for June to translate to 18bp on core PCE and mark the start of a softer trend. We also expect the BEA's recently announced methodological changes designed in part to fix the mismeasurement of AI effects to shave 0.2pp off of year-over-year inflation. But the re-escalation of the war with Iran and attacks on Russian oil refineries have pushed energy prices higher and revived fears that the already lengthy series of supply shocks could continue.

David Mericle
+1(212)357-2619 |
david.mericle@gs.com
GS & Co. LLC

We expect the FOMC to leave the fed funds rate unchanged at its July meeting next week. The statement might acknowledge the upside risks to inflation posed by renewed geopolitical conflict, and there will likely be at least one dissent in favor of a hike.

Market pricing implies that investors see the outcome of the July meeting as unusually uncertain, likely because the FOMC has been split recently, Chairman Warsh's own position remains unclear, and some of the re-escalation with Iran occurred during the blackout period. But most voters appear unlikely to push for a hike next week after the softer June inflation data, the Fed has historically avoided delivering surprise rate hikes, and we suspect that voters might be especially reluctant to do so at a meeting without a Summary of Economic Projections.

Despite the rebound in oil prices, we continue to think that the combined impact of tariffs, the war, and AI effects on monthly inflation should diminish in the months ahead, leaving core inflation soft enough for the FOMC to stay on hold through the end of the year.

But comments from FOMC participants indicate that many could support hiking if the inflation news is worse than we expect. As a result, as we noted when the re-escalation with Iran began, we see little margin for error on inflation and suspect that continued conflict could influence the rate hike debate more than the oil passthrough math alone implies by adding to concerns that supply shocks could continue and can come back unpredictably even after they appear over.

We are skeptical that modest rate hikes would provide much of a disinflationary offset to the impact of supply shocks. We suspect Fed officials would agree, but if the inflation news does not continue to improve as we expect, some might still see it as important for the Fed to respond to avoid the public misperception that it accepts high inflation. Many FOMC participants have also expressed concern that prolonged high inflation could unanchor inflation expectations, and while we do not think this has happened yet, some might feel that it can be difficult to know in real time and that it is better to err on the side of acting early.

For these reasons, while our baseline forecast remains that the Fed will remain on hold through year-end, we have raised our probability of eventual rate hikes from 25% to 35%. Even after the change, our probability-weighted Fed forecast remains dovish relative to market pricing.

## July FOMC Preview: Better Inflation Data, Worse Geopolitical News

The inflation data have improved but the geopolitical news has worsened since the FOMC last met in June. We expect the -2bp core CPI print for June to translate to 18bp on core PCE and mark the start of a softer trend for core inflation. We also expect the BEA's recently announced methodological changes designed in part to fix the mismeasurement of AI effects to shave 0.2pp off of year-over-year inflation in the August report released in late September.

But the re-escalation of the war with Iran and attacks on Russian oil refineries have pushed energy prices higher (Exhibit 1) and revived fears that the already lengthy series of supply shocks could continue. The White House also announced new tariffs on Friday, though they will have little impact on the average tariff rate.

Exhibit 1: Re-escalation of the War with Iran Has Pushed Oil and Refined Product Prices Higher Again  
![](images/96ebb7d4c1b53374531e3307f388e40cd56c19c2ad88e8aafed592d1dbbc0b5b.jpg)  
Source: GS Global Investment Research, Department of Energy, EIA

We expect the FOMC to leave the fed funds rate unchanged at its July meeting next week. President Logan has expressed support for “modestly higher” interest rates and might dissent in favor of a hike, and one or two other voters might as well. The post-meeting statement might acknowledge the upside risks to inflation posed by renewed geopolitical conflict as a nod toward the possibility that the FOMC could hike if the situation worsens.

We do not expect Warsh to offer many hints about the policy outlook in his press conference, though he might also acknowledge the upside risks to inflation posed by the latest rise in oil prices. He recently announced the leaders of the five Chairman's Task Forces for Advancing Monetary Policy and might provide an update on the timeline for their work.

Market pricing implies that investors see the outcome of the July meeting as unusually uncertain. If current pricing implying a roughly 40% chance of a hike persists going into the meeting, either outcome would be the largest surprise in a few decades at a meeting where the Fed hiked or held (Exhibit 2), because the Fed has historically avoided

delivering surprise rate hikes at its meetings.

The market uncertainty likely reflects that Chairman Warsh's approach is sufficiently different to raise doubts about whether historical patterns still apply, that his own position on hiking remains unclear, that the FOMC has been split recently, that some of the re-escalation with Iran occurred during the blackout period, and that further escalation is possible before Wednesday. While we agree that the uncertainty is greater than usual, most voters appear unlikely to push for a hike next week after the softer June inflation data, and some might be especially reluctant to deliver a surprise hike at a meeting without a Summary of Economic Projections out of fear that the market might infer more than they intended.

Exhibit 2: In Recent Decades, the Fed Has Shown a Strong Aversion to Delivering Surprise Rate Hikes  
![](images/c40ac93f643be4fa098c65f2e2760fc449513b0060a6c6aab875437f54071076.jpg)  
\* Assuming that current market pricing remains unchanged before the meeting.  
Source: GS Global Investment Research

Despite the rebound in oil prices, we continue to expect the combined impact of tariffs, the war, and AI mismeasurement on monthly inflation to diminish in the months ahead (Exhibit 3). That said, both the effects of the war and the month-to-month impact of the software & accessories category are uncertain. FOMC participants have appeared to take the effects of AI demand on the inflation statistics at face value—in contrast to our view, which is shared by some Fed staff economists and the BEA—and the FOMC’s June minutes suggested that any source of further firmness in inflation, including these three factors that a central bank might normally look through, could count as an argument for rate hikes.

Exhibit 3: Despite the Rebound in Oil Prices, We Still Think That the Combined Impact of Tariffs, the War, and AI Mismeasurement on Monthly Inflation Should Diminish in the Coming Months

![](images/0ae01fa81e7e8df4a1708e2a58fdb3b110b95043d65bdfe1dbfa9444328dfc03.jpg)  
Source: GS Global Investment Research

Our core PCE inflation forecasts for the rest of the year, starting with 18bp in June, 21bp in July, and 23bp in August (Exhibit 4), should be soft enough for the FOMC to stay on hold through year-end.

Exhibit 4: We Expect Upcoming Core Inflation Numbers to Be Soft Enough to Keep the Fed on Hold, but the Re-escalation with Iran and the Rebound in Oil Prices Have Further Reduced the Margin for Error  
![](images/4ff5da685443aca57ad5e24b9ac9ade0a6ce67e959ac069fa484faf50c445102.jpg)

<table><tr><td colspan="5">Upcoming FOMC Meetings and GS Inflation Forecasts</td></tr><tr><td>FOMC Meeting</td><td>July</td><td>September</td><td>October</td><td>December</td></tr><tr><td>Latest Data</td><td>June CPI and implied PCE</td><td>August CPI and implied PCE</td><td>September CPI and implied PCE</td><td>October CPI and PCE</td></tr><tr><td>MoM Core CPI</td><td>-0.02%</td><td>0.20%</td><td>0.17%</td><td>0.21%</td></tr><tr><td>YoY Core CPI</td><td>2.57%</td><td>2.34%</td><td>2.29%</td><td>2.41%</td></tr><tr><td>MoM Headline CPI</td><td>-0.42%</td><td>0.49%</td><td>0.09%</td><td>0.10%</td></tr><tr><td>YoY Headline CPI</td><td>3.46%</td><td>3.50%</td><td>3.29%</td><td>3.26%</td></tr><tr><td>MoM Core PCE</td><td>0.18%</td><td>0.23%</td><td>0.20%</td><td>0.20%</td></tr><tr><td>YoY Core PCE</td><td>3.33%</td><td>3.05%</td><td>3.06%</td><td>3.04%</td></tr></table>

Source: GS Global Investment Research

But comments from FOMC participants indicate that many could support hiking if the inflation news is worse than we expect (Exhibit 5). As a result, as we noted two weeks ago when the re-escalation with Iran began, we see little margin for error on inflation and suspect that continued conflict could influence the rate hike debate more than the oil passthrough math alone implies by adding to concerns that supply shocks could continue and can come back unpredictably even after they appear over.

Exhibit 5: Recent Comments from FOMC Participants Suggest That Many Could Support Hiking If the Inflation News Is Worse Than We Expect

<table><tr><td>Date</td><td>Speaker</td><td>Quote</td></tr><tr><td>July 16</td><td>Jefferson</td><td>[The current] policy stance should ... [allow] inflation to resume its decline toward our 2 percent target as the effects of past tariffs and energy prices pass through completely. ... In a scenario where actual inflation does not start to cool down soon, I believe that it could be appropriate to reconsider our current policy stance to ensure we fulfill our commitment to deliver price stability. ... The quick succession of shocks raises the risk that inflation becomes entrenched and inflation expectations become unanchored.</td></tr><tr><td>July 16</td><td>Logan</td><td>Modestly higher interest rates would better balance the outlook and risks for the FOMC&#x27;s dual mandate goals.</td></tr><tr><td>July 16</td><td>Schmid</td><td>Though this week&#x27;s inflation data showed an encouraging deceleration, it would be premature to put too much weight on a single data point relative to recent trends. ... With the price of oil once again rising, it is uncertain how persistent any relief on energy will be.</td></tr><tr><td>July 15</td><td>Cook</td><td>If we do not see signs of disinflation soon, I am prepared to act.</td></tr><tr><td>July 15</td><td>Williams</td><td>With inflation running high, it is imperative that we restore it to the Federal Reserve&#x27;s 2 percent longer-run goal on a sustained basis. The current stance of monetary policy is well positioned to do that.</td></tr><tr><td>July 14</td><td>Warsh</td><td>The FOMC&#x27;s job is to make sure that any short-term changes in particular prices don&#x27;t broaden out, don&#x27;t change to a generalized change in the price level.</td></tr><tr><td>July 14</td><td>Goolsbee</td><td>We need to start having the conversation about whether inflation is going to be more persistent than we want it to be.</td></tr><tr><td>July 13</td><td>Waller</td><td>I will need to see several months of lower readings to feel that inflation is moving in the right direction ... I think that is still a reasonable outcome, and I would then continue to hold the policy rate at its current target range.</td></tr><tr><td>July 8</td><td>June FOMC Minutes</td><td>Most participants, however, also pointed to scenarios in which, in the context of stable labor market conditions, inflation would remain elevated due to strong AI-related demand, the conflict in the Middle East, or the effects of tariffs. In such scenarios, almost all of these participants indicated that some policy firming would likely be warranted to return inflation to 2 percent.</td></tr><tr><td>June 30</td><td>Hammack</td><td>Right now, I see no tension in our mandates—inflation is too high and if that continues, it may mean that we need higher interest rates to bring inflation back down to target.</td></tr></table>

Source: GS Global Investment Research

We noted last week that evidence from economic research suggests that modest rate hikes would not provide much of a disinflationary offset to the much larger inflationary impact of supply shocks.

We suspect Fed officials would agree, but if the inflation news does not improve as we expect, some might still see it as important for the Fed to respond to avoid the potential public misperception that it accepts high inflation. Many FOMC participants have also expressed concern that prolonged high inflation could eventually broaden out or unanchor inflation expectations. While we do not think either has happened in a dangerous way yet (Exhibit 6), some participants might feel that it can be difficult to know in real time and that it is better to err on the side of acting early.

Exhibit 6: We Do Not Think That High Inflation Has Broadened Out Dangerously or Inflation Expectations Have Become Unanchored, but Fed Officials Will Worry More the Longer the Supply Shocks Last

![](images/b006ed7df49e3cf348e54bd59ed504e6f6656d36e55b11c74493027aca899b89.jpg)  
Source: GS Global Investment Research

![](images/9d033077cf71d56dee12f68135b1ee9d4bcbfa209c0f3d54ea65fb48ca57e81b.jpg)

For these reasons, while our baseline forecast remains that the Fed will remain on hold through year-end, we have raised our probability of rate hikes from 25% to 35%. Even after the change, our probability-weighted Fed forecast remains dovish relative to market pricing.

Exhibit 7: We Have Raised Our Probability of Rate Hikes to 35%, but Both Our Baseline and Probability-Weighted Fed Forecasts Remain More Dovish Than Market Pricing  
![](images/302bb2ae5c34a9bc3f787c305b720b0dd508f1855ae11f3bd91d069ed49ecf39.jpg)  
Source: GS Global Investment Research

## David Mericle

## The US Economic and Financial Outlook

<table><tr><td rowspan="2"></td><td rowspan="2">2023</td><td rowspan="2">2024</td><td rowspan="2">2025</td><td rowspan="2">2026</td><td rowspan="2">2027</td><td rowspan="2">2025Q4</td><td colspan="4">2026</td><td colspan="4">2027</td></tr><tr><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td></tr><tr><td colspan="15">OUTPUT AND SPENDING</td></tr><tr><td>Real GDP</td><td>2.9</td><td>2.8</td><td>2.1</td><td>2.3</td><td>2.1</td><td>0.5</td><td>2.1</td><td>2.6</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.1</td><td>2.2</td><td>2.3</td></tr><tr><td>Real GDP (annual=Q4/Q4, quarterly=yoy)</td><td>3.4</td><td>2.4</td><td>2.0</td><td>2.2</td><td>2.1</td><td>2.0</td><td>2.7</td><td>2.4</td><td>1.8</td><td>2.2</td><td>2.2</td><td>2.0</td><td>2.1</td><td>2.1</td></tr><tr><td>Consumer Expenditures</td><td>2.6</td><td>2.9</td><td>2.6</td><td>1.8</td><td>1.9</td><td>1.9</td><td>0.5</td><td>2.3</td><td>1.5</td><td>1.5</td><td>1.9</td><td>2.0</td><td>2.1</td><td>2.2</td></tr><tr><td>Residential Fixed Investment</td><td>-7.8</td><td>3.2</td><td>-2.2</td><td>-4.1</td><td>1.2</td><td>-1.7</td><td>-7.8</td><td>-2.5</td><td>-1.5</td><td>1.5</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.3</td></tr><tr><td>Business Fixed Investment</td><td>7.3</td><td>2.9</td><td>4.1</td><td>6.9</td><td>5.8</td><td>2.4</td><td>10.6</td><td>8.8</td><td>7.5</td><td>6.9</td><td>4.9</td><td>4.9</td><td>4.9</td><td>4.9</td></tr><tr><td>Structures</td><td>16.7</td><td>1.1</td><td>-5.3</td><td>-3.6</td><td>2.1</td><td>-6.6</td><

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
