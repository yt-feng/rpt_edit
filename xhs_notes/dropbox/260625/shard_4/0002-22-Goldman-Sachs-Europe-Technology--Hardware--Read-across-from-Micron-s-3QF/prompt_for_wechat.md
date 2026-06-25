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
# Europe Technology: Hardware: Read-across from Micron's 3QFY26 results for European semicap and AI Infrastructure players

EUROPE TECHNOLOGY: HARDWARE
Analysing the role of European AI enablers and updating our view on long-term upside potential

Explore >

![](images/406b35d0c95ec59c591623c7ee41cc8e85bab52280ef60179adf0bc9a85a7788.jpg)

Alexander Duval  
+44(20)7552-2995 | alexander.duval@gs.com GS International

Anant Jakhar +1(332)245-7829 | anant.x.jakhar@gs.com GS India SPL

Micron (covered by our US team) reported 3QFY26 revenues of c.\$41.5bn (up +346% yoy and +74% qoq), materially above the Visible Alpha Consensus Data estimate of \$36.3bn. Further, the company guided for 4QFY26 revenues of \$50bn at the mid-point (up +21% qoq), which is c.15% above the Visible Alpha Consensus Data estimate of \$43.3bn going into the print. The company highlighted that its data center revenue in 3QFY26 came in above \$25bn (implying an ARR of around \$100bn). Additionally, Micron stated that AI is driving robust growth in DCs, with Memory demand significantly above supply. We note that MU expects this supply-demand imbalance to persist beyond CY27, with supply expected to improve gradually in 2028. In this vein, the company has now signed 16 take-or-pay strategic customer agreements (SCAs) across DC, consumer and automotive end markets. Importantly, our US semis team highlighted that many of these agreements contain both floor and ceiling prices, and the cumulative amount of committed revenue from these agreements represents c.\$100bn over five years at floor prices. Further, these contracts account for c.20% of MU's expected DRAM volume and a third of its NAND volume over the period. Separately, we note that Micron expects capex investment of c.\$10bn in 4QFY26 (implying FY26 capex of around \$27bn). Additionally, the company expects capex in FY27 to increase significantly yoy (GS currently models FY27 capex of \$50bn), with around 50% of the increase due to construction capex. Finally, we highlight that Micron recently agreed a multi-year EUV supply agreement with ASML (per Micron) supporting increased EUV adoption at its 1-delta node and future generations, which is a positive development for ASML and congruent with our view on increasing EUV layers in the coming years (more details in our note here). Below, we contextualise the implications of Micron's earnings and outlook for the European semicap and AI Infra players: ASML (Buy), ASMI (Buy), BESI (Buy), and NBIS (Buy).

## Readacross for European semicap and AI Infrastructure players:

We note that supply-demand tightness in Memory (both DRAM and NAND) due to continued AI demand suggests a positive near- to medium-term dynamic for the European semicap stocks ASML, ASMI and BESI given supply side tightness

Ayo Odunaiya  
+44(20)7051-5995 |  
ayo.x.odunaiya@gs.com  
GS International

results in better visibility for these players as customers are willing to share incremental details around technological and product ramp cadences.

Further, we believe ASML is best positioned on in our semicap coverage to benefit from this positive demand backdrop given its relatively higher exposure to Memory chips (around $40\%$ ) and longer lead times ( $>12$ months for its EUV tools). We note that ASM International is more skewed towards Logic demand, although it also has some memory exposure.

Furthermore, we see the continued strength of HBM demand as a positive for all three European semicap names but especially BESI given the company at its CMD reiterated that all three major Memory players are actively testing its Hybrid Bonding solutions for future adoption (see more details in our CMD note here). We believe that Memory adoption is a key component of HB demand in the coming years, and we see continued strong demand as encouraging for the adoption of this technology.

Finally, commentary around strong demand from AI bodes well for AI Infrastructure provider NBIS given the company's broad product portfolio of both bare metal and software offerings in tandem with its encouraging progress in expanding its contracted power capacity to serve this demand.

## Valuation and Key risks

ASML: We are Buy rated on ASML with a 12-month price target of €1,770 based on a 40x CY27 P/E multiple. Key risks to our view and price target include EUV delays, capex cyclicality and unfavourable market share shifts.

ASMI: We are Buy rated on ASMI with a 12-month price target of €955 based on a 25x CY27E EV/EBITDA multiple. Key risks to our view and price target include a worsening of the semi cycle, stronger-than-expected competition and high customer concentration.

BESI: We are Buy rated on BESI with a 12-month price target of €315 based on a 33x CY27 EV/EBITDA multiple. Key risks to our view and price target include customer spend cyclicality, hybrid bonding adoption delays and increasing competition.

Nebius: We are Buy rated on Nebius with a 12-month price target of \$267 based on a 9x CY27E EV/Sales multiple. Key risks to our view and price target include competitive pressure from Hyperscalers, slower-than-expected adoption of AI and reduced visibility from shorter-term contracts.

## Disclosure Appendix

## Reg AC

We, Alexander Duval, Anant Jakhar and Ayo Odunaiya, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Alexander Duval GS International, Anant Jakhar GS India SPL, Ayo Odunaiya GS International.

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

The rating(s) for ASM International, ASML Holding, BE Semiconductor Industries and Nebius Group is/are relative to the other companies in its/their coverage universe: ASM International, ASML Holding, BE Semiconductor Industries, CD Projekt, Ericsson, Infineon, Logitech, Nebius Group, Nokia, STMicroelectronics, Stillfront

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS is acting as a manager or co-manager of a pending underwriting: Nebius Group (\$259.66)

GS beneficially owned 5% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Nebius Group (\$259.66)

GS has received compensation for investment banking services in the past 12 months: ASM International (€969.20), ASM International NV (ADR) (\$1,099.17), ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77) and Nebius Group (\$259.66)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: ASM International (€969.20), ASM International NV (ADR) (\$1,099.17), ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77), BE Semiconductor Industries (€292.90) and Nebius Group (\$259.66)

GS has received compensation for non-investment banking services during the past 12 months: Nebius Group (\$259.66)

GS had an investment banking services client relationship during the past 12 months with: ASM International (€969.20), ASM International NV (ADR) (\$1,099.17), ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77), BE Semiconductor Industries (€292.90) and Nebius Group (\$259.66)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: ASM International (€969.20), ASM International NV (ADR) (\$1,099.17), ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77) and Nebius Group (\$259.66)

GS had a non-securities services client relationship during the past 12 months with: ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77) and Nebius Group (\$259.66)

GS has managed or co-managed a public or Rule 144A offering in the past 12 months: ASM International (€969.20), ASM International NV

<table><tr><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>10-Jun-26</td><td>1,770.00</td><td>1,507.20</td><td>10-Jun-26</td><td>267.00</td><td>211.69</td></tr><tr><td>13-May-26</td><td>1,600.00</td><td>1,327.00</td><td>15-May-26</td><td>234.00</td><td>219.94</td></tr><tr><td>16-Apr-26</td><td>1,570.00</td><td>1,222.60</td><td>13-Apr-26</td><td>205.00</td><td>154.56</td></tr><tr><td>29-Jan-26</td><td>1,450.00</td><td>1,192.00</td><td>15-Feb-26</td><td>160.00</td><td>98.01</td></tr><tr><td>12-Jan-26</td><td>1,270.00</td><td>1,086.40</td><td>14-Nov-25</td><td>155.00</td><td>83.54</td></tr><tr><td>08-Dec-25</td><td>1,200.00</td><td>963.20</td><td>08-Oct-25</td><td>137.00</td><td>122.00</td></tr><tr><td>16-Oct-25</td><td>1,050.00</td><td>877.40</td><td>17-Sep-25</td><td>120.00</td><td>94.08</td></tr><tr><td>17-Jul-25</td><td>935.00</td><td>650.20</td><td>08-Aug-25</td><td>77.00</td><td>68.78</td></tr></table>

## (ADR) (\$1,099.17) and Nebius Group (\$259.66)

GS makes a market in the securities or derivatives thereof: ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77) and Nebius Group (\$259.66)

## Distribution of ratings/investment banking relationships

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/97677c2f5b978a8b19f330703786ad11d738c48d58ce6380bcb8074087bfa99d.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/5bf8124e64d95b76b33052f2bde1ba8aa47c52519e23563b494d364cffbfb99a.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/3930ec31c1800d8a702c5468d01ebea958241b3aff75f5a487ae2ab2086ed04b.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/0aac64543d554b3b4340186e9d48e35fb67947389b80aac306e6c25dbd1b5263.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## ASML Holding (ASML.AS)

## Nebius Group (NBIS)

<table><tr><td colspan="3">ASML Holding (ASML.AS)</td></tr><tr><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td></tr><tr><td>16-Apr-25</td><td>910.00</td><td>574.00</td></tr><tr><td>16-Oct-24</td><td>1,010.00</td><td>633.90</td></tr><tr><td>14-Jun-24</td><td>1,185.00</td><td>953.00</td></tr><tr><td>17-Apr-24</td><td>1,075.00</td><td>852.40</td></tr><tr><td>18-Mar-24</td><td>1,070.00</td><td>870.80</td></tr><tr><td>12-Feb-24</td><td>980.00</td><td>877.60</td></tr><tr><td>24-Jan-24</td><td>885.00</td><td>775.80</td></tr><tr><td>15-Jan-24</td><td>820.00</td><td>648.20</td></tr><tr><td>18-Oct-23</td><td>785.00</td><td>553.20</td></tr><tr><td>20-Sep-23</td><td>850.00</td><td>556.60</td></tr><tr><td>19-Jul-23</td><td>860.00</td><td>651.90</td></tr><tr><td>05-Jul-23</td><td>825.00</td><td>659.30</td></tr></table>

BE Semiconductor Industries (BESI.AS)  
ASM International (ASMI.AS)

<table><tr><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td></tr><tr><td>10-Jun-26</td><td>315.00</td><td>288.80</td><td>10-Jun-26</td><td>955.00</td><td>906.60</td></tr><tr><td>27-Apr-26</td><td>286.00</td><td>248.00</td><td>23-Apr-26</td><td>895.00</td><td>851.60</td></tr><tr><td>20-Feb-26</td><td>205.00</td><td>184.50</td><td>05-Mar-26</td><td>835.00</td><td>716.40</td></tr><tr><td>22-Jan-26</td><td>200.00</td><td>175.00</td><td>22-Jan-26</td><td>795.00</td><td>713.20</td></tr><tr><td>12-Jan-26</td><td>184.00</td><td>162.15</td><td>12-Jan-26</td><td>705.00</td><td>626.40</td></tr><tr><td>24-Oct-25</td><td>172.00</td><td>147.05</td><td>30-Oct-25</td><td>645.00</td><td>566.40</td></tr><tr><td>25-Jul-25</td><td>161.00</td><td>117.10</td><td>24-Jul-25</td><td>615.00</td><td>440.80</td></tr><tr><td>24-Apr-25</td><td>146.00</td><td>95.74</td><td>01-May-25</td><td>700.00</td><td>425.30</td></tr><tr><td>16-Jan-25</td><td>170.00</td><td>147.80</td><td>27-Feb-25</td><td>805.00</td><td>524.00</td></tr><tr><td>25-Oct-24</td><td>151.00</td><td>105.65</td><td>25-Jul-24</td><td>800.00</td><td>601.00</td></tr><tr><td>26-Jul-24</td><td>177.00</td><td>122.90</td><td>14-Jun-24</td><td>815.00</td><td>675.80</td></tr><tr><td>14-Jun-24</td><td>183.00</td><td>153.60</td><td>31-May-24</td><td>740.00</td><td>640.20</td></tr><tr><td>25-Apr-24</td><td>160.00</td><td>136.00</td><td>24-Apr-24</td><td>680.00</td><td>590.00</td></tr><tr><td>12-Mar-24</td><td>170.00</td><td>142.85</td><td>18-Mar-24</td><td>665.00</td><td>551.20</td></tr><tr><td>22-Feb-24</td><td>189.00</td><td>163.30</td><td>12-Feb-24</td><td>630.00</td><td>568.30</td></tr><tr><td>17-Jan-24</td><td>165.00</td><td>133.10</td><td>15-Jan-24</td><td>550.00</td><td>450.00</td></tr><tr><td></td><td></td><td></td><td>27-Nov-23</td><td>500.00</td><td>461.90</td></tr><tr><td></td><td></td><td></td><td>25-Oct-23</td><td>460.00</td><td>383.60</td></tr><tr><td></td><td></td><td></td><td>26-Jul-23</td><td>475.00</td><td>392.80</td></tr><tr><td></td><td></td><td></td><td>18-Jul-23</td><td>435.00</td><td>408.95</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regula

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS.

This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
