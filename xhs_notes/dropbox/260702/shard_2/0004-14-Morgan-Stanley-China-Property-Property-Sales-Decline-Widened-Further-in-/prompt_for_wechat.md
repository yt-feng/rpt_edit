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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 30, 2026 02:49 PM GMT

China Property | Asia Pacific

# Property Sales Decline Widened Further in June

CRIC data show the sales decline for the top 100 developers widened to $13\%$ y-y in June. Home sales may stay weak in coming months, potentially leading to faster m-m home price drops. We suggest waiting for better entry points and sticking with quality alpha plays.

Major developers' sales weakened, as we expected, falling 11% and 13% y-y in June for top 50 and top 100 developers on attributable basis (vs. -2% each in May). This narrowed the YTD sales declines slightly to 14% for the top 50 and 16% y-y for the top 100. For the 25 major developers we track, the sales drop narrowed to 19% y-y (vs. -26% in May), bringing the YTD sales decrease to 25% y-y.

Divergence in sales performance persisted: SOEs continued to post positive sales growth. Yuexiu, COLI, Poly and Jinmao outperformed at +25%, +6%, +3% and +1% y-y, respectively. In contrast, Sunac, KWG, Longfor, Zhongliang and Shimao posted >45% y-y declines. Some semi-SOE developers also recorded weak performances; Gemdale and Vanke dropped 45% and 37% y-y, respectively. We attribute SOE outperformance to their stronger brands and more new saleable resources in top-tier cities.

Home sales may soften further in 3Q: Secondary sales volume in 25 major cities has decelerated notably to \~10% y-y in June (vs. 30% in April and 25% in May). We expect it to turn negative y-y in 3Q amid fading policy effects and pent-up demand. New home sales may continue to post y-y declines (potentially with high-single-digit % drops due to a favorable base) given reduced saleable resources of developers. We reiterate our cautious view on physical market recovery, and expect a slightly faster m-m home price decline in coming months, though select Tier 1 cities may see a mild uptrend due to their better demand/supply dynamics.

Stay selective with quality alpha plays: Considering the near-term headwinds (e.g., increasing uncertainty around sales recovery, potential weak 1H26 results), limited policy upside in July Politburo meeting and potentially continued fund flow disruption, we suggest staying prudent and waiting better entry points, despite recent sharp share price decline having dragged the industry's P/B valuation back to historical trough levels. We continue to favor quality players with credible self-help alpha. Relatively, we think CR Land (1109.HK, Top Pick), C&D (1908.HK), and Seazen (601155.SS/1030.HK) offer more alluring risk-reward at current valuations. They all have solid EPS outlooks and medium-term re-rating potential, even with no notable physical market recovery.

MS ASIA LIMITED+

Stephen Cheung, CFA  
Equity Analyst  
Stephen.Cheung@morganstanley.com

+852 3963-0385

Cara Zhu  
Equity Analyst  
Cara.Zhu@morganstanley.com +852 2848-7117

![](images/50358b2eead9928cfa668c4a2f747cd4cef93a74fbb0d7218e7b55dbbbea688e.jpg)

Asia Summer School 2026

## CHINA PROPERTY

Asia Pacific Industry View

In-Line

## Related reports:

1. An Inflection or Another False Start? (18 May 2026)

2. Our Thoughts after Recent Industry Underperformance (25 June 2026)

3. Monthly Tracker: Mixed May; Renewed Weakness Ahead (23 June 2026)

4. Managed Housing Downcycle to Last Another Two Years (25 Jan 2026)

5. 2026 Outlook: Physical Market Stays Challenging; Diverging Outperformance of Alpha Plays (10 Dec 2025)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Monthly Sales Performance

Exhibit 1: Developers contracted sales performance

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Developer type</td><td colspan="15">Monthly (Rmb bn)</td><td colspan="3">YTD (Rmb bn)</td></tr><tr><td>2025-06</td><td>2025-07</td><td>2025-08</td><td>2025-09</td><td>2025-10</td><td>2025-11</td><td>2025-12</td><td>2026-01</td><td>2026-02</td><td>2026-03</td><td>2026-04</td><td>2026-05</td><td>2026-06</td><td>YoY</td><td>MoM</td><td>2025-06</td><td>2026-06</td><td>YoY</td></tr><tr><td>Agile</td><td>3383 HK</td><td>POE</td><td>0.9</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0.7</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.5</td><td>0.7</td><td>0.8</td><td>-12%</td><td>26%</td><td>5</td><td>4</td><td>-26%</td></tr><tr><td>Binjiang</td><td>002244 CH</td><td>POE</td><td>9.4</td><td>8.8</td><td>9.0</td><td>8.1</td><td>7.7</td><td>8.2</td><td>7.2</td><td>5.3</td><td>3.9</td><td>5.9</td><td>9.3</td><td>9.3</td><td>9.6</td><td>2%</td><td>3%</td><td>53</td><td>43</td><td>-18%</td></tr><tr><td>C&amp;D International *</td><td>1908 HK</td><td>SOE</td><td>11.4</td><td>4.3</td><td>5.7</td><td>7.7</td><td>8.8</td><td>4.5</td><td>6.6</td><td>5.3</td><td>5.5</td><td>8.6</td><td>9.7</td><td>10.8</td><td>9.2</td><td>-20%</td><td>-15%</td><td>53</td><td>49</td><td>-8%</td></tr><tr><td>China SCE</td><td>1966 HK</td><td>POE</td><td>0.7</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.8</td><td>0.7</td><td>0.7</td><td>0.5</td><td>0.5</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.6</td><td>-15%</td><td>-23%</td><td>5</td><td>4</td><td>-14%</td></tr><tr><td>CIFI</td><td>884 HK</td><td>POE</td><td>1.3</td><td>1.0</td><td>1.0</td><td>0.9</td><td>1.1</td><td>0.9</td><td>1.0</td><td>0.7</td><td>0.5</td><td>1.2</td><td>0.7</td><td>0.9</td><td>1.1</td><td>-19%</td><td>24%</td><td>10</td><td>5</td><td>-51%</td></tr><tr><td>CMSK</td><td>001979 CH</td><td>SOE</td><td>21.7</td><td>15.7</td><td>19.5</td><td>16.7</td><td>15.4</td><td>14.1</td><td>25.8</td><td>7.7</td><td>7.8</td><td>17.9</td><td>21.7</td><td>20.9</td><td>20.1</td><td>-7%</td><td>-4%</td><td>89</td><td>96</td><td>8%</td></tr><tr><td>COLI</td><td>688 HK</td><td>SOE</td><td>29.7</td><td>11.9</td><td>18.3</td><td>20.2</td><td>18.7</td><td>22.2</td><td>39.8</td><td>14.5</td><td>8.5</td><td>28.6</td><td>24.2</td><td>27.3</td><td>31.3</td><td>6%</td><td>15%</td><td>120</td><td>134</td><td>12%</td></tr><tr><td>Country Garden *</td><td>2007 HK</td><td>POE</td><td>2.8</td><td>2.8</td><td>3.0</td><td>2.6</td><td>2.9</td><td>2.4</td><td>2.7</td><td>2.2</td><td>2.2</td><td>2.2</td><td>2.5</td><td>2.6</td><td>2.5</td><td>-13%</td><td>-7%</td><td>17</td><td>14</td><td>-15%</td></tr><tr><td>CR Land</td><td>1109 HK</td><td>SOE</td><td>23.5</td><td>13.3</td><td>13.2</td><td>17.6</td><td>15.2</td><td>23.0</td><td>41.0</td><td>11.7</td><td>10.1</td><td>22.4</td><td>25.9</td><td>23.5</td><td>23.0</td><td>-2%</td><td>-2%</td><td>110</td><td>117</td><td>6%</td></tr><tr><td>Gemdale</td><td>600383 CH</td><td>Semi-SOE</td><td>3.1</td><td>2.6</td><td>2.2</td><td>2.2</td><td>1.9</td><td>1.5</td><td>2.4</td><td>1.2</td><td>0.6</td><td>1.5</td><td>2.5</td><td>2.0</td><td>1.7</td><td>-45%</td><td>-15%</td><td>17</td><td>10</td><td>-44%</td></tr><tr><td>Greentown</td><td>3900 HK</td><td>Semi-SOE</td><td>14.9</td><td>5.4</td><td>10.0</td><td>12.2</td><td>12.5</td><td>12.5</td><td>20.5</td><td>6.3</td><td>4.5</td><td>14.8</td><td>10.4</td><td>12.5</td><td>11.7</td><td>-21%</td><td>-6%</td><td>80</td><td>60</td><td>-25%</td></tr><tr><td>Jinmao</td><td>817 HK</td><td>SOE</td><td>15.6</td><td>8.5</td><td>9.1</td><td>9.8</td><td>12.0</td><td>8.0</td><td>12.8</td><td>7.6</td><td>5.3</td><td>9.5</td><td>8.8</td><td>10.5</td><td>15.8</td><td>1%</td><td>50%</td><td>53</td><td>58</td><td>8%</td></tr><tr><td>KWG</td><td>1813 HK</td><td>POE</td><td>0.7</td><td>0.6</td><td>0.6</td><td>0.7</td><td>0.6</td><td>0.5</td><td>0.4</td><td>0.3</td><td>0.3</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.3</td><td>-61%</td><td>-42%</td><td>4</td><td>2</td><td>-42%</td></tr><tr><td>Logan</td><td>3380 HK</td><td>POE</td><td>0.6</td><td>0.4</td><td>0.9</td><td>0.5</td><td>0.5</td><td>0.6</td><td>0.8</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0%</td><td>0%</td><td>4</td><td>3</td><td>-24%</td></tr><tr><td>Longfor</td><td>960 HK</td><td>POE</td><td>6.5</td><td>6.0</td><td>4.7</td><td>5.0</td><td>5.0</td><td>3.6</td><td>3.8</td><td>2.5</td><td>2.0</td><td>3.0</td><td>2.9</td><td>3.3</td><td>2.8</td><td>-57%</td><td>-16%</td><td>35</td><td>16</td><td>-53%</td></tr><tr><td>Midea RE</td><td>3990 HK</td><td>POE</td><td>2.5</td><td>2.0</td><td>1.4</td><td>1.8</td><td>2.1</td><td>1.2</td><td>1.6</td><td>1.2</td><td>0.9</td><td>1.6</td><td>1.1</td><td>1.4</td><td>1.3</td><td>-48%</td><td>-7%</td><td>16</td><td>8</td><td>-52%</td></tr><tr><td>Poly</td><td>600048 CH</td><td>SOE</td><td>29.0</td><td>18.0</td><td>18.0</td><td>20.5</td><td>21.1</td><td>18.0</td><td>12.2</td><td>15.6</td><td>10.1</td><td>26.0</td><td>25.9</td><td>27.6</td><td>29.8</td><td>3%</td><td>8%</td><td>145</td><td>135</td><td>-7%</td></tr><tr><td>Powerlong</td><td>1238 HK</td><td>POE</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.5</td><td>0.7</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0.4</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.6</td><td>14%</td><td>5%</td><td>4</td><td>3</td><td>-8%</td></tr><tr><td>Seazen</td><td>1030 HK</td><td>POE</td><td>1.5</td><td>1.7</td><td>1.6</td><td>1.5</td><td>1.4</td><td>1.4</td><td>1.4</td><td>0.7</td><td>1.2</td><td>1.1</td><td>1.0</td><td>1.4</td><td>1.0</td><td>-36%</td><td>-31%</td><td>10</td><td>6</td><td>-38%</td></tr><tr><td>Shimao</td><td>813 HK</td><td>POE</td><td>2.3</td><td>2.0</td><td>1.8</td><td>1.9</td><td>1.7</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.3</td><td>1.7</td><td>1.2</td><td>1.2</td><td>1.3</td><td>-46%</td><td>3%</td><td>14</td><td>8</td><td>-39%</td></tr><tr><td>Sino-Ocean</td><td>3377 HK</td><td>Semi-SOE</td><td>3.0</td><td>1.4</td><td>1.7</td><td>2.4</td><td>2.5</td><td>2.5</td><td>2.5</td><td>1.2</td><td>0.5</td><td>1.4</td><td>1.6</td><td>1.7</td><td>1.7</td><td>-42%</td><td>-2%</td><td>13</td><td>8</td><td>-39%</td></tr><tr><td>Sunac</td><td>1918 HK</td><td>POE</td><td>7.6</td><td>1.5</td><td>5.4</td><td>1.3</td><td>1.0</td><td>1.1</td><td>3.0</td><td>1.1</td><td>2.6</td><td>2.2</td><td>1.2</td><td>1.1</td><td>0.9</td><td>-88%</td><td>-20%</td><td>24</td><td>9</td><td>-62%</td></tr><tr><td>Vanke</td><td>000002 CH</td><td>Semi-SOE</td><td>11.6</td><td>13.5</td><td>9.0</td><td>9.2</td><td>14.4</td><td>9.4</td><td>9.8</td><td>5.6</td><td>3.5</td><td>7.5</td><td>4.8</td><td>6.2</td><td>7.4</td><td>-37%</td><td>18%</td><td>69</td><td>35</td><td>-49%</td></tr><tr><td>Yuexiu</td><td>123 HK</td><td>SOE</td><td>10.8</td><td>6.0</td><td>5.5</td><td>6.8</td><td>12.3</td><td>5.1</td><td>9.0</td><td>4.2</td><td>2.9</td><td>10.1</td><td>8.5</td><td>11.3</td><td>13.5</td><td>25%</td><td>19%</td><td>62</td><td>51</td><td>-18%</td></tr><tr><td>Zhongliang</td><td>2772 HK</td><td>POE</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.1</td><td>0.9</td><td>0.9</td><td>0.8</td><td>0.7</td><td>0.5</td><td>0.6</td><td>0.6</td><td>0.5</td><td>-52%</td><td>-13%</td><td>6</td><td>4</td><td>-44%</td></tr><tr><td>Aggregate</td><td></td><td></td><td>212</td><td>129</td><td>143</td><td>151</td><td>161</td><td>144</td><td>208</td><td>98</td><td>76</td><td>170</td><td>167</td><td>179</td><td>188</td><td>-11%</td><td>5%</td><td>1,010</td><td>878</td><td>-13%</td></tr><tr><td>Median</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-19%</td><td>-2%</td><td></td><td></td><td>-25%</td></tr><tr><td>SOE Median</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1%</td><td>8%</td><td></td><td></td><td>6%</td></tr><tr><td>Semi-SOE Median</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-39%</td><td>-4%</td><td></td><td></td><td>-42%</td></tr><tr><td>POE Median</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-27%</td><td>-7%</td><td></td><td></td><td>-39%</td></tr><tr><td>Top 30 (attributable)</td><td></td><td></td><td>195</td><td>114</td><td>119</td><td>140</td><td>156</td><td>140</td><td>209</td><td>96</td><td>50</td><td>181</td><td>159</td><td>173</td><td>178</td><td>-9%</td><td>3%</td><td>945</td><td>837</td><td>-11%</td></tr><tr><td>Top 50 (attributable)</td><td></td><td></td><td>229</td><td>131</td><td>137</td><td>164</td><td>179</td><td>161</td><td>234</td><td>110</td><td>80</td><td>180</td><td>177</td><td>196</td><td>204</td><td>-11%</td><td>4%</td><td>1,108</td><td>948</td><td>-14%</td></tr><tr><td>Top 100 (attributable)</td><td></td><td></td><td>267</td><td>164</td><td>154</td><td>198</td><td>201</td><td>184</td><td>262</td><td>129</td><td>91</td><td>206</td><td>205</td><td>227</td><td>233</td><td>-13%</td><td>2%</td><td>1,301</td><td>1,091</td><td>-16%</td></tr></table>

Source: CRIC, CREIS, MS. \*Country Garden and C&D International report attributable sales, the rest report gross sales.

Exhibit 2: CRIC monthly sales of top 20/30/50/100 developers

<table><tr><td></td><td colspan="4">Monthly attributable sales - y-y</td><td colspan="4">Monthly attributable sales - m-m</td><td colspan="4">YTD attributable sales - y-y</td></tr><tr><td>Month</td><td>Top 20</td><td>Top 30</td><td>Top 50</td><td>Top 100</td><td>Top 20</td><td>Top 30</td><td>Top 50</td><td>Top 100</td><td>Top 20</td><td>Top 30</td><td>Top 50</td><td>Top 100</td></tr><tr><td>2018-01</td><td>54%</td><td>54%</td><td>54%</td><td>54%</td><td>-18%</td><td>-26%</td><td>-29%</td><td>-37%</td><td>54%</td><td>54%</td><td>54%</td><td>54%</td></tr><tr><td>2018-02</td><td>31%</td><td>32%</td><td>31%</td><td>32%</td><td>-24%</td><td>-22%</td><td>-22%</td><td>-20%</td><td>43%</td><td>43%</td><td>43%</td><td>44%</td></tr><tr><td>2018-03</td><td>-5%</td><td>-2%</td><td>0%</td><td>3%</td><td>33%</td><td>35%</td><td>35%</td><td>35%</td><td>21%</td><td>22%</td><td>23%</td><td>25%</td></tr><tr><td>2018-04</td><td>24%</td><td>22%</td><td>25%</td><td>26%</td><td>-5%</td><td>-6%</td><td>-3%</td><td>-4%</td><td>21%</td><td>22%</td><td>23%</td><td>25%</td></tr><tr><td>2018-05</td><td>45%</td><td>47%</td><td>54%</td><td>54%</td><td>8%</td><td>11%</td><td>14%</td><td>20%</td><td>26%</td><td>27%</td><td>30%</td><td>31%</td></tr><tr><td>2018-06</td><td>32%</td><td>35%</td><td>35%</td><td>36%</td><td>34%</td><td>31%</td><td>27%</td><td>28%</td><td>27%</td><td>29%</td><td>31%</td><td>32%</td></tr><tr><td>2018-07</td><td>64%</td><td>65%</td><td>65%</td><td>64%</td><td>-23%</td><td>-24%</td><td>-23%</td><td>-24%</td><td>32%</td><td>33%</td><td>35%</td><td>36%</td></tr><tr><td>2018-08</td><td>33%</td><td>43%</td><td>46%</td><td>43%</td><td>-11%</td><td>-10%</td><td>-9%</td><td>-7%</td><td>32%</td><td>34%</td><td>36%</td><td>37%</td></tr><tr><td>2018-09</td><td>26%</td><td>27%</td><td>28%</td><td>31%</td><td>22%</td><td>20%</td><td>18%</td><td>14%</td><td>31%</td><td>33%</td><td>35%</td><td>36%</td></tr><tr><td>2018-10</td><td>24%</td><td>26%</td><td>29%</td><td>29%</td><td>-8%</td><td>-7%</td><td>-7%</td><td>-6%</td><td>30%</td><td>32%</td><td>34%</td><td>35%</td></tr><tr><td>2018-11</td><td>22%</td><td>126%</td><td>118%</td><td>98%</td><td>0%</td><td>91%</td><td>88%</td><td>74%</td><td>29%</td><td>42%</td><td>43%</td><td>42%</td></tr><tr><td>2018-12</td><td>-2%</td><td>-74%</td><td>-58%</td><td>-44%</td><td>12%</td><td>-83%</td><td>-72%</td><td>-57%</td><td>26%</td><td>27%</td><td>30%</td><td>30%</td></tr><tr><td>2019-01</td><td>-15%</td><td>-13%</td><td>-11%</td><td>-9%</td><td>-29%</td><td>145%</td><td>49%</td><td>3%</td><td>-15%</td><td>-13%</td><td>-11%</td><td>-9%</td></tr><tr><td>2019-02</td><td>-10%</td><td>-10%</td><td>-8%</td><td>-9%</td><td>-19%</td><td>-19%</td><td>-19%</td><td>-21%</td><td>-13%</td><td>-12%</td><td>-9%</td><td>-9%</td></tr><tr><td>2019-03</td><td>9%</td><td>9%</td><td>12%</td><td>12%</td><td>61%</td><td>63%</td><td>65%</td><td>67%</td><td>-5%</td><td>-4%</td><td>-1%</td><td>-1%</td></tr><tr><td>2019-04</td><td>17%</td><td>17%</td><td>16%</td><td>17%</td><td>2%</td><td>1%</td><td>0%</td><td>0%</td><td>1%</td><td>1%</td><td>3%</td><td>4%</td></tr><tr><td>2019-05</td><td>12%</td><td>9%</td><td>8%</td><td>5%</td><td>3%</td><td>4%</td><td>7%</td><td>9%</td><td>3%</td><td>3%</td><td>4%</td><td>4%</td></tr><tr><td>2019-06</td><td>7%</td><td>6%</td><td>6%</td><td>3%</td><td>28%</td><td>27%</td><td>25%</td><td>25%</td><td>4%</td><td>4%</td><td>5%</td><td>4%</td></tr><tr><td>2019-07</td><td>-5%</td><td>-4%</td><td>-5%</td><td>-3%</td><td>-31%</td><td>-31%</td><td>-31%</td><td>-29%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td></tr><tr><td>2019-08</td><td>12%</td><td>8%</td><td>5%</td><td>2%</td><td>5%</td><td>1%</td><td>1%</td><td>-2%</td><td>4%</td><td>3%</td><td>3%</td><td>3%</td></tr><tr><td>2019-09</td><td>18%</td><td>20%</td><td>15%</td><td>11%</td><td>29%</td><td>32%</td><td>30%</td><td>24%</td><td>6%</td><td>5%</td><td>5%</td><td>4%</td></tr><tr><td>2019-10</td><td>24%</td><td>22%</td><td>21%</td><td>16%</td><td>-4%</td><td>-5%</td><td>-3%</td><td>-1%</td><td>7%</td><td>7%</td><td>7%</td><td>5%</td></tr><tr><td>2019-11</td><td>20%</td><td>-36%</td><td>-34%</td><td>-28%</td><td>-3%</td><td>0%</td><td>3%</td><td>8%</td><td>9%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>2019-12</td><td>18%</td><td>339%</td><td>181%</td><td>100%</td><td>11%</td><td>15%</td><td>19%</td><td>18%</td><td>10%</td><td>9%</td><td>8%</td><td>6%</td></tr><tr><td>2020-01</td><td>-13%</td><td>-13%</td><td>-14%</td><td>-16%</td><td>-48%</td><td>-51%</td><td>-55%</td><td>-57%</td><td>-13%</td><td>-13%</td><td>-14%</td><td>-16%</td></tr><tr><td>2020-02</td><td>-26%</td><td>-30%</td><td>-34%</td><td>-38%</td><td>-31%</td><td>-35%</td><td>-38%</td><td>-42%</td><td>-19%</td><td>-21%</td><td>-23%</td><td>-26%</td></tr><tr><td>2020-03</td><td>-6%</td><td>-10%</td><td>-11%</td><td>-15%</td><td>104%</td><td>110%</td><td>121%</td><td>129%</td><td>-14%</td><td>-16%</td><td>-18%</td><td>-21%</td></tr><tr><td>2020-04</td><td>0%</td><td>0%</td><td>0%</t

[中间内容因长度限制已省略]

oprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of China Overseas Land & Investment Ltd., China Resources Land Ltd., China Vanke Company Ltd. listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: China Property

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/30/2026)</td></tr><tr><td>C&amp;D International Investment Group Ltd (1908.HK)</td><td>O (08/01/2024)</td><td>HK$13.50</td></tr><tr><td>China Jinmao Holdings Group Ltd (0817.HK)</td><td>E (03/28/2024)</td><td>HK$1.23</td></tr><tr><td>China Merchants Shekou Industrial Zone (001979.SZ)</td><td>E (05/06/2021)</td><td>Rmb6.43</td></tr><tr><td>China Overseas Land &amp; Investment Ltd. (0688.HK)</td><td>E (01/20/2025)</td><td>HK$12.06</td></tr><tr><td>China Resources Land Ltd. (1109.HK)</td><td>O (01/02/2019)</td><td>HK$30.00</td></tr><tr><td>China Vanke Company Ltd. (2202.HK)</td><td>E (11/07/2023)</td><td>HK$2.12</td></tr><tr><td>China Vanke Company Ltd. (000002.SZ)</td><td>U (11/30/2022)</td><td>Rmb2.96</td></tr><tr><td>Gemdale Corporation (600383.SS)</td><td>U (01/28/2026)</td><td>Rmb2.11</td></tr><tr><td>Greentown China Holdings (3900.HK)</td><td>U (08/26/2025)</td><td>HK$6.76</td></tr><tr><td>Longfor Group Holdings Ltd. (0960.HK)</td><td>E (05/17/2024)</td><td>HK$5.98</td></tr><tr><td>Poly Developments and Holdings Group (600048.SS)</td><td>E (05/17/2024)</td><td>Rmb4.63</td></tr><tr><td>Seazen Group Ltd (1030.HK)</td><td>O (01/28/2026)</td><td>HK$1.33</td></tr><tr><td>Seazen Holdings Company Ltd. (601155.SS)</td><td>O (11/03/2025)</td><td>Rmb10.26</td></tr><tr><td>Yuexiu Property Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$3.34</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
