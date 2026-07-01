你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## TECHNICAL ASSISTANCE REPORT

PERU

Report on Physical Energy Flow and Air Emissions Accounts (October 6–10, 2025)

OCTOBER 2025

Prepared By

Lisbeth Rivas and Alcino Gomes

Authoring Departments:

Statistics Department

## DISCLAIMER

"The contents of this document constitute technical advice provided by the staff of the International Monetary Fund to the authorities of National Statistical Office of Peru (CD Recipient) in response to their request for technical assistance. This document (in whole or in part) or summaries thereof may be disclosed by the IMF to the IMF Executive Director for Peru, to other IMF Executive Directors and members of their staff, as well as to other agencies or instrumentalities of the CD recipient, and upon their request, to World Bank staff, and other technical assistance providers and donors with legitimate interest, unless the CD recipient specifically objects to such disclosure (see Operational Guidance for the Dissemination of Capacity Development Information). Publication or Disclosure of this report (in whole or in part) to parties outside the IMF other than agencies or instrumentalities of the CD recipient, World Bank staff, other technical assistance providers and donors with legitimate interest shall require the explicit consent of the CD recipient and the IMF's Statistics department."

## MEMBERS/PARTNERS

![](images/02947fbf1433d725bbe55a8e37473affba1b3e8e7efa6f06bc1f55381da61bd6.jpg)

Schweizerische Eidgenossenschaft
Confédération suisse
Confederazione Svizzera
Confederaziun svizra

State Secretariat for Economic Affairs
SECO
Economic Cooperation and Development

## Table of Contents

Acronyms and Abbreviations....2
Summary of Mission Outcomes and Priority Recommendations....3
Section II. Detailed Technical Assessment and Recommendations....5
A. Officials Met During the Mission....7

Acronyms and Abbreviations

AEA Air Emissions Accounts
APN Autoridade Portuária Nacioanl
BCRP Banco Central de Reserva del Perú
ICSEEA Interinstitutional Committee of Statistics and Environmental and Economic Accounts
IMF International Monetary Fund
INEI Instituto Nacional de Estadística e Informática
MIDAGRI Ministerio de Desarrollo Agrario y Riego
MINAM Ministerio del Ambiente
MINEM Ministerio de Energía y Minas
MTC Ministerio de Transportes y Comunicaciones
NA National Accounts
NDNA National Directorate of National Accounts of the INEI
OECD Organization for Economic Cooperation and Development
OSINERGMIN Organismo Supervisor de la Inversión en Energía y Minería
PEFA Physical Energy Flow Accounts
SECO Swiss State Secretariat for Economic Affairs
SEEA System of Environmental Economic Accounting
SEEACF System of Environmental-Economic Accounting 2012 – Central Framework
SEEA Energy. System of Environmental-Economic Accounting for Energy
SENAMHI Servicio Nacional de Meteorología e Hidrología
SERFOR Servicio Nacional Forestal y de Fauna Silvestre
SNA System of National Accounts
UNSIAP United Nations Statistical Institute for Asia and the Pacific

## Summary of Mission Outcomes and Priority Recommendations

1. A technical assistance (TA) mission visited the Instituto Nacional de Estadística e Informática of Peru during October 6–10, 2025. The objective of the mission was to review, assess, analyze, and validate the results of the revised Physical Energy Flow Accounts (PEFA) and Air Emissions Accounts (AEA) for 2019, the preliminary PEFA for the period 2020–2022 and the preliminary AEA for the years 2020–2021, and discuss dissemination strategies for releasing these accounts. A second objective was to develop a time series for the indicators building on the experience of the data compiled for 2019 and set up a mechanism for regular production of the accounts. The mission also supported a broader stakeholder engagement. The COVID-19 Pandemic affected the availability and timeliness of the source data for compiling the accounts.

2. The IMF Statistics Department with support from the Switzerland State Secretariat for Economic Affairs (SECO)—launched a two-year “Environmental and Climate Change Statistics Capacity Development Program” to assist countries in designing and implementing programs for developing timely and internationally comparable statistics that can help in formulating policies to address the environmental, financial, economic, and social implications of climate change.

3. The project was launched in March 2023, and a diagnostic mission conducted in July 2023 suggested that INEI could explore the development of energy and air emissions accounts. $^{1}$ Later, in February 2024, three participants from Peru attended the training workshop conducted in collaboration with the United Nations Statistical Institute for Asia and the Pacific (UNSIAP) in Chiba, Japan. Linking air emission and energy data to economic activities provides the necessary information to develop policies that promote reducing emissions and a shift towards a low-carbon economy. Further, because energy and air emission accounts use the same structure as supply and use tables, they can be used in the input-output modelling for calculating carbon footprints. These accounts also support decision making regarding carbon taxes/prices as well as understanding the effect of border carbon adjustments.

4. A TA mission visited the INEI of Peru during May 27–31, 2024, to initiate the compilation of energy and air emission accounts and to train compilers. Different teams from INEI, ministries and government institutions related to agriculture, forest, mines, energy, environment, and climate participated in the workshop and provided information on the data currently collected and compiled and their use. Exercises were developed and solved to illustrate the compilation procedures. The sources and methods of compilation for the energy and air emissions accounts were discussed based on presentations and examples using actual data from Peru.

5. The May 2024 mission stressed the need to enhance communication, collaboration and coordination among data producing agencies through data sharing mechanisms such as memorandums of understanding and establishing technical committees considering that the data needed to produce energy and air emission accounts are dispersed across institutions. The Peru's National Interinstitutional Committee of Statistics and Environmental and Economic Accounts (ICSEEA) serve as a coordination mechanism among various stakeholders. The mission stressed the importance of releasing the energy and air emission accounts before the end of the project in April 2025, even if the

data could be labelled as experimental. Continued virtual monthly TA was provided to the INEI for compiling the energy and air emissions accounts for 2019 following the mission.

6. A third mission was conducted in February 2025 to provide assistance to the INEI in the data analysis/validation, dissemination strategies, and in preparing metadata and data releases on the energy and air emission accounts for 2019.

7. The experimental accounts for 2019 were released on July 11, 2025, in a document called: "Experimental Accounts of Physical Energy Flows and Air Emissions—Methodology and Results (Cuentas Experimentales de Flujos de Energía Física y Emisiones al Aire—Metodología y Resultados). $^{2}$ The publication provides the data, the description of the methodologies used as well as the indicators disseminated through user friendly charts. Several source data producers and other stakeholders made comments on the publication that will be considered at the next release of the accounts.

8. This present mission reviewed, assessed, and validated the PEFA data for the period 2020–2022 and the AEA data for the period 2020–2021, and provided recommendations for improvement as needed, in particular, on the allocation of natural gas and diesel to the relevant industries and in applying the residence principle to maritime and inland water transport, involving the allocation of energy use and air emissions to the resident units in the country. These adjustments are necessary to align energy and air emission data to national accounts data.

9. The mission provided hands-on assistance to make the recommended adjustments and interpret the results and the different indicators included in the accounts. Most adjustments were incorporated into the accounts on site.

10. Additional hands-on assistance was provided by the mission on the allocation of different diesel types used by the domestic economy to PEFA energy products. Allocation was cross-checked with the Ministry of Energy and Mines (MINEM) experts on site.

11. Economic-environmental indicators production and dissemination were discussed and settled, namely on the use of GDP at current or constant prices. In addition, the use of the supply and use table by product and the value added by economic activity at current prices from the national accounts was discussed.

12. The mission also discussed guidelines for preparing the publication of the tables with the accounts and their respective metadata.

13. The objective is that by April 2026, the country would have released the revised data for 2019 and the preliminary PEFA for the period 2020–2022 and the preliminary AEA for the period 2020–2021 and would have set up a mechanism for the regular compilation of the accounts. To accomplish this, additional human resources need to be allocated to the compilation of the PEFA and the AEA.

14. To support progress in the above work areas, the mission recommended the following priority recommendations to compile PEFA and AEA.

TABLE 1. Priority Recommendations

<table><tr><td>Target Date</td><td>Priority Recommendation</td><td>Responsible Institutions</td></tr><tr><td>October 2025</td><td>Make the adjustments suggested by the mission on natural gas, diesel, and maritime and inland water transport to the accounts.</td><td>INEI</td></tr><tr><td>October 2025</td><td>Use the supply and use table and the GDP at current prices for the year in question to calculate the ratios for the adjustments and the indicators used in the accounts.</td><td>INEI</td></tr><tr><td>April 2026</td><td>Publish the tables with revised data, and their respective metadata, for 2019 and preliminary energy accounts for the period 2020–2022 and air emissions accounts for the period 2020–2021 by April 2026.</td><td>INEI</td></tr></table>

15. Further details on the priority recommendations and the related actions/milestones can be found in the action plan under Detailed Technical Assessment and Recommendations.

## Section II. Detailed Technical Assessment and Recommendations

16. A technical assistance mission visited the Instituto Nacional de Estadística e Informática of Peru during October 6–10, 2025. The objective of the mission was to review, assess, analyze, and validate the results of the revised Physical Energy Flow Accounts (PEFA) and Air Emissions Accounts (AEA) for 2019, the preliminary PEFA for the period 2020-2022 and the preliminary AEA for the years 2020–2021, and discuss dissemination strategies for releasing these accounts. A second objective was to develop a time series for the indicators building on the experience of the data compiled for 2019 and set up a mechanism for regular production of the accounts. The mission also supported a broader stakeholder engagement. The Covid-19 Pandemic affected the availability and timeliness of the source data for compiling the accounts.

17. This present mission reviewed, assessed, and validated the PEFA data for the period 2020–2022 and the AEA data for the period 2020–2021.

18. During the data analysis, incoherence in natural gas allocation was detected on the mining and manufacturing industry's data source: the energy balance. Therefore, revision and redistribution of the own consumption of energy products by the mining and manufacturing industries were recommended by the mission, because besides the own consumption of natural gas, it includes the consumption of oil derivative products that will affect both mining and manufacturing industries.

19. The mission suggested collaboration and coordination with the MINEM to access additional detailed data for making the adjustments to the PEFA.

20. Both PEFA and AEA compilation requires applying the national accounts residence principle, by which all energy flows and/or emissions used or generated by resident units should be included in these accounts, and all energy flows and/or emissions used or generated by non-resident units in the economic territory should be deducted. Issues requiring residence adjustment were reviewed.

21. Allocation of natural gas and diesel to the relevant industries and residence principle adjustments to maritime and inland water transport require improvements, involving the allocation of energy use and air emissions to the resident units in the country. These adjustments are necessary to align energy and air emission data to national accounts data. The mission suggested contacting the OECD to request more detailed data on the experimental database on navigation transport, and the Reserve Bank of Peru to request the detailed balance of payments data (e.g., fuel sales to non-residents and fuel purchases abroad by residents).

22. Special attention was given to inter-connections between PEFA and AEA. For example, adjustments to residence principle can be performed once for both accounts, using energy flows with emissions to boost compilation process productivity and data quality.

23. The mission provided hands-on assistance to make the recommended adjustments and interpret the results and the different indicators included in the accounts. Most adjustments were incorporated into the accounts on site. AEA and PEFA are in line with the accounting structures and principles of the System of Environmental-Economic Accounting 2012—Central Framework (SEEA-CF), and, therefore, fully consistent with monetary data from the System of National Accounts (SNA). As stressed during the mission, this allows all kinds of analyses, and it can be an input for other statistics and/or accounts, such as between AEA and PEFA, or national accounts.

24. Additional hands-on assistance was provided by the mission on the allocation of different diesel types used by the domestic economy to PEFA energy products. Allocation was cross-checked with the MINEM experts on site.

25. Economic-environmental indicators production and dissemination were discussed and settled, namely on the use of GDP at current or constant prices. In addition, the use of the supply and use table by product and the value added by economic activity at current prices from the national accounts was discussed.

26. The mission also discussed guidelines for preparing the publication of the tables with the accounts and their respective metadata. Examples from other countries and international institutions published data and metadata were explored on site.

27. The objective is that by April 2026, the country would have released the revised data for 2019 and the preliminary PEFA for the period 2020–2022 and the preliminary AEA for the period 2020–2021 and would have set up a mechanism for the regular compilation of the accounts. To accomplish this, additional human resources need to be allocated to the compilation of the PEFA and the AEA.

The mission made the following main recommendations:

\- Allocate additional human resources to the compilation of the energy and air emission accounts.

\- Make the adjustments suggested by the mission on natural gas, diesel, and maritime and inland water transport to the accounts.

\- Review and redistribute the own consumption of energy products by the mining and manufacturing industries because besides the own consumption of natural gas, it includes the consumption of oil derivative products that will affect both mining and manufacturing industries. Request additional detailed data to the MINEM for making the adjustments to the PEFA.

\- Use the supply and use table and the GDP at current prices for the year in question to calculate the ratios for the adjustments and the indicators used in the accounts.

\- Publish the tables with revised data, and their respective metadata for 2019, preliminary energy accounts for the period 2020–2022, and air emissions accounts for the period 2020–2021 by April 2026.

\- Contact the OECD to request more detailed data on the experimental database on navigation transport and the and the Reserve Bank of Peru to request the detailed balance of payments data (e.g., fuel sales to non-residents and fuel purchases abroad by residents).

\- Increase the level of detail from aggregated to medium breakdown both on the AEA and the PEFA for the next compilation exercise.

\- Establish a mechanism for the regular compilation and publication of the accounts at national level from 2026 onwards.

\- Start the regular annual reporting of the AEA and the PEFA questionnaires to the United Nations and OECD by March 2026.

## A. OFFICIALS MET DURING THE MISSION

<table><tr><td>Name</td><td>Institution</td></tr><tr><td>Raymundo Guillermo Chirinos Cabrejos</td><td>BCRP</td></tr><tr><td>Sebastián Alejandro Basurto Cervantes</td><td>BCRP</td></tr><tr><td>Jhonatan Edwin Bruno Ramirez</td><td>SENAMHI</td></tr><tr><td>Juan Carlos Zegarra Vargas</td><td>SENAMHI</td></tr><tr><td>Rosalinda Cedy Aguirre Almeyda</td><td>SENAMHI</td></tr><tr><td>Carmen Carolina Calle Benavides</td><td>MTC</td></tr><tr><td>Diego Lope</td><td>MINAM</td></tr><tr><td>Robert Cordoña Ccahuata</td><td>MINEM</td></tr><tr><td>Giannina Ibarra</td><td>MINEM</td></tr><tr><td>Celia Bedoya Jimenez</td><td>MIDAGRI</td></tr><tr><td>Irma Romero</td><td>MIDAGRI</td></tr><tr><td>Milagros Montes Matos</td><td>MIDAGRI</td></tr><tr><td>Sandra Roncal</td><td>MIDAGRI</td></tr><tr><td>Alfredo Apaza Ticona</td><td>SERFOR</td></tr><tr><td>Alexs Arana Olivos</td><td>SERFOR</td></tr><tr><td>Wilder Santos Viera</td><td>OSINERGMIN</td></tr><tr><td>Jose Luis Robles</td><td>INEI</td></tr><tr><td>Consuelo Landa</td><td>INEI</td></tr><tr><td>Henry Meza Meza</td><td>INEI</td></tr><tr><td>Judith Samaniego</td><td>INEI</td></tr><tr><td>Ysabel Galvan Palomino</td><td>INEI</td></tr><tr><td>Ernesto Mercado</td><td>INEI</td></tr><tr><td>Bertha Rodriguez Jara</td><td>INEI</td></tr><tr><td>Carlos Carre Rodriguez</td><td>INEI</td></tr><tr><td>Felixalberto Lavado</td><td>INEI</td></tr><tr><td>Fanny Sumalave</td><td>INEI</td></tr><tr><td>Jean Gonzales Vitancio</td><td>INEI</td></tr><tr><td>Miluska Luy Fabab</td><td>INEI</td></tr></table>
"""
