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
# The Case for Borrower-Based Macroprudential Measures in Spain

Nina Biljanovska, Laura Valderrama

SIP/2026/055

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on May 4, 2026. This paper is also published separately as IMF Country Report No 26/103.

# IMF Selected Issues Paper European Department

# The Case for Borrower-Based Macroprudential Measures in Spain\* Prepared by Nina Biljanovska and Laura Valderrama

Authorized for distribution by Romain Duval

June 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on May 4, 2026. This paper is also published separately as IMF Country Report No 26/103.

ABSTRACT: House prices in Spain have risen rapidly since the pandemic, and the share of riskier mortgages at issuance has increased, suggesting a potential buildup of mortgage-related vulnerabilities. This paper provides analytical inputs to inform the potential design and calibration of borrower-based measures (BBMs), currently not activated in Spain. It first reviews international experience with BBMs, then uses Spanish loan-level data and scenario-based stress tests to assess alternative calibrations. The results suggest that loan-to-value caps would deliver the largest reduction in default risk and mortgage portfolio losses, with additional gains from income-based caps. BBMs would complement capital buffers by addressing risks at origination.

RECOMMENDED CITATION: Biljanovska, Nina and Laura Velderrama. "The Case for Borrower-Based Macroprudential Measures in Spain." IMF Selected Issues Paper (SIP/2026/055), European Department. Washington, DC: International Monetary Fund.

<table><tr><td>JEL Classification Numbers:</td><td>G21, G28, E58, E44</td></tr><tr><td>Keywords:</td><td>Mortgage lending, borrower-based measures, mortgage default risk, housing markets, Spain</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>nbiljanovska@imf.org, LValderramaFerrando@imf.org</td></tr></table>

SELECTED ISSUES PAPERS

# The Case for Borrower-Based Macroprudential Measures in Spain

Spain

Prepared by Nina Biljanovska, Laura Valderrama $^{1}$

# THE CASE FOR BORROWER-BASED MACROPRUDENTIAL MEASURES IN SPAIN $^{1}$

House prices in Spain have grown rapidly since the COVID-19 pandemic, and while household leverage remains low by euro area standards, the share of risky mortgage loans at issuance has risen. Against this backdrop, this paper provides analytical inputs to inform the potential design and calibration of borrower-based measures (BBMs)—currently not activated as part of the Bank of Spain's toolkit—should such measures be considered. It combines a review of international experience with two complementary empirical analyses using Spanish data: a loan-level analysis assessing how lending standards at issuance affect the subsequent probability of mortgage default, and a scenario-based stress analysis quantifying how alternative BBM calibrations would affect bank mortgage portfolio losses under adverse macroeconomic conditions. Both approaches point in the same direction: a collateral-based measure, such as a loan-to-value (LTV) cap, would be associated with the largest reduction in default probabilities at origination and in portfolio losses under stress, with further gains if complemented by an income-based cap. The evidence also suggests that BBMs and existing capital-based measures—such as the ongoing phasing-in of the counter-cyclical buffer—could act as complementary instruments, addressing risk ex ante at origination and ex post through banks' loss-absorption capacity.

## A. Introduction

1. House prices in Spain have been rising over the past decade, with a sharp increase since the COVID-19 pandemic. After the major correction that followed the global financial crisis (GFC), the housing market stabilized and gradually recovered, but prices have accelerated markedly since 2020—including amid the unprecedented ECB monetary policy tightening episode (Figure 1). The post-pandemic rebound has been broad-based, with especially large price gains in large urban areas and touristic regions where supply is more rigid. While the current buoyancy does not pose immediate macro-financial risks, affordability pressures are mounting (2025 Spain Article IV Consultation), and financial vulnerabilities could build over time.

2. Notwithstanding subdued growth in household mortgage credit, the share of risky loans at issuance has been steadily increasing over the past few years. Households have continued to deleverage, extending a decade-long trend, and the stock of mortgage credit has only recently begun to rise modestly. Spain's overall household debt-to-income ratio is now well below the euro area average, reflecting healthy household balance sheets on the back of a strong labor market and prudent lending standards. Yet these aggregate indicators can mask shifts in the composition of new lending: the share of loans with loan-to-value ratios above 80 percent has risen steadily since 2023 (Figure 1), suggesting some deterioration in the risk profile of recent originations even as average leverage remained contained.

Figure 1. House Price Growth and New Mortgage Issuance  
![](images/33269b1cbaaa6b19160b8032f28dfa84174a759cefcdf7f86fa41ec9de940149.jpg)

![](images/ec33ca865d8999eca3f8d1150a67675d9e2def38b7d22a339738b60cf2282bc2.jpg)

3. Despite relatively low household leverage, persistently strong house price growth and emerging signs of easing in lending standards raise the question of whether pre-emptive borrower-based measures (BBMs) are warranted, and if so, how they should be calibrated. Sustained increases in valuations may, over time, create pressure to ease bank lending standards or encourage riskier lending behavior, as historical evidence suggests (Martín and others, 2021; Duca and others, 2011; Justiniano and others, 2019). Over and above the role of micro-prudential supervision, one option to pre-empt such accumulation of vulnerabilities would be to introduce BBMs, an increasingly popular macro-prudential tool. Implementing such measures before they become strongly binding could also minimize their economic, social, and political costs, as they are unlikely to constrain credit materially and would face less public resistance if introduced early on. To date, BBMs have not been activated as part of the Bank of Spain's macroprudential toolkit, while they are in place in most other euro area countries.

4. This Selected Issues paper provides analytical inputs to inform the potential design and calibration of BBMs should such measures be considered. It draws on three complementary building blocks. First, it reviews international experience with BBMs—their objectives, benefits and costs, design features, and calibration practices across euro area peers. Second, it uses loan-level data to assess how loan-to-value (LTV), loan-to-income (LTI), and loan-service-to-income (LSTI) ratios at origination affect the probability of mortgage default in Spain, and how these effects interact with lenders' capitalization. Third, it employs a scenario-based stress analysis of the Spanish mortgage portfolio to quantify how alternative BBM calibrations could lower bank losses under an adverse macroeconomic scenario.

## B. Overview of BBMs and Complementary Macroprudential Measures

5. BBMs are regulatory limits on loan underwriting criteria. They are most often applied to residential real estate lending, directly constraining borrowers' capacity to borrow, containing the build-up of vulnerabilities, and thereby supporting the resilience of banks and the broader financial system (ECB 2025). BBMs that have been most widely used across countries, and which empirical evidence suggests have been the most effective at containing housing-related systemic risks, include:

\- LTV ratios, which cap the loan amount at a fixed share of the property's value at origination, requiring borrowers to fund the remainder through a downpayment. The borrower's equity then acts as a first-loss buffer in the event of a house price correction, lowering banks' loss given default.

\- LSTI or LTI ratios restrict borrowers' total debt service or debt stock relative to gross income. These lower the probability of default by strengthening households' ability to withstand interest rate or income shocks.

6. While not BBMs, loan maturity caps and amortization requirements are frequently applied alongside them to strengthen their effectiveness (Valderrama 2023). By limiting loan terms and ensuring steady debt repayment, they prevent circumvention of debt-service limits and promote faster equity build-up. More specifically:

\- Loan maturity limits cap the tenor of loans (e.g., 30 years for mortgages). They prevent risk build-up from excessively long loans, which lower initial payments but raise total debt and could also otherwise be used to circumvent LSTI limits (2025 France FSSA). Shorter maturities accelerate amortization and reduce default risk, all else equal.

\- Amortization requirements and interest-only restrictions impose a repayment structure. Regulators may limit interest-only mortgages or request that high-LTV loans amortize more quickly. Such measures set amortization schedules to reduce default risks.

<table><tr><td colspan="3">Table 1. Spain: Key Policies to Address Vulnerabilities in the Residential Real Estate Market</td></tr><tr><td></td><td>Policies to Contain Build-Up of Vulnerabilities</td><td>Policies to Strengthen Banks Resilience</td></tr><tr><td>Objective</td><td>Keep borrowing at sustainable levels</td><td>Build bank buffers to absorb losses</td></tr><tr><td>Tools</td><td>Borrower-based limits:- LTV, LSTI, LTIAmortization requirements:- Amortization rate, max loan maturity</td><td>Capital-based requirements:- Broad/sectoral CCyB or sectoral SyRB- Risk-weight measuresRegulatory provisions</td></tr><tr><td>Channel</td><td>Direct: Credit demandIndirect: House prices</td><td>Direct: Higher capital in good timesIndirect: Credit supply; house prices</td></tr><tr><td>Impact</td><td>Direct: Decrease the size/number of loansIndirect: Increase resilience of borrowers; save regulatory capital</td><td>Direct: Increase capital requirement in good timesIndirect: Decrease build-up of vulnerabilities (if pass-through effect); increase regulatory capital</td></tr><tr><td colspan="3">Sources: Valderrama (2023).</td></tr></table>

7. Another important complementarity to be considered is with prevailing capital-based measures. In Spain, two key measures are currently in place: the countercyclical capital buffer (CCyB), which has been set at 1 percent, effective October 2026, and the capital buffers for systemically important institutions (G-SII and O-SII), with rates ranging from 0.25 to 1.25 percent (2025 Bank of Spain). Other macroprudential tools in the capital-based toolkit—such as the Systemic Risk Buffer (SyRB) and the Sectoral CCyB—are part of the framework but not currently activated (2025 ESRB). By limiting leverage and ensuring debt serviceability at issuance, BBMs can strengthen households' balance sheets and improve banks' asset quality ex ante, complementing capital-based measures that act on the outstanding stock of exposures and improve resilience ex post.

## 8. Nearly all Euro-area

countries have adopted BBMs in some form over the last decade (Figure 2). As of 2025, 18 out of 21 banking union countries have at least one active measure (ECB 2025), and use of combined collateral-, income- and maturity-based limits has risen markedly (Table 2). This broad adoption reflects the growing consensus on the effectiveness of BBMs in safeguarding financial stability, even though less is known about their overall welfare effects. Evidence from both advanced and

Figure 2. Activation of BBMs in Euro Area Countries, 2015–25  
![](images/ef4d26718ca41f6cbd9448754a074f643c37f2fb7f33948ea7fe7e03b9103a24.jpg)

emerging economies shows that these tools have helped curb the build-up of risky mortgage lending by limiting high-LTV and high-LSTI loans, thereby strengthening household and bank resilience (e.g., Ahuja and Nabar, 2011; Kuttner and Shim, 2016; Valderrama, 2023). Recent monetary tightening episodes also suggest that countries with established borrower-based frameworks experience milder housing corrections and smaller increases in default rates (2024 IMF WEO).

9. BBMs are primarily designed for residential real estate lending, though some countries extend them to other types of credit. A few EU countries—including Romania and Slovakia—apply BBMs to consumer credit as well. Commercial real estate lending, by contrast, generally falls outside the borrower-based framework and is addressed through capital-based tools instead. The analysis in this paper focuses on BBMs for residential mortgage lending.

## C. Design and Calibration Considerations

10. Designing BBMs requires balancing their financial-stability benefits against potential costs in terms of reduced credit access for affected households and economic activity. Well-calibrated BBMs strengthen household and bank resilience by limiting excessive leverage and debt burdens, but if introduced too late or set too tightly, they can restrict credit unnecessarily and contribute to or amplify an economic downturn. Insofar as they are more binding for lower-income households, they may also entail unwanted distributive consequences in terms of access to home ownership. Effective design therefore hinges on when and how these tools are deployed, how tightly they are calibrated, what exemptions if any might be introduced, and how flexibly they adapt to evolving market conditions. The following principles—on timing, calibration, complementarity, flexibility, implementation, and coordination—capture key lessons from international experience on how to strike this balance.

11. First, timing matters: BBMs are most effective when introduced early in the financial cycle, before systemic risks accumulate. Deployed at this stage, BBMs act as a structural safeguard: imposing prudent lending standards ex ante while avoiding immediately binding constraints on credit. This logic is consistent with both theory (Bianchi, 2011) and empirical evidence (Valderrama, 2023; Biljanovska and others, 2023), which imply that preemptive activation is less distortionary and more effective than waiting until vulnerabilities are already entrenched. Introducing BBMs only after lending standards have already loosened can amplify procyclicality, as late tightening may trigger a correction in credit and housing markets.

12. Second, calibration should be data-driven and grounded in country-specific risk analysis. Common benchmarks have emerged, but with wide variation across countries. LTV limits across countries are typically set between 80 and 100 percent for first-time buyers purchasing a primary residence, and somewhat tighter for repeat buyers (70-90 percent). Income-based limits usually complement these collateral constraints, with LSTI caps ranging from 30 to 80 percent of the borrower's monthly income across countries.

13. While international benchmarks provide useful reference points, effective limits should be tailored to domestic factors. These factors include household indebtedness, income distribution, housing market dynamics, and typical underwriting standards, as well as how these may affect household and bank resilience in the future versus credit today. To this end, authorities should rely on granular, loan-level data to analyze the distributions of borrower leverage and debt-service burdens and identify thresholds where default risk rises sharply. Model-based stress testing and scenario analysis—such as those developed by Gornicka and Valderrama (2020) and applied recently to Austria and Switzerland, for example—can further help quantify how much alternative LTV or LSTI limits would strengthen households' capacity to service their debt and banks' ability to withstand potential losses under various stress scenarios.

14. Third, a multi-pronged approach can be more effective than relying on a single instrument. In particular, LTV and LSTI caps address different dimensions of risk—loss given default and likelihood of default, respectively—and are thereby mutually reinforcing. Complementary constraints, such as maturity caps or amortization requirements, can help prevent circumvention (e.g., stretching maturities to pass a LSTI test) and further reduce borrower vulnerabilities (ESRB, 2016).

Table 2. Spain: BBMs, Maturity Caps, and Capital-Based Measures across EU Banking Union Countries

<table><tr><td rowspan="2"></td><td colspan="2">LTV</td><td colspan="2">LTV exemption</td><td colspan="2">DSTI/LSTI</td><td colspan="2">DSTI/LSTI exemption</td><td colspan="2">DTI/LTI</td><td colspan="2">DTI/LTI exemption</td><td colspan="2">Maturity</td><td colspan="2">Maturity exemption</td><td>CCyB</td></tr><tr><td>FTB</td><td>SSB</td><td>FTB</td><td>SSB</td><td>FTB</td><td>SSB</td><td>FTB</td><td>SSB</td><td>FTB</td><td>SSB</td><td>FTB</td><td>SSB</td><td>FTB</td><td>SSB</td><td>FTB</td><td>SSB</td><td></td></tr><tr><td>Austria</td><td>90</td><td></td><td>20%</td><td></td><td>40</td><td></td><td>20%</td><td></td><td></td><td></td><td></td><td></td><td>35y</td><td></td><td>20%</td><td></td><td>0</td></tr><tr><td>Belgium</td><td>90</td><td></td><td>35%</td><td>20%</td><td>50</td><td></td><td>5%</td><td></td><td>9y</td><td></td><td>5%</td><td></td><td></td><td></td><td></td><td></td><td>1%</td></tr><tr><td>Bulgaria</td><td>85</td><td></td><td>5%</td><td></td><td>50</td><td></td><td>5%</td><td></td><td></td><td></td><td></td><td></td><td>30y</td><td></td><td>5%</td><td></td><td>2%</td></tr><tr><td>Cyprus</td><td>80</td><td></td><td></td><td></td><td>80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1% (1.5% from Jan 2026)</td></tr><tr><td>Germany</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.75%</td></tr><tr><td>Estonia</td><td>85</td><td></td><td>15%</td><td></td><td>50</td><td></td><td>15%</td><td>15%</td><td></td><td></td><td></td><td></td><td>30y</td><td></td><td>15%</td><td></td><td>1.5%</td></tr><tr><td>Spain</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td

[中间内容因长度限制已省略]

><td>0.0435</td><td>0.0454</td><td>0.0441</td><td>0.0454</td><td>0.0441</td></tr><tr><td>Time-Bank FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time-Province FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Annex I. Table 2. Spain: Effects of High-Risk Loans on Mortgage Defaults Contingent on Lenders' Capital Ratio

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>LTV&gt;80%</td><td>0.0106***(0.0018)</td><td></td><td></td></tr><tr><td>LTI&gt;6</td><td></td><td>0.0023*(0.0013)</td><td></td></tr><tr><td>LSTI&gt;40%</td><td></td><td></td><td>0.0042***(0.0014)</td></tr><tr><td>LTV&gt;80% # RWA Capital Ratio</td><td>-0.0039***(0.0012)</td><td></td><td></td></tr><tr><td>LTI&gt;6 # RWA Capital Ratio</td><td></td><td>-0.0018**(0.0007)</td><td></td></tr><tr><td>LSTI&gt;40% # RWA Capital Ratio</td><td></td><td></td><td>0.0004(0.0011)</td></tr><tr><td>LTV&gt;80% # LTI&gt;6</td><td></td><td></td><td></td></tr><tr><td>LTV&gt;80% # LSTI&gt;40%</td><td></td><td></td><td></td></tr><tr><td>Observations</td><td>463933</td><td>470862</td><td>462178</td></tr><tr><td>R-squared</td><td>0.0451</td><td>0.0445</td><td>0.0433</td></tr><tr><td>Time-Bank FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time-Province FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: The dependent variable is mortgage delinquency. Lending standards are included as indicator variables equal to one when the loan exceeds the following thresholds: LTV > 80%, LTI > 6 and LSTI>40. The risk weighted assets (RWA) capital ratio is winsorized at the 1st and 99th percentiles and standardized. Regressions include bank-by-time and province-by-time fixed effects. Robust standard errors are reported in parentheses. \*\*\*, \*\*, \* denotes coefficients statistically different from 0 at 1%, 5% and 10% levels, respectively.

## Annex II. Scenario-Based Default Model Calibration

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Calibrate sensitivity of FD to shifts in DSTI</td><td> $\beta_1 = 0.0016$   $\gamma = 2.5$ </td></tr><tr><td>Calibrate sensitivity of FD to initial DSTI by bucket</td><td> $\phi(DSTI) = \begin{cases} \left( \frac{DSTI - 15\%}{30\% - 15\%} \right) & 15\% < DSTI < 30\% \\ 1 & \text{otherwise} \end{cases}$ </td></tr><tr><td>Calibrate sensitivity of FD to unemployment</td><td> $\beta_2 = 0.06$   $\beta_3 = 0.727$   $\alpha = 1$ </td></tr><tr><td>Allocate financial distress to shocks during the Spanish real estate crisis 2013-14</td><td> $\xi_{FD,u} = \frac{\partial FD}{\partial u} = 17.6\%$   $\xi_{FD,i} = \frac{\partial FD}{\partial i} = 14.8\%$ </td></tr><tr><td>Estimate sensitivity to demographic factors</td><td> $D = 0.02$ </td></tr><tr><td>Estimate foreclosure transaction costs</td><td> $C = 3.65\%$ </td></tr><tr><td>Estimate liquid financial assets as a share of average residential real estate price</td><td> $1.15\% \cdot \tilde{P}$ </td></tr></table>

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Foreclosure discount</td><td>27.26%</td></tr><tr><td>Time to sell collateral after foreclosure</td><td>6.17 year</td></tr><tr><td>Discount rate of real estate collateral</td><td>2.7%</td></tr><tr><td>Spread on discount rate on foreclosed collateral</td><td>1.0%</td></tr></table>

## Annex III. Macrofinancial Variables Path Assumptions

Annex III. Table 1 reports the time paths of the key macrofinancial variables used in the scenario-based analysis—unemployment, interest rates (weighted average of fixed/floating mortgages across all maturities whose counterparty is a household), income growth (year-on-year), and house prices (nominal year-on-year growth)—under both the baseline and the adverse scenario. The baseline paths are drawn from the January 2026 WEO (except the house price projections), while the house price projections and the adverse paths follow the European Banking Authority's (EBA) 2025 EU-wide stress test exercise. The shocks embedded in the 2025 EU-wide stress scenario are applied to the January 2026 WEO baseline forecasts to project the adverse paths in levels. These trajectories feed into the model simulations underlying the mortgage portfolio loss estimates—with and without BBMs—reported in Section E.

<table><tr><td colspan="7">Annex III. Table 1. Spain: Baseline and Adverse Scenario</td></tr><tr><td>Baseline</td><td>2025</td><td>2026</td><td>2027</td><td>2028</td><td>2029</td><td>2030</td></tr><tr><td>January 2026 WEO</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Unemployment</td><td>10.8</td><td>10.7</td><td>10.7</td><td>10.7</td><td>10.7</td><td>10.7</td></tr><tr><td>Interest rates</td><td>2.6</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.5</td></tr><tr><td>Income growth</td><td>6.0</td><td>5.1</td><td>4.2</td><td>4.4</td><td>4.0</td><td>4.0</td></tr><tr><td>EBA 2025 stress test</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>House prices</td><td>8.5</td><td>7.6</td><td>6.7</td><td>4.9</td><td>4.9</td><td>4.9</td></tr><tr><td>Adverse</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBA 2025 stress test</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Unemployment</td><td>10.8</td><td>10.7</td><td>10.7</td><td>14.0</td><td>17.2</td><td>16.4</td></tr><tr><td>Interest rates</td><td>2.6</td><td>2.5</td><td>2.5</td><td>5.1</td><td>4.5</td><td>4.1</td></tr><tr><td>Income growth</td><td>6.0</td><td>5.1</td><td>4.2</td><td>4.4</td><td>4.0</td><td>4.0</td></tr><tr><td>House prices</td><td>8.5</td><td>7.6</td><td>6.7</td><td>-4.3</td><td>-11.0</td><td>-5.6</td></tr></table>
"""
