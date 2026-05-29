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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

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

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>24-Jul-24 08:56:09</td><td>1</td><td>*110.00</td><td>87.21</td></tr><tr><td>7</td><td>31-Oct-24 04:34:18</td><td>1</td><td>*105.00</td><td>84.08</td></tr><tr><td>8</td><td>26-Feb-25 12:15:35</td><td>1</td><td>*75.00</td><td>63.47</td></tr><tr><td>9</td><td>01-May-25 13:33:57</td><td>1</td><td>*65.00</td><td>51.73</td></tr><tr><td>10</td><td>23-Jul-25 13:13:41</td><td>1</td><td>*75.00</td><td>62.91</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>11 11-Aug-25 11:00:54</td><td>1</td><td>*85.00</td><td>69.88</td></tr><tr><td>12 31-Oct-25 03:41:57</td><td>1</td><td>*100.00</td><td>81.63</td></tr><tr><td>13 21-Jan-26 18:19:50</td><td>1</td><td>*125.00</td><td>101.34</td></tr><tr><td>14 04-Mar-26 15:09:09</td><td>1</td><td>*145.00</td><td>107.51</td></tr><tr><td>15 22-Apr-26 15:53:46</td><td>1</td><td>*180.00</td><td>151.51</td></tr></table>

\*Indicates Change   
Rating/target price changes above reflect Eastern Time

# ASMPT (0522.HK)

Short-Term View/Catalyst Watch Research

Analyst: Kevin Chen

![](images/a8ea985db553b7fe07f4af4b99e6cfb5cf89c10db53608c607128b221884a071.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>24-Jul-24 04:56:09</td><td>Add STV</td><td>Downside</td><td>30 Days</td><td>87.21</td></tr><tr><td>2</td><td>23-Aug-24 14:19:04</td><td>Remove STV</td><td>Downside</td><td>30 Days</td><td>86.26</td></tr></table>

<table><tr><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>3</td><td>23-Jul-25 09:13:41</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>62.91</td></tr><tr><td>4</td><td>22-Oct-25 00:34:21</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>83.17</td></tr></table>

<table><tr><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>5</td><td>14-Apr-26 00:41:45</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>124.93</td></tr><tr><td>6</td><td>15-May-26 00:28:53</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>172.00</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View   
Rating/target price changes above reflect Eastern Time

The Firm has made a market in the publicly traded equity securities of ASMPT Ltd on at least one occasion since 1 Jan 2025.

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from ASMPT in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: ASMPT.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: ASMPT.

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and service

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
