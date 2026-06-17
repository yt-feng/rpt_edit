你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
EQUITY: METALS & MINING

# Update on China coking coal disruptions

China coking coal supply resumes, but recovery remains uneven; seaborne prices stable for now

## Mine restarts underway, but supply normalization remains gradual, reinforcing our regulatory-risk thesis

Following the fatal Shanxi mine accident in late May-26 (link), several suspended coking coal mines have gradually resumed operations. According to a Mysteel survey (link), 77 mines had restarted by 11 June 2026, representing around $56\%$ of the suspended 137 mines in Shanxi since 23 May 2026 (Fig. 9). However, the recovery remains uneven, with some mines reportedly suspending operations again after only a few days of resumption amid intensified safety inspections. Notably, authorities have expanded inspections across major mining regions, particularly targeting illegal and hidden mining tunnels (link).

## China domestic coking coal prices continue to reflect supply concerns

Despite resumption of some mining activity, domestic prices reflect uncertainties around coal availability. China's spot domestic coking coal price has climbed to USD270/t, up more than $10\%$ since the incident (Fig. 8), suggesting the market is pricing in a broader tightening in domestic steelmaking raw material availability rather than an isolated operational event.

## Australian exports to China rise as buyers seek seaborne supply

Recent developments strengthen our view that prolonged safety-led disruptions in China could gradually shift demand towards seaborne coking coal markets. Australia's coking coal exports to China surged 114% m-m (+77% y-y) to 1.48MT in May-26, with Australia's share of exports to China rising to \~11% in May-26 from \~7% in both May-25 and Apr-26, although it remains a relatively small contributor to China's overall coking coal requirements (link).

While we believe China can offset part of the disrupted supply via inland imports, primarily Mongolia/Russia (Fig. 4), logistics constraints and quality differences might limit full substitution. Consequently, if inspections persist, mine resumptions are delayed and domestic supply recovery remains uneven, China may increasingly rely on Australia's seaborne supplies potentially pressuring global coking coal prices, in our view. However, Australian spot premium hard coking coal prices have largely remained stable and increased marginally by around $1.5\%$ to USD244/t so far since the incident.

## Indian steelmakers' margins largely shielded as China's coal supply recovers

For Indian steelmakers, the primary transmission mechanism is imported coking coal costs. As a directional sensitivity, we calculate that every USD10/t increase in coking coal can create \~USD7-9/t EBITDA impact for integrated steelmakers, depending on inventory cover and coal blend assumptions. Within our coverage, we believe JSW Steel and Tata Steel India would be the most exposed (Fig. 5), with partial impact on Jindal Steel depending on the procurement mix. However, the gradual resumption of coking coal supply in China is likely to keep seaborne coking coal prices relatively stable and therefore, may not be incrementally negative for near-term margin expectations of Indian steel players, in our view (Fig. 11).

We maintain our Buy recommendations on Tata Steel (TATA IN), JSW Steel (JSTL IN), Jindal Steel (JINDALST IN) and Lloyds Metals (LLOYDSME IN).

## Research Analysts

India Metals & Mining

Jashandeep Singh Chadha - NFASL

jashandeep.singhchadha@NOM.com

+91 22 40374124

Fig. 1: China's coal production run-rate suggests \~500MT of coal production in CY26F  
China Met coal production (MT)  
![](images/f75f8f8c508f78a5370216e7d86294db3d89ed5b04795f86df94d1c402e294e0.jpg)

<details>
<summary>bar chart</summary>

| Year | Value |
| :--- | :--- |
| 2021 | 458 |
| 2022 | 471 |
| 2023 | 490 |
| 2024 | 486 |
| 2025 | 502 |
| 2026* | 167 |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 2: Shanxi is the biggest coal producing province in China; it accounts for \~25% of total coal and >20% of met coal  
China top 5 coal producing states (ex-Inner Mongolia)  
![](images/f1515e25b4372e7f55006fc925e29fbce84731b32481b8bb15a079867d09a9f8.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Shanxi (%) | Hebei (%) | Xinjiang (%) | Shaanxi (%) | Shandong (%) |
|---|---|---|---|---|---|
| 2021 | 24 | 10 | 6 | 10 | 7 |
| 2022 | 23 | 10 | 6 | 11 | 7 |
| 2023 | 22 | 10 | 8 | 10 | 7 |
| 2024 | 21 | 10 | 9 | 10 | 7 |
| 2025 | 23 | 10 | 9 | 10 | 7 |
| 2026* | 22 | 10 | 9 | 9 | 7 |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 3: China accounts for \~20-25% of global seaborne coking coal trade, in our view  
![](images/4d3268552fe4b571e9cdc8f1ef7df0cc2942cd2916a153fbfe81d5528d986745.jpg)

<details>
<summary>bar chart</summary>

China coking coal imports (MT)
| Year | Value (MT) |
| :--- | :--- |
| 2021 | 55 |
| 2022 | 64 |
| 2023 | 103 |
| 2024 | 122 |
| 2025 | 119 |
| 2026* | 44 |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 4: Mongolia should be China's first mitigation lever in case of supply shortfall  
![](images/8fef97bdd8d910650daa43f56038e903d01990104b5cab3b3b3456ce04e4cbb8.jpg)

<details>
<summary>stacked bar chart</summary>

China coking coal importing countries (%)
| Year | Mongolia (%) | Russia (%) | Canada (%) | United States (%) | Australia (%) | Indonesia (%) | Others (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2021 | 26 | 20 | 18 | 19 | 13 | 4 | 3 |
| 2022 | 40 | 33 | 15 | 7 | 4 | 3 | 3 |
| 2023 | 53 | 26 | 7 | 6 | 3 | 4 | 2 |
| 2024 | 46 | 25 | 8 | 10 | 8 | 3 | 2 |
| 2025 | 51 | 28 | 9 | 5 | 8 | 3 | 1 |
| 2026* | 61 | 27 | 6 | 3 | 6 | 1 | 1 |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 5: JSW Steel has the highest exposure to imported coking coal among our coverage, followed by Tata Steel; Jindal Steel appears better placed  
![](images/843f46f700008340b0b0660dfa5548b32fa4bf4b685127d80e194e310f292951.jpg)

<details>
<summary>stacked bar chart</summary>

| Year   | SAIL  | JSW Steel | Tata Steel | RINL  | Jindal Steel | Bhushan Power & Steel | NMDC  | Others |
|--------|-------|-----------|------------|-------|--------------|------------------------|-------|--------|
| 2020   | 25%   | 18%       | 17%        | 5%    | 7%           | 3%                     | 4%    | 15%    |
| 2021   | 24%   | 19%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 17%    |
| 2022   | 29%   | 18%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 15%    |
| 2023   | 26%   | 19%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 16%    |
| 2024   | 25%   | 19%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 17%    |
| 2025   | 22%   | 19%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 19%    |
| 2026*  | 19%   | 20%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 20%    |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 6: China's coking coal imports have increased significantly as a % of consumption; any domestic supply gap can lead to increased global prices  
![](images/b3d3d7c805ddd272fcc7244072fdaee4c305c83a20f0b37824a803a3569b9d33.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | China Coking Coal Imports/Consumption Ratio | Median (last 9 years, in INR) |
|--------|---------------------------------------------|-------------------------------|
| Apr-17 | 10%                                         | 13%                           |
| Apr-18 | 15%                                         | 13%                           |
| Apr-19 | 17%                                         | 13%                           |
| Apr-20 | 19%                                         | 13%                           |
| Apr-21 | 14%                                         | 13%                           |
| Apr-22 | 18%                                         | 13%                           |
| Apr-23 | 28%                                         | 13%                           |
| Apr-24 | 26%                                         | 13%                           |
| Apr-25 | 34%                                         | 13%                           |
| Apr-26 | 24%                                         | 13%                           |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 7: Gap between Australian and Chinese coking coal has narrowed due to the pick up in the latter's prices  
![](images/7ca56c968f202f5ca891e229af9260a974a12c2406fba3dce606df351fa3aa3f.jpg)

<details>
<summary>line chart</summary>

| Date   | China domestic coking coal premium/(discount) over Australia (USD/t) |
|--------|---------------------------------------------------------------------|
| May-17 | ~0                                                                  |
| May-18 | ~-50                                                                |
| May-19 | ~0                                                                  |
| May-20 | ~50                                                                 |
| May-21 | ~100                                                                |
| May-22 | ~200                                                                |
| May-23 | ~50                                                                 |
| May-24 | ~0                                                                  |
| May-25 | ~-50                                                                |
| May-26 | ~0                                                                  |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 8: China's domestic coking coal spot prices are trading over $10\%$ higher since the incident  
![](images/d972493eeee365589166b463e888b3af406f0bd83b06b400abe20e2b5cdf00fe.jpg)

<details>
<summary>line chart</summary>

| Date   | Price (USD/t) |
|--------|---------------|
| Jun-20 | 170           |
| Jun-21 | 300           |
| Jun-22 | 480           |
| Jun-23 | 230           |
| Jun-24 | 280           |
| Jun-25 | 180           |
| Jun-26 | 270           |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 9: Number of coking coal mines halted and resumed at Shanxi  
![](images/3bf367fc345e928eceddc6c663100f75a03affbc8a86ae742856fad5559f8b45.jpg)

<details>
<summary>stacked bar chart</summary>

| Date | Halted | Resumed |
|---|---|---|
| 25 May'26 | 109 | 0 |
| 27 May'26 | 113 | 16 |
| 29 May'26 | 112 | 18 |
| 1 Jun'26 | 87 | 43 |
| 3 Jun'26 | 75 | 59 |
| 5 Jun'26 | 74 | 61 |
| 8 Jun'26 | 65 | 70 |
| 10 Jun'26 | 56 | 81 |
| 11 Jun'26 | 60 | 77 |
</details>

Source: BigMint, Mysteel Global, NOM

Fig. 10: China's export HRC margins levels have recovered recently due to higher realization but remain below median levels  
![](images/f54a539827c6cffc410fac87787ba818844a2466e01be5b4e659c7f1ed20fad9.jpg)

<details>
<summary>line chart</summary>

| Date   | China Export HRC Margins (USD/Ton) |
|--------|------------------------------------|
| Jun-19 | 150                                |
| Jun-20 | 250                                |
| Jun-21 | 550                                |
| Jun-22 | 350                                |
| Jun-23 | 250                                |
| Jun-24 | 200                                |
| Jun-25 | 180                                |
| Jun-26 | 170                                |
</details>

Note: Margins calculated using Australia iron ore and China domestic coking coal prices  
Source: Bloomberg Finance L.P., NOM

Fig. 11: India steelmakers' margins have moderated recently as HRC prices ease, but remain at healthy levels  
![](images/a03795cbc70954d2e6d25ee899fc93e900f336130617d7fb9f5764fe63c3dc10.jpg)

<details>
<summary>line chart</summary>

| Date   | India HRC Margin (INR/t) |
|--------|--------------------------|
| Jun-19 | 27,000                   |
| Jun-20 | 28,000                   |
| Jun-21 | 49,000                   |
| Jun-22 | 47,000                   |
| Jun-23 | 39,000                   |
| Jun-24 | 32,000                   |
| Jun-25 | 34,000                   |
| Jun-26 | 36,000                   |
</details>

Note: Margins calculated using domestic iron ore and Australia coking coal prices  
Source: Bloomberg Finance L.P., NOM

## Appendix A-1

This report has been produced by NOM Financial Advisory and Securities (India) Private Limited (NFASL), India.

See Disclaimers for NOM Group entity details.

## Analyst Certification

I, Jashandeep Singh Chadha, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>Jindal Steel</td><td>JINDALST IN</td><td>INR 1,140</td><td>16-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>JSW Steel</td><td>JSTL IN</td><td>INR 1,274</td><td>16-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Lloyds Metals and Energy</td><td>LLOYDSME IN</td><td>INR 1,765</td><td>16-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Tata Steel</td><td>TATA IN</td><td>INR 196</td><td>16-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

Jindal Steel (JINDALST IN)  
Rating and target price chart (three year history)  
![](images/51c6e371dfc5023940238e2d1b8394a17abab91a181ede049f2243c560696a3f.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2024/07/01 | ~1000.00      | -                   | -                      |
| 2025/01/01 | ~950.00       | -                   | -                      |
| 2026/01/01 | ~1300.00      | -                   | -                      |
| As of 16-Jun-2026 | -           | -                   | INR                    |
</details>

INR 1,140 (16-Jun-2026) Buy (Sector rating: N/A)

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>04-May-26</td><td></td><td>1,350.00</td><td>1,261.00</td></tr><tr><td>01-Feb-26</td><td></td><td>1,280.00</td><td>1,131.00</td></tr><tr><td>22-Sep-25</td><td></td><td>1,150.00</td><td>1,033.00</td></tr><tr><td>31-Jan-25</td><td></td><td>1,080.00</td><td>792.00</td></tr><tr><td>07-Nov-24</td><td></td><td>1,180.00</td><td>947.00</td></tr><tr><td>02-Oct-24</td><td>Buy</td><td></td><td>1,036.00</td></tr><tr><td>02-Oct-24</td><td></td><td>1,200.00</td><td>1,036.00</td></tr></table>

Source: LSEG, NOM  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We arrive at TP of Rs1,350 by applying slightly higher than mid-cycle one-year-forward EV/EBITDA of 8.0x on new steady-state EBITDA in June-28F. The benchmark for this stock is NIFTY50

Risks that may impede the achievement of the target price 1. Lower spreads - If Chinese HRC m

[中间内容因长度限制已省略]

uthority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public

offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Financial Advisory and Securities (India) Private Limited, India. All rights reserved.
"""
