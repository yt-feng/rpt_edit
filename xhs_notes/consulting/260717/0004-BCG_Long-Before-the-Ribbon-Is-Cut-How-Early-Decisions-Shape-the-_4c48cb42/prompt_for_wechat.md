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
# Long Before The Ribbon Is Cut

# How Early Decisions Shape The Fate Of Large-Scale Projects

May 2026

By Devanshu Mathur, Andrea Nogara, Dr. Nuno Couto, Richard El Cheikh, Mawadda Abdan

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

## Contents

01 Unprecedented Scale, Unforgiving Expectations

02 Where Operational Risk Is Formed

03 Four Case Studies: How Operational Planning Shapes Performance

\- Case Study #1: FIFA World Cup Qatar 2022

• Case Study #2: Expo 2020 Dubai

• Case Study #3: Istanbul Airport

\- Case Study #4: Fontainebleau Las Vegas

04 BCG's Asset Ops360: How to Redefine Operational Viability in Capital Programs

# Unprecedented Scale, Unforgiving Expectations

The world has never built like this before.

Capital and infrastructure investments now operate at a multitrillion-dollar scale. In 2026, it's estimated that the transport, energy, industrial, and residential sectors will attract over \$7 trillion in combined capital investment. $^{1}$ And according to the 2025 Global CAPEX Survey from the Boston Consulting Group (BCG), 94% of large-scale project owners (those that spend at least \$5B annually) expect to maintain or increase their investments over the next 12 months. At the same time, 54% of respondents in that same survey report that post-FID delivery challenges have intensified over the past year. Saudi Arabia alone, under Vision 2030, is deploying more than \$1 trillion in capital expenditures for large-scale projects. $^{2}$

Yet the most striking shift is not scale. It is expectations.

Assets are now expected to perform from day one. Revenue must ramp up rapidly. The tolerance for disruption, whether political, financial, or reputational, is minimal. The margin for underperformance has disappeared.

Still, the record of large-scale projects has struggled to meet these demands. Only around 1 in 12 projects is delivered on time and on budget, with cost overruns averaging over $60\%$ of the initial budget. $^{3}$ Schedule slippage often reaches one to two years. Berlin's Brandenburg Airport, for example, opened more than nine years behind schedule and over €4 billion above its original budget. $^{4}$

Under pressure to recover time and money, developers often compress testing, training, and commissioning. Operational teams are mobilized late. Systems are exposed under live conditions, shifting risk directly into operations.

The consequences are severe. Congestion, system failures, safety incidents, reputational damage, regulatory scrutiny, and prolonged stabilization efforts follow.

These breakdowns are often framed as execution failures at project delivery. Yet the fact that they occur consistently across sectors and geographies suggests something deeper. Failure is rarely created just before the opening. It is embedded earlier — in design trade-offs, sequencing priorities, and governance choices made long before the first guest arrives.

This paper shifts the lens upstream. It examines large-scale projects across their lifecycles to understand how operational risk is formed, compounded, and ultimately revealed under live conditions. Rather than treating opening day as the starting point of failure, we investigate how early decisions shape operational performance well before launch.

This lens also underpins BCG's ongoing work in embedding operational viability earlier in the lifecycle of large-capital projects.

![](images/2f1ea3c2f37c3975d03262c1fb948f46a93195e94c3c98f2c305085932298220.jpg)

Project lifecycle

# Where Operational Risk Is Formed

Operational risk does not begin on opening day. It starts during strategy definition, when early assumptions about demand, operating models, and performance targets are set.

As a project moves into design and construction, those assumptions are translated into fixed layouts, capacities, and system interfaces. Flexibility narrows. Decisions become structural. By the time a project reaches testing and delivery, budget and schedule pressure have compressed readiness activities, as illustrated in Exhibit 1.

Once a project enters live operations, accumulated risk materializes quickly and at scale. Operational teams shift from execution to containment. Manual interventions replace automation. Procedural workarounds substitute for system reliability. Extraordinary effort becomes the norm.

At this point, these conditions are expensive to manage, difficult to unwind, and highly visible to regulators, stakeholders, and, most importantly, the public. The implication is clear: The operational lens cannot be applied at delivery alone. Instead, it must be embedded earlier — at strategy, design, and construction — where risk takes root and is locked into the system.

## EXHIBIT 1

## Where Operational Risk Really Begins

![](images/3e6b283bf7a43853823225f4b3cd86df9be1974f55e5d19c300b9b22d76f8dee.jpg)  
Testing & delivery Go-live (Ops start)

# Four Case Studies: How Operational Planning Shapes Performance

To understand how early operational choices shape real-world outcomes, we examine four large-scale projects that made fundamentally different governance and planning decisions.

1. FIFA World Cup Qatar 2022 (Qatar): This project embedded operational considerations from strategy through construction. Design decisions reflected operating realities, resulting in stable and controlled operations.

2. Expo 2020 Dubai (The United Arab Emirates): This project institutionalized a detailed concept of operations (ConOps) and accountability model, led by the chief

operating officer (COO), early in the lifecycle. When COVID-19 disrupted core assumptions, the pre-established structure enabled rapid adaptation.

3. Istanbul Airport (Turkey): Constrained by extreme timelines, this project entered operations before construction was complete. Once the project was public, operational strain surfaced immediately.

4. Fontainebleau Las Vegas (The United States): This project faced multiple strategic resets. As a result, a new operating model was imposed on legacy infrastructure. Redesign, construction, and activation timelines got compressed. And initial operations became strained.

![](images/305ed0796c8e1b61703495628b0a8846f3596cf2c273fac9089d5e27bb178c0e.jpg)

# Case Study #1: FIFA World Cup Qatar 2022

EXHIBIT 2

# FIFA World Cup Qatar 2022: Operations Designed Early, and Thus Delivered at Scale

![](images/28c9c0f8acae8bee090f63c2371f0e7d57edd38821bd3024f0270e5885473433.jpg)

Qatar 2022 stands as one of the most operationally successful mega events in history. Unlike prior World Cups that were awarded to countries with existing infrastructure, Qatar won the 2010 bid based on ambition: 65 percent of the country's infrastructure did not yet exist.

Strategy: From the outset, the World Cup was embedded within Qatar's National Vision 2030. In 2012, a 'Supreme Committee' was established as an integrated delivery authority, responsible for delivering the Cup while aligning the project with the country's national development agenda. Infrastructure, urban planning, transport, and security were coordinated a decade before kickoff, turning the event into a national operating program.

Design: By 2015, Qatar had built a tournament demand model simulating up to 3.5 million people and daily movements by 800,000. $^{5}$ The model simulated full match-day demand across flights, accommodations, the metro, highways, fan zones, and stadiums. Real-time dashboards visualized pressure points hour by hour. When thresholds were breached, capacity and routing were adjusted — not after kickoff, but years before.

In parallel, operational capability was being built. The Josoor Institute, created with the SDA Bocconi School of Management in 2013, trained future World Cup leaders through courses and live roles at FIFA World Cup Brazil 2014, UEFA Euro 2016, and FIFA World Cup Russia 2018. $^{6}$ Operator readiness began nearly a decade before opening, well beyond standard event timelines.

Construction and Testing: Continuous simulations informed design and translated directly into construction. Each newly completed stadium hosted live events as operational trials. In 2017, the Amir Cup final was used to test new World Cup venues; this test revealed entry-gate compression and post-match metro surges. In 2019, the FIFA Club World Cup ran full FIFA procedures; this test revealed gaps in transport coordination and accreditation. In 2021, the FIFA Arab Cup replicated a condensed World Cup across all eight stadiums; this test revealed peak departure congestion and fan-zone overflow patterns.

Testing drove correction. Gate sequences were redesigned. Metro capacity was extended. Escalation protocols were tightened. Transport routing was recalibrated. As a result, operational viability was confirmed well before the event's official start.

Operational Start: The contrast with prior tournaments was clear: Brazil 2014 began with metro systems that were late and untested. Russia 2018 faced food-supply disruptions on opening day. Qatar 2022, on the other hand, was fully commissioned at launch.

The economics reflected this readiness. Whereas Brazil generated 4,826 million in total FIFA revenue, $^{7}$ and Russia brought in 6,421 million, $^{8}$ Qatar delivered 7,568 million, $^{9}$ the highest revenue in World Cup history.

Qatar 2022 succeeded not because it performed well at delivery. It succeeded because operational viability was designed, tested, and proven over a 10-year horizon.

![](images/1658f18fef4ee733870888946657c0be55dc9d636b17ec49aa537f41e3e670c5.jpg)

# Case Study #2: Expo 2020 Dubai

EXHIBIT 3

# Expo 2020 Dubai: Built to Adapt, Resilient Under Shock

![](images/38f7c9fb53e560770b0184e8c90ea5ca8c11347c968bb54a0f68324591f78969.jpg)

Expo 2020 Dubai delivered a six-month mega event under unprecedented disruption. But such resilience did not emerge during a crisis; it was engineered years earlier through a robust operating model.

Strategy: As early as 2015, the organizing committee developed a detailed end-to-end Concept of Operations (ConOps). This ConOps defined how the Expo would function on day one, day 100, and day 180. Every service line (security, venue management, food and beverage, retail, transport, etc.) was assigned ownership, service levels, escalation pathways, and cost parameters. Operational accountability was centralized under a COO-led governance model. As a result, ConOps became the reference against which every scope decision, capacity threshold, and trade-off was tested.

Design: Initial forecasts projected 25 million visitors, supported by over 30,000 volunteers. $^{10}$ These projections were translated into service levels and capacity thresholds. In 2016, ConOps helped detail customer journeys and map arrival, screening, circulation, dwell time, and exit flows. Assumptions were converted into quantifiable requirements: gate capacity, clinic sizing, staffing ratios, payment infrastructure, and overnight reset operations.

Construction and Testing: As delivery progressed, ConOps governed sequencing, interfaces, and adjacencies. Full end-to-end rehearsals could only begin once venues and teams were mobilized, which happened as early as 2019. In parallel, simulations and scenario testing stress-tested crowd surges, emergency response, and command escalation under peak conditions.

Then COVID-19 fundamentally altered every operating assumption and projection. International arrivals dropped. Health screening became mandatory. Density thresholds were reduced. Workforce availability fluctuated.

But because ConOps had already done so much work — defining everything from service levels and ownership to escalation pathways and capacity baselines — the system did not require redesign. It merely needed recalibration.

Health controls were inserted into existing entry flows. Crowd limits were adjusted against established thresholds. Staffing models were resized within predefined role structures.

The operating logic remained stable; only the parameters changed.

Operational Start: The Expo opened to the public in 2021, operating continuously for six months. Transport to the Expo was integrated with Dubai's Roads and Transport Authority (RTA) through dedicated buses and metro services. A centralized control room unified security, police, fire services, and transport authorities under real-time command oversight.

Despite global travel disruption and fluctuating capacity restrictions, the Expo welcomed over 24 million visits. The lesson: operational resilience must be engineered early. When disruption reshapes demand and constraints, a defined operating architecture absorbs the shock. The system flexes without losing control.

![](images/e25f2f4a8d6e7c02c9003fc02b3d08d4423d30302f355f05bca0e3b5443e76ee.jpg)

# Case Study #3: Istanbul Airport

Istanbul Airport: Rushed Into Operation, Breakdowns When Going Live

![](images/c2865da5003aee052abb12441b6ffa5725af98ce2a73c72db3545257997349de.jpg)

Istanbul Airport, an \$11.7 billion large-scale project, $^{11}$ entered operations while construction, commissioning, and system integration were still ongoing.

Strategy: In 2014, the Turkish government launched the project to position Istanbul as a global aviation hub. Atatürk Airport had reached capacity and demand was rising sharply. Strategic decisions about scale and ambition were set centrally and moved rapidly into design. The airport was designed for an initial capacity of 90 million passengers annually, with long-term expansion to 200 million, positioning it among the largest hubs in Europe.

Design: This ambition translated into exceptional complexity. For example, a typical large airport operates fewer than 3,000 airfield ground lights; Istanbul was designed for approximately 35,000. $^{12}$ What's more, such complexity required coordination with airlines, ground handlers, and Eurocontrol. Finally, the launch date of 2018 compressed development cycles. As construction progressed, key operational interdependencies continued to evolve.

Construction: Construction progressed while aspects of the design were still being finalized. Layout revisions were incorporated while construction proceeded on site. With limited flexibility to pause or resequence, momentum and deadlines took precedence over operational alignment.

Testing and Delivery: In October 2018, Phase 1 operations started even as additional runways, terminal capacity, and expansion phases remained under development as part of the broader master plan. Mandatory technical commissioning was completed, but without full operational rehearsals. Large portions of the terminal remained unfinished, so the airport initially handled only 20–30 flights per day.

The results were predictable: Passenger satisfaction plummeted. Problems emerged in access, circulation, baggage handling, routing, and facility readiness. The Airport Operational Database (AODB) was not fully stabilized; airlines and ground handlers operated across separate systems, thus exposing data misalignment under live conditions. Operational coordination was subsequently consolidated under an Airport Operations Control Centre (AOCC), providing unified oversight across airlines, ground handlers, and airport systems.

Operational Start: In April 2019, all flights were transferred from Atatürk to Istanbul Airport. Operational strain became visible immediately: Flights arrived without luggage. Layout inefficiencies, incomplete moving walkways, and extended taxi time added to the strain. Basic services lagged expectations. With no metro connection in place, access relied entirely on road transport, thus creating congestion and missed flights. Negative media coverage exacerbated the situation.

In March 2020, the COVID-19 pandemic brought a sharp drop in traffic, slowing operations until 2022. This period of reduced demand provided time to continue developing infrastructure and stabilize operations. Over time, operators stabilized performance. Today, the airport handles approximately 80 million passengers annually.

The lesson is structural: Istanbul Airport did not fail at opening; it absorbed operational risk that had accumulated across earlier phases. The cost of embedding operations late was paid in public.

![](images/9ab5cb5f45de5c83aa892267fa910f81c40a2e9c87718875fb19cea79fcd6833.jpg)

# Case Study #4: Fontainebleau Las Vegas

Fontainebleau Las Vegas: Dormant for a Decade. Operational Strain at Restart

![](images/844a9b1a4cd77ddaa5b1fd3ef3ec2cd0cd7a56d6c49728aea774dd5b5dec6dc8.jpg)

After nearly two decades of interruption and ownership changes, Fontainebleau Las Vegas opened in December 2023 as a \$3.7 billion $^{13}$ integrated resort. Its eventual launch was not the continuation of a linear development cycle, but the culmination of multiple resets resulting from multiple ownership changes. The project illustrates how a change in project vision, executed on partially completed infrastructure, jeopardizes the successful launch and operations of a large development project.

Strategy: The project was initially launched in 2006 under Fontainebleau Development, with the ambition to introduce modern luxury to Las Vegas. The program combined hospitality, gaming, retail, food and beverage, and residential condos. Located about three kilometers north of the Strip, the thesis was product-led: A unique resort would compensate for the distance from core footfall in the Vegas Strip.

Construction began in 2007. However, during the 2008 financial crisis, the developer filed for Chapter 11. At that stage, the core structure was largely complete, but interior works, back-of-house areas, and life-safety systems were unfinished.

The project then changed ownership three times:

1 In 2009, after bankruptcy, the project was sold and remained dormant.

2 In 2017, new ownership relaunched the asset as “The Drew Las Vegas,” pivoting toward a convention-led gaming resort.

3 In 2021, after COVID-19, Fontainebleau Development reacquired the property and positioned it as a luxury integrated resort.

Design: Initial design proceeded conventionally. However, a changing vision led to continuous adjustments to the design despite construction progress. Design decisions were constrained by existing structures and previously installed systems.

For example, a substantial redesign was required in 2021 to align the core and shell with updated luxury positioning and new code requirements. Residential condo layouts were reconfigured into hospitality rooms. Public spaces and the back of house were modernized after years of dormancy.

Construction and Testing: When Fontainebleau Development repurchased the asset in 2021, it set the goal to open by 2023. As a result, timelines were compressed, and design, construction, and operational readiness efforts proceeded concurrently.

Once construction was finalized, the project team had less than two months to get up and running. During this period, they onboarded and trained more than 6,500 team members while simultaneously resolving last-minute issues (including incidents such as pipe failures during testing). Unsurprisingly, full operational readiness was not achieved before opening day.

Operational Start: After 16 years of development, Fontainebleau Las Vegas debuted on December 13, 2023. Despite a grand opening that featured celebrities, early operations struggled. The property underperformed

against targets, with visible underutilization in both the hotel and gaming facets. Within months of opening, workforce and executive turnover occurred, including layoffs of dozens of table-game dealers. $^{14}$

Guests left mixed reviews of the resort. While some praised the design and quality of the amenities, others criticized inconsistent service and poor value for money. Guests also reported long internal walking distances (due to the layout configuration). And reports showed discrepancies in check-in times and room assignments as well as housekeeping inconsistencies.

Fontainebleau Las Vegas shows what happens when multiple changes are made to an asset's vision and strategy: Operational struggles materialize at every turn. Morale suffers. Underperformance is inevitable.

![](images/efb5dcef0a2f211755312540cf2c39077616d185770c901e74cec5c3df4e81c2.jpg)  
14. David Danzis, 2025, “More employee cuts on Las Vegas Strip as casino lays off ‘dozens’ of dealers,” Las Vegas Review Journal, May 28.

# BCG's Asset Ops360: How to Redefine Operational Viability in Capital Programs

The pattern across these four cases is consistent. Projects that perform from day one are not better managed at launch. They are better designed from the start.

Qatar 2022 did not succeed because its operations team was exceptional on opening day. It succeeded because operational viability was treated as a design parameter for over a decade. Expo 2020 did not absorb a global pandemic through improvisation. It absorbed it through a governance architecture that was already in place. Where projects have struggled, the failure was rarely created at delivery. The risk accumulated earlier — in strategy and design — and was simply revealed when operations began.

The implication is structural, not cultural. Operational viability cannot be bolted on at the end. It must be embedded at every stage, from strategy through construction, where assumptions are set, trade-offs are made, and flexibility is either preserved or lost.

Yet in most large-scale programs today, this does not happen. Operational viability is treated as an implicit outcome rather than an explicit requirement. By the time issues surface, scope is frozen, layouts are locked, and systems are built. Flexibility is gone. Recovery is expensive. And the cost is paid in public.

This is the gap that BCG's Asset Ops360 is designed to close.

Asset Ops360 is a structured diagnostic framework that embeds the operational lens across the full project lifecycle. It evaluates viability simultaneously across three dimensions: every stage of development from strategic definition through completion; every operational component of the asset; and every key function that must contribute at the right moment. Together, these dimensions produce a quantified viability profile, making risk visible at every point in the lifecycle.

In practice, this means three things that traditional project governance does not provide: assumptions are stress-tested before they become commitments, gaps are surfaced at the stage when closing them is still cheap, and intervention shifts from opening day to the design table, where it belongs.

The leaders who delivered Qatar 2022 and Expo 2020 understood this intuitively. They built operational thinking into the earliest conversations, and it showed when the ribbon was cut. For those overseeing the next generation of large-scale projects, BCG's Asset Ops360 offers a way to make that discipline systematic, transferable, and measurable. The question is not whether to apply it. It is how early.

![](images/84245d7f31eefbce512d06212249ff48a7c4b61afa2471d514cebd3286cdf3a0.jpg)

# About the Authors

![](images/f88c54892ee4e71ab49a156b6795a787bbaeb79347c43c046dca581e298c248e.jpg)

Devanshu Mathur is a Managing Director and Partner in BCG's Middle East office. He is a core member of the Travel, Cities & Infrastructure practice, specializing in tourism, megaprojects and entertainment destinations, including theme parks and water parks. You may contact him by email at Mathur.Devanshu@bcg.com

![](images/8c842c661421039fc62604e7e1da4727db5313b4e14d4163b1cc5cf05e73fe8d.jpg)

Dr. Nuno Couto is a Partner in BCG's Middle East office and a core member of the Travel, Cities & Infrastructure practice. He specializes in large-scale entertainment and luxury hospitality developments. You may contact him by email at Couto.Nuno@bcg.com

![](images/ab7e09386b54c0357709d5d37e2ec61193a7700e228e90bd8cc928c7a3e5780a.jpg)

Mawadda Abdan is an Associate in the firm's Middle East office. She has worked on various projects supporting regional transformation, with a focus on megaprojects and transportation. You may contact her by email at Abdan.Mawadda@bcg.com

## For Further Contact

If you would like to discuss this report, please contact the authors.

![](images/4561df51b6f172aad8f571408b97499a3c4bfd849914fc331c97f716d3511774.jpg)

Andrea Nogara is a Managing Director and Partner in BCG's Middle East office. He is a core member of the Industrial Goods practice and has extensive experience across construction and automotive industries. You may contact him by email at Nogara.Andrea@bcg.com

![](images/4bcf6c9b5a069f56c5cafd7e9e194b4966be5f12887d64a286ec6ec778134452.jpg)

Richard El Cheikh is a Consultant in the firm's Middle East office. He has worked on various projects supporting Saudi Arabia's transformation, with a focus on megaprojects across the Kingdom. You may contact him by email at Elcheikh.Richard@bcg.com

![](images/80361b454fc872cbbed09c128725fa0302401b7398f9f64f1d50ab3abe60cdbf.jpg)
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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
