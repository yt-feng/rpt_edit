你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Labor Taxation in the United Kingdom

SIP/2026/074

Thomas McGregor and Philippe Wingender

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 24, 2026. This paper is also published separately as IMF Country Report No 26/173.

2026
JUL

![](images/f3028a99a9ca2f00eab624cd95135fee4674fe82830f3d37b364c000597b3005.jpg)

# IMF Selected Issues Paper European Department

Labor Taxation in the United Kingdom
Prepared by Thomas McGregor and Philippe Wingender\*

Authorized for distribution by Romain Duvall
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 24, 2026. This paper is also published separately as IMF Country Report No 26/074.

ABSTRACT: This paper uses a microsimulation model to assess the revenue potential, labor-supply and distributional effects of alternative labor tax reforms. The scope for new measures to raise significant revenue in the future through a uniform increase in labor taxes, without significantly weakening labor supply, is limited. Targeted increases in marginal tax rates toward the bottom of the earnings distribution could raise more revenue, with lower efficiency losses, but come with an equity trade-off. More fundamental reforms that improve work incentives in line with optimal tax design could deliver higher revenues with a better efficiency-equity trade-off.

RECOMMENDED CITATION: McGregor, Thomas and Wingender, Philippe. "Labor Taxation in the United Kingdom". IMF Selected Issues Paper 26/074.

<table><tr><td>JEL Classification Numbers:</td><td>H21, H24, H31, J22, C63</td></tr><tr><td>Keywords:</td><td>Labor taxation; optimal taxation; marginal effective tax rates; microsimulation; labor supply; tax-benefit reform; United Kingdom</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>TMcGregor@imf.org; PWingender@imf.org</td></tr></table>

SELECTED ISSUES PAPERS

# Labor Taxation in the United Kingdom

United Kingdom

Prepared by Thomas McGregor and Philippe Wingender

# UNITED KINGDOM

SELECTED ISSUES

July 2026

## Approved By

European Department

## Prepared By Thomas McGregor (EUR) and Philippe

Wingender (RES)

## CONTENTS

LABOR TAXATION IN THE UK \_\_\_\_ 2
A. Motivation \_\_\_\_ 2
B. Labor Taxes in the UK \_\_\_\_ 3
C. Model and Data \_\_\_\_ 6
D. Simulation Results \_\_\_\_ 8
E. Robustness \_\_\_\_ 12
F. Policy Conclusions \_\_\_\_ 14

## FIGURES

1. Labor Taxation Across Countries \_\_\_\_ 4

2. Structure of Labor Taxation in the UK 5

3. Labor Tax Reform Scenarios 11

4. Robustness Scenarios 13

## TABLE

1. Participation Elasticities by Income Group \_\_\_\_ 7

2. Targeted 5ppts Marginal Tax Increases Across Income Groups \_\_\_\_9

References 15

# LABOR TAXATION IN THE UK

With labor tax revenues set to rise steadily over the medium term, the debate over how much additional revenue can be raised from labor taxes, while preserving work incentives and supporting growth, is likely to intensify. This annex seeks to contribute to the current policy debate. It uses a microsimulation model that combines household-level microdata with a detailed representation of the tax and benefit system to assess the revenue potential, labor-supply and distributional effects of alternative reforms. There are three main findings. First, the scope for new measures to raise significant revenue in the future through a uniform increase in labor taxes, without significantly weakening labor supply, is limited. Second, targeted increases in marginal tax rates toward the bottom of the earnings distribution could raise more revenue, with lower efficiency losses, but come with an equity trade-off. Third, more fundamental reforms that improve work incentives in line with optimal tax design could deliver higher revenues with a better efficiency-equity trade-off. These findings are robust to different modelling assumptions about the labor supply elasticities as well as the degree of social aversion towards inequality, although the key trade-offs can differ depending on the structural assumptions used.

## A. Motivation

1. As one of the largest and most reliable sources of public revenues, labor taxation is likely to remain at the center of the UK fiscal debate. Labor taxes—income tax and national insurance contributions—account for just under half of all tax revenues in the UK, or around 16 percent of GDP. Labor income is, therefore, an obvious candidate for raising revenue to reduce the deficit and meet growing spending pressures. But the UK is already relying heavily on this channel: despite collecting somewhat less from labor taxes than many OECD peers, revenues have increased substantially in recent years and are projected to rise further as frozen thresholds broaden the tax base and push more income into higher bands. Taxing labor also creates disincentives to work and increase effort. This creates a tension between revenue needs and the growth agenda: additional increases may be a priori fiscally attractive, but their economic cost will depend critically on how they interact with the existing tax and benefit system, and how they affect people's decisions to work.

2. The extent to which higher labor taxation and the design of social benefits may be weighing on labor-market outcomes is already under discussion. Bank of England analysis suggests that the increase in employer NICs announced in the Fall 2024 budget, alongside rises in the National Living Wage, has added to labor costs and contributed to weaker employment growth. Recent work by the Institute for Fiscal Studies suggests these changes may have had particularly strong effects on job opportunities for young people. At the same time, Resolution Foundation analysis suggests that the design of health-related benefits may weaken incentives to work at the margin, particularly where support is more generous than standard unemployment benefits and conditionality is lighter.

3. This debate is likely to intensify in the coming years as spending pressures grow. Demands on public finances are set to increase, driven by defense spending commitments, the climate transition, and an ageing population. In this context, a key question is how much space there is to increase labor taxation under the current structure without exacerbating existing labor-market distortions and undermining the growth agenda. A related question is whether labor taxes should be increased uniformly across, or whether some rebalancing is needed across income brackets.

4. Modelling the tax system can help assess the trade-offs that tax and benefit reforms create between revenue potential, efficiency, and equity. Raising tax rates can increase revenue, but it may also reduce incentives to work, save, or earn more, lowering economic activity and limiting the revenue gain. At the same time, a more progressive system may improve equity by shifting the burden toward higher earners but can also create sharper distortions if it relies on very high marginal tax rates or abrupt benefit withdrawal. Conversely, depending on how they are designed, reforms that strengthen work incentives may improve efficiency and labor supply but may reduce redistribution or require offsetting measures elsewhere to preserve revenues. A model-based approach can help make these trade-offs more transparent by quantifying how alternative reforms affect labor decisions, earnings, and fiscal revenues across the earnings distribution.

## B. Labor Taxes in the UK

5. The UK collects slightly less revenue from labor taxation than other OECD countries. $^{1}$ Indeed, many high-tax European economies collect substantially more revenue from labor taxes than the UK does (Figure 1.A). This reflects lower social security contributions in the UK compared to other countries and a greater reliance on progressive income taxes, although the distinction between these two types of labor income taxation is less clear-cut in the UK where national insurance contributions are more loosely linked to benefit entitlements. $^{2}$

6. However, labor tax revenues have increased substantially in recent years and are set to rise further over the medium term. The UK's overall tax burden, measured by the tax-to-GDP ratio, has increased by about $5 \frac{1}{2}$ ppts since the mid-1960s and now stands at around 35 percent. Within this broader rise, labor-tax revenues—defined here as personal income tax plus employee and employer social security contributions—have also risen markedly. Having remained relatively low compared with other G7 economies for much of the post-war period, labor-tax revenues in the UK have risen by almost 4 percentage points of GDP since the mid-2010s. Under the current fiscal plans, revenues from labor taxes are projected to increase by a further 2 percentage points of GDP by the end of the decade, as the extension of the income tax threshold freezes beyond 2028 take effect (Figure 1.B). This implies that labor taxation will account for a large share of the projected increase in the overall tax burden over the coming years.

Figure 1. Labor Taxation Across Countries

7. While average tax rates are low by international standards, marginal tax rates can be very high, particularly for high earners. The tax wedge—which measures the difference between labor costs to the employer and the corresponding net take-home pay of the employee—for an average earner in the UK is lower than the OECD and G7 averages (Figure 1.C). This reflects lower social security contributions than in many continental European economies. Marginal tax rates—the share of additional labor income that is either taxed away or lost due to the reduction in benefits—are also broadly in line with other advanced economies for average earners. However, the highly progressive labor tax system in the UK means that the marginal tax rates faced by high earners in the UK are significantly above those faced by workers in other G7 countries (Figure 1.D).

A. Composition of Labor Taxes (Percent of GDP; 2024)

![](images/78f69046db713c11ab1c4ec86b003ec2112dabb3a1c09b8d735ab379a20083df.jpg)  
Sources: Global Revenue Statistics 2025 and staff calculations  
B. Labor Tax Share (Percent of GDP)

![](images/612a79b64e081201ef92d73807a0df3008a0fc6f19dd83e8480e70efd00f0651.jpg)  
Sources: Global Revenue Statistics 2025 and staff calculations  
C. Average Tax Wedge (Percent of labor cost)

![](images/da7b4df9b85023adaa1404efbca3e657d14c026be88dd55b2e1a1062e5b79f95.jpg)  
Sources: OECD Taxing Wages 2026 and staff calculations
Notes: The tax wedge is the share of income taxes and social security contributions, and cash benefits, in total labor costs. Household composition: 2 adult couple, with 2 kids, earning 100 percent and 67 percent of average wage.  
D. Marginal Tax Rate (Percent)

![](images/1a1190a89198e628eaf344416f2ec56d6b5493f625f758abb46f802267955043.jpg)  
Sources: OECD Tax-Benefit model and staff calculations
Notes: The marginal tax rate is the percentage point increase in taxes paid for an additional 1 percent increase in labor income. Household composition: 1 adult, earning 100 percent of the average wage.

8. The UK tax system is marked by significant threshold effects. Threshold effects, or tax “cliff edges”, here refer to sharp increases in marginal tax rates that can create either disincentives to enter the labor market or work more. Several important threshold effects in the UK tax system mean that marginal tax rates on labor earnings vary substantially depending on an individual’s level of earnings. First, for low earners the withdrawal of Universal Credit (UC), the main means-tested benefit in the UK, can significantly reduce the financial gain from employment. This effectively creates a very high tax rate on participating in the labor market—the tax rate that someone pays on their earned income when they start working compared to what they would receive out-of-work (Figure 2.A). For those already in work, a second threshold exists when the basic income tax rate begins to apply, on earnings above the £12,570 personal allowance (PA). Third, there are a set of sharp threshold effects for higher earners that are driven by the combination of progressive income tax rates, withdrawal of child benefits (CB) at earnings above £60,000, and tapering of the personal allowance (PA) at earnings over £100,000. These can result in very high marginal tax rates as earnings rise, reducing the incentive to work more. Figure 2.B shows how the marginal effective tax rate—which takes into account both taxes and benefits—changes as earnings rise. These “tax cliffs” can result in the “bunching” of taxpayers just below the point at which high marginal tax rates take effect (Figure 2.C).

Figure 2. Structure of Labor Taxation in the UK  
![](images/c9dea65b68c91d37138982d516778dc0ca66087a1fc816f2dda42d47e03c51d8.jpg)  
Sources: UKFRS 2023/24, UKMOD and staff calculations
Notes: The participation tax rate (PTR) is defined as the change in post-tax, post-transfer, income in work compared to out of work. Indirect taxes refer to VAT.  
Sources: UKFRS 2023/24, UKMOD and staff calculations
Notes: The marginal effective tax rate (METR) is defined as the ratio of change in disposable income to change in pre-tax earnings. Indirect taxes refer to VAT.

![](images/46f97159b078f6a6e1ce741e5e79e9fa1030fe5821a1f91bd73aed4aae3bfa7f.jpg)

## C. Model and Data

9. The analysis presented here uses a microsimulation model based on the Mirrlees framework. $^{3}$ The model combines household-level microdata, a detailed representation of the current UK tax and benefit system, and a social welfare function to assess the revenue, labor-supply, and distributional effects of alternative labor income tax reforms. The framework assumes individuals differ in productivity and earnings, derive utility from consumption, and face disutility from work. They also respond to changes in after-tax income along two margins: whether to participate in the labor market, and, conditional on working, how much to work and earn. The government is assumed to choose a non-linear labor tax schedule subject to an exogenous revenue requirement, trading off revenue needs, efficiency costs from behavioral responses, and redistribution objectives. In this framework, the “optimal” marginal tax schedule depends on four sufficient-statistic objects: social marginal welfare weights (i.e. the value society places on an additional unit of consumption of an individual), the fiscal cost of participation responses, the local shape of the earnings distribution, and the intensive-margin elasticity of earnings with respect to the net-of-tax rate.

10. Household data for the UK are combined with a detailed description of the UK tax and benefit system. Data on earnings, employment status, and family structure come from the UK Family Resources Survey (FRS) 2023–24. UKMOD is then used to apply the main parameters of the current UK tax and benefit system and to construct disposable income, participation tax rates, and marginal effective tax rates across the earnings distribution. The analysis focuses on the working-age population and maps the joint effect of taxes and transfers—including Personal Income Tax (PIT), National Insurance contributions (NICs), Universal Credit (UC), and non-means-tested benefits such as Child Benefit (CB)—into marginal effective tax rates (METR). These METRs capture the full incentive wedge created by both higher taxes and the withdrawal of benefits as earnings rise.

11. The calibration combines externally chosen parameters for labor-supply elasticities and social preferences inferred from the existing tax-benefit schedule. The baseline assumes an average intensive-margin elasticity of 0.15 and an average extensive-margin elasticity with respect to in-work income of 0.25 with a declining profile in income, with participation responses lowest for high-income workers (Table 1). $^{4}$ These values are taken from Adams and Phillips (2013) and are broadly within the range of estimates used in the empirical literature, albeit toward the lower end of that range. $^{5}$ In section E, we test the robustness of our results to these assumptions by increasing the elasticities used by 25 and 50 percent. Social marginal welfare weights are recovered using an inverse-tax approach: conditional on the assumed elasticities, the current UK schedule of marginal effective tax rates is inverted to infer the redistributive preferences that would have generated the same system (Bourguignon and Spadaro 2012; Jacobs, Jongen and Zoutman 2017). The non-linear reform scenarios then solve for alternative marginal tax schedules under different revenue targets, tracing the trade-offs between revenue, aggregate labor supply, and redistribution.

Table 1. United Kingdom: Participation Elasticities by Income Groups

<table><tr><td></td><td>Adams and Phillips (2013)</td><td>Baseline calibration</td></tr><tr><td>Lowest 20 percent</td><td>0.50</td><td>0.49</td></tr><tr><td>Next 20 percent</td><td>0.31</td><td>0.37</td></tr><tr><td>Middle 20 percent</td><td>0.21</td><td>0.21</td></tr><tr><td>Next 20 percent</td><td>0.14</td><td>0.13</td></tr><tr><td>Highest 20 percent</td><td>0.06</td><td>0.08</td></tr><tr><td colspan="3">Notes: Participation elasticities are defined as the percent change in the participation rate resulting from a percent change in in-work income. Adams and Phillips (2013) Table E.2.</td></tr></table>

## D. Simulation Results

12. Three parametric labor tax reform scenarios are constructed. The simulations are based on the current tax and benefit system (that is, before the extension of the income tax threshold freezes currently planned) and consider changes to the marginal effective tax rates (rather than changes to specific income tax or NIC rates) which better capture the joint effect of changes to taxes and benefits. Each scenario is designed to shed light on the implications of tax increases for revenue potential, labor market responses (as proxied by aggregate labor supply $^{6}$ ), and equity considerations. The scenarios are as follows:

\- Scenario 1: Uniform tax increase. Under this scenario, the marginal effective tax schedule is increased uniformly across the distribution of earnings. In practical terms, this entails an upward shift of the METR line in Figure 2.A.

\- Scenario 2: Segmented tax increases. Instead of raising marginal tax rates uniformly for all ta

[中间内容因长度限制已省略]

o the right, implying more adverse earnings responses and lower revenue potential. This is a consequence of

placing a greater weight on the efficiency costs borne by high earners. Figure 4.B shows that around 5 percent in additional revenue could be achieved with an associated 6.5 percent reduction in labor supply.

20. The effects of alternative assumptions are highly non-linear. This reflects the complex interactions between behavioral responses and the desired progressivity of the tax system. In particular, small changes in elasticities or inequality aversion can lead to disproportionately large changes in optimal tax schedules and associated revenue and aggregate earnings outcomes, especially at the top of the income distribution. As a result, while the qualitative conclusions of the baseline analysis remain robust—namely that there is scope to improve the efficiency-equity trade-off through tax reform—the quantitative results are sensitive to these assumptions. Higher labor elasticities and a lower inequality aversion both tend to reduce revenue potential (as shown in Figures 4 A and B), albeit through different channels, and with different implications for labor supply. This highlights the importance of carefully calibrating these parameters when considering reform options.

## Figure 4. Robustness Scenarios

A. Revenue and Earnings Change of Non-linear Reforms Using Higher Labor Supply Elasticities (Percent)

Source: IMF staff calculations  
![](images/d8e387507973daaae51f897e303cce68c75f65c5204ceb862e6da498cb6cd55b.jpg)  
Notes: The chart shows changes to total earnings (vertical axis) and total revenue (horizontal axis) under non-linear reform scenarios.  
B. Revenue and Earnings Change of Non-linear Reforms Using Alternative Inequality Aversion Parameters (Percent)

![](images/704248b5671695dd99580891834282990016637bfa6e4a72ead26585b1f580a4.jpg)  
Source: IMF staff calculations  
Notes: The chart shows changes to total earnings (vertical axis) and total revenue (horizontal axis) under non-linear reform scenarios.

## F. Policy Conclusions

21. There is limited scope for new measures to raise significant additional revenue through labor taxation without significantly weakening labor supply. The baseline model simulations in this paper suggest that a uniform increase in marginal effective tax rates could raise some additional revenue but would come with substantial labor supply losses. This is because increasing marginal tax rates across the whole schedule would exacerbate existing distortions, including weak incentives to enter the labor market at the bottom of the distribution and high marginal effective tax rates in upper parts of the earnings distribution.

22. More fundamental reforms could deliver higher revenue gains while strengthening work incentives across the earnings distribution. Targeted increases in marginal tax rates towards the bottom of the earnings distribution, accompanied by more generous in-work transfers, would be more efficient, reflecting the size of the tax base affected, but would come with equity trade-offs. More fundamental reforms that improve work incentives in line with optimal tax design could deliver higher revenues with a better efficiency-equity trade-off. The results point to the benefits of strengthening incentives to work at the bottom of the distribution while reducing very high marginal effective tax rates at the top. In practice, this would require a broader redesign of the tax-benefit schedule, including smoothing benefit withdrawal and other threshold effects, rather than simply increasing headline rates of income tax or National Insurance contributions.

23. Against the backdrop of rising spending pressures, designing labor taxation in a way that both raises revenue and is consistent with the UK's growth agenda will be central. This requires moving beyond a narrow focus on headline tax rates and placing greater weight on how the tax-benefit system affects people's incentives to work and firms' incentives to hire. Broad-based rate increases would risk adding to existing distortions and weaken labor supply, while better-designed reforms that strengthen incentives to enter and progress in work could support both fiscal sustainability and stronger medium-term growth.

## References

Adam, S. and Phillips, D. (2013). "An ex-ante analysis of the effects of the UK Government's welfare reforms on labour supply in Wales" IFS Report No. R75.

Bourguignon, F., and Spadaro, E. (2012). "Tax-benefit revealed social preferences" Journal of Economic Inequality, 10: 75–108.

Brewer, M., Saez, E. and Shephard, A. (2010). "Means-testing and tax rates on earnings" in Dimensions of Tax Design: the Mirrlees Review, 1(4): 90-201.

Mirrlees, J. ed., 2011. Tax by design: The Mirrlees review. Oxford University Press (OUP) Oxford.

Piketty, T., and Saez, E. (2013). "Optimal labor income taxation" In Handbook of Public Economics, Volume 5, edited by Alan J. Auerbach, Raj Chetty, Martin Feldstein, and Emmanuel Saez, 391–474. Amsterdam: Elsevier.

Richiardi, M., Collado, D. and Popova, D., 2021. UKMOD-A new tax-benefit model for the four nations of the UK (No. CeMPA WP 7/21). CeMPA Working Paper Series.

Jacobs, B., Jongen, E.L., and Zoutman, F.T. (2017). "Revealed social preferences of Dutch political parties" Journal of Public Economics, 156, 81–100.

Jacquet, L, Lehmann, E. and Van der Linden, B. (2013) "Optimal redistributive taxation with both extensive and intensive responses" Journal of Economic Theory, 148 (5): 1770-1805.

Zoutman, F.T., Jacobs, B. and Jongen, E.L. (2013). "Optimal redistributive taxes and redistributive preferences in the Netherlands" Erasmus University Rotterdam.
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
