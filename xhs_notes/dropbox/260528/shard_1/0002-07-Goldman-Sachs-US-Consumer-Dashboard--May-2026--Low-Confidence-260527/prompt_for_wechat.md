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
# US Consumer Dashboard: May 2026: Low Confidence

Download: Data | Slide (pdf) | Slide (PowerPoint)

\- Spending: Spending has remained resilient, with real PCE growth tracking at a healthy $2.1\%$ year-over-year pace through March. The April retail sales report was also strong, as headline retail sales increased by $0.5\%$ and core retail sales increased by $0.5\%$ in nominal and real terms (with positive revisions to March). We believe that the recent resilience in spending largely reflects an outsized boost from OBBBA-related tax cuts, and expect that spending headwinds from higher inflation will weigh on spending growth for the rest of the year. We therefore forecast below consensus spending growth in 2026H2 and $1.5\%$ real spending PCE spending growth in 2026 on a Q4/Q4 basis (vs. $1.7\%$ consensus).

Employment: The labor market appears to have stabilized for now. Employment increased by 115k in April, and the three-month average of payroll growth (+48k) and our estimate of the underlying pace of job growth (+51k) are close to our estimate of the breakeven pace of job growth. In addition, the unemployment rate moved sideways at 4.3%. We expect that growth headwinds from the war in Iran will moderately slow job growth (GS forecast for 38k/month job growth for rest of 2026) and push up the unemployment rate to 4.6% by end-2026. We continue to see risks of more labor market weakening if higher energy prices create a larger drag on growth or AI-related job losses prove larger than expected.

Income: Real disposable income growth is very weak, slowing by 0.8pp to 0.4% on a year-over-year basis and by 0.3pp to 0.2% on a 6-month annualized basis in March. While the boost from higher tax refunds and lower tax payments from the OBBBA appears to have provided an almost \$140bn boost to household income during the 2026 tax-filing season, we expect that higher energy prices will erode household spending power for the rest of the year, particularly for lower-income households that spend a larger share of their budget on food and energy. As a result, we forecast only 1.3% real income growth in 2026 on a Q4/Q4 basis (with growth of just 0.5% real income growth for the bottom income quintile), and see an even more challenging outlook for cashflow (adjusted for the timing of OBBBA-related boosts to tax refunds and reductions in tax payments) in 2026H2.

■ Wealth: Household balance sheets are still strong, and the net worth-to-disposable personal income ratio remains near its all-time high, especially after the recent rebound in equity valuations. The saving rate declined

Joseph Briggs

+1(212)902-2163

joseph.briggs@gs.com

GS & Co. LLC

by 0.3pp to $3.6\%$ in March, but we forecast an increase to $3.9\%$ by end-2026 and $4.3\%$ by end-2027 on the back of a stronger precautionary saving motive.

Debt: Consumer credit growth ticked up by 0.3pp to $2.6\%$ on a year-over-year basis and by 0.5pp to $2.7\%$ on a 6-month annualized basis in March—possibly reflecting an increase in credit utilization to smooth the energy price shocks—but home equity loan growth slowed significantly (+1.4% 12-week annualized average through May 13th). Although household leverage and debt servicing costs remain low by historical standards, 90+ day credit card and subprime auto loan delinquencies remain elevated relative to historical levels.

\- Consumer Confidence: UMich consumer sentiment fell by 5.0pt to 44.8—its lowest level on record—while the Conference Board’s consumer confidence index decreased by 0.7pt to 93.1 in May. More timely measures of consumer sentiment, including the daily consumer sentiment measure from Morning Consult and our GS Social Media Economic Sentiment Index, also point to retrenchments in consumer confidence in recent weeks.

Exhibit 1: Our US Consumer Dashboard Points To Weak Income Growth and Consumer Confidence but Strong Balance Sheets 

<table><tr><td colspan="10">GS US Consumer Dashboard*</td><td></td></tr><tr><td></td><td>1980</td><td>1985</td><td>1990</td><td>1995</td><td>2000</td><td>2005</td><td>2010</td><td>2015</td><td>2020</td><td></td></tr><tr><td>Spending</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Current Percentile: 24th</td></tr><tr><td>Employment</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>64th</td></tr><tr><td>Income</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>9th</td></tr><tr><td>Wealth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>97th</td></tr><tr><td>Debt</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>87th</td></tr><tr><td>Confidence</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>11th</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>48th</td></tr></table>

\*Shading indicates most negative (red) to most positive (green) observations, 1980-present. Measures used in heat map are as follows. Spending: 6MMA of real spending growth. Employment: Unemployment gap (vs. NAIRU). Income: 6MMA of real income growth. Wealth: Ratio of household net worth to disposable income. Debt: Household debt service ratio. Confidence: Average of normalized UMich and Conference Board measures.

![](images/fc7ff7518e3588fa38db419100aab3ad090c0dc9c6847fc1577e7cb0c67fc4f4.jpg)  
Source: Bureau of Economic Analysis, US Bureau of Labor Statistics, Federal Reserve Board, University of Michigan, The Conference Board, US Federal Reserve Bank, GS Global Investment Research, IRS, Morning Consult

# Spending

Exhibit 2: We Expect Softer Spending Growth in 2026H2   
![](images/456cd972bebb5567a0c39c5d99004e303b1941c56887111a41395c8dd33266f7.jpg)

<details>
<summary>line</summary>

| Year | Goods | Services | Consumption | GS Forecast |
|------|-------|----------|-------------|-------------|
| 2000 | ~5    | ~3       | ~6          | ~4          |
| 2005 | ~3    | ~2       | ~4          | ~3          |
| 2010 | ~-2   | ~-1      | ~2          | ~1          |
| 2015 | ~3    | ~2       | ~4          | ~3          |
| 2020 | ~-10  | ~-5      | ~-10        | ~-10        |
| 2025 | ~2    | ~1       | ~3          | ~2          |
| 2026 | ~1    | ~0.5     | ~1          | ~0.5        |
</details>

![](images/1953d6773ad33d97be10f2e27a6d39606ae47243d035d84443f4a05d7e69a943.jpg)

<details>
<summary>line</summary>

| Year | Goods | Services | Consumption | GS Forecast |
|------|-------|----------|-------------|-------------|
| 2000 | ~8%   | ~4%      | ~9%         | ~8%         |
| 2005 | ~6%   | ~3%      | ~7%         | ~6%         |
| 2010 | ~-3%  | ~-1%     | ~4%         | ~3%         |
| 2015 | ~4%   | ~2%      | ~5%         | ~4%         |
| 2020 | ~-10% | ~-5%     | ~-10%       | ~-10%       |
| 2025 | ~5%   | ~3%      | ~5%         | ~5%         |
</details>

![](images/36789f02e57877de02577489238d00f5c32846aa2cdf0b3c9a1c782dc7faa21f.jpg)

<details>
<summary>bar</summary>

Year-Over-Year Real Spending Growth By Category
| Category | Value (%) |
|---|---|
| Other | 4.1 |
| Recreational Goods | 1.1 |
| Furniture | -0.7 |
| Motor Vehicles | -3.4 |
| Apparel | 3.3 |
| Other | 2.5 |
| Food and Beverage | 0.1 |
| Gasoline | -0.9 |
| Health Care | 4.8 |
| Financial Services | 4.4 |
| Recreation | 4.2 |
| Nonprofits | 3.7 |
| Transportation | 3.5 |
| Other | 2.3 |
| Housing | 1.0 |
| Food and Accom. | 0.0 |
</details>

![](images/7ba048d2c804f53bf61ccda495eef2e2c8bc162ce1406b1b5a6f4d1441fbee78.jpg)

<details>
<summary>bar</summary>

Real Personal Consumption Expenditure (PCE) Growth Forecasts
| Period | GS (%) | Consensus (%) |
| :--- | :--- | :--- |
| 2026, QoQ AR | 1.6 | 1.6 |
| 2026 | 1.5 | 1.6 |
| 2026 | 1.4 | 1.8 |
| 2026 | 1.5 | 1.9 |
| YoY | 1.9 | 1.9 |
| Q4/Q4* | 1.5 | 1.7 |
* Calculated from quarterly consensus forecasts
</details>

Source: Bureau of Economic Analysis, US Bureau of Labor Statistics, GS Global Investment Research, US Federal Reserve Bank

# Labor Market

Exhibit 3: The Labor Market Appears to Be Stabilizing   
![](images/c29305733a58563bd3c288ad30ebdf5f4b416912b44e6e1ce87e70a4ec690ccb.jpg)

<details>
<summary>line</summary>

| Year | Unemployment Rate (Percent) |
|---|---|
| 1960 | 5.0 |
| 1961 | 7.0 |
| 1962 | 5.5 |
| 1963 | 5.0 |
| 1964 | 4.5 |
| 1965 | 4.0 |
| 1966 | 3.5 |
| 1967 | 3.0 |
| 1968 | 3.5 |
| 1969 | 4.0 |
| 1970 | 3.5 |
| 1971 | 3.0 |
| 1972 | 3.5 |
| 1973 | 4.0 |
| 1974 | 5.0 |
| 1975 | 6.0 |
| 1976 | 7.0 |
| 1977 | 8.0 |
| 1978 | 9.0 |
| 1979 | 7.0 |
| 1980 | 6.0 |
| 1981 | 7.0 |
| 1982 | 8.0 |
| 1983 | 10.5 |
| 1984 | 8.0 |
| 1985 | 7.0 |
| 1986 | 6.5 |
| 1987 | 6.0 |
| 1988 | 5.5 |
| 1989 | 5.0 |
| 1990 | 5.5 |
| 1991 | 6.0 |
| 1992 | 7.0 |
| 1993 | 6.5 |
| 1994 | 6.0 |
| 1995 | 5.5 |
| 1996 | 5.0 |
| 1997 | 4.5 |
| 1998 | 4.0 |
| 1999 | 4.5 |
| 2000 | 4.0 |
| 2001 | 4.5 |
| 2002 | 5.0 |
| 2003 | 5.5 |
| 2004 | 6.0 |
| 2005 | 5.5 |
| 2006 | 5.0 |
| 2007 | 4.5 |
| 2008 | 4.0 |
| 2009 | 4.5 |
| 2010 | 6.0 |
| 2011 | 7.0 |
| 2012 | 8.0 |
| 2013 | 7.5 |
| 2014 | 7.0 |
| 2015 | 6.5 |
| 2016 | 6.0 |
| 2017 | 5.5 |
| 2018 | 5.0 |
| 2019 | 4.5 |
| 2020 | 3.5 |
| 2021 | 3.0 |
| 2022 | 3.5 |
| 2023 | 4.0 |
| 2024 | 4.5 |
Gray bars indicate: The data is estimated based on the percentage values shown on the left y-axis and the corresponding x-axis label for the data series.
</details>

![](images/75c0354752b87e40022b01adffe3f0f6ec10ea2d4c54ea7ce5928502b3f72cb7.jpg)

<details>
<summary>line</summary>

Labor Force Participation Rate
| Year | Labor Force Participation Rate (Percent) |
| :--- | :--- |
| 1960 | 59.5 |
| 1965 | 58.5 |
| 1970 | 60.5 |
| 1975 | 61.5 |
| 1980 | 63.5 |
| 1985 | 65.0 |
| 1990 | 66.5 |
| 1995 | 67.0 |
| 2000 | 67.2 |
| 2005 | 66.0 |
| 2010 | 64.5 |
| 2015 | 63.0 |
| 2020 | 60.0 |
| 2021 | 62.5 |
| 2022 | 62.0 |
| 2023 | 61.5 |
The chart displays a line graph representing the labor force participation rate over time. The x-axis represents years from 1960 to 2023, and the y-axis represents the participation rate in percent. The data is labeled as 'Percent'. The shaded vertical bars indicate specific time intervals or regions of interest around the trend line.
</details>

![](images/6d32c70ff10fdccbc8914026fad038a8b7c688b01dc8fd908ea69967ac7fe26f.jpg)

<details>
<summary>line</summary>

| Year | Employment-to-Population Ratio (Percent) |
| ---- | ---------------------------------------- |
| 1960 | 56.0                                     |
| 1970 | 58.0                                     |
| 1980 | 60.0                                     |
| 1990 | 63.0                                     |
| 2000 | 65.0                                     |
| 2010 | 58.0                                     |
| 2020 | 52.0                                     |
| 2025 | 59.0                                     |
</details>

![](images/515e45fafe09e36bc80a754f4483cc581b8688c21765b6983f950f29b0aaf3d1.jpg)

<details>
<summary>line</summary>

| Year | Percentage |
|------|----------|
| 1980 | -3.5     |
| 1985 | -8.0     |
| 1990 | -1.0     |
| 1995 | -5.0     |
| 2000 | 0.5      |
| 2005 | -4.0     |
| 2010 | -8.0     |
| 2015 | -2.0     |
| 2020 | -10.0    |
| 2025 | 3.5      |
</details>

![](images/506d8dc85bc0cef89a6f05f8828d39a15fd2fc945bd3ce89a284f7a3f6f91d72.jpg)

<details>
<summary>line</summary>

| Year | Layoff Rate | Quits Rate |
|------|-------------|------------|
| 2000 | ~1.5        | ~2.3       |
| 2005 | ~1.4        | ~2.1       |
| 2010 | ~1.3        | ~1.3       |
| 2015 | ~1.2        | ~1.8       |
| 2020 | ~1.1        | ~3.0       |
| 2025 | ~1.0        | ~1.9       |
</details>

![](images/262a54547dd999be9bf527848151c42a0453ed8e5984254f3c72f96bf3e0df38.jpg)

<details>
<summary>bar</summary>

| Month | Net Job Gains (Thousands) | 3m avg. (Thousands) |
|---|---|---|
| Jan | 108 | 3 |
| Feb | 76 | 3 |
| Mar | 20 | 3 |
| Apr | 72 | 3 |
| May | 62 | 3 |
| Jun | 34 | 3 |
| Jul | 19 | 3 |
| Aug | -8 | 3 |
| Sep | 24 | 3 |
| Oct | -44 | 3 |
| Nov | -4 | 3 |
| Dec | -38 | 3 |
| Jan | 62 | 3 |
| Feb | -4 | 3 |
| Mar | 64 | 3 |
| Apr | 48 | 3 |
| May | 114 | 3 |
| Jun | 68 | 3 |
| Jul | 34 | 3 |
| Aug | 32 | 3 |
| Sep | 30 | 3 |
| Oct | 32 | 3 |
| Nov | 36 | 3 |
| Dec | 48 | 3 |

Shaded bars indicate GS forecast.
</details>

Source: Bureau of Economic Analysis, US Bureau of Labor Statistics, GS Global Investment Research

# Income

Exhibit 4: We Forecast Only 1.3% Real income Growth in 2026 Due to Energy Price Headwinds, With Significant Underperformance Among Lower-Income Households and Weak Cashflow Growth (Adjusted for Timing of OBBBA Tax Cuts) in 2026H2   
![](images/1eb0ec35dfc1838d83f1abe0bf69f06a18d675b3db81cd81e2c67151415df246.jpg)

<details>
<summary>line</summary>

| Year | Total Income | GS Forecast | Compensation | Transfers | Other |
|------|--------------|-------------|--------------|-----------|-------|
| 2000 | ~5%          | ~5%         | ~5%          | ~5%       | ~5%   |
| 2005 | ~5%          | ~5%         | ~5%          | ~5%       | ~5%   |
| 2010 | ~5%          | ~5%         | ~5%          | ~5%       | ~5%   |
| 2015 | ~5%          | ~5%         | ~5%          | ~5%       | ~5%   |
| 2020 | ~15%         | ~15%        | ~10%         | ~10%      | ~10%  |
| 2025 | ~5%          | ~5%         | ~5%          | ~5%       | ~5%   |
</details>

![](images/d6d8c0dae157c5c43baa2c84711fd1b0ab34533feffdb43a76d8c6b2806dee49.jpg)

<details>
<summary>line</summary>

| Year | Percent change, year ago |
|------|--------------------------|
| 1985 | 4.5                      |
| 1990 | 4.7                      |
| 1995 | 2.2                      |
| 2000 | 5.0                      |
| 2005 | 2.5                      |
| 2010 | 1.2                      |
| 2015 | 2.5                      |
| 2020 | 3.0                      |
| 2025 | 3.5                      |
</details>

![](images/4bcfd6f41d72a8f32d993d0fcffad4c34b51179601c21436a7031c801b77bbfd.jpg)

<details>
<summary>line</summary>

| Year | Bottom | Second | Third | Fourth | Top |
|------|--------|--------|-------|--------|-----|
| 2021 | 1.5    | 1.6    | 1.7   | 1.8    | 1.9 |
| 2022 | 8.0    | 7.5    | 7.3   | 7.1    | 6.5 |
| 2023 | 5.5    | 5.0    | 4.8   | 4.6    | 4.2 |
| 2024 | 3.0    | 2.8    | 2.7   | 2.6    | 2.5 |
| 2025 | 2.5    | 2.4    | 2.3   | 2.2    | 2.1 |
| 2026 | 4.0    | 3.8    | 3.7   | 3.6    | 3.5 |
| 2027 | 2.0    | 1.9    | 1.8   | 1.7    | 1.6 |
</details>

![](images/c9a30ab4e8bb0e48400cece3af39902fde883a765f0614b0bb2fb8f1adb0d964.jpg)

<details>
<summary>bar</summary>

GS 2026 Real Income Growth Forecasts, Q4/Q4 Basis
| Income Cohort | Percent |
| :--- | :--- |
| Bottom | 0.5 |
| Second | 1.5 |
| Third | 1.9 |
| Fourth | 1.7 |
| Fifth | 1.1 |
| Overall | 1.3 |
</details>

![](images/2e96c206ad0d732dc699d0d7c16294282db0e128bea6022f1dadbfad82cc23ab.jpg)

<details>
<summary>area</summary>

| Date     | Lower Payments ($bn) | Higher Refunds ($bn) |
|----------|----------------------|----------------------|
| 1-Jan    | 0                    | 0                    |
| 22-Jan   | 0                    | 0                    |
| 12-Feb   | 10                   | 5                    |
| 5-Mar    | 30                   | 15                   |
| 26-Mar   | 40                   | 25                   |
| 16-Apr   | 70                   | 40                   |
| 7-May    | 140                  | 50                   |
</details>

![](images/cd254faaa9ede380648a48be2930125f114eaf1522414f7a2d0549457c50f7e8.jpg)

<details>
<summary>line</summary>

| Date | Real income (Percent, yoy) | Real cash flow (Percent, yoy) |
|---|---|---|
| Jun-25 | 1.85 | |
| Sep-25 | 1.78 | |
| Dec-25 | 1.28 | 1.3 |
| Mar-26 | 1.08 | 1.58 |
| Jun-26 | 0.48 | 1.15 |
| Sep-26 | 0.65 | 0.25 |
| Dec-26 | 1.25 | 0.65 |
</details>

Source: Bureau of Economic Analysis, GS Global Investment Research

# Wealth/Balance Sheets

Exhibit 5: Household Balance Sheets Are Still Very Strong   
![](images/7b6fb0143f04dc71c9d08b8fdc9be982aa38a6de5fc9d864ef4d3b41e32616c1.jpg)

<details>
<summary>line</summary>

| Year | Assets | Liabilities | Net Worth |
|------|--------|-------------|-----------|
| 1960 | ~600   | ~0          | ~550      |
| 1970 | ~550   | ~0          | ~500      |
| 1980 | ~550   | ~0          | ~450      |
| 1990 | ~550   | ~0          | ~450      |
| 2000 | ~650   | ~0          | ~550      |
| 2010 | ~750   | ~-100       | ~650      |
| 2020 | ~850   | ~-50        | ~750      |
| 2025*| ~900   | ~-50        | ~800      |
</details>

![](images/48edde23be8acaa0a934ce8dc3774fd465a913ce3f818078400059fbb4f71872.jpg)

<details>
<summary>line</summary>

| Year | Personal Saving Rate |
|------|----------------------|
| 1980 | 10.0                 |
| 1985 | 12.0                 |
| 1990 | 8.0                  |
| 1995 | 7.0                  |
| 2000 | 4.0                  |
| 2005 | 2.0                  |
| 2010 | 6.0                  |
| 2015 | 5.0                  |
| 2020 | 24.0                 |
| 2025 | 4.0                  |
</details>

![](images/a0a8dbf8395e054b533eeb409d645bc317c8347a470856658d1353b4ea06ed2e.jpg)

<details>
<summary>line</summary>

| Year | Home Equity | Stocks and Mutual Funds | Other | Net Worth |
|------|-------------|--------------------------|-------|-----------|
| 1980 | ~2          | ~1                       | ~13   | ~14       |
| 1985 | ~1          | ~0                       | ~10   | ~11       |
| 1990 | ~0          | ~-1                      | ~6    | ~7        |
| 1995 | ~1          | ~0                       | ~8    | ~9        |
| 2000 | ~2          | ~-2                      | ~14   | ~15       |
| 2005 | ~3          | ~-3                      | ~16   | ~17       |
| 2010 | ~-5         | ~-5                      | ~-14  | ~-15      |
| 2015 | ~2          | ~0                       | ~12   | ~13       |
| 2020 | ~1          | ~-1                      | ~24   | ~25       |
| 2025 | ~0          | ~0                       | ~10   | ~11       |
</details>

![](images/84e87325c7aac21c11c411020c6699a3d84684b1f2e037f065da9e1e091dd4d0.jpg)  
Source: Bureau of Economic Analysis, US Bureau of Labor Statistics, Federal Reserve Board, GS Global Investment Research

# Debt

Exhibit 6: Overall Debt Levels Are Benign and Credit Growth is Weak, but Credit Card and Subprime Auto Loan Delinquencies Remain Elevated   
![](images/0ba6080086a23ece167a2bd54d4e50c861c8816a21245fbb2410323c00f43bb1.jpg)

<details>
<summary>area</summary>

| Year | Mortgage (%) | Consumer Credit/Other (%) | Total (%) |
|---|

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
