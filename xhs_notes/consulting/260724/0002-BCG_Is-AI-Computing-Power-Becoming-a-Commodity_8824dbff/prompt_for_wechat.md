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
![](images/694e063a073b68ff6c24c2d2fc03518e2494e373f7a1e9e8521ac8ce299408d8.jpg)

ARTIFICIAL INTELLIGENCE

# Is AI Computing Power Becoming a Commodity?

By Antti Belt and Allen Thomas

ARTICLE JULY 23, 2026 15 MIN READ

The economics of enterprise AI are shifting fast. Until recently, flat-rate subscriptions allowed large enterprise users of AI tools to focus more on driving uptake than on managing the costs of AI. But that flat-fee era for enterprise users has ended, as AI labs such as Anthropic and OpenAI have shifted to metered pricing. The next development is likely to be dynamic pricing, under which prices surge at times of peak demand. For end users, the implication is clear: AI cost exposure is rising.

Meeting that challenge will require a fundamental evolution in today's market for AI computing power (known as “AI compute”), away from heterogeneous contracts, opaque pricing, and limited tools to a system that is more liquid and transparent. How far the market moves toward complete commoditization is uncertain, owing to notable headwinds—among them the fact that AI compute is heterogeneous, varying across hardware generations, timing, and geography. But a shift is undoubtedly under way, and benchmarks and futures contracts for AI chip rentals are already emerging to enable price transparency and risk management.

As the market grows more liquid and efficient, it creates opportunities, not only for end users but also for data center players, AI labs, and other large users of AI compute. All told, BCG Institute estimates that this change could unlock as much as \$140 billion in annual “dark value”—value that exists in virtually every industry due to inefficiencies in the supply and demand of capital, goods, and services. (See Exhibit 1.) In the AI compute market, dark value is likely to concentrate in two primary areas:

\- Price optimization and trading across the three primary components of the market: AI chips—largely graphical processing units (GPUs)—AI compute rental rates for those chips, and end user tokens

\- Lower borrowing costs for data center players

Players that move early will be in the best position to adapt to a rapidly changing market and unlock dark value in the AI compute market.

## EXHIBIT 1

AI Market Evolution Can Release up to \$140 Billion of Value

DARK VALUE (\$BILLIONS)

![](images/5ef0f6543b8a3502029034f421d64b1d9a3010c1280f0b71effce0222cfa9692.jpg)  
Sources: LSEG; Goldman Sachs Global Institute; BCG analysis.

# The Challenges of Today's Market for AI Computing Power

The market for AI compute is growing at a breakneck pace. BCG analysis projects that it will climb from \$360 billion in 2025 to roughly \$2.3 trillion in 2030. Yet players across the ecosystem face a number of structural challenges that a more liquid, transparent market could help address.

## AI End Users: Increasing Exposure to AI Cost

As pricing approaches evolve, end users are increasingly exposed to the wholesale market for AI compute that undergirds AI models.

End-user tokens are just a way of representing AI compute use. Every time an AI model provider like Anthropic or OpenAI answers a query, it uses AI compute, which has a cost. But until recently, flat subscription pricing largely insulated end users from the true costs of AI. To manage surges in end user demand, AI providers didn't raise prices; instead, they controlled demand directly. When AI compute capacity tightened, providers responded with rate limits, queue delays, or outright throttling. Users experienced worse service but ultimately paid the same flat subscription regardless of conditions.

More recently, many providers have shifted to metered pricing. Anthropic began moving enterprise customers to a \$20-per-seat base fee plus pay-per-token API rates in April 2026. The company explicitly tied the change to deepening crunch for AI compute. Similarly, OpenAI moved Codex from flat-message pricing to token metering in early April, GitHub tightened Copilot limits days later, and Windsurf replaced flat credits with hard weekly limits in March.

The next step in the market's evolution could be dynamic token pricing, where the price of inference (the computational process of running a trained AI model to generate a response) moves with the underlying supply of and demand for AI compute, much as wholesale electricity prices rise on hot afternoons and fall overnight.

With tokens, dynamic prices would reflect both demand-side workload characteristics and supply-side conditions. On the demand side, not all inference loads are equally valuable: a real-time customer-facing agent running at 9:00 AM and an overnight batch summarization job should not clear at the same price. On the supply side, available AI compute capacity fluctuates continuously. Buyers that can tolerate latency or can schedule work flexibly will pay less; those that need guaranteed throughput at a specific moment will pay a premium.

This market would work efficiently in a setting where models are substitutable. For example, a developer building a chatbot, a summarization tool, or a coding assistant can often run it on Claude, GPT, or an open-source alternative with comparable results. That keeps competition strong and ties prices closer to the provider's actual cost of AI compute in the moment.

However, not all AI activity is substitutable. Deeper ecosystem integration—such as for custom silicon, fine-tuned models, data residency arrangements, and enterprise support agreements—creates switching costs that remove the substitutability on which spot market discipline depends. In these cases, token prices will reflect negotiated relationship value as much as marginal costs for AI compute, and they will behave less like wholesale electricity and more like a long-term utility contract: stickier, less transparent, and less responsive to real-time supply conditions.

As enterprises scale their AI usage, a more developed market will help them adjust to dynamic pricing by adopting several practical measures:

\- Time flexible workloads strategically. For substitutable, latency-tolerant jobs, enterprises should treat AI compute as they would any commodity that has predictable price cycles—scheduling batch work, model evaluations, and non-urgent processing to run when spot prices are low.

\- Use futures markets to manage price risk on nonflexible workloads. In situations where enterprises can’t defer timing but providers remain substitutable, enterprises need visibility into real-time prices for AI compute and into financial instruments to hedge against cost volatility.

\- Scrutinize committed capacity arrangements. For mission-critical workloads where the cost of switching providers is high, enterprises need to understand what they are actually paying for lock-in. It is crucial to negotiate committed capacity terms with full awareness of their alternatives and to avoid sleepwalking into pricing that is detached from the underlying costs of AI compute.

## AI Labs and Other Large Users of AI Computing Power: Risk Management and Price Discovery

AI labs, including Anthropic and OpenAI, need vast amounts of AI compute to train new frontier models and to run end users' inference workloads. Today's market structure presents them with two challenges.

First, price discovery is limited. The listed prices that are readily accessible on the websites of AI compute providers rarely match the real transaction price. Often, for AI labs and other large users of AI compute (such as autonomous vehicle players and biotech companies), providers strike prices bilaterally through negotiated discounts, reserved capacity commitments, and enterprise agreements that happen off-market and go unreported. Other markets have successfully created price discovery by establishing benchmarks. Price reporting agencies in markets such as crude oil collect real transaction data from market participants, standardize it, and publish it as a reference that the rest of the market can price against. A solid benchmark for AI compute would enable AI labs to assess whether they are paying a fair market price. At the same time, it would establish a reference price for futures markets while laying the foundation for price-indexed agreements, where fees track real supply and demand rather than trapping buyers in flat rates that are disconnected from market conditions.

Second, AI labs and other large consumers have limited tools for managing supply and price risk. That’s why they are not just buying what they need today, but instead striking long-term bilateral agreements that lock in capacity at fixed or predictable rates well before they know exactly how much they will need.

This race to lock up supply is evident in data center vacancy rates of 1%, with roughly 92% of new capacity already precommitted before it is even built. But the utilization rate for some GPU clusters that enterprise users of AI compute rent or own can be as low as 5%, according to Cast.AI. Utilization is likely much higher at leading AI labs, but even there the issue does not disappear entirely. That can look inefficient from the outside, especially when some capacity is consistently underused. But from the buyer's point of view, the alternative may be worse. Undercommitting could mean not having enough AI compute to train the next model, serve the next wave of users, or keep up with competitors.

Those long-term contracts also help address price risk. According to the Silicon Data H100 rental index, the price of an H100 GPU has risen about 2.2% per month since January 2025. Over that same period, prices fell by as much as 11% at one point and rose to roughly 25% above their starting level at another.

A more developed market would enable two critical types of risk management:

\- Supply Risk Management. In other markets, companies use long-term bilateral contracts for baseline supply planning, while a liquid short-term market lets buyers flex capacity up or down as demand changes. A secondary market enables this flexibility in both directions: companies that need more supply can buy it, and those with too much can sell the excess. The market for AI compute does not yet work that way.

\- Pricing Risk Management. In commodities markets, futures allow firms to manage price risk by locking in future prices without physical procurement of commodities such as oil, gas, or wheat. A liquid financial market for AI compute would allow AI labs to better manage price volatility risk by hedging future costs of such power.

## Data Center Players: High Borrowing Costs

Until now, the AI data center market, being young, has relied heavily on financing via hyperscaler equity and cash flow. But as the market matures, the need for debt financing is likely to grow quickly. Hyperscalers and neoclouds today borrow at relatively high interest rates to cover their data center investments. Lenders prefer predictable cash flow and minimal performance risk, but AI data center financing today breaks both requirements.

To understand why, consider the assets that secure data center loans today: GPU hardware and customer rental agreements. GPUs have uncertain residual value because they depreciate rapidly as new generations ship roughly every two years. Rental rates in customer contracts, meanwhile, have been volatile, with H100 hourly rates falling from around \$8 per hour at a peak in early 2024 to \$1.96 per hour by late 2025 before climbing back to \$2.64 per hour in April 2026. In addition, these customer contracts often concentrate in one or two counterparties, magnifying the impact of any single renegotiation or default.

The emergence of forward markets for both GPU residual values and rental rates could change the equation by enabling two things:

\- Hedging Residual Value. Without a market view on future residual value, lenders guess at depreciation and lend conservatively, keeping loan-to-value covenants tight and rates high. Establishing a forward curve for AI chips would permit data center players and lenders to hedge residual risk directly.

\- Hedging Rental Rates. Rental revenue services a company’s debt while the business is running. A liquid forward curve would allow companies to strike standardized contracts, giving them the same degree of revenue certainty that they now garner via large offtake agreements.

Ultimately, the development of such financial tools would translate into lower borrowing costs, enabling data center players to reallocate capital toward building more data center capacity.

## The Dark Value Opportunity

As the market for AI compute evolves, data centers, AI labs, and large end users will have access to new mechanisms for managing their investment and spending. Those mechanisms will enable them to unlock dark value in two areas: arbitrage and lower borrowing costs for data center players.

## Optimization and Trading

BCG's dark value research, finds that 3% to 4% of total market size in any industry is available for capture through arbitrage—an opportunity that arises from a market's complexity. Applied to an expected \$2.2 to \$2.4 trillion AI compute market by 2030, this implies a potential annual value of \$66 billion to \$97 billion.

That value is distributed across the market's three primary components:

\- AI Chips. This segment could yield \$12 billion to \$17 billion in annual dark value. Data center players would capture much of it.

\- AI Compute Rental. Rental of this sort is typically measured in GPU-hours. The total annual dark value would come in at \$22 billion to \$34 billion. AI labs and large AI compute users would be the primary beneficiaries of this value.

\- Tokens Consumed by End Users of AI Applications. Large enterprise users would be in a position to be well positioned to collect most of the annual dark value of \$32 billion to \$46 billion in this area.

Our estimate does not assume that everything will be optimized and traded. After all, most buyers of AI compute run AI workloads, and depending on the workload, arbitrage—especially geographic arbitrage—may not be feasible in practice for many of them. Some workloads cannot be transferred to a data center in another region, owing to cost constraints (data transfer fees can erase savings) or to the need for real-time turnaround. (See Exhibit 2.) This constraint may become less relevant over time, however, as companies such as Lumen Technologies advance AI infrastructure to support high-capacity, low-latency networking for moving massive AI data sets.

## EXHIBIT 2

Arbitrage Opportunity Depends on Workload Portability and Latency Requirements  
![](images/23226fb303362b7a13dd0be83b213152bc0ec22868450873525834d24c5b75cd.jpg)  
Note: API = application programming interface; NAS = neural architecture search; RAG = retrieval-augmented generation; RLHF = reinforcement learning from human feedback.

## Reduced Borrowing Costs

To estimate the potential financing savings for data center players, we drew on loan data from LSEG/Refinitiv. First we volume-weighted investment-grade loans to calculate the average spread over the secured overnight financing rate (SOFR). Then we analyzed a subset of data center companies, including CoreWeave and xAI, to estimate spreads specific to AI infrastructure.

Assuming a \$3.6 trillion investment in AI infrastructure from 2026 through 2030, we compared interest costs with no forward curve for AI compute versus an environment with a reliable forward curve. Under both scenarios, we held the financing structure constant: 70% loan-to-value, 4.5-year amortization (the median investment-grade tenor), and SOFR at 3.6%. (See Exhibit 3.)

## EXHIBIT 3

Lower Interest Rates Can Save Data Center Players \$116 Billion over the Next 4.5 Years

<table><tr><td></td><td>Without forward curve</td><td>With forward curve</td><td>Difference</td></tr><tr><td>All-in interest rate</td><td>6.43%</td><td>4.75%</td><td>1.68%</td></tr><tr><td>Interest as a percentage of principal</td><td>17.7%</td><td>13.1%</td><td>4.6%</td></tr><tr><td>Interest across $3.6 trillion buildout</td><td>~$446 billion</td><td>~$330 billion</td><td>$116 billion</td></tr></table>

\~\$26 billion saved per year, redeployable into added capacity  
Source: BCG analysis.  
Note: Assumptions: \$3.6 trillion buildout (2026–2030); 70% loan-to-value; 4.5-year amortization; secured overnight financing rate at 3.6%.

# Headwinds to the Development of a Liquid AI Computing Power Market

Companies have made some moves to evolve the market. Amazon Web Services, for example, launched EC2 Spot Instances in 2009 as a bidding market for unused capacity, but it later shifted to a model based on long-term supply and demand for spare capacity. More recently, independent venues such as SF Compute have pushed the idea further by building a marketplace for GPU clusters with resale built in.

However, several factors have made such efforts—and the overall shift toward a more efficient market—challenging:

\- Technical Complexity. AI compute differs along three dimensions. First, it can be cheaper or more available at certain times (for example off-peak hours, periods of low demand, seasonal lulls, or demand spikes immediately after the launch of a new AI model). Second, it can vary in quality. An H100 does not deliver the same performance as an H200. And non-GPU expenses such as CPU computing power, networking, storage, orchestration software, and support are often hidden, as are provider-specific factors such as downtime, setup time, debugging time, and the performance tuning required for networking and storage. Third, AI compute costs and availability differ by geographic location. (See Exhibit 4.)

\- Lack of Consensus Benchmarks. A trusted benchmark for AI compute would enable all players across the ecosystem to compare offers, evaluate GPU-backed assets, or build the financial products to hedge price risk. In mature commodity markets such as oil, benchmarks may differ but they still give participants a common view of price. Benchmarks for AI compute are beginning to emerge, including the Ornn H100 Index and the Silicon Data H100 Rental Index, among others. But each benchmark uses a different methodology to collect data and normalize pricing on the basis of heterogeneous AI compute. As a result, the same GPU on the same day can fetch significantly different prices across indices. (See Exhibit 5.)

\- Capital Availability. Although many AI labs and AI services companies are not yet highly profitable, equity funding is still available; and although debt is costly, they can often find alternatives. As a result, managing price risk has only recently become a

[中间内容因长度限制已省略]

favorable price movements. It would also strengthen the connection between long-term contracted capacity and near-term spot pricing, making the benchmark more robust by expanding the pool of observable transactions.

# Recommendations for Players Across the Ecosystem

We believe that all stakeholders need to prepare for a world of increasingly dynamic pricing, greater transparency, and a more sophisticated financial layer around physical AI compute. The specific actions that each stakeholder will take, however, differ.

## AI End Users

As AI labs shift toward metered and dynamic pricing, large AI end users can take three actions to manage their cost:

\- Tier demand into separate baseload and flexible categories. AI end users should identify workload tiers—including high-value, customer-facing applications (baseload demand) that must be served regardless of price—and background tasks (batch summarization, internal research, and report generation) whose requirements are more flexible.

\- Hedge baseload demand. Enterprises with large and growing AI cost lines should treat AI compute the same way they treat energy or foreign exchange exposure: by hedging systematically where doing so is material to earnings.

\- Throttle flexible demand. End users can throttle, delay, or reroute flexible workloads when prices spike. In a price shock, companies should be in a position to scale down flexible consumption while preserving baseload.

## AI Labs and Other Large AI Computing Power Users

AI compute is the single largest cost line for most of these players, often consuming a substantial share of early-stage capital. Managing that exposure actively, rather than treating it as a fixed input, is a strategic necessity. Several strategic steps are available:

\- Structure contracts to match exposure. As benchmarks become trusted, buyers should push for indexed pricing (for example, “OCPI H100 + differential”) rather than fixed rates for long-term commitments. At minimum, buyers should use existing benchmarks to pressure-test and negotiate fixed-rate agreements so they aren't flying blind in their efforts to gauge fair value.

\- Manage AI compute exposure across the contract life cycle. Long-term fixed-rate contracts reduce price volatility during the term but introduce other risks, including renewal cliffs, exposure to spot pricing for overages, and potentially being locked into paying above market prices if overall prices fall. As benchmarks and derivatives mature, financial instruments tied to indices can hedge renewal risk, cap overage costs, and offset losses on above-market contracts.

\- Arbitrage across time, quality, and geography. As switching costs fall and AI chip substitutability increases, AI labs and other AI compute users should prepare to route workloads on the basis of price signals. Batch jobs can run overnight or in lower-cost regions; non-latency-sensitive training can move to off-peak windows.

\- Optimize model and provider selection. Substitutability across frontier models creates real optionality. Routing each workload to the provider and model that offer the best price-performance at a given moment, rather than standardizing on a single vendor, can capture savings with minimal loss of quality.

## Data Center Players

Data centers sit at the supply end of the market and stand to benefit most directly from the development of forward curves and financial instruments. They should make the following moves:

\- Use forward curves to lower financing costs. If residual-value and rental-rate benchmarks gain liquidity, data center players should incorporate them into underwriting. They can present lenders with rental revenue and AI chip residual value projections on the basis of forward curves rather than bottom-up forecasts, compressing credit spreads toward those savings.

\- Hedge residual value and rental rate risk. Another smart step is to transfer the two core balance-sheet risks (hardware depreciation and rental rate volatility) to financial counterparties as derivatives markets develop. By hedging in this way, data center players can offset their losses if GPU prices fall or rental rates drop.

![](images/ac78528769fe82a2fd855ce495110a039d83c452fb5fd8e470e585f58957e9e9.jpg)

The market for AI compute is changing quickly, with benchmarks, futures contracts, and secondary markets already beginning to emerge. Whether the market moves toward true commoditization is a question mark. But the shift toward greater liquidity and transparency is unstoppable. Early movers—whether end users managing cost exposure, data center players unlocking cheaper financing, or AI labs securing supply—stand to capture disproportionate value as this shift unfolds. The era of opaque contracts and flat-rate pricing is ending. The question now is who will seize advantage in the new landscape.

## Authors

![](images/fcfef621246430e29a29ecc529be59e803111968fad3a1936c372a33c284400e.jpg)

Antti Belt

Managing Director & Senior Partner; BCG Institute Fellow Helsinki

![](images/124b411e853308c40ed3c0a878e41ffb76c8a8596b87f000cfddf4442bd5dfd8.jpg)  
Allen Thomas  
Consultant Chicago

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
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
