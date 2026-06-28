你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/0afb1e792892214c151cc2de7d052cb71d10482135cd299784867071f6ea75a4.jpg)

CLIMATE CHANGE AND SUSTAINABILITY

# Processed and Pressured: CPG's Lost Decade of R&D

By Alejandro Navarro, Brad Jakeman, Geraldine Rhodes, Ezgi Sonmez, and Nina Peters

ARTICLE JUNE 11, 2026 15 MIN READ

Is the R&D bill coming due for big consumer packaged goods companies?

Growth in the food and beverage industry has been hard to come by. Inflation, supply chain disruption, geopolitical turmoil, and consumer belt-tightening have all played a role, but those forces, however severe, are mostly cyclical. The structural shift that many big CPG manufacturers have so far failed to navigate is consumers' growing preference for healthier and simpler products and for greater transparency about ingredients, which has exposed at least a decade of underinvestment in R&D.

Most food and beverage companies have long pursued a strategy that prioritized scale and marketing muscle. The bet was that size and strength could keep heritage brands relevant without breakthrough product and ingredient innovation. These companies put their money where their thinking was, investing a meager 1.5% of sales in R&D from 2015 to 2025; in 2025, meanwhile, they spent 6% to 15% of revenues on advertising and promotion.

It was a successful formula for a long time, but now the bargain is breaking down. In May 2025, we argued that consumers were transitioning toward healthier food and beverage choices faster than CPG companies were moving to provide them. At the same time, regulators are emphasizing healthy and nutritious eating—and are introducing additional scrutiny and regulatory requirements in some product categories. These shifts have added to the share-loss problem for big manufacturers. Marketing muscle and big brand names cannot compensate for product portfolios that do not reflect today’s priorities, including those around health and nutrition.

## The Lost Decade

The underinvestment in R&D wasn't a blip; it was a sustained strategic choice. Over the past two decades, while big food and beverage companies were making minimal investments in R&D, other industries dedicated large percentages of revenues to new-product development, including pharmaceuticals (21%), consumer electronics (18%), and software (16% to 20%), according to January 2026 data compiled by New York University's Stern School of Business. The industry comparisons may be imperfect but the order of magnitude is hard to ignore. Moreover, during this period, global CPG R&D spending grew at just 1.2% a year, while advertising and promotion grew at 2.6%, more than double the pace of spending on R&D. (See Exhibit 1.) Of course, marketing remains essential, and it helps carry heritage brands, but it cannot fix a portfolio problem on its own.

![](images/e9b82943d84a9746cc731f7ae08119200699c809fb6473008d42a987cec64a92.jpg)  
Sources: Barclays Investment Bank Equity Research, “The new rules of the FMCG game,” January 2026; S&P Capital IQ; BCG analysis. $^{1}$ Annualized TSR of companies in the S&P Global LargeCap index, as well as Unilever, Nestlé, and Danone; TSRs use company reporting currency and are based on data ending in December 2025. $^{2}$ The S&P Food & Beverage Select Industry Index covers food and beverage manufacturers, whose products include foods and meats, soft drinks, and nonalcoholic beverages. Weighted average and median TSRs calculated by geometrically compounding each company’s annual returns over three years and then weighting by market capitalization.

The breakthroughs that are reshaping CPG, such as prebiotic sodas, plant-based dairy, GLP-1-friendly snacks, and reformulated “clean label” products, have overwhelmingly come from challengers and insurgents rather than incumbents. The missing ingredient for big CPG has been a sustained engine of rigorous, well-financed R&D in recipes, ingredients, processes, and equipment that meets consumers where they want to be.

Investors are rendering their verdict. Over the three years through December 2025, the median large-cap food and beverage company delivered a total shareholder return of approximately -5%, while the S&P 500 delivered a cumulative total return of almost 90%. The worst CPG performers registered cumulative TSRs of -20% or less. Investors have repriced growth assumptions, recognizing that what little revenue growth there's been since 2021 has come from price, not volume, which has actually declined 0.6%.

There are exceptions, and they reward study. Danone, for example, increased R&D spending by roughly 32% over the past two years, reinvested in new capabilities, and divested noncore assets. It delivered like-for-like revenue growth of 4.3% in 2024 and 4.5% in 2025, propelled ROIC back into double-digit territory, and delivered TSR well ahead of its large-cap food and beverage peers. Smaller, more nimble manufacturers are also demonstrating that innovation sells—a lot. Their brands are growing faster than the incumbents’ despite the latter’s considerable scale advantages.

They say you can't cut your way to growth. Nor can you advertise your way to innovation. CPG companies need to reset how they approach R&D.

# Why the Bill Is Coming Due

We observed last year that multiple trends were driving big changes in consumers' food and beverage purchases, particularly those involving what are commonly known as ultraprocessed foods (UPFs). Three of the biggest underlying trends are:

\- Increasing awareness of health and nutrition, fueled in part by the rising use of GLP-1s

\- Expanding regulatory action around food and diet

\- An increasing array of digital- and AI-enabled shopping apps and interfaces

These trends are not abating; in fact, they are picking up speed and catalyzing other market forces. UPF categories, which play an outsized role for most major CPG manufacturers, have continued to decline or grow more slowly than the overall food and beverage market. (See Exhibit 2.) While a few categories show short-term rebounds, performance remains uneven and structurally weaker than the total market.

EXHIBIT 2

US Consumers Are Rewiring Demand for Processed Foods and the Shift Is Sticking

![](images/e9fbee0772c77dc41c1aa7f16ebc8e24feb2c6bba1d7438fa08e6ec54150d563.jpg)

<table><tr><td></td><td>CAGR, 2022-2023 (%)</td><td>CAGR change, 2023-2024 (%)</td><td>CAGR change, 2024-2025 (%)</td></tr><tr><td>— Candy, gum, mints</td><td>6.6</td><td>1.7</td><td>4.2</td></tr><tr><td>— Salty snacks</td><td>6.9</td><td>0.1</td><td>-0.2</td></tr><tr><td>— Rolls and buns</td><td>6.3</td><td>1.3</td><td>-0.9</td></tr><tr><td>— Prepared foods</td><td>4.9</td><td>0.3</td><td>0.7</td></tr><tr><td>— Cookies and crackers</td><td>5.8</td><td>-0.5</td><td>-1.3</td></tr><tr><td>— Desserts</td><td>4.4</td><td>1.2</td><td>1.7</td></tr><tr><td>— Cereal/granola bars</td><td>5.9</td><td>-6.4</td><td>3.2</td></tr><tr><td>— Salad dressing</td><td>5.4</td><td>0.5</td><td>-3.7</td></tr><tr><td>— Bread</td><td>5.8</td><td>-1.2</td><td>-2.7</td></tr><tr><td>— Ready-to-eat cereal</td><td>5.0</td><td>-1.4</td><td>-2.3</td></tr><tr><td>--- Total F&amp;B</td><td>5.2</td><td>2.2</td><td>2.4</td></tr></table>

x.x Above market x.x Below market x.x Declining  
Sources: NielsenIQ data; Babak Ravandi et al., "Prevalence of processed foods in major US grocery stores," Nature Food, January 13, 2025; BCG analysis. Note: Highly processed according to FPro (Food Processing) score.

Across multiple categories, large brands continue to lose share to insurgent products from small companies as well as to retailers' house brands. Multiple forces are at work, including affordability (discussed below). Still, it's clear that both insurgents and retailers are gaining share by staying closer to consumers, paying attention to their needs and preferences, and communicating with them through the channels they use today, such as social media. Consider a few category shifts: in cereal and granola bars, a 12.4 percentage-point loss for big brands from 2021 to 2025 versus a gain of 10.8 points for insurgents and 1.6 points for private labels. Or ready-to-eat cereal: a 5.2-point big-brand loss versus a 4-point gain for small brands and a 1.3-point gain for private labels. (See Exhibit 3.)

## EXHIBIT 3

Large Brands Continue Losing Share in Ultraprocessed-Food and Beverage Categories to Both Smaller Brands and Private-Label Manufacturers

![](images/c020f200324df53e078812c56a43169c7dd8e556b13202440ade69f5d3c2179a.jpg)  
Sources: NielsenIQ data; BCG analysis.  
Note: Ultraprocessed according to FPro (Food Processing) score.

Some of the fuel for this fire comes from GLP-1 use, which continues to rise. Recent BCG consumer research estimates that there are 16 million GLP-1 users in the US today, up from 6 million in 2022. We estimate that more than 30 million people will be using these drugs by 2030 as prices fall and generics and new oral formulations come to market.

The implications for CPG are structural. Active users of GLP-1s cut their calorie intake by about 30%, with snacking down 40% in processed foods, sugar-sweetened beverages, and refined grains. Roughly a third of food spending shifts to nutritional supplements, fitness, beauty, and self-care. Some 70% of households with one GLP-1 user follow the same patterns, expanding the demand shift to 1.5 times the user base.

One immediate challenge to UPFs comes from regulatory intervention. The US government has introduced a new food pyramid that discourages consumption of UPFs and refined grains in favor of meat, produce, and a broader range of fats, including animal-based fats. The new guidelines

likely mark the beginning of a broader set of policy interventions targeting UPFs, including required food labeling and the removal of UPFs from government-funded food programs such as SNAP (the Supplemental Nutrition Assistance Program). At the state level, more than 130 proposed bills in almost 20 states could add complexity as well as restrictions to existing regulations.

Governments have cited both fiscal and public-health considerations in recent policy discussions, particularly the growing awareness of the long-term costs to society of chronic illness. Annual US health care costs exceeded \$5.3 trillion in 2024, and the Centers for Medicare & Medicaid Services estimates 2025 growth at 7%. Obesity alone costs the US health care system up to \$260 billion a year. (Encouragingly, Gallup data through the third quarter of 2025 shows that obesity among US adults has declined for the first time in years, from a peak of 39.9% in 2022 to 37%, coinciding with the scaleup of GLP-1 use.)

The impact on CPG is becoming apparent. For the first time, we are seeing early evidence of a reversal in UPF consumption as an expanding coalition of policy makers, regulators, consumers, and cultural voices reframe food as a systemic health topic.

## Power to the (Informed) Consumer

Another significant long-term shift for CPG companies is consumers' rising use of digital apps and new AI-powered interfaces that are reshaping how they find and choose products. Yuka, one of multiple apps that provide real-time information on food products' health and nutritional value, is now available in 12 markets worldwide; the app has 25 million users in the US and is adding 600,000 users a month—without a dollar spent on advertising.

As agentic commerce develops, the balance of power among e-commerce, brick-and-mortar stores, and direct-to-consumer channels will evolve, putting the consumer in greater control and creating both disruption and new routes to market for manufacturers. Increased transparency and comparability mean that product and price differentiation becomes harder to sustain, with digital intermediaries having a greater say in how products are described and assessed. CPG companies need to build visibility and capability in these new interfaces, using test-and-learn approaches and, selectively, developing their own AI-enabled consumer touchpoints.

Then there is the critical issue of affordability, especially in the US, where food prices—more than 30% higher than in 2019—are running well ahead of the 26% rise in the headline consumer price index. Lower-income households are especially hard hit, now spending about a third of their aftertax income on food. One result is a more discerning, value-seeking consumer, one for whom R&D and price-value architecture must work together.

Another factor is how private label has become a structural force in the competitive landscape. Major retailers have invested significantly in their own brands, developing offerings that compete on quality, transparency, and innovation as well as on price. The innovation playing field is more crowded than it has been in a generation. Retailers have become genuine competitive peers, not just price followers.

## A \$100 Billion Challenge?

All of these pressures can be expected to have significant financial implications for food and beverage players, affecting demand, margins, and valuations. UPFs are at particular risk. We see as much as \$100 billion in US UPF revenues that could face disruption as a result of shifts in consumer purchasing behavior, restrictions on food assistance program spending (SNAP alone exceeded \$100 billion in UPF spending in 2024), and changes in food procurement by government institutions. At the same time, costs for manufacturers are set to increase by 5% to 25%, thanks to increased R&D spending on reformulation efforts, a shift to more expensive clean-label ingredients, and rising marketing expenses and legal and compliance costs.

Of course, the ultimate pace and extent of consumer and regulatory change remains to be seen. But it’s already clear that a fast-growing number of both large CPG manufacturers and major retailers are moving to embrace an evolving marketplace:

\- More and more retailers and manufacturers, including Walmart, PepsiCo, Nestlé USA, General Mills, Kraft Heinz, Conagra, Hershey, J.M. Smucker, and Kellanova, have committed to removing artificial dyes in foods, drugs, and cosmetics from US products by the end of 2027.

\- Retailers such as Kroger and Intermarché are employing nutrition scoring systems and are adjusting the formulas of their private-label products (often to satisfy the criteria of apps such as Yuka).

\- CPG companies and retailers are launching “better for you” line extensions of popular brands. UK retailer Marks & Spencer’s “Only…Ingredients” product line offers simplified, clean-label recipes (with eight or fewer ingredients). Separately, a growing wave of nutrient-dense launches across the industry—products with more protein, fiber, and key micronutrients per calorie—is targeting consumers, including GLP-1 users, who are eating less.

\- Large manufacturers are acquiring and investing in health and nutrition brands. PepsiCo acquired prebiotic-beverage company Poppi for \$1.95 billion in 2025.

\- Companies such as Nestlé are resetting the cost base to fund reinvestment in innovation, R&D, and AI. Nestlé expects its Fuel for Growth program to deliver CHF 3 billion in savings by the end of 2027, which the company has been clear will fund accelerated innovation and growth.

Companies that wait for clarity risk falling behind. In a market where expectations are moving faster than legacy portfolios, delayed adaptation can quickly translate into share loss and margin erosion.

## How Companies Can Adapt

The big strategic question involves capital allocation. For the past decade, returning free cash flow to shareholders through dividends and buybacks has been the default value creation tool for many large CPG companies. This model worked well while volume and pricing were dependable. The conversation underway now in many CPG boardrooms is more complex: how to balance shareholder returns with the reinvestment in R&D, new capabilities, and M&A that the next decade will require. Getting this mix right is the main strategic issue of today.

At the same time, companies should pursue a coordinated set of actions across their product portfolios. (See Exhibit 4.)

EXHIBIT 4 How Companies Can Adapt  
![](images/4e1765286e6c56e0a41b1f8f1736efb8663f13494a84d021f5b7e21216b61467.jpg)  
Source: BCG analysis.

Assess brand and portfolio exposure. Companies need to understand where their brands are most exposed. Some products, such as those with ingredients experiencing consumer or regulatory skepticism, face structural headwinds; others may not be affected or may even benefit from shifting demand. Gaining clarity on exposure involves building a robust foresights capability to understand where the opportunities are today—and discerning the still-weak signals that indicate where opportunities could come from tomorrow. A number of AI-powered tools, including several developed by BCG, are available to monitor and assess relevant trends and developments, foster consumer insights, and help build an in-depth understanding of the intricacies of policy and regulation.

(Re)build trust through transparency. As we argued last May, CPG players may want to take a step back and reset their overall direction on nutrition, developing and communicating a transparent and consistent corporate perspective on processed foods and their role in modern diets. Trust is maintained (or rebuilt) through clearer ingredient narratives, visible commitments to improvement, and alignment ahead of evolving policy expectations. Companies need to be upfront and clear about the makeup of their products, their sustainability, the role of each SKU in the portfolio, and the reasons for and benefits of reformulations as they occur. In an environment shaped by AI-enabled transparency, inconsistencies can quickly surface.

(Re)build the innovation engine. Rebuilding the innovation engine is the work of years, not quarters. There are two avenues that need to be pursued in parallel: building or buying into high-potential adjacencies, and disciplined reformulation of the core. Most companies have historically prioritized one or the other; future leaders will do both.

The first avenue is to seek growth in new market segments or demand spaces (the intersection of consumers' current context and their emotional and functional needs). CPG companies can use a demand-centric analysis to rethink products in light of emerging and unmet consumer needs, as well as define new product categories. Execution can take place through internal innovation or M&A. A growing number of big companies are already pursuing the latter route, but it’s important to remember that acquisition is only a starting point and often an expensive one at that. Integration must preserve the agility, culture, and authenticity of the acquired brand(s). There are plenty of cautionary tales of fast-growing brands that were undermined by their new owners.

The second route is reformulating winning products using tools such as BCG's “design to sustainable value” approach. Reformulation is often treated as a defensive response to regulatory or reputational pressure, but this view is too narrow. Leading companies are institutionalizing a more disciplined product design model that does the following:

\- Integrates consumer value, cost optimization, and health and sustainability objectives into one product design logic

\- Differentiates reformulation intensity by product role, occasion, and positioning (not all products should be treated the same)

\- Redesigns formulas and sourcing in parallel to protect margins rather than layering cost onto legacy structures

\- Uses cross-functional, agile teams and advanced analytics to accelerate decision making and reduce execution risk

\- Combines near-term optimization with longer-term category reinvention to future-proof portfolios

\- Explores other innovation models, such as “open innovation” approaches that involve collaboration with academia, venture firms, and other players

UPF categories are under intensifying structural pressure. Incremental tweaks are insufficient solutions; a product line extension here or a clean-label SKU there will not move the needle. The winners of the next decade will be the companies that reshape their portfolios through stronger innovation engines and disciplined M&A and that have the conviction to start before the bill for past strategies comes fully due. For most large CPG players, the first move is straightforward: a brutally honest portfolio diagnosis, done in weeks rather than quarters, that classifies every SKU by its exposure to structural forces in the marketplace. Everything else flows from there.

The authors gratefully acknowledge Dafne Kuisch and Emma Ligthart for their contributions to this article.

## Authors

![](images/03077a4c00f6f3e17965373aef49f3be8005d8a6690858471b209ccee92f84ca.jpg)

![](images/91304a8e164ac53c5be2600689819a06f412fca0e9d7054c0b4250bd672f3488.jpg)  
Alejandro Navarro  
Managing Director & Partner
Amsterdam

![](images/388cbae0e2c33f13a27941a2022258c04593f9e4f2a5f9b58ce40f19d0b19887.jpg)

![](images/2ebb0560a4ee7231c6c9143dac194a65bd61a415e604e349d5287851d8e5143d.jpg)

![](images/b96662d4f2b3bc8408cf44f1f85c0c558e9d37a66ece525492f2b84c8763b521.jpg)  
Senior Advisor
New York

## Brad Jakeman

![](images/fb4e1f94d5f21df72d554d6b33b31bdae2e2a502d67a8231c589bdcafb1ec8fb.jpg)  
Geraldine Rhodes  
Managing Director & Partner
Washington, DC

![](images/bde40fdfca5430752253c0e7dd3a3d85bc77541e7a6871cde72825e6154e0e3f.jpg)  
Nina Peters

Project Leader
Amsterdam

![](images/ad39efe491778d5ee9a7d823c00cbb2b0aca1eb6685f3f7293f1854d185d7d16.jpg)

![](images/636df3ea97c0d982a48e723a57259b4420ae20c95988cded06fd3d79164c6579.jpg)  
Ezgi Sonmez  
Project Leader
London

![](images/0e7d895422b4c1d31ce1ecb7cc0e5564a6f05bcca8f9acafe08fa33a538451e5.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
