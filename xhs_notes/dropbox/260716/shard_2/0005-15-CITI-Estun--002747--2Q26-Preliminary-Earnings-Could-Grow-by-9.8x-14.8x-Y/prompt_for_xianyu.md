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
# Estun (002747.SZ)

2Q26 Preliminary Earnings Could Grow by 9.8x-14.8x YoY to Rmb52mn-82mn from a Low Base

## CITI'S TAKE

Estun released its 1H26 preliminary results today (14 July), indicating that net profit could reach Rmb150mn-180mn, up 21x-26x YoY from a very low base of Rmb7mn in 1H25. This implies that Estun's 2Q26 net income could increase by 9.8x to 14.8x YoY to Rmb52mn-82mn, significantly higher than Bloomberg consensus of Rmb37mn and CitiE of Rmb26mn, which we believe was due more to its cost reduction efforts (e.g., procuring reducers from low-cost suppliers and disciplining OPEX) than to the industrial robot demand improvement. Although 2Q26/1H26 results beat, we are concerned about earnings growth momentum since \~60% of 1H26 net profit, or Rmb98 on average, was from one-off items, mainly the revaluation gains on Nanjing Yigong. Plus that its share price has risen by \~60% YTD and is trading at \~160x 2026E P/E and 16.9x 2026E P/B; we keep our Sell rating on Estun.

Implications — While we don't rule out the possibility that the share price could react positively to the better-than-expected 2Q26/1H26 results, we remain cautious on Estun as we are worried that its earnings growth momentum may not be sustainable to support its rich valuation, in terms of both P/E and P/B (see Estun (002747.SZ) - Fundamentals Improve But Share Price Seems Overshooting; Maintain Sell). In the China factory automation and equipment space, AI-related names are still our top picks: Han's Laser (002008.SZ, Apple and AI PCB equipment) > Han's CNC-H (3200.HK, AI PCB equipment) > Hongfa Technology (600885.SS, AIDC relay) > SUPCON (688777.SS, Industrial AI)

<table><tr><td colspan="2">Sell</td></tr><tr><td>Price (14 Jul 26 15:00)</td><td>Rmb38.400</td></tr><tr><td>Target price</td><td>Rmb28.000</td></tr><tr><td>Expected share price return</td><td>-27.1%</td></tr><tr><td>Expected dividend yield</td><td>0.0%</td></tr><tr><td>Expected total return</td><td>-27.1%</td></tr><tr><td>Market Cap</td><td>Rmb33,447MUS$4,941M</td></tr></table>

<table><tr><td>Year to 31 Dec</td><td>Net Profit (RmbM)</td><td>Diluted EPS (Rmb)</td><td>EPS growth (%)</td><td>P/E (x)</td><td>P/B (x)</td><td>ROE (%)</td><td>Yield (%)</td></tr><tr><td>2024A</td><td>-810</td><td>-0.930</td><td>na</td><td>na</td><td>18.7</td><td>-36.1</td><td>na</td></tr><tr><td>2025A</td><td>45</td><td>0.050</td><td>105.4</td><td>na</td><td>17.1</td><td>2.4</td><td>na</td></tr><tr><td>2026E</td><td>233</td><td>0.241</td><td>382.5</td><td>159.2</td><td>16.9</td><td>11.2</td><td>na</td></tr><tr><td>2027E</td><td>273</td><td>0.282</td><td>16.7</td><td>136.4</td><td>15.1</td><td>11.7</td><td>na</td></tr><tr><td>2028E</td><td>345</td><td>0.357</td><td>26.8</td><td>107.6</td><td>13.2</td><td>13.1</td><td>na</td></tr></table>

Source: Powered by dataCentral

Eric Lau
+852-2501-2726
eric.h.lau@citi.com

## Earnings Summary

Jamie Wang $^{AC}$ +852-2501-2772
jamie.ck.wang@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Figure 1. Estun: 2Q26/1H26 preliminary results snapshot

<table><tr><td rowspan="2">(Rmb mn)</td><td rowspan="2">1H25</td><td colspan="3">1H26P</td><td rowspan="2">2Q25</td><td rowspan="2">1Q26</td><td colspan="3">2Q26P</td></tr><tr><td>Lower bound</td><td>Mid point</td><td>Upper bound</td><td>Lower bound</td><td>Mid point</td><td>Upper bound</td></tr><tr><td>P&amp;L</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net profit</td><td>7</td><td>150</td><td>165</td><td>180</td><td>(6)</td><td>98</td><td>52</td><td>67</td><td>82</td></tr><tr><td>Recurring profit</td><td>(18)</td><td>60</td><td>68</td><td>75</td><td>(22)</td><td>19</td><td>41</td><td>48</td><td>56</td></tr><tr><td>YoY</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net profit</td><td>109%</td><td>2146%</td><td>2370%</td><td>2595%</td><td>93%</td><td>675%</td><td>977%</td><td>1229%</td><td>1481%</td></tr><tr><td>Recurring profit</td><td>82%</td><td>441%</td><td>484%</td><td>526%</td><td>74%</td><td>364%</td><td>287%</td><td>321%</td><td>356%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Company Reports

## Bull/Bear: Estun

![](images/7e11dc1a903caf2a7c788aadde81bc2b0ed31bdf960501cc329f5e1e11806973.jpg)  
Spread 62pp
Current Price and expected returns (upside/downside) as of 14 Jul 2026

![](images/16beb48280a5aed1ded8093fa6374f7f8ccf153bda65eb0e7991ef497be03409.jpg)

## BULL Assumptions

\- Rerated to 20.0x P/B due to better-than-expected Estun & CLOOS shipment

![](images/9fb3cda1a81334a0cdebca6b1fef0c728f98d29195993efb267dddb7a22f0d25.jpg)

## BASE Assumptions

\- Valued at 12.3x 2026E P/B

![](images/8616d1dac83f16994e4e75cfe024541531d71c08932ffd47d61ac50c382e7f87.jpg)

## BEAR Assumptions

\- Worse-than-expected Estun & CLOOS shipment

## Estun

## Valuation

We use P/B as our valuation methodology due to Estun's fluctuating earnings. Our target price of Rmb28.0 is based on 12.3x 2026E P/B, set at 2.0 SD above average to reflect Estun's improving fundamentals.

## Risks

Key upside risks that could cause Estun shares to trade above our target price include: 1) stronger-than-expected industrial robot shipments or market share gains; 2) better-than-expected GPM due to lower raw material costs or alleviated price competition; and 3) favorable FX.

## Han's CNC Technology

(3200.HK; HK\$126.9; 1; 14 Jul 26; 16:10)

## Valuation

Our target price of HK\$325 is based on \~51x 2027E P/E, set at 25% discount to its A-share's valuation. We believe that our target multiple is not aggressive given a \~81% earnings CAGR for 2026E-27E.

## Risks

Potential downside risks that could impede the shares from reaching our target price include: 1) weaker-than-expected AI PCB equipment demand, 2) worse-than-expected GPM due to rising component costs, and 3) intensifying price competition due to the industry's equipment supply increase.

## Han's Laser Technology

(002008.SZ; Rmb119.5; 1; 14 Jul 26; 15:00)

## Valuation

Our 12-month target price for Han's Laser of Rmb177.0 is based on 55x 2027E P/E, set at the previous peak P/E in 2018 to reflect its "super cycle" led by stronger demand for PCB and IT (Apple) equipment.

## Risks

Key fundamental downside risks that could prevent the shares from reaching our target price include: 1) fewer-than-expected Apple orders; 2) fiercer competition, which could pressure margins; 3) any weakening of auto sales, which would hurt high-power laser equipment demand; 4) failure of any of the new investment projects; and 5) newly emerging technologies substituting laser equipment.

## Hongfa Technology

(600885.SS; Rmb34.15; 1; 14 Jul 26; 15:00)

## Valuation

Our 12-month target price of Rmb43.0 is based on \~32x 2026E P/E, set at +1.0x SD to reflect Hongfa's faster earnings growth driven by strong demand and ASP hikes, despite GPM pressure.

## Risks

Key downside risks include: 1) weaker relay demand especially from NEV and auto sectors; 2) worse-than-expected GPM pressure; and 3) intensifying competition particularly from home appliance segement.

## SUPCON Technology

(688777.SS; Rmb98.24; 1; 14 Jul 26; 15:00)

## Valuation

Our TP of Rmb99.0 is based on SOTP methodology. We assign \~60x P/E (avg.) to the value of SUPCON's business as a whole and add an incremental market cap to value SUPCON's fast-growing industrial AI revenue at 60x 2026 P/S, set at the difference of P/S between SUPCON and Chinese pure AI model companies such as MiniMax (100.HK), Knowledge Atlas (2513.HK), Deepexi (1384.HK), and Xunce (3317.HK)

## Risks

Downside risks that could prevent the stock from reaching our target price include 1) weaker-than-expected industrial AI revenue growth, 2) worse industrial AI monetization, and 3) worse-than-expected GPM contraction due to unfavorable product mix changes.

<table><tr><td>Date1 18-Feb-24 16:00:08</td><td>Rating*1</td><td>Target Price*50.00</td><td>Closing Price40.14</td></tr><tr><td>2 06-Apr-25 18:46:58</td><td>*3</td><td>*46.00</td><td>52.38</td></tr></table>

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Hongfa Technology (600885.SS)
Ratings and Target Price History
Fundamental Research

Analyst: Jamie Wang

![](images/7e46b0188557fed4a7bb179d76e7159872246cfbd9103e427bd36d76cba5f4b1.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>02-Nov-23 10:35:31</td><td>1</td><td>*25.71</td><td>19.72</td></tr><tr><td>2</td><td>01-Apr-24 06:20:14</td><td>1</td><td>*25.00</td><td>18.68</td></tr><tr><td>3</td><td>14-Jun-24 11:56:27</td><td>1</td><td>*23.86</td><td>20.86</td></tr><tr><td>4</td><td>08-Aug-24 13:47:41</td><td>1</td><td>*24.29</td><td>19.69</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>28-Mar-25 14:38:49</td><td>1</td><td>*30.00</td><td>25.68</td></tr><tr><td>6</td><td>29-Jul-25 12:10:44</td><td>1</td><td>*30.00</td><td>23.61</td></tr><tr><td>7</td><td>14-Jan-26 05:18:38</td><td>*2</td><td>*33.00</td><td>31.39</td></tr><tr><td>8</td><td>09-Apr-26 10:50:44</td><td>2</td><td>*28.00</td><td>26.47</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>04-May-26 08:17:57</td><td>*1</td><td>*38.00</td><td>31.14</td></tr><tr><td>10</td><td>27-May-26 13:09:01</td><td>1</td><td>*43.00</td><td>35.61</td></tr></table>

Rating/target price changes above reflect Eastern Time

## SUPCON Technology (688777.SS)

Ratings and Target Price History
Fundamental Research

Analyst: Jamie Wang

![](images/92cdb046bf0b071d1a54d0bc1ade439ea63b364319715897306299b6fbd9a3e4.jpg)  
\*Indicates Change  
Rating/target price changes above reflect Eastern Time

Ratings and Target Price History
Fundamental Research

![](images/cc4980487ad4eeec03202309b62ebdb2ad5a6d0474234c185073699e7f395eb9.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>31-Oct-23 15:07:48</td><td>1</td><td>*29.00</td><td>18.80</td></tr><tr><td>2</td><td>02-Feb-24 02:20:39</td><td>1</td><td>*16.00</td><td>12.63</td></tr><tr><td>3</td><td>07-May-24 03:17:15</td><td>*3</td><td>*14.00</td><td>16.59</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>11-Jul-24 13:42:47</td><td>3</td><td>*10.60</td><td>13.10</td></tr><tr><td>5</td><td>04-May-25 18:27:04</td><td>3</td><td>*13.60</td><td>20.00</td></tr><tr><td>6</td><td>01-Sep-25 19:52:14</td><td>3</td><td>*13.80</td><td>23.63</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>13-Jul-26 05:08:34</td><td>3</td><td>*28.00</td><td>38.50</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Han's CNC Technology (3200.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Jamie Wang

![](images/6000d4439f67a4170482e000fd3ac9399583f8c3fb037314b3f99e08b5961ea7.jpg)

<table><tr><td>Date109-Feb-26 03:30:27</td><td>Rating*1</td><td>Target Price*142.00</td><td>Closing Price120.80</td></tr><tr><td>210-Apr-26 12:18:38</td><td>1</td><td>*160.00</td><td>119.80</td></tr></table>

\*Indicates Change  
Rating/target price changes above reflect Eastern Time

## Han's Laser Technology (002008.SZ)

Ratings and Target Price History
Fundamental Research

Analyst: Jamie Wang

![](images/1d56e17bb5ff577983ed8b3783d58224c5675a0d14f1206deba6e721e0fb363e.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>22-Aug-23 02:00:19</td><td>1</td><td>*28.00</td><td>22.53</td></tr><tr><td>2</td><td>23-Oct-23 15:54:01</td><td>1</td><td>*25.00</td><td>21.11</td></tr><tr><td>3</td><td>18-Apr-24 13:03:24</td><td>1</td><td>*23.00</td><td>18.95</td></tr><tr><td>4</td><td>16-Aug-24 03:59:06</td><td>1</td><td>*24.00</td><td>20.12</td></tr><tr><td>5</td><td>26-Jan-25 11:17:15</td><td>1</td><td>*31.00</td><td>25.75</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>25-Apr-25 13:05:16</td><td>1</td><td>*28.00</td><td>23.44</td></tr><tr><td>7</td><td>28-Aug-25 00:11:15</td><td>1</td><td>*45.00</td><td>37.19</td></tr><tr><td>8</td><td>30-Sep-25 09:43:36</td><td>1</td><td>*54.00</td><td>40.71</td></tr><tr><td>9</td><td>02-Mar-26 09:47:27</td><td>1</td><td>*89.00</td><td>74.62</td></tr><tr><td>10</td><td>10-Apr-26 12:18:38</td><td>1</td><td>*99.00</td><td>76.55</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>11</td><td>20-Apr-26 13:52:14</td><td>1</td><td>*103.00</td><td>89.18</td></tr><tr><td>12</td><td>15-Jun-26 22:58:34</td><td>1</td><td>*155.00</td><td>124.20</td></tr><tr><td>13</td><td>24-Jun-26 11:21:29</td><td>1</td><td>*177.00</td><td>152.23</td></tr></table>

Rating/target price changes above reflect Eastern Time

Estun (002747.SZ)
Short-Term View/Catalyst Watch Research  
![](images/c431358a53f3eddfe955a365e4f8dbc20883fbb1d396264968aef4e1e08cc895.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>11-Jul-24 09:42:47</td><td>Add STV</td><td>Downside</td><td>90 Days</td><td>13.10</td></tr><tr><td>2</td><td>09-Oct-24 23:26:15</td><td>Remove STV</td><td>Downside</td><td>90 Days</td><td>15.18</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>3 24-Jan-25 02:16:06</td><td>Add STV</td><td>Downside</td><td>30 Days</td><td>20.17</td></tr><tr><td>4 23-Feb-25 21:14:39</td><td>Remove STV</td><td>Downside</td><td>30 Days</td><td>23.54</td></tr></table>

<table><tr><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>5</td><td>14-Jul-25 08:31:16</td><td>Add STV</td><td>Downside</td><td>30 Days</td><td>20.39</td></tr><tr><td>6</td><td>13-Aug-25 23:05:37</td><td>Remove STV</td><td>Downside</td

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a

subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
