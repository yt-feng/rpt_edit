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
# US Equity Strategy

# 1Q26 Earnings Brief: May 14

84.0% of the S&P 500's market cap has reported. 1Q expectations are for revenues to grow 11.2% and EPS 28.4%. Projected EPS growth among groups varies significantly, as shown below (a blend of consensus estimates and reported results where available):

# Expected EPS Growth YoY

- TECH+: 59.6%   
• Financials: 24.7%   
• Non-Cyclicals: 1.7%   
• Cyclicals ex-Energy: 15.7%   
- Energy: $0.0\%$

The 6 largest TECH+ companies are expected to outgrow the rest of the market as a group (EPS growth 61.2% vs. 17.9%), though forecasts vary for each company:

# Big 6 TECH+ Earnings Growth (Expected vs. Actual, YoY)

• AMZN – 1Q26E: 6.6%; 1Q26A: 81.1%   
• META – 1Q26E: 5.5%; 1Q26A: 62.2%   
• MSFT – 1Q26E: 17.3%; 1Q26A: 23.3%   
• GOOGL – 1Q26E: -7.2%; 1Q26A: 80.8%   
- AAPL – 1Q26E: 15.5%; 1Q26A: 19.1%   
• NVDA – 1Q26E: 115.1%; 1Q26A: Wednesday 20/05

Current consensus estimates suggest only TECH+ and Materials are expected to outpace the S&P 500, while Energy is expected to be a drag on 1Q earnings.

Earnings are beating estimates by 17.3% on aggregate so far, with 78% of companies topping projections to date. EPS is on pace for 28.6%, assuming the historical trend of estimate revisions through the end of reporting season.

Over the next 5 trading days, 12 companies representing 9.9% of the S&P 500's market cap will report results, including Applied Materials, Home Depot, Keysight Tech and NVIDIA.

# Equity Strategy

Americas

Sean Simonds

Strategist

sean.simonds@UBS.com

+1-212-713 2851

Maxwell Grinacoff, CFA

Strategist

maxwell.grinacoff@UBS.com

+1-212-713 3892

Andrew Garthwaite

Strategist

andrew.garthwaite@UBS.com

+44-20-7567 4343

Gerry Fowler

Strategist

gerry.fowler@UBS.com

+44-20-7567 5490

# S&P 500

Figure 1: S&P 500 EPS Growth   
![](images/a5cd1b9610fb1efc2dc79c0e92012f472282826ac91b4f36bc7547b3d4ef251c.jpg)

<details>
<summary>bar</summary>

| Period | Value (%) |
| :--- | :--- |
| 1Q25 | 10.6 |
| 2Q25 | 11.5 |
| 3Q25 | 16.1 |
| 4Q25E | 12.5 |
| 1Q26E | 28.6 |
| Current Consensus Forecast | 28.4 |
Expected Final Reported Growth
</details>

Source: Standard & Poor's, Refinitiv, FactSet, UBS

Expected 1Q EPS Growth is now 28.6% YoY

Figure 2: S&P 500 EPS Growth - Impact from TECH+   
![](images/72d92f6b5f214c753b6b77887daab9b7c551f48f73ad16662c4c0ed75a90c218.jpg)

<details>
<summary>bar</summary>

| Quarter | Value (%) |
| :--- | :--- |
| 1Q25 | 8.1 |
| 2Q25 | 6.9 |
| 3Q25 | 6.5 |
| 4Q25 | 9.3 |
| 1Q26E | 17.3 |
</details>

Source: Standard & Poor's, Refinitiv, FactSet, UBS   
Note: Impact calculated as difference in EPS growth between S&P 500 and S&P 500 ex-TECH+

TECH+ has had an outsized impact on S&P 500 EPS growth over the past year

Figure 3: 1Q26 Earnings Dashboard – S&P 500 

<table><tr><td rowspan="2"></td><td colspan="5">Weighted Growth YoY (%)</td></tr><tr><td>Revenue</td><td>Margins</td><td>Earnings</td><td>Buybacks</td><td>EPS</td></tr><tr><td>S&amp;P 500</td><td>11.2</td><td>16.4</td><td>27.6</td><td>0.8</td><td>28.4</td></tr><tr><td>TECH+</td><td>25.1</td><td>34.1</td><td>59.1</td><td>0.5</td><td>59.6</td></tr><tr><td>Big 6 TECH+</td><td>24.9</td><td>35.9</td><td>60.7</td><td>0.5</td><td>61.2</td></tr><tr><td>Rest of TECH+</td><td>25.3</td><td>30.3</td><td>55.7</td><td>0.4</td><td>56.1</td></tr><tr><td>Cyclicals</td><td>7.1</td><td>3.5</td><td>10.5</td><td>1.3</td><td>11.8</td></tr><tr><td>Cyclicals ex-Energy</td><td>8.0</td><td>5.7</td><td>13.8</td><td>2.0</td><td>15.7</td></tr><tr><td>Energy</td><td>4.4</td><td>-3.8</td><td>0.6</td><td>-0.7</td><td>0.0</td></tr><tr><td>Materials</td><td>10.0</td><td>31.4</td><td>41.4</td><td>0.8</td><td>42.2</td></tr><tr><td>Industrials</td><td>8.2</td><td>-0.8</td><td>7.4</td><td>1.6</td><td>9.0</td></tr><tr><td>Discretionary ex-AMZN</td><td>7.3</td><td>6.2</td><td>13.5</td><td>2.9</td><td>16.4</td></tr><tr><td>Non-Cyclicals</td><td>7.4</td><td>-6.2</td><td>1.2</td><td>0.5</td><td>1.7</td></tr><tr><td>Staples</td><td>6.7</td><td>-0.5</td><td>6.2</td><td>0.8</td><td>7.0</td></tr><tr><td>Health Care</td><td>7.0</td><td>-11.7</td><td>-4.7</td><td>0.9</td><td>-3.8</td></tr><tr><td>Health Care ex-MRK</td><td>7.0</td><td>1.0</td><td>8.0</td><td>1.0</td><td>8.9</td></tr><tr><td>Utilities</td><td>13.7</td><td>3.9</td><td>17.6</td><td>-1.9</td><td>15.7</td></tr><tr><td>REITs</td><td>11.8</td><td>-6.0</td><td>5.8</td><td>-1.7</td><td>4.1</td></tr><tr><td>Telcos</td><td>4.2</td><td>-9.4</td><td>-5.1</td><td>2.0</td><td>-3.1</td></tr><tr><td>Financials</td><td>9.7</td><td>13.7</td><td>23.4</td><td>1.3</td><td>24.7</td></tr><tr><td>S&amp;P 500 ex-TECH+</td><td>7.6</td><td>2.6</td><td>10.2</td><td>0.9</td><td>11.1</td></tr><tr><td>S&amp;P 500 ex-Energy</td><td>11.8</td><td>17.1</td><td>28.8</td><td>0.9</td><td>29.7</td></tr><tr><td>S&amp;P 500 ex-Financials</td><td>11.4</td><td>17.1</td><td>28.5</td><td>0.7</td><td>29.2</td></tr></table>

Source: Standard & Poor's, Refinitiv, FactSet, UBS
Note: Blend of actuals where available and estimates

Figure 4: 1Q26 Surprise Dashboard – S&P 500 

<table><tr><td rowspan="2"></td><td rowspan="2">Rptd</td><td rowspan="2">Total</td><td colspan="3">Surprise (%)</td><td colspan="3">Surprise (%) - Median</td></tr><tr><td>Revenue</td><td>Margins</td><td>Earnings</td><td>Revenue</td><td>Margins</td><td>Earnings</td></tr><tr><td>S&amp;P 500</td><td>456</td><td>500</td><td>2.2</td><td>15.1</td><td>17.3</td><td>1.7</td><td>4.0</td><td>5.7</td></tr><tr><td>TECH+</td><td>65</td><td>83</td><td>2.6</td><td>31.0</td><td>33.5</td><td>1.8</td><td>4.0</td><td>5.9</td></tr><tr><td>Cyclicals</td><td>161</td><td>174</td><td>2.3</td><td>11.6</td><td>13.8</td><td>1.8</td><td>4.8</td><td>6.6</td></tr><tr><td>Energy</td><td>22</td><td>22</td><td>1.6</td><td>17.3</td><td>18.9</td><td>4.0</td><td>10.5</td><td>14.5</td></tr><tr><td>Materials</td><td>26</td><td>26</td><td>3.6</td><td>13.7</td><td>17.3</td><td>3.6</td><td>7.4</td><td>11.1</td></tr><tr><td>Industrials</td><td>76</td><td>79</td><td>2.6</td><td>3.4</td><td>6.0</td><td>1.7</td><td>4.3</td><td>6.0</td></tr><tr><td>Discretionary ex-AMZN</td><td>37</td><td>47</td><td>2.1</td><td>20.9</td><td>22.9</td><td>2.1</td><td>20.9</td><td>22.9</td></tr><tr><td>Non-Cyclicals</td><td>154</td><td>167</td><td>1.7</td><td>6.0</td><td>7.8</td><td>1.8</td><td>2.3</td><td>4.2</td></tr><tr><td>Staples</td><td>26</td><td>35</td><td>1.1</td><td>5.0</td><td>6.1</td><td>1.7</td><td>5.0</td><td>6.7</td></tr><tr><td>Health Care</td><td>55</td><td>59</td><td>1.2</td><td>9.4</td><td>10.6</td><td>1.8</td><td>4.3</td><td>6.1</td></tr><tr><td>Utilities</td><td>31</td><td>31</td><td>6.8</td><td>1.4</td><td>8.3</td><td>4.9</td><td>-1.7</td><td>3.2</td></tr><tr><td>REITs</td><td>31</td><td>31</td><td>2.4</td><td>-3.5</td><td>-1.1</td><td>1.0</td><td>0.2</td><td>1.3</td></tr><tr><td>Telcos</td><td>4</td><td>4</td><td>0.9</td><td>6.0</td><td>6.9</td><td>0.7</td><td>6.9</td><td>7.6</td></tr><tr><td>Financials</td><td>76</td><td>76</td><td>2.7</td><td>3.8</td><td>6.4</td><td>0.6</td><td>3.4</td><td>4.0</td></tr></table>

Source: Standard & Poor's, Refinitiv, FactSet, UBS
Note: Surprise calculated based on revenue beat/miss by +/- 0.25%, earnings beat/miss by +/- 1%

# Price Action

Figure 5: S&P 500 Price Action   
![](images/bea184a6a07786530d4adcdebe6af08ecff09d58b1171f46d771b3a4f10f0420.jpg)

<details>
<summary>heatmap</summary>

Current
| | Revenue Surprises | Beats | Hits/Misses |
|---|---|---|---|
| EPS Surprises | 1.2 | -0.5 | 0.8 |
| Hits/Misses | -1.7 | -2.8 | -2.2 |
| | 0.7 | | |
The chart displays a correlation matrix between the two variables, where higher values (e.g., 0.8) indicate stronger positive correlation with EPS surprises and negative values (e.g., -2.2) indicate weaker negative correlation with EPS surprises and negative correlation with hits/misses. The color scale on the right maps the values to the cells.
</details>

![](images/7461e0c83b5e0d78d27682c446ea7d5a7f87f390f6c78130cdf666ebed45b3e3.jpg)

<details>
<summary>heatmap</summary>

Historical Average
| | Revenue Surprises Beats | Revenue Surprises Hits/Misses | EPS Surprises |
| :--- | :--- | :--- | :--- |
| Beats | 1.7 | -0.4 | 0.9 |
| Hits/Misses | -1.4 | -3.1 | -2.4 |
| | 1.1 | -1.5 | |
</details>

Source: Standard & Poor's, Refinitiv, FactSet, UBS   
Note: Surprises calculated based on revenue beat/miss by +/- 0.25%, earnings beat/miss by +/- 1%. Price performance -1 to +1 days

Figure 6: S&P 500 Price Action Table 

<table><tr><td rowspan="3"></td><td colspan="5">Price Action (%)</td></tr><tr><td rowspan="2">Overall</td><td colspan="2">EPS Beat with</td><td colspan="2">EPS Miss with</td></tr><tr><td>Rev Beat</td><td>Rev Miss</td><td>Rev Beat</td><td>Rev Miss</td></tr><tr><td>S&amp;P 500</td><td>0.2</td><td>1.2</td><td>-0.5</td><td>-1.7</td><td>-2.8</td></tr><tr><td>TECH+</td><td>1.5</td><td>1.7</td><td>4.5</td><td>-8.4</td><td>11.9</td></tr><tr><td>Cyclicals</td><td>0.1</td><td>0.5</td><td>-0.4</td><td>0.3</td><td>-2.9</td></tr><tr><td>Energy</td><td>-0.6</td><td>0.0</td><td>-1.7</td><td>0.6</td><td>-2.8</td></tr><tr><td>Materials</td><td>0.8</td><td>0.9</td><td>-1.7</td><td>1.9</td><td>NA</td></tr><tr><td>Industrials</td><td>1.0</td><td>1.6</td><td>0.7</td><td>-1.9</td><td>-1.2</td></tr><tr><td>Discretionary ex-AMZN</td><td>-1.9</td><td>-2.9</td><td>-0.6</td><td>1.3</td><td>-5.6</td></tr><tr><td>Non-Cyclicals</td><td>0.1</td><td>1.8</td><td>-1.4</td><td>-2.2</td><td>-4.7</td></tr><tr><td>Staples</td><td>1.7</td><td>2.8</td><td>-5.0</td><td>-0.2</td><td>-2.2</td></tr><tr><td>Health Care</td><td>-0.3</td><td>2.0</td><td>-2.8</td><td>-9.7</td><td>-11.6</td></tr><tr><td>Utilities</td><td>-0.6</td><td>-0.7</td><td>0.1</td><td>-1.1</td><td>0.5</td></tr><tr><td>REITs</td><td>0.4</td><td>2.1</td><td>-1.4</td><td>0.8</td><td>-1.4</td></tr><tr><td>Telcos</td><td>3.8</td><td>4.6</td><td>1.4</td><td>NA</td><td>NA</td></tr><tr><td>Financials</td><td>-0.4</td><td>0.6</td><td>-1.3</td><td>0.1</td><td>-2.4</td></tr></table>

Source: Standard & Poor's, Refinitiv, FactSet, UBS   
Note: Surprises calculated based on revenue beat/miss by +/- 0.25%, earnings beat/miss by +/- 1%. Price performance -1 to +1 days

Figure 7: Relative 1d price performance (median %, current reported)   
![](images/ee13722a6f74ccb25848e75ee3f666429583b800dc607e1510f23dea13bb742d.jpg)

<details>
<summary>line</summary>

| Quarter | Perf on earnings beat | Perf on revenue beat | Perf on earnings miss | Perf on revenue miss |
|---------|------------------------|----------------------|------------------------|----------------------|
| Q3 2006 | 0.5                    | 0.5                  | -1.5                   | -1.0                 |
| Q1 2007 | 0.8                    | 0.7                  | -1.8                   | -1.2                 |
| Q3 2007 | 1.0                    | 0.9                  | -2.0                   | -1.4                 |
| Q1 2008 | 1.2                    | 1.1                  | -2.2                   | -1.6                 |
| Q3 2008 | 1.5                    | 1.4                  | -2.5                   | -1.8                 |
| Q1 2009 | 2.8                    | 2.7                  | -2.8                   | -2.0                 |
| Q3 2009 | 0.0                    | 0.0                  | -3.0                   | -2.2                 |
| Q1 2010 | 0.3                    | 0.4                  | -2.5                   | -1.8                 |
| Q3 2010 | 0.5                    | 0.6                  | -2.0                   | -1.5                 |
| Q1 2011 | 0.7                    | 0.8                  | -1.5                   | -1.2                 |
| Q3 2011 | 1.0                    | 1.1                  | -1.0                   | -0.8                 |
| Q1 2012 | 0.5                    | 0.6                  | -0.5                   | -0.3                 |
| Q3 2012 | 0.8                    | 0.9                  | 0.0                    | 0.1                  |
| Q1 2013 | 1.2                    | 1.3                  | 0.3                    | 0.4                  |
| Q3 2013 | 0.8                    | 0.9                  | -0.5                   | -0.2                 |
| Q1 2014 | 0.5                    | 0.6                  | -1.0                   | -0.6                 |
| Q3 2014 | 0.7                    | 0.8                  | -1.3                   | -0.9                 |
| Q1 2015 | 1.0                    | 1.1                  | -1.5                   | -1.1                 |
| Q3 2015 | 1.2                    | 1.3                  | -1.8                   | -1.3                 |
| Q1 2016 | 1.5                    | 1.4                  | -2.0                   | -1.5                 |
| Q3 2016 | 1.3                    | 1.5                  | -2.2                   | -1.7                 |
| Q1 2017 | 1.0                    | 1.1                  | -2.5                   | -2.0                 |
| Q3 2017 | 0.8                    | 0.9                  | -2.8                   | -2.2                 |
| Q1 2018 | 0.5                    | 0.6                  | -3.0                   | -2.4                 |
| Q3 2018 | 0.7                    | 0.8                  | -3.2                   | -2.6                 |
| Q1 2019 | 1.2                    | 1.3                  | -3.5                   | -3.0                 |
| Q3 2019 | 1.4                    | 1.5                  | -3.8                   | -3.2                 |
| Q1 2020 | 1.6                    | 1.7                  | -4.0                   | -3.4                 |
| Q3 2020 | 1.3                    | 1.5                  | -4.2                   | -3.6                 |
| Q1 2021 | 1.5                    | 1.7                  | -4.4                   | -3.8                 |
| Q3 2021 | 1.7                    | 1.9                  | -4.6                   | -4.0                 |
| Q1 2022 | 1.5                    | 1.6                  | -4.8                   | -4.2                 |
| Q3 2022 | 1.8                    | 1.8                  | -5.0                   | -4.4                 |
| Q1 2023 | 1.6                    | 1.5                  | -5.2                   | -4.6                 |
| Q3 2023 | 1.4                    | 1.3                  | -5.4                   | -4.8                 |
| Q1 2024 | 2.2                    | 2.3                  | -5.6                   | -5.0                 |
| Q3 2024 | 1.8                    | 1.9                  | -5.8                   | -5.2                 |
| Q1 2025 | 1.5                    | 1.6                  | -6.0                   | -5.4                 |
| Q3 2025 | 1.7                    | 1.8                  | -6.2                   | -5.6                 |
| Q1 2026 | 2.0                    | 2.1                  | -6.4                   | -5.8                 |
</details>

Source: Standard & Poor's, Refinitiv, FactSet, UBS

Figure 8: 1Q26 EPS Growth YoY 

<table><tr><td rowspan="2"></td><td colspan="2">EPS</td></tr><tr><td>Weighted</td><td>Median</td></tr><tr><td>S&amp;P 500</td><td>28.4</td><td>12.9</td></tr><tr><td>TECH+</td><td>59.6</td><td>26.2</td></tr><tr><td>Cyclicals</td><td>11.8</td><td>11.4</td></tr><tr><td>Energy</td><td>0.0</td><td>16.0</td></tr><tr><td>Materials</td><td>42.2</td><td>8.5</td></tr><tr><td>Industrials</td><td>9.0</td><td>12.0</td></tr><tr><td>Discretionary ex-AMZN</td><td>16.4</td><td>8.3</td></tr><tr><td>Non-Cyclicals</td><td>1.7</td><td>7.3</td></tr><tr><td>Staples</td><td>7.0</td><td>6.6</td></tr><tr><td>Health Care</td><td>-3.8</td><td>9.6</td></tr><tr><td>Utilities</td><td>15.7</td><td>7.5</td></tr><tr><td>REITs</td><td>4.1</td><td>2.4</td></tr><tr><td>Telcos</td><td>-3.1</td><td>-2.2</td></tr><tr><td>Financials</td><td>24.7</td><td>20.0</td></tr></table>

Source: Standard & Poor's, Refinitiv, FactSet, UBS   
Note: AMZN is included in TECH+, not Cyclicals / Discretionary

The median company is expected to outgrow the cap-weighted index in 4 out of 11 groups

On a median basis, Tech+ and Financials are expected to see the strongest growth

Figure 9: 1Q26 S&P 500 EPS Growth YoY   
![](images/4fdc492f23a89ab4519b71217f38f663a91f6949a4a94725a9543d117645ddd7.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| Big 6 TECH+ | 61.2 |
| Rest of TECH+ | 56.1 |
| Mats | 42.2 |
| S&P 500 | 28.4 |
| Fins | 24.7 |
| S&P 500 ex-Big 6 | 17.9 |
| Disc ex-AMZN | 16.4 |
| Utils | 15.7 |
| Ind | 9.0 |
| Stap | 7.0 |
| REITs | 4.1 |
| Ene | 0.0 |
| Telcos | -3.1 |
| H.C. | -3.8 |
</details>

TECH+ and Materials are expected to outpace the rest of the market

Energy is expected to be a drag

Source: Standard & Poor's, Refinitiv, FactSet, UBS

Note: AMZN included in TECH+, not Discretionary; blend of actuals where available and estimates

Figure 10: 2026E S&P 500 EPS Growth YoY   
![](images/b7375569be9bf775e1f9c9cbabb878c899de97a8c1bbaa30a12a89258621a829.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| Ene | 55.0 |
| Rest of TECH+ | 46.4 |
| Mats | 38.4 |
| Big 6 TECH+ | 33.5 |
| S&P 500 | 22.2 |
| S&P 500 ex-Big 6 | 18.6 |
| Fins | 11.9 |
| Utils | 10.6 |
| Ind | 10.2 |
| Disc ex-AMZN | 8.3 |
| Stap | 6.7 |
| REITs | 5.1 |
| H.C. | 3.8 |
| Telcos | 0.1 |
</details>

S&P 500 is expected to grow at

22.2% based on consensus estimates

Source: Standard & Poor's, Refinitiv, FactSet, UBS

Note: AMZN included in TECH+, not Discretionary

Figure 11: 1Q26E S&P 500 Industry Group EPS Growth YoY   
![](images/bbb33be1503ed9b1fa86c56416a53b66a9b7a1f65d94143542c91fc04f947ee1.jpg)

<details>
<summary>bar</summary>

| Sector | Value (%) |
| :--- | :--- |
| Semis & Equip | 101.3 |
| Autos & Comp | 78.2 |
| Media & Entertain | 70.6 |
| Insurance | 47.8 |
| Retailing | 47.1 |
| Materials | 42.2 |
| Tech Hdw & Equip | 36.0 |
| S&P 500 | 28.4 |
| Banks | 21.8 |
| Software & Svcs | 21.5 |
| Div Financials | 19.2 |
| Consumer Svcs | 16.4 |
| Utilities | 15.7 |
| Capital Goods | 14.5 |
| Comm & Prof Svcs | 9.7 |
| Food & Stap Retail | 9.0 |
| HH & Personal Prod | 7.2 |
| HC Equip & Svcs | 6.5 |
| Food Bev & Tob | 5.9 |
| Real Estate | 4.1 |
| Energy | 0.0 |
| Telecom | -3.1 |
| Transportation | -9.4 |
| Pharma Biotech & LS | -11.8 |
| Cons Dur & App | -18.2 |
</details>

Source: Standard & Poor's, Refinitiv, FactSet, UBS

Figure 12: 2026E S&P 500 Industry Group EPS Growth YoY   
![](images/a150835b2e67d610c4c634a042b4c3f1da21e4e35cbaf94967aa8abff32e334a.jpg)

<details>
<summary>bar</summary>

| Sector | Value (%) |
| :--- | :--- |
| Semis & Equip | 75.7 |
| Energy | 55.0 |
| Materials | 38.4 |
| Media & Entertain | 35.8 |
| Tech Hdwr & Eq

[中间内容因长度限制已省略]

ny recommendations or opinions in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: ol-UBS-sec-compliance@UBS.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.UBS.com/global/en/about\_UBS/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.UBS.com/UBSsi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a sUBSidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian Citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian Citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/10a9466d3aacd698c81d5a75f099f4d5511c95d66540891783d8202af0b22e5f.jpg)

# UBS
"""
