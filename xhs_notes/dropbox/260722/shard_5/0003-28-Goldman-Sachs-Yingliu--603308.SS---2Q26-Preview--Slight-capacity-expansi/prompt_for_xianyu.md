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
# Yingliu (603308.SS): 2Q26 Preview: Slight capacity expansion in June with more to come in 2H26, with long-term agreements extended; Buy

We revise our 2026-30E EPS forecasts down by c.10-11%, mainly reflecting an updated revenue ramp based on the company's latest capacity-expansion schedule, as well as more limited pricing actions as management prioritizes volume growth and strategic market-share gains.

Previewing 2Q26 earnings, we forecast 2Q26 revenue of Rmb916mn, up 27% yoy. With gross margin recovering modestly to 34.5% from 33.7% in 1Q26, we expect net profit of Rmb118mn, up 23% yoy.

In our view, the key market debate has shifted away from Yingliu's company-specific execution toward the sustainability of global gas-turbine order growth. We maintain our Buy rating following the recent correction. The stock is trading at 38.6x 12-m forward P/E, with approximately $20\%$ downside to its historical trough multiple of 30x but materially greater upside with visibility extending to 2028-29 and beyond (our target multiple implies $88\%$ upside), should hyperscalers provide better visibility on data center capex. Remain Buy with new 12-m TP at Rmb82.4.

## 2Q26 and 2H26 preview: Additional capacity to ramp in 2H26

We expect Yingliu's two-engine business (gas turbine and aero-engine) to generate approximately Rmb420mn of production value in 2Q26, based on monthly output of Rmb130-140mn in April and May and approximately Rmb150mn in June. Assuming the traditional business remains broadly stable, we forecast total revenue of Rmb916mn, Rmb981mn and Rmb1,033mn in 2Q26, 3Q26 and 4Q26, respectively, representing yoy growth of $27\%$ , $33\%$ and $30\%$ , which is based on the following capacity expansion plan.

Capacity should continue to expand in 2H26 as three new pieces of equipment enter production. The first machine arrived on May 20 and is expected to complete commissioning in August. The second has arrived and is expected to commence production in September, while the third is scheduled to arrive on July 29 and begin production in October. Each machine could add approximately Rmb10mn of monthly production value after reaching normal utilization. Assuming the ramp proceeds broadly on schedule, quarterly two-engine production value could increase to approximately Rmb450-480mn in 3Q26E and Rmb480-530mn in 4Q26E vs c.Rmb400mn in 1Q26 and Rmb420 in 2Q26E.

Zhou Li
+86(21)2401-8648 |
zhou.li@goldmansachs.cn
GS (China) Securities
Company Limited

Jacqueline Du
+852-2978-1783 |
jacqueline.du@gs.com
GS (Asia) L.L.C.

Hao Chen
+86(21)2401-8812 |
hao.z.chen@goldmansachs.cn
GS (China) Securities
Company Limited

2Q26 margin preview: Raw-material pressure easing, but pricing remains stable The company has partially passed higher raw-material costs through to customers, supported by contractual adjustment mechanisms in certain long-term agreements. However, management does not intend to pursue aggressive price increases with key strategic customers. Given the importance of long-term qualification, market-share gains and deeper customer relationships, Yingliu is prioritizing volume growth and supplier positioning over maximizing near-term pricing.

Nickel, cobalt and tungsten account for approximately 57%, 14% and LSD%, respectively, of raw-material costs within COGS. Their prices increased by approximately 19%, 67% and 322% yoy, while changing by +4%, 0% and -1% qoq.

As sequential raw-material pressure begins to ease and part of the cost increase is passed through, we expect gross margin to recover to 34.5% in 2Q26 from 33.7% in 1Q26. We forecast net profit of Rmb118mn, up 23% yoy. Margin improvement should remain gradual, as the company continues to prioritize strategic customer relationships and volume expansion over aggressive pricing.

## Order momentum remains strong, with backlog continuing to expand

Yingliu's order momentum remained robust in 2Q26. Backlog increased slightly from approximately Rmb2.1bn at the end of 1Q26 to more than Rmb2.2bn currently, net of deliveries of roughly Rmb420mn of two-engine products in the quarter. This suggests that new order intake of roughly Rmb500mn in 2Q26, or ytd total of 1.34bn (45% run rate of previous full-year target of Rmb3bn, while the new target of Rmb4bn looks aggressive at this point). However, management indicated that they generally record firm orders only when they can commit to delivery within 52 weeks; longer-dated indications and framework agreements are not included in reported backlog.

2Q26 orders were roughly Rmb500mn, including Rmb100-200mn from Ansaldo (ytd Rmb450mn orders signed), rolling orders from Baker Hughes, new order with Shanghai Electric, prototyping orders with Doosan, and orders from Safran.

## Long-term agreements with Baker Hughes renewed and new orders signed

Long-term agreements also extended with Baker Hughes: Yingliu recently renewed its long-term agreement with Baker Hughes through 2031. Compared with the previous agreement signed in June 2023, the renewed framework covers a broader product range and materially higher committed volumes. Under the latest agreement, expected monthly volumes include: c.14 sets per month across eight LT16 gas-turbine models; four sets per month across five MS5002E product categories; one set for the MS5001 and LM9000 platforms each.

This implies total annual deliveries of more than 200 sets once the agreement reaches its targeted run rate. The higher volumes are expected to begin converting into firm orders from 2027 and beyond for delivery in 2028 and beyond. Additionally on July 10, the company just certified for Frame5Max products, with a content value of several million RMB per unit, at 50% market share, and 4 sets of orders per month. Lastly, they are also starting to conduct R&D for LT12 products.

The Baker Hughes agreement also includes a raw-material adjustment mechanism. If raw-material prices move by more than $10\%$ , product prices can be renegotiated, reducing Yingliu's exposure to significant alloy-price volatility.

## Siemens Energy cooperation is moving from validation toward mass production

Yingliu's cooperation with Siemens Energy continues to deepen across both large and medium-sized gas-turbine platforms. The company expects all relevant 4000F prototypes to enter mass production during 2026. It is also developing components for the 8000H platform and progressing projects for the SGT-450, SGT-700 and SGT-800 medium-sized gas turbines. Beyond individual component programs, Yingliu and Siemens Energy are establishing a joint laboratory in Hainan.

## Key debate: Has gas-turbine order growth peaked?

Although we continue to expect gas-turbine supply to remain tight beyond 2028-29, consistent with the current delivery lead times of major turbine OEMs, the market has increasingly shifted its focus toward the outlook for new order growth and whether the cycle has peaked in 2026.

We agree that order growth is unlikely to remain at the same exceptionally high level in 2027. However, we still expect order level to remain robust, supported by both the replacement cycle for turbines installed in the early 2000s and incremental demand from data centers. At its June 29 pre-close call, Siemens Energy indicated that, based on current visibility, it expects the global gas-turbine market to sustain annual demand of approximately 110-120GW over the coming years.

Near term, the key uncertainty is the limited visibility on hyperscaler capex beyond 2026. Until hyperscalers provide clearer spending plans for 2027 and beyond, we think investors may continue to treat Yingliu as a cyclical stock and value it closer to pre-AI multiples, which has contributed to the recent correction. The stock is already trading at 38.6x P/E, below its historical average of around 40x since 2018, with approximately 20% downside to its historical trough valuation of around 30x P/E.

However, once hyperscaler capex provides greater clarity on the durability of data-center power demand, we believe order visibility could extend again into 2028-29 and potentially beyond, supporting a more favorable rerating. At current levels, we continue to see the risk-reward as skewed to the upside.

Exhibit 1: Yingliu is trading at 38.6x P/E, slightly below historical average of 40x since 2018  
![](images/43759d1da1279f7f8d590dc6f961151266e9b03e67b0319386662279b68294ae.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: Yingliu is trading at 40.5x 2026E P/E, slightly below peers' median of 45.6x

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">PCY</td><td rowspan="2">Last closing price (PCY)</td><td rowspan="2">12m-Target price</td><td rowspan="2">Upside/ (downside)</td><td rowspan="2">Rating</td><td rowspan="2">Mkt Cap (US$bn)</td><td colspan="4">P/E</td><td colspan="4">P/B</td><td colspan="4">EV/EBITDA</td><td colspan="4">ROE</td></tr><tr><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="24">Global peers</td></tr><tr><td>Yingliu</td><td>603308.SS</td><td>CNY</td><td>43.90</td><td>82.4</td><td>88%</td><td>Buy</td><td>4.3</td><td>70.1x</td><td>40.5x</td><td>28.2x</td><td>18.6x</td><td>5.5x</td><td>4.9x</td><td>4.4x</td><td>3.7x</td><td>43.5x</td><td>32.1x</td><td>24.4x</td><td>16.1x</td><td>8%</td><td>13%</td><td>16%</td><td>21%</td></tr><tr><td>Howmet</td><td>HWM</td><td>USD</td><td>271.98</td><td>303</td><td>11%</td><td>Buy</td><td>109.1</td><td>72.1x</td><td>53.9x</td><td>45.3x</td><td>39.7x</td><td>20.5x</td><td>17.0x</td><td>15.0x</td><td>13.3x</td><td>29.8x</td><td>35.1x</td><td>31.0x</td><td>27.4x</td><td>30%</td><td>36%</td><td>35%</td><td>36%</td></tr><tr><td>MHI</td><td>7011.T</td><td>JPY</td><td>3681.00</td><td>6,000</td><td>63%</td><td>Buy</td><td>76.2</td><td>50.4x</td><td>37.2x</td><td>32.0x</td><td>24.3x</td><td>5.3x</td><td>4.0x</td><td>3.7x</td><td>3.4x</td><td>12.3x</td><td>22.2x</td><td>16.6x</td><td>13.0x</td><td>10%</td><td>12%</td><td>11%</td><td>14%</td></tr><tr><td>Siemens Energy</td><td>ENR1n.DE</td><td>EUR</td><td>152.64</td><td>212</td><td>39%</td><td>Buy*</td><td>151.2</td><td>98.6x</td><td>34.9x</td><td>26.0x</td><td>19.3x</td><td>12.4x</td><td>12.3x</td><td>11.9x</td><td>10.6x</td><td>14.8x</td><td>18.5x</td><td>13.9x</td><td>10.5x</td><td>13%</td><td>35%</td><td>46%</td><td>58%</td></tr><tr><td>GE Vernova</td><td>GEV</td><td>USD</td><td>1079.18</td><td>1,289</td><td>19%</td><td>Buy</td><td>295.7</td><td>60.6x</td><td>73.7x</td><td>41.9x</td><td>31.7x</td><td>24.1x</td><td>21.1x</td><td>19.5x</td><td>19.5x</td><td>39.4x</td><td>43.6x</td><td>27.1x</td><td>20.2x</td><td>43%</td><td>31%</td><td>47%</td><td>61%</td></tr><tr><td>Median</td><td></td><td></td><td></td><td></td><td>29%</td><td></td><td></td><td>66.4x</td><td>45.6x</td><td>37.0x</td><td>28.0x</td><td>16.5x</td><td>14.7x</td><td>13.5x</td><td>12.0x</td><td>22.3x</td><td>28.6x</td><td>21.8x</td><td>16.6x</td><td>22%</td><td>33%</td><td>41%</td><td>47%</td></tr></table>

\* refers to stocks on Regional Conviction List. Pricing is as of closing price on July 20.  
Source: Company data, GS Global Investment Research

TP, EPS revision: We revise down our 2026-30E EPS by c.10-11%. Accordingly, our 12-m TP moves lower to Rmb82.4 (from previously Rmb92.0), still based on 2030E P/E of 30X, discounted to 2027E at a COE of 10.0%.

## Investment thesis, valuation methodology and risks

## Yingliu (603308.SS, Buy)

Yingliu is a leading domestic high-end cast component supplier with <1% global share, leaving a long runway for growth. We expect U.S. AIDC to source up to \~60% of power from gas turbines, while global OEMs (Siemens Energy, GE Vernova, MHI) face severe capacity constraints, with turbine blades a key bottleneck due to stringent metallurgical requirements and supply concentration among Western suppliers (e.g., PCC, Howmet), who prioritize aerospace and face labor shortages. Yingliu is well positioned to capture demand spillover given available capacity, lower ASPs, comparable quality, and strong R&D and customer relationships, reinforced by expanded product development for Siemens Energy and long-term contracts with Baker Hughes, Ansaldo, and GE Aerospace. While still a complementary supplier relative to Western incumbents with single-digit global share by 2030E, improving product mix, scale, and asset turnover should drive GPM, NPM, and ROE expansion through the cycle. We forecast 28%/41% total sales/earnings CAGR in 2026E-30E and derive a 12m TP of Rmb82.4. We are Buy rated.

Valuation methodology: Our 12m target price of Rmb82.4 is based on 2030E P/E of 30x discounted back to 2027E at 10% CoE.

Key downside risks: (1) Capacity ramp-up comes in below expectations due to failure to improve yield rate or recruit skilled technicians; (2) Order intake growth below our expectations, potentially due to the long cycle to develop new SKU; (3) AIDC demand weakens with hyperscalers canceling orders for gas turbine manufacturers.

Exhibit 3: Yingliu earnings revision summary

<table><tr><td>Yingliu</td><td></td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenue (new)</td><td>Rmb mn</td><td>3,818</td><td>5,277</td><td>6,946</td><td>8,434</td><td>10,117</td></tr><tr><td>Previous</td><td>Rmb mn</td><td>4,063</td><td>5,307</td><td>7,051</td><td>8,579</td><td>10,382</td></tr><tr><td>vs. Previous</td><td>%</td><td>-6.0%</td><td>-0.6%</td><td>-1.5%</td><td>-1.7%</td><td>-2.5%</td></tr><tr><td>EBIT (new)</td><td>Rmb mn</td><td>586</td><td>926</td><td>1,418</td><td>1,819</td><td>2,340</td></tr><tr><td>Previous</td><td>Rmb mn</td><td>652</td><td>1,064</td><td>1,617</td><td>2,054</td><td>2,655</td></tr><tr><td>vs. Previous</td><td>%</td><td>-10.1%</td><td>-13.0%</td><td>-12.3%</td><td>-11.4%</td><td>-11.9%</td></tr><tr><td>Net Income (new)</td><td>Rmb mn</td><td>627</td><td>998</td><td>1,523</td><td>1,944</td><td>2,484</td></tr><tr><td>Previous</td><td>Rmb mn</td><td>697</td><td>1,119</td><td>1,704</td><td>2,159</td><td>2,771</td></tr><tr><td>vs. Previous</td><td>%</td><td>-10.1%</td><td>-10.8%</td><td>-10.6%</td><td>-9.9%</td><td>-10.4%</td></tr></table>

Source: Company data, GS Global Investment Research

<table><tr><td>603308.SS</td><td>12m Price Target: Rmb82.4</td><td colspan="2">Price: Rmb44.34</td><td colspan="2">Upside: 85.8%</td></tr><tr><td rowspan="2">Buy</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: Rmb30.1bn / $4.4bn</td><td>Revenue (Rmb mn) New</td><td>2,918.8</td><td>3,818.4</td><td>5,276.6</td><td>6,945.7</td></tr><tr><td>Enterprise value: Rmb34.6bn / $5.1bn</td><td>Revenue (Rmb mn) Old</td><td>2,918.8</td><td>4,063.4</td><td>5,307.1</td><td>7,051.3</td></tr><tr><td>3m ADTV :Rmb1.6bn/ $228.9mn</td><td>EBITDA (Rmb mn)</td><td>698.6</td><td>982.8</td><td>1,379.7</td><td>1,913.4</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>0.51</td><td>0.92</td><td>1.47</td><td>2.24</td></tr><tr><td rowspan="2">China Industrial Tech &amp; Machinery</td><td>EPS (Rmb) Old</td><td>0.51</td><td>1.03</td><td>1.65</td><td>2.51</td></tr><tr><td>P/E (X)</td><td>51.9</td><td>48.0</td><td>30.2</td><td>19.8</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/B (X)</td><td>3.3</td><td>5.1</td><td>4.5</td><td>3.8</td></tr><tr><td rowspan="4">Leases incl. in net debt &amp; EV?: Yes</td><td>Dividend yield (%)</td><td>0.6</td><td>0.4</td><td>0.7</td><td>1.0</td></tr><tr><td>CROCI (%)</td><td>9.2</td><td>10.0</td><td>12.5</td><td>15.0</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS 

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
