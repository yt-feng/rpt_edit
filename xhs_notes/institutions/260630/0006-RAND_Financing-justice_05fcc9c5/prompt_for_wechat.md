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
- 已识别机构名：`兰德公司`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份兰德公司研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
LUCY STRANG, RICHARD HUGHES

Justice
for All
series

## Financing justice

JUNE 2026

![](images/63e10d1b59291f1d08787590f2f0ce37fdc1415bcecc5c4304a0fce6953d052e.jpg)

Foreword by Alderman & Sheriff Robert Hughes-Penney

Justice for All
Series – Financing
justice

Equal access to justice is

![](images/c1861d8b7861d3c0132c2252989d2601fc1f1ffbfac214a6b1a46b44dbed9438.jpg)

a cornerstone of any fair and well-functioning society. However, as the Justice for All series at the Old Bailey has consistently highlighted, the current reality of the criminal justice system is one of mounting pressure, constrained resources and increasing complexity. This latest briefing, ‘Financing justice’, examines a fundamental question: whether the way we fund justice today is capable of meeting the demands of tomorrow.

Evidence gathered throughout this series points to a system under significant strain. Court backlogs have reached unprecedented levels, with open Crown Court cases approaching 80,000 and delays extending for years. At the same time, prison capacity has remained persistently high, operating at or above 95% occupancy for more than a decade. These challenges are closely interlinked: delays in the courts contribute to rising remand populations, which in turn place further pressure on an already stretched prison estate.

Against this backdrop, a clear imbalance has emerged between demand on the system and the resources available to meet it. Although levels of some traditional crimes have declined, increases in offences such as sexual crime and fraud illustrate the evolving nature of criminal activity.

The growing complexity of cases places additional demands on investigators, advocates and the courts, requiring the system to adapt not only to greater volumes but also to more intricate forms of offending.

The longer-term trajectory of justice funding compounds this imbalance. Investment has not kept pace with economic growth or overall public spending, and real-terms funding for the Ministry of Justice (MoJ) remains below historic levels. While recent funding commitments – particularly in relation to prison infrastructure – are both necessary and welcome, they are largely directed towards managing acute pressures rather than enabling broader, system-wide reform.

In this context, the role of the private sector becomes increasingly important. As this report highlights, substantial pools of capital exist across institutional impact investment, social investment and philanthropic sources. Of this funding, however, relatively little currently focuses on justice-related outcomes. Innovative approaches – including social impact bonds, blended finance models and outcome-based funding – demonstrate that private capital can be deployed to support rehabilitation, prevention and system capacity. By linking financial returns to measurable social outcomes, such as reductions in reoffending or improved resettlement, these models enable investors to contribute meaningfully while sharing risk and complementing limited public resources.

The case studies presented in this report bring these approaches to life. Initiatives such as His Majesty's Prison (HMP) Peterborough Social Impact Bond (SIB) show how private investment can fund targeted rehabilitation services, with returns linked directly to reductions in reoffending. Similarly, programmes such as the Skill Mill and Offender to Rehab illustrate how combining public, private and third-sector funding can deliver concrete social and economic benefits, including improved employment prospects and reduced criminal activity. Collectively, these examples highlight the potential for scaling such models and the need for careful design to ensure they remain effective, accountable and aligned with wider policy objectives.

## Introduction

Over the past year, the Justice for All events series at the Old Bailey has explored the state of the UK criminal justice system through multiple lenses. Reflections from keynote speeches, panel discussions and accompanying research briefings have shed light on the sustained pressures on the system as a whole. The second event in the series, ‘Justice for the Accused’, explored the drivers of inefficiencies in the courts, including ineffective and collapsed trials, increased case complexity, declining availability of criminal law practitioners, court closures, limited sitting days in the Crown Court and the lingering impacts of the COVID-19 pandemic. $^{1}$

The paper also highlights the increase in demand across the system, particularly since the pandemic. MoJ data published in 2025 indicated that open caseloads in the Magistrates' courts increased from the previous year to 373,084, and reached an unprecedented 79,619 in the Crown Court. $^{2}$ Similar levels of strain have been evident in the prisons and probation services over the past decade. Dame Anne Owers' 2025 Prison Capacity Review found that prison estate occupancy has remained above 95% for over 12 years, barring a short window at the start of the pandemic. $^{3}$ These pressures within the system can often interact and compound each other. For example, delays in the Crown Court contribute to a high remand population in prisons, which in turn adds pressure to an overcrowded prison estate.

The third paper in the Justice for All series, ‘Justice for Victims and Survivors’, also illuminated emerging trends in crime across England and Wales. The Office for National Statistics (ONS) indicates clear declines in many ‘traditional’ crime categories, such as homicide (which decreased by 6% in the year ending December 2025) and offences involving knives or sharp instruments (which decreased by 10%). $^{4}$ By contrast, police recorded 209,079 sexual offences in England and Wales in the year ending March 2025 – an 11% increase from the previous year, $^{5}$ and prosecutions for sexual offences increased by 18% in the year ending September 2025. $^{6}$ ONS data also indicate that fraud increased by 33% to around 4.4 million incidents in the year ending December 2025, a 30% increase on the earliest comparable year (ending March 2017). $^{7}$

Available resources within the criminal justice system have also experienced long-term constraints. A report by the Institute for Fiscal Studies $^{8}$ on MoJ spending showed that real-terms resource expenditure in 2025–2026 was 14% lower than its peak in 2007–2008. Alongside significant growth in the Capital budget, recent funding increases do not offset severe cuts in the 2010s, given a 33% real-terms reduction between 2007–2008 and 2016–2017.

The Institute for Government has also highlighted capacity constraints within the system. It has reported increasing staffing shortages in the criminal justice system, with a 30% decline in permanent court staff since 2010–2011 and the probation service operating at 30% below its target staffing level as of 2025. $^{9}$

Furthermore, spending in the justice system has not kept pace with growth in the UK economy as a whole, nor with overall government spending. A recent report commissioned by the Bar Council noted that the economy grew by 11.5% between 2009–2010 and 2022–2023, while government spending increased by 10.1% in real per-person terms. However, justice funding in England and Wales fell by 22.4% in real per-person terms. $^{10}$ Similarly, the Institute for Fiscal Studies reported that, for 2025–2026, MoJ real-terms spending was set to be 14% lower than in 2007–2008, and 24% lower per person. $^{11}$

In this context, the Independent Review of the Criminal Courts (often referred to as the ‘Leveson Review’) was commissioned to explore the nature and scale of the challenges facing the criminal justice system. The Review highlighted the effects of chronic underfunding on the courts and their workforce, as well as the increasing complexity of criminal law. It described deep-rooted problems in the system, and stressed that addressing them effectively requires that ‘all the levers – more resources, structural reform and efficiency – have to be engaged.’ $^{12}$

The fourth briefing paper in the Justice for All series, ‘Justice for Prison Leavers’, also explored the wider financial, social and personal costs of poor outcomes in the criminal justice system. It highlighted evidence demonstrating the vital importance of stable housing, employment support and mental health and substance use services for people leaving to reduce reoffending. $^{13}$ It also sought to capture the costs of reoffending for victims, communities, the health system, policing, courts, prisons and probation, and the false economies of cutting resourcing in one part of the system only to generate costs elsewhere by reducing the system’s ability to prevent offending or resolve cases efficiently.

# Demand for prison spaces is likely to exceed capacity by 12,400 places by the end of 2027.

It is important to note that there has been increased recent investment in some priority areas of the criminal justice system, largely to keep pace with rapidly growing demand. For example, the Spending Review 2025 committed £7bn between 2024–2025 and 2029–2030 towards prison builds, aiming to increase capacity by 14,000 additional places by 2031, with additional investment in building maintenance across prisons and the probation service. $^{14}$ However, the National Audit Office has noted that, according to the MoJ's projections, demand for prison spaces is likely to exceed capacity by 12,400 places by the end of 2027 – even if current expansion projects are delivered within anticipated timelines. $^{15}$ The Spending Review also included up to £700m in additional funding for probation service capacity expansion per year by 2028–2029, as part of the sentencing reforms recommended by the Independent Sentencing Review. $^{16}$

Earlier this year, the government announced plans to lift the cap on sitting days for Crown Courts in England and Wales, and to increase the use of artificial intelligence and introduce ‘Blitz courts’ that would list similar cases together. The aim is to relieve pressure on the court system, with some cases now scheduled for hearings in 2030. $^{17}$

However, it has acknowledged that reducing court backlogs will take time, and stakeholders such as the Criminal Bar Association have warned that workforce shortages continue to constrain the use of available capacity.

## Fiscal constraints in government

The government faces multiple competing demands on spending, balancing those for health, defence, education, welfare and justice. Furthermore, current fiscal rules limit the scope for using additional borrowing to meet increased demands.

As an ‘unprotected department’, whereby its funding is not ring-fenced, the MoJ has tended to lose out in spending reviews (acknowledging that not all funding for the justice system goes through the MoJ).

Where funding is available, it is often – understandably – directed towards crisis response: delivering new prison capacity is a government obligation, ensuring there are places for the courts to send people who require custody and maintaining the integrity of the system.

By contrast, investing in prevention often loses out, despite the potentially significant returns. According to a study for the Access to Justice Foundation and the Bar Council, every £1 invested in free early legal advice saves the government £2.71 in downstream costs (e.g. reduced reliance on benefits). $^{18}$ Unlike this example, where most of the savings were realised in the first year, the savings from prevention can often be longer-term and evident beyond one-year budgets, three-year settlements and five-year parliaments. In particular, investing in diversionary work with young people at risk could realise savings over a much longer period. Tackling the complexities of individual offending also relies on combining different departments'

interventions and resources, which introduces bureaucratic constraints when departments are funded individually, and savings may not accrue to the department that invests.

Private finance initiatives (PFIs) have been used in the UK to secure funding for justice capital projects (new prisons and court buildings) $^{19}$ and operational services (through Design, Construct, Manage & Finance contracts). $^{20}$ However, the then Chancellor of the Exchequer confirmed in his October 2018 Budget speech that the UK government would abolish the use of PFI, and its successor, Private Finance 2, as the basis for future public-private partnership projects. The Autumn 2025 Budget announced a new Public-Private Partnership model for new Neighbourhood Health Centres, involving the upgrading and repurposing of existing buildings and the construction of new facilities. $^{21}$

## Investment models for the justice system

We identified a range of innovative alternative financing models used to tackle the challenges facing the justice system.

The following case studies briefly summarise alternative financing models tested in the justice system in recent years, broadly divided into three categories:

![](images/b0b1fb613fabbf55b1b2d9ec7543615f4a0768794a06199570d8faae071c9660.jpg)

Social investment

![](images/a647a30b8dc5b57528ca332518d65eca921c466a710c94d2575c6f8d61e509aa.jpg)

Payment by results

![](images/2ba176e9a57a6ec2d5f19fe7a528ea1e2973371a87dd4b0dca3373d7eeffb407.jpg)

Blending public and private sector funds.

## HMP Peterborough Social Impact Bond (SIB)

Between 2010 and 2015, a new service called the One Service supported adult men leaving HMP Peterborough after short prison sentences. At the time, this group had no statutory post-release supervision and no systematic resettlement support, and the pilot aimed to reduce reoffending by filling this gap. The One Service provided ‘through-the-gate’ support with staff meeting prisoners before their release, assessing their needs and planning what would happen when they left custody. Post-release support was offered for up to 12 months after release, including for men who were recalled or returned to prison during that period.

The support offer included help with finding somewhere to live; with benefits, debts and basic financial stability; with employment, training and skills; and with referrals to health, drug and alcohol and other local services. It was initially intended to cover three cohorts of around 1,000 short-sentenced men each, released from HMP Peterborough. A third cohort received similar support on a fee-for-service basis after Transforming Rehabilitation unexpectedly introduced statutory supervision and a new payment-by-results (PbR) model for this group.

The programme aimed to test an SIB as a PbR mechanism in criminal justice, shifting performance risk away from the government and paying only for measured reductions in reoffending. Private, non-governmental investors provided the up-front money to run One Service, and the MoJ, supported by the Big Lottery Fund, agreed to repay these investors, with a return, only if reoffending was reduced by an agreed amount. If reoffending did not fall by enough, investors could lose some or all of their money.

An evaluation of the first cohort in Peterborough showed a noticeable reduction in reoffending (of 8.4%), enabling investors to recover their capital and achieve a positive return. $^{22}$ In a subsequent process evaluation, service users and practitioners highlighted the importance of immediate practical help (especially accommodation and basic costs) in reducing pressure to reoffend. $^{23}$ The evaluation also found that the Peterborough SIB helped foster stronger relationships between HMP Peterborough, local agencies and voluntary providers, leading to more services operating within the prison than before. Overall, it found that the SIB structure enabled flexible, adaptive delivery, including adding new partners, making service changes, and quickly using small funds to prevent crises. However, under Transforming Rehabilitation, shifting the third cohort to fee-for-service demonstrated how major policy changes can reshape SIB/PbR schemes and why contracts must anticipate policy risk.

## The Skill Mill

The Skill Mill is a social enterprise that employs young ex-offenders (aged 16–18) on six-month paid work placements on environmental projects in the UK. During their placement, participants are supported by mentoring and counselling, gain practical experience and skills and can receive recognised qualifications. Local authorities, businesses and charities can commission work. The programme seeks to address the high rates of recidivism among juvenile offenders and existing barriers to accessing education, training and employment among this cohort. $^{24}$ Analysis by the Youth Endowment Fund indicates that 32.5% of offenders aged 10–17 reoffended in 2022–2023. $^{25}$ Furthermore, according to ONS data, 987,000 UK young people aged 16–24 were not in education, employment or training in 2024. $^{26}$

In 2020, the Skill Mill introduced an SIB to deliver their services in eight locations over four years. Income generated through the programme consisted of outcomes payments and revenues from local clients for completing the work. Outcomes payments relied on individuals' programme registration and completion, an AQA Employability Skills Level 2 award qualification, at least 75% programme attendance, prevention of reoffending and engagement in employment and/or further education. $^{27}$

An evaluation of the Skill Mill SIB was published in January 2025. $^{28}$ It found that, of the 243 young people who participated in the programme, 237 completed induction and 179 completed the programme. A total of 203 did not reoffend within 12 months of the programme start, and 86 secured employment or further training within 6 months of the programme ending. The evaluation notes that the programme's timing, launched just before the start of the COVID-19 pandemic, significantly impacted its implementation. The SIB was unable to return investors' funding in full, and Skill Mill funded around £181,000 of the costs of running the final two cohorts itself. The original revenue target from sales to employers was £1,149,754, but the programme only generated £958,129.

![](images/3be7a512c3cee1fe3d441ed5bec9a40a39ce16b3d96de8c351317aed100eab28.jpg)

## Payment by Results

Local Justice Reinvestment (LJR) Pilots

The MoJ launched the LJR Pilot in 2011 to test PbR commissioning to reduce demand on the criminal justice system in six local areas. Savings from reduced demand were partially reinvested in additional local crime-reduction efforts. Each area was given the flexibility to

[中间内容因长度限制已省略]

rope. Ministry of Justice Analytical Series.

24 Government Outcomes Lab. 2023. 'The Skill Mill.' As of 16 June 2026: https://golab.bsg.ox.ac.uk/knowledge-bank/case-studies/the-skill-mill/

25 Youth Endowment Fund. 2025. Statistics Update: Trends in Violence Affecting Children (April 2025).

26 Office for National Statistics. 2025. 'Young people not in education, employment or training (NEET), UK: February 2025.' As of 16 June 2026:
https://www.ons.gov.uk/employmentandlabourmarket/
peoplenotinwork/unemployment/bulletins/
youngpeoplenotineducationemploymentortrainingneet/february2025

27 Government Outcomes Lab. 2023. 'The Skill Mill.' As of 16 June 2026: https://golab.bsg.ox.ac.uk/knowledge-bank/case-studies/the-skill-mill/

28 BaBaines, Susan, Russell Webster, Chris Fox, and Harry Armitage. 2025. Final Evaluation of the Skill Mill SIB January 2025.

29 Ministry of Justice. 2013. Justice Reinvestment Pilots: First Year Results. London: MoJ. As of 16 June 2026: https://www.gov.uk/government/publications/justice-reinvestment-pilots-first-year-results

30 Ministry of Justice. 2013. Justice Reinvestment Pilots: Second Year Results. London: MoJ. As of 16 June 2026:
https://www.gov.uk/government/publications/justice-reinvestment-pilots-second-year-results

31 Ministry of Justice. 2015. Local Justice Reinvestment Pilot: Final process evaluation report. London: MoJ. As of 16 June 2026: https://assets.publishing.service.gov.uk/media/5a75020740f0b6399b2afee7/local-justice-reinvestment-pilot-process-evaluation-report.pdf

32 British Retail Consortium. 2026. Crime Survey 2026. London: British Retail Consortium. Published 24 February 2026.

33 Taylor, Emmeline, and Arabella Kyprianides. 2022. Offender to Rehab Programme: A Process Evaluation of the Birmingham Pilot – Final Report. Birmingham: West Midlands Office of the Police and Crime Commissioner. July 2022.

34 Prisoners Building Homes. 2026. 'How prisoners building homes works.' As of 16 June 2026: https://www.pbh.org.uk/how-prisoners-building-homes-works/

35 UK Debt Management Office. 2021. 'Press notice: Syndicated launch of the inaugural green gilt manufacturing on 31 July 2033 in the week commencing 20 September 2021.' As of 16 June 2026: https://www.dmo.gov.uk/media/mafhgoyu/pr270821.pdf

36 UK Parliament. 2025. 'Better Futures Fund.' Vol. 772, 9 September. As of 16 June 2026: https://hansard.parliament.uk/commons/2025-09-09/debates/EB54DE24-6031-430D-B39C-30CFFB623FF9/BetterFuturesFund

37 Gadd, Caroline. 2026. 'The Better Futures Fund: Why it matters and why it needs heart as well as finance.' Social Finance. As of 16 June 2026: https://www.socialfinance.org.uk/evidence/the-better-futures-fund-why-it-matters-and-why-it-needs-heart-as-well-as-finance

38 Social Impact Investment Advisory Group. 2025. Mobilising the impact economy as partners in national renewal. As of 16 June 2026: https://assets.publishing.service.gov.uk/media/6904bd34823bdda9488b2505/SIIAG\_Recommendations.pdf

39 Office for the Impact Economy. 2026. 'Office for the Impact Economy.' Gov.uk. As of 16 June 2026: https://www.gov.uk/government/groups/office-for-the-impact-economy

40 Ministry of Justice, and HM Prison & Probation Service. 2026. 'Offender management statistics quarterly: October to December 2025.' Gov.uk. As of 16 June 2026: https://www.gov.uk/government/statistics/offender-management-statistics-quarterly-october-to-december-2025/offender-management-statistics-quarterly-october-to-december-2025

## About the Justice for All series

Justice underpins our freedoms, our economy, and our civic life. Yet our systems are under pressure. The Justice for All Series provides a platform to confront this reality with honesty and ambition.

Conceived by Sheriff Robert Hughes-Penney of the City of London (2025–26), and hosted at the Central Criminal Court (Old Bailey), the five-part Justice for All series brings together those in a position to ask hard questions – and propose evidence-based solutions.

Framed around the anniversaries of Magna Carta (1225) and UN Sustainable Development Goal 16, the series does not seek consensus, but clarity: What does a just society require today? Who must act? And what will it cost us if we do not?

The Justice for All paper series has been funded internally by RAND Europe internal research.

Find out more about the initiative here: https://justiceseries.org/

## About the authors

Lucy Strang is a Research Leader at RAND Europe, focusing on criminal justice, public health, and drug policy research. She has extensive experience in evaluating government programmes, particularly relating to vulnerable groups in the criminal justice system. Strang holds a B.A. in law and a B.A. in Humanities from the Australian National University (ANU). She also received her M.S.Sc. in applied anthropology and participatory development from ANU.

Richard Hughes is a Partner at PA Consulting, where he leads PA's work in Justice. He has spent the majority of his career working in the Criminal Justice System, delivering complex change and improving operational performance for the different agencies, initially as a Civil Servant, including a stint in the Prison Service, and for the last 25 years as a consultant. His experience includes delivering youth justice reform; supporting the digital transformation of the courts; designing new business processes for the CPS; contributing to the Review of Civil Legal Aid; successive rounds of Probation Reform and the introduction of new Electronic Monitoring services. He also leads PA and the PA Foundation's award-winning Second Chance Programme, working with a group of rehabilitation charities to enable innovative approaches to rehabilitation.
"""
