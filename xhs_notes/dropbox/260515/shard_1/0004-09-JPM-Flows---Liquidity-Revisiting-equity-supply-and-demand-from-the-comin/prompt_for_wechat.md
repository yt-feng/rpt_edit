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
# Flows & Liquidity

Revisiting equity supply and demand from the coming IPOs

- The typical jump in the free float share after the expiry of the lock-up period in IPOs reflects a rather mechanical reclassification by index providers and is not necessarily the result of selling by insiders or other shareholders.   
- What is certain is that the inclusion of the anticipated big three IPOs into equity indices would necessitate sizeable passive demand from index inclusion and rebalancing.   
- We estimate \$410bn of total passive buying once lock up periods expire, most likely during H1 2026. This \$410bn of buying by passive funds could be accommodated by a combination of companies themselves releasing previous repurchased shares or non-strategic investors selling to passive funds.   
- At index level, the increased weights of the newly included companies would come at the expense of the weights of the companies they replace as well as the biggest tech companies like Mag7. That said, this index rebalancing would not necessarily entail actual selling of Mag7 stocks by passive funds if the past years pattern of strong and steady inflows into passive equity funds continues going forward.   
- The YTD rotation away from Chinese tech towards Korea and Taiwan tech continues in the equity futures space, with only tentative signs of a pause in the equity ETF space.   
- The underperformance trend of both ethereum and other altcoins vs. bitcoin is unlikely to change unless we see meaningful improvements in network activity, DeFi and real world applications.

# Global Markets Strategy

# Nikolaos Panigirtzoglou AC

(44-20) 7134-7815

nikolaos.panigirtzoglou@JPM.com

JPM Securities plc

# Mika Inkinen

(44-20) 7742 6565

mika.j.inkinen@JPM.com

JPM Securities plc

# Min Moon AC

(1-212) 272-8456

min.k.moon@JPM.com

JPM Securities LLC

# Mayur Yeole

(91 22) 6157 3872

mayur.yeole@jpmchase.com

JPM India Private Limited

# Krutik P Mehta

(91-22) 6157-5016

krutik.mehta@jpmchase.com

JPM India Private Limited

Cross Asset Fund Flow Monitor   
Current level shows the latest percentile of weekly flows; Min is denoted by 0 and Max by 1. As of 6 $^{th}$ May 26. 

<table><tr><td>MF &amp; ETF Flows</td><td>Min</td><td>Max</td><td>4 wk avg ($bn)</td><td>2025 avg ($bn)</td></tr><tr><td>All Equities</td><td></td><td>◆</td><td>11.6</td><td>8.1</td></tr><tr><td>All Bonds</td><td></td><td>◆</td><td>13.0</td><td>11.3</td></tr><tr><td>US Equities</td><td></td><td>◆</td><td>8.3</td><td>3.5</td></tr><tr><td>US Bonds</td><td></td><td>◆</td><td>4.7</td><td>4.3</td></tr><tr><td>Non-US Equities</td><td></td><td>◆</td><td>3.3</td><td>4.6</td></tr><tr><td>Non-US Bonds</td><td></td><td></td><td>8.4</td><td>7.0</td></tr><tr><td>US HG Bonds</td><td></td><td>◆</td><td>3.3</td><td>3.4</td></tr><tr><td>US HY Bonds</td><td></td><td></td><td>1.2</td><td>0.4</td></tr><tr><td>US Lev. Loans *</td><td></td><td>◆</td><td>0.3</td><td>0.0</td></tr><tr><td>US MMFs</td><td></td><td>◆</td><td>-0.3</td><td>4.0</td></tr><tr><td>EM Equities</td><td></td><td>◆</td><td>0.5</td><td>0.9</td></tr><tr><td>EM Bonds</td><td></td><td></td><td>1.54</td><td>0.50</td></tr><tr><td>Japan Equities</td><td></td><td>◆</td><td>0.4</td><td>-0.1</td></tr><tr><td>China Equities</td><td></td><td>◆</td><td>-0.19</td><td>-0.15</td></tr><tr><td colspan="5">Europe</td></tr><tr><td>Europe Equities</td><td></td><td>◆</td><td>-2.0</td><td>0.9</td></tr><tr><td>Europe Bonds</td><td></td><td>◆</td><td>4.0</td><td>4.3</td></tr><tr><td>Europe HG Bonds</td><td></td><td>◆</td><td>-0.3</td><td>0.9</td></tr><tr><td>Europe HY Bonds</td><td></td><td></td><td>0.26</td><td>0.17</td></tr><tr><td>Europe MMFs</td><td></td><td>◆</td><td>2.5</td><td>3.8</td></tr><tr><td>Other Equities</td><td></td><td>◆</td><td>4.59</td><td>3.00</td></tr></table>

Source: Lipper, ICI, Bloomberg Finance L.P. and JPM Flows & Liquidity.   
\* US LL historical flows are monthly averages converted to weekly for comparison. China onshore A-share ETFs have been excluded.

Cross Asset Positioning Monitor   
Current level shows the latest percentile, Min is denoted by 0 and Max by 1. 

<table><tr><td>As of 12-May-26</td><td>MIN</td><td>MAX</td><td>Current percentile</td></tr><tr><td>Equities</td><td></td><td></td><td>0.72</td></tr><tr><td>Govt Bonds</td><td></td><td></td><td>0.52</td></tr><tr><td>Credit</td><td></td><td></td><td>0.28</td></tr><tr><td>Dollar</td><td></td><td></td><td>0.47</td></tr><tr><td>Commodities ex Gold</td><td></td><td></td><td>0.90</td></tr><tr><td>Gold</td><td></td><td></td><td>0.67</td></tr><tr><td>Bitcoin</td><td></td><td></td><td>0.66</td></tr><tr><td>EM Equities</td><td></td><td></td><td>0.59</td></tr><tr><td>EM Bonds/FX</td><td></td><td></td><td>0.32</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>0.90</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>0.75</td></tr><tr><td colspan="4">US Equity Sectors:</td></tr><tr><td>Energy</td><td></td><td></td><td>0.78</td></tr><tr><td>Materials</td><td></td><td></td><td>0.66</td></tr><tr><td>Industrials</td><td></td><td></td><td>0.45</td></tr><tr><td>Discretionary</td><td></td><td></td><td>0.59</td></tr><tr><td>Staples</td><td></td><td></td><td>0.17</td></tr><tr><td>Health Care</td><td></td><td></td><td>0.37</td></tr><tr><td>Financials</td><td></td><td></td><td>0.29</td></tr><tr><td>Technology</td><td></td><td></td><td>0.79</td></tr><tr><td>Communication Services</td><td></td><td></td><td>0.54</td></tr><tr><td>Utilities</td><td></td><td></td><td>0.40</td></tr></table>

Source: JPM Flows & Liquidity.
Cross Asset Positioning Monitor aggregates across the various position indicators of Appendix ranging from positioning proxies across various futures contracts, momentum signals as proxies of how trend-following funds/CTAs are positioned, mutual fund betas as proxies of how mutual fund managers are positioned, risk parity fund positioning and leverage proxies, hedge fund betas as proxies of how hedge fund managers are positioned, client surveys, asset allocation estimates of private non-bank investors at global level, short interest indicators, etc.

\- We have noted previously (F&L, Feb 26th) that the close to zero net equity issuance that underpins our bullish equity demand/supply projection for this year is unlikely to change as a result of the potential IPOs by the three biggest private AI companies. This in turn has raised questions in our conversations over what happens after the companies go public. To look at this question, we look at the experience on the aftermath of companies listing via IPOs in terms of the evolution of the share of free float to total market cap and the holdings of insiders, typically company officers and directors as well as large shareholders that hold a more than 10% stake.

\- We start by looking at ten of the largest IPOs since 2010 for data availability on insider shares, and look at the free float share as well as the percentage share of insider holdings in the first 12 months after the IPO. Figure 1 and Figure 2 show the average of the free float shares and the individual free float shares of these IPOs respectively, and Figure 3 and Figure 4 show the average of insider shares and the insider share for the individual companies respectively.

\- We make the following observations. First, the free float shares normally increase relatively slowly until lockups expire, typically around 6 months after the IPO. Second, there is considerable variation in level in terms of both free float shares and insider shares at the company level, reflecting a significant heterogeneity in capital structures. This suggests that while there is a common trend in the free float share, we cannot generalise from this historical experience on where the coming three large AI company IPOs will settle around in terms of the level of free float and insider shares. And third, there is on average a trend for a modest decline in the insider shares in the year after the IPO, though at the company level there are also significant differences (for many companies there has been little reduction in insider stakes).

Figure 1: Average free float shares   
x axis denotes number of trading days after the IPO. In %.   
![](images/37a73eb6c34683968c77644d38e71fa76df5ae309b8ea8e7cfac9f8874aa4bcc.jpg)

<details>
<summary>line</summary>

| x    | y    |
| ---- | ---- |
| 0    | 45   |
| 50   | 45   |
| 100  | 50   |
| 150  | 75   |
| 200  | 78   |
| 250  | 79   |
</details>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 2: Breakdown of free float shares   
x axis denotes number of trading days after the IPO. In %.   
![](images/37859f2275383c09d96bda4894ff523afb646e5154527743f6706dc4a9056e6e.jpg)

<details>
<summary>line</summary>

| X | Meta | Uber | Rivian | Airbnb | Snowflake | DoorDash | Snap | Coinbase | Palantir | Lyft |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 65 | 10 | 20 | 55 | 75 | 80 | 35 | 85 | 90 | 10 |
| 50 | 80 | 10 | 20 | 55 | 75 | 80 | 35 | 85 | 90 | 10 |
| 100 | 85 | 10 | 20 | 55 | 75 | 80 | 35 | 85 | 90 | 70 |
| 150 | 90 | 60 | 65 | 60 | 85 | 85 | 45 | 85 | 90 | 70 |
| 200 | 95 | 60 | 65 | 60 | 85 | 85 | 50 | 85 | 90 | 70 |
| 250 | 95 | 60 | 65 | 60 | 85 | 85 | 50 | 85 | 90 | 70 |
</details>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 3: Average of Insiders shares   
x axis denotes number of trading days after the IPO. In %.   
![](images/b8702a3ca4b37cd1ef8e03c44e8fce404a5d0b47ae6c30bdaa24dd08d00fa750.jpg)

<details>
<summary>line</summary>

| x    | y     |
| ---- | ----- |
| 0    | 6.9   |
| 10   | 7.1   |
| 20   | 7.9   |
| 30   | 7.8   |
| 40   | 7.7   |
| 50   | 7.7   |
| 60   | 7.6   |
| 70   | 7.5   |
| 80   | 7.4   |
| 90   | 7.4   |
| 100  | 7.3   |
| 110  | 7.0   |
| 120  | 6.8   |
| 130  | 6.9   |
| 140  | 6.7   |
| 150  | 6.5   |
| 160  | 6.3   |
| 170  | 6.1   |
| 180  | 5.5   |
| 190  | 5.4   |
| 200  | 5.5   |
| 210  | 5.5   |
| 220  | 5.5   |
| 230  | 5.4   |
| 240  | 5.4   |
| 250  | 5.3   |
| 260  | 5.4   |
</details>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 4: Breakdown of Insiders shares   
x axis denotes number of trading days after the IPO. In %.   
![](images/97353b9b16fc92f26824d3d052045a029d375f86085778dd2ccf6ae1bf2fbcd7.jpg)

<details>
<summary>line</summary>

| X    | Meta | Uber | Rivian | Airbnb | Snowflake | DoorDash | Snap | Coinbase | Palantir | Lyft |
| ---- | ---- | ---- | ------ | ------ | --------- | -------- | ---- | -------- | -------- | ---- |
| 0    | 1    | 1    | 1      | 13     | 5         | 1        | 30   | 1        | 5        | 1    |
| 50   | 1    | 1    | 1      | 13     | 5         | 1        | 30   | 1        | 8        | 1    |
| 100  | 1    | 1    | 1      | 10     | 5         | 1        | 30   | 1        | 8        | 1    |
| 150  | 4    | 8    | 1      | 9      | 5         | 1        | 26   | 1        | 7        | 1    |
| 200  | 4    | 7    | 1      | 7      | 5         | 1        | 25   | 1        | 7        | 1    |
| 250  | 4    | 7    | 1      | 5      | 5         | 1        | 24   | 1        | 7        | 1    |
</details>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- Is the typical jump in the free float share after the expiry of the lock-up period the result of selling by insiders or other shareholders? The answer to our mind is no. Instead, the jump in the free float share after the expiry of the lock-up period is rather mechanical. This is due to the fact that once the lock-up periods expire, the holdings of non-insiders, i.e. non-strategic investors with a stake of less than 10% or employees other than those classified as insiders, are counted toward the free float whether they sell or keep their stakes. This is effectively a reclassification effect by index providers. An argument could also be made that there have been already several opportunities for non-insiders to sell part of their stakes in the big three private AI companies before listing through structured tender offers or secondary market transactions, though in practice the capacity of these secondary markets may be limited. And companies themselves may have been willing to repurchase some of their shares ahead of the listing, perhaps to release these holdings after the lock-up period expiry to facilitate passive demand.

- Indeed, what is certain is that the inclusion of the anticipated big three IPOs into equity indices would necessitate sizeable passive demand from index inclusion and rebalancing. While the visibility of capital structures is limited, it seems that the free float of these companies would eventually likely increase to around 30%-50% after the 6-month lock up periods expires, most likely during the first half of 2027. How much passive buying could this generate?   
- Our colleague Min Moon in equity index research has outlined some timelines of how the inclusion process could take place for different index providers, as well as some calculations of how much passive demand could be created at different levels of free float share assumptions (see Large Cap IPOs and Potential Index Inclusion, May 11th). Assuming the three anticipated IPOs account for a combined market cap of around \$3.5tr, and that at listing around 4% of the shares would be counted toward the free float, this would imply passive rebalancing demand of around \$40bn in total when they are initially included in indices. At the end of the lockup periods (typically 6 months) and assuming that the free float share increases to around 40%, or the mid-point of the 30%-50% range, this could create additional passive rebalancing demand of \$370bn bringing the cumulative total rebalancing related demand to \$410bn. This \$410bn of buying by passive funds could be accommodated by a combination of companies themselves releasing previous repurchased shares or non-strategic investors selling to passive funds. At index level, the increased weights of the newly included companies would come at the expense of the weights of the companies they replace as well as the biggest tech companies like Mag7. That said, this index rebalancing would not necessarily entail actual selling of Mag7 stocks by passive funds if the past years pattern of strong and steady inflows into passive equity funds continues going forward as a disproportionate amount of these inflows could be deployed into the newly listed companies to reach the increased weights.

- What about the historical experience at the index level? Figure 5 shows the free float to total market cap ratio for the S&P 500 and Nasdaq composite. The free float share has historically been more stable, which reflects the fact that by the time companies are listed in the S&P they tend to be more mature and established, there are stricter inclusion criteria, and the share of institutional holdings tends to be higher. That said, there has been a greater convergence over time as the free float share of the Nasdaq has been rising towards that of the S&P over time. In part, this is likely due to the maturing of the tech sector and institutionalisation of ownership, as well as increasing overlap as the S&P has become increasingly tech heavy.   
- This process has not been linear, however. For example, from 2020 until late 2021, the free float share of the Nasdaq declined significantly amid a tech IPO and SPAC boom that saw a lot of newly public companies with significant stakes from founders as well as PE and VC investors, and perhaps with increased stock rewards for insiders and employees amid the bull market. From 2022 to 2024, this reversed as lockup periods expired, allowing founders to sell to institutional investors and as strategic investor holdings were either sold or reclassified as part of the free float, as the market correction reduced tech weights somewhat and as IPO activity dried up. The inclusion of the anticipated three IPOs into equity indices at a somewhat more expedited timeline could see another decline in index free float ratios as the new companies enter equity indices at lower free float ratios than the current index average.

Figure 5: Free float to total market cap ratios for the S&P 500 and Nasdaq composite   
![](images/86c7e9c27ab30923ff7b79a080078cd5c643265e05d6429739d1e40f2077bb97.jpg)

<details>
<summary>line</summary>

| Year | S&P 500 | Nasdaq Composite |
|------|---------|------------------|
| 06   | 95.5%   | 89.5%            |
| 07   | 95.8%   | 90.2%            |
| 08   | 95.7%   | 90.5%            |
| 09   | 95.6%   | 90.3%            |
| 10   | 95.5%   | 90.8%            |
| 11   | 95.4%   | 91.2%            |
| 12   | 95.3%   | 91.5%            |
| 13   | 95.2%   | 91.8%            |
| 14   | 95.1%   | 92.0%            |
| 15   | 95.0%   | 91.8%            |
| 16   | 94.8%   | 91.5%            |
| 17   | 94.7%   | 91.3%            |
| 18   | 94.6%   | 91.2%            |
| 19   | 94.5%   | 91.0%            |
| 20   | 94.4%   | 91.5%            |
| 21   | 94.3%   | 91.8%            |
| 22   | 94.2%   | 92.0%            |
| 23   | 94.1%   | 92.5%            |
| 24   | 94.0%   | 93.0%            |
| 25   | 93.9%   | 93.5%            |
| 26   | 93.8%   | 93.8%            |
</details>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- In all, the typical jump in the free float share after the expiry of the lock-up period in IPOs reflects a rather mechanical reclassification by index providers and is not necessarily the result of selling by insiders or other shareholders. That said the inclusion of the anticipated big three IPOs into equity indices would necessitate sizeable passive demand from index inclusion and rebalancing. We estimate \$410bn of total passive buying once the lock-up periods expire, most likely during H1 2026. This \$410bn of buying by passive funds could be accommodated by a combination of companies themselves releasing previously repurchased shares or non-strategic investors selling to passive funds. At index level, the increased weights of the newly included companies would come at the expense of the weights of the companies they replace, as well as the biggest tech companies like Mag7. That said, this index rebalancing would not necessarily entail actual selling of Mag7 stocks by passive funds if the past years pattern of strong and steady inflows into passive equity funds continues going forward.

# The YTD rotation away from Chinese tech towards Korea and Taiwan tech continues in the equity futures space with only tentative signs of a pause in the equity ETF space

\- One of the most intense flows YTD has been t

[中间内容因长度限制已省略]

ates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its sUBSidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised April 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 13 May 2026 09:52 PM BST

Disseminated 13 May 2026 09:52 PM BST
"""
