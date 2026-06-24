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
# ASIA STRATEGY BASKET

# Built for Orbit: Introducing Asia Space Economy Basket (GSSZSPCE)

We see a compelling relative risk/reward in Asia Space Economy stocks, supported by structural demand, measurable earnings delivery, policy support, and under-positioned thematic flows.

The Space Economy is in an active deployment phase. Satellite launches reached 4,400+ in 2025 (+65% YoY), with \~70,000 additional satellites targeted over the next five years. Our Technology equity analysts forecast the LEO satellite market to expand 7× to US\$108bn by 2035. Sovereign constellation programs are already in funded execution through 2028, providing non-discretionary demand independent of end-user adoption.

Asia's role in the global supply chain is critical. Asia represents the hardware backbone of the global buildout, spanning satellite buses and payloads, rocket engines, RF/GNSS chips, phased-array antennas, earth observation instruments, and in-orbit servicing. China, Japan, Korea, Taiwan, and India occupy distinct but complementary positions across the value chain, supported by contracted order books and government-backed programs.

Theme broadening, with AI convergence extending duration. Orbital AI compute is moving into procurement in 2026, driven by terrestrial energy and permitting constraints. The linkage to AI infrastructure capex broadens the investment case and extends the duration of the theme beyond pure space deployment.

Thematic flows are accelerating. Global space-themed funds and ETF AUM have reached \~US\$25bn at peak across 40+ products, up from only \~US\$1bn at the beginning of 2025. However, Asia supply chain companies remain structurally underrepresented, creating a clear gap between positioning and fundamentals.

Structural Investment Opportunity: We introduce the Asia Space Economy basket (GSSZSPCE), focused on companies with direct or supply chain exposure across four categories: (1) Upstream — Launch & Propulsion, (2) Satellite Manufacturing & Components, (3) Ground Segment & Downstream Applications, and (4) Space-Grade Materials & Electronics. The basket has outperformed broader markets since 2025, while trading in a consolidation range over the past 3 months.

Valuation and earnings support an attractive risk/reward. Asia Space Economy stocks are trading at deep discounts to global peers (-60% P/E; -25% P/B), with relative valuations near the low end of the historical range, despite supportive earnings momentum, suggesting fundamentals are not yet fully reflected in pricing.

## Alvin So, CFA

+852-2978-1585 | alvin.so@gs.com
GS (Asia) L.L.C.

Timothy Moe, CFA
+65-6889-1199 | timothy.moe@gs.com
GS (Singapore) Pte

Kinger Lau, CFA
+852-2978-1224 | kinger.lau@gs.com
GS (Asia) L.L.C.

Bruce Kirk, CFA
+81(3)4587-9950 | bruce.kirk@gs.com
GS Japan Co., Ltd.

Sunil Koul
+44(20)7051-4931 | sunil.koul@gs.com
GS International

John Kwon
+65-6654-6337 |
jongmin.kwon@gs.com
GS (Singapore) Pte

Amorita Goel, CFA
+65-6654-5445 | amorita.goel@gs.com
GS (Singapore) Pte

## Lift-Off to a New Growth Frontier

The Space Economy — Scale and TAM Growth
The Satellite Industry Association (SIA)'s Annual State of the Satellite Industry Report estimates the global space economy at US\$429bn in 2025 (+3% YoY), including US\$303bn in revenues across the commercial satellite value chain.

Deployment activity continues to accelerate: 4,434 satellites were launched in 2025 (+65% YoY), bringing the total number of operational satellites to 14,266. Within the value chain, commercial launch revenues grew 33% to US\$12.4bn, satellite manufacturing reached US\$20.4bn, and satellite ground network revenues increased 8% to US\$165bn.

Looking ahead, with \~70,000 satellites targeted for launch over the next five years, our Technology equity analysts forecast the LEO satellite market to expand 7× to US\$108bn by 2035, implying a \~20% CAGR over 2024–35E. In upside scenarios, the TAM could double in a bull case and potentially quadruple in a blue-sky scenario.

Broader industry estimates point to a similarly large opportunity set. The World Economic Forum and McKinsey project the overall space economy to reach US\$1.8tn by 2035, while Novaspace estimates the market could exceed US\$1tn by 2034. Multiple programs are now competing for this TAM, with Asia's supply chain manufacturers positioned to benefit across the deployment cycle.

The Asia opportunity is centred on manufacturing but also extends across a broader economic footprint, including connectivity, earth observation, logistics, climate and agriculture analytics, and digital infrastructure. Deloitte and the Singapore Space & Technology Think Tank estimate that earth observation services alone could contribute \~US\$100bn to ASEAN GDP by 2030.

Exhibit 1: US remains the most active player in launching activities globally, while China is the most active player among Asia  
![](images/3fa077eda37007d6f83d13e6f48bf54ac3da86de7994935192f8475a05e9078b.jpg)  
Source: Our World in Data, Orbital Radar

Exhibit 2: Global space object launches (primarily satellites) surged by \~60% to over 4,500 annually in 2025

![](images/d304e458cd944b3d6d9dfd6f30de13e29809b58e65de216bd3c2a8613a70ec47.jpg)  
Source: Our World in Data, Orbital Radar

Exhibit 3: Our Technology equity analysts forecast the LEO satellite TAM to increase from US\$15bn to US\$108bn over 2024–35E  
![](images/ffe692b84ac93d9a02dc45409da7ca5231acead72cb6054d7ab78ac86eb18cb5.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: Governments across global economies have committed to increased space investment and spending

![](images/53df7a9bff8f5bd0aceaa82426f1496261d7601cd65a90d62dc7f29d52e39c7e.jpg)  
Source: Novaspace, GS Global Investment Research

The distinction between core/established and early-growth/emerging segments is important in assessing exposure to the theme. We believe core positioning should be anchored in contracted, revenue-generating segments, while emerging areas are better viewed as optionality.

We map the value chain across time horizons, growth profiles, and Asia's role in the supply chain:

## Core / Established

■ Launch Vehicles: The key enabler. Reusability-driven cost declines have unlocked downstream scale. Asia has the broadest non-US launch base, spanning China (state and private), Japan (H3), and India (ISRO and emerging private players).

Satellite Manufacturing: Strongest order book visibility, with sovereign constellations anchoring non-discretionary demand. China leads on scale and integration; Japan on precision systems; Korea is scaling production; Taiwan specialises in subsystems and components; India remains early but is ramping rapidly.

■ Ground Electronics & Infrastructure: The largest segment and most direct volume lever. Satellite deployment mechanically drives hardware demand with limited execution risk. Taiwan dominates RF/GNSS and phased-array components, while Korea and Japan supply network and ground systems.

Earth Observation & Data Services: The most mature downstream segment, supported by recurring data revenues. Japan and India anchor supply; Southeast Asia is the fastest-growing demand market, with Singapore serving as the regional hub.

■ LEO Satellite Connectivity / Broadband: The clearest near-term monetisation pathway. Maritime and aviation lead adoption given meaningful cost advantages versus legacy services. Asia Pacific is a key growth market, with Taiwan, Korea, and Japan supplying core connectivity hardware.

## Early-Growth / Emerging

■ Space Sustainability / In-Orbit Services: Structurally non-discretionary, as LEO congestion scales with deployment. Japan holds a near-monopoly position globally in commercial in-orbit servicing.

Orbital AI Compute / Space Data Centers: Moving into early-stage procurement in 2026, driven by terrestrial energy and permitting constraints. The linkage to AI capex broadens investor relevance. Japan, Korea, and Taiwan are the key hardware beneficiaries.

\- Direct-to-Device / Connected Mobility: Evolving from a niche to an integrated connectivity layer. 6G standardisation is expected to embed D2D structurally. China leads in EV integration, while Taiwan, Korea, and Japan supply core components.

\- Space Pharma / Microgravity Manufacturing: Scientifically validated but commercially early-stage. Regulatory frameworks remain nascent. Asia’s role is currently focused on launch access and payload return logistics (India and Japan), with long-duration optionality.

## Asia Supply Chain — Distinct Market Exposures

We frame the opportunity as geographically diversified but thematically coherent, with each market offering differentiated exposure across the value chain:

China, Japan, and Korea — High exposure: Positioned upstream across launch, satellite manufacturing, and system integration, where contract values are highest and visibility is multi-year. China’s ramp is largely non-discretionary through 2028, driven by ITU filing timelines. Japan adds a differentiated sustainability angle (e.g. Astroscale), while Korea is building toward commercial scale with a more integrated model across launch, manufacturing, and data.

Taiwan — Moderate to high exposure: Positioned in ground electronics, the largest segment by revenue. Established supply chain relationships with global constellation operators provide relatively low execution risk, though exposure is further downstream.

India — Moderate exposure: Reflects a sector still in early commercial scale-up, but with a broad three-pillar opportunity set over the next 3-5 years.

ASEAN/Singapore — Low to moderate exposure: Primarily a demand market and regional hub today, with potential for incremental manufacturing exposure over time as supply chains reallocate.

In parallel, sovereign programs are moving into funded execution, including Japan's JPY1tn Space Strategy Fund, Korea's KRW200bn private space fund, India's IN-SPACe VC facility, and Singapore's NSAS.

Exhibit 5: Asia Space Supply Chain — Market Positioning

<table><tr><td>Market</td><td>Space Economy Exposure</td><td>Value Chain Tier</td><td>What Asia Makes and Sells</td><td>Government Anchor &amp; Target</td></tr><tr><td>China</td><td>High</td><td>Full-Stack:Upstream To Downstream</td><td>Satellite bus, payloads, and subsystems at industrial scale (mass production, smart factories)Liquid and solid rocket engines, incl. reusable launch vehicles targeting &lt;20,000 yuan/kgIntegrated commercial spaceport cluster (700+ companies)RF and ground electronics (broad domestic supply chain)EO data platforms and downstream analytics (agriculture, logistics, climate)Emerging: in-orbit services, space tourism, microgravity manufacturing</td><td>CNSA Commercial Space Action Plan 2025–27; commercial space as core national pillar•ITU-driven sovereign constellation deployment (through 2028)National development fund with patient capital•20+ provincial space industrial policies</td></tr><tr><td>Japan</td><td>High</td><td>Upstream:Launch, Propulsion, Satellite Bus, In-Orbit Sustainability</td><td>Heavy/medium launch vehicles (accelerating cadence)Rocket propulsion systems (high reliability)Satellite bus and system integration (scaling production)Solar arrays and satellite power componentsGround electronics, EO instruments, satcom systemsIn-orbit servicing (only commercial debris-removal capability in operation)</td><td>JPY1tn Space Strategy Fund (10-year,JAXA-led)Targets: low-cost launch, domestic supply chain, GEO refuelling, microsatellite swarmsGoal: 2nd-largest national space program globally</td></tr><tr><td>South Korea</td><td>High</td><td>Midstream:Launch Systems, Satellite Manufacturing</td><td>Rocket engine manufacturing and KSLV-III (preliminary design from 2026)Mass-production satellite facility (operational late 2025)SAR/EO satellite systems (exported to 7+ countries)Integrated space infrastructure model (conglomerate-led)Small satellites, structural components, precision manufacturingEmerging space data services and analytics</td><td>KASA established 2024 • KRW200bn private space fund • KRW1.2tn SAR constellation contract under evaluation (Oct 2026 milestone)•Target: top-7 global space power by 2045</td></tr><tr><td>Taiwan</td><td>Moderate-High</td><td>Midstream:Ground Electronics, RF/GNSS Subsystems, LEO H/W</td><td>RF front-end modules and phased-array antennas (linked to semiconductor strength)GNSS chips, controllers, baseband electronicsPCBs, fibre connectors, precision electronics (dominant revenue driver)Satellite subsystems and payload componentsCubeSat platforms and miniaturised manufacturingSemiconductor packaging and radiation-tolerant chips</td><td>NT$27bn 6G/satellite alliance (6-year)•NT$1tn production target by 2029–30•TASA Emerging Star Plan•Space Development Act (2021)</td></tr><tr><td>India</td><td>Moderate</td><td>Mid-To-Downstream:Launch, Manufacturing, EO Data</td><td>Government/private launch vehicles (multi-payload capability)Satellite manufacturing scaling (300+ startups under IN-SPACe)NavIC/IRNSS domestic navigation systemEO analytics (agriculture, logistics, water, disaster response)Component manufacturing (structures, propulsion, electronics)Emerging space pharma logistics</td><td>IN-SPACe PPP framework•Fully liberalised FDI (satellites, launch, ground systems)•Target: US$44bn sector by 2033 (vs ~US$8.4bn today)•WEF ecosystem initiative</td></tr><tr><td>ASEAN / Singapore</td><td>Low-Moderate</td><td>Downstream:EO Data Demand, LEO Connectivity</td><td>Singapore as regional HQ/financial hub (~70 companies, ~2,000 professionals)High-growth EO demand (agriculture, maritime, O&amp;G, utilities, climate)LEO broadband bridging infrastructure gaps (US$40bn+ potential benefit)Emerging manufacturing/assembly footprint</td><td>Singapore NSAS (Apr 2026), SGD200mn+ committed•Deloitte-SSTL:EO~US$100bn ASEAN GDP contribution by 2030•Vietnam-Japan cooperation; national programs across SEA</td></tr></table>

Source: Various news, government, and industry sources (e.g. Bloomberg, The Economist, SIA, Novaspace, Invest India, Japan Earth Observer, Focus Taiwan, China in Space), company data, GS Global Investment Research.

## Investor Flows and Thematic Positioning

Space-themed funds have seen meaningful inflows since 2015 (+US\$19bn), with aggregate AUM reaching US\$25bn at peak across 40+ funds globally, up from \~US\$1bn at the beginning of 2025. Among the top 10 funds by AUM, six are ETFs, accounting for roughly 50% of assets in the theme. Recent ETF launches by multiple asset managers reflect growing institutional demand for dedicated exposure. That said, flows remain concentrated in US-listed names. Asia supply chain companies remain underrepresented in global thematic allocations and index benchmarks — a structural gap that we believe represents a key source of potential alpha for Asia beneficiaries.

Over the medium to longer term, continued sovereign program execution, convergence with AI infrastructure, and increasing institutional participation should support sustained investor interest across the space economy value chain.

Exhibit 6: Space-themed funds have seen meaningful inflows since 2015, with aggregate AUM reaching US\$24bn across 40+ funds globally  
![](images/1dbeb9cfe28dda6496dec76750f1d32351c125ba241bae3f879c327a6bb74add.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 7: Asia supply chain companies remain materially underrepresented in global thematic allocations, with a few exceptions in China-domiciled funds  
![](images/82d4662e00d545e69c574c473a5a0c85ebc34cccc9ab2368ea4b3d140ca771dc.jpg)  
Source: Bloomberg, GS Global Investment Research

## Asia Space Economy Basket (GSSZSPCE)

Our Asia Space Economy (GSSZSPCE) basket comprises companies with direct or supply chain exposure to the space economy, across four business categories: (1) Upstream — Launch & Propulsion, (2) Satellite Manufacturing & Components, (3) Ground Segment & Downstream Applications, and (4) Space-Grade Materials & Electronics. The basket includes 53 constituents, with 4, 16, 18, and 15 stocks in each segment, respectively, contributing 16% /40% / 26% / 18% of basket weight.

Asia Space Economy stocks have delivered meaningful outperformance vs. broader regional markets since 2025, led by Korea and Taiwan names. The rally was most pronounced in late 2025, with performance subsequently consolidating. At the segment level, Satellite Manufacturing & Components has been the clear outperformer, reflecting strong order book visibility and direct exposure to the constellation deployment ramp. Upstream — Launch & Propulsion saw a sharp run-up into February, followed by a pullback, while Ground Segment & Downstream Applications has lagged, suggesting markets are prioritizing near-term earnings delivery, with volume-driven downstream plays yet to re-rate.

Earnings momentum remains supportive, with Asia Space Economy stocks continuing to deliver positive growth and upward revisions, led by Japan and Korea, partially offset by weaker trends in China. Valuations remain compelling for Asia Space Economy stocks, which are trading at deep P/E (-60%) and P/B (-25%) discounts to global peers, with relative valuations near the low end of the historical range.

During April–May, Asia supply chain names underperformed global peers after tracking broadly in line earlier in the year. We view this divergence as flow-driven, with strong inflows into space-themed ETFs disproportionately benefiting globally listed names. Relative performance has rebounded since June, as US peers likely faced liquidity drag, while Asian stocks remain structurally supported as beneficiaries outside the US.

We see this dislocation as creating a compelling relative risk/reward opportunity for Asia supply chain exposures, supported by a constructive fundamental backdrop.

Exhibit 8: Asia Space Economy stocks have outperformed the broader regional equity market since 2025, led by Korea and Taiwan suppliers, although performance has recently consolidated following a strong rally in late 2025

![](images/511837023c9e8a26469cc92464664689720d46cf55abfeea2e8620a3cf04e907.jpg)  
Source: FactSet, GS Global Investment Research

Exhibit 9: Satellite Manufacturing & Components has been the strongest performer, while Ground Segment & Downstream Applications has lagged, while Launch & Propulsion has seen a drawdown after peaking in February

Indexed Performance of Asia Space Economy Basket by Segment (USD)  
![](images/37e9996d50c1f2bcffc3967f2ae21c81e8ba26232af5f

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at

https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
