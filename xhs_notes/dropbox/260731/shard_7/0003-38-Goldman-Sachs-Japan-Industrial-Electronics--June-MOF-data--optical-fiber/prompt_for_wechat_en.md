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
# Japan Industrial Electronics: June MOF data (optical fiber/cable): Sharp growth in optical fiber/cable export value; fundamentals favorable

Era of Optics: Innovation behind AI
Insights into optical product technology and trends
Explore >

![](images/0c5ae8e3ca62469768ba703a9e9817c4f0b4250d33e8d208076848e2163f325d.jpg)

Ryo Harada
+81(3)4587-9865 | ryo.harada@gs.com
GS Japan Co., Ltd.

Hiroki Muramatsu
+81(3)4587-9872 |
hiroki.muramatsu@gs.com
GS Japan Co., Ltd.

According to Ministry of Finance (MOF) trade statistics for June (released on July 30), export value was +129% yoy for optical fiber cable and +56% yoy for optical fiber (including some other optical fiber cables). The ASP for optical fiber grew +55% yoy. As seen in Corning's results on July 28, fundamentals for the optical industry appear favorable. Against this backdrop, a valuation gap continues to exist for Japanese optical-related companies on a forward P/E (LSEG) basis, with Fujikura at 24X, Sumitomo Electric Industries at 18X, and Furukawa Electric at 20X, versus Corning at 32X, and we look for this gap to narrow.

Heading into 1Q results, we focus in particular on Sumitomo Electric, which we think has significant room for an upward revision to guidance for its infocommunications business. For Fujikura, which announced an upward revision on June 19, we see limited room for further revisions, but there is potential for a positive forex impact given the recent yen weakness. Its 2H guidance also still looks conservative. For Furukawa Electric, we think 2H earnings are more likely to be a catalyst, as water-cooled cold plates, the biggest driver, will contribute from 2H. In the near term, some investors are citing the possibility of some form of equity financing for large-scale investments as a concern (link). For Anritsu, a manufacturer of optical transceiver test equipment, we expect strong earnings as demand related to 800 G/1.6 T is also strong.

By destination (Exhibit 7), ASPs for exports of both optical fiber and optical fiber cable to the US increased yoy and qoq. By customs jurisdiction (Exhibit 9), the value of optical fiber cable was up yoy at Tokyo, Yokohama, and Nagoya, suggesting the possibility that exports from the three major cable manufacturers are increasing. The main manufacturing bases of the three major cable companies in our coverage are Fujikura: Chiba (Tokyo customs jurisdiction), Sumitomo Electric: Yokohama (Yokohama customs jurisdiction), and Furukawa Electric: Mie (Nagoya customs jurisdiction).

Exhibit 1: Export value for optical fiber cable (¥ mn)  
![](images/c9f909f503e52dc38af915d92c2deb6ce1c0211759123dbc76aec53b06960d6e.jpg)  
Source: Ministry of Finance

Exhibit 2: Export value for optical fiber (¥ mn)  
![](images/2fa56dcefc9bede8b617034984fa9cb16d3b1418a3ff490486e6fd9386b9cc1a.jpg)  
Includes some other optical fiber cables.  
Source: Ministry of Finance

Exhibit 3: Export volume for optical fiber cable (kg)  
![](images/6088052ed01015d6db8db024376f3ce7ced1849726e91cebeb4b2b34b4525088.jpg)  
Source: Ministry of Finance

Exhibit 4: Export volume for optical fiber (kg)  
![](images/a213c3c5ae5f29e86a6c4745dd41481aedfc8cee0fe5c73874dbf8134fcca022.jpg)  
Includes some other optical fiber cables.  
Source: Ministry of Finance

Exhibit 5: Average export price for optical fiber cable (¥1,000/kg)  
![](images/ec104a544d62f404ab04ef71313487a26ddbf5412eda4d9bf83d3f5e3d7b9506.jpg)  
Source: Ministry of Finance

Exhibit 6: Average export price for optical fiber (¥1,000/kg)  
![](images/411cf8bd8034c39a9b7d8e69fcd198159273010bb507ede180b468dc21f29deb.jpg)  
Includes some other optical fiber cables.

Exhibit 7: Export value, volume and average export price (yoy, mom) for top 10 destinations (annual export basis)

<table><tr><td rowspan="2">Region</td><td rowspan="2">% in CY2025</td><td colspan="2">Value</td><td colspan="2">Volume</td><td colspan="2">ASP</td></tr><tr><td>YoY</td><td>MoM</td><td>YoY</td><td>MoM</td><td>YoY</td><td>MoM</td></tr><tr><td colspan="8">Optical Cable</td></tr><tr><td>US</td><td>58%</td><td>50%</td><td>95%</td><td>-16%</td><td>66%</td><td>78%</td><td>18%</td></tr><tr><td>Mexico</td><td>10%</td><td>293%</td><td>1030%</td><td>243%</td><td>435%</td><td>15%</td><td>111%</td></tr><tr><td>China</td><td>5%</td><td>54%</td><td>-20%</td><td>102%</td><td>30%</td><td>-24%</td><td>-38%</td></tr><tr><td>UK</td><td>4%</td><td>-83%</td><td>247%</td><td>-69%</td><td>359%</td><td>-46%</td><td>-24%</td></tr><tr><td>Poland</td><td>4%</td><td>-</td><td>-</td><td>-89%</td><td>-92%</td><td>-</td><td>-</td></tr><tr><td>Taiwan</td><td>3%</td><td>199%</td><td>129%</td><td>311%</td><td>11%</td><td>-27%</td><td>107%</td></tr><tr><td>Australia</td><td>3%</td><td>687%</td><td>186%</td><td>1870%</td><td>196%</td><td>-60%</td><td>-3%</td></tr><tr><td>Canada</td><td>2%</td><td>195%</td><td>190%</td><td>31%</td><td>136%</td><td>125%</td><td>23%</td></tr><tr><td>Philippines</td><td>1%</td><td>-</td><td>937231%</td><td>-</td><td>325171%</td><td>-</td><td>188%</td></tr><tr><td>Vietnam</td><td>1%</td><td>415%</td><td>387%</td><td>132%</td><td>268%</td><td>122%</td><td>33%</td></tr><tr><td>All regions</td><td>100%</td><td>129%</td><td>140%</td><td>168%</td><td>458%</td><td>-14%</td><td>-57%</td></tr><tr><td colspan="8">Optical Fiber</td></tr><tr><td>US</td><td>54%</td><td>109%</td><td>138%</td><td>21%</td><td>117%</td><td>72%</td><td>10%</td></tr><tr><td>Romania</td><td>13%</td><td>-56%</td><td>-21%</td><td>-62%</td><td>-5%</td><td>16%</td><td>-16%</td></tr><tr><td>China</td><td>9%</td><td>4%</td><td>-39%</td><td>-51%</td><td>-50%</td><td>112%</td><td>22%</td></tr><tr><td>Netherlands</td><td>3%</td><td>-100%</td><td>-100%</td><td>-100%</td><td>-100%</td><td>-</td><td>-</td></tr><tr><td>Sweden</td><td>3%</td><td>31%</td><td>-10%</td><td>-38%</td><td>-49%</td><td>112%</td><td>77%</td></tr><tr><td>Turkey</td><td>3%</td><td>637%</td><td>239%</td><td>132%</td><td>214%</td><td>218%</td><td>8%</td></tr><tr><td>France</td><td>2%</td><td>-69%</td><td>-21%</td><td>-60%</td><td>-12%</td><td>-24%</td><td>-10%</td></tr><tr><td>Taiwan</td><td>2%</td><td>226%</td><td>149%</td><td>111%</td><td>116%</td><td>55%</td><td>15%</td></tr><tr><td>UK</td><td>1%</td><td>19%</td><td>-29%</td><td>-48%</td><td>574%</td><td>127%</td><td>-90%</td></tr><tr><td>UAE</td><td>1%</td><td>-</td><td>30%</td><td>-</td><td>-11%</td><td>-</td><td>46%</td></tr><tr><td>All regions</td><td>100%</td><td>56%</td><td>26%</td><td>0%</td><td>51%</td><td>55%</td><td>-17%</td></tr></table>

% in CY2025 is based on value for optical fiber cable and volume for optical fiber.  
Source: Ministry of Finance

Exhibit 8: Export value, volume and average export price (yoy, mom) for two major European markets and the US

<table><tr><td rowspan="2"></td><td rowspan="2">% in CY2025</td><td colspan="2">Value</td><td colspan="2">Volume</td><td colspan="2">ASP</td></tr><tr><td>YoY</td><td>MoM</td><td>YoY</td><td>MoM</td><td>YoY</td><td>MoM</td></tr><tr><td colspan="8">Optical Cable</td></tr><tr><td>US</td><td>58%</td><td>50%</td><td>95%</td><td>-16%</td><td>66%</td><td>78%</td><td>18%</td></tr><tr><td>UK</td><td>4%</td><td>-83%</td><td>247%</td><td>-69%</td><td>359%</td><td>-46%</td><td>-24%</td></tr><tr><td>France</td><td>0%</td><td>-63%</td><td>1%</td><td>-99%</td><td>0%</td><td>6095%</td><td>1%</td></tr><tr><td>All regions</td><td>100%</td><td>129%</td><td>140%</td><td>168%</td><td>458%</td><td>-14%</td><td>-57%</td></tr><tr><td colspan="8">Optical Fiber</td></tr><tr><td>US</td><td>54%</td><td>109%</td><td>138%</td><td>21%</td><td>117%</td><td>72%</td><td>10%</td></tr><tr><td>UK</td><td>1%</td><td>19%</td><td>-29%</td><td>-48%</td><td>574%</td><td>127%</td><td>-90%</td></tr><tr><td>France</td><td>2%</td><td>-69%</td><td>-21%</td><td>-60%</td><td>-12%</td><td>-24%</td><td>-10%</td></tr><tr><td>All regions</td><td>100%</td><td>56%</td><td>26%</td><td>0%</td><td>51%</td><td>55%</td><td>-17%</td></tr></table>

% in CY2025 is based on value for optical fiber cable and volume for optical fiber.

Source: Ministry of Finance

Exhibit 9: Export value, volume and average export price by customs jurisdiction (yoy, mom)

<table><tr><td rowspan="2">Custom</td><td rowspan="2">% in CY2025</td><td colspan="2">Value</td><td colspan="2">Volume</td><td colspan="2">ASP</td></tr><tr><td>YoY</td><td>MoM</td><td>YoY</td><td>MoM</td><td>YoY</td><td>MoM</td></tr><tr><td colspan="8">Optical Cable</td></tr><tr><td>Tokyo</td><td>37%</td><td>38%</td><td>-3%</td><td>13%</td><td>-12%</td><td>22%</td><td>10%</td></tr><tr><td>Yokohama</td><td>53%</td><td>226%</td><td>419%</td><td>372%</td><td>1066%</td><td>-31%</td><td>-55%</td></tr><tr><td>Nagoya</td><td>2%</td><td>89%</td><td>354%</td><td>-53%</td><td>234%</td><td>302%</td><td>36%</td></tr><tr><td>All customs</td><td>100%</td><td>129%</td><td>140%</td><td>168%</td><td>458%</td><td>-14%</td><td>-57%</td></tr><tr><td colspan="8">Optical Fiber</td></tr><tr><td>Tokyo</td><td>93%</td><td>58%</td><td>32%</td><td>2%</td><td>64%</td><td>55%</td><td>-19%</td></tr><tr><td>Yokohama</td><td>0%</td><td>-100%</td><td>-100%</td><td>-</td><td>0%</td><td>-</td><td>0%</td></tr><tr><td>Nagoya</td><td>3%</td><td>-65%</td><td>-9%</td><td>-98%</td><td>0%</td><td>1872%</td><td>-9%</td></tr><tr><td>All customs</td><td>100%</td><td>56%</td><td>26%</td><td>0%</td><td>51%</td><td>55%</td><td>-17%</td></tr></table>

% in CY2025 is based on value for optical fiber cable and volume for optical fiber.  
Source: Ministry of Finance

## Price Target Risks and Methodology - Fujikura

We are Buy rated. Our 12-month price target of ¥7,500 is based on an EV/EBITDA of 25.0X (FY3/28E; multiple based on the EV/EBITDA and EBITDA margin correlation across its domestic and global competitors). Downside risks: Telecommunications: A delay in benefits from hyperscaler investment, a prolonged restraint in telecom carrier investment, and competitors in ultra-high-density optical fiber cables catching up with Fujikura. Electronics: A greater-than-expected slowdown in the smartphone market and/or more intense competition. Automotive products: Automobile production volume undershooting our assumptions. Companywide: Forex swings.

## Price Target Risks and Methodology - Furukawa Electric

Our 12-month target price is ¥7,200. We apply an EV/EBITDA multiple of 25.0X (FY3/28E, based on the correlation between EV/EBITDA and EBITDA growth rate for domestic and overseas competitors). We are Buy rated. Risks: Communications solutions: If sales expansion of high-margin optical products for data centers does not proceed as expected and there is no improvement in profits. If the profitability of the acquired Furukawa FITEL Optical Components (FFOC) deteriorates again due to factors such as changes in competitiveness. If generative AI data center investment slows for reasons such as delays in data center construction due to supply shortages of some essential products, or if investment in generative AI data centers starts to wane as project profitability deteriorates due to price hikes for component products. Energy infrastructure: If demand for both high-voltage and medium/low-voltage cables slows due to factors such as a slowdown in generative AI investment. If the company decides on capex for HVDC cables but fails to secure the expected orders from customers. Electronics & automotive systems: If auto production volume or sales of models supplied by the company do not grow as much as expected. If fluctuations in auto production volume are larger than expected and the company is unable to absorb fixed costs through measures such as price revisions. If material prices surge more than expected and the company is unable to pass these on to customers. Functional products: If, in the copper foil business, sales expansion of high-function circuit foils does not proceed as planned and profitability improvement is not expected, if orders for thermal products for generative AI are not booked as sales for some reason or are delayed, or if the acquisition of new customers for semiconductor manufacturing tape does not progress as expected.

Price Target Risks and Methodology - Sumitomo Electric Industries
We are Buy rated. Our 12-month target price is ¥3,400. We apply a target EV/EBITDA multiple of 13.0X (based on FY3/28E, using an SOTP approach). Key downside risks: Automotive segment: Decline in automobile production volume; slower-than-expected pass-through of material procurement costs to selling prices. Infocommunications segment: Longer-than-expected inventory adjustments due to a slowdown in hyperscaler capex; catch-up by competitors in ultra-high density optical fiber cables. Environment & energy segment: Delays in new and replacement power infrastructure projects due to difficulties in procuring materials and securing workers; slower-than-expected earnings contributions from the Japanese government's clean energy strategy. Industrial materials and other segments: Slowdown in demand for cemented carbide tools, etc., due to a macroeconomic slowdown; increase in manufacturing costs for sintered parts, etc., due to rising energy prices. Company-wide: FX fluctuations; sustained high material prices.

## Price Target Risks and Methodology - Anritsu

Our 12-month target price is ¥5,300, based on a target EV/EBITDA multiple of 17X on FY3/28E (our target multiple is based on the correlation between EV/EBITDA and EBITDA margin for global competitors). We are Buy rated.

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

The rating(s) for Anritsu, Fujikura, Furukawa Electric and Sumitomo Electric Industries is/are relative to the other companies in its/their coverage universe: Anritsu, Daihen, Fuji Electric Co., Fujikura, Furukawa Electric, Hitachi, Meidensha, Mitsubishi Electric, Panasonic Holdings, SWCC, Sumitomo Electric Industries

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The Goldman

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
