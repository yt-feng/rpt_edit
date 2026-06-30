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
- 已识别机构名：`Citi`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Greater China Semiconductors

## Apple's Reported Interest in CXMT Memory a Strong Validation of the Company's Technological Progress

## CITI'S TAKE

FT reported over the weekend that Apple is seeking U.S. government approval to source memory from CXMT, a leading Chinese DRAM maker currently included on the Pentagon 1260H Chinese Military Company List. While the approval outcome remains uncertain, Apple's consideration already provides a strong endorsement of CXMT's technological progress, in our view. Such validation shifts CXMT from a ‘China domestic substitution story’ towards a ‘credible global No.4 DRAM maker’. We expect the news to be positive for CXMT and its supply chain, including the equipment vendors and OSAT providers. Within our coverage we prefer ASMPT and JCET.

Apple reportedly seeking approval to buy memory from CXMT — News reported Apple is lobbying the Trump administration for approval to buy DRAM from CXMT (Financial Times, Jun 27 $^{th}$ ) amid surging memory costs. CXMT is currently on the Pentagon's 1260H Chinese Military Company List. While 1260H does not bar U.S. companies from purchasing CXMT DRAM, Apple is seeking policy comfort as CXMT may later be subject to tighter restrictions, such as the BIS Entity List.

Apple's ‘stamp of approval’ positive for CXMT/supply chain — We believe securing approval to procure CMXT memory could prove challenging given the current U.S. political climate. However, Apple’s consideration of CXMT is a strong validation of CXMT’s product reliability and the severity of the memory shortage. CXMT LPDDR5X (12Gb/16Gb die capacity) reaches speed of 10667Mbps, potentially addressable to high-end mobile, tablet, and notebook applications. Regardless of whether Apple gets the purchase approval, its consideration of CXMT as a potential supplier shifts market perception of CXMT from a domestic substitution play to a credible global No.4 DRAM maker. We view the news as positive for CXMT and its supply chain, such as equipment vendors and OSAT providers.

Prefer ASMPT, JCET — We prefer ASMPT (back-end equipment) given: 1) TCB and advanced packaging demand upside; 2) rising OSAT capex; and 3) industry shifting focus towards the back end. We see broadening opportunities in TCB and photonics and expect shares to re-rate beyond its historical range. We recently updated our forecast for the 3 China OSATs (JCET, TFME, and TSHT) and raised TPs to reflect the strong sector re-rating. JCET is our top pick given its high advanced packaging exposure (60-70% revenue), strong capability (2.5D, 3D, memory), and diverse customer base.

Kevin Chen AC
+852-2501-2125
kevin.y.chen@citi.com

Kyna Wong
+852-2868-7820
kyna.wong@citi.com

Karen Huang
+852-2501-2755

karen.xw.huang@citi.com

Yiming Li, CFA

+852-2501-2857

yiming.li@citi.com

Figure 1. Share Price Movement by Sector

<table><tr><td>26-Jun-2026</td><td>1D</td><td>1W</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td></tr><tr><td>Foundry</td><td>-2.6%</td><td>11.7%</td><td>20.3%</td><td>97.1%</td><td>86.7%</td><td>234.8%</td></tr><tr><td>OSAT</td><td>-2.2%</td><td>9.3%</td><td>8.5%</td><td>86.5%</td><td>102.2%</td><td>154.4%</td></tr><tr><td>Equipment - Front end</td><td>2.3%</td><td>14.5%</td><td>39.2%</td><td>101.4%</td><td>102.4%</td><td>239.6%</td></tr><tr><td>Equipment - Back end</td><td>1.7%</td><td>18.1%</td><td>34.7%</td><td>129.5%</td><td>206.6%</td><td>446.9%</td></tr><tr><td>CPU / SoC</td><td>-3.6%</td><td>0.7%</td><td>-5.4%</td><td>33.8%</td><td>40.7%</td><td>74.7%</td></tr><tr><td>GPU / ASIC</td><td>-9.4%</td><td>-4.3%</td><td>2.5%</td><td>66.5%</td><td>31.2%</td><td>255.8%</td></tr><tr><td>Memory</td><td>-1.2%</td><td>18.0%</td><td>30.3%</td><td>131.8%</td><td>201.2%</td><td>563.8%</td></tr><tr><td>SiPh / CPO</td><td>-8.6%</td><td>-0.8%</td><td>23.3%</td><td>97.1%</td><td>231.8%</td><td>780.9%</td></tr><tr><td>Analog</td><td>-3.4%</td><td>-1.0%</td><td>11.6%</td><td>76.6%</td><td>88.2%</td><td>113.3%</td></tr><tr><td>Power - IDM &amp; Fabless</td><td>-2.2%</td><td>7.8%</td><td>16.9%</td><td>69.4%</td><td>79.9%</td><td>135.2%</td></tr><tr><td>Power - Wide Bandgap</td><td>-1.5%</td><td>3.3%</td><td>-6.0%</td><td>65.3%</td><td>40.0%</td><td>114.6%</td></tr><tr><td>CIS</td><td>-2.2%</td><td>-1.6%</td><td>-13.3%</td><td>2.1%</td><td>-10.7%</td><td>-11.7%</td></tr><tr><td>RF</td><td>-4.8%</td><td>-6.5%</td><td>-10.0%</td><td>4.4%</td><td>5.1%</td><td>26.9%</td></tr><tr><td>EDA / Design service</td><td>1.2%</td><td>7.6%</td><td>3.3%</td><td>37.0%</td><td>46.1%</td><td>101.0%</td></tr><tr><td>Wafer</td><td>7.3%</td><td>8.4%</td><td>31.4%</td><td>88.9%</td><td>76.4%</td><td>105.4%</td></tr><tr><td>Materials</td><td>2.7%</td><td>16.1%</td><td>42.1%</td><td>84.0%</td><td>145.4%</td><td>241.7%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: dataCentral, Citi

Figure 2. Share Price Movement – 1 Week  
![](images/f19198a7f3b8064420f40e12b477bce84444cc570378c98d344e9fff0568d44f.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: dataCentral, Citi

Figure 3. Share Price Movement – 1 Month  
![](images/6828e9d09d179bf3867ce774b51ab21da29bc7b052fae7961941afe0fc5dcb25.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: dataCentral, Citi

Figure 4. Share Price Movement – 3 Months  
![](images/a24bd713fb0ae3e91b27f9c7bd9a7438ee16542bfb78fa417c309b4679c9cdf8.jpg)  
Source: dataCentral, Citi  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 5. Share Price Movement – 6 Months  
![](images/9bce5fa6a9547edc92893f1470342fc39a3e44cd40c0a111c48870e805b1b2c5.jpg)  
-20% 0% 20% 40% 60% 80% 100% 120% 140% 160% 180% 200% 220% 240%  
Source: dataCentral, Citi  
© 2026 Citi Inc. No redistribution without Citi's written permission.

## RELATED:

Greater China Semiconductors: Sector Re-Rating Lifts Valuations Across the Board; Model Update

JCET Group (600584.SS): JCET's New Rmb7.8bn Investment Further Strengthens Its Advanced Packaging Leadership

## ASMPT

(0522.HK; HK\$195.1; 1; 26 Jun 26; 16:10)

## Valuation

Our target price of HK\$180 is based on peak valuation of 37x 2027E P/E. We view the peak valuation as justified because we expect strong revenue and earnings recovery driven by: 1) AI-driven advanced packaging order wins, including TCB for HBM and CoW applications; and 2) ongoing recovery of mainstream SEMI and SMT. Potential sales of SMT business could solidify its market position as a leading provider of advanced packaging solutions, leading to valuation re-rating beyond its historical range.

## Risks

Downside risks to our target price being achieved include: 1) a slowdown in AI infrastructure outlook with delayed investment; 2) TCB market share loss at key customers; 3) reduced TCB demand due to alternative technologies, such as hybrid bonding; 4) intensifying industry competition; and 5) export restriction extending to back-end equipment.

## JCET Group

(600584.SS; Rmb100.89; 1; 26 Jun 26; 15:00)

## Valuation

We set our target price for JCET at Rmb110 based on a 6.0x 2027E P/B. We believe the China OSAT industry is entering an unprecedented upcycle driven by AI proliferation, tightening industry supply, and growing emphasis on advanced packaging, thus awarding JCET a premium valuation as a key enabler for advanced packaging. We expect industry capacity utilization to remain tight given the robust demand.

## Risks

Key downside risks to our target price include: 1) advanced packaging expansion outpacing demand growth, especially given challenges at the front-end; 2) memory makers internalizing back-end packaging operations; 3) falling utilization after industry capacity expansion; 4) geopolitical tensions reducing demand for JCET's overseas operations; 5) US export restrictions limiting supply of back-end equipment.

## Tianshui Huatian

(002185.SZ; Rmb22.56; 1; 26 Jun 26; 15:00)

## Valuation

We set our target price for TSHT at Rmb23.5 based on a 4.0x 2027E P/B. We believe the China OSAT industry is entering an unprecedented upcycle driven by AI proliferation, tightening industry supply, and growing emphasis on advanced packaging, thus awarding TSHT a premium valuation over its

historical range. We expect industry capacity utilization to remain tight given the robust demand.

## Risks

Key downside risks to our target price include: 1) AI capex slowdown casting concerns over subsequent OSAT demand; 2) falling utilization after industry capacity expansion; 3) geopolitical tensions reducing demand for TSHT's overseas operations; 4) US export restrictions limiting supply of back-end equipment.

## TongFu Microelectronics

(002156.SZ; Rmb71.6; 1; 26 Jun 26; 15:00)

## Valuation

We set our target price for TFME at Rmb80 based on a 6.5x 2027E P/B. We believe the China OSAT industry is entering an unprecedented upcycle driven by AI proliferation, tightening industry supply, and growing emphasis on advanced packaging, thus awarding TFME a premium valuation as a key enabler for advanced packaging. TFME is also positioned for a strong growth trajectory supported by robust demand from key customer AMD.

## Risks

Key downside risks to our target price include: 1) market share loss at the key customer for exclusion of AI-related business; 2) memory makers internalizing back-end packaging operations; 3) falling utilization after industry capacity expansion; 4) geopolitical tensions reducing demand for TFME's overseas operations; 5) US export restrictions limiting supply of back-end equipment.

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>21-Jun-26 23:19:33</td><td>1</td><td>*110.00</td><td>83.03</td></tr></table>

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

## ASMPT (0522.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Kevin Chen

![](images/a9dd66c3e388f284b95594fe3d54e752c99accb2dbad8cd07d758c8c0d988a99.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>26-Jul-23 21:43:15</td><td>2</td><td>*85.00</td><td>78.46</td></tr><tr><td>2</td><td>25-Oct-23 19:24:43</td><td>*1</td><td>85.00</td><td>67.92</td></tr><tr><td>3</td><td>28-Feb-24 17:15:12</td><td>1</td><td>*120.00</td><td>90.64</td></tr><tr><td>4</td><td>24-Apr-24 15:46:35</td><td>1</td><td>*140.00</td><td>100.84</td></tr><tr><td>5</td><td>24-Jul-24 08:56:09</td><td>1</td><td>*110.00</td><td>87.21</td></tr></table>

\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>31-Oct-24 04:34:18</td><td>1</td><td>*105.00</td><td>84.08</td></tr><tr><td>7</td><td>26-Feb-25 12:15:35</td><td>1</td><td>*75.00</td><td>63.47</td></tr><tr><td>8</td><td>01-May-25 13:33:57</td><td>1</td><td>*65.00</td><td>51.73</td></tr><tr><td>9</td><td>23-Jul-25 13:13:41</td><td>1</td><td>*75.00</td><td>62.91</td></tr><tr><td>10</td><td>11-Aug-25 11:00:54</td><td>1</td><td>*85.00</td><td>69.88</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>11</td><td>31-Oct-25 03:41:57</td><td>1</td><td>*100.00</td><td>81.63</td></tr><tr><td>12</td><td>21-Jan-26 18:19:50</td><td>1</td><td>*125.00</td><td>101.34</td></tr><tr><td>13</td><td>04-Mar-26 15:09:09</td><td>1</td><td>*145.00</td><td>107.51</td></tr><tr><td>14</td><td>22-Apr-26 15:53:46</td><td>1</td><td>*180.00</td><td>151.51</td></tr></table>

Rating/target price changes above reflect Eastern Time

## JCET Group (600584.SS)

Ratings and Target Price History
Fundamental Research

Analyst: Kevin Chen

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>27-Aug-23 19:18:26</td><td>1</td><td>*40.00</td><td>29.81</td></tr><tr><td>2</td><td>27-Nov-23 04:47:04</td><td>1</td><td>*45.00</td><td>30.88</td></tr><tr><td>3</td><td>30-Apr-24 03:51:38</td><td>1</td><td>*40.00</td><td>25.77</td></tr></table>

\*Indicates Change

![](images/b253a55e584162632ecc0a95c0bcee8347d6136b4712f65651ebb569574856da.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>25-Aug-24 23:35:27</td><td>1</td><td>*44.00</td><td>30.57</td></tr><tr><td>5</td><td>22-Jan-25 13:39:33</td><td>1</td><td>*50.00</td><td>40.81</td></tr><tr><td>6</td><td>20-Jun-25 02:02:03</td><td>1</td><td>*42.00</td><td>31.54</td></tr></table>

Rating/target price changes above reflect Eastern Time

TongFu Microelectronics (002156.SZ)

Ratings and Target Price History
Fundamental Research

Analyst: Kevin Chen

![](images/3513ff65212152bb7e8df305e26992c6c866a6a48ecb192c29af474a4dc95963.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1 27-Nov-23 04:47:04</td><td>1</td><td>*26.00</td><td>23.00</td></tr><tr><td>2 19-Jun-24 03:13:06</td><td>1</td><td>*28.00</td><td>24.78</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>3</td><td>22-Jan-25 13:39:33</td><td>1</td><td>*34.00</td><td>28.87</td></tr><tr><td>4</td><td>20-Jun-25 02:02:03</td><td>1</td><td>*30.00</td><td>23.59</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>05-Nov-25 18:43:02</td><td>1</td><td>*48.00</td><td>40.16</td></tr><tr><td>6</td><td>21-Jun-26 23:19:33</td><td>1</td><td>*80.00</td><td>68.27</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Tianshui Huatian (002185.SZ)

Ratings and Target Price History
Fundamental Research

![](images/94da7bf271d33846e44e87ff849fda16c1305f8ff1599f0c9b696416242b3b49.jpg)

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>27-Nov-23 04:47:04</td><td>1</td><td>*11.00</td><td>9.00</td></tr><tr><td>2</td><td>22-Jan-25 13:39:33</td><td>1</td><td>*14.00</td><td>11.43</td></tr></table>

\*Indicates Change  
Rating/target price changes above reflect Eastern Time

## ASMPT (0522.HK)

Short-Term View/Catalyst Watch Research

Analyst: Kevin Chen

![](images/c013f56d0fbf17d96125d6c7abdb9c2dbefb7adff5ed227ad38c17d45513548a.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>24-Jul-24 04:56:09</td><td>Add STV</td><td>Downside</td><td>30 Days</td><td>87.21</td></tr><tr><td>2</td><td>23-Aug-24 14:19:04</td><td>Remove STV</td><td>Downside</td><td>30 Days</td><td>86.26</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>3</td><td>23-Jul-25 09:13:41</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>62.91</td></tr><tr><td>4</td><td>22-Oct-25 00:34:21</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>83.17</td></tr></table>

<table><tr><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>5</td><td>14-Apr-26 00:41:45</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>124.93</td></tr><tr><td>6</td><td>15-May-26 00:28:53</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>172.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/753f2df681c815d263b9d238542009ef3bccc8840c4b04532b8181a95c7a3f36.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>25-Aug-24 19:35:27</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>30.57</td><td>3</td><td>21-Aug-25 08:12:51</td><td>Add STV</td><td>Downside</td><td>90 Days</td><td>36.58</td><td>5</td><td>21-Jun-26 19:19:33</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>83.03</td></tr><tr><td>2</td><td>24-Sep-24 23:26:37</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>29.00</td><td>4</td><td>19-Nov-25 21:14:59</td><td>Remove STV</td><td>Downside</td><td>90 Days</td><td>36.59</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time  
Short-Term View/Catalyst Watch Research

![](images/01e13b9edaf89796cb7924fa1886651b5cd7b862472fcccac06b0bdcdbe4ce85.jpg)

<table><tr><td>Date1</td><td>ActionAdd STV</td><td>ExpectedDirectionUpside</td><td>Duration90 Days</td><td>ClosingPrice23.40</td><td>Date2</td><td>ActionRemove STV</td><td>ExpectedDirectionUpside</td><td>Duration90 Days</td><td>ClosingPrice23.74</td><td>Date3</td><td>ActionAdd STV</td><td>ExpectedDirectionUpside</td><td>Duration90 Days</td><td>ClosingPrice68.27</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above ref

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
