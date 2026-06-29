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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# The Fiscal Policy of Autonomous Communities: Its Macroeconomic Effects and the Role of the National Fiscal Rule

Carlo Pizzinelli

SIP/2026/054

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on May 4, 2026. This paper is also published separately as IMF Country Report No 26/103.

2026
JUN

![](images/b2e0bf17d3ed10fe00390eadf4be8b05c6fe5c8e77e481e8efab93c07281d6e2.jpg)

# IMF Selected Issues Paper European Department

# The Fiscal Policy of Autonomous Communities: Its Macroeconomic Effects and the Role of the National Fiscal Rule\* Prepared by Carlo Pizzinelli

Authorized for distribution by Romain Duval
June 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on May 4, 2026. This paper is also published separately as IMF Country Report No 26/103.

ABSTRACT: The transposition of the EU economic governance framework to national legislation provides an opportunity to reform the subnational fiscal rule, especially with regard to its regional component. While compliance by autonomous communities has improved in the last decade, the current framework has not delivered on two key objectives of subnational fiscal rules for regional governments: avoiding procyclical public spending and ensuring debt sustainability. This paper makes the case for centering a revised fiscal rule on an expenditure growth target—consistent with the formulation of the EU framework—to ensure that spending by regional governments, particularly on health and education, remains mostly acyclical while also achieving debt-stabilizing regional fiscal policy.

RECOMMENDED CITATION: Pizzinelli, C. (2026) “The Fiscal Policy of Autonomous Communities: It’s Macroeconomic Effects and the Role of the National Fiscal Rule.” IMF Selected Issues Paper (SIP/2026/054). Washington, DC. International Monetary Fund.

JEL Classification Numbers:

E61, E62, E32, H70

Keywords:

Fiscal Rules, Federalism, Fiscal Policy, Cyclicality

Author's E-Mail Address:

cpizzinelli@imf.org

# The Fiscal Policy of Autonomous Communities: Its Macroeconomic Effects and the Role of the National Fiscal Rule

Spain

Prepared by Carlo Pizzinelli $^{1}$

# THE FISCAL POLICY OF AUTONOMOUS COMMUNITIES: ITS MACROECONOMIC EFFECTS AND THE ROLE OF THE NATIONAL FISCAL RULE $^{1}$

The transposition of the EU economic governance framework to national legislation provides an opportunity to reform the subnational fiscal rule, especially with regard to its regional component. While compliance by autonomous communities has improved in the last decade, the current framework has not delivered on two key objectives of subnational fiscal rules for regional governments: avoiding procyclical public spending and ensuring debt sustainability. This paper makes the case for centering a revised fiscal rule on an expenditure growth target—consistent with the formulation of the EU framework—to ensure that spending by regional governments, particularly on health and education, remains mostly acyclical while also achieving debt-stabilizing regional fiscal policy.

## A. Introduction

1. Autonomous communities are a crucial component of fiscal policy in Spain. In 2021 Spain ranked third among OECD and EU economies for the size of public spending carried out by regional governments as a share of GDP—approximately 18 percent—and fifth as regards regions' share of total public sector expenditure—approximately 27 percent (OECD, 2024). This large percentage is explained by the autonomous communities' responsibility for delivering several essential public services, including education, health, long-term care, and some other forms of social assistance.

2. Regional public spending is supported by an institutional framework aiming to balance risk-sharing, redistribution, autonomy, and fiscal responsibility. Under the “common regime”, applied to 15 communities, regional governments receive resources from a selection of taxes over which they have some ability to adjust rates, and have full autonomy over other taxes. Part of the revenues, together with additional transfers from the central government, are pooled into a set of funds that redistribute resources across regions to mitigate disparities in financing per capita. Meanwhile, the two communities under the “foral regime” (Navarra and País Vasco) pay a negotiated contribution to the general government’s budget but retain the entirety of their tax collections. Autonomous communities can also finance spending by issuing debt. While some communities issue bonds and receive loans from banks, several of them finance part or the entirety of their debt through central-government sponsored vehicles, collectively denominated Fondos de Financiación Autonómica. These were established in 2014, originally as emergency instruments, to ensure access to credit at contained interest rates for all communities in the wake of the Global Financial Crisis (GFC) and the subsequent euro area crisis. Finally, a subnational fiscal rule sets yearly targets for communities' deficits, primary spending growth, and debt levels to safeguard fiscal sustainability and align regional budgets to the government's overall fiscal strategy.

![](images/507aa55125ee36789f4090607fbbd482d99870ddfc49e6a7f5200278cbf7c463.jpg)

3. Autonomous communities have historically been large contributors to Spain's fiscal deficit and debt (Figure 1). Prior to the GFC, the consolidated regional government sector regularly achieved a close-to-balanced budget, and its total debt remained stable at around 5 percent of GDP. From 2008 to 2019, however, the primary (overall) balance of autonomous communities was mostly negative, with a peak deficit of 4.6 (5.1) percent of GDP in 2011. As a result, regional debt rose pronouncedly, edging close to 25 percent of GDP in 2016. Since then, the consolidated deficits have decreased in size, with several individual communities reaching surpluses. With the exception of 2020, the first year of the COVID-19 pandemic, regional debt has declined every year, but challenges remain. By end-2025, total debt—including that issued via the government-sponsored funds—remained above 20 percent of GDP. This level amounts to a fifth of Spain's total public sector debt and is significantly above the long-term debt anchor of 13 percent envisioned in Spanish law (Organic Law 2/2012). Moreover, given their purview of health and long-term care services, autonomous communities will bear a substantial share of the large aging-related fiscal pressures that Spain is projected to face over the coming decades.

4. Overhauling the subnational fiscal rule would be a crucial step to strengthen the medium-term orientation and credibility of fiscal policy in Spain. The subnational fiscal rule is underpinned by the Organic Law on Budget Stability and Financial Sustainability 2/2012 (LOEPSF, for its Spanish name). The multiplicity of fiscal targets under the current subnational rule, as set out under the LOEPSF, has historically led to inconsistencies in the fiscal position of different communities, and compliance with its targets has been partial. Moreover, while compliance has improved over the last decade, the framework has not delivered on two key goals of subnational fiscal rules: stabilizing debt and avoiding procyclical fiscal policy. Additionally, as noted by AIReF (2025), the methodology for setting yearly targets on spending growth is not aligned with that of

the new EU economic governance framework, which became operational in 2025, leading to potential conflicts in the fulfillment of both rules. The need to align the subnational framework to the EU one therefore provides an opportunity to revise the former in order to better align it with optimal principles of regional fiscal policy and better tailor it to the nature of spending conducted by autonomous communities in Spain.

5. This paper provides new insights in support of a revised fiscal rule for autonomous communities centered on expenditure growth limits. Given their primary focus on essential public services, the expenditures of autonomous communities should remain decoupled from business cycle fluctuations. Deficit-based rules, while in principle preserving debt sustainability, would lead to procyclical spending that could exacerbate recessions and hinder long-term growth through cuts to education and health, as was the case in the GFC. Moreover, due to their limited debt-carrying capacity, autonomous communities are not well placed to conduct active countercyclical fiscal policy, as large deficits may quickly result in high debt financing costs, and the central government can in principle step in and fulfill this macroeconomic stabilization role. A viable solution would therefore be a rule centered on expenditure growth that ensures debt sustainability for individual regions, either through region-specific spending growth limits or through a common one with tighter adjustment requirements for high-debt regions whose debt is above a certain threshold—such as the 13 percent of GDP limit envisioned in the current debt rule. To further reduce the risk of procyclical spending cuts, the central government should ensure that its transfers to autonomous communities do not fall during downturns. The rule should also entail a clear and applicable corrective arm in the event of non-compliance, enforced by the Ministry of Finance.

6. The paper makes the case for an expenditure target through both descriptive and econometric analysis. Section B discusses the basic principles of fiscal federalism and subnational fiscal rules, relating them to the Spanish context. It highlights the case of the GFC to stress the need to prevent procyclical spending and the importance of debt sustainability. Sections C and D apply econometric techniques to more formally assess the historical conduct of fiscal policy by autonomous communities over 2004–2024. The analysis finds that regional public spending was positively correlated with the business cycle—falling in downturns, particularly in the aftermath of the GFC—and that most regions failed to stabilize their debt dynamics over this period. Moreover, Spain’s strong procyclicality of spending on health and education—the communities’ main responsibilities—is at odds with the experience from peer euro area countries, where it is mostly acyclical, as warranted. Section E discusses Spain’s current subnational fiscal rule, set out by the LOEPSF, examining regions’ historical compliance and highlighting the inherent inconsistency between the yearly deficit and spending growth targets. Section F considers key issues in the design of an expenditure-based fiscal rule for Spain’s regions, drawing also from two recent proposals by AIReF (2025) and Martínez-López and others (2026).

7. The finances of autonomous communities have been the subject of significant analysis, particularly after the GFC and the euro area crisis. For instance, Fernández-Llera (2011) and Pérez and Prieto (2015) present early analysis of regional debt, while Canuto and Liu (2013) place the Spanish case in the comparative context of other countries in the wake of the GFC. More recently, Marín-González and Martínez-López (2024) provide an in-depth analysis of historical drivers of regional debt. Moreover, the yearly fiscal performance and budget execution of communities has been highly studied and tracked by academics and think tanks (e.g., see for instance de la Fuente, 2025). Several works point to the importance of examining regional finances in the broader context of national fiscal policy in Spain (Hernández de Cos and Pérez, 2013). Studies thus considered the limited coordination of fiscal effort (Lledó, 2015), spillovers from the fiscal stance of the central government (Molina-Parra and Martínez-López, 2018), the role of extraordinary liquidity funds that allow for soft budget constraints (Herrero-Alcalde and others, 2019; Calvo-López and Cadaval-Sampedro, 2022), and the spending responsibility of regions on essential services, which tend to be prioritized over debt reduction (Marín-González and Martínez-López, 2026).

8. Several studies have also examined the historical track record of compliance with the subnational fiscal rule and the implications for fiscal policy. Agrimón and Hernández de Cos (2012) examine an earlier version of the national fiscal rule, in place between 1992 and 1998, finding that it did not have significant effects on regional fiscal balances. Leal and López-Laborda (2015), Lago-Peñas and others (2016), and Delgado Téllez and others (2017) study econometrically the drivers of non-compliance with the objectives of the fiscal rule, finding that a variety of “hard” and “soft” factors matter. Among the former are the ambitiousness and volatility of the targets, exogenous growth shocks, and the persistence of non-compliance (i.e., a track record of low compliance decreases the likelihood of meeting current targets, all else equal). Among the latter are political-economy factors such as soft budget constraints, the degree of fiscal autonomy, and changes in the political affiliations of regional governments. Martínez-López (2020) points to the reduced efficacy particularly of the debt and spending rules of the LOEPSF, as well as the limited enforceability of the rule’s corrective mechanisms. More recently, however, Herrero-Alcalde and others (2022) find that, despite partial compliance, the expenditure rule has to some extent helped contain growth in current and primary expenditure.

## B. Principles of an Enhanced Subnational Rule in the Context of Spain's Spending Areas

9. Autonomous communities account for the majority of public sector expenditure in health and education in Spain (Figure 2, left panel). $^{2}$ The central administration, on the other hand, concentrates its spending on economic development, public administration, and defense and security. Finally, the social security administration and local governments (i.e., municipalities) have more specialized functions such as pensions and local security, respectively, and, in the case of the latter, represent a smaller share of total spending. This distribution of responsibilities is well aligned with theories of optimal federal spending (Oates 1972, 1999), whereby central authorities are best placed to address macroeconomic stabilization and deliver country-level public goods like national defense, while territorial governments should focus on the provision of services that may require

tailoring to the needs and preferences of their populations. Although spending in health and education is mostly comprised of wages and social transfers, autonomous communities also account for approximately half of all capital spending (amounting to 1.6 percent of GDP) concentrated under economic affairs and general public service programs (Figure 2, right panel). $^{3}$

![](images/6ce7fa0a05fac3c4c6c5a0f65bf0ed2d96e2395c129c5ed243c6a80627fae813.jpg)  
Note: The left plot reports average spending as a share of GDP over 2022–2024. The right plot reports the average composition of spending by autonomous communities in different programs by its economic classification over 2022–2024.

10. Autonomous communities' spending should not fluctuate significantly over the business cycle. Health and education are crucial for fostering long-term economic growth but do not have strong macroeconomic stabilization functions, as they generally have lower short-run multipliers (Atolia and others, 2017) and are mostly determined by inelastic demand for essential services. Hence, they do not lend themselves well to countercyclical spending. At the same time, procyclical spending in these areas should also be avoided, as health and education services provision should not be diminished or discontinued due to macroeconomic circumstances, and evidence shows that cuts in health and education during downturns can lengthen the duration of the recession—a phenomenon called hysteresis—and inflict long-lasting scars on human capital and potential output (Jackson and others, 2021). These spending programs should therefore remain

acyclical, while still contributing to debt sustainability and fiscal consolidation efforts by following predictable multi-year trajectories and through spending efficiency reviews. $^{4}$

11. In turn, to maintain stable spending through the business cycle, autonomous communities require a combination of debt-issuance capacity and stability in revenue sources. Some access to debt markets, allows communities to maintain stable (acyclical) spending on essential services when revenues decline due to cyclical shocks. However, while autonomous communities can issue debt in the form of bonds and loans, their overall debt-carrying capacity is more limited than that of the national government. $^{5}$ Therefore, acyclical spending also requires that, during economic upswings, revenue surpluses be devoted to debt repayments rather than increased provision of services above initial plans. Moreover, the more stable revenues are, the less likely it is that communities need to issue debt to finance spending. In particular, transfers from the central

![](images/343d22b994c95d9583f99d8a2dac48029c66c99265e31eea53e514137aa20673.jpg)  
Sources: IGAE, INE, and IMF staff calculations.
Note: Net transfers are computed as transfers (current and capital) from other public sector entities minus transfers to other public sector entities (current and capital) minus 50 percent of the central government's VAT revenues minus 58 percent of the central government's revenues of alcohol, tobacco, and hydrocarbons excise taxes, and minus 100 percent of the central government's revenues of electricity excise taxes.

government should remain stable and predictable, if not actively offsetting fluctuations in communities' own tax revenues, whose bases fluctuate with the business cycle.

12. The experience of the Global Financial Crisis (GFC) and euro area crisis in Spain illustrates how limited debt issuance capacity and unstable revenues can result in procyclical spending by regions. The consolidated revenues of autonomous communities began to slow down in 2007, driven primarily by lower tax revenues, while net transfers from the central government remained stable at first and eventually rose (Figure 3). Spending continued to rise over 2007–2009, outgrowing revenues and leading to an in

[中间内容因长度限制已省略]

Liquidaciones</td><td></td><td></td><td></td><td>0.007(0.007)</td><td></td><td></td><td></td><td>0.002(0.008)</td><td></td><td></td><td></td><td>0.007(0.007)</td></tr><tr><td>Observations</td><td>300</td><td>340</td><td>357</td><td></td><td>300</td><td>340</td><td>357</td><td></td><td>300</td><td>340</td><td>357</td><td></td></tr><tr><td>Number of CAs $^{1}$ </td><td>15</td><td>17</td><td>17</td><td></td><td>15</td><td>17</td><td>17</td><td></td><td>15</td><td>17</td><td>17</td><td></td></tr><tr><td>IV 1: Neighbors&#x27; GDP</td><td>YES</td><td>YES</td><td>-</td><td>YES</td><td>YES</td><td>YES</td><td>-</td><td>YES</td><td>YES</td><td>YES</td><td>-</td><td>YES</td></tr><tr><td>IV 2: Trading Partners GDP</td><td>YES</td><td>-</td><td>YES</td><td>YES</td><td>YES</td><td>-</td><td>YES</td><td>YES</td><td>YES</td><td>-</td><td>YES</td><td>YES</td></tr><tr><td>Foral Communities</td><td>NO</td><td>YES</td><td>YES</td><td>YES</td><td>NO</td><td>YES</td><td>YES</td><td>YES</td><td>NO</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>First-Stage F-stat</td><td>225.1</td><td>423.8</td><td>318.6</td><td>264</td><td>225.1</td><td>423.8</td><td>318.6</td><td>264</td><td>225.1</td><td>423.8</td><td>318.6</td><td>264</td></tr><tr><td>P-val</td><td>0.00</td><td>0.00</td><td>0</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0</td><td>0.00</td></tr><tr><td>R Sq. - Between</td><td>0.247</td><td>0.322</td><td>0.0141</td><td>0.0497</td><td>0.239</td><td>0.310</td><td>0.0230</td><td>0.0461</td><td>0.329</td><td>0.390</td><td>0.0474</td><td>0.00240</td></tr><tr><td>R Sq. - Within</td><td>0.0250</td><td>0.0257</td><td>0.0241</td><td>0.0289</td><td>0.0319</td><td>0.0330</td><td>0.0298</td><td>0.0359</td><td>0.0657</td><td>0.0654</td><td>0.0590</td><td>0.0736</td></tr></table>

Robust standard errors in parentheses  
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

Sources: IGAE, INE, and IMF staff calculations.

<table><tr><td>VARIABLES</td><td>(1) Total Expenditure</td><td>(2) Primary Expenditure</td><td>(3) Public Consumption</td></tr><tr><td>Regional GDP</td><td>0.238***(0.049)</td><td>0.295***(0.052)</td><td>0.284***(0.024)</td></tr><tr><td>GFC * Regional GDP</td><td>2.694***(0.320)</td><td>2.984***(0.322)</td><td>1.413***(0.209)</td></tr><tr><td>Constant</td><td>0.004***(0.000)</td><td>0.004***(0.000)</td><td>0.003***(0.000)</td></tr><tr><td>Observations</td><td>340</td><td>340</td><td>340</td></tr><tr><td>Number of id</td><td>17</td><td>17</td><td>17</td></tr><tr><td>IV 1: Neighbors&#x27; GDP</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>IV 2: Trading Partners GDP</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>First-Stage F-stat</td><td>264</td><td>264</td><td>264</td></tr><tr><td>P-Val.</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>R Sq. - Between</td><td>0.109</td><td>0.110</td><td>0.0816</td></tr><tr><td>R Sq. - Within</td><td>0.158</td><td>0.175</td><td>0.133</td></tr><tr><td colspan="4">Robust standard errors in parentheses*** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1</td></tr></table>

<table><tr><td>VARIABLES</td><td>(1) Total Expenditure</td><td>(2) Primary Expenditure</td><td>(3) Public Consumption</td></tr><tr><td>D% Regional GDP</td><td>0.152*</td><td>0.176*</td><td>0.151**</td></tr><tr><td></td><td>(0.091)</td><td>(0.099)</td><td>(0.062)</td></tr><tr><td>Constant</td><td>0.016***</td><td>0.015***</td><td>0.020***</td></tr><tr><td></td><td>(0.003)</td><td>(0.004)</td><td>(0.002)</td></tr><tr><td>Observations</td><td>340</td><td>340</td><td>340</td></tr><tr><td>Number of CAs&#x27;</td><td>17</td><td>17</td><td>17</td></tr><tr><td>IV 1: Neighbors&#x27; GDP</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>IV 2: Trading Partners GDP</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>First-Stage F-stat</td><td>169.9</td><td>169.9</td><td>169.9</td></tr><tr><td>R Sq.</td><td>0.009</td><td>0.011</td><td>0.024</td></tr><tr><td colspan="4">Robust standard errors in parentheses</td></tr><tr><td colspan="4">*** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1</td></tr></table>

Sources: IGAE, INE, and IMF staff calculations.

Annex I. Table.4. Spain: System-GMM Specification with Arellano-Bond Instruments of Expenditure for the Panel Regression of Expenditure on the Cyclical Component of Real GDP

<table><tr><td>VARIABLES</td><td>(1) Total Expenditure</td><td>(2) Primary Expenditure</td><td>(3) Public Consumption</td></tr><tr><td>Regional GDP - Detrended</td><td>0.149***(0.047)</td><td>0.173***(0.050)</td><td>0.200***(0.025)</td></tr><tr><td>Total Expenditure t-1</td><td>0.701***(0.016)</td><td></td><td></td></tr><tr><td>Primary Expenditure t-1</td><td></td><td>0.681***(0.015)</td><td></td></tr><tr><td>Public Consumption t-1</td><td></td><td></td><td>0.756***(0.021)</td></tr><tr><td>Constant</td><td>0.004***(0.000)</td><td>0.004***(0.000)</td><td>0.004***(0.000)</td></tr><tr><td>Observations</td><td>340</td><td>340</td><td>340</td></tr><tr><td>Number of CAs&#x27;</td><td>17</td><td>17</td><td>17</td></tr><tr><td>P-val of AB Test for AR-1</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>P-val of AB Test for AR-2</td><td>0.14</td><td>0.33</td><td>0.27</td></tr><tr><td>P-val Hansen J test</td><td>0.09</td><td>0.09</td><td>0.13</td></tr><tr><td colspan="4">Robust standard errors in parentheses*** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1</td></tr><tr><td colspan="4">System GMM specification with both fist-differences and level equation; moment conditions for the lag dependent variables include lags 2 to 10. Instruments for regional GDP growth include growth of neighboring regions and Spain&#x27;s trading partner growth.</td></tr></table>

Sources: IGAE, INE, and IMF staff calculations.
"""
