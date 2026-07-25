你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# BECOMING AN ALL-WEATHER COMPANY

By Martin Reeves, Saumeet Nanda, Kevin Whitaker, and Edzard Wesselink

"The world is simply not prepared to deal with a disease—an especially virulent flu, for example—that infects large numbers of people very quickly. Of all the things that could kill 10 million people or more, by far the most likely is an epidemic. But I believe we can prevent such a catastrophe by building a global warning and response system for epidemics."

—Bill Gates, 2015

T HAS BEEN KNOWN for a long time that pandemics pose a major risk to global health and economies, yet the world was caught mostly flat-footed when COVID-19 started spreading. A few countries were well-prepared for the crisis, but many were not, and some had even scrapped or defunded preparation plans in recent years.

As we have seen time and again, if good times last long enough, it becomes hard to justify investments to ameliorate the bad times—efficiency becomes prized over resilience.

Many companies have effectively made a similar choice to value short-run efficiency over resilience, such as by spending down cash buffers on shareholder buybacks and removing operational slack, only to be hit hard during the pandemic. Many companies now express an intention to rebuild their business more resiliently, but it remains to be seen whether they will be able to respond effectively to the current crisis—and whether they will maintain resilient practices during good times in the future.

To help leaders do so, it is worth asking several questions: What is resilience and how does it work? How valuable is resilience in the long run? And how can companies go about building it?

Our quantitative study of nearly 1,800 companies over 25 years shows that resilience in unfavorable periods accounts for nearly 30% of long-term outperformance. We also find that some companies are consistently resilient over time and offer clues about how to build and sustain resilience.

How Resilience Creates Value At its core, resilience is a company's capacity to absorb stress, recover critical functionality, and thrive in altered circumstances.

This is needed when a sudden and unfavorable shift in the business environment causes an immediate shock to one or more critical business functions. For instance, when COVID-19 hit, some businesses saw a rapid fall in demand, while others experienced interruptions in supply chains or labor availability. Eventually, recovery ensues, but at very different rates across firms. In the shock-recovery trajectory, resilient companies enjoy better outcomes than their peers on one or more of three dimensions:

\- First, the immediate impact of an external shock on their performance can be lower than their peers.

\- Second, the speed of their recovery can be higher than peers.

\- Finally, the extent of their recovery can be higher than peers.

Measuring these three parameters offers a route to quantify the value of resilience across companies and to compare their strategies. (See Exhibit 1.)

To better understand the value and dynamics of resilience, we studied the performance of approximately 1,800 US companies from 1995 to 2020. $^{1}$ We assessed relative resilience by measuring the relative total shareholder return (TSR) of each company, compared with the average of its industry, during crisis quarters (quarters in which the industry TSR saw a peak decline of at least 15 percentage points [pp] from the start of the quarter).

## Quantifying the Impact of Resilience

Our study revealed several insights about the value of resilience:

Crisis periods have a disproportionate effect on long-run outperformance. While many companies tend not to focus on resilience, our analysis found it has an outsized effect: Although crises occurred in only 11% of the quarters in our study period, relative TSR during those times accounts for 30% of a company's long-run relative TSR. In other words, performance during crisis periods has almost three times the impact of performance during stable periods.

This impact stems from the fact that shareholder returns of companies in a given industry tend to move together during normal periods, but they diverge significantly during a crisis. In stable quarters, the average gap in TSR between the 25th and 75th percentile performers in an industry is 16 pp. However, this nearly doubles to 30 pp in crisis quarters.

EXHIBIT 1 | Resilient Companies Enjoy Better Outcomes on Three Fronts  
![](images/7e2adb119b055475b890cce6f0f2be26eaf579dd81d786eadc256000ba478e14.jpg)  
Source: BCG Henderson Institute analysis.

What happens during crisis quarters? The majority were linked to major economic recessions—the dot-com recession, the global financial crisis, and the coronavirus crisis. The rest were about evenly spread between nonrecession, market-wide crises (such as the one caused by the Russian financial crisis in 1998) and industry-specific crises (such as the 2015–2016 energy industry crisis caused by a drop in oil prices).

The deeper the crisis, the greater the value of resilience. As the depth of a crisis increases, so does the contribution of the corresponding quarter to long-run relative performance. (See Exhibit 2.)

Quarters with a TSR decline of more than 15% have a disproportionately higher impact on overall performance. Moreover, this impact dissipates in the first quarter after the crisis is over. (See Exhibit 3.)

The value of resilience differs by industry. The value of resilience tends to be higher in industries that face deeper or more frequent crises. While the value of resilience is greatest in technology and consumer durables sectors, which have tended to be more volatile, it is lowest in industries with more stable demand, such as food and beverages, household products, and health care. (See Exhibit 4.)

Outperformance is driven primarily by withstanding the immediate impact. Of the three phases of resilience, not all are equally important. Reducing the immediate impact of a shock accounts for 63% of relative TSR in crisis periods, while greater recovery speed accounts for 23%. The remaining 15% is explained by the extent of recovery; some companies benefit from the crisis and end up at a higher level than when they started.

Most paths to long-term success leverage resilience. We looked at the more than 500 companies that outperformed their industries from 1994 to 2020 (while being public for at least ten years in that time) and identified five archetypes of success. (See Exhibit 5.)

EXHIBIT 2 | Deeper Crises Have Greater Impact on Long-Term Performance

Relative impact of crisis performance on long-term performance

![](images/882ab46c3d8ec153b47b6ce7b65bb22414c0e7a1713b5081fadaa4e4d4ed2408.jpg)  
Sources: Capital IQ; BCG Henderson Institute analysis.  
Note: Maximum TSR drop from quarter opening is used to categorize depth of crisis.

Nearly two-thirds of the long-run outperformers did better than their peers in crisis periods. Moreover, nonresilient companies were only half as likely as resilient companies to achieve long-run outperformance. In order to succeed in the long run without resilience, companies needed to reach a very high bar during good times—outperforming their industry by 8 pp each year on average.

Achieving General Resilience
Each crisis is unique—for instance,
COVID-19 helped companies like Zoom and Clorox outperform, as the pandemic forced people to work from home and increased the focus on hygiene. However, companies can't always predict what kind of risks they will run into or when they will occur. This raises the question of whether general resilience—the capability to deal with any kind of crisis—is possible.

We found that there is indeed such a thing as general resilience in business: 15% of companies displayed general resilience by outperforming their industries in more than 80% of the crisis quarters they faced over the 25-year study period. (This is

![](images/8d6a3cec0f8277b6ec89de591f757abf8fde3e9ec1aa1598b35c77a0f898c795.jpg)  
Sources: Capital IQ; BCG Henderson Institute analysis.

![](images/774cb912dd5fa3b139a001db8ef463d81f8847d64fdbda0268ffef80f0b7f43f.jpg)  
Sources: Capital IQ; BCG Henderson Institute analysis.

Total industry outperformance (annualized)

Crisis-period outperformance (annualized)

significantly higher than the roughly 4% that would have done so if outperformance was completely uncorrelated across crises.)

An example of a generally resilient company is Berkshire Hathaway. From 1995 onwards it has outperformed the diversified financials industry by about 2 pp per year—but this outperformance was achieved entirely in crisis quarters (it outperformed in 15 of the 17 crisis quarters it faced). Across all noncrisis quarters, the company actually underperformed. (See Exhibit 6.)

Being generally resilient is extremely valuable over the long run, as such companies achieved an annual 5-pp TSR outperformance over their industries for the 25-year period that we observed (1995–2020). And, perhaps not surprisingly, five of the current Fortune 10 companies have been generally resilient.

EXHIBIT 5 | Two-Thirds of Long-Run Outperformers Do Well in Crises  
![](images/ee0db15e3cc12844bb71acf9fe573659faad48184e4ac19422cc790d467586e7.jpg)  
Sources: Capital IQ; BCG Henderson Institute analysis.

EXHIBIT 6 | Berkshire Hathaway Outperforms Industry via General Resilience  
![](images/1797075141b9a9e752bb0fd918c4fbafba13db37dab94141aca48c08e4a7097a.jpg)

Industry-normalized dividend-adjusted share price (indexed to 100)  
![](images/b217463f4acbbc481467b9db1d0cb9af4223ce9d9d432118c45657df93e39c4c.jpg)  
Sources: Capital IQ; BCG Henderson Institute analysis.  
Note: Good-period and crisis-period outperformances are over different time frames, so they are not directly additive or multiplicative.

## What Resilient Companies Do

Resilient companies create four types of advantage that help them achieve superior performance in crises:

\- Anticipation advantage: the ability to recognize threats and prepare for them in advance, which helps cushion the immediate impact and improve recovery speed.

\- Cushioning advantage: the ability to withstand the initial shock, which helps in cushioning the immediate impact.

\- Adaptation advantage: the ability to quickly identify the actions needed to restore operations and implement them swiftly, which helps improve recovery speed and achieve a greater extent of recovery.

\- Shaping advantage: the ability to shape the dynamics of the industry in the postshock environment, which helps in achieving a greater extent of recovery.

We have previously studied long-lasting biological systems to understand how they are structured for resilience, finding that these systems reflect six implicit design principles: prudence, redundancy, diversity, modularity, embeddedness, and adaptivity. These same design principles can also help companies anticipate a crisis, cushion its impact, adapt to it on different timescales, and shape the environment. (See Exhibit 7.)

Here we explore some specific measures that resilient companies deploy to operationalize the six principles.

## PRUDENCE

Prudence involves operating on the precautionary principle that if something can plausibly happen, it eventually will. Prudent companies therefore have an anticipation advantage, which helps them be better prepared to manage a crisis.

Resilient companies operationalize prudence by preparing for long-term shifts that can significantly disrupt an industry, developing plans or circumvention mechanisms in anticipation of a disruption, and looking for early warning signals to identify a crisis before it affects them.

Prepare for long-term shifts. Slow-moving trends often contribute to crises. For example, the continuous increase in international mobility was one of the factors responsible for COVID-19's global spread. Long-term shifts may also point to new opportunities; this crisis has accelerated trends like digitization of work and service delivery. Companies that navigate slow but significant shifts are likely to be advantaged in anticipating and preparing for a wide range of disruptions.

![](images/fb973fe19c53878b4ece98c2c2af2b2e78478498f1da21078d03e4b65783c7ca.jpg)  
Source: BCG Henderson Institute analysis.

The video conferencing technology company Zoom was one of the biggest outperformers (achieving TSR 110 pp better than its industry) in the coronavirus crisis. Zoom's founder and CEO Eric Yuan recognized the shift from audio-based to video-based communication as a major long-term trend and focused on improving video quality even at lower bandwidths. As a result of this video-first mentality, Zoom was in position to take advantage of the demand surge brought about by the pandemic.

Build contingency plans for disruptions. Whether resulting from long-term changes or sudden shifts, a wide range of disruptions can cause shocks. Hence, resilient companies identify potential causes and invest in building contingency plans or circumvention mechanisms for them. Just because there are plans on paper does not mean they will be executed successfully—war games and simulations can help ensure that they are pressure-tested and implementable during a crisis.

Build an early warning system and continuously scan the environment for emerging risks. Once a company has recognized potential threats and developed contingency plans, it can gain further advantage by scanning the environment for early warning signals. Though risks may seem unpredictable, the study of natural systems indicates that some disruptions are reliably preceded by certain indicators, such as the breaking down of historical correlations or a gradual slowing down of recovery time from smaller disruptions. $^{2}$

In business, early warning signals may be found by scanning the activity of fringe competitors or studying events in other regions. For example, Regeneron Pharmaceuticals CEO Leonard Schleifer said that the company's alarm bells rang in late January when Chinese authorities built new hospitals in Wuhan in less than a week. $^{3}$ Realizing this was not a normal incident, Regeneron turned its full attention to the new virus. As a result of this head start, it has been one of the frontrunners in COVID-19 research, contributing to 45-pp outperformance during the crisis.

Decoding early warning signals is particularly advantageous because many companies often do not recognize crises until it is too late. For instance, of the roughly 100 major US companies with earnings calls between January 24 and February 24—when the coronavirus outbreak was still largely confined to China—only ten discussed the possibility of a global pandemic affecting their business. Seven of them outperformed when the pandemic eventually spread (with an average overperformance of 9 pp), illustrating the value of anticipation.

## REDUNDANCY

Redundancy involves creating buffers to cushion against unexpected shocks, giving companies a cushioning advantage. There are two main ways in which highly resilient companies build in redundancy: operational buffering and financial buffering.

Operational Buffers. Redundancy in operational components like stocks, production capacity, and skilled workers for critical functions can help companies deal with demand fluctuations and supply disruptions. One company that benefited from such buffers is 3M, which has outperformed its industry in 78% of the crises faced in the past 25 years. After experiencing supply shortages during the SARS crisis, 3M deliberately built up excess “surge” capacity for respirator masks, enabling a rapid production ramp-up in the COVID-19 crisis. $^{4}$ As a result, 3M became one of the major PPE manufacturers in the US during the pandemic.

Financial Buffers. Generally resilient companies have a 16% lower debt/enterprise value (debt/EV) ratio and a 27% higher cash/operating costs ratio than the industry averages. $^{5}$ This financial buffering increases the capacity to sustain operations during a deeper or longer revenue shock. Moreover, having more cash or debt capacity also allows companies to purchase distressed assets inexpensively during a severe crisis. For example, Chevron has outperformed its industry in 80% of crisis quarters over time, in part because it maintains an advantageous debt position. In 2020, Chevron had a debt/EV ratio less than one-third of its peers' average, giving it more flexibility—in July, it completed the first major US energy acquisition of the crisis, agreeing to purchase Nobel Energy for \$5 billion.

## DIVERSITY

Diversity creates different types of options with which to react to a crisis. Companies with diverse businesses or operations are less likely to experience catastrophic failure; they enjoy a cushioning advantage. Companies can leverage diversity in their revenue sources (what they sell, where, how, and to whom) or in their operations (how they create and deliver products).

Revenue Source Diversity. Diversity of offerings, customers, geographies, or sales channels can protect against a sharp decline in demand during a crisis, because different segments are likely to respond to a shock differently. Companies that report revenues from more geographic or business segments than the industry median achieve an annualized crisis outperformance of 4 pp and 1 pp, respectively, in the long run.

Operational Diversity. Diversity of supply chain options, operational processes, and means of production can also provide alternatives during a crisis. For example, whereas most large hotel chains are concentrated in major tourist destinations, Airbnb offers a more diverse set of accommodation options thanks to the ease with which it can onboard new rental properties. When long-distance business and leisure travel stopped during the pandemic, the hotel industry suffered a prolonged shock—but Airbnb recovered much more quickly owing to its wider range of rental options. As people looked for safer vacations at smaller locations near major cities,

Airbnb's US bookings from the end of April to early June actually surpassed its 2019 figures.

## MODULARITY

Modularity refers to organizing a system in separate, loosely linked modules. This allows individual elements of a system to fail without the entire system collapsing. Modularity thus confers a cushioning advantage. Modularity can involve either operational or financial separation between businesses or components of businesses.

Operational Modularity. Companies with highly concentrated supply chains benefit from economies of scale, but they can suffer cascading effects from a small disruption. For example, the Fukushima earthquake

[中间内容因长度限制已省略]

ed for the unexpected. This naturally helps large organizations balance efficiency with resilience.

Think long-term. Calm seas will be disturbed by stormy weather at some point. Long-run performance is disproportionately determined by performance in crisis periods. Therefore, it is necessary to think ahead and prepare for unexpected and unfavorable events.

Think in systems and emphasize collaboration. A chain is only as strong as its weakest link. A company with a brittle supply chain or mistrustful regulators cannot be resilient. When diagnosing resilience, you must look beyond the boundaries of your organization.

Redefine “performance.” Businesses tend to be very goal-oriented. Leaders should aim for consistent long-term value creation—in changing and unfavorable times as well as in good times. Aspire to measure and manage forward-looking, long-term metrics like resilience, vitality, and adaptability.

Educate your managers. The term “resilience” is important and topical, but sadly it is also a source of confusion. It is defined in various contradictory ways, and few know how to achieve it. Furthermore, your managers have likely been weaned on efficiency thinking rather than resilience thinking. It is important to discuss what you mean by resilience, how it works, and how you plan to achieve it.

Go beyond the numbers. Resilience involves coping with and benefiting from the unexpected—it can’t be reduced to a closed-form equation. Modeling and quantifying knowable risks play a role. But restricting measures to the easily quantifiable is not enough to create a generally resilient company. You need to embrace weak signals, deal with contingencies, change plans in light of new information, and make judgments about the right level of “insurance” for your business.

Be optimistic. Resilience is not only about reacting to events with the aim of minimizing downside impact. It is also about outflanking your competition by learning faster from changing circumstances and shaping them to your advantage. “Opportunity” should figure in your thinking as much as “risk.”

THE CORONAVIRUS CRISIS has brought renewed attention to the need for resilience. Given that resilience is a critical

capability to deliver long-term outperformance, companies need to start the process of operationalizing resilience today to ensure that they are best prepared to navigate the future.

## NOTES

1. Analysis includes all companies with a market cap of \$3 billion or more at the beginning of 2020 or an equivalent inflation-adjusted market cap at the beginning of any five-year period since 1995.
2. Scheffer et al., “Early-warning signals for critical transitions,” Nature, September 2009; Scheffer et al., “Anticipating critical transitions,” Science, October 2012.

3. See “These Scientists Raced to Find a Covid-19 Drug. Then the Virus Found Them.”
4. See “How 3M Plans to Make More Than a Billion Masks by End of Year.”
5. Cash ratio defined as Cash-in-bank/(Operating costs ex DA).
6. See “Industries Mobilizing Against the Coronavirus.”
7. See “Airbnb launches Go Near, a new campaign to support domestic travel.”
8. See “Building a Resilient Supply Chain.”

## About the Authors

Martin Reeves is a managing director and senior partner in the San Francisco office of Boston Consulting Group and chairman of the BCG Henderson Institute. You may contact him by email at reeves.martin@bcg.com.

Saumeet Nanda is a consultant in the San Francisco office of Boston Consulting Group and an ambassador to the BCG Henderson Institute. You may contact him by email at nanda.saumeet@bcg.com.

Kevin Whitaker is head of strategic analytics at the BCG Henderson Institute. You may contact him by email at whitaker.kevin@bcg.com.

Edzard Wesselink is a principal in the firm's San Francisco office and an ambassador to the BCG Henderson Institute. You may contact him by email at wesselink.edzard@bcg.com.

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

## About BCG Henderson Institute

The BCG Henderson Institute is Boston Consulting Group's strategy think tank, dedicated to exploring and developing valuable new insights from business, technology, and science by embracing the powerful technology of ideas. The Institute engages leaders in provocative discussion and experimentation to expand the boundaries of business theory and practice and to translate innovative ideas from within and beyond business. For more ideas and inspiration from the Institute, please visit https://www.bcg.com/featured-insights/thought-leadership-ideas.aspx

## © Boston Consulting Group 2020. All rights reserved. 9/20

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and Twitter.
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
