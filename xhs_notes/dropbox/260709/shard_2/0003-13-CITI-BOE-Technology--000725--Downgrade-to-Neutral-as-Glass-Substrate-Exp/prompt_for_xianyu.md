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
# BOE Technology (000725.SZ)

Downgrade to Neutral as Glass Substrate Expectations Likely Priced In

## CITI'S TAKE

We attended BOE's investor day. BOE reiterated its position as the global leader in displays while emphasizing that its next phase of growth will be driven by the extension of its core capabilities into glass-based advanced packaging, optical interconnect, perovskite photovoltaics, foldable glass, etc. BOE anticipates reaching a definitive mass-production investment decision by mid-2027. Its optical interconnect devices remain at a validation stage and have not yet entered mass production, but BOE targets to launch mature multi-channel product demos aligned with 1.6T, 3.2T and 6.4T industry requirements in 2028. We downgrade BOE from Buy to Neutral with a new TP of Rmb8.7 (prev: Rmb5.0), as we believe current valuation has factored in an improving LCD biz and potential glass substrate contribution.

BOE's second and third growth curves are increasingly material — Since launching its IoT transformation in 2021, BOE has achieved global No.1 shipment positions in more than 20 sub-segments, including automotive display, commercial display and public healthcare. Innovation business revenue is expected to reach Rmb60bn in 2026, representing around $30\%$ of total revenue and becoming a major growth pillar, according to mgmt. The third-curve incubation portfolio includes perovskite photovoltaics, glass-based packaging substrates, optical communication / interconnect, automotive dimming glass, regenerative medicine, robotics, VR/AR and 3D light-field display.

Cooperation with Corning — BOE and Corning have forged a strategic partnership to unlock global market opportunities across four key technological frontiers. In glass-based packaging substrates, BOE is combining Corning's TGV formulations with its experience in large-scale manufacturing to execute process qualification, technology transfer, and domestic market expansion. In optical interconnect, BOE will combine its micro-LED technology with Corning's optical systems to achieve mass-production readiness for next-generation AI data transmission. They are also validating foldable and bendable glass to expand beyond smartphones into broader automotive & IT applications. In perovskite photovoltaics, BOE is testing Corning's specialized UV-converting glass to enhance module efficiency & lifespan. Propelled by these joint validations, BOE targets a definitive mass-production investment decision for the perovskite business by late 2026 or early 2027, anticipating it will scale into a major business pillar by 2028–29. (continued inside/below...)

## Earnings Summary

<table><tr><td>Year to 31 Dec</td><td>Net Profit (RmbM)</td><td>Diluted EPS (Rmb)</td><td>EPS growth (%)</td><td>P/E (x)</td><td>P/B (x)</td><td>ROE (%)</td><td>Yield (%)</td></tr><tr><td>2024A</td><td>5,323</td><td>0.141</td><td>110.5</td><td>54.9</td><td>2.2</td><td>4.1</td><td>0.6</td></tr><tr><td>2025A</td><td>5,857</td><td>0.156</td><td>10.4</td><td>49.7</td><td>2.2</td><td>4.4</td><td>0.7</td></tr><tr><td>2026E</td><td>7,560</td><td>0.203</td><td>30.1</td><td>38.2</td><td>2.0</td><td>5.5</td><td>0.9</td></tr><tr><td>2027E</td><td>9,469</td><td>0.256</td><td>25.9</td><td>30.4</td><td>1.9</td><td>6.5</td><td>1.2</td></tr><tr><td>2028E</td><td>12,037</td><td>0.325</td><td>27.1</td><td>23.9</td><td>1.8</td><td>7.6</td><td>1.5</td></tr></table>

Source: Powered by dataCentral

Neutral ↓ from Buy

Price (06 Jul 26 15:00) Rmb7.760

Target price Rmb8.700↑

Expected share price return 12.1%

Expected dividend yield 0.9%

Expected total return 13.0%

Market Cap Rmb285,023M

## Price Performance

![](images/ad5cc69e3bdca15cf41904a9e2afd3b7159f7175f222b722e733207f38ff3b83.jpg)

Karen Huang $^{AC}$ +852-2501-2755
karen.xw.huang@citi.com

Kyna Wong
+852-2868-7820
kyna.wong@citi.com

Kevin Chen
+852-2501-2125
kevin.y.chen@citi.com

Glass-based packaging substrates. While glass substrates are emerging as superior alternatives to traditional PCBs for high-end AI and HPC applications, BOE is rapidly advancing its industrialization. Leveraging over six years of experience, BOE established mainland China's first glass substrate pilot line in 2024 and successfully delivered second-generation samples in 2025. The company has overcome major technical bottlenecks, achieving significant breakthroughs in TGV drilling (reaching a 20:1 aspect ratio), void-free metal filling, high-density routing (supporting over 20 build-up layers with sub-2μm line widths), and chip-free cutting. Crucially, BOE's substrates have passed rigorous industry reliability tests, demonstrating very low warpage even during high-temperature reflow soldering. Over the next two years, BOE aims to prioritize yield optimization, stable mass-production capabilities, and innovative layer-reduction designs alongside ecosystem partners. BOE anticipates reaching a definitive mass-production investment decision by mid-2027.

Optical interconnect and micro-LED light source. BOE is advancing its optical interconnect technologies, highlighted by its development of a micro-LED light source featuring a 1.8GHz response speed and a 3Gbps transmission rate. BOE is also working with Corning and other partners on high-purity optical fiber, optical bridges, waveguides and related optical transmission technologies. To drive technology implementation, BOE has outlined a clear roadmap: it plans to launch a two-dimensional multi-channel demo by 2027, followed by mature product demos meeting 1.6T, 3.2T, and 6.4T industry requirements in 2028. Ultimately, BOE aims to transition these innovations into mass production, expanding their application to data centers and automotive interconnect scenarios.

## Cooperation with Corning

The disclosed core cooperation areas with Corning include glass-based advanced packaging substrates, optical interconnect, foldable or bendable glass, and perovskite glass materials. The parties aim to jointly develop global markets and potentially create one or multiple Rmb100bn-scale new business opportunities.

The first core cooperation area is glass-based packaging substrates. In the AI era, rising computing power is driving the need for larger IC sizes, higher packaging stack complexity and more stringent physical-layer requirements. Traditional PCB substrates increasingly face limitations in warpage, flatness and heat resistance. Corning will provide glass and process technologies specifically developed for through-glass via, or TGV, applications. BOE will contribute its strengths in glass-based processing and large-scale manufacturing. The cooperation will proceed in three steps: (1) Complete systematic qualification of the new glass formulation and related processes. (2) Technology transfer. (3) Joint development of the domestic strategic market for glass-based advanced packaging. For BOE, the cooperation priorities include introduction experiments for high-performance glass substrates, optimization of key processes such as total thickness variation, or TTV, and improvement of substrate reliability.

The second core cooperation area is optical interconnect. With AI driving significant data transmission demand, traditional copper interconnects face bandwidth, power consumption and heat dissipation bottlenecks. BOE and Corning believe the industry is moving from copper to optical transmission. Corning can provide optical fiber, connectors and optical system technologies, reflecting its full-stack capability in optical transmission. BOE will contribute its micro-LED light-source technology. BOE noted that related optical interconnect technologies are also a core enabler for future Glass Bridge technology. The companies aim to jointly advance technology implementation and mass-production readiness.

The third core cooperation area is foldable or bendable glass. The initial focus is material validation and system integration. Future market expansion will not be limited to smartphones. BOE and Corning will focus on broader applications in automotive and IT, where foldable and bendable glass could unlock a larger addressable market.

The fourth core cooperation area is perovskite photovoltaics. Corning will provide specialty glass materials that can convert ultraviolet light into visible light. By leveraging the inherent properties of the glass itself, the material can improve perovskite conversion efficiency without a coating layer. Because there is no coating layer, the efficiency enhancement will not degrade over time, allowing the glass to meet the 15-20 year lifetime requirement of perovskite modules. For BOE, the collaboration with Corning will focus on ultraviolet performance optimization, power degradation improvement and photovoltaic module compatibility testing. BOE expects the perovskite business to meet the conditions for a mass-production investment decision by end-2026 or early 2027, subject to requirements on power-generation efficiency, stability and product lifetime. Management expects perovskite to gradually become an important business in 2028-29.

## Glass-based packaging substrates

High-end packaging substrates need to support large area with low warpage, high-density routing and low dielectric loss. Traditional PCB materials face growing limitations in AI and HPC applications. Glass substrates have three key advantages versus traditional materials: (1) Coefficient of thermal expansion, or CTE, close to silicon, resulting in low warpage. (2) Ability to achieve very small via diameters, supporting high-density packaging for AI chips. (3) Strong thermal performance, supporting heat dissipation in high-computing-power scenarios.

Packaging-related glass technologies can be divided into three categories (1) Panel-level packaging, or PLP. Square glass is used as a carrier and then peeled off in wafer-level packaging. (2) Glass interposer. Used for high-end, high-density direct die-to-die connection. (3) Glass substrate. Serves as the connection layer between the die and the PCB. Among these, glass substrate is currently the direction with the fastest industrialization progress.

The major technical bottlenecks include: (1) TGV drilling. The process must solve 20:1 aspect-ratio hole drilling, simultaneous processing of dense/sparse and large/small holes, roundness qualification, no open circuits and no hidden cracks. (2) Metal filling. Electroplating uniformity must be ensured. Surface copper and via copper thickness need to be consistent. Filling must be void-free, while stress between metal and glass must be managed. (3) Build-up and cutting. Multi-layer build-up can create stress accumulation and line breaks. Cutting brittle glass after build-up requires chip-free cutting technology. Automated inspection solutions must also be developed for transparent glass.

BOE has accumulated more than six years of TGV packaging process experience. In 2020, the company began work on single-process and material validation. In 2022, BOE invested in a 510mm × 515mm large-panel-width pilot line. The line achieved full process connection six months after equipment move-in. BOE also

has an 8-inch experimental line platform for basic material and formulation validation. In 2024, BOE built mainland China's first innovative pilot line for glass-based substrates. The company has completed customer conceptual validation. In 2025, BOE delivered second-generation samples. The 510mm × 515mm line is a complete mass-production validation line with investment of several hundred million Rmb, including more than Rmb100mn in automation equipment. It can validate automated yield and board-level small-sample production, providing high accuracy for future mass-production evaluation.

BOE has achieved meaningful process progress: (1) TGV process. Aspect ratio can reach 20:1. Waist diameter is adjustable between 65μm and 100μm. Roundness exceeds 90%. There are no cracks at the corner or via wall. (2) Filling process. Electroplating uniformity is below 5%. Surface copper and via copper thickness consistency reaches 80%. There are no blocked holes or bubbles. (3) Routing process. Line width is below 2μm. Line spacing is above 2μm. Alignment accuracy is 1μm. Routing uniformity is below 5%, with no broken lines. BOE can achieve more than 20 build-up layers and vertical stacked vias, supporting high-density interconnect requirements. (4) Cutting process. Chip-free cutting can be achieved, with 90-degree cutting angles that are 100% vertical.

BOE's single-layer substrate has passed industry-standard reliability tests, including 1,000 temperature cycles, HAST, high/low-temperature storage, and high-temperature/high-humidity aging. A $75\mathrm{mm} \times 75\mathrm{mm}$ sample showed room-temperature warpage of only $40\mu \mathrm{m}$ . It maintained low warpage after being heated to $260^{\circ}\mathrm{C}$ for reflow soldering, supporting AI and HPC chip requirements.

Over the next two years, BOE's key priorities are yield improvement and stable, sustainable mass-production capability. The company will also strengthen cooperation with ecosystem partners to overcome remaining process challenges and further explore the core value of glass substrates in layer-reduction design and packaging architecture optimization. Management emphasized that beyond large-area advantages, glass-based packaging substrates also create value through layer-reduction design. By optimizing packaging architecture using rectangular routing paths, glass substrates could potentially deliver meaningful system-level value. BOE expects to reach the conditions for a mass-production investment decision for glass substrates by mid-2027.

## Optical interconnect and micro-LED light source

BOE has established joint project teams with upstream and downstream enterprises and universities. Current progress includes a micro-LED light source with 1.8GHz response speed and 3Gbps transmission rate. Compared with VCSEL and other light sources, micro-LED has lower power consumption and lower temperature sensitivity. It can operate stably above 100°C, improving data stability while reducing temperature-control and heat-dissipation energy consumption. The company is working on high-speed photodiodes, optical drivers, electrical drivers, electrical chips and transmission protocols, with a goal of building a mature full-chain solution. BOE is also working with Corning and other partners on high-purity optical fiber, optical bridges, waveguides and related optical transmission technologies. Optical interconnect devices are still at a validation stage and have not yet entered mass production. BOE aims to continue to work with domestic and overseas research institutions and industry partners to advance technology implementation. BOE's roadmap is as follows (1) In 2027, to launch a two-dimensional multi-channel micro-LED optical interconnect solution demo. (2)

In 2028, to launch mature multi-channel product demos aligned with 1.6T, 3.2T and 6.4T industry requirements. (3) To expand applications into data centers, automotive interconnect and other scenarios.

## Third-generation semiconductor and GaN

BOE Huacan has completed construction of a gallium nitride (GaN) pilot line and now has preliminary mass-production conditions. Its 650V high-voltage product has passed customer validation. The company expects to launch a 40V low-voltage product by end-2026. It plans to later expand into automotive-grade and AI-scenario applications. In GaN power electronics, BOE Huacan has delivered the second high-voltage GaN device product to customers through its Yiwu GaN pilot line. GaN products remain at an optimization stage. Related products are likely to launch in 2027, with future applications targeting AI, industrial and automotive-grade power chips.

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
