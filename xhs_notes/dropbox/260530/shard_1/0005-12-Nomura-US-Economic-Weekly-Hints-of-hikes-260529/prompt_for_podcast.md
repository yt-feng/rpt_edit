你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# US Economic Weekly

Economics - North America

# Hints of hikes

- We expect headline payrolls remained strong at 110k in May. The unemployment rate likely remained stable at $4.3\%$ , while average hourly earnings rebounded.   
- Core PCE inflation moderated in April, but backward revisions to prior months led y-o-y core PCE inflation to accelerate to $3.289\%$ in April from $3.236\%$ in March. Core PCE remained well above the Fed's target of $2\%$ and upside inflation risks persist.   
- Trimmed-mean PCE inflation, Chair Warsh's preferred measure, eased to $2.3\%$ y-o-y in April. We remain skeptical about the usefulness of the measure as it tends to be slow in detecting a change in the inflation trend and has understated inflation lately.   
- Fedspeak this week leaned hawkish as officials discussed inflation scenarios that would warrant hikes. While their base case continues to be a moderation in inflation, various policymakers said they would support hikes if inflation does not come down in a “timely” manner.

# We expect employment growth remained elevated in May

Headline nonfarm payrolls likely rose 110k in May – a slight deceleration from the prior two months but still above the year-to-date average. Our forecast would bring the 3m average of NFP growth up to 137k – the strongest since December 2024. We expect private payroll gains remained essentially unchanged at 115k in May from 123k in April.

Despite lead indicators (e.g., ADP's weekly private employment measure and continuing jobless claims), pointing to signs of accelerating job gains (Fig. 1 & 2), we expect a roughly sideways NFP reading this month due to risks of mean-reversion in certain sectors that outperformed in March and April. For instance, retail trade and couriers and messengers have been exceptionally strong, and are likely to edge lower in April, offsetting strength in construction and manufacturing payrolls.

Fig. 1: Continuing jobless claims stabilized close to a multi-year low   
![](images/bda55bd856997dc5daf1137d28fca024778c8c1f27c4d5ca1f0667d036aecf18.jpg)

<details>
<summary>line</summary>

| Date    | Value |
|---------|-------|
| Jun 24  | 1825  |
| Jul 24  | 1835  |
| Aug 24  | 1845  |
| Sep 24  | 1855  |
| Oct 24  | 1865  |
| Nov 24  | 1875  |
| Dec 24  | 1885  |
| Jan 25  | 1895  |
| Feb 25  | 1905  |
| Mar 25  | 1915  |
| Apr 25  | 1925  |
| May 25  | 1935  |
| Jun 25  | 1945  |
| Jul 25  | 1955  |
| Aug 25  | 1965  |
| Sep 25  | 1975  |
| Oct 25  | 1965  |
| Nov 25  | 1955  |
| Dec 25  | 1945  |
| Jan 26  | 1935  |
| Feb 26  | 1925  |
| Mar 26  | 1915  |
| Apr 26  | 1905  |
| May 26  | 1895  |
| Jun 26  | 1885  |
| Jul 26  | 1875  |
| Aug 26  | 1865  |
| Sep 26  | 1855  |
| Oct 26  | 1845  |
| Nov 26  | 1835  |
| Dec 26  | 1825  |
| Jan 27  | 1815  |
| Feb 27  | 1805  |
| Mar 27  | 1795  |
| Apr 27  | 1785  |
| May 27  | 1775  |
| Jun 27  | 1765  |
| Jul 27  | 1755  |
| Aug 27  | 1745  |
| Sep 27  | 1735  |
| Oct 27  | 1725  |
| Nov 27  | 1715  |
| Dec 27  | 1705  |
| Jan 28  | 1695  |
| Feb 28  | 1685  |
| Mar 28  | 1675  |
| Apr 28  | 1665  |
| May 28  | 1655  |
| Jun 28  | 1645  |
| Jul 28  | 1635  |
| Aug 28  | 1625  |
| Sep 28  | 1615  |
| Oct 28  | 1605  |
| Nov 28  | 1595  |
| Dec 28  |        |
</details>

Note: Markers refer to NFP survey reference week  
Source: DOL, BLS, Haver, NOM

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

Fig. 2: ADP's weekly private employment measure remained elevated through April and early May   
w-o-w changes in ADP private employment   
![](images/1ba50689c70329d04ece5978ff1079d62e33e9735216eaa4e5ae8641e48a6187.jpg)

<details>
<summary>line</summary>

| Date   | Old ADP weekly series | 12 May vintage | 19 May vintage | Latest |
|--------|------------------------|----------------|----------------|--------|
| 7/5    | 90                     | -              | -              | -      |
| 8/5    | -30                    | -              | -              | -50    |
| 9/5    | -                      | -              | -              | -      |
| 10/5   | -                      | -              | -              | -      |
| 11/5   | -                      | -              | -              | -      |
| 12/5   | -                      | -              | -              | 20     |
| 1/5    | -                      | -              | -              | 10     |
| 2/5    | -                      | -              | -              | 15     |
| 3/5    | -                      | -              | -              | 10     |
| 4/5    | -                      | -              | -              | 40     |
| 5/5    | -                      | -              | 40             | 35     |
</details>

Source: ADP, Haver, NOM   
Production Complete: 2026-05-29 19:14 UTC

We expect the unemployment rate remained unchanged at 4.3%. Labor demand has stabilized in recent quarters (Fig. 3), leading to a faster pace of hiring and shorter unemployment duration. Measures of job losses have been mixed (Fig. 4). The 4-week moving average for initial jobless claims reached a multi-year low in the May NFP reference week, while the April household survey and March JOLTS point to a modest increase in job losses.

Fig. 3: Labor demand has stabilized in recent quarters   
Measures of job finding   
![](images/32b3b7b01bf4f9aa75d29130f1d685b91cac50c8483aeaedd1e33227e0507993.jpg)

<details>
<summary>line</summary>

| Year | Vacancy-Unemployment Ratio (LHS) | Labor Differential (RHS) |
|------|----------------------------------|--------------------------|
| 19   | ~1.2                             | ~1.3                     |
| 20   | ~1.1                             | ~0.1                     |
| 21   | ~0.6                             | ~0.5                     |
| 22   | ~2.0                             | ~1.6                     |
| 23   | ~1.8                             | ~1.4                     |
| 24   | ~1.3                             | ~1.0                     |
| 25   | ~1.0                             | ~0.8                     |
| 26   | ~0.9                             | ~0.6                     |
</details>

Source: BLS, The Conference Board, Haver, NOM

Fig. 4: Measures of job losses have been mixed   
Job loss rates   
![](images/eeb4ac220f6127b54e532784dc00d827c8b0aff6d297c8456059ca54422573de.jpg)

<details>
<summary>line</summary>

| Year | Initial Claims | E-U Flow Rate | JOLTS Layoffs and Discharges | Short-Term Unemployment |
|------|----------------|---------------|-------------------------------|--------------------------|
| 19   | 0.6%           | 0.9%          | 1.2%                          | 1.7%                     |
| 20   | 0.6%           | 1.0%          | 1.3%                          | 1.8%                     |
| 21   | 2.5%           | 1.5%          | 1.4%                          | 2.2%                     |
| 22   | 0.7%           | 1.0%          | 1.0%                          | 1.8%                     |
| 23   | 0.6%           | 0.9%          | 1.1%                          | 1.7%                     |
| 24   | 0.6%           | 0.9%          | 1.1%                          | 1.7%                     |
| 25   | 0.6%           | 1.0%          | 1.2%                          | 1.7%                     |
| 26   | 0.5%           | 0.9%          | 1.2%                          | 1.7%                     |
</details>

Source: BLS, Haver, NOM

Average hourly earnings (AHE) growth likely rebounded to 0.4% m-o-m. A negative calendar effect weighed on AHE in April, but it turns positive in May (AHE tends to underperform when the 12th of the month is on a weekend, and outperforms when the 12th falls mid-week). In our view, the recent slowdown in AHE has largely been driven by technical factors. Underlying wage growth appears elevated, supporting our expectation for positive payback this month.

# Core PCE inflation in April softer, but details point to continued price pressures

Core PCE came in softer than expected at 0.24% m-o-m in April, below both our and consensus forecasts of 0.30%. The miss was partly driven by tax-preparation services (Fig. 5) and some non-CPI/PPI components. However, prior-month revisions were slightly firmer, leaving core PCE inflation at 3.29% y-o-y in April, up modestly from 3.24% in March.

Despite the downside surprise, financial service prices which declined in April are likely to rebound in May, given the recent strong performance of stock markets. Moreover, we expect airline fares will continue to rise at a decent pace in the next month. Beyond May, the balance of risks is tilted toward the upside as higher energy prices, shortages of semiconductors, and rising transportation costs point to upside risks to the near-term inflation outlook.

Fig. 5: Supercore PCE inflation moderated slightly in April due to temporary weakness in financial service prices   
m-o-m supercore PCE inflation   
![](images/9fb6424bd9628f015af632b243e8713b4caede5d9c6d37ac381523cea03a051f.jpg)

<details>
<summary>bar_line</summary>

| Date | Airline fares (%) | Others (%) | Food services and accommodations (%) | Healthcare (%) | Financial services (%) | Supercore PCE inflation (%) |
|---|---|---|---|---|---|---|
| Jan-24 | 0.75 | 0.55 | 0.15 | 0.10 | 0.28 | 0.75 |
| Jul-24 | -0.05 | 0.33 | 0.08 | 0.12 | 0.12 | 0.33 |
| Jan-25 | 0.33 | 0.25 | 0.10 | 0.15 | 0.22 | 0.50 |
| Jul-25 | 0.18 | 0.23 | 0.09 | 0.14 | 0.06 | 0.33 |
| Jan-26 | 0.33 | 0.25 | 0.12 | 0.16 | 0.14 | 0.55 |
| Apr-26 | 0.18 | 0.18 | 0.11 | 0.17 | -0.08 | -0.15 |
</details>

Source: BEA, BLS, Haver, NOM

Fig. 6: PCE trimmed-mean inflation appears to understate the underlying inflation trend   
PCE trimmed-mean inflation: official vs. bias-adjusted   
![](images/f4f60b6cb9dde8f5f0735f38491c9ccab4105e67a764d1a7dfee2699235a69f4.jpg)

<details>
<summary>line</summary>

| Year | Bias-adjusted PCE trimmed-mean inflation | PCE trimmed-mean inflation | Core PCE inflation |
|------|------------------------------------------|-----------------------------|--------------------|
| 2006 | ~2.5                                     | ~2.8                        | ~2.4               |
| 2010 | ~1.5                                     | ~0.8                        | ~0.7               |
| 2014 | ~1.2                                     | ~1.6                        | ~1.4               |
| 2018 | ~1.8                                     | ~1.9                        | ~1.7               |
| 2022 | ~5.0                                     | ~5.0                        | ~5.5               |
| 2026 | ~2.8                                     | ~2.4                        | ~3.2               |
</details>

Source: BEA, Dallas Fed, Haver, NOM

Notably, trimmed-mean PCE — which Chair Warsh has highlighted as an alternative gauge of underlying inflation — eased to 2.3% y-o-y, about a full percentage point below core PCE (Fig. 6). In our recent report, we argued that trimmed-mean PCE may be understating inflation risks, particularly because it has been slow to capture shifts in goods inflation dynamics and the recent change in the skewness of the inflation distribution. In our calculation, PCE trimmed-mean inflation underestimates the underlying inflation by 48bp on a y-o-y basis.

Based on recent Fedspeak, it appears that the measure has not yet gained broad-based support to replace core PCE inflation. One outlier is Governor Bowman, who said she has referred to trimmed-mean PCE over the past year “as an alternative measure of the underlying trend in inflation that can look through large one-time actors affecting a few goods categories.” Bowman also referenced the trimmed-mean PCE measure in a January 2026 speech as a useful tool to look through increased volatility in recent inflation data (she cited unusually large price increases in small categories driving the rise in core PCE inflation since September 2025).

# Fed officials discuss scenarios for hikes

Fedspeak this week reflected a broad-based shift towards a more hawkish tone on the FOMC, even as most officials continue to expect disinflation in coming months as their base case. Some policymakers laid out the timeline during which they would like to see evidence of price pressures fading though, before starting to consider hikes more seriously. We continue to expect no changes to the policy rate through the end of the next year.

Governor Cook signaled openness to tightening “if the expected disinflation does not appear in a timely manner.” This joins previous comments from Governor Waller and Boston Fed president Collins about the possibility of rate hikes if inflation fails to decelerate “soon” (Waller) or “in a timely manner” (Collins). Although Cook indicated that her base case is for rates to remain on hold, this is a notable shift since the “timely” comment has typically been a talking point for FOMC hawks.

St. Louis Fed president Musalem was also hawkish, saying that the real policy rate currently sits below the FOMC's estimate of long-run neutral. He said if he does not see disinflation "in the next one to two quarters," that would concern him, which suggests he would not call for an immediate rate hike. Other hawkish FOMC participants remained concerned about inflation risks. Minneapolis Fed President Kashkari stressed upside risks to the inflation outlook and KC Fed President Schmid said he placed "little stock in assuming that the most recent runup in prices is transitory within an acceptable time horizon."

On the other hand, NY Fed president Williams reiterated his view that policy remains “slightly” restrictive and shared his relatively sanguine inflation outlook that recent inflation pressures tied to the Iran war energy shocks, as well as higher tariffs, should peak in coming months. Similarly, Governor Bowman described monetary policy as “moderately” restrictive and attributing elevated inflation readings largely to higher energy prices.

Bowman expected core PCE inflation to be only slightly above 2% after removing one-off shocks, with the caveat that broadening price pressures may lead her to shift her view on the balance of risks. Other dovish policymakers remained cautiously optimistic about the inflation outlook. In her Fox Business interview this morning, SF Fed President Daly supported the Fed's wait-and-see strategy, and expected crude oil prices to come down further, citing the backwardation of crude oil futures. Despite prolonged hostilities in the Middle East, Philly Fed President Paulson delivered a similar speech to the one on 19 May, reiterating that monetary policy is “mildly” restrictive and there was no structural change in inflation dynamics.

Skepticism of labor productivity-led disinflation has been a focus for the FOMC recently. Several officials acknowledged AI's potential to lift longer-run growth, but remain unconvinced that productivity gains can reliability ease inflation in the near term. Cook warned that AI investment could strengthen demand and exacerbate inflation pressures, even as it boosts output, and flagged risks of labor market disruption during the transition. Bowman, by contrast, remained optimistic that productivity growth may offset some inflationary pressure from AI-related supply chain pressures.

St. Louis Fed President Musalem had one of the strongest pushbacks against the productivity-led disinflation argument. He said that evidence of sustained, disinflationary productivity gains remains limited and cautioned that a persistent increase in productivity (his baseline assumption) would likely generate a stronger demand response that offsets supply-side cost relief. Musalem argued that relying on future productivity gains to solve today's inflation problem would be risky, particularly as the labor market stabilizes.

# GDP tracking

Our Q2 GDP tracking estimate stands at 2.4% q-o-q ar from 2.6% last week. Our estimate for real final sales to private domestic purchasers now stands at 2.8% q-o-q ar from 2.9% previously.

Downward revisions to inventory investment in Q1 led us to revise up our Q2 estimate due to the base effect. Slower-than-expected inventory investment was partially offset by a narrowing of the advance goods trade deficit in April.

Additionally, real personal spending and core capex goods shipments both came in below our expectations for April, weighing on our estimates for personal consumption and equipment investment. In addition, a downside surprise in new home sales weighed on our estimate for residential investment.

# Data Preview

# The week ahead

We expect job gains remained solid at 110k in May, and average hourly earnings rebounded.

ISM manufacturing (Monday): We expect the ISM Manufacturing Index ticked up to 53.4 in May from 52.7 in April. The employment index likely ticked up, while supplier delivery times lengthened, reflecting supply chain disruptions due to the Iran war. New orders and production likely ticked down but remained in expansionary territory.

JOLTS job openings (Tuesday): We expect JOLTS job openings fell to 6790k in April from 6866k in March. Our forecast suggests the job openings rate ticked down to 4.10% from 4.15% previously, and the V-U ratio edged lower to 0.92 from 0.95 previously. Data from Indeed and Revelio suggest job openings continued to decline in March and April.

Vehicle sales (Tuesday): We expect vehicle sales rose 16.3mn saar in May from 15.9mnn in April. The average interest rate on new vehicles loans ticked down, while average incentive spending by manufacturers picked up, likely boosting sales.

ISM services (Wednesday): We expect the ISM Services Index edged up to 53.9 in May from 53.6 in April. Regional services surveys suggest business activity softened in the month, while new orders rose. The price index remained elevated and the employment index likely returned to expansionary territory.

Fed Beige Book (Wednesday): We expect the Beige Book's description of economic activity remained stable in May, with activity increasing “at a slight to modest pace.” Regional Fed surveys throughout the month were mixed, but a majority of surveys showed some improvement in activity. On employment, a range of indicators point to positive momentum in most districts and a limited impact of AI thus far.

We expect the Beige Book will continue to emphasize the impacts of t

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
