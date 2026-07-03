你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by Ind

[中间内容因长度限制已省略]

ctuations in the nationwide consumer price index. The notional principal of inflation-indexed JGBs changes in line with the rate of change in nationwide CPI inflation from the time of its issuance. The amount of the coupon payment is calculated by multiplying the coupon rate by the notional principal at the time of payment. The maturity value is the amount of the notional principal when the issue becomes due. For JI17 and subsequent issues, the maturity value shall not undercut the face amount. Purchases of investment trusts (and sales of some investment trusts) are subject to a purchase or sales fee of up to $5.5\%$ (tax included) of the transaction amount. Also, a direct cost that may be incurred when selling investment trusts is a fee of up to $2.0\%$ of the unit price at the time of redemption. Indirect costs that may be incurred during the course of holding investment trusts include, for domestic investment trusts, an asset management fee (trust fee) of up to 5.5% (tax included/annualized basis) of the net assets in trust, as well as fees based on investment performance. Other indirect costs may also be incurred. For foreign investment trusts, indirect fees may be incurred during the course of holding such as investment company compensation.

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
