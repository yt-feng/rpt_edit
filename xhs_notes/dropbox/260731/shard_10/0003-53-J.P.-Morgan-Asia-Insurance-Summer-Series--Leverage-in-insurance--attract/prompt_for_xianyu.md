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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## Asia Insurance

## Summer Series: Leverage in insurance; attractive ROE, but no free lunch

Leverage is a defining feature of insurance economics. Premiums are collected upfront, claims are paid later, and the resulting float allows insurers to run larger balance sheets relative to their capital base. This is how the sector converts thin underwriting margins, often below 10%, into attractive ROE. The trade-off is equally clear: higher leverage brings greater sensitivity to underwriting cycles, asset markets, funding conditions and solvency pressures. For equity investors, leverage sits at the centre of the valuation debate. Too much excess capital dilutes ROE, but excessive leverage raises the implied cost of equity and can drive a valuation discount. The right question is not whether leverage is good or bad, but whether it is being used with sufficient capital resilience and earnings quality. In this report, we assess insurance leverage through three lenses: underwriting leverage, asset leverage and financial leverage. Overall, we view sector leverage as manageable, barring a severe macro shock. Our equity picks are AIA, PingAn-H, T&D HD, Samsung F&M, Fubon FHC, SBI Life, and Thai Life. Among opportunities on the credit side, our picks include Meiji Yasuda in Japan and AIA in Hong Kong.

\- Underwriting leverage. This measures insurance risk per dollar of capital. For non-life, we use net written premiums as a multiple of IFRS BV. For life, we use insurance reserves on the B/S as a multiple of IFRS BV. The appeal is clear: US\$3 of premiums per US\$1 of surplus, written at a 5% underwriting margin, generates a 15% return on surplus. The risk is equally clear: cyclicality, adverse claims development and reserve weakness can quickly erode returns. In Asia, insurers with a conservative reserving history seem to enjoy a valuation premium and lower volatility. Those are AIA, Samsung Life, and Thai Life.

\- Asset leverage. This measures investment risk per dollar of capital, using total assets divided by IFRS BV. At 10x asset leverage, a 1% increase in investment yield adds 10%p to pre-tax ROE, all else equal. However, the same gearing can pressure capital, BV and solvency ratios when rates, spreads, equity markets or credit losses move against the B/S. Asian life/non-life insurers had an average 14x/4x asset leverage respectively, reflecting the differences in liability duration and cashflow characteristics. Indian insurers' higher asset leverage seemingly reflects simple product mix and less stringent solvency capital framework while AIA, Samsung Life and Thai Life appear more conservative.

\- Financial leverage. This measures debt risk per dollar of capital, using borrowings divided by borrowings, IFRS BV and net CSM. Debt can fund growth or M&A without equity dilution, but it is less flexible than equity. In periods of stress, weaker subsidiary cash upstreaming and tighter refinancing conditions can pressure HoldCo liquidity, dividends and TSR. Debt-servicing capacity is therefore another important lens when assessing financial leverage.

\- Solvency is the binding constraint. Solvency ratio compares available capital with required capital (link). Higher leverage can enhance ROE, but usually increases required capital and reduces solvency buffers. Solvency frameworks are therefore designed to discourage excessive leverage, particularly where underwriting, asset or debt risks could weaken capital resilience under stress. In Asia, the average FY26E ROE for life/non-life insurers is 13%/12%.

## Insurance

MW Kim AC
(852) 2800-8517
mw.kim@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Koki Sato AC
(81-3) 6736-8609
koki.sato@JPM.com
JPM Securities Japan Co., Ltd.

Jemmy S Huang AC
(886-2) 2725-9870
jemmy.s.huang@JPM.com
JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

(91-22) 6157-3594
madhukar.ladha@JPM.com
JPM India Private Limited, JPM Tower, Santacruz(E), Mumbai - 400098, SEBI Registration: INH000001873, (91-22) 6157-3000.

Dan Wang
(86-21) 6106-6349
dan.wang@JPM.com
SAC Registration Number: S1730524080001
JPM Securities (China) Company Limited

Julia Kim
(852) 2800-8540
julia.c.kim@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Emma Xing
(852) 2800-8727
emma.xing@JPM.com
JPM Securities (Asia Pacific) Limited

(81-3) 6736-8619
yuka.azami@JPM.com
JPM Securities Japan Co., Ltd.

Amanda Chang
(886-2) 2725-9861
amanda.chang@JPM.com
JPM Securities (Taiwan) Limited

See page 24 for analyst certification and important disclosures, including non-US analyst disclosures.

## Upcoming Webinar - 5 August 4PM HK/9AM UK

Use of capital – Exploring leverage, from capital adequacy to capital efficiency (Registration)

## Relevant publications

Asia Insurance: Summer Series: Life company analysis: dividends need cash, not just IFRS profit, 21 July 2026

Asia Insurance: Summer Series: A guide to Solvency Capital beyond all the Abbreviations. 14 July 2026

Asia Insurance: Summer Series: China's humanoid robots open a new frontier for P&C growth, 22 June 2026

Asia Insurance: Summer Series: China's marine insurance: Strategic repatriation of maritime risk. 6 July 2026

## Investment thesis

## Insurance leverage: three lenses on risk and return

Our final note in the summer series focuses on three key measures of insurance leverage: 1) underwriting leverage, 2) asset leverage, and 3) financial leverage. Leverage is central to insurance economics. Insurers assume risks today in exchange for future obligations: premiums are collected upfront, while claims and benefits are paid later. This timing gap creates a sizeable pool of investable capital before policyholder liabilities are settled. This creates three distinct forms of leverage. First, underwriting leverage captures the scale of insurance risk written relative to the capital base. Second, asset leverage measures the size of the investment balance sheet relative to IFRS capital. Third, financial leverage reflects the use of debt within the overall capital structure.

Based on available financial data, our observation is that Asian insurers have historically focused more on ‘capital adequacy’ than ‘capital efficiency’. As a result, balance sheet leverage appears more conservatively managed than in developed markets. Relatively low underwriting leverage across the region we think may reflect several factors: less profitable underwriting per unit of capital consumed, given the historical dominance of low-margin savings products in life; greater underwriting cyclicality in non-life products; less mature risk-modelling experience versus developed-market insurers; regulatory intervention in pricing, including auto insurance and medical indemnity; and less developed experience tables for modelling long-term risks, particularly morbidity risk.

That said, we view Asian insurers' leverage metrics as manageable, barring a severe macro shock over the foreseeable future. Our equity picks are AIA, Ping An-H, T&D Holdings, Samsung F&M, Fubon FHC, SBI Life and Thai Life. On the credit side, our preferred opportunities include Meiji Yasuda in Japan and AIA in Hong Kong.

Figure 1: Asia Insurance: FY26E P/B vs. ROE comparison by market  
![](images/763156a82b18f84e31c54b3923a6ef0447a3fb738c47efe8726c46e7d4cd6f85.jpg)  
Source: Bloomberg Finance L.P., JPM estimates. Price data as of 28 Jul 2026.

Broadly speaking, insurance is a highly regulated financial product with typically modest underwriting margins, often below 10% and, in many cases, around 5% or lower. For an insurer with a cost of equity above 10%, a low-margin standalone underwriting model is unlikely to meet shareholder return expectations without leverage. Insurers therefore use leverage to convert thin operating margins into more attractive ROE.

From a stock valuation perspective, leverage can be an important driver of multiple expansion, provided it is used prudently. We see two main routes to improving capital efficiency: reducing excess capital that dilutes ROE, and increasing profitability through appropriate use of leverage. The key is to strike the right balance between higher returns and sufficient solvency resilience. The trade-off is balance sheet sensitivity. Higher leverage can enhance ROE, but it also increases exposure to underwriting volatility, asset market movements, funding conditions and solvency pressure.

Regulators address this through solvency capital frameworks, which are designed to limit excessive leverage and protect policyholders. Higher leverage typically increases required capital, which in turn reduces the solvency ratio, all else equal. Minimum solvency requirements, together with regulatory thresholds for dividend approval, act as policy tools to protect customers through market and underwriting cycles. In addition, by recognising only part of debt financing as available capital relative to required capital, regulators discourage insurers from taking excessive balance sheet leverage.

For equity investors, this creates a clear valuation debate. Excess capital can be criticised for inefficient capital allocation and ROE dilution, but excessive leverage is also penalised for higher balance sheet risk. In practice, investors typically reflect elevated leverage through a higher implied cost of equity and, in many cases, a valuation discount.

The central challenge for insurers is therefore to generate sustainable ROE above the cost of equity while maintaining an adequate solvency buffer. In Asia, life and non-life insurers generate average FY26E ROE of 13% and 12%, respectively (Figure 1).

Figure 2: Asia Insurance: FY26E P/B vs ROE comparison by company x, %  
![](images/6c0b3c4bdb5f7437d6468c179637634ae292a79d25b4fbcdd7d8d17ee5ef0761.jpg)  
Source: Bloomberg Finance L.P., JPM estimates. Note: 1) Price data as of 28 Jul 2026. 2) India is excluded for presentation simplicity.

Table 1: Asia Insurance: Valuation comparison table
Local currency, %, x

<table><tr><td>Company</td><td>B&#x27;berg Code</td><td>Rating</td><td>Price (28-Jul-2026)</td><td>PT (Dec-26)</td><td>Upside/downside</td><td>P/E 26e</td><td>P/E 27e</td><td>P/BV 26e</td><td>P/BV 27e</td></tr><tr><td colspan="10">China</td></tr><tr><td>AIA Group</td><td>1299 HK Equity</td><td>OW</td><td>77.9</td><td>112.0</td><td>44%</td><td>13</td><td>11</td><td>2.2</td><td>2.0</td></tr><tr><td>FWD Group</td><td>1828 HK Equity</td><td>OW</td><td>29.5</td><td>47.0</td><td>60%</td><td>17</td><td>13</td><td>0.6</td><td>0.5</td></tr><tr><td>China Life-H</td><td>2628 HK Equity</td><td>OW</td><td>27.9</td><td>40.0</td><td>43%</td><td>5</td><td>4</td><td>1.1</td><td>1.0</td></tr><tr><td>China Life-A</td><td>601628 CH Equity</td><td>N</td><td>40.2</td><td>39.0</td><td>-3%</td><td>20</td><td>18</td><td>1.8</td><td>1.7</td></tr><tr><td>Ping An-H</td><td>2318 HK Equity</td><td>OW</td><td>57.1</td><td>90.0</td><td>58%</td><td>7</td><td>6</td><td>0.8</td><td>0.7</td></tr><tr><td>Ping An-A</td><td>601318 CH Equity</td><td>OW</td><td>54.2</td><td>83.0</td><td>53%</td><td>7</td><td>7</td><td>0.9</td><td>0.8</td></tr><tr><td>CPIC-H</td><td>2601 HK Equity</td><td>OW</td><td>30.0</td><td>43.0</td><td>43%</td><td>6</td><td>6</td><td>0.7</td><td>0.6</td></tr><tr><td>CPIC-A</td><td>601601 CH Equity</td><td>OW</td><td>31.7</td><td>50.0</td><td>58%</td><td>7</td><td>7</td><td>0.8</td><td>0.8</td></tr><tr><td>New China Life-H</td><td>1336 HK Equity</td><td>N</td><td>47.6</td><td>45.0</td><td>-6%</td><td>6</td><td>5</td><td>1.0</td><td>1.0</td></tr><tr><td>New China Life-A</td><td>601336 CH Equity</td><td>N</td><td>62.8</td><td>59.0</td><td>-6%</td><td>8</td><td>8</td><td>1.6</td><td>1.5</td></tr><tr><td>PICC Group-H</td><td>1339 HK Equity</td><td>N</td><td>5.3</td><td>5.8</td><td>9%</td><td>6</td><td>5</td><td>0.5</td><td>0.4</td></tr><tr><td>PICC Group-A</td><td>601319 CH Equity</td><td>N</td><td>7.5</td><td>6.9</td><td>-8%</td><td>12</td><td>10</td><td>1.1</td><td>1.0</td></tr><tr><td>PICC P&amp;C</td><td>2328 HK Equity</td><td>N</td><td>16.2</td><td>14.0</td><td>-14%</td><td>9</td><td>8</td><td>1.2</td><td>1.1</td></tr><tr><td colspan="10">Korea</td></tr><tr><td>Samsung Life*</td><td>032830 KP Equity</td><td>OW</td><td>285,000</td><td>580,000</td><td>104%</td><td>13</td><td>13</td><td>0.5</td><td>0.5</td></tr><tr><td>Hanwha Life</td><td>088350 KP Equity</td><td>UW</td><td>4,295</td><td>2,100</td><td>-51%</td><td>7</td><td>8</td><td>0.4</td><td>0.4</td></tr><tr><td>Samsung F&amp;M*</td><td>000810 KP Equity</td><td>OW</td><td>609,000</td><td>800,000</td><td>31%</td><td>11</td><td>10</td><td>0.9</td><td>0.8</td></tr><tr><td>Hyundai M&amp;F</td><td>001450 KP Equity</td><td>UW</td><td>38,450</td><td>22,000</td><td>-43%</td><td>5</td><td>4</td><td>0.6</td><td>0.5</td></tr><tr><td>DB Insurance</td><td>005830 KP Equity</td><td>OW</td><td>159,000</td><td>250,000</td><td>57%</td><td>5</td><td>5</td><td>0.9</td><td>0.9</td></tr><tr><td>Korean Re</td><td>003690 KP Equity</td><td>OW</td><td>13,600</td><td>17,000</td><td>25%</td><td>5</td><td>7</td><td>0.6</td><td>0.6</td></tr><tr><td>Seoul Guarantee Insurance</td><td>031210 KP Equity</td><td>OW</td><td>41,700</td><td>90,000</td><td>116%</td><td>10</td><td>8</td><td>0.5</td><td>0.5</td></tr><tr><td colspan="10">ASEAN</td></tr><tr><td>Bangkok Life**</td><td>BLA TB Equity</td><td>OW</td><td>25.5</td><td>29.1</td><td>14%</td><td>6</td><td>6</td><td>0.8</td><td>0.7</td></tr><tr><td>Thai Life**</td><td>TLI TB Equity</td><td>OW</td><td>11.7</td><td>17.5</td><td>50%</td><td>10</td><td>9</td><td>0.8</td><td>0.8</td></tr><tr><td>LPI Capital</td><td>LPI MK Equity</td><td>OW</td><td>15.0</td><td>20.0</td><td>33%</td><td>13</td><td>12</td><td>2.3</td><td>2.3</td></tr><tr><td colspan="10">Taiwan</td></tr><tr><td>Cathay FHC***</td><td>2882 TT Equity</td><td>OW</td><td>95.4</td><td>130.0</td><td>36%</td><td>11</td><td>11</td><td>1.5</td><td>1.3</td></tr><tr><td>Fubon FHC***</td><td>2881 TT Equity</td><td>OW</td><td>125.5</td><td>69.8</td><td>-44%</td><td>11</td><td>12</td><td>1.6</td><td>1.4</td></tr><tr><td>KGI FHC***</td><td>2883 TT Equity</td><td>OW</td><td>29.6</td><td>41.0</td><td>39%</td><td>10</td><td>10</td><td>1.1</td><td>1.0</td></tr><tr><td></td><td></td><td></td><td rowspan="2">Price (28-Jul-2026)</td><td rowspan="2">PT (Dec-26)</td><td rowspan="2">Upside/downside</td><td rowspan="2">P/E FY27e</td><td rowspan="2">P/E FY28e</td><td rowspan="2">P/BV FY27e</td><td rowspan="2">P/BV FY28e</td></tr><tr><td>Japan</td><td>B&#x27;berg Code</td><td>Rating</td></tr><tr><td>Dai-ichi Life</td><td>8750 JT Equity</td><td>N</td><td>1,903</td><td>1,900</td><td>0%</td><td>13</td><td>13</td><td>1.7</td><td>1.7</td></tr><tr><td>T&amp;D Holdings</td><td>8795 JT equity</td><td>OW</td><td>5,032</td><td>5,300</td><td>5%</td><td>17</td><td>11</td><td>1.5</td><td>1.5</td></tr><tr><td>Japan Post Insurance</td><td>7181 JT Equity</td><td>OW</td><td>1,753</td><td>1,790</td><td>2%</td><td>12</td><td>11</td><td>0.4</td><td>0.4</td></tr><tr><td>Sony Financial Group</td><td>8729 JP Equity</td><td>N</td><td>156.1</td><td>150</td><td>-4%</td><td>446</td><td>17</td><td>1.1</td><td>1.0</td></tr><tr><td>MS&amp;AD Insurance Group***</td><td>8725 JT Equity</td><td>N</td><td>5,039</td><td>5,000</td><td>-1%</td><td>13</td><td>11</td><td>1.1</td><td>1.1</td></tr><tr><td>Tokio Marine Holdings***</td><td>8766 JT Equity</td><td>N</td><td>8,234</td><td>8,100</td><td>-2%</td><td>18</td><td>16</td><td>1.

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
