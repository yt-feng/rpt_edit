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
- 已识别机构名：`国际货币基金组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际货币基金组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Brazil's VAT Reform: Improving Equity

Ana Cebreiro Gomez and Christina Kolerus

WP/26/132

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN

![](images/f6dac0c44ccd859f192bf6bffe85e515a6c231bc9b0b66a81bed900ac65edf1f.jpg)

# IMF Working Paper WHD and FAD

Brazil's VAT Reform: Improving Equity Prepared by Ana Cebreiro Gomez and Christina Kolerus\*

Authorized for distribution by Daniel Leigh and Alexander Klemm
June 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: After decades in the making, Brazil's landmark VAT reform was approved in 2023. The primary objective of the reform is to eliminate distortions and reduce the complexity of the current consumption tax system while maintaining revenue neutrality. In addition, specific design features were included to alleviate the VAT's inherent regressivity and improve the equity of the Brazilian tax system. This paper assesses the reform's expected equity print leveraging a microstatic model based on household data and simulates policy options to further improve distributional outcomes. While the new VAT achieves a fairly equal distribution of the tax burden across most income groups, the poorest still carry a heavier load in terms of their disposable income. Dissecting the impact by policy instrument, the reform's approved reduced rates aggravate regressivity, while zero rates and the new cashback lower the tax burden for poorer households, under the revenue neutrality assumption. Overall, the combined use of these measures dampens the reform's equity outcomes somewhat as a higher VAT reference rate is required on all other items to maintain revenue neutrality. The paper also shows that some equity improvements stem from the reform's implied pivot towards taxing services. Finally, simulations show that focusing on and expanding the cashback could amplify equity gains by raising the poorest disposable income by 25 percent via reductions in their tax liability.

JEL Classification Numbers:

H21, H22

Keywords:

VAT reform; equity analysis; microstatic simulations

Author's E-Mail Address:

acebreirogomez@imf.org; ckolerus@imf.org

WORKING PAPERS

# Brazil's VAT Reform: Improving Equity

Prepared by Ana Cebreiro Gomez and Christina Kolerus $^{1}$

## Contents

Contents 4

Introduction 5

Status quo and key reform features 7

Brazil's current tax system 7

The 2023 vat reform \_\_\_\_ 11

Equity analysis 14

Data and methodology 14

The distributional pattern of reform policies 15

Policy options to further improve equity 20

Robustness 23

Conclusion 25

References 30

## BOXES

1. Brazil’s Subnational Revenue Collection 10

2. Scenario Map 16

## FIGURES

1. Tax Burden and Structure 8

2. Pre-reform Average Tax Liability by Income Decile 11

3. Old and New Consumption Taxes 12

4. Number of VAT Rates Across Countries 13

5. Consumption per Decile 14

6. Post-reform Average Tax Liability By Decile 18

7. Equity Impact by Policy Instrument 19

8. Services Shift 20

9. Expanding the Cashback 22

10. Relaxing Revenue Neutrality 23

11. Robustness 24

## TABLE

1. Progressivity Indicators 21

## ANNEXES

I. Existing Taxes on Goods and Services 26

II. Reform Laws 27

III. Reform Policy Settings 28

IV. Supplementary Figures 29

## Introduction

After more than three decades in the making, Brazil's landmark VAT reform was approved in 2023. The reform merges five taxes on goods and services (PIS/COFINS, IPI, ICMS, ISS), $^{2}$ raised across three levels of government, into a dual value added tax and an excise. A constitutional amendment was approved at the end of 2023, followed by complementary legislation that defines rates and details on implementation in 2024 and 2025. Implementation will start in 2026 and be completed in 2033 while some compensation funds for Brazil's states will remain in place for almost 50 years. The current design foresees a general rate of 28 percent, $^{3}$ a zero rate for most basic goods of the so-called Cesta Basica, reduced rates on selected goods, and a cashback mechanism for the poorest, partially reimbursing VAT paid (with full reimbursement of water and sewage, cooking/natural gas, energy and telecommunications at the federal level). The new excise would be strictly limited to products harmful to health and environment, including alcohol, sweet beverages, combustion engines, cigarettes, and lottery.

The primary objective of the reform is to eliminate distortions and reduce complexity of the current consumption tax system while maintaining revenue neutrality. Taxation of goods and services in Brazil is one of the most complex worldwide giving rise to wide-spread and deep-rooted distortions. Cascading taxes, due to overlapping bases and incomplete credits for intermediate inputs, and tax competition among states have led to a profound misallocation of factors of production in the economy, with negative repercussions particularly for the manufacturing sector. High compliance costs and opportunities for tax avoidance have given rise to substantial legal uncertainty as well as significant compliance gaps translating into high statutory tax rates. By replacing the existing consumption taxes with a dual VAT (a full-fledged VAT with a two-tier structure), aligning tax bases across municipalities, states, and the federal level, and harmonizing the administration of the new tax, the reform would significantly reduce complexity and boost efficiency and transparency. Maintaining revenue neutrality $^{4}$ would require a relatively high statutory tax rate of 28 percent, but the tax burden would be distributed more evenly across states and sectors, accompanied by important improvements in revenue administration (Cebreiro et al. 2025). This, in turn, would facilitate compliance and reduce administrative costs, and diminish tax treatments' heterogeneity, which would unleash important productivity gains (Cavalcanti et al 2024). The reform would further boost output by eliminating consumption taxes on intermediate inputs, which would improve the allocation of production factors (Domingues and Freire Cardoso 2020 and Badel and Kolerus 2025).

In addition, the new VAT has the potential to improve the equity of the Brazilian tax system and contribute to reducing Brazil's high levels of inequality. While revenue neutrality would imply a continued high burden from indirect taxation, which typically weighs more heavily on lower income households, several factors would mitigate the VAT's inherent regressivity. $^{5}$ First, at the business level, increased simplicity and

lower compliance costs would have a relatively stronger impact on smaller businesses, given the fixed-cost nature of these costs (IMF, 2023; Coolidge, 2012; Coolidge, 2010). Higher productivity and rising wages in formal firms would further improve incentives for formalization (De Paula and Scheinkman, 2010, Badel and Kolerus, 2025). In addition, the reform allows firms under the SIMPLES regime to opt into the dual VAT regime, i.e. claim input tax credits (ITC) and continue benefiting from SIMPLES for other (income and profits) tax purposes. $^{6}$ Second, the reform allows for zero (and reduced) rates for a number of goods and services more strongly represented in consumption baskets of lower income households. Third, the shift in the tax burden from goods to services, a consequence of harmonizing tax bases and eliminating cascading, would benefit lower income households more given their greater reliance on goods consumption. And finally, the introduction of the cashback mechanism grants a direct possibility to support vulnerable households.

A broad-based literature evaluates equity considerations of the abovementioned tax design features. A first strand of literature assesses the regressivity of VAT. While indirect taxes are commonly known to exert a relatively higher burden on lower-income households, there are variations in terms of the underlying metric used. When the VAT burden is measured as percentage of income for a single year, several studies find that the VAT is highly regressive (e.g., Lustig, Pessino and Scott, 2014, Leahy et al., 2011; Ruiz and Trannoy, 2008; O'Donoghue et al., 2004). However, other studies show that VAT regressivity declines when taking into consideration savings, which increase with income and often materialize as deferred income that will be subject to taxation in the future (e.g., Swistak et al., 2015; IFS, 2011a; Creedy, 1998; Metcalf, 1994), and informality, which decreases as household expenditure increases (Bachas et al., 2023; Jenkins et al., 2006). Moreover, the VAT is found proportional, and even progressive, when the burden is measured relative to expenditure rather than income (e.g., Thomas, 2022a; Bird and Smart, 2016; IFS, 2011a; Metcalf, 1994). A second strand of literature looks into distributional aspects of VAT policy design. In most countries, VAT systems include exemptions and zero and reduced rates on certain products that are typically consumed disproportionately by poorer households to address regressivity concerns $^{7}$ . However, ample theoretical and empirical evidence find little support for these measures to address income redistribution. In particular, seminal theoretical literature shows a weak case for reduced VAT rates when other, more direct instruments are available such as personal income taxes (e.g., Atkinson and Stiglitz, 1976; Christiansen, 1984; Edwards et al., 1994). In addition to vertical equity concerns (redistribution), IFS (2011) note that multi-rate VAT systems could also raise horizontal equity concerns (different treatment for identical households) due to different consumption patterns (for reduced vs general-rated goods and services) in otherwise identical households. $^{8}$ On the other hand, targeted cash transfers have been proven as a more efficient policy instrument to deliver support to low-income households, including Corbacho et al. (2013) for Costa Rica, Mexico and Uruguay; Cseres-Gergely et al. (2017) for Hungary; Van Oordt (2018) for South Africa; Warwick et al. (2022) for Ethiopia, Ghana, Senegal, Sri Lanka, Uzbekistan and Zambia; and Thomas (2024) for OECD countries. Finally, combining targeted cash transfers with a broad based, single-rate VAT allows reaping the benefits from efficient taxation while compensating the most vulnerable (Warwick et al., 2022; de Mooij and Keen, 2013; Mirrlees, 2011). Moreover, when these compensations are received in real time at the moment of purchase (e.g. facilitated by a digital mechanism), a progressive VAT system can be achieved (Swistak and De la Feria, 2024).

This paper assesses the 2023 reform's expected equity outcomes and simulates policy options to further improve distributional outcomes. Using the World Bank's SimVat tool calibrated with Brazilian data from the 2018 PNAD household survey and adjusted with the latest reform parameters for tax rates and cashback, the paper evaluates the impact of the reform's policies on household income and consumption. As the new VAT system combines exemptions, zero and reduced rates on certain goods and services and introduces a cashback system, the relative impact of each measure is being assessed. The paper builds on Lara Ibarra et al 2021 and Vale et al 2023, and applies the latest reform policies as approved by Parliament (including law LC 214/2025), notably on exemptions, zero and reduced rates, excises, and cashback. By means of microstatic simulations, the paper further assesses the equity implications of the shift from goods to services taxation, leveraging findings from Cebreiro et al 2025, and simulates alternative policy settings to improve equity considerations, including relaxing the revenue neutrality condition.

Findings. First, the new VAT would result in a relatively equitable distribution of the tax burden for lower- to middle-income households, albeit the poorest still carry the heaviest load in terms of disposable income. Second, dissecting the impact by policy instrument, the reform's policy settings for reduced rates worsen the VAT's regressivity, while zero rates, mainly applied to Cesta Basica products disproportionately consumed by lower-income households, reduce the tax burden of the bottom three deciles by 7 percent of their income compared with a full VAT without concessions. The introduction of the new cashback represents an important relief for poorer households lowering their tax liability by almost 10 percent of their income relative to a full VAT. Overall, the reform's equity gains remain somewhat moderate given the combined use of the various measures, as a higher VAT reference rate is needed to compensate for the associated revenue loss from VAT concessions to maintain revenue neutrality. Third, some equity gains from the reform are not directly linked to policy instruments but result from shifting the tax burden from manufactured goods to services, which, given consumption patterns, levies the richest households the most. Fourth, to further improve equity, simulations show that targeting the poorest with an expanded cashback, while removing other concessions, would improve their household income by 25 percent (via tax reduction) and allow for a lower reference rate. Fifth, relaxing revenue neutrality and aligning revenue collection closer with peers improves regressivity relative to income but not relative to consumption.

The paper is structured as follows. First, the design features of the reform are summarized, describing the status quo as well as the approved policy changes. Second, data and assumptions are presented. Third, the equity impact of the reform settings is analyzed. Fourth, simulations to further improve distributional outcomes with and without revenue neutrality are conducted. Section five concludes.

## Status Quo and Key Reform Features

## Brazil's Current Tax System

Brazil's tax system has historically heavily relied on the taxation of good and services. Total tax revenues to GDP in Brazil, at 32 percent in 2023, are among the highest in Latin America and the Caribbean (LAC), reaching levels close to the OECD average of 34 percent in 2023 (Figure 1). Moreover, Brazil raises most tax revenues from charges on consumption of goods and services (41 percent of total revenue and 13 percent of GDP in 2023). $^{9}$ The heavy reliance on indirect taxes, jointly with the relatively low contribution of personal income taxes to total tax revenues, reduces the potential progressivity of the overall tax system. $^{10}$ This is further aggravated by the significant weight of social security contributions and payroll taxes (8.6 percent of GDP, close to the OECD average 9.2 percent), which are typically applied in form of a flat rate on all formal incomes.

Figure 1. Tax Burden and Structure Tax-to-GDP Trend (1990-2023)  
![](images/b7a15e73723eb6babb1b71f23774ebc366ce121e3ce6c4ca723070fb008dcf7e.jpg)

Consumption Tax Revenues by Sector Percent of GDP

![](images/80d8fb2a8e9a8a69124c61d51c843567e9cec3b7a0317772ef7de3e6be34446a.jpg)

Tax Structure: Comparing Brazil with Latin America and OECD Averages, 2023 (Percent of GDP)  
![](images/12ca9957068e0240f81159cefb081d43efd3ec9c761ee057750f8c658ce857dd.jpg)  
Notes: LAC includes Caribbean countries while LAT only Latin American countries.  
Source: OECD Global Revenue Statistics 2025, Cebreiro et al, 2025.

In addition, the consumption tax system is highly complex, giving rise to important distortions and a significant compliance gap, further pushing up tax rates to achieve the desired collection. With five

different taxes across three levels of Government (PIS/COFINS, IPI, ICMS, ISS $^{11}$ -- see Annex I for details), rates can vary among the federal government, 26 states, and 5,568 municipalities, reflecting approximately 10 general tax rates and more than 300 differentiated rates and exemptions. This complexity raises many efficiency concerns and, at the same time, undermines productivity, growth and revenue potential. It further acts as an obstacle for formalization and SME growth as fixed costs of filing taxes weigh more heavily on smaller firms. $^{12}$ In addition, cascading taxes due to overlapping bases (which lead to cumulative taxes, largely based on origin rather than destination principle) $^{13}$ and incomplete credits for intermediate inputs distort the allocation of factors of production in the economy. Taken together, these factors translate into high statutory tax rates, in particular on goods, which disproportionately affect poorer household's disposable income.

Brazil's federal system also plays a role in explaining the heavy tax burden on consumption. Brazil is highly decentralized, and important public goods are directly provided by its states and municipalities (Box 1). Consequently, Brazil's subnational governments dispose of wider revenue collection powers than most peers in other federal economies. Combined state and municipal total tax revenues (29.6 percent of total revenue in 2022) are close to Germany and significantly higher than in other countries in the region. However, while other federal countries rely on a broader mix of taxes (including labor income and profits), most of Brazil's subnational revenues (90 percent) are raised via taxes on goods and services. Raising revenues on sales is constitutionally protected and became a politically viable way to balance subnational budgets, given states' more limited access to income taxation, and higher administrative costs of other taxes (e.g. property) at given revenue collection capacity. With rising expenditures, subnational governments increased their sales tax collections in tandem.

The current system of indirect taxation is substantially regressive. This regressivity is driven by (i) high combined tax rates; (ii) a biased taxation of goods relative to services; and (iii) numerous concessions that disproportionately benefit middle- and upper-income households. A range of studies show that households in the poorest decile of the income distribution face a consumption tax liability of 20-45 percent of their monetary income, compared with around 10 percent for the richest decile. The estimated di

[中间内容因长度限制已省略]

pment in the Americas, Inter-American Development Bank. New York: Palgrave Macmillan

de la Feria, R. and M. Walpole, 2020. The Impact of Public Perceptions on General Consumption Taxes. British Tax Review 67/5, 637-669.

de la Feria, Rita, 2025. Tax Fairness: reconceptualizing Taxation and Inequalities, in R. de la Feria (Ed.) Taxation and Inequalities, Amsterdam: IBFD.

de la Feria, R. and A. Swistak, 2024. Designing a Progressive VAT. IMF Working Paper No. 2024/078, International Monetary Fund.

de Mooij, R.; Hebous, S., and Keen, M., 2025. Efficiency Aspects of the Value Added Tax; IMF Working Papers WP/25/165, International Monetary Fund.

Domingues, E. P. and D. Freire Cardoso, 2020. Simulações dos impactos macroeconômicos, setoriais e distributivos da PEC 45/2019. Mimeo CciF

Ebrill, L., M. Keen, J.-P. Bodin and V. Summers, 2001. The Modern VAT. Washington, DC: International Monetary Fund.

Evans, C., P. Lignier, and B. Tran-Nam, B., 2013. Tax compliance costs for the small and medium enterprise business sector: Recent evidence from Australia [Discussion Paper: 003-13]. Tax Administration Research Centre Seminar, University of Exeter Business School.

Fenochietto, Ricardo and Juan Carlos Benítez, 2021. “Encouraging Formal Invoicing and Reducing the VAT Impact on Low-Income individuals”, IMF Working Paper No. 2021/040.

Guilherme Giglio, G. and Natale, M., 2020. The long expected Brazilian tax reform – objectives, challenges and pitfalls. International Tax Review, March 30, 2020.

Gupta, R., & Sawyer, A., 2014. Tax compliance costs for small businesses in New Zealand: Some recent findings [Conference presentation]. Australasian Tax Teachers' Association, Griffith University, Brisbane.

Hill Collins, P. and Bilge, S., 2020. Intersectionality. Polity Press.

IFC, 2010. Tax Compliance Cost Surveys, Investment Climate in Practice, International Finance Corporation.

IMF, 2023. How to Design a Presumptive Income Tax for Micro and Small Enterprises; How to Note 2023/002.

IFS, 2011, “Assessing Existing Rate Structures” in IFS et al., A retrospective evaluation of elements of the EU VAT system, Report prepared for the European Commission, TAXUD/2010/DE/328.

Insper, 2020. “Contencioso tributário no Brasil, Relatório 2019 - Ano de referência 2018”, July.

Keen, Michael, and Ruud A. de Mooij, 2012. Fiscal Devaluation and Fiscal Consolidation: The VAT in Troubled Times. IMF Working Papers 12/85, International Monetary Fund.

Kumar, A.S., and Dash, S.K., 2022. Impact of GST on inflation: Evidence from Bayesian causal analysis, GIFT Discussion Paper 2022/03, GIFT, Thiruvananthapuram, India.

Lara Ibarra, Gabriel & Rubião, Rafael Macedo & Simoes Fleury, Eduardo, 2021. Indirect Tax Incidence in Brazil: Assessing the Distributional Effects of Potential Tax Reforms, Policy Research Working Paper Series 9891, The World Bank.

Mathew, S. and Kumary, A., 2025. GST Implementation in India: some Unresolved Issues; GIFT Discussion Paper Series 1/2025; Gulati Institute of Finance and Taxation Thiruvananthapuram, Kerala, India.

Mattos, E., Rocha, F., and Toporcov, P., 2013. Programas de Incentivos Fiscais São Eficazes? Evidência a Partir da Avaliação do Impacto do Programa Nota Fiscal Paulista Sobre a 44 Arrecadação de ICMS Revista Brasileira de Economia, Rio de Janeiro v. 67 n. 1 / p. 97–120 Jan-Mar.

Mirrlees J. (Ed.), 2011. Tax by design: The Mirrlees review. Oxford: Oxford University Press.

Orair, R.O. and S. W. Gobetti, 2019. Reforma Tributária e Federalismo Fiscal: uma análise das propostas de crialão de um novo imposto sobre of valor adicionado para o Brasil. IPEA discussion text 2530. December

Paiva, L. H., L. Bartholo, P. Ferreira de Souza and R. O. Orair, 2021. A reformulação das transferências de renda no Brasil: simulações e desafios, IPEA preliminary publication.

Palomo, T., Bhering, D., Scot, T., Bachas, P., Barcarolo, L., Campos, C., Feinmann, J., Moreira, L. And Zucman, G., 2025. Tax Progressivity and Inequality in Brazil: Evidence from Integrated Administrative Data. EU Tax Observatory, Report No. 9, August 2025.

Sandford, C., Godwin, M., Hardwick, P., & Butterworth, M., 1981. Costs and benefits of VAT. Heinemann Educational Books.

Sandford, C., Godwin, M., & Hardwick, P., 1989. Administrative and compliance costs of taxation. Fiscal Publications.

SERT, 2024. Estimativas atualizadas após o envio da proposta de regulamentação da Reforma Tributária - 1/7/2024. Secretaria Extraordinária da Reforma Tributária do Ministério da Fazenda (SERT/MF)

Skatterverket, 2006. Compliance costs of value-added tax in Sweden (Report No. 3B). Swedish Tax Agency, Ministry of Finance.

Swistak, A., S. Wawrzak and A. Alinska, 2015. In Pursuit of Tax Equity: Lessons from VAT Rate Structure Adjustment in Poland. Financial Theory and Practice 39 (2), 115-137.

Swistak, A., de la Feria, R., and Warwick, R., 2026. VAT Equity; Chapter V in The Future of the VAT, IMF.

Thomas, A., 2024. VAT Rate Structures in Theory and Practice. World Bank Policy Research Working Papers, No. 10677.

Thomas, A., 2022. Reassessing the regressivity of the VAT. Fiscal Studies, 43(1), 23-38.

Vale, R., G. Lara Ibarra, E. Fleury, and K. Trzcinski, 2023. Distributional Impacts of Brazil's Tax Reform: scenarios regarding Cesta Básica exemption. World Bank Poverty and Equity Notes, October 2023

Varsano, R., 2001. “Tributação Cumulativa, Distorção a Erradicar”. Boletim de Conjuntura n. 53. Rio de Janeiro: IPEA. April, pp. 57-59.

Wei, F. and Wen, J-F., 2019. “The Optimal Turnover Threshold and Tax Rate for SMEs.” IMF Working Paper WP/19/98. Washington: International Monetary Fund.

![](images/b6f58ec1fb82e8c1d4319a477653930b84a7e755fc9351821c3f6047ff93cb05.jpg)
"""
