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
## BCG X | BCG

## BCG AI AT WORK

## Strategy Matters More Than Tools

## Survey parameters

11,749

respondents

![](images/aaa99690530ae1a97eae95ce925fd8bed8ddc8f03a27f06f756282cef963d623.jpg)

![](images/de86d6fc66cdb561a130f1a2293d2d470d4bd02671ac794e7ee3213dbe8d53dd.jpg)  
Sources: AI at Work, 2026 (n=11,749); BCG analysis.

![](images/5aa7235c2c572c985963b5804f86a043e918e7e9abb0e5592b12a1722bed094c.jpg)  
Notes: Frontline employees = individual white-collar employees with no managerial responsibilities. TMT = technology, media, and telecommunications. Nordics include Sweden, Denmark, Norway, and Finland. Middle East includes UAE, Saudi Arabia, Kuwait, and Qatar. Benelux includes Belgium and the Netherlands.

## New findings reinforce trends observed in 2025

![](images/828aba6a760c33ce94f6372fe6c7178af86b59bf44d35d3eb0d7f80f7b60fe5f.jpg)

The time individuals save doesn’t automatically translate into value

42% of frontline employees who are regular AI users save a full day or more per week. But 66% still receive limited or no guidance on what to do with time they save, and more than half don’t redirect it to strategic work.

![](images/abe3726af7301b57aac2cbf16e1e617db843ac53f4abb8cbe4ce244b4b8b82da.jpg)

Rethinking work end-to-end is a prerequisite for creating value

More organizations are using AI to “invent,” building new business models. Companies that redesign workflows end-to-end outperform those that only deploy tools on value captured and employee joy. The gap keeps widening, driven by a clearer roadmap and deeper investment in people.

![](images/a31f92a3f7969bc88d4d50881582c329291de324e6e674c3a677fba49722d9fc.jpg)

Proper training and leadership support remain the biggest unmet promises and strong levers to unlock AI's potential

72% of respondents say expectations about skills have shifted, yet only 36% feel they received sufficient training, stable vs 2025. Only 33% of frontline employees say leadership communicates clearly about AI, and 28% see strong alignment between what leaders say and what the organization actually does.

## Five key takeaways

## 1

No more “silicon ceiling”: frontline employees have integrated AI into their daily work

74% of frontline employees are now regular AI users, an increase of 23 percentage points from 2025. India and the Middle East lead adoption, while the US, France, and Italy trail behind.

## 2

The real challenge is now organizational and managerial

Everyone talks about time saved, but the real shift is deeper and structural. 72% of respondents report skill expectations have changed, and nearly half say their roles have shifted toward managing and directing AI instead of doing the work itself.

## 3

Business value and employee joy aren't tradeoffs, they're driven by the same forces

67% of regular AI users enjoy work more. The organizations that capture the most business value are also the places where employees enjoy working the most.

## 4

The AI “honeymoon” won’t last unless leaders bring strategic clarity driving sustained impact

AI's novelty and cognitive stretch fuel enjoyment early on. But sustained joy comes from strategic clarity. Employees thrive when the direction is real and the message reaches them with strong CEO involvement.

## 5

AI agents went from concept to reality, but operating models haven't caught up

Integration into workflows more than doubled since 2025, and $61 \%$ of respondents believe agents could do half their job within three years. Yet governance (oversight, accountability) still lags far behind the tech.

## New findings reinforce trends observed in 2025

![](images/e48254153321ce0b07d7601fef8a208196105ce7c7e3657395d8be096337b093.jpg)  
Respondents saving at least 8 hours per week

Among frontline
employees who
are regular AI
users, 42% report
saving at least a
workday per week

Leaders have the biggest AI payoff, with 60% saving at least a workday per week

## Some job functions are further ahead than others

Top job functions where frontline employees are saving at least 8 hours per week

60% Marketing

50% Human resources

49% Finance

48% Data science and analytics

## The gap is wide: managers and leaders feel guidance is clearer and perceive more impact than frontline employees

Frontline employees report getting the least guidance on how to spend the time AI saves, and more than half of them don’t redirect it into strategic work

Respondents who say their organizations give limited or no guidance on what to do with the time saved

![](images/56c8f9a6062fd0f6647ac135cc15dd22cc63c1cdee37af4094fe1c9e97be4ab3.jpg)  
Respondents who declare not reinvesting time saved into more strategic work

![](images/3c45f33a647c782e9aa8963577663e8635e3d4fc74810906af12fd555c787f53.jpg)  
Sources: AI at Work, 2026 (n=8,989, includes regular AI users, consistent sample with time-saved analysis); BCG analysis. Note: Frontline employees = individual white-collar employees with no managerial responsibilities.

## How organizations are implementing AI tools

Organizations are
moving past
individual use case
deployments; Invent
initiatives have
nearly doubled

![](images/9325b0ff2daf180d77adc9921453df790e0a1145b19b7b076197726e595df403.jpg)  
Deploy
Supporting adoption of
GenAI tools and
fostering productivity

![](images/8a96fb60851289d64fd55a0848ca3f0a6588427f7ef2b033d6bcdab57c9b3ca2.jpg)

![](images/b61f6798d50f99e21b4fd44fe34b0eade4847fbfe584cef6439803f5336189f5.jpg)  
Invent
Building and innovating
new business models and
products to drive growth

Using AI for
Reshape or Invent
initiatives pays off
by delivering more
value and providing
a better employee
experience

Companies pursuing Reshape or Invent initiatives deliver more value...

Save more time
Employees who
save at least a day
per week

Prove the impact
Employees who see
measurable business
improvement

![](images/8528950b1630a3dc9fa75595bfca21dc34238f94a7c98521f17cf2f0a0034ac4.jpg)  
Earn trust
Employees who fully trust leadership's AI communications

... and their employees thrive

![](images/1dccf9482fa44bdc7ea11c63cb03714e9e725c06eac7e6b990e22704b97b2ebd.jpg)

![](images/0df2ad121ff03a7956357ba8437d9b318052465d679391745cd825b5f4b166d4.jpg)  
■ Respondents at companies that only focus on Deploy initiatives  
Enjoy work more
Employees who
report increased
job satisfaction

![](images/70f1211c2f2a80787e2293f235c989bf93262aa5c84cc3506e103e6b1e9baaca.jpg)  
Show their value
Employees who find it
easier to demonstrate
unique value

![](images/c2a3f19cc1c4a90acac09c73afafa2a4895e1747e12b705d2d9969d20583c17d.jpg)  
Feel more confident
Employees who feel
confident working
with AI

![](images/41e74626dfd6d9c5d80768246b7a10c26706468504f49e0a115a61ea5cba9daa.jpg)  
- Respondents at companies that focus on Reshape or Invent initiatives

![](images/1f83b81843bedb29f9c717ebaeca72db0efb5e8043558648c593e5987bc8072d.jpg)

What makes
Reshape or Invent
initiatives more
successful: a clearer
roadmap and
deeper investment
in people

## Companies pursuing Reshape or Invent initiatives build a clearer roadmap...

## ... and invest in the people behind it

Sets the direction
Employees who say
AI strategy is clear

Defines the rules
Employees who see
adequate guardrails
in place

Puts agents to work
Employees who see
agents integrated
into workflows

Brings people in
Employees who
participate in
process redesign

![](images/65433209fedb6a9a1ee3ac6705e0b6f6dbee6eae34c3cecd19dd5d0c78e38085.jpg)  
Measures what matters
Employees who see AI value creation properly tracked  
Invests in skills
Employees who
experience a major
reskilling initiative  
■ Respondents at companies that focus on Reshape or Invent initiatives

Most respondents expect a need for upskilling in the next five years, yet only 36% feel properly trained

Demand for
upskilling is loud
and persistent.
The response still
falls short

![](images/18a4af00cd73ccd70fe75b5dd9d4bd133e7f47e4e15b497805d849b56db10acb.jpg)

88%

Of respondents believe
they need major upskilling
in the next five years

36%

![](images/222a586c58bbdeb22a50736581bef361e675bc9ca4648939f6c45a0a882104fe.jpg)  
Of respondents feel
properly trained

Sources: AI at Work, 2026 (n=11,749); BCG analysis.
Note: Share of respondents for both metrics is unchanged from 2025.

## No more “silicon ceiling”: frontline employees have integrated AI into their daily work

74% of frontline
employees now
describe themselves
as regular AI users,
driving overall
adoption

Regular AI use across worker levels  
![](images/f5b68110d4024fea299461304e83391545cd35ddf9f611f49fe0d5368a17d0f2.jpg)

India, the Middle East, and Australia lead adoption for frontline employees, while France, Italy, and US trail the average

Frontline employees who use AI at least several times a week, by market  
![](images/2c68dc6582e0c61b9fb306a922081758d0e5a9ea2703bbeb84c353af468fdffb.jpg)  
Sources: AI at Work, 2026 (n=4,040 frontline employees); BCG analysis.  
Note: Frontline employees = individual white-collar employees with no managerial responsibilities. Middle East includes UAE, Saudi Arabia, Kuwait, and Qatar. Benelux includes Belgium and the Netherlands. Nordics include Sweden, Denmark, Norway, and Finland.

Support functions lead adoption among frontline employees, while sales and operations lag behind

Frontline employees who use AI at least several times a week, by function  
![](images/8174931963a21d1ff42673ddd146b555bf0dea3ee04fc64f03c267e6d2f50ee0.jpg)  
Sources: AI at Work, 2026 (n=4,040 frontline employees); BCG analysis.  
Note: Frontline employees = individual white-collar employees with no managerial responsibilities.

## The real challenge is now organizational and managerial

AI is reshaping
work, impacting the
very nature of jobs
and management

Aspect of work that respondents say have been changed by AI  
![](images/2cd2a38b96a603f02b4bc6ea1a231ec991d450ed7386775e552e1449d08921ab.jpg)  
Sources: AI at Work, 2026 (n=11,749); BCG analysis.  
$^{1}$ Share of respondents who report AI will significantly or moderately change the expectation for the skills needed for the role.

## Business value and employee joy aren’t tradeoffs, they’re driven by the same forces

The “joy paradox” of AI: it makes work both better and harder

## More than two-thirds of regular AI users report an increase in job satisfaction...

Change in day-to-day work enjoyment and satisfaction since adopting AI

![](images/97cc48038fe8a02351222c1d4dc11f8110304edee706d13afad30b087a1fc051.jpg)  
... but 41% report increased mental strain associated with it  
Change in cognitive load since adopting AI

![](images/3f2e95e1fbcd2c88a8a9e24851f215557779dc90ccf8ae2831b1ad9d1a0a7dba.jpg)  
Sources: AI at Work, 2026 (n=9,923 regular AI users); BCG analysis.  
Note: Frontline employees = individual white-collar employees with no managerial responsibilities.

The actions that
drive business
impact are the same
ones that make
employees thrive

Top 5 organizational levers ranked by uplift across employee joy and measurable impact  
![](images/f7f9719c224e279a546865262c9e7cb375e36153fe4f9a5a19a2cbc2054d6e0f.jpg)  
Sources: AI at Work, 2026 (n=9,923 regular AI users); BCG analysis.
Note: Measurable impact = Improvement in key business metrics attributed to AI.

## Want the AI “honeymoon” to last? Strategic clarity beats tools in driving sustained impact

Strategic clarity
beats tools:
employees with clear
strategy but limited
access to tools
outperform those
with strong access
but no direction

## Respondents reporting measurable impact based on AI strategy clarity and availability of AI tools

Limited strategic clarity and limited access to tools

Limited strategic clarity and strong access to tools

Strong strategic clarity and limited access to tools

Strong strategic clarity and strong access to tools

![](images/3ca6a372b036ac461f3856228f9c86c4065ecfbfb55ea758ccd2e50d892f4fda.jpg)

Sources: AI at Work, 2026 (n=6,998 respondents who use AI regularly, less than 6 months vs more than a year); BCG analysis.
Note: +/-pp = the extra share of employees who enjoy work when a driver is present (+) or the share lost when a blocker is present (-).

## The drivers of joy at work when using AI evolve over time...

The AI “honeymoon”? At first employees enjoy the cognitive load, but strategic clarity is the unlock to sustaining joy over time

Regular AI users for less than 6 months

Regular AI users for more than a year

Cognitive load

+43pp

+30pp

Clear AI strategy

Clear AI strategy

+24pp

Clear guidance on saved time

+23pp

Clear guidance on saved time

+25pp

Cognitive load

+21pp

## ...the drivers of toil do not

Regular AI users for less than 6 months

Difficulty showing unique value

-29pp

Regular AI users for more than a year

Difficulty showing unique value

-26pp

Inadequate training

-15pp

Inadequate training

-16pp

## AI agents have evolved from concept to reality, but operating models haven’t caught up

86%

More people are
aware of AI agents
and see their
importance, but few
understand what
they are: a sign for
leaders to make a
better case for what
they can do

Respondents who have heard about AI agents

![](images/2553e8d647adb7a0909c6f7d317709b4469b5f709df1b6fbb17e06e7d5a454a9.jpg)

Respondents who have a limited understanding of what AI agents are

![](images/7e7778420dc223504bc097e44959e8fa229c616047c0559c089864a2cf95443c.jpg)  
Sources: AI at Work, 2026 (n=11,749); BCG analysis.
Note: Frontline employees = individual white-collar employees with no managerial responsibilities.  
Respondents who think AI agents will be important in the next 2 to 3 years

![](images/3118fc9b062c1976c8e5ae3deb1314a865f9d7ce79e650ba376f1dbf04cea2be.jpg)

More than double the organizations from 2025 have integrated AI agents into workflows, with meaningful impacts expected at the managerial level

Respondents reporting measurable impact based on AI strategy clarity and availability of AI tools

AI agent use by type

![](images/0680fe6e6e862f1774fd7347232770a9baed610ae58d272c7d6389cd250f00f5.jpg)

Most people believe agents could do at least half their job in the future, and managers and leaders expect the biggest shift

Respondents who think that in the next three years AI agents could perform at least half of their job

![](images/4c25c38b79caa8be052ea4d0c3bb3c34c5e2aedfded6d1eb0279aefa9a9527c4.jpg)  
Sources: AI at Work, 2026 (n=9,923 regular AI users); BCG analysis.
Note: Frontline employees = individual white-collar employees with no managerial responsibilities.

The missing piece: operating models haven’t caught up with AI agents’ deployment

Half of employees lack clear governance for managing human × AI teams: frontline employees and managers feel it the most

Respondents who say their company has not put in place clear guidance on managing human × AI teams

![](images/ba5da8981125f58da0e55135b5550dedc6c74e28fb394f1f67418fd3ca970efb.jpg)

Accountability is a universal concern, equally shared across all levels
Respondents who rank AI-driven accountability as a top 3 concern in the next 2 to 3 years

![](images/dc29b841df874e9788f0f4d9d54da1e2fbee3d2ceb17aa5cb001a19193e21978.jpg)  
Sources: AI at Work, 2026 (n=8,849 respondents who have heard of AI agents and regular AI users); BCG analysis.
Notes: Frontline employees = individual white-collar employees with no managerial responsibilities.

![](images/c62d54599d276da8bce7e48c8b7d7ca749852cc7c50611d919ff5a865a80bc37.jpg)

## Five CEO imperatives

1

Make strategic clarity your top priority, and own it personally

Change the scoreboard: measure value, not adoption

3

Invest in redesigning work end-to-end, not in more tools

4

Put people at the heart of that redesign

![](images/dd72ac8e5258c200b09d5cc9c154bc6928e1972c31cb2279474578502f17790c.jpg)

Govern it as a
moving target, not a
one-off program

Strategic clarity is not a communications task, it’s a leadership posture. Set AI as an explicit top priority, be clear about where the company is heading, and make sure everyone gets it, the frontline included. CEOs who personally own the transformation outperform on every dimension: value captured, employee joy, and trust.

Adoption tells you that people use AI, not whether it pays off. The time that individuals save leaks out of the organization unless it is tracked and deliberately reinvested. So, watch business outcomes rather than usage.

Most companies still treat AI as a tool for individual productivity, but the more important change is a collective one: AI is reshaping how teams work together and how tasks flow across the organization. Capturing that value means redesigning a few core processes from end-to-end.

The redesign only works if people are in it. Look ahead at how roles will shift over the next few years, train for the skills that matter most, and bring people into shaping the change rather than presenting it to them. What keeps people engaged is knowing how AI helps them grow, not how much faster they work.

Technology moves faster than any company can. Treat AI as something you keep steering, not a program with a finish line. Put a light, standing governance in place that rechecks what works, remeasures the value, and adjusts as the models and agents evolve.

## BCG X | BCG

bcg.com
"""
