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

## A Plateauing Inflation Path in 26H2E after Energy Shock?

## CITI'S TAKE

CPI and PPI staged a small miss compared with expectations in June, but it came mostly from external factors including oil and gold prices. Domestic demand could have remained lackluster but largely stable, with supply conditions driving most of the volatility. For the whole quarter of 26Q2, nominal growth could rise further despite a real growth slowdown. We expect a plateauing path for inflation in 26H2E, with sporadic gains from AI inflation across CPI and PPI and a tentative stabilization of the pork cycle. Domestic demand could remain weak in this K-shaped economy, yet targeted support along with supply-side efforts on anti-involution could capture the downside to prices, in our view. The upcoming Politburo meeting could offer more signals.

Xinyu Ji $^{AC}$ +852-2501-2792
xinyu.ji@citi.com

Xiangrong Yu AC

+852-2501-2754

xiangrong.yu@citi.com

Inflation readings missed expectations in June as the energy shock faded. CPI edged down to 1.0%YoY (Citi/Mkt: 1.1%YoY) from earlier 1.2%YoY. Its sequential change was softer than seasonality at -0.3%MoM vs. an average of -0.2%MoM in the past three years. The small miss came from external factors of oil and gold. By major components,

\- Food prices dipped -0.4%MoM in June and stayed largely unchanged at -1.6%YoY (vs. -1.7%YoY in May). Pork downcycle could be closer to its bottom, with sequential change at -0.8%MoM, the smallest contraction in four months. Most food prices were stable, with vegetables at -1.0%MoM (-0.3%YoY) and fruits at -2.0%MoM (-0.7%YoY). Egg prices rose sharply amid hot weather at 5.8%MoM (16.0%YoY). Extreme weather events as El Nino develops are starting to have a more visible impact on China, and it is likely that supply conditions over the summer drives more price volatility.

■ Energy prices retreated as the oil shock faded. Prices dropped -4.5%MoM for transportation fuel, and its year-on-year change normalized to 15.3%YoY from 21.1%YoY in May, the first decline since the conflict. More downside is likely ahead in July with deeper adjustment of retail fuel prices, and year-on-year change could inch towards low single digits.

■ Core inflation dipped to 1.0%YoY, with its sequential change at -0.1%MoM and in line with seasonality. [1] Core goods inflation eased further to 1.3%YoY per our estimate, the lowest reading in one year. Gold prices eased to -5.9%MoM and 28.1%YoY and are largely responsible for the miss in June combined with oil prices. Durable goods prices are mixed: telecom equipment CPI rose to 7.6%YoY, an all-time high amid AI inflation, while auto CPI stayed unchanged at -1.1%YoY and home appliances prices retreated to 2.2%YoY (vs. 3.4%YoY). [2] Services CPI was lackluster but steady at 0.0%MoM and 0.8%YoY before the travel season.

Sequential PPI turned negative with energy shock fading. PPI dropped - 0.3%MoM, the first negative reading since July 2025, while its year-on-year reading continued to rise on base effect to 4.1%YoY (Citi/Mkt: 4.3/4.1%YoY).

■ Mideast conflict: We estimated that energy and chemical related sectors dragged 0.2ppts to sequential change of PPI of -0.3%MoM with Mideast conflict impact fading. With global oil prices easing in June, oil & gas extraction dropped -11.8%MoM and fuel processing declined -1.9%MoM in June, while chemicals eased -2.0%MoM.

■ Domestic energy prices: Coal prices rose into the summer and partially offset the drag from global prices. PPI for coal extraction inched up to 5.6%MoM with its year-on-year change at 20.6%YoY after turning positive only three months ago. Coal prices could have had wider spillover to ferrous metal processing, whose PPI rose to 5.2%YoY.

■ AI inflation: PPI for computer and other electronics mfg rose to 3.3%YoY, also an all-time high since 1996. Its momentum sustained with sequential change at 0.7%MoM, and 3M/3M annualized change at 7.9% in the past few months, hinting at further upside ahead. The NBS noted broad-based price hikes among electronics, with VR at 8.4%MoM, wearables at 3.4%MoM and industrial PCs at 3.3%MoM (NBS, Jul 9 $^{th}$ ).

■ Domestic demand: demand weakness remains a concern, as auto PPI remained subdued at -2.1% YoY and non-metallic mining at -3.3% YoY. Seasonal demand drove air conditioner mfg prices up 0.4% MoM.

Figure 1. CPI and PPI posed a small miss in June mostly on external factors  
![](images/33b6ffd6538be76346561108cfa61536b17e7bdf2125fb99e2b4c8d6fe1c99c5.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 2. Core goods prices eased further as soft demand met various supply conditions  
![](images/e02ce4f3c7297e8c14b122325ed440cba2a52a6dd2605f648f785c59b487e761.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi

Figure 3. Telecom equipment CPI rose to an all-time high amid AI inflation  
![](images/8b41192431cc18c81b04fc26875827b6094ca50de505b209c83962ef9279290d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi

Figure 4. We estimate a drag of -0.2ppts from energy & chemical to sequential PPI in June  
![](images/a2d88f3a4520d27c5749873c35e8c10e639d503de83f7c24281a4ad75d8424fc.jpg)  
Energy Chemical Non-Ferrous Construction Others PPI, %MoM © 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi

Figure 5. Mideast conflict impact retreated for PPI, but domestic energy prices and AI inflation rose further

<table><tr><td rowspan="2" colspan="3">Sector</td><td rowspan="2">Deflation easing sequentially?</td><td rowspan="2">Consecutive months of PPI deflation</td><td colspan="3">%YoY</td><td colspan="3">3M/3M Annualized</td></tr><tr><td>Apr</td><td>May</td><td>Jun</td><td>Apr</td><td>May</td><td>Jun</td></tr><tr><td>Up</td><td>煤炭开采和洗选业</td><td>Coal mining and washing</td><td></td><td></td><td>3.1</td><td>10.0</td><td>20.6</td><td>6.1</td><td>22.8</td><td>52.1</td></tr><tr><td>Up</td><td>石油和天然气开采业</td><td>Petroleum and natural gas extraction</td><td></td><td></td><td>28.6</td><td>35.7</td><td>16.8</td><td>332.6</td><td>253.2</td><td>18.9</td></tr><tr><td>Up</td><td>石油、煤炭及其他燃料加工业</td><td>Petroleum, coal and other fuel processing</td><td></td><td></td><td>14.2</td><td>18.4</td><td>16.7</td><td>133.7</td><td>130.0</td><td>70.0</td></tr><tr><td>Up</td><td>黑色金属矿采选业</td><td>Ferrous metal mining</td><td></td><td></td><td>1.3</td><td>3.3</td><td>5.2</td><td>-5.1</td><td>1.6</td><td>4.1</td></tr><tr><td>Up</td><td>有色金属矿采选业</td><td>Non-ferrous metal mining</td><td></td><td></td><td>38.9</td><td>36.5</td><td>25.5</td><td>82.8</td><td>31.3</td><td>-21.4</td></tr><tr><td>Up</td><td>非金属矿采选业</td><td>Non-metallic mineral mining</td><td>Yes</td><td>20</td><td>-4.1</td><td>-3.4</td><td>-3.3</td><td>-0.4</td><td>3.7</td><td>0.0</td></tr><tr><td>Middle</td><td>电力、热力的生产和供应业</td><td>Electricity and heat production/supply</td><td></td><td>32</td><td>-4.2</td><td>-4.4</td><td>-4.4</td><td>-12.3</td><td>4.0</td><td>-5.1</td></tr><tr><td>Middle</td><td>燃气生产和供应业</td><td>Gas production/supply</td><td></td><td></td><td>-0.6</td><td>2.5</td><td>4.0</td><td>3.2</td><td>12.6</td><td>15.4</td></tr><tr><td>Middle</td><td>水的生产和供应业</td><td>Water production/supply</td><td></td><td></td><td>1.6</td><td>1.7</td><td>0.9</td><td>0.4</td><td>1.6</td><td>-1.6</td></tr><tr><td>Middle</td><td>黑色金属冶炼及压延加工业</td><td>Ferrous metal smelting</td><td></td><td></td><td>-1.1</td><td>1.0</td><td>3.1</td><td>4.1</td><td>8.7</td><td>9.2</td></tr><tr><td>Middle</td><td>有色金属冶炼及压延加工业</td><td>Non-ferrous metal smelting</td><td></td><td></td><td>22.5</td><td>24.0</td><td>23.4</td><td>25.6</td><td>9.6</td><td>4.9</td></tr><tr><td>Middle</td><td>金属制品业</td><td>Metal products</td><td></td><td></td><td>0.5</td><td>0.8</td><td>1.6</td><td>2.4</td><td>1.6</td><td>2.0</td></tr><tr><td>Middle</td><td>非金属矿物制品业</td><td>Non-metallic mineral products mfg</td><td>Yes</td><td>46</td><td>-5.5</td><td>-5.1</td><td>-4.4</td><td>-3.5</td><td>-5.1</td><td>-5.8</td></tr><tr><td>Middle</td><td>化学原料及化学制品制造业</td><td>Chemical</td><td></td><td></td><td>8.9</td><td>12.7</td><td>11.3</td><td>66.9</td><td>71.5</td><td>37.3</td></tr><tr><td>Middle</td><td>纺织业</td><td>Textile</td><td></td><td></td><td>0.2</td><td>1.1</td><td>1.5</td><td>4.9</td><td>7.9</td><td>6.6</td></tr><tr><td>Down</td><td>农副食品加工业</td><td>Agricultural products</td><td>Yes</td><td>38</td><td>-1.3</td><td>-1.4</td><td>-1.2</td><td>-1.2</td><td>-3.5</td><td>-4.7</td></tr><tr><td>Down</td><td>食品制造业</td><td>Food mfg</td><td></td><td>39</td><td>-1.6</td><td>-1.0</td><td>-1.0</td><td>0.4</td><td>3.2</td><td>1.6</td></tr><tr><td>Down</td><td>酒、饮料和精制茶制造业</td><td>Wine and beverage mfg</td><td></td><td>26</td><td>-2.9</td><td>-1.9</td><td>-5.3</td><td>-2.8</td><td>1.2</td><td>-12.3</td></tr><tr><td>Down</td><td>烟草制品业</td><td>Tobacco products</td><td></td><td></td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Down</td><td>纺织服装、服饰业</td><td>Textile and apparel mfg</td><td>Yes</td><td>17</td><td>-1.5</td><td>-1.4</td><td>-1.3</td><td>-3.5</td><td>-0.4</td><td>0.4</td></tr><tr><td>Down</td><td>木材加工及木、竹、藤、棕、草制品业</td><td>Wood and wood products</td><td></td><td>44</td><td>-2.3</td><td>-1.9</td><td>-1.9</td><td>-0.4</td><td>-0.8</td><td>0.0</td></tr><tr><td>Down</td><td>造纸及纸制品业</td><td>Paper and paper products</td><td>Yes</td><td>7</td><td>-1.2</td><td>-0.7</td><td>-0.1</td><td>-3.9</td><td>-0.8</td><td>0.4</td></tr><tr><td>Down</td><td>印刷业和记录媒介的复制</td><td>Printing</td><td></td><td>42</td><td>-2.7</td><td>-2.7</td><td>-2.8</td><td>-2.0</td><td>-1.2</td><td>-2.0</td></tr><tr><td>Down</td><td>医药制造业</td><td>Pharmaceutical mfg</td><td></td><td>30</td><td>-4.7</td><td>-4.5</td><td>-4.5</td><td>-4.3</td><td>-3.5</td><td>-3.5</td></tr><tr><td>Down</td><td>化学纤维制造业</td><td>Chemical fiber mfg</td><td></td><td></td><td>5.4</td><td>8.5</td><td>7.4</td><td>45.6</td><td>50.9</td><td>27.8</td></tr><tr><td>Down</td><td>橡胶和塑料制品业</td><td>Rubber and plastic products mfg</td><td></td><td></td><td>-1.3</td><td>0.5</td><td>1.4</td><td>8.3</td><td>16.3</td><td>15.8</td></tr><tr><td>Down</td><td>通用设备制造业</td><td>General machinery</td><td>Yes</td><td>42</td><td>-1.0</td><td>-0.9</td><td>-0.7</td><td>-1.2</td><td>-0.8</td><td>-0.4</td></tr><tr><td>Down</td><td>汽车制造业</td><td>Auto</td><td></td><td>46</td><td>-2.0</td><td>-2.0</td><td>-2.1</td><td>-2.4</td><td>-2.4</td><td>-0.4</td></tr><tr><td>Down</td><td>铁路、船舶、航空航天和其他运输设备制造</td><td>Railway and other transportation</td><td>Yes</td><td>13</td><td>-0.3</td><td>-0.3</td><td>-0.2</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Down</td><td>计算机、通信和其他电子设备制造业</td><td>Computer and other electronics</td><td></td><td></td><td>1.5</td><td>2.1</td><td>3.3</td><td>7.9</td><td>7.9</td><td>7.9</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

Nominal growth is set to rise further in 26Q2E. CPI averaged 1.1% YoY in the past quarter vs. 0.8% YoY in 26Q1, while PPI rose to 3.6% YoY vs. -0.6% YoY. GDP deflator could rise to 1½ \~2%, lifting nominal growth even as real growth slows – with our GDP forecast at 4.5% YoY for 26Q2E, nominal growth could still challenge the high rate since mid-2023.

We see a plateauing path for inflation in 26H2E. The miss in June for both CPI and PPI is mostly from external volatility, instead of further intensifying domestic weakness – on the former, the corrections seem to have been factored in the data. On the domestic side, stabilization of pork cycle could provide some relief to CPI, while AI inflation creates sporadic gains across CPI and PPI. Domestic demand could remain weak in this K-shaped economy, yet targeted support along with supply-side efforts on anti-involution could capture the downside to prices, in our view. The upcoming Politburo meeting could offer more signals.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at

https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the prece

[中间内容因长度限制已省略]

consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the "Product"), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
