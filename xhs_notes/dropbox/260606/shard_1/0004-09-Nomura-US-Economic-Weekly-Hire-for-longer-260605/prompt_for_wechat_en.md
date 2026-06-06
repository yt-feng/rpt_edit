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
# US Economic Weekly

Economics - North America

# Hire for longer

- The May employment report showed continued acceleration in the labor market. Job gains surprised to the upside, with positive revisions to prior months, and the unemployment rate held steady.   
- The labor market is not overheating, but there are also no signs of stress from overly restrictive policy. We expect Fed officials will remain focused on inflation risks.   
- We expect core CPI inflation moderated to $0.183\%$ m-o-m in May from $0.376\%$ in April as a temporary boost from rent-related technical factors diminished. Goods inflation was slightly positive as IT-related price pressures offset the waning impact of tariffs.   
- Despite benign core CPI, we expect core PCE inflation accelerated in May due to strength from PCE relevant PPI components.   
- The Trump administration announced new Section 301 tariffs, largely aimed at replicating the IEEPA tariff framework after Section 122 tariffs expire on 24 July. We view the move mainly as an effort to preserve continuity in the trade regime rather than a meaningful escalation.

# Employment growth remained robust in May

Headline nonfarm payrolls rose 172k in May, well above expectations (NOM: 110k, consensus: 88k). Revisions to prior months were also positive, which helped push the 3m average to its highest level since March 2024. A broad range of indicators now suggest the underlying trend for employment growth is gaining momentum (Fig. 1).

Fig. 1: A broad range of indicators suggest the underlying trend for employment growth is gaining momentum   
3mma private payrolls   
![](images/5952ba30c3e3a15edb10d713715624f82a8c2e2cff399908c0949db055d7a353.jpg)

<details>
<summary>line</summary>

| Date   | NFP private employment | HH employment, concept and population adjusted | ADP private employment |
|--------|------------------------|--------------------------------------------------|------------------------|
| Dec-22 | ~200                   | ~400                                             | ~200                   |
| Jun-23 | ~150                   | ~400                                             | ~350                   |
| Dec-23 | ~100                   | ~-300                                            | ~200                   |
| Jun-24 | ~100                   | ~200                                             | ~150                   |
| Dec-24 | ~100                   | ~250                                             | ~100                   |
| Jun-25 | ~50                    | ~-250                                            | ~50                    |
| Dec-25 | ~150                   | ~100                                             | ~100                   |
</details>

Source: ADP, BLS, Haver, NOM

Fig. 2: Breadth of job gains have improved lately   
BLS' diffusion indices   
![](images/a64378149e42c22b6f7c9a0be292c0aca9617d1363090aff06d27d0d2240d575.jpg)

<details>
<summary>line</summary>

| Year | 1-month | 3-month | 6-month |
|------|---------|---------|---------|
| 19   | 65      | 68      | 70      |
| 20   | 30      | 30      | 30      |
| 21   | 75      | 78      | 80      |
| 22   | 80      | 85      | 88      |
| 23   | 65      | 70      | 75      |
| 24   | 50      | 55      | 60      |
| 25   | 45      | 50      | 55      |
| 26   | 55      | 50      | 50      |
</details>

Source: BLS, Haver, NOM

Sector level details suggest that some one-off factors boosted NFP on net. An outsize 70k increase in leisure and hospitality may have been partly driven by a temporary boost from the World Cup. In addition, local government employment rose 55k, driving government employment higher in the month. These increases were only modestly offset by negative

# Research Analysts

# North America Economics

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

# Global Economics

David Seif - NSI

david.seif@NOM.com

+1 212 667 9180

mean-reversion in trade and transportation sectors as well as a 9k decline due to the Spirit Airlines bankruptcy. Despite some noise in the details, the overall breadth of job gains continued to improve alongside strength in cyclical sectors (Fig. 2).

The unemployment rate remained steady at $4.3\%$ on a rounded basis. Measures of job losses fell in May, reversing a concerning increase in April (Fig. 3). This puts the household survey back in line with other layoff measures like jobless claims and JOLTS, all pointing to a resilient labor market. The job-finding rate picked up modestly but remains lackluster (Fig. 4).

Fig. 3: Measures of job losses fell in May, reversing a concerning increase in April   
![](images/28cf56e9d33f1d602eac5a0536ad910441ce5f9c1b9efda4ff664cec97ba7788.jpg)

<details>
<summary>line</summary>

| Year | Initial Claims | E-U Flow Rate | JOLTS Layoffs and Discharges | Short-Term Unemployment |
|------|----------------|---------------|-------------------------------|--------------------------|
| 19   | 0.6%           | 1.0%          | 1.2%                          | 1.8%                     |
| 20   | 0.6%           | 1.0%          | 1.2%                          | 1.8%                     |
| 21   | 2.5%           | 1.5%          | 1.0%                          | 2.0%                     |
| 22   | 0.7%           | 1.0%          | 1.0%                          | 1.8%                     |
| 23   | 0.6%           | 1.0%          | 1.0%                          | 1.8%                     |
| 24   | 0.6%           | 1.0%          | 1.0%                          | 1.8%                     |
| 25   | 0.6%           | 1.0%          | 1.0%                          | 1.8%                     |
| 26   | 0.6%           | 1.0%          | 1.0%                          | 1.8%                     |
</details>

Source: BLS, Haver, NOM

Fig. 4: The job-finding rate picked up modestly but remains lackluster   
![](images/8e9f308cca0a147eb2182e31e0c96814a149ae4d7b2ce42a6b7fbf9f499cc85d.jpg)

<details>
<summary>line</summary>

| Week | Median duration (weeks unemployed) | Job-finding rate (duration-based) | Job-finding rate (flows-based) | Labor differential (RHS) |
|------|------------------------------------|-----------------------------------|----------------------------------|---------------------------|
| 17   | 0.2                                | 0.35                              | 0.25                             | 0.2                       |
| 18   | 0.2                                | 0.35                              | 0.25                             | 0.25                      |
| 19   | 0.2                                | 0.35                              | 0.25                             | 0.3                       |
| 20   | 0.5                                | 0.3                               | 0.35                             | 0.35                      |
| 21   | 0.1                                | 0.3                               | 0.25                             | 0.4                       |
| 22   | 0.2                                | 0.35                              | 0.3                              | 0.45                      |
| 23   | 0.2                                | 0.35                              | 0.3                              | 0.4                       |
| 24   | 0.2                                | 0.35                              | 0.25                             | 0.3                       |
| 25   | 0.2                                | 0.3                               | 0.2                              | 0.25                      |
| 26   | 0.15                               | 0.3                               | 0.2                              | 0.2                       |
</details>

Source: BLS, The Conference Board, Haver, NOM

Average hourly earnings growth picked up to $0.3\%$ m-o-m, driving payroll income growth to $0.4\%$ m-o-m.

Overall, today's report should keep Fed officials focused on inflation risks. Accelerating job gains and steady unemployment suggest the current policy stance is not restraining the economy. Timely measures of job losses show few signs of stress, while backward-looking benchmark data suggest we are unlikely to see a substantial negative revision to NFP later this summer.

While the labor market is healthy, it is also not overheating. The unemployment rate has remained stable, and wage growth is decelerating faster than we had expected. Sideways income growth suggests consumer spending should begin to cool later in the summer. We are skeptical that inflation is on track to return to the Fed's $2\%$ target, but officials can reasonably claim that the labor market is not a significant source of price pressure

# We expect core CPI inflation slowed in May, but broader trajectory remains unchanged

Core CPI inflation likely moderated to $0.183\%$ m-o-m in May from $0.376\%$ in April, as a short-lived boost from rent-related technical adjustment waned in the month (Fig. 5).

We forecast core goods inflation rose $0.03\%$ m-o-m, essentially unchanged from April (Fig. 6). Leading indicators, including the Adobe Digital Price Index, suggest tech-related components continued to see price increases, while tariff-related inflation eased. Vehicle prices likely remained stable. Overall, we expect that the global chip shortage, energy shocks due to the Iran war, and higher metal prices will continue to push up core goods inflation, offsetting the waning price pressure from tariffs.

Fig. 5: We expect core CPI inflation moderated to $0.183\%$ m-o-m in May as a temporary boost from rent-related technical adjustment waned in the month   
Decomposition of m-o-m core CPI inflation   
![](images/eb65e3574f4f2e3e3d5afc0a061cf4c3f0ed52d1fc832478b16d2f69b4f6c4d1.jpg)

<details>
<summary>bar_stacked</summary>

| Month | Used vehicle prices (%) | Auto insurance (%) | Airline fares (%) | Rent + OER (%) | Others (%) | New vehicles (%) | Lodging (%) | Apparel (%) | Medical care services (%) | Core CPI |
|---|---|---|---|---|---|---|---|---|---|---|
| Jan-25 | 0.05 | 0.08 | -0.03 | 0.15 | 0.27 | 0.04 | 0.03 | 0.01 | 0.03 | 0.42 |
| Apr-25 | 0.03 | 0.02 | -0.15 | 0.12 | 0.21 | 0.03 | 0.02 | 0.01 | 0.03 | 0.12 |
| Jul-25 | 0.03 | 0.02 | -0.03 | 0.15 | 0.24 | 0.04 | 0.03 | 0.01 | 0.04 | 0.31 |
| Oct-25 | 0.02 | 0.03 | -0.15 | 0.12 | 0.21 | 0.04 | 0.03 | 0.01 | 0.03 | 0.11 |
| Jan-26 | 0.03 | 0.02 | -0.03 | 0.15 | 0.27 | 0.04 | 0.03 | 0.01 | 0.04 | 0.29 |
| Apr-26 | 0.02 | 0.02 | -0.15 | 0.12 | 0.21 | 0.04 | 0.03 | 0.01 | 0.04 | 0.38 |
forecast (right axis) |
| Feb-27 | 0.03 | 0.02 | -0.15 | 0.15 | 0.21 | 0.04 | 0.03 | 0.01 | 0.04 | 0.21 |
Figure label: forecast.
</details>

Note: For CPI components which are not available in October 2025, we assume no inflation on a not-seasonally adjusted basis for survey-based components, but seasonal adjustment is applied.   
Source: BLS, Haver, NOM

Fig. 6: We expect CPI core goods inflation remained slightly positive in May   
![](images/05479cc42b0c75d3906bd1ea252ff7832381f21259d2234d4cc5a93f864cde50.jpg)

<details>
<summary>bar_line</summary>

| Date    | Household Furnishings and Supplies | Medical care commodities | Apparel | New and used vehicles | Other core goods | CPI core goods inflation |
|---------|------------------------------------|---------------------------|---------|------------------------|------------------|--------------------------|
| Jul-24  | -0.25                              | -0.15                     | -0.10   | -0.10                  | -0.15            | -0.25                    |
| Jan-25  | 0.30                               | 0.40                      | 0.15    | 0.35                   | 0.10             | 0.30                     |
| Jul-25  | 0.15                               | 0.10                      | 0.05    | 0.15                   | 0.05             | 0.15                     |
| Jan-26  | 0.25                               | 0.20                      | 0.25    | -0.25                  | 0.15             | 0.25                     |
| Latest  | -0.10                              | -0.15                     | -0.10   | -0.15                  | -0.10            | -0.35                    |
</details>

Source: BLS, Haver, NOM

Supercore service inflation appears to have decelerated to $0.247\%$ m-o-m in May from a $0.454\%$ advance in April (Fig. 7). We expect inflation of lodging-away-from-home prices (which tend to mean-revert) slowed in May after having risen strongly in April. Other personal services component also likely slowed in the month due to negative residual seasonality. These declines were modestly offset by airline fares, which likely remained strong due to higher jet fuel prices.

Fig. 7: CPI supercore service inflation likely moderated in May, driven by muted inflation of hotel prices and residual seasonality   
Decomposition of m-o-m CPI supercore service inflation   
![](images/3b7ce0dd02bffbf7fa248b679e65b0c4d73fdd58f257ba973ae2df528e2948c4.jpg)

<details>
<summary>bar_line</summary>

| Date | Others | Medical care | Lodging away from home | Airline fares | Auto insurance | CPI supercore inflation |
|---|---|---|---|---|---|---|
| Jan-24 | 0.35 | 0.15 | 0.05 | 0.15 | 0.15 | 0.75 |
| Jul-24 | 0.25 | 0.10 | -0.05 | 0.10 | 0.10 | 0.35 |
| Jan-25 | 0.35 | 0.10 | -0.10 | 0.15 | 0.15 | 0.65 |
| Jul-25 | 0.35 | 0.15 | -0.05 | 0.20 | 0.20 | 0.45 |
| Jan-26 | 0.65 | 0.15 | 0.10 | 0.25 | -0.10 | 0.60 |
| Latest | 0.25 | 0.05 | 0.15 | 0.20 | 0.15 | 0.45 |
</details>

Source: BLS, Haver, NOM

Fig. 8: Despite benign core CPI, core PCE inflaiton likely accelerated in May due to elevated PPI components   
![](images/93a1dae38532411a3616b117049670f2ce281b5d1248ae7fb57df328fed45566.jpg)  
Source: BLS, BEA, Haver, NOM

Although we anticipate a slowdown in m-o-m core CPI inflation in May, core PCE inflation likely accelerated to $0.327\%$ m-o-m from $0.239\%$ in April due to strength in PCE-relevant PPI components (Fig. 8). PCE prices for portfolio management and investment advice

services and airline fares (both derived from corresponding PPI data) appear to have risen strongly in May. Our forecast translates into further firming of y-o-y core PCE inflation to $3.4\%$ in May from $3.3\%$ in April, significantly higher than the Fed's target.

There is broader evidence of spillovers from the Iran war. The prices paid index of ISM services rose to its highest level since mid 2022, and in addition to energy, firms noted rising costs for freight, packaging material, food, fertilizers, construction material, and labor. The Beige Book also reported that price increases were "moderate to strong," faster than the "moderate" growth indicated in April.

# Fedspeak remains hawkish

Fedspeak has remained hawkish. Dallas Fed president Logan was the highlight of the week. While other officials have laid out scenarios that could solicit some policy tightening, Logan seems to be the first who has unconditionally advocated for increasing rates. She mentioned that current economic conditions suggest that "monetary policy is not restraining the economy," and she was "increasingly concerned that higher interest rates could be necessary later this year" to appropriately balance both sides of the Fed's dual mandate. Cleveland Fed president Hammack also remained hawkish and commented that the May employment report affirms that labor market is roughly in balance. She fell short of advocating for a hike, saying that it is reasonable to keep rates steady now.

NY Fed president Williams remained a dovish outlier, suggesting that he was not concerned about persistent inflation. He also did not see any obvious reason to change the forward guidance language.

Regarding the upcoming June FOMC meeting, a Financial Times article indicated that Fed Chair Warsh might not submit his own forecast for the policy rate, sticking to his belief that forward guidance is not useful. Consistent with his claim to make a “reform-oriented” Fed, Warsh reportedly tapped two advisors who had previously called for drastic changes in monetary policy operations.

# Tariff update: continuity more than escalation

The Trump administration announced new Section 301 tariffs of 10–12.5% on 60 trade partners, largely aimed at replicating the IEEPA tariff framework after Section 122 tariffs expire on 24 July. We view the move mainly as an effort to preserve continuity in the trade regime rather than a meaningful escalation. Our estimate for the terminal effective tariff rate remains unchanged at 8–9%.

The proposed tariff rates as a result of forced labor investigations under Section 301 are modestly below corresponding IEEPA tariffs for many countries. However, USTR Greer said that results of Section 301 investigations into countries to uncover unfair trade practices related to "structural" excess capacity and production would be released in the coming weeks. These separate 301 probes could result in additional stackable tariffs. We estimate that the shift from country-specific IEEPA tariffs to universal $10\%$ section 122 tariffs lowered the effective tariff rate by 1.5pp. We expect full implementation of Section 301 tariffs would likely reverse most of the decline, lifting the effective tariff rate to $\sim 8.5\%$ from $\sim 7.0\%$ currently.

The broader trajectory of trade policy remains de-escalatory despite episodic flare-ups. Section 232 tariffs on certain metal products were recently cut to 15% from 25%, while the domestic content threshold for imported products to qualify as made “entirely” from US aluminum, steel, or copper is set to decline to 85% from 95% of US melted and poured metals. In addition, Greer mentioned that proposed additional 25% tariffs on Brazil would be “quite nuanced” and continue to exclude beef, coffee, metals, and some other goods.

# Q2 GDP tracking

We lowered our Q1 GDP tracking to $2.3\%$ from $2.4\%$ last week. Our estimate for real final sales to private domestic purchasers stands at $2.6\%$ from $2.8\%$ previously. Nonresidential construction spending came in below our expectations, weighing on our estimate for fixed investment. In addition, our forecast for May PCE suggest real spending slowed in the month. These were only partly offset by strength in government consumption to expenditure and IPP due to strong May employment report

Fig. 9: NOM's inflation forecasts 

<table><tr><td rowspan="2"></td><td colspan="2">Headline 

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
