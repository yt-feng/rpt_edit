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
ISRAEL

July 2026

# 2026 ARTICLE IV CONSULTATION—PRESS RELEASE; STAFF REPORT; AND STATEMENT BY THE ALTERNATE EXECUTIVE DIRECTOR FOR ISRAEL

Under Article IV of the IMF's Articles of Agreement, the IMF holds bilateral discussions with members, usually every year. In the context of the 2026 Article IV consultation with Israel, the following documents have been released and are included in this package:

\- A Press Release summarizing the views of the Executive Board as expressed during its June 24, 2026 consideration of the staff report that concluded the Article IV consultation with Israel.

\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on June 24, 2026, following discussions that ended on February 5, 2026, with the officials of Israel economic developments and policies. Based on information available at the time of these discussions, the staff report was completed on June 10, 2026.

• An Informational Annex prepared by the IMF staff.

• A Statement by the Alternate Executive Director for Israel.

The documents listed below have been or will be separately released.

Selected Issues

The IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.

Copies of this report are available to the public from

International Monetary Fund • Publication Services
PO Box 92780 • Washington, D.C. 20090
Telephone: (202) 623-7430 • Fax: (202) 623-7201
E-mail: publications@imf.org Web: http://www.imf.org

International Monetary Fund
Washington, D.C.

# IMF Executive Board Concludes 2026 Article IV Consultation with Israel

FOR IMMEDIATE RELEASE

\- The elevated regional tensions are casting a shadow on Israel's economy. Growth forecasts for 2026 have been revised down to 3.5 percent from 4.8 percent before the war in the Middle East, while inflation is expected to rise temporarily due to higher energy prices and supply constraints despite shekel appreciation.

\- The conflicts' economic repercussions and longstanding labor market challenges weigh on the medium-term outlook.

\- With medium-term growth challenges looming, key priorities include rebuilding fiscal buffers, raising labor supply and productivity, and ensuring price and financial stability

Washington, DC – July 1, 2026: The Executive Board of the International Monetary Fund (IMF) completed the Article IV Consultation for Israel on June 24, 2026. $^{1}$

The elevated regional tensions are casting a shadow on Israel's economy. Growth forecasts for 2026 have been revised down to 3.5 percent from 4.8 percent before the war in the Middle East, reflecting a sharp contraction in the first quarter followed by a modest rebound over the remainder of the year. Inflation is expected to rise temporarily in the near term, due to higher energy prices and supply constraints despite shekel appreciation. Risks to the growth outlook are tilted to the downside and the inflation outlook to the upside, with deeper and more prolonged regional conflicts remaining the key concern.

Amid ongoing hostilities in the Middle East, defense expenditure is expected to remain high, and labor supply constrained by military mobilization and reduced availability of non-Israeli workers. These pressures would compound longstanding structural challenges—such as persistently low labor-market participation among certain groups—and weigh on Israel’s medium-term economic outlook.

## Executive Board Assessment $^{2}$

The Executive Directors welcomed that the economy has shown resilience, despite repeated shocks. Directors, however, noted that elevated regional geopolitical uncertainty and long-standing structural impediments are expected to weigh on the outlook. Furthermore, renewed intensification of regional tensions remains a key downside risk. Accordingly, Directors emphasized the need to implement prudent policies to safeguard macroeconomic stability and advance structural reforms to boost growth potential.

Directors welcomed the authorities' commitment to fiscal discipline and emphasized that gradual, credible fiscal consolidation is important to rebuild buffers and stabilize public debt. Noting the elevated defense spending and already low levels of civil spending, Directors considered that fiscal adjustment should rely primarily on revenue measures and efforts to enhance spending efficiency. They highlighted that a comprehensive review of the tax system, including tax expenditures, would help improve its simplicity, efficiency, and equity.

Directors welcomed the authorities' efforts to bring inflation back to the target range. They agreed that a moderately tight, data-dependent monetary policy stance remains appropriate to safeguard price stability, given inflationary pressures arising from higher energy prices and supply shocks. Directors highlighted that financial sector systemic risks appear contained and that banks remain well-capitalized, liquid, and profitable. Nonetheless, they emphasized the need for continued vigilance, particularly with respect to banks' real estate exposures. Directors recommended continued strengthening of stress testing frameworks, extending borrower-based measures to nonbank financial institutions, and careful implementation of Basel III requirements. While welcoming recent reforms to strengthen the BOI's resolution powers, they advised further progress on enhancing the crisis management framework. Directors also encouraged continued efforts to strengthen the AML/CFT framework.

Directors stressed that advancing structural reforms is critical to boost potential growth and support fiscal sustainability. While welcoming recent progress, they underscored the need to address persistent gaps in labor force participation and skills, particularly among fast-growing population groups. Directors welcomed progress in trade reforms and called for further efforts to improve product markets and infrastructure. They emphasized the importance of ensuring an adequate and sufficiently skilled labor supply to maintain the competitive edge in high-tech, including AI. Strengthening active labor market policies to facilitate reskilling and labor mobility is also important.

<table><tr><td rowspan="2"></td><td rowspan="2">2024</td><td rowspan="2">2025</td><td>2026</td><td>2027</td></tr><tr><td colspan="2">Proj.</td></tr><tr><td colspan="5">Output</td></tr><tr><td>Real GDP growth (percent change)</td><td>1.0</td><td>2.9</td><td>3.5</td><td>4.4</td></tr><tr><td colspan="5">Employment</td></tr><tr><td>Unemployment (percent)</td><td>3.0</td><td>3.0</td><td>3.0</td><td>3.1</td></tr><tr><td colspan="5">Prices</td></tr><tr><td>Inflation (period average, percent change)</td><td>3.1</td><td>3.0</td><td>2.3</td><td>2.1</td></tr><tr><td colspan="5">General government finances</td></tr><tr><td>Revenue (percent of GDP)</td><td>35.6</td><td>38.3</td><td>38.0</td><td>37.2</td></tr><tr><td>Expenditure (percent of GDP)</td><td>43.7</td><td>43.5</td><td>44.2</td><td>42.4</td></tr><tr><td>Fiscal balance (percent of GDP)</td><td>-8.1</td><td>-5.2</td><td>-6.2</td><td>-5.1</td></tr><tr><td>Public debt (percent of GDP)</td><td>67.7</td><td>68.4</td><td>70.1</td><td>70.7</td></tr><tr><td colspan="5">Central government finances</td></tr><tr><td>Revenue (percent of GDP)</td><td>24.2</td><td>26.1</td><td>25.8</td><td>25.2</td></tr><tr><td>Expenditure (percent of GDP)</td><td>31.0</td><td>30.8</td><td>31.1</td><td>29.6</td></tr><tr><td>Fiscal balance (percent of GDP)</td><td>-6.8</td><td>-4.7</td><td>-5.3</td><td>-4.4</td></tr><tr><td colspan="5">Monetary and credit</td></tr><tr><td>Broad money (percent change)</td><td>8.1</td><td>6.5</td><td>...</td><td>...</td></tr><tr><td>Credit to the private sector (percent change)</td><td>9.0</td><td>12.8</td><td>...</td><td>...</td></tr><tr><td>3-month Treasury bill interest rate (percent)</td><td>4.3</td><td>4.3</td><td>...</td><td>...</td></tr><tr><td colspan="5">Balance of payments</td></tr><tr><td>Current account (percent of GDP)</td><td>2.9</td><td>1.5</td><td>1.3</td><td>1.8</td></tr><tr><td>External debt (percent of GDP)</td><td>27.2</td><td>27.0</td><td>...</td><td>...</td></tr><tr><td>Foreign reserves (end-of-period, billions of US$)</td><td>214.6</td><td>229.5</td><td>...</td><td>...</td></tr><tr><td colspan="5">Exchange rates</td></tr><tr><td>NIS per U.S. dollar (period average)</td><td>3.7</td><td>3.5</td><td>...</td><td>...</td></tr><tr><td>REER (percent change)</td><td>0.3</td><td>6.7</td><td>...</td><td>...</td></tr></table>

# ISRAEL

# STAFF REPORT FOR THE 2026 ARTICLE IV CONSULTATION

June 10, 2026

## KEY ISSUES

Context. Elevated regional tensions have tested Israel's economic resilience. Amid ongoing hostilities in the Middle East, defense expenditure is expected to remain high, and labor supply constrained by military mobilization and reduced availability of non-Israeli workers. These pressures would compound longstanding structural challenges—such as persistently low labor-market participation among certain groups—and weigh on Israel's medium-term economic outlook.

Outlook and risks. The baseline assumes that the ceasefire in the Middle East largely holds, while geopolitical tensions remain elevated. Staff project output growth at 3.5 percent in 2026, down from 4.8 percent before the Middle East war, reflecting a sharp contraction in the first quarter followed by a modest rebound over the remainder of the year. The medium-term outlook is weaker, with potential growth forecast at around 3.5 percent, about 0.5 percentage point below its pre-2023 average. Downside risks mainly stem from deeper and more prolonged regional conflicts; upside risks include lasting regional geopolitical stability that improves regional security and expands participation in the Abraham Accords. Inflation is expected to stay slightly above 2 percent in 2026, reflecting higher global energy prices and tighter supply constraints despite shekel appreciation, with risks tilted to the upside. Public debt is projected to steadily rise, with higher defense spending pressures reducing fiscal space.

Policy recommendations. Key priorities include rebuilding fiscal buffers, raising labor supply and productivity, and ensuring price and financial stability.

\- Fiscal policy. Given elevated deficits and rising debt, a gradual and credible consolidation is needed to stabilize debt and rebuild fiscal buffers. With defense spending elevated, essential civil spending—especially infrastructure—risks being crowded out. Fiscal adjustment should focus on growth-friendly revenue measures, while strengthening spending efficiency remains important.

\- Structural. Raising labor supply and productivity is now more urgent to overcome post-conflict challenges and lift medium-term growth. Priorities include increasing labor force participation across the population, improving infrastructure, advancing product market reforms, and maintaining a competitive edge in high tech.

\- Monetary policy. A moderately tight monetary policy stance should be maintained under the baseline, where inflation is expected to rise temporarily due to higher energy prices and supply constraints. The BOI should continue to closely monitor war-related effects on labor supply, the pass-through of higher energy prices and exchange rate movements, and the impact of the latest rate cut on financial conditions and domestic demand, and stand ready to adjust course if incoming data or the heightened risk environment indicate meaningful deviations from the baseline.

\- Financial sector policy. The financial system remains resilient, with banks well capitalized, liquid, and profitable. However, banks' sizable exposure to real estate poses risk, especially as the ongoing housing-market adjustment is marked by weakening prices and transactions. Financial supervisors should continue to closely monitor risks and ensure that banks rigorously assess real estate exposures and update provisions.

Discussions were held in Jerusalem and Tel Aviv from January 25–February 5, 2026, and follow-up virtual meetings were held on May 7, 2026. The team comprised Kotaro Ishi (head), Pablo Druck, Ozge Emeksiz, Yinqiu Lu, Vahram Stepanyan (all EUR), and Vincent Tang (FAD). Carlos Acosta (LEG) participated in financial integrity-related discussions virtually. Martin Andres Caruso Bloeck and Seng Guan Toh (both EUR), Alexandra Solovyeva (FAD), and Jaunius Kamelavičius and Thomas Piontek (both MCM) contributed to some analyses. Rogelio Celaya (EUR) provided research assistance, and Marizielle Evio and Caitlin Aingé (EUR) provided administrative assistance. Nadav Steinberg (Senior Advisor to Executive Director) participated in the discussions, while Marnix van Rij (Alternate Executive Director) participated in several meetings, including the concluding meeting.

## CONTENTS

CONTEXT—CHALLENGES 5

RECENT ECONOMIC DEVELOPMENTS 5

OUTLOOK AND RISKS 9

POLICY DISCUSSIONS 13

A. Restoring Fiscal Buffers Amid Persistently Higher Defense Spending \_\_\_\_ 13

B. Advancing the Longstanding Structural Reform Agenda \_\_\_\_ 17

C. Ensuring Price Stability 20

D. Safeguarding Financial Stability 21

E. Strengthening Financial Integrity 23

AUTHORITIES' VIEWS 23

STAFF APPRAISAL 25

## BOX

1. Israel: Energy Shocks 12

## FIGURES

1. Recent Macroeconomic Developments 27

2. Labor Market Developments 28

3. Inflation and Monetary Developments 29

4. Selected Financial Indicators 30

5. Performance of the Banking System 31  
6. External Sector Developments 32  
7. Fiscal Developments 33

## TABLES

1. Selected Economic Indicators, 2022–31 \_\_\_\_ 34
2. Summary of Central Government Operations, 2022–31 \_\_\_\_ 35
3. General Government Operations, 2022–31 \_\_\_\_ 36
4. Depository Corporations Survey, 2019–26 \_\_\_\_ 37
5. Financial Soundness Indicators, Banks, 2018–2025Q3 \_\_\_\_ 38
6. Balance of Payments, 2022–31 \_\_\_\_ 39
7. International Investment Position, 2018–25 \_\_\_\_ 40

## ANNEXES

I. Authorities' Responses to Past Article IV Recommendations 41  
II. Macroeconomic Developments From October 2023 to February 2026 42  
III. External Sector Assessment 45  
IV. Risk Assessment Matrix 48  
V. Data Issues 50  
VI. Sovereign Risk and Debt Sustainability Assessment 52  
VII. Macroprudential and Financial Policy Measures 59  
VIII. Risks from Housing Finance in Israel 61  
IX. Authorities' Responses to Past FSAP Recommendations 66

## CONTEXT—CHALLENGES

1. Elevated regional tensions over the past three years have tested the economy's resilience. These reflect a succession of geopolitical shocks, including the 2023-25 Gaza conflict, the June 2025 escalation with Iran, and the war in the Middle East that began on February 28, 2026. Economic activity rebounded after each shock, but repeated disruptions have hindered a durable recovery, leaving output about 9 percent below its pre-October 2023 trend. The latest conflict risks prolonging these losses, amid elevated defense spending, higher

![](images/062d19a0af441ed519676c7eb892eed3ebfe376e72180ffaff793dbbef4b60ae.jpg)  
Sources: Central Bureau of Statistics; and IMF staff calculations.
1/ The pre-conflict trend is constructed by applying the average growth rate over Q2 2019-Q2 2023 to GDP from Q2 2023 onward.

debt and interest costs, and persistent labor supply constraints from military mobilization and reduced availability of Palestinian workers.

2. These pressures compound longstanding structural challenges. Labor force participation and skill levels remain low for some groups, particularly Haredi men and Arab-Israelis, weighing on potential growth. In addition, the dual structure of the economy, with world-class high-tech sectors alongside lower productivity in other industries, exposes Israel to sectoral shocks. As a small, open economy, Israel remains particularly exposed to global trade tensions and growth prospects.

3. General elections are due by late October 2026. The political landscape is fragmented, and early elections are possible if the Knesset (the Israeli parliament) fails to pass key legislations. During recent conflicts, the government has maintained prudent macroeconomic and financial sector policies broadly in line with the past staff recommendations, while progress in structural reform has been mixed (Annex I).

## RECENT ECONOMIC DEVELOPMENTS

## 4. The economy gradually recovered from earlier conflicts through 2024-25.

\- Output fell sharply in late 2023, followed by a recovery in 2023-25. Following the October 2023 Gaza conflict, output contracted sharply (-21 percent, annualized quarter-over-quarter, q/q), driven by a collapse in tourism, a drop in construction due to the loss of Palestinian workers, and weakened private consumption (Annex II). Activity began to recover in early 2024 and

![](images/ba292d1cb0576ab249ad6686cfa612d8f080594f9ca5f75846954c5795e6118a.jpg)

strengthened into 2025 as the conflict ebbed, supported by private demand and easing supply constraints, with a brief interruption from the June 2025 Iran escalation and a strong rebound in H2 2025. GDP growth rose from 1 percent in 2024 to 2.9 percent in 2025 (Figure 1).

Labor markets tightened (Figure 2). Military mobilization, displacement, and the loss of Palestinian workers reduced labor supply significantly in Q4 2023, tightening labor markets. Labor supply subsequently gradually recovered through 2024-25 as reservists returned and foreign workers replaced Palestinians. Nonetheless, employment, unemployment, and vacancy indicators pointed to continued tightness into early 2026. Compensation of non-public sector employees increased by 6.8 percent year on year (y/y) in 2025, up from 2.3 percent in 2024.

![](images/4fa266e7c5a7393cdc53c2a3f89909ed9b2436cbbb6af27dbd082f548ce698d3.jpg)

![](images/74102668f36c606600dc498e6d76109b930bd5d3bb55c9bd4c3520b4e59e45d7.jpg)

\- Inflation rose in 2024 before returning to the target range in 2025 (Figure 3). Inflation accelerated through 2024, reflecting supply constraints, elevated shipping costs, and initial shekel depreciation. Headline and core inflation (CPI excluding energy and food) peaked at 3.8 percent y/y and 3.6 percent y/y, respectively, in January 2025. Subsequently, a stronger shekel, easing supply constraints, and tight monetary policy helped bring inflation back within the 1-3 percent target range by fall 2025. Headline and core inflation were 2 percent y/y and 2.2 percent y/y, respectively, in February 2026.

\- Financial markets were initially volatile but strengthened through 2024-25 (Figure 4). Following the October 7, 2023 shock, t

[中间内容因长度限制已省略]

shekel appreciation, lower risk premia, and somewhat lower energy prices.

We welcome staff's assessment that the monetary policy stance remains appropriate for maintaining price stability. As inflation pressures eased and risk premia declined at the end of 2025, the BOI cut its policy rate by a cumulative 50 basis points. Given heightened uncertainty at the onset of the war in the Middle East, the BOI paused, but, noting the shekel appreciation and the contained inflation level and inflation expectations, it cut the interest rate by 25 basis points on May 25. The BOI shares staff's assessment that the current interest rate level of 3.75 percent reflects a moderately tight stance and supports price stability. Going forward, the interest rate path will be determined in accordance with developments in inflation, economic activity, geopolitical uncertainty, and fiscal developments. A further decline in inflation expectations towards the lower end of the target range may require a more neutral policy stance.

The BOI concurs that market forces should continue to determine the FX rate, barring abrupt market disruptions. They welcome staff's assessment that the external position in 2025 was broadly in line with the level implied by medium-term fundamentals and desirable policies. Israel maintains a positive, though narrowing, current account surplus, driven by strong high-tech services exports. The international investment position and gross reserves are at high levels, providing adequate buffers against global and regional shocks.

## Financial sector

The financial system remains resilient. Banks are well capitalized, liquid, and profitable, with non-performing loans at historical lows. The authorities recognize that banks' sizeable exposure to real estate poses risks. To mitigate these risks, the BOI introduced several macroprudential measures, including limits on mortgage loan-to-value ratios, payment-to-income ratios, and the adjustable-rate share of mortgage composition. In April 2025, the BOI capped contractor-subsidized balloon loans and imposed higher capital requirements on exposure to developers heavily engaged in presales, resulting in reduced subsidized presales. The Tel Aviv Stock Exchange transitioned to a Monday–Friday trading schedule at the beginning of 2026, facilitating foreign-investors' participation and supporting increased trading volumes.

Financial stability has been supported by prudent and proactive supervision and timely policy measures. The establishment of the Financial Stability Committee in 2019 enhanced cooperation between financial regulators. In accordance with staff's advice, the BOI is working to develop a bank liquidity stress testing framework and, together with the Capital Market and Insurance Authority, it is working to regularize joint stress tests for banks and insurance companies. Recently adopted amendments to the Banking Order strengthen bank resolution capacity by enhancing the BOI's powers and flexibility in application of resolution tools. The BOI is working to implement the Basel III capital structure, while maintaining current capital requirements. Finally, the authorities are taking measures to strengthen banking competition while safeguarding financial stability. Two new digital banks have been established in recent years, while new legislation approved by the Knesset in April will facilitate new entry by creating a three-tiered regime based on proportionality without compromising financial stability or supervisory integrity.

## Structural policies

Better integration of all population groups in the labor market and closing of infrastructure gaps are key for sustainable growth. Persistently low participation and limited labor-relevant skills among the fast-growing population of Haredi men, as well as low participation of Arab women, weigh on potential growth. The authorities note the contribution of past initiatives to enhance Arab-Israelis' educational and workforce outcomes and recognize the need to improve incentives for Haredi men to enter the labor force. To enhance broad-based productivity, the government is investing heavily in physical infrastructure as well as AI-related infrastructure. To improve productivity and reduce the high cost of living, the government has pursued product-market reforms to strengthen competition and facilitate trade, including aligning import procedures with EU standards and removing remaining tariffs on U.S. goods.

The Israeli high-tech sector is at the global frontier, and Israel is well-positioned to reap the fruits of the AI revolution. The IMF's AI Preparedness Index ranks Israel $18^{\text{th}}$ globally, while the Stanford AI index places Israel at the top in AI-related private investment and newly funded AI companies. Recent CBS data point to a further increase in AI adoption among Israeli firms, with the share of firms reporting AI use rising to 39 percent in 2026, very high by international standards. Finally, recent survey by the BOI and Israel Democracy Institute shows that the share of employees using AI for work purposes in Israel is higher than in any European country included in the Eurostat survey. Staff's analysis suggests that the Israeli labor force enjoys higher AI complementarity than that of other European countries. At the same time, skill shortages, sectoral disparities, and skill gaps among Arab-Israeli and Haredi populations could constrain economy-wide AI diffusion. The authorities are committed to maintaining Israel's leadership in innovation and advanced technologies, including artificial intelligence, through continued investment in human capital, digital infrastructure, and research and development.
"""
