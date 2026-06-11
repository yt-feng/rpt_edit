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
09 Jun 2026 09:01:07 ET | 10 pages

# Greater China Semiconductors

## China's New Rmb2tn AI Investment Plan Positive for Domestic AI Supply Chain

## CITI'S TAKE

Bloomberg reported on June $9^{\text{th}}$ that China is preparing to invest Rmb2tn (US\$295bn) over the next 5 years on data centers/networks to support its domestic AI sector. Chinese telcos will operate the data centers using at least 80% local AI accelerators. We view the new initiative as positive to: 1) foundries SMIC, Hua Hong (both covered by Laura Chen); 2) OSATs JCET, Tongfu, 3) equipment suppliers ASMPT, Vital Deeptech; and 4) AI accelerator vendors; given a clearer roadmap ahead for China's AI localization. The 80%+ AI chip localization target should be achievable as domestic AI chip vendors have effectively captured the commanding majority of China's AI accelerator market this year with Nvidia H200 import largely stalled. This may also be more constructive to smaller AI chip vendors as state-funded data centers are more willing to purchase from a broader range of suppliers, in our view.

Figure 1. China AI Accelerator Comparison

<table><tr><td rowspan="2">Vendor</td><td rowspan="2">Model</td><td rowspan="2">Node</td><td colspan="2">Performance (PELOP)</td><td colspan="3">Memory</td></tr><tr><td>FP16</td><td>FP8</td><td>Type</td><td>Size</td><td>Bandwidth</td></tr><tr><td>Nvidia</td><td>H200</td><td>4nm</td><td>2.0</td><td>4.0</td><td>HBM3e</td><td>141GB</td><td>4.8 TB/s</td></tr><tr><td>Nvidia</td><td>H20</td><td>5nm</td><td>0.3</td><td>0.6</td><td>HBM3</td><td>96GB</td><td>4.0 TB/s</td></tr><tr><td>Huawei</td><td>910B</td><td>7nm</td><td>0.4</td><td>0.8</td><td>HBM2e</td><td>64GB</td><td>1.6 TB/s</td></tr><tr><td>Huawei</td><td>910C</td><td>7nm</td><td>0.8</td><td>1.6</td><td>HBM2e</td><td>96GB</td><td>3.2 TB/s</td></tr><tr><td>Huawei</td><td>920</td><td>6nm</td><td>0.9</td><td>1.8</td><td>HBM3</td><td>128GB</td><td>4.0 TB/s</td></tr><tr><td>Huawei</td><td>950 PR</td><td>6nm</td><td>1.0</td><td>2.0</td><td>HBM3e</td><td>192GB</td><td>1.6 TB/s</td></tr><tr><td>Huawei</td><td>950 DT</td><td>6nm</td><td>1.0</td><td>2.0</td><td>HBM3e</td><td>256GB</td><td>4.0 TB/s</td></tr><tr><td>Cambricon</td><td>S590</td><td>7nm</td><td>0.3</td><td>0.6</td><td>HBM2e</td><td>64GB</td><td>1.6 TB/s</td></tr><tr><td>Cambricon</td><td>S690</td><td>7nm</td><td>0.7</td><td>1.4</td><td>HBM3</td><td>96GB</td><td>2.4 TB/s</td></tr><tr><td>Baidu (Kunlun)</td><td>P800</td><td>7nm</td><td>0.3</td><td>0.7</td><td>HBM2e</td><td>64GB</td><td>0.8 GB/s</td></tr><tr><td>Baidu (Kunlun)</td><td>P900</td><td>7nm</td><td>0.5</td><td>1.0</td><td>HBM3</td><td>96GB</td><td>1.6 TB/s</td></tr><tr><td>Biren</td><td>BR100</td><td>7nm</td><td>1.0</td><td>2.0</td><td>HBM2e</td><td>64GB</td><td>1.2 TB/s</td></tr><tr><td>Iluvatar CoreX</td><td>V100</td><td>7nm</td><td>0.2</td><td>0.4</td><td>HBM2e</td><td>32GB</td><td>2.4 TB/s</td></tr><tr><td>Iluvatar CoreX</td><td>V200</td><td>7nm</td><td>0.4</td><td>0.8</td><td>HBM3</td><td>64GB</td><td>2.3 TB/s</td></tr><tr><td>MetaX</td><td>C500</td><td>7nm</td><td>0.2</td><td>0.4</td><td>HBM3</td><td>48GB</td><td>0.8 GB/s</td></tr><tr><td>MetaX</td><td>C600</td><td>6nm</td><td>0.3</td><td>0.6</td><td>HBM3</td><td>80GB</td><td>1.6 TB/s</td></tr><tr><td>Moore Threads</td><td>S4000</td><td>7nm</td><td>0.1</td><td>0.2</td><td>GDDR6</td><td>48GB</td><td>0.8 GB/s</td></tr><tr><td>Moore Threads</td><td>S5000</td><td>7nm</td><td>0.5</td><td>1.0</td><td>HBM</td><td>80GB</td><td>1.6 TB/s</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi

## Kevin Chen $^{AC}$

+852-2501-2125

kevin.y.chen@citi.com

## Kyna Wong

+852-2868-7820

kyna.wong@citi.com

## Yiming Li, CFA

+852-2501-2857

yiming.li@citi.com

## Karen Huang

+852-2501-2755

karen.xw.huang@citi.com

## See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

Figure 2. Share Price Movement – by Sectors

<table><tr><td>9-Jun-2026</td><td>1W</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td></tr><tr><td>Foundry</td><td>-4.8%</td><td>13.6%</td><td>32.9%</td><td>43.6%</td><td>158.9%</td></tr><tr><td>OSAT</td><td>-1.7%</td><td>28.3%</td><td>31.1%</td><td>61.8%</td><td>103.9%</td></tr><tr><td>Equipment - Front end</td><td>4.8%</td><td>17.6%</td><td>35.2%</td><td>49.3%</td><td>127.5%</td></tr><tr><td>Equipment - Back end</td><td>4.6%</td><td>20.1%</td><td>62.7%</td><td>142.4%</td><td>306.8%</td></tr><tr><td>CPU / SoC</td><td>-6.6%</td><td>-8.6%</td><td>13.3%</td><td>27.2%</td><td>54.3%</td></tr><tr><td>GPU / ASIC</td><td>0.5%</td><td>-8.2%</td><td>34.4%</td><td>0.4%</td><td>34.8%</td></tr><tr><td>Memory</td><td>2.2%</td><td>16.6%</td><td>51.2%</td><td>81.9%</td><td>265.2%</td></tr><tr><td>SiPh / CPO</td><td>5.0%</td><td>18.1%</td><td>82.4%</td><td>183.8%</td><td>743.2%</td></tr><tr><td>Analog</td><td>2.2%</td><td>10.9%</td><td>39.5%</td><td>68.3%</td><td>70.9%</td></tr><tr><td>Power - IDM &amp; Fabless</td><td>1.7%</td><td>21.5%</td><td>22.1%</td><td>52.0%</td><td>90.2%</td></tr><tr><td>Power - Wide Bandgap</td><td>0.9%</td><td>13.7%</td><td>24.5%</td><td>26.0%</td><td>43.7%</td></tr><tr><td>CIS</td><td>-2.6%</td><td>-5.4%</td><td>-10.1%</td><td>-8.1%</td><td>-11.6%</td></tr><tr><td>RF</td><td>0.5%</td><td>-8.5%</td><td>-1.9%</td><td>12.3%</td><td>15.2%</td></tr><tr><td>EDA / Design service</td><td>2.4%</td><td>-1.0%</td><td>7.3%</td><td>21.0%</td><td>68.0%</td></tr><tr><td>Wafer</td><td>20.0%</td><td>22.9%</td><td>48.3%</td><td>53.0%</td><td>68.6%</td></tr><tr><td>Materials</td><td>11.5%</td><td>11.8%</td><td>48.2%</td><td>94.6%</td><td>151.7%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: dataCentral, Citi

## Companies Mentioned:

ASMPT (0522.HK; HK\$185.3; 1; 09 Jun 26; 16:10) | Baidu Inc (9888.HK; HK\$116.6; Not Rated; 09 Jun 26; 16:10) | Baidu.com (BIDU.O; US\$119.1; 1; 08 Jun 26; 16:00) | Cambricon Technologies Corp Ltd (688256.SS; Rmb1270.01; Not Rated; 09 Jun 26; 15:00) | Hua Hong Grace Semiconductor (1347.HK; HK\$140.1; 1; 09 Jun 26; 16:10) | JCET Group (600584.SS; Rmb75.29; 1; 09 Jun 26; 15:00) | MetaX Integrated Circuits (Shanghai) Co Ltd (688802.SS; Rmb704.98; Not Rated; 09 Jun 26; 15:00) | Moore Threads Technology Co Ltd (688795.SS; Rmb615.89; Not Rated; 09 Jun 26; 15:00) | NVIDIA Corp (NVDA.O; US\$208.64; 1; 08 Jun 26; 16:00) | Shanghai Biren Technology Co Ltd (6082.HK; HK\$54.5; Not Rated; 09 Jun 26; 16:10) | Shanghai Iluvatar CoreX Semiconductor Co Ltd (9903.HK; HK\$515.5; Not Rated; 09 Jun 26; 16:10) | Shanghai Vital Deeptech (600641.SS; Rmb27.03; 3; 09 Jun 26; 15:00) | SMIC (0981.HK; HK\$75.0; 1; 09 Jun 26; 16:10) | TongFu Microelectronics (002156.SZ; Rmb64.43; 1; 09 Jun 26; 15:00)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>The Firm has made a market in the publicly traded equity securities of Shanghai Biren Technology Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Baidu Inc on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Semiconductor Manufacturing International Corp is subject to Executive Order 13959 described below.The Firm has made a market in the publicly traded equity securities of Semiconductor Manufacturing International Corp on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of ASMPT Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Hua Hong Grace Semiconductor Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from ASMPT,Baidu.com,JCET Group,NVIDIA Corp,TongFu Microelectronics in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: ASMPT,Baidu.com,JCET Group,NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: ASMPT,Baidu.com,JCET Group,NVIDIA Corp,TongFu Microelectronics.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Baidu.com,NVIDIA Corp. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>The Firm is a market maker in the publicly traded equity securities of ASMPT,Baidu.com,Hua Hong Grace Semiconductor,SMIC,Shanghai Biren Technology Co Ltd.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.</td></tr></table>

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Apr 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>8%</td><td>37%</td><td>47%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>41%</td><td>28%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks.

Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
