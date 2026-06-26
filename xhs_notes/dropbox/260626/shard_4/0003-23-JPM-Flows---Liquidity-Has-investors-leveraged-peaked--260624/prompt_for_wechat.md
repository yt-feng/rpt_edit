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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
![](images/9ba43ec3857356e494bce2f8e1402e14fdecca1f837e1035c7fc014c9feb0be1.jpg)  
Source: Federal Reserve, ECB, BoJ, BoE, JPM Flows & Liquidity.

## A modest deterioration in the global bond supply-demand balance for 2026 is already priced in by bond markets

\- With the recent release of the US flow of funds for 1Q26, quarterly worldwide fund flow data from the ICI covering 1Q26, as well as updated supply estimates from our colleagues' mid-year outlooks, we update our estimates for the global bond supply-demand balance (F&L, Nov 26 $^{th}$ , 2025).

\- Starting with demand, net bond demand by G4 central banks was broadly flat in 2025 vs. 2024 at just under -\$1.3tr. With the Fed continuing to reinvest its maturing Treasuries across the curve, while MBS run-offs are reinvested in T-bills, this implies an ongoing modest negative duration impulse from the Fed (given we exclude T-bills from our global bond supply-demand analysis). For the ECB, both APP and PEPP holdings continue to run-off, and the BoE continues its QT via ongoing modest active sales as well as maturing bonds. And the BoJ has gradually accelerated its QT, and looks set to reduce its JGB holdings by around JPY48tr over the next 12 months. Net of these influences, we continue to G4 central bank net purchases at around -\$1.2tr for 2026, or an improvement in demand of around \$0.1tr for 2026 vs. 2025.

Figure 10: Net QE by G4 central banks  
![](images/d1acf64617d4ee9be14b40267fdf5c906216514db02d335f1a9a0012d864a09a.jpg)  
Source: Federal Reserve, ECB, BoE, BoJ, JPM Flows & Liquidity.

\- What about retail investors? In our 2026 global bond supply-demand analysis, we used a forecasting model that forecasts current year annual bond flows as a % of AUM as a function of the previous year's bond flow and bond returns. For this year, based on bond flows and returns in 2025, the model forecasted around \$1.1tr of inflows into bond funds, which would have represented around a \$0.2tr deterioration in bond demand from 2026 vs. 2025.

When we look at year-to-date inflows into bond funds, including quarterly reporting funds for 1Q and monthly or higher frequency for 2Q and add to this the average additional inflows into quarterly reporting funds since the start of 2025, this suggests that inflows into bond funds are, if anything, running at an annualized pace that is modestly stronger than the 2025 and 2024 pace of around \$1.4tr. This would imply a modest improvement in in bond demand from retail investors in 2026 vs. 2025 of around \$0.1tr.

\- That said, as we have argued previously, the duration impulse of this support from retail investors in 2025 to-date has been fading. Figure 11 depicts this cumulative duration impulse of net flows into bond ETFs, and shows 

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 24 Jun 2026 11:12 PM BST

Disseminated 24 Jun 2026 11:12 PM BST
"""
