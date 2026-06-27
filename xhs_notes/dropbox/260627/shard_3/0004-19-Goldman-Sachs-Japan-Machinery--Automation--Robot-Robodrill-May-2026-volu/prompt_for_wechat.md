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
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Japan Machinery: Automation: Robot/Robodrill May 2026 volume trends

The Ministry of Finance announced May 2026 trade data (customs data) during morning trading on June 26. We use this data as an indicator of volume trends for Fanuc's (Sell) robots and Robodrill No. 30 vertical machining centers, and Yaskawa Electric's (Buy, on CL) robots. Japanese companies have a large share of the global robot market and high domestic production ratios. Since Japan accounts for the majority of global robot production, we believe export volume trends from Japan to the rest of the world can be viewed as an indicator of investment in robots and automation, mainly in the auto and electronics industries. In this note, we outline our views on the robot industry and casing demand trends inferred from this month's data.

Yuichiro Isayama  
+81(3)4587-9806 |  
yuichiro.isayama@gs.com  
GS Japan Co., Ltd.

Takeru Adachi  
+81(3)4587-4067 |  
takeru.adachi@gs.com  
GS Japan Co., Ltd.

Takato Enoki  
+81(3)4587-1739 |  
takato.enoki@gs.com  
GS Japan Co., Ltd.

Chie Hu  
+81(3)4587-6330 | chie.hu@gs.com  
GS Japan Co., Ltd.

Exhibit 1: Robots: Trade statistics summary

<table><tr><td colspan="5">Robot: Japan</td></tr><tr><td></td><td>N. America</td><td>Europe</td><td>China</td><td>Global</td></tr><tr><td>Volume</td><td>1,720</td><td>1,497</td><td>5,390</td><td>10,828</td></tr><tr><td>yoy</td><td>3%</td><td>7%</td><td>6%</td><td>9%</td></tr><tr><td>mom</td><td>-17%</td><td>-25%</td><td>-13%</td><td>-24%</td></tr><tr><td>Value (¥mn)</td><td>4,966</td><td>4,334</td><td>8,541</td><td>21,550</td></tr><tr><td>yoy</td><td>-18%</td><td>-34%</td><td>9%</td><td>-8%</td></tr><tr><td>mom</td><td>-11%</td><td>-16%</td><td>-22%</td><td>-22%</td></tr><tr><td>ASP (¥mn)</td><td>2.89</td><td>2.90</td><td>1.58</td><td>1.99</td></tr><tr><td>yoy</td><td>-20%</td><td>-39%</td><td>3%</td><td>-16%</td></tr><tr><td>mom</td><td>7%</td><td>11%</td><td>-10%</td><td>3%</td></tr></table>

Exhibit 2: Robodrills: Trade statistics summary

<table><tr><td colspan="5">Robodrill: Japan</td></tr><tr><td></td><td>Asia</td><td>China</td><td>AeCJ</td><td>Global</td></tr><tr><td>Volume</td><td>1,134</td><td>559</td><td>575</td><td>1,204</td></tr><tr><td>yoy</td><td>-26%</td><td>-4%</td><td>-39%</td><td>-26%</td></tr><tr><td>mom</td><td>-28%</td><td>-33%</td><td>-22%</td><td>-27%</td></tr><tr><td>Value (¥mn)</td><td>8,480</td><td>4,649</td><td>3,832</td><td>9,619</td></tr><tr><td>yoy</td><td>-11%</td><td>16%</td><td>-31%</td><td>-18%</td></tr><tr><td>mom</td><td>-22%</td><td>-22%</td><td>-22%</td><td>-24%</td></tr><tr><td>ASP (¥mn)</td><td>7.48</td><td>8.32</td><td>6.66</td><td>7.99</td></tr><tr><td>yoy</td><td>20%</td><td>21%</td><td>14%</td><td>12%</td></tr><tr><td>mom</td><td>8%</td><td>16%</td><td>-1%</td><td>4%</td></tr></table>

<table><tr><td colspan="5">Robot: Fanuc (GSE)</td></tr><tr><td></td><td>N. America</td><td>Europe</td><td>China</td><td>Global</td></tr><tr><td>Volume</td><td>1,389</td><td>1,150</td><td>3,591</td><td>7,175</td></tr><tr><td>yoy</td><td>13%</td><td>27%</td><td>5%</td><td>18%</td></tr><tr><td>mom</td><td>-15%</td><td>-27%</td><td>-23%</td><td>-24%</td></tr><tr><td>Value (¥mn)</td><td>4,309</td><td>3,717</td><td>7,061</td><td>17,049</td></tr><tr><td>yoy</td><td>12%</td><td>53%</td><td>8%</td><td>22%</td></tr><tr><td>mom</td><td>-11%</td><td>-18%</td><td>-24%</td><td>-17%</td></tr><tr><td>ASP (¥mn)</td><td>3.10</td><td>3.23</td><td>1.97</td><td>2.38</td></tr><tr><td>yoy</td><td>-1%</td><td>21%</td><td>2%</td><td>4%</td></tr><tr><td>mom</td><td>5%</td><td>13%</td><td>-1%</td><td>9%</td></tr></table>

Source: Ministry of Finance, GS Global Investment Research

<table><tr><td colspan="5">Robodrill: Fanuc (GSE)</td></tr><tr><td></td><td>Asia</td><td>China</td><td>AeCJ</td><td>Global</td></tr><tr><td>Volume</td><td>797</td><td>376</td><td>421</td><td>801</td></tr><tr><td>yoy</td><td>-35%</td><td>-27%</td><td>-41%</td><td>-35%</td></tr><tr><td>mom</td><td>-31%</td><td>-39%</td><td>-20%</td><td>-30%</td></tr><tr><td>Value (¥mn)</td><td>5,066</td><td>2,714</td><td>2,352</td><td>5,083</td></tr><tr><td>yoy</td><td>-25%</td><td>-7%</td><td>-38%</td><td>-25%</td></tr><tr><td>mom</td><td>-25%</td><td>-30%</td><td>-19%</td><td>-26%</td></tr><tr><td>ASP (¥mn)</td><td>6.36</td><td>7.22</td><td>5.59</td><td>6.35</td></tr><tr><td>yoy</td><td>16%</td><td>27%</td><td>5%</td><td>15%</td></tr><tr><td>mom</td><td>7%</td><td>16%</td><td>1%</td><td>7%</td></tr></table>

Source: Ministry of Finance, GS Global Investment Research

## Robot export volume (Fanuc, Yaskawa Electric, and Japan total)

Fanuc: We estimate that Fanuc robots made at its Yamanashi main plant and its Tsukuba plant account for the bulk of exports from Tokyo/Yokohama. Mom momentum for export volume to China was -14% in April and -23% in May, suggesting that exports have not seen the strong continued growth observed in machine tools and some other FA equipment. We believe that companies with relative strength in small 6-axis or SCARA robots are benefiting more from AI-related demand in China. Exports to North America, where yoy momentum turned negative in April, saw yoy momentum rebound to +8% in May, but momentum appears to be losing steam, partly due to a high prior-year hurdle.

Yaskawa Electric (global exports from Moji in May: 347 units, -54% yoy/-73% mom): Yaskawa Electric is the only major robot maker with a production base in Kyushu, and we therefore believe its robots account for the majority of export volume from the port of Moji. Exports to South Korea totaled 74 units (-80% mom) and exports to China totaled 60 units (-51% mom), both declining, which we believe is a sign that OEM-related projects are starting to wind down. Exports to India, which saw a sharp increase in April, fell in May (-86% mom).

Exhibit 3: Fanuc: Robot shipment value by destination (GSe)  
![](images/694f4a9c3419fdd8ed1b92e2d296a990e41be822c87ab46247b6482bd78bab49.jpg)  
Source: Ministry of Finance, GS Global Investment Research

Exhibit 4: Japan: Robot shipment value by destination  
![](images/46500ba1986ab5f8b089115a74090ebf93c62c9c505c8f164c1c7f8b029967b8.jpg)  
Source: Ministry of Finance, Data compiled by GS Global Investment Research

Exhibit 5: Fanuc: Robot export volume to China and average export price (GSe)  
![](images/8f6fd630479af680f0970076e69c54584ce3b81528383826cd79780d39aa52fd.jpg)  
Source: Ministry of Finance, GS Global Investment Research

Exhibit 6: Fanuc: Robot export volume to North America and average export price (GSe)  
![](images/43c10d86efe7fbf201a8b84329360571b9fc3c95d0d8947089e2f92c8652db0a.jpg)  
Source: Ministry of Finance, GS Global Investment Research

Vertical machining center export volume from Tokyo/Yokohama (assumes Fanuc accounts for the majority of export volume)

Fanuc: We estimate that Robodrills made at Fanuc's Tsukuba plant account for the bulk of the No. 30 vertical machining centers exported to Asia from Tokyo/Yokohama customs. Of these, 376 units were shipped to mainland China (-27% yoy/-39% mom). Exports to India totaled 173 units (-67% yoy/-30% mom), and exports to Vietnam totaled 26 units (-78% yoy/-30% mom), with the sense of having peaked continuing. While we will need to monitor trends going forward, we believe that smartphone-related demand has remained limited in CY26.

Exhibit 7: Fanuc: Breakdown of Robodrill export volume by region (GSe)  
![](images/4315dc70eb3294c99070e0a9f51e0415a48afdcb0195442e936707cbbed0eb25.jpg)  
Source: Ministry of Finance, GS Global Investment Research

Exhibit 8: Fanuc: Robodrill export volume to China and average export price (GSe)  
![](images/b63b0f4ee823e266a11fe1c532d912bdff1be168122f7b405ca5c2b35a313c26.jpg)  
Source: Ministry of Finance, GS Global Investment Research

## Price Target Risks and Methodology - Fanuc (6954.T)

Our 12-month target price of ¥5,600 is based on FY3/28E EV/EBITDA, applying the sector-average multiple of 10X and a 70% sector-relative premium.

Key upside risks include sales in the FA business recovering to levels above past peaks, greater-than-expected improvement in robot business margins, and share buybacks or other moves to strengthen shareholder returns.

## Price Target Risks and Methodology - Yaskawa Electric (6506.T)

Our 12-month target price of ¥9,200 is based on FY2/28E EV/EBITDA, applying the sector-average multiple of 10X and a 90% sector-relative premium.

Key downside risks include (1) a slowdown in semiconductor and AI Capex related business, (2) slower-than-expected results from cost optimization measures, and (3) disappointment in the capital policy and growth strategy in the next medium-term plan and long-term vision.

## Disclosure Appendix

## Reg AC

We, Yuichiro Isayama, Takeru Adachi, Takato Enoki and Chie Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yuichiro Isayama GS Japan Co., Ltd., Takeru Adachi GS Japan Co., Ltd., Takato Enoki GS Japan Co., Ltd., Chie Hu GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Fanuc and Yaskawa Electric is/are relative to the other companies in its/their coverage universe: AeroEdge, CKD, Daifuku, Daikin Industries, Fanuc, Harmonic Drive Systems, Hoshizaki, IHI, Japan Steel Works, Kawasaki Heavy Industries, Keyence, Makita, Misumi Group, Mitsubishi Heavy Industries, Okuma, Omron, SKY Perfect JSAT Corp, SMC, THK, Yaskawa Electric

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Yaskawa Electric (¥6,824)

GS had a non-securities services client relationship during the past 12 months with: Yaskawa Electric (¥6,824)

There are no company-specific disclosures for: Fanuc (¥7,030)

Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/efb5607b4b7d9cdc494e1a7ac249b767aa0b7b0a7dcece95b58712c03f122724.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/7c00afb937a80de75c12196c6d2986f4898ad97d51ec7b5527d4587f596a736b.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## Fanuc (6954.T)

Yaskawa Electric (6506.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>28-May-26</td><td>5,600</td><td>7,984</td><td>28-May-26</td><td>9,200</td><td>7,136</td></tr><tr><td>26-Apr-26</td><td>5,300</td><td>6,256</td><td>29-Apr-26</td><td>7,300</td><td>5,381</td></tr><tr><td>14-Jan-26</td><td>5,000</td><td>6,935</td><td>10-Apr-26</td><td>6,500</td><td>4,894</td></tr><tr><td>31-Oct-25</td><td>4,300</td><td>4,909</td><td>09-Mar-26</td><td>6,300</td><td>4,325</td></tr><tr><td>13-Oct-25</td><td>4,100</td><td>4,780</td><td>09-Jan-26</td><td>6,000</td><td>5,026</td></tr><tr><td>25-Jul-25</td><td>3,400</td><td>4,220</td><td>13-Oct-25</td><td>5,000</td><td>4,085</td></tr><tr><td>20-Jun-25</td><td>3,300</td><td>3,713</td><td>03-Oct-25</td><td>3,400</td><td>3,178</td></tr><tr><td>11-Apr-25</td><td>3,200</td><td>3,388</td><td>08-Jul-25</td><td>3,000</td><td>2,833</td></tr><tr><td>12-Jan-25</td><td>3,600</td><td>4,116</td><td>20-Jun-25</td><td>3,700</td><td>3,190</td></tr><tr><td>19-Nov-24</td><td>3,400</td><td>4,099</td><td>11-Apr-25</td><td>3,900</td><td>2,881</td></tr><tr><td>31-Oct-23</td><td>3,300</td><td>3,653</td><td>06-Apr-25</td><td>4,600</td><td>3,344</td></tr><tr><td>13-Sep-23</td><td>3,400</td><td>4,081</td><td>10-Jan-25</td><td>5,300</td><td>4,271</td></tr><tr><td>28-Jul-23</td><td>4,500</td><td>4,689</td><td>24-Dec-24</td><td>5,500</td><td>3,950</td></tr><tr><td>13-Jul-23</td><td>5,200</td><td>4,762</td><td>04-Oct-24</td><td>6,400</td><td>5,023</td></tr><tr><td></td><td></td><td></td><td>16-Aug-24</td><td>6,700</td><td>4,796</td></tr><tr><td></td><td></td><td></td><td>05-Jul-24</td><td>7,000</td><td>5,972</td></tr><tr><td></td><td></td><td></td><td>05-Apr-24</td><td>7,500</td><td>6,174</td></tr><tr><td></td><td></td><td></td><td>13-Sep-23</td><td>7,000</td><td>5,725</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are p

[中间内容因长度限制已省略]

term impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
