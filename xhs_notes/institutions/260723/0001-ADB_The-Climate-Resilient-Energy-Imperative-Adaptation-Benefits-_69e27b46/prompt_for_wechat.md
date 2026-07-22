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
![](images/4bd8aaf9acf7191e4c2e4ebaadf09f2cda31879c88d520322b1204d4fd5e3086.jpg)

THE CLIMATE-RESILIENT
ENERGY IMPERATIVE
ADAPTATION BENEFITS AND ACTIONS FOR ALL
JULY 2026

# THE CLIMATE-RESILIENT ENERGY IMPERATIVE

JULY 2026

© 2026 Asian Development Bank

6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines

Tel +63 2 8632 4444; Fax +63 2 8636 2444

www.adb.org

Some rights reserved. Published in 2026.

ISBN 978-92-9277-883-5 (print); 978-92-9277-884-2 (PDF); 978-92-9277-885-9 (e-book)

Publication Stock No. TCS260324-2

DOI: http://dx.doi.org/10.22617/TCS260324-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed to another source, please contact the copyright owner or publisher of that source for permission to reproduce it. ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use the ADB logo.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

## Notes:

1. In this publication, "\$" refers to United States dollars.

2. ADB recognizes “Laos” as the Lao People’s Democratic Republic and “Republic of Marshall Islands” as the Republic of the Marshall Islands.

3. Effective 1 February 2021, ADB place a temporary hold on sovereign project disbursements and new contracts in Myanmar ADB placed its regular assistance to Afghanistan on hold, effective 15 August 2021.

Cover design by Michael Cortes.

Contents

Tables and Figures iv
Acknowledgments v
Abbreviations vi
Executive Summary vii
1 Introduction 1
2 Why Should Energy Systems Be Resilient to Climate Impacts? 2
Increasing Climate Impacts 2
Climate Impacts on Energy 3
3 Who Will Benefit from Resilient Energy Systems? 7
Growing Demand for Building Resilience 7
Multiple Benefits of Building Resilience 9
4 What Are the Key Barriers to Energy Sector Resilience? 11
Limited Availability of Accessible and Accurate Climate and Weather Information for Energy 11
Limited Consideration of Energy System's Adaptation in National Climate Strategies 13
Insufficient Adaptation Finance in the Energy Sector 15
Slow Progress in Adopting Innovative Technologies 17
5 How Can the Energy Sector Overcome Key Barriers and Build Resilience? 20
Improved Quality of Climate Information for Energy Systems 20
Incorporation of Climate-Resilient Energy Systems in National Strategies 22
Scaling Up Adaptation Finance in the Energy Sector 25
Accelerated Deployment of Innovative Adaptation Technologies 28
6 Conclusion 34
References 35

# Tables and Figures

## Tables

1 Climate Risks to Electricity Supply in the Low-emissions and High-emissions Scenarios, 2080–2100
2 Multiple Benefits of Climate-Resilient Energy System
3 Actions for Improved Quality of Climate Information for Energy Systems by Stakeholder
4 Actions for Incorporation of Climate-Resilient Energy Systems in National Strategies by Stakeholder
5 Actions for Scaling Up Adaptation Finance in the Energy Sector by Stakeholder
6 Status of Key Existing Policy Instruments to Improve the Energy Efficiency of Appliances
7 Actions for Accelerating Deployment of Innovative Adaptation Technologies in the Energy Sector by Stakeholder
Figures
1 Exposed Value and Average Annual Loss by Infrastructure Sector
2 Share of National Meteorological and Hydrological Services
Providing Data Services to the Energy Sector as of 2022
3 Share of Adaptation Priorities in All NDCs as of 2024
4 Share of Adaptation Priorities in All NAPs as of 30 September 2023
5 Share of NDCs and NAPs Including Energy as Adaptation Priority, ADB DMCs
Comparison of Adaptation Finance Needs (extrapolated) and Modelled Costs of Adaptation (annual to 2030) and International Public Adaptation Finance Flow (2018–2022 average) for Developing Countries by Sector
Share of Solar PV and Wind in Electricity Generation by Country
Share of ADB DMCs That Prioritized Energy as an Adaptation Priority in NDCs and NAPs
MDB Adaptation Finance by Sector in Low- and Middle-Income Economies, 2013 and 2023
Boxes
1 Border-Crossing Climate Impacts Through Interconnected Electricity Networks
2 Resilient Energy Systems for Vulnerable Groups
3 ADB's Commitment to Adaptation Finance in the Energy Sector
4 Innovative Wind Turbines Against Intensifying Tropical Cyclones

## Acknowledgments

This report was written by Jinsun Lim, adaptation solutions specialist (energy) under the strategic guidance of Arghya Sinha Roy, director climate change. The author extends sincere thanks to colleagues at the Asian Development Bank (ADB) for their valuable feedback, suggestions, and thoughtful engagement throughout the drafting and review process. In particular, the author is grateful to Architrandi Priambodo (senior energy specialist), Kelly Hewitt (principal energy specialist), Martin Okata (senior climate and disaster risk specialist), and Silas Markert (climate resilience specialist) for their insightful comments on the earlier versions of the report and Marilyn Aure. Parra (operations analyst) for her support. The author also appreciates insightful comments from Roberta Boscolo (World Meteorological Organization), and input from David von Hippel (Consultant) as well as editing and visualization support from Alfredo De Jesus, Jess Macasaet, John Mercurio, and Rocilyn Laccay.

## Abbreviations

ADB Asian Development Bank
AI artificial intelligence
CPS country partnership strategy
DMC developing member country
ENSO El Niño Southern Oscillation
IEA International Energy Agency
IPCC Intergovernmental Panel on Climate Change
IRENA International Renewable Energy Agency
Lao PDR Lao People's Democratic Republic
MDB multilateral development bank
NAP national adaptation plan
NDC nationally determined contribution
OCR ordinary capital resources
PPP public-private partnership
PRC People's Republic of China
PV photovoltaic
UNFCCC United Nations Framework Convention on Climate Change
VRE variable renewable energy
WMO World Meteorological Organization

# Executive Summary

Climate-resilient energy systems are an imperative now. Rising temperatures, shifting precipitation patterns, sea level rise, and more frequent extreme weather events are disrupting energy supply while reshaping energy demand patterns. Energy systems in Asia and the Pacific are already struggling to cope with power outages caused by extreme heat events, physical damage to assets by floods and landslides, increasing threats to coastal energy infrastructure due to tropical cyclones and sea level rise, and changes in energy resource availability. As the energy sector in the region is already strained by weak infrastructure and rapidly increasing demand, such impacts due to the changing climate pose a significant challenge to energy system resilience.

Recognizing these growing risks, diverse stakeholders—including energy suppliers, consumers, and national authorities—are increasingly calling for stronger resilience measures. Energy suppliers seek to protect assets, maintain service reliability, and safeguard revenue streams from disruptions due to changes in the climate and extreme weather. Resilient energy systems help energy suppliers avoid costly damage, pursue long-term planning, and strengthen stability. For consumers, reliable energy access underpins economic growth, ensures the continuity of essential public services such as health care and water supply, and safeguards livelihoods—especially for vulnerable groups who lack alternative resources to cope with disruptions. Governments and regulators view energy resilience as essential for ensuring energy security, advancing renewable energy transitions, and enhancing disaster risk management capacity.

Despite rising awareness and clear benefits, adaptation in the energy sector lags behind. Many efforts focus narrowly on individual assets rather than developing system-wide, long-term resilience. The report identifies four critical barriers to progress:

\- Limited availability of accessible and accurate climate and weather information for energy. Although climate and weather data are becoming increasingly important with growing impacts of the changing climate and the rapid expansion of renewable energy, developers and investors frequently report challenges in accessing and interpreting climate information. Government support also remains limited despite its critical role in the collection and dissemination of such information.

\- Limited consideration of energy system's adaptation in national climate strategies. Discussions on energy and climate have traditionally concentrated on mitigation while adaptation has received significantly less attention. This imbalance is particularly evident in national climate strategies such as nationally determined contributions (NDCs) and national adaptation plans (NAPs). Globally, only $41\%$ of NDCs submitted by 2024 prioritized adaptation in the energy sector, while only $27\%$ of global NAPs (13 out of 48, as of 2023) recognized energy as an adaptation priority. In Asia and the Pacific, $43\%$ of NDCs and $63\%$ of NAPs (as of October 2025) included energy as one of their adaptation priorities. Although these efforts align with, or even exceed, global trends, they remain insufficient given the scale of the impact of the changing climate on energy systems.

\- Insufficient adaptation finance in the energy sector. Although energy is among the sectors requiring the largest amount of adaptation financing, it continues to fall short as most climate finance goes to mitigation. For instance, in 2023, MDBs committed only \$7.25 billion for adaptation in energy, transport, and other built environment and infrastructure, accounting for less than 10% of total climate finance committed to these sectors (\$76.45 billion). Moreover, adaptation finance from the private sector remains limited, particularly in developing countries, due to perceived high up-front costs, overlooked long-term adaptation benefits, lack of reliable climate risk data, monopolistic market structures, and policy uncertainties.

\- Slow progress in adopting innovative technologies. In the energy sector, the uptake of innovative adaptation technologies has lagged even though many of these technologies are both mature and economically viable. Variable renewable energy technologies, which enable diversification and decentralization of energy sources against climate impacts, remain limited in many developing countries. Deployment of smart grids and efficient cooling solutions also remains low. The slow progress is due to various reasons including low awareness, limited technical capacity, high financing costs, weak institutional frameworks, and the need to adapt technologies to local contexts.

To overcome these barriers and strengthen resilience, the following actions from all key stakeholders, including energy suppliers, consumers and authorities, are essential (Table):

\- Improve quality of climate information for energy systems. Government authorities, including relevant ministries and agencies, can address knowledge barriers by enhancing the quality of climate information services and strengthening observation networks near major energy assets. Energy suppliers can contribute to improving climate information by conducting robust climate risk and impact assessments and feeding the results back into national information systems. Energy consumers can also provide data on climate impacts from the demand side through monitoring and feedback systems.

\- Incorporate climate-resilient energy systems in national strategies. National authorities can avoid market failures and enforce resilience measures to protect broader socioeconomic benefits by recognizing the energy sector as an adaptation priority. As of October 2025, 22 out of 42 the Asian Development Bank developing member countries included the energy sector as an adaptation priority in their NDCs or NAPs. Energy suppliers may be encouraged to embed resilience considerations into project design and operations, following the recommendations outlined in national climate strategies. Energy consumers can advocate for climate resilience, raise public awareness of climate risks, and foster broader acceptance of adaptation measures.

\- Scale up adaptation finance in the energy sector. Private energy suppliers and investors can expand adaptation finance by embedding climate risk assessments and resilience benefits into their decision-making processes. This approach enables them to better understand the financial impacts of climate hazards and enhance long-term revenues. Public investment from national authorities and multilateral development banks can help lower costs, boost investor confidence, and facilitate the implementation of resilience measures. Energy consumers can encourage energy suppliers to adopt resilience measures through power purchase agreements that include reliability clauses against climate-driven disruptions.

Table: Actions to Build Climate Resilience in the Energy Sector by Stakeholder

<table><tr><td></td><td><img src="images/ef4b12e3184e8d6db94809173c50f93c63f6eb388e08de8d12eefc878619cefa.jpg"/></td><td><img src="images/56f6b0c37b336e46442f7c3fa0860a862e5c3655f9b72488cb6a6e41f4673e0b.jpg"/></td><td></td></tr><tr><td>STAKEHOLDERS</td><td>National authorities</td><td>Energy suppliers</td><td>Energy consumers</td></tr><tr><td colspan="4">ACTIONS</td></tr><tr><td>Actions for Improved Quality of Climate Information for Energy Systems by Stakeholder<img src="images/fab9f54951924c7bf04a7fdb4ad9b22aadff75cbe40655c994b0b6f61ebf02d9.jpg"/></td><td>Enhance the quality of public climate information services at national, regional, and local levelsStrengthen climate observation networks by expanding observation stations near major energy assets and introducing advanced technologies</td><td>Conduct robust climate risk and impact assessmentsFeed assessment results back into national climate information systems</td><td>Offer valuable feedback on how climate and weather influence their energy consumption patterns and comfort levelsInstall energy consumption monitoring systems to enable more detailed analysis of climate variables and energy demand patterns</td></tr><tr><td>Actions for Incorporation of Climate-resilient Energy Systems in National Strategies by Stakeholder<img src="images/bc9c81752d8b391a84b77bcc5603ecab76abb3d2dc41920384d2bbcb49a0090a.jpg"/></td><td>Include the energy sector in national adaptation strategies as one of the adaptation prioritiesOrganize stakeholder consultations to identify concrete actions across the entire lifecycle of energy projectsDevelop a robust implementation plan</td><td>Embed resilience considerations into project design and operationsAlign corporate strategies with national adaptation goalsProvide technical feedback and share best practices for further development and effective implementation of adaptation policies</td><td>Provide a strong political foundation for advancing climate resilience policies and regulationsRaise public awareness of climate risks to the energy sectorFoster broader acceptance of adaptation measures</td></tr><tr><td>Actions for Scaling Up Adaptation Finance in the Energy Sector by Stakeholder<img src="images/754c9cad213d12453fb804ebacf4cd74fdbce71af23ba2d21d791bd03e0a1fe3.jpg"/></td><td>Promote blended finance approaches that combine concessional capital from the public sector with private sector investmentsCreate an enabling environment for private investment by providing technical assistance for climate risk assessments and demonstrating the viability of innovative technologiesOffer risk-sharing mechanisms through diverse and innovative financial instruments to scale up adaptation finance</td><td>Expand adaptation finance by systematically embedding climate risk assessments in investment planningIncorporate long-term resilience benefits into decision-making and valuation processesLeverage insurance as an effective risk-transfer mechanism to manage climate-related uncertainties</td><td>Integrate reliability requirements into power purchase agreements</td></tr><tr><td>Actions for Accelerating Deployment of Innovative Adaptation Technologies in the Energy Sector by Stakeholder<img src="images/dc500878e29c3e5a2d32a60c2d39a071763d87403e1979561aa50d4d91cb57c2.jpg"/></td><td>Support the adoption of innovative energy-efficient technologies by improving standards and labeling systemsEncourage behavioral changes by providing incentives</td><td>Scale up new renewable energy technologies for diversification of energy sourcesImprove the accuracy of forecasts of potential outages and enable early warning systems through digital technologiesEnable faster detection and restoration of climate-related faults with advanced smart technologies</td><td>Enhance the accuracy and applicability of digital technologies as a knowledge providerAccelerate the deployment of innovative technologies by purchasing more efficient options</td></tr></table>

\- Accelerate deployment of innovative adaptation technologies. Energy suppliers can enhance resilience through technological and geographical diversification of energy sources. The increasing penetration of new renewable energy can be a resilience solution when its climate sensitivity is addressed through innovative designs and technologie

[中间内容因长度限制已省略]

y Assessment with GIS.

European Investment Bank (EIB) et al. 2024. 2023 Joint Report on Multilateral Development Banks' Climate Finance.

EIB, et al. 2022. Joint Methodology for Tracking Climate Change Adaptation Finance.

EVN Viet Nam Electricity. 2024. UAV and AI Technology Applications: Breakthrough in Transmission Grid Operation Management.

Global Center on Adaptation and Climate Policy Initiative. 2023. State and Trends in Climate Adaptation Finance 2023.

Google. FireSet.

Google. Flood Forecasting.

Institut Penyelidikan Air Kebangsaan Malaysia. Malaysia Adaptation Index.

Intergovernmental Panel On Climate Change (IPCC). 2021. IPCC Sixth Assessment Report: Working Group II: Impacts, Adaptation and Vulnerability.

——. 2021. IPCC Sixth Assessment Report: Working Group III: Mitigation of Climate Change.

——. 2021. IPCC Sixth Assessment Report: Working Group II: Impacts, Adaptation and Vulnerability.

International Energy Agency (IEA) et al. 2024. Tracking SDG7: The Energy Progress Report 2024.

IEA. 2021. Climate Impacts on South and Southeast Asian Hydropower.

——. 2022. Climate Resilience for Energy Security.

——. 2024. Renewables 2024.

——. 2019. The Future of Cooling in Southeast Asia.

——. 2023. Deployment to Date of Residential Smart Meters, 2021.

——. 2024. Climate Resilience for Energy Security in Southeast Asia.

——. 2024. Southeast Asia Energy Outlook 2024.

——. 2025. Energy and AI.

——. 2025. World Energy Investment 2025.

International Renewable Energy Agency (IRENA). 2022. Renewable Energy Statistics.

Kingdom of Cambodia. 2025. Cambodia's Third Nationally Determined Contribution (NDC 3.0).

Manila Observatory. 2022. High-Definition Clean Energy, Climate, and Weather Forecasts for Philippines.

Milliken, K., J. Lim, and N. Kuruppu. 2025. Cooling the Heat Crisis with Energy and Health Solutions. Asian Development Blog. 10 February.

National Oceanic and Atmospheric Administration (NOAA). 2025. 2024 Was the World's Warmest Year on Record.

Philippine Energy Development Corporation. 2018. Bouncing Back Strong as Consumers Make the Switch to Renewable Energy.

Qi, W. 2013. Chinese Typhoon Knocks Out 17 Wind Turbines. Windpower Monthly. 25 September.

Reliefweb. 2024. UNICEF Pacific: Drought Emergency Response for the North Pacific – Federated States of Micronesia and Republic of Marshall Islands.

Rojas, D. et al. 2025. Energy Justice Through Energy Storage: Supporting Energy Resilience in Disadvantaged Communities. Current Sustainable/Renewable Energy Report. 12 (17).

Skywatch. 2022. How to Use Satellite Imagery to Reduce Risk in Oil & Gas.

The Straits Times. 2024. Heatstroke Kills 61 in Thailand So Far In 2024. 10 May. https://www.straitstimes.com/asia/se-asia/heatstroke-kills-61-in-thailand-so-far-in-2024.

United Nations Environment Programme (UNEP). 2023. Adaptation Gap Report 2023.

UNEP. 2023. State and Trends in Climate Adaptation Finance 2023.

——. 2024. Adaptation Gap Report: Come Hell and High Water.

UNEP Copenhagen Climate Centre. 2023. Technology Transfer for Climate Mitigation and Adaptation.

United Nations Framework Convention on Climate Change (UNFCCC). 2023. National Adaptation Plans 2023: Progress in the Formulation and Implementation of NAPs.

——. 2024. NDC Synthesis Report.

—. National Adaptation Plans.

——. 2023. Overview - National Adaptation Plans.

——. 2024. Nationally Determined Contributions under the Paris Agreement Synthesis Report by the Secretariat.

United Nations Office for Disaster Risk Reduction (UNDRR). 2024. Intense Heatwaves Make April 2024 the Hottest On Record.

Visapra, P. 2024. Heatwave Strains Power Supply Across Laos: Electricity State Company Responds to Public Backlash. The Laotian Times. 9 May.

World Bank Group. 2019. Stronger Power: Improving Power Sector Resilience to Natural Hazards.

World Bank. 2021. Enabling Private Investment in Climate Adaptation and Resilience: Current Status Barriers to Investment and Blueprint for Action.

World Bank. 2024. Rising to the Challenge.

World Meteorological Organization (WMO). 2022. 2022 State of Climate Services.

——. 2022. 2022 State of Climate Services.

——. 2024. State of the Climate in Asia 2023.

——. 2025. WMO Confirms 2024 as Warmest Year On Record at About 1.55°C Above Pre-industrial Level.

Yao, Q. et al. 2024. Anti-tropical Cyclone Load Reduction Control of Wind Turbines Based on Deep Neural Network Yaw Algorithm. Applied Energy. Volume 376, Part B.

## The Climate-Resilient Energy Imperative Adaptation Benefits and Actions for All

Climate-resilient energy systems are becoming imperative as the impacts due to the changing climate intensify across the region. Energy infrastructure in the Asia and Pacific region is already under strain, facing power outages due to the impact of changes in the climate, physical damage, and shifting demand patterns. In response to these growing risks, stakeholders are calling for stronger and more coordinated resilience measures. This report outlines the multiple benefits of climate-resilient energy systems, examines current barriers to progress, and proposes targeted actions for key actors—including energy providers, consumers, and government regulators—to accelerate the transition toward a more resilient energy future.

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
