你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
## Asian Tech

## 2026 Computex Takeaways Part 1

In this note, we summarize the highlights from NVIDIA's GPU Technology Conference (GTC) and QCOM's keynote sessions at Computex.

\- Few new product introductions, other than the much awaited N1X for Windows PCs, bringing agents to the client device: Overall, the event was light on new product reveals, with NVIDIA announcing its first processor for Windows PCs, N1X or RTX Spark, designed in partnership with Mediatek. This chip has been in the works for \~2 years and should span desktop, notebook and Workstation categories of Windows PCs, bringing high-end token processing capabilities to the PC. NVIDIA envisions this to become a key enabler in bringing AI Agents to client devices with 1 petaflops of AI capability, and the ability to run 120b parameter LLMs at up to 1M context window. We believe the re-imagining of the application suite (for agentic AI) and compatibility of legacy x86 applications (something that has held back Qualcomm's ARM PC growth) are still key factors in determining the success of this product in the medium term. On PCs overall, the key watch point is whether the increasing edge AI adoption will stimulate incremental PC unit shipments. For Mediatek, this is a small (1-2%) revenue driver (largely royalty-based for the ARM CPU and other connectivity chip sales), but it could establish its presence in the Compute space, after its recent success with Chrome/Googlebook. Qualcomm did not introduce any new products during its keynote, with a passing mention of its Dragonfly AI Server racks, likely to be introduced in late June, at its analyst day. Our supply chain checks indicate that Qualcomm's inference-focused ASICs and Datacenter CPUs are likely for Bytedance and one US hyperscaler, with volumes ramping in 2027.

\- Agentic AI workloads as key focus, split between edge and cloud, will be interesting to watch: Both keynotes from NVIDIA and Qualcomm spent a lot of time on agentic AI workloads (as expected), given the rapid rise of AI agents. NVIDIA framed the AI agent as comprising four components—LLM (brain), Harness (body/orchestration), Tools, and Runtime (working environment)—noting that GPUs, CPUs and DPUs are all part of the hardware stack required for agentic AI. In addition, NVIDIA highlighted its move towards being the full-stack enabler of agentic AI infrastructure and software for enterprises (CUDA-X libraries, Nemotron open models, etc., in addition to various forms of compute) and highlighted indicative agentic workloads such as a partnership with Cadence on a chip-design super-agent that accelerates verification cycles by \~40x, from weeks to hours. Qualcomm’s CEO, Cristiano Amon, highlighted the staggering growth in token consumption, projecting a 40x growth from 2026 to 2030. Qualcomm expects agentic AI to redesign how applications are written for personal devices like smartphones and expects agents to work across multiple devices in the future, rather than be tethered to one primary device. Interestingly, QCOM expects agentic AI workload to be distributed between on-device and cloud over time (unlike now, where almost 100% of the AI workload resides in the cloud), which could trigger a replacement cycle for edge devices. Qualcomm indicated that several

## Technology and Telecoms

## Gokul Hariharan AC

(852) 2800-8564

gokul.hariharan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Albert Hung AC

(886-2) 2725-9875

albert.hung@jpmchase.com

JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hòng Kong) Limited

## William Yang AC

(886-2) 2725-9899

william.yang@JPM.com

JPM Securities (Taiwan) Limited

## Jennifer Hsieh

(886-2) 2725-9868

jennifer.hsieh@JPM.com

JPM Securities (Taiwan) Limited

## Anthony Leng

(886-2) 2725-9240

anthony.leng@JPM.com

JPM Securities (Taiwan) Limited

## Megan Hsueh

(886-2) 2725-9249

megan.hsueh@JPM.com

JPM Securities (Taiwan) Limited

## David Chou

(886-2) 2725-9618

david.chou@JPM.com

JPM Securities (Taiwan) Limited

## Jason Chen

(886-2) 2725-9864

jason.bh.chen@JPM.com

JPM Securities (Taiwan) Limited

## Subham Singhania

(91-22) 6157-3801

subham.singhania@JPM.com

JPM India Private Limited

workloads such as coding/webpage creation could run with 30-60% less tokens and potentially run faster using a device-cloud hybrid approach. In this context, what Apple announces at its WWDC next week could be more important, potentially giving momentum to the idea of a resurgence in edge-based AI compute. In the near term, we believe the quest for faster LLMs is likely to keep most of compute on the cloud.

\- NVIDIA Vera Rubin now in full production, focus on co-design of various rack elements and token maximization: NVIDIA confirmed that Vera Rubin is now in full production, with Microsoft and Dell/CoreWeave already standing up engineering racks. Based on our checks, we believe a larger-scale rack production ramp would likely be in 4Q this year. The production efficiency leap is meaningful—VR racks can now be assembled in approximately 5 minutes compared with 2 hours for the prior Blackwell generation, due to limited cabling and fans, replaced with liquid cooling and a mid-plane PCB for interconnections. The emphasis on Vera Rubin is on the co-design of various compute elements (Vera Rubin, Vera CPU, Bluefield DPU, storage rack, Spectrum SPX rack with Co-packaged Optics, LPX for fast tokens) to enable much higher token throughput (10x higher compared to GB300s) and maximizing revenue per GW. Overall mass production timelines are largely in line with our expectations; we continue to expect Rubin shipments to be constrained by HBM4 supply and minor issues in CoWoS-L packaging through 2026 and expect \~2M units of front-end shipments, which should translate to \~10k racks of VR200 NVL 72 deliveries in 2026 (major vendors such as MSFT/Dell are expected to produce 1-2K in 2026, in our view).

\- Heavy focus on Vera CPU and designing CPUs purpose-built for agentic AI: NVIDIA's CEO Jensen Huang spent significant time detailing the Vera CPUs designed specifically for agentic AI workloads. Vera CPU delivers 1.8x agentic AI sandbox performance versus x86, with the highest instructions per clock (IPC) in the world, per management. The chip is the first to implement PCIe 6 and LPDDR5X memory at 1.2 TB/s, delivering 3x bandwidth both internally and externally while consuming 40% lower peak memory latency. On database workloads, Vera runs SQL 3x faster than x86. NVIDIA appears to be positioning standalone Vera CPU sales as a major incremental growth driver for the company, given the rise in agentic AI workloads. We believe that Vera CPU shipments should start ramping up from 2H26 (we estimate 0.6M units in 2026) but with a strong ramp (3M+ units with potential for upside) in 2027, with packaging solutions coming from TSMC, Amkor, and potentially ASE. Hon Hai and Quanta are likely to be the key standalone rack vendors, with more vendors likely to be added over time. We do expect competition to increase over the next few quarters given the rise of CPU as a new TAM, with Qualcomm and potentially Mediatek entering the fray, along with in-house projects at all major CSPs. For the semiconductor ecosystem (TSMC, OSATs such as ASE, substrate vendors), datacenter CPUs represent a very strong new TAM growth opportunity, adjacent to AI accelerators, which should prolong the supply shortages well into 2027. Meanwhile, for cooling specifically, CPU racks have more cold plates and QDs, potentially benefitting AVC and Fositek, in our view.

\- Moving beyond the compute rack to full-stack infra – NVIDIA launches DSX as a full-stack infra reference design solution to empower AI factories: NVIDIA also launched the DSX platform at the GTC, showcasing its expanded capabilities from chip/rack sales to a reference design for a full AI factory infrastructure, integrating power optimization and infra/platform software. As the capital intensity grows higher than ever (from \$20-30bn per GW in prior generations to potentially \$80-100bn per GW in the future), DSX is intended to improve AI factory efficiency and cost of ownership for CSPs. DSX MaxLPS is one of the highlighted software suites that utilizes 45-degree Celsius hot liquid cooling and optimizes GPU deployment within the same power budget (given NVIDIA believes that today’s datacenters overprovision power by up to 40%), while the DSX Flex platform can help dynamically adjust workloads based on grid conditions. DSX early adopters include CoreWeave and Lambda, among others. Key beneficiaries in the Asian tech supply chains, in our view, include liquid cooling supplier AVC and power supply vendor, Delta.

Note: NVIDIA (NVDA US) is covered by JPM analyst Harlan Sur, and Qualcomm (QCOM US) is covered by JPM analyst Samik Chatterjee.

Companies Discussed in This Report (all prices in this report as of market close on 01 June 2026, unless otherwise indicated) ASE Technology Holding Co Ltd(3711.TW/NT\$601.00/OW), Asia Vital Components(3017.TW/NT\$2,785.00/OW), Delta Electronics, Inc.(2308.TW/NT\$2,420.00/OW), Fositek(6805.TW/NT\$2,120.00/OW), MediaTek Inc.(2454.TW/NT\$4,555.00/OW), NVIDIA Corporation(NVDA/\$224.36/OW), Qualcomm(QCOM/\$228.99/N), TSMC(2330.TW/NT\$2,355.00/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Hariharan, Gokul : ASE Technology Holding Co Ltd (3711.TW), ASMPT Ltd (0522) (0522.HK), Alchip Technologies (3661.TW), Chipbond Technology (6147.TWO), GDS Holdings (GDS), GUC (3443.TW), Hon Hai Precision (2317.TW), MediaTek Inc. (2454.TW), Novatek Microelectronics Corp. (3034.TW), Powerchip Semiconductor Manufacturing Corp. (6770.TWO), SMIC (0981) (0981.HK), Silicon Motion (SIMO), TSMC (2330.TW), UMC (2303.TW), Vanguard International Semiconductor Corp. (5347.TWO), Xiaomi (1810) (1810.HK)Hung, Albert : ASPEED Technology Inc. (5274.TWO), ASUSTek Computer (2357.TW), Compal Electronics, Inc. (2324.TW), Delta Electronics, Inc. (2308.TW), Inventec (2356.TW), Lenovo Group Limited (0992) (0992.HK), Lotes (3533.TW), Micro-Star International Co., Ltd. (2377.TW), Pegatron Corp (4938.TW), Quanta Computer Inc. (2382.TW), VNET Group (VNET), Wistron Corporation (3231.TW), Wiwynn Corp (6669.TW)Yang, William : AAC Technologies Holdings (2018) (2018.HK), AP Memory Technology Corp (6531.TW), ASMedia Technology Inc. (5269.TW), Advanced Energy Solution Holding (6781.TW), Advantech (2395.TW), Andes Technology Corp (6533.TW), Asia Vital Components (3017.TW), Auras Technology (3324.TW), Fositek (6805.TW), Genius Electronic Optical Co., Ltd (3406.TW), Jentech Precision Industrial Co. (3653.TW), Klinik (1560.TW), Largan Precision Co Ltd (3008.TW), Parade Technologies (4966.TWO), Realtek Semiconductor (2379.TW), Shin Zu Shing (3376.TW), Silergy Corp (6415.TW), Simplo Technology Co Ltd (6121.TWO), Speed Tech Corp (5457.TWO), Sunny Optical Technology Group Co. (2382) (2382.HK)

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial 

[中间内容因长度限制已省略]

ptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL

LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 02 Jun 2026 10:50 AM HKT

Disseminated 02 Jun 2026 10:50 AM HKT
"""
