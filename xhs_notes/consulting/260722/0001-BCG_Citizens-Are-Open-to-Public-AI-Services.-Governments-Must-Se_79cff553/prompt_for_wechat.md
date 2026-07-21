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
2026 DIGITAL GOVERNMENT CITIZEN SURVEY REPORT

# Citizens Are Open to Public AI Services. Governments Must Seize the Opportunity.

July 2026

By Miguel Carrasco, Dr. Lars Littig, Heidi Kim, Rami Mourtada, and Joseph Hsiao

## Table of Contents

03 Introduction
07 Fertile Ground to Build On
09 Getting the Next Decade Right
14 Standing Still Is Not an Option
15 Citizens’ Concerns and Call to Action

![](images/15f759b66afb8a6e1195ca3bd2ae2e83dd439a5e070ef3a73a0758e54b5ad42b.jpg)

## Introduction

Since 2012, BCG has conducted a biennial global survey of citizens' attitudes toward digital service delivery by governments. (See the sidebar “About This Report.”) The results of the 2026 Digital Government Citizen Survey present governments with both an opportunity and a challenge. The digital transformation in government services over the past decade has been profound, resulting in improved adoption, usage, and reliability. During that time, adoption has risen 15 percentage points as citizens have engaged with their governments in new ways online, with approximately 45% of them—including 42% in countries surveyed in both 2016 and 2026—now using those services weekly. (See Exhibit 1.) Advances in private sector offerings have continued to lift expectations, and more citizens are pegging their expectations for their government’s digital offerings to the quality of private sector services they use.

## Citizens Want Governments to Take the Next Leap

As governments have proactively invested in more expansive, more personalized digital offerings and as citizens have come to depend on those services, citizens' satisfaction with them has waned, falling 13 percentage points since 2016. As these offerings grow more sophisticated, they also become more intricate, with more moving parts that can break down. Consequently, despite the services' central role in people's daily lives, citizens are expressing greater dissatisfaction with usability problems that make the products more difficult to navigate and operate. The proportion of citizens who reported problem-free use of these government tools dropped 5 percentage points over the decade, contributing to an overall decline in citizens' satisfaction with the digital services that their governments provide.

![](images/19f5b04dac2a0c0721a03797d575fc02426aa3af7f6562090fbf9881ff235725.jpg)

## About This Report

BCG conducts its Digital Government Citizen Survey (DGCS) every two years. Since the inaugural edition in 2012, the survey has grown into a preeminent resource for identifying citizens' opinions and beliefs about government digital service delivery. The 2026 survey is the most expansive one yet, representing citizens' viewpoints from 88% of OECD countries, accounting for 70% of the world's population.

The DGCS is an online survey that uses random sampling to collect input from respondents who self-identify as regular internet users. The data reflects respondents' views on government digital services at a specific point in time. The local context in which citizens and government operate shapes these views. The sampling methodology filters respondents to balance demographic attributes such as location and gender. This approach allows the results to be statistically representative of the general population with a margin of error of $\pm 5\%$ .

# A Decade of Digital Progress Has Lifted Usage, Adoption, and Service Quality, but Satisfaction Has Not Kept Pace

Service usage

Respondents who use e-services weekly or more frequently (%)

Service adoption $^{1}$

Average respondents who use surveyed government e-services (%)

Government vs. private sector

No problem

Net respondents who rate government e-services as better than private sector e-services (%)

Respondents who report no issue when using an online government service (%)

Net satisfaction

Net respondents who are satisfied with online government services (%)

![](images/a3f7c1434fd899e27d069b642161ca3d0471f95e79c32f519f5c691cc821042d.jpg)

![](images/fb6b8ed35b234d624da02e61f32b92dfc08510a243b6322357003ca24b2824e6.jpg)

![](images/6b8560398d0a93fb59caed77072e9823392d3d921d8dc3b2a3d88eed722688e1.jpg)

![](images/de7dcb9a003965245f013cfdda109b16ef619fd9447bfa4f4e8c139db0202cc0.jpg)  
Sources: 2016 and 2026 BCG Digital Government Citizen Surveys.  
Note: Percentage changes shown in the green ovals compare survey results for 2016 and 2026 for the matched set of countries surveyed in both years. pp = percentage points.  
$^{1}$ Service adoption reflects online usage rate based on the 30 services surveyed.

The emergence and subsequent expansion of AI represents an inflection point in digital transformation that can accelerate the full realization of this new era of possibility, elevating government services, improving their delivery, and reviving citizen enthusiasm. But as AI transitions from broad abstraction to visible direct impact—more negative than positive for some—public sentiment is likely to harden further overall. Public backlash to AI infrastructure (for example, data centers) and its effect on the cost of living has rapidly changed the context that governments operate within, reinforcing the need to ground government AI strategy in citizen sentiment.

At the same time, however, the continued expansion of AI in tools and services that touch every aspect of daily life will further raise citizens' public sector expectations, potentially widening the gap between citizens' expectation and governments' service delivery. Fortunately, AI also offers governments the opportunity to reimagine their digital offerings to meet those rapidly rising expectations. Our 2026 survey makes clear that people's receptiveness to AI and their expectations of public digital services have evolved in a way that should spur governments to fully actualize their AI strategies without delay. This conducive environment reflects a targeted emphasis, previously seen in the 2024 survey, on building citizen confidence in AI through increased exposure and proficiency, as well as on implementing guardrails to guide governments in the safe deployment and use of AI.

Today, citizens are increasingly ready to take the next step in the AI era. In fact, this year's survey shows a correlation between lower citizen satisfaction in digital government services and a sense that government is moving too slowly in adopting AI to transform its services—a correlation not present when citizens feel that government is moving too quickly.

For governments, the challenge and the opportunity that AI transformation presents is clear: they must move beyond merely setting a foundation for incorporating AI in digital service delivery. Building the tech foundation, devising governance frameworks, and establishing guardrails are necessary steps in reimagining digital services in the age of AI. But these building blocks are not the finish line. They are the launching pad for what comes next—and today, citizens expect their governments to take that next giant leap. For governments, the mandate to embrace AI to scale up their digital transformation means that standing still is no longer an option.

## Citizens' Relationship Beliefs About AI Are Evolving

Citizens' views of AI are not uniform across all regions. (See the sidebar “Attitudes About AI Depend on Where You Are.”) But some broader trends transcend regional differences. In the most recent survey, the proportion of regular AI users rose sharply—by 26 percentage points—with nearly two-thirds (64%) of citizens reporting that they use AI tools at least once a week. (See Exhibit 2.) The survey also showed a 4-percentage-point decrease in “don’t know” responses about AI’s potential risks and rewards. The crystallizing of citizens’ opinions about AI appears to be a natural effect of meaningful exposure to the technology. The observed decline in “don’t know” responses thus signals broadening exposure across the population. Accompanying this spike in familiarity is a growing receptiveness to AI that could enable governments to deepen their integration of AI into their digital offerings. Overall attitudes have become more positive over the past two years, as 70% of citizens now hold a neutral-to-positive view of AI, up 5 percentage points since 2024.

The survey results reveal that individuals are increasing their active use of AI and that the increased exposure is affecting how they feel about the technology. No matter where governments are in their digital service transformation, they have an opportunity to take bold steps thanks to evidence that citizens' attitudes are open, evolving, and growing more receptive to the idea that government deployment of AI could improve and transform digital services that they rely on. At the same time, the variability of these attitudes should encourage governments to act. Later, through exposure and time, those opinions about AI may become far less malleable, potentially reducing the inclination to support government exploration.

## EXHIBIT 2

Citizens’ AI Proficiency Is Growing Fast, with Experts Almost Seven Times as Positive About AI’s Benefits as Those with No AI Experience

Respondents' self-assessed level of AI knowledge (%)

Respondents who view the benefits of using AI in government as outweighing the risks (%)

![](images/5881a6d801debbfd3efdc68c8e57d905350f7e263d835913511c720b9e9b7162.jpg)  
Sources: 2024 and 2026 BCG Digital Government Citizen Surveys.  
Note: pp = percentage points.

$^{1}$ As used in this exhibit, “proficient” encompasses “intermediate,” “advanced,” and “expert.”

Sources: 2024 and 2026 BCG Digital Government Citizen Surveys.

## Attitudes About AI Depend on Where You Are

Despite exhibiting an overall trajectory of increasing openness to AI, citizens' attitudes about the technology varied significantly by region. (See the exhibit.) In the Americas, public opinion showed a notably positive shift, with a 5-percentage-point increase in respondents who said that AI's benefits outweigh its risks. These gains came in part at the expense of “don’t know” responses in the 2024 survey and in part from a decline in the percentage of responses asserting that the risks presented by AI are greater than the potential rewards.

In the US, the overall perception that the benefits of AI outweigh the risks has risen, but these findings are tempered by concerns within specific demographics, such as an apparent drop in optimism among younger citizens about the influence of AI. For example, in spring 2026, graduating students at US colleges such as Stanford University and the University of Central Florida repeatedly booed tech executive speakers who praised AI, reflecting growing anxiety about AI's impact on the entry-level job market. Protests against the construction and impact of data centers are growing, too. These objections

underscore the importance of demographics: the opinion of younger citizens and college graduates entering the workforce has changed quickly, even as overall sentiment has trended toward greater AI acceptance. Factoring in short-term divergence will be key to governments' thinking, as will acknowledging that citizens' AI sentiment may differ by age or other demographic variable.

In the Middle East and Africa, the survey found that positive sentiment has dampened, with a decrease of 9 percentage points over the past two years among those who said that they viewed AI as a net positive. Most of this dip in support for AI consisted of a shifted from a positive position on the impact of AI to a neutral one. A smaller proportion of respondents moved went further, seeing the risks of the technology as outweighing the rewards. Even so, respondents in the Middle East and Africa continue to express the greatest comfort with AI of any regional population. In Asia Pacific and Europe, attitudes about AI were largely unchanged from 2024.

## Regional Attitudes Toward AI Are Converging, with the Americas Growing More Positive and the Middle East and Africa More Cautious

Respondents who view the benefits of AI as exceeding the risks, by region (%)

![](images/a3e0486e96b4aad871c7aa3d1cbf5246dd017b3724eed5146fd83da72100ce7d.jpg)

Notes: We assigned the 44 countries included in this survey to the following regions: Americas: (Argentina, Brazil, Canada, Chile, Mexico, US); Asia-Pacific (Australia, Bangladesh, China, India, Indonesia, Japan, Kazakhstan, Malaysia, New Zealand, Philippines, Singapore, South Korea, Sri Lanka, Thailand, Vietnam); Europe (Austria, Denmark, Estonia, France, Germany, Greece, Italy, Netherlands, Norway, Spain, Sweden, Switzerland, Turkey, UK); Middle East and Africa (Egypt, Kenya, Kuwait, Morocco, Nigeria, Qatar, Saudi Arabia, South Africa, UAE). pp = percentage points.

![](images/6176003e5c72861c049875c5068b66a6c6e0d12650d14811ed423586f3af6204.jpg)

# Fertile Ground to Build On

The 2026 survey data shows a 10-percentage-point rise in the proportion of proficient AI users over the past two years. Today, 64% of citizens identify themselves as intermediate, advanced, or expert users of AI. This expanded number of proficient users is an important strategic input for governments, as the data indicates that expert users are almost seven times as likely to have a positive view of AI as those who have no experience with the technology. The growth in highly proficient users can thus be a key enabler for governments strategizing about adding AI use cases across their digital services.

## Citizens' Comfort with Agentic AI Is Growing

With the public release of ChatGPT in November 2022, followed by Claude and Gemini, access to AI became ubiquitous. People—first English speakers, and then others—began using the natural language tool en masse, in part because chat interfaces such as ChatGPT and Claude Chat spoke their language. Each AI tool that followed in the wake of the original version of AI adopted the same format: they used natural language and typically responded to user prompts by returning outputs. The latest frontier is agentic AI, also known as AI agents, a more sophisticated version of the technology. Advances in AI now allow AI agents not just to come up with answers, but to act autonomously on individuals’ behalf.

As this more autonomous version of AI emerged, industry observers assumed that users would be slow to adopt it, given agentic AI's increasingly immersive and imposing nature. But this has not been the case. In a short amount of time, citizens are demonstrating growing comfort with agentic AI use cases—situations where AI has permission to act directly on an individual's behalf. (See Exhibit 3.) As citizens' exposure to AI has increased, particularly in real-world use cases, they increasingly care more about the benefits that the specific use case provides than about the underlying technology that makes it possible.

In Abu Dhabi, the capital emirate of the UAE, the government's TAMM platform introduced AutoGov, an AI agent that autonomously manages multiple recurring government services. These include renewing licenses, processing utility payments, and scheduling routine health-care appointments, without resident having to initiate each transaction. The technology runs quietly in the background of daily life, notifying the user at each step. TAMM exemplifies how agentic AI can shift a government service from reactive to anticipatory, while residents retain the ability to customize their automation settings and override at any point.

# Citizens Are Increasingly Comfortable with Deployment of Agentic AI in Citizen-Facing Use Cases, but Less So for Internal Operations

Respondents' comfort or discomfort with AI deployment for specific types of tasks (%)

![](images/bfef92dfc5f8944a3002e8d7a902240d857efb45817ca8856a9c7f47f595d6fd.jpg)  
Source: 2026 BCG Digital Government Citizen Survey.  
Note: Three of the top four use cases involve agentic AI. Percentages in the “comfortable” column combine survey responses of “very comfortable” and “somewhat comfortable”; percentages in the “uncomfortable” column combine survey responses of “somewhat uncomfortable” and “very uncomfortable.” Bars do not sum to 100% because “I don’t know” responses are excluded.

The dawn of agentic AI also enabled programs like the ALERTCalifornia network, which uses AI to process live feeds from more than 1,200 high-definition cameras to help detect wildfires while they are still small. The cameras, which possess a 360° viewing range, sweep sensitive areas in the state every two minutes, allowing AI to identify spikes in heat or the presence of smoke. AI agents then alert authorities accelerating the dispatch of firefighters by as much as 45 minutes—a huge boost to public safety in fire-prone areas.

The 2026 survey showed that citizens' comfort with AI usage exists on a continuum. respondents were broadly most comfortable with citizen-facing AI use cases, such as 24-7 access to help and information via chatbots (66%). Three of the four most highly rated use cases deploy agentic AI to perform such tasks as providing virtual assistance, detecting fraud, and delivering personalized services. Citizens' receptiveness dipped in assessing AI-supported internal operations, however, although 57% of respondents remained comfortable with scenarios that involved using AI to facilitate administrative tasks. These users

expressed some reservation about government use of AI to generate images or to synthesize social media content for purposes of assessing public sentiment. Their greatest reservations came in response to the use case in which AI was empowered to decide on access to public services.

## A Strong Digital Foundation Informs AI Attitudes

The rapidly evolving opportunities presented by AI arise on a foundation laid by the expansion of digital delivery over the past decade. During that period, citizens learned to transact with their government online, built familiarity with digital channels, and gained confidence in the results. Today, as governments' strategic imperative shifts toward AI adoption and its capacity to further transform digital service delivery, those earlier experiences inform citizens' receptiveness to AI's potential.

![](images/a3e6e0e2e4fa8f4d63747072f79c17dd0d9d4c04ca36d607bebf9bb445910530.jpg)

# Getting the Next Decade Right

Citizens are growing more comfortable with using AI beyond basic functions, as the survey showed that 60% of users at intermediate or higher levels of proficiency were willing to allow AI agents to act on their behalf. (See Exhibit 4.) Among less proficient users, which represent a minority of all users, 36% of respondents shared more advanced users' willingness to empow

[中间内容因长度限制已省略]

n applying blanket oversight or autonomy. This approach positions humans to take on roles that are more valuable to service delivery—interacting with citizens and thereby boosting performance and satisfaction.

\- Build AI proficiency. Invest in citizen and workforce AI literacy, recognizing that proficiency shifts attitudes and unlocks comfort with deeper AI use. Executing this step requires building internal AI literacy to meet growing external proficiency, upskilling across the board—particularly to work with service delivery agents—and elevating customer experience.

\- Tailor the delivery to regional concerns. Meet the reality on the ground by sequencing the rollout of service use cases. Calibrate complexity and agentification to match these local concerns and environments, and tailor the narrative to suit specific populations.

\- Elevate trust by making government accountability visible. Prioritize the levers that citizens can see and contest, including appeal with human review, public performance reporting, and independent audits. Citizens favor these over less-visible technical or back-office assurances.

# The High Stakes of Taking the Right Steps at the Right Time

For governments, the 2026 survey shows that now is the moment to look to the future and boldly embrace what AI can do to transform not just the services they provide, but the lives of the citizens they serve. Citizens are giving governments a mandate to do just that, further transforming the digital services that they rely on. As governments embark on this next step, the potential benefits and the risks are great. Simple user errors can lead to spiraling problems, and missteps such as moving too fast and not meeting citizens' expectations can erode public trust and have significant adverse consequences. To ensure citizens' comfort and optimism, governments must act diligently and responsively, taking the right steps at the right time. They must also move decisively, as the survey findings make clear that the current level of positive sentiment may not last. Recognition of that fact makes it even more important for leaders to seize the moment and explore the frontier of agentic AI to expand what's possible for their citizens.

## About the Authors

![](images/1b428d28daf1ae8137e5aa55bff82d5df7c98153215e47942991491ec69f671e.jpg)

Miguel Carrasco is a managing director and senior partner in the Sydney office of Boston Consulting Group. He is the founder of BCG's Center for Digital Government and director of the Center for Public Impact. You may contact him by email at carrasco.miguel@bcg.com.

![](images/46f2ae5fe6054bffceefd26136bce3bf3d0ed088b1e09dfaf495227e61ca6150.jpg)

Heidi Kim is a managing director and partner in BCG X's Manhattan Beach office. Her work focuses on innovation, technology, and bringing world-class customer experiences to government. You may contact her by email at kim.heidi@bcg.com.

![](images/153ad4f9892efdbed3082f5bfe0d255f96534835065e6b224b87e82ced3631ab.jpg)

Joseph Hsiao is a senior manager in BCG's Sydney office and leads the Center for Digital Government's Vantage team. He focuses on developing BCG perspectives and intellectual properties, including BCG's flagship Digital Government Citizen Survey since 2018. You may contact him by email at hsiao.joseph@bcg.com.

![](images/ce69f6fabab1cde74eda4f15651242cde14fc9bf6d9052e938cf2490587aa8a8.jpg)

Dr. Lars Littig is a managing director and senior partner in the firm's Middle East offices. He is the leader of BCG's Center for Digital Government across the Europe, Middle East, South America, and Africa region and of the Technology & Digital Advantage practice in the Middle East. You may contact him by email at littig.lars@bcg.com.

![](images/56c71fb8ac1966c825ddf0b47e005729ea9d39f3dbd452848636a2fd6cb13587.jpg)

Rami Mourtada is a partner and director in the firm's Middle East offices, as a core member of BCG's Technology Advantage and Public Sector practices. He leads BCG's digital transformation topic in the region and is part of BCG's Center for Digital Government. You may contact him by email at mourtada.rami@bcg.com.

## Acknowledgments

The authors would like to express their sincere gratitude to Hassan Abdelkhalek, Khushee Verma, Elliot Hannon, Maureen Ton, Tanya Sharma, Raghav Sharma, Faisal Faraz, Hannah Coatsolonia, Angela Everitt, and members of the BCG design studios and editorial team for their invaluable contributions to this work. Their thoughtful input, expertise, and generous support throughout the development of this report and the interactive dashboard have been greatly appreciated.

## Boston Consulting Group

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

## Center for Digital Government

BCG's Center for Digital Government partners with leaders in government and society to unlock the potential of digital, data, and technologies to transform the public sector and deliver better outcomes for citizens through best-in-class government digital services.

![](images/62483b7280b1c1161300033d7db161d8774a61145d4d26c7d7c4e3ef1ee55776.jpg)
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
