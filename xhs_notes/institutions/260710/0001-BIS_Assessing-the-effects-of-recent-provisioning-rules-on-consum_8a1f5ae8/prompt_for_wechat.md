你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
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
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
![](images/27ce714762a4be128a069f01cd1fcab6b8caf684c687dc36e53ea5ceb1122a1b.jpg)

## BIS Working Papers No 1366

# Assessing the effects of recent provisioning rules on consumer credit allocation in Colombia

by Diego Cuesta-Mora, Fredy Gamboa-Estrada and Camilo Sanchez-Quinto

Monetary and Economic Department

July 2026

JEL classification: E51, E60, G21, G28

Keywords: loan-loss provisions, credit supply, consumer loans, credit risk

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).

ISSN 1020-0959 (print)
ISSN 1682-7678 (online)

# Assessing the Effects of Recent Provisioning Rules on Consumer Credit Allocation in Colombia\*

DIEGO CUESTA - MORA♦ FREDY GAMBOA-ESTRADA§ CAMILO SANCHEZ - QUINTO $^{L}$

## Abstract

Colombia's post-pandemic recovery in 2021–2022 was marked by rapid consumer credit growth, followed by deteriorating credit quality indicators amid tightening financial conditions. In January 2023, the Superintendence of Finance of Colombia (SFC) introduced higher provisioning requirements for long-term consumer loans to enhance financial resilience against credit risk materialization and to help moderate the rapid expansion of consumer credit observed prior to the reform. From the perspective of credit institutions (CIs), increased provisions imply higher expenses and potential profitability pressures, which could lead to adjustments in lending strategies. This study evaluates the effect of that regulatory policy on consumer credit dynamics and CI soundness. We find that the measure increased CIs' provision coverage ratio, indicating progress toward the policy's resilience objective, but it did not significantly affect overall credit supply conditions for longer-maturity loans in terms of loan amounts, interest rates, and collateral requirements. However, these average effects mask notable heterogeneity across institutions. Smaller lenders tightened credit supply for loans whose maturity exceeds 108 months by reducing loan amounts and lowering loan-to-value ratios, while larger lenders absorbed the higher provisioning costs without altering credit terms.

JEL Classification: E51, E60, G21, G28.

Keywords: Loan-loss provisions, credit supply, consumer loans, credit risk.

## 1. Introduction

The Colombian economy experienced a notable recovery during 2021 and 2022 following the severe contraction caused by the Covid-19 pandemic. This rebound was accompanied by real credit growth across all segments, with consumer credit expanding particularly rapidly. A breakdown of this segment shows that personal loans and credit card lending accounted for the largest share of this dynamism. At the same time, the stance of monetary policy led to a broad-based increase in lending rates across consumer credit products. Moreover, throughout 2022, newly disbursed loans were increasingly granted at maturities longer than five years, even though the overall stock of consumer credit continues to be dominated by loans with maturities shorter than five years (Cuesta-Mora et al., 2022).

From the second half of 2022 onward, however, the acceleration in consumer credit coincided with a deterioration in credit quality indicators, including rising short-term delinquency rates. Although loan-loss provisions continued to grow, their pace slowed relative to the previous year; nonetheless, the provision coverage ratio remained at historically high levels. These developments unfolded against a macroeconomic outlook characterized by rising inflation, tighter monetary conditions, slowing economic activity, and increasing unemployment. Given that 2023 was expected to bring a further deceleration of the economy, with interest rates remaining elevated and inflation above the Central Bank of Colombia's target, pressures on households' repayment capacity intensified, raising concerns about the sustainability of consumer credit growth and underscoring the importance of continued monitoring of these trends.

In response to these challenges, the Superintendence of Finance of Colombia (SFC)—the regulatory authority overseeing the financial system—issued External Circular 026 of 2022 on November 29, 2022. This regulation introduced new guidelines for credit institutions (CIs) on the provisioning of consumer loan risk, aiming to promote the healthy and sustainable growth of this portfolio while recognizing the potential deterioration in borrowers' repayment capacity amid economic slowdown and persistent inflation. Effective January 1, 2023, CIs were required to incorporate the risk associated with long-term leverage into the calculation of individual provisions for new consumer loans, excluding credit cards, revolving credit, and pensioner loans. Specifically, for new loans with maturities exceeding 72 months and 108 months, provisions had to be increased by 10% and 40%, respectively, relative to the amounts calculated under the existing expected loss model.

Regulatory changes of this type are commonly expected to influence credit supply conditions and the characteristics of newly originated loans. Existing literature on macroprudential and supervisory interventions in Colombia finds that tighter regulatory requirements—particularly those related to countercyclical provision schemes for commercial loans—can affect loan supply and its characteristics (López et al., 2014; Gómez et al., 2020; Morais et al., 2021; Cabrera et al., 2025). Nevertheless, empirical evidence on the effects of provisioning-based regulatory measures remains limited, especially in the context of emerging economies and consumer credit portfolios. Therefore, the introduction of maturity-specific provisioning requirements provides an opportunity to examine how higher regulatory costs associated with long-term lending affect consumer loan supply decisions and the allocation of credit across maturities.

The contribution of this paper is threefold. First, using granular supervisory data, it evaluates the effects of the 2022 macroprudential policy measure that updated the expected loss-based provisioning rules on supply conditions of new long-term loans, including loan amounts, interest rates, and collateral requirements. Second, it examines the heterogeneity of institutional responses by analyzing how lenders with different market positions adjusted to the higher provisioning requirements applied at the 72- and 108-month thresholds. Third, the analysis employs advanced matching methodologies that address issues such as imbalance, inefficiency, model dependence, and bias that typically arise in widely used causal inference techniques like propensity score matching, which have been prevalent in prior studies on Colombia (López et al., 2014). By doing so, we provide new insights into the interaction between regulatory measures, credit market behavior, and financial stability in emerging economies.

Our results indicate that the introduction of maturity-specific provisioning requirements did not lead to a contraction in the supply of long-term consumer credit. Contrary to concerns that higher provisioning costs would reduce loan amounts or tighten contract terms, we find no significant effects on loan volumes, interest rates, or collateral requirements for those loans in terms of loan-to-value ratios. Instead, the regulation increased coverage ratios, thereby strengthening the capacity of credit institutions to absorb potential losses. However, we also find that smaller institutions tightened credit standards for loans with maturities above 108 months—reducing both disbursed capital and loan-to-value (LTV) ratios. These asymmetric responses highlight the importance of financial institutions' market share in the consumer credit segment and their balance sheet strength in shaping the transmission of provisioning-based regulation. Taken together, the results suggest that macroprudential policies focused on broad, system-wide provisioning requirements may have more pronounced effects on credit supply conditions than maturity-specific provisioning schemes that target only a narrow segment of the loan portfolio. Additionally, because the policy measure studied in this paper coincided with a period of contractionary monetary policy, its effects on credit supply were marginal, and the policy rate likely had a stronger influence on the dynamics of consumer loans. Overall, these findings suggest that the reform improved the preparedness of CIs for potential defaults on longer-term loans, thereby supporting their overall resilience against credit risk materialization.

This article consists of five sections including this introduction. The second section describes the background on changes of the provisioning framework in Colombia and reviews prior literature. The third section describes the data and presents descriptive statistics. The fourth section presents the econometric approach and the main results. The last section summarizes the findings and discusses policy implications.

## 2. Contextual background and literature overview

## 2.1. Background on changes to the loan portfolio provisioning framework in Colombia

Since 2002, Colombia's prudential regulation evolved from a reactive, cyclical approach to a risk-sensitive, forward-looking framework that integrates countercyclical buffers and loan-loss provisions based on expected loss models. This transition reflects a broader trend toward prudential regulation aligned with global standards (e.g., Basel III, IFRS 9), aiming to enhance financial stability and reduce systemic risk.

Prior to 2002, loan-loss provisioning in Colombia was governed by accounting and supervisory rules that required CIs to increase provisions mainly in response to observed loan delinquency and did not account for macroeconomic conditions. As a result, during economic expansions CIs maintained low levels of provisions, whereas they were sharply increased during downturns, which destabilized earnings and weakened capital adequacy. In 2002, Colombia's financial regulation on loan-loss provisioning evolved to address systemic vulnerabilities caused by procyclicality. SFC introduced a comprehensive reform of the credit risk management framework in 2002, known as the Sistema de Administración de Riesgo de Crédito (SARC, External Circular 11). SARC established a structured approach to identifying, measuring, and monitoring credit risk at the institutional level, requiring credit institutions to develop internal processes, information systems, and governance arrangements to support risk management. Its implementation was carried out in phases, allowing institutions to progressively adapt their systems and reporting capabilities.

Within this broader risk management framework, the SFC later in 2007 introduced a countercyclical provisioning tool—drawing inspiration from Spain’s 2000 model. The objective was to maintain a stable ratio of provisions-to-loan portfolio throughout credit cycles, thereby reducing volatility and strengthening financial resilience. Under the mechanism, banks accumulated additional provisions during credit expansions and released them during downturns. These countercyclical provisions (CIC) were defined as the difference between current and long-term average provisions. By mitigating the procyclicality of profits and fostering stability in the entity’s credit growth, these measures enhanced resilience of the financial system—a desirable outcome for regulators—while reducing uncertainty regarding future dividends and profitability $^{1}$ , which is advantageous for shareholders.

To ensure practical implementation, SARC introduced a standardized provisioning methodology, known as the reference model for expected loss (Chapter 31 of the Circular Básica Contable y Financiera). $^{2}$ To establish individual provisions that reflect borrowers' credit risk, CIs distinguish across loan portfolio segments. For the housing and microcredit segments, CIs must provision at least 1% of the combined loan portfolio and then apply the deterministic model. In contrast, for commercial and consumer segments, CIs follow the individual provisioning model, which combines procyclical individual (CIP) and countercyclical individual (CIC) components. The CIP represents the portion of the provision that reflects the current credit risk of each borrower, whereas the CIC accounts for potential deterioration in asset quality under adverse economic conditions.

Within the individual provisioning model, CIs must distinguish two phases—accumulation and decumulation—which govern the evolution of CIC over the credit cycle. The calculation of provisions differs across these phases, and transitioning from accumulation to decumulation requires meeting specific conditions, such as a sustained increase in provisions and moderate growth in the consumer loan portfolio (Appendix A). Despite these phase-dependent rules, the input used to compute provisions remains unchanged: loan exposure, risk matrices, adjustment factors, and expected loss. Loan exposure is determined by the outstanding balance of the loan, while risk matrices and adjustment factors are predefined by regulation and vary across loan sub-segments, collateral types, and borrower risk ratings.

Expected loss is computed as shown in Equation 1, where the probability of default (PD) represents the likelihood that a borrower will default within the next 12 months. This parameter is critical because it captures the forward-looking credit risk of the portfolio. PD is estimated using transition matrices under both normal conditions and stress scenarios (Appendix B). The exposure at default (EAD) measures the total exposure at the time of default—including principal, accrued interest, and other receivables—and is essential because it determines the magnitude of potential losses if default occurs, directly linking credit risk to the size of the outstanding obligation. The loss given default (LGD) indicates the proportion of exposure that is not recoverable after default; LGD is assigned based on the number of days past due following classification in the default category (Appendix C).

$$
E x p e c t e d L o s s = P D * E A D * L G D\tag{1}
$$

Since 2007, the provisioning framework for consumer credit (i.e., the individual provision model) has undergone incremental adjustments aimed at strengthening its sensitivity to emerging risks. In 2012, the SFC introduced a temporary additional provision for consumer loans, activated when delinquency indicators deteriorated, thereby reinforcing buffers during periods of rising household credit risk. Subsequently, in 2016, the framework was refined to account explicitly for loan maturity, requiring expected losses on new consumer loans—excluding credit cards and revolving credit lines—to increase with the remaining repayment horizon. This change recognized that longer maturities expose lenders to greater uncertainty over the credit cycle and updated the expected loss formula to include a fourth term that is triggered when the remaining maturity of a loan exceeds 72 months.

In November 2022, the SFC released External Circular 026, which introduced new instructions for the establishment of provisions for risk on consumer loan portfolios. The new framework requires CIs to incorporate a factor that captures the additional risk associated with higher borrower leverage at longer maturities. For new loans—excluding credit cards, revolving credit lines and payroll loans to pensioners—granted since January 2023, an additional provisioning percentage of 10% applies when the loan maturity is greater than 72 months (6 years), and 40% when the maturity is greater than 108 months (9 years).

According to External Circular 026, these measures aim to promote the sound and sustainable growth of the consumer loan portfolio and to recognize the potential impact on borrowers' repayment capacity in the context of economic slowdown and persistent inflation. Following this update, expected losses for consumer loans should be calculated as shown in Equation 2 where the maturity adjustment (MA)—introduced in the 2016 regulatory update—accounts for loan term risk in expected loss calculations. The MA equals 1 for loans with a remaining maturity shorter than 72 months, and $MA = \frac{m}{72}$ otherwise, where $m$ denotes the remaining maturity in months. Additionally, CIs were also required to conduct a forward-looking analysis of potential deterioration in the consumer loan portfolio and, if necessary, establish an additional general provision no later than December 31, 2022.

$$
E x p e c t e d L o s s = P D * E A D * L G D * M A * K\tag{2}
$$

Longer maturities generally imply greater uncertainty and increased exposure to adverse conditions, making this adjustment essential for risk-sensitive provisioning. The $K$ factor captures additional risk associated with higher leverage at longer maturities, enhancing the model's sensitivity to structural vulnerabilities in consumer credit portfolios, particularly under scenarios of prolonged debt accumulation. The $K$ factor is calculated as follows:

$$
K = \left\{ \begin{array}{c c} 1 & i f m \leq 7 2 \\ 1. 1 i f 7 2 <   m \leq 1 0 8 \\ 1. 4 & i f m > 1 0 8 \end{array} \right\}\tag{3}
$$

By design, the introduction of the K factor increases the marginal cost of supplying long-maturity consumer credit, particularly for loans extending beyond six and nine years. This discrete and maturity-specific adjustment to expected loss calculations provides a natural setting to assess how higher regulatory provisioning requirements influence loan supply decisions and the allocation of credit across maturities in the consumer loan market.

## 2.2. Related literature

Since the global financial crisis of 2008, regulatory authorities in an increasing number of jurisdictions have required CIs to adopt an expected credit loss (ECL) provisioning framework. Under this approach, institutions must accumulate provisions from the time a loan is disbursed, rather than waiting for credit risk to materialize, as was the case under the incurred loss approach. This shift responds to concerns that delayed recognition of credit losses can exacerbate systemic vulnerabilities (Cohen and Edwards, 2017). Moreover, the ECL fr

[中间内容因长度限制已省略]

td><td>407818 (28.5)</td><td rowspan="15"></td><td>47501 (8.0)</td><td rowspan="31">1.387*</td></tr><tr><td>1_12</td><td>5615 (0.1)</td><td>5058 (0.4)</td><td>24518 (4.1)</td></tr><tr><td>1_13</td><td>347281 (5.7)</td><td>71675 (5.0)</td><td>118266 (19.9)</td></tr><tr><td>1_2</td><td>64493 (1.1)</td><td>26416 (1.8)</td><td>61015 (10.3)</td></tr><tr><td>1_23</td><td>152212 (2.5)</td><td>129165 (9.0)</td><td>28678 (4.8)</td></tr><tr><td>1_30</td><td>367205 (6.0)</td><td>34773 (2.4)</td><td>29043 (4.9)</td></tr><tr><td>1_39</td><td>1069268 (17.5)</td><td>73824 (5.2)</td><td>124238 (20.9)</td></tr><tr><td>1_42</td><td>63707 (1.0)</td><td>126948 (8.9)</td><td>11381 (1.9)</td></tr><tr><td>1_43</td><td>31292 (0.5)</td><td>19403 (1.4)</td><td>2094 (0.4)</td></tr><tr><td>1_49</td><td>81664 (1.3)</td><td>24266 (1.7)</td><td>50124 (8.4)</td></tr><tr><td>1_51</td><td>56351 (0.9)</td><td>3666 (0.3)</td><td>16556 (2.8)</td></tr><tr><td>1_54</td><td>22213 (0.4)</td><td>31106 (2.2)</td><td>1236 (0.2)</td></tr><tr><td>1_55</td><td>72635 (1.2)</td><td>26346 (1.8)</td><td>6605 (1.1)</td></tr><tr><td>1_56</td><td>316103 (5.2)</td><td>6291 (0.4)</td><td>1 (0.0)</td></tr><tr><td>1_57</td><td>14191 (0.2)</td><td>6075 (0.4)</td><td>22026 (3.7)</td></tr><tr><td>1_59</td><td>16830 (0.3)</td><td>21953 (1.5)</td><td rowspan="16">0.992*</td><td>338 (0.1)</td></tr><tr><td>1_6</td><td>38507 (0.6)</td><td>10195 (0.7)</td><td>7229 (1.2)</td></tr><tr><td>1_60</td><td>208696 (3.4)</td><td>0 (0.0)</td><td>0 (0.0)</td></tr><tr><td>1_62</td><td>126 (0.0)</td><td>0 (0.0)</td><td>0 (0.0)</td></tr><tr><td>1_63</td><td>37531 (0.6)</td><td>2028 (0.1)</td><td>12 (0.0)</td></tr><tr><td>1_65</td><td>92366 (1.5)</td><td>1 (0.0)</td><td>0 (0.0)</td></tr><tr><td>1_7</td><td>1476298 (24.2)</td><td>346178 (24.2)</td><td>29836 (5.0)</td></tr><tr><td>32_1</td><td>18477 (0.3)</td><td>247 (0.0)</td><td>0 (0.0)</td></tr><tr><td>32_2</td><td>104014 (1.7)</td><td>20670 (1.4)</td><td>0 (0.0)</td></tr><tr><td>32_4</td><td>5936 (0.1)</td><td>562 (0.0)</td><td>0 (0.0)</td></tr><tr><td>32_5</td><td>62058 (1.0)</td><td>1722 (0.1)</td><td>89 (0.0)</td></tr><tr><td>4_121</td><td>18708 (0.3)</td><td>2993 (0.2)</td><td>10071 (1.7)</td></tr><tr><td>4_122</td><td>30045 (0.5)</td><td>26300 (1.8)</td><td>0 (0.0)</td></tr><tr><td>4_26</td><td>137325 (2.3)</td><td>1 (0.0)</td><td>0 (0.0)</td></tr><tr><td>4_31</td><td>18503 (0.3)</td><td>6712 (0.5)</td><td>0 (0.0)</td></tr><tr><td>4_46</td><td>106650 (1.7)</td><td>177 (0.0)</td><td>2531 (0.4)</td></tr><tr><td colspan="3">Observations</td><td>6094433</td><td>1432569</td><td></td><td>593388</td><td></td></tr></table>

Source: Financial Superintendence of Colombia (SFC). Authors' calculations. Note: For categorical variables, values represent the number of observations (percentage of the subsample in parentheses). For continuous variables, values represent the mean (standard deviation in parentheses). An asterisk (\*) denotes a Standardized Mean Difference (SMD) > 0.1, indicating a substantial imbalance.

Table F.1. Effects on Interest Rates

<table><tr><td></td><td colspan="3">72 - Threshold</td><td colspan="3">108 - Threshold</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td colspan="7">Panel A. Difference-in-Differences Estimates</td></tr><tr><td>μ</td><td>0.89769(0.77035)</td><td>0.8949**(0.36424)</td><td>0.88975**(0.39246)</td><td>-2.09606(1.24943)</td><td>-1.44776(1.54285)</td><td>-1.46901(1.58289)</td></tr><tr><td>β</td><td>-0.17389(0.29796)</td><td>0.12936(0.27414)</td><td>0.12828(0.26723)</td><td>1.34583(0.9601)</td><td>1.07844(0.97408)</td><td>1.08756(0.99765)</td></tr><tr><td>Time Fixed Effects</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>FI Fixed Effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FI Characteristics</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="7">Panel B. Matching Procedure</td></tr><tr><td>EM1</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>EM2</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td></tr><tr><td>EM3</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>Observations</td><td>6,687,016</td><td>5,344,050</td><td>5,049,605</td><td>3,801,224</td><td>2,288,194</td><td>2,040,704</td></tr></table>

Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

Chart G.1. Results on Interest Rate  
![](images/30a446a9c25b13031cf6bce96405a8ccfebd334e130d95ea3d775d4fd1889d2f.jpg)

![](images/5ecb1b51cc5bd85a731c04870a77497de0497671bb4f51c8dd6b5a4ecc833095.jpg)

Chart G.2. Results on Loan Amount (log)  
![](images/d284d08d5843ccbe2ac6a1573f0149a4fc3b56d570b6ac9acead210d2b3faae8.jpg)

![](images/e6bd2a53826b7d209ff1fea5397e91b23096b52e72d58ba658cf5ac47c67a618.jpg)

Chart G.3. Results on the Loan-to-Value (LTV) ratio  
![](images/9f9e7f0cbfdc793bfae72c9f65587fa2a45504140551639f65775e4de6856036.jpg)

![](images/6b7668c484da00c9f79283d4a4b5d3ee7ac134b4217fd446ffb57a7d42c5a62f.jpg)  
Source: Financial Superintendence of Colombia (SFC). Authors' calculations. Notes: the figure plots the coefficients estimated from Equation (4) along with their 95% confidence intervals, computed using standard errors clustered at the entity level. The vertical red line denotes the reference period of the analysis.
"""
