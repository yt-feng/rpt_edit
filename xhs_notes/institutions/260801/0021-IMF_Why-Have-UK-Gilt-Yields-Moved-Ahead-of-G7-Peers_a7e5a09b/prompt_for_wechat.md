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
# Why Have UK Gilt Yields Moved Ahead of G7 Peers?

Benjamin Mosk

SIP/2026/073

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 24, 2026. This paper is also published separately as IMF Country Report No 26/173.

2026
JUL

![](images/6988b04a4b59d87c909a39887eb235d6e3097bd2a3279db87aebefa0d1494064.jpg)

# IMF Selected Issues Paper European Department

# Why Have UK Gilt Yields Moved Ahead of G7 Peers? Prepared by Benjamin Mosk

Authorized for distribution by Romain Alexandre Duval
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 24, 2026. This paper is also published separately as IMF Country Report No 26/073.

ABSTRACT: Since 2022, UK gilt yields, especially at long maturities, have risen above G7 peers, increasing borrowing costs and tightening financial conditions. This paper examines the drivers of the UK term premium—the component of yields reflecting time-varying risk compensation beyond expected short rates. In the UK, shifts in the investor base and rising importance of domestic factors may also have contributed, alongside signs of increased market fragility after the September 2022 turmoil. Maintaining credible policy frameworks and adapting debt management strategies to evolving demand conditions are key to containing the term premium.

RECOMMENDED CITATION: Mosk, Benjamin. "Why Have UK Gilt Yields Moved Ahead of G7 Peers?" IMF Selected Issues Paper 26/073.

JEL Classification Numbers:

G12, G15, E43, H63

Keywords:

Term Premium; United Kingdom

Author's E-Mail Address:

bmosk@imf.org

SELECTED ISSUES PAPERS

# Why Have UK Gilt Yields Moved Ahead of G7 Peers?

United Kingdom

Prepared by Benjamin Mosk $^{1}$

# UNITED KINGDOM

SELECTED ISSUES

July 2026

## Approved By

Prepared By Benjamin Mosk (MCM)

European Department

## CONTENTS

WHY HAVE UK GILT YIELDS MOVED AHEAD OF G7 PEERS?\_\_\_\_3
A. Introduction \_\_\_\_3
B. Gilt Market Structure and Long-Term Trends \_\_\_\_7
C. Analysis of Term Premium Drivers and Dynamics \_\_\_\_12
D. Discussion and Recommendations\_\_\_\_23

## FIGURES

1. G7 Long-Term Yields \_\_\_\_ 4
2. UK Term Premium Decomposition \_\_\_\_ 5
3. UK & G7 Yield Changes Since 2022 \_\_\_\_ 6
4. Sovereign Debt Structure \_\_\_\_ 8
5. Maturity Distribution and Pension Fund Size \_\_\_\_ 8
6. Gilt Holdings \_\_\_\_ 9
7. Term Premium and Investor Base \_\_\_\_ 10
8. Sovereign Bond Market Size \_\_\_\_ 11
9. Government Debt \_\_\_\_ 11
10. Credit Ratings \_\_\_\_ 12
11. Economic Policy Uncertainty \_\_\_\_ 12
12. Factor Analysis of Yield Dynamics \_\_\_\_ 15
13. Term Premium Shock Decomposition \_\_\_\_ 17
14. G7 Panel Regression Coefficients \_\_\_\_ 19
15. UK Term Premium Sensitivity to Economic Policy Uncertainty \_\_\_\_ 20
16. Gilt Yield Volatility \_\_\_\_ 21

## TABLE

1. Overview of Empirical Approaches \_\_\_\_ 13

2. BVAR Sign Restrictions \_\_\_\_ 16

3. G7 Panel Regression \_\_\_\_ 18

4. UK Term Premium Regression 19  
5. Volatility Regression 20  
6. Summary of Findings 22  
ANNEX  
I. Supplementary Data and Empirical Results 25  
References 30

# WHY HAVE UK GILT YIELDS MOVED AHEAD OF G7 PEERS?

Since 2022, UK gilt yields—particularly at long maturities—have risen and moved above G7 peers. Elevated long-term yields increase sovereign borrowing costs and can transmit to financial conditions more broadly, with implications for fiscal sustainability and financial stability. This paper presents stylized facts and a range of complementary empirical analyses to identify the contribution of the UK term premium to higher yields, assess its drivers and derive policy-relevant insights.

The level of UK yields reflects both elevated expected short rates and the term premium. This paper focuses on the latter, which captures the time-varying risk compensation not explained by the expected path of short rates. Empirical evidence points to a coherent set of drivers behind the rise in the UK term premium across two dimensions: (1) a gradual long-term structural change in demand-supply conditions in the gilt market; and (2) a regime shift following the September 2022 gilt market turmoil, after which domestic risk factors have played a larger role and gilt markets have become more prone to volatility spikes.

Against this backdrop, policy should focus on three areas: managing the quantity and composition of bond supply, reinforcing policy credibility, and strengthening market resilience.

## A. Introduction

1. While gilt yields had declined and remained broadly in the middle of the G7 range for much of the 2010s, they have risen and moved ahead of G7 peers in the past few years. This divergence is particularly pronounced at the long end of the curve, with 30-year gilt yield increasing more sharply relative to other G7 sovereigns (see Figure 1). $^{1}$ This shift began in 2022, coinciding with the gilt market turmoil following the September 2022 “mini budget” announcement, marking a clear break from previous dynamics.

Figure 1. G7 Long-Term Yields  
![](images/88811bd50bf0a1c6c1521de7a816c40a3e491cad919af41a2625942ea561fbe8.jpg)

![](images/45491fc709ab0307f397c26065d7aafb75a0402494fff5cf85722c78e0f81fdf.jpg)  
Sources: Refinitiv Datastream, and IMF staff calculations. Blue area indicates range of yields of G7 peers.

2. Over the past two years, increases in the UK term premium have more than offset declines in expected short rates, bringing long-term yields to their highest level since 2008. $^{2}$ Sovereign borrowing costs can move for different reasons. At longer maturities, yields can generally be decomposed into the expected path of future short-term interest rates and a term premium compensating investors for risk. In advanced economies, short rates are largely determined by the central bank's policy rate, which is set to achieve price stability. In the UK—similar to other economies—policy rates were raised sharply during the post-pandemic period of elevated inflation, driven by supply chain disruptions and pent-up demand, and further amplified by the energy price shock following Russia's invasion of Ukraine. While expected short rates have declined gradually since mid-2023, the UK term premium has increased, preventing longer-term yields from falling accordingly (see Figure 2). Decompositions based on the Bank of England's (BoE) term structure models similarly attribute 2025 movements in UK long-term yields primarily to changes in the (real) term premium (Panigrahi and Sidhu, 2026). These observations raise the question of what has driven long-term UK gilt yields—and the term premium in particular—to rise ahead of G7 peers, and what could be done to reverse this trend.

Figure 2. Term Premium Decomposition  
![](images/c3f94b01e3a246d62fef8bbecfd75870713ce1b53c95a3206e1aa14c4285b8de.jpg)  
Source: Bloomberg, IMF staff calculations. Latest data: 5/31/2026.

3. The expected path of short rates and the term premium are influenced by different policy channels. The expected path of short rates reflects monetary policy decisions in response to macroeconomic conditions, including exogenous shocks to inflation and growth, but is also shaped—albeit indirectly—by fiscal policy and underlying macroeconomic features of the economy. By contrast, the term premium captures risk compensation, uncertainty, and bond market structure factors, such as changes in the investor base. As a result, while short-rate expectations adjust in part to broader economic conditions, credible and predictable policies—particularly in fiscal policy, debt management, and efforts to enhance market functioning—can help contain the term premium by reducing uncertainty and improving the market's capacity to absorb shocks.

4. This paper focuses on the term premium, which can vary independently of monetary policy expectations and has been a key driver of higher long-term yields in recent years. Over 2022–26, both expected short rates and the term premium have contributed to increases in long-term gilt yields (see Figure 3). In March 2026, UK CPI inflation was highest among G7 peers—and had been on the higher end of the range since the mid of 2023 (Annex Figure 17). Commensurately, the UK policy rate was also on the upper end of the G7-range in recent years (Annex Figure 18). However, looking at the mid-2023 to early-2026 period, expected short rates declined (Figure 2), and an increase in the term premium (see Figures 2 and 3) was the primary force behind the rise in long-term yields to their highest levels since 2008. Most recently, the contribution of expected short-term rates to long-term yields jumped at the start of the 2026 conflict in the Middle East, as markets repriced for higher inflation expectations in response to the energy price shock—this illustrates how the short rate component reacts to exogenous shocks.

Sources: Bloomberg, and IMF staff calculations.
Note: Yield and component changes since 1/1/2022 until 5/31/2026.

Figure 3. UK & G7 Yield Changes Since 2022  
![](images/5bb9ed0ab39657b5694c2c22e6263b43c6fbad406a0287e69c6db72eaa3aaf05.jpg)

![](images/ca2968eec0ca77f6e3a2710c2412c4bbf88ddfe9df95e4a29d054841967b605e.jpg)

5. Term premia are shaped by a combination of financial, macroeconomic, policy, and structural supply-demand factors. A substantial body of literature examines the determinants of sovereign bond term premia. Foundational work focuses on the measurement of term premia using no-arbitrage term structure models, notably Kim and Wright (2005) and Adrian, Crump, and Moench (2013), which provide widely used decompositions of long-term yields into expected short rates and risk compensation. Building on these measures, the return-predictability literature demonstrates that term premia are time-varying and predictable using financial indicators such as forward rates (Cochrane and Piazzesi, 2005). Another important strand emphasizes the role of supply and demand factors within preferred-habitat or market segmentation frameworks. Vayanos and Vila (2009, published 2021) provide the theoretical foundation, while Greenwood and Vayanos (2014) show empirically that government bond supply of and investor demand for duration influence term premia. The impact of monetary policy and central bank balance sheets has also been extensively studied; Krishnamurthy and Vissing-Jorgensen (2011) and Hanson and Stein (2015) document how large-scale asset purchases affect long-term yields through duration removal and portfolio balance channels. Finally, a growing literature highlights the importance of global risk and policy uncertainty. Miranda-Agrippino and Rey (2020) emphasize the role of the global financial cycle, while Leippold and Mueller (2022) show that economic policy uncertainty can significantly affect the yield curve and term premia. Together, these strands underscore that term premia are shaped by a combination of financial, macroeconomic, policy, and structural supply-demand factors. The foundational literature is largely based on US data; UK-focused work is limited. For example, Kaminska and Mumtaz (2022) show that QE affects gilt yields through multiple channels—including signaling, policy uncertainty, and bond-supply effects—with the latter two operating through term premia. Stehn (2025) assesses drivers of the UK term premium and finds a positive relationship with unemployment, debt, inflation uncertainty and foreign term premia. Kadiric (2022) shows that the Brexit referendum materially affected sovereign risk premia (although not directly assessing the impact on the term premium).

Lengyel (2026) finds that higher-than-expected sovereign debt issuance raises yields by increasing both real term premia and inflation risk premia, with these effects becoming more pronounced during periods of market stress. This note adds a cross-country perspective combined with UK-focused analysis.

6. This Selected Issues Paper is structured as follows. Section B presents key stylized facts on the evolution of UK gilt yields in a G7 context, focusing on relevant long-term trends. Section C addresses the puzzle of why UK gilt yields have risen above G7 peers by combining multiple complementary empirical approaches, with a focus on the term premium and its drivers. Section D discusses policy implications.

## B. Gilt Market Structure and Long-Term Trends

7. This section provides structural context for recent term premium dynamics by examining key features of the UK gilt market. It presents stylized facts on the investor base, market liquidity, and sovereign credit profile, with a focus on long-term trends and cross-country comparisons. These structural characteristics are difficult to capture in empirical models but are essential for interpreting recent developments in gilt yields and term premia.

## Gilt Market's Investor Base

8. The UK's debt structure has historically reflected investors' strong demand for long-term bonds, which helped to contain the term premium despite a long average maturity. The UK debt's weighted average maturity is just under 14 years, compared to 6 to 9 years for other G7 countries (see Figure 4). This reflects the Debt Management Office's long-standing strategy of issuing a large share of long-dated bonds, alongside a relatively high proportion of inflation-linked securities and a limited reliance on short-term bills. A key factor underpinning this strategy has been strong demand from the UK's sizable defined benefit pension fund sector, which has a natural preference for long-term bonds and inflation-linked assets to match its liabilities (see Figure 5). $^{3}$ This stable demand at the long end of the curve has enabled the DMO to maintain a high average maturity, thereby reducing rollover risk at relatively modest cost.

The UK stands out with its high average maturity and large share of inflation linked bonds

Figure 4. Sovereign Debt Structure

Sovereign Debt Weighted Average Maturity (Years)

![](images/5a5b58638d469aa0217e4c62f9dfd24a4fcae055fe3c1cb008ba18c29b288621.jpg)  
Source: Bloomberg, IMF staff calculations. Reference date: 2/12/2026.

![](images/20aeb44b03892708692fdedeb4e9980d0a002fde777d4bea12da5b1c54f97cee.jpg)

## Figure 5. Maturity Distribution and Pension Fund Size

Amongst G7 countries, the UK has the largest share of bonds with maturity >30 years. The UK has a large defined benefit pension fund sector, with long-term interest rate exposures on the liability side.

G7 Sovereign Debt Maturity Distribution (Percent)

![](images/0f7577ac7965f7aaa844d472b6b0b02c6464bb9f67d188e41921fdfd61c0bb90.jpg)  
Sources Bloomberg, and IMF staff calculations. Reference date: 2/12/2026.  
Pension Fund Assets as Percentage of GDP (Percent)

![](images/d152a4ed952ab8b1605c8c7a8211ad07077f02a39a9a90b785cf52dcc5a38115.jpg)  
Source: OECD. DB = defined benefit. DC=defined contribution. Note: breakdown between DB and DC is not available for all countries. 2024.

9. However, gilt demand is shifting, with weaker domestic institutional demand and greater foreign participation, resulting in a less stable investor base. UK pension funds are increasingly shifting from defined benefit to defined contribution schemes, and their holdings of gilts have declined both in absolute and relative terms. While insurance corporations and pension funds have reduced their share of gilt holdings over the past two decades, the BoE partly offset this by becoming a significant and stable holder through its asset purchase programs (Figure 6). With quantitative tightening now ongoing, however, the Bank is reducing its holdings. At the same time, foreign participation in the gilt market has increased, potentially bringing a larger share of more price-sensitive “fast money” investors and exposing the market to more volatile capital flows. The

trend of declining pension fund gilt holdings is expected to continue (Office for Budget Responsibility, 2025), in part due to a volume effect, but also due to the shift from defined benefit schemes to defined contribution schemes (see Annex Figure 21). The Office for Budget Responsibility estimates that the decline in the pensions sector's gilt holdings could push up interest rates on government debt by around 0.8 percentage points, assuming the stock of debt remains close to 100 per cent of GDP (Office for Budget Responsibility, 2025).

## Figure 6. Gilt Holdings

The share of gilts held by the insurance corporation and pension fund sector has declined, while foreign holdings have increased.

UK Gilt Market Holding Structure by Sector (Percent)

![](images/3c7182be79d2317f4394020440c05fe6f3b2c2e752f8b695e18cb035ca6c502a.jpg)  
Defined Benefit Pension Scheme Gilt Holdings (GBP billion)

![](images/7efe06f439708f9a98c16c2bf6c0b12962c8705a4108d0512bb8fe725c299b31.jpg)  
Sources: HM Treasury, Office for National Statistics, and IMF staff calculations. MFI = monetary financial institutions. ICPF = insurance corporations and pension funds. OFI = other financial institutions. Sectoral holdings in the UK financial accounts are subject to limitations related to data granularity, coverage gaps, and the constraints of traditional survey-based methodologies.  
Sources: Office for National Statistics, and IMF staff calculations. LDI = liability-driven investment.

10. The shift in the investor base may have contributed to a higher term premium. A commonly cited explanation for the increase in long-term yields is a decline in structural demand for gilts, particularly at longer maturities. Empirically, however, the strength of this relationship is subject to uncertainty, as the relevant variables are slow-moving and observed at low frequency, making it challenging to distinguish genuine relationships from coinciding trends. To provide a high-level perspective, an index is constructed that captures the share of foreign holdings relative to more stable holders—namely the central bank, insurance corporations, and pension funds (see below). This indicator shows a positive correlation with the term premium (Figure 7), suggesting that a shift toward more price-sensitive investors may be associated with higher required compensation for holding gilts.

Holders Vulnerability Index =

Share of gilts held by foreign investors

Share of gilts held by Central Bank, Insurance Corporations and Pension Funds

This relationship should be interpreted with caution: the UK does not necessarily stand out in terms of the share of foreig

[中间内容因长度限制已省略]

t country level.*p&lt;0.10, **p&lt;0.05, ***p&lt;0.01</td></tr></table>

## D. Background on UK Time Series Regression

<table><tr><td colspan="2">Table I.3. United Kingdom: Term Premium Regression</td></tr><tr><td colspan="2">Time series regression, UK, Monthly Data, Dependent Variable Term Premium</td></tr><tr><td></td><td>(1)</td></tr><tr><td></td><td>D.tp</td></tr><tr><td>Net issuance</td><td>4.068***</td></tr><tr><td></td><td>(1.001)</td></tr><tr><td> $\Delta U_{t}^{policy}$ </td><td>-0.006</td></tr><tr><td></td><td>(0.018)</td></tr><tr><td>post $_{Sep.2022}$ </td><td>1.111</td></tr><tr><td></td><td>(1.794)</td></tr><tr><td>post $_{Sep.2022}$  x  $\Delta U_{t}^{policy}$ </td><td>0.064**</td></tr><tr><td></td><td>(0.026)</td></tr><tr><td>Constant</td><td>0.090</td></tr><tr><td></td><td>(0.788)</td></tr><tr><td>Observations</td><td>304.000</td></tr><tr><td colspan="2">Notes: Standard errors in parentheses. Newey-West standard errors (lag 4). Includes issuance (3-month change) and policy uncertainty interaction with a dummy that takes the value of 1 during and after September 2022.* p &lt; 0.10, ** p &lt; 0.05, *** p &lt; 0.01</td></tr></table>

## E. Background on UK BVAR Analysis

The BVAR sample consists of daily data spanning 2004-2026. Sign-restrictions (Table 2) are imposed on the first two periods of the impulse response functions (0-2). The analysis uses a standard Minnesota prior, and a 4-period lag-structure.

![](images/3e863cf2585a088f392c7b784e2932193defd94b2d3a1fbf63dab60a0dd6f8d7.jpg)  
Sources: Bloomberg, and IMF staff calculations using the BEAR Toolbox (Dieppe, van Roye and Legrand, 2016).

## References

Adrian, Tobias, Richard K. Crump, and Emanuel Moench. 2013. Pricing the Term Structure with Linear Regressions. Journal of Financial Economics, 110(1), 110–138.

Baker, Scott R. & Nicholas Bloom & Steven J. Davis, 2015. "Measuring Economic Policy Uncertainty," CEP Discussion Papers dp1379, Centre for Economic Performance, LSE.

Brandt, Lennart & Saint Guilhem, Arthur & Schröder, Maximilian & Van Robays, Ine, 2021. "What drives euro area financial markets? The role of US spillovers and global risk," Working Paper Series 2560, European Central Bank.

Cochrane, John H., and Monika Piazzesi. 2005. Bond Risk Premia. American Economic Review, 95(1), 138–160.

Dieppe, Alistair & van Roye, Björn & Legrand, Romain, 2016. "The BEAR toolbox," Working Paper Series 1934, European Central Bank.

Don H. Kim & Jonathan H. Wright, 2005. "An arbitrage-free three-factor term structure model and the recent behavior of long-term yields and distant-horizon forward rates," Finance and Economics Discussion Series 2005-33, Board of Governors of the Federal Reserve System (U.S.).

Giese, Julia, Michael Joyce, Jack Meaning and Jack Worlidge (2023). "Preferred habitat investors in the UK government bond market", Bank of England Staff Working Paper No. 939

Greenwood, R and Vissing-Jorgensen, A., "The Impact of Pensions and Insurance on Global Yield Curves", Harvard Business School, Working Paper 18-109, 2018.

Hanson, Samuel G. & Stein, Jeremy C., 2015. "Monetary policy and long-term real rates," Journal of Financial Economics, Elsevier, vol. 115(3), pages 429-448.
https://doi.org/10.1016/j.jfineco.2014.11.001

International Monetary Fund (2025), October 2025 Global Financial Stability Report, Annex 1.7. https://www.imf.org/-/media/files/publications/gfsr/2025/october/english/ch1annex.pdf

Kadiric S, (2022). The determinants of sovereign risk premiums in the UK and the European government bond market: the impact of Brexit. Int Econ Econ Policy. 2022;19(2):267-298.

Kaminska, Iryna and Haroon Mumtaz (2022). Monetary policy transmission during QE times: role of expectations and term premia channels. Bank of England Staff Working Paper No. 978

Krishnamurthy, A., Vissing-Jorgensen, A., Gilchrist, S., & Philippon, T. (2011). The Effects of Quantitative Easing on Interest Rates: Channels and Implications for Policy [with Comments and Discussion]. Brookings Papers on Economic Activity, 215–287.
http://www.jstor.org/stable/41473600

Leippold, Markus, Felix Matthys, Economic Policy Uncertainty and the Yield Curve, Review of Finance, Volume 26, Issue 4, July 2022, Pages 751–797, https://doi.org/10.1093/rof/rfac031

Lengyel, Andras (2026). Government bond issuance surprises and the term structure of interest rates in the UK, Journal of Banking & Finance, Volume 189, 2026, 107715

McCauley, Robert and Eli Remolona, 2000. "Size and liquidity of government bond markets," BIS Quarterly Review, Bank for International Settlements, November.

Office for Budget Responsibility (2025). "Fiscal risks and sustainability". CP 1343, July 2025

Organisation for Economic Co-operation and Development (2026). "Global Debt Report 2026". 4 March 2026

Panigrahi, Lisa and Amarjot Sidhu, 2026. "What were the drivers of UK long-term interest rates in 2025?", Bank of England. https://www.bankofengland.co.uk/bank-insights/2026/what-were-the-drivers-of-uk-long-term-interest-rates-in-2025

Robin Greenwood, Dimitri Vayanos, Bond Supply and Excess Bond Returns, The Review of Financial Studies, Volume 27, Issue 3, March 2014, Pages 663–713, https://doi.org/10.1093/rfs/hht133

Silvia Miranda-Agrippino, Hélène Rey, U.S. Monetary Policy and the Global Financial Cycle, The Review of Economic Studies, Volume 87, Issue 6, November 2020, Pages 2754–2776, https://doi.org/10.1093/restud/rdaa019

Stehn, Sven Jari (2025). "How Vulnerable are the UK's Public Finances?" Goldman Sachs Research, 26 September 2025

Vayanos, D. and Vila, J.-L. (2021), A Preferred-Habitat Model of the Term Structure of Interest Rates. Econometrica, 89: 77-112. https://doi.org/10.3982/ECTA17440
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
