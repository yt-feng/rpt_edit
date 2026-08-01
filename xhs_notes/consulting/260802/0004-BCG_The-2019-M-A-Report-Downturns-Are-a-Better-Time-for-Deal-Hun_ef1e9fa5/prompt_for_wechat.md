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
THE 2019 M&A REPORT
DOWNTURNS ARE A BETTER
TIME FOR DEAL HUNTING

![](images/e52651ff0aeed2f0444d4e0fa15557344ffc1e572555fd6088f792cbedc518e1.jpg)

BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

![](images/a95373fdebd00419bade59377fa78f6ced634fc117aa5d0fb1a98b8fb0d3091e.jpg)

# THE 2019 M&A REPORT DOWNTURNS ARE A BETTER TIME FOR DEAL HUNTING

JENS KENGELBACH

GEORG KEIENBURG

MAXIMILIAN BADER

DOMINIK DEGEN

SÖNKE SIEVERS

JEFF GELL

JESPER NIELSEN

## CONTENTS

3 EXECUTIVE SUMMARY

8 GLOBAL M&A ACTIVITY TAKES A BREATHER
Alarming Trends Persisted in the First Half of 2019
Buyers of Public Targets Lose Investor Support
Four Major Trends

15 DEALMAKERS DO WELL IN DOWNTURNS
Why Do Buyers Outperform in a Weak Economy?
How Do Economic Conditions Affect Execution?
Experienced Buyers Excel in Downturns

21 HOW TO MASTER M&A IN A DOWNTURN
Apply the Lessons of Experience
Boldly Pursue Downturn M&A Opportunities
Use Transformational Deals to Stay Ahead of the Curve

26 APPENDIX I: METHODOLOGY

28 APPENDIX II: SELECTED BCG-SUPPORTED TRANSACTIONS, 2019, 2018, AND 2017

30 FOR FURTHER READING

31 NOTE TO THE READER

# EXECUTIVE SUMMARY

THE 2019 M&A REPORT examines how dealmakers should think about M&A activity in a downturn. Our recommendations are based on a study of the returns of dealmaking throughout the economic cycle. Simply put, our research shows that downturns can be excellent times for dealmaking. But success requires careful preparation, thorough execution, and, especially, bold decision making.

2018 might be remembered as the year that foreshadowed more challenging times ahead for dealmakers. The year got off to a strong start, but overall M&A activity fell sharply over the course of the year. Dealmakers coped with increased volatility in equity markets, decreasing valuations, and macroeconomic and political uncertainty. This turmoil carried over into the first half of 2019 and affected dealmaking around the world. Perhaps most alarming, for the first time since 2011, cumulative abnormal returns (CARs) were negative for acquirers of public targets—an indication that investor sentiment toward M&A is returning to the historical norm.

The net result for 2018, though, was a largely stable year in which global M&A value increased moderately despite declining volume. A 7% uptick left the global value near the five-year average. But after a strong first quarter, deal value declined steadily throughout the rest of the year. The fast start was attributable to a flood of megadeals (deals valued at \$10 billion or more)—17 in the first three months versus 14 thereafter. In the first half of 2019, M&A value stabilized near the long-term average while volume dropped significantly. The rebound in value was propelled by strong levels of North American dealmaking, supported by several megadeals, especially in the second quarter.

What will happen next? Several trends are likely to promote M&A activity. Corporations have ramped up sell-side activities, in some cases seeking to placate activist investors. Similarly, private equity firms are exiting investments to cash in on the returns achieved in the recent positive environment. At the same time, high levels of liquidity and low interest

rates are motivating buy-side activities. In many industries, digitization and the emergence of new business models are driving M&A-enabled transformations.

So far, so good. But the wild card here is the macroeconomic environment. Through several years of persistent political uncertainty and market volatility, the M&A market has remained resilient. Today, however, dealmakers must come to terms with the fact that the global economy is most likely in the later stages of the cycle. Trade wars, Brexit, weakness in China's economy, forecasts of slower growth, and ominous leading economic indicators are among the issues weighing down sentiment in capital markets. With storm clouds building, what can forward-looking dealmakers do to get ready for a recession?

We analyzed a unique data set totaling more than 51,600 deals made over the past 40 years that met our study criteria (out of our total M&A database of more than 750,000 deals). We found that, two years after a transaction, deals made in a weak economy created more value for buyers than those made in a strong economy. Boldness pays off—the outperformance is largely driven by acquisitions outside the buyer's core business segments. And, although occasional buyers create value through acquisitions in weak economies, experienced buyers outperform by a wide margin.

To prepare for dealmaking in a downturn, a company must carefully assess which types of acquisitions will set the foundation for strong growth in the recovery. To emulate experienced dealmakers, it must build the capabilities required to identify critical assets—both within and outside its core business segments—as well as those needed to execute transactions and integrate new businesses effectively.

## Deal value increased moderately, despite declining volume.

\- In 2018, global M&A value increased by about 7%, which is close to the five-year average. Deal volume declined slightly (by 3%), with about 35,800 deals announced during the year. But the annual figures mask a decline in deal value and volume in the second half of the year.

\- Europe and North America drove the global increase in deal value in 2018, with growth rates of 7% and 5%, respectively. Among other regions, only Latin America saw growth in deal value. Deal volume declined in all regions. Some industries posted increases in deal value, owing to outlier effects from a few large deals. However, nearly every industry saw a decline in overall M&A volume.

\- In the first half of 2019, M&A value stabilized near the long-term average. However, several alarming trends persisted. Europe and Asia-Pacific experienced sharp declines in deal value compared with the first half of 2018. Only North America saw an uptick in deal value, with US megadeals fueling the global rebound in M&A. In all regions, deal volume declined versus the first half of 2018. Most industries experienced a decline in deal value versus the first half of 2018—notable exceptions included energy and power and industrial companies, which saw double-digit increases. All

industries saw a decline in deal volume compared with the first half of 2018.

## Buyers of public targets lose investor support.

\- Deal multiples—enterprise value divided by EBITDA—declined slightly in 2018, to a median of about 13.7x. In the first half of 2019, multiples declined further to 13x. That is lower than the all-time high of 15x in 2017 but still above the long-term average of 12x. Acquisition premiums, on average, held steady in 2018 (24.1% in 2018 versus 24.6% in 2017.) In the first half of 2019, they rose to 31.2%—slightly above the long-term average of 30.6%.

\- Acquirers' CARs centered on the announcement date fell to an average of $-0.4\%$ in 2018. Although it is well above the historical average of $-1.1\%$ , this negative figure indicates a shift in sentiment compared with recent years. Targets saw their CARs dip slightly to $18.5\%$ in 2018, still above the average of $14.8\%$ .

## Various trends are shaping the M&A market.

\- Corporate divestitures and spinoffs, as well as private equity (PE) exits, are supporting supply. Although the volume of corporate divestitures fell slightly in 2018, total deal value rebounded to near the recent highs reached in 2014 and 2015. The volume and value of PE exits are also slightly off their peaks, but still at moderate to high levels.

\- High cash levels and dry powder are driving demand. Among the S&P Global 1200 (excluding financial institutions and insurance companies), cash holdings totaled \$2.4 trillion in 2018, down slightly from 2017 but still 21% above the level in 2013. Among PE firms, reserves of dry powder increased by 15%, continuing the streak of annual records.

\- Increasingly, the objective of deals is not to take control of a company but rather to gain access to specific capabilities, talent, or technology or to establish partnerships. The absolute number of venture capital (VC) investments by corporate investors and the relative share in all VC investments (by volume) have doubled since 2013. Two related developments are promoting the shift in emphasis: industry convergence and the emergence of complex corporate ecosystems throughout the business landscape and across industries.

\- In recent years, the M&A market has shown an unusually high level of resilience in the face of persistent political and economic uncertainty. Macroeconomic fundamentals have remained strong enough to support a healthy level of M&A activity. However, the cooldown in the second half of 2018 showed that resilience has its limits.

## Dealmakers can perform well in downturns.

\- Markets reward dealmakers who take the risk of pursuing acquisitions in a weak economy. One year after an acquisition, buyers'

relative total shareholder return (RTSR) is nearly 7 percentage points higher for deals done in a weak economy than those done in a strong economy. After two years, the differential increases to more than 9 percentage points.

\- In a weak economy, acquisitions of businesses outside the buyer's industry (that is, noncore deals) create more value than those within the buyer's industry (core deals): one-year RTSR is 3.9 percentage points higher. In a strong economy, noncore deals destroy value for the buyer (RTSR of $-1.0\%$ ), while core deals preserve value (RTSR of $0.0\%$ ). Investors apparently prefer that companies focus on their core businesses in good economic times, while they appreciate diversification in weak economic times.

\- As a group, weak-economy deals take longer to close than strong-economy deals. This suggests that buyers—despite facing less competition—conduct more thorough due diligence or need more time to get the deal financing in place. The finding holds true regardless of whether the target is in a core or noncore segment of the buyer or whether the buyer is public or private.

## Experienced buyers excel in a weak economy.

\- Experienced buyers can create value from M&A in any economic environment (two-year RTSR of 1.1% in a strong economy and 7.3% in a weak economy). Remarkably, they achieve this value creation even as the overall sample experiences, on average, a negative two-year RTSR.

\- Occasional buyers destroy value in good economic times (two-year RTSR of $-13.8\%$ ). In weak economic times, they are able to deliver some value creation from M&A (two-year RTSR of $1.4\%$ ), but clearly lag behind the experienced buyers' returns.

To master M&A in a downturn, companies must follow a set of imperatives.

\- Apply the lessons of experience so that you can prepare for downturn dealmaking, use M&A to further your strategic objectives, and realistically assess a deal's potential to create value. Experienced acquirers apply their knowledge and outperform occasional dealmakers, especially in core deals in a weak economy.

\- Boldly pursue downturn M&A opportunities to advance your strategic agenda and get ahead of the competition. Successful corporate leaders use dealmaking to shape, remodel, or even completely transform their corporate portfolio.

\- Use transformational deals to stay ahead of the curve. Forward-looking companies that anticipate changes to their industry can use acquisitions in a downturn to tap into emerging revenue streams and profit pools. They can also acquire the complementary skills and capabilities that they need to address changing customer needs or to catch up on technological advances.

\- Take advantage of downturn opportunities—such as lower valuation multiples and targets’ lower standalone profitability during crisis times—to position the company for profitable growth during the recovery. Be bold and stay the course, even in the face of negative investor sentiment. The bottom-line advice for succeeding with M&A in a downturn is clear: Get off the sidelines and into the game, but make sure you are prepared to win.

# GLOBAL M&A ACTIVITY TAKES A BREATHER

TAKEN AS A WHOLE, 2018 continued the streak of good years for M&A activity dating back to 2014. Global M&A value increased by about 7%, which is close to the five-year average. Deal volume declined slightly (by 3%), with about 35,800 deals announced during the year. (See Exhibit 1.)

But the annual figures mask a significant development: both deal value and volume declined sharply in the second half of the year. The first quarter of 2018 was especially strong. The number of megadeals (those valued at \$10 billion or higher) announced in the first three months soared to 17, compared with a quarterly average of six in each of the previous ten years. In contrast, only 14 mega-deals were announced in the remainder of 2018. The slowdown in the second half of the year can be blamed on a number of factors, including increased volatility in equity markets, decreasing valuations, and macroeconomic uncertainty.

Europe and North America drove the global increase in deal value in 2018 with growth

EXHIBIT 1 | Global M&A Value Increased Moderately in 2018 Despite Declining Volume

After a strong start in Q1, M&A activity cooled down significantly...

![](images/04387e8c7aa32edb9cb387728561dd76ec22a6ead72fd43d3df3ae71619f5c3d.jpg)  
Volume and value declined in each of the last three quarters of 2018  
...while total deal value remained stable near the five-year average

![](images/d581a7c877b3520ab2ecf2550e19abd3ab06669ad0c26d73f924e74cc500f7fb.jpg)  
Sources: Refinitiv; BCG analysis.  
Note: The total of 722,785 M&A transactions comprises pending, partly completed, completed, unconditional, and withdrawn deals announced between 1990 and 2018, with no transaction-size threshold. Self-tenders, recapitalizations, exchange offers, repurchases, acquisitions of remaining interest, minority-stake purchases, privatizations, and spinoffs were excluded. $^{1}$ Deal value includes assumed liabilities.

rates of 7% and 5%, respectively. Deal volume declined in all regions. Europe ( $-11\%$ ) and North America ( $-13\%$ ) were largely responsible for the overall global decline.

The value of global cross-border M&A grew by 45% in 2018, while volume followed the overall trend and declined by 6%. The same trend was seen, to varying degrees, on a regional level. Most notably, compared with the peak reached in 2016, outbound M&A from China experienced sharp reversals in both value (-78%) and volume (-31%).

In 2018, some industries posted increases in deal value, owing to outlier effects from a few large deals. However, nearly every industry saw a decline in overall M&A volume. The leader in deal value was the media and entertainment sector, with a 42% increase in 2018 (although volume was actually down by 4%) resulting from large-scale industry consolidation. Two noteworthy deals were US cable company Comcast's \$40 billion bid for Sky and Vodafone's \$22 billion acquisition of German cable operator Unitymedia. The health care industry posted the second-biggest increase, driven by large-scale deals such as the \$60 billion takeover of UK-based biopharmaceutical specialist Shire by Takeda, Asia's largest pharmaceutical company.

Alarming Trends Persisted in the First Half of 2019
In the first half of 2019, M&A value stabilized near the long-term average. However, some alarming trends persisted. M&A volume dropped to 15,400 deals, approximately 3,000 fewer than in the first half of 2018—possibly indicating an end to the current M&A cycle. (See Exhibit 2.)

The rebound in deal value was propelled largely by megadeal activity in North America, especially in the second quarter. Among the 21 megadeals announced in the first half of 2019, the following were the top five in value:

\- United Technologies' bid for Raytheon (\$87 billion)

\- Bristol-Myers Squibb's takeover of rival drug maker Celgene (\$79 billion)

\- Saudi Aramco's majority-stake acquisition of petrochemicals group Sabic (\$69 billion)

\- AbbVie’s bid for Allergan (\$62 billion)

\- Occidental Petroleum Corporation's outbidding of Chevron for Anadarko (\$38 billion)

EXHIBIT 2 | Volume Dropped Significantly in H1 2019 While Megadeals Pushed Value Above Average  
![](images/853cb4fd44de5508aab8416d1ed669a2e020818225bafc54e99b9df9decc8ba0.jpg)  
Sources: Refinitiv; BCG analysis.  
Note: The total of 158,733 M&A transactions comprises pending, partly completed, completed, unconditional, and withdrawn deals announced between 2010 and June 30, 2019, with no transaction-size threshold. Self-tenders, recapitalizations, exchange offers, repurchases, acquisitions of remaining interest, minority-stake purchases, privatizations, and spinoffs were excluded. $^{1}$ Deal value includes assumed liabilities.

Comparing the first half of 2019 with the first half of 2018, deal value declined sharply in Europe ( $-60\%$ ) and Asia-Pacific ( $-45\%$ ). Only North America saw an uptick in deal value (16%), with US megadeals fueling the global rebound in M&A. Each of these regions saw relative declines in deal volume. The sharpest decline occurred in North America ( $-22\%$ ).

The first half of 2019 brought relatively few announced cross-border megadeals, possibly because of increased trade tensions and other geopolitical factors. Newmont Mining Corporation, a US company, acquired Goldcorp, a Canadian competitor, in a stock-for-stock transaction valued at \$10 billion. Barrick Gold Corp's hostile takeover offer for Newmont Mining, valued at about \$23 billion, was announced in the first half of 2019 as well, but later withdrawn.

Most industries experienced a decline in deal value compared with the first half of 2018. However, two industries stood out with double-digit i

[中间内容因长度限制已省略]

oston Consulting Group,
August 2018

What Really Matters for a Premium IPO Valuation?
An article by Boston Consulting Group, July 2018

When Building International Joint Ventures, Set-up Matters
An article by Boston Consulting Group,
May 2018

As Prices Peak, Should Dealmakers Wait for the Next Downturn?
An article by Boston Consulting Group, March 2018

Anatomy of an Ideal IPO Candidate
An article by Boston Consulting Group,
February 2018

The Impact of US Tax Reform on Corporate Strategy and M&A
An article by Boston Consulting Group,
February 2018

The 2017 M&A Report: The Technology Takeover
A report by Boston Consulting Group,
September 2017

Cracking the Code in Private Equity Software Deals
A Focus by Boston Consulting Group,
May 2017

Six Essentials for Achieving Postmerger Synergies
A Focus by Boston Consulting Group,
March 2017

# NOTE TO THE READER

## About the Authors

Jens Kengelbach is a managing director and senior partner in the Munich office of Boston Consulting Group. He is also the firm's global head of M&A, the leader of the BCG Transaction Center, the head of the firm's Transaction & Integration Excellence practice in Germany, Austria, and Switzerland, and a member of the Industrial Goods practice. Georg Keienburg is managing director and partner in BCG's Cologne office and a core member of the Transaction & Integration Excellence practice and BCG's Transaction Center, focusing on deals in the industrial goods and health care sectors. Maximilian Bader is an expert project leader in the firm's Munich office. He is an expert on M&A and a core member of the Transaction & Integration Excellence practice and the BCG Transaction Center. Dominik Degen is a knowledge expert and team manager in BCG's Transaction & Integration Excellence practice in the firm's Munich office. Sönke Sievers holds the chair of international accounting at Paderborn University. Jeff Gell is a managing director and senior partner in BCG's Chicago office. He leads the firm's Transaction & Integration Excellence practice globally. Jesper Nielsen is a managing director and senior partner in BCG's London office. He is a core member of BCG's Transaction Center and its Transaction & Integration Excellence practice.

BCG Transaction Center
BCG's Transaction Center is the hub of the firm's global M&A expertise and provides businesses with end-to-end transaction support, including strategic decision making in mergers and acquisitions, preparing and executing divestitures, and supporting IPOs and spinoffs. The Transaction Center combines BCG's deep sector expertise with its comprehensive knowledge of, and experience in, all aspects of M&A across all sectors and industries. These services complement the process-focused offerings of investment banks. With more than 300 professionals worldwide, we concentrate on the commercial drivers of the business plan and equity story. We help both corporate and private equity clients execute deals efficiently and, more importantly, maximize value. For more information, please visit connect.bcg.com/transactioncenter.

Paderborn University
The authors are grateful for the support provided by Paderborn University, the University for the Information Society, which has a strong foundation in computer science and its applications. Paderborn's Chair of International Accounting, Sönke Sievers, focuses on research related to information processing in financial markets and valuation. Since 2019, he is a principal investigator in two projects of the TRR 266 Accounting for Transparency (https://accounting-for-transparency.de/), which is a transregional collaborative research center funded by the German Research Foundation (Deutsche Forschungsgemeinschaft – DFG). In addition to academic research, he intensively collaborates with business partners to advance knowledge in the fields of corporate finance, accounting, and mergers and acquisitions. For more information, please visit www.upb.de/accounting.

# NOTE TO THE READER

The authors thank Daniel Kim and Fabian Turcinov for their insights and support in the research and content development for this report. They also thank Monika Sturz, Boryana Hintermair, Lisa Chiecchi, and Gonca Yildrim for coordinating the publication, David Klein for his assistance in writing the report, and Katherine Andrews, Kim Friedman, Adam Giordano, Frank Müller-Pierstorff, Shannon Nardi, and Ron Welter for editorial, design, and production support.

For Further Contact
This report is a product of BCG's Transaction & Integration Excellence practice, which works with its clients to deliver solutions to the challenges identified in this report. If you would like to discuss the insights drawn from this report or learn more about the firm's capabilities in M&A, please contact one of the authors.

Jens Kengelbach
Managing Director and Senior Partner
BCG Munich
+49 89 231 740
kengelbach.jens@bcg.com

Georg Keienburg
Managing Director and Partner
BCG Cologne
+49 221 55 00 50
keienburg.georg@bcg.com

Maximilian Bader
Expert Project Leader
BCG Munich
+49 89 231 740
bader.maximilian@bcg.com

Dominik Degen
Knowledge Expert and Team Manager
BCG Munich
+49 89 231 740
degen.dominik@bcg.com

Jeff Gell
Managing Director and Senior Partner
BCG Chicago
+1 312 993 3300
gell.jeff@bcg.com

Jesper Nielsen
Managing Director and Senior Partner
BCG London
+44 207 753 5353
nielsen.jesper@bcg.com

© Boston Consulting Group 2019. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com.

To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com.

Follow Boston Consulting Group on Facebook and Twitter. 9/19

## BCG
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
