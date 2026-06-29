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
# IRELAND

June 2026

## 2026 ARTICLE IV CONSULTATION—PRESS RELEASE; AND STAFF REPORT

Under Article IV of the IMF's Articles of Agreement, the IMF holds bilateral discussions with members, usually every year. In the context of the 2026 Article IV consultation with Ireland, the following documents have been released and are included in this package:

## A Press Release.

\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on a lapse-of-time basis, following discussions that ended on May 25, 2026, with the officials of Ireland on economic developments and policies. Based on information available at the time of these discussions, the staff report was completed on June 10, 2026.

• An Informational Annex prepared by the IMF staff.

The documents listed below have been or will be separately released.

## Selected Issues

The IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.

Copies of this report are available to the public from

International Monetary Fund • Publication Services
PO Box 92780 • Washington, D.C. 20090
Telephone: (202) 623-7430 • Fax: (202) 623-7201
E-mail: publications@imf.org Web: http://www.imf.org

International Monetary Fund
Washington, D.C.

# IMF Executive Board Concludes 2026 Article IV Consultation with Ireland

FOR IMMEDIATE RELEASE

\- The Irish economy has remained resilient in the face of consecutive external shocks.

\- Growth is projected to slow but remain healthy amid trade and geopolitical tensions and elevated global uncertainty. Risks to the growth outlook are on the downside and to inflation on the upside.

\- While the war in the Middle East demands near-term policy attention, the current strong economic position provides a window to future-proof the economy.

Washington, DC – June 29, 2026: The Executive Board of the International Monetary Fund (IMF) completed the Article IV Consultation $^{1}$ with Ireland, considered and endorsed the staff appraisal without a meeting on a lapse-of-time basis.

The Irish economy has remained resilient in the face of consecutive external shocks. The domestic economy, as measured by the Modified Gross National Income, is estimated to have grown by about 4 percent in 2025. Robust consumption and investment, together with strong exports dominated by foreign multinational enterprises (MNEs), contributed to solid growth. Headline inflation remained close to 2 percent in 2025 but has accelerated recently due to higher energy prices. The labor market has become less tight as employment growth slowed. The general government balance remained in a sizeable surplus in 2025, supported by continued strong corporate income tax receipts from MNEs.

The economy is projected to grow at a slower but still robust pace. Private consumption is expected to slow down due to weaker employment and real income growth. Modified investment is projected to normalize from the high 2025 level and would be supported by continued construction activity. Export growth is expected to slow significantly in 2026 and the current account surplus to moderate over the medium term.

Risks to the growth outlook are on the downside and to inflation on the upside. Substantial external risks stem from the war in the Middle East, contingent on the war's intensity and duration. Ireland's reliance on MNEs continues to be a key source of vulnerability. Rising geoeconomic fragmentation and elevated policy uncertainty could lead to further reorganization of supply chains and shifts in trade and capital flows that would be detrimental to Ireland's globally integrated economy. The rapidly evolving landscape of AI poses novel

risks, including threat to cyber security. Domestically, persistent supply-side constraints could weigh on productivity.

## Executive Board Assessment $^{2}$

The Irish economy has remained resilient and is projected to grow at a slower but still robust pace amid higher energy prices and global uncertainty. Modified domestic demand growth is projected to moderate from almost 5 percent in 2025 to about 2½ percent in 2026–27, largely reflecting a softening of private consumption due to weaker employment and real income growth, as well as normalization of modified investment. Headline inflation is projected to rise to about 3½ percent in 2026 and return to 2 percent around 2028. The outlook is subject to elevated uncertainty, with downside risks to growth and upside risks to inflation. Ireland's external position is preliminarily assessed to be moderately stronger than the level implied by medium-term fundamentals and desirable policies.

Ireland's current strong economic position provides an opportunity to future-proof its economy. Reliance on MNEs continues to be a source of vulnerability; housing and infrastructure gaps remain to be fully addressed; long-term spending pressures from aging and the green transition are looming; and the rapid development of AI presents both risks and opportunities. Given these vulnerabilities and risks in a more shock-prone and fragmented world, Ireland cannot take its resilience for granted and should use the current window to address vulnerabilities, improve productivity, and secure lasting prosperity.

Fiscal policy should achieve a broadly neutral stance while scaling up public investment efficiently. With the economy operating at full capacity and upside inflation risks, fiscal policy should avoid injecting unnecessary demand stimulus. Furthermore, a broadly neutral stance would help build buffers for future shocks and spending needs stemming from aging and the green transition. In case of downside risks materializing, automatic stabilizers should be allowed to operate fully. Any discretionary fiscal support should be temporary, targeted, and preserve price signals, to be accommodated within a broadly neutral fiscal stance, except in a severe downside scenario. Staff welcomes the authorities' commitment to accelerating public investment and effective implementation will be key. Current expenditure needs to be closely managed, including through stronger controls to minimize overruns.

Broadening the tax base and strengthening the national fiscal framework would reduce vulnerability to the highly concentrated CIT and help prepare Ireland for long-term challenges. Increasing revenues from PIT, VAT, and local property taxes would provide more sustainable revenue sources for permanent spending commitments and allow for channeling more excess CIT revenues into the two savings funds. A stronger national fiscal framework would help Ireland balance competing priorities, enhance budget credibility, and safeguard sustainability. Given the lack of a fiscal anchor at present, the MTFSP should guide annual budgets and act as a binding mechanism on spending ceilings over the medium term.

Systemic risks have risen, warranting ongoing vigilance to safeguard financial stability. The financial system has proven resilient in the face of external shocks. But vulnerabilities in segments of Ireland's large and complex non-bank sector related to leverage and liquidity mismatches could amplify and transmit adverse shocks. Asset quality should remain a key supervisory focus for banks. Macroprudential settings are appropriate, and the CBI should continue to review and adjust them as macro-financial conditions develop. Evolving risks from digitalization and cybersecurity require continued focus on operational resilience.

Strengthening regulation and supervision of non-banks requires continued efforts and cooperation with the international community. The CBI should maintain its leadership role in developing a macroprudential framework for non-banks and continue to monitor the implementation of the macroprudential measures for Irish property funds and GBP-denominated liability-driven investment funds. The CBI's ongoing efforts, in collaboration with ESMA and other regulators, to improve data availability and quality, enhance risk assessment, and develop system-wide stress tests are welcome.

Structural reforms should focus on addressing housing shortages, enhancing energy security, and preparing for the AI transformation. Achieving the new housing targets will require further efforts to streamline the complex planning and judicial review process, increase urban density, boost construction productivity, and crowd in private capital. Upgrading the electricity grid, strengthening integration with the EU energy market, and harnessing Ireland's potential in renewables are key to bolstering energy security and delivering a cost-effective green transition. Realizing AI-related productivity gains while ensuring adjustment does not undermine inclusive growth will require policies to help workers adapt and acquire new skills, enhance labor mobility, and foster innovation to leverage Ireland's abundant talent.

The Irish economy would benefit significantly from deepening the EU Single Market. The SIU can facilitate the redirection of savings into productive investments, and Ireland's financial sector, a global leader in asset management, is uniquely positioned to lead the transition. The proposed 28th corporate regime, if designed and implemented well, would enable Irish firms to operate more efficiently in the Single Market and bring economies of scale. Advancing new EU trade agreements would allow Irish firms to diversify supply chains and capture efficiency gains from trade.

<table><tr><td colspan="11">Ireland: Selected Economic Indicators, 2022-31</td></tr><tr><td rowspan="2"></td><td colspan="10">Projections</td></tr><tr><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td><td>2027</td><td>2028</td><td>2029</td><td>2030</td><td>2031</td></tr><tr><td colspan="11">(Annual percentage change, constant prices, unless otherwise indicated)</td></tr><tr><td colspan="11">Output/Demand</td></tr><tr><td>Real GDP 1/</td><td>7.5</td><td>-2.5</td><td>2.6</td><td>12.3</td><td>-0.8</td><td>3.7</td><td>2.9</td><td>2.4</td><td>2.3</td><td>2.3</td></tr><tr><td>Real GNI* (growth rate) 2/</td><td>3.3</td><td>5.7</td><td>4.8</td><td>4.0</td><td>2.0</td><td>2.7</td><td>2.6</td><td>2.4</td><td>2.3</td><td>2.3</td></tr><tr><td>Domestic demand</td><td>7.7</td><td>8.0</td><td>-9.8</td><td>14.8</td><td>2.3</td><td>2.6</td><td>2.7</td><td>2.7</td><td>2.5</td><td>2.3</td></tr><tr><td>Public consumption</td><td>2.5</td><td>5.0</td><td>5.3</td><td>4.1</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.3</td></tr><tr><td>Private consumption</td><td>10.8</td><td>5.0</td><td>2.9</td><td>2.9</td><td>2.0</td><td>2.3</td><td>2.4</td><td>2.3</td><td>2.2</td><td>2.3</td></tr><tr><td>Gross fixed capital formation</td><td>2.8</td><td>13.4</td><td>-28.5</td><td>42.6</td><td>2.0</td><td>3.5</td><td>3.2</td><td>3.3</td><td>3.0</td><td>2.5</td></tr><tr><td>Exports of goods and services</td><td>12.0</td><td>-3.9</td><td>8.6</td><td>9.7</td><td>0.7</td><td>4.5</td><td>3.0</td><td>2.5</td><td>2.5</td><td>2.5</td></tr><tr><td>Imports of goods and services</td><td>15.0</td><td>2.2</td><td>2.7</td><td>9.5</td><td>3.1</td><td>4.1</td><td>2.9</td><td>2.7</td><td>2.7</td><td>2.6</td></tr><tr><td>Output gap</td><td>2.2</td><td>3.2</td><td>1.2</td><td>1.9</td><td>0.5</td><td>0.3</td><td>0.2</td><td>0.1</td><td>0.0</td><td>0.0</td></tr><tr><td colspan="11">Contribution to Growth</td></tr><tr><td>Domestic demand</td><td>4.5</td><td>4.7</td><td>-6.4</td><td>8.6</td><td>1.3</td><td>1.6</td><td>1.6</td><td>1.6</td><td>1.5</td><td>1.4</td></tr><tr><td>Consumption</td><td>3.0</td><td>1.8</td><td>1.4</td><td>1.3</td><td>0.8</td><td>0.9</td><td>0.9</td><td>0.9</td><td>0.9</td><td>0.9</td></tr><tr><td>Gross fixed capital formation</td><td>0.6</td><td>2.8</td><td>-7.1</td><td>7.4</td><td>0.4</td><td>0.8</td><td>0.7</td><td>0.7</td><td>0.7</td><td>0.6</td></tr><tr><td>Inventories</td><td>0.9</td><td>0.1</td><td>-0.8</td><td>-0.1</td><td>0.1</td><td>-0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net exports</td><td>2.2</td><td>-7.7</td><td>8.9</td><td>3.9</td><td>-1.8</td><td>2.3</td><td>1.3</td><td>0.8</td><td>0.8</td><td>0.9</td></tr><tr><td>Residual</td><td>0.7</td><td>0.5</td><td>0.1</td><td>-0.1</td><td>-0.4</td><td>-0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td colspan="11">Prices</td></tr><tr><td>Inflation (HICP)</td><td>8.1</td><td>5.2</td><td>1.3</td><td>2.1</td><td>3.5</td><td>2.6</td><td>2.0</td><td>2.1</td><td>2.0</td><td>2.0</td></tr><tr><td>Inflation (HICP, core)</td><td>5.0</td><td>5.0</td><td>2.4</td><td>2.2</td><td>2.5</td><td>2.4</td><td>2.2</td><td>2.1</td><td>2.0</td><td>2.0</td></tr><tr><td>GDP deflator</td><td>8.0</td><td>3.4</td><td>4.5</td><td>1.0</td><td>1.9</td><td>2.4</td><td>1.5</td><td>1.7</td><td>1.7</td><td>1.8</td></tr><tr><td colspan="11">Employment</td></tr><tr><td>Employment (% changes of level, ILO definition)</td><td>6.9</td><td>3.4</td><td>2.7</td><td>2.2</td><td>1.2</td><td>1.1</td><td>1.0</td><td>1.0</td><td>0.9</td><td>0.8</td></tr><tr><td>Unemployment rate (percent)</td><td>4.5</td><td>4.3</td><td>4.3</td><td>4.7</td><td>5.0</td><td>5.0</td><td>5.0</td><td>5.1</td><td>5.1</td><td>5.1</td></tr><tr><td colspan="11">(Percent of GDP)</td></tr><tr><td colspan="11">Public Finance, General Government</td></tr><tr><td>Revenue</td><td>22.3</td><td>23.6</td><td>26.5</td><td>22.7</td><td>23.5</td><td>23.4</td><td>23.6</td><td>23.6</td><td>24.0</td><td>24.3</td></tr><tr><td>Expenditure</td><td>20.6</td><td>22.2</td><td>22.3</td><td>21.0</td><td>22.5</td><td>22.5</td><td>23.0</td><td>23.2</td><td>23.4</td><td>23.8</td></tr><tr><td>Overall balance</td><td>1.6</td><td>1.4</td><td>4.1</td><td>1.8</td><td>0.9</td><td>0.9</td><td>0.6</td><td>0.4</td><td>0.6</td><td>0.5</td></tr><tr><td>in percent of GNI*</td><td>3.2</td><td>2.5</td><td>7.3</td><td>3.3</td><td>1.7</td><td>1.6</td><td>1.2</td><td>0.8</td><td>1.1</td><td>0.9</td></tr><tr><td>Primary balance</td><td>2.3</td><td>2.1</td><td>4.7</td><td>2.2</td><td>1.5</td><td>1.4</td><td>1.3</td><td>1.1</td><td>1.4</td><td>1.3</td></tr><tr><td>Cyclically adjusted primary balance</td><td>1.6</td><td>1.1</td><td>4.2</td><td>1.7</td><td>1.3</td><td>1.3</td><td>1.2</td><td>1.1</td><td>1.4</td><td>1.3</td></tr><tr><td>Structural primary balance 3/</td><td>-0.4</td><td>-1.1</td><td>-0.7</td><td>-1.2</td><td>-1.8</td><td>-1.9</td><td>-2.0</td><td>-2.0</td><td>-1.8</td><td>-1.9</td></tr><tr><td>General government gross debt</td><td>43.0</td><td>41.8</td><td>38.3</td><td>32.9</td><td>32.2</td><td>30.0</td><td>28.6</td><td>27.6</td><td>26.6</td><td>25.9</td></tr><tr><td>General government gross debt (percent of GNI*)</td><td>83.9</td><td>75.2</td><td>67.1</td><td>62.2</td><td>59.2</td><td>55.8</td><td>53.4</td><td>51.5</td><td>49.6</td><td>48.4</td></tr><tr><td colspan="11">Balance of Payments</td></tr><tr><td>Trade balance (goods)</td><td>39.4</td><td>29.9</td><td>31.2</td><td>36.1</td><td>31.2</td><td>30.6</td><td>30.0</td><td>29.4</td><td>28.9</td><td>28.5</td></tr><tr><td>Current account balance</td><td>8.8</td><td>7.0</td><td>16.2</td><td>8.2</td><td>7.8</td><td>8.0</td><td>8.0</td><td>7.6</td><td>7.2</td><td>7.1</td></tr><tr><td>Gross external debt (excl. IFSC) 4/</td><td>187.7</td><td>175.7</td><td>154.2</td><td>130.8</td><td>125.5</td><td>114.2</td><td>105.6</td><td>98.3</td><td>91.8</td><td>85.9</td></tr><tr><td colspan="11">Saving and Investment Balance</td></tr><tr><td>Gross national savings</td><td>31.6</td><td>33.7</td><td>34.4</td><td>31.1</td><td>31.4</td><td>31.1</td><td>31.1</td><td>30.9</td><td>30.8</td><td>30.7</td></tr><tr><td>Private sector</td><td>29.0</td><td>31.3</td><td>29.3</td><td>28.5</td><td>29.6</td><td>29.4</td><td>29.7</td><td>29.8</td><td>29.5</td><td>29.6</td></tr><tr><td>Public sector</td><td>2.7</td><td>2.4</td><td>5.1</td><td>2.6</td><td>1.8</td><td>1.6</td><td>1.4</td><td>1.1</td><td>1.3</td><td>1.1</td></tr><tr><td>Gross capital formation</td><td>22.9</td><td>26.7</td><td>18.2</td><td>22.9</td><td>23.6</td><td>23.1</td><td>23.1</td><td>23.4</td><td>23.6</td><td>23.6</td></tr><tr><td colspan="11">Memorandum Items:</td></tr><tr><td>Nominal GDP (€ billions)</td><td>520.7</td><td>524.7</td><td>562.8</td><td>638.7</td><td>645.2</td><td>685.1</td><td>715.6</td><td>745.1</td><td>775.4</td><td>807.6</td></tr><tr><td>Nominal GNI* (€ billions)</td><td>266.7</td><td>291.4</td><td>321.1</td><td>337.3</td><td>350.5</td><td>368.3</td><td>383.4</td><td>399.2</td><td>415.5</td><td>432.9</td></tr><tr><td>Modified domestic demand (percentage change) 5/</td><td>8.4</td><td>6.2</td><td>1.8</td><td>4.9</td><td>2.5</td><td>2.6</td><td>2.6</td><td>2.5</td><td>2.4</td><td>2.3</td></tr></table>

# IRELAND

## STAFF REPORT FOR THE 2026 ARTICLE IV CONSULTATION

June 10, 2026

## KEY ISSUES

Context and outlook. The Irish economy has remained resilient amid trade and geopolitical tensions, but its favorable outlook faces challenges and uncertainties. Ireland's reliance on investment and tax revenues from multinational enterprises makes it vulnerable in an increasingly shock-prone and fragmented world, while aging, energy security, and technological transformations present additional challenges. While the war in the Middle East demands near-term policy attention, the current strong economic position provides a window to future-proof the economy.

Fiscal. Staff supports the authorities' plan to scale up and accelerate public investment; effective implementation will be key. Current expenditure needs to be managed closely, including through stronger controls to minimize spending overruns, to achieve a broadly neutral fiscal stance appropriate for the near and medium term. Support should prioritize temporary, targeted transfers over tax cuts, subsidies, or price controls. Broadening the tax base would reduce risks from tax revenue uncertainty and build buffers for future shocks and spending needs. Staff reiterates the importance of strengthening the national fiscal framework and budget credibility.

Financial. Systemic risks, including cyber and operational risks, have risen, underscoring the importance of continued vigilance and close monitoring to bolster resilience and safeguard financial stability. The banking sector remains sound, but asset quality should remain a key supervisory focus. Macroprudential settings are appropriate; the CBI should continue reviewing and adjusting them as macro-financial conditions evolve. In collaboration with other jurisdictions, work should continue to strengthen regulation and supervision of the growing NBFI sector (including o

[中间内容因长度限制已省略]

le 3. Ireland: Table of Common Indicators for Surveillance (concluded) As of June 4, 2026

Any reserve assets that are pledged or otherwise encumbered should be specified separately. Also, data should comprise short-term liabilities linked to a foreign currency but settled by other means as well as the notional values of financial derivatives to pay and to receive foreign currency, including those linked to a foreign currency but settled by other means.

$^{2}$ Other depository corporations include all deposit-taking corporations (except for the central bank) and money market funds.

$^{3}$ Both market-based and officially determined, including discount rates, money market rates, rates on treasury bills, notes and bonds. $^{4}$ Foreign, domestic bank, and domestic non-bank financing.

$^{5}$ The general government consists of the central government (budgetary funds, extra-budgetary funds, and social security funds) and state and local governments. The total stock of general government debt is required for SDDS Plus countries and encouraged for SDDS and e-GDDS countries. $^{6}$ Including currency and maturity composition.

$^{7}$ Frequency and timeliness: (“D”) daily; (“W”) weekly or with a lag of no more than one week after the reference date; (“M”) monthly or with lag of no more than one month after the reference date; (“Q”) quarterly or with lag of no more than one quarter after the reference date; (“A”) annual; (“SA”) semi-annual; (“I”) irregular; (“NA”) not available or not applicable; and (“NLT”) not later than.

$^{8}$ Encouraged frequency of data and timeliness of reporting under the e-GDDS and required frequency of data and timeliness of reporting under the SDDS and SDDS Plus. Any flexibility options or transition plans used under the SDDS or SDDS Plus are not reflected. For those countries that do not participate in the IMF Data Standards Initiatives, the required frequency and timeliness under the SDDS are shown for New Zealand, and the encouraged frequency and timeliness under the e-GDDS are shown for Eritrea, Nauru, South Sudan, and Turkmenistan. Indicators that are not in the IMF Data Standards Initiatives are shown as “...”.

$^{a}$ Based on the information from the Summary of Observance for SDDS and SDDS Plus participants, and the Summary of Dissemination Practices for e-GDDS participants, available from the IMF Dissemination Standards Bulletin Board (https://dsbb.imf.org/). For those countries that do not participate in the Data Standards Initiatives, as well as those that do have a National Data Summary Page, the entries are shown as “...”.

## IRELAND

June 10, 2026

## STAFF REPORT FOR THE 2026 ARTICLE IV CONSULTATION—INFORMATIONAL ANNEX

Prepared By

European Department

## CONTENTS

FUND RELATIONS 2

## FUND RELATIONS

(As of May 31, 2026)

## Membership Status: Joined August 8, 1957; Article VIII

<table><tr><td>General Resources Account:</td><td>SDR Million</td><td>Percent of Quota</td></tr><tr><td>Quota</td><td>3,449.90</td><td>100.00</td></tr><tr><td>Fund holdings of currency</td><td>2,555.11</td><td>74.06</td></tr><tr><td>Reserve position in Fund</td><td>894.82</td><td>25.94</td></tr></table>

<table><tr><td>SDR Department:</td><td>SDR Million</td><td>Percent of Allocation</td></tr><tr><td>Net cumulative allocation</td><td>4,082.00</td><td>100.00</td></tr><tr><td>Holdings</td><td>4,331.07</td><td>106.10</td></tr></table>

Outstanding Purchases and Loans: None

Financial Arrangements:

<table><tr><td>Type</td><td>Approval Date</td><td>Expiration Date</td><td>Amount Approved (SDR million)</td><td>Amount Drawn (SDR million)</td></tr><tr><td>EFF</td><td>12/16/10</td><td>12/15/13</td><td>19,465.80</td><td>19,465.80</td></tr></table>

## Overdue Obligations and Projected Payments to Fund

(SDR million; based on existing use of resources and present holdings of SDRs):

<table><tr><td></td><td>2026</td><td>2027</td><td>2028</td><td>2029</td><td>2030</td></tr><tr><td colspan="6">Principal</td></tr><tr><td>Charges/Interest</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td></tr><tr><td>Total</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td></tr></table>

## Exchange Rate Arrangements and Exchange Restrictions:

Ireland's currency is the euro, which floats freely and independently against other currencies. Ireland has accepted the obligations under Article VIII, Sections 2, 3, and 4 of the IMF's Articles of Agreement, and maintains an exchange system free of multiple currency practices and restrictions on payments and transfers for current international transactions, other than restrictions maintained solely for security reasons, which have been notified to the Fund pursuant to Decision No. 144 (52/51).

## Article IV Consultation:

The last Article IV consultation was concluded on June 6, 2025. The associated Executive Board assessment is available at https://www.imf.org/en/news/articles/2025/06/10/pr25189-ireland-imf-executive-board-concludes-2025-article-iv-consultation-with-ireland and the staff report (Country Report No. 25/128) at https://www.imf.org/en/publications/cr/issues/2025/06/10/ireland-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-567588. Ireland is on the standard 12-month consultation cycle.

## Financial Sector Assessment Program (FSAP) Participation and ROSC:

The Financial System Stability Assessment (FSSA) for the last mandatory financial stability assessment was discussed by the Board on July 1, 2022. The FSSA and accompanying Reports on the Observation of Standards and Codes (ROSCs) are available at https://www.imf.org/en/Publications/CR/Issues/2022/07/07/Ireland-Financial-System-Stability-Assessment-520469.
"""
