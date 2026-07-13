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
# Americas Energy & Transition

# Americas Power & Energy Transition: Baseload, Rising - Bernstein's Power Forecast until 2030

![](images/06e18e3d8284adaff6cf7b91531f06c9191ae8ae48df1eeeb2bef7fa3c88498c.jpg)  
Sunaina Ocalan  
.+1 917 344 8503

sunaina.ocalan@bernsteinsg.com

![](images/3d5c46194fe46eb455b39b0153ead1fae15a47dbd6623efde8974ebc715a79f5.jpg)

Anshika Bajpai

+1 917 344 8306

anshika.bajpai@bernsteinsg.com

![](images/02bdf547211bfe2a90eeb3c8aed434aa26b243b4e0859b93378e79ca1d3774b5.jpg)

Raphael Lee

+1 917 344 8355

raphael.lee@bernsteinsg.com

There's never been a more important time to have a good power demand forecast. After decades of no demand growth, electricity demand is growing in the US. It's not just artificial intelligence - it's reshoring, it's electrification, and normal GDP growth. At current demand, Independent Power Producers (IPPs) are growing and providing returns to shareholders. The macro debate isn't really whether power demand is going up or how much is power demand increasing anymore....I think everyone agrees it's going up (more on our forecast below). The debate is who captures the margin on supplying it.

We use an in-house built power supply and demand model to forecast power demand by sector - that we think is really easy to use and sensitize. We use the power supply portion to inform our view on our forecasts for the companies that will serve this demand. The supply model also helps provide a sanity check for the guidance from the companies we cover. We go into detail below.

Our proprietary power supply and demand model helps us forecast demand by sub-sector (residential, commercial, industrial, and transport) and deep-dive into key drivers of those sub-sectors below (for example, data centers for commercial power demand). We forecast supply by sub-sector and consider the role of intermittency of renewables in the forecast as well.

We expect power demand to rise by \~3% annually (CAGR) to 2030 with increased consumption occurring in all three major sectors - residential, commercial, and industrial. Since our initiation three weeks ago, we have gotten feedback that our power demand forecast might be conservative. We think 3% is a LOT when historical power demand has risen at only a 0.35% CAGR from 2000 to 2024. The range of other sources we’ve seen (IEA, EIA, Rystad) has power demand growing anywhere from 2 - 5% in the 2025-2030 time frame, so our model falls on the more conservative side of power demand.

We have updated our model through 1Q26 with actual monthly data from the EIA, keeping our forecasts the same.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td colspan="4">9 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>BE (Bloom Energy)</td><td>M</td><td>USD</td><td>257.02</td><td>276.00</td><td>823.3%</td><td>USD</td><td>0.82</td><td>2.30</td><td>4.27</td><td>312.0</td><td>111.6</td><td>60.2</td></tr><tr><td>LNG (Cheniere Energy)</td><td>O</td><td>USD</td><td>261.29</td><td>283.00</td><td>(11.5)%</td><td>USD</td><td>24.19</td><td>16.70</td><td>15.06</td><td>10.8</td><td>15.6</td><td>17.3</td></tr><tr><td>CQP (Cheniere Energy Partners)</td><td>M</td><td>USD</td><td>64.88</td><td>58.00</td><td>(5.2)%</td><td>USD</td><td>5.17</td><td>4.69</td><td>3.66</td><td>12.6</td><td>13.8</td><td>17.7</td></tr><tr><td>CEG (Constellation Energy)</td><td>O</td><td>USD</td><td>250.74</td><td>296.00</td><td>(40.7)%</td><td>USD</td><td>7.40</td><td>11.82</td><td>12.67</td><td>33.9</td><td>21.2</td><td>19.8</td></tr><tr><td>ENPH (Enphase Energy)</td><td>M</td><td>USD</td><td>44.89</td><td>56.00</td><td>(14.3)%</td><td>USD</td><td>1.29</td><td>0.58</td><td>1.22</td><td>34.9</td><td>76.8</td><td>36.9</td></tr><tr><td>FRVO (Fervo)</td><td>O</td><td>USD</td><td>27.35</td><td>47.00</td><td>NA</td><td>USD</td><td>(0.25)</td><td>(0.10)</td><td>(0.16)</td><td>(110.1)</td><td>(279.4)</td><td>(173.7)</td></tr><tr><td>FSLR (First Solar)</td><td>U</td><td>USD</td><td>228.50</td><td>217.00</td><td>18.1%</td><td>USD</td><td>14.21</td><td>17.70</td><td>22.65</td><td>16.1</td><td>12.9</td><td>10.1</td></tr><tr><td>GEV (GE Vernova)</td><td>O</td><td>USD</td><td>1,075.26</td><td>1,206.00</td><td>83.4%</td><td>USD</td><td>17.70</td><td>25.21</td><td>26.05</td><td>60.8</td><td>42.6</td><td>41.3</td></tr><tr><td>NEE (NextEra Energy)</td><td>O</td><td>USD</td><td>87.10</td><td>107.00</td><td>(3.7)%</td><td>USD</td><td>3.30</td><td>4.30</td><td>4.48</td><td>23.5</td><td>20.2</td><td>19.4</td></tr><tr><td>ORA (Ormat Technologies)</td><td>U</td><td>USD</td><td>110.37</td><td>115.00</td><td>4.1%</td><td>USD</td><td>2.02</td><td>2.26</td><td>2.48</td><td>54.7</td><td>48.8</td><td>44.4</td></tr><tr><td>TE (T1 Energy)</td><td>M</td><td>USD</td><td>7.26</td><td>9.00</td><td>367.1%</td><td>USD</td><td>(2.19)</td><td>(0.31)</td><td>(0.07)</td><td>(3.3)</td><td>(23.1)</td><td>(101.0)</td></tr><tr><td>VG (Venture Global)</td><td>M</td><td>USD</td><td>12.53</td><td>14.00</td><td>(48.3)%</td><td>USD</td><td>0.86</td><td>0.86</td><td>0.86</td><td>14.6</td><td>14.6</td><td>14.6</td></tr><tr><td>VST (Vistra Corporation)</td><td>O</td><td>USD</td><td>157.98</td><td>181.00</td><td>(39.4)%</td><td>USD</td><td>2.18</td><td>9.44</td><td>11.70</td><td>72.6</td><td>16.7</td><td>13.5</td></tr><tr><td>SPX</td><td></td><td></td><td>7,575.39</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
BE, VG estimate is Adjusted EPS; NEE estimate is Reported EPS Adjusted EPS; BE, NEE, VG valuation is Adjusted P/E (x); Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We are Outperform on GEV, FRVO, NEE, VST, CEG and LNG

We are Market-Perform on BE, ENPH, TE, VG, CQP

We are Underperform on FSLR and ORA

## DEMAND

Power demand in the U.S. has grown at a 1.2% CAGR since 2019, and 0.3% CAGR since 2010, significantly slower than overall GDP growth, as electricity use per kWh of GDP has declined by -3.7% in that time. However, we are now witnessing a once-in-a-generation increase in power demand. We bucket it into four categories: i) Residential demand from homes ii) Commercial demand from office spaces, warehouses, and other places of business (including data centers) iii) Industrial demand from manufacturing and iv) Transportation demand from the operation of public transport systems (which is a much smaller slice than the other three). We expect to see unprecedented growth in demand for power from all of these categories.

The biggest driver of demand is the addition of data centers in the US. Currently, 45% of global data centers are in the United States (more than 10X data centers in the US as compared to China!). By 2030, we expect \~50% of global data centers to be in the US. The proliferation of AI is meaningfully adding to the energy required to support data centers. Data center power demand currently makes up 6% of overall demand, growing to 10% of overall demand in 2030.

Additionally, the push to “reshore” manufacturing in an environment of increasing global geopolitical fragmentation will add incremental power demand from the industrial sector in the U.S.

Even before these more recent trends, the need to lower emissions by increasing electrification in various sectors of the economy (EVs, heat pumps, induction stoves) was set to increase the reliance on electricity.

## POWER FORECASTING

While there is probably no debate that power consumption is set to increase in the U.S., the extent of this growth is widely debated. The main tension here is that demand could materialize before supply can be connected. Power forecasting is driven by weather, seasonality, economic activity, and large technological changes. There is a short (months - 2 years), medium (3-5 years) and long term (6+ years) forecasting of power - the short term is still based on weather and seasonality and this is a mature science. The long term forecasting is based on large technology shifts and has been more scenario analysis than “forecasting”. Medium term power demand is driven by economic activity and industrial capacity additions - this used to be relatively predictable and slow moving - but now with AI and data centers, this medium term piece is difficult to predict. The current projection of increased load from data centers would have seemed ludicrous a decade ago, and interconnection requests still include a large share of speculative projects.

EXHIBIT 1: Various vintages of US Electricity Generation from the IEA show the difficulty in forecasting power

US Electricity Generation Historical Forecasts 2010-2050  
![](images/79137e2de5358dad1cd26c73031fe6ba8924928bdc57c2525304c6c1ad576f09.jpg)  
Source: IEA World Energy Outlook 2015-2025, Bernstein analysis

We pause to make the point that we may not be the best at forecasting power. Under the wise words of one of the best statisticians of all time, George Edward Pelham Box, “All models are wrong, some are useful”, we proceed with a sectoral approach to our forecasting.

We built an in-house model to put a helpful framing around the potential load growth from macro trends in data center development, re-shoring of manufacturing, EV adoption, and broader electrification. The model is easy to sensitize to various inputs. We outline our base case assumptions and inputs below, and elaborate on the methodology we used.

## EXHIBIT 2: Our in-house model allows us to sensitize demand and supply on various fronts

## DEMAND

Forecasts future monthly demand by estimating major growth drivers, and using base growth at 2010-2019 CAGR:

■ Residential: EV sales, heat pump sales

■ Commercial: data center and AI power demand

\- Industrial: Reshoring of manufacturing gross domestic output

\- Transportation flat

Adds 8% transmission losses based on historical data from EIA

## SUPPLY

Supply (plus imports) available to meet demand plus transmission losses. Imports negligible

By fuel source:

■ We sum monthly generation capacity adds of late-stage projects

\- We add monthly additions to current capacity to get future monthly capacity by generation, assuming a capacity factor

\- We gross up solar capacity 3 years out to account for continuous underestimation

■ Manually add nuclear restarts

Delta between demand and supply met by gas

## Inputs:

## INPUTS

\- Generation fleet

\- Outages

\- Renewable profiles

\- Import/ Exports

\- Transmission losses

■ Historical data from EIA

## Sources:

## SOURCES

■ Edison Electric Institute

\- Department of Energy

\- AHRI – Heat pump sales

■ International Energy Institute

■ Federal Reserve Bank

Bloomberg

Built in excel with scenario modeling approach

## DRIVERS OF FUTURE DEMAND GROWTH

## AI/ Data centers and commercial demand

We estimated the U.S. has \~45GW of installed data center capacity out of a total global installed base of \~100GW. These data centers currently consume \~260TWh of electricity. In addition to running compute, these facilities also use power for cooling, lighting and other operations. Therefore, 1GW of data center capacity has to be grossed up to account for total power consumption. Current estimates range from 10-50% gross up. This implies a range of “power use efficiency” or PUE of 1.1x to 1.5x for each GW of capacity. Data centers do not run at 100% of the time either with utilization depending on a variety of factors including type of workload (training vs. inference).

We use estimates of future U.S. data center capacity built by our Communications Infrastructure team, and estimate 40GW of capacity growth from 2025-30. In order to account for potential power use efficiency gains we assume a base case PUE of 1.25x and assume a capacity utilization of \~50%. These assumptions yield a power demand add of \~230TWh by 2030 from data centers.

EXHIBIT 3: At 40GW of data center capacity growth and 1.25x PUE, we see power demand from data centers growing \~230TWh by the end of the decade

<table><tr><td>Metric</td><td>Value</td></tr><tr><td>2025 U.S. data center capacity</td><td>46 GW</td></tr><tr><td>2030 U.S. data center capacity</td><td>86 GW</td></tr><tr><td>Total capacity added</td><td>40 GW</td></tr><tr><td>PUE</td><td>1.25x</td></tr><tr><td>Utilization</td><td>52%</td></tr><tr><td>Incremental power demand</td><td>26 GW</td></tr><tr><td>TWh added</td><td>228 TWh</td></tr></table>

Source: Bernstein Analysis and Estimates

In the bear case, if PUE improves to only 1.1x, demand growth would be closer to \~200TWh. This could also reflect lower power use for the actual compute (i.e. lower overall capacity demand or utilization). In the bull case for power, at a punitive 1.5x PUE, power demand would grow by \~270TWh in our model.

EXHIBIT 4: Our scenarios for potential data center power demand range from +200TWh to +270TWh reflecting a PUE range of 1.1x to 1.5x  
U.S. data center electricity demand (TWh)  
![](images/d1b967ac4ce57c9c984fddff915c4cbd866ad32f5630a0d004dc72822b963300.jpg)  
Source: IEA, Bernstein analysis and estimates

We consider this demand growth to be incremental. Commercial demand for power grew at a 0.7% CAGR from 2010-2019. We continue to grow “base” commercial demand at this CAGR. We do not use the last 5 years that have a higher CAGR as we believe this might already include the effect of recent data center demand adds (as well as noise from temporary COVID-19 related moves).

We see commercial demand overall growing at a 3.6% CAGR over the next five years, from \~1,500TWh today to \~1,800TWh in 2030.

## Manufacturing "re-shoring" and industrial demand

Prior to the rapid globalization of supply chains, the share of domestic manufacturing out of total supply was much higher than it is today. Our machinery team estimated this share was \~84% in the late 90s and has fallen to \~72% today. There has been a recent push to move some manufacturing back on-shore to reduce reliance on imports and exposure to global supply chain risks. While it would be difficult to reach a pre-globalization share of domestic manufacturing in a short time frame, we believe there is no debate on the US wanting to reinvigorate domestic manufacturing. We believe that will drive meaningful industrial power demand growth to the end of the decade.

U.S. gross domestic output (GDO) stands at \~\$7Tr. If we assume GDO grows roughly with GDP growth expectations in the low single digits, and that domestic manufacturing grows share modestly to 75% by 2030, electricity demand from the U.S. industrial sector would grow by \~100TWh.

This reflects an overall industrial demand growth CAGR of $\sim 2\%$ over the next 5 years (vs. $< 1\%$ over the prior 5 years) from $\sim 1,000\mathrm{TWh}$ today to $\sim 1,100\mathrm{TWh}$ in 2030.

EXHIBIT 5: We believe growth in the share of domestic manufacturing could add \~100TWh of industrial power demand by 2030 reflecting a \~2% CAGR

<table><tr><td>Reshoring</td><td>Value</td></tr><tr><td>Est. 2025 manufacturing Gross Domestic Output (GDO)</td><td>$7,321bn</td></tr><tr><td>2030 Gross Domestic Output at 2%/yr growth</td><td>$8,083bn</td></tr><tr><td>Assumed 2030 domestic manufacturing capacity</td><td>75%</td></tr><tr><td>Electric intensity (GWh/ $GDO)</td><td>142</td></tr><tr><td>2030 industrial power demand</td><td>863 TWh</td></tr><tr><td>2025 implied manufacturing power demand</td><td>761 TWh</td></tr><tr><td>Manufacturing TWh added by 2030</td><td>102 TWh</td></tr></table>

Source: FRED, Bernstein Analysis

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
