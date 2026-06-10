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
## FX Insights

Global Markets Research

9 June 2026

Foreign Exchange - Asia ex-Japan

## Inflows into US equities remained robust amid AI optimism

- Foreign inflows into US-focused funds remained strong at USD2.6bn between 1 and 5 June, predominantly into equity funds.  
- Outflows from EM-focused ETFs were USD250mn between 1 and 5 June, from inflows of USD475mn over the previous week.  
- Korea's retail investors net bought USD139mn of US portfolio assets between 2 and 6 June, partly reversing outflows of USD601mn in the previous week.  
- Taiwan's investors net sold USD196mn of USD-denominated bond funds between 1 and 5 June, and compared with net selling of USD149mn over the previous week.

## Research Analysts

## Asia FX Strategy

Craig Chan - NSL

craig.chan@NOM.com

+65 6433 6106

Wee Choon Teo - NSL

weechoon.teo@NOM.com

+65 6433 6107

Vicky Chen - NSL

vicky.chen1@NOM.com

+65 6433 6540

Manthan Shingala - NSL

manthan.shingala1@NOM.com

+65 6433 6427

Fig. 1: Summary of flows into US securities

<table><tr><td></td><td colspan="3">Foreign investments in US-focused funds (ETF and MF)</td><td colspan="3">EM-focused ETFs</td><td colspan="3">Korea retail investments</td><td>Taiwan investments in local ETFs</td></tr><tr><td>USD mn</td><td>US Equities</td><td>US Bonds</td><td>Total</td><td>Equity funds</td><td>Bond funds</td><td>Total</td><td>US Equities</td><td>US Bonds</td><td>Total</td><td>USD-denominated Bonds</td></tr><tr><td>Latest week (5 sessions)</td><td>2,559</td><td>6</td><td>2,565</td><td>-363</td><td>113</td><td>-250</td><td>235</td><td>-95</td><td>139</td><td>-196</td></tr><tr><td>Previous week (previous 5 sessions)</td><td>2,905</td><td>209</td><td>3,114</td><td>184</td><td>291</td><td>475</td><td>-501</td><td>-101</td><td>-601</td><td>-149</td></tr><tr><td>Monthly flow in June</td><td>2,851</td><td>-34</td><td>2,817</td><td>-362</td><td>113</td><td>-249</td><td>-452</td><td>-121</td><td>-573</td><td>-197</td></tr><tr><td>Monthly flow in May</td><td>8,780</td><td>776</td><td>9,556</td><td>2,418</td><td>51</td><td>2,469</td><td>-940</td><td>372</td><td>-568</td><td>183</td></tr><tr><td>Monthly flow in April</td><td>3,091</td><td>103</td><td>3,194</td><td>5,832</td><td>453</td><td>6,285</td><td>-469</td><td>-441</td><td>-910</td><td>-339</td></tr><tr><td>Monthly flow in March</td><td>-110</td><td>-1,412</td><td>-1,522</td><td>-237</td><td>-2,646</td><td>-2,882</td><td>1,691</td><td>-166</td><td>1,525</td><td>-29</td></tr><tr><td>Monthly flow in February</td><td>4,605</td><td>85</td><td>4,690</td><td>18,920</td><td>184</td><td>19,104</td><td>3,949</td><td>257</td><td>4,206</td><td>-662</td></tr><tr><td>Monthly flow in January</td><td>9,564</td><td>2,669</td><td>12,233</td><td>25,150</td><td>401</td><td>25,551</td><td>5,003</td><td>396</td><td>5,399</td><td>1,065</td></tr></table>

Note: Note: The latest weekly data are up to 5 June for US equity and bond-focused ETFs and mutual funds, 5 June for EM-focused ETFs, 6 June for Korea retail investors and 5 June for Taiwan investors. Data for the previous week are the preceding 5 sessions of the latest week.
Source: Bloomberg, KSD, NOM

## Weekly update of high-frequency investor flows

- Foreign inflows into US-focused equity ETFs and mutual funds[1] totaled USD2.6bn between 1 and 5 June (Figure 3), and compared with inflows of USD2.9bn over the previous week. In May, inflows into these funds totaled USD8.8bn, the largest inflows since USD9.5bn in January 2026 (Figure 2).  
- Foreign inflows into US-focused bond ETFs and mutual funds $^{[2]}$ were largely flat at USD6mn between 1 and 5 June, slowing from inflows of USD209mn in the previous week (Figure 5). In May, inflows into these funds totaled USD776mn, following inflows of USD103mn in April 2026 (Figure 4).  
- Foreign outflows from EM-focused ETFs[3] totaled USD250mn between 1 and 5 June following inflows of USD475mn in the previous week. In May, foreign investors net bought USD2.5bn of EM funds, down from USD6.3bn in April (Figures 6 and 7)  
- Outflows from Taiwan's exchange-listed USD bond ETFs amounted to USD196mn (1 to 5 June), following outflows of USD149mn over the previous week (Figure 9). In May, Taiwanese investors net bought USD183mn of USD denominated bonds, partially offsetting the USD339mn of selling in April (Figure 8).  
- Korean retail investors net bought USD139mn of US portfolio assets from 2 to 8 June. This consisted of net selling of USD95mn of US bonds and net buying of USD235mn of US equities (Figures 10 and 11). We observe Korea's retail investors are starting to net buy US portfolio assets this week, after two months of net selling.

Fig. 2: Foreign flows into US-focused equity ETFs and mutual funds (monthly)  
![](images/8f59d63a2861e020553b60e5ebed1e6c2d72def031cc28b5283b06ae52bb3820.jpg)

<details>
<summary>bar chart</summary>

| Month    | Foreign flows into US-focused equity funds (USD bn) |
| -------- | -------------------------------------------------- |
| Dec-23   | 7.0                                                |
| Jan-24   | 10.0                                               |
| Feb-24   | 11.0                                               |
| Mar-24   | 6.0                                                |
| Apr-24   | 5.0                                                |
| May-24   | 4.5                                                |
| Jun-24   | 12.0                                               |
| Jul-24   | 12.5                                               |
| Aug-24   | 8.0                                                |
| Sep-24   | 9.5                                                |
| Oct-24   | 8.0                                                |
| Nov-24   | 21.0                                               |
| Dec-24   | 16.0                                               |
| Jan-25   | 16.0                                               |
| Feb-25   | 3.0                                                |
| Mar-25   | 0.5                                                |
| Apr-25   | 1.5                                                |
| May-25   | 0.5                                                |
| Jun-25   | -3.0                                               |
| Jul-25   | 0.0                                                |
| Aug-25   | 4.5                                                |
| Sep-25   | 6.5                                                |
| Oct-25   | 5.0                                                |
| Nov-25   | -1.0                                               |
| Dec-25   | 3.5                                                |
| Jan-26   | 9.6                                                |
| Feb-26   | 4.6                                                |
| Mar-26   | -0.1                                               |
| Apr-26   | 3.1                                                |
| May-26   | 8.8                                                |
| Jun-26   | 2.9                                                |
</details>

Note: June's data are up to 5 June.  
Source: Bloomberg, NOM.

Fig. 4: Foreign flows into US-focused bond ETFs and mutual funds (monthly)  
![](images/28e34c6e71291e83c33c1e2bdba0dded96abb097122007e84f3d79e7472c6146.jpg)

<details>
<summary>bar chart</summary>

| Date | Foreign flows into US-focused bond funds (ETFs and mutual funds; monthly) |
| --- | --- |
| Dec-23 | 2.0 |
|  | 4.0 |
|  | 4.0 |
|  | 3.5 |
|  | 3.5 |
|  | 5.0 |
| Jun-24 | 5.5 |
|  | 4.0 |
|  | 8.0 |
|  | 3.0 |
| Dec-24 | 2.0 |
|  | 1.0 |
|  | 1.5 |
|  | 1.0 |
|  | -1.0 |
|  | -4.0 |
| Jun-25 | 2.0 |
|  | 4.5 |
|  | 3.0 |
|  | -2.0 |
| Dec-25 | 2.5 |
|  | 2.0 |
|  | 1.5 |
|  | 2.7 |
|  | -1.4 |
|  | -1.0 |
|  | 0.1 |
|  | 0.1 |
| Jun-26 | 0.8 |
|  | 0.0 |
</details>

Note: June's data are up to 5 June.  
Source: Bloomberg, NOM.

Fig. 6: Foreign flows into EM-focused ETFs (Monthly)  
![](images/c762b2ddc7fcf18790ee753a3ac62f0d4d4b8d2dd6dc6c0184b5e89a82ffcbef.jpg)

<details>
<summary>line chart</summary>

| Date    | foreign flow to EM-focused ETFs (USD bn) | total foreign flows to EM-focused ETFs (USD bn) |
|---------|------------------------------------------|--------------------------------------------------|
| Dec-23  | 0.0                                      | 6.0                                              |
| Jun-24  | 0.0                                      | 1.0                                              |
| Dec-24  | 0.0                                      | 3.0                                              |
| Jun-25  | 0.0                                      | 10.0                                             |
| Dec-25  | 0.0                                      | 25.6                                             |
| Jun-26  | 0.0                                      | -2.9                                             |
</details>

Note: June's data are up to 5 June.  
Source: Bloomberg, NOM

Fig. 3: Foreign flows into US-focused equity ETFs and mutual funds (daily)  
![](images/2e8b3fa9dbab9667f403a2cea174e78a5b43c424d7fbc66b4b89e71dd606334f.jpg)

<details>
<summary>bar chart</summary>

| Date | Foreign flows into US-focused equity funds (ETFs + mutual funds) (USD mn) |
|---|---|
| 20-May | 419 |
| 20-May | -112 |
| 25-May | 143 |
| 25-May | 552 |
| 25-May | 77 |
| 25-May | 228 |
| 28-May | 990 |
| 28-May | 790 |
| 28-May | 820 |
| 2-Jun | 528 |
| 2-Jun | 704 |
| 2-Jun | 775 |
| 5-Jun | 54 |
| 5-Jun | 498 |
</details>

Source: Bloomberg, NOM.

Fig. 5: Foreign flows into US-focused bond ETFs and mutual funds (daily)  
![](images/891510d3b8750f1ff025bac5626d851317e56c1a71a04ca88cf33f2fd6da65fa.jpg)

<details>
<summary>bar chart</summary>

| Date | Foreign flows into US-focused bond funds (ETFs + mutual funds) (USD mn) |
| :--- | :--- |
| 15-May | 214 |
| 20-May | -97 |
| 25-May | 79 |
| 28-May | 202 |
| 2-Jun | -10 |
| 5-Jun | 12 |
| 15-May | 243 |
| 28-May | -175 |
| 2-Jun | -170 |
| 5-Jun | -28 |
| 6-Jun | 68 |
| 7-Jun | 66 |
| 8-Jun | 60 |
| 9-Jun | 62 |
| 10-Jun | 82 |
</details>

Source: Bloomberg, NOM.

Fig. 7: Foreign flows into EM-focused ETFs (Daily)  
![](images/524e4e015854845b31a902c6021388f49c517901e40adfeee792eb85ce758103.jpg)

<details>
<summary>bar-line hybrid</summary>

| Date | Flows to bonds (USD mn) | Flows to equities (USD mn) | Total flows (USD mn) |
| :--- | :--- | :--- | :--- |
| 20-May | -10 | 367 | 367 |
| | 120 | 295 | 295 |
| | 133 | -8 | 133 |
| 25-May | 53 | 36 | 36 |
| | 100 | 53 | 53 |
| 28-May | 39 | 39 | 39 |
| | 70 | 210 | 210 |
| | 137 | -429 | -429 |
| 2-Jun | 61 | 195 | 195 |
| | 150 | 104 | 104 |
| 5-Jun | -80 | -80 | -80 |
</details>

Source: Bloomberg, NOM

Fig. 8: Taiwan flows into ETFs invested in USD bonds (monthly)  
![](images/09b664d669e62249e9809fd1c653be6beaf8342a4a80c7881fbfec87368db8b9.jpg)

<details>
<summary>bar chart</summary>

| Date    | Flows (USD bn) |
|---------|----------------|
| Dec-23  | 3.4            |
|         | 4.0            |
|         | 3.2            |
|         | 3.7            |
|         | 2.5            |
|         | -0.5           |
| Jun-24  | 3.7            |
|         | 2.0            |
|         | 5.8            |
|         | 2.0            |
|         | 1.8            |
|         | 0.5            |
|         | 0.9            |
|         | -1.2           |
|         | -1.5           |
|         | 0.3            |
| Jun-25  | 2.8            |
|         | 0.6            |
|         | -0.4           |
|         | 0.4            |
|         | 0.9            |
|         | 1.1            |
|         | -0.7           |
|         | -0.3           |
| Jun-26  | 0.2            |
</details>

Note: June's data are up to 5 June.  
Source: Bloomberg, NOM.

Fig. 9: Taiwan flows into ETFs invested in USD bonds (daily)  
![](images/c3c07d59b0a3fa43e9f826c5bb62fbd84e324ac5c990ef1373041dc21338ed45.jpg)

<details>
<summary>bar chart</summary>

Flows into Taiwan exchange-listed Bond ETFs (USD mn)
| Date | Flows into Taiwan exchange-listed Bond ETFs (USD mn) |
| :--- | :--- |
| 15-May | 118 |
| 20-May | -147 |
| 25-May | 31 |
| 28-May | -11 |
| 2-Jun | 0 |
| 5-Jun | 69 |
</details>

Source: Bloomberg, NOM.

Fig. 10: Korea retail flows into US equities and bonds (monthly)  
![](images/2e8fb2dedd7074ff1672a70e5db2924f58b065c852d15f6aee8b9dcd47ac739e.jpg)

<details>
<summary>bar-line hybrid</summary>

| Date | Korea retail net purchase of US bonds (USD bn) | Korea retail net purchases of US equity (USD bn) | Total (equity + bonds) (USD bn) |
|---|---|---|---|
| Dec-23 | -1.5 | -0.8 | -1.8 |
| Jun-24 | 0.8 | 1.2 | 2.9 |
| Dec-24 | 0.5 | 1.8 | 4.7 |
| Jun-25 | 1.5 | -1.2 | 0.0 |
| Dec-25 | 0.0 | 6.8 | 6.8 |
| Jun-26 | -0.9 | -0.6 | -0.6 |
</details>

Note: June's data are up to 6 June.  
Source: KSD, NOM.

Fig. 11: Korea retail flows into US equities and bonds (daily)  
![](images/cb8fc70f2bf0cae6d510d3bc6fa26d73ad48460db4b3e9933df723cc5c1a8ed6.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date | Net (Bond) (USD mn) | Net (Equity) (USD mn) | Net daily flow into US (Equity & Bond) (USD mn) |
| :--- | :--- | :--- | :--- |
| 18-May | 274 | 300 | -588 |
| 21-May | 360 | -600 | -708 |
| 26-May | -9 | -200 | -181 |
| 29-May | -209 | 501 | -712 |
| 3-Jun | 579 | -456 | -534 |
| 8-Jun | -100 | 313 | 237 |
</details>

Source: KSD, NOM.

1. Our proxy for tracking foreign flows into US-focused equity funds is based on the assumption that US-focused funds listed/domiciled in non-US based markets are primarily invested in by non-US based retail and institutional investors.  
2. Our proxy for tracking foreign flows into US bond funds is based on the assumption that US-focused funds listed on non-US based markets are primarily invested in by non-US based retail and institutional investors.  
3. Our proxy for tracking foreign flows into EM-focused funds is based on the assumption that EM-focused funds listed in non-EM markets are primarily invested in by foreign investors.

## Appendix A-1

This report has been produced by NOM Singapore Ltd. (NSL), Singapore.

See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Craig Chan, Wee Choon Teo, Vicky Chen and Manthan Shingala, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) an

[中间内容因长度限制已省略]

efined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved.
"""
