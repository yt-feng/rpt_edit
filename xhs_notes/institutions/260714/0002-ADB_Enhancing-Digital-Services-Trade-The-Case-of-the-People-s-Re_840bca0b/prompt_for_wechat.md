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
ENHANCING DIGITAL
SERVICES TRADE

THE CASE OF THE PEOPLE'S REPUBLIC OF CHINA

Rolando Avendano and Hildegunn Kyvik Nordås

NO. 855

July 2026

ADB ECONOMICS

WORKING PAPER SERIES

# Enhancing Digital Services Trade: The Case of the People's Republic of China

Rolando Avendano and Hildegunn Kyvik Nordås

No. 855 | July 2026

The ADB Economics Working Paper Series presents research in progress to elicit comments and encourage debate on development issues in Asia and the Pacific. The views expressed are those of the authors and do not necessarily reflect the views and policies of ADB or its Board of Governors or the governments they represent.

Rolando Avendano (ravendano@adb.org) is a senior economist at the Economic Research and Development Impact Department, Asian Development Bank. Hildegunn Kyvik Nordås (hildegunn.kyviknordas@oru.se) is an adjunct professor at the School of Business Administration, Örebro University (Sweden), and a senior associate at the Council on Economic Policies (Switzerland).

© 2026 Asian Development Bank

6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines

Tel +63 2 8632 4444; Fax +63 2 8636 2444

www.adb.org

Some rights reserved. Published in 2026.

ISSN 2313-6537 (print), 2313-6545 (PDF)

Publication Stock No. WPS260321-2

DOI: http://dx.doi.org/10.22617/WPS260321-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed to another source, please contact the copyright owner or publisher of that source for permission to reproduce it. ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use the ADB logo.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

## ABSTRACT

This paper studies the drivers of trade in services with a focus on the People's Republic of China (PRC). It explores how the digital transformation of services has made services more easily tradable across borders and the policies that facilitate or hinder services trade. The paper starts with a descriptive analysis of new data on bilateral trade and sales from foreign affiliate trade statistics (FATS). Using structural gravity, it then studies the impact of regulatory reform on services trade flows as well as foreign affiliates at a granular level. Finally it applies general equilibrium structural gravity to simulate the impact of (i) regulatory reform in the information and communication technology (ICT) sector in the PRC and ii) implementation of the Regional Comprehensive Economic Partnership on trade, sales and output in services across all economies for which data are available. The largest effect stems from regulatory reforms of the ICT sector in the PRC, which benefit all economies.

Keywords: PRC, digital, services trade, policy

JEL codes: F13, F14

## 1 INTRODUCTION

The economic landscape in the People's Republic of China (PRC) has experienced significant shifts in recent decades. Economic reforms, combined with rapid industrialization, allowed the country to consolidate its position as a global industrial hub, with exports in manufacturing goods as a key driver. With the contribution of the manufacturing sector to GDP and exports declining, the services sector has emerged a potential engine to support its economic development model. As the PRC enters a tertiarization process, with service industries growing faster than agriculture and manufacturing, the importance of opening-up service industries has increased.

Opening-up of service industries has been an important element for the modernization and diversification of the PRC economy, driving innovation and enhancing efficiency, but also for integrating more fully into global markets. Domestically, while services industries providing inputs to the industry sector have increased, the consolidation of the middle class has also prompted higher demand for personal services, such as in health and education. Abroad, the PRC has become a competitive services provider in industries that hitherto have largely been confined to the local market, including information services, telecommunications and other business services.

Together with these developments, digitalization has brought down barriers to services trade and investment and deepened access to a new range of products. The PRC has been at the forefront of the expansion in digital services trade, with the sector growing above 9% from 2010 to 2023. While structural reforms in areas such as human capital development, digital connectivity and information, communication and technology (ICT) investment have been associated to digital services trade in the PRC and Asia, the role of regulatory reforms on services competitiveness requires further analysis.

This paper proposes scenarios for opening-up the PRC's service industries and looks at the implications for digital services trade. Considering different areas of reform, it provides estimates on the impact of regulatory reforms, as well as their importance in the opening-up process.

The rest of the paper is organized as follows: The next section offers a descriptive analysis of cross-border services trade and foreign direct investment (FDI) focusing on digitally deliverable services. Section three analyses the services trade policy framework in a comparative perspective. In addition to a discussion of the services and services related provisions in RCEP, it presents and compares policy indices for services trade openness as well as regulatory performance in telecommunications. Providing network and infrastructure services over which all digital services are transmitted within and across borders, telecommunications are of particular interest. Having described services trade patterns and the policy framework governing such trade and investment patterns, the next sections study how the trade policy framework shapes trade flows. We start in Section 4 with a description of the data that we use, followed by an outline of the analytical framework, which draws on the most recent development in gravity modeling and estimation techniques. The results of the gravity regressions are presented and discussed in Section 5. Section 6 extends the analysis to predicting the outcomes for exports and services

(b) Imports

output of unilateral regulatory reforms in the ICT sector as well as a full implementation of the provisions in RCEP using a general equilibrium gravity framework. Finally, Section 7 summarizes, draws policy implications and concludes.

## 2 PATTERNS OF TRADE

Figure 1 depicts the PRC's trade in digitally deliverable services over 2000 to 2019. The data cover cross-border trade, movement of natural persons and consumption abroad. Both exports and imports grew very rapidly from a low base at the turn of the century. Other business services dominate exports and are also among the largest import categories. However, the largest import category for digitally deliverable services is charges for the use of intellectual property rights. This reflects the importance of imported technology in all sectors, including manufacturing, mining and agriculture. $^{1}$

Figure 1: The PRC's Trade in Digitally Deliverable Services By Sector  
![](images/22e995bfcf40d23676f1f27a7e75ff39fc062cbcfd0fbf12acb8fa36b4a28df8.jpg)

![](images/85fdeb66765fa72291a25ae25e14091508902a7e5eb0e8dde990f7f5c313ae2b.jpg)  
PRC = People's Republic of China.  
Note: The sector ID: 159, Insurance and pension services; 160, Financial services; 161, Charges for the use of intellectual property n.i.e; 162, Telecommunications, computer and information services; 163, Other business services.
Source: International Trade and Production Database for Estimation.

A recently released database, the Multinational Revenue, Employment and Investment Database (MREID) provides information on bilateral affiliate sales, number of affiliates, foreign assets and employment in multinationals for 25 NAICS industries and 185 economies for 2010-2021 $^{2}$ . We used this database to analyze trends in FDI and foreign affiliate sales (Mode 3 in the terminology of the General Agreement on Trade in Services, or GATS).

Comparing the statistics for trade by foreign affiliates against other categories of trade data gives a rough idea of the importance of Mode 3 relative to the other modes, and differences in the sector composition of trade and FATS. First, we notice that similar to global services trade patterns FATS dwarfs trade through other modes. $^{3}$ Second, while imports are larger than exports on both counts, the gap is much larger for affiliate sales. Third, while information services account for the bulk of outward affiliate sales, finance dominated inward sales in the first years for which data are available. Information services have, however, gained prominence in recent years also for inward affiliate sales.

Figure 2: The PRC's Trade in Digitally Deliverable Services By Region  
(a) Exports  
![](images/13c61db62a14a3faa36569d96082a47c807ba15653dc788fa84d6871aba167b1.jpg)

(b) Imports  
![](images/aa85c5e66c54343781328a113a46ed7417b0761119e5888a8ddfea2a420f2d8f.jpg)  
DDS = digitally deliverable services, EU = European Union, PRC = People's Republic of China, RCEP = Regional Comprehensive Economic Partnership, ROW = rest of the world, USMCA = United States–Mexico–Canada Agreement.
Note: The sectors are the same as in Figure 1.  
Source: International Trade and Production Database for Estimation.

Figure 3: The PRC's Affiliate Sales of Digitally Deliverable Services by Sector  
(a) Outward  
![](images/cc6dfada07580882399dd5a9c4b8039fca354c61bfeb516a95c79ab80e179020.jpg)

(b) Inward  
![](images/aa9311b0b18c227252a49b40dabd0d2e0c7e40d22c27e37451f48dc697bb1928.jpg)  
Source: Multinational Revenue, Employment and Investment Database.

Figure 4: The PRC's Affiliate Sales of Digitally Deliverable Services by Region  
(a) Outward  
![](images/ea40ba8a297428fb0a20a0cfdcb32efdd5f550bb2d41c4c730a5d62112580f22.jpg)

(b) Inward  
![](images/a01a8c30fd4c2e6295a2014c1c9500043945b6ab045834788f24842157d8b51d.jpg)  
EU = European Union, PRC = People's Republic of China, RCEP = Regional Comprehensive Economic Partnership, ROW = rest of the world, USMCA = United States–Mexico–Canada Agreement.
Notes: Outward refers to sales by the PRC multinationals. Inward refers to sales in the PRC by foreign affiliates.
Source: Multinational Revenue, Employment and Investment Database.

Analyzing trade in digitally deliverable services across modes by partner regions, we split the global market into four regions, the economies of the Regional Comprehensive Economic Partnership (RCEP), the European Union, the United States-Mexico-Canada Agreement (USMCA), and the rest of the world. Figures 2 and 4 respectively show trade and FATS by region. While the three USMCA economies dominate both exports and imports, the rest of the world accounts for the better part of outward and inward FATS. Detailed FATS data reveals that Hong Kong, China and the Cayman Islands and Bermuda account for the bulk of rest of the world. $^{4}$

As in most economies, the domestic market is the most important for Chinese multinationals. Furthermore, Chinese multinationals have become more inward-oriented during the past decade or so. Home market sales were on average slightly above 60% in 2010 for all sectors and increased to about 80% in 2020. Services followed the same pattern. As illustrated in Figure 5 digitally deliverable services also depict the same pattern, although with an interesting dispersion of home market reliance. Postal and legal services have been strongly inward oriented throughout the period, but information services and finance and insurance have become much more inward oriented over time. Only management of companies and enterprise multinationals have become more outward oriented over time. These enterprises probably provide Chinese affiliates abroad with management services and constitute a relatively small sector, accounting for less than 1% percent of Chinese affiliate sales.

Figure 5: The PRC Multinationals Home Market Sales, Share of Total Sales  
![](images/b6c2cd9ee2ce414238c204c98c7db84013095af7365db6657a07f38f012ff735.jpg)

![](images/d0d88995fef4df11cc80a6aa58faedf5e9db9a0beed7db396ff2371ed0952610.jpg)

![](images/3415615ae7cce460a867ca57015bc0f62ad50ff3fa9e54dee33708eedcf665b4.jpg)

![](images/77f7eff7f7fccc6e4cbe5f8b3cefc9c1f33e5a3c668ba1bdc9c038f9b67e4f5d.jpg)  
PRC = People's Republic of China.

![](images/5f405251d9d4b6e230fcd50c7499530b1fb50a1e999f65c66d4a49d8156473c0.jpg)  
Source: Multinational Revenue, Employment and Investment Database.

We finally look at the role of foreign affiliates in employment creation in the PRC. Employment is concentrated in foreign manufacturing affiliates and peaked at about six million workers in 2018. "Other" consists of agriculture forestry and fisheries, oil and gas, and utilities.

Figure 6: Employment in Foreign Affiliates in the PRC by Sector  
![](images/6e703921c0c55495fe470e3527f541ac028f0adbc633fe2057abe4cff596329e.jpg)  
DDS = digitally deliverable services, PRC = People's Republic of China. Source: Multinational Revenue, Employment and Investment Database.

## 3 DIGITAL SERVICES SECTOR OPENNESS

## 3.1 Domestic Regulation and Most-Favored Nation Provisions

This section presents the PRC's openness to trade and investment in digitally deliverable services in comparison to the other G20 members, RCEP and the Comprehensive and Progressive Agreement for Trans-Pacific Partnership (CPTPP). It starts with studying information provided in the Organisation for Economic Co-operation and Development (OECD)'s Digital Services Trade Restrictiveness Index (DSTRI) and the regulatory tracker of the International Telecommunication Union (ITU). Then it looks into the provisions in RCEP relevant to trade in digitally deliverable services. The DSTRI takes value between zero and one, where zero represents no restrictions while one represents the case where all the measures covered are restrictive. The largest contribution to the PRC's restrictiveness as measured by the DSTRI comes from infrastructure, which refers to restrictions on cross-border data flows and data localization requirements. Turning to the ITU regulatory tracker, its scores run from zero to 100, where a higher score represents better regulation. On this metric, the PRC comes closest to the other economies on 'regulatory regime', which records tools and measures the regulator has at its disposal. Examples are licensing, mandating a reference offer for access and interconnection with telecoms networks, number portability and secondary spectrum trading to mention but a few. $^{5}$ The PRC falls short on the 'regulatory authority' metric, which refers to the presence and independence of a regulator for the ICT sector. The PRC also falls short on competition, which reflects the state of competition in each market segment. As this is an outcome pillar, we exclude it from regressions presented in the next sections.

Figure 7: Digital STRI Scores, G20, RCEP and CPTPP economies, 2023  
![](images/6b7ccdc7efe9e6e1f471a51bda4524f8d8b3bb09876b75c5692d30085fac502d.jpg)

CPTPP = Comprehensive and Progressive Agreement for Trans-Pacific Partnership, IPR = intellectual property rights, RCEP = Regional Comprehensive Economic Partnership, STRI = OECD Services Trade Restrictiveness Index.

Notes: The figure shows the score on the OECD Services Trade Restrictiveness Index for 2023 by policy area. Scores range from 0 (completely open) to 1 (completely closed). Infrastructure refers Infrastructure and connectivity, Payment to Payment systems Electr. trans to Electronic transactions, IPR to intellectual property right and Other to Other barriers affecting trade in digitally enabled services. The three-letter codes are a combination of the Asian Development Bank and ISO 3166-1 alpha-3 codes. Source: Organisation for Economic Co-operation and Development.

Figure 8: Score on ITU Regulatory Tracker, G20, RCEP, and CPTPP Economies, 2022  
![](images/76fbe184df8d8f5f0230919cfb8a7775e555671d99b227026e676151149efd03.jpg)  
CPTPP = Comprehensive and Progressive Agreement for Trans-Pacific Partnership, G20 = Group of 20, ITU = International Telecommunication Union, RCEP = Regional Comprehensive Economic Partnership. Notes: The figure shows the score on the ITU regulatory tracker for 2022 by policy area. Scores rank from zero to 100 where a higher score means more open and better regulated. The three-letter codes are a combination of the Asian Development Bank and ISO 3166-1 alpha-3 codes.
Source: International Telecommunication Union.

## 3.2 RCEP

The RCEP agreement consolidates into one framework free trade agreements (FTA) between the Association of Southeast Asian Nations (ASEAN) and its free trade partners (Australia, Japan, the Republic of Korea, New Zealand and the PRC). Among RCEP members, Japan and the Republic of Korea; and Japan and the PRC do not have other common FTAs. Thus, RCEP brings together the largest Asian economies in a trade agreement for the first time.

## 3.2.1 The services chapter

The services chapter covers all services sectors except air transport. Its architecture is similar to the GATS. Thus, as in the G

[中间内容因长度限制已省略]

d generate spillovers to neighboring economies in Asia. These reforms have the potential to improve the density, quality and cost-effectiveness of ICT infrastructure, resulting in a potential 50% increase in digital services trade and gains in market share both at home and abroad. These effects are driven by the positive spillovers of regulatory accountability, the existence of a competition authority and higher flexibility for consumers through measures such as number portability.

The scenario analysis also underscores that the PRC's neighboring trading partners such as the Lao PDR and Cambodia can experience significant trade and welfare gains. The modernization of ICT regulatory regimes can both increase the PRC foreign affiliate sales and favor the establishment of new foreign affiliates domestically. In this regard, the PRC's unilateral reforms in the ICT sector can be significant for enhancing regional integration in Asia and the Pacific.

The second scenario explores the PRC's implementation of services digital commitments under RCEP. The RCEP agreement reflects the commitment of Asian economies to take a gradual approach toward a free trade area of Asia and the Pacific. It was intended as a stepping stone toward more comprehensive integration, while deliberately leaving room for improvement. It also considers more flexibility on imposing disciplines on members at early stages of development.

The three scenarios proposed suggest positive impacts for different levels and degrees of implementation of RCEP commitments. Assuming simple FTA participation, the scenario suggests significant gains in services trade, in particular for the PRC, Japan and the Republic of Korea, who would form new preferential relationships. A second scenario creates a bilateral counterfactual by mapping RCEP provisions to the STRI/APEC index and provides a metric of the full potential of the agreement when fully implemented. The scenario analysis explores the implementation of both horizontal policy measures and sector measures, with a focus on telecommunications and banking services. Besides the potential gains in services trade and welfare, implementing RCEP commitments may also attract new FDI flows, reinforce the PRC's international credibility and support new trade negotiations.

## REFERENCES

Anderson, James E, Mario Larch, and Yoto V Yotov (2018). “GEPPML: General Equilibrium Analysis with PPML”. In: The World Economy 41.10, pp. 2750–2782.

Andrenelli, Andrea and Javier López González (2019). “Electronic Transmissions and International Trade-shedding new light on the moratorium debate”. In: Working Paper of the Trade Committee TAD/TC/WP(2019)19/FINAL.

Bergstrand, Jeffrey H and Jordi Paniagua (2024). “Do Deep Trade Agreements ‘Provisions Actually Increase—or Decrease—Trade and/or FDI?” In.

Beverelli, Cosimo et al. (2024). “Institutions, Trade, and Development: Identifying the Impact of Country-Specific Characteristics on International Trade”. In: Oxford Economic Papers 76.2, pp. 469–494.

Greenleaf, Graham (2009). “Five years of the APEC Privacy Framework: Failure or promise?” In: Computer Law & Security Review 25.1, pp. 28–43.

Heid, Benedikt, Mario Larch, and Yoto V Yotov (2021). “Estimating the Effects of Non-discriminatory Trade Policies Within Structural Gravity Models”. In: Canadian Journal of Economics/Revue canadienne d’économique 54.1, pp. 376–409.

Hummels, David and Alexandre Skiba (2004). “Shipping the Good Apples Out? An empirical Confirmation of the Alchian-Allen Conjecture”. In: Journal of political Economy 112.6, pp. 1384–1402.

Liberatore, Antonella and Steen Wettstein WTO (2021). “THE OECD-WTO Balanced Trade IN Services Database (BaTIS)”. In.

Lipovetsky, Stan and Michael Conklin (2001). “Analysis of Regression in Game Theory Approach”. In: Applied stochastic models in business and industry 17.4, pp. 319–330.

McElheran, Kristina et al. (2024). “AI Adoption in America: Who, what, and where”. In: Journal of Economics & Management Strategy.

Nordås, Hildegunn Kyvik (2023). “Services in the India-EU Free Trade Agreement”. In: International Economics 176, p. 100460.

Sullivan, Clare (2019). “EU GDPR or APEC CBPR? A comparative analysis of the approach of the EU and APEC to cross border data transfers and protection of personal data in the IoT era”. In: computer law & security review 35.4, pp. 380–397.

Yotov, Yoto V (2022). “On the Role of Domestic Trade Flows for Estimating the Gravity Model of Trade”. In: Contemporary Economic Policy 40.3, pp. 526–540.

— (2024). “The Evolution of Structural Gravity: The Workhorse Model of Trade”. In: Contemporary economic policy.

## Enhancing Digital Services Trade The Case of the People's Republic of China

This paper examines the drivers of digital services trade in the People's Republic of China and the role of regulatory reforms in shaping services competitiveness. Using new data on bilateral trade and foreign affiliate sales, the paper assesses the impact of information and communication technology (ICT) regulatory reforms and the implementation of the Regional Comprehensive Economic Partnership. Results show that both reforms would benefit Asian economies, with the largest effects stemming from reforms in the ICT sector.

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
