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
# Economic Insights

Global Markets Research

29 May 2026

Economics - North America

# US: Skewed vision – evaluating trimmed-mean inflation

- Fed Chair Kevin Warsh described core PCE inflation, the Fed's long-time preferred inflation metric, as a "rough swag" and proposed alternative inflation measures including trimmed-mean inflation.   
- PCE trimmed-mean inflation tends to be slow in detecting a change in the inflation trend, while underlying inflation trend measures indicate the risk of a new upward trend emerging recently.   
- We remain skeptical about the usefulness of PCE trimmed-mean inflation, whose method of removing outliers might not be optimal due to the recent shift in skewness of the cross-sectional inflation distribution. Trimmed-mean inflation might underestimate underlying inflation by about 48bp on a y-o-y basis.   
- A primary factor making PCE trimmed-mean inflation negatively biased is its failure to capture changes in goods price inflation dynamics in the post-pandemic era.

# What is PCE trimmed-mean inflation?

Monthly inflation data are noisy, and idiosyncratic moves by a few components can have an outsized effect. Policymakers aim to look through temporary noise and gauge the underlying trend of inflation. One of the simplest metrics that diminishes such noise is core PCE inflation, which excludes volatile energy and food prices. Most FOMC participants put a heavy weight on PCE core inflation as a gauge of the underlying trend.

Fed Chair Kevin Warsh has criticized PCE core inflation, describing it as a “rough swag” at his confirmation hearing. Instead, he proposed alternative inflation measures, including PCE trimmed-mean inflation and private sector price measures.

Fig. 1: The 12-month change in PCE trimmed-mean stands at $2.35\%$ in April, 94bp lower than $3.29\%$ for core PCE inflation   
![](images/469f11a032e65b2d314487d32593f683594863497ebf8899e74007806eb8e7dd.jpg)

<details>
<summary>line</summary>

| Date    | Trimmed-mean PCE inflation | Median PCE inflation | Core PCE inflation | Headline PCE inflation |
|---------|----------------------------|----------------------|--------------------|------------------------|
| Jan-16  | ~1.5                       | ~2.0                 | ~1.5               | ~-2.0                  |
| Jan-18  | ~1.8                       | ~2.2                 | ~1.8               | ~-1.0                  |
| Jan-20  | ~1.7                       | ~2.3                 | ~1.7               | ~-0.5                  |
| Jan-22  | ~4.5                       | ~6.0                 | ~5.5               | ~6.5                   |
| Jan-24  | ~3.0                       | ~4.0                 | ~3.5               | ~-1.0                  |
| Jan-26  | ~2.5                       | ~3.0                 | ~3.0               | ~-0.5                  |
</details>

Source: BEA, Dallas Fed, Cleveland Fed, Haver, NOM

PCE trimmed-mean inflation is constructed from the cross-sectional distribution of monthly price changes and is designed to remove components with large monthly swings in either direction. Currently, the metric – published by the Dallas Fed – trims 24% from the lower tail and 31% from the upper tail of the distribution. The 12-month change in PCE trimmed-mean stood at 2.35% in April, 94bp lower than 3.29% for core PCE inflation (Fig. 1).

# Research Analysts

# North America Economics

Aichi Amemiya - NSI

aichi.amemiya@NOM.com

+1 212 667 9347

Ruchir Sharma - NSI

ruchir.sharma@NOM.com

+1 212 667 9186

Jeremy Schwartz - NSI

jeremy.schwartz@NOM.com

+1 212 667 9637

Jacklyn Goloborodsky - NSI

jacklyn.goloborodsky@NOM.com

+1 212 298 4739

# Global Economics

David Seif - NSI

david.seif@NOM.com

+1 212 667 9180

# Tracking "true inflation"

A key factor in evaluating the value of trimmed-mean inflation is whether it accurately captures “true inflation,” or underlying inflation. In order to assess whether PCE trimmed-mean inflation captures changes in the inflation trend in a timely manner, we calculate four “true” inflation trend series using ex-post data;

• A centered 36-month moving average of annualized monthly headline PCE inflation   
• A band-pass filtered annualized monthly headline PCE inflation   
- The average of annualized monthly PCE inflation for the contemporaneous and following 24 months   
- A centered 12-month moving average of a centered 24-month moving average of annualized headline PCE inflation

Among these four “true” inflation measures, a Dallas Fed economist used the first three to choose the optimal cutoffs when formulating PCE trimmed-mean inflation. Note that the optimal trimming proportions (24% of the lower tail and 31% of the upper tail) were determined to minimize the gap between PCE trimmed-mean inflation and the average of those true inflation measures over the period of January 1977 to June 2009. The last “true” inflation measure was a benchmark Cleveland Fed economists used to assess the usefulness of not-seasonally adjusted Median CPI inflation.

# Evaluating trimmed-mean's performance

# PCE trimmed-mean failed to detect the post-pandemic inflation surge

PCE trimmed-mean inflation is designed to look through idiosyncratic noise and avoid sending false positive signals about the underlying inflation trend. Thus, PCE trimmed-mean inflation is often better than core PCE inflation in the sense of fewer false signals of new inflation trends. However, that same feature can make it less responsive when a new inflation regime is emerging, especially if the initial shock is concentrated in a narrow set of components, leading to a change in skewness of the inflation distribution.

This limitation was evident during the post-pandemic inflation surge. At the onset of post-pandemic inflation acceleration, annualized monthly PCE trimmed-mean inflation lagged these four true inflation measures (Fig. 2). On the other hand, annualized monthly core PCE inflation started accelerating at almost the same time as the true measures, except for the average of future 24-month inflation (Fig. 3).

Fig. 2: PCE trimmed-mean inflation lagged four "true" inflation measures in 2021-2022   
![](images/fc8a8f36ce0e3524b9c286533a94c2240d8921c154faa94272e7b786d71a0a69.jpg)

<details>
<summary>line</summary>

| Year | Band-pass filtered headline PCE inflation | Centered 36-month moving average of headline PCE inflation | Forward 24-month moving average of headline PCE inflation | Centered 12-month moving average of centered 24-month moving average of headline PCE inflation | PCE trimmed-mean inflation, m-o-m, annualized |
|------|------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------| ----------------------------------------------------------------------------------|---------------------------------------------|
| 2000 | ~2.8%                                    | ~2.0%                                                         | ~1.8%                                                         | ~2.0%                                                                            | ~3.0                                        |
| 2002 | ~1.5%                                    | ~1.8%                                                         | ~1.7%                                                         | ~1.9%                                                                            | ~2.5                                        |
| 2004 | ~2.8%                                    | ~2.5%                                                         | ~3.0%                                                         | ~2.8%                                                                            | ~3.5                                        |
| 2006 | ~3.0%                                    | ~2.8%                                                         | ~2.5%                                                         | ~2.7%                                                                            | ~3.0                                        |
| 2008 | ~1.0%                                    | ~1.5%                                                         | ~0.5%                                                         | ~1.5%                                                                            | ~1.0                                        |
| 2010 | ~1.5%                                    | ~1.8%                                                         | ~1.5%                                                         | ~1.8%                                                                            | ~1.5                                        |
| 2012 | ~2.5%                                    | ~2.0%                                                         | ~1.8%                                                         | ~2.0%                                                                            | ~2.5                                        |
| 2014 | ~1.0%                                    | ~1.2%                                                         | ~0.8%                                                         | ~1.0%                                                                            | ~1.5                                        |
| 2016 | ~0.5%                                    | ~0.8%                                                         | ~0.5%                                                         | ~0.8%                                                                            | ~1.0                                        |
| 2018 | ~2.0%                                    | ~1.8%                                                         | ~1.5%                                                         | ~1.8%                                                                            | ~2.5                                        |
| 2020 | ~1.5%                                    | ~1.8%                                                         | ~3.0%                                                         | ~2.5%                                                                            | ~3.5                                        |
| 2022 | ~6.5%                                    | ~5.0%                                                         | ~6.0%                                                         | ~5.5%                                                                            | ~7.0                                        |
| 2024 | ~2.0%                                    | ~3.0%                                                         | ~3.5%                                                         | ~3.0%                                                                            | ~5.5                                        |
| 2026 | ~4.5%                                    | ~4.0%                                                         | ~3.0%                                                         | ~3.5%                                                                            | ~3.0                                        |
</details>

Source: BEA, Haver, NOM

Fig. 3: Core PCE inflation has tracked four "true" inflation measures better than PCE trimmed-mean inflation in recent years   
![](images/b6ca88ed2c35303e37305dcc16b4f1c1b57cfbe8e97cec0c9b18b4b5eee7d3d5.jpg)

<details>
<summary>line</summary>

| Year | Band-pass filtered headline PCE inflation | Centered 36-month moving average of headline PCE inflation | Forward 24-month moving average of headline PCE inflation | Centered 12-month moving average of centered 24-month moving average of headline PCE inflation | Core PCE inflation, m-o-m, annualized |
|------|------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------| ---------------------------------------------------------------------------------------------|-------------------------------------|
| 2000 | ~2.8%                                    | ~2.0                                                          | ~1.8                                                          | ~2.2                                                                                         | ~1.0                                |
| 2002 | ~1.5%                                    | ~2.5                                                          | ~2.0                                                          | ~2.5                                                                                         | ~8.0                                |
| 2004 | ~2.8%                                    | ~2.5                                                          | ~3.0                                                          | ~2.8                                                                                         | ~3.0                                |
| 2006 | ~3.0%                                    | ~2.8                                                          | ~3.0                                                          | ~3.0                                                                                         | ~3.5                                |
| 2008 | ~1.5%                                    | ~1.8                                                          | ~1.5                                                          | ~1.5                                                                                         | ~4.5                                |
| 2010 | ~2.5%                                    | ~2.0                                                          | ~2.0                                                          | ~2.0                                                                                         | ~3.5                                |
| 2012 | ~2.8%                                    | ~2.0                                                          | ~1.5                                                          | ~1.5                                                                                         | ~3.0                                |
| 2014 | ~1.5%                                    | ~1.0                                                          | ~0.5                                                          | ~1.0                                                                                         | ~2.0                                |
| 2016 | ~1.0%                                    | ~1.5                                                          | ~1.0                                                          | ~1.5                                                                                         | ~3.0                                |
| 2018 | ~2.5%                                    | ~1.5                                                          | ~1.5                                                          | ~1.5                                                                                         | ~4.0                                |
| 2020 | ~1.5%                                    | ~2.5                                                          | ~4.0                                                          | ~3.0                                                                                         | ~7.0                                |
| 2022 | ~6.5%                                    | ~5.0                                                          | ~6.0                                                          | ~5.5                                                                                         | ~7.5                                |
| 2024 | ~2.0%                                    | ~3.0                                                          | ~3.0                                                          | ~3.0                                                                                         | ~6.5                                |
| 2026 | ~4.5%                                    | ~4.5                                                          | ~3.0                                                          | ~3.0                                                                                         | ~5.0                                |
</details>

Source: BEA, Haver, NOM

A similar dynamic appears to have played out in the opposite direction during the post-GFC disinflation. PCE trimmed-mean inflation was slow to respond to the emerging downshift in underlying inflation, while core PCE inflation began to decelerate earlier.

The components excluded from PCE trimmed-mean may offer a better early signal around inflation turning points. A closer look at the distribution of cross-sectional monthly price changes suggests the weighted average of components trimmed from both tails began to react to the pandemic-induced inflation wave as early as Q1 2021, much earlier than PCE trimmed-mean inflation did (Fig. 4). The same dynamic was visible in the opposite direction during the post-GFC disinflation, when components removed from the lower tail dropped sharply, while PCE trimmed-mean inflation remained steady for some time.

Fig. 4: Components removed from PCE trimmed-mean inflation reacted quickly to the post-pandemic acceleration

Weighted average of the upper and lower tails removed from PCE trimmed-mean inflation vs. PCE trimmed-mean inflation

![](images/dd342e32d4e48f7ff77e1c7e18eeffd5ef1ca68b9cac7060f90964105a4a2365.jpg)

<details>
<summary>line</summary>

| Year | Upper tail (removed from PCE trimmed-mean) | PCE trimmed-mean | Lower tail (removed from PCE trimmed-mean) |
|------|---------------------------------------------|------------------|---------------------------------------------|
| 01   | ~15                                         | ~3               | ~-10                                        |
| 04   | ~12                                         | ~3               | ~-8                                         |
| 07   | ~22                                         | ~3               | ~-6                                         |
| 10   | ~10                                         | ~2               | ~-15                                        |
| 13   | ~10                                         | ~2               | ~-6                                         |
| 16   | ~12                                         | ~2               | ~-8

[中间内容因长度限制已省略]

ct of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

# NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities International, Inc., US. All rights reserved.
"""
