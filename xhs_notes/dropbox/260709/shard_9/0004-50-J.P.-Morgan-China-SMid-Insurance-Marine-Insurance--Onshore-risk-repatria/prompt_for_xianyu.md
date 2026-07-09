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
## China SMid Insurance

## Marine Insurance: Onshore risk repatriation creates medium-term upside for China Re and China Taiping

China's seaborne trade has expanded rapidly over recent decades, alongside the build-out of domestic merchant fleet capacity, driving robust demand for marine insurance. More recently, regulators have introduced a suite of supportive policies and positioned Shanghai as a marine insurance hub, with the aim of strengthening China's independent domestic risk governance capabilities. The full marine insurance value chain, including underwriting capacity, reinsurance support, specialized clauses and cross-border dispute settlement, has long been dominated by London and other developed markets (For details, see Asia Insurance: Summer Series: China's marine insurance: Strategic repatriation of maritime risk). China Re is a key medium-term beneficiary, in our view, and is well positioned to capture upside from state-led initiatives focused on onshore risk repatriation. Compared with major peers, the stock offers a compelling risk-reward profile, trading at a 4x FY26E P/E with an $8\%$ dividend yield, vs peers at $3 - 6\%$ . China Taiping also has relevant P&C and reinsurance exposure that may benefit from policy catalysts, alongside expectations of strong life sales momentum in 1H26.

\- China's marine insurance development and current issues. Marine insurance is a critical financial pillar for China's shipping and cross-border trade ecosystem. China has developed into a leading global maritime power, ranking at or near the top globally in shipbuilding output, cross-border cargo volumes and merchant fleet tonnage. However, China has historically relied on overseas reinsurers and insurers for marine insurance products, arbitration and claims services, creating potential supply chain security risks. Rising demand from green shipping, offshore wind transportation and Belt & Road maritime infrastructure further highlights the need for independent domestic underwriting capacity. In addition, the long-standing dominance of overseas markets has resulted in persistent premium outflows, accelerating policy-driven development of domestic marine insurance and reinsurance capabilities.

\- Policy support. China's marine insurance industry is shifting from volume expansion towards higher-value, specialized risk services. In response, authorities are optimizing marine legal frameworks, digitizing claims settlement procedures and upgrading underwriting standards. The revised Maritime Code, effective May 2026, together with Shanghai's marine insurance guidance issued in October 2024, reinforces the city's role as a national pilot zone for maritime risk aggregation, allocation and governance. These developments should help reduce structural reliance on overseas risk transfer over time.

\- Stock positioning. High technical underwriting barriers should sustain a concentrated market structure, which is favorable for China Re. As China's only national comprehensive reinsurance group, China Re leads the National Vessel Insurance Consortium and the Maritime Silk Road Consortium. We therefore expect leading domestic P&C insurers to retain more onshore marine risks while ceding more complex exposures to China Re, supporting steady and visible medium-term earnings growth. Alternatively, China Taiping also offers upside exposure to the domestic risk repatriation theme among insurers and manufacturers, given its long operating history as both a key non-life insurer and reinsurer (China Re/Taiping Re S&P credit rating: A(Stable)/A(Stable)).

## Insurance

Dan Wang AC  
(86-21) 6106-6349  
dan.wang@JPM.com  
SAC Registration Number: S1730524080001  
JPM Securities (China) Company Limited

(852) 2800-8517
mw.kim@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

Julia Kim
(852) 2800-8540
julia.c.kim@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

## Recent publications:

Asia Insurance: Summer Series: China's humanoid robots open a new frontier for P&C growth, 22 June 2026

China SMid Insurance: China Taiping: Niche robot insurance as a SMid-cap catalyst, 22 June 2026.

Table 1: China policy support for Marine Insurance

<table><tr><td>Policy Category</td><td>Policy Name</td><td>Issuing Authority</td><td>Date</td><td>Core Policy Content</td></tr><tr><td>Hainan Free Trade Port Marine Insurance Policies</td><td>Provisions on Promoting Cross-border Financial Development in Hainan FTP (Draft for Comments)</td><td>Hainan Provincial Financial Affairs Office</td><td>Jun-26</td><td>1. Promote RMB pricing and settlement in insurance; 2. Attract domestic/foreign insurers to set up a presence in Hainan; 3. Focus on vessel and cargo marine insurance; 4. Integrate shipping finance leasing with insurance innovation</td></tr><tr><td>Belt and Road Initiatives (BRI) Marine Insurance Policies</td><td>Joint Notice on Promoting “Maritime Credit + Shipping Insurance”</td><td>Ministry of Transport &amp; National Administration of Financial Regulation</td><td>Jun-26</td><td>1. Link maritime credit records with insurance pricing; 2. Simplify vessel insurance procedures; 3. Promote electronic policies and data interoperability; 4. Shift insurance focus from post-loss indemnity to pre-risk control</td></tr><tr><td>Hainan Free Trade Port Marine Insurance Policies</td><td>Opinions on Piloting High-Standard Institutional Opening-up in Financial Sector</td><td>PBOC, MOFCOM, NAFR, CSRC, SAFE</td><td>Jan-25</td><td>1. Shanghai and Hainan pilot financial opening-up reforms; 2. Foreign financial institutions receive national treatment; 3. Facilitate cross-border insurance services and capital flows; 4. Promote compliant cross-border financial data flows</td></tr><tr><td>Belt and Road Initiatives (BRI) Marine Insurance Policies</td><td>Action Plan for Strengthening Regulation, Preventing Risks and Boosting High-Quality Development of Property Insurance</td><td>National Administration of Financial Regulation (NAFR)</td><td>Dec-24</td><td>1. Accelerate shipping insurance development and expand underwriting capacity; 2. Strengthen export credit insurance for Chinese outbound investment; 3. Upgrade the BRI reinsurance consortium; 4. Explore insurance-investment integrated risk management models</td></tr><tr><td>Shanghai Free Trade Zone Marine Insurance Policies</td><td>Guiding Opinions on High-Quality Development of Shanghai Shipping Insurance Industry</td><td>National Administration of Financial Regulation (NAFR)</td><td>Oct-24</td><td>1. Enrich shipping insurance product offerings; 2. Consolidate domestic reinsurance underwriting capacity; 3. Improve global shipping insurance service standards; 4. Build a world-class shipping insurance center</td></tr></table>

Source: China regulatory authority including NAFR, PBOC, CSRC, SAFE etc.,

Table 2: Policy summary for promoting Shanghai's high-quality development of Marine Insurance

<table><tr><td>Policy Name</td><td>Date</td><td>Issuing Authority</td><td>Key Content</td></tr><tr><td>关于印发修订后的《中国(上海)自由 贸易试验区临港新片区支持国际再保 险功能区建设的若干措施》的通知</td><td></td><td></td><td rowspan="2">支持再保险机构和人才享受重点产业政策。对经国家金融监管部门批准并入 驻功能区的保险公司、再保险公司、保险经纪公司等相关机构及其金融人才, 给予落户奖励、增资奖励和人才奖励 Support insurance and reinsurance institutions settled in Lingang to enjoy key industrial policies. For insurance companies, reinsurance companies, marine insurance brokers and other relevant institutions and their financial talent that settle in Lingang Special Area, settlement subsidies, operation incentives and talent allowances will be provided.</td></tr><tr><td>Revised Measures to Support the Development of the International Reinsurance Function Zone within the Lingang New Area of China (Shanghai) Pilot Free Trade Zone (Circular)</td><td>Aug-24</td><td>上海市人民政府Shanghai Municipal People&#x27;s Government</td></tr><tr><td>提升上海航运服务业能级助力国际航 运中心建设行动方案 Action Plan to Upgrade Shanghai&#x27;s Shipping Service Capacity and Boost the Construction of the International Shipping Center</td><td>Jun-23</td><td>上海市人民政府Shanghai Municipal People&#x27;s Government</td><td>推动航运保险产品创新,探索研究对新能源船舶险、船舶建造险等重点险种的支持政策。Launch support policies covering shipping insurance products, and explore supportive policies targeting new energy-powered vessels and ship construction insurance.</td></tr><tr><td>提升上海航运服务业能级助力国际航 运中心建设行动方案 Action Plan to Upgrade Shanghai&#x27;s Shipping Service Capacity and Boost the Construction of the International Shipping Center</td><td>Jun-23</td><td>上海市人民政府Shanghai Municipal People&#x27;s Government</td><td>鼓励各类市场主体在民商事合同中选择上海作为争议解决地。支持境外仲裁和争议解决机构在上海设立机构并开展业务。鼓励海事仲裁机构参与国际海事争议解决规则、标准制定。Encourage all market entities to select Shanghai as the venue for resolving maritime commercial disputes. Support overseas arbitration and dispute resolution institutions to set up branches in Shanghai and carry out related businesses. Encourage maritime arbitration institutions to formulate localized rules aligned with international maritime dispute resolution standards.</td></tr><tr><td>关于促进洋山特殊综合保税区高能级 航运服务产业发展的实施意见 Implementation Opinions on Promoting the High-quality Development of High-level Shipping Service Industry within the Yangshan Special Comprehensive Bonded Zone</td><td>May-24</td><td>上海市人民政府Shanghai Municipal People&#x27;s Government</td><td>支持电力、氢能、液化天然气、绿色甲醇、氨等新能源、清洁能源在航运业推 广运用,加快推进行业绿色低碳转型。对符合条件的企业,加注甲醇、氨、绿电、氢能、液化天然气等清洁能源,按其清洁能源加注成本的20%予以支持,同一企业年度支持金额最高不超过1000万元。对提供甲醇、氨、液化天然气等清洁能源加注服务企业,按船舶购置成本给予适当奖励 Support the wide application of methanol, hydrogen, LNG, ammonia and other new clean energy sources in shipping industry, and accelerate the green low-carbon transformation of the industry. Subsidies covering 20% of vessel construction costs will be granted to eligible enterprises that build new vessels powered by methanol, hydrogen, LNG, ammonia and other clean energy; the maximum annual subsidy for a single enterprise shall not exceed Rmb10 million. Appropriate incentives will also be offered to shipping enterprises that deploy new energy-powered vessels fueled by methanol, LNG and other clean energy sources.</td></tr><tr><td>关于推动上海航运保险业高质量发展 的指导意见 Guiding Opinions on Promoting the High-quality Development of Shanghai&#x27;s Marine Insurance Industry</td><td>Oct-24</td><td>国家金融监督管理总局上海监管局,中共上海市委金融委员会办公室 NAFR Shanghai Bureau and CPC Shanghai Municipal Finance Committee Office</td><td>针对LNG船、甲醇船、纯电池船等绿色能源船舶和辅助驾驶等智能化船舶领域,多式联运、跨境电商、“中国制造”出口等物流贸易领域,智能码头、航运网络安全等基础设施领域,开发专业化、定制化的保险产品,逐步探索在新型风险领域率先建立行业标准和规范 Develop specialized, customized insurance products for LNG vessels, methanol vessels, lithium battery-powered vessels and other new energy vessels, as well as intelligent berthing, multi-modal transport, cross-border e-commerce and China manufacturing export cargo trade sectors; gradually formulate industry standards and norms for new risk-based insurance businesses.</td></tr><tr><td>关于推动上海航运保险业高质量发展 的指导意见 Guiding Opinions on Promoting the High-quality Development of Shanghai&#x27;s Marine Insurance Industry</td><td>Oct-24</td><td>国家金融监督管理总局上海监管局,中共上海市委金融委员会办公室 NAFR Shanghai Bureau and CPC Shanghai Municipal Finance Committee Office</td><td>鼓励辖内保险机构探索销售、承保、理赔、服务全流程数字化运营,优化业务流程,提升客户体验。把握航运贸易数字化趋势,运用区块链等技术,促进货运险电子保单等电子单证使用推广。Encourage insurance institutions to build full digital operation systems covering sales, underwriting, claims settlement and customer service, so as to optimize business processes and improve customer experience. Seize the digital transformation trend of shipping trade, adopt blockchain technology to promote the application of electronic documents such as freight insurance electronic policies.</td></tr></table>

Companies Discussed in This Report (all prices in this report as of market close on 07 July 2026, unless otherwise indicated)

China Reinsurance Group - H(1508.HK/HK\$1.11/N), China Taiping Insurance - H(0966.HK/HK\$19.72/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to China Reinsurance Group - H, China Taiping Insurance - H or related entities.

\- Market Maker/ Liquidity Provider (Hong Kong): JPM Securities (Asia Pacific) Limited and/or JPM Broking (Hong Kong) Limited and/or an affiliate is a market maker and/or liquidity provider in the securities of China Taiping Insurance - H or related entities and/or warrants or options thereon, which are listed or traded on The Stock Exchange of Hong Kong Limited.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: China Reinsurance Group - H, China Taiping Insurance - H or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: China Reinsurance Group - H or related entities.

\- Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from China Reinsurance Group - H or related entities.

\- Debt Position: JPM may hold a position in the debt securities of China Reinsurance Group - H, China Taiping Insurance - H or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

China Reinsurance Group - H (1508.HK, 1508 HK) Price Chart  
![](images/a2cdf6cc927b8d9e187f89be69492b4f5516acc8db9d2c59a4941689c11c5a40.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target (HK$)</td></tr><tr><td>22-Jun-25</td><td>OW</td><td>1.14</td><td>1.4</td></tr><tr><td>18-Aug-25</td><td>OW</td><td>1.68</td><td>2.1</td></tr><tr><td>16-Jan-26</td><td>N</td><td>1.69</td><td>1.8</td></tr><tr><td>10-Apr-26</td><td>N</td><td>1.39</td><td>1.6</td></tr><tr><td>12-May-26</td><td>N</td><td>1.28

[中间内容因长度限制已省略]

es discussed, unless otherwise stated. Past performance is not indicative of

future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
