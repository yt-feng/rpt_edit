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
# IT'S TIME FOR GROCERY RETAILERS TO SIMPLIFY

By Sandeep Chugani, Aftab Hussain, Travis Jackson, Greg Curreri, Jill Wang, and Peter Tilton

THE GROCERY INDUSTRY HAS been significantly disrupted by the speed and scale of COVID-19. Since the onset of the pandemic, customers and retailers alike have faced the challenges of empty shelves, social distancing, face masks, rising costs, and overwhelmed supply chains. But times of crisis and uncertainty are often the best times to discover better ways to do business.

Reducing a store's product range to simplify operations and stock the products that are most in demand has been a pivotal measure in helping traditional retailers manage during the height of the crisis. As middle-market grocery retailers emerge from the unprecedented strain of COVID-19 on their businesses, offer simplification will be an essential strategy for improving both the customer experience and operational efficiencies.

A Turning Point for Simplification
Long before the COVID-19 crisis hit, traditional middle-market chains have been

struggling with the climbing costs and complexity produced by unprecedented product proliferation. This trend has created larger stores stocked with 80% more SKUs on average than a typical store would have offered 30 years ago. Although customers may appreciate having more choice, they also value the ability to easily and quickly find what they want—an experience that has been lost as more products appear on shelves.

Product proliferation has also become a competitive disadvantage for such retailers. BCG research conducted in 2020 shows that regional US grocery chains carry an average of 50% more SKUs per linear foot of shelf space than their mass and value channel competitors. And they have been losing market share to value-priced wholesale clubs and mass retailers—and even small, no-frills convenience stores, which are more expensive but provide a much faster, easier shopping experience.

Many grocers have resisted offer simplification because they mistakenly believe that removing products from the shelf hurts sales. Our work proves this is not the case. We recently led an offer simplification trial where our client reduced 20% to 25% of SKUs across 30 categories. Sales across the impacted categories increased by 2%.

But the benefits of offer simplification go much further than increasing sales. Simplification can create a virtuous cycle that scales end-to-end (E2E) efficiencies from the warehouse to the grocery cart. Handling fewer products frees up space in warehouses to store products in ways that streamline the supply chain. Relationships with suppliers improve. And customers find the products they want.

## The Costs of Variety

There is a fine line between just enough variety and too much duplication and complexity. On the one hand, variety is key to a successful retail grocery business. Offers that appeal to different customer tastes are important, especially in high-innovation categories such as salty snacks and frozen meals. Variety can also stimulate impulse buying. On the other hand, in most commoditized categories, such as vitamins, frozen vegetables, and canned soup, too much variety overwhelms customers.

Over the years, numerous consumer psychology studies have pointed to a phenomenon known as “decision paralysis,” or “choice overload”—that is, when customers have too many choices, it feels harder to decide what to purchase and diminishes the retail experience. According to a 2020 National Retail Federation customer survey, 63% of respondents said that “convenience” is important to them—and 47% included “making it easy to find options” as part of their definition of convenience.

Looking beyond the customer experience, the costs of product proliferation affect multiple facets of a traditional retailer's operations:

\- Stocking. Too many products on the shelf means that grocers have less space for staples that drive sales and for the

unique products that increase customer loyalty. In addition, undue variety requires complex inventory processes that can increase out-of-stocks of the products customers depend on. Both crowded and empty shelves frustrate shoppers. This is a hazard for traditional retailers because it has the potential to drive their customers to competitors.

\- Merchandising. Consumer packaged goods companies provide funding incentives (including new-item slotting fees) to make sure their products are kept on the shelf. But under these arrangements, retailers yield too much control over merchandising decisions to suppliers. Their own teams have less power to craft offers that are of most value to customers.

\- Purchasing. Too much variety and too many new products reduce grocers' ability to consolidate their purchasing power to obtain the best costs. This puts them in a difficult spot. They can either compete with value and mass stores on price, but at the expense of margins, or they can maintain margins at the expense of customer transactions and traffic.

\- Store Operations. The growing number of SKUs increases the time needed to restock shelves, manage backroom inventory, change price tags, and reorder products—all of which drive up labor costs. The new COVID-19 health, sanitation, and safety measures have added further cost burdens.

\- Supply Chain. With more SKUs moving through distribution centers, supply chains are operating at near full capacity. Unpredictable demand surges related to the pandemic will continue to strain supply chains and increase the risk of product shortages.

## The Benefits of Simplicity

The current health crisis underscores the benefits of adopting a strategy of offer simplification. The benefits we have seen

among grocery retailers that were pursuing offer simplification before the pandemic will become even more compelling as they adjust to the changed landscape of a post-COVID-19 world.

Consider the following operational improvements offer simplification can deliver:

\- Optimized SKUs That Benefit Stores and Customers. Thoughtfully pruning SKUs allows merchandisers to balance top-selling and unique items in their offer and remove duplications that drive neither sales nor customer loyalty. Fewer products on the shelf makes shopping easier and more pleasant for customers and will reduce out-of-stocks for key products.

\- Reduced Costs in the Supply Chain. Simplification reduces carrying costs as less cash is tied up in obsolete inventory. It also opens up warehouse space so similar products can be stored together, reducing load times for trucks delivering to stores. Longer term, capex allocations for network expansion can be deferred or saved as simplification eases capacity constraints.

\- Increased Efficiencies in Store Operations. Fewer SKUs and less backroom inventory will reduce the hours store associates spend repricing items and restocking and replenishing shelves. This gives them more time to serve customers and, during the pandemic, to perform COVID-19-related sanitization procedures.

\- More Productive Vendor Relationships. Because grocers associate variety with vendor funding, they often believe that they will lose these funding premiums if they take products off the shelf. As we noted earlier, after our work on offer simplification, our client saw a net increase in vendor funding. Using analytics to simplify and concentrate marketing spending on the most popular core items strengthens the partnership between retailers and their suppliers.

## The Right Way to Start Offer Simplification

Whether you have already embarked on a SKU rationalization initiative or are re-thinking how to simplify your offer in light of COVID-19, there are a number of traps that could undercut the initiative. To maximize the effectiveness, we suggest applying three perspectives when starting a simplification initiative.

The Customer. Many grocers frame objectives for process improvements around productivity and cost, rather than putting customer needs first. Every offer simplification needs to begin with an open conversation about the customer experience that is supported by deep analytics.

All merchandisers should be making their category and planogram decisions based on a robust consumer decision tree. A CDT shows the key attributes, and combinations of attributes, that are important to customers when they are deciding what products to purchase. (See the exhibit, a CDT analysis we did for a client.)

Customer data from a CDT, along with other loyalty and preference data, enables retailers to maintain a comprehensive offering, avoiding decisions that end up removing high-loyalty products—or eliminating new items before they can gain traction with customers. Customer loyalty data will also highlight low-volume SKUs that retailers need to keep because they're important to specific customer groups.

Customer data captured from deep analytics and loyalty metrics will form the basis for designing the offer; an offer simplification trial will validate the customer analytics and metrics.

The Offer. Demand-driven assortment strategies are based on learning as much as possible about customer purchasing behaviors as well as comprehensive analysis of costs of buying, distributing, and stocking different products. Retailers make fully informed decisions by assessing their current offering against a CDT analysis and loyalty data by SKU and comparing relative

A Canned Soup Category Customer Decision Tree  
![](images/8abaa9ae856f8d88aa1661479fc4fabbcf40e52615dd39dcd4289f60a1b6dc58.jpg)  
Note: OB = own brand; NB = national brand; index calculated as company total SKUs vs. next highest or vs. average for traditional grocers.

E2E margins. Failing to consider E2E cost implications can lead to the removal of high-margin items. In addition, grocers need to thoughtfully consider the customer experience when making merchandising decisions. If the data suggests cutting nine out of ten SKUs of a brand in a category (which will look odd on the shelf), it makes more sense to remove them all.

Simplification does not mean standardization. Grocers need to work with their merchandise teams to maintain a product lineup that satisfies regional and local customer tastes. Every simplified offer initiative needs to be tested before it is rolled out to all stores. Thorough testing will balance statistically significant insights and practical observations, and include a regional trial.

Suppliers. Relying on suppliers' data alone to make decisions shifts the focus from customers to vendors. With offer simplification, retailers can regain control of mer-

chandising decisions, including more customer-driven placement of suppliers' products and greater emphasis on the placement of a retailer's private label brands.

We encourage discussing simplification plans with suppliers and sharing performance data from test stores. This will give suppliers insight into what customers are buying and how they can best support an offer.

## A Post-COVID-19 Grocery Transformation

As the world adjusts to the new realities of living with COVID-19, offer simplification should be at the forefront of every retail grocery leader's mind. People's habits, including their grocery shopping routines, have changed almost overnight—and they are unlikely to revert to what they were before the virus struck. Economic burdens caused by the pandemic will only heighten customer focus on price and convenience. This will ramp up pressure on grocers already competing with value and mass retailers. At the same time, costs related to regulations around store cleanliness will continue to eat into retailers' narrow margins.

In light of these realities, offer simplification is an especially compelling opportunity to launch a cross-functional and transformational initiative. Indeed, grocers must make improvements across the value chain to compete successfully in a rapidly evolving market.

## About the Authors

Sandeep Chugani is a managing director and senior partner in the Miami office of Boston Consulting Group and the global leader of BCG TURN and Transformation. You may contact him by email at chugani.sandeep@bcg.com.

Aftab Hussain is a managing director and senior partner in the firm's New Jersey office. You may contact him by email at hussain.aftab@bcg.com.

Travis Jackson is a managing director and partner in BCG's New Jersey office. You may contact him by email at jackson.travis@bcg.com.

Greg Curreri is a principal in the firm's Miami office. You may contact him by email at curreri.greg@bcg.com.

Jill Wang is a project leader in BCG's New Jersey office. You may contact her by email at wang.jill@bcg.com.

Peter Tilton is a project leader in the firm's New Jersey office. You may contact him by email at tilton. peter@bcg.com.

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

## © Boston Consulting Group 2020. All rights reserved. 8/20

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and Twitter.
"""
