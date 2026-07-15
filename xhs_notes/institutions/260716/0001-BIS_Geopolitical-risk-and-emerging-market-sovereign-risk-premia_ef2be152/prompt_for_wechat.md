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
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/eeb57e1bf379393d80f2ad2a1e38ba6fd7704c049e230c16bbf2d413259f242f.jpg)

BIS Working Papers
No 1368

# Geopolitical risk and emerging market sovereign risk premia

by Fredy Gamboa-Estrada and José Vicente Romero
Monetary and Economic Department

July 2026

JEL classification: C23, C54, F34, G15

Keywords: sovereign risk, credit default swaps, EMBI, emerging markets, geopolitical risk, panel local projections, state-dependent transmission

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).

ISSN 1020-0959 (print)
ISSN 1682-7678 (online)

# Geopolitical Risk and Emerging Market Sovereign Risk Premia\*

Fredy Gamboa-Estrada $^{\dagger}$ José Vicente Romero $^{\ddagger}$

## Abstract

This study examines how geopolitical risk (GPR) transmits to sovereign credit risk in emerging market economies (EMEs), using monthly data on the 5-year sovereign credit default swap (SCDS) and the J.P. Morgan Emerging Markets Bond Index (EMBI) spread for 13 EMEs over the period of January 2005–October 2025. Using fixed-effects panel local projections, the framework is extended to allow for state-dependent transmission. Differences in impulse responses across states are attributed to specific macro-financial fundamentals. Three main findings are identified. First, an increase in the GPR index raises both SCDS and EMBI spreads. Second, disaggregating the index into its subcomponents reveals a larger response to threats than to acts, consistent with the possibility of anticipation effects in sovereign credit markets. Third, evaluating the state-dependent impulse response around the Russian invasion of Ukraine yields substantially different responses, with the post-invasion configuration increasing the sovereign risk premia response. Our findings show the importance of modeling the state-dependent transmission of geopolitical shocks and provide a useful tool for incorporating geopolitical scenarios into sovereign risk analysis.

JEL Clasification: C23, C54, F34, G15.

Keywords: Sovereign risk, credit default swaps, EMBI, emerging markets, geopolitical risk, panel local projections, state-dependent transmission.

## 1 Introduction

Sovereign credit default swaps (SCDS) and the J.P. Morgan Emerging Markets Bond Index (EMBI) spread are widely used by policymakers and market participants as proxies for sovereign risk in emerging market economies (EMEs). SCDS, as financial derivatives, represent the cost of insuring against sovereign default and therefore directly capture sovereign credit risk. Meanwhile, the EMBI spread tracks the performance of sovereign bonds issued by EMEs, reflecting sovereign credit risk via stripped yield spreads relative to U.S. Treasuries. Both measures are indicators of investor perceptions of sovereign creditworthiness and are closely monitored, particularly given the additional risk premia investors face in EMEs, stemming from weaker fiscal fundamentals and external financial conditions. Despite their widespread use, the simultaneous analysis of these two indicators remains uncommon, leaving a gap in understanding their combined insights into sovereign risk.

In periods of heightened political and economic uncertainty, investors demand a higher premium to hedge their portfolios against the increased probability of sovereign default. This drives both the SCDS and EMBI spreads higher. Among the factors influencing sovereign risk premia, geopolitical factors can play a significant role. Rising geopolitical risk, by increasing instability, can further widen SCDS and EMBI spreads.

This paper examines how geopolitical risk transmits to sovereign risk in EMEs. Understanding the mechanisms through which geopolitical events influence sovereign credit markets is important for policymakers and practitioners alike. Such insights are increasingly important in light of a growing body of literature and policy discussions, including contributions by Caldara and Iacoviello (2022), Ortiz et al. (2026), International Monetary Fund (2025) and Niepmann and Shen (2025).

The contribution of this study to the literature is threefold. First, we jointly analyze the responses of SCDS and EMBI spreads to geopolitical risk across a panel of 13 EMEs, a relatively underexplored topic in the literature on EMEs' risk premia. While we treat SCDS as our primary outcome, we also include EMBI results as a complementary exercise, given SCDS spreads' greater responsiveness to geopolitical risk. Second, we exploit the threats and acts subindices of the Caldara and Iacoviello (2022) geopolitical risk index and examine whether each transmits differently to sovereign spreads. This decomposition captures both the realization of adverse geopolitical events and threats of future events, which may convey different information to sovereign credit markets. Third, we extend the local projections framework of Jordà (2005) to a state-dependent panel setting following Cloyne et al. (2023), allowing the response to vary with macro-financial fundamentals. We then compare responses before and after Russia's 2022 invasion of Ukraine since two configurations of these fundamentals differ sharply.

We obtain three main findings. First, geopolitical risk significantly raises both the SCDS and EMBI spreads, with the larger effect on SCDS. Second, within the geopolitical risk index, threats drive larger increases in spreads than acts, particularly for EMBI spreads, consistent with the possibility of anticipation effects. Finally, the post-invasion configuration, following Russia's invasion of Ukraine, amplifies SCDS and EMBI responses, underlining how geopolitical events interact with sovereign risk fundamentals to raise sovereign risk.

The article has five sections, including this introduction. Section 2 reviews the related literature, the theoretical motivation, and the channels through which geopolitical risk affects sovereign risk in EMEs. Section 3 describes the data and presents stylized facts on the dynamics and co-movement of SCDS and EMBI spreads in the 13 EMEs in our sample. Section 4 details the econometric approach and presents the main results. The final section summarizes the findings and discusses policy implications.

## 2 Assessing the importance of geopolitical risk for EMEs' risk premia

Why is it important to study the impact of geopolitical shocks on EMEs' risk premia? Recent literature on the impact of geopolitical risk has highlighted that such shocks can significantly affect asset prices. According to Klement (2021), geopolitical shocks affect an asset's fair value by altering the sovereign risk premium. Pástor and Veronesi (2013) argue that investors may demand extra returns to hold riskier assets in a politically uncertain environment. In this case, geopolitical shocks may command a risk premium unrelated to economic shocks but tied to heightened uncertainty, as economic sentiment falls and markets tend to pull back.

In its Global Financial Stability Report, the IMF (International Monetary Fund, 2025) explains that geopolitical risks affect financial asset prices through two key channels: the economic channel and the market sentiment channel. The economic channel captures the impact of disruptions to trade, supply chains, and financial transactions, as well as increased fiscal vulnerabilities from higher military spending and reduced economic activity. These factors can raise sovereign borrowing costs by widening SCDS spreads and sovereign bond yields. The market sentiment channel reflects heightened uncertainty and risk aversion, which can lead to capital outflows and a flight to safety, further influencing sovereign risk premia.

Although there is extensive literature on the impact of geopolitical risk on equity prices, fixed income, and commodities (Fernández-Villaverde et al., 2024; Caldara and Iacoviello, 2022; Umar et al., 2022; Iyke et al., 2022; Nonejad, 2022; Gong and Xu, 2022; Wang et al., 2022; Zaremba et al., 2022; Jung et al., 2021), few studies have specifically analyzed the effect of geopolitical risk shocks on sovereign risk premia (either the SCDS or EMBI spreads) in EMEs, which is the focus of this paper. For example, Klement (2021) suggests that, according to the evidence found by Caldara and Iacoviello (2022) regarding the effects of an increase in the GPR index on financial markets, geopolitical risk shocks tend to have long-lasting impacts on the risk premium when the shock persistently affects economic growth and other variables such as the inflation rate and the risk-free rate. Simonyan and Bayraktar (2022) analyze the relationship between CDS and country-specific and global factors, including geopolitical risk. The authors find that equity indices, international reserves, the VIX, and oil prices are the most important determinants of CDS spreads across 11 EMEs. However, the impact of geopolitical risk is not significant in their estimations. Subramaniam (2022) finds that the impact of geopolitical uncertainty on the sovereign bond spreads of BRICS economies depends on the interest rate regime. Decomposing sovereign bond yields into long-, medium-, and short-term factors, the author shows that geopolitical risk positively affects the yield-curve factors in extremely high-rate regimes, whereas in extremely low-rate regimes, the effects are concentrated in the yield curve's curvature and slope.

Naifar and Aljarba (2023) analyze the potential co-movement between sovereign credit risk and geopolitical risk in 19 advanced economies and EMEs. Using a quantile approach, the authors find that geopolitical risk has a heterogeneous, asymmetric, and mainly positive effect on the CDS spread, and that countries with larger sovereign wealth funds are less affected than others. Demiralay et al. (2024) provide global evidence that country-specific geopolitical risk significantly increases CDS spreads, with the effect being more pronounced during periods of heightened market volatility, sovereign credit risk, and weaker economic performance.

Bratis et al. (2024) find evidence of volatility spillovers between a global geopolitical index and sovereign risk during the crisis period of 2009–2012 for core and periphery Economic and Monetary Union (EMU) countries, and show that geopolitical risk has a greater influence on CDS spreads than on sovereign bond yields. Similarly, Afonso et al. (2024) show that geopolitical tensions in border countries increase the sovereign risk of European economies, with the effect being more pronounced during periods of market turbulence, such as the subprime crisis. Papavassiliou (2025) study the relationship between geopolitical risks and euro-area sovereign bond yields and find a positive association. Markets demand higher risk premia during geopolitical events, and this effect remains significant even after accounting for key economic factors.

Aslam and Newaz (2025) provide further evidence that sovereign bonds are particularly sensitive to geopolitical risks, highlighting that bonds respond more strongly to threats than to realized geopolitical events. Ortiz et al. (2026) add to this growing body of evidence by showing that geopolitical shocks primarily affect risk premia through direct sovereign repricing, whereas geoeconomic shocks are transmitted via financial conditions, policy uncertainty, and domestic amplification.

While existing studies have explored the relationship between geopolitical risk and sovereign risk premia, they often focus on aggregate risk measures or a single instrument such as SCDS spreads. Our paper distinguishes itself by jointly analyzing the SCDS and EMBI spreads, enabling a more comprehensive understanding of sovereign risk dynamics. Additionally, by exploiting the threats and acts subindices of the geopolitical risk index, we uncover asymmetric responses that studies using only the aggregate index cannot detect. Finally, our state-dependent framework highlights the role of sovereign risk fundamentals in shaping the transmission of geopolitical shocks, offering insights that static models miss.

One important consideration regarding the dynamics of sovereign risk premia is that the SCDS and EMBI spreads depend on the joint behavior of the valuation discount factor and default probabilities (Chernov et al., 2020). Default probabilities reflect the economy's endogenous responses to shocks and to government debt. When adverse shock realizations and increases in government debt occur, investors require compensation for potential losses from default during such episodes. In this context, a crucial determinant of the value of expected payments is the hazard rate, the probability of default conditional on the event not yet having occurred. This hazard rate depends on the variables that determine the ability to pay (Gamboa and Romero, 2024). In EMEs, the variables most used as fundamentals of default probabilities are debt levels, commodity prices, regional financial conditions, and factors tied to the global financial cycle, all of which directly affect economic performance, creditworthiness, and the discount factor used in valuation. These variables, in turn, can be influenced by geopolitical developments.

![](images/da538e8c623dcfe96c99fd7ab4686ab976ad24230550d9e5e4e0c1b68f69cd8b.jpg)  
Figure 1: Transmission of geopolitical risk shocks to sovereign risk premia in EMEs  
Source: Authors' elaboration.

Nonetheless, given the complex nature of geopolitical shocks, several channels may affect the determinants of sovereign credit risk, and ex ante, it is not clear how these shocks might impact a specific country's sovereign risk, as shown in Figure 1. The figure maps the two channels identified in the IMF's Global Financial Stability Report (International Monetary Fund, 2025): an economic channel, operating through commodity prices, terms of trade, and fiscal and external balances, and a market sentiment channel, operating through global risk aversion, capital flows, and external financing costs. For example, certain geopolitical shocks could raise oil prices, potentially improving the risk profile of an oil-exporting EME. Conversely, some geopolitical shocks may reduce international investors' appetite for EME risk, leading to tighter external financial conditions and higher SCDS and EMBI spreads for

## 3 Data and Stylized Facts

## 3.1 Geopolitical Risk (GPR) Index

Although there is no straightforward method for measuring geopolitical uncertainty, the GPR index developed by Caldara and Iacoviello (2022) has become a widely adopted indicator for assessing this risk. According to the authors, geopolitical risk encompasses the “threat, realization, and escalation of adverse events associated with wars, terrorism, and any tensions among states and political actors that affect the peaceful course of international relations.”

The GPR index quantifies geopolitical risk by tracking the frequency of relevant terms in leading international newspapers. $^{1}$ It captures a broad spectrum of geopolitical events and serves as a comprehensive summary measure of global geopolitical uncertainty, highlighting periods of heightened tensions, as illustrated in Figure 2. $^{2}$

From 2005 onwards, the index remained at a moderate baseline until the Russian invasion of Ukraine in early 2022, after which geopolitical tensions have remained significantly elevated. For our econometric analysis, we standardize the index to a mean of 0 and a variance of 1, using it as our measure of geopolitical risk. Caldara and Iacoviello (2022) further decompose the index into two sub-indices: Threats and Acts. The Threats sub-index captures anticipatory geopolitical risks, such as war risks and military tensions, while the Acts sub-index reflects the materialization of adverse events, such as terrorist attacks and military escalations.

![](images/301681b107b03807653ebff92e579f12bb48d1abf9e41d142b11de7ed1fe7eeb.jpg)  
Figure 2: Geopolitical Risk (GPR) index of Caldara and Iacoviello (2022) and main geopolitical events, January 1985–October 2025.

## 3.2 Emerging Market Sovereign Risk Premia and Control Variables

In our empirical analysis, we investigate sovereign risk premia across a panel of 13 emerging market economies, using the 5-year SCDS and EMBI spreads. The sample includes Brazil, Chile, China, Colombia, Hungary, Indonesia, Malaysia, Mexico, Peru, the Philippines, Poland, South Africa, and Türkiye, covering the period from January 2005 to October 2025. These countries were selected because they are part of the MSCI Emerging Markets Index and have data available for both SCDS and EMBI spreads. Spreads are measured in basis points, with higher values indicating greater perceived default risk. Building on the empirical specifications of Gamboa and Romero (2024) and Vargas-Herrera et al. (2022), we include each country's commodity terms-of-trade cycle, public-debt position relative to global levels, global financial conditions, and a country-specific common component of EME sovereign spreads as controls.

Commodity terms of trade, as calculated by the IMF, reflect the relative price movements of a country's commodity exports and imports. This serves as an indicator for assessing economic performance, particularly in commodity-dependent economies. To capture exposure to commodity-price fluctuations, we rely on each country's commodity terms-of-trade cycle. $^{3}$ As a measure of debt and fiscal position, we include the cyclical component of each country's gross debt position relative to the global average, derived from IMF data. $^{4}$

To approximate the global financial cycle, we use the Chicago Fed National Financial Conditions Index (NFCI). The NFCI, calculated by the Federal Reserve Bank of Chicago, is a comprehensive indicator that reflects overall risk, liquidity, and leverage conditions in the U.S. financial system. $^{5}$ As a measure of emerging-market-specific financial conditions, or the appetite of international investors for foreign-currency-denominated emerging-market debt, we construct a country-specific indicator based on the dynamic factor of emerging-market SCDS and EMBI spreads, following the approach of Gamboa and Romero (2024). $^{6}$

## 4 Econometric Approach

## 4.1 Impact of Geopolitical Risk on E

[中间内容因长度限制已省略]

0</td></tr><tr><td>Indonesia</td><td>162.0</td><td>103.2</td><td>63.5</td><td>142.9</td><td>774.3</td><td>250</td></tr><tr><td>Malaysia</td><td>83.2</td><td>48.9</td><td>13.1</td><td>77.7</td><td>282.8</td><td>250</td></tr><tr><td>Mexico</td><td>120.3</td><td>53.8</td><td>30.8</td><td>111.7</td><td>420.4</td><td>250</td></tr><tr><td>Peru</td><td>120.1</td><td>57.3</td><td>43.8</td><td>106.1</td><td>409.4</td><td>250</td></tr><tr><td>Philippines</td><td>131.0</td><td>90.0</td><td>36.0</td><td>102.1</td><td>487.4</td><td>250</td></tr><tr><td>Poland</td><td>83.9</td><td>59.4</td><td>8.0</td><td>67.6</td><td>362.8</td><td>250</td></tr><tr><td>South Africa</td><td>187.7</td><td>81.1</td><td>26.3</td><td>188.5</td><td>455.9</td><td>250</td></tr><tr><td>Türkiye</td><td>289.1</td><td>137.6</td><td>119.0</td><td>256.2</td><td>863.3</td><td>250</td></tr><tr><td>Total</td><td>141.9</td><td>101.5</td><td>8.0</td><td>117.7</td><td>863.3</td><td>3,250</td></tr></table>

Notes: The table reports descriptive statistics for the 5-year sovereign CDS spread (in basis points) for the 13 EMEs in the sample at monthly frequency (January 2005 to October 2025; T = 250 months per country). Source: Bloomberg; authors' calculations.

Table 5: EMBI spreads: descriptive statistics by country

<table><tr><td>Country</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Median</td><td>Max</td><td>N</td></tr><tr><td>Brazil</td><td>262.6</td><td>78.9</td><td>143.5</td><td>241.6</td><td>557.6</td><td>250</td></tr><tr><td>Chile</td><td>146.7</td><td>52.0</td><td>54.8</td><td>138.0</td><td>383.0</td><td>250</td></tr><tr><td>China</td><td>147.1</td><td>55.0</td><td>37.5</td><td>157.1</td><td>287.1</td><td>250</td></tr><tr><td>Colombia</td><td>244.1</td><td>89.6</td><td>108.4</td><td>215.8</td><td>551.1</td><td>250</td></tr><tr><td>Hungary</td><td>197.6</td><td>125.8</td><td>25.3</td><td>159.2</td><td>650.1</td><td>250</td></tr><tr><td>Indonesia</td><td>231.5</td><td>119.2</td><td>72.9</td><td>205.0</td><td>890.8</td><td>250</td></tr><tr><td>Malaysia</td><td>137.3</td><td>60.2</td><td>57.6</td><td>123.6</td><td>428.3</td><td>250</td></tr><tr><td>Mexico</td><td>263.5</td><td>101.0</td><td>97.6</td><td>244.6</td><td>676.3</td><td>250</td></tr><tr><td>Peru</td><td>182.7</td><td>59.9</td><td>103.8</td><td>169.5</td><td>523.7</td><td>250</td></tr><tr><td>Philippines</td><td>166.5</td><td>99.3</td><td>56.2</td><td>129.8</td><td>566.0</td><td>250</td></tr><tr><td>Poland</td><td>102.0</td><td>66.0</td><td>-1.8</td><td>94.2</td><td>324.8</td><td>250</td></tr><tr><td>South Africa</td><td>270.2</td><td>117.2</td><td>57.8</td><td>270.0</td><td>682.5</td><td>250</td></tr><tr><td>Türkiye</td><td>338.1</td><td>125.9</td><td>162.4</td><td>298.4</td><td>744.4</td><td>250</td></tr><tr><td>Total</td><td>206.9</td><td>112.9</td><td>-1.8</td><td>182.6</td><td>890.8</td><td>3,250</td></tr></table>

Notes: The table reports descriptive statistics for the J.P. Morgan Emerging Markets Bond Index spread (in basis points) for the 13 EMEs in the sample at monthly frequency (January 2005 to October 2025; T = 250 months per country). Source: Bloomberg; authors' calculations.

Table 6: Descriptive Statistics: SCDS and EMBI Spreads

<table><tr><td></td><td>CDS spread (bps)</td><td>EMBI spread (bps)</td></tr><tr><td>Mean</td><td>141.91</td><td>206.91</td></tr><tr><td>Std. dev.</td><td>101.54</td><td>112.91</td></tr><tr><td>Minimum</td><td>7.98</td><td>-1.84</td></tr><tr><td>Maximum</td><td>863.27</td><td>890.78</td></tr><tr><td colspan="3">Percentiles</td></tr><tr><td>1%</td><td>14.86</td><td>37.47</td></tr><tr><td>5%</td><td>30.37</td><td>67.78</td></tr><tr><td>10%</td><td>48.77</td><td>86.67</td></tr><tr><td>25%</td><td>73.95</td><td>129.98</td></tr><tr><td>50%</td><td>117.69</td><td>182.59</td></tr><tr><td>75%</td><td>180.00</td><td>262.04</td></tr><tr><td>90%</td><td>262.67</td><td>351.10</td></tr><tr><td>95%</td><td>337.84</td><td>427.83</td></tr><tr><td>99%</td><td>537.02</td><td>582.68</td></tr><tr><td colspan="3">Distributional shape</td></tr><tr><td>Skewness</td><td>2.01</td><td>1.36</td></tr><tr><td>Kurtosis</td><td>9.24</td><td>5.94</td></tr><tr><td>Observations</td><td>3,250</td><td>3,250</td></tr></table>

Notes: Sample covers 13 EMEs at monthly frequency from 2005m1 to 2025m10 (perfectly balanced panel, $N = 13 \times 250 = 3,250$ ). Spreads are expressed in basis points.  
Source: Authors' calculations based on Bloomberg and JPMorgan EMBI Global data.

Table 7: Within and Between Variation in Sovereign Spreads

<table><tr><td>Variable</td><td>Dimension</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td><td>N</td></tr><tr><td rowspan="3">CDS</td><td>Overall</td><td>141.91</td><td>101.54</td><td>7.98</td><td>863.27</td><td>N = 3,250</td></tr><tr><td>Between</td><td></td><td>61.79</td><td>69.21</td><td>289.14</td><td>n = 13</td></tr><tr><td>Within</td><td></td><td>82.37</td><td>-28.27</td><td>754.24</td><td>T = 250</td></tr><tr><td rowspan="3">EMBI</td><td>Overall</td><td>206.91</td><td>112.91</td><td>-1.84</td><td>890.78</td><td>N = 3,250</td></tr><tr><td>Between</td><td></td><td>67.62</td><td>102.02</td><td>338.12</td><td>n = 13</td></tr><tr><td>Within</td><td></td><td>92.34</td><td>-5.51</td><td>866.20</td><td>T = 250</td></tr></table>

Notes: Decomposition of total variation into between-country and within-country components, computed via Stata's xtsum. Within-country variation exceeds between-country variation for both spreads, indicating substantial time-series variation remains after absorbing country fixed effects. Negative within-dimension minima reflect deviations from country-specific means and do not imply negative spreads.
Source: Authors' calculations.
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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
