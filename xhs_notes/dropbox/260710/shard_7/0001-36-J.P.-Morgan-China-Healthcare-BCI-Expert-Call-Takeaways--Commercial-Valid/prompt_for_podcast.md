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
# JPM

## China Healthcare

BCI Expert Call Takeaways: Commercial Validation, Not Technology Demonstration, Is the Next Inflection Point

We hosted three brain-computer interface (BCI) expert call sessions in the last few days and the experts we invited came from leading BCI companies in China, hold key management positions and on average possess about 10 years of experience in this field. Our most important takeaway based on the expert speakers' views is that BCI is transitioning from technology validation to clinical and commercial validation, but that the pace of monetization is likely to be slower and more volatile than recent headline regulatory news would suggest. The BCI competitive landscape should not be viewed as a pure technology race in which more advanced technology - such as higher channel count or more sophisticated signal acquisition - automatically translates into greater commercial value. Rather, the industry is increasingly segmenting by patient severity, clinical need and device invasiveness. Non-invasive BCI is likely sufficient for the majority of lower-acuity rehabilitation and training applications; semi-invasive systems may occupy the most attractive risk-benefit position for patients with severe functional impairment; penetrating BCI will remain concentrated in a small population requiring the highest signal fidelity; and ultrasound is, for now, more realistically a neuromodulation platform than a read & write BCI. The experts tend to believe that the first approved invasive BCI products in China may serve primarily as policy and clinical infrastructure milestones rather than meaningful revenue generators. They think that the next stage of sector differentiation will be determined by whether companies can demonstrate incremental efficacy over standard of care (SoC) for various disease indications, accumulate scalable patient data for further development, secure government and commercial insurance reimbursement, and convert hospital/home access into repeatable utilization. Here are a few key takeaways from the calls.

\- The emerging clinical hierarchy will be determined by the trade-off between signal quality and invasiveness. Non-invasive EEG (electroencephalogram)-based BCI has a fundamental signal-to-noise disadvantage, but for a large proportion of stroke patients with mild-to-moderate impairment, the expert feedback suggests that EEG may already be sufficient for rehabilitation, and subjecting these patients to neurosurgery would offer limited incremental value. Semi-invasive systems appear to occupy a potentially attractive middle ground: by avoiding penetration of the dura, they reduce surgical complexity and long-term biological risk while offering materially better signal quality than scalp EEG. This could make semi-invasive BCI the most commercially relevant implantable route for severe motor impairment, provided that it can demonstrate functional outcomes beyond those achievable through intensive rehabilitation activities plus non-invasive BCI. Penetrating systems such as Neuralink offer the highest signal resolution, but their addressable population is likely to remain narrow because the incremental functional benefit must be large enough to justify substantially greater surgical, ethical and long-term safety burdens.

\- Regulatory approval should be viewed as the beginning of product validation rather than the end of development. The experience of the first approved semi-invasive system is particularly instructive: according to one expert, rapid approval carries substantial policy and symbolic value, yet commercial adoption may remain constrained by limited functional

## Healthcare

Yang Huang AC (852) 2800 3812 yang.huang@JPM.com JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Eric Zhao, CFA  
(86-21) 6106 6256  
eric.zhao@JPM.com  
SAC Registration Number: S1730524050001  
JPM Securities (China) Company Limited

See page 4 for analyst certification and important disclosures, including non-US analyst disclosures.

Derek Choi
(852) 2800-8744
derek.c.choi@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

differentiation, uncertain physician conviction, and a substantial patient self-pay burden. This suggests a meaningful disconnect between regulatory progress and revenue realization. More BCI products could reach the market around 2027, but early commercial adoption is still likely to resemble controlled clinical deployment or advanced research rather than conventional high-volume medical-device adoption. According to the expert, a genuine commercial inflection point would require a reinforcing cycle in which post-launch clinical use generates broader datasets, better algorithms and more stable outcomes, which in turn support indication expansion, physician adoption and reimbursement.

\- The technical bottleneck is shifting from individual hardware components towards system-level integration and longitudinal signal robustness. The current development cycle has been enabled by advances in semiconductor miniaturization, packaging, high-density feedthroughs and electrode fabrication, but the expert feedback indicates that many BCI systems remain a collection of independently optimized modules rather than a fully integrated product. This is an important distinction: a high-channel-count electrode has limited value if the implant, acquisition chip, wireless transmission, decoding algorithm and effector cannot operate reliably as one system over years. The same logic applies to headline channel count. For motor-function restoration, the experts suggest that roughly 200 channels may already be clinically useful and that approximately 512 channels could address the large majority of current requirements. This implies diminishing returns from pursuing channel count alone. The more defensible competitive advantages may instead lie in chronic signal stability, implant durability, low-power processing, reproducible surgical implantation and closed-loop system performance.

\- AI can create real value in BCI, but its near-term impact will be highly asymmetric across technology routes and might be overstated when described as a universal solution. The non-invasive BCI expert argued that large AI models can materially shorten algorithm-development cycles and accelerate individual calibration, while the invasive BCI expert remained skeptical that existing large-model architectures can solve the fundamental instability of continuous, patient-specific neural signals. In non-invasive BCI, where products often solve more constrained classification or personalization problems and suffer from noisy signals, AI can improve denoising, reduce calibration requirements and make existing hardware materially easier to use. In implanted/invasive BCI, however, the core bottleneck is not simply AI model sophistication: neural signals differ between individuals, change with patient state and may drift over time after implantation. A generalizable “brain foundation model” therefore requires large, standardized and longitudinal multimodal datasets that do not yet exist. Plus, what algorithm will be best for a BCI-related model is also unknown. According to the expert, near-term value of AI for BCI should accrue to companies using AI to reduce patient-specific training and improve real-world robustness, while the much larger promise of universal neural decoding or even “brain model” should be viewed as a longer-term thesis.

\- The domestic supply chain opportunity is rising and might be important to support long-term needs. For BCI components, China needs to catch up in analog front-end chips for EEG, implantable acquisition chips and certain highly specialized biocompatible materials, while its strengths are more visible in non-invasive electrode manufacturing. However, the commercial significance of each localization opportunity differs sharply. Implant-grade polyimide and biocompatible silicone may be strategically important, but current industry demand is too small to support a large standalone upstream market. The more attractive opportunities are likely to emerge where BCI requirements overlap with larger markets, such as low-noise analog front ends, flexible electronics, high-density packaging, MEMS (micro-electromechanical systems) transducers and low-power signal processing. Our experts also expect local production to accelerate for strategic and data-security reasons, even where domestic components initially trail imported products in absolute performance.

\- Ultrasound represents the highest long-term technical optionality among emerging routes. The ultrasound session presented an ambitious vision of broader brain coverage with ultrasound technology, multimodal foundation models and eventual whole-brain read-write capability, but the current commercial pathway is much more concrete on the “write” side than the “read” side. Low-intensity focused ultrasound (LIFU) can modulate specific brain regions non-invasively, creating real applications in chronic pain management, psychiatric disease control, stroke rehabilitation and blood-brain-barrier opening. In contrast, high-resolution transcranial reading remains constrained by the skull, and blood flow-based signals introduce a temporal gap relative to direct electrical activity. Chronic pain could be a sensible first indication for ultrasound-based BCI, and its success will depend on conventional endpoints including clinical efficacy, durability, and safety. The expert is optimistic about this indication as the target population is large and there is a clear unmet need for non-opioid alternatives.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Huang, Yang : Akeso (9926.HK), Ascentage Pharma - H (6855.HK), BeOne - A (688235.SS), BeOne - H (6160.HK), Bora Pharmaceuticals (6472.TW), DaShenLin Pharmaceutical Group - A (603233.SS), Genscript Biotech - H (1548.HK), Hansoh Pharma - H (3692.HK), Hengrui - A (600276.SS), Hengrui - H (1276.HK), Innovent Biologics (1801) (1801.HK), Kelun Biotech (6990.HK), Laobaixing Pharmacy Chain - A (603883.SS), Mindray - A (300760.SZ), RemeGen - A (688331.SS), RemeGen - H (9995.HK), Shanghai Junshi Biosciences - A (688180.SS), Shanghai Junshi Biosciences - H (1877.HK), Tigermed - A (300347.SZ), Tigermed - H (3347.HK), WuXi AppTec - A (603259.SS), WuXi AppTec - H (2359.HK), WuXi Biologics (2269.HK), WuXi XDC (2268.HK), Yifeng - A (603939.SS)

JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or const

[中间内容因长度限制已省略]

rom any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

Completed 08 Jul 2026 10:44 PM HKT
"""
