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
# Digital Realty Trust Inc. (DLR): 2Q26 review: Growing backlog and favorable pricing dynamics support beat & raise

DLR’s core FFO per share of \$2.65 beat GS/consensus (Visible Alpha) of \$1.97/\$1.98 driven by strong underlying growth, as well as net promote; excluding net promote, core FFO per share of \$2.13 still beat. First, bookings of \$208 mn at DLR share included \$108 mn of 0-1MW and interconnection bookings, beating consensus bookings of \$199 mn (but missing our estimate of \$247 mn). Notably, DLR signed 2 hyperscaler leases in July representing \$205 mn bookings at DLR share. Second, DLR renewed \$261 mn of annualized rental revenue at 25% cash renewal spread reflecting 5% spreads in 0-1MW and 67% spreads in >1MW related to supply/demand tightness in Singapore. Third, DLR raised its 2026E core FFO per share (excludes net promote) guidance to \$8.15-\$8.20 (v. \$8.00-\$8.10). DLR expects commencements to accelerate meaningfully in 2H26 as \$635mn of annualized rent is scheduled to commence (45% in 3Q26 & 55% in 4Q26). DLR is also seeing growing fee income within its strategic private capital platform. We continue to view DLR as among the best positioned to satisfy hyperscale demand for wholesale capacity with \~1.4GW under construction, and view the company’s growing and increasingly diversified backlog (\$1.4 bn DLR share exiting 2Q26 with new markets and 142 customers added in 2Q26) as reflective of the visibility into the company’s ability to see continued growth over the medium term.

Read-through to our coverage: DLR noted increasing levels of engagement from customers deploying AI-enabled applications, which we see as a positive read through for Equinix (reporting July 29), which is more indexed towards retail colocation.

DLR delivered an in-quarter beat and raise driven by strength in rental revenues.

■ DLR rental revenue of \$1,146 mn beat GSe/Visible Alpha Consensus \$1,094/\$1,119 mn.

☐ Total revenue came in at \$1,924 mn above GS at \$1,615 mn and the Street at \$1,655 mn.

☐ DLR’s share of total new bookings came in at \$208 mn at its share (v. GS at \$247 mn), down from \$243 mn in 1Q26 but up from \$135 mn in 2Q25. 0-1 MW plus interconnect bookings were \$108 mn, up from \$98 mn in 1Q26 and \$90 mn in 2Q25.

\- Adjusted EBITDA of \$978 mn beat our estimate of \$913 mn and the Street at \$914 mn.

Michael Ng, CFA
+1(212)902-8618 | michael.ng@gs.com
GS & Co. LLC

Lindsey Shema
+1(801)578-2673 |
lindsey.shema@gs.com
GS & Co. LLC

Yash Goenka, CFA
+1(212)934-6312 |
yash.goenka@gs.com
GS India SPL

Zorayda Montemayor
+1(212)357-6403 |
zorayda.montemayor@gs.com
GS & Co. LLC

Core FFO per share (excluding net promote) came in at \$2.13, above GSe/consensus at \$1.97/\$1.98.

■ AFFO per share came in at \$2.47, above GS/Street at \$1.84/\$1.80.

2026 guidance updated, including: (1) Core FFO per share of \$8.15-\$8.20 (v. \$8.00-\$8.10 prior); (2) 2026 revenues of \$6,850-\$6,950 mn (v. \$6,650-\$6,750 mn prior); (3) 2026 cash basis rental rates on renewal leases of 9.0-11.0% (v. 6.5-8.5% prior); (4) Adjusted EBITDA between \$3.75-\$3.85 bn (v. \$3.65-\$3.75 bn prior); (5) Development capex (net of partner contributions) between \$4.25-\$4.75 bn (v. \$3.5-\$4.0 bn prior); and (6) recurring capex between \$400-\$425 mn (unchanged).

Estimate changes: We raise our revenue/EBITDA estimates by 7%/4% on average in 2026/27/28 on the company’s raised outlook.

Price target and risks. We are Buy rated on DLR with a 12-month revised target price of \$223 (vs \$215 prior) based on a 26X (unchanged) NTM+1Y P/AFFO. Our price target increases due to rolling over our NTM+1Y AFFO.

Key downside risks: (1) excess supply-side dynamics in the data center market; (2) weaker-than-expected demand dynamics from key datacenter customers; (3) more intense price competition.

We reiterate our Buy rating on DLR. We believe Digital Realty is well positioned to benefit from the supply/demand tightness in the datacenter industry, which we think will persist for longer than the market expects.

Exhibit 1: Digital Realty - Variance summary

<table><tr><td></td><td colspan="5">2Q26</td><td colspan="2">2Q25</td></tr><tr><td>Consolidated ($ millions)</td><td>Actual</td><td>GS</td><td>Actual/Gse</td><td>Street</td><td>Actual/Street</td><td>Actual</td><td>Y/Y %</td></tr><tr><td>Rental revenues</td><td>1,146</td><td>1,094</td><td>4.7%</td><td>1,119</td><td>2.4%</td><td>1,004</td><td>19.3%</td></tr><tr><td>Total Revenue</td><td>1,924</td><td>1,615</td><td>19.1%</td><td>1,655</td><td>16.3%</td><td>1,493</td><td>36.7%</td></tr><tr><td>Adjusted EBITDA</td><td>978</td><td>913</td><td>7.1%</td><td>914</td><td>6.9%</td><td>823</td><td>23.6%</td></tr><tr><td>Core FFO per share</td><td>$2.13</td><td>$1.97</td><td>8.1%</td><td>$1.98</td><td>7.5%</td><td>$1.87</td><td>20.1%</td></tr><tr><td>AFFO</td><td>889</td><td>659</td><td>34.9%</td><td>642</td><td>38.4%</td><td>576</td><td>45.7%</td></tr><tr><td>AFFO per Share</td><td>$2.47</td><td>$1.84</td><td>34.4%</td><td>$1.80</td><td>37.2%</td><td>$1.68</td><td>38.9%</td></tr><tr><td>Leasing</td><td>208</td><td>247</td><td>-15.6%</td><td>199</td><td>4.7%</td><td>135</td><td>-14.0%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

Exhibit 2: Digital Realty - Old vs. new estimates

<table><tr><td></td><td colspan="7">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Consolidated ($ millions)</td><td>New</td><td>Old</td><td>Δ</td><td>Y/Y (%)</td><td>Guidance</td><td>Street</td><td>GS/Street</td><td>New</td><td>Old</td><td>Δ</td><td>New</td><td>Old</td><td>Δ</td></tr><tr><td>Rental revenues</td><td>4,712</td><td>4,512</td><td>4.4%</td><td>15.4%</td><td></td><td>4,558</td><td>3.4%</td><td>5,642</td><td>5,182</td><td>8.9%</td><td>6,308</td><td>5,788</td><td>9.0%</td></tr><tr><td>Total Revenue</td><td>7,170</td><td>6,703</td><td>7.0%</td><td>17.3%</td><td>6,850 - 6,950 mn</td><td>6,754</td><td>6.2%</td><td>8,046</td><td>7,519</td><td>7.0%</td><td>8,889</td><td>8,298</td><td>7.1%</td></tr><tr><td>Adjusted EBITDA</td><td>3,855</td><td>3,758</td><td>2.6%</td><td>15.5%</td><td>3,750 - 3,850 mn</td><td>3,729</td><td>3.4%</td><td>4,394</td><td>4,214</td><td>4.3%</td><td>4,791</td><td>4,588</td><td>4.4%</td></tr><tr><td>EPS</td><td>$3.13</td><td>$2.68</td><td>16.8%</td><td>-14.1%</td><td></td><td>$2.08</td><td>50.5%</td><td>$2.08</td><td>$2.02</td><td>3.3%</td><td>$2.41</td><td>$2.33</td><td>3.6%</td></tr><tr><td>Core FFO per share</td><td>$8.20</td><td>$8.14</td><td>0.8%</td><td>10.9%</td><td>$8.150 - $8.200</td><td>$8.04</td><td>2.0%</td><td>$9.03</td><td>$8.83</td><td>2.3%</td><td>$9.68</td><td>$9.49</td><td>2.0%</td></tr><tr><td>AFFO</td><td>2,628</td><td>2,600</td><td>1.1%</td><td>15.9%</td><td></td><td>2,557</td><td>2.8%</td><td>3,244</td><td>3,008</td><td>7.8%</td><td>3,558</td><td>3,305</td><td>7.7%</td></tr><tr><td>AFFO per Share</td><td>$7.14</td><td>$7.25</td><td>-1.5%</td><td>9.0%</td><td></td><td>$7.12</td><td>0.3%</td><td>$8.35</td><td>$8.13</td><td>2.7%</td><td>$8.92</td><td>$8.72</td><td>2.3%</td></tr><tr><td>Leasing</td><td>1,071</td><td>1,168</td><td>-8.3%</td><td>50.0%</td><td></td><td>1,131</td><td>-5.3%</td><td>916</td><td>1,015</td><td>-9.8%</td><td>937</td><td>1,038</td><td>-9.8%</td></tr></table>

Source: Company data, GS Global Investment Research

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $64.7bn</td><td>Revenue ($ mn) New</td><td>6,112.7</td><td>7,170.5</td><td>8,045.7</td><td>8,889.3</td></tr><tr><td>Enterprise value: $83.6bn</td><td>Revenue ($ mn) Old</td><td>6,112.7</td><td>6,702.9</td><td>7,518.9</td><td>8,297.9</td></tr><tr><td>3m ADTV: $523.3mn</td><td>EBITDA ($ mn)</td><td>3,339.1</td><td>3,855.0</td><td>4,393.5</td><td>4,790.9</td></tr><tr><td>United States</td><td>EBIT ($ mn)</td><td>658.5</td><td>1,124.7</td><td>1,331.9</td><td>1,514.3</td></tr><tr><td rowspan="2">Americas Hardware, Media, Cable,Telco</td><td>EPS ($) New</td><td>3.65</td><td>3.13</td><td>2.08</td><td>2.41</td></tr><tr><td>EPS ($) Old</td><td>3.65</td><td>2.68</td><td>2.02</td><td>2.33</td></tr><tr><td rowspan="3">M&amp;A Rank: 3</td><td>P/E (X)</td><td>45.4</td><td>57.3</td><td>86.1</td><td>74.4</td></tr><tr><td>Dividend yield (%)</td><td>3.0</td><td>2.7</td><td>2.7</td><td>2.7</td></tr><tr><td>Net debt/EBITDA (X)</td><td>4.5</td><td>4.5</td><td>4.5</td><td>4.5</td></tr><tr><td></td><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td></td><td>EPS ($)</td><td>1.21</td><td>0.71</td><td>0.72</td><td>0.44</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 23 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Michael Ng, CFA, Lindsey Shema, Yash Goenka, CFA and Zorayda Montemayor, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Michael Ng, CFA GS & Co. LLC, Lindsey Shema GS & Co. LLC, Yash Goenka, CFA GS India SPL, Zorayda Montemayor GS & Co. LLC.

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

The rating(s) for Digital Realty Trust Inc. is/are relative to the other companies in its/their coverage universe: AT&T Inc., American Tower Corp., Apple Inc., Arista Networks Inc., Axon Enterprise Inc., Blend Labs, Celestica Inc., Charter Communications Inc., Cisco Systems Inc., Cogent Communications Holdings, Comcast Corp., Compass Inc., Crown Castle Inc., Dell Technologies Inc., Digital Realty Trust Inc., Equinix Inc., F5 Inc., HP Inc., Hewlett Packard Enterprise Co., IREN Ltd., Ingram Micro, Lumen Technologies Inc., NetApp Inc., Opendoor Technologies Inc., Optimum Communications Inc., Penguin Solutions Inc., SBA Communications Corp., Stagwell Inc., Super Micro Computer Inc., T-Mobile US Inc., TD SYNNEX Corp., Verizon Communications, Versant Media Group, Walt Disney Co., Zillow Group

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Digital Realty Trust Inc. (\$179.34)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Digital Realty Trust Inc. (\$179.34)

GS had an investment banking services client relationship during the past 12 months with: Digital Realty Trust Inc. (\$179.34)

GS had a non-securities services client relationship during the past 12 months with: Digital Realty Trust Inc. (\$179.34)

GS makes a market in the securities or derivatives thereof: Digital Realty Trust Inc. (\$179.34)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys

and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/73f3982de3ad9cddb23ea1ffde807c94f78dfb374fa0975a405a809b3e42bafc.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Digital Realty Trust Inc. (DLR)

<table><tr><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>24-Apr-26</td><td>215.00</td><td>200.00</td></tr><tr><td>06-Feb-26</td><td>190.00</td><td>171.62</td></tr><tr><td>18-Dec-25</td><td>188.00</td><td>147.93</td></tr><tr><td>24-Jul-25</td><td>205.00</td><td>180.02</td></tr><tr><td>03-Apr-25</td><td>195.00</td><td>141.09</td></tr><tr><td>14-Feb-25</td><td>205.00</td><td>164.28</td></tr><tr><td>12-Dec-24</td><td>208.00</td><td>187.13</td></tr><tr><td>25-Oct-24</td><td>190.00</td><td>181.01</td></tr><tr><td>26-Sep-24</td><td>185.00</td><td>162.06</td></tr><tr><td>01-Jul-24</td><td>175.00</td><td>152.13</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant 

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

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any

such system.
"""
