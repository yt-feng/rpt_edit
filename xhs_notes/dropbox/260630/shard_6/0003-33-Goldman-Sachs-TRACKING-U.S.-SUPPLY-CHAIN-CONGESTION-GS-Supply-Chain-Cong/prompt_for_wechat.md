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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
TRACKING U.S. SUPPLY CHAIN CONGESTION

# GS Supply Chain Congestion Scale: June 29th; Index Higher W/W, Bottleneck Scale Unchanged at ‘2’

GS Supply Chain Congestion Scale
Week of 6/29/2026

![](images/b8c243acb981f477f4f7016a76bf8f1405bf0d8cb38ca71a65ac0930b5a83ac3.jpg)  
Scale is based solely off weekly metrics to give more granularity on high frequency data indications; see Appendix for scale that combines weekly and monthly metrics

Our weekly bottleneck scale remained at ‘2’ this week, reflecting the absolute level of our congestion index decreasing moderately on a sequential basis (-7% w/w; Exhibit 2). For this week’s scale and index, the number of container ships waiting to dock and unload goods along the West Coast remained unchanged at 1, while backlogs along the East Coast ticked up to 4 from 3 (Exhibit 6). West Coast rail intermodal traffic growth accelerated versus last week (+14% YoY vs +11% YoY last week; Exhibit 7), while rail

Jordan Alliger
+1(212)357-4913 |
jordan.alliger@gs.com
GS & Co. LLC

Andrzej Tomczyk, CFA
+1(212)357-4445 |
andrzej.tomczyk@gs.com
GS & Co. LLC

Paul Stoddard
+1(801)744-3761 |
paul.x.stoddard@gs.com
GS & Co. LLC

Source: GS Global Investment Research

service metrics were mixed. Chassis dwell times increased slightly on average at US ports (Exhibit 9), while ocean container shipping rates (China to US West Coast) were up +19% WoW and up +3% YoY (Exhibit 10).

Exhibit 1: Our weekly composite index decreased in the most recent week (-7% w/w); the bottleneck scale remained at '2'; overall bottleneck levels remain well below peak congestion levels when scale was at '10' and now imply levels in line with pre-Covid fluidity
GS Weekly Bottleneck Index, Feb 2020 - June 2026

![](images/38c5182869b2ebe2e836dcf258bbad6a6e2bc8a1b1eb8b8bbd443cdd49121593.jpg)  
Source: GS Global Investment Research

Exhibit 2: Our average weekly bottleneck score in June is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline

GS Weekly Congestion Scale, Scored by Month\*

![](images/4e435334f9d124fc5fb40561d8cdcd5ee41c12c2c887f04a563b2a73e203a2db.jpg)  
\*Numbers reflect the average weekly score seen in each respective month  
Source: GS Global Investment Research

As a reminder (and to help reiterate why and how we construct the index), please refer to the Appendix following Exhibit 17. Additionally, for further clarity on tracked congestion metrics, please refer to the glossary following Exhibit 19.

## Transport Subsectors to Watch as Congestion Remains Muted

The key question remains as to what impact tariffs and geopolitical conflicts will have on demand and timing of freight flows, as well as ability to normalize around global trade. Please see our recent tariff impact tracker for additional commentary. Should supply chain pressures broadly continue to mitigate, then it is conceivable we could see the index remaining more consistently in ‘1’ territory in 2026.

## Indicator Updates

Of the metrics we track (Exhibit 3), we provide updates for the weekly and monthly variables below (Exhibit 4 - Exhibit 5).

Exhibit 3: Tracked Congestion Metrics

<table><tr><td colspan="2">Tracked Metrics</td></tr><tr><td>Weekly VariablesContainer Ships Waiting to Dock at LA/LBContainer Ships Waiting Along to U.S. Gulf/East CoastUNP Intermodal TrafficUNP Intermodal VelocityUNP Intermodal DwellBNSF Intermodal TrafficBNSF Intermodal VelocityBNSF Intermodal DwellOcean Shipping Rates, East Asia to U.S. West Coast Chassis Street Dwell, 20ft ContainersChassis Street Dwell, 40/45ft ContainersChassis Terminal Dwell Time, 20ft ContainersChassis Terminal Dwell Time, 40/45ft Containers</td><td>Monthly VariablesContainer Weighted Average Dwell (San Pedro&#x27;s Bay)Containers Dwelling &gt; 5 days (San Pedro&#x27;s Bay)PMI Manufacturing Supplier Delivery TimeBig Three&#x27; West Coast Ports&#x27; Inbound Loaded ContainersLMI Transportation CapacityLMI Warehousing CapacityLMI Warehousing UtilizationDoor to Door Shipping Days, China to USClass 8 Trucking Driver Count GrowthRail Container Dwell (San Pedro&#x27;s Bay)</td></tr></table>

Source: GS Global Investment Research

Exhibit 4: Bottleneck metrics indicated mixed results this week versus last

<table><tr><td></td><td>Mar 23 - Mar 29</td><td>Mar 30 - Apr 5</td><td>Apr 6 - Apr 12</td><td>Apr 13 - Apr 19</td><td>Apr 20 - Apr 26</td><td>Apr 27 - May 3</td><td>May 4 - May 10</td><td>May 11 - May 17</td><td>May 18 - May 24</td><td>May 25 - May 31</td><td>Jun 1 - Jun 7</td><td>June 8 - June 14</td><td>June 15 - June 21</td></tr><tr><td>Container Ships Waiting to Dock at LALB</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Container Ship Backup (East and Gulf Coast)*</td><td>5</td><td>4</td><td>4</td><td>1</td><td>2</td><td>2</td><td>4</td><td>5</td><td>4</td><td>5</td><td>5</td><td>3</td><td>4</td></tr><tr><td>UNP Intermodal Traffic (YoY Growth)</td><td>-8.7%</td><td>-9.0%</td><td>-8.2%</td><td>-4.3%</td><td>-2.0%</td><td>-0.3%</td><td>-0.8%</td><td>8.4%</td><td>8.4%</td><td>8.3%</td><td>15.6%</td><td>10.4%</td><td>12.5%</td></tr><tr><td>UNP Intermodal Velocity (YoY Growth)</td><td>8.5%</td><td>5.0%</td><td>8.3%</td><td>7.4%</td><td>8.3%</td><td>3.9%</td><td>2.5%</td><td>4.2%</td><td>2.9%</td><td>0.0%</td><td>-1.9%</td><td>-2.2%</td><td>-1.6%</td></tr><tr><td>UNP System Dwell (Hours)</td><td>20.3</td><td>20.1</td><td>19.9</td><td>19.6</td><td>19.4</td><td>20.0</td><td>20</td><td>19.9</td><td>19.5</td><td>19.8</td><td>19.7</td><td>19.4</td><td>19.9</td></tr><tr><td>BNSF Intermodal Traffic (YoY Growth)</td><td>1.9%</td><td>2.6%</td><td>2.3%</td><td>5.7%</td><td>4.7%</td><td>7.7%</td><td>7.8%</td><td>9.7%</td><td>18.7%</td><td>11.5%</td><td>15.9%</td><td>11.8%</td><td>14.9%</td></tr><tr><td>BNSF Intermodal Velocity (YoY Growth)</td><td>3.3%</td><td>-3.1%</td><td>-1.6%</td><td>-2.4%</td><td>-2.1%</td><td>-3.9%</td><td>-0.6%</td><td>-3.7%</td><td>6.9%</td><td>-8.6%</td><td>-10.3%</td><td>-7.2%</td><td>-6.1%</td></tr><tr><td>BNSF System Dwell (Hours)</td><td>22.6</td><td>22.5</td><td>22.1</td><td>22.7</td><td>22.3</td><td>22.1</td><td>22.3</td><td>23.0</td><td>22.8</td><td>22.6</td><td>22.2</td><td>22.1</td><td>22.4</td></tr><tr><td>Ocean Shipping Rates, East Asia to U.S. West Coast (YoY Growth)</td><td>-0.1%</td><td>7.7%</td><td>0.9%</td><td>13.2%</td><td>14.9%</td><td>17.4%</td><td>18.1%</td><td>14.3%</td><td>14.1%</td><td>15.6%</td><td>(11.9%)</td><td>(19.3%)</td><td>2.7%</td></tr><tr><td>Chassis Street Dwell, 20ft Containers (Days)</td><td>5.3</td><td>4.9</td><td>4.4</td><td>4.2</td><td>5.4</td><td>4.5</td><td>4.2</td><td>4.9</td><td>4.4</td><td>4.7</td><td>4.7</td><td>4.4</td><td>5.1</td></tr><tr><td>Chassis Street Dwell, 40/45ft Containers (Days)</td><td>6.5</td><td>6.9</td><td>5.7</td><td>5.8</td><td>6.0</td><td>5.5</td><td>5.7</td><td>5.6</td><td>5.5</td><td>5.8</td><td>6.2</td><td>6.3</td><td>6.5</td></tr><tr><td>Chassis Terminal Dwell Time, 20ft Containers (Days)</td><td>10.6</td><td>10.6</td><td>9.4</td><td>9.1</td><td>11.4</td><td>10.3</td><td>10.2</td><td>11.5</td><td>12.0</td><td>12.4</td><td>10.8</td><td>10</td><td>11.1</td></tr><tr><td>Chassis Terminal Dwell Time, 40/45ft Containers (Days)</td><td>7.2</td><td>7.7</td><td>6.3</td><td>6.1</td><td>6.5</td><td>6.2</td><td>6.2</td><td>6.3</td><td>5.5</td><td>5.5</td><td>5.2</td><td>4.9</td><td>5.3</td></tr></table>

As of 3/28/22, we added and backdated our estimates for the East and Gulf Coast container ship backlog.

Source: Marine Exchange of Southern California, AAR, STB, Freightos, Pool of Pools, Pacific Merchant Shipping Association, Port of Long Beach, Port of Oakland, Port of Los Angeles, LMI, US Bureau of Labor Statistics, IHS Markit, Refinitiv Eikon, compiled by GS Global Investment Research

Exhibit 5: Lagged monthly bottleneck metrics for May indicated mixed results vs April

<table><tr><td>Monthly Variables</td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Container Weighted Average Dwell (Days)</td><td>3.3</td><td>2.8</td><td>2.8</td><td>2.8</td><td>3.0</td><td>2.6</td><td>2.9</td><td>2.7</td><td>2.8</td><td>2.7</td><td>2.6</td><td>2.5</td><td>2.8</td><td>2.6</td><td>2.6</td><td>2.6</td><td>2.6</td></tr><tr><td>% of Containers Dwelling &gt; 5 days</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td></tr><tr><td>Rail Container Dwell (Days)</td><td>7.1</td><td>8.0</td><td>6.8</td><td>4.7</td><td>4.7</td><td>3.3</td><td>5.2</td><td>5.0</td><td>4.0</td><td>3.3</td><td>3.7</td><td>5.1</td><td>6.1</td><td>5.1</td><td>4.4</td><td>5.1</td><td>5.2</td></tr><tr><td>Big Three Inbound Loaded Containers (YoY)</td><td>23.6%</td><td>5.8%</td><td>11.6%</td><td>9.5%</td><td>-10.0%</td><td>-4.6%</td><td>8.6%</td><td>-2.1%</td><td>-7.3%</td><td>-11.5%</td><td>-9.5%</td><td>-7.1%</td><td>-11.6%</td><td>0.6%</td><td>-2.0%</td><td>-1.0%</td><td>29.6%</td></tr><tr><td>LMI Transportation Capacity</td><td>52.6</td><td>55.1</td><td>53.6</td><td>55.2</td><td>54.7</td><td>52.4</td><td>52.6</td><td>57.3</td><td>55.1</td><td>54.5</td><td>50.0</td><td>36.9</td><td>47.1</td><td>41.0</td><td>39.2</td><td>28.4</td><td>31.7</td></tr><tr><td>LMI Warehousing Capacity</td><td>51.7</td><td>50.5</td><td>52.3</td><td>55.4</td><td>50.0</td><td>47.8</td><td>51.1</td><td>50.5</td><td>51.6</td><td>52.0</td><td>54.8</td><td>61.2</td><td>50.0</td><td>50.0</td><td>46.0</td><td>45.5</td><td>50.5</td></tr><tr><td>LMI Warehousing Utilization</td><td>68.3</td><td>65.5</td><td>59.7</td><td>60.1</td><td>62.5</td><td>62.2</td><td>59.4</td><td>62.1</td><td>65.3</td><td>56.5</td><td>47.5</td><td>42.9</td><td>54.4</td><td>60.3</td><td>59.8</td><td>64.4</td><td>62.9</td></tr><tr><td>Door to Door Shipping Days, China to US</td><td>50</td><td>51</td><td>54</td><td>49</td><td>48</td><td>50</td><td>46</td><td>44</td><td>46</td><td>47</td><td>47</td><td>47</td><td>47</td><td>47</td><td>47</td><td>47</td><td>47</td></tr><tr><td>Class 8 Driver Count</td><td>1493.1</td><td>1487.6</td><td>1491.4</td><td>1490.6</td><td>1487.7</td><td>1482.7</td><td>1482.5</td><td>1480.2</td><td>1472.3</td><td>1472.6</td><td>1467.8</td><td>1467.2</td><td>1465.6</td><td>1465.1</td><td>1464.3</td><td>1469.2</td><td>1464.8</td></tr><tr><td>PMI Manufacturing Supplier Delivery Time (YoY)</td><td>0.8</td><td>11.6</td><td>6.1</td><td>6.2</td><td>9.8</td><td>-0.3</td><td>-4.7</td><td>2.3</td><td>10.8</td><td>-0.5</td><td>0.1</td><td>5.5</td><td>-0.4</td><td>4.6</td><td>6.3</td><td>10.7</td><td>8.4</td></tr></table>

Source: Marine Exchange of Southern California, AAR, STB, Freightos, Pool of Pools, Pacific Merchant Shipping Association, Port of Long Beach, Port of Oakland, Port of Los Angeles, LMI, US Bureau of Labor Statistics, IHS Markit, compiled by GS Global Investment Research

## Weekly Indicator Update

Anchored Container Ships

■ West Coast container ship backlogs remained flat at 1 in the most recent week while East Coast backlogs were higher at 4.

Exhibit 6: 4/1\* container ships backed up this week on the East/West Coast

West vs. East Coast Container Ship Backlog, Weekly Average, Feb 2020 - June 2026

![](images/4504ce8cb3d208845b5e1235929accee2ec70c04504b2eab16966e434aa7b18c.jpg)  
\*East Coast is estimated via satellite data - includes container ships sitting for more than 3 days within 140 miles of US ports to the right of longitude 100 (i.e., Gulf and East Coast)  
Source: Marine Exchange of Southern California, Refinitiv Eikon, GS Global Investment Research

## Rail Intermodal Trends

West Coast Class 1 Rails' (Union Pacific and Burlington Northern Santa Fe) average intermodal traffic growth accelerated to +14% last week versus +11% in the prior week.

☐ BNSF intermodal traffic at +15% YoY this week vs. +12% YoY last week; UNP intermodal traffic at +12.5% YoY vs. +10% YoY last week.

☐ See average BNSF/UNP growth trends in Exhibit 7.

Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52
YoY % growth  
![](images/45f1908c953cbfc2940c4b745495e7f8095ca4aaeacd0d358f34882a3a93b29b.jpg)  
Source: AAR, Data compiled by GS Global Investment Research  
Exhibit 8: West Coast intermodal carload growth (UNP and BNSF) is tracking up \~14% YoY on average in June
West Coast Class 1 Rail Intermodal Traffic YoY % Growth

![](images/d748b5c9f77638eacc92915484a887cdb57453f7fadf539f3316758480f4dde2.jpg)  
Source: AAR, Data compiled by GS Global Investment Research

■ West Coast Class 1 Rail terminal dwell and intermodal train speed were mixed in the recent week (detailed below).

☐ UNP terminal dwell increased slightly from 19.4 hours to 19.9 hours in the most recent week; BNSF dwell increased from 22.1 hours to 22.4 hours.

☐ On intermodal train speed, BNSF was at -6% YoY vs. -7% YoY last week; UNP was at -1.6% YoY vs. -2.2% last week.

## Chassis Dwell Time

\- Chassis dwell is down significantly when comparing June to peak congestion levels – as per Exhibit 9; dwell data for the most recent week implied mostly worsened results vs last week.

☐ Average Street dwell time for 20ft shipping container chassis was at 5.1 days in week 25 of 2026, higher versus 4.4 days in the prior week.

☐ Street dwell time for 40/45ft container chassis was 6.5 days in week 25, up versus 6.3 days in the prior week.

☐ Chassis terminal dwell time for 20/40ft containers was at 11.1/5.3 days in week 25 versus 10/5.3 days in the prior week.

Exhibit 9: Dwell for the more typical 20ft container chassis is well off peak congestion levels
Chassis Street Dwell Time (20ft Containers)

![](images/12a5854119ee9eb05266973561c6baa539e89852a1e537d3d4ac430daa770f30.jpg)  
Dwell time shown in days

## Ocean Shipping Rates

The prior week saw ocean container rates at \~\$5.74k (+3% YoY), increased vs \~\$4.84k in the previous week (-19% YoY).

Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast  
![](images/68838aeec7e33021995b68d7b589149a9828a46a3202f17178b91ee2d717357c.jpg)  
Rate is \$ per FEU (Forty-Foot Equivalent Unit)  
Source: FBX

## Lagged Monthly Indicators (May Data)

San Pedro's Bay Container Dwell

\- Container weighted average dwell time was \~2.6 days in May, unchanged versus \~2.6 days in April.

Rail container dwell was higher in May at 5.2 days vs 5.1 days in April; this result for dwell remains far below 2022's peak rail container dwell of \~16 days.

Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days  
![](images/9de3abf9223187a2f635b6f8be35c799089ea9a33e96cbc13f7f7e8a85ff4208.jpg)  
Source: Pacific Merchant Shipping Association

Exhibit 12: % of Containers Dwelling More than 5 Days  
![](images/b5189790c80fa36dd717ea746166fcfe008fed6d2177da11e08846ee84e47c95.jpg)  
Source: Pacific Merchant Shipping Association

Exhibit 13: Rail Container Dwell Time, Days  
![](images/e9324af051ae0ce9c592e50034060e368a6df35f305df7f9590f75f172d776bf.jpg)  
Source: Pacific Merchant Shipping Association

"Big Three" West Coast Ports' Inbound Loaded Containers

■ Total inbound containers for the Ports of LA, Long Beach, and Oakland +30% YoY in April. See our Big Three Note.

Exhibit 14: West Coast Ports' Inbound Loaded Containers +30% YoY in April

![](images/abf379919c63cda1df75b13eae94afea368507b771bb31e741d169a37041fc8a.jpg)  
Source: Port of Long Beach, Port of Los Angeles, Port of Oakland

Door to Door Shipping, China to US

It was taking an average of 47 days to ship (door to door) from China to the US in October, much closer to average pre-pandemic transit times when compared to peak congestion at 80+ days, and largely unchanged MoM vs 46 days in September. We assumed unchanged transit times in Nov-April for index updating purposes (given limited updates from data provider).

Exhibit 15: Door to Door Shipping Days, China to US

![](images/f08302233df49d23376d3af3e3682ef8b47357fc4364bccb6791acca27d83529.jpg)  
Source: Freightos

Trucking Employee Count

Truck transportation employee count was implied to be below pre-pandemic highs in May (-7.8% below pre-Covid); YoY growth has averaged -1.7% over the past six months. May's employee count was -0.3% sequentially.

Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted

![](images/4049716da7371455bf937273eaf11d385c57e1c76e2475038a6e67d5e4a00e6d.jpg)  
Source: US Bureau of Labor Statistics

LMI Capacity and Utilization

## ■ LMI Transportation Capacity Index

Transportation capacity contracted in May at a slower rate compared to April given the 31.7 reading; the reading increased relative to April's 28.4 reading (implying a slower contraction of capacity).

## ■ LMI Warehouse Capacity Index

☐ Warehouse capacity was expanding in May given the 50.5 reading; this result was up from April (indicating more available overall warehouse capacity).

## ■ LMI Warehouse Utilization Index

☐ Warehouse utilization showed expansion in May at a slower pace compared to April (62.9 reading vs 64.4 in April).

## PMI Supplier Delivery Times

\- Delivery times were expanding in May (i.e., below 50 indicates expanding delivery times) given the 41.4 reading; the May supplier delivery PMI index was +8.4% YoY.

Exhibit 17: PMI: Manufacturing Suppliers' Delivery Times, YoY, Seasonally Adjusted  
![](images/60c70322fe05a3c7a45268d27de3769e0e6f08474050687ffe802827643aa8ec.jpg)  
Source: IHS Markit

## Appendix

Given the importance supply chain fluidity has on retailers, consumer goods companies, inflationary pricing, etc., we think this scale's importance is tied most directly to the pace at which supply chain congestion is on the mend. To this end, we look at a variety of variables that we think tie directly, or in some cases indirectly, to overall congestion; including ships at anchor, days to deliver, various dwell times, intermodal volume and velocity statistics amongst others. Aggregating this data, we create the Supply Chain Congestion Scale – an attempt to quantify the balance between supply chains being “Fully Bottlenecked” and “Fully Open,” relative to the pre-pandemic benchmark we chose as Feb 3 $^{rd}$ , 2020. Basically, how fluid is the overall transport logistics network.

To det

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
