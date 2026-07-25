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
22 Jul 2026 11:00:37 ET | 13 pages

# China Renewable Energy

## Solar Product Prices Stayed Low; PRC Solar Installation Fell 66% in 1H26

## CITI'S TAKE

PRC solar product prices had mixed trends this week, including down 0.4-2.3% wow for wafers and solar modules but up 0.1-0.9% wow for polysilicon and solar cells. Solar glass prices were stable with industry operational capacity reducing 6,250 tons/day or 7.7% month-to-date due to low profitability. PRC solar installations dropped 65.9% yoy to 72.1GW in 1H26 from a high base, including -9.3% yoy to 12.5GW in June. The official papers of the energy consumption standards for polysilicon and the energy efficiency standards for solar modules and inverters, released recently and effective from 1 Jan 2027, could help phase out low-efficiency capacities. Nevertheless, they may not have a material impact on current effective supply. In PRC solar and ESS sector, we prefer ESS makers like Sungrow and Deye with high shipment volume growth.

Polysilicon prices slightly improved — The average market price of rod-type polysilicon increased 0.1% wow to Rmb31.6/kg, and was flat for granular polysilicon at Rmb31.5/kg in the week ended 22 Jul 2026. According to SMM, total polysilicon inventory at producer plants was high at 318k tons as of 16 July. Some plants slightly increased productions during flood season. China Silicon Industry Association forecast the monthly polysilicon output is expected to be 100k tons in July, slightly more than the monthly demand of 91k tons.

Prices down for wafers but up for solar cells — Market prices of n-type wafer declined 2.3% wow to Rmb0.84/W for 182mm products and -0.9% wow to Rmb1.15/W for 210mm products, due to weak demand and relatively high plant utilization. SMM estimates China wafer production volume could drop by 3.7% mom to 52.3GW in July, and its inventory level decreased 3.1% wow to 27.1GW as of July 16. Capacity consolidation has begun at wafer segment, with tier 2 and 3 companies leasing out their capacity, according to SMM. Average solar cell price increased 0.9% wow to Rmb0.27/W for TOPCon products this week. SCI99 expects cell segment price to be steady in the near term.

Solar module prices mildly dropped wow — Average solar module price was down 0.4% wow to Rmb0.71/W for 182mm products this week. PRC monthly solar module output is expected to be +11.0% mom to 42.0GW in July, according to SMM.

More solar glass capacity suspended operation — Average solar glass market prices stayed at Rmb9.0/m2 for 2.0mm products and Rmb15.5/m2 for 3.2mm ones. The industry-wide average inventory period was 47.3 days as of July 16, - 1.2% wow.

## China Solar Sector

Pierre Lau, CFA $^{AC}$ +852-2501-2716
pierre.lau@citi.com

Air Ma
air.ma@citi.com

## See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

Source: SMM, Citi

China operational daily solar glass melting capacity reduced 2.2% wow to 77,750 tons (-15.6% yoy) as of July 16. PRC operational solar glass production capacity has reduced 6,250 tons/day or 7.7% month-to-date due to low profitability.

Figure 1. PRC weekly polysilicon prices in the week ended Jul 22

<table><tr><td></td><td colspan="4">Mono-$</td></tr><tr><td>182mm TOPCon</td><td>This week</td><td>WoW</td><td>MoM</td><td>YoY</td></tr><tr><td>Polysilicon (Rmb/kg)</td><td>31.6</td><td>0.1%</td><td>-3.2%</td><td>-29.3%</td></tr><tr><td>Wafer (Rmb/pc)</td><td>0.84</td><td>-2.3%</td><td>-3.4%</td><td>-30.0%</td></tr><tr><td>Cell (Rmb/W)</td><td>0.27</td><td>0.9%</td><td>-7.8%</td><td>-7.8%</td></tr><tr><td>Module (Rmb/W)</td><td>0.71</td><td>-0.4%</td><td>-1.5%</td><td>7.1%</td></tr><tr><td>Glass -2.0mm (Rmb/m2)</td><td>9.0</td><td>0.0%</td><td>0.0%</td><td>-12.2%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 2. PRC weekly polysilicon price  
![](images/51a499492001b6e0bdba940deff7344702699a70adee06e73d895fac018ed259.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: SMM, Citi

Figure 3. PRC weekly wafer price  
![](images/d4271586665eb0677e1163f35c5f7652fe38641cd16a5b1758c5df5b615875d9.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: SMM, Citi

Figure 4. PRC weekly cell price  
![](images/92fb5d7f7c70facb7b6bbc227db8a51a86658a621410356c0675d002a9e54182.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 5. PRC weekly module price  
![](images/694965d4239da0fbe94df9a13a067398e349a8bb129bf1b79e07cccf269984f9.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 6. PRC weekly solar glass price  
![](images/76923749f5faf4173f4cb53e1ae2b82487f6636fe8f47cf3e150f2e6703290a4.jpg)  
Source: SMM, Citi  
© 2026 Citi Inc. No redistribution without Citi's written permission.

## Ningbo Deye Technology

(605117.SS; Rmb80.46; 1; 22 Jul 26; 15:00)

## Valuation

Our target price for Deye of Rmb142.857/share is based on a DCF model, which we believe is a suitable valuation methodology as we expect sustainable growth in energy storage demand from emerging markets, from current low penetration levels. Our model incorporates our forecasts for cash flows up to 2035E and assumes a terminal growth rate of 3.0%. We apply a WACC of 8.4%, derived from a risk-free rate of 1.6%, a market risk premium of 8.9%, and an equity beta of 0.9x. Our target price equates to a 2027E P/E of 26.8x and P/B of 10.0x.

## Risks

Key downside risks that could cause Deye's shares to trade below our target price include: (i) lower-than-expected residential and C&I energy storage demand in emerging markets; (ii) fiercer-than-expected price competition among inverter peers; and (iii) higher-than-expected trade tariffs against Chinese inverter products in overseas markets.

## Sungrow Power Supply

(300274.SZ; Rmb109.95; 1; 22 Jul 26; 15:00)

## Valuation

Our target price for Sungrow shares of Rmb185.0 is based on a DCF valuation, which we believe is appropriate because it captures the long-term potential returns of the company. We factor in earnings forecasts up to 2035E and terminal growth of 4%. Our WACC for Sungrow is 10.2%, which assumes: 1) a risk-free rate of 5.2%; 2) a market risk premium of 6.8%; 3) an equity beta of 1.1x; 4) a cost-of-debt of 3.9%; 5) a target debt-to-capital ratio of 30%; and 6) a 25.0% corporate tax rate. At our DCF-based target price, Sungrow would trade at 20.2x 2027E PE and 5.3x PB.

## Risks

Key downside risks that could prevent Sungrow shares from reaching our target price include: (i) slower-than-expected solar installation that could accelerate Sungrow's PV inverter and EPC business growth; (ii) less-than-expected energy storage system demand from China and the overseas market; and (iii) intensification of overseas trade tensions that could lessen the exports of Sungrow's products.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

![](images/8fb88c4b880a8cbaf927c6bdf992a8c3a34510988315e6eec3760b59918f46e3.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>11-Jul-25 15:08:17</td><td>*1</td><td>*48.57</td><td>39.34</td></tr><tr><td>2</td><td>28-Aug-25 12:58:00</td><td>1</td><td>*50.71</td><td>44.42</td></tr><tr><td>3</td><td>22-Sep-25 03:45:06</td><td>1</td><td>*55.86</td><td>49.53</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>09-Nov-25 18:20:39</td><td>1</td><td>*72.86</td><td>62.72</td></tr><tr><td>5</td><td>10-Mar-26 05:39:48</td><td>1</td><td>*103.57</td><td>85.64</td></tr><tr><td>6</td><td>09-Apr-26 13:43:44</td><td>1</td><td>*117.86</td><td>90.65</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>7</td><td>20-May-26 02:58:11</td><td>1</td><td>*142.86</td><td>121.21</td></tr><tr><td>8</td><td>05-Jun-26 02:40:31</td><td>1</td><td>*142.86</td><td>104.91</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Sungrow Power Supply (300274.SZ)

Ratings and Target Price History
Fundamental Research

Analyst: Pierre Lau, CFA

![](images/642bba6be49528b687dc0adaeef1fb1dbb8f2f23f7b3888e90be9a2042295719.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>24-Aug-23 14:05:57</td><td>1</td><td>*104.29</td><td>70.93</td></tr><tr><td>2</td><td>27-Oct-23 14:13:49</td><td>1</td><td>*85.71</td><td>59.19</td></tr><tr><td>3</td><td>22-Apr-24 12:53:27</td><td>1</td><td>*87.86</td><td>67.14</td></tr><tr><td>4</td><td>30-Jun-24 14:26:02</td><td>1</td><td>*76.00</td><td>62.03</td></tr><tr><td>5</td><td>25-Aug-24 11:11:18</td><td>1</td><td>*78.00</td><td>68.12</td></tr><tr><td>6</td><td>31-Oct-24 12:55:52</td><td>1</td><td>*105.00</td><td>90.62</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>7</td><td>10-Feb-25 09:07:21</td><td>1</td><td>*85.00</td><td>72.13</td></tr><tr><td>8</td><td>23-Feb-25 08:42:35</td><td>*3</td><td>*63.00</td><td>67.47</td></tr><tr><td>9</td><td>15-Apr-25 08:13:28</td><td>3</td><td>*48.00</td><td>57.29</td></tr><tr><td>10</td><td>27-Apr-25 20:08:42</td><td>3</td><td>*53.00</td><td>58.82</td></tr><tr><td>11</td><td>27-Jul-25 17:35:10</td><td>*1</td><td>*90.00</td><td>75.78</td></tr><tr><td>12</td><td>25-Aug-25 13:35:38</td><td>1</td><td>*120.00</td><td>102.60</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>13</td><td>22-Sep-25 03:45:06</td><td>1</td><td>*160.00</td><td>137.23</td></tr><tr><td>14</td><td>28-Oct-25 12:58:24</td><td>1</td><td>*200.00</td><td>165.88</td></tr><tr><td>15</td><td>09-Nov-25 16:02:51</td><td>1</td><td>*240.00</td><td>201.00</td></tr><tr><td>16</td><td>31-Mar-26 13:36:12</td><td>1</td><td>*200.10</td><td>150.76</td></tr><tr><td>17</td><td>27-Apr-26 12:08:02</td><td>1</td><td>*168.00</td><td>131.39</td></tr><tr><td>18</td><td>25-Jun-26 10:15:49</td><td>1</td><td>*185.00</td><td>152.66</td></tr></table>

Rating/target price changes above reflect Eastern Time

Sungrow Power Supply (300274.SZ)
Short-Term View/Catalyst Watch Research  
Ningbo Deye Technology (605117.SS)
Short-Term View/Catalyst Watch Research  
![](images/41a1b947ef0f1610c6fc9d4f20e0da6528f55d555f329b984e3b1caed90a05b7.jpg)

<table><tr><td rowspan="2"></td><td rowspan="2">Date</td><td rowspan="2">Action</td><td colspan="2">Expected</td><td rowspan="2">Closing Price</td></tr><tr><td>Direction</td><td>Duration</td></tr><tr><td>1</td><td>08-Jul-26 00:32:26</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>89.57</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

![](images/8854aff409f99c8ebf7d88f10faf7d956fdc3ae0b6d4ba2998cf70014e42890f.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>15-Apr-24 01:38:47</td><td>Add CW</td><td>Downside</td><td>30 Days</td><td>71.24</td></tr><tr><td>2</td><td>15-May-24 13:01:03</td><td>Remove CW</td><td>Downside</td><td>30 Days</td><td>75.11</td></tr><tr><td>3</td><td>01-Jul-24 00:27:42</td><td>Add CW</td><td>Downside</td><td>90 Days</td><td>63.15</td></tr><tr><td>4</td><td>27-Sep-24 14:27:48</td><td>Remove CW</td><td>Downside</td><td>90 Days</td><td>85.20</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>5</td><td>10-Feb-25 04:07:21</td><td>Add CW</td><td>Downside</td><td>90 Days</td><td>72.13</td></tr><tr><td>6</td><td>11-May-25 23:13:57</td><td>Remove CW</td><td>Downside</td><td>90 Days</td><td>62.52</td></tr><tr><td>7</td><td>27-Jul-25 13:35:10</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>75.78</td></tr><tr><td>8</td><td>24-Oct-25 14:21:43</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>165.00</td></tr></table>

<table><tr><td rowspan="2" colspan="2">Date</td><td rowspan="2">Action</td><td rowspan="2">Expected Direction</td><td rowspan="2">Duration</td><td rowspan="2">Closing Price</td></tr><tr></tr><tr><td>9</td><td>27-Jan-26 22:15:05</td><td>Add CW</td><td>Downside</td><td>90 Days</td><td>158.19</td></tr><tr><td>10</td><td>28-Apr-26 23:16:25</td><td>Remove CW</td><td>Downside</td><td>90 Days</td><td>129.89</td></tr><tr><td>11</td><td>25-Jun-26 06:15:49</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>152.66</td></tr></table>

Rating/target price changes above reflect Eastern Time

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Sungrow Power Supply in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Sungrow Power Supply.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Sungrow Power Supply.

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommen

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
