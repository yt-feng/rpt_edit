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
## US Economic Weekly

Economics - North America

## Chair Transplant

- We expect the Fed to remain on hold at the June FOMC meeting. The meeting statement will likely drop the easing bias, and we expect the dot plot medians to show rates on hold through the end of 2027.  
- We think Chair Warsh will decline to submit his own economic and policy projections. In his first press conference, Warsh may continue to downplay the usefulness of forward guidance, while hinting at a future case for rate cuts.  
- CPI and PPI inflation data point to an acceleration in core PCE inflation to $0.345\%$ m-o-m or $3.426\%$ y-o-y in May. Pipeline price pressures measured by PPI data continued to grow and point to an upside risk to the inflation outlook.

## We expect the Fed to remain on hold and remove an easing bias

The Fed will likely keep the policy rate on hold for the fourth consecutive meeting at the June FOMC meeting. Since the April meeting, economic indicators show growing inflation risks, while labor markets have stabilized with some signs of acceleration.

Fig. 1: The Fed will likely keep the policy rate on hold  
![](images/c2ae3fe51175c523d0c55c405234c7156a028f799f91036b80ce3c1edb95b94f.jpg)

<details>
<summary>line chart</summary>

| Date   | March FOMC median forecast | OIS fwd rates (as of 11 Jun) | NOM's policy rate forecast |
|--------|----------------------------|------------------------------|-------------------------------|
| Mar 23 | 4.80                       | 4.80                         | 4.80                          |
| Dec 23 | 5.40                       | 5.40                         | 5.40                          |
| Sep 24 | 4.80                       | 4.80                         | 4.80                          |
| Jun 25 | 4.40                       | 4.40                         | 4.40                          |
| Mar 26 | 3.80                       | 3.80                         | 3.80                          |
| Dec 26 | 3.60                       | 3.60                         | 3.60                          |
| Sep 27 | 3.20                       | 3.80                         | 3.60                          |
</details>

Source: FRB, Bloomberg, NOM

## Research Analysts

## North America Economics

## Aichi Amemiya - NSI

aichi.amemiya@NOM.com

+1 212 667 9347

## Jeremy Schwartz - NSI

jeremy.schwartz@NOM.com

+1 212 667 9637

## Ruchir Sharma - NSI

ruchir.sharma@NOM.com

+1 212 667 9186

## Jacklyn Goloborodsky - NSI

jacklyn.goloborodsky@NOM.com

+1 212 298 4739

## Global Economics

## David Seif - NSI

david.seif@NOM.com

+1 212 667 9180

Fig. 2: We expect Chair Warsh to acknowledge the current hawkish macroeconomic environment, but make a case for policy easing in the medium term

<table><tr><td>Tool</td><td>Key assumptions</td></tr><tr><td colspan="2">Policy rate</td></tr><tr><td>2026</td><td>No rate cuts, EOP 3.625%</td></tr><tr><td>2027</td><td>No rate cuts, EOP 3.625%</td></tr><tr><td>Terminal</td><td>3.50 - 3.75%</td></tr><tr><td colspan="2">Balance sheet policy</td></tr><tr><td>Size</td><td>Reserve management purchases of $10bn/month. The NY Fed is actively managing reserve management purchases in response to seasonal liquidity demand and market conditions. We expect balance sheet growth to average $20bn per month in the medium term.</td></tr><tr><td>Composition</td><td>MBS rundown to continue, with proceeds reinvested into Treasuries. Both reinvestments and eventual reserve management purchases will be skewed towards Treasury bills.</td></tr></table>

Source: FRB, NOM

We expect the post-meeting policy statement will remove the easing bias from the forward guidance language with unanimous support. Fedspeak has turned more hawkish recently, with several FOMC participants explicitly discussing the possibility of a rate hike. That being said, a dovish faction on the Committee remains cautiously optimistic about the inflation outlook and sees policy as moderately restrictive.

Revisions to the economic projections will likely be concentrated in the inflation outlook. We expect the median inflation projection for both the headline PCE and core PCE price indices will rise over the near term (Fig. 3). We expect policymakers will make a mark-to-market adjustment to their unemployment rate projections for 2026 and 2027, reflecting recent strength in labor markets. We expect real GDP growth projections will remain unchanged from the March meeting.

Fig. 3: We expect the median inflation projection for both headline PCE and core PCE price indices to rise over the near term NOM's forecast for the June 2026 Summary of Economic Projections

<table><tr><td></td><td></td><td>2026</td><td>2027</td><td>2028</td><td>Longer-run</td></tr><tr><td rowspan="2">Change in real GDP</td><td>Jun-26</td><td>2.4</td><td>2.3</td><td>2.1</td><td>2.0</td></tr><tr><td>Mar-26</td><td>2.4</td><td>2.3</td><td>2.1</td><td>2.0</td></tr><tr><td rowspan="2">Unemployment rate</td><td>Jun-26</td><td>4.3</td><td>4.2</td><td>4.2</td><td>4.2</td></tr><tr><td>Mar-26</td><td>4.4</td><td>4.3</td><td>4.2</td><td>4.2</td></tr><tr><td rowspan="2">PCE inflation</td><td>Jun-26</td><td>3.6</td><td>2.2</td><td>2.0</td><td>2.0</td></tr><tr><td>Mar-26</td><td>2.7</td><td>2.2</td><td>2.0</td><td>2.0</td></tr><tr><td rowspan="2">Core PCE inflation</td><td>Jun-26</td><td>3.2</td><td>2.3</td><td>2.0</td><td></td></tr><tr><td>Mar-26</td><td>2.7</td><td>2.2</td><td>2.0</td><td></td></tr><tr><td colspan="6">Projected appropriate policy path: Median</td></tr><tr><td rowspan="2"></td><td>Jun-26</td><td>3.625</td><td>3.625</td><td>3.375</td><td>3.250</td></tr><tr><td>Mar-26</td><td>3.375</td><td>3.125</td><td>3.125</td><td>3.125</td></tr></table>

Source: FRB, Haver, NOM

We do not expect Chair Warsh to submit interest rate projections for the dot plot, consistent with his past criticisms of Fed forward guidance (Fig. 4). Such an omission would reduce the total number of dots to 18 from 19. Warsh cannot unilaterally eliminate any aspects of the summary of economic projections, but there is a precedent for participants declining to submit forecasts.

We expect the median dots for 2026 and 2027 will rise to $3.625\%$ , indicating no change from the current rate level for the next one and a half years. Given that most officials have discussed multiple scenarios, it is difficult to gauge individual dots for 2026, but we expect that 4-5 dots will indicate a rate hike, 7-9 dots will correspond to no changes, and 4-6 dots will be consistent with rate cuts. We expect the median 2028 dot to be $3.375\%$ , consistent with one rate cut, and the longer-run median dot (a proxy of the neutral rate of interest) to be revised up to $3.250\%$ from $3.125\%$ , as the FOMC participants' characterization of the policy stance suggests an upward revision to their estimate of neutral rate.

Fig. 4: We think Warsh will decline to submit his interest rate projections for the dot plot, which is consistent with his past criticisms of Fed forward guidance  
NOM's expectation for policymakers' 2026 dots

<table><tr><td>%</td><td colspan="2">2026 dot as of June (NOM&#x27;s expectation)</td><td></td></tr><tr><td>3.875</td><td>Goolsbee</td><td>One rate hike</td><td>1</td></tr><tr><td>3.875</td><td>Schmid</td><td>One rate hike</td><td>2</td></tr><tr><td>3.875</td><td>Hammack</td><td>One rate hike</td><td>3</td></tr><tr><td>3.875</td><td>Musalem</td><td>One rate hike</td><td>4</td></tr><tr><td>3.875</td><td>Logan</td><td>One rate hike</td><td>5</td></tr><tr><td>3.625</td><td>Collins</td><td>No more rate cuts</td><td>6</td></tr><tr><td>3.625</td><td>Barkin</td><td>No more rate cuts</td><td>7</td></tr><tr><td>3.625</td><td>Kashkari</td><td>No more rate cuts</td><td>8</td></tr><tr><td>3.625</td><td>Barr</td><td>No more rate cuts</td><td>9</td></tr><tr><td>3.625</td><td>Venable</td><td>No more rate cuts</td><td>10</td></tr><tr><td>3.625</td><td>Cook</td><td>No more rate cuts</td><td>11</td></tr><tr><td>3.625</td><td>Waller</td><td>No more rate cuts</td><td>12</td></tr><tr><td>3.375</td><td>Jefferson</td><td>One more rate cut</td><td>13</td></tr><tr><td>3.375</td><td>Powell</td><td>One more rate cut</td><td>14</td></tr><tr><td>3.375</td><td>Daly</td><td>One more rate cut</td><td>15</td></tr><tr><td>3.375</td><td>Paulson</td><td>One more rate cut</td><td>16</td></tr><tr><td>3.375</td><td>Williams</td><td>One more rate cut</td><td>17</td></tr><tr><td>3.125</td><td>Bowman</td><td>Two more rate cuts</td><td>18</td></tr><tr><td>3.125</td><td>Warsh</td><td>Two more rate cuts</td><td>19</td></tr></table>

Source: FRB, NOM

In the press conference, we think Warsh is unlikely to call for an immediate rate cut given the current hawkish macroeconomic environment. However, we think Warsh could make a case for policy easing in the medium term, suggesting that a pause in easing is largely driven by uncertainty around the Iran war. As he did at his confirmation hearing, we expect Warsh to reiterate his view that AI will boost productivity and lead to disinflation. Warsh may also characterize currently elevated inflation as a temporary phenomenon due to the Iran war.

Warsh may continue to downplay the usefulness of core PCE inflation and instead propose alternative inflation measures. He may also discuss the possibility of balance sheet reduction, possibly laying out a roadmap or timeframe for a smaller balance sheet. In addition, he could discuss how he might make changes to the Fed's communication strategy.

## May CPI and PPI reports point to an acceleration in core PCE inflation

Incorporating CPI and PPI data, we forecast core PCE inflation of $0.345\%$ m-o-m in May from $0.23\%$ in April. This would translate into y-o-y core PCE inflation of $3.426\%$ , the highest reading since October 2023.

Fig. 5: Core PCE inflation likely accelerated in May, driven by components derived from PPI data  
Decomposition of m-o-m core PCE inflation by data source  
![](images/676b24a4bc560fdfaaf9113948e72d788da1be90d353ff2dc2e7b9b5c24cac03.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date | Other components (m-o-m %) | Contributions from components that are covered by PPI (m-o-m %) | Contributions from components that are covered by CPI (m-o-m %) | Core PCE inflation (m-o-m %) |
|---|---|---|---|---|
| Jan-23 | 0.05 | 0.15 | 0.25 | 0.45 |
| Jul-23 | -0.05 | 0.05 | 0.10 | 0.20 |
| Jan-24 | 0.05 | 0.15 | 0.25 | 0.50 |
| Jul-24 | 0.05 | 0.10 | 0.15 | 0.25 |
| Jan-25 | 0.05 | 0.15 | 0.25 | 0.45 |
| Jul-25 | 0.05 | 0.10 | 0.15 | 0.25 |
| Jan-26 | 0.05 | 0.15 | 0.25 | 0.45 |
forecast
(m o-m %)
</details>

Source: BLS, BEA, Haver, NOM

Fig. 6: Y-o-y core PCE inflation likely rose to $3.4\%$ in May  
![](images/737f1fc5bc94169dccf5f28c8cca47f384d1df66af41228e86495ecf84a4374b.jpg)

<details>
<summary>line chart</summary>

| Date    | 3-month annualized | 6-month annualized | y-o-y core PCE inflation |
|---------|--------------------|--------------------|--------------------------|
| Jan-23  | 4.8                | 5.0                | 5.0                      |
| Jul-23  | 2.0                | 3.0                | 4.0                      |
| Jan-24  | 4.8                | 3.5                | 3.0                      |
| Jul-24  | 2.0                | 3.5                | 2.8                      |
| Jan-25  | 3.8                | 3.0                | 3.0                      |
| Jul-25  | 2.5                | 3.0                | 2.8                      |
| Jan-26  | 4.8                | 4.0                | 3.5                      |
| forecast| forecast           | forecast           | forecast                 |
</details>

Source: BEA, Haver, NOM

Core CPI inflation moderated to $0.208\%$ m-o-m from $0.376\%$ in April. Core CPI goods inflation turned negative for the first time since May 2025. The tariff impact appears to have continued to wane, while inflationary pressures from global shortages of semiconductors on consumer electronics diminished. We expect core PCE goods inflation also turned negative in May. By contrast, Core CPI service inflation remained resilient. Rent-related components remained elevated, and supercore CPI components continued to increase at a decent pace. Transportation service prices (e.g., airline fares and auto insurance prices) were volatile.

Compared with our expectations, PCE-relevant PPI data were mixed, as the strength in portfolio management and investment advice prices was partially offset by an unexpected decline in domestic airline fares. CPI and PPI data suggest that supercore PCE inflation likely accelerated to 0.5% m-o-m, the highest since January 2026. Backward revisions to PPI data suggest that January core PCE inflation will likely be revised up, while March and April core PCE inflation will likely be revised down.

Details of PPI data for manufacturers' production costs and selling prices indicate upward pressure on core goods inflation in the coming months. Production costs for US manufacturers kept growing as PPI's processed materials and components for manufacturing continued to increase, in line with the recent increase in factory surveys' prices paid indices (Fig. 7).

Despite the softness in core CPI goods prices, manufacturers continued to pass higher hosts on to their consumers, as PPI for finished consumer goods excluding food and energy increased in May (Fig. 8). Regional manufacturing surveys' prices received indices also point to pass-through of higher costs into consumer product prices.

Fig. 7: Recent business surveys' show firming of prices  
Manufacturing prices paid index vs. PPI's input costs for manufacturing  
![](images/4660a5f7e3d333188f1e1b64a370b63c4285c30deb55644ed902035f4c153934.jpg)

<details>
<summary>line chart</summary>

| Date   | ISM mfg prices paid index (LHS) | S&P: US Mfg PMI: Prices paid index (LHS) | PPI: processed materials and components prices for manufacturing (RHS) |
|--------|----------------------------------|---------------------------------------------|---------------------------------------------------------------|
| Jan-18 | 75                               | 65                                          | 60                                                            |
| May-19 | 50                               | 45                                          | 55                                                            |
| Sep-20 | 90                               | 85                                          | 100                                                           |
| Jan-22 | 85                               | 80                                          | 70                                                            |
| May-23 | 40                               | 35                                          | 45                                                            |
| Sep-24 | 65                               | 60                                          | 65                                                            |
| Jan-26 | 80                               | 75                                          | 70                                                            |
</details>

Source: BLS, ISM, S&P, Haver, NOM

Fig. 8: PPI's finished consumer goods prices excluding food and energy continued to increase in May, suggesting pass-through of higher costs into consumer goods prices  
![](images/eee6d3b6d5b56c2e1cb19aade2bc8422042903f1a27dbdffa784e74cb68296ba.jpg)

<details>
<summary>line chart</summary>

| Date    | PPI: Finished Consumer Goods Less Foods & Energy (LHS) | CPI's core goods prices excluding used vehicle prices (LHS) | GDP-weighted prices received index from regional Fed factory surveys (RHS) |
|---------|--------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------------------|
| Jan-18  | ~0.3                                                   | ~0.2                                                          | ~20                                                                      |
| Jan-20  | ~0.1                                                   | ~-0.6                                                         | ~-20                                                                     |
| Jan-22  | ~1.0                                                   | ~1.0                                                          | ~50                                                                      |
| Jan-24  | ~0.2                                                   | ~-0.4                                                         | ~0                                                                       |
| Jan-26  | ~0.4                                                   | ~0.2                                                          | ~20                                                                      |
</details>

Source: BLS, BEA, NY Fed, Philly Fed, Dallas Fed, KC Fed, Haver, NOM

## Data next week

We expect retail sales rose $0.5\%$ m-o-m in May, as gasoline spending remained strong and motor vehicle sales picked up. Strong payroll income growth and higher tax refunds from the OBBBA have supported spending thus far, despite inflationary headwinds from the Iran war (Fig. 9 & Fig. 10).

Fig. 9: Strong payroll income growth has supported spending  
Aggregate private payroll income  
![](images/3ee4ba588e7699a277382dd07380b52ba9c315315c3e12446024e60fd9997214.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | %m-o-m | 3m average |
|---------|--------|----------|
| Jan-24  | 0.85   | 0.35     |
| Feb-24  | 0.48   | 0.38     |
| Mar-24  | -0.18  | 0.32     |
| Apr-24  | 0.70   | 0.30     |
| May-24  | 0.40   | 0.31     |
| Jun-24  | -0.10  | 0.33     |
| Jul-24  | 0.68   | 0.34     |
| Aug-24  | 0.45   | 0.36     |
| Sep-24  | 0.78   | 0.39     |
| Oct-24  | -0.15  | 0.37     |
| Nov-24  | 0.60   | 0.35     |
| Dec-24  | 0.52   | 0.36     |
| Jan-25  | -0.18   | 0.34     |
| Feb-25  | 0.58   | 0.38     |
| Mar-25  | 0.40   | 0.45     |
| Apr-25  | 0.18   | 0.25     |
| May-25  | 0.35   | 0.28     |
| Jun-25  | 0.40   | 0.30     |
| Jul-25  | 0.25   | 0.27     |
| Aug-25  | 0.38   | 0.31     |
| Sep-25  | 0.28   | 0.33     |
| Oct-25  | 0.78   | 0.39     |
| Nov-25  | -0.18   | 0.36     |
| Dec-25  | -0.15   | 0.38     |
| Jan-26  | -0.18   | 0.40     |
| Feb-26  | -0.15   | 0.37     |
| Mar-26  | -0.18   | 0.39     |
| Apr-26  | -0.15   | 0.36     |
| May-26  | -0.18   | 0.38     |
| Jun-26  | -0.15   | 0.37     |
| Jul-26  | -0.18   | 

[中间内容因长度限制已省略]

t of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities International, Inc., US. All rights reserved.
"""
