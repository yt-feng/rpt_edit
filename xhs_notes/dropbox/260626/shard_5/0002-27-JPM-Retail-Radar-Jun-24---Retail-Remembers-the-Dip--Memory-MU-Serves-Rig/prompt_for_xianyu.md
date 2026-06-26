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
# JPM

# Retail Radar

# Jun 24 - Retail Remembers the Dip, Memory (MU) Serves Right

## Retail Trading Activity Overview

\- This week's global Tech rout did little to deter retail participation; while activity eased from last week's elevated levels, Figure 11, it remained around the 1y median, with resilience in single-stocks (65%ile) offsetting softer ETF inflows (25%ile). The sell-off—led by Korea and semis—created another opportunity for retail investors to add to their Memory exposure, with buying concentrated in MU and SNDK, particularly on weakness this week.

\- Within ETFs, Korea (e.g. EWY and KORU) saw mixed flows (-4.2z and +2.7z, resp.). Communication ETFs Imbalance reached a 15-month low, Figure 9, driven by XLC (-4.2z, Figure 10). GLD has been effectively ignored by retail in recent months, but prices plunging below 4000 on Wednesday was a catalyst for stronger outflows (-1.9z day).

—even as near-term catalysts kept volatility elevated. In Mag 7 positioning, our derivatives analysts recommend selling 2-month out of the money puts on GOOGL and MSFT as a target-buy strategy, given both names are down \~11% over the past month, despite the Nasdaq making new highs and fundamentals remaining constructive, report.

\- In Memory specifically, demand was strong in MU on Wednesday (8.3z, Figure 2), ahead of its strong earnings announcement that prompted the company's shares to soar over $14\%$ in after-hours trading. SNDK also continued to see strong inflows over the week (2.4z, Figure 21), although there was minimal activity on Wednesday (-0.5z).

\- Within options, retail share is at highs, Figure 46, driven by a spike in option volumes in the Communication Sector, Figure 3, which came at the expense of most other sectors, including Tech, Figure 4. The top names by contracts traded were TSLA, NVDA, AAPL, and AMZN.

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

Arda Sebuktekin
(1-212) 270-4397
arda.sebuktekin@jpmchase.com
JPM Securities LLC

Khuram Chaudhry
(44-20) 7134-6297
khuram.chaudhry@JPM.com
JPM Securities plc

Bhupinder Singh AC
(1-212) 622-9812
bhupinder.singh@JPM.com
JPM Securities LLC

Dubravko Lakos-Bujas AC
(1-212) 622-3601
dubravko.lakos-bujas@JPM.com
JPM Securities LLC

We thank G. K. Kiruthik Srinivaas and Aditya Mulye of JPM India Private Limited for their significant contributions to this report.

## Past Issues:

6/17 - Tech Craze Spillover to Communications
6/10 - Tech Selling amidst Drawdown, World Cup Theme Yet to Kick In
6/3 - MEME Earnings, Trading around IPOs
5/27 - Theme Stack: AI, Memory, Space, Quantum
5/13 - Software vs Semis Positioning

## Retail Trading Activity in Numbers for the Week: Jun 18 to Jun 24

\- Retail flows were \$6.3B this week, just below the 12-month avg of \$6.7B/week. Retail investors continued to favor ETFs (+\$4.8B) over Single Stocks (+\$1.5B).

\- Outside of Broad Based Large Cap Equity ETFs (+\$1.4B), retail ETF buying was influenced by Fixed Income — Multi Sector (+\$205M), Equity Style Dividend (+\$198M), Equity Style Multi Cap (+194M), and International Equity EAFE (+\$178M). In contrast, they sold Precious Metals (-\$85M, -1.3z) and Equity Sector — Energy (-\$55M, -1.4z).

\- This week, in line with prior weeks, retail investors continued to buy Top 30 AI/ Datacenter Beneficiaries, Growth, AI datacenters and electrification (JPAMAIDE), and Mag7, along with US Companies with High Direct China Exposure, see Figure 12.

\- Activity in Mag7 this week: Retail investors bought: NVDA (+\$470M), TSLA (+\$425M), MSFT (+\$256M), GOOGL/GOOG (+\$107M), META (+\$102M), AMZN (+\$32M), and were flat AAPL (-\$0M).

\- Outside of Mag7, retail investors favored Tech (+\$1.4B) and Staples (+\$109M) and were net sellers of Communications (-\$499M), Materials (-\$192M), Consumer Disc. (-\$158M), and Energy (-\$154M).

\- Top 5 retail stocks last week: MU (+\$868M, 5.4z), NVDA (+\$470M), TSLA (+\$425M), SNDK (+\$354M, 2.4z), MSFT (+\$256M). Bottom 5 retail stocks: ORCL (-\$76M, -1.5z), HOOD (-\$68M, -1.3z), AMD (-\$58M), AZO (-\$41M, -2.8z).

\- In options, retail share is at highs, Figure 46, driven by a spike in option volumes in the Communication Sector, Figure 49. The most traded options were in the following names, echoing previous weeks: TSLA, MU, NVDA, AMZN, META, SNDK, AMD, INTC and GOOGL/GOOG. For the most bought/sold delta and gamma names, see Retail Activity in Options. Also see Retail Investors Options Activity by Sectors.

\- Futures Activity (Non Retail): Over the past week, Futures traders net sold \~\$3.6B, primarily driven by net selling in ES (\~\$0.5B) and NQ (\~\$4B) partially offset by net buys in RTY (\~\$1B).

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

Figure 1: Retail Imbalance in Memory Stocks (\$B) As of 24 $^{th}$ June  
![](images/035bdc4d8fcc41c16d8ef64d610eaeb8928a76a0ed82275a1c4549d73dbc21d3.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 2: Retail Imbalance in MU
As of 24 $^{th}$ June  
![](images/860429ec8e385252b894a4768698356e42060345b56bcaae6ac86f802467d822.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 3: Retail Options Volume (Calls and Puts), Communication Services  
![](images/d6582376c858caddf91c8308c965a2f35d28c6353d8dfb0a0f78330eddc7de54.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 4: Retail Options Volume (Calls and Puts), Information Technology  
![](images/a1943783049a077f3a3ab41099ac427f737054e89c618dbd44202b3b89269d8f.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 5: Retail Imbalance in EWY
As of June 24 $^{th}$  
![](images/a60ce365121bb6c0db5dc2f77568cba30eb006d123e2208b63118aa471f81947.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 6: Cumulative Retail Imbalance in EWY
As of June 24 $^{th}$  
![](images/39082e976a0642284bad5cc58744e6b0d0f931594f0310537d08847a10797723.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 7: Retail Imbalance in KORU
As of June 24 $^{th}$  
![](images/d318e6b5becb50cae71277c5245feacb401e6baa9ed702b7bced218fb8b0d716.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners  
Figure 9: Communication ETFs Imbalance at its lows...

Figure 8: Cumulative Retail Imbalance in KORU
As of June 24 $^{th}$  
![](images/6f3ac72c1ca24d9954b3b3c213608d3b09604a2cbbf434c8ef7366fafbdd375b.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

![](images/c4830a2b03a13fe21ea48ee565211d60dff3f41da84a46e155de308b29f7e0fc.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 10: ...driven by large outflows in XLC (-4.2z week)
As of Jun 24 $^{th}$ .  
![](images/8b168f1813fcd25e90195e7fb5e3a440dc23146d652637aad43115f4e9e0b323.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 11: Retail Investor Daily Purchases by Stocks and ETFs \$M, as of Jun 24 $^{th}$  
![](images/9a19489b4960f4eff714c75eec055f26cd09c3b994fc300ce8867cc0d60b5713.jpg)  
-2000 -
24-Dec 02-Jan 09-Jan 16-Jan 26-Jan 02-Feb 09-Feb 17-Feb 24-Feb 03-Mar 10-Mar 17-Mar 24-Mar 31-Mar 08-Apr 15-Apr 22-Apr 29-Apr 06-May 13-May 20-May 28-May 04-Jun 11-Jun 18-Jun

Source: JPM Equity Strategy & Quantitative Research

## Retail Cash Activity – Overview

Figure 12: Retail Single Stock Activity by Themes

<table><tr><td colspan="2">Thematic Baskets</td><td colspan="3">Δ in Retail Turnover ($Bn)</td></tr><tr><td>Basket</td><td>Index</td><td>Week Ago</td><td>Month Ago</td><td>YTD</td></tr><tr><td>S&amp;P 500 Top 30 AI/Datacenter Beneficiaries</td><td>JPRAID30</td><td>1.18</td><td>6.00</td><td>37.19</td></tr><tr><td>Growth</td><td>JPAMGROW</td><td>1.10</td><td>6.68</td><td>36.80</td></tr><tr><td>AI/Datacenter/Electrification</td><td>JPAMAIDE</td><td>1.04</td><td>6.13</td><td>37.94</td></tr><tr><td>US Companies with High Direct China Revenue Exposure</td><td>JPAMCREV</td><td>0.96</td><td>4.60</td><td>20.13</td></tr><tr><td>Magnificent 7</td><td>Mag7</td><td>0.80</td><td>5.11</td><td>30.75</td></tr><tr><td>OBBBA Immediate Expensing Beneficiaries</td><td>JPGTIEXB</td><td>0.60</td><td>1.96</td><td>17.12</td></tr><tr><td>Government Efficiency</td><td>JPAMDOGE</td><td>-0.04</td><td>-0.11</td><td>0.68</td></tr><tr><td>US Federal Budget Sensitive</td><td>JPAMGOVT</td><td>-0.05</td><td>-0.20</td><td>0.33</td></tr><tr><td>US Inflation</td><td>JPAMINFL</td><td>-0.07</td><td>-0.31</td><td>-1.87</td></tr><tr><td>Trump Deregulation Agenda</td><td>JPRGDREG</td><td>-0.09</td><td>-1.21</td><td>-4.06</td></tr><tr><td>Inflation Outperformers</td><td>JPAMINOP</td><td>-0.13</td><td>-0.95</td><td>-3.11</td></tr><tr><td>Domestic</td><td>JPAMDOME</td><td>-0.15</td><td>-0.79</td><td>-0.20</td></tr></table>

Figure 13: Retail Cumulative Purchases in Mag 7 + PLTR (\$B)  
![](images/219786fb07da51ac0bd17cb7d0106819f28df61de4134813f4e5c7a5700c70b9.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Source: JPM Equity Strategy & Quantitative Research. See report, report, and report for details on above baskets. Note: JPM does not provide research coverage of the baskets mentioned here, and investors should not expect continuous analysis or additional reports relating to them.

Figure 14: Retail Single Stock Activity by Sector (\$B)
Activity is dominated by Tech and Cons. Disc.  
![](images/ae884d55d543b31bc2bbed9332b1320ae871bf6a0f319a306e47a43600c5e9f1.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 15: Retail ETF Activity by Themes
Buying / Selling of ETFs aggregated by themes, in \$B.  
![](images/4ac361d37d88fd1dee7f3730ea096385c75c0bfb5b0227d8a7cb477e7fd8d7da.jpg)  
Source: JPM Equity Strategy & Quantitative Research

## Single Stock Stories with Elevated Retail Activity

Hedge Funds vs. Retail: High Short Interest Meme Stocks

\- BIRD (\$2.5M sold last week, 1.1z, Figure 18): The company rebranded on June 17, completing its pivot from a footwear retailer to an AI infrastructure-focused business, and increased its financing facility to \$100 million from \$50 million. Retail interest has picked up since April 2026, with net purchases totaling \$14M, alongside rising short interest now at \~20% of float, up 12% since April 2026.

\- CPB (\$2.0M bought last week, -0.3z, Figure 19): The stock fell by more than 3% on June 22 after it was removed from the S&P 500. The stock has been on retail investors' radar since January 2025, with purchases accelerating since March 2026 totaling \$100M, amid elevated short interest of \~25% of float, up 5% since March 2026.

\- ODD (\$0.5M sold last week, -0.6z, Figure 20): The stock rose by more than 6% on June 12 after the company entered into privately negotiated agreements to repurchase \$50 million of 0% exchangeable senior notes due 2030 for \$35 million. Retail investors have net purchased \$35M since August 2025, alongside rising short interest at \~24% of float, up 6% this month.

## Macro & Fundamental Stories

\- Semiconductor stocks are down -6% in the last 3 days (vs. S&P 500 at -1%). Of note, SNDK (\$455M bought last week, 3.2z, Figure 21), MU (\$258M bought last week, 1.1z, Figure 23), WDC (\$37M bought last week, 1.4z, Figure 25), AMAT (\$38M bought last week, 2.1z, Figure 27), LRCX (\$11.4M bought last week, 0.7z, Figure 29), and KLAC (\$30M sold last week, -1.9z, Figure 31) have been among the worst performers, declining between -9% and -14%. NVDA (\$510M bought last week, 0.0z, Figure 33) is down -4%.

\- Apogee Therapeutics (APGE, \$6M sold on 6/22, -8.7z, Figure 35) was up +47% after AbbVie (ABBV, \$15.4M bought on 6/22, 2.4z, Figure 37) announced they were acquiring it for \~\$11B. Our analysts see this transaction as a solid fit for AbbVie as it further builds out the company's pipeline in immunology / atopic dermatitis. The deal, which is expected to close in 3Q26, should be moderately dilutive through 2032 (link). AbbVie's stock traded up +8% on the back of the news.

\- GETY (\$0.7M bought on 6/22, 3.0z, Figure 39): Getty Images was up +90% on 6/22 after announcing a deal with OpenAI to integrate its digital image libraries into ChatGPT.

\- AMC (\$0.5M sold on 6/23, -0.4z, Figure 41): AMC Theaters' stock was down -26% on 6/23 after announcing a \$200M cash raise to retire costly debt following a strong opening weekend for "Toy Story 5".

Figure 17: Decreasing Squeeze Risk in Meme Stocks: Retail Selling in High Short Interest Names

## Meme Battlegrounds: Retail Buying vs. Hedge Fund Shorting

In this section, we are flagging a few stocks that are heavily mentioned on Social Media and have high Retail buying as well as high Hedge fund Shorting. These stocks may experience unexpected flows in case of increased activity.

## Social Media Screen and Retail Activity

Figure 16: Most Hyped Stocks on Social Media  
Top 20 names based on social media traction over the week (Social Interest), Scaled by market cap

<table><tr><td>Ticker</td><td>Name</td><td>Mkt Cap ($B)</td><td>Social Interest Score</td><td>Median Short Interest (% float)</td><td>Extreme Imbalance 1D Z</td><td>Date of Imbalance</td></tr><tr><td>ACM</td><td>AECOM</td><td>8.9</td><td>38.9</td><td>5.1%</td><td>0.9</td><td>17-Jun</td></tr><tr><td>SNAP</td><td>Snap Inc</td><td>7.4</td><td>37.5</td><td>10.3%</td><td>0.7</td><td>17-Jun</td></tr><tr><td>ACN</td><td>Accenture PLC</td><td>78.1</td><td>35.5</td><td>4.3%</td><td>5.1</td><td>18-Jun</td></tr><tr><td>SMCI</td><td>Super Micro Computer Inc</td><td>21.6</td><td>35.0</td><td>13.9%</td><td>1.5</td><td>17-Jun</td></tr><tr><td>PLTR</td><td>Palantir Technologies Inc</td><td>279.8</td><td>33.7</td><td>3.2%</td><td>-0.7</td><td>23-Jun</td></tr><tr><td>SMR</td><td>NuScale Power Corp</td><td>4.0</td><td>33.2</td><td>17.6%</td><td>-1.5</td><td>17-Jun</td></tr><tr><td>MU</td><td>Micron Technology Inc</td><td>1186.1</td><td>32.8</td><td>3.3%</td><td>1.6</td><td>18-Jun</td></tr><tr><td>JD</td><td>JD.com Inc</td><td>35.7</td><td>32.7</td><td>2.6%</td><td>0.5</td><td>23-Jun</td></tr><tr><td>IREN</td><td>IREN Ltd</td><td>19.6</td><td>32.4</td><td>17.8%</td><td>-1.4</td><td>23-Jun</td></tr><tr><td>NBIS</td><td>Nebius Group NV</td><td>69.9</td><td>32.4</td><td>21.6%</td><td>-2.7</td><td>23-Jun</td></tr><tr><td>AMD</td><td>Advanced Micro Devices Inc</td><td>847.7</td><td>32.2</td><td>2.7%</td><td>-1.1</td><td>22-Jun</td></tr><tr><td>RDDT</td><td>Reddit Inc</td><td>31.9</td><td>32.0</td><td>9.7%</td><td>-0.4</t

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 24 Jun 2026 10:20 PM EDT

Disseminated 24 Jun 2026 10:20 PM EDT
"""
