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

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>5</td><td>16-Aug-24 07:31:42</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>4.43</td></tr><tr><td>6</td><td>16-Sep-24 00:14:55</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>4.67</td></tr><tr><td>7</td><td>15-Oct-24 14:49:20</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>6.10</td></tr><tr><td>8</td><td>29-Oct-24 06:06:17</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>5.53</td></tr></table>

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>9</td><td>02-Jun-25 06:34:49</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>4.59</td></tr><tr><td>10</td><td>03-Jul-25 00:22:45</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>5.48</td></tr><tr><td>11</td><td>14-Apr-26 04:28:27</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>12.68</td></tr><tr><td>12</td><td>15-May-26 00:28:25</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>10.54</td></tr></table>

Rating/target price changes above reflect Eastern Time

## China Hongqiao (1378.HK)

Short-Term View/Catalyst Watch Research

Analyst: Jack Shang, CFA

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>22-May-24 04:40:28</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>11.84</td></tr><tr><td>2</td><td>21-Jun-24 00:25:11</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>12.22</td></tr><tr><td>3</td><td>16-Jul-24 14:50:56</td><td>Add CW</td><td>Downside</td><td>30 Days</td><td>10.64</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

![](images/f43f685fae9c3ca29a14d5c2cb02f4f69068839956e6b3441d27139894f0b115.jpg)

<table><tr><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>17-Jan-25 04:11:17</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>12.68</td></tr><tr><td>16-Feb-25 22:14:31</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>12.58</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/3e52aa4c22bd4ae1abb418b1b0b1da46ba1789fe74d1829ecdefaf464b282cd7.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>1</td><td>16-Jul-24 14:50:56</td><td>Add CW</td><td>Downside</td><td>30 Days</td><td>7.91</td><td>3</td><td>15-Oct-24 14:49:20</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>8.51</td><td>5</td><td>14-Apr-26 04:27:40</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>12.46</td></tr><tr><td>2</td><td>15-Aug-24 23:12:08</td><td>Remove CW</td><td>Downside</td><td>30 Days</td><td>6.55</td><td>4</td><td>31-Oct-24 08:03:43</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>7.63</td><td>6</td><td>14-May-26 23:28:26</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>11.61</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View 

[中间内容因长度限制已省略]

tives, financial situation or needs of any particular investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.
"""
