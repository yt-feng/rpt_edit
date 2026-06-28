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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
People & Organizational Performance Practice

# HR Monitor 2026

A comprehensive benchmark survey of workforce and HR trends across Europe, the United States, and China delivers critical insights for today's HR leaders.

June 2026

## HR Monitor 2026

June 2026

This report is a collaborative effort by Julian Kirchherr, Karel Eloot, Sandra Durth, Ulf Schrader and Vincent Bérubé, with Charlotte Seiler, Kira Rupietta, Kristina Störk, Marlene Senst, Séverine Fobe, and Simon Gallot Lavallée, representing views from McKinsey's People & Organizational Performance Practice.

## Contents

INTRODUCTION

![](images/716272e8c332e86b994e15df2d12296c92a5b2d00dc1778c822f196121f04a8e.jpg)

CHAPTER 1

![](images/70e5863b6aacfbab64e08efd6a8fcc12ca693f3cf397a6de25a62e4e61783f0a.jpg)

CHAPTER 2

CHAPTER 3

![](images/551f122fff0f227e739919705161251827e9cbf4e486f095c117ab65fac8e7f6.jpg)

CHAPTER 4

![](images/bf9c210255a323889c8fc49a09d0c7267651264f4f2bfa71b3fa86bfa22d666d.jpg)

CHAPTER 5

![](images/19a063539df824cc06872d308c5efccd99d6437de43db11f020e3b1571e91ad4.jpg)

## 3 Preface

![](images/240deaa751c0d0924d25fb27778d7959a37959e375d5c3ffa95a3540d60587e8.jpg)

4 HR at a turning point: From functional excellence to system-level transformation
6 Strategic workforce planning in the age of human-AI collaboration
11 Talent acquisition: Enhancing hiring effectiveness as labor markets steady
18 Employee development: Preparing workers for rapidly evolving skill and AI requirements
23 A cautious workforce: Insights into employee experience and retention
31 HR's operating model: Rewiring the people function in the age of AI
39 Conclusion
40 Appendix
42 About the authors

## Preface

As AI transforms how work gets done, the people function is more important than ever. The workforce is undergoing fundamental change as roles and skill requirements shift and new forms of human–machine collaboration emerge. HR is taking on a new dual role: It serves as an architect of AI transformation, shaping how work, roles, and capabilities evolve, and as a “lighthouse,” leading by example in reimagining its own operating model and demonstrating how to embed AI into core processes.

In this environment, chief human resource officers (CHROs) and other HR leaders need a sharper understanding of where the function stands today and how it needs to advance. We have expanded our HR Monitor report to provide leaders with richer data to benchmark their people function against peers, evaluate progress, and identify key areas for action.

Our inaugural report in 2024 focused on Germany's HR landscape. Last year, we highlighted workforce and HR trends across Europe. This year, we surveyed approximately 1,300 HR professionals and 5,500 employees across ten countries, with a primary focus on Europe (Belgium, France, Germany, Italy, Netherlands, Poland, Spain, and the United Kingdom), complemented by comparative data from the United States and China. The data was collected in January 2026, spans multiple industries, and is complemented by insights drawn from discussions with HR leaders and experts across McKinsey's People & Organizational Performance Practice. The result is a robust data set enabling cross-country, cross-industry, and year-over-year comparisons. (Note: Year-over-year differences in survey results should be interpreted as directional only, as country coverage changed slightly compared to 2025, with the addition of China, the Netherlands, and Belgium.)

This year's report explores what HR delivers—covering core dimensions such as workforce planning, talent acquisition, learning and development, and employee experience—and how HR generates value, including the impact of digital technologies and AI. Additionally, it compares HR's own assessment with employees' experiences to highlight potential perceptual gaps. In each chapter, we will highlight the key themes emerging from our survey data, along with recommendations for leaders.

Thank you for your interest in the HR Monitor. We look forward to further refining and expanding this benchmark in the coming years.

![](images/da6f822609ed892c58fe78da9b121dcdff8442fe64486bfa5c10914b75147d0e.jpg)  
Julian Kirchherr
Partner, Berlin

![](images/7e77ff86216d150743019a3ce4859f15945a3b9f288151895f3fc870eeff98f7.jpg)  
Kristina Störk
Associate Partner, Munich

![](images/a3e7b4bf780c3e3a5cb5b619f57d7ea93ec8007023b6d764a4eee1419733aef6.jpg)  
Vincent Bérubé
Senior Partner, Montréal

![](images/5f7edb9cfca27443caf5368678e44e94bd2f900de23aa91a224b0f58216a1621.jpg)  
Introduction

# HR at a turning point: From functional excellence to system-level transformation

Economic pressures, AI disruptions, and shifting workforce expectations are redefining effective people management. While many HR functions have strengthened processes in recent years, our data reveal a need for broader progress. Structural gaps persist between operational planning and strategic foresight, training and skills growth, employee expectations and organizational responses, and AI experimentation and scaled impact.

Based on our survey data, this year's HR Monitor identifies five priority changes that leaders will need to embrace in the age of human–AI collaboration:

— Workforce planning must move beyond operational capacity planning to strategic capability planning. Automation and AI are rapidly reshaping how work gets done and which skills are required. Yet, workforce planning remains predominantly focused on short-term headcount planning, with only 11 percent of organizations adopting a long-term perspective. At the same time, skills gaps persist and demand is shifting toward more people-centered and AI-related capabilities as the need for routine task-based skills declines. Organizations must evolve toward forward-looking, task- and capability-based planning or risk underestimating the scale of the workforce transformation ahead.

# Automation and AI are rapidly reshaping how work gets done and which skills are required.

— In employer-driven labor markets, recruiting is becoming less critical but hiring effectiveness remains essential. Global labor markets have largely steadied, with offer acceptance rates up three percentage points and overall hiring success up four percentage points. While the market continues to favor employers, they still need to make hiring practices more efficient. Companies may need to process higher application volumes per vacancy, requiring greater screening and coordination effort. At the same time, long hiring cycles persist, raising the risk of losing top candidates. AI has substantial potential to increase hiring speed and improve candidate experience, but it must be integrated into disciplined, well-designed processes instead of being layered onto existing complex approaches.

— Performance management and employee development are back on leaders' agendas, but remain fragmented in execution. Many organizations are placing renewed emphasis on measurable performance and systematic capability building. However, this ambition is not yet reflected in practice. Learning participation remains limited, with 24 percent of employees reporting no training participation at all. Feedback cycles are infrequent, with more than half of employees receiving feedback once per year or not at all. HR professionals tend to overestimate both participation in training and the importance that employees assign to development opportunities. Companies need to treat performance management as a core driver of employee development and improve measurement of skill building to better prepare their workforce for the future.

— Amid economic instability, labor market mobility is declining and compensation is a top concern for employees. In an environment of macroeconomic uncertainty, employee mobility is declining. Voluntary attrition is down two percentage points year over year, even as employee satisfaction levels remain broadly stable. At the same time, employees' decisions to stay at their jobs are increasingly driven by tangible factors: compensation (52 percent), work–life balance (46 percent), and job security (45 percent). While compensation has become a central concern for employees amid pressure on real incomes, companies are only partially addressing the issue. Employer-driven labor markets reduce external opportunities and, in turn, the pressure on organizations to adjust. Against this backdrop, improving employee experience is less about rolling out additional programs and more about reinforcing fairness, transparency, and sustainable workload models.

— Agentic HR operating models are emerging, but large-scale AI adoption remains limited. The traditional Ulrich model is gradually giving way to more agile and technology-enabled configurations, but most organizations remain in a hybrid transition. Although automation models suggest substantial AI potential across HR, adoption is progressing slowly (with zero- to six-percentage-point increases in operational use, depending on the domain). Many organizations remain in pilot mode, with deployments largely concentrated in administrative areas. The fragmented technology landscape and limited capability building continue to constrain companies' ability to scale their AI adoption. Unlocking AI's full value will require HR to redesign its operating model around flow-to-work principles, establish a unified data backbone, and move decisively from experimentation to enterprise-wide transformation.

![](images/6ad9ec92c577fdbbe21c62f261cf86ef59848ccc4b5e99f3f8c647db3a6af2d1.jpg)

## Strategic workforce planning in the age of human-AI collaboration

Advances in AI are expected to substantially shift how and where skills are applied as work evolves into a partnership between people and agents, combining human judgment with the power of automation. If AI is adopted at a moderate pace through 2030, up to 30 percent of current work hours in Europe and the United States could be automated, according to a McKinsey Global Institute (MGI) analysis. $^{1}$ MGI projects that over the same period, more than 70 percent of today's skills are expected to remain relevant and could be applied in both automatable and non-automatable work. But this does not mean roles themselves will remain unchanged. Nearly every occupation will experience skill shifts by 2030, as tasks are reallocated between humans and intelligent systems. $^{2}$

In periods of rapid technological change, the organizations best positioned to respond are those that treat talent with the same strategic rigor as financial capital. S&P 500 companies that excel at maximizing their return on talent generate 300 percent more revenue per employee compared with the median firm. $^{3}$ In many cases, these top performers use strategic workforce planning to stay ahead, taking a three-to-five-year view and anticipating multiple scenarios so that they have the right number of people with the right skills at the right time.

Yet, the uncertainty introduced by gen AI makes this forward-looking view harder and more critical than ever. Gen AI is not just another technological advancement affecting specific tasks; it is a catalyst for organizations to rewire how they operate and generate value, fundamentally altering the ratio of humans to technology. Strategic workforce planning provides the analytical foundation to model these shifts explicitly, helping organizations move from reactive headcount adjustments to capability- and scenario-based workforce decisions. This enables organizations to anticipate future workforce needs under different adoption trajectories for AI, identify emerging skills gaps, and implement targeted reskilling and upskilling measures to ensure long-term workforce readiness.

Here we highlight key themes related to workforce planning emerging from the HR Monitor survey data.

## Skills gaps persist but vary across industries

According to surveyed HR professionals, 23 percent of employees lack at least some of the skills required to perform in their current role, down nine percentage points from last year. At the same time, 22 percent of employees indicate that they doubt they will have the skills needed to remain in their role over the next five years, down six percentage points from 2025.

HR professionals in Italy report the highest current skills gap (28 percent), while Poland reports the lowest (23 percent). At the industry level, the highest current skills gaps are reported in chemicals (30 percent); the public and social sector, and electronics (28 percent); and tourism and food services, and semiconductors (27 percent). The lowest skills gaps are reported in mechanics (16 percent); travel, logistics, and transport (18 percent); and real estate (19 percent). These figures suggest that HR professionals are underestimating the extent of future skill changes, as MGI research projects that nearly every occupation will experience skill shifts in the next few years.

## Important future skills are shifting

Problem-solving remains the most frequently cited future skill, with 44 percent of HR professionals ranking it in their top five this year (Exhibit 1). Creativity is cited second most often, whereas last year it was the fifth most cited. Data analytics and AI remains one of the top three most-cited skill areas.

By contrast, a decline in the importance of software development and other highly specialized technical execution skills reflects that AI systems increasingly take over those tasks. At the same time, skills necessary to guide, interpret, and apply AI outputs are gaining prominence. Digital literacy is the fastest-rising skill, cited sixth this year after ranking 20th in 2025. Ability to reason rose to ninth place after ranking 12th last year.

## Exhibit 1

Future skills will shift from routine task-based capabilities to skills focused on analyzing and interpreting AI outputs.

Top future skills according to HR professionals, 2025–26, % of respondents (who mentioned the skill among their top 5)

![](images/e42b263a493d31c2ca322db6a2e639d0f34a489958529538f04f27a66789f570.jpg)

Note: Year-over-year differences should be interpreted as directional only, as country coverage changed slightly compared with 2025, with the addition of Belgium, China, and the Netherlands. Source: McKinsey HR Monitor Survey, Jan 2026, n = 1,303 HR professionals in Belgium, China, France, Germany, Italy, Netherlands, Poland, Spain, UK, and US; McKinsey HR Monitor Survey, Dec 2024, n = 1,925 HR professionals in France, Germany, Italy, Poland, Spain, UK, and US.

Most companies conduct operational workforce planning, but only 11 percent take a strategic, long-term approach.

These shifts illustrate the need for skills intelligence: the ability to systematically capture, analyze, and forecast skill supply and demand across the organization. Without a granular, continuously updated understanding of which skills the organization holds and which are emerging as critical, workforce planning cannot keep pace with the rate at which AI is reshaping task structures. Organizations that build robust skills intelligence—combining comprehensive skills taxonomies with AI-powered analytics—can detect these compositional shifts early, identify skill adjacencies that enable talent to be redeployed, and translate emerging requirements into targeted workforce interventions. Strategic workforce planning, underpinned by skills intelligence, provides the foundation to systematically assess future skill needs and define the workforce required to meet long-term business objectives.

## Workforce planning remains predominantly short term and operational

On average, 62 percent of HR professionals indicate that their companies conduct organization-wide workforce planning, while 34 percent apply it to at least part of their workforce. However, only 11 percent conduct strategic workforce planning, defined as forecasting workforce needs three years or more into the future, while nearly two-thirds focus on a planning horizon of up to 12 months (Exhibit 2).

## Exhibit 2

Engagement in workforce planning, $^{1}$ % of respondents

![](images/a81373acb4c122ff45474125904d0645491e02e88401203f07d445be3d1cdbcb.jpg)  
How far in advance companies typically forecast workforce needs, $^{4}$ % of respondents

![](images/7c47f9dea55e0cb8f3f1a0e233238592bfe1c77fd37ff09bb114181b576ffc9e.jpg)  
Note: Figures may not sum to 100%, because of rounding.  
$^{1}$ Question: Does your company carry out strategic personnel planning?  
$^{2}$ Including demand and supply side, regularly updated data.  
$^{3}$ Not all roles are tracked; data is not always up to date.  
$^{4}$ Question: How far in advance does your company typically forecast workforce needs?  
Source: McKinsey HR Monitor Survey, Jan 2026, n = 1,303 HR professionals: Belgium, n = 101; China, n = 131; France, n = 142; Germany, n = 145; Italy, n = 142; Netherlands, n = 100; Poland, n = 130; Spain, n = 130; UK, n = 141; US, n = 141

Industries reporting the highest skills gaps—for example, chemicals and the public and social sector—are less engaged in organization-wide workforce planning (47 percent and 45 percent, respectively, compared with the cross-industry average of 62 percent). If these industries do not increase organization-wide workforce planning, they risk falling further behind and experiencing widening skills gaps.

In addition, 85 percent of organizations report having a skills taxonomy in place, up from 78 percent in 2025. However, only 57 percent combine organization-wide workforce planning with comprehensive skills documentation. This indicates that many organizations do not yet use skills taxonomies to inform workforce planning—missing an opportunity to identify skill adjacencies that enable faster internal redeployment and to use granular people data to make more informed, evidence-based talent decisions.

Forecasting practices further illustrate the dominant planning logic: 46 percent plan at the level of specific roles or positions, roughly one-third at the level of job families, and only 22 percent apply a skill-based forecasting approach. Given the increasing importance of task-level transformation and evolving skill requirements, even skill-based approaches may not be sufficient. At the same time, the pace and uncertainty of AI adoption make point forecasts increasingly unreliable because the range of plausible workforce scenarios is wider than ever. This makes it critical for organizations to adopt scenario-based planning, modeling different trajectories for how AI reshapes activities and capacity needs.

## Workforce planning recommendations for leaders

As change accelerate

[中间内容因长度限制已省略]

ogists are flexibly deployed to strategic priorities through flow-to-work pools.

— Invest in a unified technology and data backbone. Build a harmonized HR technology architecture that integrates fragmented systems and enables clean, interoperable, and accessible data across the employee life cycle. A robust digital and governance foundation is the prerequisite for comprehensive self-service, responsible AI deployment, and a scalable, intelligent EX layer.

— Build data and AI capabilities within HR. Systematically strengthen AI and data expertise within HR to keep pace with technology change and the function's evolving role. Provide targeted reskilling and upskilling for existing staff, and hire for new talent profiles, to move from the current low baseline to a substantially higher share of HR professionals with relevant tech skills.

— Move fast and scale AI rapidly. Shift from fragmented experimentation to systematic scaling of proven use cases, extending toward an end-to-end process redesign. In a rapidly evolving technology landscape, organizations can no longer afford prolonged pilot phases; they must transition swiftly from validation to enterprise-wide deployment.

![](images/393ab4ee80241d8c187f8f3412a1bf07e88472656141e29296e2a7669a70f0b5.jpg)

Conclusion

The HR function stands at a defining moment. The shift toward AI-enabled, agentic organizations represents the greatest opportunity the function has had in decades, but also one of its most demanding challenges. The scope of change is substantial, requiring HR to rethink how work is structured, how capabilities are built, and how value is delivered across the enterprise.

From here, two paths emerge. In one scenario, the growing complexity and technological developments outpace the function's ability to respond, leading to an increasing share of HR responsibilities being absorbed by IT or other digital functions. In the other, HR rises to the challenge, stepping into a leadership role in shaping the future of work, potentially in close integration or even merging with technology functions, but with a clear mandate for the people function to define how human and agentic workforces operate together.

Which path organizations take will depend on their ability to build a fact-based view of their maturity and performance and translate it into clear priorities for transformation. The HR Monitor supports HR leaders in assessing their current position, identifying gaps, and defining targeted actions to inform their strategies and turn ambition into execution.

# The shift toward AI-enabled, agentic organizations represents the greatest opportunity the HR function has had in decades.

Appendix

## Methodology of the HR Monitor 2026 Survey

This report is based on the HR Monitor 2026 HR Professionals Survey and the HR Monitor 2026 Employee Survey. Both surveys were conducted in January 2026. Survey respondents spanned ten countries: Belgium, China, France, Germany, Italy, Netherlands, Spain, Poland, the United Kingdom, and the United States.

## HR Professionals Survey

Respondents were more than 1,300 managers who are (co-)decision-makers for human resources topics at organizations with at least 100 employees. Participants spanned ten countries and represented companies from more than 18 industries. We asked HR leaders about efficiency and effectiveness indicators of their own HR functions, spanning core HR dimensions (strategic workforce planning, talent acquisition, learning and development, and HR operating model).

Countries represented in survey:

— Germany: 145

— China: 131

— France: 142

— Poland: 130

— Italy: 142

— Spain: 130

— United Kingdom: 141

— Belgium: 101

— United States: 141

— Netherlands: 100

## Employee Survey

Respondents were more than 5,000 full-time or part-time employees who are between 18 and 66 years old and work at companies with at least 100 employees. Participants spanned ten countries and represented companies from more than 18 industries. We asked employees about their experience at work.

## Age group:

— Gen Z (18–28 years): 618

— Millennials (29–44 years): 2,528

— Gen X (45–60 years): 2,022

— Baby boomers (61 years or older): 333

## Countries represented in survey:

— Germany: 1,006

— United Kingdom: 516

— United States: 516

— France: 515

— Italy: 515

— Belgium: 502

— China: 501

— Poland: 501

— Spain: 501

— Netherlands: 428

# About the authors

## HR Monitor leadership

Julian Kirchherr, partner in McKinsey's Berlin office
Email: Julian\_Kirchherr@McKinsey.com

## Author team

Julian Kirchherr, partner in the Berlin office

Karel Eloot, senior partner in the Shenzhen office

Sandra Durth, partner in the Cologne office

Ulf Schrader, senior partner in the Hamburg office

Vincent Bérubé, senior partner in the Montréal office

Charlotte Seiler, associate partner in the San Francisco office

Kira Rupietta, expert in the Düsseldorf office

Kristina Störk, associate partner in the Munich office

Marlene Senst, senior analyst in the Düsseldorf office

Séverine Fobe, associate partner in the Brussels office

Simon Gallot Lavallée, associate partner in the Rome office

The authors wish to thank Jürgen Sauer, Maria Ocampo, and Sophia Herwing for their contributions to this report.

This report was edited by Eric Quiñones, a senior editor in the New Jersey office.

## Press contact

Mirona Kraljic, senior communication specialist in the Berlin office
Email: Mirona\_Kraljic@mckinsey.com

June 2026

Copyright © McKinsey & Company

www.McKinsey.com

## Find more content like this on the McKinsey Insights App

![](images/cbb7555a9a6e4cfeed1aa753e4198a180be9f201fc43fcdc648bdfcb6b9d2b4e.jpg)

Scan • Download • Personalize
"""
