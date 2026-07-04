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
# Dynamic Effects of Fiscal Rules Do Initial Conditions Matter?

Antonio Fatás

Bram Gootjes

Joseph Mawejje

POLICY RESEARCH WORKING PAPER 11066

## Abstract

Fiscal rules have been shown to support fiscal discipline by improving government budget balances and restraining the growth of debt. However, questions remain about what enhances their effectiveness and how certain conditions help to build the credibility needed for their survival and success. Using data from 108 countries between 1984 and 2012, this paper studies the dynamic effects of fiscal rule adoption. It shows that although fiscal rules generally improve the primary balance, their effects depend on the time horizon under consideration and the context of adoption. In advanced economies and countries with strong political institutions, the effects strengthen over time. Conversely, in emerging markets and developing economies—especially those with weaker institutions—their impact tends to fade as time passes. The findings highlight the critical role of economic conditions and consensus building at the time of adoption. Specifically, fiscal rules introduced in times of economic hardship or under highly concentrated political power are often less effective in the medium term.

# Dynamic Effects of Fiscal Rules: Do Initial Conditions Matter?

Antonio Fatás\*, Bram Gootjes\*\* and Joseph Mawejje\*\*

JEL classification: E62; H30; H62
Keywords: Fiscal Policy; Fiscal Rules; Initial Conditions; State dependence; Institutions; Local Projections

\* INSEAD, CEPR, and ABFER. \*\* World Bank, USA

## 1. Introduction

Over the last decades, fiscal sustainability concerns have intensified across the globe because of increasing government debt levels in both advanced and developing economies (Kose et al. 2021). At the same time, fiscal policy has gained prominence as a tool for macroeconomic stabilization, particularly in response to large global shocks, when monetary policy alone proves insufficient to counter recessions. However, to deploy fiscal policy effectively during downturns, governments must maintain adequate fiscal space to respond without compromising the long-term sustainability of public finances.

To promote fiscal policies that ensure sustainability while allowing their stabilization role, numerous countries have implemented fiscal rules. These rules impose constraints on fiscal policy by setting specific limits on budgetary aggregates (Schaechter et al. 2012). Early rules primarily focused on either the government's fiscal balance or the extent of its debt accumulation. In recent times, a growing number of countries have also adopted expenditure rules. $^{1}$ While fiscal rules were first adopted predominantly by advanced economies, developing countries have rapidly followed suit in the past few decades (Caselli et al. 2022; Davoodi et al. 2022). Today, fiscal rules have become the de facto benchmark for fiscal policy worldwide.

There is ample evidence in the academic literature highlighting the benefits of fiscal rules. Earlier studies have shown that fiscal rules can lower fiscal deficits (Debrun et al. 2008; Caselli and Reynaud 2020), curtail the accumulation of public debt (Azzimonti, Battaglini, and Coate 2016; Strong 2023), diminish sovereign bond spreads (Iara and Wolff 2014), and constrain political budget cycles (Gootjes, de Haan, and Jong-A-Pin 2021). However, the impact of fiscal rules is not uniformly positive, as it varies among different objectives and across countries (Bova et al. 2014; Ardanaz and Izquierdo 2022). For instance, the effectiveness of fiscal rules is often shaped by country-specific factors, including the amount of budget transparency provided by the government and quality of political and financial institutions (Beetsma et al. 2019; Gootjes and De Haan 2022a). At the same time, design features such as the flexibility embedded within the rules or a strong statutory basis have been shown to be more conducive to fostering fiscal discipline (Guerguil, Mandon, and Tapsoba 2017; Asatryan, Castellón, and Stratmann 2018). Therefore, welldesigned fiscal rules, supported by strong governance and institutions, are essential for ensuring effective fiscal discipline.

While the literature on fiscal rules is vast, certain aspects key to their effectiveness have not received sufficient attention. In particular, we have limited understanding of how the effects of fiscal rules develop over time. $^{2}$ Most studies estimate the average effects of fiscal rules, sometimes accounting for specific conditions. However, this approach implicitly assumes that these effects remain constant in both the short and medium-to-long term—an assumption that is unlikely to hold. Credibility, a cornerstone for the success of a fiscal rule, takes time to develop. Furthermore, over time, the conditions that led to the adoption of the rule may have changed, potentially weakening the motivation of governments to stick to the rule's constraint(s). The evolution of fiscal rule effectiveness likely depends on country-specific characteristics, offering valuable insights into how these factors shape medium-to-long term outcomes. For example, better governance structures and higher-quality institutions may enhance the effectiveness of fiscal rules by helping to build the credibility necessary to ensure their long-term survival. In contrast, the absence of such institutional support may yield only short-to-medium term effects.

Studying the dynamic effects of fiscal rule adoption also helps us understand whether initial conditions—the environment in which these rules are introduced—matter. The notion that initial conditions might influence the long-term success of fiscal rules can be inferred from the literature on economic reform. Several studies show that the origin of economic reforms, along with the political and economic conditions at the time of adoption, play a crucial role for their success (Rodrik 1996; Duval, Furceri, and Miethe 2020; Alesina et al. 2024; IMF 2024). The same logic can be applied to the environment in which fiscal rules are implemented. For instance, the effect of rules introduced during economic downturns may evolve differently compared to those implemented in more stable times. Likewise, fiscal rules adopted in a political climate of strong consensus may yield different effects than those established with limited political support. In their early survey of fiscal rules, Kopits and Symansky (1998) emphasized the importance of commitment and linked the effectiveness of these rules to the context in which they are introduced. However, empirical research has largely overlooked this aspect in subsequent studies. $^{3}$

In this paper, we examine the dynamic effects of fiscal rule adoption on fiscal policy in a large sample that includes both advanced and emerging market and developing economies (EMDEs). We address two key questions: First, how does the primary balance evolve following the adoption of fiscal rules? Second, do initial conditions influence the subsequent effectiveness of fiscal rules?

Our primary contribution to the literature lies in the careful examination of the dynamic effects of the adoption of fiscal rules. We complement existing research—which recognizes the positive effects of fiscal rules and the importance of the economic and political contexts—by refining its findings and uncovering patterns that become visible only when the dynamics of rule implementation are considered. We offer novel insights into the importance of conditions at the time of adoption, such as the state of the economy or the concentration of political power, demonstrating that fiscal rules succeed when adopted in some circumstances while struggling in others.

Specifically, our results show that the adoption of fiscal rules has a positive effect on the primary balance that gradually builds over time. Over a ten-year horizon, the primary balance has improved by about 1% of GDP. The dynamic effects are stronger in advanced economies and countries that are less dependent on commodity exports. For emerging markets and developing economies (EMDEs) and commodity exporters, we find evidence of positive short- to medium-term effects, but these effects tend to die out over time. Further analysis shows that stronger institutions support the effectiveness of fiscal rules across all country types, while in countries with weaker institutions, fiscal rules only lead to short-term improvements in the primary balance.

In addition, we find that the effects of fiscal rules adopted during periods of economic weakness tend to dissipate over time. This suggests that fiscal rule adoption is more likely to install long-term fiscal discipline when it is motivated by choice, and not distress or compulsion. Moreover, fiscal rules adoption is more effective when the distribution of seats between government and opposition parties is more balanced. This signals the importance of achieving broad consensus for effective implementation, a goal that is less necessary to achieve when the government holds greater political power. These results remain robust when we condition the model on situations where fiscal rule effectiveness is more likely, notably the presence of strong institutions. In sum, our findings suggest that while strong institutions are an important factor, they are not the only condition necessary for the successful adoption and sustainable effects of fiscal rules.

Our results are robust to a range of alternative model specifications that formally account for the Nickell Bias, heterogenous treatment effects, and endogeneity. The results are also robust when an alternative measure that purges cyclical effects from the primary balance is used. Further sensitivity analyses show that the design of fiscal rules does not drive our findings.

The paper is structured as follows. Section 2 provides a detailed review of the academic literature. Section 3 introduces the econometric methodology. Section 4 presents the baseline estimates of the dynamic responses of the primary balance to the introduction of fiscal rules and how they vary across different contexts. Section 5 focuses on how initial conditions matter for these dynamic responses. Section 6 presents a battery of robustness tests. Section 7 concludes.

## 2. Literature review

Fiscal rules have been in place for decades, but their widespread adoption occurred in an era where many countries had witnessed a worsening of fiscal sustainability. Japan was the first country (on record) to adopt a fiscal rule at the federal level, doing so in 1947. Over the following decades, other countries such as Malaysia (1959), the Netherlands (1961), Singapore (1965), Indonesia (1967), and Germany (1969) took similar action. There is no doubt, however, that the numerical constraints enshrined in the Maastricht Treaty of 1992, which laid the foundation for the creation of the Economic and Monetary Union (EMU), served as a catalyst for the global adoption of such rules (Figure 1). Given that the European Union (EU) comprises a group of advanced economies accounting for a large share of the global GDP, their adoption of fiscal rules represented both an experiment and a potential model for other countries to follow. It also generated a vigorous academic debate, yielding valuable insights on the effectiveness and optimal design of fiscal rules (Debrun et al. 2008; Hallerberg, Strauch, and Von Hagen 2007).

Figure 1: Adoption timeline of fiscal rules  
![](images/f2244d3eab3f5a5418743f143c8f009e683eb6dc4faf9a4d9f92d7b43b41b04b.jpg)  
Source: International Monetary Fund; Kopits and Symansky (1998).

The academic literature posits the origin of fiscal rules on the need to foster fiscal discipline and ensure debt remains on a sustainable path (Wyplosz 2013; Kopits and Symansky 1998). Accordingly, most fiscal rules take the form of numerical constraints on debt, fiscal balances, or budget components (Caselli et al. 2022). Beyond debt sustainability, fiscal discipline can also be understood more broadly. For example, fiscal rules may require governments to build buffers during times of economic expansion to be used for fiscal stimulus efforts during recessions. This type of discipline supports fiscal policies that optimize macroeconomic stabilization and helps reduce excessive fiscal policy volatility and procyclicality, both of which have been widely documented across many countries (Fatás and Mihov, 2003). The literature also tackles the issue of potential negative side effects of fiscal rules, such as how the same constraints that promote savings in good times could limit fiscal stimulus during periods of slow growth (Fatás and Mihov, 2010).

With a focus on US states, much of the earlier empirical literature on the effect of budgetary constraints found that fiscal rules provide discipline, reduce volatility, and improve the countercyclicality of fiscal policy (Alesina and Bayoumi 1996; Bohn and Inman 1996; Fatás and Mihov 2006). As more countries began adopting fiscal rules—in particular, EU countries in the run-up to the launch of the euro and the creation of the EMU—similar studies were conducted at the country level. $^{4}$ For instance, research demonstrates strong evidence that fiscal rules across EU member states have successfully reduced fiscal procyclicality (Debrun et al. 2008; Larch, Orseau, and Van Der Wielen 2021; Gootjes and De Haan 2022b). $^{5}$

In the EMU context, Debrun and Kumar (2009) make use of both case-study methodologies and panel regressions to show the disciplining effects of fiscal rules on the primary balance and public debt. However, they caution that some of these effects may be influenced by endogeneity: for example, rules may have been adopted by fiscally conservative governments that would have been disciplined even in the absence of a rule. Endogeneity can also work in the opposite direction, where fiscal rules are adopted by governments struggling to implement sound fiscal policy, making them more likely to fail in enforcing the rules effectively.

As more countries have adopted fiscal rules in the past few decades, research has increasingly provided evidence supporting their disciplining effect across a broad range of countries. Heinemann, Moessinger, and Yeter (2018) present a meta-regression analysis of 30 studies from the preceding decade. Their findings largely support the view that fiscal rules have a restraining effect on excessive policies, with a more significant impact on deficits than on debt or expenditures. Like in many studies in this field of literature, the authors acknowledge the possibility of endogeneity bias. This issue is sometimes addressed using instrumental variable (IV) analysis. For example, Caselli and Reynaud (2020), tackle causality by using an instrument based on the logic that the adoption of fiscal rules is influenced by their diffusion among neighboring countries. Their paper focuses on the budget balance and presents evidence of the effects of fiscal rules once the design of specific rules is considered.

The improvements in fiscal policy across a wide sample of countries can partly be attributed to the dual role of fiscal rules. $^{6}$ Beyond serving as a commitment device that constrains government actions and curtails discretionary fiscal measures, fiscal rules also act as a signaling mechanism. By explicitly communicating the government's fiscal intentions and strategies to the public and financial markets, fiscal rules bolster transparency and credibility in fiscal policy (Debrun and Kumar, 2007). This signaling effect has tangible benefits: fiscal rules have been demonstrated to improve market access for both advanced and developing economies by reducing sovereign risk premia and borrowing costs (Sawadogo 2020; Iara and Wolff 2014). $^{7}$

With a larger sample of countries, recent empirical studies have also been able to explore a broader set of issues related to fiscal rules, extending their analysis beyond direct measures of fiscal sustainability. For instance, fiscal rules have been shown to influence the patterns and composition of government spending by, for example, protecting investment and increasing the ratio of public investment to government consumption (Vinturis 2023). $^{8}$ There is also evidence that fiscal rules can improve government efficiency (Barbier-Gauchard, Baret, and Debrun 2023). Additionally, fiscal rules can reduce the vulnerability to sudden stops (Buda 2024), and also impact private domestic investment (Sawadogo 2024), with stronger effects in developing economies.

While fiscal rules are generally regarded as effective, their impact in EMDEs remains mixed. Much of the discussion here has centered on fiscal procyclicality, a notable challenge in the developing world (Gavin and Perotti 1997; Kaminsky, Reinhart and Végh 2004). On the one hand, studies have shown that fiscal rules help reduce fiscal procyclicality in the case of developing, low-income, and resource-rich countries (Céspedes and Velasco 2014; Bergman and Hutchison 2020; Mawejje and Odhiambo 2024). However, several other studies have found weaker to no evidence of this. For instance, Ardanaz and Izquierdo (2022) observe that fiscal rules have little impact on mitigating procyclical fiscal policy behavior in developing countries. Similarly, Bova, Carcenac, and Guerguil (2014) report limited effects of fiscal rules on procyclicality in emerging markets, and Bova, Medas, and Poghosyan (2016) find no evidence that the adoption of fiscal rules in resource-rich countries reduced the procyclicality bias in a significant way. Rather, the quality of political institutions emerges as a crucial factor in alleviating the procyclical nature of fiscal policy across these studies.

Studies comparing different types of rules, such as deficit, expenditure, or debt rules, have found mixed results. Other important dimensions, such as the flexibility of fiscal rules, have also been studied. For example, Guerguil, Mandon, and Tapsoba (2017) show that rules are linked to a small reduction in fiscal procyclicality, though not all rules produce the same results. In particular, deficit rules appear to have a strong effect, while flexible rules—especially those designed to shield investment—seem to be most successful. Ardanaz et al. (2021) find similar results, showing that flexibility in fiscal rules can create a growth-friendly environment by protecting investment from falling during episodes of fiscal consolidation. Likewise, the literature finds that some features of second-generation rules, such as cyclically adjusted targets and stronger e

[中间内容因长度限制已省略]

nomía, 16(1): 41-76.

Hallerberg, M., R. Strauch, R., and J. Von Hagen. 2007. “The Design of Fiscal Rules and Forms of Governance in European Union Countries.” European Journal of Political Economy, 23(2): 338-359.

Heinemann, F., M. Moessinger, and M. Yeter., 2018. “Do Fiscal Rules Constrain Fiscal Policy? A Meta-Regression-Analysis.” European Journal of Political Economy 51, 69–92.

Iara, A., and G. B. Wolff. 2014. "Rules and Risk in The Euro Area." European Journal of Political Economy 34, 222–236.

Ilzetzki, E., C. Reinhart and K. Rogoff. 2019. “Exchange Arrangements Entering the 21st Century: Which Anchor Will Hold?” Quarterly Journal of Economics 134, 599–646.

IMF (International Monetary Fund). 2009. Fiscal Rules—Anchoring Expectations for Sustainable Public Finances. Washington, DC.: International Monetary Fund.

IMF (International Monetary Fund). 2010a. “Guinea-Bissau: Enhanced Initiative for Heavily Indebted Poor Countries-Completion Point Document and Multilateral Debt Relief Initiative.” IMF Country Report No. 10/380, International Monetary Fund, Washington, DC.

IMF (International Monetary Fund). 2010b. “Liberia: Enhanced Initiative for Heavily Indebted Poor Countries-Completion Point Document and Multilateral Debt Relief

Initiative." IMF Country Report No. 10/192, International Monetary Fund, Washington, DC.

IMF (International Monetary Fund). 2016. “United Republic of Tanzania: Selected Issues.” IMF Country Report No. 16/254, International Monetary Fund, Washington, DC.

IMF (International Monetary Fund). 2024. World Economic Outlook: Policy Pivot, Rising Threats. October. Washington, DC: International Monetary Fund.

Jordà, Ó. 2005. “Estimation and Inference of Impulse Responses by Local Projections.” American economic review, 95(1), 161-182.

Jordà, Ó., and A.M. Taylor. 2016. The Time for Austerity: Estimating the Average Treatment Effect of Fiscal Policy." The Economic Journal, 126(590): 219-255.

Jordà, Ó., and A.M. Taylor. 2024. “Local Projections.” Working Paper 32822, National Bureau of Economic Research, Cambridge, MA

Kaminsky, G. L., C. M. Reinhart, and C. A. Vegh. 2004. “When it Rains, It Pours: Procyclical Capital Flows and Macroeconomic Policies.” NBER Macroeconomics Annual 19:11-53.

Kopits, G. and S. Symansky. 1998. “Fiscal Policy Rules.” Occasional Paper 162, International monetary fund, Washington, DC

Kose, M. A., P. Nagle, F. Ohnsorge, and N. Sugawara. 2021. Global Waves of Debt: Causes and Consequences. Washington, DC: World Bank

Larch, M., E. Orseau, and W. Van Der Wielen. 2021. Do EU Fiscal Rules Support or Hinder Counter-Cyclical Fiscal Policy?" Journal of International Money and Finance, 112, 102328.

Mawejje, J., and N. M. Odhiambo. 2024. “Fiscal Rules and the Cyclicality of Fiscal Policy in the East African Community.” Applied Economics Letters, 31(15): 1429-32.

Mei, Z., L. Sheng, and Z. Shi. 2023. "Nickell Bias in Panel Local Projection: Financial Crises Are Worse Than You Think. The Chinese University of Hong Kong, Hong Kong.

Mihalyi, D. and L. Fernández. 2018. “How Did Fiscal Rules Hold Up in The Commodity Price Crash?” Natural Resource Governance Institute, New York.

Montiel Olea, J. L., and M. Plagborg-Møller. 2021. “Local Projection Inference is Simpler and More Robust Than You Think.” Econometrica, 89(4), 1789-1823.

Nickell, S. 1981. "Biases in Dynamic Models with Fixed Effects." Econometrica, 49(6):1417-1426.

Okonjo-Iweala, N., and P. Osafo-Kwaako. 2007. “Nigeria's Economic Reforms: Progress and Challenges.” Working Paper No. 6, Brookings Global Economy and Development, The Brookings Institution, Washington, DC.

Piguillem, F. and A. Riboni. 2021. “Fiscal Rules as Bargaining Chips.” The Review of Economic Studies, 88 (5): 2439–78.

Reuter, W. H. 2015. “National Numerical Fiscal Rules: Not Complied With, But Still Effective?” European Journal of Political Economy 39: 67–81.

Rodrik, D. 1996. "Understanding Economic Policy Reform." Journal of Economic Literature, 34 (1): 9-41.

Sawadogo, P. N. 2020. “Can Fiscal Rules Improve Financial Market Access For Developing Countries?” Journal of Macroeconomics, 65: 103214.

Sawadogo, R. F. 2024. Do Fiscal Rules Shape Private-Sector Investment Decisions? Journal of Macroeconomics, 81: 103617.

Scartascini, C., C. Cruz., and P. Keefer. 2021. The Database of Political Institutions 2020 (DPI2020). https://doi.org/10.18235/0003049

Schaechter, A., T. Kinda, N. Budina, and A. Weber. 2012. “Fiscal Rules in Response to the Crisis—Toward the ‘Next-Generation’ Rules. A New Dataset”, Working Paper No.12/187, International Monetary Fund, Washington, D.C.

Strong, C. O. 2023. “The Impact of Fiscal Rules on Government Debt: Evidence From The CFA Zone.” Empirical Economics, 65(5): 2357-2391.

Sun, L., and S. Abraham. 2021. “Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects.” Journal of econometrics, 225(2), 175-199.

Tapsoba, R. 2012. "Do National Numerical Fiscal Rules Really Shape Fiscal Behaviours in Developing Countries? A Treatment Effect Evaluation." Economic Modelling 29 (4): 1356-69.

Teulings, C. N., and N. Zubanov. 2014. “Is Economic Recovery a Myth? Robust Estimation of Impulse Responses.” Journal of Applied Econometrics, 29(3): 497-514.

Vinturis, C. 2023. “How Do Fiscal Rules Shape Governments’ Spending Behavior?” Economic Inquiry 61: 322–341.

World Bank. 2022. Nigeria Public Finance Review: Fiscal Adjustment for Better and Sustainable Results. World Bank, Washington, DC.

Wyplosz, C. 2013. “Fiscal Rules: Theoretical Issues and Historical Experiences.” In Fiscal Policy After the Financial Crisis, edited by Alesina, A. and F. Giavazzi, 495-525. Chicago: University of Chicago Press.
"""
