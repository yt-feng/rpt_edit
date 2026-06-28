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

BCG AI RADAR 2026

## As AI Investments Surge, CEOs Take the Lead

## Survey methodology

2,360

![](images/996d1d6e3f70e586f1db0f16b62887db765ef6819c45e449fc78ca7aeda1ba92.jpg)

![](images/290a4efead4a59cb815c0c1348397242de9201043e1f0120406ebd2bdddb38d2.jpg)  
Sources: BCG AI Radar Survey 2026 (n = 2,360); BCG analysis. $^{1}$ Executives who directly report to C-suite (EVP, SVP, VP, etc.).

![](images/d559650cd740b4ce24345be1e981ba2c1f7c79ff48cc4631e8347f8b6899147f.jpg)  
Markets (number of respondents)

![](images/5b35e1b667a212344af2368f2275ee59a684594f4c94e8eb99bbbd47eeb1fbc3.jpg)

## Key takeaways

1

Corporate investments in AI have doubled since last year and are here to stay

94%

of CEOs say they will continue to invest even if it does not pay off in 2026

2

AI corporate transformation is moving from a CIO-led to a CEO-led initiative

72%

of CEOs say they are the main decision maker on AI in their organization

3

Three CEO archetypes emerge with Trailblazer CEOs leading end-to-end AI transformation

60%

of Trailblazers' AI budget will be spent on agentic AI

## Takeaway 1

Corporate investments in AI have doubled since last year and are here to stay

## 94%

of organizations
will continue their
investments even
if they do not pay
off in 2026

Only 6% of companies plan to pull back AI investments if current initiatives fall short

![](images/cacfe21f226515f8e92e3a97fc613737182578d868e94d5a1d10535649739312.jpg)  
Sources: BCG AI Radar 2026 Survey (n = 2,360); BCG analysis.  
Note: AI investments refer to all investments needed to realize the benefits from AI including but not limited to technology and infrastructure, data and architecture enablement, talent and upskilling, external partners, etc.  
Question: “What is the plan if your organization’s AI investments do not produce the desired financial impact in the next 12 months?”

Investment in AI as share of an organization’s revenue $(\%)$ 1

Investments in
AI is projected to
double in 2026

![](images/7940b0ca047fac9f8bd2909f057e3debee8f699a8f4c34df07830611de582416.jpg)  
Note: AI investments refer to all investments needed to realize the benefits from AI including but not limited to technology and infrastructure, data and architecture enablement, talent and upskilling, external partners, etc.  
Questions: “How much do you expect your organization to invest in AI in 2026?”, “What is the annual revenue range of your company or organization globally?” $^{1}$ The average base revenue of the underlying companies has remained almost the same.

INVESTMENT IN AI AS SHARE OF ANNUAL REVENUE

## All industries plan to increase their AI investments in 2026

![](images/723bd3f036b850659d3e77bd31c321470878b7a0811eb496f2162f5bf4306ca9.jpg)  
Sources: BCG AI Radar 2026 Survey (n = 2,308 due to exclusion of “I don’t know” and blank responses); BCG analysis.  
Note: Consumer combines consumer/retail and travel/tourism industries. Public sector combines government/public sector and education industries. Communication services combines advertising/marketing, media, and telecom industries. Industrials and real estate combines manufacturing, industrial goods, automotive, transportation, agriculture, and real estate industries.  
Question: "How much do you expect your organization to invest in AI in 2026?"

<table><tr><td rowspan="9">Data privacy and cybersecurity remain the primary concern</td><td colspan="2">Top three AI concerns remain the same, but their share is declining</td></tr><tr><td>Share of respondents</td><td>Change vs. 2025</td></tr><tr><td>Data privacy and cybersecurity risks</td><td>-12pp</td></tr><tr><td>Lack of control or understanding of AI decisions</td><td>-7pp</td></tr><tr><td>Regulatory or compliance challenges</td><td>-5pp</td></tr><tr><td colspan="2">And a few other concerns have become more prominent</td></tr><tr><td>Technological failure</td><td>+6pp</td></tr><tr><td>Environmental impact of AI</td><td>+10pp</td></tr><tr><td>Geopolitical instability</td><td>+8pp</td></tr></table>

Sources: BCG AI Radar 2026 Survey (n = 2,360), BCG AI Radar 2025 Survey (n = 1,803); BCG analysis. Question: “What are the top three risks you are most concerned about when it comes to AI?”

## Agentic AI introduces both opportunity and risk in cybersecurity

9% of leaders view cybersecurity as the biggest threat from agentic AI

32% of leaders view cybersecurity as the biggest opportunity of agentic AI

## Automation

Scale

System access

New targets

Can search for weaknesses and break without rest

Learning

Can send many fake messages and frauds to many users

If taken over, can change settings, move data, or turn off protection

AI systems can be hacked

Can learn which attacks work and keep improving them

Can watch systems continuously and react to problems quickly

59%

Can check huge amounts of logs/alerts that humans would miss

Can repeatedly follow security steps quickly and correctly

of leaders view it
as both a threat and
an opportunity

Can regularly check accounts, passwords, and settings for issues

Can learn which attacks appear and keep improving defense

## Takeaway 2

## AI corporate transformation is moving from a CIO-led to a CEO-led initiative

72%

of CEOs say they are the main decision maker on AI in their organization

2x last year

## 82%

## are more optimistic about AI's potential for ROI this year than last year

## Half of CEOs surveyed believe their job stability depends on getting AI strategy right

50%

## CEOs show stronger conviction in AI than their executive counterparts

Expect major role disruption in the organization by 2030 $^{6}$

![](images/03343bdbaa7fb5dccedb0845247607e532feed0cd6eeeab82c9aeaa167f2e783.jpg)  
Sources: BCG AI Radar 2026 Survey (n = 2,360); BCG analysis.  
$^{1}$ Includes Chief Data Officer, Chief Digital Officer, Chief AI Officer, and Chief Analytics Officer. $^{2}$ Includes Chief Financial Officer, Chief Strategy Officer, and other C-suite roles who report to the CEO. $^{3}$ Includes VP-level roles reporting into CXOs. $^{4}$ “How confident are you in your ability to lead your organization through an AI transformation that will deliver a positive return on investment?”, Replies for “Very confident.” $^{5}$ “Which of the following best reflects how you feel about investing in AI?”, Replies for “Confident AI will pay off.” $^{6}$ “To what extent do you agree with the following: By 2030, more than half the roles in your organization, including the C-suite, will be gone or transformed by AI.”

CEOs in the
East are more
confident AI
will pay off

Sources: BCG AI Radar 2026 Survey (n = 640 for CEOs); BCG analysis.

Question: “Which of the following best reflects how you feel about investing in AI?”, Replies “Confident that AI will pay off.”

$^{1}$ Greater China includes mainland China, Hong Kong, and Taiwan. $^{2}$ Middle East and Africa includes Morocco, Qatar, Saudi Arabia, South Africa, and the UAE. $^{3}$ Europe includes France, Germany, Italy, and Spain.

Global East
SHARE OF CEOS CONFIDENT THAT AI WILL PAY OFF

![](images/3f051ade33b3d1a651c5694939ec61d3ac0ea4c057fe67506124c4cfcbf8b0ac.jpg)  
Global West
SHARE OF CEOS CONFIDENT THAT AI WILL PAY OFF

![](images/55c9e7475dc5e533b3c4c56a3f940401cf0a476f6f33f0e6296bc39646dc0349.jpg)

## CEOs in Asia express confidence, while those in the West feel pressure

![](images/5002a345b02b397b70c56309b1c67b34dc06f88599cf05c1f63028b136c64d92.jpg)  
Sources: BCG AI Radar 2026 Survey (n = 640 for CEOs); BCG analysis.  
Question: “Which of the following best reflects how you feel about investing in AI?”, Replies “Confident that AI will pay off” and “Pressured to act or risk falling behind.”  
$^{1}$ Europe includes France, Germany, Italy, and Spain. $^{2}$ Middle East and Africa includes Morocco, Qatar, Saudi Arabia, South Africa, and the UAE. $^{3}$ Greater China includes mainland China, Hong Kong, and Taiwan.

\~90%

of CEOs believe AI agents will enable their organizations to report measurable ROI in 2026

# CEOs have committed >30%

of their organization's AI investment for 2026 to agentic AI

## Agentic AI is taking on multiple roles, changing how companies organize work

"To what extent do AI applications occupy the following roles for people in your functional area?"

SHARE OF ORGANIZATIONS

![](images/8a4d267eb2965a180b4d9685c9047da66e040a3d1fd32d9d4d119d3d7fda86e1.jpg)  
Sources: BCG-MIT Sloan Management Review report, 2025 (n = 2,102); BCG analysis.  
Note: Respondents who answered “strongly agree” or “agree” to the question.

AI systems work
independently from
humans

![](images/73cfc4d390208ecc86f16ae13fe0c490867a08ad63f0584268fbc9b33be06349.jpg)

## As AI systems increasingly gain autonomy, leaders must develop adaptable governance structures

58%

of leading
organizations
expect a change in
governance and
decision rights due
to AI

"To what extent do you agree with the following statements about your organization?"

AI systems work
with ambiguous
inputs

## 90% of CEOs believe that by 2028 AI will significantly transform what success looks like

Staying competitive

Building competitive advantage

![](images/327d2c869fcee515de6eb7ded117f65cf33c5ec926c8730449dbeb182c12f9dd.jpg)

Deploy AI in
everyday tasks

![](images/38cdfa23d9a18b16f51a1e1735f762a8a6f6485bc0708d855098ebfb6221380f.jpg)

Reshape critical
workflows and
functions

![](images/ecc5ef8f1ca09f5931e7c6a2fb47d2084d4c136f7f2a7c08bd654b6470edf34f.jpg)

Invent new business
models and revenue
streams

## Takeaway 3

## Three CEO archetypes emerge with Trailblazer CEOs leading end-to-end AI transformation

## Three CEO archetypes emerge from the survey data $^{1}$

![](images/b62b52a603fd4f3233c406a8710a11014b1c92fa3df4fbedc284b85cccbed9d3.jpg)  
Sources: BCG AI Radar 2026 Survey (n = 640 for CEOs); BCG analysis.  
$^{1}$ K-means clustering analysis reveals the five key variables that differentiate CEOs. These variables are used to define the three CEO archetypes. $^{2}$ Investments in AI as a part of the organization's transformational budget in 2026. $^{3}$ Includes all forms of engagement, not just formal training but also discussions, briefings, demos, and direct exploration of tools.

## Trailblazers emerge, but nearly all CEOs are focused on AI

![](images/b335a7ecb80df396a99b97d3acb5908ec5f8a1ec6ef269a431b3d4d96769b94a.jpg)

## \~15% Followers

Recognize AI's potential but lack full conviction, making some early, cautious investments

Are excited and confident about AI but only invest when they see evident value and low risk

## \~15% Trailblazers

Drive AI-powered transformation through decisive investment, rapid upskilling, and strong belief in AI's ROI

Increasing levels of confidence, investments, workforce upskilling, pressure to deliver, and excitement/preparedness

![](images/178d221d7414a4f511cca79412a15fb14b15e30a8dda71fa7cc948535ef196a9.jpg)

Trailblazer CEOs create a positive flywheel by prioritizing, investing, and upskilling the organization in AI

## 1. Make AI and agentic AI a top priority

Having “accelerate AI” as their top priority

## 5. Track measurable ROI from AI

Feeling “very confident” their AI strategy will pay off

## 2. Deepen AI literacy

Spending more than six hours a week expanding their expertise on AI

![](images/588720dbc95b15a6aaf54f4ed97669851613af9ae599155a5105f685e140d5a5.jpg)

## 3. Invest capital at scale

Investing more than \$50M in AI in 2026

## 4. Upskill their organization

Upskilling more than half of their workforce

![](images/c6045350a030c48bf0d37813f8e520c17f98161b89276f7a62bb01ff109a6923.jpg)

## "End-to-end AI transformation is one of our greatest opportunities to succeed with AI agents in the next 12 months"

SHARE OF RESPONSES FROM CEOS THAT AGREE

## Trailblazer CEOs are twice as likely to apply agentic AI end-to-end

![](images/7f8a9db6b7e836505635309f57ffb633428241f9945f291a75f858fa60d3fec6.jpg)  
Followers  
Pragmatists  
Trailblazers

Trailblazer CEOs
see value in AI
agents and invest
significantly

![](images/52b9720e98a1291e1b132cd78d46d935e11dd9aeead27677098d28c0f1b5108e.jpg)

Trailblazers

![](images/4c3410c286aab68aed4c3a64a0afa2776fa77bcba4e3b0ae4b8faee2ab2b1534.jpg)  
Pragmatists

\~60%

of their AI budget is currently being spent on agentic AI

![](images/236177f85bdd7802389cd25e5a59248f4ff1cd94379a196b561c486b244d0a12.jpg)

![](images/2a3c99807504f189ad4b4bb75040d206599ae3ec09f78ec341ed67cc6a2f6c93.jpg)  
Followers

![](images/e9858e60542f3eb4082540758ae408d0d70d902cded9a4a4f0ac79d71636bebf.jpg)

## Trailblazers invest twice as much in upskilling their workforce

![](images/33746d6ae1735f70feb880fb9462d21c6461e217018efbaad49f1e17e99c5e37.jpg)

\~60%

of their organization's AI budget is allocated to upskilling and retraining current workforce on $\mathsf{AI}^1$

\~70%

of their workforce has been upskilled/reskilled on AI $^{2}$

VS

27%

![](images/39563ae080d81301794ffa9f5305006f0ef498dce02c67551df23080fcb7180a.jpg)

Pragmatists

![](images/6835a7885e26ef29a232ecb3b74cde7fc00b1330019b694f794caec4904b76c8.jpg)

24%

Followers

![](images/40730ddc1a851e40a5dae8c5a011157ec893afa3947bb014f5d5e85fb4aa3a45.jpg)

41%

Pragmatists

![](images/8c8e61b60901114c010f2d5e0227c60842f995040a60a8f0cf2eea4945ddceef.jpg)

35%

Followers

Sources: BCG AI Radar 2026 Survey (n = 640 for CEOs); BCG analysis.

$^{1}$ “Approximately what percent of your overall AI budget is being allocated to upskill and retrain your current workforce on AI?” $^{2}$ “What share of your workforce has been upskilled/reskilled for AI?”

## Trailblazers see significant impact and returns from their investments in AI

![](images/1c6168caf704de1ab57129ccb1d27ccec7c5ff8c17a64916fd9c586493657bb7.jpg)

![](images/d2669de467b3ea0cf0e85832f425b150a97eb47f62d1f7e3f480c79af2223d3e.jpg)

## Foxconn

Over \$400M targeted savings identified from a scalable AI operating model and AI platform deployed across more than 200 factories

## Reckitt

Quality output doubled through an end-to-end AI-driven workflow reinvention in marketing, cutting routine activities by up to 90%

## CEOs must act decisively to execute their AI agenda

1. Make AI your key priority
Position the organization to be the disruptor, not the disrupted.

5. Track measurable ROI from AI
Track AI's impact to drive sustainable ROI over time.

2. Deepen AI literacy
Expand individual AI fluency to effectively lead transformations.

3. Commit investments at scale
Invest decisively across end-to-end
business functions.

4. Upskill the organization
Upskill the workforce to optimize productivity, creativity, and judgment.

## In summary

Corporate investment in AI is here to stay...

94%

will continue to invest
even if it does not pay off
in 2026

1.7%

of an organization's revenue is dedicated to AI investment

2x

increase in projected AI investments from 2025

AI transformation is moving from a CIO-led initiative to a CEO-led strategy...

72%

of CEOs say they are the main decision maker on AI, 2x last year

50%

of CEOs believe their job depends on getting AI right

90%

of CEOs believe AI agents will enable their companies to see measurable ROI this year
"""
