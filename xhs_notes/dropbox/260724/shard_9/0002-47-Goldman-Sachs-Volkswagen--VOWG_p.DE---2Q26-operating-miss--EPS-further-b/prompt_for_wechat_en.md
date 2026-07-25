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
# Volkswagen (VOWG\_p.DE): 2Q26 operating miss, EPS further burdened by tax while auto cash flow beat; growth outlook revised down

Volkswagen reported 2Q26 results today (24th of July). We expect VW 2026 consensus EPS to see LSD downgrades mechanically on lower growth ambitions (now -3%-0% prior 0%-3%). We remain Neutral rated.

Operating miss driven by Progressive/Luxury and special costs: VW reported 2Q26 group op. profit of €3.47bn, 10% below company-compiled consensus (€3.85bn, GSe €4.04bn) while revenues were 1.3% above expectations, leading to an 4.2% RoS (cons 4.7%, GSe 5.0%). The miss was largely driven by a miss in Brand Group Progressive (-29% below EBIT cons) burdened by residual value revaluation effects and Luxury Brand beat by 12%. The operating line was also burdened by a low 3-digit (GSe €100mn) one-off cost related to the discontinued Bosch partnership. Meanwhile, Brand Group Core beat expectations on operating result by 8.5% (cons €1.91bn, GSe €2.23bn). China proportionate at-equity income for the 2Q stood at €101mn (GSe €35mn). On EPS (prefs) level, VW missed expectations, reporting €2.56 (cons €4.70, GSe €4.75) as a negative financial result and a higher tax rate mainly dragged below operating line results.

Strong 2Q cash flow beat: 2Q cash flow came in 101% above expectations (cons €583mn, GSe -€592mn). The better-than-expected auto net cash flow was driven by €1.5bn lower cash consumption in working capital, €0.9bn lower investment in capex/R&D, €0.1bn lower M&A expense and the -€0.9bn Rivian investment being slightly offset by the Sinotruk stake sale by €0.3bn. 2Q auto cash R&D was €4.68bn (GSe €4.96bn) with capitalized development costs of €2.08bn (GSe €2.25bn) lifting PnL by €99mn (GSe €147mn).

2026 outlook adjusted on top-line: The company adjusted its outlook, now expecting lower sales revenue -3%-0% (prior 0-3%) but maintained its operating margin of 4.0-5.5%. Cash flow guidance and net liquidity also remains unchanged despite the strong 2Q performance. The company highlights that these estimates do not factor potential effects arising from development and implementation of the Group Target Picture 2030 as well as the announced Everllence stake sale.

Key questions for the call: 1) Progress and execution of ongoing cost initiatives; 2) Updates on Everllence sale process and potential other cash return opportunities in FY26; 3) Outlook on China JV business and competitive landscape; 4) European competitive landscape

Christian Frenes  
+44(20)7051-8641 |  
christian.frenes@gs.com  
GS International

Robert Triulzi  
+44(20)7552-2281 | robert.triulzi@gs.com GS International

Monika Mengting Liu, CFA
+44(20)7051-7601 | monika.liu@gs.com
GS International

Shivam Kotecha
+1(332)245-7822 |
shivam.kotecha@gs.com
GS India SPL

## Volkswagen vs GSe and consensus

Exhibit 1: VW 2Q26 vs GSe and company-compiled consensus

<table><tr><td rowspan="2">€ mn</td><td colspan="6">2Q26</td><td colspan="3">2026E</td></tr><tr><td>Reported</td><td>GSe</td><td>Cons</td><td>Reported vs. GSe</td><td>Reported vs. Cons</td><td>GSe vs. Cons</td><td>GSe</td><td>Cons</td><td>GSe vs. Cons</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Brand Group Core</td><td>38,161</td><td>37,601</td><td>36,855</td><td>1.5%</td><td>3.5%</td><td>2.0%</td><td>145,492</td><td>145,597</td><td>-0.1%</td></tr><tr><td>Brand Group Progressive</td><td>14,999</td><td>17,532</td><td>16,493</td><td>-14.4%</td><td>-9.1%</td><td>6.3%</td><td>64,870</td><td>65,281</td><td>-0.6%</td></tr><tr><td>Brand Group Sport Luxury</td><td>7,777</td><td>8,243</td><td>7,842</td><td>-5.7%</td><td>-0.8%</td><td>5.1%</td><td>31,944</td><td>31,225</td><td>2.3%</td></tr><tr><td>Brand Group Trucks</td><td>11,310</td><td>10,719</td><td>11,156</td><td>5.5%</td><td>1.4%</td><td>-3.9%</td><td>44,235</td><td>44,008</td><td>0.5%</td></tr><tr><td>VW Financial Services</td><td>15,743</td><td>14,424</td><td>15,396</td><td>9.1%</td><td>2.3%</td><td>-6.3%</td><td>62,417</td><td>61,255</td><td>1.9%</td></tr><tr><td>Other Segments</td><td>-5,546</td><td>28,106</td><td>-6,365</td><td>NA</td><td>NA</td><td>NA</td><td>-22,070</td><td>-24,740</td><td>NA</td></tr><tr><td>Group</td><td>82,444</td><td>81,283</td><td>81,377</td><td>1.4%</td><td>1.3%</td><td>-0.1%</td><td>326,887</td><td>322,626</td><td>1.3%</td></tr><tr><td>Operating Profit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Brand Group Core</td><td>2,070</td><td>2,276</td><td>1,908</td><td>-9.0%</td><td>8.5%</td><td>19.3%</td><td>7,325</td><td>6,936</td><td>5.6%</td></tr><tr><td>Brand Group Progressive</td><td>533</td><td>635</td><td>750</td><td>-16.1%</td><td>-29.0%</td><td>-15.3%</td><td>3,438</td><td>3,699</td><td>-7.1%</td></tr><tr><td>Brand Group Sport Luxury</td><td>692</td><td>704</td><td>621</td><td>-1.7%</td><td>11.5%</td><td>13.4%</td><td>2,005</td><td>1,856</td><td>8.0%</td></tr><tr><td>Brand Group Trucks</td><td>902</td><td>765</td><td>771</td><td>17.9%</td><td>17.0%</td><td>-0.7%</td><td>2,675</td><td>2,599</td><td>3.0%</td></tr><tr><td>VW Financial Services</td><td>805</td><td>824</td><td>846</td><td>-2.3%</td><td>-4.8%</td><td>-2.5%</td><td>3,531</td><td>3,630</td><td>-2.7%</td></tr><tr><td>Other Segments</td><td>-1,533</td><td>3,093</td><td>-1,048</td><td>NA</td><td>NA</td><td>NA</td><td>-4,481</td><td>-4,600</td><td>NA</td></tr><tr><td>Group</td><td>3,469</td><td>4,041</td><td>3,848</td><td>-14.2%</td><td>-9.8%</td><td>5.0%</td><td>14,494</td><td>14,120</td><td>2.6%</td></tr><tr><td>Operating margin, %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Brand Group Core</td><td>5.4%</td><td>6.1%</td><td>5.2%</td><td>-0.6%</td><td>0.2%</td><td>0.9%</td><td>5.0%</td><td>4.8%</td><td>0.3%</td></tr><tr><td>Brand Group Progressive</td><td>3.6%</td><td>3.6%</td><td>4.5%</td><td>-0.1%</td><td>-1.0%</td><td>-0.9%</td><td>5.3%</td><td>5.7%</td><td>-0.4%</td></tr><tr><td>Brand Group Sport Luxury</td><td>8.9%</td><td>8.5%</td><td>7.9%</td><td>0.4%</td><td>1.0%</td><td>0.6%</td><td>6.3%</td><td>5.9%</td><td>0.3%</td></tr><tr><td>Brand Group Trucks</td><td>8.0%</td><td>7.1%</td><td>6.9%</td><td>0.8%</td><td>1.1%</td><td>0.2%</td><td>6.0%</td><td>5.9%</td><td>0.1%</td></tr><tr><td>VW Financial Services</td><td>5.1%</td><td>5.7%</td><td>5.5%</td><td>-0.6%</td><td>-0.4%</td><td>NA</td><td>5.7%</td><td>5.9%</td><td>NA</td></tr><tr><td>Other Segments</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Group</td><td>4.2%</td><td>5.0%</td><td>4.7%</td><td>-0.8%</td><td>-0.5%</td><td>0.2%</td><td>4.4%</td><td>4.4%</td><td>0.1%</td></tr><tr><td>Reported EPS (prefs)</td><td>2.56</td><td>4.75</td><td>4.70</td><td>-46.1%</td><td>-45.5%</td><td>1.2%</td><td>17.25</td><td>17.49</td><td>-1.4%</td></tr><tr><td>Auto Cash Flow Reported</td><td>1,172</td><td>-592</td><td>583</td><td>297.8%</td><td>101.0%</td><td>-201.6%</td><td>5,190</td><td>5,124</td><td>1.3%</td></tr><tr><td>Automotive Net Liquidity</td><td>32,750</td><td>31,025</td><td>31,624</td><td>5.6%</td><td>3.6%</td><td>-1.9%</td><td>34,815</td><td>34,590</td><td>0.6%</td></tr></table>

Source: Company data, GS Global Investment Research

## Valuation and Key risks

## Valuation & Key Risks

We value Volkswagen using a P/E-based approach, applying a target multiple of 4.0x (in line with our approach to its European mass-market peers) to our blended 27/28E EPS, to derive a 12-month price target of €89. We remain Neutral-rated on the stock.

## Upside risks:

■ Stronger improvement in European demand

■ Macro concerns, notably with respect to Europe, do not materialise

■ Accelerated BEV adoption and cost curve benefits

■ Corporate reorganisation

■ Tariff relief or regulatory easing

■ China performance stabilisation

\- Investors start to take a SoTP approach to valuing VW, thereby crediting the equity value of Porsche AG

## Downside risks:

■ Software and BEV production issues

■ New products less well-received than recent products

■ Supply-chain constraints

■ Commodity and energy prices

Geopolitics

China slowdown

■ Pricing pressure and increased competition

<table><tr><td>VOWG_p.DE</td><td>12m Price Target: €89.00</td><td colspan="2">Price: €72.94</td><td colspan="2">Upside: 22.0%</td></tr><tr><td rowspan="2">Neutral</td><td rowspan="2">GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11">Market cap: €36.8bn / $41.9bnEnterprise value:€53.3bn / $61.2bn3m ADTV: €82.9mn / $95.7mnGermanyEurope AutosM&amp;A Rank: 3Leases incl. in net debt &amp; EV?:Yes</td><td>Revenue (€ mn)</td><td>321,913.5</td><td>326,886.7</td><td>336,154.4</td><td>342,587.7</td></tr><tr><td>EBIT (€ mn)</td><td>8,868.0</td><td>14,493.7</td><td>17,121.6</td><td>19,408.3</td></tr><tr><td>EPS (€)</td><td>13.35</td><td>17.25</td><td>20.94</td><td>23.62</td></tr><tr><td>EV/EBITDA (X)</td><td>4.3</td><td>3.7</td><td>3.4</td><td>3.1</td></tr><tr><td>P/E (X)</td><td>7.2</td><td>4.2</td><td>3.5</td><td>3.1</td></tr><tr><td>Dividend yield (%)</td><td>5.5</td><td>7.1</td><td>8.4</td><td>9.5</td></tr><tr><td>FCF yield (%)</td><td>(12.1)</td><td>8.5</td><td>13.6</td><td>13.0</td></tr><tr><td>CROCI (%)</td><td>(0.5)</td><td>3.8</td><td>4.0</td><td>4.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(1.0)</td><td>(0.9)</td><td>(1.0)</td><td>(1.1)</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (€)</td><td>2.61</td><td>4.75</td><td>2.78</td><td>7.11</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 23 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Christian Frenes, Robert Triulzi, Monika Mengting Liu, CFA and Shivam Kotecha, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Christian Frenes GS International, Robert Triulzi GS International, Monika Mengting Liu, CFA GS International, Shivam Kotecha GS India SPL.

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

The rating(s) for Volkswagen is/are relative to the other companies in its/their coverage universe: Aston Martin Lagonda Global Holdings, BMW, Ferrari NV, Mercedes-Benz Group AG, Porsche AG, Renault, Stellantis NV, Volkswagen

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, "GS") and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Volkswagen (€239.00), Volkswagen (€72.94) and Volkswagen (€73.85)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Volkswagen (€239.00), Volkswagen (€72.94) and Volkswagen (€73.85)

GS had an investment banking services client relationship during the past 12 months with: Volkswagen (€239.00), Volkswagen (€72.94) and Volkswagen (€73.85)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Volkswagen (€239.00), Volkswagen (€72.94) and Volkswagen (€73.85)

GS had a non-securities services client relationship during the past 12 months with: Volkswagen (€239.00), Volkswagen (€72.94) and Volkswagen (€73.85)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/495e88bc663f0ea8827f5485f2cc5f788fe1bd42fb1712ba9b15f41c84379365.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Volkswagen (VOWG\_p.DE)

Date of report Target price (€) Closing price (€)

<table><tr><td>Date of report</td><td>target price (€)</td><td>Closing price (€)</td></tr><tr><td>15-Jul-26</td><td>89.00</td><td>74.40</td></tr><tr><td>20-Apr-26</td><td>97.00</td><td>90.48</td></tr><tr><td>24-Feb-26</td><td>99.00</td><td>101.60</td></tr><tr><td>23-Nov-25</td><td>106.00</td><td>94.72</td></tr><tr><td>18-Feb-25</td><td>101.00</td><td>100.30</td></tr><tr><td>14-Jan-25</td><td>98.00</td><td>91.88</td></tr><tr><td>16-Oct-24</td><td>114.00</td><td>91.24</td></tr><tr><td>02-Oct-24</td><td>116.00</td><td>92.84</td></tr><tr><td>30-Aug-24</td><td>127.00</td><td>96.18</td></tr><tr><td>12-Jul-24</td><td>143.00</td><td>108.55</td></tr><tr><td>22-Apr-24</td><td>140.00</td><td>121.30</td></tr><tr><td>19-Feb-24</td><td>146.00</td><td>119.98</td></tr><tr><td>16-Jan-24</td><td>139.00</td><td>111.28</td></tr><tr><td>17-Nov-23</td><td>137.00</td><td>108.84</td></tr><tr><td>18-Oct-23</td><td>147.00</td><td>107.62</td></tr><tr><td>18-Sep-23</td><td>145.00</td><td>107.44</td></tr><tr><td>16-Aug-23</td><td>146.00</td><td>115.10</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits 

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
