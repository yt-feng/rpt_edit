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
# South Korea Aerospace & Defense: Potential inflection point in beaten down sentiment

Hanwha Aerospace (Hanwha) and Hyundai Rotem (Rotem) closed higher at $+6.3\% / +10.7\%$ on Friday outperforming Kospi $(+4.5\%)$ by $+1.8\mathrm{ppt} / +6.2\mathrm{pt}$ , respectively. We note that share prices continued to slide down over the past few months, which came after a re-rating in valuation during Mar-Apr period on expectations surrounding the Middle East's swift restocking of air defense systems (refer to our past report on Middle East air missile defense system opportunities). We attribute such lackluster market sentiment to the prolonged tensions in the region, which put discussions on the potential order pipelines on hold and left limited sector catalysts post 1Q results (Exhibit 1 & Exhibit 2).

In that sense, Friday's share price strength was likely driven by media reports of a potential US-Iran peace agreement, which we believe would be a critical catalyst needed for both Hanwha And Rotem in advancing talks on the pending potential orders that we continue to highlight (Exhibit 3 & Exhibit 4). As such, our view is that any further development towards peace would lead up to the market incrementally pricing back in the order pipelines. As a recap, at a $100\%$ win-rate, we see W95.5tn, W89.5tn potential orders for Hanwha and Rotem, which would translate to GSe EPS CAGR of $32\% / 48\%$ during 2025-2028 under our probability-weighted model. We reiterate Hanwha (TP W1.8mn) and Rotem (W280k) as BUYs.

## Do Hyoung Kim

+82(2)3788-1376

dohyoung.kim@gs.com

GS (Asia) L.L.C., Seoul Branch

## Joshua Kim

+82(2)3788-1791 | joshua.kim@gs.com

GS (Asia) L.L.C., Seoul

Branch

Exhibit 1: Hanwha Aerospace share price has been falling since April highs - key events  
![](images/7d28ed1cb50fe5858ef0d9be3237c84a3c167705b223e8f674b4f242f5e5d0f1.jpg)

<details>
<summary>line chart</summary>

| Date       | Event Description                                      | Value     |
|------------|-----------------------------------------------------|-----------|
| Nov 3      | 3Q earnings (↓)                                       | ~1,050,000|
| Nov 5      | US-Greenland headlines (↑)                             | ~950,000  |
| Nov 21     | US President proposes 28-point R-U peace plan (↓)           | ~850,000  |
| Dec 2      | Potential W7,700bn Spain SpH program reported (↑)        | ~1,050,000|
| Dec 16     | Estonia Chunmoo deal signed (W440bn) (−)               | ~850,000  |
| Dec 29     | Poland Chunmoo missile deal signed (W5,600bn) (↑)         | ~950,000  |
| Feb 2      | Norway Chunmoo deal signed (W1.3tn) (↑)                | ~1,350,000|
| Feb 8      | WDS2026 Kick-off (↓)                                 | ~1,250,000|
| Feb 9      | 4Q earnings (↓)                                      | ~1,250,000|
| Feb 18     | France MLRS potential reported (↑)                            | ~1,150,000|
| Feb 19     | Possible US strikes in Iran reported (↑)                   | ~1,450,000|
| Mar 25     | Signs joint development of tracked-K9E (Spain) with Indra group (-)   | ~1,450,000|
| Apr 30     | 1Q earnings (−)                                     | ~1,450,000|
| Jun 1      | Explosion at Daejeon plant (↓)                              | ~1,450,000|
| Jun 26     | $35bn UAE defense MOU announced (↑)                           | ~1,450,000|
| Jun 11     | Possible US-Iran peace deal reported (↑)                          | ~1,450,000|
</details>

Source: Quantiwise, Various media reports, Compiled by GS Global Investment Research

Exhibit 2: Hyundai Rotem share price has been falling since April highs - key events  
![](images/594e7e424eb0d2bc65fc75be647f9de45a306d6da8b246ea486028865e25a9aa.jpg)

<details>
<summary>line chart</summary>

| Date       | Event Description                                      | Earnings (bn) |
|------------|-----------------------------------------------------|---------------|
| Nov 3      | 3Q earnings (↓)                                       | -             |
| Nov 21     | US President proposes 28-point R-U peace plan (↓)           | -             |
| Jan 13     | US President tells protestors in Iran that help is on its way (↑)   | -             |
| Feb 19     | Possible US strikes in Iran reported (↑)              | -             |
| Feb 26     | $35bn UAE defense MOU announced (↑)               | -             |
| Feb 28     | US strikes Iran (↑)                                   | -             |
| Feb 8      | WDS2026 Kick-off (-)                                | -             |
| Jan 30     | 4Q earnings (↓)                                     | -             |
| Mar 26     | K2ME-variant unveiled (-), 189,800                  | -             |
| Apr 24     | 1Q earnings (↑)                                    | -             |
| Jun 11     | Possible US-Iran peace deal reported (↑)            | -             |
| Dec 10     | Peru K2/K808 framework deal signed (e.W2.5-3.0tn) (-)    | -             |
| Jan 3      | US seizure of Venezuelan President (↑)                | -             |
| Jan 26     | Romania presents SAFE fund allocation plans (MBTs not included) (↑) | -             |
| Jun 11     | Possible US-Iran peace deal reported (↑)              | -             |
</details>

Source: Quantiwise, Various media reports, Compiled by GS Global Investment Research

Exhibit 3: At $100\% / 50\%$ win-rate, the key potential order pipeline would push up Hanwha's export backlog to W95tn/62tn which exceeds GSe $26 - 30\%$ overseas revenue  
![](images/f3813e1861f25f40c49552c90b9c6539a6853d4929e607314c8795d4c212a0e6.jpg)

<details>
<summary>bar chart</summary>

GSe Hanwha Aerospace order potentials
| Category | Value |
|---|---|
| Current export backlog | 29,378 |
| K9 (2nd hand) Finland | 941 |
| K9 US | 11,000 |
| IFV / K9 / Chummoo etc. Saudi Arabia | 20,000 |
| K9 UAE | 1,560 |
| K9 Canada | 1,780 |
| Middle East M-SAM/L- SAM | 15,000 |
| K9 Poland | 6,160 |
| K239 Chummoo France | 1,971 |
| K9 Spain | 7,700 |
| Case 1: 100% win | 95,490 |
| Case 2: 50% win | 62,434 |
| GSe '26-'30 overseas revenue | 47,613 |
</details>

Source: Company data, Various media reports, GS Global Investment Research

Exhibit 4: At a $100\% / 50\%$ win-rate, the key potential order pipeline would push up Rotem's export backlog to W90tn/49tn, which exceeds GSe 2026-2030E overseas revenue  
![](images/c37459c8edfc8878db9c95701fe183f3da040fe65e5841d466ebf55b12e15557.jpg)

<details>
<summary>bar chart</summary>

Hyundai Rotem order potentials
| Category | Value |
|---|---|
| Current export backlog | 8,981 |
| K2 Peru EC1 | 1,350 |
| K808 IFV Peru EC1 | 1,150 |
| K2 local production Peru | 2,600 |
| K808 Peru | 1,448 |
| K2 Iraq | 9,000 |
| K2 Saudi Arabia | 18,360 |
| K2 UAE | 11,160 |
| K2 Poland | 24,000 |
| K2 Romania | 6,480 |
| K2 Morocco | 5,000 |
| Case 1: 100% win | 89,529 |
| Case 2: 50% win | 49,255 |
| GSe '26-'30 overseas revenue | 34,828 |
</details>

Source: Company data, Various media reports, GS Global Investment Research

## Price Target Risks and Methodology - Hanwha Aerospace

Our 12-month target price of W1,800,000 is based on a target P/E multiple of 28.0x applied to 2027E EPS. Key risks include: 1) lower-than-expected order wins, 2) lower-than-expected OPM from overseas production, 3) lower-than-expected demand from NATO's Eastern Flank and MENA countries, 4) regional geopolitical developments resulting in shift in focus to domestic procurement, and 5) stronger KRW against the USD.

## Price Target Risks and Methodology - Hyundai Rotem

Our 12-month target price of W280,000 is based on a target P/E multiple of 20.8x applied to 2027E EPS. Key risks include: 1) lower-than-expected order wins, 2) lower-than-expected OPM from overseas production, 3) lower-than-expected demand from NATO's Eastern Flank and MENA countries, 4) regional geopolitical developments resulting in shift in focus to domestic procurement, and 5) stronger KRW against the USD.

## Disclosure Appendix

## Reg AC

We, Do Hyoung Kim and Joshua Kim, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Do Hyoung Kim GS (Asia) L.L.C., Seoul Branch, Joshua Kim GS (Asia) L.L.C., Seoul Branch.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Hanwha Aerospace and Hyundai Rotem is/are relative to the other companies in its/their coverage universe: Doosan Robotics, HL Mando, Hanwha Aerospace, Hyundai Mobis, Hyundai Motor, Hyundai Rotem, Kia, Robotis

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned $1\%$ or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Hyundai Rotem (W208,500)

GS has received compensation for investment banking services in the past 12 months: Hanwha Aerospace (W1,078,000)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Hanwha Aerospace (W1,078,000) and Hyundai Rotem (W208,500)

GS had an investment banking services client relationship during the past 12 months with: Hanwha Aerospace (W1,078,000) and Hyundai Rotem (W208,500)

GS had a non-securities services client relationship during the past 12 months with: Hanwha Aerospace (W1,078,000) and Hyundai Rotem (W208,500)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking

Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/3a3e05388b88735c4a4c118980db4802bff1b0cfa2a52bedc95920be890c75b5.jpg)

<details>
<summary>line chart</summary>

| Date       | Stock Price | Index: Price |
|------------|-------------|--------------|
| Nov 19     | 1300000     | 1830000      |
| Feb 2025   | 1480000     | 1830000      |
</details>

The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/38dc6246f84d47de604d1db9cf41810a85163a67dfdf28bef91656705d2fed73.jpg)

<details>
<summary>line chart</summary>

| Date       | Stock Price | Index: Price |
|------------|-------------|--------------|
| Nov 19     | 280000      | 7,000        |
</details>

The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

Hyundai Rotem (064350.KS)

<table><tr><td>Date of report</td><td>Target price (W)</td><td>Closing price (W)</td></tr><tr><td>19-Nov-25</td><td>280,000</td><td>186,800</td></tr></table>

Hanwha Aerospace (012450.KS)

<table><tr><td>Date of report</td><td>Target price (W)</td><td>Closing price (W)</td></tr><tr><td>30-Apr-26</td><td>1,800,000</td><td>1,417,000</td></tr><tr><td>10-Mar-26</td><td>1,830,000</td><td>1,455,000</td></tr><tr><td>20-Jan-26</td><td>1,480,000</td><td>1,309,000</td></tr><tr><td>19-Nov-25</td><td>1,300,000</td><td>905,000</td></tr></table>

Price targets sh

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
