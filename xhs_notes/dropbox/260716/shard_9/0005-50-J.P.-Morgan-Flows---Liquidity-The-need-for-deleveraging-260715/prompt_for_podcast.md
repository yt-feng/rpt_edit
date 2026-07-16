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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# Flows & Liquidity

The need for deleveraging

\- The investor deleveraging phase that started in June appears to be still ongoing and we see more room for deleveraging in leveraged equity ETFs, options and margin accounts, thus acting as a headwind for equities going forward.

\- The excessive growth of leveraged equity ETFs can be self-correcting: if excess leverage creates higher frequency of VaR shocks, a volatile range-trading in equities would over time shrink the AUM of leveraged equity ETFs.

\- That said, it will perhaps take another three months or so of volatile range-trading in equities until the leveraged equity ETF AUM ratios to the market cap of underlying stocks return to pre-April levels for either memory stocks or all equity ETFs.

\- Once this deleveraging abates, longer-term equity demand/supply dynamics should provide a support.

• Some encouraging signs from bitcoin futures.

## Cross Asset Fund Flow Monitor

Current level shows the latest percentile of weekly flows; Min is denoted by 0 and Max by 1. As of 8 $^{th}$ July 26.

<table><tr><td>MF &amp; ETF Flows</td><td>Min</td><td>Max</td><td>4 wk avg ($bn)</td><td>2025 avg ($bn)</td></tr><tr><td>All Equities</td><td></td><td></td><td>29.6</td><td>8.1</td></tr><tr><td>All Bonds</td><td></td><td></td><td>16.8</td><td>11.3</td></tr><tr><td>US Equities</td><td></td><td></td><td>20.3</td><td>3.5</td></tr><tr><td>US Bonds</td><td></td><td></td><td>10.1</td><td>4.3</td></tr><tr><td>Non-US Equities</td><td></td><td></td><td>9.3</td><td>4.6</td></tr><tr><td>Non-US Bonds</td><td></td><td></td><td>6.7</td><td>7.0</td></tr><tr><td>US HG Bonds</td><td></td><td></td><td>10.1</td><td>3.4</td></tr><tr><td>US HY Bonds</td><td></td><td></td><td>0.7</td><td>0.4</td></tr><tr><td>US Lev. Loans *</td><td></td><td></td><td>0.3</td><td>0.0</td></tr><tr><td>US MMFs</td><td></td><td></td><td>-0.3</td><td>4.0</td></tr><tr><td>EM Equities</td><td></td><td></td><td>-1.3</td><td>0.9</td></tr><tr><td>EM Bonds</td><td></td><td></td><td>0.74</td><td>0.50</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>0.8</td><td>-0.1</td></tr><tr><td>China Equities</td><td></td><td></td><td>-0.91</td><td>-0.15</td></tr><tr><td colspan="5">Europe</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>-0.6</td><td>0.9</td></tr><tr><td>Europe Bonds</td><td></td><td></td><td>4.2</td><td>4.3</td></tr><tr><td>Europe HG Bonds</td><td></td><td></td><td>0.7</td><td>0.9</td></tr><tr><td>Europe HY Bonds</td><td></td><td></td><td>0.59</td><td>0.17</td></tr><tr><td>Europe MMFs</td><td></td><td></td><td>6.9</td><td>3.8</td></tr><tr><td>Other Equities</td><td></td><td></td><td>10.72</td><td>3.00</td></tr></table>

Source: Lipper, ICI, Bloomberg Finance L.P. and JPM Flows & Liquidity.
\* US LL historical flows are monthly averages converted to weekly for comparison. China onshore A-share ETFs have been excluded.

## Global Markets Strategy

Nikolaos Panigirtzoglou AC
(44-20) 7134-7815
nikolaos.panigirtzoglou@JPM.com
JPM Securities plc

## Mika Inkinen

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

<table><tr><td>As of 14-Jul-26</td><td>MIN</td><td>MAX</td><td>Current percentile</td></tr><tr><td>Equities</td><td></td><td></td><td>0.64</td></tr><tr><td>Govt Bonds</td><td></td><td></td><td>0.64</td></tr><tr><td>Credit</td><td></td><td></td><td>0.29</td></tr><tr><td>Dollar</td><td></td><td></td><td>0.79</td></tr><tr><td>Commodities ex Gold</td><td></td><td></td><td>0.51</td></tr><tr><td>Gold</td><td></td><td></td><td>0.49</td></tr><tr><td>Bitcoin</td><td></td><td></td><td>0.56</td></tr><tr><td>EM Equities</td><td></td><td></td><td>0.81</td></tr><tr><td>EM Bonds/FX</td><td></td><td></td><td>0.22</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>0.72</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>0.87</td></tr><tr><td colspan="4">US Equity Sectors:</td></tr><tr><td>Energy</td><td></td><td></td><td>0.74</td></tr><tr><td>Materials</td><td></td><td></td><td>0.51</td></tr><tr><td>Industrials</td><td></td><td></td><td>0.42</td></tr><tr><td>Discretionary</td><td></td><td></td><td>0.54</td></tr><tr><td>Staples</td><td></td><td></td><td>0.14</td></tr><tr><td>Health Care</td><td></td><td></td><td>0.43</td></tr><tr><td>Financials</td><td></td><td></td><td>0.22</td></tr><tr><td>Technology</td><td></td><td></td><td>0.65</td></tr><tr><td>Communication Services</td><td></td><td></td><td>0.35</td></tr><tr><td>Utilities</td><td></td><td></td><td>0.47</td></tr></table>

Cross Asset Positioning Monitor aggregates across the various position indicators of Appendix ranging from positioning proxies across various futures contracts, momentum signals as proxies of how trend-following funds/CTAs are positioned, mutual fund betas as proxies of how mutual fund managers are positioned, risk parity fund positioning and leverage proxies, hedge fund betas as proxies of how hedge fund managers are positioned, client surveys, asset allocation estimates of private non-bank investors at global level, short interest indicators, etc.

\- Despite a decline in S&P500 and Nasdaq indices during June, the performance of equity-focused hedge funds such as Equity Long/Short and Equity Sector TMT was positive at 1.2% and 3.7%, respectively. Their performance was likely helped by semiconductors, with the SMH Semiconductor ETF up 9.5% in June vs. -14.5% loss for US hyperscalers on the month. In other words, last month's hedge fund performance is consistent with equity-focused hedge funds maintaining an overweight exposure to semiconductors through June.

\- We do not have comprehensive data for July yet from monthly reporting hedge funds, but the smaller universe of daily reporting Equity Long/Short funds points to a less close relationship with semiconductor stocks (Figure 1), suggesting that equity-focused hedge funds might have deleveraged/reduced their exposure to semiconductors during July.

Figure 1: HFRX Equity Hedge index vs SMH Semiconductor equity ETF  
![](images/04284363d6c1fc9c1b9507d38605c09be1700b636712cfbba9e65e8b4ee8b9a2.jpg)  
Source: HFR, Bloomberg Finance L.P., JPM Flows & Liquidity.

\- This is consistent with our higher-frequency leverage proxy for Equity Long/Short hedge funds, which as shown in Figure 2 it subsided somewhat in July after reaching its highest level since 2017 in June.

Figure 2: Our higher-frequency leverage proxy for equity Long/Short hedge funds  
![](images/60a0b6a235e39f6a9e280b09512b462496f26f4c2b4c066e9d3f7e93221f8505.jpg)  
Source: HFR, Bloomberg Finance L.P., JPM Flows & Liquidity.

\- In our opinion there is a need for normalizing in leverage across a wider investor spectrum beyond equity-focused hedge funds. Indeed, we see signs that this normalizing in leverage across a wide set of metrics beyond the HF leverage metric of Figure 2.

\- For leveraged equity ETFs, volatile range-trading is naturally reducing their AUM due to convexity. For example, if the underlying index falls 10% one day and rises 11.1% the following day to reach its previous level, a 3x leveraged ETFs would be down 30% on the first day and up 33.3% in the second day, thus ending 7% lower from its previous level. In other words, the excessive growth of leveraged equity ETFs can be self-correcting due to convexity: if excess leverage creates higher frequency of VaR shocks, a volatile range-trading in equities would over time shrink their AUM.

\- Indeed, after peaking in June, the AUM of leveraged memory stock ETFs has shrunk by 34% while that of all leveraged equity ETFs has shrunk by 13% (Figure 3). That said, relative to the market cap of underlying stocks, the decline looks more modest as shown in Figure 4 for both the AUM of leveraged memory stock ETFs and of all equity ETFs. In our mind it will perhaps take another three months or so of volatile range-trading in equities before the leveraged equity ETF AUM ratios to the market cap of underlying stocks return to pre-April levels for either memory stocks or all equity ETFs.

Figure 3: AUM of leveraged equity ETFs In \$bn.  
![](images/5b574dd63e2f9706f52e3d135c93fe620f114258c1c3479cc964f43cd2e37347.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 4: AUM of leveraged equity ETFs as % of the market cap of underlying stocks  
![](images/8ba4d5c7ecea36b73a68a331f6593c0976984ac5535209090e4c129e7d0b8b47.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- This is also because these leveraged equity ETFs saw further inflows in July as shown by the orange bars in Figure 5 and Figure 6, thus prolonging the duration of volatile range-trading needed to shrink/normalize their AUM.

\- Finally, while Figure 4 illustrates why leveraged ETFs have become a bigger source of volatility for memory stocks, as their AUM ratio to the market cap of underlying stocks is three times higher for memory stocks than that of all equity ETFs, the elevated level of the dark blue line in Figure 4 relative to its own history reveals that the leveraged ETF problem as a source of volatility is not only confined to memory stocks but is a broader problem for the overall equity market due to the proliferation of leveraged equity index ETFs.

Figure 5: Flows stemming from equity funds globally In \$bn per month, July MTD.  
![](images/3f98994cc55fd3b9d3915529e980bf665c4bc3783b9870bd6d9526152922a53b.jpg)  
Source: LSEG Lipper, Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 6: Flows stemming from equity funds that invest in Korea In \$bn per month, July MTD.  
![](images/c291ed0ee00f60449c8eefceb3b5554dafab88a7ffa686ae1c3ab0745203c408.jpg)  
Source: LSEG Lipper, Bloomberg Finance L.P., JPM Flows & Liquidity.

\- In the risk parity fund space, our leverage proxy has already normalized as shown in Figure 7, so excessive leverage by risk parity funds should no longer present a significant headwind for equities going forward.

Figure 7: Implied leverage of risk-parity funds  
Ratio of 3-month rolling volatility of risk-parity funds' returns to the volatility of our risk parity strategy benchmark.  
![](images/12f4b2214a35d8eb2bbbd293240e39e86beb08ecc64f65b82f5dc076b405dcad.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.  
Figure 8: Exchange-traded Call Option Buys at Open minus Sells at Open for Customers with less than 10 contracts for options on individual equities

\- In the options space, previous extreme call option buying by retail investors appears to have subsided to a significant extent (Figure 8). As a reminder, our proxy of retail investors' option buying based on OCC data (on exchange-traded call option buying by customers with less than 10 contracts), retreated significantly after peaking on June 5th. The peak on June 5th at close to 14 million contracts had matched the previous peaks seen in October 2025 and November 2021. Following these previous peaks, tech stocks had seen a multi-month correction with the bottom/capitulation in tech stocks coinciding with low readings in this metric of between 2-4 million contracts. In other words, the peaking of this metric since the high of June 5th suggests the retail impulse in the options space is currently subsiding and thus could continue to present a headwind for tech stocks (the preferred habitat of retail investors) going forward if capitulation levels of 2-4 million contacts are eventually reached.

In mn contracts. Last obs is for the week ending 10th July 2026.

![](images/beb8a876cf52d9df57b5671d97fcffc45b7c8a6fe2c94fd92a2b7f8d6cb0bd47.jpg)  
Source: OCC, Bloomberg Finance L.P., JPM Flows & Liquidity.

\- Leverage in margin accounts remains rather elevated and thus significantly more deleveraging is needed in this space for margin accounts to no longer present a significant headwind for equities. As a reminder, for margin accounts we use the NYSE Net Debit balance as a proxy for US individual investor leverage. While in principle it includes both retail and institutional investors, we believe the majority is likely retail investors. In contrast to hedge funds, who can get leverage more easily or cheaply via options and futures, individuals rely more on Federal Reserve Regulation T. This regulation, which governs customer cash accounts and the amount of credit that brokerage firms and dealers may extend to customers for the purchase of securities, stipulates that one can borrow up to 50% of the purchase price of securities that can be purchased on margin. The NYSE Net Debit balance is calculated as the difference between margin debit balance minus the sum of total credit balances (cash accounts credit + margin account credit). This leverage proxy suggests that US individual investor leverage via margin accounts stands at extreme levels by historical standards, with tentative signs of retreating in recent months (Figure 9). This year’s peak matches that seen at the end of 2021 or before then in mid 2018, with both of those previous episodes having been followed by a multi-month correction in equity markets.

Figure 9: Net Debit balances in NYSE margin accounts  
The NYSE margin account Net Debit balance is equal to the margin debit balance minus the sum of total credit balances (cash account credit +margin account credit). The blue line is constructed by the Net Debit balance in \$bn divided by the market capitalisation of the S&P500 Index.  
![](images/ae99b051283178a7f5c5bde9866c9cfffd0bab50b131741669621b15ca408db1.jpg)  
Source: FINRA, NYSE, JPM Flows & Liquidity.

\- In all, the investor deleveraging phase that started in June appears to be still ongoing and we see more room for deleveraging in leveraged equity ETFs, options and margin accounts, thus acting as a headwind for equities going forward. The excessive growth of leveraged equity ETFs can be self correcting: if excess leverage creates higher frequency of VaR shocks, a volatile range-trading in equities would over time shrink their AUM. That said, it will perhaps take another three months or so of volatile range-trading in equities until the leveraged equity ETF AUM ratios to the market cap of underlying stocks return to pre-April levels for either memory stocks or all equity ETFs.

## Once this deleveraging abates, longer-term equity demand/supply dynamics should provide a support

\- With global equities delivering a strong 10% return despite recent volatility, a question has arisen about which flows could support equities during the second half of the year.

\- Starting with L/S hedge funds, the biggest equity hedge fund sector with an AUM of around \$1.4tr, we have typically proxied their equity beta by looking at the futures positions of asset managers and leveraged funds given equity L/S funds use futures as an overlay to achieve their desired beta. These futures positions of asset managers and leveraged funds are in turn proxied by the z-score of net CFTC positions as a % of open interest shown in Figure 10. A neutral z-score of zero is assumed to correspond to a historical average equity beta of 0.5 for Equity L/S hedge funds. We also assume that a very extreme 3 stdevs move in the z-score of CFTC futures positions corresponds to a very extreme 0.5 change in the equity beta. Using these assumptions, we estimate that the beta has declined somewhat from around 0.65 late last year (F&L, Dec 3rd) and is around similar levels currently. This implies modestly positive equity demand of around \$20bn in 2026 to-date. As the above section notes, leverage remains elevated and we see little further increase in the beta into end-2026.

Figure 10: Proxy for Equity L/S positioning from US equity futures by Asset managers and Leveraged funds

CFTC positions in US equity futures by Leveraged funds and Asset managers (as a % of open interest). Rescaling as described in the text. It is an aggregate of the S&P500, Dow Jones, NASDAQ and their Mini futures contracts.

![](images/01cc02aa5e1393dabd8349b10950959b89592b86577ca1065d8e129860caf103.jpg)  
Source: CFTC, Bloomberg Finance L.P., JPM Flows & Liquidity.  
- For momentum-based investors such as CTAs, Figure 11 shows the average z-score of the short and long lookback period momentum signals for the S&P, Nikkei, Eurostoxx

50, FTSE 100 and MSCI EM indices. This z-score sat at around 0.9 at the turn of the year and is currently around 1.0 implying modest net purchases YTD of around \$20bn. For the remainder of the year, we continue to project a z-score of around 1.0 by end-2026, which in turn implies little net buying in 2H26.

## Figure 11: Weighted average of the z scores of equity index momentum signals

Z-score of the momentum signals in our Trend Following Strategy framework shown in Tables A3 and A4 in the Appendix. The line shows the average z-score of the short and long lookback period momentum signals for the S&P 500, Nikkei, EuroStoxx50, FTSE100 and MSCI EM indices. We attach 50% weight on the S&P500 momentum signals and 50% weight on the momentum signals of the remaining four indices combined.

![](images/18ccbad6bb2f4e3f52c6044ff319ca1ccc9d087b7c1f4c0262a19679c5ddd2be.jpg)  
Source: CFTC, Bloomberg Finance L.P., JPM Flows & Liquidity.  
Figure 12: Equity beta of US Balanced Mutual funds and Risk Parity funds

\- What about the universe of risk parity funds? Estimates of its size vary, but a conservative estimate suggests an AUM of around \$150bn. Our calculations (Figure 12) suggest that the risk parity beta to equities has risen to around 0.4 currently, not far from its levels at the time we outlined our outlook for the 2026 equity supply-demand balance. Assuming some mean reversion to its long-run average, this would imply modest negative net demand of around \$20bn in 2H26. For US balanced mutual funds, the beta to equities has declined notably to around 0.49, compared to 0.54 around the turn of the year, implying negative net demand YTD. While this is consistent with rebalancing from equities to HG bonds in end-May, much of the move has taken place in June and coincided wit

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 15 Jul 2026 09:26 PM BST

Disseminated 15 Jul 2026 09:26 PM BST
"""
