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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Memory Market Update

SOCAMM content noise offers a buying opportunity; thoughts on NVDA-SKH partnership and takeaways from Computex 2026

\- The truth behind the SOCAMM content cut for Vera Rubin. Multiple media outlets highlighted the SOCAMM content downgrade for the VR NVL72 rack from 192GB to 96GB (or from 1.5TB of content to 768GB per CPU) stoking fears among investors on the cooling CPU-related memory demand (link). CPU-driven memory demand upside was the core driver of memory demand accelerating into 2027E (JPMe: DRAM bit demand +33%/+34% in 2026/27E - see details in our GMM report). Based on our supply chain checks, we sense growing demand for the 96GB SOCAMM module, while believe that the shift in demand is predominantly due to limited memory supply rather than performance down-spec. Despite the higher 96GB-grade SOCAMM SKU, we are seeing no changes to overall SOCAMM bit procurement demand, implying that the content downward revision will likely be compensated by higher SOCAMM module demand (e.g. reshuffle of content and volume based on memory supply and content configurations).

Table 1: Sensitivity analysis on NVDA demand based on Vera CPU content configuration  
Unit in K, Content in GB

<table><tr><td>AI headnode</td><td>2026E</td><td>50% of 96GB and 50% of 192GB</td><td>75% of 96GB and 25% of 192GB</td><td>100% of 96GB and 0% of 192GB</td></tr><tr><td># of CPU</td><td></td><td></td><td></td><td></td></tr><tr><td>Rubin</td><td>1,050</td><td>1,400</td><td>1,680</td><td>2,100</td></tr><tr><td>Blackwell</td><td>2,568</td><td>2,568</td><td>2,568</td><td>2,568</td></tr><tr><td>Content per CPU</td><td></td><td></td><td></td><td></td></tr><tr><td>Rubin</td><td>1,536</td><td>1,152</td><td>960</td><td>768</td></tr><tr><td>Blackwell</td><td>512</td><td>512</td><td>512</td><td>512</td></tr><tr><td>Bit demand by product</td><td></td><td></td><td></td><td></td></tr><tr><td>Rubin</td><td>1,613</td><td>1,613</td><td>1,613</td><td>1,613</td></tr><tr><td>Blackwell</td><td>1,315</td><td>1,315</td><td>1,315</td><td>1,315</td></tr><tr><td>Bit Demand (8Gb, Mn. Equiv)</td><td>2,928</td><td>2,928</td><td>2,928</td><td>2,928</td></tr><tr><td>Standalone CPU</td><td></td><td></td><td></td><td></td></tr><tr><td># of Vera CPU</td><td>600</td><td>600</td><td>600</td><td>600</td></tr><tr><td>Content per CPU</td><td>768</td><td>768</td><td>768</td><td>768</td></tr><tr><td>Bit Demand (8Gb, Mn. Equiv)</td><td>461</td><td>461</td><td>461</td><td>461</td></tr><tr><td>NVDA bit demand</td><td>3,388</td><td>3,388</td><td>3,388</td><td>3,388</td></tr></table>

Source: JPM estimates.

\- Strengthening partnership between NVDA and SKH. Nvidia (OW, covered by JPM analyst, Harlan Sur) and SK Hynix announced a multi-year technology partnership to co-develop the next-generation HBM memory for global AI data centers, with SK Hynix formally designated as Nvidia's largest memory partner (2+ year term with extension options). The pact extends well beyond data center HBM, with SK Hynix co-developing memory across Nvidia's full stack namely Vera Rubin supercomputers (JPMe: AI memory products including HBM/DRAM/NAND), Vera CPUs (JPMe: SOCAMM2), RTX Spark PCs (JPMe: LPDDR5X), and Jetson Thor robotics platforms, effectively diversifying SK Hynix into the AI infrastructure, personal AI, and Physical AI markets Nvidia is creating (see more details link). We believe the multi-year partnership implies extended demand visibility (JPMe: likely until 27E) and highlight that this also acts in favor of other existing memory makers given the likely limited supply. In addition, NVIDIA announced a series of partnerships with leading South Korean technology companies to build large-scale AI

## Technology - Semiconductors

## Jay Kwon AC

(82-2) 758-5725

jay.h.kwon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

## Sangsik Lee

(82-2) 758 5146

sangsik.lee@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

## Neelay Y Kamath

(91-22) 6157 3764

neelay.kamath@jpmchase.com

JPM India Private Limited

## Mio Shikanai

(81-3) 6736 1313

mio.shikanai@JPM.com

JPM Securities Japan Co., Ltd.

infrastructure in Asia, seeking to solidify its data-center footprint and expand its AI ecosystem (see more details in the table 2 provided below). Lastly, CEO Jensen mentioned (link) that 2x DRAM wafer capacity expansion plans over the next five years may not be sufficient, suggesting potentially stronger AI memory demand ahead (consistent with JPM view).

Table 2: NVIDIA partnership announcements with major South Korean firms

<table><tr><td>Partner</td><td>Nature of Deal</td><td>Key Details</td></tr><tr><td>SK Hynix</td><td>Multi-year memory technology partnership</td><td>Next-gen memory chips for AI data centers; ensures stable supply of advanced memory. Named Nvidia&#x27;s largest memory partner; 2+ years with extension options.</td></tr><tr><td>SK Telecom</td><td>Gigawatt-scale AI cloud</td><td>Building GW-scale AI cloud on Nvidia tech; first data center online in 2027.</td></tr><tr><td>Naver</td><td>GW-scale AI factory roadmap</td><td>Starts at Gak Sejong data center, expanding capacity then building additional GW-scale AI factories; begins with 55MW project in 2027.</td></tr><tr><td>Doosan</td><td>Physical AI / robotics</td><td>Develops robotics and makes components for Nvidia GPUs; planning several ventures with Nvidia.</td></tr><tr><td>Krafton / NC</td><td>Gaming to physical AI</td><td>Collaboration with game developers for AI and next-gen robotics; Nvidia views gaming as strategic to physical AI / humanoid robots.</td></tr><tr><td>Samsung / Hyundai</td><td>AI factories</td><td>Both companies to invest in AI factories.</td></tr></table>

Source: NVIDIA newsroom, Reuters and WSJ.

\- Takeaways from Computex Taiwan 2026. We attended Computex 2026 last week and walked away with positive impressions, with several implications for our sector:

- SK Hynix: We visited SK Hynix's booth and the key takeaways are: 1) Mass production of 12-Hi HBM4 is on track, echoing CEO Jensen's commentary that all three memory makers have qualified HBM4 (link); 2) higher interest in 12-Hi 48GB HBM4E which supports up to 16 Gbps vs. 16-Hi HBM4E broadly similar to SEC's recent 12-Hi HBM4E sample shipment to customers (link); 3) Inkling of AI-N B (similar to HBF) which carries throughput like HBM and capacity like SSD and is suitable for inference batches, albeit demand pick-up sounded conservative in 2030 (inline with SKH's HBF demand projection - link).  
- Solidigm: We attended the Solidigm Key Note session and the key takeaways were: 1) Storage is becoming a critical infrastructure for various AI data pipelines (i.e. Local SSD (G3) used for data prep, training & inferencing; High performance SSD (G3.5) used in KV cache tier for inferencing; and Shared Storage (G4) used to store inactive KV and for archiving purposes; 2) The value of offloading KV Cache to NAND leads to up to 27x faster time to first token (TTFT) vs. recomputing the context; and 3) Solidigm SSD solutions with VAST's software offers 90% savings in DC space costs vs. HDD (link).  
- Kioxia: We attended the Kioxia Key Note session with some information overlapping with the investor day announcement (report). We find the extensive partnership collaboration details between Kioxia and NVDA constructive - Kioxia delivering a cost effective solution for ultra-large scale RAG (Retrieval-Augmented Generation) server mainly leveraging Kioxia's AiSAQ software. The SSD software development was surprising to us given the stickiness of the solution leapfrogging from a hardware vendor. We believe the software partnership and commitment will be a strong differentiating factor for Kioxia against NAND competitors.

\- 11% memory share correction offers a buy-into-dip opportunity. We believe that memory shares corrected 11% in the past week (vs. SOX: -6%) due mainly to the SOCAMM content cut noise and escalating geopolitical issues. We believe the SOCAMM content cut noise is misleading and anticipate Vera CPU volume upside to more than offset the 96GB SOCAMM SKU. Among the multiple partnerships announced between NVDA and SKH, we believe the 2+ year partnership bodes well for extended demand visibility into 2027E which also reads positively to other memory makers. In the NAND space, we reconfirmed eSSD's growing role as the critical infrastructure layer in AGI, which should bode well for its mid-to-long term demand outlook. We do not rule out the possibility of additional memory content cuts or optimizations in the future; however, we view it as a necessary reaction from end customers to handle the severe shortage of memory supply. We would rather focus on the ongoing customer needs to deploy higher memory content to the system for superior performance. All in all, we see the recent correction as a good buying opportunity from a midterm horizon, and recommend investors add into the pullback and focus on the “higher for longer” upcycle. Key OW names in Asia are: SEC, SK Hynix, and Kioxia. Next key catalysts are: a) Long-term supply agreement announcement update by CSP/memory suppliers, b) x86 and ARM CPU related memory sourcing and demand update (incl. Vera CPU), c) 3Q26 contract pricing update, and d) MU May-quarter results and outlook commentary (slated for late June).

Figure 1: Global memory makers' share price performance including SOX (Philadelphia Semiconductor index)  
![](images/4b24209fae4e5d2d3b2237627dc6c256292cffb881f50ca709d7613842ca1181.jpg)

<details>
<summary>bar chart</summary>

| Company | 1M (%) | 3M (%) | YTD (%) | 1Yr (%) |
| :--- | :--- | :--- | :--- | :--- |
| SEC | 63 | 67 | 201 | 598 |
| Sk hynix | 80 | 119 | 256 | 1020 |
| Micron | 91 | 51 | 263 | 955 |
| NYT | 95 | 47 | 17 | 816 |
| Kioxia | 113 | 260 | 643 | 3787 |
| SNDK | 481 | 85 | 642 | 4619 |
| SOX | 22 | 59 | -83 | 168 |
</details>

Source: Bloomberg Finance L.P.

Companies Discussed in This Report (all prices in this report as of market close on 08 June 2026, unless otherwise indicated) KIOXIA Holdings (285A)(285A.T/¥71,880/OW), SK hynix(000660.KS/W1,934,000/OW), Samsung Electronics(005930.KS/W298,000/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

• Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to KIOXIA Holdings (285A), Samsung Electronics, SK hynix or related entities.  
- Manager or Co-manager: JPM acted as manager or co-manager in a public offering of securities or financial instruments (as such term is defined in Directive 2014/65/EU) of/for Samsung Electronics or related entities within the past 12 months.  
- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of Samsung Electronics or related entities.  
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: KIOXIA Holdings (285A), Samsung Electronics, SK hynix or related entities.  
- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: Samsung Electronics or related entities.  
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Samsung Electronics, SK hynix or related entities.  
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Samsung Electronics, SK hynix or related entities.  
- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from Samsung Electronics or related entities.  
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from KIOXIA Holdings (285A), Samsung Electronics, SK hynix or related entities.  
• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Samsung Electronics, SK hynix or related entities.  
- Debt Position: JPM may hold a position in the debt securities of KIOXIA Holdings (285A), Samsung Electronics, SK hynix or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

KIOXIA Holdings (285A) (285A.T, 285A JP) Price Chart  
![](images/e2aa5d8375eb74183a3b921064f9d5463302feef062a2dd1c9608e9abb5da120.jpg)

<details>
<summary>line chart</summary>

| Date  | Price(Y) |
|-------|----------|
| Jan 26 | 25,000   |
| Mar 26 | 38,000   |
| May 26 | 80,000   |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Y)</td><td>Price Target (Y)</td></tr><tr><td>23-Jan-26</td><td>OW</td><td>17910</td><td>25,000</td></tr><tr><td>22-Mar-26</td><td>OW</td><td>22360</td><td>38,000</td></tr><tr><td>17-May-26</td><td>OW</td><td>44450</td><td>80,000</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Jan 23, 2026. All share prices are as of market close on the previous business day.

Samsung Electronics (005930.KS, 005930 KS) Price Chart  
![](images/c4763b90750f8895bfed9fe23117961579760bad36eb55b07be539adb3486018.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(W) |
| ---------- | -------- |
| Sep 23     | 70k      |
| Jan 24     | 80k      |
| May 24     | 90k      |
| Sep 24     | 110k     |
| Jan 25     | 120k     |
| May 25     | 135k     |
| Sep 25     | 140k     |
| Jan 26     | 160k     |
| May 26     | 350k     |
</details>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Oct 09, 2011. All share prices are as of market close on the previous business day.

<table><tr><td>Date</td><td>Rating</td><td>Price (W)</td><td>Price Target (W)</td></tr><tr><td>15-Jun-23</td><td>OW</td><td>71900</td><td>90,000</td></tr><tr><td>01-Feb-24</td><td>OW</td><td>72700</td><td>95,000</td></tr><tr><td>03-Apr-24</td><td>OW</td><td>85000</td><td>110,000</td></tr><tr><td>03-Jul-24</td><td>OW</td><td>81800</td><td>120,000</td></tr><tr><td>08-Sep-24</td><td>OW</td><td>68900</td><td>100,000</td></tr><tr><td>08-Oct-24</td><td>OW</td><td>61000</td><td>84,000</td></tr><tr><td>31-Oct-24</td><td>OW</td><td>59100</td><td>83,000</td></tr><tr><td>10-Dec-24</td><td>N</td><td>53400</td><td>60,000</td></tr><tr><td>03-Apr-25</td><td>OW</td><td>58800</td><td>74,000</td></tr><tr><td>30-Apr-25</td><td>OW</td><td>55800</td><td>68,000</td></tr><tr><td>02-Jul-25</td><td>OW</td><td>60200</td><td>71,000</td></tr><tr><td>01-Aug-25</td><td>OW</td><td>71400</td><td>84,000</td></tr><tr><td>25-Sep-25</td><td>OW</td><td>85400</td><td>100,000</td></tr><tr><td>27-Oct-25</td><td>OW</td><td>98900</td><td>135,000</td></tr><tr><td>30-Oct-25</td><td>OW</td><td>101700</td><td>140,000</td></tr><tr><td>14-Dec-25</td><td>OW</td><td>108500</td><td>160,000</td></tr><tr><td>16-Jan-26</td><td>OW</td><td>145000</td><td>200,000</td></tr><tr><td>29-Jan-26</td><td>OW</td><td>164300</td><td>240,000</td></tr><tr><td>22-Mar-26</td><td>OW</td><td>199800</td><td>300,000</td></tr><tr><td>30-Apr-26</td><td>OW</td><td>226500</td><td>350,000</td></tr><tr><td>17-May-26</td><td>OW</td><td>273500</td><td>480,000</td></tr></table>

SK hynix (000660.KS, 000660 KS) Price Chart  
![](images/00652cc8525f0de8bdb08de48a02ecd80de202f7af75ae987ebb4bd7e64fc6c2.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(W) |
| ---------- | -------- |
| Sep 23     | 150,000  |
| Jan 24     | 160,000  |
| May 24     | 185,000  |
| Sep 24     | 175,000  |
| Jan 25     | 300,000  |
| May 25     | 240,000  |
| Sep 25     | 260,000  |
| Jan 26     | 280,000  |
| May 26     | 360,000  |
| Sep 26     | 460,000  |
| Jan 27     | 650,000  |
| May 27     | 700,000  |
| Sep 27     | 1,550,000|
| Jan 28     | 1,550,000|
| May 28     | 1,550,000|
| Sep 28     | 1,550,000|
| Jan 29     | 1,550,000|
| May 29     | 1,550,000|
| Sep 30     | 1,550,000|
| Jan 31     | 1,550,000|
| May 31     | 1,550,000|
| Sep 32     | 1,550,000|
| Jan 33     | 1,550,000|
| May 34     | 1,550,000|
| Sep 35     | 1,550,000|
| Jan 36     | 1,550,000|
| May 37     | 1,550,000|
| Sep 38     | 1,550,000|
| Jan 39     | 1,550,000|
| May 40     | 1,550,000|
| Sep 41     | 1,550,000|
| Jan 42     | 1,550,000|
| May 43     | 1,550,000|
| Sep 44     | 1,5

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”)

©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 09 Jun 2026 12:19 AM HKT

Disseminated 09 Jun 2026 12:19 AM HKT
"""
