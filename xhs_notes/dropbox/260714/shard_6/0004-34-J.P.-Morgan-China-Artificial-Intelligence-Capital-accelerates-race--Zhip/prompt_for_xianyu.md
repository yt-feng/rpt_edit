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

<table><tr><td>Estimate changes (US$mn)</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>383</td><td>830</td><td>1,652</td><td>3,194</td><td>6,633</td></tr><tr><td>Old</td><td>383</td><td>830</td><td>1,652</td><td>3,194</td><td>6,633</td></tr><tr><td>% change</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Operating profit</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>(932)</td><td>(1,217)</td><td>(1,353)</td><td>(1,148)</td><td>(41)</td></tr><tr><td>Old</td><td>(932)</td><td>(1,217)</td><td>(1,353)</td><td>(1,148)</td><td>(41)</td></tr><tr><td>% change</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Adjusted net profit</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>(432)</td><td>(948)</td><td>(1,003)</td><td>(647)</td><td>633</td></tr><tr><td>Old</td><td>(432)</td><td>(948)</td><td>(1,003)</td><td>(647)</td><td>633</td></tr><tr><td>% change</td><td>0%</td>

[中间内容因长度限制已省略]

es discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into

which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
