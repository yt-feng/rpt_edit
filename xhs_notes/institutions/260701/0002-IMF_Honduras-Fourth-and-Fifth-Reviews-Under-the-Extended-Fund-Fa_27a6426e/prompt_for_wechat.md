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
IMF Country Report No. 26/160

HONDURAS

June 2026

FOURTH AND FIFTH REVIEWS UNDER THE EXTENDED FUND FACILITY AND THE EXTENDED CREDIT FACILITY ARRANGEMENTS, AND REQUESTS FOR A WAIVER OF NONOBSERVANCE OF PERFORMANCE CRITERION AND EXTENSION OF THE ARRANGEMENTS—PRESS RELEASE; STAFF REPORT; AND STATEMENT BY THE EXECUTIVE DIRECTOR FOR HONDURAS

In the context of the Fourth and Fifth Reviews Under the Extended Fund Facility and the Extended Credit Facility Arrangements, and Requests for a Waiver of Nonobservance of Performance Criterion and Extension of the Arrangements, the following documents have been released and are included in this package:

• A Press Release including a statement by the Chair of the Executive Board.

\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on June 29, 2026, following discussions that ended on May 11, 2026, with the officials of Honduras on economic developments and policies underpinning the IMF arrangements under the Extended Fund Facility and the Extended Credit Facility. Based on information available at the time of these discussions, the staff report was completed on June 12, 2026.

\- A Debt Sustainability Analysis prepared by the staffs of the IMF and the International Development Association.

• A Statement by the Executive Director for Honduras.

The IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.

Copies of this report are available to the public from

International Monetary Fund • Publication Services
PO Box 92780 • Washington, D.C. 20090
Telephone: (202) 623-7430 • Fax: (202) 623-7201
E-mail: publications@imf.org Web: http://www.imf.org

International Monetary Fund
Washington, D.C.

# IMF Executive Board Completes Fourth and Fifth Reviews Under the Extended Fund Facility and Extended Credit Facility Arrangements for Honduras

FOR IMMEDIATE RELEASE

\- The Executive Board of the International Monetary Fund (IMF) completed the Fourth and Fifth Reviews under the Extended Fund Facility (EFF) and Extended Credit Facility (ECF) arrangements for Honduras, enabling a disbursement of about US\$242 million (SDR 178.4 million).

\- The Honduran economy has remained resilient, and program performance for the fourth and fifth reviews has been favorable. With a healthy accumulation of international reserves alongside prudent fiscal policies, and an appropriate monetary and exchange rate policy mix, the economy is well placed to navigate the challenging external environment, while progress in structural reforms has strengthened in recent months.

\- The continuation of well-calibrated macroeconomic policies, anchored by a contained fiscal deficit, continued efforts to strengthen the monetary and exchange rate frameworks, and decisive progress on governance and energy sector reform will be essential to preserve macroeconomic stability and support inclusive growth.

Washington, DC – June 29, 2026: The Executive Board of the International Monetary Fund (IMF) today completed the fourth and fifth reviews under the Extended Fund Facility and Extended Credit Facility arrangements for Honduras. The completion of the reviews enables the authorities to draw about US\$242 million (SDR 178.4 million), bringing the total disbursements under the programs so far to about US\$725 million (SDR 535.3 million). $^{1}$ Honduras’ 36-month arrangements totaling about US\$847 million (SDR 624.5 million) were approved on September 21, 2023.

Program performance for the fourth and fifth reviews has been favorable. In completing the reviews, the Executive Board assessed quantitative performance targets for end-June 2025 and end-December 2025. While all quantitative performance targets for end-June 2025 had been met, the end-December 2025 performance criterion on the stock of domestic arrears at the public electricity utility ENEE was not met. The Board approved the authorities' request for a waiver of non-observance of the end-December 2025 performance criterion on the basis of corrective actions. 11 of 17 structural benchmarks due for these reviews were met or implemented with delay, with particularly strong progress made in recent months.

The Honduran economy has remained resilient, growing 3.8 percent in 2025, supported by record-high coffee prices and surging remittances. Economic growth is projected to slow to 3.3 percent in 2026 as higher global oil prices weigh on economic activity. Following a convergence of inflation to the 4 percent objective in 2025, headline inflation is projected to increase to 5.7 percent at end-2026, driven by higher energy prices. Fiscal performance

continues to be strong, with a fiscal deficit of 0.7 percent of GDP in 2025 outperforming the program target of a deficit of 1.5 percent of GDP, with a deficit of 1.0 percent of GDP targeted in 2026. International reserve coverage has strengthened considerably since 2024, and performance of the foreign exchange auction system has improved, supported by favorable foreign exchange inflows in the context of elevated remittance flows and high coffee prices, along with earlier monetary policy tightening and the resumption of exchange rate crawl.

At the conclusion of the Executive Board's discussion, Mr. Kenji Okamura, Deputy Managing Director and Acting Chair, made the following statement:

"The Honduran economy has been resilient, despite elevated external uncertainty. The continued implementation of prudent fiscal policies, an appropriate monetary and exchange policy mix, and the recent acceleration of structural reform implementation demonstrate the authorities' strong commitment to the Fund-supported program. The authorities are focused on strengthening macroeconomic stability and fostering inclusive, sustainable growth. Elevated and evolving external risks related to global energy prices and climate-related events call for continued policy agility, contingency planning and engagement with the Fund and development partners.

"The authorities remain committed to fiscal discipline, including through their efforts to prioritize current expenditures, mobilize revenue, and improve the targeting of energy subsidies. Efforts to reorganize and enhance the execution of social spending remain critical to protect vulnerable households and strengthen the social safety net. Further progress in enhancing fiscal governance and public financial management frameworks, including through the liquidation of existing trust funds, remains essential to underpin sound fiscal policies and maintain debt sustainability.

"In the context of external uncertainty, standing ready to adjust monetary and exchange rate policies as needed to contain broader inflationary pressures and safeguard external stability is important. The authorities' ongoing efforts to improve mechanisms to allocate foreign exchange will be supported by the continued implementation of appropriate and consistent monetary and exchange rate policies, alongside efforts to strengthen the institutional framework of the central bank. Strengthening financial sector supervision is also important.

"Reinvigorating reform momentum in the energy sector is critical to limit fiscal risks and support medium-term economic growth. Renewed efforts are needed to reduce electricity losses and address arrears to strengthen the state-owned electricity company's financial position. Further improvements to governance and operational efficiency are also essential to improve the sector's sustainability and support much-needed investment in the electricity sector.

"A steadfast commitment to strengthen governance and combat corruption will be essential to foster private investment and inclusive growth. The approval and implementation of key reforms to the AML/CFT framework remain vital in this regard. Furthermore, the implementation of the governance and anti-corruption agenda will be critical to improve investor confidence and support a favorable environment for job creation. Measures to enhance climate resilience are also important."

# HONDURAS

June 12, 2026

FOURTH AND FIFTH REVIEWS UNDER THE EXTENDED FUND FACILITY AND THE EXTENDED CREDIT FACILITY ARRANGEMENTS, AND REQUESTS FOR A WAIVER OF NONOBSERVANCE OF PERFORMANCE CRITERION AND EXTENSION OF THE ARRANGEMENTS

## EXECUTIVE SUMMARY

Context. Following elections in late 2025, the new government of President Asfura has affirmed its commitment to the Fund-supported program and decisively resumed reform momentum. Economic developments have remained largely favorable, supported by appropriate fiscal, monetary, and exchange rate policies alongside a supportive external environment in 2025 that fostered a marked improvement in foreign exchange market conditions and the accumulation of international reserves. A changed international environment, however, marked by the oil supply shock, alongside a possible strong El Niño event, poses new risks that require an agile policy response.

Program performance has been favorable for the Fourth and Fifth Reviews, with strong performance against quantitative targets but structural reform delays—partly due to the election and change in government—with stronger performance more recently. Except for the end-December 2025 electricity utility (ENEE) arrears Performance Criterion (PC), all PCs and most Indicative Targets (ITs) have been met. ITs were missed on electricity losses for each test date, along with the end-March 2026 ENEE arrears and social spending. End-December 2025 ITs on tax revenues and current primary spending were also marginally missed. 11 of the 17 Structural Benchmarks (SBs) scheduled through end-April 2026 were met or implemented with delay, seven of which since February 2026. Of the remaining SBs, one is proposed to be dropped, one was partially implemented with delay, and four are proposed to be reset for completion for the sixth and final reviews. A prior action for these reviews—the amendment of regulations to ensure that a new health trust fund to address urgent medical needs is ringfenced, temporary, and subject to rigorous safeguards—has been met.

Policy discussions centered on the importance of maintaining a prudent and agile policy mix in the context of heightened external risks, advancing policies to resume reform progress in the energy sector and to upgrade the AML/CFT framework ahead of

FATF's evaluation starting later this year, placing safeguards on the new health trust fund, and the implementation of delayed SBs. The authorities concurred on the need to reprioritize expenditures to maintain the program's fiscal target while creating space for priority expenditures, including in response to the oil price shock, while improving subsidy targeting. They are prepared to adjust monetary and exchange rate policies as needed to contain possible second-round inflationary pressures and maintain external stability and expressed a commitment to improving access to foreign exchange, including through a transition back to an interbank market, while improving the medium-term frameworks for monetary and exchange rate policies. The authorities also affirmed program commitments to improve the efficiency and financial health of ENEE and concurred on the importance of upgrading the AML/CFT framework.

Staff supports the completion of the Fourth and Fifth Reviews and the authorities' requests for a waiver of non-observance of the end-December 2025 ENEE arrears performance criterion and extension of the arrangements. Favorable program performance, corrective actions taken, and the authorities' demonstrated commitment, including a completed prior action, offer assurances of their ability to achieve program objectives. The authorities request a short extension of the arrangements to complete the sixth and final reviews. A total of SDR 178.42 million would be available upon completion of the combined reviews (SDR 118.94 million under the EFF arrangement and SDR 59.48 million under the ECF arrangement).

Discussions were held in Tegucigalpa on April 27-May 11, 2026. The team comprised Emilio Fernandez-Corugedo (head), Bunyada Laoprapassorn, William Lindquist (all WHD), Pedro Juarros (FAD), Jorge León (SPR), Fabiano Rodrigues Bastos (Resident Representative) and Kevin Gutierrez (Resident Representative Office). Felipe Palmeira (FAD), Joaquin Gadea and Karla Vasquez (both LEG) virtually participated in some discussions. Ms. Mendez Bertolo (Executive Director) and Mr. Monterroso (Senior Advisor to Executive Director, OEDCE) also joined the meetings. The mission met with President Asfura and senior economic officials, including Minister of Finance Emilio Hernández Hércules and Central Bank of Honduras President Roberto Lagos, in addition to representatives of Congress, the private sector, and other stakeholders. Giselle Ballon de Rivero and Millena Machado Damasio (WHD) provided administrative support, and Joe Ue (WHD) analytical support.

## CONTENTS

CONTEXT 5

RECENT ECONOMIC DEVELOPMENTS \_\_\_\_ 5

MACROECONOMIC OUTLOOK AND RISKS 9

PROGRAM PERFORMANCE \_\_\_\_ 12

POLICY DISCUSSIONS 13

A. Fiscal Policies 13

B. Monetary, Exchange Rate, and Financial Sector Policies 17

C. Energy Sector Policies 20

D. Other Structural Policies 22

PROGRAM MODALITIES 22

STAFF APPRAISAL 24

## BOXES

1. Possible Impact of El Niño Events on Honduras \_\_\_\_ 12

2. Supporting the Health Emergency Response While Managing Fiscal Risks \_\_\_\_ 16

## FIGURES

1. Real Sector Developments 27

2. External Sector Developments 28  
3. Fiscal Developments 29  
4. Monetary and Financial Sector Developments 30

## TABLES

1. Selected Economic Indicators, 2023-2031 \_\_\_\_ 31
2. Statement of Operations of the Central Government, 2023-2031 (millions of Lempiras) \_\_\_\_ 32
3. Statement of Operations of the Central Government, 2023-2031 (percent of GDP) \_\_\_\_ 33
4. Statement of Operations of the Nonfinancial Public Sector, 2023-2031 (millions of Lempiras) 34
5. Statement of Operations of the Nonfinancial Public Sector, 2023-2031 (percent of GDP) \_\_\_\_ 35
6. Summary Accounts of the Financial System, 2023-2031 \_\_\_\_ 36
7. Balance of Payments, 2023-2031 (millions of U.S. dollars) \_\_\_\_ 37
8. Balance of Payments, 2023-2031 (percent of GDP) \_\_\_\_ 38
9. External Financing Needs and Sources, 2026-2031 \_\_\_\_ 39
10. External Financing Gap, 2023-2026 \_\_\_\_ 40
11. External Vulnerability Indicators, 2023-2031 \_\_\_\_ 40
12. Decomposition of Public Debt and Debt Service by Creditor, 2025-2027 \_\_\_\_ 41
13. Medium-Term Macroeconomic Framework, 2023-2031 \_\_\_\_ 42
14. Structure and Performance of the Banking Sector, 2018-2026 \_\_\_\_ 43
15. Schedule of Reviews, Disbursements, and Purchases \_\_\_\_ 44
16. Indicators of Fund Credit, 2026-2035 \_\_\_\_ 44

## ANNEXES

I. Risk Assessment Matrix \_\_\_\_ 45
II. External Sector Assessment \_\_\_\_ 49
III. Equilibrium REER and Exchange Rate Policy \_\_\_\_ 53
IV. Recent Developments in the Foreign Exchange Auction \_\_\_\_ 54
V. Summary of Poverty Reduction and Growth Strategy \_\_\_\_ 56
VI. Trust Funds: Recent Developments and Performance \_\_\_\_ 58

## APPENDIX

I. Letter of Intent 61
Attachment I. Memorandum of Economic and Financial Policies 65
Attachment II. Technical Memorandum of Understanding 91

Sources: Central Bank of Honduras; and IMF staff calculations.

## CONTEXT

1. The government of President Nasry Asfura took office in January 2026. Asfura won a narrow plurality in the November 30, 2025 elections, after a protracted vote-counting process decided in late December. While staff-level agreement on policies to complete the Fourth Reviews was reached in September 2025, the extended post-election process and change in government made infeasible the completion of the reviews.

2. The new authorities have strongly affirmed their commitment to continuing the Fund-supported program, which remains a key policy anchor, especially in the context of a changed external environment and heightened external risks. Implementation of the structural agenda slipped during the electoral period and change in government, with stronger performance more recently. At the same time, the supportive external environment of 2025 has changed, marked by the global oil supply shock and the risk of a strong El Niño event. In this context, the new authorities recognize the value of the Fund-support policy framework to anchor their policy response, including their reform agenda.

## RECENT ECONOMIC DEVELOPMENTS

3. Supported by favorable external conditions, the economy remained resilient in 2025. Real GDP grew by 3.8 percent, driven by remittance-supported consumption, a smaller real exports' contraction amid record-high coffee prices, and buildup of inventories, although fixed investment stagnated, given electoral and trade policy-related uncertainties. On the supply side, services remained the main driver of growth in 2025, with some recovery in the agricultural and manufacturing sectors. Monthly economic activity indicators suggest broadly stable growth in early 2026.

4. Inflation had remained within the Central Bank of Honduras (BCH)'s tolerance range (4±1 percent) prior to the conflict in the Middle East. $^{1}$ Headline inflation ended 2025 just under 5.0 percent and had declined to 3.5 percent in February, driven by lower core and food inflation and favorable base

![](images/871ae543b671ab179d01b275b1bd13ebfb770a3d5047987abb66b9adb6f06453.jpg)

![](images/7cf6280ebe7acd3bc22dd768d1e52b5266bba54cbe315bf875808560d2572150.jpg)

...as higher global oil prices passed through quickly to domestic fuels prices.

effects (Text Figure 1). $^{2}$ The passthrough of higher global oil prices has since exerted upward pressure on headline inflation, which increased to 5.6 percent in April, with the contribution of transport fuels increasing by 1.6 percentage points in April.

![](images/f599b67add00affac78b6e7f81ed6280e6a1f15de45e22cb157d4034ad88fb00.jpg)  
Sources: Central Bank of Honduras; and IMF staff calculations.

![](images/94990043891d143d529a9274f79f42627e8120213971690792690c450a0949e0.jpg)

5. The fiscal balance outperformed in 2025 as capital spending slowed. The non-financial public sector (NFPS) deficit declined from 1.0 percent of GDP in 2024 to 0.7 in 2025 (versus 1.5 programmed), meeting the end-December 2025 QPC, driven by a slowdown in capital spending and lower-than-projected interest payments. Fiscal performance in 2026Q1 has remained strong, with an NFPS registering a surplus, meeting the end-March 2026 IT. The IT on priority social spending was met in end-D

[中间内容因长度限制已省略]

ment in EMBI spreads, which have fallen below 200 basis points, and the strengthening of domestic financing conditions. They remain committed to deepening the domestic debt market, diversifying their financing mix toward concessional and semi-concessional sources, and managing rollover risks associated with upcoming Eurobond redemptions, including the 2027 maturity.

## Monetary and Exchange Rate Policy

The authorities remain committed to implementing a consistent monetary and exchange rate policy framework aimed at maintaining low and stable inflation, preserving external stability, safeguarding international reserves, and strengthening the central bank's capital position. BCH

has maintained a data-driven approach under the crawling band regime, holding the monetary policy rate at 5.75 percent since October 2024 while allowing the exchange rate to depreciate cumulatively by about 7 percent since the crawl resumed in 2024 Q3. The new authorities of the Central Bank agree with staff that the current policy rate remains broadly appropriate, while standing ready to act decisively should second-round effects from higher oil prices emerge.

The authorities have continued to strengthen the FX allocation mechanism, progressively easing documentation thresholds for FX purchases to improve market functioning and transparency. Looking ahead, BCH intends to move carefully toward a transition back to an interbank FX market and, over time, toward an inflation-targeting framework supported by greater exchange rate flexibility. The authorities value the continued Fund technical assistance in this transition and the support to strengthen BCH's governance.

## Financial Sector

The National Banking and Insurance Commission (CNBS) continues to closely monitor financial sector conditions, with a view to safeguarding financial stability and ensuring the soundness and resilience of the banking system.

The financial system remains sound, with capital adequacy at 14.2 percent, well above the 10 percent regulatory minimum—and nonperforming loans remain low at 2.6 percent at 2026

Q1. The CNBS is updating its stress testing framework to incorporate the impact of higher oil prices, and continues to strengthen prudential regulation, including finalization of the capital conservation buffer and preparations for the net stable funding ratio and IFRS-9 implementation. The authorities are also preparing new legislation on securities markets and on insurance and reinsurance, reflecting their commitment to a deeper and more resilient financial sector.

## Structural Reforms

The authorities are working to address the energy sector's structural weaknesses and find a durable solution. In this regard, the authorities recognize that addressing ENEE's financial difficulties remains central to the program's success and to broader fiscal sustainability. While the end-December 2025 QPC on ENEE arrears was missed, reflecting election-related execution challenges, the extension of the bill-payment period, and higher oil prices, the authorities have adopted a comprehensive corrective financing plan combining timely subsidy payments from the Ministry of Finance (SEFIN) with calibrated ENEE debt issuance, supporting the request for a waiver of nonobservance on the basis of corrective actions already underway.

On electricity losses, the authorities are implementing the merger of ENEE's distribution-related units, expanding smart metering, and strengthening billing and collection, alongside continued progress toward cost-reflective tariffs, including the 10.49 percent tariff adjustment for 2026Q2 and the phasing out of generalized subsidies. The submission to Congress of the draft decree reforming the Electricity System Law reflects the authorities' broader vision for a more market-oriented energy sector, with a strengthened role for the regulator and improved targeting of subsidies to protect vulnerable households.

On governance, the beneficial ownership law has been approved by the Congress, and AML/CFT legislative amendments have been submitted to Congress to secure timely approval ahead of the upcoming FATF evaluation. Honduras' rejoining of ICSID in March 2026 and efforts to digitalize investment and trade documentation underscore the authorities' commitment to strengthening the investment climate and rule of law.

Statistical capacity is strengthening, with key advances in price indicators, national accounts, and fiscal statistics—supported by recent updates to the CPI, ongoing rebasing efforts, and steady progress toward alignment with international standards (SNA 2025, BPM7, and GFSM 2014), alongside continued improvements in data quality and coverage.

## Conclusion

The Honduran authorities remain firmly committed to the objectives of the EFF/ECF-supported program amid a more challenging external environment. Favorable program performance to date, reflected in strong compliance with quantitative targets and renewed momentum on structural reforms, together with the corrective actions taken on ENEE arrears and the safeguards established for the health trust fund, demonstrate the authorities' resolve and ownership of the program. We thank directors for their continued engagement and support and request the Executive Board's approval of the proposed decisions, including completion of the Fourth and Fifth Reviews, the requested waiver, the extension of the arrangements until December 31, 2026, to allow for the proper completion of the sixth and final reviews, and approval of the exchange restriction. Finally, we thank the Fund for its continued support under the EFF/ECF arrangements, and for the valuable technical assistance and capacity development.
"""
