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

# Signs of Stabilization Ahead of Politburo? – Jun/Q2 Data Preview

## CITI'S TAKE

June data is likely to show tentative stabilization, with exports leading growth and retail sales potentially turning positive on accelerating trade-in subsidies. Likely soft investment and weak credit nonetheless reinforce the case for easing – July's LPR decision is the earliest test point.

Signs of stabilization ahead of Politburo? — We maintain our growth forecast at 4.5%YoY for 26Q2E, which could mark the trough for the year (see: China Outlook 26H2: AI Supercycle Cuts into the K-shaped Economy). Monthly indicators could show signs of stabilization. Industrial production is likely to hold steady at 4.6%YoY thanks to AI-centric exports and investment. Retail sales may turn positive at 0.6%YoY on a more favorable base and – more importantly – accelerating trade-in subsidies. Daily average subsidized sales quickened to \~RMB8.8bn in Jun 1-20 compared with \~RMB5.4bn in Jan-May (people.com, Jun 22 $^{nd}$ and Jun 20 $^{th}$ ). Investment remains a drag: we expect cumulative contraction in FAI to deepen to -4.5%YoY Ytd, though the monthly pace of decline could narrow to a mid-single digit. This set of data is unlikely to shift the tone of the mid-year Politburo meeting. We continue to see only piecemeal consumer support, with July as the earliest window for an LPR cut following the surprisingly low O/N reverse repo rate.

Will exports continue to lead growth? — We forecast China's exports to stay strong at 18.0%YoY in June, with imports also elevated at 25.0%YoY, leaving the trade surplus at \~US\$119.5bn. Export momentum is likely to remain solid, supported by easing Middle East tensions and the ongoing global AI supercycle. This is consistent with the rebound in June PMI new export orders and improving high-frequency volume data, with cargo throughput up 1.3%YoY in the first four weeks of June. For imports, robust AI-related demand is the key tailwind, evidenced by South Korea's exports to China rising 92.1%YoY in June. However, softer commodity prices may partially offset headline import growth.

Disinflation after oil shock? — We pencil in June CPI at 1.1% YoY and PPI at 4.3% YoY. The oil shock appears largely behind us, with price-related PMI indices moderating and Brent down -20.2% MoM. Yet we tend not to overestimate the downside risk: coal prices extended their rise into June and could have broader spillover effects than oil & gas. AI inflation may also surface further in PPI. On CPI, the picture is little changed – food prices are tracking broadly in line with seasonality (pork -1.9% MoM, vegetables +2.0% MoM, fruit -3.2% MoM), while oil and gold prices weighing on the headline, partly offset by firmer travel prices around Dragon Boat Festival and into the summer season.

The return of monetary easing? — New credit data looks set to disappoint again with the PBoC's third consecutive window guidance (Reuters, Jun 26 $^{th}$ ) and subdued bills discount rates throughout the month. We expect new RMB loans at RMB1,800bn (vs. RMB2,240bn last June) and new Total Social Financing at RMB3,500bn (vs. RMB4,225bn), with government bond issuance (\~RMB800bn) and corporate bond financing (\~RMB500bn) providing the main support to the latter. Monetary growth is also likely to retreat as a higher base kicks in. We expect M1 growth at 3.5%YoY and M2 at 8.1%YoY. Together, this reinforces the case for further monetary easing, with July's LPR decision a key test point to watch.

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

Xiangrong Yu AC +852-2501-2754 xiangrong.yu@citi.com

Xinyu Ji AC +852-2501-2792 xinyu.ji@citi.com

Yuanliu Hu $^{AC}$ +852-2501-2746
yuanliu.hu@citi.com

© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 1. June data is likely to show tentative stabilization, yet sluggish investment could reinforce the case for easing

<table><tr><td>Indicators</td><td>Date</td><td>For</td><td>Citi Fcast</td><td>Prior</td><td>Indicators</td><td>Date</td><td>For</td><td>Citi Fcast</td><td>Prior</td></tr><tr><td>FX Reserves (US$ bn)</td><td>Jul 7</td><td>Jun</td><td>3,450</td><td>3,442</td><td>M1 (%YoY)</td><td>Jul 9~15</td><td>Jun</td><td>3.5</td><td>5.5</td></tr><tr><td>Exports Growth (%YoY)</td><td>Jul 14</td><td>Jun</td><td>18.0</td><td>19.4</td><td>M2 (%YoY)</td><td></td><td></td><td>8.1</td><td>8.6</td></tr><tr><td>Imports Growth (%YoY)</td><td></td><td></td><td>25.0</td><td>27.4</td><td>New RMB Loans (RMB bn)</td><td></td><td></td><td>1,800</td><td>520</td></tr><tr><td>Trade Balance (US$ bn)</td><td></td><td></td><td>119.5</td><td>105.4</td><td>Total Social Financing (RMB bn)</td><td></td><td></td><td>3,500</td><td>2,026</td></tr><tr><td>CPI (%YoY)</td><td>Jul 9</td><td>Jun</td><td>1.1</td><td>1.2</td><td>GDP(%YoY)</td><td>Jul 15</td><td>Q2</td><td>4.5</td><td>5.0</td></tr><tr><td>PPI (%YoY)</td><td></td><td></td><td>4.3</td><td>3.9</td><td>Industrial Production (%YoY)</td><td></td><td>Jun</td><td>4.6</td><td>4.5</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Retail Sales (%YoY)</td><td></td><td></td><td>0.6</td><td>-0.6</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>FAI (%YoYYtd)</td><td></td><td></td><td>-4.5</td><td>-4.1</td></tr></table>

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

## RESEARCH ANALYST AFFILIATIONS / NON-US RESEARCH ANALYST DISCLOSURES

The legal entities employing the authors of this report are listed below (and their regulators are listed further herein). Non-US research analysts who have prepared this report (i.e., all research analysts listed below other than those identified as employed by Citi Global Markets Inc.) are not registered/qualified as research analysts with FINRA. Such research analysts may not be associated persons of the member organization (but are employed by an affiliate of the member organization) and therefore may not be subject to the FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Citi Global Markets Asia Limited

Xinyu Ji; Xiangrong Yu; Yuanliu Hu

## OTHER DISCLOSURES

Any price(s) of instruments mentioned in recommendations are as of the prior day's market close on the primary market for the instrument, unless otherwise stated.

The completion and first dissemination of any recommendations made within this research report are as of the Eastern date-time displayed at the top of the Product. If the Product references views of other analysts then please refer to the price chart or rating history table for the date/time of completion and first dissemination with respect to that view.

<table><tr><td>European regulations require that where a recommendation differs from any of the author&#x27;s previous recommendations concerning the same financial instrument or issuer that has been published during the preceding 12-month period that the change(s) and the date of that previous recommendation are indicated. Please refer to the trade history in the published research or contact the research analyst.</td></tr><tr><td>Citi has implemented policies for identifying, considering and managing potential conflicts of interest arising as a result of publication or distribution of investment research. A description of these policies can be found at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures.</td></tr><tr><td>The proportion of all Citi recommendations that were the equivalent to &quot;Buy&quot;,&quot;Hold&quot;,&quot;Sell&quot; at the end of each quarter over the prior 12 months (with the % of these that had received investment firm services from Citi in the prior 12 months shown in brackets) is as follows; Q1 2026 Buy 33%(63%), Hold 44% (52%), Sell 23% (46%), RV 0.5% (89%): Q4 2025 Buy 33% (63%), Hold 44% (50%), Sell 23% (46%), RV 0.4% (91%); Q3 2025 Buy 33% (61%), Hold 44% (52%), Sell 23% (50%), RV 0.4% (80%); Q2 2025 Buy 33%(63%), Hold 44% (51%), Sell 23% (49%), RV 0.4% (86%). For the purposes of disclosing recommendations other than for equity (whose definitions can be found in the corresponding disclosure sections), &quot;Buy&quot; means a positive directional trade idea; &quot;Sell&quot; means a negative directional trade idea; and &quot;Relative Value&quot; means any trade idea which does not have a clear direction to the investment strategy.</td></tr><tr><td>European regulations require a 5 year price history when past performance of a security is referenced. CitiVelocity&#x27;s Charting Tool (https://www.citivelocity.com/cv2/#go/CHARTING_3_Equities) provides the facility to create customisable price charts including a five year option. This tool can be found in the Data &amp; Analytics section under any of the asset class menus in CitiVelocity (https://www.citivelocity.com/). For further information contact CitiVelocity support (https://www.citivelocity.com/cv2/go/CLIENT_SUPPORT). The source for all referenced prices, unless otherwise stated, is DataCentral, which sources price information from LSEG Data &amp; Analytics. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance.</td></tr><tr><td>Investors should always consider the investment objectives, risks, and charges and expenses of an ETF carefully before investing. The applicable prospectus and key investor information document (as applicable) for an ETF should contain this and other information about such ETF. It is important to read carefully any such prospectus before investing. Clients may obtain prospectuses and key investor information documents for ETFs from the applicable distributor or authorized participant, the exchange upon which an ETF is listed and/or from the applicable website of the applicable ETF issuer. The value of the investments and any accruing income may fall or rise. Any past performance, prediction or forecast is not indicative of future or likely performance. Any information on ETFs contained herein is provided strictly for illustrative purposes and should not be deemed an offer to sell or a solicitation of an offer to purchase units of any ETF either explicitly or implicitly. The opinions expressed are those of the authors and do not necessarily reflect the views of ETF issuers, any of their agents or their affiliates.</td></tr><tr><td>Citi Global Markets India Private Limited and/or its affiliates may have, from time to time, actual or beneficial ownership of 1% or more in the debt securities of the subject issuer.</td></tr><tr><td>Please be advised that pursuant to Executive Order 13959 as amended (the &quot;Order&quot;), U.S. persons are prohibited from investing in securities of any company determined by the United States Government to be the subject of the Order. This research is not intended to be used or relied upon in any way that could result in a violation of the Order. Investors are encouraged to rely upon their own legal counsel for advice on compliance with the Order and other economic sanctions programs administered and enforced by the Office of Foreign Assets Control of the U.S. Treasury Department.</td></tr><tr><td>This communication is directed at persons who are &quot;Eligible Clients&quot; as such term is defined in the Israeli Regulation of Investment Advice, Investment Marketing and Investment Portfolio Management law, 1995 (the &quot;Advisory Law&quot;). Within Israel, this communication is not intended for retail clients and Citi will not make such products or transactions available to retail clients or to non-Eligible Clients. The presenter is not li

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
