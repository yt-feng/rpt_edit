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

Jul 22 – Momentum Cooldown, Hyperscaler Earnings

## Retail Trading Activity Overview

\- Retail flows were moderate last week (35.3%ile), essentially unchanged from the prior week. ETF inflows continued to fade (4%ile from 18%ile), but stronger single-stock activity helped offset some of that softness (71.8%ile from 51%ile). This slowdown in retail engagement aligns with the recent market nervousness around the Momentum drawdown. The factor has unwound sharply over the past month (down 14% on a long vs. short basis across cap-weighted S&P 500 quintiles). The unwind was particularly intense given crowding was at an extreme, Figure 2, signaling a high probability of a factor flash crash (see Mid-Year Outlook). Consistent with that dynamic, the current unwind has featured repeated high-magnitude negative tail events, including a -6 sigma day last Thursday and seven extreme negative-sigma observations (-3 sigma or worse) over the 18 days during this unwind (see Figure 3).

\- Within ETFs, weakness continued to be broad based. Sector flows were particularly soft, Figure 2, with Tech ETF inflows turning negative, Figure 4. The most sold ETFs this week were SOXL (-1.6z) and SMH (-1.6z). Flows into Financial ETFs cooled back to flat after last week's exceptional post-earnings surge, while Crypto ETF inflows were stronger (e.g., BITO: 3.0z). As for Single Stocks, Communications and Tech drove purchases, with SPCX, NVDA, GOOGL/GOOG, TSLA and NU the top five names. The 2Q Earnings season continued with the first Mag-7 companies reporting on Wednesday, see Single Stock Stories with Elevated Retail Activity:

\- What to expect as hyperscaler report this week and next? According to our Earnings Scorecard, “AI capex supercycle remains the dominant theme heading into hyperscaler earnings, with a clear bias towards the upside. Across the group, the key swing factors are AI monetization and returns, where investors are looking for improved monetization across cloud, ads, and enterprise, in addition to token pricing dynamics, frontier model competition and a more volatile macro backdrop where resilient spending could drive guidance upside, even as softer consumer sentiment and renewed military activity could temper some 3Q outlooks.”

\- Retail investors bought GOOGL (1.9z) and TSLA (0.4z) ahead of their earnings announcements on Wednesday. GOOGL, Figure 15, traded down \~4% after Wednesday's announcement. Beyond the hype around potential 2027 capex guidance (Street at \$250B and JPMe at \$290B), the key metric that mattered was Google Cloud growth, which beat expectations (+82% reported vs. buy side +70-75% y/y vs. Street +64%). Capex guidance for this year was increased to \$195-205B (vs. \$180-190B prior), Figure 17. TSLA reported an earnings miss on Wednesday despite strong revenue growth on EV sales due to lower prices and regulatory credits, Figure 17. The stock slightly declined in after hours trading following the announcement.

\- TSMC's 2Q earnings came in better than expected, helped by strong operating leverage (driving margins to $60 + \%$ for the first time), while

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
3/11 - Buying Oil, Selling Energy
3/4 - Cautiously Optimistic

revenue and gross margins came in at the top of the guidance range. The positive surprises came from the revenue guidance upgrade in 2026 and capex upside, along with strong AI demand commentary. Retail involvement was modest over the week (0.3z) as the stock faced some pressure following the announcement, before recovering (link).

\- SMCI drew moderate retail interest (-0.6z on Wednesday, Figure 21) as the shares jumped \~23% on Wednesday, after the server maker issued preliminary quarterly results showing positive surprises coming on gross margins and orders (link).

## Retail Trading Activity in Numbers for the Week: Jul 16 to Jul 22

\- Retail flows were \$5.7B this week, below the 12-month average of \$6.8B/week. Retail investors continued to favor ETFs (+\$3.9B) over Single Stocks (+\$1.8B).

\- Outside of Broad Based Large Cap Equity ETFs (+\$1.4B), retail ETF buying was influenced by Equity Style Dividend (+\$220M), Equity Style Call/Put writing (+220M), Fixed Income – Multi Sector (+\$182M), and International Equity EAFE (Broad Based) (+\$152M).

\- This week, in line with prior weeks, retail investors continued to buy AI datacenters and electrification (JPAMAIDE), Top 30 AI/Datacenter Beneficiaries, Mag 7, Growth, along with AI Software/Product/Monetization, and OBBBA Immediate Expensing Beneficiaries, see Figure 4.

\- Activity in Mag7 this week: Retail investors bought NVDA (+\$412M), TSLA (+\$319M), MSFT (+\$202M), AMZN (+\$177M), and META (+\$21M) and sold AAPL (-\$114M).

\- Outside of Mag7, retail investors favored Communications (+\$535M) and Tech (+\$409M) and were net sellers of Industrials (-\$231M) and Cons. Disc. (-\$226M).

\- Top five retail stocks last week: SPCX (+\$514M), NVDA (+\$412M), GOOGL/GOOG (+\$328M), TSLA (+\$319M), and NU (+\$308M). Bottom 5 retail stocks: AAPL (-\$114M), AAL (-\$107M), SNDK (-\$44M), PYPL (-\$43M), and CBRS (-\$42M).

\- In options, retail share is at highs, Figure 41. The most traded options were in the following names, echoing previous weeks: TSLA, MU, NVDA, AMZN, META, SNDK, AAPL, AMD, GOOGL/GOOG, and MSFT. For the most bought/sold delta and gamma names, see Retail Activity in Options. Also see Retail Investors Options Activity by Sectors.

\- Futures Activity (Non Retail): Over the past week, Futures traders net sold \~\$4.1B, primarily driven by net sales in NQ (\~\$8.3B) and partially offset by net buys in ES (\~\$2.3B) and RTY (\~\$1.9B)

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

Figure 1: Momentum Crowding  
![](images/8db0df2b6030279eb43fee179deb732e5fb9cf86c5d7147cc58238df6e89477e.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 2: Momentum Unwind Now vs Feb-Mar'25  
![](images/0563ff5f7c1972e0cd5869c423d2038436e909f847347c741d0f7dd5eaaed5dd.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 3: Frequent Negative High-Sigma Events in Momentum  
![](images/30b164dca48c6a9d39402cf3fc98fd87e7536090e12bdef2e25dcaec8a24cbda.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 4: Retail Imbalance in Tech ETFs Turned Negative As of July $22^{\text{th}}$  
![](images/b4a12bdb48e7e210e43a9ecb7f6c2f16576458b92638447986569bb21d1e7de2.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 5: Retail Investor Daily Purchases by Stocks and ETFs \$M, as of Jul 22 $^{th}$  
![](images/3d560c23c594665af449fd286dd78190b580f567c77330e81461646aa0a05b3b.jpg)  
2000 - 22-Jan 29-Jan 05-Feb 12-Feb 20-Feb 27-Feb 06-Mar 13-Mar 20-Mar 27-Mar 06-Apr 13-Apr 20-Apr 27-Apr 04-May 11-May 18-May 26-May 02-Jun 09-Jun 16-Jun 24-Jun 01-Jul 09-Jul 16-Jul

Source: JPM Equity Strategy & Quantitative Research

## Retail Cash Activity – Overview

Figure 6: Retail Single Stock Activity by Themes

<table><tr><td colspan="2">Thematic Baskets</td><td colspan="3">Δ in Retail Turnover ($Bn)</td></tr><tr><td>Basket</td><td>Index</td><td>Week Ago</td><td>Month Ago</td><td>YTD</td></tr><tr><td>AI/Datacenter/Electrification</td><td>JPAMAIDE</td><td>1.32</td><td>7.14</td><td>44.72</td></tr><tr><td>S&amp;P 500 Top 30 AI/Datacenter Beneficiaries</td><td>JPRAID30</td><td>1.28</td><td>6.92</td><td>43.67</td></tr><tr><td>Magnificent 7</td><td>Mag7</td><td>1.09</td><td>4.97</td><td>35.32</td></tr><tr><td>Growth</td><td>JPAMGROW</td><td>1.02</td><td>5.92</td><td>42.31</td></tr><tr><td>AI Software/Product/Monetization</td><td>JPAMAISO</td><td>0.90</td><td>3.73</td><td>27.33</td></tr><tr><td>OBBBA Immediate Expensing Beneficiaries</td><td>JPGTIEXB</td><td>0.88</td><td>4.14</td><td>21.25</td></tr><tr><td>Sensitive to Low-End Consumer</td><td>JPRLOWCO</td><td>-0.03</td><td>-0.15</td><td>-1.50</td></tr><tr><td>US Inflation</td><td>JPAMINFL</td><td>-0.05</td><td>-0.16</td><td>-2.03</td></tr><tr><td>Inflation Underperformers</td><td>JPAMINUP</td><td>-0.05</td><td>0.10</td><td>1.09</td></tr><tr><td>Inflation Outperformers</td><td>JPAMINOP</td><td>-0.15</td><td>-0.54</td><td>-3.60</td></tr><tr><td>Trump Deregulation Agenda</td><td>JPRGDREG</td><td>-0.28</td><td>-0.40</td><td>-4.48</td></tr><tr><td>Wage Sensitive</td><td>JPAMWAGG</td><td>-0.47</td><td>0.55</td><td>3.97</td></tr></table>

Figure 7: Retail Cumulative Purchases in Mag 7 + PLTR (\$B)  
![](images/77d8af643d83ff3733a1b66be618ed46e00d865cd3c0ddf12564bfb37e9ed0cf.jpg)

Source: JPM Equity Strategy & Quantitative Research. See report, report, and report for details on above baskets. Note: JPM does not provide research coverage of the baskets mentioned here, and investors should not expect continuous analysis or additional reports relating to them.

Source: JPM Equity Strategy & Quantitative Research  
Figure 8: Retail Single Stock Activity by Sector (\$B)
Activity is dominated by Tech and Cons. Disc.  
![](images/1e22fe47482c699fbc206be749e16a1b5f605cc0f121ead3a7b61e93d07b370d.jpg)  
Source: JPM Equity Strategy & Quantitative Research

Figure 9: Retail ETF Activity by Themes
Buying / Selling of ETFs aggregated by themes, in \$B.  
![](images/866fd4f44ce45cb17fd20fdc6495ccbb2c86d24e675abff9d882b26763c6c82d.jpg)  
Source: JPM Equity Strategy & Quantitative Research

## Single Stock Stories with Elevated Retail Activity

## Hedge Funds vs. Retail: High Short Interest Meme Stocks

\- KOPN (\$0.6M bought last week, 0.4z, Figure 12): The company recently reached three key milestones in its color MicroLED development program under the U.S. government's Industrial Base Analysis and Sustainment (IBAS) initiative. Retail flows have increased since May 2026, with net purchases totaling \$14M, alongside rising short interest of \~16% of float, up 6% over the same period.

\- ONDS (\$134.2M bought last week, 4.3z, Figure 13): The company secured a \$6.9M order from the Australian Department of Defence for its DTIM Operator, contributing to an 11.5\% rise in the share price. The stock has been on retail investors' radar since January 2026, with net inflows totaling \$600M, amid elevated short interest of \~42\% of float, up 20\% over the same period.

\- WYFI (\$1.2M bought last week, 0.4z, Figure 14): The company reported initial R&D test results for its cross–data center networking solution, indicating successful outcomes. Retail investors have purchased \$20M since late May 2026, alongside high short interest of \~50% of float, up 15% over the same period.

## Earnings Stories

For more details on this earnings season, please see Hyperscalers vs. AI Hardware.

\- GOOGL (\$74.7M bought on 7/22, 1.9z, Figure 15): Google reported earnings this afternoon, trading down \~4% after market close. Beyond the hype around potential 2027 capex guidance (Street at \$250B and JPMe at \$290B), the key metric that mattered was Google Cloud growth, which beat expectations (+82% reported vs. buy side +70-75% y/y vs. Street +64%). Capex guidance for this year was increased to \$195-205B (vs. \$180-190B prior).

\- TSLA (\$101M bought on 7/22, 0.4z, Figure 17): Tesla reported an earnings miss this afternoon despite strong revenue growth on EV sales due to lower prices and regulatory credits. The stock slightly declined in after hours trading following the announcement.

\- SCHW (\$1.3M bought on 7/21, 0.5z, Figure 19): Charles Schwab reported a solid 2Q26 beat and raised its full-year guidance, supported by better top line and steady expense management. While the muted stock reaction suggested near-term expectations were looking for more, our analysts highlight tailwinds supportive of more growth ahead in the back half of the year (link).

\- SMCI (\$0.8M bought on 7/21, 0.1z, Figure 21): Super Micro published preliminary results, revising their revenue guide toward the lower end of the prior, but with positive surprises coming on gross margins (guidance up by +7-9% vs. prior) and orders. The stock is up +23% since the announcement (link).

\- TSMC: TSMC's 2Q earnings came in better than expected, helped by strong operating leverage (driving margins to $60 + \%$ for the first time), while revenue and GMs came in at the top of the guidance range. The positive surprises came from the revenue guidance upgrade (to $40 + \%$ y/y) in 2026 and the capex upside ( $\$ 60 - 64$ B in 2026, with significant upside in 2027/28 as well), and strong AI demand commentary, suggesting AI demand trends are likely to remain strong into 2029-30. The stock faced some pressure following the announcement but has since recovered (link).

\- UNH (\$11.7M sold on 7/16, -0.5z, Figure 23): UnitedHealth beat and guidance was meaningfully revised upward. All four business lines outperformed expectations. The stock reaction was muted (link).

\- GE (\$4.4M bought on 7/16, 0.8z, Figure 25): Expectations were more elevated than usual for 2Q results, with GE Aerospace's stock underperforming despite good numbers and higher guidance. The key issue for investors is the trajectory of highly profitable CES Services sales, where the outsized growth of recent quarters has sparked some debate about the shape and stock impact of an inevitable deceleration. Margins and cash flow are also in focus (link).

\- NFLX (\$22.3M bought on 7/16, 0.3z, Figure 27): Netflix's stock traded down \~9% post-earnings on concerns around engagement, monetization, and returns on content spending. Nonetheless, strong revenue and profit growth continued (link).

\- ABT (\$7.1M sold on 7/16, -1.3z, Figure 29): Abbott Laboratories reported better than expected 2Q26 results, beating on both the top and bottom line and raising guidance for the latter. The stock was up +11% following the be

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 22 Jul 2026 08:15 PM EDT

Disseminated 22 Jul 2026 08:15 PM EDT
"""
