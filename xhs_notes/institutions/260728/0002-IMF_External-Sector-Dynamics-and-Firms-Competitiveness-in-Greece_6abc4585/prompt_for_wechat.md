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
# External Sector Dynamics and Firms' Competitiveness in Greece

Tomohide Mineyama

SIP/2026/071

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on April 30, 2026. This paper is also published separately as IMF Country Report No 26/109.

2026
JUL

![](images/d1636c7704ed2eec3d22eadc0d5a537a147d182e73c893a9f21d5d23ca6c1fee.jpg)

# IMF Selected Issues Paper European Department External Sector Dynamics and Firms' Competitiveness in Greece Prepared by Tomohide Mineyama\*

Authorized for distribution by Joong Shik Kang
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on April 30, 2026. This paper is also published separately as IMF Country Report No 26/109.

ABSTRACT: Greece's external sector has undergone significant transformation over the past decades. Precrisis imbalances—including large fiscal deficits, household overinvestment, and elevated labor costs—have largely been corrected. Nevertheless, the current account deficit remains sizable, reflecting persistent challenges such as subdued private saving, low value added in exporting sectors, and high external debt. Advancing supply-side reforms would help strengthen international competitiveness and raise productivity, supporting higher domestic value-added and saving. Maintaining prudent fiscal policy remains essential to further reduce external debt.

RECOMMENDED CITATION: Tomohide Mineyama. External Sector Dynamics and Firms' Competitiveness in Greece. IMF Selected Issues Paper (SIP2026/071). Washington DC. International Monetary Fund.

<table><tr><td>JEL Classification Numbers:</td><td>F32, F41, D24</td></tr><tr><td>Keywords:</td><td>External Balance, Savings, Trade, Competitiveness, Structural Reforms</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>tmineyama@imf.org</td></tr></table>

SELECTED ISSUES PAPERS

# External Sector Dynamics and Firms' Competitiveness in Greece

Greece

Prepared by Tomohide Mineyama $^{1}$

## GREECE

SELECTED ISSUES

April 30, 2026

Approved By

Prepared By Tomohide Mineyama (EUR).

European Department

## CONTENTS

EXTERNAL SECTOR DYNAMICS AND FIRMS' COMPETITIVENESS IN GREECE 2
A. Motivation 2
B. Shifting Sectoral Saving-Investment Balances 3
C. Persistent Domestic Production Gaps 5
D. Cyclical Implications of Structural Challenges 9
E. Structural Reforms and Export Competitiveness 11
F. Policy Recommendations 12

## BOX

1. External Financial Flows and Debt Service Burdens 5

## FIGURES

1. Current Account Balance 2  
2. Sectorial SI Balance 3  
3. Sectoral Gross Saving and Investment 3  
4. Drivers of Household and NFC Savings 4  
5. Decomposition of Current Account and Trade Balances 6  
6. Exports and Cost Competitiveness 7  
7. Characteristics of Export Sectors 8  
8. Cost and Non-Cost Competitiveness 9  
9. Estimated Impacts of Recent Developments on CA Balance 10  
10. Structural Impediments and Firms' Performance 12

## APPENDICES

I. Input-Output Analysis 14

II. World Bank Enterprise Survey 16

References 19

# EXTERNAL SECTOR DYNAMICS AND FIRMS' COMPETITIVENESS IN GREECE $^{1}$

Greece's external sector has undergone significant transformation over the past decades. Pre-crisis imbalances—including large fiscal deficits, household overinvestment, and elevated labor costs—have largely been corrected. Nevertheless, the current account deficit remains sizable, reflecting persistent challenges such as subdued private saving, low value added in exporting sectors, and high external debt. Advancing supply-side reforms would help strengthen international competitiveness and raise productivity, supporting higher domestic value-added and saving. Maintaining prudent fiscal policy remains essential to further reduce external debt.

## A. Motivation

1. Greece's current account (CA) deficit has widened in recent years, reversing much of the post-crisis adjustment. While the sovereign debt crisis was marked by large external imbalances, which narrowed substantially during the subsequent adjustment period, the CA deficit

widened again after the pandemic (Figure 1). The deterioration initially reflected the collapse of tourism followed by the impact of higher energy prices and rising interest rates after Russia's war in Ukraine. Although these pressures have partly eased, the CA deficit remains elevated, driven by strong goods imports associated with robust domestic demand, including NGEU-financed investment. As a result, Greece records the second largest CA deficit in the euro area and the largest negative net international investment position (NIIP).

![](images/92f5a8562fc68f7c79173b76c4ef7a85bf35c296329db3ce289958ed83fb46c9.jpg)

2. This paper examines recent CA dynamics from both cyclical and structural perspectives, highlighting post-crisis improvements alongside remaining challenges. Section B examines the CA dynamics from the saving-investment balance perspectives to understand shifts in sectoral contributions after the crisis. Section C discusses remaining challenges in exporting sectors and competitiveness on the production side of the economy. Section D examines the implications of these challenges for recent CA developments and Section E presents an empirical analysis of the

relationship between structural impediments and firms' competitiveness. Section F concludes with policy implications.

## B. Shifting Sectoral Saving-Investment Balances

3. The recent CA deficit is driven primarily by private sector's saving-investment (SI) imbalance, in contrast to the pre-crisis period when deficits were largely public sector driven.

Before the crisis, external imbalances reflected negative general government (GG) net saving, stemming from expansionary fiscal policies and weak tax collection, alongside household overinvestment associated with the housing boom (Figure 2). Over time, substantial fiscal consolidation has shifted the GG SI balance into surplus, aside from temporary pandemic-related support measures. Despite elevated public external debt, debt service costs remain contained due to a large share of official debt with low interest rates and ultra-long maturities (Box 1). In contrast, the recent CA deficit is largely driven by the private

![](images/6a03ba43853e02b1b20a7e60b8f808f885469dffb60a917bc33535cd2ce9b7bc.jpg)

sector, with non-financial corporates' (NFCs') SI balance turning to negative, while households' saving remaining subdued.

4. Private gross saving remains insufficient to finance rising investment. The recent widening of the private sector's SI deficit has been driven mainly by higher NFCs' investment (Figure 3), reflecting the implementation of NGEU projects, pent-up investment needs following years of post-crisis underinvestment, and growing needs related to ICT and energy security. However, domestic saving has not kept pace. Household saving remains low—aside from a temporary post-

Figure 3. Sectoral Gross Saving and Investment  
![](images/df695683810d407d690fac034781632ea64d93901e7b2ad2a59ce6b09b26a746.jpg)  
Sources: Eurostat and IMF staff calculations.

![](images/0daaf7c61f64bbad93e993e902d29f7f0604b1b4b0baa4aed93b9c8f680dc781.jpg)

![](images/ac40dfae9be6925ac04ad0651da8aaf3b3c521df6d2ff9cbb18438f801396701.jpg)

2002 2004 2006 2008 2010 2012 2014 2016 2018 2020 2022 2024
Note: NPISH and GOS stand for "non-profit institutions serving households" and "gross operating surplus," respectively.
Sources: Eurostat and IMF staff calculations.

pandemic increase—despite strong economic growth (Figure 4). $^{2}$ Real wage growth has been limited, consistent with weak labor productivity growth (reflected in “compensation of employees” for employed workers and “gross operating surplus and mixed income” for self-employed workers). High living costs for essentials such as housing, energy, and food further constrain households’ saving capacity. Fiscal consolidation, including lower net social benefits and higher tax burdens, has further weighed on household disposable income. At the same time, NFCs’ gross value-added creation has stagnated, reflecting low productivity growth and high intermediate input costs. Going forward, it is essential that the current investment cycle translates into sustained gains in value-added production, supporting higher corporate surpluses and household incomes—key elements of durable saving.

Figure 4. Drivers of Household and NFC Savings  
![](images/b4a0056736650802b4fecdebbbaf75f1244b20bf26c02ad0a69cd586c216d743.jpg)

![](images/171ab62f5fd57fd56813bad92f71e4e0335842694bf876f66a8dfa5d35cb57fd.jpg)

Box 1. External Financial Flows and Debt Service Burdens

Despite high external debt, debt service burdens remain contained. The net international investment position (NIIP), in percent of GDP, continued to increase after the crisis, reflecting elevated external financing needs and the sharp contraction in nominal GDP. However, as the bulk of external debt consists of low-interest official loans with very long maturities and extended grace periods, debt service obligations have remained manageable (see figures below).

The negative NIIP, albeit still elevated, has been on a sustained improving trend in recent years. External financing was initially dominated by official flows in the aftermath of the crisis, but normalized as market access was restored. At the same time, FDI inflows strengthened, reflecting the privatization program and improved investor confidence. Thanks to contained financing need supported by substantial fiscal consolidation and strong nominal GDP growth, the NIIP began to improve after the pandemic.

![](images/aa6aa6d275e286da890246cfe92d4e684f6834ad598c63857ba87aa1e136448d.jpg)

![](images/255473c7a65ab2779db67c161fabb28f239c7bdaccc8de0e6bfd488c9e34fad2.jpg)  
Financial Account Balance (Percent of GDP)

![](images/5eda6c256a41d3bf3f11c07878c64ca50e7906f86b6e1c8a021f8f20980c6556.jpg)

![](images/00b238431a7e7515eddfe5c26483147cd494c05687365e80219c2a95ffa184e5.jpg)

## C. Persistent Domestic Production Gaps

5. The weak private sector SI balance reflects a persistent trade deficit. While Greece generates substantial net services exports, mainly from tourism and shipping, it remains heavily reliant on goods imports across consumption, intermediate, and capital goods, underscoring a limited domestic production base (Figure 5). Despite the recent expansion of renewable energy production, such as solar and wind, the energy balance remains in deficit. The trade balance has averaged a deficit of 5.7 percent of GDP since 2000, as a large goods deficit of 13.7 percent more than offset a service surplus of 8.0 percent, accounting for most of the CA deficit (6.8 percent of GDP).

Figure 5. Decomposition of Current Account and Trade Balances  
![](images/082dd028286ca8808fd9aeb99a32e06dc44c1e0293da6b71ddf0d0cc58ca1ab8.jpg)

![](images/ccfc793fd1e494a6f6ce7c506924c84213e488bfd636183f10a8bfc7bd59ce0e.jpg)

6. Exports have expanded markedly across a broad range of sectors over the past decades. Despite the large trade deficit, the exports-to-GDP ratio has almost doubled since the early 2000s, reaching about 40 percent of GDP in 2025—close to the euro area average of 49 percent (Figure 6). This increase reflects broad-based growth both in goods and services. Goods exports have been driven by traditional sectors, such as (i) refined petroleum products that capitalize on Greece's geographic position by importing crude oil from the Middle East and North Africa and exporting refined products to the rest of Europe, and (ii) food, beverages, and agricultural products, supported by well-established Greek brands. At the same time, (iii) pharmaceuticals and cosmetic products, and (iv) medical devices have emerged as dynamic export sectors, with rising market shares in the EU.

7. Export growth has been underpinned by improved cost competitiveness. The unit labor cost (ULC)-based real effective exchange rate (REER), which measures production costs relative to trading partners, depreciated by more than 30 percent from its peak in 2011Q3 (Figure 6). This was achieved largely through wage adjustments enabled labor market reforms that increased flexibility and facilitated internal devaluation during the adjustment period. This adjustment reversed the pre-crisis overvaluation driven by rapid wage growth and helped restore cost competitiveness across both goods and services, supporting export performance.

## Figure 6. Exports and Cost Competitiveness

Export of Goods and Services (Percent of GDP)

![](images/e05958cf8625daa2895601e4a5cfb3529efcbb3f77494d81ff2c07f4852e6b22.jpg)  
Goods Exports by Product (Percent of GDP)

![](images/bd5a73a121ec9f0f35caa3516f9295897423d7434e8edd31a368a2d7d6894717.jpg)  
Export Share in EU (Percent)

![](images/381d00f196acb9b2461d55954dea2d16fc94895cfa0237737b55a4ebd1882dd6.jpg)  
Real Effective Exchange Rate

![](images/300f0b767b0e7d10b1d5f5b87420edb3822b1466c9179a9786474c67a011950a.jpg)

8. However, exports remain concentrated in relatively low value-added sectors, limiting their contribution to net exports. Despite the strong export growth, diversification remains limited, with goods exports dominated by refined petroleum and agricultural and food products, and services exports largely driven by tourism. This concentration is evident in the economic complexity index and revealed comparative advantage measures (Figure 7). While export expansion has supported domestic activity and employment, an analysis based on sectoral input–output linkages indicates that the domestic value-added multiplier of exports is relatively low—about 0.43 on average—implying that €1 of exports generates only about €0.43 in domestic value added or GDP, with substantial import leakages (see Appendix I for technical details). Large sectors—including refined petroleum, metals, and food products—remain locked into lower value-added activities. Moreover, although some higher-technology sectors—including pharmaceuticals and electronic and optical equipment (such as medical devices)—have recorded rapid export growth, their contribution to domestic value added has so far been limited. As a result, export expansion has had only a modest impact on improving the trade balance.

## Figure 7. Characteristics of Export Sectors

Economic Complexity Index of Exports

![](images/90791e355d8c739520464ccb6d63ffe652a806eb6c271afea140ef8c42bb5006.jpg)  
Sources: Hausmann et al. (2013), and IMF staff calculations.
Note: The Economic Complexity Index (Hausmann et al., 2013) measures the amount of productive knowledge in exports. It is a function of a country's Export diversity (number of products exported) and uniqueness (number of countries exporting a product) in a relative sense. Black diamonds are averages for 1995-1999; blue bars are averages for 2018-23.

![](images/27c673d69452719f28bd62cfab97ae0340ef39dc4bbe1e4287af3883e88cdcb1.jpg)  
Notes: The RCA measures a country's export shares relative to the world export shares. Dots are goods at the SITC 3-digit level.
Source: UNCTAD.  
Employment and Export Growth (x-axis: export growth from 2010 to 2020 in percent, y-axis: employment growth from 2010 to 2020 in percent)

![](images/13f7f15270e406aa513b99df63233f6646bb711a79f50bc19f389eda62c5ef3c.jpg)  
Notes: The size of bubbles represents export values in 2020. Sources: ELSTAT, EU KLEMS, and IMF staff calculations.  
Value Added Multiplier and Export Growth (x-axis: export growth from 2010 to 2020 in percent, y-axis: value added multiplier in percent)

![](images/ff6d2f40e151416565f689c5c4b30e763de14e27fea1911a3bf0979f9c1cdf0e.jpg)  
Notes: The size of bubbles represents export values in 2020. Sources: ELSTAT, EU KLEMS, and IMF staff calculations.

9. Despite gains in cost competitiveness, improvements in underlying productivity have been sluggish. The large post-crisis depreciation of the ULC-based REER was mainly driven by real wage compression, while labor productivity contributed little and at times even exerted upward pressure on ULCs before a recent partial improvement (Figure 8). Real wage adjustment was further dampened by slow price adjustment, reflecting persistent product-market frictions and high non-wage costs, including regulatory and administrative burdens and energy costs. As a result, notwithstanding some recent progress, Greece continues to perform poorly across several structural indicators, and adjustments of the CPI-based REER were much more contained than the ULC-based rate (Figure 6).

Figure 8. Cost and Non-Cost Competitiveness  
![](images/73c03f0040881a7159d2d1ec5f035a3b3412b7b693958f3920017b7f29823e37.jpg)

![](images/ec324fa15aad2eb927a9f240559381cd1f6c363738d4f6f623346a56d0c12710.jpg)

## D. Cyclical Implications of Structural Challenges

10. Structural weaknesses have amplified the recent widening of the CA deficit. Subdued private saving and limited domestic value-added activities, underpinned by sluggish productivity growth, have remained persistent structural constraints. This section aims to quantify how much these structural challenges contribute to the recent widening of the CA deficit, in the context of strong domestic demand-driven growth and volatile global commodity prices and interest rates. Specifically, low household saving implies hand-to-mouth consumption behavior, with income gains translating quickly into consumption rather than saving. At the same time, stagnant value-added creation by NFCs, combined with rising investment, has resulted in a negative SI balance. On the production side, insufficient domestic production capacity—exacerbated by weak productivity growth—has constrained the economy's ability to meet rising domestic demand and leads to higher imports. Moreover, the disparity between a goods trade deficit and a services trade surplus has heightened the sensitivity of the CA balance to relative price movements, especially global commodity price fluctuations. Similarly, a highly negative NIIP has amplified exposure to interest rate movements through higher primary income payments.

11. Parsimonious simulations are conducted to quantify the impacts of key recent domestic and external dynamics. The analysis below focuses on estimating the contribution of domestic demand growth and global commodity price and interest rate fluctuations, based on a set of assumptions:

\- Domestic demand. Imports associated with domestic demand are estimated by applying import multipliers—derived 

[中间内容因长度限制已省略]

wspan="2">Age squared</td><td>0.001***</td><td>0.001***</td><td>0.001***</td><td>0.001***</td><td>0.001***</td><td>-0.010</td><td>-0.007</td><td>-0.008</td><td>-0.013</td></tr><tr><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.026)</td><td>(0.026)</td><td>(0.024)</td><td>(0.024)</td></tr><tr><td>N of obs.</td><td>9,991</td><td>10,162</td><td>11,035</td><td>10,968</td><td>9,300</td><td>4,426</td><td>4,565</td><td>4,925</td><td>4,898</td></tr><tr><td>R-squared</td><td>0.086</td><td>0.085</td><td>0.084</td><td>0.093</td><td>0.107</td><td>0.087</td><td>0.072</td><td>0.072</td><td>0.095</td></tr><tr><td colspan="10">(B) Export Participation</td></tr><tr><td rowspan="2">Dependent variable: Sample:</td><td rowspan="2"></td><td rowspan="2">All firms</td><td colspan="7">Exporter (1 or 0)</td></tr><tr><td></td><td></td><td></td><td colspan="4">Young firms</td></tr><tr><td colspan="10">Obstacles for businesses (1 or 0)</td></tr><tr><td rowspan="2">Regulation and admin burden</td><td>-0.312***</td><td></td><td></td><td>-0.328***</td><td>-0.397***</td><td></td><td></td><td></td><td>-0.433***</td></tr><tr><td>(0.080)</td><td></td><td></td><td>(0.091)</td><td>(0.138)</td><td></td><td></td><td></td><td>(0.145)</td></tr><tr><td rowspan="2">Competition with informal sector</td><td></td><td>-0.185***</td><td></td><td>-0.155**</td><td></td><td>-0.264***</td><td></td><td></td><td>-0.233***</td></tr><tr><td></td><td>(0.060)</td><td></td><td>(0.062)</td><td></td><td>(0.077)</td><td></td><td></td><td>(0.073)</td></tr><tr><td rowspan="2">Educated workforce</td><td></td><td></td><td>-0.023</td><td>-0.013</td><td></td><td></td><td>0.014</td><td></td><td>0.011</td></tr><tr><td></td><td></td><td>(0.046)</td><td>(0.054)</td><td></td><td></td><td>(0.056)</td><td></td><td>(0.064)</td></tr><tr><td rowspan="2">Access to finance</td><td></td><td></td><td></td><td>0.018</td><td>0.063</td><td></td><td></td><td></td><td>0.053</td></tr><tr><td></td><td></td><td></td><td>(0.047)</td><td>(0.049)</td><td></td><td></td><td></td><td>(0.057)</td></tr><tr><td colspan="10">Controls</td></tr><tr><td rowspan="2">Ln(TFP)</td><td>-0.044***</td><td>-0.046***</td><td>-0.049***</td><td>-0.048***</td><td>-0.044***</td><td>-0.048***</td><td>-0.046***</td><td>-0.051***</td><td>-0.052***</td></tr><tr><td>(0.013)</td><td>(0.013)</td><td>(0.013)</td><td>(0.013)</td><td>(0.013)</td><td>(0.013)</td><td>(0.015)</td><td>(0.015)</td><td>(0.014)</td></tr><tr><td rowspan="2">Foreign ownership</td><td>0.630***</td><td>0.632***</td><td>0.612***</td><td>0.609***</td><td>0.634***</td><td>0.681***</td><td>0.633***</td><td>0.641***</td><td>0.630***</td></tr><tr><td>(0.046)</td><td>(0.048)</td><td>(0.046)</td><td>(0.046)</td><td>(0.050)</td><td>(0.061)</td><td>(0.063)</td><td>(0.064)</td><td>(0.063)</td></tr><tr><td rowspan="2">Ln(Employment)</td><td>0.368***</td><td>0.372***</td><td>0.370***</td><td>0.370***</td><td>0.374***</td><td>0.336***</td><td>0.348***</td><td>0.341***</td><td>0.340***</td></tr><tr><td>(0.019)</td><td>(0.018)</td><td>(0.018)</td><td>(0.018)</td><td>(0.019)</td><td>(0.022)</td><td>(0.023)</td><td>(0.022)</td><td>(0.022)</td></tr><tr><td rowspan="2">Age</td><td>0.006***</td><td>0.006***</td><td>0.006***</td><td>0.006***</td><td>0.006***</td><td>0.018</td><td>0.011</td><td>0.018</td><td>0.017</td></tr><tr><td>(0.001)</td><td>(0.002)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.018)</td><td>(0.016)</td><td>(0.017)</td><td>(0.017)</td></tr><tr><td rowspan="2">Age squared</td><td>-0.000***</td><td>-0.000***</td><td>-0.000***</td><td>-0.000***</td><td>-0.000***</td><td>-0.000</td><td>-0.000</td><td>-0.000</td><td>-0.000</td></tr><tr><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td></tr><tr><td>N of obs.</td><td>10,233</td><td>9,966</td><td>10,776</td><td>10,702</td><td>9,527</td><td>4,605</td><td>4,527</td><td>4,859</td><td>4,830</td></tr></table>

## References

Backinezos, Constantina, Stelios Panagiotou, and Christos Papazoglou (2020), "The Current Account Adjustment in Greece during the Crisis: Cyclical or Structural?," Economic Bulletin 51, pp. 73-90, Bank of Greece, July 2020.

Backinezos, Constantina, Stelios Panagiotou, and Evangelia Vourvachaki (2020), "Multiplier Effects by Sector: An Input-Output Analysis of the Greek Economy," Economic Bulletin 52, pp. 7-27, Bank of Greece, December 2020.

Bank of Greece (2026), "Annual Report 2025."

Baqaee, David Rezza and Emmanuel Farhi (2024), "Networks, Barriers, and Trade," Econometrica, 92(2), pp. 505–541.

Bartolini, David, Mengxue Wang, and Zeju Zhu (forthcoming), "Firm-Level Productivity in CESEE Countries," IMF Working Paper.

Beck Thorsten, Asli Demirgüc-Kunt, and Vojislav Maksimovic (2005), "Financial and Legal Constraints to Growth: Does Firm Size Matter?" Journal of Finance 60(1), pp. 137–177.

Francis, David C., Nona Karalashvili, Hibret Maemir, and Jorge Rodriguez Meza (2020), "Measuring Total Factor Productivity Using the Enterprise Surveys: A Methodological Note," World Bank Policy Research Working Paper 9491, December 2020.

Hjort and Poulsen (2019), "The Arrival of Fast Internet and Employment in Africa," American Economic Review 109(3), pp. 1032–1079.

Klapper, Leora, Luc Laevena, and Raghuram Rajan (2006), "Entry Regulation as a Barrier to Entrepreneurship," Journal of Financial Economics 82, pp. 591–629.

Ospina, Sandra and Marc Schiffbauer (2010), “Competition and Firm Productivity: Evidence from Firm-Level Data,” IMF Working Paper WP/10/67.

Reinikka and Svensson (2002), "Coping with poor public capital," Journal of Development Economics 69, pp. 51–69.
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
