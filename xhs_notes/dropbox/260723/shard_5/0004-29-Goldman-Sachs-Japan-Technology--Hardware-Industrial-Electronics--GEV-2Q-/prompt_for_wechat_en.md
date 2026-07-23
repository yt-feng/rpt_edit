You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Japan Technology: Hardware - Industrial Electronics: GEV 2Q read-across: Strong power grid demand positive for Hitachi Energy

GE Vernova (covered by US Multi-Industry sector analyst Joe Ritchie) announced its 2Q FY26 results (LINK) on July 22. 2Q sales in the Electrification business, which handles power grid products, came to \$3,637 mn (FactSet consensus: \$3,437 mn), and EBITDA was \$671 mn (consensus: \$630 mn), both exceeding expectations. 2Q orders for the business were \$6,347 mn, up 93% yoy. GEV raised its full-year guidance for the business, lifting its sales outlook to \$14.5-\$15.0 bn from \$14.0-\$14.5 bn (including revised Prolec GE guidance of \$3.1 bn, up from \$3.0 bn); EBITDA margin guidance was maintained at 18-20%.

Ryo Harada
+81(3)4587-9865 | ryo.harada@gs.com
GS Japan Co., Ltd.

Hiroki Muramatsu
+81(3)4587-9872 |
hiroki.muramatsu@gs.com
GS Japan Co., Ltd.

The results confirmed that the demand environment for power grid products such as transformers and switchgear remains strong. Data center-related orders in 1H FY26 exceeded \$5 bn, already surpassing the full-year FY25 level, which suggests that in addition to conventional infrastructure upgrade demand, data center demand is also growing strongly. According to GEV, some shipments of solid state transformers (SSTs) to hyperscalers will also begin in the second half of this year, which could lead to increased demand for 800VDC-related products going forward. The confirmation of a strong demand environment has positive implications for Hitachi Energy, which operates a similar business. Hitachi's 1Q results are scheduled for release on July 29.

## Key points from the GE Vernova results briefing

Commentary below refers to the Electrification business.

2Q sales came to \$3,637 mn (FactSet consensus: \$3,437 mn), for organic growth of +29% yoy.

■ 2Q EBITDA was \$671 mn (consensus: \$630 mn), and the EBITDA margin was 18.4% (+390 bps yoy).

■ 2Q orders were \$6,347 mn, for organic growth of +66% yoy.

■ The order backlog was \$44.6 bn, up +65% yoy.

Demand was strong for grid equipment such as substations, switchgear, and transformers, with 2Q orders at roughly 1.7x sales.

■ Strong demand for switchgear, substations, transformers, and HVDC equipment drove sales growth.

■ EBITDA margins trended higher on increased volume, productivity gains, and price improvements.

\- The company booked \$2.7 bn in data center-related orders in 2Q alone and over \$5 bn for 1H FY26, surpassing the full-year FY25 level.

\- GEV commented that this \$5 bn in orders includes Solid State Transformers (SSTs), and that shipments of 5MW indoor SST prototypes to hyperscalers will begin in 2H of this year. It also said it is developing a 6MW outdoor SST.

■ Development of MV UPS is also underway, and the company expects to book orders for these sooner than for SSTs. It is targeting order wins from 2H26 to 2027.

The company won \$800 mn in transformer orders for the US market in 1H FY26. It said this reflects the benefits of establishing a global production system through the acquisition of Prolec GE.

■ GEV raised its full-year FY26 guidance. Sales guidance was lifted to \$14.5-\$15.0 bn (from \$14.0-\$14.5 bn), including Prolec GE guidance of \$3.1 bn (up from \$3.0 bn). EBITDA margin guidance was maintained at 18-20%.

## Price Target Risks and Methodology - Hitachi

We are Buy rated. Our 12-month target price of ¥6,300 for Hitachi is based on an EV/EBITDA multiple of 13X (base year is FY3/28E; the multiple is based on the EV/EBITDA and EBITDA margin correlation across its domestic and global competitors). Risks: Digital systems & services: delays and losses on large projects, weaker IT capex sentiment at customers accompanying a macroeconomic downturn, reemergence of supply disruptions for servers and other products, slower standalone growth at GlobalLogic, slower-than-expected realization of synergies between Hitachi and GlobalLogic; Energy (Power grid): delays on power transmission/distribution projects, a sharp rise in input costs; Connective industries: weaker new construction demand in China, losing out on new repair/maintenance orders to competitors in Japan, semiconductor production equipment (SPE) prices not improving over the long term a risk for the measurement and analysis systems business (Hitachi High-Tech); Companywide: Forex swings (¥1 appreciation vs. USD likely has a negative impact of ¥7 bn on sales and ¥0.8 bn on adjusted EBITA) and an increase in purchase price allocation (PPA) amortization due to forex swings.

## Disclosure Appendix

## Reg AC

We, Ryo Harada and Hiroki Muramatsu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ryo Harada GS Japan Co., Ltd., Hiroki Muramatsu GS Japan Co., Ltd..

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

The rating(s) for Hitachi is/are relative to the other companies in its/their coverage universe: Anritsu, Daihen, Fuji Electric Co., Fujikura, Furukawa Electric, Hitachi, Meidensha, Mitsubishi Electric, Panasonic Holdings, SWCC, Sumitomo Electric Industries

The rating(s) for GE Vernova is/are relative to the other companies in its/their coverage universe: 3M Co., ATS Corp., Allegion Plc, Carrier Global Corp., Cognex Corp., Core & Main Inc., Dover Corp., DuPont de Nemours Inc., EquipmentShare, Flowserve Corp., Forgent Power Solutions Inc., GE Vernova, Graco Inc., Honeywell International Inc., INNIO, ITT Inc., Illinois Tool Works, Ingersoll Rand Inc., Johnson Controls International Plc, Kennametal Inc., Lennox International Inc., Madison Air Solutions, Mirion Technologies Inc., Parker Hannifin Corp., RBC Bearings Inc., Regal Rexnord Corp., Rockwell Automation Inc., Roper Technologies Inc., Stanley Black & Decker Inc., Timken Co., Trane Technologies Plc, Vontier Corp., Zurn Elkay Water Solutions Corp., nVENT Electric Plc.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: GE Vernova (\$1,078.81), Hitachi (¥4,807) and Hitachi (ADR) (\$29.40)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: GE Vernova (\$1,078.81), Hitachi (¥4,807) and Hitachi (ADR) (\$29.40)

GS has received compensation for non-investment banking services during the past 12 months: Hitachi (¥4,807) and Hitachi (ADR) (\$29.40)

GS had an investment banking services client relationship during the past 12 months with: GE Vernova (\$1,078.81), Hitachi (¥4,807) and Hitachi (ADR) (\$29.40)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Hitachi (¥4,807) and Hitachi (ADR) (\$29.40)

GS had a non-securities services client relationship during the past 12 months with: GE Vernova (\$1,078.81), Hitachi (¥4,807) and Hitachi (ADR) (\$29.40)

GS makes a market in the securities or derivatives thereof: GE Vernova (\$1,078.81)

## Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/d4c9eaed7a40b2625d338b8443afb5442c6549cdb4a71e1af311d0c9e85cb3eb.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/3ae601915eb686408d0ed80bc85c2e5088a718385ee5f0c91f914c1a1121b2be.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

GE Vernova (GEV)

<table><tr><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>10-Jul-26</td><td>1,289.00</td><td>1,091.57</td></tr><tr><td>24-Apr-26</td><td>1,328.00</td><td>1,149.19</td></tr><tr><td>06-Apr-26</td><td>1,000.00</td><td>897.36</td></tr><tr><td>28-Jan-26</td><td>925.00</td><td>711.59</td></tr><tr><td>16-Dec-25</td><td>840.00</td><td>686.22</td></tr><tr><td>22-Oct-25</td><td>735.00</td><td>576.00</td></tr><tr><td>08-Sep-25</td><td>715.00</td><td>600.23</td></tr><tr><td>23-Jul-25</td><td>686.00</td><td>629.03</td></tr><tr><td>07-Jul-25</td><td>600.00</td><td>530.28</td></tr><tr><td>09-Jun-25</td><td>570.00</td><td>480.00</td></tr><tr><td>23-Jan-25</td><td>500.00</td><td>437.71</td></tr><tr><td>16-Jan-25</td><td>446.00</td><td>391.00</td></tr><tr><td>12-Dec-24</td><td>400.00</td><td>329.91</td></tr><tr><td>24-Oct-24</td><td>324.00</td><td>297.00</td></tr><tr><td>09-Oct-24</td><td>308.00</td><td>266.60</td></tr><tr><td>26-Jul-24</td><td>220.00</td><td>173.11</td></tr><tr><td>10-Jul-24</td><td>196.00</td><td>179.73</td></tr><tr><td>29-Apr-24</td><td>172.00</td><td>159.01</td></tr><tr><td>16-Apr-24</td><td>154.00</td><td>130.07</td></tr></table>

Hitachi (6501.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>07-Jul-26</td><td>6,300</td><td>4,942</td></tr><tr><td>27-Apr-26</td><td>6,100</td><td>5,356</td></tr><tr><td>19-Feb-26</td><td>5,700</td><td>4,992</td></tr><tr><td>29-Jan-26</td><td>6,100</td><td>5,077</td></tr><tr><td>05-Jan-26</td><td>6,000</td><td>5,068</td></tr><tr><td>17-Nov-25</td><td>5,900</td><td>5,122</td></tr><tr><td>30-Oct-25</td><td>5,600</td><td>4,963</td></tr><tr><td>08-Oct-25</td><td>5,300</td><td>4,477</td></tr><tr><td>28-Apr-25</td><td>4,900</td><td>3,747</td></tr><tr><td>16-Apr-25</td><td>4,800</td><td>3,260</td></tr><tr><td>31-Jan-25</td><td>5,600</td><td>3,946</td></tr><tr><td>22-Jan-25</td><td>5,200</td><td>3,929</td></tr><tr><td>23-Oct-24</td><td>5,400</td><td>3,896</td></tr><tr><td>07-Oct-24</td><td>4,870</td><td>3,904</td></tr><tr><td>02-Sep-24</td><td>4,830</td><td>3,603</td></tr><tr><td>31-Jul-24</td><td>4,850</td><td>3,288</td></tr><tr><td>18-Jul-24</td><td>4,800</td><td>3,663</td></tr><tr><td>11-Jun-24</td><td>18,300</td><td>3,412</td></tr><tr><td>07-Jun-24</td><td>18,000</td><td>3,270</td></tr><tr><td>03-Jun-24</td><td>17,600</td><td>3,313</td></tr><tr><td>26-Apr-24</td><td>17,100</td><td>2,695</td></tr><tr><td>12-Mar-24</td><td>16,700</td><td>2,467</td></tr><tr><td>31-Jan-24</td><td>13,500</td><td>2,335</td></tr><tr><td>19-Dec-23</td><td>13,000</td><td>1,988</td></tr><tr><td>16-Nov-23</td><td>12,300</td><td>2,009</td></tr><tr><td>16-Oct-23</td><td>12,000</td><td>1,806</td></tr><tr><td>28-Jul-23</td><td>10,300</td><td>1,742</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the ad

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
