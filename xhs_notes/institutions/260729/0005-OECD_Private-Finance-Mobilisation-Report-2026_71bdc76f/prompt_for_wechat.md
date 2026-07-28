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
- 已识别机构名：`经合组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份经合组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Private Finance Mobilisation Report 2026

![](images/9dee9ed3b5fd290ef850394abae20d56a8bc9c78ffbcdb02818efb0919732036.jpg)

## Private Finance Mobilisation Report 2026

This work is issued under the responsibility of the Secretary-General of the OECD, and does not necessarily reflect the official views of OECD Member countries.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

Please cite this publication as: OECD (2026), Private Finance Mobilisation Report 2026, OECD Publishing, Paris, https://doi.org/10.1787/a871a032-en.

ISBN 978-92-64-78369-0 (print)
ISBN 978-92-64-72349-8 (PDF)
ISBN 978-92-64-90547-4 (HTML)

Photo credits: Cover © coldsnowstorm/Getty Images.

Corrigenda to OECD publications may be found at: https://www.oecd.org/en/publications/support/corrigenda.html.
© OECD 2026

![](images/1681f6aa73cc6418d7cddb76bd8093053ed998fa0c4bef2ec476eb010067f41f.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of the original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

The global development finance landscape is under growing strain. Amid intensifying fiscal pressures and tightening public budgets, mobilising private finance has become a critical strategy in efforts to achieve more effective sustainable development outcomes. At the Fourth International Conference on Financing for Development (FFD4) in Sevilla, the international community reaffirmed the urgency of scaling up private finance mobilisation while improving its effectiveness, transparency and alignment with sustainable development priorities, an imperative also reflected in the OECD Secretary-General's Taskforce on Mobilisation. The current DAC review process will also help position the use of official development assistance within the broader landscape of sustainable finance and demonstrate how it complements and enables other forms of development finance, including mobilising the private sector.

Within this context, the OECD's 2025 Private Finance Mobilisation Report provides a crucial stocktake of where mobilisation efforts stand today. Drawing on the OECD Development Assistance Committee's statistical framework, the report offers the most comprehensive and internationally comparable evidence on private finance mobilised by official development finance interventions. It sheds light on which instruments and approaches are working, where progress has stalled, and which sectors and regions continue to be left behind.

While private finance mobilisation has increased over time, the evidence in this report shows that volumes remain well below what many had hoped for at the time of the adoption of the Sustainable Development Goals in 2015. Mobilisation outcomes remain highly concentrated across a limited number of instruments, providers and markets, raising important questions about scalability, risk sharing and the targeting of public resources. Strengthening the quality of mobilisation, improving data transparency and ensuring that mobilised finance contributes meaningfully to development outcomes are therefore as important as increasing volumes.

This report is intended to support policymakers, development finance providers and their partners in making more informed, evidence-based decisions on how to deploy scarce public resources to crowd in private investment effectively. By providing robust data, analytical insights and forward-looking recommendations, it aims to contribute to a more coherent, accountable and impactful mobilisation agenda in line with the commitments made at the FFD4 in Sevilla in July 2025. In an increasingly constrained global environment, getting mobilisation right is no longer optional; it is essential.

Pilar Garrido

Carsten Staur

Director

Chair

OECD DCD

OECD DAC

[Signature]

Clark's

## Foreword

More than ten years after the Addis Ababa Action Agenda (2015) called for mobilising all sources of finance to close the Sustainable Development Goal (SDG) financing gap – and in light of the outcomes of the Fourth Financing for Sustainable Development Conference – the time is ripe to take stock of the progress made by official development finance providers in unlocking commercial capital for the SDGs. While private finance has become a strategic priority for many providers, current mobilisation levels fall short of what is needed to meet the accelerating financing gap and the growing needs across the development ecosystem. At the same time, in response to the call for additional resources, development finance providers are increasingly deploying innovative financial structures and mechanisms, often in partnership with private sector actors, peer institutions, and other stakeholders.

Building on the 2023 OECD report Private finance mobilised by official development finance interventions, this edition takes stock of the progress made by development co-operation providers – bilateral and multilateral – to mobilise private finance in support of sustainable development, highlighting the contribution of such finance to key sectors and regions as well as climate action. It also describes providers' portfolios and the instruments they use to mobilise private finance, with a focus on their use of leveraging mechanisms, as well as the main incentives and obstacles they encounter in scaling up private finance for sustainable development, climate and nature-related sectors.

The report draws upon OECD DAC statistics as the international standard for measuring private finance mobilised by official development finance interventions. In response to the Addis Ababa Action Agenda's call for more transparency, and under a high-level mandate from the Development Assistance Committee (DAC), the OECD has been working with experts from bilateral development finance institutions (DFIs) and multilateral development banks (MDBs) as well as the climate community to develop this OECD DAC international standard for measuring and collecting data on the amounts mobilised from the private sector by official development finance interventions. In this context, three methodological points are noteworthy:

\- The term “mobilisation” (or leveraging) refers to the ways in which specific mechanisms stimulate the allocation of additional financial resources for sustainable development; mobilisation requires a demonstrable causal link between finance made available for a specific project and the leveraging instrument used (OECD, 2025, Handbook on Measuring and Reporting on Mobilised Private Finance in OECD DAC Statistics).

\- Data on mobilised private finance have been collected since 2012 for the leveraging mechanisms known to be used by development co-operation providers, among them syndicated loans, guarantees, shares in collective investment vehicles, direct investment in companies, credit lines, project finance and simple co-financing arrangements.

\- The methodologies for reporting on amounts mobilised are defined instrument (or leveraging mechanism) by instrument (OECD, 2025, Handbook on Measuring and Reporting on Mobilised Private Finance in OECD DAC Statistics). They reflect the principles of causality and, in cases where more than one official provider is involved in a project mobilising private finance, pro-rated attribution.

# Acknowledgements

This report was prepared by the OECD Development Co-operation Directorate, headed by Director Pilar Garrido, under the strategic guidance of Haje Schütte, Deputy Director.

The report was elaborated under the direction of Cécile Sangaré, Policy Analyst. It was primarily drafted by Emilia Stazi, Junior Policy Analyst, with Callum Thomas, Junior Policy Analyst, as co-author. Cécile Seguineaud, Chiara Falduto and Fatoumata Ngom also made significant contributions. The report also benefitted from valuable inputs by Wiebke Bartz-Zuccala, Paul Horrocks, Lasse Moller and Raphael Jachnik. Valérie Gaveau, Head of the Statistical Standards and Methods Unit, provided overall direction and strategic guidance throughout the process.

The authors are also grateful to Wiebke Bartz-Zuccala, Chiara Falduto, Paul Horrocks, Raphael Jachnik and Emma Raiteri for peer reviewing the paper. Additionally, they also thank all participating institutions and their representatives for their valuable insights and contributions: Drishti Basi (British International Investment), Magnus Cedergren (Impact Fund Denmark), and Emma Blomqvist, Albert Granholm, Agnes Rova and Camilla Rubensson (Swedish International Development Agency).

## Table of contents

Preface 3   
Foreword 4   
Acknowledgements 5   
Abbreviations and acronyms 8   
Executive summary 9   
1 Trends in private finance mobilisation 11   
Overview 11   
Main beneficiaries 14   
Sectoral distribution 20   
Focus on climate action 26   
References 33   
Notes 36   
2 The private finance mobilisation ecosystem: actors and leveraging mechanisms 37   
Leading providers 37   
Leveraging mechanisms currently captured in DAC statistics 42   
Innovative approaches to private finance mobilisation 48   
References 59   
3 Challenges and opportunities to scale up mobilisation efforts 63   
Development finance providers should undertake to scale up private finance for sustainable development 63   
References 68

## FIGURES

Figure 1.1. Trends in private finance mobilised by official development interventions, 2012-2024 11  
Figure 1.2. Mobilised private finance by leveraging mechanism, 2021-2024 13  
Figure 1.3. Regional distribution of private finance mobilised, categorised by leveraging mechanism, 2021-2024 15  
Figure 1.4. Top 20 recipients of mobilised private finance, 2021-2024 16  
Figure 1.5. Private finance mobilised by multilateral and bilateral providers by income group, 2021-2024 17  
Figure 1.6. Main leveraging mechanisms in fragile contexts and SIDS, 2021-2024 19  
Figure 1.7. Mobilised private finance by category of providers in fragile contexts and SIDS, 2021-2024 19

Figure 1.8. Private finance mobilised by sector, 2021-2024 22  
Figure 1.9. Mobilised private finance towards different areas of climate action, 2021-2024 26  
Figure 1.10. Geographical distribution of mobilised private climate finance by climate action area, 2021-2024 27  
Figure 1.11. Mobilised private finance for climate action, by focus and recipient country income group, 2021-2024 29  
Figure 1.12. Mitigation-related mobilised private finance for the steel, cement and chemical sectors 31  
Figure 1.13. Mitigation-related mobilised private finance for the steel, cement and chemical sectors, by recipient countries 32  
Figure 2.1. Private finance mobilised by DFIs, 2021-2024 37  
Figure 2.2. Mobilised private finance by multilateral development finance providers, 2021-2024 38  
Figure 2.3. Mobilised private finance by bilateral development finance providers, 2021-2024 39  
Figure 2.4. Mobilised private finance by development finance institutions, 2021-2024 40  
Figure 2.5. Typical structured fund capital stack 45  
Figure 2.6. Broadening the scope of mobilisation interventions in OECD statistics 49  
Figure 2.7. Joint MDB-OECD typology of catalytic interventions 57

## BOXES

Box 1.1. Leveraging mechanisms used to mobilise private finance for sustainable development 13  
Box 1.2. Brazil-led Tropical Forest Forever Facility: Creating Investable Pathways for Nature 17  
Box 1.3. Mobilising private finance in conflict-affected contexts: The case of Ukraine 20  
Box 1.4. Private finance mobilised for mini-grid energy projects: the German development agency's mini-grid project in Uganda 24  
Box 1.5. Mobilising private finance towards water and sanitation: the expansion of the As-Samra Wastewater Treatment Plant in Jordan 25  
Box 1.6. Climate Investor Two 28  
Box 2.1. Strengthening financial inclusion in Rwanda: the Sida and Impact Fund Denmark Joint Guarantee Initiative 44  
Box 2.2. The Private Infrastructure Development Group's Emerging Africa and Asia Infrastructure Fund 46  
Box 2.3. Private sector instruments for development 47  
Box 2.4. British International Investment's approach to portfolio mobilisation: the case of Blue Earth Capital 51  
Box 2.5. The Currency Exchange Fund 52  
Box 2.6. Sida's approach to generation: the Sida-IDB Amazon Guarantee 55  
Box 2.7. Emerging typology of catalytic interventions 56  
Box 2.8. Macro-level advisory engagement: the IFC-SECO Crop Receipts Project 57  
Box 2.9. Unlocking mobilisation and catalytic effects: IDB's Social Housing Financing Programme in Ecuador 58

## Abbreviations and acronyms

<table><tr><td>CIV</td><td>collective investment vehicle</td></tr><tr><td>DFI</td><td>development finance institution</td></tr><tr><td>DIC</td><td>direct investment in companies</td></tr><tr><td>EMDEs</td><td>emerging markets and developing economies</td></tr><tr><td>MDB</td><td>multilateral development bank</td></tr><tr><td>NCQG</td><td>New Collective Quantified Goal</td></tr><tr><td>ODA</td><td>official development assistance</td></tr><tr><td>PPA</td><td>power purchase agreement</td></tr><tr><td>PSI</td><td>Private sector instruments</td></tr><tr><td>SPV</td><td>special purpose vehicle</td></tr></table>

# Executive summary

## Key findings

Between 2012 and 2024, official development finance interventions mobilised more than USD 600 billion in private resources, primarily through guarantees (30%), direct investment in companies (25%) and syndicated loans (16%), underscoring the central role of risk-sharing and market-participation instruments in crowding in private capital.

To capture the most recent trends in private finance mobilisation, this report focuses on the period 2021-2024. During this time frame, mobilised private finance displayed a gradual upward trend, peaking at USD 77 billion in 2024. Nevertheless, mobilisation levels remain insufficient relative to projected development needs and to seize available investment opportunities.

\- Regional distribution. Africa accounted for 30% of total mobilised private finance or an average of USD 19.7 billion per year, making it the largest beneficiary region. Latin America and the Caribbean (LAC) ranked second, with 28% of the total (USD 18 billion on average per year). At the country level, Brazil and India emerged as the main recipients, benefiting from approximately USD 6.5 billion and USD 5.7 billion, respectively, of mobilised private finance per year.

\- Risk profile concentration. Mobilisation remained concentrated in markets perceived as less risky, with middle-income but not least developed countries (LDCs) receiving nearly 70% of all mobilised finance. In contrast, only 8% reached low-income countries (LICs), highlighting persistent structural barriers to directing private capital to the most fragile contexts.

\- Sectoral trends. Economic infrastructure and business-related activities attracted 70% of mobilised private finance, while social sectors accounted for just 6%, reflecting ongoing challenges in mobilising private investment at scale in education, health and other social sectors.

\- Mobilised private finance for climate. About 40% of mobilised private finance (USD 26.2 billion per year) supported climate action. Of this amount, nearly 70% focused on mitigation, 22% addressed both mitigation and adaptation, and only 8% focused exclusively on adaptation despite significant and rising adaptation needs in vulnerable countries.

\- Main actors. Multilateral development banks (MDBs) remained the dominant mobilisers, accounting for 71% of total mobilised private finance. At the same time, bilateral providers played a meaningful complementary role, led by the United States (USD 6.5 billion per year on average) and followed by France and the United Kingdom (USD 2.1 billion each), largely through the operations of their respective DFIs.

Recent policy discussions at the Fourth Financing for Development Conference (FFD4) emphasised the need to scale up private finance mobilisation through mechanisms such as joint guarantee programmes, blended finance facilities and thematic bond issuances. These approaches aim to move beyond single-instrument approaches to achieve greater scale and efficiency.

Looking ahead, ongoing analytical work is assessing the feasibility of capturing additional approaches used by development finance providers to mobilise private investment such as catalytic interventions and balance-sheet optimisation (including originate-to-distribute or generation approaches). While statistics on mobilisation will continue to provide a unique source of comprehensive and comparable data series, expanding measurement frameworks could provide a more complete picture of how public development finance supports private capital at scale.

## Key recommendations

\- Development finance providers should further strengthen the comprehensiveness, consistency and transparency of data on mobilised private finance for sustainable development. Improving the quality and granularity of reporting can help build investor confidence, reduce information asymmetries, and narrow the gap between real and perceived investment risks in developing countries, particularly in higher-risk contexts.

\- Policymakers are encouraged to collectively uphold the highest inte

[中间内容因长度限制已省略]

stakeholders, alongside capacity building across the ecosystem, remains critical to advancing the development and uptake of these instruments (OECD, 2025[6]).

Addressing the challenges faced by investors in developing countries and scaling up the volumes of mobilised private finance to close the SDG and climate finance gaps will therefore require a more profound and radical shift in providers' portfolios and approach in the coming years. Experience sharing between providers (e.g. to develop green bond ecosystems to attract private investors) could help drive behavioural change and contribute to strengthening institutions' financial capacities and expertise. More comprehensive reporting and full disclosure on co-financing schemes involving private finance would support peer learning in this area and contribute to building trust in the markets and reducing the risk perception. These structural challenges require effective deployment of blended finance approaches including technical assistance programmes, local currency financing and sustainable outcome bonds (e.g. GSSS bonds) (Dembele, Schwarz and Horrocks, 2021[14]; OECD, 2025[15]).

## References

Dembele, F., R. Schwarz and P. Horrocks (2021), “Scaling up Green, Social, Sustainability and Sustainability-linked Bond Issuances in Developing Countries”, OECD Development Perspectives, No. 11, OECD Publishing, Paris, https://doi.org/10.1787/8a5c3156-en.

Falduto, C., J. Noels and R. Jachnik (2024), The New Collective Quantified Goal on climate finance: Options for reflecting the role of different sources, actors, and qualitative considerations, OECD Publishing, Paris, https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/05/the-new-collective-quantified-goal-on-climate-finance\_b2ac72e8/7b28309b-en.pdf.

Horrocks, P. et al. (2025), “Unlocking local currency financing in emerging markets and developing economies: What role can donors, development finance institutions and multilateral development banks play?”, OECD Development Co-operation Working Papers, No. 117, OECD Publishing, Paris, https://doi.org/10.1787/bc84fde7-en.

OECD (2026), Global Debt Report 2026: Sustaining Debt Market Resilience Under Growing Pressure, OECD Publishing, Paris, https://doi.org/10.1787/e9d80efd-en.

OECD (2025), “FDI in Figures”, OECD Publishing, Paris,
https://www.oecd.org/en/publications/fdi-in-figures-april-2025\_d5a76fd0-en.html.

OECD (2025), Global Outlook on Financing for Sustainable Development 2025: Towards a More Resilient and Inclusive Architecture, OECD Publishing, Paris, https://doi.org/10.1787/753d5368-en.

OECD (2025), Increasing development finance efforts to scale private finance mobilised and its impact, OECD Publishing, Paris, https://doi.org/10.1787/345b768b-en. [4]

OECD (2025), “Mobilising private finance for development, climate and biodiversity in emerging markets and developing economies: Financing our futures”, OECD Business and Finance Policy Papers, No. 91, OECD Publishing, Paris, https://doi.org/10.1787/ada2dfcd-en.

OECD (2025), OECD DAC Blended Finance Guidance 2025, Best Practices in Development Co-operation, OECD Publishing, Paris, https://doi.org/10.1787/e4a13d2c-en. [5]

OECD (2025), Supporting emerging markets and developing economies in developing their local capital markets, OECD Publishing, Paris, https://doi.org/10.1787/4456de62-en. [6]

OECD (2024), Multilateral Development Finance 2024, OECD Publishing, Paris, https://doi.org/10.1787/8f1e2b9b-en.

OECD (2023), “A supervisory framework for assessing nature-related financial risks: Identifying and navigating biodiversity risks”, OECD Business and Finance Policy Papers, No. 33, OECD Publishing, Paris, https://doi.org/10.1787/a8e4991f-en.

OECD (2023), “Private finance mobilised by official development finance interventions”, OECD Development Perspectives, No. 29, OECD Publishing, Paris, https://doi.org/10.1787/c5fb4a6c-en.

OECD (forthcoming), Blended Finance Guidance for Climate Change Adaptation, OECD Publishing, Paris. [8]

World Bank (2024), “Scaling Up Co-Financing for Greater Development Impact”, https://www.worldbank.org/en/news/feature/2024/04/23/scaling-up-co-financing-for-greater-development-impact. [2]

## Private Finance Mobilisation Report 2026

As public budgets tighten and development needs grow, private finance mobilised through public resources has become a central pillar of sustainable development efforts. This report provides the most comprehensive and internationally comparable evidence to date on how mobilisation supports sustainable development outcomes.

Drawing on OECD Development Assistance Committee (DAC) statistics, the report analyses recent trends in private finance mobilisation across regions, sectors, instruments and providers. It highlights where mobilisation has increased, where progress has stalled, and which markets and sectors continue to face persistent financing gaps. The analysis shows that while mobilisation volumes have grown over time, results remain concentrated in a limited number of instruments, providers and countries, raising important questions about scalability and effectiveness.

The report emphasises the importance of improving the quality, transparency and targeting of mobilisation efforts. It sheds light on which financial instruments tend to mobilise the most private capital, where risk-sharing remains insufficient, and how public resources can be used more strategically to crowd in private investment. The report is intended for policymakers, development finance institutions and partners seeking evidence-based insights to strengthen mobilisation approaches and ensure that scarce public resources deliver meaningful development impact.
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
