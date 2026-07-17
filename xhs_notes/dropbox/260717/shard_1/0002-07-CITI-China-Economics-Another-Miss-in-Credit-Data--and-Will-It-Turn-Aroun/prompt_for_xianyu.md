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
# China Economics

## Another Miss in Credit Data, and Will It Turn Around?

## CITI'S TAKE

China's money and credit data for June missed expectations, hardly a surprise now with the miss in GDP published earlier today. Household and corporate credit demand stayed subdued, while lagging government bond issuance weighed on new TSF further. We maintain our view of incremental policies ahead, with a 10bps cut from the PBoC as early as July and acceleration in fiscal policy deployment. We are, however, cautious about whether credit numbers could turn around. The boost from government bonds issuance could be offset by weakness in credit demand. Credit impulse could stay negative in 26H2E amid the K-shaped economy.

Xinyu Ji $^{AC}$ +852-2501-2792
xinyu.ji@citi.com

Xiangrong Yu $^{AC}$

+852-2501-2754

xiangrong.yu@citi.com

Money and credit data came in below consensus expectations in June. It is hardly a surprise now with the GDP miss and investment slump released by the NBS earlier. New RMB Loans came in at RMB1,610bn (Citi/Mkt: RMB1,800/1,950bn) compared with RMB2,240bn last June. New Total Social Financing missed expectations at RMB3,364bn (Citi/Mkt: RMB3,500/3,702bn), vs. RMB4,225bn last June. Risk appetite remains subdued for private sector, with lagging fiscal deployment further weighing on new TSF.

■ Household loans turned positive, with short-term loans at RMB106bn and long-term loans at RMB158bn, lower than RMB262bn and RMB335bn last June, respectively.

■ Corporate credit demand remained low, with combined long-term loans and long-term loans \~RMB289bn lower than last June – the former was RMB560bn vs. RMB1,018bn last June and bond financing reached RMB404bn vs. RMB242bn. Short-term loans and bills financing still supported the headline number with the PBoC’s window guidance in the third consecutive month.

■ Government financing recorded RMB769bn in June, the lowest reading within the year. Funds deployment has likely accelerated, with drawdown of fiscal deposits at RMB939bn vs. RMB820bn last June.

Credit and money growth decelerated with the soft numbers. Growth of outstanding TSF decelerated to 7.4%YoY, a new all-time low. Both M1 and M2 growth softened: M1 growth dipped to 4.0%YoY as a higher base kicked in (Citi/Mkt: 3.5/4.9%YoY), a one-year low, and M2 growth dropped to 8.0%YoY (Citi/Mkt: 8.1/8.5%YoY), a low reading within the year. Deceleration of M1 could continue within the year, with M1-M2 gap declining further, hinting at plateauing and decelerating PPI inflation going forward.

We maintain our view for incremental policy ahead after the GDP miss earlier today. For monetary policies, we see 10bps cut in LPR rates as early as this July with the PBoC's earlier finetuning of its interest corridor and newly set O/N reverse repo. The PBoC vowed supportive policies at a press conference today (SCIO, Jul $15^{\text{th}}$ ), listing its tools for liquidity management, reiterating to keep financing cost low and pledging to expand the quota for structural policies if necessary – the last as the most explicit forward guidance on incremental policies from the central bank today. Pressure on headline number would still prompt the PBoC to act in our view, and we watch upcoming Politburo meeting for more comprehensive policy signals.

Will credit rebound follow with incremental measures? We tend to be more cautious. Government financing is the most certain driver for new TSF in 26H2. Remaining quota for government bonds is RMB7.45trn, providing a boost of RMB1.3trn compared with actual issuance of RMB6.18trn in 25H2. This part could be offset by weakness in organic credit demand: total of household loans and corporate long-term loans and bond financing were RMB2.2trn lower in 26H1 compared with 25H1, and we don't see immediate catalysts for a rebound. Fiscal policy implementation may slow the fall in credit growth but not reverse it. Credit impulse could stay negative throughout 26H2E.

Figure 1. Money and credit growth decelerated in June with soft credit data  
![](images/4b97eec0964f9601d397dd271208c830e2f496d360fb3f6b8dacb659c9145ba4.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: PBoC, Wind, Citi

Figure 2. Credit impulse could stay negative in 26H2E as we expect fiscal policies to cushion not reverse the fall  
![](images/c4e18a415a09040200c60c75d8b16f75d0e80d76d46e5d5efaa84ca36f8a95f8.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, PBoC, Wind, Citi

Figure 3. Short-term lending and bills financing still helped with the loan number  
![](images/32e01eb42b78369e2a1170a8ac21af2579017520708852b9908e16a40c62598c.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: PBoC, Wind, Citi

Figure 4. Pace of government bond issuance weighed further on new TSF in June  
![](images/4337b0fba7ce4923190e1b166f8a9444e3cc7eee2b2345499b29e4398a2f7b88.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: PBoC, Wind, Citi

Figure 5. Household risk appetite stayed subdued even with a seasonal rebound in new loans  
![](images/78e4b83baf86e6bc248e182aa34ec917adbc16980a52c14919dc7cf58a5ae801.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: PBoC, Wind, Citi

Figure 6. Corporate credit demand was soft even after adding bonds to long-term loans  
![](images/192cb7a392ed9f020e0e51ee93c0782a0642b3e55123ef41ba448878f283a0ff.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: PBoC, Wind, Citi

Figure 7. Government bond issuance could accelerate and add an additional RMB1.3trn to new TSF in 26H2E  
![](images/23a591afcfad9b1445e49d2b0cfd3d1224deeb7feacaf4192052e6c571b42331.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: MoF, PBoC, Wind, Citi

Figure 8. Fiscal policy deployment could have started to accelerate with drawdown of fiscal deposits  
![](images/3fdbadc9ba5a53fc154ffe47105e5a7389abc84fb580f59ac4d940a6f3cd4571.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: PBoC, Wind, Citi

Figure 9. Reallocation of household deposits is steady on track  
![](images/ec951ec2d14fc833e06eae9330fcabe7d6dddbf54e4282d3e9ad1218793dd41d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: PBoC, Wind, Citi

Figure 10. M1 growth dropped on a higher base, not boding well for PPI reflation beyond the year  
![](images/ce394d9614fdfa8ee597151f94ba7e960360a0b039f3c72b0c44c3983e21bcd9.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: NBS, PBoC, Wind, Citi

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from China in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: China.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to China. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.</td></tr><tr><td>For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.</td></tr><tr><td>Citi Global Markets Asia Limited Xinyu Ji; Xiangrong Yu</td></tr><tr><td>OTHER DISCLOSURES</td></tr><tr><td>Any price(s) of instruments mentioned in recommendations are as of the prior day's market close on the primary market for the instrument, unless otherwise stated.</td></tr><tr><td>The completion and first dissemination of any recommendations made within this research report are as of the Eastern date-time displayed at the top of the Product. If the Product references views of other analysts then please refer to the price chart or rating history table for the date/time of completion and first dissemination with respect to that view.</td></tr><tr><td>European regulations require that where a recommendation differs from any of the author's previous recommendations concerning the same financial instrument or issuer that has been published during the preceding 12-month period that the change(s) and the date of that previous recommendation are indicated. Please refer to the trade history in the published research or contact the research analyst.</td></tr><tr><td>Citi has implemented policies for identifying, considering and managing potential conflicts of interest arising as a result of publication or distribution of investment research. A description of these policies can be found at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures.</td></tr><tr><td>The proportion of all Citi recommendations that were the equivalent to "Buy","Hold","Sell" at the end of each quarter over the prior 12 months (with the % of these that had received investment firm services from Citi in the prior 12 months shown in brackets) is as follows; Q1 2026 Buy 33%(63%), Hold 44% (52%), Sell 23% (46%), RV 0.5% (89%): Q4 2025 Buy 33% (63%), Hold 44% (50%), Sell 23% (46%), RV 0.4% (91%); Q3 2025 Buy 33% (61%), Hold 44% (52%), Sell 23% (50%), RV 0.4% (80%); Q2 2025 Buy 33%(63%), Hold 44% (51%), Sell 23% (49%), RV 0.4% (86%). For the purposes of disclosing recommendations other than for equity (whose definitions can be found in the corresponding disclosure sections), "Buy" means a positive directional trade idea; "Sell" means a negative directional trade idea; and "Relative Value" means any trade idea which does not have a clear direction to the investment strategy.</td></tr><tr><td>European regulations require a 5 year price history when past performance of a security is referenced. CitiVelocity's Charting Tool (https://www.citivelocity.com/cv2/#go/CHARTING_3_Equities) provides the facility to create customisable price charts including a five year option. This tool can be found in the Data &amp; Analytics section under any of the asset class menus in CitiVelocity (https://www.citivelocity.com/). For further information contact CitiVelocity support (https://www.citivelocity.com/cv2/go/CLIENT_SUPPORT). The source for all referenced prices, unless otherwise stated, is DataCentral, which sources price information from LSEG Data &amp; Analytics. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance.</td></tr><tr><td>Investors should always consider the investment objectives, risks, and charges and expenses of an ETF carefully before investing. The applicable prospectus and key investor information document (as applicable) for an ETF should contain this and other information about such ETF. It is important to read carefully any such prospectus before investing. Cli

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
