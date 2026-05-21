你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
19 May 2026 00:05:10 ET | 11 pages

# China Auto Manufacturers

Weekly EV Orders (Except NIO) continually missed (11-17 May)

# CITI'S TAKE

Weekly Orders continually missed: According to weekly orders, we estimate last week (11-17 May) China NEV orders improved by $4\%$ WoW with first 17-days daily average surging $7.9\%$ MoM which is not strong enough to improve Beta trend because: (1) If May full month NEV retail also up $8\%$ MoM, the implied YoY would still be negative at $-8\%$ YoY; (2) Inventory concerns (End-Apr Inventories estimate); (3) High variances between brands for WoW and MoM comparison enlarged to 56ppt and 87ppt, implying divergent growth trend among brands. BYD downside risk remains: Combining only Ocean and Dynasty brands, BYD's WoW $(-7\%)$ and MoM $(-19\%)$ trend both underperformed sector. While export growth may help to defend its 2Q earnings yet to be released by end-Aug, the May-July domestic growth momentum remains relatively un-exciting.

Xpeng/Tesla: Both registered daily average MoM at negative pace (-43%/-12%).

Nio/Li: Nio appears to be significantly outperforming at 48% MoM (113% WoW) with new product cycle; while Li's MoM at 6% after including new L9 orders provide limited visibility 2Q margin trend at this stage.

The only minor positive (April Orders-to-Sales; Figure 3): We estimate Apr26 NEV sector's orders-to-sales ratio was $1.59\mathrm{x}$ (10% YoY, 6% MoM) with BYD ratio up 9% YoY. However as sector also entered into down-cycle from May-2025, a slightly better order-to-sales ratio on YoY comparison this year could be irrelevant.

# Further readings:

NIO (NIO.N) – A ST Game Changer; 2Q margin visibility > BYD/Li/Xpeng/Leapmotor, Buy

Li Auto (LI.O) – Not A Game Changer; Maintain Neutral

Leapmotor (9863.HK) – Expect 2Q Breakeven, Lower FY26 GPM to 14.5%, Buy

BYD (1211.HK) – BYD Export MSRP & Discount Tracker (End-April)

BYD (1211.HK) – BYD inventory Update; Estimating Sales Volume Required to Deliver Positive YoY Growth in June

# Jeff Chung $^{AC}$

+852-2501-2787

jeff.m.chung@citi.com

# Kyle Wu

+852-2501-8483

kyle.wu@citi.com

Figure 1. Weekly Order 

<table><tr><td rowspan="3">Brands</td><td colspan="4">Apr-26</td><td colspan="3">May-26</td></tr><tr><td>1st week</td><td>2nd week</td><td>3rd week</td><td>4th week</td><td>1st week</td><td>2nd week</td><td>3rd week</td></tr><tr><td>30 Mar - 5 Apr</td><td>6 Apr - 12 Apr</td><td>13 Apr - 19 Apr</td><td>20 Apr - 26 Apr</td><td>27 Apr - 3 May</td><td>4 May - 10 May</td><td>11 May - 17 May</td></tr><tr><td>Li Auto</td><td>8.4k</td><td>9.3k</td><td>8.8k</td><td>8.2k</td><td>7.4k</td><td>6.3k</td><td>13.4k</td></tr><tr><td>Huawei Harmony</td><td>11.5k</td><td>11.2k</td><td>9.6k</td><td>64.3k</td><td>50.8k</td><td>28.4k</td><td>31.5k</td></tr><tr><td>Leapmotor</td><td></td><td></td><td></td><td>17.6k</td><td>18.8k</td><td>17.7k</td><td>12.7k</td></tr><tr><td>NIO (incl. ONVO)</td><td>10.4k</td><td>9.9k</td><td>9.6k</td><td>11.5k</td><td>9.9k</td><td>10.0k</td><td>21.3k</td></tr><tr><td>BYD</td><td>63.1k</td><td>53.0k</td><td>49.1k</td><td>47.5k</td><td>51.2k</td><td>43.7k</td><td>40.7k</td></tr><tr><td>Zeekr</td><td></td><td></td><td></td><td>19.2k</td><td>12.3k</td><td>9.0k</td><td>7.1k</td></tr><tr><td>Tesla</td><td>15.1k</td><td>15.8k</td><td>13.4k</td><td>13.3k</td><td>15.1k</td><td>13.7k</td><td>11.4k</td></tr><tr><td>Geely Galaxy</td><td></td><td></td><td></td><td>17.3k</td><td>16.7k</td><td>13.9k</td><td>13.4k</td></tr><tr><td>Xpeng (incl. Mona)</td><td>16.5k</td><td>9.1k</td><td>7.8k</td><td>6.8k</td><td>6.8k</td><td>6.3k</td><td>5.4k</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Citi Dealership Check

Figure 2. Weekly Order 

<table><tr><td></td><td>11-17 May single week WoW</td><td>Implied May 17-days daily avg. MoM</td></tr><tr><td>BYD (Ocean + Dynasty)</td><td>-7%</td><td>-19%</td></tr><tr><td>Huawei Harmony</td><td>11%</td><td>215%</td></tr><tr><td>Li Auto</td><td>113%</td><td>6%</td></tr><tr><td>Tesla</td><td>-17%</td><td>-12%</td></tr><tr><td>Nio</td><td>113%</td><td>48%</td></tr><tr><td>Xpeng</td><td>-14%</td><td>-43%</td></tr><tr><td>Zeekr</td><td>-21%</td><td>NA</td></tr><tr><td>Leapmotor</td><td>-28%</td><td>NA</td></tr><tr><td>Geely Galaxy</td><td>-4%</td><td>NA</td></tr><tr><td>EV Sector</td><td>4%</td><td>7.9%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Citi Dealership Check

Figure 3. Order-to-sales Summary 

<table><tr><td rowspan="2"></td><td colspan="4">Orders to Sales</td><td rowspan="2">Apr26 vs. Mar26</td><td rowspan="2">Apr26 vs. Apr25</td></tr><tr><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>2.60</td><td>1.39</td><td>1.59</td><td>1.47</td><td>-8%</td><td>9%</td></tr><tr><td>Tesla</td><td>1.98</td><td>0.86</td><td>1.11</td><td>2.36</td><td>113%</td><td>66%</td></tr><tr><td>Li Auto</td><td>0.86</td><td>0.56</td><td>0.67</td><td>1.09</td><td>64%</td><td>-7%</td></tr><tr><td>Huawei Harmony</td><td>0.73</td><td>0.72</td><td>1.75</td><td>3.71</td><td>113%</td><td>-6%</td></tr><tr><td>Leapmotor</td><td>1.59</td><td>-</td><td>-</td><td>-</td><td>na</td><td>na</td></tr><tr><td>Zeekr</td><td>0.88</td><td>-</td><td>-</td><td>-</td><td>na</td><td>na</td></tr><tr><td>NIO (incl. Onvo)</td><td>0.71</td><td>0.64</td><td>1.11</td><td>1.32</td><td>19%</td><td>6%</td></tr><tr><td>Xpeng (incl. Mona)</td><td>2.06</td><td>1.15</td><td>1.92</td><td>1.56</td><td>-19%</td><td>42%</td></tr><tr><td>Geely Galaxy</td><td>1.96</td><td>-</td><td>-</td><td>-</td><td>na</td><td>na</td></tr><tr><td>Xiaomi</td><td>0.36</td><td>0.50</td><td>2.71</td><td>0.92</td><td>-66%</td><td>-30%</td></tr><tr><td>Subtotal</td><td>1.44</td><td>1.01</td><td>1.50</td><td>1.59</td><td>6%</td><td>10%</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="4">Orders</td><td colspan="4">Retail Sales</td></tr><tr><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>200.4k</td><td>96.5k</td><td>252.2k</td><td>223.9k</td><td>77.2k</td><td>69.5k</td><td>158.4k</td><td>152.8k</td></tr><tr><td>Tesla</td><td>39.7k</td><td>32.6k</td><td>60.9k</td><td>61.9k</td><td>20.0k</td><td>37.9k</td><td>54.9k</td><td>26.2k</td></tr><tr><td>Li Auto</td><td>23.8k</td><td>14.6k</td><td>26.9k</td><td>36.4k</td><td>27.6k</td><td>26.0k</td><td>40.4k</td><td>33.4k</td></tr><tr><td>Huawei Harmony</td><td>40.4k</td><td>19.6k</td><td>45.6k</td><td>122.3k</td><td>55.6k</td><td>27.0k</td><td>26.1k</td><td>33.0k</td></tr><tr><td>Leapmotor</td><td>34.2k</td><td>na</td><td>na</td><td>na</td><td>21.5k</td><td>16.6k</td><td>37.6k</td><td>49.8k</td></tr><tr><td>Zeekr</td><td>16.8k</td><td>na</td><td>na</td><td>na</td><td>19.0k</td><td>14.7k</td><td>23.6k</td><td>23.1k</td></tr><tr><td>NIO (incl. Onvo)</td><td>21.1k</td><td>13.4k</td><td>38.2k</td><td>44.0k</td><td>29.9k</td><td>20.9k</td><td>34.5k</td><td>33.4k</td></tr><tr><td>Xpeng (incl. Mona)</td><td>32.7k</td><td>14.6k</td><td>41.6k</td><td>39.4k</td><td>15.9k</td><td>12.7k</td><td>21.7k</td><td>25.3k</td></tr><tr><td>Geely Galaxy</td><td>70.1k</td><td>na</td><td>na</td><td>na</td><td>35.8k</td><td>28.7k</td><td>61.8k</td><td>64.8k</td></tr><tr><td>Xiaomi</td><td>14.0k</td><td>10.2k</td><td>60.6k</td><td>33.5k</td><td>39.0k</td><td>20.3k</td><td>22.3k</td><td>36.6k</td></tr><tr><td>Subtotal (units)</td><td>493.1k</td><td>276.9k</td><td>721.6k</td><td>762.8k</td><td>341.6k</td><td>274.3k</td><td>481.3k</td><td>478.3k</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Citi Dealership Check, Thinkercar

# Companies Mentioned:

BYD (1211.HK; HK\$93.8; 1; 18 May 26; 16:10)   
BYD (002594.SZ; Rmb94.51; 1; 18 May 26; 15:00)   
Geely Automobile (0175.HK; HK\$20.58; 1; 18 May 26; 16:10)   
Leapmotor (9863.HK; HK\$41.68; 1; 18 May 26; 16:10)   
Li Auto (LI.O; US\$16.69; 2; 18 May 26; 16:00)   
Li Auto Inc (2015.HK; HK\$64.9; 2; 18 May 26; 16:10)   
NIO (NIO.N; US\$5.88; 1; 18 May 26; 16:00)   
NIO (9866.HK; HK\$47.54; 1; 18 May 26; 16:10)   
Xiaomi (1810.HK; HK\$30.66; 1; 18 May 26; 16:10)   
XPeng (XPEV.N; US\$15.06; 1; 18 May 26; 16:00)   
XPeng (9868.HK; HK\$60.65; 1; 18 May 26; 16:10)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

# Appendix A-1

# ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

# IMPORTANT DISCLOSURES

<table><tr><td>The Firm has made a market in the publicly traded equity securities of Li Auto Inc on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Geely Automobile Holdings Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of NIO Inc on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of BYD Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Zhejiang Leapmotor Technology Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Xiaomi Corp on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has a net short position of 0.5% or more of any class of common equity securities of Li Auto,NIO.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from BYD,Geely Automobile,Xiaomi.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from BYD,Geely Automobile,Li Auto,NIO,XPeng,Xiaomi in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): BYD,Geely Automobile,Xiaomi.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: BYD,Geely Automobile,Li Auto,NIO,XPeng,Xiaomi.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: BYD,Geely Automobile,Li Auto,NIO,XPeng,Xiaomi.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to BYD,XPeng,Xiaomi. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>The Firm is a market maker in the publicly traded equity securities of BYD,Geely Automobile,Leapmotor,Li Auto,NIO,Xiaomi.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.</td></tr></table>

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution 

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Apr 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>8%</td><td>37%</td><td>47%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>41%</td><td>28%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

# Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

# Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside 

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
