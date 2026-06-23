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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Weekly Warm-up: Mixed Messages as Warsh Pushes for Fed Credibility

In February, we noted our view that Kevin Warsh was the right choice to fortify market credibility for the Fed, a critical element for the eventual success of the administration's plan to grow out of the debt problem. The rally in S&P/Gold is supportive of that view as is last Wednesday's FOMC meeting.

\- Short-Term Pain for Long-Term Gain...We continue to view the Warsh nomination and subsequent appointment as a market-stabilizing event even if it leads to some short-term turbulence. Following on from a note we wrote in February, the roughly 40% rise in the S&P 500/Gold ratio since his nomination reinforces our view that markets are giving him the benefit of the doubt. Specifically, we think markets are signaling that Warsh can shake up the Fed, reduce reliance on the balance sheet as a policy tool, and help re-establish confidence in policy makers. Last Wednesday's price action suggests that transition is off to a good start, but could be a bit messy for stocks in the short term alongside the initial reaction of a sharp bear flattening of the yield curve, a stronger dollar and weak precious metal prices.

\- Kevin Warsh's First Fed Meeting Marked an Important Step Toward Restoring Credibility...In our view, Warsh made it clear that the Fed's primary mandate is inflation, not labor markets or growth, and his willingness to call out the Fed's repeated misses on its inflation target suggests there is a new sheriff in town who intends to enforce that mandate. The stronger economy and jobs market provides the Fed with an opportunity to lean into the inflation mandate and that's what they appear to be doing. We do not think this means the Fed will raise rates immediately, or even this year, but markets don't like uncertainty and may struggle with the transition in the near term. We also applaud Warsh's move away from excessive forward guidance and toward greater reliance on market signals. We have long argued that the Fed has become too influential in shaping not only market behavior, but also how investors interpret the data. Letting markets react more freely to incoming information should give the Fed better signals and improve the quality and timing of its decision-making.

\- We See Liquidity, Rather than Rate Hikes, As the More Important Near-Term Risk for Equities...Balance-sheet support has already begun to fade with the RMP down 75% from peak. Treasury buybacks have been reduced, while lending growth is accelerating to fund a strong economy and capital

MS & CO. LLC
Michael J Wilson
Equity Strategist
M.Wilson@morganstanley.com +1 212 761-2532

Andrew B Pauker
Equity Strategist
Andrew.Pauker@morganstanley.com +1 212 761-1330

Diane Ding, Ph.D.
Quantitative Strategist
Qian.Ding@morganstanley.com +1 212 761-6758

Nicholas Lentini, CFA
Equity Strategist
Nick.Lentini@morganstanley.com +1 212 761-5863

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

spending. Net-net, we think liquidity conditions are tightening and may remain a headwind for stocks into July, especially if markets test the Fed's newfound resolve. Peace negotiations with Iran are also likely to play a role in near-term price action, but longer term, we remain bearish on oil prices as this conflict likely drives new sources of supply out of a necessity for energy independence.

\- Ultimately, Earnings Remain the Primary Driver of this Bull Market...Our out of consensus view on the earnings recovery at the beginning of the year is no longer unique, but it's still underappreciated in terms of the breadth and resilience of the data, and earnings are likely to exceed expectations for the full year. This growth has offset the multiple contraction YTD and will likely soften any further blows from tighter monetary policy or uncertainty due to less Fed guidance and/or market challenges of the new Chair.

# Mixed Messages As Warsh Pushes for Fed Credibility

Last week, Kevin Warsh presided over his first Fed meeting as Chairman. While there have been many hints as to how he might steer the Fed going forward, it was a good chance for him to tell the world how dynamics might change from how the Fed has operated in the past. We think there were several key takeaways that were very much in line with our views about how this Fed will be viewed by markets going forward, particularly in the context of current economic and market conditions.

First, in order to set the table, we refer readers to a note we wrote the week after Kevin Warsh was nominated for the Chair position by President Trump back in early February ("Run It Hot" Takes a Detour to Ensure It Reaches Its Destination). We encourage readers to review that note for more details on our thinking. Below is the key message from that report:

\- "The Warsh nomination should be viewed as a market stabilizing event with the recent parabolic rise in precious metals raising questions about the "run it hot" strategy. Friday's price action signals it was the right move as the S&P 500/Gold ratio had one of its best days in history."

At the time, we viewed the selection of Warsh as the right choice to fortify market credibility for the Fed, a critical element for the eventual success of the administration's plan to grow out of the debt problem. The move in precious metals after the Fed began asset purchases again in December suggested markets were questioning the Fed and/or the government's ability to "run it hot" without creating a disorderly move lower in the US dollar or inflationary pressures more broadly. Since the nomination, S&P/Gold ratio is up close to 40 percent—in line with our thinking back in February that stocks were the better hedge against inflation given the outsized move in precious metals. Four weeks later, we suggested the war in Iran might further support that ratio, which was an out of consensus statement at the time. Since then, the S&P 500/Gold ratio is up close to 40 percent, the largest move in over 10 years.

Exhibit 1: S&P 500/Gold Is Up 40% Since Warsh Was Nominated as Fed Chair; We Think This Is a Signal from the Market that Warsh Will Shake Up the Fed and Use Balance Sheet Less as a Policy Tool

![](images/38709a445028b4438973e14f571ffc25e74c5f87fd352552b20af06051c78ff1.jpg)  
Source: Bloomberg, MS

In short, the Warsh nomination was the right choice if the goal is to fortify some questioned credibility for policy makers as evidenced by the moves in precious metals earlier this year and over the past decade. The improvement in the SPX/Gold ratio is a vote of confidence by markets, in our view. But now, the hard part begins—i.e., the new Chair must execute on that mission and deal with what is likely to be pressure from markets to test that resolve. Last week was a positive step in that direction, in our view. More specifically, Chair Warsh was crystal clear about the Fed's primary mandate—i.e., inflation, not labor markets/growth. Recent data on both employment and inflation support this position with private payrolls growing at their fastest pace in years due to the "rolling recovery" and policy changes (OBBBA, tax cuts, DOGE and immigration restrictions), and inflation still running well above target. He even called out the Fed for having missed its inflation target for the past 5 years, suggesting there is a new sheriff in town that will enforce that mandate.

Exhibit 2: Private Payrolls Are Back on the Rise  
![](images/e76d9b0f705aadbe1087a648c8a655ced75ecf06275444a37596555d0ccd98dc.jpg)  
Source: Bloomberg, MS

Exhibit 3: But So Is Inflation  
![](images/7d50462a1d6b0f8171f8d0b906d37049fa46b45ec5a1184d3d63fc9ab5a4436b.jpg)  
Source: Bloomberg, MS

In addition to pivoting the Fed's main reaction function toward inflation, Chair Warsh also indicated that the Fed would no longer provide as much "hand holding" on its policy intentions going forward. More specifically, the Chair did not submit a dot plot projection and indicated the Fed's communication strategy is likely to change going forward. We applaud this move as a means to keep the market on its toes while providing the Fed a greater ability to have shock value, when necessary, in pursuit of its goals.

As the same time, Warsh also indicated he is more focused on the left side of the decimal place when considering inflation. That suggests he might be ok with inflation between 2-3 percent rather than a hard target of 2 percent. While subtle, we think it indicates the Chair is fully aware of the need to run the economy hot to some extent if they have a real chance of managing the debt problem in the long term. In other words, this is going to be a balancing act of letting the economy boom (higher real and nominal GDP growth) while not losing control of the bond market, particularly the back end (both rate levels and volatility).

As usual, we take our cues from the markets in how we interpret this new messaging. As an aside, we found the new Chair's comments about how he uses markets in his own decision making to be very encouraging:

\- "We've dropped forward guidance."

\- "Financial markets perform best when they react to incoming data."

\- "Financial market prices are probably the most important source of information to guide central bankers. But when all the financial markets are doing is reflecting

back what we've said, then we're taking the most important source of information and we're being blind to it."

We could not agree more with these statements. We have been in the camp for years that the Fed has become too influential in how markets not only behave, but how they interpret the actual data because they are trying to also incorporate how the Fed will respond in that process. In short, the increasing use of forward guidance has altered many of the valuable market signals that we find to be more helpful than the Fed's interpretation of the data—i.e., the wisdom of crowd is superior. The Chair went on to say:

\- "I'd like us to create a system where those blinders come off, where markets are following data that they efficiently think is reliable. And they'll be watching data, we'll be watching data. They'll come with better information through market prices to us, we can make more informed decisions."

We agree it is time to rein in these often conflicting opinions designed to "manage" markets. Such efforts can be counterproductive and dilute the true message from markets that could be helpful to the Fed's actual decision making process, thereby increasing its longer term success in achieving its core mandates. While the new Chair did not talk about mission creep at the Fed over the past several decades, we suspect that could also come under review. For example, using balance sheet for economic goals rather than just emergencies and blurring of monetary and fiscal policy.

Having said that, while the Fed may try to narrow its mission back to its statutory boundaries of full employment and more importantly price stability, it's unlikely they will abandon the third mandate of "financial stability" that was informally established in 2010 with the Dodd-Frank Act (more on that later).

Initial market reactions to the Fed meeting were fairly clear last week with both stocks and bonds selling off—i.e., it was viewed as incrementally hawkish. Both front and back end rates rose but the curve bear flattened substantially as 2-year yields rose much more than 10-year yields. The reaction in stocks was risk-off alongside similar moves in gold, silver and bitcoin against a stronger USD. From our perspective, this is a win for the new Fed Chair as he tries to fortify the Fed's credibility around its commitment to price stability and hard money. As noted above, the messaging was somewhat mixed with Warsh talking tough on getting inflation back to target while at the same time acknowledging a "2 handle" is fine—perhaps implicitly signaling 2-2.9 percent is tolerable, if not preferential, given the need to "run it hot".

This leads us to the final point around liquidity. Chair Warsh did not talk much about the Fed's balance sheet other than that there is task force being established to examine its use going forward. Here, we have a view that the balance sheet has been used aggressively this year to manage funding markets and provide liquidity for the increased T-Bill issuance from Treasury. This liquidity has played a positive role in financial markets YTD, in our view. However, as noted on our last two weeklies, the rate of change on these balance sheet provisions has rolled over since the Fed reduced the size of its Reserve Management Program (RMP) from \$40B per month to just \$10B today. Meanwhile, Treasury buybacks that have been funded through greater bill issuance have also been curtailed by about 50% with back-end purchases remaining about flat. Meanwhile, lending growth has accelerated this year thanks to a strong economy/demand for capital and less restrictive

capital requirements on the banks. Net-net, we believe the path on liquidity is already tightening and think it is unlikely to reverse in the absence of funding market stress, higher bond volatility or credit market disruption. In other words, liquidity remains the greater risk to equity markets in the short-term rather than any fears about the Fed raising rates to fight inflation. Our latest proprietary liquidity measure shows this risk for equities is likely to persist into July before subsiding. We will have to see if markets challenge the Fed's current stance on the RMP or the Treasury's current level of buybacks.

Bottom line, we believe last week's Fed meeting set the stage for a new regime under which the Fed may be willing to take some short term pain in markets to establish a higher chance of success in its longer term goals to support the administration's "Run it Hot" / rebalancing strategy. We commend this approach but wonder how it will react if markets test its resolve. It's possible such a test may be forthcoming over the next few weeks as the rate of change on liquidity interacts with the rate of change peak in earnings revisions as discussed in last week's note.

Finally, we're not sure what to make of Thursday's very positive rebound in stocks on the back of the US/Iran deal being signed only to be challenged again based on new headlines over the weekend. As of this writing, the talks are back on which could lead to either a continuation of Thursday's rally or perhaps a sell the news on the premise this situation remains quite fluid. Longer term, we remain bearish on oil prices as this conflict simply highlighted how much excess oil and gas there is in the world and the resiliency of global energy markets. We also believe this conflict highlighted how unacceptable this choke point is going forward. We expect significant action to be taken by countries all over the world to ensure redundancies on oil supplies going forward which may include drilling activities in places thought to be off limits. We think this will keep the forward curve in check and could even act as a positive supply shock going forward that will help the Fed's increased focus on inflation. See the latest views and oil forecasts from our commodities team here.

# Fresh Money Buy List

Exhibit 4: Fresh Money Buy List - Stats & Performance

<table><tr><td rowspan="2">Company Name</td><td rowspan="2">Ticker</td><td rowspan="2">MS Rating</td><td rowspan="2">Sector</td><td rowspan="2">Market Cap ($Bn)</td><td rowspan="2">Price</td><td rowspan="2">MS PT</td><td rowspan="2">% to MS PT</td><td rowspan="2">MS Analyst</td><td rowspan="2">Date Added</td><td colspan="2">Total Return Since Inclusion</td></tr><tr><td>Absolute</td><td>Rel. to S&amp;P</td></tr><tr><td>Abbvie Inc.</td><td>ABBV</td><td>Overweight</td><td>Health Care</td><td>$397.6</td><td>$225.02</td><td>278.00</td><td>23.5%</td><td>Flynn, Terence</td><td>8/12/2024</td><td>27.1%</td><td>(15.2%)</td></tr><tr><td>American Tower Corp.</td><td>AMT</td><td>Overweight</td><td>Real Estate</td><td>$89.7</td><td>$192.50</td><td>220.00</td><td>14.3%</td><td>McVeigh, Cameron</td><td>4/7/2025</td><td>(10.2%)</td><td>(58.7%)</td></tr><tr><td>CenterPoint Energy Inc</td><td>CNP</td><td>Equal-Weight</td><td>Utilities</td><td>$27.9</td><td>$42.73</td><td>39.00</td><td>(8.7%)</td><td>Arcaro, David</td><td>3/21/2022</td><td>64.3%</td><td>(12.6%)</td></tr><tr><td>Delta Airlines, Inc.</td><td>DAL</td><td>Overweight</td><td>Industrials</td><td>$50.3</td><td>$76.49</td><td>105.00</td><td>37.3%</td><td>Shanker, Ravi</td><td>11/17/2025</td><td>43.0%</td><td>31.8%</td></tr><tr><td>EQT Corp.</td><td>EQT</td><td>Overweight</td><td>Energy</td><td>$32.9</td><td>$52.62</td><td>74.00</td><td>40.6%</td><td>McDermott, Devin</td><td>11/17/2025</td><td>(12.8%)</td><td>(24.0%)</td></tr><tr><td>Knight-Swift Transportation Holdings Inc</td><td>KNX</td><td>Overweight</td><td>Industrials</td><td>$12.9</td><td>$79.27</td><td>70.00</td><td>(11.7%)</td><td>Shanker, Ravi</td><td>11/17/2025</td><td>91.5%</td><td>80.4%</td></tr><tr><td>Northrop Grumman Corp.</td><td>NOC</td><td>Overweight</td><td>Industrials</td><td>$77.0</td><td>$542.14</td><td>745.00</td><td>37.4%</td><td>Liwag, Kristine</td><td>8/12/2024</td><td>15.1%</td><td>(27.2%)</td></tr><tr><td>Atlassian Corporation PLC</td><td>TEAM</td><td>Overweight</td><td>Information Technology</td><td>$23.3</td><td>$91.54</td><td>120.00</td><td>31.1%</td><td>Singh, Sanjit</td><td>11/17/2025</td><td>(41.7%)</td><td>(52.9%)</td></tr><tr><td>Target Corp</td><td>TGT</td><td>Overweight</td><td>Consumer Staples</td><td>$58.1</td><td>$127.95</td><td>150.00</td><td>17.2%</td><td>Gutman, Simeon</td><td>11/17/2025</td><td>53.3%</td><td>42.2%</td></tr><tr><td>Walmart Inc.</td><td>WMT</td><td>Overweight</td><td>Consumer Staples</td><td>$959.7</td><td>$120.59</td><td>140.00</td><td>16.1%</td><td>Gutman, Simeon</td><td>3/27/2023</td><td>165.6%</td><td>70.1%</td></tr><tr><td colspan="12">Current List Performance</td></tr><tr><td>Average (Eq. Weight)</td><td></td><td></td><td></td><td>$172.9</td><td></td><td></td><td>19.7%</td><td></td><td></td><td>39.51%</td><td>3.39%</td></tr><tr><td>Median</td><td></td><td></td><td></td><td>$54.2</td><td></td><td></td><td>20.4%</td><td></td><td></td><td>35.0%</td><td>(13.9%)</td></tr><tr><td>% Positive Returns (Abs. / Rel.)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>70%</td><td>40%</td></tr><tr><td>% Negative Returns (Abs. / Rel.)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></

[中间内容因长度限制已省略]

onal Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
