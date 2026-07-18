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
# Industry Humanoid Robot Pulse

Asia
Japan
North America

Industrials
Manufacturing

Date
16 July 2026

Industry Update

# US activities stepping up; China scaling fast; Supportive policies (2Q edition)

Amid the heavy newsflow around humanoid robots, we summarise the key themes and developments in the market globally in this quarterly series.

DB views: The humanoid robot market is accelerating globally. China is leading in production, with government officials estimating 100,000 units of humanoid robot production in 2026, significantly higher than our expectation of \~40,000 units. In the US, Agility Robotics utilises a 75% locally-sourced supply chain and aims to reduce the bill of materials (BOM) cost from US\$125k currently to US\$30k. AGIBOT and Figure AI have livestreamed their humanoid robots working in factories and warehouses, demonstrating commercial viability. This rapidly developing market indicates growing component demand, which bodes well for component manufacturers. Within our APAC Industrials coverage, we prefer Hengli (Buy, closing price RMB110.58), Shuanghuan (Buy, closing price RMB42.39), Harmonic Drive (Buy, closing price ¥7,430), and Yaskawa (Buy, closing price ¥5,490). We also highlight Tesla (Buy, closing price US\$394.46) and Mobileye (Buy, closing price US\$9.43) (through Mentee Robotics) as humanoid robotic OEMs in the US.

## We highlight the key themes and developments in 2Q26:

1. Activities in the US stepping up: Agility going public through SPAC by 4Q26; Meta acquiring an embodied AI model startup; OpenAI recruiting robotics engineers; and NVIDIA expanding its robotics team in China.

2. Continuing developments in China: AGIBOT accelerating production; updates from BYD and Li Auto on robotics; Alibaba unveiling robotic models; and Kepler undergoing acquisition.

3. Policy updates: China to produce 100,000 humanoids in 2026; Shanghai to deploy 100,000 humanoids by 2030; the US could restrict Chinese robotics; and Japan to deploy 10mn AI robots by 2040.

4. Use case: Livestreaming of humanoids working in factories and warehouses by AGIBOT and Figure.

5. Emotional companion: Bionic humanoids from UBTECH and DOBOT.

Iris Zheng, CFA
Research Analyst
+852-2203-5884

Edison Yu
Research Analyst
+1-212-250-7263

Laura Li
Research Associate
+1-212-250-2266

Winnie Dong
Research Analyst
+1-212-250-5121

## Companies featured

<table><tr><td colspan="2">Companies featured</td></tr><tr><td>Hengli Hydraulic(601100.SS),CNY110.58</td><td>Buy</td></tr><tr><td>Shuanghuan Driveline(002472.SZ),CNY42.39</td><td>Buy</td></tr><tr><td>Yaskawa Electric (6506.T),¥5,490</td><td>Buy</td></tr><tr><td>Harmonic Drive Systems (6324.T),¥7,430</td><td>Buy</td></tr><tr><td>Tesla Inc. (TSLA.OQ),USD394.46</td><td>Buy</td></tr><tr><td>Mobileye (MBLY.OQ),USD9.43</td><td>Buy</td></tr><tr><td>FANUC (6954.T),¥7,008</td><td>Hold</td></tr><tr><td colspan="2">Source: DB</td></tr></table>

## We also highlight reports from DB Research:

Comparing Unitree, UBTECH, DEEP, Dobot and Leju based on their prospectuses and public information, published on 15 June. Link to report.

■ Comprehensive update of the humanoid robot market and six visions for 2026, published on 6 March. Link to report.

## Activities in the US stepping up: Agility; Meta; OpenAI; NVIDIA

## Agility targets IPO through SPAC by 4Q26; 75% supply chain sourced within the US

On 24 June 2026, Agility Robotics announced its intention to go public through a business combination with Churchill Capital Corp XI (CCXI), a publicly traded Special Purpose Acquisition Company (SPAC). The transaction will make Agility the first US-listed pure humanoid robotics company. Upon completion, the combined entity will operate as Agility and trade under the ticker "AGLT." The deal values Agility at a pre-money valuation of US\$2.5bn, and is expected to raise more than US\$620mn, according to Agility.

Agility's humanoid robot Digit is commercially deployed with enterprises including Schaeffler, GXO, Toyota Motor Manufacturing Canada, and Mercado Libre, with more than 65,000 hours of operation accumulated. Agility runs a manufacturing facility with production capacity of up to 10,000 units of Digits annually. Agility sources \~75% of Digit parts within the US. Agility has recorded over US\$300mn orders for Digit v5 so far, with a pipeline multiple times that amount. Digit v4 has a carrying capacity of 35lbs (\~16kg) and a runtime of 4 hours. Agility plans to launch Digit v5 in 2026, which is designed to safely operate outside the work cell and alongside humans for commercial scale. Agility aims to reduce the bill of materials (BOM) cost from US\$125k currently to US\$30k when the production scales up to 10,000 units per year.

## Meta acquired embodied AI model startup Assured Robot Intelligence

On 1 May 2026, Meta Platforms announced its acquisition of Assured Robot Intelligence (ARI), a San Diego-based start-up specializing in AI models for robots, for an undisclosed amount. ARI's 20-member team, led by its co-founders Lerrel Pinto and Mr. Wang Xiaolong, will join Meta Superintelligence Labs (MSL) to build humanoid intelligence, as announced by Wang via his X account. Wang was a former NVIDIA researcher and currently holds an associate professorship at the University of California. Pinto previously co-founded Fauna Robotics in 2024, and the humanoid robot startup was officially acquired by Amazon in March 2026.

## OpenAI recruiting robotics engineers

On 31 May 2026, OpenAI's CEO Sam Altman publicly revealed that the company was seeking to hire “exceptional full-stack hardware, operations, systems, and machine learning engineers to help OpenAI program and manufacture robots that are useful for society”. It marked the relaunch of OpenAI’s internal robotics division, five years after disbanding its previous robotics research team in 2021 to pivot resources toward Large Language Models (LLMs).

## NVIDIA expanding robotics team in China

According to Nvidia's official account announcement on 30 June 2026, the company is recruiting for more than a dozen roles within its robotics team in China. These new opening roles, located in Shanghai, Beijing and Shenzhen include four key domains: embodied intelligence, simulation, implementation and solutions architecture.

## NVIDIA unveiled Reference Humanoid Robot on GTC Taipei 2026

At GTC Taipei on 1 June 2026, NVIDIA CEO Jenson Huang launched the NVIDIA Isaac GR00T reference humanoid robot, an open humanoid robot reference design built on NVIDIA Jetson Thor and NVIDIA's humanoid-focused AI models, namely NVIDIA Isaac GR00T, for academic research. The robot features 22 DoF on each dexterous hand supplied by Singapore-based Sharpa, and integrates H2 Plus humanoid robot from Unitree Robotics. According to Unitree's website, this Reference Humanoid Robot is expected to be available in late 2026. Furthermore, the NVIDIA Isaac GR00T developer platform will also support Unitree's G1 humanoid robot. However, Unitree has since been added to the Military Companies list by the U.S. Department of Defense, on 8 June 2026, which raises questions over this collaboration.

Following the GTC Taipei event, Jensen Huang visited South Korea and met with LG Group Chairman Koo Kwang-mo, to discuss their collaborations spanning robotics, AI data centers and mobility. As part of the strategic partnership, LG plans to leverage NVIDIA's Isaac GR00T open platform to develop its own humanoid and logistics robots.

## Continuing developments in China: AGIBOT; BYD; Li Auto; Alibaba; Kepler

## AGIBOT achieved 15,000 units cumulative embodied robot production

On 28 June 2026, AGIBOT announced the production of its 15,000th general-purpose embodied robot, Genie G2. This milestone follows a rapid increase in production, with AGIBOT's embodied robot cumulative production reaching 1,000 units in January 2025, 5,000 units by 8 December 2025, and 10,000 units by 28 March 2026. The accelerating pace in 1Q26 underscores AGIBOT's enhanced scaling capabilities.

## BYD provided updates on humanoid robot

In May 2026, BYD's Executive Vice President Ms. Li Ke shared the company's advancements in robotics business. Ms. Li stated that BYD's accumulated technology in intelligent driving, sensor fusion, motor control, and other fields can naturally be transferred to humanoid robots. As for manufacturing, she commented that BYD intends to establish an open platform to either self-develop humanoid robots or cooperate with external partners. However, BYD recently refuted several items of market news, including claims that "the humanoid robot project is named 'Yao Shun Yu'," "the 7th-generation prototype is being tested on-site at Shenzhen and Changsha factories," and "approximately 150 units of humanoid robots are on duty, with a target of 20,000 units for internal use within 2026."

## Li Auto announced its entry into humanoid robots

During Li Auto's 1Q26 earnings call on 28 May 2026, the Chairman and CEO Mr. Li Xiang outlined the strategic approach to develop both facets of embodied AI: autonomous driving, considered the "first half" of the technology, and general-purpose humanoid robots, representing the "second half." The company highlighted that the core technological stack—comprising self-developed chips, large language models, perception systems, control systems, and operating systems—essential for autonomous driving, also forms the fundamental base for general-purpose humanoid robots. This synergy allows technical capabilities validated in mass-produced vehicles to directly propel advancements in humanoid robots. Li Auto has already initiated the development of humanoid robot products. According to unconfirmed market news from early 2026, Li Auto's humanoid robot team, operating under the internal codename "Nexus," has been working on the project for nearly a year. The team has planned two distinct products: a two-wheeled humanoid robot and a bipedal humanoid robot. The two-wheeled product is ideally slated for release by mid-2026, primarily targeting factory manufacturing applications.

## Alibaba unveiled robotics foundation model Qwen-Robot

On 16 June 2026, Alibaba launched its Qwen-Robot series, a suite of embodied intelligent large models comprising three components:

Qwen-RobotManip: a Vision-Language-Action (VLA) model excels in object manipulation and interaction within physical environments. It empowers robots to perform intricate tasks such as grasping objects and opening / closing drawers. The model addresses the challenge of incompatible action representations across various robot platforms.

Qwen-RobotNav: a Vision-Language-Navigation (VLN) model engineered to tackle autonomous robot movement and navigation challenges. Equipped with a built-in environmental memory module, it enables robots to perform tasks such as indoor item retrieval and short-distance material transfer.

Qwen-RobotWorld: a world model simulates the underlying physical dynamics that facilitate both navigation and manipulation. This model allows personnel to generate extensive simulated training data, significantly reducing the costs associated with on-site calibration of physical robots.

## Kepler Robotics was acquired by Hangzhou Kelin

On 19 May 2026, Hangzhou Kelin Electric Co., Ltd. (688611.SH) announced its plan to acquire a $41.57\%$ stake in Kepler Robotics for no more than RMB300mn. Combined with the $9.43\%$ stake already secured, Hangzhou Kelin will hold $51\%$ of Kepler' equity. Kepler is valued at approximately RMB722mn in this acquisition. Hangzhou Kelin, specializing in intelligent monitoring and control technologies for the power IoT, developed six-axis force sensors for humanoid robots in early 2026. Notably, prior to this acquisition, Kepler's former CEO and co-founder, Mr. Hu Debo, had departed to establish his own venture. According to financial disclosures from Hangzhou Kelin, in 2025, Kepler reported revenue of RMB4.3mn and net loss of RMB67mn; in 1Q26, revenue stood at RMB2.6mn with a net loss of RMB17mn. Despite these figures, according to Kepler's CFO, the internal target for FY2026 is to achieve over RMB100mn in revenue. Currently, Kepler holds orders backlog exceeding RMB47mn across industrial and commercial sectors, all representing commercialized repurchase orders from existing clients.

## Policy updates: China; the US; Japan

China's humanoid robot production to exceed 100,000 units in 2026

On 7 July 2026, an official from the Ministry of Industry and Information Technology (MIIT) projected that China's annual humanoid robots production would surpass 100,000 units in 2026. Compared to our estimates of \~15k units in 2025, it represents a more than five-fold increase. The official also noted that more than 30% of China's large-scale industrial enterprises currently are utilising AI applications. MIIT is implementing specialised initiatives, such as "Model-Data Resonance" and "Humanoid Robots and Embodied Intelligence Real-Scenario Training", to identify high-value application scenarios.

## Shanghai to deploy 100,000 units of humanoids by 2030

On 18 May 2026, the Shanghai Municipal Government Information Office announced its "AI+" initiative during a press conference on the "15th Five-Year Plan." This strategic action aims to leverage artificial intelligence to drive a paradigm shift in industrial sectors. By the end of the "15th Five-Year Plan" period (2026-2030), Shanghai plans to integrate 100,000 units of humanoid robots into local factories and achieve an intelligent agent application popularisation rate exceeding $80\%$ among industrial enterprises above a designated size.

## Figure 1: Shanghai policies on robotics

<table><tr><td>Date</td><td>Policy</td></tr><tr><td colspan="2">Shanghai</td></tr><tr><td>May-26</td><td>Shanghai &quot;AI+&quot; initiative (上海&quot;人工智能+行动)&quot;15th Five Year Plan (2026-2030)&quot; goal: integrate 100,000 units of humanoid robots into local factories and achieve an intelligent agent application popularization rate exceeding 80% among industrial enterprises above a designated size.</td></tr><tr><td>Jan-26</td><td>&quot;Shanghai Action Plan for Supporting the Transformation and Upgrade of Advanced Manufacturing (2026-2028)&quot; (上海市支持先进制造业转型升级三年行动方案(2026-2028年))Encourage enterprises to invest in emerging fields such as low-altitude economy, commercial aerospace, embodied intelligence, bio-manufacturing, and intelligent terminals, accelerating the breakthrough of industrial large-scale development bottlenecks for innovative products such as eVTOL, commercial rockets, and humanoid robots.</td></tr><tr><td>Oct-25</td><td>Shanghai: &quot;Action Plan for High-Quality Development of the Smart Terminal Industry (2026-2027)&quot; (智能终端产业高质量发展行动方案(2026-2027年))Further supports the mass production of humanoid robots and the industrialization of core components such as edge-side chips and dexterous hands.</td></tr><tr><td>Aug-25</td><td>Shanghai: &quot;Embodied AI Industry Development Implementation Plan&quot; (上海市具身智能产业发展实施方案)2027 goal: Achieving 20+ core algorithm and other technology breakthroughs in embodied models and datasets; clustering 100 industry leading companies, launching 100 innovative application scenarios, and promoting 100 globally competitive products. Overall to grow the embodied AI industry&#x27;s core output beyond RMB50bn.</td></tr><tr><td>Dec-24</td><td>Shanghai: &quot;Implementation Plan for AI &#x27;Molding Shanghai&#x27;&quot; (关于人工智能“模塑申城”的实施方案)Organizing technological R&amp;D efforts to develop embodied AI algorithmic models, including end-to-end, multi-modal, and spatial intelligence. Focusing on open-source robot bodies and datasets, as well as open-source autonomous simulation platforms, to build an open-source technology found

[中间内容因长度限制已省略]

ted performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
