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
# Aerospace, Defense, Metals & Mining: Feedback from Singapore and Hong Kong Marketing

We met about 25 investors during our recent marketing trip to Singapore and Hong Kong. Key discussion points from our meetings and interactions: 1) Defense: Investors wanted to know the likely major orders in FY27 and were interested to know the reasons for weak order inflow in Q1FY27; 2) Metals & Mining: Investors wanted to understand the direction of steel prices and likely consumption growth; 3) Compared to the last visit, there were fewer queries on the valuations; and 4) Investors specifically inquired on the stocks with category leadership or unique proposition. Overall, investors agreed that the Defense sector has performed well even in the backdrop of overall weak India market performance and easing of US-Iran tensions. Furthermore, they wanted to understand if the Indian defense sector had sufficient legs to outperform despite the structural upcycle in global defense sector witnessing headwinds. On Metals, investors wished to understand the reasons of more weakness in flats prices compared to longs, but in general appeared to be in wait and watch mode in the seasonally weak period. In case In terms of actionable, 1) Investors we met were positive on Solar Industries in Aerospace & Defense and JSW Steel in Metals & Mining; 2) Investors are weighing Hindustan Aeronautics (HAL) and Bharat Electronics (BEL) considering valuations and potential earnings surprises; 3) Among mid-caps, PTC Industries was discussed the most. A lot of investors also inquired on Shyam Metalics; and 4) In precision components machining space, investors favored Azad Engineering over others.

Amit Dixit
+91(22)6616-9008 | amit.dixit@gs.com
GS India SPL

Overall: Most of our interactions started with investors wanting to discuss the Defense space, particularly catalysts for individual stocks. Investors we met wanted to understand the potential order inflow in the next couple of years and the focus areas of the government in defense. They were broadly of the view that the defense spending will continue to rise, regardless of fiscal balancing between consumption and capex. However, they were circumspect of the weak order inflow thus far in Q1FY27. Most of the investors agreed that our themes of increasing TAM, Indigenization and Exports still stay relevant. Many investors we met wanted to understand the drone and radar electronics market in India. In Metals, investors wanted to understand the direction of steel prices, parity with imports and demand conditions. On valuations, there was a slight push back for JSW Steel and BEL, though investors were comfortable with HAL.

## Key points from discussion on Defense companies

Solar Industries (Buy): SOIL was the most discussed stock among large-caps and most of the investors agreed that it is a clear Buy among the Defense picks. In this

Kumari Rishika
+91(22)6616-9154 |
rishika.x.singh@gs.com
GS India SPL

stock, the most common question from investors was the sustainability of the recent stock price run-up. Investors wanted to get more details on the execution of the order book and there were queries around the participation of the company in the bidding for MALE UAVs. Also, there were queries on the near-term catalysts and likely TAM of 155mm shells and Counter-drone system (Bhargavastra). Certain sections of investors wanted to understand the earnings impact of the recent downtick in the Ammonium Nitrate prices and the key drivers behind the impressive growth of international (non-defense) business. Also, investors were wondering about the transition of the company from being an explosives' player to a complex platform player, bidding for the MALE drone project and the R&D capability of the company. That said, most of the investors are of the view while the stock appears to be expensive, the earnings growth and robust balance sheet seem to work in its favor and justify the valuations.

PTC Industries (Buy): PTCIL was the most discussed mid-cap stock in our meetings due to its steep earnings growth trajectory. Investors we met inquired on the order backlog, potential inflow and commissioning timelines of capacity. There was a broad-based acknowledgment of the company's existing customer base and investors wished to understand the competitive moat for the company. Some investors drew comparisons with Howmet Aerospace (covered by our US Aerospace & Defence analyst, Noah Poponak) and Precision Cast Corp (PCC) and wished to analyze the difference in business model, products and capabilities of both. There was a discussion of the entry barriers in the Titanium and Superalloys business and the relative margins of Castings and Ingots. There was a slight pushback on the FY-2 valuations, though most of the investors agreed if our earnings growth estimates are realised, the stock is not at a steep valuation. That said, some investors pointed out the relatively low trading volume in the stock. Most of the investors we interacted agreed that the company has a unique business model and leadership position in large castings space.

Bharat Electronics (Buy): A lot of investors we met were perplexed about the relative underperformance of BEL. Investors expressed concern if the margins have peaked out and the impact of sharply escalated semiconductor prices on the same. On order accretion front, investors seemed to be worried about the tepid inflow in Q1FY27 and wished to understand the timeline of QRSAM order. A lot of investors were wondering if the company's order book at <3x for revenue, implies that revenue growth is likely to slow down. Furthermore, investors wanted to understand in detail the order pipeline (and near-term catalysts) for the company and how long the revenue growth of plus-15% could last. A few investors also wished to understand the preparedness of BEL in executing new-age electronics orders on its own. On valuations, investors mentioned that the premium to HAL had expanded and the stock lacked attractiveness unless there is a positive surprise on order book accretion.

Hindustan Aeronautics (Neutral): Many investors seemed to have warmed up significantly for HAL compared to last marketing trip in Jan-26. Almost all the investors wished to understand if there was clarity on timelines pertaining to engine delivery from GE Aerospace (covered by our US Aerospace & Defence analyst, Noah Poponak) and delivery of 5 Tejas Mk-1A to the IAF. There was a consensus that the deliveries of Tejas Mk-1A are likely to commence from Sep'26 and from there on, the delivery of Tejas Mk-1A is likely to be contingent on engine deliveries from GE Aerospace. Most of the investors were of the opinion that integration issues on Tejas Mk-1A are likely to get streamlined soon and street is undermining the earnings from the delivery of

LCH-Prachand and manufacture of Su-30 MK-I. On the valuation front, most of the investors were fairly comfortable and mentioned that earnings cuts hereon are highly unlikely. They also mentioned that Repair and Overhaul (RoH) revenue is also likely to grow higher than 8%.

Bharat Dynamics (Sell): A lot of investors queried the recent sharp price uptick in the stock. While the investors were comfortable on the order book and expect a strong order inflow of INR 150bn in FY27 (including INR 100bn from QRSAM), they were concerned on the execution of the existing contracts. Many investors wished to understand the extent of external dependence on the platforms currently being executed to get comfort on the revenue in FY27/FY28. A lot of investors were also concerned on the management's guidance of EBITDA margin of 10-15%, during their interaction with the latter: while the investors agreed that >100% revenue growth is likely in FY27E due to spill-over of Akash Weapon Systems (AWS) execution in FY27, they were concerned on lack of export orders currently that is likely to adversely impact the margins.

Azad Engineering (Buy): Investors are familiar with the Azad stock and sought to compare the company's business model with other precision component manufacturing companies. Most of the investors liked the high earnings growth trajectory and margin profile of the company. Besides, Azad's existing customer profile and product portfolio also appears to be better compared to peers according to investors. However, investors seemed wary of high working capital requirement and capex intensity of the company. Per investors, the ongoing development of the ATGG engine and foray into the hot section of turbine through contract with Mitsubishi Heavy Engineering (MHE) are the two key catalysts for the company. A lot of investors also inquired about the fit of Azad to the Datacenter theme and development programs in Aerospace segment. Also, the company's moats and qualification timeline for its products were discussed.

Astra Microwave (Buy): Investors were trying to understand the reasons behind the recent sharp uptick in the stock price of the company. A few investors wanted to understand the company's strategy for Space vertical, Counter-drone system and IP-enabled products. Some investors were wondering if there was a case for Astra Microwave growing bigger and faster in the context of the government's focus on new age electronics and the company's involvement in key defense platforms such as Tejas Mk-1A, Su-30 upgrades, Space and Naval platforms etc. being rolled out. There were lot of queries on comparisons with Data Patterns and the differences in business model between the two companies.

Data Patterns (Buy): Most of the investors know about the strengths of the company and asked us about the sustainability of the robust margins. A lot of investors appreciated the IP-driven business model of the company but were puzzled by the sharp uptick in the stock price movement. Some investors inquired about the exports opportunity, particularly in light of possible Brahmos deal with Vietnam and UAE. Also, export opportunities for the company, particularly in light of the recent Precision Approach Radar (PAR) order were extensively discussed. Investors also wished to understand about the working capital cycle and overall R&D investment by the company.

## Key points from discussion on Metals & Mining companies

JSW Steel (Buy): Investors seemed fine with the volume growth trajectory of the company but inquired about the possibility of delay in projects and/or cost over-runs. A few investors wished to understand about the raw material security of the company and the peak net debt/EBITDA. Certain investors wanted to run the sensitivity of earnings to coking coal and steel prices. The only push-back we received was on valuation, as JSW Steel is the most expensive steel stock in the world (of companies with more than 3mtpa capacity) on EV/EBITDA (2yr-fwd) per Bloomberg consensus.

Tata Steel (Neutral): A lot of investors queried the extent of (India) realization uptick (QoQ) in Q1FY27 against management's guidance of INR 6,000/t. Few investors were of the opinion that in the near term, EU prices might go significantly up owing to regulatory changes pertaining to quota system and carbon border adjustment in Europe. Furthermore, some investors were of the view that India's realization might rise further in Q2FY27 owing to auto contracts getting negotiated at higher prices. A lot of investors we spoke to were of the opinion that downside in the stock appears relatively limited.

Jindal Steel (Neutral): Investors we interacted with primarily wanted to understand if the company would be able to deliver the volume growth of 20% YoY in FY27. Also, few investors were of the view that the recent weakness in the Jindal Steel stock price has tracked the downturn in longs prices and is overdone as the incremental volume growth of the company is likely to come in flats. That said, investors believe that the stock's price performance is likely to stay muted until Oct'26 when infrastructure activities start to pick up again, driving longs prices up. Some investors also wished to know if management plans to start providing volume updates every month and inquired about the completion of slurry pipeline project and ramp up of captive coal mining operations. Few investors also inquired on the next capacity expansion announcement by the company.

Shyam Metalics (Buy): Investors inquired on the company's vision FY31 and the key building blocks for the same. Investors wanted to understand the rationale behind the management's unique business model of having carbon steel, stainless steel and aluminium foil capacity under one roof. Also, they wished to understand the company's capability in standing up to the incumbents in stainless steel and aluminium foil. Investors also inquired on the capex intensity of the company and timeliness/adherence to the announced capex plans in the past. Investors also wanted to understand if the valuation of Shyam Metalics appeared excessive compared to peers.

NMDC (Sell): Most of the investors wished to understand the ratione behind our Sell call, despite better performance of RoE compared to steel companies. That said, investors agreed with our view that the management's plan of achieving 100mtpa of sales volume by FY30E looks like an uphill task. On prices as well, investors were concerned on the recent hike taken by NMDC, despite domestic downturn in rebar prices. Overall, investors were comfortable on valuations, but remain cautious on volume growth trajectory.

## Investment Thesis and Price Target Risks & Methodology for each stock

## PTC Industries

PTCIL was incorporated in 1963, and caters to aerospace, defense, oil and gas, power and marine industries. The company is setting up a 6,700tpa Ti ingot and 900tpa Superalloys ingot capacity and is also enhancing its casting capacity for both Ti and Superalloys casting. PTCIL is one of the few players in the world to have developed single crystal blade technology, used in hot part of the turbine/aero engine. PTCIL holds a unique position within the domestic processed material industry, being the sole player with capabilities to produce both Ti/SA in ingot and castings form. The global Aerospace Ti supply chain is already facing ongoing challenges from geopolitical conflicts. In this scenario, we see capacity ramp up at PTCIL's facility happening faster-than-expected and believe there is an ample opportunity within the domestic defense ecosystem, driven by the Ministry of Defence's (MoD's) focus on indigenization, and PTCIL is the only supplier for advanced hot turbine section components. We are Buy rated on PTCIL.

We estimate an EPS CAGR of 51% through FY35E, firmly placing PTCIL as one of the fastest growing participants in our India Defense coverage. Consistent with our approach for other stocks in our India Defense coverage, we derive our 12-month target price for PTCIL on a P/E-based methodology. Specifically, we discount PTCIL's FY31E EPS by its cost of equity (11.5%) to FY28E and apply a target multiple of 27x P/E (FY-2), corresponding to the global peer-set's average P/E (FY-2). Accordingly, our 12m TP for PTCIL is INR 25,770/sh on P/E methodology and implies a P/E of 191x and 64x on our FY27E and FY28E EPS respectively.

Key risks: Slower-than-expected ramp up of capacity, slower-than-expected aircraft build rates, delay in qualification.

## Solar Industries

SOIL started with the trading of explosives in 1983 and ventured into explosives manufacturing in 1996. It manufactures bulk explosives, packaged explosives, and initiating systems, which find application in mining, infrastructure and construction industries. The company forayed into the defense sector in 2010 and diversified into the manufacturing of propellants for missiles and rockets, warheads and warhead explosives. At present, there are 32 manufacturing plants in India, in addition to 7 overseas units.

Currently, SOIL plans to invest INR 127bn over the next 10 years to expand and diversify its capacity in high-margin defense segment. In our view, the company is well-positioned to benefit from a global shortage of energetic materials. On order books, the defense segment has an order backlog in excess of INR 155bn, of which INR 85bn is towards exports. The company is augmenting its capabilities by making a foray into focused segments such as UAVs, Medium and large carbine ammunition and Strategic systems. We also expect international non-defense business to be a key growth enabler as the company expands its presence in both existing and new geographies. On financials, SOIL has the best asset turns compared to global and local peers. Its cash conversion cycle of 90 days is the best among domestic defense companies. We are Buy rated on SOIL.

## Price Target Risks and Methodology

We derive our 12-month target price for SOIL on a P/E-based methodology. Specifically, we discount SOIL's FY31E EPS by its cost of equity (10.8%) to FY28E and apply a target multiple of 57x P/E (FY-2), corresponding to its 18-month mean. As a result, our 12m TP for SOIL is at INR 19,590/sh and implies a P/E of 77x and 69x P/E on FY27E and FY28E EPS, respectively. We are Buy rated on SOIL.

Key risks: 1) Delay in defense orders 2) Expansion in unchartered defense domains 3) Hyperinflation risks in international geographies

## Azad Engineering

Azad Engineering was incorporated in 2008, and manufactures rotating airfoil portions of turbine engines and other critical products for defense and civil aircrafts, defense missiles, nuclear power, hydrogen, gas power, oil and thermal power. The precision forged and machined components manufactured are highly complex and mission-critical and hence, some of them have “zero PPM” defects requirement. Currently, Azad is on a steep earnings’ trajectory, enabled by vast TAM and a book/bill of 14.2x, but with constrained free cash generation potential due to sustained capex and working capital needs. We see two key catalysts for the company: 1) DcPP for ATGG engine will catapult Azad from being a component supplier to a solutions provider. The use case of an indigenous ATGG engine is significant as it can potentially power RPVs and LRSAMs; and 2) Progress on MoU with Baker Hughes in KSA under the “Made in Kingdom, for the kingdom” program. We are Buy rated on Azad.

We derive our 12-month target price for Azad on a P/E based methodology. Specifically, we discount Azad's FY33E EPS by its cost of equity (13.3%) to FY28E. We apply a target multiple of 26x, corresponding to the global peer-set's average P/E (FY-2) in view of the limited trading history of the stock. Our 12m TP for Azad is at INR 2,460/sh on

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
