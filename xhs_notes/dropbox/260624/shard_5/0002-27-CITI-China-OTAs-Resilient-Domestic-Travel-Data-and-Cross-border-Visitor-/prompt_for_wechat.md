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
## China OTAs

Resilient Domestic Travel Data and Cross-border Visitor Volume During Dragon Boat Festival

## CITI'S TAKE

China's MCT reported travel traffic and industry revenues during the 3-day Dragon Boat Festival of 124mn/Rmb44.5bn, +4.4/+4% yoy growth, implying average spending -0.4% yoy. The national passenger throughput recorded 0.9% yoy decline during the holiday with railway/airline/roadway/waterway +2.9/+0.6/-1.2/-1.8% yoy. China's Immigration Department reported cross-border visitor volume was up 12.9% yoy with Chinese citizen volume up 5.5% yoy, which is in line with the Immigration's projection prior to the holiday. Albeit national passenger throughput data a bit weak, we view overall domestic revs and traffic performance resilient, especially considering the surging airline ticketing price and heavy rain during the holiday, while cross-border data for Chinese citizens also looks resilient despite the oil price impact. Nonetheless, TCOM is scheduled to release its 1Q26 results on 25 Jun HKT, and we expect conservative tone on 2Q26E likely from mgmt given the potential impacts from oil price and investigation. Maintain Buy ratings on TCOM/Tongcheng.

Details of transportation and cross-border data – During the 3-day holiday, national passenger throughput reached 647.9mn, representing -0.9% yoy, with railway/airline/roadway/waterway +2.9/+0.6/-1.2/-1.8% yoy, respectively, according to data from Ministry of Transport. The data shows the overall passenger throughput likely impacted by heavy rain across China, especially for roadway, while railway performance was relatively more resilient vs. airline which might be dragged by higher airline ticketing prices. Cross-border visitor volume was up 12.9% yoy with Chinese citizens/HK & Macau & Taiwan residents/foreigners volume up 5.5/18.4/23.3% yoy, which performance was resilient especially considering surging oil price impact.

More color from OTAs – TCOM: Trip.com data indicates that during the Dragon Boat Festival holiday, popular major cities and “hidden gem” small towns were top destinations, with female travelers and the post-90s generation leading the trend, predominantly opting for inter-provincial short trips (pls click link, 100EC.cn, 22-Jun 26). Tongcheng: Tongcheng indicates that during the Dragon Boat Festival holiday, short-distance “micro-vacations” remained popular, especially in the Jiangsu, Zhejiang, and Shanghai region, with a growing trend towards “hidden gem” small towns and “village-drifting” tourism for relaxed experiences. (pls click link, SinaNews, 22-Jun 26). Fliggy: Fliggy indicated a significant increase in per capita booking value and hotel stays during the Dragon Boat Festival, driven by consumers’ preference for quality travel and a surge in demand for summer escape and grassland tours in Northwest and Northeast regions. (pls click link, TheCover, 22-Jun 26).

Brian Gong $^{AC}$ +852-2501-2747
brian.gong@citi.com

Alicia Yap, CFA
+852-2501-2773
alicia.yap@citi.com

Nelson Cheung
nelson.cheung@citi.com

Figure 1. Dragon Boat festival travel data in 2026

<table><tr><td></td><td>2025 New Year</td><td>2025 CNY</td><td>2025 Qingming</td><td>2025 Labour Day</td><td>2025 Dragon Boat</td><td>2025 National Day</td></tr><tr><td>Domestic visitor volume (mn)</td><td>135</td><td>501</td><td>126</td><td>314</td><td>119</td><td>888</td></tr><tr><td>yoy growth %</td><td>9.4%</td><td>5.9%</td><td>6.3%</td><td>6.4%</td><td>5.7%</td><td>16.1%</td></tr><tr><td>Domestic tourism revs (Rmb bn)</td><td>77</td><td>677</td><td>58</td><td>180</td><td>43</td><td>809</td></tr><tr><td>yoy growth %</td><td>na</td><td>7.0%</td><td>6.7%</td><td>8.0%</td><td>5.9%</td><td>15.4%</td></tr><tr><td>Average Spending (Rmb)</td><td>567</td><td>1,351</td><td>457</td><td>574</td><td>359</td><td>911</td></tr><tr><td>yoy growth %</td><td>na</td><td>1.0%</td><td>0.4%</td><td>1.5%</td><td>0.2%</td><td>-0.6%</td></tr></table>

<table><tr><td></td><td>2026 New Year</td><td>2026 CNY</td><td>2026 Qingming</td><td>2026 Labour Day</td><td>2026 Dragon Boat</td></tr><tr><td>Domestic visitor volume (mn)</td><td>142</td><td>596</td><td>135</td><td>325</td><td>124</td></tr><tr><td>yoy growth %</td><td>2.6%</td><td>19.0%</td><td>6.8%</td><td>3.6%</td><td>4.4%</td></tr><tr><td>Domestic tourism revs (Rmb bn)</td><td>85</td><td>803</td><td>61</td><td>185</td><td>44</td></tr><tr><td>yoy growth %</td><td>3.1%</td><td>18.7%</td><td>6.6%</td><td>2.9%</td><td>4.0%</td></tr><tr><td>Average Spending (Rmb)</td><td>597</td><td>1,348</td><td>455</td><td>571</td><td>359</td></tr><tr><td>yoy growth %</td><td>-1.0%</td><td>-0.2%</td><td>-0.2%</td><td>-0.7%</td><td>-0.4%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Ministry of Culture and Tourism, Citi

Figure 2. National passenger throughput data during Dragon Boat Festival

<table><tr><td>Dragon Boat Festivel</td><td>Date</td><td>Railway</td><td>yoy</td><td>Airline</td><td>yoy</td><td>Roadway</td><td>yoy</td><td>Waterway</td><td>yoy</td><td>Total</td><td>yoy</td></tr><tr><td>The day before the holiday</td><td>18-Jun</td><td>16.7</td><td>6.1%</td><td>2.2</td><td>0.1%</td><td>196.5</td><td>7.2%</td><td>0.6</td><td>-5.7%</td><td>216.0</td><td>7.0%</td></tr><tr><td>1st day</td><td>19-Jun</td><td>19.4</td><td>6.9%</td><td>1.9</td><td>0.0%</td><td>209.3</td><td>-0.3%</td><td>0.9</td><td>-10.1%</td><td>231.4</td><td>0.2%</td></tr><tr><td>2nd day</td><td>20-Jun</td><td>12.1</td><td>2.0%</td><td>1.7</td><td>-2.6%</td><td>186.3</td><td>-2.1%</td><td>1.0</td><td>0.8%</td><td>201.2</td><td>-1.8%</td></tr><tr><td>3rd day</td><td>21-Jun</td><td>17.9</td><td>-0.5%</td><td>2.1</td><td>3.9%</td><td>194.5</td><td>-1.3%</td><td>0.8</td><td>5.4%</td><td>215.3</td><td>-1.2%</td></tr><tr><td>Total 3 days during the holiday</td><td></td><td>49.4</td><td>2.9%</td><td>5.7</td><td>0.6%</td><td>590.1</td><td>-1.2%</td><td>2.7</td><td>-1.8%</td><td>647.9</td><td>-0.9%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: Citi, Ministry of Transport

## Tongcheng Travel Holdings

(0780.HK; HK\$13.12; 1; 22 Jun 26; 16:10)

## Valuation

We believe PE is appropriate to value Tongcheng to capture strong growth momentum and is consistent with our valuation methodology for its peers. Our target price of HK\$25 is based on 14x non-IFRS 2026E EPS, set at a discount to the historical average of 21x before the pandemic given a slower revs growth profile.

## Risks

Key risks that may prevent the share price from reaching our target price include: 1) greater-than-expected competition from OTA peers or other traveling booking channels; 2) heavy reliance on hotel supply from Trip.com; 3) heavy reliance on Tencent's platforms; and 4) worsening macro.

## Trip.com Group Ltd

(TCOM.O; US\$45.1; 1; 18 Jun 26; 16:00)

## Valuation

Our target price of US\$82 for Trip.com is based on SOTP. We value the core business at \~US\$76/sh based on a 2026E P/E of 20x, applying a 20% premium to the average P/E of other vertical leaders given TCOM's structural overseas expansion story. We apply the target multiple to TCOM's 2026E adj. earnings excluding the profits from equity investments. We value the major equity investments at \~US\$6/sh based on the market caps of the listed names. We employ an SOTP approach to better factor in the value of the investments.

## Risks

Downside risks that could prevent the shares from reaching our target price include: 1) a further softening of the China macro environment that affects travel demand; 2) travel demand taking longer than expected to recover; 3) spending and margins turning worse than expected; 4) an intensification of domestic competition; and 5) any significant new outbreaks of Covid-19 or other epidemics.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Trip.com Group Ltd (TCOM)
Ratings and Target Price History
Fundamental Research

Analyst: Brian Gong

![](images/1ecb3c5fb544510d4edd1bb50e491d91633ee4ce1f0c354bf1b85ebe9b38d5b3.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>05-Sep-23 07:30:07</td><td>1</td><td>*49.00</td><td>38.26</td></tr><tr><td>2</td><td>22-Feb-24 07:20:06</td><td>1</td><td>*53.00</td><td>44.67</td></tr><tr><td>3</td><td>01-Apr-24 08:03:49</td><td>1</td><td>*55.00</td><td>46.96</td></tr><tr><td>4</td><td>21-May-24 07:19:17</td><td>1</td><td>*66.00</td><td>55.83</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>09-Oct-24 11:57:16</td><td>1</td><td>*72.00</td><td>62.39</td></tr><tr><td>6</td><td>19-Nov-24 08:50:04</td><td>1</td><td>*73.00</td><td>62.74</td></tr><tr><td>7</td><td>02-Jan-25 23:25:44</td><td>1</td><td>*78.00</td><td>64.77</td></tr><tr><td>8</td><td>25-Feb-25 11:46:46</td><td>1</td><td>*75.00</td><td>57.30</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td></td><td>20-May-25 06:27:17</td><td>1</td><td>*78.00</td><td>63.38</td></tr><tr><td></td><td>28-Aug-25 11:14:59</td><td>1</td><td>*85.00</td><td>75.03</td></tr><tr><td></td><td>18-Nov-25 07:03:01</td><td>1</td><td>*86.00</td><td>72.44</td></tr><tr><td></td><td>29-Jan-26 09:42:02</td><td>1</td><td>*82.00</td><td>62.02</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Tongcheng Travel Holdings (0780.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Brian Gong

![](images/be7501c05fb568914b78ab2ee90c5171d72040167f35d73d6a778504387f5752.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>22-Aug-23 17:18:07</td><td>1</td><td>*25.00</td><td>17.20</td></tr><tr><td>2</td><td>17-Apr-24 12:59:49</td><td>1</td><td>*26.00</td><td>22.05</td></tr><tr><td>3</td><td>22-May-24 04:37:48</td><td>1</td><td>*25.00</td><td>18.48</td></tr><tr><td>4</td><td>18-Jul-24 13:00:07</td><td>1</td><td>*23.00</td><td>14.64</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>20-Aug-24 17:12:48</td><td>1</td><td>*20.00</td><td>13.12</td></tr><tr><td>6</td><td>19-Nov-24 18:58:56</td><td>1</td><td>*21.00</td><td>17.70</td></tr><tr><td>7</td><td>20-Mar-25 15:48:36</td><td>1</td><td>*24.00</td><td>18.38</td></tr><tr><td>8</td><td>16-Apr-25 12:21:19</td><td>1</td><td>*26.00</td><td>22.40</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>18-Aug-25 13:55:41</td><td>1</td><td>*28.00</td><td>19.66</td></tr><tr><td>10</td><td>21-May-26 16:33:04</td><td>1</td><td>*25.00</td><td>15.68</td></tr></table>

Rating/target price changes above reflect Eastern Time

Tongcheng Travel Holdings

(0780.HK)

Short-Term View/Catalyst Watch Research

Analyst: Brian Gong

![](images/6e00a49f7598de275a2577a93c514944c3402484a2fcdeaf3e4dde2d7ebf8b06.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>26-Jul-23 23:00:00</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>18.00</td></tr><tr><td>2</td><td>27-Aug-23 13:17:36</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>18.44</td></tr><tr><td>3</td><td>26-Sep-24 23:35:15</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>16.82</td></tr><tr><td>4</td><td>19-Nov-24 13:58:56</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>17.70</td></tr><tr><td>5</td><td>20-Mar-25 11:48:36</td><td>Add STV</td><td>Upside</td><td>30 Days</td><td>18.38</td></tr><tr><td>6</td><td>16-Apr-25 08:21:19</td><td>Remove STV</td><td>Upside</td><td>30 Days</td><td>22.40</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td colspan="2">Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>7</td><td>25-May-25 16:22:57</td><td>Add STV</td><td>Upside</td><td>30 Days</td><td>20.50</td></tr><tr><td>8</td><td>25-Jun-25 00:26:28</td><td>Remove STV</td><td>Upside</td><td>30 Days</td><td>20.25</td></tr><tr><td>9</td><td>16-Jul-25 10:07:34</td><td>Add STV</td><td>Upside</td><td>30 Days</td><td>21.80</td></tr><tr><td>10</td><td>15-Aug-25 14:06:14</td><td>Remove STV</td><td>Upside</td><td>30 Days</td><td>19.70</td></tr><tr><td>11</td><td>18-Aug-25 09:55:41</td><td>Add STV</td><td>Upside</td><td>30 Days</td><td>19.66</td></tr><tr><td>12</td><td>18-Sep-25 00:18:07</td><td>Remove STV</td><td>Upside</td><td>30 Days</td><td>24.18</td></tr></table>

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>13</td><td>20-Oct-25 07:56:33</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>21.88</td></tr><tr><td>14</td><td>18-Jan-26 22:32:24</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>22.24</td></tr><tr><td>15</td><td>21-Jan-26 08:16:57</td><td>Add STV</td><td>Upside</td><td>30 Days</td><td>23.60</td></tr><tr><td>16</td><td>20-Feb-26 12:03:45</td><td>Remove STV</td><td>Upside</td><td>30 Days</td><td>21.76</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Trip.com Group Ltd (TCOM) Short-Term View/Catalyst Watch Research

Analyst: Brian Gong

![](images/dafdb76cdd70c88d493efe17a0ee45e300ff7d774476a1a68ac5f6e2082a732b.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>19-Jul-23 12:01:15</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>36.75</td></tr><tr><td>2</td><td>26-Jul-23 23:00:00</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>38.42</td></tr><tr><td>3</td><td>26-Aug-23 12:09:28</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>39.15</td></tr><tr><td>4</td><td>01-Apr-24 04:03:49</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>46.96</td></tr><tr><td>5</td><td>21-May-24 03:19:17</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>55.83</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>6</td><td>21-Jul-24 17:40:41</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>45.36</td></tr><tr><td>7</td><td>26-Sep-24 23:35:15</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>56.68</td></tr><tr><td>8</td><td>26-Sep-24 23:35:15</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>56.68</td></tr><tr><td>9</td><td>26-Dec-24 11:28:59</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>73.06</td></tr><tr><td>10</td><td>02-Jan-25 18:25:44</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>64.77</td></tr></table>

<table><tr><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>11 25-Feb-25 06:46:46</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>57.30</td></tr><tr><td>12 14-Oct-25 07:05:16</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>70.16</td></tr><tr><td>13 12-Jan-26 11:04:07</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>78.96</td></tr></table>

Rating/target price changes above reflect Eastern Time

The Firm has made a market in the publicly traded equity securities of Tongcheng Travel Holdings Ltd on at least one occasion since 1 Jan 2025.

<table><tr><td>The Firm has made a market in the publicly traded equity securities of Trip.com Group Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Tongcheng Travel Holdings,Trip.com Group Ltd in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Trip.com Group Ltd.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Tongcheng Travel Holdings,Trip.com Group Ltd.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Trip.com Group Ltd. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts’ compensation is determined by Citi management and Citi’s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in e

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
