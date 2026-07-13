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
BCG

# Keeping Defense Aircraft Mission-Ready

July 2026

By Doug Peck, Brian Hirshman, Lacy Ketzner, Diana Dimitrova, Patrick Frailey, and Greg Mallory

![](images/df66f4065229b52837416eed5c90b36e4bacbdfc9967081043f9a22c5f8c7a6f.jpg)

![](images/c92e0a417b545eea6a753a87b0f0a277680f74651d89eb86fc4732ebe5c0bb28.jpg)

The US Department of War spends nearly a third of its annual budget on operations and maintenance, yet the mission-capable rates for most defense aircraft have fallen steadily for decades.

Roughly 1,900 aircraft are out of service on a given day. Across 49 aircraft types studied by the Government Accountability Office between 2011 and 2021, only four met their annual mission-capable goals in a majority of years. Twenty-six did not meet them in any year. Similarly, in the UK, only one-third of its F-35 fleet was fully mission capable in 2024, far below both UK and global program targets.

Many countries around the world face readiness challenges with their air defenses. The typical response has been to throw resources at the problem: more maintenance staff, more spare parts, more depot capacity, more funding. Yet based on our engagements with military aviation clients around the world, resources are not the limiting factor. Instead, the operating system—the velocity, prioritization, demand discipline, and governance through which those inputs are deployed—is the real chokepoint on mission readiness. In many forces, maintenance systems are decades out of date when compared with commercial best practices. In other cases, the system is solid but forces don’t have the discipline to follow it.

By directly addressing these system elements and improving maintenance processes, armed services can improve mission-capable (MC) rates in aviation by 30% to 50% in 6 to 12 months, without any additional inputs. The measures required are not radically innovative; many are in wide use among commercial aviation fleets. When implemented and executed consistently, they can keep military assets where they belong: airborne and executing missions.

## More Resources, Yet Fewer Mission-Ready Aircraft

A few numbers show the clear disconnect between inputs and outcomes in defense readiness. In the US, the absolute spending on operations and maintenance is roughly double what it was in 2000, when adjusted for inflation. Yet, as the exhibit shows, aviation readiness levels for the Air Force and Navy have decreased 12% to 19% over the same period. The Air Force's fleet-wide MC rate declined to 67% in 2024, the lowest in at least two decades, with a weighted average closer to 62% when accounting for fleet size. (Notably, reported readiness rates can overstate actual fleet availability because they typically exclude aircraft undergoing long-term overhauls, upgrades, or modifications.) The services have more maintainers, more spare parts funding, and more depot capacity than they did a generation ago. Yet MC rates continue to fall.

In France, fighter aircraft and tactical transport aircraft availability fell by 26.5 points and 15 points, respectively, compared with 2014, despite substantial efforts to reform maintenance contracting and structure. Similarly, while Germany's Bundeswehr reported average readiness of $76\%$ across all major weapon systems, combat aircraft readiness averaged only $64\%$ —well below the $80\%$ benchmark commonly associated with highly available operational fleets.

While these figures may be cause for concern, particularly in a time of geopolitical instability, there are solutions. For example, between 2008 and 2018, MC rates for the US Navy's F/A-18 Super Hornet were below $50\%$ , representing billions of dollars of assets grounded. In 2018, the Navy launched a program to improve the rate to $80\%$ , largely by applying the concepts discussed in this publication. Within a year, the service achieved its MC target rate and continued making progress, reaching a fleet record number of mission-capable Super Hornets by 2023. At the same time, per-aircraft maintenance costs fell by approximately half.

The Super Hornet case illustrates a broader principle: the constraint was not inputs. It was the system that converted inputs to outcomes. The same platform, fleet, and maintainers used a different operating model to deliver a radically different outcome.

Despite Increased Investment in the US, Aviation Mission Readiness Has Declined Since 2000

![](images/894b76547a2636421be3f6cd9aace0ac736a3854babc9070befd47a4ac6b42e9.jpg)  
Sources: DoD National Defense Budget Estimates (Green Book); GAO-03-300; GAO-23-106217; GAO-25-107870; CBO; Air & Space Forces Magazine FY2025 Almanac data; FY2027 President's Budget Overview Book (April 2026).  
Note: O&M = operations and maintenance. Spending includes total discretionary and mandatory. FY2027 reflects PB27 request. Readiness is a proxy constructed from publicly available service-average/representative data.

## Identifying the Root Causes to Develop Solutions

Our work across a range of military aviation platforms has consistently identified four root causes for low mission-capable rates.

Highly variable maintenance cycle times. Identical scheduled inspections on the same aircraft type can often take two to three times longer at some squadrons than others. A small number of long-tail events, typically 15% to 20% of all maintenance actions, account for a disproportionate share of total non-mission-capable days. The difference in inspection times across facilities typically comes down to the details of execution: planning discipline, structured and integrated master schedules, ring-fenced maintainer capacity, pre-kitting, standardized work, and avoiding mid-event diversions.

Lack of fleet-wide prioritization. Each unit typically focuses on its own performance and controls its own supply of scarce resources, including maintenance staff, parts, and input from engineers. No entity looks at overall enterprise readiness and reallocates resources to the aircraft most critical to the current mission. Short-term priorities like the current day's flying schedule supersede what is best for readiness overall.

programs. Maintenance programs and inspection requirements accumulate over time, based on historical precedents and OEM specifications rather than current maintenance issues and data from the field. For example, corrosion programs designed for one deployment profile get applied uniformly across a fleet, even to aircraft operating under different conditions.

Ineffective governance. Most services have readiness governance structures—weekly reviews, daily stand-ups, and monthly briefings—but they tend to focus on reporting aircraft status rather than making decisions to improve performance. Many of these structures are delegated to lower-level officers, rather than the three- and four-star leaders who can mandate change.

## Rethinking Maintenance Systems

Each of these root causes has an effective solution. These are not radically innovative actions—many have been in use in commercial aviation fleets for decades. Notably, defense ministries often tell us that versions of these solutions are already in place. But in our experience, they need to be implemented in full, as a coherent, integrated system. Military units can take the following actions to deliver a meaningful difference in mission-capable rates.

## Develop and strengthen the maintenance operations center.

A maintenance operations center (MOC) operates as a central hub of information and a resource allocation engine. It maintains a real-time picture of fleet material condition and has the institutional authority to rapidly address issues. Effective, fleet-level MOCs have strong organizational and data infrastructure. They are directly integrated with supply and engineering systems, and they have the authority to actively redirect parts and personnel to where they can have the biggest impact on fleet readiness.

These entities have strong governance in place, focusing on a handful of leading indicators tied to a specific MC target, with explicit owners and clear escalation paths for issues. AI and data tools are increasingly the differentiator here: services that integrate real-time fleet data into governance forums can identify emerging constraints days earlier, prioritize more precisely, and iterate faster, without adding headcount.

## Develop a demand management program.

Demand management programs track the performance of components and parts and maintain a single, ranked list of degraders—the parts that fail most frequently. Based on that information, military leaders can conduct a cross-functional root-cause analysis of these degraders, determine actions and timelines to improve, and enforce them. In one BCG engagement, we found that the top eight degraders accounted for approximately 20% of total days down for maintenance. A targeted demand-management effort could reduce that number by half.

## Optimize maintenance requirements.

Reducing unnecessary maintenance and inspection requirements to what is truly necessary—based on operational data—can free up maintainer capacity and improve aircraft material condition. A strong program puts the right maintenance solution at the right place, at the right time, with the right crew. The impact can be dramatic: a 20% to 40% decrease in scheduled maintenance labor hours, which translates to gains in MC rates of three to five percentage points.

## Create a supply chain control tower.

When high numbers of aircraft are grounded while waiting for parts, the problem is usually prioritization and visibility. The part exists somewhere in the system, but the service doesn't have a mechanism to locate it and route it to the right aircraft. Or, if a given part is consistently scarce, the enterprise doesn't have the supplier relationships needed to fulfill orders. Supply control towers provide real-time visibility into the location of parts, order status, and administrative lead time, consistently reducing non-mission-capable days without requiring additional investment in inventory.

## Enable the workforce through digital.

Digital technology can help military units make their current maintenance workforce far more productive. In many forces, maintenance processes are still documented on paper logs or isolated, desktop computers. New AI-enabled tools are increasingly prevalent in commercial fleets and can be applied to defense applications as well. These tools can clarify processes in real-time on job sites and create audit trails for each procedure, reducing administrative workloads and keeping wrench-time metrics high. Similarly, troubleshooting generative AI tools and AR- and VR-enabled training can help technicians gain new skills faster.

## What Leaders Can Do Now

To begin closing the gap in mission-readiness, without requiring additional resources, military leaders can immediately begin to implement the following actions.

## Set an explicit North Star goal.

Vague objectives like “improve readiness” aren’t helpful. Organizations do better with a specific, time-bound, quantifiable target: a defined number of mission-capable aircraft by a target date, derived from operational requirements, with a named owner who is formally accountable for results. This kind of specificity forces trade-offs, exposes constraints, and creates the urgency needed to evolve beyond the status quo.

## Accurately diagnose the problem before jumping into solutions.

Mission-capable rates are a lagging indicator. Before designing interventions, leaders can break the broader issue down into its component categories (supply, unscheduled maintenance, scheduled maintenance, and out-of-reporting). Teams can then compare the baseline performance of each category and identify which account for the majority of days lost. If the corrective actions still focus on a request for “more people and more parts,” push the team to try again on root cause analysis. This forward-looking approach can help organizations identify the true underlying issues and focus their actions and accountability accordingly.

## Make readiness an enterprise-wide initiative.

Operational squadrons cannot solve this problem on their own. Top-performing organizations integrate data from across the fleet, leverage advanced AI tools, assemble cross-functional teams, and ensure that root-cause analyses have the right level of urgency and the right level of leadership authority.

## Manage at the fleet level, rather than the squadron level.

Avoid decisions that optimize local metrics at the expense of overall readiness. MOCs perform best when they are centralized and have the insights and clout needed to prioritize across the entire fleet. Restructuring authority in this way requires adjusting operational metrics, so that units aren't punished for missing readiness targets at their level.

## Govern to make decisions and track outcomes.

Effective governance is linked directly to operational performance, with cascading metrics. Avoid status updates or “strategic” meetings that discuss issues but don’t have the operational rigor to identify and implement solutions. Readiness is the daily business of senior leaders, not delegated to their deputies or staffs. The effort of governance teams rises with the scale of the problem: bigger issues require more frequent interventions from more senior leaders. And AI and data tools can be part of the governance and oversight, starting today, to surface constraints faster and reduce the burden of manual processes.

As defense budgets face renewed scrutiny and as recapitalization timelines extend, the armed service divisions that improve readiness within existing budgets and constraints will gain a meaningful strategic advantage over those waiting for more resources. But in a fast-changing world, the time to act is now.

## About the Authors

![](images/42a6b2d9a25edb29ad1d6f7f760ae9b992da6f314deca554d5d726c6254849b1.jpg)  
Doug Peck
Managing Director and Partner
Washington, DC
peck.doug@bcg.com

![](images/e33c4a1e9eca0348e8cf1afd567cd922eb85731d084dbc3b9fc41cd87eacb871.jpg)  
Brian Hirshman
Managing Director and Senior Partner
Dallas
hirshman.brian@bcg.com

![](images/25b354ae8b9c730653a6f920373efeba9c6921ed31b6f180ac54d47eb405051d.jpg)  
Lacy Ketzner
Managing Director and Senior Partner
Philadelphia
ketzner.lacy@bcg.com

![](images/65ec229b2087bf3720cd7d525754e0f85de63ce1d245b50719d95af6f5758f05.jpg)  
Diana Dimitrova
Managing Director and Partner
London
dimitrova.diana@bcg.com

![](images/7505f0ea8830281ff1e5c45d95e1a30e621439e8a5176614cc2a74375153d4a8.jpg)  
Patrick Frailey
Partner
Washington, DC
frailey.patrick@bcg.com

![](images/466f065ede3d264cb7a44c47f95bf2d602ba52269ac56064f737f45b27c4308f.jpg)  
Greg Mallory
Managing Director and Senior Partner
Washington, DC
mallory.greg@bcg.com

## BCG

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.

![](images/7addf9c02d556dca453c724cbfeff05e4a5b46b785613ab0531f617d7f79cbf0.jpg)
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
