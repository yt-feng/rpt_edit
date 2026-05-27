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
# China Healthcare

Global China Summit Takeaways (Day 3): AI drug discovery validation on the way; BD and global market focus; service sector update

Across meetings, management teams leaned into a consistent narrative: AI is moving from “promise” to measurable productivity (faster drug candidate generation, higher pipeline throughput, and deeper CMC integration), while China remains the near-term monetization engine through commercialization scale-up and BD-driven partnering. WuXi Bio reiterated its accelerated growth target for the next few years. MedBot pointed to hospital utilization ramp and KOL-backed global readiness, and Aier/Dashenlin reinforced how operational execution and revenue mix shift are central to sustaining growth and investor confidence.

- Insilico Medicine (Not Covered\*): Validating AI through rapid pipeline asset number growth and major pharma deals. Management emphasized its ability to dramatically accelerate drug discovery, noting that its platform can generate a new preclinical candidate (PCC) in just 4.5 months on average. Viewing pipeline asset count as a key metric of its AI's success, it proudly highlighted the generation of \~30 PCCs since 2021 to demonstrate this unmatched scale. To prove that the technology translates into the real world, it pointed to its lead drug, rentosertib, which successfully completed a Ph2a trial as a fully AI-designed molecule. Strategically, management is monetizing this high productivity through a dual-business model: advancing a large number of its pipeline assets for out-licensing, while securing major co-development deals with multinational partners such as Eli Lilly and Servier to fund ongoing research and validate its platform.   
- WuXi Biologics: Mitigating geopolitical risk while shifting portfolio mix toward higher-margin complex biologics. Management reassured investors on geopolitical risk reduction by highlighting its active geographic capacity diversification in the US, EU and Singapore, and reinforcing a steadfast commitment to global clients. Commercially, it is driving a strategic portfolio shift beyond plain mAbs, which face margin compression, toward complex modalities such as bispecifics and ADCs, aiming to grow the multispecific business to $25\%$ of the revenue mix in a few years. To support scale and efficiency, the company is increasingly embedding AI into its CMC (chemistry, manufacturing, and controls) and process development workflows, targeting the capacity to handle hundreds of IND (investigational new drug)-enabling packages annually to reduce wet lab work and maintain a competitive edge.   
- Sino Biopharm: Building an AI-enhanced development engine anchored by late-stage assets. Management positioned the company as the commercial partner of choice in China, highlighting its distribution agreement for GSK's bepirovirsen (an antisense oligonucleotide hepatitis B virus therapy) as a cornerstone of its commercial strategy. Alongside advancing internal assets such as the M701 bispecific antibody (EpCAMxCD3) towards an anticipated 2026 NDA filing, it is focused on combining AI-driven target discovery with aggressive out-licensing efforts. Management's core priority is to leverage this integrated development model to partner with multinationals seeking to commercialize novel, high-value drug modalities such as ADCs and siRNAs.

# Healthcare

Yang Huang AC

(852) 2800 3812

yang.huang@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Derek Choi

(852) 2800-8744

derek.c.choi@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Eric Zhao, CFA

(86-21) 6106 6256

eric.zhao@JPM.com

SAC Registration Number: S1730524050001

JPM Securities (China) Company Limited

\*NOTE: THIS DOCUMENT IS INTENDED AS INFORMATION ONLY AND NOT AS A RECOMMENDATION FOR ANY STOCK. IT CONTAINS FACTUAL INFORMATION, OBTAINED BY THE ANALYST DURING MEETINGS WITH MANAGEMENT. JPM DOES NOT COVER THIS COMPANY AND HAS NO RATING ON THE STOCK.

\- Plenary Session: “Re-defining biopharma innovation: From drug discovery to business development”. The panel of leaders from Inscilico, Regor Therapeutics and LaNova focused on how AI is fundamentally changing the economics of drug discovery, allowing companies to generate up to four times more clinical candidates for the same R&D budget. Management teams agreed that value creation now hinges on an “East-to-West” strategy, where China biotechs must develop best-in-class assets to Western clinical standards to command premium global licensing deals. They stressed that AI is no longer just an early-discovery tool but is also actively being integrated across wet lab and CMC operations, projecting that AI-enabled pipelines backed by strong BD deals could drive significant top-line CAGRs for well-positioned biotechs by 2027–2028.

\- Refractive ASP recovery and overseas expansion continue to be key drivers of Aier into 2H26. On the refractive business, the SMILE price war is structurally over following Zeiss's decision to restrict SMILE 4.0 licensing only to large chains and public hospitals, restoring pricing discipline, with SMILE prices back above Rmb10,000; the V5 ICL lens was supply-constrained in 1Q but capacity is expected to normalize in 2H26, creating a visible volume as well as an ASP uplift catalyst for the segment. Overseas is another growth story: the Europe business will see sustained growth with margins above domestic levels, and a potential Brazil acquisition (\~Rmb1 bn revenue, valuation <2x P/S, 40% stake) might be closed in 2H26. As for the proposed H-share listing, management confirmed that it had passed the IPO hearing on May 18 and the stock is expected to be listed by the end of 2026 at the earliest.

\- Dashenlin's \~10% FY26 growth target hinges on same-store recovery, restarted store expansion, and non-pharma category contribution. Management confirmed QoQ improvement in same-store sales, and maintained guidance of 2,000+ new franchise stores alongside 500 self-built and 400–500 acquired stores. Dashenlin is also executing a phased store-rearranging program (100 stores completed in 1Q, targeting 500 by the end of 1H26) to feature more non-pharma products. Unlike some of the other chains, Dashenlin is targeting higher gross margin for the non-pharma categories (30–40%), supported by its supply chain advantage and collaboration with some online-native brands to gain higher margins in exchange for offline distribution. It also utilized more private-label products, which typically carry higher GPMs.

\- Duality's (Not Covered\*) most important near-term catalyst is the WCLC presentation of B7-H3 ADC (DB-1311)'s combo data with BioNTech's PD-L1/VEGF bispecific in lung cancer, covering ORR and safety across approximately 150 enrolled first- and second-line NSCLC and SCLC patients. Management believes the competitive window in the bispecific antibody-plus-ADC combo space is narrow and closing: it estimates a two-year window before one of the three competing first-line lung cancer combo approaches (bispecific plus chemo, PD-1/PD-L1 plus ADC, or bispecific plus ADC) establishes itself as standard of care. Management also commented that the company is currently ahead of GSK/Hansoh's competing B7-H3 ADC program, which is not expected to initiate Ph3 trials in prostate cancer until the end of 2026. Another differentiation case for DB1311 rests on a meaningfully cleaner safety profile, with Grade 3+ TRAE of only 20% as a single agent in CRPC (castration-resistant prostate cancer). The absence of on-target toxicity makes it better suited for front-line combo use. Financially, the company is in a strong position with Rmb3.5 bn in cash, US\$100mn in expected 2026 milestone income, and annual R&D spend of approximately US\$150 mn, providing a comfortable multi-year runway. The upcoming STAR Market listing, through which the company expects to raise Rmb4–6+ billion, depending on the A-share valuation, would provide additional liquidity to support co-development of B7-H3 ADC and HER2 ADC development, as well as other key assets such as DB-1419 (B7-H3/PD-L1 ADC).

\- MedBot: driving commercial scale, KOL validation, and US market preparation. Management is focused on the commercial scale-up of the Toumai surgical robot, targeting a shift toward 60% OR utilization in key accounts by 2026 to capture China's price-sensitive hospital base. It heavily emphasized key opinion leader (KOL) validation—specifically citing Dr. Vipul Patel and a recent FDA-IDE approved USA-Africa telesurgery milestone—as definitive proof of the platform's global competitiveness. Financially, management believes sustainable profitability will come from manufacturing cost reductions, higher-margin service offerings, and expanding its active hospital footprint toward 800–1,000 sites. Management views near-term growth as China-led while laying the clinical groundwork for an eventual US market entry.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

# Important Disclosures

- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Duality or related entities.   
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Insilico Medicine or related entities.   
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Insilico Medicine or related entities.   
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Insilico Medicine or related entities.   
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Insilico Medicine or related entities.   
- Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Insilico Medicine or related entities.   
- Debt Position: JPM may hold a position in the debt securities of Duality, Insilico Medicine or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

# Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Huang, Yang : Akeso (9926.HK), Ascentage Pharma - H (6855.HK), BeOne - A (688235.SS), BeOne - H (6160.HK), DaShenLin Pharmaceutical Group - A (603233.SS), Genscript Biotech - H (1548.HK), Hansoh Pharma - H (3692.HK), Hengrui - A (600276.SS), Hengrui - H (1276.HK), Innovent Biologics (1801) (1801.HK), Kelun Biotech (6990.HK), Laobaixing Pharmacy Chain - A (603883.SS), Mindray - A (300760.SZ), RemeGen - A (688331.SS), RemeGen - H (9995.HK), Shanghai Junshi Biosciences - A (688180.SS), Shanghai Junshi Biosciences - H (1877.HK), Tigermed - A (300347.SZ), Tigermed - H (3347.HK), WuXi AppTec - A (603259.SS), WuXi AppTec - H (2359.HK), WuXi Biologics (2269.HK), WuXi XDC (2268.HK), Yifeng - A (603939.SS)

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into 

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase &

Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 25 May 2026 01:34 PM HKT

Disseminated 25 May 2026 01:42 PM HKT
"""
