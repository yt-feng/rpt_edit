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

<table><tr><td>Ticker</td><td>Name</td><td>Mkt Cap ($B)</td><td>Social Interest Score</td><td>Median Short Interest (% float)</td><td>Extreme Imbalance 1D Z</td><td>Date of Imbalance</td></tr><tr><td>WEN</td><td>Wendy&#x27;s Co/The</td><td>1.6</td><td>50.7</td><td>32.4%</td><td>0.9</td><td>24-Jun</td></tr><tr><td>ASTS</td><td>AST SpaceMobile Inc</td><td>34.5</td><td>35.9</td><td>37.5%</td><td>0.7</td><td>24-Jun</td></tr><tr><td>MSTR</td><td>Strategy Inc</td><td>30.5</td><td>33.7</td><td>12.2%</td><td>5.1</td><td>25-Jun</td></tr><tr><td>MU</td><td>Micron Technology Inc</td><td>1303.6</td><td>33.1</td><td>3.7%</td><td>1.5</td><td>24-Jun</td></tr><tr><td>SLS</td><td>SELLAS Life Sciences Group Inc</td><td>2.7</td><td>30.3</td><td>34.7%</td><td>-0.7</td><td>29-Jun</td></tr><tr><td>BB</td><td>BlackBerry Ltd</td><td>7.4</td><td>29.9</td><td>6.4%</td><td>-1.5</td><td>24-Jun</td></tr><tr><td>BABA</td><td>Alibaba Group Holding Ltd</td><td>230.4</td><td>28.8</td><td>1.7%</td><td>1.6</td><td>25-Jun</td></tr><tr><td>RDDT</td><td>Reddit Inc</td><td>33.4</td><td>27.7</td><td>12.0%</td><td>0.5</td><td>29-Jun</td></tr><tr><td>MSFT</td><td>Microsoft Corp</td><td>2771.0</td><td>27.0</td><td>1.3%</td><td>-1.4</td><td>29-Jun</td></tr><tr><td>OPTX</td><td>Syntec Optics Holdings Inc</td><td>0.5</td><td>26.8</td><td>19.0%</td><td>-2.7</td><td>29-Jun</td></tr><tr><td>SNDK</td><td>Sandisk Corp</td><td>336.7</td><td>26.7</td><td>7.5%</td><td>-1.1</td><td>26-Jun</td></tr><tr><td>NOW</td><td>ServiceNow Inc</td><td>102.4</td><td>26.5</td><td>5.8%</td><td>-0.4</td><td>25-Jun</td></tr><tr><td>RCAT</td><td>Red Cat Holdings Inc</td><td>1.6</td><td>25.3</td><td>21.3%</td><td>2.2</td><td>25-Jun</td></tr><tr><td>POET</td><td>POET Technologies Inc</td><td>1.8</td><td>25.2</td><td>15.9%</td><td>3.5</td><td>25-Jun</td></tr><tr><td>AMPX</td><td>Amprius Technologies Inc</td><td>2.0</td><td>25.1</td><td>17.4%</td><td>-0.9</td><td>25-Jun</td></tr><tr><td>NVDA</td><td>NVIDIA Corp</td><td>4842.2</td><td>25.0</td><td>1.3%</td><td>0.9</td><td>24-Jun</td></tr><tr><td>META</td><td>Meta Platforms Inc</td><td>1429.9</td><td>25.0</td><td>1.3%</td><td>-1.7</td><td>26-Jun</td></tr><tr><td>CEG</td><td>Constellation Energy Corp</td><td>90.0</td><td>24.5</td><td>3.3%</td><td>-0.6</td><td>29-Jun</td></tr><tr><td>ONDS</td><td>Ondas Inc</td><td>4.3</td><td>24.2</td><td>35.3%</td><td>-0.7</td><td>25-Jun</td></tr><tr><td>GOOGL</td><td>Alphabet Inc</td><td>4327.0</td><td>23.4</td><td>1.5%</td><td>-0.7</td><td>24-Jun</td></tr></table>

Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 11: Increasing Squeeze Risk in Meme Stocks: Retail Buying in High Short Interest Names  
Positive Slope = Opposite Positioning (Heightened Risk of Short Squeeze or Retail Losses); Negative Slope = Similar Positioning (Diffusing Squeeze Risk)  
![](images/d6d51f9df1b841ff52afe6900da8e59d910290ef4c9bcbba17bb2fc5045f4391.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 12: Retail Activity in QXO  
![](images/de39a7f9d88f8bee909fe6386d705fd44b5b693c8a10ce62e016583570d66988.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 13: Retail Activity in VELO  
![](images/1a9443303e5ed9a8deb81ac290fb52aa4fc50e73d00b83d0a9ab79cd565d563a.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 14: Retail Activity in ARES  
![](images/5f9ab3de5e4d0cc67b85c442a85a78c14db081ae929712006d009fba913d0741.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners

## Macro & Fundamental Stories

![](images/794565b6eeb6f27c298fe87cefa28204ca364d00abbff11457d25814bcd7cc3c.jpg)  
Source: JPM Equity Strategy & Quantitative Research, S3 Partners  
Figure 17: Retail Imbalance in TMUS

Figure 16: Cumulative Retail Imbalance in VZ
As of June 30 $^{th}$  
![](images/66bac46140d47638cb7d6ae8dadc06ff3df7ddc9bf5f040e94790e8d2fc7d2ef.jpg)  
Source: JPM Equity Strat

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 01 Jul 2026 10:43 PM EDT

Disseminated 01 Jul 2026 10:43 PM EDT
"""
