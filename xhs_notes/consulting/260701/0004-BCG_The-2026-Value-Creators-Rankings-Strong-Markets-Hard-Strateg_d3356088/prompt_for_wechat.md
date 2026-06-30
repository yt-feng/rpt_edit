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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/caa11e7cba0acb73d879751aa376be445ec48141d211bbcb3fb007c817c375f8.jpg)

CORPORATE FINANCE AND STRATEGY

# Strong Markets, Hard Strategic Choices

The 2026 Value Creators Rankings

By Hady Farag, Jody Foldesy, Julien Ghesquieres, Gerry Hansell, Akshay Kohli, Jeff Kotzen, Martin Link, Alexander Roos, Alexis Colombo, and James Tucker

ARTICLE JUNE 30, 2026 8 MIN READ

Global stock markets continue to deliver strong, sustained, and broad-based performance, remaining resilient through inflation, geopolitical disruption, and recurring bouts of volatility. But for the first time in more than a decade, the companies and sectors leading that performance are not the ones investors have come to expect.

BCG's 2026 Value Creators ranking reveals that leadership in value creation has rotated. Asset-heavy industries such as mining, oil and gas, aerospace and defense, construction, and banking now hold top positions that technology-driven sectors occupied for much of the past decade. Within technology itself, hardware and electrical components continue to outperform, while software and IT services have fallen sharply—from fourth place in last year’s rankings to 31st in this year’s.

This rotation is not a market correction or a temporary blip. It reflects longer-term structural shifts, including where AI is disrupting business models, how geopolitical and macroeconomic forces are redirecting capital, and how investors are recalibrating expectations after years of expanding valuation multiples. Understanding what is driving the rotation—and what it demands of leadership teams—is the central challenge highlighted by this year’s rankings.

The 2026 rankings of top value creators are based on average annual total shareholder return (TSR) over the five years from 2021 through 2025. The five-year lens, which BCG has used in its Value Creators rankings since 1999, helps look past short-term market volatility to identify more durable trends in fundamental value creation. The 2026 sample includes 2,368 companies across 35 industries. (Their performance can be explored via this interactive exhibit; for more on our methodology, see “About the Research.”)

## - About the Research

Since 1999, BCG has published annual rankings of top value creators based on total shareholder return over the previous five-year period. The 2026 rankings reflect our analysis of TSR at 2,368 companies worldwide from 2021 through 2025. To arrive at this sample, we began with TSR data provided by S&P Capital IQ—data that covers nearly 70,000 companies.

We eliminated companies that either were not listed on a stock exchange for the full five years of our study or did not currently have at least 20% of their shares traded in public capital markets. We allow exceptions to this rule for companies that are regarded as key industry players and whose stocks have sufficient liquidity. In addition, we eliminated companies for which five-year TSR was distorted by exogenous factors, such as speculative trading not based on fundamentals. We also eliminated companies that are headquartered in Russia or have predominantly Russian operations. Finally, we eliminated Argentinian, Turkish, and Venezuelan companies because these countries’ hyperinflationary environment skews TSR.

We further refined the sample by organizing the remaining companies into 35 industry groups and establishing an appropriate market capitalization hurdle to eliminate the smallest companies in each group. (We identify the size of the hurdle for each industry in the interactive exhibit.)

Our global large-cap ranking focuses on the top 50 of the 200 largest companies by market capitalization. We based the global and industry rankings on five-year average TSR performance for the individual companies from 2021 through 2025. TSRs and the contributing financial metrics are based on a company's reporting currency.

In addition, for all but four of the industry rankings, we divided TSR performance into the six investor-oriented financial metrics that BCG's TSR disaggregation model uses: sales growth, margin change, multiple change (based on EBITDA), dividend yield, change in the number of shares outstanding, and change in net debt plus leverage effect.

For four industries—asset management and brokerage, banking, insurance, and real estate—we used a slightly different approach to TSR disaggregation because of the special analytical challenges involved in measuring value creation in those sectors. For asset management and brokerage and real estate, equity growth replaces sales growth, ROE change replaces margin change, and the price-to-earnings multiple replaces the EBITDA multiple. Change in net debt is not shown. For both banking and insurance, equity growth replaces sales growth and the price-to-book multiple replaces the EBITDA multiple. Margin change and change in net debt are not shown.

The interactive exhibit and this article reflect the rankings of companies in our 2026 database and do not include companies that dropped off the list before 2026 as a result of mergers, bankruptcies, or other events. For that reason, the rankings from previous Value Creators reports may be slightly different.

## Sources: S&P Capital IQ; LSEG Workspace; BCG ValueScience® Center.

Note: Market capitalization of equity is shown as of December 31, 2025. The location shown is of the corporate headquarters. The contribution of each factor in the TSR disaggregation to the five-year average TSR is shown in percentage points. Dividend yield may include cash dividends, special dividends, proceeds from spinoffs, other extraordinary payouts and adjustments for share splits, issuance of bonus shares, or other one-off events. Although disaggregation is multiplicative, it is converted and shown here as additive, with remainders assigned to the margin and multiple change fields. Because of rounding, the numbers may not add up to the TSR figure shown. Share change refers to the change in the number of shares outstanding, not to the change in share price. Net debt change refers to the change in market capitalization relative to the change in enterprise value, and it includes the change in debt and cash.

Disclaimer: The materials contained in the interactive exhibit and article are designed for information purposes only. BCG does not provide fairness opinions or valuations of market transactions, and these materials should not be relied on or construed as such. A company’s inclusion in the ranking does not represent an endorsement by BCG. The interactive and article do not provide investment or financial advice. Users should contact their advisors for such advice.

BCG has used publicly available data and has not independently verified the data and assumptions used in these analyses. BCG has made no undertaking to update these materials after the date they were gathered for publication, after which such information may become outdated or inaccurate. Changes in the underlying data or operating assumptions will have an impact on the analyses and conclusions. The underlying model used for the interactive and article is designed to work across industries and is no replacement for a detailed calculation that accommodates company- or industry-specific adjustments, which may have an impact on the accuracy of the results.

# Markets Are Resilient, But the Landscape Is Changing

Global markets have delivered average returns of approximately 12% annually since 2020. Although this is only modestly above the averages over the past 10 to 15 years, it is notably strong given recent periods of volatility—including stalled market performance post-COVID and the April 2025 correction amid shifting US trade policy. An unprecedented 11 companies exceeded \$1 trillion in market capitalization at the end of 2025.

Beneath this stability, however, the composition of ranking leaders has changed dramatically. (See Exhibit 1.) Asset-heavy sectors have moved into the top ranks, displacing innovation-driven industries. Meanwhile, performance within technology has diverged. Hardware and electrical components have outperformed software and IT services as well as other technology-enabled sectors, such as financial infrastructure providers or medtech. The decline of software and IT

services—a 27-place drop—is particularly striking: the sector was among the top five industries last year but now sits in the bottom five.

EXHIBIT 1 Several Industry Rankings Shifted by Double Digits

<table><tr><td>Rank</td><td>Industry</td><td>Median 5-yr.TSR, 2020–2024 (%)</td></tr><tr><td>1</td><td>Technology Hardware</td><td>20.0</td></tr><tr><td>2</td><td>Construction</td><td>16.0</td></tr><tr><td>3</td><td>Mining</td><td>15.8</td></tr><tr><td>4</td><td>Software and IT Services</td><td>15.7</td></tr><tr><td>5</td><td>Machinery</td><td>15.2</td></tr><tr><td>6</td><td>Metals</td><td>14.2</td></tr><tr><td>7</td><td>Building Materials</td><td>13.8</td></tr><tr><td>8</td><td>Oil and Gas</td><td>12.7</td></tr><tr><td>9</td><td>Multibusiness</td><td>12.6</td></tr><tr><td>10</td><td>Electronic Components</td><td>12.6</td></tr><tr><td>11</td><td>Asset Management and Brokerage</td><td>12.2</td></tr><tr><td>12</td><td>Financial Infrastructure Providers</td><td>12.0</td></tr><tr><td>13</td><td>Insurance</td><td>11.8</td></tr><tr><td>14</td><td>Aerospace and Defense</td><td>11.6</td></tr><tr><td>15</td><td>Services</td><td>11.6</td></tr><tr><td>16</td><td>Automotive OEMs</td><td>11.5</td></tr><tr><td>17</td><td>Retail</td><td>11.4</td></tr><tr><td>18</td><td>Banks</td><td>11.3</td></tr><tr><td>19</td><td>Fashion and Luxury</td><td>10.1</td></tr><tr><td>20</td><td>Media and Publishing</td><td>8.5</td></tr><tr><td>21</td><td>Transportation and Logistics</td><td>8.2</td></tr><tr><td>22</td><td>Health Care Services</td><td>7.5</td></tr><tr><td>23</td><td>Forest Products and Packaging</td><td>7.5</td></tr><tr><td>24</td><td>Power and Utilities</td><td>7.4</td></tr><tr><td>25</td><td>Chemicals</td><td>7.4</td></tr><tr><td>26</td><td>Consumer Durables</td><td>7.2</td></tr><tr><td>27</td><td>Automotive Components</td><td>6.8</td></tr><tr><td>28</td><td>Medical Technology</td><td>6.8</td></tr><tr><td>29</td><td>Large-cap Pharma</td><td>6.5</td></tr><tr><td>30</td><td>Water and Environment</td><td>5.6</td></tr><tr><td>31</td><td>Mid-cap Pharma</td><td>5.3</td></tr><tr><td>32</td><td>Consumer Nondurables</td><td>4.3</td></tr><tr><td>33</td><td>Communication Service Providers</td><td>4.3</td></tr><tr><td>34</td><td>Travel and Tourism</td><td>3.7</td></tr><tr><td>35</td><td>Real Estate</td><td>1.4</td></tr></table>

Sources: S&P Capital IQ; BCG Value Creators database 2026; BCG ValueScience® Center.
Note: The dataset includes more than 2,300 companies per year and applies minimum market capitalization thresholds by industry. Russian companies were omitted. Venezuelan, Argentinian, and Turkish firms were excluded because these countries' hyperinflationary environments skew valuations.

Several forces are driving this rotation:

\- Among public companies, AI value is accruing to the physical infrastructure layer. The current phase of AI deployment is capital-intensive: it requires chips, data centers, power infrastructure, and physical connectivity. Hardware manufacturers, electrical component producers, and energy providers are direct beneficiaries. Software companies, by contrast, face a more uncertain monetization path. The AI-driven revenue uplift many investors expected has yet to materialize at scale, while AI itself is beginning to disrupt parts of the software value chain.

\- Geopolitics and trade policy are redirecting capital toward tangible assets. Defense spending has accelerated across Europe and Asia. Energy security has become a strategic priority. Oil and other raw materials prices have risen sharply. Infrastructure investment has increased in response to supply chain fragmentation. These trends directly favor aerospace and defense, oil and gas, mining, metals, and construction, now five of the top six performing sectors.

\- Banks have benefited from the higher-rate environment. A sustained period of elevated interest rates has improved net interest margins for financial institutions, resulting in rising valuations of bank stocks. With inflation not returning to its low pre-COVID levels, investors appear to expect these tailwinds to outweigh concerns about private credit risks.

Regional patterns reflect these shifts. While the US continues to dominate in scale and mega-cap concentration, Asia remains overrepresented among top-performing companies, and Europe lags despite signs of stabilization.

## Industry Is Not Destiny

While the sector rotation is consequential, BCG's data consistently shows that it does not determine outcomes at the company level. In all but three of the 35 industries studied, top-quartile companies outperformed the $12\%$ market median—including in industries that ranked near the bottom of the overall rankings. (See Exhibit 2.)

Five-year average annual TSR, 2021–2025 (%)

![](images/32cd1e65f8bf24e85fbd17fb07c980ffa88d8e005aad31209cf00f863f2971b4.jpg)  
Sources: S&P Capital IQ; LSEG Workspace; BCG Value Creators database 2026 (n=2368); BCG ValueScience® Center.
Note: Russian companies were omitted. Venezuelan, Argentinian, and Turkish companies were excluded because these countries' hyperinflationary environment skews valuations.

In other words, although the macro environment shapes the terrain, it does not pick the winners. A company in a low-performing sector can still deliver strong shareholder returns, and being in a sector that benefits from TSR tailwinds does not protect against underperformance.

This highlights the important impact of company-level choices: strategy, capital allocation, operational execution, and the ability to adapt as conditions shift.

## The Emerging Challenge

Given record-high stock market levels, a significant consideration is the “expectation premium”—the gap between current market value and underlying fundamental value. For US non-financial companies, this premium has reached its highest level since 1926, exceeding even the peak of the dot-com bubble in 2000.

Companies, therefore, face a critical balancing act. They must meet near-term performance expectations while also investing to capture longer-term opportunities and navigating structural shifts in value creation. In many cases, this requires reshaping business portfolios—reallocating capital toward emerging sources of value—a process that is often complex and difficult to execute.

The required trade-offs are not always obvious. They depend on industry- and company-specific circumstances and on how leaders interpret current conditions—for example, whether they view current headwinds as temporary disruptions or indicators of structural changes.

Compelling strategies strike the right balance, translating into strong value creation across time horizons. Near-term performance can be boosted by an uplift in the valuation multiple or large capital returns (such as share buybacks). However, longer-term outperformance requires combining fundamental drivers (such as profitable revenue growth) with disciplined capital allocation, and valuations that reflect future upside. (See Exhibit 3.)

## EXHIBIT 3

In the Long Run, High-Quality Growth Is Essential for Value Creation

Sources of TSR for top-quartile performers among industrial businesses, 2005–2025 (%)

![](images/7a9b8a5aa067bf21d9143a21ce09b447bb299f23965a1013215a30850b679265.jpg)  
Sources: S&P Capital IQ, BCG ValueScience® Center.
Note: Top quartile of the 2026 BCG Value Creators sample of industrial businesses (n=2056), 2005–2025. $^{1}$ Includes dividend contribution, share count change, and net debt change and leverage effect.

# Control What You Can—and Bring Investors Along

Going forward, companies will need to focus on what they can control near-term, including cost, pricing, and operations—and have a compelling value creation agenda for the long term. Successful leaders will approach these decisions with the urgency of activist investors, leveraging a tool kit that includes significant cost reduction, major changes to capital allocation priorities, and portfolio reshaping (including through divestitures).

For some companies, this will require using the current tailwinds to deliver strong through-cycle performance rather than overspend today in response to their newfound prosperity. For others, the immediate priorities must be securing their financial foundation and freeing up capital for investments. In any case, CEOs and their leadership teams will need to identify the right paths to delivering the growth that is non-negotiable for longer-term value creation, including through AI and analytics and focused, value-accretive M&A.

In a market defined by extremely high expectations, investor support is especially critical for durable value creation. Companies that make the right strategic choices but fail to bring investors along will not see those choices reflected in their valuations and TSR. Companies that manage investor expectations skillfully—while executing with the capabilities of seasoned operators — have a compounding advantage.

Some companies will also need to actively reshape their investor base—attracting long-term investors whose time horizon aligns with the company’s strategy, rather than relying on short-term holders whose investing decisions focus on quarterly performance. In a market this expectation-laden, the quality of a company’s investor base is itself a strategic asset.

BCG's 2026 Value Creators rankings highlight both the strength and complexity of today's market. Sustained returns, historic valuation levels, and rapidly shifting sector performance are not contradictions. They are the defining features of the current environment, and they demand a thoughtful strategic response.

The companies that will lead the next phase of value creation are not simply those in the right sectors today. They are the ones making deliberate choices about near-term performance and long-term positioning—and executing those choices with discipline and strong investor alignment.

## Authors

![](images/bd532354e5b771ad84319223f0bf183e7c8bd841bbd1a721d5ecdc4d8968d1ae.jpg)

![](images/414fdbc0d75aaefbbd69aa5646b22d5b5ce2c917abf98c7aff1833e88a30df50.jpg)

![](images/a23d46bb40f0b4f52e91b98699a69604031823555016e8c3685c32f4cf8afdb4.jpg)

![](images/7ed6b68ec63a6e4c72ace1b80543edaaf84b834cb747eae94328ea5b249fbdc3.jpg)

![](images/aa453a29891a531c1423020bf01d7d07d42f89edfdd31ea02ff39ca03fa61088.jpg)

## Hady Farag

Partner & Director, Shareholder Value Strategy
New York

![](images/90070029bb908e7a8c5049eb7892c7983ae33d1fab14664040b063d5e2a62933.jpg)

## Julien Ghesquieres

Managing Director & Senior Partner/ Global Leader, Corporate Finance
New York

![](images/786ebc5572ec81546c991387dac3b812186750ad83c536e168eb35a3030b8f7d.jpg)

## Akshay Kohli

India Leader, Corporate Finance and Strategy
Mumbai

![](images/9e8dcf6e8868ddaac061b06955f4800673678e61d9abbd898759de60436be104.jpg)

## Martin Link

Knowledge Expert, Team Manager
Munich

![](images/28284abc4e22382932ef537715c1cd18aef235bc95e00edaac132a25a70a976b.jpg)

## Alexis Colombo

Managing Director & Partner
London

![](images/de5b156e99d6b16c305f95640fe632a8c4fdea10949cad213f57f836a287dda5.jpg)

![](images/519696559298302b4686bdcd1c379f76bc891d4405e19ee411ef9b922a0b826e.jpg)

![](images/52280ba42e582ae658c4ea8b2d158330b7473ec9d6b45d033f8295ebc234f932.jpg)

![](images/19b4b2068235196c22ed2b7591784c33bb7bdc08324d4ca2ee368a592fc33066.jpg)

![](images/00145c32d1d69793b0526fb01c55f716eec61ef4c3a2ad25e6ab2c0b809f5938.jpg)

![](images/b305d6671b77a12c5acaead4f9bab961fea97d24a61e7ee32337b3745aafbf83.jpg)

## Jody Foldesy

Managing Director & Senior Partner
Los Angeles

![](images/9980f39016ae56b5ad663fb63a99dfbeb83c876fd3f9f53eed148df3c1037cf0.jpg)

## Gerry Hansell

Managing Director & Senior Partner
Chicago

![](images/04301fd0d585ab81a470f4da32e17c30414795102245a4222541167af0305c05.jpg)

## Jeff Kotzen

Managing Director & Senior Partner
New Jersey

![](images/8d0ae35585ca624e0c440884ad4d1dfdcf87fa4b9dff7171fb3ba60757063a33.jpg)

## Alexander Roos

Managing Director & Senior Partner
Berlin

![](images/e90f537c2155ac9a0d34d7c3d0947032f2f8044c93f52c3d34a0cd689290c394.jpg)

## James Tucker

Managing Director & Senior
Partner; Global Leader,
Corporate Finance and Strategy
Practice
Toronto

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
