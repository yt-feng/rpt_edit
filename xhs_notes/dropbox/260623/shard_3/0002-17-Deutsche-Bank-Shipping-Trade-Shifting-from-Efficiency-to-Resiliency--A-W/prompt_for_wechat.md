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
- 已识别机构名：`DB`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份DB研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
North America
Shipping

Industry
Shipping

Date
22 June 2026

# Trade Shifting from Efficiency to Resiliency: A Win for Shipping and Investors

Last week, we had the opportunity to attend Marine Money Week, a three-day shipping industry conference held each year in New York. The tone at this year's conference was solidly optimistic, especially as it relates to the interplay between deglobalization and heightened geopolitical risk and the possibility of increased tonne-mile demand for vessels across various segments and classes. This note serves as a recap of major themes and takeaways from the conference and presents our thesis that maritime shipping equity assets are an interesting opportunity for investors to hedge against greater geopolitical risk and uncertainty.

The conference reinforced our view that maritime shipping is increasingly being shaped less by classical supply/demand and more by a structural overlay of geopolitics, trade fragmentation, infrastructure bottlenecks, and concerns around energy and supply-chain security. Across the dry bulk, tanker, LPG carrier, and LNG carrier segments, the clearest common thread is that global trade is becoming less efficient as globalization turns towards deglobalization, regionalization, confederation, and self-sufficiency. While these trends may not be great for global peace and stability, they are generally supportive of tonne-mile demand, utilization, and shipping rates.

Our core takeaway is that the shipping industry will continue to benefit from deglobalization trends, including strategic stockpiling of key commodities, the build-out of additional storage infrastructure, and increased regional security concerns around supply chains and energy security. In that vein, we believe that high-quality shipping companies with modern, more fuel-efficient fleets, relatively low reinvestment risk, balance sheet flexibility, and operational spot exposure will benefit in this environment. We continue to have Buy ratings on International Seaways (INSW) and Scorpio Tankers (STNG) in the tanker segment, Buy ratings on Genco (GNK) and Star Bulk Carriers (SBLK) in the dry bulk segment, and a Buy rating on Navigator Gas (NVGS) in the LPG carrier Segment. Beyond the “shipping-as-transport names, we also like the geopolitical backdrop for companies such as Excelerate Energy (EE) and Golar LNG (GLNG) in the marine-based LNG value chain, and Venture Global (VG) in the land-based LNG liquefaction segment.

## Geopolitics is no longer a background variable – it drives trade patterns

Several panel discussions came back to the same point: the shipping market is being reshaped by a world that is becoming less integrated and more security-focused, especially after the latest closure in the Strait of Hormuz and conflicts in the Middle East. Owners and operators expect global trade to evolve towards more regionalization, self-sufficiency, confederation, and/or balkanization. While globalization of trade has been a major driver of cargo volumes, a deglobalization trend may not necessarily imply less trade, but rather longer voyage distances, lower logistical efficiencies, more strategic storage requirements, and higher redundancies in supply chains. This combination should be fundamentally supportive for shipping tonne-mile demand and rates. When voyages are longer, loading/discharge is slower and less efficient, and vessels reroute or avoid unsafe or dangerous regions, the result is the same: less effective available supply.

As it relates to the Strait of Hormuz, tanker owners are looking for the following conditions to be met before returning to the region: 1) a full cessation of hostilities in the region and several weeks or months of no hostile attacks on ships or other marine infrastructure; 2) safe and unrestricted travel conditions that are not hampered by various state or military actors; 3) normalization of insurance prices and availability, and; 4) stabilization in the broader region. One panel participant noted that these conditions have not been met at the current time even if headline diplomacy has improved. Ship owners remain cautious around risks to their crews and to their assets. Owners believe that the current conflict will encourage additional investment in storage infrastructure in various countries and regions as a way to further bolster strategic oil reserves. The peace agreement is still relatively fragile, especially as it relates to big questions around whether hostilities between Israel and Lebanon will persist.

Notably, tanker owners were quite positive around the prospect for sanctions relief on Iranian oil and what this could mean for demand for compliant, mainstream tonnage. The Iranian dark fleet primarily consists of older, less maintained vessels. These vessels were popular among smaller, Chinese refiners when Iranian oil was trading at a significant discount, and these ships were the only options. Should sanctions on Iranian oil be lifted, then demand for newer, better maintained and compliant ships should increase. A real-world example of this dynamic can be seen in Venezuela today where previously sanctioned crude volumes are now being lifted using mainstream, compliant vessels, displacing dark-fleet activity.

## China - Remains a key driver of commodity import demand

A notable conference panelist said that he continues to be surprised when his Western colleagues visit China for the first time and they are surprised by the current living and economic standards, economic resilience, and technological advancement. These direct observations challenge previous notions or biases and matters for shipping into two important ways: 1) Even if China is not re-accelerating in the classic property-led model, it remains the marginal buyer of many bulk and energy commodities, and; 2) China's policy orientation is increasing strategic, focusing on greater integration of its global supply chain via the Belt and Road initiative which includes sourcing, transporting, storing and stockpiling, and use of various strategic commodities. Given trade frictions between China and the US and between China and Australia in recent years, we believe that China will continue towards more self-sufficiency and supply-chain diversification.

## LNG and related marine-based energy infrastructure remain a theme

The conference reinforced that LNG-related infrastructure and other marine-based energy infrastructure remains a durable theme. A growing number of market participants are evaluating opportunities through the lens of: 1)

geopolitical risk diversification; 2) energy security; 3) price index diversification, and; 4) infrastructure optionality and flexibility. There was also increasing recognition that adjacent gas derivatives, including ethane, could become more relevant in smaller market. We believe this theme will be beneficial for Golar (GLNG), Excelerate (EE), and Navigator Gas (NVGS).

Dry bulk fundamentals remain supported by tonne-mile growth and slow speeds. Turning to the dry bulk segment, commentary was constructive around rising commodity flows from West Africa and South America into China, including iron ore, bauxite, and grains. Slow steaming speeds and higher fuel prices have also helped reduce effective supply in the current market. These trends continue to support tonne-mile demand and rates going forward.

Bauxite exports from Guinea have doubled since 2020 and have been a meaningful driver of tonne-mile demand. That said, Guinea has proposed an export cap of \~150 Mt in 2026, roughly 15% below 2025 levels. This could be an important swing factor.

It was noted by one speaker that iron ore imports into China have been decreasing in quality in recent quarters. This has positive implications for iron ore trade volumes as it takes more iron ore of lower quality to produce the same amount of steel compared with higher-quality ore. This might be an underappreciated support factor for dry bulk demand.

China has resumed purchases of US grains, along with stockpiling corn from Argentina. This points to a strategy of agricultural stockpiling as a security hedge.

Tanker demand fundamentals look positive, but monitoring growth in orderbook The conference tone on tankers remained positive, with a strong emphasis on three key themes: 1) geopolitical factors will continue to drive trade inefficiency; 2) tinkering ordering has increased but should be balanced by the current, aging fleet, and; 3) current secondhand asset values are great for sellers of older tonnage.

There was broad agreement by several panelists that it is a good seller's market for owners looking to divest older, less fuel efficient ships. In turn, this cash can be returned to shareholders or held back as cash on the balance sheet as treated like an “option” to engage in purchase and acquisitions in the future when the market eventually turns. This is especially attractive for companies with relatively modern fleet, like Scorpio (STNG), because they can monetize older, non-core assets, while not running into a complete wall due to lack of operating assets.

A major discussion point was that 10-15% of the current tanker fleet is currently tied to sanctioned or dark-fleet vessels. If Iranian sanctions are eased or lifted, the immediate effect may be more mainstream and compliant ships displacing dark fleet or non-compliant ships. This would be a net positive for mainstream tanker demand and rates. It was noted that smaller Chinese refineries were benefiting from the use of Iranian-linked dark fleet vessels largely because of discounted Iranian crude prices. If sanctions are lifted, then there will be less of an incentive to use sub-standard ships.

While the crude tanker orderbook has moved up in recent months, the overall message was not overly-bearish as: 1) deliveries are spread out over many years, with most of the orders delivering in 2028 or beyond; 2) the existing fleet is fairly old and will continue to age between now and then, and 3) current order levels remain below historical peaks. This suggests that while supply pressure is building, it is not necessarily at a critical breaking point, especially in the next 12 to 24 months.

## Supply, orderbooks, and asset prices

One of the more concerning trends was around the increase in newbuilding orders in the crude tanker and product tanker segments, with crude tanker newbuilding orders accelerating in recent months. That said, newbuilding prices remain elevated and this is discouraging a rush of speculative orders and helping preserve some supply disciplines. Many owners remain reluctant to place speculative orders but may order some newbuilding assets as a means of normal-course fleet renewal. Secondhand asset prices remain robust and many owners are taking advantage of the current market to divest older, less efficient assets.

Conference commentary suggested that while newbuilding prices may ease in the coming years, the current delivery schedule now puts new assets squarely in 2029 or even in 2030. Ship yards remain full in the near term and a higher structural floor may have been established. If true, this means that: 1) fleet replacement becomes more expensive or cost prohibitive; 2) NAV support for public shipping equities could improve; 3) modern tonnage should command a larger premium compared to older, less fuel efficient assets.

## Regulations and technology – part of everyday operations, but less of a focus

Compared with previous years, there were far fewer discussions on decarbonization and green technology. This does not mean that regulation has gone away, but it appears to have been largely displaced by more urgent discussions around trade dislocations and geopolitical disruptions. The regulatory discussion appears to be shifting towards more regional implementation, including at the Port of Singapore. We view the possibility of more regional regulatory templates moving faster than global frameworks.

Unlike some of the more speculative AI narratives in other sectors, the maritime use case presented at the conference felt much more concrete and applicable to real-world, analog applications. The focus was on the use of AI for 1) predictive maintenance and downtime forecasting and management; 2) route optimization, and; 3) digitization and analysis of largely hand-written reports and materials within the sector. The implications are better uptimes on assets, lower maintenance costs (all else equal), improved voyage planning, and better asset utilization. For asset-heavy sectors like shipping, modest improvements in operations can have meaningful economic value to things like operating availability and reduced opex.

## Deglobalization, geopolitical risk, and trade

While globalization and internationalization of trade has been a key factor for growth in trade volumes, the key analytical mistake of looking at trends in deglobalization would be to assume that fragmentation will necessarily hurt tonne-mile demand. A fragmented and increasingly complex global supply chain and geopolitical environment can be supportive for shipping if shifting trade patterns result in: 1) longer voyage distances; 2) more rerouting occurs; 3) more stockpiling and inventory building occurs; 4) there is less efficient loading/discharge activities at smaller, less-sophisticated terminal and ports, and; 5) regionalization of regulations creates even more complexity.

## Summary and Final Thoughts

The bottom line is that the shipping market is becoming increasingly complex and that shipping is a hedge against geopolitical risk and uncertainty. This is uncomfortable from a geopolitical perspective, but constructive in terms of potential earnings power. From an equity standpoint, the winners should be those companies that can translate this new operating backdrop into shareholder value through capital discipline, balance sheet flexibility, and robust shareholder returns. Ship owners should benefit from the move from maximizing trade efficiency to optimizing around trade and supply chain resiliency.

We leave you with a sobering quote from French economist, Frederic Bastiat, who said that "...what would be the use of large standing armies and powerful navies if trade were free..."

Companies that will benefit from deglobalization, trade inefficiency, and greater global focus on energy security and supply-chain diversification:

• Star Bulk Carriers (SBLK) and Genco Shipping (GNK), dry bulk segment

○ Increased tonne-mile demand due to greater voyage distances and supply diversification in iron ore, bauxite, and grains.

\- Greater inefficiencies in loading dry bulk commodities in West Africa compared to other regions.

\- Higher fuel prices will encourage ongoing slow-steaming of the fleet, limiting some effective supply.

\- International Seaways (INSW) and Scorpio Tankers (STNG), tanker segment

\- Lasting energy security concerns, supply-chain diversification, and stockpiling should drive demand for crude oil and refined products, resulting in greater demand for tankers.

\- Sanctions relief on Iranian oil may incentivize demand for mainstream (not dark fleet) tankers, much like in Venezuela.

\- Navigator Holdings (NVGS), LPG carrier and petchem export infrastructure segment

Similar to crude, refined oil products and LNG, the current conflict in the Middle East has disrupted global petchem supply chains and security of supply. As such, we believe that the abundance of cost-advantaged US gas-derived products such as ethylene, ethane, etc., will remain a cost-advantage source of supply.

\- Opportunities for additional smaller-scale infrastructure projects along the non-Methane gas value chain.

## • Excelerate Energy (EE), FSRU segment

o Greater need for flexibility in the LNG import market and additional need for stockpiling and storing LNG. Should help drive underlying demand for FSRUs and other regasification infrastructure.

## • Golar LNG (GLNG), marine-based FLNG segment

o Greater focus on energy security and supply-chain diversification by buyers of LNG in Europe and in Asia should drive demand for non-US Gulf and non-Qatari LNG liquefaction infrastructure, resulting in additional contract opportunities.

## • Venture Global (VG), US land-based LNG liquefaction segment

In line with the increased global focus on energy security and supply-chain resiliency, we believe LNG from the US Gulf Coast will continue to be a vitally important part of the global energy mix, resulting in more opportunities for Venture Global to lock in longer-duration sales agreements with European and Asian buyers of LNG.

## Appendix 1

## Important Disclosures

Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at

https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Chris Robertson.

Company rating dispersion and banking relationships

<table><tr><td>DBSI Companies under Coverage</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Covered</td><td>57%</td><td>42%</td><td>0%</td></tr><tr><td>w/ Banking relationship</td><td>43%</td><td>36%</td><td>0%</td></tr><tr><td>w/ MiFID services</td><td>62%</td><td>51%</td><td>67%</td></tr></table>

<table><tr><td>Global Companies under Coverage</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Covered</td><td>57%</td><td>41%</td><td>2%</td></tr><tr><td>w/ Banking relationship</td><td>47%</td><td>35%</td><td>29%</td></tr><tr><td>w/ MiFID services</td><td>75%</td><td>69%</td><td>94%</td></tr></table>

## Company Rating and Dispersion Key

The above table provides a snapshot of DB's company research rating distribution across our covered companies. We also present the percentage of companies where Deuts

[中间内容因长度限制已省略]

r confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau
Group Chief Economist and Global Head of Research

<table><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr></table>

DB AG
21 Moorfields
London EC2Y 9DB
United Kingdom
Tel: (44) 20 7545 8000

DB Securities Inc.

The DB Center
1 Columbus Circle
New York, NY 10019
Tel: (1) 212 250 2500

DB AG
Filiale Singapur
One Raffles Quay, South Tower
Singapore 048583
Tel: (65) 6423 8001
"""
