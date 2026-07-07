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
![](images/ae3149960295300c29261f623c7e1e3226309fbf20f6dc7fcc0a178a353003a5.jpg)

B2C PRICING

# Overcoming Retail Complexity with AI- Powered Pricing

By Javier Anta Callersten, Sebastian Bak, Robert Xu, Roelant Kalthof, and Scott Bradley

ARTICLE APRIL 16, 2024 8 MIN READ

Retailers are in a new age of pricing, and they need a new set of tools. Persistent cost inflation, lingering supply chain volatility, ongoing shifts in consumer spending, and intensifying price competition have created a level of complexity that is more than retailers can manage using traditional retail price-setting tools and methods. Instead of sticking with traditional rule-based approaches that focus on simplification, retailers are now implementing AI-powered solutions and dynamic pricing models.

These solutions enable retailers to transform the complexity of their markets from an obstacle into a valuable resource. Those that have made this transition have increased gross profit by 5% to 10% while also sustainably increasing revenue and improving customer value perception. (See Exhibit 1.)

Exhibit 1 - The Impact of Improving Pricing Capabilities

![](images/2d3bffbc279091fb5c93035189814c6f20ddfabe858187518891aa4efc93f76d.jpg)

With AI-powered solutions, retailers can translate their strategic choices into optimal prices for each product and store. They can respond dynamically to both internal and external changes, while maintaining alignment with a clear, customer-centric pricing strategy.

With AI-powered solutions, retailers can respond dynamically to both internal and external changes, while maintaining alignment with a clear, customer-centric pricing strategy.

# How Retailers Are Implementing AI-Powered Pricing

AI-powered price optimization requires holistic problem solving across multiple dimensions. (See Exhibit 2.) Rule-based pricing, meanwhile, tends to focus on only one or two of these dimensions, usually at an aggregated level, because available tools and data do not allow a retailer to embrace complexity. Armed with richer, faster insights into what customers want, retailers can target their investments in ways that can improve volumes, margins, and customer value perception simultaneously.

Exhibit 2 - AI-Powered Engines Embrace the Full Complexity of Retail Pricing

![](images/9bed049628e778da0ef95f3de0c11abd1b5a64099ae2d8fbc06bff53351523fc.jpg)

The dimensions of an AI-powered approach to pricing fall into three categories: strategic, hygienic, and dynamic. AI-powered solutions can iterate through billions of potential scenarios to find the optimal price for each store and item, considering all of these dimensions at once.

## Strategic Dimensions

This category focuses on the retailer's key objectives for pricing and on establishing how it will position and de-average prices relative to the competition. Here are the defining factors.

\- Objectives. Retailers need to define a clear ambition for their pricing strategy and translate that into specific commercial and customer objectives. A growing online retailer, for example, may want to maximize revenue first and foremost, while an established player might make gross profit its primary focus. Retailers also need to set overall constraints, such as minimum revenue and margin thresholds based on their broader business plan or minimum volume thresholds based on supplier agreements.

\- Category Roles and Key Value Items (KVIs). Retailers can harness the power of AI to optimize individual price decisions instead of focusing on average prices across their assortment. De-averaging their prices allows them to invest in the categories that drive customers to their stores and in the KVIs that have the strongest influence on value perception. Amidst high inflation in 2022, one large US retailer made targeted price reductions to its KVIs. The move contributed to a 10% improvement in customer value perception, which drove long-term market share.

\- Omnichannel Pricing. In an era when consumers can quickly compare prices across channels and competitors, retailers need to manage what consumers see and use these opportunities for comparison to their advantage. AI can help identify items that should have the same competitive price online and offline, as well as items for which they can differentiate prices by channel without hurting customer perception.

\- Price Zones. Advanced geoanalytics gives retailers the ability to determine consumer willingness to pay at the local level. One big retailer used hundreds of metrics to understand customer affluence and competitive intensity at each store. This let them set prices to reflect local market conditions.

## Hygienic Dimensions

Retailers can use AI to optimize prices under complex conditions, but its recommendations should be logical to consumers. Price hygiene has three factors that are critical to driving consumer trust and value perception.

\- Item Relationships. If retailers are using a category architecture such as good-better-best or larger pack sizes with better value per unit, they need to evaluate the price relationships among interdependent products. How prices compare to each other often matters more than the individual prices themselves.

\- Own Brand Versus National Brand. Retailers also need to optimize the price spread between national-brand products and their own branded items. The optimal price spread will be large enough to nudge consumers toward own-brand products but not so large that it erodes own-brand margins.

\- Rounding Rules. A retailer should offer clean and consistent prices that take advantage of “magic” price points and avoid crossing thresholds that would negatively influence value perception.

## Dynamic Dimensions

Retailers generally play what we refer to as the Uniform Game, in which they share value with consumers by offering uniform prices aimed at striking a balance between volume and margin. With AI-powered solutions, retailers can switch to the Dynamic Game and set prices by taking multiple dimensions into account simultaneously. Here are the key factors of dynamic pricing.

\- Real-Time Competitive Pricing. Tracking the prices of key competitors ensures an accurate and up-to-date view of the retailer's price position. This enables retailers to translate a desired level of competitiveness into actual price points that are de-averaged based on strategic dimensions. It also allows them to identify additional opportunities. When one grocery chain started to track competitors' prices systematically, it identified some situations where its own prices were 20% to 30% lower. By increasing prices to sit just below those of their main competitor, the retailer improved its margins with almost no impact on unit volume.

\- Dynamic Forecasting. Most retailers have estimates for price elasticities that allow them to forecast the impact of price changes. However, they typically use static elasticities, which prevents them from taking advantage of seemingly minor changes in customer behavior. Also, they often conflate base price elasticities with promotion elasticities and thus overestimate the impact of base price changes. Retailers can derive more accurate elasticities by using AI to gain insights from their vast transaction and loyalty data, as well from third-party sources such as weather data and competitive intelligence.

# The Enablers of AI-Powered Pricing

Implementing AI-powered pricing requires an aligned set of choices and an investment in teams, processes, and technology capabilities across the operating model.

Teams. Best-in-class retailers typically have a centralized pricing team or center of excellence that spans categories, regions, and channels. This team possesses the necessary strategic insight and data science capabilities to manage AI-powered pricing engines. It usually sits within the merchandising function to ensure alignment with other commercial levers such as promotions, vendor negotiations, and assortment. Sometimes the pricing team sits within marketing, IT, or data science (more common among retailers with highly dynamic pricing, such as online retailers).

The best practice is for the pricing team and merchants to set pricing strategy collaboratively, with the pricing team responsible for using AI-powered tools to optimize prices within that strategy and merchants providing final review and approval before execution.

Processes. AI changes not only the way retailers make decisions but also the quality and range of those decisions. The reset that most retailers do once or twice per year becomes a more strategic review with the ability to run price optimization scenarios based on richer inputs that reflect market dynamics. AI also allows retailers to monitor performance against strategy on a more frequent basis, identify deviations, and implement corrective price changes. This “read and react” process lets them quickly respond to competitor price moves, cost price inflation, or changes in customer behavior.

AI changes not only the way retailers make decisions but also the quality and range of those decisions.

Technology. An AI-powered optimization engine is underpinned by a fully integrated and automated data platform, which brings together strategic data assets such as customer loyalty data, competitor prices, and promotional and markdown plans. This platform enables the retailer to have near real-time updates from a single source of truth. User-friendly tools give decision makers access to the data easily in a standardized way. Custom user interfaces and reports, tailored to specific user profiles, open the “black box” by making reviews and intervention more efficient and by providing full transparency into the rationale behind any price recommendation. When integrated with upstream and downstream systems, the AI solution can also automate updates and price changes.

## How to Get Started

Retailers at the beginning of their AI adoption journey should answer several key questions to define the scope for a transformation:

\- Vision. What is your overall ambition for pricing, what is the value you can unlock, and how quickly do you want to achieve that?

\- Feasibility. What changes will be required to your current operating model across teams, processes, and technology? What is the corresponding level of investment?

\- Build, Buy, or Partner. Is an off-the-shelf tool sufficient, or will you benefit from a customized solution that's optimized for your unique data, processes, and market context? Do you have the right data science, engineering, and pricing expertise to build this capability internally, or do you need a partner to accelerate the journey?

Regardless of a retailer's current position, the increasing complexity and uncertainty of pricing is pushing existing approaches and technologies beyond their limits. Investments in AI capabilities are no longer just an option but a necessity. Retailers that build and successfully embed a cutting-edge, AI-powered pricing solution will realize significant benefits in operating efficiency, customer perception, and financial performance.

The authors wish to thank Laurence Heinrichs, Connie Gao, Shamel Merchant, and Shane Mono for their contributions.

## Authors

![](images/c889d518b6b099c5a4d8a2f59b246c833ef9bff51d79bd96d203182170cd7ddf.jpg)

![](images/c1c0b5b7e7fcfd47fda0f89daed87c5309e14f2a0ff2886ead0ba421e9bd5f94.jpg)

![](images/eea64bb20a7c96295775828b8a8ca18f84853b5d5791a302ac8b8af6635b7b9b.jpg)

## Javier Anta Callersten

Managing Director & Senior Partner
London

![](images/5de598ef7dadee0491bf101af7bf758fbf3d2bbc5537403b4ddd4a761a2cf0e8.jpg)

## Robert Xu

Managing Director & Partner,
BCG X
Dubai

![](images/6d0dfbd77464d6700b1b083d3e1d9beb446c542c19b02ffbfb5f488f31ede869.jpg)  
Scott Bradley

![](images/2dd24defa6f08c1da2ce8574a6953c93d1a21ede885b12c58f5b23e6b35f74eb.jpg)

Associate Director
London

![](images/ca57ecf03dfb8f36a570828d189923dd3e0e6ef4ad0c936dbfc5968e01d106f3.jpg)

## Sebastian Bak

![](images/ffb31b67d2b0670b3af1c03c300cf11fa9d8f62f9114039819dc5eda8b77691b.jpg)

![](images/b84486f25f6f23c51aeaf255b79edb8d27f4457cfc41f5555e35e93d0518608c.jpg)  
Managing Director & Partner; Marketing, Sales & Pricing Regional Practice Area Lead Los Angeles

## Roelant Kalthof

![](images/1d695152fae6ef5c9696ea8d11dfd224a1d064225fc80ec713d8f4eba4e87e75.jpg)

Managing Director & Partner
Silicon Valley - Bay Area

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
