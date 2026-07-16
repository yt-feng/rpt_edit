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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## China Power Infrastructure

## Solid State Transformers – Expert Call Takeaways

We hosted an expert call yesterday on the development of solid state transformers (SST) and high-voltage direct current (HVDC) with the following takeaways: the expert views SST as a potentially important long-term upgrade path for data center (DC) power architecture, given benefits in efficiency, footprint and intelligent/bidirectional power dispatch, but believes commercialization remains early due to immature standards, limited reliability validation, 'good-enough' HVDC alternatives, and a lack of proven use cases. He believes near-term adoption will be more likely centered on EV charging, high-energy industrial, renewables+storage, and microgrids, with a broad DC rollout unlikely before 2028. On the value proposition, SSTs can lift end-to-end efficiency by $5+$ percentage points vs a line-frequency transformer plus uninterruptible power supply (UPS) chain (typically $<90\%$ ) and reduce power equipment volume to $\sim 1/5 - 1/10$ , while enabling software-defined power management and power-compute coordination. The expert characterized 800V HVDC as an interim architecture that keeps the front-end line-frequency transformer but moves downstream distribution to 800V DC, with UPS, HVDC and SST approaches likely to coexist for 5-10 years, depending on chip power density and DC efficiency targets. Commercial traction is still limited: one electrical equipment company cited $\sim 100 - 200$ North America units, and China XD has four units of overseas orders, but broader DC-scale orders remain scarce. See Table 1 for valuation comps of companies with SST exposure, and Figure 1 for the illustrative diagram.

\- SST outlook: benefits and adoption timing: The expert believes SST offer advantages (energy efficiency, smaller footprint, smarter and bidirectional energy dispatch) and could become a key upgrade path for DC power architectures long term, but commercialization is still early due to immature standards, limited reliability validation, ‘good-enough’ HVDC alternatives, and scarce proven use cases. He believes near-term adoption is more likely in EV charging, high-energy industrial, renewables+storage and microgrids, with large-scale DC rollout unlikely before 2028.

\- SST value proposition vs line-frequency transformers: The expert noted SSTs offer clear advantages over traditional line-frequency transformers in efficiency, footprint and energy dispatch, making them attractive for next-generation AI DC and integrated energy systems. 1) A conventional supply chain built around a line-frequency transformer plus UPS typically delivers less than $90\%$ end-to-end efficiency, while an SST-based approach can lift total system efficiency by more than 5 percentage points, reducing losses, heat and operating costs. 2) In AIDC facilities where transformers and power distribution equipment are taking up more space, SST solutions can cut equipment volume to roughly one-fifth to one-tenth of traditional setups, releasing valuable floor area and supporting higher power density. 3) Unlike traditional transformers that mainly provide one-way power output with limited controllability, SSTs enable software-defined power management and coordination between power supply and computing loads, aligning with smarter DC designs. 4) SSTs can act as an energy router with bidirectional power flow, supporting multi-energy complementarity across wind, solar and storage, while traditional transformers are largely one-directional converters.

Power Equipment and Utilities

Stephen Tsui, CFA AC (852) 2800-8592 stephen.tsui@JPM.com

Vento Suen  
(852) 2800-8546  
vento.suen@JPM.com

Alan Hon  
(852) 2800-8573  
alan.hon@JPM.com  
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 4 for analyst certification and important disclosures, including non-US analyst disclosures.

\- 800V HVDC architecture: interim approach and evolution path: The expert believes that the 800V HVDC architecture is best viewed as a transitional pathway. It typically retains the conventional line-frequency transformer on the front end, while shifting the downstream distribution to 800V DC to improve overall system efficiency by reducing conversion losses and current-related inefficiencies. Looking ahead, if SST mature, they could replace the traditional transformer entirely and deliver 800V DC directly, enabling a more efficient end-to-end power conversion chain. Over the next five to ten years, traditional UPS-based architecture, 800V HVDC solutions, and SST-based approaches are expected to coexist. Which design ultimately prevails will depend on the trajectory of chip power consumption and rack power density, as well as each data center's efficiency targets and tolerance for adopting newer power technologies.

\- Commercial traction: early signs and current limitations: The expert believes that SST commercialization remains at an early stage. An electrical equipment company has indicated it has secured roughly 100-200 units of orders in North America, which is a notable proof point, while China XD has won four units of overseas orders. Apart from these, there is still limited evidence of clear, sizable commercial orders specifically for data center deployments. More than 20 companies in China have already announced SST products, and over 30 more are in pre-release, yet most remain in development and lack true mass-production capability. Overseas players such as Eaton (ETN US, NR) have also announced products, but the expert hasn't seen widely referenced commercialization cases. Overall, meaningful large-scale SST adoption is more likely after 2028, when the market may enter a small-batch, scaled commercial phase; until then, deployments are expected to focus on pilots, niche scenarios, and operational learning.

\- Commercialization constraints: standards, validation, and economics: The expert believes that SST commercialization is constrained by four main factors. First, there is a lack of finalized specifications and standards, and the broader data center supply chain still lacks unified product standards, which delays both vendor roadmaps and owner investment decisions. Second, reliability validation remains insufficient: data centers require extremely high power availability, but operating data and long-duration field proof for SSTs are still limited, making owners reluctant to approve large-scale deployments. Third, today's 800V HVDC solutions are ‘good enough’ for current needs, meaning that SSTs can be seen as over-engineered in some use cases and therefore harder to justify economically or operationally. Fourth, rising silicon carbide device prices are putting upward pressure on system costs; however, cost is not viewed as the primary blocker. The more fundamental issue is the limited willingness among owners to pilot SSTs at scale, given uncertain standards, incomplete reliability evidence, and an unclear set of near-term applications where SSTs deliver uniquely compelling benefits.

\- Vendor landscape: positioning and key differentiators: Among SST vendors, the expert believes that Delta Electronics (2308 TT, covered by Albert Hung, OW) is generally viewed as a first-tier player, having started R&D earliest and achieved the strongest industry recognition, with its key edge coming from early deployments and accumulated operating data. Some other Chinese players may also stand out, including Sungrow (see note for Sungrow's launch of SST products by our China renewable analyst). Sifang Automation (601126 CH, NC) has a utility-grid background and practical experience in PV-storage-DC architectures, with relatively advanced industrialization, and is exploring cooperation with a leading US DC electrical equipment supplier, aiming to leverage the partner's North American channel presence while it works toward the necessary certifications, according to the expert. Overall, domestic vendors are not clearly disadvantaged on the hardware front; the larger gap is access to real deployments and operating data, where Delta leads.

415 VAC Distribution - Today  
Table 1: Companies with SST exposure

<table><tr><td rowspan="2"></td><td rowspan="2">Ticker</td><td rowspan="2">JPM rating</td><td rowspan="2">Share price (LC)</td><td rowspan="2">Mkt Cap (USDm)</td><td rowspan="2">Daily liquidity (USDm)</td><td colspan="2">PE (x)</td><td colspan="2">P/BV (x)</td><td colspan="2">ROE (%)</td><td colspan="2">EV/EBITDA (x)</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="14">Mainland China</td></tr><tr><td>Qingdao TGOOD</td><td>300001 CH</td><td>OW</td><td>30.5</td><td>4,747</td><td>197.9</td><td>20.8</td><td>17.0</td><td>3.3</td><td>2.8</td><td>16.8</td><td>17.8</td><td>14.2</td><td>12.3</td></tr><tr><td>Sungrow</td><td>300274 CH</td><td>OW</td><td>101.5</td><td>31,026</td><td>1,711.7</td><td>13.8</td><td>11.4</td><td>3.5</td><td>2.8</td><td>26.7</td><td>25.6</td><td>10.9</td><td>9.1</td></tr><tr><td>China XD</td><td>601179 CH</td><td>NC</td><td>12.1</td><td>9,129</td><td>472.1</td><td>39.7</td><td>32.3</td><td>2.5</td><td>2.4</td><td>6.5</td><td>7.6</td><td>21.0</td><td>18.1</td></tr><tr><td>Sifang Automation</td><td>601126 CH</td><td>NC</td><td>49.8</td><td>6,113</td><td>323.6</td><td>42.2</td><td>36.0</td><td>7.7</td><td>7.0</td><td>18.7</td><td>20.0</td><td>32.7</td><td>27.7</td></tr><tr><td>Sinexcel Electric</td><td>300693 CH</td><td>NC</td><td>36.9</td><td>1,704</td><td>143.8</td><td>19.3</td><td>15.5</td><td>4.3</td><td>3.5</td><td>24.4</td><td>24.8</td><td>15.5</td><td>12.4</td></tr><tr><td>Eaglerise Electric</td><td>002922 CH</td><td>NC</td><td>25.9</td><td>1,615</td><td>148.5</td><td>22.9</td><td>15.1</td><td>2.6</td><td>2.4</td><td>11.9</td><td>16.4</td><td>14.5</td><td>10.8</td></tr><tr><td colspan="14">Korea</td></tr><tr><td>LS Electric</td><td>010120 KS</td><td>N</td><td>176,800</td><td>17,856</td><td>474.3</td><td>52.2</td><td>37.6</td><td>10.6</td><td>8.7</td><td>22.2</td><td>25.4</td><td>31.1</td><td>23.0</td></tr><tr><td>Hyosung Heavy</td><td>298040 KS</td><td>OW</td><td>2,522,000</td><td>15,815</td><td>220.6</td><td>29.6</td><td>20.7</td><td>7.6</td><td>5.7</td><td>29.2</td><td>31.6</td><td>21.1</td><td>15.0</td></tr><tr><td colspan="14">Others</td></tr><tr><td>GE Vernova</td><td>GEV US</td><td>OW</td><td>1,042.6</td><td>280,167</td><td>2,893.7</td><td>31.3</td><td>38.2</td><td>16.4</td><td>12.0</td><td>39.8</td><td>36.1</td><td>43.2</td><td>26.8</td></tr><tr><td>ABB</td><td>ABBN SW</td><td>N</td><td>83.8</td><td>187,851</td><td>241.0</td><td>33.2</td><td>32.2</td><td>11.0</td><td>9.2</td><td>33.8</td><td>31.0</td><td>21.7</td><td>21.0</td></tr><tr><td>Schneider Electric</td><td>SU FP</td><td>OW</td><td>268.6</td><td>176,607</td><td>297.1</td><td>25.1</td><td>21.6</td><td>5.6</td><td>5.0</td><td>24.0</td><td>25.0</td><td>17.0</td><td>14.8</td></tr><tr><td>Eaton</td><td>ETN US</td><td>NR</td><td>402.9</td><td>156,427</td><td>1,045.5</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Delta Electronics</td><td>2308 TT</td><td>OW</td><td>1,800.0</td><td>145,209</td><td>833.8</td><td>40.3</td><td>26.5</td><td>12.8</td><td>9.8</td><td>31.8</td><td>36.9</td><td>25.2</td><td>17.1</td></tr><tr><td>Vertiv</td><td>VRT US</td><td>NR</td><td>305.9</td><td>117,487</td><td>1,979.3</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Enphase Energy</td><td>ENPH US</td><td>N</td><td>43.1</td><td>5,675</td><td>381.1</td><td>22.5</td><td>20.4</td><td>4.3</td><td>3.5</td><td>20.9</td><td>18.9</td><td>16.7</td><td>15.5</td></tr><tr><td>SolarEdge</td><td>SEDG US</td><td>N</td><td>52.1</td><td>3,170</td><td>197.1</td><td>179.8</td><td>23.4</td><td>5.7</td><td>3.9</td><td>3.6</td><td>20.1</td><td>45.5</td><td>15.8</td></tr></table>

Source: Bloomberg Finance L.P. (consensus estimates for not covered [NC] names), JPM estimates. Priced as of 14 Jul 2026.

Figure 1: Datacenter architecture over time  
![](images/3243cd590cf1165e5a23b76c3140cdf25dbed494215410ef1a036568c5be097f.jpg)  
Source: NVIDIA.

Companies Discussed in This Report (all prices in this report as of market close on 14 July 2026, unless otherwise indicated) Delta Electronics, Inc.(2308.TW/NT\$1,855.00/OW), Sungrow - A(300274.SZ/Rmb108.00[13 July 2026]/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Delta Electronics, Inc., Sungrow - A or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Delta Electronics, Inc., Sungrow - A or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Delta Electronics, Inc. or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Delta Electronics, Inc. or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Delta Electronics, Inc., Sungrow - A or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Delta Electronics, Inc. or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Delta Electronics, Inc., Sungrow - A or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should con

[中间内容因长度限制已省略]

ent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Completed 14 Jul 2026 03:03 PM HKT
"""
