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
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## BULLETS AND BUDGETS MEASURING DEFENSE SPENDING MULTIPLIERS

João Tovar Jalles, John Beirne, and Donghyun Park

NO. 857

July 2026

ADB ECONOMICS

WORKING PAPER SERIES

# Bullets and Budgets: Measuring Defense Spending Multipliers

João Tovar Jalles, John Beirne, and Donghyun Park

No. 857 | July 2026

The ADB Economics Working Paper Series presents research in progress to elicit comments and encourage debate on development issues in Asia and the Pacific. The views expressed are those of the authors and do not necessarily reflect the views and policies of ADB or its Board of Governors or the governments they represent. ADB's prohibited investment activities list includes the production of or trade in weapons and munitions, including paramilitary materials.

João Tovar Jalles (joaojalles@gmail.com) is a senior associate professor at the University of Lisbon. John Beirne (jbeirne@adb.org) is a principal economist at the Economic Research and Development Impact Department, Asian Development Bank. Donghyun Park (donghyun.park@seacen.org) is director of Macroeconomic and Monetary Policy Management, The South East Asian Central Banks (SEACEN) Research and Training Centre.

© 2026 Asian Development Bank
6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines
Tel +63 2 8632 4444; Fax +63 2 8636 2444
www.adb.org

Some rights reserved. Published in 2026.

ISSN 2313-6537 (print), 2313-6545 (PDF)

Publication Stock No. WPS260334-2

DOI: http://dx.doi.org/10.22617/WPS260334-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed to another source, please contact the copyright owner or publisher of that source for permission to reproduce it. ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use the ADB logo.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

## Note:

In this publication, “\$” refers to United States dollars.

## ABSTRACT

This paper examines the macroeconomic effects of defense spending shocks in emerging markets and developing economies (EMDEs), with a focus on Asia and the Pacific over 1990–2023. Using large cyclically adjusted defense shocks identified through local projections, we find that defense spending generates modest but persistent positive output responses in EMDEs, while effects in advanced economies are weak or negative. Within EMDEs, multipliers are strongest in South Asia and weaker in East Asia, reflecting differences in labor intensity and capital intensity of procurement. Functional decompositions show that core military outlays and defense-related research and development drive the positive effects. State dependence is central: fiscal space, revenue capacity, financial development, institutional quality, and—critically—conflict exposure shape both the size and persistence of multipliers, with much stronger effects in high conflict environments. Regional spillovers are weak, short-lived, and turn negative at longer horizons. Extensive robustness checks confirm the stability of these findings.

Keywords: defense spending shocks, fiscal multipliers, emerging markets, Asia and the Pacific, state dependence, local projections

JEL codes: H50, H56, E62, F41, O23, C33

## 1. INTRODUCTION

Defense spending has long occupied a contested space in economic policy. On one side, Keynesian perspectives emphasize its potential to stimulate demand and output, especially in economies facing cyclical downturns (Ramey, 2011; Batini et al., 2014). On the other, classical and endogenous growth arguments stress the risks of crowding out: military outlays may divert resources away from more productive investments in infrastructure, education, or health, thereby undermining long-term growth prospects (Barro, 1991; Dunne and Tian, 2015). For emerging markets and developing economies (EMDEs), where fiscal space is often constrained and external vulnerabilities high, the trade-offs are particularly acute. These tensions are further amplified in environments exposed to elevated geopolitical risk and active conflict, where security considerations may dominate traditional growth–efficiency trade-offs.

Recent trends highlight the urgency of reassessing these questions. According to the Stockholm International Peace Research Institute (SIPRI), global military expenditure reached a record \$2.4 trillion in 2023, with EMDEs in Asia accounting for over one-third of the increase (SIPRI, 2024). The People's Republic of China (PRC) alone spent \$296 billion—nearly 40% of regional defense outlays. Other EMDEs in Asia and the Pacific, such as Viet Nam and the Philippines, have increased defense budgets by more than 50% over the past decade. Even smaller economies are affected: Indonesia and Malaysia have gradually raised defense burdens to about 1.2%–1.5% of gross domestic product (GDP) while Pacific island countries, though spending less in absolute terms, face mounting security commitments.

These developments stand in contrast to other EMDE regions, where defense spending has remained stable or declined relative to GDP. In Latin America, average military expenditure has hovered around 1.3% of GDP since the 1990s, while in sub-Saharan Africa, spending share fell from 2.3% of GDP in 2000 to 1.6% in 2022 (SIPRI, 2024). Asia and the Pacific thus emerges as an outlier: defense budgets are rising faster and more persistently than in peer EMDEs, reflecting both heightened geopolitical risks and domestic political priorities.

The economic implications are unclear. Some argue that ramping up defense spending can boost output in the short run by mobilizing idle resources (Benoit, 1978; Kollias et al., 2004). Others caution that such spending is capital-intensive, less labor-absorbing, and yields limited spillovers, thereby generating smaller multipliers than investment in infrastructure, education, or health (Gupta et al., 2004; Deger and Sen, 1995). For Asia and the Pacific EMDEs, where developmental needs remain pressing and fiscal buffers uneven, the central policy question is whether higher defense outlays provide macroeconomic stimulus or instead crowd out more productive investment. This trade-off between short-run stimulus and medium-term displacement is therefore at the heart of the policy debate surrounding defense spending in EMDEs. Unlike infrastructure, health, or education outlays, military expenditure is rarely justified on growth grounds alone. Its macroeconomic effects must therefore be evaluated primarily through the lens of opportunity costs—namely, whether defense shocks crowd in private activity through demand spillovers or crowd out more productive forms of public and private investment. This assessment is incomplete without accounting for both conflict exposure and cross-border spillovers from regional military buildups.

This paper addresses that question by estimating defense spending multipliers in EMDEs, with a particular focus on Asia and the Pacific. Using the United Nations' (UN's) Classification of the Functions of Government (COFOG) to identify military expenditure as a share of GDP, we construct cyclically adjusted defense spending shocks following country-specific output elasticities. Exogenous shocks are defined as large increases—exceeding one standard deviation above historical means—thus capturing discretionary policy changes rather than automatic stabilizers. We then employ the local projections framework of Jordà (2005) to estimate impulse responses of output, investment, and external balances. We augment this framework to incorporate both conflict-based geopolitical risk and regional spillover channels.

Our contributions are threefold. First, we provide new causal evidence on the macroeconomic effects of defense spending in EMDEs, a context where empirical work remains limited compared to advanced economies (IMF, 2021; Ramey, 2019). Second, we highlight Asia and the Pacific as a critical regional case where geopolitical pressures have fueled sustained increases in military budgets. Third, we explore nonlinearities: do multipliers depend on debt levels, external balances, or institutional quality? These conditions are especially relevant for EMDEs, where fiscal and external vulnerabilities often constrain policy effectiveness (Auerbach and Gorodnichenko, 2013; Ilzetzki et al., 2013). In addition, we disaggregate defense spending into its main functional components—core military outlays, civil defense, defense-related research and development (R&D), and foreign defense aid—allowing us to assess which categories, if any, generate meaningful growth dividends. $^{1}$

The findings show that defense shocks in EMDEs produce positive and persistent output effects, with multipliers reaching around 0.7%–1% after 8 years, while advanced economies experience weak or even negative responses. Within EMDEs, South Asia displays strong and sustained gains, whereas East Asia exhibits muted effects due to the capital-intensive nature of defense procurement. Functional decomposition reveals that only core military spending and defense-related R&D contribute positively to growth, while civil defense and foreign aid exert no significant effects. State dependent analysis further shows that fiscal space, trade openness, financial development, revenue capacity, and institutional quality strongly shape the size and persistence of multipliers. Crucially, defense spending is substantially more expansionary in high conflict environments, while regional defense shocks generate only weak short-run spillovers and negative medium-run effects. Taken together, the evidence indicates that the macroeconomic impact of defense spending is neither universally expansionary nor contractionary, but highly conditional on country circumstances and spending composition.

The remainder of the paper is organized as follows. Section 2 reviews the literature on defense spending and economic outcomes. Section 3 outlines our identification strategy and empirical methodology. Section 4 presents data and stylized facts for EMDEs and Asia and the Pacific. Section 5 reports baseline and nonlinear results, including decomposition by spending category, and analyzes regional spillovers. Section 6 concludes with policy implications.

## 2. LITERATURE REVIEW

## 2.1. Theoretical Framework

The economic effects of defense spending have long been debated, reflecting the tension between its potential as a short-term stimulus and its risks as a long-term drag on growth. Early contributions emphasized its role in driving aggregate demand and generating technological spillovers (Benoit, 1978; Smith, 1980). From a Keynesian perspective, increases in government expenditure—including military outlays—can support output by mobilizing idle capacity, particularly in downturns or under security threats (Batini et al., 2014). In this view, defense spending may function as a countercyclical tool that stimulates activity in the short run.

By contrast, neoclassical and endogenous growth theories stress the potential costs. Military spending is often capital-intensive, less labor-absorbing, and yields fewer positive externalities compared to education, health, or infrastructure investment (Deger, 1986; Heo and Eger, 2005). Moreover, it may crowd out private investment, reduce the accumulation of human capital, and divert fiscal resources from more productive uses (Barro, 1991; Deger and Sen, 1995). Financing considerations add further risks: debt-financed defense buildups can worsen external balances, raise sovereign risk, and undermine macroeconomic stability (Knight et al., 1996).

Taken together, theory suggests an inherent ambiguity: while defense spending can generate demand-driven growth in the short term, it may impose structural and financing costs that weaken productivity and sustainability in the long term. This tension motivates reduced form empirical strategies, such as local projections, that allow the data to reveal which of these competing mechanisms dominate in practice and under what conditions.

## 2.1. Empirical Evidence

Empirical results mirror this theoretical ambiguity. A large body of work points to small or negative multipliers. Gupta et al. (2004) find that defense outlays in developing countries often displace public investment in infrastructure and social sectors, undermining productivity and inclusiveness. Dunne and Tian (2015), in their survey of more than 3 decades of research, conclude that the average growth effects of defense spending are weak or negative, especially in low- and middle-income countries.

Other studies identify short-term expansionary effects. Ramey (2011) shows that United States defense-driven fiscal shocks yielded positive, though modest, multipliers, while Kollias et al. (2004) argue that military outlays can stimulate output in the North Atlantic Treaty Organization (NATO) countries by mobilizing idle capacity. These results suggest that timing and state conditions—particularly slack and security threats—matter for the short-run impact of defense spending. Related to this, IMF (2026a) note that rising geopolitical tensions are leading to more frequent defense spending booms. Using a global sample of advanced and emerging economies over the period 1946 to 2024, they find that booms in defense spending are associated with higher defense spending of around 2.7 percentage points of GDP on average and last for over two-and-a-half years. Economic activity is found to strengthen in the short-term through higher consumption and investment, notably in defense-related sectors. At the same time, IMF (2026a) finds that defense outlays lead to higher inflation in the short-term and a deterioration in fiscal balances, public debt levels, and external balances. The analysis also finds that while defense spending multipliers are close to 1 on average, this depends on how the spending is allocated and financed. $^{2}$

The broader fiscal multiplier literature reinforces this point. In EMDEs, multipliers are generally smaller than in advanced economies due to higher openness, weaker institutions, and financing constraints (Ilzetzki et al., 2013; IMF, 2014). State dependence further complicates the picture: Auerbach and Gorodnichenko (2013) find that multipliers are larger in recessions, under low debt, and when external balances are strong. While much of this empirical work has focused on public investment or consumption multipliers (Miyamoto et al., 2020), systematic evidence on defense spending multipliers in EMDEs remains scarce. Asia and the Pacific, in particular, has attracted growing attention due to its rising share of global military expenditure and unique geopolitical risks. According to SIPRI (2024), the region now accounts for nearly 30% of global defense outlays. However, earlier studies yield mixed evidence on the macroeconomic effects of such spending (Yildirim et al., 2005; Deger and Sen, 1995).

Despite this rich literature, three gaps remain. First, much evidence is correlational, making it difficult to isolate exogenous defense shocks from endogenous responses to growth or conflict. Second, cross-country studies often pool advanced and developing economies, obscuring the distinct fiscal and institutional contexts of EMDEs. Third, Asia and the Pacific—epicenter of rising defense budgets—remains understudied relative to other EMDE regions. This paper addresses these gaps by identifying cyclically adjusted defense spending shocks using COFOG data and estimating their dynamic effects in a panel local projections framework that explicitly incorporates fiscal, external, and institutional heterogeneity.

## 3. A SIMPLE THEORETICAL FRAMEWORK

We outline a stylized model to illustrate the channels through which defense spending affects output, and to motivate our empirical specification. Consider an economy where output is given by:

$$
Y _ {t} = C _ {t} + I _ {t} + G _ {t} ^ {c} + G _ {t} ^ {m} + N X _ {t}\tag{1}
$$

where $C_{t}$ is household consumption, $I_{t}$ is private investment, $G_{t}^{c}$ is civilian government spending, $G_{t}^{m}$ is military (defense) spending, and $NX_{t}$ is net exports.

In the short run, higher military outlays directly raise aggregate demand, consistent with a Keynesian mechanism. If idle resources are present, the multiplier is positive,

$$
\frac {\partial Y _ {t}}{\partial G _ {t} ^ {m}} > 0\tag{2}
$$

implying that defense spending can temporarily boost output. At the same time, however, defense expenditures may require higher taxation or additional borrowing. When financed through debt accumulation, the interest rate increases according to

$$
r _ {t} = r ^ {*} + \varphi D _ {t}\tag{3}
$$

where $D_{t}$ denotes public debt. This crowds out private investment, since

$$
\frac {\partial I _ {t}}{\partial r _ {t}} <   0\tag{4}
$$

Further consideration relates to long-term productivity. Defense spending may generate fewer positive spillovers than civilian public investment. A simple way to capture this is through technology dynamics,

$$
A _ {t + 1} = A _ {t} (1 + \gamma G _ {t} ^ {c} - \delta G _ {t} ^ {m})\tag{5}
$$

where $A_{t}$ denotes the technology level, $\gamma>0$ measures the growth enhancing effect of civilian investmen

[中间内容因长度限制已省略]

rt C. Kraay. 1998. “Consistent Covariance Matrix Estimation with Spatially Dependent Panel Data.” Review of Economics and Statistics 80 (4): 549–560.

Dunne, J. Paul, and Nan Tian. 2015. “Military Expenditure and Economic Growth: A Survey.” Economics of Peace and Security Journal 10 (1): 15–30.

Fatás, Antonio, and Ilian Mihov. 2001. “The Effects of Fiscal Policy on Consumption and Employment.” Journal of Political Economy 109 (4): 995–1015.

Ghassibe, Mishel and Francesco Zanetti. 2022. “State Dependence of Fiscal Multipliers: The Source of Fluctuations Matters,” Journal of Monetary Economics, 132(C), 1–23.

Granger, Clive W. J., and Timo Teräsvirta. 1993. Modelling Nonlinear Economic Relationships. Oxford: Oxford University Press.

Gupta, Sanjeev, Benedict Clements, Rina Bhattacharya, and Shamit Chakravarti. 2004. “Fiscal Consequences of Armed Conflict and Terrorism in Low- and Middle-Income Countries.” European Journal of Political Economy 20 (2): 403–421.

Heo, Uk, and Robert J. Eger. 2005. “Paying the Price for ‘Big Eyes’: Defense Spending and Economic Growth in East Asian Countries.” Journal of Asian Economics 16 (6): 737–754.

Herbst, Edward P., and Niels Johannesen. 2024. “Bias in Local Projections.” Journal of Econometrics 240: 105655.

Ilzetzki, Ethan, Enrique G. Mendoza, and Carlos A. Végh. 2013. “How Big (Small?) Are Fiscal Multipliers?” Journal of Monetary Economics 60 (2): 239–254.

IMF. 2014. Fiscal Multipliers: Size, Determinants, and Use in Macroeconomic Projections. Washington, DC: International Monetary Fund.

IMF. 2015. Fiscal Policy and Long-Term Growth. Washington, DC: International Monetary Fund.

IMF. 2021. World Economic Outlook. Washington, DC: International Monetary Fund.

IMF. 2026a. “Defense Spending: Macroeconomic Consequences and Trade-offs.” World Economic Outlook April 2026 Chapter 2. Washington, DC: International Monetary Fund.

IMF. 2026b. “The Macroeconomics of Conflicts and Recovery.” World Economic Outlook April 2026 Chapter 3. Washington, DC: International Monetary Fund.

Jordà, Óscar. 2005. “Estimation and Inference of Impulse Responses by Local Projections.” American Economic Review 95 (1): 161–182.

Jordà, Óscar, and Alan M. Taylor. 2016. “The Time for Austerity: Estimating the Average Treatment Effect of Fiscal Policy.” Economic Journal 126 (590): 219–255.

Knight, Malcolm, Norman Loayza, and Delano Villanueva. 1996. “The Peace Dividend: Military Spending Cuts and Economic Growth.” IMF Staff Papers 43 (1): 1–37.

Kollias, Christos, George Manolas, and Suzanna-Maria Paleologou. 2004. “Defense Spending and Economic Growth in the European Union.” Journal of Development Economics 74 (1): 211–231.

Miyamoto, Wataru, Minh Le, and Daniel R. Murphy. 2020. “Fiscal Stimulus and the Role of Public Investment.” Journal of International Economics 124: 103–116.

Pesaran, M. Hashem. 2015. “Testing Weak Cross-Sectional Dependence in Large Panels.” Econometric Reviews 34 (6–10): 1089–1117.

Pesaran, M. Hashem, and Ron Smith. 1995. “Estimating Long-run Relationships from Dynamic Heterogeneous Panels.” Journal of Econometrics 68 (1): 79–113.

Plagborg-Møller, Mikkel, and Christian Wolf. 2020. “Local Projections and VARs Estimate the Same Impulse Responses.” Econometrica 88 (2): 955–980.

Ramey, Valerie A. 2011. “Identifying Government Spending Shocks: It’s All in the Timing.” Quarterly Journal of Economics 126 (1): 1–50.

Ramey, Valerie A. 2019. “Ten Years after the Financial Crisis: What Have We Learned from the Renaissance in Fiscal Research?” Journal of Economic Perspectives 33 (2): 89–114.

Ramey, Valerie A., and Sarah Zubairy. 2018. “Government Spending Multipliers in Good Times and in Bad.” Journal of Political Economy 126 (2): 850–901.

Romer, Christina D., and David H. Romer. 2019. “Fiscal Space and the Aftermath of Financial Crises: How It Matters and Why.” Brookings Papers on Economic Activity 2019 (1): 239–331.

SIPRI. 2024. Trends in World Military Expenditure 2023. Stockholm: Stockholm International Peace Research Institute.

Smith, Ron. 1980. “Military Expenditure and Investment in OECD Countries, 1954–1973.” Journal of Comparative Economics 4 (1): 19–32.

Teulings, Coen, and Nick Zubanov. 2014. “Is Economic Recovery a Myth? Robust Estimation of Impulse Responses.” Journal of Applied Econometrics 29 (3): 497–514.

Warner, Andrew M. 2014. “Public Investment as an Engine of Growth.” IMF Working Paper No. 14/148.

Yildirim, Jülide, Nadir Özdemir, and Fuat Sezgin. 2005. “Military Expenditure and Economic Growth in Middle Eastern Countries: A Dynamic Panel Data Analysis.” Defence and Peace Economics 16 (4): 283–295.

## Bullets and Budgets Measuring Defense Spending Multipliers

This study shows that defense spending in emerging economies yields modest yet lasting boosts to output, while effects in advanced economies are more muted. The impact magnitudes depend on initial conditions across fiscal space, revenue capacity, financial development, institutional quality, and conflict exposure. Although defense spending can provide stimulus to growth, it should not be regarded as a blanket tool for macroeconomic stabilization. Resource allocation to infrastructure, health, or education could lead to larger and more inclusive long-term gains.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.
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
