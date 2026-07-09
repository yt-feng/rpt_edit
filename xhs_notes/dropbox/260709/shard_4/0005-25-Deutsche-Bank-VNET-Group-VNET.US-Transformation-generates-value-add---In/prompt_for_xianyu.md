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
Company
VNET Group

Rating Buy

Asia China

Telecommunications
Telecommunications

Reuters
VNET.OQ

Bloomberg
VNET US

Exchange
NSM

Ticker VNET

Date
7 July 2026

# Transformation generates value-add - Initiate at BUY

VNET also possesses substantial development optionality. The company has over 1GW of reserved wholesale capacity, primarily in Ulanqab, where construction costs are lower while economics remain attractive. Management is targeting further expansion across Inner Mongolia and key "East Data, West Compute" locations.

Funding appears manageable despite an aggressive RMB10-12bn annual capex program. The successful monetization of mature data centers at 13-14x EV/EBITDA through REIT listing provides an important source of capital and could support a self-reinforcing development model. Assets with a value of RMB6.4bn have been 70% sold down YTD through such channels.

## Transformation generating value

Strong bookings, a deep development pipeline, rising utilization, improving margins, and access to capital underpin forecasts for sustained strong growth through at least 2028. Management is targeting a 10GW build out. We assume only half of that build, but this still would represent a transformative increase in scale and earnings power.

Demand has accelerated as AI and cloud customers resume capacity expansion following improved chip availability. VNET has materially outperformed peers in bookings, securing 517MW YTD compared with GDS's 334MW, including a 510MW order from ByteDance. These projects are expected to be delivered between 2H26 and 1H28 and should drive a meaningful acceleration in revenue and EBITDA, particularly from 2027 onward as utilization ramps.

VNET is one of China's leading carrier-neutral data center operators, serving more than 7,000 enterprise customers through a combination of retail colocation, wholesale hyperscale data centers, cloud services, and enterprise networking. While historically driven by retail IDC services, the company is now undergoing a significant business mix shift toward becoming a hyperscale-focused data center developer benefiting from AI and cloud demand.

The recent acquisition of a major stake by a CATL affiliate removes a shareholder overhang and strengthens confidence in VNET's strategic direction. While potential operating synergies remain uncertain, CATL's involvement could

Price at 6 Jul 2026 (CNY) 7.81
Price target - 12mth (CNY) 12.50
52-week range (CNY) 14.03 - 6.97
Unavailable 23,616

## Initiation of Coverage

## Valuation & Risks

Peter Milliken, CFA
Research Analyst
+852-2203 6190

![](images/6e19965994182a7b82182dad6c095571db21768fdad815f6e7f113146da1da8f.jpg)

<table><tr><td>Performance (%)</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Absolute</td><td>-11.7</td><td>-3.6</td><td>0.8</td></tr><tr><td>HANG SENG INDEX</td><td>-5.4</td><td>-6.0</td><td>-1.3</td></tr><tr><td colspan="4">Source: DB</td></tr></table>

<table><tr><td>ROE (%)</td><td>-24.1</td></tr><tr><td>Net debt/equity (%)</td><td>97.1</td></tr><tr><td>Book value/share (CNY)</td><td>6.52</td></tr><tr><td>Price/book (x)</td><td>1.2</td></tr><tr><td>Net interest cover (x)</td><td>1.3</td></tr><tr><td>Operating profit margin (%)</td><td>8.7</td></tr><tr><td colspan="2">Source: DB</td></tr></table>

enhance financing access, energy-storage expertise, and support future overseas expansion.

Our estimates do not account for the potential value add from the company's development model, yet we still estimate the company's stock to be worth USD12.50 per share based on our DCF estimate, helped by its ramp up. We are also attracted to its wide discount to peer multiples. We therefore initiate with BUY. Key downside risks include: 1) With high growth in both industry supply and demand this is a risk of oversupply and/or demand slowdown, and 2) Execution and funding risks surrounding its plans for a rapid build out.

## Table Of Contents

Company highlights....4
From retail to wholesale....4
Diversified capital access to fund capex....9
Strategic investor change and synergies....10
Industry trends....12
Demand: cloud & AI capex fueling the up-cycle....12
Supply: market, pricing, and competition....13
Policy: national layout and controls....15
Valuation and risks....18
DCF....18
Multiples and comps....18
Key risks....22
Acknowledgment....23

# Company highlights

## From retail to wholesale

VNET is a leading carrier-neutral data center service provider in China. It operates one of the largest third-party IDC networks domestically, concentrated around Tier-1 cities, and serves a diversified base of over 7,000 enterprise customers.

The company provides managed hosting services (IDC), which includes colocation, inter-connectivity, and other value-added services, as well as cloud and business VPN services (non-IDC). We summarize its business segments below:

Wholesale IDC: \~40% of 1Q26 net revenues; providing large-scale, customized data center sites for cloud hyperscalers. Introduced in 2019, this business has become the company's key growth driver, with revenues increasing 58.1% YoY in 1Q26. Meanwhile for the first time, wholesale surpassed retail in terms of revenues, marking a significant milestone in the company's dual-core growth strategy.

Retail IDC: \~38% of 1Q26 net revenues; retail IDC offers standard cabinet colocation, either dedicated or shared, as well as inter-connectivity and a suite of VAS such as hybrid IT, bare metal services, and firewall management. This segment serves a diverse customer base, from blue-chip enterprises to SMEs across various industries. VNET has maintained a high retention rate, with core IDC business churn rate consistently below 1%.

Non-IDC business: \~22% of 1Q26 net revenues; this segment consists of cloud services and VPN services. Through a long-term strategic partnership in place since 2013, VNET is Microsoft's partner in mainland China for cloud offerings (Azure, Microsoft 365, Dynamics 365, and Power Platform), operating under a revenue-sharing model with monthly settlement and performance-based incentives. The VPN business is offered under brand DYXnet, covering enterprise-grade network solutions like MPLS and SD-WAN, across Asia.

Figure 1: VNET revenue and YoY growth  
![](images/322ece4d569776dfb25cf7d099ec68d20c9491a065fbd06805b29d8393097026.jpg)  
Source : Company data, DB

Figure 2: VNET revenue breakdown  
![](images/0121a1165e05cd7dbdac825a8b7d9c4b9d0404598fa958071be4400ce866a704.jpg)  
Source : Company data, DB

![](images/a531ca665eed392228e049e8733c9b8e27badbef5b9b7e22fc8ae2a37c26e389.jpg)

Strong bookings momentum to support revenue acceleration

We believe VNET is entering a notable revenue expansion phase, underpinned by the rapid scaling of wholesale IDC and the stabilization of retail IDC and Non-IDC businesses.

The order trend in the wholesale market has recovered since mid-2025 due to better chip availability, and VNET has so far displayed exceptional bookings momentum, outpacing its major IDC competitors. It secured 199MW new bookings in 2H25 and 517MW YTD, compared with 90MW and 334MW at GDS during the same period.

510MW of YTD bookings is from ByteDance for two data center campuses in the Greater Beijing Area. The delivery is scheduled in three phases: one-third in 2H26, one-third in 1H27, and the remainder in 2H27-1H28. Given ByteDance typically ramps up quite fast, we anticipate these capacities will quickly translate into revenue and EBITDA contributions for VNET.

With that said, the delivery pattern for the next 12 months is back-end loaded. The company guided for 2026 capacity delivery to add 450-500MW, of which over 80% should be in 2H based on our estimates. Coupled with some time for customer move-in and utilization to pick up, we think the revenue growth for 2027 should be better than 2026. Overall, we estimate revenue growth of 18.2% for 2026, in line with the guided range of 15.6%-18.6%, and 19.5%/19.6% for 2027/28.

![](images/30f68b665ac60af11e011b434060f5f6e6c0f56e4fd28e6cd2f9d4783a3a7c4d.jpg)

![](images/a0ad003b523252e04b21c086c9dc2b97891d00cfd635e0c13a79e6549b58c9f8.jpg)

Figure 6: Current capacity under construction & delivery pipeline

<table><tr><td>IDC Code</td><td>Tenure</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td></tr><tr><td>Yangtze River Delta</td><td></td><td>-</td><td>-</td><td>44</td><td>-</td><td>-</td></tr><tr><td>E-JS Campus 03B</td><td>Owned</td><td>-</td><td>-</td><td>44</td><td>-</td><td>-</td></tr><tr><td>Greater Beijing Area</td><td></td><td>18</td><td>66</td><td>140</td><td>124</td><td>142</td></tr><tr><td>N-HB Campus 02</td><td>Owned</td><td>-</td><td>-</td><td>-</td><td>59</td><td>-</td></tr><tr><td>N-HB Campus 03</td><td>Owned</td><td>18</td><td>4</td><td>-</td><td>-</td><td>-</td></tr><tr><td>N-HB04</td><td>Leased</td><td>-</td><td>-</td><td>7</td><td>-</td><td>14</td></tr><tr><td>N-OR Campus 01</td><td>Owned</td><td>-</td><td>9</td><td>-</td><td>-</td><td>-</td></tr><tr><td>N-OR Campus 02A</td><td>Owned</td><td>-</td><td>28</td><td>73</td><td>-</td><td>-</td></tr><tr><td>N-OR Campus 02B</td><td>Owned</td><td>-</td><td>-</td><td>-</td><td>65</td><td>-</td></tr><tr><td>N-OR Campus 03</td><td>Owned</td><td>-</td><td>25</td><td>60</td><td>-</td><td>128</td></tr><tr><td>Total</td><td></td><td>18</td><td>66</td><td>184</td><td>124</td><td>142</td></tr></table>

Source : Company data, DB estimates

Figure 7: Revenue & YoY growth forecasts  
![](images/ce1e1da82d0122b3dfbead17b2c16e530166a5517748e6e220d3a446059556c6.jpg)  
Source : Company data, DB estimates

Figure 8: Wholesale capacity & MRR forecasts  
![](images/cd40158491df6f43bec657d7e67e7daf4c62b5156c136a98759d44afb2779c7e.jpg)  
Source : Company data, DB estimates

## Land reserves as delivery backup

The company holds 1,056MW wholesale capacity reserves for future development as of 1Q26, mostly concentrated in Ulanqab, of which 697MW is for short-term and 359MW for long-term deployment. We highlight in the later section (Economics in the west) that the unit capex for data center construction in Ulanqab is \~10% lower than in Tier-1 cities, while development yield remains similar; and Ulanqab is favored by hyperscalers for lower utility and rental costs and attractive latency.

Management has confirmed that these reserves were either obtained before the "window guidance" came into practice or have already secured power quotas, which allows them to fast-track delivery by commencing construction immediately upon receiving client orders.

Looking ahead, the company plans to further increase its reserves in Inner Mongolia, the Yangtze River Delta, and two or three key nodes along the "East Data, West Compute" route, as part of its long-term expansion plan. Land acquisition accounts for only low-single-digit percentages of the unit capex, so funding the land bank is manageable.

![](images/c7cb77c28825c9516c1ff2d7901b7499c294edb87e4d977e9c5f5922085cd45e.jpg)  
Source : Company data, DB

![](images/b4527e8a42590acdde1a2ebd4153fab656950968dc66c2b78366d52275d30588.jpg)

Figure 11: VNET's wholesale data center portfolio

<table><tr><td colspan="2">(As of Mar 31, 2026)</td><td colspan="5">Wholesale capacity in service (MW)</td><td colspan="5">Wholesale capacity under construction (MW)</td></tr><tr><td>IDC Code</td><td>Tenure</td><td>In service</td><td>Utilized</td><td>Committed</td><td>Utilization rate</td><td>Commitment rate</td><td>Under construction</td><td>Pre-committed</td><td>Pre-commitment rate</td><td>Ready for service</td><td>Held for future</td></tr><tr><td>Yangtze River Delta</td><td></td><td>310</td><td>276</td><td>310</td><td>89.2%</td><td>100.0%</td><td>44</td><td>44</td><td>100.0%</td><td>/</td><td>37</td></tr><tr><td>as % of total</td><td></td><td>34.1%</td><td>40.2%</td><td>35.7%</td><td></td><td></td><td>8.5%</td><td>9.9%</td><td></td><td></td><td>3.5%</td></tr><tr><td>E-JS Campus 01 Phase 1</td><td>Owned</td><td>28</td><td>27</td><td>28</td><td>95.0%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS Campus 01 Phase 2</td><td>Owned</td><td>16</td><td>13</td><td>16</td><td>79.0%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS Campus 02A</td><td>Owned</td><td>25</td><td>24</td><td>25</td><td>95.7%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS Campus 02B</td><td>Owned</td><td>24</td><td>24</td><td>24</td><td>99.8%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS Campus 02C</td><td>Owned</td><td>26</td><td>26</td><td>26</td><td>98.1%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS Campus 02D</td><td>Owned</td><td>26</td><td>26</td><td>26</td><td>99.8%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS Campus 02E</td><td>Owned</td><td>64</td><td>56</td><td>64</td><td>87.7%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS Campus 03A</td><td>Owned</td><td>32</td><td>29</td><td>32</td><td>90.3%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS Campus 03B</td><td>Owned</td><td></td><td></td><td></td><td></td><td></td><td>44</td><td>44</td><td>100.0%</td><td>2H26</td><td></td></tr><tr><td>E-JS02A</td><td>Leased</td><td>13</td><td>13</td><td>13</td><td>96.8%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS02B</td><td>Leased</td><td>13</td><td>13</td><td>13</td><td>97.3%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS02C</td><td>Leased</td><td>13</td><td>12</td><td>13</td><td>95.0%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS03</td><td>Leased</td><td>15</td><td>15</td><td>15</td><td>97.4%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E-JS04</td><td>Leased</td><td>15</td><td>1</td><td>15</td><td>4.4%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Greater Beijing Area</td><td></td><td>598</td><td>411</td><td>559</td><td>68.7%</td><td>93.6%</td><td>472</td><td>399</td><td>84.4%</td><td>/</td><td>1,019</td></tr><tr><td>as % of total</td><td></td><td>65.9%</td><td>59.8%</td><td>64.3%</td><td></td><td></td><td>91.5%</td><td>90.1%</td><td></td><td></td><td>96.5%</td></tr><tr><td>BJ15</td><td>Owned</td><td>9</td><td>-</td><td>-</td><td>0.0%</td><td>0.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N-HB02 Phase 1</td><td>Owned</td><td>28</td><td>27</td><td>28</td><td>96.9%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N-HB Campus 01A</td><td>Owned</td><td>35</td><td>6</td><td>6</td><td>16.6%</td><td>16.6%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N-HB Campus 01B</td><td>Owned</td><td>36</td><td>32</td><td>36</td><td>88.7%</td><td>100.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N-HB Campus 02</td><td>Owned</td><td></td><td></td><td></td><td></td><td></td><td>59</td><td>-</td><td>0.0%</td><td>2H26</td><td></td></tr><tr><td>N-HB Campus 03</td><td>Owned</td><td>47</td><td>11</td><td>47</td><td>22.8%</td><td>100.0%</td><td>4</td><td>4</td><td>91.4%</td><td>1H26</td><td></td></tr><tr><td>N-OR Campus 01</td><td>Owned</td><td>152</td><td>129</td><td>152</td><td>84.7%</td><td>100.0%</td><td>9</td><td>9</td><td>100.0%</td><td>1H26</td><td></td></tr><tr><td>N-OR Campus 02A</td><td>Owned</td><td>117</td><td>53</td><td>117</td><td>45.5%</td><td>99.7%</td><td>101</td><td>101</td><td>100.0%</td><td>2H26</td><td></td></tr><tr><td>N-OR Campus 02B</td><td>Owned</td><td></td><td></td><td></td><td></td><td></td><td>65</td><td>65</td><td>100.0%</td><td>2H26</td><td></td></tr><tr><td>N-OR Campus 03</td><td>Owned</td><td></td><td></td><td></td><

[中间内容因长度限制已省略]

ted performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
