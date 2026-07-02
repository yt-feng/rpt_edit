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
![](images/943387e86f3b031fd31e80c19f096388248d48c1a338433f3

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
