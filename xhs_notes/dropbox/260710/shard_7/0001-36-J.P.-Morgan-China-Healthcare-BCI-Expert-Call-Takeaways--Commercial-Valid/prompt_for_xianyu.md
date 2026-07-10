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

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM 

[中间内容因长度限制已省略]

 opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

Completed 08 Jul 2026 10:44 PM HKT
"""
