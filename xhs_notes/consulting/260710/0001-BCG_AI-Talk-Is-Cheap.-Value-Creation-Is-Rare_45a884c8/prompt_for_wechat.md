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
![](images/f4a2f1e443e380771aeb1fdf889a40c9ed17fa10dc1f2c16addd71b34ed481ba.jpg)

ARTIFICIAL INTELLIGENCE

# AI Talk Is Cheap. Value Creation Is Rare.

By Ulrich Pidun, Adam Job, Tania Wang, Matthew Molloy, Michael Grebe, Marc Roman Franke, and Viacheslav Romanov

ARTICLE JULY 09, 2026 12 MIN READ

AI talk dominates corporate communications. In a recent BCG analysis of 4,800 quarterly earnings calls, it was the most-mentioned topic by CEOs globally. But which companies are translating that talk into measurable performance—and how?

Most evidence on AI adoption today comes from these communications or from self-reported surveys. Both have limitations: corporate communications reflect what company leaders think investors want to hear, and surveys reflect what companies say about themselves. To cut through the noise, we developed an outside-in measure of AI adoption and applied it to more than 600 US public companies. Our findings push back on three threads of the public conversation around AI:

\- The public narrative is that AI adoption is widespread and that companies are seeing real benefits from it. An $FT$ analysis of S&P 500 filings found 75% of companies mentioned AI on earnings calls in the past year, with 87% of those mentions wholly positive. In contrast, we find that only 6% of firms in our sample qualify as real adoption leaders. But this select group is capturing meaningful value from AI, with industry-adjusted total shareholder returns (TSR) over the past three years running 9 percentage points above median.

\- Many analysts argue AI value is a hype story driven by investor exuberance rather than fundamentals. But among the leading 6%, return outperformance is driven entirely by fundamentals—revenue growth and margin expansion—not by higher price-to-earnings (P/E) multiples.

\- Public discourse frames AI as a tool for increasing efficiency and reducing headcounts. The recent wave of layoff announcements referencing AI reinforces this narrative. However, among the leading 6%, the dominant path to value generation is growth, not efficiency—and these firms are increasing headcount at a 3 percentage points higher compound annual growth rate (CAGR) than the median firm in our sample (between 2022–2025).

What's more, by studying AI adoption leaders, we've traced their journey—identifying the strategies that enabled these companies to translate AI into competitive advantage.

# Identifying the AI Adoption Leaders

Our AI adoption score is built around three pillars:

\- AI tech—the off-the-shelf tools a company is using and its underlying tech stack enabling the development of bespoke solutions.

\- AI talent—the share of employees in AI-specific roles, building solutions, and the prevalence of AI-related skills across the workforce.

\- AI deployment—the breadth of functions where use cases exist and the depth of these on a spectrum from exploratory pilots to enterprise-wide production.

## - How We Measure AI Adoption

Our AI adoption score is grounded in the resource-based view of the firm, which treats AI capability as a higher-order construct combining technological, human, and intangible organizational resources. $^{1}$ The three pillars of our score—AI tech, AI talent, and AI deployment—map directly onto these three categories of resources.

Six equal-weighted indicators sit beneath the three pillars:

\- AI tech captures both the off-the-shelf AI tools a company uses and the underlying infrastructure that supports them. Two indicators: the strength and number of AI vendors in the company’s ecosystem, and the share of the firm’s tech stack composed of products that enable AI development. This pillar represents the technological-resource dimension of AI capability.

\- AI talent captures both specialists and broader workforce fluency. Two indicators: the share of employees in AI-specific roles, and the prevalence of AI-related skills across the broader workforce. The human-capital dimension has been linked to firm growth and productivity in prior work. $^{2}$

\- AI deployment captures both how widely and how maturely AI is being used—the intangible-resource dimension that determines whether technology and talent are actually translated into organizational use. Two indicators: the breadth of functions in which AI use cases have been documented, and the depth of those use cases on a six-step spectrum from discussion-only through pilot and early deployment to enterprise-wide production. This dimension follows prior research measuring AI usage as a combination of breadth and depth and linking it to innovation and growth outcomes, as well as work emphasizing that scaling AI from pilot to production is a critical determinant of whether AI investments yield value. $^{3}$

Talent indicators are based on labor-market data from Revelio Labs (derived from LinkedIn resumes). Tech indicators draw on IT-installment data from HG Insights. Deployment indicators are derived from natural-language analysis of annual 10-K filings and quarterly earnings calls.

For each indicator, companies in our sample are stack-ranked and assigned a normalized score from 0 to 100. The three pillar scores are then averaged with equal weight to produce the overall AI adoption score. The measure is applied to more than 600 US public companies with a market capitalization above \$5 billion.

TSR findings in this article are reported on an industry-adjusted basis—each company is compared against the median in its own industry.

The methodology was developed in collaboration with Cindy Laura Stahl, a researcher at the University of St. Gallen.

The scores across pillars are averaged to arrive at an overall metric. Applying our measure to a sample of publicly listed US companies, we classify companies as falling into one of four tiers on AI adoption: nascent, emerging, active, and leading. (See Exhibit 1.)

## EXHIBIT 1

The Value of AI Adoption Is Concentrated in the Top 6%

![](images/1f6dda1db98b8e88a284163abb7097d9e5745079f5353c5af07479b216a6d9ac.jpg)  
Sources: S&P Capital IQ; BCG Institute analysis. $^{1}$ TSR for December 2022–December 2025, relative to industry median in sample.

Only 6% of companies are AI leaders, but they are seeing real value. Industry-adjusted TSR over the past three years runs at +9.3% for the leading tier vs. sample median. This is a clear premium over the laggards (-1.7%). The even more striking finding is the gap between leaders and the active tier sitting just below them: active firms see essentially no premium (+0.6%), meaning the value accrues only at the very top, and not progressively along the adoption curve. In other words, the impact of AI adoption on value creation emerges in a step change fashion, not linearly.

The AI adoption leaders in our sample are concentrated in the tech sector, but breakout performers exist across industries. More importantly, the TSR lift cannot be dismissed as a “shovel-seller” effect: the numbers we find are industry-adjusted, meaning that leaders outperform the median company in their own industry. Technology leaders are compared to the technology median, not to the broader market.

One might worry that the TSR advantage of AI leaders is driven by market enthusiasm—investors bidding up AI-associated stocks based on future expectations rather than real business results. To address this, we decomposed the TSR outperformance of leaders (compared to laggards, the bottom two tiers of our sample) into its components. (See Exhibit 2.) This analysis shows that the outperformance is driven almost entirely by fundamentals: revenue growth and margin expansion (+10 percentage points and +6 percentage points respectively, both industry-adjusted). Meanwhile, P/E multiple expansion—the channel through which “AI hype” would show up—contributes essentially nothing.

## EXHIBIT 2

AI Leaders' Returns Driven by Fundamentals, Not Hype

![](images/5b9e63d31ac6444ae316d2ca9bf9a8d20e63272a8387d10aeb7722bf142a122e.jpg)  
Sources: S&P Capital IQ; BCG Institute analysis. $^{1}$ TSR for Dec 2022–Dec 2025; difference in median TSR of leaders vs. laggards. $^{2}$ Including residual effects (-2pp).

The conclusion here is that the market is rewarding real business performance, not narratives about AI's future impact. Notably, these effects also hold when we compare TSR of leading companies against active companies.

An additional driver worth noting is that leaders show a negative TSR contribution (-5 percentage points) from cash effects (consistent with equity issuances and/or reduced dividends). Thus, the leaders are not extracting cash—they are using it to fund AI investments.

AI Leaders Are Seeing a Productivity Dividend

The productivity engine behind the value. Underlying this fundamental performance is a productivity advantage: revenue per employee is growing 4 percentage points faster at AI leaders than at laggards, on an industry-adjusted basis. (See Exhibit 3.) This gap emerged with the release of foundation models in late 2022, which made AI broadly useful across functions. It widened in subsequent years and remains sizable today.

## EXHIBIT 3

Annual productivity growth $(\%)^{1}$

![](images/8b694872e2a0fd62c62911500f166455a459c380266336a121a81f2b20c37873.jpg)  
Sources: S&P Capital IQ; BCG Institute analysis. $^{1}$ Productivity is measured as revenue per employee (based on headcount).

The fact that this productivity advantage is concentrated in 6% of the sample helps reconcile a broader puzzle: some economists have noted that AI has not shown up in aggregate productivity data. This is consistent with our findings: averaging leaders together with the 94% of companies that have not reached comparable adoption levels washes out the real, sizable effects happening within a small group.

For CEOs, this raises an obvious question: How are these leaders deploying this productivity to create higher value than peers?

# What AI Leaders Do: Save, Scale, Innovate

We observe three distinct ways in which AI leaders create value, differentiated by whether they use AI to improve margins, accelerate growth, or both. (See Exhibit 4.)

Most Leaders Use AI to Do More, Not Less  
![](images/19ad285380f80e68f0d8b5c03d6b3e950aab3929eeca9d2edc50538fb0c5697b.jpg)  
Sources: S&P Capital IQ; BCG Institute analysis. $^{1}$ Headcount CAGR for 2022–2025, relative to industry median in sample. $^{2}$ Relative to industry median in sample.

Do the same with less. The most intuitive path is to use AI to streamline operations, automate back-office processes, and expand margins at the functional level. For example, IBM, an AI leader in our sample, has automated its HR support function with an AI agent called AskHR, which now handles over 94% of employee requests and contributed to a 40% reduction in HR operating costs over four years.

This is the path many executives instinctively associate with AI, and the one that dominates the public narrative around automation and job displacement. Yet among leaders, it is the least common path—only 10% follow it. This is because a focus on efficiency is an entry point. It enables quick wins, building organizational experience with AI, and proving the case for further investment, but not an end state. Doing the same things faster is unlikely to yield durable competitive advantage when the underlying technology is widely available, and leaders recognize this.

Expand what each employee can deliver. The second path is using AI to create scale. This is where the largest share of leaders, 59%, concentrate their efforts—and it is the best approach for converting AI’s productivity gains into competitive advantage. By making each unit of work more productive, leaders can serve more customers, accelerate throughput, enter adjacent markets, or reach segments that were previously uneconomic to serve—unlocking both margin expansion and revenue growth simultaneously.

For example, Salesforce, an AI leader in our sample, reports that service agents using AI spend 20% less time on routine cases, freeing roughly four hours per week for higher-value issues, which is projected to boost upsell revenue by 15%.

The common thread among leaders is that productivity gains are reinvested into the business rather than translated into cost cuts. This is consistent with BCG research on AI's labor market impact, which finds that the main effect of AI on work is augmentation—making people more productive—rather than substitution. When productivity rises in roles where demand can expand, companies tend to grow output rather than shrink headcount. Consistent with this, AI leaders in our sample are growing headcount 3 percentage points faster on average than laggards.

Build new products, services, and business models. The most ambitious path, taken by 21% of leaders, is using AI to innovate. These firms are creating offerings that would not have been possible or economically viable without AI. The strategic posture is different from the efficiency path: it requires a willingness to invest in new business models, accept a temporary margin trade-off, and bet on revenue streams that do not yet exist.

We see multiple leading companies in our sample pursuing an innovation strategy. For example, Meta has built AI marketing tools that generate creative assets tailored both to the product being advertised and to the user being advertised to. Moody's is leveraging its proprietary data on credit ratings, financial data, and risk models to build new analytical offerings for customers.

## Becoming an AI Leader

Save, scale, and innovate describe what leaders do with AI once they’ve reached the top. But how do they get there in the first place? To trace the journey, we examined how the three pillars of our score—AI tech, AI talent, and AI deployment—evolve through the adoption tiers. Across the 600+ companies in our sample, a recognizable pattern emerges, with three key transitions that separate the starting point from the leader tier. (See Exhibit 5.)

## EXHIBIT 5 The Journey to AI Leadership

Median score per pillar across firms in each adoption tier (0–100 scale)

![](images/7240edc2ca656cc9a8267dd008976cba53f7e925220578181a263e499ecffcc2.jpg)  
Source: BCG Institute analysis.

Starting Point. Most companies begin their AI adoption journey by acquiring off-the-shelf AI tools and running experiments in a small number of functions, typically focused on efficiency use cases for which off-the-shelf tools are readily available.

Transition 1: Expanding the Toolkit. Progressing from this starting point involves expanding scope: moving beyond a narrow set of general-purpose tools toward a broader, more specialized AI ecosystem, and making the tools accessible to a wider set of functions and use cases. In this phase, organizations are still buying tools, not building their own. It remains an important learning phase—companies experiment to discover what works and what their scalable AI stack will need to look like—and some get stuck running an ever-expanding set of disconnected pilots.

Transition 2: Going Broad and Deep on Deployment. The next step is to go deeper, converting pilots into production-grade deployments starting in a few functions, building reusable platforms and playbooks there, then scaling breadth as the marginal cost of each new deployment falls. Across this transition, the share of companies that are simultaneously broad (use cases covering eight or more functions) and deep (at-scale deployment) in their AI deployment grows from roughly 12% of the cohort to over 50%. Walmart, started by going deep in demand forecasting, then used it as a foundation that fed downstream applications across the supply chain—inventory management, warehouse robotics, store operations, and last-mile delivery.

Transition 3: Crossing the Talent Gap. Mastering the first two transitions means a firm has built operational and technical foundations, but our data shows this is not yet enough to capture AI's productivity and value benefits. One more transition remains, and it is the one that matters most: the talent gap. Across the three pillars, tech and deployment scores barely change between the active and leading tiers. Meanwhile, the talent score nearly triples.

But “talent” should not be read narrowly as “hire AI developers.” What leaders do is broader. For one, they invest in talent breadth: AI fluency across the organization, going beyond core AI specialists. At leaders, 13% of employees have AI-related skills, compared to 1% at laggards. Consistent with this, BCG research finds that leading companies upskill a significantly larger share of their workforce in AI skills than laggards. The goal is for teams across the organization to be able to identify where AI changes the economics of their business or function and co-design solutions, rather than waiting for a central team to deliver them. When AI fluency is distributed, the organization develops a richer pipeline of use cases than any central team could generate alone.

Moreover, leaders invest in talent depth: AI-specific positions reach 3.5% of the workforce at leaders, versus 0.1% at laggards. These dedicated specialists scale solutions identified or prototyped across the business into proprietary, enterprise-grade capabilities.

Crucially, this talent transformation does not happen organically. It requires deliberate organizational change: rethinking workflows end-to-end rather than bolting AI onto existing processes, establishing joint ownership between business and IT, and shifting the center's role from building all AI solutions to curating, governing, and amplifying the best ones.

This is consistent with what BCG has long observed about successful AI transformation, often summarized as the 10-20-70 rule: roughly 10% of the effort is technology, 20% is algorithms and data, and 70% is people, processes, and organizational change.

The reason talent is decisive at this stage is that tools have commoditized; every company can buy the same AI products from the same vendors. What cannot be bought is the organizational capability to deploy them into the specific economics of a business.

## Walking the Walk on AI Adoption

AI is inescapable in corporate communications and public conversation, and for good reason. Our analysis reveals that companies that talk about AI are rewarded with higher P/E multiples at every level of real adoption. For example, laggards discussing the technology in earnings conference calls see a 1 percentage point lift in P/E multiple contribution to TSR vs. peers that stay quiet. Investors clearly want to see firms engaging with the technology, and signal that engagement back through valuation.

Yet the real benefits of AI we observe—the return premium, the improvement in fundamental performance, the productivity benefits—come not from talking the talk, but from walking the walk. Of course, adoption alone is not replacement for a good strategy. This is evidenced by the fact that a small minority of leaders (10%) in our study are failing to translate AI into fundamental performance gains: they are experiencing declining margins and growth. But a closer look reveals that these companies are held back by fundamental business model challenges that AI cannot overcome, such as core offerings being commoditized, or legacy business models displaced by digitally native disruptors. These cases offer a cautionary note: AI amplifies a strong strategy; it does not substitute for one.

When this strong foundation exists, our data shows that senior leaders need to build the talent base to create proprietary capabilities around AI, the organizational architecture to deploy it across the business, and the ambition to use the resulting productivity gains for competitive advantage rather than cost cuts. This is what separates the 6%.

The BCG Institute is Boston Consulting Group's strategy think tank, dedicated to exploring and developing valuable new insights from business, technology, and science by embracing the powerful technology of ideas. The Institute engages leaders in provocative discussion and experimentation to expand the boundaries of business theory and practice and to translate innovative ideas from within and beyond business. For more ideas and inspiration from the Institute, please visit our website and follow us on LinkedIn and X (formerly Twitter).

## Authors

![](images/2a85416273e268428074a21f9c025022d2f6b09288bf5bd04d6196f4c27f290a.jpg)

![](images/01ca905b2b10304dcf927e725aeceebd26bcef280493dbba571f69a908e7b128.jpg)

![](images/f48c8d8725e875069920e47a4a2e57cbb34926cc7f6dcd1952014bb09ebc3d84.jpg)

![](images/9975c1464b174e3a49b0ac9c5295648f052038158c091e5a7688ba85a678be9a.jpg)  
Partner & Director; BCG Institute Insight Leader
Frankfurt

## Ulrich Pidun

![](images/246bcdb887cbbb7fa755bf97df628ee9e129daf18b10b8872c3d4af2f417d95e.jpg)

## Tania Wang

Lead Forward Deployed AI Scientist
Los Angeles

![](images/6c9054675ecfd3feaf3eaedba1c5739079e3c5805adf92fa4ab2371c2f004312.jpg)

## Michael Grebe

Managing Director & Senior Partner
Munich

![](images/3932fec0331667932ebaa6c4b2017685ff1f5ffebe0141d88f17748104337fc9.jpg)

## Viacheslav Romanov

Partner & Associate Director,
PIPE Tech Capital
Boston

![](images/9e8b474191f8e9381c2f6c910157db334e598ca3ae52968dfacd38a69a7c2c30.jpg)

![](images/f1e47c6064410ba4a738e8d173eefe22d20aa6bb4442d487bdcc2e2ed81f39e5.jpg)

![](images/b6be86c682afb562fb588b31223b4049273a51a9c47a716292e383d37837925f.jpg)

![](images/2eea7ddebb1574d68a4716d2580d20d10d0c51ea3ff245dfaa1d79ef165c7748.jpg)

## Adam Job

Senior Director, BCG Institute
Frankfurt

![](images/2b0210c763902d874db832f9800d8965f198e3358267120029b91d744e792e34.jpg)

## Matthew Molloy

Project Leader
New York

![](images/0832db801a69dcf16599b5f946257752177d82b9f1311b7092b4ea0c707b6bf9.jpg)

## Marc Roman Franke

Partner & Associate Director, AI and digital transformation
Berlin

![](images/eb1791a2c3524d707c1f77b332fe65509702a58a320fc45f0b755e9ed5ae38c8.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
