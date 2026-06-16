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
# Global Macro Outlook and Strategy

Global Rates, Commodities, Currencies and Emerging Markets

Luis Oganes AC

(44-20) 7742-1420

luis.oganes@JPM.com

JPM Securities plc

## US Rates

Money markets price an earlier and more aggressive Fed hiking path than our forecast, though with labor market data potentially suggesting policy may not be restrictive and term premium normalizing, this justifies an upward sloping OIS curve. Global central bank tightening combined with unattractive Treasury valuations versus other DM government bonds should anchor Treasury yields at higher levels, and could push yields higher from here. We project 2- and 10-year yields will rise to 4.20% and 4.70%, respectively, at YE26. Stay short 10-year Treasuries versus Bunds, and enter 10s/30s Treasury curve flatteners, as a soft-bearish trade with relative value. Given large funding gaps emerging in FY27 and beyond, we expect Treasury to remove the “at least” from its forward guidance in August, to prepare for a multi-quarter series of coupon increases commencing in February 2027. The administration's focus on lowering long-end yields increases risks this forward guidance change may be delayed, potentially pushing coupon increases later into 2027. We adjust lower our projections for foreign demand for Treasuries, as well as our bank demand forecast

## International Rates

After the sharp sell-off driven by the energy price spike at the start of the Middle East conflict in late February, DM front-end rates have traded in a wide range over the past couple of months. With inflation still high but growth broadly holding up, we expect most DM central banks to deliver a gradual and shallow policy tightening over the coming months. OIS markets are broadly pricing a larger and faster tightening than our forecasts across most DM. On the Middle East conflict, we believe that risks remain skewed more towards the ongoing status quo and Strait of Hormuz limbo. We continue to expect EUR and GBP rates to range trade and our strategy is to favour long positions when valuations are close levels projected in our energy price spike scenario.

## Commodities

We estimate June oil flows through Hormuz are running at 5.1 mbd, up from 2.9 mbd in May, 3.3 mbd in April, and 2.2 mbd in March. The rebound is meaningful, but it still leaves flows at only about 25% of pre-war levels. NWE storage sits at record lows for this time of year, and the longer summer TTF prices remain at a premium to winter prices and at a discount to JKM, the higher the risk of policy intervention.  
The sharp deficit in aluminum is taking time to transmit through the supply chain, a process that will continue even after the Strait reopens. As part of the US-China summit held on May 15-16 in Beijing, China has agreed to purchase US agricultural products of at least \$17 billion per year in addition to the already agreed upon purchase commitments of 25 million tonnes of soybean purchases per year in 2026-28.

## Currencies

Pockets of upside inflation surprises in G10, rising US real yields, and a fading debasement narrative keep our bullish USD/bullish carry barbell strategy intact. Chair Warsh's inaugural FOMC is the marquee event next week, with the 2027 dot and the press conference set to be market-movers. An orthodox acknowledgement of stronger US cyclicals may be enough to constitute a hawkish outcome for the dollar, which continues to trade at a discount to rates fair value; we head into event long. History counsels that the dollar reliably appreciates \~5% in the 6 months leading up to the first Fed hike of a cycle, FX carry benefits, and vol ratchets 3-5pts post-delivery. Elsewhere in G10, a fully-priced hike, potential QT halt, and Ueda's absence at the presser skew JPY risks dovish at next week's BoJ; hawkish Norges vs. dovish Riksbank divergence could headline European CB outcomes; while the Makerfield by-election aftermath will likely prove a bigger GBP driver than the BoE.

## Emerging Markets

Resilient cyclical backdrop, low fundamental vulnerabilities and the proactive stance of several EM central banks to allow for continued carry outperformance even as higher inflation and a likely hawkish shift by the Fed could challenge the asset class.  
We turn OW EM FX (from MW) in higher yielders and currencies where central banks are ready to hike and also favor frontier FX. Elsewhere, we note that valuations do not offer a clear risk reward amid elevated risks and we stay MW rates, sovereign and corporate credit.

Page

<table><tr><td>1</td><td>US Rates: Raising year-end forecasts, stay short Treasuries versus bunds</td><td>2</td></tr><tr><td>2</td><td>International Rates: More of the same over 2H: range trade duration, cross market long EUR vs. US</td><td>11</td></tr><tr><td>3</td><td>FX: Central banks take centre stage</td><td>18</td></tr><tr><td>4</td><td>Commodities: Schrödinger&#x27;s Strait</td><td>27</td></tr><tr><td>5</td><td>Emerging Markets: Stay OW EM FX and MW Rates, EM Sovereigns &amp; Corporates</td><td>32</td></tr><tr><td>6</td><td>Appendix</td><td>38</td></tr></table>

JPM US interest rate forecast, %

<table><tr><td></td><td>Actual12-Jun-26</td><td>2Q2630-Jun-26</td><td>3Q2630-Sep-26</td><td>4Q2631-Dec-26</td><td>1Q2731-Mar-27</td><td>2Q2730-Jun-27</td></tr><tr><td colspan="7">Rates (%)</td></tr><tr><td>Effective funds rate</td><td>3.62</td><td>3.62</td><td>3.62</td><td>3.62</td><td>3.62</td><td>3.62</td></tr><tr><td>S OFR</td><td>3.60</td><td>3.60</td><td>3.60</td><td>3.60</td><td>3.60</td><td>3.60</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2-yr Treasury</td><td>4.08</td><td>4.15</td><td>4.15</td><td>4.20</td><td>4.20</td><td>4.30</td></tr><tr><td>3-yr Treasury</td><td>4.13</td><td>4.20</td><td>4.20</td><td>4.25</td><td>4.25</td><td>4.35</td></tr><tr><td>5-yr Treasury</td><td>4.21</td><td>4.30</td><td>4.40</td><td>4.45</td><td>4.50</td><td>4.50</td></tr><tr><td>7-yr Treasury</td><td>4.34</td><td>4.40</td><td>4.45</td><td>4.55</td><td>4.65</td><td>4.65</td></tr><tr><td>10-yr Treasury</td><td>4.48</td><td>4.55</td><td>4.65</td><td>4.70</td><td>4.75</td><td>4.75</td></tr><tr><td>20-yr Treasury</td><td>4.98</td><td>5.05</td><td>5.15</td><td>5.20</td><td>5.25</td><td>5.25</td></tr><tr><td>30-yr Treasury</td><td>4.97</td><td>5.00</td><td>5.10</td><td>5.15</td><td>5.15</td><td>5.15</td></tr><tr><td colspan="7">Spreads (bp)</td></tr><tr><td>Fed funds/2yr</td><td>46</td><td>53</td><td>53</td><td>58</td><td>58</td><td>68</td></tr><tr><td>2s/10s</td><td>40</td><td>40</td><td>50</td><td>50</td><td>55</td><td>45</td></tr><tr><td>2s/5s</td><td>13</td><td>15</td><td>25</td><td>25</td><td>30</td><td>20</td></tr><tr><td>5s/10s</td><td>27</td><td>25</td><td>25</td><td>25</td><td>25</td><td>25</td></tr><tr><td>5s/30s</td><td>76</td><td>70</td><td>70</td><td>70</td><td>65</td><td>65</td></tr><tr><td>10s/30s</td><td>49</td><td>45</td><td>45</td><td>45</td><td>40</td><td>40</td></tr></table>

Source: JPM

We forecast US GDP will grow 2.0% (q4/q4) in 2026, while core PCE remains firm at 3.4% (q4/q4). The unemployment rate should gradually fall over 2026, reaching 4.1% (%q/q, saar) in 4Q26  
We expect the Fed to remain on pause for the whole of 2026, holding the funds rate target range to $3.5 - 3.75\%$ . We see the Fed as likely to raise policy rates in 3Q27 as labour markets tighten and inflation remains above target  
- Against this backdrop, we see 2-year Treasury yields reaching $4.20\%$ by YE26. Meanwhile 10-year yields should rise to $4.70\%$ by YE26  
• We see the intermediate section of the curve underperforming, with 2s/10s modestly steeper over the period

Three-month moving average of nonfarm payroll growth (lhs, '000s) versus continuing jobless claims (rhs, '000s)  
![](images/dfec72b096c1bc1a82081a86b6c65a85f9fd4167d1f9f2d454cd1c83331ed099.jpg)

<details>
<summary>line chart</summary>

| Date   | NFP (lhs) | Containing claims (rhs) |
|--------|-----------|--------------------------|
| May 23 | 250       | 1700                     |
| Nov 23 | 150       | 1750                     |
| May 24 | 200       | 1800                     |
| Nov 24 | 100       | 1850                     |
| May 25 | 50        | 1900                     |
| Nov 25 | -50       | 1950                     |
| May 26 | 1700      | 1800                     |
</details>

Source: BLS, Department of Labor

10-year Treasury/German bund spread regressed on 1y1y USD/EUR OIS spread (bp), regression over the last 5 years; bp  
![](images/c9a3dcb4f9116b02c0258312db818ed854a43b65308c91366bc6705047cc1a87.jpg)

<details>
<summary>scatterplot</summary>

| Date       | Value |
| ---------- | ----- |
| 12-Jun-26  | 140   |
</details>

Source: JPM

- OIS forwards are pricing in a full hike by the January meeting, and upward of 35bp in hikes over the next 1- to 2 years, a more hawkish pricing than our own projection of a single hike in 3Q27. However, we do not think this gap will close soon, as a stable unemployment rate leaves a question of whether the current stance of monetary policy is actually restrictive  
- A steeper OIS curve should propagate through to higher Treasury yields, and we think valuations also support Treasury yields rising further from current levels: intermediate Treasury yields appear 24bp too low to fair value model  
- Central banks which lean hawkish could act to keep yields across the DM and in the US buoyed at higher levels than prevailed pre-conflict, especially as Treasuries remain relatively unattractive compared to other DM bonds. For this reason, alongside relatively attractive European valuations, we recommend selling 10-year Treasuries versus German bunds

Current levels for various Treasury curves, with 5-year statistics and regression statistics from curve fair-value models\* with current residuals and z-scores;

<table><tr><td>Curve</td><td>Last</td><td>Min</td><td>Max</td><td>Avg</td><td>%</td><td>R^2</td><td>1y1y OIS</td><td>5y5y BE</td><td>Tariff dummy</td><td>Fed Balance Sheet</td><td>Current residual</td><td>Current Z-score</td><td>3m C+R</td></tr><tr><td>2s/5s</td><td>13</td><td>-78</td><td>78</td><td>-5</td><td>67%</td><td>71%</td><td>-0.32</td><td>0.75</td><td>0.07</td><td>-0.02</td><td>31.1</td><td>1.5</td><td>3.3</td></tr><tr><td>2s/10s</td><td>40</td><td>-109</td><td>136</td><td>9</td><td>62%</td><td>82%</td><td>-0.52</td><td>0.93</td><td>0.14</td><td>-0.05</td><td>37.2</td><td>1.5</td><td>4.0</td></tr><tr><td>2s/30s</td><td>89</td><td>-119</td><td>203</td><td>40</td><td>64%</td><td>87%</td><td>-0.67</td><td>0.84</td><td>0.26</td><td>-0.08</td><td>51.5</td><td>1.9</td><td>5.7</td></tr><tr><td>3s/7s</td><td>21</td><td>-55</td><td>88</td><td>8</td><td>62%</td><td>86%</td><td>-0.29</td><td>0.46</td><td>0.05</td><td>-0.03</td><td>14.9</td><td>1.3</td><td>0.3</td></tr><tr><td>5s/10s</td><td>27</td><td>-36</td><td>71</td><td>14</td><td>67%</td><td>93%</td><td>-0.20</td><td>0.18</td><td>0.07</td><td>-0.03</td><td>6.1</td><td>1.0</td><td>0.7</td></tr><tr><td>5s/20s</td><td>77</td><td>-23</td><td>133</td><td>54</td><td>68%</td><td>90%</td><td>-0.27</td><td>-0.02</td><td>0.19</td><td>-0.04</td><td>17.0</td><td>1.6</td><td>0.8</td></tr><tr><td>5s/30s</td><td>76</td><td>-46</td><td>141</td><td>45</td><td>69%</td><td>93%</td><td>-0.35</td><td>0.09</td><td>0.20</td><td>-0.06</td><td>20.3</td><td>1.7</td><td>2.4</td></tr><tr><td>7s/10s</td><td>14</td><td>-21</td><td>31</td><td>6</td><td>69%</td><td>95%</td><td>-0.09</td><td>0.08</td><td>0.05</td><td>-0.02</td><td>2.5</td><td>0.9</td><td>0.8</td></tr><tr><td>10s/20s</td><td>50</td><td>13</td><td>65</td><td>40</td><td>72%</td><td>71%</td><td>-0.07</td><td>-0.20</td><td>0.12</td><td>-0.01</td><td>11.0</td><td>1.6</td><td>0.1</td></tr><tr><td>10s/30s</td><td>49</td><td>-18</td><td>70</td><td>31</td><td>72%</td><td>87%</td><td>-0.15</td><td>-0.09</td><td>0.12</td><td>-0.02</td><td>14.2</td><td>1.9</td><td>1.7</td></tr><tr><td>20s/30s</td><td>-1</td><td>-32</td><td>11</td><td>-9</td><td>74%</td><td>90%</td><td>-0.08</td><td>0.11</td><td>0.00</td><td>-0.02</td><td>3.3</td><td>1.1</td><td>1.6</td></tr></table>

\*5-year regression of various Treasury curves on 1y1y OIS rates (%), 5y5y TIPS seasonally-adjusted breakevens (%), tariff dummy for trade uncertainty that turns 1 between 4/2/25 and 2/26/26, and Fed balance sheet size relative to GDP (%)  
Source: JPM

- The Treasury curve has retraced to its flattest levels in over a year, also driven by the hawkish shift in Fed policy expectation. However, most curve pairs appear too steep after controlling for 1y1y OIS, 5y5y TIPS breakevens, the Fed’s balance sheet as a share of GDP, and our trade policy uncertainty variable, using a sample over the last 5 years  
- Combined with our modest bearish bias conveyed in our interest rate forecasts, rich valuations versus other DM government bonds, and the output of our curve model, we think flatteners offer better value than outright duration shorts  
- Along the curve, we recommend 10s/30s flatteners as this curve appears 14bp steep after adjusting for its fundamental drivers, a divergence of nearly 2 standard deviations

Statistics from JPM 10-year Treasury fair-value model; units as indicated

<table><tr><td>Factor</td><td>Current value</td><td>Coefficient</td><td>T-stat</td></tr><tr><td>1y1y OIS rate; %</td><td>3.365</td><td>0.603</td><td>86.36</td></tr><tr><td>JPM US FRI; % pts</td><td>92.4</td><td>-0.055</td><td>-9.02</td></tr><tr><td>5y5y TIPS breakevens; %</td><td>1.975</td><td>0.080</td><td>1.71</td></tr><tr><td>Fed B/S as share of US economy</td><td>21.1</td><td>-0.113</td><td>-39.20</td></tr><tr><td>Tariff dummy variable*</td><td>1</td><td>-0.074</td><td>-4.35</td></tr><tr><td>R=squared; %</td><td>98.1%</td><td></td><td></td></tr><tr><td>Standard Error, bp</td><td>13.6</td><td></td><td></td></tr><tr><td>Residual; bp</td><td>-11.6</td><td></td><td></td></tr></table>

\* Represents trade policy uncertainty, that is 1 on and after 4/2/25  
Source: JPM, Federal Reserve

- The US Attorney for DC announced it was ending the investigation into the Fed headquarters cost overrun, which paved the way for the swearing in of Kevin Warsh as the new Chair of the Federal Reserve  
We continue to believe that the Committee's tradition of collegiality and respect for dissent means that policy is ultimately a collective decision, and that the chair's effectiveness depends on their ability to align his views with the broader group  
- Warsh has made the case for simultaneously shrinking the balance sheet and cutting rates, as this would reduce the Fed's footprint in the market while having a more neutral impact on financial conditions overall. Our fair value model suggests that it would take close to \$1tn reduction in the size of the balance sheet even to warrant a 25bp cut

JPM projection of net privately-held borrowing, Treasury buybacks, Federal Reserve purchases of Treasuries, and expected change in Treasuries held by private investors; \$bn

<table><tr><td rowspan="2">Year</td><td rowspan="2">Total net privately-held borrowing</td><td rowspan="2">Buybacks</td><td colspan="2">Fed secondary market purchases</td><td colspan="2">Net change in privately-held debt outstanding</td></tr><tr><td>Bills</td><td>Coupons</td><td>Bills</td><td>Coupons</td></tr><tr><td>CY 2020</td><td>4301</td><td>0</td><td>157</td><td>2184</td><td>2390</td><td>-432</td></tr><tr><td>CY 2021</td><td>1607</td><td>0</td><td>0</td><td>938</td><td>-1195</td><td>1961</td></tr><tr><td>CY 2022</td><td>1681</td><td>0</td><td>0</td><td>99</td><td>-37</td><td>1539</td></tr><tr><td>CY 2023</td><td>3122</td><td>0</td><td>0</td><td>0</td><td>2047</td><td>1107</td></tr><tr><td>CY 2024</td><td>2422</td><td>85</td><td>0</td><td>0</td><td>538</td><td>1823</td></tr><tr><td>CY 2025</td><t

[中间内容因长度限制已省略]

of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
