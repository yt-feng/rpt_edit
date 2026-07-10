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
# Artificial Intelligence

## Bottlenecks Remain for Scaling Physical AI, But Commercialization Progressing

## CITI'S TAKE

Citi's $4^{\text{th}}$ annual Robotics and Physical AI Leadership Conference brought together leading founders, investors, and operators at the frontier of physical AI to assess where the market stands and the road ahead. The dominant theme was that commercialization has arrived, but scaling remains hard. Participants distinguished between the promise of physical AI models and the operational reality of deploying them in unstructured, safety-critical environments. Labor shortages, reshoring, and favorable regulatory tailwinds are accelerating enterprise demand, while data scarcity, talent constraints, battery limitations, and high deployment costs remain key friction points. Humanoids are generating significant investment enthusiasm, but near-term ROI is being driven by purpose-built AMRs and specialized systems from companies like Locus Robotics and Dexterity. The conference reinforced our view that physical AI is a decade-long buildout, with durable value accruing to companies that own the data flywheel, solve real deployment problems, and meet the highest safety standards.

Industrial Automation — Advances in physical AI are expanding addressable markets for automation solutions into new end markets and use cases. We see a durable long-term growth tailwind for automation-exposed industrial companies such as Buy-rated ROK, EMR, HON, SYM, RAL, and BDC as a constrained labor market and accelerating domestic manufacturing activity accelerates demand for physical AI solutions.

Commercialization — Real deployments are generating measurable ROI, with humanoid robots pricing at a discount to human labor and delivering payback periods of approximately one year, Dexterity approaching \$300 million in ARR after tripling revenue for three consecutive years, and Gatik holding \$600 million in contracted autonomous trucking revenue. Data flywheel advantages and RaaS business models are emerging as the key commercial moats separating leaders from the field.

Bottlenecks — Commercial deployments are scaling across logistics, warehousing, automotive, and defense, with Locus Robotics processing 200 units per second across 600 sites and Reliable Robotics holding a \$1 billion aviation automation backlog, though data scarcity, power constraints, and high system integration costs remain the key gating factors, creating durable competitive advantages for companies that have solved these bottlenecks at scale.

Heath Terry $^{AC}$ +1-212-723-4624
heath.terry@citi.com

Andrew Kaplowitz $^{AC}$ +1-212-816-0642
andrew.kaplowitz@citi.com

Vladimir Bystricky
+1-212-816-6595
vladimir.bystricky@citi.com

Shelby Spencer
+1-212-816-0416
shelby.spencer@citi.com

Ashley Kim
+1-212-816-6689
ashley.kim@citi.com

Janna Withrow
+1-212-723-0439
janna.withrow@citi.com

Piyush Avasthy
+1-212-816-9159
piyush.avasthy@citi.com

Jose Sulca Flores
+1-212-816-1717
jose.alonso.sulcaflores@citi.com

## Key AI Takeaways

Physical AI is transitioning from proof-of-concept to commercial deployment, but the path to scale is more operationally intensive than the digital AI analogy suggests. Unlike large language models, where a base model carries a lot of the value, physical AI places the premium on proprietary, task-specific data collected in real-world environments, purpose-built hardware, and safety certification.

Across sessions, participants consistently identified data scarcity as the binding constraint, with Instawork noting that even tens of millions of hours of data being collected in 2026 likely represents only basis points, not percentage points, of what is ultimately needed to achieve high-level robotic performance. Power, battery longevity, and chip architecture are also emerging as critical bottlenecks, with panelists noting that existing semiconductor platforms were designed for datacenter workloads, not real-time edge inference on mobile platforms.

The most commercially advanced companies, whether in humanoids, warehouse AMRs, autonomous trucking, or construction, shared a common profile: they started with a specific, high-pain labor problem, adopted a Robotics-as-a-Service model to lower customer adoption barriers, and prioritized safety and reliability above model sophistication.

## Key Industrials Takeaways

After attending Citi's Robotics & Physical AI Leadership Conference, we came away convinced that automation, robotics, and physical AI continue to make gradual progress toward broader commercialization, creating what we view as a durable long-term growth tailwind for our automation-exposed industrial companies. Our preferred ways to gain exposure to industrial automation are through Buy-rated ROK, EMR, and HON (pure-play automation providers), SYM (warehouse automation), RAL (sensors and T&M), and BDC (industrial networking), as we view these companies as well positioned to benefit from increasing investments in automation (including equipment, software, and AI). Key drivers of automation adoption remain a constrained labor market as well as accelerating domestic manufacturing activity and capacity expansions, with automation supportive of higher throughput, increased uptime, and improved operational efficiency/accuracy that appears supportive of healthy ROIs.

While logistics, warehousing, and autos appear to be important end markets driving automation adoption (higher volume, repetitive tasks), several panelists highlighted AI's potential to unlock new skills/capabilities for robotics and automation, which could, over time, expand addressable markets for automation solutions (new end markets and new use cases), which we view as a broad positive. Advances in AI/LLMs along with growing availability of data (real-world as well as simulated) are leading to more refined technology through, for instance more integrated hardware and software and more active usage driving increasingly capable deployments (as AI-enabled systems grow “smarter”), which we think could further support accelerating automation adoption over time. In some instances, access to high-quality data remains a bottleneck (where companies are combining simulations with limited real-world data), but we also view this as an opportunity and competitive moat for our companies, given their large installed base and ability to leverage/mine data to further drive autonomy and operational efficiency.

Select companies also highlighted robotics-as-a-service (RaaS) business models that potentially lower the barriers to adoption for small and medium sized

enterprises given lower or minimal upfront capital costs, which we view as supportive of our constructive view on SYM's warehouse-as-a-service offering (GreenBox/Exol), which we think could help drive increasing adoption of SYM's warehouse automation solutions amongst a broader range of customers.

## Session Summaries

## Investor Panel: Robotics and Physical AI as the Next AI Frontier for Investors

Speakers: Aaron Goldman, Managing Director, General Atlantic; Bill Boyd, Chief Strategy Officer of Symbiotic; Isaac Schecter, Head of Private Capital Markets, Americas at Millennium Management

Approximately \$20 billion has been deployed into physical AI over the past 24 months, though panelists were candid that valuations appear stretched relative to near-term fundamentals. Commercialization was identified as the true pivot point, with Symbiotic advising companies to wait for genuine proof points before raising, keep KPIs simple, and recognize that physical AI requires significantly more operational handholding than software-first businesses.

On foundation models and commoditization, panelists noted that the transformer architecture and pre-training and post-training consensus that exists for large language models has not yet emerged for the models that control robots, where Vision-Language-Action (VLA) models, world models, and various combinations remain in active debate. Data remains in short supply precisely because the industry has not yet converged on what kind of data it needs, and the hardware-software coupling in physical AI is far tighter than in the digital AI stack. Symbiotic's focus centers on filling portfolio gaps, extending battery longevity, and identifying what is genuinely solving a revenue-generating problem at scale.

Pre-IPO appetite for physical AI is expanding, with public markets prioritizing companies that can demonstrate scale, long-term contracts with major retail or logistics customers, and differentiated technology roadmaps with anchor customers 6 to 12 months out. The US and China are identified as the dominant innovation centers, with China holding a meaningful advantage in hardware manufacturing, and price points on humanoid robots approaching \$20,000.

## How Robotics Companies Evolve in the Era of Physical AI

Speakers: John Ha, CEO of Bear Robotics; Sean Hsu, CEO of Botrista; and Rick Faulk, CEO of Locus Robotics

Each panelist described a scaled commercial deployment achieved through a differentiated go-to-market approach. Locus Robotics, which has built the largest RaaS business in the US with around 600 sites globally, and 200 units processed per second across its network, succeeded by targeting brownfield warehouse buildings with a demonstrable ROI story rooted in the logistics and 3PL DNA of its founding team.

Bear Robotics has deployed 16,000 robots across 5,000 active sites in hospitality, hotels, casinos, factories, and warehouses, achieving scale by defining its core market across three geographies simultaneously and leveraging strategic investors to accelerate international sales, dramatically reducing total cost of ownership by solving more than 90 percent of issues remotely without deploying field engineers.

Botrista's approach centered on a six-week payback period for customers and near-zero enterprise churn, achieved by bundling consumables with its RaaS beverage solution into a single sticky package for more than 6,000 locations across F&B, hospitality, schools and office spaces.

Panelists identified the next wave of progress as agentic coordination at scale. Bear Robotics has built an agentic fleet management system from day one, allowing robots to communicate peer-to-peer and build consensus to maintain resilience against network failures, a critical design choice given that networking failures are the number one cause of field failures in dense deployments.

Locus's newest product, Array, uses a visual AI stack that learns with every pick to maximize efficiency and accuracy across an installed base approaching eight billion picks, building a data network effect across different robot form factors. On the five-year outlook, Bear Robotics expects physical AI to enable robots to understand human environments through gesture and voice commands at a higher level and Locus envisions fully lights-out dark warehouses operating 24 hours a day. Panelists agreed that the challenge today is no longer whether robots work but change management on the human side.

## Fireside Chat: Velaura AI

## Speaker: Rajiv Khemani, CEO of Velaura AI

Khemani argued that the physical AI world requires a complete semiconductor redesign from the ground up. The technology stack for robotics has evolved across three eras: pure CPU-based software algorithms for fixed-function tasks, CNN-based visual perception models, and the current transformer-based generation, but none of these architectures were purpose-built for the unique requirements of robotics at the edge.

Purpose-built chips for physical AI must prioritize ultra-low power (to obtain maximum performance from humanoid robots while avoiding overheating), real-time inference without server roundtrips, and integrated safety modules capable of making decisions locally with minimal false positives. Velaura's technology is already deployed across more than 30 million chips in the field through its work with hyperscalers, providing a proven foundation for its physical AI ambitions.

Khemani identified the key bottleneck areas for scaling physical AI beyond compute: sensor innovation (partnering with RealSense in this area); memory; and battery technologies. The competitive dynamic mirrors the broader AI chip market, where incumbent players designed for very large, homogeneous markets struggle to serve the segmented, specialized requirements of physical AI applications, creating a structural opening for purpose-built entrants.

On defense, Khemani noted that throwaway drones currently achieve accuracy rates of 50 to 55 percent and improving that to 80 to 90 percent constitutes a national security-grade advantage, making defense one of the highest-value near-term applications for purpose-built physical Al silicon.

# Physical AI Building the Physical World: Robotics in Construction and Manufacturing

Speakers: Rodion Shishkov, CEO of All3; Noah Ready-Campbell, CEO of Built Robotics; and Edward Mehr, CEO of Machina Labs

Panelists described three distinct applications of physical AI in the built environment. Built Robotics retrofits existing heavy construction equipment from manufacturers such as Caterpillar with custom software and models, enabling autonomous operation primarily in energy and solar construction, which accounts for approximately 80 percent of new power generation projects today.

Machina Labs operates general-purpose robotic platforms called RoboCraftsman for metal structure fabrication across aerospace, defense, and automotive sectors, completing different parts in a single day across a distributed factory model. All3 is applying robotics to multi-story residential construction, a domain characterized by almost entirely unstructured environments.

All three companies identified data generation as a primary challenge and strategic asset. Machina Labs noted that its high-rate data collection now enables customers to perform quality control in entirely new ways and generates high-bandwidth physical data streams capable of producing new scientific discoveries. All3 sees its data layer as a platform for third-party developers to build on, while Built Robotics views operational data from autonomous solar construction as an additional value proposition to accelerate customer adoption. On the question of robotics market hype, Noah Ready-Campbell expressed the view that humanoids are likely overhyped in construction specifically, where specialized equipment that becomes progressively smarter over time is more practical. Edward Mehr argued that the manufacturing conversation needs to be more strategic, with flexibility and distributed manufacturing as the critical advantages rather than replication of existing China-style mass production.

The three biggest scaling challenges identified across panelists were qualification burdens in manufacturing, particularly for safety-critical components in aerospace and automotive; manufacturing execution precision, where small errors in hardware fabrication become deployment blockers; and talent scarcity, with AII3 employing approximately 50 roboticists speaking 10 to 15 languages to address the global nature of the problem. Regulatory standards development was also flagged as a significant gap.

## General-Purpose Physical AI Models and Robotics Shaping the Physical World

## Speakers: Samir Menon, CEO of Dexterity and Lindon Gao, CEO of Dyna Robotics

Dexterity has built general-purpose AI models enabling hardware-agnostic robots to perform human-level skills at customers including FedEx across e-commerce, parcel, and airport applications, and is approaching \$300 million in ARR after tripling revenue year over year for three consecutive years. Dyna Robotics, backed by \$150 million from Nvidia and other corporat

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
