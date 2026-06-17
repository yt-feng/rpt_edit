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
# US Communications Infrastructure

# Data Center Interconnection: A literal network effect

![](images/06d2c307aaeb6bf036e64d26fd8a263db54598b7d01cd50e5948e8e62ed65e06.jpg)  
Madison Rezaei

+1 917 344 8622

madison.rezaei@bernsteinsg.com

![](images/c02991a5ea7d2bfd002e51b6d3808f7dcc4dda280ebc9293d8d8ad0c536bef7c.jpg)

Nancy Wu

+1 917 344 8545

nancy.wu@bernsteinsg.com

If you've been paying attention to any players in the data center colocation market, it'd be hard to miss conversations on interconnection. Interconnection is simply linking networks to one another and handing off data, keeping the traffic off of the public internet. Players do this to minimize costs, lower latency, and increase security. It's an \~\$8B market, but measurement has always been a bit wishy-washy...we recently unearthed a new data source and constructed our own proprietary database, giving us new insight into the players. Spoilers: EQIX is even stronger than you think and AMT's CoreSite is a great asset.

For enterprise colo data centers, interconnection is a high-margin (70-90%), high-moat layer that shifts a data center from being commoditized power and space to being a true network hub. Cross connects (whether physical or virtual) are cheap to make, sticky for customers, and multiply in value as campuses fill - a literal network effect.

Historically this segment was more buying criteria than revenue driver, but with AI's emergence, interconnect is becoming a real growth story. Data is getting heavier, models bigger, and workloads increasingly latency sensitive...interconnection is increasingly dictating not only a data center's right to win, but also its own meaningful revenue stream.

In our new dataset, we look at 645 of the most critical interconnected enterprise collocation facilities in the world. Across them, we register 21,000+ interconnections from various network providers across a series of categories: Cloud On-Ramps, Tier 1 / Global Transit providers, Content / CDNs, US + Can ISPs, Global ISPs, Interconnect Economy Players, and Neoclouds.

Our overwhelming takeaway is that EQIX has more, denser facilities than anyone else - 222 facilities with an average of 58 interconnect partners per site, supporting 513k revenue-generating interconnections (as of 1Q26). The next closest is CoreSite (owned by AMT) with 29 facilities and an average of 46 providers per site. DLR comes in second in terms of total networks, but fourth on a per-facility average (34), expected given their relatively recent shift to enterprise.

60% of our observed cloud on-ramps are in an EQIX facility. In fact, 57% of the facilities with 3+ on-ramps belong to EQIX; DLR is a distant second with 23%. This is both meaningful and hard to replicate.

There is a geographic angle - EQIX's footprint overindexes towards interconnection in the U.S., where the average cross-connect is \~\$342 relative to \~\$197 in the rest of the world (EQIX proxies). DLR has some exceptionally strong, dense European facilities - their Frankfurt hub has 611 networks (Equinix Sao Paulo next highest at 586), but inherently lower cross-connect prices.

So what does this analysis mean for investors? EQIX's interconnect moat is sizeable, defensible, and valuable. We maintain our Outperform on the stock with a target price of \$1,222 and feel that there's still room despite its run this year (+39% YTD). We believe there may be even further upside as interconnect continues to grow, which would bolster both top and bottom line for EQIX.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">15 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>DLR (Digital Realty)</td><td>O</td><td>USD</td><td>184.90</td><td>232.00</td><td>(20.4)%</td><td>USD</td><td>3.87</td><td>2.74</td><td>2.37</td><td>47.8</td><td>67.6</td><td>77.9</td></tr><tr><td>EQIX (Equinix)</td><td>O</td><td>USD</td><td>1,064.38</td><td>1,222.00</td><td>(7.2)%</td><td>USD</td><td>14.96</td><td>17.88</td><td>21.36</td><td>71.1</td><td>59.5</td><td>49.8</td></tr><tr><td>AMT (American Tower)</td><td>O</td><td>USD</td><td>185.76</td><td>207.00</td><td>(39.9)%</td><td>USD</td><td>5.40</td><td>6.60</td><td>7.08</td><td>34.4</td><td>28.2</td><td>26.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,554.29</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We value DLR on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$232 price target is based on 27x our 2027E AFFO per share of \$8.52.

We value EQIX on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$1,222 price target is based on 25x our 2027E AFFO per share of \$48.63.

We value AMT on a Price to NTM Adjusted Funds From Operations (AFFO) per share multiple. Our \$207 price target is based on 18x our 2027E AFFO per share of \$11.49.

## DETAILS

## INTERCONNECTION CONTEXT

## A BRIEF HISTORY ON INTERCONNECTION AND WHY IT EXISTS TODAY

Originally, data centers were glorified computer closets. But with the advent of the internet, the market realized it needed neutral hosts where telcos and ISPs could meet and swap traffic. This was the origin of the “meet-me room” (MMR $^{1}$ ), when cross-connects became critical pieces of fiber. Then clouds / SaaS / content platforms came into being, and they too needed to swap traffic - the carrier hotels with meet me rooms were the logical locations...an interconnection moat began to form.

Now, we're in the world of multicloud, edge, and AI, where interconnection is critical infrastructure. For an enterprise, data center capacity is no longer only about the building, it's also about the access and proximity to an increasingly broad partner set. Today, it's both colocation buying criteria and a product in itself.

## FLAVORS OF INTERCONNECTION

We have a few different types of interconnection, serving different purposes within the ecosystem.

1. Physical cross-connects (inside the facility): the most basic building block: a direct, point-to-point cable between two parties in the same data center, usually fiber or copper via a patch panel or meet-me room. Physical cross-connects are simple, predictable, and offer low-latency, private connectivity between an enterprise and a carrier, cloud on-ramp, or another tenant. Economically, they are sold as recurring monthly connections with a one-time install fee, and once in place they tend to be very sticky because they underpin production traffic. For AI, these links often tie GPU clusters to nearby storage, network providers, and cloud on-ramps within the same campus.  
2. Data center interconnect (between facilities): extends the idea beyond a single building, linking multiple data centers within a campus so they can share workloads and data. At the short end, campus and metro connects make several sites in a city behave like one logical platform; at the long end, inter-market and regional connects support replication, disaster recovery, and performance across geographies. This layer lets customers design active-active architectures, spread AI training and inference across sites, and treat a provider's footprint as a single resource rather than isolated buildings.  
3. Virtual cross-connections and software-defined network fabrics: Virtual cross-connects (VXCs) take the cross-connect concept and implement it in software over an existing network fabric. Instead of running a new cable each time, a customer uses a portal or API to create a private Layer 2 connection between two endpoints on the fabric — for example, between their port in a colo facility and a cloud region, or between two different data centers. The key differences versus physical cross-connects are provisioning speed and flexibility: VXCs can often be set up or removed in minutes, and capacity can be adjusted without touching any physical cabling. That makes them a useful tool for AI and multicloud workloads, where teams may need to test new data paths, connect to additional regions, or scale bandwidth for specific training runs without waiting on manual changes. Importantly, while the provisioning is virtual in a VXC, the termination is still physical.

EXHIBIT 1: Global Registered Network Connections by Provider (Units)  
![](images/379aefed013eb745bfdebba61d4bbd7e63f4fec6844c505d2898e0986814149f.jpg)

<details>
<summary>bar chart</summary>

Global Registered Network Connections by Provider (Units)
| Provider | Number of Registered Networks |
| :--- | :--- |
| Equinix | 12,864 |
| Digital Realty | 4,702 |
| CoreSite | 1,278 |
| Cologix | 685 |
| DataBank | 509 |
| Netrality | 329 |
| QTS | 232 |
| Flexential | 195 |
| CyrusOne | 105 |
| Others | 253 |
</details>

Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 2: Global Interconnected Sites by Provider (Units)  
![](images/62ff3454d5ff1e31b61d58e55783688c86d59e3ebc04de46d6eb69ee5fb91498.jpg)

<details>
<summary>bar chart</summary>

| Provider        | Units |
| --------------- | ----- |
| Equinix         | 222   |
| Digital Realty  | 140   |
| DataBank        | 63    |
| Cologix         | 44    |
| Flexential      | 40    |
| CyrusOne        | 33    |
| CoreSite        | 29    |
| QTS             | 25    |
| Netrality       | 9     |
| Others          | 40    |
</details>

Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 3: Average and Median Networks by Facility by Provider (Units)  
![](images/f5d92a17abab67378742b137f7abdfa5b37833437eef44e3567947e9b22ad063.jpg)

<details>
<summary>bar chart</summary>

Average and Median Networks by Facility by Provider (Units)
| Provider | Average (Units) | Median (Units) |
| :--- | :--- | :--- |
| Equinix | 58 | 24 |
| Digital Realty | 34 | 7 |
| CoreSite | 46 | 19 |
| Cologix | 16 | 8 |
| DataBank | 8 | 4 |
| Netrality | 37 | 41 |
| QTS | 9 | 7 |
| Flexential | 5 | 3 |
| CyrusOne | 3 | 2 |
</details>

Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 4: Densest Global Interconnection Sites by Registered Network Count  
![](images/92dbed0a8786ffaef7dedc242c38c96e2bfc97c6986e05ff6e2a0089d531a846.jpg)

<details>
<summary>bar chart</summary>

Densest Global Interconnection Sites by Registered Network Count
| Densenst Global Interconnection Site | Count |
| :--- | :--- |
| Digital Realty Frankfurt FRA1-27 | 611 |
| Equinix SP4 - Sao Paulo | 586 |
| Equinix FR5 - Frankfurt, KleyerStrasse | 534 |
| Equinix SG1 - Singapore | 520 |
| Equinix DC1-DC15,DC21-DC22 - Ashburn | 508 |
| CoreSite - Los Angeles (LA1) One Wilshire | 339 |
| Equinix CH1/CH2/CH4 - Chicago | 329 |
| Equinix MI1 - Miami, NOTA | 327 |
| Equinix LD8 - London, Docklands | 319 |
| Equinix SV1/SV5/SV10 - Silicon Valley, San Jose | 283 |
| Equinix MB1 - Mumbai (GPX Mumbai 1) | 246 |
| Equinix WA1 - Warsaw, Centrum LIM | 241 |
| Equinix SP2 - Sao Paulo | 237 |
| Digital Realty Seattle SEA10 | 233 |
| Digital Realty Madrid MAD1-2 | 231 |
| Digital Realty Marseille MRS1/2/3/4 | 216 |
| Equinix AM7 - Amsterdam, Kuiperberweg | 213 |
| Equinix HK2 - Hong Kong | 199 |
| Equinix SY1/SY2 - Sydney | 197 |
</details>

Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 5: Average Registered Network per Site by Provider (Units)  
Average Registered Network per Site by Provider (Units)  
![](images/48d6b670ab066495ab07fec4fd7f2cbaee271f31d2ff20d620a8b6e5e98165ea.jpg)

<details>
<summary>bar chart</summary>

| Company | Value |
| :--- | :--- |
| Equinix | 58 |
| CoreSite | 46 |
| Netrality | 37 |
| Digital Realty | 34 |
| Cologix | 16 |
| QTS | 9 |
| DataBank | 8 |
| Flexential | 5 |
| CyrusOne | 3 |
| Other | 16 |
</details>

Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

## INTERCONNECTION PARTNERS

Interconnection is fundamentally about who an operator can put “across the aisle” from an enterprise rack. The richer the mix, the more valuable every incremental port and cross-connect becomes. Enterprise colo providers that assemble diverse, carrier-neutral ecosystems can monetize the same piece of real estate multiple times through cross-connects, ports, and virtual links, while also making their campuses the default location for new workloads.

For our database, we have assessed \~80 specific providers across seven categories.

- Hyperscalers: Amazon (AWS), Google (GCP), $^{2}$ Microsoft (Azure), Oracle (OCP), $^{3}$ IBM Cloud, $^{4}$ Alibaba (on ramps only for first four) $^{5}$  
- Tier 1 Global Transit Partners: Lumen, Arelion, Cogent, NTT, GTT, Zayo, Tata, TI Sparkle, Orange International, Telxius, PCCW Global, Vodafone Global Network, DT ICSS  
- Content + CDN Providers: Cloudflare, $^{6}$ Akamai, Fastly, Netflix, $^{7}$ Meta, $^{8}$ Apple, $^{9}$ Valve, Twitch, ByteDance  
• US / Canada ISPs: Comcast, Charter, AT&T, Verizon, T-Mobile, $^{10}$ Cox, Altice USA, Frontier, Bell Canada, Rogers, Telus

- Global ISPs: BT, Vodafone (consumer), Telefónica, $^{11}$ Iliad/Free, Sky, Liberty Global, KPN, Swisscom, Proximus, Telia (consumer), Telenor, $^{12}$ Türk Telekom; Singtel, Telstra, KDDI, SoftBank, $^{13}$ Reliance Jio, Airtel, SK Broadband, KT, Claro, Telmex  
- Interconnect Economy Players: Hurricane Electric, Internet2, Megaport, Zscaler, $^{14}$ PacketFabric, Zenlayer, ESnet, and GÉANT  
- Neoclouds: CoreWeave, Nebius, Lambda, Crusoe, Together AI, Vultr, Voltage Park, IREN, Applied Digital, NVIDIA NGC $^{15}$

EXHIBIT 6: % of Interconnected Facilities That Have at Least 1 Provider per Category

<table><tr><td>Inter. Comp.</td><td>Hyperscalers</td><td>Tier 1 GTP</td><td>Content + CDN</td><td>US &amp; Can. ISPs</td><td>Global ISPs</td><td>Interconnect Econ.Players</td></tr><tr><td>Equinix</td><td>33%</td><td>57%</td><td>45%</td><td>51%</td><td>69%</td><td>40%</td></tr><tr><td>Digital Realty</td><td>21%</td><td>20%</td><td>21%</td><td>28%</td><td>24%</td><td>26%</td></tr><tr><td>CoreSite</td><td>5%</td><td>7%</td><td>6%</td><td>7%</td><td>3%</td><td>9%</td></tr><tr><td>Cologix</td><td>7%</td><td>5%</td><td>5%</td><td>2%</td><td>1%</td><td>6%</td></tr><tr><td>DataBank</td><td>10%</td><td>4%</td><td>7%</td><td>7%</td><td>1%</td><td>3%</td></tr><tr><td>Netrality</td><td>2%</td><td>2%</td><td>2%</td><td>5%</td><td>0%</td><td>3%</td></tr><tr><td>QTS</td><td>4%</td><td>2%</td><td>3%</td><td>0%</td><td>0%</td><td>6%</td></tr><tr><td>Flexential</td><td>7%</td><td>1%</td><td>0%</td><td>0%</td><td>1%</td><td>2%</td></tr><tr><td>CyrusOne</td><td>4%</td><td>1%</td><td>3%</td><td>0%</td><td>1%</td><td>2%</td></tr><tr><td>Others</td><td>7%</td><td>2%</td><td>7%</td><td>0%</td><td>0%</td><td>1%</td></tr></table>

Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 7: Average Number of Providers by Category Per Interconnected Building (Units)

<table><tr><td>Inter. Comp.</td><td>Hyperscalers</td><td>Tier 1 GTP</td><td>Content + CDN</td><td>US &amp; Can. ISPs</td><td>Global ISPs</td><td>Interconnect Econ.Players</td></tr><tr><td>Equinix</td><td>0.64</td><td>0.47</td><td>0.39</td><td>0.10</td><td>0.35</td><td>0.36</td></tr><tr><td>Digital Realty</td><td>0.64</td><td>

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
