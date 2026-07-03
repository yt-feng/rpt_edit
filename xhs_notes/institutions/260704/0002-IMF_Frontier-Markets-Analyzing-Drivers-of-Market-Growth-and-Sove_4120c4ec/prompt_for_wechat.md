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
# Frontier Markets

# Analyzing Drivers of Market Growth and Sovereign Risks

Younes Takki Chebihi, Naoya Kato, Maxwell Kushnir, Andreja Lenarčič, Yinhao Sun, and Bilal Tabti

WP/26/140

IMF Working Papers describe research in progress by the authors and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the authors and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL © 2026 International Monetary Fund

![](images/c09e10ae9092cce2018ed239010dd5b578130423274f6f78ac764bdd5a35cf97.jpg)

WP/26/140

IMF Working Paper
Strategy, Policy, and Review Department

Frontier Markets: Analyzing Drivers of Market Growth and Sovereign Risks\* Prepared by Younes Takki Chebihi, Naoya Kato, Maxwell Kushnir, Andreja Lenarčič, Yinhao Sun, and Bilal Tabti

Authorized for distribution by Pritha Mitra
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Frontier Market (FM) status serves as a steppingstone for Low-Income Countries (LICs) aspiring to become Emerging Markets (EMs). Since the concept first emerged over three decades ago, FMs have gained substantial investment appeal, particularly after the 2008 Global Financial Crisis. At the same time, the recent series of global shocks starting with the COVID-19 pandemic highlighted the countries' persistent vulnerabilities. This paper seeks to deepen our understanding of FMs by offering new analysis on the determinants of frontier market status and, using a dynamic country sample, examining the factors that help LICs attain and lose FM status. It finds that building robust macroeconomic fundamentals and ensuring good governance are critical for becoming an FM. In addition, the paper identifies flexible exchange rates, substantial official reserve buffers, and relatively low public debt and deficit levels as key contributors to lessening the sensitivity of FMs' sovereign spreads to changes in global financial conditions.

RECOMMENDED CITATION: Chebihi, Y.T., Kato, N., Kushnir, M., Lenarcic, A., Sun, Y., and Tabti, B. 2026. "Frontier Markets: Analyzing Drivers and Sovereign Risks". Working Paper WP/26/140. International Monetary Fund, Washington D.C.

<table><tr><td>JEL Classification Numbers:</td><td>E6, E44, F34, G12, G15, O11, O57</td></tr><tr><td>Keywords:</td><td>Frontier Markets; Sovereign Spreads; Market Access; U.S. Monetary Policy Spillovers</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>youneschebihi@gmail.com, naoya.katou@boj.or.jp, mkushnir@imf.org, ALenarcic@imf.org, ysun5@imf.org, BTabti@imf.org</td></tr></table>

WORKING PAPERS

# Frontier Markets

# Analyzing Drivers of Market Growth and Sovereign Risks

Prepared by Younes Takki Chebihi, Naoya Kato, Maxwell Kushnir, Andreja Lenarcic, Yinhao Sun, and Bilal Tabti $^{1}$

## Contents

Introduction .... 3
Related Literature .... 4
Frontier Markets: Identification and Stylized Facts .... 5
Identifying Frontier Markets .... 5
Descriptive Analysis .... 8
Empirical Analysis .... 12
Factors Influencing the Transition to Frontier Market Status.... 12
The Sensitivity of FMs to US Monetary Policy Stance, Compared with NFLICs and EMs.... 15
Role of Structural Factors in Mitigating Exposure to US Monetary Policy .... 17
Robustness .... 20
Robustness of FM identification .... 20
Robustness Checks for Frontier Market Classification and Transition Determinants from NFLICs to FMs .... 20
Robustness Checks on FMs Spreads Sensitivity .... 20
Conclusion .... 21
Annex I. Additional Stylized Facts.... 22
Annex II. Robustness Checks .... 24
References .... 34

## FIGURES

1. Tracking the shifts in countries status: A heatmap view (1993-2022)....8
2. Dynamics of key variables: Comparison between NFLICs and FMs (1993-2022)....11
3. FMs spreads response to a U.S. monetary policy stance changes: A comparative analysis of regime switching with NFLICs and EMs....16
4. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals....16
5. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure...18
6. EMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals....19
7. EMs spreads response to a U.S. monetary policy stance changes: The role of external position structure...19

## TABLES

1. Description of FM identification criteria .... 7
2. Correlation matrix of the baseline FM identification and different definition criteria .... 7
3. Descriptive analysis .... 9
4. Factors driving the transition from NFLIC to FM status.... 14

## Introduction

Frontier market (FM) status is a steppingstone on the trajectory of Low-Income Countries (LICs) $^{2}$ graduating towards Emerging Market (EM) status. The concept of Frontier Markets was born three decades ago, $^{3}$ reflecting a need to better recognize the particular characteristics of advanced LICs that are more integrated into the global economic and financial system than their peers in the LIC universe. Being granted FM status signaled that countries are becoming an attractive destination for investment due to rapid growth and development, buttressed by significant exposure to international private capital flows in the form of FDI or portfolio flows. FMs were seen as beacons of optimism among LICs, and FM status as a milestone on the path to becoming an EM.

The number of countries considered to be FMs has been growing since the 1990s. This trend accelerated in the aftermath of the Global Financial Crisis (GFC), which saw increased investor interest in this subgroup of low-income developing countries (LIDCs). This growth in market interest paved the way for greater access and heightened external debt issuance, with 23 LIDCs tapping international financial markets between the GFC and 2022. Investment banks and corporations supported this new interest by launching indices like the J.P. Morgan NexGen, S&P Frontier BMI, and FTSE Frontier Index. Additionally, the inclusion of LICs since 2009 and investors' growing interest in these markets helped promote the J.P. Morgan EMBI Global Diversified Index.

More recently, these countries have been affected by a series of adverse global shocks that tested their resilience and affected their growth trajectories. These shocks started with the COVID-19 pandemic, which was succeeded by shocks on energy and food prices as a result of the Russia-Ukraine war, the tightening of global financial conditions in response to monetary policy tightening in advanced economy interest rates to support disinflation, and major shifts in external financing to LICs with declines in remittances and official development assistance (ODA) flows. As FMs saw their macroeconomic fundamentals deteriorate, they experienced capital outflows, currency depreciations, widening spreads and difficulties in issuing new bonds after the COVID-19. However, these pressures have somewhat unwound recently, with several FMs successfully regaining market access $^{4}$ in a context of overall better economic performance than less advanced LICs. Nevertheless, the exposure to sizeable adverse shocks has highlighted risks of FMs losing their frontier status, which motivates our paper's focus on FMs' economic characteristics and vulnerabilities and their implications for their FM status.

The analysis proceeds in three steps. First, we refine and extend the definition of what constitutes a FM that was initially developed in the 2014 report on Macroeconomic Developments in Low-Income Developing Countries ("2014 LIDC report" hereafter; IMF 2014) and create a time-varying sample of FMs. We then compare the macroeconomic and structural characteristics of FMs compared to non-frontier LICs (NFLICs) and EMs. Second, we examine the drivers of the transition from NFLICs to FMs and evaluate the relative importance of country specific fundamentals compared to global conditions in increasing the probability of attaining the FM status. Third, we estimate the sensitivity of FMs' sovereign spreads to changes in global financial conditions, captured by the shadow U.S. short term interest rate, and examine how their response is affected by countries' structural characteristics.

We find that the transition from NFLICs to FM essentially depends on fundamentals such as strong output growth and low public debt, as well as improvements in economic institutions and governance. Meanwhile, global push factors such as US monetary policy stance and stock market volatility seem to matter less for the transition from NFLIC to FM status. We also find that the response of FM sovereign spreads to changes in U.S. monetary policy does not differ to that observed for EMs, while no such sensitivity is observed for the spreads of NFLICs that are less integrated into global financial markets. A closer look at the role of countries' structural characteristics for the sensitivity of FMs' sovereign spreads to global financial conditions, proxied by U.S. monetary policy stance points to a positive impact of flexible exchange rates, large official reserves buffers, low deficits and public debt—consistent with findings of studies investigating the likelihood of financial crises in EMs.

## Related Literature

Our paper contributes to the broader literature on (i) market access and (ii) the propagation of shocks among Frontier and Emerging Markets. It does so by relying on a systematic approach to identify Frontier Market countries that reduces the role of judgment and subjective factors. In practice, the classification of countries as FMs, including for analytical work, typically occurs based on their inclusion in dedicated FM market indices (e.g., IMF, 2022) or a combination of market access and income criteria. Our identification method relies on financial variables beyond market access and is closely related to Abidi et al. (2016) who also use a time-varying version of the IMF (2014) classification. While the focus of their analysis is on capital flows dynamics, this study focuses on the determinants of the transition to FM status and the response of FMs to changes in the global financial conditions.

First, we contribute to the literature that assesses the relative importance of push (external shocks) and pull (macroeconomic fundamentals and other country-specific characteristics) factors in driving market access by looking at how these factors affect the transition to Frontier Market status, which is a broader concept than market access. We find that the transition to FM status is mainly driven by pull factors, consistent with findings from our identification methodology that FM status tends to be a persistent state. Our findings complement Presbitero et al. (2015), who find that countries with stronger fiscal and external positions and more robust institutions are more likely to access international markets, and Haque et al. (2017), who find that strong growth performance, quality of governance and favorable sovereign credit rating tends to increase LICs' likelihood to access international markets. $^{5}$ Da Silva et al. (2021) reach similar conclusions but also find a role for easing external financial conditions in determining increased external issuance and lower spreads. Kogan et al. (2024) find that global financial conditions and country debt ratios are the most important factors that determine market access during IMF programs, using a sample of 56 EMs and FMs. On the other hand, Feyen et al. (2015) show that global push factors mattered significantly for external bond issuance in EMs and LIDCs between 2000-2014. Recent analysis on LICs (IMF, 2025) shows however a distinct role for both push and pull factors: domestic pull factors matter more to attract longer-term FDI flows, while global push factors together with financial market development are more important determinants of portfolio flows.

Second, we contribute to the extensive literature studying the response of sovereign yields to economic shocks and global factors. This literature shows that (i) global factors, such as global liquidity and contagion among others have a crucial role in driving the dynamics of sovereign yields in EMs (González-Rozada and Yeyati (2008), Agur et al. (2019)), and that (ii) there is a positive link between changes in U.S. monetary policy and EMs sovereign yields through a capital flow channel (Ahmed and Zlate, 2014; Broner et al., 2021; Bhattarai et al., 2021; Albagli et al., 2019; Gilchrist et al., 2019). Comelli et al. (2012) find that periods of high global uncertainty are characterized by a dampened response of spreads to domestic fundamentals. We find that the response of FMs' yields to US monetary policy stance does not differ from that of EMs, $^{6}$ which contrasts with the prevailing perception of higher vulnerability of this group of countries compared to EMs. We also find that strong fiscal and external buffers as well as a diversified export structure help dampen the rise of sovereign spreads for FMs following a US monetary policy tightening. Our analysis highlights the importance for policymakers in LICs to improve macroeconomic fundamentals to reach FM status and to keep strong fiscal and external buffers to dampen the costs of external macroeconomic fluctuations.

The rest of the paper is organized as follows. Section II introduces the methodology to identify Frontier Markets and presents descriptive statistics, comparing FMs to non-FM LICs and EMs. Section III presents empirical analysis to (i) identify determinants of FM status and (ii) analyze the sensitivity of their spreads to changes in global financial conditions. Section IV discusses robustness checks. Section V concludes.

## Frontier Markets: Identification and Stylized Facts

## Identifying Frontier Markets

This section exploits time series variation in macroeconomic and financial indicators to identify FMs over time and compare them with NFLICs and EMs. There is no universally agreed-upon definition of what constitutes an FM, despite many efforts to define this concept.

Credit rating agencies (CRA) and financial institutions have attempted to identify FMs in efforts to compile investment indices targeting this market segment. As the primary purpose of these indices is to provide information to investors, indices developed by these entities (e.g., JP Morgan EMBIG, S&P Frontier BMI, and MSCI Frontier Markets Index) rely on classification based on financial depth, and encompass elements such as market size, liquidity, and market regulation and structure. While their classification is widely used for economic monitoring, using these indices to identify FMs for investigating their fundamental characteristics could be problematic due to a lack of transparency in the underlying methodologies and use of judgment. Using these indices to track FMs over time prior to the early 2000s presents additional challenges, owing to data availability constraints.

Apart from CRA-based definitions, other definitions often rely on the concept of market access. Da Silva et al. (2021) propose a rule to distinguish FMs from other low-income countries using two criteria, one of which includes at least one public and publicly guaranteed (PPG) external bond issuance between 1990 to 2019. $^{7}$ One drawback of this definition is that it does not vary in time and does not account for changes in PPG bond issuance over time. An additional risk includes inaccurately identifying countries as FMs based on a one-off debt issuance.

On the other hand, the 2014 LIDC report (IMF, 2014) uses a more granular and data-oriented definition that is based on five indicators. The definition captures a country's financial system's depth (broad money-to-GDP ratio, stock market capitalization), its openness (cross-border loans and deposits, portfolio inflows), and its capacity to issue in international markets (see Table 1). A key point of this definition is that it exclusively relies on financial variables and does not cover macroeconomic fundamentals. To identify FMs, the values of these variables for each LIDC country are compared to those from the sample of EMs, according to a methodology that is described below.

Our paper aims to build on the 2014 LIDC methodology, while incorporating additional sources of data, to construct an annual time series of FMs.

Given differences in the definition and coverage of “low-income countries” across the literature, this study adopts a broad initial sample when identifying FMs with a quantitative methodology, so as to minimize the risk of omission. The sample is based on the 2023 vintage of PRGT-eligible countries, $^{8}$ supplemented by additional countries that have a been part of the LIDC classification in the past or have potential to be identified as FMs due to their inclusion in FM financial indices. $^{9}$ The final sample comprises 87 countries. For each country in the sample, we then compare the average value of several financial indicators (described in Table 1) over a three-year rolling window $^{10}$ to the value of the same indicator for countries labeled as EMs in the WEO classification for those years. A country in our sample is classified as a FM if it meets at least 4 out of the 5 criteria each year (considering the rolling window). For four indicators, (i) the ratio of broad money to GDP, (ii) cross-border loans and deposits, (iii) stock market capitalization and (iv) portfolio inflows, the criterion associated with that indicator is considered met if the three-year average surpasses the lower end of the one-standard-deviation band of the three-year average of the EMs. The fifth criterion, sovereign bond issuance, is considered met if a country issued external bonds in the current and past two years or has a credit rating above BB-.

Frontier Market status is assigned to 369 observations, corresponding to roughly 14.13% of the sample (1,921 observations categorized as NFLICs and 320 EMs). Market capitalization and market access appear to be key drivers of the FM classification, as illustrated in Table 2, which shows a correlation matrix between the FM indicator and its five determinants.

Table 1. Description of FM identification criteria $^{11}$

<table><tr><td>Criterion</td><td>Definition</td><td>Data source</td><td>Dummy construction</td></tr><tr><td>Bro

[中间内容因长度限制已省略]

erging Markets Review, 38, 347-363.

Ahmed, S., & Zlate, A. (2014). Capital flows to emerging market economies: A brave new world? Journal of International Money and Finance, 48, 221-248.

Ahmed, S., Coulibaly, B., & Zlate, A. (2017). International financial spillovers to emerging market economies: How important are economic fundamentals?. Journal of International Money and Finance, 76, 133-152.

Aizenman, J., Park, D., Qureshi, I. A., Saadaoui, J., & Uddin, G. S. (2024). The performance of emerging markets during the Fed's easing and tightening cycles: a cross-country resilience analysis. Journal of International Money and Finance, 148, 103169.

Albagli, E., Ceballos, L., Claro, S., & Romero, D. (2019). Channels of US monetary policy spillovers to international bond markets. Journal of Financial Economics, 134(2), 447-473.

Balcilar, M., & Demirer, R. (2015). Effect of global shocks and volatility on herd behavior in an emerging market: Evidence from Borsa Istanbul. Emerging Markets Finance and Trade, 51(1), 140-159.

Bhattarai, S., Chatterjee, A., & Park, W. Y. (2021). Effects of US quantitative easing on emerging market economies. Journal of Economic Dynamics and Control, 122, 104031.

Bowman, D., Londono, J. M., & Sapriza, H. (2015). US unconventional monetary policy and transmission to emerging market economies. Journal of International Money and Finance, 55, 27-59.

Broner, F., Martin, A., Pandolfi, L., & Williams, T. (2021). Winners and losers from sovereign debt inflows. Journal of International Economics, 130, 103446.

Calvo, G. A., Leiderman, L., & Reinhart, C. M. (1996). Inflows of capital to developing countries in the 1990s. Journal of Economic Perspectives, 10(2), 123-139.

Chuhan, P., Claessens, S., & Mamingi, N. (1998). Equity and bond flows to Latin America and Asia: The role of global and country factors. Journal of Development Economics, 55(2), 439-463.

Comelli, F. (2012). Emerging market sovereign bond spreads: Estimation and back-testing. Emerging Markets Review, 13(4), 598-625.

da Silva, V. H. C. A., de Almeida, L. A., & Singh, D. (2021). Determinants of and prospects for market access in frontier economies (IMF Working Paper WP/21/137). International Monetary Fund.

Ebeke, C., & Lu, Y. (2015). Emerging market local currency bond yields and foreign holdings—A fortune or misfortune? Journal of International Money and Finance, 59, 203-219.

Fernandez-Arias, E., & Montiel, P. J. (1996). The surge in capital inflows to developing countries: An analytical overview. The World Bank Economic Review, 10, 51-77.

Feyen, E., Ghosh, S., Kibuuka, K., & Farazi, S. (2015). Global liquidity and external bond issuance in emerging markets and developing economies. (World Bank Policy Research Working Paper 7363) World Bank.

Fowler, H., (2010), Frontier Markets: The changing face of risk, Emerging Markets News, analysis and opinions, Global Markets, 09/10/2010.

Gilchrist, S., Yue, V., & Zakrajšek, E. (2019). US monetary policy and international bond markets. Journal of Money, Credit and Banking, 51, 127-161.

González-Rozada, M., & Yeyati, E. L. (2008). Global factors and emerging market spreads. The Economic Journal, 118(533), 1917-1936.

Guscina, A., Malik, S., & Papaioannou, M. G. (2017). Assessing loss of market access: Conceptual and operational issues. Washington, DC: International Monetary Fund.

Haque, T., Bogoev, J., & Smith, G. (2017). Push and pull: Emerging risks in frontier economy access to international capital markets. Washington, DC: World Bank.

Kogan, J., Kazandjian, R., Luo, S., Mbohou, M., & Miao, H. (2024). The role of IMF arrangements in restoring access to international capital markets (IMF Working Paper WP/24/173). International Monetary Fund.

Inoguchi, M. (2021). The impact of foreign capital flows on long-term interest rates in emerging and advanced economies. Review of International Economics, 29(2), 268-295.

International Monetary Fund. (2014). Macroeconomic developments in low-income developing countries: 2014. Washington, DC: International Monetary Fund.

International Monetary Fund. (2022). Global financial stability report—Navigating the high-inflation environment. Washington, DC: International Monetary Fund.

International Monetary Fund. (2025). Macroeconomic developments and prospects for low-income countries - 2025. Washington, DC: International Monetary Fund.

Jordà, Ó. (2005). Estimation and inference of impulse responses by local projections. American Economic Review, 95(1), 161-182.

Nellor, D. C. L. (2008). The rise of Africa's "frontier" markets. Finance and Development, 45(3), 30-33.

Ngene, G., Post, J. A., & Mungai, A. N. (2018). Volatility and shock interactions and risk management implications: Evidence from the US and frontier markets. Emerging Markets Review, 37, 181-198.

Presbitero, A., Ghura, M. D., Adedeji, M. O., & Njie, L. (2015). International sovereign bonds by emerging markets and developing economies: Drivers of issuance and spreads (IMF Working Paper WP/15/275). International Monetary Fund.

Quisenberry, C. (2010). Exploring the frontier emerging equity markets. CFA Institute.

Samarakoon, L. P. (2011). Stock market interdependence, contagion, and the US financial crisis: The case of emerging and frontier markets. Journal of International Financial Markets, Institutions and Money, 21(5), 724-742.

Seth, N., & Singhania, M. (2019). Volatility in frontier markets: A multivariate GARCH analysis. Journal of Advances in Management Research, 16(3), 294-312.

Speidell, L. S., & Krohne, A. (2007). The case for frontier equity markets. The Journal of Investing, 16(3), 12-22.

![](images/b9adff0cc4b4aaa0815303cd24579d11476daea913e442bfca8dac4f44e3bc44.jpg)
"""
