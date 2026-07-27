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
# Inside Greece's Housing Affordability Paradoxes

Tarak Jardak and Summer (Yutian) Cai

SIP/2026/066

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on April 30, 2026. This paper is also published separately as IMF Country Report No 26/109.

2026
JUL

![](images/dffec6b71214d7e8040b69977210ebea3b181e36f258bdba55c8592442b9c242.jpg)

# IMF Selected Issues Paper European Department

Inside Greece's Housing Affordability Paradoxes Prepared by Tarak Jardak and Summer Cai

Authorized for distribution by Joong Shik Kang
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on April 30, 2026. This paper is also published separately as IMF Country Report No 26/109.

ABSTRACT: Housing affordability is a key challenge in Greece despite high homeownership rates and a relatively large housing stock. This paper investigates the drivers of this apparent paradox using regional housing market data and household-level EU-SILC microdata. The analysis shows that affordability pressures resulted from strong and increasingly concentrated demand, high recurring housing costs, persistent supply constraints, and mismatches between the housing stock characteristics of and household needs. The paper discusses reforms to improve affordability, including through a more efficient use of existing stock, a reduction of the risk premium for short-term rental, and better targeted demand support measures.

RECOMMENDED CITATION: Jardak, Tarak, and Summer (Yutian) Cai. Inside Greece's Housing Affordability Paradoxes. IMF Selected Issues Paper (SIP/26/066). Washington, D.C.: International Monetary Fund, 2026.

<table><tr><td>JEL Classification Numbers:</td><td>R21; R31; D31; G51; H24</td></tr><tr><td>Keywords:</td><td>Housing affordability; Housing cost burden; Residential real estate; Housing supply constraints; Household vulnerability; Housing demand; Housing mismatches, Foreign residential investment; Short-term rental, Housing policy; EU-SILC; Greece</td></tr><tr><td>Authors&#x27; E-Mail Address:</td><td>tjardak@imf.org, scai@imf.org</td></tr></table>

SELECTED ISSUES PAPERS

# Inside Greece's Housing Affordability Paradoxes

Greece

Prepared by Tarak Jardak and Summer (Yutian) Cai $^{1}$

## GREECE

SELECTED ISSUES

April 30, 2026

Approved By

Prepared By Tarak Jardak (EUR).

European Department

## CONTENTS

INSIDE GREECE'S HOUSING AFFORDABILITY PARADOXES 3
A. Introduction 2
B. How Severe are Housing Affordability Challenges? 4
C. Why is the Housing Cost Burden so High? A Micro Perspective 6
D. What Drives Housing Market Imbalances Despite Ample Stock? 9
E. Policies 13
F. Conclusions 17

## FIGURES

1. Greece Housing Affordability Paradoxes 3  
2. House Price Dynamics 4  
3. Rent Price Dynamics 5  
4. Housing Cost Burdens 7  
5. Households Characteristics and Housing Affordability: Who is Affected the Most? 7  
6. Households Joint Wealth-Income Distribution 8  
7. Energy Poverty Trap 9  
8. Housing Demand 10  
9. Distribution of Supply by Price and Size Range 11  
10. Supply Bottlenecks 13

## TABLE

1. Impact of STR Intensity on Asking Prices and Rent \_\_\_\_ 13
References \_\_\_\_ 19

# INSIDE GREECE'S HOUSING AFFORDABILITY PARADOXES $^{1}$

Like many other European countries, Greece faces growing affordability challenges. House prices and—more recently rents—have outpaced income gains, reflecting strong and increasingly concentrated demand, including from foreigners, alongside structural supply rigidities and supply-demand mismatches. Affordability pressures are compounded by high recurring costs, especially utility bills, due to old and energy inefficient stock and limited energy upgrades. Policy priority should be given to mobilizing the underutilized housing stock by combining renovation programs with disincentives to vacancy and by addressing bottlenecks such as fragmented co-ownership, stranded assets related to legacy distressed debt, and unresolved construction compliance issues. The authorities should assess the effectiveness of restrictions on short-term rentals and take measures to reduce the risk premium associated with long-term rental while improving price discovery. Expanding the supply of social and affordable housing requires close public-private partnerships while reducing regulatory uncertainty and streamlining potential zoning and building permits regulations. Facilitating labor and capital reallocation within the construction sector and strengthening domestic workforce training would help raise productivity, ease labor shortages and contain construction costs.

## A. Introduction

1. Like many European countries, Greece is facing mounting and multifaceted housing affordability challenges with potentially significant socioeconomic consequences. In a recent OECD survey, two-thirds of surveyed Greek households declared being concerned about finding or maintaining adequate housing. Since 2017, house prices have rebounded from post-crisis correction

and outpaced income gains. This, together with higher mortgage rates, low savings and borrowing constraints, caused homeownership rates to drop. Rental affordability has also more recently deteriorated, albeit with some heterogeneity across markets and segments. Although improving from post-crisis peaks, the housing cost burden and the share of overburdened households remain very high. The resulting financial strain leads to high level of arrears and could amplify consumption volatility

![](images/01a0dd4d4411c0035a73ec2ca2d1422a0531780cbd3065707a4eefee14d89640.jpg)  
Sources: OECD (2025), More Effective Social Protection for Stronger Economic Growth: Main Findings from the 2024 OECD Risks that Matter Survey, OECD Publishing, Paris, https://doi.org/10.1787/3947946a-en.
Notes: Respondents had the option of selecting: 1. Not at all concerned; 2. Not so concerned; 3. Somewhat concerned; 4. Very concerned; 5. Can't choose / Not applicable

and growth. It also affects the ability of homeowners to maintain and renovate their properties, leading to high depreciation rate and lower housing quality. Moreover, deteriorating affordability pushes young Greeks to stay longer with their families with delayed independence affecting the already low fertility rate (Hallaert and Vassileva, forthcoming). Finally, rising housing costs can reduce labor mobility toward more productive sectors and regions, weakening competitiveness and the country's ability to retain and attract talent.

2. These affordability pressures coexist with seemingly favorable structural conditions, raising potential paradoxes. First, the high housing cost burden contrasts with the fact that more than 60 percent of Greek households are outright owners (i.e., with no mortgages), incurring only recurring housing costs. Second, Greece has one of the highest dwelling stock per capita with declining population but 35 percent of these properties not used as primary residence, of which one third (12-13 percent of total stock) is vacant. These puzzles point to deeper structural issues, including supply rigidities and mismatches between housing supply and demand.

Figure 1. Greece Housing Affordability Paradoxes  
![](images/18c9338144ea0e8db7f87edcb9e482ccc6e7cb372fcb6399a650b65d46bfcd84.jpg)

![](images/10fb0d30111a98839e225e9e405c11d149d8a094db78b00b4728b37a76914c0f.jpg)

3. To tackle these challenges, the authorities have deployed a combination of demand-and supply-side measures and are developing a new housing strategy. On the demand side, policies include subsidized housing loans for first-time buyers, other help-to-buy measures and rental refunds. In parallel, the regulatory framework for the Golden Visa program has been tightened through higher investment thresholds. On the supply side, the strategy focuses on mobilizing the idle housing stock through renovation programs and tax incentives to boost supply of long-term rentals (LTRs) while restricting short-term rentals in targeted locations. The authorities also plan to develop social housing and student accommodation. In parallel, they are designing a new housing strategy, informed by a better mapping of housing needs and available supply.

4. To better understand the apparent paradoxes and inform the authorities' housing strategy, this paper addresses several key questions. First, how severe are housing affordability pressures (Section B), and what drives the high housing cost burden (Section C)? Second, what explains housing market imbalances? What is the role of foreign demand and short-term rentals, and what factors constrain effective housing supply (Section D)? Finally, what policy measures are needed to address these challenges (Section E)?

## B. How Severe are Housing Affordability Challenges?

5. House prices have outpaced income growth in recent years, largely reflecting a catch-up effect, while overvaluation remains moderate. Prior to the sovereign debt crisis, Greece experienced a prolonged housing boom supported by strong income growth, financial liberalization and expanding mortgage credit following euro adoption, which contributed to rising residential investment and housing demand. The crisis abruptly reversed this cycle with prices falling by more than 40 percent over 2008-16. Since then, prices have been recovering steadily, increasing cumulatively by about 85 percent against 47 percent for disposable income per capita. Most of the price increase occurred after the pandemic (+61 percent since 2020Q4) and unlike in other euro area (EA) countries, the ECB's monetary policy tightening impact on prices has been rather muted. Overvaluation is estimated at around 10 percent. Geographically, asking prices from online real estate platform Spitogatos show significant heterogeneity with prices significantly higher in Attica, Thessaloniki and touristic hubs than in the rest of the country.

Figure 2. House Price Dynamics  
![](images/2a444d94ac5ccc265032e4a1fa086368009d8a97b737d452ad4c03c65bd38ee5.jpg)

![](images/1401926c8e71bcd436c1e89ffae34a2f7fbe62753291dd3919134cbebd1d9f19.jpg)

## 6. Access to homeownership is mainly hindered by mortgage affordability and low savings. Reflecting the rapid increase in house prices relative to income as well as higher mortgage

rates, the housing affordability index (Biljanovska et al., 2023)—which measures the ability of the median household to purchase a typical property while meeting other essential consumption needs—has deteriorated in recent years. Assuming a debt service-to-income (DSTI) ratio of 30 percent and a loan-to-value (LTV) ratio of 70 percent (respectively 80 percent), the median household would fall about 7 percent (respectively 17 percent) short of the income needed to qualify for a mortgage in 2024. Even when household income is sufficient to satisfy

![](images/147fefc2285d4b1de01f481bf1bf366f937872b462b85814f208b33693bacaab.jpg)  
Notes: HAI is defined as in Biljanovska et al., 2023, Housing Affordability: A New Dataset, IMF WP 2023/247. The number of years of savings assumes an annual saving rate of 10 percent of disposable income.

typical DSTI requirements, the downpayment required to access mortgage credit remains a major barrier. Assuming a saving rate of 10 percent per year, it would take roughly 24 years (respectively

14 years) to accumulate the required downpayment. Access to mortgage credit is further constrained by the crisis legacy, which translates into conservative bank lending standards.

7. Rent prices have been slower to adjust but are increasingly showing signs of pressure. The rent component of the Harmonized Index of the Consumer Price (HICP) remains below pre-crisis levels. However, rent inflation accelerated post-pandemic, culminating at 10 percent in 2025. Additionally, market-based indicators point to stronger dynamics for asking rents per square meter, suggesting faster increases for new leases and continued upward pressure on rent in coming years. Finally, significant heterogeneity across regions and segments is also evident, with much stronger pressures emerging in large metropolitan areas such as Thessaloniki and Athens.

Figure 3. Rent Price Dynamics  
![](images/d16b1eeaad9465fd3a14caa092bc5e4462b323c7cf4c6af80a3f3fdcd0bfd593.jpg)

![](images/419fed8afc936cfd98aad18c747fba8db2c1b5a5c0e6f0c00c0b3f3b5cebb749.jpg)

8. The housing cost burden remains persistently elevated, although it remains lower than post-crisis peaks. $^{2}$ The share of disposable income spent on housing costs has been historically high in Greece and increased further during the sovereign debt crisis. This burden has moderated somewhat as the economy recovered, but the improvement has recently stalled and even reversed for lower income households. According to our estimates based on the EU Statistics on Income and Living Conditions (EU-SILC) micro data, the median housing cost (including mortgages) exceeded a third of disposable income in 2025. Approximately two out of five households are overburdened (i.e. they spend more than 40 percent of disposable income on housing-related expenditure) and an additional 20 percent of households spend 30-40 percent of disposable income on housing costs, making them potentially vulnerable in case of income or interest rate shocks.

9. Other indicators point to housing-related difficulties. To cope with affordability challenges, young people stay longer with their parents and households tend to live in smaller houses contributing to a high overcrowding rate, particularly for renters. High housing costs are also associated with a large share of households in arrears on their housing payments (41.8 percent according to EU-SILC survey) and reporting difficulty to warm and cool their properties.

![](images/6601583cae490d76c20f1650510c8cd264ad2bbb0d1603195739e3aba029f428.jpg)

Figure 4. Housing Cost Burden  
![](images/2d904b338d3689f705bb30721b31b4892f4f0bb5ec67010243fdac370b623f2b.jpg)

![](images/dcd6bb6fa79c812a4fc8558fb2c60fae8a2de5bce5fbc353986c6dc82d5519e1.jpg)

![](images/4570ed2484b7d6f48121ce3d6ffa56fbae00d0aef5c2b858d6c6d0c9a0b8cd8a.jpg)

## C. Why is the Housing Cost Burden so High? A Micro Perspective

## 10. The housing cost burden is fundamentally rooted in income capacity.

\- Based on pooled repeated cross-sections regression of the housing cost overburden on household characteristics (using EU-SILC micro data over 2021-25), tenure emerges as a key determinant, but its effect is highly conditional on income. Relative to outright owners, households with a mortgage and renters face a significantly higher probability of overburden. However, these differences widen substantially when interacted with income. Predicted probabilities indicate that low-income households face markedly higher risks across all tenures. Holding other characteristics constant, being in the bottom 40 percent of the income distribution increases the probability of being overburdened by large margins. For example, the predicted probability for low-income mortgagors (renters) exceeds 90 percent, compared to about one-third for higher-income households. A similar gradient is observed for renters, where a low-income household faces four times larger probability of being overburdened than higher income. Even among outright owners, the probability increases sharply for low-income households, underscoring that ownership does not fully shield against affordability pressures.

\- Other household characteristics also play a significant role. Single-person and single-parent households exhibit higher probabilities of overburden, reflecting reduced economies of scale in housing consumption. Lower education and weaker labor market attachment are also associated with higher risk, consistent with their impact on income capacity. Finally, the regional dimension also plays a role, especially for renters. More specifically, households renting in Attica and Central Macedonia (Thessaloniki) have a higher probability of being overburdened than other regions.

Figure 5. Households Characteristics and Housing Affordability: Who is Affected the Most?  
![](images/01f57382c1bbea545a0bc240dd26250a160b75c9c16d71ddf0a26f0058fb1372.jpg)

![](images/74fa162ea1be91bf08147d1330762b05e035c296f851933957bffdd6c68a3564.jpg)

![](images/5b727205f765199e979fc423d4c67c280e89d492e389aef3e2140c0bfe3679c2.jpg)

![](images/e4ba91ac3ff2f13929fceea6d920dc9a32ae85e8207d5acbf684fafd9f8a781a.jpg)  
Notes: The probability of housing cost overburden is estimated using a logit model on pooled EU-SILC microdata (2021–25). The dependent variable equals 1 if total housing costs exceed 40 percent of disposable income. The estimating equation is: $Pr(Overburden_{i} = 1) = \Lambda(\alpha + \beta 1\ Tenure_{i} + \beta 2\ LowInc_{i} + \beta 3(Tenure_{i} \times LowInc_{i}) + \gamma'X_{i} + \delta_{r} + \tau_{t})$ where $\Lambda(u) = 1/(1 + e^{(-u)})$ . $X_{i}$ includes other household characteristics (size, type, age, education, employment), while $\delta_{r}$ and $\tau_{t}$ denote region and year fixed effects. $LowInc_{i}$ is a dummy taking the value 1 if the household belongs to the bottom 40 percent of the income distribution. The model is estimated using survey weights.
Predicted probabilities are computed as: $P_{-}i = 1/(1 + e^{(-X_{-}i\beta)})$ .

These probabilities are evaluated for representative household profiles (e.g., by tenure and income group), holding other characteristics constant, to compare housing affordability risks across groups.

## 11. Compositional effects and changes in preferences have further increased aggregate vulnerability.

\- The joint distribution of income and wealth (households finance and consumption survey) has shifted over 2011-21 and shows a greater share of households holding illiquid housing assets but with limited current income (asset-rich income-poor). As a result, outright owners—who are typically expected to face low housing costs—still incur significant expenses relative to income, particularly when liquidity constraints prevent smoothing through borrowing or asset liquidation. This disconnect between stock wealth and flow income is a central feature of the Greek housing affordability puzzle.

\- Demographic and behavioral shifts have increased per-household housing consumption. The rise in single-person and single-parent households (12 percentage points since 2011), alongside changing preferences (e.g., greater share of students living indepen

[中间内容因长度限制已省略]

co-living given the prevalence of large properties.

## Advice 5: Recalibrating Demand Measures to Reduce Price Capitalization

## 27. Demand-side support should be better targeted and calibrated to avoid price

capitalization and potential regressive effects. While potentially beneficial in the short term, evidence confirms that when supply is inelastic, untargeted support tends to benefit landlords and sellers rather than improving affordability (OECD, 2021). Indexing the rent refund on the monthly payment could help enhance transparency of the rental market but will come at a higher fiscal cost in the future. Going forward, refining eligibility criteria and means-testing would improve cost-

effectiveness and limit regressive outcomes. Similarly, the authorities should assess the impact of tax incentives, such as the VAT exemption on new construction, which could tend to benefit richer households or real estate companies. Should this be the case, the authorities should consider phasing it out or possibly reorienting it toward renovation.

## Advice 6: Strengthening Policy Coordination

28. Improving housing affordability requires stronger policy coordination across labor, financial, energy, and regional policies to address underlying structural drivers of income, costs, and demand concentration. Labor market measures to increase participation and broader supply-side reforms to boost productivity and wages would support income growth. On the financial side, easing credit constraints is essential, including through accelerating the resolution of legacy debt, promoting greater competition in the banking sector, and encouraging banks to develop tailored financing products for housing renovation. Lowering energy costs requires continued efforts to expand renewable energy and improve interconnections—particularly for island regions.

## F. Conclusions

## 29. Our analysis's main conclusions are as follows:

\- Housing affordability is at the center of a self-reinforcing loop between households' vulnerability, aging housing stock, and societal/demographic dynamics changes.

\- Greece faces a housing allocation problem rather than a standard housing shortage. Structural challenges impede efficient use of the existing stock. Spatial distribution, segmented demand, and market inefficiencies exacerbate supply demand-mismatch.

\- Overall, government measures go in the right direction but need further consolidation, greater focus on affordable supply, and a mix between sticks and carrots to mobilize the existing stock and reduce mismatches. Alleviating capacity constraints in the construction sector and boosting productivity is key to unlock supply and contain the increase in construction costs. The ongoing digitalization and centralization of information on properties will help better identify the problems and design adequate policies. Finally, housing policies are not the only lever; exploiting synergies with other policies is important.

## References

Alpha Bank (2025). Housing Market Insights. Athens.

Alpha Bank (2026). Housing Market Insights. Athens.

Athanassiou, S., & Kotsi, E. (2023). The Sharing Economy in Greece: Short-Term Rental Developments. Athens: Research Report.

Athens University of Economics and Business (2025). Economic and Housing Impact of Short-Term Rentals in Greece. Athens.

Bank of Greece (2025). Economic Bulletin No. 61: Housing Affordability for Greek Households. Athens.

Barron, K., Kung, E., & Proserpio, D. (2021). The Effect of Home-Sharing on House Prices and Rents: Evidence from Airbnb. Marketing Science, 40(1), 23–47.
https://doi.org/10.1287/mksc.2020.1227

Biljanovska, N., Fu, M. C., & Igan, M. D. (2023). Housing Affordability: A New Dataset. IMF Working Paper No. 2023/247. International Monetary Fund. https://doi.org/10.5089/9798400259746.001

European Commission (2022). Greece Country Report 2022. Brussels.
https://commission.europa.eu/system/files/2022-05/2022-european-semester-country-report-greece\_en.pdf

European Commission (2025). Housing in the European Union: Developments and Policy Challenges. Brussels.

Foundation for Economic and Industrial Research (2025). Trends, Challenges and Prospects of the Construction Sector in Greece. Athens. https://iobe.gr/wp-content/uploads/2026/01/RES\_05\_F\_24062025\_REP\_EN.pdf

Foundation for European Progressive Studies (2024). Housing as Investment in Southern Europe. Brussels.

Housing Europe Observatory (2023). Tools to Deal with Vacant Housing. Brussels.

International Monetary Fund (2025). Golden Visa Programs. IMF Working Paper No. 2025/008. Washington, DC.

Karamanis, D., Kotsogiannis, C., & Papapetrou, E. (2026). Threshold-Based Policies and Distortions in Housing Markets. Working Paper No. 359. Bank of Greece. https://doi.org/10.52903/wp2026359

Kontonikas, A., & Pyrgiotakis, E. (2025). A Comprehensive Analysis of Transactions in the Greek Residential Property Market. Hellenic Observatory, London School of Economics and Political Science. London. https://www.lse.ac.uk/Hellenic-Observatory/Assets/Documents/Publications/GreeSE-Papers/GreeSE-No204.pdf

Organisation for Economic Co-operation and Development (2021). Brick by Brick: Building Better Housing Policies. Paris: OECD Publishing. https://doi.org/10.1787/b453b043-en

Organisation for Economic Co-operation and Development (2022). Housing Taxation in OECD Countries. Paris: OECD Publishing. https://doi.org/10.1787/03dfe007-en

Piraeus Bank (2025). Greek Residential Real Estate Market Outlook. Athens.

Vettas, N., Mavropoulos, A., Antonopoulou, C., Valentis, H., Gatopoulos, G., & Kontos, C. (2026). Housing in Greece: Trends, Challenges and Prospects. Dianeosis. Athens (in Greek).
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
