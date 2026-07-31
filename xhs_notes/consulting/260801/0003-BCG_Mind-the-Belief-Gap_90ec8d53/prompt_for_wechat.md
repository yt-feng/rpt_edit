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
![](images/08fb4b0c726a07a2c8fdae60de33010faa10b2e7d663355c9e8cf7a7bc633df1.jpg)

LEADERSHIP DEVELOPMENT

# Mind the Belief Gap

By Fanny Potier and Brittany Heflin

ARTICLE JULY 31, 2026 12 MIN READ

When a leadership team underperforms, the first explanations are often external. The market shifted. A competitor got aggressive. The technology moved faster than anyone expected and planned for.

Sometimes that's the whole story. More often, it's the comfortable version of a harder reality: the team acted on an assumption that it stopped examining.

That was Hubert Joly's diagnosis when he became CEO of Best Buy in 2012. The company had plenty of reasons to blame the market for its struggles. Consumers were moving online. Apple was opening its own stores. Devices were converging. Whatever the precise mix of factors might be, Best Buy was losing ground.

But Joly was not convinced that these headwinds were the fundamental source of the company's difficulties. If some of those same forces were helping Amazon and Apple, then, as he put it, “The wind is probably not the problem. We must be the problem.” That conclusion marked a shift in belief from “the market is doing this to us” to “we're still in charge of what we can change.”

Most leadership teams carry these kinds of unexamined assumptions, whether about the market, their own limits, or what good leadership demands of them.

In a recent BCG survey of 563 senior leaders across 11 markets, $63\%$ said that the senior leaders in their organization are not well prepared for what long-term success will require. The survey also found a sharp split between teams that treat leadership growth as real work and teams that don't. Those that reframe beliefs, practice deliberately, and hardwire new behaviors are $144\%$ as likely as their competitors to outperform and $75\%$ as likely to report strong long-term preparedness. (See Exhibit 1.)

## EXHIBIT 1

Leaders Who Reframe, Practice, and Hardwire Are More Likely to Outperform, but Only 15% Do All Three

![](images/b08ac30fb04c8afa59cefaf66de665a1e455df57dd0e64a929864c9b208dc05b.jpg)  
Source: BCG Global leadership survey, March 2026 (N = 563).
Note: Spearman's rank correlations show statistically significant associations between reframe, practice, and hardwire behaviors and long-term preparedness and competitive performance ( $\rho = 0.15-0.35$ ). $^{1}$ “Senior leaders at my organization actively challenge assumptions about leadership and demonstrate a willingness to adapt their beliefs to meet evolving business and organizational needs.” $^{2}$ “Senior leaders in my organization regularly and intentionally experiment with evolving leadership behaviors in their day-to-day work, seek feedback, and adapt based on what they learn.” $^{3}$ “Senior leaders in my organization consistently work to ensure systems, structures, or routines within the organization reinforce and support leadership growth.”

Reframing beliefs is the hardest of the three changes to implement and the area that most often separates teams that pull ahead from the teams that stall. It’s also the endeavor that most teams get wrong. We call this struggle the belief gap—the distance between what a leadership team knows good leadership requires and what it can actually get itself to do. It closes only when a team, together, surfaces the assumptions that it has been running on, tests to determine which still fit, and changes the ones that don’t.

## Belief Comes First

A belief, in this context, is a shared assumption that a team acts on together: what it treats as possible, what it treats as risky, or what it expects will be rewarded. Although rarely stated outright, beliefs surface in such forms as how a team spends its time, what it does under pressure, and how it reacts to failure.

The stated value of something and the working assumption surrounding it are often very different things. A team may say that it values learning but then treat learning as time away from real work. It may say that collaboration matters but then reward people who look out for themselves. It may say that empathy is essential but then treat it as a soft skill that gets in the way when results are on the line. The working assumptions, not the stated values, are what a team runs on.

A leadership team grows, evolves, and adapts to what the market demands in three ways, and our survey measured all three:

\- Reframe the beliefs that leaders hold.

• Practice new behavior deliberately.

\- Hardwire the new behavior into how the team runs.

Only 15% of the leaders surveyed do all three of these things consistently. Of the three, one carries disproportionate weight: leaders who actively reframe beliefs are 168% more likely to outperform their competitors, a bigger effect than practicing or hardwiring on its own.

Why does belief so often determine whether practice and hardwiring stick? Ginni Rometty, who led IBM through its reinvention, puts it simply: “until you experience it, you don’t really believe it.” You can’t argue a team into a belief. People have to live it before it takes hold, which is why belief is usually where lasting change begins, not where it ends.

Consider the two things that leaders most often credit for their own growth. Having a growth mindset (63%) and embracing discomfort and uncertainty (51%) may sound like capabilities, but both reflect assumptions that leaders hold about themselves. (See Exhibit 2.) A growth mindset means believing that what worked before may no longer be enough. Embracing discomfort means accepting, as Rometty puts it, that “growth and comfort can never coexist”—that there’s no development without going through some discomfort.

## EXHIBIT 2

Leadership Teams Should Reframe, Practice, and Hardwire, but the Highest Return Lies in Reframing Beliefs

Leadership growth accelerators | Q: What factors have most accelerated your growth as a leader? LEADERS WHO LISTED THE SPECIFIED ACCELERATOR AS A TOP 3 FACTOR (%)

![](images/6895f144ad4a69331e5b7926a6f3c47b28d0dc62adb39d61a110b9265b558fea.jpg)  
Source: BCG Global leadership survey, March 2026 (N = 563).

Some leaders won't step into discomfort on their own, and moving them takes more than a good argument. For Rometty, it meant helping them experience the belief rather than debate it, often by drawing on their own history. Most people have weathered something hard; and viewed next to that, a professional risk looks smaller than it might in isolation. When someone had less personal experience to draw on, Rometty would talk through the possible worst-case outcome until it lost its grip, and then help the leader take a small first step and see that it held.

Joly’s own instinct fit a similar pattern. He didn’t start with a strategy offsite. He spent a week working in Best Buy stores, wearing a “CEO in training” badge and asking employees three questions: what’s working, what’s not, and what do you need? The experience shifted his sense of where the truth was and what it would take to act on it: less talking from the top, more doing based on what the floor already knew.

## One Mind Isn't Enough

When one leader holds an unexamined belief, it’s a personal blind spot. When a whole leadership team shares one, it becomes a ceiling to what the organization thinks is possible. Reframing is likelier to succeed on teams drawn from different backgrounds and skills, where discussion and dissent are welcome. It stalls in situations where a team’s shared assumptions and unspoken

norms prevent new ideas from ever surfacing. A single leader can change what she believes, but if she walks back into a team whose shared assumptions haven't moved, the old behavior will pull her back.

Joly’s second shift at Best Buy was to deal with the latter issue. The company had been running as a set of departments each optimizing for itself, and the underlying belief was that value creation is a zero-sum contest, both inside the company and with suppliers. He moved the team to act in support of “one team, one dream, one Best Buy,” putting every officer on a single set of goals and a single bonus tied to the company’s overall performance. The belief had to move across the team, incentives and all. One leader changing his mind would not have been enough.

In many cases, shared assumptions that a team never examines show up later as obstacles that it complains about. When leaders name what gets in the way of their own growth, the most common answers—unclear expectations, lack of strategic clarity, inadequate attention to learning—look like process problems, but each tends to sit on an assumption that no one has questioned. The most frequent of these may be the idea that leadership development is separate from the real work. You can hardwire every system you want, but if the team’s shared belief hasn’t shifted, behavior reverts to its previous norms.

## Leaders Know What Good Looks Like

This is not a knowledge problem. Ask senior leaders which qualities matter, and they will answer without hesitation: empathy, clarity, courage, vision, and the ability to lead across functions and boundaries, which the survey calls superteaming. That list has remained strikingly stable, closely matching the qualities that leaders named in our previous leadership research.

The problem is performance. Teams fall shortest on some of the qualities they rank highest. Empathy is the clearest case: 41% of leaders identify it as a top-three quality, but only 16% say that senior leaders in their organization excel at it, a 25-percentage-point gap. Likewise, clarity shows a 22-percentage-point gap. Leaders fall short exactly where they say they care most. (See Exhibit 3.)

# Leaders Underperform on the Characteristics That Matter Most

Top 5 most important leadership characteristics and performance LEADERS WHO SELECTED THE QUALITY AS A TOP 3 CHARACTERISTIC

![](images/748d336059b015086e8b548ed177b79201d4f9b7ee07875054ce841df90aec71.jpg)  
Source: BCG leadership survey, March 2026 (N = 563).  
Source: BCG leadership survey, March 2020 (N = 503).

Note: Gaps were calculated as the difference between the share of respondents selecting each characteristic as a top 3 priority and the share indicating strong performance; characteristics are ranked by largest positive gaps.  
2“What are the top 3 most important leadership qualities for senior leaders to drive long-term organizational success, employee engagement, and customer satisfaction?”
2“What are the top 3 leadership qualities senior leaders at your organization currently excel at?”

These gaps don't signal a lack of skill. They come from believing that using these qualities would cost them something. The empathy gap arises out of the assumption that real empathy would erode a team's accountability. The clarity gap rests on the assumption that admitting uncertainty would cost a leader authority.

This is where Joly and Rometty landed when we asked them what had been the most difficult thing to change. For Rometty the hardest shift was accepting that empathy takes vulnerability, and that vulnerability builds followership instead of undercutting it. For Joly the hardest thing he had to learn was to say, “I don’t know” and “I need help.” Both leaders approached the question from different directions but landed in the same place: admitting a limit makes a leader stronger.

## How to Start

In order to shift a shared belief, a team must surface the assumptions that it has been running on, examine them together, and be willing to find that some no longer fit. Here are a few ways in:

\- Name the belief underlying the decision. Before making a major call, have the team finish the sentence: “We’re doing this because we believe…” Run it backward on decisions that didn’t land: “We did that because we believed… Was that accurate?” Teams often find that they’ve been acting collectively on an assumption that stopped being true a while ago.

\- Challenge the false tradeoff. Leadership teams often make false choices, such as between individualism and collaboration or between strategic clarity and tolerance for ambiguity. A team needs both. Running a polarity workshop can help surface the belief that a team has defaulted to in situations that call for more of the other side. It treats two seemingly opposed sides as a tension to manage, not a choice to settle once and for all, since the right balance shifts with the business context. The team works from a real decision that it has faced. For example, a team that leans on consensus by default can learn to recognize situations where a call needs fewer voices and a faster owner.

\- Audit the two widest gaps. The empathy gap and the clarity gap arise from beliefs that are consistent across teams: that showing vulnerability will undermine authority, and that admitting uncertainty will create panic. Those beliefs won't shift until they are exposed to light, which is why the right question isn't “How do we get better at empathy?” but “What would have to be true for us to exhibit empathy when the pressure is on?”

\- Treat leadership development as a team sport, not a matter of individual enrichment. The belief that most often blocks leadership growth is that development belongs in a program, separate from actual work. At Best Buy, Joly restructured the way the team worked together, identifying one set of goals and establishing one bonus tied to company performance, so that every officer's incentives pointed the same direction. People who had been protecting their own departments began acting differently. The organization had created the conditions necessary to nurture a different belief.

\- Make the new belief experiential, then wire it in. When Rometty needed to shift the way nearly half a million IBM employees worked, she started with three beliefs, translated them into nine behaviors, and asked the workforce to define what each one looked like at its best. Every meeting opened with a story about one of the behaviors, and the company rewarded and celebrated those stories. Only after that did Rometty hardwire the behaviors into promotion criteria and pulse surveys. A system that is installed before people have lived the belief is easy to ignore. The story has to come first.

Naming beliefs is the easy part. The harder thing is getting a team to look at its own assumptions together, discuss them out loud, and recognize the fact that some of them no longer fit. Most leaders would rather do almost anything else. Joly's teams didn't turn Best Buy around by working harder at what they already believed. They started the comeback by admitting that the market was not the only thing that had to change.

That shift is what separates the teams that move from the ones that stall, and no single leader can make it happen alone.

## Authors

![](images/fd335affbb6b1d8118ce513dbd0d65da805ea4bc398635cf276d1f712721022d.jpg)  
Fanny Potier  
Partner & Director, People Strategy & Leadership Paris

![](images/1bc55652600202117540958685f6ad3061d63228a31f291570e57161c37c6c40.jpg)  
Brittany Heflin  
Associate Director, Leadership, Culture & Change
Houston

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
