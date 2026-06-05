你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
HOUSING AND MORTGAGE MONITOR

Manufacturing a solution to the housing shortage

# Shipments of manufactured homes remain well below pre-2000 levels

Affordability continues to be a major concern in the housing market. Our economics team estimates there is currently a shortage of approximately 3-4 million homes nationwide. One approach for increasing the supply of homes at more affordable price points is to promote access to manufactured housing. Manufactured homes (MH), colloquially also referred to as mobile homes, are residences that are prefabricated in a factory setting and then transported to their final location for installation. This method not only streamlines the construction process but also offers significant cost savings compared to traditional site-built homes, making manufactured housing a promising solution for those seeking affordable housing options. There are currently about 8.4 million manufactured housing units across the country.

Prior to 2000, shipments of manufactured homes averaged about 265k a year (Exhibit 1). Manufactured housing experienced a construction boom in the 1990s driven by overproduction and lax lending standards. However, this ended in a sharp increase in delinquencies, which was then followed by tighter lending standards and increased zoning restrictions. These restrictions reduced the attractiveness of manufactured housing. During the housing boom of the early 2000s, manufactured housing was increasingly viewed as a choice of last resort. The negative sentiment towards this sector has largely persisted with MH shipments averaging just 80,000 units a year since 2010. According to the 2024 American Community Survey, manufactured housing units account for about 6% of all owner-occupied housing in the US, although the share has drifted marginally lower from around 7% in 2010.

The top markets for manufactured homes are in the South and Southeast (Exhibit 2). Interestingly, several states that rank high in manufactured home sales rank low in single family home construction, suggesting the importance of local zoning and land-use regulations as a key constraining factor for the growth of MH. Over 54% of manufactured housing units are in rural areas (defined as territories with fewer than 2,500 people), while single-family homes are primarily in large urban areas (Exhibit 3). Manufactured homes are generally smaller than site-built homes and are historically viewed as starter homes for lower-income households (Exhibit 4).

Arun Manohar

+1(212)902-8763

arun.manohar@gs.com

GS & Co. LLC

Ben Shumway

+1(801)578-2553

ben.shumway@gs.com

GS & Co. LLC

Neth Karunamuni

+1(212)934-0799

neth.karunamuni@gs.com

GS & Co. LLC

# Table of Contents

Housing Forecasts and Key Charts 8   
Economic growth remains positive year over year 9   
US housing affordability is still poor 10   
Home sales volume has fallen 11   
Supply of completed homes remains constrained 12   
33% of new GSE purchase mortgages have DTI above 43% 13   
Homeownership rates have ticked down in Q12026 14   
Sequential home price growth has slowed 15   
Most US metros are seeing home price growth stabilize 16   
Household balance sheet metrics remain resilient 17   
Subprime auto ABS losses have grown 18   
2.2% of mortgaged properties have negative equity 19   
30-year FNMA prepayment rates were down 16% in April vs. March 20   
Conventional MBS prepayment rates decreased for higher coupons in April vs. March 21   
High coupon Ginnie Mae prepayments decreased month-on-month 22   
About 20% of mortgage borrowers are in-the-money for refinancing 23   
The Federal Reserve's agency MBS assets remain below \$2.1 trillion 24   
Agency MBS valuations have improved recently 25

CMBS delinquency rates remain contained despite challenging CRE fundamentals 26   
High CMBS note rates will be an obstacle to debt refinancing 27   
Apartment property prices have declined 28   
CMBS spreads have tightened 29   
Disclosure Appendix 30

Exhibit 1: Shipments of manufactured homes experienced a significant decline after 2000 and continue to stay at low levels today   
Shipments of new manufactured homes   
![](images/ddbcc5cb4e919b4826d46ddde33a0fdbd7d9ed1586578b70e3d127fab39a8526.jpg)

<details>
<summary>line</summary>

| Year | Shipments of manufactured homes (SAAR) (Thous.) |
|------|--------------------------------------------------|
| 75   | ~200                                             |
| 77   | ~280                                             |
| 79   | ~300                                             |
| 81   | ~170                                             |
| 83   | ~310                                             |
| 85   | ~280                                             |
| 87   | ~250                                             |
| 89   | ~220                                             |
| 91   | ~160                                             |
| 93   | ~250                                             |
| 95   | ~350                                             |
| 97   | ~380                                             |
| 99   | ~390                                             |
| 01   | ~200                                             |
| 03   | ~130                                             |
| 05   | ~120                                             |
| 07   | ~100                                             |
| 09   | ~50                                              |
| 11   | ~60                                              |
| 13   | ~70                                              |
| 15   | ~80                                              |
| 17   | ~90                                              |
| 19   | ~85                                              |
| 21   | ~100                                             |
| 23   | ~110                                             |
| 25   | ~105                                             |
</details>

Source: US Census, Haver Analytics, GS Global Investment Research

Exhibit 2: Several states that rank high in manufactured home sales rank low in single family home construction   
![](images/942f34d609728a8b753f3e80eb9b65fb801c3e1bd86cf3eaf2bcb9716c8b51f2.jpg)

<details>
<summary>bar</summary>

| State | Manufactured Housing Shipments (%) | Single-family (1-4 units) housing authorized (%) |
|---|---|---|
| Texas | 17.0 | 15.6 |
| Florida | 6.7 | 12.0 |
| North Carolina | 6.1 | 7.0 |
| Alabama | 5.2 | 1.6 |
| South Carolina | 5.2 | 4.2 |
| Georgia | 4.8 | 4.8 |
| Louisiana | 4.5 | 1.2 |
| Mississippi | 3.9 | 0.8 |
| Tennessee | 3.8 | 3.4 |
| Kentucky | 3.8 | 1.0 |
| Michigan | 3.6 | 1.8 |
| California | 3.0 | 6.5 |
| Oklahoma | 2.5 | 1.3 |
| Arizona | 2.2 | 3.6 |
| Ohio | 2.1 | 2.0 |
| Indiana | 2.0 | 2.1 |
| Pennsylvania | 1.9 | 1.8 |
| Arkansas | 1.8 | 1.2 |
| Missouri | 1.8 | 1.4 |
| New York | 1.7 | 1.5 |
</details>

Source: US Census, GS Global Investment Research

Exhibit 3: Manufactured homes account for a greater share of homes in rural areas   
![](images/fba6c22ea25cf80fad0dd7ce71c956cb0c34b7f1f8d947539bdc21ba8047dd52.jpg)

<details>
<summary>bar</summary>

Distribution by geographical areas
| Area | Single family (%) | Manufactured Housing (%) |
| :--- | :--- | :--- |
| Urbanized Area (territories with >= 50,000 people) | 65.5 | 32.8 |
| Urban Cluster (2,500 to 50,000 people) | 9.8 | 13.4 |
| Rural (<2,500 people) | 25.2 | 54.1 |
</details>

Source: US Census, 2023 National American Housing Survey, GS Global Investment Research

Exhibit 4: Typically, manufactured homes have less square footage than site-built single-family homes   
![](images/d37dbf61108065402a1defd5affef207337d5d02471c6f50aad9b2ff8f8faac5.jpg)

<details>
<summary>bar</summary>

Distribution of square footage
| Square Footage Range | Single family (%) | Manufactured Housing (%) |
| :--- | :--- | :--- |
| <500 | 1 | 5.5 |
| 500-750 | 2 | 9.5 |
| 750-1000 | 6.5 | 22.5 |
| 1000-1500 | 24.5 | 37.5 |
| 1500-2000 | 25.5 | 17.5 |
| 2000-2500 | 18 | 4.5 |
| 2500-3000 | 10 | 1.5 |
| 3000-4000 | 9.5 | 1 |
| >=4000 | 4.5 | 1 |
</details>

Source: US Census, 2023 National American Housing Survey, GS Global Investment Research

# The main attraction of manufactured housing is its affordability

Manufactured housing provides a cost-effective alternative to traditional site-built starter homes. Among various actions to enhance housing affordability, expanding access to manufactured housing has received bipartisan support in recent months. Manufactured homes can be produced at a lower cost and are typically smaller, thereby contributing to increased affordability despite higher mortgage rates. As a result, easier access to MH can enable homeownership rates to rise. On average, manufactured housing is approximately half as expensive as site-built homes, excluding land costs (Exhibit 5).

Exhibit 5: Manufactured housing is more affordable vs. site-built housing   
Comparison of average sale price (left panel) and average cost of structure per square foot (right panel) across manufactured homes and site-built homes   
![](images/a92f7db4e24b546185a2e880e36477f469779772d588201b94204aa1e6389361.jpg)

<details>
<summary>line</summary>

| Year | Manufactured homes ($Thous.) | Site-built homes ($Thous.) |
|------|-------------------------------|-----------------------------|
| 2014 | ~65                           | ~350                        |
| 2015 | ~70                           | ~355                        |
| 2016 | ~75                           | ~365                        |
| 2017 | ~80                           | ~390                        |
| 2018 | ~85                           | ~390                        |
| 2019 | ~90                           | ~390                        |
| 2020 | ~95                           | ~395                        |
| 2021 | ~110                          | ~450                        |
| 2022 | ~130                          | ~520                        |
| 2023 | ~125                          | ~515                        |
| 2024 | ~125                          | ~515                        |
</details>

![](images/07f7280bcde9c9f34ef7b1f449ea030c7ede5e094804b7e8db5ac1643e95eb00.jpg)

<details>
<summary>line</summary>

| Year | Manufactured homes | Site-built homes |
| ---- | ------------------ | ---------------- |
| 2014 | 45                 | 98               |
| 2015 | 47                 | 100              |
| 2016 | 49                 | 105              |
| 2017 | 51                 | 110              |
| 2018 | 55                 | 115              |
| 2019 | 57                 | 120              |
| 2020 | 60                 | 125              |
| 2021 | 70                 | 145              |
| 2022 | 88                 | 168              |
| 2023 | 86                 | 166              |
| 2024 | 84                 | 170              |
</details>

Source: US Census, GS Global Investment Research

# Zoning, financing, and negative perception are key impediments to manufactured housing demand

Manufactured housing demand faces major obstacles from local zoning regulations, financing difficulties, and negative public perception. Broadly, there is a lack of sufficient awareness. In a 2022 Manufactured Housing survey conducted by Freddie Mac, 53% of the respondents reported having never heard of or being unfamiliar with MH, while only 17% reported being very familiar with the sector. Limited access to affordable financing has been a major challenge for the sector in recent years.

Manufactured homes are titled as either real property or personal property based on whether the owner owns the underlying land. Based on industry estimates, about 40% of manufactured housing units are situated within manufactured housing communities, where the homeowner typically does not own the land but rather pays rent to the community operator. When the homebuyer does not own the land on which the home is placed, they use chattel loans to finance the purchase. These loans come with shorter terms, higher interest rates and fewer borrower protections. The combination of shorter terms and higher interest rates makes them less affordable than if the borrower were to obtain a traditional mortgage. Also, in the case of payment defaults, lenders can more easily repossess properties backed by chattel loans (as they are treated as personal property like autos) without having to initiate a foreclosure process.

In response to MH quality issues in the past, HUD published a comprehensive building code in 1976 that set minimum material quality and energy efficiency standards for manufactured housing. As part of this code, HUD required manufactured housing units to be built on a permanent steel chassis. While the presence of this steel structure may have helped improve the structural integrity of the unit, lenders likely viewed the home as more akin to a movable property than an immovable property. The presence of a permanent chassis also increased the cost of the home.

Finally, even if the borrower owns the land and obtains a traditional MH mortgage, the fixed costs of origination may be prohibitively high compared to size of the mortgage.

# Proposed changes are a step in the right direction; however, modifications to local zoning regulations will remain necessary

Support for manufactured housing is a key component of the 21st Century Road to Housing Act, which has recently garnered bipartisan backing. Among other proposals, the bill aims to eliminate the permanent chassis requirement, establishes HUD as the primary authority on construction and safety standards for manufactured homes, and increases the loan limits of FHA-insured manufactured housing loans. Removal of the permanent chassis requirement can reduce the cost of manufactured homes by \$5-10k, enable more floor plan flexibility, and could make it easier to obtain local municipality approval. Without a permanent chassis, lenders may be more likely to treat these homes like site-built properties since they are less likely to be moved. Hence, financing terms for MH borrowers could become more favorable. The industry is optimistic about these proposals (Exhibit 6).

Exhibit 6: The industry is optimistic about the effects of the proposed manufactured housing changes in the 21st Century Road to Housing Act 

<table><tr><td>Ticker</td><td>Company</td><td>Profile</td><td>Date of comments</td><td>Comments</td></tr><tr><td>SUI</td><td>Sun Communities</td><td>REIT operating MH communities</td><td>4/28/2026</td><td>Hugely supportive of anything that supports attainable housing.From a federal perspective, we get the intent, but much of this is local.The removal of the chassis requirement creates some really interesting opportunities potentially, both in the form of cost savings and making the product even more affordable, but at the same time, being able to build houses that have a different spec level and are more appealing to not just the consumers, but to the powers that be at the local level that ultimately provide the approvals for development that we may do someday. So we think all this is positive. We remain optimistic and encouraged by the progress with it.</td></tr><tr><td>SKY</td><td>Champion Homes</td><td>Manufactured housing builder</td><td>5/26/2026</td><td>It&#x27;s clear the bipartisan focus on solving the affordable housing crisis remains strong, including support for manufactured housing. More broadly, we continue to monitor HUD code evolution, chassis rulemaking, and zoning reform activity at the state and local levels.</td></tr><tr><td>CVCO</td><td>Cavco Industries</td><td>Manufactured housing builder</td><td>5/22/2026</td><td>Various parts of the bill enable product innovation, reduce regulatory confusion, improve consumer and commercial funding availability, and encourage zoning improvement.</td></tr></table>

Source: Company earnings transcripts, Bloomberg, GS Global Investment Research

Recently, HUD released a final rule (effective March 2025) updating the national building code for factory-built manufactured homes introducing the flexibility to have up to four units per structure, which could make the units more competitive, especially in urban areas (in addition to other design upgrades).

However, these changes alone may not resolve all the issues facing the industry. In addition to federal initiatives, changes to local zoning laws are also required. The sector will benefit tremendously if states allow manufactured homes to be titled as real property – Montana and Kentucky recently passed legislation to treat MH on par with site-built homes, while a recent law change in Texas will see more areas within the state be available for MH effective September 2026.

Finally, if the GSEs were to launch a program to finance chattel loans, it could serve as an important benchmark for lending standards for the entire industry and increase access to financing.

Thank you to Patricia Pacheco for her contribution to this publication.

# Housing Forecasts and Key Charts

Exhibit 7: We forecast total mortgage origination volume to be around \$2.2 trillion in 2026   
GS housing and mortgage forecasts 

<table><tr><td rowspan="2">Variable</td><td colspan="4">2026</td><td colspan="3">Annual Data</td></tr><tr><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>2025</td><td>2026</td><td>2027</td></tr><tr><td>Interest Rates</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10-Year Treasury (%)</td><td>4.32</td><td>4.30</td><td>4.20</td><td>4.10</td><td>4.17</td><td>4.10</td><td>4.15</td></tr><tr><td>PMMS 30-Year Fixed-Rate Mortgage (%)</td><td>6.38</td><td>6.40</td><td>6.30</td><td>6.15</td><td>6.18</td><td>6.15</td><td>6.20</td></tr><tr><td>Mortgage Originations</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total 1-4 Family ($Billions)</td><td>551</td><td>513</td><td>557</td><td>558</td><td>2,050</td><td>2,179</td><td>2,127</td></tr><tr><td>Purchase Originations</td><td>332</td><td>373</td><td>388</td><td>352</td><td>1,356</td><td>1,445</td><td>1,460</td></tr><tr><td>Refinance Originations</td><td>219</td><td>140</td><td>169</td><td>206</td><td>694</td><td>734</td><td>667</td></tr><tr><td>Refinance Share (%)</td><td>40</td><td>27</td><td>30</td><td>37</td><td>34</td><td>34</td><td>31</td></tr></table>

Note 1: Annual data for mortgage originations are the sum of quarterly originations.   
Note 2: Interest rates refer to period end values.   
Note 3: Sources for historical data are Census Bureau, NAR, Moody's Analytics, Fe

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a

recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
