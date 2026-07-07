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
THE BOSTON CONSULTING GROUP

# Omnichannel Alchemy

Turning Online Grocery Sales to Gold

![](images/feb8b3b221d0b5323d9f99d779da0e54d73204d8a3ef7f20e456a8eb511cd79e.jpg)

1710

The Boston Consulting Group (BCG) is a global management consulting firm and the world's leading advisor on business strategy. We partner with clients from the private, public, and not-for-profit sectors in all regions to identify their highest-value opportunities, address their most critical challenges, and transform their enterprises. Our customized approach combines deep insight into the dynamics of companies and markets with close collaboration at all levels of the client organization. This ensures that our clients achieve sustainable competitive advantage, build more capable organizations, and secure lasting results. Founded in 1963, BCG is a private company with 78 offices in 43 countries. For more information, please visit bcg.com.

# Omnichannel Alchemy

Turning Online Grocery Sales to Gold

## AT A GLANCE

Consumer demand for online grocery shopping is fueling a market that is expected to grow to \$100 billion by 2018. We believe that establishing profitable online operations is not only possible but essential for grocers that want to continue to grow and maintain market leadership. Early movers will gain a significant competitive advantage over those that come late to the market.

## DON'T WAIT

Seize the opportunity now to lock in core customers and drive share.

## AVOID THE COSTLY LAST MILE

Start out with the “click and collect” model and add home delivery in selected areas only after sufficient local scale has been achieved.

## TARGET AFFORDABLE DIFFERENTIATION

Invest in the drivers of online satisfaction; monitor the economics of execution.

## EVOLVE AND ADAPT

Any model will need to evolve over time as the market and customer base—and a grocer’s own capabilities—develop. Create a realistic timetable and return targets.

A SK MOST INDUSTRY EXECUTIVES about the prospects for online grocery shopping, and you'll encounter hesitancy, if not skepticism. Ask consumers—especially younger, more affluent consumers and families—and they'll tell you that they are excited by the idea. They wonder why the industry has been slow to deliver.

Online grocery shopping has yet to take off in most countries for many reasons—cost, logistical complexity, and the prospects for profitability key among them. There’s also the fact that many of the business’s early pioneers went bust.

We believe that the prevailing doubtful view is about to hit its expiration date. We expect the global online grocery market to reach \$100 billion by 2018. (See Exhibit 1.) Based on new consumer research in eight countries, as well as on our experience with leading companies around the world, we also believe that establishing profitable online grocery operations is not only possible, it is

EXHIBIT 1 | The Market for Online Grocery Shopping Is Expected to Reach \$100 Billion by 2018 essential for those that want to continue to grow and maintain market leadership. $^{1}$ Early movers will seize a significant competitive advantage over those that come late to the game.

![](images/89f205a207032693eeabd1844e1824c1e45f1631542d325149b9774286a66248.jpg)

Skeptics will point to the early failures and the fact that even today plenty of players still struggle to hit volume and profitability targets. High costs for delivery and the picking and packing of orders, combined with the need for flawless execution to keep customers coming back, make the online game challenging, to say the least. Cannibalization and different ways of accounting for costs complicate fair comparisons. Still, we believe that grocers in most markets can establish profitable, substantial online businesses with positive returns on investment and healthy margins within a period of a few years. Companies as diverse as Tesco and Fresh Direct have done it. And even if a grocer does not believe that it can drive incremental profits through an online service, it nonetheless needs to act or risk losing out in a race for omnichannel sales.

Grocers are pursuing a broad range of models and approaches, but we have identified four fundamental imperatives for building a successful online grocery business. This game plan can be applied to most markets and company circumstances:

\- Don't wait. Seize the opportunity now to lock in core customers and drive share.

\- Avoid the costly last mile. Start out with the “click and collect” model, in which a customer chooses goods online and then picks them up at a store or a dedicated facility, and add home delivery in selected areas only after sufficient local scale has been achieved.

\- Target affordable differentiation. Invest in the drivers of online satisfaction. Focus on the elements of the customer value proposition that will attract and retain shoppers while keeping a careful eye on the economics of execution.

\- Evolve and adapt. Whatever model a grocer begins with will need to evolve over time as the market and customer base—and the company’s own capabilities—develop. Plan a journey with a realistic timetable and return targets.

## Don't Wait

Our research indicates that there's plenty of pent-up demand in major markets, even after factoring in the tendency of respondents in surveys such as this one to overstate demand.

Consumers in the countries we surveyed said that they would expect to use an online grocery service offering either a click-and-collect option or home delivery an average of 13.5 times a year—more than once a month. In some markets, such as Brazil and China, consumers would shop for groceries online nearly twice a month. In the United States, approximately half of the respondents said that they would try home delivery or a click-and-collect service. Our research also shows that grocers' most important customers—young families and affluent couples—are especially

EXHIBIT 2 | Significant Pent-Up Demand Exists for Online Grocery Shopping
Expected online grocery demand in 2013 by...  
![](images/0475b6fc0940af6930c12e7a0ae80cc87d86b0b94767d58b4600c1648ab99e3f.jpg)

![](images/2c649b50893d7996d5fde55d8d657db093ec63ee94de45f011b7292c9612492e.jpg)

![](images/3ef477a768733d843e9bcf1d23739ed13103a9c8b6eb62f70f8592ee729770a5.jpg)  
Source: BCG online grocery survey of 4,325 participants conducted in April 2013.  
Source: BCG online grocery survey of 4,325 participants conducted in April 2013.

Note: The survey questions were, “If you were doing your main groceries shopping online, which of the following delivery options would you consider?” and “For online [home delivery/click-and-collect], how frequently do you think you would use this service?” $^{1}$ Frequency of visits determined by survey respondents’ stated willingness to shop online. $^{2}$ Represents only respondents who don’t yet shop online for groceries.  
$^{3}$ Low income was defined as the bottom 25 percent of household income distribution; high income was defined as the top 25 percent of household income distribution.

ready to take advantage of online grocery shopping. (See Exhibit 2.) And when they do move online, they are likely to spend far more across all channels than they would have done by shopping only in the traditional way—the uplift often ranges from 30 to 50 percent.

The difference in penetration rates among markets is much more about supply than demand. Any market in which two or three grocers engage in an online fight for customers sees a substantial rise in online penetration as the competing companies invest in building and marketing their offers. Online grocery shopping has already reached a substantial size in several countries: 5 percent of the total grocery market in the U.K., for example, 3 percent in France, and 4 percent in South Korea. The online share of grocery shopping is growing at rates of 20 to 50 percent per year in leading markets and should double in many markets by 2016. The difference between the leaders and the countries in which online grocery shopping has yet to establish a significant presence has a lot more to do with the reluctance of retailers than the desires of consumers.

Big players in countries with developed online markets, such as Tesco in the U.K., already attribute a substantial proportion of their overall grocery sales to online purchasing—8 percent in Tesco's case. An even higher percentage of these companies' yearly growth is driven by online sales. In large and competitive grocery markets, such as the U.S. and Germany, the competition for share is intense and becoming more so, thus limiting the ability to grow by adding stores. Moreover, in most instances, an online grocery operation is a much lower-cost growth option, and it can help grocers address current drivers of dissatisfaction among customers, such as the lack of assistance with carrying packed bags and boxes to their cars.

Even so, many grocers are taking a wait-and-see approach to moving online, and they are doing so for three key reasons: cost, cannibalization, and complacency. Companies and markets vary, of course, but we believe that in countries with widespread Internet access and fast-rising mobile penetration, the viability of online grocery shopping is a question of how soon rather than if. The advantages of moving early outweigh those of waiting to see what happens.

Cost. In the decade or so since the first pioneers tried to make online grocery shopping work, costs have come down. New models, such as a click-and-collect service, are cheaper to operate at low volumes. Technology has advanced significantly; efficient automated picking systems enable some dedicated fulfillment centers to operate at a cost well below 10 percent of sales—and a few approach 5 percent. Better routing and delivery software has resulted in fuel savings and optimal fleet utilization, lowering delivery costs. At the same time, consumers are growing more accustomed to shopping online, websites and mobile applications are easier to use, and online payments are more secure.

Cannibalization. Our experience has shown that fears of cannibalization are overstated. Indeed, the dynamics of online marketing allow first movers to increase share aggressively, develop customer loyalty, and lock in the most attractive customer segments. Moreover, early movers climb the learning curve ahead of the pack, building scale and improving service, operations, and marketing. The experience of companies such as Tesco, LeShop, and Fresh Direct demonstrate that online operations can achieve profitability relatively quickly while establishing strong market positions. On the other hand, companies that allow competitors to establish an unchallenged online service risk losing customers—perhaps permanently.

Complacency. A false sense of security about the strength of a company's current position in the market can lead to underestimating the threats from both traditional and nontraditional competitors. Many traditional grocers are testing online grocery shopping through trials in almost all major markets. There are also a host of mounting threats, including:

\- Nontraditional competitors, including e-retailers such as Ocado and Fresh Direct.

\- Online marketplaces, such as Amazon.com and Soap.com, that sell ambient, or nonperishable, goods. Amazon.com recently expanded its fresh-food offering to Los Angeles from its original trial city of Seattle.

\- Over-the-border competitors, such as Peapod, owned by Ahold of the Netherlands, which has introduced a mobile shopping service for rail commuters in

Philadelphia. Customers use their smartphones to scan product codes on train station billboards and have the groceries delivered to their homes later that day.

\- Consumer goods companies looking to sell directly through various online channels, which can include third parties such as Amazon.com; their own online stores—P&G eStore, for example; or potentially their own click-and-collect types of service. We are already seeing more expensive, higher-margin, long-tail ambient goods going online through online marketplaces.

## Avoid the Costly Last Mile

As BCG has observed before, click-and-collect services are gaining popularity in many markets, particularly where home delivery is problematic. (See “Digital’s Disruption of Consumer Goods and Retail,” BCG article, November 2012.) Major grocers in France, the largest market for click-and-collect services, have established more than 2,000 such physical sites, many operated as drive-throughs. (See the sidebar “Click-and-Collect Services Gain Favor in France.”) These sites have fueled online-sales growth of 50 percent per year for the past several years. Groupe

## CLICK-AND-COLLECT SERVICES GAIN FAVOR IN FRANCE

In the French online grocery market, as in many others, the early pioneers stumbled—in large part because of the high costs of home delivery.

In 2004, Groupe Auchan and Système U piloted the click-and-collect concept, known in France as “the drive”; in fact, Intermarché has branded its service “Le Drive.” Auchan rolled it out across France later that year. E-retailer Chronodrive was founded in the same year and operates a system using regional-warehouse picking and packing and designated customer pickup points. French grocers were quick to respond; the click-and-collect model was adapted by many others, although companies continue to experiment with different forms of the collection half of the equation.

The online grocery market grew at about 30 percent per year until 2008 when, thanks to aggressive competition from new entrants, the overall growth rate accelerated to 50 percent per year from 2008 to 2013. In 2012, the online grocery market represented 2.9 percent of the total French grocery market. It is projected to reach €3 billion to €3.5 billion in 2013, and forecasts show that it will grow to about 7 percent of the total grocery market by 2016. Home delivery is not yet a factor. French grocers also are taking the click-and-collect concept to other countries, including Auchan in China and Carrefour in Indonesia.

The question of which will be the winning collection model—pickup points in or near stores or freestanding dedicated facilities—remains unanswered. There is a strong argument that dedicated facilities reduce the risk of substantial cannibalization of existing stores.

Auchan offers an innovative combination model based on a dedicated facility that allows customers to shop for fresh goods when they pick up their online orders. Asda, the number-two U.K. grocer by size, is investing £700 million in 2013, much of it in the company's online operation, and plans to offer a same-day click-and-collect service, a first for the U.K. market.

It is especially important for new entrants to select one delivery channel, or one channel in each region of operation, so they can build volume quickly without fragmenting sales between click-and-collect services and home delivery. We believe that the click-and-collect model is the best for markets in which home delivery has yet to be established. Our research shows that customers in most markets consider the service attractive and are willing to drive up to 13 minutes, on average, to pick up an order—a figure that was remarkably consistent across the eight countries we surveyed. Our research also indicates that consumers are not willing to pay delivery fees that are high enough to cover the last-mile cost of a new entrant. In the U.S., for example, consumers are willing to pay from \$5 to \$10 per delivery, while our models show that the actual cost to grocers can run as high as \$20 per delivery in low-penetration areas.

In part for historical reasons, the U.K. has become the leading home-delivery market. Some innovative companies in other countries, such as Fresh Direct in the U.S. and LeShop in Switzerland, are also demonstrating success. But they are doing so in markets with high gross margins and particular characteristics: densely populated, supermarket-unfriendly New York City, for example, or Switzerland, where supermarkets' hours of operation are often restricted by law. These companies have built scale quickly, and they employ innovative models. Like many successful companies, they also offer short delivery windows of an hour or two—one of the most important considerations for consumers. We expect to see more innovation in delivery models in the near future. For example, some companies have started to combine multiple deliveries in locations convenient for both the grocer and its customers, such as office buildings, to help reduce last-mile costs.

Fresh Direct has hundreds of thousands of customers and delivers fresh, high-quality foods and grocery items to homes and offices in the New York City and Philadelphia metropolitan areas. The company is profitable, generating revenues of \$400 million in 2012. LeShop offers a full range of products from Migros, Switzerland's biggest supermarket chain, and uses the Swiss post-office fleet during downtimes—from approximately 6:00 p.m. to 8:00 p.m. on weekdays and 7:00 a.m. to 1:00 p.m. on Saturdays—to handle deliveries. The company has developed special packaging that helps keep fresh and frozen foods cool to allow for delivery when no one is home.

Home delivery will continue to develop as major players experiment with new models. Google is testing same-day home delivery of groceries with various partners in the San Francisco Bay area in the U.S. Executives of Wal-Mart Stores have said that a crowdsourced solution may be possible within a year or two, with customers taking on the task of delivering to others in return for a discount. In the near to medium term, however, grocers in most markets are likely to pursue the click-and-collect model.

## Target Affordable Differentiation

Succeeding in the online world takes more than a website with a mobile app and a fulfillment facility. It is critical to understand what elements are really important to customers and how you can differentiate your services from the competition without straining your economics. Customers tend to be even more demanding online than in the store. Our research shows that customers in two of the most developed online grocery markets, the U.K. and France, look for grocers to meet four basic expectations: the right range and quality of products; consistent delivery of the expected basket of goods, with low rates of substitution and high levels of freshness; punctual delivery in convenient time slots; and ease of use of the service, especially on the website. (See Exhibit 3.) One key for success is satisfying these drivers of demand on a continui

[中间内容因长度限制已省略]

d markets. (See the sidebar “The Big Opportunity in the Nascent U.S. Market.”)

GROCERY STORES AREN'T going away. Consumers around the world like them, and grocers do a good job of meeting customer demand and expectations. But the rise of omnichannel retailing—the interaction of consumers and retailers anytime, anywhere, on any kind of digital device—is the most significant and far-reaching development shaping the retail industry today. Grocers will not be spared its impact.

Successful companies have already shown how to harness this trend to their advantage. The experience of grocers in countries such as the U.K. and France demonstrates that even in their youthful days, online markets can quickly become highly competitive. The question for major players in nascent markets is whether they want to leverage their existing assets now to establish strong and defensible online businesses or wait until the market develops and they have to claw back share from others—when they are already behind the online curve.

## NOTE

# THE BIG OPPORTUNITY IN THE NASCENT U.S. MARKET

The United States is the world's largest e-commerce market, and it is still growing fast: spending is expected to rise by more than 13 percent to some \$260 billion in 2013, according to Forrester Research. Online grocery shopping, however, remains an exception: penetration in the U.S. trails that of many other countries.

Few of the large players in the U.S. have established online operations, but notable exceptions include Peapod, which is owned by the Dutch company Ahold, and Safeway. Some niche players have also established profitable businesses; the best known is probably Fresh Direct in and around New York City and Philadelphia.

This situation could be ripe for change. BCG research shows substantial pent-up demand—more than 40 percent of U.S. consumers want to do more online grocery shopping. At the same time, large players are experimenting with different online formats. Two of the biggest, Wal-Mart Stores and Amazon.com, have sufficient scale to transform the market.

Wal-Mart is testing multiple online business models through trials, including same-day and next-day delivery of online groceries and general merchandise in the San Francisco Bay area.

Amazon.com, under its Subscribe & Save program, will deliver a standing order of consumer staples at regular, customer-specified intervals. The company recently expanded its AmazonFresh grocery-delivery service to parts of Los Angeles, where it offers same-day delivery on orders of \$35 or more. Customers can choose from more than 500,000 items. Amazon.com is also testing delivery from centralized distribution facilities to “parcel lockers”—temporary storage facilities for nonperishable goods in convenient locations where individual online orders are held for pickup. The company piloted the concept in New York, Seattle, and London and has now expanded to additional markets. BCG estimates that parcel lockers can reduce the cost of delivery by as much as 30 to 40 percent compared with direct delivery to the home.

Ahold has moved beyond home delivery and is now offering a store-based click-and-collect service that allows customers to order online at Peapod.com and then collect their groceries at selected Stop & Shop stores.

The prize is substantial. Applying current U.K. penetration growth and penetration rates to the U.S. indicates a market potential of more than \$24 billion in a few years' time. While home delivery is likely to be profitable only in the densest cities, we are convinced that the click-and-collect service can be profitable across the U.S. With the right model, we believe that early movers can achieve an attractive profit margin within about five years after startup.

## About the Authors

Chris Biggs is a partner and managing director in the London office of The Boston Consulting Group and the leader of the omnichannel retail topic. You may contact him by e-mail at biggs.chris@bcg.com.

Julian Suhren is a project leader in the firm's London office. You may contact him by e-mail at suhren.julian@bcg.com.

## Acknowledgments

The authors are grateful to Olivier Abtan, Patrick Ducasse, Thor Jorgensen, and Pedro Yip for their input into this report. They would like to acknowledge Frederick Boels, Alla Dubrovina, Quentin Philippe, and Robert Xu for their assistance. They would also like to thank David Duffy for his help in writing the report and Katherine Andrews, Gary Callahan, Lisa Clark, Lilith Fondulas, Kim Friedman, Kim Plough, and Sara Strassenreiter for assistance with editing, design, production, and distribution.

## For Further Contact

If you would like to discuss this publication, please contact one of the authors.

To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcgperspectives.com.

Follow bcg.perspectives on Facebook and Twitter.

## BCG

## THE BOSTON CONSULTING GROUP

Abu Dhabi

Chennai

Amsterdam

Chicago

Athens

Johannesburg

Cologne

Kiev

Munich

Nagoya

Atlanta

Seoul

Kuala Lumpur

Copenhagen

Shanghai

New Delhi

Auckland

Dallas

Lisbon

Singapore

New Jersey

Bangkok

London

Detroit

Stockholm

New York

Barcelona

Dubai

Stuttgart

Los Angeles

Oslo

Beijing

Sydney

Madrid

Düsseldorf

Paris

Berlin

Taipei

Melbourne

Perth

Frankfurt

Tel Aviv

Bogotá

Mexico City

Philadelphia

Tokyo

Geneva

Miami

Prague

Toronto

Boston

Hamburg

Rio de Janeiro

Milan

Vienna

Brussels

Helsinki

Minneapolis

Rome

Warsaw

Budapest

Hong Kong

Monterrey

San Francisco

Washington

Buenos Aires

Houston

Montréal

Santiago

Zurich

Canberra

Istanbul

Moscow

São Paulo

Casablanca

Jakarta

Mumbai

Seattle

bcg.com
"""
