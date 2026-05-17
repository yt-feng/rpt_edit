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
JAPAN WEEKLY KICKSTART

# Critical thinking; 4Q 3/26 results summary (as of May 14)

# Summary of the week

TOPIX: 3,863.97 (0.9%) / NK225: 61,409.29 (-2.1%)

■ Top sectors: Insurance, Trading/Wholesale   
■ Bottom sectors: Non-Ferrous Metals, Machinery

In this week's Japan Weekly Kickstart we focus on the recent performance of our GS Japan Critical Resources (GSJPCRTR) basket. This basket was initially highlighted last March (LINK), and was designed to give clients exposure to areas where we expected to see Economic Security concerns drive increased demand. It includes exposure to sectors where companies are involved in the extraction, transportation and/or processing of critical resources (such as Trading Companies, Energy Resources companies and Shippers), and has been a very strong performer so far this year (Exhibit 1). The basket is currently $+43\%$ ytd (vs. TOPIX $+12\%$ ), and should continue to see interest while the geopolitical situation in the Middle East remains relatively volatile.

FY3/26 earnings results (as of May 14): 84% of Feb/Mar fiscal year-end TOPIX companies (by market-cap) have reported 4Q earnings, and the number of positive surprises (54%) exceeded negative surprises (35%). At an aggregate level, TOPIX 4Q/FY net profit growth is +16/+2pp versus consensus (Exhibit 4), but only in-line when excluding Softbank Group. Guidance now seems to be slightly more conservative than usual (Exhibit 6).   
Price reaction: As we highlighted in Why does geopolitical risk no longer seem to matter?, the performance concentration of the Japanese equities market remained high entering the earnings results season. As can be seen in Exhibit 8 below, 1M momentum stocks reacted strongly to negative surprises while positive surprises were not rewarded. We also had high dispersion in price reactions this season (Exhibit 9).   
Foreigners were net buyers, Domestic Institutions and Individuals were net sellers: According to the latest data from the TSE, for the week 7-8 May, Foreigners net bought ¥1.2tn of TSE Prime cash equities, while Domestic Institutions and Individuals net sold -¥457bn and -¥468bn respectively.

Bruce Kirk, CFA

+81(3)4587-9950 | bruce.kirk@gs.com

GS Japan Co., Ltd.

Julius Chan

+81(3)4587-1789 | julius.chan@gs.com

GS Japan Co., Ltd.

Mark Hung

+852-3465-4266 | mark.hung@gs.com

GS (Asia) L.L.C.

# Japan Critical Resources and Critical Technologies Baskets

Exhibit 1: GSJPCRTT and GSJPCRTR have outperformed TOPIX   
Data as of May 14, 2026   
![](images/7a10f64946dfeecab9cb7018212b0491eacf8cec78bf03fd631c728949b08407.jpg)

<details>
<summary>line</summary>

| Date   | GSJPCRTT | GSJPCRTR | TOPIX |
|--------|----------|----------|-------|
| 1/25   | 100      | 100      | 100   |
| 4/25   | 80       | 80       | 80    |
| 7/25   | 100      | 100      | 100   |
| 10/25  | 120      | 130      | 110   |
| 1/26   | 130      | 150      | 120   |
| 4/26   | 150      | 200      | 130   |
| 7/26   | 160      | 220      | 140   |
</details>

Source: FactSet, Data compiled by GS Global Investment Research

# 4Q earnings summary (as of May 14)

# Exhibit 2: So far, 4Q positive surprises exceed negative surprises

TOPIX constituent companies with Feb/Mar fiscal year-end, as of May 14

![](images/06f04820d564dcc69714f1ce3836aba284f84328ce707fb8a33b0e7e91380381.jpg)

<details>
<summary>bar_line</summary>

| Quarter | % of Positive - % of Negative Surprises Cos (lhs) | Global CAI (3M-Avg, rhs) |
|---------|-----------------------------------------------|--------------------------|
| 16-1Q   | ~10%                                          | ~2%                      |
| 3Q      | ~30%                                          | ~4%                      |
| 17-1Q   | ~35%                                          | ~5%                      |
| 3Q      | ~15%                                          | ~4%                      |
| 18-1Q   | ~10%                                          | ~3%                      |
| 3Q      | ~0%                                           | ~2%                      |
| 19-1Q   | ~5%                                           | ~1%                      |
| 3Q      | ~-20%                                         | ~0%                      |
| 20-1Q   | ~25%                                          | ~8%                      |
| 3Q      | ~45%                                          | ~6%                      |
| 21-1Q   | ~50%                                          | ~5%                      |
| 3Q      | ~25%                                          | ~4%                      |
| 22-1Q   | ~20%                                          | ~3%                      |
| 3Q      | ~-10%                                         | ~2%                      |
| 23-1Q   | ~30%                                          | ~4%                      |
| 3Q      | ~15%                                          | ~3%                      |
| 24-1Q   | ~30%                                          | ~4%                      |
| 3Q      | ~-5%                                          | ~3%                      |
| 25-1Q   | ~10%                                          | ~2%                      |
| 3Q      | ~20%                                          | ~3%                      |
</details>

Source: I/B/E/S, Toyo Keizai, FactSet, GS Global Investment Research

# Exhibit 4: Blended YoY 4Q/FY net profits is +16/+2pp above pre-season consensus, but only in-line excluding Softbank-Group

TOPIX constituent companies with Feb/Mar fiscal year-ends, as of May 14

<table><tr><td rowspan="2"></td><td colspan="3">4Q Net Profit Blended YoY (%)</td><td colspan="3">FY3/26 Full-year Net Profit Blended YoY (%)</td></tr><tr><td>consensus (4/13)</td><td>Latest</td><td>%-point</td><td>consensus (4/13)</td><td>Latest</td><td>%-point</td></tr><tr><td>TOPIX companies</td><td>22</td><td>38</td><td>+16</td><td>7</td><td>9</td><td>+2</td></tr><tr><td>ex-Financials</td><td>14</td><td>32</td><td>+18</td><td>4</td><td>6</td><td>+2</td></tr><tr><td>Manufacturers</td><td>43</td><td>35</td><td>-9</td><td>0</td><td>-6</td><td>-6</td></tr><tr><td>Nonmanufacturers</td><td>-8</td><td>30</td><td>+38</td><td>8</td><td>18</td><td>+10</td></tr><tr><td>Financials</td><td>67</td><td>72</td><td>+5</td><td>21</td><td>24</td><td>+3</td></tr><tr><td colspan="7">Excluding SoftbankGr</td></tr><tr><td>TOPIX (ex-SoftbankGr)</td><td>26</td><td>26</td><td>-0</td><td>3</td><td>2</td><td>-1</td></tr><tr><td>Non-Mfg (ex-SoftbankGr)</td><td>-3</td><td>3</td><td>+5</td><td>-3</td><td>-0</td><td>+3</td></tr></table>

Source: I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

# Exhibit 3: So far, 54%/35% of companies reported positive/negative earnings surprises

TOPIX constituent companies with Feb/Mar fiscal year-end, as of May 14

<table><tr><td rowspan="2"></td><td colspan="2">% - reported</td><td colspan="3">Surprise 4Q vs Consensus</td></tr><tr><td>by Cos</td><td>by Mcap</td><td>% of +ve</td><td>% of -ve</td><td>#-of data</td></tr><tr><td>TOPIX</td><td>85%</td><td>84%</td><td>54%</td><td>35%</td><td>630</td></tr><tr><td>ex-Financials</td><td>86%</td><td>93%</td><td>55%</td><td>36%</td><td>600</td></tr><tr><td>Manufacturers</td><td>85%</td><td>93%</td><td>55%</td><td>34%</td><td>323</td></tr><tr><td>Nonmanufacturers</td><td>88%</td><td>92%</td><td>54%</td><td>37%</td><td>277</td></tr><tr><td>Financials</td><td>72%</td><td>42%</td><td>50%</td><td>33%</td><td>30</td></tr></table>

Source: I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

# Exhibit 5: FY25 Q4 surprises by sector

TOPIX constituent stocks with Feb/Mar fiscal year-ends, as of May 14

![](images/e089d63d4f93c8c419d3993597b2d41704636a3ae5eeeebf04a51fbdfb68241f.jpg)

<details>
<summary>bar</summary>

| Sector | %-of +ve surprise cos | In-line | -ve surprise |
| --- | --- | --- | --- |
| Energy Resources | 80% | 0% | 0% |
| Construction & Materials | 75% | 0% | 0% |
| Pharmaceutical | 65% | 0% | 0% |
| Banks | 55% | 0% | 0% |
| Steel & Nonferrous Metals | 45% | 0% | 0% |
| Auto & Parts | 40% | 0% | 0% |
| Transportation & Logistics | 35% | 0% | 0% |
| Retail Trade | 30% | 0% | 0% |
| Machinery | 25% | 0% | 0% |
| Trading | 20% | 0% | 0% |
| Raw Materials & Chemicals | 15% | 0% | 0% |
| Electric Appl. & Precisions | 10% | 0% | 0% |
| Foods | 5% | 0% | 0% |
| Real Estate | 0% | 0% | 0% |
| Electric Power & Gas | -5% | 0% | 0% |
| IT & Services Others | -10% | 0% | 0% |
| Financials ex-Banks | -15% | 0% | 0% |
</details>

Source: I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

Exhibit 6: Guidance is slightly more conservative than history, -9.2% vs consensus (10y median is -8.1%)   
Data as of May 14   
![](images/362723fe79a79b3c505200067ad32c40d2bd58a4146c072b997866ae093b065e.jpg)

<details>
<summary>bar_line</summary>

| Fiscal Year | %- Surprise: New guidance vs IBES consensus (lhs) (%) | %- of companies with +ve surprise (rhs) (%) | %- of companies with -ve surprise (rhs) (%) |
|---|---|---|---|
| FY3/03 | -15.0 | 35.0 | 40.0 |
| FY3/04 | 5.0 | 30.0 | 35.0 |
| FY3/05 | -2.0 | 25.0 | 45.0 |
| FY3/06 | -5.0 | 20.0 | 55.0 |
| FY3/07 | -8.0 | 15.0 | 65.0 |
| FY3/08 | -15.0 | 10.0 | 75.0 |
| FY3/09 | -25.0 | 15.0 | 60.0 |
| FY3/10 | -10.0 | 20.0 | 50.0 |
| FY3/11 | -5.0 | 25.0 | 45.0 |
| FY3/12 | -2.0 | 30.0 | 40.0 |
| FY3/13 | -1.0 | 35.0 | 35.0 |
| FY3/14 | -2.0 | 40.0 | 45.0 |
| FY3/15 | -3.0 | 45.0 | 50.0 |
| FY3/16 | -4.0 | 50.0 | 55.0 |
| FY3/17 | -5.0 | 55.0 | 60.0 |
| FY3/18 | -6.0 | 60.0 | 65.0 |
| FY3/19 | -7.0 | 65.0 | 70.0 |
| FY3/20 | -25.0 | 75.0 | 85.0 |
| FY3/21 | -8.0 | 65.0 | 75.0 |
| FY3/22 | -7.0 | 60.0 | 70.0 |
| FY3/23 | -6.0 | 55.0 | 65.0 |
| FY3/24 | -7.0 | 50.0 | 60.0 |
| FY3/25 | -8.0 | 45.0 | 55.0 |
| FY3/26 | -9.0 | 40.0 | 50.0 |
</details>

Source: I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

# Exhibit 7: Share price reaction post results announcement

TOPIX constituent stocks with Mar fiscal year-end, median TOPIX-relative price reaction, as of May 15

![](images/a631471b20c7e8e95924b6e3f1ab93a5e401e175f20ca568fcb4faafc7e4b542.jpg)

<details>
<summary>line</summary>

| Period | 4Q Profit: Positive surprise | 4Q Profit: Negative surprise | All stocks |
|--------|------------------------------|------------------------------|------------|
| 0D     | 0.0%                         | 0.0%                         | 0.0%       |
| +1D    | ~0.8%                        | ~-2.0%                       | ~-0.2%     |
| +2D    | ~1.2%                        | ~-2.0%                       | ~-0.3%     |
| +3D    | ~0.0%                        | ~-3.5%                       | ~-1.0%     |
</details>

![](images/aea8686777e7dae36b457df08376b11b85f754764d8b11dfc113ef6cb3ccd82f.jpg)

<details>
<summary>line</summary>

| Period | New Guidance: Positive surprise (%) | New Guidance: Negative surprise (%) |
|--------|-------------------------------------|--------------------------------------|
| 0D     | 0.0%                                | 0.0%                                 |
| +1D    | 4.5%                                | -4.0%                                |
| +2D    | 4.5%                                | -3.5%                                |
| +3D    | 3.5%                                | -4.5%                                |
</details>

![](images/651da6d2fe3f155e0acc82ba980c62a02ac613de177c8c9fdc263cb89dfdfb5f.jpg)

<details>
<summary>line</summary>

| Period | With new year guidance | No disclosure of new year guidance |
| ------ | ---------------------- | ---------------------------------- |
| 0D     | 0.0%                   | 0.0%                               |
| +1D    | -0.2%                  | -1.8%                              |
| +2D    | -0.4%                  | -2.0%                              |
| +3D    | -1.0%                  | -2.1%                              |
</details>

Source: QUICK, I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

# Exhibit 8: Momentum stocks reacted strongly to negative surprises and did not react to positive surprises

1M momentum stocks with Mar fiscal year end, median TOPIX-relative price reaction, as of May 15

![](images/5f7805cc20aa68a344311c4683b83964ae12da47aab92e4659a081317e95b74e.jpg)

<details>
<summary>line</summary>

| Period | 4Q Profit: Positive surprise | 4Q Profit: Negative surprise |
| ------ | ---------------------------- | ---------------------------- |
| 0D     | 0.0%                         | 0.0%                         |
| +1D    | -1.0%                        | -5.0%                        |
| +2D    | -1.0%                        | -5.5%                        |
| +3D    | 1.5%                         | -5.0%                        |
</details>

Source: QUICK, I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

# Exhibit 9: Spike in standard deviation of +1D price reactions

As of May 15

![](images/24ac189eb9ccc8f7e22e344f8fe8221d1d4972513355a76c755e75cff72c6768.jpg)

<details>
<summary>line</summary>

| Quarter | Value |
| ------- | ----- |
| 3Q 2025 | 7.7%  |
</details>

Source: QUICK, I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

# Market Dashboard

Performance table 

<table><tr><td>Sector / Thematic Index</td><td>1-week</td><td>1-month</td><td>3-month</td><td>6-month</td><td>52-week</td><td>YTD</td></tr><tr><td>Autos</td><td>10%</td><td>3%</td><td>-15%</td><td>-7%</td><td>10%</td><td>-9%</td></tr><tr><td>Insurers</td><td>8%</td><td>5%</td><td>5%</td><td>26%</td><td>43%</td><td>18%</td></tr><tr><td>Trading Companies</td><td>7%</td><td>9%</td><td>4%</td><td>41%</td><td>96%</td><td>33%</td></tr><tr><td>High Dividend Yield</td><td>5%</td><td>1%</td><td>-1%</td><td>14%</td><td>26%</td><td>10%</td></tr><tr><td>Financials</td><td>4%</td><td>1%</td><td>-4%</td><td>25%</td><td>54%</td><td>16%</td></tr><tr><td>Energy</td><td>4%</td><td>-6%</td><td>0%</td><td>17%</td><td>107%</td><td>19%</td></tr><tr><td>PBR Below 1.0x</td><td>3%</td><td>1%</td><td>4%</td><td>24%</td><td>52%</td><td>19%</td></tr><tr><td>Mega Banks</td><td>3%</td><td>0%</td><td>-6%</td><td>27%</td><td>66%</td><td>17%</td></tr><tr><td>Auto Components</td><td>3%</td><td>5%</td><td>-1%</td><td>6%</td><td>37%</td><td>6%</td></tr><tr><td>Consumer Discretionary</td><td>3%</td><td>0%</td><td>-7%</td><td>1%</td><td>30%</td><td>2%</td></tr><tr><td>Brokers</td><td>3%</td><td>-5%</td><td>-11%</td><td>4%</td><td>53%</td><td>-1%</td></tr><tr><td>US Demand</td><td>3%</td><td>-1%</td><td>-4%</td><td>8%</td><td>46%</td><td>8%</td></tr><tr><td>Telcos</td><td>2%</td><td>-1%</td><td>-2%</td><td>-3%</td><td>2%</td><td>-3%</td></tr><tr><td>PBR Between 1.0-2.0x</td><td>2%</td><td>4%</td><td>2%</td><td>25%</td><td>58%</td><td>21%</td></tr><tr><td>Apple Supply Chain</td><td>2%</td><td>18%</td><td>28%</td><td>46%</td><td>103%</td><td>44%</td></tr><tr><td>EU Demand</td><td>2%</td><td>5%</td><td>14%</td><td>29%</td><td>103%</td><td>28%</td></tr><tr><td>Electronic Components</td><td>1%</td><td>18%</td><td>52%</td><td>104%</td><td>310%</td><td>105%</td></tr><tr><td>Materials</td><td>1%</td><td>3%</td><td>4%</td><td>43%</td><td>142%</td><td>36%</td></tr><tr><td>Factory Automation</td><td>0%</td><td>26%</td><td>33%</td><td>62%</td><td>75%</td><td>48%</td></tr><tr><td>Shippers</td><td>0%</td><td>-7%</td><td>11%</td><td>20%</td><td>13%</td><td>16%</td></tr><tr><td>Exporters</td><td>0%</td><td>4%</td><td>12%</td><td>35%</td><td>111%</td><td>33%</td></tr><tr><td>Gaming</td><td>0%</td><td>-5%</td><td>-4%</td><td>-21%</td><td>-11%</td><td>-14%</td></tr><tr><td>Medical Devices</td><td>0%</td><td>-7%</td><td>-7%</td><td>-18%</td><td>-10%</td><td>-13%</td></tr><tr><td>Health Care</td><td>0%</td><td>-7%</td><td>-6%</td><td>-2%</td><td>18%</td><td>-1%</td></tr><tr><td>Retail</td><td>-1%</td><td>-4%</td><td>-10%</td><td>-1%</td><td>10%</td><td>-1%</td></tr><tr><td>Defense</td><td>-1%</td><td>-3%</td><td>-9%</td><td>9%</td><td>59%</td><td>13%</td></tr><tr><td>Industrials</td><td>-1%</td><td>6%</td><td>6%</td><td>30%</td><td>87%</td><td>28%</td></tr><tr><td>Pharma</td><td>-1%</td><td>-7%</td><td>-7%</td><td>4%</td><td>31%</td><td>4%</td></tr><tr><td>Internet</td><td>-1%</td><td>-1%</td><td>-1%</td><td>-7%</td><td>12%</td><td>-5%</td></tr><tr><td>Consumer Staples</td><td>-1%</td><td>-5%</td><td>-11%</td><td>-2%</td><td>3%</td><td>-2%</td></tr><tr><td>Utilities</td><td>-2%</td><td>-6%</td><td>-10%</td><td>-1%</td><td>46%</td><td>1%</td></tr><tr><td>Machinery</td><td>-2%</td><td>9%</td><td>8%</td><td>37%</td><td>88%</td><td>31%</td></tr><tr><td>Food and Beverage</td><td>-2%</td><td>-5%</td><td>-7%</td><td>0%</td><td>5%</td><td>2%</td></tr><tr><td>Domestic Demand</td><td>-2%</td><td>-4%</td><td>-9%</td><td>-1%</td><td>23%</td><td>-2%</td></tr><tr><td>PBR Between 2.0-4.0x</td><td>-2%</td><td>2%</td><td>2%</td><td>16%</td><td>88%</td><td>18%</td></tr><tr><td>Information Technology</td><td>-2%</td><td>9%</td><td>23%</td><td>44%</td><td>146%</td><td>42%</td></tr><tr><td>China Demand</td><td>-2%</td><td>7%</td><td>14%</td><td>40%</td><td>90%</td><td>36%</td></tr><tr><td>Travel</td><td>-2%</td><td>-7%</td><td>-16%</td><td>-12%</td><td>0%</td><td>-12%</td></tr><tr><td>System Integrators</td><td>-4%</td><td>-8%</td><td>-2%</td><td>-27%</td><td>-11%</td><td>-24%</td></tr><tr><td>PBR Above 4.0x</td><td>-4%</td><td>-1%</td><td>0%</td><td>8%</td><td>82%</td><td>10%</td></tr><tr><td>AI Beneficiaries</td><td>-4%</td><td>15%</td><td>25%</td><td>57%</td><td>205%</td><td>57%</td></tr><tr><td>SPE</td><td>-4%</td><td>5%</td><td>11%</td><td>48%</td><td>129%</td><td>41%</td></tr><tr><td>Real Estate</td><td>-6%</td><td>-8%</td><td>-15%</td><td>1%</td><td>21%</td><td>-1%</td></tr><tr><td>Construction</td><td>-7%</td><td>-3%</td><td>-18%</td><td>12%</td><td>105%</td><td>3%</td></tr><tr><td>Cosmetics and Personal Care</td><td>-13%</td><td>-9%</td><td>-19%</td><td>-14%</td><td>-3%</td><td>-3%</td></tr></table>

Source: FactSet, GS Global Investment Research

Best-Worst spread table 

<table><tr><td>Sector / Thematic Index</td><td>1-week</td><td>1-month</td><td>3-month</td><td>6-month</td><td>52-week</td><td>YTD</td></tr><tr><td>PBR Above 4.0x</td><td>52%</td><td>83%</td><td>145%</td><td>424%</td><td>1982%</td><td>377%</td></tr><tr><td>Domestic Demand</td><td>47%</td><td>41%</td><td>60%</td><td>113%</td><td>274%</td><td>112%</td></tr><tr><td>Materials</td><td>46%</td><td>52%</td><td>114%</td><td>210%</td><td>968%</td

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or

performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
