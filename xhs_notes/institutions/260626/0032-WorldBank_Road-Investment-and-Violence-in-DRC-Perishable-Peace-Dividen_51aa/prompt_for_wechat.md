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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Road Investment and Violence in DRC Perishable Peace Dividends

Mathilde Lebrand

Hannes Mueller

Peer Schouten

Jevgenijs Steinbuks

POLICY RESEARCH WORKING PAPER 11071

## Abstract

This paper explores the effect of road rehabilitation on violent conflict using a novel, rich dataset of road rehabilitation projects in the Democratic Republic of Congo. The country received massive external investments in transport infrastructure rehabilitation under conditions of endemic conflict, often with the explicit objective of supporting peacebuilding objectives. The paper finds that investments in road rehabilitation deter violence, which decreases significantly by around 5 to 10 percentage points after the completion of road rehabilitation. However, another significant finding, based on large-scale machine learning analysis of remote sensing data of road quality over time, is that the peace dividend of infrastructure investments is perishable: violence increases again as roads progressively deteriorate. Improved durability and systematic maintenance of roads are thus necessary to extend the “peace dividend” of road investments.

# Road Investment and Violence in DRC: Perishable Peace Dividends\*

Mathilde Lebrand $^{1}$ , Hannes Mueller $^{2}$ , Peer Schouten $^{3}$ , and Jevgenijs Steinbuks $^{1}$

$^{1}$ The World Bank $^{2}$ The Barcelona School of Economics $^{3}$ Danish Institute for International Studies

Keywords: DRC, mining, remote sensing, road infrastructure, violence
JEL Classification: O18, O19, O55, Q34

## 1 Introduction

In recent decades, billions of dollars have been spent on road projects in conflict-affected areas. Such investments are often motivated by a combination of donor objectives, which may include access to resources, economic development, stabilization, and state-building. While there is a growing body of literature around the impact of investments in transport infrastructure on economic development in fragile states (Ali et al. 2015; Berg et al. 2017; Damania et al. 2018), there is little evidence that transport infrastructure also improves stability in conflict-affected countries (Bachmann and Schouten 2018; Schouten et al. 2022).

This paper addresses this gap by analyzing the impact of road rehabilitation projects on violence in the Democratic Republic of Congo (DRC). The DRC is an ideal setting to explore the relationships between roads and violence. Since 1997, it has been home to one of the most protracted humanitarian crises and complex conflicts in the world and has a road network that ‘is about 152,400 kilometers long but, for a large part, it only exists on maps’ (World Bank 2017). Concomitantly, the DRC has been subjected to sustained reconstruction and stabilization efforts by the international community, involving large investments in its road network. We, therefore, ask the following question: what effect, if any, did these investments in the road network have on violence in the DRC? We explore the impact of road investments on violence through a longitudinal study, monitoring conflict incidence before, during, and after road rehabilitation, comparing levels of violence to areas where no roads were rehabilitated. We are also interested in how long the putative effects of roadworks on violence lasted: while the theories of change of road projects assume ‘forever impacts’, previous research suggests that rehabilitated roads rapidly deteriorate again, given a lack of maintenance (Bachmann and Schouten 2018; Schouten et al. 2022). Does the effect of road rehabilitation on violence wane as the road quality gradually decreases again?

We first assembled a new database of the main transport infrastructure projects that occurred in the DRC since the end of the Second Congo War in 2003. A comprehensive list of such projects did not exist. We collected project data (start and completion years, cost, location, and type of infrastructure) from multiple sources, including international donors and government agencies, to create a panel of geolocalized investments. Our final panel of large inter-city road investments includes 192 projects (see Appendix B).

To answer our first question, we estimated the causal impacts of road construction on conflicts. Establishing causal links is challenging because of the interaction of road projects and the activity of armed actors with other, often unobserved factors, such as conflict dynamics and economic activity. For instance, mining (a key economic activity in eastern DRC), outbreaks of violence, and road construction are all placed endogenously, often reacting to each other (cf. Luo et al. (2021)). We address this issue of causality between roads and conflicts in three ways. First, we show that road projects do not select into peaceful regions. This means that it is unlikely that armed violence generally forces road rehabilitation out of a conflict-affected region. Second, we use an identification strategy exploiting the fact that a road project crosses a 55km by 55km cell. Such localized treatment is unlikely to be related to local violence trends as the project completion is recorded at a higher level.

Third, we demonstrate this using a matched difference-in-difference method introduced by Mueller and Rauh (2023) but at the local cell level. This method matches treated cells with other untreated cells on the predicted conflict risk before treatment. Treated and untreated units are then analyzed together using a new two-way fixed effects method introduced by Callaway and Sant'Anna (2021). If road completion is selected for de-escalating conflict dynamics, then this would be detected by the local conflict forecast and lead to significantly lower treatment effects. By contrast, and in line with the declared international stabilization strategy for DR Congo of the 2010s (see DFID 2011), we find that controlling for conflict risk during the construction period, if anything, increases the estimated treatment effect of road project completion.

To answer our second question, we use novel techniques to extract information on changes in road quality based on satellite images. This allows us to observe how long road rehabilitation has had effects on road quality, and whether decreasing road quality correlates with an uptake of violence. Our findings can be summarized as follows. First, we see a statistically significant reduction in the incidence of violence after road rehabilitation projects are completed. Depending on the estimation method, we find that the completion of a project reduces violence by around 5-10 percentage points. The association between roads and reduction in violence tends to be the strongest for violence against civilians. Within our sample, the improved quality of transport infrastructure thus has a beneficial effect on conflict dynamics and stabilization (a 'peace dividend'). Second, we observe statistically that the effect of road rehabilitation on the number of violent incidents diminishes significantly after some time. The dynamic treatment effects we estimate around the completion date show that violence is first reduced directly after completion of a road project, but rebounds to pre-rehabilitation levels within three years. These findings are consistent with the suggestion that rehabilitated roads deteriorate again after projects are completed. To further substantiate this, we combine machine learning with thousands of remote sensing data observations to estimate overall road degradation patterns. Doing so, we arrive at a road discount factor of 0.735 per year, meaning that within three years, the road quality of rehabilitated roads on average decreases by 60 percent. $^{1}$

Our findings speak back to the literature on the links between transport infrastructure and conflict. Theories on these links vary wildly. On the one hand, road density is often used as a proxy for government control and associated with peace. Bad geography, from this perspective, is seen as an opportunity for rebels and an impediment to international peacekeepers and government security forces (Ruggeri et al. 2016; Müller-Crepon et al. 2021). Faulty transport networks also dampen economic activity that may constitute stumbling blocks to peace and prosperity. On the other hand, transport infrastructure and the ease of access it entails may also increase violence by facilitating the logistics of armed actors, whether rebels or military, and roads may act as magnets for violence (Zhukov 2012; Getmanski et al. 2019; Moreno et al. 2019; Rogall 2021; Voigtländer and Voth 2022; González et al. 2023; Raleigh and Hegre 2009). If there are strong hypotheses for both a negative and positive association between roads and political violence (Juan and Pierskalla 2014), it becomes all the more crucial to explore these links empirically, focusing on the impact of road interventions on conflicts. Taking advantage of new data on road rehabilitation over time to identify causal impacts, to the best of our knowledge, our paper is among the first to identify the positive, but temporary, impact of roadworks on conflict.

The rest of the paper is organized as follows. Section 2 provides a brief overview of the country's background and possible mechanisms at stake. Section 3 presents the data. Section 4 discusses our empirical framework and presents the main results. Section 5 brings additional results. Section 6 concludes.

## 2 Background

## 2.1 Country Background

Roads have a turbulent and violent history in Congo. They arguably only made their first appearance in the early 20th century, when the Belgian colonial administration began forcing local communities through appointed chiefs to expand and maintain the colonial road network to more efficiently project colonial power, replace endemic and deadly porterage that colonial logistics overbearingly relied on, and feed agricultural produce to the burgeoning population centers emerging around mines (Northrup 1988). Around the late 1940s, the Belgian Congo boasted over 130,000 km of road, most of it unpaved earth roads constructed through forced labor (see Figures 1 and 2).

![](images/476f07c2c0be9985d8e0d6043bf8996064f2cf333848f45a16142216130d075a.jpg)  
Figure 1: Road network in Belgian Congo, 1919

Tropical conditions meant that these roads needed near-permanent maintenance, which was largely ‘subsidized’ by the colonial administration through forced labor exactions. When the country became independent in 1960, the Congolese, of course, immediately gave up on forced roadworks, epitomizing as it did colonial oppression. As a result, within a matter of months after independence, 60 percent of the road network was unusable; by 1965, only 5,000 of the initial 130,000 km of road network was in good state (Eycken and Vorst 1967, p.421). Mobutu — the dictator ruling from 1965 to 1997 - was considered an ally of the West and consistently received major donor funding to maintain and rebuild main arteries. International donors held that maintenance of the vast road network that Zaire—as the country was called under Mobutu—inherited from the Belgians was not economically feasible, with the cost of rehabilitation exceeding the tax revenues the roads would yield, so donor funds focused on keeping open ‘priority roads’ that facilitated raw material exports and bulk imports (World Bank 1975, p.3). This mainly targeted the rail- and road network connecting copper mines in southeastern Zaire’s Katanga region to the Congo River and neighboring countries. Even so, much of these funds were misappropriated by Mobutu and his cronies (Willame 1986). The plummeting of copper prices in 1974, waves of failed nationalization, and structural adjustment destroyed already corrupt and faltering road maintenance parastatals in the 1980s, accelerating infrastructural dilapidation (Pourtier 1993).

![](images/7cb3ffa039e99784a0b6e5461471b15afc0e29516da7c3a75f20baafc6f61727.jpg)  
Figure 2: Road network in Belgian Congo, 1960

Maintenance of feeder roads in rural areas was by and large neglected, and rural populations were forced to rely on subsistence farming; underpaid government agents and local authorities lined whatever rural roads remained with roadblocks to extract wealth from farmers, largely as a legacy of colonial rule (Newbury 1984). When Western donors began investing in rural road rehabilitation in the 1980s as part of efforts to connect poor farmers to markets, anthropologists observed that improved transport connections only exacerbated wealth extraction by local authorities (Fairhead 1992).

Mobutu was allegedly wary of constructing direct roads between the capital Kinshasa and the East for fear of allowing insurrection to reach the capital. What he feared nonetheless happened, when in 1997 a Rwanda- and Uganda-backed rebel force swept across the country, taking town after town and eventually overtaking the capital Kinshasa. Ever since, eastern Congo has remained mired in conflict, the region's roads transformed into sinews of war. The number of armed groups has, over time, exploded, with larger groups fragmenting and new militia popping up. By the latest count, there are well over 120 armed groups active in Eastern Congo (Kivu Security Tracker 2021), many of which maintain connections to networks of patronage inside the Congolese army—which has itself been called the country's largest armed group, for the similarities in its mode of operating on the ground. Over decades of conflict, government forces and militia alike have sustained and enriched themselves as much through extracting rents from artisanal mines and farmers as from road users through roadblocks (Schouten 2022). While dynamics are extremely fluid and can, at times, be volatile, overall, government agents and larger armed groups such as M23 have competed for control over main roads, while government soldiers and smaller militia have tended to dominate rural connections in the countryside. Indeed, in 2017, 70% of the roadblocks with a government/army presence in North Kivu sat on national or provincial roads, while 79% of rebel roadblocks sat along tertiary/feeder roads (Schouten 2022, pp. 117-118). However, such patterns are highly unstable over time, with rebels periodically overtaking control over main roads. Roads are, therefore, magnets of continuous and often violent contestation among different types of authorities and road users over how goods, people, and capital circulate and who gets to benefit. According to the Congo Research Group (CRG 2019, p. 6), almost half of all violent events between 2017 and 2019 took place at or near roads, as opposed to mines or villages (cf. (O'Mealia 2022)).

In this context, stabilization operations by the international donor community have sought to intervene by coupling peacekeeping, humanitarian, and development efforts with ambitious road rehabilitation efforts. Rehabilitating roads would bring down the cost of logistics for aid and peacekeeping, kickstart economic development, and facilitate the extension of state authority (Bachmann and Schouten 2018, p. 14). To wit, the UN-led stabilization strategy for Congo spearheaded that roads are key because

‘rural areas are completely isolated and armed groups in the east have been able to move unhindered, populations have been cut-off and commerce has all but disappeared... Rebuilding roads and creating jobs in the process, expanding the transport grid and clearing corridors of checkpoints will not only destroy key profit centres of the remaining armed groups, these actions will also accelerate the economic reunification of the east, return markets to their past vibrancy and permit people to move freely.’ (DFID 2011, p. 14)

## 2.2 Theory Background

The premises upon which such strategies rest have been subject to a lively academic debate, which posits contradictory linkages between roads and violence.

Conflict studies typically assume that low road density, rough terrain and inaccessibility are enabling conditions for the onset and duration of civil war, arguing that rebels thrive in ‘ungoverned zones’ because of an absence of adequate transport infrastructure to enable government forces to maintain order (Tollefsen and Buhaug 2015; Hendrix 2011; Müller-Crepon et al. 2021). Such studies are based on the assumption that transport networks represent a form of ‘infrastructural power’, indispensable for states to actually control the population within their territories (Mann 1984; Scott 2009; Schouten and Bachmann 2022). By extension, the absence of well-functioning transport infrastructure is often taken as a key aspect of state fragility (Herbst 2014; Jimenez-Ayora and Ulubaşoğlu 2015; Schouten 2013). The policy implication is clear and has been widely internalized by stabilization operations: overcome the ‘friction of terrain’ by investing in road rehabilitation to allow government forces logistical access (Schouten and Bachmann 2017). Or, as Lt. Gen. Karl Eikenberry, then American military commander in Afghanistan, famously posited ‘Wherever the road ends, that’s where the Taliban starts’.

It is, however, just as easy to argue that efficient transport infrastructure facilitates more violence (Zhukov 2012). Rough terrain, from this angle, may protect populations from violence (Nunn and Puga 2012), whether affiliated to the state or not. Building on this idea, Mueller et al. (2022) argue that there is a dark side to proximity, in which higher transport costs between attackers and defenders reduce violence. In line with this, several case studies use the ease of transportation as an instrument for the intensity of adverse violence treatment. The most striking example here is Rogall (2021), who shows that bad road quality protected villages during the Rwandan genocide. There is some evidence that donor roads meant to increase the reach of the state in South Sudan inadvertently helped government forces perpetrate violence against civilians (Schouten and Bachmann 2017). Similarly, Ali et al. (2015) found that distance from roads may offer villagers in the Congolese countryside some protection from conflict. They suggest that ‘when conflict is high … better roads enhance the payoffs from rebellion’ (Ali et al. 2015, p.21). In other words, there are good arguments for both a positive and negative relation between road investments and violence in conflict settings.

Studying this dynamic is complicated by the fact that road investments and violence tend to cluster in mineral-rich Congolese provinces, making it difficult to isolate road-conflict dynamics from violent incidents that may be related to resource rents in the same geographica

[中间内容因长度限制已省略]

port the distribution of the number of projects by the starting year, the end year, and their duration. The average starting year is 2010, the year with the largest number of infrastructure projects that started. The average duration of projects is 3 years, with a large number of projects lasting less than a year.

Figures 4 and A8 map the location of all road investments that have been geolocalized and the investments by the donor (China, World Bank, UNOCHA, Belgium, etc.). The latest shows that most Chinese investments are located in the South, while World Bank investments are focused on the East and Northern parts of the country.

![](images/213a1c6c49254b4fdf23afacb1d0bf9d8573dc7e54f978b9ee4fb5c307059159.jpg)  
Figure A5: Number of projects by starting year

![](images/87225724c788ccb884f1ebfa398c50895cd43c3593d93b4ccc9a5a2557a7dfcd.jpg)  
Figure A6: Number of projects by end year

![](images/cce7d86d99672308f3662fad437e9f1db178dd9b21685e4b71b0146d7406b050.jpg)  
Figure A7: Number of projects by duration

![](images/c46d1dd4d2267024ecf910526a9b2e2d0c5d4ef2f2d2a3084d97bcb309ce7837.jpg)  
Figure A8: Map of geolocalized projects by donor

## B.5 Delays in World Bank projects

The following extracts come from the Implementation Completion Report (ICR), a World Bank document that closes a project by reviewing and assessing all the issues encountered during the project. This document provides the reasons why projects are delayed. For each of the following road projects from our final list, we highlighted some of the main reasons listed in ICRs explaining delays in the completion of the project.

## 1. High Priority Reopening and Maintenance Project (P101745)

“the delay in the execution of the works that were suspended for about a year after the suspension of Pro-Routes.”

"On November 27, 2017, the Bank suspended its disbursements for all road works financed under the Project due to the Borrower's noncompliance with its obligations to carry out the Project in conformity with appropriate environmental and social standards and practices, including management of gender-based violence (GBV), and to minimize the risk of additional harm to Project-affected people. The lifting of the suspension of IDA disbursements was approved on December 10, 2018, following a review that all conditions set out in had been met for works to re-start in full compliance with World Bank policies and safeguards obligations.”

“Project delivery was severely delayed by 28 months, delaying benefits to the population.”

“Slow pace of adoption of policies and institutional reforms. Delays were observed in the completion of numerous tasks connected to institutional capacity because of the weak capacity of the MIPWR, OdR, and other institutions that were responsible to review, endorse, or issue decisions concerning various activities under Component 2. Numerous institutional weaknesses were documented during implementation, including the capacity of DRC’s SMEs which requested a heavy capacity-building program to overcome the challenges to contribute effectively to the implementation of Pro-Routes. 68. Delays in the procurement process. Generally, the procurement office of the CI has been able to prepare and issue contracts for road reopening works. However, recurrent delays occurred in preparing bidding documents and contracting supervision firms. The lapse between the signing of the contracts for works and those related for monitoring resulted in considerable delays in the implementation and takeover of completed works, resulting in a Moderately Satisfactory procurement rating for CI up to AF2.”

## 2. Emergency Urban and Social Rehabilitation Project

"The extension was not triggered by the AF activities but due to delays with implementing the Roads and Water Components caused by technical difficulties and time taken to manage the resettlement process"

“During implementation, it transpired that the studies were more outdated than could have been expected, which did result in some delays.”

3. Dem Rep Congo - Western Growth Poles (P124720)

“Other important events include: (i) delays in getting SEZ legal framework in place, particularly the adoption of SEZ law (only completed in 2014)”

“because of non-adherence to WB safeguard standards with regard to resettlements and compensation of owners being displaced because of the establishment of the SEZ plus absence of an Environment and Social Management Plan - ESMP linked to the construction by the Government of a wholesale market, also was responsible for delays in project execution. 20.”

"The efforts made by the management team allowed to: (i) reduce the range of some activities; (ii) overcome the delays and difficulties encountered during the first years of implementation;"

“slow start of activities due to procurement delays with low disbursements”

4. DRC Urban Development Project FY13 (P129713)

“operational efficiency was encumbered by lengthy project implementation and delays to launch investments, in large part explained by limited capacity in the PS responsible for project implementation and multiple changes to project management. The organization of the 2018 elections (including for local government) and government reshuffles led to tensions in the country and delays in the delivery of project activities. For instance, the reshuffle of mayors and governors seriously affected the implementation of the performance-based contract, while the changes of ministers at the central level often led to changes in leadership within the PS, with ministers opting to nominate a confidant to lead the PS.”

5. Democratic Republic Of Congo Emergency Social Action Project P086874 Large Implementation delays
"""
