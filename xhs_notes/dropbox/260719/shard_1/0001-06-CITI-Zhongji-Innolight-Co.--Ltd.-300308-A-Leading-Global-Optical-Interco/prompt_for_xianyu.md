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
# Zhongji Innolight Co., Ltd.

## A Leading Global Optical Interconnects Solution Provider

## CITI'S TAKE

Innolight is the global No.1 optical interconnects solution provider as of 2025 by revenue, according to LightCounting. We believe the company's (1) comprehensive product offering, (2) scalable production capacity, (3) cutting-edge technology advancement and R&D capability, (4) flexible and resilient supply chain, and (5) strong relationships with global leading CSP/AI customers will support its leading position in the AI era. We forecast Innolight can deliver $129\% / 149\%$ revenue/net profit CAGR in 2025-28E thanks to rapid capacity ramp, improving product mix (high-speed products), rising adoption of SiPh technology, and operating leverage.

Robust optical interconnects demand — Global cumulative AI capex is forecast to reach up to US\$6.1trn over 2026E-30E, from US\$0.9trn from 2021-25, per CIC. The global datacom market could reach c.US\$98.6bn by 2030E, on LightCounting projections. In 2025, C.77% of datacom optical interconnects were demanded from scale-out network and 22% from front-end network and others, and this is forecast by LightCounting to grow at 19.4% and 21.6% CAGR during 2026E-30E respectively. Scale-across network is a niche market, which is forecast by LightCounting to grow from 1% of market in 2025 to 7% in 2030E with a CAGR of 117.4%. Scale-up network will require many optical interconnects, as it is replacing copper interconnects within the rack; LightCounting projects this market to grow at 297.7% in the period.

High-speed migration in datacom optics — Per LightCounting and CIC, 1.6T is emerging in 2025, accounting for c.4% of the global datacom optical interconnect market, with forecast expansion to c.45% of market by 2030E. 3.2T is seen by LightCounting and CIC emerging in 2027E with initial contribution of 0% likely and forecast expansion to 32% of market by 2030E. 800G became a mainstream product in 2025/26 with contribution of 51%/48%, surpassing 400G and likely peaking out and shrinking to 16% by 2030E given rise of 1.6T and 3.2T. We estimate Innolight could ship 30.1mn / 60.2mn / 96.4mn optical transceivers in 2026E / 27E / 28E, up 43%/100%/60% YoY, with high-speed optical transceivers (800G or above) contributing 26.0mn/57.0mn/94.0mn or 86%/95%/98% of total shipments.

Leader with strong competitive edge — Innolight ranked as the No.1 optical interconnect solutions provider globally for five consecutive years since 2021, with market share of 21.2% by revenue in 2025. The company is the first to launch 400G/800G/1.6T optical transceivers globally with its leadership in SiPh-based optical transceiver. We believe Innolight's (1) comprehensive product offering, (2) scalable production capacity, (3) cutting-edge technology advancement and R&D capability, (4) flexible and resilient supply chain, and (5) strong relationship with global leading CSP/AI customers will support its leading position in the AI era.

Estimates revisions — See details of our revised estimates in the “Financial Analysis” section below.

Valuation — We believe Innolight would tend to be valued at a premium to direct peers TFC, DSBJ, and Eoptolink, with average 2027E P/E of 15.4x, given its market leadership, early SiPh penetration and exposure to all US CSPs and AI customers.

Key risks — Customer concentration, intensifying competition, demand cyclicality, technology risks, supply chain and manufacturing risks, geopolitical/trade risks.

Kyna Wong $^{AC}$

+852-2868-7820

kyna.wong@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

## Contents

A Leading Optical Interconnects Solution Provider 3
Business overview 3
A leader and enabler 3
Comprehensive product offerings 4
Scalable production supports time-to-market & global coverage 4
Cutting-edge technologies and strong R&D 5
Flexible and resilient supply chain 6
Strong relationships with industry-leading customers 6
Company history 7
Industry Overview & Outlook 8
Riding on Promising Optical Interconnects Demand in the AI Era 8
Global AI capex 8
Optical interconnects market 8
Financial Analysis 12
Estimates revisions 12
Revenues, volumes, and ASPs 12
Margins 13
R&D 14
Profits 14
Financial statements 15
Valuation Analysis 18
P/E analysis 18
Valuation comps 20
Key Risks 21
Appendix: Management & Key Shareholders 23
Management profiles 23
Shareholder structure 24
Appendix A-1 25

# A Leading Optical Interconnects Solution Provider

## Business overview

Zhongji Innolight, founded in 2008, is now a world leader in development of optical transceivers. It provides a wide range of high-speed optical solutions for optical communications networking, especially for AI and data center applications by global top-tier data center operators and cloud service providers. In addition, Innolight provides optical transceivers solutions for enterprise data networking applications, metro and long-haul transport networking, and mobile-access networking applications.

## A leader and enabler

Innolight ranked No.1 in the optical interconnect solutions provider globally for four consecutive years since 2021, with market share of 21.2% by revenue in 2025. The company is the first to launch 400G/800G/1.6T optical transceivers globally with its leadership in SiPh-based optical transceiver.

![](images/75e25b32f479e863d5c191465a6507b1d00c806bfd60599ce5c80231b7414071.jpg)

Figure 2. Global Ranking of Top-5 Optical Interconnects Solution Providers, 2024

<table><tr><td>Company Name</td><td>Market share (%)</td></tr><tr><td>The Company</td><td>21.20%</td></tr><tr><td>Company A</td><td>14.00%</td></tr><tr><td>Company B</td><td>12.10%</td></tr><tr><td>Company C</td><td>5.00%</td></tr><tr><td>Company D</td><td>4.70%</td></tr><tr><td colspan="2">© 2026 Citi Inc. No redistribution without Citi’s written permission.Source: Citi, LightCounting, CIC</td></tr></table>

## Comprehensive product offerings

The company has a comprehensive and versatile product offering, covering datacom and telecom use cases, short-range/ long-range/ ultra-long-range transmission distances, and various form factors including OSFP (octal small form factor pluggable), QSFP-DD (quad small form factor pluggable double density), QSFP 28 (quad small form factor pluggable 28), CFP2 DCO (C form factor pluggable 2 - digital coherent optics) etc. as well as various transmission speed including 10G to 1.6T and beyond that XPO, NPO, CPO, etc.

The company was the early mover to commence offering SiPh at scale and currently is the market leader. It also demonstrated 800G LR2 OSFP coherent compact optical transceivers and is working on Coherent-Lite solution for future scale across solutions. The company also showcased the industry's first 12.8T 8xDR8 XPO optical transceiver at OFC 2026. For advanced packaging optics, Innolight commercialized 800G and 400G LPO optical transceivers and has achieved R&D progress with customers leveraging accumulated capabilities in SiPh technology for NPO and CPO solutions.

![](images/efd2eafd18ce86885c9ef7e462ed3e80a2873fc9c001d81b1af09fe4e26c3e6c.jpg)

## Scalable production supports time-to-market & global coverage

In order to serve global customers, Innolight has several production bases including Suzhou, Chengdu, Tongling, Taiwan, and Thailand, with 28.1mn units of optical transceivers production capacity in 2025, 2.9x growth vs. 2023. Overseas capacity accounted for 71% of total production capacity in 2025, and the remaining is from mainland China. We expect Innolight will expand its capacity 100%/100%+ YoY in 2026E/27E in order to fulfill rising demand.

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Company Reports  
Figure 4. Innolight – Production Capacity and Utilization Rate  
![](images/5d612a2bb67c89ddd6c2fb7190065169234958451bb6e454825e1affaab0e29e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Company Reports

Figure 5. Innolight – Manufacturing Sites in Asia  
![](images/cdf1ebec152304a6ef5daaa101d96f8d19dc6326b9a1aa48696e532bf795ca49.jpg)

The company has built up differentiated new product introduction (NPI) processes, with highly adaptive equipment and streamlined production processors, supported by automation and AI applications, to drive rapid scaling to mass production.

## Cutting-edge technologies and strong R&D

Innolight is a market leader in Silicon Photonics (SiPh). Its R&D investment in SiPh-based optical transceivers started from 2017, making it an early mover to commercialize SiPh at scale. Now, $50\%+$ of high-speed products utilize SiPh technology. The company also demonstrated its R&D capabilities in cutting-edge technologies, including 800G LR2 OSFP coherent compact optical transceivers, showcasing the industry's first 12.8T 8x DR8 XPO optical transceiver at OFC 2026, commercialized 800G and 400G LPO optical transceivers for scale-out network, and R&D for NPO/CPO by leveraging accumulated capabilities in SiPh technology.

According to LightCounting and CIC, SiPh penetration could reach 73% by 2030E from 38% in 2025. We believe Innolight, as a leader in SiPh optical interconnect solutions, will significantly benefit from the booming growth in SiPh products. Products utilizing SiPh technology constituted approximately 70% of Innolight's high-speed product portfolio by revenue in 1Q26.

Figure 6. Rising Penetration of SiPh in Global Datacom Optical Interconnect Market  
![](images/eaf724896cfa944b29474b779ebbebea7fafc8baaebc32ae90752d24402b7fb8.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, LightCounting, CIC

## Flexible and resilient supply chain

Innolight generally procures key components (including PMIC, DSP, EML) from global premier suppliers, but at the same time, it cultivates domestic supply chains to further diversify its supplier base. The company also uses its strategic investments and partnerships to prepare for advanced technologies and global expansion.

We believe Innolight has a unique edge in supply-chain management, including global, broad-based supplier networks with low concentration in single suppliers and strong bargaining power. The company uses multi-year framework agreements to secure critical components. Long-term strategic collaboration is important to provide resilience in supply-chain procurement, as a result driving an excellent delivery track record and cost-competitive supply to its customers.

## Strong relationships with industry-leading customers

90% of the company's revenue came from non-China markets in 2025. The company is serving a majority of global leading CSPs and AI computing solutions providers, which are mostly the world's leading players. Innolight has built up long-term customer partnerships backed by seamless alignment on technology and product roadmaps. The company is able to provide unique insights on emerging industry trends as customers upgrade AI infrastructure. We think customers also see value in Innolight's positioning as market leader driving industry innovation and delivering sustained value to partners.

## Company history

Figure 7. Innolight – Key Development Milestones

<table><tr><td>Year</td><td>Key milestones</td></tr><tr><td>2008</td><td>Inception in Silicon Valley and SuzhouEarly investment from US investors including Acorn Campus, Monet Investments, Cascade Capital</td></tr><tr><td>2009</td><td>Launched 10G optical transceiver products</td></tr><tr><td>2011</td><td>Began cooperation with the first top-tier CSP customer</td></tr><tr><td>2012</td><td>Launched 40G optical transceiver products</td></tr><tr><td>2014</td><td>Received investments from Google Capital, Lightspeed China PartnersLaunched 100G optical transceiver products</td></tr><tr><td>2018</td><td>Expanded global footprint by establishing Singapore subsidiaryLaunched the first in the industry 400G optical transceiver products</td></tr><tr><td>2020</td><td>Launched the first in the industry 800G optical transceiver products</td></tr><tr><td>2021</td><td>Became world&#x27;s largest provider of optical interconnect solutions</td></tr><tr><td>2022</td><td>Thailand factory commenced operation</td></tr><tr><td>2023</td><td>Launched the first in the industry 1.6T optical transceiver products</td></tr><tr><td>2025</td><td>Annualized production capacity exceeded 28mn units</td></tr><tr><td colspan="2">© 2026 Citi Inc. No redistribution without Citi&#x27;s written permission.</td></tr><tr><td colspan="2">Source: Citi, Company Reports</td></tr></table>

# Industry Overview & Outlook

# Riding on Promising Optical Interconnects Demand in the AI Era

## Global AI capex

According to CIC, global capital expenditure on AI amounted to US\$0.9trn between 2021 and 2025. Moving forward, investments in AI are projected by CIC to continue to grow substantially, reaching US\$6.1trn over 2026E to 2030E, representing an increase of more than five times compared to the prior five-year period. CIC expects the contribution of optical interconnects should also increase as a percentage of global AI capex from 5% in 2025E, driven by high-bandwidth, low-latency and energy-efficient data transmission, changes in datacenter network architecture, as well as increasing scale of computing clusters and higher interconnect density.

## Optical interconnects market

According to LightCounting and CIC, the global optical interconnects market reached US\$24.8bn in 2025 and is forecast to reach US\$111.0bn in 2030E, with a CAGR of 31.6% (2026E-30E). The expansion is expected to be led by datacom, where LightCounting projects the market to scale from US\$19.4bn in 2025 to US\$98.6bn in 2030E, delivering a CAGR of 33.8% over 2026E to 2030E. The telecom optical interconnects market is forecast by LightCounting to grow at 18.4% CAGR (2026E-30E) to US\$12.4bn by 2030E.

Figure 8. Global Optical Interconnects Industry by End-Markets  
![](images/2f50b265cdbf41dcb907b18bb57557c95c6f57e6945e999ce054a57604cf7bfb.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CIC, LightCounting

In data center networks, optical interconnects are widely applied between switch-to-switch and switch-to-server connections, across all application scenarios such as scale-out network, scale-up network, front-end network, and scale-across network etc. to provide high-speed, low-latency connectivity.

Figure 9. Global Datacom Optical Interconnects Market by Transmission Speed to Reach  
![](images/b7a20af611259f7978055e6e7bb96b0047974ab0e00eb750885e71acd62f4554.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, LightCounting, CIC

Figure 10. Global Datacom Optical Interconnects Market by Networking Scenarios  
![](images/a0cf6db7a8ba75bde48a918150b732b597a13e81af1a802260b3454332c43351.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, LightCounting, CIC

According to LightCounting, 77% of datacom optical interconnects were demanded from scale-out network and 22% from front-end network in 2025, and this is forecast to grow at 19.4% and 21.6% CAGR during 2026E-30E respectively. Scale-across network is a niche market which is forecast by LightCounting to grow from 1% of market in 2025 to 7% in 2030E with a CAGR of 117.4%. Scale-up network will require many optical interconnects as it is replacing copper interconnects within the rack; it is projected by LightCounting to grow at 297.7% in the period.

Increasing data transmission bandwidth, speed, and density are driving accelerat

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing

such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
