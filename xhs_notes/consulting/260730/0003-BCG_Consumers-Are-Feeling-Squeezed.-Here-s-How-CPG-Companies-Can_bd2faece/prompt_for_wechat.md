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
![](images/afd5ef7b9ec367951ccd9b8d8ac773bcf413388bdd2caa136f53e668c27e3119.jpg)

CONSUMER PRODUCTS INDUSTRY

# Consumers Are Feeling Squeezed. Here's How CPG Companies Can Adapt.

By Alicia Pittman, David Webb, Luke Pototschnik, Geraldine Rhodes, Anastasia Kouvela, Amy Kondo, and Amber Chourasia

ARTICLE JANUARY 07, 2026 8 MIN READ

Consumer packaged goods (CPG) companies are facing a brutal environment. Consumer spending is slowing as households cut back, trade down, and turn to private-label products. At the same time, inflation is eroding spending power and pushing CPG costs up, while tariff volatility creates

additional uncertainty. These conditions aren't going away, and how companies respond will separate the winners from the rest.

Many CPG companies are countering these disruptions with supply chain productivity initiatives, price tweaks, and promotional shifts—but these tactics are not enough. To stay ahead, companies must go bigger and bolder with cross-functional, cross-product, and cross-company cost-reduction programs. Leadership teams need to focus on the most relevant and impactful areas, and—critically—they need to leverage analytics and AI (including GenAI) in a way that delivers returns.

In our work with leading CPG businesses around the world, we’ve seen how those that act decisively and holistically win on cost while reigniting growth.

## Why Most Cost Programs Fail

In a recent BCG survey, 60% of global CEOs in the consumer sector cite cost management as a top priority moving forward, along with other strategic goals like managing prices and growing volume. But launching a cost program is the easy part; generating value and making it last is not. In the same survey, half of global consumer CEOs said their previous cost efforts failed to deliver sustainable savings—or worse, they cut spending in areas critical to growth.

Why do most cost programs fail? Our experience turning around underperforming efforts points to some common missteps:

\- False Victories. Companies often claim success when they hit their cost-reduction targets (such as better asset utilization, eliminating some IT applications, or reducing overhead), but these don’t translate to sustained gains in the profit and loss statement.

\- Siloed Targets. Leaders focus on familiar, and often functionally specific, cost levers, while neglecting the cross-business moves that will generate a bigger impact.

\- Weeding Instead of Mulching. Companies chase short-term savings only to see costs grow back like weeds. Lasting impact requires holistic, structural solutions—mulching to keep costs from growing in the first place.

\- Outdated Processes. Organizations rely on outdated, often manual decision-making processes and incentive systems that handicap productivity and competitiveness.

\- Insufficient Resources. Too often we see cost programs that have a leader but lack sufficient resources or buy-in from teams. Companies kick off projects but don’t see them through to the finish line.

# A Smarter Approach: AI-Powered Holistic Cost Reduction

To unlock sustainable value, companies must adopt a holistic approach that pulls from the full suite of cost levers across the value chain. But the same breadth that makes holistic cost reduction so powerful also makes it challenging—these efforts require deep expertise across functions, product lines, and markets, plus the scale to execute globally.

Successful programs share several key attributes. They are strongly linked to strategy, with cost targets aligned to the company's overall strategy and plans for total shareholder return. This in turn directs resources to the highest areas for return on investment.

Winning programs also feature AI-powered spend assessment and reduction. With today's real-time data, digital, and AI tools, and the right agile governance around decision-making, CPG companies can quickly assess cost drivers to pinpoint the biggest structural costs, leveraging GenAI to accelerate analysis and move faster from insight to action. Through this approach, companies can eliminate $5\%$ to $20\%$ of the cost base, depending on the function, while also improving the speed to market and service levels.

The most successful cost-reduction programs are led by activist transformation management offices with dedicated resources, whose people have a seat at the executive table.

Programs that work through cross-functional sprint teams also come out ahead because cost initiatives span key areas of spend. That way, teams across functions, including end-to-end cost practitioners, deep functional experts, and AI specialists, work in lockstep to complement and reinforce each other.

Another attribute separating winners from losers is the right kind of transformation office. The most successful cost-reduction programs are led by activist transformation management offices with dedicated resources, whose people have a seat at the executive table to ensure delivery, swiftly address emerging issues, and provide leaders transparency about program status.

Finally, successful programs require decisive implementation. Leaders are held accountable to move quickly to execute and wire into the budget a portfolio of initiatives. These are prioritized by return on investment (ROI) and benchmarked against evolving competitor cost structures. Initiatives include both quick wins to fund the journey and longer-term initiatives that deliver bigger gains.

# The Full Solution Map: Three Comprehensive Cost Levers

Companies should pull cost levers across operational, functional, and commercial areas to drive margin impact. (See “Transforming a Global Beverage Leader for Breakthrough Performance.”) Which levers to pull, how to pull them, and in what order depends on each company’s position and priorities.

## - Transforming a Global Beverage Leader for Breakthrough Performance

Facing cost pressure, a multibillion-dollar global beverage company launched an ambitious, enterprise-wide transformation to reduce costs and improve performance across supply chain, commercial, and functional support areas. By taking a cross-enterprise view and sequencing initiatives for maximum impact, the program dramatically increased efficiency in operations, in metrics like higher manufacturing OEE, increased warehouse throughput, and stronger service levels for priority parts of the business. Overall, the program led to a 20% profit increase within a few years, while also positioning the company for sustained growth and competitiveness in a rapidly evolving market.

Operational Levers. The first set of measures addresses how organizations buy and produce goods:

\- Manufacturing. Reduce costs and boost productivity through lean operations, digital upgrades, and frontline GenAI enablement. Improve overall equipment effectiveness and optimize production capacity to lower fixed costs. Use advanced analytics to evaluate total landed costs across sourcing and manufacturing models under varying trade and labor scenarios. Explore partnership options—such as comanufacturing—to reduce costs and make operations more resilient.

\- Supply Chain. Rethink the full network and optimize within: right-size the network footprint and partnerships across warehouse, logistics, and distribution functions to improve service levels and productivity. Optimize within the footprint, bringing digital lean beyond manufacturing into warehouses, and leverage real-time analytics and digital twins for optimal, cost-efficient routing. Step up end-to-end, AI-enabled planning capabilities to minimize waste and lost orders.

\- Procurement. Improve sourcing and negotiation across direct and indirect procurement. Use AI to increase spend transparency, refine contract policies, and scale supplier negotiations. Rethink business needs and operating model changes to drive down indirect spend. (For example, different sales models can bring sales teams closer to the customer while reducing travel costs.)

Reduce costs and boost productivity through lean operations, digital upgrades, and frontline GenAI enablement.

Functional Levers. The second set of measures addresses how organizations manage core business functions:

\- Marketing Spend. Use ROI to reallocate marketing spend, plan effective activations, and optimize retail media. Leverage consumer data to stay aligned with evolving trends and tailor marketing by channel.

\- Go-to-Market and Sales. Review the sales strategy, operations, execution, and operating model to improve top-line growth while managing commercial spend.

\- Organizational Costs. Fundamentally rethink how work gets done and the operating model needed to sustain it. Build GenAI capabilities to improve productivity, reduce complexity, and streamline decision making.

\- IT Costs. Streamline tech, digital, and data spend by cutting redundant applications and using fit-for-purpose or second-tier solutions. Leverage automation and AI in recompetes for outsourced IT services to obtain savings up to 20%. Move up to 70% of tech roles to hubs in low-cost regions in India, Latin America, and Eastern Europe.

Leverage consumer data to stay aligned with evolving trends and tailor marketing by channel.

Commercial Levers. The third set of measures addresses how organizations price products and manage trade:

\- Trade Terms. Tie customer trade funding to specific behaviors (for example, distribution, feature, and display support) that improve sales velocity at the shelf. Rightsize nonworking trade levers like bracket pricing, payment terms, and logistics allowances.

\- Promotions. Adjust promo calendars to prioritize the highest ROI and lift-driving tactics. Use AI-powered engines and predictive models to simulate thousands of promotion scenarios and pinpoint the optimal timing, mechanics, and mix.

\- Price-Pack Architecture. Offer different pack sizes and formats to meet relevant demand occasions and maximize customers’ willingness to pay. Rationalize the long tail by deprioritizing low-value SKUs and focusing on high-impact core items.

# Where to Hunt: Imperatives Across Levers

Across the full map of levers, we’ve found several measures that can help give companies a clear cost advantage.

Balance savings and investment. Many CEOs feel pressure to go into austerity mode right now, but companies can't cut their way to growth. The challenge is finding space to invest even when budgets tighten. The winning organizations strike the right equilibrium between disciplined efficiency and targeted reinvestment in capabilities that sustain long-term momentum.

Deploy de-averaged revenue growth strategies. Move beyond one-size-fits-all approaches by leveraging granular data, advanced analytics, and dynamic portfolio management to capture incremental growth and margin.

Harness digital and GenAI. Embed intelligent automation and generative copilots to amplify human capacity at scale, from procurement negotiations that optimize spend in real time to AI-assisted promotional and demand planning aimed at sharpening ROI. (See “Reducing Costs with Digital and GenAI.”)

## - Reducing Costs with Digital and GenAI

A leading CPG manufacturer launched a program to automate core business processes using digital tools and GenAI, leading to substantial efficiency and performance gains. Initiatives focused on reducing waste and low-value work across functions—optimizing labor and streamlining logistics—while simultaneously improving service levels. Overall, the program reduced costs related to penalties and fees by more than 20%, freed up labor hours in key processes by 10%, and improved the customer experience by providing faster response time and more consistent service levels. Through this approach, the company freed up resources that it could reinvest to fuel future growth.

Redesign supply chains and operations for the new normal. In a world of geopolitical uncertainty, unlock the full power of AI that is currently dormant in expensive IT investments through people and process excellence. Reassess network footprints and sourcing—and build internal capability to keep doing it, because volatility on trade and policy direction is here to stay.

The global chessboard has changed, and traditional cost programs and siloed workstreams will not cut it in today's macroenvironment. To stay competitive, leaders must pursue bolder, broader, and holistic cost transformations. Those that move decisively will protect margins and reshape their position. Those that wait for conditions to improve may face checkmate.

## Authors

![](images/cb31ce92efe89aad4fd388a9cee6134e9f92c29fce520ba43ea95b30c974a311.jpg)

![](images/9bb2aa75828123333961bb748a287b376139a63e677bd3a5650198fe9ff2a534.jpg)

![](images/645174f91deb84875a0379b2c4120849a81c0de453fb4ca6ad444f5bb5b591a3.jpg)

![](images/e9fc3ee49d9fd81168f2783dcdfaa9ba0b3b35139649270969bbb6fb8bdf1153.jpg)  
Managing Director & Senior Partner; Global People Chair
Washington, DC

## Alicia Pittman

![](images/7ca4984722a27d3702321eeae42fbe58b7cd05cff6b93de1f57186920428d1e3.jpg)

## Luke Pototschnik

Managing Director & Senior Partner
Nashville

![](images/a2646d93b08be0a1d201e29d16f07746eb6e969df83eba33c152b2889c03eb05.jpg)

## Anastasia Kouvela

Managing Director & Partner London

![](images/dcbb386dd5ddef59d8be9105f0f061c6a80529811f3ff68082de9620ad7f3742.jpg)

![](images/e21cde75a3b0aa397bea9489ca618161726a862dd23cf733cd1d6b35ce93c34f.jpg)

![](images/c232296b2cb2ed144d0e7062141a694b7070657c96792864bba7e1bea2d87430.jpg)

## Amber Chourasia

Senior Manager - BCG Vantage
London Canary Wharf

## David Webb

![](images/99369265b1617d391a996b7a290132088d1703173c61d4d1899425b6d49e12a2.jpg)  
Managing Director & Senior Partner, Chief Sustainability Officer, Managing Director of North American Systems
Philadelphia

![](images/e1f6b2f503d8f5632afacf68ee9ebf47b097c31cf41f32ff7f0b418f070eae39.jpg)

![](images/32479d87a09ae4e3de1d8fffc04cce63e77809a9c658ed4de0accb453bdd4fc0.jpg)

## Geraldine Rhodes

![](images/d3ca42901d89437d2f276c4d2a2708afe17229808d9eb7a1ab4e6cf3a3b23026.jpg)

Managing Director & Partner
Washington, DC

## Amy Kondo

Partner
Washington, DC

![](images/9fb63498a987aabac24d84ee227f9c714b65606073df66315d9b91fc2b8cfb61.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

## © Boston Consulting Group 2026. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and X (formerly Twitter).
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
