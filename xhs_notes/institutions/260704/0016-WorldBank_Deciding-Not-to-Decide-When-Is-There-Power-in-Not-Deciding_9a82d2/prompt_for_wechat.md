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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Deciding Not to Decide

## When Is There Power in Not Deciding?

Marya Hillesland

Cheryl R. Doss

Serena Masino

Martina Querejeta

Aletheia Donald

Greg Seymour

Clare Clingain

POLICY RESEARCH WORKING PAPER 11065

## Abstract

Agency—the ability to define one’s own goals and make choices to achieve them—is often measured through questions that capture an individual’s direct involvement in decision-making. Yet not participating in decision-making may not always imply a lack of power. Drawing on the notion of effective power, this paper conceptualizes two forms of this power: effective power by proxy and effective power by influence or persuasion. The paper explores indirect ways of pursuing one’s goals when not directly involved in the decision, using unique mixed methods data from multiple members of rural households in Kilifi County, Kenya. The results indicate that traditional decision-making measures underestimate the agency of some individuals—particularly that of husbands and fathers, who can disproportionately rely on their preferences being met through their effective power by proxy, without bearing the time and cognitive cost of actively engaging in decision-making. The results also indicate that women's agency varies by marital status and household composition. Focusing on decisions between married women and their husbands overlooks the dynamics of intergenerational households where other members, like mothers-in-law or sons, are involved in the decision-making process. The paper concludes by providing practical recommendations for measuring agency in surveys.

![](images/aa1f32a936fbce3faedc4cb2735e0d9afdac333ac5f831ee33bd7fdfbbcb2e7f.jpg)

# Deciding Not to Decide: When Is There Power in Not Deciding?

Marya Hillesland, Cheryl R. Doss, Serena Masino, Martina Querejeta, Aletheia Donald, Greg Seymour and Clare Clingain\*

Keywords: gender, households, power, survey methodology, Kenya

JEL codes: C8, J16, I32, Q25

## 1. Introduction

Empowerment is the ability to make strategic decisions to command resources and influence outcomes (Kabeer, 1999, Kabeer, 2005). Agency, a concept central to empowerment, is the ability to define one's goals and aspirations and exercise one's own choices to reach desired outcomes (Kabeer, 2001, Kabeer, 1999). Agency includes claiming the right to influence important decisions as a strategic part of the empowerment process (Annan et al., 2021) and cannot be understood outside the context of the individual's own goals and the values deemed important to her (Sen, 1985).

In the literature, measures of agency and empowerment are often operationalized through questions regarding decision-making (see Donald et al., 2020, for an overview). Many studies use survey questions on women's participation in household decisions related to health care, expenditures, children's education, visits to family, family planning, and agriculture to create either separate indicators measuring whether the individual considers herself a decision-maker, or a combined index to proxy agency (e.g. Hou and Ma, 2013). These indicators focus on what Sen (1985) describes as the “person's ability to make choices and to control procedures directly (whether or not he or she is successful in achieving the desired goal)” (Alkire, 2008)—or more precisely, a specific enactment of this control where the individual is actively exercising that ability. It is control over the process of choice, or procedural control, regardless of the outcome.

Conceptually, there are limitations to measuring empowerment in this way. For example, it is often assumed that if a person does not participate in making decisions, it means that she does not have power to influence the decision. In addition, many studies focus on the decision-making of married women with respect to their husbands. Yet, in many contexts, intergenerational or extended family households are common—and different dynamics may be at play when decisions are made with a mother-in-law or son, rather than a spouse.

In this paper, we use unique mixed methods data on decision-making within rural households in Kilifi County, Kenya, collected between October 2022 and March 2023, to better understand when not participating in decision-making might be a form of agency. Our data is unique in that it allows us to examine decision-making across various family relationships and roles within the household, and to interrogate the way household composition relates with decision-making power, or authority or influence in decisions made in the household, and forms of agency.

Our intrahousehold survey was administered to all adults in the household, going beyond the usual focus of just the husband and wife. Questions are asked about the decisions made about the household's water, including water collection, allocation, and expenditures. Because water collection and allocation are often within women's domain, these provide new insights into intrahousehold decision-making. In addition, we ask more traditional decision-making questions on health care for oneself, visits to one's family or relatives, and on how the money one earns is used. We also draw on qualitative data on intrahousehold decision-making processes and norms, with a particular focus on securing water for the household.

Kilifi County, which is on the eastern coast of Kenya just north of Mombasa City, is predominately inhabited by the Giriama people, one of the ethnic groups that make up the Mijikenda peoples. Households traditionally consist of a large homestead with several small huts built on the compound. Extended families often live together on the compound and share daily tasks. Sons' and nephews' homes are often situated alongside their father's or uncle's homes. The Giriama are traditionally polygamous and in some homesteads, co-wives reside together, although not necessarily in the same dwelling. The homestead may have a shared 'kitchen' building, and the group may share cooking responsibilities. Water for the household is often collected from multiple sources to meet domestic needs and the needs of livestock and other productive activities.

Rural households derive their livelihoods largely from rainfed agriculture and livestock activities, and Kilifi County has arid and semi-arid lands which are vulnerable to drought conditions. As such, inadequate and unpredictable rainfall in recent decades contributes to continued food insecurity and poverty in the area. During data collection, a prolonged dry period continued over many months following years of reduced rainfall. In this regard, decisions made about water collection and use within the household play an important role in the health and wellbeing of household members.

We begin by providing an overview of decision-making as a measure of agency, emphasizing the notion of “effective power,” which can be a form of power even when an individual does not directly participate in the decision-making process. We then describe the data and decision-making processes within households in Kilifi County. We explore who is and is not involved in household decision-making, and then investigate who has effective power even when not directly involved in the decision. Finally, we explore how effective power differs across the life-cycle and by household composition.

We argue that the exercising of agency allows for multiple pathways of pursuing goals that matter to oneself, which may or may not include direct participation in decisions. Measuring effective power when not directly involved in the decision-making process is crucial for comprehensively assessing agency, as it captures forms of power that might otherwise go unnoticed. When an individual is in a position of power or has the ability to delegate, effective power may require little effort. The individual's status may allow his needs to be met without direct involvement in decisions or through delegation. However, other forms of effective power when not directly involved in the decision-making process require more time and effort to influence outcomes. While power can be wielded to achieve goals, this indirect approach may not always be as efficient as traditional, direct decision-making.

## 2. Decision-making as a measure of agency: Control versus effective power

While decision-making is often used as a proxy for agency, there are a number of reasons why it may not be appropriate to do so (Arugay et al., 2024). One reason is that an individual's direct participation in a decision-making activity may not always accurately reflect control over the process. Many studies use any involvement in decision-making as an indicator of agency, without considering the extent to which the individual has voice or authority over the choice in the decision. For example, in surveys when people report joint decision-making, it could indicate that there was collaboration and negotiation. But it does not mean that each had equal voice and power in the process. As an example, Acosta et al. (2020) found that in rural households in the District of Nwoya in Northern Uganda, women often reported joint decision-making with their spouse. But this simply meant that men informed their wives of decisions they had taken, and their wives consented with their silence (Acosta et al., 2020). Without understanding the decision-making process within the community and cultural context, it is impossible to know whether an individual's claim to joint decision-making is actually an exercise of control over the choice (Seymour and Peterman, 2018). To address this, some decision-making question sets—such as those in the Women's Empowerment in Agriculture Index (WEAI) regarding agricultural production on the household farm—ask respondents both about the level of input the individual had in the household decision and about who typically makes the decision (Alkire et al., 2013, Malapit et al., 2015, Malapit et al., 2019).

But even for those with voice in the decision-making process (and, thus, procedural control), researchers typically do not know whether the decision-makers are making choices that are in line with their values and goals. To constitute a form of agency, the decision needs to be motivated by and reflective of the individual's own values and interests (Donald et al., 2020). Yet, even when someone exercises control over the outcome, he or she may be compelled to make decisions in ways that do not align with his or her values or interests.

Self-determination theory recognizes a person's actions are the product of several different motivations (Ryan and Deci, 2000b, Ryan and Deci, 2000a). Intrinsic motivation refers to moving toward a goal because something is inherently interesting or fulfilling to the individual. An intrinsically motivated person is self-motivated; she or he “is moved to act for the fun or challenge entailed rather than because of external prods, pressures, or rewards” (Ryan and Deci, 2000a). Extrinsic motivation, on the other hand, refers to being swayed to do something because of something external (Ryan and Deci, 2000a). This includes being motivated to act to avoid physical or economic consequences or verbal abuse (external regulation) or to conform to the expectation of others and the desire to be accepted and to avoid shame (introjected regulation). An individual may choose not to directly engage in decision-making because he fears social backlash for participating in decisions, particularly when doing so fits outside conventional gender norms (Rudman, 1998). Individuals who undermine conventional social norms often trigger hostile responses within the community (Rudman et al., 2012). For example, men in Makondo Parish in Uganda who collect water daily for household domestic purposes are ridiculed as being submissive to their partners or mentally unsound (Asaba et al., 2013). Because social rejection diminishes community belonging and self-esteem, avoiding backlash by conforming is a means of self-protection (Rudman et al., 2012). While both men and women are constrained by prevailing gender norms, social norms do not just reinforce the gender hierarchy. They can also reinforce hierarchy by age and status. As an example, a qualitative study in Gujarat, India, finds younger women, particularly daughters-in-law and daughters, benefited little from a water intervention as compared to the older women in their household. Younger women were burdened with collecting most of the water, while the older women were able to invest their time in new income-generating activities, which improved their status (Sijbesma et al., 2009).

For decision-making to be a form of agency, the choice made needs to be motivated by one's own values and interests, rather than by external or introjected regulation. Recent studies are able to distinguish between motivations that are reflective of one's own values and interests and external regulation, but have a more difficult time distinguishing between one's own values and introjected regulation within decision-making (Seymour and Peterman, 2018, Vaz et al., 2016). Vaz et al. (2016) suggest that this may occur because it can be difficult to distinguish personal values from internalized community norms. An individual's knowledge and value system are socially situated and influenced by one's culture.

Another limitation of decision-making as a proxy for agency is that it may not be necessary to directly participate in decision-making to exercise power. Exercising control over the process of choice in line with one's goals and values is one aspect of agency; there are also forms of “effective power” or the “power to achieve chosen results” (Sen, 1985). In situations of “effective power,” regardless of how outcomes are reached, power is “exercised in line with what we would have chosen and because of it” (Sen, 1985). If an individual has “effective power,” he may make the choice not to actively participate in decision-making as he knows the decision will be made, as it has in the past, in line with his desired outcome. Not participating in the decision-making process is possible when there is a viable default option, which is the outcome when a decision is not made directly. For example, the allocation of water in the household may reflect the male household head’s preferences regardless of whether or not he is directly involved in the decision. As such, not participating in the decision-making process may be a viable option for the household head. Default decisions often bias the status quo (Kahneman et al., 1991, Jachimowicz et al., 2019), and thus, the default outcomes favor those with influence within the existing structures and power relations.

It could also be an individual may not be directly involved in decision-making because he has delegated the decision to a person he trusts will make a good decision, or because he lacks interest in the decision as any outcome is acceptable to him. In these cases, the individual chooses not to participate in the decision as a way to free up his own time and mental space for something more important. The choice not to actively engage in the decision-making process is motivated by the person's own interests and personal values, and the knowledge the preferred outcome is likely to be attained without the individual's involvement. Bandura (2001) calls this a form of “proxy agency,” where an individual does not want the responsibility and stress that direct control over the decision-making would require. As Bandura (2001) explains: “No one has the time, energy, and resources to master every realm of everyday life. Successful functioning necessarily involves a blend of reliance on proxy agency in some areas of functioning to free time and effort to manage directly other aspects of one’s life.”

There also can be tension between asserting one's needs through direct action and participation in decision-making and navigating within socialized norms and structures of subordination. Someone may opt not to directly engage in decision-making because of fear of backlash or social and economic penalties for participating in decisions. She could worry that it is not appropriate to participate. Speaking up may be a form of agency in itself in that it may challenge the larger power structures and norms, but with potentially heavy consequences. When this is the case, she may assert her goals within her space of subordination. Rather than resist and challenge oppressive power dynamics, she may even use the “instruments of [her] oppression” for her aims. Agency in this context is the capacity to realize one’s goals within the confines of customs and traditional norms (Mahmood, 2016). To avoid negative consequences and attain a preferred outcome, she may influence or exert pressure on the decision-maker without actively engaging in the decision-making process (Agarwal, 1997). This can also be an expression of power through “proxy agency,” where people use different means to influence people to act on their behalf to get their favored outcomes (Bandura, 2001). Kabeer (1999) refers to this as a form of “informal decision-making agency.” The individual is claiming her right to influence decisions important to her; although, it is not done by asserting authority directly within the decision-making process. It may be done behind the scenes because it is inappropriate to speak up, or it may be through regular discussions or other input into the decision (Donald et al., 2020).

In these ways, not being in direct control of the decision could still be a manifestation of acting on one's goals and values, and thus an aspect of agency. We investigate expressions of “effective power” when an individual does not directly participate in the decision-making process, and compare this to when a person does participate directly in the decisions.

In this paper, we define two separate expressions of “effective power” when people do not have procedural control. We define having effective power by proxy as choosing not to be directly involved in the decision so as to free up time or mental space for something else. This type of effective power is most likely to manifest in household-related decisions, such as decisions over household expenditures or water source choices. For personal matters, such as decisions over one’s own health care and control of own income, we expect that individuals would want direct control in the decision, or if they do not, that not wanting direct control is motivated by external or introjected regulations, meaning they are motivated to avoid physical or economic consequences or verbal abuse (external regulation) or inf

[中间内容因长度限制已省略]

ender & Development, 13, 13-24.

KAHNEMAN, D., KNETSCH, J. L. & THALER, R. H. 1991. Anomalies: The Endowment Effect, Loss Aversion, and Status Quo Bias. Journal of Economic Perspectives, 5, 193-206.

MAHMOOD, S. 2016. Feminist theory, embodiment, and the docile agent: Some reflections on the Egyptian Islamic revival. Readings in the Theory of Religion. Routledge.

MALAPIT, H., KOVARIK, C., SPROULE, K., MEINZEN-DICK, R. & QUISUMBING, A. 2015. Instructional guide on the abbreviated women's empowerment in agriculture index (A-WEAI). Washington, DC: International Food Policy Research Institute.

MALAPIT, H., QUISUMBING, A., MEINZEN-DICK, R., SEYMOUR, G., MARTINEZ, E. M., HECKERT, J., RUBIN, D., VAZ, A., YOUNT, K. M. & PHASE, G. A. A. P. 2019. Development of the project-level Women's Empowerment in Agriculture Index (pro-WEAI). World development, 122, 675-692.

RUDMAN, L. 1998. Self-Promotion as a Risk Factor for Women: The Costs and Benefits of Counterstereotypical Impression Management. Journal of personality and social psychology, 74, 629-45.

RUDMAN, L. A., MOSS-RACUSIN, C. A., GLICK, P. & PHELAN, J. E. 2012. Reactions to vanguards: Advances in backlash theory. Advances in experimental social psychology. Elsevier.

RYAN, R. M. & DECI, E. L. 2000a. Intrinsic and Extrinsic Motivations: Classic Definitions and New Directions. Contemporary Educational Psychology, 25, 54-67.

RYAN, R. M. & DECI, E. L. 2000b. Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. American psychologist, 55, 68.

SEN, A. 1985. Well-Being, Agency and Freedom: The Dewey Lectures 1984. The Journal of Philosophy, 82, 169-221.

SEYMOUR, G. & PETERMAN, A. 2018. Context and measurement: An analysis of the relationship between intrahousehold decision making and autonomy. World Development, 111, 97-112.

SIJBESMA, C., VERHAGEN, J., NANAVATY, R. & JAMES, A. 2009. Impacts of domestic water supply on gender and income: results from a participatory study in a drought-prone region in Gujarat, India. Water Policy, 11.

VAZ, A., PRATLEY, P. & ALKIRE, S. 2016. Measuring Women's Autonomy in Chad Using the Relative Autonomy Index. Feminist Economics, 22, 264-294.

## 9. Appendix

Table A.1. Descriptive statistics and differences between those in household roster and sample

<table><tr><td></td><td>Women in the household roster</td><td>Women&#x27;s Sample</td><td>Diff</td><td>Men in the household roster</td><td>Men&#x27;s Sample</td><td>Diff</td></tr><tr><td>Age</td><td>39.88(18.18)</td><td>40.49(17.34)</td><td>0.61(0.75)</td><td>38.35(17.35)</td><td>39.40(18.07)</td><td>1.05(0.83)</td></tr><tr><td colspan="7">Marital status</td></tr><tr><td>Never married</td><td>0.21(0.40)</td><td>0.16(0.36)</td><td>-0.05***(0.02)</td><td>0.36(0.48)</td><td>0.34(0.47)</td><td>-0.02(0.02)</td></tr><tr><td>Monogamous union</td><td>0.49(0.50)</td><td>0.53(0.50)</td><td>0.04*(0.02)</td><td>0.53(0.50)</td><td>0.53(0.50)</td><td>0.00(0.02)</td></tr><tr><td>Polygamous union</td><td>0.06(0.24)</td><td>0.06(0.24)</td><td>0.00(0.01)</td><td>0.04(0.20)</td><td>0.05(0.21)</td><td>0.00(0.01)</td></tr><tr><td>Widow/er, divorced, separated</td><td>0.24(0.43)</td><td>0.25(0.43)</td><td>0.01(0.02)</td><td>0.07(0.26)</td><td>0.08(0.27)</td><td>0.01(0.01)</td></tr><tr><td>Currently attending School</td><td>0.06(0.25)</td><td>0.07(0.26)</td><td>0.01(0.01)</td><td>0.13(0.34)</td><td>0.14(0.34)</td><td>0.00(0.02)</td></tr><tr><td colspan="7">Educational attainment</td></tr><tr><td>No schooling</td><td>0.43(0.50)</td><td>0.43(0.50)</td><td>-0.00(0.02)</td><td>0.10(0.30)</td><td>0.10(0.30)</td><td>0.00(0.01)</td></tr><tr><td>At least some primary school</td><td>0.41(0.49)</td><td>0.41(0.49)</td><td>0.00(0.02)</td><td>0.61(0.49)</td><td>0.60(0.49)</td><td>-0.00(0.02)</td></tr><tr><td>Some secondary school (or higher)</td><td>0.16(0.36)</td><td>0.15(0.36)</td><td>-0.00(0.02)</td><td>0.30(0.46)</td><td>0.30(0.46)</td><td>0.00(0.02)</td></tr><tr><td>Lives with parents</td><td>0.21(0.41)</td><td>0.21(0.41)</td><td>-0.00(0.02)</td><td>0.49(0.50)</td><td>0.50(0.50)</td><td>0.01(0.02)</td></tr><tr><td>Lives with in-laws</td><td>0.19(0.39)</td><td>0.19(0.39)</td><td>-0.00(0.02)</td><td>0.01(0.09)</td><td>0.00(0.06)</td><td>-0.00(0.00)</td></tr><tr><td>Lives in single adult household</td><td>0.02(0.16)</td><td>0.03(0.17)</td><td>0.00(0.01)</td><td>0.02(0.15)</td><td>0.03(0.17)</td><td>0.01(0.01)</td></tr><tr><td>Lives in household with a couple and no other adults</td><td>0.14(0.34)</td><td>0.15(0.35)</td><td>0.01(0.01)</td><td>0.15(0.36)</td><td>0.15(0.36)</td><td>0.01(0.02)</td></tr><tr><td>Lives in extended family household</td><td>0.62(0.49)</td><td>0.62(0.49)</td><td>-0.00(0.02)</td><td>0.59(0.49)</td><td>0.58(0.49)</td><td>-0.01(0.02)</td></tr><tr><td>Lives in a household with co-wives</td><td>0.07(0.25)</td><td>0.06(0.24)</td><td>-0.00(0.01)</td><td>0.04(0.20)</td><td>0.04(0.20)</td><td>-0.00(0.01)</td></tr><tr><td>Ganze</td><td>0.21(0.40)</td><td>0.24(0.43)</td><td>0.03*(0.02)</td><td>0.19(0.39)</td><td>0.24(0.43)</td><td>0.05**(0.02)</td></tr><tr><td>Kaloleni</td><td>0.38(0.49)</td><td>0.44(0.50)</td><td>0.06***(0.02)</td><td>0.30(0.46)</td><td>0.39(0.49)</td><td>0.08***(0.02)</td></tr><tr><td>Magarini</td><td>0.28(0.45)</td><td>0.33(0.47)</td><td>0.05**(0.02)</td><td>0.29(0.45)</td><td>0.38(0.48)</td><td>0.09***(0.02)</td></tr><tr><td></td><td>1,214</td><td>1,059</td><td>2,273</td><td>1,054</td><td>808</td><td>1,862</td></tr></table>

Notes: Standard errors in parentheses. \*\*\* p<0.01, \*\* p<0.05, \* p<0.1. All estimations are computed using survey weights to address sampling. There is less than one percent of men who live with their in-laws.
"""
