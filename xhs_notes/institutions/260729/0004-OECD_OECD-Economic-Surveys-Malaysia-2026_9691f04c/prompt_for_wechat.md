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
# OECD Economic Surveys: Malaysia 2026

July 2026

Volume 2026/22

![](images/c2d7855f0b56394ca9c077520db3891d4349ea034f4f875ba9c70994a779cba7.jpg)

## OECD Economic Surveys: Malaysia 2026

This work was approved and declassified by the Economic and Development Review Committee on 3 July 2026.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

The statistical data for Israel are supplied by and under the responsibility of the relevant Israeli authorities. The use of such data by the OECD is without prejudice to the status of the Golan Heights, East Jerusalem and Israeli settlements in the West Bank under the terms of international law.

## Note by the Republic of Türkiye

The information in this document with reference to “Cyprus” relates to the southern part of the Island. There is no single authority representing both Turkish and Greek Cypriot people on the Island. Türkiye recognises the Turkish Republic of Northern Cyprus (TRNC). Until a lasting and equitable solution is found within the context of the United Nations, Türkiye shall preserve its position concerning the “Cyprus issue”.

## Note by all the European Union Member States of the OECD and the European Union

The Republic of Cyprus is recognised by all members of the United Nations with the exception of Türkiye. The information in this document relates to the area under the effective control of the Government of the Republic of Cyprus.

## Please cite this publication as:

OECD (2026), OECD Economic Surveys: Malaysia 2026, OECD Publishing, Paris, https://doi.org/10.1787/9ab6b826-en.

ISBN 978-92-64-90122-3 (print)
ISBN 978-92-64-73410-4 (PDF)
ISBN 978-92-64-51012-8 (HTML)

OECD Economic Surveys
ISSN 0376-6438 (print)
ISSN 1609-7513 (online)

OECD Economic Surveys: Malaysia
ISSN 2959-4944 (print)
ISSN 2959-4952 (online)

Photo credits: Cover © AzriSuratmin/Shutterstock.com. Chapter 1 © nicepix/Shutterstock.com. Chapter 2 © Aisyaqilumaranas/Shutterstock.com. Chapter 3 © Abdul Razak Latif/Shutterstock.com. Chapter 4 © Shutterstock AI/Shutterstock.com.

Corrigenda to OECD publications may be found at: https://www.oecd.org/en/publications/support/corrigenda.html.

![](images/f12edb4a971401ddb403b50c1a2a42189d758e1618de7d1358cc3bfffc53cef6.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of the original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

## Foreword

This Economic Survey was prepared by Kazuyoshi Ohnuma, Randall Jones, Vincent Koen and Paula Adamczyk under the supervision of Jens Arnold. Research assistance was provided by Isabella Medina, administrative and editorial support by Sophie Jenkins and communication assistance by Francois Iglesias.

This Survey is published under the responsibility of the Economic Development and Review Committee of the OECD. The Committee discussed the draft survey on 17 June 2026 with participation of representatives of the Malaysian authorities. The draft report was then revised in light of the discussions. The report does not necessarily reflect the official views of the Malaysian government. The cut-off date for data used in the Survey is 17 July 2026.

Support from the government of Japan is gratefully acknowledged.

Information about this and previous Surveys and more information about how Surveys are prepared is available at https://www.oecd.org/en/topics/economic-surveys.html.

## Table of contents

Foreword 3   
Basic statistics of Malaysia, 2025 7   
Executive summary 8   
1 Macroeconomic resilience and policies 17   
1.1.Growth held up in the face of shocks but has begun to slow 18   
1.2.Inflation came down from its 2022 peak 23   
1.3.Growth is projected to remain solid 24   
1.4.The monetary stance is broadly neutral and the exchange rate has appreciated 26   
1.5.Financial sector risks seem to be contained 28   
1.6.The need to press ahead with fiscal consolidation 30   
1.7.Strengthening long-term growth prospects through reforms 41   
References 43   
2 Coping with Climate Change 45   
2.1.Malaysia is exposed to significant climate-related hazards 46   
2.2.Adapting to climate change 48   
2.3.Continuing mitigation efforts 56   
References 65   
3 Boosting productivity through openness, smarter regulation and digitalisation 69   
3.1.Productivity growth has fallen short of targets 70   
3.2.Lifting remaining regulatory barriers at the border 72   
3.3.Addressing domestic hurdles 75   
3.4.Ensuring a more level playing field 77   
3.5Stepping up the digitalisation of government and healthcare 80   
3.6.Streamlining public governance and combating corruption and money laundering 82   
References 87   
4 Improving skills, education and training 89   
4.1.Building on progress in education reform to improve living standards 90   
4.2.Early childhood education: the groundwork for better learning outcomes 95   
4.3.Primary and secondary schools 103   
4.4.Technical and vocational education and training and lifelong learning 117

4.5. Improving higher education in Malaysia 121
References 128

## FIGURES

Figure 1. Malaysia has outperformed peers
Figure 2. High fossil fuel subsidies run counter to carbon pricing effort
Figure 3. Productivity growth has trended down
Figure 4. Malaysia has a high share of low-performing students and few high-performing ones
Figure 1.1. Growth has been supported by the buoyancy of the tech cycle
Figure 1.2. Malaysia trades actively with the rest of the world
Figure 1.3. Labour market conditions have improved
Figure 1.4. CPI inflation has been subdued since 2024
Figure 1.5. The policy interest rate has remained close to 3% over the past three years
Figure 1.6. The real effective exchange rate has appreciated since 2024
Figure 1.7. The share of non-performing loans has remained low
Figure 1.8. Some fiscal consolidation has taken place but public debt is high
Figure 1.9. Demographic headwinds loom
Figure 1.10. Ageing pressures will call for spending and revenue measures
Figure 1.11. A comparatively large share of public spending takes the form of subsidies
Figure 1.12. Petrol prices are very low in Malaysia
Figure 1.13. Coverage of pension schemes is low
Figure 1.14. Corporate income tax accounts for a large share of total tax revenue
Figure 2.1. Floods are frequent and costly
Figure 2.2. Insurance penetration for natural hazards is very low across Asia and the Pacific
Figure 2.3. Insurance is more affordable than in peers but challenging for low-income earners
Figure 2.4. GHG emissions are driven by the energy sector
Figure 2.5. Fossil fuel dependence is high compared to peer countries
Figure 2.6. Fossil fuels dominate electricity generation
Figure 2.7. Fuel prices are very low
Figure 2.8. Malaysia does not yet price carbon emissions
Figure 2.9. Reaching net zero will require higher carbon prices
Figure 3.1. The level of productivity is higher than in most peer countries
Figure 3.2. Productivity growth has trended down
Figure 3.3. Malaysia has ample scope to make regulation more competition-friendly
Figure 3.4. The FDI regime is fairly restrictive, largely reflecting foreign equity restrictions
Figure 3.5. Restrictions on trade in computer services remain
Figure 3.6. The regulatory framework for market competition can be improved
Figure 3.7. Distortions induced by public ownership are high
Figure 3.8. Corruption perception
Figure 3.9. Anti-money laundering measures
Figure 4.1. Workers' mean years of schooling in Malaysia have risen rapidly
Figure 4.2. Gains in labour quality have made a large contribution to productivity growth
Figure 4.3. Government education spending is below OECD countries and some peers
Figure 4.4. Government expenditure per student is relatively low
Figure 4.5. Registered childcare centres are closing in parts of Malaysia
Figure 4.6. Preschool enrolment has risen significantly since 2010
Figure 4.7. Spending per child in preschool is low compared to primary and secondary students
Figure 4.8. Students from low-income quintiles are less well-prepared for primary school
Figure 4.9. Proficiency in reading and mathematics has fallen, but still exceeds some lower-income ASEAN countries
Figure 4.10. Malaysian students have fallen below the international average in the TIMMS
Figure 4.11 Malaysia's scores fell into the bottom one-third in the 2022 PISA
Figure 4.12. Malaysia's PISA scores have declined significantly
Figure 4.13. Malaysia has many low-performing students and few high-performing ones
Figure 4.14. The gap between private and public schools in PISA has widened
Figure 4.15. The share of students not enrolled in secondary school in Malaysia is high (2023)
Figure 4.16. A framework for dealing with consistently underperforming teachers
Figure 4.17. The impact of socio-economic factors on Malaysia's PISA scores was relatively high

Figure 4.18. The share of young people in TVET programmes is relatively low in Malaysia 118  
Figure 4.19. The share of firms providing formal training in Malaysia exceeds the ASEAN average 121  
Figure 4.20. The share of tertiary graduates in STEM programmes is exceptionally high 123  
Figure 4.21. Malaysia's tertiary enrolment rate has fallen in recent years and is below its peers 124

## TABLES

Table 1. Real GDP growth will remain solid 10  
Table 1.1. Macroeconomic indicators and projections 24  
Table 1.2. Low-probability events that could lead to major changes to the outlook 25  
Table 1.3. Past recommendations on monetary and financial policies and actions taken 30  
Table 1.4. Past recommendations on fiscal policy and actions taken 32  
Table 1.5. Indicative fiscal revenues and costs 34  
Table 1.6. Past recommendations on social policies and actions taken 37  
Table 1.7. Illustrative impact of selected structural reforms on GDP per capita 41  
Table 1.8. Macroeconomic policy recommendations 42  
Table 2.1. Past recommendations on climate challenges 64  
Table 2.2. Policy recommendations 64  
Table 3.1. Past recommendations on MSMEs and GLCs and actions taken 79  
Table 3.2. Past recommendations on strengthening governance and actions taken 84  
Table 3.3. Policy recommendations 86  
Table 4.1 Quantitative targets for education that are included in the Thirteenth Malaysia Plan 93  
Table 4.2. Preschool is provided by government ministries and the private sector (2025) 98  
Table 4.3. The nutritional status of children under age 5 has deteriorated 103  
Table 4.4. Malaysia ranks in the middle in digital competitiveness, although its score has fallen 115  
Table 4.5. The number of public TVET institutions by ministry (2024) 118  
Table 4.6. Malaysia's higher education sector 122  
Table 4.7. Policy Recommendations 127

## BOXES

Box 1.1. Malaysia's New Industrial Master Plan 18  
Box 1.2. Leveraging the global data centre boom and Malaysia's resource endowments 21  
Box 1.3. Malaysia's exposure to the global energy price shock 26  
Box 1.4. Cyber risks facing Malaysia's economy and financial system 31  
Box 1.5. Leveraging PADU to improve targeting of social assistance and support fiscal consolidation 38  
Box 1.6. Aiming support better in the face of energy price shocks 39  
Box 2.1. The OECD ENV-Linkages modelling framework 62  
Box 3.1. The OECD's product market regulation indicator 71  
Box 3.2. Malaysia's policies to improve the economic status of Bumiputera 73  
Box 3.3. Affirmative action without distortion in South Africa, Canada and Australia 80  
Box 3.4. Digital health as a driver of efficiency: lessons from Estonia and Denmark 82  
Box 4.1. The Thirteenth Malaysia Plan 2026–2030 focuses on education 92  
Box 4.2. Poland: an example of reforms that led to a sharp rise in its PISA score 107  
Box 4.3. Professional frameworks for teachers: Saudi Arabia, Singapore and Colorado, USA 109  
Box 4.4. The Malaysia Education Blueprint 2013-2025: A strategy to improve the quality of teaching 110  
Box 4.5. The power of incentives in education: Lessons from the Brazilian state of Ceará 111

## Basic statistics of Malaysia, 2025

(Numbers in parentheses refer to the OECD average)

<table><tr><td colspan="6">LAND, PEOPLE AND ELECTORAL CYCLE</td></tr><tr><td>Population (million)</td><td>35.6</td><td></td><td>Population density per km2</td><td>108.2</td><td>(39.6)</td></tr><tr><td>Under 15 (%),</td><td>21.8</td><td>(16.7)</td><td>Life expectancy at birth (years, 2023)</td><td>76.7</td><td>(80.2)</td></tr><tr><td>Over 65 (%)</td><td>7.7</td><td>(18.6)</td><td>Men (2023)</td><td>74.3</td><td>(77.6)</td></tr><tr><td>International migrant stock (% of population, 2024)</td><td>10.7</td><td>(15.7)</td><td>Women (2023)</td><td>79.4</td><td>(82.8)</td></tr><tr><td>Latest 5-year average growth (%)</td><td>1.2</td><td>(0.5)</td><td>Latest general election</td><td colspan="2">November 2022</td></tr><tr><td colspan="6">ECONOMY</td></tr><tr><td>Gross domestic product (GDP)</td><td></td><td></td><td>Value added shares (%,2025)</td><td></td><td></td></tr><tr><td>In current prices (billion USD)</td><td>473.2</td><td></td><td>Agriculture, forestry and fishing</td><td>8.2</td><td>(2.6)</td></tr><tr><td>In current prices (billion MYR)</td><td>2025.4</td><td></td><td>Industry including construction</td><td>33.2</td><td>(26.0)</td></tr><tr><td>Latest 5-year average real growth (%)</td><td>5.2</td><td>(3.0)</td><td>Services</td><td>57.2</td><td>(71.4)</td></tr><tr><td>Per capita (thousand USD PPP)1</td><td>38.8</td><td>(62.1)</td><td></td><td></td><td></td></tr><tr><td colspan="6">GENERAL GOVERNMENT</td></tr><tr><td>Expenditure (OECD: 2024)</td><td>23.9</td><td>(42.7)</td><td>Gross financial debt (OECD: 2024)</td><td>70.1</td><td>(112.5)</td></tr><tr><td>Revenue (OECD: 2024)</td><td>19.9</td><td>(37.9)</td><td></td><td></td><td></td></tr><tr><td colspan="6">EXTERNAL ACCOUNTS</td></tr><tr><td>Exchange rate (MYR per USD)</td><td>4.28</td><td></td><td>Main exports (% of merchandise exports, 2024)</td><td></td><td></td></tr><tr><td>PPP exchange rate (USA = 1, 2024)</td><td>1.40</td><td></td><td>Machinery and electronics</td><td>51.3</td><td></td></tr><tr><td>In per cent of GDP</td><td></td><td></td><td>Fuels</td><td>11.1</td><td></td></tr><tr><td>Exports of goods and services</td><td>72.2</td><td>(31.0)</td><td>Animal/vegetable fats, oils, waxes</td><td>5.7</td><td></td></tr><tr><td>Imports of goods and services</td><td>66.8</td><td>(31.2)</td><td>Main imports (% of total merchandise imports, 2024)</td><td></td><td></td></tr><tr><td>Current account balance (OECD: 2024)</td><td>1.6</td><td>(-0.3)</td><td>Machinery and electronics</td><td>47.8</td><td></td></tr><tr><td>Net international investment position</td><td>-0.5</td><td></td><td>Fuels</td><td>12.0</td><td></td></tr><tr><td></td><td></td><td></td><td>Metals</td><td>7.0</td><td></td></tr><tr><td colspan="6">LABOUR MARKET, SKILLS AND INNOVATION</td></tr><tr><td>Employment rate (aged 15 and over, %, 2024, OECD: 2024)</td><td>68.4</td><td>(59.8)</td><td>Unemployment rate, Labour Force Survey (aged 15 and over, %, 2024, OECD: 2024)</td><td>3.2</td><td>(4.8)</td></tr><tr><td>Men (2024, OECD: 2024)</td><td>80.5</td><td>(67.5)</td><td>Youth (aged 15-24, %, 2024, OECD: 2024)</td><td>10.3</td><td>(10.5)</td></tr><tr><td>Women (2024, OECD: 2024)</td><td>54.7</td><td>(52.6)</td><td>Long-term unemployed (1 year and over, %, 2024, OECD: 2024)</td><td>0.2</td><td>(1.0)</td></tr><tr><td>Participation rate (aged 15 and over, %, 2024, OECD: 2024)</td><td>70.6</td><td>(62.6)</td><td>Tertiary educational attainment (aged 25-64, %, 2022, OECD: 2024)2</td><td>23.3</td><td>(41.8)</td></tr><tr><td>Mean weekly hours worked (2024, OECD: 2024)</td><td>44.8</td><td>(36.8)</td><td>Gross domestic expenditure on R&amp;D (% of GDP, 2022, OECD: 2022)</td><td>1.01</td><td>(3.0)</td></tr><tr><td colspan="6">ENVIRONMENT</td></tr><tr><td>Total primary energy supply per capita (toe, 2023, OECD: 2024)</td><td>3.0</td><td>(3.7)</td><td>CO2 emissions from fuel combustion per capita (tonnes, 2023, OECD: 2024)</td><td>7.3</td><td>(7.5)</td></tr><tr><td>Exposure to air pollution (more than 10 μg/m3of PM 2.5, % of population, 2020)</td><td>4.5</td><td>(13.1)</td><td>Renewable internal freshwater resources per capita (1 000 m3, 2022)</td><td>16.7</td><td></td></tr><tr><td>Exposure to air pollution (more than 10 μg/m3of PM 2.5, % of population, 2020)</td><td>99.2</td><td>(56.5)</td><td></td><td></td><td></td></tr><tr><td colspan="6">SOCIETY</td></tr><tr><td>Income inequality (Gini coefficient, 2021, OECD: latest available)</td><td>0.407</td><td>(0.315)</td><td>Education outcomes (PISA 2022 score)</td><td></td><td></td></tr><tr><td>Poverty gap at USD 6.85 a day (2017 PPP, %, 2021)</td><td>0.5</td><td></td><td>Reading</td><td>388</td><td>(476)</td></tr><tr><td></td><td></td><td></td><td>Mathematics</td><td>409</td><td>(472)</td></tr><tr><td>Public and private spending (% of GDP)</td><td></td><td></td><td>Science</td><td>416</td><td>(485)</td></tr><tr><td>Health care (2022, OECD: 2024)</td><td>3.9</td><td>(9.3)</td><td>Share of women in parliament (%, 2024)</td><td>13.5</td><td>(33.3)</td></tr><tr><td>Education (public spending, % of GNI, 2021)</td><td>3.9</td><td>(4.4)</td><td></td><td></td><td></td></tr></table>

Note: The year is indicated in parenthesis if it deviates from the year in th

[中间内容因长度限制已省略]

n Working Papers, No. 174, OECD Publishing, Paris, https://doi.org/10.1787/f1cb24d5-en OECD (2020).

Révai, N. (2018), “What difference do standards make to educating teachers?: A review with case studies on Australia, Estonia and Singapore”, OECD Education Working Papers, No. 174, OECD Publishing, Paris, https://doi.org/10.1787/f1cb24d5-en OECD (2020).

Rosli, C., A. Zolkipli and A. Masran (2024), The Legal Landscape of Childcare Centres in Malaysia: An Overview from Stakeholders – International Journal of Research and Innovation in Social Science.

Ruban, A. (2017), So, why have more and more parents enrolled their children in international schools? | Malay Mail, 23 July.

Samuel, M., M. Tee, L. Symaco (2017), “The Educational Landscape of Malaysia”, Chapter 1 in Samuel, M., Tee, M., Symaco, L. (eds), Education in Malaysia, Education in Malaysia: Developments and Challenges | Springer Nature Link.

Schleicher, A. (2020), “Insights from TALIS 2018: Teaching and Learning International Survey.” In TALIS 2018 Results (Volume II): Teachers and School Leaders as Valued Professionals. Paris: OECD Publishing.

SCImago Journal and Country Rank (2024), SJR - International Science Ranking.

Simamora, J. (2025), Malaysia’s Graduate Employment Crisis: Overqualified, Underpaid, and Underutilized - The World Politics

South China Morning Post (2023), Malaysian ex-students sue absent teacher, win nearly US\$11,000 each in damages | South China Morning Post, 2 August.

Tee, M. (2024), “Overview of Education in Malaysia” in International Handbook on Education in Southeast Asia | Springer Nature Link.

Tee, M. and N. Lee (2024), Shaping Teaching Practice In Malaysia: A System's View, Routledge, London.

The Burning Glass Institute and the Strada Education Foundation (2024), College Graduates, Underemployment and the Way Forward, 679a6fadfda4220bbac585d7\_Talent-Disrupted-2.pdf.

Tiong, N. (2023), On the State of Education in Malaysia and What it Means for the Country's Economy – New Naratif.

Trends in International Mathematics and Science Study (2023), Average Achievement (Grade 8) - TIMSS 2023.

UNESCO (2020), UNESCO Institute for Statistics.

UNESCO (2025), World education statistics, 2025 - UNESCO Digital Library.

UNICEF (2019), A-world-ready-to-learn-advocacy-brief-2019.pdf.

UNICEF, 2023, Early Childhood Development Index 2030 (ECDI2030) - UNICEF DATA.

UNICEF & SEAMEO. (2020), SEA-PLM 2019 Main Regional Report, Children's learning in 6 Southeast Asian countries, Bangkok, Thailand: UNICEF & SEAMEO – SEA-PLM Secretariat.

Wan, C., M. Sirat and D. Razak (2018), “Education in Malaysia Towards a Developed Nation”, ISEAS Yusof Ishak Institute Economics Working Paper, No. 2018-4, Microsoft Word - ISEAS EWP 2018-4 Wan.

Wan, C. (2025), Can the 13th Malaysia Plan's Bold Education Reforms Pass the Test of Delivery? | FULCRUM, 28 August.

Wan, C. (2025a), Higher education in Malaysia: a history plagued by fluctuations, ISEAS-Yusof Ishak Institute, Singapore.

Wan, C. (2025b), “TVET in Malaysia’s Human Resource Development: Plans, Realities and ‘Game Changers’”, ISEAS Yusof Ishak Institute Perspective, Issue 2025: No. 5, ISEAS Perspective 2025 5.pdf.

Wei, L. and M. Yew (2024), “The Overeducation Dilemma: Graduate Skill Mismatch in Malaysia’s Labour Market”, International Journal of Business, Economics and Law, Vol. 33, Issue 1, IJBEL31 34.pdf.

Woo, W. (2019), Decentralising Malaysia's education system | East Asia Forum.

World Bank (2013), Malaysia Economic Monitor, December 2013: High-Performing Education - Search

World Bank (2023), Shaping First Steps: A Comprehensive Review of Preschool Education in Malaysia.

World Bank (2024a), Malaysia Economic Monitor - Bending Bamboo Shoots : Strengthening Foundational Skills, April.

World Bank (2024b), Malaysia Economic Monitor : Farming the Future: Harvesting Malaysia’s Agricultural Resilience through Digital Technologies, October

World Bank (2025), A Fresh Take on Reducing Inequality and Enhancing Mobility in Malaysia.

World Salaries (2026), Average Teacher Salary in Malaysia for 2026.

Zalani, A. (2026), “Master Malay and sharpen English skills for global edge, Anwar tells Malaysians”, Malay Mail, 20 January.

Zhahir, Z. (2025), Shortage of registered childcare centres in Malaysia, 18 August.

# OECD Economic Surveys: Malaysia 2026

July 2026

Volume 2026/22

Strong growth and resilience to shocks have helped Malaysia achieve sizeable improvements in material living standards. Further progress will now hinge on new policy approaches to boost productivity and provide better opportunities for wider parts of the population, including through reforms in the education system. Fiscal consolidation should be stepped up to reduce Malaysia's vulnerability to economic shocks and anticipate rising spending pressures from social protection, education and investment. This will require reducing fossil fuel subsidies and re-introducing a broad value-added tax while protecting low-income households with targeted transfers. The effects of climate change are becoming increasingly visible, calling for more coordinated adaptation efforts and further emission reductions. Boosting productivity will require stronger human-capital investment and regulations that are simpler and more conducive to dynamic firm entry and growth. Deteriorating education outcomes and skill mismatches require fundamental reforms of the education system, including more and better spending on pre-school, primary and secondary education, stronger incentives and more autonomy and accountability for educational institutions.

SPECIAL FEATURES: BOOSTING PRODUCTIVITY; COPING WITH CLIMATE CHANGE; IMPROVING SKILLS, EDUCATION AND TRAINING
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
