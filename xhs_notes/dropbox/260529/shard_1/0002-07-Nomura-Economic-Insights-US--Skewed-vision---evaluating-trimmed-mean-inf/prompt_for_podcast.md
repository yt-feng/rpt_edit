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
