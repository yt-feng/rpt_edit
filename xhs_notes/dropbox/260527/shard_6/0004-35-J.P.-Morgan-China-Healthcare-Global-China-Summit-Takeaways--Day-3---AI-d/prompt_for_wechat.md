你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

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

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

# History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

# Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to th

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase &

Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 25 May 2026 01:34 PM HKT

Disseminated 25 May 2026 01:42 PM HKT
"""
