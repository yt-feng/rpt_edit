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
# CHINA MERCHANTS PROP OPERATION (001914.SZ)

# Weak shareholder return outlook and asset impairment risk overhang; downgrade to Sell

We downgrade CMPO to Sell from Neutral given low visibility on both growth and improvement in shareholder return, alongside lingering IP write down risks:

\- Shareholder returns appear to be less of a focus compared to the rest of coverage PMs, with no indication of a plan to raise the dividend payout ratio beyond the current level of c.30%, placing CMPO's dividend yield (3%) at the lowest level for the coming three years among our coverage universe (average 6-7%).

IP write down risks aggravating amid macro adversities, which could overshadow the company's profitability stabilization. CMPO is the most “asset-heavy” property manager among our coverage universe, with Rmb5.5bn of investment properties sitting on its balance sheet, equivalent to 27% of CMPO's 1Q26 total assets. These assets, consisting of hotels, malls, offices, apartments and leasable public buildings with aggregate GFA of over 0.6mn sqm, have seen weakening occupancy rates (-2pp yoy in FY25) and rental income generation (-4% yoy, vs. CMPO's overall topline +12% in FY25). We expect unfavorable rental reversion and occupancy pressure due to low consumer confidence and macro headwinds, potentially leading to steeper fair value losses (vs. Rmb19mn in FY25) going ahead.

Margin likely under pressure: we expect CMPO's PMS GPM consistently to stay behind the peer average level by c.5pp for years and is unlikely to catch up considering 1) limited cash collection efforts spent so far; and 2) non-residential space offering limited pricing power against government customers and SOE affiliates. As such, we lower GPM forecasts by an average 0.3pp in 2026E-28E to average $9.7\%$ vs. $10.4\%$ in FY25, and cut our 2026E-28E earnings estimates by an average $5\%$ to $6\%$ CAGR. Our net profit forecasts are now on average $7\%$ below Wind consensus.

Revise our 12m TP to Rmb9.4 (from Rmb11.7), based on a 13X (from prior 15X) 2028E FCF discounted back to 2026E with a $9.7\%$ CoE, after we added a $10\%$ discount to the company's L-T multiple to reflect the aforementioned IP asset impairment risk (vs. $10\%$ credit discount that we applied to CGS and Onewo due to affiliated developer risks and nil discount to the rest of coverage). Correspondingly,

Yi Wang, CFA
+86(21)2401-8930 |
yi.wang@goldmansachs.cn
GS (China) Securities
Company Limited

Shi Xu
+86(21)2401-8929 |
shi.x.xu@goldmansachs.cn
GS (China) Securities
Company Limited

Kaiyan Jing
+86(21)2411-8092 |
kaiyan.jing@goldmansachs.cn
GS (China) Securities
Company Limited

our TP suggests 4% upside against PM coverage average of 24%. Downgrade to Sell from Neutral. CMPO trades at 10X/10X/9X 2026E-28E P/Es against a 6% EPS CAGR plus 3% yield vs. our PM coverage at 11X/9X/9X against a 10% EPS CAGR plus 7% yield. We could turn more positive on the company if we were to see 1) greater focus on shareholder returns (more generous dividend policy or the utilization of channels such as share buybacks) from management; 2) downward margin trend easing on the back of portfolio optimization and effective cost saving; 3) broader macroeconomic and consumer confidence recovery alleviating IP write down risks, or strong execution in heavy asset disposal.

Key risks: 1) Scale growth beat due to stronger-than-expected 3P projects engagements especially in the non-residential sphere on the back of group-level synergies or broader property sector recovery. 2) Faster-than-expected specialized value-added-services development (e.g. housekeeping services, NEV charging station, real estate brokerage, etc.) driven by broad-based consumption recovery, resulting in stronger-than-expected topline; 3) More resilient-than-expected margin profile through more effective cost-control initiatives, efficient technological empowerment and digitalization, rising project density/scale effect, broader economic/labor market recovery and consumer confidence pick-up, etc.

<table><tr><td>001914.SZ</td><td>12m Price Target: Rmb9.4</td><td colspan="2">Price: Rmb9.05</td><td colspan="2">Upside: 3.9%</td></tr><tr><td rowspan="2">Sell</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: Rmb9.5bn / $1.4bn</td><td>Revenue (Rmb mn) New</td><td>19,273.2</td><td>20,503.7</td><td>21,786.0</td><td>22,909.4</td></tr><tr><td>Enterprise value: Rmb4.0bn / $593.0mn</td><td>Revenue (Rmb mn) Old</td><td>19,273.2</td><td>20,503.7</td><td>21,786.0</td><td>22,909.4</td></tr><tr><td>3m ADTV :Rmb74.8mn/ $11.0mn</td><td>EBITDA (Rmb mn)</td><td>1,245.0</td><td>1,353.9</td><td>1,369.4</td><td>1,407.7</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>0.62</td><td>0.89</td><td>0.93</td><td>0.96</td></tr><tr><td rowspan="2">China Property Services</td><td>EPS (Rmb) Old</td><td>0.62</td><td>0.91</td><td>0.98</td><td>1.03</td></tr><tr><td>P/E (X)</td><td>18.5</td><td>10.1</td><td>9.7</td><td>9.4</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/B (X)</td><td>1.1</td><td>0.8</td><td>0.8</td><td>0.7</td></tr><tr><td rowspan="4">Leases incl. in net debt &amp; EV?: No</td><td>Dividend yield (%)</td><td>2.3</td><td>3.0</td><td>3.1</td><td>3.2</td></tr><tr><td>CROCI (%)</td><td>28.7</td><td>27.0</td><td>29.0</td><td>26.8</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.30</td><td>0.34</td><td>0.29</td><td>(0.04)</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 20 Jul 2028 close.

## Investment Thesis

CMPO is a diversified PM with the support from SOE parent CM Shekou to capture both residential/non-residential opportunities. We are Sell rated on the company as we see low visibility on growth and shareholder return improvement, alongside lingering IP write down risks. Shareholder returns appear to be less of a focus for CMPO vs peers and a persistently conservative dividend payout ratio places its dividend yield at the lowest level of our coverage universe for the coming three years. We also see IP write down risks, with CMPO as the most “asset-heavy” property manager among peers, carrying investment properties equivalent to nearly 30% of total assets but with a somewhat mixed track record in commercial operation, and this could lead to earnings downside amid macro adversities. We also believe CMPO needs some more time to catch up with peers in terms of PMS margin and specialized services development. The company currently trades at similar valuation to the peer average yet with lower EPS CAGR and a dividend yield at half the peer average.

## Price Target, Risks and Methodology

Our 12-month target price of Rmb9.4 is based on 13X 2028E FCF discounted back to 2026E with a 9.7% CoE.

Key risks: 1) Scale growth beat due to stronger-than-expected 3P project engagements on the back of group-level synergies or property sector recovery. 2)

Faster-than-expected specialized value-added-services development. 3) Upbeat margin profile due to effective cost control initiatives.

## Disclosure Appendix

## Reg AC

We, Yi Wang, CFA, Shi Xu and Kaiyan Jing, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Contributing Authors: Yi Wang, CFA GS (China) Securities Company Limited, Shi Xu GS (China) Securities Company Limited, Kaiyan Jing GS (China) Securities Company Limited.

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

The rating(s) for China Merchants Prop Operation is/are relative to the other companies in its/their coverage universe: Beijing New Building Materials, China Merchants Prop Operation, China Overseas Property Holdings, China Resources Mixc Lifestyle, Country Garden Services Holdings, Greentown Service Group, Onewo Inc., Oriental Yuhong, Poly Property Services Co., Skshu Paint Co., Vasen

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, "GS") and companies covered by GS Global Investment Research and referred to in this research.

There are no company-specific disclosures for: China Merchants Prop Operation (Rmb9.05)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/ddc14476adbb13e071c827ed3d7f476d32235b1825b88fe3ff0e94d49b3ebad4.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) China Merchants Prop Operation (001914.SZ)

Date of report Target price (Rmb) Closing price (Rmb)

<table><tr><td>28-Apr-26</td><td>11.70</td><td>10.12</td></tr><tr><td>16-Mar-26</td><td>12.20</td><td>10.38</td></tr><tr><td>23-Jan-26</td><td>12.60</td><td>11.75</td></tr><tr><td>11-Dec-25</td><td>13.10</td><td>11.06</td></tr><tr><td>17-Mar-25</td><td>12.90</td><td>11.92</td></tr><tr><td>13-Jan-25</td><td>12.00</td><td>9.79</td></tr><tr><td>31-Oct-24</td><td>10.40</td><td>11.56</td></tr><tr><td>30-Aug-24</td><td>10.00</td><td>8.79</td></tr><tr><td>10-Jul-24</td><td>11.40</td><td>9.42</td></tr><tr><td>26-Apr-24</td><td>12.00</td><td>10.12</td></tr><tr><td>18-Mar-24</td><td>13.50</td><td>10.95</td></tr><tr><td>22-Jan-24</td><td>14.00</td><td>10.23</td></tr><tr><td>27-Oct-23</td><td>19.00</td><td>13.53</td></tr><tr><td>25-Aug-23</td><td>19.50</td><td>15.63</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products i

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
