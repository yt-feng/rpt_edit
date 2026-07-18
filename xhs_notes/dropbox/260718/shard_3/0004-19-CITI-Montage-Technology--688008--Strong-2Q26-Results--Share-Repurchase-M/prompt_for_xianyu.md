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
16 Jul 2026 20:09:45 ET | 13 pages

# Montage Technology (688008.SS)

Strong 2Q26 Results, Share Repurchase May Help Stabilize Share Volatility

## CITI'S TAKE

Montage announced on July 16 preliminary 1H26 results with strong 2Q26 net profit in the range of Rmb1,053-1,253mn (66%-98% YoY growth), at 37%/42% above consensus/Citi est. driven by higher revenue scale, GPM expansion, and investment gains. Revenue grew 33% YoY to Rmb1,874mn, at 6%/11% above consensus/Citi est., with interconnect chips revenue growing 28% YoY (+20% QoQ) to Rmb1,694mn. Shipment of DDR5 RCD continues to grow, with Gen 3 and Gen 4 portion further expanded. MRCD/MDB, PCIe retimer, CXL sales notably increased. Montage-A/H share plunged 16%/23% on July 16 after news of Korean prosecutors raiding offices of Montage, Renesas, and Rambus over suspicion of price-fixing collusion (Chosun, July 15). While the investigation is ongoing and could cause further share volatilities, we believe the strong 2Q26 pre-announce and Montage mgmt. announcement for a Rmb300-600mn Montage-A share repurchase plan should help stabilize the share price.

Figure 1. Montage – 2Q26 Preliminary Results vs. Estimates

<table><tr><td rowspan="2">(Rmb mn)</td><td rowspan="2">1Q25</td><td rowspan="2">2Q25</td><td rowspan="2">3Q25</td><td rowspan="2">4Q25</td><td rowspan="2">1Q26</td><td colspan="5">2Q26</td></tr><tr><td>Prelim</td><td>BBG</td><td>Diff</td><td>Citi est</td><td>Diff</td></tr><tr><td>Revenue</td><td>1,222</td><td>1,411</td><td>1,424</td><td>1,399</td><td>1,461</td><td>1,874</td><td>1,773</td><td>6%</td><td>1,682</td><td>11%</td></tr><tr><td>YoY %</td><td>66%</td><td>52%</td><td>57%</td><td>31%</td><td>20%</td><td>33%</td><td>26%</td><td></td><td>19%</td><td></td></tr><tr><td>Gross Profit</td><td>739</td><td>853</td><td>902</td><td>902</td><td>1,019</td><td></td><td>1,215</td><td></td><td>1,130</td><td></td></tr><tr><td>GPM</td><td>60.4%</td><td>60.4%</td><td>63.3%</td><td>64.5%</td><td>69.8%</td><td></td><td>68.5%</td><td></td><td>67.2%</td><td></td></tr><tr><td>Opex</td><td>(278)</td><td>(349)</td><td>(575)</td><td>(353)</td><td>(343)</td><td></td><td>(435)</td><td></td><td>(366)</td><td></td></tr><tr><td>Opex %</td><td>22.7%</td><td>24.8%</td><td>40.3%</td><td>25.3%</td><td>23.5%</td><td></td><td>24.5%</td><td></td><td>21.8%</td><td></td></tr><tr><td>EBIT</td><td>461</td><td>503</td><td>328</td><td>548</td><td>677</td><td></td><td>781</td><td></td><td>763</td><td></td></tr><tr><td>EBIT margin</td><td>37.7%</td><td>35.7%</td><td>23.0%</td><td>39.2%</td><td>46.3%</td><td></td><td>44.0%</td><td></td><td>45.4%</td><td></td></tr><tr><td>Pre-Tax Profit</td><td>531</td><td>655</td><td>507</td><td>628</td><td>877</td><td></td><td>902</td><td></td><td>864</td><td></td></tr><tr><td>Net Profit</td><td>525</td><td>634</td><td>473</td><td>603</td><td>847</td><td>1,153</td><td>842</td><td>37%</td><td>812</td><td>42%</td></tr><tr><td>YoY %</td><td>135%</td><td>71%</td><td>23%</td><td>39%</td><td>61%</td><td>82%</td><td>33%</td><td></td><td>28%</td><td></td></tr><tr><td>EPS (Rmb)</td><td>0.46</td><td>0.55</td><td>0.41</td><td>0.53</td><td>0.69</td><td></td><td>0.67</td><td></td><td>0.66</td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: Company Reports, Bloomberg, Citi Estimates

<table><tr><td colspan="2">Buy</td></tr><tr><td>Price (16 Jul 26 15:00)</td><td>Rmb211.130</td></tr><tr><td>Target price</td><td>Rmb245.000</td></tr><tr><td>Expected share price return</td><td>16.0%</td></tr><tr><td>Expected dividend yield</td><td>0.3%</td></tr><tr><td>Expected total return</td><td>16.3%</td></tr><tr><td>Market Cap</td><td>Rmb241,694MUS$35,704M</td></tr></table>

Kevin Chen $^{AC}$ +852-2501-2125
kevin.y.chen@citi.com

Kyna Wong
kyna.wong@citi.com

Karen Huang

karen.xw.huang@citi.com

Yiming Li, CFA

yiming.li@citi.com

## Bull/Bear: Montage Technology

![](images/6dcfb6684e278584c95220e47241117036681d7218fe1a2d93428384e15f08be.jpg)  
Spread 65pp
Current Price and expected returns (upside/downside) as of 16 Jul 2026

## BULL Assumptions

![](images/63dd2a450c92a7e06ee80b4af07478d20e5e3071eed92b102242fcae1d1953d3.jpg)

• Revenue growth of 35%/38% in 2026E/27E

• Net profit growth of 60%/40% in 2026E/27E

\- 65x 2027E P/E valuation (2SD above 5-year average)

## BASE Assumptions

![](images/b4bcfb45920be51243b1ee855b64a6e4bb702464d417a2672e6f1b32b9233a5b.jpg)

• Revenue growth of 31%/38% in 2026E/27E

• Net profit growth of 50%/40% in 2026E/27E

\- 60x 2027E P/E valuation (1.5SD above 5-year average)

## BEAR Assumptions

![](images/3325bc28481db038c0595ab90026c1305de189c038c92279248aa9e3500e2ca0.jpg)

• Revenue growth of 26%/24% in 2026E/27E

• Net profit growth of 32%/24% in 2026E/27E

• 45x 2027E P/E valuation (5-year average)

## Montage Technology

## Valuation

Our target price of Rmb245 is based on 60x 2027E P/E, at 1.5SD above its 5-year average. We believe the valuation is justified given Montage's improving product mix (DDR5 Gen 3 surpassing Gen 2) and growing contribution from new AI-driven connectivity solutions (MRDIMM, CXL), with demand upside coming from agentic AI and inferencing. The company should continue to benefit from China's increasing semiconductor localization in the coming few years.

## Risks

Key downside risks to our target price include: 1) AI infrastructure capex slowdown, 2) market share loss if international customers shift away from Chinese suppliers; 3) rising SOCAMM / LPDDRX adoption in servers that reduces memory interface demand, 4) delayed product migration (DDR5 sub-gen) and development (PCIe switch, CXL switch).

## Montage Technology

(6809.HK; HK\$278.6; 1; 16 Jul 26; 16:10)

## Valuation

Our target price for Montage-H is set at HK\$305 based on 66x 2027E P/E, at 10% premium to our Montage-A share target multiple. We view Montage-H a rare opportunity for international investors to invest in both China and global AI data center expansion. Such quality name with strong AI-thematic has gained strong traction from international investors and resulted in an unusual H-share premium over its A-share counterpart.

We believe the valuation is justified given Montage's improving product mix (DDR5 Gen 3 surpassing Gen 2) and growing contribution from new AI-driven connectivity solutions (MRDIMM, CXL), with demand upside coming from agentic AI and inferencing. The company should continue to benefit from China's increasing semiconductor localization in the coming few years.

## Risks

Key downside risks to our target price include: 1) AI infrastructure capex slowdown, 2) market share loss if international customers shift away from Chinese suppliers; 3) rising SOCAMM / LPDDRX adoption in servers that reduces memory interface demand, 4) delayed product migration (DDR5 sub-gen) and development (PCIe switch, CXL switch).

Citi's quant system rates Montage-H high-risk given its short trading history. We view Montage's fundamentals remain strong and expect solid AI-driven revenue/earnings momentum in the coming years. As such, we do not assign a High-Risk rating to Montage-H.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

![](images/e8a55ce5ced8ec334723a31cd4ac30641686bc1b820823215bf5ba59c47ecaba.jpg)

<table><tr><td>Date10-Feb-26 04:59:21</td><td>Rating*1</td><td>Target Price*205.00</td><td>Closing Price178.00</td></tr></table>

\*Indicates Change  
Rating/target price changes above reflect Eastern Time

## Montage Technology (688008.SS)

![](images/e37615e1be6f8eea7019dca269cfb36d6367cb284741c3382ff1a1a217cc080c.jpg)  
\*Indicates Change  
Rating/target price changes above reflect Eastern Time

![](images/72d29bc5daa512ffaca4d807674a0eef82111abd8853abf0f319b1fb09d4b274.jpg)  
CW - Catalyst Watch, STV - Short-Term View

![](images/614745ed06e530cf95242eaf5135b86521782e75f2b0e799d93ff9de8ec5fe53.jpg)  
CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

The Firm has made a market in the publicly traded equity securities of Montage Technology Co Ltd on at least one occasion since 1 Jan 2025.

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Montage Technology in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Montage Technology.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Montage Technology.

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive

compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

The Firm is a market maker in the publicly traded equity securities of Montage Technology.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to rev

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
