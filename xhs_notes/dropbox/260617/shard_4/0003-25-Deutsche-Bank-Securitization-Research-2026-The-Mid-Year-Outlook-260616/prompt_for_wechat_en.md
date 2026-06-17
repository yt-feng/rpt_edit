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
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
## Securitization Research 2026 The Mid-Year Outlook

16 June 2026

Edward Reardon, Douglas Runte, CFA, Conor O-Toole, Kayvan Darouian,

Bipul Sinha, CFA, Jamie Flannick, Rupesh Shrivastav, Vivek John, Nick Huang

## Table of Contents

Macro: Demand-surge pricing

Commercial MBS: Supportive technicals, accelerating credit resolution

CLO: Reflections at the midpoint

Consumer and Esoteric ABS: Rising issuance, mixed picture on credit

Transportation Debt: Record aircraft ABS issuance in 2026

Residential MBS: Stand and de-lever: AAAs for carry/roll, BB for de-lever/upgrade

Download DB Securitization Market Databank.xlsx

## Securitized Mid-Year Outlook Demand-surge pricing

Ed Reardon, Managing Director
Rupesh Shrivastav, Research Associate

## Big Pic: Demand surge pricing

DB Economics View.

■ Resilient economy: 2.2% real GDP growth forecast. Supported by fiscal policy, financial conditions, and AI investments. Fiscal deficit at 6.6% with risk from war, tariff refunds. Higher oil (\$150/bbl) a risk to consumer spending and could reduce real GDP to 1.75%.  
Labor: Firmer payroll gains, broader job growth. 4.3% unemployment through 2026.  
Inflation: Disinflation story less convincing, with core PCE expected to remain at 3.0%.  
Rates: Fed on hold “indefinitely”; risk skewed towards hikes. 10yr UST forecast: 4.7%.

■ Supply. Securitized full-year issuance now projected at \$1tn, net issuance is only \$270bn.

Demand. \$500bn of inflows into IG credit. \$300bn of projected annuity inflows plus \$200bn IG mutual and bond funds. Securitized likely to garner \~\$200bn.

Credit. We downgrade the Consumer slightly from B+ to a B. For securitized, a 'B' grade is still a positive backdrop and only impacts a handful of sectors and some deep subordinates.

Rates. Higher rates normally a headwind for issuance/credit, but strong economy over-riding this challenge. Higher rates will create refi stress for CLOs, CMBS.

Demographics. Demographics are playing a key role in credit. How? 1) Boomers have strong natural demand for fixed income and have the most assets, 2) Boomers are also home-owners and sitting on significant home equity.

\- Relative Value. Take the carry. Securitized will outperform Corporates via carry. Securitized sector forecasts are slightly wider. We see Non-QM as an outperformer; CLO carry is compelling. Subordinate securitized bonds will remain a food fight due to insurance demand and annuity inflows.

## Private Label Issuance Approaches Record Highs

US Securitized Credit Issuance by Sector, \$bn  
![](images/8ec89bd6272c902a35c55c9e5aee320d58c366f03951c6a9f8f177e9d5da63aa.jpg)

<details>
<summary>stacked bar chart</summary>

| Year       | ABS  | CLO  | Non-Age CMBS | Non-Age RMBS |
| ---------- | ---- | ---- | ------------ | ------------ |
| 2020       | 170  | 80   | 50           | 130          |
| 2021       | 260  | 190  | 140          | 230          |
| 2022       | 230  | 130  | 80           | 140          |
| 2023       | 250  | 110  | 40           | 60           |
| 2024       | 310  | 180  | 110          | 130          |
| 2025       | 330  | 190  | 140          | 230          |
| 2026ytd    | 160  | 60   | 80           | 130          |
| 2026 YE Proj. | 350 | 170 | 140          | 230          |
</details>

Source: CMA, Intex, DB, Bloomberg Finance LLP

We forecast Private Label issuance to reach \$925bn in 2026 broadly in line with the record volumes observed in 2025 (\$909bn). Including Agency CMBS, total gross issuance will exceed \$1tn.  
■ Strong capital markets execution and healthy investor demand continue to support issuance across structured credit sectors.

## Elon Musk isn't the the only Trillion-dollar game in town

![](images/83ecdd54d35d1274656bff88b79bf44a91a5eb56a28202ec45f54c74cc78c683.jpg)

2026 Issuance and Net Supply Projections, \$bn

<table><tr><td rowspan="2">Sector</td><td colspan="3">Issuance, $bn</td><td colspan="2">Net Issuance, $bn</td></tr><tr><td>2025</td><td>2026YTD</td><td>2026YE</td><td>2026 Proj. Paydowns</td><td>2026F Net</td></tr><tr><td>CMBS Non-Ag</td><td>155</td><td>82</td><td>160</td><td>145</td><td>15</td></tr><tr><td>CMBS Agency</td><td>57</td><td>39</td><td>75</td><td>45</td><td>30</td></tr><tr><td>ABS</td><td>339</td><td>168</td><td>360</td><td>305</td><td>55</td></tr><tr><td>CLO BSL</td><td>166</td><td>58</td><td>145</td><td>85</td><td>60</td></tr><tr><td>CLO Mid Mkt</td><td>43</td><td>14</td><td>45</td><td>15</td><td>30</td></tr><tr><td>RMBS Non-Ag</td><td>205</td><td>101</td><td>215</td><td>135</td><td>80</td></tr><tr><td>Total</td><td>966</td><td>462</td><td>1000</td><td>730</td><td>270</td></tr></table>

Source: CMA, Intex, DB, Bloomberg Finance LLP

■ Gross issuance projected to exceed \$1tn for the first time.  
ABS and Non-Agency RMBS remain the largest contributors to market growth, benefiting from resilient consumer credit and non-agency mortgage origination.  
- Net Supply will only be \~\$270bn, much lower than the \$1tn headline.

## Demand-surge pricing: \$500bn inflows into credit Cumulative IG Fund Flows vs Fixed Annuity Sales \$bn

![](images/69a52c4d8f995b2b9ff6e600d1584aa86288a05c08facb816f1c285ea0eab464.jpg)

<details>
<summary>line chart</summary>

| Week | 2022 | 2023 | 2024 | 2025 |
|------|------|------|------|------|
| 0    | -    | -    | -    | -    |
| 4    | -    | -    | -    | -    |
| 8    | -    | -    | -    | -    |
| 12   | -    | -    | -    | -    |
| 16   | -    | -    | -    | -    |
| 20   | -    | -    | -    | -    |
| 24   | -    | -    | -    | -    |
| 28   | -    | -    | -    | -    |
| 32   | -    | -    | -    | -    |
| 36   | -    | -    | -    | -    |
| 40   | -    | -    | -    | -    |
| 44   | -    | -    | -    | -    |
| 48   | -    | -    | -    | -    |
| 52   | -    | -    | -    | -    |
</details>

Note: EPFR data as of 06/03/26. Bloomberg LINSTFA Index. Lines represent cumulative. EPFR fixed annuity funds flows: Dots represents cumulative. LIMRA fixed annuity sales at quarter end. Colors denoted Calander year.

Source: EPFR, DB

■ Underlying annuity demand: LIMRA fixed annuity sales will reach \~\$300bn. Higher rates likely to stimulate more inflows. Credit bond/mutual funds could bring in another \$200bn.  
Insurers buy IG Corp as a staple holding but securitized bonds help deliver the promised annuity yields.

Give Grandma and Grandpa a call...

<table><tr><td>Life event</td><td>Age Bucket</td><td>Pop Size, mn</td><td>Home Ownership rate</td><td>Est. Net Worth excl-Home</td></tr><tr><td></td><td>0-9</td><td>36</td><td></td><td></td></tr><tr><td></td><td>10-19</td><td>46</td><td></td><td></td></tr><tr><td></td><td>20-29</td><td>45</td><td>38%</td><td>$30,000</td></tr><tr><td></td><td>30-39</td><td>44</td><td>49%</td><td>$123,000</td></tr><tr><td></td><td>40-49</td><td>42</td><td>65%</td><td>$266,000</td></tr><tr><td></td><td>50-59</td><td>43</td><td>73%</td><td>$392,000</td></tr><tr><td></td><td>60-69</td><td>41</td><td>77%</td><td>$528,000</td></tr><tr><td></td><td>70-79</td><td>25</td><td>79%</td><td>$538,000</td></tr><tr><td></td><td>80+</td><td>18</td><td></td><td>$425,000</td></tr></table>

Note: Homeownership uses 50/50 blend of age groups to match with Census Bureau age groupings.  
Source: DB, Census Bureau, ICI.

Grandma and grandpa are doing pretty well for themselves.  
Homes and stocks. Demographics show a 60+ population of 84mn where over 75% own a home, participated in home price appreciation (40yrs: 5.5x increase) and a massive rise in financial wealth (40yrs S&P: 70x increase). Boomers control 60-70% of financial wealth. Big change. In 1990, working age segment controlled that share.  
■ Next up: Fixed Income. Underinvested in fixed income: coming decade could unleash \$2-4tn in fixed income demand, with some pull forward due to higher rates. Boomers have been waiting for this moment: the average 10yr UST has been 2.9% over the past 20 years.  
■ Annuity Appeal. Earn high annuity rates today of 5.5%, avoid taxes on this annuity income. Average fixed income annuity buyer is 62 years old.

## Securitized trading: Record year in sight!

Investment Grade, Non-Agency Securitization volumes, \$bn  
![](images/d2b9371280ad28937a7475e1b704f673a6f193da2e90d8bcad4a98b408f31b97.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | ABS   | CLO   | CMBS  | Non-Agy CMO |
|------|-------|-------|-------|-------------|
| 2019 | 235   | 100   | 140   | 40          |
| 2020 | 240   | 130   | 180   | 50          |
| 2021 | 170   | 80    | 130   | 30          |
| 2022 | 165   | 150   | 140   | 45          |
| 2023 | 185   | 160   | 120   | 55          |
| 2024 | 210   | 155   | 130   | 65          |
| 2025 | 230   | 180   | 150   | 75          |
| 2026 | 105   | 135   | 70    | 60          |
</details>

Source: Finra Trace

2026 YTD, overall IG trading volumes are \$375bn.  
■ RMBS and CLO trading activity has accelerated in 2026, with YTD volumes up 57% and 32% respectively vs same period in 2025.  
While ABS (-16%) and CMBS(-13%) volumes have moderated, despite softer ABS and CMBS trading volumes, liquidity conditions remain constructive across structured credit markets.

## Securitized spreads near historical lows

AAA Spreads vs 3-year trading range, bp  
![](images/b69f66d9b7c7e7cb7d8993e9aefb93e11e52d36e9a7d8522bf138da8d146a0d2.jpg)

<details>
<summary>scatterplot</summary>

| Category             | Current | 3yr Ave | 3yr High | 3yr Low |
|----------------------|---------|---------|----------|---------|
| CMBS AAA 5Yr         | 70      | 105     | 180      | 60      |
| CMBS AAA 10Yr        | 70      | 105     | 160      | 70      |
| Corp IG              | 70      | 90      | 140      | 70      |
| CLO AAA              | 105     | 125     | 190      | 90      |
| NonQM AAA            | 115     | 145     | 205      | 95      |
| Subprime Auto AAA 2yr| 45      | 65      | 120      | 45      |
| Prime Auto AAA 3year | 30      | 50      | 90       | 30      |
</details>

BBB Spreads vs 3-year trading range, bp  
![](images/05ae9aca7c4b949ff69d80d8cca9aca6738b0f2b006912b981547172c004d36c.jpg)

<details>
<summary>scatterplot</summary>

| Category           | Current | 3yr High | 3yr Ave | 3yr Low |
| ------------------ | ------- | -------- | ------- | ------- |
| CLO BBB            | 280     | 500      | 300     | 220     |
| CMBS BBB 10Yr       | 550     | 1100     | 780     | 560     |
| Corp HY            | 280     | 480      | 300     | 240     |
| NonQM BBB          | 180     | 480      | 240     | 160     |
| Prime Auto BBB 3year | 120     | 280      | 160     | 100     |
</details>

Note: Spreads as of 06/12. Min/Max values are within 3year range. US CMBS 2.0 Total Return Index unhedged spreads.  
Source: DB, Intex.

■ Most credit sectors are pricing on the tight end of a 3-year history.  
IG and HY Corp are close to 25-year tights.  
- Carry and security selection are likely to be larger drivers of returns in 2H26.

## Securitized Credit Spread Forecast

## Securitized issuance, \$bn

Spreads, bp

<table><tr><td colspan="2">Sector</td><td>2026 Current (06/11)</td><td>YearEnd-2026 Forecast</td><td>Change</td></tr><tr><td rowspan="11">Securitized Credit</td><td>AAA CMBS</td><td>75</td><td>75</td><td>0</td></tr><tr><td>BBB CMBS</td><td>425</td><td>475</td><td>50</td></tr><tr><td>AAA CLO</td><td>124</td><td>126</td><td>2</td></tr><tr><td>BBB CLO</td><td>285</td><td>295</td><td>10</td></tr><tr><td>AAA SP Auto 2yr</td><td>48</td><td>50</td><td>2</td></tr><tr><td>BBB SP Auto</td><td>120</td><td>125</td><td>5</td></tr><tr><td>AAA Cards</td><td>27</td><td>30</td><td>3</td></tr><tr><td>AAA PSLABS</td><td>90</td><td>95</td><td>5</td></tr><tr><td>AAA FFELP</td><td>80</td><td>80</td><td>0</td></tr><tr><td>AAA Non-QM RMBS</td><td>112</td><td>105</td><td>-7</td></tr><tr><td>BBB Non-QM RMBS</td><td>170</td><td>155</td><td>-15</td></tr><tr><td rowspan="4"></td><td>Fed Funds</td><td>3.75%</td><td>3.75%</td><td>0.00%</td></tr><tr><td>10 Yr UST</td><td>4.5%</td><td>4.7%</td><td>0.24%</td></tr><tr><td>IG Corp</td><td>74</td><td>82</td><td>8</td></tr><tr><td>HY Corp</td><td>271</td><td>305</td><td>34</td></tr></table>

Note: Fed Funds is the upper bound of Fed Funds target range.  
Source: CMA, Intex, DB, Bloomberg Finance LP

AAA securitized spreads expected to remain largely stable through year-end. BBB spreads likely to modestly widen amid macro and rate uncertainty.

## Insurers: Hoovering up "securitized" bonds

## Insurance bond holdings, \$bn

<table><tr><td></td><td>2025</td><td>% Total</td></tr><tr><td>Agy CMBS</td><td>90</td><td>2%</td></tr><tr><td>Non Agy CMBS</td><td>200</td><td>4%</td></tr><tr><td>Agy RMBS</td><td>324</td><td>6%</td></tr><tr><td>Non Agy RMBS</td><td>186</td><td>3%</td></tr><tr><td>CLO</td><td>311</td><td>6%</td></tr><tr><td>ABS</td><td>398</td><td>7%</td></tr><tr><td>Corp</td><td>2745</td><td>49%</td></tr><tr><td>UST</td><td>394</td><td>7%</td></tr><tr><td>Other Securities</td><td>898</td><td>16%</td></tr><tr><td>Total</td><td>5,547</td><td>100%</td></tr></table>

Note: We exclude \$54bn of Equity-backed ABS from ABS, included in Other securities
Source: DB, S&P Global Market Intelligence, NAIC Schedule D.

## "ABS" securitized bond holdings reported to NAIC

<table><tr><td>Assets</td><td>NAIC Category</td><td>Total, $bn</td><td>% of Total</td><td>Remarks</td></tr><tr><td>Financial Assets</td><td>Self-Liquidating</td><td>165</td><td>45%</td><td>Traditional ABS, RMBS, CMBS, CLOs</td></tr><tr><td></td><td>Not Self-Liquidating</td><td>57</td><td>16%</td><td></td></tr><tr><td></td><td>Equity Backed</td><td>52</td><td></td><td>Fund finance notes; Structured equity investments</td></tr><tr><td></td><td>Other</td><td>6</td><td></td><td>Warehouse Facilities / Private Credit Warehouses</td></tr><tr><td rowspan="3">Non Financial Assets</td><td>Practical Expedient</td><td>62</td><td>17%</td><td></td></tr><tr><td>Lease Backed</td><td>24</td><td></td><td>Aircraft lease ABS; Solar lease / Solar loan ABS</td></tr><tr><td>Other</td><td>39</td><td></td><td>Music royalties, and and solar/other ABS</td></tr><tr><td></td><td>Full Analysis</td><td>80</td><td>22%</td><td></td></tr><tr><td></td><td>Lease Backed</td><td>34</td><td></td><td>Data center ABS / Digital infrastructure ABS</td></tr><tr><td></td><td>Other</td><td>46</td><td></td><td>Whole-business ABS and IP/royalty ABS</td></tr><tr><td></td><td>Total</td><td>365</td><td>100%</td><td></td></tr></table>

Note: \$365bn is life insurance holdings only  
Source: DB, S&P Global Market Intelligence, NAIC Schedule D.

Insurers own \$1tn+ of credit-sensitive securitized assets (\$200bn non agency CMBS, \$186bn non agency RMBS, \$311bn CLO and \$398bn "ABS"). ABS is more than just traditional ABS.  
NAIC reporting change gives some further clues on “ABS” bucket: warehouse finance facilities, solar, datacenter, whole business, royalties.

## Basel III: Banks will be better buyers

<table><tr><td>Description</td><td>2023 Proposal</td><td>2026 Re-Proposal (Mar-26)</td><td>Comment</td></tr><tr><td>P-factor</td><td>1.0 (Punitive)</td><td>0.5 (Unchanged from Current)</td><td>2023 Proposal to use 1.0 &quot;p factor&quot; in KSSFA formula would increase capital for all tranches.P factor was left unchanged at 0.5</td></tr><tr><td>Risk weight floor</td><td>20%</td><td>15% for senior tranches</td><td>Proposal lowers the floor for senior securitization tranche risk weights</td></tr><tr><td>Senior tranche &quot;Look-through&quot;</td><td>Limited</td><td>Banks can use a&quot;look through&quot; to the risk weight of the underlying assets to determine the senior tranche risk weight</td><td>Prevents situation where banks hold more capital in a senior tranche than the underlying assets themselves</td></tr></table>

Source: Federal Basel III proposal.

Basel III includes favorable capital requirements for securitized tranches held by banks.  
- Mostly favorable outcomes: Lower risk weight floor of 15% on senior tranches, p factor left unchanged at 0.5. (P factor is an input into the securitized formula called KSSFA, where higher P input increases capital for more senior tranches).  
Bank demand should improve via the lower risk weight floor and p-factor staying the same. Banks have been net sellers of securitized products for a couple of years.

## CMBS 2026 Mid-Year Outlook

## Supportive technicals, accelerating credit resolution

Ed Reardon, Managing Director

Bipul Sinha, CFA, Research Analyst

Rupesh Shrivastav, Research Associate

15 $^{th}$ June 2026

## Big Pic: Supportive technicals, accelerating credit resolution

Supply runs hot, but the market is rate-constrained. We forecast \$160bn of private-label CMBS issuance in 2026, with SASB and CRE CLO activity carrying the momentum while conduit remains capped by borrower refi economics and rate volatility.  
- Spreads. Technicals remain constructive. Limited net supply and higher rates will keep demand firm. We expect AAA spreads to remain range-bound at 75-80bp, with BBB spreads widening by roughly 50bp.  
■ Relative value. Prefer SASB mezz over conduit due to better collateral transparency and sponsor selection, even though risk is binary.  
Credit stress is moving from extension to realization

Conduit 60+ delinquency continue to rise. Legacy office and recent multi-family loans are the primary delinquency driver.  
Headline delinquency understates stress. SASB delinquencies remain contained, but proactive extensions, modifications, and denominator growth have helped keep delinquencies low. Office needs more A/B modifications to reflect the basis reset.  
Liquidation volume/severity are increasing as special servicers work through the distressed backlog. Loss severity is a key trend to watch over the next year.

CMBS governance is a structural weak link. Workout outcomes hinge on conflicted control rights, opaque modifications, and delayed loss recognition. We propose cleaner incentives, proper accountability, faster transparency, and clearer documentation that limits discretion in workout outcomes.

Issuance Forecast, \$bn

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td>2024</td><td>2025</td><td colspan="2">2026</td></tr><tr><td>Full</td><td>Full</td><td>YTD</td><td>YE</td></tr><tr><td rowspan="4">Private Label</td><td>Conduit</td><td>33</td><td>34</td><td>12</td><td>30</td></tr><tr><td>SASB</td><td>70</td><td>91</td><td>44</td><td>95</td></tr><tr><td>CRE CLO</td><td>9</td><td>31</td><td>22</td><td>35</td></tr><tr><td>Total</td><td>112</td><td>155</td><td>78</td><td>160</td></tr><tr><td rowspan="4">Agency</td><td>Freddie</td><td>33</td><td>39

[中间内容因长度限制已省略]

 the Russian Federation.

Kingdom of Saudi Arabia: Deutsche Securities Saudi Arabia (DSSA) is a closed joint stock company authorized by the Capital Market Authority of the Kingdom of Saudi Arabia with a license number (No. 37-07073) to conduct the following business activities: Dealing, Arranging, Advising, and Custody activities. . DSSA registered office is at Faisaliah Tower, 17th floor, King Fahad Road - Al Olaya District Riyadh, Kingdom of Saudi Arabia P.O. Box 301806.

United Arab Emirates: DB AG in the Dubai International Financial Centre (registered no. 00045) is regulated by the Dubai Financial Services Authority. DB AG - DIFC Branch may only undertake the financial services activities that fall within the scope of its existing DFSA license. Principal place of business in the DIFC: Dubai International Financial Centre, The Gate Village, Building 5, PO Box 504902, Dubai, U.A.E. This information has been distributed by DB AG. Related financial products or services are available only to Professional Clients, as defined by the Dubai Financial Services Authority.

Australia and New Zealand: This research is intended only for "wholesale clients" within the meaning of the Australian Corporations Act and New Zealand Financial Advisors Act, respectively. Please refer to Australian specific research disclosures and related information at https://www.dbresearch.com/PROD/RPS\_EN-PROD/PROD000000000521304.xhtml. Where research refers to any particular financial product recipients of the research should consider any product disclosure statement, prospectus or other applicable disclosure document before making any decision about whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG
"""
