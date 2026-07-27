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
# Moderna Inc. (MRNA): 2Q earnings preview: Upcoming Phase 3 melanoma data is the primary catalyst

MRNA shares have outperformed the sector and the broader market (+61% vx. XBI; +76% vs. S&P 500 YTD), benefiting primarily from: 1) optimism into Phase 3 interim data from MRK-partnered individualized neoantigen therapy intismeran in adjuvant melanoma this year, a binary event that could establish the commercial oncology vertical and carries expansion opportunities on positive readthrough to other solid tumors per nine ongoing Phase 2 and 3 studies; and 2) increased investor comfort on the near-term revenue outlook, which has largely stabilized, noting FY26 guidance of up to 10% YoY revenue growth (GSe/consensus 7.2%/7.8%) is inclusive of a potential decline in US COVID vaccinations - we monitor areas for upside including an increase in mNEXSPIKE market share YoY and vaccination rates, with visibility into these dynamics emerging in summer/early fall given seasonality. We note short interest has pulled back and is at 52-week lows, in the context of these two factors, in our view - but still high on an absolute basis. At current levels (\$54/share), success in the aforementioned melanoma study is largely priced in - however, options markets imply +49% by mid-January on success and in the downside scenario, shares will move towards the base business (\~\$25/share) - see our deep dive into the data here.

For 2Q earnings, MRNA has guided to \$50-\$100mn in total revenue (GSe/FactSet consensus of \$90mn/\$103mn), split 50/50 between US/international geographies, and our analysis of script data suggests MRNA can meet the guide, albeit noting a portion of the total revenue is non-product and thus we have less visibility. We model for GAAP EPS of $2.11$ vs. consensus of $2.03$ . We expect questions on the call on: 1) the timing, disclosure strategy and statistical considerations on the Phase 3 melanoma data, 2) readthrough from melanoma to other solid tumor indications (we next expect Phase 2 data in renal cell carcinoma this year/early 2027 followed by muscle invasive bladder cancer, with non-small cell lung cancer data likely in 2027), 3) pipeline assets disclosed at the recent Science Day and 4) the revenue outlook in seasonal influenza, given the August 5th PDUFA for the vaccine (we expect approval), which could contribute to revenue in the US in 2027+.

We expect an in-line 2Q GAAP EPS. For 2Q earnings, we project total revenue of \$90mn (vs. FactSet consensus of \$103mn), driven primarily by Spikevax/mNEXSPIKE/mRESVIA product revenues of \$58mn and other revenues of \$32mn (inclusive of manufacturing revenue and collaboration revenue). MRNA has guided to \$50-100mn in revenue in 2Q. We model for GAAP EPS of $2.11$ vs. consensus of $2.03$ .

Salveen Richter, CFA
+1(212)934-4204 |
salveen.richter@gs.com
GS & Co. LLC

Elizabeth Webster, Ph.D.
+1(212)357-9925 |
elizabeth.webster@gs.com
GS & Co. LLC

Mark Aleynick, Ph.D.
+1(212)357-6820 |
mark.aleynick@gs.com
GS & Co. LLC

Matt Dellatorre, Ph.D.
+1(212)855-0830 |
matt.dellatorre@gs.com
GS & Co. LLC

Tommie Reerink, CFA
+1(212)357-2470 |
tommie.reerink@gs.com
GS & Co. LLC

Lydia Erdman  
+1(212)357-6383 | lydia.erdman@gs.com GS & Co. LLC

Shrunatra Mishra
+1(332)245-7673 |
shrunatra.mishra@gs.com
GS India SPL

Exhibit 1: GSe vs. consensus

<table><tr><td rowspan="5">MRNA</td><td rowspan="2"></td><td colspan="2">2Q26</td><td colspan="3">FY26</td><td colspan="2">FY27</td></tr><tr><td>GSe</td><td>Cons.</td><td>GSe</td><td>Cons.</td><td>Guidance</td><td>GSe</td><td>Cons.</td></tr><tr><td>Product revenue ($mn)</td><td>$58</td><td>$60</td><td>$1,919</td><td>$1,911</td><td></td><td>$2,024</td><td>$2,523</td></tr><tr><td>Total revenue ($mn)</td><td>$90</td><td>$103</td><td>$2,083</td><td>$2,095</td><td>Up to 10% YoY growth</td><td>$2,204</td><td>$2,523</td></tr><tr><td>GAAP EPS</td><td>($2.11)</td><td>($2.03)</td><td>($9.08)</td><td>($8.66)</td><td></td><td>($4.82)</td><td>($4.77)</td></tr></table>

Source: Data compiled by GS Global Investment Research, FactSet

Key catalysts: In the oncology vertical, which we see as the key driver for MRNA shares, we expect multiple catalysts through 1H27. Notably for MRK-partnered individualized neoantigen vaccine intismeran, we anticipate: 1) interim Ph3 adjuvant melanoma data in combination with Keytruda in 2H26, the key source of investor focus, 2) Ph2 data this year or early-2027 in adjuvant renal cell carcinoma (RCC), followed by muscle invasive bladder cancer in 2027, and 3) Ph3 non-small cell lung cancer (NSCLC) data in 2027 (the next update in NSCLC will be around completing trial enrollment, which will inform our timing expectations). Outside of intismeran but within oncology, we expect 1) initial data from Ph1/2 T-cell engager mRNA-2808 in multiple myeloma this year, where MRNA sees potential for differentiation versus traditional bispecific approaches per targeting three antigens (BCMA, GPRC5D, and FcRH5) - we acknowledge this as important given the competitive/crowded treatment landscape, 2) additional Ph1/2 data from cancer antigen therapy mRNA-4359 (targeting PD-L1 and IDO1) in 2027, 3) Ph1 data in 2H26 and Ph2 proof-of-concept data in 2028 for the therapeutic addressing Epstein-Barr virus associated conditions including multiple sclerosis, and 4) data from additional cancer antigen therapies in advanced solid tumors in 2027+. We also note the August 5th PDUFA for the seasonal influenza monotherapy (we largely expect approval), which could contribute to topline revenue in the US in 2027+, and Ph3 norovirus data and registrational data in rare disease propionic acidemia this year, both less a focus for the Street.

Exhibit 2: Key catalysts into 2027

<table><tr><td>Company</td><td>Timing</td><td>Drug</td><td>Event</td></tr><tr><td rowspan="12">MRNA</td><td>2H26</td><td>intismeran autogene</td><td>Potential interim Ph3 data in adjuvant melanoma</td></tr><tr><td>August 5th</td><td>mRNA-1010</td><td>PDUFA for seasonal influenza vaccine (aged 50+)</td></tr><tr><td>2H26</td><td>mRNA-3927</td><td>Registrational data in PA</td></tr><tr><td>2H26</td><td>mNEXSPIKE (mRNA-1283)</td><td>Approvals and strain updates in Australia, Europe, Japan, and Taiwan</td></tr><tr><td>2H26</td><td>mRNA-1403 (norovirus vaccine)</td><td>Interim Ph3 data</td></tr><tr><td>2H26</td><td>mRNA-2808 (TCE in multiple myeloma)</td><td>Ph1/2 dose escalation data at a medical meeting</td></tr><tr><td>2H26</td><td>mRNA-1195 (MS therapeutic)</td><td>Ph1 Part B data (EBV sero-pos and neg.), safety and reacto, humoran immunogenicity and viral shedding</td></tr><tr><td>2H26/early-2027</td><td>intismeran autogene</td><td>Potential Ph2 data in renal cell carcinoma</td></tr><tr><td>2027</td><td>intismeran autogene</td><td>Potential Ph2 data in muscle invasive bladder cancer</td></tr><tr><td>2027</td><td>Multiple</td><td>Additional cancer antigen therapy data</td></tr><tr><td>2027</td><td>mRNA-4359</td><td>Full Ph2 data from wholly-owned cancer antigen therapy targeting PD-L1/IDO</td></tr><tr><td>2027</td><td>intismeran autogene</td><td>Ph3 data in NSCLC</td></tr></table>

Source: Data compiled by GS Global Investment Research

## Valuation and Risks

MRNA (Neutral): We are Neutral rated on MRNA. Our 12-month PT of \$67 is based on a 100% DCF value (4% TGR, 11% WACC). Upside risks: Commercial risk - higher than anticipated sales and penetration into patient populations, earlier-than-expected approval timelines from the INT programs, other pipeline success and competitive failures. Downside risks: Failure to demonstrate clinical proof of concept across additional modalities, such as latent viral vaccines, or across additional oncology indications, IP risk, manufacturing difficulties and financing/dilution, failure to achieve the projected commercial profile, physician/payor pushback on use and coverage, approval of competitor drugs.

<table><tr><td>MRNA</td><td>12m Price Target: $67.00</td><td colspan="2">Price: $54.07</td><td colspan="2">Upside: 23.9%</td></tr><tr><td colspan="2">Neutral</td><td colspan="4">GS Forecast</td></tr><tr><td></td><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td></tr><tr><td rowspan="11" colspan="2">Market cap: $21.3bn Enterprise value: $20.3bn 3m ADTV: $448.8mn United States Americas Biotechnology M&amp;A Rank: 3</td><td>Revenue ($ mn)</td><td>1,944.0</td><td>2,083.2</td><td>2,204.2</td></tr><tr><td>EBITDA ($ mn)</td><td>(2,859.0)</td><td>(3,644.8)</td><td>(1,923.3)</td></tr><tr><td>EBIT ($ mn)</td><td>(3,074.0)</td><td>(3,767.9)</td><td>(2,017.8)</td></tr><tr><td>EPS ($)</td><td>(7.25)</td><td>(9.08)</td><td>(4.82)</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EV/EBITDA (X)</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>FCF yield (%)</td><td>(18.1)</td><td>(14.0)</td><td>(5.0)</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>-</td><td>-</td><td>-</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td></tr><tr><td>EPS ($)</td><td>(3.40)</td><td>(2.11)</td><td>(1.60)</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 24 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Salveen Richter, CFA, Elizabeth Webster, Ph.D., Mark Aleynick, Ph.D., Matt Dellatorre, Ph.D., Tommie Reerink, CFA, Lydia Erdman and Shrunatra Mishra, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Salveen Richter, CFA GS & Co. LLC, Elizabeth Webster, Ph.D. GS & Co. LLC, Mark Aleynick, Ph.D. GS & Co. LLC, Matt Dellatorre, Ph.D. GS & Co. LLC, Tommie Reerink, CFA GS & Co. LLC, Lydia Erdman GS & Co. LLC, Shrunatra Mishra GS India SPL.

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

The rating(s) for Moderna Inc. is/are relative to the other companies in its/their coverage universe: 4D Molecular Therapeutics, Acadia Pharmaceuticals Inc., Agios Pharmaceuticals Inc., Alnylam Pharmaceuticals Inc., Amgen Inc., Annexon Biosciences, BioMarin Pharmaceutical Inc., Biogen Inc., CRISPR Therapeutics, Denali Therapeutics Inc., Enliven Therapeutics Inc., Generate Biomedicines Inc., Gilead Sciences Inc., Immunome Inc., Incyte Corp., Intellia Therapeutics, Ionis Pharmaceuticals Inc., Moderna Inc., Rapport Therapeutics, Regeneron Pharmaceuticals Inc., Relay Therapeutics, Sarepta Therapeutics Inc., Summit Therapeutics Inc., Taysha Gene Therapies Inc., Ultragenyx Pharmaceutical, Vertex Pharmaceuticals Inc., uniQure

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Moderna Inc. (\$54.07)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Moderna Inc. (\$54.07)

GS had an investment banking services client relationship during the past 12 months with: Moderna Inc. (\$54.07)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Moderna Inc. (\$54.07)

GS had a non-securities services client relationship during the past 12 months with: Moderna Inc. (\$54.07)

GS makes a market in the securities or derivatives thereof: Moderna Inc. (\$54.07)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/298f146af91841b2cbe7fdbd460c17414a46f5b9048269036dae275628b8e19f.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Moderna Inc. (MRNA)

<table><tr><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>20-Jul-26</td><td>67.00</td><td>59.49</td></tr><tr><td>01-May-26</td><td>49.00</td><td>45.37</td></tr><tr><td>17-Apr-26</td><td>43.00</td><td>53.72</td></tr><tr><td>13-Feb-26</td><td>41.00</td><td>42.23</td></tr><tr><td>12-Jan-26</td><td>36.00</td><td>33.84</td></tr><tr><td>06-Nov-25</td><td>33.00</td><td>24.33</td></tr><tr><td>17-Oct-25</td><td>34.00</td><td>26.01</td></tr><tr><td>14-Apr-25</td><td>35.00</td><td>26.80</td></tr><tr><td>14-Feb-25</td><td>49.00</td><td>32.99</td></tr><tr><td>29-Jan-25</td><td>51.00</td><td>40.72</td></tr><tr><td>27-Jan-25</td><td>99.00</td><td>41.65</td></tr><tr><td>07-Nov-24</td><td>112.00</td><td>50.28</td></tr><tr><td>04-Oct-24</td><td>130.00</td><td>60.20</td></tr><tr><td>13-Sep-24</td><td>139.00</td><td>68.28</td></tr><tr><td>02-Aug-24</td><td>178.00</td><td>86.58</td></tr><tr><td>02-May-24</td><td>204.00</td><td>125.59</td></tr><tr><td>22-Feb-24</td><td>206.00</td><td>99.44</td></tr><tr><td>22-Jan-24</td><td>232.00</td><td>99.70</td></tr><tr><td>03-Nov-23</td><td>231.00</td><td>77.53</td></tr><tr><td>13-Oct-23</td><td>269.00</td><td>98.30</td></tr><tr><td>04-Aug-23</td><td>285.00</td><td>108.19</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in de

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
