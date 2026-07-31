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
# Samsung SDI Co. (006400.KS): Core OP in line; AI infra batteries gain momentum

Samsung SDI (SDI) posted strong revenue growth (+19% YoY) and returned to operating profit of W204bn in 2Q26, following six consecutive loss-making quarters. Results included a one-off tariff refund of \~W200bn relating to duties paid last year; excluding this, operating profit was near Bloomberg consensus (-W13bn). Key takeaways from the analyst call:

Turnaround to be gradual and led by small cylindrical battery. UPS and BBU battery revenue are each guided to grow more than 70% YoY in 2026 with c.40-50% market share, and existing high-power cylindrical lines are running at full capacity with expansion planned; qualification barriers around instantaneous high-power output and safety supports higher profitability than other product categories.

US ESS order book extends through 2029 and points to a capacity constraint from 2028. Secured orders cover a substantial portion of capacity through 2029 and, including projects with a high likelihood of award in 2H26, demand is expected to exceed production capacity from 2028, with options to secure additional capacity under review; this compares with 2-3 years of local US capacity coverage guided at 1Q26.

EV recovery is Europe-led, with further order wins guided within the year. xEV losses are expected to narrow as volume models that entered mass production in 2Q26 ramp, though volume declines in existing projects were flagged as a risk. SDI is in discussion with multiple European OEMs off a prismatic lineup now spanning high-nickel, mid-nickel and LFP, and expects additional orders within the year following the Mercedes-Benz win in April.

all-solid-state. The 2H27 all-solid-state mass production target was maintained, with humanoid likely the first commercial application, samples due in 2H26, while EV development runs in parallel for expansion thereafter. Near term, the US prismatic LFP for ESS begins cell production in October with SBB 2.0 deliveries within the year; sodium-ion UPS and utility ESS solutions are in development with mass production lines being prepared, and SDI won its first project applying cylindrical batteries to HEV.

Key upside/downside risks: (1) Higher/lower-than-expected global EV penetration rate growth; (2) faster/slower-than-expected EV/ESS shipment and market share growth in battery-related business; (3) higher/lower-than-expected battery business margins, higher/lower-than-expected EM business margins; (4)

## Nikhil Bhandari

+65-6889-2867 | nikhil.bhandari@gs.com GS (Singapore) Pte

Giuni Lee
+82(2)3788-1177 | giuni.lee@gs.com
GS (Asia) L.L.C., Seoul Branch

John Tsang
+65-6654-5454 | john.tsang@gs.com
GS (Singapore) Pte

weaker/stronger-than-expected KRW:USD.

Exhibit 1: Samsung SDI 12M Fwd P/B vs ROE trend  
![](images/39bffbec7bc4d0c6ccedff42562f220f0b8e2e51c04960b86c42a4c5f360a584.jpg)  
Source: Refinitiv Eikon, GS Global Investment Research

## Investment Thesis - Samsung SDI

Samsung SDI (SDI) is a battery and electronic materials manufacturer maintaining industry-leading profitability levels in the large-sized battery business while becoming more of a pure-play battery company. We expect Samsung SDI battery margins to be more resilient than that of peers given long-term contracts with premium customers. Meanwhile, SDI is making good progress on technology leadership (alongside LGES) with strong know-how and a diversified new product offering (mass production of prismatic P6 with Ni >90%, cylindrical 46-pi, and solid state batteries). We also see potential for further cell order momentum in the US market as OEMs look for battery suppliers and form factor diversification.

While we remain positive on SDI's fundamentals, the stock is now already pricing in our base case xEV long-term market share and core xEV EBITDA margin growth; as well as our base case ESS assumptions. The stock is also trading above its long-term average 12m forward P/B multiple. We are Neutral rated on the stock.

## Price Target Risks and Methodology - Samsung SDI Co.

We are Neutral rated on Samsung SDI with a 2027E/28E SOTP-based 12m TP of W695,000 (xEV Battery: DCF; Small-size Battery/ESS/EM: 11x/14x/8x 27E/28E EBITDA multiple; Listed/unlisted subsidiaries: market/book value).

## Key upside/downside risks:

(1) Higher/lower-than-expected global EV penetration rate growth; (2) faster/slower-than-expected EV/ESS shipment and market share growth in battery-related business; (3) higher/lower-than-expected battery business margins, higher/lower-than-expected EM business margins and; (4) weaker/stronger-than-expected KRW:USD.

<table><tr><td>006400.KS</td><td colspan="2">12m Price Target: W695,000</td><td colspan="2">Price: W358,500</td><td colspan="2">Upside: 93.9%</td></tr><tr><td colspan="2">Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9" colspan="2">Market cap: W24.0tr / $16.6bnEnterprise value:W32.2tr / $22.3bn3m ADTV: W349.1bn / $232.1mnSouth KoreaKorea EV BatteryM&amp;A Rank: 3Leases incl. in net debt &amp; EV?:Yes</td><td>Revenue (W bn)</td><td>13,266.7</td><td>15,732.7</td><td>24,143.5</td><td>31,838.1</td></tr><tr><td>EBITDA (W bn)</td><td>380.6</td><td>2,438.3</td><td>4,684.2</td><td>6,290.3</td></tr><tr><td>EPS (W)</td><td>(8,253)</td><td>5,227</td><td>23,551</td><td>35,477</td></tr><tr><td>P/E (X)</td><td>NM</td><td>68.6</td><td>15.2</td><td>10.1</td></tr><tr><td>P/B (X)</td><td>0.7</td><td>1.2</td><td>1.1</td><td>1.0</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>23.9</td><td>3.4</td><td>1.7</td><td>1.0</td></tr><tr><td>CROCI (%)</td><td>2.0</td><td>3.9</td><td>6.5</td><td>7.9</td></tr><tr><td>FCF yield (%)</td><td>(14.6)</td><td>(0.8)</td><td>(1.6)</td><td>2.6</td></tr><tr><td colspan="2"></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td colspan="2"></td><td>EPS (W)</td><td>(356)</td><td>487</td><td>2,179</td><td>2,917</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 30 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Nikhil Bhandari, Giuni Lee and John Tsang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Nikhil Bhandari GS (Singapore) Pte, Giuni Lee GS (Asia) L.L.C., Seoul Branch, John Tsang GS (Singapore) Pte.

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

The rating(s) for Samsung SDI Co. is/are relative to the other companies in its/their coverage universe: Ecopro BM, L&F, LG Chem, LG Energy Solution, Posco Future M, SK Innovation, Samsung SDI Co.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Samsung SDI Co. (W358,500)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Samsung SDI Co. (W358,500)

GS had a non-securities services client relationship during the past 12 months with: Samsung SDI Co. (W358,500)

Distribution of ratings/investment banking relationships
GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/f40f9564a0bceb240df42b5e60b46e3a7074fde0bbbec22e3e92597c66e26d9d.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Samsung SDI Co. (006400.KS)

Date of report Target price (W) Closing price (W)

<table><tr><td>Date of Report</td><td>Target price (M)</td><td>Closing price (M)</td></tr><tr><td>01-Jun-26</td><td>695,000</td><td>652,000</td></tr><tr><td>11-Feb-26</td><td>410,000</td><td>377,000</td></tr><tr><td>11-Jan-26</td><td>360,000</td><td>267,500</td></tr><tr><td>03-Oct-25</td><td>225,000</td><td>206,500</td></tr><tr><td>28-Aug-25</td><td>235,000</td><td>216,000</td></tr><tr><td>31-Jul-25</td><td>240,000</td><td>201,000</td></tr><tr><td>08-Jun-25</td><td>260,000</td><td>174,300</td></tr><tr><td>27-Apr-25</td><td>270,000</td><td>185,100</td></tr><tr><td>10-Apr-25</td><td>300,000</td><td>177,200</td></tr><tr><td>02-Mar-25</td><td>340,000</td><td>218,876</td></tr><tr><td>06-Nov-24</td><td>530,000</td><td>291,672</td></tr><tr><td>04-Sep-24</td><td>560,000</td><td>349,811</td></tr><tr><td>30-Jul-24</td><td>630,000</td><td>322,940</td></tr><tr><td>25-Mar-24</td><td>730,000</td><td>474,883</td></tr><tr><td>30-Jan-24</td><td>740,000</td><td>365,934</td></tr><tr><td>09-Jan-24</td><td>800,000</td><td>422,118</td></tr><tr><td>26-Oct-23</td><td>850,000</td><td>413,324</td></tr><tr><td>03-Oct-23</td><td>890,000</td><td>500,289</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client's objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client's own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS' Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered 

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
