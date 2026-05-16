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
US EQUITY VIEWS

# The rise and reach of retail trading in US equities

Retail trading activity has inflected higher alongside the recent equity market rally. GS trading desk estimates show that retail trading volumes have risen by $28\%$ since mid-April and a basket of retail favorite stocks (GSXURFAV) has rallied by $29\%$ over the same period. The recent replacement of pattern day trader rules with less stringent margin requirements increases the likelihood that retail trading activity will rise further.   
We estimate retail traders hold \$12 trillion of equity assets in self-directed brokerage accounts, amounting to approximately 10% of total US corporate equity market value. Retail traders are a sUBSet of US households, which directly and indirectly own the majority of the \$111 trillion US corporate equity market.   
Retail trading activity has recently accounted for roughly $20\%$ of total US equity trading volumes. This is up from $15\%$ a decade ago but below the peak of $24\%$ in 2021. Specialized market makers known as wholesalers execute the majority of retail order flow. As a result, institutional investors typically interact with only a fraction of retail trading activity.   
Retail trading activity has increased during recent equity market drawdowns. Retail volumes in index-linked ETFs rose during the equity market selloffs in 2020, 2022, and 2025. During the most recent selloff, volumes remained light but increased as the market rebounded. In addition to market-wide selloffs, retail trading activity has tended to increase in individual stocks with sharp declines.   
Retail investors employ both margin and leveraged ETFs to boost their equity market exposures. Retail margin debt across select brokers currently equates to 1.8% of customer assets, similar to the previous high reached in 2021. The retail share of trading volumes in leveraged S&P 500 and Nasdaq-100 ETFs has been roughly double the share in unleveraged ETFs tracking the same indices.   
Retail trading activity has recently tilted towards stocks with small market caps, volatile returns, and high valuations. Retail also tends to trade more actively in stocks with high short interest. The retail share of trading volumes in Russell 3000 stocks with the highest short interest was higher in 2025 than in 2021.   
■ Stocks with elevated retail trading activity generally carry elevated

# Daniel Chavez

+1(212)357-7657

daniel.chavez@gs.com

GS & Co. LLC

# Ben Snider

+1(212)357-1744 | ben.snider@gs.com

GS & Co. LLC

# Ryan Hammond

+1(212)902-5625

ryan.hammond@gs.com

GS & Co. LLC

# Jenny Ma

+1(212)357-5775 | jenny.ma@gs.com

GS & Co. LLC

# Kartik Jayachandran

+1(212)855-7744

kartik.jayachandran@gs.com

GS & Co. LLC

# Christophe Sung

+1(212)902-3841

christophe.sung@gs.com

GS & Co. LLC

valuations and exhibit above-average volatility, even controlling for fundamentals like sales growth. Stocks with elevated retail trading activity have also exhibited greater underperformance following earnings misses, suggesting that elevated retail participation may affect how stock prices move to reflect fundamental information.

# Retail traders in the equity ownership landscape

Following a decline in early 2026, retail trading activity has inflected higher alongside the recent equity market rally. GS Global Banking & Markets estimates of retail trading volumes show a $28\%$ increase in retail trading activity since mid-April. Mirroring this increase, a basket of stocks popular with retail traders (GSXURFAV) has rallied by $29\%$ over the same period. See Exhibit 25 for the current constituents of GSXURFAV with the largest recent retail share of trading volumes. The recent replacement of pattern day trader rules with less stringent margin requirements increases the likelihood that retail trading activity will rise further.

Exhibit 1: Retail favorite stocks have rallied alongside a rebound in retail trading activity   
![](images/f67f7cd47ce0c6288a62609a663f36139c03c2c3ca25e557ba1f1278445bea9d.jpg)

<details>
<summary>line</summary>

| Date   | Indexed return of Retail Favorites basket vs. equal-weight S&P 500 (right axis) | Estimated retail trading activity in Russell 3000 stocks (million shares) |
|--------|----------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Jun-25 | ~1250                                                                            | ~1150                                                              |
| Sep-25 | ~1350                                                                            | ~1200                                                              |
| Dec-25 | ~600                                                                             | ~900                                                               |
| Mar-26 | ~100                                                                             | ~700                                                               |
| Jun-26 | ~1300                                                                            | ~850                                                               |
</details>

GSXURFAV basket developed by GS Global Banking & Markets. Retail trading activity reflects GS Global Banking & Markets' estimates of total shares executed on behalf of retail investors.

Source: GS Global Investment Research, GS FICC and Equities

Retail traders are a sUBSet of US households, which are the largest owner of the US equity market. We define retail investors as individuals making self-directed trading decisions in brokerage accounts. The Fed's latest Financial Accounts of the United States data (Z.1) show that US households are the largest owner of corporate equities. Of the \$111 trillion value of corporate equity assets, 40% is directly held by households. Including indirect ownership via retirement accounts, mutual funds, and ETFs, households own the majority of the US corporate equity market.

Exhibit 2: Ownership of the US equity market   
![](images/87fc3607ec1bb1f38aa2c5a26bfb57bc608c07ab60a3f638cdac34647b39e735.jpg)

<details>
<summary>area_stacked</summary>

Ownership of the US corporate equity market
| Year | Direct household ownership (%) |
|---|---|
| 2005 | 40 |
| 2010 | 65 |
| 2015 | 63 |
| 2020 | 60 |
| 2025 | 58 |

| Ownership Type | Percentage (%) |
| :--- | :--- |
| Passive mutual funds | 6 |
| ETFs | 10 |
| Active mutual funds | 10 |
| Pension and govt retirement funds | 9 |
| Foreign investors | 18 |
| Hedge funds | 3 |
| Business hldgs | 3 |
| Other | 2 |
</details>

Source: Federal Reserve, GS Global Investment Research

# Household equity ownership is concentrated at the top of the wealth distribution.

The top 10% of households own 87% of total household equity assets while the bottom 50% of households own just 1% of the total.

However, households in the bottom half of the wealth distribution have historically made larger adjustments to their equity portfolios from quarter to quarter. Across the average quarter since 1990, flows into and out of equities from the bottom $50\%$ of households amounted to $3\%$ of their assets, nearly three times the average for the top $10\%$ of households.

Exhibit 3: Equity ownership share by wealth percentile   
![](images/0801e76b0cefb190c60cc7f3d95dd4215295883ca50c623f6a02049afacaa3c5.jpg)

<details>
<summary>pie</summary>

Household equity ownership by wealth percentile
| Wealth Percentile | Percentage (%) |
| :--- | :--- |
| Top 1% | 47 |
| Next 9% | 40 |
| Next 40% | 12 |
| Bottom 50% (1%) | (1) |
</details>

The “Household” sector described in the DFAs includes private funds such as hedge funds. We reduce the value of the “Top 1%” category’s assets by the Federal Reserve’s estimate of hedge fund corporate equity assets.

Exhibit 4: Variation in household equity flows by wealth percentile quarterly since 1990   
![](images/0189ed0c19dde559f26ba6893f9ab2ef9401b34835c3e6a75c2396de50148eac.jpg)

<details>
<summary>bar</summary>

Average estimated magnitude of quarterly household flow in equities as % of equity assets
| Household wealth percentile | Average estimated magnitude of quarterly household flow in equities as % of equity assets |
| :--- | :--- |
| Top 10% | 1.3 |
| Next 40% | 1.6 |
| Bottom 50% | 3.3 |
</details>

Source: Federal Reserve, GS Global Investment Research   
Source: Federal Reserve, GS Global Investment Research

We estimate that equity assets in self-directed brokerage accounts total \$12 trillion, or 18% of US household directly- and indirectly-owned equity assets. This equates to approximately 10% of total US corporate equity market value. The remaining share represents household equity assets held outside self-directed brokerage accounts, including the value of equity assets held in retirement accounts and equity ownership stakes in private companies, for example.

Exhibit 5: We estimate 18% of households' equity assets are held in self-directed brokerage accounts   
Estimated household ownership of equity assets (\$ trillions)   
![](images/286232d0945f7a12a8bd7f1f3feadd14400ab18dbe951847dddaa84982cca4d9.jpg)

<details>
<summary>pie</summary>

| Category | Value ($tn) | Percentage (%) |
|---|---|---|
| Retirement accounts | 10 | 15 |
| Mutual funds | 10 | 15 |
| ETFs | 5 | 8 |
| Equity assets in self-directed brokerage accounts | 12 | - |
| Direct ownership of individual equities | 41 | 62 |
</details>

Includes ownership of foreign equities. Estimated equity assets in self-directed brokerage account reflects both direct equity ownership and ownership of equities through mutual fund and ETF shares. See appendix for estimation methodology.   
Source: Federal Reserve, GS Global Investment Research

Although retail trading assets represent roughly $10\%$ of US corporate equity assets, retail trading activity has recently accounted for roughly $20\%$ of total US equity trading volumes. According to Bloomberg estimates, retail traders accounted for $19\%$ of US equity trading volumes on average over the last 4 quarters, below a peak of $24\%$ in 2021 and up from $15\%$ a decade ago. As of Q1 2026 retail traders accounted for $17\%$ of US equity trading volumes. Nevertheless, retail's $17\%$ share of trading volume is smaller than the $34\%$ attributable to institutional investors in aggregate. FINRA estimates show that retail accounts for a smaller $11\%$ of trading volumes.

Exhibit 6: Retail share of trading activity has risen in past decade Latest estimate as of Q1 2026   
![](images/34437dcd223eda6a5a0f40796fb678245f87524deb69ad502013687394145b7b.jpg)

<details>
<summary>line</summary>

| Year | Quantitative funds | Retail | Fundamental hedge funds | Long-only funds |
|------|---------------------|--------|--------------------------|-----------------|
| 2016 | 15%                 | 15%    | 15%                      | 12%             |
| 2018 | 15%                 | 15%    | 15%                      | 10%             |
| 2020 | 15%                 | 15%    | 15%                      | 9%              |
| 2022 | 24%                 | 15%    | 12%                      | 8%              |
| 2024 | 18%                 | 15%    | 10%                      | 7%              |
| 2026 | 18%                 | 15%    | 9%                       | 7%              |
| 2028 | 18%                 | 15%    | 9%                       | 7%              |
| 2030 | 18%                 | 15%    | 9%                       | 7%              |
</details>

Remaining share of trading activity is attributable to banks and market makers.   
Source: Bloomberg, GS Global Investment Research

However, institutional investors typically interact directly with only a small portion of retail order flow. Retail brokers route over $87\%$ of order flow to specialized market makers known as wholesalers. A recent analysis from Schwarz et al. (2025) suggests that wholesalers execute $84\%$ of retail orders against their own inventories, a practice known as internalization. Retail orders that are not internalized are routed to another market maker, to dark pools, or to traditional exchanges. As a result, investors are able to access directly only a small share of retail trading activity.

Retail trading volumes are more likely to reach exchanges in volatile markets or when retail order flow becomes large and correlated, however. A 2021 SEC report noted that an increase in on-exchange volumes during volatility spikes may partly reflect wholesalers seeking to avoid internalizing retail orders as hedging becomes more difficult. Furthermore, large and imbalanced retail order flow makes it challenging for wholesalers to keep bid-ask spreads tighter than on-exchange spreads.

Retail trader assets are currently concentrated among a handful of large brokers.

Retail self-directed assets at Charles Schwab, Fidelity, and Vanguard account for roughly 80% of total retail self-directed assets, while Robinhood accounts for just 2%. In 2025, aggregated daily average trades were highest at Charles Schwab, totaling 8 million daily average trades. Daily average trades per account were highest at Interactive Brokers, whose accounts exhibited roughly 4 times the activity of remaining brokers with available data.

Exhibit 7: Retail investor assets are spread across multiple brokers 

<table><tr><td>Broker</td><td>Retail self-directed assets (trillions)</td><td>Share of retail self-directed assets</td></tr><tr><td>Charles Schwab</td><td>$6.6</td><td>38 %</td></tr><tr><td>Fidelity</td><td>4.4</td><td>25</td></tr><tr><td>Vanguard</td><td>2.8</td><td>16</td></tr><tr><td>MS / E*Trade</td><td>1.6</td><td>9</td></tr><tr><td>Wirehouses ex MS</td><td>0.9</td><td>5</td></tr><tr><td>Interactive Brokers</td><td>0.3</td><td>2</td></tr><tr><td>Robinhood</td><td>0.3</td><td>2</td></tr><tr><td>Other</td><td>0.5</td><td>3</td></tr><tr><td>Total</td><td>$17.5</td><td>100 %</td></tr></table>

Source: Cerulli Associates, Company data, GS Global Investment Research

Exhibit 8: Trading activity across select retail brokers   
![](images/fb37240bd67fa650b2d5ffc50096d47b09ffa67f37fd2231d797b165ebc47c22.jpg)

<details>
<summary>bar</summary>

| Category             | Value |
| -------------------- | ----- |
| MS/E*Trade | 1.0   |
| Interactive Brokers  | 3.8   |
| Robinhood            | 4.5   |
| Fidelity             | 4.5   |
| Charles Schwab       | 7.8   |
</details>

Number of 2025 retail accounts at Fidelity is estimated based on number of retail accounts in 2024, 2025 growth in total customer accounts, and proportion of retail accounts to total customer accounts from 2021-2024.   
Source: Data compiled by GS Global Investment Research

# Characteristics of retail trading activity

To analyze retail trading activity we utilize stock-level estimates of retail trading volumes from GS Global Banking & Markets. These estimates largely rely on identifying retail trades in Trade Reporting Facility (TRF) data using an identification method from Boehmer et al. (2021). This approach has become common in academic literature studying retail trading activity $^{1}$ . Academic research has also shown that estimates of retail trading activity using this methodology are likely conservative, particularly for stocks that trade with wide bid-ask spreads $^{2}$ .

# Margin debt and leverage

Margin debt has recently surged to new highs. Margin debt across all FINRA member firms rose to \$1.3 trillion this year, or 52% of gross customer balances. This share is the highest level on record and 6 pp above the previous highest reading in 1998.

Exhibit 9: Margin debt remains near record highs   
![](images/40afca5970e716b8ffb27252f09a764d7b81a82f51000aefe80984e507818f9c.jpg)

<details>
<summary>line</summary>

| Year | % of US equity market cap (right axis) | % of gross customer balances (left axis) |
|------|------------------------------------------|-------------------------------------------|
| 1998 | ~40%                                     | ~45%                                      |
| 2002 | ~-20%                                    | ~-30%                                     |
| 2006 | ~0%                                      | ~0%                                       |
| 2010 | ~-60%                                    | ~-70%                                     |
| 2014 | ~20%                                     | ~15%                                      |
| 2018 | ~45%                                     | ~35%                                      |
| 2022 | ~35%                                     | ~30%                                      |
| 2026 | ~50%                                     | ~45%                                      |
</details>

Source: FINRA, GS Global Investment Research

Margin balances have also increased sharply at several retail brokers. Margin balances at Interactive Brokers, Robinhood, and Charles Schwab registered \$230 billion at the end of March, equating to 1.8% of customer assets. This share is now slightly above the previous record from 2021 but has not meaningfully surpassed that high, in contrast with FINRA data.

Much of the rise in total margin debt over the past decade has likely been driven by institutional investors. FINRA's margin statistics show a \$737 billion increase in margin debt over the past decade vs. a \$189 billion increase in margin balances at Interactive Brokers, Robinhood, and Charles Schwab in aggregate. Furthermore, a recent FINRA survey shows that the proportion of retail investors who own margin accounts and who make margin purchases has declined since 2015.

Exhibit 10: Margin balances at several retail brokers have surged   
![](images/a10170d973e74803bfc9ebb8cc51abe704818227656a1ce4740978ee93ef8e95.jpg)

<details>
<summary>line</summary>

| Year | % of customer assets (right axis) | Margin balances (left axis, billions) |
|------|------------------------------------|----------------------------------------|
| 2010 | ~$20                               | ~1.0%                                  |
| 2012 | ~$30                               | ~1.2%                                  |
| 2014 | ~$40                               | ~1.4%                                  |
| 2016 | ~$50                               | ~1.6%                                  |
| 2018 | ~$70                               | ~1.8%                                  |
| 2020 | ~$50                

[中间内容因长度限制已省略]

me have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
