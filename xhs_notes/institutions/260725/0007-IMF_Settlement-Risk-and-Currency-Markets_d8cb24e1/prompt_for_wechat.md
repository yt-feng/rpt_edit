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
# Settlement Risk and Currency Markets

Seungduck Lee, Angelo Ranaldo, and Tomohiro Tsuruga
WP/26/156

IMF Working Papers describe research in progress by the authors and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the authors and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/b537485ecad617f779dea6b7eb760d4183aaae0418095c0e24747d11ab4489bb.jpg)

# IMF Working Paper Monetary and Capital Markets Department

Settlement Risk and Currency Markets
Prepared by Seungduck Lee, Angelo Ranaldo, and Tomohiro Tsuruga\*

Authorized for distribution by Mahvash Qureshi
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Settlement risk is a central friction in currency markets. We provide causal evidence on its pricing by exploiting Hungary's 2015 adoption of CLS, which introduced payment-versus-payment settlement, sharply reducing settlement risk. Using a difference-in-differences design, we find that currency excess returns decline by about ten basis points after CLS adoption, consistent with lower compensation for bearing settlement risk, while exchange rate volatility also falls. Deviations from triangular arbitrage conditions narrow, indicating a reduction in the effective cost of arbitrage and improved market efficiency. Additional evidence based on U.S.-specific holidays supports a mechanism operating through time-zone exposure. Our findings show that settlement risk is a priced friction and a source of limits to arbitrage in currency markets.

RECOMMENDED CITATION: Lee, Seungduck, Angelo Ranaldo, and Tomohiro Tsuruga (2026) “Settlement Risk and Currency Markets” IMF Working Paper WP/26/156, International Monetary Fund, Washington DC.

JEL Classification Numbers:

F31; G14; G15

Keywords:

Foreign exchange; Settlement risk; Market microstructure; Payment-versus-payment; Limit to arbitrage

Authors' E-Mail Addresses:

SLee14@imf.org, angelo.ranaldo@unibas.ch, TTsuruga@imf.org

WORKING PAPERS

# Settlement Risk and Currency Markets

Prepared by Seungduck Lee, Angelo Ranaldo, and Tomohiro Tsuruga

## Contents

1. Introduction .... 1
2. Settlement risk, returns, and volatility .... 3
2.1 Data and measurement .... 4
2.2 Difference-in-differences (DiD) design .... 5
2.3 Estimation results .... 6
2.4 Placebo evidence .... 8
3. Identification with U.S.-specific holidays .... 9
3.1 Settlement risk around U.S.-specific holidays .... 9
3.2 U.S.-specific holidays and intraday data .... 11
3.3 Difference-in-difference-in-differences (DiDiD) design .... 12
3.4 Estimation results .... 12
4. Settlement risk and triangular arbitrage .... 13
4.1 Triangular arbitrage .... 13
4.2 Estimation results .... 15
5. Conclusion .... 18
References .... 19
Appendix .... 22
FIGURES
Figure 1. Hungarian Forint Around CLS Entry: Excess Returns and Volatility .... 4
Figure 2. Placebo Tests: Alternative Treated Currencies and Event Dates .... 10
TABLES
Table 1. Difference-in-Differences Estimates: Excess Returns and Volatility .... 8
Table 2. DiDiD Estimates Around U.S. Holidays: Excess Returns and Volatility .... 14
Table 3. Difference-in-Differences Estimates: Triangular Deviation .... 17
Table A1. Three-Month Pre-Event Differential Linear Trend Tests .... 22
Table A2. Donut-Hole Robustness: Excess Returns and Volatility .... 22
Table A3. Placebo-Treated Currency Tests .... 23
Table A4. Placebo Event-Date Tests .... 23
Table A5. Randomization Inference for Baseline DiD Estimates .... 24
Table A6. Triangular Deviations: Means by Treatment and Period .... 24
Table A7. Triangular Deviations: Pre-period Distributional Benchmarks .... 24

## 1 Introduction

Settlement risk is a fundamental friction in financial markets and is particularly important in foreign exchange (FX) markets, where transactions involve the exchange of two currencies across time zones and payment systems. Since the collapse of Bankhaus Herstatt in 1974, which led to substantial losses for counterparties, a wide range of regulatory and infrastructure initiatives have sought to mitigate this risk. Nevertheless, settlement failures continue to occur. $^{1}$ Settlement risk materializes when one counterparty delivers the currency it has sold while the other fails to deliver—this risk is exacerbated by lengthy settlement cycles and time-zone differences. Given the large notional amounts in FX markets, with daily turnover of approximately \$9.6 trillion (Bank for International Settlement, 2025), even small settlement exposures can translate into economically significant costs and undermine financial stability.

Despite its importance, it remains unclear whether and how settlement risk is reflected in exchange rate dynamics. If market participants require compensation for bearing settlement exposure, exchange rates should embed a settlement risk premium. Even a premium of a few basis points would imply aggregate transaction costs of several billion dollars per day. Beyond pricing, settlement risk may also affect market stability and efficiency. By increasing counterparty exposure and liquidity risk, settlement uncertainty can constrain intermediaries' risk-bearing capacity and require precautionary funding, reducing their ability to absorb demand imbalances and leading to higher exchange rate volatility. It may also raise the effective cost of arbitrage across currencies, weakening no-arbitrage relationships.

Reducing settlement risk, however, is not costless. Alternative approaches—such as shortening settlement cycles or modifying trading infrastructure—may lower exposure but increase liquidity demands, reduce netting efficiency, or introduce operational costs (Rochet and Tirole, 1996; Capponi and Chang, 2025), and compress the time dealers have to source securities for delivery (Mattille, 2026). As a result, the equilibrium pricing of settlement risk depends not only on its presence but also on how it is mitigated. This makes it challenging to isolate the effect of settlement risk on asset prices.

We provide causal evidence on the role of settlement risk in currency pricing by exploiting Hungary's adoption of the Continuous Linked Settlement (CLS) system in November 2015.

CLS introduces payment-versus-payment (PvP) settlement, ensuring that both legs of an FX transaction are settled simultaneously, and thereby eliminating principal risk arising from the timing gap between the deliveries of the two currencies in an exchange. Importantly, CLS reduces settlement risk while preserving settlement cycles and multilateral netting arrangements. This feature allows us to isolate the effect of settlement risk from confounding changes in liquidity demand or market structure, providing a quasi-natural experiment to assess how settlement risk affects exchange rate dynamics and market efficiency. $^{2}$

We conduct three complementary empirical analyses. First, we examine the impact of CLS adoption on currency excess returns and their volatility using a difference-in-differences (DiD) design that compares Hungary with neighboring central and eastern European (CEE) currencies.

Second, we exploit variation in settlement risk induced by U.S.-specific holidays. On these days, trading in CEE currencies is more likely to involve counterparties operating within similar time zones such as those in Europe, reducing settlement risk. Using a difference-in-difference-in-differences (DiDiD) framework, we assess whether Hungary's entry into CLS altered exchange rate dynamics on these days.

Third, we study whether settlement risk affects the enforcement of no-arbitrage conditions by examining deviations from triangular parity across currencies. If settlement risk differs across currency pairs and counterparties, it can act as a limit to arbitrage, leading to persistent deviations from parity conditions. We test whether the introduction of CLS reduces such deviations.

Our results show that settlement risk is priced and has economically meaningful effects on FX markets. Currency excess returns decline by about ten basis points following CLS adoption, consistent with a reduction in compensation for bearing settlement risk. Exchange rate volatility also falls, indicating improved risk-bearing capacity of intermediaries and a relaxation of balance sheet constraints. Evidence based on U.S.-specific holidays further supports a mechanism operating through time-zone exposure. In addition, deviations from triangular arbitrage conditions narrow, suggesting that settlement risk can raise arbitrage costs and limit market integration.

These findings establish settlement risk as both a priced friction in currency markets and a source of limits to arbitrage. By isolating the payment-versus-payment (PvP) channel, our analysis provides a benchmark for evaluating alternative approaches to settlement design. More broadly, the paper contributes to the literature on financial market frictions by showing how settlement infrastructure shapes asset prices and market efficiency, and to the literature on limits to arbitrage in FX markets by identifying settlement risk as a distinct source of deviations from no-arbitrage conditions.

Our paper relates to two strands of the literature. First, a literature on settlement arrangements shows that institutional features such as netting and centralized clearing affect prices and risk (Bernstein et al., 2019; Mcsherry et al., 2017; Hattori, 2023), but focuses primarily on equity and bond markets rather than currency markets. Second, a growing literature documents deviations from no-arbitrage conditions in FX markets and attributes them to financial frictions such as funding constraints and intermediary balance sheet limitations (e.g., Du et al., 2018; Huang et al., 2025), without identifying settlement risk as a source of these frictions. We bridge these strands by providing causal evidence that settlement risk is both priced and a source of limits to arbitrage in currency markets. $^{3}$

The remainder of the paper is organized as follows. Section 2 presents the empirical strategy and main results. Section 3 examines the role of time-zone variation using holiday effects. Section 4 studies implications for triangular arbitrage. Section 5 concludes.

## 2 Settlement risk, returns, and volatility

This section estimates the causal effect of a discrete reduction in FX settlement risk on currency excess returns and exchange rate volatility. Our identification exploits Hungary's transition to payment-versus-payment (PvP) settlement for the Hungarian forint (HUF) through CLS in November 2015.

Settlement risk arises when one leg of an FX transaction is delivered while the counterparty fails to deliver the other leg. CLS, a multicurrency settlement system, mitigates this risk by ensuring that both legs of a transaction settle simultaneously through PvP arrangements, thereby sharply reducing settlement exposure.

If market participants price settlement exposure, a reduction in settlement risk should lower currency excess returns. When settlement risk is elevated, market participants with greater unsettled exposures must reserve balance sheet capacity and precautionary funding to survive potential counterparty default. This constraints their ability to absorb order flow shocks, thereby amplifying exchange rate volatility. Eliminating such exposure through PvP settlement should therefore reduce volatility. Figure 1 shows that both excess returns and excess return volatility for the Hungarian forint decline around the CLS entry date. However, because the figure captures only unconditional patterns and settlement risk can be affected by various other factors, the economic significance of the treatment effect is better assessed using the difference-in-differences estimates.

Figure 1: Hungarian Forint Around CLS Entry: Excess Returns and Volatility  
![](images/c1d80b64853167bd397102572d8bbe110aa40499bf7134fcd797e84c1005d666.jpg)  
Notes: The figure plots daily excess returns and excess return volatility of the Hungarian forint in percent, one month before and after November 16,2015. Volatility is measured as the square root of daily realized volatility computed from intraday data. For more details about the construction of the data and the measurement methodology, see Section 2.1.

We estimate these effects using a difference-in-differences design that compares HUF with a set of neighboring Central and Eastern European (CEE) currencies that did not experience the same settlement infrastructure change.

## 2.1 Data and measurement

Our sample covers six CEE currencies against the U.S. dollar and the euro—HRK, CZK, HUF, PLN, RON, and RSD—from 2015 to 2016. We use Bloomberg bid and ask quotes, timestamped in London time, available at both daily and 30-minute frequencies. Midquotes are computed as the average of bid and ask prices.

We construct two main outcome variables. First, excess returns are measured as the daily log change in the exchange rate relative to the change implied by the overnight interest-rate differential, expressed in basis points. Second, exchange rate volatility is measured using realized volatility, computed from 30-minute intraday returns. $^{4}$ We also construct bid–ask spreads as a proxy for market liquidity and use it as a control variable. In addition, we collect overnight interest rates for each country from Bloomberg. $^{5}$

## 2.2 Difference-in-differences (DiD) design

We define the event date as November 16, 2015, the first day on which HUF became eligible for CLS payment-versus-payment (PvP) settlement (CLS Group, 2015). Following CLS entry, a non-negligible share of HUF transactions was settled through PvP. According to the Magyar Nemzeti Bank (MNB), between November 16, 2015 and March 31, 2016, the daily gross turnover of HUF transactions settled in CLS averaged about 336.6 million U.S. dollars and peaked at 850.9 million U.S. dollars. While this remained a fraction of total market turnover, the participation of major banks at the core of the interdealer network and the availability of PvP settlement likely reduced frictions arising from settlement risk in HUF transactions. $^{6}$ We therefore treat November 16, 2015 as the event date in our empirical design.

The treated unit is the Hungarian forint (HUF). HUF's inclusion in CLS was motivated by the fact that a large share of HUF trading takes place internationally and by the aspiration to improve market stability—considerations shared by other small open economies in CEE. $^{7}$ The control group consists of five geographically and economically proximate CEE currencies that did not join CLS during the sample period: Croatia (HRK), the Czech Republic (CZK), Poland (PLN), Romania (RON), and Serbia (RSD). These currencies share exposure to broad regional developments and global FX conditions. Under the identifying assumption that, absent treatment, HUF and the control currencies would have followed similar shortrun dynamics, this comparison provides a suitable counterfactual. $^{8}$ We define the set of currencies as $CEE = \{HRK, CZK, HUF, PLN, RON, RSD\}$ .

Our baseline specification uses a symmetric window of one month before and after the event. We also consider a three-month window to assess robustness. The choice of window length balances two competing considerations: shorter windows reduce exposure to confounding macroeconomic developments but may limit statistical power, whereas longer windows improve precision at the cost of potentially capturing unrelated shocks. $^{9}$

We estimate the following difference-in-differences specification:

$$
Y _ {c, c ^ {\prime}, t} = \beta P o s t _ {t} + \delta (T r e a t e d _ {c, c ^ {\prime}} \times P o s t _ {t}) + \theta B A S _ {c, c ^ {\prime}, t} + \mu_ {c, c ^ {\prime}} + \Gamma_ {c, m, y} + \varepsilon_ {c, c ^ {\prime}, t},\tag{1}
$$

where $Y_{c,c',t}$ denotes the outcome of interest for the currency pair $(c,c')$ at time t, with $c \in CEE$ and $c' = USD$ . The indicator $Post_{t}$ equals one after November 16, 2015, and zero otherwise, capturing common shifts affecting all currencies over time. $Treated_{c,c'}$ equals one for the HUF/USD pair and zero for the control currencies. The coefficient of interest, $\delta$ , measures the differential change in HUF after CLS adoption relative to the control group and identifies the causal effect of reduced settlement risk under the parallel trends assumption. To control for the effects of potential changes in market liquidity, bid-ask spreads $(BAS_{c,c',t})$ of the currency pair $(c,c')$ at time t are included, following Bernstein et al. (2019) and Hattori (2023). All specifications include currency-pair fixed effects $\mu_{c,c'}$ and currency–month-year fixed effects $\Gamma_{c,m,y}$ . In some specifications, we additionally include date fixed effects to absorb common shocks at the daily level. Focusing on short symmetric windows around the CLS entry limits exposure to unrelated macroeconomic developments, while robustness to longer windows ensures the persistence of the effect.

## 2.3 Estimation results

Table 1 reports the DiD estimates of the impact of Hungary's participation in CLS on FX market conditions, focusing on excess returns (columns (1)-(4)) and their volatility (columns (5)-(8)). All specifications include currency fixed effects and currency-month-year fixed effects, and columns (2), (4), (6), and (8) additionally include date fixed effects. Following Roth et al. (2023), standard errors are clustered at the currency level, which matches the level of treatment assignment and allows for serial correlation and heteroskedasticity within currency series. As our regression specifications include date effect, there is little concern about error correlations across currencies within the same time period. $^{10}$

Across all specifications, the estimated Treated × Post coefficient for excess returns is negative and statistically significant. In the one-month window (columns (1)–(2)), the point estimates are close to -0.10 and significant at the 1% level, implying a reduction of about 10 basis points in daily excess returns following CLS adoption. Given that the average pre-event excess return for HUF is approximately 28 basis points, this decline is economically meaningful. Expanding the window to three months (columns (3)–(4)) yields very similar estimates, indicating that 

[中间内容因长度限制已省略]

s returns; Panel B uses excess return volatility. The reported coefficient is the DID interaction term between the HUF indicator and the post-event dummy. All regressions include currency, date, and country-month-year fixed effects, with standard errors clustered at the currency level. The actual event date is 16 November 2015; placebo dates are 16 May, 16 June, and 16 July 2015. \*\*\* $p < 0.01$ , \*\* $p < 0.05$ , \* $p < 0.1$ .

Table A5: Randomization Inference for Baseline DiD Estimates

<table><tr><td>Specification</td><td>DID Coefficient</td><td>Std. Err.</td><td>t-statistic</td><td>RI p-value (|b|)</td><td>RI p-value (|t|)</td><td>Assignments</td></tr><tr><td colspan="7">Panel A. Excess Returns</td></tr><tr><td>(1) 1-month, no date FE</td><td>-0.0988</td><td>0.0103</td><td>-9.6163</td><td>0.2836</td><td>0.0246**</td><td>528</td></tr><tr><td>(2) 1-month, date FE</td><td>-0.1002</td><td>0.0106</td><td>-9.4962</td><td>0.2779</td><td>0.0359**</td><td>528</td></tr><tr><td>(3) 3-month, no date FE</td><td>-0.1005</td><td>0.0115</td><td>-8.7375</td><td>0.2665</td><td>0.0662*</td><td>528</td></tr><tr><td>(4) 3-month, date FE</td><td>-0.0979</td><td>0.0121</td><td>-8.0673</td><td>0.2741</td><td>0.0510*</td><td>528</td></tr><tr><td colspan="7">Panel B. Excess Return Volatility</td></tr><tr><td>(5) 1-month, no date FE</td><td>-0.0321</td><td>0.0049</td><td>-6.5928</td><td>0.0964*</td><td>0.0813*</td><td>528</td></tr><tr><td>(6) 1-month, date FE</td><td>-0.0326</td><td>0.0055</td><td>-5.9614</td><td>0.0851*</td><td>0.0794*</td><td>528</td></tr><tr><td>(7) 3-month, no date FE</td><td>-0.0320</td><td>0.0051</td><td>-6.2167</td><td>0.0756*</td><td>0.0926*</td><td>528</td></tr><tr><td>(8) 3-month, date FE</td><td>-0.0326</td><td>0.0056</td><td>-5.7812</td><td>0.0813*</td><td>0.0945*</td><td>528</td></tr></table>

Notes: This table reports the results of space-time placebo tests for the four baseline difference-in-differences specifications. We construct an extended placebo distribution by reassigning treatment across all six currencies and dates during the 90-day pre-event period (August 15 to November 15, 2015), which yields 528 distinct placebo assignments. For each placebo assignment, estimation is performed using a sliding window that matches the baseline specification's sample width ( $\pm30$ days for 1-month specifications and $\pm90$ days for 3-month specifications). The numbering of the specifications corresponds to those used in Table 1. All regressions include currency and country-month-year fixed effects, with standard errors clustered at the currency level. The reported RI p-values indicate the proportion of the reference distribution—comprising all placebo assignments and the actual estimate—for which the absolute DID coefficient ( $|b|$ ) or absolute t-statistic ( $|t|$ ) is at least as large as the actual estimate for HUF on November 15, 2015. We rely primarily on the studentized t-statistic ( $|t|$ ) to account for potential heteroskedasticity across different currencies and time periods. \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1.

Table A6: Triangular Deviations: Means by Treatment and Period

<table><tr><td></td><td>Pre mean (bp)</td><td>Post mean (bp)</td><td>Change (bp)</td><td> $N_{\text{pre}}$ </td><td> $N_{\text{post}}$ </td></tr><tr><td colspan="6">Panel A. CLS = ±1 month window</td></tr><tr><td>Control (Other CEE)</td><td>0.0425</td><td>0.0447</td><td>0.0022</td><td>126</td><td>132</td></tr><tr><td>Treated (HUF)</td><td>0.0714</td><td>0.0546</td><td>-0.0168</td><td>21</td><td>22</td></tr><tr><td>Unconditional DiD</td><td></td><td>-0.0190</td><td></td><td></td><td></td></tr><tr><td colspan="6">Panel B. CLS = ± 3 months window</td></tr><tr><td>Control (Other CEE)</td><td>0.0448</td><td>0.0603</td><td>0.0155</td><td>374</td><td>396</td></tr><tr><td>Treated (HUF)</td><td>0.0742</td><td>0.0692</td><td>-0.0050</td><td>65</td><td>66</td></tr><tr><td>Unconditional DiD</td><td></td><td>-0.0205</td><td></td><td></td><td></td></tr></table>

Notes: Pre/post means of triangular deviations (bp) are computed within each window sample. The unconditional DiD is $(\bar{D}_{1,1}-\bar{D}_{1,0})-(\bar{D}_{0,1}-\bar{D}_{0,0})$ .

Table A7: Triangular Deviations: Pre-period Distributional Benchmarks

<table><tr><td></td><td>N</td><td>Mean</td><td>SD</td><td>p25</td><td>Median</td><td>p75</td><td>IQR</td><td>Min-Max</td></tr><tr><td colspan="9">Panel A. CLS = 1 month window (pre period only)</td></tr><tr><td>All</td><td>147</td><td>0.0466</td><td>0.0346</td><td>0.0243</td><td>0.0436</td><td>0.0615</td><td>0.0372</td><td>0.0021-0.2959</td></tr><tr><td>Control (Other CEE)</td><td>126</td><td>0.0425</td><td>0.0272</td><td>0.0227</td><td>0.0397</td><td>0.0629</td><td>0.0401</td><td>0.0021-0.1220</td></tr><tr><td>Treated (HUF)</td><td>21</td><td>0.0714</td><td>0.0583</td><td>0.0500</td><td>0.0541</td><td>0.0596</td><td>0.0096</td><td>0.0445-0.2959</td></tr><tr><td colspan="9">Panel B. CLS = 3 months window (pre period only)</td></tr><tr><td>All</td><td>439</td><td>0.0491</td><td>0.0470</td><td>0.0267</td><td>0.0440</td><td>0.0622</td><td>0.0355</td><td>0.0019-0.5057</td></tr><tr><td>Control (Other CEE)</td><td>374</td><td>0.0448</td><td>0.0373</td><td>0.0227</td><td>0.0404</td><td>0.0630</td><td>0.0402</td><td>0.0019-0.4270</td></tr><tr><td>Treated (HUF)</td><td>65</td><td>0.0742</td><td>0.0794</td><td>0.0499</td><td>0.0548</td><td>0.0592</td><td>0.0093</td><td>0.0388-0.5057</td></tr></table>

Notes: The table summarizes the distribution of triangular deviations (bp) in the pre period within each event window sample. IQR is defined as p75–p25.

![](images/945cbdea33d37740bbde733d11aa176d9c1bcbced26130473737b66b646115b0.jpg)
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
