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
# THE 2020 M&A REPORT ALTERNATIVE DEALS GAIN TRACTION

![](images/63f6c3e496aeca745e16b25b53897c8935d4fdea7a3fe642ec305d55ae12c5c8.jpg)

BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

![](images/e9730310e0be815f5565819221938edbd86442051191c19f266181ec0cb50056.jpg)

# THE 2020 M&A REPORT ALTERNATIVE DEALS GAIN TRACTION

JENS KENGELBACH

GEORG KEIENBURG

DOMINIK DEGEN

TOBIAS SÖLLNER

ANTON KASHYRKIN

SÖNKE SIEVERS

## CONTENTS

3 EXECUTIVE SUMMARY

10 COVID-19 DERAILS DEAL MAKING
2019 Was the Calm Before the Storm
The Pandemic Disrupted Deal Making in 2020

14 POST-COVID M&A—A DIP OR A TROUGH?
Checking the Pulse of M&A
Divestitures and Distressed Deals Will Increase Significantly
Private Equity and Venture Capital May Quickly Recover
Bold Strategic Acquirers Will Seize Opportunities
Longer-Term Trends May Accelerate

20 THE RISE OF ALTERNATIVE DEAL MAKING
Minority Deals Are Becoming More Common Companies Show Renewed Interest in JV&A Corporate Venture Capital Adds Fuel Motivations and Goals Are Expanding Value Creation Is a Coin Toss Deal Execution and Experience Matter

30 HOW TO WIN IN ALTERNATIVE DEALS
Organizing for Success
Applying the Lessons of Experience

33 APPENDIX I: DATA AND METHODOLOGY

35 APPENDIX II: SELECTED BCG-SUPPORTED TRANSACTIONS, 2020, 2019, AND 2018

37 FOR FURTHER READING

38 NOTE TO THE READER

# EXECUTIVE SUMMARY

THE 2020 M&A REPORT takes stock of an eventful first nine months of the year and looks ahead to how the COVID-19 crisis might shape the new reality for M&A in the coming months and years. In this context of disruption and uncertainty, we examine the increasing popularity of alternative deals. In these deals, rather than acquiring control of and integrating a target, companies acquire minority stakes or establish cooperative arrangements—such as through joint ventures, strategic alliances, or corporate venture capital investments. Alternative deals have been and will continue to be important tools for gaining access to capabilities—so that companies can address not only the current pandemic-induced crisis but also ongoing trends such as technology-driven disruption and the convergence of industries.

It has been an eventful period, to say the least, since our previous annual M&A report. Deal-making activity generally held steady in 2019, with modest single-digit declines in deal value and volume. The decline in activity accelerated in the first four months of 2020, as supply chain disruptions caused by the initial virus-related lockdowns in China proved to be harbingers of the full-scale global economic crisis that lay ahead. Once the magnitude of the COVID-19 crisis became clear, M&A activity shut down as swiftly and abruptly as the overall global economy. And just as the global economy has gradually revived to some extent, so, too, has M&A activity.

In this environment, dealmakers increasingly see alternative deals as effective ways to pursue strategic goals and reduce risk. But, as we shall discuss, a lack of experience among many dealmakers means that they will need to climb a learning curve to capture the benefits.

To analyze alternative deals, we focused our research on joint ventures and alliances (JV&A). We collected a comprehensive data set comprising approximately 180,000 JV&A deals, covering the period January 1990 through June 2020. Of these deals, 75,544 met our study criteria. Leveraging our M&A database of more than 810,000 deals, we also analyzed classic M&A deals, covering the period January 1980 through June 2020. In addition to our quantitative analyses, we conducted two surveys to ask corporate deal-makers about their experience and opinions related to alternative deals.

Although alternative deals and classic M&A represent significantly different deal structures, our research revealed important similarities with respect to investor perceptions and success factors. Investors reward experienced JV&A dealmakers with higher returns, just as they do for experienced dealmakers in classic M&A. Moreover, alternative deals have failure rates similar to those of classic M&A, as well as similar success factors, such as thorough deal execution and dedicated deal teams. Perhaps most important, it is clear that alternative deals are not a passing fad—they are here to stay as essential approaches to creating value through corporate transactions.

## 2019 was the calm before the storm.

\- The number of deals and deal value fell by 5% and 4%, respectively, in 2019 compared with 2018. Deal volume and value were also slightly down compared with the average of the past five years, but they still exceeded the most recent ten-year average. Activity was fueled by 38 megadeals (deals valued at \$10 billion or more), compared with 32 in 2018.

\- Deal multiples—enterprise value divided by EBITDA—held steady in 2019: a median of 13.8x, versus 13.7x in 2018. That was lower than the all-time high of 15x set in 2017, but higher than the long-term average of 12x. Acquisition premiums, on average, rose to 29.0% in 2019 (versus 24.1% in 2018).

## The pandemic disrupted deal making in 2020.

\- M&A activity started slowly in 2020 and then declined sharply when the pandemic took hold—deal volume in April 2020 was 80% lower than in December 2019. As of mid-September, there had been only 15 megadeals in 2020 (compared to 27 in the same period in 2019). None exceeded \$50 billion in value, and only 10 have been announced since mid-March.

\- Across industries, deal volume declined in each sector by 15% to 30% in the first half of 2020 compared with the same period in 2019. However, deal value was actually fairly strong in some sectors, such as financial services, owing to larger deals announced before the onset of the pandemic.

\- For transactions that were not paused or abandoned, the economic crisis swiftly reduced valuation multiples. In the first eight months of 2020, the median deal multiple was 10.5x (versus 13.8x in 2019). Acquisition premiums, in contrast, rose to 30.8%—surpassing the long-term average of 30.7%.

## A historical comparison offers reason for cautious optimism.

\- Initially, the drop-off in M&A activity in the current crisis was worse than in the 2008–2009 financial crisis. But a clearly discernible uptick occurred during June through August, as monthly deal activity returned to the lower end of normal levels.

\- Indeed, the uptick in M&A activity that began in June, including the resurgence in megadeals, suggests that the M&A market has turned the corner in recovering from the crisis—although a return of major COVID-19 lockdowns would likely set back the recovery.

However, many dealmakers expect a prolonged period of low volume and depressed deal prices.

\- Among dealmakers surveyed by BCG, nearly two-thirds do not expect to see a full turnaround in deal volume and prices earlier than next year.

\- Even so, survey respondents said that they see attractive opportunities—approximately 75% said that downturns are as good or better environments for value creation through M&A than “normal” times.

## Divestitures and distressed deals will increase significantly.

\- Some companies that have taken on high debt burdens in the crisis will want to quickly reduce their debt load by divesting businesses (especially those outside their core or those with a disrupted business model) once M&A activity picks up and valuations rise.

\- The number of distressed deals, in particular, is likely to increase as the downturn continues and companies struggle with high debt loads. This is a concern especially for industries encountering disruptions, whether disruptions caused by the pandemic or ongoing disruptions that predate the crisis.

## Private equity and venture capital may quickly recover.

\- The number of private equity (PE) deals in April 2020 was more than 70% lower than in December 2019. PE firms pulled back despite sitting on record amounts of dry powder and facing at least some pressure to invest their committed capital. Looking ahead, we expect PE deal activity to gain more traction toward the end of 2020.

\- A similar dynamic is playing out for venture capital (VC) investments. The number of deals fell significantly in the first half of 2020, while capital invested remained relatively stable. Because VC firms also have record amounts of dry powder, we expect startup funding to rebound quickly.

## Bold strategic acquirers will seize opportunities.

\- Our research shows that deals done in a downturn outperform. Examining the 2008–2009 global financial crisis and its aftermath, we found that the sweet spot for large transformational deals

occurred as soon as uncertainty subsided. At that point, funding became available and market volatility decreased, but targets were still available at a discount.

\- And being bold clearly helps. Our research has shown that acquiring companies outside of the core business during a downturn helps to position a company for success during the recovery. Examples during the 2008–2009 crisis included PepsiCo's acquisitions of its two largest bottlers and BlackRock's acquisition of Barclays Global Investors.

## The pandemic may accelerate longer-term trends.

\- The monetary policy measures implemented to combat the economic crisis mean that low interest rates will persist, which supports deal making on the buy side.

\- Digitization and other disruptive technological megatrends—such as advanced analytics, artificial intelligence, automation, and big data—will continue to be very relevant or become even more relevant in the postpandemic world.

\- In some industries, strong companies will continue their efforts to gain market share or reduce overcapacity by engaging in small serial acquisitions and large-scale mergers. In others, the convergence of industry sectors, such as mobility and technology, will continue to promote deal making.

\- The pandemic might contribute to the reversal of globalization, considering that international borders were quickly closed and cross-border supply chains became vulnerable. However, the regionalization of supply chains will not necessarily diminish M&A activity in the short term.

\- Taken together, these developments and trends—short, medium, or longer term—may drive a need for talent and capabilities that promotes not only classic M&A but also alternative deal types such as joint ventures, strategic alliances, and corporate venturing. Indeed, the crisis appears to be accelerating the trend of using such alternative deal types.

## Minority deals are becoming more common.

\- The most common alternative deals are those in which the buyer acquires a minority stake. During the past several years, the number of minority deals in total and as a share of all deals increased to about 35%, up from 20% to 25% dating back to 1990. The share of minority deals has peaked in turbulent times, such as 2009 and 2020.

\- In some cases, companies structure deals as minority transactions as part of a stake-building process or as a form of co-ownership or co-investment. Companies also acquire minority stakes in the context of JV&A transactions, such as equity alliances or corporate ventures.

## Companies are showing renewed interest in JV&A.

\- Our deal database shows that 2019 saw an all-time high of 11,000 JV&A deals, comprising 1,600 JVs and 9,400 alliances.

\- The recent surge has been driven largely by alliances related to software and IT services, commercial and professional services, and health care equipment and services—indicating that trends such as technological change and the emergence of corporate ecosystems are a motivation. Analyses using Quid, a machine intelligence “discovery tool,” confirmed that global trends are a major factor in promoting the increased use of these deal types.

\- During the past three years, more than half of all JV transactions globally took place in the Asia-Pacific region, while almost two-thirds of alliances took place in North America.

## Corporate venture capital also fuels alternative deal making.

\- The use of corporate venture capital investments, a type of equity alliance, has been growing steadily over the past ten years, with 2018 marking the peak. In 2009, companies invested \$5 billion of corporate venture capital, compared with roughly \$85 billion in 2018 and \$60 billion in 2019. The number of deals has steadily increased as well.

\- Corporate venture capital has also grown as a share of the overall VC market. In recent years, corporate venture capital has represented 7% to 8% of all VC deals and about one-quarter of the total VC invested.

\- These alliances give established companies access to startups' creativity, new ways of working, and proficiency with new technologies, while startups receive a reputational boost and gain access to established players' markets, customers, and industry expertise.

## Motivations and goals are expanding.

\- In a recent BCG global survey of dealmakers, approximately $60\%$ of respondents said that they expect alternative deal volumes to rise in the next five years, and another $25\%$ expect them to stay at today's high level.

\- The two most commonly cited reasons for the growth of alternative deal making are long-term trends—technology (54% of respondents) and business model change (54%). Many respondents (45%) pointed to risk sharing and/or gaining experience as motivations.

\- The findings indicate that the current wave of alternative deals has a much broader range of motivations and goals than previous waves. Rather than addressing specific needs, today's alternative deals have become an essential and sophisticated component of dealmakers' arsenals.

## Value creation in alternative deals is a coin toss.

\- From the perspective of short-term value creation, investors appear to be increasingly receptive to companies' use of JV&A. From 1990 through mid-2020, announcement returns trended higher for both JVs and alliances. Longer-term value creation has been more challenging, however. Less than half of all JV&A deals create returns that outperform their industry after one or two years (as measured by relative total shareholder return).

\- Our survey results reinforce the finding that alternative deals have mixed results in terms of value creation. Respondents said that approximately 40% of alternative deals do not achieve their stated financial and/or strategic goals.

\- As the main reasons why alternative deals fail, respondents cited the absence of a clear roadmap for value creation, KPIs, and monitoring mechanisms; the lack of clearly defined and robust governance; and the absence of a clear strategic rationale.

\- Companies with significant experience (at least three alternative deals per year) report that 61% of their deals are successful, whereas inexperienced companies (two or fewer alternative deals per year) report that 58% of their deals are successful.

## Successful companies adjust to the intricacies of alternative deals.

\- Companies that succeed with alternative deals typically have experience—they do 3.1 alternative deals, on average, per year. They also do 2.5 classic M&A deals, on average, per year.

\- Almost all successful dealmakers have dedicated M&A teams, and approximately 25% have separate teams or individual staff assigned exclusively to alternative deals.

\- Of the most successful dealmakers, 29% use different processes for alternative deals and classic M&A.

\- Successful companies give their alternative deal teams full control during the execution phase. These teams also provide strong support during the 100-day plan and postmerger integration phases, and even beyond.

To maximize value from alternative deals, companies should follow a set of best practices.

\- Get an early start developing a well-thought-out, long-term plan for alternative deals that advances your overall strategy. Unlike some classic M&A deals, alternative deals do not come out of the blue. Periodically review your plan and stick to it throughout the journey.

\- Do not skimp on due diligence, even though that may be tempting given the seemingly lower financial stakes. A detailed and holistic assessment of the target and the overall deal clearly pays off and is as crucial as it is for classic M&A.

\- Clearly define, negotiate, and formalize postdeal governance before signing, and make governance a top-management task.

\- Use people with explicit experience in alternative deals to negotiate and manage these arrangements, and seek external support, if necessary. A “one size fits all” approach to deal making does not work.

\- Define and implement transparent and feasible incentive schemes for key decision makers in the alternative deal process.

# COVID-19 DERAILS DEAL MAKING

THE COVID-19 PANDEMIC ENDED one of the longest economic expansions in recent history. Global real GDP growth in 2020 is expected to be -3.9%, according to Bloomberg Consensus Estimates as of early September, compared with a forecast of 3.1% as the year began. This would be the largest decline on record for the global economy. Considering the strong correlation between the real economy and corporate transactions, it comes as no surprise that global M&A activity also experienced a swift and abrupt downturn in 2020. To set the stage for discussing this turbulent year, we begin by looking back at 2019.

## 2019 Was the Calm Before the Storm

Despite fears of an economic slowdown, global M&A activity saw only modest declines in 2019 compared with 2018—the number of deals and deal value fell by 5% and 4%, respectively. (See Exhibit 1.) Deal volume and value were also slightly down compared with the averages of the past five years, but they still exceeded the most recent ten-year averages.

tions helped to drive an 11% increase in deal value in the regi

[中间内容因长度限制已省略]

 Creators Rankings
An interactive guide by Boston Consulting Group, June 2019

Why Software PMIs Need to Get Agile
A report by Boston Consulting Group,
May 2019

Riding the M&A Wave in Consumer Goods
An article by Boston Consulting Group, April 2019

The M&A Way into Distributed Energy
A report by Boston Consulting Group,
March 2019

Cracking the Code of Digital M&A
A report by Boston Consulting Group,
February 2019

The 2018 M&A Report: Synergies Take Center Stage
A report by Boston Consulting Group, September 2018

How the Best Corporate Venturers Keep Getting Better
A report by Boston Consulting Group,
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
An article by Boston Consulting Group, February 2018

# NOTE TO THE READER

## About the Authors

About the Authors
Jens Kengelbach is a managing director and senior partner in the Munich office of Boston Consulting Group. He is also the firm's global head of M&A, the leader of the BCG Transaction Center, the head of the firm's Transaction & Integration Excellence practice in Germany, Austria, and Switzerland, and a member of the Industrial Goods practice. Georg Keienburg is a managing director and partner in BCG's Cologne office and a core member of the Transaction & Integration Excellence practice and BCG's Transaction Center, focusing on deals in the industrial goods and health care sectors. Dominik Degen is a knowledge expert and team manager in BCG's Transaction & Integration Excellence practice in the firm's Munich office. Tobias Soellner is an associate director in BCG's Munich office. He is an expert on M&A and a core member of the Transaction & Integration Excellence practice and BCG's Transaction Center. Anton Kashyrkin is a project leader in the firm's Munich office and a member of the Corporate Finance task force and BCG's Transaction Center. Sönke Sievers holds the chair of international accounting at Paderborn University.

BCG Transaction Center
BCG's Transaction Center is the hub of the firm's global M&A expertise and provides businesses with end-to-end transaction support, including strategic decision making in mergers and acquisitions, preparing and executing divestitures, and supporting IPOs and spinoffs. The Transaction Center combines BCG's deep sector expertise with our comprehensive knowledge of, and experience in, all aspects of M&A across all sectors and industries. These services complement the process-focused offerings of investment banks. With more than 300 professionals worldwide, we concentrate on the commercial drivers of the business plan and equity story. We help both corporate and private equity clients execute deals efficiently and, more importantly, maximize value. For more information, please visit connect.bcg.com/transactioncenter.

Paderborn University
The authors are grateful for the support provided by Paderborn University, the University for the Information Society, which has a strong foundation in computer science and its applications. Paderborn's Chair of International Accounting, Sönke Sievers, focuses on research related to information processing in financial markets and valuation. Since 2019, he is a principal investigator in two projects of the TRR 266 Accounting for Transparency (https://accounting-for-transparency.de/), which is a transregional collaborative research center funded by the German Research Foundation (Deutsche Forschungsgemeinschaft – DFG). In addition to academic research, he intensively collaborates with business partners to advance knowledge in the fields of corporate finance, accounting, and mergers and acquisitions. For more information, please visit www.upb.de/accounting.

## Acknowledgments

The authors thank Vincent Blum, Debbie Fellmerk, Viet Le, Daniel Kim, and Jan Moritz Zessin for their insights and support in the research and content development of this report. They also thank Gonca Yildrim and Adam Lewis for coordinating the publication, David Klein for his assistance in writing the report, and Katherine Andrews, Kim Friedman, Adam Giordano, Frank Müller-Pierstorff, Shannon Nardi, and Ron Welter for editorial, design, and production support.

## For Further Contact

This report is a product of BCG's Transaction & Integration Excellence practice, which works with its clients to deliver solutions to the challenges identified in this report. If you would like to discuss insights drawn from this report or learn more about the firm's capabilities in M&A, please contact one of the authors.

## Jens Kengelbach

Managing Director and Senior Partner
BCG Munich
+49 89 231 740
kengelbach.jens@bcg.com

## Georg Keienburg

Managing Director and Partner
BCG Cologne
+49 221 55 00 50
keienburg.georg@bcg.com

Dominik Degen
Knowledge Expert and Team Manager
BCG Munich
+49 89 231 740
degen.dominik@bcg.com

Tobias Soellner
Associate Director
BCG Munich
+49 89 231 740
soellner.tobias@bcg.com

Anton Kashyrkin
Project Leader
BCG Munich
+49 89 231 740
kashyrkin.anton@bcg.com

© Boston Consulting Group 2020. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com.

To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com.

Follow Boston Consulting Group on Facebook and Twitter. 9/20

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
