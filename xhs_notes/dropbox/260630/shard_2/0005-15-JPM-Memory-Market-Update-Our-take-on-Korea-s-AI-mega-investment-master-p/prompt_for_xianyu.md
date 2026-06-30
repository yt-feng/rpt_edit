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
## Memory Market Update

## Our take on Korea's AI mega-investment master plan and recent memory industry developments

\- Entering the Mega Investment Era. The Korean government (Presidential office and multiple cabinet members) and major AI ecosystem C-level executives (incl. Samsung/SK group chairmen) attended a national briefing today and shared the long-term AI mega project vision. The Ministry of Trade, Industry and Resources (“MOTIR”) announced the “Three Mega Project Plans” establishing 1) semiconductors; 2) AI robotics and physical AI; and 3) AI datacenters as the three major growth pillars (link). The genesis of the investment stems from retaining the current AI leadership (especially in AI semiconductors) and leapfrogging as an AI export country through nurturing and developing various AI-derivative businesses including robotics and AI datacenters. Within the semiconductor business, MOTIR highlighted 3S (Speed + Stronghold + Spearhead) + 1F (Full Support) as growth strategies: 1) Speed: MOTIR expects memory capacity to double in the next five years and pull-forward the advanced Yongyin fab ramp timeline by 7-12 years (From 2045-2047 to 2033-2040); 2) Stronghold: W800T investment in the Southeast region (four fabs in total) and W81T HBM backend fab investment in the Chungcheong region; 3) Spearhead: W30T investment over the next 15 years in R&D and labor to support the pathway from R&D to full production; and lastly 4) Full Support from the government backed by MOTIR. Other investments include fostering Robotics as the next growth engine and W550T investment in AI DC split between two phases (1st phase: 8.4GW and 2nd phase: W10GW investment by 2035).

\- Samsung Group: W2,655T investment of which W2,100T in semiconductors. Samsung Group announced a W2,655T investment in Korea (link) and SEC announced a W2,450T investment throughout 2026-2040 (W2,100T investment in semiconductors) (link). Combining the two investment announcements, SEC is expected to invest: 1) W1,650T in Yong-in fab cluster and existing semiconductor fabs; 2) W400T in Gwangju potentially as a new manufacturing hub; 3) W56T in HBM backend packaging line in Cheonan/Onyang; 4) W67T in next-gen display and micro display in Asan; and 5) <W60trn in physical AI and humanoid mass production line in Gumi. Within the Samsung group, other investment includes: SEMCO (Substrate packaging fab in Sejong and MLCC/substrate fab in Busan); Samsung SDS (AI DC buildout in Haenam and Gumi); Samsung C&T (Green energy, power facility, etc. in Honam) and Samsung SDI (Battery factory in Ulsan/Cheonan).

\- SK Group: W2,100T investment (W1,100T in memory and W1,000T in AI infrastructure). SK Group explained the role of the datacenter is transitioning from storage to token generation and emphasized AI factory as the next growth engine of the group (link). The SK Group announced to invest W1,000T in AI infrastructure equating to 15GW by 2035 split between two phases (1st phase of 5GW ramp split between a mix of 0.5GW/1GW projects and an additional 10GW ramp by 2035). SK Group also announced that it will invest W1,100T in memory split between W600T in Yongin (pulling forward the ramp time from 2045 to 2033), W100T in NAND in Cheongju, and W400T for the next semiconductor cluster, potentially in the Southeast region.

See page 5 for analyst certification and important disclosures, including non-US analyst disclosures.

Technology - Semiconductors

Jay Kwon AC
(82-2) 758-5725
jay.h.kwon@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

JPM Securities (Far East) Limited, Seoul Branch

Neelay Y Kamath
(91-22) 6157 3764
neelay.kamath@jpmchase.com
JPM India Private Limited

\- JPM view: W4,755T (or US\$3.1T) includes more than a dozen of\~400k WSPM fab investments on a scale which is 2x that of the current installed DRAM WSPM capacity, implying the pace of building 1mn additional DRAM capacity (from 1H16-1H26) will be multiple times faster than in the past after the tipping point in late-2020s. Within the US\$3.1T long-term investment plan, we estimate 60-70% to be allocated to front-end wafer equipment spending, 20-30% for infrastructure and cleanroom construction, and the rest for back-end packaging facilities. We expect to hear more details on specific timelines for investment (fab and investment plan in multiple stages and timeline) in the upcoming result season and follow-up corporate events.

Table 1: Investment details by company/group

<table><tr><td>Related companies</td><td>Location</td><td>Investment amount</td><td>Category</td><td>Investment details</td></tr><tr><td rowspan="4">SEC</td><td>Yongin</td><td>W1,650T</td><td>Semiconductor</td><td>expected completion of Yongin semiconductor cluster by 2040, advancing by 7 years</td></tr><tr><td>Gwangju</td><td>W400T</td><td>Semiconductor</td><td>construction of a new semiconductor fab and creation of innovation hub based on digital twin technology</td></tr><tr><td>Cheonan /Onyang</td><td>W56T</td><td>HBM / advanced packaging</td><td>HBM fab investment, focusing on HBM capacity and backend packaging capabilities</td></tr><tr><td>Gumi</td><td>&lt; W60T</td><td>Humanoids / robotics</td><td>construction of innovation hub with mass-production lines for physical AI and humanoid robots</td></tr><tr><td>SEMCO</td><td>Busan/Sejong</td><td rowspan="6">&lt; W625T</td><td>ABF substrate/packaging</td><td>investments in advanced package substrate line for AI servers</td></tr><tr><td>Samsung SDS</td><td>Haenam/Gumi</td><td>AI data center</td><td>AIDC construction to serve as the govt. headquarter for public AI transformation</td></tr><tr><td>Samsung SDI</td><td>Ulsan/Cheonan</td><td>Battery/energy storage</td><td>increasing investment in next-generation solid=state batteries and batteries for BESS</td></tr><tr><td>Samsung Engineering</td><td>Geoje</td><td>Shipbuilding</td><td>investment in shipbuilding base for high-value-added vessels</td></tr><tr><td>Samsung C&amp;T</td><td>Southwest region</td><td>Solar energy</td><td>investment for building solar energy construction / nuclear energy-based hydrogen production facilities</td></tr><tr><td>Samsung Display</td><td>Asan</td><td>Display</td><td>construction of production base for ultra-high resolution micro displays - used for foldable smartphones</td></tr><tr><td rowspan="5">SK Group</td><td>Ulsan</td><td rowspan="2">W1,100T</td><td rowspan="2">AI infrastructure/data center</td><td>1st phase: 5GW built in regions where SK has secured power and land</td></tr><tr><td>TBD</td><td>2nd phase: additional 10GW by 2035, with AIDC functioning as token factories</td></tr><tr><td>Yongin</td><td>W600T</td><td>Semiconductor</td><td>construction of fourth fab by 2033, ramping by 12 years</td></tr><tr><td>Cheongju</td><td>W100T</td><td>Semiconductor (NAND)</td><td>expansion of its NAND flash production line</td></tr><tr><td>TBD, likely Southwest</td><td>W400T</td><td>Semiconductor</td><td>capital allocation for the fab sit sourcing, fosucing on sufficient land, utility resources, electricity, labor</td></tr></table>

Source: MOTIR, SK Group, Samsung Group

\- How should we interpret the US\$3T investment plan? Investment plan timeline is far out (through 2040E/2033E each by Samsung/SK group) and we believe the actual capacity buildout execution is largely subjective to industry S-D by the nature of the memory industry cycle. Nevertheless, the magnitude and commitment shown by the two conglomerates and the Korean government underpin their ultra long-term vision and growth strategy. Two key words that stood out to us were shortage and competition. Memory industry senior executives mentioned multiple times officially that supply sufficiency is only half relative to the demand and foresees it worsening in coming years. That said, the two chairmen's commentary sounded like a decisive message to debottleneck the supply shortage to fulfill customer demand and avoid potential demand disruption, which is the centerpiece of current market debate on memory (i.e. Memory value share in AI capex race is too high). We also read it as a Korean Memory Inc's determined message to maintain the market leadership amidst growing competition. Underlying AI computation-related memory demand remains substantial and we have identified a more than multi-year up-cycle view from the chairmen's message. This should be a long-term positive for SPE, Power Infrastructure, and Semi EPC (Engineering, Procurement, and Construction) suppliers. We like SK Inc and Samsung C&T from a Semi ECP operation standpoint. Depending on the stage of the cycle, capex acceleration can be interpreted as either positive (early to mid-cycle) or negative (mid-peak cycle). While today's market reaction was negative for Korean memory makers, we believe mid-to-long term shares are risk-reward favorable as a US\$3T investment could eventually return accumulated US\$12-20trn (using 15%-25% capital intensity) revenue opportunity (vs. Korean memory makers' accumulated revenue in the last 20 years; 2006-2025; at US\$1.2trn).

\- Apple-MU dispute highlights where memory sentiment is at right now: the market views the skewed profit sharing as a risk. Recent reports (link) featuring the dispute between Apple (OW, covered by Samik Chaterjee) and MU (OW, covered by Harlan Sur) regarding unprecedented price rises in a short amount of time highlight the precarious memory related sentiment engulfing the world right now. Suppliers argue that customers were unfair with prices during a downcycle while customers argue that suppliers reigned in supply on purpose to squeeze out higher profit margins. We believe that this skewed profit sharing agreement, currently in favor of the memory makers, is being viewed by the market as unsustainable in nature. We believe that given the rising BOM impact of souring memory prices, Consumer Electronics brands will have greater challenges in procuring the required memory going forward. Despite the Chinese DRAM memory maker's intent to do major capex, we believe the additional supply falls well short of demand due to the S/D imbalance. Therefore, even if U.S. consumer electronics brands seek to source memory chips from Chinese suppliers, it is uncertain if they will be able to source enough volume. We expect AI and server compute centric memory demand bipolarization trend to continue in 2H26E-2027E, which is likely to result in favorable pricing trend for LPDDR memory.

Figure 1: DRAM bit demand vs bit supply  
![](images/75ccc2bc1a26e3ce2852b9f033c1f8c9e959aceef5c4100373d4838b8c3544ce.jpg)  
Source: OMDIA, Company data, JPM estimates.

Figure 2: NAND bit demand vs bit supply  
![](images/ac0eae6e3e0c3fb9652d201115549437e2a53ce8d3e836098680279aae240f78.jpg)  
Source: OMDIA, Company data, JPM estimates.

Figure 3: DRAM bit demand vs bit consumption vs bit supply in absolute terms  
![](images/3162a3487fc2f235e23c872ef746e65cfe2b7d888913b9872d7caf599d45b479.jpg)  
Source: OMDIA, Company data, JPM estimates.

Figure 4: NAND bit demand vs bit consumption vs bit supply in absolute terms  
![](images/ca66e7e0dfe45e46b10aa226d61b3120af1a2f03a271f1b04646ad4eb8f51180.jpg)  
Source: OMDIA, Company data, JPM estimates.

\- A class-action lawsuit has been filed against memory suppliers over potential allegations of collusion and price-fixing. In response to historically high memory prices, consumers have filed a private class-action lawsuit in the US (link) against the three big DRAM manufacturers, arguing that these companies gouged prices by artificially creating shortages in the industry. We would like to highlight that while this is a recurring pattern due to the memory market's oligopoly market structure, the class action is at the consumer level with government investigation not involved at the moment. However, given the unprecedented price rises and given memory's rising importance as a strategic asset, we would closely monitor the situation for a potential update. Looking back at history, the early-2000s DRAM cartel is the strongest precedent, as it produced admissions of guilt, not just allegations, with major manufacturers paying millions in criminal fines and executives serving jail time. This was followed by a consumer civil settlement in 2006 to compensate consumers who overpaid for DRAM products. We would also like to highlight the 2016-17 supply restriction claim which structurally resembles the present lawsuit, however, that civil case never produced any findings of guilt the way the early 2000s criminal case did.

Figure 5: Global memory makers' share price performance including SOX (Philadelphia Semiconductor index) %  
![](images/27463c6d1d54b0a9d458ef270eb43d80571784e68956978b6b6793087b7313ad.jpg)  
Source: Bloomberg Finance L.P. Note: Past performance is not an indicator of future results.

Companies Discussed in This Report (all prices in this report as of market close on 29 June 2026, unless otherwise indicated) SK Inc(034730.KS/W799,000/OW), Samsung C&T(028260.KS/W478,500/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

• Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Samsung C&T, SK Inc or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Samsung C&T, SK Inc or related entities.

\- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: SK Inc or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Samsung C&T, SK Inc or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Samsung C&T, SK Inc or related entities.

\- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from SK Inc or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Samsung C&T, SK Inc or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than 

[中间内容因长度限制已省略]

representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is
"""
