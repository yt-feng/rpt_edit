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
17 May 2026 17:00:18 ET | 15 pages

# Greater China Semiconductors

May Week 3 Recap: H200 Approval Unlikely to Derail China Localization, WFE Upside on Memory Expansion

# CITI'S TAKE

We review Week 3 (May 11–15) for the China/Hong Kong semiconductor sector. Positive AI sentiment supported a rally in SiC, memory, and equipment, while domestic GPU and CPU were dampened by a potential Nvidia H200 approval. We believe the 750k H200 import allowance cannot meet China's aggressive AI capacity build and would not alter the AI localization progress. Domestic WFE demand is seeing upside on China's accelerating memory capacity expansion. We prefer ASMPT and SG Micro on improving industry outlook and better risk/reward in our view.

May week 3 share price movement — CN/HK semis rallied on positive AI sentiment, with SiC (TSEM results, price stabilization), memory (supply tightness, YMTC filing for IPO), and semis equipment (demand upside) gaining the most. GPU and CPU pulled back on concerns of a potential H200 import approval.

H200 approval unlikely to change localization outlook — The US has reportedly cleared sales of Nvidia H200 chips to 10 Chinese firms (Reuters, 14 May) for up to 75k chips per company. We believe the combined 750k volume is in line with industry expectations. While near-term negative to local AI accelerators, foundries, and WFE vendors, 750k is far below China's AI chip demand, which could still be met by sourcing from domestic accelerators. We view an H200 approval mildly positive for server vendors and Montage (upside for memory interface, PCIe retimers).

WFE demand upside on memory capacity expansion — CN WFE vendors AMEC and NAURA are seeing demand upside given strong memory capacity expansion. YMTC is reportedly submitting an IPO filing in June. We expect CXMT IPO in 2H26 and YMTC in 2027, and both memory makers to accelerate their capacity expansion in 2H26–2027.

Strong CN CSP capex — Alibaba reported expanded C1Q26 capex with AI capex upside (vs. original Rmb380bn) in the next 3–5 years. Tencent capex grew 16% YoY to Rmb31.9bn in 1Q26 while guiding for capex increase in 2H26. ByteDance is raising its 2026 capex by 25% to Rmb200bn. We expect the rising CN CSP capex to further propel demand for the domestic supply chain.

Top picks: ASMPT, SG Micro — We prefer ASMPT (back-end equipment) given: 1) TCB/AP demand upside; 2) rising OSAT capex; and 3) back-end refocusing. We see broadening opportunities in TCB and photonics, and expect share re-rating beyond historical range. SG Micro (analog) should benefit from price upside as TXN and NXPI plan another round of price hikes. SG Micro is seeking additional foundry capacity to meet incremental demand. Supply-demand is improving as AI applications claim a larger share of industry capacity. We continue to view Montage as best positioned among CN semis to invest in AI capacity expansion. Kioxia's strong outlook should carry positive sentiment for memory in the near term. That said, we see less attractive risk/reward after the recent share rally.

Kevin Chen $^{AC}$

+852-2501-2125

kevin.y.chen@citi.com

Jamie Wang

+852-2501-2772

jamie.ck.wang@citi.com

Kyna Wong

kyna.wong@citi.com

Karen Huang

karen.xw.huang@citi.com

Figure 1. Share Price Movement by Sector 

<table><tr><td>15-May-2026</td><td>1W</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td></tr><tr><td>Foundry</td><td>1.5%</td><td>22.6%</td><td>6.8%</td><td>21.0%</td><td>130.7%</td></tr><tr><td>OSAT</td><td>10.4%</td><td>12.9%</td><td>10.8%</td><td>37.9%</td><td>73.9%</td></tr><tr><td>Equipment - Front end</td><td>14.2%</td><td>29.2%</td><td>23.6%</td><td>49.7%</td><td>121.8%</td></tr><tr><td>Equipment - Back end</td><td>14.4%</td><td>38.9%</td><td>49.1%</td><td>147.6%</td><td>293.1%</td></tr><tr><td>CPU / SoC</td><td>-1.2%</td><td>22.7%</td><td>12.6%</td><td>37.6%</td><td>67.2%</td></tr><tr><td>GPU / ASIC</td><td>-7.4%</td><td>19.3%</td><td>34.6%</td><td>6.0%</td><td>27.7%</td></tr><tr><td>Memory</td><td>16.5%</td><td>42.3%</td><td>59.5%</td><td>74.5%</td><td>279.7%</td></tr><tr><td>SiPh / CPO</td><td>6.0%</td><td>28.9%</td><td>80.4%</td><td>186.9%</td><td>691.2%</td></tr><tr><td>Analog</td><td>10.0%</td><td>35.5%</td><td>37.1%</td><td>52.4%</td><td>73.3%</td></tr><tr><td>Power - IDM</td><td>6.2%</td><td>17.5%</td><td>0.7%</td><td>35.8%</td><td>61.5%</td></tr><tr><td>Power - Fabless</td><td>12.0%</td><td>20.9%</td><td>1.1%</td><td>31.3%</td><td>79.9%</td></tr><tr><td>Power - Wide bandgap</td><td>26.5%</td><td>48.6%</td><td>33.1%</td><td>42.3%</td><td>51.9%</td></tr><tr><td>CIS</td><td>6.0%</td><td>12.6%</td><td>-4.8%</td><td>-1.9%</td><td>-0.6%</td></tr><tr><td>RF</td><td>12.4%</td><td>15.0%</td><td>24.6%</td><td>30.9%</td><td>36.0%</td></tr><tr><td>EDA / Design service</td><td>3.9%</td><td>14.2%</td><td>-3.4%</td><td>24.3%</td><td>92.9%</td></tr><tr><td>Wafer</td><td>5.1%</td><td>34.4%</td><td>22.6%</td><td>25.2%</td><td>48.2%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: dataCentral, Citi

Figure 2. Share Price Movement – 1 Week   
![](images/f5b7d798a3cebb4f031fae0347fa5c0fdf30515c1fd6c7d4b78bc664b4e21e6f.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| Power - Wide bandgap | 26.5 |
| Memory | 16.8 |
| Equipment - Back end | 14.5 |
| Equipment - Front end | 14.5 |
| RF | 12.7 |
| Power - Fabless | 12.3 |
| OSAT | 10.9 |
| Analog | 10.3 |
| Power - IDM | 6.5 |
| CIS | 6.3 |
| SiPh / CPO | 6.2 |
| Wafer | 5.7 |
| EDA / Design service | 4.3 |
| Foundry | 1.5 |
| CPU / SoC | -0.8 |
| GPU / ASIC | -6.8 |
1-Week Avg Px Move
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: dataCentral, Citi

Figure 3. Share Price Movement – 1 Month   
![](images/534729e92e5d8d257a5aeec3777058b4358b897c427ad2214352c2ec5c8c286e.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| Power - Wide bandgap | 48.5 |
| Memory | 42.0 |
| Equipment - Back end | 39.0 |
| Analog | 36.0 |
| Wafer | 34.0 |
| Equipment - Front end | 29.0 |
| SiPh / CPO | 28.5 |
| CPU / SoC | 22.5 |
| Foundry | 22.0 |
| Power - Fabless | 20.5 |
| GPU / ASIC | 19.0 |
| Power - IDM | 17.5 |
| RF | 15.0 |
| EDA / Design service | 13.5 |
| OSAT | 12.5 |
| CIS | 12.0 |
1-Month Avg Px Move
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: dataCentral, Citi

Figure 4. Share Price Movement – 3 Months   
![](images/11734262bb91928a4c05f64ce48ff90417e8cf75c61191c68760f37be8a5dbfd.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| SiPh / CPO | 80 |
| Memory | 60 |
| Equipment - Back end | 50 |
| Analog | 40 |
| GPU / ASIC | 35 |
| Power - Wide bandgap | 35 |
| RF | 25 |
| Equipment - Front end | 25 |
| Wafer | 25 |
| CPU / SoC | 15 |
| OSAT | 15 |
| Foundry | 10 |
| Power - Fabless | 5 |
| Power - IDM | 2 |
| EDA / Design service | -5 |
| CIS | -5 |
3-Month Avg Px Move
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: dataCentral, Citi

Figure 5. Share Price Movement – 6 Months   
![](images/c506a382045f146676036fda7228289784aa8728253de29e1e8f502118234ec7.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| SiPh / CPO | 190 |
| Equipment - Back end | 150 |
| Memory | 75 |
| Analog | 55 |
| Equipment - Front end | 52 |
| Power - Wide bandgap | 45 |
| OSAT | 40 |
| CPU / SoC | 38 |
| Power - IDM | 36 |
| Power - Fabless | 32 |
| RF | 30 |
| Wafer | 28 |
| EDA / Design service | 26 |
| Foundry | 22 |
| GPU / ASIC | 10 |
| CIS | -2 |
6-Month Avg Px Move
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: dataCentral, Citi

# Recent published notes:

■ Greater China Semiconductors – Quick Thoughts on Potential H200 China Sales Clearance   
China Datacenters – Quick Thoughts on Chinese CSP Capex Up in 1Q26 & H200 China Sales Clearance   
■ China Technology – Read-across from US CSP Capex and Optics Peer Commentaries   
OmniVision (603501.SS) – What’s New from Citi 2026 China Elite Corporate Day – Recovery Expected From 2Q26   
■ SG Micro (300661.SZ) – Model Update; Brighter Outlook on Positive Pricing Trend   
■ ASMPT (0522.HK) – Broadening TCB/Photonics Opportunities; Lift TP to HK\$180

# ASMPT

(0522.HK; HK\$172.0; 1; 15 May 26; 16:10)

# Valuation

Our target price of HK\$180 is based on peak valuation of 37x 2027E P/E. We view the peak valuation as justified because we expect strong revenue and earnings recovery driven by: 1) AI-driven advanced packaging order wins, including TCB for HBM and CoW applications; and 2) ongoing recovery of mainstream SEMI and SMT. Potential sales of SMT business could solidify its market position as a leading provider of advanced packaging solutions, leading to valuation re-rating beyond its historical range.

# Risks

Downside risks to our target price being achieved include: 1) a slowdown in AI infrastructure outlook with delayed investment; 2) TCB market share loss at key customers; 3) reduced TCB demand due to alternative technologies, such as hybrid bonding; 4) intensifying industry competition; and 5) export restriction extending to back-end equipment.

# Montage Technology

(6809.HK; HK\$448.6; 1; 15 May 26; 16:10)

# Valuation

Our target price for Montage-H is set at HK\$305 based on 66x 2027E P/E, at 10% premium to our Montage-A share target multiple. We view Montage-H a rare opportunity for international investors to invest in both China and global AI data center expansion. Such quality name with strong AI-thematic has gained strong traction from international investors and resulted in an unusual H-share premium over its A-share counterpart.

We believe the valuation is justified given Montage's improving product mix (DDR5 Gen 3 surpassing Gen 2) and growing contribution from new AI-driven connectivity solutions (MRDIMM, CXL), with demand upside coming from agentic AI and inferencing. The company should continue to benefit from China's increasing semiconductor localization in the coming few years.

# Risks

Key downside risks to our target price include: 1) AI infrastructure capex slowdown, 2) market share loss if international customers shift away from Chinese suppliers; 3) rising SOCAMM / LPDDRX adoption in servers that reduces memory interface demand, 4) delayed product migration (DDR5 sub-gen) and development (PCIe switch, CXL switch).

Citi's quant system rates Montage-H high-risk given its short trading history. We view Montage's fundamentals remain strong and expect solid AI-driven revenue/earnings momentum in the coming years. As such, we do not assign a High-Risk rating to Montage-H.

# Montage Technology

(688008.SS; Rmb247.98; 1; 15 May 26; 15:00)

# Valuation

Our target price of Rmb245 is based on 60x 2027E P/E, at 1.5SD above its 5-year average. We believe the valuation is justified given Montage's improving product mix (DDR5 Gen 3 surpassing Gen 2) and growing contribution from new AI-driven connectivity solutions (MRDIMM, CXL), with demand upside coming from agentic AI and inferencing. The company should continue to benefit from China's increasing semiconductor localization in the coming few years.

# Risks

Key downside risks to our target price include: 1) AI infrastructure capex slowdown, 2) market share loss if international customers shift away from Chinese suppliers; 3) rising SOCAMM / LPDDRX adoption in servers that reduces memory interface demand, 4) delayed product migration (DDR5 sub-gen) and development (PCIe switch, CXL switch).

# SG Micro

(300661.SZ; Rmb107.9; 1; 15 May 26; 15:00)

# Valuation

Our target price of Rmb120 is based on 61x 2027E P/E, set at its 5-year average valuation. Chinese analog stocks have traded at higher valuation vs. international peers driven by expectation of increasing analog localization. We expect steady market share gain for SG Micro to drive strong top- and bottom-line growth in the coming years.

# Risks

Key downside risks to our target price include: 1) intensifying price competition from global and Chinese peers; 2) GPM compression as SG Micro overly prioritize market share over profitability; 3) tariff-induced industry inventory overbuilt leading to correction; 4) inventory write-off.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

# Appendix A-1

# ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

# IMPORTANT DISCLOSURES

Montage Technology (688008.SS)

Ratings and Target Price History
Fundamental Research

Analyst: Kevin Chen

![](images/18d6ca349351615fd3f927f508104f9cb39f83501a4c5cb9be4f132d95528db8.jpg)

<details>
<summary>line</summary>

| Date       | Covered | Not covered |
| ---------- | ------- | ----------- |
| 2026       | 1       | 2           |
| 2026       | 3       | 3           |
</details>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>05-Jan-26 16:00:18</td><td>*1</td><td>*170.00</td><td>127.75</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>2 10-Feb-26 04:59:21</td><td>1</td><td>*205.00</td><td>177.50</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>3 27-Apr-26 18:12:40</td><td>1</td><td>*245.00</td><td>178.09</td></tr></table>

Rating/target price changes above reflect Eastern Time   
\*Indicates Change   
Analyst: Kevin Chen

SG Micro (300661.SZ)

Ratings and Target Price History
Fundamental Research

![](images/5464992dc2cb1db441f2519cc4a3b4938be9854854a4e78f9889836265ac575f.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>16-Aug-23 18:16:35</td><td>2</td><td>*61.54</td><td>60.01</td></tr><tr><td>2</td><td>26-May-24 20:50:54</td><td>2</td><td>*57.69</td><td>56.82</td></tr></table>

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>3 29-Aug-24 18:57:29</td><td>*1</td><td>*64.62</td><td>51.79</td></tr><tr><td>4 07-Apr-25 18:56:35</td><td>1</td><td>*88.46</td><td>70.00</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>02-Sep-25 13:15:51</td><td>1</td><td>*100.00</td><td>74.30</td></tr><tr><td>6</td><td>07-May-26 12:41:11</td><td>1</td><td>*120.00</td><td>89.95</td></tr></table>

Rating/target price changes above reflect Eastern Time   
\*Indicates Change

# ASMPT (0522.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Kevin Chen

![](images/67b8f7cdcf88259221a0389d04000a4ec914ace4c2ae7a7ac42707181451a416.jpg)

<details>
<summary>line</summary>

| Date       | Value |
| ---------- | ----- |
| J 2024     | 1     |
| J 2024     | 2     |
| A 2024     | 3     |
| S 2024     | 4     |
| O 2024     | 5     |
| N 2024     | 6     |
| D 2024     | 7     |
| J 2025     | 8     |
| F 2025     | 9     |
| M 2025     | 10    |
| A 2025     | 11    |
| M 2025     | 12    |
| J 2026     | 13    |
| A 2026     | 14    |
| M 2026     | 15    |
</details>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>28-May-23 23:18:47</td><td>2</td><td>*63.00</td><td>62.89</td></tr><tr><td>2</td><td>26-Jul-23 21:43:15</td><td>2</td><td>*85.00</td><td>78.46</td></tr><tr><td>3</td><td>25-Oct-23 19:24:43</td><td>*1</td><td>85.00</td><td>67.92</td></tr><tr><td>4</td><td>28-Feb-24 17:15:12</td><td>1</td><td>*120.00</td><td>90.64</td></tr><tr><td>5</td><td>24-Apr-24 15:46:35</td><td>1</td><td>*140.00</td><td>100.84</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>24-Jul-24 08:56:09</td><td>1</td><td>*110.00</td><td>87.21</td></tr><tr><td>7</td><td>31-Oct-24 04:34:18</td><td>1</td><td>*105.00</td><td>84.08</td></tr><tr><td>8</td><td>26-Feb-25 12:15:35</td><td>1</td><td>*75.00</td><td>63.47</td></tr><tr><td>9</td><td>01-May-25 13:33:57</td><td>1</td><td>*65.00</td><td>51.73</td></tr><tr><td>10</td><td>23-Jul-25 13:13:41</td><td>1</td><td>*75.00</td><td>62.91</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>11</td><td>11-Aug-25 11:00:54</td><td>1</td><td>*85.00</td><td>69.88</td></tr><tr><td>12</td><td>31-Oct-25 03:41:57</td><td>1</td><td>*100.00</td><td>81.63</td></tr><tr><td>13</td><td>21-Jan-26 18:19:50</td><td>1</td><td>*125.00</td><td>101.34</td></tr><tr><td>14</td><td>04-Mar-26 15:09:09</td><td>1</td><td>*145.00</td><td>107.51</td></tr><tr><td>15</td><td>22-Apr-26 15:53:46</td><td>1</td><td>*180.00</td><td>151.51</td></tr></table>

\*Indicates Change   
Rating/target price changes above reflect Eastern Time

# Montage Technology (6809.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Kevin Chen

![](images/bfe385736189f153223a3bcde15be3613dd5615a9640a7cfaac855a271f0d28b.jpg)

<details>
<summary>line</summary>

| Date       | Covered | Not covered |
| ---------- | ------- | ----------- |
| F 2026     | 180     | 180         |
| A 2026     | 200     | 200         |
| M 2026     | 450     | -           

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
