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
BCG

Executive Perspectives

## BCG's Guide to Cost and Growth

Strategic Insights for Navigating Economic Uncertainty

January 2025

![](images/c504545034afa56aa50f35b59ebabe637ac8b8ce2740cf9736756b3ea98c11db.jpg)

## Introduction

The year ahead brings both opportunities and challenges as CEOs and executive leaders worldwide grapple with economic uncertainty and the need for strategic reinvestment. In our latest survey of over 570 executives across regions and industries (conducted at the close of 2024), we explored the primary concerns and strategies shaping business priorities for 2025.

Our research reveals that cost management remains a top priority amid fluctuating interest rates and global trade tensions. This edition synthesizes insights from CEOs and leading experts at BCG, providing a roadmap for sustainable margins and cost efficiency while positioning businesses for long-term growth.

This edition also delves into the factors critical to maintaining financial discipline in companies and explores how leaders can reinvest strategically to fuel competitive advantage in 2025.

![](images/e15ba231b9a4b1f229fae195926501c4bc1578baa815a0d3aa4e2f4c33ad7e52.jpg)

In this BCG Executive Perspectives edition, we share executives' views on the 2025 macroeconomic outlook, with a focus on cost management and growth

## Executive summary | In a complex and uncertain economic environment, cost management remains the top priority for executives across industries

<table><tr><td>Navigating the economic landscape of 2025</td><td>The global market outlook for 2025 remains relatively steady, with declining optimism in 2025 relative to 2024 following the US election outcome40% of executives feel unprepared for market shocks in 2025, despite years of navigating disruptions (e.g., COVID, supply chain, ChatGPT)North American and European executives are increasingly concerned about margins and profitability as rising interest rates, inflation, and potential tariff and regulatory changes intensify pressureAsia-Pacific1 executives are concerned about impacts on exports that could slow economic growth as geopolitical tensions in the region could further erode investor confidence and disrupt global supply chainsIn the wake of the recent US election,85% of executives are already addressing tariffs and regulatory changes to mitigate potential disruptions</td></tr><tr><td>Managing cost structures in 2025</td><td>Amid a complex economic landscape,cost management remains executives’ top priorityHeading into 2025, executives are prioritizing cost efficiency in theircore operations including supply chain optimization and product portfolio simplificationto remain competitiveExecutives in the sample report thatonly 48% of cost-saving targets are achievedand that their companies struggle to maintain efficiencies Companies that announce but fail to achieve targets average9pp TSR underperformance compared with successful peersThe greatest barrier to lasting structural cost change is &quot;cultural resistance&quot; to cost-saving measures, but firms withactive focus to align culture on cost and efficiencies and agile management achieve up11% greater lasting cost reduction</td></tr><tr><td>Unlocking sustainable growth</td><td>Laying the foundations for sustainablecost management is vital, as67% of executives plan reinvest savings into growth and innovationExecutives view GenAI as a pillar for efficiency, with86% planning to invest in AI and advanced analytics in 2025Executives see GenAI and advanced analytics as anopportunity to cut costs in areas like customer serviceBCG’s holistic approach combines deep expertise and proprietary capabilities todeliver cost management programs that drive lasting savings, fuel growth, and tackle structural cost challenges</td></tr></table>

![](images/c044e207209db2190279bd6ef3e0797ccd81ee4e2f171c5560aaadee90e9ee94.jpg)

## BCG Executive Perspectives

AGENDA

![](images/ad061ce396a3c7ba7ee28169a145ff744b9ea8dcf6971b80c833a42e4edf92ce.jpg)

Navigating the economic landscape of 2025
Managing cost structures in 2025
Unlocking sustainable growth

## Executives show caution regarding 2025 outlook amid economic and geopolitical uncertainty

How do executives view the stability of the markets they are operating in?

![](images/8d866f31619c3e51fdfdd9989613043a7b0e25b8b5bcc0ed2d7e6851b0171034.jpg)

\- The US economy has remained strong and stable since COVID, despite threats of recession, with $\pm 2.2\%$ GDP growth $^{2}$ projected for 2025

• 42% of executives expect their markets to outperform the forecasted GDP growth

\- Nevertheless, concerns over global economic and geopolitical stability have arisen following the recent US election outcome

![](images/06ff06be6d5f1e15c8352eeb3bcf95eecee5536a194f454a2c48607745eec93a.jpg)

\- Despite economic challenges, optimism remains steady supported by low unemployment and a projected $\pm 1.5\%$ GDP growth $^{1}$ in 2025

• 47% of executives expect their markets to outperform the forecasted GDP growth

\- Pessimism likely reflects an uneven recovery since COVID, geopolitical tensions, armed conflicts, and energy concerns

![](images/1cde782ceb5ffdd7df9101dd10d2ae700752cda57c70872ccea8f771fb2b6882.jpg)

\- Optimism has dropped in Asia $^{2}$ , despite the continuously strong GDP growth forecast of ±4.5% $^{3}$ for 2025

\- Yet 47% of executives expect their markets to outperform the forecasted GDP growth

\- Executives’ sentiment toward market stability has shifted further to neutrality following the recent US election outcome, as they are seeking early indications of potential tariffs and trade policy changes

## 40% of executives feel unprepared for market shocks heading into 2025

## How prepared are executives for market shocks heading into 2025?

![](images/7f03466ce4a59c02378fe4b04d6645ba34aa1dc26b20d7f1d72d9bc3465ba93f.jpg)

40% of executives continue to feel unprepared for potential future market shocks, despite navigating years of disruptions like COVID, supply chain crises, the ChatGPT launch, and other economic upheavals

## Learn more about current challenges and risks:

![](images/411859cac16feabd67d009bea40cc8bd25c9d314402275610d29672dec0f8d1a.jpg)

## Geopolitical tensions and supply chain

Ongoing conflicts impact trade and market stability; companies should use scenario planning and diversify supply chains to enhance resilience

Read more about geopolitical risk management in strategic planning

![](images/3d635ce49781a937d69eff44172d5e5e87d58a5f3900aeaf0f9dd37546573f33.jpg)

## Rapid technological changes

Companies struggle to keep up with innovation yet need to adapt quickly by implementing new tech and upskilling employees

## Read more about the value in AI

## North American and European executives are increasingly concerned about margin pressure

What top macroeconomic factors do executives expect to affect their company performance in 2025?

North America

## Europe

## Asia-Pacific $^{1}$

![](images/d70e844debb7c0188f72d1564c327c5a33fc04a238e98b079cbe70d003f3b48a.jpg)  
Over 60% of executives expressed increased concerns about tariffs, following the recent US election outcome

North American and European executives are increasingly concerned about margins and profitability as high interest rates, inflation, potential changes in regulations, and tariffs intensify pressures

Protectionist measures introduced by the recently elected US government could reshape global trade dynamics, reducing trade flows and disrupting supply chain stability—even before considering potential retaliatory actions

These measures, aimed at boosting domestic US manufacturing, may accelerate local investments while discouraging offshoring. For Europe, this could exacerbate existing competitiveness challenges

## Asia-Pacific executives are concerned about impacts on exports that could slow economic growth

What top macroeconomic factors do executives expect to affect their company performance in 2025?

North America

Europe

Asia-Pacific $^{1}$

![](images/f0ce4c96e3741d7287640b90987781701c14e541ac619de4e564e5ddb9b16b91.jpg)  
Over 60% of Asia-Pacific (excl. China) executives expressed increased concerns about economic uncertainty and tariffs, following the US election outcome

Asia-Pacific executives are navigating a complex economic environment marked by persistent inflation, varied monetary policy responses, and global trade uncertainties—all of which contribute to heightened concerns over inflation and interest rates

They are increasingly concerned about economic uncertainty stemming from the recent US election outcome, with recession risks and US-China trade tensions emerging as top underlying concerns

Potential geopolitical tensions in the region could further erode investor confidence and disrupt global supply chains, potentially reducing revenues and slowing economic growth in export-dependent Asia-Pacific economies

Note: Asia-Pacific countries excluding China  
Source: BCG global executive survey on strategic priorities (N=570) Q4 2024; BCG analysis  
1. Asia-Pacific includes India, Australia, Japan, and South Korea

1. No immediate actions taken in response to the US election outcome
Source: BCG global executive survey on strategic priorities (N=570) Q4 2024; BCG analysis

## Following the US election, 85% of executives are acting on tariffs and regulatory changes

## What actions are executives taking in response to the US election outcome?

![](images/64a45a100767fa98d86a80cb479932b90aa42a4a1fa0ffd6e2db3569ab8a9a21.jpg)

## 54% are actively monitoring

What top indicators are executives tracking, given the recent US election outcome?

1. Tariffs changes

2. Regulatory changes

3. Geopolitical conflicts

4. Supply chain disruption

## 31% have launched contingency plans

What top initiatives have executives launched, given the recent US election outcome?

1. Planning response to tariffs changes

2. Assessing impact of regulatory changes

3. Redesigning supply chain

4. Reviewing geopolitical risks and business impacts

Executives across regions express concern for supply chain disruption, driven by the potential reinstatement or escalation of tariffs and trade barriers, which could significantly impact companies' performances in 2025

Corporate leaders globally are closely monitoring or assessing developments in geopolitical conflicts in Eastern Europe and the Middle East, along with US-China trade tensions, as potential sanctions and the economic isolation of certain countries could have significant impacts on business operations such as energy prices, supply chain disruption

Read more about managing geopolitical risk in the context of supply chains

![](images/652de93b0323b3262cbed753b0fbf7c1d8747b4c32dcf9b37d3ea82dc91a0799.jpg)

![](images/8881daf119ba794f74d80d5ed53c456c34d48e27257b962aa30e37a6feee76a7.jpg)

![](images/9f77cbd7fd8c282bfd5ae1ffc5910dcf8ca257e97b4e0694eab7351036d502cc.jpg)

## BCG Executive Perspectives

AGENDA

![](images/69db3a114e7fb1a0253cbe79ace54e8d8f4711eb7627d1e35c78fdd953e32158.jpg)

Navigating the economic landscape of 2025
Managing cost structures in 2025
Unlocking sustainable growth

![](images/a66c027a06b08186a4e6c4b5876a8db6a3b73e0ef6089de39a47b196dd82c967.jpg)

## Cost management remains the top priority for executives across regions and industries

## What are the top three strategic priorities for executives heading into 2025?

![](images/71f7f8909552ea64168ef10b60f5c84290206ae8fe5dc095bcb4b095d10945c6.jpg)

## #1

![](images/1171688bac4aabf019417e660aa2a584480d32c8a3cc25591320e492fa30b08e.jpg)

## Cost management

33% of corporate leaders are prioritizing cost reduction as most critical, +8pp compared with 2024

## #2

## Growth/Expansion

Growth remains a focus, with 70% of executives reporting that they have sufficient mid-term visibility to make informed investment decisions

![](images/068aaa8794d130ee7ab1d964c1d176ab8a9082481aa3c22294652fff4241d2a3.jpg)

## #3

## Revenue management

Executives are looking into pricing strategies to manage potential rising supply chain costs while addressing end-consumer pressures

In a challenging economic landscape, companies that prioritize productivity growth through disciplined cost management will outperform those that choose to absorb margin pressures or pass costs on to consumers

## When it comes to cost efficiency, executives prioritize supply chain optimization and product portfolio simplification

What key cost drivers are executives prioritizing for optimization in 2025?

## Top ranking across industries

#1

![](images/21892fd69372fa0e27ebe38f100ccf6bb627a11f023247f4965fc623628a3a05.jpg)

Supply chain optimization #2

![](images/f60a34100107264e4f877658cba66a634033e7e9a59d23c6ebf27e6cedfb141e.jpg)

Product
portfolio
simplification #3

![](images/4f00bab3ee81106fec2b8881c13d7f99be2e6fde6af2e28874ca8b81d7560d8c.jpg)

Operating
model and
workforce
productivity #4

![](images/7bd4ac94f24221d245beb4fc48122cb37bfa6c61d61c32e15396a41d10abe12b.jpg)

Customer
service
operations #5

![](images/180bff431b9e779b80e3118b824d7d3f7c08b3407ceed1f51780344b780429ce.jpg)

Sales
and
marketing

## Industries where each cost action is top-of-mind

Consumer

Industrials

Insurance

Technology

Finance

Industrials

Health care

Insurance

Finance

Technology

Consumer

While all companies prioritize cost management, there is no one-size-fits-all approach—it must be tailored to focus on areas that strengthen the industry’s competitive advantage

To remain competitive,
executives are prioritizing core
operations, optimizing supply
chains, and streamlining
product portfolios for cost
efficiency

Read more about our latest thinking on cost excellence

## A cost-efficient and resilient supply chain reinforces competitive advantage

![](images/555f3df7144e2082cf58f62635abf42b3ccab758625cd0ad3993a77dea8273e3.jpg)

## Supply chain optimization

Supply chains remain under
relentless pressure from multiple
directions:

\- Geopolitical crisis

• Uncertain macroeconomic outlook

• Climate change and pressure of net zero commitments

• Technology disruptions

• Changing consumer expectations

## Cost-efficient and resilient supply chains need to be managed across the value chain...

## Dimensions

![](images/f47872eb9b123af0df942adc14d0090257a8e36c75983fa6b861ac035e0d542f.jpg)

Product

development

![](images/8a7e0e9050aa6b8d765172832aede0ccf0d4d64f5b3838d323d85918f9558568.jpg)

Planning

![](images/a117124befbf0fc2fffb5e707e3b7ecbe7030772c0383233da8a9bb3802cb2a2.jpg)

## Procurement

![](images/9a5842976bb3a474376f329b07b7aacf4ee231ea37dcaeb8e55477c403fb4c3d.jpg)

## Manufacturing

![](images/2198102c740467d0de0a1238c6db0f303538093077fac6efe5c187ea6138e359.jpg)

Logistics and transportation

![](images/bb830338359fa232009d67de49683156cc21abd871cc3d2b83cc0bc4ec92be75.jpg)

## Warehousing

## Optimization levers

\- Modularize product design

\- Design solution-oriented for fast-cycled processes and reduced bottlenecks

• Leverage digital scenario planning

\- Engage AI in forecasting

\- Align processes between supply chain and manufacturing

\- Deploy strategic global sourcing to identify best suppliers

\- Ensure best prices through competitive tenders, benchmarking, should-cost models

• Enhance supplier relationship and develop joint innovation programs

• Conduct material flow and utilization analysis

\- Optimize plant layout and equipment

• Reassess service level and maintenance needs

\- Optimize logistics network

• Consolidate transport routes and explore shared services

\- Reduce "rush shipments"

• Consolidate warehousing

• Explore digitization and automation

\- Renegotiate capacity and rates

Read more about future-proof end-to-end supply chain transformations

## A design-to-value optimization approach ensures a lean and competitive product portfolio

![](images/23241bec05c83d09138a30ee5ed13c3517deb70c78f2f6e0d88527f3f48583a2.jpg)

## Product portfolio optimization

In fast-moving markets, growing product complexity and shifting priorities drive up structural costs and profitability pressures

• Product complexity and proliferation (e.g., too many SKUs)

\- Raw material and component costs

• Manufacturing overhead and supply chain complexity

• Inventory holding costs

• Product development and R&D costs

• Life cycle management costs

• Marketing and sales expenses

• Regulatory and compliance costs

## Focusing resources on high-value products while improving operation efficiency and reducing supply chain complexity

## Optimization levers

## #1

Eliminating the “tail” through consolidation to eliminate low-volume configurations while retaining volume and revenue

#2 A design-to-value approach with a customer-centric perspective helps to rebalance value and cost of the product portfolio

## Baseline setting

• Understanding customer voice

• Detailed cost breakdown

\- Gap analysis

## Idea generation

• Cross-functional workshops to rebalance value and cost

\- Benchmarking

## Implementation

• Ensuring customer and supplier alignment on design changes

• Monitoring progress

![](images/2d75f5c3011b5d190db785fdf2568f46cf9d1522c74723858259f4da22fc53b7.jpg)

## Companies struggle to achieve their cost targets

![](images/d09a11979a8df0e27de0fbd71f5dde4e50287df29de00755570eca569adccd2a.jpg)

![](images/d8c215ca99dafeaec733345cc4ed85d45ddf2d5b8ea1b4f5b5724e8c43e8e814.jpg)

Average proportion of
cost-saving target
achieved by companies

![](images/895089f9c7717cc3e392e28e366167d6fc0225a78068bf065a7bb67fd42b3b29.jpg)  
Proportion of
companies failed to
achieve long-lasting
structural cost cutting

Companies failing to meet cost targets underperformed on total shareholder return by an average of 9pp compared with the average TSR of peers that met their targets

## What were the biggest challenges to the success of past cost reduction efforts?

![](images/f0561eb6758cb657be68f23a7a99a54c71212bf87a1c488cffad930c61c09442.jpg)  
Employee and
organizational
culture

![](images/f25b56a6454d395d7aee499d7fb98112d89ed42139ab53f408c650a10a601616.jpg)

![](images/b4ad969f463adebefc0a8d08e7be3be71827d58b289dd887be1009804316acbb.jpg)  
Change in mgmt.
(org. structure
and process)  
Skills/Expertise

![](images/3b29a934b4564126e292d2e16853b53e946d76d700acdaae1a9ae7f21bb28f59.jpg)  
Technical
infrastructure
and capabilities

![](images/393c577b29c61b402835a3ee3ddf8f04ab3942e545fd05b68677754396b18182.jpg)

Resistance to change can hinder implementation of new cost-saving measures and efficiency improvements; however, firms with aligned culture and agile management see up to 11% higher efficiency in cost reduction initiatives

## A cost-conscious organ

[中间内容因长度限制已省略]

nt processes

## BCG has deep expertise in cost management Partnering with your organization to craft a cost program that creates enduring impact

We leverage our unique strengths and approach to transform your organization, delivering lasting structural cost savings that fuel growth

![](images/e11990a1091922ef4df8ce383e1a2625e7b151c51cf72294e335a0b2fb3deebf.jpg)

![](images/ad4492df64ae017121553dee6671f681bdfdf03b2462f41e7ccabec60b9a06b8.jpg)

![](images/d91eadae6e111577b0bbfd604cd09b6e31b0ce7371b45c55a76ee17db81b7f79.jpg)

![](images/1b6554c3f675e7f5823c5370746afbe80fedb9977fd4ebe99955fc1bbca1a465.jpg)

<table><tr><td>Strategic cost optimization with growth focus</td><td>We design lean cost structures that drive savings without limiting growth, aligning cost management with your strategic objectives</td></tr><tr><td>Empowered culture and continuous improvement</td><td>We foster a culture of continuous improvement, empowering employees to take accountability, ensuring sustainable progress even after our engagement</td></tr><tr><td>Customized expertise and reliable execution</td><td>We deliver tailored cost solutions for competitive advantage leveraging our deep industry expertise, ensuring end-to-end focus and reliable outcomes</td></tr><tr><td>Advanced digital &amp; AI capabilities and data-driven insights</td><td>We embed cutting-edge digital and AI tools in operations, enabling data-driven decisions for enhanced operations efficiency and productivity</td></tr><tr><td>Collaborative partnership and lasting impact</td><td>We work hand-in-hand with your leaders, ensuring projects are co-created for lasting results that stick, with a “done with” partnership mentality</td></tr></table>

![](images/0160c1bcb0179ca301e89c1c3fe6510409fe0808209df08f346a62546c39b474.jpg)

## BCG cost experts

![](images/e9c962a193b71e69a73edbd9a00f7ec24a5fdf63c95012725515b4b99482b2ba.jpg)

## Paul Goydan

Managing Director & Senior Partner Houston

![](images/8154e26b10e90a65c7037345bbd85dd2121b7b55e3694fe6cfb291a5e5415469.jpg)

![](images/4acca7459ef27780bad07affa51d79d37b5e1cfab1dd75a1b28a97859aa64dd4.jpg)

## Namit Puri

Managing Director & Senior Partner

New Delhi

![](images/4c96d508102bb00dd2001f24dd21ba39e2a96acc6fa8ab1fb6bf106275386155.jpg)

![](images/3e80a01223ff0cd71b5933182c1905f240ff368edd10c8b27f2c12cf0f0c2de6.jpg)

## Karin von Funck

Managing Director

& Senior Partner

Munich

![](images/4be501fd2d80400e69f134fddc4c2b6b7dd0e9069fbecdea059915c38af56260.jpg)

## Michael Grebe

![](images/8fc3e5562d37ce90a54e73dadd39b6bcf63debbcfff914e8494d8dd1cd4de0a6.jpg)

Managing Director

& Senior Partner

Munich

![](images/56120463c61700bf95d80d8c3e335a70dcfff3b5eae44d11c6b96b2132661f93.jpg)

![](images/a4d0779cf4a0f8539cb4716d692917d8737187bfab2d0cfefb4d5aa725599c16.jpg)

## Jochen Schönfelder

Managing Director

& Senior Partner

![](images/cf652315f9a6db5bf9d42a430677a778e98c0c3d9d32bc6afbcbd60a8a08a5b4.jpg)

Cologne

## Jacopo Brunelli

Managing Director & Senior Partner Milan

## Dwight Hutchins

Managing Director & Senior Partner Boston

## Kevin Kelley

Managing Director & Senior Partner Dallas

## Rashi Agarwal

Managing Director & Partner
New York

## Mai-Britt Poulsen

Managing Director & Senior Partner London

## Disclaimer

The services and materials provided by Boston Consulting Group (BCG) are subject to BCG's Standard Terms (a copy of which is available upon request) or such other agreement as may have been previously executed by BCG. BCG does not provide legal, accounting, or tax advice. The Client is responsible for obtaining independent advice concerning these matters. This advice may affect the guidance given by BCG. Further, BCG has made no undertaking to update these materials after the date hereof, notwithstanding that such information may become outdated or inaccurate.

The materials contained in this presentation are designed for the sole use by the board of directors or senior management of the Client and solely for the limited purposes described in the presentation. The materials shall not be copied or given to any person or entity other than the Client (“Third Party”) without the prior written consent of BCG. These materials serve only as the focus for discussion; they are incomplete without the accompanying oral commentary and may not be relied on as a stand-alone document. Further, Third Parties may not, and it is unreasonable for any Third Party to, rely on these materials for any purpose whatsoever. To the fullest extent permitted by law (and except to the extent otherwise agreed in a signed writing by BCG), BCG shall have no liability whatsoever to any Third Party, and any Third Party hereby waives any rights and claims it may have at any time against BCG with regard to the services, this presentation, or other materials, including the accuracy or completeness thereof. Receipt and review of this document shall be deemed agreement with and consideration for the foregoing.

BCG does not provide fairness opinions or valuations of market transactions, and these materials should not be relied on or construed as such. Further, the financial evaluations, projected market and financial information, and conclusions contained in these materials are based upon standard valuation methodologies, are not definitive forecasts, and are not guaranteed by BCG. BCG has used public and/or confidential data and assumptions provided to BCG by the Client. BCG has not independently verified the data and assumptions used in these analyses. Changes in the underlying data or operating assumptions will clearly impact the analyses and conclusions.

![](images/2ed5d841faf0a98a3b7a76877ac823e57744f110eaf7e76d7ee08d4948f32901.jpg)
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
