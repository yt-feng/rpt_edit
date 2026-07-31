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
29 Jul 2026 01:47:13 ET | 13 pages

# BYD (1211.HK)

## Fundamentals, AI-Fund Flows, BYD Robots update

## CITI'S TAKE

We note 1) China July NEV retail YoY forecast this week was better than last week (July EV Orders Tracking at -9% MoM (EV Retail at -6.8% YoY), 2) BYD orders (+0% WoW/-10% MTD-MoM) stabilized after factoring in high base from last month, 3) BYD weekly wholesale greatly improved from -13% MTD-MoM last week to -1% MTD-MoM this week per CPCA data; On the other hand we note the share prices of AI & CV names (Weichai/Generac/Bloom Energy/Sinotruk Index, see Fig 3) further declined -26% MoM/ -10% WoW, suggesting fund flow unwinding to continue. We therefore adjust our July forecast on BYD after factoring in factual data from above and generate the following outputs below (Figure 1-3): We expect BYD's weighted-fundamental index to stay at steady-state (i.e. at 0 when not improving or worsening). PIs also refer to last week's update: BYD (1211.HK) - Fundamentals vs Fund-Flow Dashboard

BYD 2Q earnings: After almost a full month of fund flow unwinding, we expect 2Q earnings release in Aug will be critical (i.e. 2Q NP Rmb9-10b range) in order to prove (1) Whether BYD have been making profit or loss in the domestic China EV market; (2) Whether BYD domestic China EV market share can recover; (3) If the domestic market carries no losses for BYD, a 2.7m units export in FY27 would warrant over Rmb5bn NP.

ChangXin (CXMT)/Horizon Robotics further boosts China PV export strength: The positive sentiment recently on Changxin, as well as Horizon Robotics' L3/L4 partnership with VW indicates China Auto exports (BYD/Geely/Chery/Nio/Xpeng/Leapmotor) may further gain edges on cost-reduction and R&D cadences from their international peers by including new variables (China semi & ADAS supplies).

BYD Robots: On BYD's Humanoid Robots announcement in Aug (TMTPOST, 28-Jul-2026), from a big picture prospective we believe it should be potentially LT earnings accretive to major auto makers because (1) Unitree's FY25 full CAPEX was only <0.5% of BYD; (2) Unitree made >60% GPM FY25 versus major auto makers 10-20% range; and (3) auto parts and Humanoid robot parts production and development could be 60-80% overlapped, while ADAS/Robotaxi algorithm and Humanoid/Robotics algorithm can also be built from the same platforms with similar sensor fusions. That said, we do not see any reason as to why auto makers should not engage in Humanoid Robotic development at an aggressive pace.

<table><tr><td colspan="2">Buy</td></tr><tr><td>Price (28 Jul 26 16:10)</td><td>HK$89.80</td></tr><tr><td>Target price</td><td>HK$142.00</td></tr><tr><td>Expected share price return</td><td>58.1%</td></tr><tr><td>Expected dividend yield</td><td>1.7%</td></tr><tr><td>Expected total return</td><td>59.8%</td></tr><tr><td>Market Cap</td><td>HK$818,724MUS$104,418M</td></tr></table>

Jeff Chung $^{AC}$ +852-2501-2787
jeff.m.chung@citi.com

+852-2501-8483

kyle.wu@citi.com

## See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

## Stock calls:

Defensive LT Buys: Chery, Geely, Minth

High-beta upside swing potential into car sales high season: Leapmotor, Xpeng

2Q & 2H earnings re-rating potential from export: BYD/Weichai/Sinotruk/Yutong

Sells: Seres, Great Wall; Neutral on Li Auto, Sanhua and Tuopu

Figure 1. BYD weighted-fundamental index

<table><tr><td></td><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td><td>MTD Jul</td></tr><tr><td>BYD inventory MoM movement (LHS)</td><td>1.3%</td><td>0.6%</td><td>-1.1%</td><td>1.1%</td><td>6.8%</td><td>1.7%</td><td>-6.0%</td></tr><tr><td>BYD export MoM movement (LHS)</td><td>-24.5%</td><td>0.1%</td><td>19.4%</td><td>12.5%</td><td>18.9%</td><td>9.2%</td><td>5.5%</td></tr><tr><td>China NEV sector retail YoY (LHS)</td><td>-19.7%</td><td>-34.5%</td><td>-17.6%</td><td>-6.0%</td><td>-5.2%</td><td>-9.9%</td><td>-6.8%</td></tr><tr><td>BYD orders MoM movement (RHS)</td><td>-36.7%</td><td>-51.8%</td><td>161.2%</td><td>-11.2%</td><td>-11.9%</td><td>49.7%</td><td>-5.0%</td></tr><tr><td>BYD Weekly wholesale implied full month wholesale MoM</td><td></td><td></td><td></td><td></td><td></td><td></td><td>3.0%</td></tr><tr><td>BYD weighted-fundamental index</td><td>-17.3%</td><td>-12.3%</td><td>51.0%</td><td>6.0%</td><td>8.0%</td><td>19.4%</td><td>0.0%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi Estimates, Company Reports, CPCA

Figure 2. BYD fundamentals and its H share price movement  
![](images/f3a86fa7450ad9520d4b98f659f52e633fb50d4f1b65e3fa3f9586607e404a7f.jpg)  
BYD weighted-fundamental index (LHS) BYD-H share price movement MoM (RHS)  
Source: Citi, Company Reports, CPCA  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 3. YTD share price movements of BYD and AIDC/SOFC/HDT players  
![](images/f21dc13e2ccd52c7878d74ec64ec97e9879235767000bacc3d781ae1cf2c31fb.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Bloomberg

## Companies Mentioned:

BYD (1211.HK; HK\$89.8; 1; 28 Jul 26; 16:10)
Bloom Energy Corp (BE.N; US\$166.84; 2H; 28 Jul 26; 16:00)
BYD (002594.SZ; Rmb93.35; 1; 28 Jul 26; 15:00)
Chery (9973.HK; HK\$24.66; 1; 28 Jul 26; 16:10)
CXMTCorp (688825.SS; Rmb47.0; Not Rated; 28 Jul 26; 15:00)
Geely Automobile (0175.HK; HK\$19.12; 1; 28 Jul 26; 16:10)
Generac Holdings (GNRC.N; US\$195.6; 2H; 28 Jul 26; 16:00)
Great Wall Motor (2333.HK; HK\$8.96; 3; 28 Jul 26; 16:10)
Great Wall Motor (601633.SS; Rmb16.43; 3; 28 Jul 26; 15:00)
Horizon Robotics (9660.HK; HK\$5.0; 1H; 28 Jul 26; 16:10)
Leapmotor (9863.HK; HK\$38.52; 1; 28 Jul 26; 16:10)
Li Auto (LI.O; US\$13.21; 2; 28 Jul 26; 16:00)
Li Auto Inc (2015.HK; HK\$49.68; 2; 28 Jul 26; 16:10)
Minth (0425.HK; HK\$26.5; 1; 28 Jul 26; 16:10)
Ningbo Tuopu Group (601689.SS; Rmb45.6; 2; 28 Jul 26; 15:00)
NIO (NIO.N; US\$4.68; 1; 28 Jul 26; 16:00)
NIO (9866.HK; HK\$36.98; 1; 28 Jul 26; 16:10)
Sanhua (2050.HK; HK\$24.96; 2; 28 Jul 26; 16:10)
Seres Group (601127.SS; Rmb55.93; 3; 28 Jul 26; 15:00)
Seres Group (9927.HK; HK\$43.16; 3; 28 Jul 26; 16:10)
Sinotruk (Hong Kong) (3808.HK; HK\$40.08; 1; 28 Jul 26; 16:10)
Volkswagen (VOWG\_p.DE; €73.92; 1; 28 Jul 26; 17:30)
Weichai Power (2338.HK; HK\$30.92; 1; 28 Jul 26; 16:10)
XPeng (XPEV.N; US\$12.71; 1; 28 Jul 26; 16:00)
XPeng (9868.HK; HK\$49.56; 1; 28 Jul 26; 16:10)
Yutong Bus (600066.SS; Rmb32.85; 1; 28 Jul 26; 15:00)
Zhejiang Sanhua Intelligent Controls (002050.SZ; Rmb35.58; 2; 28 Jul 26; 15:00)

## BYD

## Valuation

By applying 1.2x 2026E PEG on a +25% 2026-28E NP CAGR, we derive our TP of HK\$142, implying 30x/25x 2026E/27E PER. We adopt PEG valuation, as we believe it can more accurately reflect the valuation of this growth stock.

## Risks

Key downside risks that could prevent the BYD H-share from reaching our target price include: 1) weaker-than-expected NEV bus or PV sales; 2) a slower-than-expected ramp-up of the Skyrail business; 3) another prolonged capex cycle; and 4) unexpected cash flow issues.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analyst: Jeff Chung

![](images/a9239f887886d8efcdbbf5e1d9988a6312a58138c07c58c2022d83cd1db7c0c2.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>11-Jan-24 13:28:07</td><td>1</td><td>*154.33</td><td>70.80</td></tr><tr><td>2</td><td>29-May-24 07:27:17</td><td>1</td><td>*158.33</td><td>72.53</td></tr><tr><td>3</td><td>01-Sep-24 20:09:08</td><td>1</td><td>*162.67</td><td>80.40</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>30-Oct-24 11:36:39</td><td>1</td><td>*166.67</td><td>98.33</td></tr><tr><td>5</td><td>14-Feb-25 11:26:49</td><td>1</td><td>*229.33</td><td>121.40</td></tr><tr><td>6</td><td>20-May-25 14:45:04</td><td>1</td><td>*242.33</td><td>148.20</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>7 13-Jun-25 00:00:04</td><td>1</td><td>*233.00</td><td>131.10</td></tr><tr><td>8 07-Sep-25 20:44:21</td><td>1</td><td>*174.00</td><td>105.60</td></tr><tr><td>9 30-Mar-26 12:12:39</td><td>1</td><td>*142.00</td><td>105.80</td></tr></table>

Rating/target price changes above reflect Eastern Time

## BYD (1211.HK)

Short-Term View/Catalyst Watch Research

Analyst: Jeff Chung

![](images/28f43e3b251adb9e8e55950dd122280a012a02d33ed8d0b3167f49f5ed7d5308.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>03-Oct-23 00:16:29</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>79.53</td></tr><tr><td>2</td><td>12-Mar-24 15:43:32</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>69.87</td></tr><tr><td>3</td><td>11-Jun-24 00:18:43</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>76.13</td></tr><tr><td>4</td><td>12-Jun-24 06:02:24</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>73.33</td></tr><tr><td>5</td><td>12-Jul-24 00:12:00</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>82.20</td></tr><tr><td>6</td><td>13-Aug-24 21:14:13</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>71.00</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>7</td><td>13-Sep-24 14:17:22</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>79.93</td></tr><tr><td>8</td><td>23-Sep-24 21:08:42</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>80.13</td></tr><tr><td>9</td><td>25-Oct-24 00:28:51</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>97.53</td></tr><tr><td>10</td><td>28-Oct-24 22:24:43</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>98.20</td></tr><tr><td>11</td><td>12-Jan-25 22:48:43</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>83.80</td></tr><tr><td>12</td><td>12-Nov-25 21:56:41</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>100.50</td></tr></table>

<table><tr><td rowspan="2" colspan="2">Date</td><td rowspan="2">Action</td><td rowspan="2">Expected Direction</td><td rowspan="2">Duration</td><td rowspan="2">Closing Price</td></tr><tr></tr><tr><td>13</td><td>11-Feb-26 22:14:43</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>99.15</td></tr><tr><td>14</td><td>10-Apr-26 04:39:55</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>105.10</td></tr><tr><td>15</td><td>11-May-26 00:13:29</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>101.70</td></tr><tr><td>16</td><td>01-Jun-26 07:20:22</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>90.75</td></tr><tr><td>17</td><td>02-Jul-26 00:35:24</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>78.30</td></tr></table>

Rating/target price changes above reflect Eastern Time

<table><tr><td>The Firm has made a market in the publicly traded equity securities of Great Wall Motor Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Li Auto Inc on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of NIO Inc on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Horizon Robotics on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Zhejiang Leapmotor Technology Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Geely Automobile Holdings Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Zhejiang Sanhua Intelligent Controls Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates beneficially owns 1% or more of any class of common equity securities of Zhejiang Sanhua Intelligent Controls. This position reflects information available as of the prior business day.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has a net short position of 0.5% or more of any class of common equity securities of Li Auto,NIO.</td></tr><tr><td>Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Bloom Energy Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Bloom Energy Corp,Chery,Geely Automobile,Sinotruk (Hong Kong),Volkswagen,XPeng.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from Chery,Sinotruk (Hong Kong),Volkswagen.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from BYD,Bloom Energy Corp,Chery,Geely Automobile,Generac Holdings,Great Wall Motor,Horizon Robotics,Li Auto,Minth,NIO,Ningbo Tuopu Group,Seres Group,Sinotruk (Hong Kong),Volkswagen,Weichai Power,XPeng,Yutong Bus,Zhejiang Sanhua Intelligent Controls in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Bloom Energy Corp,Chery,Geely Automobile,Sinotruk (Hong Kong),Volkswagen,XPeng.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: BYD,Bloom Energy Corp,Chery,Geely Automobile,Great Wall Motor,Li Auto,Minth,NIO,Ningbo Tuopu Group,Seres Group,Sinotruk (Hong Kong),Volkswagen,XPeng,Zhejiang Sanhua Intelligent Controls.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 1

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
