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

## Closing the Offshore Trust Tax Loophole

## CITI'S TAKE

The MoF issued Document #21 on 24 July, materially tightening personal income tax (PIT) rules governing offshore trusts – effective immediately (Xinhua, Jul 24 $^{th}$ ). The move represents another step to closing regulatory loopholes on outbound investments. It also confirms our longstanding view that the era of large-scale tax & fee cuts is behind us. We see this as a near-term sentiment headwind for HK equities: red-chip/VIE founders holding stakes via offshore trusts may need to monetize assets to fund compliance. Medium-term, with offshore trust tax advantages eliminated, H-share structures should be set to further prevail over red-chip alternatives in the IPO market. For wealth management, ultra-high-net-worth families largely lose the tax planning rationale for offshore trust structuring.

Xiangrong Yu $^{AC}$ +852-2501-2754
xiangrong.yu@citi.com

Xinyu Ji AC

+852-2501-2792

xinyu.ji@citi.com

What happened? — The MoF issued Document #21 on 24 July, materially tightening personal income tax (PIT) rules governing offshore trusts – effective immediately (Xinhua, Jul 24 $^{th}$ , 2026). Key provisions include: [1] Settlement tax: Resident individuals transferring assets into offshore trusts are taxed on unrealized gains at market value at the point of contribution (current PIT rate = 20%); [2] Annual attribution: Trust income is taxed annually in the resident settlor's hands (20% PIT), whether distributed or retained, including income derived through controlled offshore entities (i.e., look-through treatment); [3] Anti-avoidance: Loans, guarantees, expense reimbursements, and below-market use of trust assets may be recharacterized as taxable distributions; [4] Exit tax: A taxable event is triggered upon trust termination, the settlor's death, or loss of Chinese tax residency; [5] Broad residency test: Foreign nationality or overseas residency does not preclude Chinese tax domicile if an individual's primary economic interests remain in China; [6] Retrospective clean-up: Unpaid tax liabilities arising from 1 January 2023 must be self-declared within 90 days, without late-payment surcharges if filed on time.

Another step to closing regulatory loopholes on outbound flows — Document #21 is the latest measure in the sequential tightening of China's outbound investment regulation. Earlier, the State Council tightened rules on direct outbound investment, and the CSRC issued action plans to rectify illegal cross-border securities, futures, and fund operations following investigations into three cross-border brokers. Our prior expert call flagged tax compliance as an imminent follow-up issue –that has now materialized. Offshore trusts have become a popular vehicle for business owners to hold economic interests in offshore-listed companies (via red-chip and VIE structures) and a wealth-planning and tax-deferral tool for ultra-high-net-worth families more broadly. Document #21 resolves the previous tax ambiguity in full. Enforcement was already underway ahead of formalization: authorities in Shanghai, Jiangsu, Shenzhen, and other jurisdictions had initiated inspections of offshore trust arrangements as early as 2025 (Sina, April $13^{\text{th}}$ , 2026), with a $20\%$ levy applied in select cases. The MoF announcement formalizes existing practice and establishes a comprehensive national framework.

The era of large-scale tax & fee cuts is behind us — Document #21 reinforces our long-standing view that the years of large tax and fee cuts are behind us. The government has already [1] raised VAT on telecom services, [2] reduced export tax rebates, and [3] tightened social security collections (Sina, Jul 6 $^{th}$ , 2026), among others. The trend is also visible in the data: PIT revenue growth has consistently outpaced retail sales growth and urban household income growth in recent years, with the divergence widening sharply in 26H1 – PIT revenue jumped 13.1%YoY against a near-flat 1.3%YoY retail sales print. The tightening impulse reflects multiple sources of pressure: structurally weaker land-sale revenues, K-shaped income dynamics that demand redistribution, and – as we have highlighted – the growing fiscal imperative to recycle gains from AI-driven capital concentration toward lower-income cohorts. In this sense, we believe targeted support for lower-income groups is as important a policy lever as taxing the ultra-wealthy.

Market impact: likely near-term sentiment headwind, medium-term ecosystem reshaping — we believe HK-listed equities could be more sensitive to such impact.

\- Near-term – red-chip/VIE overhang: red-chip/VIE founders – who commonly hold their stakes through offshore trusts – face two compounding sources of pressure. First, the settlement tax and annual attribution rules generate immediate cash tax liabilities on previously unrealized or undistributed wealth – potentially forcing asset monetization to fund compliance. Second, the retrospective clean-up obligation concentrates this pressure within a 90-day window. These factors together might lead to a risk of forced or pre-emptive stake reductions, particularly for large shareholders in HK-listed red-chip/VIE chip names, where block sales are the most liquid exit.

Medium-to-long term – IPO & wealth management: Red-chip structures have already lost popularity in the IPO market on regulatory grounds, and Document #21 strips out their tax advantages. H-share structures, which keep the listing vehicle onshore, now appears to be the path of least resistance, likely accelerating a shift already underway. On wealth management, with the tax efficiency of offshore trusts effectively eliminated, ultra-high-net-worth families lose a key incentive for outbound structuring. Incremental flows are somewhat more likely to stay onshore or even return on rising compliance costs, in our view. The announcement may reshape financial and legal service businesses, facilitating cross-border wealth structuring – trusts, family offices, and private banking in particular.

Exchange rate, capital controls, and RMB internationalization: We regard Document #21 as a tax compliance measure, not a new capital control policy. It should have minimal impact on the exchange rate or interest rates. Crucially, it leaves intact the “golden window” for RMB internationalization – the associated flows run through official, tax-compliant channels, including QFII, Bond Connect, CIBM Direct, Stock Connect, and related programs.

\- Hong Kong as a wealth management hub: The city's role is mostly unaffected, in our view. Document #21 applies uniformly to all offshore trusts regardless of domicile. We view that Hong Kong remains the most accessible and well-regulated gateway for compliant cross-border wealth management.

What to watch ahead? — Implementation tops the list, and PIT revenue data in the coming months should serve as a timely check. Remaining gray areas could be subject to increasing scrutiny as well, potentially including cross-border SPVs, family office/private banking business, insurance, and real estate. Meanwhile, the redistribution dimension of fiscal policy – how enhanced tax revenues from the ultra-wealthy translate into support for lower-income groups – will be as important to track as the revenue impact itself.

Figure 1. Personal income tax revenue growth has outpaced income growth in recent years  
![](images/29b8f01f735f4a51e48a496ce983b8c05ed404f404997987d154c4bacc02d9fc.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: MoF, NBS, Wind, Citi

Figure 2. Red-chip structures have already lost popularity to H-shares in Hong Kong's IPO market  
![](images/389335e5dc12eb34ccd69a5a6b846c10ee28a9f885790e60c510e913fe77e1c8.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Wind, Citi

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from China.

Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from China.

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from China in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): China.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: China.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: China.

Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to China. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013,

Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at

https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

## RESEARCH ANALYST AFFILIATIONS / NON-US RESEARCH ANALYST DISCLOSURES

The legal entities employing the authors of this report are listed below (and their regulators are listed further herein). Non-US research analysts who have prepared this report (i.e., all research analysts listed below other than those identified as employed by Citi Global Markets Inc.) are not registered/qualified as research analysts with FINRA. Such research analysts may not be associated persons of the member organization (but are employed by an affiliate of the member organization) and therefore may not be subject to the FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Citi Global Markets Asia Limited

Xinyu Ji; Xiangrong Yu

## OTHER DISCLOSURES

Any price(s) of instruments mentioned in recommendations are as of the prior day's market close on the primary market for the instrument, unless otherwise stated.

The completion and first dissemination of any recommendations made within this research report are as of the Eastern date-time displayed at the top of the Product. If the Product references views of other analysts then please refer to the price chart or rating history table for the date/time of completion and first dissemination with respect to that view.

European regulations require that where a recommendation differs from any of the author's previous recommendations concerning the same financial instrument or issuer that has been published during the preceding 12-month period that the change(s) and the date of that previous recommendation are indicated. Please refer to the trade history in the published research or contact the research analyst.

Citi has implemented policies for identifying, considering and managing potential conflicts of interest arising as a result of publication or distribution of investment research. A description of these policies can be found at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures.

The proportion of all Citi recommendations that were the equivalent to "Buy", "Hold", "Sell" at the end of each quarter over the prior 12 months (with the % of these that had received investment firm services from Citi in the prior 12 months shown in brackets) is as follows; Q1 2026 Buy 33%(63%), Hold 44% (52%), Sell 23% (46%), RV 0.5% (89%): Q4 2025 Buy 33% (63%), Hold 44% (50%), Sell 23% (46%), RV 0.4

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the "Product"), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
