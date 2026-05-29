你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：约 850 字，允许上下浮动 15%。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

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

The components excluded from PCE trimmed-mean may offer a better early signal around inflation turning points. A closer look at the distribution of cross-sectional monthly price changes suggests the weighted average of components trimmed from both tails began to react to the pandemic-induced inflation wave as early as Q1 2021, much earlier than PCE trimmed-mean inflation did (Fig. 4). The same dynamic was visible in the

[中间内容因长度限制已省略]

rofessional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

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
