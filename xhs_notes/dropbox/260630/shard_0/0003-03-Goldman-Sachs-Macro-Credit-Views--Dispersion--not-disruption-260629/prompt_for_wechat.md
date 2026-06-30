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
# Macro Credit Views: Dispersion, not disruption

The directional view: Some modest spread widening, albeit contained by the ‘yield-based bid’. For corporate credit investors, a key area of relative value ‘tension’ has been front-and-center in discussions: spreads are (still) tight by historical standards, while all-in yields are attractive due to elevated risk-free rates (Exhibit 1). We believe the resilience (tightness) of IG corporate credit spreads is directly related to the depth of demand from ‘yield-based’ buyers such as pensions and insurers. For example, in the USD corporate bond market, we estimate this cohort of investors owns at least 40% of the notional outstanding. And beyond the current (and large) size of these holdings, we see scope for allocations to high quality corporate credit to grow further, owing to consistent improvements in pensions’ funded ratios, and the favorable comparison of USD IG long-end yields (5.7%) vs. the US life insurance industry’s average yield for its bond portfolio (4.8%, per the most recent disclosure). This is a key reason why we expect only modest spread widening in the USD and EUR markets (above and beyond the early signs of spread widening visible last week), despite valuations which screen tight vs. history—especially considering the elevated supply backdrop that we expect.

Exhibit 1: Credit spreads are hovering at the tight end of the historical range, while all-in yields are elevated
Index-level spreads (left panel) and yields (right panel) for the Bloomberg USD and EUR IG Corporate indices  
![](images/46763dcf3bd754775f69ee25bbae67cba0e5edc90f86440f31d80b0862812318.jpg)  
Note: As of June 26, 2026.

![](images/624c779930b13b534a73146e30c97e9cb9f0def8a9d5e9469b02620e75940905.jpg)  
Source: Bloomberg, GS Global Investment Research

Rates are likely to remain in the driver's seat—especially in IG. The combination of tight spreads and elevated risk-free rates means that a large portion of relative value in the corporate credit market is now determined by the interest rate backdrop. As shown in Exhibit 2, from 2010 to 2021, USD IG spreads represented, on average, $43\%$ of all-in yields; today, they represent just $15\%$ . In the USD HY market, credit spreads represent a larger role in the overall relative value calculus, but the same directional pattern is visible: spreads generated $73\%$ of all-in yields from 2010 to 2021, vs. $39\%$ today. In the EUR HY market, the shift is even more pronounced, considering the years of extremely low (or negative) interest rates in the region. EUR IG spreads represented $84\%$ of all-in yields from 2010 to 2021 vs. just $23\%$ today, while EUR HY fell from $88\%$ to $47\%$ over the same horizon. Our rates strategists expect the 10-year US Treasury and German Bund to be range bound through year-end 2026, closing the year at $4.4\%$ and $3.0\%$ , respectively. This should keep IG spreads anchored, given the yield-based technical tailwind. That said, the level of rate volatility is important to monitor, given its higher correlation with credit spreads as of late. If rate volatility increases meaningfully, we would expect credit investors to demand additional risk premia in the form of wider credit spreads. Flattening in the US Treasury curve has also resulted in some modest steepening in credit spread curves.

Exhibit 2: With risk-free rates elevated vs. history, USD and EUR credit spreads now reflect a much smaller portion of total all-in yields vs. the 2010-2021 average
The share of index-level all-in yield represented by the credit spread  
![](images/763a7ee8302a66dfe018eba2056b51815d4757ace4cafb45046f11d1b390b36b.jpg)  
Note: As of June 26, 2026.  
Source: Bloomberg, GS Global Investment Research

The outperformance of USD credit vs. EUR should persist, but the regional lines are blurring. So far this year, excess returns in the USD IG and HY markets have slightly outperformed their EUR peers, although the gap has narrowed in recent days (Exhibit 3). Our current spread forecasts reflect some additional underperformance of the EUR market vs. USD, driven by a somewhat less favorable growth, inflation and monetary policy mix in the Euro area. We also anticipate some modest decompression in the EUR market (underperformance of HY spreads, relative to IG), as the recent ECB rate hike (with a 2 $^{nd}$ hike possible) is an unwelcome development for financially stretched firms navigating other macro headwinds. That said, the regional preference for USD credit is modest. More importantly, the lines are blurring across regions, given the increased frequency of cross-border debt issuance in recent years. For example, US-based firms have generated more than 17% of total EUR IG debt issuance so far this year, which is the highest share since 2017. As a result, the regional exposures in the credit market are not as ‘siloed’ as they have been. We expect the pattern of increased fluidity across geographies to gain further momentum as US-based firms—especially those in the Technology sector—utilize financing capacity in a range of ex-USD corporate credit markets.

Exhibit 3: In both the IG and HY markets, USD credit has slightly outperformed its EUR peer on an excess return basis

Year-to-date excess returns for the Bloomberg IG and HY Corporate indices (USD and EUR markets)

![](images/6f1ab37a756db1f7db80fbb55faa2feb428630b5e1a24331cc7e6232ae24ef6b.jpg)  
Source: Bloomberg, GS Global Investment Research

We prefer to move down in quality in USD IG. One of our key relative value views in the USD IG market has been a preference for BBBs vs. the higher-rated AA and A cohorts, as a way for investors to capture incremental spread without sacrificing too much on fundamental credit quality. In fact, we continue to see the most scope for balance sheet deterioration within the high-end of the IG rating spectrum, where many balance sheets are likely under-leveraged and appear poised to shift capital allocation priorities to favor more debt issuance (this has been most visible in subsets of the Technology sector). As Exhibit 4 illustrates, BBBs have outperformed on an excess return basis so far this year, with a performance gap becoming visible in late April and widening since. We believe the supply backdrop has played a key role in this performance differential. So far this year, issuance from firms rated AA- or higher has represented 22% of total USD IG gross issuance—the highest share since 2017. And firms in the BBB cohort (across all three notches) have generated 35% of supply—below the 39% average of the past several years. In the EUR market, the AA cohort has also lagged its lower-rated peers. Here too, the supply patterns are likely a key driver. Firms rated AA- and higher generated 13% of year-to-date EUR IG supply (vs. an average of 10% for the last several years). Meanwhile, issuance from BBB firms has represented 38% of total EUR IG supply—the lowest share since 2015. In the EUR IG market, we have a slight preference for As over BBBs (given the weaker macro backdrop), but would not move too far up the quality spectrum, as we expect AA supply technicals will become a more pronounced headwind over time.

Exhibit 4: BBBs have been the best performing rating cohort across IG, year-to-date
Year-to-date cumulative excess returns for the rating specific cohorts of the Bloomberg USD (left panel) and EUR (right panel) IG Corporate indices

![](images/8b2ea136f4000c0444d7f865e232c63c4c993349b4d97e9e5f6c53893475d30c.jpg)  
Note: As of June 26, 2026. We exclude AAAs due to very small market sizing in both regions.  
Source: Bloomberg, GS Global Investment Research

![](images/ee40700b107946cea8925a7abf820940337718771b4b6ad19e287e280f0258be.jpg)

Dispersion: A tale of two markets. Despite the tight band of index-level spread valuations across a range of markets, dispersion is evident under the surface—especially in HY (Exhibit 5). While the first instinct may be to attribute the increase in HY dispersion to the idiosyncratic CCC cohort (where aggregate spreads have underperformed the broader HY market), our recent analysis revealed that dispersion is elevated even among BBs (i.e., the 'high end' of the HY rating spectrum). This suggests the gap between the strongest and weakest HY credits is wide and likely driven more by fundamentals than by technicals. As a result, security selection remains critical—especially when navigating (avoiding) potential asymmetric downside situations. The ongoing AI-related financing wave, and parsing potential disruption from the technology, is likely to keep dispersion elevated, in our view. In USD HY, we are overweight BBs, neutral CCCs, and underweight Bs, driven in large part by our estimates of the credit risk premia (after accounting for expected losses) embedded in each rating cohort. In EUR HY, we continue to take a more cautious stance, and are overweight BBs, neutral Bs, and underweight CCCs. And while many traditional dispersion metrics in the IG market have been contained, the ongoing wave of AI-related financing is becoming a more influential driver of performance for some sectors and issuers, and is already a driver of dispersion at the ratings level.

Exhibit 5: Bond-level dispersion is near historically compressed levels in IG, while HY dispersion is more elevated
Bond-level ((75th percentile - 25th percentile) / 50th percentile) dispersion for EUR and USD IG (left panel) and EUR and USD HY (right panel)

![](images/2f0c9084646f24223d66aad09dac00fb2c7f344e26243934a3032bf8528a9bc0.jpg)  
Source: iBoxx, GS Global Investment Research

![](images/91f1f1d95f6a4c31b31de589598a497c1c6e76ee911239940eaf78c914f5c852.jpg)

Supply—risks are skewed to the upside in IG. As shown in Exhibit 6, more than \$1.2 trillion of gross debt has already been issued in the USD IG market so far this year. This 1H2026 total is essentially on par with the full-year issuance volumes from 2022-2023. Beyond the elevated headline figures, two other themes stand out to us. First, the IG Technology sector has represented 20% of total gross supply in the USD market—a new peak. We expect this share to grow further, as hyperscalers continue to utilize debt capacity and increase their index weighting in the USD IG market. While we remain mindful of potential issuer concentration and market saturation constraints, we do not expect them to be binding in the near-term, owing to the low ‘starting points’ for balance sheet leverage. That said, given the magnitude and multi-year nature of the AI-related investment cycle, we believe a range of markets (public and private), structures, and currencies will ultimately be required to satisfy the AI-related capex build out. Second, excluding preferred shares and medium-term notes, the average deal size in the USD IG market has jumped to \$1.6 billion so far in 2026—well above the \$1.0-\$1.1 billion pace which prevailed for the last several years. This increases the risk of technical headwinds during heavy supply periods. The risks to our full-year USD IG gross supply forecast of \$2.1 trillion are skewed to the upside, especially if M&A- and AI-related supply breaks from the typical seasonal pattern and results in a busier than normal summer stretch. Over the long-term, we also see potential for AI-related investment and adoption efforts to place at least some upward pressure on corporate spending needs (across a wide range of sectors), which may warrant additional borrowing in the corporate credit market.

Exhibit 6: Against a backdrop of elevated USD IG issuance, the share of supply from the Technology sector has reached a new high
USD IG supply and the share represented by the Technology sector

![](images/82b5cce440d60072dc07e7236bf25bffb1d490c7776cc2907498a93c848c4bbb.jpg)  
Note: As of June 26, 2026.  
Source: Dealogic (ION Analytics), GS Global Investment Research

Private credit: Our base case is for dispersion, not widespread disruption. While redemption activity among retail-focused private credit vehicles has persisted, investor sentiment toward the broader private credit asset class appears to have improved vs. the first quarter. We attribute this to two key factors. First, we believe market participants have become more familiar with the sizing and structural nuances between retail and institutional private credit vehicles, realizing the limitations of ‘extrapolating’ the retail dynamics to the institutional community. Specifically, the fact that institutional funds—which represent the bulk (85%+) of AUM—do not offer the same redemption capabilities as their retail peers (which are, themselves, typically limited to 5% per quarter). Second, the 1Q2026 performance and fundamental data for the private credit asset class hasn’t highlighted broad deterioration. Using the Cliffwater Direct Lending Index as a proxy for the US direct lending market, Exhibit 7 illustrates that performance in 1Q2026 has outpaced the syndicated leveraged finance markets. Two factors have contributed. First, trailing 12-month realized loss rates in the US direct lending market remain below the historical average (58bp vs. 100bp), and still compare favorably to the yield of the asset class (9.8%). Second, the illiquidity premium in private credit has persisted vs. syndicated markets (albeit it has compressed vs. 2022-2023). Per data from PitchBook LCD, leveraged buyouts (LBOs) financed in the US direct lending market so far this year were done at a roughly 140bp higher spread than those financed in the broadly syndicated loan market.

Exhibit 7: Private credit (using US direct lending as a proxy) outperformed USD HY and leveraged loans on a total return basis in 1Q2026, driven in part by the spread premium vs. syndicated markets

Total return comparisons; green = best performer; red = worst performer

<table><tr><td>Year</td><td>Cliffwater Direct Lending Index (CDLI)</td><td>Bloomberg USD HY Index</td><td>Morningstar / LSTA USD Leveraged Loan Index</td></tr><tr><td>2005</td><td>10.1%</td><td>2.7%</td><td>5.1%</td></tr><tr><td>2006</td><td>13.7%</td><td>11.9%</td><td>6.8%</td></tr><tr><td>2007</td><td>10.2%</td><td>1.9%</td><td>2.0%</td></tr><tr><td>2008</td><td>-6.5%</td><td>-26.2%</td><td>-29.1%</td></tr><tr><td>2009</td><td>13.2%</td><td>58.2%</td><td>51.6%</td></tr><tr><td>2010</td><td>15.8%</td><td>15.1%</td><td>10.1%</td></tr><tr><td>2011</td><td>9.8%</td><td>5.0%</td><td>1.5%</td></tr><tr><td>2012</td><td>14.0%</td><td>15.8%</td><td>9.7%</td></tr><tr><td>2013</td><td>12.7%</td><td>7.4%</td><td>5.3%</td></tr><tr><td>2014</td><td>9.6%</td><td>2.5%</td><td>1.6%</td></tr><tr><td>2015</td><td>5.5%</td><td>-4.5%</td><td>-0.7%</td></tr><tr><td>2016</td><td>11.2%</td><td>17.1%</td><td>10.2%</td></tr><tr><td>2017</td><td>8.6%</td><td>7.5%</td><td>4.1%</td></tr><tr><td>2018</td><td>8.1%</td><td>-2.1%</td><td>0.4%</td></tr><tr><td>2019</td><td>9.0%</td><td>14.3%</td><td>8.6%</td></tr><tr><td>2020</td><td>5.5%</td><td>7.1%</td><td>3.1%</td></tr><tr><td>2021</td><td>12.8%</td><td>5.3%</td><td>5.2%</td></tr><tr><td>2022</td><td>6.3%</td><td>-11.2%</td><td>-0.8%</td></tr><tr><td>2023</td><td>12.1%</td><td>13.5%</td><td>13.3%</td></tr><tr><td>2024</td><td>11.3%</td><td>8.2%</td><td>9.0%</td></tr><tr><td>2025</td><td>9.3%</td><td>8.6%</td><td>5.9%</td></tr><tr><td>1Q2026</td><td>1.1%</td><td>-0.5%</td><td>-0.6%</td></tr></table>

Note: Performance for the CDLI is unlevered and shown gross of fees.  
Source: Cliffwater Direct Lending Index, Bloomberg, PitchBook LCD, Morningstar LSTA, GS Global Investment Research

Directional indicators of potential stress warrant close monitoring, however. Some may argue that the 1Q2026 data in private credit is backward looking—especially with the overhang of potential AI-related disruption in the Software sector. This underscores the importance of monitoring a wide range of metrics for leading indicators of potential financial stress. Two of the most important private-credit-specific signposts, in our view, are 1) the volume of new loans added to non-accrual status, and 2) ‘amended payment-in-kind’, which can often precede non-accrual status. As Exhibit 8 highlights, the combined ‘stress rate’ across these two metrics did increase in 1Q2026, driven by some larger loans placed on non-accrual status. That said, it is not outsized and is occurring against a backdrop where leveraged finance capital markets activity remains robust, as lending markets have been receptive to a wide range of borrowers. Moreover, the growth backdrop, which is just slightly below trend per our economists’ forecasts, should be ‘good enough’ for corporate credit. As it relates to the potential for disruption in the Software sector, both the private credit and broadly syndicated loan (BSL) markets count that industry as the largest index weight. In such a scenario of potential disruption (which has yet to be confirmed), we expect the private credit industry may look to deploy some of its sizable dry powder into strategies focused on opportunistic and special situations lending—as such ‘patient’ capital may prove to be a competitive advantage. Finally, while Fed rate hikes are not the base case of our US economists, incrementally higher debt service costs for floating rate issuers would be an unwelcome development at a time when the BSL and private credit markets are navigating potential disruption risks in the Software sector. As a result, monitoring the reaction function of the central bank will also be key, in our view.

Exhibit 8: Amended PIK and new non-accrual volume are two leading indicator metrics we monitor closely in private credit
Combined ‘stress rate’ for the Cliffwater Direct Lending Index

![](images/93e77b9521b8339565d1972228813d12304320b8a6e67569557e8d88b19dd9f3.jpg)  
Note: Captures data through 1Q2026 (most recent available). ‘Amended PIK’ captures loans which switch from ‘cash pay’ to PIK and are marked below \$96 (as a potential indicator of utilizing PIK in response to financial stress).  
Source: Cliffwater Direct Lending Index, GS Global Investment Research

## Disclosure Appendix

## Reg AC

I, Amanda Lynam, CPA, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Amanda Lynam, CPA GS & Co. LLC.

Unless otherwise stated, the individuals l

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
