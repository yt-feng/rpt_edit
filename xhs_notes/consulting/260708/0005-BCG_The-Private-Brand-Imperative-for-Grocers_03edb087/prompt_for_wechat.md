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
# THE PRIVATE-BRAND IMPERATIVE FOR GROCERS

By Marco Valentini, Antonio Alvarez, Travis Jackson, Victoria Ma, Andy Adcock, Alexander Deopito, and Francesco Manzi

THE PROCESS OF SHOPPING for groceries today is radically different from what it was a decade ago. Products are fresher, cheaper, more healthful, more locally sourced, higher quality, more innovative, and more convenient. They are also available through a wider range of channels, including online shopping, club stores, and discounters, and increasingly they reflect the proliferation of private brands. The old mindset about private brands—that they’re similar to but not as good as national brands, come in plain packaging, and carry a lower price—is outdated and changing fast. Grocers that don’t rapidly adapt their private-brand strategy will soon be left behind, without a way to differentiate their offer or give customers the value they demand. And the pandemic has only intensified the need for them to change.

In the US, private brands now account for \$120 billion in sales each year, which amounts to 18% of the overall market. In Europe, private brands achieved even higher penetration levels two decades ago and now often rank as market leaders in their categories. In this context, many top-performing established grocers are investing in private brands. The move comes in response to a growing threat from new competitors, such as discounters, and as part of an effort by grocers to deliver more value to consumers, in the form of better products at a better price, as well as to differentiate themselves through unique products and to strengthen their brand equity.

Developing a winning private-brand proposition requires long-term investments and new capabilities. It isn't a simple process. Although some companies are further along in this journey than others, all grocers can—and indeed must—improve their offering in order to win in a fast-changing market and at a time when supply chains, product availability, and traditional consumer behaviors are threatened by a global pandemic.

## A Changing Industry

Several converging trends—many of which are being accelerated by fears of the coronavirus—are contributing to the current evolution in grocery retail. Consumer preferences are changing, particularly among millennials, who make up about 27% of US shoppers aged 18 and older and whose influence will continue to grow. Millennials demand offerings that are more convenient (especially as restaurants close), innovative, healthy, and environmentally sustainable. More broadly, grocery consumers tend to be better informed and more demanding, and their response to economic volatility is to seek value in the grocery products they buy—not necessarily the lowest price but a unique experience and the best quality for the price they’re willing to pay. Value for money is the fundamental principle. Consumers are more open to trying new products, and they have a stronger appreciation for convenience and fast access. In this vein, consumers are increasingly likely to shop for their groceries online, both because it is easy and to maintain social distancing.

These trends have encouraged the growth of alternatives to traditional grocers, including wholesale clubs, discounters such as Aldi and Lidl, convenience stores, e-commerce players, and mass merchants like Walmart and Target. This growth, in turn, has led to increased competition. Over the past five years, all of these channels have seen their market share in the grocery category in the US rise, as traditional grocers' share has declined. (See Exhibit 1.) A look at the disaggregated numbers behind the macro trend reveals that private brands have driven most of the shift. In the US market, \$3 billion per year of private-brand sales has moved from traditional supermarket players to other formats, although there has been no corresponding shift for national brands.

As we look at the overall rise of discount and other formats in the US, the correlation is clear: traditional supermarkets are in decline, and channels that rely more heavily on private brands are gaining share.

Private brands used to be nothing more than lower-priced copies of national brands, but that has changed dramatically over the past decade. Today, private brands are trendsetters in the grocery industry. They are increasingly on-trend, high-quality, innovative, and exclusive products that meet the demands of shoppers for fresher, more convenient, and more sustainable offerings. They also benefit from

EXHIBIT 1 | Private-Label Products Help Drive a Shift in US Market Share from Traditional Supermarkets to Other Channels

CONSUMERS ARE SHIFTING FROM SUPERMARKETS TO WHOLESALE CLUB, CONVENIENCE, OR DISCOUNT STORES

![](images/c29af104ef0aef7c12662e1d6377b3ef1a417f3ab48298d14fd9393d0f1d9b82.jpg)  
Sources: Planet Retail; Nielsen/PLMA 2018 Yearbook; BCG analysis.  
THE SHARE OF PRIVATE-LABEL PRODUCTS IS GROWING AT MASS, CLUB, AND DISCOUNT STORES AS CONSUMERS SEEK DIFFERENTIATED VALUE

![](images/bf1078328e5d0722256c78c99534374e24fe842d2cc6db326358209c0854e784.jpg)  
$^{1}$ Includes hypermarkets, club stores, drug stores, deep discounters, dollar stores, and convenience stores.

Source: Nielsen/PLMA 2018 Yearbook.

operational advantages: private brands enable grocers to reduce their dependence on national brands, narrowing their assortment of national-brand products and focusing on a smaller number of SKUs with higher sell-through rates. Grocers can create a unique value proposition by selling brands that customers can't find elsewhere—or whose equivalents can't be found in supply-constrained grocery aisles—and they can build stronger partnerships with a select set of national-brand suppliers.

For these reasons, retailers in virtually all geographic markets and all price tiers are investing to take their private-brand capabilities to the next level. Here are five publicly available examples from different geographic markets around the world:

\- Walmart is vertically integrating the supply chain for many of its private brands, allowing it to control the entire process from farm to shelf.

\- Aldi has used its private-label offering (responsible for about 90% of total sales) and extremely efficient store operations to lower costs and build a loyal following. An ongoing US expansion will put the company on track to become the third-largest grocer in the US by 2022.

\- Lidl has built a dynamic, modern assortment of offerings with a large lineup of private-label products that can compete with national brands. It was one of the first retailers to introduce different tiers of private-label products—good, better, best, premium—and it emphasizes responsiveness to customer needs.

\- Texas retailer HEB has become a destination for innovative private-label products, which now make up 28% of its online sales. The company even promoted its brand during the 2019 Super Bowl.

\- In Europe, Tesco and Carrefour have formed a buying alliance to jointly source their private-brand products in order to compete more effectively with discounters and to reset their relationships with consumer packaged goods (CPG) companies.

Overall, European grocers generate a larger share of sales from private brands than US grocers do. (See Exhibit 2.) Both European and US players are investing in private brands and will see continued growth in penetration, but we expect the US private-brand share to grow at a higher rate, narrowing the gap between them.

EXHIBIT 2 | US Retailers Lag Behind Their European Peers in Share of Sales from Private-Label Products  
![](images/0208125324ed55b3c4c7c818a8ac72b58f5cde14aa23960feddb9de077eaf113.jpg)  
$^{1}$ Figures are for 2017 and exclude data on label share for fresh food categories.

Challenges in Implementation
Although grocers may aspire to build a strong private-brand proposition, achieving this goal can be challenging, for several reasons. The most successful private brands essentially operate as CPG companies—a transformation that calls for steep investment and the right organizational structure, including new roles, decision rights, and incentives to support private brands. It takes time and marketing investments to build a brand, and grocers need to rethink their overall portfolio and ensure that their brand architecture can support the breadth of products needed to compete.

In terms of new capabilities, successfully introducing private brands requires a product development process that can identify consumer needs and trends and respond quickly, as well as a base of suppliers and partners that can provide the right quality at the right cost.

In some cases, the challenges are economic: some grocers depend on CPG funding to support national brands—and reducing sales of those products reduces the CPG funding. In other cases, increasing sales of lower-priced private brands leads to a drop in top-line sales and profits.

## A Structured Approach to Build Private Brands

No single formula effectively addresses these issues. The right approach varies from one grocer to the next. However, the strategic objectives involved in developing private brands are consistent: they are a way for grocers to differentiate themselves by offering a unique selling proposition, increase margins, and control a greater share of the product range in key categories.

Our experience working with leading players in the industry leads us to believe that grocers need to focus on three key elements in order to succeed with private brands.

Set the vision and strategy, with the right organizational structure to support it. First, grocers need to establish a clearly defined vision and strategy for how private brands will fit into their overall offering and business model. Strategic brand decisions include how many brands and tiers to offer, whether to use the retailer's banner as a brand or instead create a new brand, and how to balance quality and value in comparison to national-brand products. There is no one right set of universally applicable answers, because these decisions affect a customer's perception of the product's quality and value—and thus the customer's willingness to try the product. Grocers must also set the right level of ambition and appropriate targets, being realistic about their starting point, their right to win, and their desired destination.

In addition, grocers need to put the right organization in place to champion private brands. Different models have been successful, depending on the retailer's aspiration, maturity, and culture. We have identified three potential organizational models for private brands:

\- Some retailers give a dedicated and entrepreneurial category management team full responsibility for making all decisions about private-brand products and merchandising—including assortment, pricing, space, sourcing, and quality—so that it is accountable for its own sales and net margin results.

\- In other organizations, a center of excellence leads the private-brand business. The center of excellence supports the broader category management teams in such processes as product development, specifications, sourcing, and merchandising for private-brand products. Managers hold economic accountability and make decisions at the category level.

\- Finally, some retailers opt for a hybrid structure, in which specialized category managers below a head of merchandising oversee private brands and national brands separately. Each manager has some latitude to run processes and make decisions, but coordinated support and more strategic category planning come from higher levels in the organization.

Build up capabilities in innovation and new product development. The second critical priority is to build up strong innovation and product development capabilities. Leading grocers have introduced significant innovations to help make products more healthful, fresher, more environmentally sustainable, more convenient (including packaging for ready-to-drink or ready-to-eat use), and better differentiated from the competition overall in terms of quality and price. But others need to improve their ability to capture consumer insights and to use data to identify unmet needs, assess the relevance of their private brands, and spot emerging trends to capitalize on.

Retailers often base their assortment decisions entirely on the national and private brands within their own stores. Yet innovation starts with a holistic view of the market that extends beyond the retailer's four walls. The first step toward creating a differentiated private brand that attracts loyal customers is for retailers to identify categories that they want to be known for and that are important to customers. Then, through a systematic review process that entails quantitative data and a hands-on assessment of actual products, retailers can assess their offerings (of both national brands and private brands) against those of key competitors to identify opportunities. This type of side-by-side comparison of similar products can often uncover unmet needs in areas such as product quality, form, and packaging—or additional products themselves.

Customers are only one side of the equation. In a store where private-brand products appear on the same shelf with national-brand products that meet the same customer need, the retail merchandising organization must have an incentive to support sales of the private-brand products. This means finding the right balance between cost and quality on the supply side to ensure that selling a unit of a private-brand product has the same or a better bottom-line impact than selling a comparable national-brand product, even at a lower retail price.

Strengthen the supplier network. In order to succeed, retailers need strategic supplier partnerships, not just transactions. Today, it's not enough to solicit bids on individual items and award contracts to the lowest-cost supplier. Instead, retailers need to review a supplier's capabilities holistically and identify the right key partners to grow with—organizations that can bring CPG-like insights across categories, invest in innovation, and reliably provide high-quality products at the right cost, so that retailers can price them competitively and deliver value to the consumer.

When retailers can't find suitable manufacturing and innovation capabilities in their markets, they need to adopt a longer-term perspective and make the investments required to build these capabilities internally. Another option is to co-invest with suppliers to jointly develop such capabilities.

Together, retailers and suppliers can create a mutually beneficial partnership by sharing information, jointly seeking efficiencies to reduce costs, and tailoring the merchandising strategy to maximize sales and grow together. For these reasons, successful retailers often maintain preferred or exclusive relationships with strategic suppliers.

THE CHANGES AFFECTING the grocery industry aren't going away. Millennials will exert greater purchasing power, non-traditional formats such as discounters and mass merchants will continue to put pressure on incumbent grocers with highly competitive prices, and customers will continue their relentless search for value.

Of course, the pandemic will continue to shape consumer behavior—even after vaccines have been developed and distributed.

For established grocers, one fundamental way to address these challenges is to invest in private brands. These products are no longer just higher-value copies of national brands; instead, they are a means for grocers to become more innovative and to set industry trends. Retailers with winning pri-

vate brands have invested systematically to build their own new product development capabilities and are consistently ahead of the curve. Getting there isn't easy, but the rewards of success—stronger customer loyalty, improved operations, and better financial performance—justify the effort.

## About the Authors

Marco Valentini is a managing director and partner in the Miami office of BCG. He is BCG's global lead for private brands. You may contact him by email at valentini.marco@bcg.com.

Antonio Alvarez is a partner in the firm's Miami office. You may contact him by email at alvarez.antonio@bcg.com.

Travis Jackson is a managing director and partner in BCG's New Jersey office. You may contact him by email at jackson.travis@bcg.com.

Victoria Ma is a principal in the firm's New Jersey office. You may contact her by email at ma.victoria@bcg.com.

Andy Adcock is a senior advisor in BCG's London office. You may contact him by email at adcock.andy@bcg.com.

Alexander Deopito is a senior advisor at BCG and operates worldwide. He was an executive for more than 20 years at Lidl, where he was responsible for the company's private label business, among other functions and business units. You may contact him by email at deopito.alexander@advisor.bcg.com.

Francesco Manzi is a principal in the firm's Miami office. You may contact him by email at manzi.francesco@bcg.com.

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

## © Boston Consulting Group 2020. All rights reserved. 4/20 Rev. 2/21

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and Twitter.
"""
