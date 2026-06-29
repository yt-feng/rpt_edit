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
BOARD BRIEF

# AI in CPG and Retail: How Winners Are Pulling Ahead

A Collaboration of the Consumer Goods Forum and Boston Consulting Group

By Mai-Britt Poulsen, Nicolas de Bellefonds, Yotam Ariav, Nate Shenck, and Arnaud Bassoulet

## Boston Consulting Group

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

## The Consumer Goods Forum

Guided by the vision “Better Lives Through Better Business”, The Consumer Goods Forum (CGF) is the only CEO-led, global organisation that unites retailers and manufacturers to drive positive change across the consumer goods industry.

With a unique model grounded in pre-competitive collaboration, we bring together the world's leading companies to tackle shared challenges such as sustainability, human rights, food safety and product data. Our global network offers unparalleled access to insights, best practices, and a thriving community committed to securing consumer trust, delivering greater impact and supporting sustainable growth.

By working across regions and with key stakeholders, we help future-proof businesses and shape a better future — for people, for the planet, and for the industry. Creating Better Lives Through Better Business.

The CGF reflects the immense diversity of the industry, representing more than 380 retailers, manufacturers, and service providers across 70 countries. Our member companies account for combined sales of EUR 5.2 trillion and directly employ nearly 10 million people, with an estimated 90 million additional jobs along the value chain.

For more information, please visit: www.theconsumergoodsforum.com

## Introduction

Consumer companies are facing a harder path to profitable growth. Shoppers are more value-conscious, costs remain volatile, and purchasing decisions are harder to predict across channels, brands, and occasions. AI is intensifying that pressure by changing how consumers search, compare, plan, and decide. It is also creating a new route to advantage for companies that can apply it to the commercial decisions that matter most. Across CPG and retail, companies are launching pilots, testing agents, and applying AI across most functions, from innovation and marketing to merchandising, replenishment and on-shelf availability. Yet few companies are capturing material value at scale.

The next competitive separation will not come from adding more solutions, nor from building more sophisticated models. It will come from applying AI more deeply to the core commercial initiatives that build sustainable advantage: faster innovation, higher-fidelity demand sensing, more localized assortment, and better execution across physical and digital channels.

While there are several opportunities to deploy AI in support functions and reset cost structures, we see the greatest potential impact for consumer companies in applying AI to drive growth.

To understand how leaders are approaching this shift, Boston Consulting Group and The Consumer Goods Forum surveyed 39 senior CPG and retail executives. We complemented the findings with focused interviews and BCG's experience helping companies design and scale AI transformations across the industry.

This report examines where companies are applying AI today, why many remain short of full value capture, and what winners are doing differently to build growth, productivity, and advantage. While the sample size is not necessarily representative of the full industry landscape, the perspectives collected offer a directional view into how the industry is addressing AI transformation in demand-generation value chain.

![](images/df60d29e9bd8699028d9d70e301b5de6e29a5333f2672253dd3625a7dce0f61f.jpg)

# State of Play: Real Value, Unevenly Captured

AI's impact is expanding across the demand value chain. CPG companies and retailers have long used analytics and machine learning in areas such as product recommendations, pricing, and demand forecasting. What has changed is the range of work that AI can now address. Generative AI (GenAI) and agentic models can process unstructured consumer and demand signals, create and test concepts, and orchestrate actions within guardrails.

CPG companies are applying AI from concept and product formulation through revenue growth management, customer planning, digital shelf, and brand engagement.

Retailers are using AI to inform pricing and assortment, improve demand forecasting, strengthen inventory management and replenishment, support store operations, and personalize marketing. A new layer is emerging across both sectors: generative engine optimization (GEO), which shapes how brands and products appear in AI-enabled search, AI-generated answers, and agentic commerce, in which AI-enabled assistants help consumers discover, compare, choose, and buy. (See Exhibit 1.)

## Where the Focus Is Today

![](images/58aea0b8c3da2e6d0216b3ea34c09b2a7c09e7be6af45da46d0c499e2e510779.jpg)  
Source: CGF x BCG “AI for Growth, Productivity & Advantage” Survey, April 2026 (n=39), BCG case experience

So far, companies have moved fastest where the economics are clearest. In CPG, that movement has occurred in demand and supply forecasting and revenue growth management optimization. Retailers have advanced furthest in how they manage availability, forecasting, and operations. In these areas, data is relatively rich, decisions occur frequently, financial impact can be measured more directly, and AI can be embedded into existing commercial rhythms.

Progress has been slower in more generative, growth-oriented activities, such as idea to market and consumer engagement, where the strategic prize can be significant but the path to value is harder to define and scale.

Maturity remains uneven across sectors. Most CPG companies have yet to turn experimentation into scale. Roughly 75% of respondents remain in pilot and exploration mode, and only 18% are scaling impact. (See Exhibit 2.)

![](images/9126325c070bc699a339b32fdee7f5de5bef49db4c363cacdacbc2949b079344.jpg)

![](images/12032efc5b58b47b59d669a38150267f357642b4e5e127d12eb9f46450949d30.jpg)  
Sources: CGF x BCG, “AI for Growth, Productivity, and Advantage” survey, April 2026 (n = 39); BCG analysis.
Note: “Scaling impact” = companies scaled or fully deployed on at least half of the demand-generation initiatives. “Explorers” = companies with a mix of scaled and piloting initiatives. “Behind” = companies yet to start or still in early pilot on at least half of the initiatives.

## EXHIBIT 2

# Significant Dispersion in Maturity; CPG Lags Retailers

CPG

Most CPGs have yet to turn experimentation into scale

Current state of AI deployment maturity (% of respondents in each stage, aggregated across domains)

Explorers 76%

RETAIL

Sharp split between advanced players and explorers

Current state of AI deployment maturity (% of respondents in each stage, aggregated across domains)

Behind 40%

Explorers 15%

Scaling impact 45%

Our retail sample shows a two-speed world: 45% are scaling impact, while a comparable percentage (40%) have barely begun. The most advanced players do not spread their efforts evenly across the enterprise. Instead, they concentrate on initiatives where value is easiest to prove, including demand forecasting, replenishment, pricing, and transport optimization.

For the leaders, the value pool is material and likely to grow. BCG experience with clients in scaling individual initiatives suggests that scaling the full set of relevant AI initiatives across the demand value chain can deliver 220 to 350 basis points of cumulative EBIT for CPG companies and 180 to 360 basis points for retailers, assuming all initiatives are implemented at scale. (See Exhibit 3.) The value can flow directly to the bottom line, or companies can reinvest it in more competitive pricing, better offerings, and a wider array of services. AI-funded improvements can create a flywheel, making players more competitive, more relevant, and more responsive, which in turn can drive additional growth.

AI solutions create a powerful, much more agile approach and faster cycle times to repeatedly pursue a more favorable balance in the consumer industry's highly competitive environment.

## EXHIBIT 3

## Potential Value Today

![](images/b3071c0816a9ba935abf31c26c656d1e8f5445f97f605ded85dcecf96d6df3bc.jpg)  
+220 - 350 bps
Total prize at scale today

![](images/ff1bec148b88e0fc97e940d41f5ee1cc64264aa691398837f296a84093a9cb73.jpg)  
Source: BCG case experience
Note: Numbers may not add up due to rounding  
+180 - 360 bps
Total prize at scale today

![](images/401dc045e98e7b3db23607e81be734534d7b46b860e0a116340e810c893a946b.jpg)

We do not formally measure ROI of AI investments

As agentic capabilities mature and as AI moves from decision support to workflow orchestration, the full-scale opportunity could expand close to 1.7x for CPGs and retailers alike. This represents full potential delivered at scale through the use of future technology before appropriate reinvestment.

Tapping some of the next value pools may depend on stronger foundational capabilities. Voluntary, lawful and appropriately governed cross-sector collaboration on noncompetitive AI remains at an early stage of development. Surveyed executives are split on whether AI will create opportunities for voluntary collaboration, reinforce competition, or remain too uncertain to predict its future effects. The near-term opportunity may be to explore voluntary precompetitive foundational elements that help AI-enabled interactions work more reliably (for example, neutral product-data taxonomies, supply and stock signal definitions, and other standards that do not involve sharing competitively sensitive information).

Measurement remains the weak link. More than half of respondents said that they do not formally measure the ROI of consumer AI investments. (See Exhibit 4.) The most common reported barrier to scaling was that pilot economics did not translate into full-scale ROI.

Part of the challenge is structural. In a live commercial environment, AI improves decisions shaped simultaneously by seasonality, supply constraints, competitor moves, and consumer demand. That makes outcomes difficult to isolate and pilot economics hard to replicate at full scale.

This is where the pilot trap becomes real. A pilot can succeed in a controlled environment where it operates with selected data, dedicated teams, simplified workflows, and limited integration. At scale, the same initiative must handle live data, legacy systems, frontline adoption, governance requirements, and cross-functional tradeoffs.

The other part of the challenge involves a value gap. Many pilots track activity, adoption, or solution performance without including a clear baseline or threshold for scale.

## EXHIBIT 4

2x to 5x ROI for Best in Class, but the Rest Rarely Measure It

![](images/b0cee360232f679c1ec0cc9bed8759162ec64c707a28e55e4327ed5dff225fef.jpg)

Source: CGF x BCG “AI for Growth, Productivity & Advantage” Survey, April 2026 (n=39), BCG case experience, desk research
Note: Numbers may not add up to 100% due to rounding. Respondents were asked, “What was the realized ROI of your Consumer AI investments targeted in 2025?”

![](images/87a6323865d686614a33d97bcd1abf469abb3b8497f37334fb8cfd08b5dac8d8.jpg)

# Recommended CEO Considerations: Six questions that matter now

Our findings point to six questions for CEOs and leadership teams. (See Exhibit 5.) Together, they provide a practical way to pressure-test the AI agenda and identify the moves needed to turn AI into growth, productivity, and advantage in the demand value chain.

## EXHIBIT 5

Six Questions That Matter Now in AI Transformation

01

Are we aligning investments with strategic priorities?

02

Are we ambitious enough, and how do we measure impact?

03

How do we improve the odds for successful and sustainable transformation?

04

What are the broader impacts on the workforce and the operating model?

05

How should we think about our data assets and tech partnerships?

06

How do we move quickly without losing control of risks and costs?

Sources: CGF x BCG, “AI for Growth, Productivity, and Advantage” survey, April 2026 (n = 39); BCG analysis.

## Q1: Are we aligning investments with strategic priorities?

In many companies, AI activity does not yet target the processes that leaders say matter most. Almost half of CPG respondents named idea to market as their most strategic process, but only 11% have deployed AI initiatives in innovation. Retailers show a similar pattern: 46% of respondents named offer to assortment as the most strategic process, but only 34% have scaled AI significantly in that area.

The mismatch is understandable. Early initiatives often focus on areas where data is available, the process is less fragmented, and the risk is easier to manage. Over time, however, this can create a portfolio of initiatives that are easy to launch but hard to connect to future growth or productivity.

The leadership challenge is to transition from a long list of initiatives to a focused set of core commercial priorities. Winners narrow the agenda before they accelerate. They focus AI on a few core commercial processes that the company has chosen to win, such as faster innovation, sharper demand sensing, better availability, or more relevant assortment.

## Q2: Are we ambitious enough, and how do we measure impact?

Ambition is a moving target. As capabilities mature, the value pool could expand significantly, as illustrated above. Industry leaders need to take into account how quickly capabilities are improving, where technology can shift from support to orchestration, where AI can unlock more generative sources of growth, and where value may depend on better connections beyond the enterprise.

Ambition should run ahead of today's capabilities. Winners set ambition against the capabilities that their organizations can build over the next 18 to 24 months, not only against what today's solutions can do. If a $20\%$ improvement seems achievable today, leaders should test what data, workflow, and operating-model changes would be required to reach $30\%$ to $40\%$ over the next 18 to 24 months.

A higher percentage of initiatives should move beyond copilot to autopilot. In our survey, 67% of respondents said that they are still using AI mainly as a copilot, where AI generates insights but humans make the final call. Only 9% of respondents have pushed AI efforts into autopilot, where AI executes decisions within guardrails and humans manage exceptions.

Some processes from the demand value chain qualify today for autopilot operation. Demand forecasting is one example.

In copilot mode, AI strengthens the analytical layer: it brings together demand signals, inventory positions, customer orders, promotion calendars, and supply constraints; highlights where the forecast is changing; and explains the drivers. Meanwhile, planning teams still adjust assumptions, reconcile results, and decide on the next action. In autopilot mode, AI continuously reads demand signals, inventory positions, customer orders, and supply constraints. It can then refresh forecasts and trigger allocation and replenishment actions within agreed guardrails, with humans in the loop to manage exceptions.

Leaders stretch ambition to the generative frontier. AI has significant potential in generative work, expanding the set of ideas, options, and strategic choices that a team can explore.

For example, in innovation, advanced CPGs are beginning to use agentic portfolio management to test opportunities through multiple lenses: consumer need, white space, brand fit, margin potential, supply feasibility, cannibalization risk, and retailer relevance. The output provides a faster, sharper judgment on whether an innovation deserves to be funded, reshaped, scaled, or stopped.

Companies need to account for value beyond the enterprise. The next frontier of the demand value chain may require lawful, selective, voluntary, pro-competitive collaboration. Better replenishment, smarter promotion planning, and more relevant personalization can all be enhanced through lawful, voluntary and appropriately governed bilateral data sharing and more connected ways of working across CPGs, retailers, and platforms.

Measurement should begin on day one. As our survey shows, the pilot trap is real. AI initiatives can prove to be technically feasible while leaving scale economics unclear. To avoid that trap, at the pilot stage, winners track leading indicators that will hold at scale, balancing effectiveness with efficiency measurement. Relevant indicators include share of projects course-corrected early, time saved in key development steps, and evidence that AI is strengthening the quality of the innovation funnel.

One client accomplished this by making measurement a governance discipline from the outset. Before launching the pilot, the finance and business teams jointly built and endorsed a full-fledged business case that included value at stake, ROI, and leading KPIs for confirming, reducing, or expanding the potential. The differentiator was the depth of the as-is baseline. Teams mapped the current workflow, quantified the distribution of time and effort across the process, and used that information as a baseline for gauging expected improvement. This created a confidence loop: the baseline gave the measurement credibility, pilot evidence refined the value case, and each stage-gate update increased confidence in what could be delivered. By the end of the pilot, leaders could look at a revised business case grounded in tested potential, giving them a clearer basis for deciding what and where to scale.

## Q3: How do we improve the odds of successful and sustainable transformation?

Successful AI transformations start with clarity regarding how far the company intends to go. Three levels of transformation depth apply: deploy, reshape, and invent.

Deploy puts AI into existing work. In practice, AI deployment involves rolling out enterprise productivity solutions at scale. Most companies are 

[中间内容因长度限制已省略]

form brand building</td></tr><tr><td>11 Tailored content &amp; end-to-end campaign execution</td><td>Produce and localize creative assets for marketing purposes</td></tr><tr><td>12 Media optimization &amp; ROI measurement</td><td>Enhance targeting and campaign activation; simulate 360° A&amp;P performance</td></tr><tr><td>13 AI-driven social &amp; influencer marketing insight &amp; activation</td><td>Identify social media trends and relevant influencers for target audience; generate content</td></tr><tr><td>14 Direct-to-consumer new business models</td><td>Unlock new service-led revenues via AI-driven disintermediated models</td></tr><tr><td>GEO and agentic commerce</td><td>15 Agentic commerce orchestration, including GEO Optimization and building connected agents</td><td>Enable AI agents to discover, compare, and purchase for consumers</td></tr></table>

Sources: CGF x BCG, "AI for Growth, Productivity, and Advantage" survey, April 2026 (n = 39); BCG case experience. Note: A&P = advertising and promotion; CRM = customer relationship management; GEO = generative engine optimization; KAM = key account manager; OOS = out of stock

## EXHIBIT 10

## Retail Demand Value Chain

<table><tr><td></td><td>AI lever</td><td>Description</td></tr><tr><td rowspan="4">Offer to assortment</td><td>1 Shopper insights &amp; demand detection</td><td>Identify shopper needs, preferences, and emerging trend patterns</td></tr><tr><td>2 Pricing &amp; promotion optimization</td><td>Optimize price ladders, markdowns, and promotion mechanics to improve margins</td></tr><tr><td>3 Assortment, category &amp; planogram</td><td>Optimize category mix, clustering, and automated planogram design</td></tr><tr><td>4 Supplier &amp; negotiation assistant</td><td>Support negotiations, trade terms, joint planning scenarios, and contract management</td></tr><tr><td rowspan="7">Plan to on-shelf availability</td><td>5 Demand &amp; inventory forecasting</td><td>Predict SKU-level demand to reduce overstocking and understocking</td></tr><tr><td>6 Supply chain &amp; replenishment</td><td>Automate stock deployment and replenishment under operations constraints to ensure OSA</td></tr><tr><td>7 Warehousing &amp; transport optimization</td><td>Optimize routes and transport modes across geographies and warehouses</td></tr><tr><td>8 Digital shelf accuracy &amp; compliance</td><td>Ensure PDP/PLP completeness and accuracy, and facilitate OOS detection</td></tr><tr><td>9 Smart operations &amp; monetization</td><td>Automate checkouts and extract operations insights for in-store efficiencies and monetization</td></tr><tr><td>10 Store workforce &amp; schedule optimization</td><td>Streamline workforce scheduling, task routing, and smart checks orchestration</td></tr><tr><td>11 Store footprint &amp; layout</td><td>Streamline store footprint and localization per store; build customer-centric layouts</td></tr><tr><td rowspan="5">Marketing to engagement</td><td>12 Media optimization and ROI measurement</td><td>Enhance targeting and campaign execution, and simulate 360° A&amp;P performance</td></tr><tr><td>13 Tailored content generation &amp; end-to-end marketing campaign execution</td><td>Produce and localize marketing assets</td></tr><tr><td>14 Churn prediction &amp; CRM activation</td><td>Identify customers at risk of churn, and launch personalized retention actions</td></tr><tr><td>15 Personalized loyalty programs</td><td>Deliver personalized rewards and experiences to increase repeat purchases</td></tr><tr><td>16 Customer service assistant</td><td>Support shoppers prepurchase, and manage postpurchase interactions and returns</td></tr><tr><td>GEO and agentic commerce</td><td>17 Agentic shopping, including GEO optimization and building connected agents</td><td>Help shoppers discover, compare, and evaluate products across channels</td></tr></table>

Sources: CGF x BCG, “AI for Growth, Productivity, and Advantage” survey, April 2026 (n = 39); BCG case experience.  
Note: A&P = advertising and promotion; CRM = customer relationship management; GEO = generative engine optimization; KAM = key account manager; OOS = out of stock.

## About the Authors

![](images/d92e231a0cc7034d2eb371110230091664d1eb59e9480bc390e9855686e04dc8.jpg)  
Mai-Britt Poulsen
Managing Director and Senior Partner
London
Poulsen.Mai-Britt@bcg.com

![](images/e9cfa8f5179d14d46d52f9e77834c8de1fab07427d7e04b78a7d79559032eec9.jpg)  
Yotam Ariav
Managing Director and Senior Partner
Chicago
Ariav.Yotam@bcg.com

![](images/3db775a0b0a09112ecc48eb4e4709d4acaa4d72a821db54e34082a4c4e5311ff.jpg)  
Nicolas de Bellefonds
Managing Director and Senior Partner
Paris
deBellefonds.Nicolas@bcg.com

![](images/ddf18bfb83e52a2734f9eb194fc003cf25b388ef25c2baede308a3678e5e29be.jpg)  
Nate Shenck
Managing Director and Senior Partner
Washington, D.C
Shenck.Nathan@bcg.com

![](images/68a8af141018f9d60341d117b836c3fe875d701f4ebaacf15b261612057ace2f.jpg)

Arnaud Bassoulet
Managing Director and Partner
Paris
Bassoulet.Arnaud@bcg.com

The authors extend their gratitude to everyone who contributed to the research and development of this report. The survey at the heart of this report was partially delivered through an AI-mediated platform, Verso. (https://www.askverso.ai/). If you would like to discuss this report, please contact the authors.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.

© Boston Consulting Group 2026. All rights reserved.

![](images/393cf78540024fd65398c9dc43a8044708373b99b3ce606ce1793ce362eb210b.jpg)
"""
