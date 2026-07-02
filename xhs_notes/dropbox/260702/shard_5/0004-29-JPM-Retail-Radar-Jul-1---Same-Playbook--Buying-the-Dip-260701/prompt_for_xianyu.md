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

## Retail Radar

Jul 1 - Same Playbook, Buying the Dip

## Retail Trading Activity Overview

\- Retail investor flows were resilient last week (75.4%ile), driven by strong single-stock inflows (94.8%ile) while ETF activity remained modest (17.5%ile). Wednesday was a clear standout, with retail purchases reaching their 93%ile, Figure 9. Once again, Tech and Memory were the primary drivers of retail demand, even as concerns of an AI bubble resurfaced.

\- ETF activity remained relatively modest across categories. In Semis, positioning has largely plateaued: steady outflows from leveraged SOXL (-2.9z, Figure 2) have been partly offset by inflows into SOXX and SMH, as well as Tech-tilted indices QQQ and QQQM. Within Software, activity also remained unchanged—particularly in IGV, even as the ETF is up \~8% over the past week. Fixed Income ETF flows have rebounded to roughly month-ago levels after several weeks of softness, led by inflows into Corporate bond ETFs (notably Investment Grade) and Aggregate/Multi-Sector products, including AGG.

\- Within single stocks, inflows into Semis climbed to their highest levels in more than a year, Figure 4, while Tech Hardware also attracted its second-strongest demand in over 2 years (2.5z). As in prior weeks, retail's top stock picks stayed concentrated in Memory and Semis, with investors continuing to buy on dips, with a particular focus on the same two favorites: MU (3.7z) and SNDK (4.6z), Figure 2, followed by NVDA, SPCX and MSFT. Communications was the second most sought-after sector, led by SPCX and dip-buying in T (2.4z) and VZ (0.8z) after reports of a planned launch of a Starlink-branded retail mobile service for US customers, see Macro & Fundamental Stories.

## Retail Trading Activity in Numbers for the Week: Jun 25 to Jul 1

\- Retail flows were \$8.1B this week, above the 12-month avg of \$6.7B/week. Retail investors continued to favor ETFs (+\$4.6B) over Single Stocks (+\$3.5B).

\- Outside of Broad Based Large Cap Equity ETFs (+\$1.4B), retail ETF buying was influenced by Fixed Income — Multi Sector (+\$253M) and Corporates Investment Grade (+\$242M), International Equity EAFE (+\$217M) and Equity Style Dividend (+\$189M).

\- This week, in line with prior weeks, retail investors continued to buy AI datacenters and electrification (JPAMAIDE), Top 30 AI/Datacenter Beneficiaries, Growth, along with OBBBA Immediate Expensing Beneficiaries and AI Software/Product/Monetization, see Figure 6.

\- Activity in Mag7 this week: Retail investors bought NVDA (+\$492M), MSFT (+\$292M), GOOGL /GOOG (+\$94M), AAPL (+\$35M), and sold AMZN (-\$1M), META (-\$18M) and TSLA (-\$130M).

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

Dubravko Lakos-Bujas AC
(1-212) 622-3601
dubravko.lakos-bujas@JPM.com
JPM Securities LLC

We thank Aditya Mulye and G. K. Kiruthik Srinivaas of JPM India Private Limited for their significant contributions to this report.

## Past Issues:

7/1 - Retail Remembers the Dip, Memory (MU)
Serves Right
6/17 - Tech Craze Spillover to Communications
6/10 - Tech Selling amidst Drawdown, World Cup Theme Yet to Kick In
6/3 - MEME Earnings, Trading around IPOs
5/27 - Theme Stack: AI, Memory, Space, Quantum
5/13 - Software vs Semis Positioning
5/6 - Memory and AI, the Catch-Up Trade
4/29 - Peak Earnings, Peak Mag-7
4/22 - Towards a MEME Revival?

\- Outside of Mag7, retail investors favored Tech (+\$2.3B), Communications (+\$546M), Industrials (+\$120M) and Health Care (+\$114M) and were net sellers of Financials (-\$269M) and Consumer Disc. (-\$135M).

\- Top 5 retail stocks last week: MU (+\$897M, 3.7z), SNDK (+\$705M, 4.6z), NVDA (+\$492M), SPCX (+\$460M), MSFT (+\$292M). Bottom 5 retail stocks: TSLA (-\$130M), ORCL (-\$67M), CSCO (-\$46M), V (-\$41M), TDG (-\$39M).

\- In options, retail share is at highs, Figure 35. The most traded options were in the following names, echoing previous weeks: TSLA, MU, NVDA, AMZN, SNDK, AMD, META, SPCX, MSFT and AAPL. For the most bought/sold delta and gamma names, see Retail Activity in Options. Also see Retail Investors Options Activity by Sectors.

\- Futures Activity (Non Retail): Over the past week, Futures traders net sold \~\$11.3B, driven by net sales in ES (\~\$7.3B), NQ (\~\$2.2B) and RTY (\~\$1.8B).

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

Figure 1: Retail Investor Daily Purchases by Stocks and ETFs \$M, as of Jul 1 $^{st}$  
![](images/d72acaf54eb9118ebbb0223b6d26099822cf1c9426a66dce52bf9a2032fc0663.jpg)  
-2000 - 02-Jan 09-Jan 16-Jan 26-Jan 02-Feb 09-Feb 17-Feb 24-Feb 03-Mar 10-Mar 17-Mar 24-Mar 31-Mar 08-Apr 15-Apr 22-Apr 29-Apr 06-May 13-May 20-May 28-May 04-Jun 11-Jun 18-Jun 26-Jun

Source: JPM Equity Strategy & Quantitative Research

Figure 2: Retail Imbalance in Memory Stocks (\$B)
As of Jul 1 $^{st}$  
![](images/2daa4a8ebfec8eb05298da978ecbefe2ceb55dfedfb895bfa431ea4955e70295.jpg)  
Source: JPM Equity Strategy & Quantitative Research  
Figure 4: Semis stocks Imbalance at its \~14 month highs...

Figure 3: Retail Imbalance in Tech ETFs
As of Jul 1 $^{st}$  
![](images/395948117b343fff5944513e16a0908e36c151667e679270226e1c74d7c5375b.jpg)  
Source: JPM Equity Strategy & Quantitative Research

![](images/c2888e7f82a3499a193f3d61380fe18140384fc65090d4c3157f180445183fb4.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 5: ...driven by MU (and NVDA)
As of Jul 1 $^{st}$  
![](images/b8b3d71645a5f454cc0f851e89a582a853111a1e85aae02a0eeb248a40178ac6.jpg)  
Source: JPM Equity Strategy & Quantitative Research

## Retail Cash Activity – Overview

Figure 6: Retail Single Stock Activity by Themes

<table><tr><td colspan="2">Thematic Baskets</td><td colspan="3">Δ in Retail Turnover ($Bn)</td></tr><tr><td>Basket</td><td>Index</td><td>Week Ago</td><td>Month Ago</td><td>YTD</td></tr><tr><td>AI/Datacenter/Electrification</td><td>JPAMAIDE</td><td>1.45</td><td>6.22</td><td>40.15</td></tr><tr><td>S&amp;P 500 Top 30 AI/Datacenter Beneficiaries</td><td>JPRAID30</td><td>1.45</td><td>5.86</td><td>39.44</td></tr><tr><td>Growth</td><td>JPAMGROW</td><td>1.26</td><td>6.27</td><td>38.80</td></tr><tr><td>OBBBA Immediate Expensing Beneficiaries</td><td>JPGTIEXB</td><td>1.06</td><td>3.02</td><td>18.84</td></tr><tr><td>AI Software/Product/Monetization</td><td>JPAMAISO</td><td>0.84</td><td>3.03</td><td>24.82</td></tr><tr><td>Fed Rate Cut Outperformers</td><td>JPGTFEDO</td><td>0.80</td><td>2.22</td><td>12.14</td></tr><tr><td>Consumer Laggards with Brand Value</td><td>JPAMBRND</td><td>-0.06</td><td>1.24</td><td>7.79</td></tr><tr><td>US Tariff Sensitive</td><td>JPGTTRUS</td><td>-0.07</td><td>0.77</td><td>8.18</td></tr><tr><td>US Trade Tariff Underperformers</td><td>JPGTUSTU</td><td>-0.10</td><td>1.11</td><td>8.19</td></tr><tr><td>Inflation Outperformers</td><td>JPAMINOP</td><td>-0.10</td><td>-0.87</td><td>-3.25</td></tr><tr><td>IRA Green/EV/Climate Beneficiaries</td><td>JPAMIRAG</td><td>-0.14</td><td>1.25</td><td>8.32</td></tr><tr><td>Domestic Manufacturing Tax</td><td>JPAMDMAN</td><td>-0.17</td><td>1.11</td><td>8.53</td></tr></table>

Figure 7: Retail Cumulative Purchases in Mag 7 + PLTR (\$B)  
![](images/a63e69a9c062effb99c7f3bfe21d59359096944bc45895709929b56aa6ed5acf.jpg)  
Source: JPM Equity Strategy & Quantitative Research. See report, report, and report for details on above baskets. Note: JPM does not provide research coverage of the baskets mentioned here, and investors should not expect continuous analysis or additional reports relating to them.

Source: JPM Equity Strategy & Quantitative Research  
Figure 8: Retail Single Stock Activity by Sector (\$B)
Activity is dominated by Tech and Cons. Disc.  
![](images/786e28f39d0404b99b9f6fc5d6eed6f020161381092dd035002086945fbcb7d9.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 9: Retail ETF Activity by Themes
Buying / Selling of ETFs aggregated by themes, in \$B.  
![](images/71d754c84bc4ad8adc23b2a4cabda05600f42f54646253d4a666632b44c51bce.jpg)  
Source: JPM Equity Strategy & Quantitative Research

## Single Stock Stories with Elevated Retail Activity

## Hedge Funds vs. Retail: High Short Interest Meme Stocks

\- QXO (\$4.4M bought last week, -0.4z, Figure 12): The company finalized its acquisition of TopBuild, enhancing its end-to-end position across the building products value chain. The stock has been on retail investors' radar since September 2025, with purchases accelerating since April 2026 totaling \$112M, amid elevated short interest of \~21% of float, up 11% since March 2026.

\- VELO (\$6.1M bought last week, -2.0z, Figure 13): The company announced it is expanding manufacturing capacity to meet strong demand from the defense and aerospace markets. Since June 2026, retail investors have been buying aggressively, with net purchases of roughly \$27M for the month. At the same time, short interest has climbed to about 34% of the float - up 13% over the month.

\- ARES (\$1.3M sold last week, -0.3z, Figure 14): The company recently announced that its credit fund led a \~\$1.7 billion debt financing in support of a sponsor-backed acquisition, further expanding its role in large-scale leveraged transactions. Retail interest has picked up since March 2026, with net purchases totaling \$66M, alongside rising short interest now at \~9% of float, up 4% since the start of this year.

## Macro & Fundamental Stories

\- Verizon (VZ, \$25M bought last week, 0.8z, Figure 16), T-Mobile (TMUS, \$8M sold last week, -0.3z Figure 18) and AT&T (T, \$33M bought last week, 2.7z, Figure 20) have each fallen 8-10% since 6/26, following reports of a planned launch of a Starlink-branded retail mobile service for US customers.

\- ON Semiconductor (ON, \$14M bought on 6/26, 5.3z, Figure 22) was down -24% on 6/26 after announcing an agreement to acquire Synaptics Inc (SYNA, \$6.5M sold on 6/26, -7.9z, Figure 24) in an all-stock deal with an enterprise value of \~\$7B. The transaction is expected to close in mid-CY27. Management noted that the strategic rationale for the combination centers on positioning the combined company at the intersection of what was characterized as the “four pillars of Physical AI” (i.e., power, sensing, connected compute, and control), extending ON’s existing strengths in power and sensing into edge/physical AI compute and connectivity through SYNA’s Astra processor/MCU platform, wireless connectivity portfolio (Wi-Fi, Bluetooth, GPS/GNSS), and human-machine interface (HMI) solutions (link).

\- MU (\$897M bought last week, 4.5z, Figure 26): Retail investors continue to be quite active in Micron, with the stock up +16% on 6/25 after a blockbuster earnings report. The company reported results and guidance were far ahead of expectations, but the even more meaningful development was the substantial expansion of its Strategic Customer Agreements (SCAs) from a single 5-year contract (announced last qtr) to 16 signed agreements, a step-change that fundamentally transforms MU's business model from a cyclical commodity producer to a multi-year contracted supplier with significant downside protection on both revenue and margins in our analysts' view (link). Note that the stock gave back most of these gains in subsequent days, up +3% in the last 7 days.

\- AAPL (\$110M bought on 6/25, 3.2z, Figure 28): Apple was down -6% on 6/25 after announcing higher-than-expected product price increases for Macs, iPads and home devices to offset cost hikes associated with the shortage of memory chips and storage. While notably leaving iPhone, Apple Watch, and AirPods unchanged, the company hinted that there may be more price adjustments in the future. The increases are global and range from \$30 to \$500 in absolute terms, with price increases for most high-volume SKUs in the range of 15%-20% (link).

\- CMCSA (\$5M bought on 6/29, 1.4z, Figure 30): On Monday (June 29), Comcast announced plans to separate into two independent, publicly traded companies via a tax-free spin-off of NBCUniversal and Sky to Comcast shareholders, expected to close in about a year. The split will create two distinct entities: a connectivity and cable company (RemainCo Comcast), comprising broadband, wireless, and business services, and a global media and entertainment company (NBCUniversal, including Sky), spanning theme parks, film and TV studios, streaming, sports, and news. No exchange ratio was disclosed. Comcast will retain up to a 19.9% stake in NBCU for up to one year following the spin, to be sold down in a tax-efficient manner over that period to support deleveraging (link). The stock was up +5% on the back of the announcement.

## Meme Battlegrounds: Retail Buying vs. Hedge Fund Shorting

In this section, we are flagging a few stocks that are heavily mentioned on Social Media and have high Retail buying as well as high Hedge fund Shorting. These stocks may experience unexpected flows in case of increased activity.

## Social Media Screen and Retail Activity

## Figure 10: Most Hyped Stocks on Social Media

Top 20 names based on social media traction over the week (Social Interest), Scaled by market cap

<table><tr><td>Ticker</td><td>Name</td><td>Mkt Cap ($B)</td><td>Social Interest Score</td><td>Median Short Interest (% float)</td><td>Extreme Imbalance 1D Z</td><td>Date of Imbalance</td></tr><tr><td>WEN</td><td>Wendy&#x27;s Co/The</td><td>1.6</td><td>50.7</td><td>32.4%</td><td>0.9</td><td>24-Jun</td></tr><tr><td>ASTS</td><td>AST SpaceMobile Inc</td><td>34.5</td><td>35.9</td><td>37.5%</td><td>0.7</td><td>24-Jun</td></tr><tr><td>MSTR</td><td>Strategy Inc</td><td>30.5</td><td>33.7</td><td>12.2%</td><td>5.1</td><td>25-Jun</td></tr><tr><td>MU</td><td>Micron Technology Inc</td><td>1303.6</td><td>33.1</td><td>3.7%</td><td>1.5</td><td>24-Jun</td></tr><tr><td>SLS</td><td>SELLAS Life Sciences Group Inc</td><td>2.7</td><td>30.3</td><td>34.7%</td><td>-0.7</td><td>29-Jun</td></tr><tr><td>BB</td><td>BlackBerry Ltd</td><td>7.4</td><td>29.9</td><td>6.4%</td><td>-1.5</td><td>24-Jun</td></tr><tr><td>BABA</td><td>Alibaba Group Holding Ltd</td><td>230.4</td><td>28.8</td><td>1.7%</td><td>1.6</td><td>25-Jun</td></tr><tr><td>RDDT</td><td>Reddit Inc</td><td>33.4</td><td>27.7</td><td>12.0%</td><td>0.5</td><td>29-Jun</td></tr><tr><td>MSFT</td><td>Microsoft Corp</td><td>2771.0</td><td>27.0</td><td>1.3%</td><td>-1.4</td><td>29-Jun</td></tr><tr><td>OPTX</td><td>Syntec Optics Holdings Inc</td><td>0.5</td><td>

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 01 Jul 2026 10:43 PM EDT

Disseminated 01 Jul 2026 10:43 PM EDT
"""
