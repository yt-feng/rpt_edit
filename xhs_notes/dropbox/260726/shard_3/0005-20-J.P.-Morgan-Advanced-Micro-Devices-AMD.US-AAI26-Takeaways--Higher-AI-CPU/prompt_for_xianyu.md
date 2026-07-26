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
## Advanced Micro Devices

## AAI26 Takeaways: Higher AI/CPU TAM Forecasts and MI450/Helios Ramp Underscore a Broadening AI Opportunity; Closing the Gap with GPU Peers While Capitalizing on CPU Tailwinds

We attended AMD's flagship Advancing AI event (AAI26) in San Francisco yesterday and left feeling much more constructive on the company's end-to-end compute product portfolio (semis + systems + software), upcoming product roadmaps, and its strengthening AI ecosystem partnerships (with companies like Anthropic, OpenAI, Meta, and more). As usual, AMD also launched several new products at this year's event, with the most notable releases including its $6^{\text{th}}$ Gen EPYC CPUs ("Venice"), Instinct MI4XX series GPUs, and Helios AI rack-scale solutions (other launches included Ryzen AI Embedded X100s and Kria AI SOM, among others). However, in our view, the real key takeaways from this year's event were as follows: (1) Management raised its AI accelerator TAM forecast to \~\$1.4T by 2030, up from the >\$1T estimate it laid out at its Nov-25 Analyst Day and the >\$500B by 2028 outlook from last year's event (AAI25). The expansion in TAM primarily stems from the proliferation of agentic AI applications, which are driving higher aggregate demand across GPU and CPU markets (see Figure 1). (2) Management also raised its data center CPU TAM forecast to \~\$220B by 2030 (>50% server CPU CAGR through 2030), reflecting a \$100B increase from the \$120B outlined on the company's 1Q26 earnings call and a nearly 4x increase from the \$60B indicated at its Nov-25 Analyst Day (see Figure 2). (3) AMD confirmed that its MI450 series GPUs and Helios rack-scale systems would begin shipping at the end of this quarter, with a more aggressive ramp into 4Q26 and 1H27. We think first shipments at the end of September were a touch later than market expectations, but believe this is relatively inconsequential as multiple GWs of MI450 are scheduled for deployment through CY27/CY28 (across Anthropic, OpenAI, and Meta). Management also further clarified that it intentionally built the ramp this way as it would allow ODMs to fine-tune manufacturing (if needed) while also aligning the ramp with customer data center builds. (4) AMD believes this is the strongest and broadest product portfolio it has ever had, and at a high level, we think AMD's expansive silicon portfolio — which spans data center EPYC CPUs, Instinct GPUs, and Helios rack-scale systems, as well as Ryzen AI and edge/embedded processors — positions the company to capture AI opportunities across virtually every vertical, from frontier model training in the data center to agentic workloads, edge computing, and client/physical AI. All told, we believe this year's event uniquely highlighted how AMD is continuing to close the gap with larger GPU peers, while at the same time benefiting from accelerating trends in CPU and ancillary markets.

## Neutral

AMD, AMD US  
Price (22 Jul 26):\$552.33  
Price Target (Dec-26):\$385.00

Semiconductors & Semiconductor Capital Equipment / IT Hardware

Harlan Sur AC (1-415) 315-6700 harlan.sur@JPM.com

Mayur Ramdhani (1-212) 622-1664 mayur.ramdhani@JPM.com

Apoorva Kumar (1-212) 270-0668 apoorva.kumar@JPM.com JPM Securities LLC

See page 6 for analyst certification and important disclosures.

\- AI Accelerator TAM raised to \~\$1.4T by 2030 (up from >\$1T prior), driven by AI-related compute demand broadening into agentic AI workloads... AMD raised its AI accelerator TAM forecast to \~\$1.4T by 2030, which implies a >45% CAGR over the next 5 years (from \~\$200B in 2025). This marks a meaningful step-up from the >\$1T estimate laid out at the company's Nov-25 Analyst Day and the >\$500B outlook provided at last year's AAI event. The upward revision primarily reflects AMD's belief that AI-related compute demand is expanding beyond model training into inference and, increasingly, agentic AI workloads. The argument here is that as agentic applications proliferate across enterprise and consumer use cases, they will drive higher aggregate demand not just for GPUs but across the compute stack, including CPUs — and AMD's Instinct GPU and EPYC CPU franchises give the company multiple avenues to benefit from this same secular tailwind. All told, we think the higher AI TAM forecast reflects management's rising confidence in the breadth and durability of the AI buildout through the end of the decade — a net positive for our entire sector. We remain of the view though that AI ASIC/XPU growth will continue to outpace DC GPU growth through 2030, which should trim GPU TAM share from \~85% in CY25 to \~60-70% by 2030. This would imply that the GPU TAM CAGR is slightly lower than the overall AI accelerator TAM CAGR, likely closer to the \~40% range, with AMD likely gaining share (from a <5% level in CY25). If we were to conservatively assume that GPU share of the overall AI accelerator TAM sits at \~60% in 2030 and that AMD captures 15% of that GPU share, it would imply DC GPU revenues potentially being in the \$125B range, which is considerably above current Street consensus estimates of \~\$94B...

Figure 1: AI Accelerator TAM Forecast (\$B)  
![](images/04c398fb57ee2486492ae84bb2cb398beaf31ea542496fdb3f62d59d09bfc17a.jpg)  
Source: AMD Advancing AI 2026, JPM Estimates

\- Data center CPU TAM raised to \~\$220B by 2030, up from \$120B outlined on the 1Q26 earnings call and slightly higher than buyside estimates (\~\$200B)... AMD also raised its data center CPU TAM forecast to \~\$220B by 2030, which implies a >50% CAGR over the next 5 years (from \~\$26B in 2025). The new TAM figure came in a touch higher than some of the buyside bogeys we heard heading into the event (\~\$200B) and marks a \$100B increase from the \~\$120B figure outlined on the company's 1Q26 earnings call just a few months ago. It also reflects a nearly 4x increase from the \$60B indicated at its Nov-25 Analyst Day last year. We think the magnitude and pace of these successive raises are notable in their own right, but unsurprising when considering how inference and agentic workloads will naturally require substantial amounts of general-purpose compute alongside GPUs to handle orchestration and data processing tasks. While the implied TAM CAGR now sits at >50%, we think additional share capture could fuel an even higher growth rate for AMD's server CPU business. If we were to conservatively assume in-line growth, AMD's server CPU revenues could potentially reach \$85B+ in 2030, which, in combination with DC GPU revenues in the \~\$125B range (see prior bullet), could yield total data center segment revenues in the \$200B+ range for CY30 (considerably higher than current Street forecasts of \~\$122B).

Figure 2: Data Center CPU TAM (\$B)  
![](images/daca6032927af28bc26d8803a784f7ea7532778b118d83a509e849829dc31063.jpg)  
Source: AMD Advancing AI 2026, JPM Estimates

\- MI450 GPUs / Helios rack-scale system start shipping in Sep-26, with an aggressive ramp into 4Q26 and 1H27... AMD confirmed that its MI450 series GPUs and Helios rack-scale systems would begin shipping at the end of 3Q26 — in September, specifically — with a more aggressive ramp into 4Q26 and 1H27. While first shipments in September may have been slightly later than what was broadly expected heading into the event, we view it as relatively inconsequential as multiple GWs of MI450 capacity are already scheduled for deployment through CY27. In other words, the demand pipeline remains robust, and that is ultimately what matters most for the trajectory of the ramp, and thus AMD fundamentals — not the precise start date. For what it is worth, management also clarified that the timing was a deliberate design choice rather than a sign of execution slippage. Staging the ramp this way gives ODM partners room to fine-tune manufacturing if needed, while also aligning shipments with customers' own data center build-out schedules.

\- AMD believes this is the strongest and broadest product portfolio it has ever had, and we are inclined to agree... AMD's expansive silicon portfolio, which spans data center EPYC CPUs, Instinct GPUs, and Helios rack-scale systems, as well as Ryzen AI and edge/embedded processors, positions the company to capture AI opportunities across virtually every vertical, from frontier model training to agentic workloads, edge computing, and physical AI. What particularly stood out to us at this year's event was that AMD is increasingly able to offer customers a full-stack solution — silicon, rack-scale integration, and open software (ROCm) — which, in theory, expands the dollar content AMD can capture per deployment. This breadth also provides a natural hedge against the uneven pace of any one end market, allowing AMD to participate in AI buildout upside wherever demand materializes — whether that's hyperscale training clusters, enterprise inference, autonomous robotics, or on-device AI at the edge.

# Investment Thesis, Valuation and Risks

Advanced Micro Devices (Neutral; Price Target: \$385.00)

## Investment Thesis

Although AMD has improved its competitiveness across CPU and GPU products with Ryzen, EPYC, and Radeon platforms and is on track to improve its market share and drive meaningful revenue growth in the near term, we believe long-term share gains are less certain. In addition, AMD will have to invest heavily in operating expense (especially R&D) in order to keep pace with the market leaders. While we are encouraged by AMD's execution, we remain Neutral as shares appear to be nearly fully valued.

## Valuation

Our Dec-26 PT of \$385 assumes shares trade at a \~35x P/E multiple (in line with peer multiples) applied to \~\$11 of earnings power exiting CY26.

## Risks to Rating and Price Target

AMD typically derives $\sim 50\%$ of its revenue from the core PC end market, which is highly correlated with macroeconomic conditions. If the PC end market is weaker/stronger than expected, this could lead to a decrease/increase in microprocessor and GPU shipments, which could result in a downward/upward revision of our revenue and EPS estimates for AMD.

AMD competes with Intel and NVIDIA in the microprocessor and graphics markets, respectively. Therefore, any material share gains/losses could result in upside / downside to our revenue and EPS estimates, which could cause us to reassess our Neutral rating on AMD.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

• Market Maker: JPM Securities LLC makes a market in the securities of Advanced Micro Devices or related entities.

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Advanced Micro Devices or related entities.

\- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of Advanced Micro Devices or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Advanced Micro Devices or related entities.

\- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: Advanced Micro Devices or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Advanced Micro Devices or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Advanced Micro Devices or related entities.

\- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from Advanced Micro Devices or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Advanced Micro Devices or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Advanced Micro Devices or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Advanced Micro Devices or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Advanced Micro Devices (AMD, AMD US) Price Chart  
![](images/5ff1bbe61bc51623203e4bc0d599da8f4a9f421f44d7f2e91b17c2ea65bc4f41.jpg)  
Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Sep 12, 2002. All share prices are as of market close on the previous business day.

<table><tr><td>Date</td><td>Rating</td><td>Price ($)</td><td>Price Target ($)</td></tr><tr><td>02-Aug-23</td><td>N</td><td>117.60</td><td>130</td></tr><tr><td>01-Nov-23</td><td>N</td><td>98.50</td><td>115</td></tr><tr><td>31-Jan-24</td><td>N</td><td>172.06</td><td>180</td></tr><tr><td>05-Feb-25</td><td>N</td><td>119.50</td><td>130</td></tr><tr><td>07-May-25</td><td>N</td><td>98.62</td><td>120</td></tr><tr><td>06-Aug-25</td><td>N</td><td>174.31</td><td>180</td></tr><tr><td>05-Nov-25</td><td>N</td><td>250.05</td><td>270</td></tr><tr><td>06-May-26</td><td>N</td><td>355.26</td><td>385</td></tr></table>

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperfor

[中间内容因长度限制已省略]

or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Morgan any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 24 Jul 2026 12:07 AM EDT

Disseminated 24 Jul 2026 12:07 AM EDT
"""
