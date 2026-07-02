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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# US Macroscope: Decomposing recent Russell 2000 outperformance and the second-half outlook for small caps

The Russell 2000 has returned $23\%$ in the first half of 2026 and $41\%$ during the past 12 months, its strongest returns since the COVID rebound. The small-cap index has generated roughly 2x the S&P 500 return on trailing 6- and 12-month bases. However, this outperformance represents just a modest reversal following nearly 300 percentage points of Russell 2000 underperformance vs. the S&P 500 during the past 15 years.

The AI trade has been a major driver of recent small-cap strength. AI infrastructure stocks have contributed roughly $40\%$ of the YTD return for the Russell 2000. Small caps have also benefited relative to the S&P 500 by avoiding the drag from the Magnificent 7, which returned $0\%$ in H1 2026. However, last week's index reconstitution cut the weight of AI infrastructure stocks in the Russell 2000 from $15\%$ to $7\%$ , including the removal of some of the largest contributors to the index's YTD return.

■ Outside of AI, a healthy economic backdrop and surging healthcare M&A have also been factors behind the recent Russell 2000 strength. Russell 2000 stocks have outperformed S&P 500 companies in 9 of 11 sectors YTD. Outside of TMT, the largest contributors have been cyclical sectors, including Industrials and Financials. Among industries, Biotechnology has the largest weight in the Russell 2000 relative to the S&P 500 and has contributed $10\%$ of the YTD return.

Consensus estimates show the Russell 2000 growing earnings at twice the rate of the S&P 500 this year, but revisions for the two indices have been moving in opposite directions. Analysts model $48\%$ EPS growth for the Russell 2000 in 2026. This would be the strongest annual growth rate in decades, outside of 2009 and 2021, and twice the $24\%$ EPS growth for the S&P 500. However, analysts have cut Russell 2000 2026 EPS estimates by $9\%$ YTD. Rising valuations have accounted for about half the small-cap return so far in 2026.

The combination of elevated valuations and near-trend US economic growth points to low single-digit Russell 2000 returns in the next 12 months. The biggest upside risk for small-caps is stronger economic or AI capex growth than the market currently prices. On the downside, in addition to disappointing growth, a hawkish Fed would be a particular challenge for small-caps. Nearly $30\%$ of Russell 2000 stocks are unprofitable and $29\%$ of Russell 2000 debt is floating rate.

■ Surging return dispersion within the US equity market signals elevated alpha opportunity, especially among small-caps. Russell 2000 return dispersion has

Ben Snider  
+1(212)357-1744 | ben.snider@gs.com  
GS & Co. LLC

Ryan Hammond +1(212)902-5625 | ryan.hammond@gs.com GS & Co. LLC

Jenny Ma  
+1(212)357-5775 | jenny.ma@gs.com  
GS & Co. LLC

Daniel Chavez +1(212)357-7657 | daniel.chavez@gs.com GS & Co. LLC

Kartik Jayachandran +1(212)855-7744 | kartik.jayachandran@gs.com GS & Co. LLC

Christophe Sung +1(212)902-3841 | christophe.sung@gs.com GS & Co. LLC

averaged roughly 2x the level of S&P 500 dispersion during the past 30 years, and small-cap dispersion currently registers higher in every sector relative to large-caps.

## Why have small-caps performed so well this year?

The Russell 2000 has returned $23\%$ in the first half of 2026, outperforming the S&P 500 by 12 percentage points YTD. This represents one of the strongest semiannual periods of small-cap outperformance during the last 30 years. During the past 12 months, the 18 percentage point excess return of the Russell 2000 vs. the S&P 500 ranks in the 95th percentile since 1995. However, this recent strength reverses only a small portion of the cumulative Russell 2000 underperformance of the past 15 years, during which the S&P 500 has generated nearly twice its total return (680% vs. 375%).

Exhibit 1: The Russell 2000 has outperformed the S&P 500 by 12 pp YTD  
![](images/d3ea978753db79f8c78d3854aea122e86b4aa96b5aa56b5da651a3fa42b19a9f.jpg)  
Source: GS Global Investment Research

Exhibit 2: The Russell 2000 has recently outperformed the S&P 500 but lagged for most of the past decade  
![](images/4abf88143c003d1287d8c598ffb68043cc1681d37b4e945be0945b43e38a665b.jpg)  
Source: GS Global Investment Research

Going forward, Russell 2000 index outperformance will likely fade in the second half of the year, but the small-cap universe should remain exceptionally fertile ground for alpha generation. Coming into 2026, the combination of an accelerating economy and easing Fed created an ideal backdrop for small-caps. Those macro dynamics appear less favorable in the back half of the year. In addition, the AI trade has been a major source of small-cap outperformance, but that tailwind should also fade following the recent rebalance. Valuations and positioning in the Russell 2000 are also less friendly than they were at the start of the year. Nonetheless, small-caps should continue to generate positive returns during the remainder of 2026, and the opportunity set for stock-pickers should remain very attractive.

Three main factors have driven the recent strength of small-cap equities: The AI trade, a robust economic environment, and the surge in biotech stocks. Russell 2000 stocks have outperformed S&P 500 companies in nearly every sector YTD, with Materials and Utilities the exceptions. The performance differential, and contribution to the Russell 2000 YTD return, has been largest in TMT (the Info Tech and Comm Services sectors). The cyclical Financials and Industrials sectors have also been large contributors, as has Health Care.

Exhibit 3: Russell 2000 sector composition and returns vs. S&P 500

<table><tr><td rowspan="3">Sector</td><td colspan="3">Index weight</td><td colspan="3">YTD total return</td><td rowspan="3">Contribution to R2K YTD return</td></tr><tr><td colspan="3">Russell</td><td colspan="3">Russell</td></tr><tr><td>2000</td><td>S&amp;P 500</td><td>Difference</td><td>2000</td><td>S&amp;P 500</td><td>Difference</td></tr><tr><td>Info Tech</td><td>14 %</td><td>37 %</td><td>(24)pp</td><td>49 %</td><td>20 %</td><td>29 pp</td><td>28 %</td></tr><tr><td>Industrials</td><td>15</td><td>9</td><td>6</td><td>28</td><td>20</td><td>8</td><td>24</td></tr><tr><td>Health Care</td><td>20</td><td>9</td><td>11</td><td>19</td><td>3</td><td>16</td><td>14</td></tr><tr><td>Financials</td><td>19</td><td>12</td><td>7</td><td>16</td><td>(1)</td><td>17</td><td>13</td></tr><tr><td>Energy</td><td>6</td><td>3</td><td>3</td><td>22</td><td>20</td><td>3</td><td>6</td></tr><tr><td>Cons Discretionary</td><td>10</td><td>9</td><td>0</td><td>15</td><td>(1)</td><td>16</td><td>5</td></tr><tr><td>Real Estate</td><td>6</td><td>2</td><td>4</td><td>18</td><td>15</td><td>3</td><td>5</td></tr><tr><td>Materials</td><td>4</td><td>2</td><td>2</td><td>9</td><td>12</td><td>(3)</td><td>2</td></tr><tr><td>Comm Services</td><td>2</td><td>10</td><td>(7)</td><td>38</td><td>1</td><td>37</td><td>2</td></tr><tr><td>Cons Staples</td><td>2</td><td>5</td><td>(3)</td><td>9</td><td>8</td><td>1</td><td>1</td></tr><tr><td>Utilities</td><td>3</td><td>2</td><td>0</td><td>0</td><td>8</td><td>(7)</td><td>1</td></tr><tr><td>Total index</td><td>100 %</td><td>100 %</td><td>0 pp</td><td>23 %</td><td>10 %</td><td>12 pp</td><td>100 %</td></tr></table>

Source: FactSet, GS Global Investment Research

One major driver of recent small-cap strength has been the AI trade, with AI infrastructure stocks contributing nearly $40\%$ of the Russell 2000 YTD return. Prior to the recent rebalance, the largest constituents of the Russell 2000 were AI infrastructure stocks (Exhibit 8). In total, semiconductors and constituents of various GS AI infrastructure baskets, including electrical equipment, construction stocks, and others, accounted for $15\%$ of Russell 2000 index weight and $37\%$ of the index return at the halfway point of 2026.

Reflecting the impact of the AI trade, the Russell 2000 has been more correlated with the GS AI basket during the last few months than at any other time since the start of the AI boom in 2023. Likewise, a regression decomposition shows that AI has recently outweighed the cyclical economy as the most significant macro driver of Russell 2000 returns, although economic cyclicality remains the most important driver for the small-cap index on an equal-weight basis.

Exhibit 4: The Russell 2000 has become increasingly correlated with the AI trade

Correlation of daily returns vs. the equal-weight S&P 500; GS AI Basket = GSTMTAIP

![](images/10474f45e47b88f103beaf1ae24baa787e0aa34df636aa4cfafd34c2ee91d899.jpg)  
GSTMTAIP basket developed by GBM

Exhibit 5: Macro drivers of Russell 2000 returns weekly returns vs. equal-weight S&P 500 during the past 12 months

![](images/5cb54c2daef727bb69e450b419c2693ddd10754e630cd611f4e3f9588641eb98.jpg)  
Source: GS Global Investment Research  
Source: GS FICC & Equities, GS Global Investment Research

The Russell 2000 has also benefited from the AI trade relative to the S&P 500 because it has not been affected by the poor recent performance of the largest US tech stocks. The Magnificent 7 returned a collective $0\%$ in H1 2026 vs. $16\%$ for the S&P 493.

However, the small-cap AI tailwind is likely to diminish following the recent index rebalance. The weight of AI infrastructure stocks has declined from $15\%$ prior to last Friday's reconstitution to $7\%$ currently. In addition, we expect revisions to the outlook for AI capex to be less of a catalyst for the AI infrastructure trade this coming earnings season than last quarter.

Exhibit 6: The weight of AI infrastructure stocks in the Russell 2000 has declined following index reconstitution

AI infrastructure stocks include semiconductors and the constituents of various GS AI infrastructure baskets

![](images/489b77eccf7dc166f7225e20cf2ae84284abcc7dc5189c0fa8f3dccaf50c444a.jpg)  
Source: FactSet, GS Global Investment Research

The new largest stocks in the Russell 2000 include a mix of Info Tech, Industrials, Financials, and Health Care. Prior to the rebalance, the top constituents were primarily members of the Info Tech and Industrials sectors. These former top 10 stocks contributed $16\%$ of the Russell 2000 return in H1 2026. Following reconstitution, HUT is now the largest stock in the index, with a weight of $0.4\%$ , compared with BE previously $(1.6\%)$ .

Exhibit 7: Current largest Russell 2000 stocks  
Current largest stocks in the Russell 2000

<table><tr><td>Name</td><td>Ticker</td><td>Sector</td><td>Market cap (bn)</td><td>Index weight</td></tr><tr><td>Hut 8</td><td>HUT</td><td>Info Tech</td><td>$14</td><td>0.4 %</td></tr><tr><td>Moog Inc.</td><td>MOG.A</td><td>Industrials</td><td>13</td><td>0.4</td></tr><tr><td>BrightSpring Health Services</td><td>BTSG</td><td>Health Care</td><td>14</td><td>0.4</td></tr><tr><td>Cytokinetics, Incorporated</td><td>CYTK</td><td>Health Care</td><td>10</td><td>0.3</td></tr><tr><td>UMB Financial</td><td>UMBF</td><td>Financials</td><td>11</td><td>0.3</td></tr><tr><td>Argan</td><td>AGX</td><td>Industrials</td><td>11</td><td>0.3</td></tr><tr><td>Riot Platforms</td><td>RIOT</td><td>Info Tech</td><td>11</td><td>0.3</td></tr><tr><td>StoneX Group Inc.</td><td>SNEX</td><td>Financials</td><td>11</td><td>0.3</td></tr><tr><td>Krystal Biotech</td><td>KRYS</td><td>Health Care</td><td>11</td><td>0.3</td></tr><tr><td>JFrog Ltd.</td><td>FROG</td><td>Info Tech</td><td>11</td><td>0.3</td></tr><tr><td>Top 10</td><td></td><td></td><td>$116</td><td>3.4 %</td></tr></table>

Source: FactSet, GS Global Investment Research

Exhibit 8: Largest Russell 2000 constituents prior to the recent rebalance  
Largest stocks in the Russell 2000 prior to rebalance

<table><tr><td>Name</td><td>Ticker</td><td>Sector</td><td>Market cap (bn)</td><td>Index weight</td></tr><tr><td>Bloom Energy</td><td>BE</td><td>Industrials</td><td>$72</td><td>1.6 %</td></tr><tr><td>Credo Technology Group</td><td>CRDO</td><td>Info Tech</td><td>44</td><td>1.1</td></tr><tr><td>Sterling Infrastructure</td><td>STRL</td><td>Industrials</td><td>25</td><td>0.7</td></tr><tr><td>TTM Technologies</td><td>TTMI</td><td>Info Tech</td><td>20</td><td>0.6</td></tr><tr><td>Fabrinet</td><td>FN</td><td>Info Tech</td><td>19</td><td>0.5</td></tr><tr><td>Guardant Health</td><td>GH</td><td>Health Care</td><td>20</td><td>0.5</td></tr><tr><td>IonQ</td><td>IONQ</td><td>Info Tech</td><td>18</td><td>0.5</td></tr><tr><td>Coeur Mining</td><td>CDE</td><td>Materials</td><td>17</td><td>0.5</td></tr><tr><td>Nextpower Inc.</td><td>NXT</td><td>Industrials</td><td>16</td><td>0.4</td></tr><tr><td>SiTime</td><td>SITM</td><td>Info Tech</td><td>18</td><td>0.4</td></tr><tr><td>Top 10</td><td></td><td></td><td>$268</td><td>6.8 %</td></tr></table>

Source: FactSet, GS Global Investment Research

The health of the cyclical economy is usually the most important macro driver of small-cap US equities, and resilient economic activity has also contributed to the Russell 2000 strength so far this year. Despite the energy shock this spring, US economic data have generally remained solid, with our economists' US Current Activity

Indicator pointing to real growth in the range of 2.5%-3.0% during the past few months and their MAP index signaling positive economic data surprises.

Exhibit 9: US economic data have generally surprised to the upside in recent months, supporting small-caps

![](images/23ac69ca59e9446d0b51267ead7712bd25904b203ff56b33c8fcceff866dfba4.jpg)  
Source: GS Global Investment Research

A wave of healthcare M&A and the large index weight of Biotech have also helped lift the Russell 2000 this year. Biotechnology accounts for 11% of Russell 2000 index weight, a 9 percentage point tilt relative to the S&P 500, and has driven roughly 10% of the small-cap index YTD return. One reason for this strength is the ongoing wave of M&A. Announced US healthcare M&A totaled \$236 billion in the first half of 2026, a 90% increase relative to H1 2025 and the strongest start to a year since 2021.

Exhibit 10: Largest difference in industry weight between the Russell 2000 and the S&P 500  
![](images/abb38eceaf2ff290bda0670d0450ea2f80643733e602919effd413b4efc4f819.jpg)  
Source: FactSet, GS Global Investment Research

Exhibit 11: Announced US Healthcare M&A was up $90\%$ y/y in H1 2026  
![](images/183f36b7ea590787685b1e15f479b2ab59d73cb6f92cc5812facfa01106ea920.jpg)  
Source: Dealogic, GS Global Investment Research

From a fundamental perspective, consensus estimates show the Russell 2000 generating 2x the EPS growth of the S&P 500 this year (48% vs. 24%). If realized, this would be the strongest year of small-cap EPS growth since the COVID recovery in 2021, when index EPS growth exceeded 100%, and prior to that the earnings rebound in 2009.

Exhibit 12: Consensus estimates show the Russell 2000 growing EPS at 2x the rate of the S&P 500 this year and next

![](images/5193613d5dbe5a362db69bf18258fdc60a8bcc8031b5de30cf94e196af5711e6.jpg)  
Source: FactSet, GS Global Investment Research

However, Russell 2000 EPS estimates have recently been falling, in contrast with upward revisions for the S&P 500. YTD, analysts have lifted 2026 EPS estimates for the S&P 500 by $9\%$ while cutting Russell 2000 estimates by $9\%$ . As a result, while the entire S&P 500 YTD return has been driven by near-term earnings, the Russell 2000 YTD return can be attributed in roughly equal parts to growing earnings and rising valuations.

Exhibit 13: Unlike the S&P 500, valuations and earnings have both contributed to the Russell 2000 YTD return  
![](images/610374d1329379ac322b4eaaf29e295a873f565683dabc2bfdbc82509bc51141.jpg)

Exhibit 14: Russell 2000 EPS estimates for 2026 have declined by $9\%$ YTD  
![](images/943387e86f3b031fd31e80c19f096388248d48c1a338433f3c01667bec9dcb01.jpg)  
Source: FactSet, GS Global Investment Research

While analyst estimates point to strong EPS growth, roughly a quarter of the Russell 2000 is unprofitable. Unprofitable stocks represent $29\%$ of Russell 2000 constituents and $23\%$ of market cap. This unprofitable share has trended higher during the past 20

years and increased slightly following last week's rebalance.

Exhibit 15: Roughly a quarter of the Russell 2000 is unprofitable  
![](images/a5da7fc42acb88352028853ec144bd73be2d5295f034697e7b48fdd2d263b874.jpg)  
Source: FactSet, Compustat, GS Global Investment Research

A Fed tightening cycle would pose a bigger risk to small-caps than large-caps. While our economists believe that the Fed will most likely remain on hold for the next few quarters, the market is pricing roughly 35 bp of Fed tightening through year-end. About $30\%$ of Russell 2000 debt is floating rate, compared with $7\%$ for the S&P 500.

Exhibit 16: Russell 2000 stocks have a higher share of floating rate debt than large-caps  
![](images/f1318e0b11485fa630f82d619858a278821608487f22dcbe4cfc5f88e4ad86ce.jpg)  
Source: Bloomberg, GS Global Investment Research

Russell 2000 valuations remain below prior extremes but are less attractive than they were at the start of 2026. Unlike for large-caps, small-cap valuations – and specifically price/book multiples – have historically been a useful indicator for near-term forward returns. Today, the Russell 2000 trades at P/B ratio of 2.4x. This falls below the 2.6x ratio it carried prior to the recent rebalance but above both the long-term average of 2.1x and the 2.2x multiple it carried at the start of 2026.

Exhibit 17: Russell 2000 P/B valuation ranks in the 76th percentile since 1985  
![](images/616ea2b32d86c1fa280e1e90ccef15c8cae8a9520ab51f5a469db7d515677ab0.jpg)  
Source: FactSet, Compustat, GS Global Investment Research

Exhibit 18: Russell 2000 P/E valuation with and without negative earners  
![](images/a48e61a1b2980a0d5a78de2c43b5cbebb0547cc09974b7d78182631f661f4a1e.jpg)  
Source: FactSet, Compustat, GS Global Investment Research

Given elevated valuations, our economists' forecast for real US GDP growth of roughly $2\%$ in coming quarters would signal a low single-digit Russell 2000 return during the next 12 months. The major upside risk to this modeled return would be stronger economic growth than they forecast or continued upside surprises to the AI infrastructure boom. The largest downside risks are that those growth tailwinds disappoint or that the Fed tightens more than the market is currently pricing.

Exhibit 19: Macr

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
