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
# Retail Radar

# Jul 8 — Split-the-Dip as Momentum Cools

## Retail Trading Activity Overview

\- Retail buying strengthened last week (82%ile), driven by renewed demand for ETFs (71%ile) and continued robust activity in Single Stocks (86%ile). Sector flows were little changed, with Tech remaining a favorite amid the recent sell-off and buying-the-dip activity concentrated in retail's preferred names (e.g. Memory leaders). Within ETFs, allocation was stable week-on-week, with continued scaling back in SOXL (-1.9z) offset by ongoing buying in SMH (2.6z).

\- As the US military launched a new round of strikes against Iran and oil rebounded above \$80, retail buying in Energy stocks climbed to their 92%ile on Wednesday. However, oil ETFs only saw moderate demand, e.g. BNO (1.0z) and USO (0.2z), while short oil positioning (SCO) was trimmed again this week (-1.5z, Figure 7).

\- The Momentum factor has been losing steam this month, with Semis leading the slowdown—our proprietary Momentum crowding metric has declined from \~100%ile to 98.6%ile, Figure 4. Retail activity in the High Momentum names that drove July’s pullback split into two camps: buying-the-dip in this year’s favorites SNDK (2.3z, although the stock experienced outflows on Wednesday) and MU (0.3z), while selling the weakness in AMAT (-3.4z), WDC (-3.0z), KLAC (-2.9z), MRVL (-1.0z) and LRCX (-2.3z). AVGO’s announcement that it is expanding its partnership with AAPL through 2031 did little to attract retail flows (AVGO: 0.0z, AAPL: 0.6z, see Macro & Fundamental Stories).

\- Aside from June 18–23, retail investors have been consistent net buyers of SpaceX, Figure 6. Activity was heaviest during the first three sessions post-IPO, when the stock rallied \~50%. On Tuesday, our analysts initiated coverage of SPCX with an Overweight Rating at Dec-27 PT of \$225 (+51% upside). The thesis centers on the company's launch capabilities and the rapid reusability of Starship. They expect Starship launches to scale from a handful in 2026 to roughly 5,000 in 2031, enabling SpaceX to build 75 GW of orbital compute. The team forecasts a 91% revenue CAGR over 2025 to 2030, alongside meaningful margin expansion as the business mix shifts from Connectivity to AI, first terrestrial and then orbital. SpaceX's NASDAQ debut saw a record \~20% allocation to retail investors, versus a typical level closer to 5%.

\- Power generation equipment stocks like GEV (-1.3z on 7/1, Figure 17), CAT (-1.5z, Figure 19), and CMI (0.6z, Figure 21) sold off \~7% on July 1 $^{st}$ following the downgrade of a German-based competitor, in a broad-based selloff that suggests that peak AI-spend concerns are still weighing on valuation sentiment across adjacent, upstream AI beneficiaries—see Macro & Fundamental Stories.

## Equity Strategy and Quantitative Research

Arun Jain AC
(1-212) 622-9454
arun.p.jain@JPM.com
JPM Securities LLC

Shizuka Suga, CFA AC
(1-212) 622-2134
shizuka.suga@JPM.com
JPM Securities LLC

Ana Pous Avila
(1-212) 622-0496
ana.pousavila@JPM.com
JPM Securities LLC

William Matheson
(1-212) 622-9538
william.matheson@jpmchase.com
JPM Securities LLC

Khuram Chaudhry
(44-20) 7134-6297
khuram.chaudhry@JPM.com
JPM Securities plc

Bhupinder Singh AC
(1-212) 622-9812
bhupinder.singh@JPM.com
JPM Securities LLC

(1-212) 622-3601
dubravko.lakos-bujas@JPM.com
JPM Securities LLC

## Past Issues:

7/1 - Same Playbook, Buying the Dip
6/24 - Remembers the Dip, MU Serves Right
6/17 - Tech Craze Spillover to Communications
6/10 - Tech Selling amidst Drawdown, World Cup
6/3 - MEME Earnings, Trading around IPOs
5/27 - Theme Stack: AI, Memory, Space, Quantum
5/13 - Software vs Semis Positioning
5/6 - Memory and AI, the Catch-Up Trade
4/29 - Peak Earnings, Peak Mag-7
4/22 - Towards a MEME Revival?
4/15 - Back to Average
4/8 - Not Buying Despite the Ceasefire
4/1 - In Defensive Mode
3/25 - Selling Rips
3/18 - From FOMO to FOHO: Fear Of Higher Oil
3/11 - Buying Oil, Selling Energy
3/4 - Cautiously Optimistic
2/25 - Balanced Optimism
2/18 - AI Software Averaging Down

## Retail Trading Activity in Numbers for the Week: Jul 1 to Jul 8

\- Retail flows were \$8.9B this week, above the 12-month avg of \$6.8B/week. Retail investors continued to favor ETFs (+\$6.2B) over Single Stocks (+\$2.7B).

\- Outside of Broad Based Large Cap Equity ETFs (+\$1.9B), retail ETF buying was influenced by Fixed Income — Multi Sector (+\$337M), Corporates Investment Grade (+\$235M), Equity Style Dividend (+\$233M), and Equity Broad Based Multi Cap (+\$222M).

\- This week, in line with prior weeks, retail investors continued to buy Mag 7, AI datacenters and electrification (JPAMAIDE), Top 30 AI/Datacenter Beneficiaries, AI Software/Product/Monetization, Growth, along with OBBBA Immediate Expensing Beneficiaries, see Figure 8.

\- Activity in Mag7 this week: Retail investors bought NVDA (+\$498M), TSLA (+\$432M), MSFT (+\$308M), GOOGL/GOOG (+\$223M), META (+\$61M), AMZN (+\$43M), and sold AAPL (-\$18M).

\- Outside of Mag7, retail investors favored Tech (+\$712M), Communications (+\$617M) and were net sellers of Cons. Disc. (-\$189M) and Financials (-\$135M).

\- Top 5 retail stocks last week: SPCX (+\$554M), NVDA (+\$498M), SNDK (+\$459M, 2.3z), TSLA (+\$432M), MSFT (+\$308M). Bottom 5 retail stocks: AMAT (-\$78M, -3.4z), PANW (-\$75M, -2.4z), MRVL (-\$66M), WDC (-\$64M, -3.0z), KLAC (-\$52M, -2.9z).

\- In options, retail share is at highs, Figure 51. The most traded options were in the following names, echoing previous weeks: TSLA, MU, NVDA, META, AMZN, SNDK, AMD, AAPL, MSFT and SPCX. For the most bought/sold delta and gamma names, see Retail Activity in Options. Also see Retail Investors Options Activity by Sectors.

\- Futures Activity (Non Retail): Over the past week, Futures traders net sold \~\$2.2B, primarily driven by net sales in RTY (\~\$5.2B) and partially offset by net buys in ES (\~\$3.0B).

2/11 - Positioning around Dislocations  
2/4 - Softening Sentiment, Software vs Semis  
1/28 - Earnings, Intl Equities, Precious Metals  
1/21 - Unfazed through Vol Shock  
1/14 - The January Effect?  
1/7 - December Spree and a good start to January  
12/10 - 2025 Retail Mania  
12/3 - The Retail AI Trade  
11/26 - Weekly Highlights  
11/19 - 2025 Retail Mania: Dip-buying in AI  
11/12 - Bullion to Silicon: AI Gold Rush Resumes  
11/5 - Skipping the Dip, Earnings Stock Picking  
10/29 - Reaching Peak-Earnings, AI, FOMC  
10/22 - Sold GLD, onto New Memes and Earnings  
10/15 - Trading around Tariffs, AI and Earnings  
10/8 - Back after Summer Break  
10/1 - Back to Stocks, Thematic ETFs, GLD Rush  
9/24 - Precious Metals, Cyclicals and Domestic  
9/17 - FOMC, Herding in OPEN and GRAB

We thank G. K. Kiruthik Srinivaas and Aditya Mulye of JPM India Private Limited for their significant contributions to this report.

Figure 1: Retail Imbalance in SPCX
As of July 8 $^{th}$  
![](images/9032a68bcd134aa4fe4457c1658e52678c29a9049cf86ecc8562025792cf8a55.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 2: Cumulative Retail Imbalance in SPCX
As of July 8 $^{th}$  
![](images/e043a64d673183ec74d8ae28608980bcce4273a588a7b47c3737abcab3e2bbe6.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 3: Momentum Crowding off its recent highs...
As of Jul 7 $^{th}$  
![](images/5139f70611480ff55bfb7b90bd3023545707e6aa5757b1b01ee4983776c9a876.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 4: ... recently

![](images/163889c080c880614f15a18b11d05c7c76f83c7166a54776af9c68238391d408.jpg)  
Source: JPM Equity Strategy & Quantitative Research

-2000 - 08-Jan 15-Jan 23-Jan 30-Jan 06-Feb 13-Feb 23-Feb 02-Mar 09-Mar 16-Mar 23-Mar 30-Mar 07-Apr 14-Apr 21-Apr 28-Apr 05-May 12-May 19-May 27-May 03-Jun 10-Jun 17-Jun 25-Jun 02-Jul

Figure 5: Retail Investor Daily Purchases by Stocks and ETFs \$M, as of Jul 8 $^{th}$  
![](images/d05d95b00618384e6508af22969a3540f076719d3f971531e693c3b89df451f2.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 6: Retail Imbalance in SCO
As of July 8 $^{th}$  
![](images/9f54a010bc40b940d0ddbd73221233e1ab2908f749712c4a68443231d7b16b43.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 7: Cumulative Retail Imbalance in SCO As of July $8^{\text{th}}$  
![](images/4b31e681fa7fba610a0a797bc9acee4cda73b594d03e2a88dffb283a677cc7ac.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

## Retail Cash Activity – Overview

Figure 8: Retail Single Stock Activity by Themes

<table><tr><td colspan="2">Thematic Baskets</td><td colspan="3">Δ in Retail Turnover ($Bn)</td></tr><tr><td>Basket</td><td>Index</td><td>Week Ago</td><td>Month Ago</td><td>YTD</td></tr><tr><td>Magnificent 7</td><td>Mag7</td><td>0.99</td><td>3.47</td><td>32.82</td></tr><tr><td>AI/Datacenter/Electrification</td><td>JPAMAIDE</td><td>0.96</td><td>6.42</td><td>41.64</td></tr><tr><td>S&amp;P 500 Top 30 AI/Datacenter Beneficiaries</td><td>JPRAID30</td><td>0.89</td><td>6.52</td><td>40.94</td></tr><tr><td>AI Software/Product/Monetization</td><td>JPAMAISO</td><td>0.86</td><td>3.42</td><td>25.77</td></tr><tr><td>Growth</td><td>JPAMGROW</td><td>0.70</td><td>5.57</td><td>39.94</td></tr><tr><td>OBBBA Immediate Expensing Beneficiaries</td><td>JPGTIEXB</td><td>0.36</td><td>3.90</td><td>19.62</td></tr><tr><td>Domestic</td><td>JPAMDOME</td><td>-0.03</td><td>-0.53</td><td>-0.29</td></tr><tr><td>Trump Deregulation Agenda</td><td>JPRGDREG</td><td>-0.04</td><td>-0.56</td><td>-4.10</td></tr><tr><td>Inflation Outperformers</td><td>JPAMINOP</td><td>-0.06</td><td>-0.89</td><td>-3.36</td></tr><tr><td>High Beta Speculative Growth</td><td>JPAMHBSG</td><td>-0.08</td><td>1.48</td><td>7.46</td></tr><tr><td>CHIPS Act Beneficiaries Basket</td><td>JPAMCHIP</td><td>-0.35</td><td>2.06</td><td>4.44</td></tr><tr><td>De-Globalization/Reshoring Beneficiaries</td><td>JPAMDGLO</td><td>-0.37</td><td>2.03</td><td>4.26</td></tr></table>

Figure 9: Retail Cumulative Purchases in Mag 7 + PLTR (\$B)  
![](images/df471e6dcdfb94a4839b290e3b25d904e6a6f35bc6a96db02e0e75ed0905c55d.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Source: JPM Equity Strategy & Quantitative Research. See report, report, and report for details on above baskets. Note: JPM does not provide research coverage of the baskets mentioned here, and investors should not expect continuous analysis or additional reports relating to them.

Figure 10: Retail Single Stock Activity by Sector (\$B)  
Activity is dominated by Tech and Cons. Disc. Note: The last weekly data point includes a holiday, Jul 3.  
![](images/ba131d64d4f68692209d0fdc58bcd47d743266d00a0521aac039cc17133ac20a.jpg)  
Source: JPM Equity Strategy & Quantitative Research  
Figure 11: Retail ETF Activity by Themes  
Buying / Selling of ETFs aggregated by themes, in \$B. Note: The last weekly data point includes a holiday, Jul 3.

![](images/55539ddbc477e4065952ff195313ea61576c3506ca4d834c7295b279fb5b8187.jpg)  
Source: JPM Equity Strategy & Quantitative Research

## Single Stock Stories with Elevated Retail Activity

Hedge Funds vs. Retail: High Short Interest Meme Stocks

\- CUPR (\$1.2M bought last week, 0.9z, Figure 14): The company filed a registration statement on July 7 for a proposed underwritten public offering of its Class A ordinary shares. Retail interest has been elevated since June 2026, with net purchases totaling \$10M, alongside rising short interest of \~30\% of float, up 28\% since late May 2026.

\- HIVE (\$1.1M sold last week, -0.4z, Figure 15): The stock fell 6% on July 7, 2026, and the company recently completed a \$130M private offering of 0% exchangeable senior notes through a subsidiary, including the full exercise of the initial purchasers' option for additional notes. The stock has been on retail investors' radar since May 2025, with net purchases totaling \$60M, alongside short interest of \~18%, up 8% since May 2026.

\- SERV (\$0.2M sold last week, -0.2z, Figure 16): The company recently implemented changes to its board of directors, while retail interest has remained persistent with net purchases of \$30M since September 2025. These developments have occurred amid elevated short interest of \~32% of the float, up 10% since October 2025.

## Macro & Fundamental Stories

\- Our analysts initiated coverage of SpaceX with an Overweight Rating at Dec-27 PT of \$225 (+51% upside). They cite the company's launch capabilities and the rapid reusability of Starship as key pillars of the thesis, with Starship launches expected to ramp from a handful in 2026 to roughly 5,000 in 2031, enabling SpaceX to build 75 GW of orbital compute. The team forecasts a 91% revenue CAGR over 2025 to 2030, alongside meaningful margin expansion as the business mix shifts from Connectivity to AI, first terrestrial and then orbital. SpaceX debuted on NASDAQ on June 12, allocating a record 20% of shares to retail investors versus a typical level closer to 5%. Retail demand supported strong first-week trading, with purchases totaling \$1.1B. The stock is down -26% from its July 16 peak and is up +11% versus its IPO level, with retail investors net sellers/buyers over the past seven days (\$529.6M bought last week, 0.3z).

\- Power generation equipment stocks like GE Vernova (GEV, 8M sold on 7/1, -1.3z, Figure 17), Caterpillar (CAT, 12M sold on 7/1, -1.5z, Figure 19), and Cummins (CMI, 2M bought on 7/1, 0.6z, Figure 21) were down \~7% on July 1 $^{st}$ following the downgrade of a German-based competitor. The broad-based selloff suggests that concerns about peak AI-related spending continue to weigh on valuation sentiment across adjacent, upstream AI beneficiaries.

\- Semiconductor stocks are down -8% in the last week (vs. S&P 500 at -0.3%) led by Teradyne (TER, \$9M sold last week, -0.9z, Figure 23), Kla Corp (KLAC, \$52.7M sold last week, -2.9z, Figure 25), Lam Research (LRCX, \$16M sold last week, -1.0z, Figure 27), Intel (INTC, \$24.6M bought last week, -0.1z, Figure 29), Marvell Technology (MRVL, \$47.5M sold last week, -0.7z, Figure 31), Applied Materials (AMAT, \$69.7M sold last week, -3.0z, Figure 33) and Skyworks Solutions (SWKS, \$2.3M sold last week, -0.5z, Figure 35). Broadcom (AVGO, \$87.3M bought last week, 0.3z, Figure 37) and Qualcomm (QCOM, \$9.7M bought last week, 0.6z, Figure 39) were the only stocks which saw marked positive performance at +4% and +1%, respectively, with the former announcing an expansion of their partnership with Apple (AAPL, \$48.3M sold on 7/6, -0.8z, Figure 41) through 2031 (link).

\- Memory stocks, namely Micron (MU, \$261.4M bought last week, 0.7z, Figure 43) and Western Digital (WDC, \$54.9M sold last week, -2.6z, Figure 45), are down -17% over the past week. Notably, however, WSTS May industry data was published with industry revenue on pace to exceed \$1.5T in 2026, underpinned by improving cyclical trends, AI spending momentum, and favorable pricing dynamics (link).

## Meme Battlegrounds: Retail Buying vs. Hedge Fund Shorting

In this section, we are flagging a few stocks that are heavily mentioned on Social Media and have high Retail buying as well as high Hedge fund Shorting. These stocks may experience unexpected flows in case of increased activity.

## Social Media Screen and Retail Activity

Figure 12: Most Hyped Stocks on Social Media  
Top 20 names based on social media traction over the week (Social Interest), Scaled by market cap

<table><tr><td>Ticker</td><td>Name</td><td>Mkt Cap ($B)</td><td>Social Interest Score</td><td>Median Short Interest (% float)</td><td>Extreme Imbalance 1D Z</td><td>Date of Imbalance</td></tr><tr><td>TLRY</td><td>Tilray Brands Inc</td><td>0.5</td><td>42.6</td><td>14.3%</td><td>0.2</td><td>06-Jul</td></tr><tr><td>MSTR</td><td>Strategy Inc</td><td>34.1</td><td>41.3</td><td>12.1%</td><td>1.2</td><td>02-Jul</td><

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 08 Jul 2026 10:18 PM EDT

Disseminated 08 Jul 2026 10:18 PM EDT
"""
