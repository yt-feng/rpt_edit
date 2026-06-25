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
- 已识别机构名：`DB`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份DB研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Asia Europe North America

Industry
DB Luxury 360

Consumer Discretionary & Luxury
Luxury Goods

Date\n23 June 2026

Industry Update

# China luxury import: Slower April-May vs. months of 1Q

## DB view

Luxury imports sequentially declined in 2Q26 (April-May) to -7.2% YoY vs. 5.0% YoY in 1Q26, on simple average terms. Strongest decline was in handbags -11.2% YoY, followed by jewellery -8.6% YoY and -1.9% in watches, all in unit terms. In terms of monthly evolution, all categories were down negative YoY in May, except for watches. Jewellery and watches sequentially improved by +2.3% and +9.8% pts, respectively.

From a macro data perspective, weaker YoY in retail and household wealth points to a discretionary spending environment that is tougher for a gradual cFX sales growth recovery. Home prices remain down YoY at -4.8% vs. -4.9% in April and stock market returns slowed to +14.8% vs. +21% in April. This implies the pace of consumer confidence YoY may slow further (latest available as of April at +1.4% vs. +3.3% during the months of 1Q26), which can act as headwind for the sector recovery in the region.

## Summary of 2Q26 data points

Import (in unit YoY terms): Total handbags -11.2% vs. +5.1% in 1Q26; leather handbags -9.8% vs. +2.5%; non-leather -12.4% vs. +7.5%; jewellery -8.6% vs. -6.0%/Retail: Apparel & footwear +1.5% vs. +6.5%; Gold, silver & jewellery -17.1% vs. +10.6%/Wealth: Nationwide home prices -4.8% vs. -4.9%; SSE HSI avg +17.9% vs. +21.2%.

## Summary of May data points

Import (in unit YoY terms): Total handbags -11.1% (-11.2% in Apr); leather handbags -20.6% (+0.9%); non-leather handbags -3.1% (-21.6%); jewellery -7.4% (-9.7%) / Retail: Apparel & footwear +3.8% (+3.6% in Apr); Gold, silver & jewellery -8.9% (-21.3%) / Wealth: Nationwide home prices -4.8% (-4.9% in Apr); SSE HSI avg +14.8% (+21.0%)

Do-Hyun Yoo
Research Associate
+44-20-754-19487

Adam Cochrane
Research Analyst
+44-20-754-17812

Andre Juillard
Research Analyst
+33-1-4495-6585

Figure 1: Summary of key datapoints

<table><tr><td>Category</td><td></td><td>Apr 25</td><td>May 25</td><td>Jun 25</td><td>Jul 25</td><td>Aug 25</td><td>Sep 25</td><td>Oct 25</td><td>Nov 25</td><td>Dec 25</td><td>Jan 26</td><td>Feb 26</td><td>Mar 26</td><td>Apr 26</td><td>May 26</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td colspan="21">1. Handbags</td></tr><tr><td rowspan="2">FRA + ITA total(Leather and non leather)</td><td>RMB</td><td>-12.6%</td><td>+1.5%</td><td>-7.9%</td><td>+5.5%</td><td>-4.9%</td><td>+0.9%</td><td>-3.4%</td><td>+11.6%</td><td>-1.8%</td><td>+13.1%</td><td>+19.7%</td><td>+1.2%</td><td>+5.6%</td><td>-10.4%</td><td>-6.5%</td><td>+0.6%</td><td>+1.9%</td><td>+10.9%</td><td>-2.7%</td></tr><tr><td>Unit</td><td>-11.8%</td><td>-1.7%</td><td>-13.8%</td><td>+3.1%</td><td>-8.7%</td><td>+1.2%</td><td>-3.8%</td><td>+0.8%</td><td>-11.9%</td><td>+2.3%</td><td>+10.0%</td><td>+3.4%</td><td>-11.2%</td><td>-11.1%</td><td>-9.2%</td><td>-1.5%</td><td>-5.5%</td><td>+5.1%</td><td>-11.2%</td></tr><tr><td rowspan="2">Leather</td><td>RMB</td><td>-10.1%</td><td>+0.6%</td><td>-9.1%</td><td>+7.3%</td><td>+1.2%</td><td>+0.9%</td><td>-1.4%</td><td>+15.3%</td><td>+10.8%</td><td>+15.2%</td><td>+16.1%</td><td>-1.3%</td><td>+20.3%</td><td>-18.6%</td><td>-6.3%</td><td>+3.3%</td><td>+8.3%</td><td>+9.3%</td><td>+0.2%</td></tr><tr><td>Unit</td><td>-13.5%</td><td>-2.6%</td><td>-15.8%</td><td>+3.9%</td><td>+4.8%</td><td>+5.9%</td><td>+3.7%</td><td>+3.6%</td><td>-0.7%</td><td>+1.5%</td><td>-0.4%</td><td>+6.4%</td><td>+0.9%</td><td>-20.6%</td><td>-10.8%</td><td>+4.8%</td><td>+2.1%</td><td>+2.5%</td><td>-9.8%</td></tr><tr><td rowspan="2">Non leather</td><td>RMB</td><td>-16.0%</td><td>+2.9%</td><td>-5.9%</td><td>+2.9%</td><td>-14.1%</td><td>+0.9%</td><td>-6.8%</td><td>+5.9%</td><td>-17.2%</td><td>+10.2%</td><td>+24.4%</td><td>+5.4%</td><td>-15.4%</td><td>+1.2%</td><td>-6.8%</td><td>-3.3%</td><td>-7.4%</td><td>+13.3%</td><td>-6.8%</td></tr><tr><td>Unit</td><td>-10.3%</td><td>-0.9%</td><td>-12.0%</td><td>+2.3%</td><td>-20.3%</td><td>-3.1%</td><td>-11.4%</td><td>-1.9%</td><td>-20.5%</td><td>+3.1%</td><td>+19.3%</td><td>+0.6%</td><td>-21.6%</td><td>-3.1%</td><td>-7.7%</td><td>-7.1%</td><td>-12.4%</td><td>+7.5%</td><td>-12.4%</td></tr><tr><td rowspan="2">FRA total(Leather and non leather)</td><td>RMB</td><td>+0.7%</td><td>+15.8%</td><td>+1.9%</td><td>+8.6%</td><td>+8.2%</td><td>+0.9%</td><td>+1.6%</td><td>+8.1%</td><td>+6.1%</td><td>+14.2%</td><td>+37.1%</td><td>-12.4%</td><td>+11.0%</td><td>-10.6%</td><td>+6.2%</td><td>+6.0%</td><td>+5.5%</td><td>+9.7%</td><td>-0.5%</td></tr><tr><td>Unit</td><td>+10.5%</td><td>+16.7%</td><td>+1.8%</td><td>+4.2%</td><td>+1.0%</td><td>+1.7%</td><td>-7.6%</td><td>-8.3%</td><td>-11.2%</td><td>+0.2%</td><td>+21.5%</td><td>-8.1%</td><td>-21.7%</td><td>-5.8%</td><td>+9.7%</td><td>+2.4%</td><td>-9.3%</td><td>+3.6%</td><td>-14.0%</td></tr><tr><td rowspan="2">Leather</td><td>RMB</td><td>-1.9%</td><td>+10.6%</td><td>-6.7%</td><td>+8.9%</td><td>+10.3%</td><td>+1.9%</td><td>+3.6%</td><td>+14.6%</td><td>+30.7%</td><td>+27.0%</td><td>+50.8%</td><td>-20.4%</td><td>+44.4%</td><td>-21.3%</td><td>+0.9%</td><td>+7.1%</td><td>+17.0%</td><td>+11.2%</td><td>+7.3%</td></tr><tr><td>Unit</td><td>-8.8%</td><td>+7.2%</td><td>-12.6%</td><td>+5.1%</td><td>+14.0%</td><td>+11.3%</td><td>+4.0%</td><td>+0.1%</td><td>+13.2%</td><td>+11.6%</td><td>+26.9%</td><td>-12.6%</td><td>+15.6%</td><td>-15.3%</td><td>-4.8%</td><td>+9.9%</td><td>+6.0%</td><td>+5.9%</td><td>-1.2%</td></tr><tr><td rowspan="2">Non leather</td><td>RMB</td><td>+3.5%</td><td>+24.5%</td><td>+16.4%</td><td>+8.3%</td><td>+4.8%</td><td>-0.3%</td><td>-1.5%</td><td>-1.0%</td><td>-19.7%</td><td>-0.5%</td><td>+24.3%</td><td>+1.2%</td><td>-24.5%</td><td>+4.9%</td><td>+13.8%</td><td>+4.4%</td><td>-9.2%</td><td>+7.8%</td><td>-10.1%</td></tr><tr><td>Unit</td><td>+21.9%</td><td>+23.6%</td><td>+12.4%</td><td>+3.7%</td><td>-7.6%</td><td>-3.6%</td><td>-15.3%</td><td>-13.6%</td><td>-23.7%</td><td>-5.8%</td><td>+18.9%</td><td>-4.9%</td><td>-38.1%</td><td>+0.1%</td><td>+19.5%</td><td>-2.1%</td><td>-18.3%</td><td>+2.2%</td><td>-20.7%</td></tr><tr><td rowspan="2">ITA total(Leather and non leather)</td><td>RMB</td><td>-22.5%</td><td>-10.4%</td><td>-16.2%</td><td>+2.9%</td><td>-15.7%</td><td>+0.9%</td><td>-7.4%</td><td>+15.3%</td><td>-9.8%</td><td>+11.9%</td><td>+5.4%</td><td>+20.3%</td><td>+0.3%</td><td>-10.2%</td><td>-16.6%</td><td>-4.1%</td><td>-1.6%</td><td>+12.2%</td><td>-5.0%</td></tr><tr><td>Unit</td><td>-24.5%</td><td>-12.3%</td><td>-23.2%</td><td>+2.3%</td><td>-14.2%</td><td>+0.8%</td><td>-1.3%</td><td>+8.3%</td><td>-12.4%</td><td>+3.9%</td><td>+2.2%</td><td>+14.2%</td><td>-2.5%</td><td>-15.2%</td><td>-20.2%</td><td>-4.0%</td><td>-2.7%</td><td>+6.3%</td><td>-9.0%</td></tr><tr><td rowspan="2">Leather</td><td>RMB</td><td>-15.4%</td><td>-8.4%</td><td>-11.3%</td><td>+6.1%</td><td>-7.0%</td><td>+0.1%</td><td>-5.1%</td><td>+16.1%</td><td>-6.7%</td><td>+4.6%</td><td>-5.5%</td><td>+25.5%</td><td>+2.2%</td><td>-15.6%</td><td>-11.9%</td><td>+0.0%</td><td>+0.7%</td><td>+7.5%</td><td>-6.3%</td></tr><tr><td>Unit</td><td>-15.4%</td><td>-7.4%</td><td>-17.4%</td><td>+3.3%</td><td>+0.7%</td><td>+3.4%</td><td>+3.5%</td><td>+5.5%</td><td>-8.1%</td><td>-3.3%</td><td>-11.1%</td><td>+19.9%</td><td>-5.4%</td><td>-23.5%</td><td>-13.6%</td><td>+2.5%</td><td>+0.0%</td><td>+0.8%</td><td>-14.0%</td></tr><tr><td rowspan="2">Non leather</td><td>RMB</td><td>-33.1%</td><td>-13.0%</td><td>-24.4%</td><td>-2.1%</td><td>-27.9%</td><td>+2.4%</td><td>-11.7%</td><td>+14.0%</td><td>-14.3%</td><td>+23.0%</td><td>+24.6%</td><td>+11.3%</td><td>-3.3%</td><td>-2.7%</td><td>-23.6%</td><td>-10.5%</td><td>-5.3%</td><td>+20.1%</td><td>-3.0%</td></tr><tr><td>Unit</td><td>-34.7%</td><td>-16.9%</td><td>-29.7%</td><td>+1.1%</td><td>-28.9%</td><td>-2.6%</td><td>-7.8%</td><td>+11.9%</td><td>-17.0%</td><td>+12.2%</td><td>+19.9%</td><td>+7.3%</td><td>+1.6%</td><td>-6.2%</td><td>-27.1%</td><td>-11.4%</td><td>-5.9%</td><td>+13.2%</td><td>-2.7%</td></tr><tr><td colspan="21">2. Jewellery</td></tr><tr><td rowspan="2">FRA + ITA + CHE(Gold, silver, platinum, diamond)</td><td>RMB</td><td>-23.6%</td><td>-1.3%</td><td>+14.9%</td><td>-8.4%</td><td>-29.7%</td><td>+14.5%</td><td>-7.7%</td><td>+12.2%</td><td>-10.7%</td><td>+45.0%</td><td>+5.1%</td><td>-5.7%</td><td>+35.8%</td><td>-6.1%</td><td>-1.7%</td><td>-10.1%</td><td>-3.7%</td><td>+12.5%</td><td>+12.2%</td></tr><tr><td>Grams</td><td>-10.0%</td><td>-15.1%</td><td>+2.4%</td><td>+9.9%</td><td>-0.7%</td><td>+28.8%</td><td>-0.6%</td><td>+4.5%</td><td>-21.0%</td><td>+76.2%</td><td>-36.9%</td><td>-29.3%</td><td>-9.7%</td><td>-7.4%</td><td>-7.3%</td><td>+11.8%</td><td>-6.9%</td><td>-6.0%</td><td>-8.6%</td></tr><tr><td colspan="21">3. Watches</td></tr><tr><td>Swiss export to China</td><td>CHF</td><td>-30.5%</td><td>-17.4%</td><td>+6.1%</td><td>-6.5%</td><td>-35.6%</td><td>+17.8%</td><td>+13.5%</td><td>-2.0%</td><td>-6.8%</td><td>+5.0%</td><td>-11.0%</td><td>+4.2%</td><td>+17.1%</td><td>-21.4%</td><td>-14.9%</td><td>-10.8%</td><td>+2.0%</td><td>-0.7%</td><td>-4.4%</td></tr><tr><td>Swiss export to Asia</td><td>Unit</td><td>-23.4%</td><td>-17.6%</td><td>-15.4%</td><td>-11.3%</td><td>-10.7%</td><td>+4.9%</td><td>+6.1%</td><td>-12.6%</td><td>+2.6%</td><td>+21.6%</td><td>+10.2%</td><td>+15.9%</td><td>-6.9%</td><td>+2.9%</td><td>-18.9%</td><td>-6.3%</td><td>-1.9%</td><td>+15.9%</td><td>-1.9%</td></tr><tr><td colspan="21">4. Macro</td></tr><tr><td>Consumer confidence</td><td>YoY</td><td>-0.5%</td><td>+1.9%</td><td>+2.0%</td><td>+3.5%</td><td>+4.0%</td><td>+4.6%</td><td>+2.9%</td><td>+4.8%</td><td>+3.6%</td><td>+3.5%</td><td>+3.6%</td><td>+2.9%</td><td>+1.4%</td><td></td><td>+1.1%</td><td>+4.0%</td><td>+3.7%</td><td>+3.3%</td><td>+1.4%</td></tr><tr><td>Nationwide avg. home price $^{1}$ </td><td>YoY</td><td>-5.7%</td><td>-5.2%</td><td>-4.9%</td><td>-4.6%</td><td>-4.2%</td><td>-4.0%</td><td>-4.0%</td><td>-4.2%</td><td>-4.6%</td><td>-4.8%</td><td>-4.9%</td><td>-5.0%</td><td>-4.9%</td><td>-4.8%</td><td>-5.2%</td><td>-4.3%</td><td>-4.3%</td><td>-4.9%</td><td>-4.8%</td></tr><tr><td>Tier 1 avg. home price $^{1}$ </td><td>YoY</td><td>-2.6%</td><td>-2.2%</td><td>-2.2%</td><td>-2.2%</td><td>-2.2%</td><td>-2.0%</td><td>-2.6%</td><td>-3.6%</td><td>-4.3%</td><td>-4.8%</td><td>-4.9%</td><td>-4.8%</td><td>-4.5%</td><td>-3.8%</td><td>-2.3%</td><td>-2.1%</td><td>-3.5%</td><td>-4.8%</td><td>-4.1%</td></tr><tr><td>Avg. SSE HIS</td><td>YoY</td><td>+15.1%</td><td>+18.6%</td><td>+26.0%</td><td>+32.2%</td><td>+37.6%</td><td>+21.7%</td><td>+24.0%</td><td>+25.0%</td><td>+23.1%</td><td>+31.0%</td><td>+20.7%</td><td>+11.9%</td><td>+21.0%</td><td>+14.8%</td><td>+19.9%</td><td>+30.5%</td><td>+24.0%</td><td>+21.2%</td><td>+17.9%</td></tr><tr><td>Retail sales</td><td>YoY</td><td>+4.1%</td><td>+5.4%</td><td>+3.8%</td><td>+2.7%</td><td>+2.4%</td><td>+2.1%</td><td>+2.0%</td><td>+0.3%</td><td>-0.1%</td><td></td><td>+2.8%</td><td>+1.6%</td><td>+0.2%</td><td>-0.6%</td><td>+4.4%</td><td>+2.4%</td><td>+0.7%</td><td>+2.4%</td><td>-0.2%</td></tr><tr><td>Retail apparel &amp; footwear</td><td>YoY</td><td>+4.5%</td><td>+5.4%</td><td>+3.6%</td><td>+1.1%</td><td>+1.6%</td><td>+2.9%</td><td>+7.0%</td><td>+2.8%</td><td>+0.0%</td><td></td><td>+7.9%</td><td>+3.6%</td><td>+2.0%</td><td>+1.1%</td><td>+4.5%</td><td>+1.9%</td><td>+3.0%</td><td>+6.5%</td><td>+1.5%</td></tr><tr><td>Retail gold, silver &amp; jewellery</td><td>YoY</td><td>+29.7%</td><td>+23.5%</td><td>+6.5%</td><td>+7.8%</td><td>+19.4%</td><td>+9.5%</td><td>+36.4%</td><td>+2.0%</td><td>+6.3%</td><td></td><td>+10.9%</td><td>+9.8%</td><td>-23.1%</td><td>-11.2%</td><td>+19.2%</td><td>+12.5%</td><td>+14.4%</td><td>+10.6%</td><td>-17.1%</td></tr></table>

Source : GACC, NBS, Bloomberg Finance LP, DB
Note: (1) Average of both primary and secondary prices

## May luxury import highlights

## Figure 2: Limited improvement in lux imports YoY

China monthly luxury import YoY  
![](images/d54f6a706b996c400d92008f1e4bd29f3cb81fd2f3eb7a5b8b7e4094219a0eee.jpg)  
Source: GACC, NBS, DB  
Note: Mechanical watch import data as per NBS, Marh FHS data to be released on the 21st of April  
Figure 3: 1Q YoY improvement momentum did not carry into 2Q

China quarterly luxury import (volume, YoY)  
![](images/ee74ea5b68503c29be3bafca47baa577a8fc381a7329b4035ed8a8654b7d6828.jpg)  
Source : GACC, NBS, DB
Note: (1) 2Q26 YoY is based on April-May 2026 vs. April-May 2025

Total handbag import unit YoY vs. LVMH Asia cFX

Total handbag import unit from ITA vs. Gucci APAC cFX
All handbag unit import (ITA, units, YoY) Gucci APAC cFX%

Figure 4: Macro set up is not optimal for luxury recovery

Explanation of data and historical trend analysis vs. sector cFX

We use 8-digit HS codes and trading partner codes to identify the specific products we track. This data is released with a lag (on the $20^{\text{th}}$ of each month) to the preliminary release (typically between the $7^{\text{th}}$ to $14^{\text{th}}$ of each month). Generally, we find that the sum of leather and non-leather handbags a better measure of the broader category demand. Please see below for longer-term trend analysis against relevant sector cFX.

## Handbags

![](images/03976b069b8fe629d928b5685435a6cc98fd282c51aa93f3f055146cc086a1c6.jpg)  
Source : GACC, NBS, DB  
Figure 5: May volume import -11.1% in May, -6.3% in 3MA terms

![](images/1d092937eb4c1f042029156eb9cb02735f0760d4b8676dd8276db4bbcf5e1b80.jpg)  
Source : GACC, Company data, DB
Note: This import figure includes both leather and non-leather handbags  
Figure 6: April-May 2026 volume import down -11.2% YoY vs. April-May 2025

![](images/d98981e26119d0971d1ac421009e123a1db7a70ebbd9359e76011fc1dde8e4e1.jpg)  
Source : GACC, Company data, DB
Note: This import figure includes both leather and non-leather handbags from France and Italy

Figure 7: Italian handbag imports are down sequentially - 9.0% in units in Q2 vs. +6.3% in Q1

![](images/dbb59b28a8feeb686848ff7bd8a0ffbe287f8c7d63e1955b0761f2efecacedcc.jpg)  
Source : GACC, Company data, DB
Note: This import figure includes both leather and non-leather handbags from Italy

Source : GACC, Company data, DB

Figure 8: French leather handbag imports are down -1.2% in units Q2 vs. +5.9% in Q1

Leather handbag unit import from FRA vs. RMS Asia cFX
—Leather handbag unit import from France (YoY) —Hermes Asia cFX%  
![](images/8838a3529bc0751e70851f20205e49ca53412b6d5e7fb5c1a96d4ddee5095957.jpg)  
Source : GACC, Company data, DB

## Jewellery

The headline data for 'Clothing and accessories' and 'Diamonds' imports available on the preliminary release does a moderately good job of tracking the relevant category cFX. However, we find that the jewellery data we track does a better job of tracking the quarterly volatility we see in the cFX data. We track imports of gold, platinum and diamond jewellery (in grams) from France, Italy and Switzerland.

Figure 9: Jewellery import is down -7% in May vs. -10% in April; it is down -15% in 3MA terms

Monthly jewellery import volume from FRA ITA CHE vs. relevant sector cFX

![](images/507a81cad2d1383fe20a5d05b5e84c72231073fc4831799b444ae47cd46d86fc.jpg)  
Source : GACC, Company data, DB

Quarterly jewellery import volume from FRA ITA CHE  
![](images/45a264cb452a6fd8ae4129437a5e1f5e0d00a2f813b55b3340fe07b3858ba97a.jpg)

## Watches

For watches, the official Swiss watch export data (FH) to Asia ex-Middle East has higher correlation with the relevant sector cFX. However, the publication schedule can vary depending on the month, making it difficult to compare against other categories for some months. On such occasions we substitute to total 'mechanical watch' import data, which tends to be more sensitive than the official Swiss data but in line with the FH data in terms of the direction of YoY change.

Figure 11: Swiss watch export to Asia +3% in May vs. -7% in April  
Monthly Swiss watch export to Asia (units) vs. relevant sector cFX  
![](images/cb0b78600deda432ccd3037c8725b10e9ad9616fa45bbec6672d7adbae892b94.jpg)  
Source : GACC, Company data, DB  
Figure 12: 2Q26 unit import to Asia down -1.9% YoY vs. 1Q26 +15.9%

Quarterly Swiss watch export to Asia (units)  
![](images/134e7817a28a3f64fb741d9bae425108a2e1abc46d29efd586c16668cc595824.jpg)  
Source : GACC, Company data, DB

## China consumer confidence and wealth growth

Discretionary spending environment remains suboptimal for luxury. Retail sales growth slowed down to -0.6% vs. +0.2% in April vs. an average of +3.3% during the months of Q1. Chinese consumer confidence continued to recover into April (latest available data) but at a slower pace. The measure was up +1.4% in April vs. +2.9% in March and +3.6% February. Household balance sheet remains under pressure with home prices down -4.8% vs. -3.9% in April and stock market returns slowing to +14.8% vs. +21.0% in April, all on YoY terms. The datapoints suggest the appetite for consumer discretionary spend remains fragile and requires more fiscal support.

Figure 13: Wealth improvement driven by stock market returns is slowing and may contribute to a slower recovery in luxury spend in China

## Wealth growth vs. sector APAC ex-Japan cFX

![](images/7c570ef369f969dea8b78ef984eb16d18ac5e5545efa2e019c8a4fbb4456e77d.jpg)  
Source : Company data, Bloomberg Finance LP, DB
Note: SSE - Shanghai Stock Exchange; HSI - Hang Seng Index; We exclude Moncler from this analysis as we believe the stock is benefiting from its own exposure to the structural shifts in the Chinese Winter luxury market

## Bridging consumer confidence vs. wealth growth

Figure 14: Consumer confidence declined in April vs. the months of March and February

China consumer confidence (1997=100)  
![](images/73cff59051fff51df0e5a64b6e70131b80019bf8538fd3408e6e2780c9b108db.jpg)  
Source : NBS, DB
Note: Latest consumer confidence data as of April  
Figure 16: SSE and HSI up +15% YoY in May vs. +21% in April; down by c.-2% MoM in May

![](images/6137638ba7e7c5f03450cc7e2ffab7deb0c79f11919ec411b919c535ad86394f.jpg)  
Source : NBS, Bloomberg Finance LP, DB
Note: SSE and HSI returns as of May; SSE - Shanghai Stock Exchange; HSI - Hang Seng Index; Consumer confidence data as of April

Figure 15: Home prices were down -4.8% in May vs. -4.9% in April

![](images/3f8c9a9e3f37ac0ce4d46d366442fdf9f5b0c50f14e7378dfd15b00de090dc57.jpg)  
Source : NBS, Bloomberg Finance LP, DB  
Note: Latest consumer confidence data as of April and home price dat

[中间内容因长度限制已省略]

ut whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
