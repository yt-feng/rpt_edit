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
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
BUSINESS CLIMATE,
ECONOMIC COMPLEXITY,
AND PERFORMANCE AT THE
PROVINCIAL LEVEL IN VIET NAM

Ari Kokko, Nguyen Tien Thong, and Katariina Nilsson Hakkala

NO. 856

July 2026

ADB ECONOMICS

WORKING PAPER SERIES

# Business Climate, Economic Complexity, and Performance at the Provincial Level in Viet Nam

Ari Kokko, Nguyen Tien Thong, and Katariina Nilsson Hakkala

No. 856 | July 2026

The ADB Economics Working Paper Series presents research in progress to elicit comments and encourage debate on development issues in Asia and the Pacific. The views expressed are those of the authors and do not necessarily reflect the views and policies of ADB or its Board of Governors or the governments they represent.

Ari Kokko (ako.egb@cbs.dk) is a professor at the Department of International Economics, Government and Business, Copenhagen Business School. Nguyen Tien Thong (thongtiennguyen@gmail.com) is a lecturer in business economics at Nha Trang University. Katariina Nilsson Hakkala (knilssonhakkala@adb.org) is a senior economist at the Economic Research and Development Impact Department, Asian Development Bank.

© 2026 Asian Development Bank
6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines
Tel +63 2 8632 4444; Fax +63 2 8636 2444
www.adb.org

Some rights reserved. Published in 2026.

ISSN 2313-6537 (print), 2313-6545 (PDF)
Publication Stock No. WPS260325-2
DOI: http://dx.doi.org/10.22617/WPS260325-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed to another source, please contact the copyright owner or publisher of that source for permission to reproduce it. ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use the ADB logo.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

## Notes:

In this publication, “\$” refers to United States dollars.
ADB recognizes “China” as the People’s Republic of China, “Vietnam” as Viet Nam, and “Hanoi” as Ha Noi.

## ABSTRACT

This study explores the impact of subnational institutions on Viet Nam's provincial manufacturing sector, comparing foreign-invested and domestic firms using a two-step difference GMM model with data from 63 provinces (2006–2020). Results show that changes in subnational institutions, measured by the Provincial Competitiveness Index, have little effect on economic complexity, revenues, employment, productivity, or firm size. Unexpectedly, weaker governance in areas like land access, transparency and legal institutions sometimes leads to better performance. This weak connection persists across all samples, periods, controls, and estimation methods, likely due to the dominance of foreign-invested companies and their limited interaction with local firms, which impacts overall firm development.

Keywords: FDI, provincial competitiveness index, business climate, economic complexity, manufacturing performance

JEL codes: F63, L53, O12, O25

## 1. INTRODUCTION

This paper examines how local institutions and policies—proxied by the Provincial Competitiveness Index (PCI)—influence the development and performance of foreign-invested enterprises and domestic firms in Viet Nam's manufacturing sector. Institutions and policies nationally and provincially have to some extent been designed to attract inflows of foreign direct investment (FDI), and earlier research has confirmed that the local business environment is one of the determinants of FDI inflows in Vietnamese provinces (Meyer and Nguyen 2005, Doan and Lin 2016; Esiyok and Ugur 2017; Do, Nguyen, and Thanh 2025). Provinces with higher PCI scores tend to receive more FDI.

It has also been shown that the local business environment is partly shaped by active lobbying from foreign-invested enterprises (Malesky 2004, 2008). However, although foreign-invested enterprises that have already entered the host country have primarily carried out the lobbying of local decisionmakers, not much is known about how incumbent foreign-invested enterprises respond to institutional and policy reforms provincially. Both the general debate and the academic literature on FDI and host country institutions have instead assumed that “good” institutions will not only attract FDI, but also ensure that the foreign-invested enterprises are competitive, generate more jobs (and tax revenue) over time, and upgrade their activities from simple assembly to more complex activities with higher value added. Empirical evidence on whether this assumption is correct is scarce: earlier research has rarely examined how the operations of foreign-invested enterprises—rather than their entry decisions—are influenced by the local business environment. This research gap motivates the question “Do subnational institutions, proxied by the PCI, explain differences across provinces in the performance of foreign-invested enterprises?”

A closely connected research question is related to how local firms are influenced by institutions and policies that are partly designed to attract FDI and also influenced by lobbying from foreign-invested enterprises with strong connections to policymakers (Malesky 2008, 2009). This is particularly relevant for the case of Viet Nam, where observers have complained that policies seem to focus more on attracting FDI inflows than supporting the development of the domestic private sector and their opportunities to benefit from FDI inflows (Kokko, Nestor, and Le 2023). Viet Nam's domestic private sector is relatively weak, although the number of private firms has grown rapidly over the past decades. The domestic private sector's share of formal sector employment and revenues was about $30\%$ in the year 2000, peaked at $50\%$ around 2010, but fell back to $40\%$ in 2020. The average number of employees in private domestic manufacturing firms fell from 54 to 32 over the same period. Simultaneously, foreign-invested enterprises increased their shares of employment and revenue from about 10% in 2000 to 20% in 2010 and 30% in 2020, and account now for the bulk of manufacturing output in modern sectors, such as electronics machinery, and motor vehicles (Thong, Kokko, and Hakkala 2025). Hence, given the strong emphasis on FDI attraction in Vietnamese provincial policy and the potential bias in institutions and policies in favor of foreign-invested enterprises, it is unclear how domestic firms are affected by the local business environment. Are cross-provincial differences in growth and upgrading in domestic firms explained by the same institutional variables that supposedly influence the behavior of foreign-invested enterprises?

To answer these research questions, we have constructed a panel data set for 2006–2020 including information on the provincial business environment and the operations of foreign-owned and domestic manufacturing firms across Viet Nam's 63 provinces, as defined before the administrative reform in 2025 which reduced them to 28 provinces and 6 cities. The data is available at the industry, province, and ownership group level. Hence, we know how the foreign-invested enterprises in specific provinces and industries developed, but not how the performance of individual firms changed over time. The development of foreign-invested enterprises and local firms is proxied by several alternative dependent variables based on aggregated data from annual enterprises censuses carried out by the National Statistics Office.

Our analysis used economic complexity as a measure of firm performance. The economic complexity indicators are calculated separately for foreign-invested enterprises and domestic firms and aggregated to the provincial level. They are based on four-digit product complexity scores provided by Harvard's Growth Lab, which have been transposed to the three-digit industry classifications used in Viet Nam. The value for an industry's Economic Complexity Index (ECI) is the average product complexity score for the products manufactured by that industry. A province's economic complexity score is the revenue-weighted average economic complexity score of the manufacturing industries represented in the province. The other dependent variables in our analysis are the average revenue, employment, productivity, and firm size of the relevant firm groups. The core explanatory variables are based on Viet Nam's Provincial Competitiveness Index (PCI), which has been collected since 2005. In addition to the aggregate PCI score, we use 10 of its subindices measuring specific dimensions of the province's business environment and economic governance. To avoid problems caused by changes in methodology and survey questions, we focus on time-consistent variables that highlight changes in provincial institutional quality over time (Malesky, Pham, and Phan 2025).

Using a two-step Difference GMM panel data model, we find notable differences between the effects of provincial institutions on foreign-invested enterprises and domestic firms. In our estimations for foreign-invested enterprises, there are few significant coefficients, and no clear indications that institutional reforms and stronger local business environments explain differences in economic performance across provinces. Differences in the growth patterns across provinces for domestic firms are also weakly connected to the subnational institutional characteristics proxied by the PCI and its sub-indexes. The same holds for the sub-set of private domestic firms (i.e., excluding firms with state or collective ownership): few of the proxies for provincial institutions record significant coefficients in our GMM estimations, and even fewer have the expected effects—in fact, several estimations indicate that private employment growth is faster in provinces where improvements in transparency and legal institutions are slower.

Our interpretation of the results is that many of the operational decisions in foreign-invested enterprises are made with reference to events outside the Vietnamese province where the enterprise is located. These decisions are likely to be driven by strategic considerations related to production costs, developments in foreign markets, and changes in other parts of the global value chain in which the FIE participates. Domestic firms, on the other hand, are more firmly rooted in the local business environment, and should therefore be more sensitive to the specific policies and conditions in the local market. The fact that they do not seem to be strongly impacted by ongoing institutional reforms could indicate that reform processes are too closely linked to the interests of current and prospective foreign investors to matter to private domestic firms, or that Viet Nam's private firms have developed ways to survive even in weak institutional environments. It is also possible that institutional reforms do not generate quick responses among private firms—if firms respond slowly and gradually to reforms, it will be difficult to capture their responses in studies where the province/industry/ownership group is the unit of analysis.

A tentative policy conclusion is that local authorities should focus more on the needs and concerns of domestic enterprises in policy design and institutional reform. It is likely that foreign-invested enterprises will welcome—and lobby in favor of—reforms that reduce uncertainty, risk, and operational costs, but it is uncertain whether any such policies are impactful enough to balance other operational or strategic determinants. To the extent that provincial authorities feel the need to accede to the reform requirement of foreign-invested enterprises, it is necessary to ensure that the reforms will be beneficial also for private domestic firms (Blomström and Kokko 2003).

In the paper, section 2 discusses related literature and surveys existing studies of the links between FDI and subnational institutions in Viet Nam. Section 3 presents the data and estimation model. Section 4 presents results and section 5 concludes with plausible explanations for the findings and outlines policy implications.

## 2. LITERATURE REVIEW

## 2.1. Institutions and Economic Growth

The importance of institutions for economic growth and development is well established (North 1990; Rodrik, Subramanian, and Trebbi 2004; Acemoglu, Johnson, and Robinson 2001; 2002; 2005; Williamson 2009; Hall and Jones 1999). Strong institutions reduce risk and transaction costs and provide incentives for investment, innovation, and entrepreneurship by establishing transparent rules and regulations, protecting property rights, enforcing contracts, and facilitating the accumulation and diffusion of knowledge. Formal institutions are intimately connected to policies. Policies largely reflect institutions, but policy innovations may change institutions over time. As Rodrik, Subramanian, and Trebbi (2004) argue, if institutions are seen as a stock variable, policy is the related flow variable.

However, formal institutions, which are designed through political processes and enforced by regulatory authorities, do not automatically generate successful development. They are most successful when they are embedded in supporting informal institutions that are made up by unwritten norms, conventions, and social practices—often rooted in history, culture, and development level—that constrain the behavior and interactions of individuals (Williamson 2009; Chemin 2009). This link makes it difficult to transfer successful formal institutions between locations.

It is often assumed that formal institutions are uniform within countries, but there are at least two reasons to expect subnational diversity. First, institutional rules established centrally, at the national level, are not always easy to replicate outside the center (Ostrom 2010; Dai et al. 2025). Implementation and enforcement will vary depending on the local context, local informal institutions, and the specific interests of local stakeholders (Williamson 2009; Gertler 2010: Pintar and Scherngell, 2022). Second, national institutions embody only part of the formal standards, rules, and regulations influencing people's lives, such as constitutional rights and obligations, civil and criminal law, national taxation, regulation of entry, and national defense (Djankov et al., 2002; Giacomelli and Menon 2017: Pintar and Scherngell, 2022). The governance of other areas, such as healthcare, education, and local infrastructure is often delegated (within set boundaries) to subnational institutions (Dai et al. 2025: Pintar and Scherngell, 2022).

Regional development research emphasizes that growth is tightly linked to a location's industrial structure (Porter 2003). Industries emerge and persist where essential inputs and institutional needs can be reliably met (Bustos and Yildirim 2022). While some inputs are sourced externally, many others—such as secure access to land and property rights, regulatory compliance, infrastructure, skilled labor, finance, and worker amenities—must be provided locally. The supply of these local inputs partly depends on the quality of subnational institutions (Nee and Opper 2010). Locations with stronger institutions will be able to develop stronger capabilities that allow local firms to grow faster and produce more sophisticated products, underpinning higher productivity and living standards.

## 2.2. Institutions and FDI

The links between institutional quality and FDI inflows have been discussed at length. Numerous studies have shown that strong institutions are positively correlated with inward FDI nationally (Wei 2000; Globerman and Shapiro 2002; Bénassy-Quéré, Coupet, and Mayer 2007; Sabir, Rafique, and Abbas 2019; Andersen, Kett, and von Uexkull, 2017). Some of the institutions highlighted in these studies are stable political regimes, effective protection of property rights, transparent and predictable regulation, and low corruption. However, Daude and Stein (2007), who analyzed the determinants of FDI in 152 host countries in a gravity framework, argue that not all institutional dimensions will be equally important for FDI. While they found robust and significant positive effects of government effectiveness and regulatory quality on FDI, other institutional indicators, including voice and accountability, political stability, and lack of violence were often not significant. Bénassy-Quéré, Coupet, and Mayer (2007) find that bureaucratic efficiency, low corruption, and strong financial institutions are important determinants of inward FDI, while weak capital concentration and employment protection have insignificant or even negative effects. FDI is attracted by institutions that reduce costs and risk and raise productivity prospects but repelled by poor institutions that generate additional costs or uncertainty to foreign investors. Hence, instead of using broad aggregated indices of institutional quality, analysis should focus on the effects of specific institutions and policies (Daude and Stein 2007; Bénassy-Quéré et al. 2007; Hayat 2019).

In addition to the general institutional framework, many countries have introduced policies to attract FDI. For instance, many countries have established specialized investment promotion agencies to reduce the information and transacti

[中间内容因长度限制已省略]

 of Economic Integration 14 (4): 606–624.

Ostrom, E. 2010. “Beyond Markets and States: Polycentric Governance of Complex Economic Systems.” American Economic Review 100 (3): 641–672.

Pérez-Balsalobre, S., C. Llano Verduras, and J. Díaz-Lanchas. 2019. Measuring Subnational Economic Complexity: An Application with Spanish Data. JRC Working Papers on Territorial Modelling and Analysis No. 05/2019. European Commission, Joint Research Centre.

Porter, M. 2003. "The Economic Performance of Regions." Regional Studies 37 (6-7): 545-546.

Pham, H. M. 2002. “Regional Economic Development and Foreign Direct Investment Flows in Vietnam, 1988–98.” Journal of the Asia Pacific Economy 7 (2): 182–202.

Pinheiro, F. L., P. A. Balland, R. Boschma, and D. Hartmann. 2025. “The Dark Side of the Geography of Innovation: Relatedness, Complexity and Regional Inequality in Europe.” Regional Studies 59 (1): 2106362.

Pintar, N., and T. Scherngell. 2022. “The Complex Nature of Regional Knowledge Production: Evidence on European Regions.” Research Policy 51 (8): 104170.

Poncet, S., and F. Starosta de Waldemar. 2012. Export Upgrading and Growth: The Prerequisite of Domestic Embeddedness. FERDI Working Paper No. 57. Fondation Pour Les Etudes Et Recherches Sur Le Développement International.

Rodrik, D., A. Subramanian, and F. Trebbi. 2004. “Institutions Rule: The Primacy of Institutions over Geography and Integration in Economic Development.” Journal of Economic Growth 9 (2): 131–165.

Roodman, D. 2009. A Note on the Theme of Too Many Instruments. Oxford Bulletin of Economics and Statistics 71 (1): 135-158.

Sabir, S., A. Rafique, and K. Abbas. 2019. “Institutions and FDI: Evidence from Developed and Developing Countries.” Financial Innovation 5 (1): 1–20.

Sethi, D., W. Q. Judge, and Q. Sun. 2011. “FDI Distribution within China: An Integrative Conceptual Framework for Analyzing Intra-Country FDI Variations.” Asia Pacific Journal of Management 28 (2): 325–352.

Slattery, C., and O. Zidar. 2020. "Evaluating State and Local Business Incentives." Journal of Economic Perspectives 34 (2): 90–118.

Steven, L., In, S.K, S. M., and Feng, Z. Package "concordance" in R. https://cran.r-project.org/web/packages/concordance/concordance.pdf

Thong, T. N., A. Kokko, and K. N. Hakkala. 2025. A Descriptive Analysis of Firm Development in Vietnam Between 2000 and 2020. ADB Working Paper. Asian Development Bank.

Török, I., J. Benedek, and M. Gómez-Zaldívar. 2022. “Quantifying Subnational Economic Complexity: Evidence from Romania.” Sustainability 14 (17): 10586.

Tran, T. B., R. Q. Grafton, and T. Kompas. 2009. “Institutions Matter: The Case of Vietnam.” The Journal of Socio-Economics 38 (1): 1–12.

Thong, T.N, Kokko A., Nguyen, T.H.D, Trang, P.T.T, Thang, T.T. 2025. A New Approach to Identifying Productive Capacity Gaps Between Firm Groups. Working paper.

Turco, A. L., and D. Maggioni. 2022. “The Knowledge and Skill Content of Production Complexity.” Research Policy 51 (8): 104059.

Van Dam, A., and Frenken, K. 2022. Variety, Complexity and Economic Development. Research Policy 51(8): 103949.

Venables, A. J. 1996. “Equilibrium Locations of Vertically Linked Industries.” International Economic Review 37 (2): 341–359.

Vu, T. V. 2022. “Does Institutional Quality Foster Economic Complexity? The Fundamental Drivers of Productive Capabilities.” Empirical Economics 63 (3): 1571–1604.

Wang, J. 2013. “The Economic Impact of Special Economic Zones: Evidence from Chinese Municipalities.” Journal of Development Economics 101: 133–147.

Wei, S. J. 2000. "How Taxing Is Corruption on International Investors?" Review of Economics and Statistics 82 (1): 1–11.

Williamson, C. R. 2009. “Informal Institutions Rule: Institutional Arrangements and Economic Performance.” Public Choice 139 (3): 371–387.

Wooldridge, J. M. 2010. Econometric Analysis of Cross Section and Panel Data. 2nd ed. Cambridge, MA: MIT Press.

World Bank. 2017. Special Economic Zones: An Operational Review of Their Impacts. Washington, DC: World Bank.

Zaheer, S. 1995. “Overcoming the Liability of Foreignness.” Academy of Management Journal 38(2): 341–363.

Zhou, C., A. Delios, and J. Y. Yang. 2002. “Locational Determinants of Japanese FDI in China.” Asia Pacific Journal of Management 19 (1): 63–86.

Zhu, S., and X. Fu. 2013. "Drivers of Export Upgrading." World Development 51: 221–233.

Zhu, S., and R. Li. 2017. “Economic Complexity, Human Capital and Economic Growth: Empirical Research Based on Cross-Country Panel Data.” Applied Economics 49 (38): 3815–3828.

## Business Climate, Economic Complexity, and Performance at the Provincial Level in Viet Nam

This study investigates how subnational institutions impact the manufacturing sector in Viet Nam, comparing foreign-invested and domestic firms. Using data from 63 provinces, results reveal that institutional changes—measured by the Provincial Competitiveness Index—have little effect on economic complexity, revenues, employment, or productivity. Surprisingly, weaker governance in certain areas sometimes correlates with better firm outcomes. The weak relationship between institutions and firm performance is attributed to the dominance of foreign-invested companies and their limited engagement with local firms.

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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
