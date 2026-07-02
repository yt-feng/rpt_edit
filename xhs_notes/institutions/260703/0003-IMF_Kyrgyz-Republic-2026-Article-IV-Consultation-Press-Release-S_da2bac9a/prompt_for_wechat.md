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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
IMF Country Report No. 26/163

## KYRGYZ REPUBLIC

July 2026

## 2026 ARTICLE IV CONSULTATION—PRESS RELEASE; STAFF REPORT; AND STATEMENT BY THE EXECUTIVE DIRECTOR FOR KYRGYZ REPUBLIC

Under Article IV of the IMF's Articles of Agreement, the IMF holds bilateral discussions with members, usually every year. In the context of the 2026 Article IV consultation with the Kyrgyz Republic, the following documents have been released and are included in this package:

\- A Press Release summarizing the views of the Executive Board as expressed during its June 3, 2026, consideration of the staff report that concluded the Article IV consultation with the Kyrgyz Republic.

\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on June 3, 2026, following discussions that ended on April 1, 2026, with the officials of the Kyrgyz Republic on economic developments and policies. Based on information available at the time of these discussions, the staff report was completed on May 14, 2026.

• An Informational Annex prepared by the IMF staff.

\- A Debt Sustainability Analysis prepared by the staffs of the IMF the International Development Association.

• A Statement by the Executive Director for the Kyrgyz Republic.

The documents listed below have been or will be separately released.

Selected Issues

The IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.

Copies of this report are available to the public from

## IMF Executive Board Concludes 2026 Article IV Consultation with Kyrgyz Republic

## FOR IMMEDIATE RELEASE

\- The Kyrgyz Republic has sustained strong economic growth for the fourth consecutive year, but inflation is now above the central bank's target.

• Growth is expected to moderate as reexport and trade-related activities plateau.

\- The favorable economic performance provides a window of opportunity to enhance resilience, strengthen policy buffers, and support inclusive growth.

Washington, DC – June 4, 2026: The Executive Board of the International Monetary Fund (IMF) completed the Article IV Consultation for the Kyrgyz Republic. $^{1}$ The authorities need more time to consider the publication of the Staff Report prepared for this consultation. $^{2}$

The Kyrgyz Republic continues to record strong economic performance as the economy transitions from low-income status. Since 2022, expanded trade flows, robust remittance and capital inflows, and strong construction activity supported by government spending have underpinned rapid growth. Output is estimated to have grown by 11 percent in 2025. At the same time, inflation rose to 11 percent in March 2026, well above the central bank's 5–7 percent target range.

Growth is expected to moderate as recent trade-related gains fade but will be buoyed by large infrastructure projects over the medium term. Inflation is likely to remain high through 2027 before easing gradually if macroeconomic policies are tightened appropriately. After fiscal surpluses in 2023–25, the budget is projected to move into deficit in 2026, mainly because of higher public wages and capital spending. Public debt remains sustainable, but financing needs are sizable. Strong remittances and high gold prices are expected to support the external position.

Even though the Kyrgyz Republic has limited exposure to the war in the Middle East, sustained high oil prices could add to inflation pressures. With heightened global uncertainty, accelerating reforms will be key to enhance resilience, strengthen policy buffers, and support inclusive growth.

## Executive Board Assessment

Executive Directors agreed with the thrust of the staff appraisal. They welcomed the Kyrgyz Republic's rapid economic growth and declining poverty, while noting downside risks, emerging signs of overheating, and elevated inflation pressures. In this context, Directors underscored the need for careful policy recalibration, supported by Fund capacity development, to enhance resilience, strengthen buffers, and foster private sector-led inclusive growth.

Directors underscored the need to bolster the fiscal position by strengthening revenue mobilization to create space for priority infrastructure and targeted social spending, while containing expenditure on energy subsidies and wages. They called for enhancing public financial, investment, and debt management to strengthen efficiency, resilience, and fiscal sustainability. Directors also emphasized the need to fully capture quasi-fiscal operations and SOE risks, including ensuring that the operations of the Stabilization Fund are transparently reflected in fiscal reporting and risk assessments.

Directors supported maintaining an appropriately tight and data-dependent monetary policy stance until inflation durably returns to the central bank's target range. They emphasized the importance of strengthening the operational framework and encouraged the authorities to strengthen the independence of the central bank. Greater exchange rate flexibility and more diversified reserves would further enhance external resilience.

Noting rapid credit growth, high NPLs and a deepening bank–sovereign nexus, Directors called for heightened financial supervisory vigilance and capacity, focusing on a risk-based approach and proactive macroprudential measures. They also noted the need for enhanced AML/CFT measures and stronger supervision and governance of virtual asset service providers.

Directors called for ambitious structural reforms to support private sector-led growth. They agreed that priority areas include SOE reform and strengthening the business environment, competition, the rule of law, and anti-corruption. Directors supported ongoing efforts to reduce informality and labor market rigidities, invest in human capital and digital infrastructure, and harness the gains of AI. Strengthening external sector and national account statistics is essential to enhance macroeconomic surveillance.

<table><tr><td colspan="10">Table 1. Kyrgyz Republic: Selected Economic Indicators</td></tr><tr><td colspan="10">I. Social and Demographic Indicators</td></tr><tr><td>Population (in millions, 2024)</td><td colspan="2">7.3</td><td colspan="5">Gini coefficient (2023)</td><td colspan="2">0.26</td></tr><tr><td>Unemployment rate (2024)</td><td colspan="2">3.7</td><td colspan="5">Life expectancy at birth in years (2025)</td><td colspan="2">72.1</td></tr><tr><td>Poverty rate (in percent, national definition, 2024)</td><td colspan="2">25.7</td><td colspan="5">Adult literacy rate (percent of popul., 2025)</td><td colspan="2">99.6</td></tr><tr><td>Per capita GDP (in million U.S. dollars, World Bank, 2024)</td><td colspan="2">2,420</td><td colspan="5">Under-five mortality (per 1000 live births, 2025, est.)</td><td colspan="2">12.6</td></tr><tr><td colspan="10">II. Economic Indicators</td></tr><tr><td rowspan="2"></td><td>2023</td><td>2024</td><td>2025</td><td>2026</td><td>2027</td><td>2028</td><td>2029</td><td>2030</td><td>2031</td></tr><tr><td></td><td></td><td>Est.</td><td></td><td></td><td>Proj.</td><td></td><td></td><td></td></tr><tr><td colspan="10">Real Sector</td></tr><tr><td>Nominal GDP (in billions of soms)</td><td>1,334</td><td>1,583</td><td>1,976</td><td>2,342</td><td>2,761</td><td>3,204</td><td>3,645</td><td>4,108</td><td>4,607</td></tr><tr><td>Nominal GDP (in millions of U.S. dollars)</td><td>15,187</td><td>18,175</td><td>22,625</td><td>25,817</td><td>28,298</td><td>30,731</td><td>33,101</td><td>35,419</td><td>37,597</td></tr><tr><td>Real GDP (growth in percent)</td><td>9.0</td><td>11.5</td><td>11.1</td><td>6.1</td><td>5.8</td><td>6.1</td><td>5.4</td><td>5.3</td><td>5.2</td></tr><tr><td>GDP per capita (in U.S. dollars)</td><td>2,191</td><td>2,568</td><td>3,131</td><td>3,502</td><td>3,759</td><td>3,998</td><td>4,222</td><td>4,424</td><td>4,599</td></tr><tr><td>Consumer prices (12-month percent change, eop)</td><td>7.3</td><td>6.3</td><td>9.4</td><td>12.5</td><td>10.5</td><td>8.5</td><td>7.5</td><td>6.5</td><td>6.5</td></tr><tr><td>Consumer prices (12-month percent change, average)</td><td>10.8</td><td>5.0</td><td>8.2</td><td>11.7</td><td>11.4</td><td>9.4</td><td>7.9</td><td>7.0</td><td>6.5</td></tr><tr><td colspan="10">General government finances (in percent of GDP) 1/</td></tr><tr><td>Revenue</td><td>34.5</td><td>34.5</td><td>38.5</td><td>33.4</td><td>31.4</td><td>31.2</td><td>31.1</td><td>30.8</td><td>30.6</td></tr><tr><td>Of which: Tax revenue</td><td>21.9</td><td>21.7</td><td>23.0</td><td>22.6</td><td>22.6</td><td>22.6</td><td>22.7</td><td>22.6</td><td>22.5</td></tr><tr><td>Expense</td><td>26.1</td><td>25.7</td><td>26.3</td><td>27.5</td><td>25.6</td><td>25.3</td><td>25.3</td><td>25.4</td><td>25.3</td></tr><tr><td>Gross operating balance</td><td>8.4</td><td>8.8</td><td>12.2</td><td>5.8</td><td>5.8</td><td>6.0</td><td>5.9</td><td>5.4</td><td>5.4</td></tr><tr><td>Net acquisition of nonfinancial assets</td><td>6.8</td><td>6.9</td><td>9.6</td><td>9.7</td><td>9.3</td><td>9.5</td><td>8.9</td><td>8.2</td><td>8.1</td></tr><tr><td>Overall balance (net lending/borrowing) 2/</td><td>1.6</td><td>2.0</td><td>2.6</td><td>-3.8</td><td>-3.5</td><td>-3.6</td><td>-3.1</td><td>-2.8</td><td>-2.8</td></tr><tr><td>Net lending/borrowing excluding CKU railways</td><td>1.6</td><td>2.0</td><td>3.0</td><td>-2.6</td><td>-2.5</td><td>-2.6</td><td>-2.5</td><td>-2.8</td><td>-2.8</td></tr><tr><td>Primary net lending/ borrowing</td><td>2.6</td><td>3.1</td><td>3.7</td><td>-2.8</td><td>-1.9</td><td>-1.7</td><td>-1.0</td><td>-0.6</td><td>-0.4</td></tr><tr><td>Total government debt 3/</td><td>42.0</td><td>36.2</td><td>39.4</td><td>41.4</td><td>40.6</td><td>40.5</td><td>40.4</td><td>40.6</td><td>40.8</td></tr><tr><td>Of which domestic debt</td><td>10.9</td><td>11.3</td><td>15.8</td><td>14.8</td><td>13.3</td><td>12.3</td><td>12.6</td><td>16.0</td><td>18.5</td></tr><tr><td colspan="10">Monetary sector</td></tr><tr><td>Reserve money (percent change, eop)</td><td>9.9</td><td>17.5</td><td>29.7</td><td>17.2</td><td>17.2</td><td></td><td></td><td></td><td></td></tr><tr><td>Broad money (percent change, eop)</td><td>15.0</td><td>31.9</td><td>43.3</td><td>36.4</td><td>19.2</td><td></td><td></td><td></td><td></td></tr><tr><td>Credit to private sector (percent change, eop)</td><td>25.9</td><td>33.9</td><td>49.0</td><td>27.8</td><td>26.5</td><td></td><td></td><td></td><td></td></tr><tr><td>Credit to private sector (in percent of GDP)</td><td>19.8</td><td>22.4</td><td>26.7</td><td>28.8</td><td>30.9</td><td></td><td></td><td></td><td></td></tr><tr><td>Velocity of broad money 4/</td><td>2.6</td><td>2.4</td><td>2.0</td><td>1.8</td><td>1.8</td><td></td><td></td><td></td><td></td></tr><tr><td>Policy Rate 5/</td><td>13.0</td><td>9.0</td><td>11.0</td><td>...</td><td>...</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">External sector</td></tr><tr><td>Current account balance (in percent of GDP) 6/</td><td>-44.9</td><td>-22.6</td><td>-24.4</td><td>-7.3</td><td>-7.0</td><td>-6.2</td><td>-5.7</td><td>-5.4</td><td>-5.3</td></tr><tr><td>Export of goods and services (in millions of U.S. dollars)</td><td>5,522</td><td>8,459</td><td>7,229</td><td>12,319</td><td>13,263</td><td>14,503</td><td>15,615</td><td>16,680</td><td>17,718</td></tr><tr><td>Export growth (percent change)</td><td>52.0</td><td>53.2</td><td>-14.5</td><td>70.4</td><td>7.7</td><td>9.4</td><td>7.7</td><td>6.8</td><td>6.2</td></tr><tr><td>Import of goods and services (in millions of U.S. dollars)</td><td>14,461</td><td>15,105</td><td>15,563</td><td>17,299</td><td>18,528</td><td>19,969</td><td>21,315</td><td>22,814</td><td>24,282</td></tr><tr><td>Import growth (percent change)</td><td>35.6</td><td>4.5</td><td>3.0</td><td>11.2</td><td>7.1</td><td>7.8</td><td>6.7</td><td>7.0</td><td>6.4</td></tr><tr><td>Gross International reserves (in millions of U.S. dollars) 7/</td><td>3,044</td><td>4,923</td><td>8,698</td><td>9,246</td><td>8,904</td><td>8,826</td><td>8,636</td><td>7,654</td><td>6,926</td></tr><tr><td>Gross reserves (months of next year imports, eop)</td><td>2.4</td><td>3.8</td><td>6.0</td><td>6.0</td><td>5.4</td><td>5.0</td><td>4.5</td><td>3.8</td><td>3.2</td></tr><tr><td>Gross reserves (months of next year imports adjusted for re-exports, eop)</td><td>2.4</td><td>4.0</td><td>7.3</td><td>7.3</td><td>6.5</td><td>6.1</td><td>5.5</td><td>4.6</td><td>3.9</td></tr><tr><td>External public debt outstanding (in percent of GDP)</td><td>31.1</td><td>24.9</td><td>23.6</td><td>26.6</td><td>27.4</td><td>28.2</td><td>27.8</td><td>24.6</td><td>22.3</td></tr><tr><td>External public debt service-to-export ratio (in percent) 8/</td><td>6.4</td><td>4.5</td><td>7.3</td><td>3.8</td><td>4.2</td><td>4.4</td><td>4.9</td><td>10.0</td><td>8.6</td></tr><tr><td colspan="10">Memorandum items:</td></tr><tr><td>Exchange rate (soms per U.S. dollar, average)</td><td>87.8</td><td>87.1</td><td>87.4</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Real effective exchange rate (2010=100) (average)</td><td>116.1</td><td>121.6</td><td>127.7</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td colspan="10">Sources: Kyrgyz authorities; and IMF staff estimates and projections.</td></tr><tr><td colspan="10">1/ General Government comprises the State Government, the Social Fund, and the Mandatory Health Insurance Fund (MHIF).</td></tr><tr><td colspan="10">2/ Includes loans by the State Government to State-Owned Enterprises in the energy sector.</td></tr><tr><td colspan="10">3/ Total Public and Publicly Guaranteed Debt, calculated at end-period exchange rates.</td></tr><tr><td colspan="10">4/ Twelve-month GDP over end-period broad money.</td></tr><tr><td colspan="10">5/ End-of-year rate.</td></tr><tr><td colspan="10">6/ Adjusted for re-exports as of 2026.</td></tr><tr><td colspan="10">7/ Gross International Reserves exclude reserve assets in non-convertible currencies.</td></tr><tr><td colspan="10">8/ External Public and Publicly Guaranteed Debt.</td></tr></table>

# KYRGYZ REPUBLIC

## STAFF REPORT FOR THE 2026 ARTICLE IV CONSULTATION

May 14, 2026

## KEY ISSUES

Context: The Kyrgyz Republic has sustained strong economic growth for the fourth consecutive year. The outlook, is however clouded by significant downside risks. The overall favorable economic performance provides a window of opportunity to accelerate reforms that enhance resilience, strengthen policy buffers, and make room for private sector-led growth.

## Recommendations:

\- Fiscal policy. Investment in infrastructure and human capital needs to be balanced with the creation of fiscal space and prudent debt management. In this context, stronger PFM measures and proper budget classification would enhance the efficiency and transparency of public spending. In the longer term, fiscal prospects would be safeguarded by a careful assessment of the public pension system.

\- Monetary and exchange rate policies. To bring inflation in line with the National Bank of the Kyrgyz Republic's target, the monetary policy stance may need to be tightened further should inflation not be on a firmly downward trajectory, in the context of reinforcing the independence of the central bank. The economy's resilience to external shocks would be enhanced by greater exchange rate flexibility and diversification of reserve composition.

\- Financial sector policies. The financial sector would benefit from strengthened supervisory capacity and risk monitoring.

\- Structural reforms—in particular, creating the space for private sector-led growth—remain crucial, in line with past staff advice.

\- Data adequacy. Strengthening the quality of data, especially in the external sector and in national accounts statistics, is essential.

Discussions were held during March 18–April 1, 2026 in Bishkek. The staff team comprised Dmitry Gershenson (head), Khaled Abdelkader, Nasir Rao, Jean van Houtte (all MCD), Anh Nguyen (FAD), Maksym Markevych (LEG), Farid Talishli (Resident Representative), Erkeaim Shambetova and Anvar Muratkhanov, with support from Aigerim Toigonbaeva (all Resident Representative office). Patryk Loszewski and Lilia Kadyrberdieva (OED) participated in key meetings. Nihal Haider, Elyad Shojaei, and Svetlana Zolotareva assisted from the headquarters. The mission met with central bank Governor Baketaev, Minister of Finance Suinaliev, former central bank Governor Turgunbaev, and other officials, as well as representatives of the business and diplomatic communities and development partners.

## CONTENTS

CONTEXT 4
RECENT MACROECONOMIC DEVELOPMENTS 4
OUTLOOK AND RISKS 5
POLICY DISCUSSIONS 7
A. Fiscal Policy 7
B. Monetary and Exchange Rate Policies 8
C. Financial Sector Policies 9
D. Structural Reforms 11
E. Data Adequacy 12
STAFF APPRAISAL 13
FIGURES
1. Real Sector and Social Indicators 15
2. External and Monetary Sectors 16
3. Fiscal Sector 17
4. Financial Soundness Indicators 18
TABLES
1. Selected Economic Indicators 19
2. National Accounts, 2023-2031 20
3. Balance of Payments, 2023-2031 21
4. NBKR Accounts, 2023-2027 22
5. Monetary Survey, 2023-2027 23

6. State Government Finances, 2023-2031 (in millions of soms) \_\_\_\_ 24
7. State Government Finances, 2023-2031 (in percent of GDP) \_\_\_\_ 25
8. General Government Finance, 2023-2031, GFSM 2014 Presentation 1/\_\_\_\_ 26
9. General Government Finances, 2023-2031, GFSM 2014 Presentation \_\_\_\_ 27
10. Selected Financial Soundness Indicators, 2020-2025 \_\_\_\_ 28

## ANNEXES

I. Implementation of Key Recommendations of the 2025 Article IV Consultation \_\_\_\_ 29
II. Risk Assessment Matrix \_\_\_\_ 32
III. External Sector Assessment \_\_\_\_ 38
IV. Data Issues \_\_\_\_ 42
V. Assessing Fiscal Risks in the Public Pension System of the Kyrgyz Republic \_\_\_\_ 45
VI. Artificial Intelligence Exposure and Preparedness \_\_\_\_ 51
VII. Mitigation of Cross-border Financial Integrity Risks in Kyrgyz Republic \_\_\_\_ 57

## CONTEXT

1. The Kyrgyz Republic is transitioning from low-income status. Since 2022, expanded trade flows, robust remittance and capital inflows, and strong construction activity supported by government spending have underpinned rapid growth. Real GDP expanded by 47 percent between 2021 and 2025, making the Kyrgyz Republic the third-fastest-growing economy in the world. During this period, per capita GDP in U.S. dollars doubled, reaching 3,100 in 2025.

2. The current favorable economic environment provides an opportunity to accelerate reforms. In June 2025, the authorities adopted the National Development Program (NDP) 2030. Th

[中间内容因长度限制已省略]

The authorities recognize the importance of carefully assessing the public pension system to safeguard long-term fiscal sustainability. The authorities view the Stabilization Fund (SF) as an extra-budgetary fund that plays an important role in safeguarding fiscal resilience and supporting sustainable socio-economic development. The SF serves both savings and stabilization functions, including: (i) ensuring continuity of socio-economic development during global downturns; (ii) mitigating the impact of adverse external shocks on the domestic economy and public finances; and (iii) providing resources for deficit financing to address unforeseen expenditures and maintain budget balance in the event of revenue shortfalls. Together with measures to further improve expenditure efficiency, these reforms are aimed at reducing fiscal vulnerabilities and limiting reliance on external borrowing.

Prudent debt management remains central to the authorities' policy framework. While flagship infrastructure projects continue to be financed primarily through concessional lending from international financial institutions, the authorities are mindful of the costs and risks associated with external borrowing on commercial terms and recognize the importance of careful planning of external debt maturities to avoid pressure on the treasury's liquidity position and risks to international reserves. The authorities emphasize that external financing is expected to be directed predominantly toward high-return infrastructure investments.

## Monetary policy and financial sector

Monetary conditions were tightened amid intensifying external and domestic inflationary factors. Monetary policy remains focused on containing inflation and safeguarding financial stability, with the NBKR maintaining a price-stability-oriented framework aimed at achieving inflation targets within the range of 5-7 percent in the medium term.

The inflation outlook in the Kyrgyz Republic remains sensitive to external conditions. The primary external risks are linked to ongoing geopolitical tensions, price volatility in global food markets, and potential disruptions in global supply chains. Domestic inflation factors are more predictable in nature and are primarily driven by sustained domestic demand and the implementation of tariff policies. Collectively, these conditions shape the prospective trajectory of inflation, with risks mostly stemming from external factors.

Against this backdrop, the NBKR continues to closely monitor and assess inflation drivers. Consequently, the NBKR's key policy rate has been maintained at 12 percent while establishing a symmetric and narrower interest rate corridor. On May 26, the overnight deposit rate—used to remunerate banks' excess liquidity—was further increased from 6 to 10 percent. Effective June 2025, the NBKR transitioned to issuing longer-term notes, specifically with maturities of three and six months. Sustaining tight monetary conditions will create a solid foundation for bringing inflation down to the 5-7 percent range over the medium term.

In the financial sector, the NBKR remains well-positioned to address and closely monitor elevated levels of non-performing loans and rapid credit expansion. The authorities recognize the challenges associated with crypto assets and are actively addressing emerging risks stemming from the rapidly evolving virtual assets sector. Efforts are underway to establish a robust regulatory response, supported by clearly defined institutional mandates. In parallel, the authorities are committed to strengthening the effectiveness of AML/CFT frameworks, while enhancing the supervision and governance of Virtual Asset Service Providers.

In response to Western sanctions affecting Kyrgyzstan's financial sector, the authorities have adopted a two-pronged strategy. This approach combines targeted domestic enforcement measures—aimed at preventing exposure to secondary sanctions—with active diplomatic

engagement to address and mitigate external constraints. Key measures undertaken include conducting audits of the banking sector, strengthening oversight of virtual asset activities, suspending the operations of firms exposed to sanctions risks, and maintaining ongoing diplomatic dialogue with international partners.

## Structural reforms

The economic policy agenda remains focused on preserving macroeconomic stability and strengthening resilience, while recognizing the need for further reforms to reduce informality, enhance competition, and foster more private sector-driven and inclusive growth. The authorities are committed to advancing governance reforms, including the effective implementation of the 2025 Anti-Corruption Strategy.

Reducing informality remains critical to achieving inclusive growth. SMEs account for approximately 50 percent of GDP; however, they continue to face regulatory constraints, and relatively few are able to scale. In response, reform efforts are now underway to implement an improved Investment Law with stronger investor protections, improved arbitration mechanisms, and streamlined licensing and permitting processes through digitalization and the reduction of administrative burdens. Continued efforts to improve skills matching, labor mobility, and access to finance for SMEs will be essential to facilitating their transition to the formal sector.

The authorities also recognize the transformative potential of artificial intelligence and are committed to harnessing its applications to improve public service delivery and support broader socio-economic development. In this context, they plan to further strengthen the regulatory framework and continue investing in digital infrastructure.
"""
