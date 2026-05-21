你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# Flows & Liquidity

Are bond yields becoming a problem for equities?

- The gap between the equity discount rate of the S&P500 index and the real 10y UST yield, i.e. a proxy for the Equity Risk Premium, has declined to only 2.2% on our estimates, a new low for the post-financial crisis period, breaching the previous low of 2007.   
- The current Equity Risk Premium of 2.2% stands 90bp below its long-run historical average of 3.1%.   
- While it is still some way above its 2000 trough, this implies that there is currently more limited room before a further rise in bond yields starts becoming a problem for the equity market and that from a long-term asset allocation point of view, bonds should command a higher weight relative to equities compared to the norms of the post financial crisis period.   
- Which investor categories have been making bonds trading long in recent weeks?   
- Tokenized money market funds still represent a relatively small 5% proportion of the stablecoin universe.

Cross Asset Fund Flow Monitor   
Current level shows the latest percentile of weekly flows; Min is denoted by 0 and Max by 1. As of 13 $^{th}$ May 26. 

<table><tr><td>MF &amp; ETF Flows</td><td>Min</td><td>Max</td><td>4 wk avg ($bn)</td><td>2025 avg ($bn)</td></tr><tr><td>All Equities</td><td></td><td></td><td>14.8</td><td>8.1</td></tr><tr><td>All Bonds</td><td></td><td></td><td>16.4</td><td>11.3</td></tr><tr><td>US Equities</td><td></td><td></td><td>10.1</td><td>3.5</td></tr><tr><td>US Bonds</td><td></td><td></td><td>7.6</td><td>4.3</td></tr><tr><td>Non-US Equities</td><td></td><td></td><td>4.7</td><td>4.6</td></tr><tr><td>Non-US Bonds</td><td></td><td></td><td>8.8</td><td>7.0</td></tr><tr><td>US HG Bonds</td><td></td><td></td><td>4.1</td><td>3.4</td></tr><tr><td>US HY Bonds</td><td></td><td></td><td>0.8</td><td>0.4</td></tr><tr><td>US Lev. Loans *</td><td></td><td></td><td>0.3</td><td>0.0</td></tr><tr><td>US MMFs</td><td></td><td></td><td>-0.2</td><td>4.0</td></tr><tr><td>EM Equities</td><td></td><td></td><td>-1.5</td><td>0.9</td></tr><tr><td>EM Bonds</td><td></td><td></td><td>1.80</td><td>0.50</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>2.5</td><td>-0.1</td></tr><tr><td>China Equities</td><td></td><td></td><td>-0.16</td><td>-0.15</td></tr><tr><td colspan="5">Europe</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>-1.5</td><td>0.9</td></tr><tr><td>Europe Bonds</td><td></td><td></td><td>4.8</td><td>4.3</td></tr><tr><td>Europe HG Bonds</td><td></td><td></td><td>-0.1</td><td>0.9</td></tr><tr><td>Europe HY Bonds</td><td></td><td></td><td>0.47</td><td>0.17</td></tr><tr><td>Europe MMFs</td><td></td><td></td><td>-1.5</td><td>3.8</td></tr><tr><td>Other Equities</td><td></td><td></td><td>5.30</td><td>3.00</td></tr></table>

Source: Lipper, ICI, Bloomberg Finance L.P. and JPM Flows & Liquidity.   
\* US LL historical flows are monthly averages converted to weekly for comparison. China onshore A-share ETFs have been excluded.

# Global Markets Strategy

# Nikolaos Panigirtzoglou AC

(44-20) 7134-7815

nikolaos.panigirtzoglou@JPM.com

JPM Securities plc

# Mika Inkinen

(44-20) 7742 6565

mika.j.inkinen@JPM.com

JPM Securities plc

# Mayur Yeole

(91 22) 6157 3872

mayur.yeole@jpmchase.com

JPM India Private Limited

# Krutik P Mehta

(91-22) 6157-5016

krutik.mehta@jpmchase.com

JPM India Private Limited

# Cross Asset Positioning Monitor

Current level shows the latest percentile, Min is denoted by 0 and Max by 1. 

<table><tr><td>As of 19-May-26</td><td>MIN</td><td>MAX</td><td>Current percentile</td></tr><tr><td>Equities</td><td></td><td></td><td>0.70</td></tr><tr><td>Govt Bonds</td><td></td><td></td><td>0.48</td></tr><tr><td>Credit</td><td></td><td></td><td>0.32</td></tr><tr><td>Dollar</td><td></td><td></td><td>0.56</td></tr><tr><td>Commodities ex Gold</td><td></td><td></td><td>0.83</td></tr><tr><td>Gold</td><td></td><td></td><td>0.52</td></tr><tr><td>Bitcoin</td><td></td><td></td><td>0.61</td></tr><tr><td>EM Equities</td><td></td><td></td><td>0.66</td></tr><tr><td>EM Bonds/FX</td><td></td><td></td><td>0.35</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>0.90</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>0.71</td></tr><tr><td colspan="4">US Equity Sectors:</td></tr><tr><td>Energy</td><td></td><td></td><td>0.75</td></tr><tr><td>Materials</td><td></td><td></td><td>0.51</td></tr><tr><td>Industrials</td><td></td><td></td><td>0.36</td></tr><tr><td>Discretionary</td><td></td><td></td><td>0.73</td></tr><tr><td>Staples</td><td></td><td></td><td>0.16</td></tr><tr><td>Health Care</td><td></td><td></td><td>0.38</td></tr><tr><td>Financials</td><td></td><td></td><td>0.28</td></tr><tr><td>Technology</td><td></td><td></td><td>0.79</td></tr><tr><td>Communication Services</td><td></td><td></td><td>0.54</td></tr><tr><td>Utilities</td><td></td><td></td><td>0.38</td></tr></table>

Source: JPM Flows & Liquidity.
Cross Asset Positioning Monitor aggregates across the various position indicators of Appendix ranging from positioning proxies across various futures contracts, momentum signals as proxies of how trend-following funds/CTAs are positioned, mutual fund betas as proxies of how mutual fund managers are positioned, risk parity fund positioning and leverage proxies, hedge fund betas as proxies of how hedge fund managers are positioned, client surveys, asset allocation estimates of private non-bank investors at global level, short interest indicators, etc.

\- The steep rise in bond yields over the past weeks is raising questions about its impact on equity markets and whether we have reached a level of interest rates that could induce a more significant equity market correction.

\- In this note, we try to answer this question by looking at the historical evolution of equity yields over time in relation to bond yields. The obvious challenge with this comparison is that equity yields are less straightforward to calculate than bond yields as one needs to make assumptions about the future path of dividends or equity cash flows to be able to derive the equity discount rate as the residual in an equity valuation model. To address this issue, we resort to our long-term fair value framework for the S&P500 index for which we have historical data since 1957 (see A fair value model for US Bonds, Credit and Equities, Panigirtzoglou and Loeys, June 2005). The starting point of this valuation model is the Dividend Discount Model (DDM). Equity valuation is more complicated than bond valuation because of the difficulty in measuring expectations of future cash flows, but ultimately equities also need to be analysed in a discounted cash flow model. That is, the equity price is equal to the expected future cash flows (i.e. dividends) discounted to the present using an Equity Discount Rate (EDR). The equation below illustrates the discounted cash flow model:

$$
P = \sum_ {i} \frac {k \cdot E _ {0} (1 + g) ^ {i}}{(1 + E D R) ^ {i}}
$$

- where P denotes the equity price, E0 is current earnings, k is the payout ratio, g is the growth rate of dividends, and EDR is the Equity Discount Rate.   
- In brief, we take as the starting point for current earnings the four-quarter rolling sum of earnings per share. For the growth rate of dividends, we assume a two-stage DDM, where the first five years are modelled in a recursive model that depends on lagged 5-year earnings and the previous period's P/E ratio. In the second stage, we assume that real earnings growth reverts to a long run average. And the EDR or equity yield is then derived as the residual by inserting the current price of the S&P500 in the above equation.   
- This model-based real Equity Discount Rate or real equity yield of the S&P500 index is depicted along with the real UST yield in Figure 1. The latter is proxied by the nominal yield minus the Philly Fed 10y ahead inflation expectation as index linked yields are only available since late 1990s.

Figure 1: Our model based S&P500 Equity Discount Rate vs. the real 10y UST yield   
![](images/38a9df00cefa517f25efa13b0a8c7fb0bc3228e4c72e18e3c0fb46b48d206c3f.jpg)

<details>
<summary>line</summary>

| Year | S&P500 EDR | 10y real yield |
|------|------------|----------------|
| 57   | ~4.5       | ~1.0           |
| 62   | ~5.0       | ~2.0           |
| 67   | ~4.5       | ~2.5           |
| 72   | ~5.5       | ~3.0           |
| 77   | ~6.0       | ~3.5           |
| 82   | ~7.0       | ~4.0           |
| 87   | ~8.0       | ~3.0           |
| 92   | ~6.5       | ~2.5           |
| 97   | ~5.5       | ~2.0           |
| 02   | ~4.5       | ~1.5           |
| 07   | ~5.0       | ~1.0           |
| 12   | ~6.0       | ~0.5           |
| 17   | ~5.0       | ~0.0           |
| 22   | ~4.5       | ~-1.0          |
</details>

Source: JPM Flows & Liquidity.

- Figure 1 implies relative insensitivity of equity yields to bond yields outside the high macro/policy uncertainty regime seen between 1967 and 1981. It was mostly during that period of macro instability that the equity yield of the S&P500 exhibited high sensitivity to interest rates and had increased almost in tandem with interest rates. Better macro policies after 1981 contributed to normalization in both bond and equity yields.   
- This normalization process lasted for about 15 years until 1996. Since 1996 the real equity yield of the S&P500 has been hovering around 5% even as real bond and cash yields trended lower for more than two decades approaching zero by March 2020. In other words, the steady and large decline in interest rates over the previous two decades had little impact on real equity yields which have been hovering around the 5% mark. As a result, Equity Risk Premia, i.e. the gap between equity and bond yields kept widening reaching a peak of almost 700bp in 2020. Hefty equity risk premia had underpinned the equity bull market that emerged after the financial crisis of 2008.   
- However, Equity Risk Premia have been declining rapidly in recent years with a sharp drop during 2022/2023 as bond yields spiked and another drop more recently as the Iran conflict caused another repricing in bond yields. At the same time an AI driven equity rally since 2023 has pushed equity yields to significantly lower levels. At the moment, on our model, the real equity yield of the S&P500 index stands at 4.4% on our long-term fair value model which is 60bp below the 5% average since mid 1990s. In other words equities look rather expensive (60bp multiplied by duration of around 30 years is equivalent to 18% expensiveness in price terms) on an outright basis relative to the norms of the past thirty years.   
• This expensiveness becomes more pronounced if one

compares equity yields to bond yields. Indeed, as a result of the equity rally and the rise in bond yield in recent months, the gap between the two yields ie the Equity Risk Premium has declined to only 2.2% a new low for the post Lehman crisis period, breaching the previous low of 2007 (Figure 2). In addition, the current Equity Risk Premium of 2.2% is 90bp below its long-run historical average of 3.1%. In other words, equities currently look even more expensive relative to bonds from a long-term investor's perspective.

Figure 2: Equity Risk Premium proxied by the difference between the S&P500 Equity Discount Rate and the real 10y UST yield   
![](images/5dec54da480820972bf612dd332fe4a925867aa71b3f8504e58f174ea71331db.jpg)

<details>
<summary>line</summary>

| Year | S&P500 ERP |
| ---- | ---------- |
| 78   | 5.0        |
| 83   | -1.0       |
| 88   | 2.5        |
| 93   | 3.5        |
| 98   | 1.0        |
| 03   | 4.5        |
| 08   | 5.5        |
| 13   | 7.0        |
| 18   | 6.0        |
| 23   | 2.5        |
</details>

Source: JPM Flows & Liquidity.

\- Admittedly, the Equity Risk Premium had reached a historical low of close to zero at the peak of the tech bubble in 2000, so there is some way to go until we reach the exuberant territory of the late 1990s. Whether markets eventually reach this exuberant territory is an open question. But what is clear from our exercise is that there is currently more limited room before a further rise in real bond yields starts becoming a problem for the equity market, and that from a long-term asset allocation point of view bonds should command a higher weight relative to equities compared to the norms of the post Lehman period.

# Which investor categories have been making bonds trading long in recent weeks?

\- The bond selloff that started with the Iran conflict accelerated in May pushing the Global Agg Bond Index yield to close to 4% (Figure 3). And our implied bond positioning metric based on the reaction of bond markets to economic news shifted towards more positive territory over the past month, suggesting that bond markets have been trading long since late April (Figure 4). Which investor categories have been making bond markets trading long?

Figure 3: Global Agg Bond Index yield   
![](images/2200c93426d64cd6b07d2303842dd629aa064cf6087a0c6732cac8979749a01a.jpg)

<details>
<summary>line</summary>

| Date   | Value |
|--------|-------|
| Jan 25 | 3.7   |
| Mar 25 | 3.6   |
| May 25 | 3.5   |
| Jul 25 | 3.6   |
| Sep 25 | 3.4   |
| Nov 25 | 3.35  |
| Jan 26 | 3.55  |
| Mar 26 | 3.4   |
| May 26 | 3.9   |
</details>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 4: Reaction of bond markets to economic news, a positive number implies that bonds are “trading long”   
![](images/4cf7b32b4a5f985ae8b82ac076759cd7629a4bce9a085dedf77ca4fa5caee971.jpg)

<details>
<summary>line</summary>

| Date   | Bond Yield |
|--------|------------|
| Jan-23 | -0.60      |
| Jul-23 | 0.40       |
| Jan-24 | -0.80      |
| Jul-24 | -0.70      |
| Jan-25 | 0.30       |
| Jul-25 | 0.35       |
| Jan-26 | 0.10       |
</details>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- As a reminder to our readers, the we take as our starting point the economic releases incorporated in our USD and EUR EASI indices, complement them with inflation releases, and then calculate for each release the z-score of surprises (actual – survey median) / (std. dev. of past surprises) and the z-score of changes in UST and Bund yields for that day. We calculate separately the average beta (or the ratio of the z-score of UST and Bund yield

changes over the z-score of economic surprises) for positive and negative news over rolling two-month windows, and take the difference between the two. This indicator represents an indirect positioning metric, and positive (negative) values suggest bond investors have found themselves longer (shorter) duration than they would like to be given the surprises in the economic data flow, rather than necessarily long (short) relative to the benchmark.

\- The largest active US bond mutual fund managers are one investor category that appears to be long duration. This is shown by Figure 5 that depicts the 21-day rolling beta of the 20 largest active US bond mutual fund managers with respect to the US Agg Bond Index. It suggests that the largest active US bond mutual fund managers are long total duration, i.e. government and spread duration together.

Figure 5: 21-day rolling beta of the 20 largest active US bond mutual fund managers with respect to the US Agg Bond Index   
The dotted line shows the average beta since 2013.   
![](images/55cdaafd0176b829e76f31d3592e5f6ce2da8270514ebf2c57a9c0eb921af2f4.jpg)

<details>
<summary>line</summary>

| Date   | Value |
|--------|-------|
| Jan 21 | 0.70  |
| 

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 20 May 2026 08:28 PM BST

Disseminated 20 May 2026 08:28 PM BST
"""
