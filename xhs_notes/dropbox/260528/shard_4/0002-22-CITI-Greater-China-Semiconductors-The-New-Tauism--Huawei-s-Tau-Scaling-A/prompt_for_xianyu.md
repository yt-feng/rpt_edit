你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
26 May 2026 10:02:58 ET | 12 pages

# Greater China Semiconductors

The New Tauism: Huawei's Tau Scaling Advances Chip Performance

# CITI'S TAKE

Huawei introduced the Tau (τ) Scaling Law at the IEEE ISCAS on May 25 $^{th}$ , a new design philosophy of chip scaling with time (latency reduction) rather than geometry (transistor shrinkage). Exemplified as LogicFolding, Huawei vertically stacked active tiers of logic, analog, and memory circuits using ultra-fine hybrid bonding (at 1.5μ pitch) and claims to achieve 55% increase in transistor density to 238 MTr/mm $^{2}$ for the Kirin 2026 chip. While the same geometry constraints remain, we view this a credible design response to China's restriction on advanced nodes and a shift towards innovations in chip/circuit/system designs. We expect providers of advanced packaging equipment and services to be key beneficiaries.

Tau Scaling: scaling of time instead of geometry — On May 25 $^{th}$ , Huawei presented at the IEEE ISCAS its Tau ( $\tau$ ) Scaling Law, a new design philosophy of using latency reduction as the primary metric for chip performance. Given Huawei's lack of access to advanced equipment, Huawei aims to narrow the chip performance gap through 3D integration, hybrid bonding, logic/memory fusion, optical I/O, backside power, and EDA flows. Huawei targets to achieve 1.4nm-equivalent logic density by 2031.

LogicFolding: vertical stacking of mobile SoC — The Tau Scaling was implemented first on Huawei's mobile SoC using LogicFolding methodology. Logic, analog, and memory circuits across vertically stacked active tiers are bonded using ultra-fine-pitch hybrid bonding, acting as a single continuous fabric. The Kirin 2026 chip achieved a $1.5\mu$ hybrid bonding pitch. Huawei claims a $55\%$ increase in transistor density (from 155 to 238 MTr/mm²) and a $41\%$ power-efficiency gain at a fixed device node, and forecasts transistor density to $>400$ MTr/mm² from 2026 to 2035.

Tau Scaling achievement and limitation — We view Huawei's Tau Scaling a credible design response to China's restriction on advanced nodes. Huawei pushes ahead chip performance through innovations across transistor, circuitry, chip, and system levels. That said, the geometry shrinkage remains given lack of EUV lithography. The 238 MTr/mm $^{2}$ density in 3D does not equate to density in planar designs. 3D design could also lead to new challenges in thermal constraints and EDA limitations.

Implications — We believe Tau Scaling signals a shift towards chip/circuit/system design innovations, which could become more popularized if proven effective. We expect key beneficiaries in 1) advanced packaging equipment – especially providers of hybrid bonders, 2) OSAT – given rising packaging complexity, 3) foundry – given advanced chip design, and 4) EDA – to support 3D design. Within our coverage, we favor ASMPT given its broadening advanced packaging solution offerings.

Kevin Chen $^{AC}$

+852-2501-2125

kevin.y.chen@citi.com

Laura (Chia Yi) Chen

+886-2-8726-9090

laura.cy.chen@citi.com

Kyna Wong

kyna.wong@citi.com

Karen Huang

karen.xw.huang@citi.com

Figure 1. Comparison – Geometry Scaling vs. Tau (Time) Scaling 

<table><tr><td>Geometry Scaling</td><td>Tau (τ) Scaling</td></tr><tr><td>Transistor shrinkage</td><td>Signal latency reduction</td></tr><tr><td>Transistor density</td><td>Compute + memory + interconnect efficiency</td></tr><tr><td>2D planar scaling</td><td>3D stacking + hybrid bonding</td></tr><tr><td>Advanced foundry capability</td><td>Advanced packaging, EDA design, system architecture</td></tr><tr><td>Device performance optimization</td><td>Full stack co-optimization</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi

Figure 2. Huawei Kirin Performance Comparison 

<table><tr><td>Year</td><td>SoC</td><td>Architecture</td><td>Frequency (GHz)</td><td>State</td></tr><tr><td>2023</td><td>Kirin9000s</td><td>Planar</td><td>2.6</td><td>Mass production</td></tr><tr><td>2024</td><td>Kirin9020</td><td>Planar</td><td>2.65</td><td>Mass production</td></tr><tr><td>2025</td><td>Kirin9030 pro</td><td>Planar</td><td>2.75</td><td>Mass production</td></tr><tr><td>2026</td><td>Kirin 2026</td><td>LogicFolding</td><td>3.1</td><td>Silicon</td></tr><tr><td>2027</td><td>Kirin 2027</td><td>LogicFolding</td><td>3.39</td><td>Silicon</td></tr><tr><td>2028</td><td>Kirin 2028</td><td>LogicFolding</td><td>3.71</td><td>Pre-silicon</td></tr><tr><td>2029</td><td>Kirin 2029</td><td>LogicFolding</td><td>4</td><td>Pre-silicon</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi

Figure 3. Share Price Movement – by Sectors 

<table><tr><td>26-May-2026</td><td>1D</td><td>1W</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td></tr><tr><td>Foundry</td><td>2.2%</td><td>21.4%</td><td>37.3%</td><td>29.1%</td><td>56.3%</td><td>178.4%</td></tr><tr><td>OSAT</td><td>7.3%</td><td>28.2%</td><td>65.5%</td><td>41.5%</td><td>85.9%</td><td>132.9%</td></tr><tr><td>Equipment - Front end</td><td>-3.0%</td><td>5.8%</td><td>41.9%</td><td>32.7%</td><td>74.0%</td><td>149.8%</td></tr><tr><td>Equipment - Back end</td><td>-1.0%</td><td>10.1%</td><td>47.8%</td><td>67.3%</td><td>193.3%</td><td>355.0%</td></tr><tr><td>CPU / SoC</td><td>-1.1%</td><td>4.9%</td><td>26.3%</td><td>27.7%</td><td>55.9%</td><td>87.7%</td></tr><tr><td>GPU / ASIC</td><td>0.1%</td><td>3.4%</td><td>12.8%</td><td>46.0%</td><td>9.9%</td><td>37.2%</td></tr><tr><td>Memory</td><td>-3.1%</td><td>4.2%</td><td>63.3%</td><td>65.4%</td><td>97.5%</td><td>297.4%</td></tr><tr><td>SiPh / CPO</td><td>-2.1%</td><td>5.2%</td><td>27.0%</td><td>88.9%</td><td>195.7%</td><td>722.3%</td></tr><tr><td>Analog</td><td>-3.4%</td><td>2.9%</td><td>26.7%</td><td>46.5%</td><td>70.7%</td><td>83.1%</td></tr><tr><td>Power - IDM &amp; Fabless</td><td>-0.9%</td><td>10.4%</td><td>30.7%</td><td>11.8%</td><td>58.6%</td><td>95.8%</td></tr><tr><td>Power - Wide Bandgap</td><td>0.7%</td><td>1.3%</td><td>26.2%</td><td>24.8%</td><td>36.3%</td><td>45.8%</td></tr><tr><td>CIS</td><td>-2.5%</td><td>2.3%</td><td>13.3%</td><td>-2.6%</td><td>2.8%</td><td>1.3%</td></tr><tr><td>RF</td><td>-4.3%</td><td>-4.0%</td><td>10.7%</td><td>15.9%</td><td>26.6%</td><td>32.2%</td></tr><tr><td>EDA / Design service</td><td>-2.4%</td><td>11.6%</td><td>30.7%</td><td>14.1%</td><td>37.2%</td><td>115.4%</td></tr><tr><td>Wafer</td><td>-4.8%</td><td>-7.7%</td><td>24.9%</td><td>14.6%</td><td>33.9%</td><td>48.3%</td></tr><tr><td>Materials</td><td>-1.3%</td><td>0.0%</td><td>19.1%</td><td>38.6%</td><td>104.1%</td><td>155.7%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: dataCentral, Citi

Figure 4. Share Price Movement – 1 Day   
![](images/127114d80b553a942460105b7438e916d055771afa8d2263bd494c83df28523d.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| OSAT | 7.2 |
| Foundry | 2.0 |
| Power - Wide Bandgap | 0.8 |
| GPU / ASIC | 0.1 |
| Power - IDM & Fabless | -0.5 |
| Equipment - Back end | -0.7 |
| CPU / SoC | -0.9 |
| Materials | -1.2 |
| SiPh / CPO | -1.8 |
| EDA / Design service | -2.3 |
| CIS | -2.5 |
| Equipment - Front end | -2.9 |
| Memory | -3.1 |
| Analog | -3.6 |
| RF | -4.2 |
| Wafer | -4.8 |
1-Day Avg Px Move
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: dataCentral, Citi

Figure 5. Share Price Movement – 1 Week   
![](images/8c4770d3b52e6532635728672c0509093740a6b038fd5598ba7f695f9ea97d9d.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| OSAT | 28.5 |
| Foundry | 21.0 |
| EDA / Design service | 11.5 |
| Power - IDM & Fabless | 10.5 |
| Equipment - Back end | 9.5 |
| Equipment - Front end | 6.0 |
| SiPh / CPO | 5.5 |
| CPU / SoC | 5.0 |
| Memory | 4.5 |
| GPU / ASIC | 3.5 |
| Analog | 3.0 |
| CIS | 2.0 |
| Power - Wide Bandgap | 1.0 |
| Materials | -3.0 |
| RF | -4.0 |
| Wafer | -7.0 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: dataCentral, Citi

# ASMPT

(0522.HK; HK\$204.6; 1; 26 May 26; 16:10)

# Valuation

Our target price of HK\$180 is based on peak valuation of 37x 2027E P/E. We view the peak valuation as justified because we expect strong revenue and earnings recovery driven by: 1) AI-driven advanced packaging order wins, including TCB for HBM and CoW applications; and 2) ongoing recovery of mainstream SEMI and SMT. Potential sales of SMT business could solidify its market position as a leading provider of advanced packaging solutions, leading to valuation re-rating beyond its historical range.

# Risks

Downside risks to our target price being achieved include: 1) a slowdown in AI infrastructure outlook with delayed investment; 2) TCB market share loss at key customers; 3) reduced TCB demand due to alternative technologies, such as hybrid bonding; 4) intensifying industry competition; and 5) export restriction extending to back-end equipment.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

# Appendix A-1

# ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

# IMPORTANT DISCLOSURES

# ASMPT (0522.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Kevin Chen

![](images/b12c326fd2e44f6daa2446a5d618d63b3d32ab2a22d788957382ca11373237e6.jpg)

<details>
<summary>line</summary>

| Date       | Value |
| ---------- | ----- |
| J 2024     | 1     |
| A 2024     | 2     |
| O 2024     | 3     |
| N 2024     | 4     |
| D 2024     | 5     |
| F 2024     | 6     |
| M 2024     | 7     |
| A 2024     | 8     |
| M 2024     | 9     |
| J 2025     | 10    |
| J 2025     | 11    |
| A 2025     | 12    |
| M 2025     | 13    |
| A 2025     | 14    |
| M 2025     | 15    |
| J 2026     | 16    |
| A 2026     | 17    |
| S 2026     | 18    |
| O 2026     | 19    |
| N 2026     | 20    |
| D 2026     | 21    |
| J 2027     | 22    |
| F 2027     | 23    |
| M 2027     | 24    |
| A 2027     | 25    |
| M 2027     | 26    |
| A 2028     | 27    |
| M 2028     | 28    |
| A 2029     | 29    |
| M 2029     | 30    |
| A 2030     | 31    |
| M 2030     | 32    |
| A 2031     | 33    |
| M 2031     | 34    |
| A 2032     | 35    |
| M 2032     | 36    |
| A 2033     | 37    |
| M 2033     | 38    |
| A 2034     | 39    |
| M 2034     | 40    |
| A 2035     | 41    |
| M 2035     | 42    |
| A 2036     | 43    |
| M 2036     | 44    |
| A 2037     | 45    |
| M 2037     | 46    |
| A 2038     | 47    |
| M 2038     | 48    |
| A 2039     | 49    |
| M 2039     | 50    |
| A 2040     | 51    |
| M 2040     | 52    |
| A 2041     | 53    |
| M 2041     | 54    |
| A 2042     | 55    |
| M 2042     | 56    |
| A 2043     | 57    |
| M 2043     | 58    |
| A 2044     | 59    |
| M 2044     | 60    |
| A 2045     | 61    |
| M 2045     | 62    |
| A 2046     | 63    |
| M 2046     | 64    |
| A 2047     | 65    |
| M 2047     | 66    |
| A 2048     | 67    |
| M 2048     | 68    |
| A 2049     | 69    |
| M 2049     | 70    |
| A 2050     | 71    |
| M 2050     | 72    |
| A 2051     | 73    |
| M 2051     | 74    |
| A 2052     | 75    |
| M 2052     | 76    |
| A 2053     | 77    |
| M 2053     | 78    |
| A 2054     | 79    |
| M 2054     | 80    |
| A 2055     | 81    |
| M 2055     | 82    |
| A 2056     | 83    |
| M 2056     | 84    |
| A 2057     | 85    |
| M 2057     | 86    |
| A 2058     | 87    |
| M 2058     | 88    |
| A 2059     | 89    |
| M 2059     | 90    |
| A 2060     | 91    |
| M 2060     | 92    |
| A 2061     | 93    |
| M 2061     | 94    |
| A 2062     | 95    |
| M 2062     | 96    |
| A 2063     | 97    |
| M 2063     | 98    |
| A 2064     | 99    |
| M 2064     | 100   |
| A 2065     | -     |
| M 2065     | -     |
| A 2066     | -     |
| M 2066     | -     |
| A 2067     | -     |
| M 2067     | -     |
| A 2068     | -     |
| M 2068     | -     |
| A 2069     | -     |
| M 2069     | -     |
| A 2070     | -     |
| M 2070     | -     |
| A 2071     | -     |
| M 2071     | -     |
| A 2072     | -     |
| M 2072     | -     |
| A 2073     | -     |
| M 2073     | -     |
| A 2074     | -     |
| M 2074     | -     |
| A 2075     | -     |
| M 2075     | -     |
| A 2076     | -     |
| M 2076     | -     |
| A 2077     | -     |
| M 2077     | -     |
| A 2078     | -     |
| M 2078     | -     |
| A 2079     | -     |
| M 2079     | -     |
| A 2080     | -     |
| M 2080     | -     |
| A 2081     | -     |
| M 2081     | -     |
| A 2082     | -     |
| M 2082     | -     |
| A 2083     | -     |
| M 2083     | -     |
| A 2084     | -     |
| M 2084     | -     |
| A 2085     | -     |
| M 2085     | -     |
| A 2086     | -     |
| M 2086     | -     |
| A 2087     | -     |
| M 2087     | -     |
| A 2088     | -     |
| M 2088     | -     |
| A 2089     | -     |
| M 2089     | -     |
| A 2090     | -     |
| M 2090     | -     |
| A 2091     | -     |
| M 2091     | -     |
| A 2092     | -     |
| M 2092     | -     |
| A 2093     | -     |
| M 2093     | -     |
| A 2094     | -     |
| M 2094     | -     |
| A 2095     | -     |
| M 2095     | -     |
| A 2096     | -     |
| M 2096     | -     |
| A 2097     | -     |
| M 2097     | -     |
| A 2098     | -     |
| M 2098     | -     |
| A 2099     | -     |
| M 2099     | -     |
| A          | -1    |

Note: The data series is labeled as 'Covered' or 'Not covered'. The values for 'Covered' are explicitly labeled on the chart.
</details>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>28-May-23 23:18:47</td><td>2</td><td>*63.00</td><td>62.89</td></tr><tr><td>2</td><td>26-Jul-23 21:43:15</td><td>2</td><td>*85.00</td><td>78.46</td></tr><tr><td>3</td><td>25-Oct-23 19:24:43</td><td>*1</td><td>85.00</td><td>67.92</td></tr><tr><td>4</td><td>28-Feb-24 17:15:12</td><td>1</td><td>*120.00</td><td>90.64</td></tr><tr><td>5</td><td>24-Apr-24 15:46:35</td><td>1</td><td>*140.00</td><td>100.84</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>24-Jul-24 08:56:09</td><td>1</td><td>*110.00</td><td>87.21</td></tr><tr><td>7</td><td>31-Oct-24 04:34:18</td><td>1</td><td>*105.00</td><td>84.08</td></tr><tr><td>8</td><td>26-Feb-25 12:15:35</td><td>1</td><td>*75.00</td><td>63.47</td></tr><tr><td>9</td><td>01-May-25 13:33:57</td><td>1</td><td>*65.00</td><td>51.73</td></tr><tr><td>10</td><td>23-Jul-25 13:13:41</td

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
