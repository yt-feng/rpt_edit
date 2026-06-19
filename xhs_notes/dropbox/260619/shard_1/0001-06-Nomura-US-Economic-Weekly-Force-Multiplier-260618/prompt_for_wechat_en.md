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

## Force Multiplier

- The FOMC kept rates on hold at their June meeting. The dot plot and economic projections were hawkish, while Chair Warsh's press conference signaled his dovish tilt. The risk of rate hikes has increased, but we continue to expect the Fed will remain on hold through the end of 2027.  
- Warsh announced the creation of five new task forces to revamp the Fed, focusing on communication, data measurement, balance sheet policy, productivity, and inflation frameworks. He indicated that he will likely announce personnel in the next few weeks, with task force recommendations targeted for year-end.  
- Incorporating CPI, PPI, and import prices, we expect core PCE inflation accelerated by $0.376\%$ m-o-m in May. This translates into y-o-y core PCE inflation of $3.457\%$ .  
- The US and Iran have announced a preliminary agreement to end the war, during which negotiations are expected to continue on unresolved issues, including sanctions relief and the future of Iran's nuclear program.

The FOMC kept rates on hold at their June meeting (Fig. 1). The dot plot and economic projections were hawkish. Chair Warsh's press conference, however, signaled his dovish bias. Overall, we maintain our expectation of no changes to the policy rate through the end of 2027 (Fig. 2).

Fig. 1: The FOMC kept rates on hold at their June meeting  
![](images/a89076857f74247bd892767245ee23229441f57fbfdd05d6434eb57507eefc86.jpg)

<details>
<summary>line chart</summary>

| Date   | June FOMC median forecast | OIS fwd rates (as of 17 Jun) | NOM's policy rate forecast |
|--------|---------------------------|------------------------------|-------------------------------|
| Mar 23 | 4.80                      | -                            | 4.90                          |
| Dec 23 | 5.40                      | -                            | 5.40                          |
| Sep 24 | 4.80                      | -                            | 4.90                          |
| Jun 25 | 4.40                      | -                            | 4.40                          |
| Mar 26 | 3.70                      | -                            | 3.70                          |
| Dec 26 | 3.80                      | 4.00                         | 3.70                          |
| Sep 27 | 3.70                      | 4.00                         | 3.70                          |
</details>

Source: FRB, Bloomberg, NOM

## Research Analysts

## North America Economics

Aichi Amemiya - NSI

aichi.amemiya@NOM.com

+1 212 667 9347

Jeremy Schwartz - NSI

jeremy.schwartz@NOM.com

+1 212 667 9637

Ruchir Sharma - NSI

ruchir.sharma@NOM.com

+1 212 667 9186

Jacklyn Goloborodsky - NSI

jacklyn.goloborodsky@NOM.com

+1 212 298 4739

## Global Economics

David Seif - NSI

david.seif@NOM.com

+1 212 667 9180

Fig. 2: We maintain our expectation of no changes to the policy rate through the end of 2027

<table><tr><td>Tool</td><td>Key assumptions</td></tr><tr><td colspan="2">Policy rate</td></tr><tr><td>2026</td><td>No rate cuts, EOP 3.625%</td></tr><tr><td>2027</td><td>No rate cuts, EOP 3.625%</td></tr><tr><td>Terminal</td><td>3.50 - 3.75%</td></tr><tr><td colspan="2">Balance sheet policy</td></tr><tr><td>Size</td><td>Reserve management purchases of $10bn/month. The NY Fed is actively managing reserve management purchases in response to seasonal liquidity demand and market conditions. We expect balance sheet growth to average $20bn per month in the medium term.</td></tr><tr><td>Composition</td><td>MBS rundown to continue, with proceeds reinvested into Treasuries. Both reinvestments and eventual reserve management purchases will be skewed towards Treasury bills.</td></tr></table>

Source: FRB, NOM

## The dot plot and economic projections became more hawkish

The June dot plot was more hawkish than expected, as the median 2026 dot indicated half a rate hike (3.750%) from the current level of 3.625% (NOM and Consensus: 3.625%) (Fig. 3). Although Chair Warsh did not submit his own dots, nine out of a total 18 dots were consistent with at least one rate hike in 2026, and only one participant, likely Governor Bowman, believed a rate cut in 2026 was appropriate, with the rest expecting no changes.

Beyond 2026, the median 2027-2028 dots were in line with our expectations (3.625% for

Production Complete: 2026-06-18 19:13 UTC

2027 and $3.375\%$ for 2028), but higher than the consensus forecasts (Consensus: $3.375\%$ for 2027 and $3.125\%$ for 2028). In the medium term, most FOMC participants believed some policy easing would be appropriate, allowing the policy rate to converge toward neutral. One dovish surprise was a slight decline in the median longer-run dot, which unexpectedly fell to $3.063\%$ from $3.125\%$ previously. However, the mean of the longer-run dots moved higher to $3.208\%$ from $3.164\%$ previously. The dispersed distribution of longer-run dots indicates a wide range of views on the neutral rate.

Note that one unidentified participant (in addition to Warsh) did not submit a dot for 2028, leaving the total number of 2028 dots at 17. We think it could be former Chair Powell, whose term as a governor expires in January 2028.

The Summary of Economic Projections was also hawkish on net, as the median projections for core PCE inflation for 2026-2028 were revised up, which suggests many FOMC participants expected some lingering price pressures.

Fig. 3: The dot plot was more hawkish than expected  
The December dot plot  
![](images/6d2ef918e4054828c0b4cbff53382fc078f2b2c7e4cfb397a4e88e9588d056ad.jpg)

<details>
<summary>scatterplot</summary>

| Date | Mar SEP | June SEP |
| --- | --- | --- |
| 2026-01 | 3.4 | 3.9 |
| 2026-02 | 3.4 | 3.9 |
| 2026-03 | 3.4 | 3.9 |
| 2026-04 | 3.4 | 3.9 |
| 2026-05 | 3.4 | 3.9 |
| 2026-06 | 3.4 | 3.9 |
| 2026-07 | 3.4 | 3.9 |
| 2026-08 | 3.4 | 3.9 |
| 2026-09 | 3.4 | 3.9 |
| 2026-10 | 3.4 | 3.9 |
| 2026-11 | 3.4 | 3.9 |
| 2026-12 | 3.4 | 3.9 |
| 2027-01 | 3.4 | 3.9 |
| 2027-02 | 3.4 | 3.9 |
| 2027-03 | 3.4 | 3.9 |
| 2027-04 | 3.4 | 3.9 |
| 2027-05 | 3.4 | 3.9 |
| 2027-06 | 3.4 | 3.9 |
| 2027-07 | 3.4 | 3.9 |
| 2027-08 | 3.4 | 3.9 |
| 2027-09 | 3.4 | 3.9 |
| 2027-10 | 3.4 | 3.9 |
| 2027-11 | 3.4 | 3.9 |
| 2027-12 | 3.4 | 3.9 |
| Longer run | Mar SEP | June SEP |
| Longer run | Mar SEP | June SEP |
| Longer run | Mar SEP | June SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
| Longer run | Mar SEP | Jun SEP |
</details>

Source: FRB, NOM

## Simplified policy statement with assurance of continuing the ample-reserve system

Chair Warsh successfully simplified the meeting statement, which was significantly shorter than previously. It mentioned the policy decision and the Fed's assessment on economic activity and inflation but omitted any forward-looking elements. Importantly, the statement explicitly noted the Fed's intention to maintain "ample" reserves, which confirmed no imminent changes to balance sheet policy.

## Warsh's press conference hinted at dovishness

While economic and monetary policy projections were hawkish on net, Warsh's comments signaled his dovish tilt.

Despite the significant hawkish shift in the 2026 dot plot, he downplayed its importance. He said “all the submissions [of the dots] were coming in with pencils—those kinds with big erasers,” suggesting the dots could be revised drastically if the macroeconomic environment changes. Moreover, he suggested a false symmetry in the dot plot, saying “half of my colleagues thought the policy rate… should be at this level or lower between now and year-end,” although only one participant expected a rate cut this year.

Moreover, when asked about the Fed's $2\%$ inflation target, he said, "I tend to focus on the left of the decimal point," which suggests he might consider inflation of $2.0 - 2.9\%$ as consistent with the Fed's $2\%$ target.

In addition, Warsh described the restrictiveness of monetary policy as “uneven,” contrasting weak housing markets, whereby interest rates are suppressing growth, with financial markets, which have been strong despite relatively high interest rates. He attributed the unevenness to “whether monetary policy is coming from our interest rate tool or our balance sheet tool.” This suggests that he appears to see the policy rate as

restrictive, while balance sheet policy supports financial markets.

Another dovish element of his press conference was his comments on a conventional trade-off between the Fed's dual mandate – price stability and maximum employment. He said that he did not believe the existence of “a cruel choice” between the two, and “we can make strong growth, low prices, and strong employment mutually compatible.”

## Focus is on the five task forces

Warsh announced the establishment of task forces focusing on five areas: Fed communication, balance sheet policy, the use of and reliance on existing data sources, productivity and jobs, and inflation frameworks. Warsh avoided giving direct answers to many questions from reporters by deferring to future work by those task forces.

Warsh said that he is in the process of recruiting task force members and expects them to begin work “in the next couple of weeks,” provide some insights “starting in the fall,” and that “hopefully most, if not all,” conclude “by year-end.” Although inflation risks are at the center of discussion on the Committee, one of those task forces is aimed at reviewing how the Fed should gauge inflation, suggesting that the bar to a hike might be higher until those task forces provide policy proposals later this year.

Moreover, Warsh said that he is “enlisting” economists for the task forces, raising the possibility that the task forces will deliver dovish recommendations that may not have the support of a majority of the FOMC.

For instance, at his press conference, Warsh criticized federal government statistics, saying most of them “come with old-fashioned survey methods.” Instead, he favored “real-time” data and was eager to incorporate new data collection techniques from the private sector. Although former Chair Powell previously highlighted some issues caused by low response rates for some key survey-based data, most policymakers have said that they consider statistics from federal statistical agencies as the “gold-standard” of economic data.

Some FOMC participants might not accept any task force recommendations that emphasize alternative inflation data because their recommendations could be considered as an opportunistic shift in the inflation target. Note that FOMC participants pushed back against Warsh's preference for the PCE trimmed-mean inflation measure recently.

Fig. 4: PCE trimmed-mean inflation appears to understate the underlying inflation trend  
PCE trimmed-mean inflation: official vs. bias-adjusted  
![](images/ea7390c823136b4cc37bc9394cfdaa8227c2adcb748579d0a612064a69471ff2.jpg)

<details>
<summary>line chart</summary>

| Year | Bias-adjusted PCE trimmed-mean inflation | PCE trimmed-mean inflation | Core PCE inflation |
|------|------------------------------------------|-----------------------------|--------------------|
| 2006 | 2.5                                      | 2.8                         | 2.4                |
| 2010 | 1.5                                      | 1.0                         | 0.7                |
| 2014 | 1.2                                      | 1.8                         | 1.5                |
| 2018 | 1.8                                      | 2.0                         | 1.9                |
| 2022 | 5.5                                      | 5.0                         | 5.8                |
| 2026 | 2.8                                      | 2.3                         | 3.2                |
</details>

Source: BEA, Dallas Fed, Haver, NOM

## Core PCE likely accelerated in May

Incorporating relevant details from CPI, PPI, and import prices, we expect core PCE inflation accelerated to $0.376\%$ m-o-m in May from a revised $0.230\%$ in April. This forecast along with expected backward revisions translates into $3.457\%$ y-o-y core PCE inflation in May from a revised $3.307\%$ in April (Fig. 5).

Core CPI inflation moderated and core CPI goods inflation turned negative in May for the first time since May 2025. We expect core PCE goods inflation also turned negative in May. The increase in core PCE inflation was likely driven by components derived from PPI data. In particular, PPI financial service prices rose strongly. Additionally, import prices for air passenger fares, an input into PCE's price index for passenger fares for foreign travel, jumped sharply and pushed up our estimate for core PCE inflation. As a result, we expect supercore PCE inflation accelerated strongly to $0.5\%$ m-o-m in May, the highest since January (Fig. 6).

Fig. 5: Y-o-y core PCE inflation likely rose to 3.457% in May  
![](images/f91438700012d17172648e0912b2ac6cf64f59778f68e30561da8b2b3aec984f.jpg)

<details>
<summary>line chart</summary>

| Date   | 3-month annualized | 6-month annualized | y-o-y core PCE inflation |
|--------|--------------------|--------------------|--------------------------|
| Jan-23 | 4.8                | 5.1                | 5.0                      |
| Jul-23 | 3.8                | 4.2                | 4.5                      |
| Jan-24 | 1.8                | 2.0                | 3.0                      |
| Jul-24 | 2.0                | 3.5                | 2.8                      |
| Jan-25 | 3.9                | 3.0                | 2.9                      |
| Jul-25 | 2.1                | 3.1                | 2.7                      |
| Jan-26 | 4.9                | 3.8                | 3.3                      |
| forecast | 3.5              | 4.1                | 3.4                      |
</details>

Source: BEA, Haver, NOM

Fig. 6: Supercore PCE inflation likely accelerated sharply in May, driven by a rebound in financial service prices  
![](images/ca44c1786cd934ecc628503e35dc174cd0c77860807c37b7046381578c3f669d.jpg)

<details>
<summary>stacked bar chart</summary>

m-o-m supercore PCE inflation
| Date | Airline fares (%) | Others (%) | Food services and accommodations (%) | Healthcare (%) | Financial services (%) | Supercore PCE inflation |
|---|---|---|---|---|---|---|
| Jan-24 | 0.05 | 0.15 | 0.08 | 0.12 | 0.25 | 0.75 |
| Jul-24 | -0.05 | 0.10 | 0.05 | 0.08 | 0.15 | 0.35 |
| Jan-25 | -0.08 | 0.12 | 0.06 | 0.10 | 0.20 | 0.50 |
| Jul-25 | 0.02 | 0.18 | 0.07 | 0.11 | 0.18 | 0.32 |
| Jan-26 | 0.03 | 0.25 | 0.10 | 0.13 | 0.15 | 0.55 |
| forecast | -0.15 | -0.18 | -0.12 | -0.15 | -0.18 | -0.15 |
</details>

Source: BEA, BLS, Haver, NOM

## Data next week will likely show the economy's resilience

The data which are scheduled for release next week will likely show the economy's resilience. Excluding the volatile transportation equipment component, we expect durable goods orders to have continued to rise at a decent pace of $0.6\%$ m-o-m in May, reflecting the positive impact from the AI investment boom. The S&P manufacturing PMI likely inched down in June, but remained at a healthy level. We expect personal income and spending increased robustly and inflation-adjusted personal spending growth was slightly positive in May. The third estimate of Q1 GDP will likely be revised higher from the second estimate due to an upward revision to net exports.

## Q2 GDP tracking was revised up due to stronger-than-expected retail sales

We have revised our Q2 GDP tracking estimate to 2.6% q-o-q ar from 2.4% last week. Our estimate for real final sales to private domestic purchasers now stands at 2.8% from 2.7% previously. Retail sales rose 0.9% m-o-m in May, and the "control" group of retail sales also continued to grow at a decent pace of 0.7% m-o-m. The broad strength in retail sales pushed up the contribution from the PCE component of GDP, offsetting the impact of weaker-than-expected housing starts in May.

## Iran war update

President Trump signed the memorandum of understanding ending the war with Iran on 17 June. The MOU includes opening the Strait of Hormuz and extending the ceasefire for 60 days, during which the US and Iran plan to negotiate a finalized deal. Crude oil prices dropped sharply in reaction to the agreement. Retail gasoline prices have been declining recently, which will likely weigh on headline inflation in June.

Fig. 7: NOM's inflation forecasts

<table><tr><td rowspan="2"></td><td colspan="2">Headline PCE</td><td colspan="3">Core PCE</td><td colspan="2">Headline CPI</td><td colspan="3">Core CPI</td><td>CPI NSA</td></tr><tr><td>m/m %</td><td>y/y %</td><td>m/m %</td><td>y/y %</td><td>qtrly, y/y %</td><td>m/m %</td><td>y/y %</td><td>m/m %</td><td>y/y %</td><td>qtrly, y/y %</td><td>Index</td></tr><tr><td>Jan-25</td><td>0.35</td><td>2.61</td><td>0.31</td><td>2.78</td><td></td><td>0.43</td><td>3.00</td><td>0.43</td><td>3.26</td><td></td><td>317.671</td></tr><tr><td>Feb-25</td><td>0.40</td><td>2.71</td><td>0.45</td><td>2.97</td><td></td><td>0.23</td><td>2.82</td><td>0.25</td><td>3.12</td><td></td><td>319.082</td></tr><tr><td>Mar-25</td><td>0.02</td><td>2.36</td><td>0.10</td><td>2.67</td><td>2.81</td><td>0.03</td><td>2.39</td><td>0.07</td><td>2.79</td><td>3.08</td><td>319.799</td></tr><tr><td>Apr-25</td><td>0.17</td><td>2.28</td><td>0.19</td><td>2.61</td><td></td><td>0.16</td><td>2.31</td><td>0.24</td><td>2.78</td><td></td><td>320.795</td></tr><tr><td>May-25</td><td>0.18</td><td>2.46</td><td>0.23</td><td>2.78</td><td></td><td>0.10</td><td>2.35</td><td>0.13</td><td>2.79</td><td></td><td>321.465</td></tr><tr><td>Jun-25</td><td>0.29</td><td>2.59</td><td>0.26</td><td>2.81</td><td>2.74</td><td>0.25</td><td>2.67</td><td>0.23</td><td>2.93</td><td>2.82</td><td>322.561</td></tr><tr><td>Jul-25</td><td>0.17</td><td>2.61</td><td>0.25</td><td>2.86</td><td></td><td>0.23</td><td>2.70</td><td>0.31</td><td>3.06</td><td></td><td>323.048</td></tr><tr><td>Aug-25</td><td>0.26</td><td>2.75</td><td>0.22</td><td>2.91</td><td></td><td>0.35</td><td>2.92</td><td>0.31</td><td>3.11</td><td></td><td>323.976</td></t

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
