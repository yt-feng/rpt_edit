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
MS European Capital Goods
25 $^{th}$ June 2026

MORGANSTANLEYRESEARCH Europe

MS & Co. International plc+

# Industrial capex > production. A case for selective broadening out

Max Yates  
Equity Analyst  
Max.Yates@morganstanley.com  
+44 20 7425-1917

Harry Stephenson
Research Associate
Harry.Stephenson@morganstanley.com
+44 20 7425-0859

Sara Chemello
Research Associate
Sara.Chemello@morganstanley.com
+44 20 7425-2931

## Capex resilience. Customers learning to live with uncertainty

\- Reminiscent of 2022. Data center, strategic capex and price will protect nominal sector earnings. The bigger sector risks are 1) EBITA margins and cost pressure, and 2) multiples, particularly if interest rates start moving higher.

\- Capex ‘green-shoots’, in particular in US and in Asia. Customers ‘looking through’

\- Less risk of an industrial demand collapse from here, given demand for many short-cycle companies has not grown volumes versus 2019 levels.

\- Cost inflation is back. This time affecting Electricals more than Mechanicals. Some concerns across Signify, Vestas, Weir and Rexel.

## Selective in Electricals / Mechanicals. Keep our quality growth skew.

\- Electricals: we prefer Schneider (OW). Best balance of growth vs valuation. We also stay OW Legrand and view the recent sell-off as overdone.

\- We like upstream mining. Since March-26, we have preferred Epiroc (OW) to Sandvik (EW). Too early to buy the mid-stream names.

\- Stocks for a broadening out: Atlas Copco (OW), Knorr Bremse (OW), Spirax (OW). Risk reward on Siemens (EW) also looks positive here into 2027.

\- We stay cautious on Wartsila (UW), Signify (UW), and Kone (UW).

End market order growth trends. Electrification order growth has likely peaked. Process / Construction is in no mans land  
![](images/c3f1d02ba195c24c786980f0236811599455d0bf482f8ed65655a0ba72a4ce42.jpg)

## Global capex in 2026. Still a thematic world. Capex growth (based on analyst ests) is still confined to a smaller number of sub-sectors. Process is a soft spot.

We see a mixed picture for capex into 2026. Hyperscaler, and Semis are bright spots. We see relatively higher risks in O&G, Pharma and Chemicals

![](images/c9cde2ed2ee5bbbdc3b52a51cada79ade2850aff9dfdb73d674a97c0170e8fd9.jpg)

Capex green shoots. We see this in US manufacturing starts, and Asia (ex China) Cap Goods imports, which lead Machinery gross capital formation.

US Dodge manufacturing starts. After many headlines on US ‘reshoring’ we are starting to see manufacturing starts grow again, which was a driver in 2021-22.

![](images/c7de47c641400c84c98f5326151dc95e5f0b490be5b71d0e45ba4d672c136463.jpg)

Our Asia economists see an emerging Asia (ex China) capex cycle. Capital Goods imports have picked up, and this should translate into greater gross fixed capital formation for machinery.

![](images/36d572f6942503a0087810138566c824e36ceefbc8b69d33bbbc0becc9c43fee.jpg)

## European Infra / Capex still has challenges. German Infra spending is taking longer, and European manufacturers (eg Auto) are still seeing challenges

German Infrastructure budget. Even with a German fiscal plan, the rate of Infra spending is falling behind expectations

![](images/9f96df28790d65526175a05d27c784f545c4a0928da77834765b77b119888bd5.jpg)

European Auto OEM's market share. Market share relative to global peers is continuing to increase. This is affecting EU Auto capex, a big European Industrial capex market

![](images/aca27fe790d7d768f26f7cdc1fe9ba93245ecd2982af82e1e56642e560cfe0d0.jpg)

Hyperscaler capex still stands out, and data centers are still the main growth driver for Electricals. 79% growth in 2026e, and 39% in 2027e

![](images/c5e014423750988ff1c04bb3dc58e29022184c859405a2534c1e87575fa6007c.jpg)

European and US IP. We are less fearful of a sharp Cap Goods volume slowdown. We are already coming out of a 2023-24 Industrial production recession in Europe. But we think risks are higher for the ‘production / consumer’ linked companies in our coverage.

EU and US Industrial production. We are coming off low levels, while the US has moved broadly sideways in 2023-25.

![](images/e9038fc3f46af8d7ac6dab452d190fcb74ed92b93fec407ee812e150d75824b1.jpg)  
Sandvik Machining volume growth has been negative for the majority of the last 3 years.

![](images/fea47cb87b432c6b116485030206b154bce0628ef10917d72d902ccab5b33128.jpg)

## Short-cycle data across US and Asia is still delivering strong growth rates. In particular, we would highlight US durable goods orders and Japan machine tool orders.

US Durable goods orders. These have continued to accelerate into 2Q26, which suggests to us that we are not seeing any major snap-back from potential pre-buying

![](images/ce314f30e6f5052f85edc3f5e4f3f7ab076654a239778caffdd1b090ccfb7f9e.jpg)  
Japan machine tool orders. These continue to deliver attractive growth rates, suggesting a continued strong backdrop for Factory Automation in our view.

![](images/ef99a06aa1c29d0e32737f0d8495298c597c0ef883a6899f642a6abed0a1e369.jpg)

## EMEA revenue exposure vs North America. We prefer US exposure over EU at this point in the cycle, given favourable short-cycle data and scope for incremental capex

![](images/d4a7bc97d5f3147f85191b0686d43e636b765941ab211139e5ff622796e9558c.jpg)

# EBITA margins – Arguably a bigger risk than growth. In 2022, companies with backlogs saw margin pressure. In 2026, Electricals costs are rising faster

Raw material average cost increases, and raw mats cost increases YOY in 2026 for Electricals and Mechanicals. Raw materials are typically 5-10% of Cap Goods company costs

Raw Material Average Cost Increase  
![](images/3fad23b55642667590b6d59ef1f31ebb9b3dc1aed3a42d14c68ae3b921a198d3.jpg)

Costs for Industrial companies have continued to rise for Industrials across a number of cost buckets. We think prices will need to rise $\sim 4\%$ in 2026e.

<table><tr><td></td><td>% of sales</td><td>2025</td><td>2026e</td></tr><tr><td>Raw materials</td><td>6%</td><td>2%</td><td>27%</td></tr><tr><td>Components</td><td>30%</td><td>3.0%</td><td>3.5%</td></tr><tr><td>Wages</td><td>25%</td><td>2.9%</td><td>3.5%</td></tr><tr><td>Freight</td><td>5%</td><td>8.2%</td><td>6.0%</td></tr><tr><td>D&amp;A</td><td>3%</td><td>3.0%</td><td>3.0%</td></tr><tr><td>Other costs</td><td>13%</td><td>2.5%</td><td>3.0%</td></tr><tr><td>Electricity</td><td>1%</td><td>-0.1%</td><td>25.0%</td></tr><tr><td>Cap Goods Annual cost inflation</td><td>82%</td><td>2.5%</td><td>4.4%</td></tr></table>

## EBITA margins – 2026 YOY increase in consensus margins (bps)

![](images/c0b8cd52e77e17ee7acb7880e2de4282090cb1fd7a97c2489b265cb733cdb706.jpg)

European sectors consensus EPS revisions (45 days). Cap Goods has seen relatively favourable EPS revisions versus the rest of the market.

We show cyclical (sectors) vs Defensives (sectors) across the broader European market. We have seen a pull-back, but it has been relatively modest so far compared to ‘typical cyclical pullbacks’.

European Sectors NTM Earnings Revision Ratio (FFMCap Weighted)  
![](images/9353858eba2c1fce5988ab727c5b354eb85dc1a218488e0e77030c74e17e0d65.jpg)

## Cap Goods EBITA revisions and multiple re-rating / de-rating since the start of the Iran conflict. Electricals have seen upgrades and re-rating. Mechanicals, a 10-25% de-rating

Electricals have mostly seen small upgrades to 2027 consensus, and this has largely combined with multiple re-rating. Schneider has lagged, while Prysmian, Signify and ABB have led the re-rating

![](images/850bdad392150b018ca6fbac311144c3779ccd4a5330515b201973ea851ea363.jpg)  
Mechanicals. 93% of mechanicals de-rated since the start of the Iran conflict. The majority of companies have de-rated by 10%-22% on concerns over global growth

![](images/c0b8283ae7a924bd9ef6e1df58b41786a122734c8934f101cfcbd1f097765dc0.jpg)

## Cap Goods Multiple vs 10-Year Average. 70% of stocks in our coverage are at or above their 10-year average valuations.

Left to right. The stocks on the left are trading at a high current valuation vs their ten-year average. Stocks on the right are relatively cheaper vs ten-year average. The thematic stocks (grid, power, data centre) are all relatively expensive versus history. We continue to like the risk/reward at Schneider, Epiroc, Siemens Energy, Legrand, Atlas Copco and Knorr Bremse. We remain Underweight on Wartsila, Signify and Kone

![](images/46947d5632d569d6c8db10fd7b32448bef8da087d5daeaf6a9c4f4debee9481f.jpg)

Fundamental Views: What to Own – What to Avoid. We keep a quality growth bias.

Atlas Copco

KNORR-BREMSE

L1 legrand

Spirax Group

Schneider Electric

![](images/daae06b13b7e96df797dd6aee5940222be510b1ecaf18e02bb2c30ff141a9eb8.jpg)

Rexel

SIEMENS
energy

## KONE ⑤ignify

![](images/d910e0fb4b741d684c36ab9e2803e24acfa26136cd3328a081eb34849277be8d.jpg)

# Industrial data. Holding up so far. US / Asia are reassuring, while Europe is moving sideways

## Europe. Soft data like the IFO has weakened, with the German IFO declining -3.1% YoY in June, despite a small MoM improvement

German Industrial is now back in negative territory YOY since January. April IP was -0.5% YoY.

![](images/36d290be11351a3b69cedad0b2fa204b12404c7ae24709439cdddb6f169868b8.jpg)  
German IFO business expectations have dipped. They are not yet at 2022 lows but have deteriorated.

![](images/c68d7c5a9a8f3144e649b17ca28ec2607af255016974bc14f014d0368846cc4f.jpg)

## Europe. Resi construction starts (Germany) and permits (France) are still nicely positive. Companies (RXL, St Gobain) see a slower 1Q26 start (weather)

German and French residential permits are still showing positive signs.  
![](images/a9ff33302ececa06d965625b95a87cb67d28be4db9d0b58da743fd65bc8a003c.jpg)

Companies (Rexel, St Gobain) had a slower start to 1Q26 with volumes again turning slightly negative (partially weather)  
![](images/24fde2b266b6a47b6e93a74ab9eb06ce2bb716ba0595886a58d71609bdf9366d.jpg)

## US. The ISM new orders showed some moderation in March from a much-improved Feb. New orders / Inventory do not suggest any major cause for concern.

US ISM new orders. A modest recovery in May, after a March pull back. Still nicely above 50 suggesting US industrial resilience.

![](images/12578cb038df79cb851b3c5062919dbe3d7d193be4e01a943be0d2578109e5f4.jpg)

The US ISM new orders to inventory remains well above the US ISM level. We do not see the US Industrial recovery as being derailed.

![](images/f4c52e5390e0aaa7ae1aafa6875a37c532ea38d275b4ef9301ad3135b9648e3f.jpg)

## Hard US Data. Fastenal April sales growth (14.3%) continued on a recovery path. Rockwell's orders also increased materially QoQ (\~20%) in the US.

Fastenal Daily sales growth. No signs of a slowdown. May (14.8%) vs Apr (14.3%) vs Mar (11.5%)

![](images/f155dce3b7936641728489df2d59e965f65e544cc1cb171db956c306b169ee4f.jpg)  
Rockwell orders were +20% QoQ, with the company pointing to some project capex unlock in the quarter across end markets like Automotive and Food and Beverage.

![](images/0e8c2ddd7add0ea3754f8b4032ba8c957538678065d0a187d43c56528a40e5aa.jpg)

Asia short-cycle data. Foreign Japan Machine Tool orders have accelerated through 1Q26, while Airtac sales were still +25% YOY in April.

Japan Machine Tool orders. Foreign demand grew at 46% in April, compared to 35% on average in Jan - Mar.

![](images/b6721c6e850fb16939f2314c1678d287b2303b5a3d81184f5a6eace8587020d6.jpg)  
Airtac sales. Overall 1Q26 sales growth was +11% QoQ and +24% YOY. Shipments to battery, general machinery and electronics was strong in March

![](images/edc5798dc102192772e9554209f638e163528ece8810fd23f859ce80d3dcbb8d.jpg)

## Asia Automation (including Fanuc Factory Automation) is strong. This illustrates continued Asia investments.

Fanuc factory automation orders saw a strong YOY increase in calendar 1Q26. Siemens order intake did not see the same intake, with Siemens lagging our expectation on China growth

![](images/82c9bc6bfded0731e0842b7ded677827aeed869e377be024f7bbf6efa02b73d0.jpg)

MIR China Automation data. This shows the YOY change in total China automation spend by end market. We can see particular strength in Battery and Electronics.  
![](images/8f5de8feff0f2cc6bc1d086c18bb8b74fc625d7d47ad9bc69fb406c538bc550d.jpg)

## Pre-buying debate. Is the March / April demand resilience real, or is it more pre-buy ahead of price rises? We have seen instances of companies highlighting pre-buy.

<table><tr><td>Company</td><td>Commentary</td></tr><tr><td>Metso</td><td>&quot;... with Aggregates... in this order intake, we see a clear pattern that some of the orders are placed not only for the second quarter but also for the second half of the year, so sort of a pre-buying phenomena visible in that regard.&quot;</td></tr><tr><td>Kion</td><td>&quot;The increase in new business contained pull-forward effects related to the price increases announced for early April 2026 intended to offset rising costs resulting from the Iran war.&quot;</td></tr><tr><td>Sandvik</td><td>&quot;Also solid demand in general industry. This is partly driven by prebuying, but also we are seeing early signs of an improved underlying sentiment in the market.&quot;</td></tr><tr><td>Flowserve</td><td>&quot;With the dynamics in the Middle East... we&#x27;re seeing folks trying to think about expanding capacity or doing things a little bit differently or potentially accelerating projects, and a lot of this is around energy security... customers talking about doing things differently about increasing capacity or actual expansions and even new projects.&quot;</td></tr><tr><td>Carrier</td><td>&quot;April movement was better than we thought. And I think part of that was probably people trying to beat the price.&quot;</td></tr><tr><td>3M</td><td>&quot;And then when you put all that together, it gives us a sense that perhaps there&#x27;s some advanced buying from these price increases that are going out.&quot;</td></tr><tr><td>Wacker Chemie</td><td>&quot;We had a solid start to the year and even surpassed our own expectations due to pull-forward effects... stemming from the conflict in the Middle East...&quot;</td></tr><tr><td>BASF</td><td>&quot;You really saw an uptick in the volumes... it&#x27;s difficult to evaluate now, are we talking about restocking effects? Or is this really an underlying demand development?&quot;</td></tr></table>

## Key ideas, positioning and valuation

## Stock Selection – Screen

## Overweight Ideas

\- Schneider (OW, PT €300): Best in class topline growth, and productivity accelerating group margin expansion in 2026/27.

\- Rexel (OW, PT €42): Upside to FY26 organic growth guidance from pricing. Mid-term margin upside from self-help.

\- Knorr Bremse (OW, PT €116): Solid backdrop for Rail end market, with continued cost optimization supporting group margin expansion beyond 14%. Balance sheet optionality.

\- Siemens Energy (TP, OW, PT € 200): Outstanding visibility with some modest upside to consensus. However, we continue to get closer to the peak in Gas orders, in our view.

\- Epiroc (OW, PT SEK 300) : Consensus margin downgrades done, and a multi-year order growth story.

\- Atlas Copco (OW, PT SEK 200): VT recovery on semi capex growth, Compressor Energy efficiency tailwinds, with balance sheet optionality.

\- Legrand (OW, PT €166): Upside to 2026 organic growth estimates, and M&A contributions in 2025-26 above trend.

\- Spirax (OW, PT GBp 8,500): Headwinds from semis / biopharma becoming growth tailwinds, and helping margin mix

## Margins

\- Signify (TP, UW, PT €15) : Organic growth lagging peers. Pricing pressure can lead to EBITA margins down YOY in 2026. Slow start to the year in 1Q26 and risk to the dividend.

End Market Exposure

\- KONE (TP, UW, PT €46.6): Full valuation relative to EPS growth CAGR. China remains a drag to growth in 2026, and ISP competition in service continues.

\- Wartsila (TP, UW, PT €29): Peak valuation, with limited consensus upside. Increased competition in Energy, and Marine set to sequentially weaken through 2026.

## Underweight Ideas

## MS vs Consensus for Electricals and Mechanicals (2027 EBIT)

![](images/8882170512c2e5ed7227089d71ba3868a5ba5d86591c880353e204eb24b1a104.jpg)

MSe vs VA EBIT 2027 Electricals  
![](images/2cb36286da8df449370782cece3577f3763460720b6f19b1ad28dbe66826ec3a.jpg)

## Sector valuation. Trading at a 23% premium vs the market. Defensives have also de-rated vs cyclicals through 2025. This also indicates expectations of a cyclical recovery

![](images/e507bb23819844451529714b5b12ce85a2e80f6f1797043b3afb97fd101a562e.jpg)

![](images/473c440f60fe8f9e3adcc38049f1791d3efed009a9adebc817593f4492f67a28.jpg)

![](images/3f2c0fd702c67fc45b5b98a452196c0b077308627138e9e8a72ac29358f7097f.jpg)

## European vs US Industrials valuation dispersion. Still a lot of room for Europe to close the gap in a continued Iran conflict de-escalation.

US Cap Goods back to a peak premium vs its EU peers.

![](images/18e94f03c268f9975984049f0c4ad1005eb2943556558275680e8ed4d8d79f27.jpg)  
The ‘European’ discount is most notable in 1) Siemens Energy vs GE Vernova, 2) Siemens vs Rockwell, and 3) Schneider vs Eaton.

![](images/14b8803e209e22dcc2d7f41b261239e1480c8981c2881fa049d65711d568be6b.jpg)

## Thematic valuations within Industrials (2028 EV/EBIT). Semi-cap (22x) at a premium. Defence (14x), Electrification (15.5x) and Aero Engines (16x) more tightly grouped.

Electrification stocks (ABB, SU, LR) are trading on similar multiples to Aero Engines. Power Gen is a 20% premium to Defence.

![](images/9e2c83968f63e907c8fe5b93bb74d20226ef0910a9c5f957b0ff216167a82ca2.jpg)

![](images/ffc1aa98b49553f19dbd6f0c1be99a1fcc6bd4b60e476958dc3f8eca58c6c5da.jpg)

# Digging into company valuations. Siemens is back to a -14% discount to its theoretical SOTP, while Schneider screens as attractive vs ABB

Siemens EV/EBIT vs a weighted average of its peer group (weighted by Siemens' divisional exposure). Siemens is back to trading at an 14% discount to its theoretical SOTP

![](images/61157e65691c662c4117d261e39ea02f703eb40bb53563d87ddebcc930b09d28.jpg)  
Schneider vs ABB relative EV/EBIT. Schneider is trading at a c.20% discount to ABB on consensus EV/EBIT. Schneider screens as relatively attractive.

![](images/e11b8d7c300d8e959997b0895e326af125317307711a5736997980858aca09f6.jpg)

## 2026e P/E multiple vs 2026-28e EPS CAGR. We see an attractive combination of valuation and EPS growth at Rexel and KBX.

2026e P/E vs 2026-28 EPS CAGR  
![](images/16a65ec916b1884b59474d537b372ad9b569c81f776043b834fe2168ade8e780.jpg)

## Long-only positioning data in the sector. Schneider well owned, but Legrand is catching up. Siemens Energy remains below large

[中间内容因长度限制已省略]

 Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative. The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA. As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations. The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS. Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.
KD170626

The Americas

1585 Broadway
New York, NY 10036-8293
United States
+1 212 761 4000

Europe
20 Bank Street, Canary Wharf
London E14 4AD
United Kingdom
+44 (0)20 7425 8000

Japan
1-9-7 Otemachi, Chiyoda-ku
Tokyo 100-8104
Japan
+81 (0) 3 6836 5000

1 Austin Road West
Kowloon
Hong Kong
+852 2848 5200

Asia/Pacific
"""
