你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
