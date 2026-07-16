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
![](images/ddc6b44969da36a002fc1800515a5bb8beef6b042990f2dc557e0f7833f0d188.jpg)

BIS Working Papers
No 1369

The evolving nexus: sovereigns, banks and NBFIs
Stefan Avdjiev, Bryan Hardy and Maximilian Jager

Monetary and Economic Department

July 2026

JEL classification: F34, G01, G21, G23, H63

Keywords: banks, sovereign default, feedback loop, NBFI, nexus, risk

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).

ISSN 1020-0959 (print)
ISSN 1682-7678 (online)

# The evolving nexus: sovereigns, banks and NBFIs

Stefan Avdjiev Bryan Hardy Maximilian Jager

This version: July 14, 2026\*

## Abstract

This paper documents that the traditional sovereign-bank nexus has morphed into a broader nexus that now also includes non-bank financial institutions (NBFIs): the sovereign-bank-NBFI nexus. The classical sovereign-bank nexus has been a major financial stability concern following the eurozone crisis. Since then, sovereign debt levels have increased substantially in many major economies, while NBFIs' footprint in sovereign bond markets has grown significantly. This paper examines the transmission of risks among banks, sovereigns and NBFIs using European bank-level data and global country-level data. We find that banks' direct sovereign exposures have recently become less important in explaining the co-movement between bank and sovereign risk. By contrast, banks' exposures to NBFIs have become a significant determinant of the bank-sovereign risk co-movement. We also find evidence that NBFIs' sovereign debt holdings have become important drivers of the co-movement between NBFI and sovereign risk.

JEL classification: F34, G01, G21, G23, H63

Keywords: banks, sovereign default, feedback loop, NBFI, nexus, risk

## 1 Introduction

The sovereign–bank nexus – often referred to as the sovereign-bank “doom loop” (Brunnermeier, Garicano, Lane, Pagano, Reis, Santos, Thesmar, Van Nieuwerburgh, and Vayanos, 2016; Gennaioli, Martin, and Rossi, 2014) – has been a major vulnerability in the global financial system. It gained particular notoriety during the euro area crisis, when banks’ holdings of sovereign debt exposed them to potential losses associated with sovereign distress, weakening their balance sheets and impairing their credit provision to the real economy. In turn, deteriorating bank health had a negative impact on the creditworthiness of sovereigns by increasing their contingent liabilities and by decreasing their tax revenues (due to the slowdown in economic activity caused by the associated reduction in banks’ supply of credit to the real economy). The above self-reinforcing mechanisms generated a two-way feedback loop in which stress could propagate from sovereigns to banks and vice versa.

Since the euro area crisis, the structure of the financial system has changed in ways that call for a reassessment of the sovereign-bank nexus. In particular, non-bank financial institutions (NBFIs) have grown substantially along several key dimensions – overall size, participation in sovereign debt markets, and interconnectedness with banks (Bank for International Settlements, 2025; Garcia Luna and Hardy, 2019; Aldasoro, Huang, and Kemp, 2020). These developments motivate the main hypothesis we examine in this paper: that the traditional sovereign–bank nexus has evolved into a broader sovereign–bank–NBFI nexus, in which NBFIs play an increasingly important role in the transmission of sovereign risk to banks. This paper tests this hypothesis by examining how the channels linking sovereigns and banks have changed over time, and by documenting the role of NBFIs in shaping these relationships.

The key mechanisms underlying the expansion of the nexus stem from the emergence of new frictions and feedback channels involving NBFIs. Many NBFIs, particularly hedge funds, engage in leveraged sovereign bond trading, often funded through short-term (repo)

borrowing from banks. This implies that even relatively small shocks to sovereign risk can have a large negative impact on NBFIs' balance sheets. In response, NBFIs may deleverage by engaging in fire sales of sovereign bonds and by withdrawing deposits from banks. Moreover, in such a stress scenario, there would be an additional negative impact on banks due to a rise in the expected losses associated with their direct exposures to NBFIs. All of this would have a negative impact on both banks and sovereigns, which would in turn have additional (second round) negative effects on NBFIs. This would give rise to a triangular propagation mechanism, in which shocks to any one of the three sectors – sovereigns, banks, or NBFIs – are transmitted to the other two, resulting in a negative feedback loop passing through all three nodes of the sovereign-bank-NBFI nexus.

We empirically test this hypothesis using both bank-level and aggregate (country-level) data. At the bank level, we use European Banking Authority (EBA) data to examine how the correlation between bank and sovereign CDS spreads is affected by banks' exposures to sovereigns and financial institutions. At the aggregate level, using the BIS international banking statistics, we examine the respective relationships at the national banking system level. In both (bank-level and country-level) sets of empirical exercises, we examine whether the relative importance of banks' exposures to sovereigns and the financial/NBFI sector has changed over time.

Our results suggest that the traditional sovereign–bank nexus has weakened (when considered in isolation). In the earlier part of our sample (prior to 2016), the co-movement between the CDS spreads of banks and sovereigns was higher for banks with greater holdings of risky sovereign debt (in line with the classical sovereign-bank nexus mechanisms). However, in the later part of our sample (post-2016), this relationship weakened significantly.

When we incorporate banks' exposures to the financial sector, particularly to NBFIs, we find a very different pattern. In the later period, greater exposure to financial counterparties located in high-risk sovereign jurisdictions is associated with a stronger correlation between bank and sovereign risk. This shift in the main drivers of the sovereign-bank risk co-movement – from banks’ direct sovereign exposures to their indirect exposures via the financial sector – is also documented in the results generated using aggregate data.

To isolate the underlying mechanism, we examine banks' foreign exposures. This allows us to abstract from the domestic bailout channel that may confound the drivers of the sovereign–bank CDS spread co-movement. The results from these international regressions confirm our main finding: the importance of banks' direct sovereign exposures has declined over time, while that of their financial sector exposures has increased. Moreover, we document that this shift is driven by the riskiness of the borrowing sovereign rather than by the nationality of the lending bank. For example, the main determinant of the CDS spread co-movement between core European banks and peripheral sovereigns switches from banks' direct sovereign exposures prior to 2016 to banks' exposures to the financial sector. In contrast, the co-movement between the CDS spreads of peripheral banks and core sovereigns is driven primarily by banks' exposures to financial institutions throughout the sample.

We also investigate the role of banks' asset and funding composition in amplifying these effects. The expanded (sovereign-bank-NBFI) nexus is more pronounced for banks holding more liquid assets. This is consistent with the hypothesis that banks that provide funding to certain NBFIs (such as hedge funds) through short-term repo lending are more exposed to sovereign risk through their exposures to NBFIs. In addition, banks' liability-side exposures (through deposits) to NBFIs independently contribute to higher co-movement between bank and sovereign risk, over and above the effects attributed to their asset-side exposures.

Finally, we examine the third side of the (sovereign-bank-NBFI) triangle by analyzing the direct relationship between NBFIs and sovereigns. Using aggregate data on NBFIs' holdings of sovereign debt, we find patterns consistent with our bank-level results. Namely, higher sovereign debt exposures of NBFIs are associated with stronger co-movement between NBFI and sovereign risk, especially in the later part of the sample.

Taken together, our findings provide strong evidence that the classical sovereign-bank nexus has evolved into a broader sovereign–bank–NBFI nexus. While banks' direct holdings of sovereign debt have become less central in explaining risk transmission between banks and sovereigns, the importance of banks' indirect exposures through NBFIs has grown. This shift is most pronounced for riskier sovereigns and likely reflects changes in regulation, market structure, and business models. More broadly, our results highlight the need to incorporate NBFIs and their triangular relationships into analyses of financial stability and sovereign risk transmission.

Literature Our paper is related to several strands of existing literature. More concretely, we build on existing work that has examined each of the three edges of the triangle linking sovereigns, banks, and NBFIs.

The sovereign-bank nexus has been explored both theoretically and empirically in a number of insightful papers. Much of this work focuses on the eurozone crisis, where both domestic and cross-border aspects of this nexus were on display (Brunnermeier et al., 2016; Fahri and Tirole, 2018; Acharya and Steffen, 2015; Bocola, 2016; Gennaioli et al., 2014; Acharya, Drechsler, and Schnabl, 2014). A few others examine these dynamics in the context of emerging markets, where sovereign risk and banking fragility are often more apparent and crises (sovereign, currency, banking) often come together (Baskaya, Hardy, Şebnem Kalemli-Özcan, and Yue, 2024; Brutti, 2011; Reinhart and Rogoff, 2011). Our paper’s key contribution to this discussion is expanding the view of the sovereign-bank nexus to account for the growing role of NBFIs, their particular risk sensitivities, and their feedback loops. We also highlight the particular vulnerability of (exposure to) riskier sovereigns for these dynamics.

A growing literature has highlighted the growth and financial stability risks of the NBFI sector and its links with banks. Many NBFIs are reliant on banks for their funding, even when they are competing with them in credit markets (Jiang, 2023; Acharya, Gopal, Jager, and Steffen, 2025). The links between banks and NBFIs run even deeper, as NBFIs also often provide funding to banks. These “interwoven” activities mean banks are exposed to credit and liquidity risks that may appear to have been shifted to the NBFI sector, likely generating the observed correlation in bank and NBFI abnormal equity returns (Acharya, Cetorelli, and Tuckman, 2024). $^{1}$ Our paper brings these risk links into the sovereign-bank nexus and documents how sovereign risk propagates through NBFIs to banks.

Lastly, a set of papers have documented the participation of NBFI investors in the sovereign debt market. Fang, Hardy, and Lewis (2025); Arslanalp and Tsuda (2014a,b) show that non-bank investors (mainly NBFIs) are large investors in terms of the share of sovereign debt that they hold. Fang et al. (2025) further highlights how NBFIs' holdings of sovereign debt are more price responsive than those of other investors, making their behavior (especially flightiness during stress) particularly important for the price of sovereign debt. As central banks wind down their balance sheets, non-bank investors have been the key players stepping in, thus increasing their market exposure and relevance in recent years (Du, Forbes, and Luzzetti, 2024; Eren, Schrimpf, and Xia, 2025). NBFIs also affect this market through their use of sovereign bonds in leveraged trading activities (e.g. the cash-futures basis trade (Barth and Kahn, 2025)). We connect the implications of these links and vulnerabilities back to the sovereign-bank nexus.

The above literature strands have examined each of the three edges of the sovereign-NBFI-bank triangle in isolation (i.e. focusing on only one of the three bilateral links at a time). In contrast, we examine all three edges of the sovereign-NBFI-bank triangle simultaneously and document how they influence each other in a feedback loop that is broader than the traditional sovereign-bank loop. This is our main contribution to the existing literature.

The remainder of this paper is structured as follows: Section 2 describes conceptually how the expanded sovereign-bank-NBFI nexus operates; Section 3 details the data used in our analysis; Section 4 describes our empirical approach; Section 5 presents the results examining different sides of the sovereign-bank-NBFI triangle; and Section 6 concludes.

## 2 The sovereign-bank-NBFI nexus

The sovereign-bank nexus used to have a two-way feedback loop at its core (Figure 1). For banks, this operated through their direct exposures to sovereign debt. A decline in the value of sovereign debt impaired their net worth and led to a cut in credit. For sovereigns, this worked through the risk that a systemic banking crisis would further weaken the economy and impair their creditworthiness, incentivizing them to (at least implicitly) provide support to banks during stress. Thus, both sovereigns and banks are directly impacted by each other's default risk, in addition to the general macroeconomic impacts of the individual failure of each.

Figure 1: The Classical Sovereign-Bank Loop  
![](images/48191ff9c144d6376a914fbd572cb180f759e71afd2b1aebb52179a880144d2c.jpg)  
Notes: Replicated from Brunnermeier et al. (2016).

Adding NBFIs into this nexus changes the dynamics (Figure 2). NBFIs have long been key intermediaries and investors in the sovereign debt market, particularly among advanced economies. Moreover, NBFIs' role in the global financial system has grown significantly over the past decade. There has been a substantial increase in both NBFIs' footprint in sovereign debt markets and their linkages with banks. NBFIs that directly hold sovereign debt are exposed to increases in sovereign risk or sovereign defaults. These vulnerabilities can be amplified when these intermediaries take leveraged positions with these investments. Sovereign debt is also increasingly used as collateral in financial transactions. A rise in sovereign risk lowers the value of sovereign bonds as an investment or as collateral, potentially inducing margin calls or fire sales.

Figure 2: The Sovereign-Bank-NBFI Triangle  
![](images/6a418b525f3856ae787da4542e7082585655081d9735e0f74bb1840a639a2def.jpg)  
Notes: Authors' elaboration.

The above shocks can be transmitted back to both sovereigns and banks. In the case of fire sales, this further depresses the value of sovereign debt, increases sovereigns' borrowing costs, reduces their fiscal space, and impairs their creditworthiness. When NBFIs face margin calls and incur losses on their sovereign bond holdings, they become riskier counterparties for banks. Furthermore, as NBFIs become more constrained, this could generate significant liquidity shocks for banks, as NBFIs are also key providers of funding to banks.

To give a more concrete example, the leveraged trading strategies that some NBFIs – and hedge funds in particular – deploy in sovereign bond markets could generate several of the above stress transmission channels (Hernández de Cos, 2025). These leveraged strategies are typically facilitated by NBFIs' short-term repo borrowing from banks. As a result, they are highly vulnerable to adverse shocks in funding markets. Thus, even a mildly negative shock in sovereign bond markets (triggered either by negative fiscal news or shifts in overall market sentiment) could be significantly amplified by the rapid unraveling of NBFIs' leveraged strategies. In turn, this would (i) transmit to banks via their direct lending exposures to NBFIs and (ii) likely lead to sharp spikes in government bond yields. The latter effect could then result in further unwinding of NBFIs' leveraged positions, thus triggering a new round in the three-way (sovereign-bank-NBFI risk) feedback loop. As a consequence, the impact of the initial shock in sovereign bond markets would be more negative for banks that are more exposed to NBFIs than for banks that are more directly exposed to the sovereign (since, in most cases, the volatility in sovereign bond yields would not translate into a sharp increase in the sovereign's probability of default).

In addition to the direct exposure channels described above, the three-way feedback loop could also be fueled via the indirect exposures that all three nodes of the sovereign-bank-NBFI nexus have to the real economy. More concretely, the spikes in government bond rates described above would likely translate into sharp increases in interest rates in the real economy (e.g. mortgages, consumer loans, business loans, corporate bond rates, etc). This would have a negative impact on economic activity, which would in turn be an additional adverse shock for sovereigns (due to lower tax revenues), as well as for banks and NBFIs (due to the deterioration in the creditworthiness of their real-economy borrowers).

Thus, through all of the above channels, sovereign stress can transmit risk to NBFIs, which can propagate that risk on to banks. In turn, stress in the NBFI sector can directly spill over to banks and have a direct impact on the pricing of sovereign debt (Fang et al., 2025). This naturally leads us to hypothesize that the classical sovereign-bank nexus has morphed into a broader sovereign-bank-NBFI nexus. In the rest of the paper, we test this hypothesis empirically along multiple dimensions.

## 3 Data

We examine the linkages among sovereigns, banks and NBFIs using bank-level data for European banks as well as country-level data for a global sample of banks.

The bank-level data are obtained from the EBA's stress test and transparency exercises. Between 2009 and 2011, the EBA conducted annual stress tests and published the results. In 2011, in response to growing worries 

[中间内容因长度限制已省略]

 the financial sector has crucial implications for financial stability. In this paper, we utilize European bank-level data and global country-level data to examine the transmission of risks among banks, sovereigns, and NBFIs. We document that, in recent years, the co-movement between bank and sovereign risk has become less dependent on banks' sovereign exposures and more dependent on banks' exposures to other financial institutions. We also find that the correlation between NBFI risk and sovereign risk has been increasingly driven by NBFIs' sovereign debt holdings. Taken together, our results suggest that the classical sovereign-bank nexus has evolved into a broader

sovereign-bank-NBFI nexus.

Our findings have important policy implications. The vulnerabilities associated with the expanded nexus could be addressed by deploying a carefully selected combination of tools in a targeted manner (Hernández de Cos (2025)). In terms of financial regulation and supervision, this includes limiting NBFI leverage, incentivizing greater use of central clearing and imposing minimum haircuts on repo borrowing. While implementing these policy measures could substantially reduce the risks associated with the expanded nexus between the sovereign and the financial sector, addressing those risks comprehensively would inevitably require ensuring sustainable fiscal trajectories.

Our paper provides scope for future research along several dimensions. New theoretical models will help to better understand the dynamics and quantify the strength and relevance of the various mechanisms underpinning this broader nexus. On the empirical side, there is scope for more granular analysis that distinguishes as much as possible among different types of NBFIs, while conditioning on the nature of their presence in sovereign bond markets. For example, analysis of fund-level data, especially those with levered trading strategies linked to sovereign bonds, could yield new insights into how and when stress amplification might arise.

## References

ACHARYA, V., I. DRECHSLER, AND P. SCHNABL (2014): “A pyrrhic victory? Bank bailouts and sovereign credit risk,” The Journal of Finance, 69, 2689–2739.

ACHARYA, V. V., N. CETORELLI, AND B. TUCKMAN (2024): “Where do banks end and NBFIs begin?” Tech. rep., National Bureau of Economic Research.

ACHARYA, V. V., M. GOPAL, M. JAGER, AND S. STEFFEN (2025): “Shadow always

touches the feet: implications of bank credit lines to non-bank financial intermediaries," Tech. rep., National Bureau of Economic Research.

ACHARYA, V. V. AND S. STEFFEN (2015): “The “greatest” carry trade ever? Understanding eurozone bank risks,” Journal of Financial Economics, 115, 215–236.

ALDASORO, I. N., W. HUANG, AND E. KEMP (2020): “Cross-border links between banks and non-bank financial institutions,” BIS Quarterly Review, September, 61–74.

ARSLANALP, S. AND T. TSUDA (2014a): “Tracking global demand for advanced economy sovereign debt,” IMF Economic Review, 62, 430–464.

(2014b): “Tracking global demand for emerging market sovereign debt,” IMF Working Paper, No. 14/39.

BANK FOR INTERNATIONAL SETTLEMENTS (2025): “Financial conditions in a changing global financial system,” Annual Economic Report, Chapter II, 47–76.

BARTH, D. AND R. J. KAHN (2025): “Hedge funds and the Treasury cash-futures basis trade,” Journal of Monetary Economics, 155.

BASKAYA, Y. S., B. HARDY, ŞEBNEM KALEMLI-ÖZCAN, AND V. YUE (2024): “Sovereign risk and bank lending: evidence from the 1999 Turkish earthquake,” Journal of International Economics, 150.

BOCOLA, L. (2016): “The pass-through of sovereign risk,” Journal of Political Economy, 124, 879–926.

BRUNNERMEIER, M., L. GARICANO, P. LANE, M. PAGANO, R. REIS, T. SANTOS, D. THESMAR, S. VAN NIEUWERBURGH, AND D. VAYANOS (2016): “The Sovereign-Bank Diabolic Loop and ESBies,” American Economic Review, 106, 508–512.

BRUTTI, F. (2011): “Sovereign defaults and liquidity crises,” Journal of International Economics, 84, 65–72.

CETORELLI, N., M. LANDONI, AND L. LU (2023): “Non-bank financial institutions and banks’ fire-sale vulnerabilities,” FRB of Boston Supervisory Research & Analysis Unit Working Paper No. SRA, 23–01.

Du, W., K. FORBES, AND M. LUZZETTI (2024): “Quantitative Tightening Around the Globe: What Have We Learned?” NBER Working Paper, No 32321.

EREN, E., A. SCHRIMPF, AND F. D. XIA (2025): “The demand for government debt,” BIS Working Papers, No 1105.

FAHRI, E. AND J. TIROLE (2018): “Deadly Embrace: Sovereign and Financial Balance Sheets Doom Loops,” Review of Economic Studies, 85, 1781–1823.

FANG, X., B. HARDY, AND K. K. LEWIS (2025): “Who holds sovereign debt and why it matters,” Review of Financial Studies, 38, 2326–2361.

GARCIA LUNA, P. AND B. HARDY (2019): “Non-bank counterparties in international banking,” BIS Quarterly Review, September, 15–31.

GENNAIOLI, N., A. MARTIN, AND S. ROSSI (2014): “Sovereign Default, Domestic Banks, and Financial Institutions,” Journal of Finance, 69, 819–866.

HARDY, B. AND S. ZHU (2023): “Covid, central banks and the bank-sovereign nexus,” BIS Quarterly Review, March, 15–31.

HERNÁNDEZ DE COS, P. (2025): “Fiscal threats in a changing global financial system,” Lecture at the London School of Economics, 27 Nov.

JIANG, E. X. (2023): “Financing competitors: Shadow banks’ funding and mortgage market competition,” The Review of Financial Studies, 36, 3861–3905.

ONGENA, S., A. POPOV, AND N. VAN HOREN (2019): “The invisible hand of the government: Moral suasion during the European sovereign debt crisis,” American Economic Journal: Macroeconomics, 11, 346–379.

REINHART, C. AND K. ROGOFF (2011): “From financial crash to debt crisis,” American Economic Review, 101, 1676–1706.
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
