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
# Japan Technology: Hardware - Industrial Electronics: GLW 2Q: DC demand strong; valuation gap with Japanese peers to narrow

Corning (Not Covered) held its 2QFY26 results briefing on July 28 (from 21:30 JST). 2Q companywide core sales were US\$4,738 mn (Bloomberg consensus: US\$4,644 mn), and core EPS was US\$0.78 (vs. US\$0.76). In the Optical Communications segment, which supplies optical fiber/cables, 2Q sales of US\$2,072 mn (vs. BBG consensus of US\$2,011 mn) and segment profits of US\$438 mn (vs. consensus of US\$403 mn) both beat expectations. In 2Q, while Enterprise Network sales were up 65% yoy, Carrier Networks sales were up just 1% yoy and down 9% qoq due to timing shifts in customer projects. However, Corning commented that it expects continued solid demand, supported by data center interconnect (DCI) and FTTH demand. The company also said its view on demand for photonics such as CPO/NPO, and scale-up demand, such as in-rack optical interconnects for AI servers, has not changed significantly since its Investor Day in May.

Ryo Harada
+81(3)4587-9865 | ryo.harada@gs.com
GS Japan Co., Ltd.

Hiroki Muramatsu  
+81(3)4587-9872 |  
hiroki.muramatsu@gs.com  
GS Japan Co., Ltd.

As of 10:48 AM local time, Corning's stock was trading down $19\%$ from the previous day. While its data center optics-related business is strong, we think the share price decline owes to the Solar business falling into the red in 2Q on one-off expenses and weak 3Q sales guidance.

Near-term sentiment on AI-related stocks warrants caution as they have recently tended to fall despite strong results. However, forward P/E multiples (LSEG basis) are down to 26X for Fujikura, 19X for Sumitomo Electric, and 22X for Furukawa Electric, versus 41X for Corning, and as such we look for eventual re-ratings for these coverage names. In addition, while we have heard concerns from market participants about competition with Chinese manufacturers, this is precisely why Japanese manufacturers have refrained from capacity expansion investments in commodity areas like optical fiber (where oversupply has previously been an issue) and instead focused on high-value-added cables and other products. We believe that once the market calms down, the time will come when these management decisions will be recognized.

## Key takeaways from Corning's results briefing

The following summarizes company commentary on the Optical Communications segment.

■ 2Q sales: US\$2,072 mn (Bloomberg consensus: US\$2,011 mn), up 32% yoy.

■ 2Q segment profits: US\$438 mn (vs. consensus of US\$403 mn), up 77% yoy.

2Q sales for the Enterprise Network subsegment were US\$1,269 mn (vs. consensus of US\$1,057 mn), up 65% yoy, while sales for the Carrier Network subsegment were US\$803 mn (vs. consensus of US\$939 mn), up 1% yoy.

In Enterprise Networks, AI data center-related demand nearly doubled yoy. The company said generative AI-related demand is strong and that orders are accelerating further.

Carrier Networks sales were down 9% qoq, but this was due to timing shifts in customer projects; for 1H26, sales were solid, up 17% yoy. The company said it expects mid-single-digit sales growth in the long term, driven by strong demand from data center interconnect (DCI) and fiber-to-the-home (FTTH).

According to Corning, its major capacity expansion initiatives are based on long-term contracts with customers, proceeding with an appropriate sharing of investment risk and return. It indicated that it expects the number of long-term contracts to increase in the future.

Regarding business opportunities in Photonics and Scale-up, the company said there has been no significant change in its view from the May Investor Day, and that it is preparing to capture demand related to the optical transition of next-generation scale-up networks.

## Price Target Risks and Methodology - Fujikura

We are Buy rated. Our 12-month price target of ¥7,500 is based on an EV/EBITDA of 25.0X (FY3/28E; multiple based on the EV/EBITDA and EBITDA margin correlation across its domestic and global competitors). Downside risks: Telecommunications: A delay in benefits from hyperscaler investment, a prolonged restraint in telecom carrier investment, and competitors in ultra-high-density optical fiber cables catching up with Fujikura. Electronics: A greater-than-expected slowdown in the smartphone market and/or more intense competition. Automotive products: Automobile production volume undershooting our assumptions. Companywide: Forex swings.

## Price Target Risks and Methodology - Furukawa Electric

Our 12-month target price is ¥7,200. We apply an EV/EBITDA multiple of 25.0X (FY3/28E, based on the correlation between EV/EBITDA and EBITDA growth rate for domestic and overseas competitors). We are Buy rated. Risks: Communications solutions: If sales expansion of high-margin optical products for data centers does not proceed as expected and there is no improvement in profits. If the profitability of the acquired Furukawa FITEL Optical Components (FFOC) deteriorates again due to factors such as changes in competitiveness. If generative AI data center investment slows for reasons such as delays in data center construction due to supply shortages of some essential products, or if investment in generative AI data centers starts to wane as project profitability deteriorates due to price hikes for component products. Energy infrastructure: If demand for both high-voltage and medium/low-voltage cables slows due to factors such as a slowdown in generative AI investment. If the company decides on capex for HVDC cables but fails to secure the expected orders from customers. Electronics & automotive systems: If auto production volume or sales of models supplied by the company do not grow as much as expected. If fluctuations in auto production volume are larger than expected and the company is unable to absorb fixed costs through measures such as price revisions. If material prices surge more than expected and the company is unable to pass these on to customers. Functional products: If, in the copper foil business, sales expansion of high-function circuit foils does not proceed as planned and profitability improvement is not expected, if orders for thermal products for generative AI are not booked as sales for some reason or are delayed, or if the acquisition of new customers for semiconductor manufacturing tape does not progress as expected.

## Price Target Risks and Methodology - Sumitomo Electric Industries

We are Buy rated. Our 12-month target price is ¥3,400. We apply a target EV/EBITDA multiple of 13.0X (based on FY3/28E, using an SOTP approach). Key downside risks: Automotive segment: Decline in automobile production volume; slower-than-expected pass-through of material procurement costs to selling prices. Infocommunications segment: Longer-than-expected inventory adjustments due to a slowdown in hyperscaler capex; catch-up by competitors in ultra-high density optical fiber cables. Environment & energy segment: Delays in new and replacement power infrastructure projects due to difficulties in procuring materials and securing workers; slower-than-expected earnings contributions from the Japanese government's clean energy strategy. Industrial materials and other segments: Slowdown in demand for cemented carbide tools, etc., due to a macroeconomic slowdown; increase in manufacturing costs for sintered parts, etc., due to rising energy prices. Company-wide: FX fluctuations; sustained high material prices.

## Price Target Risks and Methodology - SWCC

Valuation methodology: We have a Buy rating. Our 12-month target price of ¥16,200 is based on an EV/EBITDA of 11.5X (FY3/28E, multiple based on the correlation between EV/EBITDA and EBITDA margin for global competitors).

Key downside risks: Energy & infrastructure segment: The balancing out of supply and demand for wires/cables and power equipment in Japan, resulting in lower selling prices; a lack of progress with the further leveling of construction work and improvement of personnel allocation efficiency, resulting in slower-than-expected profit margin improvement; an influx of foreign workers significantly alleviating the shortage of construction workers in Japan. Communication & components segment: Sharp declines in optical fiber cable selling prices due to a large supply of inexpensive products from China, India, and other countries, and profitability deteriorating as a result; home appliance sales in China and Japan falling short of expectations; acceleration in the trend toward a paperless society, resulting in a steeper-than-expected decline in sales of printer rollers. A slower-than-expected shift to EVs by the company's customers, leading to lower demand; significant declines in automobile production volume, including EVs; increases in prices of materials such as copper, with the company unable to pass these increases on to customers. Company-wide: The implementation of large-scale growth investments aimed at furthering overseas expansion in the electronic equipment & components and communication & industrial devices segments, with returns on these investments falling short of expectations and significantly impacting company-wide margins; yen appreciation.

## Price Target Risks and Methodology - Anritsu

Our 12-month target price is ¥5,300, based on a target EV/EBITDA multiple of 17X on

FY3/28E (our target multiple is based on the correlation between EV/EBITDA and EBITDA margin for global competitors). We are Buy rated.

Risks: Test and Measurement: Demand for 5G applications has already cooled, and there is a risk that sales may not grow as expected, leading to a deterioration in profit margins. For the data center business, uncertainty due to US tariffs could lead to slower decision-making by customers, resulting in stagnating or weaker demand. Testing methods may change from $100\%$ testing to sampling testing. PQA: Possible decline in domestic market share, or the failure of sales expansion to proceed as expected in regions where the company is accelerating business development, such as North America, Europe, and China. Environmental Measurement: The possibility that earnings in battery test equipment fail to grow as expected due to a slowdown in the BEV market. Company-wide: Disappointing returns from M&A and/or growth investment. An increase in the R&D expense ratio. Yen appreciation.

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

The rating(s) for Anritsu, Fujikura, Furukawa Electric, SWCC and Sumitomo Electric Industries is/are relative to the other companies in its/their coverage universe: Anritsu, Daihen, Fuji Electric Co., Fujikura, Furukawa Electric, Hitachi, Meidensha, Mitsubishi Electric, Panasonic Holdings, SWCC, Sumitomo Electric Industries

## Company-specific regulatory disclosures

Compendium report: please see disclosures at https://www.gs.com/research/hedge.html. Disclosures applicable to the companies included in this compendium can be found in the latest relevant published research

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

Compendium report: please see disclosures at https://www.gs.com/research/hedge.html. Disclosures applicable to the companies included in this compendium can be found in the latest relevant published research

Target price history table(s)  
Sumitomo Electric Industries (5802.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>07-Jul-26</td><td>3,400</td><td>2,443</td></tr><tr><td>12-May-26</td><td>12,500</td><td>2,913</td></tr><tr><td>20-Apr-26</td><td>11,500</td><td>2,494</td></tr><tr><td>13-Mar-26</td><td>12,300</td><td>2,598</td></tr><tr><td>03-Feb-26</td><td>8,700</td><td>1,914</td></tr><tr><td>05-Jan-26</td><td>7,350</td><td>1,678</td></tr><tr><td>31-Oct-25</td><td>6,700</td><td>1,413</td></tr><tr><td>09-Oct-25</td><td>5,500</td><td>1,158</td></tr><tr><td>10-Sep-25</td><td>5,000</td><td>1,073</td></tr><tr><td>31-Jul-25</td><td>4,500</td><td>940</td></tr><tr><td>07-Jul-25</td><td>4,300</td><td>756</td></tr><tr><td>13-May-25</td><td>2,800</td><td>658</td></tr><tr><td>16-Apr-25</td><td>2,500</td><td>516</td></tr><tr><td>04-Feb-25</td><td>3,150</td><td>752</td></tr><tr><td>22-Jan-25</td><td>2,900</td><td>727</td></tr><tr><td>01-Nov-24</td><td>2,670</td><td>583</td></tr><tr><td>07-Oct-24</td><td>2,630</td><td>606</td></tr><tr><td>07-Aug-24</td><td>2,650</td><td>530</td></tr><tr><td>18-Jul-24</td><td>2,700</td><td>600</td></tr><tr><td>09-Apr-24</td><td>2,600</td><td>602</td></tr><tr><td>12-Mar-24</td><td>2,400</td><td>556</td></tr><tr><td>05-Feb-24</td><td>2,150</td><td>501</td></tr><tr><td>19-Dec-23</td><td>1,900</td><td>443</td></tr><tr><td>02-Nov-23</td><td>1,850</td><td>404</td></tr><tr><td>02-Aug-23</td><td>1,800</td><td>469</td></tr></table>

<table><tr><td colspan="3">Fujikura (5803.T)</td></tr><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>07-Jul-26</td><td>7,500</td><td>5,072</td></tr><tr><td>18-Jun-26</td><td>7,600</td><td>4,461</td></tr><tr><td>14-May-26</td><td>7,100</td><td>6,355</td></tr><tr><td>20-Apr-26</td><td>7,000</td><td>5,529</td></tr><tr><td>13-Mar-26</td><td>31,000</td><td>4,420</td></tr><tr><td>09-Feb-26</td><td>27,000</td><td>3,659</td></tr><tr><td>05-Jan-26</td><td>23,400</td><td>3,074</td></tr><tr><td>07-Nov-25</td><td>22,700</td><td>3,403</td></tr><tr><td>09-Oct-25</td><td>18,800</td><td>2,798</td></tr><tr><td>10-Sep-25</td><td>15,200</td><td>2,272</td></tr><tr><td>07-Aug-25</td><td>13,000</td><td>1,918</td></tr><tr><td>07-Jul-25</td><td>9,400</td><td>1,235</td></tr><tr><td>13-May-25</td><td>6,600</td><td>957</td></tr><tr><td>16-Apr-25</td><td>6,700</td><td>761</td></tr><tr><td>10-Feb-25</td><

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
