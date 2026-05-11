You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as Goldman Sachs. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Americas Technology: Semiconductors: SIA data shows broad-based above-seasonal trends in March, with DRAM moderating

# Above-seasonal total unit trends in March were relatively broad based, with DRAM moderating

Shipments of integrated circuits (ex. memory) increased 29% month over month in March, well above typical seasonality, according to data from Semiconductor Industry Association (SIA). Most segments shipped at above-seasonal levels for the month except for discretes, DRAM, MPU, and DSP. Shipments are now tracking 4% below long-term demand on a three-month moving average basis (vs. 8% below trend in February). Improving trends over the past few months are consistent with companies' commentary on shipping closer to end demand on average, but still at a measured rate of improvement. Performance by sub-segment was as follows.

IC ex. Memory: Units were $3.9\%$ below trend vs. below $7.8\%$ in February.   
■ Analog: Units were 2.0% below trend, better than 6.5% below trend in January.   
■ MCU: Units were 26.0% below trend, better than 27.5% in January.

James Schneider, Ph.D.

+1(212)357-2929

jim.schneider@gs.com

Goldman Sachs & Co. LLC

Khalil Fenina

+1(212)357-6392

khalil.fenina@gs.com

Goldman Sachs & Co. LLC

Lal Kablan

+1(212)357-8793 | lal.kablan@gs.com

Goldman Sachs & Co. LLC

Anmol Makkar

+1(212)357-1366

anmol.makkar@gs.com

Goldman Sachs & Co. LLC

Luya You

+1(212)902-5297 | luya.you@gs.com

Goldman Sachs & Co. LLC

Exhibit 1: M/M % change in revenue, units and ASPs vs. historical levels 

<table><tr><td></td><td colspan="3">Revenue</td><td colspan="3">Units</td><td colspan="3">ASPs</td></tr><tr><td>March 2026</td><td>M/M Rev % Chg</td><td>Hist. M/M % Chg</td><td>Y/Y % Chg</td><td>M/M Unit % Chg</td><td>Hist. M/M Unit % Chg</td><td>Y/Y Unit % Chg</td><td>M/M ASP % Chg</td><td>Hist. M/M ASP %</td><td>Y/Y ASP % Chg</td></tr><tr><td>Total Semiconductors</td><td>14%</td><td>14%</td><td>115%</td><td>20%</td><td>19%</td><td>34%</td><td>-4%</td><td>-5%</td><td>60%</td></tr><tr><td>Discretes</td><td>26%</td><td>23%</td><td>36%</td><td>21%</td><td>25%</td><td>28%</td><td>4%</td><td>-1%</td><td>6%</td></tr><tr><td>Integrated Circuits</td><td>14%</td><td>12%</td><td>127%</td><td>27%</td><td>20%</td><td>40%</td><td>-10%</td><td>-7%</td><td>62%</td></tr><tr><td>DRAM</td><td>10%</td><td>9%</td><td>330%</td><td>5%</td><td>9%</td><td>21%</td><td>5%</td><td>2%</td><td>256%</td></tr><tr><td>NAND</td><td>34%</td><td>13%</td><td>324%</td><td>15%</td><td>10%</td><td>25%</td><td>16%</td><td>4%</td><td>241%</td></tr><tr><td>ICs ex. Memory</td><td>11%</td><td>12%</td><td>45%</td><td>29%</td><td>22%</td><td>39%</td><td>-14%</td><td>-8%</td><td>5%</td></tr><tr><td>MPU</td><td>9%</td><td>7%</td><td>36%</td><td>0%</td><td>8%</td><td>21%</td><td>9%</td><td>-2%</td><td>13%</td></tr><tr><td>MCU</td><td>25%</td><td>25%</td><td>40%</td><td>22%</td><td>19%</td><td>26%</td><td>3%</td><td>-1%</td><td>11%</td></tr><tr><td>DSP</td><td>27%</td><td>25%</td><td>-5%</td><td>17%</td><td>18%</td><td>-8%</td><td>9%</td><td>-1%</td><td>3%</td></tr><tr><td>Analog</td><td>17%</td><td>19%</td><td>32%</td><td>32%</td><td>26%</td><td>44%</td><td>-11%</td><td>-7%</td><td>-9%</td></tr><tr><td>Logic</td><td>10%</td><td>10%</td><td>35%</td><td>21%</td><td>14%</td><td>21%</td><td>-9%</td><td>-4%</td><td>11%</td></tr></table>

Source: SIA, Goldman Sachs Global Investment Research

Stock implications: We expect shipments to further approach trend in the near term, which is consistent with more constructive company commentary on the normalization of demand and customer inventory levels, which we view as positive for analog overall. We continue to prefer Microchip, NXP, and Analog Devices as we focus on shipping furthest below trend and differentiated supply chain management.

Goldman Sachs does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

# IC Units ex. Memory

IC units ex. Memory relative to trend are shown below (see Exhibit 2).

Exhibit 2: IC units ex. Memory are \~4% below trend as of March   
IC units ex. Memory 3 months average (units in millions)   
![](images/5793f8fffc55cf202c210b70dc3226cca3bb0ba3ad2c1da5633f193fec489a08.jpg)

<details>
<summary>line</summary>

| Date     | IC units ex Memory 3m avg (units in mn) |
|----------|------------------------------------------|
| Jan-93   | ~2,000                                   |
| Feb-94   | ~2,500                                   |
| Mar-95   | ~3,000                                   |
| Apr-96   | ~3,500                                   |
| May-97   | ~4,000                                   |
| Jun-98   | ~4,500                                   |
| Jul-99   | ~5,000                                   |
| Aug-00   | ~5,500                                   |
| Sep-01   | ~6,000                                   |
| Oct-02   | ~6,500                                   |
| Nov-03   | ~7,000                                   |
| Dec-04   | ~7,500                                   |
| Jan-06   | ~8,000                                   |
| Feb-07   | ~8,500                                   |
| Mar-08   | ~9,000                                   |
| Apr-09   | ~10,000                                  |
| May-10   | ~11,000                                  |
| Jun-11   | ~12,000                                  |
| Jul-12   | ~13,000                                  |
| Aug-13   | ~14,000                                  |
| Sep-14   | ~15,000                                  |
| Oct-15   | ~16,000                                  |
| Nov-16   | ~17,000                                  |
| Dec-17   | ~18,000                                  |
| Jan-19   | ~19,000                                  |
| Feb-20   | ~20,000                                  |
| Mar-21   | ~22,000                                  |
| Apr-22   | ~25,000                                  |
| May-23   | ~28,000                                  |
| Jun-24   | ~29,000                                  |
| Jul-25   | ~30,000                                  |
</details>

Source: SIA, Goldman Sachs Global Investment Research

Exhibit 3: IC units ex. memory were up $29\%$ M/M, above typical history   
M/M % change in units   
![](images/3ec9b426f7fbcb1db57dbaeb3b43751684da9e082d00eb241f7d5593da025932.jpg)

<details>
<summary>bar</summary>

| Year | IC Units ex Memory (%) |
|---|---|
| 2015 | 32.2 |
| 2016 | 22.0 |
| 2017 | 24.1 |
| 2018 | 27.3 |
| 2019 | 19.0 |
| 2020 | 18.9 |
| 2021 | 14.4 |
| 2022 | 12.2 |
| 2023 | 44.2 |
| 2024 | 15.3 |
| 2025 | 29.0 |
Median (dashed line) at ~22.0%
</details>

Source: SIA, Goldman Sachs Global Investment Research

# Analog

Analog units relative to trend are shown below (see Exhibit 4).

Exhibit 4: Analog units are $\sim 2\%$ below trend as of March Analog units 3 months average (units in millions)   
![](images/b65c9ed33e2ea9e49849becaa19f4fb5baaba4fc49551d3d23e7c6e4b7db466e.jpg)

<details>
<summary>line</summary>

| Date    | Analog units 3m avg (units in mn) |
|---------|------------------------------------|
| Jan-93  | ~1,000                             |
| Apr-94  | ~1,500                             |
| Jul-95  | ~2,000                             |
| Oct-96  | ~2,500                             |
| Jan-98  | ~3,000                             |
| Apr-99  | ~3,500                             |
| Jul-00  | ~4,000                             |
| Oct-01  | ~4,500                             |
| Jan-03  | ~5,000                             |
| Apr-04  | ~5,500                             |
| Jul-05  | ~6,000                             |
| Oct-06  | ~6,500                             |
| Jan-08  | ~7,000                             |
| Apr-09  | ~7,500                             |
| Jul-10  | ~8,000                             |
| Oct-11  | ~8,500                             |
| Jan-13  | ~9,000                             |
| Apr-14  | ~9,500                             |
| Jul-15  | ~10,000                            |
| Oct-16  | ~11,000                            |
| Jan-18  | ~12,000                            |
| Apr-19  | ~13,000                            |
| Jul-20  | ~14,000                            |
| Oct-21  | ~15,000                            |
| Jan-23  | ~16,000                            |
| Apr-24  | ~17,000                            |
| Jul-25  | ~18,000                            |
</details>

Source: SIA, Goldman Sachs Global Investment Research

Exhibit 5: Analog units were up $32\%$ M/M, well above typical history   
M/M % change in units   
![](images/6aff4adf872690ddf9c0f27ea5b39170af8fa58d8733e073d223437c6d44bbb4.jpg)

<details>
<summary>bar</summary>

| Year | Analog (%) | Median (%) |
|---|---|---|
| 2015 | 40.0 | 26.8 |
| 2016 | 27.1 | 26.8 |
| 2017 | 27.6 | 26.8 |
| 2018 | 28.8 | 26.8 |
| 2019 | 22.2 | 26.8 |
| 2020 | 22.6 | 26.8 |
| 2021 | 17.9 | 26.8 |
| 2022 | 13.1 | 26.8 |
| 2023 | 51.8 | 26.8 |
| 2024 | 16.2 | 26.8 |
| 2025 | 31.9 | 26.8 |
</details>

Source: SIA, Goldman Sachs Global Investment Research

# Microcontrollers (MCU)

MCU units relative to trend are shown below (see Exhibit 6).

Exhibit 6: MCU units are \~26% below trend as of March MCU units 3 months average (units in millions)   
![](images/135a4803b55617a170a2087b6d5e77abd8df1671ae3edbcfe7dec3dc7cd15306.jpg)

<details>
<summary>line</summary>

| Date    | MCU units 3m avg (units in mn) |
|---------|-------------------------------|
| Jan-93  | 0                             |
| Apr-94  | 100                           |
| Jul-95  | 200                           |
| Oct-96  | 300                           |
| Jan-98  | 400                           |
| Apr-99  | 500                           |
| Jul-00  | 600                           |
| Oct-01  | 700                           |
| Jan-03  | 800                           |
| Apr-04  | 900                           |
| Jul-05  | 1000                          |
| Oct-06  | 1100                          |
| Jan-08  | 1200                          |
| Apr-09  | 1300                          |
| Jul-10  | 1400                          |
| Oct-11  | 1500                          |
| Jan-13  | 1600                          |
| Apr-14  | 1700                          |
| Jul-15  | 1800                          |
| Oct-16  | 1900                          |
| Jan-18  | 2000                          |
| Apr-19  | 2100                          |
| Jul-20  | 2200                          |
| Oct-21  | 2300                          |
| Jan-23  | 2400                          |
| Apr-24  | 2500                          |
| Jul-25  | 2600                          |
</details>

Source: SIA, Goldman Sachs Global Investment Research

Exhibit 7: MCU units were up $22\%$ M/M, above typical history   
M/M % change in units   
![](images/ced104ef490913ee993f81c7b5bbb068d05bf308299624b031a67b203ad49af1.jpg)

<details>
<summary>bar</summary>

| Year | Microcontrollers (%) | Median (%) |
|---|---|---|
| 2015 | 28.4 | 19.6 |
| 2016 | 15.5 | 19.6 |
| 2017 | 29.8 | 19.6 |
| 2018 | 32.0 | 19.6 |
| 2019 | 13.3 | 19.6 |
| 2020 | 14.3 | 19.6 |
| 2021 | 15.3 | 19.6 |
| 2022 | 18.7 | 19.6 |
| 2023 | 48.8 | 19.6 |
| 2024 | 17.8 | 19.6 |
| 2025 | 22.2 | 19.6 |
</details>

Source: SIA, Goldman Sachs Global Investment Research

# Memory

DRAM revenues were up 10% M/M, roughly in-line with typical M/M seasonality. NAND revenues were up 34% M/M, above typical M/M seasonality.

Exhibit 8: DRAM units were up $5\%$ M/M, below typical seasonality   
![](images/3bb2e7604b6d594e1b34eaa83dd0a57bcde23d24bd64535297d7fb8ebc5ad2e1.jpg)

<details>
<summary>line</summary>

| Date    | Units DRAM | ASP ($) |
|---------|------------|---------|
| Feb-04  | 500        | 5       |
| Dec-04  | 600        | 6       |
| Oct-05  | 700        | 7       |
| Aug-06  | 800        | 8       |
| Jun-07  | 900        | 9       |
| Apr-08  | 1000       | 10      |
| Feb-09  | 1100       | 11      |
| Oct-09  | 1200       | 12      |
| Aug-10  | 1300       | 13      |
| Jun-11  | 1400       | 14      |
| Apr-12  | 1500       | 15      |
| Feb-13  | 1600       | 16      |
| Oct-13  | 1700       | 17      |
| Aug-14  | 1800       | 18      |
| Jun-15  | 1900       | 19      |
| Apr-16  | 2000       | 20      |
| Feb-17  | 2100       | 21      |
| Oct-17  | 2200       | 22      |
| Aug-18  | 2300       | 23      |
| Jun-19  | 2400       | 24      |
| Apr-20  | 2500       | 25      |
| Feb-21  | 2600       | 26      |
| Oct-21  | 2700       | 27      |
| Aug-22  | 2800       | 28      |
| Jun-23  | 2900       | 29      |
| Apr-24  | 3000       | 30      |
| Feb-25  | 3100       | 31      |
| Oct-25  | 3200       | 32      |
</details>

Source: SIA, Goldman Sachs Global Investment Research

Exhibit 9: NAND units were up $15\%$ M/M, above typical seasonality   
![](images/822c8715e1aa5ce61810aac591b094fc8626b7b24590d8f0068263ac9ec0e29b.jpg)

<details>
<summary>line</summary>

| Date   | Units NAND | ASP |
|--------|------------|-----|
| Feb-04 | ~50        | ~10 |
| Feb-05 | ~100       | ~8  |
| Feb-06 | ~150       | ~7  |
| Feb-07 | ~200       | ~6  |
| Feb-08 | ~250       | ~5  |
| Feb-09 | ~300       | ~4  |
| Feb-10 | ~400       | ~3  |
| Feb-11 | ~500       | ~3  |
| Feb-12 | ~600       | ~3  |
| Feb-13 | ~700       | ~3  |
| Feb-14 | ~800       | ~3  |
| Feb-15 | ~900       | ~3  |
| Feb-16 | ~1,000     | ~3  |
| Feb-17 | ~1,100     | ~4  |
| Feb-18 | ~1,200     | ~4  |
| Feb-19 | ~1,300     | ~4  |
| Feb-20 | ~1,400     | ~4  |
| Feb-21 | ~1,500     | ~4  |
| Feb-22 | ~1,600     | ~4  |
| Feb-23 | ~1,700     | ~5  |
| Feb-24 | ~1,800     | ~6  |
| Feb-25 | ~1,900     | ~7  |
| Feb-26 | ~2,000     | ~18 |
</details>

Source: SIA, Goldman Sachs Global Investment Research

# Disclosure Appendix

# Reg AC

We, James Schneider, Ph.D., Khalil Fenina, Lal Kablan, Anmol Makkar and Luya You, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in Goldman Sachs' Global Investment Research division.

Contributing Authors: James Schneider, Ph.D. Goldman Sachs & Co. LLC, Khalil Fenina Goldman Sachs & Co. LLC, Lal Kablan Goldman Sachs & Co. LLC, Anmol Makkar Goldman Sachs & Co. LLC, Luya You Goldman Sachs & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in Goldman Sachs' Global Investment Research division.

# GS Factor Profile

The Goldman Sachs Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the Goldman Sachs analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

# M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

# Quantum

Quantum is Goldman Sachs' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

# Disclosures

# Rating and pricing information

Analog Devices Inc. (Buy, \$318.34), Microchip Technology Inc. (Buy, \$65.60) and NXP Semiconductors NV (Buy, \$194.55)

# Distribution of ratings/investment banking relationships

Goldman Sachs Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td>

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or Goldman Sachs policy.

The views attributed to third party presenters at Goldman Sachs arranged conferences, including individuals from other parts of Goldman Sachs, do not necessarily reflect those of Global Investment Research and are not an official view of Goldman Sachs.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from Goldman Sachs sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by Goldman Sachs Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is Goldman Sachs responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 Goldman Sachs.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of Goldman Sachs. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of Goldman Sachs. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
