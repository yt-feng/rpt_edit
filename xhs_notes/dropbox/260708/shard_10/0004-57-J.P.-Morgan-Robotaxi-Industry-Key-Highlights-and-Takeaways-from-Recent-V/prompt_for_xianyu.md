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
## Robotaxi Industry

## Key Highlights and Takeaways from Recent Videos, Podcasts and News Developments

The evolving robotaxi landscape is relevant to our coverage of TSLA, RIVN, F, GM, and key auto tech supply chain names (APTV, VC, MGA, INVZ). In this update (click here for our previous update and also click here for our robotaxi deep-dive and TSLA deep-dive), we’ve pulled together key highlights from the steady stream of videos and podcasts that surface on this industry each week. Key incremental takeaways were: 1) Robotaxi scaling accelerates — TSLA launched unsupervised Robotaxi in West Miami on July 3, while a production Cybercab with no wheel or pedals is now self-driving in Austin as an engineering test and the Cybercab cleared onto the Texas DPS first-responder registry, and management teased a July 7 Giga Texas scaling announcement; 2) FSD software and regulatory momentum both build — v14 Lite began rolling to the \~4mn HW3 fleet on 6/29 with encouraging early feedback, while European approval advances country-by-country (Finland eyeing a fast-track), though the EU-wide vote slips to October with Sweden pushing a no over speed-limit compliance; 3) TSLA launched the stretched three-row Model YL in the US at \$61,990, confirmed a Giga Berlin ramp toward 7,500/wk from October on a European demand rebound, and is running FSD validation testing on the refreshed Semi; 4) Waymo exited its Phoenix Uber pilot and incorporated a German unit, Zoox unveiled its production-intent redesigned robotaxi ahead of a ramp to 100/wk, and Wayve advanced its OEM-licensing model (Stellantis, Nissan) alongside an \$85 mn private markets sale; and 5) Regulatory backdrop turns more permissive — NHTSA moved to drop the manual brake-pedal mandate for ADS-only vehicles (a direct precondition for purpose-built robotaxis like Cybercab and Zoox), while UNECE adopted the first global ADS technical regulation, setting a shared safety floor across the US, China, EU, Japan, Canada and the UK. We focus on resources that have consistently proven valuable and reliable in our research process, but we welcome any suggestions from investors on what they’re watching, listening to, or reading. Below are quick summaries of the most value-add content we’ve come across in recent weeks:

## Podcasts & Videos:

\- On Brighter with Herbert, TSLA VP of Vehicle Engineering Lars Moravy discussed Cybercab, Optimus, manufacturing and AI, teasing a major scaling announcement tied to the Giga Texas campus on July 7 and characterizing the \~150 Cybercabs on site as a test fleet with the majority in Autopilot training, running versions that still carry steering wheels and pedals, with burn-in begun on a new campus-edge track, lines installed and over 90% automated, and the ramp roughly where expected, which he credited to scars from production hell, virtual commissioning and pre-ship machine testing. He framed Cybercab as its own platform built for scale, analogizing the transition to hard disks giving way to solid-state flash (cheaper, faster, more reliable, more durable), argued its key underestimated advantage is end-to-end efficiency from raw material through vehicle + charging, and named Zoox as a fellow white-sheet competitor while characterizing Waymo as buying cars and adding compute. He expects Cybercab to outsell Model Y and noted Starlink integration is being explored. On factory AI utilization, he detailed code generation for software teams, an internal agent aggregating owner and lessons-learned data, anomaly detection on equipment KPIs, linked systems feeding end-of-line body scans upstream into tolerance changes, and cars self-driving from end-of-line. On Optimus, he said Fremont is transitioning to Optimus, with the first modular

Autos & Auto Parts

Rajat Gupta AC

(1-212) 622-6382

rajat.gupta@JPM.com

Jash Patwa

(1-212) 622-5472

jash.patwa@jpmchase.com

Yash Beswala

(1-212) 622-0028

yash.beswala@jpmchase.com

JPM Securities LLC

See page 12 for analyst certification and important disclosures.

line landed and roughly $\sim$ 40 more to go, and emphasized that Optimus benefits from TSLA's manufacturing, actuator and motor design and real-world AI.

\- On Brighter with Herbert, host Herbert and Futurazza's Brian White discussed the milestone that a production Cybercab with no steering wheel and no pedals is driving itself on Austin public roads as an engineering test, albeit involving a person aboard the two-seater but not touching controls, with Musk confirming it is driving itself. They covered the Texas DPS officially adding the Cybercab to its connected-AV first-responder interaction page (a requirement for Level 4 scale operations, giving Texas police, fire and EMS a standardized protocol) and, separately, Coral Gables, FL fire personnel completing specialized robotaxi safety training covering battery systems, emergency access and incident management despite no local service yet. On semiconductors, they detailed Terafab landing its first major hire in a 18-year Intel manufacturing veteran and former factory manager (Gary Jang) as director of the Austin fab project.

\- On his July 1 Giga Texas drone update, Joe Tegtmeyer reported Cybercabs seen for the first time racing around the site's outer oval and performing stop-and-go testing plus simulated passenger drop-offs and pickups near the west main entrance, distinguishing logo-ed Cybercab units (no wheel or pedals, fully autonomous, no supervisor) from engineering versions with a steering wheel and supervisor — including one instance of the two tested together — alongside Model Ys driving themselves out to the west outbound lot indicating production underway, Cybertruck production appearing to pick up again, Cybercab groupings staged on the outbound lot, and transport trucks lined up to move units offsite. On construction, he covered Optimus factory steel erection proceeding north and south with seven cranes, continued clearing at the east-side advanced-technology chip-fab site ahead of building construction expected later in summer running into 2027, water-retention pond liner work, conduit connecting the expanded switchyard to Megapacks for Cortex 2, horizontal drilling under the Colorado River to pull an HDPE pipe, and accumulation of older engineering-version robotaxis he speculated are staged for recycling.

\- On his channel, David Moss walked through newly posted Cybercab first-responder materials on tesla.com, including a \~30-page interaction plan, an Arizona one-pager, an emergency response guide and a rescue sheet, confirming TSLA classifies Cybercab, unsupervised FSD and Model Y robotaxi as SAE Level 4 while steer-by-wire engineering vehicles with a steering wheel are Level 2, and detailing a 400V battery on a 48V low-voltage architecture (contrary to speculation it might match Cybertruck's 800V), first-responder-adjustable geo-fencing, 10 airbags, three glass types (laminated front, tempered sides, plastic over the B-pillar cameras), powered seats, interior door latches, an active hood that spikes up before a detected collision, external microphones and speakers for two-way support communication, camera washers with pressurized air, an emergency charge-cable release, and orange coolant/battery lines. He noted it is TSLA's first FWD-only vehicle, that opening a door or unbuckling a seatbelt causes it to disengage and park, that it charges (battery) before accepting new bookings when low, flashes hazards rapidly on a fault, responds to hand signals (which he says he tested with police and flaggers on cross-country FSD drives), and will not take rides in extreme weather (rain, fog, snow).

\- On WSJ, a reporter rode through central London in a Wayve-equipped Ford Mustang Mach-E (safety driver aboard) and interviewed co-founder and CEO Alex Kendall. He described the 2017-founded, \~\$8.6 bn valued startup's embodied AI as an end-to-end system that learns from human behavior and requires no HD mapping and, in his framing, little compute or infrastructure. Kendall cast it as a deliberately contrarian bet against rigid rules-based stacks and the hybrid model used by Waymo, citing a McKinsey survey in which 78% of AV experts believed hybrid was the likeliest path, and stressed the tech is adaptable across cities, vehicles, sensors and deployable on any OEM. The segment noted Uber and Wayve are teaming to launch London public-road robotaxi trials once UK regulators approve, positioning London as a near-term three-provider battleground alongside Waymo and Baidu's Apollo Go, and cited partnerships with Stellantis (supervised hands-free driving, with Uber planning to add Stellantis-designed Wayve-equipped vehicles to its fleet) and Nissan (driver assistance for mass-produced vehicles). On an AI bubble, Wayve CEO highlighted the opportunity as under-hyped while questioning whether today's giants will be tomorrow's.

\- On Odd Lots, recorded live at Bloomberg Invest in Hong Kong, hosts Joe Weisenthal and Tracy Alloway interviewed Baidu CFO Henry He, who described the company as a full-stack AI player across chips, the Ernie model, cloud and applications. He picked cloud as the must-win layer, since it hosts Ernie plus other models and connects to Baidu's inference chips, and noted \~80% of incremental token demand is inference. On robotaxis, Mr. He emphasized outlined economics on a cost-per-mile basis, citing a US owning vs. renting tipping point of \~\$0.60-0.80/mile against current robotaxi costs of \~\$1-2.50/mile, and noted only two cities globally host 1,000+ robotaxis (San Francisco via Waymo, one Chinese city via Apollo Go). He said Apollo Go delivered \~350K trips last quarter across 27 cities, \~20-25% below Waymo's \~500K/wk, and also shipped cars into London as both players open that market, and noted that the company partners with Uber, Lyft and Grab.

\- On Bloomberg Television, Nissan president and CEO Ivan Espinosa, said the company intends to embed autonomous driving tech across as much as \~90% of its lineup as an AI-defined vehicle. He called the Wayve-developed system almost Level 4 ready but to be rolled out step by step for regulators and consumers, beginning in Japan with an end-to-end-capable car called El Grand by FY2027-end before a gradual global rollout. Espinosa said Nissan has cut development time \~40% over 18 months, taking a global car from concept to start of production in 30 months. On US manufacturing, he confirmed Nissan will keep building at Smyrna, TN and Canton, MS, with US-built mix up from \~45% last January to 60% by year-end, citing \~\$2,000-3,000 of added tariff cost per Mexico-built vehicle and a cost-reduction program to keep them competitive.

\- On The Driverless Digest, host Harry interviewed Rocsys CEO and co-founder Crijn Bouman, previously founder of the ABB-acquired fast-charger Epyon. Bouman shared that removing the driver breaks vehicles' interface to the built world, especially as charging, garages and car washes all assume a driver, and that charging is the highest-frequency depot task and the bottleneck for scaling driverless fleets. He estimated a 24/7 robotaxi covering \~200-300 miles cycles requiring three to four charging shifts daily, and that a city like Los Angeles might need \~10,000 vehicles, implying \~30,000 sessions and 60,000-80,000 plug/unplug events per day. He introduced the M1, billed as the world's first multi-bay hands-free charging solution, featuring an overhead rail with a robotic arm that moves between bays to plug in, works with any make and charger, and retrofits existing lots without extra space (up to 10 bays per rail). Bouman said computer vision proved more capable than feared, handling snow, rain, hail, sand and even spider webs, with remote operators for edge cases, and framed London as the European battleground under the UK's AV framework effective January.

## TSLA specific newsflow:

\- Robotaxi launches in Miami. TSLA launched its robotaxi service in a section of West Miami on July 3, with initial availability limited to areas outside downtown as with the Dallas and Houston rollouts and riders already using unsupervised vehicles without an in-car safety monitor. Scope is expected to widen over time, as it did to the full Austin metro last month. Miami is the first of TSLA's five stated target cities to come online — Phoenix, Las Vegas, Orlando and Tampa remain on the near-term roadmap — and enters a market where Waymo has operated since January and Zoox is testing ahead of its own launch.

\- FSD v14 Lite launched; distills the HW4 stack; adds parking and speed profiles;

FSD v14 feedback remains encouraging. TSLA began rolling out FSD v14 Lite (firmware 2026.20.5.1) to a first wave of Hardware 3 (AI3) owners on 6/29, with Mr. Elluswamy, TSLA's VP of AI Software, noting the release is limited initially to Early Access Group members — vetted influencers and high-safety-score owners — before widening to more of the \~4 mn affected cars over coming weeks pending feedback. The build distills the HW4 v14 driving behavior into HW3's cameras and compute, passing through HW4 gains including reinforcement learning and offline models, sharpening proactive and reactive handling across navigation, merges/forks, pedestrian interactions, traffic lights and vehicle cut-ins, and adding comfort gains (fewer false slowdowns, smoother steering, more consistent lane centering) plus new parking, unparking and reverse functions, always-on Speed Profiles, and Arrival Options (lot, street, driveway, curbside); Mr. Elluswamy framed the headline change as significantly improved safety and characterized it as a compressed neural network rather than a feature-reduced one, though v14 Lite stays supervised and hands-on. It marks the first major step for a legacy fleet that had stalled at v13.2.9 — with many cars still running on v12.6.4 — and early impressions from owners running both previous stacks have been positive, with the step-up from v12.6.4 described as night-and-day alongside reports of multi-hour, zero-intervention drives through rush-hour traffic and tight canyon roads that testers characterized as feeling close to their AI4 cars. Separately, community trackers and social-media commentary reported FSD 14.3.4 running minimal disengagements across NYC, including an unsupervised New Haven-to-NYC trip and a widely circulated double-yellow sideswipe-avoidance maneuver cited as reactive capability beyond coded responses.

\- FSD regulatory expansion: Finland fast-tracked; EU vote slips to October with Sweden pushing a no. The national-recognition fast path in EU continues to compress approval from years to weeks, with the original Dutch RDW provisional approval dated April 10 after 18 months of testing, since followed by Lithuania, Estonia, Denmark, Belgium, and Finland's Traficom now signaling it may move ahead of the EU-wide decision on a faster schedule after summer once it resolves questions on driver-handover timing, low-visibility overtaking and the speed-offset feature. The EU-wide approval route requires a qualified majority of 15 of 27 states representing \~65% of the population via the TCMV, whose June 30 committee meeting was held but a vote is not expected before October 2026, and the more material opposition signal is that Sweden's transport authority is actively calling for a vote against the rollout unless TSLA removes the ability to exceed posted speed limits, with Norway and Finland flagging curve and roundabout handling.

\- Production-ready Cybercab driving around Austin. A video shared by Mr. Musk shows a production-ready Cybercab, featuring no steering wheel or pedals driving around in Austin with a safety monitor seated in the vehicles.

\- Cybercab First Responder guide surfaces technical details. TSLA's newly relea

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 06 Jul 2026 03:17 AM EDT

Disseminated 06 Jul 2026 03:17 AM EDT
"""
