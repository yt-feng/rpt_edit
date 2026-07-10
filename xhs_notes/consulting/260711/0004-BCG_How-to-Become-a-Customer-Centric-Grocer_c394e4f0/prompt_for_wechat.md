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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# HOW TO BECOME A CUSTOMER-CENTRIC GROCER

By Gavin Parker, Thomas Jensen, Pascale Morillon, Bill Urda, and Stephanie Halgren

FOR GROCERY RETAILERS, customer-centricity is a bit like personal virtue: everyone agrees that it's a good thing, and no one can possibly argue against it, but actually achieving it is a challenge. Most grocery executives understand that they need to put their customers first, and many have initiatives in place to do so. Yet in most cases, these efforts result in marginal programs that don't fundamentally improve the customer experience.

Consequently, large grocers in markets around the world are struggling as they face more competitive threats than ever, from a wider array of players. Discounters can beat grocers on price, and specialty retailers can beat them with a deeper selection of products and better service and expertise in a specific category. In this environment, the only way that grocers can differentiate themselves and grow is by identifying the things that matter most to their customers and then executing to meet those needs. Grocers must understand their unique value proposition and create a far more relevant customer experience in stores, online, in marketing communications, and at every other touch point with customers.

A grocer's success depends on more than an incremental initiative or two. It requires fundamentally rewiring the organization to put the customer first—aligning the company's culture, brand strategy, operations, and organizational and cultural enablers. There is a real opportunity to engage employees more effectively, to make customers happier, and ultimately to improve the company's financial performance.

This is the third publication in BCG's “Retail Revival” series. In the first piece, we discussed how grocery transformations must begin at the store level. (See “Succeeding with a Store-Led Strategy,” BCG article, September 2014.) In the second, we focused on clarifying the customer value proposition, resetting categories, and aligning operations to deliver on that promise. (See “Help Your Shelf: The Moves Mainstream Grocers Must Make Now,” BCG article, April 2016.) In this third and final part of the series, we explain how grocers can promote customer-centricity throughout the organization by fostering the right culture, using analytics, and developing employees' capabilities.

## Stores Tend to Be as Homogenized as the Milk

Almost all grocery executives tell us that they are customer-centric. And yet the customer experience in most grocery stores is bland and interchangeable. BCG's Brand Advocacy Index research, which looks at companies across all industries, supports this. (See “The Most Recommended Brands 2015,” BCG article, September 2015). Customers’ expectations have changed, and many grocers haven’t kept up. Given the industry’s narrow margins, the situation is understandable: Most companies have focused on supplier relationships and trade spending. Their primary objectives have been to streamline processes, reduce costs, and match their competitors’ tactics on pricing and assortment—priorities that invariably lead to decisions aimed at improving stores’ financial performance, rather than upgrading their customer experience.

A recent BCG survey of companies across industries found that fewer than half of the leadership decisions that companies make reflect insights into customers. (See “The Introverted Corporation,” BCG article, April 2016.) The numbers for strategic decisions—such as portfolio strategy and mergers and acquisitions—are even worse: only one-third are made with the customer in mind. In four of every five responding companies, customer insights played a major role only in commercial functions such as sales and marketing.

Technology has upended that thinking. Customers today are less brand-loyal and more empowered by technology to compare prices and shop around, often by smartphone, and younger people are more willing to visit multiple stores. Consumers want to be able to quickly find exactly what they're looking for, and they'll seek elsewhere if a store fails to meet their expectations. New market entrants are another challenge.

Discounters typically offer significantly lower prices on a limited set of products—up to 60% lower in some categories—and they are starting to catch up to full-line grocers in quality as well. On the other hand, although some discounters have put significant thought into improving the customer experience—with fun, innovative store features—many are expanding to a point where they look and feel closer to a traditional grocery store. As a result, they must guard against diluting the very features and experience that attracted customers and fueled their growth over the past decade.

Meanwhile, specialty retailers are winning against traditional grocers in ever narrower segments. In this environment, incumbent full-line grocers are stuck in the middle, with higher prices and a less compelling customer experience.

## Five Priorities for Leadership Teams

If companies are to compete effectively and grow in the current environment, they need to consistently provide a relevant and differentiated customer experience across all channels. A company can't simply focus its customer initiatives on a few parts of its operations such as store operations and marketing, because success won't come through an isolated program or change effort. Instead, customer needs must become a core strategic theme—a central organizing principle in what the company does and how it thinks on all fronts. Besides affecting obvious aspects such as store design and layout, customer needs should influence how the company handles pricing and assortment, how it works with suppliers, and how it makes virtually every other decision, every day, from the board room to the store floor.

That level of rethinking calls for changes in the company's organization model, processes, systems, employee engagement, and corporate culture. It's a complex challenge, but we think it comes down to five strategic priorities. Most companies focus on one or two of these, but few address all of them.

Give senior leadership a baseline understanding, grounded in data, of the company's customers. Change toward dedicated consumer-centricity starts in the C-suite, with a strong endorsement of change from the CEO (and not merely the CMO, who oversees the customer experience at most grocers). The senior leadership team should gather available customer data from loyalty schemes, point-of-sale systems, syndicated agencies, e-commerce data, and the company's proprietary research (including direct conversations with customers), and then aggregate that data in a single, baseline view of the customer. C-level leaders should then carefully review the insights from this data and identify potential gaps that call for more investigation.

At many companies, where customer insights show up only in certain areas of the organization such as marketing, adopting this approach means committing to a major change in mindset. (Grocers tend to be far more disciplined in tracking their financial performance and their competitors' moves, than in tracking their own customers.) Customer insights need to become a common language throughout the organization and a critical conceptual foundation that shapes and informs all future strategic and tactical decisions—in stores, at centralized departments such as logistics, and in back-office functions such as HR.

Create a customer-centric culture grounded in the company's purpose. Because the move to a consistently consumer-centric orientation is so comprehensive, companies need to develop a complementary culture that provides guidance for all employees and reinforces “the way we do things around here.” Fostering this culture requires understanding and articulating the company’s purpose, a central organizational ethos reflecting something that goes deeper than the company’s bottom line. For example, one grocer’s purpose might be to help its customers become healthier (by carrying a greater variety of fresh produce, organic goods, and similar items), while a second grocer’s purpose might be to delight its customers (by designing stores to be fun and unconventional).

Pursuing the right purpose addresses the needs of customers, but it also gives greater meaning to the work that employees do. BrightHouse, a division of BCG, found that having a purpose grounded in shared values led to a greater sense of loyalty among employees, turned customers into brand advocates, and ultimately yielded better financial performance. Across all industries, organizations with a purpose-driven culture enjoyed substantially higher revenue and better stock performance than their competitors.

Once the company is aligned behind a specific purpose regarding its customers' primary concerns, management needs to translate that viewpoint into a common language, using insights from customer data—so that everyone understands the goal and can communicate it in a consistent manner. This language runs through all strategic and operational initiatives, and ultimately into a set of customer promises that clarify the organization's priorities. For example, a customer promise might be that the grocer will offer the lowest prices no matter what, or it might be that customers will leave the store happier than they were when they arrived.

Such promises serve as lodestars for the workforce. Some grocers have more than a million employees, many of whom deal directly with customers every day and thus directly influence those customers' experience. Given such large head counts, it's not practical or desirable to issue scripted rules for how to respond in specific situations throughout a workday. Instead, developing the right purpose—and translating that purpose into a small number of customer promises upheld across the organization—gives employees the tools they need to make the proper customer-centric decisions on their own, without requiring explicit guidance or resorting to a playbook from HR.

Develop KPIs to measure progress and reward improvements. Companies should develop KPIs to systematically track, store by store, how well they are carrying out their customer promises and to make

rapid, tangible improvements over time. Many grocers already have KPIs and dashboards in place, but these tools tend to emphasize financial performance. Customer experience needs to be a critical part of a company's dashboards too, and the metrics need to be as concrete and granular as possible. This will enable the company to convert the qualitative experience it delivers to customers into quantitative yardsticks, which it can then analyze and use to devise tangible steps toward improvement, in stores and throughout the organization. Specific KPIs include in-store metrics (such as product availability, time spent in checkout lines, and store cleanliness) and loyalty measures (such as a customer's increased affiliation with the brand and willingness to recommend it to friends, or growth in the number of loyal customers the store has). If a store receives low customer-service ratings, the company might respond by shifting top-performing employees to other departments, offering events such as tastings, or taking other steps to rectify the problem quickly.

Critically, a grocer's KPIs should be linked to employees', managers', and senior leaders' incentive plans. If a customer-centric culture is to succeed, people from the boardroom to the shop floor need to know that they will be rewarded for making gains—and feel the financial consequences if they fall short.

Use analytics to make customer-oriented decisions. Understanding customers' expectations entails understanding their emotional, functional, and experiential needs. Analytics can give companies deep insights into these aspects of their customers, especially in three particular areas.

One crucial application of analytics involves studying customers to determine how they shop and what they want, down to the level of individual products. Another involves using this information to understand the potential trade-offs associated with every operating decision the company makes, such as pricing, promotions, and new service levels in stores. At each decision point, the insight should help answer a fundamental question: will this decision improve or erode the customer experience, and by how much? A third application of analytics is to gauge the company's performance in meeting its customers' expectations, so that the company can continuously refine its service and offerings.

Many traditional grocers are accustomed to basing their decisions on gut instinct—or on financial objectives or their competitors' actions—rather than on customer-data-driven insights. For example, consider a grocer that carries seven types of strawberry yogurt. Although analytics may reveal that customers strongly favor five of those options, eliminating two brands may seem counterintuitive, since merchandisers tend to believe that offering more choices is automatically better than offering fewer. Yet the right data and analytics can help the grocer accurately determine whether reducing the range of options will lead to a better customer experience (as is often the case). To make that decision, however, the company must ensure that it has the right data and capabilities in place, and it must be willing to make decisions that may seem counterintuitive—and may run counter to what the competition is doing.

The same principle holds true for private-label products. In-depth research can often help a grocer understand what customers don't like about certain products that it stocks, and the company can then respond by creating its own branded versions to address those shortcomings.

Invest in the company's people. Employees make or break the customer experience. Companies need to train their workers in both hard skills (such as technical abilities) and soft skills (such as communication and customer engagement), with an unwavering emphasis on putting the customer first and building advocacy and loyalty. Adopting the right training approach will help employees understand the key role they play in creating a positive customer experience and recognize how specific—and often seemingly small—actions can improve that experience. Brand loyalty is built on authenticity and genuine interactions; employees must understand this and feel empowered to create these crucial experiences for customers.

When a customer complains, store associates should be trained to treat the situation as an opportunity to build loyalty by fixing the problem in a way that surprises and delights the customer. Some companies in other industries give employees a small amount of discretionary money that they are authorized to spend to rectify problems and please customers. Similarly, a grocer might give its employees the leeway to open a package on request to give a customer a sample. Or it might permit them to accept returns from customers—no questions asked—without requiring a manager's approval.

In addition, companies need to reinforce employees' awareness that the best ideas often come from the bottom up, thus encouraging and empowering employees to take measures that the training did not exexplicitly cover. Employees should have clear, two-way communication processes that enable them to give suggestions and feedback to top management.

A S THE TERM itself suggests, customer-centricity entails putting the customer at the heart of everything a company does. Yet most grocers don't operate that way. Instead, they tend to separate their customer insights into a few isolated functions, while focusing far more on their financial performance and on the moves their competitors make. The situation opens a real opportunity for companies to create a sustainable competitive advantage by taking deliberate steps to better understand customers and by considering how every decision the company makes will ultimately affect them. This undertaking involves making a profound shift toward consumer-centric planning and management—a shift that requires a lot of hard work. Yet there are clear rewards for companies that get it right.

## About the Authors

Gavin Parker is a partner and managing director in the Melbourne office of The Boston Consulting Group. He leads the firm's global work in retail transformation and reinvention, particularly among large national and international grocery chains. You may contact him by email at parker.gavin@bcg.com.

Thomas Jensen is a partner and managing director in the firm's Stockholm office. He leads the firm's Consumer practice in the Nordic countries, and he is a core member of BCG's Marketing, Sales & Pricing practice. You may contact him by email at jensen.thomas@bcg.com.

Pascale Morillon is a principal in BCG's London office. You may contact her by email at morillon.pascale@bcg.com.

Bill Urda is a senior knowledge expert in the firm's Washington, DC, office and a member of BCG's Consumer practice, specializing in the grocery sector. You may contact him by email at urda.bill@bcg.com.

Stephanie Halgren is a senior knowledge analyst in BCG's Washington, DC, office and a member of BCG's Consumer practice. You may contact her by email at halgren.stephanie@bcg.com.

The Boston Consulting Group (BCG) is a global management consulting firm and the world's leading advisor on business strategy. We partner with clients from the private, public, and not-for-profit sectors in all regions to identify their highest-value opportunities, address their most critical challenges, and transform their enterprises. Our customized approach combines deep insight into the dynamics of companies and markets with close collaboration at all levels of the client organization. This ensures that our clients achieve sustainable competitive advantage, build more capable organizations, and secure lasting results. Founded in 1963, BCG is a private company with 85 offices in 48 countries. For more information, please visit bcg.com.

© The Boston Consulting Group, Inc. 2017. All rights reserved. 3/17 Rev. 7/17
"""
