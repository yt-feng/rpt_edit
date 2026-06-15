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
## Global Energy Storage

# Global Energy Storage: How to power AI with solar-plus-storage

![](images/0e9de7c08efcadde37d724c27bfb44a41b946ab2d8060b813fa4344ec6e6699a.jpg)

Brian Ho, CFA

+852 2123 2615

brian.ho@bernsteinsg.com

![](images/205faff560a86e9a6d7174d727fe62073267961a9c2bc1932a3ace071a2f6a09.jpg)

Neil Beveridge, Ph.D.

+852 2123 2648

neil.beveridge@bernsteinsg.com

![](images/ca87267ccf4fe86c835719866576b0a5b9f17d41b445f94a58fbc187e93c0bad.jpg)

Kelvin Yuan, Ph.D., CFA

+852 2123 2612

kelvin.yuan@bernsteinsg.com

The industry has long viewed solar-plus-storage as insufficient for baseload power particularly for 24/7 AI-driven demand. Masdar and EWEC's gigascale solar-plus-storage project challenges this view with the world's first deployment of firm renewable power at scale. Our analysis leaves us incrementally more constructive on solar-plus-storage as a competitive source of baseload power, with Sungrow and CATL as key beneficiaries.

Solar-plus-storage can deliver baseload reliability at scale. UAE's Masdar and EWEC are building 5.2 GW of solar combined with 19 GWh of storage (19 hours duration) to deliver \~1 GW of continuous power, with completion targeted by 2027. Based on our analysis, the system could achieve \~99.6% system reliability, representing a structural shift in renewables from intermittent energy sources to providers of firm capacity.

Economics are competitiveness particularly for higher gas price markets. While the upfront capex is high at \~\$6,000/kW, solar-plus-storage benefits from low operating costs and zero fuel exposure. At an estimated LCOE of \$97/MWh for the project, solar-plus-storage can compete with gas-fired power at gas price of \~\$8/mmbtu or higher. At 12-hour storage scenario, the LCOE falls to around \$80/MWh which can still achieve high system reliability of 95%. The attractiveness of solar-plus-storage as baseload is important given ongoing volatility and disruption in global gas supply. That said, we still believe gas-fired power is favored in regions with abundant low cost gas supply such as the US.

Faster deployment versus gas and nuclear is a key advantage. Solar and storage projects can be delivered in roughly two years, compared with current gas turbine lead times of around four years due to supply constraints, and even longer timelines for nuclear, typically six years or more.

The key constraint is access to high solar irradiance and land. While the system is replicable, we think it is still limited to solar-rich regions with abundant, low-cost land. This project alone requires $\sim60\ km^{2}$ of land—roughly the size of Manhattan—highlighting the significant physical footprint required to deliver firm renewable power at scale.

Storage is the primary driver of system economics rather than solar. ESS account for roughly half of total project capex, meaning cost competitiveness is primarily driven by storage cost, efficiency, and performance rather than module pricing.

We expect global ESS demand to grow at \~34% CAGR over the next five years, driven by the need for firming renewable generation and grid stability. Within the value chain, CATL leads in ESS battery supply and technology, while Sungrow is a key player in system integration, inverters, and broader power conversion solutions, positioning both as primary beneficiaries of this structural shift.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">12 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>300750.CH (CATL)</td><td>O</td><td>CNY</td><td>394.85</td><td>800.00</td><td>18.9%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>24.5</td><td>18.0</td><td>13.7</td></tr><tr><td>247540.KS (EcoPro BM)</td><td>U</td><td>KRW</td><td>167,800</td><td>140,000</td><td>32.9%</td><td>KRW</td><td>403.00</td><td>854.00</td><td>1,963.00</td><td>416.4</td><td>196.5</td><td>85.5</td></tr><tr><td>051910.KS (LG Chem)</td><td>M</td><td>KRW</td><td>320,000</td><td>298,000</td><td>20.7%</td><td colspan="2">KRW(13,258.70)</td><td>2,042.47</td><td>31,118</td><td>(24.1)</td><td>156.7</td><td>10.3</td></tr><tr><td>373220.KS (LGES)</td><td>M</td><td>KRW</td><td>387,000</td><td>347,000</td><td>(9.9)%</td><td colspan="2">KRW (5,308.10)</td><td>1,811.04</td><td>9,452.97</td><td>(72.9)</td><td>213.7</td><td>40.9</td></tr><tr><td>003670.KS (Posco Future M)</td><td>U</td><td>KRW</td><td>188,800</td><td>190,000</td><td>13.4%</td><td colspan="2">KRW (2,740.96)</td><td>376.72</td><td>898.20</td><td>(68.9)</td><td>501.2</td><td>210.2</td></tr><tr><td>006400.KS (SDI)</td><td>M</td><td>KRW</td><td>507,000</td><td>520,000</td><td>168.1%</td><td colspan="2">KRW (9,933.80)</td><td>2,099.51</td><td>18,376</td><td>(51.0)</td><td>241.5</td><td>27.6</td></tr><tr><td>300274.CH (Sungrow)</td><td>O</td><td>RMB</td><td>148.76</td><td>185.00</td><td>90.9%</td><td>RMB</td><td>6.55</td><td>8.22</td><td>9.33</td><td>22.7</td><td>18.1</td><td>15.9</td></tr><tr><td>002466.CH (Tianqi Lithium)</td><td>O</td><td>CNY</td><td>62.50</td><td>73.00</td><td>63.3%</td><td>CNY</td><td>0.28</td><td>3.29</td><td>6.18</td><td>221.5</td><td>19.0</td><td>10.1</td></tr><tr><td>9696.HK (Tianqi Lithium)</td><td>O</td><td>HKD</td><td>47.58</td><td>61.00</td><td>36.7%</td><td>CNY</td><td>0.28</td><td>3.29</td><td>6.18</td><td>145.5</td><td>12.5</td><td>6.6</td></tr><tr><td>034020.KS (Doosan Enerbility)</td><td>O</td><td>KRW</td><td>90,100</td><td>95,000</td><td>32.8%</td><td>KRW</td><td>173.88</td><td>45.91</td><td>687.53</td><td>518.2</td><td>N/M</td><td>131.0</td></tr><tr><td>3750.HK (CATL)</td><td>M</td><td>HKD</td><td>670.00</td><td>770.00</td><td>77.7%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>35.8</td><td>26.3</td><td>20.1</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,966.72</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
003670.KS, 034020.KS base year is 2024;  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

In a structurally power-constrained world, solar-plus-storage is emerging as an increasingly important solution to deliver stable, baseload-like power, particularly for fast-growing AI and data center demand. The Masdar project demonstrates that, with sufficient overbuild and long-duration storage, renewables could achieve high system reliability while offering competitive economics in higher gas price environments, alongside the key advantages of being emissions-free and having no fuel price risk. While scalability remains dependent on geography, land availability, and grid infrastructure, the overall direction is clearly positive, with costs expected to decline further through scale and ongoing technology improvements, including next-generation batteries such as sodium-ion. As storage now drives system economics and demand continues to accelerate, we see strong upside for global ESS deployment and recommend Sungrow and CATL as key beneficiaries of this structural shift.

## DETAILS

The UAE's Masdar and EWEC project demonstrates at scale that solar-plus-storage can deliver firm baseload power. This fundamentally reframes the role of renewables: the key question is no longer whether solar can generate cheap energy, but whether it can reliably meet a continuous load profile when paired with sufficient storage and overbuild. The project combines 5.2 GW of solar with 19 GWh of storage to deliver \~1 GW of continuous power, with completion targeted by 2027. This represents the first gigascale attempt to overcome solar intermittency through system design, and therefore serves as a key proof point for the industry. We find that solar-plus-storage is increasingly cost competitive in higher gas price environments. At current cost levels, it can compete with gas-fired generation when fuel prices are elevated, making it an attractive alternative amid volatility in global gas markets. However, gas remains structurally advantaged in regions with persistently low fuel costs, such as the US.

EXHIBIT 1: Solar plus storage (12+ hours) are competitive against gas-fired power at high gas prices  
![](images/766e1072c17a7a2945458340dd99f33f7ce547889c423267c87e0442c09a7170.jpg)

<details>
<summary>line chart</summary>

| Gas price ($/mmbtu) | LCOE ($/MWh) |
| ------------------- | ------------ |
| 4                   | 65           |
| 17                  | 160          |
</details>

Source: Company data, Bernstein analysis

We estimate total project capex at approximately \$6bn for 1GW of firm solar-plus-storage capacity (or \~\$6,000/kW). This can be broadly broken down into \~\$0.5bn for solar modules, \~\$0.5bn for inverters and balance-of-plant, and \~\$2.5bn for ESS, with the remaining \~\$2.5bn covering grid/electrical infrastructure, EPC, land, and other development costs. The key takeaway is that while solar generation itself is already low cost, storage dominates the economics, accounting for roughly half of total system cost. As a result, the competitiveness of baseload solar-plus-storage is primarily driven by battery cost declines rather than further reductions in module pricing. This reinforces our view that continued cost reductions in ESS will be the critical enabler for scaling firm renewable power.

EXHIBIT 2: We estimate total project capex at approximately \$6bn (or \~\$6,000/kW). Energy storage dominates the economics  
![](images/6ee1c40b83014698da378c020f9f19d58dd7086427a3b0bac5d8c62075e4bc76.jpg)

<details>
<summary>bar chart</summary>

Project cost ($bn) for 5.2GW solar + 19GWh storage = 1GW baseload power
| Project developer | Project cost ($bn) |
| :--- | :--- |
| Solar module | 0.5 |
| Inverter and BOP | 0.5 |
| ESS (excl. EPC) | 2.5 |
| Other (Electrical, EPC, Land) | 2.5 |
Jinko Solar
JA SOLAR
CATL SUNGROW
Jinko MASDAI
EWEC
中国电建 POWERCHINA
Larsen & TOUBRO
</details>

CATL and Sungrow are covered by Bernstein. All other companies are not covered by Bernstein.  
Source: Company data, Bernstein analysis and estimates

Solar-plus-storage is emerging as a credible alternative to traditional baseload generation, offering several advantages over gas and nuclear, but with clear trade-offs. The Masdar project demonstrates that, with sufficient overbuild and long-duration storage, renewables can achieve near-baseload reliability (\~99% uptime), while also benefiting from faster deployment timelines of \~2 years compared to \~3–6 years for gas (given turbine bottlenecks) and \~6+ years for nuclear. Economically, solar-plus-storage is increasingly competitive in higher gas price environments, providing cost certainty without fuel price exposure. However, it remains constrained by geography, requiring high solar irradiance and large land footprints, and its economics are heavily dependent on battery costs, which account for \~50% of capex. By contrast, gas remains more flexible and competitive in low-cost fuel markets such as the US, while nuclear offers the highest level of clean baseload reliability but with significantly longer build times and higher execution risk. As such, solar-plus-storage can deliver very competitive firm power in select regions, particularly for new demand such as AI and data centers.

EXHIBIT 3: Comparison of solar-plus-storage, gas and nuclear power for baseload power

<table><tr><td>Metric</td><td colspan="2">Solar + Storage (12+ hours)</td><td colspan="2">Gas - CCGT</td><td colspan="2">Nuclear</td></tr><tr><td>Uptime</td><td>~90–99.x%</td><td>√</td><td>~95–99.9%</td><td>√</td><td>~95–99.9%</td><td>√</td></tr><tr><td>LCOE</td><td>~$80-100/MWh</td><td>√</td><td>~$50/MWh ($3.5/mmbtu) ~$110/MWh ($12/mmbtu)</td><td>√</td><td>~$50-150/MWh</td><td></td></tr><tr><td>Lead time</td><td>~2 years</td><td>√</td><td>~3–6 years</td><td></td><td>6+ years</td><td></td></tr><tr><td>Land requirement</td><td>~60 km2</td><td></td><td>~0.02–0.05 km2</td><td>√</td><td>~1–4 km2</td><td>√</td></tr><tr><td>Carbon emissions</td><td>Zero</td><td>√</td><td>~0.35–0.4 tCO2/MWh</td><td></td><td>Near zero</td><td>√</td></tr><tr><td>Fuel risk</td><td>none</td><td>√</td><td>gas - high fuel cost</td><td></td><td>uranium - low fuel cost</td><td>√</td></tr><tr><td>Bottleneck</td><td>location, grid connection</td><td></td><td>turbine supply, gas supply</td><td></td><td>long development</td><td></td></tr></table>

Assuming a build for 1GW of baseload power  
Source: Company data, Bernstein analysis

## SOLAR-PLUS-STORAGE PROVIDES BASELOAD POWER

The UAE's Masdar and EWEC project represents a step-change in solar-plus-storage system design. Rather than optimizing for peak shaving, it is engineered to deliver round-the-clock baseload power. By pairing 5.2 GW of solar with 19 GWh of storage, \~1 GW of continuous power output can be achieved to match stable power load of 1GW. This “abundance” is critical: excess midday generation is not curtailed but stored in the battery system (equivalent to \~19 hours of duration) and discharged through the evening and overnight. In effect, the project replaces curtailment with energy shifting, reshaping variable solar generation into a stable, near-continuous output profile.

EXHIBIT 4: By pairing 5.2 GW of solar with 19 GWh of storage, 1 GW of continuous power output can be achieved to match stable a power load of 1GW  
![](images/1f6874d0328f53d0f055f45f4d7df5793775d19865d89e118223cac414530413.jpg)

<details>
<summary>text_image</summary>

EWEC
Enagas Water & Electricity Co.
J20D
MASDAR
5 GW
19 GW Hrs
1 GW of
uninterrupted
power
</details>

Source: Company presentation

How does this work? With 5.2 GW of installed solar capacity, the project could generate approximately 12.45 TWh of annual solar output, implying a \~27% capacity factor based on the local irradiance profile. This equates to \~34 GWh per day of energy production vs. a constant 24 GWh/day load for 1 GW baseload, highlighting that the system is intentionally overbuilt by \~40% on an energy basis. Of this total generation, around 4.09 TWh is used to directly supply daytime demand, while \~4.62 TWh is stored in the battery during the day and discharged at nighttime to maintain continuous output. The remaining \~3.74 TWh represents surplus generation, which serves as headroom to meet storage losses, seasonal variability, and system reliability requirements. With this system, we estimate a 99.6% system reliability can be achieved.

EXHIBIT 5: Annual power output of the project (TWh). Solar and storage overbuilt enables continuous 1 GW output  
![](images/93a71d3e27a97e2b222951ec993cea66d135c06c85ed9f632ef2b0aa4501214b.jpg)

<details>
<summary>sankey diagram</summary>

| Category                  | Value |
| ------------------------- | ----- |
| Daytime supply            | 4.09  |
| Baseload served          | 8.71  |
| Battery charging          | 4.62  |
| Night discharge           | 4.62  |
| Reserve / curtailment / headroom | 3.74  |
</details>

Source: Company data, Bernstein analysis

We have carried out an analysis of what the operations and economics would look like for the project based on the region's irradiance profile and the system design. Building solar capacity in UAE offers significant advantages due to the region's abundant solar resources, characterized by high solar irradiance and vast available land, enabling large-scale, cost-effective solar power generation. Additionally, favorable government policy and expanding transmission infrastructure support export of electricity. B

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
