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
# HELP YOUR SHELF

# THE MOVES MAINSTREAM GROCERS MUST MAKE NOW

By Gavin Parker, Thomas Jensen, Lodewijk van Meeuwen, Bill Urda, and Kate Cormack

N MARKET AFTER MARKET worldwide, an increasingly popular breed of retailers is proving an old credo wrong. Stores such as Aldi, Lidl, Trader Joe's, and Mercadona, which offer more targeted assortments than traditional grocers do, are showing that shoppers don't have to choose between value and quality.

Mainstream grocers need a fresh approach to serving customers and running their businesses—an approach that goes beyond tactical bottom-up moves at the store level. (See “Succeeding with a Store-Led Strategy,” BCG article, September 2014.) They have long positioned themselves as champions of assortment and value as well as beacons of quality. But they have been finding it increasingly difficult to settle on the right positioning (and to drive top-and bottom-line growth). That’s because the needs and behaviors of shoppers have been shifting—and because the targeted assortment stores have recognized and responded to those shifts more quickly, upsetting the economics of the grocery trade in the process. (See the exhibit, “Hard

Numbers That Should Rattle Traditional Grocers.")

These days, far fewer families shop for what they'll need next month. Instead, they take shorter, more frequent shopping trips, increasingly to smaller stores nearby that are easier to get in to and out of than the larger-format supermarkets and hyper-markets that, in the 1980s and 1990s, held the high ground on price and selection. Online retail further undercuts the “one-stop shopping” advantage and is well-suited to today's consumers.

The relative newcomers in the grocery industry—firmly established in Europe and rapidly making inroads in the US, Australia, and elsewhere—were quick to seize the opportunity. With their smaller footprints, superior value, and steady additions of fresh and appealing products, they have won over more and more mainstream shoppers—and they’re keeping them. Why shop elsewhere when you can get almost everything on your list for 20% less and navigate the store more quickly?

Hard Numbers That Should Rattle Traditional Grocers

<table><tr><td></td><td>Mainstream supermarket</td><td>Targeted assortment store</td><td></td></tr><tr><td>Store footprint</td><td>2,500–5,000  $m^{2}$ </td><td>1,000–1,800  $m^{2}$ </td><td>Easier in-and-out means faster shopping. The targeted assortment stores decide the number of SKUs to be stocked and the size and locations of their stores on the basis of their understanding of customers&#x27; needs and buying habits.</td></tr><tr><td>Number of SKUs</td><td>16,000–18,000</td><td>3,000–4,000</td><td>The majority of today&#x27;s shoppers are satisfied with a smaller selection of products.</td></tr><tr><td>Labor cost as a % of cost of sale</td><td>9%–12%</td><td>4% –5.5%</td><td>Far fewer staff are needed per store.</td></tr><tr><td>Price index (relative basket pricing)</td><td>X</td><td>X minus 20%–25%</td><td>Targeted assortment stores can consistently offer lower prices.</td></tr><tr><td>Occupancy cost (building, heat, light, power, water, security, maintenance, etc.)</td><td>Y</td><td>Y minus about 50%</td><td>Targeted assortment stores are engineered from the start for low-cost, basic features.</td></tr><tr><td>Shopping frequency of typical customer</td><td>1x weekly</td><td>2x or 3x weekly</td><td>A customer&#x27;s basket size per month may be the same, but the individual shops are smaller.</td></tr></table>

Source: BCG analysis.

The targeted assortment retailers have not been standing still. They have been adding services such as in-store butchers and products such as cage-free eggs, champagne, and snow crab claws at surprisingly low prices—items that once were sold only by retailers catering to affluent shoppers. Interestingly, more than a few of those well-heeled customers now shop at the targeted assortment stores.

## Traditional Retailers' Responses Have Fallen Flat

Traditional retailers were quick to slap “discounter” labels on the newcomers, dismissing their collective moves as a low-quality play. But the incumbents have finally seen how fundamental are the shifts in customer demand and how different are the underlying proposition, operating model, and economic model that characterize the targeted assortment retailers. As a result, the mainstream grocers have realized that many of their initial responses have actually widened the gap. Below are some of the moves they have made—with limited impact.

Adding Products. As their sales volumes have declined, many retailers have added range to try to stimulate sales and satisfy suppliers during negotiations. Variety appeals to shoppers, of course, but 176 types of salad

dressing—an actual SKU count at a leading US supermarket chain—is probably excessive. Wide, undifferentiated ranges dilute sales per product line, make stores more cluttered and harder to navigate, and add costs throughout the value chain.

Many retailers have also launched “discount” private-label lines. Yes, this has given them a lower entry price point in the categories, but it has failed to match the quality-price balance of the targeted assortment grocers. Worse, the private-label push has diluted sales per SKU and has created price and quality inconsistencies in many categories between different private-label tiers.

Boosting Promotions. Many traditional retailers have increased promotions to spark short-term sales, compensate for lack of price competitiveness, and please suppliers during negotiations. These days, it’s not uncommon for retailers to have upward of 40% of their sales come from promotions. However, the added promo typically disrupts shoppers’ perceptions of price and undermines their trust in the retailer. And it often inflates the shelf price and piles on operating costs across the retailer’s value chain.

Cutting Labor. Many grocers are cutting team members' hours to relieve pressure on the bottom line and free up funds to invest in price cuts. But the consequences are quick to appear, in the form of deteriorating service levels, and shoppers soon notice. Associates who are disengaged or too busy are poor ambassadors for a store's brand; if they're surly or rude, many customers will shop elsewhere.

While many factors shape grocery operations, short-term moves such as the ones we’ve described can be a “triple whammy”—a detriment to shoppers, suppliers, and retailers. More and more consumers see traditional retailers as expensive, complex, and unengaged. Suppliers experience declining volume, more complexity, and lack of scale per product line. And retailers see sales volumes sliding and operating costs heading in the wrong direction.

## The Right Way to Rethink Operating Models

So, how should retail executives respond? Leading grocery retailers that have successfully reinvented their operating models emphasize the following actions:

\- Revisit the customer value proposition. A crystal-clear value proposition demonstrates a deep understanding of a store's target customers and a high degree of confidence in being able to meet their expectations. Note that “value” in this context does not simply mean “discount” (although it could); instead, it refers to whether the customer feels that the store is meeting or exceeding his or her expectations.

BCG identifies three priorities for retailers that are reinventing their value propositions. The first is developing a clear understanding of customer demand, priority segments for the retailer, and its mission or purpose.

The second priority is clarifying the role and intent of each product category. By “role,” we mean the core purpose of a category as determined by customer insight, market attractiveness, and economics, and by the strategic importance to the grocer. The “intent” of a category refers to the direction for resource allocation and prioritization; it is based on relative market share, relative growth, and profit margin.

The third priority is ensuring that the right type of store is in the right location. To be sure, store types and networks can't be changed overnight, but retailers can quickly adjust macro spaces within their walls, and micro spaces within categories, in order to deliver a desired customer experience.

\- Get ready for category reset. For too long, retailers have either outsourced the category management process to major suppliers or have done little more than match competitors' actions in that respect. By “resetting” their categories, retailers can regain control of all aspects of them, including range, own brand, price architecture and level, trade strategy, merchandising principles, and supplier strategy and terms. A reset should also involve operational considerations such as pack size, stock levels, availability, and waste.

The reset process should be guided by a clear understanding of customer behavior and needs in the category, competitive positioning, and the economics of delivering the category proposition.

Range is an essential consideration for retailers facing rivals with lower SKU counts, such as Lidl and Biedronka. To compete, it's crucial to curate SKUs—carefully matching them to what most shoppers need most often—instead of adding more of them.

The reset process depends on the category. For fresh categories—often the key to driving overall customer perceptions—the process could result in more range, higher service levels, and more everyday low pricing. For basic packaged categories, the reset could result in big reductions in range and suppliers, a move to merchandising units, and a mid-low pricing strategy.

\- Streamline the total business operating model. Any reinvention initiative will require a hard look at end-to-end operations, from supplier to shelf. Trade-offs have to be made between investing in customer service and the funds required to pay for that while supporting the format's economic model. An efficient operating model is the basis for long-term price competitiveness, and the differences between retailers can be significant. For example, less efficient retailers can have a total loss (due to waste, shrink, and markdowns) of 4.0% to 4.5% of sales, whereas the efficient exemplars have losses as low as 2.0% to 2.5%.

Several elements of the operating model merit attention. One is collaboration between retailers and suppliers. Retailers and suppliers can achieve mutually beneficial outcomes by working together to improve promotion planning and

on-shelf availability; tailor flows and delivery volumes by format, store, and category; and cut supply chain costs.

Another important element is labor, which accounts for far and away the largest chunk of store operating costs. The key here is to establish and apply standard operating procedures that routinize store execution, improve productivity on the shop floor, and free up associates' time to spend with customers—all of which helps the bottom line.

THERE CAN BE no doubt that shoppers' buying habits and needs have changed substantially in the past decade. Name-brand loyalty is a thing of the past; the targeted assortment retailers have proved that point. It's time for mainstream stores to grasp those changes, too, and respond appropriately, with long-term positioning in mind.

## About the Authors

Gavin Parker is a partner and managing director in the Melbourne office of The Boston Consulting Group. He is also the global topic leader for retail transformation and reinvention and a core member of the firm's Consumer practice. You may contact him by e-mail at parker.gavin@bcg.com.

Thomas Jensen is a partner and managing director in the firm's Stockholm office. He leads BCG's European grocery retail sector and Nordic consumer business. You may contact him by e-mail at jensen.thomas@bcg.com.

Lodewijk van Meeuwen is a principal in BCG's Amsterdam office. You may contact him by e-mail at vanmeeuwen.lodewijk@bcg.com.

Bill Urda is a senior knowledge expert in BCG's Washington, DC office. You may contact him by e-mail at urda.bill@bcg.com.

Kate Cormack is a lead knowledge analyst in BCG's Auckland office. You may contact her by e-mail at cormack.kathryn@bcg.com.

The Boston Consulting Group (BCG) is a global management consulting firm and the world's leading advisor on business strategy. We partner with clients from the private, public, and not-for-profit sectors in all regions to identify their highest-value opportunities, address their most critical challenges, and transform their enterprises. Our customized approach combines deep insight into the dynamics of companies and markets with close collaboration at all levels of the client organization. This ensures that our clients achieve sustainable competitive advantage, build more capable organizations, and secure lasting results. Founded in 1963, BCG is a private company with 85 offices in 48 countries. For more information, please visit bcg.com.

© The Boston Consulting Group, Inc. 2016.
All rights reserved.
3/16
"""
