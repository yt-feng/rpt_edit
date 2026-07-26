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
# Global Semiconductors

Reality Check: Memory Upcycle Intact on Tight Inventories and Strong KV Cache Demand

## CITI'S TAKE

Korea memory equities have seen share price pullback amid the debate around possible peak-out of DRAM/NAND cycle on weakened Chinese smartphone demand and rising NAND channel inventory. Contrary to the market concern, our market analysis indicates that NAND inventories stand extremely lean at 2.6 weeks at memory suppliers and 3 weeks at hyperscalers who are major eSSD customers. We reaffirm that solid AI demand keeps memory in undersupply. Reiterate Buy rating on Samsung and Hynix.

NAND Inventory of Memory Suppliers/Hyperscalers at 2.6/3.0 weeks — Our analysis indicates (Fig.1) that 3Q26 NAND inventory at NAND suppliers is severely depleted at 2.6 weeks, below the normal level of 5 weeks. Hyperscaler's NAND inventory is at 3 weeks, much lower than the normal level of 7 weeks. In terms of NAND channel inventory, the inventory is at 5 weeks, significantly lower than the average normal level of 15 weeks. Likewise, DRAM suppliers' inventory is at 2.7 weeks (Fig.2), lower than the normal level of 5 weeks. Hyperscalers' DRAM inventory remains very low at 2.5 weeks, falling below the normal level of 7 weeks. DRAM channel inventory is at 4 weeks, which is also exceptionally lower vs. the normal level of 15 weeks.

Robust NAND Demand Upside from CMX and QLC NAND despite Consumer NAND Weakness — While recent weakness in Chinese smartphone demand has raised concerns about softening NAND prices, we expect CMX demand to rise driven by KV cache demand growth on the increasing usage of AI agents. Moreover, we project QLC SSD NAND demand to grow further as QLC SSD NAND will be increasingly utilized as a near GPU storage solution to enhance AI computing efficiency. In particular, given that Nvidia's Vera Rubin has adopted 16TB TLC SSD for CMX operation, 1,152 TB SSD is required per Rubin server system. We project CMX NAND demand to reach 34.6/115.2bn 8Gb Equiv. in 26E/27E respectively, which translates to 2.8%/9.3% of 26E global NAND demand.

Implication — Contrary to market concerns, we find memory inventory levels to be materially low at both memory suppliers and their customers. Despite fears of weak Chinese smartphone demand, memory supply/demand sufficiency at DRAM/NAND suppliers has in fact fallen from 70% to 50%. With lean memory inventory situation across supply chain, rising CMX and QLC NAND demand will result in persistent undersupply. Reiterate Buy rating on Samsung and Hynix.

Peter Lee $^{AC}$ +82-2-3705-0720
peter.sc.lee@citi.com

Jayden Oh
+82-2-3705-0747
jayden.oh@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Figure 1. NAND Inventory Trend  
![](images/e5fe38efd64e2b1d617225422ae5da64b8ce0b3c8b37155e222d0d99f9e2f610.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi Estimates

Figure 2. DRAM Inventory Trend  
![](images/516ca34d7a8a8a9a5148df549b4001032ca8ba7f327d9e342126924e3e7d0d36.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi Estimates

## Samsung Electronics

(005930.KS; W249500.0; 1; 24 Jul 26; 15:45)

## Valuation

Our 12-month target price for Samsung of W530,000 is derived using a sum-of-the-parts (SOTP) methodology, based on 2026E EBITDA. In calculating total operating value, we reference global peers in assigning fair-value EV/EBITDA multiples for the five main divisions (7.6x for Memory, 4.1x for Foundry, 0.5x for Display Panel, 4.8x for Mobile and 2.0x for Consumer Electronics), in line with trading multiples of relevant peer companies.

## Risks

Downside risks that could prevent the shares from reaching our target price include: 1) Longer-than-expected approval delay in HBM shipment to its key customers; 2) PC sales weaken more than our forecast and NAND demand fails to meet our expectations; 3) aggressive investment by competitors in memory semiconductor/foundry could have a negative impact on prices; 4) competition in the handset market intensifies, reducing SEC's handset margins; 5) any major appreciation of the won would impact SEC's earnings.

## SK Hynix

(000660.KS; W1759000.0; 1; 24 Jul 26; 15:45)

## Valuation

Our 12-month target price for SK Hynix of W3,100,000 is derived using a sum-of-the-parts (SOTP) methodology, based on 2026E EBITDA. In calculating total operating value, we break down SK Hynix's operating businesses into HBM and commodity/others business to reflect a structural change in next-gen memory market. We reference a global peer (TSMC) in assigning a fair-value EV/EBITDA multiple for HBM business, as we project the memory market is evolving from a traditional commodity market into a highly customized & customer-specific market much closer to the foundry business. For commodity memory business, we apply a historical average of 12m fwd EV/EBITDA during the beginning or early stage of memory upcycles in the past. We apply 7.2x EV/EBITDA to HBM segment and 4.2x to commodity segment to derive the target price.

## Risks

Downside risks that could prevent the shares from reaching our target price include: 1) a downturn in DRAM demand; 2) weaker NAND demand than our forecasts; and 3) weakness in global consumption.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

SK Hynix (000660.KS)
Ratings and Target Price History
Fundamental Research

![](images/e43c32d9ceb2753976ece98e37d7f28387247852527b622eb27cd6160230d370.jpg)

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>30-Aug-23 11:34:39</td><td>1</td><td>*180,000.00</td><td>119,400.00</td></tr><tr><td>2</td><td>04-Oct-23 06:14:16</td><td>1</td><td>*185,000.00</td><td>115,400.00</td></tr><tr><td>3</td><td>13-Nov-23 09:52:50</td><td>1</td><td>*190,000.00</td><td>131,800.00</td></tr><tr><td>4</td><td>01-Jan-24 18:20:58</td><td>1</td><td>*230,000.00</td><td>141,500.00</td></tr><tr><td>5</td><td>18-Mar-24 10:47:11</td><td>1</td><td>*234,000.00</td><td>164,300.00</td></tr><tr><td>6</td><td>01-Apr-24 10:34:31</td><td>1</td><td>*238,000.00</td><td>185,500.00</td></tr><tr><td>7</td><td>12-Apr-24 08:17:40</td><td>1</td><td>*310,000.00</td><td>187,400.00</td></tr><tr><td>8</td><td>25-Jun-24 06:27:18</td><td>1</td><td>*350,000.00</td><td>225,000.00</td></tr><tr><td>9</td><td>25-Jul-24 03:44:27</td><td>1</td><td>*337,000.00</td><td>190,000.00</td></tr></table>

\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>10</td><td>09-Sep-24 02:31:32</td><td>1</td><td>*310,000.00</td><td>157,000.00</td></tr><tr><td>11</td><td>24-Oct-24 06:29:30</td><td>1</td><td>*330,000.00</td><td>198,200.00</td></tr><tr><td>12</td><td>12-Nov-24 10:31:16</td><td>1</td><td>*350,000.00</td><td>185,800.00</td></tr><tr><td>13</td><td>31-Dec-24 06:45:21</td><td>1</td><td>*340,000.00</td><td>173,900.00</td></tr><tr><td>14</td><td>03-Mar-25 15:00:11</td><td>1</td><td>*350,000.00</td><td>190,200.00</td></tr><tr><td>15</td><td>01-Jul-25 03:45:10</td><td>1</td><td>*430,000.00</td><td>285,500.00</td></tr><tr><td>16</td><td>24-Jul-25 04:40:40</td><td>1</td><td>*380,000.00</td><td>269,500.00</td></tr><tr><td>17</td><td>08-Sep-25 10:00:23</td><td>1</td><td>*430,000.00</td><td>277,000.00</td></tr><tr><td>18</td><td>22-Sep-25 06:19:28</td><td>1</td><td>*480,000.00</td><td>351,000.00</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>19 20-Oct-25 04:22:50</td><td>1</td><td>*640,000.00</td><td>485,500.00</td></tr><tr><td>20 29-Oct-25 02:38:54</td><td>1</td><td>*770,000.00</td><td>558,000.00</td></tr><tr><td>21 23-Nov-25 10:20:04</td><td>1</td><td>*830,000.00</td><td>521,000.00</td></tr><tr><td>22 02-Jan-26 03:22:42</td><td>1</td><td>*900,000.00</td><td>677,000.00</td></tr><tr><td>23 26-Jan-26 07:57:46</td><td colspan="2"> $\dagger$ 1,400,000.00</td><td>736,000.00</td></tr><tr><td>24 24-Feb-26 08:08:02</td><td colspan="2"> $\dagger$ 1,550,000.00</td><td>,005,000.00</td></tr><tr><td>25 08-Apr-26 07:47:52</td><td colspan="2"> $\dagger$ 1,700,000.00</td><td>,033,000.00</td></tr><tr><td>26 11-May-26 07:42:14</td><td colspan="2"> $\dagger$ 3,100,000.00</td><td>,880,000.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

Samsung Electronics (005930.KS)
Ratings and Target Price History
Fundamental Research  
![](images/10bb59904398a9fa376654f01655ded8321e3b2cb4920493bf31d4562fb5c7bc.jpg)

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>27-Jul-23 05:53:47</td><td>1</td><td>*110,000.00</td><td>71,700.00</td></tr><tr><td>2</td><td>31-Aug-23 06:54:46</td><td>1</td><td>*120,000.00</td><td>66,900.00</td></tr><tr><td>3</td><td>22-Sep-23 09:53:22</td><td>1</td><td>*110,000.00</td><td>68,800.00</td></tr><tr><td>4</td><td>01-Apr-24 05:23:20</td><td>1</td><td>*120,000.00</td><td>82,000.00</td></tr><tr><td>5</td><td>09-Sep-24 02:31:35</td><td>1</td><td>*110,000.00</td><td>67,500.00</td></tr><tr><td>6</td><td>02-Oct-24 05:16:51</td><td>1</td><td>*97,000.00</td><td>61,300.00</td></tr><tr><td>7</td><td>26-Dec-24 07:42:50</td><td>1</td><td>*87,000.00</td><td>53,600.00</td></tr><tr><td>8</td><td>31-Dec-24 06:21:22</td><td>1</td><td>*83,000.00</td><td>53,200.00</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>16-Jul-25 05:08:04</td><td>1</td><td>*90,000.00</td><td>64,700.00</td></tr><tr><td>10</td><td>31-Jul-25 02:49:57</td><td>1</td><td>*100,000.00</td><td>71,400.00</td></tr><tr><td>11</td><td>08-Sep-25 09:30:31</td><td>1</td><td>*110,000.00</td><td>70,100.00</td></tr><tr><td>12</td><td>22-Sep-25 05:57:03</td><td>1</td><td>*120,000.00</td><td>83,500.00</td></tr><tr><td>13</td><td>14-Oct-25 07:05:40</td><td>1</td><td>*133,000.00</td><td>91,600.00</td></tr><tr><td>14</td><td>20-Oct-25 06:25:10</td><td>1</td><td>*145,000.00</td><td>98,100.00</td></tr><tr><td>15</td><td>30-Oct-25 11:44:04</td><td>1</td><td>*150,000.00</td><td>104,100.00</td></tr><tr><td>16</td><td>23-Nov-25 10:07:18</td><td>1</td><td>*170,000.00</td><td>94,800.00</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>17 02-Jan-26 02:41:08</td><td>1</td><td>*200,000.00</td><td>128,500.00</td></tr><tr><td>18 26-Jan-26 09:32:20</td><td>1</td><td>*240,000.00</td><td>152,100.00</td></tr><tr><td>19 24-Feb-26 05:11:17</td><td>1</td><td>*280,000.00</td><td>200,000.00</td></tr><tr><td>20 02-Apr-26 07:54:27</td><td>1</td><td>*300,000.00</td><td>178,400.00</td></tr><tr><td>21 07-Apr-26 02:31:16</td><td>1</td><td>*320,000.00</td><td>196,500.00</td></tr><tr><td>22 30-Apr-26 03:49:59</td><td>1</td><td>*300,000.00</td><td>220,500.00</td></tr><tr><td>23 11-May-26 07:42:55</td><td>1</td><td>*460,000.00</td><td>285,500.00</td></tr><tr><td>24 02-Jul-26 03:16:27</td><td>1</td><td>*530,000.00</td><td>286,000.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/2a4ce8f0fc9371be2df691795bbb112a3603ca765f2fe7aad93deece3f09b52b.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>31-Aug-23 02:54:46</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>66,900.00</td></tr><tr><td>2</td><td>28-Nov-23 21:19:48</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>72,700.00</td></tr><tr><td>3</td><td>01-Apr-24 01:23:20</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>82,000.00</td></tr><tr><td>4</td><td>30-Apr-24 22:52:33</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>77,500.00</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>5</td><td>17-Nov-24 11:09:02</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>53,500.00</td></tr><tr><td>6</td><td>14-Feb-25 12:17:17</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>56,000.00</td></tr><tr><td>7</td><td>16-Jul-25 01:08:04</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>64,700.00</td></tr><tr><td>8</td><td>15-Aug-25 14:07:20</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>71,600.00</td></tr></table>

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>9</td><td>23-Nov-25 05:07:18</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>94,800.00</td></tr><tr><td>10</td><td>23-Dec-25 20:51:38</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>111,500.00</td></tr><tr><td>11</td><td>11-May-26 03:42:55</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>285,500.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/94cfc697f994a8bce8252226f8cd748b279066563fc2b021330cfb5fab4c16b5.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>27-Aug-23 22:58:59</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>116,500.00</td></tr><tr><td>2</td><td>04-Oct-23 02:14:16</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>115,400.00</td></tr><tr><td>3</td><td>01-Jan-24 21:19:41</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>141,500.00</td></tr><tr><td>4</td><td>03-Mar-25 10:00:11</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>190,200.00</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td>Date</td><td>Action</td><td>Expected Direction</td><td>Closing Price</td></tr><tr><td>19-Nov-25 21:15:03</td><td>Remove CW</td><td>Upside</td><td>30 Days 562,000.00</td></tr><tr><td>26-Jan-26 02:57:46</td><td>Add CW</td><td>Upside</td><td>30 Days 736,000.00</td></tr><tr><td>25-Feb-26 20:57:35</td><td>Remove CW</td><td>Upside</td><td>30 Dayd,018,000.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of SK Hynix, Samsung Electronics.

<table><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment bankin

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
