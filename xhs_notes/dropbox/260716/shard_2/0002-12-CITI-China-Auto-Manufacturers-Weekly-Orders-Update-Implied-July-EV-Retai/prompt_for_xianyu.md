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
# China Auto Manufacturers

## Weekly Orders Update - Implied July EV Retail at -5% MoM/-3% YoY

## CITI'S TAKE

According to our dealer industry checks, overall 2nd week July (6 Jul - 12 Jul) EV orders were down -16% WoW (-5% MTD-MoM), weaker than our expectations. If the MoM pace of orders is eventually the same as retail growth, by assuming -5% NEV retail sales MoM decline for the full month of Jul-26, this should yield monthly EV retail sales at 950k units, implying Jul-26 NEV retail -2.7% YoY (7M26 at -12.4% YoY). In terms of MTD-MoM pace. BYD (+59%) and Leapmotor (+11%) outperformed sector at -5%; while Li Auto (-9%), Xiaomi (-11%), Geely Galaxy(-14%), Xpeng(-22%), Tesla(-26%) and Zeekr (-27%) underperformed. The large MoM decline of Huawei Harmony and Nio was due to early-June order peak post new models launch (all-new M9 and ES9). Further readings: (1) BYD (1211.HK) - July Outlook, after June retail beats; (2) Seres (601127.SS/9927.HK) - Lower H-sh to Sell; A-sh Still a Sell; Cut TPs to Rmb37.4/HK\$33.5

Figure 1. Weekly Orders

<table><tr><td rowspan="3">Brands</td><td colspan="4">Jun-26</td><td colspan="3">Jul-26</td><td rowspan="3">WoW</td><td rowspan="3">MTD MoM</td></tr><tr><td>1st week</td><td>2nd week</td><td>3rd week</td><td>4th week</td><td>1st week</td><td>2nd week</td><td></td></tr><tr><td>1 Jun - 7 Jun</td><td>8 Jun - 14 Jun</td><td>15 Jun - 21 Jun</td><td>22 Jun - 28 Jun</td><td>29 Jun - 5 Jul</td><td>6 Jul - 12 Jul</td><td></td></tr><tr><td>Li Auto</td><td>6.7k</td><td>5.5k</td><td>5.9k</td><td>9.9k</td><td>5.7k</td><td>5.4k</td><td>-5%</td><td>-9%</td><td></td></tr><tr><td>Huawei Harmony</td><td>24.2k</td><td>18.2k</td><td>11.7k</td><td>10.8k</td><td>8.1k</td><td>6.8k</td><td>-16%</td><td>-65%</td><td></td></tr><tr><td>Leapmotor</td><td>14.6k</td><td>11.5k</td><td>14.1k</td><td>15.0k</td><td>13.8k</td><td>15.2k</td><td>10%</td><td>11%</td><td></td></tr><tr><td>NIO (incl. ONVO)</td><td>28.0k</td><td>19.5k</td><td>14.5k</td><td>11.6k</td><td>10.8k</td><td>12.2k</td><td>13%</td><td>-52%</td><td></td></tr><tr><td>BYD</td><td>47.7k</td><td>45.7k</td><td>106.8k</td><td>70.6k</td><td>86.5k</td><td>62.1k</td><td>-28%</td><td>59%</td><td></td></tr><tr><td>Xiaomi</td><td>7.4k</td><td>5.0k</td><td>7.2k</td><td>6.1k</td><td>5.4k</td><td>5.6k</td><td>4%</td><td>-11%</td><td></td></tr><tr><td>Zeekr</td><td>6.5k</td><td>5.5k</td><td>5.3k</td><td>5.4k</td><td>4.6k</td><td>4.2k</td><td>-9%</td><td>-27%</td><td></td></tr><tr><td>Tesla</td><td>14.2k</td><td>13.1k</td><td>12.6k</td><td>11.2k</td><td>10.9k</td><td>9.3k</td><td>-15%</td><td>-26%</td><td></td></tr><tr><td>Geely Galaxy</td><td>18.3k</td><td>21.3k</td><td>18.9k</td><td>22.9k</td><td>18.1k</td><td>15.8k</td><td>-13%</td><td>-14%</td><td></td></tr><tr><td>Xpeng (incl. Mona)</td><td>9.5k</td><td>8.3k</td><td>9.0k</td><td>7.3k</td><td>6.8k</td><td>7.1k</td><td>5%</td><td>-22%</td><td></td></tr><tr><td>Sector total (incl. Xiaomi)</td><td>177,110</td><td>153,640</td><td>206,000</td><td>170,770</td><td>170,660</td><td>143,640</td><td>-16%</td><td>-5%</td><td></td></tr><tr><td>Sector total (excl. Xiaomi)</td><td>169,700</td><td>148,630</td><td>198,800</td><td>164,670</td><td>165,260</td><td>138,040</td><td>-16%</td><td>-5%</td><td></td></tr><tr><td>Lithium Carbonate ASPBattery Grade (Rmb/ton)</td><td>159,000</td><td>173,800</td><td>162,700</td><td>146,500</td><td>166,500</td><td>150,000</td><td>-10%</td><td>-14%</td><td></td></tr></table>

Jeff Chung $^{AC}$ +852-2501-2787
jeff.m.chung@citi.com

© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: Citi, Citi Dealership Check

Kyle Wu

+852-2501-8483

kyle.wu@citi.com

Figure 2. Weekly Orders  
![](images/59419ab22ec3703b303807bd228331d4a8e6c316c2e898cd36e52a4a760f2b72.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Citi Dealership Check  
Horizontal Axis: WoW

## BYD

(1211.HK; HK\$83.95; 1; 13 Jul 26; 16:10)

## Valuation

By applying 1.2x 2026E PEG on a +25% 2026-28E NP CAGR, we derive our TP of HK\$142, implying 30x/25x 2026E/27E PER. We adopt PEG valuation, as we believe it can more accurately reflect the valuation of this growth stock.

## Risks

Key downside risks that could prevent the BYD H-share from reaching our target price include: 1) weaker-than-expected NEV bus or PV sales; 2) a slower-than-expected ramp-up of the Skyrail business; 3) another prolonged capex cycle; and 4) unexpected cash flow issues.

## BYD

(002594.SZ; Rmb86.98; 1; 13 Jul 26; 15:00)

## Valuation

Our target price of Rmb131 is set at 1.2x 26E PEG based on a +25% 2025-27E NP CAGR. Our TP implies 30x/25x 2026E/27E P/Es. We adopt a PEG valuation as we believe it more accurately reflects the potential of a growth stock.

## Risks

Downside risks that could prevent the BYD A-share from reaching our target price include 1) weaker-than-expected NEV bus or PV sales, 2) a slower-than-expected ramp-up of the Skyrail business, 3) another prolonged capex cycle, and 4) unexpected cash flow issues.

## Seres Group

(9927.HK; HK\$41.32; 3; 13 Jul 26; 16:10)

## Valuation

We adopt P/S valuation given near-term profitability has largely deteriorated. By adopting 0.35x 2026E P/S (2SD below average since H-share listing to reflect margin headwinds and competition), we derive a target price of HK\$33.5.

## Risks

Potential upside risks include: (1) Improved auto market sentiment on higher government subsidy support; (2) Better-than-expected operating efficiency improvements; (3) Better-than-expected export sales to fuel earnings growth; (4) Better-than-expected ADAS penetration growth to boost smart EV sales.

Potential downside risks: (1) China economy slowdown may drag down overall NEV growth; (2) Uncertain research and development outcomes; (3) Intensified market competition; (4) Potential defects in NEV and software systems; (5) Potential instability of the partnership with Huawei.

Any of these risk factors could cause the shares to deviate from our target price.

## Seres Group

(601127.SS; Rmb53.91; 3; 13 Jul 26; 15:00)

## Valuation

We adopt P/S valuation given near-term profitability has largely deteriorated. By adopting 0.45x 2026E P/S (2SD below 1-year average to reflect margin headwinds and competition), we derive a target price of Rmb37.4.

## Risks

Potential upside risks include: (1) Improved auto market sentiment on higher government subsidy support; (2) Better-than-expected operating efficiency improvements; (3) Better-than-expected export sales to fuel earnings growth; (4) Better-than-

expected ADAS penetration growth to boost smart EV sales.

Potential downside risks: (1) China economy slowdown may drag down overall NEV growth; (2) Uncertain research and development outcomes; (3) Intensified market competition; (4) Potential defects in NEV and software systems; (5) Potential instability of the partnership with Huawei.

Any of these risk factors could cause the shares to deviate from our target price.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

BYD (1211.HK)
Ratings and Target Price History
Fundamental Research

Analyst: Jeff Chung

![](images/a010c0797c5595f8cd9bbc22b2461cae1397d8695c6d9cb800476c432592752d.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>11-Jan-24 13:28:07</td><td>1</td><td>*154.33</td><td>70.80</td></tr><tr><td>2</td><td>29-May-24 07:27:17</td><td>1</td><td>*158.33</td><td>72.53</td></tr><tr><td>3</td><td>01-Sep-24 20:09:08</td><td>1</td><td>*162.67</td><td>80.40</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>30-Oct-24 11:36:39</td><td>1</td><td>*166.67</td><td>98.33</td></tr><tr><td>5</td><td>14-Feb-25 11:26:49</td><td>1</td><td>*229.33</td><td>121.40</td></tr><tr><td>6</td><td>20-May-25 14:45:04</td><td>1</td><td>*242.33</td><td>148.20</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>7 13-Jun-25 00:00:04</td><td>1</td><td>*233.00</td><td>131.10</td></tr><tr><td>8 07-Sep-25 20:44:21</td><td>1</td><td>*174.00</td><td>105.60</td></tr><tr><td>9 30-Mar-26 12:12:39</td><td>1</td><td>*142.00</td><td>105.80</td></tr></table>

Rating/target price changes above reflect Eastern Time

## BYD (002594.SZ)

Ratings and Target Price History
Fundamental Research

Analyst: Jeff Chung

![](images/7ad78b5640f27d20e1360e2ff692574e2f3a8b8d1fcaef86cddad360801a5d2d.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>11-Jan-24 13:28:07</td><td>1</td><td>*140.33</td><td>65.59</td></tr><tr><td>2</td><td>29-May-24 07:27:17</td><td>1</td><td>*145.67</td><td>74.90</td></tr><tr><td>3</td><td>01-Sep-24 20:09:08</td><td>1</td><td>*149.67</td><td>83.14</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>30-Oct-24 11:36:39</td><td>1</td><td>*153.33</td><td>101.85</td></tr><tr><td>5</td><td>14-Feb-25 11:26:49</td><td>1</td><td>*210.00</td><td>118.68</td></tr><tr><td>6</td><td>20-May-25 14:45:04</td><td>1</td><td>*223.00</td><td>131.60</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>7</td><td>29-Jul-25 23:21:33</td><td>1</td><td>*214.00</td><td>111.42</td></tr><tr><td>8</td><td>07-Sep-25 20:44:21</td><td>1</td><td>*160.00</td><td>107.26</td></tr><tr><td>9</td><td>30-Mar-26 12:12:39</td><td>1</td><td>*131.00</td><td>106.05</td></tr></table>

Rating/target price changes above reflect Eastern Time

Seres Group (9927.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Jeff Chung

![](images/9f769e06adda7eebee71aa1d3474d5fd843e01b528045d0b9fc0fac955934111.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>05-Nov-25 10:48:26</td><td>*2</td><td>*140.40</td><td>131.50</td></tr><tr><td>2</td><td>26-Feb-26 03:57:58</td><td>2</td><td>*98.90</td><td>93.60</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>3</td><td>10-Jun-26 05:07:18</td><td>2</td><td>*63.70</td><td>58.80</td></tr><tr><td>4</td><td>13-Jul-26 04:56:33</td><td>*3</td><td>*33.50</td><td>41.32</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Seres Group (601127.SS)

Ratings and Target Price History
Fundamental Research

Analyst: Jeff Chung

![](images/0993b343bb68e8aec14d5c80419ff6544d959493633150ed91728f3e37152ea2.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>24-Jun-24 06:23:05</td><td>*1</td><td>*124.10</td><td>95.23</td></tr><tr><td>2</td><td>18-Oct-24 07:02:36</td><td>1</td><td>*126.70</td><td>90.82</td></tr><tr><td>3</td><td>30-Oct-24 11:46:40</td><td>1</td><td>*143.90</td><td>109.46</td></tr><tr><td>4</td><td>22-Jan-25 00:59:36</td><td>1</td><td>*161.70</td><td>131.90</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>20-May-25 15:00:33</td><td>1</td><td>*165.50</td><td>130.50</td></tr><tr><td>6</td><td>30-Oct-25 10:38:34</td><td>*2</td><td>165.50</td><td>162.94</td></tr><tr><td>7</td><td>05-Nov-25 10:48:26</td><td>*3</td><td>*129.10</td><td>146.03</td></tr><tr><td>8</td><td>26-Feb-26 03:57:58</td><td>3</td><td>*88.10</td><td>106.08</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>10-Jun-26 05:07:18</td><td>3</td><td>*55.40</td><td>68.88</td></tr><tr><td>10</td><td>13-Jul-26 04:56:33</td><td>3</td><td>*37.40</td><td>53.91</td></tr></table>

Rating/target price changes above reflect Eastern Time

## BYD (002594.SZ)

Short-Term View/Catalyst Watch Research

Analyst: Jeff Chung

![](images/c5e7b0f33e8a5408c0a78ae2c1a816916d81c58b58e1c58050083d1dc93288b2.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>03-Oct-23 13:11:32</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>78.90</td></tr><tr><td>2</td><td>13-Mar-24 05:44:35</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>68.79</td></tr><tr><td>3</td><td>11-Jun-24 13:00:44</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>81.54</td></tr><tr><td>4</td><td>12-Jun-24 20:03:36</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>80.97</td></tr><tr><td>5</td><td>12-Jul-24 12:04:28</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>87.54</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>6</td><td>23-Sep-24 21:08:42</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>83.33</td></tr><tr><td>7</td><td>24-Oct-24 23:28:51</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>101.23</td></tr><tr><td>8</td><td>28-Oct-24 22:24:43</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>101.70</td></tr><tr><td>9</td><td>27-Jan-25 21:14:39</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>91.50</td></tr><tr><td>10</td><td>12-Nov-25 21:56:41</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>97.77</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>11</td><td>11-Feb-26 21:14:42</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>92.28</td></tr><tr><td>12</td><td>10-Apr-26 04:39:55</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>101.67</td></tr><tr><td>13</td><td>10-May-26 23:13:11</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>100.02</td></tr><tr><td>14</td><td>01-Jun-26 07:20:22</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>93.65</td></tr><tr><td>15</td><td>01-Jul-26 23:05:17</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>80.66</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/2eea3549f473bd89003113059e01d27720915d8bd4dfc64b955771f062e94b2b.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected D

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
