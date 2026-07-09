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

## How Discounters Are Remaking the Grocery Industry

The Boston Consulting Group (BCG) is a global management consulting firm and the world's leading advisor on business strategy. We partner with clients from the private, public, and not-for-profit sectors in all regions to identify their highest-value opportunities, address their most critical challenges, and transform their enterprises. Our customized approach combines deep insight into the dynamics of companies and markets with close collaboration at all levels of the client organization. This ensures that our clients achieve sustainable competitive advantage, build more capable organizations, and secure lasting results. Founded in 1963, BCG is a private company with 85 offices in 48 countries. For more information, please visit bcg.com.

THE BOSTON CONSULTING GROUP

# How Discounters Are Remaking the Grocery Industry

## AT A GLANCE

Discount grocers used to focus primarily on low prices. Now, however, they are building larger stores and selling a wider range of goods, including a broader assortment of fresh products. As a result, discount grocers are poised to take more than half of the total grocery market share in many regions.

## MOST ESTABLISHED PLAYERS WILL NEED TO TRANSFORM THEMSELVES

In markets where discounters are already a large and growing presence, established grocers must improve their pricing, product assortment, and overall store experience, potentially through a transformation program that reinvents the brand.

## AMBITIOUS GROCERS CAN LAUNCH THEIR OWN DISCOUNT BRAND

In markets where discounters are just getting established, grocers can launch their own discount brand, clearly separated from the core business. But in addition to significant investment, this approach will require a new mindset and culture.

## DISCOUNTERS MUST AVOID THE RISKS OF OVEREXPANSION

Discounters must refrain from rushing into new markets and introducing complexity into their winningly simple business models. They will need to thoroughly understand the markets in which they plan to expand and continue to execute well.

A DECADE AGO, DISCOUNT GROCERS had a limited impact in most markets. These players, which primarily offered cheaper prices for a narrower range of products, typically took 10% to 20% of market share around the edges. Today, discounters are evolving from stripped-down, no-frills stores to become a genuine alternative for many consumers—and a major factor in the grocery industry. As a result, they may soon claim up to half of the total share in many markets.

Discounters are opening bigger stores with innovative features, expanding their assortment of fresh and organic products, and selling private-label products that beat out established brands in taste tests—all at much lower prices. Not coincidentally, discounters in many markets are also scoring higher than established companies on customer advocacy, as measured by BCG’s proprietary Brand Advocacy Index (BAI). Their customer base has grown beyond low-income shoppers to include savvy, high-income consumers, who are increasingly asking a fundamental question: “Why should I pay more?”

The dramatic growth of discounters will have profound consequences for the overall grocery industry. Given that discounters are here to stay in many markets, mainstream players need to address the challenge head on by fundamentally transforming themselves to improve their prices, product assortment, and store experience. Some may also opt to launch a discount brand of their own. And discounters must avoid the risks of overexpansion by being judicious about the markets they move into and by ensuring that they can still achieve a structural advantage over current players in those markets.

## The Rise of Discounters

Discounters first began to gain traction in the 1990s, particularly in Germany with the Aldi and Lidl brands. The winning formula at the time was to offer low prices on a targeted assortment of mostly private-label products. Stores were cramped and had a low-budget feel, but customers felt they were getting better value—a key differentiator that was sufficient to increase traffic. As a result, discounters managed to disrupt the grocery retail market in multiple countries.

In that initial phase, discount grocers typically performed well during periods when consumer spending was down. These shops were countercyclical, like dollar stores; they benefited from budget-conscious shoppers during recessions. Mainstream retailers, therefore, could afford to ignore the discount grocers and still retain 80% to 90% of the total market.

Today, however, that's no longer true. Discounters grew at a rapid clip from 2000 to 2015, gaining significant market share in many Western countries, including Denmark, Poland, and Turkey. (See Exhibit 1.) That growth shows no signs of slowing, even as household incomes have risen. Worldwide, discounters are projected to increase their number of store locations by $4.4\%$ a year through 2020, compared with just $2.9\%$ for mainstream supermarkets and $1.6\%$ for superstores and hyper-markets. Some regions will see an even faster expansion, including Eastern Europe (more than $30\%$ ) and Latin America (approximately $8\%$ ).

There is a demographic aspect to that growth: millennials prefer discounters over mainstream grocers in most markets. In large developed markets (including the US, Europe, Australia, Canada, and Japan), this population comprises 275 million people, more than any other demographic segment, and their aggregate spending power rivals that of all other segments combined. Millennials tend to be very pragmatic, opting to buy most of what they need in a convenient location, without the hassle and burden of an overwhelming number of choices. Moreover, they inherently distrust some mainstream brands and are willing to try unconventional options—particularly given the right in-store experience.

Yet the biggest factor in discounters' success over the past decade is that these companies have evolved and redefined their approach to offer higher-quality products, a broader assortment, and an improved shopping experience.

\- Higher Quality. Discounters have always focused on private-label products at lower prices, but they are increasingly beating out branded products in head-to-head tests. Aldi Süd and Lidl Stiftung were pioneers in this area: their house brand products have won in both blind taste tests and independent quality reviews in Germany since the 1990s. Both companies have further customized their products to meet local taste preferences. More recently, the private-label

EXHIBIT 1 | Discounters Are Growing Quickly in Many Western Markets  
![](images/7077768edb5b24af4279bc0f9bdb07c589ca4f9aa8fdf569b67046fd2781b177.jpg)  
Sources: Planet Retail; BCG analysis.

ketchup from a leading discounter in the UK beat a global brand in a taste test conducted by the Guardian. The two versions have identical ingredients and very similar packaging, yet the private-label version costs roughly two-thirds less than the established brand.

In addition to taking the lead in price and quality in dry goods, discounters have become more innovative and are now succeeding not only in categories that consumer packaged goods companies have long considered to be “safe”—such as baby food, breakfast cereals, pet food, and personal care—but also in categories for which branding and marketing are paramount, such as beauty products. Discounters are raising their quality standards in some areas, such as packaging and design, as well.

\- Broader Assortment of Products. Discounters have also begun opening larger stores, with an average increase in size of 16%, over the past ten years. They typically use the additional space to sell a broader assortment of products. In addition, because discounters focus so intently on understanding what customers want, they can meet a wider range of needs, even though their stores are still smaller than those of traditional grocers and carry fewer products. As store sizes increase, discounters typically add fresh-food categories, such as produce and baked goods that are prepared onsite. Other additions include organic and gluten-free options and luxury products, such as lobster and quail. Many now have a large refrigerated section with prepared foods, dips, and soups as well.

Convenience is another recurring theme. In the Netherlands, the variety of fresh, ready-to-heat meals in aluminum trays that Lidl offers far exceeds similar options from some of its rivals. Discounters also limit the availability of new products for a short time, creating an aura of exclusiveness about them and encouraging customers to buy quickly so they don't miss out.

\- Improved Shopping Experience. Many discounters now offer extended opening hours, faster checkout service, and an upgrade of the look and feel of the stores, such as wider aisles, improved lighting, and digital signs. Lidl, for example, is investing roughly \$3 billion to upgrade its stores in Germany over the next five years, and \$1.5 billion on its stores in the UK over the next three years. Some chains are even testing innovative store features. At a new Lidl store in Belgium, for instance, shoppers can charge their electric cars and bikes for free; the capability is powered by nearly 1,000 solar panels on the store's roof.

One thing that hasn't changed, however, is the price advantage. Discounters' prices are typically $15\%$ lower than the private-label offerings from established grocers, and up to $200\%$ lower than branded products at traditional grocers. As discounters have increased the size of their stores and added new features and products, they've focused on higher-margin offerings. As a result, they've managed to keep their operational costs down while boosting store productivity, which has pushed their margins higher. (For a case study, see the sidebar.)

In fact, that price advantage is becoming more transparent to shoppers. Unlike in the past, the broader assortment of products now available at discounters means

# HOW ONE DISCOUNTER KEEPS COSTS DOWN AND MARGINS UP

To understand the success of discounters, consider one discount chain that operates in many developed markets and has been expanding rapidly. The company has a highly efficient and profitable operating model and lower costs, particularly in labor. Its gross margins are approximately 8 percentage points lower than those of supermarkets, yet its margins for earnings before interest and taxes are higher—about $5\%$ , beating the average supermarket chain by about $2\%$ . Here's how the company has gained an edge:

\- Rather than relying on suppliers to develop products, the company uses strict internal processes. For example, it designs packaging so that employees can read barcodes, stock products more efficiently, and make better use of shelf space.

\- To reduce the cost of goods sold, it negotiates net-net buying prices with suppliers. Under that ar-

rangement, the chain agrees not to charge suppliers for such things as bonuses, rebates, and funding. In return, suppliers cover other costs on their side, including packaging and logistics.

\- The company pays above-market wages to attract employees, and it develops them through well-defined career paths, rigorous training, and extremely high standards. That leads to lower attrition rates, a result that reduces the cost of replacing departed employees—and ultimately boosts margins.

\- Although the company pays employees more than its competitors, it keeps labor costs down through a supply chain that is built to minimize in-store logistics and to maximize the efficiency of store workers. For instance, store labor schedules are carefully aligned with delivery schedules.

that the prices for items purchased during a typical shopping trip at a discounter are easily comparable with the prices for items purchased at a traditional grocer: shoppers can literally compare apples with apples. When consumers can buy essentially the same products at a discounter and easily see how much they saved, the challenge for established grocers gets even bigger.

## Huge Shifts in Market Share

For established mainstream grocers in many markets, the growth of discounters has led to a pronounced drop in market share. Consider Ireland, for example. From 2000, when the first discount stores were launched, to 2015, discounters grew dramatically and took one-fourth of the market share from established players in the country. Some chains, such as Lidl, use Ireland as a test market for store innovations before exporting them to other locations; the country has become a talent incubator for Lidl as well.

The story in the UK is similar. Over the past ten years, discounters there have dramatically expanded their assortment of products, improved the store experience, and grown their profit margins. Mainstream grocers, on the other hand, have watched their margins shrink from more than 5% to less than 3%, with a corresponding drop in shareholder value.

But discounters can disrupt grocers even without taking significant market share from them. Because their product assortment is targeted to essential customer needs, discounters can sell a much greater volume of individual items and dominate a category. For example, a discounter in one market with just 18% share has 12 types of pasta available—compared with more than 100 offered by the established grocer in that market—yet it sells more than three times as much pasta in core product lines as the established grocer. This allows for a much more efficient supply chain arrangement with the manufacturer—including larger production sizes and full truck loads, for example—and thus lower product prices for the discounter.

Notably, discounters are not only winning over customers but also converting them into loyal brand ambassadors. Overall, discounters have a higher BAI than established grocers in most of the markets in which BCG tracks that metric. In part, this increased advocacy is because discounters today focus not only on value—the most important factor in BAI for the grocery industry—but also on such key areas as product assortment, store hours, fresh goods, and the overall shopping experience.

To better understand the dynamics of discounters and how much they will challenge established grocers, we identified three distinct phases of development with different levels of activity and success among discounters: nascent, expanding, and mature. (See Exhibit 2.)

\- Nascent. In these markets, discounters have yet to establish a serious presence; they typically have market shares of less than 15%. And some of these markets—including in the US, Sweden, and Australia—are still essentially white spaces. They present an opportunity for discounters to disrupt the market, and some are already taking steps to do so. For example, Lidl is planning to open 20 stores in the US in mid-2017 and another 80 during the subsequent 12 months. Those stores will be significantly larger than Lidl’s European locations, with elements such as cold beer and free bakery samples. In addition, Aldi, which operates in some US states, will revamp 1,300 of its stores and open another 650 by 2018, for a total of more than 2,000.

\- Expanding. In expanding markets, such as those in Belgium and Poland, discounters have established a foothold and begun to take significant market share: approximately 10% to 40%. They have strong operating models in place, with high sales productivity per square foot, and they are continuing to grow by replicating that model through newly opened locations. Lidl plans to open 200 locations in Poland, along with 100 in Romania.

\- Mature. In mature markets—such as those in Norway, Germany, and Denmark—discounters have taken more than 35% of market share. Established grocers in this type of market can still react, but they can no longer get ahead of the threat.

EXHIBIT 2 | Discounter Markets Fall into Three Phases of Maturity  
![](images/7bea6ab085089f7e1c72116bf2397a59155b3a66fd308aa539a6bc2140040c6d.jpg)  
Sources: Planet Retail; BCG analysis.

In response to the industry's changing dynamics, some established grocers may decide to do nothing. In nascent markets, for example, doing nothing may be the best option. Yet most grocers will need to take action. On the basis of our analysis, we see two strategic options that mainstream grocers can take to respond to the changing dynamics in the industry: revamp the operating model and costs or create a spinoff discount brand.

## Revamp the Operating Model and Costs

The first strategic action is to fundamentally improve the company's operating model and to reduce costs in such a way that management can justify the remaining price differential with discounters to its customers and shareholders. This response—which is less a suggestion and more of an imperative for many established grocers—requires more than a few incremental tweaks here and there. Instead, companies need a major transformation in multiple areas.

Reduce the price gap with discounters, especially for price-sensitive products. Mainstream grocers will never completely eliminate the price gap with discounters—and they don’t need to. They just need to be competitive in the areas that are most important to customers.

For example, consumers are often very price sensitive about commodity-type products, such as canned goods, paper products, and cleaning supplies, which are not highly differentiated. In these areas, grocers need to be more aggressive about price reductions. Conversely, in some fresh-product categories—such as the deli counter, butcher, or seafood counter—consumers are far less price sensitive (with some exceptions) and more willing to pay for service. In these areas, grocers can capitalize on their advantages: more customers, higher volume, bigger stores, and more developed supply chains. To take advantage of this split, grocers need deep customer insights to understand which departments and products really matter to their customers, where they can win, and how they should target their investments and improvements.

Scale back operating costs. Improving prices also requires decreasing operating costs and the cost of goods sold. Options include reducing the total loss of unsellable food that gets thrown away, using labor more efficiently, changing the assortment to reduce supply chain complexity and cost, negotiating pricing and other terms with suppliers, and introducing private-label products. For a typical mainstream grocer, cutting prices by 5% requires a reduction of either 7.5% 

[中间内容因长度限制已省略]

 execution—and try to compete in ways that favor established grocers. (Already, a few discounters have undergone management changes due to these kinds of growing pains.) To avoid this fate, discount management teams should make sure that they are maximizing their efforts in the markets where they currently operate before expanding into new ones—particularly in large countries, such as the US and Australia, which require sprawling distribution networks. They also need to carefully analyze which markets make the most sense to enter, how many stores they should open in those markets, and what the distribution infrastructure should look like. Above all, they need to avoid sacrificing their highly efficient operating model in pursuit of a more attractive customer experience.

DISCOUNTERS IN MANY markets have triggered a major disruption for the grocery industry over the past decade—a disruption that will continue. By evolving the way they operate—and becoming more innovative in how they develop new products to meet customers' needs—they are taking greater market share from established grocers. But they need to avoid overexpanding and introducing too much complexity into their simple operating models, which have worked so well. Incumbent players need to decide on the right strategic response—transforming their operations or launching a discount brand of their own.

Both groups, however, face similar challenges: to identify the needs of their target customers, offer them a unique experience, and strike the right balance between complexity and efficiency. Customers can be extremely loyal to their favorite grocery chain. Companies that understand the underlying factors of that loyalty will position themselves to win.

## About the Authors

Rune Jacobsen is a senior partner and managing director in the Oslo office of The Boston Consulting Group. He is the global leader of the firm's consumer retail sector. He is an expert with BCG TURN, which helps clients deliver rapid, visible performance improvements in the short term while strengthening their organizations and positioning them to win in the future. You may contact him by email at jacobsen.rune@bcg.com.

Gavin Parker is a partner and managing director in the firm's Melbourne office. He leads BCG's global work in retail transformation and reinvention, and he specializes in helping large national and international grocery chains transform themselves to improve performance. You may contact him by email at parker.gavin@bcg.com.

Thomas Jensen is a partner and managing director in BCG's Stockholm office. He leads the firm's Consumer practice in the Nordic countries, and he is a core member of the firm's Marketing, Sales, & Pricing practice. He has significant experience in helping retailers manage their product categories to improve the customer experience while also increasing operational efficiency. You may contact him by email at jensen.thomas@bcg.com.

Jeroen Magnus is a principal in the firm's Brussels office. You may contact him by email at magnus.jeroen@bcg.com.

Holger Gottstein is a senior partner and managing director in BCG's Melbourne office. He leads the firm's Consumer practice in Australia and New Zealand. He has significant experience helping global retail companies launch business transformations, improve supply-chain performance, develop new store concepts, and implement e-commerce strategies. You may contact him by email at gottstein.holger@bcg.com.

Markus Hepp is a partner and managing director in the firm's Cologne office. He is a member of the global leadership team of BCG's Consumer practice, and he leads the firm's retail work in Europe. He focuses on helping retail clients develop new store concepts, manage categories, and improve pricing and store operations. You may contact him by email at hepp.markus@bcg.com.

Bill Urda is a senior knowledge expert in BCG's Washington, DC, office and a member of the firm's Consumer practice, specializing in the grocery sector. You may contact him by email at urda.bill@bcg.com.

## Acknowledgments

The authors thank Jan Fockedey, Jonathan Sharp, and Frédéric Tiberghien for their support on this report. In addition, they thank Dalton Philips (a former CEO of Wm Morrisons Supermarkets) and Tor Helge Gundersen (the chief marketing officer of Coop Norge) for their expertise and insight.

The authors acknowledge Jeff Garigliano and Kelli Gould for their contributions to the development and writing of this report, and Katherine Andrews, Gary Callahan, Lilith Fondulas, Kim Friedman, Abby Garland, and Sara Strassenreiter for its editing, design, and production.

## For Further Contact

If you would like to discuss this report, please contact one of the authors.

To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcgperspectives.com.

## BCG

## THE BOSTON CONSULTING GROUP

Bogotá

Berlin

Abu Dhabi

Boston

Amsterdam

Athens

Beijing

Chicago

Cologne

Atlanta

Brussels

Copenhagen

Barcelona

Auckland

Geneva

Buenos Aires

Frankfurt

Kiev

Bangkok

Dallas

Kuala Lumpur

Düsseldorf

Budapest

Munich

Hamburg

Dubai

Denver

Nagoya

Lagos

Detroit

Helsinki

Madrid

Ho Chi Minh City

Lima

Calgary

New Delhi

Luanda

Melbourne

Lisbon

Hong Kong

Mexico City

New Jersey

London

Los Angeles

Houston

New York

Miami

Perth

Milan

Philadelphia

Prague

Oslo

Paris

Minneapolis

Rio de Janeiro

Riyadh

Rome

Canberra

San Francisco

Santiago

Monterrey

São Paulo

Montréal

Istanbul

Shanghai
Singapore
Stockholm
Stuttgart
Sydney
Taipei
Tel Aviv
Tokyo
Toronto
Vienna
Warsaw
Washington
Zurich

Casablanca

Jakarta

Chennai

Seattle

Johannesburg

Moscow

Mumbai

Seoul

bcg.com
"""
