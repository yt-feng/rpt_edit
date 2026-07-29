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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# The state of AI

How organizations are rewiring to capture value

Alex Singla  
Alexander Sukharevsky  
Lareina Yee  
Michael Chui  
Bryce Hall

March 2025

![](images/00abe614f19d434dc86ddbc74db43b4bfd036ebeb5ae21f62de057418c2d3770.jpg)

Organizations are beginning to create the structures and processes that lead to meaningful value from gen AI. While still in early days, companies are redesigning workflows, elevating governance, and mitigating more risks.

![](images/eb7684cb3c0cc2bad00ef2fc5b287c15cbdabf0bea3f5f58b70bab46f821b8b7.jpg)

![](images/756111a7c61024f1cb95de58808948ed4f9d2c8544e87a534ebc45a07732542c.jpg)

organizations are starting to make organizational changes designed to generate future value from gen AI, and large companies are leading the way. The latest McKinsey Global Survey on AI finds

that organizations are beginning to take steps that drive bottom-line impact—for example, redesigning workflows as they deploy gen AI and putting senior leaders in critical roles, such as overseeing AI governance. The findings also show that organizations are working to mitigate a growing set of gen-AI-related risks and are hiring for new AI-related roles while they retrain employees to participate in AI deployment. Companies with at least \$500 million in annual revenue are changing more quickly than smaller organizations. Overall, the use of AI—that is, gen AI as well as analytical AI—continues to build momentum: More than three-quarters of respondents now say that their organizations use AI in at least one business function. The use of gen AI in particular is rapidly increasing.

# How companies are organizing their gen AI deployment—and who’s in charge

Our survey analyses show that a CEO's oversight of AI governance—that is, the policies, processes, and technology necessary to develop and deploy AI systems responsibly—is one element most correlated with higher self-reported bottom-line impact from an organization's gen AI use. $^{1}$ That's particularly true at larger companies, where CEO oversight is the element with the most impact on EBIT attributable to gen AI. Twenty-eight percent of respondents whose organizations use AI report that their CEO is responsible for overseeing AI governance, though the share is smaller at larger organizations with \$500 million or more in annual revenues, and 17 percent say AI governance is overseen by their board of directors. In many cases, AI governance is jointly owned: On average, respondents report that two leaders are in charge.

The value of AI comes from rewiring how companies run, and the latest survey shows that, out of 25 attributes tested for organizations of all sizes, the redesign of workflows has the biggest effect on an organization's ability to see EBIT impact from its use of gen AI. Organizations are beginning to reshape their workflows as they deploy gen AI. Twenty-one percent of respondents reporting gen AI use by their organizations say their organizations have fundamentally redesigned at least some workflows.

# Twenty-eight percent of respondents whose organizations use AI report that their CEO is responsible for overseeing AI governance.

$^{1}$ The correlation analyses considered 25 attributes and the reported effect of gen AI use on organizations' EBIT, and using the Johnson's Relative Weights regression analysis yielded an R-squared of 0.20. The attributes included which leaders oversee AI governance at organizations, how organizations are managing the time saved by gen AI deployment (for example, assigning completely new activities and fewer hours to employees, reducing head count), whether organizations have fundamentally redesigned at least some of their workflows as a result of gen AI deployment, and whether they have adopted each of 12 gen AI adoption and scaling best practices: 1) establishing a dedicated team to drive gen AI adoption (for example, a project management office, transformation office, or dedicated adoption and scaling team); 2) having regular internal communications about the value created by their gen AI solutions to build awareness and momentum; 3) having senior leaders who are actively engaged in driving gen AI adoption, including role modeling the use of gen AI; 4) embedding gen AI solutions into business processes effectively (for example, changing frontline employees' processes, creating user interfaces to incorporate gen AI solutions); 5) establishing role-based capability training courses to make sure employees at each level know how to use gen AI capabilities appropriately; 6) creating a comprehensive approach to foster trust among employees in our use of gen AI (for example, understanding primary sources, mitigating inaccuracies); 7) having a mechanism to incorporate feedback on the performance of gen AI solutions and improve them over time; 8) establishing a clearly defined road map to drive adoption of gen AI solutions (for example, with phased rollouts across teams and business units); 9) establishing a compelling change story about the need for gen AI adoption; 10) tracking well-defined KPIs for gen AI solutions, enabling insights into their adoption and ROI; 11) establishing employee incentives that reinforce gen AI adoption; and 12) creating a comprehensive approach to foster trust among customers in our use of gen AI (for example, transparency on regulatory compliance, use of customer data).

# Twenty-one percent of respondents reporting gen AI use by their organizations say their organizations have fundamentally redesigned at least some workflows.

![](images/e821c97ecaaef5c1244a8632091fcb8ff2afb11f4c5f9094f30123434e1ffa0f.jpg)

## McKinsey commentary Alexander Sukharevsky Senior partner and global coleader of QuantumBlack, AI by McKinsey

The more we see organizations using AI, the more we recognize that it takes a top-down process to really move the needle. Effective AI implementation starts with a fully committed C-suite and, ideally, an engaged board. Many companies' instinct is to delegate implementation to the IT or digital department, but over and over again, this turns out to be a recipe for failure.

There are several reasons for this. The first is that getting real value out of AI requires transformation, not just new technology. It’s a question of successful change management and mobilization, which is why C-suite leadership is essential. It’s also a potentially expensive transformation, requiring intensive use of sometimes scarce resources and talent. A lot rides on how those resources are made available, and that’s an executive-level call requiring nuanced decision-making that reflects the balance organizations must strike between efficient resource use and broad empowerment—a balance that must be constantly reevaluated as the technology and organization evolve.

As organizations become more fluent with AI, it will essentially become embedded in all functions, leaving leadership to focus on higher-level tasks like impact monitoring and talent development rather than on implementation.

## Organizations are selectively centralizing elements of their AI deployment

The survey findings also shed light on how organizations are structuring their AI deployment efforts. Some essential elements for deploying AI tend to be fully or partially centralized (Exhibit 1). For risk and compliance, as well as data governance, organizations often use a fully centralized model such as a center of excellence. For tech talent and adoption of AI solutions, on the other hand, respondents most often report using a hybrid or partially centralized model, with some resources handled centrally and others distributed across functions or business units—though respondents at organizations with less than \$500 million in annual revenues are more likely than others to report fully centralizing these elements.

Exhibit 1

Risk and data governance are two of the most centralized elements of deploying AI solutions, whereas tech talent is often hybrid.

Degree of centralization of AI deployment, $^{1}$ % of respondents

![](images/96db87b310ea75f90688beeeaca4bbdcf35b8e7c0ce3da15573819dea742b6da.jpg)

Twenty-seven percent of respondents say employees at their organizations review all content created by gen AI before it is used, and a similar share says that 20 percent or less of gen-AI-produced content is checked.

## Organizations vary widely in how they monitor gen AI outputs

Organizations have employees overseeing the quality of gen AI outputs, though the extent of that oversight varies widely. Twenty-seven percent of respondents whose organizations use gen AI say that employees review all content created by gen AI before it is used—for example, before a customer sees a chatbot’s response or before an AI-generated image is used in marketing materials (Exhibit 2). A similar share says that 20 percent or less of gen-AI-produced content is checked before use. Respondents working in business, legal, and other professional services are much more likely than those in other industries to say that all outputs are reviewed.

Exhibit 2

Respondents are about equally likely to say their organizations review all gen AI outputs as they are to say few are reviewed.

Share of gen AI outputs reviewed before usage, $^{1}$ % of respondents

![](images/82f9470a442d221f819c131b8167d18641c50d47f56ef19e19668ea6f323a986.jpg)

$^{1}$ Only asked of respondents whose organizations regularly use gen AI in at least 1 function. Figures were calculated after removing the share who said “don’t know”; n = 830.
Source: McKinsey Global Survey on the state of AI, 1,491 participants at all levels of the organization, July 16–31, 2024

McKinsey & Company

Regulatory compliance

## Organizations are addressing more gen-AI-related risks

Many organizations are ramping up their efforts to mitigate gen-AI-related risks. Respondents are more likely than in early 2024 to say their organizations are actively managing risks related to inaccuracy, cybersecurity, and intellectual property infringement (Exhibit 3)—three of the gen-AI-related risks that respondents most commonly say have caused negative consequences for their organizations. $^{2}$

## Exhibit 3

Respondents report increasing mitigation of inaccuracy, intellectual property infringement, and privacy risks related to use of gen AI.

Gen-AI-related risks that organizations are working to mitigate, $^{1}$ % of respondents

Intellectual property infringement

![](images/f3a350bbd3a00791546458bc1dfc481b2a146fd2ce5f20a40396ac2c22449223.jpg)  
$^{1}$ Only asked of respondents whose organizations use AI in at least 1 business function. Respondents who said “don’t know/not applicable” are not shown. Source: McKinsey Global Surveys on the state of AI, 2023–24

## McKinsey & Company

Respondents at larger organizations report mitigating more risks than respondents from other organizations do. They are much more likely than others to say their organizations are managing potential cybersecurity and privacy risks, for example, but they are not any more likely to be addressing risks relating to the accuracy or explainability of AI outputs.

![](images/9e6e7f0f37848f3a71b006b64219571cff63dc0ac57fc7853f5cebcfb63d4eca.jpg)

## McKinsey commentary

## Alex Singla

## Senior partner and global coleader of QuantumBlack, AI by McKinsey

We've learned a lot about generative AI over the past two years. But perhaps the most important lesson is this: It pays to think big. The organizations that are building a genuine and lasting competitive advantage from their AI efforts are the ones that are thinking in terms of wholesale transformative change that stands to alter their business models, cost structures, and revenue streams—rather than proceeding incrementally.

Our experience helping organizations create and deploy gen AI systems also shows that it pays to be ambitious from the outset—pursuing end-to-end solutions to transform entire domains, rather than taking a piecemeal, use-case-by-use-case approach. Beginning with an overarching, enterprise-level transformative vision opens up possibilities down the line. That’s because a clear picture of where you’re going influences the data you capture and the models you build. You’re thinking about things like access control; security; reusability of code at the front end, not as an afterthought; and creating a foundational infrastructure that is well beyond any individual use case or domain. This allows further functionality to be deployed faster and more cheaply than if you go use case by use case—which, in turn, becomes a competitive advantage that others will have a hard time keeping up with.

Transformative thinking also forces the CEO and top team to be aligned—something that use case thinking does not. This is critical because successful transformations require siloed parts of the enterprise to come together in a single orchestrated effort—and that can typically only happen when the CEO and other top leaders are involved.

# Respondents at larger organizations report mitigating more gen-AI-related risks than other respondents do.

# Best practices for adoption and scaling can enable value, and companies are beginning to follow them

Most respondents have yet to see organization-wide, bottom-line impact from gen AI use—and most aren't yet implementing the adoption and scaling practices that we know from earlier research help create value when deploying new technologies. In a complementary survey in a set of developed markets, only 1 percent of company executives describe their gen AI rollouts as “mature.” Even though these remain early days for deployment, we are beginning to see the impact when these practices are employed to capture value.

We asked respondents about 12 adoption- and scaling-related practices for gen AI and found that there are positive correlations on EBIT impact from each. The one with the most impact on the bottom line is tracking well-defined KPIs for gen AI solutions, while at larger organizations, establishing a clearly defined road map to drive adoption of gen AI also has one of the biggest impacts.

Overall, companies are in the early stages of putting these practices in place. So far, less than one-third of respondents report that their organizations are following most of the 12 adoption and scaling practices, with less than one in five saying their organizations are tracking KPIs for gen AI solutions. Respondents working for larger organizations are more likely to report using at least some of these practices (Exhibit 4). Those at larger organizations, for example, are more than twice as likely as their small-company peers to say their organizations have established clearly defined road maps to drive adoption of gen AI solutions (such as through phased rollouts across teams and business units) and to have established a dedicated team (such as a project management or transformation office) to drive gen AI adoption. Responses show larger organizations are also ahead on building awareness and momentum through internal communications about the value created by gen AI solutions, creating role-based capability training courses to make sure employees at each level know how to use gen AI capabilities appropriately, and having comprehensive approaches to foster trust among customers in their use of gen AI.

## Exhibit 4

# Larger organizations are following more adoption and scaling best practices for gen AI deployment than are smaller organizations.

Organizations engaging in given gen AI practices, $^{1}$ % of respondents

Organizations with \$500 million or more in annual revenue

Smaller organizations

![](images/55de85cee80560e9f3e987bf4aea11db687e9e1e899094d4957b4e346587d684.jpg)  
$^{1}$ Only asked of respondents whose organizations use AI in at least 1 business function. Figures were calculated after removing the share who said “don’t know.” Respondents who said “None of the above” are not shown.
Source: McKinsey Global Survey on the state of AI, 1,491 participants at all levels of the organization, July 16–31, 2024

McKinsey & Company

![](images/ac49ce059ff8b22a36a5e95d2d379befae4f926fbaa290925a59f23bbda972c5.jpg)

## McKinsey commentary Bryce Hall Associate partner

The initial wave of excitement and novelty around generative AI is evolving into an intentional focus on how to create value from these technologies. Executives are rightfully looking for a return on their AI investments; in many cases, they are paring back their strategies from trying to apply gen AI everywhere to prioritizing the domains that have the greatest potential.

We're now far enough into the gen AI era to see patterns among companies that are capturing value. One significant difference is that these companies focus as much on driving adoption and scaling as they do on the up-front technology development. This is not just hand-waving. Instead, they are following specific management practices that enable them to be successful—such as developing a clear road map for scaling, establishing and tracking KPIs, and driving change management by ensuring senior leaders are actively engaged in driving gen AI adoption. The fact that so many companies continue to struggle with these management practices is a testament to the fact that they're not so simple to get right.

In addition, companies that report capturing value from gen AI are “rewiring” their business processes to effectively embed gen AI solutions while appropriately incorporating human-in-the-loop mechanisms to validate models and outputs and effectively mitigating risks associated with the technology.

# AI is shifting the skills that organizations need

This survey also examines the state of AI-related hiring and other ways AI affects the workforce. Respondents working for organizations that use AI are about as likely as they were in the early 2024 survey to say their organizations hired individuals for AI-related roles in the past 12 months. The only roles that differ this year are data-visualization and design specialists, which respondents are significantly less likely than in the previous survey to report hiring. The findings also indicate several new risk-related roles that are becoming part of organizations' AI deployment processes. Thirteen percent of respondents say their organizations have hired AI compliance specialists, and 6 percent report hiring AI ethics specialists. Respondents at larger companies are more likely than their peers at smaller organizations to report hiring a broad range of AI-related roles, with the largest gaps seen in hiring AI data scientists, machine learning engineers, and data engineers.

# Half of respondents whose organizations use A

[中间内容因长度限制已省略]

 AI use cases have increased revenue within the business units deploying them (Exhibit 12). Respondents report similar revenue increases from gen AI as they did from analytical AI activities in the previous survey. This emphasizes the need for companies to have a comprehensive approach across both AI and gen AI solutions to capture the full potential value.

Exhibit 12

Organizations increasingly see gen AI's effects on revenues in the business units using the technology.

Revenue increase within business units from gen AI use, past 12 months, by function, $^{1}$ % of respondents

![](images/7f306628f618821b0380eaa77cbc51e80b9b1d530992e5754259d900ee557f08.jpg)

![](images/0b787661a93e6edb187bf4ec907f398c776bcedf896acd0c83e14b2d4375b201.jpg)

$^{1}$ Questions were asked only of respondents who said their organizations regularly use gen AI in a given function. Respondents who said “no change,” “decreased revenue,” “don’t know,” and “not applicable,” as well as business functions that are cost centers, are not shown. Segments may not sum to the total shown, because of rounding. The first 2024 survey was in the field from Feb 22 to Mar 5, and the second was fielded from July 16 to July 31.
Source: McKinsey Global Surveys on the state of AI, 2024

McKinsey & Company

Overall, respondents are also more likely than in the previous survey to say they are seeing meaningful cost reductions within the business units using gen AI (Exhibit 13). In early 2024, among respondents reporting use of gen AI in specific business functions, a minority saw cost reductions from its use. $^{6}$ The latest survey finds that, for use of gen AI in most business functions, a majority of respondents report cost reductions. Yet gen AI's reported effects on bottom-line impact are not yet material at the enterprise-wide level. More than 80 percent of respondents say their organizations aren't seeing a tangible impact on enterprise-level EBIT from their use of gen AI. $^{7}$

Respondents increasingly report cost reductions from gen AI within business units using the technology.

Cost decrease within business units from gen AI use, past 12 months, by function, $^{1}$ % of respondents

![](images/097d9c5bb4a5385a401fd811eeb44e5dfdf331799f76a0fc1c4aed536ed4978e.jpg)

![](images/e88c221b833ea3052210232b70902cccbfc88890c835427369c0cb8e724bc607.jpg)

![](images/2282a0efe54065ad7cb2e00d30f563c8d1e3411a0a6171467d64024c9de1ed6a.jpg)

## McKinsey commentary Michael Chui Senior fellow

Things are moving fast in the field of AI. But even as we try to keep up with the pace of technological advancements, we are also learning that AI only makes an impact in the real world when enterprises adapt to the new capabilities that these technologies enable. That's what we are hearing in our individual conversations with business leaders—and it is also reflected in the global data we have collected in our latest survey.

Since our previous state of AI survey, the use of AI has continued to increase. More companies are using AI in a growing number of business functions. They are using gen AI to reinvent aspects of their enterprises: marketing and sales, product and service development, service operations, corporate IT, and software engineering. More of our survey respondents are reporting top-line and cost benefits from deploying gen AI solutions. And more respondents say they are using gen AI in their daily lives. Interestingly, it's C-level executives who are leading in their own use, but their employees could be much more ready to use gen AI at work than their C-suite leaders expect.

Organizations have been experimenting with gen AI tools. Use continues to surge, but from a value capture standpoint, these are still early days—few are experiencing meaningful bottom-line impacts. Larger companies are doing more organizationally to help realize that value. They invest more heavily in AI talent. They mitigate more gen-AI-related risks. We have seen organizations move since early last year, and the technology also continues to evolve, with a view toward agentic AI as the next frontier for AI innovation. It will be interesting to see what happens when more companies begin to follow the road map for successful gen AI implementation in 2025 and beyond.

Alex Singla and Alexander Sukharevsky are the global coleaders of QuantumBlack, AI by McKinsey, and senior partners in McKinsey's Chicago and London offices, respectively; Lareina Yee is a director of the McKinsey Global Institute and a senior partner in the Bay Area office, where Michael Chui is a senior fellow; and Bryce Hall is an associate partner in the Washington, DC, office.

They wish to thank Erika Byun, Kaitlin Noe, Larry Kanter, Nicole Lindley, Robert Levin, Roger Roberts, and Tara Balakrishnan for their contributions to this work.

This article was edited by Heather Hanselman, a senior editor in McKinsey's Atlanta office.

## About the research

![](images/844aef6a48916ce2d05f1d2df54cc3ce073a8ab099b62b876f94b95dc6ac4ebd.jpg)

The online survey was in the field from July 16 to July 31, 2024, and garnered responses from 1,491 participants in 101 nations representing the full range of regions, industries, company sizes, functional specialties, and tenures. Forty-two percent of respondents say they work for organizations with more than \$500 million in annual revenues. To adjust for differences in response rates, the data are weighted by the contribution of each respondent's nation to global GDP.

March 2025  
Copyright © McKinsey & Company  
Designed by McKinsey Global Publishing

Find more content like this on the McKinsey Insights App

![](images/895f3dad910ac20379134c2354cdacc21a744cd7bca1b24b64f152892163268e.jpg)
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
