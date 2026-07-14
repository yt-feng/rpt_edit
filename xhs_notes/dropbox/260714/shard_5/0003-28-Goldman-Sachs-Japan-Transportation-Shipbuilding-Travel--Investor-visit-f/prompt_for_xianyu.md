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
# Japan Transportation/Shipbuilding/Travel: Investor visit feedback: Organizing main points of debate and future catalysts for each sector

Based on our visits to investors in Hong Kong from July 8 to 10, we summarize below the coverage sectors (shipping/shipbuilding/airlines/inbound tourism/logistics) that have been particularly discussed with investors recently.

\- Shipping: Overall, the majority view is that if the unstable situation in Middle East continues, the shipping market will rise due to the diversification of procurement routes, while if the situation improves, the market will deteriorate due to increased supply including the resumption of passage through the Suez Canal. In the short term, as the containership market is improving mainly due to better cargo volumes, there were many opinions expecting an upward revision to full-year profit guidance centered on containerships at the April-June earnings results, and a dividend hike based on a 40% payout ratio for Nippon Yusen (our FY3/27 estimate is ¥210/share, guidance is ¥200/share). On the other hand, there are also concerns about the possibility of supply-demand loosening from 2027 onward against the backdrop of an increase in containership completions. Furthermore, the upward trend in car carrier charter rates and the asset value of owned vessels that we pointed out are not widely recognized, and we believe they will remain as medium-term stock valuation catalysts.

\- Shipbuilding: There were many discussions on the trends of the Japanese government's support measures for the shipbuilding industry, the competitive environment with China/South Korea, and recent share price trends. As to the background of the share price correction over the past 3 months, a significant money flow from defense/geopolitics-related stocks, including shipbuilding, to AI tech stocks was most frequently cited. The FY3/27 P/E for Namura Shipbuilding/Mitsui E&S (for both, we are Buy rated) is around 10X, and we believe their undervaluation will become even stronger as earnings expand going forward. Tokyo Keiki (we are Buy rated), on which we recently initiated coverage, is in a position to capture overseas defense demand as a major supplier of defense equipment, and our impression is that the story of expanding domestic and overseas defense demand over the medium to long term had no particular pushbacks.

\- Airlines: Our impression was that there were many positive opinions toward the sector against the backdrop of the crude oil market peaking out. On the other hand, with investors' perspectives that share prices are pricing in normalized

Norihiro Miyazaki  
+81(3)4587-9842 |  
norihiro.miyazaki@gs.com  
GS Japan Co., Ltd.

Ryohei Kurita  
+81(3)4587-1799 |  
ryohei.kurita@gs.com  
GS Japan Co., Ltd.

earnings, there was also interest in looking for further earnings upside. From that viewpoint, we consider structural reforms in the domestic passenger business and the improvement in the international air cargo market as upside, and we had the impression that the latter, in particular, is not yet widely recognized. For ANA Holdings (we are Buy rated), the top-line upward elasticity is higher than in past cycles due to the consolidation of NCA in the most recent fiscal year, and we believe there is a high possibility that earnings expectations will be raised further.

Inbound tourism: Against the backdrop of the crude oil market peaking out, concerns about soaring fuel surcharges on flight tickets have receded, and our impression is that positive views have increased somewhat compared to 3 months ago. On the other hand, there were many views that Kyoritsu Maintenance/Kotobuki Spirits (for both, we are Buy rated) have seen quick share price recoveries, and that the earnings improvement for FY3/27 is largely priced in. We believe that short-term earnings are trending above guidance, and we can also expect medium-term catalysts (loyalty point program for Kyoritsu, and the launch of emerging brands for Kotobuki). For Japan Airport Terminal (we are Sell rated), although there are few catalysts to lift medium-term earnings, there were also points made to be aware of the positive impact from the introduction of the refund method for downtown duty-free shopping toward the second half of the fiscal year.

Logistics: Following the recent price revision for Yu-Pack/Yu-Packet by Japan Post, although there were some opinions expecting an improvement in the competitive environment of the parcel delivery industry, our impression was that the prevailing view was that the competitive environment remains severe given the recent fluctuations in volume share, and a sustained price hike cycle is still hard to envision. For SG Holdings (we are Sell rated), which has relatively high profitability, we maintain a cautious stance as we see lingering risks of profitability deterioration due to intensifying competition in the parcel delivery industry.

Exhibit 1: Valuations of companies mentioned in the report

<table><tr><td rowspan="3" colspan="2"></td><td rowspan="3">Rating</td><td rowspan="2">12m TP</td><td rowspan="2">Price</td><td rowspan="2">Upside /Downside</td><td rowspan="2">Market Cap</td><td rowspan="2">ADVT (6M)</td><td rowspan="2" colspan="3">PER</td><td rowspan="2">PBR</td><td rowspan="2">Div Yield</td><td rowspan="2">EV/EBITDA</td><td rowspan="2">RoE</td><td rowspan="2" colspan="3">OP YoY</td><td rowspan="2" colspan="4">SP performance</td></tr><tr></tr><tr><td>JPY</td><td>JPY</td><td>%</td><td>JPYbn</td><td>JPYbn</td><td>FY1</td><td>FY2</td><td>FY3</td><td>FY1</td><td>FY1</td><td>FY1</td><td>FY1</td><td>FY1</td><td>FY2</td><td>FY3</td><td>1M</td><td>3M</td><td>6M</td><td>YTD</td></tr><tr><td>SMID</td><td>Business domain</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Namura Shipbuilding Co.</td><td>Shipbuilding</td><td>7014.T Buy</td><td>5,600</td><td>3,800</td><td>47%</td><td>264</td><td>6.8</td><td>12</td><td>11</td><td>8</td><td>1.7</td><td>1.6%</td><td>5</td><td>16%</td><td>6%</td><td>19%</td><td>30%</td><td>11%</td><td>-7%</td><td>-8%</td><td>8%</td></tr><tr><td>Mitsui E&amp;S Co.</td><td>Ship engine manufacturer</td><td>7003.T Buy</td><td>7,000</td><td>4,579</td><td>53%</td><td>462</td><td>29.5</td><td>13</td><td>12</td><td>10</td><td>1.8</td><td>1.5%</td><td>10</td><td>14%</td><td>12%</td><td>12%</td><td>23%</td><td>17%</td><td>-24%</td><td>-29%</td><td>-17%</td></tr><tr><td>Kyoritsu Maintenance</td><td>Business hotel operator</td><td>9616.T Buy</td><td>3,800</td><td>2,897</td><td>31%</td><td>263</td><td>2.6</td><td>14</td><td>12</td><td>11</td><td>1.6</td><td>1.4%</td><td>9</td><td>12%</td><td>5%</td><td>16%</td><td>12%</td><td>9%</td><td>13%</td><td>-2%</td><td>4%</td></tr><tr><td>Tokyo Keiki</td><td>Defense &amp; shipbuilding components manufacturer</td><td>7721.T Buy</td><td>8,800</td><td>6,360</td><td>38%</td><td>105</td><td>2.7</td><td>20</td><td>20</td><td>16</td><td>2.1</td><td>0.8%</td><td>14</td><td>11%</td><td>28%</td><td>2%</td><td>24%</td><td>23%</td><td>-16%</td><td>0%</td><td>20%</td></tr><tr><td>Kotobuki Spirits Co.</td><td>Premium gift sweets</td><td>2222.T Buy</td><td>2,650</td><td>2,609</td><td>2%</td><td>403</td><td>1.3</td><td>28</td><td>23</td><td>20</td><td>7.3</td><td>1.4%</td><td>16</td><td>28%</td><td>12%</td><td>20%</td><td>18%</td><td>9%</td><td>42%</td><td>43%</td><td>45%</td></tr><tr><td>Japan Airport Terminal Logistics/Airline/Shippers</td><td>Airport terminal operator</td><td>9706.T Sell</td><td>4,700</td><td>5,301</td><td>-11%</td><td>494</td><td>1.7</td><td>19</td><td>19</td><td>19</td><td>2.0</td><td>1.8%</td><td>7</td><td>11%</td><td>6%</td><td>2%</td><td>-1%</td><td>13%</td><td>-3%</td><td>16%</td><td>22%</td></tr><tr><td>ANA Holdings</td><td>Airline</td><td>9202.T Buy</td><td>3,500</td><td>3,016</td><td>16%</td><td>1,419</td><td>8.6</td><td>10</td><td>9</td><td>8</td><td>0.9</td><td>2.1%</td><td>3.3</td><td>8%</td><td>-10%</td><td>10%</td><td>6%</td><td>7%</td><td>4%</td><td>0%</td><td>4%</td></tr><tr><td>Japan Post Holdings</td><td>Postal business</td><td>6178.T Buy</td><td>2,550</td><td>2,320</td><td>10%</td><td>6,893</td><td>11.4</td><td>16</td><td>12</td><td>11</td><td>0.6</td><td>2.6%</td><td>N/A</td><td>2%</td><td>5%</td><td>25%</td><td>7%</td><td>5%</td><td>25%</td><td>32%</td><td>42%</td></tr><tr><td>Mitsui OSK Lines Ltd.</td><td>Shipper</td><td>9104.T Buy</td><td>6,500</td><td>5,324</td><td>22%</td><td>1,929</td><td>26.1</td><td>9</td><td>7</td><td>7</td><td>0.6</td><td>3.9%</td><td>10.6</td><td>7%</td><td>22%</td><td>20%</td><td>9%</td><td>-6%</td><td>-18%</td><td>11%</td><td>15%</td></tr><tr><td>Yamato Holdings</td><td>Parcel delivery</td><td>9064.T Neutral</td><td>1,900</td><td>1,944</td><td>-2%</td><td>616</td><td>2.4</td><td>26</td><td>17</td><td>16</td><td>1.1</td><td>2.4%</td><td>5.3</td><td>4%</td><td>31%</td><td>19%</td><td>5%</td><td>8%</td><td>6%</td><td>-7%</td><td>-11%</td></tr><tr><td>Japan Airlines Co.</td><td>Airline</td><td>9201.T Neutral</td><td>2,850</td><td>2,945</td><td>-3%</td><td>1,287</td><td>10.2</td><td>13</td><td>10</td><td>10</td><td>1.1</td><td>3.3%</td><td>3.6</td><td>9%</td><td>-25%</td><td>23%</td><td>4%</td><td>12%</td><td>14%</td><td>0%</td><td>3%</td></tr><tr><td>Nippon Yusen KK</td><td>Shipper</td><td>9101.T Neutral</td><td>5,300</td><td>5,286</td><td>0%</td><td>2,143</td><td>20.3</td><td>10</td><td>10</td><td>9</td><td>0.6</td><td>4.0%</td><td>8.1</td><td>7%</td><td>3%</td><td>18%</td><td>14%</td><td>-5%</td><td>-14%</td><td>2%</td><td>6%</td></tr><tr><td>Kawasaki Kisen Kaisha Ltd.</td><td>Shipper</td><td>9107.T Neutral</td><td>1,900</td><td>2,527</td><td>-25%</td><td>1,597</td><td>15.8</td><td>14</td><td>15</td><td>15</td><td>0.8</td><td>4.7%</td><td>11.5</td><td>6%</td><td>16%</td><td>7%</td><td>6%</td><td>-3%</td><td>-5%</td><td>13%</td><td>18%</td></tr><tr><td>SG Holdings</td><td>Parcel delivery</td><td>9143.T Sell</td><td>1,550</td><td>1,571</td><td>-1%</td><td>937</td><td>3.1</td><td>15</td><td>17</td><td>18</td><td>1.6</td><td>3.4%</td><td>6.6</td><td>11%</td><td>5%</td><td>-11%</td><td>-4%</td><td>8%</td><td>1%</td><td>9%</td><td>12%</td></tr></table>

Using July 10 close price  
Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - Nippon Yusen KK

Our 12-month target price of ¥5,300 is based on applying a target P/B of 0.65X to end-FY3/27E shareholders' equity per share. Key risks include forex fluctuations, fluctuations in the US consumption environment, changes in the dividend, and fluctuations in dividend income from subsidiary ONE.

## Price Target Risks and Methodology - Mitsui OSK Lines Ltd.

Our 12-month target price of ¥6,500 is based on applying a target P/B of 0.73X to end-FY3/27E shareholders' equity per share. Key risks include yen appreciation against the US dollar, a slowdown in the US consumption environment, lower-than-expected shareholder returns, and lower-than-expected dividend income from subsidiary ONE.

## Price Target Risks and Methodology - Kawasaki Kisen Kaisha Ltd.

Our 12-month target price of ¥1,900 is based on applying a target P/B of 0.65X to end-FY3/27E shareholders' equity per share. Key risks include forex fluctuations, fluctuations in the US consumption environment, changes to the dividend, and fluctuations in dividend income from subsidiary ONE.

## Price Target Risks and Methodology - Namura Shipbuilding Co.

Our 12-month target price of ¥5,600 is based on a target P/B of 2.6X applied to our end-FY3/30E BPS estimate, discounted back to FY3/27E using a cost of equity of 9.8%. Key risks include a sudden increase in production capacity in the shipbuilding industry, higher steel prices, production problems, and a decline in vessel prices.

## Price Target Risks and Methodology - Mitsui E&S Co.

Our 12-month target price is ¥7,000. Using a Sum of the Parts (SOTP) model, we apply target P/E multiples of 10X-19X to our net profit estimates for each segment and the respective reference years we use for them, and discount the sum back to FY3/27 using a cost of equity of 9.8%. We apply a P/E of 19X on FY3/31E for marine propulsion systems, 14X on FY3/30E for logistics systems, 14X on FY3/28E for new business development, and 10X on FY3/28E for peripheral services. Key risks include a sharp increase in input costs, deterioration in container transport demand, production problems, and a decline in prices.

## Price Target Risks and Methodology - Tokyo Keiki

Our 12-month target price is ¥8,800. The target price is derived applying a target P/E multiple of 23X on our FY3/31E EPS estimate and discounting the value back to FY3/27 using a cost of equity of 10%. Key risks include a deterioration in defense demand, a decline in shipping demand, and a decline in prices caused by competition and other relevant factors.

## Price Target Risks and Methodology - Japan Airlines Co.

We are Neutral rated on Japan Airlines with a 12-month target price of ¥2,850 based on a target FY3/27E EV/GCI multiple of 0.83X (-0.5 standard deviation from the past 10-year average). Key risks include upside/downside in passenger yield due to changes in passenger mix, larger-/smaller-than-expected earnings contributions from the non-airline and LCC businesses, changes in fixed costs, and swings in crude oil prices.

## Price Target Risks and Methodology - ANA Holdings

We are Buy rated on ANA Holdings with a 12-month target price of ¥3,500 based on a target FY3/27E EV/GCI multiple of 0.85X (+1.5 standard deviation from the past 10-year average). Key risks include higher crude oil prices, an increase in foreign currency-denominated costs due to ongoing yen weakness, and larger-than-expected fixed-cost increases.

## Price Target Risks and Methodology - Kotobuki Spirits

Our 12-month target price of ¥2,650 is based on a target 3/27E EV/EBITDA of 18X. A comparison with other Japanese food companies shows a strong correlation between EV/EBITDA and EBITDA margin. Given that the company has a higher profit margin than similar companies, we use a multiple that is higher than the sector average. Key downside risks include a temporary decline in travel demand due to natural disasters, margin deterioration due to rising raw material prices, delays in the expansion of international airports, and a slowdown in demand for inbound travel to Japan.

## Price Target Risks and Methodology - Kyoritsu Maintenance

Our 12-month target price is ¥3,800. Our target price is based on a target 3/27E EV/EBITDA of 11X. We consider this valuation appropriate in view of similar global hotel stocks and the company's historical range. A comparison with similar global hotel stocks shows a strong correlation between EV/EBITDA and EBITDA growth + EBITDA/total assets. Key downside risks include a temporary decline in travel demand due to natural disasters, tougher competition, a significant rise in domestic interest rates, and a slowdown in inbound demand.

## Price Target Risks and Methodology - Japan Airport Terminal

Our 12-month target price is ¥4,700. This is based on a target FY3/27E EV/EBITDA of 7.0X, which takes into account that the company's EBITDA/total assets and its EBITDA growth is in line with similar sectors. A comparison with global airport-related stocks shows a strong correlation between EV/EBITDA and EBITDA/total assets and EBITDA growth. Key upside risks include greater shareholder returns than we anticipate, easing of competition in the duty-free market, a larger-than-expected decrease in fixed costs, and an increase in duty-free demand owing to a weaker yen.

## Price Target Risks and Methodology - SG Holdings

We are Sell-rated on SG Holdings 

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
