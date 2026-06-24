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
22 Jun 2026 12:47:05 ET | 12 pages

## China Aluminum

## Addressing Investor Concerns; Reiterate Buy on Hongqiao and Chalco

## CITI'S TAKE

According to mysteel, China operating aluminum capacity is 45.3mntpa on $22^{\text{nd}}$ Jun 2026 and total aluminum output is expected to reach 45.4mnt in 2026E considering possible slight overproduction. The NBS's monthly aluminum output data is more spiky than SMM and Mysteel data hence less used by industry participants. Citi commodity team remains bullish on aluminum and expects average aluminum price at \~US\$4,000/t in 3Q26E. We see aluminum price and margins will stay higher for longer and the strong free cash flows will continue to support dividends and buybacks for equities. We see the weakness as an opportunity to buy shares. Maintain Buy on both Hongqiao and Chalco with attractive valuation.

China capacity – According to mysteel, China operating aluminum capacity is 45.3mntpa on 22 $^{nd}$ Jun 2026 and total aluminum output is expected to reach 45.4mnt in 2026E considering possible slight overproduction. Investors' concerns of 48mntpa capacity was based on annualized China aluminum output in Apr 2026 reported by NBS. However, mysteel expects aluminum output data reported by NBS was more fluctuated and could be misleading as the annualized China aluminum output in May 2026 reported by NBS decreased to 45.8mntpa. In addition, the monthly operating capacity calculated from NBS's output data since Mar 2025 has been fluctuated and even decreased MoM at some months, which is different from industry's view that aluminum utilization ratio has kept increasing with hiking profitability. We expect there is no change in the capacity cap policy in China (see our note).

Overseas aluminum inventory and capacity – Mysteel expects the aluminum inventory in the Middle East that could be transported out after the reopening of Strait of Hormuz is less than 400kt. For Indonesia capacity addition, mysteel expects power supply is a key focus in addition to the construction of aluminum capacity. It takes time for the construction of power units and the ramp-up of aluminum capacity. Mysteel expects total overseas aluminum capacity addition at 1.85mntpa in 2026E, contributing 1.2mnt aluminum output, while total overseas aluminum output will decrease 1.6mnt YoY after considering the impact from capacity suspension in the Middle East and slight resumption in Europe. In 2027E, mysteel expects overseas aluminum output to increase \~3mnt YoY after the production resumption in the Middle East and some overseas capacity addition.

Remain bullish on aluminum price – Citi commodity team remains bullish on aluminum and expects average aluminum price at \~US\$4,000/t in 3Q26E as Strait of Hormuz reopening stabilizes demand faster than it restores supply. Citi commodity team expects the aluminum market as being in a genuine deficit phase of \~2Mt primary deficit in 2026E and \~270kt primary deficit in 2027E. See more from our note here.

Jack Shang, CFA $^{AC}$ +852-2501-2441
jack.shang@citi.com

Anna Wang
+852-2501-2739
anna.d.wang@citi.com

Jimmy Feng
+852-2501-7588
jimmy.feng@citi.com

Cynthia Wu

+852-2868-7813

cynthia.d.wu@citi.com

Reiterate Buy on Hongqiao and Chalco – We see aluminum price and margins to stay higher for longer and the strong free cash flows to continue to support dividends and buybacks for equities. We see the weakness as an enhanced opportunity to buy shares. Maintain Buy on both Hongqiao and Chalco with attractive valuation.

Figure 1. Aluminum names 26E P/E sensitivity to aluminum price

<table><tr><td rowspan="2">Change in Aluminum price</td><td colspan="2">Change in 2026E net profit</td><td rowspan="2">Aluminum price (Rmb/t)</td><td colspan="2">2026E Net Profit (Rmb mn)</td><td rowspan="2">Aluminum price (Rmb/t)</td><td colspan="3">2026E P/E</td></tr><tr><td>Chalco</td><td>Hongqiao</td><td>Chalco</td><td>Hongqiao</td><td>Chalco-A</td><td>Chalco-H</td><td>Hongqiao</td></tr><tr><td>-20%</td><td>-71%</td><td>-55%</td><td>18,581</td><td>5,950</td><td>14,222</td><td>18,581</td><td>28.4</td><td>21.5</td><td>13.7</td></tr><tr><td>-15%</td><td>-53%</td><td>-41%</td><td>19,742</td><td>9,513</td><td>18,609</td><td>19,742</td><td>17.8</td><td>13.5</td><td>10.4</td></tr><tr><td>-10%</td><td>-35%</td><td>-28%</td><td>20,903</td><td>13,076</td><td>22,995</td><td>20,903</td><td>12.9</td><td>9.8</td><td>8.5</td></tr><tr><td>-5%</td><td>-18%</td><td>-14%</td><td>22,064</td><td>16,639</td><td>27,381</td><td>22,064</td><td>10.2</td><td>7.7</td><td>7.1</td></tr><tr><td>0%</td><td>0%</td><td>0%</td><td>23,226</td><td>20,203</td><td>31,767</td><td>23,226</td><td>8.4</td><td>6.3</td><td>6.1</td></tr><tr><td>5%</td><td>18%</td><td>14%</td><td>24,387</td><td>23,766</td><td>36,153</td><td>24,387</td><td>7.1</td><td>5.4</td><td>5.4</td></tr><tr><td>10%</td><td>35%</td><td>28%</td><td>25,548</td><td>27,329</td><td>40,539</td><td>25,548</td><td>6.2</td><td>4.7</td><td>4.8</td></tr><tr><td>15%</td><td>53%</td><td>41%</td><td>26,710</td><td>30,892</td><td>44,925</td><td>26,710</td><td>5.5</td><td>4.1</td><td>4.3</td></tr><tr><td>20%</td><td>71%</td><td>55%</td><td>27,871</td><td>34,456</td><td>49,311</td><td>27,871</td><td>4.9</td><td>3.7</td><td>3.9</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: Based on alumina price at Rmb2,843/t in 2026E and as of market close on 22nd Jun

Source: Citi

Figure 2. Aluminum names 26E EV/EBITDA sensitivity to aluminum price

<table><tr><td rowspan="2">Aluminum price (Rmb/t)</td><td colspan="2">2026E EBITDA (Rmb mn)</td></tr><tr><td>Chalco</td><td>Hongqiao</td></tr><tr><td>18,581</td><td>26,257</td><td>32,695</td></tr><tr><td>19,742</td><td>34,034</td><td>39,514</td></tr><tr><td>20,903</td><td>41,812</td><td>46,333</td></tr><tr><td>22,064</td><td>49,589</td><td>53,152</td></tr><tr><td>23,226</td><td>57,366</td><td>59,971</td></tr><tr><td>24,387</td><td>65,143</td><td>66,790</td></tr><tr><td>25,548</td><td>72,921</td><td>73,610</td></tr><tr><td>26,710</td><td>80,698</td><td>80,429</td></tr><tr><td>27,871</td><td>88,475</td><td>87,248</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

<table><tr><td rowspan="2">Aluminum price (Rmb/t)</td><td colspan="3">2026E EV/EBITDA</td></tr><tr><td>Chalco-A</td><td>Chalco-H</td><td>Hongqiao</td></tr><tr><td>18,581</td><td>9.0</td><td>7.5</td><td>6.6</td></tr><tr><td>19,742</td><td>7.0</td><td>5.8</td><td>5.4</td></tr><tr><td>20,903</td><td>5.7</td><td>4.7</td><td>4.6</td></tr><tr><td>22,064</td><td>4.8</td><td>3.9</td><td>4.0</td></tr><tr><td>23,226</td><td>4.1</td><td>3.4</td><td>3.6</td></tr><tr><td>24,387</td><td>3.6</td><td>3.0</td><td>3.2</td></tr><tr><td>25,548</td><td>3.2</td><td>2.7</td><td>2.9</td></tr><tr><td>26,710</td><td>2.9</td><td>2.4</td><td>2.7</td></tr><tr><td>27,871</td><td>2.7</td><td>2.2</td><td>2.5</td></tr></table>

Note: Based on alumina price at Rmb2,843/t in 2026E and as of market close on 22nd Jun

Source: Citi

## Aluminum Corporation of China

(601600.SS; Rmb9.86; 1; 22 Jun 26; 15:00)

## Valuation

Our target price for the Chalco A-share of Rmb17.24/sh is based on 3.28x 2026E PB, set at 2SD above the historical average of 1.86x as we expect stronger-than-historical-average 2026-27E ROEs, benefitting from higher aluminum price.

## Risks

Downside risks that could impede the stock from reaching our target price are: 1) lower-than-expected aluminum and alumina prices; 2) higher-than-expected costs; 3) higher-than-expected impairment loss; and 4) the Chinese government may loosen its supply cut policies if aluminum prices overshoot.

## Aluminum Corporation of China

(2600.HK; HK\$8.58; 1; 22 Jun 26; 16:10)

## Valuation

Our target price of HK\$17.08/sh for the Chalco H-share is based on 2.83x 2026E PB, set at 2.25x SD above the historical average of 1.27x to reflect stronger-than-historical-average 2026-27E ROEs, benefitting from higher aluminum price.

## Risks

Downside risks that could impede the stock from reaching our target price are: 1) Lower-than-expected aluminum and alumina prices; 2) Higher-than-expected costs; 3) Higher-than-expected impairment loss; and 4) The Chinese government may loosen its supply cut policies if aluminum price overshoots.

## China Hongqiao

(1378.HK; HK\$22.76; 1; 22 Jun 26; 16:10)

## Valuation

Our target price for Hongqiao of HK\$48.0/sh is based on 13.0x 2026E PE, set at China peers average. Our target price implies 2.7x 2026E PB and 12.9x 2026E PE.

## Risks

Major risks that could impede Hongqiao from reaching our target price include: 1) cost and capex overruns; 2) higher-than-expected capacity addition in the industry; and 3) a significant slowdown in the Chinese economy.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Aluminum Corporation of China (2600.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Jack Shang, CFA

HKD  
![](images/308a88ebcc707e373abf8455c9eb82485e4b914613edf380389b9d3be579c43a.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>04-Oct-23 09:06:45</td><td>1</td><td>*5.96</td><td>4.21</td></tr><tr><td>2</td><td>12-Dec-23 10:00:35</td><td>1</td><td>*5.51</td><td>3.59</td></tr><tr><td>3</td><td>11-Apr-24 11:41:48</td><td>1</td><td>*7.88</td><td>5.20</td></tr><tr><td>4</td><td>15-Oct-24 18:49:20</td><td>1</td><td>*9.09</td><td>6.10</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>29-Oct-24 10:06:17</td><td>1</td><td>*8.89</td><td>5.53</td></tr><tr><td>6</td><td>02-Jun-25 10:34:49</td><td>1</td><td>*7.60</td><td>4.59</td></tr><tr><td>7</td><td>29-Jul-25 11:38:09</td><td>1</td><td>*7.47</td><td>6.47</td></tr><tr><td>8</td><td>02-Nov-25 22:06:33</td><td>1</td><td>*12.41</td><td>9.88</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>07-Jan-26 10:23:57</td><td>1</td><td>*15.94</td><td>13.46</td></tr><tr><td>10</td><td>22-May-26 07:12:45</td><td>1</td><td>*17.08</td><td>10.87</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Aluminum Corporation of China (601600.SS)

Ratings and Target Price History
Fundamental Research

Analyst: Jack Shang, CFA

CNY  
![](images/0ecfe0fc7f487b59c54ea7e17272a9bb3d16f8e3d2f3f7773e5f77d8f3d662df.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>04-Oct-23 09:06:45</td><td>2</td><td>*7.12</td><td>6.28</td></tr><tr><td>2</td><td>12-Dec-23 10:00:35</td><td>*1</td><td>*7.18</td><td>5.23</td></tr><tr><td>3</td><td>11-Apr-24 11:41:48</td><td>1</td><td>*9.70</td><td>7.33</td></tr><tr><td>4</td><td>15-Oct-24 18:49:20</td><td>1</td><td>*10.96</td><td>8.51</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>31-Oct-24 12:12:41</td><td>1</td><td>*10.72</td><td>7.63</td></tr><tr><td>6</td><td>02-Jun-25 21:44:39</td><td>1</td><td>*9.62</td><td>6.54</td></tr><tr><td>7</td><td>29-Jul-25 11:30:20</td><td>1</td><td>*9.68</td><td>7.71</td></tr><tr><td>8</td><td>02-Nov-25 22:06:33</td><td>1</td><td>*14.77</td><td>9.99</td></tr></table>

Rating/target price changes above reflect Eastern Time

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>07-Jan-26 10:32:16</td><td>1</td><td>*16.74</td><td>14.05</td></tr><tr><td>10</td><td>22-May-26 07:14:31</td><td>1</td><td>*17.24</td><td>11.15</td></tr></table>

China Hongqiao (1378.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Jack Shang, CFA

![](images/a8c54a08ef2c69bd28c521da799cec20080612f50df6da1578ced6722cfa533e.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>20-Aug-23 13:05:13</td><td>1</td><td>*8.70</td><td>6.92</td></tr><tr><td>2</td><td>12-Dec-23 10:00:35</td><td>1</td><td>*9.30</td><td>5.80</td></tr><tr><td>3</td><td>01-Apr-24 03:07:57</td><td>1</td><td>*11.50</td><td>8.80</td></tr><tr><td>4</td><td>02-May-24 04:55:09</td><td>1</td><td>*13.80</td><td>11.22</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>15-Oct-24 18:49:20</td><td>1</td><td>*14.80</td><td>12.84</td></tr><tr><td>6</td><td>17-Jan-25 09:11:17</td><td>1</td><td>*15.00</td><td>12.68</td></tr><tr><td>7</td><td>20-Mar-25 11:42:49</td><td>1</td><td>*21.00</td><td>15.46</td></tr><tr><td>8</td><td>29-Jul-25 11:28:03</td><td>1</td><td>*25.20</td><td>21.35</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>04-Nov-25 04:34:03</td><td>1</td><td>*36.00</td><td>29.68</td></tr><tr><td>10</td><td>08-Apr-26 10:07:49</td><td>1</td><td>*48.00</td><td>37.36</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Aluminum Corporation of China (2600.HK)

Short-Term View/Catalyst Watch Research

Analyst: Jack Shang, CFA

![](images/54eaed3e8b064a685ad4cba5407bb169e7032023c871191b9bf196737d38bc84.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>22-May-24 04:40:28</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>5.63</td></tr><tr><td>2</td><td>21-Jun-24 00:24:50</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>5.46</td></tr><tr><td>3</td><td>16-Jul-24 14:50:56</td><td>Add CW</td><td>Downside</td><td>30 Days</td><td>5.19</td></tr><tr><td>4</td><td>16-Aug-24 00:12:08</td><td>Remove CW</td><td>Downside</td><td>30 Days</td><td>4.43</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>5</td><td>16-Aug-24 07:31:42</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>4.43</td></tr><tr><td>6</td><td>16-Sep-24 00:14:55</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>4.67</td></tr><tr><td>7</td><td>15-Oct-24 14:49:20</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>6.10</td></tr><tr

[中间内容因长度限制已省略]

e information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.
"""
