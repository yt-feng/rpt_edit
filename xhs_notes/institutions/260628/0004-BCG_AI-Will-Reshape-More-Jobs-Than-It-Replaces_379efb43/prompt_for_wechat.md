你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/e2d6e16a072dd2c009daf2810773723e0dd1880b962e4ec2ba34e88c97a9e112.jpg)

ARTIFICIAL INTELLIGENCE

# AI Will Reshape More Jobs Than It Replaces

By Greg Emerson, Matthew Kropp, Julie Bedard, Lisa Krayer, Viacheslav Romanov, Megan Hsu, Luis Sanchez Boedo, and Diya Mohnot

ARTICLE APRIL 03, 2026 15 MIN READ

Over the next two to three years, 50% to 55% of jobs in the US will be reshaped by AI. For many employees, this will mean that they retain the same or a similar role but face radically new expectations for how they work and what they produce. For company leaders, it will require a clear vision for how the transformation is managed, including a scaled, strategic approach to upskilling and reskilling and the restructuring of career ladders.

This shift is already happening—and will pick up speed as AI adoption spreads. Our analysis, based on microeconomic modeling, identified a significant swath of the labor force for which AI will meaningfully augment current roles. Moreover, when the productivity gains from AI use trigger increased end product demand and the potential for augmentation is high, we believe there will be a need for more and, in some cases, new human roles. (See Exhibit 1.) While job augmentation and new-job creation will happen rapidly, full substitution of jobs by AI will be slower. Five years from now—or perhaps further in the future—10% to 15% of jobs in the US could be eliminated. $^{1}$ This level of potential job loss is considerable and creates an important call to action for business leaders.

## EXHIBIT 1

Two Critical Factors in AI's Impact Are Labor Substitution and Demand Expandability

![](images/ef61ea66863ded51a6b55d401d17d7942e7b9594d3a5ef9186ccb3c231c568e4.jpg)  
Source: BCG Henderson Institute analysis.

Critically, our analysis is not intended to be an unemployment forecast. It does not account for macroeconomic factors such as geopolitics or inflation, nor does it contemplate the impact of new AI breakthroughs beyond the capabilities of today's frontier models. Moreover, our model can't solve for powerful and influential unknowns, such as the future impact of AI on the accessibility of jobs and the speed with which the technology is adopted. (See “Methodology: Translating Automation Potential into Labor Market Outcomes” for more on our approach.)

## — Methodology: Translating Automation Potential into Labor Market Outcomes

This analysis applied a structured microeconomic framework to assess how AI reshapes employment outcomes. Rather than equating automatable tasks with job loss, we evaluated three distinct forces: task-level automation potential, substitution versus augmentation dynamics, and demand expandability.

## AI Task Automation Potential

We began by estimating automation potential at the task level for each role. Using granular occupational data (Revelio Labs' 1,500-role taxonomy, O\*NET task decomposition, and Revelio headcount data), we evaluated the share of individual work activities within each role that are automatable given current AI capabilities.

Each task was assessed using a structured rubric and classified as automatable if it met the following criteria:

\- The task does not require a significant physical human presence or manual interaction in the real world.

\- The task can be executed without substantial emotional intelligence, negotiation, or complex interpersonal judgment.

\- The task is sufficiently structured to be performed without excessive ambiguity or open-ended reasoning.

\- The necessary data inputs are observable or available to an agentic AI system.

\- The task's outcome is governed by rule-based logic grounded in documentation, precedents, or established procedures.

For each role, we applied the share of time spent on each automatable task to estimate the overall task automation potential. Roles with automation potential below the average of 40% were classified as lower automation, as they are less likely to be prioritized for material disruption in the next four to five years. We segmented lower-automation roles into enabled and limited-exposure roles using a 25% automation potential cutoff. Roles exceeding the 40% threshold were evaluated in subsequent stages of the analysis.

## Substitution Versus Augmentation

For roles with meaningful automation potential, we assessed whether AI is more likely to substitute for labor or augment it. This depends on the degree of human value embedded in the role, which we evaluated on two dimensions:

\- Human Interaction and Judgment. We determined whether reliable performance requires significant emotional intelligence, negotiation, or complex interpersonal judgment. Roles scoring low involve routine, transactional interactions in which persuasion needs are minimal and outcomes hinge on objective criteria requiring limited discretion; these roles are more likely to be substituted. Roles scoring high require nuanced interpretation of emotional and social cues, and outcomes depend on trust, persuasion, and contextual judgment; these are more likely to be augmented.

\- Process Structure and Repeatability. We evaluated how structured and codifiable the workflow is. Roles scoring low involve structured, repeatable processes with well-defined inputs and outputs; these roles are more susceptible to substitution. Roles scoring high involve open-ended problem solving and frequent exceptions requiring expert judgment; these roles are more likely to be augmented.

## Demand Expandability

Even when AI substitutes for humans in executing tasks, labor outcomes depend on whether productivity gains expand total demand. We evaluated demand expandability through two lenses:

\- Demand Headroom. We evaluated whether AI-driven reductions in unit cost or cycle time unlock additional output. We assessed this on the basis of two empirical signals. First, we estimated industry-level price elasticity by relating changes in industry price indices to changes in real industry output, normalized for overall real GDP growth.\* Industries where output is especially responsive to price movements were classified as more elastic, implying that AI-driven cost reductions are likely to translate into higher demand for output.

Second, as a proxy for unmet demand, we used labor market indicators, particularly job openings from the US Bureau of Labor Statistics' Job Openings and Labor Turnover Survey. Openings were normalized for baseline turnover to avoid overstating demand in high-churn occupations. A persistently elevated job opening rate suggests that employers face supply constraints, indicating latent or underserved demand.

Together, these measures help distinguish industries where demand is expandable from those that are saturated.

\- Structural Scalability. We used this lens to evaluate whether supply can scale if demand increases. Even when demand headroom exists, expansion may be constrained by capital intensity (such as physical capacity, capex requirements, or long lead times) or by credentialing barriers (including education level, licensing, certification, regulatory requirements, and extended training pipelines). In roles with high structural scalability, demand expansion is more likely to translate into employment growth.

## Defining Roles Versus Jobs

We applied our model at the level of roles. We evaluated each role and translated the resulting insights into impacts on the total number of jobs. A role refers to a type of work defined by a specific set of responsibilities, while jobs refer to the positions within a role. In our dataset, approximately 165 million US jobs (the employment level as of January 2026 reported by the US Bureau of Labor Statistics) are distributed across roughly 1,500 distinct roles defined by Revelio Labs. (Revelio aggregates publicly available professional profile data, including LinkedIn profiles, and applies weighting adjustments to account for workers not represented in the data.) Our analysis focuses on the US labor market, where Revelio's data is more comprehensive than elsewhere.

## Quantifying Potential Job Impact

To estimate the share of jobs potentially vulnerable due to AI, the model considers:

\- Substituted Roles: the number of jobs where AI substitutes for human workers multiplied by the role's automation potential

\- Divergent Roles: the number of jobs where AI substitutes for human workers multiplied by the role's automation potential multiplied by a demand-expansion adjustment (0.5–1.0) reflecting how much employment persists as output grows

\- Aggregation Across Roles: adding together these adjusted impacts across roles produces a point-in-time estimate of 10% to 15% of US jobs that are vulnerable over the next four to five years

## Quantifying Potential Share of Reshaped Jobs

We defined reshaped jobs as those in which AI materially changes how work is done, even if the job itself remains. This includes amplified and rebalanced roles, where AI augments work; remaining roles in substituted and divergent categories, where workers will need significant upskilling; and enabled roles with more than 25% automation potential, where task exposure is high enough to alter day-to-day responsibilities. Aggregated across roles, this suggests that 50% to 55% of US jobs could be reshaped over the next two to three years.

## Scope and Limitations

The analysis reflects current AI capabilities, with a focus on large language models and autonomous driving technologies because of the demonstrated commercial progress in both domains. Other forms of physical AI and robotics were excluded, as large-scale deployment across most industries remains limited. While advances are accelerating, we do not expect diffusion to materially alter labor market outcomes in the near term. The results therefore reflect potential exposure under current AI capabilities; realized outcomes will depend on how quickly organizations deploy these technologies.

If AI systems were to consistently perform open-ended, judgment-intensive tasks autonomously at human-level proficiency, the distribution of roles across the substitution and augmentation categories would shift materially, and the framework would need to be revisited.

This is a microeconomic assessment of labor impact, not a forecast of aggregate unemployment or near-term layoffs. Employment outcomes are also influenced by macroeconomic forces—including inflation, interest rates, trade policy, recession cycles, and geopolitical dynamics—which are outside the scope of this analysis.

That said, the analysis provides clear guidance for CEOs on how to act in the face of this workforce shift. They are making decisions today that affect their people and the viability of their business, and they need a nuanced view of AI's impact. Those who cut their workforce beyond AI's ability to replace it will see productivity drop, institutional knowledge disappear, and critical talent walk away. Those who fail to dramatically rethink work will see their competitors grow faster and more profitably.

# Task Automation Doesn't Have to Mean Job Loss

To build our model, we calculated the number of jobs involving tasks that are at least 40% automatable. This represents the average level of automation for all US-based occupations and the threshold after which role and organization redesign becomes a stronger business case. The 43% of jobs that exceed this threshold formed the focus of our analysis. The other 57% are jobs that depend heavily on the physical presence of human workers, on hands-on work, or on sustained human interaction, all of which limit the potential for automation and thus are less likely to be disrupted by AI. (See Exhibit 2.)

## EXHIBIT 2

Agentic AI May Drive High Levels of Task Automation in 43% of Jobs

![](images/78962d42aceb9e51a76aeef77cce6046c63cf389c79422518ab36c16aa7d9b70.jpg)  
Sources: Revelio Labs; O\*NET; US Bureau of Labor Statistics; BCG Henderson Institute analysis.

Substitution Versus Augmentation. To illustrate the difference between substitution and augmentation, consider call center representatives and software engineers, two roles that are already deploying agentic AI at scale.

A call center representative is typically responsible for resolving a defined set of customer inquiries within established workflows. Much of the work involves structured interactions such as account lookups, policy explanations, and scripted troubleshooting. When AI systems can reliably handle these repeatable inquiries end to end, fewer representatives are required. In this setting, the workflow can often be clearly bifurcated, with AI handling first-line interactions and humans focusing on escalations and exceptions.

In some cases, representatives can transition into higher-value roles focused on relationship building and proactive risk mitigation. But overall employment in the call center rep role will decline as the most structured tasks are absorbed by the system.

A software engineer, by contrast, produces a very different output. While coding includes routine elements, the core value of the role lies in system design, architectural judgment, tradeoffs between performance and cost, and the translation of business needs into technical solutions. AI can dramatically accelerate code generation and testing, but given today's capabilities, it cannot replace the system-level judgment required to own the outcome end to end—meaning the work cannot be cleanly divided between system and engineer. Instead, software development becomes an ongoing interaction in which engineers define objectives, refine outputs, validate results, and integrate components into broader systems.

AI supports and accelerates these steps but does not replace the need for human judgment and accountability. As a result, AI helps engineers do their jobs more effectively rather than replacing them, making these roles less likely to experience direct displacement and shifting engineers' work toward system-level thinking, orchestration, and product and design tasks, rather than repetitive coding tasks.

Low Versus High Demand Expandability. When AI lowers the cost of delivering a business outcome or end product, the question is whether demand for the output expands or remains bounded. If lower costs unlock unmet demand, increase accessibility, or accelerate consumption, total output may rise and employment may remain stable or even grow despite significant automation at the task level. If demand for the outcome is fixed, productivity gains are more likely to translate into fewer required workers.

This dynamic is not new. Economists have long observed that efficiency improvements can increase total consumption rather than reduce it, a phenomenon often referred to as Jevons Paradox. When the cost of a resource falls, usage can rise. The same logic applies to labor: whether productivity reduces employment depends on how demand for the output responds.

Software engineering illustrates expandable demand. Organizations across industries continue to face persistent unmet need for digital products, automation, and new features. As AI reduces the cost and time required to build software, organizations often build more. Output expands and overall job volume may remain stable or grow, even as the productivity of individual engineers rises, because humans continue to play a meaningful role. The continued growth of software engineering headcount in the years following the introduction of ChatGPT in 2022 illustrates this phenomenon. (See Exhibit 3.)

EXHIBIT 3
Software Engineering Headcount Has Risen Steadily in the Past Three Years  
![](images/91c7ed5d37efd105069f5f842e9695baf7e7a2120f741b10526493c9b48168ce.jpg)  
Sources: Revelio Labs; BCG Henderson Institute analysis. $^{1}$ Approximately 500 US-based software companies tagged as AI in PitchBook.

Call center representatives illustrate bounded demand. The volume of inbound interactions is largely determined by the size of the customer base and the frequency of service needs. When AI reduces the cost of handling routine inquiries, the number of interactions does not expand proportionally. In this context, productivity gains are more likely to reduce the number of representatives required.

# The Majority of Current Jobs Will Stay but Evolve

By analyzing roles against the factors above, we can identify where they belong in BCG Henderson Institute's proprietary AI Labor Disruption Segments, which comprise six categories. (See Exhibit 4.)

In the US, Most Jobs Will Remain in Some Form in the Coming Years

![](images/83f1d91142457b86155fd54c8af2eccffa7f92cef8343e7204b7b0414242c681.jpg)  
Sources: Revelio Labs; O\*NET; US Bureau of Labor Statistics; BCG Henderson Institute analysis. Note: Demand expandability was not assessed for lower-automation roles, because the expected disruption is less significant.

Amplified Roles. When AI augments human capabilities and demand expands, employment may remain stable or grow. Humans remain central to value creation, and wage inflation may develop as higher productivity increases competition for skilled talent. This type of role represents 5% of current jobs.

Software engineering falls under this category. (For a “what if” scenario, see “What Would It Take for Software Engineering to Move from an Amplified to a Divergent Role?”) So do many lawyers, particularly those in advisory and judgment-intensive areas of law. Investment in legal tech startups, like Harvey AI, reached record-high levels in 2025, spurring significant discussion of how AI will reshape this field. As AI accelerates research, drafting, and case preparation, legal services could become more accessible. In domains where unmet demand exists, such as compliance, regulatory review, and contract management, lower costs may increase the volume of legal work. Senior legal judgment would remain central, with AI amplifying professional capabilities.

## — What Would It Take for Software Engineering to Move from an Amplified to a Divergent Role?

The future of software engineering is an incredibly controversial topic. Some AI leaders have publicly claimed that there’s never been a better time to be a software engineer, while others have forecast the end of the profession. The expandability of demand around the output of software engineers is without question: the number of IT roadmaps is nearly infinite and AI implementation itself will be a massive driver of more engineering output. The question for the medium and long term is whether to categorize the software engineering role as amplified (suggesting that AI will augment the work of software engineers and most jobs will remain) or div

[中间内容因长度限制已省略]

 AI into day-to-day workflows and building broad-based AI fluency across the workforce. The priority is consistent adoption: removing barriers to usage, standardizing tools and workflows, and setting clear expectations so that gains are realized widely.

Shape the AI narrative to unlock performance. Sequencing and signaling matter. Focusing first on highly substitutable roles may deliver short-term efficiency gains, but it can create a demoralized atmosphere that undermines broader transformation. When employees associate automation with displacement, engagement declines and the motivation to upskill erodes. They may resist augmentation efforts, even when designed to elevate their roles. Leaders must communicate clearly that if workers upskill, AI in most roles will be about value creation, not displacement. The narrative set at the top will shape whether the workforce embraces transformation or resists it.

AI creates a massive opportunity for business leaders but also significant uncertainty in terms of how to unlock it. Moreover, this is all happening in a charged environment. In some cases, restructurings that would have occurred regardless, as part of the normal business cycle, are likely to be attributed to AI, which will create fear at a societal level.

At the same time, AI's impact will vary significantly across companies. Some will lean into AI to drive innovation and growth, while others will focus on efficiency and automation. This could lead to very different talent strategies, with some reducing headcount while others hire aggressively.

For CEOs, the imperative today is to focus on achieving the right balance of automation, upskilling, and deliberate talent planning—to deliver enterprise ROI at scale and help their employees develop the skills they need to thrive in the AI era.

The authors would like to thank Djon Kleine, Philip Ventura, Nissim Ray, and Hanson Wong for their valuable contributions to the research and analysis that informed this article.

## BCG HENDERSON INSTITUTE

The BCG Henderson Institute is Boston Consulting Group's strategy think tank, dedicated to exploring and developing valuable new insights from business, technology, and science by embracing the powerful technology of ideas. The Institute engages leaders in provocative discussion and experimentation to expand the boundaries of business theory and practice and to translate innovative ideas from within and beyond business. For more ideas and inspiration from the Institute, please visit our website and follow us on LinkedIn and X (formerly Twitter).

## Authors

![](images/cf063cfabed5bd80ca8f47ee7f6bd850815466d6f7d700dc7c5b13a9d131dff8.jpg)

![](images/d3b8233007a9ce4ed3f42d9c5c0cfc39179096771db848f3406c9dbae1f59296.jpg)

![](images/b55ca3ebcbc1be563274658ddf843ee1ea2f88245038291b84932af845b49f7c.jpg)

![](images/e3a5e47d01fd71ba13b8a42f02b0a81391f4f85fd06e53a147d1161b8379e2b8.jpg)  
Managing Director & Senior Partner
San Francisco - Bay Area

## Greg Emerson

![](images/799cf540b315520b20b9c707be9034a3ad38b5db923c6385e04417a41e23393c.jpg)

## Julie Bedard

Managing Director & Partner; BCG Henderson Institute Fellow
Boston

![](images/1d6b87b6b717eff47c45df8644e16aad3d6d0b3c79c440d4e7a51797f7b16bae.jpg)

## Viacheslav Romanov

Partner & Associate Director, PIPE Tech Capital
Boston

![](images/f30a326d6b9e81eb974c4d1e4ba36122bee3978467b8e2551d26daa35dea9f11.jpg)

## Luis Sanchez Boedo

Consultant
Raleigh-Durham

![](images/f37c010f690f6b6e9378beb3a3a4ca2b0142b0f2449f0a0a135827db4d937982.jpg)

![](images/a18b65d0fe655799eab25f6b8ba7a688776791198ea1cd63ead2e87be51ecf40.jpg)

## Matthew Kropp

Managing Director & Senior Partner; BCG Henderson Institute Fellow
San Francisco - Bay Area

![](images/cb28b6b64891ba59703b09d3d1e9c51ce207cebffc1f5325dcb8a6e6d8f5a122.jpg)

![](images/fc0fb36d23809f56bc82b5232bff7995329a0b6560f117f84936ab901c884c9c.jpg)

## Lisa Krayer

Principal Philadelphia

![](images/e4de0ce6559fba4b817b11c95ec3f6a0fc65f89d3e18eb311815c106c0e2a3d7.jpg)

![](images/0c7e9c6ad67baa08126c2d7a31749a7461dedf477b11af7619a7aa21b14cb68b.jpg)

## Megan Hsu

Project Leader
San Diego

![](images/31b33219ae5a2fcfc8aba84bc2f53f6b8ef7df9c71098a20cb7447cb3fccb25f.jpg)

## Diya Mohnot

![](images/b0931f55c6b1aaa4433fdfc4e1fdd63f2c20b71f563056bd98920f50e625cc0d.jpg)

![](images/8004d65caa91abde61ed5565aa5a2938e3fb1eabd59069d3f815b491938ac274.jpg)

Associate Philadelphia

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

© Boston Consulting Group 2026. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and X (formerly Twitter).
"""
