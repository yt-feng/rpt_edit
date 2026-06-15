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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Distribution of ratings: See the distribution of ratings disclosure above. Price chart: See the price chart, with changes of ratings and price targets in prior periods, above, or, if electronic format or if with respect to multiple companies which are the subject of this report, on the GS website at https://www.gs.com/research/hedge.html.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any acce

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
