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
# China Pharma and Biotech

# The Long View: Comparing R&D muscles of China Pharma & Biotech

![](images/6813fb0f9116eef783110f72e528cfe2db9b6576cee191a05f2adc824da8e69f.jpg)

Rebecca Liang, Ph.D.

+852 2123 2656

rebecca.liang@bernsteinsg.com

![](images/7d7ebab8780e3acace193c29e47b3b5b141695ddd68d98c78530c6208eec625b.jpg)

Ellie Li

+852 2123 2621

ellie.li@bernsteinsg.com

It's been a while since our last deep-dive in R&D capabilities - we provide an update here with three sets of analysis to assess R&D efficiency across companies, and Innovent, Akeso, and Hengrui emerge as future champions.

Economic return on R&D. This is the most important measure as it looks at the ability to turn R&D spending into revenue. To evaluate the return on company level, we need to compare revenue from innovative drugs to the cumulative R&D spending a few years back. At the time of our previous assessment, most companies had been too “young” without enough years of R&D data. Now we can get to the return from two angles: 1) sales return on R&D and license income return on R&D (see detailed formula in Exhibit 1). Results: 1) Leading biotech companies have seen a moderate increase in their sales return on R&D from 2023 to 2025, while pharma players, except Hansoh, suffered a decline at the same time as their top products declined. 2) In 2025, Hansoh had the highest sales return on R&D at 2.0X across companies. Kelun-Biotech outperformed in license income return on R&D at 1.0X. 3) Going forward, we expect Akeso and Innovent to improve the most, becoming champions in both sales (\~3X) and license income returns (0.7-0.9X) in 2030E. Hengrui ranks best among pharmas in 2030E.

R&D efficiency - timeline and conversion. 1) Time-to-market: we calculate the median time between IND application to marketing approval for all innovative products. The average is 2100 days for oncology products and 2900 days for non-oncology for our coverage. In both categories, Zai Lab has the shortest time-to-market, not surprising given their business model of in-licensing late-stage global products that only require Ph3 or bridging studies in China. Among companies with substantial internal pipelines, Innovent consistently leads in time-to-market, 1067 days in oncology (\~50% of average) and 2111 days in non-oncology (\~30% lower than average). 2) Hit rate: as evaluated by the total number of marketed innovative drugs over all INDs submitted before end of 2023, measuring the conversion along the clinical trials funnel. Biotech have almost twice the hit rate as pharma on average, and Innovent and Akeso again stand out with the highest hit rates at over 40%.

Size and quantity measures. 1) Pipeline size: Hengrui still dominates with quantity with 360+ assets. Notably Innovent now has over 100 assets, entering the level of mature biopharma; also highest potentially FIC % at 28% vs. average c. 20%. 2) No. of trials: Hengrui and Innovent have sponsored the most trials so far. Interestingly, we looked at no. trials sponsored per billion RMB of R&D spending, and Akeso and Hengrui are the most efficient, averaging \~20 trials per year.

BERNSTEIN TICKER TABLE 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Cur</td><td rowspan="2">20 May 2026 Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>9926.HK (Akeso)</td><td>M</td><td>HKD</td><td>115.00</td><td>130.00</td><td>1.4%</td><td>CNY</td><td>(0.60)</td><td>(0.52)</td><td>0.70</td><td>(165.5)</td><td>(193.8)</td><td>143.2</td></tr><tr><td>ONC (BeOne)</td><td>O</td><td>USD</td><td>297.01</td><td>412.00</td><td>2.1%</td><td>USD</td><td>2.63</td><td>5.65</td><td>8.93</td><td>112.9</td><td>52.5</td><td>33.3</td></tr><tr><td>1093.HK (CSPC)</td><td>M</td><td>HKD</td><td>7.39</td><td>10.70</td><td>(20.8)%</td><td>HKD</td><td>0.37</td><td>0.52</td><td>0.56</td><td>17.4</td><td>12.4</td><td>11.5</td></tr><tr><td>3692.HK (Hansoh)</td><td>O</td><td>HKD</td><td>33.60</td><td>47.00</td><td>(2.9)%</td><td>CNY</td><td>0.93</td><td>1.01</td><td>1.10</td><td>31.4</td><td>28.9</td><td>26.5</td></tr><tr><td>1801.HK (Innovent)</td><td>O</td><td>HKD</td><td>79.40</td><td>120.00</td><td>5.4%</td><td>HKD</td><td>0.48</td><td>0.71</td><td>2.90</td><td>163.7</td><td>111.9</td><td>27.4</td></tr><tr><td>600276.CH (Hengrui)</td><td>O</td><td>CNY</td><td>50.95</td><td>71.00</td><td>(44.6)%</td><td>CNY</td><td>1.19</td><td>1.54</td><td>1.92</td><td>42.8</td><td>33.0</td><td>26.6</td></tr><tr><td>6990.HK (Kelun-Biotech)</td><td>O</td><td>HKD</td><td>437.00</td><td>526.00</td><td>(8.1)%</td><td>CNY</td><td>(1.66)</td><td>(2.75)</td><td>0.85</td><td>36.9</td><td>37.5</td><td>23.1</td></tr><tr><td>1177.HK (Sino BioPh)</td><td>M</td><td>HKD</td><td>5.17</td><td>7.90</td><td>(14.5)%</td><td>CNY</td><td>0.19</td><td>0.20</td><td>0.22</td><td>23.5</td><td>22.7</td><td>20.5</td></tr><tr><td>9688.HK (Zai Lab)</td><td>M</td><td>HKD</td><td>14.35</td><td>15.00</td><td>(81.5)%</td><td>USD</td><td>(0.16)</td><td>(0.15)</td><td>(0.09)</td><td>3.6</td><td>3.3</td><td>2.8</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,894.75</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,353.61</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
6990.HK, 9688.HK valuation is EV/Sales (x); 9926.HK, 1093.HK, 1177.HK base year is 2024;   
Source: Bloomberg, Bernstein estimates and analysis.

# DETAILS

# FRAMEWORK FOR RETURN AND EFFICIENCY METRICS

EXHIBIT 1: Framework and methodology to evaluate R&D capabilities across companies 

<table><tr><td>I. Economic return</td><td>II. Efficiency</td><td>III. Size &amp; quantity</td></tr><tr><td>Sales return on R&amp;DInnovative drug sales in year T / cumulative R&amp;D expense in years T-7 to T-4 (4 years cumulative)</td><td>Time to marketMedian time between IND application to marketing approval</td><td>Pipeline sizeNo. assets at each preclinical and clinical stage</td></tr><tr><td>License income return on R&amp;DLicense income in year T / Cumulative R&amp;D expense in years T-5 to T-3 (3 years cumulative)</td><td>Hit rateNo. marketed innovative drugs / No. INDs until end of 2023</td><td>No. trialsNo. of trials per year &amp;No. trials sponsored per Bn Yuan of R&amp;D expense</td></tr></table>

Source: Bernstein analysis

# CONCLUSIONS FIRST: RETURN ON R&D SPENDING

We estimate a clear shift in China pharma/biotechs R&D return dynamics by 2030E (Exhibit 2). In 2025, Hansoh delivers the highest sales return on R&D, followed by Innovent, while Kelun Biotech leads peers in license income return despite minimal innovative drug sales. Looking to 2030E, Akeso and Innovent are expected to outperform peers across both innovative sales and licensing income-derived R&D returns, driven by the rapid sales ramp-up for their innovative assets and rising milestone/royalty payouts from out-licensed assets. Hengrui emerges as the top-performing pharma in overall R&D returns compared to other pharma companies, underpinned by strong commercial ability and steady licensing momentum.

EXHIBIT 2: We expect top-tier innovators (Hansoh, Hengrui, Akeso, Kelun, Innovent) to significantly improve sales and licensing returns on R&D by 2030   
China pharma & biotech under coverage (2025 vs. 2030E)
Evaluating changes of sales return on R&D vs. License income return on R&D   
![](images/58cea7f730dd69d14fbed35b0d7d4b4adaa836654939f063a435490afb7bfe22.jpg)

<details>
<summary>bubble</summary>

| Company       | FY2025 | FY2030E |
| ------------- | ------ | ------- |
| Kelun Biotech | 1.0x   | 1.0x    |
| Hengrui       | 0.8x   | 0.2x    |
| CSPC          | 0.8x   | 0.2x    |
| SBP           | 0.8x   | 0.0x    |
| Zai lab       | 0.4x   | 0.0x    |
| Akeso         | 1.2x   | 0.0x    |
| BeOne         | 1.2x   | 0.0x    |
| Hansoh        | 2.0x   | 0.6x    |
| Kelen Biotech | 2.4x   | 0.7x    |
| Hengrui       | 2.4x   | 0.6x    |
| Innovent       | 1.6x   | 0.1x    |
| Zai lab       | 1.6x   | 0.1x    |
| Akeso         | 1.2x   | 0.1x    |
| BeOne         | 1.2x   | 0.1x    |
| Akeso         | 1.2x   | 0.1x    |
| Hansoh        | 2.0x   | 0.4x    |
| Innovent       | 1.6x   | 0.1x    |
| Akeso         | 1.2x   | 0.1x    |
| BeOne         | 1.2x   | 0.1x    |
| Akeso         | 1.2x   | 0.1x    |
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | 2.4x   | 0.7x    |
| Akeso         | 2.4x   | 0.7x    |
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | 2.4x   | 0.7x    |
| Akeso         | 2.4x   | 0.7x    |
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | 2.4x   | 0.7x
Akeso     |
| Akeso         | 2.4x   | 0.7x    |
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | 2.4x   | 0.7x    |
| Akeso         | 2.4x   | 0.7x    |
| Hansoh        | 2.4x   | 0.7x    |
|
| Innovent       | 2.4x   | 0.7x    |
| Akeso         | 2.4x   | 0.7x    |
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | 2.4x   | 0.7x    |
| Akeso         | 2.4x   | 0.7x    |
|
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | 2.4x   | 0.7x    |
| Akeso         | 2.4x   | 0.7x    |
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | 2.4x   | 0.7x    |
| Anisoft        | 2.4x   | 0.7x    |
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | 2.4x   | 0.7x    |
| Anisoft        | 2.4x   | 0.7x    |
| Hansoh        | 2.4x   | 0.7x    |
| Innovent       | -      | -       |
| Anisoft        | -      | -       |
| Hansoh        | -      | -       |
| Innovent       | -      | -       |
| Anisoft        | -      | -       |
| Hansoh        | -      | -       |
| Innovent       | -      | -       |
| Anisoft        | -      | -       |
| Hansoh        | -      | -       |
| Innovent       | -      | -       |
| Anisoft        | -      | -       |
| Hansoh        }<fcel>-      {Sales return on R&D %}<lcel><nl>
<fcel>Akeso         {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Innovent       {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Anisoft        {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><fcel>-<nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><fcel>-<nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><fcel>-<nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><fcel>-<nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><fcel>-<nl>
<fcel>Hengrui       {Sales return on R&D %}<lcel><fcel>-<nl>
<fcel>Hongrui      {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui      {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui      {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui      {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui      {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui      {Sales return on R&D %}<lcel><lcel><nl>
<fcel>Hengrui      {Sales return on R&D %} of CNY Mn: Sales return on R&D: $ \text{CNY Mn} $; Annualized annualized revenue: $ \text{CNY Mn} $; Bubble size represents cumulative R&D spending: $ \text{CNY Mn} $.
</details>

Note: 1. FY2025 cumulative R&D spending is the sum of 2016-2020, while FY2030E is the sum of 2021-2025, except for Kelun Biotech (sum of 2021-2025 and 2026-2030)   
Source: Company disclosures, Bernstein analysis and estimates

# RETURN ON R&D: INNOVATIVE DRUG SALES OVER CUMULATIVE R&D EXPENSES

Our analysis measures innovative drug sales return on R&D as innovative product sales divided by 4-year cumulative R&D spending incurred4 years prior to the sales reporting year, capturing lagged R&D payback. Across covered biotechs, we estimate steady, accelerating innovative sales returns on R&D for Innovent and Akeso by 2030E, supported by their robust domestic commercial ramp-ups alongside controlled R&D spending growth; by contrast, BeOne is expected to experience flat returns as revenue growth modest post Brukinsa uptake while R&D outlays continue rising (Exhibit 3). For covered pharma companies, Hansoh maintains the highest near-term R&D sales return despite with limited upside ahead, while broader pharma companies faced declining returns from 2022-2025 as major products enter the later stage of life cycle and ballooning R&D spending. In the long-term, Hengrui stands out as a late-cycle winner, with accelerated new product launches driving higher R&D returns from 2027E-2030E (Exhibit 4).

EXHIBIT 3: We project accelerating innovative sales return on R&D across covered biotech driven by strong commercial ramp-up, contrasting with more mature, stable returns for BeOne   
Innovative drug sales return on R&D spending $^{1}$ (Biotech)   
![](images/4a08ca26174a40d984f3ca77c913d96a1ce3f422ca4e555b979697fe4d3853a1.jpg)

<details>
<summary>line</summary>

| Year | Innovent | BeOne | Zai Lab | Akeso | Kelun Biotech |
|---|---|---|---|---|---|
| 2023 | 1.6x | 1.1x | - | - | - |
| 2024 | 1.7x | 1.2x | - | - | - |
| 2025 | 1.7x | 1.2x | 0.4x | 1.3x | - |
| 2026E | 1.9x | 1.2x | 0.4x | 1.4x | - |
| 2027E | 2.2x | 1.1x | 0.4x | 1.7x | - |
| 2028E | 2.3x | 1.2x | 0.6x | 2.3x | 1.2x |
| 2029E | 2.9x | 1.2x | 1.2x | 2.9x | 1.7x |
| 2030E | 3.1x | 1.2x | 1.8x | 3.1x | 2.5x |
</details>

Note: 1. R&D spending represent 4-y cumulative figures ending 4-y prior to the year of product sales figures   
Source: Company disclosures, Bernstein estimates and analysis

EXHIBIT 4: We forecast a steady recovery for Hengrui to 1.7x by 2028E backed by its innovative drug commitment; in contrast, we foresee CSPC facing headwinds as it navigates a transition phase marked by high R&D ahead of meaningful innovative sales   
Innovative drug sales return on R&D spending $^{1}$ (Pharma)   
![](images/0eb72c3f9b77a49b0e0d47276d81e59825ffef7245ca1c07de59e34a52d01197.jpg)

<details>
<summary>line</summary>

| Year   | Hengrui | Hansoh | SBP  | CSPC |
|--------|---------|--------|------|------|
| 2022   | 1.2x    |        | 1.1x | 2.5x |
| 2023   | 1.1x    | 2.1x   | 0.9x | 1.7x |
| 2024   | 1.0x    | 2.1x   | 0.9x | 1.2x |
| 2025   | 0.9x    | 2.0x   | 0.8x | 0.9x |
| 2026E  | 1.1x    | 2.1x   | 0.8x | 0.7x |
| 2027E  | 1.4x    | 2.1x   | 0.9x | 0.6x |
| 2028E  | 1.7x    | 2.0x   | 1.0x | 0.5x |
| 2029E  | 2.2x    | 2.1x   | 1.2x | 0.6x |
| 2030E  | 2.4x    | 2.1x   | 1.2x | 0.7x |
</details>

Note: 1. R&D spending represent 4-y cumulative figures ending 4-y prior to the year of product sales figures   
Source: Company disclosures, Bernstein estimates and analysis

RETURN ON R&D: LICENSE INCOME OVER CUMULATIVE R&D EXPENSES

Our methodology calculates BD income return on R&D as licensing revenue divided by 3-year cumulative R&D spending incurred 3 years prior, tracking lagged payoff from global partnership investments. For covered biotechs, we foresee out-licensing to remain a core monetization driver. Specifically, Akeso is expected to lead as its AK112 will enter a milestone and royalty harvest phase soon following potential FDA approval in 2027E. Kelun Biotech is anticipated to face a near-term return drop as its core asset sac-TMT still in global Ph3 trial development. In addition, we expect Innovent to see a sharp licensing return jump in 2027E from potential milestone received from Takeda (Exhibit 5). For covered pharma companies, we anticipate Hengrui to deliver steadily rising BD income return on R&D given its consistent BD activities and a deep pipeline portfolio. By contrast, CSPC and SBP are expected to have materially lower returns due to limited BD activities (Exhibit 6).

EXHIBIT 5: We expect out-licensing to remain a vital monetization engine for covered biotech, with Innovent and Akeso leading the cohort   
![](images/fa8d1cf795f0c163eb708ff7e45d65ec8d18558b211fa3e5279fd49ace09553c.jpg)

<details>
<summary>bar</summary>

BD income return on R&D spending¹ (Biotech)
| Company | Year | Return on R&D Spending (x) |
| :--- | :--- | :--- |
| Akeso | 2025 | 0.0 |
| Akeso | 2026E | 0.2 |
| Akeso | 2027E | 0.2 |
| Akeso | 2028E | 0.7 |
| Akeso | 2029E | 0.9 |
| Akeso | 2030E | 0.9 |
| Kelun Biotech | 2025 | 1.0 |
| Kelun Biotech | 2026E | 0.3 |
| Kelun Biotech | 2027E | 0.3 |
| Kelun Biotech | 2028E | 0.3 |
| Kelun Biotech | 2029E | 0.4 |
| Kelun Biotech | 2030E | 0.7 |
| Innovent | 2025 | 0.1 |
| Innovent | 2026E | 0.3 |
| Innovent | 2027E | 0.7 |
| Innovent | 2028E | 0.7 |
| Innovent | 2029E | 0.6 |
| Innovent | 2030E | 0.7 |
</details>

Note: 1. R&D spending represent 3-y cumulative figures ending 3-y prior to the year of product sales figures; we omit BeOne Medicines and Zai Lab since their business models are not out-licensing focused  
Source: Company disclosures, Bernstein estimates and analysis

EXHIBIT 6: Among covered pharma, we estimate Hengrui and Hansoh to lead the cohort in BD return on R&D driven by their proactive out-licensing business model   
![](images/ffb9de852ab09daef468506988af4969df898a7b02f7a5f8be69a140a93d2882.jpg)

<details>
<summary>bar</summary>

BD income return on R&D spending¹ (Pharma)
| Company | Year | Return on R&D Spending (%) |
| :--- | :--- | :--- |
| Hengrui | 2023 | 0.18 |
| Hengrui | 2024 | 0.21 |
| Hengrui | 2025 | 0.31 |
| Hengrui | 2026E | 0.51 |
| Hengrui | 2027E | 0.65 |
| Hansoh | 2023 | 0.22 |
| Hansoh | 2024 | 0.38 |
| Hansoh | 2025 | 0.45 |
| Hansoh | 2026E | 0.48 |
| Hansoh | 2027E | 0.43 |
| Hansoh | 2028E | 0.43 |
| CSPC | 2023 | 0.01 |
| CSPC | 2024 | 0.00 |
| CSPC | 2025 | 0.17 |
| CSPC | 2026E | 0.27 |
| CSPC | 2027E | 0.24 |
| CSPC | 2028E | 0.22 |
| SBP | 2023 | 0.06 |
| SBP | 2024 | 0.08 |
| SBP | 2025 | 0.05 |
| SBP | 2026E | 0.06 |
| SBP | 2027E | 0.06 |
| SBP | 2028E | 0.06 |
</details>

Note: 1. R&D spending represent 3-y cumulative figures ending 3-y prior to the year of product sales figures  
Source: Company disclosures, Bernstein estimates and analysis

# R&D SPENDING OVER TIME

EXHIBIT 7: Biopharma (Innovent, BeOne) sees accelerated R&D growth 2016-20 with slowdown in 2021-25   
R&D spending trend comparison (Biopharma/Pharma)   
![](images/4d54276546793d5c6d4b2dd4f2a725214ae15ebd8bed2df58cf95c37011fb02d.jpg)  
Source: Company disclosures, Bernstein analysis

EXHIBIT 8: R&D ratio of China pharma companies have steadi

[中间内容因长度限制已省略]

 learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
