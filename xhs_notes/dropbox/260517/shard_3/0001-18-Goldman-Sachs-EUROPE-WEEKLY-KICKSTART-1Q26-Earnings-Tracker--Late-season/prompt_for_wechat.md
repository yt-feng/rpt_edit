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
EUROPE WEEKLY KICKSTART

1Q26 Earnings Tracker: Late season update

The bulk of the season is behind us. As of today, more than 280 companies included in our Tracker have reported earnings, representing roughly 75% of the total market cap due to report in 1Q26 season.

Earnings beats remain positive but concentrated. So far in the season, EPS has surprised by around 2.3% on a cap-weighted basis, only slightly below the historical average (Exhibit 1). Financials and Commodities, whose companies tend to report quarterly to a greater extent than the rest of the market, are continuing to lead the positive surprises. At the margin, and despite lower Middle East sales given the Iran conflict, Consumer companies are also contributing to aggregate earnings beats. Among those under our Equity research coverage, Puma and Adidas reported earnings ahead of expectations, with their share prices up 5% and 8% on reporting day, respectively. In the retail space, our sector analysts have also highlighted better than expected US margins for Ahold Delhaize and adj. EBIT for Zalando.

EU Big Oils are experiencing a strong 1Q26 season with sector Operating Cash Flow beating expectations by 9%, offsetting the higher-than-expected capex and driving solid FCF delivery. Our Equity analysts expect further upside for LNG trading profits and upstream earnings in Q2, and rising profits point to a major capex upcycle from 2027.

Capital goods are showing strong order momentum (on which 77% of our Equity research coverage surprised to the upside) in the 1Q26 season led by AI/datacentre demand, but our analysts note that investors have flagged concerns that pre-buy activity may have inflated order strength, as conversion of orders into sales (c. 70% missed) seems to be getting longer. Furthermore, companies that have reported earnings are showing margins under pressure (c.50% missed) from input costs.

Earnings misses continue to be penalised, while beats are only marginally rewarded. On average, companies missing expectations have underperformed the market by c.1.5% on the reporting day, whereas earnings beats have outperformed by less than 1% (Exhibit 2).

Companies providing guidance away from consensus expectations are seeing a smaller price reaction than has historically been the case, possibly because the increasing macro uncertainty is contributing to make these estimates less reliable. Of the 450 SXXP companies that have reported earnings or published a shorter interim

Peter Oppenheimer

+44(20)7552-5782

peter.Oppenheimer@gs.com

GS International

Sharon Bell

+44(20)7552-1341

sharon.bell@gs.com

GS International

Guillaume Jaisson

+44(20)7552-3000

guillaume.jaisson@gs.com

GS International

Giovanni Ferrannini

+44(20)7051-2589

giovanni.ferrannini@gs.com

GS International

report in the current season, ca. 140 have also issued their 2026 guidance on at least one key financial item. Roughly half of these names provided guidance below analysts' expectations while performing in line with the market on the reporting day (Exhibit 3) (in all cases in which guidance was provided as a range, we match the range mid-point against consensus expectations). On the other hand, companies guiding above consensus have outperformed the market by less than 1% (vs. >2% during last earnings season).

Aggregate earnings upgrades continue to be sustained by commodity-related sectors. Exhibit 4 shows that Energy and Basic Resources names are guiding the aggregate 4% EPS upgrade observed since the outbreak of the Iran war. Chemicals producers, which are proving able to pass higher costs through to downstream buyers, have also experienced positive earnings revisions since the start of the season (+3%, vs. +1.5% for the market). Outside of the commodities space: higher real rates, more active fiscal policy, reshoring, supply-chain reconfiguration and geopolitics all remain supportive our basket of capital-intensive stocks (GSSTCAPI), whose 2026 earnings have been revised up by 3% in the past month.

Exhibit 1: EPS has surprised by around 2%, only slightly below the historical average   
Equal Weighted (%)   
![](images/402672a602a2c2c697d30a9e832d6bbffe697823493f3dbba750258ebfece6b1.jpg)

<details>
<summary>bar</summary>

| Quarter | SXXP Earnings Surprise |
| ------- | ---------------------- |
| Q1 10   | 7.0%                   |
| Q1 11   | 5.0%                   |
| Q1 12   | -5.0%                  |
| Q1 13   | 2.0%                   |
| Q1 14   | -2.0%                  |
| Q1 15   | 5.0%                   |
| Q1 16   | 4.0%                   |
| Q1 17   | 12.0%                  |
| Q1 18   | 3.0%                   |
| Q1 19   | 2.0%                   |
| Q1 20   | -3.0%                  |
| Q1 21   | 13.0%                  |
| Q1 22   | 8.0%                   |
| Q1 23   | 6.0%                   |
| Q1 24   | 5.0%                   |
| Q1 25   | 3.0%                   |
| Q1 26   | 2.0%                   |
</details>

Source: Bloomberg, FactSet, GS Global Investment Research

Exhibit 3: Guidance surprises are seeing small price reactions   
SXXP companies. Average price reaction on reporting day (vs. the market). FY1 guidance (vs. consensus one day before the guidance was issued).   
![](images/78f879cbb2d48bd50959b5511071ed6762c19e11824c685f87a528c6d05542b9.jpg)

<details>
<summary>bar</summary>

| Quarter | Median relative price reaction (%) |
| ------- | ---------------------------------- |
| Q1 - 18 | 1.8                                |
| Q3 - 18 | 0.6                                |
| Q1 - 19 | 0.4                                |
| Q3 - 19 | 0.2                                |
| Q1 - 20 | 2.1                                |
| Q3 - 20 | 0.3                                |
| Q1 - 21 | 1.4                                |
| Q3 - 21 | 1.3                                |
| Q1 - 22 | 1.6                                |
| Q3 - 22 | 1.1                                |
| Q1 - 23 | 0.5                                |
| Q3 - 23 | -0.3                               |
| Q1 - 24 | 1.2                                |
| Q3 - 24 | 1.6                                |
| Q1 - 25 | 0.6                                |
| Q3 - 25 | 1.2                                |
| Q1 - 26 | 1.7                                |
</details>

Guidance issued across a selection of 19 relevant items.

Exhibit 2: Market reactions remain asymmetric   
Average price reaction on reporting day vs. the market - STOXX 600 companies   
![](images/8382afd725baea3882114d380b554413932b85d162c7de267801a6d9728b8c4c.jpg)

<details>
<summary>bar</summary>

| Quarter | Average relative price reaction (%) |
| ------- | ----------------------------------- |
| Q1-05   | 0.5                                 |
| Q1-06   | 0.7                                 |
| Q1-07   | 0.9                                 |
| Q1-08   | 1.2                                 |
| Q1-09   | 2.3                                 |
| Q1-10   | 1.5                                 |
| Q1-11   | 1.0                                 |
| Q1-12   | 1.8                                 |
| Q1-13   | 1.6                                 |
| Q1-14   | 1.4                                 |
| Q1-15   | 1.3                                 |
| Q1-16   | 1.2                                 |
| Q1-17   | 1.1                                 |
| Q1-18   | 1.0                                 |
| Q1-19   | 1.5                                 |
| Q1-20   | 2.0                                 |
| Q1-21   | 0.8                                 |
| Q1-22   | 0.6                                 |
| Q1-23   | 0.4                                 |
| Q1-24   | 0.3                                 |
| Q1-25   | 0.2                                 |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 4: Energy and Basic Resources names continue to guide the aggregate upgrades   
2026 EPS revisions. STOXX 600 sectors.   
![](images/5fbc026b6b1778094e8d2228c150c02fc6caaf4d23fb239be8e2caf54d4c1108.jpg)

<details>
<summary>bar</summary>

| Sector | Since 1Q26 season (%) | Since the Iran War (%) |
| :--- | :--- | :--- |
| Energy | +17 | +57 |
| Basic Resources | 2.3 | 4.2 |
| STOXX 600 | 1.8 | 3.4 |
| Tech | 2.5 | 2.8 |
| Chemicals | 3.5 | 2.6 |
| Telecom | 2.0 | 1.9 |
| Utilities | 0.5 | 1.3 |
| Retail | -0.2 | 1.1 |
| Financials | -0.1 | 0.3 |
| STOXX 600 ex Comm. | -0.1 | -0.1 |
| Health Care | -0.1 | -0.3 |
| Consumer Staples | -0.1 | -0.4 |
| Industrials | -0.1 | -0.5 |
| Media | -0.1 | -0.6 |
| Real Estate | -0.1 | -0.7 |
| Luxury* | -0.1 | -3.2 |
| Autos & Parts | -3.2 | -5.8 |
| Travel and Leisure | -0.1 | -14 |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 5: Earnings of capital-intensive and internationally exposed names are being upgraded   
1-month revisions 2026 Earnings - selection of European baskets   
![](images/9381bc866e3eea2579179abdfe90743e71e094ee3f3066b33cba4a22c4fd6489.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
| :--- | :--- |
| Capital Intensive (GSSTCAPI) | 3.1 |
| Dividend growth (GSSTDIVG) | 2.3 |
| Strong Balance Sheet (GSSTSBAL) | 2.1 |
| EM Exposure (GSSTBRIC) | 2.0 |
| International Exposure (GSSTINTL) | 1.9 |
| UK International Exposure (GSSTUKIE) | 1.9 |
| STOXX 600 | 1.2 |
| High Dividend Yield (GSSTDIVY) | 1.2 |
| Buybacks (GSSTREPO) | 1.1 |
| Quality (GSSTQUAL) | 1.1 |
| Fiscal Infrastructure Spending (GSSTFISC) | 1.0 |
| US Exposure (GSSTAMER) | 0.9 |
| High Growth Investment Ratio (GSSTHGIR) | 0.9 |
| China Exposure (GSSTCHNA) | 0.8 |
| Defensives (GSSTDEFS) | 0.7 |
| STOXX 600 ex commodities | 0.4 |
| Domestic Eurozone (GSSTDOME) | 0.2 |
| Cyclicals (GSSTCYCL) | 0.2 |
| UK Domestic Exposure (GSSTUKDE) | -0.7 |
| Capital Light (GSSTCAPL) | -0.7 |
| EU High Labour Cost (GSSTHLAB) | -1.4 |
| Weak Balance Sheet (GSSTWBAL) | -2.5 |
</details>

Source: FactSet, GS Global Investment Research

# Earnings surprises — Equal-weighted

Exhibit 6: Earnings surprises

Equal-weighted

<table><tr><td rowspan="2">Sector</td><td colspan="3">Number of Companies</td><td colspan="3">Surprise &gt;5%</td><td colspan="2">Absolute Surprise</td><td rowspan="2">Average Surprise</td></tr><tr><td>Reported</td><td>Expected</td><td>%</td><td>Positive</td><td>In-Line</td><td>Negative</td><td>Positive</td><td>Negative</td></tr><tr><td>Chemicals</td><td>9</td><td>12</td><td>75.0</td><td>77.8</td><td>11.1</td><td>11.1</td><td>88.9</td><td>11.1</td><td>5.5</td></tr><tr><td>Consumer Products and Services</td><td>8</td><td>12</td><td>66.7</td><td>50.0</td><td>50.0</td><td>0.0</td><td>87.5</td><td>12.5</td><td>9.4</td></tr><tr><td>Financial Services</td><td>8</td><td>14</td><td>57.1</td><td>50.0</td><td>37.5</td><td>12.5</td><td>75.0</td><td>25.0</td><td>1.8</td></tr><tr><td>Insurance</td><td>11</td><td>15</td><td>73.3</td><td>45.5</td><td>27.3</td><td>27.3</td><td>54.5</td><td>45.5</td><td>3.4</td></tr><tr><td>Banks</td><td>41</td><td>50</td><td>82.0</td><td>36.6</td><td>58.5</td><td>4.9</td><td>80.5</td><td>19.5</td><td>5.5</td></tr><tr><td>Basic Resources</td><td>11</td><td>12</td><td>91.7</td><td>36.4</td><td>54.5</td><td>9.1</td><td>54.5</td><td>45.5</td><td>5.6</td></tr><tr><td>Energy</td><td>20</td><td>22</td><td>90.9</td><td>35.0</td><td>40.0</td><td>25.0</td><td>55.0</td><td>45.0</td><td>4.4</td></tr><tr><td>Technology</td><td>15</td><td>24</td><td>62.5</td><td>33.3</td><td>60.0</td><td>6.7</td><td>73.3</td><td>26.7</td><td>2.1</td></tr><tr><td>Retail</td><td>3</td><td>3</td><td>100.0</td><td>33.3</td><td>66.7</td><td>0.0</td><td>66.7</td><td>33.3</td><td>1.1</td></tr><tr><td>Automobiles and Parts</td><td>9</td><td>10</td><td>90.0</td><td>33.3</td><td>22.2</td><td>44.4</td><td>55.6</td><td>44.4</td><td>-2.9</td></tr><tr><td>Food Beverage and Tobacco</td><td>7</td><td>15</td><td>46.7</td><td>28.6</td><td>57.1</td><td>14.3</td><td>57.1</td><td>42.9</td><td>1.6</td></tr><tr><td>Personal Care Drug and Grocery Stores</td><td>8</td><td>10</td><td>80.0</td><td>25.0</td><td>62.5</td><td>12.5</td><td>62.5</td><td>37.5</td><td>2.6</td></tr><tr><td>Health Care</td><td>28</td><td>32</td><td>87.5</td><td>25.0</td><td>57.1</td><td>17.9</td><td>57.1</td><td>42.9</td><td>0.8</td></tr><tr><td>Real Estate</td><td>10</td><td>15</td><td>66.7</td><td>20.0</td><td>30.0</td><td>50.0</td><td>40.0</td><td>60.0</td><td>-5.7</td></tr><tr><td>Construction and Materials</td><td>12</td><td>16</td><td>75.0</td><td>16.7</td><td>50.0</td><td>33.3</td><td>33.3</td><td>66.7</td><td>-4.4</td></tr><tr><td>Travel and Leisure</td><td>7</td><td>9</td><td>77.8</td><td>14.3</td><td>71.4</td><td>14.3</td><td>85.7</td><td>14.3</td><td>4.1</td></tr><tr><td>Utilities</td><td>15</td><td>22</td><td>68.2</td><td>13.3</td><td>86.7</td><td>0.0</td><td>80.0</td><td>20.0</td><td>2.0</td></tr><tr><td>Industrial Goods and Services</td><td>46</td><td>61</td><td>75.4</td><td>10.9</td><td>69.6</td><td>19.6</td><td>52.2</td><td>47.8</td><td>-1.8</td></tr><tr><td>Telecommunications</td><td>16</td><td>19</td><td>84.2</td><td>6.3</td><td>93.8</td><td>0.0</td><td>68.8</td><td>31.3</td><td>1.3</td></tr><tr><td>Media</td><td>1</td><td>2</td><td>50.0</td><td>0.0</td><td>0.0</td><td>100.0</td><td>0.0</td><td>100.0</td><td>-6.6</td></tr><tr><td>SXXP</td><td>285</td><td>375</td><td>76.0</td><td>27.7</td><td>56.5</td><td>15.8</td><td>63.5</td><td>36.5</td><td>1.7</td></tr><tr><td>SXXP ex Financials</td><td>215</td><td>281</td><td>76.5</td><td>24.7</td><td>59.5</td><td>15.8</td><td>61.4</td><td>38.6</td><td>1.3</td></tr></table>

Source: Factset, Bloomberg, GS Global Investment Research

# Earnings surprises — Market cap-weighted

Exhibit 7: Earnings surprises

Market cap-weighted

<table><tr><td rowspan="2">Sector</td><td colspan="3">Weight of Companies</td><td colspan="3">Surprise &gt;5%</td><td colspan="2">Absolute Surprise</td><td rowspan="2">Average Surprise</td></tr><tr><td>Reported</td><td>Expected</td><td>%</td><td>Positive</td><td>In-Line</td><td>Negative</td><td>Positive</td><td>Negative</td></tr><tr><td>Chemicals</td><td>0.5</td><td>1.2</td><td>39.5</td><td>90.4</td><td>5.6</td><td>4.0</td><td>96.0</td><td>4.0</td><td>7.1</td></tr><tr><td>Banks</td><td>9.8</td><td>11.9</td><td>82.7</td><td>56.9</td><td>41.5</td><td>1.6</td><td>80.2</td><td>19.8</td><td>6.0</td></tr><tr><td>Technology</td><td>1.4</td><td>3.0</td><td>46.4</td><td>55.4</td><td>41.5</td><td>3.1</td><td>85.7</td><td>14.3</td><td>3.7</td></tr><tr><td>Consumer Products and Services</td><td>1.9</td><td>2.0</td><td>96.8</td><td>49.9</td><td>50.1</td><td>0.0</td><td>97.4</td><td>2.6</td><td>14.6</td></tr><tr><td>Retail</td><td>0.1</td><td>0.1</td><td>100.0</td><td>49.2</td><td>50.8</td><td>0.0</td><td>70.3</td><td>29.7</td><td>2.2</td></tr><tr><td>Financial Services</td><td>1.6</td><td>5.6</td><td>28.7</td><td>46.4</td><td>49.7</td><td>3.9</td><td>93.8</td><td>6.2</td><td>10.2</td></tr><tr><td>Insurance</td><td>1.1</td><td>1.6</td><td>70.8</td><td>43.0</td><td>41.5</td><td>15.6</td><td>53.5</td><td>46.5</td><td>7.2</td></tr><tr><td>Energy</td><td>5.9</td><td>6.0</td><td>96.8</td><td>39.6</td><td>54.6</td><td>5.8</td><td>88.2</td><td>11.8</td><td>6.9</td></tr><tr><td>Automobiles and Parts</td><td>1.2</td><td>1.3</td><td>95.9</td><td>36.7</td><td>18.8</td><td>44.5</td><td>55.5</td><td>44.5</td><td>-1.3</td></tr><tr><td>Real Estate</td><td>1.6</td><td>3.1</td><td>53.1</td><td>28.0</td><td>64.7</td><td>7.3</td><td>33.5</td><td>66.5</td><td>-1.9</td></tr><tr><td>Construction and Materials</td><td>1.9</td><td>2.6</td><td>73.0</td><td>24.6</td><td>40.2</td><td>35.2</td><td>35.2</td><td>64.8</td><td>-13.4</td></tr><tr><td>Health Care</td><td>7.7</td><td>8.5</td><td>90.6</td><td>16.2</td><td>63.7</td><td>20.2</td><td>49.6</td><td>50.4</td><td>-2.5</td></tr><tr><td>Utilities</td><td>2.6</td><td>3.6</td><td>73.8</td><td>10.2</td><td>89.8</td><td>0.0</td><td>68.1</td><td>31.9</td><td>1.3</td></tr><tr><td>Travel and Leisure</td><td>0.3</td><td>1.1</td><td>30.1</td><td>9.6</td><td>48.9</td><td>41.6</td><td>58.4</td><td>41.6</td><td>-3.3</td></tr><tr><td>Industrial Goods and Services</td><td>6.5</td><td>8.2</td><td>78.8</td><td>9.3</td><td>78.9</td><td>11.8</td><td>68.5</td><td>31.5</td><td>0.7</td></tr><tr><td>Personal Care Drug and Grocery Stores</td><td>1.0</td><td>1.0</td><td>94.4</td><td>8.5</td><td>53.7</td><td>37.8</td><td>34.4</td><td>65.6</td><td>-1.2</td></tr><tr><td>Telecommunications</td><td>1.8</td><td>2.0</td><td>93.9</td><td>8.2</td><td>91.8</td><td>0.0</td><td>48.2</td><td>51.8</td><td>0.7</td></tr><tr><td>Basic Resources</td><td>1.6</td><td>1.6</td><td>95.9</td><td>7.3</td><td>91.3</td><td>1.4</td><td>25.9</td><td>74.1</td><td>0.9</td></tr><tr><td>Food Beverage and Tobacco</td><td>0.9</td><td>3.5</td><td>26.8</td><td>6.0</td><td>40.6</td><td>53.4</td><td>38.6</td><td>61.4</td><td>-1.3</td></tr><tr><td>Media</td><td>0</td><td>0</td><td>86.9</td><td>0.0</td><td>0.0</td><td>100.0</td><td>0.0</td><td>100.0</td><td>-6.6</td></tr><tr><td>SXXP</td><td>50</td><td>68</td><td>73.0</td><td>30.7</td><td>57.8</td><td>11.5</td><td>66.1</td><td>33.9</td><td>2.3</td></tr><tr><td>SXXP ex Financials</td><td>36</td><td>46</td><td>77.3</td><td>22.4</td><td>62.9</td><td>14.6</td><td>62.8</td><td>37.2</td><td>1.0</td></tr></table>

Source: Factset, Bloomberg, GS Global Investment Research

# Sales surprises — Equal-weighted

Exhibit 8: Sales surprises

Equal-weighted

<table><tr><td colspan="11">SALESSTOXX EUROPE 600 - EQUAL WEIGHTED</td></tr><tr><td rowspan="2">Sector</td><td colspan="3">Number of Companies</td><td colspan="3">Surprise &gt;2%</td><td colspan="2">Absolute Surprise</td><td rowspan="2">Average Surprise</td><td>Sales Growth</td></tr><tr><td>Reported</td><td>Expected</td><td>%</td><td>Positive</td><td>In-Line</td><td>Negative</td><td>Positive</td><td>Negative</td><td>2026</td></tr><tr><td>Financial Services</td><td>9</td><td>14</td><td>64.3</td><td>55.6</td><td>22.2</td><td>22.2</td><td>66.7</td><td>33.3</td><td>1.9</td><td>NM</td></tr><tr><td>Energy</td><td>21</td><td>22</td><td>95.5</td><td>38.1</td><td>28.6</td><td>33.3</td><td>61.9</td><td>38.1</td><td>0.8</td><td>11.6</td></tr><tr><td>Retail</td><td>3</td><td>3</td><td>100.0</td><td>33.3</td><td>66.7</td><td>0.0</td><td>33.3</td><td>66.7</td><td>0.7</td><td>5.6</td></tr><tr><td>Consumer Products and Services</td><td>10</td><td>12</td><td>83.3</td><td>30.0</td><td>60.0</td><td>10.0</td><td>80.0</td><td>20.0</td><td>0.9</td><td>NM</td></tr><tr><td>Insurance</td><td>11</td><td>15</td><td>73.3</td><td>27.3</td><td>63.6</td><td>9.1</td><td>81.8</td><td>18.2</td><td>4.1</td><td>NM</td></

[中间内容因长度限制已省略]

me have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
