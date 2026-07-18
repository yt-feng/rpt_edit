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
# US Communications Equipment

## 2Q26 Earnings Preview: Investor Focus on Supply Constraints

## CITI'S TAKE

We remain constructive on multi-year networking infrastructure growth driven by AI with focus on “stage 4” or early adoption of scale up optics with NPO and CPO (see Figure 1). Our top buy-rated picks into earnings are LITE, KEYS, & CIEN and least preferred pick is CLS. Our stock rankings are influenced by the impact of constrained supply environments, especially silicon/lasers, and impact to the overall gross margins (see Figure 2).

Big Five Hyperscale 2026 Capex — The outlook for aggregate FY26 Big Five cloud data center capex has moved meaningfully higher (+16%) compared to April expectations with Citi estimates for 3 of the big 5 revised higher. Current Citi analysts' projections point to aggregate data center capex growth of >80% Y/Y in 2026 and more than 30% Y/Y in 2027. Ahead of Q2 reporting, four of the big five cloud SPs are expected to see an acceleration in 2026 data center capex growth vs 2025, according to Citi estimates compared to just one (Google) into Q1 results. In addition, three of the big five are now forecasted to grow 2026 capex above their two-year average growth rate, enough to shift the group on aggregate. As a result, we view the current capex environment as incrementally more positive for our networking coverage. Within our networking coverage: CLS's top 3 customers, GOOGL, META, and AMZN, were 58% of FY25 sales; ANET's top 2 customers were MSFT and META at 42% of FY25 sales; 2 hyperscalers were >30% of CIEN's Apr-Q sales.

Front End Switch — Q1 26 front end data center switch market grew by mid 20s% Y/Y, per Dell'Oro, ahead of their expectations. Their FY26 outlook was raised to mid-teens growth Y/Y due to increasing prices, higher growth related to AI front end, and infrastructure investments ahead of AI deployments. ANET remained the market leader followed by CSCO.

Al Back-End switch — Q1'26 Ethernet back-end switch market was up more than 100% Y/Y and reached >\$3.7B, according to Dell'Oro. The market is on track to double Y/Y in 2026. CLS led in 1Q, followed by NVDA, ANET, white box and CSCO.

Campus Switch — Q1 campus switch market grew mid-teens Y/Y on volume and price increases, according to Dell'Oro. CSCO maintained its $>50\%$ share while ANET switch sales grew $>20\%$ Y/Y for the $2^{nd}$ consecutive Q, resulting in $\sim3\%$ share.

Optical Transport — Q1 optical transport market grew 20% Y/Y, according to Dell'Oro reflecting high teens growth in optical transport systems and >30% growth in ZR/ZR+. CIEN led the market with >25% share, up more than 300bps Y/Y, while CSCO was #5 with MSD share, up 200bps Y/Y.

Celestica (CLS) will be the first in our coverage to report 2Q26, on July 27.

Atif Malik $^{AC}$ +1-415-951-1892
atif.malik@citi.com

Papa Sylla
+1-212-816-9476
papa.sylla@citi.com

Adrienne Colby

+1-212-816-8975

adrienne.colby@citi.com

## 2Q26 Earnings Preview

1. Citi's AI Infrastructure Playbook

2. Stock Rankings

3. Citi Cloud AI Capex Model

4. Key End markets

## 1. Citi's AI Infrastructure Playbook

Figure 1. Stages of AI - Focus on Stage 4  
![](images/ed6f8195e6028fbc794e2e03c3f495ce75512e129faf133c4d4d7cb4a9242d6a.jpg)

Citi's AI infrastructure playbook divides networking into five stages. Following InfiniBand to Ethernet adoption, acceleration of ASIC solutions driving the need for intra and inter server networking, and data center interconnect stages, we are focused on “stage 4” or early adoption of scale up optics with NPO or CPO.

## 2. Stock Rankings

Figure 2. Citi Relative Stock Rankings (Highest to Lowest Y/Y Gross Margins)  
![](images/360e1783c0fe52957860cecda527cadf6dbd39ad4f51bd60ab2ad29772dd9a2f.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

We continue to expect supply shortages, including silicon switches, memory, and lasers to impact the networking equipment supply chain negatively in 2H26. Our relative stock rankings are influenced by a) our concerns on the impact of the above component shortages, product mix, and the indirect impact to the gross margins, and b) exposure to “stage 4” to drive above average hyperscale capex growth in 2026.

## 3. Citi Cloud Data Center Capex

Figure 3. Big 5 Cloud Capex

<table><tr><td>$ millions</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>AWS</td><td>53,436</td><td>90,080</td><td>154,689</td><td>197,231</td><td>243,897</td></tr><tr><td>Meta Compute</td><td>39,225</td><td>72,215</td><td>138,847</td><td>171,460</td><td>204,626</td></tr><tr><td>GSP</td><td>52,535</td><td>91,447</td><td>188,080</td><td>254,532</td><td>319,668</td></tr><tr><td>Azure</td><td>67,746</td><td>108,836</td><td>179,428</td><td>269,781</td><td>300,879</td></tr><tr><td>OCI</td><td>10,241</td><td>37,637</td><td>69,881</td><td>85,083</td><td>91,340</td></tr><tr><td>Big Five US</td><td>$223,183</td><td>$400,215</td><td>$730,926</td><td>$978,087</td><td>$1,160,410</td></tr><tr><td>Year-over-Year (%)</td><td>70%</td><td>79%</td><td>83%</td><td>34%</td><td>19%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Company Reports

Figure 4. Growth outlook for Big Five Cloud Capex

<table><tr><td>Capex Y/Y %</td><td>2024</td><td>2025</td><td>2026E</td></tr><tr><td>AWS</td><td>70%</td><td>69%</td><td>72%</td></tr><tr><td>Meta Compute</td><td>40%</td><td>84%</td><td>92%</td></tr><tr><td>GSP</td><td>63%</td><td>74%</td><td>106%</td></tr><tr><td>Azure</td><td>97%</td><td>61%</td><td>65%</td></tr><tr><td>OCI</td><td>112%</td><td>268%</td><td>86%</td></tr><tr><td>Big Five US</td><td>70%</td><td>79%</td><td>83%</td></tr></table>

<table><tr><td>Capex Y/Y %</td><td>2024</td><td>2025</td><td>2026E</td><td>AVG (3yr)</td></tr><tr><td>AWS</td><td>70%</td><td>69%</td><td>72%</td><td>70%</td></tr><tr><td>Meta Compute</td><td>40%</td><td>84%</td><td>92%</td><td>72%</td></tr><tr><td>GSP</td><td>63%</td><td>74%</td><td>106%</td><td>81%</td></tr><tr><td>Azure</td><td>97%</td><td>61%</td><td>65%</td><td>74%</td></tr><tr><td>OCI</td><td>112%</td><td>268%</td><td>86%</td><td>155%</td></tr><tr><td>Big Five US</td><td>70%</td><td>79%</td><td>83%</td><td>77%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Company Reports

The outlook for aggregate FY26 Big Five cloud data center capex has moved meaningfully higher (+16%) compared to expectations in April with Citi estimates for META, MSFT, and AMZN revised higher. We note current Citi analysts' projections point to aggregate data center capex growth of >80% Y/Y in 2026 and more than 30% growth in 2027.

Ahead of Q2 reporting, four of the big five cloud SPs are expected to see an acceleration in 2026 data center capex growth vs 2025, according to Citi estimates compared to just one (Google) into Q1 results. In addition, three of the big five are now forecasted to grow 2026 capex above their two-year average growth rate, enough to shift the group in aggregate. As a result, we view the current capex environment as incrementally more positive for our networking coverage.

■ Within our networking coverage, CLS's top three customers are GOOGL, META, and AMZN at 58% of FY25 sales and ANET's top two customers are MSFT and META at 42% of FY25 sales. In CIEN's April-Q, two hyperscalers accounted for just over one-third of sales.

## 4. Key End Markets

## Data center – Front end switch

\- Q1 26 front end data center switch market grew by mid-20s% Y/Y, ahead of Dell'Oro's low-teens expectations.

\- Dell'Oro's outlook for 2026 was raised from mid-single digit to mid-teens growth Y/Y due to increasing prices, higher growth related to AI front end, and infrastructure investments ahead of AI deployments.

\- In the Q, top 4 cloud grew by $>50\%$ Y/Y and accounted for nearly 1/3 of the market; all cloud segments (top 4, top 3 China, tier 2, rest of cloud) combined grew by $>40\%$ Y/Y and were more than $50\%$ of the front-end data center switch market.

– Large enterprise segment grew slower than the overall market and made up just over 1/3rd of the market.

\- 400G accounted for mid-40s% of the market by sales while 800G was mid-single digits share of the market.

\- ANET remained the top vendor in the market with nearly 3pt lead over #2 CSCO due to its strong position with cloud customers; ANET had nearly 1/3 of the top 4 cloud SP segment, nearly 8pts ahead of the next largest vendor. ANET was the 2nd largest provider to large enterprises and gained modest share in the quarter. 800G accounted for mid-teens % of ANET's mix.

\- CSCO saw strong growth with cloud customers, where it gained nearly 3pts of share but remained the 5th largest cloud vendor, driven mostly by gains in the rest of cloud segment followed by top 4 cloud. Enterprise sales still account for $>70\%$ of CSCO's data center switch sales

\- CLS was the fifth vendor in the market with mid-teens share, essentially flat Y/Y. With top 4 cloud SPs the company was edged out of 2nd place to 3rd by Accton. 800G accounted for low-teens % of CLS's quarterly mix.

\- Dell'Oro is now reporting Accton separately from the other white box category. Accton is the 3rd largest player in the market and gained 3pts of share Y/Y.

## Data center – AI back-end switch

\- According to Dell'Oro, Q1'26 Ethernet back-end switch market was up more than 100% Y/Y and reached >\$3.7B.

\- The InfiniBand back-end switch segment grew by $>200\%$ Y/Y to $>$ 2B.

\- The Ethernet back-end switch market is on track to more than double Y/Y in 2026 to nearly \$22B.

\- 800G made up approximately $80\%$ of Ethernet sales ( $\sim 70\%$ of ports.)

\- 1.6T was less than $1\%$ of the market and remains in pre-production, but Dell'Oro expects a ramp in 2H with shipments initially to Amazon and Google then in 1H27 to Meta with CPO.

\- CLS was the top vendor in the quarter with $>25\%$ share due to its positioning with top 4 cloud customers, which as a segment is over half of the market. However, CLS did lose $\sim 5$ pts Y/Y in overall share, reflecting meaningful share loss in top 4 cloud, mostly to CSCO. CLS is the only vendor shipping 1.6T, although in very small sampling volumes.

\- NVDA #2 player with mid-20s% share. Dell'Oro notes they plan to start shipping CPO on Spectrum-X in 2H.

\- ANET was the third largest vendor in Q1 with low teens share and CSCO ranked $5^{\text{th}}$ with high single digits share.

\- CSCO wasn't in the market a year ago but was the $5^{\text{th}}$ vendor in the Q1 market with $\sim 8\%$ overall share and $\sim 13\%$ with top 4 cloud customers. Cisco's growth is largely tied to Meta deployments, according to Dell'Oro.

## Campus Switch

\- Dell'Oro estimates the 1Q campus switch market grew mid-teens Y/Y to \~\$5B, reflecting volume and price increases.

\- Increasing ASPs and extending lead times are expected to weigh on volumes over the balance of the year with Dell'Oro currently anticipating MSD growth Y/Y in 2026.

– CSCO remained the leading vendor with over 50% share that was essentially unchanged Y/Y.

\- HPE was the #2 player in the market with low teens share, which was flat Y/Y adjusted for JNPR. Huawei was the third largest vendor in the market with high single digits share (essentially flat Y/Y).

\- ANET remained the 6th ranked vendor with just over $3\%$ market share but saw its campus switch sales grow by more than $20\%$ Y/Y for the second consecutive quarter.

## Optical Transport

\- Q1 optical transport market grew by 20% Y/Y to >\$4B, according to Dell'Oro.

\- Transport systems grew by high teens Y/Y.

\- ZR/ZR+ pluggable revenues were up high 30s% Y/Y.

\- Cloud customers accounted for over one-third of the market, with quarterly revenues up \~50% Y/Y.

\- Declines in the China market, due to a pivot in compute infrastructure to traditional telecom infrastructure, is amplifying typical weak seasonality for Huawei and ZTE.

\- CIEN was the top vendor in the market with $>25\%$ share and revenues grew by nearly $40\%$ Y/Y due to its strong positioning with cloud SPs. CIEN gained 100bps of share in both ZR/ZR+ pluggables and DCI applications.

\- NOK was the 3rd largest vendor. While Q1 is seasonally weaker for NOK, sales grew $>20\%$ Y/Y and the company gained $\sim 100$ bps, adjusted for Infinera in the prior period, due to demand from traditional carriers.

\- CSCO sales grew by high 80s% Y/Y on higher cloud SP sales. The company gained >200bps of share and was the 5th ranked vendor in the market. Acacia had the highest share in pluggables based on shipments for both 400 ZR/ZR+ and 800 ZR/ZR+.

\- Dell'Oro raised its FY26 outlook from +10% to mid-teens % Y/Y growth.

## Companies Mentioned:

Arista Networks (ANET.N; US\$171.92; 1; 15 Jul 26; 16:00) | Astera Labs, Inc (ALAB.O; US\$350.62; 1; 15 Jul 26; 16:00) | Celestica (CLS.N; US\$334.77; 1; 15 Jul 26; 16:00) | Ciena (CIEN.K; US\$418.46; 1; 15 Jul 26; 16:00) | Cisco Systems (CSCO.O; US\$111.77; 1; 15 Jul 26; 16:00) | Coherent Corp (COHR.K; US\$299.38; 1; 15 Jul 26; 16:00) | Keysight Technologies (KEYS.N; US\$322.71; 1; 15 Jul 26; 16:00) | Lumentum Holdings Inc (LITE.O; US\$752.0; 1; 15 Jul 26; 16:00)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>Citi Global Markets Inc. or its affiliates has a net long position of 0.5% or more of any class of common equity securities of Astera Labs, Inc.</td></tr><tr><td>Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Ciena.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Celestica,Ciena,Cisco Systems,Keysight Technologies.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Arista Networks,Celestica,Ciena,Cisco Systems,Coherent Corp,Keysight Technologies,Lumentum Holdings Inc in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Celestica,Ciena,Cisco Systems,Keysight Technologies.</td></tr><tr><td>Citi Global Markets Inc. or its

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
