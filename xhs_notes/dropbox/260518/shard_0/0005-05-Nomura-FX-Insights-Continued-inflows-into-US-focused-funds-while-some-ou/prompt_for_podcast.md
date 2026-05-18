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
# Continued inflows into US-focused funds while some outflows from EM-focused funds

- Net foreign flows into US-focused funds remained elevated at USD2.1bn between 8 and 14 May, predominantly into equity funds.   
- Specifically, inflows into US-focused equity funds accelerated to USD2.4bn, while there were small outflows of USD292mn from bond funds.   
- Outflows from EM-focused ETFs were marginal at USD97mn between 9 and 15 May, from inflows of USD1.2bn in the previous week.   
- Within EM-focused funds, outflows from bond funds of USD217mn offset inflows of USD120mn into equity funds.   
- Korea's retail investor flows into US portfolio assets remained lacklustre, with net selling of USD72mn of US portfolio assets between 9 and 15 May.   
- Taiwan's investors were also net buyers of USD-denominated bond funds at USD103mn between 8 and 14 May which compares with net buying of USD220mn in the previous week.

# Research Analysts

# Asia FX Strategy

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

<table><tr><td></td><td colspan="3">Foreign investments in US- focused funds (ETF and MF)</td><td colspan="3">EM-focused ETFs</td><td colspan="3">Korea retail investments</td><td>Taiwan investments in local ETFs</td></tr><tr><td>USD mn</td><td>US Equities</td><td>US Bonds</td><td>Total</td><td>Equity funds</td><td>Bond funds</td><td>Total</td><td>US Equities</td><td>US Bonds</td><td>Total</td><td>USD-denominated Bonds</td></tr><tr><td>Latest week (5 sessions)</td><td>2,369</td><td>-292</td><td>2,077</td><td>120</td><td>-217</td><td>-97</td><td>-221</td><td>149</td><td>-72</td><td>103</td></tr><tr><td>Previous week (previous 5 sessions)</td><td>2,172</td><td>395</td><td>2,567</td><td>1,253</td><td>-79</td><td>1,174</td><td>2</td><td>57</td><td>58</td><td>220</td></tr><tr><td>Monthly flow in May</td><td>4,609</td><td>217</td><td>4,826</td><td>1,421</td><td>-265</td><td>1,156</td><td>-216</td><td>202</td><td>-14</td><td>323</td></tr><tr><td>Monthly flow in April</td><td>3,051</td><td>100</td><td>3,151</td><td>5,832</td><td>453</td><td>6,285</td><td>-469</td><td>-441</td><td>-910</td><td>-342</td></tr><tr><td>Monthly flow in March</td><td>-259</td><td>-1,412</td><td>-1,671</td><td>-237</td><td>-2,645</td><td>-2,882</td><td>1,691</td><td>-166</td><td>1,525</td><td>-29</td></tr><tr><td>Monthly flow in February</td><td>4,559</td><td>74</td><td>4,634</td><td>18,920</td><td>184</td><td>19,104</td><td>3,949</td><td>257</td><td>4,206</td><td>-662</td></tr><tr><td>Monthly flow in January</td><td>9,524</td><td>2,616</td><td>12,140</td><td>25,150</td><td>401</td><td>25,551</td><td>5,003</td><td>396</td><td>5,399</td><td>1,065</td></tr></table>

Note: Note: The latest weekly data are up to 14 May for US equity and bond-focused ETFs and mutual funds, 15 May for EM-focused ETFs, 15 May for Korea retail investors and 14 May for Taiwan investors. Data for the previous week are the preceding 5 sessions of the latest week.
Source: Bloomberg, KSD, NOM

# Weekly update of high-frequency investor flows

- Foreign inflows into US-focused equity ETFs and mutual funds $^{[1]}$ totaled USD2.4bn between 8 and 14 May (Figure 3), continuing from inflows of USD2.2bn in the previous week. MTD May, inflows into these funds totaled USD4.6bn surpassing total inflows of USD3.1bn in April (Figure 2).   
- Foreign outflows from US-focused bond ETFs and mutual funds $^{[2]}$ were limited at USD292mn between 8 and 14 May, partly offsetting inflows of USD395mn in the previous week (Figure 5). MTD May, inflows into these funds totaled USD217mn after inflows of USD100mn in April 2026 (Figure 4).   
- Foreign outflows from EM-focused ETFs[3] were limited at USD97mn between 9 and 15 May, albeit a reversal from inflows of USD1.2bn in the previous week. MTD May, foreign investors net bought USD1.4bn of equity funds and sold USD265mn of bond funds (Figures 6 and 7). Inflows into these funds in MTD May amounted to USD1.2bn, after inflows of USD6.3bn in April.   
- Inflows into Taiwan's exchange-listed USD bond ETFs amounted to USD103mn (8 to 14 May), from inflows of USD220mn in the previous week (Figure 9). After selling USD342mn of USD-denominated bonds in April, Taiwanese investors net bought USD323mn in MTD May (Figure 8).

\- Korean retail investors net sold USD72mn of US portfolio assets from 9 to 15 May. This consisted of net buying of USD149mn of US bonds and net selling of USD221mn of US equities (Figures 10 and 11). In MTD May, Korea's retail investors net sold USD14mn of US portfolio assets, after net selling USD910mn of US portfolio assets in April 2026.

Fig. 2: Foreign flows into US-focused equity ETFs and mutual funds (monthly)   
![](images/34157a10eac73fc41aa9e0960c5422cba9cf41ed2527dcc90b682c3eaf71291c.jpg)

<details>
<summary>bar</summary>

| Month    | Foreign flows into US-focused equity funds (USD bn) |
| -------- | -------------------------------------------------- |
| Nov-23   | 7.0                                                |
| Dec-23   | 10.0                                               |
| Jan-24   | 6.0                                                |
| Feb-24   | 5.0                                                |
| Mar-24   | 4.0                                                |
| Apr-24   | 12.0                                               |
| May-24   | 12.0                                               |
| Jun-24   | 8.0                                                |
| Jul-24   | 9.0                                                |
| Aug-24   | 8.0                                                |
| Sep-24   | 20.0                                               |
| Oct-24   | 16.0                                               |
| Nov-24   | 16.0                                               |
| Dec-24   | 3.0                                                |
| Jan-25   | 0.0                                                |
| Feb-25   | 0.0                                                |
| Mar-25   | 0.0                                                |
| Apr-25   | 0.0                                                |
| May-25   | -5.0                                               |
| Jun-25   | 0.0                                                |
| Jul-25   | 0.0                                                |
| Aug-25   | 4.0                                                |
| Sep-25   | 6.0                                                |
| Oct-25   | 5.0                                                |
| Nov-25   | -1.0                                               |
| Dec-25   | 3.0                                                |
| Jan-26   | 9.5                                                |
| Feb-26   | 4.6                                                |
| Mar-26   | 4.6                                                |
| Apr-26   | -0.3                                               |
| May-26   | 3.1                                                |
| Jun-26   | 4.6                                                |
</details>

Note: May's data are up to 14 May.  
Source: Bloomberg, NOM.

Fig. 3: Foreign flows into US-focused equity ETFs and mutual funds (daily)   
![](images/91a95336e8a81ff938446808d7ef582ae7a2424f2fb32cbbdac0338269519d7a.jpg)

<details>
<summary>bar</summary>

| Date | Foreign flows into US-focused equity funds (ETFs + mutual funds) (USD mn) |
| :--- | :--- |
| 28-Apr | 243 |
| 28-Apr | -354 |
| 1-May | 840 |
| 1-May | 438 |
| 1-May | 558 |
| 1-May | 140 |
| 1-May | 98 |
| 6-May | 483 |
| 6-May | 893 |
| 11-May | 1401 |
| 11-May | 708 |
| 11-May | 69 |
| 14-May | -134 |
| 14-May | 225 |
</details>

Source: Bloomberg, NOM.

Fig. 4: Foreign flows into US-focused bond ETFs and mutual funds (monthly)   
![](images/1f281a0fcd224dbd353eb9b8f6e320ca8f310a4b65a4b8d9561ced14d890f1ab.jpg)

<details>
<summary>bar</summary>

| Date    | Foreign flows into US-focused bond funds (ETFs and mutual funds; monthly) |
|---------|----------------------------------------------------------------------------------|
| Nov-23 | 2.5                                                                              |
| May-24  | 4.0                                                                              |
| Nov-24  | 8.0                                                                              |
| May-25  | -4.0                                                                             |
| Nov-25  | 2.6                                                                              |
| May-26  | 0.2                                                                              |
</details>

Note: May's data are up to 14 May.  
Source: Bloomberg, NOM.

Fig. 5: Foreign flows into US-focused bond ETFs and mutual funds (daily)   
![](images/d7a528117c6664f3ce50117271321dd00cdbec1674668687fd55105dd57a3785.jpg)

<details>
<summary>bar</summary>

| Date | Foreign flows into US-focused bond funds (ETFs + mutual funds) (USD mn) |
| :--- | :--- |
| 23-Apr | -60 |
| 28-Apr | 78 |
| 1-May | -26 |
| 6-May | 40 |
| 11-May | -106 |
| 14-May | 203 |
| 6-May | -57 |
| 11-May | 28 |
| 14-May | -123 |
| 11-May | -235 |
| 14-May | -5 |
| 14-May | 34 |
| 14-May | 150 |
</details>

Source: Bloomberg, NOM.

Fig. 6: Foreign flows into EM-focused ETFs (Monthly)   
![](images/5641953efe0d26fd411ea586aceb0af28e4dacf5a2e96eda2220d5de012ee9cd.jpg)

<details>
<summary>line</summary>

| Date    | foreign flow to EM-focused equity ETFs (USD bn) | foreign flow to EM-focused bond ETFs (USD bn) | total foreign flows to EM-focused ETFs (USD bn) |
|---------|--------------------------------------------------|-----------------------------------------------|------------------------------------------------|
| Nov-23  | 0                                                | 0                                             | 0                                              |
| May-24  | 0                                                | 0                                             | 0                                              |
| Nov-24  | 0                                                | 0                                             | 0                                              |
| May-25  | 0                                                | 0                                             | 0                                              |
| Nov-25  | 0                                                | 0                                             | 0                                              |
| May-26  | 0                                                | 0                                             | 0                                              |
</details>

Note: May's data are up to 15 May.  
Source: Bloomberg, NOM

Fig. 7: Foreign flows into EM-focused ETFs (Daily)   
![](images/59debc9859b196dcf6b8d86fb63a024de361cc234d8730bd214c494afaf72024.jpg)

<details>
<summary>bar_line</summary>

| Date | Flows to bonds (USD mn) | Flows to equities (USD mn) | Total flows (USD mn) |
| :--- | :--- | :--- | :--- |
| 29-Apr | 14 | 124 | 180 |
| | -73 | | -100 |
| 4-May | 46 | 83 | 50 |
| | | 146 | 150 |
| 7-May | 292 | 607 | 607 |
| | -42 | -8 | -20 |
| 12-May | -101 | 48 | -100 |
| 15-May | 6 | 100 | 60 |
</details>

Source: Bloomberg, NOM

Fig. 8: Taiwan flows into ETFs invested in USD bonds (monthly)   
![](images/1563d3b184e2acecfc92a7a74246cb512a57e536a61908d375915fd40f3a6c2e.jpg)

<details>
<summary>bar</summary>

Flows into Taiwan exchange listed Bond-ETFs
| Date | Flows (USD bn) |
|---|---|
| Nov-23 | 1.2 |
| Dec-23 | 3.4 |
| Jan-24 | 3.9 |
| Feb-24 | 3.2 |
| Mar-24 | 3.7 |
| Apr-24 | 2.5 |
| May-24 | 3.5 |
| Jun-24 | -0.7 |
| Jul-24 | 3.7 |
| Aug-24 | 1.9 |
| Sep-24 | 5.8 |
| Oct-24 | 2.0 |
| Nov-24 | 1.7 |
| Dec-24 | 0.5 |
| Jan-25 | 0.9 |
| Feb-25 | -1.3 |
| Mar-25 | -1.4 |
| Apr-25 | -1.5 |
| May-25 | 0.3 |
| Jun-25 | 2.8 |
| Jul-25 | -0.1 |
| Aug-25 | 0.6 |
| Sep-25 | -0.4 |
| Oct-25 | 0.4 |
| Nov-25 | 0.9 |
| Dec-25 | 1.1 |
| Jan-26 | -0.7 |
| Feb-26 | -0.3 |
| Mar-26 | 0.3 |
</details>

Note: May's data are up to 14 May.
Source: Bloomberg, NOM.

Fig. 9: Taiwan flows into ETFs invested in USD bonds (daily)   
![](images/ccdd34cf7b3ecca5722e78749fe48341a47fddbc9dc3206681cac7984bda9c89.jpg)

<details>
<summary>bar</summary>

Flows into Taiwan exchange-listed Bond ETFs (USD mn)
| Date | Flow (USD mn) |
| :--- | :--- |
| 23-Apr | 15 |
| | 41 |
| 28-Apr | -31 |
| | -25 |
| 1-May | 24 |
| | 16 |
| | 0 |
| 6-May | 19 |
| | -86 |
| 11-May | 288 |
| | 288 |
| 14-May | -1 |
| | -129 |
| | -31 |
| | -146 |
| | 121 |
</details>

Source: Bloomberg, NOM.

Fig. 10: Korea retail flows into US equities and bonds (monthly)   
![](images/7dbdbbf8e0c5393ef2c41583b381ef3e7d98a7ab37df72f9baa2e0fc90077a36.jpg)

<details>
<summary>bar_line</summary>

| Date | Korea retail net purchase of US bonds (USD bn) | Korea retail net purchases of US equity (USD bn) | Total (equity + bonds) (USD bn) |
|---|---|---|---|
| Nov-23 | 0.5 | -1.8 | -1.9 |
| May-24 | 1.0 | 1.5 | 2.8 |
| Nov-24 | 0.5 | -0.5 | 1.7 |
| May-25 | 1.5 | -1.5 | 4.8 |
| Nov-25 | 0.0 | 6.8 | 6.8 |
| May-26 | 0.0 | 1.5 | 4.2 |
| Jun-26 | 0.0 | 0.0 | -0.9 |
</details>

Note: May's data are up to 15 May.  
Source: KSD, NOM.

Fig. 11: Korea retail flows into US equities and bonds (daily)   
![](images/6a5e392ad031ce7b5a17519718efd8306341442afcec90b45a35effb2c94a4e5.jpg)

<details>
<summary>line</summary>

| Date     | Net (Bond) | Net (Equity) | Net daily flow into US (Equity & Bond) |
| -------- | ---------- | ------------ | -------------------------------------- |
| 24-Apr   | -218       | -            | -                                      |
| 29-Apr   | -          | 506          | 187                                    |
| 4-May    | 0          | -            | -92                                    |
| 7-May    | 31         | 651          | -530                                   |
| 12-May   | -2         | 422          | -543                                   |
| 15-May   | 0          | 97           | -49                                    |
</details>

Source: KSD, NOM.

1. Our proxy for tracking foreign flows into US-focused equity funds is based on the assumption that US-focused funds listed/domiciled in non-US based markets are primarily invested in by non-US based retail and institutional investors.   
2. Our proxy for tracking foreign flows into US bond funds is based on the assumption that US-focused funds listed on non-US based markets are primarily invested in by non-US based retail and institutional investors.   
3. Our proxy for tracking foreign flows into EM-focused funds is based on the assumption that EM-focused funds listed in non-EM markets are primarily invested in by foreign investors.

# Appendix A-1

This report has been produced by NOM Singapore Ltd. (NSL), Singapore.

See Disclaimers for NOM Group entity details.

# Analyst Certification

We, Craig Chan, Wee Choon Teo, Vicky Chen and Manthan Shingala, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

# Important Disclosures

# Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

# ADDITIONAL DISCLOSURES REQUIRED IN THE U.S.

Principal Trading: NOM Securities International, Inc and its affiliates will usually trade as principal in the fixed income securities (or in related derivatives) that are the subject of this research report. Analyst Interactions with other NOM Securities International, Inc. Personnel: The fixed income research analysts of NOM Securities International, Inc and its affiliates regularly interact with sales and trading desk personnel in connection with obtaining liquidity and pricing information for their respective coverage universe.

# Valuation methodology - Fixed Income

NOM's Fixed Income Strategists express views on the price of securities and financial markets by providing trade recommendations. These can be relative value recommendations, directional trade recommendations, asset allocation recommendations, or a mixture of all three.

The analysis which is embedded in a trade recommendation would include, but not be limited to:

- Fundamental analysis regarding whether a security's price deviates from its underlying macro- or micro-economic fundamentals.   
• Quantitative analysis of price variations.   
- Technical factors such as regulatory changes, changes to risk appetite in the market, unexpected rating actions, primary market activity and supply/ demand considerations.

The timeframe for a trade recommendation is variable. Tactical ideas have a short timeframe, typically less than three months. Stra

[中间内容因长度限制已省略]

ER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved.
"""
