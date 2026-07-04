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
# Should Oil Economies Worry About Oil Shocks' Impact on the Banking System? The Case of Oman

Prepared by Yurii Sholomytskyi, Nathaniel Butler Blondel, and Mumtaz Hussain

WP/26/142

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/7718d4be33b4a21b753321bb357b0acd85c6e1ea22c643e7d8009f16aee7edf9.jpg)

# IMF Working Paper Institute for Capacity Development

Should Oil Economies Worry About Oil Shocks' Impact on the Banking System? The Case of Oman

Prepared by Yurii Sholomytskyi, Nathaniel Butler Blondel, $^{1}$ and Mumtaz Hussain

Authorized for distribution by Ali Alichi

July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper investigates the transmission of oil price shocks to the banking sector in oil-dependent economies, using Oman as a case study. We develop a DSGE model featuring an integrated banking block with endogenous credit rationing and a sovereign wealth fund stabilization rule, calibrated to Omani institutional targets and disciplined by Bayesian methods. Our structural approach disentangles two primary transmission channels: the solvency channel, driven by credit risk and non-performing loans (NPLs), and the liquidity channel, driven by pro-cyclical government deposit withdrawals and sovereign debt issuance. The structural variance decomposition attributes over 54% of non-oil GDP variance and 53% of credit variance to oil price shocks, while bank capital shocks account for less than 0.1%, confirming the quantitative dominance of the liquidity channel. We identify a precautionary liquidity motive—a “liquidity buffer trap”—where banks maintain excess liquidity during booms to hedge against hydrocarbon volatility, structurally suppressing credit to the productive sector. Our counterfactual regime analysis reveals the stabilizing power of credit depth: banking conservatism protects long-term physical capital formation, and the ongoing financialization of the corporate sector—including the rapid growth of Islamic banking and sukuk markets—under Vision 2040 further amplifies this structural resilience. We acknowledge identification challenges inherent in small-sample structural estimation and discuss the sensitivity of results to key modeling assumptions.

RECOMMENDED CITATION: Should Oil Economies Worry About Oil Shocks' Impact on the Banking System? The Case of Oman.

<table><tr><td>JEL Classification Numbers:</td><td>E44, E52, G21, Q43</td></tr><tr><td>Keywords:</td><td>Oil price shocks; DSGE; Credit rationing; Banking liquidity; Sovereign Wealth Fund; Fiscal-financial nexus; Islamic banking; Oman</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>ysholomytskyi@imf.org, nathaniel.butlerblondel@sciencespo.fr, mhussain@imf.org</td></tr></table>

WORKING PAPERS

# Should Oil Economies Worry About Oil Shocks' Impact on the Banking System? The Case of Oman

Prepared by Yurii Sholomytskyi, Nathaniel Butler Blondel, and Mumtaz Hussain

## Contents

I. Introduction 3
II. Literature review 4
III. The Omani financial sector: stylized facts and macro-financial theory 5
A. Monetary anchor and structural rigidities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
B. Solvency buffers and asymmetric asset quality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
C. The sovereign-bank nexus and the dual liquidity squeeze. 6
D. Asset allocation and the SME paradox. 6
E. The precautionary liquidity buffer and pro-cyclicality. 7
F. Islamic banking, sukuk markets, and the evolving financial landscape. 8
G. Pecuniary externalities and the construction nexus. 8
IV. Households 9
A. Patient households (savers and asset owners) 9
B. Impatient households (constrained borrowers) 10
C. The collateral constraint: statutory vs. market limits. 10
D. Aggregation and distributional dynamics. 10
V. The production sector 11
A. Intermediate goods producers and technology. 11
B. The hydrocarbon sector. 11
C. Real marginal cost and the financial-wage friction. 12
D. Staggered price setting and the hybrid Phillips curve. 12
VI. The capital goods sector and investment dynamics 13
A. Capital accumulation and adjustment costs. 13
B. Tobin's Q and investment pricing. 13
VII. The labor market and the "vent" channel 14
A. Domestic labor supply and employment adjustment. 14
B. Migrant labor and foreign supply. 14
C. The remittance channel and import sluggishness. 15
VIII. Housing and the collateral accelerator 15
A. House price determination. 15
B. Housing stock and investment. 16
IX. The sovereign wealth fund (Oman Investment Authority) 16
A. Wealth accumulation and returns. 16
B. The dual-mandate transfer rule. 17
X. The government and fiscal policy 17
A. Revenue generation: the two pillars of Omani income. 18
B. The stabilized budget constraint and deficit management. 18
C. The net liquidity proxy: formalizing the "squeeze". 18
D. Fiscal pro-cyclicality and the expenditure rule. 19

XI. The banking system: solvency, liquidity, and endogenous risk-taking 19
A. The wholesale bank's optimization problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
B. Retail units and the rollover risk channel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
C. Optimal credit rationing: the behavioral filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
D. Credit flows, legacy loans, and portfolio stickiness. 22
XII. Monetary policy 23
A. The fixed exchange rate regime 23
B. Interest rate parity and risk premiums 23
XIII. External balance and national debt 23
XIV. Empirical strategy: calibration with Bayesian discipline 24
A. Data sources and sample 24
B. Identification limitations and the supply-demand distinction 25
C. Steady-state moments and model fit 26
D. Structural parameterization 26
D..1 Calibrated parameters and stationarity bounds 26
D..2 Bayesian-disciplined parameters (cyclical dynamics) 27
XV. Empirical results 29
A. Structural variance decomposition 29
B. Regime analysis: the sustainability gap 30
C. Sensitivity analysis 34
XVI. Conclusions 35
XVII. Technical Annex: Full Log-Linearized Model Specification 37

## I. Introduction

The intricate relationship between oil price fluctuations and the banking sector is a subject of great importance for oil-dependent economies such as Oman. As one of the world's leading oil exporters, Oman derives a significant portion of its revenue from oil, with petroleum accounting for about $70\%$ of government revenue and $80\%$ of export earnings. As global markets remain susceptible to geopolitical tensions and demand variability, oil shocks can have profound implications for financial stability. This paper seeks to address the critical question: should oil economies like Oman be concerned about the impact of oil shocks on their banking systems, and is the primary risk one of solvency or liquidity?

Oil shocks, characterized by sudden and significant changes in prices, affect financial stability through two distinct channels. First, the solvency channel: an economic contraction leads to increased default rates and a deterioration of asset quality (non-performing loans), eroding bank capital. Second, and often overlooked in the literature, is the liquidity channel: in state-dominated economies like Oman, the banking system relies heavily on government deposits. A collapse in oil revenues triggers a dual “liquidity squeeze”: the government simultaneously draws down these deposits and actively issues domestic sovereign debt to fund fiscal deficits. For domestic banks, both actions mechanically drain available loanable funds, creating an immediate funding squeeze that crowds out private credit independent of the underlying credit risk.

Understanding these mechanisms is crucial for policymakers. While the interconnectedness of global markets means Omani banks are exposed to international sentiment, domestic structural features—specifically the fiscal-financial nexus—may amplify these shocks.

This paper differentiates itself from the existing literature by analyzing these dynamics through a New Keynesian DSGE model tailored to a small open economy with a fixed exchange rate. Unlike reduced-form empirical models (such as VARs or ECMs) which estimate historical correlations, our structural approach allows us to:

1. Explicitly model the sovereign wealth fund (SWF) and its stabilization rule, isolating how fiscal buffering (or lack thereof) transmits shocks to the banking sector.

2. Disentangle the deposit channel (funding costs) from the financial accelerator channel (collateral constraints).

3. Explore the role of regulatory constraints—including Loan-to-Value (LTV) and Payment-to-Income (PTI) limits—in a regime where monetary policy is constrained by the US dollar peg.

We find that while Omani banks possess strong solvency buffers, they exhibit significant vulnerability to liquidity pressures driven by pro-cyclical government deposit flows. This finding highlights the importance of liquidity management and fiscal-financial coordination alongside traditional capital adequacy monitoring. We discuss the identification challenges inherent in this approach— particularly the difficulty of separating supply-side credit rationing from demand-side effects—in Section X.

## II. Literature review

The academic inquiry into the nexus between oil prices and financial stability has evolved from aggregate macroeconomic analysis to detailed banking sector studies.

## Macroeconomic impact of oil shocks

Seminal work by Hamilton [1983] established the foundational understanding of how oil price shocks precipitate economic downturns through supply-side constraints and demand destruction. Subsequent research by Kilian [2009] refined this by decomposing shocks into supply, demand, and precautionary motives using structural VAR models, highlighting that the origin of the shock determines its macroeconomic transmission.

## Banking channel

A substantial body of literature highlights the banking sector as a specific transmission vector. Bernanke et al. [1997] emphasized the role of monetary policy responses in mediating oil shocks, suggesting that the resulting interest rate adjustments often amplify the contraction. Gelain and Lorusso [2022] extended this to a DSGE framework for the US, finding that oil price fluctuations account for up to 17% of GDP variation, primarily transmitted through the “financial accelerator” effect where falling asset prices constrain borrowing capacity.

However, the transmission mechanism in oil-exporting developing economies differs significantly from the US context. Khandelwal et al. [2016] utilized a multivariate panel approach for GCC countries, demonstrating a strong feedback loop between oil prices, bank balance sheets, and asset prices. This is corroborated by Alkhater [2014] and Fattouh and El-Katiri [2012], who emphasize that in Bahrain and the UAE, the banking sector's health is intrinsically tied to government oil revenues rather than just private sector productivity.

## Systemic risk and liquidity

Recent empirical work has attempted to distinguish between risk types. Maghyereh and Abdoh [2021] find that supply-side oil shocks significantly increase systemic risk in GCC banking systems. Monnin and Jokipii [2014] argue that banking sector stability is a prerequisite for real output growth, finding that instability leads to significant underestimations of future GDP contractions.

## Gap in the literature

While existing studies [e.g., Qin, 2020, Ma et al., 2021] utilize VAR methodologies to estimate risk correlations, there is a scarcity of structural models that explicitly capture the sovereign wealth fund mechanics and the government deposit channel prevalent in the Gulf region. Most DSGE models for the region focus on fiscal sustainability without a detailed banking sector. Our paper fills this gap by integrating a banking block with endogenous credit rationing [following Gerali et al., 2010] into a resource-rich small open economy framework. This allows us to quantify the trade-off between fiscal stabilization (drawing down deposits and issuing domestic debt) and financial stability (maintaining bank liquidity).

## III. The Omani financial sector: stylized facts and macro-financial theory

The financial sector in Oman is characterized by a bank-dominated structure, operating under a fixed exchange rate regime and significant exposure to the global hydrocarbon cycle. With total banking sector assets standing at 102.3% of GDP, the commercial banking system acts as the primary intermediary for national wealth. This section identifies the critical empirical features and theoretical drivers of the Omani macro-financial cycle that motivate the structural frictions in our DSGE framework.

## A. Monetary anchor and structural rigidities

The Central Bank of Oman (CBO) maintains a fixed exchange rate peg of the Omani rial to the US dollar, which serves as the economy's primary nominal anchor. Under this regime, domestic policy rates generally track the federal funds rate to prevent capital flight. However, the interest rate pass-through in Oman is historically weak, even compared to structurally similar GCC peers. Kroen [2024] find that what little pass-through exists is driven almost entirely by foreign currency lending, leaving the domestic transmission mechanism largely blunted.

Despite a moderate concentration ratio—where the top three and top five banks account for 60% and 80% of assets, respectively—there is evidence of significant structural rigidity. A persistent spread of approximately 300 basis points between lending and deposit rates has remained resilient even during recent monetary tightening cycles. This stickiness suggests a degree of market power and structural friction in the deposit market, justifying the monopolistic competition framework and the inclusion of adjustment costs in the setting of interest rates within our model.

## B. Solvency buffers and asymmetric asset quality

Omani banks maintain robust solvency buffers and resilience. The sector-wide capital adequacy ratio (CAR) stands at 17.5%, reflecting a steady accumulation of capital since the 2015 oil price shock. While this deleveraging has compressed the return on equity (ROE) to approximately 7.8%, the sector remains profitable with a return on assets (ROA) of nearly 1.5%.

However, asset quality exhibits emerging stress that is highly asymmetric across sectors. The NPL ratio has risen consistently since 2016, reaching $4.5\%$ by end-2023—more than double preshock levels. Crucially for our model's sectoral differentiation, distress is concentrated: loans to the corporate sector (particularly construction and manufacturing) exhibit an NPL rate of $6.5\%$ , whereas household personal loans remain resilient with a default rate of only $2.35\%$ . While high provisioning levels ( $69.3\%$ coverage for Stage 3 loans) have kept the net NPL ratio stable at roughly $1.4\%$ , the rising gross NPLs constrain banks' future risk appetite and trigger the non-price rationing mechanisms identified in our theory.

## C. The sovereign-bank nexus and the dual liquidity squeeze

The liability side of the banking balance sheet reveals a critical systemic vulnerability. Omani banks rely heavily on domestic funding, with less than 3% of liabilities sourced from non-residents. More importantly, the system exhibits a structural dependence on the public sector: over 30% of total deposits are held directly by the government and state-owned enterprises (SOEs).

In our stylized theory, we identify these holdings not as stable savings, but rather as transactional float. These deposits represent oil revenue in transit to finance budgetary expenditures. Crucially, when oil prices fall, the government bridges fiscal gaps through multiple mechanisms: drawing down these deposits, issuing domestic sovereign bonds absorbed by commercial banks, and—particularly during prolonged downturns—accessing external capital markets and sovereign wealth fund buffers. While the SWF and external borrowing channels partially attenuate the domestic liquidity impact, CBO data confirm that government deposit positions within the domestic banking system nonetheless experience material fluctuations that are quantitatively significant relative to the private credit stock.

From the perspective of the commercial banking system's balance sheet, the net effect of government deposit withdrawals and domestic sovereign debt issuance is functionally identical: both drain available loanable funds from the private sector. We formally define this combined net effect as the “liquidity squeeze”. Our model captures this through a consolidated net liquidity proxy ( $D_t^G$ ) that abstracts from the government's external financing choices to focus on the residual domestic banking system impact. This creates a direct liquidity channel where negative oil shocks precipitate crowding-out of private credit, independent of private sector credit risk or bank solvency.

## D. Asset allocation and the SME paradox

Credit allocation in Oman is heavily skewed toward the household sector. Personal loans account for 37.5% of total credit, including 18.5% for mortgages. Construction lending, the second-largest category at 9%, is also largely residential. Consequently, over 50% of private non-financial credit effectively finances household consumption and housing. This justifies our model's distinction between “patient” (savers) and “impatient” (borrowers) households. Furthermore, the CBO imposes caps on personal loans (35% of total book) and mortgages (15%). These limits appear binding, as banks consistently lend near these thresholds despite interest rates remaining well below the 6% statutory ceiling, suggesting that credit supply is constrained by regulation and quantity rationing rather than price.

In sharp contrast, lending to SMEs is structurally suppressed, accounting for only 2.9% of total credit. In comparison, 

[中间内容因长度限制已省略]

, forming

the transmission link to the banking block:

$$
g _ {t} = \rho_ {g e} g _ {t - 1} + \phi_ {g e \_ o i l} (p _ {t} ^ {O} + y _ {t} ^ {O}) + \varepsilon_ {G E, t}\tag{77}
$$

$$
d _ {t} ^ {G} = p _ {t} ^ {O} + y _ {t} ^ {O} + \varepsilon_ {D G, t}\tag{78}
$$

Government revenue $(gr_{t})$ and social transfers $(tr_{t})$ respond dynamically to the aggregate economy:

$$
g r _ {t} = \frac {\tau \overline {{W N}} ^ {D}}{\overline {{G R}}} (w _ {t} + n _ {t} ^ {D}) + \frac {\tau_ {o i l} \overline {{P}} ^ {O} \overline {{Y}} ^ {O}}{\overline {{G R}}} (p _ {t} ^ {O} + y _ {t} ^ {O})\tag{79}
$$

$$
t r _ {t} = \rho_ {t r} t r _ {t - 1} + \phi_ {t r} (p _ {t} ^ {O} + y _ {t} ^ {O})\tag{80}
$$

Sovereign wealth fund $(s_{t})$ accumulation and rule-based stabilization transfers $(t_{t}^{SWF})$ :

$$
s _ {t} = (1 + r ^ {s w f}) s _ {t - 1} - \left(\frac {\overline {{T}} ^ {S W F}}{\overline {{S}}}\right) t _ {t} ^ {S W F}\tag{81}
$$

$$
t _ {t} ^ {S W F} = \phi_ {s w f} \left(\frac {\overline {{S}}}{\overline {{T}} ^ {S W F}}\right) s _ {t - 1} + \left(\frac {\phi_ {d e f}}{\overline {{T}} ^ {S W F}}\right) d e f _ {t}\tag{82}
$$

## Market Clearing and External Balance

The aggregate goods market clears across both domestic and external sectors:

$$
y _ {t} ^ {t o t} = \frac {\overline {{Y}}}{\overline {{Y}} ^ {t o t}} y _ {t} + \frac {\overline {{P}} ^ {O} \overline {{Y}} ^ {O}}{\overline {{Y}} ^ {t o t}} (p _ {t} ^ {O} + y _ {t} ^ {O})\tag{83}
$$

$$
x _ {t} ^ {\text {nonoil}} = \phi_ {x} r e r _ {t} + a _ {t}\tag{84}
$$

$$
m _ {t} = \frac {\overline {{C}} c _ {t} + \overline {{G E}} g e _ {t} + \overline {{I}} ^ {t o t} i _ {t} ^ {t o t}}{\overline {{C}} + \overline {{G E}} + \overline {{I}} ^ {t o t}} - \phi_ {m} r e r _ {t} - \kappa_ {m} (m _ {t} - m _ {t - 1})\tag{85}
$$

$$
c _ {t} = \frac {\overline {{Y}}}{\overline {{C}}} y _ {t} + \frac {\overline {{P}} ^ {O} \overline {{Y}} ^ {O}}{\overline {{C}}} (p _ {t} ^ {O} + y _ {t} ^ {O}) - \frac {\overline {{I}} ^ {t o t}}{\overline {{C}}} i _ {t} ^ {t o t} - \frac {\overline {{G E}}}{\overline {{C}}} g e _ {t} - \frac {\overline {{N X}}}{\overline {{C}}} n x _ {t}\tag{86}
$$

The government deficit $(def_{t})$ acts as a level deviation driving the SWF transfers:

$$
d e f _ {t} = \overline {{G E}} \cdot g e _ {t} + \overline {{T R}} \cdot t r _ {t} - \overline {{G R}} \cdot g r _ {t} - \overline {{T}} ^ {S W F} \cdot t _ {t} ^ {S W F}\tag{87}
$$

Because net foreign assets are exactly zero in the baseline steady state $(\overline{B}=0)$ , $b_{t}$ must strictly be defined as a level deviation. It evolves according to the log-deviations of the trade balance $(nx_{t})$ , remittance outflows $(rm_{t})$ , and capital injections $(t_{t}^{SWF})$ , formally weighted by their respective steady-state volume capacities:

$$
\overline {{N X}} \cdot n x _ {t} = \overline {{P}} ^ {O} \overline {{Y}} ^ {O} (p _ {t} ^ {O} + y _ {t} ^ {O}) + \overline {{X}} ^ {N o n O i l} x _ {t} ^ {n o n o i l} - \overline {{M}} m _ {t}\tag{88}
$$

$$
b _ {t} = \frac {1}{\beta} b _ {t - 1} + \overline {{N X}} \cdot n x _ {t} - \overline {{R M}} \cdot r m _ {t} + \overline {{T}} ^ {S W F} \cdot t _ {t} ^ {S W F}\tag{89}
$$

## References

K. R. Alkhater. The Economic Developments in Qatar and GCC Banking. Gulf Centre for Development Studies, 2014.

P. Beaudry and F. Portier. An exploration into Pigou's theory of cycles. Journal of Monetary Economics, 51(6):1183–1216, 2004.

B. S. Bernanke, M. Gertler, and M. Watson. Systematic monetary policy and the effects of oil price shocks. Brookings Papers on Economic Activity, 1:91–142, 1997.

B. S. Bernanke, M. Gertler, and S. Gilchrist. The financial accelerator in a quantitative business cycle framework. Handbook of Macroeconomics, 1:1341–1393, 1999.

L. J. Christiano, M. Eichenbaum, and C. L. Evans. Nominal rigidities and the dynamic effects of a shock to monetary policy. Journal of Political Economy, 113(1):1–45, 2005.

B. Fattouh and L. El-Katiri. Energy market dynamics and financial stability in the UAE. Technical report, Oxford Institute for Energy Studies, 2012.

P. Gelain and M. Lorusso. Oil price shocks and bank balance sheets. Journal of International Money and Finance, 2022.

A. Gerali, S. Neri, L. Sessa, and F. M. Signoretti. Credit and Banking in a DSGE Model of the Euro Area. Journal of Money, Credit and Banking, 42(s1):107-141, 2010.

J. D. Hamilton. Oil and the macroeconomy since World War II. Journal of Political Economy, 91(2):228–248, 1983.

P. Khandelwal, K. Miyajima, and A. Santos. The Impact of Oil Prices on the Banking Sector in the GCC. IMF Working Paper WP/16/161, 2016.

L. Kilian. Not all oil price shocks are alike: Disentangling demand and supply shocks in the crude oil market. American Economic Review, 99(3):1053–69, 2009.

T. Kroen. Monetary policy transmission in Oman. IMF Selected Issues Papers, 2024(018), 2024.

R. Ma et al. Oil price shocks and the systemically important banks in China. Energy Economics, 2021.

A. Maghyereh and H. Abdoh. The impact of oil supply and demand shocks on systemic risk in GCC banking systems. Journal of International Financial Markets, Institutions and Money, 2021.

P. Monnin and T. Jokipii. The impact of banking sector stability on the real economy. Journal of International Money and Finance, 47:1–16, 2014.

M. Qin. The impact of oil price shocks on financial stress. Journal of Commodity Markets, 2020.

J. J. Rotemberg. Sticky prices in the United States. Journal of Political Economy, 90(6):1187–1211, 1982.

C. A. Sims. Solving linear rational expectations models. Computational Economics, 20(1-2):1–20, 2002.

![](images/517e7dea3686b487fbb834ea838ab2857fc087598a0187a905f732568774fd30.jpg)
"""
