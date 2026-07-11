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

## Austerity Now, Acceleration Later?

## CITI'S TAKE

An underappreciated driver of the sharp 26Q2 slowdown is a de facto fiscal austerity. Central and local governments are each contributing, but through distinct channels: the central government has collected larger-than-usual revenues even while running ahead of the pace observed in recent years in expenditures; local governments are pressured by falling land sales, debt constraints, and a lack of high-quality projects, limiting their ability and willingness to stimulate via traditional means. Our base case is for this austerity to reverse in 26H2 as fiscal deployment accelerates, driving a mild rebound. We don't expect a mid-year budget revision; instead, long-term fiscal reforms addressing central-local imbalances and redistribution issues in the AI era are the key themes to watch.

Xiangrong Yu $^{AC}$ +852-2501-2754
xiangrong.yu@citi.com

Xinyu Ji $^{AC}$

+852-2501-2792

xinyu.ji@citi.com

An underappreciated driver of the sharp 26Q2 slowdown is a de facto fiscal austerity. FAI growth slumped -5.7%YoY in Mar-May amid flattish subsidies for “two key projects” (两重) and equipment upgrades. Retail sales growth turning negative at -0.6%YoY in May is partly attributable to the scale-back of the trade-in scheme and delays in fund disbursement. At the aggregate level, the broad fiscal deficit (general budget + government funds) $^{1}$ was 2.2% of GDP in Jan-May, below the 2.4% recorded a year earlier. On a 12-month rolling basis, the deficit has narrowed to 8.8% of GDP in May from 9.0% at end-2025. Central and local governments are each contributing to this austerity, but through distinct channels:

■ Central government austerity is a less obvious but a meaningful contributor – driven by revenue outperformance rather than spending restraint. Broad central government spending is running ahead of the run-rate seen in recent years, reaching a five-year high of 33.3% of the annual budget by May and growing a solid 10.1% YoY in Jan-May. The tightening has stemmed entirely from the revenue side. A combination of PPI reflation and stricter tax collection, particularly for Personal Income Tax (PIT, up 12.2% YoY in Jan-May), has bolstered tax receipts and resulted in a central surplus larger than last year.

■ Local governments are the main and more visible source of fiscal drag – pressured on both revenue and spending sides. In contrast to the central government, broad local government spending contracted -1.7% YoY in the first five months, and the spending progress decelerated to 34.8% of the annual budget compared with 35.0% in the same period of 2025. On the revenue side, pressure from the property downturn persists, with broad local government revenue down -2.4% YoY; slumping land sales alone created a drag of -4.6ppts. Meanwhile, local government financing was sluggish, with special LGB issuance slowing in 26Q2 and net LGFV bond financing remaining negative.

Figure 1. Broad fiscal deficit declined in Jan–May in a de facto austerity  
![](images/4990d2aeae9657e4cb0802ea81fddd3c6aa5bf437015e090d5955225a3cb13b0.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: MoF, NBS, NPC, CEIC, Citi

Figure 2. Central government spending is running ahead of recent years while local government spending is lagging  
![](images/3ede851d2fa4e1884a07373f23567f29b7ec5cfae6e8307c65d1317182c9138b.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: MoF, Wind, Citi

Figure 3. Local governments remain under pressure amid the property downturn on both revenue...  
![](images/c2cd58b9a51f87c62203a3cadb2cdc3591ff04a0b71e02e418b175db582053fa.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: MoF, Wind, Citi

Figure 4. ... and expenditure sides  
![](images/00fbb526afc3e3392ce6b2ce933e70636a76588511ffb28cafe1b8d07e1fa96d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: MoF, Wind, Citi

Figure 5. Special LGB financing has been lagging in 26H1, likely out of prudence  
![](images/bc7cea5bc683a388e7de43d73bbed20cfb089c068db2c815554ae152055187fd.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Wind, Citi

Figure 6. Net LGFV bond financing is deeply negative amid debt resolution  
![](images/82909d5ee59c93d3c4a7d582ba157884c056e99cb2f6a869390369249315301d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Wind, Citi

## Structural Local Fiscal Stress

Despite the “more proactive” fiscal stance pledged at the CEWC since end-2024, local officials appear constrained in both the ability and willingness to stimulate the economy the old way.

## Ability to Stimulate

Local governments are operating with tight budgets:

The revenue rebound this year has disproportionately benefited the central government. Under the tax-sharing system, the central government retains a 60% share of PIT, which rebounded 12.2% YoY Ytd. It was also the primary beneficiary of strong import-related VAT and consumption taxes (+10.4% YoY Ytd), a surge in securities transaction duties (+88.9% YoY Ytd), and the phase-out of the auto-purchase tax cut and export VAT rebates.

The property downturn continues to weigh heavily on local government revenues. For the general budget, property-related budgetary taxes – including property tax, deed tax, land VAT and others – contracted -4.5%YoY in Jan–May.

For government funds, land sales revenue fell even more sharply, down - 28.7% YoY, with the rolling 12-month sales value now at only RMB3.8trn. Local government fiscal self-sufficiency remains depressed as a result.

Earlier off-financing channels are mostly closed as debt resolution continues. Issuance of special refinancing bonds – this round’s debt-swap instrument – proceeded at a steady RMB1.6trn in Jan–May, against RMB1.8trn in the same period last year. Beyond that, however, off-budget financing avenues show no signs of revival: Net LGFV bond financing remains in deep contraction, Public-Private Partnership (PPP) activity is subdued, and Government-Guided Funds are pivoting toward “new productive forces” like AI, rather than broad-based local investment (Sina, May 29 $^{th}$ ).

Figure 7. Revenue rebound has disproportionately benefited the central government

<table><tr><td></td><td>Tax (Central: Local)</td><td>Revenue, 2025(RMB trn)</td><td>Jan-May 26(%YoY)</td></tr><tr><td rowspan="3">Shared</td><td>VAT (50:50)</td><td>6.9</td><td>6.2</td></tr><tr><td>Corporate Income Tax (60:40)</td><td>4.1</td><td>0.2</td></tr><tr><td>Personal Income Tax (60:40)</td><td>1.6</td><td>12.2</td></tr><tr><td rowspan="5">Central</td><td>VAT and CT for Imports</td><td>1.8</td><td>10.4</td></tr><tr><td>Consumption Tax /1</td><td>1.7</td><td>-3.1</td></tr><tr><td>Stamp Duty for Securities Trading</td><td>0.2</td><td>88.9</td></tr><tr><td>Tariff</td><td>0.2</td><td>5.6</td></tr><tr><td>Auto Purchase Tax</td><td>0.2</td><td>12.7</td></tr><tr><td rowspan="3">Mostly Local</td><td>Property Related Tax</td><td>1.8</td><td>-4.5</td></tr><tr><td>Urban Maintenance Tax /2</td><td>0.5</td><td>3.8</td></tr><tr><td>Other Stamp Duty</td><td>0.2</td><td>4.0</td></tr></table>

Reform Plans: 1/ Collection of CT to shift to sellers and adjust its coverage and rates; 2/ To be combined with two other fees and set up as Local Surcharge  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: MoF, Wind, Citi

Figure 8. Land sales amounted to only RMB3.8trn in the past 12 months, down from the peak of RMB9trn in 2021  
![](images/e1e53054640b48127936556edb88d5c997dc5d4acab7fbb82c9ff088baecc839.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: MoF, Wind, Citi

Figure 9. Local government's fiscal self-sufficiency ratio stays depressed  
![](images/7b02e05402447e5c1f0e40da985a85b542675c9e3ab31eccfaa2f7ac1f95248b.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: MoF, Wind, Citi

Figure 10. Debt resolution is steady on track, while off-budget financing channels are mostly closed  
![](images/524486444c7721d4844a34945117b0eec279c7e3859f58220362a43c61da1596.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Wind, Citi

## Willingness to Stimulate

Prudence under tight budgets captures local government's willingness to spend. A clear pecking order appears to have emerged in expenditure priorities, with social security > tech & education > infrastructure, broadly consistent with signals from the central government (e.g., see Finance Minister's comments in Nov 2024, MoF). In Jan-May, budgetary social security spending rose $7.8\%$ YoY, while spending on

tech & education was nearly flat. Infrastructure spending – despite a 2.8% YoY increase in this year’s budget – dropped -6.3% YoY, deepening the slump since mid-2025. Tighter scrutiny from the central government on projects, as reflected in recent audit reports, likely reinforces this caution.

Competing official targets further dampen spending willingness. While GDP growth still matters, its perceived weight as a performance metric appears to be fading – based on both the trajectory of recent years and the downgraded national target this year. The ongoing campaign to establish the correct view of political performance (树立正确的政绩观) could add further considerations ahead of the 21st Party Congress next year. Local officials need to navigate a range of binding constraints – debt management, financial stability (especially small banks), production safety, and social stability. Stimulating local growth the old way is, in our view, unlikely to be a top priority.

Figure 11. Expenditure seemingly follows a pecking order of social security > tech & education > infrastructure  
![](images/3d0d6a884c96ab89806d29d0017ea43b7928432a3eb2182fec45079fe89de96e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: MoF, Wind, Citi

Figure 12. Tighter scrutiny from the central government could reinforce this prudence  
![](images/724660a36a8cc02f682ad1b2b3ae13b8dc1a464ef312b206b2506f834d4dbf61.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NAO, Citi

## What to Expect Ahead?

Fiscal deployment looks set to accelerate in 26H2E (see: 26H2 Outlook: AI Supercycle Cuts into the K-shaped Economy). This includes [1] an increased pace of special bonds issuance, [2] faster fund deployment, and [3] more effective usage of the RMB800bn policy-financing tool. Implementation acceleration should lead to a natural reversal of the austerity seen in 26H1. Targeted measures such as the “Six Networks” initiative are underway, enabling AI transition and stabilizing investment. Growth could thus stage a mild rebound, aided by a low base from 25H2 and the fading impact from the Middle East conflict.

A mid-year budget revision is not our base case with limited urgency for broad-based stimulus. A 2024-style pivot seems unlikely to us, as GDP growth could still reach the lower end of the 4.5-5.0% target range despite the 26Q2 slowdown. Further, fiscal stress is primarily a local issue, and market sentiment appears more stable now than in 2024. While a 2023-style revision prompted by extreme weather events and super El Nino over the summer – the MoF then issued an additional RMB1trn of CGB for disaster relief (MoF, Oct 24 $^{th}$ , 2023) – cannot be fully ruled out, the fiscal context is different. This year’s deficit is already set at 4% of GDP, offering less headroom than in 2023, when the initial target was 3% before being raised to 3.8%.

Fiscal reform is a key theme to watch for 2027 and beyond, with two primary areas of focus:

■ Rebalancing the fiscal relationship between central and local governments has become a high-priority issue post the real-estate era. Policymakers have already signaled reforms to the consumption tax and a consolidation of local surcharges. While follow-up measures could be announced as soon as this year, the full reallocation of the estimated RMB2trn in revenue will likely take years to complete.

\- Redistributing the gains from AI is also a rising fiscal imperative. The AI-led new economy is now front and center in China's K-shaped economy, widening the divergence and creating an overhang on Chinese consumers with increasing job displacement risks amid rapid adoption. We have previously highlighted [1] direct wage support and [2] targeted AI taxes as two potentially plausible solutions to this growing challenge. Both could gain traction in policy discussions as fiscal reforms deepen in the years to come.

Figure 13. A mid-year budget revision is not our base case with limited urgency for broad-based stimulus

<table><tr><td></td><td>26Q2</td><td>24Q3</td></tr><tr><td>Quarterly GDP Growth</td><td>4.5 (Citi F)</td><td>4.6</td></tr><tr><td>Cumulative Growth</td><td>4.7 vs. 4.5~5.0% Target</td><td>4.8 vs. ~5% Target</td></tr><tr><td>Inflation</td><td>PPI ~4%, CPI ~1%</td><td>PPI ~-2.5%, CPI ~0</td></tr><tr><td>Fiscal Revenue</td><td>4% revenue growth vs. 2.2% budgeted</td><td>~RMB1.4trn shortfall</td></tr><tr><td>Local Government Debt</td><td>Debt swap mostly done</td><td>Rising LGFV debt risk</td></tr><tr><td>Equity Market</td><td>SHCOMP ~4,000</td><td>SHCOMP ~2,700</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: MoF, NBS, Wind, Citi

Figure 14. Rebalancing the central-local fiscal relationship has become a high-priority issue  
![](images/cbe1c8081d42510619de13a93f7d1b29b0a93f6bac0766a24d9906671b2aacfe.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: MoF, Wind, Citi

Figure 15. Consumption tax reform is in the pipeline, and some steps could follow later this year  
![](images/d325a9aa3fc99404eb43daf5a007622c87ecbebd008e37e30e53a22831a1b62d.jpg)  
Source: MoF, Wind, Citi  
© 2026 Citi Inc. No redistribution without Citi's written permission.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
