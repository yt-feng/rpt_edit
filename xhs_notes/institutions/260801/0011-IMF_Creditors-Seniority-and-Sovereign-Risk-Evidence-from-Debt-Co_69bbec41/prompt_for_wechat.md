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
# Creditors' Seniority and Sovereign Risk: Evidence from Debt Composition

Prepared by Chiara Ferrero, Sansan Vincent de Paul Kambou, Kady Keita
WP/26/161

IMF Working Papers describe policy-related analysis and research being developed by IMF staff members and are published to elicit comments and to encourage debate. The views expressed in Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/d1a81056c4a8d4ebca0b8ab8b877d1c4aeaa07bdd8ea90f312b8ba7d6e697c71.jpg)

<table><tr><td>JEL Classification Numbers:</td><td>F34, G15, H63</td></tr><tr><td>Keywords:</td><td>Sovereign default; Debt crisis; Market access; Bonds spreads; Creditors compositions; Debt Seniority</td></tr><tr><td>Authors’ email addresses:</td><td>cferrero@IMF.orgkkeita2@IMF.orgvincentdepaulkambou@gmail.com</td></tr></table>

# IMF Working Paper Finance Department

# Creditors' Seniority and Sovereign Risk: Evidence from Debt Composition

Prepared by Chiara Ferrero, Sansan Vincent de Paul Kambou, Kady Keita

Authorized for distribution by Joseph Thornton
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper shows that creditor composition has economically meaningful implications for both the likelihood of sovereign debt crises and access to international capital markets. A central finding is the asymmetric role of IMF lending relative to other creditor groups. We show that debt owed to the IMF and the World Bank is, on average, the most senior, followed by debt owed to official bilateral creditors. Private creditors, notably bondholders and commercial banks, are on average junior to official creditors, with commercial banks being the least prioritized group for repayments. Beyond characterizing the seniority hierarchy, our empirical analysis shows that creditor composition has economically meaningful implications for sovereign risk. Our results show that IMF credit outstanding as a share of Gross National Income (GNI) is robustly and negatively associated with the probability of a debt crisis, with this stabilizing effect weakening progressively as debt stocks rise. Turning to sovereign borrowing costs, we find that IMF lending is negatively associated with sovereign bond spreads.

RECOMMENDED CITATION: Ferrero C., Kambou S. V. P., Keita K. (2026): “Creditors Seniority and Sovereign Risk: Evidence from Debt Composition” IMF Working Paper No WP/26/161.

WORKING PAPERS

# Creditors Composition and Sovereign Risk: Evidence from Debt Composition

Prepared by Chiara Ferrero, Sansan Vincent de Paul Kambou, Kady Keita $^{1}$

## Table of Contents

Table of Contents....2   
1. Introduction....4   
2. Data....6 Figure 1: Scatter Plots of Sovereign Bond Spreads and Debt Composition by Creditor Type....7   
3. Evidence on the Seniority Structure of Debt....8 Figure 2: Composition of Sovereign External Debt by Creditor Group....8 Measuring Seniority....9 Stylized Facts on Seniority....10 Figure 3: Creditors' RPDs (Overall sample)....12 Figure 4: Creditors' RPDs (Low- and middle-income countries)....12   
4. Creditor Composition and Sovereign Risk: Empirical Strategy and Results....14 Creditor Composition and Debt crises....14 Table 1 : Baseline Estimates of the Effect of Creditor Composition on Debt Crises....16 Table 2: IV-Estimates of the Effect of Creditor Composition on Debt Crises....18 Table 3: Non-Linear Effects of IMF Credit Outstanding on Sovereign Debt Crises....20 Creditors Composition and Market Access....20 Sovereign bonds spreads....20 Table 4: Baseline Estimates of Creditor Seniority's Impact on Bonds Spreads....22   
5. Robustness Tests....24 Alternative samples....24 Table 5: Robustness Tests with Alternative Sample....24 Additional controls....25 Alternative estimation Methods....26   
6. Conclusion....27   
Appendices....28 Appendix A....28 Table A1: Overview of control variables....28 Table A2: Descriptive statistics....29 Table A3: Share of Senior Debt and the Sovereign Debt Crisis....29 Table A4: Share of Senior Debt and Borrowing Costs....30 Figure A1: Analysis of Creditors' RPDs in Countries with an IMF Program....31 Figure A2: Analysis of Creditors' RPDs in Countries During Financial Crises....32 Figure A3: Percentile distribution of external debt stock as % of GNI....32 Appendix B....33

Table B1: Robustness Test - Additional controls .... 33
Table B2: Robustness Test - Additional controls .... 33
Table B3: Robustness Test - Alternative estimation methods .... 34
References.... 36

## 1. Introduction

Global debt as share of GDP peaked at 258 percent of GDP in 2020 during the COVID emergency, and decreased afterwards, remaining however at levels higher than pre-COVID $^{2}$ . As nations face high levels of public debt, the role of the composition of debt, particularly the hierarchy between senior and subordinated claims, is crucial to understand debt dynamics that can affect the cost of accessing new credit as well as the sustainability of debt.

The hierarchy between senior and subordinated claims, or the seniority structure of debt, refers to the priority with which creditors are repaid when a debtor country is unable to repay all obligations on time. The legal and de facto seniority structure of debt may differ, with the de facto structure being dependent not only on the legal contracts, but also on established conventions. Schlegl et al. (2019) have provided evidence on the de facto seniority structure of debt. The authors show that sovereign borrowers selectively default on their creditors, and they find that the IMF and multilateral creditors hold the most senior status, while unexpectedly finding that bilateral official loans are treated as less senior than Bonds creditors. The latter finding differs from the general convention that bilateral official loans are at least as senior as private loans, in line for example with the comparability of treatment principle of the Paris Club.

Given potential differences in how countries prioritize repayments to different creditors, the composition of debt could affect the cost of new credit and the outcome of debt restructuring negotiations. Indeed, the manner of restructuring negotiations is not independent of the creditor hierarchy, as it may be affected by the presence of preferred creditors, the share of senior debt in the total debt stock, and the need, during periods of severe stress, to preserve sources of financing that could continue to lend when markets withdraw.

As a result, the composition of debt by creditor type can be an important determinant of sovereign risk, although existing theoretical and empirical literature has documented an ambiguous effect of creditors seniority on sovereign financing. On one hand, the intervention of multilateral creditors can play a catalytic role by facilitating access to financing during crises (Corsetti et al., 2006; Boz, 2011). On the other hand, an excessive share of senior debt can lead to a subordination effect, increasing the risk premiums demanded by junior creditors (Dell’Erba et al., 2013; Steinkamp and Westermann, 2014). The works of Broner et al. (2014) illustrate the potential conflicts and inefficiencies generated by the presence of multiple creditors with various seniority statuses, which can lead to debt crises. Additionally, the models of Diamond & Rajan (2001) and Gennaioli et al. (2014) demonstrate how seniority can influence market liquidity and exacerbate financial crises during times of stress. This perspective is complemented by the analysis of Arellano & Ramanarayanan (2012), which considers the effect of a country's reputation on its financing costs and access to credit, taking into account the debt structure. In the European context, Steinkamp and Westermann (2014) have shown that an increase in the share of multilateral loans in public debt is correlated with a rise in sovereign bond spreads, reflecting an increased risk premium for subordinate creditors. These findings are particularly relevant for developing economies, where dependence on official creditors is more marked and access to financial markets may be more volatile (Saravia, 2010). Sometimes, this dependence prompts governments to austerity to avoid high restructuring costs, although in some cases, increased senior debt can lead to more lenient fiscal policy (Corsetti & Dedola, 2016; Cheelo et al., 2023). Corsetti and Dedola's (2016) modeling underscores this idea, finding that creditor seniority can not only affect borrowing costs but also alter the incentives of states to generate budget surpluses or restructure their debt during crises.

Building on this literature, our paper empirically revisits the de facto seniority structure of debt and investigates how the composition of debt by creditor type can impact countries' likelihood to experience debt crises and their ability to tap international capital markets.

By exploiting disaggregated debt data from 119 emerging markets and developing economies from 1980 to 2022, we show that on average the IMF and the World Bank are the most senior creditors. Unlike in the results of Schlegl et al. (2019), we find that sovereigns facing repayment difficulties are more likely to default on private claims, such as bondholders or commercial banks, than on official bilateral creditors. Commercial banks in turn are the least likely to see their repayments prioritized. The seniority of bilateral creditors is in line with general convention, which draws from the Paris Club principles on comparability of treatment, the G20 Common Framework, and the important role of bilateral lenders during crises.

Our empirical results show that while a positive conditional correlation exists between debt from other creditor groups and the likelihood of a debt crisis, this is not true in the case of an increase in debt outstanding to the IMF as share of Gross National Income (GNI) $^{3}$ . The mitigating effect of IMF loans on the likelihood of debt crisis remains significant for countries with debt stock surpassing 100 percent.

Moreover, the results show that an increase in borrowing from the IMF is associated with an improvement in market access proxies, as measured by bond spreads. Instead, an increase in borrowing from more junior creditors is associated with an increase in bonds spreads. The estimation of this impact however, may be affected by selection bias, as countries' characteristics may affect both their access to markets and the composition of their debt. While we are able to address this issue in the case of IMF borrowing with an instrumental variable strategy, the case of other multilateral creditors and other lending comprises different rules and agencies and addressing the bias is less straightforward, and the subject of further research on this topic.

The remainder of the paper is organized as follows: Section 2 describes the data. Section 3 introduces new evidence regarding the seniority structure of debt. Section 4 describes our empirical strategy and the results of the analysis. Section 5 delves into robustness tests to validate the reliability of our findings. Finally, Section 6 concludes by summarizing our main findings.

## 2.Data

This analysis uses annual data spanning the period from 1980 to 2022, including 119 emerging market and developing economies. We categorize external creditors into five distinct groups based on the World Bank's classification as used in the International Debt Statistics: (i) bilateral creditors; (ii) multilateral institutions, excluding the IMF; (iii) bondholders $^{4}$ ; (iv) long-term commercial bank loans and credits, which include syndicated bank loans and supplier credits extended by exporters and other vendors of goods; and (v) the International Monetary Fund (IMF) $^{5}$ . We use data on debt stocks from IDS, and debt defaults from the BoC-BoE sovereign default database (see Beers et al., 2023). In the context of the IMF, the BoC-BoE sovereign default database generally reports payments overdue for at least 6 months as payments in arrears, although the IMF has ultimately never incurred ultimate losses on its loans as even in instances of delayed payments, the IMF has eventually been repaid. $^{6}$

To measure sovereign risk, we employ a dummy variable indicating sovereign debt crises as defined by Laeven and Valencia (2020). $^{7}$ We use bond yield spreads from the J.P. Morgan EMBIG index $^{8}$ , and data on sovereign ratings, calculated using the average ratings from the three primary credit rating agencies: Moody's, Fitch, and Standard & Poor's (S&P). $^{9}$ Additionally, our analysis incorporates a range of control variables, including GDP per capita, GDP growth, the VIX index, which measures expected stock market volatility, the ratio of short-term debt to total external debt, a dummy variable for prior debt restructurings, a dummy variable indicating banking crises, and foreign direct investment (FDI) flows, among others. Tables A1 and A2 in the Appendix provide a detailed overview of all the variables used in our analysis, accompanied by descriptive statistics.

To provide an initial descriptive overview, Figure 1 complements the summary statistics by providing descriptive evidence on the relationship between sovereign bond spreads and the composition of external debt. The simple pairwise correlations point to some differences across creditor groups. IMF debt is weakly negatively correlated with EMBI spreads, while multilateral debt excluding the IMF is essentially uncorrelated with spreads. By contrast, bilateral debt displays a more pronounced negative correlation with spreads, whereas private debt is positively correlated with sovereign spreads. Although purely descriptive, these patterns are consistent with the paper's broader argument that creditor composition is associated with different market perceptions of sovereign risk. These figures should not, however, be interpreted as evidence of causality, since debt composition itself may be shaped by underlying macroeconomic conditions and market access.

Figure 1: Scatter Plots of Sovereign Bond Spreads and Debt Composition by Creditor Type  
![](images/2215230a8f140394f5e17f0f618b3d7465d907427356b8756e4eadd866795bfd.jpg)

![](images/4a565518703bc67e61e700c6d3596a8ecf61c142c7a2d2b2db28ca90a9b6d085.jpg)

![](images/de9b55a9681b16936daec291e5e6e2e4426988257beafc8c2df93f463404fc31.jpg)

![](images/bff1ebd74341b7afb7e13dda52aace3b09600d2446b3904d5d0dd2235af66b12.jpg)  
Source: Authors' calculations based on data from the World Bank's International Debt Statistics (IDS) and J.P. Morgan's Emerging Markets Bond Index Global (EMBIG).

## 3.Evidence on the Seniority Structure of Debt

The distribution of creditors has undergone significant changes over the last 45 years. The 1990s were marked by a notable increase in the share of bonds relative to bank loans and commercial credits, particularly following the Brady debt restructuring agreements. Although bilateral creditors and the IMF experienced a slight decline after the 1990s, the overall share of official lending, including other multilaterals, has remained broadly steady. As shown in Figure 2, new lenders such as China have also strengthened their role.

Figure 2: Composition of Sovereign External Debt by Creditor Group  
![](images/63342e5360ee6eebc46959a32034a2e1ff0ba1638ec4b590ddaa89d5426ca36b.jpg)  
Source: Authors' calculations based on data from the World Bank's International Debt Statistics (IDS)

Against this backdrop, we look at whether creditors' treatment has also changed over time. Traditionally, multilateral institutions such as the IMF and the World Bank have enjoyed senior creditor status, followed by bilateral creditors grouped within the Paris Club and private creditors (bondholders and commercial banks). The seniority of the IMF and of multilateral creditors is usually supported by the Paris Club, with multilateral credit excluded from restructuring. The de-facto senior status is seen as supporting the stabilizing role of multilateral institutions, perceived as lenders of last resort (Fischer, 1999 and Steinkamp and Westermann, 2014). In addition, the IMF and WB have implemented policies on arrears that regulate lending to countries in arrears (IMF, 2015 and 2022).

However, seniority of creditors may have changed over time, as creditors implemented policies to deal with arrears, the international financial system evolved, new creditors like China increased their global role, and a succession of systemic shocks (2008 crisis, Covid-19 pandemic) took place. $^{10}$ In the following, we empirically evaluate the seniority of the main groups of lenders over time.

## Measuring Seniority

Recent research by Schlegl et al. (2019) has explored the treatment of creditors in default scenarios. The authors propose two indicators to evaluate seniority, based on arrears to different types of creditors (relative percentage of amounts in arrears indicator) and on the magnitude of creditors' losses, and provide empirical evidence confirming that multilateral institutions like the IMF and World Bank are senior creditors. However, the authors find that, contrary to conventional understanding, bilateral creditors are not senior to private creditors. The authors also find that the average haircut on official creditors' debt is higher than the one on private creditors.

Building upon this research, we replicate the relative percentage of amounts in arrears indicator computed in Schlegl et al. (2019) using the BoC-BoE data on defaults (while the authors use arrears data obtained from the World Bank's Debt Reporting System). The BoC-BoE database classifies as defaults cases in which “debt service is not paid on the due date or within a specified grace period or payments are not made within the period specified under a guarantee”. $^{11}$ This does not imply that payments are not eventually made, in the case of IMF, as mentioned above, loans have historically been ultimately repaid, so the dataset includes payments with reported protracted delays $^{12}$ . The indicator includes two elements: the first component (A) reflects the absolute scale of sovereign defaults per unit of loan from a specific creditor group, for a given country, and the second component (B) measures the absolute scale of sovereign defaults per unit of loan of all creditors, for a give

[中间内容因长度限制已省略]

4), 503-526.

Easterly, W. (2005). What Did Structural Adjustment Adjust? The Association of Policies and Growth with Repeated IMF and World Bank Adjustment Loans. Journal of Development Economics, 76(1), 1-22.

Eaton, J., & Gersovitz, M. (1981). Debt with Potential Repudiation: Theoretical and Empirical Analysis. Review of Economic Studies, 48(2), 289-309

Edwards, S. (1986). The Pricing of Bonds and Bank Loans in International Markets: An Empirical Analysis of Developing Countries' Foreign Borrowing. European Economic Review, 30(3), 565-589.

Fischer, S. (1999). On the Need for an International Lender of Last Resort. Journal of Economic Perspectives, 13(4), 85-104.

Fuchs, A., & Gehring, K. (2017). The Home Bias in Sovereign Ratings. Journal of International Money and Finance, 77, 1-22.

Gelpern, A. (2004). Building a better seating chart for sovereign restructurings. Emory LJ, 53, 1115.

Gelpern, A., Horn, S., Morris, S., Parks, B., & Trebesch, C. (2023). How China lends: A rare look into 100 debt contracts with foreign governments. Economic Policy, 38(114), 345-416.

Gennaioli, N., Martin, A., & Rossi, S. (2014). Sovereign default, domestic banks, and financial institutions. The Journal of Finance, 69(2), 819-866.

Gehring, K., & Lang, V. (2020). Stigma or cushion? IMF programs and sovereign creditworthiness. Journal of Development Economics, 146, 102507.

Hatchondo, J. C., Martinez, L., & Sapriza, H. (2017). Debt Dilution and Sovereign Default Risk. Journal of Political Economy, 125(5), 1388-1422.

Horn, S., Reinhart, C. M., & Trebesch, C. (2021). China's overseas lending. Journal of International Economics, 133, 103539.

Horn, S., Reinhart, C. M., & Trebesch, C. (2022, May). Hidden defaults. In AEA Papers and Proceedings (Vol. 112, pp. 531-535). 2014 Broadway, Suite 305, Nashville, TN 37203: American Economic Association.

IMF (2015). The IMF's Lending Framework and Sovereign Debt—Further Considerations. IMF Policy Paper.

IMF (2022). Reviews of the Fund's Sovereign Arrears Policies and Perimeter. IMF Policy Paper.

Jeanne, O., & Zettelmeyer, J. (2001). International Bailouts, Moral Hazard, and Conditionality. Economic Policy, 16(33), 409-432.

Jordà, Ó. (2005). Estimation and Inference of Impulse Responses by Local Projections. American Economic Review, 95(1), 161-182.

Jorra, M. (2012). The Effect of IMF Lending on the Probability of Sovereign Debt Crises. Journal of International Money and Finance, 31(4), 709-725.

Laeven, L., & Valencia, F. (2012). Systemic Banking Crises Database: An Update. IMF Working Paper, WP/12/163.

Laeven, L., & Valencia, F. (2020). Systemic Banking Crises Revisited. IMF Working Paper, WP/2020/133.

Lang, V. (2021). The economics of the democratic deficit: The effect of IMF programs on inequality. The Review of International Organizations, 16(3), 599-623.

Marchesi, S., & Thomas, J. P. (1999). IMF Conditionality as a Screening Device. Economic Journal, 109(454), 111-125.

Nelson, S. C. (2014). The Currency of Confidence: How Economic Beliefs Shape the IMF's Relationship with Its Borrowers. Cornell University Press.

North, D. C. (1990). Institutions, Institutional Change and Economic Performance. Cambridge University Press.

Nunn, N., & Qian, N. (2014). U.S. Food Aid and Civil Conflict. American Economic Review, 104(6), 1630-1666.

Obstfeld, M., Shambaugh, J. C., & Taylor, A. M. (2010). Financial Stability, the Trilemma, and International Reserves. American Economic Journal: Macroeconomics, 2(2), 57-94.

Panizza, U., Sturzenegger, F., & Zettelmeyer, J. (2009). The Economics and Law of Sovereign Debt and Default. Journal of Economic Literature, 47(3), 651-698.

Reinhart, C. M., & Rogoff, K. S. (2011). This Time Is Different: Eight Centuries of Financial Folly. Princeton University Press.

Rodrik, D., & Velasco, A. (1999). Short-Term Capital Flows. Annual World Bank Conference on Development Economics, 1999, 59-90.

Roubini, N., & Setser, B. (2003). The US as a Net Debtor: The Sustainability of the US External Imbalances. Journal of Economic Perspectives, 17(4), 177-198.

Saravia, D. (2010). On the role and effects of IMF seniority. Journal of International Money and Finance, 29(6), 1024-1044.

Schlegl, M., Trebesch, C., & Wright, M. L. J. (2019). The Seniority Structure of Sovereign Debt. NBER Working Paper, No. 25793.

Sinha, P. (2015). Government Debt and Economic Growth: Decomposing the Cause and Effect Relationship. Journal of Economic Policy Reform, 18(1), 17-37.

Steinkamp, S., & Westermann, F. (2014). The Role of Creditor Seniority in Europe’s Sovereign Debt Crisis. Economic Policy, 29(79), 495-552.

Steinkamp, S., & Westermann, F. (2017). Multilateral loans and interest rates: further evidence on the seniority conundrum. International Journal of Finance & Economics, 22(2), 169-178.

Stock, J. H., & Yogo, M. (2005). Testing for Weak Instruments in Linear IV Regression. In Identification and Inference for Econometric Models: Essays in Honor of Thomas Rothenberg (pp. 80-108). Cambridge University Press.

Stone, R. W. (2002). Lending Credibility: The International Monetary Fund and the Post-Communist Transition. Princeton University Press.

Thacker, S. C. (1999). The High Politics of IMF Lending. World Politics, 52(1), 38-75.

Tirole, J. (2002). Financial Crises, Liquidity, and the International Monetary System. Princeton University Press.

Trebesch, C., & Zabel, M. (2017). The Output Costs of Hard and Soft Sovereign Default. European Economic Review, 92, 416-432.

Trebesch, C. (2019). The Lender of Last Resort: IMF Programs and Sovereign Borrowing. NBER Working Paper, No. 26091

![](images/ceff60d629c93ec9149f6d60937f0f855b6752b47851492c71abc4809cae6ebb.jpg)

## PUBLICATIONS
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
