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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## U.S. IT Hardware

# Memory & Storage: Is the New Memory Paradigm back? Best Idea Presentation from Bernstein's Strategic Decisions Conference

![](images/cc4fe35d31e3168e153d66977708dcf1d25a52278a151fd80af6d9ee47bf3635.jpg)

Mark C. Newman

+1 212 845 7822

mark.newman@bernsteinsg.com

![](images/91bb0919bc0b41c7bc6daabc93b569a63a47a2a7d43a4b81d0b29196312c8623.jpg)

April Li

+1 917 344 8339

april.li@bernsteinsg.com

![](images/46e424a77a20473bdc85be0b941ac1093c22f5c9e650faf4ccefa4e0c80381e7.jpg)

Phoebe Sun

+1 917 344 8481

phoebe.sun@bernsteinsg.com

At Bernstein's $42^{nd}$ Strategic Decisions Conference, we pitched Memory and Storage as our best idea, where we brushed off our New Memory Paradigm thesis from a decade ago and addressed where we got things right and wrong and further upside from here. Enclosed are the presentation slides with key points from the speech.

AI is driving a large and unprecedented demand surge across all forms of memory and storage. As workloads evolve from training and basic chatbot inference to advanced inference and agentic AI, memory and storage requirements change. HBM & DRAM were early beneficiaries, but NAND & HDD also benefit as AI workloads become more advanced.

Data center customers now dominate demand in DRAM, NAND and HDD and are less price sensitive, which is supporting much stronger pricing than in prior cycles.

Is the New Memory Paradigm is back? We first wrote about the New Memory Paradigm in our 2013 Blackbook and 2014 Blackbook as a structural improvement thesis for the memory industry. Much of that thesis has played out as slower tech-driven supply growth and greater industry consolidation are creating stronger upcycles and less severe downcycles, which in turn creates higher highs and higher lows.

This has largely played out as expected in DRAM. Supply growth from technology migration has continued to decline and has remained well below demand growth. That has made it more difficult and more time-consuming for supply to catch up in upcycles, while also reducing the severity of downcycles.

In NAND, the structural supply constraint thesis was delayed by the 3D NAND supply expansion. Planar NAND had followed a pattern similar to DRAM, with GB per fab growth falling sharply as planar NAND approached its technical limits. The transition to 3D NAND created a one-time step-up in GB per wafer and GB per fab. However, 3D NAND is now also beginning to face diminishing returns. NAND is also earlier in the cycle than DRAM, which suggests greater upside potential from current levels.

HDD is also seeing a meaningful structural change, as this is the first time in history that the industry is both consolidated and growing. Since consolidation in 2012, the HDD industry had been shrinking because of aggressive NAND cannibalization. Those headwinds are now largely exhausted. What remains is the business-critical, or nearline, segment, which is fundamentally a capacity market where NAND cannot compete.

Long-term agreements are becoming more favorable for suppliers, with pricing, prepayments, and take-or-pay terms helping reduce cyclicality.

Overall, we continue to like the sector and see further upside. SNDK is our preferred short-term idea, given the significant earnings upside that remains as NAND is earlier in the cycle than DRAM. Seagate is our preferred long-term idea, supported by steadier earnings growth from both volume and pricing, as well as HAMR-driven cost declines.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td colspan="5">8 Jun 2026</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>TTM Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>SNDK (SanDisk)</td><td>O</td><td>USD</td><td>1,642.00</td><td>1,700.00</td><td>3802.9%</td><td>USD</td><td>2.99</td><td>64.73</td><td>200.47</td><td>549.2</td><td>25.4</td><td>8.2</td></tr><tr><td>STX (Seagate)</td><td>O</td><td>USD</td><td>876.77</td><td>1,000.00</td><td>550.1%</td><td>USD</td><td>8.10</td><td>14.89</td><td>32.49</td><td>108.2</td><td>58.9</td><td>27.0</td></tr><tr><td>WDC (Western Digital)</td><td>O</td><td>USD</td><td>526.93</td><td>590.00</td><td>800.7%</td><td>USD</td><td>4.80</td><td>9.81</td><td>20.19</td><td>109.8</td><td>53.7</td><td>26.1</td></tr><tr><td>SPX</td><td></td><td></td><td>7,405.73</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We are positive on Memory and Storage, with top Short-term pick SNDK and top Long-term pick STX. We also rate WDC Outperform.

## DETAILS

We are seeing an unprecedented demand surge in memory and hard disk drives, with important implications for memory and HDD stocks.

We will first discuss why AI is driving substantial demand for memory and storage. We will then revisit the New Memory Paradigm thesis from 2013 and assess whether it remains in place across DRAM, NAND, and hard disk drives. We will conclude with valuation and our top picks, STX as the long-term pick and SNDK as the short-term pick, both initiated Outperform last September.

At first glance, recommending stocks that are up roughly 4,000% and 700% over the past 12 months may seem aggressive. However, we continue to see meaningful upside in both names.

EXHIBIT 1: Agenda

## Agenda

■ AI driving unprecedented demand surge in Memory & Storage  
Is the New Memory Paradigm back?

- DRAM: Technology driven supply constraint playing out  
- NAND: Earlier cycle than DRAM  
- HDD: Consolidated and growing for the first time

Valuation and top picks

- Top ST pick: SNDK – still significant earnings upside (initiated Outperform 15 $^{th}$ Sep '25)  
- Top LT pick: STX – technology leader in HAMR (initiated Outperform 15 $^{th}$ Sep '25)

BERNSTEIN | SG GROUP

| 2

Source: Bernstein analysis

SNDK up 3,866% in 12 months, 437% YTD  
![](images/8cb9de6b4441bb8b35c27a62012535551c7c2016dda792594a7f6a8a528b3391.jpg)

<details>
<summary>line chart</summary>

| Date       | Price | Bern. target price |
| ---------- | ----- | ----------------- |
| 5/22/2025  | 0     | 0                 |
| 6/22/2025  | 0     | 0                 |
| 7/22/2025  | 0     | 0                 |
| 8/22/2025  | 0     | 0                 |
| 9/22/2025  | 0     | 0                 |
| 10/22/2025 | 0     | 0                 |
| 11/22/2025 | 100   | 100               |
| 12/22/2025 | 150   | 150               |
| 1/22/2026  | 300   | 300               |
| 2/22/2026  | 600   | 1000              |
| 3/22/2026  | 500   | 1000              |
| 4/22/2026  | 800   | 1200              |
| 5/22/2026  | 1500  | 1800              |
</details>

STX up 621% in 12 months, 183% YTD  
![](images/d11bd7392cd81bda947f22dfcfead98ad410ddf8d021c84539d7dd7e15737e1f.jpg)

<details>
<summary>line chart</summary>

| Date       | Price | Bern. target price |
| ---------- | ----- | ------------------ |
| 5/22/2025  | 100   | -                  |
| 6/22/2025  | 120   | -                  |
| 7/22/2025  | 130   | -                  |
| 8/22/2025  | 140   | -                  |
| 9/22/2025  | 150   | 250                |
| 10/22/2025 | 160   | 260                |
| 11/22/2025 | 170   | 380                |
| 12/22/2025 | 180   | 380                |
| 1/22/2026  | 190   | 500                |
| 2/22/2026  | 200   | 500                |
| 3/22/2026  | 210   | 600                |
| 4/22/2026  | 220   | 600                |
| 5/22/2026  | 800   | 1000               |
</details>

BERNSTEIN | SG GROUP Source: Bloomberg, Bernstein

| 3

Source: Bloomberg, Bernstein

At the heart of AI is data, and that data resides in memory and storage. The hierarchy runs from SRAM at the top, which resides on GPUs and CPUs, down through HBM, DRAM, NAND, HDD, and tape at the bottom. As you move up the stack, performance increases but cost rises. As you move down the stack, performance declines but cost falls.

## EXHIBIT 3: Memory/Storage Hierarchy for AI

At the heart of AI is data, which resides in Memory and Storage  
![](images/1889fc9ce294edf934102cb3657cee1041179fb69979fcbece6c630d11b4f3bd.jpg)

<details>
<summary>pyramid chart</summary>

| Technology | Value     |
| ---------- | --------- |
| SRAM       | $3,000/GB |
| HBM        | ($20/GB)  |
| DRAM       | ($20/GB)  |
| NAND (enterprise SSD) | ($0.29/GB) |
| HDD        | ($0.014/GB) |
| TAPE       | ($0.005/GB) |
</details>

Source: Company reports, DRAMeXchange, Trendforce, Bernstein estimates & analysis

BERNSTEIN | SG GROUP

| 4

Source: Company reports, DRAMeXchange, Trendforce, Bernstein estimates & analysis

AI is driving a large and unprecedented demand surge across all forms of memory and storage. As workloads evolve from training and basic chatbot inference to advanced inference and agentic AI, memory and storage requirements change as well. High Bandwidth Memory (HBM) and Conventional DRAM were the early beneficiaries, but NAND and HDD also benefit more as AI workloads become more advanced.

EXHIBIT 4: AI Demand for Memory & Storage  
AI is driving unprecedented demand surge in Memory & Storage  
![](images/aee35756808aa4323e18557592c8ef91964aabd96a6f30a17c23880d6658b939.jpg)

<details>
<summary>heatmap</summary>

| Category | Stage 1: Training Pre-training | Stage 2: Basic chatbot inference | Stage 3: Advanced inference Long-context, RAG, reasoning | Stage 4: Agentic AI Tool use, memory, workflows |
|---|---|---|---|---|
| HBM (DRAM) | Extreme | High | Extreme | High |
| Conventional DRAM (DDR5) | High | Moderate | High | Extreme |
| NAND Flash / Enterprise SSD | High | Moderate | Extreme | Extreme |
| HDD (Nearline) | High | Low/Indirect | Moderate | High |
| Tape (LTO / archive) | Moderate | Low | Low | Moderate |
Legend: Extreme, High, Moderate, Low/Indirect
</details>

Source: Trendforce, Company reports, Bernstein estimates and analysis

BERNSTEIN | SG GROUP

| 5

Source: Trendforce, Company reports, Bernstein estimates and analysis

This demand surge is leading data center customers to dominate demand across the major memory and storage categories. What is different this time is that hyperscalers building AI data centers are far less price sensitive than historical end customers. That dynamic has helped drive pricing up 3x to 4x over roughly the past six months.

EXHIBIT 5: Data Center Mix for NAND, DRAM, and HDD

## Less price sensitive Data Center customers now dominate demand

NAND  
![](images/7056c1d30d09c3d1ab8a318427838a48b74a811a721cff6aa0dc417b93143a15.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Data Center (%) | Non-Data Center (%) |
|---|---|---|
| 2016 | 14 | 87 |
| 2026E | 52 | 48 |
</details>

DRAM  
![](images/5feb1e8ae9bfa56f46ca42cffc7238568ac89caf03de832c97b2ecd0c93b3ffe.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Data Center (%) | Non-Data Center (%) |
|---|---|---|
| 2016 | 18 | 75 |
| 2026E | 50 | 45 |
</details>

HDD  
![](images/34df6c1598dd42decc281c0401934d1edb0a157294aac45661c9e8de20a83a8a.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Data Center (%) | Non-Data Center (%) |
|---|---|---|
| 2016 | 35 | 64 |
| 2026E | 89 | 17 |
</details>

Source: Company reports, IDC, DRAMeXchange, Trendforce, Bernstein estimates & analysis

BERNSTEIN | SG GROUP

| 6

Source: Company reports, IDC, DRAMeXchange, Trendforce, Bernstein estimates & analysis

Is the New Memory Paradigm back? We first wrote about the New Memory Paradigm in our 2013 Blackbook and 2014 Blackbook as a structural improvement thesis for the memory industry. Much of that thesis has played out, although not without exceptions.

The New Memory Paradigm was based on diminishing returns from technology migration slowing supply growth and creating structural undersupply. In that setup, upcycles last longer and downcycles become less severe. As supply becomes harder, slower, and more expensive to add, and as industries consolidate, behavior improves and cycles show higher highs and higher lows.

EXHIBIT 6: 2013/2014 Black Book on the New Memory Paradigm

## Is the New Memory Paradigm back?

Bernstein's 2013/2014 Black Book on the New Memory Paradigm

![](images/5916efcc3442dc13d4444051ddd1a4e5c9bf655825f00a8765abceb3461bf22f.jpg)

<details>
<summary>text_image</summary>

Bernstein
BERNSTEIN GLOBAL VIEW
Global Memory: A New Paradigm
MAY 2013
The days of high but growth and volatility are over; a new memory paradigm emerges...
Memory is in the midst of unprecedented structural changes: consolidation and increasing barriers to entry, combined with escalating technological uncertainty and reduced demand elasticity, pave the way to a new memory paradigm that no longer rewards aggressive investment
Bit growth, the industry's long-term benefit and curse, is slowing permanently; as scaling becomes more complex, bit growth per wafer is slowing in both NAND and DRAM, leading to undersupply, robust pricing and improved margins
Complexity is increasing as we approach scaling limits; 3D memory and new memory technologies are being explored to continue bit growth and cost declines; none of these technologies will be revolutionary enough to alter this positive supply side dynamic
In this new memory paradigm, all memory suppliers will benefit, but in particular Samsung (outperform), SanDisk (outperform), Micron (outperform) and Inotera (outperform) have the most to gain; SK Hynix (market-perform) and Toshiba (not covered) also stand to benefit
</details>

![](images/c86787443f295ee64bb82eaafec9267060d9888dde216c99b65c514bc2cab992.jpg)

<details>
<summary>text_image</summary>

BERNSTEIN GLOBAL VIEW
Global Memory: The Next Leg of the New Memory Paradigm
MAY 2014
With stable profits and cash flow the new norm, multiple expansion and cash returns will follow
Following unprecedented structural changes, memory margins have rented higher but multiples do not yet reflect the new stability of earnings in the new memory paradigm; furthermore, with improving balance sheets and stable cash flows, significant cash returns are on the cards
In NAND, bifurcation is accelerating as quality becomes more important thus proving that NAND is not a commodity; datacenters' thirst for storage and need for speed are lending to interesting opportunities for memory, particularly NAND, filling the huge performance gap
Despite worries of a crash in prices, mainstream memory prices stay stable as the long-term supply constraint remains due to technical hurdles and rational behavior; 3D NAND allows NAND cost declines to continue plus further product differentiation, but little impact on supply
In the next leg of the new memory paradigm, all memory suppliers will benefit from multiple renting and increased cash returns, in particular, we like SmfDisk as the NAND solutions leader and SK Hynix as the most undervalued, but also like Samsung, Micron, Toshiba and Inotera
</details>

Source: Bernstein

BERNSTEIN | SG GROUP

| 7

Source: Bernstein

## The New Memory Paradigm: Diminishing returns from tech migration driving structural undersupply

DRAM Structural Supply Growth vs. Demand Growth in the 2013 New Memory Paradigm Blackbook  
![](images/0ac8d73d921dfa577a7c17c54ae59ee1e13dfee7722c8d707229cf83d84063c2.jpg)

<details>
<summary>line chart</summary>

| Year | Gb/wafer Growth (%) | Gb Demand Growth (%) |
|---|---|---|
| 2012 | 43.5 | 32.5 |
| 2013E | 31.8 | 30.5 |
| 2014E | 27.5 | 31.0 |
| 2015E | 25.5 | 30.0 |
| 2016E | 24.5 | 26.5 |
| 2017E | 21.5 | 23.0 |
</details>

NAND Structural Supply Growth vs. Demand Growth in the 2013 New Memory Paradigm Blackbook  
![](images/403f03108089c645e75a462d9704e657022e6a5e5e046313b1d4738310ea343e.jpg)

<details>
<summary>line chart</summary>

| Year   | GB/wafer Growth | MB Demand Growth |
| ------ | --------------- | ---------------- |
| 2010   | 57.0%           | 74.0%            |
| 2011   | 52.0%           | 77.0%            |
| 2012   | 53.0%           | 64.0%            |
| 2013E  | 41.0%           | 52.0%            |
| 2014E  | 35.0%           | 51.0%            |
| 2015E  | 32.0%           | 44.0%            |
| 2016E  | 29.0%           | 34.0%            |
| 2017E  | 26.0%           | 34.0%            |
</details>

Source: Company reports, DRAMeXchange, Trendforce, Bernstein estimates & analysis

BERNSTEIN | SG GROUP

| 8

Source: Company reports, DRAMeXchange, Trendforce, Bernstein estimates & analysis

This has largely played out as expected in DRAM. Supply growth from technology migration, measured here by GB per fab growth, has continued to decline and has remained well below demand growth. That has made it more difficult and more time-consuming for supply to catch up in upcycles, while also reducing the severity of downcycles.

## EXHIBIT 8: DRAM Structural Supply Growth vs. Demand Growth today

## Technology driven supply constraint has played out in DRAM

DRAM Structural Supply Growth vs. Demand Growth today

![](images/859f7504d78b61b7ceea291e60634dd2ab230fc4624344ecfc094a6cf6e1e01f.jpg)

<details>
<summary>line chart</summary>

| Year | GB/Fab Growth (%) | Demand Growth (%) |
| --- | --- | --- |
| 2012 | 43.5 | 33.5 |
| 2013 | 36.8 | 27.5 |
| 2014 | 29.8 | 32.2 |
| 2015 | 29.8 | 24.7 |
| 2016 | 25.5 | 28.9 |
| 2017 | 20.5 | 21.4 |
| 2018 | 14.0 | 20.5 |
| 2019 | 10.0 | 18.6 |
| 2020 | 13.0 | 17.8 |
| 2021 | 13.0 | 21.6 |
| 2022 | 8.5 | 7.8 |
| 2023 | 6.5 | 10.0 |
| 2024 | 6.8 | 19.3 |
| 2025 | 6.8 | 21.7 |
| 2026E | 6.5 | 19.5 |
| 2027E | 7.5 | 20.7 |
</details>

Source: Company reports, DRAMeXchange, Bernstein estimates & analysis

BERNSTEIN | SG GROUP

| 9

Source: Company reports, DRAMeXchange, Bernstein estimates & analysis

DRAM and HDD have also become highly concentrated industries, which has supported better behavior overall. NAND is a younger industry and has not consolidated to the same extent, but it is still relatively concentrated.

EXHIBIT 9: Industry Concentration Across Memory/Storage Segments

## Memory/Storage segments have consolidated: HDD is the highest concentration, followed by DRAM and NAND

HHI Index – measurement of industry concentration  
![](images/de0b998113347bc36fc64309ce8cd1161497cf5745d0faecf25b66e35dc41444.jpg)

<details>
<summary>line chart</summary>

| Year | HDD | DRAM | NAND |
|---|---|---|---|
| 2001 | 1800 | 1500 | 2500 |
| 2002 | 1900 | 1700 | 3

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
