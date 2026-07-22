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
# Financing Southeast Asia's Blue Economy

Development Assistance and Beyond

![](images/ed6d61f3c9193b3952bcd46739e287a0ed17d48cdcefac93e085f7db93b145aa.jpg)

# Financing Southeast Asia's Blue Economy

DEVELOPMENT ASSISTANCE AND BEYOND

This work is issued under the responsibility of the Secretary-General of the OECD, and does not necessarily reflect the official views of OECD Member countries.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

Please cite this publication as: OECD (2026), Financing Southeast Asia's Blue Economy: Development Assistance and Beyond, OECD Publishing, Paris, https://doi.org/10.1787/5371e508-en.

ISBN 978-92-64-72029-9 (print)
ISBN 978-92-64-83104-9 (PDF)
ISBN 978-92-64-93203-6 (HTML)

Photo credits: Cover © Vietnam Stock Images/Shutterstock.com.

Corrigenda to OECD publications may be found at: https://www.oecd.org/en/publications/support/corrigenda.html.
© OECD 2026

![](images/e29d4d6b7bed0b6c3dcb4cafd6a63bba919943a74db6860aef8b26c6865b3ed2.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of the original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

# Foreword

Comprising eleven countries (Brunei Darussalam, Cambodia, Indonesia, Lao People's Democratic Republic, Malaysia, Myanmar, the Philippines, Singapore, Thailand, Timor-Leste and Viet Nam), the Southeast Asia region has experienced rapid economic growth, emerging as the world's fourth-largest economic bloc in 2024. Important to this trajectory is the region's blue economy – the economic activities tied to coastal, marine and freshwater resources. Even as it presents opportunities, the region's blue economy faces mounting pressures and transitional risks. A range of stressors - including overfishing, marine pollution, habitat destruction and climate change - has undermined the resilience of Southeast Asia's blue ecosystems. At the same time, the global shift toward low-carbon economies poses transition risks, as stricter climate policies and changing market preferences may reduce demand for carbon-intensive marine activities and expose certain sectors to economic disruption. Addressing these threats and transition risks is, therefore, essential for the near and long-term outlook of Southeast Asia's blue economy.

Effective financial capital allocation is needed to navigate these opportunities and challenges, but the region faces a financing gap of nearly USD 2.1 trillion through 2030. Cognisant of this, the Association of Southeast Asian Nations (ASEAN) – which brings together all eleven Southeast Asian countries, with Timor-Leste joining in 2025 – has elevated the blue economy on the regional policy agenda, with member states pursuing a co-ordinated approach since the 2021 ASEAN Leaders' Declaration on the Blue Economy. A key milestone was the adoption of the ASEAN Blue Economy Framework in 2023. An overarching policy blueprint, the Framework provides a structured articulation of the region's blue economy priorities and elaborates on key considerations for operationalising them.

In particular, the Framework identifies “sustainable investment and finance” as an enabler of blue economy development in Southeast Asia, acknowledging that adequate and well-targeted financial resources are necessary for the implementation of the Framework’s strategic priorities. Overall, there is a strong focus on the need to reduce reliance on development assistance and instead shift towards a longer-term approach to blue economy finance and investment. This report – a landscape study of finance and investment for the blue economy in Southeast Asia – aims to support ASEAN and its member states in this endeavour, helping illustrate opportunities and challenges in diversifying away from development assistance as a source of blue economy finance.

This report starts with a review of key trends in the blue economy in Southeast Asia (Chapter 1). It then delves into the current landscape of official development assistance (Chapter 2) – the rationale being that unpacking the precise nature of finance diversification requires understanding what Southeast Asia is diversifying from. Next, it analyses the other sources of blue economy finance and investment to highlight not only their use cases, but also the barriers that the region faces in accessing them (Chapter 3). It then shifts to the solutions to these barriers – innovative mechanisms and instruments that may unlock other sources of capital – detailing case studies and lessons learned (Chapter 4). It concludes with a synthesis of findings, providing recommendations for the national and regional level, as well as for development partners (Chapter 5).

# Acknowledgements

This publication was prepared under the leadership of María del Pilar Garrido Gonzalo, Director of the OECD Development Co-operation Directorate, in close co-ordination with the OECD's Southeast Asia Regional Programme, led by Andreas Schaal, Director of the Global Relations and Co-operation Directorate.

Shashwat Koirala (Economist) led the co-ordination and drafting of the report, with contributions from Gabriele Crisfoaro (Junior Policy Analyst). The work was supervised by Jens Sedemund (Head of the Climate, Biodiversity and Sustainable Ocean Unit) with strategic guidance from Eva Beuselinck (Head of the Policies and Networks Division) – both within the OECD's Development Co-operation Directorate. Strategic steer in stakeholder engagement was provided by colleagues from the OECD's Global Relations and Co-operation Directorate: Alexander Bohmer (Head of the Southeast Asia Division), Max Bulakovskiy (Head of the Project Implementation Unit), Hans Koger (Junior Policy Analyst) and Marta Bertanzetti (Junior Policy Analyst). Harsh Desai (Acting Head of the Statistical Collections and Dissemination Unit, Development Co-operation Directorate) provided guidance on generating forecasts of official development assistance for the ocean economy. Meral Gedik provided editorial support and prepared the report for publication.

The report was informed by discussions and insights gathered through engagement with stakeholders involved in developing and implementing the ASEAN Blue Economy Framework and its subsequent implementation plan. Two milestones, in particular, offered opportunities for engagement and information-gathering: the Intersessional Meeting of the ASEAN Co-ordinating Task Force on Blue Economy (August 2025) and the ASEAN Blue Economy Forum (September 2025). The author is grateful for the partnership of the ASEAN Secretariat – Kanchana Wanichkorn, Arief Rizky Bakhtiar, Soon Hong Kwan and Latifahaida Abdul Latif – and the Economic Research Institute for ASEAN and East Asia – Intan M. Ramli – in facilitating engagement with these fora, as well as for their substantive input during the development of the report. Thanks are also due to Michelle Voyer of the Australian National Centre for Ocean Resources & Security and Kelly Hoareau of the Blue Economy Cooperative Research Centre and the blue economy focal points of ASEAN member states for their inputs and insights.

Feedback from the following OECD colleagues is also gratefully acknowledged: Claire Jolly, James Jolliffe, Bophha Chhuun, Emma Raitiri, Hans Koger and Sergio Giorgana Ampudia. Comments and input from the following members of the Development Assistance Committee's Network on Environment and Development Co-operation also helped inform the report: Italy, the European Union and New Zealand.

The report also benefited from exchanges and meetings held at several international conferences, namely the International Maritime Organisation's Innovation Forum (October 2024), the Great Ocean Dialogue (November 2024), the Finance in Common Summit (February 2025), the Our Ocean Conference (April 2025) and the Third United Nations Ocean Conference (June 2025).

The report was made possible by the generous voluntary contribution of the Government of Italy.

## Table of contents

Foreword 3   
Acknowledgements 4   
Abbreviations and acronyms 8   
Executive summary 9   
1 Blue economy trends and pressures in Southeast Asian countries 11   
1.1. The blue economy is prominent in Southeast Asia, but it faces structural and transition challenges 13   
1.2. Environmental degradation threatens blue ecosystems and the economic activities they sustain 17   
1.3. ASEAN's regional policy response is constrained by insufficient long-term finance and investment 21   
References 24   
Notes 26   
2 Development assistance: A crucial but constrained basis for blue economy finance 27   
2.1. Development assistance is vital despite its small share of the overall finance mix 28   
2.2. Ocean-related ODA to Southeast Asia shows problematic patterns in scale, allocation and delivery 33   
2.3. Declining aid budgets increase the urgency of mobilising alternative capital sources 40   
References 42   
Notes 43   
3 Diversifying blue economy finance: Opportunities and constraints across alternative sources 44   
3.1. Different capital types serve distinct purposes, but their flow to ASEAN's blue economy is poorly tracked 45   
3.2. Macroeconomic conditions create uneven availability of capital for the blue economy across Southeast Asia 48   
3.3. Even when available, capital may not always flow to Southeast Asia's blue economy due to policy gaps 56   
References 60   
Note 63

4 Financing solutions: Tools and lessons learned 64
4.1. Blended finance can mitigate individual capital availability challenges but has achieved limited success 65
4.2. Innovative instruments could ease capital constraints, but adoption remains patchy in Southeast Asia 68
4.3. Viability of these instruments is not guaranteed – making development support and hence additionality essential 76
References 84
Notes 88
5 Synthesis of recommendations 89
5.1. National level: Build the foundation for blue economy finance 90
5.2. ASEAN-level: Translate regional policies to co-ordinated action 91
5.3. Development partners: Maximise value in a constrained environment 92
References 94

## FIGURES

Figure 1.1. Southeast Asia's GDP over time 12
Figure 1.2. Contribution of ocean economy to the overall economy 14
Figure 1.3. Sectoral composition of Southeast Asia and Oceania's ocean economy in 2020 15
Figure 1.4. Composition of Southeast Asia and Oceania's ocean economy, in terms of gross value added, over time 16
Figure 1.5. Southeast Asia and Oceania's share of the global ocean economy, in terms gross value added 17
Figure 1.6. Fish stock status, according to the Yale Environmental Performance Index 18
Figure 1.7. Plastic use in ASEAN countries 19
Figure 1.8. Number of climatological, geophysical, hydrological and meteorological natural disasters, 2000-2025 20
Figure 1.9. The ASEAN Blue Economy Framework 22
Figure 2.1. ODA as a share of the overall financing mix of Southeast Asian countries 28
Figure 2.2. ODA as a share of the financial inflows and tax revenues across ODA-eligible Southeast Asian countries 31
Figure 2.3. Barriers to finance and investment for the blue economy 32
Figure 2.4. Framework for measuring ocean-related ODA 33
Figure 2.5. Ocean-related ODA over time to ASEAN 34
Figure 2.6. Sectoral distribution of ocean-related ODA to ASEAN 2022-2023 35
Figure 2.7. Commitments versus disbursements 36
Figure 2.8. Share of commitments from 2010-2013 disbursed as of 2023 37
Figure 2.9. Loans and grants over time in ocean-relevant ODA 38
Figure 2.10. Ocean-related ODA versus size of EEZ and length of coastline 39
Figure 2.11. Ocean-related ODA versus share of ODA in overall financing mix 39
Figure 2.12. Early projections of DAC members ocean-related ODA to Southeast Asia 41
Figure 3.1. Different capital types mapped to the strategic pillars of the ASEAN Blue Economy Framework 45
Figure 3.2. Philanthropic contributions to SDG14 in Southeast Asia 48
Figure 3.3. Downward adjustment of Southeast Asia's economic outlook 49
Figure 3.4. Tax-to-GDP ratio across Southeast Asian countries 50
Figure 3.5. Quality of public finance management according to the PEFA indices 52
Figure 3.6. FDI flows to and stocks in Southeast Asia 53
Figure 3.7. FDI Restrictiveness Index across Southeast Asian countries 54
Figure 3.8. Availability of domestic private capital 55
Figure 3.9. Financial inclusion across Southeast Asia 56
Figure 4.1. Blended finance instruments 65
Figure 4.2. Private finance mobilised by ODA for ocean-related activities in Southeast Asia 66
Figure 4.3. Blended finance instruments for ocean-related activities in Southeast Asia 67
Figure 4.4. Blue bonds and its relation to other use-of-proceed bonds 68
Figure 4.5. Sustainable bond Issuance as Share of Total Bond Issuance in Q2 2025 70
Figure 4.6. Debt-for-nature swap architecture 71

Figure 4.7. Mean annual carbon sequestration potentials 74  
Figure 4.8. The Seychelles sovereign blue bond 77  
Figure 4.9. Belize blue bond transaction structure 78  
Figure 4.10. The "Five Is" framework: Policy areas where donors can support GSSS bond issuances 82

## TABLES

Table 1.1. List of ocean economic activities, both established and emerging 13  
Table 1.2. Blue economy finance gap to meet the Sustainable Development Goals by 2030 in the Asia Pacific 23  
Table 2.1. Eligibility of Southeast Asian countries for development finance 30  
Table 3.1. Count of ocean-relevant economic environmental policy instruments in Southeast Asian countries 47  
Table 3.2. Level of blue economy policy development across Southeast Asian countries 57  
Table 3.3. Southeast Asian countries with ocean-related measures in their 2025 NDCs 58  
Table 4.1. Blue carbon ecosystems: global extent, rates of conversion, estimated carbon dioxide (CO₂) emissions due to human activities, and their estimated costs 73  
Table 4.2. Parametric insurance programmes in the Caribbean 76

## BOXES

Box 1.1. What is the blue economy? 13  
Box 2.1. Eligibility for and access to development finance 29  
Box 3.1. Non-profit seeking private capital: Remittances and philanthropic contributions 46  
Box 3.2. Debt sustainability and Lao PDR 51  
Box 4.1. Belize debt-for-nature-swap 78  
Box 4.2. What is marine spatial planning 81  
Box 4.3. The “Five Is” Framework: Donor support to green, social, sustainability and sustainability-linked (GSSS) bond issuances 82

## Abbreviations and acronyms

<table><tr><td>ADB</td><td>Asian Development Bank</td></tr><tr><td>ACMF</td><td>ASEAN Capital Markets Forum</td></tr><tr><td>ASEAN</td><td>Association of Southeast Asian Nations</td></tr><tr><td>CCRIF SPC</td><td>Caribbean Catastrophe Risk Insurance Facility Segregated Portfolio Company</td></tr><tr><td> $CO_2$ </td><td>Carbon dioxide</td></tr><tr><td>COAST</td><td>Caribbean Oceans and Aquaculture Sustainability Facility</td></tr><tr><td>DAC</td><td>Development Assistance Committee</td></tr><tr><td>DFC</td><td>United States International Development Finance Corporation</td></tr><tr><td>DFNS</td><td>Debt-for-nature swap</td></tr><tr><td>EEZ</td><td>Exclusive economic zone</td></tr><tr><td>ESG</td><td>Environmental, social and governance</td></tr><tr><td>EPI</td><td>Environmental Performance Index</td></tr><tr><td>FDI</td><td>Foreign direct investment</td></tr><tr><td>FTE</td><td>Full-time equivalent</td></tr><tr><td>GDP</td><td>Gross domestic product</td></tr><tr><td>GSSS</td><td>Green, social, sustainability and sustainability-linked</td></tr><tr><td>GVA</td><td>Gross value added</td></tr><tr><td>IBRD</td><td>International Bank for Reconstruction and Development</td></tr><tr><td>IDA</td><td>International Development Association</td></tr><tr><td>IDB</td><td>Inter-American Development Bank</td></tr><tr><td>IFC</td><td>International Finance Corporation</td></tr><tr><td>IUU</td><td>Illegal, unreported and unregulated (fishing)</td></tr><tr><td>Lao PDR</td><td>Lao People&#x27;s Democratic Republic</td></tr><tr><td>LDC</td><td>Least developed country</td></tr><tr><td>LIC</td><td>Low-income country</td></tr><tr><td>LMIC</td><td>Lower middle-income country</td></tr><tr><td>MDB</td><td>Multilateral development bank</td></tr><tr><td>MPA</td><td>Marine protected area</td></tr><tr><td>MSP</td><td>Marine spatial planning</td></tr><tr><td>NDC</td><td>Nationally Determined Contribution</td></tr><tr><td>NGO</td><td>Non-governmental organisation</td></tr><tr><td>OCR</td><td>Ordinary Capital Resources</td></tr><tr><td>ODA</td><td>Official development assistance</td></tr><tr><td>ODF</td><td>Official development finance</td></tr><tr><td>OECD</td><td>Organisation for Economic Co-operation and Development</td></tr><tr><td>OOF</td><td>Other official flows</td></tr><tr><td>PEFA</td><td>Public Expenditure and Financial Accountability</td></tr><tr><td>PES</td><td>Payment for ecosystem services</td></tr><tr><td>SDG</td><td>Sustainable Development Goal</td></tr><tr><td>SLB</td><td>Sustainability-linked bonds</td></tr><tr><td>TCFD</td><td>Task Force on Climate-Related Financial Disclosure</td></tr><tr><td>TFCCA</td><td>Tropical Forest and Coral Reef Conservation Act</td></tr><tr><td>THB</td><td>Thai baht</td></tr><tr><td>UMIC</td><td>Upper middle-income country</td></tr><tr><td>UNEP FI</td><td>United Nations Environment Programme Finance Initiative</t

[中间内容因长度限制已省略]

ically to enable countries to access other sources of capital, particularly for commercially viable blue economy projects that face excessive risk premiums due to weak enabling environments. The European Fund for Sustainable Development Plus is one example of this approach. However, the core principles of effective blended finance – prioritising development impact and public value, focusing on mobilising commercial finance, tailoring efforts to the local context, strengthening partnerships and monitoring for transparency and results – all apply.

\- Supporting the establishment of blue finance instruments when aligned with country priorities and demonstrating clear additionality: Blue finance instruments can form part of the broader financing solution for Southeast Asia's blue economy. While they may represent a pathway towards financial autonomy, they often remain contingent on development partner support. Channelling development assistance towards these instruments may be justified in certain contexts, but this requires clear alignment with recipient countries' priorities and needs, as well as demonstrable additionality beyond what traditional instruments can achieve.

## 5.3.2. Seek co-benefits across blue economy and broader sustainable development goals

Effectiveness in a resource-constrained environment requires strategic integration at project and policy levels. Development partners can actively pursue co-benefits across ocean health, climate, biodiversity and development objectives. While these are often treated as separate issue areas with distinct financing streams and institutional mandates, they are fundamentally interconnected. Climate finance can support blue carbon ecosystems like mangroves and seagrass beds that simultaneously sequester carbon, protect coastlines from storms and provide nursery habitat for commercially important fish species. Biodiversity finance can strengthen coastal resilience and support livelihoods of fishing communities. Blue economy investments can advance multiple Sustainable Development Goals (SDG) simultaneously – SDG 14 on oceans, SDG 13 on climate, SDG 1 on poverty and SDG 8 on economic growth.

This integrated approach maximises the impact of scarce resources by designing interventions that generate multiple benefits rather than optimising for single objectives.

## References

ADB (2023), Bonds to Finance the Sustainable Blue Economy: A Practitioner's Guide, Asian Development Bank, Manila, https://www.adb.org/publications/bonds-finance-sustainable-blue-economy-practitioners-guide.

ADB (n.d.), ASEAN Infrastructure Fund, https://www.adb.org/what-we-do/funds/asean-infrastructure-fund.

ADB (n.d.), Blue SEA Finance Hub, https://www.adb.org/what-we-do/themes/environment/bluesea.

ASEAN Capital Markets Forum (2025), ACMF Action Plan 2026-2030, https://www.sc.com.my/api/documentms/download.ashx?id=084b473a-84f3-4af5-918b-9c99cd09f3fa.

ASEAN Capital Markets Forum (2025), ASEAN Simplified ESG Disclosure Guide Version 1, https://www.theacmf.org/initiatives/sustainable-finance/asean-simplified-esg-disclosure-guide-version-1.

ASEAN Capital Markets Forum (2017), The ASEAN Corporate Governance Scorecard, https://www.theacmf.org/initiatives/corporate-governance/the-asean-corporate-governance-scorecard.

CBD (2025), Sustainable Ocean Initiative, https://www.cbd.int/soi/.

Coral Triangle Initiative (2026), Frequently Asked Questions, https://www.coraltriangleinitiative.org/frequently-asked-questions-0.

European Commission (n.d.), BlueInvest, https://maritime-forum.ec.europa.eu/theme/investments/blueinvest\_en.

OECD (2025), Promoting Sustainable Ocean Economies: Guidance for Development Co-operation, Best Practices in Development Co-operation, OECD Publishing, Paris, https://doi.org/10.1787/72055d7f-en.

Pacific Community (2024), Unlocking Blue Pacific Prosperity: Co-designing our Future for Resilient Ecosystems, Robust Food Systems and Thriving People, https://spccfpstore1.blob.core.windows.net/digitallibrary-docs/files/68/687f76b4074847552719d0344e47b741.pdf?sv=2015-12-11&sr=b&sig=p9JfD%2BYutUKnVbKSZ%2BkxVnL8jj1xJEp3cPqe%2F7ZNbfA%3D&se=2026-08-19T20%3A58%3A49Z&sp=r&rscc=public%2C%20max-age%3D864000%2C%.

The Commonwealth (2026), Commonwealth Blue Charter, https://thecommonwealth.org/bluecharter.

UNDP (2025), Biodiversity Finance Initiative, https://www.biofin.org/.

World Bank (2021), Blue Public Expenditure Review Guidance Note, https://documents1.worldbank.org/curated/en/789491639977748921/pdf/Blue-Public-Expenditure-Review-Guidance-Note.pdf.

# Financing Southeast Asia's Blue Economy

## Development Assistance and Beyond

Southeast Asia's development trajectory is closely intertwined with its blue economy – a diverse range of economic activities reliant on and non-market ecosystem services provided by the region's rich coastal, marine, and freshwater resources. However, as highlighted in the ASEAN Blue Economy Framework, the overarching policy guiding Southeast Asia's blue economy priorities, adequate and effective finance and investment are essential for the region to realise the potential of the blue economy for sustainable development. A key consideration is the need to move beyond excessive reliance on development assistance towards longer-term financing solutions, particularly in light of increasing pressures on international public finance. To support this shift and the implementation of the ASEAN Blue Economy Framework, this report assesses the current landscape of development assistance for the blue economy in Southeast Asia and examines the range of financial sources and instruments that can be leveraged to advance sustainable blue economy financing in the region.
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
