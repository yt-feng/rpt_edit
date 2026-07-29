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
# ASMPT (0522.HK): 3Q26 revenues to grow at +0% to +9% QoQ; 2Q26 beat; TCB to ride on AI infrastructure upcycle

ASMPT's 3Q26 revenue guidance for US\$630\~690mn (or HK\$4.9\~5.4bn) implies growth of +35% to +48% YoY/+0%\~+9% QoQ; the midpoint of US\$660mn (or HK\$5.2bn) is higher than our estimate of HK\$4.7bn and Visible Alpha consensus of HK\$4.7bn. Management is positive on TCB's market potential, and expects sales growth in the SEMI and SMT segments in 2026 driven by AI-related demand. Management highlighted that the company secured orders from leading IDM clients in 2Q26 and expects strong growth driven by AI development. 2Q26 revenue (+24% QoQ) was higher than management guidance, GSe and Visible Alpha Consensus; GM (42.4%) was higher than our expectations of 39.4% and the Street's 40.1%. The BB ratio was 1.43 in 2Q26, around the level of last quarter. Net income came in at HK\$335m (vs. GSe of HK\$362m/consensus of HK\$332m), slightly lower than our estimate and in line with Visible Alpha Consensus.

Exhibit 1: 3Q26 guidance

<table><tr><td></td><td>3Q26 Guidance</td><td>GS</td><td>Consensus</td></tr><tr><td>Revenue</td><td>US$630~690mn</td><td>4,729</td><td>4,743</td></tr><tr><td>Gross margin</td><td></td><td>40.9%</td><td>39.7%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

## 2Q26 results

■ Revenue higher than GSe/ consensus: Revenue came in at HK\$4.9bn (+24% QoQ, +52% YoY), higher than our/street (Visible Alpha) expectations of HK\$4.5bn, and above the mid-point of company guidance (HK\$4.2\~4.7bn).

Gross margin improved QoQ: GM was 42.4% (+292bps QoQ / +284bps YoY), higher than our / consensus estimates of 39.4%/ 40.1%. GM saw a QoQ increase in both the SMT and SEMI segments, supported by product mix and higher sales volume.

\- Operating profit higher than GSe/ consensus: Opex ratio of 26.5% (vs.33.4% in 2Q25 and 29.8% in 1Q26) was lower than our estimate of 28.6% and the Street estimate of 29.9%, thanks to expenses control. Operating profit of HK\$786mn (+104% QoQ) was 64%/ 71% higher than GSe/ consensus.

■ Net income lower than GSe/ in line with consensus: Net income was HK\$335mn, lower than GSe (HK\$362mn) and in-line with consensus (HK332mn).

Book-to-Bill ratio was 1.43 (vs. 1.43 last quarter and 1.11 in 1Q25). Group bookings were US\$904mn in 2Q26 (+24% QoQ, +87% YoY).

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Yifan Hu

+852-2978-0996 | yifan.hu@gs.com
GS (Asia) L.L.C.

Exhibit 2: 2Q26 results snapshot (Reported)

<table><tr><td>(HK$m)</td><td>2Q26Actual</td><td>2Q26GS</td><td>Diff</td><td>2Q26Con.</td><td>Diff</td><td>1Q26</td><td>QoQ</td><td>2Q25</td><td>YoY</td></tr><tr><td>Revenue</td><td>4,936</td><td>4,462</td><td>11%</td><td>4,508</td><td>9%</td><td>3,967</td><td>24%</td><td>3,244</td><td>52%</td></tr><tr><td>Gross profit</td><td>2,092</td><td>1,756</td><td>19%</td><td>1,808</td><td>16%</td><td>1,566</td><td>34%</td><td>1,283</td><td>63%</td></tr><tr><td>Operating income</td><td>786</td><td>479</td><td>64%</td><td>459</td><td>71%</td><td>385</td><td>104%</td><td>200</td><td>294%</td></tr><tr><td>Pre-tax profit</td><td>645</td><td>483</td><td>34%</td><td>527</td><td>23%</td><td>445</td><td>45%</td><td>132</td><td>388%</td></tr><tr><td>Net income</td><td>335</td><td>362</td><td>-7%</td><td>332</td><td>1%</td><td>254</td><td>32%</td><td>131</td><td>155%</td></tr><tr><td>EPS</td><td>0.80</td><td>0.87</td><td>-8%</td><td>0.78</td><td>3%</td><td>0.61</td><td>32%</td><td>0.31</td><td>158%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="2"></td><td colspan="2"></td><td colspan="2"></td></tr><tr><td>Gross margin</td><td>42.4%</td><td>39.4%</td><td></td><td>40.1%</td><td></td><td>39.5%</td><td></td><td>39.6%</td><td></td></tr><tr><td>Operating margin</td><td>15.9%</td><td>10.7%</td><td></td><td>10.2%</td><td></td><td>9.7%</td><td></td><td>6.2%</td><td></td></tr><tr><td>Net margin</td><td>6.8%</td><td>8.1%</td><td></td><td>7.4%</td><td></td><td>6.4%</td><td></td><td>4.0%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research, Bloomberg

## Price target methodology and risks - ASMPT

Valuation methodology: We are Neutral-rated on ASMPT with a 12-month target price of HK\$206, which is based on 29.5x 2030E discounted P/E (discounted back to 2027E). Our target P/E is derived from correlation between peers P/E to the sum of NI YoY and OPM.

Key upside/downside risks: 1) customers' faster-/slower-than-expected adoption of Advanced Packaging tools; 2) stronger-/weaker-than-expected demand from automotive customers; and 3) stronger-/weaker-than-expected demand for traditional IC packaging and SMT equipment.

<table><tr><td>0522.HK</td><td colspan="2">12m Price Target: HK$206.00</td><td colspan="2">Price: HK$139.50</td><td colspan="2">Upside: 47.7%</td></tr><tr><td colspan="2">Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11" colspan="2">Market cap: HK$57.5bn / $7.3bn Enterprise value: HK$55.2bn / $7.0bn 3m ADTV: HK$844.0mn / $107.7mn China Greater China Technology M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: No</td><td>Revenue (HK$ mn)</td><td>14,146.5</td><td>18,151.1</td><td>22,356.3</td><td>25,764.4</td></tr><tr><td>EBITDA (HK$ mn)</td><td>1,183.7</td><td>2,616.8</td><td>3,814.9</td><td>4,482.4</td></tr><tr><td>EPS (HK$)</td><td>2.17</td><td>3.55</td><td>5.75</td><td>6.89</td></tr><tr><td>P/E (X)</td><td>31.2</td><td>39.3</td><td>24.3</td><td>20.2</td></tr><tr><td>P/B (X)</td><td>1.7</td><td>3.3</td><td>3.2</td><td>3.0</td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>1.7</td><td>2.7</td><td>3.2</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>(1.9)</td><td>(0.9)</td><td>(0.7)</td><td>(0.7)</td></tr><tr><td>CROCI (%)</td><td>3.0</td><td>11.1</td><td>14.5</td><td>15.8</td></tr><tr><td>FCF yield (%)</td><td>(0.5)</td><td>1.2</td><td>2.0</td><td>3.5</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (HK$)</td><td>0.61</td><td>0.87</td><td>0.96</td><td>1.11</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 28 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Yifan Hu GS (Asia) L.L.C..

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

The rating(s) for ASMPT is/are relative to the other companies in its/their coverage universe: AAC, ACM Research, AMEC, ASMPT, AVC, AccoTest, Anji Micro, Asus, Auras, BOE, BYDE, Biren, CR Micro, Cambricon, Chenbro, China Mobile (HK), China Telecom, China Tower Corp., China Unicom, Chinasoft Intl, Compal, Desay SV, E Ink, E-Town Semis, EHang, Empyrean, Eoptolink, FOCI, Fositek, Foxconn Industrial Internet, Gigabyte, Gigadevice, Glodon Co., HTC Corp., Hikvision, Hon Hai, Horizon Robotics, Hua Hong, Huace Navigation, Huaqin Co.(A), Huaqin Co.(H), Hwatsing, Iluvatar, InnoScience, Inspur, Insta360, Inventec, JCET, Kematek, King Slide, Kingdee, Kingsoft Office, LandMark, Largan, Lenovo, Lingyi, Maxscend, Meitu, MetaX, Mitac, Montage (A), Montage (H), NAURA, NSIG, Nexchip, OmniVision, Pegatron, Pony AI Inc. (ADR), Pony AI Inc. (H), Quanta, RoboTechnik, Ruijie Networks, SG Micro, SICC, SMIC (A), SMIC (H), SZS, Sangfor, SenseTime, Shengyi Tech, Shennan Circuits, StarPower, Sunny Optical, TFC Optical, Thundersoft, Tongyu Communication, Transsion, UMT, UNIS, VPEC, Vanchip, VeriSilicon, Victory Giant, WNC, WUS, WeRide, Wistron, Wiwynn, YJ Semitech, YOFC, Yonyou, ZTE (A), ZTE (H), iFlytek

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: ASMPT (HK\$139.50)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/6cb924863f99322c12f2bc5aef64a96b60695d4e72e219857ccdc350f6dd37d2.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) ASMPT (0522.HK)

<table><tr><td>Date of report</td><td>Target price (HK$)</td><td>Closing price (HK$)</td></tr><tr><td>13-Jul-26</td><td>206.00</td><td>185.40</td></tr><tr><td>22-Apr-26</td><td>118.30</td><td>152.20</td></tr><tr><td>05-Mar-26</td><td>103.90</td><td>112.40</td></tr><tr><td>30-Jan-26</td><td>90.70</td><td>103.90</td></tr><tr><td>02-Oct-25</td><td>79.00</td><td>85.00</td></tr><tr><td>23-Jul-25</td><td>69.00</td><td>63.20</td></tr><tr><td>01-May-25</td><td>60.20</td><td>52.20</td></tr><tr><td>06-Apr-25</td><td>61.00</td><td>53.65</td></tr><tr><td>11-Mar-25</td><td>65.00</td><td>58.25</td></tr><tr><td>26-Feb-25</td><td>86.00</td><td>64.05</td></tr><tr><td>01-Jan-25</td><td>100.00</td><td>74.90</td></tr><tr><td>01-Nov-24</td><td>108.00</td><td>83.75</td></tr><tr><td>25-Jul-24</td><td>117.00</td><td>78.70</td></tr><tr><td>24-Apr-24</td><td>136.12</td><td>102.30</td></tr><tr><td>12-Mar-24</td><td>124.01</td><td>108.30</td></tr><tr><td>29-Feb-24</td><td>109.16</td><td>95.95</td></tr><tr><td>12-Feb-24</td><td>109.16</td><td>85.70</td></tr><tr><td>03-Dec-23</td><td>105.00</td><td>79.05</td></tr><tr><td>21-Sep-23</td><td>94.00</td><td>66.85</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client's objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client's own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS' Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for informa

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
