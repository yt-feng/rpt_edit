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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Sovereign Risk and Natural Disaster Shocks: Unraveling the Domestic Yield Curve Response

Kangni Kpodar, Alassane Drabo and Carine Meyimdjui

WP/26/139

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN

![](images/ebdcc27b030c76b756853fe32927caab9bd398061c036b9bb7436b1f66be3ce2.jpg)

# IMF Working Paper African Department

# Sovereign Risk and Natural Disaster Shocks: Unraveling the Domestic Yield Curve Response Prepared by Kangni Kpodar, Alassane Drabo and Carine Meyimdjui\*

Authorized for distribution by Kangni Kpodar

July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper investigates the impact of natural disasters on the domestic sovereign yield curve, shedding light on their distinct transmission channels. Using a sample of 72 developing countries during the period 2000-20, and leveraging a newly compiled dataset on domestic treasury bill and bond yields, the findings from the fixed-effects and the local projection difference in difference estimations point to a disaster premium in the pricing of domestic government securities. While natural disasters significantly steepen the yield curve, their effects are confined to short-term maturity debts. In contrast, a worsening in climate vulnerability shifts upward the entire yield curve. Heightened fiscal stress and monetary policy stance emerge as the main transmission channels. These results underscore the importance of integrating resilience building into debt management and fiscal policy frameworks.

JEL Classification Numbers:

H60, E43, F34

Keywords:

Natural disasters; sovereign risk; yield curve

Author's E-Mail Address:

kkpodar@imf.org, adrabo@imf.org

WORKING PAPERS

# Sovereign Risk and Natural Disaster Shocks: Unraveling the Domestic Yield Curve Response

Prepared by Kangni Kpodar, Alassane Drabo and Carine Meyimdjui

## Contents

I. Introduction......4
II. How do natural disaster shocks affect the cost of government financing?......7
A. A selective review of the literature......7
B. The transmission channels......8
III. The data, empirical model and econometric methodology......10
A. Data and measurements......10
B. The model specification and methodological approach......14
IV. Empirical results......17
A. Natural disaster shocks and the domestic sovereign yield curve......17
B. Testing the transmission channels......28
V. Conclusion......32
References......33
ANNEX
1. Domestic Sovereign Yield Database......38
FIGURES
1. Trends in Gross Public Debt in Developing Countries, 2000-20......5
2. Trends in Government Interest Bill in Developing Countries, 2000-20......5
3. Nominal Interest Rate on Government Securities, 2000-20......11
4. Yield Curve in Selected Years......11
5. Nominal Interest Rate on Government Securities by Income Group, 2000-20......12
6. Climate Change and the Cost of Government Domestic Borrowing, 2000-20......13
7. Average Treatment Effect of Drought on the Interest Rate on Domestic Government Securities, all maturities combined......25
8. Average Treatment Effect of Drought on the Interest Rate on Domestic Government Securities by Maturity......25
9. Average Treatment Effect of Storm on the Interest Rate on Domestic Government Securities, all maturities combined......26
10. Average Treatment Effect of Storm on the Interest Rate on Domestic Government Securities by Maturity......27
11. Average Treatment Effect of Climate Vulnerability on the Interest Rate on Domestic Government Securities, all maturities combined......27
12. Average Treatment Effect of Climate Vulnerability on the Interest Rate on Domestic Government Securities by Maturity......28

## ANNEX FIGURES

1. Number of Instruments, 1977-2021 ....40
2. Country Coverage by Region, 1977-2021....40
3. Country Coverage by Income Group, 1977-2021 ....41
4. Distribution of Domestic Securities by Maturity....41
5. Distribution of Nominal and Real Interest Rates on Government Securities....42

## APPENDIX FIGURES

1. Evolution of the Real Interest Rate on Government Securities, 2000-20....51
2. Real Interest Rate on Government Securities by Income Group....52
3. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to Disaster Damage as a Share of GDP....53
4. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to the Share of Affected Population in Total Population....53

## TABLES

1. Natural Disaster and Interest Rate on Government Securities, all maturities combined....18
2. Natural Disaster and Interest Rate on Short-Term Government Securities, (up to 3-month maturity)....19
3. Natural disaster and Interest Rate on Short-Term Government Securities, (up to 1 year maturity)....20
4. Natural disaster and Interest Rate on Medium-Term Government Securities, (2-to-3-year maturity)....21
5. Natural disaster and Interest Rate on Long-Term Government Securities, (4-year maturity and beyond)....22
6. Climate Vulnerability and Interest Rate on Government Securities....23
7. Drought Episodes and Interest Rate on Government Securities (all maturities combined):
Transmission Channels....29
8. Storm Episodes and Interest Rate on Government Securities (all maturities combined):
Transmission Channels....30
9. Climate Vulnerability and Interest Rate on Government Securities (all maturities combined):
Transmission Channels....31

## ANNEX TABLES

1. Country Sample and Data Coverage ....43
2. Data Sources ....46

## APPENDIX TABLES

1. Dataset on Domestic Treasury Bill and Bond Yields: Country Sample....54
2. Summary Statistics and Correlation Matrix....55
3. Variables Definitions and Sources....57
4. Climate Vulnerability and Interest Rate on Government Securities – First Stage Regression....58
5. Drought Episodes and Interest Rate on Government Securities by Maturity: Transmission Channels....59
6. Storm Episodes and Interest Rate on Government Securities by Maturity: Transmission Channels....61
7. Climate Vulnerability and Interest Rate on Government Securities by Maturity: Transmission Channels....62

## I. Introduction

The 2018 report of the Intergovernmental Panel on Climate Change (IPCC, 2018) underscores that climate variability and the frequency of natural disasters have largely increased over the last century. The combined land and ocean temperature has increased at 0.08 degrees Celsius per decade since 1880 (NOAA, 2020 annual report), whilst the number of natural disasters grew ten-fold from 39 incidents in 1960 to reach 396 in 2019 (Institute for Economics and Peace, 2020).

Recognizing that the intensification of climate and disaster shocks has drastic macroeconomic consequences, the economic literature on the matter has expanded considerably in the recent years (e.g. Benson and Clay, 2004; Hochrainer, 2009; Dell, Jones, and Olken, 2012; Auffhammer, 2018; Acevedo et al, 2020, IMF, 2020; Kahn et al., 2021; Hallegatte, Jooste and Mcisaac, 2022; etc.). The occurrence of natural events impacts economic activity through the flows of capital, goods and services, the balance of payments and public finances. Studies generally find a negative effect of natural disasters and climate anomalies on economic performance, particularly in developing countries (see Klomp and Valckx, 2014, for a meta-analysis; Noy, 2009; Dell, Jones, and Olken, 2012; Berlemann and Wenzel, 2018, Clevy and Evans, 2025; Nguyen, Feng, and Garcia-Escribano, 2025; and Aligishiev and Kolpakova, 2025).

An important consideration for policy makers, when dealing with the consequences of climate change and the solutions to address it, is the question of access to capital and its affordability. Several studies examine the implications of climate change for sovereign debt spreads, notably Kling et al (2018), and Cevik and Jalles (2022). Kling et al. (2018) use climate vulnerability data to assess the impact on bond yields and find that countries with higher exposure to climate vulnerability experience higher cost of debt on average. Similarly, Cevik and Jalles (2022) find that countries that exhibit larger vulnerability to climate risks incur higher bond yields and spreads than otherwise, with the effect being more pronounced for developing countries because of a weaker resilience to climate change.

Nonetheless, the impact of disaster shocks on the cost of government domestic borrowing was overlooked. Yet, domestic public debt has risen in many developing countries as domestic financial markets deepen, and international liquidity dried up during the global financial crisis. The average domestic debt level in developing countries was estimated at 34 percent of GDP in 2020, up from about 22 percent of GDP two decades earlier (Figure 1). As a share of total debt, domestic debt in developing countries accounted for about half of total debt in the late 2010s, almost 20 percentage points higher than in the early 2000s. Since domestic debts typically carry high interest rates, the combined quantity and price effect results in a high and burdening domestic interest bill (Figure 2), with its share in the total interest bill being much higher than the share of domestic debt in total debt. In this paper, we aim to fill this gap in the literature by addressing the following questions: (i) Do natural disasters and climate vulnerability have implications for the cost of government domestic borrowing? (ii) Is the impact uniform along the yield curve? (iii) what are the transmission channels at play?

Figure 1. Trends in Gross Public Debt in Developing Countries, 2000–20 (percent of GDP)  
![](images/cba6f99092135f308f035b47f921b09b6ccc3aff64047e3448d470f6796be7e1.jpg)  
Sources: World Economic Outlook Database and authors' calculations.

Figure 2. Trends in Government Interest Bill in Developing Countries, 2000–20 (percent of GDP)  
![](images/bf0ae8a5fd1afe780369bcab859432d2c3ca9d5fe58416e673a8217ff90e5090.jpg)  
Sources: World Economic Outlook Databases, International Debt Statistics and authors' calculations.

In contributing to a more comprehensive view on the disaster-sovereign risk nexus, this paper relates to two main strands of the literature. First, there is a rapidly growing literature on the macroeconomic impact of climate shocks; the impact of which on sovereign risk has been particularly emphasized in several papers, including Klomp (2015, 2017), Farhi and Gabaix (2015), Marto, Papageorgiou and Klyuev (2018), Kling et al. (2018), Mallucci (2022), Klusak et al., (2021), Cevik and Jalles (2022), and Zenios (2022). Second, a parallel literature focusing on the financial market pricing of climate risks (see for instance Baker et al. (2018), IMF (2020), Ehlers, Packer and de Greiff (2022) and Bolton and Kacperczyk (2023)) stresses challenges related to the limited availability of risk-sharing instruments (due to the global nature of climate risks), the high degree of uncertainty about climate risks and imperfect information available to investors about climate risks and their consequences (Eren, Merten and Verhoeven, 2022).

This paper departs from the existing literature in a meaningful way. Unlike previous studies, the paper focuses on the cost of domestic public debt across various maturities. A key challenge faced by previous studies was the lack of consolidated datasets of government T-bill and bond rates. We address this issue by compiling a new and original panel dataset on interest rates on government papers with the breakdown by maturity for 99 countries, of which 72 developing economies over the period 2000–20. The paper then links the cost of government domestic debt to a range of indicators for natural disasters and climate vulnerability. Using the data by maturity allows for a more granular analysis on how different climate indicators affect the entire yield curve.

Natural disaster shocks may exert pressures on treasury bills and bond rates for several reasons. First, the resulting revenue loss and spending pressures worsen public deficits and increase public debt, which in turn, raise the cost of financing. Second, the economic consequences of natural disasters, including the infrastructure destruction, the cost of reconstruction, the ensuing economic downturn may decrease government solvency, increase the probability of default and the risk premium in the post disaster environment (Klomp, 2015, 2017). The deterioration in the country's creditworthiness may prompt domestic investors to demand higher interest rates for buying government securities. Third, the frequent occurrence of natural disasters signal to investors that future natural disasters are likely, a risk domestic banks would price in the cost of government debt. While climate mitigation and adaptation policies strengthen resilience and therefore should help limit the rise in the interest rate on government securities, these policies require in most cases higher government spending. This suggests that at least in the short run, the funding needs of the government will increase, and hence the pressure on domestic borrowing costs for the budget. Finally, disaster shocks may lead to inflationary pressures, prompting the central bank to increase the policy rate and thus the cost of capital, notably for the government (Isoré and Szczerbowicz, 2017; Fratzscher et al., 2020).

On the methodological front, the paper relies on fixed-effect and local projection difference in difference estimations to uncover the static and dynamic response of the domestic yield curve to climate shocks. Focusing on the sample of 72 developing economies, the findings reveal that drought and storm episodes exacerbate the cost of government domestic borrowing, but only for short maturity debts, thus leaving the cost of medium and long maturity debts broadly unaffected. On the other hand, a country's vulnerability to climate shocks is associated with higher cost of short, medium and long maturity debts. Heightened fiscal stress and monetary policy stance emerge as the main transmission channels from natural disasters and climate vulnerability. As to the latter, the adverse impact on the cost of government domestic borrowing is attenuated in countries with deeper financial systems.

The remaining of the paper is organized as follows. Section 2 presents a brief literature review and lay out the transmission channels between climate shocks and public finances. This is followed by Section 3, which: (i) provides a description of the new dataset on the treasury bill and bond yields; and (ii) describes the empirical model and methodological approaches. Section 4 discusses in detail the results, and Section 5 concludes.

## II. How do natural disaster shocks affect the cost of government financing?

## A. A selective review of the literature

Several studies look at the implications of natural disasters and climate change for public finances. For instance, Mohan and Strobl (2020) show that damaging storms cause debt to increase up to three quarters after the event, using tropical storm data for the period 1993–2013 for the Eastern Caribbean. Alejos (2021) on the other hand, estimates that the occurrence of at least one extreme event leads to an increase in the fiscal deficit by an average of 0.9 percent of GDP for low-income countries in the same year.

Consistent with this line of the literature, converging evidence points to a disaster or climate risk premium embedded in the cost of external financing. Zenios (2022) goes as far as to warn of climate risk causing debt dynamics to worsen and risk premia to rise non-linearly leading potentially to a “climate-debt doom-loop”. Natural disasters are perceived by investors as adverse economic shocks that may make the government debt unsustainable considering that the credit default premium paid by bond holders accelerates in the days after a disaster (see also Klomp, 2015 and 2017; Marto, Papageorgiou and Klyuev, 2018). Using a discrete choice model and about 115 countries in the period 1985–2010, Klomp (2017) shows that one additional large-scale natural disaster raises the onset probability of a sovereign debt default by about three percentage-points.

Farhi and Gabaix (2015) proposes a model that prioritizes the exchange rate channel. Reflecting the productivity of the export sector, countries differ by their riskiness, captured by the extent to which their exchange rate would depreciate if a major world disaster were to occur. The authors argue that because the exchange rate is an asset price whose future risk affects its current value, relatively riskier countries have more depreciated exchange rates, and feature high interest rates, because investors need to be compensated for the risk of an exchange rate depreciation in a potential world disaster.

In the same vein, Kling et al. (2018) assess empirically the effect of climate change on the cost of external debt using climate data from the Notre Dame Global Adaptation Initiative. The paper finds that countries with higher exposure to climate vulnerability exhibit a higher external debt cost by 1.2 percentage point on average. Beirne et al (2021a) reach similar conclusions for Southeast Asian countries. Cevik and Jalles (2022) address potential sample selection bias due to idiosyncrasy and endogeneity concerns by relying on a larger sample than Kling et al (2018) and using alternative specifications and estimation methodologies. Vulnerability and resilience to climate change markedly affect government borrowing costs. However, the magnitude and statistical significance of the effects are much greater in developing countries with weaker capacity to adapt to and mitigate the consequences of climate change.

Mallucci (2022) adopts a standard sovereign default model to incorporate natural disaster risk. The calibration of the model with data from a sample of seven Caribbean countries shows that hurricane risks decrease government's ability to issue debt and restrict its access to financial markets. In his model, absent hurricane risk, spreads are, on average, 105 basis points lower, an estimate comparable to Cevik and Jalles (2022)'s. Finally, Klusak et al, (2021)'s simulations suggest that climate-induced sovereign downgrades could occur as early as 20

[中间内容因长度限制已省略]

d><td>354</td><td>354</td></tr><tr><td>Countries</td><td>33</td><td>33</td><td>33</td><td>33</td></tr><tr><td>R2</td><td>0.24</td><td>0.36</td><td>0.34</td><td>0.46</td></tr></table>

Notes: All control variables and time dummies are included in each of the tables; fixed effects estimates; robust standard errors in parentheses; \* significant at 10 percent, \*\* significant at 5 percent and \*\*\* significant at 1 percent.

## Appendix Table 7. Climate Vulnerability and Interest Rate on Government Securities by Maturity: Transmission Channels

## 7.1. Up to 3-month maturity

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td rowspan="2">Climate vulnerability index (lagged)</td><td>2.648*</td><td>1.648</td><td>1.345</td><td>0.923</td><td>2.343</td></tr><tr><td>(1.528)</td><td>(1.404)</td><td>(1.287)</td><td>(1.311)</td><td>(1.539)</td></tr><tr><td rowspan="2">Public debt/GDP</td><td></td><td>0.070***</td><td></td><td>0.018*</td><td></td></tr><tr><td></td><td>(0.011)</td><td></td><td>(0.011)</td><td></td></tr><tr><td rowspan="2">Monetary policy rate</td><td></td><td></td><td>0.436***</td><td>0.402***</td><td></td></tr><tr><td></td><td></td><td>(0.029)</td><td>(0.030)</td><td></td></tr><tr><td rowspan="2">Private sector credit/GDP</td><td></td><td></td><td></td><td></td><td>-0.006</td></tr><tr><td></td><td></td><td></td><td></td><td>(0.006)</td></tr><tr><td rowspan="2">Clim. vul. index (lagged) * Pri. sec. credit/GDP</td><td></td><td></td><td></td><td></td><td>0.213</td></tr><tr><td></td><td></td><td></td><td></td><td>(0.267)</td></tr><tr><td>Observations</td><td>657</td><td>569</td><td>635</td><td>547</td><td>639</td></tr><tr><td>Countries</td><td>55</td><td>49</td><td>55</td><td>49</td><td>54</td></tr><tr><td>Cragg-Donald Wald F statistic</td><td>14.4</td><td>14.3</td><td>11.8</td><td>11.2</td><td>6.5</td></tr></table>

7.2. Up to 1 year maturity

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td rowspan="2">Climate vulnerability index (lagged)</td><td>3.486**</td><td>2.448*</td><td>2.006*</td><td>1.530</td><td>3.684***</td></tr><tr><td>(1.430)</td><td>(1.339)</td><td>(1.194)</td><td>(1.255)</td><td>(1.417)</td></tr><tr><td rowspan="2">Public debt/GDP</td><td></td><td>0.076***</td><td></td><td>0.025**</td><td></td></tr><tr><td></td><td>(0.012)</td><td></td><td>(0.011)</td><td></td></tr><tr><td rowspan="2">Monetary policy rate</td><td></td><td></td><td>0.429***</td><td>0.397***</td><td></td></tr><tr><td></td><td></td><td>(0.027)</td><td>(0.031)</td><td></td></tr><tr><td rowspan="2">Private sector credit/GDP</td><td></td><td></td><td></td><td></td><td>-0.004</td></tr><tr><td></td><td></td><td></td><td></td><td>(0.006)</td></tr><tr><td rowspan="2">Clim. vul. index (lagged) * Pri. sec. credit/GDP</td><td></td><td></td><td></td><td></td><td>0.068</td></tr><tr><td></td><td></td><td></td><td></td><td>(0.243)</td></tr><tr><td>Observations</td><td>732</td><td>626</td><td>710</td><td>604</td><td>714</td></tr><tr><td>Countries</td><td>58</td><td>52</td><td>58</td><td>52</td><td>57</td></tr><tr><td>Cragg-Donald Wald F statistic</td><td>18.3</td><td>17.3</td><td>15.1</td><td>13.3</td><td>9.0</td></tr></table>

## 7.3. 2-to-3-year maturity

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Climate vulnerability index (lagged)</td><td>6.033**(2.581)</td><td>8.173***(2.889)</td><td>6.079**(2.482)</td><td>8.345***(2.911)</td><td>11.876**(5.356)</td></tr><tr><td>Public debt/GDP</td><td></td><td>0.238***(0.046)</td><td></td><td>0.231***(0.050)</td><td></td></tr><tr><td>Monetary policy rate</td><td></td><td></td><td>0.346***(0.082)</td><td>0.178*(0.099)</td><td></td></tr><tr><td>Private sector credit/GDP</td><td></td><td></td><td></td><td></td><td>0.018(0.015)</td></tr><tr><td>Clim. vul. index (lagged) * Pri. sec. credit/GDP</td><td></td><td></td><td></td><td></td><td>-0.859(0.640)</td></tr><tr><td>Observations</td><td>326</td><td>294</td><td>315</td><td>284</td><td>315</td></tr><tr><td>Countries</td><td>36</td><td>30</td><td>35</td><td>29</td><td>35</td></tr><tr><td>Cragg-Donald Wald F statistic</td><td>12.2</td><td>10.3</td><td>12.5</td><td>10.3</td><td>2.5</td></tr></table>

7.4. 4-year maturity and beyond

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Climate vulnerability index (lagged)</td><td>2.000**(0.873)</td><td>1.402**(0.665)</td><td>1.057(0.842)</td><td>0.453(0.640)</td><td>2.763***(1.008)</td></tr><tr><td>Public debt/GDP</td><td></td><td>0.120***(0.016)</td><td></td><td>0.110***(0.015)</td><td></td></tr><tr><td>Monetary policy rate</td><td></td><td></td><td>0.218***(0.058)</td><td>0.265***(0.046)</td><td></td></tr><tr><td>Private sector credit/GDP</td><td></td><td></td><td></td><td></td><td>0.007**(0.003)</td></tr><tr><td>Clim. vul. index (lagged) * Pri. sec. credit/GDP</td><td></td><td></td><td></td><td></td><td>-0.405***(0.150)</td></tr><tr><td>Observations</td><td>406</td><td>352</td><td>395</td><td>344</td><td>398</td></tr><tr><td>Countries</td><td>38</td><td>32</td><td>38</td><td>32</td><td>37</td></tr><tr><td>Cragg-Donald Wald F statistic</td><td>24.3</td><td>29.2</td><td>20.0</td><td>23.6</td><td>9.0</td></tr></table>

Notes: All control variables and time dummies are included in each of the tables; Instrumental variable estimations, climate vulnerability index is lagged by one period and instrumented by its exogenous component; robust standard errors in parentheses; \* significant at 10 percent, \*\* significant at 5 percent and \*\*\* significant at 1 percent.

![](images/0485a076cb90a35fc8822b1e55da175f6ae1bf3f43ae7e6537e8bdf48322f606.jpg)
"""
