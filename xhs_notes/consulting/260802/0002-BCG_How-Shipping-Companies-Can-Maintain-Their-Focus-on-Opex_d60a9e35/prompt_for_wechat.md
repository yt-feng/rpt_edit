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
![](images/4d993bcf43359371e1f055406bdd1f9c6f8ce394445661114fbd1a443134f0b3.jpg)

TRANSPORTATION AND LOGISTICS

# How Shipping Companies Can Maintain their Focus on Opex

By Ulrik Sanders and Christoffer Nielsen-friis

ARTICLE APRIL 28, 2026 8 MIN READ

To help shipping companies navigate the ever-shifting global seascape, BCG partners with global shipping companies through its Shipping Benchmark Initiative (SBI) to run class-by-class opex analyses and to help companies maintain cost excellence. Working directly with companies to collect granular opex data, SBI serves as a value-adding clearing-house that delivers customized, actionable insights. Upward of 60 global shipowners and managers participate in the benchmark annually; all shipping companies are invited to join.

In a seascape regularly buffeted by external shocks—pandemics, inflationary pressures, volatile oil prices, and shifting trade-war dynamics—maintaining tight, disciplined control over operating expenses (opex) has long been a strategic imperative for shipping firms. That’s because managing costs is key to both short-term profitability and long-term competitive advantage across the industry.

From the cost-cutting imperative of 2014 to 2019, through the surge in costs driven by COVID-19, and on to the current period of restraint, the past ten years have witnessed considerable volatility. As circumstances changed, shipping companies have struggled at times to master their cost base and to fully understand the factors that matter most in managing their short-term and long-term costs.

Over the past 15 years, BCG's Shipping Benchmark Initiative (SBI) has worked with more than 60 shipping companies to capture spending data and analyze key trends that have affected the industry's opex. After examining the data, we seek to answer two critical questions in this article. What trends and factors affected the industry's opex and thus its profitability over the past decade? And which levers should shipping companies pull to maintain and strengthen their cost discipline and competitive advantage in future?

## A Decade of Cost-Cutting

Over the past decade, opex spending across the shipping industry has been highly variable, falling from 2014 to 2019, rising for the next two years, and then falling again from 2022 to 2024. (See Exhibit 1.) A number of positive and negative factors affected how shipping companies managed their costs. Some, such as inflationary pressures and freight rate cycles, were systemic; others, notably the COVID-19 pandemic, were one-off impacts.

Inflation-adjusted opex per day (2020 \$)

## EXHIBIT 1

Shipping Industry Opex Has Varied Considerably over the Past Decade

![](images/e0b44eb9942df80c5bdd54f624e96c05adba84a986131d1b95e612b5e51db02a.jpg)  
Sources: International Monetary Fund; BCG Shipping Benchmark Initiative. Note: Opex calculated as the arithmetic mean of vessel-class average opex within each vessel type, neutralizing changes in fleet composition over time.

## Before the Pandemic

A cost-cutting paradigm driven by low freight rates from 2015 onward defined the pre-COVID-19 era. From 2014 to 2019, inflation-adjusted opex fell by an average of $2.7\%$ annually, led by a $2.5\%$ drop in crew costs, which account for $50\%$ to $60\%$ of total costs.

This period's focused cost-cutting trend is evident in data for all vessel classes within containers, drybulks, and tankers, indicating a rigorous industry-wide commitment to cost discipline. From 2014 to 2019, the industry achieved a cumulative $13\%$ decrease in opex, adjusted for inflation. And the inflation-adjusted vessel opex as a share of charter rate—the daily amount paid to ship owners for the use of a vessel—was 5 percentage points lower than it would have been if opex had simply grown at the rate of inflation, making the industry more profitable overall. (See Exhibit 2.)

Decrease in opex (%)

Decrease in opex share of charter rates (pp)

## EXHIBIT 2

Cost-Cutting Reduced Opex by 13% and Lowered Opex as a Share of Charter Rates by 5 Percentage Points

Cumulative inflation-adjusted Opex reductions since 2014

![](images/fac5b68e50277c99eddc9786fd888c66fce10bd49028bd97cd06f3089840b676.jpg)

![](images/43ec78292fe13e6fe4330770dce1298e1ada8a6da32fa18cde97d688352d94b0.jpg)  
Sources: Clarkson; International Monetary Fund; BCG Shipping Benchmark Initiative. Note: Charter rates are based on actual data as of August 2024 and reflect half-year and full-year rates. The charter rates are aggregated based on Clarkson's data on tanker, drybulk, and container segments, and are aggregated based on fleet-size-weighted averages to create an adapted benchmark similar to the ClarkSea Index and aligned with the opex methodology applied in the BCG Shipping Benchmarking Initiative. The baseline is assumed to grow in line with the IMF Consumer Price Index. pp = percentage points.

## COVID-19 Upends the Cost Equation

The pandemic rewired income statements in ways that few shipping companies anticipated. From 2019 to 2021, even after being adjusted for inflation, opex rose by 2.5% annually across the industry, with the container and drybulk segments climbing especially quickly, at 3.6% and 4.0% per year, respectively. The cost increase was driven by two factors.

First, as a direct result of the pandemic, two types of cost rose significantly. From 2019 to 2021, driven by travel restrictions, quarantining, and testing, crewing costs rose by 2.6% annually, adjusted for inflation, and freight forwarding costs increased by 11.6% annually, largely owing to pandemic-related disruptions to global supply chains. Despite representing just 60% of typical opex costs, crew and forwarding costs together caused 68% of the 2019-to-2021 rise in opex for drybulk ships and 87% of the 2019-to-2021 rise for tankers. (See Exhibit 3.)

## EXHIBIT 3

Crewing and Freight Forwarding Drove More Than 50% of the Opex Increases During the Pandemic

Nominal opex per day by vessel type, 2021 vs 2019 (\$)

![](images/8feeee6f188ecfa6349895b2b2e54cf916bd5a3d305cc751cfcf7fa27935ca3a.jpg)  
Source: BCG Shipping Benchmark Initiative.  
Note: Opex calculated as the arithmetic mean of vessel-class average opex within each vessel type, neutralizing changes in fleet composition over time. Because of rounding, not all nominal daily opex totals for 2021 equal the sum of their reported segment totals.

In contrast, these costs were responsible for just 51% of the increase in opex for container ships. This difference was due largely to the second factor—the rapid increase in shipping revenues, which led to a relaxation of cost discipline, especially for container and drybulk vessels. By the end of 2021, the Containerized Freight Index had risen above 5,000 points, more than 400% above pre-COVID-19 levels. This trend encouraged companies to shift their strategic focus from cost minimization to revenue optimization. As the benchmark shows, container and drybulk vessels saw the greatest increases in revenue conditions and the largest increases in both pandemic-related costs and non-pandemic-related costs such as lube oil and insurance.

The pandemic affected not only relative industry performance between companies, but also relative performance within a company’s fleet. Intrafleet variance, which measures the variation in opex performance across similar vessels under the same owner, is a key indicator of a fleet’s overall efficiency and of ship owners’ ability to predict their fleet’s performance. During the pandemic, this metric rose to its highest level since the benchmark’s inception, exposing many fleets’ lack of contingency plans in the face of disruptions. (See Exhibit 4.) It also revealed an inadequate level of sharing of effective cost-cutting practices—such as coordination of purchasing and crewing data—among ships within the same fleet. A high degree of intrafleet variance also correlates with opex underperformance across the entire fleet, an issue we examine in a forthcoming article.

## EXHIBIT 4

Opex Variance Within Fleets Widened Significantly During the Pandemic

Intrafleet opex variance (%)

![](images/9d536ebd22132bcd7e3a86e007e793fd2fcc14ada39922ef596f64487caff2b0.jpg)  
Source: BCG Shipping Benchmark Initiative.  
Note: Intrafleet opex variance is calculated as the arithmetic mean across firms in a given year. To ensure that results are not driven by changes in Shipping Benchmark Initiative participants, the analysis is adjusted to select recurring participants. At the firm level, intrafleet opex variance is calculated as the standard deviation of the deviation from a vessel's expected opex, based on its characteristics (including, among others, vessel class and age). pp = percentage points.

## The New Normal

The years following the pandemic pushed the industry back to inflation-adjusted cost decreases, in line with the pre-COVID-19 period. While consumables, lube oil, and maintenance and repair (M&R)—the line items most exposed to inflation—increased following the pandemic, total inflation-adjusted opex actually fell by 2.5%. This was largely because operators managed to keep crew spending flat relative to the exceptionally high levels of 2021 by pulling renewed crew optimization levers, notably nationality switching.

In the coming years, firms will find it necessary to be more cost disciplined than at any time since the onset of COVID-19. Geopolitical instability, for example, will continue to affect the industry, as the conflict in the Middle East makes all too clear. Firms' ability to perform in this challenging market will depend on their ability to remain cost disciplined and pull the right levers.

## Pulling the Right Levers

As the past decade's benchmarking results show, cost competitiveness at both the firm level and the vessel level is especially responsive to two factors: effective application of historically proven cost levers, and the ability to adapt to a dynamic operating environment. Systematic identification and implementation of critical cost-cutting levers have led to improved opex performance, and the SBI benchmark clearly helps ensure an exhaustive, programmatic approach.

Although traditional levers such as crew nationality switching and e-auctions can be effective, our benchmark results indicate that shipping companies must look beyond them. Companies seeking to achieve cost leadership in the years ahead should consider three additional focal areas.

## Build Contingency Plans for “Known Unknowns”

COVID-19-specific line items accounted for the vast majority of the 2021 cost increases, yielding a clear lesson: shippers should build contingency plans for “known unknowns” to avoid the risk of being swamped when the next shock hits. In volatile times, like the present, contingency plans must take into account a wide range of macro risks and provide levers that ensure both resilience (such as the dual sourcing of parts and consumables) and agility (such as framework agreements with drydocking yards across multiple countries).

## Focus on Crewing, M&R, and Drydocking

The industry's overall lack of resilience and agility during the pandemic is evident in the absence of contingency plans to counter higher drydocking costs. On average, from 2020 to 2021, inflation-adjusted drydocking costs rose by $10\%$ to $12\%$ , driven by a combination of the zero-COVID-19 policy in China, higher prices for energy and key materials such as steel, and supply bottlenecks in labor and infrastructure outside China. These costs will probably continue to rise faster than inflation in the coming years. This will exert further pressure on the industry to increase its resilience while also managing other opex costs such as crewing—an area that will be covered in more detail in an upcoming article.

Vessel fundamentals reinforce the challenging outlook on M&R and drydocking costs. Fleets have been aging over the course of a decade in which capacity grew by roughly one-third in the drybulk and tanker segments and by nearly three-quarters in container shipping. According to the UN Conference on Trade and Development, the average vessel age was 13 years in 2024, the highest average on record and two to three years higher than the average a decade ago, despite the order book's recent rise to its highest level since 2016.

This situation is likely to increase the importance of M&R and drydocking in the years ahead as average-age vessels enter their third drydocking cycle. To offset it, firms must rethink processes, including applying levers such as intelligent drydocking schedules, bundled repair campaigns, predictive maintenance, and data-driven spare-parts forecasting.

## Lead Technological Change

To remain at the forefront of cost discipline and stay competitive, shipping firms must pursue both incremental and radical technological innovation. The advent of increasingly sophisticated, cost-efficient ships running on new, lower-cost systems that can operate profitably even at lower freight rates, such as the propulsion systems used by new liquefied natural gas carriers, has increased pressure on firms with older vessels to aggressively cut their opex to remain competitive.

A similar inflection point is emerging with AI and machine learning. A recent BCG survey indicates that companies across all industries plan to increase AI their investment in 2026, with average spending more than doubling relative to 2025 levels. Within the shipping industry, firms must explore capabilities such as big-data-based predictive maintenance to reduce M&R costs and downtime, semi-autonomous ships to lower crewing costs, and live fuel optimization through weather analysis.

## Conclusion

As our SBI benchmark shows, the shipping industry has made considerable progress in controlling opex over the past ten years. Yet the voyage has been turbulent, as demonstrated by the increase in costs during the COVID-19 pandemic. Even so, the industry’s ability to refocus on cost discipline following the pandemic confirms its capacity to adjust priorities swiftly in the face of changing circumstances.

Shipping companies looking to remain competitive must continue to pull historical cost levers while also taking advantage of opportunities to lead through technological change, crewing, M&R, and drydocking. Equally important are the ability to adapt and the readiness to ride out the inevitable storms that will arise in our increasingly uncertain world.

## Authors

![](images/f05d804a5c4e775cd12a8db8d5c1bc2a38d50a44546c5b19cbd27c74de61f21e.jpg)  
Ulrik Sanders  
Managing Director & Senior Partner
Copenhagen

![](images/6c7ad68ddbf5856815afda53f02dfee8c22329e4f7d546ad4984e61fa84154cd.jpg)  
Christoffer Nielsen-
friis  
Student Analyst
Copenhagen
✉

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
