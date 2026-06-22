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
![](images/6e461d2f331ca628b46445d72dc859db7a9ce4f959360ee2115b2b8ff05ab2ea.jpg)

EUROPE ENERGY: OIL SERVICES

## The AI and Digital transformation in Oil & Gas: time to market, cost curve and oil service beneficiaries

In this report, we assess how AI, high-performance computing and digitalisation are reshaping the economics and time to market of global oil & gas projects, drawing on discussions with 15+ digital departments of integrated majors, upstream independents, oilfield services, seismic providers and digital vendors as well as our proprietary Top Projects analysis. We focus on two main questions about long-term offshore projects — by how much could AI/digitalisation compress project timelines and how materially could it shift the economics of new oil developments — at a time when the industry is facing falling reserve life and increasingly complex geology. We draw five key conclusions:

1. AI/digitalisation together with simplification and standardisation offers the potential to compress the full greenfield deepwater cycle from 12 years to 7 years (-c.38%) on average. The gains are heavily front-loaded, with 90% of the time saving captured before FID: exploration -55%, appraisal -40/50% and FEED 40-50%.

2. Post-FID, the benefits become less obvious, as the bottleneck moves to physical fabrication. Construction time could compress by 5-10% and FPSO fabrication remains at c.4 years, governed by yard capacity, steel and long-lead equipment, with limited flexibility.

3. Post start-up, we see material benefits from digital twins and predictive maintenance, as well as improved drilling efficiency, with scope to reduce opex by 10% and improve uptime by 200-300 bp. We also see the benefit of improved near-field exploration success prolonging the life of existing infrastructure, with Norway as a leading example.

4. AI is a meaningful driver of upstream economics. Our AI scenario implies an uplift in a typical greenfield IRR by 3.5pp (from 15.5% to 19.0%) and a cut in breakevens by c.15% through four levers: capex -10% (+1.9pp IRR), time to market -3 months (+0.8pp), production +3% (+0.5pp) and opex -10% (+0.3pp) relative to an average greenfield project in the previous capex cycle.

5. Flowing these improvements into our 2026 Top Projects cost curve, the 75th percentile breakeven would move from \$75/bbl to \$64/bbl (at 13-18% WACC) — with capex and time to market, not opex, doing most of the work.

Michele Della Vigna, CFA
+39(02)8022-2242
michele.dellavigna@gs.com
GS Bank Europe
SE - Milan branch

Ati Modak

+1(212)902-9365

ati.modak@gs.com

GS International

Anastasia Shalaeva
+971(4)214-9908
anastasia.shalaeva@gs.com
GS International

Yulia Bocharnikova +44(20)7051-6299

yulia.bocharnikova@gs.com
GS International

Quentin Marbach
+44(20)7774-7644
quentin.marbach@gs.com
GS International

Will Chen
+971(4)214-9942
will.y.chen@gs.com
GS International

Neil Mehta

+1(212)357-4042

neil.mehta@gs.com

GS & Co. LLC

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

The bankability of these levers varies. We group them as proven (drilling efficiency, seismic processing, production uptime, topside debottlenecking, gas-lift optimisation), emerging (predictive maintenance, autonomous platforms) and aspirational (step-change in recovery factors, improved sub-surface) — and we include only the first two in our analysis.

We map these conclusions into subsector implications for the oil & gas value chain. The producers would benefit from shorter time to market and lower costs, while we see more differentiation in services, with the enablers and structural beneficiaries of AI adoption standing out — in this context, we highlight TGS (Buy) for its independent subsurface multi-client library, the critical input for AI-driven seismic and exploration workflows, Vallourec (Buy) for the OCTG intensity of a faster, higher-throughput drilling cycle and SLB (Buy) for its leading digital business.

We spoke with companies across the oil & gas value chain — spanning integrated majors, upstream producers, services, seismic providers and digital vendors — to assess where AI could have the most tangible impact. Two questions frame our analysis: how much could AI compress project timelines and how materially could it impact the economics of oil projects and the overall Top Projects cost curve.

On time to market, AI is already delivering a clear step-change — but almost entirely pre-FID. In this report we model potential time savings enabled by AI/digitisation, estimating that AI and high-performance compute could compress the full greenfield deepwater cycle from c.12 years to c.7 years on average, a reduction of c.38%. The gains are heavily front-loaded, with 90% captured before final investment decision: exploration shortens by 55%, appraisal by 40-50% and FEED by a similar 40-50%, driven by faster seismic processing, automated interpretation and AI-enabled engineering workflows. By contrast, post-FID phases remain structurally constrained — construction compresses by only c.10% and FPSO fabrication remains effectively fixed at c.4 years, governed by yard capacity, steel fabrication and equipment lead times.

On the economics of oil projects, AI is emerging as a meaningful driver of upstream economics through four core levers: capex reduction (\~+1.9pp IRR), faster time-to-market (\~+0.8pp IRR), production uplift (\~+0.5pp IRR) and opex savings (\~+0.3pp IRR) on our estimates. In aggregate, our assumptions (capex -10%, opex -10%, \~3 months faster delivery, \~3% higher lifetime production) imply an uplift in a typical greenfield IRR from 15.5% to 19.0% (+3.5pp) and 15% cut in breakevens. Translated to our Top Projects cost curve (Exhibit 2), the 75th percentile could move our long-term Brent forecast from \$75/bl to \$64/bl.

The IRR uplift decomposes into four drivers in order of contribution. 10% capex reduction is the largest, driven by faster well design and execution (operators are quoting 20-25% reductions in drilling time and engineering cycles compressed from months to weeks). Closely behind is time to market (-3 months), which comes from compressing the subsurface-to-FID phase where companies report that seismic interpretation is now 5-10x faster and prospect prediction success has moved from \~50% to \~75% in pilot basins. On the operating side, production uplift (+3%) stems from AI-enabled optimisation of field performance: real-time tuning (e.g. artificial gas lift), digital twins identifying bottlenecks and improved uptime through predictive analytics. This effectively increases output from the same asset base. Finally, the 10% opex reduction is the smallest contributor but the most visible operationally, with autonomous platform concepts targeting around -25% platform opex and predictive maintenance aiming at -20-30% maintenance cost and reducing unplanned downtime.

We group these drivers into three buckets to flag where the numbers are bankable today versus where they are still aspirational. Proven levers — faster drilling, seismic acceleration, production efficiency, topside debottlenecking, gas-lift optimisation — are already delivering measurable results across multiple operators and underpin the bulk of the IRR uplift. Emerging levers — predictive maintenance, autonomous platforms — have credible pilots and vendor evidence but limited at-scale track record. Aspirational levers — step-change recovery factor uplift — remain a 5-10 year story and we do not reflect these.

## Stock implications. We see the most potential for companies that either enable AI adoption or structurally benefit from it.

On the enabler side, we highlight TGS (Buy), which in our view is well positioned to capture AI-driven upside in oil services through ownership of the largest global multi-client seismic library (controls \~60% of global multi-client data acquired since 2018), with strong exposure to key basins, supported by extensive seismic, well log, production and geological datasets. As AI adoption accelerates, access to high quality proprietary subsurface data becomes a gating factor, creating recurring, high-margin monetisation opportunities.

In a structural beneficiary context, we note Vallourec (Buy) for the OCTG intensity of a faster, higher-throughput drilling cycle. As AI improves subsurface imaging and well placement, operators are unlocking deeper, higher pressure and more technically demanding reservoirs, structurally reinforcing demand for high-spec OCTG. In our view, Vallourec stands out in this respect: its premium connections, corrosion-resistant alloys and integrated tubular solutions are specifically engineered for harsh-environment and HP/HT applications — a differentiated offer mass-market mills cannot easily replicate. We see this as supportive of both volumes and pricing, positioning Vallourec as a leveraged beneficiary of upstream digitalisation.

We also highlight SLB (Buy) as a key beneficiary of accelerating digital spend in oil & gas. According to SLB, industry IT penetration remains underinvested at \~4–6% of capex versus \~10–12% in peer industries, a gap the company expects to narrow over time. The company estimates its addressable digital market at \~\$25bn today, expanding to \~\$35bn by 2030 (with upside to \~\$50bn driven by AI adoption), with SLB already exposed to about two-thirds of this opportunity. SLB's competitive edge is anchored in domain-specific AI. While generic LLMs are optimised for text, upstream workflows require processing complex subsurface and engineering data. SLB's combination of proprietary datasets, deep domain expertise in oil & gas data structures and understanding of cross-functional operator workflows positions it to design fit-for-purpose AI applications with higher utility and adoption versus generic models, which typically require significant modification and often struggle with technical data. We view this integration of data, domain knowledge and workflow-specific model

Changes to 2026 Top Projects cost curve under our AI scenario design as a significant moat that should benefit SLB and sustain its leadership in oilfield digital and software.

We are more cautious on FPSO contractors and pure subsea construction where the bottleneck is physical fabrication rather than digital workflows.

Exhibit 1: Time to market of a deepwater oil project: potential AI-enabled reduction vs baseline

Total project lifecycle — AI / LLM / compute compress time-to-first-oil by \~38% (\~11.6 yrs → \~7.2 yrs)
Baseline 11.6 yrs → AI-enabled 7.2 yrs | saving of 4.4 years (-38%)

![](images/6d2d0a46e83412b34c5a353d93ed0ed77745816ccafddb0fb8060d2b12175799.jpg)

![](images/130480097af19b675ab98f9ff882fd96d21f0dff796258339be397692da29ae0.jpg)  
Block durations match the individual stage charts. Overlap between blocks: baseline 20% / 20% / 0%; AI scenario 30% / 40% / 0%.  
The AI/LLM/Compute-enabled time frame range in the exhibits is based on aggregated feedback from our industry discussions, with the estimated time savings at the midpoint.

Source: Company data, GS Global Investment Research

## Exhibit 2: At 11-15% commercial WACC, the 75th percentile of the oil cost curve would move from \$66/bbl to \$57/bbl

![](images/f1145eadcb5d4cf7ca163b4efd51f73b7ec71edc56ef9b9b7f7a986d806bdb34.jpg)  
Source: GS Global Investment Research  
Exhibit 3: We estimate AI could lift the IRR of an average greenfield field by 3.5pp, with capex and time-to-market driving most of the uplift  
IRR decomposition of our AI scenario on an average greenfield field

![](images/abb39d25defcf4cfb1d64f74eebe3b7c80a55e3af5fe823f0b4e54f2d282fdfc.jpg)  
Source: GS Global Investment Research

## Exhibit 4: Drivers of the improvement of oil field economics through AI

## AI levers on a producing offshore field

Productivity and cost levers — sized for a typical deepwater hub. Sourced from operator and vendor calls.

<table><tr><td colspan="2">Productivity levers</td><td>more barrels from the same hardware</td></tr><tr><td>LEVER</td><td>HOW IT WORKS</td><td>EXAMPLE OF WHAT IT CAN DELIVER</td></tr><tr><td>Higher exploration &amp; infill discovery ratePROVEN</td><td>AI-driven seismic processing and interpretation surface prospects a human eye misses, and reduces bias in well-targeting. Same seismic dataset, more (and better-ranked) drillable targets.</td><td>Seismic processing time 1-2 months vs 12-18 (5-10× speed-up, up to 50×)Prospect prediction rate 50% → 75% on difficult carbonates (blind tests)</td></tr><tr><td>Topside debottlenecking (digital twin)PROVEN</td><td>Live virtual copy of the FPSO topside, fed by real-time sensors. Spots the single weakest link capping throughput (separator, compressor, pump) and simulates the best operating settings before changing anything on the real plant. Best settings then replicated across sister vessels.</td><td>Guyana example: a digital twin was deployed across the 4-FPSO fleet, allowing engineers to compare vessel-to-vessel and re-tune topside operating settings live. Overall production increased by ~100 kboed (+12%) with no new wells and no new equipment — purely from replicating best-vessel parameters across sister hullsVendor framing: +2-4% production = the whole value of an AI exercise on a producing facility (equivalent to a 20-40% reduction in unplanned downtime)</td></tr><tr><td>Production efficiency / uptimePROVEN</td><td>AI ingests historical failures + live sensor data, predicts which piece of kit is about to trip the plant, and triggers intervention before it does. Higher availability = same nameplate runs closer to 100%.</td><td>Large producing hubs are pushing production efficiency into the 96-99% range, with 2-5 ppts attributable to AI. On equipped rigs, unplanned downtime is now &lt;1% vs 3-5% historically.</td></tr><tr><td>Real-time artificial gas-liftPROVEN</td><td>AI continuously adjusts the volume of gas injected into each producing well based on live downhole data, keeping every well at its individual sweet spot rather than a fleet-average setting.</td><td>+3-5% production per well in onshore tight-oil basins</td></tr><tr><td>Recovery-factor uplift (4D + reservoir AI)ASPIRATIONAL</td><td>Agentic AI ties seismic, flowlines, facilities and reservoir model into one live system, identifying bypassed oil and the best wells / EOR scheme to drain it. Needs operator subsurface data — still siloed.</td><td>Deepwater target: +2-5 ppts recovery factor</td></tr><tr><td colspan="2">Cost levers</td><td>lower opex and maintenance capex</td></tr><tr><td>LEVER</td><td>HOW IT WORKS</td><td>EXAMPLE OF WHAT IT CAN DELIVER</td></tr><tr><td>Faster drilling timePROVEN</td><td>Real-time AI on rig sensor data (geosteering, drilling parameter optimisation, invisible-lost-time elimination) shortens days-per-well; AI-assisted well design shortens the planning cycle that precedes the rig. Fewer rig days = lower well capex.</td><td>Drilling time -20-25% on modern rigs; 10-20% efficiency gain in Permian shale (replicable in deepwater)Well design cycle 5-12 months → 50% quicker17-stage well planning process: 6 months → 1 month</td></tr><tr><td>Autonomous platforms (eliminate offshore human element)PROVEN</td><td>Topside operations run from an onshore control room using a digital twin + AI agents. Platform manned only periodica

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
