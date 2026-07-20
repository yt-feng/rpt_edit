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
Are We in a
Defense
Tech Bubble?

July 2026

By Matthew Bruce, Diana Dimitrova,
Daisuke Sohta, Matt Aaronson, Brian Hirshman,
Greg Mallory, and Rob Stallard

![](images/f499403ae47714f07fc27840796e5fe2a802bf544d4c5ec34c2d768957107e8e.jpg)

## Boston Consulting Group

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

![](images/c735acda66d8de69e62cfe9e3f16b2cafdba1bce95816e456ad0080c6f40a679.jpg)

## Vertical Research Partners

Vertical Research Partners is the preeminent independent equity research firm focused on the Industrials and Materials sectors, providing high-quality, value-added proprietary investment research services derived from extensive industry knowledge.

Founded in 2010 by Jeff Sprague, Vertical Research Partners now fields 6 analyst teams covering 115 stocks across the market capitalization spectrum within the Electrical Equipment & Multi-Industry, Industrial Technology, Global Aerospace & Defense, Engineering & Infrastructure, Building Products, and Chemicals sectors.

![](images/f68fb0d4b36b677081faac420039a8f15eba5f8dae1e496c16dae731894b1f61.jpg)

# Read the recent headlines, and you'll know that defense aviation is shifting away from billion-dollar exquisite programs in favor of technologies that are smaller, cheaper, and faster to produce.

These systems have proven their worth in recent conflicts, and defense ministries are adjusting their acquisition models to focus on speed, lowering the barriers to entry. The upstart competitors that produce these platforms have attracted billions in private investment, and some legacy prime contractors are weighing whether to shift capital into this market. Our take? Not just yet.

BCG, collaborating with Vertical Research Partners, an equity research firm, recently analyzed the profit pools for traditional defense aviation platforms and for newer, cheaper solutions. The result shows that while the newer platforms show faster growth than exquisite platforms, their profitability profile is more limited and they carry characteristics that make them less attractive.

Our analysis underscores the need for incumbents and investors to assess the full business implications of these smaller programs, including R&D models and per-unit economics, so they can make an informed decision about whether, how, and where to compete in this market.

## The Rapid Rise of Nontraditional Competitors

New, lower-cost aviation solutions offer clear advantages to armed forces, offering far lower unit costs, shorter production times, and a reliance on commercially available technologies. To capitalize on these solutions, governments are adjusting procurement processes in favor of speed. In the US, for example, the Department of War's Other Transaction Authority (OTA) program enables the government to transact with companies outside of traditional contracts, typically for research, prototypes, and production. The program has increased from \$1.8 billion in 2016 to more than \$18 billion in 2025.

Competitors that offer affordable mass and expendable solutions are now starting to work their way up the value chain. (See Exhibit 1.) For example, the US Air Force is developing a Collaborative Combat Aircraft—an uncrewed vehicle that will fly alongside crewed fighter jets—and Anduril and General Atomics were both selected to develop prototypes, beating out prime contractors Lockheed Martin, Northrop Grumman, and Boeing. There is a real question as to whether the core business of incumbents is at risk, particularly if affordable mass players can adapt the production system they have built for speed and apply it to lower-rate production programs. At the same time, primes that want to participate in this market must determine the best approach. Co-invest in funding rounds? Or acquire these technologies over time?

Europe is moving in the same direction, but it faces different dynamics. European conflicts set the tone for lower-cost tech demand, yet the procurement is more fragmented among ministries of defense and countries are focused on rebuilding basic defense capabilities before committing to newer types of defense technologies. Many startups are now targeting this market, often funded in large part by private capital.

Yet while these new solutions are succeeding in conflict, and potentially introducing new tech models to consider, their underlying economics are different from those of established aviation platforms. Most manufacturers of affordable mass and expendable systems are not yet profitable, despite seeing huge demand for their products. As a result, prime contractors now face a capital-allocation dilemma: Do they continue to invest in a stable and profitable business of developing exquisite programs, or do they think about leaning into higher-growth segments? Can they simply buy the most successful startups and offer an attractive exit to the private capital investing in a perilous market? (See “Considerations for Primes and Institutional Investors.”)

## EXHIBIT 1

The Three Main Classes of Defense Aviation Technology Have Radically Different Parameters

<table><tr><td></td><td>Exquisite systems</td><td>Affordable mass systems</td><td>Expendable systems</td></tr><tr><td>Unit economics</td><td>&gt;$10 million</td><td>$100,000 to $10 million</td><td>$50,000 to $100,000</td></tr><tr><td>Annual volume (units)</td><td>&lt;200</td><td>200–10,000</td><td>&gt;10,000</td></tr><tr><td>Lifespan (years)</td><td>~20–35+</td><td>~1–15</td><td>Single-use/mission</td></tr><tr><td>Program revenue</td><td>$5 billion+</td><td>$500 million–$10 billion</td><td>$100 million–$1 billion</td></tr><tr><td>EBIT margin</td><td>10%–15%</td><td>10%–15%</td><td>15%–20%</td></tr><tr><td>R&amp;D model</td><td>Cost-plus, government-funded</td><td>Hybrid of contractor- and government-funded</td><td>Primarily contractor-funded</td></tr><tr><td>Sustainment scope</td><td>Spare parts, depot maintenance, and upgrades</td><td>Software upgrades and some hardware replacement</td><td>Pre-deployment readiness only</td></tr><tr><td>Prime supplier</td><td>Traditional players</td><td>Neo-primes and defense startups</td><td>Defense startups</td></tr></table>

Source: BCG proprietary aviation-defense market model based on expert interviews.
Note: Group 1 and 2 UAVs (unmanned aerial vehicles) excluded from affordable mass; expendable quantity focuses on expendable air systems; includes Group 1 and 2 UAVs and loitering munitions; revenue ranges are illustrative and not mutually exclusive; certain expendable systems may exceed revenue of smaller affordable mass platforms based on procurement volume; excludes space, counter-UAS (unmanned aerial systems), and broad munitions.

# Considerations for Primes and Institutional Investors

![](images/e780b6efd2dfb4e0ed4ac9e98db32617dbb642492f6f1db6235f4f014e219bff.jpg)

Primes and institutional investors weighing whether to participate into a particular profit pool should make that assessment by looking at five factors.

\- Structural Attractiveness. Is the value pool large enough, in both margin and absolute terms? Where does value concentrate across the lifecycle? How firm is demand for the foreseeable future?

\- Competitive Alignment. Do the company's current advantages apply to the value drivers in this pool, or does entry require closing a capability gap—whether organically or through acquisition—against competitors with a years-long head start?

\- Operating Model Fit. Can the company build or acquire a structurally separate unit with the operating model, cost structure, and acquisition cadence needed to compete in the affordable mass and expendable markets while the core business maintains the legacy model?

\- Capital Requirements. What is the total capital required across R&D, manufacturing scale-up, and working capital? At what volume and demand scenario does the investment break even?

\- Time Horizon. Over what period will value accrue, and does this timeline remain viable if demand contracts sharply before returns materialize?

## Five Key Findings from Our Analysis

We modeled the growth prospects and profit pools of various defense aviation categories and derived five clear insights.

Legacy players will continue to claim the bulk of industry revenue. Legacy primes dominate defense aviation budgets today, and assuming defense budgets hold steady, that scenario will continue through the coming decade. Procurement revenue from exquisite aviation systems comprised about \$65 billion in the US and EU in 2025, compared with roughly \$5 billion for affordable mass systems and just \$55 million for expendable systems.

Looking ahead, the growth prospects for these sectors through 2033 show different trajectories. Exquisite systems are estimated to grow at a compound annual rate of approximately 2% to 3%, while affordable mass will grow at 15% to 20% and expendable systems at 35% to 40%. However, even with that disparity in growth rates, exquisite systems will still comprise more than 80% of the market by 2033, because the newer categories are growing from smaller bases. (See Exhibit 2.)

## Profits are more sustainable for exquisite systems.

We mapped the contractor-addressable profit pools for two archetypal platforms: the exquisite F/A-18E/F Super Hornet fighter jet and the expendable AeroVironment Switchblade 300 loitering munition. That analysis shows that the shape of profit pools for expendable systems is not just smaller but fundamentally different.

Exquisite platforms typically derive about half of their lifetime profit from sustainment (over \$10 billion for the Super Hornet across a \$20.3 billion lifetime program). These systems require decades of spare parts support, maintenance, and post-delivery upgrades over their operational lifetime. In contrast, expendable platforms generate nearly all their value through the initial production and purchase. Sustainment after acquisition is typically limited to pre-deployment readiness, software updates, and select few spare parts. (See Exhibit 3.)

The durability of profits from sustainment for traditional primes is significant. Defense spending sees large swings based on wartime demand. In the US, for example, defense budgets fell roughly 37% after the Cold War and 30% to 45% in the drawdowns following operations in Iraq and Afghanistan. Companies that scaled up to meet surge demand were left with stranded capacity and unrecovered R&D. The risk of contracting demand applies today, and it is greater for companies that get the bulk of their profits from volume sales rather than sustainment.

## EXHIBIT 2

# Smaller Defense Programs Are Growing Fast but Will Comprise Only a Sliver of the Overall Market Through 2033

Exquisite systems (\$billions)

![](images/b9164fcb902676150a98200c2c7f959b7de3b0da89b9778d5ca8139cad3eed3c.jpg)  
Affordable mass systems (\$billions)

![](images/532013a2009f47f5a14707fec60b8f1894f7356d5bd3f38c2764cd5b8c310101.jpg)  
Expendable systems (\$millions)

![](images/202d097d0d535b602879e6e8d6f98dca60d08985c2bd2031669ce4feab4008ff.jpg)

Sources: BCG proprietary aviation-defense market model based on program-level budget data; company disclosures; expert interviews; and Tamarack Defense data.

Legacy incumbents dominate defense aviation budgets today, and assuming defense budgets hold steady, that scenario will continue through the coming decade.

![](images/e48051ac253209c603c32ea84f067b28efb188447622cc12346c24662a30883f.jpg)

![](images/9a5b64294e645d36b3b3627ea1da944b3b1ef9c94b75a715ea92b1a2afec021b.jpg)  
■ Tier 1 sensors and communications ■ Tier 1 weapons  
Sources: BCG proprietary profit pool analysis based on program-level budget data/reports (2012 Selected Acquisition Report, GAO, DSCA); company disclosures; industry benchmarks (Aviation Week MRO); expert interviews; and Tamarack Defense data. Note: Includes historical and projected future sustainment expenditure across full program life cycle; reflects contractor-addressable industry EBIT across US and European air-system expenditure; excludes space, counter-UAS, broad munitions, and non-addressable government O&S costs such as military manpower and fuel; UAS = unmanned aerial systems; UAV = unmanned aerial vehicle.

Longer supply chains foster stability. The distribution of profits along the supply chain varies as well. In exquisite programs, Tier 1 suppliers—particularly suppliers of major components like engines, mission and communication systems, and sensors—can capture 40% to 50% of lifecycle profits independently of the platform prime. What legacy primes retain, however, is decades of supply chain qualification, production experience, and familiarity with the compliance and certification requirements that government contracts demand.

Expendable programs have shallower supply chains, with value focused on owning the intellectual property behind a given platform and being the sole source of its production. The companies that sell these systems capture a larger share of a structurally smaller pool, but most currently lack the qualified suppliers and experience with compliance and certification that would help them win larger and more complex contracts.

R&D risks shift to new entrants. New defense solutions flip the risk-reward equation for R&D. Traditional programs often use government-funded development and negotiated fee structures. These cap the potential upside but also reduce the capital at risk for primes during development. (However, the risk allocation varies significantly by contract type.)

In contrast, affordable mass and expendable contractors largely fund their own R&D, often with the aid of venture or private capital, and thus bear the bulk of the financial risk. If they develop a winning idea, they own the IP and become the sole-source provider of an in-demand platform, but they face an existential risk if the idea does not pan out.

Long-term relationships create stability during peacetime. Primes continue to hold a customer relationship even during peacetime, due to sustainment and training needs on platforms. They often have permanent posts at customer bases. There is no similar precedent for new defense technology players unless the technology applies to non-defense missions like border patrol or critical infrastructure security. However, these tend to be different government customers than military. As a result, primes' revenue in this area is far less volatile and reliant on growing defense budgets.

Primes continue to hold a customer relationship even during peacetime. There is no similar precedent for new defense technology players.

# The Value of a Portfolio Approach

For primes that want to compete in the affordable mass and expendable markets, the right approach may be to consider them as part of an overall portfolio that supplements the core business rather than overshadowing it. Specifically, these companies can consider six measures:

\- Get faster and more flexible in how you go to market. Build up your bid capability and gain direct access to nontraditional acquisition channels, such as the US's OTA.

\- Apply an ecosystem strategy. Use partnerships, minority investments, and acquisitions to access innovation more quickly—without committing the time and organizational resources to develop it internally.

\- Rethink how you allocate R&D resources. When developing lower-cost programs, consider accepting more upfront risk in exchange for IP ownership and a larger share of margin pools.

\- Segregate business units with different operating models. Ring-fence affordable mass and expendable businesses with their own P&L. That will help large players with significant overhead compete on price with smaller competitors.

\- Shift to software-native production. Build agile software and hardware upgrades within long-cycle programs.

\- Compete for emerging-markets business. With IP ownership, affordable mass and expendable markets offer more attractive opportunities for non-defense sales.

Exquisite platforms will likely remain the dominant source of profits in the defense industry for the foreseeable future, but incumbents should understand the threat that comes from newer competitors and less-expensive solutions. The question in front of the defense industry is to find strike the balance between legacy platforms and tapping into growth from affordable mass and expendable solutions. The battlefield solution will require both. Winners will understand where long-duration aviation economics still dominate, where faster-cycle autonomy economics are emerging, and where profitable growth will ultimately accrue between the two.

![](images/3cd654617276ca9e487654ef8491007f326011d76168bc366721eacf5be6bb36.jpg)

## About the Authors

![](images/30c90fa5e4cd28c3909392a525602c93c4f85b9ad32bd6867e219707df1630e3.jpg)

## Matthew Bruce

Managing Director and Partner
Chicago
Bruce.Matthew@bcg.com

![](images/bc5ee7cb4338c5eb7fa97dcbfee1a84897022409476bf6abb1c1f017117b2938.jpg)

## Diana Dimitrova

Managing Director and Partner
London
Dimitrova.Diana@bcg.com

![](images/fb8f5902ab12843a8c2b7ee7c65300acbb65d94f5c75860414406f1242ad0907.jpg)

Daisuke Sohta
Managing Director and Partner
Nagoya
Sohta.Daisuke@bcg.com

![](images/8de36a046a4a02b994d18d7229badf22c7c8ffecd130098c6d260440ea49c9f8.jpg)

![](images/1de40ca74edaa9715273717f9ed4967fa676e536e3ce77796b4a50bb198f4313.jpg)

## Brian Hirshman

Global Lead, Aerospace and Defense
Dallas
Hirshman.Brian@bcg.com

## Matt Aaronson

![](images/fd3aa7d05f871ac3d642daf66651ce154320840638d7a9105652fa20e3b9a7ed.jpg)

![](images/caa21fc3e9194b58b54742ca3641ff277fdb11f6a1b3c6f89cc3325c0bfe566c.jpg)

## Rob Stallard

Partner, Aerospace & Defense
Vertical Research Partners
rs@verticalresearchpartners.com

Global Lead, Engineered Products & Industrial Technology
Chicago
Aaronson.Matt@bcg.com

## Greg Mallory

Global Lead, Defense and Security
Washington, D.C.
Mallory.Greg@bcg.com

This document has been prepared in good faith on the basis of information available at the date of publication without any independent verification. BCG does not guarantee or make any representation or warranty as to the accuracy, reliability, completeness, or currency of the information in this document nor its usefulness in achieving any purpose. Readers are responsible for assessing the relevance and accuracy of the content of this document. It is unreasonable for any party to rely on this document for any purpose and BCG will not be liable for any loss, damage, cost, or expense incurred or arising by reason of any person or entity using or relying on information in this document. To the fullest extent permitted by law, BCG shall have no liability whatsoever to any party, and any person using this document hereby waives any rights and claims it may have at any time against BCG with regard to the document. Receipt and review of this document shall be deemed agreement with and consideration for the foregoing.

This document is based on a primary qualitative and quantitative research executed by BCG. BCG does not provide legal, accounting, or tax advice. Parties responsible for obtaining independent advice concerning these matters. This advice may affect the guidance in the document.

Further, BCG has made no undertaking to update the document after the date hereof, notwithstanding that such information may become outdated or inaccurate. BCG does not provide fairness opinions or valuations of market transactions, and this document should not be relied on or construed as such. Further, any financial evaluations, projected market and financial information, and conclusions contained in this document are based upon standard valuation methodologies, are not definitive forecasts, and are not guaranteed by BCG. BCG has used data from various sources and assumptions provided to BCG from other sources. BCG has not independently verified the data and assumptions from these sources used in these analyses. Changes in the underlying data or operating assumptions will clearly impact the analyses and conclusions.

This document does not purport to represent the views of the companies mentioned in the document. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by BCG.

For Vertical Research Partners disclaimers, please go to https://research.verticalresearchpartners.com/en/disclaimer.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.

![](images/3ed4ea5e2cf0764a62206a66790048f94a78a789a34719439caf0c2d9ec710f7.jpg)
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
