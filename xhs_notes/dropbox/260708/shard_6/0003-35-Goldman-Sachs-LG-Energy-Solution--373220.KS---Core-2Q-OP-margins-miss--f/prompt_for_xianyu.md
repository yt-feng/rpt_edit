你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# LG Energy Solution (373220.KS): Core 2Q OP margins miss; focus likely on ESS margins outlook on the analyst call; Buy

LG Energy Solution (LGES) released 2Q26 preliminary earnings on Jul 7th. Ex-AMPC revenue of W7.3tn (+15% QoQ, +32% YoY) was largely in-line with GSe/Bloomberg consensus of W7.0tn/W7.4tn. AMPC of W241bn, implies a sequential recovery in US battery shipment to c.5 GWh (vs. c.4 GWh in 1Q26 and c.10 GWh in 2Q25). We believe the sequential topline recovery was led by the ESS ramp and continued small-cylindrical strength (resilient Tesla demand), while US EV pouch volumes likely stayed constrained by the well-flagged GM JV downtime.

Nikhil Bhandari  
+65-6889-2867 |  
nikhil.bhandari@gs.com  
GS (Singapore) Pte

John Tsang  
+65-6654-5454 | john.tsang@gs.com  
GS (Singapore) Pte

LGES returned to operating profit in 2Q at W113bn (1Q26: -W208bn, 2Q25: W492bn) but was behind GSe/Bloomberg consensus of W224bn/W204bn. Excluding AMPC, the OP margin improved sequentially to $-1.7\%$ (vs. $-6.2\%$ in 1Q26 and $0\%$ in 2Q25). With revenue broadly in-line, we see the softer core margin as driven by potential two factors: (1) OEM take-or-pay compensation timing; and (2) ESS conversion costs from simultaneous line conversions.

## What to expect on the 2Q26 earnings call (on 30 Jul)

We expect the following key debates and questions to be discussed during the 2Q26 earnings call:

■ Path to core profitability. Timing of the OP-accretive compensation tranche and the shape of the 2H26 recovery.

■ ESS ramp and fixed-cost absorption. How much converted-line start-up cost is already in the run-rate versus a 3Q headwind.

■ ESS margins into potential overcapacity. Whether double-digit ESS margins hold as Ford and other entrants add capacity.

■ GM JV restart. The shape of the 3Q restart and its pull-through to 4Q US EV utilization.

\- Europe strategy. How fast European plants utilization rate can improve and turn profitable as BEV registrations recover.

■ Next-gen chemistries and technologies. Commercialization timelines for dry electrode and ASSB versus incumbent LFP and high-nickel.

## Earnings, Valuations and Key Risks:

We maintain our Buy rating and TP of W520,000. Key downside risks: (1)

Lower-than-expected market share; (2) Slower-than-expected ramp-up of new EV/ESS battery plant lines; (3) Lower global EV penetration rate

Thesis in Key Charts  
Exhibit 1: LGES quarterly revenue and OP trend

<table><tr><td>(Wbn)</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26P</td></tr><tr><td>Revenue (ex-IRA)*</td><td>8,001</td><td>6,129</td><td>6,162</td><td>6,878</td><td>6,451</td><td>6,265</td><td>5,565</td><td>5,700</td><td>6,142</td><td>6,365</td><td>7,319</td></tr><tr><td>OP</td><td>338</td><td>157</td><td>195</td><td>448</td><td>(226)</td><td>375</td><td>492</td><td>601</td><td>(122)</td><td>(208)</td><td>113</td></tr><tr><td>OP (ex-IRA)</td><td>88</td><td>(32)</td><td>(252)</td><td>(18)</td><td>(603)</td><td>(83)</td><td>1</td><td>236</td><td>(455)</td><td>(398)</td><td>(128)</td></tr><tr><td>OPM</td><td>4.2%</td><td>2.6%</td><td>3.2%</td><td>6.5%</td><td>-3.5%</td><td>6.0%</td><td>8.8%</td><td>10.5%</td><td>-2.0%</td><td>-3.3%</td><td>1.5%</td></tr><tr><td>OPM (ex-IRA)</td><td>1.1%</td><td>-0.5%</td><td>-4.1%</td><td>-0.3%</td><td>-9.3%</td><td>-1.3%</td><td>0.0%</td><td>4.1%</td><td>-7.4%</td><td>-6.2%</td><td>-1.7%</td></tr></table>

\*Company includes the IRA AMPC in reported revenue from 1Q26. We have excluded AMPC in our illustration for trend comparison with historical quarters.  
Source: Company data, GS Global Investment Research  
US battery surplus bridge (2025E—2027E), GWh

Exhibit 2: US Battery Surplus Bridge

Exhibit 3: Current LGES price sits below our base case, with upside across all three scenarios

![](images/d8ed8e31f6723441e64706d4c7268e9879d75c7c843ef70c4731062c385e1a5b.jpg)  
\*Excluding VW supply and assuming 100% ESS TAM goes to ex-China cell makers.  
Source: GS Global Investment Research  
Base/Bull(ESS)/Bull(EV+SS) valuation scenarios relative to the last closing price

![](images/3b183e9976d18c2a137a83bb09a10f0a43644406e5df9299bc6bd811657ea1ba.jpg)  
Priced as of 7th Jul 2026 close. Bull (ESS) assumes higher long term ESS shipments/market share/margins, Bull (EV + ESS) assumes Bull (ESS) along with higher long term EV shipments/market share/margins.

Exhibit 4: LGES share price implied exit EBITDA multiple is now closer to the lower end of the stock's 12m forward historical range.

![](images/356ac95482d7aa67cf6a5f09051e528b95f7ec249c7fd760620662c736ca5943.jpg)  
Priced as of 7th Jul 2026 close.  
Source: GS Global Investment Research

## Investment Thesis - LG Energy Solution

LGES is the largest battery manufacturer outside China, with leadership in high nickel battery chemistries. We remain positive on LGES' fundamentals given its widening global technology leadership in batteries with upcoming commercial production of new technology battery products such as large size cylindrical 4680 batteries, cell-to-pack LFP batteries (from 2025) and dry electrode process (from 2028). Meanwhile, we see market share growth in the US, driven by rapidly expanding capacities where we expect the company's US market share growth to be margins and returns accretive (GSe 2026E-28E EBITDA CAGR of $51\%$ and $6.5\%$ CROCI expansion during this period).

While the market is anchored on near-term EV battery weakness, we believe it is underestimating the emerging clearer path to utilization rate recovery which we estimate to rise from \~42% in FY26E to \~67% in 2028E. We also see improving visibility in medium-term earnings (doubling of EBITDA between FY26E-28E), supported by ESS demand and strong order momentum for new products. We are Buy rated on LGES.

## Price Target Risks and Methodology - LG Energy Solution

We are Buy rated on LGES with a 12m TP of W520,000 derived using a 50%/50% blend of DCF (WACC: 8.4%, TGR: 3.3%) and 2027E/28E EV/EBITDA. We apply a mid-cycle 20x multiple to adjusted (ex-JV share) 2027E/28E EBITDA.

Key downside risks: (1) Lower-than-expected market share; (2) Slower-than-expected ramp-up of new EV/ESS battery plant lines; (3) Lower global EV penetration rate

<table><tr><td>373220.KS</td><td>12m Price Target: W520,000</td><td colspan="2">Price: W332,000</td><td colspan="2">Upside: 56.6%</td></tr><tr><td>Buy</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9">Market cap: W77.7tr / $50.7bn Enterprise value: W106.3tr / $69.4bn 3m ADTV: W219.6bn / $146.2mn South Korea Korea EV Battery M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: Yes</td><td>Revenue (W bn)</td><td>23,671.8</td><td>28,297.7</td><td>39,259.1</td><td>50,283.8</td></tr><tr><td>EBITDA (W bn)</td><td>5,037.4</td><td>5,418.3</td><td>8,522.5</td><td>12,415.1</td></tr><tr><td>EPS (W)</td><td>(4,585)</td><td>(1,014)</td><td>8,438</td><td>19,333</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>39.3</td><td>17.2</td></tr><tr><td>P/B (X)</td><td>4.2</td><td>3.9</td><td>3.5</td><td>2.9</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>3.7</td><td>3.1</td><td>1.8</td><td>0.8</td></tr><tr><td>CROCI (%)</td><td>6.6</td><td>9.4</td><td>12.5</td><td>15.9</td></tr><tr><td>FCF yield (%)</td><td>(6.5)</td><td>0.4</td><td>2.2</td><td>5.5</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (W)</td><td>(4,763,191)</td><td>1,428</td><td>1,500,493</td><td>2,247,338</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 7 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Nikhil Bhandari and John Tsang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Nikhil Bhandari GS (Singapore) Pte, John Tsang GS (Singapore) Pte.

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

The rating(s) for LG Energy Solution is/are relative to the other companies in its/their coverage universe: Ecopro BM, L&F, LG Chem, LG Energy Solution, Posco Future M, SK Innovation, Samsung SDI Co.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: LG Energy Solution (W332,000)

GS had an investment banking services client relationship during the past 12 months with: LG Energy Solution (W332,000)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: LG Energy Solution (W332,000)

GS had a non-securities services client relationship during the past 12 months with: LG Energy Solution (W332,000)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/848307722c616c261bc97c3e50258bdc46193378d8cc340ae2e6a4930dd15a07.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) LG Energy Solution (373220.KS)

<table><tr><td>Date of report</td><td>Target price (W)</td><td>Closing price (W)</td></tr><tr><td>01-Jun-26</td><td>520,000</td><td>455,000</td></tr><tr><td>11-Feb-26</td><td>410,000</td><td>392,000</td></tr><tr><td>11-Jan-26</td><td>440,000</td><td>363,000</td></tr><tr><td>13-Oct-25</td><td>355,000</td><td>360,000</td></tr><tr><td>03-Oct-25</td><td>350,000</td><td>399,000</td></tr><tr><td>28-Aug-25</td><td>365,000</td><td>364,000</td></tr><tr><td>27-Jul-25</td><td>375,000</td><td>363,500</td></tr><tr><td>08-Jun-25</td><td>345,000</td><td>291,000</td></tr><tr><td>10-Apr-25</td><td>355,000</td><td>349,500</td></tr><tr><td>02-Mar-25</td><td>375,000</td><td>352,000</td></tr><tr><td>08-Oct-24</td><td>455,000</td><td>436,500</td></tr><tr><td>04-Sep-24</td><td>450,000</td><td>399,500</td></tr><tr><td>25-Jul-24</td><td>455,000</td><td>332,500</td></tr><tr><td>08-Jul-24</td><td>485,000</td><td>358,500</td></tr><tr><td>25-Apr-24</td><td>500,000</td><td>372,500</td></tr><tr><td>25-Mar-24</td><td>515,000</td><td>414,500</td></tr><tr><td>28-Jan-24</td><td>530,000</td><td>381,000</td></tr><tr><td>09-Jan-24</td><td>550,000</td><td>417,500</td></tr><tr><td>25-Oct-23</td><td>610,000</td><td>409,500</td></tr><tr><td>03-Oct-23</td><td>620,000</td><td>476,500</td></tr><tr><td>27-Jul-23</td><td>605,000</td><td>540,000</td></tr><tr><td>09-Jul-23</td><td>610,000</td><td>-</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; c

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
