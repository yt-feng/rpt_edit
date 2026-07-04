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
EQUITY: JAPAN MACHINERY

## Airtac sales up 28% y-y in June

Down m-m, partly for seasonal reasons

Airtac daily sales estimated to be up 22% y-y and down 11% m-m in June
Taiwanese pneumatic equipment manufacturer Airtac [1590 TT], which generates around 90% of its sales in China, released June sales data on 2 July, with CNY-denominated sales up 28% y-y and down 1% m-m (Figure 4). We estimate that daily sales were up 22% y-y and down 11% m-m (based on 23 business days). Daily sales tend to fall m-m in June and July owing to seasonality (Figure 1). Apr–Jun sales were TWD12.2bn, exceeding our TWD11.6bn forecast.

Management's comments were largely unchanged from the previous month. The company said order value this month has stayed above shipment value and that both have been trending higher than it had been anticipating. Quarterly sales stayed at a record high as market demand is in an upcycle. The company said the 15th five-year medium-term business plan released by the Chinese government focuses on smart manufacturing and industrial advancement, and it expects both to contribute to increased demand in the pneumatic equipment market. It expects the government to continue to announce support measures as needed. It maintains an optimistic view on pneumatic industry demand in FY26.

User industry breakdown: Solid y-y performance across user industries other than energy and lighting

By user industry, we estimate sales rose 25% y-y in electronics (27% sales weighting), rose 50% in batteries (17%), rose 30% in autos (10%), rose 15% in packaging machinery (7%), rose 45% in machine tools (8%), rose 28% in general machinery (5%), rose 19% in textile machinery (4%), and fell 8% in energy and lighting (solar-power related) (3%). Daily sales fell m-m for all user industries, but the declines for autos and electronics were relatively small. In absolute terms, sales to the auto and machine tool industries have continued to rise, and those to the electronics and battery industries have been on a slight downward trend since peaking in April.

We think machine tool orders as tracked by the Japan Machine Tool Builders' Association could well peak in the near term, partly for seasonal reasons. Monthly data from Airtac shows consistently strong demand from the auto industry, and it remains to be seen whether there will be an immediate slowdown in demand from the automotive industry, which hit an all-time high in Chinese machine tool orders in May. In China, the five-year plan includes plans for AI and data center-related investment, and we expect these areas to continue to drive demand over the longer term.

## Research Analysts

Japan machinery
Kentaro Maekawa - NSC
kentaro.maekawa@NOM.com
+81 3 6703 1208

Angela Yang - NSC
wenching.yang@NOM.com
+81 3 6703 1819

## Reference figures

Fig. 1: Airtac daily sales Sales tend to decline m-m in June and July owing to seasonality  
![](images/8edd38e89eb4b2c698a222a70836359bcebdcec763d0a0e2bf98acb524bfeadc.jpg)  
Note: Daily sales = monthly sales ÷ number of business days.
Source: NOM, based on company data

Fig. 2: China: Total social financing, Airtac sales, Komtrax operating hours, machine tool orders  
![](images/9053816e56cd133bdeb1a49c1a6c36f5eddfbb13244eee712be19e9553e58578.jpg)  
Source: NOM, based on People's Bank of China data, Cheung Kong Graduate School of Business data, data disclosed by each company, and Japan Machine Tool Builders' Association data

Fig. 3: Airtac's sales mix by user industry Broad mix of customer industries, biggest is electronics

<table><tr><td>(%)</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>Electronics</td><td>25</td><td>22</td><td>29</td><td>27</td></tr><tr><td>Machinery</td><td>13</td><td>12</td><td>14</td><td>13</td></tr><tr><td>Batteries</td><td>17</td><td>14</td><td>8</td><td>14</td></tr><tr><td>Packaging</td><td>7</td><td>8</td><td>9</td><td>9</td></tr><tr><td>Autos</td><td>6</td><td>6</td><td>8</td><td>10</td></tr><tr><td>Energy and lighting</td><td>6</td><td>13</td><td>5</td><td>3</td></tr><tr><td>Other</td><td>26</td><td>25</td><td>27</td><td>24</td></tr></table>

Source: NOM, based on company data

Fig. 4: China: Airtac sales, Komtrax operating hours, JMTBA machine tool orders for general machinery in China  
Key data for considering machinery demand in China

<table><tr><td rowspan="2"></td><td colspan="2">Airtac sales</td><td colspan="2">Komtrax China</td><td colspan="2">JMTBA: China orders, general machinery</td></tr><tr><td>(CNY &#x27;000)</td><td>(y-y)</td><td>(Hours)</td><td>(y-y)</td><td>(¥mn)</td><td>(y-y)</td></tr><tr><td>24/1</td><td>658,253</td><td>102%</td><td>80</td><td>88%</td><td>9,384</td><td>-1%</td></tr><tr><td>2</td><td>323,593</td><td>-39%</td><td>28</td><td>-62%</td><td>7,349</td><td>-18%</td></tr><tr><td>3</td><td>668,579</td><td>-4%</td><td>92</td><td>-11%</td><td>8,958</td><td>16%</td></tr><tr><td>4</td><td>698,022</td><td>15%</td><td>97</td><td>-4%</td><td>8,364</td><td>-19%</td></tr><tr><td>5</td><td>627,134</td><td>-1%</td><td>101</td><td>1%</td><td>9,852</td><td>15%</td></tr><tr><td>6</td><td>565,363</td><td>-4%</td><td>88</td><td>-3%</td><td>13,358</td><td>67%</td></tr><tr><td>7</td><td>549,841</td><td>-1%</td><td>88</td><td>-1%</td><td>9,795</td><td>34%</td></tr><tr><td>8</td><td>541,490</td><td>-7%</td><td>93</td><td>3%</td><td>9,199</td><td>14%</td></tr><tr><td>9</td><td>547,280</td><td>-7%</td><td>95</td><td>7%</td><td>9,744</td><td>20%</td></tr><tr><td>10</td><td>510,106</td><td>-6%</td><td>105</td><td>4%</td><td>9,369</td><td>63%</td></tr><tr><td>11</td><td>571,907</td><td>0%</td><td>105</td><td>4%</td><td>8,593</td><td>17%</td></tr><tr><td>12</td><td>621,207</td><td>11%</td><td>108</td><td>19%</td><td>12,320</td><td>18%</td></tr><tr><td>25/1</td><td>494,763</td><td>-25%</td><td>66</td><td>-18%</td><td>9,749</td><td>4%</td></tr><tr><td>2</td><td>526,614</td><td>63%</td><td>56</td><td>98%</td><td>9,017</td><td>23%</td></tr><tr><td>3</td><td>773,101</td><td>16%</td><td>94</td><td>2%</td><td>12,908</td><td>44%</td></tr><tr><td>4</td><td>776,591</td><td>11%</td><td>98</td><td>1%</td><td>10,809</td><td>29%</td></tr><tr><td>5</td><td>668,675</td><td>7%</td><td>93</td><td>-7%</td><td>10,401</td><td>6%</td></tr><tr><td>6</td><td>656,312</td><td>16%</td><td>81</td><td>-7%</td><td>12,112</td><td>-9%</td></tr><tr><td>7</td><td>648,335</td><td>18%</td><td>87</td><td>-2%</td><td>11,279</td><td>15%</td></tr><tr><td>8</td><td>615,003</td><td>14%</td><td>83</td><td>-11%</td><td>11,280</td><td>23%</td></tr><tr><td>9</td><td>707,606</td><td>29%</td><td>81</td><td>-15%</td><td>12,200</td><td>25%</td></tr><tr><td>10</td><td>627,824</td><td>23%</td><td>88</td><td>-17%</td><td>13,430</td><td>43%</td></tr><tr><td>11</td><td>690,959</td><td>21%</td><td>100</td><td>-5%</td><td>11,529</td><td>34%</td></tr><tr><td>12</td><td>744,836</td><td>20%</td><td>99</td><td>-8%</td><td>13,247</td><td>8%</td></tr><tr><td>26/1</td><td>817,845</td><td>65%</td><td>91</td><td>38%</td><td>13,655</td><td>40%</td></tr><tr><td>2</td><td>475,088</td><td>-10%</td><td>37</td><td>-34%</td><td>13,328</td><td>48%</td></tr><tr><td>3</td><td>899,165</td><td>16%</td><td>85</td><td>-10%</td><td>17,769</td><td>38%</td></tr><tr><td>4</td><td>937,464</td><td>21%</td><td>92</td><td>-6%</td><td>21,341</td><td>97%</td></tr><tr><td>5</td><td>843,821</td><td>26%</td><td>89</td><td>-5%</td><td>18,095</td><td>74%</td></tr><tr><td>6</td><td>838,485</td><td>28%</td><td></td><td></td><td></td><td></td></tr><tr><td>23/1-2</td><td>860,331</td><td>3%</td><td>118</td><td>0%</td><td>18,378</td><td>3%</td></tr><tr><td>24/1-2</td><td>981,846</td><td>14%</td><td>108</td><td>-8%</td><td>16,733</td><td>-9%</td></tr><tr><td>25/1-2</td><td>1,021,377</td><td>4%</td><td>122</td><td>13%</td><td>18,766</td><td>12%</td></tr><tr><td>26/1-2</td><td>1,292,933</td><td>27%</td><td>128</td><td>5%</td><td>26,983</td><td>44%</td></tr></table>

Fig. 5: Timing of Chinese New Year

<table><tr><td>Year</td><td>Chinese New Year</td></tr><tr><td>11</td><td>3 Feb</td></tr><tr><td>12</td><td>23 Jan</td></tr><tr><td>13</td><td>10 Feb</td></tr><tr><td>14</td><td>31 Jan</td></tr><tr><td>15</td><td>19 Feb</td></tr><tr><td>16</td><td>8 Feb</td></tr><tr><td>17</td><td>28 Jan</td></tr><tr><td>18</td><td>16 Feb</td></tr><tr><td>19</td><td>5 Feb</td></tr><tr><td>20</td><td>25 Jan</td></tr><tr><td>21</td><td>12 Feb</td></tr><tr><td>22</td><td>1 Feb</td></tr><tr><td>23</td><td>22 Jan</td></tr><tr><td>24</td><td>10 Feb</td></tr><tr><td>25</td><td>29 Jan</td></tr><tr><td>26</td><td>17 Feb</td></tr><tr><td>27</td><td>6 Feb</td></tr></table>

Source: NOM  
Source: NOM, based on Japan Machine Tool Builders' Association and company data

Fig. 6: Chinese industrial production: Growth areas  
![](images/a84c2adfe7231d4505ec385c45545cd15f7eaf0a9f739e924f86000796781264.jpg)  
Note: Latest data is for 2026 Q2 (average of Apr and May). Figures inside boxes are most recent available monthly data (May). Figures for Li-ion batteries are through 2024 Q4.  
Source: NOM, based on CEIC (original data is from National Bureau of Statistics of China)

Fig. 7: Chinese industrial production: Cyclical areas  
![](images/ce5c41aff9520ae6b90f145b6ecd534168e5abfe5cfcb65a3b85a8781c562209.jpg)  
Note: Latest data is for 2026 Q2 (average of Apr and May). Figures inside boxes are most recent available monthly data (May).  
Source: NOM, based on CEIC (original data is from National Bureau of Statistics of China)

## Appendix A-1

This report has been produced by NOM Securities Co., Ltd. (NSC), Japan.

See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Kentaro Maekawa and Angela Yang, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

The lists of issuers that are affiliates or subsidiaries of NOM Holdings Inc., the parent company of NOM Securities Co., Ltd., issuers that have officers who concurrently serve as officers of NOM Securities Co., Ltd., issuers in which the NOM Group holds 1% or more of any class of common equity securities and issuers for which NOM Securities Co., Ltd. has lead managed a public offering of equity or equity linked securities in the past 12 months are available at https://www.NOMholdings.com/report/. Please contact the Research Production Operation Dept. of NOM Securities Co., Ltd. for additional information.

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

57% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 34% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

41% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

2% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 0% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

As at 31 March 2026.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at: http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that 

[中间内容因长度限制已省略]

f holding investment trusts include, for domestic investment trusts, an asset management fee (trust fee) of up to 5.5% (tax included/annualized basis) of the net assets in trust, as well as fees based on investment performance. Other indirect costs may also be incurred. For foreign investment trusts, indirect fees may be incurred during the course of holding such as investment company compensation.

Investment trusts invest mainly in securities such as Japanese and foreign equities and bonds, whose prices fluctuate. Investment trust unit prices fluctuate owing to price fluctuations in the underlying assets and to foreign exchange rate fluctuations. As such, investment trusts carry the risk of losses. Fees and risks vary by investment trust. Maximum applicable fees are subject to change; please thoroughly read the written materials provided, such as prospectuses or documents delivered before making a contract.

In interest rate swap transactions and USD/JPY basis swap transactions (“interest rate swap transactions, etc.”), only the agreed transaction payments shall be made on the settlement dates. Some interest rate swap transactions, etc. may require pledging of margin collateral. In some of these cases, transaction payments may exceed the amount of collateral. There shall be no advance notification of required collateral value or collateral ratios as they vary depending on the transaction. Interest rate swap transactions, etc. carry the risk of losses owing to fluctuations in market prices in the interest rate, currency and other markets, as well as reference indices. Losses incurred as such may exceed the value of margin collateral, in which case margin calls may be triggered. In the event that both parties agree to enter a replacement (or termination) transaction, the interest rates received (paid) under the new arrangement may differ from those in the original arrangement, even if terms other than the interest rates are identical to those in the original transaction. Risks vary by transaction. Please thoroughly read the written materials provided, such as documents delivered before making a contract and disclosure statements.

In OTC transactions of credit default swaps (CDS), no sales commission will be charged. When entering into CDS transactions, the protection buyer will be required to pledge or entrust an agreed amount of margin collateral. In some of these cases, the transaction payments may exceed the amount of margin collateral. There shall be no advance notification of required collateral value or collateral ratios as they vary depending on the financial position of the protection buyer. CDS transactions carry the risk of losses owing to changes in the credit position of some or all of the referenced entities, and/or fluctuations of the interest rate market. The amount the protection buyer receives in the event that the CDS is triggered by a credit event may undercut the total amount of premiums that he/she has paid in the course of the transaction. Similarly, the amount the protection seller pays in the event of a credit event may exceed the total amount of premiums that he/she has received in the transaction. All other conditions being equal, the amount of premiums that the protection buyer pays and that received by the protection seller shall differ. In principle, CDS transactions will be limited to financial instruments business operators and qualified institutional investors. Transfers of equities to another securities company via the Japan Securities Depository Center are subject to a transfer fee of up to ¥11,000 (tax included) per issue transferred depending on volume. No account fee will be charged for marketable securities or monies deposited.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved.
"""
