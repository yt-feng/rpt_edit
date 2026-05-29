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
# Aluminium: China shutdown fears lift prices Quick Note

# China shutdown fears trigger sharp price reaction

LME aluminium climbed to a four-year high after reports of smelter shutdown concerns in China reignited supply disruption fears (link). The market reaction was sharp despite a recent build in visible inventories (Fig. 1), highlighting that sentiment is being driven by forward supply concerns rather than immediate physical tightness.

# China's dominance makes any supply disruption globally relevant

China remains the largest aluminium producer globally, accounting for $\sim 60\%$ of primary aluminium output (Fig. 2). As a result, even incremental production disruptions or policy-led curtailments can have an outsized impact on global balances, particularly in a market where supply flexibility is already constrained.

# Broader global supply environment was already tightening

The China headline comes against an already tightening global supply environment. Recent operational disruptions across global aluminium markets, including operational constraints at smelting assets in regions such as the Middle East, have incrementally tightened supply expectations. As a result, we believe the current rally is not purely a China-specific reaction (Fig. 5), but an amplification of broader concerns around supply resilience.

# Price action reflects forward risk, not current scarcity

Aluminium inventories have recently moved higher, which would ordinarily weigh on pricing. However, in our view, the market appears to be looking through near-term inventory builds and instead pricing in the risk of fresh supply disruptions, suggesting commodity positioning is being driven by anticipated tightness rather than current scarcity.

# India-based upstream names in our coverage remain key beneficiaries

We believe higher aluminium prices are positive for upstream producers in our coverage through stronger realizations, improved EBITDA/tonne and stronger cash generation (Fig. 3).

We maintain our Buy recommendations on Tata Steel (TATA IN), JSW Steel (JSTL IN), Jindal Steel (JINDALST IN) and Lloyds Metals (LLOYDSME IN).

# Research Analysts

# India Metals & Mining

Jashandeep Singh Chadha - NFASL

jashandeep.singhchadha@NOM.com

+91 22 40374124

Fig. 1: China aluminium inventories have increased \~55% in 1Q vs 4Q raising risk of production curtailment   
![](images/f3c88067aef67713de02a078b39b2de79e2ce8bb8e845f59e80345775e9b4e56.jpg)

<details>
<summary>area</summary>

| Date   | LME Aluminium Inventories (MT) | SHFE Inventories (MT) |
|--------|--------------------------------|------------------------|
| May-16 | 3.0                            | 0.3                    |
| May-17 | 2.5                            | 0.4                    |
| May-18 | 1.5                            | 0.9                    |
| May-19 | 1.2                            | 0.6                    |
| May-20 | 1.8                            | 0.5                    |
| May-21 | 2.0                            | 0.4                    |
| May-22 | 0.8                            | 0.3                    |
| May-23 | 0.6                            | 0.2                    |
| May-24 | 1.2                            | 0.3                    |
| May-25 | 0.5                            | 0.2                    |
| May-26 | 0.7                            | 0.4                    |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 2: China accounts for $>60\%$ of the global primary aluminium production   
![](images/7f5a84ef605d948349b7e98346832430a58e59604164c931a443f7a1bad5068d.jpg)

<details>
<summary>line</summary>

| Date   | China share in Aluminium Production (%) |
|--------|------------------------------------------|
| Apr-15 | 54.0                                     |
| Apr-16 | 50.0                                     |
| Apr-17 | 58.0                                     |
| Apr-18 | 56.0                                     |
| Apr-19 | 57.0                                     |
| Apr-20 | 58.0                                     |
| Apr-21 | 65.0                                     |
| Apr-22 | 66.0                                     |
| Apr-23 | 65.0                                     |
| Apr-24 | 66.0                                     |
| Apr-25 | 60.0                                     |
| Apr-26 | 62.0                                     |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 3: 1Q average aluminium spreads are up \~22% vs 4Q average largely on account of strong aluminium pricing   
![](images/5da959b30241cecb84989247a77ff3f67dbbf1671148c6e512f873bccecd6861.jpg)

<details>
<summary>line</summary>

| Date    | Aluminum spread (USD/t) | LME Aluminum price (USD/t) |
|---------|--------------------------|-----------------------------|
| May-20  | ~0                       | ~-1,000                     |
| Nov-20  | ~0                       | ~-500                       |
| May-21  | ~0                       | ~1,000                      |
| Nov-21  | ~0                       | ~2,500                      |
| May-22  | ~-2,000                  | ~500                        |
| Nov-22  | ~-1,000                  | ~3,000                      |
| May-23  | ~0                       | ~3,500                      |
| Nov-23  | ~0                       | ~4,000                      |
| May-24  | ~0                       | ~5,000                      |
| Nov-24  | ~0                       | ~6,000                      |
| May-25  | ~0                       | ~7,000                      |
| Nov-25  | ~0                       | ~6,500                      |
| May-26  | ~0                       | ~6,800                      |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 4: UBC spread is up $15\%$ in 1Q vs 4Q average as scrap prices have increased $9\%$ in the same period   
![](images/fb67e63646204f666722bb2061aeffcd65e630026b40e4c602843b9aed9dd91f.jpg)

<details>
<summary>bar_line</summary>

| Date   | UBC Scrap Spread (USD/t) | LME Aluminum (USD/t) |
|--------|---------------------------|----------------------|
| May-18 | ~1,000                    | ~2,300               |
| May-19 | ~900                      | ~2,000               |
| May-20 | ~1,000                    | ~1,500               |
| May-21 | ~1,500                    | ~2,500               |
| May-22 | ~2,000                    | ~4,000               |
| May-23 | ~1,500                    | ~2,500               |
| May-24 | ~1,700                    | ~2,700               |
| May-25 | ~2,000                    | ~3,000               |
| May-26 | ~3,500                    | ~3,800               |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 5: Aluminium has been the best-performing commodity, closely followed by India's domestic HRC prices   
![](images/e7d86abedd09505190bfd09cc8bd6419069389eba277efe97e72a8b59fe2f333.jpg)

<details>
<summary>bar</summary>

YTD Return
| Commodity | YTD Return (%) |
| :--- | :--- |
| Aluminium | 25 |
| Indian HRC | 21 |
| Zinc | 15 |
| Nickel | 13 |
| Coking Coal | 10 |
| Copper | 9 |
| Silver | 6 |
| China HRC | 5 |
| Gold | 5 |
</details>

Source: Bloomberg Finance L.P., NOM

# Appendix A-1

This report has been produced by NOM Financial Advisory and Securities (India) Private Limited (NFASL), India.

See Disclaimers for NOM Group entity details.

# Analyst Certification

I, Jashandeep Singh Chadha, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

# Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers 

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>Jindal Steel</td><td>JINDALST IN</td><td>INR 1,223</td><td>26-May-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>JSW Steel</td><td>JSTL IN</td><td>INR 1,294</td><td>26-May-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Lloyds Metals and Energy</td><td>LLOYDSME IN</td><td>INR 1,854</td><td>26-May-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Tata Steel</td><td>TATA IN</td><td>INR 210</td><td>26-May-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

Jindal Steel (JINDALST IN)   
Rating and target price chart (three year history)   
![](images/d5ebc145ca86a0dd77b2b2c3e53082909809a46b9351848bc6395b3fb2d5e4a6.jpg)

<details>
<summary>line</summary>

| Date       | Rating   | Target price | Closing price |
|------------|----------|--------------|---------------|
| 04-May-26  |          | 1,350.00     | 1,261.00      |
| 01-Feb-26  |          | 1,280.00     | 1,131.00      |
| 22-Sep-25  |          | 1,150.00     | 1,033.00      |
| 31-Jan-25  |          | 1,080.00     | 792.00        |
| 07-Nov-24  |          | 1,180.00     | 947.00        |
| 02-Oct-24  | Buy      |              | 1,036.00      |
| 02-Oct-24  |          | 1,200.00     | 1,036.00      |
</details>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We arrive at TP of Rs1,350 by applying slightly higher than mid-cycle one-year-forward EV/EBITDA of 8.0x on new steady-state EBITDA in June-28F. The benchmark for this stock is NIFTY50

Risks that may impede the achievement of the target price 1. Lower spreads - If Chinese HRC margins fail to recover or if the net exports from China increase, it would result in continued pressure on export HRC prices. In such a case, domestic HRC prices will remain under pressure due to lower import parity prices leading to lower spreads/margins. 2. Delays in expansion & cost overruns - This would result in lower than expected volume from FY26F onwards. Delay in commissioning might also result in capex cost overrun resulting in lower than earlier expected ROCE 3. Domestic demand disruptions - If the domestic demand grows lower than expected or lower than the capacity addition, it would result in lower domestic HRC margins and higher dependence on exports. In such a case, the margins will be lower than expected

INR 1,223 (26-May-2026) Buy (Sector rating: N/A)

# JSW Steel (JSTL IN)

# INR 1,294 (26-May-2026) Buy (Sector rating: N/A)

Rating and target price chart (three year history)

![](images/3242b66ca9deacd911e4b6667ea60ec4b636cccc7a4e6391080e29d2077532a7.jpg)

<details>
<summary>line</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2024/07/01 | ~950.00       | -                   | Yes                    |
| 2025/01/01 | ~1050.00      | -                   | Yes                    |
| 2026/01/01 | ~1350.00      | -                   | Yes                    |
| 2026-May-26 | ~1400.00      | -                   | Yes                    |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>21-May-26</td><td></td><td>1,400.00</td><td>1,281.00</td></tr><tr><td>26-Jan-26</td><td></td><td>1,340.00</td><td>1,170.00</td></tr><tr><td>22-Sep-25</td><td></td><td>1,300.00</td><td>1,117.00</td></tr><tr><td>02-Oct-24</td><td>Buy</td><td></td><td>1,027.00</td></tr><tr><td>02-Oct-24</td><td></td><td>1,220.00</td><td>1,027.00</td></tr><tr><td>20-Sep-24</td><td>Not Rated</td><td></td><td>982.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We arrive at TP of INR1,400 by applying slightly higher than mid-cycle one-year forward EV/EBITDA of 8.1x on new steady-state EBITDA in Jun'28. The benchmark for this stock is NIFTY50

Risks that may impede the achievement of the target price 1. Lower spreads - If Chinese HRC margins fail to recover or if the net exports from China increase, it would result in continued pressure on export HRC prices. In such a case, domestic HRC prices will remain under pressure due to lower import parity prices leading to lower spreads/margins. 2. Delays in Dolvi commissioning - This would result in lower than expected volume from FY28F onwards. Delay in commissioning might also result in capex cost overrun resulting in lower than earlier expected ROCE 3. Domestic demand disruptions - If the domestic demand grows lower than expected or lower than the capacity addition, it would result in lower domestic HRC margins and higher dependence on exports. In such a case, the margins will be lower than expected

# Lloyds Metals and Energy (LLOYDSME IN)

Rating and target price chart (three year history)

![](images/d7fe93b6de3acf00ce9d83ddfd85068eec5032032d208a3898a7209a8be77058.jpg)

<details>
<summary>line</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2026-01-01 | ~1150         | ~1600               | ~1150                  |
</details>

# INR 1,854 (26-May-2026) Buy (Sector rating: N/A)

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>26-May-26</td><td></td><td>2,050.00</td><td>1,854.00</td></tr><tr><td>24-Feb-26</td><td>Buy</td><td></td><td>1,164.00</td></tr><tr><td>24-Feb-26</td><td></td><td>1,600.00</td><td>1,164.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We arrive at SOTP-based TP of INR2,050 by applying a target EV/EBITDA of 8.4x on new steady-state EBITDA in Jun'28. The benchmark for this stock is NIFTY50
Risks that may impede the achievement of the target price Risks: (1) a delay in steel capacity;, (2) political unrest in the Democratic Republic of the Congo affecting the copper business;, (3) BHQ beneficiation not yielding the same results as seen in the pilot project;, and (4) resurfacing of Naxal activities.

# Tata Steel (TATA IN)

# INR 210 (26-May-2026) Buy (Sector rating: N/A)

Rating and target price chart (three year history)

![](images/112de267ecb711105998d965b5cb523422eb986932c123331734125011c30d77.jpg)

<details>
<summary>line</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2026/01/01 | ~175.00       | ~225.00             | Yes                    |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>21-May-26</td><td></td><td>240.00</td><td>209.00</td></tr><tr><td>09-Feb-26</td><td></td><td>220.00</td><td>202.00</td></tr><tr><td>20-Oct-25</td><td>Buy</td><td></td><td>172.00</td></tr><tr><td>20-Oct-25</td><td></td><td>215.00</td><td>172.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We arrive at TP of INR240 by applying slightly higher than mid-cycle one-year forward EV/EBITDA multiple of 7.7x on new steady-state EBITDA in June'28. The benchmark for this stock is NIFTY50
Risks that may impede the achievement of the target price Delays in subsidiary's expansion, weaker-than-expected demand growth, lower spreads, increased regulatory scrutiny on European operations and sustained elevation in iron ore prices beyond FY30F.

# Important Disclosures

# Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

# Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

57% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 34% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

41% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

2% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 0% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

As at 31 March 2026.

\*The NOM Group as defined in the Disclaimer section

[中间内容因长度限制已省略]

STMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

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
