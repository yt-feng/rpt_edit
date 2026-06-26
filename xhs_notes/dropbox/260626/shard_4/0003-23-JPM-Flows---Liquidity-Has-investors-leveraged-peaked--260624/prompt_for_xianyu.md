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
# Flows & Liquidity

## Has investors leveraged peaked?

\- After reaching extreme levels earlier this year, there are currently signs of retreat in retail investors' leverage in both options and margin accounts, presenting a potential headwind for tech stocks going forward.

\- Similarly, there are signs of retreat in risk parity fund leverage in recent weeks following a historical high in mid May.

\- Signs of peaking in hedge fund or bank leverage look more tentative.

\- Both corporate and household leverage have been on a declining trend since the pandemic, thus posing little vulnerability to macro shocks.

\- A modest deterioration in the global bond supply-demand balance for 2026 is already priced in by bond markets.

## Cross Asset Fund Flow Monitor

Current level shows the latest percentile of weekly flows; Min is denoted by 0 and Max by 1. As of 17 $^{th}$ June 26.

<table><tr><td>MF &amp; ETF Flows</td><td>Min</td><td>Max</td><td>4 wk avg ($bn)</td><td>2025 avg ($bn)</td></tr><tr><td>All Equities</td><td></td><td></td><td>35.3</td><td>8.1</td></tr><tr><td>All Bonds</td><td></td><td></td><td>17.0</td><td>11.3</td></tr><tr><td>US Equities</td><td></td><td></td><td>35.9</td><td>3.5</td></tr><tr><td>US Bonds</td><td></td><td></td><td>9.3</td><td>4.3</td></tr><tr><td>Non-US Equities</td><td></td><td></td><td>-0.6</td><td>4.6</td></tr><tr><td>Non-US Bonds</td><td></td><td></td><td>7.7</td><td>7.0</td></tr><tr><td>US HG Bonds</td><td></td><td></td><td>2.0</td><td>3.4</td></tr><tr><td>US HY Bonds</td><td></td><td></td><td>0.6</td><td>0.4</td></tr><tr><td>US Lev. Loans *</td><td></td><td></td><td>0.6</td><td>0.0</td></tr><tr><td>US MMFs</td><td></td><td></td><td>0.8</td><td>4.0</td></tr><tr><td>EM Equities</td><td></td><td></td><td>-1.4</td><td>0.9</td></tr><tr><td>EM Bonds</td><td></td><td></td><td>0.81</td><td>0.50</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>-2.1</td><td>-0.1</td></tr><tr><td>China Equities</td><td></td><td></td><td>-1.65</td><td>-0.15</td></tr><tr><td colspan="5">Europe</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>-2.1</td><td>0.9</td></tr><tr><td>Europe Bonds</td><td></td><td></td><td>5.2</td><td>4.3</td></tr><tr><td>Europe HG Bonds</td><td></td><td></td><td>0.1</td><td>0.9</td></tr><tr><td>Europe HY Bonds</td><td></td><td></td><td>0.15</td><td>0.17</td></tr><tr><td>Europe MMFs</td><td></td><td></td><td>6.4</td><td>3.8</td></tr><tr><td>Other Equities</td><td></td><td></td><td>5.39</td><td>3.00</td></tr></table>

Source: Lipper, ICI, Bloomberg Finance L.P. and JPM Flows & Liquidity.
\* US LL historical flows are monthly averages converted to weekly for comparison. China onshore A-share ETFs have been excluded.

## Global Markets Strategy

Nikolaos Panigirtzoglou AC
(44-20) 7134-7815
nikolaos.panigirtzoglou@JPM.com
JPM Securities plc

Mika Inkinen
(44-20) 7742 6565
mika.j.inkinen@JPM.com
JPM Securities plc

## Mayur Yeole

mayur.yeole
(91 22) 6157 3872
mayur.yeole@jpmchase.com
JPM India Private Limited

Krutik P Mehta
(91-22) 6157-5016
krutik.mehta@jpmchase.com
JPM India Private Limited

## Cross Asset Positioning Monitor

Current level shows the latest percentile, Min is denoted by 0 and Max by 1.

<table><tr><td>As of 23-Jun-26</td><td>MIN</td><td>MAX</td><td>Current percentile</td></tr><tr><td>Equities</td><td></td><td></td><td>0.64</td></tr><tr><td>Govt Bonds</td><td></td><td></td><td>0.62</td></tr><tr><td>Credit</td><td></td><td></td><td>0.33</td></tr><tr><td>Dollar</td><td></td><td></td><td>0.73</td></tr><tr><td>Commodities ex Gold</td><td></td><td></td><td>0.38</td></tr><tr><td>Gold</td><td></td><td></td><td>0.43</td></tr><tr><td>Bitcoin</td><td></td><td></td><td>0.52</td></tr><tr><td>EM Equities</td><td></td><td></td><td>0.59</td></tr><tr><td>EM Bonds/FX</td><td></td><td></td><td>0.21</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>0.88</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>0.59</td></tr><tr><td colspan="4">US Equity Sectors:</td></tr><tr><td>Energy</td><td></td><td></td><td>0.62</td></tr><tr><td>Materials</td><td></td><td></td><td>0.59</td></tr><tr><td>Industrials</td><td></td><td></td><td>0.62</td></tr><tr><td>Discretionary</td><td></td><td></td><td>0.60</td></tr><tr><td>Staples</td><td></td><td></td><td>0.13</td></tr><tr><td>Health Care</td><td></td><td></td><td>0.43</td></tr><tr><td>Financials</td><td></td><td></td><td>0.17</td></tr><tr><td>Technology</td><td></td><td></td><td>0.66</td></tr><tr><td>Communication Services</td><td></td><td></td><td>0.36</td></tr><tr><td>Utilities</td><td></td><td></td><td>0.44</td></tr></table>

Cross Asset Positioning Monitor aggregates across the various position indicators of Appendix ranging from positioning proxies across various futures contracts, momentum signals as proxies of how trend-following funds/CTAs are positioned, mutual fund betas as proxies of how mutual fund managers are positioned, risk parity fund positioning and leverage proxies, hedge fund betas as proxies of how hedge fund managers are positioned, client surveys, asset allocation estimates of private non-bank investors at global level, short interest indicators, etc.

\- We argued in our last publication that the rising trend in semiconductor stock volatility coupled with elevated semiconductor exposures in investor positioning are raising the risk of more frequent semiconductor “VaR shocks” from here. One manifestation of elevated investor positioning is leverage. How high is investors’ leverage at the moment? And do we see signs of deleveraging?

\- To answer these questions, we look at different forms of leverage across investor types. Starting with retail investors, we examine three main forms of their leverage: their flows into leveraged ETFs, their buying of options and their borrowing via margin accounts.

\- We explained previously in our publication the increasing importance of the rebalancing flows emanating from leveraged ETFs (“A \$100bn rebalancing flow boosted April’s equity rally”, May 6 $^{th}$ 2026). These leveraged ETFs, with an AUM of \$247bn globally, typically have a tech focus and have thus acted as a big amplification force for tech stocks in recent months, in particular in places like Korea. Indeed, Figure 1 and Figure 2 show how large these leveraged ETF rebalancing flows were in March, April and May. And by looking at the capital flow into leveraged equity ETFs (orange bars in Figure 1 and Figure 2), there is little evidence of retail investors retreating from these leveraged ETFs beyond the typical profit taking seen in strongly up months.

Figure 1: Flows stemming from equity funds globally In \$bn per month  
![](images/8d12fe76155a2838273c37618ee61fbfd85628168c33819dccdd9a368739c463.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 2: Flows stemming from equity funds that invest in Korea In \$bn per month.  
![](images/08db0563c47bc4a10a209500b80cfd120dceaa15758cbc628d6a31cc8eddff48.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- Where retail investors' leverage appears to be retreating is in options and margin accounts. In options, our proxy of retail investors' option buying based on OCC data (on exchange-traded call option buying by customers with less than 10 contracts), shows signs of retreat after peaking on June $5^{\text{th}}$ (Figure 3). The peak on June $5^{\text{th}}$ at close to 14 million contracts matches the previous peaks seen in October 2025 and November 2021. Following these previous peaks, tech stocks saw a multi-month correction with the bottom/capitulation in tech stocks coinciding with low readings in this metric of between 2-4 million contracts. In other words, the peaking of this metric since the high of June $5^{\text{th}}$ suggests the retail impulse in the options space is currently subsiding and thus presents a potential headwind for tech stocks (the preferred habitat of retail investors) going forward.

Figure 3: Exchange-traded Call Option Buys at Open minus Sells at Open for Customers with less than 10 contracts for options on individual equities  
In mn contracts. Last obs is for the week ending 19 $^{th}$ June 2026.  
![](images/408c3b2c5c50c3b5b62685e7c6e3271124bf543bf0ad8e3598f53e442555aa0d.jpg)  
Source: OCC, JPM Flows & Liquidity.

\- For margin accounts, we typically use the NYSE Net Debit balance as a proxy for US individual investor leverage. While in principle it includes both retail and institutional investors, we believe the majority is likely retail investors. In contrast to hedge funds, who can get leverage more easily or cheaply via options and futures, individuals rely more on Federal Reserve Regulation T. This regulation, which governs customer cash accounts and the amount of credit that brokerage firms and dealers may extend to customers for the purchase of securities, stipulates that one can borrow up to 50% of the purchase price of securities that can be purchased on margin. The NYSE Net Debit balance is calculated as the difference between margin debit balance minus the sum of total credit balances (cash accounts credit + margin account credit). This leverage proxy suggests US individual investor leverage via margin accounts stands at extreme levels by historical standards with tentative signs of retreating in recent months (Figure 4). This year’s peak matches that seen at the end of 2021 or before then in mid 2018, with both of those previous episodes having been followed by multi-month correction in equity markets presenting a potential headwind.

Figure 4: Net Debit balances in NYSE margin accounts

The NYSE margin account Net Debit balance is equal to the margin debit balance minus the sum of total credit balances (cash account credit +margin account credit). The blue line is constructed by the Net Debit balance in \$bn divided by the market capitalisation of the S&P500 Index.

![](images/b6e9ba3b9b4ad17a5bc7551b6bab61d1c44e0b6f1ca0b4e9580d409ae0673c6c.jpg)  
Source: FINRA, NYSE, JPM Flows & Liquidity.

\- In other words, after reaching extreme levels earlier this year, there are currently signs of retreat in retail investors' leverage in both options and margin accounts.

\- What about hedge fund leverage? Figure 5 illustrates our proxy for aggregate hedge fund leverage, based on the ratio of hedge fund return volatility to the volatility of underlying asset returns, the rationale being that the higher the leverage the higher the volatility of hedge funds vs the volatility of the underlying assets. To construct our hedge fund leverage proxy, we divide hedge fund index return volatility by asset return volatility for each category. We use S&P 500 returns as a proxy for Equity Long/Short, Equity Short, and Equity Neutral funds and global bond index USD-hedged returns for Macro and Fixed-Income Arbitrage funds. The high yield corporate bond index, our proxy for hedge fund leverage, has been drifting higher since 2023 with March 2026 marking a potential local peak. While hedge fund leverage does not look particularly high by historical standards, especially compared to pre-2008 financial crisis norms, any further signs of peaking from here could add fuel to the idea that the rising trend in hedge fund leverage since 2023 is behind us.

## Figure 5: Estimated HF Leverage

Our measure of HF leverage is a weighted average of the estimated leverage for five HFR hedge fund styles: Equity long/short, Equity short, Macro, Fixed Income arbitrage, Convertible arbitrage and Emerging Markets, Equity neutral and Eventdriven/ Distressed debt. For each style, we divide the hedge fund index return volatility by asset return volatility, which we proxy by S&P 500 returns for Equity long/ short, Equity short and Equity neutral, Global bond index USD hedged returns for Macro and Fixed-Income arbitrage, high-yield returns for Convertible arbitrage and Event driven/Distressed debt and EMBIG returns for Emerging Markets. Last obs is Apr'26 for Pivotal Path, HFR & CS.

![](images/be5fe4d852a6813bfb397d1660a67a8d810aa7cab358515a7cdba818681b3f17.jpg)  
Source: Pivotal Path, CS, HFR, JPM.

\- In risk parity fund space, there are more clear signs of peaking in their leverage, with our implied leverage proxy in Figure 6retreating in recent weeks after reaching its highest level in over a decade mid-May.

Figure 6: Implied leverage of risk-parity funds  
Ratio of 3-month rolling volatility of risk-parity funds' returns to the volatility of our risk parity strategy benchmark.  
![](images/2bc05d0bd2faabb5daa53b5085072efac09b5bbc9337190daed2115158008b5e.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.  
Figure 7: Estimated US bank leverage

\- Similar to hedge funds, banks have also been raising their leverage in recent years due to deregulation. Regulations requiring banks to hold more capital and restrictions on proprietary trading by commercial banks meant bank leverage had declined after the financial crisis of 2008 and remained relatively contained until 2023. But a renewed deregulation drive by the US administration induced banks to increase their leverage. Despite the past year's increase, our bank leverage proxy remains well below pre-financial crisis norms with tentative signs of peaking (Figure 7). The bank leverage proxy in Figure 7 is proxied by the ratio of the volatility of bank trading profits over the volatility of their assets. Again, the rationale being that the higher the leverage the higher the volatility of bank trading profits vs the volatility of the underlying assets.

In the case of US banks, we proxy their leverage by the ratio of the volatility of their trading profits over the volatility of their assets. Quarterly data on the trading profits of US commercial banks are available from the Office of the Comptroller of the Currency (OCC).

![](images/30f1d7aff1767765f068776d50751c6f4725a5d48aa4d614101a912e5a691677.jpg)  
Source: OCC, Bloomberg Finance L.P., JPM Flows & Liquidity.

\- What about economic leverage? Our broad metrics of economic leverage in Figure 8 suggests that, as economies have recovered from the pandemic shock, both corporate and household leverage have been on a declining trend. A relatively contained backdrop in terms of leverage, in turn, helps to reduce macro vulnerability to shocks. Moreover, as we have noted previously, despite the sharp rise in interest rates since early 2022, the net interest paid by non-financial corporates as a proportion of cash flows generated has declined markedly for US non-financial corporates (Figure 9), as the interest rates on short-term assets re-priced faster than the interest rates on their liabilities. Taken together, Figure 8 and Figure 9 suggest that neither corporate nor household leverage appear to be posing a vulnerability to macro shocks.

Figure 8: Stock of non-financial corporate sector & household debt as % of nominal GDP for Global GDP ex-China Quarterly data, last obs. is Q4 2025.  
![](images/02215c53902c26d5220430e86c868d12363420a455bdf51d9109e1afca1e24e7.jpg)  
Source: National central banks, BIS, JPM Flows & Liquidity.

\- In all, after reaching extreme levels earlier this year, there are currently signs of retreat in retail investors' leverage in both options and margin accounts, thus presenting a potential headwind for tech stocks tech stocks going forward. Similarly, there are signs of retreat in risk parity fund leverage in recent weeks following a historical high in mid May. Signs of peaking in hedge fund or bank leverage look more tentative. Both corporate and household leverage have been on a declining trend since the pandemic, thus posing little vulnerability to macro shocks.

Figure 9: Net interest paid as % of non-financial corporate cash flows from operations  
Till Q1'26 for US and G4 ex US  
![](images/9ba43ec3857356e494bce2f8e140

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 24 Jun 2026 11:12 PM BST

Disseminated 24 Jun 2026 11:12 PM BST
"""
