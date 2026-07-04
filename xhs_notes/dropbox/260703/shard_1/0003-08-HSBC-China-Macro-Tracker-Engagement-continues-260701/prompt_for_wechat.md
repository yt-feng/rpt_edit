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
- 已识别机构名：`HSBC`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份HSBC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Macro Tracker

Engagement continues

\- China and the EU set up workstreams to discuss areas of disagreement, with an October deadline set for tangible results

\- Industrial profits softened, with mixed industry results: energy and AI sectors outperformed, but downstream faces pressure

Year 3 of LG debt swap: audit flags questionable cases; NDRC reportedly discourages LGFVs from high-yield offshore borrowing

## EU-China relations: doors remain open, but tensions are present

Just as China-US relations are showing signs of stabilising, the external narrative is starting to shift: China-EU tensions look more prone to escalation. The EU is pressing ahead with a clearer “de-risking” agenda and, with the proposed EU Industrial Accelerator Act, is signalling a more assertive push to expand made-in-EU manufacturing capacity. China’s exports to the bloc are primarily intermediate goods (40%) – largely supply chain trade, followed by capital goods (28%) and consumer goods (25%). Since 2023, the EU has launched trade remedy measures against made-in-China chemicals, steel, machinery and electrical equipment, and electric vehicles (Chart 1), and may expand its measures. In practice, the interaction is starting to look familiar: as with earlier episodes of China-US trade frictions, a sequence of targeted measures could begin to compound, broadening from specific sectors into wider questions of industrial policy and supply-chain security, and could take time to settle into a more predictable equilibrium.

For now, both sides remain in negotiations, and there's still scope for pragmatic compromise given the depth of trade and investment linkages. On 29 June, China's Commerce Minister Wang Wentao and the EU Trade Commissioner Maroš Šefčovič issued a Joint Statement outlining four workstreams (trade and investment, export controls, intellectual property rights and WTO reform) to continue dialogue. A follow-up minister-level meeting is set for the Autumn, with the EU Trade Commissioner later stating that there was an October deadline to reach “tangible results” (Reuters, 30 June).

But it's worth being realistic about the complexity: the issues at stake go beyond tariffs into subsidies, standards, procurement and strategic technologies – which tend to be areas where “technical” disputes can quickly become political. A rockier relationship would not only affect China and the EU, but may also impact the Asia region more broadly (see Regional implications of China-EU trade talks, 30 June).

China is unlikely to step back if tensions escalate, having expanded its countermeasures through initiatives such as the recent Supply Chain Security Act (China macro tracker, 9 April) and the ODI regulation taking effect on 1 July. While negotiations may continue, the risk of tit-for-tat escalation cannot be fully discounted.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

# Economics China

## Erin Xin

Senior Economist, Greater China
The Hongkong and Shanghai Banking Corporation Limited
erin.y.xin@hsbc.com.hk
+852 2996 6975

## Taylor Wang

Economist, China
The Hongkong and Shanghai Banking Corporation Limited
taylor.t.l.wang@hsbc.com.hk
+852 2288 8650

## Jing Liu

Chief Economist, Greater China
The Hongkong and Shanghai Banking Corporation Limited
jing.econ.liu@hsbc.com.hk
+852 3941 0063

## Heidi Li

Associate Guangzhou

## No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

View HSBC Global Investment Research at: https://www.research.hsbc.com

Industrial profits: Energy, AI sectors outperformed, while downstream pressure lingered China's industrial profits growth slowed to $21.1\%$ y-o-y, despite a lower base, suggesting a slowdown in momentum. The bifurcation in results continued with upstream sectors (energy and non-ferrous metals) and some industries benefiting from global AI-related demand still outperforming. Going forward, profitability in oil-related upstream sectors may start to moderate following the easing of Middle East tensions and gradual resumption in global energy supply, though robust worldwide AI capital expenditure is expected to continue, supporting margins in the electronics sector. Excluding these sectors, performance across other industries—mainly midstream and downstream—worsened, with the drag increasing to 5.5ppt in Jan-May from 4.8ppt in Jan-Apr.

Rising energy costs have increased input-cost pressure across downstream sectors, whose output prices have stayed muted, resulting in margin compression. In particular, y-o-y profits declined by c11% in garments & apparel, c19% in leather and fur-related products, and c1% in rubber & plastics, weighing on profitability (chart 4). Cost pressures are likely to ease, though still tepid domestic end-demand remains a constraint for profit revival. Relatedly, China's cautious consumer (22 May) has meant lackluster performance in related categories. Y-o-y profits in furniture, sports and recreational products and autos fell c58%, c7% and 20% in the first five months of this year.

Meanwhile, weakness in property and infrastructure investment intensified since the start of Q2, contributing to a 1.2ppt drag on headline profit growth in Jan-May from ferrous metals and non-metal minerals. Going forward, we think a re-acceleration in government bond issuance and faster deployment of the RMB800bn of new policy-based financing tools should help infrastructure and construction activities, although property investment is likely to remain a drag. The recent implementation of cuts to VAT export rebates for solar and batteries since April likely also added pressure on profits in electrical machinery, where y-t-d profits fell 14% y-o-y.

Local government debt: de-risking agenda still strong; cases of data manipulation found Local government fiscal constraints may continue to weigh on investment in the near term as an emphasis on addressing debt risk continues. However, with domestic growth showing signs of increased pressure, a policy pivot towards accelerated deployment of support is likely.

As of end-H1, over RMB2trn of local government refinancing bonds have already been issued, representing 73% of the annual quota (RMB2.8trn), showing clearly front-loaded issuance. Progress was also made in 2025, with over 82% of local government financing vehicles (LGFVs) having exited. Our estimates also suggest LGFV debt as a share of GDP edged down slightly to 46.8% in 2025 from 47.2% in 2024 (chart 5). Meanwhile, funding for projects has taken a step back. At end June, the pace of special local government bond issuance remains at a softer pace compared to 2025 levels, reaching 47% of the annual quota (chart 6).

China's National Audit Office flagged dubious cases in local debt resolution efforts, noting that $6\%$ of LGFVs in spot checks falsified data to exit the list, while some localities added new hidden debt via SOEs and artificially lowered existing debt through loan substitutions and system data deletions (NAO, 24 June). Bloomberg (30 June) reported that the NDRC is discouraging LGFVs from issuing high-yield offshore debt, underscoring Beijing's concern that some local governments may be delaying clean-up efforts and masking underlying risks.

Softer local fiscal revenues remain a constraint for de-risking. The property downturn has meant land sales revenue was down 28.7% y-o-y in Jan-May. While Beijing is encouraging local governments to monetise and revitalise existing assets, helping lift non-tax revenues by 2.2% y-o-y ytd in May, more needs to be done. Looking ahead, faster fiscal reform, particularly to better align central-local expenditure responsibilities with revenue assignments, and to strengthen local fiscal revenue by broadening the consumption tax and allowing local governments to share in the revenues will help (see China NPC Budget, 15 March).

## Charts of the week

1. The EU has expanded its trade remedy measures against China  
![](images/ba799f9cb30d749eef47e8954e1aa7a9d16bda14eb6e7e1bb5d718530dca673d.jpg)  
Source: China trade remedies information, HSBC; Note: as of 29 June.

3. Key EU imports from mainland China  
2. EU trade with China has seen a larger goods deficit in recent years  
![](images/91992c760da22ab65a5ed78c960df3016db50b28a36a16fe8254f9a7d3b02624.jpg)  
Source: UN Comtrade, HSBC

![](images/2d26ffefa3377c396fb30fc019af4a9cb27fbc8365ab80ea4c2f3f3885d22bc3.jpg)  
Source: CEIC, HSBC

4. Profits remained concentrated in energy and AI-related sectors  
![](images/6c7a22e79ff00b969921ed55eb293b726548de160f7a82667464219bf65027ef.jpg)  
Non Ferrous Metal
Computer, Communication & Other Electronic Equipment
Non Ferrous Metal Smelting & Pressing
Chemical Material & Product
Petroleum, Coal and Other Fuel Processing
Headline  
Source: CEIC, HSBC

5. LGFV debt as a share of GDP edged down slightly  
![](images/60706e422cf701b215e0b9d9e1d6b0531f3eff3c800e074b25ed475275ddd86f.jpg)  
Source: CNBS, HSBC estimates; Note: For LGFV debt, we estimate it as the sum of the interest-bearing liabilities of LGFVs that have issued LGFV bonds.

## Economic activity

6. LGSB issuance can be stepped up to support infrastructure investment  
![](images/607f3e66ea65c7a0e953503005fd102f916bdb9fd94734829ae39d37c04f4897.jpg)  
Source: Wind, HSBC; Note: Data as of 30 June.

7. Cross-city travel remained elevated  
![](images/80e0699cf08886b65a65ad0e5192cf9573748a33a32efbba340c8db791a630e3.jpg)  
Source: Baidu Index, HSBC

8. The number of domestic flights moved up  
![](images/38cc89b76ac7e9fed70043cd6ef5a583cd794f492dcb1f088741241cbb824da3.jpg)  
Source: Wind, HSBC

9. Car sales edged down in June in year-on-year terms  
![](images/7a5b13c447940b8a81f68b99df9bcbd78e5cb1cd54e34367a0d9fd6759e6f3bb.jpg)  
Source: Wind, HSBC

10. National box office revenues edged down  
![](images/47260605eb4f9a2a47a228f250b44695d379206322b7359facc801cbae5c4735.jpg)  
Source: Wind, HSBC

11. Housing prices in tier-1 cities edged up  
![](images/49a2906f81759373fb361992a499f7d47e1634a52adeaffb5140b6af893e6437.jpg)  
Source: Bloomberg, HSBC; Note: as of 30 June.

12. New home sales edged up seasonally  
![](images/66a645d7c44ee696dae4705efedff4d723725b2ce4df78cd8c3394d50e053870.jpg)  
Source: Wind, HSBC

13. New home sales in Tier-1 cities remained higher y-o-y  
![](images/0791c078df8cfbee126cc72f711ed514418ab70862f8d1d792f726a9badda76a.jpg)  
Source: Wind, HSBC

14. Second-hand home sales in 18 major cities rose seasonally  
![](images/f41e882c12213861038f3c11f69cf3d2bc384b2685fd16ffd9fee0927571bab1.jpg)  
Source: Wind, HSBC

15. Transactions in second-hand homes in Tier-2 cities remained higher y-o-y  
![](images/231b00ce4f14ba90c5e204e1e08b644074ad84fc74c417adfce4d9a3f90c84fe.jpg)  
Source: Wind, HSBC

16. Land sales edged up  
![](images/05619f38b8df1f9737cbee70a4bf5a46d504ec82a04400b967e0ae23589926e9.jpg)

17. Planned construction area of land sold edged up  
![](images/e4378a9518ae1ace45e9eb9a5c8f42412dacf0afd221f1cca854e1c8004ff1bd.jpg)  
Source: Wind, HSBC  
Source: Wind, HSBC

18. The semi-steel tyre operating rate edged down  
![](images/8b2d6ede5c9fd759b0777c1914e707f37eea63f09869cae4a1464a3f78ddfbf7.jpg)  
Source: Wind, HSBC  
Source: Wind, HSBC

19. The production rate in the chemical sector picked up  
![](images/c1a19acf60feaef02293db8ca4ea4569ce1f3940baa51ece225bbc05503309a1.jpg)

20. The blast furnace operating rate remained above historical levels  
![](images/f51de9b2681a6457a7797cffcf9cb643bd1977bb58f85abf0957caa5be563015.jpg)  
22. The cement shipping rate steadied  
Source: Wind, HSBC

21. The petroleum asphalt operating rate ticked up  
![](images/7ecd498fbc3d6b193869299132fb9d340f2fc05fea426302180fda1161d24449.jpg)  
Source: Wind, HSBC

![](images/95df3ba4485104722e383f1dae114561450b586186781aef5b5e1b3999de361b.jpg)

23. Coal consumption for eight major provinces edged down  
![](images/d9fcf37f55db2b1c9a011ec16295cdb6ac5b9fe6f2f0f851e3189ce179ff07db.jpg)

24. The operating rate of polyester filaments eased further  
![](images/5a9a70502ebc65ddc33deeab69aac091aeda5c2e57ea6fb6903e431ccd9ff4f6.jpg)  
Source: Wind, HSBC

Travel and logistics  
25. The Baltic Dry Index edged down  
![](images/157b092c0a63c88c6491a2721d1926ec0caf12c4401cf75c4dce0187dd83d62a.jpg)  
Source: Wind, HSBC

26. Metro volumes in large cities edged up  
![](images/7deca941c19fd509432d7eb951037d211edf9596836c5b265c3b1f35f10359a2.jpg)  
Source: Wind, HSBC; note: six cities include Beijing, Shanghai, Guangzhou, Shenzhen, Chengdu and Tianjin.

27. Postal delivery volumes edged down  
![](images/f5350d7904fa2c6c199f37cb7b760b3853bfc5fee68e90febe75e2948e510fbe.jpg)  
Source: Wind, HSBC

28. Container exports from China to the US edged down  
![](images/7cfd6189c325ff4a0f3ae261ca0804d3e51d02edfe9631891a7b2db3909fa9f4.jpg)  
Source: Bloomberg, HSBC

29. China's major ports' freight throughput edged up  
![](images/572c38f5f374822f3e4ea7891b2beecaaa4cc9a7a94d02c119e19807f3a4f146.jpg)  
Source: CEIC, HSBC; Note: Weekly beginning at Monday

## Inflation and policies

30. Crude oil prices fell as the US and Iran reached a deal  
![](images/761eec6f0a7734e20561028c92a142b86466f1e151ec7962458569d4f8dafba2.jpg)  
Source: Wind, HSBC

31. Cement prices and glass prices both edged down  
![](images/91bc5823b3104f4deb1c0813581fbb9660572dd1ae2c3c4c42a8df87dfe7d5eb.jpg)  
Source: Wind, HSBC

32. Agricultural product prices eased seasonally  
![](images/d231e1b4c55fe71e8b46accbff105ec1cca97eb45b5b1c2d5a5c875f12e6f479.jpg)  
Source: Wind, HSBC

33. Container shipping costs on China-Southeast Asia route edged up  
![](images/97408c29fd130c48acb333bf74adeda20bdb8224c931991f7fab186b2a71a39c.jpg)  
Source: Wind, HSBC

34. Interbank rates edged up  
![](images/8cb73239de114f5cde529beaee75511b09b583c64896ccb6c0f1c69c6e21923a.jpg)  
Feb-20 Feb-21 Feb-22 Feb-23 Feb-24 Feb-25 Feb-26
— R007 (7-day weighted-averaged interbank bond collateral repo rate )
— DR007 (7-day weighted-averaged interbank bond collateral repo rate: depository institutions)  
Source: Wind, HSBC

35. The PBOC made net injections through OMOs last week  
![](images/d96ef3769eadf6cdf2dfb16246f6edb131fc7ba5c0554a32db12ac65f440990d.jpg)  
Source: Wind, HSBC

# Links to recent reports in the China Macro Tracker series

Financial opening-up, 24 June 2026

What the US-Iran deal could mean for China, 17 June 2026

Blueprints for employment strategy, 10 June 2026

Home sweet home, 3 June 2026

Structural measures move up the agenda, 27 May 2026

Stable relations, but domestic pressures, 20 May 2026

First Presidential summit of the year arrives, 13 May 2026

Future focused, 6 May 2026

Tougher investment security reviews, 29 April 2026

More reserve policies are in the pipeline, 22 April 2026

Focus on "doing o's own thing well", 15 April 2026

Better coordination of development and security, 9 April 2026

Resilience and stability could pay off, 1 April 2026

Expanding opening-up and FDI, 25 March 2026

A good start, more moves to follow, 18 March 2026

NPC press conferences, global oil volatility, 11 March 2026

China's Two Sessions in a volatile world, 4 March 2026

US tariff changes, record breaking CNY holiday, 25 February 2026

Boosting investment and innovation, 11 February 2026

Chinese New Year migration begins, China-UK reset, 4 February 2026

A more conservative approach to the GDP target, 28 January 2026

Domestic pressures may prompt more urgency, 21 January 2026

Domestic demand needs an investment lift, 14 January 2026

Starting the new year with policy support, 7 January 2026

Demand-led rebalancing, 17 December 2025

Politburo, Pandas and Provincial Five-Year Plans, 10 December 2025

Last policy meetings for the year approaching, 3 December 2025

Phone a friend, 26 November 2025

Not yet at the finishing line, 19 November 2025

A balanced approach, 12 November 2025

A new tenuous equilibrium, 5 November 2025

Potential trade breakthroughs, 29 October 2025

Deal or no deal, 22 October 2025

On pins and needles, 15 October 2025

New measures before the Golden Week, 1 October 2025

Talking points, 24 September 2025

US-China talks see progress in Madrid, 17 September 2025

Anti-involution to help longer-term development, 10 September 2025

# Disclosure appendix

## Analyst Certification

The following analyst(s), economist(s), or strategist(s) who is(are) primarily responsible for this report, including any analyst(s) whose name(s) appear(s) as author of an individual section or sections of the report and any analyst(s) named as the covering analyst(s) of a subsidiary company in a sum-of-the-parts valuation certifies(y) that the opinion(s) on the subject security(ies) or issuer(s), any views or forecasts expressed in the section(s) of which such individual(s) is(are) named as author(s), and any other views or forecasts expressed herein, including any views expressed on the back page of the research report, accurately reflect their personal view(s) and that no part of their compensation was, is or will be directly or indirectly related to the specific recommendation(s) or views contained in this research report: Erin Xin, Taylor Wang and Jing Liu

## Important disclosures

This document has been prepared and is being distributed by the Research Department of HSBC and is intended solely for the clients of HSBC and is not for publication to other persons, whether through the press or by other means.

This document is for information purposes only and it should not be regarded as an offer to sell or as a solicitation of an offer to buy the securities or other investment products mentioned in it and/or to participate in any trading strategy. Advice in this document is general and should not be construed as personal advice, given it has been prepared without taking account of the objectives, financial situation or needs of any particular investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. If necessary, seek professional investment and tax advice.

Certain investment products mentioned in this document may not be eligible for sale in some states or countries, and they may not be suitable for all types of investors. Investors should consult with their HSBC representative regarding the suitability of the investment products mentioned in this document and take into account their specific investment objectives, financial situation or particular need

[中间内容因长度限制已省略]

 HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and intending to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, SA, Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.

# Global Economics Research Team

## Global

Global Chief Economist
Janet Henry +44 20 7991 6711
janet.henry@hsbcib.com

Global Economist
James Pomeroy +44 20 7991 6714
james.pomeroy@hsbc.com

Global Economist
Bethan Ellis +44 20 7991 6714
bethan.ellis@hsbc.com

Trade Economist
Shanella Rajanayagam +44 20 3268 4118
shanella.l.rajanayagam@hsbc.com

## Europe

Chief European Economist
Simon Wells +44 20 7991 6718
simon.wells@hsbcib.com

Senior Economist
Chris Hare +44 20 7991 2995
chris.hare@hsbc.com

## United Kingdom

Senior Economist, UK
Elizabeth Martins +44 20 7991 2170
liz.martins@hsbc.com

UK Economist
Emma Wilks + 44 20 3268 5948
emma.wilks@hsbc.com

## Germany

Stefan Schilbe +49 211 910 3137
stefan.schilbe@hsbc.de

Anja Sabine Heimann +44 738 724 7457
anja.sabine.heimann@hsbc.com

## France

Chantana Sam +33 1 4070 7795
chantana.sam@hsbc.fr

## North America

## US

Ryan Wang +1 212 525 3181
ryan.wang@us.hsbc.com

## Asia Pacific

Co-Head of Global Research, Asia-Pacific and Co-Head of Asian Economics Research
Frederic Neumann +852 2822 4556
fredericneumann@hsbc.com.hk

Chief Economist, Australia, New Zealand and Global Commodities
Paul Bloxham +612 9255 2635
paulbloxham@hsbc.com.au

Chief Economist, India and Indonesia
Pranjul Bhandari +65 6658 4976
pranjul.bhandari@hsbc.com.sg

Jamie Culling +612 9006 5042
jamie.culling@hsbc.com.au

Jing Liu +852 3941 0063
jing.econ.liu@hsbc.com.hk

Ines Lam +852 2288 7131
ines.y.k.lam@hsbc.com.hk

Yun Liu + 852 2822 4297
yun.liu@hsbc.com.hk

Aayushi Chaudhary +91 22 2268 5543
aayushi.b.chaudhary@hsbc.co.in

Maitreyi Das +91 80 6737 3155
maitreyi.das@hsbc.co.in

Erin Xin +852 2996 6975
erin.y.xin@hsbc.com.hk

Aris Dacanay +852 3945 1247
aris.dacanay@hsbc.com.hk

Jin Choi +852 2996 6597
jin.h.j.choi@hsbc.com.hk

Akiko Kitamura +852 2996 6676
akiko.kitamura@hsbc.com.hk

Justin Feng +852 2288 7108
justin.feng@hsbc.com.hk

Taylor Wang +852 2288 8650
taylor.t.l.wang@hsbc.com.hk

Priya Mehrishi +91 97 3916 9567
priya.mehrishi@hsbc.co.in

## CEEMEA

Chief Economist, CEEMEA
Simon Williams +971 50 9143382
simon.williams@hsbc.com

Senior Economist, Central & Eastern Europe
Agata Urbanska-Giner +44 20 7992 2774
agata.urbanska@hsbcib.com

Senior Economist, CEEMEA
Melis Metiner +44 20 3359 2636
melismetiner@hsbcib.com

Senior Economist, South Africa
Hugo Pienaar +44 20 7718 9563
hugo.pienaar@hsbc.com

## Latin America

Chief Economist, Mexico
Jose Carlos Sanchez +52 55 5721 5623
jose.c.sanchez@hsbc.com.mx

Head of Brazil Economics Research
Daniel Lavarda +55 11 2802 2640
daniel.lavarda@hsbc.com
"""
