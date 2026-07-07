你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
## 2025 Sustainable and inclusive growth impact report

## Contents

![](images/f9c3a505e72b8cdf97ab8680db6963753ca6cabf91b0de73feb31e6f0f6255c7.jpg)

## Introduction

![](images/06a91abf02e5a274fce0d84ed8c71e1791052b2f63ee6f172ce2070b4304080a.jpg)  
Growing economic
opportunity

![](images/9bd2059747f80aed8c2d980525e8868e91067186a851bc0a55f5091f367c6fbb.jpg)  
Improving health outcomes

![](images/353df18ec9d6b59b94c78a7b6343dd5294cf48f320cd6947e9200a827715a667.jpg)  
Driving environmental
sustainability

![](images/db0e4e2fc40f871fe880f33124cdafe9d46d0d067d52e2c26abf8a3adb249c6b.jpg)  
Unlocking inclusive growth
through technology

3 Message from our global managing partner

4 Our approach to impact

5 A century of helping organizations think bigger, build stronger, and expand opportunity for all

7 Jobs and reskilling

8 Economic mobility and affordable housing

9 Education

11 Public health

12 Brain health

13 Women's health

15 Decarbonization

16 Green business building

18 Digital transformations

19 Artificial intelligence

20 Future of work

# Message from our global managing partner

Optimism can be hard to come by these days. Take the long view, though, and you'll see that we've been here before. A century ago—when our firm was founded—we faced down similar geopolitical, economic, and technological uncertainties to those we do today. But in the 100 years since, we've doubled our lifespans, lifted billions from poverty, and put a man on the moon. Who is to say we can't go further?

We publish this report each year to measure our progress against an aspiration to accelerate sustainable and inclusive growth around the world. But for me, it's also a tribute to the power of choosing optimism. At a time when optimism can feel outdated, I see it not as naïve, but as a conviction to shape what comes next. Inside, you'll find stories of our clients and colleagues who have made that choice and decided—again and again—that they can make the next 100 years better than the last. Below is just a small sampling of what optimism in action looks like.

## Growing economic opportunity

The past century has shown what's possible when growth expands economic opportunity, and we're proud to publish research and work alongside our clients to increase access to quality jobs, strengthen income mobility, and upskill workers. What does that look like in practice? Helping a US-Kenyan biotech create jobs and support local farmers; working with a nonprofit to find mobility gaps and practical solutions; graduating 120,000 learners across 133 countries from our Forward program; and more.

## Improving health outcomes

There are many examples in this report of our efforts here, from the McKinsey Health Institute's work on women's health to expanding access to behavioral healthcare for kids. But one in particular has stayed with me—the story of a young father in Philadelphia whose life was saved thanks in part to our work with leaders in the city and beyond to embed health into trusted settings like grocery stores, schools, and workplaces. I encourage you to watch the video about this work — it's a powerful reminder of the opportunity to improve health outcomes for the people who need it most.

## Driving environmental sustainability

A successful transition must solve the “trilemma” countries face in providing energy that is secure, affordable, and sustainable … doing so will require both creativity and collaboration. Our recent work with Apple—in which we partnered to map circular value chains for materials such as aluminum, copper, and rare earth elements—is a unique example of both. So too is our work on the Climate Transition Impact Framework, which helps countries test climate pathways and socioeconomic outcomes.

## Unlocking inclusive growth through technology

AI and other new technologies give us a generational opportunity to enable small businesses to go digital, help rural educators upskill remotely, and connect job seekers to roles faster. One of my favorite client examples from 2025 was our partnership with Ecuador's largest bank to launch a new digital bank and payments ecosystem, expanding access to financial services for six million people—more than 60 percent of the total addressable market—many of whom were previously underserved or unbanked.

I'm also proud of our upskilling efforts, including our work with Junior Achievement Worldwide to create an AI-powered coach to help students pitch and present their ideas. These are the kids who will be building the AI-native businesses of tomorrow ... I can't wait to see what they achieve.

Lastly, none of this would be possible without trust. We work hard to earn and keep that trust by leading with integrity and embedding responsibility into how we operate. Over the past several years, we have worked to set the standard for accountability and compliance in our profession—and we will not let up. That includes continued investment in our risk, legal, and compliance capabilities, as well as clear standards for how we use AI and achieve our emissions reduction targets.

It also includes the kind of institution we aim to build as we step into our second century. Our commitment to a diverse meritocracy and to developing leaders through apprenticeship, sponsorship, and mentorship remains central to who we are. That commitment matters beyond our four walls: For the third year in a row, TIME has named McKinsey the top company for future leaders.

Optimism can be hard to come by these days ... just not at McKinsey & Company. Thanks for reading.

![](images/8da347bc57824b918ca43a9d8a12c3fb741572a7398aef4d619cbd89f0d95eb1.jpg)  
Bob Sternfels kicks off our centennial celebration at the global partner gathering in Chicago.

## Bob Sternfels

Global managing partner, McKinsey & Company

![](images/9f92ea8f4766306c5877c86ed89429b6a379e418a698f6ecb12aa1e808e51ba2.jpg)

## Our approach to impact

We partner with our clients, colleagues, and communities to accelerate sustainable and inclusive growth around the world.

## About our firm

CEOs and boards turn to us when the stakes are highest and the decisions will define their institution's future. At moments of disruption, transformation, or growth inflection, we help leaders set direction and translate ambition into measurable performance. We bring together deep industry expertise, advanced analytics, and hands-on execution to redesign operating models, build digital and AI capabilities, and strengthen institutions for enduring impact.

Learn more about our purpose, mission, and values.

Our clients have contributed: $^{1}$

## How we make an impact

16% of global GDP growth

1M

— Develop and share insights that drive action, including through our institutes

new jobs per year

— Help clients turn ambition into real-world results

— Give back to our communities through pro bono consulting, volunteering, and financial support

— Lead by example through our firm’s own actions and operations

>80%

of reported CO $_{2}$ emissions reductions

Economic
opportunity

Health

## Our focus areas

While our efforts to accelerate sustainable and inclusive growth span many areas, we focus on four where our capabilities and scale enable the greatest impact: economic opportunity, health, environmental sustainability, and tech-enabled inclusive growth. In each, we deliver measurable results and strengthen the foundations for long-term progress.

This report curates examples of our impact with more on our website.

Environmental
sustainability

Tech-enabled
inclusive
growth

# A century of helping organizations think bigger, build stronger, and expand opportunity for all

![](images/19269ee2d9edcae710b66aaef088dd1c98d1d4d753004aa3f3efb1a5cd58a7ca.jpg)

## 1926

Firm founded
James O. McKinsey establishes his eponymous consulting firm with a commitment to rigorous research and training.

## 1954

Pro bono work
Our partners vote to begin pro bono work for the Red Cross and other nonprofits, establishing a firm-wide commitment to giving back.

![](images/c205b9b236e00d2edb1c33c8424eba46f546f3a3905461b32e7e26b17b92292c.jpg)

## 1964

First women MBAs
Harvard Business School
graduates its first eight women
MBAs, three of whom we hire.

## 1967

Public health and air pollution
We work with New York City on public health issues, including reducing air pollution.

## 1989

Early action on climate change
We conduct one of the earliest assessments of the costs of combating global warming and identify international funding mechanisms.

## 1990

McKinsey Global Institute
We launch the McKinsey Global Institute to provide a fact base to aid decision-making on critical economic and business issues.

![](images/8a273543549c1f49782e2a586748b501b38a117a8212f004a3ae3ff2a03013fd.jpg)

## 1995

Support for LGBTQ+ colleagues
Our colleagues create GLAM,
our firm's LGBTQ+ network.
Now known as Equal, the
network has more than
1,800 members worldwide.

## 2000

We create a practice dedicated to nonprofits, foundations, and other nongovernmental organizations.

## The third sector

## 2020

## Climate analysis

## 2007

We launch a climate initiative, publishing the first global greenhouse gas cost curve to compare emissions-reduction options to help our clients decarbonize.

![](images/c6f0c58d8660e88e9ac866d0d713485877026540101ee97e878796f77c855d9b.jpg)

## 2022

## 2022

McKinsey Health Institute
We create the McKinsey Health Institute ↗ to catalyze the research, actions, and investment needed to advance human health, adding years to life and life to years.

## 2014

## 2014

McKinsey.org
We launch McKinsey.org, offering free skill-building programs to nonprofits and individuals.

Solutions to eradicate malaria
We join experts through Malaria
No More to help chart a path
to eradication by 2040.

McKinsey Institute for Economic Mobility
We launch the Institute to advance Black lives and, building on that success, later expanded our economic mobility agenda to Latino and rural communities.

Jobs that change lives
We create Generation,
a nonprofit focused on global
youth unemployment, which
trains and graduates more
than 125,000 students across
17 countries by its 10th anniversary. $^{2}$

## Responsible practices

## 2019

![](images/c06bdbf14bded65c2bd0beb693853a80cd9066a45a06335c9293f25f562a71ec.jpg)

## 2025

We introduce the most rigorous client selection policy ↗ in our profession, supported by an investment in our global risk, legal, and compliance teams that began in 2018.

More than 100 million people supported
We reach the milestone of supporting more than 100 million people toward economic opportunity through our nonprofit partners and pro bono programs.

In A Century of Plenty, the McKinsey Global Institute documents the unprecedented gains in prosperity, health, and living standards achieved over the past century, and concludes that the world does have the resources for every country to reach the living standards of today's most advanced economies by 2100. Building on the lessons of that progress and our history, we are working with leaders across sectors to help shape the next century of plenty—through growth that is sustainable, inclusive, and enduring.

![](images/852bcf5be8a1e1dc7869a94567d52fb4135f504bb1384938d9ad748cc4c0e610.jpg)

# Growing economic opportunity

The past century demonstrated what is possible when growth accelerates and opportunity expands. $^{3}$ Extending that progress so more people can fully participate in it remains one of the defining economic priorities of our time. We work alongside companies, governments, and nonprofits to broaden access to quality jobs, strengthen income mobility, and build more inclusive labor markets. We complement this work with no-cost skill-building programs that help nonprofits increase their effectiveness and equip individuals to succeed in roles that improve their lives. Through our research, we provide leaders with rigorous, fact-based insights to support coordinated action that expands economic opportunity at scale.

## In this chapter

7 Jobs and reskilling

8 Economic mobility and affordable housing

9 Education

![](images/59dc8953715df40c8381e674e182a6c554f2c8d95dbea68850195fe24523f917.jpg)

![](images/1685ca4bc86c004fdc22191b8434feb7550478c5559f7e308b68207495613763.jpg)

Abednego Brandy Opey, a graduate of the McKinsey.org Forward program.

# Jobs and reskilling

We equip people with the skills and access they need to secure higher-paying jobs that improve their lives.

## Featured insight

## The upskilling imperative: Required at scale for the future of work ↗

AI and technology are reshaping work and redefining the skills required to compete. This report highlights how closing critical skills gaps can expand economic opportunity while enabling employers to build workforces that are adaptable, resilient, and positioned for sustained performance.

## Giving back

## Building essential skills through the McKinsey.org Forward program

Forward ↗ is our free, ten-week, online learning program that equips individuals—especially those early in their careers or navigating transitions—with practical, future-ready workplace skills that enable them to thrive in a rapidly changing workforce. In 2025, we graduated approximately 120,000 learners across the 133 countries where Forward is available.

"Being part of the McKinsey.org Forward journey was like having a personal coach for my career, helping me recognize and address patterns in my behaviors. The tools helped me grow quickly in my new role."
—McKinsey.org Forward alumna

## Client impact

## Expanding economic opportunities for rural farmers in East Africa ↗

We supported Kentegra Biotechnology in refining its growth strategy and unlocking \$25M in funding that expanded job creation and support for local farmers in Kenya and beyond. With a clear path forward to grow its financial and operational capabilities, Kentegra is driving more stable employment, including more than 300 direct jobs, higher incomes for over 20,000 farmers, and increased resilience across rural communities in East Africa. $^{4}$

## Leading by example

![](images/3e24e3ee351f89f6329324d15a2a1a10daea4a7b3352d027b95450718c277688.jpg)

## Advancing the world's preeminent leadership factory

In 2025, TIME and Statista named us the world's number one company for future leaders for the third consecutive year. This recognition reflects the

strength of our leadership model: continuous skill building, apprenticeship and hands-on experience, and sustained sponsorship and mentorship at every stage of a career. We invest deliberately in developing leaders across roles, tenures, and geographies, building capabilities that endure well beyond any single engagement or role.

# Economic mobility and affordable housing

We help leaders across sectors work together to increase economic mobility, expand access to affordable housing, and address the housing and homelessness crisis.

## Featured insight

Investing in housing: Unlocking economic mobility for Black families and all Americans ↗
Quality, affordable housing is out of reach for many Americans, and a persistent housing shortage is at the heart of the problem. Investing to close this housing shortfall could unlock as many as 1.7 million jobs and add nearly \$2 trillion to GDP through 2035.

## Giving back

## Unlocking career paths for workers through skills-first hiring ↗

We partner with Opportunity@Work to tackle a simple but stubborn problem: Millions of capable workers are locked out of good jobs because they don’t have a four-year degree. By helping employers shift from degree screens to skills-based hiring practices, we’re helping open pathways to higher-wage roles for workers Skilled Through Alternative Routes (STARs), supporting Opportunity@Work’s ambition to unlock \$20 billion in aggregate wage gains for STARs by 2030.

## Client impact

## Advancing economic mobility in the United States with Blue Meridian Partners ↗

In collaboration with Blue Meridian Partners, we work alongside organizations to expand economic mobility—from strengthening historically Black colleges and universities (HBCUs) by driving enrollment growth and contributing to a \$1.3 billion increase in net assets, to helping school system leaders deploy \$35 billion in federal funding to accelerate learning. Together, we also developed the Economic Mobility Analytics Tool, drawing on 30 data sources and more than 200 indicators across education, income, housing, and health to help communities identify mobility gaps and focus on effective solutions. $^{5}$

## Leading by example

## Opening pathways to exceptional talent

We believe exceptional talent can come from anywhere, and our diverse meritocracy reflects that conviction. Our global Prism ↗ community helps us attract, support, and advance colleagues from a wide range of socioeconomic backgrounds, strengthening our firm and the perspectives we bring to clients.

![](images/fce883d77afc83461e1932c25c36633ea053045abd836e5898c7c6c1dfcc4363.jpg)  
Sarah Tucker-Ray, a partner and a leader of the McKinsey Institute for Economic Mobility.

![](images/794b5a5daa9e55efa11eebb6c871fe8fcf4a5f5bcd9aed32ec3a791a95311d3e.jpg)

Davis Arifin, a partner and a leader of our Young Leaders for Inclusion initiative in Asia.

# Education

We work with education leaders to improve student outcomes, expand access and affordability, and enable new academic research.

## Featured insight

## Manufacturing in rural America: A plan for K-12-industry partnerships ↗

As manufacturing expands in rural America, schools and employers have an opportunity to better prepare students for local jobs. We highlight practical ways K–12 schools and manufacturers can work together to connect classroom learning to the skills these roles require and to create clear paths from school to employment. When these partnerships are strong, students gain access to good jobs, employers build a reliable local workforce, and local economies benefit.

## Giving back

## Developing the next generation of leaders across Asia

Through our Young Leaders for Inclusion initiative, more than 100 colleagues across Malaysia, Singapore, the Philippines, Indonesia, Vietnam, Thailand, and Sri Lanka delivered in-person leadership training to university students. Students then applied these skills to real challenges from nonprofit partners—receiving hands-on coaching from our colleagues while delivering solutions that strengthened nonprofit impact and gave students direct, real-world leadership experience.

## Client impact

eHBCU: A first-of-its-kind HBCU online consortium to expand economic mobility through education ↗
Delaware St

[中间内容因长度限制已省略]

 launching Deuna!—a new digital bank and payments ecosystem used by six million payers and 500,000 merchants—we helped expand access to formal financial services for previously underserved and unbanked customers, while bringing more merchants into the formal economy. $^{10}$

## Leading by example

## Enhancing our recruitment efforts with AI

As part of our firm's own digital transformation, we're modernizing our recruiting process to better support both candidates and interviewers. From tools that help interviewers sharpen their skills to AI-enabled interview prep for candidates, we are exploring ways to expand access, flexibility, and consistency to help candidates feel more confident and prepared.

## Artificial intelligence

We harness AI as a force for good to help organizations reimagine how they work, grow, and advance inclusive growth.

## Featured insight

The state of AI in 2025: Agents, innovation, and transformation ↗

AI is everywhere, but for many organizations, real value remains elusive. We surveyed leaders globally to understand what's working and found that organizations that move beyond pilots—by redesigning workflows and embedding AI into strategy—are the ones turning AI adoption into meaningful performance and growth.

## Giving back

Preparing the next generation of confident communicators in an AI-driven economy ↗

Through our AI for Good initiative, Noble Intelligence, we partnered with JA (Junior Achievement) Worldwide to help students build essential communication and entrepreneurial skills. Together, we co-created JA Pitch Master, an AI-powered communication coach that could help more than 500,000 students practice and improve their pitching and presentation skills, built on responsible AI guardrails to support safe and inclusive learning. $^{11}$

## Client impact

Transforming clinical authoring through AI with Merck ↗

At Merck, the time and effort required to produce clinical study reports were limiting the speed of regulatory submissions. Drawing on the AI and data science expertise of QuantumBlack, McKinsey's AI arm, we partnered with Merck to build an AI authoring platform that cuts drafting time from weeks to days, improves quality, and enables authoring teams to focus on higher-value analysis—helping bring new medicines to patients faster.

## Leading by example

Embedding responsibility at the core of our AI
We take a comprehensive, end-to-end approach to responsible AI, embedding ethics, safety, and human oversight into how we design, deploy, and scale AI. Our Responsible AI Principles and Responsible AI Standard set clear expectations for accuracy, fairness transparency, security, and privacy, supported by firm-wide governance, continuous monitoring, and required training. Together, these guardrails enable innovation at scale while helping teams and clients manage risk and build trust as AI evolves.

![](images/b312ceccc31c863f7bdb4dfb6048888bf2cde0144298fdd81ba7072193ab76fe.jpg)

Rory Walsh, a partner and a co-leader of QuantumBlack Labs, our center for AI innovation.

# Future of work

![](images/2e9c202c2d6d36594db0ca22fcdbe7f4131ac328dd557d481d3c8a77bcd1deaf.jpg)  
Generation learners in Thailand, one of 17 countries where the global employment nonprofit operates.

We shape the future of work by redesigning how people, technology, and organizations come together to perform at their best.

## Featured insight

## Agents, robots, and us: Skill partnerships in the age of AI ↗

As AI agents and robots take on more tasks, the real challenge is redesigning work so people and technology perform better together. We show how new skill partnerships—where humans focus on judgment, creativity, and oversight while machines handle execution—can reshape workflows, boost productivity, and unlock economic value.

## Giving back

Helping people find the right job, faster
For the past decade, we have partnered with Generation to train and place adults into otherwise inaccessible careers. In 2025, Generation surpassed 140,000 cumulative graduates who have collectively earned more than \$2 billion in wages. $^{12}$ To accelerate this impact, we helped Generation build an AI-enabled tool $\nearrow$ that matches online job vacancies with their learners' skills—resulting in faster, more relevant job placements, better career outcomes, and a solution that can be scaled across Generation's 17 countries.

## Client impact

Driving a digital, operational, and skills transformation to take Jubilant Ingrevia's business to the next level ↗ When India-based Jubilant Ingrevia faced volatility and slowing growth in its specialty chemicals and life sciences ingredients businesses, we partnered to modernize its manufacturing, supply chain, and commercial operations. By embedding digital analytics and upskilling teams, we delivered more than \$13 million in EBITDA impact and built a more agile workforce empowered to make data-driven decisions. $^{13}$

## Leading by example

Reimagining the way we work to unlock value for clients

We are integrating AI into our processes so we can spend more time where it matters most for our clients. Our colleagues have already developed more than 25,000 AI solutions to handle routine tasks, freeing up time to focus on higher-value strategy, creativity, and client engagement. By redesigning workflows so AI becomes a true collaborator, we are delivering faster insights, clearer decisions, and even stronger client outcomes.

Illustrations in the report were created with the help of AI.

Learn more online at: McKinsey.com/sustainable-inclusive-growth-report

We welcome your comments and questions regarding this report. Please contact us at Social\_Responsibility@McKinsey.com
"""
