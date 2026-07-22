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
# Strengthening Domestic Revenue Mobilization in The Gambia

Chie Aoyagi, Priscilla Banda, Nour Bouzouita, Frank van Brunschot, and Jean-Marc Bedhat Atsebi

SIP/2026/068

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 22, 2026. This paper is also published separately as IMF Country Report No 26/176.

# IMF Selected Issues Paper African Department

Strengthening Domestic Revenue Mobilization in The Gambia
Prepared by Chie Aoyagi, Priscilla Banda, Nour Bouzouita, Frank van Brunschot, and Jean-Marc Bedhat Atsebi
Authorized for distribution by Eva Jenkner
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 22, 2026. This paper is also published separately as IMF Country Report No 26/176

ABSTRACT: Elevated development financing needs, persistent debt service pressures, and increased uncertainty regarding external grants have heightened the urgency of strengthening domestic revenue mobilization in The Gambia. This paper examines The Gambia's current revenue performance relative to peers, estimates tax potential and tax effort using frontier methods, evaluates the authorities' Domestic Resource Mobilization Strategy (DRMS), incorporates estimates from the IMF's Revenue Assessment and Yield Tool (RAYT) and identifies priority and feasible reforms to sustainably raise domestic revenue.

RECOMMENDED CITATION: Aoyagi, Chie, Priscilla Banda, Nour Bouzouita, Frank van Brunschot, and Jean-Marc Bedhat Atsebi. 2026. “Strengthening Domestic Revenue Mobilization in The Gambia.” IMF Selected Issues Paper SIP/2026/068. Washington, DC: International Monetary Fund.

<table><tr><td>JEL Classification Numbers:</td><td>H20, H26, H27, O23, O55</td></tr><tr><td>Keywords: [Type Here]</td><td>Domestic revenue mobilization; tax policy; tax administration; tax potential; tax effort; revenue forecasting; fiscal sustainability; The Gambia.</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>CAoyagi@imf.org ;nbouzouita@imf.org; PBanda@imf.org; FvanBrunschot@imf.org; JAtsebi@imf.org</td></tr></table>

SELECTED ISSUES PAPERS

# Strengthening Domestic Revenue Mobilization in The Gambia

The Gambia

Prepared by Chie Aoyagi, Priscilla Banda, Nour Bouzouita, Frank van Brunschot, and Jean-Marc Bedhat Atsebi $^{1}$

## THE GAMBIA

## SELECTED ISSUES

June 22, 2026

Approved By

African Department

Prepared by Chie Aoyagi, Priscilla Banda, Nour Bouzouita, Frank van Brunschot, and Jean-Marc Bedhat Atsebi.

## CONTENTS

STRENGTHENING DOMESTIC REVENUE MOBILIZATION IN THE GAMBIA 2
A. Introduction 2
B. Revenue Structure and Recent Trends 3
C. Estimating Tax Potential and Tax Effort 5
D. The Authorities' Domestic Resource Mobilization Strategy 6
E. Policy Priorities and Reform Options to Support the DRMS 8
F. Revenue Assessment and Yield Tool (RAYT) 9
G. Conclusion 13

## ANNEX

# STRENGTHENING DOMESTIC REVENUE MOBILIZATION IN THE GAMBIA $^{1}$

Elevated development financing needs, persistent debt service pressures, and increased uncertainty regarding external grants have heightened the urgency of strengthening domestic revenue mobilization in The Gambia. This paper examines The Gambia's current revenue performance relative to peers, estimates tax potential and tax effort using frontier methods, evaluates the authorities' Domestic Resource Mobilization Strategy (DRMS), incorporates estimates from the IMF's Revenue Assessment and Yield Tool (RAYT) and identifies priority and feasible reforms to sustainably raise domestic revenue.

## A. Introduction

1. Domestic revenue mobilization (DRM) has long been central to The Gambia's development strategy, but has taken on heightened importance in the current global context. Strengthening DRM would underpin the financing of poverty and inequality reduction, support fiscal consolidation amid elevated debt vulnerabilities, strengthen state-building capacity, and help meet the growing demands of climate adaptation and mitigation. Empirical evidence further suggests that sustained improvements in tax capacity can be growth-enhancing once a critical threshold is reached, with growth tending to accelerate beyond this "tipping point" (Bellon and Warwick, 2025). These considerations have become more urgent as the external financing environment tightens — with declining aid flows, heightened volatility, and tighter financial conditions—increasing reliance on domestic resources and the costs of delayed reform.

2. At the same time, higher revenue mobilization alone will not be sufficient to meet The Gambia's development challenges. The country faces substantial financing needs to advance its development agenda, including investments in human capital, infrastructure, social protection, and climate adaptation. Baseline projections from the IMF's SDG Financing Tool $^{2}$ indicates that, under current policies, The Gambia would achieve the Sustainable Development Goals only after 2054; achieving the SDGs by 2030 would require additional annual financing of about 20.5 percent of GDP. Moreover, elevated public debt and a heavy debt-service burden limit the scope for deficit financing, with debt service currently absorbing close to one-quarter of total revenues and grants. Together, these constraints suggest that closing The Gambia's financing gaps will require a comprehensive approach that combines enhanced domestic reforms with continued access to grants and concessional financing.

3. Achieving durable fiscal gains requires DRM efforts to be complemented by stronger public financial management (PFM) and spending prioritization toward growth- and

equity-enhancing uses. Improvements in public investment management and broader PFM frameworks would strengthen budget credibility, expenditure control, and transparency, while spending prioritization can help ensure that limited resources are directed toward high-impact areas. Strengthening the efficiency and composition of public spending—alongside reforms to enhance DRM—will be essential to ensure that fiscal policy supports inclusive and resilient growth. Against this broader fiscal reform agenda, the remainder of this paper focuses on DRM by assessing recent revenue performance, identifying key constraints, and outlining priority reforms to strengthen revenue outcomes.

## B. Revenue Structure and Recent Trends

4. The Gambia's domestic revenue has increased steadily since 2022, driven primarily by tax revenue. The increase of about 3.7 percentage points of GDP exceeds that observed in regional peer countries and represents a significant improvement in revenue performance.

5. Nevertheless, The Gambia remains highly dependent on external grants, exposing the budget to significant volatility and uncertainty. The share of

![](images/a6370eb38ed628a59c9471c8eb770685726bd17a6b8cdb51fb31faf3176af9f2.jpg)

grants in total government revenue remains substantially higher in The Gambia than in regional comparator countries. On-budget grant inflows have historically been volatile, contributing to fiscal uncertainty and complicating budget planning. In this context, announced global aid cuts by major donors and uncertainty surrounding their magnitude and timing pose rising risks to future budget-support inflows for The Gambia, which could further constrain fiscal policy formulation. Heavy reliance on on-budget grants therefore heightens vulnerability to external shocks and underscores the importance of strengthening DRM to enhance fiscal resilience.

Revenue Composition in The Gambia
(Percent of GDP)

![](images/264c0e5355646fe3093f91f1dab885ad36289220f067a2ff6cdeb3aaef224155.jpg)  
Revenue Composition Comparison, 2025

![](images/d71c8ad9006e6bc289f34aaa33b59f9c4e205d81592fd78ffaddc432f3aebb4b.jpg)

6. At the same time, the tax structure remains skewed, underscoring the need to diversify across tax bases and instruments. Relative to comparator countries, The Gambia relies heavily on customs and trade-related taxes, which account for about 25 percent of tax revenue, compared with an average of 19 percent in low-income country comparators, based on cross-country evidence. This reliance increases exposure to external shocks and reflects the continued dominance of taxes that are relatively easier to administer, while the underlying domestic tax base remains narrow. In this context, the African Continental Free Trade Area (AfCFTA) agreement reinforces the need for structural tax reform, as gradual trade liberalization will further test the sustainability of a revenue system heavily reliant on border taxes. The challenge is therefore not only diversification across tax categories, but more fundamentally diversification across tax bases and instruments, including a stronger contribution from domestic consumption, income, and property taxes.

Tax Composition in The Gambia (Millions of Local Currency)

![](images/63ee6bb4c3d0306b00e6caa3086ce16a854f11249b56f2dc5906b62f030a4f6f.jpg)

Tax Composition Comparison, 2025  
![](images/6975fac483d90bfc2f187e7b66c4938ceeca2e4de4147e3fb92690caa7e18dec.jpg)

7. At around 13 percent of GDP in 2025, tax revenue in The Gambia places the country in the middle of the regional LIC distribution. This comparison underscores that, despite being above the peer average, The Gambia's tax revenue remains below commonly cited adequacy thresholds of 15 percent of GDP (Baer et al., 2025).  
![](images/632baa05f664708df54957ef8f450d9f72f2243e0f695d919237b6a3d9c5379a.jpg)

## C. Estimating Tax Potential and Tax Effort

8. Tax potential analysis provides a structured framework for assessing a country's scope to raise domestic revenue by benchmarking actual tax performance against what could be achieved given its structural economic characteristics and institutional capacity. The difference between actual revenue and estimated tax potential—the tax gap—captures the extent to which weaknesses in policy design, tax administration, compliance, and enforcement constrain revenue outcomes. Importantly, tax potential should be viewed as an illustrative benchmark rather than a binding target, and closing the full gap rapidly is neither expected nor necessarily desirable.

9. Conceptually, tax potential reflects the highest level of tax revenue a country could mobilize under comparable circumstances, based on an empirically derived benchmark from peer countries. Countries operating below this frontier can narrow the tax gap through improvements in policy, administration, and compliance. By contrast, the frontier itself shifts upward only when underlying structural and institutional determinants improve. The distinction is therefore between improving performance within current constraints and easing those constraints through sustained structural and capacity-enhancing reforms.

10. The tax potential estimates are derived using Stochastic Frontier Analysis (SFA), applied to a panel dataset covering 154 countries over 1980–2024, using the methodology described in Benitez et al. (2023). This cross-country empirical approach relates observed tax-to-GDP ratios to a set of structural and institutional fundamentals. The model specifies tax revenue performance as a function of income per capita, economic structure, trade openness, and indicators of governance and institutional quality, while controlling for country-specific and time effects $^{3}$ . Unlike ordinary regression models, SFA explicitly decomposes deviations from the estimated tax frontier into random shocks and a one-sided inefficiency term, allowing the analysis to distinguish structural constraints from shortfalls attributable to policy design, administrative capacity, and compliance.

11. The estimated tax gap for The Gambia indicates that there is space for tax revenue mobilization through policy and administrative reforms. An updated estimate of the average tax potential for The Gambia over the period 2017–23 is 12.6 percent of GDP, lower than the average for LICs (21.6 percent of GDP). Compared to actual tax ratios, this implies a tax gap of about 2.5 percent of GDP on average for The Gambia. This tax gap is lower than the average for LICs (4.9 percent of GDP), indicating relatively strong revenue performance given its structural and institutional characteristics. At the same time, the smaller gap suggests that further gains from closing existing inefficiencies may be limited and mobilizing additional tax revenue will be more challenging without improvements in institutional quality. For example, Baer et al. (2025) show that raising the quality of public institutions in LICs—in general, not only tax institutions—to levels observed in EMEs could generate additional revenue of about 1.2 percent of GDP. This underscores that the scope for further revenue gains hinges critically on complementary improvements in governance, public financial management, and institutional capacity.

The Tax Gap in The Gambia (In percent of GDP)

![](images/c91101ade74a981ae1a2a736f129c5beea817f707d9b04d957189aa911f71249.jpg)

![](images/ee77b0ad0ecfb6747553d378ef0b569c52f819eea82a6df6d178cfcfa52213c0.jpg)

## D. The Authorities' Domestic Resource Mobilization Strategy

12. The country's Domestic Resource Mobilization Strategy (DRMS) for 2026–2030, approved in September 2025, sets out a broad agenda of measures to strengthen The Gambia's domestic revenue base. The DRMS is anchored in a medium-term revenue objective of raising the tax-to-GDP ratio to about 15 percent by 2030, implying an aggregate revenue gain of about 3.2 percent of GDP over 2026–30 $^{4}$ . This revenue target is intended to support fiscal sustainability, reduce reliance on volatile customs revenues and external financing, and create durable fiscal space for priority spending under the Recovery-Focused National Development Plan. The strategy identifies tax and non-tax measures structured around six pillars covering base

expansion, fiscal governance and compliance, the legal framework, tax administration effectiveness and efficiency, governance and monitoring, and institutional capacity building.

13. The six pillars of the DRMS are designed to encompass concrete policy and administrative reforms, including tax expenditure management, income tax and VAT reforms, rental income taxation, property tax reform, investment tax incentives, and reforms related to informality and presumptive taxation. These measures are embedded across the pillars, reflecting the strategy's emphasis on translating high-level objectives into specific, implementable

![](images/acbb1a8d002d9b92489b6adee67f5e3f4ccb7f4c22046439d057b6568aa158b3.jpg)

policy actions. Beyond revenue mobilization, the DRMS articulates broader revenue policy objectives, including improving equity and progressivity of the tax system, strengthening transparency and accountability to reinforce the social contract, enhancing resilience of the revenue base to external shocks, and supporting decentralization through stronger local revenue mobilization.

14. The authorities' medium-term revenue projections are underpinned by a set of tax policy measures aimed at broadening the tax base and rationalizing exemptions, including reforms to investment incentives, payroll taxation, property taxation, and the management of tax exemptions, alongside continued fuel pricing reforms and trade tariff adjustments under AfCFTA.

15. Consistent with this framework, implementation of the DRMS is already progressing across several priority areas.

\- Tax expenditure management. Work has advanced on establishing a tax expenditure framework, including defining the benchmark tax system, compiling an inventory of tax expenditures, and developing methodologies to assess foregone revenue, thereby laying the groundwork for greater fiscal transparency and informed policy decisions. A tax expenditure statement covering data through 2025 has been finalized and transmitted to Cabinet.

\- Income tax and VAT reforms. Legislative reforms are underway to modernize income tax and VAT legislative frameworks, including strengthening the taxation of cross-border transactions, enhancing anti-avoidance provisions, and separating tax administration provisions into a dedicated legal framework.

\- Rental income taxation. Efforts to strengthen rental income taxation are focusing on improving compliance through greater use of third-party information and data-driven tools to better identify taxable rental activity and reduce under-reporting.

\- Property tax reform. Preparatory work is advancing to strengthen property taxation, supported by recent IMF technical assistance, including measures to improve coverage and valuation of recurrent property taxes, modernize the legal framework, and reform property transfer taxation, with the objective of mobilizing underutilized revenue potential while improving equity and local service financing.

\- Investment tax incentives. Reforms to streamline investment-related tax incentive are well advanced, including legislative changes to narrow preferential import treatments, shift away from costly tax holidays, and strengthen customs administration, with the objective of reducing leakages, compliance risks, and administrative costs.

\- Informality and presumptive taxation. Analytical work is starting to better distinguish between size-based informality and non-compliance, informing future reforms to presumptive taxation and broader efforts to expand the tax base while supporting formalization and ease of doing business.

16. While these reforms represent important progress under the DRMS, further policy and administrative efforts will be needed to close remaining gaps and achieve the targeted revenue gains.

## E. Policy Priorities and Reform Options to Support the DRMS

17. Building on the implementation of the DRMS outlined above, IMF technical assistance helps to further prioritize reforms, quantify potential revenue gains, and identify remaining policy gaps. While many reform areas overlap with those identified in the DRMS, the discussion below focuses on areas where additional efforts could yield the largest gains or where reform momentum needs to be strengthened.

## Tax Policy

18. Tax expenditure reform remains central to strengthening revenue performance. Recent technical assistance notes that revenues forgone from tax expenditures are sizable, estimated at about 2.8 percent of GDP in 2024, and mainly driven by legacy Special Investment Certificates granted pri

[中间内容因长度限制已省略]

 adopt a holistic and institutional strategy that integrates tax administration, tax policy, and financial, institutional, or legal reforms to support revenue mobilization (Benitez et al., 2023; Atsebi et al., 2025).

34. More realistically, a feasible increase in ambition would be to target convergence toward LICs and SSA averages, corresponding to an OSI of 0.54 and estimated revenue gains of about 0.7 percentage point of GDP. This scenario would anchor reform objectives in peer performance rather than in aspirational best-case outcomes. To realize this, GRA would need to be supported with sufficient resources to strengthen IT including the deployment of the ITAS and staff capacity, alongside improvements in the legal framework.

35. Successful implementation of GRA's strategic plan is expected to generate additional revenue gains, although these may materialize with a lag. Yields from tax administration improvements often materialize with a lag. This is particularly the case for GRA's planned reforms, including digitalization, where changes may take time to translate into sustained revenue performance. The reform effort should therefore be viewed not only as a source of near-term gains, but also as an investment in stronger medium-term revenue capacity. If implementation is sustained, the impact on the tax-to-GDP ratio could accelerate after the initial five-year period.

## G. Conclusion

36. Domestic revenue performance in The Gambia has improved markedly in recent years but remains subject to important challenges. The Gambia has made notable progress in raising the tax-to-GDP ratio and strengthened fiscal resilience. At the same time, remaining gaps relative to peers, evolving financing needs, and rising external risks underscore the importance of sustaining reform momentum to further enhance revenue capacity over the medium term. Tax potential analysis and estimates from the IMF's Revenue Assessment and Yield Tool (RAYT) suggest that there is scope to raise revenues through more effective policy measures.

## 37. Going forward, reform efforts should focus on both tax policy and revenue

administration. Priority tax policy measures include rationalizing tax exemptions, broadening the tax base, and strengthening the design of key instruments such as VAT and excises. On the administration side, advancing digitalization, strengthening compliance risk management, improving the use of third-party data, enhancing the effectiveness of the Large Taxpayer Office and High-Net-Worth Individual programs, and reinforcing enforcement will be critical. Sustained progress in these areas will be essential to consolidate recent gains and unlock further revenue potential.

## Annex I. RAYT Categories and Coverage in GRA's Corporate Strategic Plan

<table><tr><td>RAYT category</td><td>Coverage in GRA strategic Plan</td><td></td></tr><tr><td>A. Compliance Risk Management</td><td>Full</td><td>CRM is adopted as a core framework and work has commenced to embed the practice</td></tr><tr><td>B. Use of Third-Party Data</td><td>Partially</td><td>The Plan implicit refers to third party data initiatives but does not yet articulate a comprehensive, end to end third party data strategy.</td></tr><tr><td>C. Digitalization</td><td>Full</td><td>Digital transformation is the Plan&#x27;s central pillar and is critical to improvements in compliance management</td></tr><tr><td>D. Service Orientation</td><td>Partially</td><td>Client experience initiatives are referred to, but several elements are only implicitly addressed or unevenly covered.</td></tr><tr><td>E. Public Accountability</td><td>Partially</td><td>Integrity, internal audit, and governance reforms are included, but systematic publication practices are not fully specified as commitments.</td></tr><tr><td>F. Autonomy</td><td>Partially</td><td>Organizational realignment and performance management are addressed. RAYT does not identify areas with a substantial revenue impact.</td></tr><tr><td>G. Large Taxpayer Office / HNWI</td><td>Partially</td><td>Large taxpayers are referenced through CRM and operational KPIs, but the Plan does not set out a distinct, comprehensive HNWI reform program.</td></tr><tr><td>H. Enforcement</td><td>Partially</td><td>Enforcement is supported indirectly through legal reform, CRM, and payment initiatives, but enforcement powers, strategies, and prioritization are not articulated.</td></tr><tr><td>I. Human Resource Management</td><td>Full</td><td>The Plan contains a comprehensive package covering leadership, skills, change management, performance management, and competency based HRM.</td></tr></table>

## References

Adan, H., Atsebi, J., Gueorguiev, N., Honda, J., and Nose, M. (2023). Quantifying the Revenue Yields from Tax Administration Reforms. IMF Working Paper: WP/23/231. International Monetary Fund, Washington, DC.

Atsebi, J., Gueorguiev, N., and Nose, M. (2025). Enhancing Tax Capacity: Revenue Gains from Strengthening Tax Administration. IMF Working Paper: WP/25/219. International Monetary Fund, Washington, DC.

Baer, K., M. Bellon, M. Davies, R. de Mooij, V. Gaspar, A. Lemgruber, M. Mansour, F. Sawadogo, M. Takebe, and C. Vellutini (2025). Building Tax Capacity for Growth and Development: Evidence-Based Analysis for Mobilizing Domestic Revenue. IMF Departmental Paper. International Monetary Fund, Washington, DC.

Bellon, M., and Warwick, R. (2025). State Capacity, Institutions and Growth: Taxing for Takeoff—Revisiting the Tax Tipping Point. IMF Working Paper.

Benitez, J. C., Mansour, M., Pecho, M., and Vellutini, C. (2023). Building Tax Capacity in Developing Countries. IMF Staff Discussion Note: SDN/2023/006. International Monetary Fund, Washington, DC.
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
