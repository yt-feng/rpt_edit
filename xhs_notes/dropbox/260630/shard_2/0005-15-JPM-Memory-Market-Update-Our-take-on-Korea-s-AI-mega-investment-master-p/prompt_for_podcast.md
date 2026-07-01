你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Samsung C&T, SK Inc or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Samsung C&T, SK Inc or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Samsung C&T (028260.KS, 028260 KS) Price Chart  
![](images/67f4c65bbd42ba4cff6e56e38543808ad148564894b27d3020a23b2f82bc6eaf.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (W)</td><td>Price Target (W)</td></tr><tr><td>01-Feb-24</td><td>OW</td><td>138000</td><td>170,000</td></tr><tr><td>01-Aug-24</td><td>OW</td><td>155300</td><td>185,000</td></tr><tr><td>23-Jan-25</td><td>N</td><td>122600</td><td>140,000</td></tr><tr><td>05-Jun-25</td><td>OW</td><td>157800</td><td>205,000</td></tr><tr><td>29-Oct-25</td><td>OW</td><td>208500</td><td>260,000</td></tr><tr><td>19-Jan-26</td><td>OW</td><td>289500</td><td>370,000</td></tr><tr><td>21-May-26</td><td>OW</td><td>375500</td><td>570,000</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Apr 08, 2015. All share prices are as of market close on the previous business day. SK Inc (034730.KS, 034730 KS) Price Chart  
![](images/a1fa0ab8ca4178b1faa5c3f5ebc497538d508573ce795c114e1e122693ffb79c.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (W)</td><td>Price Target (W)</td></tr><tr><td>26-Nov-23</td><td>OW</td><td>160700</td><td>200,000</td></tr><tr><td>28-Feb-25</td><td>N</td><td>149500</td><td>160,000</td></tr><tr><td>05-Jun-25</td><td>OW</td><td>180700</td><td>230,000</td></tr><tr><td>05-Jan-26</td><td>OW</td><td>260000</td><td>350,000</td></tr><tr><td>21-May-26</td><td>OW</td><td>532000</td><td>870,000</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Apr 06, 2015. All share prices are as of market close on the previous business day.  
The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the

[中间内容因长度限制已省略]

description of JPM EMEA’s policy for prevention and avoidance of conflicts of interest related to the production of Research can be found at the following link: JPM EMEA - Research Independence Policy.

U.S.: JPM Securities LLC (“JPMS”) is a member of the NYSE, FINRA, SIPC, and the NFA. JPM Chase Bank, N.A. is a member of the FDIC. Material published by non-U.S. affiliates is distributed in the U.S. by JPMS who accepts responsibility for its content.

General: Additional information is available upon request. The information in this material has been obtained from sources believed to be reliable. While all reasonable care has been taken to ensure that the facts stated in this material are accurate and that the forecasts, opinions and expectations contained herein are fair and reasonable, JPM Chase & Co. or its affiliates and/or subsidiaries (collectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is
"""
