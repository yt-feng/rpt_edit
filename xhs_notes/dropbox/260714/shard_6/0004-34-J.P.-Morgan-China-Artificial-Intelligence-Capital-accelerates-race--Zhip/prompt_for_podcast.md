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
## China Artificial Intelligence

## Capital accelerates race; Zhipu (OW) PT to HK\$2400 on higher ARR visibility; MiniMax (N) needs stronger model validation

We raise our price target for Zhipu AI to HK\$2,400 from HK\$2,000 and maintain Overweight; we lower our MiniMax price target to HK\$240 from HK\$300 and maintain Neutral following both companies' large financing announcements last week. We believe the foundation-model industry is moving into a more capital-intensive phase, where access to funding supports longer model development cycles and infrastructure expansion. However, investment returns will ultimately depend on each company's ability to translate resources into model improvements, customer adoption and ARR growth. For Zhipu, demand already presses against serving capacity, so incremental inference resources plausibly convert to ARR within 12 months, with the financing funds a conversion that is already visible, in our view. For MiniMax, conversion runs through model capability that is not yet demonstrated against peers, so the financing buys time to prove conversion, while its cost is certain – immediately effective at 11% and potential of another 6% assuming full-conversion of the convertible bonds. The same catalyst therefore moves the two PTs in opposite directions.

\- Capital intensity is rising across independent LLM providers, yet capital is a necessary rather than sufficient condition. Since the start of 2026, Chinese independent LLM providers collectively raised or announced over US\$20+bn via IPOs, placements and private rounds, reflecting the increasing resource requirements of frontier model development. Going forward, we expect differentiation to come from technical direction, talent quality and density, execution and efficiency of converting capital investment into commercial growth. We will judge that through the coming release cycle, specifically MiniMax's M3Pro, Zhipu's GLM 5.5, and DeepSeek's V4 official.

\- Zhipu AI: financing accelerates a visible demand-to-revenue conversion path. The US\$4bn placement at 4.4% shares alleviates potential serving capacity constraint where demand is extremely strong, in addition to its support of the forward model trainings. We believe incremental inference capacity can enhance higher ARR conversion over the next 12 months – we therefore hike PT to HK\$2,400 (implies 30-35x at US\$4-5bn 2027-end ARR) after this visible conversion. Key risks remain around: free float is at 14% after the placement, so volatility stays extreme on a stock up 14x YTD; continued pricing power or widening model leadership position would further validate our thesis.

\- MiniMax: certain cost today, unproven conversion tomorrow. The US\$2bn raise removes training resource constraints, but the two sides of the trade are not symmetric in time or certainty. The dilution is booked now: about 11% of share count from the placement, rising toward 17% on full CB conversion. The offsetting value depends on MiniMax first closing the capability gap versus peers and then monetizing it, two steps that have not yet occurred. We cut the PT to HK\$240 to reflect the certain dilution against a conversion path still to be evidenced. We would turn more constructive after seeing clear evidence of model improvement and narrowing monetization gap versus peers.

See page 13 for analyst certification and important disclosures, including non-US analyst disclosures.

Hong Kong

SAC Registration Number: S1730525060001

Alex Yao
(86 21) 6106 6505
alex.yao@JPM.com
SAC Registration Number: S1730523020001

Daniel Chen
(86-21) 6106 6205
daniel.q.chen@JPM.com
SAC Registration Number: S1730521040001
JPM Securities (China) Company Limited

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>Zhipu AI</td><td>2513 HK</td><td>46,320</td><td>HKD</td><td>1,640.00</td><td>OW</td><td>n/c</td><td>2,400.00</td><td>Dec-26</td><td>2,000.00</td><td>n/c</td></tr><tr><td>MiniMax Group Inc - H</td><td>100 HK</td><td>7,821</td><td>HKD</td><td>268.60</td><td>N</td><td>n/c</td><td>240.00</td><td>Dec-26</td><td>300.00</td><td>n/c</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 10 Jul 26.

## China AI foundation-model industry: capital accelerates the race, while execution determines outcomes

The foundation-model industry is becoming structurally more capital intensive: maintaining competitiveness requires continuous investment across pre-training, post-training, reinforcement learning, evaluation infrastructure and inference deployment. Unlike traditional software businesses where incremental distribution can scale at relatively low marginal cost, frontier AI models require repeated investment cycles to improve capability and support growing usage. This dynamic is increasingly visible among China's independent LLM providers –since the start of 2026, Chinese independent LLM providers have collectively raised or announced over US\$20+bn via IPOs, placements and private rounds.

However, the increasing importance of capital does not mean funding alone determines competitive outcomes, as model development remains dependent on several other factors, including the ability to identify the right technical direction, attract high-quality research talent, build efficient engineering processes and organize resources effectively. Capital provides additional resources and extends the ability to compete, while companies still need to demonstrate that these resources can translate into stronger models. For investors, the key question is therefore how efficiently companies convert capital into competitive advantages. Additional funding can accelerate model iteration and commercialization, while the ultimate differentiation remains the ability to consistently deliver stronger models.

Table 1: 2026 YTD financing progress of independent China LLM providers

<table><tr><td>Company</td><td>Date</td><td>Transaction Type</td><td>Amount Raised</td><td>Valuation (Post-Money)</td></tr><tr><td rowspan="3">Zhipu AI</td><td>TBD</td><td>STAR Market Listing (Target)</td><td>~US$2.1bn (Rmb15.0bn)</td><td>N/A</td></tr><tr><td>Jul-26</td><td>Share Placement</td><td>~US$4.0bn</td><td>Public Market Cap (placement on 4.4% of total shares)</td></tr><tr><td>Jan-26</td><td>Hong Kong IPO</td><td>~US$0.6bn (HK$4.4bn)</td><td>~US$13.0bn (at debut)</td></tr><tr><td rowspan="3">MiniMax</td><td>TBD</td><td>STAR Market Listing (Target)</td><td>N/A</td><td>N/A</td></tr><tr><td>Jul-26</td><td>Share Placement &amp; Convertible Bonds</td><td>~US$2.1bn (HK$16.0bn)</td><td>Public Market Cap (placement on 11% of total shares, convertible bonds at 6% of total shares)</td></tr><tr><td>Jan-26</td><td>Hong Kong IPO</td><td>~US$0.7bn (HK$5.5bn)</td><td>~US$13.7bn (at close)</td></tr><tr><td>DeepSeek</td><td>Jun-26</td><td>Series A (First External Round)</td><td>~US$7.4bn (&gt;Rmb50.0bn)</td><td>&gt;US$50.0bn (&gt;Rmb330.0bn)</td></tr></table>

Source: Zhipu/MiniMax prospectus, placement announcements, Bloomberg Finance L.P. (data as of Jul 10, 2026)

Figure 1: Zhipu & MiniMax 2022-25 R&D spending and IPO proceeds 6-month spending (US\$mn)  
![](images/9cc194ecf3f25c53ae6c68bc4f1fc903c7525a7678da94007b4b7a942cb0b9cf.jpg)  
Source: Zhipu/MiniMax prospectus and placement announcements, (data as of Jul 10, 2026)

Figure 2: Zhipu & MiniMax 2022-25 R&D spending as % of revenue  
![](images/d42da01b192090e20bbcb905579942b00da1392670ee4cd8e504fbb71e149025.jpg)  
Source: Zhipu/MiniMax prospectus and placement announcements, (data as of Jul 10, 2026)

## Zhipu AI: financing improves execution visibility across model development and commercialization; PT to HK\$2,400

We view Zhipu's financing positively as it reduces potential execution constraints across both model development and commercialization. Additional capital does not independently create model leadership, and Zhipu's long-term positioning will continue to depend on its research direction, talent quality and organizational execution. However, given Zhipu's recent strong model progress and commercial momentum, additional resources improve confidence around the company's ability to execute against future opportunities.

On the training side, financing provides greater flexibility to support future model cycles. Frontier model development requires sustained investment across pre-training, post-training, reinforcement learning and engineering optimization. As model competition continues to accelerate, maintaining sufficient resources becomes increasingly important for companies seeking to remain competitive. Zhipu's expected R&D investment reflects the significant resources required to continue improving model capability.

On the inference side, we see a more direct monetization benefit in the next 12 months. We believe Zhipu's current bottleneck has increasingly shifted from demand generation toward serving capacity. The company has demonstrated strong demand momentum across API services and enterprise use cases, while available inference resources remain a constraint across the industry. Additional compute investment should allow Zhipu to expand serving capacity, improve service availability and convert existing demand into revenue more efficiently.

The combination of training support and inference expansion creates a more favorable financing impact for Zhipu. Additional capital supports the development of future model capability while also improving the company's ability to monetize current demand. This provides greater visibility on ARR upside over the next 12 months.

Key risks remain around: free float is at 14% after the placement, so volatility stays extreme on a stock up over 1,700% YTD; continued pricing power or sustained utilization would further validate our thesis.

## Estimate changes

We raise Zhipu's 2026-30E revenue by 7-13% to reflect higher monetization visibility with more sufficient capital to expand compute power. We also increase the share count number to reflect the recent H-share placement of 4.4% of total shares. Accordingly, we lower our adjusted net loss forecasts from a loss of Rmb3,711mn, loss of Rmb3,141mn and profit of Rmb2,367mn in 2026, 2027 and 2028 to a loss of Rmb3,605mn, loss of Rmb2,566mn and profit of Rmb4,120mn. We consequently raise our Dec-26 price target to HK\$2,400 from HK\$2,000, still based on 30x 2030E P/E discounted back using a 15% WACC.

Table 2: Estimate changes summary for Zhipu AI

<table><tr><td>Rmb mn</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>5,038</td><td>13,768</td><td>37,672</td><td>101,706</td><td>175,864</td></tr><tr><td>Old</td><td>4,715</td><td>12,324</td><td>33,485</td><td>89,984</td><td>155,497</td></tr><tr><td>% change</td><td>7%</td><td>12%</td><td>13%</td><td>13%</td><td>13%</td></tr><tr><td>Operating profit</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>(5,173)</td><td>(5,532)</td><td>(569)</td><td>22,085</td><td>52,249</td></tr><tr><td>Old</td><td>(5,280)</td><td>(6,108)</td><td>(2,322)</td><td>16,932</td><td>42,847</td></tr><tr><td>% change</td><td>2%</td><td>9%</td><td>75%</td><td>30%</td><td>22%</td></tr><tr><td>Adjusted net profit</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>(3,605)</td><td>(2,566)</td><td>4,120</td><td>24,264</td><td>50,380</td></tr><tr><td>Old</td><td>(3,711)</td><td>(3,141)</td><td>2,367</td><td>20,141</td><td>42,858</td></tr><tr><td>% change</td><td>3%</td><td>18%</td><td>74%</td><td>20%</td><td>18%</td></tr></table>

Source: JPM estimates (data as of Jul 10, 2026)

## MiniMax: Financing alleviates resource constraints, while model capability remains the key catalyst; PT to HK\$240

MiniMax's latest financing meaningfully strengthens its financial position and reduces concerns around future funding requirements. The US\$2bn financing, including equity placement and convertible bonds, provides additional resources for model development, infrastructure investment and commercialization.

We view the financing as a positive step in extending MiniMax's ability to compete. As the industry becomes more capital intensive, access to sufficient resources is increasingly important for sustaining multiple model cycles. The transaction reduces pressure around future training expenditure and provides more flexibility in allocating resources across research, infrastructure and commercialization.

However, we believe the key investment question remains whether MiniMax can translate additional resources into stronger model capability. Similar to peers, long-term competitiveness will depend on technical roadmap, research talent and execution efficiency alongside capital availability. Financing improves the company's ability to participate in the competition, while future model progress will determine whether MiniMax can improve its relative positioning.

The equity component of the transaction also creates meaningful dilution – placement on 11% of total shares, convertible bonds at 6% of total shares. Such near-term financial benefit needs to be weighed against share dilution and the limited immediate impact on revenue growth.

MiniMax has established strengths in multimodal models, consumer applications and international expansion. However, recent pricing dynamics highlight the importance of demonstrating differentiated model capability. Following the M3 launch, pricing adjustments suggested that sustained monetization upside requires clearer evidence of model superiority and user willingness to pay.

We would become more constructive if future model releases demonstrate clear capability improvement and meaningful catch-up versus peers. Until then, we believe the risk-reward remains balanced.

## Estimate changes

We make no changes to MiniMax's forward P&L forecasts as the recent financing didn't give us higher conviction of the forward monetization path; on the other hand, we reflect the cost of financing with 11% of total shares on placement and 6% of shares if 100% of converted bonds are converted. Accordingly, we lower our adjusted net EPS by 4% for 2026E and 20% for 2027-30E. We consequently lower our Dec-26 price target to HK\$240 from HK\$300, still based on 30x 2030E P/E discounted back using a 15% WACC.

Table 3: Estimate changes summary for MiniMax

<table><tr><td>Estimate changes (US$mn)</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>383</td><td>830</td><td>1,652</td><td>3,194</td><td>6,633</td></tr><tr><td>Old</td><td>383</td><td>830</td><td>1,652</td><td>3,194</td><td>6,633</td></tr><tr><td>% change</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Operating profit</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>(932)</td><td>(1,217)</td><td>(1,353)</td><td>(1,148)</td><td>(41)</td></tr><tr><td>Old</td><td>(932)</td><td>(1,217)</td><td>(1,353)</td><td>(1,148)</td><td>(41)</td></tr><tr><td>% change</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Adjusted net profit</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>(432)</td><td>(948)</td><td>(1,003)</td><td>(647)</td><td>633</td></tr><tr><td>Old</td><td>(432)</td><td>(948)</td><td>(1,003)</td><td>(647)</td><td>633</td></tr><tr><td>% change</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Adjusted EPS</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>(1.30)</td><td>(2.34)</td><td>(2.47)</td><td>(1.60)</td><td>1.56</td></tr><tr><td>Old</td><td>(1.36)</td><td>(2.92)</td><td>(3.09)</td><td>(2.00)</td><td>1.95</td></tr><tr><td>% change</td><td>-4%</td><td>-20%</td><td>-20%</td><td>-20%</td><td>-20%</td></tr></table>

Source: JPM estimates (data as of Jul 10, 2026)

## Overweight

2513.HK,2513 HK
Price (10 Jul 26): HK\$1,640.00

## ▲ Price Target (Dec-26): HK\$2,400.00 Prior (Dec-26): HK\$2,000.00

## Hong Kong Internet

Internet
Olivia Xu AC
(86-21) 6106 6138
olivia.w.xu@JPM.com
SAC Registration Number: S1730525060001
JPM Securities (China) Company Limited

Key Changes (FYE Dec)

<table><tr><td colspan="4">Key Changes (FYE Dec)</td></tr><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E (Rmb)</td><td>(8.20)</td><td>(7.91)</td><td>3.6%</td></tr><tr><td>Adj. EPS - 27E (Rmb)</td><td>(6.71)</td><td>(5.40)</td><td>19.4%</td></tr></table>

## Half Yearly Forecasts (FYE Dec)

<table><tr><td colspan="4">Adj. EPS (Rmb)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>H1</td><td>(11.09)</td><td>(5.07)</td><td>(4.65)</td></tr><tr><td>H2</td><td>(9.11)</td><td>(2.89)</td><td>(0.76)</td></tr><tr><td>FY</td><td>(19.95)</td><td>(7.91)</td><td>(5.40)</td></tr></table>

Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>98</td><td>94</td><td>94</td><td>86</td><td></td></tr><tr><td>Growth</td><td>31</td><td>100</td><td>100</td><td></td><td></td></tr><tr><td>Momentum</td><td>100</td><td></td><td></td><td></td><td></td></tr><tr><td>Quality</td><td>86</td><td></td><td></td><td></td><td></td></tr><tr><td>Low Vol</td><td>100</td><td></td><td></td><td></td><td></td></tr></table>

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates.

## Zhipu AI

## Financing improves execution visibility across model development and commercialization; PT to HK\$2,400

We view Zhipu's financing positively as it reduces potential execution constraints across both model development and commercialization. Additional capital does not independently create model leadership, and Zhipu's long-term positioning will continue to depend on its research direction, talent quality and organizational execution. However, given Zhipu's recent model progress and commercial momentum, additional resources improve confidence around the company's ability to execute against future opportunities.

## Investment Thesis, Valuation and Risks

## Knowledge Atlas Techn

[中间内容因长度限制已省略]

e subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into

which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
