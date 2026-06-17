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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`NOM`。标题格式建议：`# NOM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China consumer

EQUITY: CONSUMER RELATED

## Retail sales momentum weakened further in May

China's total social retail reading recorded first y-y decline since COVID; no turnaround signal of the sector yet

## Total retail sales continued its weakening trend in May

China's total social retail sales recorded a $0.6\%$ y-y decline in May to CNY4.1tn, the first y-y decline of this consumption measure since the end of 2022 when the Chinese economy was just about to emerge from the COVID-19 lockdown, according to data from the National Bureau of Statistics (16 Jun); the $0.6\%$ y-y decline also missed the Wind consensus of a mild $0.1\%$ y-y increase. Total retail sales of merchandise by enterprises above designated size was the major drag to the total social retail sales reading in May, decreasing by $5.2\%$ y-y. Although the deteriorated merchandise sales can be partially attributed to high-base effect and unfavourable weather conditions (higher temperature and more raining days in May 2026 that limited consumers' activities), we believe the disappointing consumption dataset in May also indicates a broadening softness of the consumption sector. Given: 1) an absence of meaningful consumption-related policy stimulation on the demand side; 2) limited wealth impact of property market recovery in select tier 1&2 cities;, and 3) limited support to consumption by the AI-driven stock market, we believe consumption sentiment will remain sluggish in the near term.

Looking into major consumption categories:

- Catering services sales experienced growth of only 0.6% y-y in May, slowing down from the 2.2% y-y growth in April; merchandise retail sales, as aforementioned, saw a more significant deterioration with a 0.7% y-y decline in May, worsening from the 0.1% y-y drop in April (Fig. 1).  
- Most categories within the merchandise sales delivered weakened sales momentum in May (Fig. 2), except beverages (sales up by 6.1% y-y in May, faster than the 3.6% y-y increase in April), garments/footwear (sales up by 3.8% y-y in May, largely unchanged from the 3.6% y-y growth in April), and office equipments (sales down by 1.5% y-y in May, narrowing from the 6.9% y-y decline in April).  
- Sales of categories including home appliances (May sales down by 15.6% y-y, vs. -15.1% y-y in April) and building/decorating materials (May sales down by 13.6% y-y, vs. -13.8% y-y in April) remained deeply in negative territory with no turnaround signals yet.

## Preferred names in consumer sector

In light of the further weakened retail momentum and the lack of policy-driven demand, we maintain our preference for companies that demonstrate clear development strategies, visible margin trends, and attractive valuations (especially after the recent sector-wise share price weakness). We continue to prefer ANTA (2020 HK, Buy) in the sportswear sector. We also like Laopu Gold (6181 HK, Buy) in the retail space, as we believe Laopu is able to maintain a relatively stable margin trend and improving operating leverage, especially if spot gold price can stabilize in a more accommodative geopolitical environment.

## Research Analysts

China Consumer Related

Jizhou Dong, CFA - NIHK

jizhou.dong@NOM.com

+852 2252 1554

Summer Qian - NIHK

summer.qian@NOM.com

+852 2252 6220

Fig. 1: China – total social retail sales trend  
![](images/99f4693a33142623223331792ae2d3d395b56360c403ff0caf07d1012455feee.jpg)

<details>
<summary>bar chart</summary>

| Month | China's total retail sales (y-y%) (%) | China's total retail sales - catering services (y-y%) (%) | China's total retail sales - merchandise retail (y-y%) (%) |
|---|---|---|---|
| Jun-25 | 4.8 | 1.0 | 5.3 |
| Jul-25 | 3.7 | 1.1 | 4.0 |
| Aug-25 | 3.4 | 2.1 | 3.6 |
| Sep-25 | 3.0 | 1.0 | 3.3 |
| Oct-25 | 2.9 | 3.8 | 2.8 |
| Nov-25 | 1.3 | 3.2 | 1.0 |
| Dec-25 | 0.9 | 2.2 | 0.7 |
| 2M26 | 2.8 | 4.8 | 2.5 |
| Mar-26 | 1.7 | 2.9 | 1.5 |
| Apr-26 | 0.2 | 2.2 | -0.1 |
| May-26 | -0.6 | 0.6 | -0.8 |
</details>

Source: NBS, NOM

Fig. 2: China – total social retail sales by category  
![](images/b95024cbe3adc7897121820bf4333eb613a0d34a63e03f2fd5a2c82ba9b2dbea.jpg)

<details>
<summary>bar chart</summary>

| Category | Date | Value (y-y%) |
| :--- | :--- | :--- |
| Auto (y-y%) | Jun-25 | 4.0 |
| Beverages (y-y%) | Jun-25 | -3.0 |
| Home appliances (y-y%) | Jun-25 | 32.0 |
| Medicines (y-y%) | Jul-25 | 28.0 |
| Cosmetics (y-y%) | Jul-25 | -1.0 |
| Sports/recreation (y-y%) | Aug-25 | 14.0 |
| Petroleum (y-y%) | Sep-25 | -6.0 |
| Tobacco/liquor (y-y%) | Sep-25 | -3.0 |
| Communication equip (y-y%) | Oct-25 | 23.0 |
| Building/decorating materials (y-y%) | Nov-25 | -17.0 |
| Gold/silver/jewelry (y-y%) | Oct-25 | 38.0 |
| Grain/oil/food (y-y%) | Dec-25 | 5.0 |
| Garments/footwear (y-y%) | Dec-25 | 11.0 |
| Daily use (y-y%) | Dec-25 | 1.0 |
| Furniture (y-y%) | Mar-26 | 9.0 |
| Office equip (y-y%) | Apr-26 | -18.0 |
| Sports/recreation (y-y%) | May-26 | 4.0 |
</details>

Source: NBS, NOM

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong.

See Disclaimers for NOM Group entity details.

## Analyst Certification

I, Jizhou Dong, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>ANTA Sports Products</td><td>2020 HK</td><td>HKD 75.30</td><td>15-Jun-2026</td><td>Buy</td><td>N/A</td><td>A10</td></tr><tr><td>Laopu Gold</td><td>6181 HK</td><td>HKD 487.40</td><td>15-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

A10 The NOM Group is a registered market maker in the securities / related derivatives of the issuer.

ANTA Sports Products (2020 HK)  
Rating and target price chart (three year history)  
![](images/7885ef8909b31024387e8c13624ea1b697ac251d8fea37a70afa764c98d88f2f.jpg)

<details>
<summary>line chart</summary>

| Date       | Rating   | Target price | Closing price |
| ---------- | -------- | ------------ | ------------- |
| 25-Mar-26  | 125.00   | 75.75        |               |
| 20-Jan-26  | 116.30   | 82.55        |               |
| 27-Oct-25  | 117.00   | 87.80        |               |
| 10-Apr-25  | 121.80   | 81.55        |               |
| 19-Mar-25  | 131.30   | 97.90        |               |
| 08-Jan-25  | 104.10   | 75.25        |               |
| 27-Aug-24  | 115.00   | 71.65        |               |
| 26-Mar-24  | 125.10   | 83.55        |               |
| 06-Dec-23  | 123.10   | 76.00        |               |
| 22-Aug-23  | 120.00   | 77.65        |               |
| 18-Jul-23  | 115.20   | 84.50        |               |
</details>

HKD 75.30 (15-Jun-2026) Buy (Sector rating: N/A)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our target price of HKD125 for ANTA is based on 25x F12M P/E, equivalent to its five-year average forward P/E. The benchmark index of ANTA is the Hang Seng Index.

Risks that may impede the achievement of the target price Downside risks to our Buy rating and target price for ANTA include: 1) intensifying competition from both domestic and global players; 2) slower-than-expected sales growth; and 3) weaker-than-expected macroeconomic dynamics.

## Laopu Gold (6181 HK)

## HKD 487.40 (15-Jun-2026) Buy (Sector rating: N/A)

Rating and target price chart (three year history)

![](images/66cc1a2ccd98973aff3a530228015f8a96fac6379ff98e51f05e195937a9caac.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2025/01/01 | ~480.00       | ~550.00             | Yes                    |
| 2025/07/01 | ~1050.00      | ~1150.00            | Yes                    |
| 2026/01/01 | ~650.00       | ~1150.00            | Yes                    |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>24-Mar-26</td><td></td><td>1,114.00</td><td>648.50</td></tr><tr><td>11-Mar-26</td><td></td><td>1,171.00</td><td>654.00</td></tr><tr><td>21-Aug-25</td><td></td><td>1,160.00</td><td>751.00</td></tr><tr><td>27-Jul-25</td><td></td><td>1,148.00</td><td>764.50</td></tr><tr><td>26-Jun-25</td><td></td><td>1,023.00</td><td>868.50</td></tr><tr><td>02-Apr-25</td><td></td><td>999.00</td><td>799.00</td></tr><tr><td>20-Feb-25</td><td></td><td>576.00</td><td>468.40</td></tr><tr><td>14-Feb-25</td><td>Buy</td><td></td><td>493.00</td></tr><tr><td>14-Feb-25</td><td></td><td>525.00</td><td>493.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our target price of HKD1,114 is based on 22.5x FY26F P/E, consistent with Laopu's high sales and earnings growth trajectory. The benchmark index for the company is the Hang Seng Index.
Risks that may impede the achievement of the target price Key downside risks include: 1) any significant weakening of gold price, 2) higher-than-expected fashion risk, 3) weaker-than-expected macro environment.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

57% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 34% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

41% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

2% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 0% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

As at 31 March 2026.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow

analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at:

http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient International (Holding) Co., Ltd, and Shanghai Huangpu Investment Holding (Group) Co., Ltd. In accordance with the laws of the People's Republic of China ("PRC", excluding Hong Kong, Macau and Taiwan, for the purpose of this document), NOI is licensed in the PRC to provide sec

[中间内容因长度限制已省略]

 SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
