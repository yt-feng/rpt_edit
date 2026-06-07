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
ASIA INDEX STRATEGY

# S&P/ASX Indices Rebalancing Review and Flow Implications (June 2026)

What happened? S&P Dow Jones Indices (S&P DJI) announced its quarterly review results for the S&P/ASX Index Series after market close on June 5 (Friday). All changes will take effect after market close on June 19 (Friday).

Constituent Changes: There are 1, 1, and 5 stock changes for the S&P/ASX 50, 100, and 200 indices, respectively. For the ASX 200 index, ELV, EOS, FFM, KCN, and MI6 will replace GYG, IEL, SDR, TPW, and WEB. Overall, around $0.3\%$ of ASX 200 index weights will be adjusted. (Exhibit 3)

Index Implications: The proforma index cap is estimated at US\$1,873 billion for ASX 200. Following the rebalancing, forward 12-month P/E is expected to shift from 16.6x to 16.7x, trailing dividend yield will remain unchanged at 3.5%, and EPS growth (2026-27 CAGR) will change from 13.7% to 13.9% for ASX200. (Exhibit 1)

Sector Implications: Metals & Mining (+US\$80mn) and Capital Goods (+US\$50mn) are poised to see the largest passive inflows, while Consumer Retail (-US\$80mn) may face the biggest outflows. Overall, we estimate that the S&P/ASX rebalancing could generate over US\$900mn of gross two-way passive trading flows. (Exhibit 4)

Historical vs. Current Patterns: ASX 200 additions vs. deletions have traded along a highly volatile path ahead of the announcement; historically, post-announcement performance remains volatile with a modest negative bias, before rebounding around the effective date. (Exhibit 2)

We highlight the index and sector changes, as well as the passive flow implications for stock additions and deletions.

Alvin So, CFA

+852-2978-1585 | alvin.so@gs.com

GS (Asia) L.L.C.

Timothy Moe, CFA

+65-6889-1199 | timothy.moe@gs.com

GS (Singapore) Pte

Matthew Ross

+61(3)9679-1616

matthew.ross@gs.com

GS Australia Pty Ltd

Tony Wu

+61(3)9679-1402 | tony.wu@gs.com

GS Australia Pty Ltd

Exhibit 1: S&P DJI has announced its quarterly review results for the S&P/ASX Index Series, effective after market close on June 19 (Friday)

<table><tr><td rowspan="2"></td><td rowspan="2">S&amp;P/ASX Indices</td><td colspan="3">Jun 2026 Review Summary</td></tr><tr><td>ASX 50</td><td>ASX Mid-Cap 50</td><td>ASX 200</td></tr><tr><td rowspan="3">Stock Changes</td><td>Current # Constituents</td><td>50</td><td>50</td><td>200</td></tr><tr><td># Stocks Added / Deleted</td><td>1 / 1</td><td>2 / 2</td><td>5 / 5</td></tr><tr><td>% Weight Rebalanced</td><td>0.6%</td><td>4.9%</td><td>0.3%</td></tr><tr><td rowspan="4">Liquidity</td><td>Current Index Cap (US$bn)</td><td>1,489</td><td>231</td><td>1,872</td></tr><tr><td>Proforma % Change</td><td>+0.1%</td><td>-0.6%</td><td>+0.0%</td></tr><tr><td>Current 3M ADVT (US$bn)</td><td>3.7</td><td>1.0</td><td>5.5</td></tr><tr><td>Proforma % Change</td><td>-0.1%</td><td>+1.8%</td><td>+0.6%</td></tr><tr><td rowspan="3">Valuations / Growth</td><td>NTM P/E (x)(Current / Proforma)</td><td>17.2x /17.1x</td><td>15.3x /15.6x</td><td>16.6x /16.7x</td></tr><tr><td>LTM Dividend Yield (%) (Current / Proforma)</td><td>3.6% /3.6%</td><td>3.0% /3.0%</td><td>3.5% /3.5%</td></tr><tr><td>2026-27 EPS Growth (%) (Current / Proforma)</td><td>10.3% /10.3%</td><td>19.9% /20.8%</td><td>13.7% /13.9%</td></tr><tr><td>Passive Flows</td><td>Potential Gross Passive Buying + Selling (Two-way) (US$mn)</td><td>9</td><td>57</td><td>490</td></tr><tr><td rowspan="2">Trading Pattern Prior to Announce.</td><td>Return Since 10D Prior to Ann.(Additions / Deletions)</td><td>-1.5% /+29.5%</td><td>+14.6% /-0.9%</td><td>-12.2% /-5.5%</td></tr><tr><td>Share Turnover % Chg (Median 20D vs.Prior 3M) (Add / Del)</td><td>+8% /-21%</td><td>-8% /+6%</td><td>+0% /+53%</td></tr></table>

Note: Pricing is as of Jun 5, 2026  
Source: S&P/ASX, Bloomberg, FactSet, Refinitiv, EPFR, GS Global Investment Research

Exhibit 2: ASX 200: Additions vs. deletions have traded along a highly volatile path ahead of the announcement; historically, post-announcement performance remains volatile with a modest negative bias, before rebounding around the effective date

![](images/c2979a8128919d44f9e2a4642dc87b9015f3026f8e7fbb74bb614baae3684d40.jpg)

<details>
<summary>line chart</summary>

| # workdays before/after index review announcement date | Past Add/Del Median | Current (5-Jun-26) |
| ----------------------------------------------------- | ------------------- | ------------------ |
| -20                                                   | 103                 | 88                 |
| -15                                                   | 101                 | 104                |
| -10                                                   | 101                 | 107                |
| -5                                                    | 101                 | 108                |
| 0                                                     | 100                 | 100                |
| 5                                                     | 100                 | 100                |
| 10                                                    | 99                  | 100                |
| 15                                                    | 101                 | 100                |
| 20                                                    | 101                 | 100                |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 3: Stocks that may experience net passive buying or selling flows following the S&P/ASX indices rebalancing (only additions and deletions are shown)

<table><tr><td rowspan="2">BBG Ticker</td><td rowspan="2">Company Name</td><td rowspan="2">Sector</td><td rowspan="2">Listed Mkt Cap (US$mn)</td><td rowspan="2"># Free Float Cap (US$mn)</td><td rowspan="2">3M ADVT (US$mn)</td><td colspan="3">Potential Passive Flows (US$mn)</td><td rowspan="2">Net Passive Flows (US$mn)</td><td rowspan="2">Net Flows /3M ADVT (days)</td><td rowspan="2">S3&#x27;s Short Interest 20D Chg (pp)</td><td rowspan="2">Days to Cover (1M ADVT)</td><td rowspan="2">S3&#x27;s HF Long Interest 20D Chg (pp)</td><td rowspan="2">Return since 20D prior to ann.</td><td rowspan="2">Return since 10D prior to ann.</td><td rowspan="2">Share Turnover % Chg (Median 20D vs. Prior 3M)</td><td colspan="2">Corporate Event Dates</td></tr><tr><td>ASX 50</td><td>ASX Mid. Cap 50</td><td>ASX 200</td><td>Expected Next Report</td><td>Ex-Dividend</td></tr><tr><td colspan="6">Stocks with net passive buying following S&amp;P/ASX indices rebalancing (Additions)</td><td colspan="3">(Additions Only)</td><td colspan="2">(ranked)</td><td colspan="8"></td></tr><tr><td>ELV AT</td><td>Elevra Lithium</td><td>Metals &amp; Mining</td><td>1,592</td><td>1,353</td><td>15</td><td>-</td><td>-</td><td>53</td><td>54</td><td>3.5</td><td>(3.2%)</td><td>2.0</td><td>0.0%</td><td>(18%)</td><td>(20%)</td><td>63%</td><td>Aug 31</td><td></td></tr><tr><td>EOS AT</td><td>Electro Optic Systems</td><td>Capital Goods</td><td>1,633</td><td>1,345</td><td>23</td><td>-</td><td>-</td><td>53</td><td>54</td><td>2.3</td><td>-</td><td>-</td><td>0.0%</td><td>23%</td><td>24%</td><td>5%</td><td>Aug 20</td><td></td></tr><tr><td>MI6 AT</td><td>Minerals 260</td><td>Metals &amp; Mining</td><td>1,385</td><td>1,095</td><td>6</td><td>-</td><td>-</td><td>43</td><td>43</td><td>7.7</td><td>0.2%</td><td>4.1</td><td>-</td><td>(3%)</td><td>(8%)</td><td>0%</td><td>Sep 29</td><td></td></tr><tr><td>FFM AT</td><td>FireFly Metals Ltd</td><td>Metals &amp; Mining</td><td>1,142</td><td>1,087</td><td>7</td><td>-</td><td>-</td><td>43</td><td>43</td><td>6.1</td><td>0.8%</td><td>8.3</td><td>(0.2%)</td><td>3%</td><td>0%</td><td>(19%)</td><td>Sep 8</td><td></td></tr><tr><td>KCN AT</td><td>Kingsgate Consolidated</td><td>Metals &amp; Mining</td><td>1,007</td><td>956</td><td>7</td><td>-</td><td>-</td><td>37</td><td>38</td><td>5.3</td><td>0.0%</td><td>1.2</td><td>0.0%</td><td>(28%)</td><td>(16%)</td><td>(17%)</td><td>Mar 4</td><td></td></tr><tr><td>PME AT</td><td>Pro Medicus</td><td>Health Care</td><td>11,878</td><td>6,549</td><td>32</td><td>(3)</td><td>17</td><td>-</td><td>14</td><td>0.4</td><td>1.0%</td><td>13.6</td><td>0.1%</td><td>28%</td><td>29%</td><td>(21%)</td><td>Aug 14</td><td></td></tr><tr><td>PDN AT</td><td>Paladin Energy</td><td>Energy</td><td>3,491</td><td>3,491</td><td>23</td><td>-</td><td>9</td><td>-</td><td>5</td><td>0.2</td><td>1.5%</td><td>17.8</td><td>0.2%</td><td>(12%)</td><td>(0%)</td><td>6%</td><td>Aug 28</td><td></td></tr><tr><td colspan="6">Stocks with net passive selling following S&amp;P/ASX indices rebalancing (Deletions)</td><td colspan="3">(Deletions Only)</td><td colspan="2">(ranked)</td><td colspan="8"></td></tr><tr><td>GYG AT</td><td>Guzman y Gomez</td><td>Consumer Retail &amp; Services</td><td>1,359</td><td>747</td><td>6</td><td>-</td><td>-</td><td>(29)</td><td>(29)</td><td>(5.1)</td><td>(1.0%)</td><td>27.9</td><td>0.0%</td><td>1%</td><td>(6%)</td><td>55%</td><td>Aug 24</td><td></td></tr><tr><td>SDR AT</td><td>SiteMinder</td><td>Software &amp; Services</td><td>776</td><td>713</td><td>4</td><td>-</td><td>-</td><td>(28)</td><td>(28)</td><td>(7.1)</td><td>(1.0%)</td><td>9.8</td><td>0.0%</td><td>23%</td><td>38%</td><td>(10%)</td><td>Aug 27</td><td></td></tr><tr><td>WEB AT</td><td>WEB Travel</td><td>Consumer Retail &amp; Services</td><td>623</td><td>614</td><td>6</td><td>-</td><td>-</td><td>(24)</td><td>(24)</td><td>(4.2)</td><td>0.8%</td><td>5.9</td><td>0.0%</td><td>(13%)</td><td>3%</td><td>56%</td><td>Nov 18</td><td></td></tr><tr><td>ALQ AT</td><td>ALS</td><td>Capital Goods</td><td>8,596</td><td>8,585</td><td>26</td><td>5</td><td>(22)</td><td>-</td><td>(17)</td><td>(0.6)</td><td>0.3%</td><td>3.2</td><td>0.0%</td><td>6%</td><td>(1%)</td><td>8%</td><td>Nov 23</td><td>Jun 12</td></tr><tr><td>IEL AT</td><td>IDP Education</td><td>Consumer Retail &amp; Services</td><td>409</td><td>396</td><td>6</td><td>-</td><td>-</td><td>(16)</td><td>(16)</td><td>(2.5)</td><td>0.3%</td><td>2.7</td><td>0.0%</td><td>(30%)</td><td>(25%)</td><td>53%</td><td>Aug 20</td><td></td></tr><tr><td>TPW AT</td><td>Temple &amp; Webster</td><td>Consumer Retail &amp; Services</td><td>408</td><td>327</td><td>6</td><td>-</td><td>-</td><td>(13)</td><td>(13)</td><td>(2.3)</td><td>1.5%</td><td>5.7</td><td>(0.0%)</td><td>(21%)</td><td>(8%)</td><td>48%</td><td>Aug 18</td><td></td></tr><tr><td>MTS AT</td><td>Metcash</td><td>Consumer Staples</td><td>2,379</td><td>2,379</td><td>11</td><td>-</td><td>(6)</td><td>-</td><td>(6)</td><td>(0.5)</td><td>0.3%</td><td>7.5</td><td>0.0%</td><td>11%</td><td>(0%)</td><td>4%</td><td>Jun 22</td><td></td></tr><tr><td rowspan="2"></td><td colspan="2">ASX 200 Median</td><td>3,733</td><td>2,770</td><td>14</td><td rowspan="2" colspan="8"></td><td>(1%)</td><td>(0%)</td><td>(6%)</td><td rowspan="2" colspan="2"></td></tr><tr><td colspan="2">ASX 300 Median</td><td>1,808</td><td>1,324</td><td>6</td><td>(2%)</td><td>0%</td><td>(4%)</td></tr></table>

Note (1): Free Float Cap is calculated based on ASX-registered share assumptions prior to the current index review, and the average free float % estimates from Bloomberg, FactSet, and Refinitiv. Pricing is as of Jun 5, 2026
Note (2): Passive fund AUM is derived from EPFR and FactSet ownership data, along with our estimation of identifiable index-tracking portions from non-public funds.  
Source: S&P/ASX, FactSet, Refinitiv, Bloomberg, EPFR, GS Global Investment Research

Exhibit 4: Metals & Mining and Capital Goods are poised to see the largest passive inflows, while Consumer Retail may face the biggest outflows  
Current vs. Proforma Sector Weights and Changes in Major S&P/ASX Indices, and Aggregate Potential Passive Flows

<table><tr><td rowspan="2" colspan="2">GICS Sector/Industry</td><td colspan="4">ASX 50</td><td colspan="4">ASX Mid-Cap 50</td><td colspan="3">ASX 200</td><td colspan="3">Passive Flows (US$mn)</td><td></td></tr><tr><td>Current %</td><td>Proforma %</td><td colspan="2">Change (bps)</td><td>Current %</td><td>Proforma %</td><td colspan="2">Change (bps)</td><td>Current %</td><td>Proforma %</td><td>Change (bps)</td><td>Gross Buying</td><td>Gross Selling</td><td>Net Flows</td><td></td></tr><tr><td rowspan="2">Financials</td><td>Banks</td><td>28.9%</td><td>28.9%</td><td></td><td>-2</td><td>3.0%</td><td>3.0%</td><td></td><td>+2</td><td>23.4%</td><td>23.4%</td><td></td><td>-1</td><td>32</td><td>-5</td><td>27</td></tr><tr><td>Insurance &amp; Other Financials</td><td>9.2%</td><td>9.2%</td><td></td><td>-1</td><td>7.4%</td><td>7.4%</td><td></td><td>-6</td><td>9.2%</td><td>9.1%</td><td></td><td>-2</td><td>12</td><td>-36</td><td>-24</td></tr><tr><td></td><td>Real Estate</td><td>4.8%</td><td>4.8%</td><td></td><td>-0</td><td>9.8%</td><td>9.9%</td><td></td><td>+5</td><td>5.9%</td><td>5.9%</td><td></td><td>-0</td><td>10</td><td>-5</td><td>5</td></tr><tr><td rowspan="7">Domestic / Global Cyclicals</td><td>Capital Goods</td><td>2.0%</td><td>2.6%</td><td></td><td>+57</td><td>11.5%</td><td>7.8%</td><td></td><td>368</td><td>4.0%</td><td>4.1%</td><td></td><td>+7</td><td>69</td><td>-24</td><td>45</td></tr><tr><td>Transportation</td><td>2.9%</td><td>2.9%</td><td></td><td>-0</td><td>6.6%</td><td>6.6%</td><td></td><td>+3</td><td>3.3%</td><td>3.3%</td><td></td><td>-1</td><td>4</td><td>-10</td><td>-6</td></tr><tr><td>Autos &amp; Components</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>0.1%</td><td>0.1%</td><td></td><td>-0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Consumer Retail &amp; Services</td><td>6.8%</td><td>6.8%</td><td></td><td>-1</td><td>3.7%</td><td>3.7%</td><td></td><td>+1</td><td>6.6%</td><td>6.5%</td><td></td><td>-12</td><td>7</td><td>-88</td><td>-80</td></tr><tr><td>Tech Hardware &amp; Semis</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>0.2%</td><td>0.2%</td><td></td><td>-0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Software &amp; Services</td><td>1.1%</td><td>1.0%</td><td></td><td>-0</td><td>7.9%</td><td>8.0%</td><td></td><td>+4</td><td>2.1%</td><td>2.0%</td><td></td><td>-4</td><td>3</td><td>-29</td><td>-26</td></tr><tr><td>Internet/Media &amp; Entertainment</td><td>0.5%</td><td>0.5%</td><td></td><td>-0</td><td>3.9%</td><td>3.9%</td><td></td><td>-3</td><td>1.0%</td><td>1.0%</td><td></td><td>-1</td><td>0</td><td>-14</td><td>-14</td></tr><tr><td rowspan="3">Commodities</td><td>Energy</td><td>4.0%</td><td>4.0%</td><td></td><td>-0</td><td>5.1%</td><td>6.6%</td><td></td><td>156</td><td>4.6%</td><td>4.6%</td><td></td><td>-1</td><td>15</td><td>-19</td><td>-4</td></tr><tr><td>Metals &amp; Mining</td><td>26.3%</td><td>26.3%</td><td></td><td>-7</td><td>20.9%</td><td>21.1%</td><td></td><td>+12</td><td>25.7%</td><td>25.9%</td><td></td><td>+15</td><td>215</td><td>-143</td><td>72</td></tr><tr><td>Chemicals &amp; Other Materials</td><td>0.5%</td><td>0.5%</td><td></td><td>-0</td><td>7.4%</td><td>7.5%</td><td></td><td>+13</td><td>1.4%</td><td>1.4%</td><td></td><td>+1</td><td>20</td><td>-1</td><td>19</td></tr><tr><td></td><td>Consumer Staples</td><td>3.5%</td><td>3.5%</td><td></td><td>-0</td><td>4.8%</td><td>3.7%</td><td></td><td>103</td><td>3.5%</td><td>3.5%</td><td></td><td>-0</td><td>5</td><td>-10</td><td>-6</td></tr><tr><td rowspan="3">Defensives</td><td>Health Care</td><td>5.1%</td><td>4.6%</td><td></td><td>-46</td><td>6.5%</td><td>9.3%</td><td></td><td>283</td><td>5.0%</td><td>5.0%</td><td></td><td>-2</td><td>23</td><td>-47</td><td>-24</td></tr><tr><td>Utilities</td><td>1.6%</td><td>1.6%</td><td></td><td>-0</td><td>1.6%</td><td>1.6%</td><td></td><td>+1</td><td>1.4%</td><td>1.4%</td><td></td><td>-0</td><td>2</td><td>0</td><td>2</td></tr><tr><td>Telecommunication Services</td><td>2.7%</td><td>2.7%</td><td></td><td>-0</td><td>0.0%</td><td>0.0%</td><td></td><td>+0</td><td>2.5%</td><td>2.5%</td><td></td><td>+1</td><td>16</td><td>-2</td><td>14</td></tr></table>

Note: Proforma changes reflect additions and deletions. Pricing is as of Jun 5, 2026  
Source: S&P/ASX, FactSet, Refinitiv, EPFR, GS Global Investment Research

## Disclosure Appendix

## Reg AC

I, Matthew Ross, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

We, Alvin So, CFA, Timothy Moe, CFA and Tony Wu, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Alvin So, CFA GS (Asia) L.L.C., Timothy Moe, CFA GS (Singapore) Pte, Matthew Ross GS Australia Pty Ltd, Tony Wu GS Australia Pty Ltd.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subj

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
