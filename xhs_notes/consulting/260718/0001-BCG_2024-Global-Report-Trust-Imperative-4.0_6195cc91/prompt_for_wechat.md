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
# Trust Imperative 4.0

GenAI
The Trust Multiplier
for Government

2024 Global Report

## BCG ×

salesforce

## BCG ×

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

The BCG Center for Digital Government is a global team of 350 experts dedicated to working with governments to deliver impact through digital technologies, data and AI. We bring world-class capabilities in digital strategy and transformation, artificial intelligence and analytics, design and implementation to the public sector.

For more information, visit www.bcg.com

salesforce

Salesforce is the #1 AI CRM, helping companies connect with customers in a whole new way since 1999. Our product portfolio, Einstein 1, brings #1 CRM apps together with trusted AI and data on one integrated platform so companies can grow relationships, productivity, and their bottom line.

In our new era of artificial intelligence, Salesforce is democratizing AI for companies of every size and industry. Our pioneering formula of CRM + AI + Data + Trust helps everyone get their data together and embrace AI safely and securely across every team and employee so they can unlock the promise of AI to transform their business.

Salesforce is proud to be the market leader, but we're even more proud to lead in philanthropy, innovation and culture. Guided by core values of trust, customer success, innovation, equality and sustainability, Salesforce is more than a business — we're a platform for change.

For more information, visit www.salesforce.com

![](images/f934f6a2249cb37c21ee2fb5b03c912da05936fd368b7626dc4490af7d545ed3.jpg)

The citizens' perspective on how responsible adoption of GenAI can improve government service delivery and multiply trust.

## About this report

Welcome to our fourth report in the BCG-Salesforce Trust Imperative Series. Since 2020, we have been collaborating to explore the nature of the connection and relationship between digital government service delivery and trust in government.

Our research explores the evolution in expectations and experiences with digital government services over the last two years and, given the relevance and importance of the topic, this year we also take a close look at citizens' attitudes towards government use of artificial intelligence (AI), particularly generative artificial intelligence (GenAI).

This report is based on BCG's 2024 Digital Government Citizen Survey (DGCS). BCG conducts the DGCS every two years and it is the most comprehensive and longest-running ‘voice of the citizen’ survey on digital government in the world. In 2024, we collected data that captures the perspectives of 41,600 regular internet users across 48 jurisdictions globally; a sample that represents viewpoints of 73 percent of the total global population and 88 percent of the population in Organization for Economic Co-Operation and Development (OECD) countries.

The DGCS is conducted as an online survey and uses a random sampling approach to collect input from respondents who use the internet regularly, capturing responses using an online survey tool. The survey reflects respondents' views provided at a point in time and is not a ranking or league table to compare jurisdictions. The results reflect the views of citizens which are evidently shaped by the unique local context of each jurisdiction and encompass the many factors that shape perceptions of government digital services.

The sampling methodology provides insights that are intended to be statistically representative of the general population by filtering respondents to balance demographic attributes (e.g. location and gender). Sample sizes yielded a confidence level of 95 percent with a margin of error less than 5 percent across all jurisdictions sampled, assuming a sample proportion of 0.5. In some jurisdictions, sample sizes are larger to enable further more detailed and separate sub-national analysis. This report presents an analysis of the global results and individual jurisdictions. Global averages reflect simple averages across jurisdictions, not weighted averages by population size. Detailed information on sample sizes across jurisdictions and respondent demographics is included in Appendix A.

Exhibit 1: We surveyed 41,600 regular internet users across 48 jurisdictions  
![](images/30ce54b6142dd61a980d884958975f81709b98afa6876931273a60a4277cd09f.jpg)  
Source: 2024 BCG Digital Government Citizen Survey  
$^{1}$ Special Administration Region of the People's Republic of China

In conducting this research, we also held interviews and gathered qualitative input from 20+ global experts in digital government and service delivery from BCG, Salesforce, and externally.

This report is divided into 4 sections:

\- Section 1: Service Improvement Opportunities reveals insights on citizen expectations of digital government services, their experiences using these services and level of satisfaction.

\- Section 2: The GenAI Imperative explores the potential opportunity of GenAI in government and examines the role it can play in improving citizen experience and building trust.

\- Section 3: Citizens’ Perspectives on GenAI in Government looks at citizens’ attitudes towards the use of AI and GenAI in government, the perceived benefits and risks, trust in government to use AI responsibly, and factors that might build or erode this trust.

\- Section 4: The GenAI Roadmap for Government describes how government can establish the necessary prerequisites for trust and deliver better, more innovative digital government services using GenAI.

![](images/4ce32fb4d684c00667c6762cd4a94f239c427332c5caf2c4f960a7bd49ff8134.jpg)

## What is AI?

AI refers to the use of computer systems to perform tasks that have traditionally been associated with requiring human intelligence, such as learning, reasoning, problem-solving, and language.

## What is GenAI?

GenAI is a type of AI that uses foundational, multi-modal models. It can generate new content, including text, images, and audio/video, and support interaction using natural language prompts.

## Executive Summary

In 2024, BCG and Salesforce surveyed 41,600 regular internet users across 48 jurisdictions globally, and sought input from 20+ global experts to understand global digital government service delivery trends. The survey was conducted as part of the 2024 BCG Digital Government Citizen Survey (DGCS). This report presents the survey results and citizens' perspectives on how responsible adoption of GenAI can improve government service delivery and multiply trust.

## Digital government is improving in many jurisdictions

Despite a modest global average increase of 2 percentage points in net citizen satisfaction with digital government services over the last 2 years, there has been a noticeable upward trend and improvement in satisfaction in multiple jurisdictions. Satisfaction with online government services increased in 15 jurisdictions, remained steady in 19 and only decreased in 4.

## The bar for citizen expectations is set high

Citizens' expectations about the quality of digital government services are high, with 75 percent of respondents indicating they expect the quality of services to be similar to those provided by the world's best private sector organizations or global digital and technology leaders. Although the perception that digital government services are as good or better than a typical private sector interaction is positive in most jurisdictions, user experience issues remain common with 74 percent of respondents encountering issues in the past 2 years. There is clearly an opportunity for government to achieve a leap in service satisfaction by getting the basics right.

## GenAI could become a force multiplier for increased trust in government

Previous editions of the Trust Imperative series provided clear evidence of a direct and symmetrical relationship between customer experience of digital government services and citizens' trust in government. Specifically, in our 2020 survey, 87 percent of respondents said that positive customer experiences increased their trust and confidence in government, and 81 percent said that poor experiences eroded trust. GenAI represents a significant opportunity to increase trust in government by improving user experiences by making government services more accessible, personalized, and seamless, if deployed well and with responsible AI safeguards.

## Citizens have genuine concerns about GenAI, but are supportive for some use cases

On average just over half (51 percent) of respondents globally believe that AI is developing too quickly. The top 2 concerns about the use of AI and GenAI are the potential loss of jobs and impact to the economy (34 percent), and the accuracy of results and analysis (26 percent).

![](images/e8fc8ea4adb057f1f7f995addfe5bd8d77ecf52cc329d8d3dbe0a5a3a92c9a95.jpg)

Despite these concerns, citizens are remarkably open to government using GenAI across a range of use cases. Sixty-three percent of respondents are comfortable interacting with GenAI to access simple government services. Seventy-one percent are comfortable with government using GenAI to communicate in multiple languages, 69 percent are comfortable with government employees using GenAI support tools, and 67 percent are comfortable with government using GenAI to streamline administrative tasks.

However, there is a wider spread in comfort levels for some use cases across jurisdictions, such as using GenAI to automate service access decisions and using GenAI to monitor public sentiment.

There is an opportunity for government to unlock the benefits of GenAI for use cases where there is already strong support and acceptance. It also highlights the importance of government taking a considered approach to use case selection, tailoring AI strategies and roadmaps to the unique contexts of each jurisdiction, and aligning with public sentiment on the social license for the use of GenAI.

## Establishing guardrails and building AI literacy are key to building trust

On average, approximately 3 in 5 respondents say they trust government to use AI responsibly, but this level of trust varies significantly across jurisdictions. The top 2 factors that would most increase trust in government use of AI remained fairly consistent globally. These were: 1) specific laws and regulations on how AI can be used by government (38 percent); and 2) rules to safeguard personal information (34 percent). Increasing overall AI knowledge and expertise will also be important to build trust because people with the most knowledge of AI are twice as likely as those with a basic knowledge to say the benefits outweigh the risks, and five times more likely than those with no knowledge of AI.

## The GenAI roadmap for government

In this report, we describe 3 key actions for government to improve service quality, and multiply trust with GenAI:

1. Get started now: Learn by doing, starting with low risk/low harm use cases, to build the internal capabilities to innovate and scale and invest in building the necessary skills, critical data and technology platforms.

2. Establish the prerequisites for trust: Adopt responsible AI governance, promote a responsible AI culture, commit to accountability and transparency, and design to bring the best of human and AI to deliver maximum impact for citizens.

3. Lead in AI innovation: Foster innovation by building workforce and population AI skills and expertise, and catalyze innovation through holistic AI strategies for a thriving knowledge economy.

![](images/ae9230f65d6323351b4e4415d366b5773df85f14b8eae4c7659d6ae2011f7883.jpg)

# Section 1: Service Improvement Opportunities

## Satisfaction is improving or steady in most jurisdictions

Overall, net satisfaction with digital government services globally was 65 percent in 2024. This figure ranged from 26 to 83 percent across jurisdictions, as illustrated in Exhibit 2. Average net satisfaction remained relatively stable in the last two years, increasing only 2 percentage points (from 63 percent) across jurisdictions where longitudinal data is available (38 jurisdictions).

Despite a modest global average increase, there has been a noticeable improvement in satisfaction in multiple jurisdictions. Exhibit 2 shows that satisfaction with online government services has increased in 15 jurisdictions, remained steady in 19 and only decreased in 4.

Some jurisdictions saw significant improvements such as Thailand, Sweden, Brazil, and the Netherlands where net satisfaction has improved 10 percentage points or more.

Exhibit 2: Net satisfaction with digital government services increased or was steady in most jurisdictions  
![](images/85545a60a263ee1e6b7ea9cca9cc28acbed34d4fe692eccda6d3699d3c253e91.jpg)  
Q. How satisfied or not are you with the use of the internet in delivering each of the following government services? Response options: 1. Extremely Dissatisfied, 2. Dissatisfied, 3. Rather dissatisfied, 4. Neither satisfied or not, 5. Rather satisfied, 6. Satisfied, 7. Extremely satisfied, 8. I don't know. Net satisfaction = total satisfied – total dissatisfied.
Source: 2022 and 2024 BCG Digital Government Citizen Survey

![](images/ad7bfacfc6f5fec798da03821f1a861ccb14c8d0ebf3578bfd2adbb785e7492e.jpg)

Exhibit 3: Global net satisfaction with digital government services  
![](images/143ea39aa2696ed7f2fc682698dc50ca28fd70d243fb3f06a67ccc0277a7619a.jpg)  
Q. How satisfied or not are you with the use of the internet in delivering each of the following government services?
Net satisfaction % = total satisfied (extremely satisfied + satisfied + rather satisfied) less total dissatisfied (extremely dissatisfied + dissatisfied + rather dissatisfied). Note: Responses for 'Neither satisfied or not' are not shown.
Source: 2024 BCG Digital Government Citizen Survey

\- Similar to global digital leaders; such as Apple, Google, Uber, Spotify, Amazon, Alibaba, Tencent, JD.com, Baidu, Jumia
- Similar to best private sector institutions; such as banks, airlines, telcos, retailers, etc.
- Similar to the best online government services in the world
- My expectation is lower than any of the above

## The bar for citizen expectations is set high

Citizens’ expectations regarding the quality of digital government services are high with 75 percent of respondents indicating they expect the quality of digital government services to be similar to those provided by the world’s best private sector organizations or global digital and technology leaders. A further 19 percent expect their government digital services to be similar to the world’s best online government services (see Exhibit 4).

In our survey, respondents are also asked to compare their most recent digital government experience with a typical or average private sector interaction. On average 84 percent of global respondents say it was the same or better (36 percent the same, 48 percent better) but this varies across jurisdictions.

The challenge for government is to continue meeting the high service expectations of citizens when the benchmark for service quality, set by world leaders, is continuously being raised through accelerating technology developments such as GenAI and innovation in highly competitive global markets.

Exhibit 4: 75 percent of respondents expect the quality of digital government services to match the best private sector organizations or global digital leaders

![](images/0c85571625161adb826a15ac3f0d56ed173ec96e430c8ddd42689b23438261fe.jpg)  
Q. In your opinion, to what quality standard do you think online government services should be delivered, in terms of speed, convenience, ease of access, personalization, etc.? Source: 2024 BCG Digital Government Citizen Survey

![](images/cfd3104ab7399f8c04e42257e92eefa7612f6422cf8807b24d6f33d550443b13.jpg)

![](images/6ca8b5d29f86515decf6a1de04f1117c30ed2d462308a99654d16c84c33794e1.jpg)

## Chesterfield Borough Council's My Chesterfield Portal

Chesterfield Borough Council is a local authority in Derbyshire in the United Kingdom. It is home to around 105,000 residents and provides more than 50 council services to serve and support local communities. The My Chesterfield Portal provides an example of how a government organization is leveraging technology to deliver new products and services that meet citizen needs and expectations, and high quality experiences on par with private sector leaders.

The Chesterfield Borough Council's Right First-Time Contact Center System went live in 1 year and since then the team has seen over 15,000 registrations in the My Chesterfield portal (representing 30 percent of Chesterfield's households). The system helps streamline information and service delivery by enabling citizens to submit service requests online at any time through a single front door. It also supports the delivery of high quality services with a 360-degree-view for staff to review the inquiry, initiate service delivery, tag subject matter experts, assign tasks, and work together to close the case. The Council has seen an average of 1,100 logins to My Chesterfield every week, showing the ongoing traction an online forum has with the community. The team has continued to add new online services (over 50 in just 9 months) and as a result has seen a 6.5 percent reduction in telephone calls, a 42 percent reduction in online complaints, and a saving of an average 3 hours a day on reception activities.

Through the portal, citizens have visibility of their billing documents, benefit payments, direct debit details, and council tax balances all through My Chesterfield. The Council has also added the ability for residents to apply for grants to the My Chesterfield portal. The grants function was up and running in about 10 days and has collected roughly 95 percent of all grant app

[中间内容因长度限制已省略]

ch, analysis, writing, design and production.

We want to also thank Casey Coleman, Paul Tatum, Kevin Paschuck, Ashlee Marcuccio, Paula Goldman, Gayan Benedict, and Polly Sumner from Salesforce and Gareth Dando, Steve Mills, Frank Felden, Richard Sargeant, Kirsten Rulf, Rami Mourtada, Simon Shenton, Saibal Chakraborty, Adam Jura, Heidi Kim, Masahiro Nakagawa, and Atsushige Kimoto from BCG for providing expert advice and input.

This report was jointly funded and prepared by BCG and Salesforce.

## Appendix A

Respondents by jurisdiction (n=41,600)

<table><tr><td>Jurisdiction</td><td>No. of respondents</td></tr><tr><td>Argentina</td><td>500</td></tr><tr><td>Australia</td><td>4,323</td></tr><tr><td>Austria</td><td>501</td></tr><tr><td>Bangladesh</td><td>501</td></tr><tr><td>Brazil</td><td>502</td></tr><tr><td>Cambodia</td><td>502</td></tr><tr><td>Canada</td><td>503</td></tr><tr><td>Chile</td><td>505</td></tr><tr><td>China</td><td>509</td></tr><tr><td>Denmark</td><td>500</td></tr><tr><td>Egypt</td><td>517</td></tr><tr><td>Estonia</td><td>500</td></tr><tr><td>France</td><td>515</td></tr><tr><td>Germany</td><td>2,000</td></tr><tr><td>Greece</td><td>509</td></tr><tr><td>Hong Kong, China</td><td>505</td></tr></table>

<table><tr><td colspan="2">Jurisdiction</td><td>No. of respondents</td></tr><tr><td></td><td>India</td><td>2,002</td></tr><tr><td></td><td>Indonesia</td><td>506</td></tr><tr><td></td><td>Italy</td><td>513</td></tr><tr><td></td><td>Japan</td><td>519</td></tr><tr><td></td><td>Kazakhstan</td><td>500</td></tr><tr><td></td><td>Kenya</td><td>511</td></tr><tr><td></td><td>Kuwait</td><td>517</td></tr><tr><td></td><td>Malaysia</td><td>509</td></tr><tr><td></td><td>Mexico</td><td>505</td></tr><tr><td></td><td>Morocco</td><td>502</td></tr><tr><td></td><td>Netherlands</td><td>505</td></tr><tr><td></td><td>New Zealand</td><td>501</td></tr><tr><td></td><td>Nigeria</td><td>523</td></tr><tr><td></td><td>Norway</td><td>500</td></tr><tr><td></td><td>Philippines</td><td>500</td></tr><tr><td></td><td>Qatar</td><td>503</td></tr></table>

<table><tr><td>Jurisdiction</td><td>No. of respondents</td></tr><tr><td>Russia</td><td>503</td></tr><tr><td>Saudi Arabia</td><td>500</td></tr><tr><td>Singapore</td><td>500</td></tr><tr><td>South Africa</td><td>500</td></tr><tr><td>South Korea</td><td>501</td></tr><tr><td>Spain</td><td>516</td></tr><tr><td>Sri Lanka</td><td>503</td></tr><tr><td>Sweden</td><td>500</td></tr><tr><td>Switzerland</td><td>500</td></tr><tr><td>Thailand</td><td>500</td></tr><tr><td>Turkey</td><td>500</td></tr><tr><td>Ukraine</td><td>500</td></tr><tr><td>United Arab Emirates</td><td>505</td></tr><tr><td>United Kingdom</td><td>2,001</td></tr><tr><td>United States of America</td><td> $9,563^1$ </td></tr><tr><td>Vietnam</td><td>500</td></tr></table>

1. This survey includes 9,563 total respondents from the United States of America (USA). USA national representation data includes 2,006 respondents, and additional 7,557 respondents provide representation across 15 states. Global averages presented in this report are calculated as simple averages, and are not weighted to population. Source: 2024 BCG Digital Government Citizen Survey

## Global survey respondent demographics

![](images/8afb5f5912ef6624c6d9bd3abbc5f5c681a84814008eb682af6dc6c068ba1202.jpg)

![](images/7f23400a76dc1e1a42dfbd4588fe125a93ee2eb3e5cc57ed77723e176f714054.jpg)

![](images/f54aab61edf3949799adbb41378a76d66886c07641d7fbdbecd99901e76eba2b.jpg)

![](images/c2fa5637d8fb5426ff616c7da66c3cc180cfe963e87acd9cf8a9940316c677fb.jpg)  
Q. How old are you? Q. Which of the following best describes your current work status? Q. Which of the following best describes where you live? Q. Are you... 1. Male, 2. Female, 3. Other. Note: 1. Rounding to nearest whole numbers, totals may not add to $100\%$ . Source: 2024 BCG Digital Government Citizen Survey

27 online government services rated for usage and satisfaction  
![](images/8362a8855e7973a53008ab85f5b85f7b92635c8add0898c10efafee4a54ca48e.jpg)  
Source: 2024 BCG Digital Government Citizen Survey

## Disclaimer

The purpose of this report is to provide general and preliminary information, and its contents should not be relied upon or construed as advice or similar. The contents of this report are disclosed in good faith, and subject to change without notice. The report contains BCG and Salesforce trademarks, confidential and proprietary information, and BCG and Salesforce retain all right, title and interest to its contents. The report does not contain a complete analysis of every material fact on the subject matter, and all warranties, representations and guarantees pertaining to the reliability, timelines, suitability, accuracy or completeness of its contents are expressly disclaimed. BCG and Salesforce, and their subsidiaries and affiliates, disclaim all liability relating to or arising from access, use or reliance on this report, including but not limited to direct, indirect, incidental, special or consequential losses arising from the information in this report, howsoever arising, including third party claims.

## Artificial Intelligence Disclosure Statement

This report includes images and content generated with the assistance of artificial intelligence (AI) technology and tools. However, the final outputs, concepts and insights are based on human expertise, judgment, input, interpretation and decision-making. For further inquiries regarding the AI technologies employed in this report or for additional details on the methodology, please contact us.

© Boston Consulting Group, Inc. 2024. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com.

## BCG ×

salesforce
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
