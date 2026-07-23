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
# Texas Instruments Inc. (TXN): Strong results and guidance suggests continued momentum in the analog recovery

Key stock takeaways: We expect the stock to be range bound following a quarter and guidance that came in above the Street. We believe expectations were somewhat elevated given management's intra-quarter commentary on a fundamental recovery and the stock's outperformance over the past quarter, and based on our conversations we believe results were consistent with these expectations. We see the strong recovery in the industrial end market, as well as the beginning of broadening automotive demand improvement, as a particularly encouraging read-across for the sector. Although we continue to see a recovery across the analog sector (including for TI), we believe peers have managed their inventory levels more proactively — and hence we believe gross margins are likely to recover faster for peers (along with significant upward earnings revisions) than for TI. We continue to have a preference for peers (including Microchip and NXP) who are likely to see greater upward earnings revisions in the near term, and we retain our relative Sell rating on TXN given the ongoing gross margin headwinds we expect in the coming quarters.

Read-through to our coverage: We expect a positive initial reaction for the analog group, with the most direct read-across for NXPI (Buy), ON (Neutral), and ADI (Buy) given their relatively high automotive exposures following the incrementally positive commentary around this end market.

Quarterly revenue and EPS are above the Street: TI reported 2Q26 revenue of \$5.46 bn, above GS at \$5.38 bn and the Street (Visible Alpha) at \$5.26 bn. Gross margin of 61.4% was well above GS at 59.4% and the Street at 59.5%. Operating margin of 42.3% was well above GS at 40.9% and the Street at 40.5%. EPS of \$2.14 was above GS at \$1.99 and the Street at \$1.94.

End market trends: TI's 1Q26 industrial revenue increase of about $10\%$ QoQ was ahead of our expectations - and the company's 3Q revenue guidance of up $\sim 8\%$ QoQ (at the midpoint) suggests a continued cyclical recovery across the supply chain. The company noted that it continues to see the market continuing to improve, with demand broadening to areas such as automotive. Automotive was up in the high-single digits QoQ, personal electronics was up high-single digits QoQ, communications equipment was up QoQ, and datacenter revenue was up $20\%$ QoQ in 2Q.

\- Inventory levels: Inventory on the balance sheet was lower (down \~\$90mn) on a sequential basis to \$4.6bn and inventory days ticked 13 days lower to 196, which

James Schneider, Ph.D.  
+1(212)357-2929 | jim.schneider@gs.com GS & Co. LLC

Khalil Fenina
+1(212)357-6392 |
khalil.fenina@gs.com
GS & Co. LLC

Anmol Makkar
+1(212)357-1366 |
anmol.makkar@gs.com
GS & Co. LLC

Luya You
+1(212)902-5297 | luya.you@gs.com
GS & Co. LLC

we view as encouraging. Management intends to manage its factory loadings dynamically in order to manage internal inventory levels according to customer demand. Although we see this trend as a positive for the company's gross margins over time, we expect TI's gross margin expansion to lag peers as the recovery continues.

\- Margins: TI's implied 2Q gross margin guidance is for gradual expansion QoQ as the company manages its factory loadings to end demand, which implies gross margins up by \~100bp in 3Q (we model for 3Q26 GM of 62.4% vs. 61.4% in 2Q26)— and we expect this trend to largely continue over the course of 2026.

3Q revenue and EPS guidance are above the Street. TI guided 3Q above the Street on revenue and EPS. Revenue was guided to \$5.90 bn at the midpoint, which is above GS at \$5.65 bn and the Street at \$5.63 bn. OpEx is expected to be roughly flat QoQ in 3Q. TI's tax rate is expected to be \~13%. EPS guidance of \$2.40 at the midpoint is well above both GS at \$2.14 and the Street at \$2.18.

Estimate changes. We increase our 2025-2027 EPS estimates by an average of $9\%$ to mainly reflect higher revenue and gross margins than we had previously modeled (see detailed estimates below — Exhibit 3).

Price target. We raise our 12-month price target to \$225 (from \$200 previously) is based on a 25X P/E multiple (unchanged) applied to our normalized EPS estimate of \$9.00 (from \$8.00 previously on higher estimates). Key upside risks: 1) upside to end-demand across key verticals; 2) a reversal in market share dynamics; 3) better-than-expected gross margin performance and/or OpEx leverage.

We are Sell rated on TXN. Our Sell rating on TXN is driven by our view that its margin expansion is likely to under-run peers (such as Microchip and NXP) during the ongoing analog recovery given TI's significantly higher inventory levels.

Exhibit 1: TXN - Variance summary

<table><tr><td rowspan="2">Financials ($ mn, except EPS)</td><td colspan="5">2Q26</td></tr><tr><td>Actual</td><td>GS</td><td>Street</td><td>Actual/GS</td><td>Actual/Street</td></tr><tr><td>Revenue</td><td>5,463</td><td>5,380</td><td>5,262</td><td>1.5%</td><td>3.8%</td></tr><tr><td>QoQ</td><td>13.2%</td><td>11.5%</td><td>9.0%</td><td></td><td></td></tr><tr><td>YoY</td><td>22.8%</td><td>21.0%</td><td>18.3%</td><td></td><td></td></tr><tr><td>Gross Margin</td><td>61.4%</td><td>59.4%</td><td>59.5%</td><td>+197 bps</td><td>+183 bps</td></tr><tr><td>Operating Income</td><td>2,310</td><td>2202</td><td>2,128</td><td>4.9%</td><td>8.5%</td></tr><tr><td>Operating Margin</td><td>42.3%</td><td>40.9%</td><td>40.5%</td><td>+136 bps</td><td>+183 bps</td></tr><tr><td>EPS - GAAP</td><td>$2.14</td><td>$1.99</td><td>$1.94</td><td>7.8%</td><td>10.4%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

Exhibit 2: TXN - Guidance summary

<table><tr><td rowspan="2">Financials ($ mn, except EPS)</td><td colspan="7">3Q26</td></tr><tr><td>High</td><td>Low</td><td>Guidance (midpoint)</td><td>GS</td><td>Street</td><td>Guidance/GS</td><td>Guidance/Street</td></tr><tr><td>Revenue</td><td>6,150</td><td>5,650</td><td>5,900</td><td>5,649</td><td>5,626</td><td>4.4%</td><td>4.9%</td></tr><tr><td>QoQ</td><td>12.6%</td><td>3.4%</td><td>8.0%</td><td>5.0%</td><td>6.9%</td><td></td><td></td></tr><tr><td>YoY</td><td>29.7%</td><td>19.1%</td><td>32.6%</td><td>19.1%</td><td>18.6%</td><td></td><td></td></tr><tr><td>EPS - GAAP</td><td>$2.57</td><td>$2.23</td><td>$2.40</td><td>$2.14</td><td>$2.18</td><td>12.1%</td><td>10.0%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

Exhibit 3: TXN - New vs. old estimates

<table><tr><td rowspan="2">Financials ($mn, except EPS and FCF/Share)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>GS</td><td>Old</td><td>Δ</td><td>GS</td><td>Old</td><td>Δ</td><td>GS</td><td>Old</td><td>Δ</td></tr><tr><td>Revenue</td><td>22,167</td><td>21,277</td><td>+4.2%</td><td>25,068</td><td>23,638</td><td>+6.0%</td><td>26,344</td><td>25,000</td><td>+5.4%</td></tr><tr><td>YoY</td><td>25.4%</td><td></td><td></td><td>13.1%</td><td></td><td></td><td>5.1%</td><td></td><td></td></tr><tr><td>Gross Margin</td><td>60.9%</td><td>59.0%</td><td>+192 bps</td><td>61.8%</td><td>59.8%</td><td>+202 bps</td><td>61.4%</td><td>60.5%</td><td>+83 bps</td></tr><tr><td>Operating Income</td><td>9,409</td><td>8,544</td><td>+10.1%</td><td>10,964</td><td>9,730</td><td>+12.7%</td><td>11,234</td><td>10,439</td><td>+7.6%</td></tr><tr><td>EPS - GAAP</td><td>$8.60</td><td>$7.75</td><td>+11.0%</td><td>$10.20</td><td>$9.20</td><td>+11.0%</td><td>$10.50</td><td>$10.00</td><td>+5.0%</td></tr><tr><td>FCF/Share</td><td>$8.19</td><td>$7.82</td><td>+4.8%</td><td>$10.06</td><td>$10.30</td><td>-2.3%</td><td>$11.18</td><td>$11.59</td><td>-3.6%</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 4: Price target

<table><tr><td colspan="5">PRICE TARGET AND RISK/REWARD SUMMARY</td></tr><tr><td>Method</td><td>Metric</td><td>Base</td><td>Bull</td><td>Bear</td></tr><tr><td rowspan="4">P/E Method</td><td>Normalized EPS Estimate</td><td>$9.00</td><td>$9.90</td><td>$7.65</td></tr><tr><td>Multiple</td><td>25.0x</td><td>30.0x</td><td>22.0x</td></tr><tr><td>Valuation</td><td>$225.00</td><td>$297.00</td><td>$168.00</td></tr><tr><td>Upside/Downside</td><td>-21.1%</td><td>4.2%</td><td>-41.1%</td></tr><tr><td rowspan="4">Price Target</td><td>12-Month Price Target</td><td>$225.00</td><td></td><td></td></tr><tr><td>Potential Upside/Downside</td><td>-21.1%</td><td colspan="2">100% P/E</td></tr><tr><td>Dividend Yield at Current Price</td><td>0.5%</td><td></td><td></td></tr><tr><td>Potential Total Return</td><td>-20.6%</td><td></td><td></td></tr></table>

Source: GS Global Investment Research

<table><tr><td>TXN</td><td colspan="2">12m Price Target: $225.00</td><td colspan="2">Price: $294.19</td><td colspan="2">Downside: 23.5%</td></tr><tr><td colspan="2">Sell</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11" colspan="2">Market cap: $267.1bnEnterprise value: $273.4bn3m ADTV: $2.7bnUnited StatesAmericas Semiconductors &amp; IT ServicesM&amp;A Rank: 3</td><td>Revenue ($ mn) New</td><td>17,682.0</td><td>22,167.2</td><td>25,068.3</td><td>26,343.7</td></tr><tr><td>Revenue ($ mn) Old</td><td>17,682.0</td><td>21,276.7</td><td>23,638.3</td><td>24,999.7</td></tr><tr><td>EBITDA ($ mn)</td><td>7,941.0</td><td>11,651.5</td><td>13,512.0</td><td>14,101.7</td></tr><tr><td>EBIT ($ mn)</td><td>6,023.0</td><td>9,338.5</td><td>10,884.0</td><td>11,153.7</td></tr><tr><td>EPS ($) New</td><td>5.45</td><td>8.60</td><td>10.20</td><td>10.50</td></tr><tr><td>EPS ($) Old</td><td>5.45</td><td>7.75</td><td>9.20</td><td>10.00</td></tr><tr><td>P/E (X)</td><td>33.6</td><td>34.2</td><td>28.8</td><td>28.0</td></tr><tr><td>Dividend yield (%)</td><td>3.0</td><td>2.0</td><td>2.1</td><td>2.2</td></tr><tr><td>Net debt/EBITDA (X)</td><td>1.2</td><td>0.5</td><td>0.3</td><td>0.2</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS ($)</td><td>2.14</td><td>2.51</td><td>2.27</td><td>2.36</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 22 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, James Schneider, Ph.D., Khalil Fenina, Anmol Makkar and Luya You, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: James Schneider, Ph.D. GS & Co. LLC, Khalil Fenina GS & Co. LLC, Anmol Makkar GS & Co. LLC, Luya You GS & Co. LLC.

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

## Rating and pricing information

Analog Devices Inc. (Buy, \$386.73), Microchip Technology Inc. (Buy, \$85.02), NXP Semiconductors NV (Buy, \$278.80), and Onsemi (Neutral, \$92.33).

## Financial advisory disclosure

GS and/or one of its affiliates is acting as a financial advisor in connection with an announced strategic matter involving the following company or one of its affiliates: Texas Instruments Incorporated

Advanced Micro Devices Inc., Amkor Technology Inc., Analog Devices Inc., Applied Materials Inc., Broadcom Inc., Cadence Design Systems Inc., Camtek, Cognizant Technology Solutions, Credo Technology Group, EPAM Systems Inc., Entegris Inc., GlobalFoundries Inc., Globant SA, Intel Corp., International Business Machines Corp., KLA Corp., Lam Research Corp., MKS Instruments Inc., Marvell Technology Inc., Microchip Technology Inc., Micron Technology Inc., NXP Semiconductors NV, Nvidia Corp., ON Semiconductor Corp., Qnity, Qualcomm Inc., SanDisk Corp., Seagate Technology, SiTime Corp., Synopsys Inc., TaskUs Inc., Teradyne Inc., Texas Instruments Inc., Western Digital Corp.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Texas Instruments Inc. (\$294.19)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Texas Instruments Inc. (\$294.19)

GS has received compensation for non-investment banking services during the past 12 months: Texas Instruments Inc. (\$294.19)

GS had an investment banking services client relationship during the past 12 months with: Texas Instruments Inc. (\$294.19)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Texas Instruments Inc. (\$294.19)

GS had a non-securities services client relationship during the past 12 months with: Texas Instruments Inc. (\$294.19)

GS makes a market in the securities or derivatives thereof: Texas Instruments Inc. (\$294.19)

Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/ec37275d7127c0ff630b2c1cf370c543808335318845b106bff07ecf30feb71f.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Texas Instruments Inc. (TXN)

Date of report Target price (\$) Closing price (\$)

<table><tr><td>23-Apr-26</td><td>200.00</td><td>282.23</td></tr><tr><td>28-Jan-26</td><td>175.00</td><td>216.17</td></tr><tr><td>15-Dec-25</td><td>156.00</td><td>177.97</td></tr><tr><td>21-Oct-25</td><td>200.00</td><td>180.84</td></tr><tr><td>23-Jul-25</td><td>230.00</td><td>186.25</td></tr><tr><td>10-Jul-25</td><td>255.00</td><td>219.66</td></tr><tr><td>24-Jan-25</td><td>186.00</td><td>185.52</td></tr><tr><td>23-Oct-24</td><td>190.00</td>

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
