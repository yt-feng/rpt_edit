你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
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
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
TOWARD MORE LIVABLE CITIES
IN THE HINDU KUSH HIMALAYAS

LESSONS FROM THE NEXUS OF AFFORDABLE AND SEISMIC-RESILIENT HOUSING IN BHUTAN, THE INDIA-HIMALAYA REGION, AND NEPAL

Jude E. Kohlhase, Saswati G. Belliappa, and Charlene Liau

NO. 104

July 2026

ADB SOUTH ASIA

WORKING PAPER SERIES

# Toward More Livable Cities in the Hindu Kush Himalayas: Lessons from the Nexus of Affordable and Seismic-Resilient Housing in Bhutan, the India-Himalaya Region, and Nepal

Jude E. Kohlhase, Saswati G. Belliappa, and Charlene Liau

No. 104 | July 2026

The ADB South Asia Working Paper Series presents ongoing and recently completed research and policy studies meant to enhance greater understanding of and promote dialogue on current important economic and development issues in South Asia. The views expressed are those of the authors and do not necessarily reflect the views and policies of ADB or its Board of Governors or the governments they represent.

Jude E. Kohlhase is a principal portfolio management specialist at the Office of Business Intelligence and Operations Coordination, Asian Development Bank (ADB). Saswati G. Belliappa is a principal safeguards specialist at the Office of Safeguards (ADB). Charlene Liau is a results management specialist at the Strategy, Policy, and Partnerships Department (ADB).

© 2026 Asian Development Bank

6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines

Tel +63 2 8632 4444; Fax +63 2 8636 2444

www.adb.org

Some rights reserved. Published in 2026.

ISSN 2313-5867 (print), 2313-5875 (PDF)

Publication Stock No. WPS260311-2

DOI: http://dx.doi.org/10.22617/WPS260311-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed to another source, please contact the copyright owner or publisher of that source for permission to reproduce it. ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use the ADB logo.

The ADB South Asia Working Paper Series is a forum for ongoing and recently completed research and policy studies undertaken in ADB or on its behalf. It is meant to enhance greater understanding of current important economic and development issues in South Asia, promote policy dialogue among stakeholders, and facilitate reforms and development management.

The ADB South Asia Working Paper Series is a quick-disseminating, informal publication whose titles could subsequently be revised for publication as articles in professional journals or chapters in books. The series is maintained by the South Asia Department. The series will be made available on the ADB website and on hard copy.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

## Notes:

In this publication, “\$” refers to United States dollars and “₹” refers to Indian rupees. ADB recognizes “Vietnam” as Viet Nam.

## CONTENTS

TABLES, FIGURES, AND BOXES
ACKNOWLEDGMENTS
ABBREVIATIONS
EXECUTIVE SUMMARY
I. INTRODUCTION
Regional Context
Purpose and Method
II. SEISMIC RISK IN THE HINDU KUSH HIMALAYA REGION
Seismic Risk
Main Messages
III. URBANIZATION IN BHUTAN, THE INDIA-HIMALAYA REGION, AND NEPAL
Urbanization Trends
Economic Importance of Urban Areas
Role of Mid-Weight and Intermediate Towns
Urban Policies, Spatial Planning, and Risk Information
Bhutan's Urbanization Challenges
India's Urbanization Challenges
Nepal's Outlook on Urbanization
Main Messages
IV. HOUSING AFFORDABILITY AND SEISMIC RISK IN BHUTAN,
THE INDIA-HIMALAYA REGION, AND NEPAL
Overview
Housing Institutions and Policies
Housing Conditions of the Urban Poor and Policy Responses
Adequate Housing and Backlogs
Housing Affordability in Bhutan
De Facto Housing
Housing Typologies and Earthquakes
Main Messages

V. ROAD MAP FOR SUPPORTING AFFORDABLE AND SEISMICALLY RESILIENT HOUSING IN THE HINDU KUSH HIMALAYA REGION
Overview
Recommendations for Strategy 2030
43
44
BIBLIOGRAPHY
46

# TABLES, FIGURES, AND BOXES

## TABLES

1 Urbanization in India and the India–Himalaya Region States, 2011 7
2 Earthquake Damages for Kangra District, Himachal Pradesh 22
3 Share of Urban Population Living in Slum Conditions in the Hindu Kush Himalaya Region 26
4 Earthquake-Safe Traditional Construction Practices in the India–Himalaya Region 36

## FIGURES

1 Geomorphological Features of Hindu Kush Himalaya Region 4  
2 The Housing Value Chain 16  
3 Indonesia InaRisk Platform: Risk Assessment for Earthquakes 42

## BOXES

1 Salient Features of India's National Urban Housing and Habitat Policy 2007 20  
2 Self-Built Housing Under the Pradhan Mantri Awas Yojana Urban Mission: Dharamshala, Himachal Pradesh 21  
3 Overview of Acts and Policies in Nepal 24  
4 Housing Conditions of the Urban Poor, Shimla City, Himachal Pradesh, India Himalaya Region 28  
5 Integrating Affordability, Resilience, and Convergence: India's Evolving Urban Housing Framework 30  
6 Typical Urban Housing Typologies, Thimphu, Bhutan 34  
7 Generalized Building Typologies and Seismic Performance 37

# ACKNOWLEDGMENTS

The team leading this paper from the Asian Development Bank (ADB), Jude Kohlhase, principal portfolio management specialist of the Office of Business Intelligence and Operations Coordination; Saswati Ghosh Belliappa, principal safeguards specialist (Social), Office of Safeguards; and Charlene Liau, results management specialist, Strategy, Policy, and Partnerships Department, would like to express gratitude to the management of ADB's Water and Urban Development Sector Office (SD2-WUD) within the Sector Department 2 for their guidance, supervision, and support, most especially to Norio Saito, senior director, SD2-WUD and Manoj Sharma, director, SD2-WUD.

Preparation of this paper benefited from insightful feedback from peer reviewers Ramola Naik Singru, principal urban development specialist; and Hong Soo Lee, senior urban development specialist. We are grateful for the review comments provided by Sonomi Tanaka, country director; and Sonam Lhendup, senior economics officer, Bhutan Resident Mission. The team thanks Arnaud Cachois, country director; and Malika KC Thapa, operations assistant, Nepal Resident Mission, for their support and coordination with the Government of Nepal. We are also grateful to Rajesh Deol, principal communications officer; K. Balaji, associate operations officer; and Poornima Prasad, executive assistant, India Resident Mission, for coordinating the review by the Government of India.

This paper is based on inputs from the following ADB consultants: Colleen Butcher-Gollach, Charles Scawthorn, Deependra Pourel, Banashree Banerjee, and Sanjaya Pradhan—under the support of the Implementation of Strategy 2030 Operational Plans Technical Assistance. The team also thanks Ruthcelyn U. Francisco, ADB consultant, for coordinating the clearances and editing process.

## ABBREVIATIONS

ADB Asian Development Bank
COVID-19 coronavirus disease
GDP gross domestic product
HKH Hindu Kush Himalaya
km kilometer
MFI microfinance institution
MOHUA Ministry of Housing and Urban Affairs
MPI multidimensional poverty index
NHDCL National Housing Development Corporation Limited
PMAY-U Pradhan Mantri Awas Yojana-Urban
PRC People's Republic of China

# EXECUTIVE SUMMARY

Context. The Hindu Kush Himalaya (HKH) region stretches 3,500 kilometers (km) eastward through Afghanistan, Pakistan, the People's Republic of China (PRC), Nepal, India, Bangladesh, Bhutan, and into Myanmar. $^{1}$ It is vast and home to many glaciers. This natural “water tower of Asia” feeds the Indus, Ganges, and Brahmaputra (known as the Yarlung Zangbo in the PRC). These rivers support a rich biodiversity and the livelihoods and economies of more than a billion people. In this working paper, the Asian Development Bank (ADB) assesses the seismicity of the region and the policies and practices affecting the supply of affordable and seismic-resilient housing in India, Bhutan, and Nepal. India stands as the largest country with a staggering population of 1.46 billion. However, this study is focused on the Indian Himalayan Region within the HKH, comprising an estimated 8% of India's total population. In contrast, Bhutan is the smallest country, with a population of 800,000. Nepal, with a population of 29.6 million, is notably one of the poorer countries in the region.

Strategic challenge. Rapid population growth in seismically hazardous areas requires meeting the challenges of supplying affordable housing and reducing seismic risk. The Himalayan uplift is a result of tectonic plate movements that occurred 50 million years ago and continue to this day. The region is characterized by a concentration of ongoing seismic activity that impacts the lives, buildings, and assets of residents, and that impact is compounded by accelerating glacial melt and associated breach floods and landslides as a result of global warming. In addition to their common seismic hazard risk, the populations living in the widely disparate countries along the Himalayan arc face the additional shared challenge of adequate, affordable housing. A recorded 446 million people live in unplanned slums and informal settlements in the eight countries, comprising nearly 45% of the world's total number of people living in poor housing conditions.

The population of these seismically hazardous areas of Asia increased by 21% between 2000 and 2015, a 3.4% faster growth rate than that of less seismically hazardous areas. This growth is stretching the respective countries' resources for planning and financing the supply of well-located and safe land, infrastructure, and climate-resilient housing to meet the demands of the burgeoning population.

Housing value chain. The efficient supply of formal housing to meet demand at affordable prices in the volume needed to keep abreast with urban growth is the result of the interactions and coordination between public and private sector value chain activities. As countries' urban populations grow from natural population growth and in-migration for economic and other opportunities, bottlenecks are exacerbated, and housing prices are expected to continue to increase as the demand-supply gap widens. In the three countries analyzed, the supply-side activity of providing households and developers with access to consolidated blocks of land that are appropriately located, planned, and zoned for residential purposes, with climate-proofed infrastructure and other municipal services, is predominantly carried out by the public sector. However, the design, financing, and construction of houses are largely taken up by the private sector.

Disconnect in knowledge, policies, financial services, and practices to achieve affordable and seismically resilient housing. The housing markets of the three countries represent a disconnect in the knowledge, policies, and practices needed to achieve an adequate housing supply that meets the needs and affordability levels of lower-income groups. Another challenge is ensuring that such housing is in safe areas and that the design costs imposed by standards for seismic risk-resilient homes do not add to the rental stress of households, where housing costs exceed 30% of household income.

Housing affordability gap. In Bhutan's two largest cities (thromdes), rental stress is a burden on households across almost all Thimphu and Phuentsholing suburbs. On average, the rent-to-income ratio is 42% for women-headed families and 33% for men-headed families living in officially sanctioned housing in almost all the suburbs of Thimphu. The median rent-to-income ratio in Phuentsholing is a high 42.5%. Nationwide, the median rent-to-income ratio for privately rented housing is 27.5% and is notably higher than the ratio for public sector housing, which in the past has been subsidized. However, affordability varies for different income groups. Rental stress is felt most by the poorest 20% of households across Bhutan's thromdes, by the near-poor households (20%-40% income quintile), and middle-income households (in the third quintile) in Phuentsholing, Paro, Gelephu, and Thimphu.

In India, while the urban housing stock has grown consistently, the urban housing shortage has also risen over time. In India's Himalaya region states, $56\%$ of the population classified as economically weaker faces a housing shortage. Similarly in Nepal, the National Shelter Policy (2012) calculated the need for 1.4 million housing units in urban areas by 2023, requiring the construction of around 90,000 new housing units per year. In reality, far fewer new units were constructed each year over the period. For example, one in four households living in Bagmati Province, including Kathmandu, suffered housing deprivation in 2019.

Measures to improve affordable housing supply. Several recent studies correctly identify and recommend removing barriers to improved housing supply to meet the affordability of low- and middle-income earners. These include the need for mobilizing and designating suitable land for residential development, streamlining procedures and permitting requirements for local construction materials, public sector financing for infrastructure, and regulatory reforms to enable options for land development and housing finance accessible to lower-income earners.

Seismic risk reduction. Future earthquake damage and losses can be reduced by adopting and implementing risk-informed policies and actions in two areas. First, by using risk-informed land-use plans to avoid development in areas with underlying soil and rock conditions that will amplify ground shaking or liquefaction, avoiding landslide-prone soils, and by accommodating urban expansion onto safer lands rather than pursuing densification policies. Second, by designing and constructing stronger buildings to meet specified seismic performance standards. The most common residential building types in the three countries are vernacular, non-engineered buildings constructed with lightweight materials such as fired brick, unreinforced mortar, and adobe-block walls. If well-constructed, these traditional buildings can withstand significant seismic events. Non-engineered low-rise earth and masonry buildings should follow the seismic design guidelines of the International Association of Earthquake Engineering.

The associated increase in costs is dependent on many factors but is generally in the range of 5%–20% of total building costs. Savings effected through simple design modifications could be used to offset the costs without compromising amenities, such as lowering the height of rooms, ensuring regular shaped rooms, and promoting the use of wood-frame construction where appropriate. Subsidies offered by schemes such as Pradhan Mantri Awas Yojana Urban (PMAY-U) “Housing for All” in India offer an example of how government assistance can help offset such costs for poor households, particularly in the case of beneficiary-led construction options, serving to safeguard affordability.

The diverse range of failures during a seismic disaster highlights the need to promote not only the enforcement of building codes but also seismic awareness among households and small-scale builders and disseminating improved construction practices to enhance overall seismic resilience.

On the supply side of the housing value chain. Developers, from governments, support partners, profit and nonprofit companies to self-builders, all work to build housing that meets household needs and preferences in terms of plot size, building design, size of floor space, location, and price. Public agencies must facilitate timely access to suitable, well-located, and serviced land for development, with infrastructure services such as water supply, wastewater disposal, power, and roads. Developers and builders then decide whether or not to undertake house construction in that location.

If a steady and predictable pipeline of land is not available, or approval of sites takes a long time and is costly, the entire value chain becomes choked, and housing supply dries up and cannot keep up with population growth. This, in turn, leads to the formation and perpetuation of informal settlements, typically on marginal and unsafe land, or to overcrowding of existing housing stock, resulting in exacerbated loss to human life if a disaster were to occur.

There are several factors necessary to underwrite supply-side activities:

(i) Public and political acceptance of the positive role that well-managed cities play translating into policies and a legal framework that enable changes in land use so that the urban footprint is able to expand or densify in safer areas to accommodate urban growth and adequate provisioning for residential land, which typically accounts for between 40% and 70% of all urban land.

(ii) Availability and ease of using accurate and granular risk information to translate these policies into practice through risk-informed forward spatial city planning and infrastructure investments in well-located and low-hazard risk areas.

(iii) Resources and incentives that bring about change in the knowledge, attitudes, and practices of house designers, builders, and financiers for the design and construction of seismically strengthened but affordable houses.

On the demand side of the housing value chain. This encompas

[中间内容因长度限制已省略]

using for India's Low-Income Households: A Demand Perspective. ICRIER Working Paper Series. No. 402. Indian Council for Research on International Economic Relations.

Shanker, D. and M. L. Sharma. 1998. Estimation of Seismic Hazard Parameters for the Himalayas and Its Vicinity from Complete Data Files. Pure and Applied Geophysics. 152 (2). pp. 267–279.

Showstack, R. 2015. Reducing Earthquake Risk in Nepal. Eos. 7 May.

Singh, S., S. M. Tanvir Hassan, M. Hassan, and N. Bharti. 2020. Urbanisation and Water Insecurity in the Hindu Kush Himalaya: Insights from Bangladesh, India, Nepal and Pakistan. Water Policy. 22 (1). pp. 9–32.

Sitharam, T. G. and S. Kolathayar. 2013. Seismic Hazard Analysis of India Using Areal Sources. Journal of Asian Earth Sciences. 62. pp. 647–653.

So, E. 2016. Estimating Fatality Rates for Earthquake Loss Models. Springer Briefs in Earth Sciences. 1.

Somsa-Ard, N. and S. Pailoplee. 2013. Seismic Hazard Analysis for Myanmar. Journal of Earthquake and Tsunami. 7 (4). 1350029.

Spence, R., E. So, and C. Scawthorn, eds. 2011. Human Casualties in Earthquakes: Progress in Modelling and Mitigation. Advances in Natural and Technological Hazards Research. 29.

Stevens, V. L., R. De Risi, R. Le Roux-Mallouf, D. Drukpa, and G. Hetényi. 2020. Seismic Hazard and Risk in Bhutan. Natural Hazards: Journal of the International Society for the Prevention and Mitigation of Natural Hazards. 104 (3). pp. 2339–2367.

Stevens, V. L., S. N. Shrestha, and D. K. Maharjan. 2018. Probabilistic Seismic Hazard Assessment of Nepal. Bulletin of the Seismological Society of America. 108 (6). pp. 3488–3510.

Subedi, B. and H. R. Parajuli. 2016. Probabilistic Seismic Hazard Analysis of Nepal. Proceedings of IOE Graduate Conference. pp. 265–270.

Sultan, M. 2015. Seismic Hazard Analysis of Pakistan. Journal of Geology & Geoscience. 4 (1). 1000190.

United Nations. Department of Economic and Social Affairs, Population Division. 2018. World Urbanization Prospects: The 2018 Revision.

United Nations Development Programme (UNDP). 2019. Disaster Recovery: Challenges and Lessons.

UNDP. 2020. Rapid Assessment of Socio Economic Impact of COVID-19 in Nepal.

United Nations Entity for Gender Equality and the Empowerment of Women (UN Women). 2011. Progress of World's Women: In Pursuit of Justice.

United Nations Human Settlement Programme (UN-Habitat). 2003. The Challenge of Slums: Global Report on Human Settlements.

UN-Habitat and United Nations Economic and Social Commission for Asia and the Pacific (UNESCAP). 2010. Urbanization: The Role the Poor Play in Urban Development. In Quick Guides for Policy Makers: Housing the Poor in Asian Cities. p. 18.

Valera, H. G. A. et al. 2018. Women's Land Title Ownership and Empowerment: Evidence from India. ADB Economics Working Paper Series. No. 559. ADB.

Waseem, M., A. Lateef, I. Ahmad, S. Khan, and W. Ahmed. 2019. Seismic Hazard Assessment of Afghanistan. Journal of Seismology. 23 (2). pp. 217–242.

Wester, P. et al, eds. 2019. The Hindu Kush Himalaya Assessment - Mountains, Climate Change, Sustainability and People. Springer.

World Bank. Gender Data Portal (accessed 20 November 2023).

World Bank. World Bank Open Data (accessed 20 November 2023).

World Economics. Quarterly Informal Economy Survey (accessed 20 November 2023).

Xu, J. R. et al. 2009. The Melting Himalayas: Cascading Effects of Climate Change on Water, Biodiversity, and Livelihoods. Conservation Biology. 23. pp. 520–530.

Xuejing, L. W. Xu, and Gao, M. 2022. Probabilistic Seismic Hazard Analysis Based on Arias Intensity in the North–South Seismic Belt of PRC. Bulletin of the Seismological Society of America.

Yang, H. B. et al. 2023. Probabilistic Seismic Hazard Assessments for Myanmar and Its Metropolitan Areas. Geoscience Letters. 10 (1)

Yinyin, D., Q. Huang, C. He, S. Meng, and Q. Zhang. 2018. Rapid Population Growth Throughout Asia's Earthquake–Prone Areas: A Multiscale Analysis. International Journal of Environmental Research and Public Health. 15 (9). 1893.

Toward More Livable Cities in the Hindu Kush Himalayas
Lessons from the Nexus of Affordable and Seismic-Resilient Housing in Bhutan, the India-Himalaya Region, and Nepal

The Hindu Kush Himalaya (HKH) region—Asia’s “water tower”—supports over a billion people whose lives, livelihoods, and homes face growing risks from seismic activity and climate change. This paper examines affordable and seismically resilient housing in India, Bhutan, and Nepal, highlighting the urgent need for risk-informed relocation housing solutions that safeguard vulnerable groups and sustain livelihoods. Despite active housing programs, gaps persist in policies, financing, and practices that hinder the supply of safe and affordable homes. The paper emphasizes integrating safeguards, technology-driven approaches, and traditional building techniques to strengthen seismic resilience and community ownership. It underscores the importance of aligning housing value chains with inclusive urban planning and social protection systems. Drawing on case studies, the paper charts a road map toward sustainable, resilient, and affordable housing in the HKH region, aligned with the Asian Development Bank’s Strategy 2030 priority of making cities more livable.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.
"""
