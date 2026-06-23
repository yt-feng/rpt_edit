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
CHINA PROPERTY WEEKLY WRAP

# Week 25 Wrap - Market activities saw pullback on holiday impact but underlying momentum remained steady

## Key highlights for the week:

Market performance: Transaction volume saw sequential pullback (-5% wow in primary and -20% wow) largely resulting from lighter volumes during the Dragon Boat Festival (June 19th-21st). On an ex-holiday basis, underlying momentum remained positive with primary markets improving 6% wow while secondary gained 2% wow, reaching 7% and 31% above MTD-June daily averages, respectively. Although broad market activities likewise moderated with new home searches dipping 0.4% wow while secondary subscription sales and visitations moderating \~15% wow, transaction price improved +0.8% wow across monitored cities, supported by more curtailed listing supply (-15% wow, sending MTD June -5% mom and -18% yoy).

## Key data points:

■ New homes sales volume was -5% wow and -18% yoy, while new home search activities were -0.4% wow.

Secondary transactions were $-20\%$ wow and $-13\%$ yoy, with price appreciation expectations edging lower for both home-sellers and agents.

MTD June: Primary GFA sold on median was -17% mom and was -21% yoy; Secondary GFA sold on median was -9% mom and +6% yoy.

YTD: Primary GFA sold on average was -12% yoy and was -11%/-42% vs. the 2024/2023 level; secondary GFA sold on average was flat yoy and was +20%/+9% vs. the 2024/2023 level.

\- Inventory balance was -0.1% wow, with inventory months at 27.7 (vs. average 28.5 in May-26).

Valuation: Our covered stronger SOE developers saw share price -12% wow on average, with Poly A (600048.SS, Neutral) outperforming at -4% wow; meanwhile, POE developers and other SOE developers saw share price on average -14%/-4% wow, respectively. Our offshore/onshore coverage now trades at an average 38%/31% discount to end-2026E NAV and at 0.5X/0.4X 2026E P/Bs.

## Implications:

■ Property sales in c.75 cities suggest top-100 developers' contract sales are likely to decline 8% yoy in

Yi Wang, CFA  
+86(21)2401-8930 |  
yi.wang@goldmansachs.cn  
GS (China) Securities  
Company Limited

Shi Xu  
+86(21)2401-8929 |  
shi.x.xu@goldmansachs.cn  
GS (China) Securities  
Company Limited

Kaiyan Jing  
+86(21)2411-8092 |  
kaiyan.jing@goldmansachs.cn  
GS (China) Securities  
Company Limited

June, vs. -2% in May.

■ Completions: MTD GSPC tracker indicates c.20% yoy decline in June (vs. -20% yoy/high-teens % yoy decline in May by NBS/GSe) and -1% yoy in FY26E per GSe.

■ New starts: New starts to record a high-twenties % yoy decline in June (vs. -25%/low-twenties % yoy decline in May by NBS/GSe), based on the land sales trends in 300 cities and nationwide cement shipment ratio.

■ GTV for BEKE (new and existing) likely rose 2% yoy in Apr-MTD June (-23%/+11% for new/existing).

## Primary market Week 25: GFA $-5\%$ wow and was $-18\%$ yoy, sending YTD to $-12\%$ yoy

Exhibit 1: Primary GFA sold last week was $-5\%$ wow and $-18\%$ yoy in c.75 cities  
![](images/2a3b9989f6b618d710cde355d5b19152d8362c7235fcbe0441ba01bb5287699b.jpg)

Exhibit 2: Primary GFA sold YTD on average was -12% yoy in c.75 cities, and -11%/-42% vs. 2024/2023 level  
![](images/f5f8b9d0fc661343df4d7e037a54c27ff7db8f61f31dc1a10fdc54610801e666.jpg)

Secondary market: Week 25/YTD volumes were $-20\% / -13\%$ yoy, with price appreciation expectations edging lower both home-sellers and agents

Exhibit 3: Secondary GFA sold last week was -20% wow and -13% yoy in c.20 cities

Average weekly volume of secondary property sales

![](images/2e58a927d4a9fd71290f195262410aa94e0358c44c23955f0d35d6e3ed70a24e.jpg)  
Source: Wind, GS Global Investment Research  
Exhibit 4: Secondary GFA sold YTD was flat yoy in c.20 cities, while +20%/+9% vs. 2024/2023  
2026 secondary volume sold vs. 2022-25

![](images/e64de6d76775c326e7830881e2117079c62c2e0add134117786415f9141eae39.jpg)  
Source: Wind, GS Global Investment Research

## Inventory Week 25: Inventory -0.2% wow and -4.7% from end-25 level, with inventory months at 27.7 (vs. average 28.5 in May-26)

Exhibit 7: Inventory balance was $-0.2\%$ wow, $-4.7\%$ from end-25 levels c.20 cities' total inventory breakdown by city tier

![](images/fc18353d95b1c87a78e9b0ff479103973ce1c0869042a22a45b5a63670ac4a41.jpg)  
Exhibit 8: Inventory month was $-0.6\%$ wow, representing $-0.9\%$ from end-25 levels c.20 cities' inventory months (12mth rolling) breakdown by city tier

![](images/fc8775d9f81a30217caa851f6b4f36424824fa791e8905f3fc0fe4bc8c426710.jpg)

## MTD GSPC implies c.20% yoy decline/-1% yoy in completions for June-26/FY26E per GSe

MTD GS Property Completion (GSPC) tracker indicates a c.20% yoy decline in June-26 (vs. -20% yoy/high-teens % yoy decline in May by NBS/GSe) and -1% yoy for FY26E per GSe, based on downstream supply/demand implied from our China float glass industry outlook and proprietary weekly float glass demand model.

Exhibit 9: MTD GSPC tracker implied monthly completions...
GSPC tracker implied monthly GFA completion - based on GS float glass S-D model

![](images/d98b12466fed0716f7061ceeca124be854c0ba49a84013d168636dfb7f570561.jpg)  
Jan-Feb refers to average level in Jan and Feb.  
Exhibit 10: ...suggesting completions at a c.20% yoy decline for June-26 % yoy change of GSPC - based on GS float glass S-D model

![](images/e34352d30762475404b303bd7a94e6c530be60043dc832549fe2192ca19969ae.jpg)  
Source: Sublime China Information, Wind, NBS, GS Global Investment Research

## Valuations: P/B valuation at downturn trough

Over week 25, our covered stronger SOE developers saw share price -12% wow on average, with Poly A (600048.SS, Neutral) outperforming at -4% wow; meanwhile, POE developers and other SOE developers saw share price on average -14%/-4% wow, respectively.

\- Our offshore coverage developers on average saw share prices -14% wow (vs. -4% for MSCI China); our onshore coverage developers averaged -5% wow (vs. +3% for CSI 300).

Our offshore coverage now trades at an average $38\%$ discount to end-2026E NAV and 0.5X 2026E P/B vs. 2H2008, 2H2011 and 1H2014 troughs of $39\%$ , 0.7X; $73\%$ , 0.9X; $58\%$ , 0.9X.

Our onshore coverage trades at an average 31% discount to end-2026E NAV and 0.4X 2026E P/B vs. 2H2008, 2H2011 and 1H2014 troughs of 67%, 1.6X; 64%, 1.5X; 61%, 1.2X.

Exhibit 11: Over week 25, our covered stronger SOE developers saw share price -12% wow on average, with Poly A (600048.SS, Neutral) outperforming at -4% wow; meanwhile, POE developers and other SOE developers saw share price on average -14%/-4% wow, respectively. Our offshore coverage developers on average saw share prices -14% wow (vs. -4% for MSCI China); our onshore coverage developers averaged -5% wow (vs. +3% for CSI 300).

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Type</td><td rowspan="2">Price as of 6/22/2026</td><td colspan="3">Share price performance</td></tr><tr><td>Past week</td><td>MTD</td><td>YTD</td></tr><tr><td colspan="3">Stronger SOE developers</td><td>(LCY)</td><td></td><td></td><td></td></tr><tr><td>CMSK</td><td>001979.SZ</td><td>Central SOE</td><td>7.3</td><td>-9%</td><td>-18%</td><td>-16%</td></tr><tr><td>COLI</td><td>0688.HK</td><td>Central SOE</td><td>13.1</td><td>-16%</td><td>-16%</td><td>7%</td></tr><tr><td>CR Land</td><td>1109.HK</td><td>Central SOE</td><td>31.2</td><td>-14%</td><td>-12%</td><td>15%</td></tr><tr><td>Greentown</td><td>3900.HK</td><td>Mixed ownership</td><td>7.0</td><td>-16%</td><td>-21%</td><td>-18%</td></tr><tr><td>Jinmao</td><td>0817.HK</td><td>Central SOE</td><td>1.4</td><td>-15%</td><td>-22%</td><td>12%</td></tr><tr><td>Poly</td><td>600048.SS</td><td>Central SOE</td><td>5.0</td><td>-4%</td><td>-13%</td><td>-18%</td></tr><tr><td colspan="4">Average</td><td>-12%</td><td>-17%</td><td>-3%</td></tr><tr><td colspan="3">POE developers</td><td>(LCY)</td><td></td><td></td><td></td></tr><tr><td>Gemdale</td><td>600383.SS</td><td>Mixed ownership</td><td>2.4</td><td>-7%</td><td>-15%</td><td>-23%</td></tr><tr><td>Longfor</td><td>0960.HK</td><td>POE</td><td>6.6</td><td>-22%</td><td>-16%</td><td>-23%</td></tr><tr><td>Seazen</td><td>1030.HK</td><td>POE</td><td>1.5</td><td>-12%</td><td>-20%</td><td>-29%</td></tr><tr><td colspan="4">Average</td><td>-14%</td><td>-17%</td><td>-25%</td></tr><tr><td colspan="3">Other SOE developers</td><td>(LCY)</td><td></td><td></td><td></td></tr><tr><td>OCT</td><td>000069.SZ</td><td>Central SOE</td><td>1.8</td><td>-4%</td><td>-9%</td><td>-29%</td></tr><tr><td>Vanke (A)</td><td>000002.SZ</td><td>Mixed ownership</td><td>3.1</td><td>-1%</td><td>-12%</td><td>-33%</td></tr><tr><td>Vanke (H)</td><td>2202.HK</td><td>Mixed ownership</td><td>2.5</td><td>-6%</td><td>-9%</td><td>-25%</td></tr><tr><td colspan="4">Average</td><td>-4%</td><td>-10%</td><td>-29%</td></tr><tr><td colspan="4">H-share average</td><td>-14%</td><td>-17%</td><td>-9%</td></tr><tr><td colspan="4">A-share average</td><td>-5%</td><td>-13%</td><td>-24%</td></tr><tr><td colspan="4">Value chain Index</td><td></td><td></td><td></td></tr><tr><td colspan="4">Construction materials</td><td>10%</td><td>10%</td><td>40%</td></tr><tr><td colspan="4">Construction companies</td><td>1%</td><td>-1%</td><td>-1%</td></tr><tr><td colspan="4">Building products</td><td>-1%</td><td>-4%</td><td>-4%</td></tr><tr><td colspan="4">Decoration companies</td><td>1%</td><td>-7%</td><td>-7%</td></tr><tr><td colspan="4">Home appliances</td><td>-3%</td><td>-4%</td><td>-8%</td></tr><tr><td colspan="4">Home furnishing</td><td>-3%</td><td>-7%</td><td>-14%</td></tr></table>

Construction Materials Index (801710.SI), Construction Companies Index (801720.SI), Building Products Index (801713.SI), Decoration Companies Index (801722.SI), Home Appliances Index (801110.SI) and Home Furnishing Index (801142.SI) as compiled by Wind.

Source: Datastream, Wind, Data compiled by GS Global Investment Research

Exhibit 12: China developers' valuation comparisons

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td colspan="2">Daily liquidity (US$ mn)</td><td colspan="3">Price as of</td><td rowspan="2">12 mth Price target</td><td rowspan="2">Potential upside/ downside (%)</td><td rowspan="2">Target price disc. to NAV</td><td rowspan="2">End-26E NAV</td><td rowspan="2">Shr price (disc)/ prem to NAV</td><td colspan="4">FD Core P/E (x)</td><td colspan="4">P/B (x) (excl. revaluation gain)</td><td colspan="4">Dividend yield (%)</td></tr><tr><td>Mkt Cap (US$ bn)</td><td>1 mth trailing</td><td>Type</td><td>Rating</td><td>22/Jun/26</td><td>25</td><td>26E</td><td>27E</td><td>28E</td><td>25</td><td>26E</td><td>27E</td><td>28E</td><td>25</td><td>26E</td><td>27E</td><td>28E</td></tr><tr><td colspan="24"></td></tr><tr><td colspan="24">Developers</td></tr><tr><td colspan="24">Stronger SOE developers</td></tr><tr><td>CMSK</td><td>001979.SZ</td><td>9.7</td><td>100</td><td>Central SOE</td><td>Neutral</td><td>7.25 (Rmb)</td><td>10.10</td><td>39</td><td>-15%</td><td>11.93</td><td>(39)</td><td>n.m.</td><td>17.9</td><td>14.9</td><td>13.7</td><td>0.7</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.7</td><td>2.5</td><td>3.0</td><td>3.3</td></tr><tr><td>COLI</td><td>0688.HK</td><td>18.3</td><td>95</td><td>Central SOE</td><td>Buy</td><td>13.1 (HK$)</td><td>14.70</td><td>12</td><td>-10%</td><td>16.39</td><td>(20)</td><td>10.1</td><td>10.0</td><td>9.6</td><td>8.6</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.4</td><td>3.7</td><td>4.0</td><td>4.2</td><td>4.7</td></tr><tr><td>CR Land</td><td>1109.HK</td><td>28.4</td><td>154</td><td>Central SOE</td><td>Buy</td><td>31.2 (HK$)</td><td>36.60</td><td>17</td><td>-10%</td><td>40.70</td><td>(23)</td><td>9.1</td><td>8.3</td><td>8.2</td><td>8.0</td><td>1.0</td><td>0.9</td><td>0.8</td><td>0.8</td><td>4.1</td><td>4.7</td><td>4.8</td><td>4.9</td></tr><tr><td>Greentown</td><td>3900.HK</td><td>2.3</td><td>15</td><td>Mixed ownership</td><td>Buy</td><td>7.0 (HK$)</td><td>11.10</td><td>59</td><td>-15%</td><td>13.02</td><td>(46)</td><td>3.3</td><td>3.6</td><td>3.5</td><td>3.3</td><td>0.5</td><td>0.4</td><td>0.4</td><td>0.4</td><td>-</td><td>2.9</td><td>5.2</td><td>7.7</td></tr><tr><td>Jinmao</td><td>0817.HK</td><td>2.3</td><td>16</td><td>Central SOE</td><td>Buy</td><td>1.4 (HK$)</td><td>1.70</td><td>26</td><td>-10%</td><td>1.89</td><td>(29)</td><td>34.4</td><td>19.2</td><td>10.0</td><td>5.4</td><td>0.6</td><td>0.6</td><td>0.5</td><td>0.5</td><td>2.2</td><td>2.2</td><td>4.3</td><td>7.8</td></tr><tr><td>Poly</td><td>600048.SS</td><td>8.9</td><td>136</td><td>Central SOE</td><td>Neutral</td><td>5.00 (Rmb)</td><td>6.50</td><td>30</td><td>-10%</td><td>7.24</td><td>(31)</td><td>57.8</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.7</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="8">Average</td><td>31</td><td>-12%</td><td></td><td>(31)</td><td>10.1</td><td>10.0</td><td>9.6</td><td>8.0</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.5</td><td>1.9</td><td>2.7</td><td>3.6</td><td>4.7</td></tr><tr><td colspan="24">POE developers</td></tr><tr><td>Gemdale</td><td>600383.SS</td><td>1.6</td><td>38</td><td>Mixed ownership</td><td>Sell</td><td>2.35 (Rmb)</td><td>2.70</td><td>15</td><td>-20%</td><td>3.40</td><td>(31)</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Longfor</td><td>0960.HK</td><td>6.0</td><td>23</td><td>POE</td><td>Neutral</td><td>6.6 (HK$)</td><td>8.70</td><td>32</td><td>-25%</td><td>11.55</td><td>(43)</td><td>n.m.</td><td>n.m.</td><td>19.6</td><td>12.8</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>1.2</td><td>-</td><td>1.6</td><td>2.5</td></tr><tr><td>Seazen</td><td>1030.HK</td><td>1.3</td><td>8</td><td>POE</td><td>Sell</td><td>1.5 (HK$)</td><td>1.80</td><td>24</td><td>-50%</td><td>3.64</td><td>(60)</td><td>24.6</td><td>36.6</td><td>17.0</td><td>9.6</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="8">Average</td><td>24</td><td>-32%</td><td></td><td>(45)</td><td>24.6</td><td>36.6</td><td>18.3</td><td>11.2</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.4</td><td>-</td><td>0.5</td><td>0.8</td></tr><tr><td colspan="24">Other SOE developers</td></tr><tr><td>OCT</td><td>000069.SZ</td><td>2.1</td><td>18</td><td>Central SOE</td><td>Sell</td><td>1.77 (Rmb)</td><td>1.50</td><td>(15)</td><td>-20%</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>0.4</td><td>0.4</td><td>0.5</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Vanke (A)</td><td>000002.SZ</td><td>4.5</td><td>86</td><td>Mixed ownership</td><td>Sell</td><td>3.11 (Rmb)</td><td>3.70</td><td>19</td><td>-10%</td><td>4.10</td><td>(24)</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>0.3</td><td>0.4</td><td>0.4</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Vanke (H)</td><td>2202.HK</td><td>0.7</td><td>11</td><td>Mixed ownership</td><td>Sell</td><td>2.47 (HK$)</td><td>2.90</td><td>17</td><td>-35%</td><td>4.47</td><td>(45)</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>0.2</td><td>0.3</td><td>0.3</td><td>0.3</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="8">Average</td><td>7</td><td>-22%</td><td></td><td>(34)</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>0.3</td><td>0.4</td><td>0.4</td><td>0.4</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="24"></td></tr><tr><td colspan="8">Coverage average</td><td colspan="3">23</td><td>(36)</td><td>23.2</td><td>15.9</td><td>11.8</td><td>8.8</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.4</td><td>1.1</td><td>1.4</td><td>1.9</td><td>2.6</td></tr><tr><td colspan="24"></td></tr><tr><td colspan="8">H-share average</td><td colspan="3">27</td><td>(38)</td><td>16.3</td><td>15.5</td><td>11.3</td><td>8.0</td><td>0.5</td><td>0.5</td><td>0.4</td><td>0.4</td><td>1.6</td><td>2.0</td><td>2.9</td><td>3.9</td></tr><tr><td colspan="8">A-share average</td><td colspan="3">18</td><td>(31)</td><td>57.8</td><td>17.9</td><td>14.9</td><td>13.7</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.3</td><td>0.5</td><td>0.6</td><td>0.7</td></tr></table>

## Note:

Our 12-month target prices are based on end-2026E NAV for our coverage universe except for OCT.

Our OCT TP is based on SOTP of its property development (valued by NAV) and its tourism business (valued by P/E).

Source: Datastream, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Yi Wang, CFA, Shi Xu and Kaiyan Jing, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Contributing Authors: Yi Wang, CFA GS (China) Securities Company Limited, Shi Xu GS (China) Securities Company Limited, Kaiyan Jing GS (China) Securities Company Limited.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trad

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and

https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
