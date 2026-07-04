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
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
![](images/88ecb9943d65fe39e0e7b13b921effa19495c918b214566e708af905d09c9bf9.jpg)

BUSINESS TRANSFORMATION

# Harnessing the Human Side of Transformations

By Tuukka Seppä, Kristy Ellmer, Julia Dhar, Simon Weinstein, Garett Chau, Paul Catchlove, and Connor Currier

ARTICLE APRIL 27, 2026 8 MIN READ

The imperative for companies to transform is growing, but organizational transformations have a low success rate. According to BCG research, only about one in four succeeds in capturing short-term and long-term value. What sets the best, most successful transformations apart? A growing body of research from BCG's Bruce Henderson Institute and the firm's Behavioral Science Lab points to a crucial factor: a human-centric approach.

Human-centric transformations are grounded in, and informed by, principles of behavioral science—an understanding of how people act in different contexts—to predict behavior and design techniques and practices that can help achieve target outcomes. This type of transformation isn’t always easy. It requires elevating people at all levels, from top executives to frontline employees, to the center of the change process and tapping into their collective effort. But the approach can be learned, and it leads to measurably better transformation outcomes.

Companies that undertake human-centric transformations see faster scaling of initiatives, increased human capacity and capital within the organization, and better financial outcomes. In our experience supporting hundreds of transformations across industries, companies that make holistic, people-centered change management an integral part of the transformation outperform their peers by 15% in total shareholder return.

# The Power of Human-Centric Change

All transformations require considering the why, what, and how of the overall program. (See the exhibit.) True success hinges on a human-centric approach across all three:

• Why: Articulating the overarching purpose for undertaking the transformation now

\- What: Identifying the financial and operational objectives that must be met to create greater value—revenue growth, cost reduction, a stronger balance sheet, or some combination of the three—all aligned with the company strategy

\- How: Developing the behaviors, mindsets, organizational structure, tools, capabilities, and processes to make change happen and ensure that it sticks

# Transformations Are More Likely to Succeed When They Address Three Elements

![](images/01d8d9197a0b085dd3635ee60d178387b3b19d1400b81435f73f7be60c1d18a7.jpg)  
Source: BCG.

Here we focus on the “how” element, which is where a human-centric approach is crucial. Transformations rely on people’s willingness to change and do things differently, yet people are naturally averse to change. By applying best practices from behavioral science to address this aversion, transformations can achieve better and more lasting outcomes.

We have strong evidence of the power of human-centric change. Specifically, we see the following increases in the likelihood of sustained performance improvements through a people-based approach to transformation:

\- 90% when holistic, people-centered change management is an integral part of the transformation

\- 27% when leaders are aligned on their roles and responsibilities in the transformation and can shape the behaviors of people on their team.

\- 21% when a chief transformation officer is in place with sufficient authority to lead the transformation, challenge the status quo, and lead the overall workforce

\- 19% when all people in the organization are clear about what needs to change, how they can contribute, and how their work will evolve

# Four Elements of Success in Driving Human-Centric Change

The “how” of transformation comprises four elements: leader enablement, people engagement, executional certainty, and desired culture.

Leader Enablement. Enabling leaders to support the change is critical in a transformation. Since organizational buy-in is paramount, transformation leaders must develop an explicit case for change that they can communicate consistently and pervasively to their teams: what will change, what will stay the same, and how both will contribute to the overall change program. The case for change is grounded in the broader “why” of the transformation and helps leaders to articulate why change is needed, instill a sense of urgency, and spur the right actions among the people on their team.

Transformations also require specific targets and timelines to help leaders steer toward defined goals, with related incentives (both short term and long term) that are linked to leaders' personal performance and their teams' overall results.

Another aspect of enablement is ensuring that leaders are clear on their roles and decision rights. Moreover, companies should push leaders to look beyond traditional command-and-control models and instead inspire their teams with a more empathetic approach that incorporates the head, heart, and hands elements of a change program.

People Engagement. In addition to enabling leaders, companies need to assess the transformation's impact on their people—taking into account other initiatives that are currently underway, what else has happened recently in the organization, and the capacity needed to take on new efforts—and demonstrate that they have a good sense of how employees are feeling. An impact assessment can help companies understand the potential burden that the transformation will create for key stakeholders and get ahead of people risks by reducing cognitive loads.

Companies should also create a robust communication roadmap to deepen engagement with the mass of the organization that is doing the work. For example, a communication platform can ensure that employees understand the need for change and the level of urgency. Monthly newsletters can provide clear updates on how the transformation is progressing, so employees feel informed and see their individual efforts reflected, shared, and even celebrated across the organization. Town halls and pulse checks can provide a mechanism for employees to provide feedback and ensure that they feel heard and have a voice in the transformation.

Effective people engagement also involves understanding and addressing skill gaps in the organization as part of broader capability and confidence building. In addition, leaders can designate influential employees as change champions, as well as celebrating wins by teams and individual employees, to build enthusiasm for the transformation among the frontline workforce.

Executional Certainty. All transformations should be coordinated through a transformation office, which establishes clear governance and practices and creates a structure that organizes teams and people in explicit roles and ensures accountability. The office also sets a cadence for the overall program, such as weekly meetings for the extended leadership team and quarterly town halls for the full workforce.

Moreover, a rigorous stage gate methodology ensures that initiatives move forward in incremental steps and that the original goals of the program remain realistic. Robust reporting mechanisms provide real-time, efficient status tracking and a single source of truth, eliminating confusion about where the transformation currently stands.

Desired Culture. A transformation will succeed only if it fundamentally changes the organization's culture. Companies should conduct a diagnostic to obtain a current view of their organization's culture, operating model, leadership style, and ways of working. Doing so can lead to valuable insights, such as identification of specific areas that must be addressed to support a sustainable target culture. Moreover, companies can engage leaders, and the outsized impact they have on organizations, to model behaviors that will bring the new culture to life. For example, if a company aims to increase transparency to enable more informed decision making and a greater sense of inclusion, leaders can begin to share monthly reports and key leadership readouts with their teams. Such behaviors should be embedded into daily routines, processes, and policies, and companies should actively measure progress using quantifiable metrics.

## One Company's People-First Approach to Transformation

A leading global beverage company found itself underperforming compared with the competition in key metrics. To improve, it launched a comprehensive transformation, leveraging digital technology to make its supply chain more efficient and sustainable. Critically, the company also addressed the people component of change, focusing on each of the four parts of the “how” of transformation:

\- The company developed a clear and compelling case for change and designed a tailored leader enablement program to upskill 250 leaders.

\- Frequent communication through town halls, newsletters, and other channels ensured buy-in across the enterprise. Pulse surveys gave leaders crucial feedback from the workforce, with

more than 95% of employees saying that they understood the purpose of the program and more than 80% rating it favorably (a share that increased over time). Quarterly scorecards gave everyone a clear sense of progress.

\- The program included more than 4,000 initiatives across nine workstreams in 24 countries. To keep everything on track, the leadership team deployed a robust governance structure, including a transformation team that built a roadmap with clearly defined stage gates. A regular cadence of weekly and monthly meetings, along with transparent reporting, created visibility across the organization.

\- Critically, the company addressed its culture, examining whether employee and leader behaviors were supporting the change ambition. By clarifying roles and creating a collaborative working environment, the company was able to overcome numerous challenging practices and improve performance across all business units and functions.

By putting people at the center in this way—focusing not just on the “what” but also on the “how” of the transformation—the company reduced supply chain costs by 15% to 20% and improved productivity by 55%. The newly digitized, efficient, and resilient supply chain helped the company close the performance gap with peers and gave it a sustained competitive advantage in operations.

Transformation is an urgent priority for most companies, but it’s tough to get right. To succeed, they need to focus on the people aspect of change. This is a more holistic approach to transformation, but in our experience, it yields commensurate benefits in sustainable value and new capabilities—leaving companies far better equipped to thrive in the long term.

## Authors

![](images/1a35fdc937f38769fcc70177f01311ebf711c8f91ed707bc81f4c05d83eb77eb.jpg)

![](images/2a320985b2a3dba9d5cd62d1fec62a9d998b2a6a090f5737656da5f556e2e3c6.jpg)

![](images/d43943e475ae2724bb0cd5667600b4947d566b40a922e1e6d3f7524975bfc148.jpg)

![](images/7ac45512154565f19314b6e24467dc5c2861d00c4017b4ee6cd37143bf06a8a8.jpg)  
Managing Director & Senior Partner; Global Leader, BCG Transform Practice
Helsinki

## Tuukka Seppä

![](images/f6ede115959105f247261f5d907d8affd8af9b6121866fd8d429a0e31433ff76.jpg)

![](images/c95fd8448a900c6c39b7e3a490922e3a53c51533d706fbfe57d37ccc0656b809.jpg)

Managing Director & Partner Miami

![](images/7b3041dc8cd9f3b8f19b1c1b44d08e86b164372e49968366a8de243e489986af.jpg)

## Garett Chau

Managing Director & Partner Miami

![](images/d64bca3d8b1c2f2421d0fbe481664e2a725df97fe36fbab4b7b4f5e8687a0efe.jpg)

## Connor Currier

Senior Director
ACC – Boston

![](images/88e572e923998e78bc0ca854b6932b763554c23ecff95f18306436014af5ac3a.jpg)

![](images/f1d42579dce8b466fbc137736d9a7c14bd64308638791209c78377b9ad0264b0.jpg)

![](images/80e6b8eaaf7c6e6dcf22e776cefd14e6878d51b0d938edfc083d845195acdba9.jpg)

## Kristy Ellmer

Managing Director & Partner
Boston

![](images/bafcf61efa0371b42314511ad4003d309fdbec35e19d4405b774a926cbcf12bb.jpg)

## Simon Weinstein

Managing Director & Partner; Global Product Lead, BCG Transform
Seattle

![](images/d67bd15b8fb160afdf33d9c7662108f73572c53d390042557c801865384bdab8.jpg)

![](images/217617f8abf2b0db3ca6112d76be43809f7c04759090d16e6a6fa21140f9da39.jpg)

## Paul Catchlove

Senior Director – BCG
Transform
ACC – Boston

![](images/e7c30dd428542fbd72ea7237d0d5e23858071bfb493cc0b281963b51cdddcbe7.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
