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
# Exploring the Gender Divide in Real Estate Ownership and Property Tax Compliance

Tatiana Flores

Guillermo Cruces

Jose Carlo Bermúdez

Thiago Scot

Juan Luis Schiavoni

Dario Tortarolo

POLICY RESEARCH WORKING PAPER 11060

## Abstract

This paper investigates gender disparities in residential property ownership and tax compliance in a large Argentine municipality using detailed tax administrative data. While ownership is evenly distributed between women, men, and co-owned properties up to the 40th percentile of the value distribution, higher-value properties exhibit significant gender disparities, with women's share dropping to less than $20\%$ in the top $1\%$ . Tax compliance increases with property value, with an average evasion rate of $46\%$ , and men and women are equally likely to meet their tax obligations across the distribution. However, women face slightly higher effective tax rates due to owning lower-value properties, which are disproportionately affected by a mildly regressive tax schedule. Gender responses to enforcement measures are also comparable. A soft randomized communication campaign significantly increased timely payments equally for both men and women, with men responding more quickly. Similarly, the findings show no gender-based differences in responses to macroeconomic shocks such as COVID-19. The study underscores the role of property tax in promoting equitable revenue mobilization and highlights the importance of gender-disaggregated data for informing tax policy and enforcement strategies.

![](images/f2b145fc7d4680d4b846ab737c7acc2ca2a9b5acc481b34078263075f5f178bb.jpg)

# Exploring the Gender Divide in Real Estate Ownership and Property Tax Compliance\*

Tatiana Flores

Guillermo Cruces

Jose Carlo Bermúdez

WORLD BANK, DIME

Nottingham & CEDLAS-UNLP

PUC-CHILE

Thiago Scot

Juan Luis Schiavoni

Dario Tortarolo

WORLD BANK, DIME

WORLD BANK, DECRG

WORLD BANK, DECRG

JEL Codes: H26, H71, J16, R28.

Keywords: Gender, real estate ownership, property tax compliance, Argentina.

## 1 Introduction

The property tax is increasingly recognized as a key component of equitable domestic revenue mobilization, with significant untapped potential for generating revenue (World Bank, 2021; Benitez, Mansour, Pecho, and Vellutini, 2023; Dom, Custers, Davenport, and Prichard, 2022; Maloney, Zambrano, Vuletin, Beylis, and Garriga, 2024). In many countries, real estate emerges as a primary repository of wealth, positioning property taxation as a potential tool for redistribution. However, as this tax grows in importance, taking into consideration its gender dimension is a central concern (Scot, Flores Ibarra, Moura, Feinmann, and Rocha, 2023; Komatsu, Ambel, Koolwal, and Yonis, 2021). Despite its relevance, the relationship between property taxation and gender outcomes remains largely understudied.

This paper provides new gender-focused empirical evidence on property ownership and taxation using administrative tax micro-data from Tres de Febrero, a large urban municipality in Argentina with over 360,000 inhabitants and about 120,000 households. Residents from Tres de Febrero are required to pay a monthly tax on their real estate, locally known as Tasa por Servicios Generales (TSG), which accounts for most of the local revenues in Argentine municipalities. We leverage rich tax administrative data and exogenous variation to show how gender interacts with several fundamental issues: the distribution of property ownership, tax evasion, and tax enforcement.

The analysis unfolds in three stages. First, we examine the distribution of residential ownership, presenting novel descriptive evidence on property ownership across the municipality, with a particular focus on gender disparities and the assessed values of properties. A significant challenge for such analyses is that property ownership records often lack explicit information on owners' gender. However, a unique feature of our setting is the structure embedded within national personal tax identifiers, which can be used to infer gender. Following methodological guidance from our team, the municipality's staff utilized this structural feature to infer the gender assigned at birth and the owners' ages for over 100,000 properties annually.

Our analysis reveals significant gender disparities in residential property ownership, primarily at the higher end of the property value distribution, where women own a smaller share than men. At the lower end of the property value distribution, up to the 40th percentile, ownership is fairly balanced, with women, men, and co-owned properties each accounting for about one-third of the residences. However, this balance shifts markedly as property values rise. While men's ownership share remains relatively stable throughout the distribution, women's share declines sharply for higher-value properties. This disparity is most pronounced in the top $1\%$ of property values, where co-owned properties account for $50\%$ , men own about $30\%$ , and women's ownership drops below 20%. These findings highlight the stark gender disparities in high-value property ownership, which are important to consider in the wealth distribution and gender equity literature.

Second, we conduct a detailed analysis of property tax compliance by gender and find that men and women are equally likely to pay their property tax bills. A key advantage of studying property taxes is that evasion is directly observed: owners are billed based on cadastral valuation, and we observe whether they pay or not. We characterize tax payment rates for women and men, examining how these rates vary across the wealth distribution, proxied by the properties' assessed value. We document substantial evasion, with slightly lower rates for women-owned properties (46%) compared to men-owned (48.5%). $^{1}$ The property tax gap is economically significant, amounting to roughly 8% of total municipal spending or the equivalent of the entire local public safety budget. On-time payment rates increase with property value, ranging from about 35% in the first percentile to 60% in the top percentile, though they remain similar for men and women across the distribution. However, women face slightly higher effective tax rates than men, driven by ownership of lower-value properties and a de jure regressive tax schedule. We also document a small but statistically significant difference in payment methods: women are slightly less likely to use electronic means to pay property taxes, even after controlling for age.

Third, we examine gender-specific responses to (soft) tax enforcement measures. We estimate the effects of personalized tax letters on current, past, and subsequent property tax payments for women and men by leveraging a large-scale field experiment conducted by Cruces, Tortarolo, and Vazquez-Bare (2023) in October 2020. $^{2}$ The intervention, launched amid the COVID-19 pandemic, sought to address a sharp decline in property tax payments driven by economic disruptions and lockdown measures. It consisted of sending a one-page personalized letter to randomly selected residences, providing information on the October 2020 bill (amount due and due date), past due debt, and online or in-person payment instructions.

Our causal analysis indicates that men and women respond similarly to personalized property tax letters. First, the letter recipients are substantially more likely to pay the October 2020 tax bill on time compared to those in the control group, with no statistically significant gender differences. For women, payment rates increased by 4.2 percentage points, a 12% rise from the control baseline of 35%. For men, the increase was 4.7 percentage points, representing a 13.5% improvement over their control baseline. The granularity of our data also allows us to examine payment behavior on a daily basis. Notably, men reacted more quickly to the tax letters, with the treatment effect appearing earlier and stabilizing after the due date. In contrast, treated women continued to make overdue payments in the days following, rapidly closing the initial gender gap in compliance. Second, the impact of the personalized tax letters extended beyond the targeted October 2020 bill, but the response is similar for men and women. Despite receiving the letters in early October, the intervention prompted some treated taxpayers to clear past-due debt from previous months and also pay their November and December bills. Third, while women present homogeneous responses across quintiles of property valuation, men exhibit a slightly negative gradient. Notably, in the lowest quintile, the personalized tax letter boosted timely payments of men by 8 percentage points—twice the increase observed for women.

Lastly, the inclusion of the recent pandemic in our analysis period allows us to examine gender-specific responses to a macroeconomic shock. $^{3}$ Although payment rates dropped significantly—by approximately 25 percentage points—at the onset of the COVID-19 pandemic, we observe no noticeable gender-based differences in response. This indicates that macroeconomic shocks seem to affect property tax delinquency behavior similarly for both men and women.

Overall, our findings suggest that gender-targeted strategies may have limited potential for improving tax compliance in the context of property taxes, as men and women exhibit similar baseline payment rates and respond in comparable ways to personalized tax letters. $^{4}$ Notwithstanding, the pronounced gender disparities in higher-value property ownership documented in our analysis raise important questions about wealth inequality and underscore the need for more research into the underlying causes and broader economic implications (e.g., differences in credit access).

We contribute to several strands of the literature studying asset ownership and the link between wealth taxation (including property taxes) and gender. Many countries recently highlighted the need to improve the collection of gender-disaggregated data on taxation in general, and on men's and women's property and capital ownership in particular, which is less commonly available (OECD, 2022). We add to a growing literature documenting gender patterns in property ownership and wealth (Holden and Tilahun, 2020; Kotikula and Raza, 2021; Komatsu et al., 2021; Gaddis, Lahoti, and Swaminathan, 2022; Scot et al., 2023), corroborating previous findings that women own fewer properties than men, particularly as property values increase. We document a substantial wealth gap, with women's ownership shares declining significantly for higher-valued properties.

We also provide new evidence on gender differences in tax compliance. Prior research indicates that women are generally more compliant with tax filing and reporting obligations compared to men (Kleven, Knudsen, Kreiner, Pedersen, and Saez, 2011; Asmare and Yimam, 2020; Cabral, Gemmell, and Alinaghi, 2021). Several key factors have been proposed to explain this disparity, including women's higher risk aversion (Croson and Gneezy, 2009), stronger tax morale, disparities in tax declaration and enforcement processes (Ambel and Woldeyes, 2024), and gender-specific social norms that interact with gaps in literacy, employment type, and access to information, among others (Komatsu, Shaukat, and Ozer, 2024). Our granular administrative data enables us to offer gender-disaggregated compliance insights on property taxation, in a low-enforcement setting, finding no meaningful gender differentials. Our finding contrasts with earlier studies, which suggested that women experienced either lower effective tax rates due to exemptions for lower-valued properties—more commonly owned by women in São Paulo, Brazil (Scot et al., 2023)—or, as Komatsu et al. (2021) found, a heavier tax incidence for female-headed households based on survey data from rural Ethiopia.

Lastly, while there is ample evidence on the effect of nudges—such as deterrence letters—on tax compliance and collection (Antinyan and Asatryan, 2024), research linking compliance and gender remains limited (see, for example, López-Luzuriaga and Scartascini, 2023; Awasthi et al., 2023). Hence, the results from this project exhibit great promise of informing policy debates and the conduct of tax policy that contribute toward the achievement of gender equality goals.

The remainder of the paper is organized as follows. In section 2, we describe the institutional context. Section 3 details the sources and composition of our tax data. Section 4 characterizes residential property ownership in Tres de Febrero by gender. Section 5 brings three stylized facts on property tax compliance and also leverages experimental evidence on differences in compliance responses across genders. Finally, Section 6 discusses some policy implications behind our results and then concludes.

## 2 Institutional Context

Tres de Febrero is an urban municipality (county) in the Greater Buenos Aires metro area, Argentina. As of 2022, it had approximately 365,000 residents and 115,000 households, making up 1.2% of the total population of Argentina (INDEC, 2022). It has the third highest population density in the province of Buenos Aires, with great connectivity and accessibility to neighboring areas, and contributes 2.4% to the total urban tax valuation of the province, ranking 13th among the 135 municipalities in fiscal valuation.

The municipality levies a local tax known as TSG (Tasa por Servicios Generales), which is linked to the provision of lighting and cleaning services. This type of tax is present in every municipality of the Buenos Aires Province and is the main source of locally collected resources (Porto, Fernández Felices, and Puig, 2019). Tres de Febrero is no exception, as the TSG accounts for 20% of its total resources and 45% of its own revenue in 2021.

The monthly TSG tax comprises both variable and fixed components. In our period of analysis 2018–2020, the tax liability for residential taxpayer i was calculated as follows:

$$
\text { Monthly   tax } _ {i} = \left[ \text { Cadastral   value } _ {i} \times \text { Tax   rate } / 1 2 + \text { Fixed   charge } \right]\tag{1}
$$

The variable component is calculated by applying a tax rate to the property's assessed value. These tax rates vary across eight property-use categories defined by the municipality: residential, industrial, commercial, wholesale establishments, mixed-use residential with commerce or factory, empty lots, civil entities, and religious entities. As of 2021, the statutory tax rates ranged from $0.32\%$ to $2.48\%$ (see Table 1). Property assessments are based on the cadastre maintained by the Revenue Agency of the Province of Buenos Aires (ARBA), though the municipality reserves the right to update these values based on its own criteria.

The fixed charge corresponds to a flat fee for specific municipal services, including security, health, fire departments, and maintenance of public spaces. Notably, fixed charges constitute a larger share of the total tax burden for lower-value properties. This share varies significantly across the property value distribution, comprising 65% of the total tax burden for properties in the first decile but only 14% for those in the tenth decile (Figure C.4). As a result, the overall tax schedule has historically exhibited a mildly regressive structure, as illustrated in Figure 6. $^{5}$

TSG bills are issued monthly and are due in the first weeks of each month, with twelve equal installments per year. Alternatively, residents can opt for an advance annual payment at the beginning of the year instead of monthly installments. While cadastral values are seldom updated, both the tax rates and fixed charges are adjusted annually to keep up with inflation.

Property Tax Enforcement. Enforcing local property taxes in developing countries has historically been a tall order. Anecdotal evidence from conversations with public servants at Tres de Febrero's tax agency reveals several factors limiting their ability to enforce the TSG property tax:

1. Limited human, technical, and legal resources. Subnational tax agencies often struggle with enforcement due to inadequate IT systems and limited human resources. In 2020, for instance, Tres de Febrero's tax audit department operated with just five employees overseeing 130,000 TSG payers and over 4,000 businesses subject to a local turnover tax (TISH). This team relied on data from a 1980s IBM mainframe to determine taxpayer debts and payments, leading to high costs for identifying debts and noncompliance, making large-scale audits infeasible. Given their limited resources, local tax agencies typically focus their enforcement efforts on a few large businesses that generate most of the income and tax revenue, rather than overseeing tens of thousands of households. For example, in 2020 ten companies accounted for half of the business tax revenue, compared to 25,000 properties that made up half of TSG's revenue.

2. High political cost. The political economy of enforcing a local property tax is contentious (Cabral and Hoxby, 2012), especially in high-inflation contexts. In the Province of Buenos Aires, municipal elections occur biennially, and mayors tend to avoid comprehensive tax enforcement campaigns on delinquent households during odd years to maintain voter support. Moreover, mayors have been reluctant to update the cadastral value of properties (i.e., the tax base) for the same reason (Christensen and Garfias, 2021). Consequently, the property tax's share in the overall tax structure has declined over time.

3. Financial disincentives to compliance. Frequent debt regularization programs and a partial adjustment of delinquent tax debt can further disincentivize timely tax payments. Until 2022, the municipality charged an annual simple interest rate of 12% on late payments, significantly below the inflation rate. Additionally, the municipality has implemented payment plans with preferential interest rates and debt forgiveness (moratorias) in four of the last five years. These actions incentivize taxpayers to postpone payments to reduce the real value of their tax debt or even wait for the next moratoria to settle their obligations (e.g., see Lauletta and Montano Campos, 2023).

Collectively, these factors provide indicative evidence of low enforcement capacity for property taxes in developing countries. In this context, property tax compliance is essentially quasi-voluntary and potentially driven by intrinsic motives such as social norms and reciprocity (Luttmer and Singhal, 2014). Consequently, there is potential for soft int

[中间内容因长度限制已省略]

the July 2020 bill before and after the due date (July 8th, 2020). The area of each histogram integrates into one. A larger bar on a particular date means that the payment frequency of the corresponding group is higher than that of the other group. Panel (b) shows the coefficients and 95% confidence intervals from a saturated regression that computes, on each calendar day, the payment rate difference between treatment and control. Standard errors are clustered at the individual level. The vertical bar indicates the due date for the July 2020 bill. Reassuringly, and unlike Figure 9, men and women exhibit no response for a pre-intervention bill.

Figure C.9: Property tax compliance by quintiles and gender (PLACEBO)
(a) Timely payment rates by quintiles  
![](images/eafffc8abfb6045bfe80b47e8d34fd6d4e34d0d9f7ef0118ae5c40383af65525.jpg)

(b) Treated vs Control (September 2020)  
![](images/749f014626dd6a733effe35da823a51806cafcd6e8a86b2f8bda07d0f43e3beb.jpg)

Notes: These figures show the placebo effect of the communication campaign on payment rates by quintiles of assessed values. We focus on timely payments of the September 2020 pre-intervention bill. Timely payments are defined as bills paid before the 27th of the corresponding month (i.e., any payment made after the 27th is considered unpaid). The top panel shows payment rates in levels for the control group (women in red and men in blue). The bottom panel reports the treatment effects for each quintile—i.e., the difference between treated and control units—and 95% confidence intervals. The letters were delivered between September 28th and October 7th, 2020. Each coefficient is estimated in separate regressions. Standard errors are clustered at the street-block level. This placebo exercise using a pre-intervention bill, confirms a null effect for men and women across quintiles of assessed values.

## C.3 Balance checks

We run balance test checks to verify the comparability of the treated and control groups in terms of demographic and account-related characteristics in 2019, the year before the intervention. We estimate the difference in means with the following regression:

$$
X _ {i g} = \alpha + \theta \mathbb {1} (T r e a t e d _ {i g}) + \varepsilon_ {i g}\tag{3}
$$

where $X_{ig}$ is a property/account i characteristic observed in the data. We allow $\varepsilon_{ig}$ to be correlated within clusters g (street-blocks) and use a cluster-robust variance estimator. In this regression, $\theta$ captures the average difference of $X_{ig}$ of treated units relative to control units not receiving any letter. The results are reported in Table A2 and reassuringly confirm that our groups are highly balanced. The null effect on timely payments (i.e., excluding past-due payments) of the September 2020 bill—the bill prior to our intervention—sheds further light on the balance between groups (see Figure C.9).

Table A2: Balance tests

<table><tr><td rowspan="2"></td><td>Property Value</td><td>Front Meters</td><td>House type</td><td>Past due debt</td><td>Bill amount</td><td>N Bills paid 2019</td><td>Digital payment</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td></tr><tr><td colspan="8">A. Women and Men</td></tr><tr><td>Treated</td><td>-0.00(0.01)</td><td>-7.89(10.13)</td><td>-0.00(0.00)</td><td>-0.01(0.01)</td><td>2.86(5.31)</td><td>0.08(0.06)</td><td>-0.01(0.01)</td></tr><tr><td>Mean Control</td><td>13.65***(0.01)</td><td>822.26***(6.88)</td><td>0.92***(0.00)</td><td>0.57***(0.00)</td><td>386.25***(3.66)</td><td>7.06***(0.04)</td><td>0.38***(0.00)</td></tr><tr><td>Observations</td><td>47,645</td><td>48,488</td><td>48,488</td><td>48,488</td><td>48,488</td><td>48,488</td><td>28,194</td></tr><tr><td colspan="8">B. Women</td></tr><tr><td>Treated</td><td>0.00(0.01)</td><td>-11.87(13.14)</td><td>-0.00(0.00)</td><td>0.00(0.01)</td><td>-0.20(7.32)</td><td>0.02(0.09)</td><td>-0.00(0.01)</td></tr><tr><td>Mean Control</td><td>13.58***(0.01)</td><td>779.42***(9.30)</td><td>0.93***(0.00)</td><td>0.56***(0.01)</td><td>362.04***(4.70)</td><td>7.02***(0.06)</td><td>0.37***(0.01)</td></tr><tr><td>Observations</td><td>17,766</td><td>18,089</td><td>18,089</td><td>18,089</td><td>18,089</td><td>18,089</td><td>10,416</td></tr><tr><td colspan="8">C. Men</td></tr><tr><td>Treated</td><td>-0.00(0.01)</td><td>-5.86(11.27)</td><td>-0.00(0.00)</td><td>-0.01(0.01)</td><td>4.49(6.60)</td><td>0.11(0.07)</td><td>-0.01(0.01)</td></tr><tr><td>Mean Control</td><td>13.70***(0.01)</td><td>847.87***(7.23)</td><td>0.91***(0.00)</td><td>0.57***(0.00)</td><td>400.72***(4.40)</td><td>7.08***(0.05)</td><td>0.39***(0.01)</td></tr><tr><td>Observations</td><td>29,879</td><td>30,399</td><td>30,399</td><td>30,399</td><td>30,399</td><td>30,399</td><td>17,778</td></tr></table>

Notes: This table shows balance regressions to test for differences in observable characteristics between the treatment and control groups. Each column corresponds to a separate regression (equation (3) in the text). The dependent variables in each column are: (1) the log of assessed property value; (2) the front meters of the property; (3) an indicator for the property being a house versus a house with a store; (4) an indicator for past due debt; (5) the amount paid in the bill corresponding to December 2019 (including zeroes); (6) the number of bills paid in 2019 (the maximum is 12); (7) for those who paid, whether they did so digitally. The rows Mean Control display the constant of each regression, corresponding to the average of the dependent variable for accounts that did not receive a letter. Standard errors clustered by blocks are reported in parentheses. \* p<0.10, \*\* p<0.05, \*\*\* p<0.01
"""
