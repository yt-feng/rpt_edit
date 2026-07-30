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
# 2025 M&A Report

By Jens Kengelbach, Daniel Friedman, Dominik Degen, Christoph Schweizer, Tobias Soellner, Sönke Sievers, Reeyarn Li, Anant Shivraj, Seddik El Fihri, Jared Feiger, Lucas Garrido, Dhruv Shah, Takashi Yokotaki, Samuele Bellani, Edward Gore-Randall, and Lianne Pot

October 2025

BCG

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

## Contents

04 Introduction
05 The Brave New World of Dealmaking
11 Regional Perspectives
23 The Upside of Uncertainty
30 Capturing the Value of Cross-Border Deals
37 How We Track M&A Activity by Year
38 About the Authors
38 Acknowledgments

![](images/93bf5b8c7350a71995e42a45cc757818dc67017fea1f29c8283e00084bcd9d92.jpg)

# Introduction

The 2025 M&A Report begins by examining current M&A activity—globally and regionally. It then explores how periods of uncertainty present opportunities for dealmakers who possess the capabilities to pursue targeted acquisitions and disciplined geographic expansions. The report also considers how companies can create value from cross-border transactions by skillfully navigating regional complexities, regulatory challenges, and cultural integration.

This year's report has four parts:

\- The Brave New World of Dealmaking. In the first nine months of 2025, the global M&A market demonstrated resilience, steadily recovering despite ongoing challenges reshaping market dynamics. Seasoned dealmakers view today's volatility as an opening not merely to grow or to shrink, but to transform. Amid the prevailing uncertainty, the investment community now expects portfolio moves and growth pivots that it once viewed as optional. At the same time, AI is helping to streamline deal processes and surface hidden value, making transactions faster and smarter. In this new world, the mandate for dealmakers is clear: make selective bold moves, embrace emerging technology, and play for long-term advantage.

\- Regional Perspectives. Despite persistent uncertainty, many dealmakers are moving forward, anchoring deals in clearer theses and distinctive capabilities. Often, this includes adopting a sharper regional focus that provides some insulation from global volatility. To better understand these dynamics, we asked BCG experts in ten regions to describe the current state of their M&A markets and share insights on recent trends and near-term drivers of deal activity.

\- The Upside of Uncertainty. Periods of uncertainty offer exceptional opportunities for companies that are prepared to act with strategic precision. Successful M&A during uncertainty hinges on consolidating your core market position through targeted acquisitions, carefully expanding geographically within your comfort zone, and avoiding overly complex or transformative moves. This disciplined, strategic approach not only mitigates risk but can also unlock significant long-term value, even when markets are at their most volatile.

\- Capturing the Value of Cross-Border Deals. Cross-border M&A activity has declined from 50% of global deal value at its peak in 2007 to approximately 30% today. Even so, BCG research reveals that cross-border deals, when pursued strategically, can create significant value. Transactions within the same geographic region typically outperform deals within the same country or farther afield, as they enable companies to achieve international growth while addressing manageable integration complexity. To succeed, companies must navigate regulatory hurdles, geopolitical volatility, and the more subtle challenges of cultural integration.

By prioritizing these insights in their M&A strategy and carefully managing the complexities of planning and execution, proactive dealmakers can position themselves for success.

![](images/53c6d572e906c50b8f3db6a76bbdfc59eb701b5e3055514a07570d2f10772145.jpg)

# The Brave New World of Dealmaking

By Jens Kengelbach, Daniel Friedman, Dominik Degen, and Christoph Schweizer

In October 2025, the global M&A market's volatile recovery continues, marked by renewed optimism. After navigating significant turbulence earlier this year, the market has shown its resilience, driven by strategic adaptability among experienced dealmakers.

The trend in BCG's M&A Sentiment Index, a leading indicator of future deal activity, has been increasingly positive across all sectors recently, with particularly strong confidence in the technology and energy industries going forward. Yet this recovery unfolds amid persistent geopolitical tensions, regulatory shifts, and economic uncertainties, all of which continue to affect market dynamics.

Rather than being deterred, successful dealmakers are strategically harnessing these uncertainties. Forward-looking executives are transforming their business portfolios through targeted acquisitions and divestitures. They are also applying AI and advanced analytics to accelerate and enhance dealmaking—from identifying high-potential targets and conducting deeper due diligence to streamlining integration. For these leaders, M&A is no longer merely opportunistic; it has become an indispensable strategic tool for shaping the future of their organizations.

## The M&A Market Defies Headwinds

The global M&A market continues to demonstrate resilience, steadily recovering despite ongoing challenges. In the first nine months of 2025, aggregate deal value rose by 10% compared with the same period last year. (See Exhibit 1.)

While headwinds such as geopolitical tensions and changing tariff policies have caused some dealmakers to pause, many others have pressed forward strategically. Transactions with a regional focus, particularly in the small- and mid-cap market sectors, have proven to be more insulated from geopolitical and tariff disruptions. Similarly, deals driven by strategic growth, capability enhancement, or improving resilience continue to advance. North America has been the most active region for acquisitions in terms of value, while the technology sector has led among industries. (See “Region and Sector Insights.”)

Large-scale M&A activity continues to rebound. During the first nine months of this year, the number of megadeals—those valued at \$10 billion or more—reached 27, up from 21 over the first nine months of 2024. While still below the record 40 megadeals in the frenzy of 2021, this uptick signals growing optimism in the market.

Notably, most of the year's largest transactions have been US-focused:

\- Union Pacific announced its \$71.5 billion acquisition of railroad operator Norfolk Southern, marking a major consolidation in US freight transportation.

\- A consortium comprising by Silver Lake Group, Saudi Arabia's Public Investment Fund, and Affinity Partners acquired gaming company Electronic Arts in a deal that values the company at approximately \$55 billion. If completed, it will be the largest leveraged buyout ever (not adjusting for inflation).

\- Tech giant Alphabet pursued strategic growth in cloud security by acquiring software company Wiz for \$32 billion.

\- Electric utility Constellation Energy expanded its footprint through a \$26.9 billion deal for power generator Calpine.

\- Palo Alto Networks reinforced its competitive position by acquiring CyberArk for \$25.1 billion, with the aim of creating an end-to-end security platform tailored for AI.

Despite this positive momentum, the number of large M&A deals (those valued at \$500 million or more) remains near the low end of historical averages. (See Exhibit 2.) This is consistent with broader market sentiment and aligns closely with the BCG M&A Sentiment Index. Meanwhile, SPAC mergers, prominent from 2020 to 2022, have largely reverted to a peripheral role in the broader M&A landscape.

Private equity (PE) and venture capital (VC) activity is trending higher. Global PE deal value rose 38% year-to-date through the first three quarters of 2025 compared with the same period last year, driven by large deal activity such as the mega buyout of Electronic Arts. Similar to the overall M&A market, PE deal volume was broadly on the same level as last year. Technology, media, and telecommunications, industrials, and energy were the three most attractive sectors for financial sponsors.

## EXHIBIT 1

## Global M&A Activity Continues to Slowly Recover

Global M&A activity has recovered from 2021 lows ...  
![](images/d92c3ff992ae2181a8ca08df55229657aee16e67cf31e0559c0bd016c6681789.jpg)  
Sources: Refinitiv; BCG analysis.  
...and momentum is building despite economic and political uncertainty  
Deal value (\$billions) $^{1}$

![](images/541bc2d4be7d80ae51431d7a4eca8935e6b8e591a8abd13840e830911139b55b.jpg)  
Note: Announced M&A transactions comprise pending, partly completed, completed, unconditional, and withdrawn deals, with no transaction size threshold. Self-tenders, recapitalizations, exchange offers, repurchases, acquisitions of remaining interest, minority stake purchases, privatizations, and spinoffs are excluded. $^{1}$ Deal value includes assumed liabilities.

## Region and Sector Insights

The Americas have led global M&A activity over the past nine months, showing significant year-to-date gains, while activity in Europe and Asia-Pacific experienced declines. (See the exhibit.)

The data for 2025 reveals several key developments:

\- Deals involving targets in the Americas had a total value of \$1.26 trillion, an increase of approximately 26% versus the first nine months of 2024. The vast majority of these deals (worth \$1.20 trillion) involved targets in North America, which accounted for 62% of overall global M&A activity. US companies acquired most of these targets. Canada saw an uptick of 96%, returning to above-average levels, and South and Central America grew by 47%.

\- The value of European M&A totaled \$375 billion, a 5% decline against the first nine months of 2024. The UK remained the largest M&A market in Europe, although deal value there decreased by 35%. Deal value also declined strongly in Spain (−58%) and France (−29%). In contrast, aggregate deal value was significantly higher in the Netherlands (263%), Switzerland (109%), Italy (28%), Germany (45%), and the Nordics (31%), the last mostly driven by upticks in Norway (61%) and Sweden (36%).

\- In Africa, the Middle East, and Central Asia, M&A activity—in terms of aggregate deal value—increased slightly (6%) but remains significantly below the average level of the past ten years.

\- Deal value in Asia-Pacific declined by 19% to a ten-year low of \$284 billion. Bright spots included Singapore (38%), mainland China (11%), and Australia (1%). However, the rise in aggregate deal value in these areas did not counter downward trends in other places, such as South Korea (-13%), India (-20%), and Hong Kong (-73%).

The sectors demonstrating the most significant increases in M&A deal value compared with the same period last year were industrials (77%); technology, media, and telecommunications (10%); energy (20%); and health care (20%). Large transactions involving transportation and infrastructure companies were primarily responsible for the industrials sector's strong gains, indicating heightened activity and strategic investment. Conversely, the materials (-16%) and consumer (-17%) sectors saw substantial declines in deal value during the same period, owing mainly to a slowdown in large-scale transactions in these sectors.

## In the First Nine Months of 2025, North America and the Tech Sector Led in M&A Value

M&A value by acquisition target's region
Deal value (\$billions)

![](images/870812c00090f3c47b106cbf7a248a6e53b50963947e2d6e78b83094af524576.jpg)  
Sources: Refinitiv; OECD; BCG analysis.  
M&A value by acquisition target's sector Deal value (\$billions)

![](images/22520238716a06d2fbb94462786fc7486c1bfdefef62590823f8be6a98f2ba04.jpg)  
Note: Announced M&A transactions comprise pending, partly completed, completed, unconditional, and withdrawn deals. Because of rounding, not all bar segment values add up to the total given above each bar.

## EXHIBIT 2

# The Volume of Large Deals Remains Near the Low End of the Average Range

![](images/943812420056c81b7cb09d233009f2eb14ee21ac9ba1640acfce1ade311f0652.jpg)  
Sources: Refinitiv; OECD; BCG analysis.  
Note: Announced M&A transactions comprise pending, partly completed, completed, unconditional, and withdrawn deals, with deal values greater than or equal to \$500 million. SPAC = special-purpose acquisition company.  
$^{1}$ Large deals have values greater than or equal to 500 million. Deal values include assumed liabilities.  
$^{2}$ Volume range is an estimate of the normal range of M&A activity across the entire period tracked in this exhibit.

PE firms continue to sit on substantial dry powder—approximately \$2 trillion in undeployed capital as of early October 2025—maintaining pressure on investors to invest these resources strategically. However, global fundraising for PE has notably slowed since the 2021 peak, evidence of a more challenging environment for attracting fresh capital.

In the VC landscape, funding levels climbed by approximately 36% globally during the first nine months of 2025 compared with the previous year, according to Crunchbase data. Nevertheless, the current level remains below the highs recorded in 2021 and 2022. AI companies continue to be a primary focus for VC investment, especially mega funding rounds, despite ongoing market concerns about high valuations, market saturation, and less certain growth trajectories.

## Improving Sentiment and a Positive Outlook

BCG's M&A Sentiment Index suggests a mixed picture of deal activity across sectors over the next six months. Sentiment is particularly optimistic in the technology and energy sectors, with industrials and consumer showing weaker momentum.

Substantial capital for investment comes not only from PE funds but also from many companies worldwide with robust balance sheets, providing ample resources for strategic acquisitions. Adding impetus, interest rates have generally stabilized or even declined, while valuation levels have recovered.

The market currently reflects substantial pent-up supply and demand. On the sell side, divestiture activity has been modest, as many PE and corporate sellers have strategically delayed asset sales and carve-outs as they await more favorable conditions. On the buy side, many large-scale and cross-border transactions remain temporarily on hold, pending greater clarity for business planning. A similar situation exists for IPOs, with a healthy pipeline of companies ready to go public when the market environment turns more favorable.

... and in times of increased uncertainty
Acquirer returns (2-year relative TSR, %)

Sector-specific trends highlight areas of strong activity: technology remains a key focus that is especially attractive to PE investors. Europe has seen persistent dealmaking activity and rumors involving media companies and financial institutions, including banks, asset managers, and insurers. The energy and utilities sectors are similarly positioned for robust dealmaking activity. The materials, metals, and mining sectors are expected to remain active, too, as certain critical materials gain importance and global supply chains continue to realign. These dynamics are driving large-scale transactions, such as the recently announced merger of two mining giants, the UK’s Anglo American and Canada’s Teck Resources—a \$20.1 billion transaction to form a copper and critical minerals powerhouse. Meanwhile, thanks to high valuations and sustained business momentum, the defense sector presents notable opportunities, particularly for capital raising and IPO activities.

Despite numerous positive fundamental factors, volatility remains a persistent challenge. Political tensions, geopolitical shifts, economic policy uncertainties, regulatory complexities, and rapid technological developments—especially advances in AI and computing—continue to generate market volatility, reinforcing the importance of strategic flexibility and resilience in M&A planning.

## Get Ready for the Brave New World

Amid the uncertainty and complexity, executives must prepare to pursue deals in a landscape that differs in critical aspects from the environment they have been accustomed to. To succeed in this new world, dealmakers need to address several imperatives.

Learn to cope with uncertainties beyond your control. Seasoned dealmakers view uncertainty not as an obstacle, but as an environment in which strategic opportunities emerge. Although recent market disruptions have led to postponed or restructured deals, most transactions ultimately return to the table once conditions stabilize.

Indeed, history shows that periods of turbulence often have the greatest potential for value creation. BCG's analysis highlights that experienced dealmakers consistently outperform peers during downturns or volatile periods. (See Exhibit 3.)

## EXHIBIT 3

## Experienced Dealmakers Generate Value Even Amid Adversity

Serial acquirers outperform in every stage of the business cycle ...
Acquirer returns (2-year relative TSR, %)

![](images/b8be3ce567f7f3b5db6bbbbea5a58636fa89191d205257e11da3c7719d291209.jpg)  
Sources: BCG/Paderborn University M&A study 2025; BCG analysis.  
Note: Strong-economy (weak-economy) years are those in which the respective global real GDP growth rate is in the top (bottom) third. High (low) uncertainty periods are those in which market volatility is in the top (bottom) third based on the semi-standard deviation of global equity returns (Semi-SDRET). Experienced acquirers conducted five or more deals in the past 3 years prior to the observed acquisition; inexperienced acquirers conducted no deals in the past 3 years.

To manage risk and enhance flexibility, expert dealmakers employ alternative, collaborative stru

[中间内容因长度限制已省略]

onths of 2025, BCG's Transaction Center conducted the research that underpins The 2025 M&A Report, our latest edition of BCG's annual publication.

## Data Sets

BCG's M&A research data set (the “M&A database”), which we used as the basis our analyses, comprises approximately 1,033,000 M&A deals covering the period from January 1980 through September 2025. For our assessment of general market trends, we analyzed reported M&A transactions from 1990 through the first nine months of 2025. For our analysis of deal values and volumes, we excluded transactions marked as self-tenders, recapitalizations, exchange offers, repurchases, privatizations, and spinoffs.

In addition to using our proprietary data and analytics, we collected and collated financial data and relied on information from various data providers, including LSEG Workspace, LSEG DataStream, and S&P Capital IQ.

## Long-Term Value Creation

To determine the “announcement return,” we derived the cumulative abnormal return (CAR), by taking the difference between the actual return on the acquirer’s stock () and the return realized in the sector index () as an approximation for expected returns, starting three days before the announcement date (−3d) and ending three days after it (3d). (See Equation 1.)

For M&A deals, we tracked the stock market performance of the acquirers or the sellers over periods of different length following the acquisition announcement. We could not track the targets because, in most cases, they are delisted from the public equity markets.

First, we measured the total shareholder return (TSR) generated by the acquirer or seller over a time period of length t. (See Equation 2.)

$$
\mathrm{CAR} _ {\mathrm{acq}} = \mathrm{P} _ {3 \mathrm{d}, \mathrm{acq}} / \mathrm{P} - _ {3 \mathrm{d}, \mathrm{acq}} - \mathrm{P} _ {3 \mathrm{d}, \text { index }} / \mathrm{P} - _ {3 \mathrm{d}, \text { index }}
$$

$$
\mathsf {T S R} _ {\mathrm{t,acq}} = (\mathsf {P} _ {\mathrm{t,acq}} / \mathsf {P} _ {- _ {3 d, \mathrm{acq}}}) ^ {1 / t} - 1
$$

## EQUATION 2

$$
\mathrm{TSR} _ {\mathrm{t,index}} = (P _ {\mathrm{t,index}} / P _ {- 3 \mathrm{d,index}}) ^ {1 / \mathrm{t}} - 1
$$

## Short-Term and Long-Term Value Creation

Second, we subtracted from the TSR the return that a benchmark index delivered over the same period, in order to find the relative total shareholder return (rTSR) that the acquirer or the seller generated—in other words, the return in excess of the benchmark return. $^{2}$ (See Equation 3.)

Although analyzing different issues required us to use distinct samples, we employed the same econometric methodology to all return analyses.

## EQUATION 1

## Short-Term Value Creation

## EQUATION 3

$$
R T S R _ {t, a c q} = (1 + T S R _ {t, a c q}) / (1 + T S R _ {t, i n d e x}) - 1
$$

We could not include all deals in this analysis because, for some deals, the time elapsed since the announcement was too short to allow us to calculate the returns.

## Statistical Significance of the Results

We applied common-practice statistical significance tests to all of our quantitative results in this report. To assess whether means differed statistically from zero, we used one-sample t-tests; where appropriate, we used two-sample t-tests to determine whether the difference between means differed significantly from zero—that is, whether two groups did in fact have different means.

Generally, for longer-term analyses (such as for one- and two-year rTSR) and for the short-term analysis (that is, for CAR), we used relative measures of size impact (such as deal value compared to the enterprise value of the acquirer) as well as absolute measures of size (such as deal value) to determine whether a transaction was sufficiently material to have had an impact on overall performance.

## About the Authors

## The BCG Team

Jens Kengelbach
Managing Director and Senior Partner
Global Mergers & Acquisitions Leader
Munich
kengelbach.jens@bcg.com

## Dominik Degen

Senior Director, BCG Vantage Munich
degen.dominik@bcg.com

## Tobias Söllner

Partner and Associate Director
Munich
soellner.tobias@bcg.com

## Seddik El Fihri

Managing Director and Partner
Casablanca
elfihri.seddik@bcg.com

## Lucas Garrido

Managing Director and Partner São Paulo
garrido.lucas@bcg.com

## Takashi Yokotaki

Managing Director and Partner Tokyo
yokotaki.takashi@bcg.com

Edward Gore-Randall
Managing Director and Partner
London
gore-randall.edward@bcg.com

## The Paderborn University Team

Sönke Sievers
Chair of International Accounting
soenke.sievers@uni-paderborn.de

## Acknowledgments

The authors are grateful to the following colleagues at BCG's Transaction Center for their valuable insights and support in the preparation of this report:

## Daniel Friedman

Managing Director and Senior Partner
Global Transactions and Integrations Leader
Los Angeles
friedman.daniel@bcg.com

## Christoph Schweizer

Chief Executive Officer
Munich

## Anant Shivraj

Managing Director and Partner
Asia Pacific Transactions & Integrations Leader
Singapore
shivraj.anant@bcg.com

## Jared Feiger

Managing Director and Partner Singapore
feiger.jared@bcg.com

## Dhruv Shah

Managing Director and Partner Mumbai
shah.dhruv@bcg.com

## Samuele Bellani

Managing Director and Partner
Dubai
bellani.samuele@bcg.com

## Lianne Pot

Managing Director and Senior Partner
North America Transactions & Integrations Leader
Los Angeles
pot.lianne@bcg.com

Reeyarn Li
Post-Doctoral Researcher, International Accounting
reeyarn.li@uni-paderborn.de

Ashish Baid, Ouassima El Bouri, Thomas Endter, Daniel Kim, Duc Loc Nguyen, and Francesca Pietrogrande.

![](images/d1f7edc6570646396577b794e7aec50620c12ac39e511b32be1cfe2e3cd87750.jpg)

BCG
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
