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
U.S. Multi Industry & Electrical Equipment 3M Co

Rating Underperform

Price Target

MMM

131.00 USD

![](images/e899785c1c3c01c756827e827d170a18a1034e106cf3e229c3104aec632e39cd.jpg)

![](images/857c58a3b9748f6167bab7144a7ce26bf531d3176a1a1176629647e6750819f1.jpg)

Varun Govindaraj
+1 917 344 8543
varun.govindaraj@bernsteinsg.com

![](images/3aa6e5bf8c1908940bc78bc9d36be1d7b7c5dd48b1386aee76d1a5f810e910b9.jpg)

Mark L. Moerdler, Ph.D.
+1 917 344 8506
mark.moerdler@bernsteinsg.com

![](images/5fe7c797da6a2567fda1b6f5cf76a77090a9ba74c5150324c8e2535c5614c237.jpg)

Firoz Valliji, CFA
+1 917 344 8316
firoz.valliji@bernsteinsg.com

Shelly Tang, CFA
+1 917 344 8342
shelly.tang@bernsteinsg.com

# 3M: Is the R&D engine re-igniting? Thoughts on the EBO partnership with Microsoft for data center connectivity.

3M recently announced a strategic partnership with Microsoft centered around Expanded Beam Optical (EBO) technology - 3M's non-contact optical fiber connectivity technology for next-generation AI data centers. At its core, EBO addresses a key operational challenge in optical fiber connectivity: contamination from dust particles. Unlike traditional Multi-fiber Push On (MPO) connectors (which rely on physical fiber-to-fiber contact and require regular inspection and cleaning procedures), EBO uses a lens array to expand and refocus light across an air gap. The result is a connector that is inherently more tolerant to dust and contamination, while materially reducing installation complexity and deployment timelines. According to 3M, installation times can be reduced from roughly three minutes (for a traditional MPO) to thirty seconds per connection (for EBO). There is some strategic significance beyond the Microsoft partnership. Generally, successful technology adoption begets more adoption, and validation by one large hyperscaler often accelerates broader industry uptake. We think Microsoft's endorsement serves as an important signal to other hyperscalers evaluating EBO optical fiber connectivity architectures for increasingly dense AI clusters, where reliability, deployment speed, and operational efficiency are critical design considerations. From a competitive standpoint, 3M appears reasonable well-positioned. With patent protection extending until at least 2041, participation in the broader EBO ecosystem through the Multi-Source Agreement, an early manufacturing lead, and the absence of credible hyperscaler-scale competitive offerings collectively strengthen the company's position. While important questions remain around monetization, pricing durability, and the potential emergence of alternative standards, we believe the announcement (link) represents a meaningful milestone in the commercialization journey of EBO.

For our own thesis on 3M, where we have highlighted weakness in R&D as a reason driver behind our tepid growth forecasts, we see the partnership as an encouraging move in the right direction.

We rate MMM Underperform with a TP of \$131. We remain concerned longer-term around R&D and PFAS. However, we do acknowledge that this partnership indicates 3M is making progress in the right direction on R&D.

## Investment Implications

<table><tr><td>Close Date</td><td></td><td></td><td colspan="2">16 Jul 2026</td></tr><tr><td>MMM Close Price (USD)</td><td></td><td></td><td colspan="2">161.77</td></tr><tr><td>Price Target (USD)</td><td></td><td></td><td colspan="2">131.00</td></tr><tr><td>Upside/(Downside)</td><td></td><td></td><td colspan="2">(19)%</td></tr><tr><td>52-Week Range</td><td></td><td></td><td colspan="2">177.41/139.34</td></tr><tr><td>SPX</td><td></td><td></td><td colspan="2">7,533.77</td></tr><tr><td>FYE</td><td></td><td></td><td colspan="2">Dec</td></tr><tr><td>Div Yield</td><td></td><td></td><td colspan="2">1.9%</td></tr><tr><td>Market Cap (USD) (M)</td><td></td><td></td><td colspan="2">84,374</td></tr><tr><td>EV (USD) (M)</td><td></td><td></td><td colspan="2">93,401</td></tr><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>1.0</td><td>1.6</td><td>(3.6)</td><td>1.7</td></tr><tr><td>SPX (%)</td><td>10.1</td><td>0.3</td><td>8.6</td><td>20.3</td></tr><tr><td>Relative (%)</td><td>(9.0)</td><td>1.3</td><td>(12.1)</td><td>(18.6)</td></tr><tr><td colspan="5">Source: Bloomberg, Bernstein estimates and analysis.</td></tr></table>

Price Performance, 1YR

![](images/7d6930e8cf1dd54ec897fdb126f450d391d6b25d59767bf40fcd3ac342941f8f.jpg)

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>MMM (USD)</td><td>8.06</td><td>8.53</td><td>9.32</td><td>Revenues (M)</td><td>24,948</td><td>24,951</td><td>25,641</td><td>--</td><td>Adjusted P/E (x)</td><td>20.1</td><td>19.0</td><td>17.4</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

## DETAILS

Optical fiber cables are the circulatory system of modern data centers. Rather than transmitting electrical signals through copper wires, they carry information as pulses of light, enabling high bandwidth, low latency, and efficient transmission across the entire data center ecosystem. As AI rack densities continue to increase, the volume of data moving between GPUs, switches, and servers has increased exponentially, making optical fiber the preferred medium for high-performance networking and data transfer. In simple terms, the primary function of optical fiber is to move data quickly, reliably, and with minimal signal loss between servers, racks, rows and buildings, allowing thousands of servers to operate as a single coordinated system. In hyperscaler and AI-focused data centers, network performance is increasingly becoming as important as compute performance itself.

However, optical fibers are only useful if they can be efficiently connected together throughout the network. This is where optical fiber connectors come into play. Connectors are the physical interfaces that join one optical fiber to another, creating the data pathways that link servers, switches, storage systems, and networking equipment across a data center. Because light must pass from one fiber into the next with very high precision, connector quality directly impacts network reliability and performance. Traditional connector designs (called Multi-fiber Push On or MPO) rely on physical fiber-to-fiber contact, which makes them highly sensitive to contamination and handling.

## What is the Expanded Beam Optical (EBO) technology?

The fundamental innovation behind EBO is the elimination of physical contact between optical fibers. Traditional MPO connectors require fiber ends to be pressed together, making performance highly sensitive to contamination and creating a mandatory inspection-and-cleaning workflow prior to deployment. Even a micro-thickness dust particle can cause contamination that causes link failure. EBO replaces this architecture with a proprietary lens array that expands the optical beam significantly (to the order of $\sim 150x$ ) through a lens array before transmitting it across an air gap and refocusing it into the receiving fiber. By removing physical contact from the connection process altogether, EBO materially improves dust tolerance while simplifying installation procedures. 3M received a patent for EBO technology in Jan 2025, with an expiration through at least August 2041.

## Advantages of EBO over Traditional MPO

The practical benefits of EBO become apparent when compared directly against traditional MPO connectors. The non-contact design materially reduces contamination sensitivity, removes inspection requirements, minimizes cleaning procedures, and shortens installation times by \~85% (according to a 3M whitepaper explaining deployment at a hyperscaler facility in the United States). Beyond the obvious labor savings, these improvements have meaningful implications for large-scale data center construction where thousands of optical fiber connections must be deployed and maintained.

## Overview of 3M and Microsoft strategic partnership

In our view, the partnership creates clear value for both parties. For Microsoft, EBO offers lower installation costs, improved reliability in increasingly dense AI architectures, and faster deployment timelines that can accelerate the monetization of data center investments. Given the scale of hyperscaler capital expenditures, even modest improvements in deployment efficiency can translate into sizable economic benefits. For 3M, the value proposition is validation. Microsoft's adoption provides the first hyperscaler-scale validation of EBO, supports the rationale behind recent manufacturing expansion investments, and establishes an important customer reference point that could influence future adoption decisions across the broader hyperscaler data center ecosystem. Separately, Microsoft's Frontier Company initiative will support 3M's own enterprise transformation efforts, reinforcing management's ongoing focus on operational efficiency and process improvement.

## Traditional Multi-fiber Push On (MPO)

![](images/acd118ffbe3d66c8ed078e7f19337a3074240b4ca18bd72f77584de373dfb7e0.jpg)

Polished fiber ends are pressed together and have physical contact; even a micro-dust particle at the contact site can scatter or block the light path, causing link failure

3M Expanded Beam Optical (EBO)  
![](images/34b67ce17ebcd960615f5bd6b2f923ef39d61a9fcc9e917c7d4712a43f922825.jpg)

A proprietary 3M lens array expands the beam $\sim 150x$ before it crosses a contactless air gap, then refocuses into the receiving fiber; 3M has patent for this technology (until 2041)\*

EBO eliminates fiber-to-fiber physical contact, removing mandatory pre-installation inspection & cleaning at each connection node (required in traditional MPO); delivering inherently dust-tolerant performance

\* United States patent publication number US2023/0056995A1

Source: Bernstein Analysis

EXHIBIT 2: EBO is better than MPO across a range of technical attributes

<table><tr><td></td><td>Theme</td><td>Traditional MPO</td><td>3M EBO</td></tr><tr><td>1</td><td>Connection mechanism</td><td>Direct fiber-to-fiber physical contact</td><td>No contact (beam crosses air gap via lens array)</td></tr><tr><td>2</td><td>Contamination sensitivity</td><td>High (one dust particle disrupts signal, causing overall link failure)</td><td>Low (beam is ~150x larger and much less sensitive as a result, air gap resistance is negligible)</td></tr><tr><td>3</td><td>Inspection requirement</td><td>Yes (at every connection node)</td><td>No (requirement eliminated entirely)</td></tr><tr><td>4</td><td>Cleaning requirement</td><td>Yes (at every connection node, at routine intervals)</td><td>Minimal</td></tr><tr><td>5</td><td>Installation time (per connector)*</td><td>~3 minutes</td><td>~30 seconds (~85% reduction in installation time)</td></tr><tr><td>6</td><td>Deployment time*</td><td>~6 months</td><td>~3 days</td></tr></table>

\* Based on actual 3M deployment with a hyperscaler data center in the United States

Source: 3M Whitepaper (2025), Company Website, Bernstein Analysis

## EXHIBIT 3: Why the strategic partnership?

## What does 3M get?

## 1 First hyperscaler validation

\- Microsoft becoming the first Tier-1 cloud provider to deploy EBO transforms it from a promising pilot to production-validated technology at hyperscaler-level

\- Sets a historical precedent: once one hyperscaler endorses, others follow within 12-24 months

## 2 Demand-led capacity expansion confirmed

• 3M announced >2x capacity expansion for US EBO manufacturing in March 2026 (4 months before this deal)

\- Microsoft deployment confirms that the supply-side bet was correct, de-risking the capex

## 3 Microsoft AI for internal enterprise transformation

\- Microsoft Frontier Company (new enterprise AI vertical launched in July 2026) engineers deployed to automate 3M order management workflows (credit checks, delinquency, system updates etc.)

• Augments ongoing 3M operational efficiency improvement narrative for investors

## What does Microsoft get?

## 1 Operational cost reduction

\- \~85% reduction in installation time per connector (vs MPO) to \~30 seconds (EBO)

\- Elimination of inspection & cleaning at every connection node removes significant technician labor and tooling requirements

## 2 Improved reliability in high-density AI rack architectures

\- Any micro-dust particle can degrade cluster performance by causing link failure

\- EBO dust-tolerant non-contact design directly tackles the core problem of dense cabling environments

## 3 Reduced time to deployment (accelerated time to revenue)

\- At \~\$75B+ annual capex on data centers, this can have a direct material P&L impact

## 3M competitive advantage

3M's competitive advantage appears to stem from a combination of intellectual property, ecosystem positioning, and manufacturing execution. The company's patented ferrule and lens-array design effectively positions 3M at the center of the EBO ecosystem, with partner companies building solutions around the core technology through the Multi-Source Agreement framework (MSA partners can be thought of as integrated cable manufactures / assemblers, all of whom use the proprietary 3M ferrule design as a base). This creates opportunities spanning both direct product sales and potential licensing economics. Importantly, 3M remains the only participant to demonstrate EBO at meaningful hyperscaler data center scale, and recent investments in manufacturing capacity further reinforce their first-mover advantage. Potential competitors to 3M EBO include established fiber manufacturers (such as Corning, CommScope) and legacy EBO players (TE Connectivity, Amphenol which have EBO for military and industrial applications). None of these players currently offer comparable hyperscaler-focused EBO solutions, suggesting that 3M retains a meaningful lead in commercialization, at least as of today.

## Key factors to watch out for

Despite the positive implications of today's announcement, several important questions remain. First, investors may struggle to quantify near-term financial impacts given that 3M does not separately disclose data center-related revenues and has not provided explicit content metrics (in \$/MW terms) tied to data center deployments. Second, while the MSA framework supports ecosystem adoption, it could eventually contribute to price pressure on certain components over time. Third, broader hyperscaler adoption is not guaranteed, as alternative connector standards could emerge from competitors or be adopted by other cloud operators. Finally, incumbent connectivity suppliers maintain deep customer relationships and possess substantial technical resources, creating the possibility of competing solutions (that do not overlap with 3M's patents) in future years. While none of these risks alter our positive interpretation of today's announcement, they remain important factors to monitor as the EBO ecosystem develops further.

## EXHIBIT 4: Why 3M leads, and why that appears likely to be the case going forward as well?

<table><tr><td colspan="2">3M edge</td></tr><tr><td>1</td><td>Patented ferrule designLens array and ferrule design is patent-protected (granted in Jan 2025, valid until at least Aug 2041)*Every EBO optical fiber assembly (regardless of the actual assembler), runs on a 3M ferrule</td></tr><tr><td>2</td><td>Hub-and-spoke licensing model via EBO MSA3M co-founded the EBO Multi-Source Agreement with TE Connectivity, Amphenol, AMD, Cisco, Meta, Oracle, Arista, Molex among others as partnersPartners &quot;build&quot; cables around the 3M ferrule as baseLicensing royalties and component supply agreements compou

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
