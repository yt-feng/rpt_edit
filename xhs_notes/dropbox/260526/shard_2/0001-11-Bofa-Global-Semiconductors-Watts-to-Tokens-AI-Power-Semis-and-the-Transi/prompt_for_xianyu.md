你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# Global Semiconductors

# Watts to Tokens: AI Power Semis and the Transition to 800V Data Centers

Industry Overview

# AI Power: transformative opportunity for analog semis

Power is becoming a critical constraint in AI scaling. We estimate rising compute density drives rack power capacity up 100x from 10-15kW in traditional cloud servers to 1.5MW for Nvidia's Feynman platform (CY29/30). Existing infrastructure cannot meet demand, requiring wholesale revamp of power delivery from grid to rack to GPU/XPU core. This creates a transformative opportunity for analog semi vendors to shift mix away from cyclical auto/industrial demand toward secular, durable AI markets, where diverse architectures, new components, novel materials (wide-bandgap semis), and products create an unparalleled chance to differentiate and take share. In this report, we build a bottoms-up AI analog semi industry model translating accelerator/rack demand into content pools across components (VRM, IBC, SST, etc.) and device types (Si, SiC, GaN, etc.) into supplier revenue share across low power (<200kW) and high power (600kW+) racks. We estimate \~233GWs deployed through CY30 expands today's \$7.9bn AI analog market to \$27bn by CY30 (28% CAGR) inside a \$1.7tn AI data center systems LT TAM.

# Data Centers: \$25bn TAM led by 100x jump in rack power

We estimate rack content grows \~25x from \$36K today to nearly \$300K per 600kW rack and approaching \$1mn in the MW-class era. The TAM from “rack-to-core” expands to \$25bn CY30 from \$7.6bn today (27% CAGR). Value shifts towards components closest to the accelerator including multi-phase voltage regulator modules (Infineon, TXN, ADI, Renesas) and intermediate bus converters (IBC; ON, Infineon,) but also optics (STMicro, ADI, TXN). As high-performance power density becomes critical in 800 VDC architecture, silicon carbide (SiC) and gallium nitride (GaN) are greenfield new markets.

# Power Infra: additional \$2bn TAM as microgrids inflect

Select strategic opportunities in power infrastructure grow to \$38.9K per MW during the 800 VDC evolution from \$12.4K per MW today. The “grid-to-data hall” TAM grows to \$1.8bn by CY30 from \~\$245mn today (49% CAGR). Legacy equipment makes way for emerging tech like solid-state transformers (SSTs) and solid-state circuit breakers (SSCB) as facilities transition to microgrids. SiC is a big materials winner but we see ample analog IC, MCU, and sensing content in a market where there was little before.

# Revenue opp led by analog ICs; discretes gain most share

Best positioned vendors are those with: (1) broadest portfolio spanning the power tree across multiple device types; (2) products that meet high voltage and elite reliability requirements (similar to auto/industrial semi products); (3) provide system-level design expertise and optimization from grid-to-core. TXN's leading power semi franchise gives it the highest share in the market. Infineon boasts the broadest AI portfolio across Si, SiC, and GaN and may gain the most share CY25-30 from grid-to-core. ADI enjoys the third biggest revenue opportunity and also gains share enhanced by the Empower acquisition. ON has high leverage to novel SiC and GaN tech boosting share of wallet.

# 25 May 2026

Equity

Global

Semiconductors

Vivek Arya

Research Analyst

BofAS

vivek.arya@bofa.com

Duksan Jang

Research Analyst

BofAS

duksan.jang@bofa.com

Michael Mani

Research Analyst

BofAS

michael.mani@bofa.com

Didier Scemama >>

Research Analyst

MLI (UK)

didier.scemama@bofa.com

Mikio Hirakawa >>

Research Analyst

BofAS Japan

mikio.hirakawa@bofa.com

# Contents

Power is the ultimate AI scaling constraint 3   
Compute roadmap: 1MW per rack by CY30 4   
GW model: AI needs 233GW through CY30 7   
How power is delivered today 8   
800 VDC: power delivery for the GW era 9   
Analog semis: key beneficiaries in high power 14   
Data center: \$25bn TAM from rack to core 18   
Power Supply Units (PSU) 19   
Intermediate Bus Conversion (IBC) 20   
Server Board (GPU/XPU power, CPU, VRM, multi-phase) 23   
Other components (protection, sensors, optics, etc.) 26   
Power Infra: \$2bn TAM from grid to hall 29   
Energy Storage System (ESS)/Uninterruptible Power Supply (UPS) 30   
Solid-State Transformer (SST) 31   
Solid-State Circuit Breakers (SSCB) 32   
AI Power Analog Semi Model 34   
Glossary 44

# Power is the ultimate AI scaling constraint

Multiple bottlenecks are emerging in the multi-year AI infrastructure buildout – memory, optics, leading-edge logic wafers, advanced substrates, etc. – but among the greatest constraints to scaling is arguably power.

# Higher compute density is translating to higher power demands

Traditional cloud data center operators mainly worried about compute space as power and cooling infrastructure occupied a significantly smaller physical footprint. When the AI investment cycle began, server CPUs transitioned to power hungry GPUs, ordinary internet traffic evolved into intense training and inference workloads, and heavy computational needs turned into heavy power needs. As demand surges and clusters become larger, the need for higher compute density per server rack (e.g. Hopper had only 8 GPUs in a node while Blackwell's scale-up domain is 72) to optimize performance means power per rack also goes up. Whereas a traditional cloud rack may consume 10-15 kilowatts (kW), Blackwell generation racks require 100-120kW, and future generations like Feynman may drive a staggering over 1 megawatt per rack (enough to power up to 1000 US homes) as up to 576 GPUs are packed into a single node (exhibit 1).

Exhibit 1: By the end of the decade, we think Nvidia's roadmap could lead to $>1.5$ megawatt racks for the Feynman era, nearly 100x higher than a standard server CPU rack at 10-15 kilowatts   
Power capacity per rack (kilowatts) across various generations of Nvidia platforms vs. a traditional server rack   
![](images/942e58ec5e7e5757faaf7435e90a56a57624a68ce13375f0b28656432340018e.jpg)

<details>
<summary>bar</summary>

| Category | Value (kW) |
| :--- | :--- |
| Traditional Server Rack | ~50 |
| H100 HGX (2022) | ~80 |
| Grace Blackwell NVL72 (2024) | ~150 |
| Grace Blackwell Ultra NVL 72 (2025) | ~160 |
| Vera Rubin NVL144 (2026) | ~190 |
| Vera Rubin Ultra NVL576 (2027) | ~720 |
| Rosa Feynman (2028+) | ~1550 |
~100x increase
</details>

Source: BofA Global Research estimates, Nvidia, company reports   
BofA GLOBAL RESEARCH

Performance-per-watt is a critical metric for operators as it determines the amount of tokens you can generate per unit of power, and thus, the amount of revenue. Data Centers operate inside a fixed power envelope which is heavily dependent on location, so maximizing access to power and converting it to tokens in an efficient manner is crucial.

# Bringing gigawatt-scale power online takes time

The gating factor in power stems having to build the entire physical infrastructure flow for a new data center from grid interconnects, substations, transformers, switchgear, cooling and more. It takes time to bring this capacity online. Key equipment is also constrained, including gas turbines (5-year delivery timeline) and transformers (2–3-year lead times) Sites that have secured grid power may be able to reach 1GW capacity in 1-4 years from construction but a greenfield project could take as long as 5 years, according to the International Energy Agency, before project delays.

# Compute roadmap: 1MW per rack by CY30

Hopper H100 HGX was Nvidia's first flagship anchor accelerator platform for the AI-era launched in 2022 and utilized Hopper GPUs where thermal design power (TDP) fetched only $0.7\mathrm{kW}$ per package while other functions like switches, CPUs, and NICs, represented a small part of the power budget all in an architecture that was air-cooled (exhibit 2).

As we moved into Blackwell (GB200 NVL72), total GPU power budget jumped +400% from 17kW to 86kW as GPU TDP increased and GPU die count multiplied to 144. Networking and CPUs became more relevant driving up power consumption and an entirely new liquid-cooled rack, Oberon, was required to handle the heat generation. Total power increased from 25kW per rack to 100-120kw per rack.

As the launch of Rubin gets underway, power climbs again albeit to a lesser extent, but Rubin Ultra in CY27 represents another inflection to over 600kW per rack (+240% platform-over-platform), with its significantly larger scale-up domain of up to 576 GPUs, higher TDPs in the 3kW range, 144 Vera CPUs equipped for agentic AI, and powerful NVSwitch 6 inside the next-generation Kyber rack form factor. This is when we would expect to see initial deployments of 800 VDC due to the power demands.

While we can only speculate on specifications as official details are sparse, these same trends should persist as we approach the Feynman era (likely launches CY29/30) where architectures begin to migrate to hybrid microgrids (more on this later) and compute TDP likely takes another step up again. The roadmap then enters the zone of 1MW class racks where the sheer amount of power density packed into the physical space of filing cabinets necessitates completely new infrastructure.

Exhibit 2: The main driver of higher rack power advancing towards 1MW per rack by CY30 (Feynman) is GPU where TDP (thermal design power) is approaching 5kW per package. Rising switching, NIC, CPU, and DPU power budgets are also factors.   
Detailed power budget estimates across various generations of Nvidia platforms 

<table><tr><td colspan="7">Nvidia</td></tr><tr><td>Compute Platform</td><td>Hopper (H100) H100 HGX Rack</td><td>GB200 (Blackwell B200) Grace Blackwell NVL72</td><td>GB300 (Blackwell Ultra/B300) Grace Blackwell Ultra NVL 72</td><td>Rubin (VR200) Vera Rubin NVL72</td><td>Rubin Ultra (VR300 Ultra) Vera Rubin Ultra NVL144</td><td>Feynman (RF200) Rosa Feynman NVL576</td></tr><tr><td>Rack Architecture</td><td>Air-Cooled</td><td>Oberon; Liquid-cooled</td><td>Oberon; Liquid-cooled</td><td>Oberon; Liquid-cooled</td><td>Kyber; Liquid-cooled</td><td>Hybrid microgrid</td></tr><tr><td>GPU</td><td>Hopper</td><td>Blackwell</td><td>Blackwell Ultra</td><td>Rubin</td><td>Rubin Ultra</td><td>Feynman</td></tr><tr><td>GPU Package Count</td><td>32</td><td>72</td><td>72</td><td>72</td><td>144</td><td>576</td></tr><tr><td>GPU Die Count per Package</td><td>1</td><td>2</td><td>2</td><td>2</td><td>4</td><td>2</td></tr><tr><td>Total Dies per Rack</td><td>32</td><td>144</td><td>144</td><td>144</td><td>576</td><td>1152</td></tr><tr><td>GPU Power per Package Consumption (kW)</td><td>0.7</td><td>1.2</td><td>1.4</td><td>1.8</td><td>3.6</td><td>1.8</td></tr><tr><td>GPU Power Budget (kW)</td><td>22.4</td><td>86.4</td><td>100.8</td><td>129.6</td><td>518.4</td><td>1036.8</td></tr><tr><td>CPU</td><td>Xeon/EPYC</td><td>Grace</td><td>Grace</td><td>Vera</td><td>Vera</td><td>Rosa</td></tr><tr><td>CPU Count</td><td>8</td><td>36</td><td>36</td><td>36</td><td>72</td><td>288</td></tr><tr><td>CPU Power Consumption (kW)</td><td>0.30</td><td>0.30</td><td>0.30</td><td>0.35</td><td>0.35</td><td>0.35</td></tr><tr><td>CPU Power Budget (kW)</td><td>2.4</td><td>10.8</td><td>10.8</td><td>12.6</td><td>25.2</td><td>100.8</td></tr><tr><td>NIC</td><td>CX-7</td><td>CX-7</td><td>CX-8</td><td>CX-9</td><td>CX-9</td><td>Next Gen CX</td></tr><tr><td>NIC Die Count</td><td>32</td><td>72</td><td>72</td><td>72</td><td>144</td><td>576</td></tr><tr><td>NIC Power Consumption (kw)</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.05</td></tr><tr><td>NIC Power Budget (kW)</td><td>0.8</td><td>1.8</td><td>2.2</td><td>2.2</td><td>4.3</td><td>28.8</td></tr><tr><td>NVLink Switch</td><td>NVSwitch3</td><td>NVSwitch5</td><td>NVSwitch5</td><td>NVSwitch6</td><td>NVSwitch7</td><td>Next Gen NVSwitch</td></tr><tr><td>Switch Die Count</td><td>12</td><td>18</td><td>18</td><td>18</td><td>36</td><td>144</td></tr><tr><td>Switch Power Consumption (kW)</td><td>0.3</td><td>0.8</td><td>0.8</td><td>1.1</td><td>2</td><td>2</td></tr><tr><td>Switch Power Budget (kW)</td><td>3.0</td><td>14.4</td><td>14.4</td><td>19.8</td><td>54.45</td><td>288</td></tr><tr><td>DPU</td><td>BlueField-3</td><td>BlueField-3</td><td>BlueField-3</td><td>BlueField-4</td><td>BlueField-4</td><td>Next Gen BlueField</td></tr><tr><td>DPU Die Count</td><td>3</td><td>18</td><td>18</td><td>18</td><td>36</td><td>144</td></tr><tr><td>DPU Power Consumption (kW)</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.2</td></tr><tr><td>DPU Power Budget (kW)</td><td>0.2</td><td>1.4</td><td>1.4</td><td>2.7</td><td>5.4</td><td>28.8</td></tr><tr><td>PSU Conversion Losses (kW)</td><td>0.7</td><td>3.5</td><td>3.9</td><td>5.7</td><td>22.8</td><td>31.4</td></tr><tr><td>Cooling (kW)</td><td>1.5</td><td>1.5</td><td>1.5</td><td>2</td><td>12</td><td>15</td></tr><tr><td>Other (kW)</td><td>0.5</td><td>1.0</td><td>1.0</td><td>2.0</td><td>3.0</td><td>5.0</td></tr><tr><td>Overhead Power Budget (kW)</td><td>2.7</td><td>6</td><td>6.4</td><td>9.7</td><td>37.8</td><td>51.4</td></tr><tr><td>Total Rack Power (kW)</td><td>32</td><td>121</td><td>136</td><td>177</td><td>646</td><td>1535</td></tr></table>

Source: BofA Global Research estimates, Nvidia

BofA GLOBAL RESEARCH

# Compute and networking contribute the most to rising power

As observed, when CPUs and GPUs improve, TDP typically increases 20% generation over generation thus leading to higher server power over time. As GPUs are networked together (via NVLink or another protocol for non-NVDA platforms) to upgrade performance by functioning as a synchronized node of compute, the use of copper interconnects for scale-up means that GPUs cannot be too far from each other (limited reach). Thus, limitation of tightly integrating GPUs on the same copper domain at limited distances creates a direct relationship between maximum power density and the ability to drive maximum performance as you need to pack as many GPUs possible into a smaller physical space in order to scale (Nvidia calls this the performance-density trap). Moving from Hopper to Blackwell led to a 75% increase in TDP but a 3.4x increase in rack power density which in turn translated to a 50x increase in performance. Every subsequent increase in the scale-up networking domain size is now translating into up to 2-4x increases in total power (exhibit 3).

Exhibit 3: Large inflections in power tend to coincide with architecture shifts like when Nvidia migrated to Oberon racks for Blackwell and eventually Kyber for Rubin Ultra. GPUs generally consume most power (65-75%) followed by Switches (10-13%)   
Nvidia power budget analysis spanning Hopper to Feynman 

<table><tr><td colspan="7">Power Budget Analysis (kW)</td></tr><tr><td>Compute Platform</td><td>Hopper (H200) H100 HGX</td><td>GB200 (Blackwell B200) Grace Blackwell NVL72</td><td>GB300 (Blackwell Ultra/B300) Grace Blackwell Ultra NVL 72</td><td>Rubin (VR200) Vera Rubin NVL144</td><td>Rubin Ultra (VR300 Ultra) Vera Rubin Ultra NVL576</td><td>Feynman (RF200) Rosa Feynman</td></tr><tr><td>GPU</td><td>22.4</td><td>86.4</td><td>100.8</td><td>129.6</td><td>518.4</td><td>1036.8</td></tr><tr><td>CPU</td><td>2.4</td><td>10.8</td><td>10.8</td><td>12.6</td><td>25.2</td><td>100.8</td></tr><tr><td>NIC</td><td>0.8</td><td>1.8</td><td>2.2</td><td>2.2</td><td>4.3</td><td>28.8</td></tr><tr><td>Switch</td><td>3.0</td><td>14.4</td><td>14.4</td><td>19.8</td><td>54.5</td><td>288.0</td></tr><tr><td>DPU</td><td>0.2</td><td>1.4</td><td>1.4</td><td>2.7</td><td>5.4</td><td>28.8</td></tr><tr><td>Overhead</td><td>2.7</td><td>6.0</td><td>6.4</td><td>9.7</td><td>37.8</td><td>51.4</td></tr><tr><td>Total Rack Power</td><td>32</td><td>121</td><td>136</td><td>177</td><td>646</td><td>1535</td></tr><tr><td colspan="7">Power Budget Analysis (% budget mix)</td></tr><tr><td>GPU<

[中间内容因长度限制已省略]

lect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
