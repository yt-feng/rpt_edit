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
# Clean Energy and Power Infrastructure 2026 Spring Series

Mark Strouse, CFA AC

212-622-8244

mark.w.strouse@JPM.com

JPM Securities LLC

Michael Fairbanks

212-622-4908

michael.fairbanks@jpmchase.com

JPM Securities LLC

Anna Zhu

212-622-0012

anna.zhu@JPM.com

JPM Securities LLC

See end pages for analyst certification and important disclosures.

# Long-Term Load Growth and Decarbonization

- US generation should approximately double by 2050, driven by onshoring, electrification, data centers, and population growth   
- JPM house view that data centers add $\sim 120$ GW by 2030 in US alone   
- Increased renewables mix driven by declining cost, federal government policy, state government policy (e.g., 29 states have RPS), and corporates   
- “All of the above” power sources needed

US Electricity Generation Capacity   
![](images/6037ae42f3ff84a82dd79917448f6b20bb291f8acb579494c6769d94cdb6d5f3.jpg)

<details>
<summary>pie</summary>

| Year | Coal (TW) | Oil and Natural Gas Steam (TW) | Combined Cycle (TW) | Combustion Turbine/Diesel (TW) | Nuclear Power (TW) | Fuel Cells (TW) | Renewable Sources (TW) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2015 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 2024 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 | 1.1 |
| 2030 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 |
| 2050 | 2.2 | 2.2 | 2.2 | 2.2 | 2.2 | 2.2 | 2.2 |
</details>

# 1Q26 in Review – “All of the Above” Demand

\- Gas turbines

- Global 1Q orders of \~29 GW up 39% y/y, largest 1Q in history   
• US orders up 144% y/y   
- GEV backlog+SRA 100 GW, up from 83 GW at 4Q25 and 50 GW at 1Q25   
• Visibility building beyond 2030

\- EPC – visibility building across multiple verticals

• 1Q26 book:bill: CTRI 1.8x, PWR 1.6x, MTZ 1.4x, MWH 1.3x, PRIM 0.8x   
- AGX believes current B/S could support backlog of \~\$4bn, from \$2.9bn at 1/31/26

Annual US Gas-Fired Capacity Additions   
![](images/b262596e7eabf2981c2791355b5cad021e0d13b447ae5a4047b9a55dc236af33.jpg)

<details>
<summary>bar</summary>

GW (CCGT Terms)
| Year | NEE Forecasted Cumulative Net Additions | EIA Forecasted Cumulative Net Additions | BNEF ETS Forecasted Cumulative Net Additions | McCoy Awarded Cumulative Capacity Additions |
|---|---|---|---|---|
| 2025 | | | | |
| 2026 | | | | |
| 2027 | | | | |
| 2028 | | | | |
| 2029 | | | | |
| 2030 | 91 | 50 | 46 | 100 |
</details>

NEE and McCoy data is JPMe adjusted to include full CCGT capacity.   
Source: JPM, Bloomberg Finance L.P., Energy Information Agency, NextEra Energy, McCoy Power.

N.America CCGT Project Costs by Completion Date   
![](images/fe2a6f7fed513918845ed4d44693174de50ab7963646e3218b19670f6ce337d1.jpg)

<details>
<summary>boxplot</summary>

| Year | Lower Bound ($/kW) | Median ($/kW) | Upper Bound ($/kW) |
|------|---------------------|---------------|---------------------|
| 2025 | ~700                | ~1000         | ~1050               |
| 2026 | ~650                | ~1000         | ~1400               |
| 2027 | ~800                | ~1250         | ~1450               |
| 2028 | ~900                | ~1500         | ~1750               |
| 2029 | ~950                | ~1600         | ~2300               |
| 2030 | ~1050               | ~1800         | ~2300               |
| 2031 | ~1150               | ~2150         | ~2250               |
| 2032 | ~1250               | ~2400         | ~2500               |
</details>

Source: JPM, Press Releases, Utility Filings.

# 1Q26 in Review

# - Fuel cells

- BE signs ORCL deal for up to 2.45 GW, raised FY26 guide   
• CEO stated no customer conversations for BE as bridge power

# - Back-up power gen (diesel/nat gas engines, small turbines)

- GNRC “on one yard line” with hyperscaler deal, with second soon thereafter   
- One hyperscaler deal has potential to double C&I revenue (\~\$1.5bn in FY25)   
- CAT plans to double power gen revenue by 2030, expanding to \~50 GW annual capacity covering multiple applications. Majority will be recip engines.   
• CMI CMD on 5/21 – JPM’s Zakaria expects capacity expansion announcement

# - Storage

• BNEF increased forecast   
- Expects FY26 global deployments up \~41% y/y   
- Expects FY26 US deployments up $\sim 12\%$ y/y, below global average due to flow-thru of 1H25 tariff and policy uncertainty   
- FLNC recently signed MSAs with two hyperscalers for $\sim 10$ GWh

# - Solar

- 1Q26 book:bill: ARRY \~2.0x, SHLS 1.1x, NXT >1.0x   
- WoodMac forecasts FY26 utility-scale solar up \~20% y/y   
- Resi solar potentially bottoming though debate on shape of recovery

# Baseload Stocks Continue to Outperform, Renewables Sentiment Rebounding

- “Direct” data center beneficiaries have outperformed YTD, including fuel cells, EPCs, diesel back-up   
- NXT outperforming renewables OEMs   
- ICLN seeing highest inflows since 2022 on “all of the above” theme

YTD Return for Stocks under Coverage   
![](images/5a62c5c37414a381c1010e2f0213c7480719f8ba9f2097a066d14972307ff726.jpg)

<details>
<summary>bar</summary>

| Entity | % YTD Return (%) |
| :--- | :--- |
| BE | 251 |
| FCEL | 179 |
| AGX | 134 |
| ENLT | 102 |
| MTZ | 98 |
| GNRC | 98 |
| PWR | 84 |
| SEDG | 68 |
| GEV | 64 |
| NXT | 61 |
| ENPH | 49 |
| HASI | 32 |
| CTRI | 29 |
| BEP | 29 |
| ORA | 21 |
| SPY | 10 |
| SHLS | 10 |
| FLNC | 10 |
| BEPC | -3 |
| PRIM | -6 |
| ARRY | -7 |
| FSLR | -11 |
| ITRI | -12 |
| XYL | -19 |
| RUN | -21 |
| CSIQ | -25 |
| EOSE | -28 |
| BMI | -32 |
| EVGO | -32 |
</details>

Source: Bloomberg Finance, L.P.

ICLN Rolling 10 Day Inflow   
![](images/7afc39028e2914e12974b21d7ab8c2351c9da203d0b34e4c3dd28d2d8c92c6b1.jpg)

<details>
<summary>line</summary>

| Date       | Value     |
| ---------- | --------- |
| 8/16/2021  | ($50.00)  |
| 8/16/2022  | ($100.00) |
| 8/16/2023  | ($200.00) |
| 8/16/2024  | ($150.00) |
| 8/16/2025  | ($250.00) |
</details>

Source: Bloomberg Finance, L.P.

# Top Picks

- Expect renewables to consolidate – generally positive for larger, public companies   
- Expect DC-exposed stock performance tied to orders/visibility, not just exposure

<table><tr><td>GE Vernova (GEV)</td><td>MasTec (MTZ)</td></tr><tr><td>GEV/OW/$285bn cap/$1,302 PT</td><td>MTZ/OW/$33bn cap/$491 PT</td></tr><tr><td>Leading global provider of gas turbine and grid equipment</td><td>Leading US EPC across multiple verticals</td></tr><tr><td>*Increased pricing provides visibility into margin upside compared to the company&#x27;s long-term targets
*Expect gas turbine capacity to be sold out thru YE29 during 1H26. Deposits and milestone payments aid cash flow
*Electrification margins ramping, accelerated capacity could drive further upside</td><td>*Strong market position across several verticals benefiting from data center demand including civil, power, communications, and pipeline
*Recently issued FY28 financial targets viewed as a floor
*Strong balance sheet and cash flow provide ability to conduct accretive M&amp;A in a fragmented market</td></tr></table>

# Nextpower (NXT)

NXT/OW/\$20bn cap/\$155 PT

Leading provider of utility-scale solar solutions

\*Expect market complexity to lead to share gains for NXT and NXT's largely tier-1 customer base

\*Superior execution to peers with regards to project delays

\*Leading market position, net cash balance sheet, relatively more geographic diversification

\*Cash flow supporting accretive M&A within utility-scale solar solutions (“everything but the panel”)

# Upcoming Events

• May 18 – JPM Tech, Media, and Communications Conference – Boston   
- ARRY   
• May 21 – BMI Analyst Day – NYC   
• May 28 – JPM Sustainable Investing Mid-Year 2026 webinar   
• June 1-3 – American Clean Power Conference – Houston   
• June 4 – JPM Houston EPC Bus Tour   
- PWR, FIX, STRL management meetings   
• June 9 – JPM SF Bay Area Clean Energy Manufacturing Bus Tour   
BE, ENPH, NXT management meetings and facility tours   
- June 23-24 – JPM Natural Resources Conference, An Energy, Power, Renewables & Mining event - NYC

# US Clean Energy Stock Coverage

<table><tr><td>Company</td><td>Ticker</td><td>Rating</td><td>Close Price*</td><td>YE26 Price Target</td><td>Lead Analyst</td></tr><tr><td>Argan</td><td>AGX</td><td>OW</td><td>$719.92</td><td>$550.00</td><td>Fairbanks</td></tr><tr><td>Array Technologies</td><td>ARRY</td><td>OW</td><td>$8.79</td><td>$10.00</td><td>Strouse</td></tr><tr><td>Badger Meter</td><td>BMI</td><td>OW</td><td>$116.07</td><td>$160.00</td><td>Fairbanks</td></tr><tr><td>Bloom Energy</td><td>BE</td><td>OW</td><td>$289.76</td><td>$267.00</td><td>Strouse</td></tr><tr><td>Brookfield Renewable Corp</td><td>BEPC</td><td>OW</td><td>$37.21</td><td>$42.00</td><td>Strouse</td></tr><tr><td>Brookfield Renewable Partners</td><td>BEP</td><td>OW</td><td>$34.47</td><td>$40.00</td><td>Strouse</td></tr><tr><td>Canadian Solar</td><td>CSIQ</td><td>UW</td><td>$20.05</td><td>$9.00</td><td>Strouse</td></tr><tr><td>Centuri</td><td>CTRI</td><td>UW</td><td>$32.07</td><td>$29.00</td><td>Strouse</td></tr><tr><td>Enlight Renewable Energy</td><td>ENLT</td><td>UW</td><td>$92.11</td><td>$68.00</td><td>Strouse</td></tr><tr><td>Enphase Energy</td><td>ENPH</td><td>N</td><td>$42.00</td><td>$35.00</td><td>Strouse</td></tr><tr><td>Eos Energy</td><td>EOSE</td><td>N</td><td>$8.28</td><td>$9.00</td><td>Strouse</td></tr><tr><td>EVgo</td><td>EVGO</td><td>N</td><td>$1.95</td><td>n/a</td><td>Strouse</td></tr><tr><td>First Solar, Inc</td><td>FSLR</td><td>OW</td><td>$234.60</td><td>$256.00</td><td>Strouse</td></tr><tr><td>Fluence Energy</td><td>FLNC</td><td>N</td><td>$22.10</td><td>$17.00</td><td>Strouse</td></tr><tr><td>FuelCell Energy</td><td>FCEL</td><td>UW</td><td>$19.92</td><td>n/a</td><td>Strouse</td></tr><tr><td>GE Vernova</td><td>GEV</td><td>OW</td><td>$1,062.57</td><td>$1,302.00</td><td>Strouse</td></tr><tr><td>Generac</td><td>GNRC</td><td>OW</td><td>$267.25</td><td>$267.00</td><td>Strouse</td></tr><tr><td>HA Sustainable Infrastructure Capital Inc</td><td>HASI</td><td>OW</td><td>$40.64</td><td>$50.00</td><td>Strouse</td></tr><tr><td>Itron</td><td>ITRI</td><td>OW</td><td>$82.22</td><td>$112.00</td><td>Strouse</td></tr><tr><td>MasTec</td><td>MTZ</td><td>OW</td><td>$423.79</td><td>$491.00</td><td>Strouse</td></tr><tr><td>Nextpower</td><td>NXT</td><td>OW</td><td>$136.37</td><td>$155.00</td><td>Strouse</td></tr><tr><td>Ormat Technologies</td><td>ORA</td><td>N</td><td>$133.39</td><td>$123.00</td><td>Strouse</td></tr><tr><td>Primoris</td><td>PRIM</td><td>N</td><td>$112.94</td><td>$105.00</td><td>Strouse</td></tr><tr><td>Quanta Services</td><td>PWR</td><td>OW</td><td>$773.72</td><td>$805.00</td><td>Strouse</td></tr><tr><td>Shoals</td><td>SHLS</td><td>OW</td><td>$9.11</td><td>$10.00</td><td>Strouse</td></tr><tr><td>SolarEdge Technologies</td><td>SEDG</td><td>N</td><td>$42.77</td><td>$35.00</td><td>Strouse</td></tr><tr><td>SOLV Energy</td><td>MWH</td><td>OW</td><td>$46.77</td><td>$51.00</td><td>Strouse</td></tr><tr><td>Sunrun Inc.</td><td>RUN</td><td>OW</td><td>$14.46</td><td>$22.00</td><td>Strouse</td></tr><tr><td>Xylem</td><td>XYL</td><td>OW</td><td>$109.01</td><td>$140.00</td><td>Fairbanks</td></tr></table>

# Disclosures

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

# Important Disclosures

- Market Maker: JPM Securities LLC makes a market in the securities of GE Vernova, Nextpower or related entities.   
- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to MasTec, GE Vernova, Nextpower or related entities.   
- Manager or Co-manager: JPM acted as manager or co-manager in a public offering of securities or financial instruments (as such term is defined in Directive 2014/65/EU) of/for GE Vernova or related entities within the past 12 months.   
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: MasTec, GE Vernova, Nextpower or related entities.   
- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: MasTec, GE Vernova, Nextpower or related entities.   
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: MasTec, GE Vernova, Nextpower or related entities.   
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: MasTec, GE Vernova, Nextpower or related entities.   
- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from MasTec, GE Vernova, Nextpower or related entities.   
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from MasTec, GE Vernova, Nextpower or related entities.   
- Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from MasTec, GE Vernova, Nextpower or related entities.   
- Debt Position: JPM may hold a position in the debt securities of MasTec, GE Vernova, Nextpower or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

# Disclosures

MasTec (MTZ, MTZ US) Price Chart   
![](images/258fd86fd17a3d9893be2c31786f814a3c0c285433ffe179ccb51ee0a3b0b9d4.jpg)

<details>
<summary>line</summary>

| Date       | Price($) |
| ---------- | -------- |
| Sep 23     | 100      |
| Jan 24     | 50       |
| May 24     | 100      |
| Sep 24     | 153      |
| Jan 25     | 178      |
| May 25     | 180      |
| Sep 25     | 214      |
| Jan 26     | 235      |
| May 26     | 346      |
| May 26     | 491      |
</details>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Oct 07, 2024. All share prices are as of market close on the previous business day.

<table><tr><td>Date</td><td>Rating</td><td>Price ($)</td><td>Price Target ($)</td></tr><tr><td>07-Oct-24</td><td>OW</td><td>127.13</td><td>153</td></tr><tr><td>01-Nov-24</td><td>OW</td><td>122.89</td><td>154</td></tr><tr><td>28-Jan-25</td><td>OW</td><td>130.84</td><td>172</td></tr><tr><td>28-Feb-25</td><td>OW</td><td>126.83</td><td>178</td></tr><tr><td>02-May-25</td><td>OW</td><td>134.01</td><td>180</td></tr><tr><td>22-Jul-25</td><td>OW</td><td>175.33</td><td>214</td></tr><tr><td>16-Oct-25</td><td>OW</td><td>204.56</td><td>235</td></tr><tr><td>31-Oct-25</td><td>OW</td><td>213.95</td><td>236</td></tr><tr><td>22-Jan-26</td><td>OW</td><td>243.80</td><td>267</td></tr><tr><td>27-Feb-26</td><td>OW</td><td>289.96</td><td>346</td></tr><tr><td>16-Apr-26</td><td>OW</td><td>365.07</td><td>386</td></tr><tr><td>01-May-26</td><td>OW</td><td>394.05</td><td>471</td></tr><tr><td>13-May-26</td><td>OW</td><td>420.30</td><td>491</td></tr></table>

# Disclosures

GE Vernova (GEV, GEV US) Price Chart   
![](images/5f586dd2165488c18b362056cbff90827239a70a92571b02f3800f9ecaf9903e.jpg)

<details>
<summary>line</summary>

| Date  | Price($) |
|-------|----------|
| Apr 24 | 141      |
| Jul 24 | 176      |
| Oct 24 | 216      |
| Jan 25 | 330      |
| Apr 25 | 430      |
| Jul 25 | 715      |
| Oct 25 | 740      |
| Jan 26 | 1,000    |
| Apr 26 | 1,302    |
</details>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Apr 02, 2024. All share prices are as of market close on the previous business day.

<table><tr><td>Date</td><td>Rating</td><td>Price ($)</td><td>Price Target ($)</td></tr><tr><td>02-Apr-24</td><td>N</td><td>142.02</td><td>141</td></tr><tr><td>08-Apr-24</td><td>OW</td><td>122.70</td><td>141</td></tr><tr><td>26-Apr-24</td><td>OW</td><td>148.31</td><td>163</td></tr><tr><td>23-May-24</td><td>OW</td><td>163.85</td><td>176</td></tr><tr><td>03-Jun-24</td><td>OW</td><td>175.90</td><td>186</td></tr><tr><td>16-Jul-24</td><td>OW</td><td>177.44</td><td>195</td></tr><tr><td>25-Jul-24</td><td>OW</td><td>162.90</td><td>216</td></tr><tr><td>13-Sep-24</td><td>OW</td><td>215.27</td><td>240</td></tr><tr><td>09-Oct-24</td><td>OW</td><td>264.27</td><td>285</td></tr><tr><td>24-Oct-24</td><td>OW</td><td>279.88</td><td>330</td></tr><tr><td>03-Dec-24</td><td>OW</td><td>337.54</td><td>356</td></tr><tr><td>11-Dec-24</td><td>OW</td><td>327.39</td><td>367</td></tr><tr><td>14-Jan-25</td><td>OW</td><td>366.81</td><td>374</td></tr><tr><td>23-Jan-25</td><td>OW</td><td>427.10</td><td>436</td></t

[中间内容因长度限制已省略]

are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

# Disclosures

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised April 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
