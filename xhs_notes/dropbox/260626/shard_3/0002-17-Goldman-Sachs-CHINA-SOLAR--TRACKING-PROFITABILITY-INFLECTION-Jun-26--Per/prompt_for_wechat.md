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
CHINA SOLAR: TRACKING PROFITABILITY INFLECTION

# Jun-26: Persistent upstream pricing softness against worsening inventory expectations

Our China Solar Profitability Tracker follows monthly supply/demand and inventory dynamics by sub-sector, and spot prices/input costs implied cash GP & EBITDA margin trends for companies under our coverage.

## Key highlights in Jun MTD:

Pricing softness persisted across upstream segments in Jun: Throughout the month, pricing declined by an avg. 5% across the solar value chain. Specifically, Film (-12% MTD) and Cell (-11% MTD) led the price weakness due to lower oil price (-8% MoM) and lower silver cost (-13% MTD) amid surging producer-side inventory during the period (+21% MoM), respectively. In terms of profitability, lower pricing has led to 8pp/7pp/4pp/3pp deterioration in Cell/Film/Poly/Glass, while margin slightly improved by 2pp MTD for Module due to easing cost pressure. Looking forward, we think pricing softness will persist considering i) worsening inventory outlook into the weak demand season in Jul-Aug, and ii) lower Module production cost due to softening upstream prices and adoption of cheap metal technology by Tier 1 players staring from 3Q.

Global Module demand declined by 22% mom and 79% yoy to 29GW in May 2026, sending 5M26 down by 46% yoy to 193GW, which is tracking below our FY26E forecast of -12% yoy, mainly due to weaker demand in China (-91% yoy in May and -70% yoy in 5M26).

What to do from here? Across our coverage, we prefer Maxwell (on new application opportunity), Hangzhou First (on solar film price hike and unit profitability expansion potential) and Longi (on ESS potential and more resilient EBITDA driven by upstream price decline with mid-cycle BC upside). We stay cautious on Rod Poly (Neutral/Sell on Daqo ADR/A, and Sell on Tongwei), and Glass (Sell on Flat A/H).

Mengwen Wang
+86(21)2401-8932 |
mengwen.wang@goldmansachs.cn
GS (China) Securities
Company Limited

Jacqueline Du
+852-2978-1783 |
jacqueline.du@gs.com
GS (Asia) L.L.C.

## Profitability improved in Module but deteriorated in upstream segments

Exhibit 1: Pricing softness persisted across upstream segments in Jun Summary of the latest pricing across the solar value chain

<table><tr><td colspan="11">Spot price</td><td colspan="3">Average price</td></tr><tr><td>Price</td><td></td><td>Weekly 6/25/2026</td><td>Monthly Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>MTD Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>Since anti-involution 7/2/2025</td><td>Since anti-monopoly 1/7/2026</td><td>MoM Jun-26</td><td>QoQ 2026Q2</td><td>YTD yoy 2026</td></tr><tr><td>Poly</td><td></td><td></td><td></td><td></td><td></td><td>-6%</td><td>-19%</td><td>-37%</td><td>-4%</td><td>-37%</td><td>-4%</td><td>-30%</td><td>-5%</td></tr><tr><td>N+Granular Poly</td><td>Rmb/kg</td><td>32.5</td><td>33.1</td><td>34.2</td><td>40.8</td><td>-5%</td><td>-20%</td><td>-36%</td><td>-3%</td><td>-36%</td><td>-3%</td><td>-29%</td><td>-4%</td></tr><tr><td>N+Rod Poly</td><td>Rmb/kg</td><td>33.2</td><td>33.8</td><td>35.0</td><td>42.3</td><td>-6%</td><td>-18%</td><td>-38%</td><td>-4%</td><td>-38%</td><td>-4%</td><td>-30%</td><td>-6%</td></tr><tr><td>Poly Future Quotes (Max)</td><td>Rmb/kg</td><td>42.5</td><td>41.5</td><td>41.4</td><td>45.0</td><td>5%</td><td>10%</td><td>-30%</td><td>15%</td><td>-30%</td><td>-1%</td><td>-15%</td><td>-7%</td></tr><tr><td>Poly Future Quotes (Median)</td><td>Rmb/kg</td><td>36.7</td><td>36.6</td><td>38.2</td><td>43.0</td><td>0%</td><td>-4%</td><td>-39%</td><td>5%</td><td>-39%</td><td>-4%</td><td>-21%</td><td>-7%</td></tr><tr><td>Poly Future Quotes (Min)</td><td>Rmb/kg</td><td>35.9</td><td>35.5</td><td>34.7</td><td>40.4</td><td>0%</td><td>0%</td><td>-38%</td><td>6%</td><td>-38%</td><td>4%</td><td>-25%</td><td>-11%</td></tr><tr><td>Non-China produced Poly</td><td>US$/kg</td><td>18.5</td><td>18.5</td><td>18.5</td><td>18.5</td><td>0%</td><td>0%</td><td>3%</td><td>-3%</td><td>3%</td><td>0%</td><td>0%</td><td>-3%</td></tr><tr><td>Spread: Rod-Granular</td><td>Rmb/kg</td><td>0.7</td><td>0.7</td><td>0.8</td><td>1.4</td><td>-0.3</td><td>0.7</td><td>-2.7</td><td>-0.5</td><td>-2.7</td><td>-0.3</td><td>-1.3</td><td>-1.0</td></tr><tr><td>Spread: Max Future - Spot</td><td>Rmb/kg</td><td>9.3</td><td>7.7</td><td>6.5</td><td>2.8</td><td>4.1</td><td>11.1</td><td>2.9</td><td>6.9</td><td>2.1</td><td>1.2</td><td>7.7</td><td>n.a.</td></tr><tr><td>Spread: Median Future - Spot</td><td>Rmb/kg</td><td>3.5</td><td>2.8</td><td>3.2</td><td>0.7</td><td>2.1</td><td>5.7</td><td>-2.4</td><td>3.2</td><td>-2.6</td><td>0.0</td><td>5.2</td><td>n.a.</td></tr><tr><td>Spread: Min Future - Spot</td><td>Rmb/kg</td><td>2.7</td><td>1.7</td><td>-0.3</td><td>-1.8</td><td>2.2</td><td>7.3</td><td>-1.7</td><td>3.4</td><td>-1.4</td><td>2.9</td><td>3.3</td><td>n.a.</td></tr><tr><td>Wafer</td><td></td><td></td><td></td><td></td><td></td><td>-1%</td><td>-8%</td><td>-24%</td><td>1%</td><td>-30%</td><td>-1%</td><td>-20%</td><td>-11%</td></tr><tr><td>N+M10</td><td>Rmb/pc</td><td>0.9</td><td>0.91</td><td>0.93</td><td>1.05</td><td>-3%</td><td>-9%</td><td>-25%</td><td>5%</td><td>-31%</td><td>-2%</td><td>-21%</td><td>-9%</td></tr><tr><td>N+G12L (USS)</td><td>Rmb/pc</td><td>1.2</td><td>1.17</td><td>1.18</td><td>1.33</td><td>0%</td><td>-9%</td><td>-23%</td><td>-2%</td><td>-30%</td><td>0%</td><td>-20%</td><td>-12%</td></tr><tr><td>N+G12R (DS)</td><td>Rmb/pc</td><td>1.0</td><td>0.99</td><td>1.00</td><td>1.13</td><td>-1%</td><td>-7%</td><td>-24%</td><td>-1%</td><td>-30%</td><td>-1%</td><td>-21%</td><td>-11%</td></tr><tr><td>Cell-China</td><td></td><td></td><td></td><td></td><td></td><td>-11%</td><td>-23%</td><td>-13%</td><td>20%</td><td>-22%</td><td>-6%</td><td>-22%</td><td>31%</td></tr><tr><td>Topcon G12L-China (USS)</td><td>Rmb/w</td><td>0.30</td><td>0.31</td><td>0.33</td><td>0.37</td><td>-10%</td><td>-21%</td><td>-12%</td><td>22%</td><td>-21%</td><td>-4%</td><td>-21%</td><td>30%</td></tr><tr><td>Topcon G12R-China (DS)</td><td>Rmb/w</td><td>0.29</td><td>0.30</td><td>0.33</td><td>0.37</td><td>-12%</td><td>-26%</td><td>-15%</td><td>18%</td><td>-24%</td><td>-8%</td><td>-22%</td><td>32%</td></tr><tr><td>Cell-Ex-China</td><td></td><td></td><td></td><td></td><td></td><td>-12%</td><td>-19%</td><td>5%</td><td>n.m.</td><td>n.m.</td><td>-9%</td><td>-13%</td><td>36%</td></tr><tr><td>Topcon M10-Ex-China</td><td>US$/w</td><td>0.04</td><td>0.04</td><td>0.05</td><td>0.05</td><td>-12%</td><td>-19%</td><td>5%</td><td>n.m.</td><td>n.m.</td><td>-9%</td><td>-13%</td><td>36%</td></tr><tr><td>Module-China</td><td></td><td></td><td></td><td></td><td></td><td>0%</td><td>-1%</td><td>6%</td><td>7%</td><td>6%</td><td>0%</td><td>2%</td><td>6%</td></tr><tr><td>Bifacial Topcon-China</td><td>Rmb/w</td><td>0.74</td><td>0.74</td><td>0.75</td><td>0.74</td><td>0%</td><td>-3%</td><td>6%</td><td>9%</td><td>6%</td><td>-1%</td><td>2%</td><td>7%</td></tr><tr><td>NBC-China</td><td>Rmb/w</td><td>0.86</td><td>0.86</td><td>0.86</td><td>0.85</td><td>0%</td><td>0%</td><td>13%</td><td>8%</td><td>10%</td><td>0%</td><td>3%</td><td>10%</td></tr><tr><td>Topcon USS-China</td><td>Rmb/w</td><td>0.72</td><td>0.72</td><td>0.71</td><td>0.70</td><td>0%</td><td>3%</td><td>5%</td><td>7%</td><td>5%</td><td>0%</td><td>3%</td><td>3%</td></tr><tr><td>Topcon DS-China</td><td>Rmb/w</td><td>0.76</td><td>0.76</td><td>0.77</td><td>0.76</td><td>-1%</td><td>-4%</td><td>8%</td><td>13%</td><td>8%</td><td>-1%</td><td>2%</td><td>9%</td></tr><tr><td>Spread: NBC-Topcon</td><td>Rmb/w</td><td>0.11</td><td>0.10</td><td>0.09</td><td>0.08</td><td>0.01</td><td>0.04</td><td>0.04</td><td>-0.03</td><td>0.02</td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>Module-Export</td><td></td><td></td><td></td><td></td><td></td><td>-1%</td><td>9%</td><td>24%</td><td>n.m.</td><td>n.m.</td><td>-1%</td><td>16%</td><td>14%</td></tr><tr><td>Topcon Export</td><td>US$/w</td><td>0.12</td><td>0.12</td><td>0.12</td><td>0.11</td><td>0%</td><td>11%</td><td>29%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>20%</td><td>18%</td></tr><tr><td>BC C&amp;I EU</td><td>US$/w</td><td>0.14</td><td>0.14</td><td>0.14</td><td>0.13</td><td>-3%</td><td>1%</td><td>21%</td><td>n.m.</td><td>n.m.</td><td>-2%</td><td>11%</td><td>15%</td></tr><tr><td>BS Resi EU</td><td>US$/w</td><td>0.20</td><td>0.20</td><td>0.20</td><td>0.19</td><td>-1%</td><td>14%</td><td>22%</td><td>n.m.</td><td>n.m.</td><td>-1%</td><td>17%</td><td>7%</td></tr><tr><td>Module-US</td><td></td><td></td><td></td><td></td><td></td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>7%</td></tr><tr><td>Imported from Ex-China</td><td>US$/w</td><td>0.27</td><td>0.27</td><td>0.27</td><td>0.27</td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>7%</td></tr><tr><td>Local assembled</td><td>US$/w</td><td>0.30</td><td>0.30</td><td>0.30</td><td>0.30</td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>8%</td></tr><tr><td>Module-India</td><td></td><td></td><td></td><td></td><td></td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>-1%</td></tr><tr><td>Local assembled</td><td>US$/w</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0%</td><td>0%</td><td>0%</td><td>n.m.</td><td>n.m.</td><td>0%</td><td>0%</td><td>-1%</td></tr><tr><td>Glass</td><td></td><td></td><td></td><td></td><td></td><td>-2%</td><td>-15%</td><td>-27%</td><td>-21%</td><td>-21%</td><td>-6%</td><td>-15%</td><td>-23%</td></tr><tr><td>2.0mm PV glass</td><td>Rmb/sqm</td><td>8.3</td><td>8.1</td><td>8.7</td><td>9.5</td><td>-2%</td><td>-15%</td><td>-27%</td><td>-21%</td><td>-21%</td><td>-6%</td><td>-15%</td><td>-23%</td></tr><tr><td>Film</td><td></td><td></td><td></td><td></td><td></td><td>-12%</td><td>-8%</td><td>15%</td><td>11%</td><td>17%</td><td>-11%</td><td>29%</td><td>10%</td></tr><tr><td>EVA film (Transparent)</td><td>Rmb/sqm</td><td>5.9</td><td>6.1</td><td>7.1</td><td>6.3</td><td>-18%</td><td>-16%</td><td>10%</td><td>3%</td><td>13%</td><td>-15%</td><td>30%</td><td>7%</td></tr><tr><td>EVA film (White)</td><td>Rmb/sqm</td><td>6.4</td><td>6.6</td><td>7.6</td><td>6.8</td><td>-16%</td><td>-15%</td><td>9%</td><td>3%</td><td>12%</td><td>-14%</td><td>28%</td><td>7%</td></tr><tr><td>POE film</td><td>Rmb/sqm</td><td>10.4</td><td>10.5</td><td>10.8</td><td>9.6</td><td>-3%</td><td>7%</td><td>27%</td><td>27%</td><td>27%</td><td>-2%</td><td>29%</td><td>16%</td></tr><tr><td>Spread: POE-EVA</td><td>Rmb/sqm</td><td>4.3</td><td>4.1</td><td>3.5</td><td>3.1</td><td>1.0</td><td>1.8</td><td>1.7</td><td>1.0</td><td>1.6</td><td>0.9</td><td>0.8</td><td>0.9</td></tr><tr><td>EVA resin</td><td>Rmb/ton</td><td>9,200</td><td>9,407</td><td>10,924</td><td>10,407</td><td>-4%</td><td>-27%</td><td>3%</td><td>-6%</td><td>1%</td><td>-12%</td><td>10%</td><td>0%</td></tr><tr><td>POE resin</td><td>Rmb/ton</td><td>15,082</td><td>15,082</td><td>15,272</td><td>12,410</td><td>-1%</td><td>35%</td><td>63%</td><td>43%</td><td>65%</td><td>-1%</td><td>60%</td><td>17%</td></tr><tr><td>Spread: POE-EVA resin</td><td>Rmb/ton</td><td>5,882</td><td>5,675</td><td>4,348</td><td>2,003</td><td>195</td><td>7,279</td><td>5,627</td><td>1,387</td><td>6,225</td><td>1,180</td><td>4,691</td><td>1,894</td></tr></table>

Source: Oilchem, SiliconChina, PVInfolink, SMM, Solarbe

Exhibit 2: Jun spot price implied cash profitability improved in Module but deteriorated in upstream segments
Summary of spot price implied cash GPM and unit GP across the solar value chain

<table><tr><td rowspan="2"></td><td colspan="4">Spot price implied cash GPM</td><td colspan="6">Spot cash GPM change (in ppt)</td><td colspan="3">Average cash GPM change (in ppt)</td></tr><tr><td>Weekly 6/25/2026</td><td>Monthly Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>MTD Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>Since anti-involution 7/2/2025</td><td>Since anti-monopoly 1/7/2026</td><td>mom Jun-26</td><td>qoq 2026Q2</td><td>YTD yoy 2026</td><td></td></tr><tr><td>Poly-Tier 1</td><td>4%</td><td>8%</td><td>7%</td><td>20%</td><td>-4ppt</td><td>-14ppt</td><td>-32ppt</td><td>0ppt</td><td>-34ppt</td><td>0ppt</td><td>-26ppt</td><td>-2ppt</td><td></td></tr><tr><td>Rod Poly</td><td>-8%</td><td>-2%</td><td>-6%</td><td>8%</td><td>-2ppt</td><td>-11ppt</td><td>-36ppt</td><td>0ppt</td><td>-39ppt</td><td>4ppt</td><td>-29ppt</td><td>-4ppt</td><td></td></tr><tr><td>Granular Poly</td><td>15%</td><td>17%</td><td>20%</td><td>31%</td><td>-6ppt</td><td>-18ppt</td><td>-27ppt</td><td>1ppt</td><td>-29ppt</td><td>-4ppt</td><td>-23ppt</td><td>1ppt</td><td></td></tr><tr><td>Wafer-Tier 1</td><td>-3%</td><td>-3%</td><td>-4%</td><td>-3%</td><td>0ppt</td><td>5ppt</td><td>1ppt</td><td>8ppt</td><td>-11ppt</td><td>0ppt</td><td>-2ppt</td><td>-6ppt</td><td></td></tr><tr><td>M10</td><td>-9%</td><td>-9%</td><td>-9%</td><td>-7%</td><td>-1ppt</td><td>4ppt</td><td>-2ppt</td><td>11ppt</td><td>-14ppt</td><td>-1ppt</td><td>-4ppt</td><td>-5ppt</td><td></td></tr><tr><td>G12</td><td>3%</td><td>3%</td><td>1%</td><td>1%</td><td>2ppt</td><td>6ppt</td><td>4ppt</td><td>4ppt</td><td>-7ppt</td><td>1ppt</td><td>-1ppt</td><td>-7ppt</td><td></td></tr><tr><td>Cell-Tier 1</td><td>-6%</td><td>-2%</td><td>2%</td><td>6%</td><td>-8ppt</td><td>-15ppt</td><td>-13ppt</td><td>1ppt</td><td>-7ppt</td><td>-3ppt</td><td>-8ppt</td><td>8ppt</td><td></td></tr><tr><td>Topcon G12R China (USS)</td><td>-7%</td><td>-3%</td><td>1%</td><td>6%</td><td>-9ppt</td><td>-16ppt</td><td>-14ppt</td><td>0ppt</td><td>-8ppt</td><td>-4ppt</td><td>-9ppt</td><td>9ppt</td><td></td></tr><tr><td>Topcon G12L China (DS)</td><td>-6%</td><td>-1%</td><td>2%</td><td>6%</td><td>-8ppt</td><td>-13ppt</td><td>-12ppt</td><td>2ppt</td><td>-6ppt</td><td>-3ppt</td><td>-8ppt</td><td>8ppt</td><td></td></tr><tr><td>Module-Tier 1</td><td>11%</td><td>12%</td><td>10%</td><td>5%</td><td>2ppt</td><td>8ppt</td><td>5ppt</td><td>4ppt</td><td>18ppt</td><td>3ppt</td><td>10ppt</td><td>1ppt</td><td></td></tr><tr><td>Topcon China (pure module)</td><td>12%</td><td>12%</td><td>9%</td><td>2%</td><td>4ppt</td><td>13ppt</td><td>10ppt</td><td>3ppt</td><td>22ppt</td><td>4ppt</td><td>15ppt</td><td>-1ppt</td><td></td></tr><tr><td>Topcon China (poly to module integrated)</td><td>10%</td><td>12%</td><td>10%</td><td>6%</td><td>1ppt</td><td>7ppt</td><td>2ppt</td><td>4ppt</td><td>14ppt</td><td>3ppt</td><td>7ppt</td><td>1ppt</td><td></td></tr><tr><td>Topcon China (wafer to module integrated)</td><td>10%</td><td>12%</td><td>10%</td><td>5%</td><td>1ppt</td><td>7ppt</td><td>5ppt</td><td>4ppt</td><td>17ppt</td><td>3ppt</td><td>9ppt</td><td>1ppt</td><td></td></tr><tr><td>Topcon China (cell to module integrated)</td><td>10%</td><td>12%</td><td>10%</td><td>5%</td><td>1ppt</td><td>6ppt</td><td>4ppt</td><td>3ppt</td><td>19ppt</td><td>2ppt</td><td>10ppt</td><td>3ppt</td><td></td></tr><tr><td>Glass-Tier 1</td><td>-33%</td><td>-37%</td><td>-25%</td><td>-10%</td><td>-3ppt</td><td>-27ppt</td><td>-46ppt</td><td>-24ppt</td><td>-41ppt</td><td>-9ppt</td><td>-28ppt</td><td>-19ppt</td><td></td></tr><tr><td>2.0mm PV glass</td><td>-33%</td><td>-37%</td><td>-25%</td><td>-10%</td><td>-3ppt</td><td>-27ppt</td><td>-46ppt</td><td>-24ppt</td><td>-41ppt</td><td>-9ppt</td><td>-28ppt</td><td>-19ppt</td><td></td></tr><tr><td>Film-Tier 1</td><td>23%</td><td>24%</td><td>26%</td><td>25%</td><td>-7ppt</td><td>-3ppt</td><td>-2ppt</td><td>1ppt</td><td>-1ppt</td><td>-3ppt</td><td>3ppt</td><td>4ppt</td><td></td></tr><tr><td>EVA film</td><td>19%</td><td>20%</td><td>23%</td><td>16%</td><td>-12ppt</td><td>7ppt</td><td>6ppt</td><td>6ppt</td><td>9ppt</td><td>-4ppt</td><td>15ppt</td><td>5ppt</td><td></td></tr><tr><td>POE film</td><td>27%</td><td>27%</td><td>29%</td><td>33%</td><td>-1ppt</td><td>-12ppt</td><td>-11ppt</td><td>-4ppt</td><td>-11ppt</td><td>-1ppt</td><td>-9ppt</td><td>2ppt</td><td></td></tr><tr><td>EVA resin</td><td>-5%</td><td>-5%</td><td>-5%</td><td>2%</td><td>3ppt</td><td>-2ppt</td><td>-10ppt</td><td>-13ppt</td><td>-11ppt</td><td>-2ppt</td><td>-14ppt</td><td>-13ppt</td><td></td></tr></table>

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Spot price implied unit cash profit</td><td colspan="5">Spot cash profit change (in $)</td><td colspan="3">Average cash profit change (in $)</td></tr><tr><td>Weekly 6/25/2026</td><td>Monthly Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>MTD Jun-26</td><td>QTD 2026Q2</td><td>YTD 2026</td><td>Since anti-involution 7/2/2025</td><td>Since anti-monopoly 7/2/2025</td><td>mom Jun-26</td><td>qoq 2026Q2</td><td>YTD yoy 2026</td></tr><tr><td>Poly</td><td></td><td>1.0</td><td>2.5</td><td>2.4</td><td>8.0</td><td>-1.2</td><td>-5.4</td><td>-15.1</td><td>0.1</td><td>-16.3</td><td>0.3</td><td>-11.9</td><td>-0.1</td></tr><tr><td>Rod Poly</td><td>Rmb/kg</td><td>-2.3</td><td>-0.7</td><td>-2.0</td><td>3.4</td><td>-0.4</td><td>-3.3</td><td>-15.5</td><td>0.1</td><td>-17.0</td><td>1.2</td><td>-12.1</td><td>-1.4</td></tr><tr><td>Granular Poly</td><td>Rmb/kg</td><td>4.4</td><td>5.7</td><td>6.7</td><td>12.7</td><td>-1.9</td><td>-7.5</td><td>-14.7</td><td>0.1</td><td>-15.6</td><td>-0.7</td><td>-11.6</td><td>1.2</td></tr><tr><td>Wafer</td><td></td><td>0.00</td><td>0.00</td><td>0.00</td><td>-0.003</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.01</td><td>-0.01</td><td>0.00</td><td>0.00</td><td>-0.01</td></tr><tr><td>N+M10 Wafer</td><td>Rmb/w</td><td>-0.010</td><td>-0.009</td><td>-0.01</td><td>-0.008</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.01</td><td>-0.02</td><td>0.00</td><td>0.00</td><td>-0.01</td></tr><tr><td>N+G12 Wafer</td><td>Rmb/w</td><td>0.004</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.00</td><td>-0.01</td><td>0.00</td><td>0.00</td><td>-0.01</td></tr><tr><td>Cell</td><td></td><td>-0.017</td><td>-0.005</td><td>0.00</td><td>0.02</td><td>0.80</td><td>3.06</td><td>1.47</td><td>0.12</td><td>1.32</td><td>-0.01</td><td>-0.01</td><td>0.02</td></tr><tr><td>Topcon G12R China (USS)</td><td>Rmb/w</td><td>-0.020</td><td>-0.007</td><td>0.00</td><td>0.02</td><td>0.80</td><td>3.06</td><td>1.41</td><td>-0.03</td><td>1.42</td><td>-0.01</td><td>-0.03</td><td>0.03</td></tr><tr><td>Topcon G12L China (DS)</td><td>Rmb/w</td><td>-0.014</td><td>-0.003</td><td>0.01</td><td>0.02</td><td>0.81</td><td>3.05</td><td>1.53</td><td>0.27</td><td>1.22</td><td>0.00</td><td>0.01</td><td>0.02</td></tr><tr><td>Module</td><td></td><td>0.072</td><td>0.08</td><td>0.06</td><td>0.03</td><td>0.01</td><td>0.06</td><td>0.04</td><td>0.03</td><td>0.11</td><td>0.02</td><td>0.07</td><td>0.00</td></tr><tr><td>Topcon M10 (pure module)</td><td>Rmb/w</td><td>0.081</td><td>0.08</td><td>0.06</td><td>0.01</td><td>0.03</td><td>0.08</td><td>0.06</td><td>0.03</td><td>0.14<

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the

products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
