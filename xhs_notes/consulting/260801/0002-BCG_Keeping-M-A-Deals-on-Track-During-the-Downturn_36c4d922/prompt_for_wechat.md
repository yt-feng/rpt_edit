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
M&A UPDATE

# KEEPING M&A DEALS ON TRACK DURING THE DOWNTURN

By Jens Kengelbach, Uwe Berberich, Tobias Söllner, and Dominik Degen

THE COVID-19 CRISIS HAS amped up the complexities and stress of M&A more than ever. Many buyers and sellers have postponed, frozen, or aborted deals: in fact, 73% of respondents in a recent BCG M&A Pulse Check survey said that they had seen deal valuations being renegotiated. What's more, dealmakers expect the economic crisis to keep M&A deal volume low and prices depressed for a prolonged period.

Nevertheless, as previous BCG research shows, downturns can offer attractive M&A opportunities, particularly for experienced dealmakers. In fact, by late summer 2020, M&A activity was bouncing back even faster than expected.

The differentiating factor for M&A success is thus deal execution, not the economic climate. With this in mind, we have identified some key dealmaking lessons that can help both buyers and sellers reassess the logic of a particular deal, get a stalled transaction moving again, or make a reasoned decision to abandon a deal. In all situations, creative thinking and agile ways of working are critical.

## Steps for Buyers in the Early Stages

An acquirer considering a deal and trying to get out of the starting block early can take several common-sense steps. The prospective buyer should begin with a ruthless assessment of the pandemic's impact on both its own operations and those of its target. Have circumstances fundamentally changed for either side in ways that clearly undermine the rationale for the deal, such as the ability to realize assumed synergies?

If the strategy and rationale still seem to hold, then the acquirer needs to dig in for some painstaking due diligence. This might even mean scrapping any due diligence done so far and rebooting the process, extending the timeline to consider the impact of the crisis across all due-diligence dimensions. Such an effort could include:

\- Short-term market developments, such as the depth of the recession and changes in price versus volume

\- A midterm outlook, such as the same rate of growth but from a new, lower basis

\- Potential changes to long-term trends as a result of the pandemic, such as a faster shift to e-mobility and an increase in employees working from home

\- Changes in the value chain (for example, supplier consolidation and changes in customer behavior) and the competitive landscape

It's also important to assess how the pandemic could alter the regulatory and political environment.

If the logic of the deal continues to hold up, the next step is to engage in agile scenario planning. This will help the acquirer to better understand the range of possible effects on the business and thus begin to zero in on the right valuation—a truly daunting proposition given today's heightened uncertainty. The buyer should pick several key variables that drive value and then run scenarios for, say, a V-shaped recovery, a U-shaped recovery, and an L-shaped recovery. How sensitive is the target to each of these three scenarios? If the deal makes sense for only one of them, how likely is that scenario to occur?

Once the valuation has been determined, the acquirer can begin to negotiate contract terms. Given today's uncertainty and the range of possible outcomes over the next two years, the buyer and seller might need to agree to share risk in order to keep the deal on track. For example, the two sides might settle on a valuation based on the best-case scenario but with payments occurring in installments, depending on whether certain EBITDA milestones have been reached.

Finally, a prospective buyer also needs to align even more closely than usual with other key stakeholders in the transaction.

Such stakeholders could include financing partners, to secure acquisition financing and define feasible covenants, and board or investment committee members, to shepherd the deal along and address uncertainties.

## Steps for Buyers with a Signed Deal

If a deal has been signed but has not yet closed, the buyer should still conduct a quick assessment of the pandemic's impact on both its own operations and those of its target. This is critical, because if circumstances have fundamentally altered the playing field and undermined assumptions, then the buyer should assess options to abandon the deal—such as by triggering a material-adverse-change clause (if not ruled out) or similar language in the contract.

If the buyer moves forward—whether by choice or by necessity—or if the integration has already begun, the key is to make adjustments fast and act swiftly. Most firms focus their merger integration on three areas: day one, post-close business continuity, and overall value capture. In the current environment, companies are working on what’s important now and over the next three or four months. For example, what will day one look like and how, exactly, will they get there?

This focus on day one readiness might mean postponing some long-term planning to capture value. Alternatively, it could mean just the opposite. If, for example, the long-term plans for integration include shuttering some facilities and reducing headcount, then accelerating those plans, such as by permanently closing some facilities already idled due to the pandemic, might make sense.

It's also important to remember that good talent, especially if working remotely, might be vulnerable. Communication, therefore, is key. This is the time to double down on proactive communication and planning:

\- Devote extra energy to planning a virtual day one experience.

\- Make sure that leaders know how to welcome and integrate new team members virtually.

\- Schedule extra touch points for integration leaders to promote collaboration across teams and help fill gaps.

\- Ensure that practical tools, such as videoconferencing, work flawlessly.

Teams should also continue their integration-planning cadence to promote clear communication and governance. Sharing knowledge will be important.

## Steps for Sellers in the Early Stages

Like buyers, sellers considering a divestiture can take several common-sense steps. A seller should begin with a rapid reassessment of why—and how fast—it wants to sell. In the current environment, which is mostly a buyer's market, valuations will be under pressure. The best course of action might be to wait, if possible. The seller could then use that time to do additional prep work to make the asset more attractive for sale at a later date. For example, the seller could shut down marginal operations that are already idle or reduce headcount by converting staff furloughs into permanent cuts.

If the seller decides to move forward, it should assess how the crisis is affecting prospective buyers. Are those companies still in a position to make acquisitions? Might it be necessary, for example, to expand the universe of buyers to include not only strategic acquirers interested in synergies and access to new markets (but who might now be financially weakened) but also financial buyers, whose focus is on cash flow and optimizing operations (but who might be in a stronger position to do a deal)?

At the same time, a seller should restart the vendor due diligence that it plans to share with potential buyers. Given pandemic-related changes, virtually all previous numbers and assumptions will have to be updated. Although vendor reports are neutral assessments, a seller may also want to adjust how it positions the sale given buyers' different priorities, especially if the buyer universe has been expanded.

## Steps for Sellers in an Ongoing or Halted Process

If the divestiture process is underway and potential bidders have already been contacted—or if restarting an abandoned, halted, or postponed process is desirable—then the seller will need to develop both external and internal views of the divestiture in light of the crisis.

The external view should have two components: a market overview and a demand impact analysis.

The market overview should assess COVID-19's impact on market fundamentals, including top-line economics and the potential shape of the crisis; recovery times by industry and region; and the competitive environment (including a comparison with peers).

The demand impact analysis should include a detailed customer sentiment analysis in key dimensions, such as regions and expenditure categories. It's also important to analyze the development of short- and midterm demand, including sales and profitability across end markets, recovery time frames, and changes in customer needs.

Together, the market overview and demand impact analysis will help sellers understand demand variables and identify concrete ways to respond to specific concerns, thus putting potential bidders more at ease. For example, sellers could give potential buyers more time for due diligence and propose a risk-sharing deal structure, such as taking less money up front and agreeing to EBITDA or other milestones as the basis for future payments.

To develop an internal view of the deal in light of the crisis, sellers must revisit the logic of the divestiture. In addition, executives leading the effort need to confirm that senior stakeholders are still on board with the sale. This internal view should also have two components: operational preparedness and a review of the business plan.

For operational preparedness, the seller should analyze short- and midterm operational resilience and readiness, such as supply chain continuity. (See the exhibit.) It should also assess the divestiture's positioning to participate in a market recovery—and potentially gain market share.

## Meanwhile, the business plan review

should include implications for the top line and the bottom line, in both the short term and the midterm, in areas such as order backlog, regional growth, and margin impact. The seller should also create hypothetical scenarios developed on the basis of sensitivity analyses and update budget and midterm management plans.

DESPITE THE GRAVITY of today's economic crisis, executives should not reflexively end their M&A plans. After carefully reassessing the deal logic in light of current events, some buyers and sellers will undoubtedly decide not to move forward. But strong arguments will be made to keep many deals—probably most—on track during the COVID-19 downturn. Vital to this effort will be patience (such as during the extended due diligence) and creativity (in, for example, risk-sharing and deal structures). For acquirers, in particular, today's environment may offer a rare opportunity to buy assets at very attractive valuations—if they are both bold and careful.

## Three Lenses for Assessing a Company's Transaction Preparedness

## Analyses to assess preparedness

![](images/2983a820b7febf77db69a072210bb3230fdb20a044b82bcbebcb18a658e0c3b6.jpg)

## Suppliers

## Supply chain continuity

□ Degree of diversification of supplier base

☐ Regional footprint of suppliers (for example, their exposure to high-risk countries), including an assessment of the supplier risk index

□ Availability of raw materials and components

☐ Ability to adjust supply chain during crises, including implications for logistics; for example, border closures

□ Sufficiency of inventory levels and critical stock

![](images/dd233b31c6fcfe091e626be2b209d93ca7c57149037fc75a37da7dca0e8ab085.jpg)

## Company

## Operational readiness

☐ Regional footprint of facilities (for example, limited exposure to high-risk countries)

☐ Current production capacities and utilization of facilities

☐ Level of compliance with COVID-19 safety and health regulations

Readiness to ramp-up production; for example, the availability of auxiliary materials

☐ Full-production volumes and growth prospects in the new reality

□ Ways of working in the new reality; for example, the digitization of customer interactions

![](images/d02a8387d106d8115a6256641a8bb677e4b603606e99e84983c0f1dce6a72479.jpg)

## Customers

## Customer situation

☐ Degree of diversification of customer base

☐ Impact of pandemic on key customers, including sales, margins, and utilization of operations

☐ Expected recovery scenarios for key customers

☐ Countermeasures of key customers; for example, a decrease in supplier cost or a change in payment terms

□ Competitor moves and countermoves

Source: BCG.

## About the Authors

Jens Kengelbach is a managing director and senior partner in the Munich office of Boston Consulting Group. He leads the firm's global work in M&A. You may contact him by email at kengelbach.jens@bcg.com.

Uwe Berberich is a managing director and partner in BCG's Düsseldorf office. You may contact him by email at berberich.uwe@bcg.com.

Tobias Söllner is an associate director, transaction & integration excellence, in the firm's Munich office. You may contact him by email at soellner.tobias@bcg.com.

Dominik Degen is a knowledge expert and team manager, focusing on transaction & integration excellence, in BCG's Munich office. You may contact him by email at degen.dominik@bcg.com.

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

## © Boston Consulting Group 2020. All rights reserved. 9/20

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and Twitter.
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
