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
Source: Lipper, ICI, Bloomberg Finance L.P. and JPM Flows & Liquidity.
\* US LL historical flows are monthly averages converted to weekly for comparison. China onshore A-share ETFs have been excluded.

This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## Flows & Liquidity

## Deleveraging likely behind us

\- We find that investors deleveraging in the tech and semiconductor space, including memory stocks, has advanced faster than we had previously anticipated.

\- As a result, we now see more limited room for any further deleveraging.

\- The collapse of the odds of the Clarity Act passing by the Senate represents a setback for crypto markets.

## Cross Asset Fund Flow Monitor

Current level shows the latest percentile of weekly flows; Min is denoted by 0 and Max by 1. As of 22 $^{nd}$ July 26.

<table><tr><td>MF &amp; ETF Flows</td><td>Min</td><td>Max</td><td>4 wk avg ($bn)</td><td>2025 avg ($bn)</td></tr><tr><td>All Equities</td><td></td><td>◆</td><td>12.0</td><td>8.1</td></tr><tr><td>All Bonds</td><td></td><td>◆</td><td>17.8</td><td>11.3</td></tr><tr><td>US Equities</td><td></td><td>◆</td><td>-2.1</td><td>3.5</td></tr><tr><td>US Bonds</td><td></td><td>◆</td><td>9.5</td><td>4.3</td></tr><tr><td>Non-US Equities</td><td></td><td>◆</td><td>14.1</td><td>4.6</td></tr><tr><td>Non-US Bonds</td><td></td><td>◆</td><td>8.3</td><td>7.0</td></tr><tr><td>US HG Bonds</td><td></td><td>◆</td><td>11.8</td><td>3.4</td></tr><tr><td>US HY Bonds</td><td></td><td>◆</td><td>0.2</td><td>0.4</td></tr><tr><td>US Lev. Loans *</td><td></td><td>◆</td><td>0.3</td><td>0.0</td></tr><tr><td>US MMFs</td><td></td><td>◆</td><td>0.5</td><td>4.0</td></tr><tr><td>EM Equities</td><td></td><td>◆</td><td>2.5</td><td>0.9</td></tr><tr><td>EM Bonds</td><td></td><td>◆</td><td>0.93</td><td>0.50</td></tr><tr><td>Japan Equities</td><td></td><td>◆</td><td>2.3</td><td>-0.1</td></tr><tr><td>China Equities</td><td></td><td>◆</td><td>-0.99</td><td>-0.15</td></tr><tr><td colspan="5">Europe</td></tr><tr><td>Europe Equities</td><td></td><td>◆</td><td>0.2</td><td>0.9</td></tr><tr><td>Europe Bonds</td><td></td><td>◆</td><td>5.9</td><td>4.3</td></tr><tr><td>Europe HG Bonds</td><td></td><td>◆</td><td>0.6</td><td>0.9</td></tr><tr><td>Europe HY Bonds</td><td></td><td>◆</td><td>0.27</td><td>0.17</td></tr><tr><td>Europe MMFs</td><td></td><td>◆</td><td>1.6</td><td>3.8</td></tr><tr><td>Other Equities</td><td></td><td>◆</td><td>9.18</td><td>3.00</td></tr></table>

## Global Markets Strategy

Nikolaos Panigirtzoglou AC
(44-20) 7134-7815
nikolaos.panigirtzoglou@JPM.com
JPM Securities plc

Mika Inkinen
(44-20) 7742 6565
mika.j.inkinen@JPM.com
JPM Securities plc

Mayur Yeole
(91 22) 6157 3872
mayur.yeole@jpmchase.com
JPM India Private Limited

## Krutik P Mehta

(91-22) 6157-5016
krutik.mehta@jpmchase.com
JPM India Private Limited

Cross Asset Positioning Monitor Current level shows the latest percentile, Min is denoted by 0 and Max by 1.

<table><tr><td>As of 28-Jul-26</td><td>MIN</td><td>MAX</td><td>Current percentile</td></tr><tr><td>Equities</td><td></td><td></td><td>0.59</td></tr><tr><td>Govt Bonds</td><td></td><td></td><td>0.64</td></tr><tr><td>Credit</td><td></td><td></td><td>0.27</td></tr><tr><td>Dollar</td><td></td><td></td><td>0.81</td></tr><tr><td>Commodities ex Gold</td><td></td><td></td><td>0.64</td></tr><tr><td>Gold</td><td></td><td></td><td>0.54</td></tr><tr><td>Bitcoin</td><td></td><td></td><td>0.55</td></tr><tr><td>EM Equities</td><td></td><td></td><td>0.69</td></tr><tr><td>EM Bonds/FX</td><td></td><td></td><td>0.24</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>0.60</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>0.88</td></tr><tr><td colspan="4">US Equity Sectors:</td></tr><tr><td>Energy</td><td></td><td></td><td>0.73</td></tr><tr><td>Materials</td><td></td><td></td><td>0.57</td></tr><tr><td>Industrials</td><td></td><td></td><td>0.65</td></tr><tr><td>Discretionary</td><td></td><td></td><td>0.65</td></tr><tr><td>Staples</td><td></td><td></td><td>0.27</td></tr><tr><td>Health Care</td><td></td><td></td><td>0.48</td></tr><tr><td>Financials</td><td></td><td></td><td>0.25</td></tr><tr><td>Technology</td><td></td><td></td><td>0.56</td></tr><tr><td>Communication Services</td><td></td><td></td><td>0.32</td></tr><tr><td>Utilities</td><td></td><td></td><td>0.54</td></tr></table>

## Source: JPM Flows & Liquidity.

Cross Asset Positioning Monitor aggregates across the various position indicators of Appendix ranging from positioning proxies across various futures contracts, momentum signals as proxies of how trend-following funds/CTAs are positioned, mutual fund betas as proxies of how mutual fund managers are positioned, risk parity fund positioning and leverage proxies, hedge fund betas as proxies of how hedge fund managers are positioned, client surveys, asset allocation estimates of private non-bank investors at global level, short interest indicators, etc.

\- Two weeks ago, we argued that the deleveraging phase that started in June appeared to be still ongoing and saw room for further deleveraging by investors. Two weeks later, we find that this deleveraging has advanced faster than we had anticipated. As a result, we now see more limited room for any further deleveraging.

## • Where has deleveraging advanced:

\- 1) Starting with hedge funds, we had already noted signs of deleveraging in our previous publication two weeks ago as daily reporting Equity Long/Short funds exhibited less close relationship with semiconductor stocks. By updating our leverage proxy for daily reporting Equity Long/Short hedge funds with respect to the semiconductor (SOX) index, we find evidence that the previous increase in leverage by equity focused hedge funds during April/May has been largely unwound (Figure 1).

Figure 1: Our leverage proxy based on volatility ratios for daily reporting Equity Long/Short hedge funds with respect to the semiconductor (SOX) index  
![](images/d1e06c9bc2b099762a7fcc1f00d25f1300f2b697ab4ee93c88a306f5e66c339c.jpg)  
Source: HFR, Bloomberg Finance L.P., JPM Flows & Liquidity.

\- 2) The elevated short interest on individual tech stocks (Figure 2) or important semiconductor ETFs such as SMH and DRAM (Figure 3) is in our opinion indicative of low net exposure to tech stocks by hedge funds.

Figure 2: Short interest on Semiconductors ex Memory & Hyperscalers individual stocks
Short Interest as a % share of shares outstanding.  
![](images/5434253fb33a56f24d9bcdbe6368954793bb180d3ce63c80dc3686dc1789febd.jpg)  
Source: S3, JPM Flows & Liquidity.

Figure 3: Short interest on SMH and DRAM US Equity ETFs  
Short Interest as a % share of shares outstanding.  
![](images/d5d05054210a04cd3fb3e056ea257adb0b810d009080744c8fa94e7aeb1395e6.jpg)  
Source: S3, JPM Flows & Liquidity.

\- 3) The collapse of momentum signals in tech heavy equity indices suggests that momentum traders such as CTAs have largely unwound previous long equity positions in Nasdaq, Kospi, Taiwan and Nikkei (Figure 4 and Figure 5). In addition, Figure 5 suggests that the previously crowded relative trade of selling China's internet companies (HSCEI Index) and buying Korea/Taiwan/Japan equities has reversed fully.

## Figure 4: Momentum signals for major equity indices

Average z-score of Short- and Long-term momentum signal in our Trend Following Strategy framework shown in Tables A3 and A4 below in the Appendix.  
![](images/9e6602185aa3ca03ed46c35819c075a44d205e118974776d98c4dbcdb6886c08.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.  
Figure 5: Momentum signals for Asian equity indices  
Average z-score of Short- and Long-term momentum signal in our Trend Following Strategy framework shown in Tables A3 and A4 below in the Appendix.

weeks. As a result, the reduction in the AUM of leveraged equity ETFs has taken place much faster than we previously envisaged. In fact, after peaking in June, the AUM ratio of leveraged equity ETFs to the market cap of underlying stocks has largely normalized for all leveraged equity ETFs (including both equity index and individual stock leveraged ETFs), unwinding around 85% of its previous April/May increase (blue line in Figure 6). This is also true for semiconductor stocks ex memory (grey line in Figure 6). For memory stocks, the ratio has unwound around 55% of its previous increase during April/May (black line in Figure 6). In other words, the leveraged ETF problem as a cause of deleveraging and source of excessive volatility should no longer be a significant issue for equities overall and should be much less of an issue for individual memory stocks going forward.

![](images/916a2d09fe448943d6c3406b04cea9eed8b256ed1d7d77d6b99a9f940cd26268.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- 4) For leveraged equity ETFs, we had previously argued that volatile range-trading would suffice to naturally reduce their AUM due to convexity. For example, if the underlying index falls 10% one day and rises 11.1% the following day to reach its previous level, a 3x leveraged ETF would be down 30% on the first day and up 33.3% in the second day, thus ending 7% lower from its previous level. In other words, the excessive growth of leveraged equity ETFs can be self-correcting due to convexity: if excess leverage creates higher frequency of VaR shocks, a volatile range-trading in equities would over time shrink their AUM. And the price effects due to convexity would dominate over continued capital inflows into these leveraged ETFs.

\- Instead of range-trading, we got steep price declines in semiconductor and memory stocks over the past two

Figure 6: AUM of leveraged equity ETFs as % of the market cap of underlying stocks  
![](images/c8bd1e5485f37bd219aea16ca476b50be20b85d063308ccd4e9c215f3d1d99a4.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- 5) In the risk parity fund space, our leverage proxy has already normalized as shown in Figure 7, so excessive leverage by risk parity funds should no longer present a significant headwind for equities going forward.

Figure 7: Implied leverage of risk-parity funds  
Ratio of 3-month rolling volatility of risk-parity funds' returns to the volatility of our risk parity strategy benchmark.  
![](images/b31fe2030d4ca4bb7e65973bd90a460f36dfff5612f26f4a90acbe0b7c9363f7.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- 6) Similarly, in the options space, previous extreme call option buying by retail investors appears to have normalized to historical averages (Figure 8). As a reminder, our proxy of retail investors' option buying based on OCC data (on exchange-traded call option buying by customers with less than 10 contracts), retreated significantly after peaking on June 5th. The peak on June 5th at close to 14 million contracts had matched the previous peaks seen in October 2025 and November 2021.

Figure 8: Exchange-traded Call Option Buys at Open minus Sells at Open for Customers with less than 10 contracts for options on individual equities  
In mn contracts. Last obs is for the week ending 24th July 2026.  
![](images/73aa4e72586bb3b281dfb95c3a16f24f78ad672a9d4023be3ae1a6c0c4d68b5b.jpg)  
Source: OCC, JPM Flows & Liquidity.

\- 7) Leverage in margin accounts stood at very elevated level in June as shown in Figure 9 and thus significantly more deleveraging would need to be seen in July to be able to say that margin account leverage no longer presents a significant headwind for equities. As a reminder, for margin accounts we use the NYSE Net Debit balance as a proxy for US individual investor leverage. While in principle it includes both retail and institutional investors, we believe the majority is likely retail investors. In contrast to hedge funds, who can get leverage more easily or cheaply via options and futures, individuals rely more on Federal Reserve Regulation T. This regulation, which governs customer cash accounts and the amount of credit that brokerage firms and dealers may extend to customers for the purchase of securities, stipulates that one can borrow up to 50% of the purchase price of securities that can be purchased on margin. The NYSE Net Debit balance is calculated as the difference between margin debit balance minus the sum of total credit balances (cash accounts credit + margin account credit). This leverage proxy suggests US individual investor leverage via margin accounts stood at very elevated levels in June and we suspect that a significant decline has taken place in July. Unfortunately, we need to wait for a month to get confirmation of a potential decline in July, as the July observation will be reported at the end of August.

## Figure 9: Net Debit balances in NYSE margin accounts

The NYSE margin account Net Debit balance is equal to the margin debit balance minus the sum of total credit balances (cash account credit +margin account credit). The blue line is constructed by the Net Debit balance in \$bn divided by the market capitalisation of the S&P500 Index. Last monthly observation is for June 2026.  
![](images/df81d368bafb9281cd316e8a78a60e7b65b3f6adc0803a067b787119f27adab3.jpg)  
Source: FINRA, JPM Flows & Liquidity.

\- In all, we find that investors deleveraging in the tech and semiconductor space, including memory stocks, has advanced faster than we had previously anticipated. As a result, we now see more limited room for any further deleveraging. For Korea in particular, we recommend the recent note by our colleague Mixo Das “Korea Equity Strategy – Update on the de-leveraging process in Korea (2)” July 29th 2026, who arrived at a similar conclusion to ours.

\- Finally, assuming our thesis above proves correct and most of the investor deleveraging is behind us, we believe the equity market will likely receive support from the following developments:

\- a) Memory prices are still rising, providing fundamental support to memory makers which have been at the center of recent deleveraging (Figure 10).

Figure 10: inSpectrum Tech memory prices  
![](images/a3259c513a2ca31d2ef7473666f23b87a79d10a743dc8b1eb73127d57ccaf5d7.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- b) The hyperscalers capex projections have been raised significantly by analysts for both 2026 and 2027 (Figure 11) to \$770bn and \$1tr from \$758bn and \$925bn on July $1^{st}$ , respectively.

Figure 11: US hyperscalers capex projections by the consensus of bottom-up analysts as reported by Bloomberg

<table><tr><td>In $bn</td><td>23</td><td>24</td><td>25</td><td>26E</td><td>27E</td><td>28E</td><td>29E</td><td>30E</td></tr><tr><td>Google</td><td>32.3</td><td>52.5</td><td>91.4</td><td>197.0</td><td>290.2</td><td>312.7</td><td>305.4</td><td>315.5</td></tr><tr><td>Amazon</td><td>52.7</td><td>83.0</td><td>131.8</td><td>200.1</td><td>238.7</td><td>250.7</td><td>252.0</td><td>256.1</td></tr><tr><td>Meta</td><td>27.3</td><td>37.3</td><td>69.7</td><td>135.6</td><td>175.0</td><td>194.8</td><td>192.0</td><td>196.0</td></tr><tr><td>Microsoft</td><td>28.1</td><td>44.5</td><td>64.6</td><td>160.6</td><td>198.1</td><td>223.8</td><td>255.9</td><td>279.6</td></tr><tr><td>Oracle</td><td>8.7</td><td>6.9</td><td>21.2</td><td>76.7</td><td>99.3</td><td>102.7</td><td>90.5</td><td>73.9</td></tr><tr><td>Total</td><td>149.0</td><td>224.1</td><td>378.7</td><td>770.1</td><td>1,001.4</td><td>1,084.7</td><td>1,095.8</td><td>1,121.2</td></tr><tr><td>Y/Y growth</td><td>-4%</td><td>50%</td><td>69%</td><td>103%</td><td>30%</td><td>8%</td><td>1%</td><td>2%</td></tr></table>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- c) The price of AI compu

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 29 Jul 2026 06:16 PM BST

Disseminated 29 Jul 2026 06:16 PM BST
"""
