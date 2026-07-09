你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# McKinsey Global Institute: 2025 in charts

Here are some of the McKinsey Global Institute's favorite data visualizations from 2025.

![](images/d351b6d85fe1e27404e79588449ed26a05a6aa15cacf35c6ff8fbb87f5124904.jpg)

In 2025, we are no longer on the cusp of a new era, but truly in it. This year, MGI's fact-based insights helped make sense of the latest business and economic signals. We found that just a few “Standout” firms can move the productivity needle for entire economies. We also put forward new reasons to accelerate national productivity now, so that countries can grow their way to balance-sheet health and drive prosperity. We explored ways in which the private sector could help lift more people above an “empowerment line” to meet essential needs and otherwise advance beyond ESG checklists. As trade policy shifts and other geopolitical developments packed some surprises, we updated our analysis of the geometry of global trade and looked to foreign direct investment (FDI) as a window to what may come next. We also introduced a “rearrangement ratio” to better understand potential knock-on effects of US–China trade tensions.

To understand the demographics and other defining hallmarks of our new era, we delved into the consequences of falling fertility and increasing longevity. We took stock of where the energy transition stands and tallied the costs and benefits of meeting climate adaptation challenges. We also explored labor market dynamics through the lens of work-experience trajectories and emerging skills partnerships with robots and agents in the age of AI. The following data visualizations, grouped into our five core research themes, encapsulate some of our key findings over the past year.

## Productivity & Prosperity

Creating and harnessing the world's assets

most productively

## Single firms can move the productivity

needle for entire economies—the “power of one.” In fact, fewer than 100 of the 8,300 large firms in our study sample account for 63 percent of productivity growth observed in the three countries analyzed. Dubbed “Standouts,” these companies generated the majority of productivity growth in powerful bursts rather than in a smooth trickle of gradual change, and through bold strategic moves, top-line growth, and portfolio shifts more than efficiency gains. This is a more concentrated, dynamic, and sporadic pattern than existing literature tends to highlight, with progress on productivity being defined by a few firms moving a mile rather than many firms moving an inch.

## A few 'Standout' firms shape the majority of productivity growth.

Share of national sample's productivity growth, %

![](images/47f8438be30a50e0c5cad32810ea70db75e1d30b80409d493242017e928bb40c.jpg)  
Source: The power of one: How standout firms grow national productivity, McKinsey Global Institute, May 2025

McKinsey & Company

Entering 2025, the world's wealth reached its highest level ever. Yet much of its growth came from asset price increases, funded by a proliferation of debt, rather than new saving and investment. Borrowing a page from corporate finance, we constructed a “global balance sheet” of the world's assets and liabilities as a new lens into the economy. Households gained \$400 trillion in wealth between 2000 and 2024, but only about \$100 trillion was cumulative net investment to build new wealth, while three-quarters of the gains were from assets' appreciation on paper and general inflation, not fully backed by economic growth.

## One-third of global household wealth growth since 2000 was on paper.

Decomposition of growth in global household net worth, 2000–24, \$ trillion

![](images/5b81768f9cb07d0d8eedff7815836ce6b8d289d991dc60a0f49a45de255fb66f.jpg)  
Source: Out of balance: What's next for growth, wealth, and debt?, McKinsey Global Institute, October 2025

McKinsey & Company

Number of mandatory ESG regulations globally

After a decade of expansion, ESG as a framework to measure a company's societal impact is undergoing a rethink. At the median, large companies today manage 100 environmental, social, and governance (ESG) KPIs. The rapid proliferation of ESG metrics and ongoing disagreements about prioritization—both within companies and in public discourse—have made knowing where business and societal goals do and don't align difficult. We analyzed a representative set of 18 environmental and societal issues to see where companies can apply their capabilities and innovate to make a real difference.

Attention to ESG has increased significantly in the past decade.

![](images/42e06a8154b37143a1fc5add34a1c7cab3c175a6ff86dde9cd091edfa74a641a.jpg)  
Source: Beyond ESG: From checklists to capabilities, McKinsey Global Institute, September 2025

McKinsey & Company

If Indonesia is to meet an ambition of becoming a high-income economy by 2045, productivity growth would need to be the primary driver of its 5.4 percent annual GDP growth. The contribution from population and labor force participation factors would be lower in the years ahead, likely accounting for about 0.5 percentage points of GDP growth—less than one-third of what it has been since 2000 at 1.8 percent. The balance would need to come from productivity growth, which would have to increase 1.6 times from the 3.1 percent CAGR that Indonesia achieved between 2000 and 2023 to 4.9 percent.

The year in which Indonesia reaches high-income status depends on how fast it can accelerate growth, especially productivity growth.

Year reaching high-income status based on benchmarks' annualized GDP growth rate, %

![](images/dc9a5de1bec79b610316be8b2d006fc18d4ff3d4287fe5310ed88273f551aa57.jpg)  
Implied real GDP growth rate decomposition, percentage points

![](images/003939158f1c80ca1d48d30f7813b1b0cab4448cff9f62552be220b08420e23c.jpg)  
Source: The enterprising archipelago: Propelling Indonesia's productivity, McKinsey Global Institute, April 2025

McKinsey & Company

## Global Connections

Exploring how flows of goods, people, and ideas shape economies

## Trade reconfiguration continues along

geopolitical lines. The most significant ongoing shift in trade patterns is a fall in the average geopolitical distance of trade: It declined by about 7 percent between 2017 and 2024, a period that witnessed ongoing trade tensions between the United States and China as well as Russia's invasion of Ukraine. Economies at each end of the geopolitical spectrum have been trading less with one another: China, Germany, and the United States have experienced sharp reductions in the geopolitical distance of trade. By contrast, the average geographic distance of trade has been climbing very slowly, but steadily by about 10 kilometers each year over the past decade. This appeared to continue through 2024. Global import concentration—that is, the breadth of trading relationships an economy relies on for each of the goods it imports—also remained stable.

## Trade is traveling shorter geopolitical distances.

## Evolution of goods trade indicators, 2000–24E

Geographic distance traveled by trade, thousand km, value-weighted average

![](images/cd1880589a884e66469b236a692da478566962a07dcd66e3ecd25700c76df3b1.jpg)  
Geopolitical distance traveled by trade, value-weighted average, 0–10 scale

McKinsey & Company

![](images/44ddaf51b88c9049657b1bcc6eb84ae3816047c7f544e6cd1efd30343a7457e4.jpg)  
Source: Geopolitics and the geometry of global trade: 2025 update, McKinsey Global Institute, January 2025  
Import concentration, Herfindahl-Hirschman Index

![](images/05dda1e78215a872dce032df13019a5a5585431738e2f520add7d37388e2d18c.jpg)

## Recent patterns of foreign direct investment (FDI) announcements signal a new

shake-up. FDI promises to shape advanced manufacturing—including semiconductors, electric vehicles, and batteries—alongside communications and software (mostly AI infrastructure), and the resources that power them. Since 2022, three-quarters of cross-border announcements have gone to these types of future-shaping industries as well as energy and mining projects—up from about half pre-2020. If successful, FDI projects announced since 2022 could more than quadruple current battery manufacturing capacity outside China, nearly double the global data center capacity that powers AI, and draw the United States into the circle of top leading-edge semiconductor-producing nations. These patterns show how trade corridors are shifting, country competitiveness is evolving, and new business ecosystems are emerging worldwide.

## FDI in semiconductors reconfigured sharply toward the United States.

Semiconductors: Top 25 corridors by announced greenfield FDI, \$ billion

![](images/33cada2742f31279ea3b80870cd4009607c4c93714645681535d63530f7fa93e.jpg)  
Source: The FDI shake-up: How foreign direct investment today may shape industry and trade tomorrow, McKinsey Global Institute, September 2025

McKinsey & Company

2022–25  
![](images/e361e145a4fd101ac3b785a8e82faf16248b70c32c94b95a0df531877dfca018.jpg)

# Ease of rearrangement varies across products. Cotton T-shirts? Fairly easy. Fireworks? Impossible.

Amid pressure on US–China trade, firms may look to rearrange sourcing to alternative suppliers. We introduced a “rearrangement ratio” to quantify how hard the change might be. Thirty-five percent of US imports from China have a ratio less than 0.1, signifying a global available export market ten times larger than current US imports from China. Think T-shirts or logic chips. For higher ratios, rearrangement becomes harder, and for the 5 percent of trade with a ratio greater than 1.0—for example, rare earth magnets—US imports from China exceed available global exports. Consumer goods are harder to rearrange than business inputs. Sixty-one percent of business input imports have a rearrangement ratio less than 0.1, versus 16 percent of consumer goods. Major products like laptops, smartphones, and toys are harder to rearrange.

Rearrangement ratio for products imported by the US from China, by sector, 2023

Circle size = Value of imports from China ◇ Sector's average ratio

![](images/32366490fa9c816af38ca721d687a0a193cacef95a1bf0df35127f828d93ec7c.jpg)  
Source: The great trade rearrangement, McKinsey Global Institute, June 2025

McKinsey & Company

Technology & Markets of the Future
Discussing the next big arenas of value and competition
McKinsey Global Institute: 2025 in charts 13

## People, agents, and robots could all play significant roles in the workforce of the future.

Work in the future will be a partnership between people, agents, and robots—all powered by AI. With the capabilities of existing technologies, AI-powered agents could perform tasks that occupy 44 percent of US work hours today, and robots 13 percent. At the same time, more than 70 percent of human skills can be applied in both automatable and non-automatable work. This means most human skills will remain relevant, but how and where they are used will change. For example, in a building-supply store, workers may spend less time locating materials, managing inventory, and handling routine logistics—and more time interacting with customers and interpreting AI-driven recommendations. Our research finds that by 2030, about \$2.9 trillion of economic value could be unlocked in the United States—if organizations prepare their people and redesign workflows, rather than individual tasks, around people, agents, and robots working together.

Distribution of work hours in the US, by technical automation potential, 2024, %

![](images/7e6c8c4b03cb036fe5258d8c698622329ad6311a674fb873c67c534c8bc41178.jpg)  
Source: Agents, robots, and us: Skill partnerships in the age of AI, McKinsey Global Institute, November 2025

McKinsey & Company

The industrial landscape has shifted dramatically over the past 20 years. Just look at the top ten most valuable companies in 2005 and 2025. Only one company appears on both lists. And the rest of the 2025 leaders are worth about ten times more than the 2005 leaders they replaced. What has caused this radical reshuffling? And why are today's winners winning on a whole new scale? The short answer points to the high-growth industries we call “arenas,” which are characterized by a particularly intense race to win, with outsize rewards but also a high risk of displacement.

## The past 20 years have seen a radical reshuffling in the ranking of the top ten companies.

Company ranking by market cap, \$ billion

\- Arenas of today ○ New entries

<table><tr><td colspan="3">Ranking, 2005</td><td colspan="3">Ranking, 2025</td></tr><tr><td>1</td><td>General Electric</td><td>370</td><td>1</td><td>Nvidia</td><td>5,027</td></tr><tr><td>2</td><td>ExxonMobil</td><td>350</td><td>2</td><td>Apple</td><td>3,976</td></tr><tr><td>3</td><td>Microsoft</td><td>278</td><td>3</td><td>Microsoft</td><td>3,843</td></tr><tr><td>4</td><td>Citi</td><td>246</td><td>4</td><td>Alphabet</td><td>3,426</td></tr><tr><td>5</td><td>BP</td><td>229</td><td>5</td><td>Amazon</td><td>2,715</td></tr><tr><td>6</td><td>Shell</td><td>211</td><td>6</td><td>Broadcom</td><td>1,712</td></tr><tr><td>7</td><td>Walmart</td><td>195</td><td>7</td><td>Aramco</td><td>1,650</td></tr><tr><td>8</td><td>Bank of America</td><td>185</td><td>8</td><td>Meta</td><td>1,607</td></tr><tr><td>9</td><td>Johnson &amp; Johnson</td><td>179</td><td>9</td><td>Tesla</td><td>1,558</td></tr><tr><td>10</td><td>HSBC</td><td>177</td><td>10</td><td>TSMC</td><td>1,267</td></tr><tr><td colspan="2">Total market cap, $ billion</td><td>2,420</td><td colspan="2"></td><td>26,780</td></tr></table>

Source: Capturing the next big arenas of competition in ten charts, McKinsey Global Institute, November 2025  
McKinsey & Company

# Resources of the World

Building, powering, and feeding the world sustainably

The physical transformation needed for the energy transition is advancing, but at about half the pace required to meet global commitments. On average, about 13.5 percent of low-emissions technologies needed to meet Paris-aligned 2050 targets across the seven domains we study had been deployed by the end of 2024. This is about three percentage points of progress in two years. During this time, deployment advanced in three of the seven parts of the energy system we analyzed—namely, low-emissions power, mobility (electrifying transportation), and raw materials (critical mineral supplies). Progress is mostly stuck in carbon capture, hydrogen fuels, and in heavy industry.

## The energy transition is advancing at half the required pace.

Deployment of low-emissions technologies, 2022 and 2024 actual and 2024 at cruising speed, % of total deployment to meet 2050 targets

![](images/11a22df9f830ec2febde52a7e97acf79411d727b7426f5e21c33db6b46cfb353.jpg)  
Source: The hard stuff 2025: Taking stock of progress on the physical challenges of the energy transition, McKinsey Global Institute, November 2025

McKinsey & Company

Advancing adaptation is a good buy, but achieving protection at 2°C would require more than six times today's spending—and that spending is not guaranteed. The world currently spends \$190 billion annually to defend its denizens against extreme weather at the standards established in developed economies. As the world warms, on current emissions trajectories reaching 2°C above preindustrial levels by about 2050, exposure to drought and heat will increase the most. Maintaining today's level of protection at 2°C would require 2.5 times current spending, while achieving developed-economy standards would cost about \$1.2 trillion annually, most of which would go to air conditioning and irrigation. Many such proven measures to adapt exist, and at 2°C, their benefits outweigh their costs by seven-to-one.

## Air conditioning and irrigation systems account for more than half of the adaptation spending to protect at $2^{\circ}$ C to developed-economy standards.

Distribution of annual average operating and amortized capital costs to adapt to 2°C hazards to developed-economy standards, 2020–50, %

![](images/a05b9a396f0e2d858b8ca813eca4218e4c79d01ed8427f69efc5bb040e108495.jpg)  
Source: Advancing adaptation: Mapping costs from cooling to coastal defenses, McKinsey Global Institute, December 2025.

McKinsey & Company

Human Potential
Maximizing and achieving the potential of human talent
McKinsey Global Institute: 2025 in charts 19

Population aged 15–64 years, % of total population

## Working-age populations peak in three waves.

Falling fertility rates are propelling major economies toward population collapse in this century. Maintaining past economic progress, let alone increasing it, will require measures to address the impact of demographic headwinds. The working age population has already peaked in developed economies and Greater China, the first wave. Emerging economies in the second wave have a bit more time, but they need to “get rich” before they “get old”. The working age population share is beginning to peak in Emerging Asia, India, Latin America and the Caribbean, and the Middle East and North Africa. Sub-Saharan Africa, where the average fertility rate is still 4.4 (even if also falling), is alone in the third wave, which will peak well into the second half of the century. While many countries are trying to increase their birth rates, none has been very successful so far—and a baby born today won’t join the workforce for roughly two decades. Three levers are available to keep economic growth on course and public finances sustainable: more employment, faster productivity growth, and effective migration. The magnitude of improvement required for each individual lever is large, so they will need to be deployed in combination. Each country can opt for a different “menu” of combinations, depending on its characteristics, opportunities, and challenges.

![](images/949bfd50565f1849255c972cdc9fa4ab958d300a9b40767a1efc161aee0da919.jpg)  
McKinsey & Company  
Source: Dependency and depopulation? Confronting the consequences of a new demographic reality, McKinsey Global Institute, January 2025

Diverging work experience patterns drive a “work-experience pay gap” that makes up nearly 80 percent of the total gender pay gap, equal to 27 cents on the dollar among US professional workers. Over a 30-year career, the gender pay gap averages out to approximately half a million dollars in lost earnings per woman. To arrive at this conclusion, we analyzed how men and women go about accumulating work experience—switching jobs, returning after breaks, climbing the corporate ladder, making lateral moves, downshifting, and more—and how they realize the value of human capital differently (in terms of pay). While individual stories vary widely, the big picture indicates that diverging occupational paths and shortfalls in accumulated work experience drove most of the pay gap.

About 80 percent of the gender pay gap can be attributed to differences in work experience—both career pathways and time spent out of work.

Decomposition of average pay gap between men and women at year 10 of a career, percentage points

![](images/8a03c5cf0845ae67ea9d86f0d15d0b6a961a59b50c872a5ef1df79fe2179f290.jpg)  
Source: Tough trade-offs: How time and career choices shape the gender pay gap, McKinsey Global Institute, February 2025

McKinsey & Company

The “empowerment line” measures progress toward a world where everyone’s essential needs are met. This metric is based on an estimate of the cost of a basket of essential goods and services—including housing, healthcare, food, and transportation—for a frugal yet decent quality of life. Even in economies at similar GDP levels, the share of people living below their respective empowerment lines varies widely, because costs and income opportunities vary. Empowerment may be out of reach for context-specific reasons. Those reasons include, for example, the affordability of housing or food, or the availability of stable jobs with sufficient wages. The private sector is pivotal to achieving empowerment and has a wide array of options.

## At the country level, the elements contributing to the degree of variation in empowerment share look very different.

Importance of 9 income and affordability elements influencing economic empowerment

![](images/a8c4f9cabef66856b8b3a294ab30ab33ca1c1e7e6f8cd92f7a59b284ba39efc3.jpg)  
Source: Economic empowerment made-to-measure: How companies can benefit more people, McKinsey Global Institute, January 2025

McKinsey & Company

![](images/90d6af5d1e72aa39ad3f3b1816dd138ecf6e39faac4af02cdf7ec4533e7d3033.jpg)

Can you imagine even the poorest country in the world achieving the prosperity and quality of life of today's Switzerland—by 2100? MGI's new book, A Century of Plenty: A Story of Progress for Generations to Come, stress tests this vision. Its conclusion: we can have enough energy, food, metals, and minerals. We can innovate quickly enough. And we can do this while protecting our planet. By 2100, everyone could have the life of the top few percent of humanity today. But that requires a new, optimistic narrative, along with a belief in growth and the determination to build a better future for generations to come.

The book will be available on January 13, 2026, on Amazon.

McKinsey Global Institute

December 2025

Copyright © McKinsey & Company

Designed by the McKinsey Global Institute

mckinsey.com/mgi

X @McKinsey\_MGI

@McKinseyGlobalInstitute

in @McKinseyGlobalInstitute

Subscribe to MGI's LinkedIn newsletter,

Forward Thinking: mck.co/forwardthinking
"""
