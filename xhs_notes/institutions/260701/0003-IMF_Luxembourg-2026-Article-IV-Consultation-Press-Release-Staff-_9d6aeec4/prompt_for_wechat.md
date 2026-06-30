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
IMF Country Report No. 26/159

## LUXEMBOURG

June 2026

2026 ARTICLE IV CONSULTATION—PRESS RELEASE; STAFF REPORT; STAFF STATEMENT; AND STATEMENT BY THE EXECUTIVE DIRECTOR FOR LUXEMBOURG

Under Article IV of the IMF's Articles of Agreement, the IMF holds bilateral discussions with members, usually every year. In the context of the 2026 Article IV consultation with Luxembourg, the following documents have been released and are included in this package:

\- A Press Release, summarizing the views of the Executive Board as expressed during its June 22, 2026 consideration of the staff report that concluded the Article IV consultation with Luxembourg.

\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on June 22, 2026, following discussions that ended on May 6, 2026, with the officials of Luxembourg on economic developments and policies. Based on information available at the time of these discussions, the staff report was completed on June 3, 2026.

• An Informational Annex prepared by the IMF staff.

\- Staff Statement.

• A Statement by the Executive Director for Luxembourg.

The IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.

Copies of this report are available to the public from

International Monetary Fund • Publication Services
PO Box 92780 • Washington, D.C. 20090
Telephone: (202) 623-7430 • Fax: (202) 623-7201
E-mail: publications@imf.org Web: http://www.imf.org

International Monetary Fund
Washington, D.C.

# IMF Executive Board Concludes 2026 Article IV Consultation with Luxembourg

FOR IMMEDIATE RELEASE

\- While strong fundamentals, such as low public debt, will continue to cushion the economy against shocks, economic growth has been tepid and uneven with a softening labor market, amid a worsening fiscal balance, rising inflationary pressures, and heightened uncertainty from the war in the Middle East.

\- The fiscal deficit is expected to widen further under current policies amid structural increases in spending and a softening revenue growth. A moderate fiscal adjustment focusing on containing current expenditure is needed to preserve buffers, stabilize public debt and create room for growth-enhancing investment over the medium term.

\- The financial system has continued to demonstrate resilience to elevated market stress episodes. Rising uncertainty and geopolitical risk require continued close monitoring of liquidity, leverage and funding in the multifaceted financial system.

Washington, DC – June 30, 2026: The Executive Board of the International Monetary Fund (IMF) completed the Article IV Consultation for Luxembourg. $^{1}$ The authorities have consented to the publication of the Staff Report prepared for this consultation.

Luxembourg's economy has yet to regain its past dynamism with growth lagging peers and the public sector playing a dominant role. Growth edged up to 0.6 percent in 2025, supported by expansionary fiscal policy and real income gains, while weak external demand continued to be a drag. The labor market has softened, with unemployment rising above 6 percent. Headline inflation rose above 2.5 percent in early 2026 due to higher energy prices, despite new electricity subsidies. The fiscal balance deteriorated sharply in 2025 as spending significantly outpaced revenue. The financial system has remained resilient, and banks and non-banks maintain high capital and liquidity buffers. Asset quality in the corporate sector is gradually improving, with remaining pockets of vulnerability from the real estate sector.

Growth is projected to remain moderate amid uncertainty from the war in the Middle East and domestic constraints. The growth momentum would be dampened by the expected slowdown in European trading partners, headwinds from weaker confidence and higher inflation, while strong public spending and solid private consumption would provide support. Against this backdrop, GDP growth is projected at 1.2 percent in 2026 and to pick up to 1.7 percent in 2027 as the impact of the conflict wanes. Growth is expected to gradually

converge toward potential (around 2 percent) over the medium term as external demand recovers and private investment strengthens. Inflation is forecast to rise to 2.6 percent in 2026, driven by higher energy prices, automatic wage indexation, and second-round effects, before easing toward 2 percent in the medium-term. The outlook faces significant downside risks, including from a prolonged conflict, persistently high energy prices, weaker EU growth, financial market stress, and domestic challenges in the construction sector and the labor market. On the upside, faster progress on EU single market reform could strengthen growth prospects.

## Executive Board Assessment $^{2}$

Executive Directors noted that strong fundamentals, including low public debt and a resilient financial sector, provide buffers against downside risks, including from heightened global uncertainty. At the same time, they emphasized the need for careful policy recalibration to unlock private-sector led growth and help Luxembourg's economy regain its past dynamism.

Directors considered the broadly neutral fiscal stance in 2026 appropriate but emphasized that the composition of spending should become more growth-friendly and the energy support measures more targeted to vulnerable groups. They generally stressed that the projected medium-term weakening in fiscal balances amid rising spending pressures calls for a moderate fiscal adjustment to preserve buffers, stabilize public debt, and create room for priority investment.

Directors highlighted the need to contain current expenditure, improve spending efficiency, and broaden the tax base. They welcomed the recent pension reform and noted that the planned income tax reform could support labor supply, while underscoring the importance of offsetting measures to contain its fiscal cost. Directors also encouraged strengthening the fiscal framework, including through an enhanced national fiscal rule and stronger fiscal risk analysis.

Directors agreed that Luxembourg's financial system has remained resilient and commended the authorities for close oversight and strong fundamentals in the bank and non-bank sectors. At the same time, pockets of vulnerability remain, and elevated uncertainty, including due to geopolitical risks, require continued vigilance given Luxembourg's large, outward-oriented, and highly interconnected financial sector. Directors called for continued close monitoring and proactive management of liquidity, leverage, funding, and concentration risks across banks, investment funds, and insurers, and welcomed good progress in implementing the 2024 FSAP recommendations. As the financial cycle enters an early expansion phase, Directors supported further recalibration of the macroprudential

## framework.

Directors underscored that structural reforms are critical to revive productivity and competitiveness, and rebalance growth toward the private sector. They encouraged the authorities to accelerate digital and AI adoption, strengthen support for innovation, and address skill mismatches through education, reskilling, and upskilling policies. Directors also stressed the importance of increasing labor market flexibility, easing housing pressures through supply-side reforms and land mobilization, and reducing administrative and regulatory burden on firms. They noted that energy diversification and deeper EU single market integration, including progress on the Savings and Investment Union, would further strengthen Luxembourg's medium-term growth prospects.

Table 1. Luxembourg: Selected Economic Indicators, 2024–28

<table><tr><td rowspan="2"></td><td rowspan="2">2024</td><td rowspan="2">Est. 2025</td><td colspan="3">Proj.</td></tr><tr><td>2026</td><td>2027</td><td>2028</td></tr><tr><td colspan="6">Real Economy (percent change)</td></tr><tr><td>Gross domestic product</td><td>0.4</td><td>0.6</td><td>1.2</td><td>1.7</td><td>2.1</td></tr><tr><td>Total domestic demand</td><td>2.5</td><td>2.0</td><td>1.5</td><td>2.5</td><td>2.2</td></tr><tr><td>Private consumption</td><td>3.2</td><td>2.2</td><td>2.0</td><td>2.1</td><td>2.1</td></tr><tr><td>Public consumption</td><td>4.9</td><td>3.7</td><td>2.6</td><td>2.5</td><td>2.2</td></tr><tr><td>Gross investment</td><td>-2.0</td><td>-1.2</td><td>-0.8</td><td>3.7</td><td>2.2</td></tr><tr><td>Foreign balance 1/</td><td>-1.1</td><td>-0.7</td><td>-0.5</td><td>-0.1</td><td>0.6</td></tr><tr><td>Exports of goods and nonfactor services</td><td>-12.2</td><td>1.2</td><td>-1.4</td><td>2.2</td><td>2.0</td></tr><tr><td>Imports of goods and nonfactor services</td><td>-13.6</td><td>1.8</td><td>-1.4</td><td>2.6</td><td>2.0</td></tr><tr><td colspan="6">Labor Market (thousands, unless indicated)</td></tr><tr><td>Unemployed (average)</td><td>18.0</td><td>19.0</td><td>20.0</td><td>21.0</td><td>21.2</td></tr><tr><td>(Percent of total labor force)</td><td>5.7</td><td>6.0</td><td>6.2</td><td>6.4</td><td>6.4</td></tr><tr><td>Resident employment</td><td>295.6</td><td>299.2</td><td>304.0</td><td>307.8</td><td>312.8</td></tr><tr><td>(Percent change)</td><td>0.9</td><td>1.2</td><td>1.6</td><td>1.3</td><td>1.6</td></tr><tr><td>Total employment</td><td>516.0</td><td>522.2</td><td>528.4</td><td>535.4</td><td>544.5</td></tr><tr><td>(Percent change)</td><td>1.0</td><td>1.2</td><td>1.2</td><td>1.3</td><td>1.7</td></tr><tr><td colspan="6">Prices and Costs (percent change)</td></tr><tr><td>GDP deflator</td><td>4.6</td><td>3.2</td><td>3.3</td><td>2.3</td><td>2.1</td></tr><tr><td>CPI (harmonized), p.a.</td><td>2.3</td><td>2.5</td><td>4.3</td><td>2.0</td><td>2.1</td></tr><tr><td>CPI core (harmonized), p.a.</td><td>2.5</td><td>1.8</td><td>1.8</td><td>2.1</td><td>1.9</td></tr><tr><td>CPI (national definition), p.a.</td><td>2.1</td><td>2.3</td><td>2.6</td><td>2.3</td><td>2.1</td></tr><tr><td colspan="6">Public Finances (percent of GDP)</td></tr><tr><td>General government revenues</td><td>47.7</td><td>47.1</td><td>46.9</td><td>47.2</td><td>46.4</td></tr><tr><td>General government expenditures</td><td>46.8</td><td>49.1</td><td>48.8</td><td>49.2</td><td>49.3</td></tr><tr><td>General government balance</td><td>0.9</td><td>-2.0</td><td>-1.9</td><td>-2.0</td><td>-3.0</td></tr><tr><td>General government structural balance</td><td>0.0</td><td>-2.5</td><td>-2.3</td><td>-2.5</td><td>-3.4</td></tr><tr><td>General government gross debt</td><td>26.3</td><td>26.5</td><td>28.2</td><td>29.8</td><td>32.0</td></tr><tr><td colspan="6">Balance of Payments (percent of GDP)</td></tr><tr><td>Current account</td><td>7.1</td><td>5.3</td><td>4.7</td><td>4.4</td><td>4.3</td></tr><tr><td>Balance on goods</td><td>2.0</td><td>2.1</td><td>2.1</td><td>2.1</td><td>2.1</td></tr><tr><td>Balance on services</td><td>36.3</td><td>33.8</td><td>35.1</td><td>35.4</td><td>35.3</td></tr><tr><td>Net factor income</td><td>-30.6</td><td>-29.9</td><td>-31.8</td><td>-32.3</td><td>-32.4</td></tr><tr><td>Balance on current transfers</td><td>-0.6</td><td>-0.7</td><td>-0.7</td><td>-0.7</td><td>-0.7</td></tr><tr><td colspan="6">Exchange Rates, Period Averages</td></tr><tr><td>U.S. dollar per euro</td><td>1.08</td><td>1.13</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Nominal effective rate (2010=100)</td><td>106.3</td><td>107.8</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Real effective rate (CPI based; 2010=100)</td><td>98.6</td><td>99.5</td><td>...</td><td>...</td><td>...</td></tr><tr><td colspan="6">Credit Growth and Interest Rates</td></tr><tr><td>Nonfinancial private sector credit (eop, percent change) 2/</td><td>-5.3</td><td>0.8</td><td>5.0</td><td>4.5</td><td>4.7</td></tr><tr><td>Government bond yield, annual average (percent)</td><td>2.7</td><td>2.9</td><td>...</td><td>...</td><td>...</td></tr><tr><td colspan="6">Potential Output and Output Gap</td></tr><tr><td>Output gap (percent deviation from potential)</td><td>-0.5</td><td>-0.7</td><td>-0.5</td><td>-0.2</td><td>0.0</td></tr><tr><td>Potential output growth</td><td>0.7</td><td>0.8</td><td>1.0</td><td>1.4</td><td>1.9</td></tr><tr><td colspan="6">Sources: Luxembourg authorities; IMF staff estimates and projections.1/ Contribution to GDP growth.2/ Including a reclassification of investment companies from financial to non-financial institutions in 2015.</td></tr></table>

## LUXEMBOURG

## STAFF REPORT FOR THE 2026 ARTICLE IV CONSULTATION

June 3, 2026

## KEY ISSUES

Context. Luxembourg's economy has yet to regain its past dynamism, with growth lagging peers and the public sector playing a dominant role. Strong fundamentals, including low public debt and a resilient financial sector, provide buffers against shocks, but reigniting growth will require policy recalibration to unlock private-sector-led growth anchored in innovation and productivity.

Outlook and risks. Growth is projected to remain moderate though gaining pace. Elevated global uncertainties, alongside persistent competitive pressures, would constrain growth and employment, increase financial sector risks, and add to revenue uncertainties. Faster-than-expected progress on EU-wide reforms could boost growth.

Fiscal policy. Following a deterioration in 2025, the deficit is expected to widen further over the medium term amid revenue slowdown and rising current expenditure. A moderate fiscal tightening is needed to preserve buffers given fiscal risks and stabilize public debt. This requires containing current expenditure, improving efficiency, and broadening the tax base. If risks materialize, automatic stabilizers should be allowed to work. The decision to use fiscal space should reflect a cost-benefit analysis weighing gains from productivity-enhancing investment against reduced buffers and a higher interest bill. Pension and income tax reforms are welcome, while strengthening the fiscal framework would mitigate risks and support long-term sustainability.

Financial sector. The financial system shows resilience to elevated uncertainty and market stress, with high capital and liquidity buffers for banks and non-banks. Asset quality in corporate sector is gradually improving, and real estate market risks have eased with a recovery in residential and commercial segments. But rising uncertainty and geopolitical risk require monitoring of liquidity, leverage, and funding in the multifaceted financial system. As the financial cycle enters an early expansion phase, a gradual tightening of macroprudential policy is recommended, focusing on enhancing releasable capital buffers and implementing income-based measures.

Structural policy. To rebalance the economy towards private sector-led growth centering on reviving productivity, policies should focus on increasing labor market flexibility, raising labor supply, addressing skill mismatch, strengthening support for innovation and accelerating AI technology adoption. Addressing housing affordability and regulatory bottlenecks would ease cost-of-living pressures. Advancing single market reform at EU level would strengthen growth prospects.

Discussions took place during April 23–May 6, 2026. The team comprised A. Shabunina (Head), S. Armendariz, X. Fang, M. Jarmuzek (all EUR), and was assisted by C. Li and V. Timonova. Messrs. Clicq and Englaro (both OED) joined some meetings. The mission met with Minister of Finance Roth, Governor Reinesch, Minister of Interior Affairs Gloden, other officials, and representatives from the private sector and civil society.

## CONTENTS

CONTEXT 4
RECENT DEVELOPMENTS AND OUTLOOK 5
A. Recent Developments: Sluggish Growth Led by Public Sector 5
B. Outlook and Risks 9
POLICY DISCUSSIONS 11
A. Fiscal Policy: Safeguarding Fiscal Space and Improving Efficiency 11
B. Financial Sector: Preserving Resilience Amidst Heightened Uncertainty 15
C. Structural Policy: Promoting Productivity-Led and AI-Enabled Growth 24
STAFF APPRAISAL 28
BOX
1. Impact of External Headwinds 10

## FIGURES

1. Real Sector 30  
2. Labor Market 31  
3. Inflation 31  
4. Fiscal Sector 32  
5. Banking Sector 33  
6. External Sector 34  
7. Structural Sector 34

## TABLES

1. Selected Economic Indicators, 2020–31 \_\_\_\_ 35
2. Balance of Payments, 2020–31 \_\_\_\_ 36
3. General Government Operations, 2020–31 \_\_\_\_ 37
4. Financial Soundness Indicators, 2018–25 \_\_\_\_ 38

## ANNEXES

I. Implementation of Past IMF Advice 39  
II. External Sector Assessment 41  
III. Risk Assessment Matrix 44  
IV. Sovereign Risk and Debt Sustainability Analysis 46  
V. Individual Taxation Reform 52  
VI. AI and Labor Market 54  
VII. Data Issues 58  
VIII. Implementation of FSAP Recommendations 61  
IX. Transnational Aspects of Corruption 68

## CONTEXT

1. The Luxembourg economy is yet to regain its past dynamism. Following a strong post-pandemic recovery in 2021, economic growth has been stagnating and lagging euro area peers since 2022, with the output level below its long-term trend. Growth has increasingly been driven by the public sector, masking underlying weakness in private activity, reflecting a combination of cyclical headwinds—including the construction sector downturn, post-pandemic adjustments in ICT, and subdued external demand—and structural constraints, notably subdued productivity and weak investment by nonfinancial corporates. While the real estate sector shows tentative signs of recovery, supported by easing financial conditions and policy measures, persisting vulnerabilities impede a stronger rebound.

2. Government support has cushioned the economy against successive shocks, but a larger role for the private sector would be essential going forward. Multiple fiscal measures played an important role in smoothing income and employment during the pandemic, energy crisis, and sharp downturn in housing sector. However, as many temporary measures turned permanent, the expanding role of the public sector could risk crowding out private investment and employment, while weakening incentives for resource reallocation toward more productive sectors. Continued reliance on public spending as a growth engine is not sustainable, particularly given rising structural spending needs, including from demographic pressures.

![](images/6af28b38cc04a8f06c69653304853928e4a28b2c3f71bf717a5c371f3beaf81d.jpg)

![](images/82f75996bb8fa46cee9af7da57776af5fd836aeac6f5f4078500a592f46d79d6.jpg)

3. Strong fundamentals will help weather adverse shocks, but reigniting private-sector-led growth will require a recalibration of policies. Low public debt and a resilient financial sector provide sound buffers against new shocks.

[中间内容因长度限制已省略]

ate, the reform includes incentives to extend working lives, alongside stricter early retirement conditions through a gradual eight-month extension of the required contribution period over five years. The authorities concur with staff that further action may be needed over time but consider that this reform constitutes a solid basis for said adjustments on a highly sensitive topic.

## Financial Sector

The financial sector remains resilient and continues to perform strongly, underpinned by sound risk management practices. The banking sector is well capitalized and highly liquid, with solid capital ratios (25.2 percent) and robust asset quality as reflected in the low level of non-performing loans, currently at 1.4 percent. The investment fund sector also continues to perform strongly, supported by sustained growth in assets under management. Risks remain contained, with moderate leverage and limited liquidity vulnerabilities across the sector. The availability of liquidity management tools, further reinforced by recent regulatory developments, also play an important role in supporting the sector's resilience and mitigating liquidity risks going forward. Stress tests reveal that both the number of banks facing capital shortfalls as well as the number of funds with severe liquidity shortages under an adverse scenario are very limited. While both sectors managed recent geo-economic shock episodes well, the authorities reinforced their tight supervisory framework notably through the development of advanced stress-testing tools. This includes a system-wide stress test aimed at capturing risks related to the interconnectedness between banks and investment funds. They also followed up on a recent FSAP recommendation with the launch of an innovative new stress test that incorporates liquidity-solvency interactions. In line with staff advice, a stress test for the insurance sector is being developed as well. These enhancements will solidify the authorities' oversight of the financial sector, including the liquidity and funding risks.

The set of macroprudential measures currently in place is fit for purpose. The authorities acknowledge the specific features of the Luxembourg housing market. However, they consider that staff's characterization of the Luxembourg housing market as featuring a “sizable and persistent share of vulnerable mortgages” relies on criteria that are not suited to the Luxembourg context and therefore does not provide a sufficiently robust assessment of underlying risks. Moreover, the analysis would gain from clearer identification and segmentation of vulnerable borrowers, particularly as to whether vulnerabilities are concentrated among lower or higher-income households. The fact that previous slumps in the real estate market did not affect the banking sector in a significant manner provides comfort in that regard. Moreover, the authorities’ existing stress-testing framework, especially the interest rate stress test on residual income, already captures borrower risk in a more tailored way than BBMs.

## Structural policies

Artificial intelligence is a centerpiece of the government's plans to boost productivity. The authorities thank staff for the annex on artificial intelligence (AI) and the labor market. Recognizing AI's significant upside potential for Luxembourg's economy, the government developed an AI strategy aimed at positioning the country as a leading digital innovation hub. Multiple actions are foreseen to upskill the workforce, such as tailored training programs for professionals, specialized academic offerings for experts, and initiatives like AI4All to foster a broad AI literacy for citizens. Complementary initiatives are intended to foster firm-level adoption of AI to support a broader diffusion across the economy. A notable example is Luxembourg AI Factory, designed to serve as a one-stop shop for companies' AI adoption by providing support from concept to final deployment. The government supports these efforts by providing financial aid through the Fit4AI initiative (EUR 10,000 - 200,000) and SME packages – AI (up to EUR 25,000) to cover the cost of external experts helping companies, in particular SMEs, harness the potential of AI.

Tackling bottlenecks in the housing market remains a key priority. The 2024 policy package to support construction firms during the downturn and facilitate access to housing, combining direct financial assistance with targeted fiscal incentives, successfully halted the rise in bankruptcies and reinvigorated activity. The EUR 480 million envelope set aside for the public acquisition of housing units and off-plan purchases (VEFA) has been fully committed and will result in more social and affordable housing. At the same time, the authorities are advancing structural reforms to increase effective supply, including a land mobilization tax to discourage land hoarding and efforts to ease regulatory bottlenecks and accelerate building processes.

The ongoing energy crisis due to the war in the Middle East underscores the importance of the energy transition to enhance the economy's ability to withstand future energy shocks. The expansion of renewable energy sources continues steadfastly in Luxembourg while public support for energy-friendly renovation and sustainable construction is set to reach close to EUR 500 million from 2026 to 2029, with an additional EUR 450 million set aside for solar panels. The recently agreed “resilience package” foresees further temporary financial aid for households envisaging the installation of non-fossil fuel boilers or an energy retrofit in their homes. This is a good example of how a temporary measure can have a lasting impact.
"""
