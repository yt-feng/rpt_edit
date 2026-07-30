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

\- c) The price of AI compute is holding up as proxied by Hopper rental prices in Figure 12. The price for AI compute would be key for the ability of hyperscalers to monetize their AI capital spending. The higher the price for compute, the higher the ability by hyperscalers to maintain or increase their profit margins. After some persistent downward pressure on compute pricing into end-2025, there have been some signs of improvement in recent months. In addition, we find Figure 12 casts doubt to excessive obsolescence/depreciation assumptions made by some investors.

Figure 12: Compute Desk's Hopper US Index  
Aggregates listed on-demand and reserved prices for renting NVIDIA Hopper (H100 and H200) GPUs from US neocloud providers. The Index is priced in US dollars per GPU per hour.  
![](images/a3c98407583cc4b026bf1404cdf9902c1a6eaa033c287579276e9fd1b484a2a8.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

## The collapse of the odds of the Clarity Act passing by the Senate represents a setback for crypto markets

\- With the Senate prioritizing other legislation ahead of the summer recess, the prediction market odds of the Clarity Act passing before year-end collapsed to 37%, the lowest implied probability so far this year.

\- The ethics issue has emerged as one of the biggest obstacles. Democrats have drawn a line on state enforcement and Republicans and the White House have drawn a line on DoJ enforcement alone. Negotiations are continuing, but it is unclear how this or other impasses on yield, DeFi, and illicit finance, that have not moved in six months, will be eventually resolved.

\- We had previously argued (see F&L Feb 26th 2026) that the Market Structure Bill (i.e. Clarity Act) would act as positive catalyst for crypto markets for several reasons: the legislation introduces a clear framework for classifying crypto tokens as either digital commodities to be overseen by the CFTC or digital securities to be overseen by the SEC, the legislation provides a grace period for new projects to build and decentralize by permitting up to \$75mn in annual capital raising without full SEC registration, the legislation provides a pathway for tokens initially offered as securities to be reclassified as digital commodities in secondary markets once they are sufficiently decentralized and the issuer no longer exercises a managerial role, the legislation establishes a comprehensive regulatory framework for crypto intermediaries by requiring registration with either the CFTC or SEC, ending regulation by enforcement, the legislation promotes the tokenization of traditional securities and real world assets as it makes it easier for them to be brought on-chain, the legislation allows miners, va

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 29 Jul 2026 06:16 PM BST

Disseminated 29 Jul 2026 06:16 PM BST
"""
