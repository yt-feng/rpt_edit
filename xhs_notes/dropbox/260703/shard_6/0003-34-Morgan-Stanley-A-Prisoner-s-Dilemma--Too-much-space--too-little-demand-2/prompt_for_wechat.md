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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
July 2, 2026 03:00 AM GMT

Retailing - Food | Europe

# A Prisoner's Dilemma: Too much space, too little demand

The Polish grocery sector continues to pump supply into a falling demand backdrop. As the market digests this core supply/demand imbalance, we think earnings and multiples will be forced to rebase downward, with our average EBIT -9% below Street. We restart coverage with JMT, DNP at Underweight. Zabka at Equal-weight.

Poland's food retail market is transitioning to its next life stage, which requires a change in space/competitive strategy or risks depleting industry margins. Our views are counter-consensus and we see significant earnings risk ahead – we restart coverage with EBIT -9% below Street. We think the market fundamentally misunderstands where Polish food retail sits on the maturity curve. The sector needs to digest a shift away from space-driven growth and towards a more mature backdrop, where focus will be on driving up same store sales densities. We do not expect the process to be smooth. In the near term, there is still a race for space and a classic prisoners' dilemma, whereby no-one wants to be the first to pull back on space growth, because this would risk allowing competitors to gain scale at their expense. Our analysis shows that store pipelines among the Modern 5 are down \~4% since 2022, but a much more significant retraction is needed. At the current pace, we think it's likely we see another -5% contraction in volume sales densities as demand simply cannot keep up with supply.

Market is too bullish on both top line and margins and we see downside over a multi-year period. We expect sales to miss forecasts (we are -3% below Cssus on avg in 2028e), both due to space contribution coming down over time, but also due to mature stores generating lower sales than expected, as steep price investments continue and traditional market share funding sources are increasingly exhausted. Returns on capital also appear unlikely to recover to pre-2023 levels, and are more likely to trend further down from here, which leads us to expect further contraction in trading multiples. In addition, Poland faces a structural long-term decline in its population, shrinking \~0.4% pa historically, which directly weighs on volumes, and is only in the early stages of shifting towards digital/omni channel, which will put additional channel mix pressure on margins over time. More near term, we expect another year of intense competition, against a muted demand backdrop (Biedronka back to -3% deflation in its basket as of Q1, industry volumes down -1.4% L3M). Investor narrative is focused on cyclical weakness in volumes / food inflation; however, we think the more pertinent question to ask is – can the market absorb this much capital?

We return to coverage with Underweights on Jeronimo Martins and Dino Polska, and an Equal-weight rating on Zabka; we are materially below Consensus forecasts on all 3. By stock -

MS & CO. INTERNATIONAL PLC+

+44 20 7677-5006

RETAILING - FOOD

Industry View In-Line

Exhibit 1 : Summary of our ratings and key estimates vs Cssus.

<table><tr><td>KPI</td><td>JMT</td><td>DNP</td><td>ZAB</td></tr><tr><td colspan="4">MSe vs Cssus</td></tr><tr><td>Sales 2028e</td><td>(3.4%)</td><td>(2.3%)</td><td>(1.5%)</td></tr><tr><td>EBITDA 2028e</td><td>(3.3%)</td><td>(9.9%)</td><td>(2.5%)</td></tr><tr><td>EPS*</td><td>(8.7%)</td><td>(15.6%)</td><td>(7.7%)</td></tr></table>

<table><tr><td colspan="4">Investment view</td></tr><tr><td>Rating</td><td>Underweight</td><td>Underweight</td><td>Equal-weight</td></tr><tr><td>12m target price</td><td>€ 15.50</td><td>PLN 23.40</td><td>PLN 28.60</td></tr><tr><td>Upside/downside at TP</td><td>(7.5%)</td><td>(17.6%)</td><td>5.1%</td></tr><tr><td>Cssus trading PE</td><td>13.1x</td><td>15.9x</td><td>19.9x</td></tr></table>

Source: MS estimates. \*EPS is shown for 2028e for DNP/ZAB and 2027e for JMT due to Cssus availability. For JMT we show the EPS on a reported basis, due to meaningful lack of comparability in our definition of underlying EPS vs Cssus

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

\- Jeronimo Martins: We think Biedronka (70% sales/ 90% of Group EBIT) is pursuing the right mid-term strategy to defend ROCE and margins. From our perspective, its strategy appears to be to flex its strengths (such as scale economies, balance sheet, payment terms), invest in price aggressively and grab as much volume / space to ensure its relative scale advantage is preserved. In this stage of the food retail life cycle, we would expect to see share concentrating among the top of the pyramid, and we think Biedronka is on track to emerge as the share winner. However all this said, near term we see earnings downside: we think Cssus EBITDA estimates for Biedronka are 6.5% too high by 2028e and valuation multiples are unlikely to recover to 10yr averages. At 12.5x target P/E / 1.5x PEG, we see -8% downside.
Underweight.

\- In the case of Dino Polska, we see even greater share price downside of -18%, due to our earnings being -16% below Cssus. We think greater price investments are needed, creating margin downside, and we also note that DNP is much more reliant on space growth than Biedronka. We'd estimate \~450bp 5yr avg avg space contribution to the LfL of DNP from space ramp-up vs \~100bp for Biedronka, and of the overall 3yr sales growth of Cssus, \~70% is from space for DNP vs \~50% for Biedronka. A slowdown in top line is amplified by rapidly growing opex/capex, given increasing fixed costs through store rollout. Last year SG&A was up 19%, D&A was up 23%, against sales growth of 15%. We think mature store margins will likely exit 2028e below those of Biedronka (vs approximately on par currently). From a multiple standpoint, we think Cssus 12m fwd PE of \~16x is high relative to delivered EPS CAGR of \~5% over 2023-25 (ie since market structural dynamics changed in our view), but also relative to our 2028-26e CAGR of \~11%, considering the stock usually trades around \~1x PEG and pays no dividend. Underweight.

\- Finally, on Zabka – we see it as relatively more insulated from these market dynamics given its channel/product mix (though not immune; our sales are still -1.5% below Cssus). Franchisee economics and Romania expansion likely caps operating leverage upside near term and makes the EBITDA margin outcomes range-bound – our forecast of \~12.9% in 2028e is in line with guidance. Zooming in on the balance sheet, we think management actions on debt refinancing/de-leveraging are a key positive, however reverse factoring exposures were up +21% yoy in 2025, with increased total share of payables, which lead us to have a higher risk perception of the stock. Overall our EPS is \~8% below Cssus by 2028e, but at target P/E of \~19x / 1x PEG, we see the stock as around fair value. Equal-weight.

## Our views in more detail:

Volume growth simply cannot keep up with the level of supply entering the market. Since 2023, space growth has been expanding into a decelerating demand pool, significantly outpacing volume growth. While modern selling space has been growing in the mid SD for much of the past 10 years, historically this has not been a problem, as modern grocery volumes were amplified by share gains from the informal channel – particularly for discounters and the listed group. However, our analysis shows MDG penetration has now plateaued and traditional channels are increasingly exhausted as a funding source. We think either space growth needs to slow, or volumes need to see a material acceleration. It is difficult to see a catalyst for this, considering market volumes were down -1.7%/-0.4% over 2024/25 when real disposable income growth was up \~6% pa, whereas for 2026-28e is projected to be much lower at 3%-2% by the NBP, accompanied by an elevated savings rate of households. In numbers:

\- Selling space in Poland (ie capital invested) by the top 10 "modern formats" has grown with a \~4.5% 10yr CAGR out to 2025, and much of this has come specifically from the Discounter channel (\~5% 10yr CAGR, accelerating to \~7% in the last 5 years). Over the same period, industry volumes were up slightly, \~1% pa on average, including benefits from structural trade up in the mix of basket, as customers sought more convenience.

\- Volumes across the top "Modern 5" grocers (which we define as Biedronka, Lidl, Aldi, Kaufland and Dino Polska) fared much better than the overall market, as they were amplified by channel rotation and share gains, growing with a \~6% CAGR over 10yrs. The key funding sources have been small local grocers and hypermarkets. In other words, for most of the past decade, volume growth across the key modern formats was sufficient to cover for the growth in invested capital.

\- This changed in 2023. Industry space has still been expanding at \~3%-4% pa across modern formats, but volumes have been up only \~2%-3% pa across the top 5, against a broader market backdrop of volumes down -2%. These volume gains were hard won, with an ongoing price war between the key price setters.

Supply has started to come down, but not enough; expansion plans are still budgeted according to pre-2023 structural trends. There were \~570-500 new stores entering the market from the "Modern 5" per year over the last 3 years. The number of net stores has been slowing and is down slightly since 2022, but still needs to meaningfully moderate further to reflect the evolution in market structure. Our analysis shows that if the "Modern 5" wish to keep their sales densities flat (as that is the key driver of ROIC), in aggregate they need to generate \~PLN14bn incremental sales pa or take \~320bp of above-market growth to keep up with supply. We do not think this is realistic, as it implies a pace of share gains which is twice the run-rate of share gains over 2025 which was \~150bp pa. Over the last 3 years deflated sales densities per store are down -4% pa across the Modern 5 as a result. We expect this trend to continue over the mid-term, based on current communicated store opening plans. Key stats:

\- Modern grocery penetration in Poland sits at 85% today according to data from Euromonitor, up from 72% in 2018. Mature markets – such as the UK or Ireland – typically peak at \~90%-94% using the same Euromonitor definition of MDG, and the pace of gains beyond 90% tends to be slow. Over the past 3 years, MDG penetration in Poland has been stagnant, compared to a pre-2023 5yr average of \~260bp share gains per year.

\- In 2025, Biedronka added 152 stores (down -6% y/y) while Dino Polska added 345 stores (up 22% y/y). Lidl, Kaufland and Aldi together added another \~73 stores. Altogether, across these 5 companies, the market supply is around 570 stores entering the market per year, or \~540 if the levels of supply stay in line with the 3 year average. Running forward this level of supply would imply Poland reaches \~95% modern grocery penetration by 2028e, all else equal. This does not sound plausible, given that Poland already has one of the highest levels of discounter penetration in Europe at \~38%.

\- While \~570 stores at first glance may not sound like a large figure relative to the >29k small/independent stores still present in Poland (per Euromonitor), it represents a much more significant amount of sales. The average sales density of a 'modern' format store across these 5 companies is >5.5x higher vs the rest of the market, given their store size and wide SKU range vs traditional stores.

\- As a result, for every 570 modern stores which are added, \~PLN14bn sales need to be generated (i.e. captured away from competitors), if the 'Modern 5' want to keep their sales densities flat. In our view, this is not likely to be possible at current levels of profitability. Indeed, the sales densities gap of the Modern 5 vs the rest of the market has been narrowing over the past 3 years since the supply/demand imbalance began, falling from \~6.0x towards \~5.6x now (and vs a heyday peak of \~8x in 2016).

\- Up until now, the informal channel has served as a clear donor, but over 2025, small grocers/specialists lost only \~50bps of share, while hypers lost \~30bps. This is markedly below the pre-2023 5yr average of \~350bp across the two channels.

Food Retail is effectively a zero sum game: as long as supply exceeds demand, the fight for volumes will continue – driving incremental price investments – until a new equilibrium level is reached. The situation is reminiscent of the post-2010 period in the UK. Grocery demand is borne out of necessity and is generally inelastic to the number of stores present in the market. For volume sale densities to be maintained at the top modern 5 players, there needs to be a funding source. As has been seen in other markets, once MDG penetration flattens, competition then moves between modern players, as each aims to consolidate volume – reflected in the ongoing price war between Biedronka and Lidl. Concentration of modern market share among the top 5 players leaves room for increase vs developed market levels. Therefore, we would expect to see continued steep competition over multiple years as the market concentrates and volume growth is reliant on taking share away from other modern grocers – through price investments. This is a normal stage of evolution in the food retail life cycle.

Race for space: A prisoner's dilemma. One may ask, why keep adding space if demand cannot meet supply? Why not simply pull back? From each grocers' individual lens, their actions are rational; not adding space, while everybody else continues to do so, may deliver a worse competitive outcome for them long-term. A common theme from company communications is that white spots still exist vs their own existing portfolio – Dino Polska is a classic case in point, with bulls on the stock regularly highlighting that it is under-penetrated in certain regions. For example, in Masovia (region of Warsaw), it has only 4.8 stores per 100k inhabitants vs a nationwide avg of Poland which is much higher at 8.3x. Therefore it is true that DNP has

theoretical room to dense up its network in Masovia – however this overlooks the fact that Biedronka, Lidl, Zabka are already heavily present in Masovia and the region is not under-served in aggregate. Similarly, if Biedronka does not open a store in a region where it has 'white space' but a competitor does, it risks the competitor outpacing Biedronka in market share gains and benefiting from incremental scale economies which can then be reinvested in lower prices. In aggregate, these dynamics create a race for space.

Capital allocation: Biedronka's actions are rational from its own perspective. It is a point of debate as to which situation is preferable – a prolonged period of oversupply, gradually depleting profitability lower, or a situation where a strong market leader forces profitability lower for a 1-2 year period for everyone, and therefore forces oversupply to slow, as the market transitions. Over time, this then forces participants to reset strategies and gradually look for ways to repair margins. Squeezing the profitability / cashflows of competitors, for example by offering yoy pay increases above the growth in minimum wage, or tightening supplier terms (eg JMT days payables have come down to \~99 now vs prior peak or \~108) would make sense for a rational actor looking to capture the most of remaining profitable locations / switch volumes. In fact, the strategy is working – Carrefour's Polish operations, as an example, are up for sale and the retailer is looking to exit. In addition, from a Group standpoint, Poland remains a higher ROE region vs other geographies. While Polish profitability may be falling, it is still materially higher versus other regions – in Poland Jeronimo Martins makes EBIT margin of \~5.1% at Biedronka vs in 2.1% Portugal (and EBIT return on assets of 13% vs 4.4%, respectively). Therefore, given its high cash generation, it makes sense that incremental capital would be deployed in the highest earning region. A similar logic holds true for Lidl and its broader DM portfolio, in our view, and has generally been the reason why there is a high presence of international operators in the country (eg French grocers).

Biedronka's and Dino Polska's baskets are back in significant deflation as of Q1, with no signs of competition abating. Our Dlahandlu price tracker, plus companies' disclosures, suggest Biedronka reopened a material price gap vs the market in Q1 this year, on our estimate pricing -7% below the market average, compared to an exit rate of \~4.7% as of 4Q. This tallies with company commentary which suggests that the gap of Biedronka's rate of basket inflation vs peers widened \~from 200bp below the market over 1Q/3Q25 to >500bp in 1Q26 on our maths. Our data suggests these trends have continued over 2Q, with Lidl also responding in turn. Dino Polska is similarly operating with deflation since Q4, and 2%/3% deflation as of Q1, as the company has sharpened its pricing policy, which our price tracker shows has continued Ytd with \~140bp investment in relative price position as of 2QTD vs 2025 avg (and compared to \~270bp at Biedronka). We do not see competition abating any time soon, against a backdrop of muted food inflation for the industry as a whole (MS econ: +1.2% 26e). While food inflation will likely accelerate from Q4 onwards, on the demand side, wage growth in 2027 for the lower income quartile of households is likely to be moderate at \~3% (this is the bucket with highest propensity to consume / highest share of food items in their basket). As a result we think volume growth will remain reliant on share gains and price investments, making it challenging for food retailers to pass on the full extent of input costs.

Jeronimo Martins: Underweight. We think Biedronka (and JMT as a whole) is a fundamentally well-run an

[中间内容因长度限制已省略]

ts contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Retailing - Food

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/01/2026)</td></tr><tr><td colspan="3">Izabel Dobreva</td></tr><tr><td>Carrefour (CARR.PA)</td><td>O (06/22/2026)</td><td>€15.70</td></tr><tr><td>Dino Polska SA (DNP.WA)</td><td>U (06/16/2026)</td><td>PLN 29.00</td></tr><tr><td>Jeronimo Martins SGPS SA (JMT.LS)</td><td>U (06/16/2026)</td><td>€16.76</td></tr><tr><td>J Sainsbury PLC (SBRY.L)</td><td>E (05/18/2026)</td><td>331p</td></tr><tr><td>Koninklijke Ahold Delhaize NV (AD.AS)</td><td>U (06/08/2026)</td><td>€35.16</td></tr><tr><td>Marks and Spencer Group PLC (MKS.L)</td><td>O (05/18/2026)</td><td>376p</td></tr><tr><td>Tesco PLC (TSCO.L)</td><td>O (05/18/2026)</td><td>459p</td></tr><tr><td>Zabka Group (ZAB.WA)</td><td>E (06/16/2026)</td><td>PLN 27.65</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
