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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`Citi`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
01 Jul 2026 22:35:00 ET | 13 pages

## Kingboard Group

## The Largest Degree of Price Inflation on E-glass Fabric for Jul This Year

## CITI'S TAKE

Per F139 and company reports, we see the price of e-glass fabric for 1080 up by Rmb1.5 / m, 2116 by Rmb1.5 / m and 7628 by Rmb1.2 / m for July. See Fig 2. The extent of price inflation came in greater-than-expected at avg >Rmb0.5 per month during 2H26E. See Fig 1 for YTD price trend. Even though China Jushi kicked off new annual capacity of 390m meters (about 7-9% of total industry addition) of e-glass fabric in May, the price inflation in Jun and Jul remained quite robust without retreat. This implies the tight supply of e-glass fabric is more severe than expected due to some major players like Grace Fabric shifting into Al-fabric away from e-glass fabric and stronger-than-expected demand of Al-fabric. We prefer KBL (1888.HK) over KBH (0148.HK) as KBL should see higher degree of earnings upgrade and laminate remains the best performing segment at KBH.

Overhang on KBH is likely fading – KBH has underperformed KBL by \~15% since 18 Jun which was primarily led by Hallgain, the largest shareholder of KBH starting to sell shares through the market since 22 Jun for >6% stake. Click here for details – Kingboard Holdings (0148.HK) – Implication of Hallgain Share Disposal and Business Updates. We believe the share disposal is almost done, so the overhang for KBH may be fading.

Update on 96m capacity execution of e-glass fabric by KBL — Additionally, KBL commenced its new production facility with 96m annual capacity of e-glass fabric (mainly for 7628 and 1080) in the last week. The move will increase its monthly capacity by \~14% (from 57m meters to 65m meters) or the whole industry by \~2%. Mgmt suggested that 7628 may face more shortage than 1080 going forward due to the mix upgrade among major e-glass fabric suppliers. Thus, price inflation on % terms for the 7628 series should be more than for 1080 in the coming months, per mgmt. KBL skews toward 7628, with a 7628, 2116, and 1080 split of \~65%, \~5–10%, and \~25–30% of total e-glass fabric, respectively.

Market concern overbuild AI-infra may present a good buying opportunity – According to Reuters (1 July), Meta is planning to sell its excess computing power to outside customers. This may raise market concern the overbuild of AI-infra and may drag down the share price of KBH and KBL in the near term on sentiment. Having said that, we see KBL and KBH as having ample room for earnings upgrades during 2026-27E on their further expansion of AI-fabric by end-2026 and CCL potential certification into NVDA from mid-2027.

Eric Lau $^{AC}$ +852-2501-2726
eric.h.lau@citi.com

Alice Cai

+852-2501-2704

alice.cai@citi.com

Andy Li

+852-2501-2597

andy.li@citi.com

Figure 1. The largest degree of unit price inflation for July during YTD 2026  
![](images/96000dd14be1928275353e3b5f7d4867ed1c27e0a1da6036e8709cfcee916f27.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, F139 (a subsidiary of SCI99), Company Reports

<table><tr><td>Rmb / m</td><td>1080</td><td>2116</td><td>7628</td></tr><tr><td>Jan</td><td>0.70</td><td>0.60</td><td>0.20</td></tr><tr><td>Feb</td><td>0.60</td><td>0.60</td><td>0.60</td></tr><tr><td>Mar</td><td>0.80</td><td>0.70</td><td>0.50</td></tr><tr><td>Apr</td><td>0.95</td><td>1.00</td><td>0.20</td></tr><tr><td>May</td><td>0.75</td><td>0.70</td><td>0.55</td></tr><tr><td>Jun</td><td>0.95</td><td>0.85</td><td>0.70</td></tr><tr><td>Jul</td><td>1.50</td><td>1.50</td><td>1.20</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, F139 (a subsidiary of SCI99), Company Reports

## Kingboard Holdings

(0148.HK; HK\$117.9; 1; 30 Jun 26; 16:10)

## Valuation

Our HK\$202 target price is based on a PE-based sum-of-the-parts (SOTP) valuation methodology. We employ SOTP valuation given KB's different business lines, implying \~19x 2027E PE for the group which is +4SD above its mean; we believe this is justified by the business upcycle in both laminate and PCB businesses. In our SOTP, we value the Laminate at 29x PE (+3SD for PE peak over industry mid-cycle which is in line with our TP target of KBL), PCB at 16x PE (about half of regional comps avg for KB without entry into NVDA chain but most regional comps do) and Chemical at 6x (\~50% discount to Asian comps on account of smaller scale). For valuing the Property segment, we assume average 7% rental yield per current return for estimating the NAV of its rental property portfolio and property book value of HK\$12.2bn in 2026E. Our target price translates into \~19x 2027E P/E, which is +4SD over its historical mean since 2011 (range: 4.4x to 24.4x). Our target price translates into 3x 2027E book value, which is still well below regional comps average of 7x PB.

## Risks

We see the following risks that could impede the stock from reaching our target price: 1) slower-than-expected AI-CCL and AI-PCB contribution, 2) slower-than-expected consumption recovery could drag consumption of electronic goods/big ticket items like autos, home appliances, and smartphones, 3) lower-than-expected GDP growth in China; and 4) lower-than-expected oil prices.

## Kingboard Laminates Holdings

(1888.HK; HK\$99.15; 1; 30 Jun 26; 16:10)

## Valuation

Our target price for KBL shares of HK\$120 is based on a \~29x P/E for 2027E, at 3SD over mean, which is even higher than its historical cycle peak between +1SD and +2SD, to reflect the growing % of its AI-fabric new business from 2H26E which should trigger re-rating along with further earnings upgrade possibility on e-glass fabric given higher run rate of price inflation in June. We employ +3SD reflecting recent kickoff of three kilns on AI-fabric from 2Q26. We think the premium is justified as we expect a continued GM expansion cycle during 2026E-28E along with potential earnings upgrades given KBL would expand its customer base for AI-fabric under the NVDA and ASIC ecosystem this year. We think a PE methodology appropriately captures the company's medium-term operating performance. Our target price translates to 0.3x PEG (regional comp around 0.6x) backed by strong three-year earnings CAGR of 92% thru 2028E. We think this appears undemanding compared with regional CCL comps.

## Risks

Upside/downside risks that could cause the stock to exceed/underperform our target price include: 1) faster/ slower-than-expected demand on upstream materials such as glass fabric and copper foil on AI-related products; 2) China macro growth performs faster/slower-than-expected; 3) stronger/weaker-than-expected stimulus policies in China; or 4) recovery/weakness in end-demand of electronic goods.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

![](images/c40053e92ef0cc51e17753e5da295152e9fcf97fe8ccebe2927db520a0f26c52.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>28-Aug-23 11:03:13</td><td>1</td><td>*9.95</td><td>6.22</td></tr><tr><td>2</td><td>18-Mar-24 13:55:33</td><td>1</td><td>*8.16</td><td>6.00</td></tr><tr><td>3</td><td>20-May-24 16:10:28</td><td>1</td><td>*12.44</td><td>8.50</td></tr><tr><td>4</td><td>26-Aug-24 12:52:14</td><td>1</td><td>*11.45</td><td>6.67</td></tr><tr><td>5</td><td>24-Mar-25 13:48:33</td><td>1</td><td>*13.94</td><td>9.23</td></tr></table>

\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>25-Aug-25 14:05:25</td><td>1</td><td>*20.41</td><td>12.24</td></tr><tr><td>7</td><td>23-Feb-26 11:49:32</td><td>1</td><td>*27.87</td><td>20.29</td></tr><tr><td>8</td><td>16-Mar-26 17:59:34</td><td>1</td><td>*29.86</td><td>22.10</td></tr><tr><td>9</td><td>22-Apr-26 09:32:35</td><td>1</td><td>*42.80</td><td>30.72</td></tr><tr><td>10</td><td>03-May-26 18:02:15</td><td>1</td><td>*50.77</td><td>34.54</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>11</td><td>25-May-26 19:33:53</td><td>1</td><td>*65.70</td><td>50.87</td></tr><tr><td>12</td><td>03-Jun-26 08:03:10</td><td>1</td><td>*75.65</td><td>54.00</td></tr><tr><td>13</td><td>08-Jun-26 10:05:51</td><td>1</td><td>*79.63</td><td>55.69</td></tr><tr><td>14</td><td>14-Jun-26 17:16:22</td><td>1</td><td>*100.00</td><td>65.60</td></tr><tr><td>15</td><td>18-Jun-26 00:33:31</td><td>1</td><td>*120.00</td><td>91.85</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Kingboard Holdings (0148.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Eric Lau

![](images/85ea1ea765ccda74d2f17a913a2ba9f180a2b393add512feef9ea070ef6de77d.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>28-Aug-23 12:55:58</td><td>1</td><td>*34.95</td><td>16.66</td></tr><tr><td>2</td><td>18-Mar-24 21:59:40</td><td>1</td><td>*29.87</td><td>15.89</td></tr><tr><td>3</td><td>26-Aug-24 13:55:22</td><td>1</td><td>*26.88</td><td>15.93</td></tr><tr><td>4</td><td>25-Mar-25 03:36:46</td><td>1</td><td>*29.47</td><td>21.06</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>25-Aug-25 19:02:21</td><td>1</td><td>*35.84</td><td>27.70</td></tr><tr><td>6</td><td>23-Feb-26 11:50:02</td><td>1</td><td>*44.80</td><td>36.66</td></tr><tr><td>7</td><td>18-Mar-26 10:55:00</td><td>1</td><td>*47.79</td><td>39.41</td></tr><tr><td>8</td><td>07-May-26 19:05:58</td><td>1</td><td>*64.71</td><td>48.41</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>03-Jun-26 13:30:12</td><td>1</td><td>*89.60</td><td>62.47</td></tr><tr><td>10</td><td>21-Jun-26 20:40:54</td><td>1</td><td>*202.00</td><td>126.60</td></tr></table>

Rating/target price changes above reflect Eastern Time

<table><tr><td rowspan="2" colspan="2">Date</td><td rowspan="2">Action</td><td rowspan="2">ExpectedDirection</td><td colspan="2">ClosingPrice</td><td rowspan="2" colspan="2">Date</td><td rowspan="2">ExpectedDirection</td><td rowspan="2" colspan="2">ClosingPrice</td><td rowspan="2" colspan="2">Date</td><td rowspan="2">ExpectedDirection</td><td rowspan="2" colspan="2">ClosingPrice</td></tr><tr><td>90 Days</td><td>7.63</td></tr><tr><td>1</td><td>13-Jun-24 06:22:03</td><td>Add CW</td><td>Upside</td><td></td><td></td><td>4</td><td>07-Nov-25 12:06:35</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>11.85</td><td>7</td><td>03-May-26 14:02:15</td><td>Add CW</td><td>90 Days</td></tr><tr><td>2</td><td>11-Sep-24 00:14:59</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>5.59</td><td>5</td><td>14-Jan-26 03:04:03</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>12.40</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>09-Oct-25 07:10:54</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>12.56</td><td>6</td><td>13-Feb-26 12:13:30</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>19.29</td><td></td><td></td><td></td><td></td></tr></table>

![](images/6911129258314f15d14a6e877bcb7fdef4131b018054761e0aab097379014bc3.jpg)

<table><tr><td rowspan="2"></td><td rowspan="2">Date</td><td rowspan="2">Action</td><td colspan="2">Expected</td><td rowspan="2">Closing Price</td></tr><tr><td>Direction</td><td>Duration</td></tr><tr><td>1</td><td>21-Jun-26 16:40:54</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>126.60</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

![](images/0703f0d7557c9628fc4034cb125a39e1db41f7f4dfd27d98387a6efbddedf28a.jpg)  
CW - Catalyst Watch, STV - Short-Term View

![](images/0d28985518e99e5b3e3c675b2e3d10a38746256e33fcb906a755e8db94c562e5.jpg)  
Rating/target price changes above reflect Eastern Time

The Firm has made a market in the publicly traded equity securities of Kingboard Laminates Holdings Ltd on at least one occasion since 1 Jan 2025.

The Firm has made a market in the publicly traded equity securities of Kingboard Holdings Ltd on at least one occasion since 1 Jan 2025.

Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Kingboard Laminates Holdings.

Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Kingboard Holdings, Kingboard Laminates Holdings.

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Kingboard Holdings, Kingboard Laminates Holdings in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Kingboard Holdings, Kingboard Laminates Holdings.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Kingboard Holdings, Kingboard Laminates Holdings.
Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Kingboard Holdings, Kingboard Laminates Holdings.

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target pri

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective

investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
