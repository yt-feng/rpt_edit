你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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

Dexterity has built general-purpose AI models enabling hardware-agnostic robots to perform human-level skills at customers including FedEx across e-commerce, parcel, and airport applications, and is approaching \$300 million in ARR after tripling revenue year over year for three consecutive years. Dyna Robotics, backed by \$150 million from Nvidia and other corporate venture investors, builds general-purpose robots for commercial deployment.

Both panelists described a three-layer model architecture for physical AI: an observation layer for understanding physical and semantic space, a reasoning layer, and an actioning layer that translates instructions into motor commands.

General-purpose physical AI is exciting precisely because scaling laws apply: as data produced through reinforcement learning accumulates, robots become dramatically better, crowdsourcing intelligence from hundreds of thousands of training interactions.

On data and commercialization, Dexterity identified expert tokens, defined as optimal responses to unpredicted, unforeseen real-world events in production, as the highest-quality data and the true source of model scale, and expects the industry to remain data-starved for the foreseeable future. Dyna Robotics cautions against smaller specialized models, having found they do not scale well, and instead emphasizes that a large generalized pre-trained model provides the physical grounding and language-to-action translation capability that enables post-trained consumer applications.

On monetization, Dexterity operates a subscription model that it views as more lucrative than token consumption, while Dyna Robotics expects the industry to converge on a token-to-output model over the long term. The panel agreed that physical AI models still need to reach the sophistication level where goals can be issued on the fly, as is already possible in digital AI, and that reasoning models requiring substantial production data to train will take approximately three years in deployment to develop meaningfully.

## IBM Presents: Turning Visual Inspection into Actionable Asset Intelligence

## Speaker: Ed Neubecker, Principal Automation Technical Specialist at IBM

IBM has brought computer vision into asset management with a platform that enables domain experts to build and own AI models for use at the edge. A 1 percent improvement in quality translates to millions to hundreds of millions of dollars of value for manufacturing operators, and IBM's platform is in active use at Ford for F150 truck inspection and at Sund and Baelt Bridge using Maximo to reduce maintenance risk.

The addressable asset maintenance opportunity spans bridges, generators, HVAC systems, utilities, and IT datacenter infrastructure. The platform supports 2D vision across thermal, x-ray, and standard imagery including drone video feeds, with 3D inspection in development. IBM's build-your-own model design ensures clients retain full data ownership, a key differentiator for enterprises where visual inspection processes represent proprietary operational IP.

## How AI Is Changing the Way We Deploy Automation in Factories and Warehouses

Speakers: Ross Diankov, CEO of Mujin; and Etienne Lacroix, CEO of Vention

Mujin was fo

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
