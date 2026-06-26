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
# Assessing Macrofinancial Linkages in China Using a Machine-Learned Parsimonious VAR Model

Prepared by Jin-Chuan Duan, Dimitrios Laliotis, and Wei Sun

WP/26/134

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN

![](images/c387ab467a48b01c7c180a84a6917040d6b6bcd2ee8ca8647793bc0fe387ffba.jpg)

# IMF Working Paper Monetary and Capital Markets Department

Assessing Macrofinancial Linkages in China Using a Machine-Learned Parsimonious VAR Model Prepared by Jin-Chuan Duan\*, Dimitrios Laliotis\*\*, and Wei Sun\*\*,

Authorized for distribution by Hiroko Oura
June 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper examines macrofinancial linkages between property developers, financial institutions, and macroeconomic outcomes in China. Using a parsimonious vector autoregressive (VAR) model enabled by a machine learning algorithm, it quantifies how idiosyncratic shocks can propagate and be amplified across sectors, with potential implications for financial stability. Stress originating from privately owned developers and regionally focused financial institutions—though relatively limited in scale—can generate persistent spillovers through lending relationships, common exposures, shared markets, and changes in market sentiment. A decline in property prices may undermine investment, weaken consumer confidence, and adversely affect the health of both the property and financial sectors, thereby disrupting financial intermediation and weighing on broader economic growth. Policy considerations should take into account these feedback loops. Market- and exposure-based tools can be helpful for monitoring macrofinancial linkages and assessing the transmission of shocks.

<table><tr><td>JEL Classification Numbers:</td><td>C3, E44, G2, R3</td></tr><tr><td>Keywords:</td><td>Macrofinancial linkage; property development; financial system; machine learning; model selection</td></tr><tr><td>Authors&#x27; email addresses:</td><td>wsun@IMF.org</td></tr></table>

WORKING PAPERS

# Assessing Macrofinancial Linkages in China Using a Machine-Learned Parsimonious VAR Model

Prepared by Jin-Chuan Duan, Dimitrios Laliotis, and Wei Sun

## Contents

I. Introduction .... 3
II. Literature Review .... 5
III. Methodological Design.... 6
Data .... 7
Model Selection .... 9
IV. Empirical Results.... 10
Model Estimation .... 10
Impulse Response .... 13
V. Conclusion .... 17
References.... 18

## FIGURES

1. Impulse Response: 1 Basis Point Shock to PD of Privately-owned Developers....14
2. Impulse Response: 1 Basis Point Shock to PD of City Commercial Banks....15
3. Impulse Response: 1 Percentage Point Shock to Property Prices....16
4. Impulse Response: 1 Percentage Point Shock to Consumer Confidence Index....16

## TABLES

1. Intertemporal Relationships: Regression Coefficients .... 12
2. Contemporaneous Relationships: Covariance of Disturbance.... 13

## I. Introduction

Macrofinancial stability is a central objective of the global policy agenda. A succession of banking and financial crises since the 1980s has underscored that financial stability—alongside price stability—is essential for macroeconomic resilience. The global financial crisis of 2007-09 highlighted the profound impact of macrofinancial linkages, prompting a shift in global economic policy toward a more macroprudential direction (Claeseens, 2015; Adrian, 2017b; and IMF-FSB-BIS, 2016). These efforts aim to address propagation and amplification effects through complex linkages that traditional monetary and exchange rate tools cannot fully manage (Borio et al., 2022).

Macrofinancial linkages refer to the two-way interactions between the macroeconomy and the financial sector (Claessens and Kose, 2018). Economic shocks can impair the balance sheets of households, firms, and financial intermediaries. Amplified by financial market imperfections, such impairments can disrupt both the demand (e.g., financial accelerator effects) and supply (e.g., bank lending, capital, leverage, liquidity constraints) of financial intermediation, intensifying economic fluctuations. Financial imbalances—such as rapid credit growth and asset price swings—can distort macroeconomic equilibrium and often precede or deepen recessions if not addressed promptly (Claessens et al., 2012a).

While research on macrofinancial linkages continues to advance, challenges persist due to data limitations and methodological constraints. Large gaps remain in balance sheet data, bilateral exposures, and high-frequency asset price series critical for systemic risk assessment (Brunnermeier and Krishnamurthy, 2014). Theoretical models, including dynamic stochastic general equilibrium (DSGE) frameworks, struggle to capture agent heterogeneity, demonstrate transmission channels, or yield robust predictions under different institutional setups (Blanchard, 2017a).

This paper contributes to the evolving literature by assessing macrofinancial linkages in China—now the world’s second-largest economy and home to the second-largest financial system. China’s growth model, heavily reliant on real estate investment until recently and supported by increasingly complex and interconnected financial intermediation that does not fully reflect risk-return relationships (IMF, 2025), has given rise to intricate macrofinancial linkages with potentially profound macroeconomic consequences.

Conjunctural shocks have made this analysis particularly timely. Since 2021, China's property market has experienced its most severe adjustment in decades. Sales and prices in the primary market have declined. Secondary market corrections have been more pronounced, despite a temporary rebound around early 2025. Defaults among property developers—varying in size and ownership structure—have increased. The accumulation of unused land, unfinished projects, and undelivered housing units has inflicted significant socioeconomic costs.

This paper uncovers the interconnectedness among key economic agents and activities influenced by and impactful for property market performance. A vector autoregressive (VAR) model is used to capture general equilibrium features and endogenous responses. Through identified transmission and amplification channels, we quantify the extent to which an idiosyncratic shock can generate far-reaching and long-lasting effects.

A key feature of the paper is to analyze macrofinancial linkages founded on microeconomic behaviors (Claessens and Kose, 2018). The model includes three property development and five financial sectors, each facing distinct constraints in responding to shocks. State-owned developers have easier access to bank financing, while privately owned developers often rely on costlier funding and lose market access during periods of stress. State-owned banks are relatively stably funded and serve safer borrowers, while smaller banks engage in riskier financial market transactions and lend to developers. Non-bank financial institutions support capital allocation to non-state-owned sectors, often offering implicit guarantees until recent regulatory tightening (Allen et al., 2023).

To address data limitations related to balance sheets and bilateral exposures, we use probability of defaults (PD) metrics from the Credit Research Initiative (CRI) of the National University of Singapore (NUS-CRI, 2023). The CRI database covers 92,000 companies globally, including all publicly listed property developers and financial institutions in China. As a composite index encompassing market indicators (e.g., stock returns and volatility) and fundamentals (e.g., liquidity, profitability, and leverage), PD co-movements imply bilateral exposures better than purely market-based metrics such as CDS spreads or stock prices (Craig et al., 2024). They also reflect interdependence through sentiment and market perceptions, beyond direct borrowing-lending relationships.

Modeling eight sectoral and three macro variables in a VAR framework presents a high-dimensional challenge. To identify meaningful macrofinancial linkages, we apply a zero-norm penalty to regularize the number of non-zero coefficients (Duan, 2024). Operationally, a 10-fold cross-validated seemingly unrelated regression likelihood is solved using a sequential Monte Carlo (SMC) optimization technique. This novel machine learning approach offers several advantages. It yields a parsimonious model, retains only significant relationships, and does not require a priori specification of directional links. It is fully interpretable, avoiding the “black box” nature of many models and supporting transparent policy analysis (Duan, 2025).

Our empirical analysis reveals critical linkages between macroeconomic performance, property developers, and financial institutions. Vicious cycles can emerge through these linkages, amplifying idiosyncratic shocks. Notably, stress among privately owned developers can affect state-owned developers and financial institutions in subsequent periods. Even smaller, regionally focused banks can have systemic implications. Property prices lie at the core of these linkages, with declines triggering adverse effects on investment, sentiment and financial sector health.

The empirical analysis suggests that a well-capitalized and stably funded financial system is associated with a greater capacity to sustain credit and liquidity provision. Potential trade-offs could arise between measures affecting property developers and broader considerations of financial sector resilience. Stabilizing property prices is more effective when aligned with broader efforts to restore business and consumer confidence durably. A sustainable recovery in the property market is typically characterized by organic transaction growth supported by the financial health of key market participants. Accounting for complex feedback effects helps characterize macrofinancial dynamics over the business cycle.

Market- and composite-index-based analyses offer timely insights into macrofinancial linkages and shock-induced outcomes. They also go beyond lending-borrowing relationships and incorporate business model similarities, common exposures, and market sentiment, increasingly important factors in modern contagion dynamics. Developing comprehensive toolkits to regularly monitor linkages and assess macrofinancial impacts can enhance risk management. Complementary efforts to collect granular cross-sectoral exposures could further deepen the understanding China's macrofinancial complexity.

The remainder of the paper is structured as follows. Section II provides a short survey of the related literature. Section III introduces the design of the methodology. Section IV discusses empirical results. Section V concludes.

## II. Literature Review

This paper builds on two strands of literature. First, it contributes to the study of macrofinancial linkages, which gained prominence following the global financial crisis. The two-way interactions between the financial sector and real economy can propagate and amplify shocks, leaving long-lasting economic scars. Policymakers have struggled to counteract these effects using conventional fiscal, monetary, and financial instruments (Claessens and Kose, 2018).

The literature on macrofinancial linkages highlights the central role of asset prices in driving economic outcomes. In frictionless Arrow-Debreu markets, asset prices provide signals to economic agents for optimal consumption and investment decisions (Geanakoplos, 2008). Asset price movements affect household wealth over the life cycle, therefore influencing consumption and saving patterns (Deaton, 1992; Guiso and Sodini, 2013). They also inform future corporate profitability (Allen, 1993) and influence investment plans. Recessions accompanied by asset price busts tend to be deeper and longer (Claessens et al., 2012a; Drehmann et al., 2012; and Muir, 2017). Among asset classes, house prices have a more pronounced impact on consumption than equity prices (Carroll et al., 2011; Case et al., 2005, 2013; Kim, 2004; Gan 2010).

Financial imperfections amplify the impact of shocks on real economy due to information asymmetry and enforcement difficulty. On the demand side, the financial accelerator theory explains how initial shocks affect credit demand and subsequent spending and investment decisions. Most notably, weakening balance sheets and cash flows disrupt access to finance or increase costs. The additional premiums reduce income and profitability, postpone consumption or productive activities, which in turn makes it even more challenging to secure future financing (Antony and Broer, 2010; BCBS, 2011; Coric, 2011; Quadrini, 2011).

On the supply side, banks may curtail lending during distress due to uncertainty (e.g., Bernanke and Blinder, 1988; Stein, 1998). They may shun the risky borrowers for capital preservation motives (Bernanke and Lown, 1991; Holmström and Tirole, 1997; Repullo and Suarez, 2000; Van den Heuvel, 2006, 2008). Procyclical leverage (Adrian and Shin, 2008, 2011a; Geanakoplos, 2010) can constrain access to finance, affecting both banks and non-bank financial institutions. Interbank market freezes can induce credit crunches (Freixas and Jorge, 2008; Bruche and Suarez, 2010), and deleveraging and liquidity hoarding can exacerbate financial and economic stress.

In China, property market fluctuations significantly influence business cycles (Ge et al., 2022). Rising property prices in the past decades have supported fiscal spending via local governments land sales and off-balance sheet borrowing with land collaterals (Chen et al., 2020). Rising prices have also supported

consumption via wealth effects because households invest vast savings in this preferred vehicle yielding outstanding returns (Fang et al., 2015). The traditional banking sector supported property development until the contractionary monetary policies post-2009 (Chen, et al., 2018). Non-bank financial institutions later filled the gap, offering implicit guarantees until recent regulatory changes (Allen et al., 2023).

The second strand of literature focuses on model selection for high dimensional data. Regularization techniques address the challenge of too many regressors and too few observations. The Least Absolute Shrinkage and Selection Operator (LASSO) method (Tibshirani, 1996) introduces an $L^{1}$ -norm penalty to the original optimization problem. It optimizes the target function by shrinking the sum of the absolute values of the coefficients, leaving many of them to zero.

Later efforts advanced the $L^{1}$ -norm based methodology by achieving the oracle properties, meaning they perform as well as if the underlying model were known in advance (Fan and Li, 2001). Examples include the Smoothly Clipped Absolute Deviation (SCAD) method by Fan (1997). Fan and Li (2001) generalized the SCAD method to more parametric and nonparametric models and developed an algorithm to improve its computational efficiency. Different from applying fixed weights in the original LASSO method, the Adaptive Lasso of Zou (2006) used different weights to penalize the coefficients based on their relative importance, while also producing consistent model estimates.

Regressions with zero-norm penalty restrict directly the number of non-zero coefficients rather than the sum of the absolute values. These types of models are conceptually natural for tackling high dimensionality but are computationally demanding (Natarajan, 1995). With modern machine learning techniques, Duan (2024) introduced the Stable Combinatorially-optimized Feature Selector (SCOFS) suitable for various high-dimensional parametric models. SCOFS mitigates multilinearity and overfitting more effectively than LASSO-type methods.

This paper applies SCOFS to assess macrofinancial linkages in China. Empirical evidence suggests that property market shocks have persistent macroeconomic effects. At a micro level, financial and property sectors are interconnected in ways that amplify shocks.

## III. Methodological Design

We designed a penalized VAR model to study the macrofinancial linkages in China. A reduced-form VAR model is not identified without specifying directional relationships a priori. To avoid over-simplified assumptions on a very complex system, we introduced a zero-norm penalty to regularize the number of non-zero coefficients. This approach enables a high-dimensional model with persistent lagged effects. Recent advances in machine learning make this regularization computationally feasible and fully interpretable, unlike “black box” alternatives.

An impulse response exercise subsequently quantifies the impact of idiosyncratic shocks on interested variables over time. It differs from but complements forecast error variance decomposition, which measures volatility spillovers (Diebold and Yilmaz, 2012).

We select 11 macro and sectoral variables to underpin the VAR. They represent economic agents and activities that can be highly dependent on or impactful for the property market. Property prices, consumer sentiment, and real estate investment are proxies to capture the market and macroeconomic conditions. These monthly series are closely related to but are much more frequent and forward-looking than national account data. Prices reflect cash flow expectations and investment opportunities, while consumer sentiment reflects demand pressures and could shape future consumption behaviors.

The sectoral variables comprise probability of defaults (PD) metrics for eight groups of property developers and financial institutions. Unlike exposure or price-based metrics, the composite PD indices incorporate both market and fundamental information, reflecting sectoral health. Our PD-based interlinkage analysis does not aim to isolate a single shock transmission channel. Rather, it captures co-movements that could be driven by both common exposures, business model similarities, market sentiment and lending-borrowing relationships (Craig et al., 2024), revealing an intricate system of interconnected micro sectors.

The choice of 11 variables aims to focus on the basic feedback effects among critical sectors. Given that several variables are composite in

[中间内容因长度限制已省略]

using Boom of China", American Economic Journal: Macroeconomics, 9(2), 73-114.

Chen, Z., Z. He, and C. Liu (2020), “The Financing of Local Government in China: Stimulus Loan Wanes and Shadow Banking Waxes”, Journal of Financial Economics, 137(1), 42-71.

Claessens, S. (2015), “An Overview of Macroprudential Policy Tools”, Annual Review of Financial Economics, Vol. 7, pp. 397–422.

Claessens, S. and M.A., Kose (2018), “Frontiers of Macrofinancial Linkages”, BIS Papers, No. 95.

Claessens, S., M. A. Kose, and M. E. Terrones (2012a), “How do Business and Financial Cycles Interact?” Journal of International Economics, Vol. 87, No. 1, pp. 178–90.

Coric, B. (2011), “The Financial Accelerator Effect: Concept and Challenges”, Financial Theory and Practice, Vol. 35, No. 2, pp. 171–96.

Craig, B., M. Karamysheva, and D. Salakhova (2024), "Do Market-based Networks Reflect True Exposures Between Banks?" ECB Working Paper Series, No 2867.

Credit Research Initiative, National University of Singapore (NUS-CRI, 2023), “NUS Credit Research Initiative Technical Report, 2023 Update 1”.

Deaton, A. (1992), “Understanding Consumption”, Oxford: Clarendon Press.

Diebold, F. and K. Yilmaz (2012), “Better to Give Than to Receive: Predictive Directional Measurement of Volatility Spillover”, International Journal of Forecasting 28, 57-66.

Drehmann, M., C. Borio, and K. Tsatsaronis (2012), “Characterising the Financial Cycle: Don’t Lose Sight of the Medium Term!”, BIS Working Paper 380, Bank for International Settlements, Basel.

Duan, J-C. (2024), “Stable Combinatorially-Optimized Features Selection via Sequential Monte Carlo Optimization”, Working Paper. https://adbiza.com/static/docs/PublishFiles/VariableSelection-SMC\_October-25-2024.pdf

Duan, J-C. (2025), “Interpretable vs Black-box AI in Action”, ADBIZA Whitepaper.
https://adbiza.com/static/docs/PublishFiles/Interpretable%20vs%20Black-box%20AI%20in%20Action.pdf

Duan, J.-C., S. Li, and Y. Xu, 2022, Sequential Monte Carlo Optimization and Statistical Inference, Wiley Integrative Reviews: Computational Statistics, e1598. https://doi.org/10.1002/wics.1598

Duan, J.C., J. Sun and T. Wang, 2012, Multiperiod Corporate Default Prediction – A Forward Intensity Approach, Journal of Econometrics 170, 191-209.

Fan, J. (1997), “Comments on “Wavelets in Statistics: a Review” by A. Antoniadis”, Journal of the Italian Statistical Society, 6(20), 131-138.

Fan, J. and R. Li (2001), “Variable Selection via Nonconcave Penalized Likelihood and its Oracle Properties”, Journal of the American Statistical Association, 96, 1348-1360.

Fang, H., Q. Gu, W. Xiong, and L. Zhou (2015), “Demystifying the Chinese Housing Boom”, NBER Macroeconomics Annual, Vol 30.

Freixas, X., and J. Jorge (2008), “The Role of Interbank Markets in Monetary Policy: A Model with Rationing”, Journal of Money, Credit and Banking, Vol. 40, No. 6, pp. 1151–76.

Gan, J. (2010), “Housing Wealth and Consumption Growth: Evidence from a Large Panel of Households”, Review of Financial Studies, Vol. 23, No. 6, pp. 2229–67.

Ge, X., X. Li, Y. Li, and Y. Liu (2022), “The Driving Forces of China’s Business Cycles: Evidence from an Estimated DSGE Model with Housing and Banking”, China Economic Review.

Geanakoplos, J. (2008), “Arrow Debreu Model of General Equilibrium,” in The New Palgrave Dictionary of Economics, 2nd edition, S. N. Durlauf and L. E. Blume (eds), Palgrave Macmillan.

Geanakoplos, J. (2010), “The Leverage Cycle” in NBER Macroeconomic Annual 2009, Vol. 24, D. Acemoglu, K. Rogoff, and M. Woodford (eds), pp. 1–65, Chicago: University of Chicago Press.

Guiso, L., and P. Sodini (2013), “Household Finance: An Emerging Field,” in Handbook of the Economics of Finance, Vol. 2, G. M. Constantinides, M. Harris, and R. M. Stulz (eds), pp. 1397–532, Amsterdam: North-Holland.

Holmström, B., and J. Tirole (1997), “Financial Intermediation, Loanable Funds, and the Real Sector”, Quarterly Journal of Economics, Vol. 112, No. 3, pp. 663–91.

IMF (2025), “Financial System Stability Assessment”, People’s Republic of China.

IMF-FSB-BIS (2016), “Elements of Effective Macroprudential Policies: Lessons from International Experience”, Report to the G-20, August 31.

Kim, K. H. (2004), “Housing and the Korean Economy”, Journal of Housing Economics, Vol. 13, pp. 321–41.

Muir, T. (2017), “Financial Crises and Risk Premia”, Quarterly Journal of Economics, Vol. 132, No. 2, pp. 765–809.

Natarajan, B.K. (1995), “Sparse Approximate Solutions to Linear Systems”, SIAM Journal on Computing, 24(2), 227-234.

Quadrini, V. (2011), “Financial Frictions in Macroeconomic Fluctuations”, Economic Quarterly, Vol. 97, No. 3, pp. 209–54, Federal Reserve Bank of Richmond, Richmond.

Repullo, R., and J. Suarez (2000), “Entrepreneurial Moral Hazard and Bank Monitoring: A Model of the Credit Channel”, European Economic Review, Vol. 44, No. 10, pp. 1931–50.

Stein, J. C. (1998), “An Adverse-Selection Model of Bank Asset and Liability Management with Implications for the Transmission of Monetary Policy”, RAND Journal of Economics, Vol. 29, No. 3, pp. 466–86.

Tibshirani, R. (1996), “Regression Shrinkage and Selection via the Lasso”, Journal of the Royal Statistical Society, Ser. B, 58(1), 267-288.

Van den Heuvel, S. J. (2006), “The Bank Capital Channel of Monetary Policy”, Society for Economic Dynamics, Meeting Paper 512.

Van den Heuvel, S. J. (2008), “The Welfare Cost of Bank Capital Requirements”, Journal of Monetary Economics, Vol. 55, No. 2, pp. 298–320.

Zou, H. (2006), “The Adaptive Lasso and Its Oracle Properties”, Journal of the American Statistical Association, 101(476), 1418-1429.

![](images/d4b8a1b010a95febf540ebf94da51f185830cab5acb4a8a6b5178316da0c5ae0.jpg)
"""
