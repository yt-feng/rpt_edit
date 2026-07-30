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

Jul 29 – Momentum Unwind, Cutting Tech Losses

## Retail Trading Activity Overview

\- Sentiment deteriorated further this week as retail flows meaningfully weakened, reaching their 0.8%ile vs 1y history; this time, retail investors aggressively pulled out of single names (3.2%ile, with 4 consecutive days of single-stock selling, Figure 10), while only modestly adding exposure to ETFs (1.6%ile).

\- Within ETFs, Tech saw significant outflows—the second-largest on record, behind only the week ending June 10 $^{th}$ , Figure 5, driven primarily by SOXL (-1.2z, Figure 6). Retail investors also cut exposure to crypto ETFs, led by BITO (-4.9z).

\- Single-stock selling was overwhelmingly concentrated in Tech. Hardware names took the brunt of the selling, posting their largest weekly selling on record, Figure 7. SNDK was the biggest driver (-3.2z), followed by AAPL. In broader Semis, MU moved into the most-sold list among retail investors—just a few weeks after consistently featuring alongside SNDK among their favorites, Figure 8. In line with this, our Crowding analysis that captures broader market positioning quantifies the sharp Semis de-crowding, down to the 91.8%ile from the 99%ile, see report and report, Figure 11. In contrast, the Mag 7 + SPCX saw positive flows overall: NVDA, GOOGL, SPCX and TSLA were amongst the top 5 this week, alongside SKHY. Internationally, Korea has undergone an intense period of de-leveraging since mid-June, with the positioning setup now appearing attractive on balance according to our analysts, see report.

\- The sharp deterioration in retail YTD P&L (Figure 9) may help explain why retail investors have been quick to cut Tech exposure as the Semis-led Momentum Unwind has weighed on portfolios (see Factor Crowdings and Rotations).

\- As we head into peak-Earnings, investors are focusing on the major announcements slated for this week. Retail participation has been limited so far, underscoring a deterioration in sentiment, see Single Stock Stories with Elevated Retail Activity:

\- Retail investors trimmed META, MSFT and QCOM on Wednesday before their announcements (-0.6z, 0.8z, and -0.2z, respectively). MSFT's Cloud unit posted a larger-than-expected increase in sales at +43% y/y, with shares rising \~3% in post-market trading. Capex increased +70% y/y to \$41B during the quarter. META narrowed its 2026 capex guidance to \$130-145B, lifting the low-end from \$125B. Revenue for the quarter came in line with expectations, but next quarter's outlook was lackluster. Shares fell as much as \~10% in post-market trading after the results were published. QCOM's earnings missed expectations, but top line was better than expected. Additionally, the company expects non-handset revenue growth to accelerate to 60% in fiscal year 2027, as it tries to reduce its dependence on phones with a new push into the data center market.

\- Retail investors trimmed AAPL and AMZN on Wednesday (-0.7z and -0.6z, resp.). AMZN reports earnings tomorrow AMC, with our analysts

See page 23 for analyst certification and important disclosures.

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

7/29 - Momentum Unwind Accelerates Amid Earnings
7/22 - Momentum Cooldown, Hyperscaler Earnings
7/15 - Trading Earnings as Flows Cool
7/8 - Split-the-Dip as Momentum Cools
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

expecting AWS growth acceleration of low-mid 30%’s, higher capex guidance and retail margin expansion (link). AAPL also reports tomorrow, with price elasticity the key watchpoint after \~20% average price hikes across iPads and Macs—moves that have also lifted expectations for iPhone 18 pricing. While investors debate near-term consumer pushback amid higher memory costs, our analysts see multiple offsets that should leave revenue and earnings more resilient than feared (link).

## Factor Crowdings and Rotations

\- Amid weakening retail sentiment, a Momentum Unwind, and the recent market drawdown, we provide a few additional observations on investor positioning:

(1) Crowding remains high across higher-risk segments (e.g., Low Quality at 94.8%ile and Speculative Growth at 98.0%ile), with Value also elevated (88.7%ile);

(2) Momentum's Beta exposure is high, and Momentum–Beta correlations have declined from extremes during this unwind; and

(3) Implied stock correlations increased over the past week from historically low levels (COR3M <Index>), even as peak-Earnings season typically coincides with lower stock correlations. In many risk-model frameworks, higher implied correlations translate into higher implied betas and higher portfolio risk estimates, which lead systematic/quant portfolios to reduce net exposure as volatility targets and risk constraints bind.

\- In combination with month-end Momentum rebalancing, these conditions are consistent with the elevated volatility observed in Momentum and higher-risk factors this week.

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

We thank G. K. Kiruthik Srinivaas and Aditya Mulye of JPM India Private Limited for their significant contributions to this report.

## Retail Trading Activity in Numbers for the Week: Jul 23 to Jul 29

\- Retail flows were \$2.2B this week, well below the 12-month average of \$6.8B/week. Retail investors continued to favor ETFs (+\$3.7B) over Single Stocks (-\$1.4B).

\- Outside of Broad Based Large Cap Equity ETFs (+\$1.5B), retail ETF buying was influenced by Equity Style Dividend (+\$261M), Equity Style Call/Put writing (+206M), Fixed Income – Multi Sector (+\$172M), and Equity Broad Based Multi Cap (+\$166M).

\- This week, in line with prior weeks, retail investors continued to buy AI datacenters and electrification (JPAMAIDE), Mag 7, Top 30 AI/Datacenter Beneficiaries, Growth, along with AI Software/Product/Monetization, and OBBBA Immediate Expensing Beneficiaries, see Figure 4.

\- Activity in Mag7 this week: Retail investors bought NVDA (+\$601M), GOOGL/GOOG (+\$377M), TSLA (+\$121M), MSFT (+\$33M) and sold AMZN (-\$22M), META (-\$26M) and AAPL (-\$169M).

\- Outside of Mag7, retail investors favored Communications (+\$177M) and were net sellers of Tech (-\$2.2B), Industrials (-\$232M), Cons. Disc. (-\$200M) and Health Care (-\$176M).

\- Top five retail stocks last week: NVDA (+\$601M), GOOGL/GOOG (+\$377M), SPCX (+\$263M), SKHY (+\$166M), TSLA (+\$121M). Bottom 5 retail stocks: SNDK (-\$579M, -3.2z), MU (-\$515M, -1.9z), AMD (-\$328M, -2.2z), AAPL (-\$169M), MRVL

(-\$84M)

\- In options, retail share is at highs, Figure 54. The most traded options were in the following names, echoing previous weeks: TSLA, NVDA, MU, AMZN, SNDK, META, AMD, AAPL, SPCX, and MSFT. For the most bought/sold delta and gamma names, see Retail Activity in Options. Also see Retail Investors Options Activity by Sectors.

Figure 1: Momentum Crowding  
![](images/b2ed8a1ad79e520479912dfe0ac0e72d8db82da96bb4b51367a1b824ec78ef6b.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 2: Momentum Unwind Now vs Feb-Mar'25  
![](images/d82e4bb67ecf144321b0ea0372fed20bd5d80733cc23291a0af84051f74a7c1b.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 3: Crowding in Low Quality  
![](images/290a40c9a287802ef907c7bd8e46e6ea01387ff9debe1ccd8d242a15f8e8fecd.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 4: Momentum Beta Correlations  
![](images/9fb561b0be6e221d13570b3dcda7de0664ed5b2ad0f4bdd5904c2ddce32875ed.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 5: Weekly Outflows out of Tech ETFs were the second highest on record  
![](images/41e559c828ed61702ca9b7b20b2f0b0d4dec2083162a1700cd5def6ba27e2781.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 6: Cumulative Retail Imbalance in SOXL As of Jul 29 $^{th}$  
![](images/5dae1ec5e0bbb6a9828eefc9f13c4b0f3125a32dfe674bd7c5dc6ed42bee185d.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 7: Weekly Outflows out of Tech Hardware & Equipment stocks were the highest on record  
![](images/eb67ee07de6ef7f1e3123e4b134a9c1f2febe91db99eeb3203e8e07de94076c3.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 8: Memory Stocks: Cumulative Retail Net Bought In \$B  
![](images/4b9bf0c2dc8148b501129522c25fff0806f8e5d950fb4e30ecf46d7662a4a2ef.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 9: Retail Investors Single Stocks P&L  
![](images/be53c988dae895f48a7571b3cf01dae1087e7207468badf0e208b67e98d28523.jpg)  
Source: JPM Equity Strategy & Quantitative Research

-2000 -
29-Jan 05-Feb 12-Feb 20-Feb 27-Feb 06-Mar 13-Mar 20-Mar 27-Mar 06-Apr 13-Apr 20-Apr 27-Apr 04-May 11-May 18-May 26-May 02-Jun 09-Jun 16-Jun 24-Jun 01-Jul 09-Jul 16-Jul 23-Jul

Figure 10: Retail Investor Daily Purchases by Stocks and ETFs \$M, as of Jul 29 $^{th}$  
![](images/df6a4d6348f6aa6ed4ab56f1567c022d379b76c83ff4a92b6346ed9dd28f6589.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 11: Semis vs Software Crowding  
![](images/6f3c575b988b2312c2de19e5a04ebb255e51e36806e8fc6f9ec33d149a998f02.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 12: Tech vs Health Care Crowding  
![](images/c0a8d63f7536ce9eed0c5e3d05338ae6a9beceb729352e19dcd4d01dfd7b32dc.jpg)  
Source: JPM Equity Strategy & Quantitative Research

## Retail Cash Activity – Overview

Figure 13: Retail Single Stock Activity by Themes

<table><tr><td colspan="2">Thematic Baskets</td><td colspan="3">Δ in Retail Turnover ($Bn)</td></tr><tr><td>Basket</td><td>Index</td><td>Week Ago</td><td>Month Ago</td><td>YTD</td></tr><tr><td>AI/Datacenter/Electrification</td><td>JPAMAIDE</td><td>2.08</td><td>5.70</td><td>45.48</td></tr><tr><td>Magnificent 7</td><td>Mag7</td><td>2.07</td><td>4.80</td><td>36.29</td></tr><tr><td>S&amp;P 500 Top 30 AI/Datacenter Beneficiaries</td><td>JPRAID30</td><td>1.79</td><td>5.06</td><td>44.17</td></tr><tr><td>AI Software/Product/Monetization</td><td>JPAMAISO</td><td>1.69</td><td>3.57</td><td>28.12</td></tr><tr><td>Growth</td><td>JPAMGROW</td><td>1.64</td><td>4.48</td><td>42.93</td></tr><tr><td>OBBBA Immediate Expensing Beneficiaries</td><td>JPGTIEXB</td><td>1.27</td><td>3.02</td><td>21.63</td></tr><tr><td>Sensitive to Low-End Consumer</td><td>JPRLOWCO</td><td>-0.04</td><td>-0.12</td><td>-1.51</td></tr><tr><td>US Federal Budget Sensitive</td><td>JPAMGOVT</td><td>-0.07</td><td>-0.11</td><td>0.16</td></tr><tr><td>US Inflation</td><td>JPAMINFL</td><td>-0.10</td><td>-0.17</td><td>-2.08</td></tr><tr><td>Inflation Outperformers</td><td>JPAMINOP</td><td>-0.26</td><td>-0.45</td><td>-3.70</td></tr><tr><td>Trump Deregulation Agenda</td><td>JPRGDREG</td><td>-0.60</td><td>-0.78</td><td>-4.80</td></tr><tr><td>Wage Sensitive</td><td>JPAMWAGG</td><td>-0.89</td><td>-0.22</td><td>3.55</td></tr></table>

Figure 14: Retail Cumulative Purchases in Mag 7 + PLTR (\$B)  
![](images/09e3355b1a91592a782e6bcd4cb51e95e3841eaf74722e21d92562e4faac58d7.jpg)  
Source: JPM Equity Strategy & Quantitative Research. See report, report, and report for details on above baskets. Note: JPM does not provide research coverage of the baskets mentioned here, and investors should not expect continuous analysis or additional reports relating to them.  
Source: JPM Equity Strategy & Quantitative Research

Figure 15: Retail Single Stock Activity by Sector (\$B)
Activity is dominated by Tech and Cons. Disc.  
![](images/9fde3b4cebab1c8c2d8f6199cbb040068fa3ef82c998e09d0fa83990c4149bcd.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 16: Retail ETF Activity by Themes
Buying / Selling of ETFs aggregated by themes, in \$B.  
![](images/fd5233b0b52ba060ebd808abf0aad453be40702cd566661ce83c0b64f54ce587.jpg)  
Source: JPM Equity Strategy & Quantitative Research

## Single Stock Stories with Elevated Retail Activity

Hedge Funds vs. Retail: High Short Interest Meme Stocks

\- DBGI (\$0.4M bought last week, 0.3z, Figure 19): The company expanded its secured U.S. program by 32% to \$165M, driven by the addition of new apparel and footwear categories. Retail interest has been strong, with net purchases totaling \$70M since May 2026, amid moderate short interest of \~14% of float, up 10% over the same period.

\- INFQ (\$0.2M sold last week, -0.7z, Figure 20): The company has undergone a series of management changes and secured three Genesis Mission projects from the U.S. Department of Energy focused on AI-optimized quantum circuit design for nuclear applications. The stock has been on retail investors' radar, with net purchases totaling \$120M since March 2026, alongside elevated short interest of \~16% of float.

\- JOBY (\$13.4M bought last week, -0.0z, Figure 21): The company signed a binding agreement with Virgin Atlantic, naming it Joby's exclusive airline partner for air taxi services in the UK. Retail investors have purchased \$400M year-to-date, against a backdrop of high short interest of \~18% of float, which has increased by 8% over the same period.

## Earnings Stories

\- AAPL (\$18.6M sold on 7/29, -0.0z, Figure 22): Apple reports earnings tomorrow AMC, with price elasticity of demand the biggest watchpoint for the company across its key hardware product lines following the announcement of a \~20% price increase on average across iPads and Macs, which also raised expectations for the magnitude of price increases likely to be enacted in conjunction with the launch of iPhone 18. However, even as short-term consumer responses to the unprecedented price increases, precipitated by the rise in memory costs, are being debated by investors, our analysts believe there are several drivers to lead the revenue and earnings outcomes to be much more favorable than currently feared by investors (link).

\- AMZN (\$9.8M bought on 7/29, -0.1z, Figure 24): Amazon reports tomorrow AMC, with our analysts expecting AWS growth acceleration of low-mid 30%’s, higher capex guidance and retail margin expansion (link).

\- MSFT (\$2

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 29 Jul 2026 10:11 PM EDT

Disseminated 29 Jul 2026 10:30 PM EDT
"""
