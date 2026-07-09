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
# TO RESET OPERATIONS, GROCERS SHOULD START WITH THE CUSTOMER

By Simon Murphy, Robert Klingler, Gavin Parker, Pierre Mercier, Nathan Shenck, Maggie Orr, and Thomas Klinting

LIKE MANY RETAILERS, TRADITIONAL grocers see massive dislocations all around them—new competitive pressures, growing technological complexity, difficulties in the integration of online and offline operations, and the need to alter store formats to attract and retain customers. Recognizing these challenges, grocers are working hard to sustain and improve sales and margins.

They also know that they need to fundamentally transform their operations if they are to navigate through these dislocations. So far, however, many grocers have focused on incremental change within each function, while hesitating to make the bold moves essential for long-term success. Most are preoccupied with narrowly defined optimization projects within functional silos, such as supply chain, store labor, and waste reduction, rather than undertaking cross-functional and transformational projects.

Given the pace and magnitude of dislocations in the sector, fundamental change is necessary. Traditional grocers need to undergo a customer-centric transformation that resets their operating and service models, focusing on end-to-end (E2E) changes that deliver the right customer experience at the right cost. Such a reset of customer-centric operations typically enables companies to reduce their labor costs by an average of 5% to 10%, lower their inventory costs by 10% to 20%, and cut waste by 10% to 30%. Grocers that adopt this approach will improve their operating margins by 1% to 3%, which translates into billions of dollars sector-wide that they can reinvest in price, service, customer experience, and other competitive advantages that are critical to their survival.

## A Path to Transformational Change

Over most of the past decade, large grocery supermarkets—particularly those operating in developed markets—have suffered from stagnant topline sales growth and a steadily rising cost of doing business, resulting in disappointing profitability and shareholder returns.

We expect these trends to continue or even accelerate over the coming decade, given new competition from lower-cost competitors. Among these competitors are discount, club, and dollar stores, and disruptive players such as Amazon (with its foray into food sales) and Uber (with its Uber Eats online meal-ordering and delivery service). Emerging technologies may lead to further disruption in the way grocery stores operate and perhaps even in their value proposition. Moreover, customers' expectations continue to rise—both on their own and in response to these disruptive trends—forcing grocers to make costly changes to their operations in order to stay relevant.

In light of this unsettled environment and outlook, engineering the process to remove non-value-added tasks is a strategic imperative for all traditional grocery businesses. Such engineering will also provide the platform to drive additional fundamental change as emerging technologies become more mature and robust. Unfortunately, most traditional grocers find themselves ill equipped to tackle this challenge, for several reasons:

\- Many grocers tend to frame objectives with reference to productivity and cost takeout instead of meeting customers' needs and improving their experience.

\- The organizational structure of most grocers encourages optimization within functional silos. Often, grocers lack the governance structure necessary to make tradeoffs across functions to optimize processes end to end and to improve customer outcomes.

\- Many grocers fail to manage change effectively. They don't validate and refine solutions prior to rollout; and in rolling out change, they rely on simplistic central communications.

\- They struggle to make change stick in the long term. Few grocers have embedded new ways of working in daily store operations or created a continuous improvement mindset that empowers employees to own the change effort.

In responding to these challenges, grocers need to pursue difficult and ambitious goals, resetting the operating and service model to focus on E2E changes that provide the right customer experience at the right cost. Targeted improvement efforts—such as reducing total loss—can still generate significant value. But grocers can unlock substantially more value by integrating their business strategy and customer value more thoroughly than by addressing any one element independently.

Not only will these E2E process improvements free up resources for reinvestment in price and service, but they may also align the organization across functional areas to deliver customer value more consistently. To this end, some grocers already are pursuing a customer-centric operations reset. The approach comprises three critical strategic steps: identifying what customers truly value; reassessing and redesigning the E2E operating model; and making change stick.

## Identifying What Customers Truly Value

When grocers reset their operating processes, they need to make the customer the starting point. Before proceeding to any other step, the grocer must understand what the customer values and is willing to pay for and, ideally, how the grocer can differentiate itself and build loyalty.

It is important to avoid defining customer value too broadly or superficially. The definition must be sufficiently granular—by department or category—to be actionable and operational. For example, many retailers say that their customers prize “value” or “a high degree of choice.” But these concepts are too broad and vague to translate easily into concrete supportive action, and they are even less helpful when applied storewide.

In reality, customer expectations are not uniform across the entire store; rather, they differ by department, store area, and specific customer shopping mission. Understanding the differences can help grocers

focus their investments. For example, a gro-
cer might learn that customers of its in-
store bakeries prize “fresh out of the oven,”
with “the best crust,” and “from 7 a.m. to 7
p.m.” These are tangible goals that grocers
can tie to specific processes and actions.

## Reassessing and Redesigning the E2E Operating Model

After articulating the customer value proposition, the grocer must pursue E2E process excellence to consistently deliver the specified customer value. (See Exhibit 1.) This includes assessing all processes and departments in detail to identify current operating costs and cost drivers; establishing a baseline of current delivery-of-service levels and customer value; and then considering key cross-functional tradeoffs to better deliver value. Sometimes the goal may be to delight and attract customers (for example, by offering fresh-baked goods from 7 a.m. to 7 p.m.), and other times the focus may

be on eliminating waste and reinvesting the savings in the form of lower prices or improved service. To pursue E2E product excellence, grocers should adopt several key measures.

Set ambitious goals. To pursue and maintain E2E process excellence, leaders need to set ambitious top-down aspirations that drive employees to think big. We suggest that senior leaders set up a “shadow board” composed of high-performing individuals from each major function—for example, merchandising, space management, replenishment, logistics, and store operations. Leaders should empower this oversight board to approve solutions, manage tradeoffs, and spur healthy competition among different areas of the company to achieve ambitious goals.

For example, a leading European grocer implemented a customer-centric operations reset to reduce replenishment inefficiencies resulting from SKU proliferation that had increased search and handling times—and thus raised replenishment costs—along the entire supply chain. Because SKU proliferation had maxed out the grocer’s shelf space, introducing more replenishment-efficient merchandise was unduly difficult. To make matters worse, customers found the abundant product selection confusing rather than appealing.

EXHIBIT 1 | End-to-End Grocery Redesign Emphasizes Efficiency and Customer Value  
![](images/19189cbc299263830c8e8089d08c00c94632d8b0f9890cd4f678945dffa806b0.jpg)  
Source: BCG analysis.

To address these issues, the retailer created a cross-functional team and assigned it the task of conducting an E2E reset for all categories. The team reviewed the grocer's assortment strategy, streamlined the offerings, reduced the number of SKUs while selectively listing new products, established a better and clearer assortment structure based on customer needs and optimized planograms, and negotiated with suppliers. The team also improved the grocer's replenishment efficiency by, for example, using more shelf-friendly packaging, display pallets, or dollies. As a result of these changes, the retailer increased customer satisfaction scores, increased category sales by single digits, improved gross margins significantly, and reduced E2E operating cost from the distribution center to the store by double digits.

Embed lean principles. E2E process excellence requires embedding lean tools and principles of continuous improvement in day-to-day activities. These principles include relentlessly distinguishing between value-adding and non-value-adding activities (that is, waste), striving for standardization and consistent execution, and building a culture of continuous improvement by empowering employees and partners to identify problems and improve their work environments.

Tap emerging technologies. New technologies provide a means to redesign the operating model. Consider the checkout process. Many shoppers view this process, with its slow queues and manual scanning, as a major annoyance—and the checkout process often represents 30% or more of total store labor costs. New technologies are zeroing in on this non-value-adding

activity, making unattended checkout solutions available. But unattended checkout merely scratches the surface of potential technology-enabled solutions. Other possibilities include using in-store robotics for inventory management and customer service processes, introducing in-store replenishment systems, applying advanced analytics in automated replenishment systems, automating warehouse operations, and installing intelligent sensors.

Align mindsets and behaviors. In order for a complex change effort to succeed in the long term, a grocer must take concrete steps to align the organization's mindset and behaviors with the new goals. Examples include ensuring that the new processes become the standard way of working, confirming that day-to-day activities support the new processes, aligning governance and incentives with the new processes and goals, investing in training, and making sure that the management team is setting the right example.

Many grocers could improve their E2E processes by better aligning performance management systems across the enterprise. For example, one retailer rationalized its suite of scorecards from 20 to a single, shared scorecard containing five KPIs, thereby sharpening everyone's focus on enterprise-wide E2E goals.

## Making Change Stick

Even when grocers understand the specific actions they must take to simplify their operating or service model and to lock in ROI improvements, they may struggle to implement lasting change, given the multitude of tasks, the complications associated with staff turnover, and the complexity of distribution center and store networks. Nevertheless, companies that reset operations with a customer-centric mindset are in a better position to execute the redesign because they carefully test and refine new policies and procedures, create momentum, and scale up the change.

Many changes require a store-led approach, though others require either a category-led

## CASE STUDY Store-Led Change Management

For an example of store-led change management in action, consider the experience of a major grocery retailer. Customers were growing more and more dissatisfied with the quality and freshness of the grocer's products, contributing to stock losses of more than $25\%$ year-on-year. Senior leaders understood that curbing these losses was critical, but they struggled to effect change at individual stores.

To institute the necessary changes, the company decided to adopt a store-led change management program. The grocer began with a short, rigorous diagnostic to identify the root causes and scale of the problem. Next, it defined a few big solutions, piloted them in a single store, and then cascaded the initiative—first to 23 stores, then to 230, and onward. This rollout enabled the company to involve leadership teams across the network and rapidly test, refine, and validate solutions (which included ensuring that the solutions were scalable). Store teams then visited one of the pilot stores, and coaches helped individual stores embed the desired behaviors and new ways of working.

Using lessons from the initial store's rollout, the grocer developed a 12-week structured program, with fixed timelines specifying daily and weekly activities and multiple milestones to ensure progress.

or distribution-network-led approach. (See the sidebar.) The store-led change approach is most suitable for actions that must occur store-by-store—such as the inculcation of behavioral changes that are necessary for implementation of specific new store processes, or efforts to persuade employees at the individual stores to embrace broad change initiatives.

Using a single store to pilot a particular solution is an effective way to test and re-

The company fostered team engagement by framing the goals of the program as being to improve the freshness of products for customers and to make employees' work easier by simplifying and accelerating the markdown process. To encourage engagement, the stores created a community of change on Google+, celebrating successes and sharing tips and issues.

From the beginning, senior leaders also offered visible support to the stores. For example, the grocer determined in the initial diagnostic that stores were the root cause of about half of the quality and freshness problems, but that the other half originated in upstream areas. So the retailer's leadership announced forcefully and clearly that the initiative was a cross-functional effort and that upstream functions would support the in-store efforts.

After just one year, these store-led change efforts yielded significant improvements in the 300 stores that graduated from the grocer's 12-week program. Individual stores saw reductions in stock loss of $20\%$ to $50\%$ . Overall, the retailer cut losses by about $30\%$ , improved product freshness, and increased customer satisfaction. It also established a method for rolling out future operating changes.

fine the solution and demonstrate its value. For example, some grocers use rapid prototyping via “hothouses” or “the transparent store” to test and refine E2E optimization. This involves monitoring multiple variables, including sales, availability, hours, and product movement. Prototyping and mini-testing new processes in-store with clients and cross-functional teams can create a fast feedback loop that the grocer can use to fine-tune and quickly adapt the solution before undertaking broader testing.

Once perfected, a solution can move to several regional stores that serve as training facilities for an even wider rollout. (See Exhibit 2.) Representatives from other stores can visit these hubs, observe the changes first hand, and hear directly from their peers before implementing changes at their own stores.

Part of this training may include innovations such as advanced gamified simulation training, which differs from classroom training and traditional e-learning. (See Exhibit 3.) Grocers can tailor simulated training to their store format and value proposition, and create realistic in-store scenarios. This can help them roll out standards more consistently, measure results, and conduct appropriate follow-ups.

Making change stick for the long term depends on three additional elements:

\- A Structured Program. Grocers should break the process down into discrete, manageable tasks. By clearly defining goals and deadlines from the outset—ideally with specific actions for each

day or week—leaders can celebrate progress with their teams at regular intervals, building enthusiasm, instilling the right behaviors, and giving management a handy way to monitor progress.

\- Team Engagement. To build team engagement, grocers need to articulate the benefits of the change effort clearly and in ways that resonate well with their teams—for example, by detailing how customers will benefit and how their own work experience will improve. By encouraging friendly competition, leaders can build a community that supports and strives for change.

\- Visible Support. To convince employees that the change effort is a priority and not just a temporary productivity project that will soon fade in importance, leaders need to communicate its priority clearly, loudly, and often. They should also make clear that the reset is a team effort. This may entail explaining how, for instance, upstream functions will improve their processes while in-store teams improve theirs.

EXHIBIT 2 | A Structured Rollout of End-to-End Change Across a Store Network Occurs in Four Stages  
![](images/09ea440f0e7b5697a28e4c4fa951775e3ee7e73e69d4e65845297aea151ecaf4.jpg)  
Source: BCG analysis.  
Note: A zone is an area that consists of approximately five to eight groups of six to eight stores each. $^{1}$ The duration of the batch-by-batch rollout depends on the size of the store network.

EXHIBIT 3 | Gamified Training Maintains Employees' Interest and Improves Information Retention

# WHAT GAMIFIED TRAINING LOOKS LIKE

![](images/365340ef8448c7f52108ad7505150c7e52b65bb9c822c1fb224ef36e2470d719.jpg)  
Source: Attensi.

MANY GROCERS ARE planning to move beyond the narrowly defined optimization projects of the past to attempt more ambitious E2E projects for fundamental, cross-functional change. Admittedly, these projects are complex, and companies in the past have often been frustrated in their efforts to complete them successfully. But

some leading companies are finding success by pursuing a customer-centric operations reset. By focusing on the customer, implementing E2E optimization, and taking steps to make change stick, these companies are successfully aligning a customer-centric strategy with day-to-day activities while upgrading productivity.

## About the Authors

Simon Murphy is a partner and managing director in the Sydney office of The Boston Consulting Group. He is the topic leader for retail operations transformations in Asia-Pacific. You may contact him at murphy.simon@bcg.com.

Robert Klingler is a director in the firm's Cologne office. He is the leader for the retail operations topic area in the Central and Eastern Europe, Middle East, and Africa region. You may contact him at klingler.robert@bcg.com.

Gavin Parker is a partner and managing director in BCG's Melbourne office. He leads the firm's global work in retail transformation and reinvention. You may contact him by email at parker.gavin@bcg.com.

Pierre Mercier is a partner and managing director in the firm's London office. He is the global leader for the retail supply chain topic area. You may contact him by email at mercier.pierre@bcg.com.

Nathan Shenck is a partner and managing director in BCG's Washington, DC office. He is the topic leader for retail store labor optimization. You may contact him at shenck.nathan@bcg.com.

Maggie Orr is a principal in the firm's Boston office. You may contact her at orr.maggie@bcg.com.

Thomas Klinting is a principal in BCG's Sydney office. You may contact him at klinting.thomas@bcg.com.

The Boston Consulting Group (BCG) is a global management consulting firm and the world's leading advisor on business strategy. We partner with clients from the private, public, and not-for-profit sectors in all regions to identify their highest-value opportunities, address their most critical challenges, and transform their enterprises. Our customized approach combines deep insight into the dynamics of companies and markets with close collaboration at all levels of the client organization. This ensures that our clients achieve sustainable competitive advantage, build more capable organizations, and secure lasting results. Founded in 1963, BCG is a private company with offices in more than 90 cities in 50 countries. For more information, please visit bcg.com.

© The Boston Consulting Group, Inc. 2018. All rights reserved. 4/18
"""
