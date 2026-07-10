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
# Securing the Oil and Gas Resources of the Future

July 2026

By Rebecca Fitz, Ketil Gjerstad, Jaime Ruiz-Cabrero, Pattabi Seshadri, Odd Arne Sjatil, Martha Vasquez, and Betsy Winnike

![](images/4d6e612d5899bae789183bc7a24810ce79d1731e0a3944b99dfe808de62afa40.jpg)

For the past decade, oil and gas investors have largely de-emphasized how long a company’s reserves would last—instead rewarding capital discipline, returns on existing assets, payout consistency, and balance sheet strength. But that’s starting to change. BCG analysis shows that shareholders are beginning to factor portfolio longevity into their valuation calculations for the first time since the 1998–2008 supercycle. Although relatively small, it is a meaningful shift.

The elevation of longevity as a driver of investment decisions reflects the current reality of the energy transition. Demand for oil and gas has proven stickier-than-expected. At the same time, a decade of capital discipline has thinned the investment pipelines that players depend on for future supply, and the flexible short-cycle projects that partly masked this reality are themselves maturing. Furthermore, recent geopolitical events, including the disruption in the Strait of Hormuz, have heightened the urgency around energy security. Taken together, these developments have significant implications for energy

sustainability, affordability, and security, the three components of the energy trilemma. In this context, a focus on ensuring portfolio longevity is not about boosting overall production but rather replacing existing output as it is depleted. Disciplined, selective upstream investment therefore advances affordability and security while supporting an orderly energy transition—reducing the risk of the price volatility, energy shortages, and reliance on higher-emission sources that underinvestment would otherwise invite.

How companies respond will determine who creates value over the next cycle and who destroys it. Of course, these pressures apply across the sector—though not equally. National oil companies (NOCs) and international oil companies (IOCs) alike face the longevity challenge. But where a company sits in the competitive landscape depends on the depth of its existing portfolio and the strategic flexibility it commands. Both dimensions vary as much within company types as between them.

Against this backdrop, the central question is: Can companies' current upstream portfolios sustain the level of returns investors expect through the next cycle, and what will it take for them to do so?

Having a successful upstream strategy with adequate reserves shapes effective capital allocation for years to come—enabling companies to optimize key value creation drivers including payouts, earnings, and debt levels. It also supports the broader objectives of company owners, whether these objectives are capital market returns or sovereign energy and revenue priorities. Most players will need to take steps to extend the longevity and quality of their portfolios through a combination of organic and inorganic moves and extracting more from existing assets. For the small group of players that enjoy a structural oil and gas surplus, and so are not hampered by longevity concerns, the challenge is maximizing value through better integration across the value chain and having the right partnership model.

![](images/c6931308edc1e395b2ad92ea65fa7bb57017d075aa21cc5809a4f8d0804e7ab9.jpg)

We've found that companies can achieve similar volume outcomes through pathways that have very different risk-return profiles. The companies that outperform will be those that select pathways to replenish oil and gas reserves proactively, based on where they have a genuine right to win. Companies that fail to do this risk repeating the value destruction of previous cycles.

## The upstream sector is entering a more competitive phase

A decade of capital discipline has compressed the future supply pipeline—and the implications are becoming clear at a difficult moment

Geopolitical disruption has sharpened a question the market had largely set aside: Can today's portfolios sustain the returns investors expect through the next cycle?

Portfolio longevity is quietly re-entering the valuation equation for the first time since the super cycle

Companies enter this cycle from fundamentally different positions—and the strategic choices they make now will shape who captures the next decade of value creation

# Capital discipline has thinned the future supply pipeline Capex-to-depreciation ratios have nearly halved over the past decade

![](images/ee1b3731e110f1acb526ac2832bd45964131ea92a5733f357c07e1b3f6da0a90.jpg)  
Sources: S&P Capital IQ; International Energy Agency; BCG analysis.  
Sources: S&P Capital IQ, International Energy Agency, BCG analysis.
Notes: Capex/DD&A ratio for 81 large oil and gas producers by peer group. DD&A = depreciation, depletion, and amortization. IOC = international oil company. NOC = national oil company. E&P = exploration and production company.

# Most companies face a material production decline by 2040 Even after including identified growth projects

NET PRODUCTION 2040 VS 2025 $^{1}$ FOR LARGEST IOCS AND NOCS (%)

![](images/78c26d5d730c6b3717420e196de6a00647721464292a0e5fe519f6fbadd0fb8e.jpg)  
Sources: Wood Mackenzie; S&P Capital IQ; BCG analysis.
Notes: IOC = international oil company. NOC = national oil company. $^{1}$ Gap calculated from total forecast oil and gas production in 2040 compared to 2025, including existing growth projects.

## Much of the remaining upstream value sits in markets controlled by host states and national oil companies

![](images/ddcf941cdb919b29b05b64fc8738755c2016d43766fd9cf1f71a468444c35266.jpg)

![](images/f2e37c174a100d01d5b9f8d6364d422feea5597dca5fe16ce20a51a1f9af049e.jpg)  
Sources: Wood Mackenzie; BCG analysis.
Notes: “Limited access” represents states with restricted foreign access. “Selective access” represents states accessed via select partnerships. NPV at 10% WACC, \$65/bbl base case. NPV = net present value. Tcf = trillion cubic feet. NOC = national oil company.

Winning in upstream will depend on taking a differentiated approach  
![](images/f9c9b7aa4051fe83de39376e70b0d7f09cb376fc05e65956672ce286ea26a9ec.jpg)  
Source: BCG Center for Energy Impact analysis

## The best explorers deliver more discoveries from similar investment levels

![](images/d822c8fde88fbc8d113242c3697d148cc56be8f7b5fe3e7b816893270ef42769.jpg)

Sources: Wood Mackenzie; BCG Center for Energy Impact analysis.
Note: Companies include Aker bp, APA, bp, Capricorn Energy, Chevron, CNOOC, COP, Ecopetrole, Eni, Equinor, Exxon, Galp, Harbour Energy, Inpex, Kosmos, Murphy, Oxy, OMV, ONGC, Pemex, Petrobras, PTT, Repsol, Santos, Shell, Talos, TotalEnergies, Tullow, and Woodside.

## Different starting positions drive different renewal strategies Portfolio depth shapes renewal needs; valuation premiums create strategic optionality

![](images/9f99b8f707f0f7dfd5157e0cefd7dc1a9e0cee4e1480f51ce7a5f2d9e703067b.jpg)  
Sources: S&P Capital IQ; Wood Mackenzie; BCG Center for Energy Impact analysis.
Notes: R/P ratio from YE 2025; EV/EBITDA as of 4/10/2026. Only partially-listed NOCs are included in the data series. r/p ratio = reserves-to-production ratio.

![](images/6b1ceb4c45b0a8efec97076c413a5ef96799e5983d2bd9e6318defde7065e75d.jpg)

## Questions executives should be asking now

Where do we genuinely have a structural right to win?

How much of our renewal plan depends on growth that is economically inferior to the base business?

Does our capital framework preserve the flexibility to act offensively when the cycle or landscape shifts?

Does our strategy translate into earnings durability, payout confidence, and valuation support?

Is our portfolio resilient if geopolitical shocks create sustained volatility in prices or access?

## A More Demanding Environment

Several factors are reshaping the competitive landscape for upstream oil and gas. While some of these factors are making it harder for companies to extend the longevity of their upstream portfolios, they are also making it more important to get their upstream strategies right.

The first is capital discipline. Combined with the redirection of capital into low-carbon businesses that are not generating the earnings that were anticipated, capital discipline has predictably shortened many companies' investment pipelines. The average five-year capex-to-depreciation ratio has nearly halved over the past decade. This was the right response to the value destruction of previous cycles. But lower reinvestment is now compressing near-term supply options at a difficult moment, with geopolitical risk in the Middle East creating uncertainty over a meaningful share of the near-term supply pipeline.

Disruption in the Middle East has sharpened an already intensifying global resource access challenge. High-quality resources (with lower costs and lower carbon emissions) are becoming more concentrated in markets where entry depends on relationships and related factors. For IOCs that don’t already have strong positions in such markets, the window of opportunity to access these resources is narrowing as these factors grow in importance.

The same forces reshaping company strategies are creating both pressure and opportunity for resource-holding governments. While open markets like the US remain critically important—and highly competitive—a significant share of the remaining upstream value in both liquids and gas sits in state-controlled or access-restricted markets, where host governments set the terms on which capital enters. Maximizing the value of those resources over the long term depends on more than ownership; it requires the right partners, with the right capabilities and commitment. The governments best positioned to attract these partners will be those that offer not just access, but stable frameworks, clear terms, and a genuine alignment of interests between state and investor. With capital becoming more selective, governments should do the same in the partnerships they seek.

There are three overarching solutions to the longevity challenge: exploration, M&A, and technology.

## Exploration

Some companies can help solve their portfolio longevity issues through exploration, but this won't work for all and is unlikely to be the main source of new reserves through 2040. Most of what the industry needs is expected to come from existing production or from resources that are under development or already discovered.

For players with the right combination of access, technical capability, and financial structuring discipline, there are real opportunities in the Atlantic margin, the Eastern Mediterranean, and selective markets that are reopening across Africa.

Returns from exploration are highly concentrated, however. BCG analysis shows that, despite similar levels of spending, top performers generate significantly more positive value than laggards. The difference lies in how they manage capital exposure along with subsurface skills—through phased development, infrastructure-adjacent targets, and pre-development farmdowns that optimize partnership structures early and limit capital exposure before the highest-risk spending starts. Advances in development technology have made this model increasingly viable, creating a flexibility that has fundamentally changed the economics of exploration.

## Mergers and Acquisitions

M&A is another option for companies seeking to replenish their oil and gas reserves. However, the benefits of deal making vary widely. For companies with high valuations, it enables them to use their paper as a sought-after currency to achieve their renewal plans. But for resource-constrained companies, M&A is often most attractive when it is most dangerous—increasing the risk of overpaying for assets, eroding strategic flexibility, and potentially destroying value through the cycle.

## Technology

The biggest game-changer in enabling players to extend their portfolios could be technology. Players with genuine technical depth create value in two reinforcing ways: extracting more from their existing resource bases, and opening doors to new ones.

In terms of existing resource bases, currently some of the world's largest holders of conventional reservoirs recover less than half the average for their peer group. Innovations in equipment—including smaller and more mobile surface infrastructure; floating production, storage, and offloading units; and multiphase subsea boosting pumps—have already transformed the economics of offshore recovery and continue to do so. AI-enabled subsurface modeling is creating further headroom. The most consequential frontier may be shale: if enhanced oil recovery technologies could double recovery factors to around 15%, it would go a long way toward meeting future resource needs. Many technological pathways are being explored today, including creating fractures to expose oil to the wellbore, using chemical agents to release oil from the pores, or injecting $CO_{2}$ . But achieving this goal depends on companies making deliberate strategic choices and carries real technical risk, and the winning approach is far from settled.

The second way to create value is using technical capability as an access key. In markets where resources are controlled by host states, the basis for partnership rests on what a company can genuinely offer—whether that’s subsurface expertise, a strong execution track record, or development innovation. Players that have built deep capabilities in these areas find that doors are opened to them that remain shut for purely financial competitors.

While either route demands genuine capability and deliberate commitment, the returns for those that get it right are substantial.

## Responding to the New Upstream Reality

Companies do not enter the approaching cycle from the same starting position. The right strategic response to an upstream environment where competition and resource access are getting tougher depends on where a player sits across two dimensions: the depth of its existing portfolio and the strategic flexibility its valuation provides. In this context, valuation matters not as a scorecard but as a source of optionality. A strong valuation benefits companies via equity-financed M&A, cheaper capital, and the ability to act decisively when others cannot. It is the product of responsible capital management through the cycle—and it has a compounding effect. Companies that have maintained capital discipline enter the cycle with genuine strategic choice, while those that have been less disciplined face a more constrained set of options.

Based on these dimensions, BCG's analysis places leading oil and gas companies—among them both IOCs and NOCs—within one of four categories. While there is some overlap between the companies in different categories, each category has a distinct strategic logic for pursuing portfolio longevity. (See “Different starting positions drive different renewal strategies” on page 6 for a visual representation.)

## Deploy and Extend

Companies with both portfolio depth and strategic flexibility enter the cycle from a place of genuine strength. Their priority should be to extend resource positions selectively within the narrowing set of high-quality opportunities, without overextending beyond positions where they have a genuine right to win. The risk for this group is not scarcity of options but maintaining discipline in choosing from among them. They also need to anticipate how more constrained competitors will act under pressure, as this can reshape the opportunity set faster than internal planning cycles allow.

## Act Now

Companies with strong valuations but thinning portfolios still hold an important strategic card. A strong valuation makes inorganic moves accretive in a way that simply isn't available to lower-valued peers paying the same nominal premium. In addition, given the volatile geopolitical environment, resource positions that are available today in difficult-to-access markets may not be available on the same terms, or at all, in a few years. The risk these players face is overpaying for assets or spreading capital thinly across too many positions and plays simultaneously, eroding the valuation advantage that made action possible in the first place. Selectivity is paramount: players need to identify one or two renewal opportunities that can compound over the next decade, and concentrate their firepower here rather than hedging across multiple bets.

## Define and Focus

Players with weaker portfolio depth and more limited financial flexibility face the hardest conversations at a C-suite level. Pursuing growth without advantage (whether based on capabilities, access, or the benefits of a strong valuation) will destroy value. The constructive path involves improving technology deployment to increase recovery factors and utilizing aggressive high-grading around a genuinely advantaged core of resource positions—which requires hard choices about where to concentrate and where to exit. That is difficult to execute and harder to communicate to investors, but it can be done effectively.

Partnerships are particularly important with high-grading, as a way to create scale and share capital exposure around existing positions. The most instructive recent examples are in mature basins. They typically extend across country borders and create operational scale neither partner could achieve alone, or they involve forming standalone vehicles that enable companies to attract independent capital while retaining strategic influence. These moves don’t require new resource access or involve frontier risk. But they do require players to have the discipline to consolidate deliberately rather than managing subscale complexity indefinitely.

## Unlock the Value

Players with strong portfolios but valuations that don't reflect this strength face a different challenge: developing a credible narrative that connects portfolio quality to future cash generation. Until this valuation gap closes, their strategic flexibility will remain constrained. Their priority is not just demonstrating oil and gas delivery but actively closing the gap—through simplification of the business, balance sheet discipline, and a credible investor narrative that connects portfolio quality to future cash generation.

Although they will differ by portfolio depth and strategic flexibility, all major upstream players will enter the approaching industry cycle with genuine and hard-won strengths—whether in subsurface, project execution, enhanced oil recovery within shale and tight reservoirs, trading, or geopolitical relationship management. Companies need to ask themselves if the technical or relationship strengths they possess today align with the resource pathways (in, for example, deepwater or LNG) that are open to them. Where gaps exist, they must decide whether to use targeted M&A, partnerships, or organic moves to close them.

BCG's scenario-planning work with leading upstream players consistently shows that companies can achieve similar volume outcomes via pathways that have materially different risk-return profiles—in other words, pathways that diverge sharply on cash flow quality, capital intensity, above-ground risk, and capability requirements. The standout winners over the approaching cycle will not all have the same starting position. But players that outperform will share one aspect: they will be honest about where they have a real advantage over peers, enabling them to make better and more deliberate pathway decisions and execute their strategies more effectively.

In an environment where portfolio longevity is again becoming part of the valuation equation, the cost of not answering these questions clearly—and then acting decisively—is growing.

## About the Authors

![](images/4d6de06e29ae76e53e6810c5606475d7f965f8067feb8341ac6a35b04bdfee12.jpg)

## Pattabi Seshadri

Pattabi Seshadri
Managing Director and Senior Partner
Global Leader, Energy Practice
Dallas
seshadri.pattabi@bcg.com

![](images/13acadef9e369d4401659e1bb3c4fba9b8fce00537faf567f6fd8ad2a2815494.jpg)

Rebecca Fitz
Partner and Director,
Center for Energy Impact
Washington DC
fitz.rebecca@bcg.com

![](images/6ce501e3c0db254073d529ece40d23adf7e3b6c24485a419cb86af4b436ce2aa.jpg)

## Ketil Gjerstard

Managing Director and Senior Partner
Oslo
gjerstard.ketil@bcg.com

![](images/332dc2b78e62dc1319bcc18382230decbb7836c025c10e69ef53e5e3fc2e33ef.jpg)

## Betsy Winnike

Senior Manager,
Energy Vantage team
Washington DC
winnike.betsy@bcg.com

![](images/7b83f39d7ac28b04cadc1ac0e72accab699667e55c2c52db793c6140438b33eb.jpg)

![](images/851b3ca2ee50f9a32ffceb21ce1de70caec4bae7cc476ceab48b30716b38add0.jpg)

## Jaime Ruiz-Cabrero

The authors thank Håvard Holmås, Olivia Weber, Rachit Sharma, Steven Ho, Obel Chin, and Borja Jimenez for their contributions to this article.

## Acknowledgments

Managing Director and Senior Partner
Madrid
ruiz-cabrero.jaime@bcg.com

![](images/cab26aa3fdd26420677c219592e5dacda26eeabb8457c99153524652e69e4889.jpg)

Odd Arne Sjåtil
Managing Director and Senior Partner
Oslo
sjatil.oddarne@bcg.com

## Martha Vazquez

Partner and Associate Director
London
vasquez.martha@bcg.com

## Boston Consulting Group

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

## The Center for Energy Impact

The Center for Energy Impact (CEI) shines light on the energy transition, focusing on the actions required to achieve global transformation. CEI applies a holistic perspective to understanding and shaping bold responses to one of the most critical and complex challenges of our time.

Our deep expertise spans markets and economics, carbon and technology, capital and investors, the macrodynamics of geopolitics and resilience, and the microdynamics of politics and specific policies. We offer nuanced, constructive ideas and solutions covering the future availability, economics, and sustainability of the world's energy sources—and the implications for energy companies, industries, investors, consumers, and governments. The CEI team is committed to facilitating informed, innovative discussions to make our world sustainable.
"""
