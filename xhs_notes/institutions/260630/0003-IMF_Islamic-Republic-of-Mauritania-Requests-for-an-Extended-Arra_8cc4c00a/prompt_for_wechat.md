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
# ISLAMIC REPUBLIC OF MAURITANIA

June 2026

REQUESTS FOR AN EXTENDED ARRANGEMENT UNDER THE EXTENDED FUND FACILITY AND ARRANGEMENT UNDER THE EXTENDED CREDIT FACILITY, CANCELLATION OF THE CURRENT ARRANGEMENTS UNDER THE EXTENDED FUND FACILITY AND THE EXTENDED CREDIT FACILITY, AND FIFTH REVIEW UNDER THE RESILIENCE AND SUSTAINABILITY FACILITY ARRANGEMENT—PRESS RELEASE; STAFF REPORT; AND STATEMENT BY THE EXECUTIVE DIRECTOR FOR THE ISLAMIC REPUBLIC OF MAURITANIA

In the context of the Requests for an Extended Arrangement Under the Extended Fund Facility and Arrangement Under the Extended Credit Facility, Cancellation of the Current Arrangements Under the Extended Fund Facility and the Extended Credit Facility, and Fifth Review Under the Resilience and Sustainability Facility Arrangement, the following documents have been released and are included in this package:

• A Press Release including a statement by the Chair of the Executive Board.

\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on June 24, 2026, following discussions that ended on April 10, 2026, with the officials of the Islamic Republic of Mauritania on economic developments and policies underpinning the IMF arrangement under the Extended Credit Facility, Extended Fund Facility, and Resilience and Sustainability Facility. Based on information available at the time of these discussions, the staff report was completed on June 9, 2026.

\- A Debt Sustainability Analysis prepared by the staffs of the IMF and the International Development Association.

• A World Bank Assessment Letter for the Resilience and Sustainability Facility.

• A Statement by the Executive Director for the Islamic Republic of Mauritania.

The IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.

Copies of this report are available to the public from

International Monetary Fund • Publication Services
PO Box 92780 • Washington, D.C. 20090
Telephone: (202) 623-7430 • Fax: (202) 623-7201
E-mail: publications@imf.org Web: http://www.imf.org

International Monetary Fund
Washington, D.C.

# Islamic Republic of Mauritania: IMF Executive Board Approves 42-month Arrangements under Extended Credit Facility (ECF) and the Extended Fund Facility (EFF) and Completes Fifth Review of the Resilience and Sustainability Facility (RSF) Arrangement

FOR IMMEDIATE RELEASE

\- The Executive Board of the International Monetary Fund (IMF) approved new 42-month arrangements under the ECF and EFF and concluded the fifth and final Review under the RSF Arrangement for US\$ 95.8 million to continue to support the authorities' development program and institutional reform agenda.

\- Program performance under the 2022-26 ECF/EFF has been strong; growth in the non-extractive sector remained solid, inflation declined, the current account deficit narrowed, and international reserves remained adequate.

\- The new program will be anchored around three mutually reinforcing pillars: (i) consolidating macroeconomic stability by strengthening macroeconomic institutions and policy frameworks; (ii) strengthening human capital and promoting inclusive growth; and (iii) bolstering governance, including public enterprises.

Washington, DC – June 24, 2026: The IMF Executive Board approved today 42-month arrangements under the ECF and the EFF in the amount of SDR 70.82 million (equivalent of 55 percent of quota or US\$ 95.8 million) and the Fifth Review under the Resilience and Sustainability Facility arrangement (RSF). These decisions enable an immediate disbursement of SDR 78.78 million (about US\$ 105.6 million).

Amid an increasingly uncertain and shock prone environment, the new arrangements will help preserve external buffers while supporting the authorities' efforts to maintain macroeconomic stability and implementing structural reforms to address Mauritania's large development needs and the outstanding structural reforms.

Under the 2022-2026 ECF/EFF, Mauritania has shown a strong track record of policy implementation. Macroeconomic stability was maintained. A robust reform agenda has helped strengthen fiscal policy, develop the financial sector, including the FX market, overhaul the governance legal framework, and strengthen resilience to climate change. Program performance has been strong, with all end-December 2025 quantitative performance criteria met and the structural benchmark on the institutionalization of the fiscal rule into law implemented with some delay. The authorities completed the remaining four reform measures under the RSF, supporting the integration of climate considerations in public financial management, and strengthening the management of the water sector.

Building on the achievements of the 2022-2026 ECF/EFF, the new program will focus on (i) consolidating macroeconomic stability by strengthening macroeconomic institutions and policy frameworks; (ii) reducing poverty and strengthening private sector-led growth; and (iii) continuing to strengthen governance, including of public enterprises. The arrangements will also help catalyze support from Mauritania's development partners.

At the conclusion of the Executive Board's discussion, Mr. Okamura, Deputy Managing Director and Chair stated:

“Despite a highly uncertain external environment, Mauritania’s economy has continued to show resilience, supported by prudent and well-calibrated macroeconomic policies. Disciplined fiscal policy is contributing to the authorities’ medium-term objective of stabilizing public debt, and external buffers remain adequate. In parallel, the authorities have continued to strengthen macroeconomic policy frameworks and preserve stability.

"Program performance under the Extended Credit Facility (ECF) and Extended Fund Facility (EFF) arrangements has remained strong. The program under the Resilience and Sustainability Facility (RSF) has been successfully concluded, reflecting the authorities' commitment to advancing climate-related reforms alongside broader macroeconomic objectives.

"The authorities' commitment to prudent fiscal policy, supported by the institutionalization of the fiscal anchor, helps insulate the economy from commodity price volatility and supports debt sustainability. Continued efforts are needed to sustain revenue mobilization efforts, improve expenditure efficiency, advance SOE reforms, and preserve space for priority social and investment spending, including to protect the most vulnerable. The well-developed social registry provides a strong basis to improve the targeting of social spending to those most in need.

“Further progress has been made in modernizing the monetary policy framework. Looking ahead, strengthening liquidity management and further developing monetary policy instruments will remain important to anchor inflation expectations and support financial market development. Further efforts are also needed to deepen the foreign exchange market, which would help enhance exchange rate flexibility as an external shock absorber. Moreover, banking sector resilience needs further strengthening through effective supervision and enforcement of prudential regulations.

"Decisive implementation of structural reforms remains key to fostering higher, more inclusive, and private sector-led growth. Priorities include strengthening governance, further strengthening anti-corruption frameworks and enhancing transparency and accountability. Continued efforts to improve the business climate, deepen financial inclusion, and develop human capital will be essential to support diversification and improved social and long-term development outcomes.

“Sustained and effective implementation of the new 42-month ECF/EFF arrangements—supported by capacity development—will help anchor macroeconomic policies, address medium- and long-term economic challenges and mobilize development partner support.”

Mauritania: Selected Economic Indicators, 2021–27

<table><tr><td rowspan="2"></td><td rowspan="2">2021</td><td rowspan="2">2022</td><td rowspan="2">2023</td><td>2024</td><td colspan="2">2025</td><td>2026</td><td>2027</td></tr><tr><td>Est.</td><td>5th Review</td><td>Est.</td><td>5th Review</td><td>Projections</td></tr><tr><td colspan="4">National accounts and prices</td><td colspan="5">(Annual change in percent)</td></tr><tr><td>Real GDP</td><td>0.7</td><td>6.8</td><td>6.8</td><td>6.3</td><td>4.2</td><td>4.0</td><td>4.7</td><td>4.7</td></tr><tr><td>Real extractive GDP</td><td>-19.2</td><td>18.3</td><td>12.2</td><td>1.9</td><td>-1.2</td><td>-0.6</td><td>3.6</td><td>6.3</td></tr><tr><td>Real non-extractive GDP</td><td>6.0</td><td>3.8</td><td>5.6</td><td>7.3</td><td>5.5</td><td>5.1</td><td>5.0</td><td>4.3</td></tr><tr><td>Consumer prices (end of period)</td><td>3.2</td><td>3.2</td><td>3.2</td><td>3.1</td><td>2.0</td><td>4.1</td><td>3.0</td><td>4.5</td></tr><tr><td colspan="4">Central government operations</td><td colspan="5">(In percent of GDP, unless otherwise indicated)</td></tr><tr><td>Revenues and grants</td><td>22.6</td><td>25.0</td><td>22.3</td><td>22.2</td><td>24.1</td><td>23.5</td><td>25.2</td><td>25.0</td></tr><tr><td>Nonextractive</td><td>16.2</td><td>18.2</td><td>16.9</td><td>17.8</td><td>18.9</td><td>18.9</td><td>20.0</td><td>18.7</td></tr><tr><td>Taxes</td><td>11.7</td><td>13.4</td><td>12.5</td><td>13.9</td><td>14.7</td><td>14.7</td><td>15.5</td><td>14.3</td></tr><tr><td>Extractive</td><td>4.1</td><td>5.0</td><td>3.6</td><td>3.2</td><td>3.8</td><td>3.5</td><td>3.6</td><td>4.9</td></tr><tr><td>Expenditure and net lending</td><td>20.8</td><td>28.7</td><td>24.8</td><td>23.6</td><td>24.5</td><td>23.8</td><td>25.9</td><td>25.0</td></tr><tr><td>Of which: Current</td><td>13.0</td><td>17.2</td><td>16.2</td><td>14.9</td><td>13.7</td><td>13.5</td><td>13.7</td><td>14.3</td></tr><tr><td>Capital</td><td>7.8</td><td>11.5</td><td>8.6</td><td>8.7</td><td>10.8</td><td>10.2</td><td>12.1</td><td>10.7</td></tr><tr><td>Primary balance (excl. grants)</td><td>0.5</td><td>-4.5</td><td>-3.3</td><td>-1.6</td><td>-0.8</td><td>-0.6</td><td>-1.2</td><td>-0.5</td></tr><tr><td>Non-extractive primary balance (incl. grants)</td><td>-1.5</td><td>-7.7</td><td>-5.1</td><td>-3.5</td><td>-3.2</td><td>-3.0</td><td>-3.3</td><td>-4.0</td></tr><tr><td>Overall balance (in percent of GDP)</td><td>1.9</td><td>-3.7</td><td>-2.4</td><td>-1.4</td><td>-0.4</td><td>-0.3</td><td>-0.7</td><td>0.0</td></tr><tr><td>Public sector debt (in percent of GDP)</td><td>52.4</td><td>48.3</td><td>47.0</td><td>43.5</td><td>39.9</td><td>40.7</td><td>40.5</td><td>37.6</td></tr><tr><td colspan="9">External sector</td></tr><tr><td>Current account balance (in percent of GDP)</td><td>-8.6</td><td>-14.9</td><td>-8.7</td><td>-9.4</td><td>-6.3</td><td>-3.4</td><td>-6.9</td><td>-5.8</td></tr><tr><td>Excl. externally financed extractive capital goods imports</td><td>1.0</td><td>-0.8</td><td>-0.3</td><td>-1.4</td><td>-0.5</td><td>1.8</td><td>-1.3</td><td>-0.7</td></tr><tr><td>Gross official reserves (in millions of US$, eop)</td><td>2,347</td><td>1,877</td><td>2,032</td><td>1,921</td><td>1,922</td><td>2159</td><td>1,926</td><td>1869</td></tr><tr><td>In months of prospective non-extractive imports</td><td>8.2</td><td>6.2</td><td>6.4</td><td>5.9</td><td>5.5</td><td>5.9</td><td>5.5</td><td>5.5</td></tr><tr><td>External public debt (in millions of US$)</td><td>4,204</td><td>3,954</td><td>4,047</td><td>4,058</td><td>4,033</td><td>4052</td><td>4,290</td><td>4197.7</td></tr><tr><td>In percent of GDP</td><td>45.8</td><td>42.1</td><td>40.6</td><td>36.9</td><td>33.1</td><td>33.3</td><td>32.9</td><td>30.4</td></tr></table>

# ISLAMIC REPUBLIC OF MAURITANIA

June 9, 2026

REQUESTS FOR AN EXTENDED ARRANGEMENT UNDER THE EXTENDED FUND FACILITY AND ARRANGEMENT UNDER THE EXTENDED CREDIT FACILITY, CANCELLATION OF THE CURRENT ARRANGEMENTS UNDER THE EXTENDED FUND FACILITY AND THE EXTENDED CREDIT FACILITY, AND FIFTH REVIEW UNDER THE RESILIENCE AND SUSTAINABILITY FACILITY ARRANGEMENT

## EXECUTIVE SUMMARY

Context. Economic growth slowed to 4.0 percent in 2025 (compared to 6.3 percent in 2024), due to a contraction in the extractive sector and a slowdown in the non-extractive sector. Inflation has been on an upward trend since July 2025, with upward pressures partly explained by the disruptions along the Mali border, which affected key trade corridors. After widening in 2024, the current account (CA) narrowed in 2025, mainly reflecting lower imports related to the GTA project, and higher gold receipts alongside the start of LNG exports. The war in the Middle East has impacted Mauritania through an increased oil import bill and fiscal costs from the temporary subsidies under the newly introduced automatic fuel price mechanism, subsidies on butane gas cylinders, and targeted social protection measures. The social registry enables the government to expand targeted cash transfers in response to further adverse price developments, including increasing food prices. Structurally, persistent challenges, such as inadequate infrastructure, governance weaknesses, high vulnerability to external shocks, and limited economic diversification, continue to constrain Mauritania's long-term economic development. Additionally, frequent and severe climate-related disasters create large adaptation needs.

Implementation of the current Extended Credit Facility (ECF) and Extended Fund Facility (EFF) arrangements has been broadly on track, with all end-December 2025 targets for quantitative performance criteria (QPCs) and end-March indicative targets (ITs) met. The SB on the appointment of the members of the Anti-Corruption Authority's Directive Council was not met but implemented with delay (in April), and the SB on the institutionalization of the fiscal anchor was not met, but implemented with delay. The amendment to the Loi Organique de la Loi de Finance (LOLF) to introduce a fiscal rule on the non-extractive primary balance was adopted on May 15, 2026. An implementing

decree was adopted on June 3, 2026 to operationalize the fiscal rule, specifying, inter alia, the NEPD quantitative target and the definition of extractive revenues, clarifying institutional responsibilities, and establishing detailed provisions for escape clauses, monitoring, and correction mechanisms.

Program performance under the Resilience and Sustainability Facility (RSF) is on track. All reform measures (RM) assessed at the time of this review were completed.

Successor Program. Mauritania, under the 2022-2026 42-month ECF/EFF, has shown a strong track record of policy implementation to support macroeconomic stability. However, sustaining development ambitions while preserving external buffers has become challenging in the context of the war in the Middle East. As a result, Mauritania is facing present and prospective balance of payments (BOP) needs, that could widen considering risks to the baseline. The authorities notified the Fund of their intention to cancel the current ECF/EFF and requested successor 42-month arrangements under the ECF/EFF with a cumulative access of SDR 70.84 million (55 percent of quota, of which SDR 23.61 million or 18.33 percent of quota under the ECF and SDR 47.23 million or 36.67 percent of quota under the EFF). The program will focus on (i) consolidating macroeconomic stability by strengthening macroeconomic institutions and policy frameworks; (ii) reducing poverty and strengthening private sector-led growth; and (iii) continuing to strengthen governance, including of public enterprises. The arrangements will help catalyze support from Mauritania's development partners. The authorities consider the ECF/EFF to be the most suitable instrument to address their needs at this juncture. Staff takes note of the authorities' intention to cancel the current arrangements and supports their request for the new ECF/EFF arrangements.

CONTEXT 6
RECENT ECONOMIC DEVELOPMENTS AND STRUCTURAL REFORMS 7
OUTLOOK AND RISKS 11
PROGRAM PERFORMANCE 13
PROGRAM DISCUSSIONS 14
A. Fiscal Policy 14
B. Monetary Policy, Foreign Exchange, and Financial Sector Policies 16
C. Governance Reforms 20
D. Resilience and Sustainability Facility 20

Approved By
Taline Koranchelian
Jacques Miniane

Discussions took place during March 31 to April 10, 2026, in Nouakchott, Mauritania. The team comprised Felix Fischer (head), Onur Ozlu, Rana Fayez (all MCD), Dallal Bendjellal, (FAD), Yulia Ustyugova (SPR), Lamya Kejji (STA), and Younes Zouhar (Resident Representative), assisted by Ibrahima Ball and Moctar Bellamech (local economists). Ms. Fatimetou Yahya (OED) joined part of the discussions. Karman Singh provided research assistance, Sofia Cerna Rubinstein, Rodrigo Huguet, Ibrahima Kane, and Khalidou Harouna Ba provided administrative support. The team met with His Excellency President Mohamed Ould Ghazouani, Prime Minister Mokhtar Ould Diay, Governor of the Central Bank Mohamed Lamine Ould Dhehby, Minister of Economic Affairs and Development Abdallah Souleymane Cheikh Sidia, Minister of Education and the Reform of the Education System Houda Mint Babah, Minister of Health Tidjani Thiam, Minister of Energy and Oil Mohamed Ould Khaled, Minister of Mining and Industry Edy Ould Zeine, Minister of Public Lands, Public Estate, and Land Reform Mamadou Niang, Minister of Hydraulics and Sanitation Amal Mint Mouloud, Minister of Environment and Sustainable Development Messouda Baham Mohamed Laghdaf, other senior government officials, the civil society, the banking association and other representatives of the private sector, and the donor community.

## CONTENTS

A. Strengthening Macroeconomic Institutions and Policy Frameworks 22

B. Reducing Poverty and Strengthening Private Sector-Led Growth \_\_\_\_ 25

C. Improving Governance and Public Enterprises 26  
D. Program Modalities 28

STAFF APPRAISAL 29

## BOX

1. Sensitivity to Downside Risks from the War in the Middle East 13

## FIGURES

1. Real Sector Developments, 2014–2026 32
2. External Sector Developments, 2014–2026 33
3. Fiscal Sector Developments, 2014–2025 34
4. Monetary Sector Indicators, 2016–2026 35
5. Financial Sector Indicators, 2017–25 36

## TABLES

1. Macroeconomic Framework, 2020–2031 \_\_\_\_ 37
2a. Balance of Payments, 2020–2031 (In millions of U.S. dollars) \_\_\_\_ 38
2b. Balance of Payments, 2020–2031 (In percent of GDP) \_\_\_\_ 39
3a. Central Government Operations, 2020–2031 (In billions of MRU) \_\_\_\_ 40
3b. Central Government Operations, 2020–2031 (In percent of GDP) \_\_\_\_ 41
4. Monetary Survey, 2020–2031 \_\_\_\_ 42
5. Banking Soundness Indicators, 2010–2025 \_\_\_\_ 43


[中间内容因长度限制已省略]

et allocations and measurable social outcomes.

To ensure that broader structural gains translate into durable poverty reduction, expanding the reach and responsiveness of social protection frameworks remains vital. The authorities have adopted the National Social Protection Strategy (SNPS II 2025–2035), reinforcing their commitment to universal social protection and resilience against climate and economic shocks. Leveraging the Social Registry, which covers the poorest 40 percent of the population, the authorities rapidly deployed one-off emergency support under the El Aoun operation, to address the cost-of-living impacts of the war in the Middle East. Alongside the permanent social safety net program, Tekavoul, and its climate shock-responsive component, Tekavoul Choc, this coordinated response has been instrumental in delivering direct, targeted cash and food transfers to hundreds of thousands of vulnerable households. Furthermore, to manage the growing influx of refugees and ease the strain on host communities amidst declining ODA, the authorities have launched a comprehensive 2025 Response Plan targeting 471,000 beneficiaries, underscoring their commitment to regional solidarity and social cohesion. Going forward, the authorities are committed to expanding the National Social Registry and extending universal health insurance (CNASS) coverage to one million beneficiaries by 2027. Additionally, in tandem with the new automatic fuel pricing mechanism, the government deployed a separate targeted compensation mechanism (Tassanoud) through the Taazour agency, which provides direct cash transfers, calibrated to account for geographic remoteness and higher transport costs to households most exposed to energy price shocks.

## 3. Strengthening Governance and Public Enterprises Oversight

The authorities are intensifying their governance reform agenda, transitioning from legislative reforms to the effective implementation of the new institutional framework. Following the successful appointment of the Anti-Corruption Authority's (ACA) Directive Council, the immediate priority is to ensure the ACA is fully operationalized and resourced. To maintain momentum during the transitional period before the electronic platform is fully rolled out, the authorities issued a circular in March 2026 mandating the continued submission of asset declarations by all obligated high-level officials. Consequently, the collection of these declarations is proceeding, with the process for parliamentarians' declarations also in progress.

Building on the new SOE law, the authorities are taking decisive, structural steps to strengthen the performance and accountability of public enterprises. To address historical data gaps and improve the monitoring of SOEs, the authorities will adopt an IMF-developed tool to systematically compile and report financial indicators for the five largest commercial public enterprises (SB, end-September 2026), subsequently expanding this reporting coverage to the additional ten largest commercial enterprises (SB, end-December 2026). Moreover, they will adopt a comprehensive State ownership strategy by end-December 2027 to clarify financial objectives and will enforce fiscal transparency by including a consolidated table of all budgetary transfers and subsidies to SOEs in the 2027 Budget Law documentation (SB, end-December 2026).

The authorities are stepping up efforts to strengthen the anti-money laundering (AML/CFT) frameworks and public procurement transparency. In preparation for the upcoming MENAFATF mutual evaluation, the authorities have updated their National Risk Assessment to better target high-risk sectors and are actively expanding the Central Bank's risk-based AML/CFT supervision across financial institutions. Concurrently, to improve the efficiency and integrity of public spending, the government is reinforcing public procurement regulations by restricting the use of direct agreements, mandating independent audits for high-stake contracts, and enforcing the systematic collection and publication of beneficial ownership information for awarded companies. Finally, to guarantee accountability and close the loop on governance diagnostics, the authorities are enhancing the follow-up on oversight recommendations, notably by establishing a digital monitoring platform and granting the Court of Auditors direct access to the Ministry of Finance's information systems.

## CONCLUSION

Over the course of the 2022-26 completed arrangements, Mauritania has demonstrated remarkable economic resilience in the face of multiple global and regional shocks. The authorities successfully preserved macroeconomic stability, helping bring inflation down to low single digits, stabilizing public debt through strict adherence to their fiscal anchor, and maintaining adequate international reserves, all while advancing landmark climate and institutional reforms.

Building on these hard-won gains, the Mauritanian authorities remain firmly committed to their reform agenda. To navigate a difficult regional and global environment, the proposed successor program will serve as a critical policy anchor to transition from short-term stabilization to durable structural transformation. It will support stronger public institutions, a more dynamic private sector-led economy to reduce poverty, more efficient and better targeted social support systems, and further improvements in public sector governance.

In light of the strong program performance and the authorities' steadfast commitment, we would appreciate Executive Directors' support for the approval of the new 42-month ECF/EFF arrangements, and the completion of the Fifth Review under the RSF.
"""
