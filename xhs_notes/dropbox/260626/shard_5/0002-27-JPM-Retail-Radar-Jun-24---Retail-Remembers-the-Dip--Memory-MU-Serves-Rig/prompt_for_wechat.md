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

<table><tr><td>Ticker</td><td>Name</td><td>Mkt Cap ($B)</td><td>Social Interest Score</td><td>Median Short Interest (% float)</td><td>Extreme Imbalance 1D Z</td><td>Date of Imbalance</td></tr><tr><td>ACM</td><td>AECOM</td><td>8.9</td><td>38.9</td><td>5.1%</td><td>0.9</td><td>17-Jun</td></tr><tr><td>SNAP</td><td>Snap Inc</td><td>7.4</td><td>37.5</td><td>10.3%</td><td>0.7</td><td>17-Jun</td></tr><tr><td>ACN</td><td>Accenture PLC</td><td>78.1</td><td>35.5</td><td>4.3%</td><td>5.1</td><td>18-Jun</td></tr><tr><td>SMCI</td><td>Super Micro Computer Inc</td><td>21.6</td><td>35.0</td><td>13.9%</td><td>1.5</td><td>17-Jun</td></tr><tr><td>PLTR</td><td>Palantir Technologies Inc</td><td>279.8</td><td>33.7</td><td>3.2%</td><td>-0.7</td><td>23-Jun</td></tr><tr><td>SMR</td><td>NuScale Power Corp</td><td>4.0</td><td>33.2</td><td>17.6%</td><td>-1.5</td><td>17-Jun</td></tr><tr><td>MU</td><td>Micron Technology Inc</td><td>1186.1</td><td>32.8</td><td>3.3%</td><td>1.6</td><td>18-Jun</td></tr><tr><td>JD</td><td>JD.com Inc</td><td>35.7</td><td>32.7</td><td>2.6%</td><td>0.5</td><td>23-Jun</td></tr><tr><td>IREN</td><td>IREN Ltd</td><td>19.6</td><td>32.4</td><td>17.8%</td><td>-1.4</td><td>23-Jun</td></tr><tr><td>NBIS</td><td>Nebius Group NV</td><td>69.9</td><td>32.4</td><td>21.6%</td><td>-2.7</td><td>23-Jun</td></tr><tr><td>AMD</td><td>Advanced Micro Devices Inc</td><td>847.7</td><td>32.2</td><td>2.7%</td><td>-1.1</td><td>22-Jun</td></tr><tr><td>RDDT</td><td>Reddit Inc</td><td>31.9</td><td>32.0</td><td>9.7%</td><td>-0.4</td><td>18-Jun</td></tr><tr><td>ASTS</td><td>AST SpaceMobile Inc</td><td>28.3</td><td>31.9</td><td>31.6%</td><td>2.2</td><td>18-Jun</td></tr><tr><td>MRVL</td><td>Marvell Technology Inc</td><td>244.1</td><td>31.7</td><td>4.2%</td><td>3.5</td><td>18-Jun</td></tr><tr><td>PDD</td><td>PDD Holdings Inc</td><td>109.0</td><td>31.3</td><td>2.5%</td><td>-0.9</td><td>18-Jun</td></tr><tr><td>MSFT</td><td>Microsoft Corp</td><td>2777.8</td><td>31.3</td><td>1.2%</td><td>0.9</td><td>17-Jun</td></tr><tr><td>SWBI</td><td>Smith &amp; Wesson Brands Inc</td><td>0.7</td><td>31.1</td><td>3.7%</td><td>-1.7</td><td>22-Jun</td></tr><tr><td>RKLB</td><td>Rocket Lab Corp</td><td>59.4</td><td>31.0</td><td>5.5%</td><td>-0.6</td><td>23-Jun</td></tr><tr><td>NVDA</td><td>NVIDIA Corp</td><td>4841.0</td><td>30.1</td><td>1.2%</td><td>-0.7</td><td>18-Jun</td></tr><tr><td>AVGO</td><td>Broadcom Inc</td><td>1808.6</td><td>29.5</td><td>1.3%</td><td>-0.7</td><td>17-Jun</td></tr></table>

Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Positive Slope = Opposite Positioning (Heightened Risk of Short Squeeze or Retail Losses); Negative Slope = Similar Positioning (Diffusing Squeeze Risk)

![](images/f30309cfdbfbd69a7fc748c0f0ac025a67af6d34b01e9c2e66466889411c0708.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 18: Retail Activity in BIRD  
![](images/9bc2395e88bd87c36a677ea0f3aa18d7dccc2ca813936ebc0644e14b0b664905.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 19: Retail Activity in CPB  
![](images/389f94aeee16583af1c90187292dd68c9b15769d221e10b4269b6469703fb3f9.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 20: Retail Activity in ODD  
![](images/e94867fd4202d31b6a4479ffadf21e302550e33797fa45a9342bc1d9bf413b5b.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Macro & Fundamental Stories
Figure 21: Retail Imbalance in SNDK
As of June 24 $^{th}$  
![](images/ba4a47d6ff567ad19da2c05b5a82a16dab6f97d5141151f790a034e3d18b9fb2.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 22: Cumulative Retail Imbalance in SNDK
As of June 24 $^{th}$  
![](images/91cbf5ef383a1e4b3e7aa87bdf1709dbaefde14783a22305f2dc966a889fd91b.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 23: Retail Imbalance in MU  
![](images/dd499cacefa299cee0c13658e63060c0fca3f3d1cce35d70c1fbfb4957cd3f1e.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 24: Cumulative Retail Imbalance in MU


[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 24 Jun 2026 10:20 PM EDT

Disseminated 24 Jun 2026 10:20 PM EDT
"""
