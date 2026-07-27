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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Global Banking Annual Review 2025

# Why precision, not heft, defines the future of banking

Banks need to prepare for the next growth curve. Global Banking Annual Review 2025 shows how a targeted approach can help them thrive.

This report is a collaborative effort by Darius Imregun, Ido Segev, Jon Steitz, Klaus Dallerup, Marti Riba, Miklós Dietz, Pradip Patiath, and Saptarshi Ganguly, with Michael Kirchner, Suhas Gudhe, and Valeria Laszlo, representing views from McKinsey's Financial Services Practice.

![](images/a9ed9de814c53c804058d87e3667bb13a534e51bb760b0f131b7467d54a86333.jpg)

## Contents

Executive summary 2
Chapter 1
The peak before the plateau 4
Chapter 2
Banking's agentic AI era: Big gains, bigger disruption 26
Chapter 3
The new rules of engagement: Adapting to the modern banking consumer 42
Contacts 56
Acknowledgments 57

# Executive summary

In 2024, the global banking sector generated profits of about \$1.2 trillion, the highest total ever for any industry. Yet capital markets remain skeptical: Valuations trail the average of all other industries by nearly 70 percent.

Why? Markets doubt banks' recent highs are sustainable, seeing them as tailwind driven. Complicating the picture are macroeconomic forces, including declining interest rates, shifts in technology and consumer behavior, and the steady siphoning of attractive profit pools by fintechs, private credit, and wealth managers. This confluence of factors could push banks' ROE below the cost of equity in many markets.

To thrive in this new era, banks need new solutions. Macro-focused, scale-driven strategies once promised resilience but no longer suffice. Precision is the decisive differentiator, separating leading banks from slow movers and reshaping the industry's performance curve.

The “precision toolbox,” applicable to banks of any size, revamps strategy across four core dimensions:

— Technology: focusing surgically on technologies with the greatest impact—even within agentic and gen AI—while scaling back investments that don’t improve workflows, customer engagement, or business models.

— The new consumer: moving beyond broad segmentation to individualization (a “customer segment of one”), delivering hyperpersonalized, data-driven access to products and services that earn trust in an era of fading loyalty.

— Capital efficiency: shifting from sweeping reallocations to micro-level balance sheet discipline—product by product, client by client, down to individual risk-weighted assets—to free up trapped capital with precision and put it to work where it earns more.

\- Targeted M&A: moving from scale for size's sake to precision, pursuing deals that add reach in specific micromarkets or geographies, or that bring distinct capabilities in a specialized area.

Precision, not heft, is the great equalizer. In the age of AI, even smaller banks can capture disproportionate rewards by embedding precision into every dimension of strategy.

This report covers all four elements of the precision toolbox, with an in-depth look at AI and the new consumer.

AI, particularly agentic AI, holds significant promise for banking, with early adopters securing a lasting advantage over slow movers. Given these are still the early days of agentic and gen AI, it is imperative to use surgical precision to identify where these technologies can truly generate earnings impact, rather than piling into them because of the fear of missing out.

As AI is implemented across the banking industry, it could bring gross reductions of as much as 70 percent in certain cost categories. But because these savings will be partly offset by rising technology costs, the net effect on banks' aggregate cost base is expected to be a 15 to 20 percent decrease. The impact of these savings, while welcome, won't last. As with earlier innovations, competition will likely erode the gains for banks and most of the benefits will accrue to customers over time.

Longer term, AI is likely to erode bank profitability as consumers start routinely using AI agents to optimize their finances (for example, automatically moving deposits into higher-yield accounts), which would reduce customer inertia and reshape industry economics. In particular, agentic AI could disrupt deposits and credit card lending by cutting through inertia.

The threat from third-party agents could be material. If banks don't reposition their business models to adapt, over the next decade or so, bank profit pools globally could decline by \$170 billion, or 9 percent. This could reduce the average return on tangible equity (ROTE) by one to two percentage points and push many banks below their cost of capital.

But the effects won't be felt equally. AI pioneers could see ROTE increase by up to four percentage points, using their lead to reinvent models and capture value. Conversely, slow movers are likely to see lower profits long term.

Winning with consumers is also crucial. AI is shaking up how customers and banks interact, raising expectations for seamless, hyperpersonalized experiences, especially among younger generations.

Consumers are more digital, less loyal, and more deliberate in how they choose financial providers. In the United States, for example, only 4 percent of new checking account applicants choose their existing bank without first exploring alternatives, down from 25 percent in 2018. Instead, customers place more importance on the first few banks they consider in their purchasing journey. Banks that secure a place in this initial consideration set are best positioned for success.

The transformation has been driven by AI and mobile. Most consumers already use gen AI and expect their banks to provide these tools as well, while mobile is now the most widely used banking channel. Banks that integrate AI-powered insights with mobile-first, personalized experiences, blending digital ease with human connection, will define the next era of customer engagement.

To thrive, banks need to win consumer mind share, embrace mobile as the gateway for engagement, and embed AI into customer journeys before challengers seize the advantage.

One would be forgiven for assuming that the past few years have been mediocre for banking, given headlines about layoffs and worries about an economic slowdown. In reality, banks have racked up record after record without much fanfare or notice.

In 2024, funds intermediated by the global banking sector increased to \$426 trillion, nearly four times global nominal GDP, a historical high. Total revenues after risk cost generated by banks reached a record \$5.5 trillion, while a narrower measure of bank revenues from loans, deposits, and assets under management hit a record \$4.1 trillion. The ratio of this figure to nominal GDP reached its highest level ever, driven by record balances $^{1}$ and interest rate increases. Capital ratios $^{2}$ rose to 13.0 percent.

The global banking sector generated a record 1.2 trillion in net income for 2024, $^{3}$ more than any other industry, while its ROE reached 10.3 percent, a 20-year high, although still barely above cost of equity.

Typically, such numbers would be cause for celebration, yet capital markets remain skeptical about the banking sector's value creation potential relative to other industries', as they have been since 2003. That's because, despite the record-breaking numbers, banks have struggled to come up with a business model to get through leaner years ahead. Banks face a sea change due to macroeconomic factors, increased competition, and perhaps most important, advancements in AI, expected to erode profitability for most banks.

Banks' recent performance has been buoyed by favorable conditions—a peak in the global wealth cycle, unusually strong revenue margins boosted by higher interest rates, and low risk costs—but these tailwinds are dissipating. To catch the next growth curve, banks must shift from relying on traditional approaches to precision strategies that generate value in more challenging conditions. After the peaks of the past few years, the banking sector may experience a reversion to the mean, with slower growth and mounting pressure on profitability.

Different scenarios are possible, of course, depending on macroeconomic, technological, and regulatory outcomes. For example, regulatory easing in the United States could provide a boost for banks, at least in the short term. But the long-term pressures weighing on the sector are clear.

The likely reversion to the mean will be driven not just by macroeconomic factors, such as interest rate movements and demographic shifts, but also by disruption stemming from advancements in AI, intensifying competition from nonbank providers such as fintechs, and evolving customer expectations. Banks must dig into the precision toolbox to find new strategies that harness AI and data analytics $^{4}$ to create a targeted path to value. Traditional approaches such as broad digitalization programs or efficiency drives no longer suffice. Precision will be the key to value creation.

What exactly do we mean by precision? It goes beyond broad, one-size-fits-all strategies, as well as strategies that are simply “tailored”—for example, segmenting customers into broad groups and adjusting offers to cater to those groups. Precision means being data driven, targeted, hypergranular, and real time, enabling banks to focus resources where they create the most value. Even small steps ahead of competitors can trigger a positive cycle of growth and reinvestment, widening the performance gap over time.

Banks should deploy the precision toolbox across four key dimensions:

\- Technology: From broad digitalization to surgically using AI to unlock productivity and customer engagement. Precision means not just concentrating investment on the technologies with the greatest impact, particularly AI, but also scaling back or stopping unfocused programs and selectively revamping core systems. Banks spend the highest proportion of revenues of all sectors on tech, yet productivity gains have been elusive. $^{5}$ Furthermore, given the hype around AI, precision in this area is critical to ensuring that investments are geared to proven value creation. Precision helps prevent the “thousand flowers bloom” approach by focusing resources on AI applications with proven impact—for example, zero-touch operations, real-time risk monitoring, and agent-first customer service.

— The new consumer: From broad segmentation to hyperpersonalization and individualization. Traditionally, banks divided customers into large categories such as mass and affluent, delivering average solutions to these segments. Precision involves using data and AI to get to the “segment of one,” personalizing at the level of the individual—in terms of products, terms, servicing, and risk—and building seamless experiences that earn trust in an era of fading loyalty.

— Capital efficiency: From sweeping reallocations to line-by-line discipline. Historically, banks managed capital efficiency through sweeping reallocations, selective balance sheet adjustments, and broad tactical levers. Precision means conducting a line-by-line review of capital allocation—product by product, client by client to unlock every dollar of capital and put it to the best use. AI agents can run continuous optimization of risk-weighted assets, simulate scenarios, and uncover underperformance. Partnerships with insurers and private credit providers can help. So can targeted moves into beyond-banking products.

— M&A: From chasing aggregate scale to plugging gaps. In the past, banks pursued large M&A transactions aimed primarily at adding scale, often with mixed results. Precision calls for disciplined dealmaking focused on closing specific capability gaps—in technology, specialized propositions, or select geographies—and on tailoring integration and synergy capture to local market dynamics.

The rest of this chapter details industry trends and explains how the precision toolbox can help banks thrive. In the second chapter, we examine how AI offers banks ever greater levels of precision. The third chapter explores how precision in serving the new consumer will help determine which banks succeed at a time of fading loyalty.

By source of funds, \$ trillion

## Racking up records

In 2024, the banking sector went from strength to strength. It would probably surprise even most banking sector experts just how many records the industry broke.

## Outsize growth in the banking system

Before we examine bank performance, let's take a step back and assess the state of the global banking system, which intermediates funds between the sources and uses of those funds. Though the banking system involves nonbank providers in addition to banks, traditional banks intermediate the majority of these funds.

The rapid expansion of funds flowing through the banking system has consistently outpaced overall economic growth. Between 2019 and 2024, funds intermediated $^{6}$ by the global banking system grew significantly faster than global GDP (7.0 percent a year, on average, versus 4.8 percent). This trend was driven by elevated interest rates, increased savings during the COVID-19 pandemic due to government stimulus and changing consumption patterns, and robust investment activity, which sent additional capital through banks and asset managers, increasing the volume of funds they intermediate. Over that period, retail funds managed by financial institutions increased 6.0 percent annually, and institutional funds grew 7.7 percent annually (Exhibit 1). Funds in the banking system

## Exhibit 1

Funds intermediated by the global banking system have grown sharply.

Volume of funds intermediated by traditional banks and nonbank providers

![](images/9a7510c16983045292c21882d1465d0396e2f9110561a4908cf760f34d25273a.jpg)  
By balance sheet placement, %

![](images/590c691a6eb804458fa4cfdafb0a834a1aace5002ae0b6e4601bec6f79367d7d.jpg)  
Note: Figures may not sum to total, because of rounding.  
$^{1}$ Including public pension funds, sovereign wealth funds, and other alternatives (eg, hedge funds, real estate funds). $^{2}$ Including private debt and private equity.  
$^{3}$ Including banks' bonds and other equity, corporate deposits, corporate investments, endowments, foundations, and others. $^{4}$ Including insurance and pension holdings, mutual funds, retail deposits, and securities and derivatives held by households. Source: S&P Capital IQ; S&P Global Market Intelligence, accessed Sept 2025; McKinsey Panorama—Global Banking Pools

McKinsey & Company

originating from private capital experienced the fastest growth, expanding by 17.2 percent a year, underscoring private capital's rising influence in global markets. $^{7}$

A subcategory of intermediated funds, the global wealth of households and institutions, has been on an upward trend, helping to propel the banking industry's revenue growth. Over the past five years, global wealth as a percentage of nominal GDP surpassed the 350 percent mark. Personal financial assets, $^{8}$ a component of wealth, show similar dynamics (Exhibit 2). These developments illustrate the reallocation of wealth from real-economy assets toward financial instruments, a hallmark of finance's growing role in the global economy.

The trend of high wealth and financial assets relative to nominal GDP applies worldwide, though regional outcomes vary. Africa stands out, recording its highest levels in these metrics since 2000.

However, global wealth could be at a peak, as it's likely to be affected by demographic shifts that will play out over the next few decades. An aging population and lower birth rates will result in fewer new savers and investors. $^{9}$ Moreover, there's a generational shift in wealth, with more women and younger people seeking wealth management services. $^{10}$ Financial institutions are often ill equipped to manage the transition of wealth for the next generation, particularly those

## Exhibit 2

Total global wealth compared with nominal GDP 2000–24, $^{1}$ %

Global financial wealth as a share of GDP is at historically high levels.  
![](images/6b19d1b01d13801349f7f69328484ea7452dc4a94da21287c32a4fb68c2d4b64.jpg)  
$^{1}$ Values estimated for 2024.  
$^{2}$ Includes corporate deposits, institutional assets under management, and private capital.  
$^{3}$ Includes insurance and pension holdings, retail deposits and investments, and securities and derivatives held by households.  
Source: S&P Capital IQ; S&P Global Market Intelligence, accessed Sept 2025; McKinsey Panorama—Global Banking Pools

McKinsey & Company

who aren't part of the ultra-affluent segment. This gap could lead to a loss in market share for traditional banks as younger, more diverse clients seek out more tailored and accessible financial solutions. Additionally, the mix of intermediated funds is shifting away from banks toward alternative assets such as private capital, private equity, and even cryptocurrency, reflecting a growing appetite for higher-risk, higher-reward investments. For instance, about half of people born between 1981 and 2012 have invested in crypto. $^{11}$ This shift requires banks to use precision to adapt their strategies and risk management practices to effectively serve clients. Compounding these shifts, a McKinsey Global Institute report published in October 2025 shows that global wealth has become decoupled from productive growth, propped up by debt and asset inflation—raising questions about the sustainability of wealth levels relative to underlying economic output. $^{12}$

## Revenue growth

Not only did global banking revenues reach an all-time high in 2024, but they are increasing much faster than GDP, thanks to record balances and an advantageous margin cycle (Exhibit 3).

## Exhibit 3

Bank revenues have been boosted by high balances and strong margins.

Global banking revenues, balances, and margins, %

Revenues $^{1}$ as a share of nominal GDP

![](images/f263150a7fe87a2432ef88585d654c1f79f62a9bd4c49711b6492c661f3846d9.jpg)  
1 Bank revenues are at their strongest point in 2 decades, now making up 3.6% of global GDP  
Balances $^{2}$ as a share of nominal GDP

![](images/f6d1985e5bd04ff63a9156740dd3efc2af8106921c919c2057372dcaea18ad40.jpg)  
Revenues $^{1}$ over balances

![](images/db55fd2d1186b8a9a8254efe1b0dc990e147e7b4dbb8c4158274295dfc7095d3.jpg)  
2 One reason for this trend is elevated bank balances, equal to about 340% of GDP  
3 At the same time, as margins have improved, banks are earning more from each dollar of balances

$^{1}$ After risk cost. $^{2}$ Including assets under management, deposits, and l

[中间内容因长度限制已省略]

nderserved customers, gained share rapidly, and built an edge. Today, the bank continues to lead with data-driven personalization, using AI and cloud technologies to refine offerings and strengthen digital experiences.

Similar patterns have appeared in telecommunications, where providers that shifted from broad segmentation to individualized offers reshaped competition. Banking—with its multiple levers for personalization, including risk—has even greater potential to turn precision into long-term advantage. With the precision toolbox, banks can offer more precisely tailored products and services to the right customers at the right time, leading to improved customer satisfaction, primacy, and profitability.

For example, banks can aggregate signals from multiple data sources—such as in-house accounts, transaction histories, and accounts with other financial providers—to detect subtle indicators of significant life changes. They can then use gen AI to interpret these signals in real time to not only identify behavioral risks but also craft an experience custom made for each customer, enabling the delivery of hyperpersonalized offers and communications.

Today, using AI tools, banks that deploy precision in messaging, targeting, timing, and channel presence will capture consumers' mind share early, while those that rely on scale or generic campaigns risk being left behind.

The banking industry's next growth curve won't be won by scale but by precision. Leaders that embed precision into strategies involving technology, customer engagement, capital allocation, and M&A will capture outsize rewards, while slow movers clinging to the old playbook risk decline. In this new era, precision isn't just a strategy—it's the avenue to profitable growth. If banks can put the precision toolbox to good use, the sector's massive valuation gap can begin to close, resulting in true value creation for the banks that get it right.

## Authors

Darius Imregun
Partner, Boston
darius\_imregun@mckinsey.com

Ido Segev
Senior partner, Boston
ido\_segev@mckinsey.com

Jon Steitz
Senior partner, Bay Area
jonathan\_steitz@mckinsey.com

Klaus Dallerup
Senior partner, Copenhagen
klaus\_dallerup@mckinsey.com

Marti Riba
Partner, Barcelona
marti\_riba@mckinsey.com

Miklós Dietz
Senior partner, Vancouver
miklos\_dietz@mckinsey.com

Pradip Patiath
Senior partner, Miami
pradip\_patiath@mckinsey.com

Saptarshi Ganguly
Senior partner, Boston
saptarshi\_ganguly@mckinsey.com

Michael Kirchner
Associate partner, New York
michael\_kirchner@mckinsey.com

Suhas Gudhe
Associate partner, Miami
suhas\_gudhe@mckinsey.com

Valeria Laszlo
Panorama senior asset leader, Budapest valeria\_laszlo@mckinsey.com

## Regional leadership contacts

Asia
Renny Thomas
Senior partner, Mumbai
renny\_thomas@mckinsey.com

Europe, Middle East, & Africa
Stephanie Hauser
Senior partner, London
stephanie\_hauser@mckinsey.com

Latin America
Felipe Villarreal
Senior partner, Panama City
felipe\_villarreal@mckinsey.com

North America
Ishaan Seth
Senior partner, New York
ishaan\_seth@mckinsey.com

# Acknowledgments

The authors would like to thank the following colleagues for their contributions to this report:

## Partners and senior partners

Amit Garg, Dan Williams, David Remley, Federico Berruti, Felicia Tan, Felipe Costa, Felipe Villarreal, Fernando Ferrari-Haines, Fuad Faridi, Ishaan Seth, James Kaplan, Javier Martinez Arroyo, Jonathan Godsall, Joydeep Sengupta, Marukel Nunez Maxwell, Max Flötotto, Paul Maia, Renny Thomas, Roberto Marchi, Roger Rudisuli, Stephanie Hauser, Uzayr Jeenah, Vik Sohoni, Vinayak HV, Violet Chung, and Vishnu Kamalnath.

## Analytics and solutions colleagues

Anubhav Das, Belian Kiss-Borlase, Blanka Koji, Csanad Kortvelyessy, Debopriyo Bhattacharyya, Enrique Briega, Garima Ailawadhi, Istvan Rab, Jay Datesh, Luca Pato, Mayar Abdelaziz, Nurzhan Onashabay, Rauhan Nazir, Sanjana Agarwal, Sergey Khon, Shikha Gupta, Tanuj Sachdeva, and Urvashi Jain.

## Production team

Annie Tan, Anouk Frieden, Eszter Teszarik, Gretal Tang, Julia Shamayskaya, Lisa Kondo, Mark Staples, Matteo Camera, Polina Skladneva, Pomponia Orehoczki, Roberto Truque, and Teresa Diviu.

The authors also wish to thank the following banking equity analysts and experts for their insights: Brian Foran and John McDonald at Truist Securities; Guy Moszkowski, cofounder of Autonomous Research US and now senior advisor at McKinsey; Mathias Nielsen at Nordea; and Mike Mayo at Wells Fargo Securities.

This report was edited by Jana Zabkova, a senior editor in the New York office, and developed and produced by the McKinsey Global Financial Services Marketing and Communications team:

## Matt Cooke

Director of communications and marketing
matt\_cooke@mckinsey.com

## Monica Runggatscher

Public relations lead
monica\_runggatscher@mckinsey.com

## Chris Depin

Communications coordinator
chris\_depin@mckinsey.com

This annual review of the global banking industry is based on data and insights from McKinsey Panorama, McKinsey's proprietary banking research arm, as well as the experience of clients and practitioners from all over the world. We welcome comments about this research at fs\_external\_relations@mckinsey.com.

McKinsey & Company

October 2025

Copyright © 2025 McKinsey & Company. All rights reserved.

McKinsey.com

X @McKinsey

@McKinsey

in @McKinsey

This publication is not intended to be used as the basis for trading in the shares of any company or for undertaking any other complex or significant financial transaction without consulting appropriate professional advisors.

No part of this publication may be copied or redistributed in any form without the prior written consent of McKinsey & Company.
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
