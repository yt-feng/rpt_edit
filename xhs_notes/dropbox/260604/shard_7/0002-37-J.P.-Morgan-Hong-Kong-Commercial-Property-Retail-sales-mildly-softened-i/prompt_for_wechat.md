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
# Hong Kong Commercial Property

Retail sales mildly softened in April

HK retail sales grew 9% Y/Y in April (Figure 1), mildly moderating from +13% Y/Y in March. Relative to the 2015-18 average, retail sales in April were 15% below, softer than March (9% below). Excluding the exceptionally strong growth in motor vehicles (+46% Y/Y) and electrical goods (+22% Y/Y), overall retail sales would have risen 6% Y/Y in April, mildly slowing down from +8% Y/Y in March (Figure 2). Discretionary (+13% Y/Y, or +8% excluding outliers) continued to outperform staples (+5% Y/Y). Looking ahead, with tourist arrivals not seeing a particularly notable improvement (+9% Y/Y in May vs. +10% Y/Y in April) (Figure 9), we expect retail sales to stay at 5-10% Y/Y growth over the next few months (but the base will get higher in 2H). On stock implications, the stabilizing retail sales have not yet translated into positive (or even stable) rental reversion for the two key HK retail landlord proxies (Wharf REIC & Link REIT). We remain Neutral on both, though we see more upside risk in Link REIT due to its >6% dividend yield and potential capital recycling.

- Staples retail – hovering at mid-single-digit (MSD)% Y/Y growth: Staples rose 5% Y/Y in April (March: +5% Y/Y), and were on par with the 2015-18 average (March: +10%) (Figure 3). This is in line with Link REIT's recent comments on “stabilizing tenant sales” (more in our note “Link REIT: stabilization on the horizon, but valuation appears fair”). Over the next few months, we expect staples to continue to record a MSD% Y/Y growth. However, with the increasing penetration of cross-border e-commerce (particularly from Pinduoduo (拼多多) - Figure 7), we do not expect a material improvement in the near term.   
- Discretionary retail – Y/Y growth moderated for the first time since 2Q25: The Y/Y growth in discretionary retail softened from +22% in March to +13% Y/Y in April (Figure 3). Excluding the exceptionally strong growth in motor vehicles (+46% Y/Y) and electrical goods (+22% Y/Y), discretionary would have risen 8% Y/Y in April (March: +14%). Compared to the 2015-18 average, sales also moderated to -27% (March: -22%). Notably, the Y/Y growth in Jewelry & valuable gifts also mildly moderated from +28% Y/Y in March to +20% Y/Y in April, likely due to lower gold prices.   
- Performance by category (Figure 5): Consumer durable goods (+26% Y/Y in April, driven by motor vehicles & electrical goods) and jewelry & valuable gifts (+20%) outperformed in April and year-to-date (Figure 6). Meanwhile, fuels (-12%) and department stores (-7%) underperformed with a Y/Y decline. Supermarkets (a proxy for Link REIT's tenant sales) mildly grew 3% Y/Y in April, or 2% year-to-date.

# Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC

(852) 2800-8513

karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

Jocelyn Gao

(852) 2800-8529

jocelyn.gao@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

# Hong Kong retail sales performance

Figure 1: Hong Kong monthly retail sales – overall   
![](images/51ed79ecbd625d5a7efd60c7396d3a5e9020054952ae1de8c671b44ee07e3547.jpg)

<details>
<summary>line</summary>

| Month   | Value (HK$mn) | Y/Y   | vs. 2015-18 avg. |
|---------|---------------|-------|------------------|
| 2M24    |               | 1%    | -18%             |
| Mar-24  |               | -7%   | -16%             |
| Apr-24  |               | -15%  | -20%             |
| May-24  |               | -11%  | -19%             |
| Jun-24  |               | -10%  | -16%             |
| Jul-24  |               | -12%  | -21%             |
| Aug-24  |               | -10%  | -19%             |
| Sep-24  |               | -7%   | -16%             |
| Oct-24  |               | -3%   | -13%             |
| Nov-24  |               | -7%   | -17%             |
| Dec-24  |               | -10%  | -25%             |
| 2M25    |               | -8%   | -24%             |
| Mar-25  |               | -3%   | -19%             |
| Apr-25  |               | -2%   | -22%             |
| May-25  |               | 2%    | -17%             |
| Jun-25  |               | 1%    | -15%             |
| Jul-25  |               | 2%    | -19%             |
| Aug-25  |               | 4%    | -16%             |
| Sep-25  |               | 6%    | -11%             |
| Oct-25  |               | 7%    | -7%              |
| Nov-25  |               | 6%    | -11%             |
| Dec-25  |               | 7%    | -20%             |
| 2M26    |               | 12%   | -15%             |
| Mar-26  |               | 13%   | -9%              |
| Apr-26  |               | 9%    | -15%             |
</details>

Source: Hong Kong Census & Statistics Department. Note: We combined Jan & Feb data into 2M data to eliminate the CNY seasonality.

Figure 2: Hong Kong monthly retail sales – overall; excluding electrical goods & motor vehicles   
![](images/5207984a298a0d9497ace64a0ddadefb74b480469834abe9c59f9872a2b56d8d.jpg)

<details>
<summary>bar_line</summary>

| Date | Value (HK$mn) | Y/Y (%) |
|---|---|---|
| 2M24 | 29000 | 6 |
| Mar-24 | 25000 | -7 |
| Apr-24 | 3000 | -17 |
| May-24 | 27000 | -11 |
| Jun-24 | 26000 | -9 |
| Jul-24 | 8000 | -12 |
| Aug-24 | 11000 | -9 |
| Sep-24 | 14000 | -6 |
| Oct-24 | 15000 | -5 |
| Nov-24 | 17000 | -3 |
| Dec-24 | 13000 | -7 |
| 2M25 | 14000 | -6 |
| Mar-25 | 19000 | -1 |
| Apr-25 | 22000 | 2 |
| May-25 | 23000 | 3 |
| Jun-25 | 22000 | 2 |
| Jul-25 | 24000 | 3 |
| Aug-25 | 25000 | 5 |
| Sep-25 | 23000 | 3 |
| Oct-25 | 24000 | 4 |
| Nov-25 | 21000 | 2 |
| Dec-25 | 21000 | 1 |
| 2M26 | 31000 | 9 |
| Mar-26 | 30000 | 8 |
| Apr-26 | 26000 | 6 |
</details>

Source: Hong Kong Census & Statistics Department. Note: We combined Jan & Feb data into 2M data to eliminate the CNY seasonality

Figure 3: Hong Kong monthly retail sales – staples   
![](images/a6dd3202f7a4e853159928ae9f45fb0df809da17e027436f44ef5ebf8a408bbc.jpg)

<details>
<summary>line</summary>

| Month   | Value (HK$mn) | Y/Y   | vs. 2015-18 avg. |
|---------|---------------|-------|------------------|
| 2M24    | 18,000        | 6%    | 0%               |
| Mar-24  | 14,000        | 0%    | 2%               |
| Apr-24  | 4,000         | -9%   | -10%             |
| May-24  | 16,000        | -4%   | -1%              |
| Jun-24  | 10,000        | -2%   | 0%               |
| Jul-24  | 8,000         | -3%   | -4%              |
| Aug-24  | 10,000        | -2%   | -1%              |
| Sep-24  | 10,000        | -1%   | -1%              |
| Oct-24  | 10,000        | -1%   | -2%              |
| Nov-24  | 10,000        | 0%    | -1%              |
| Dec-24  | 8,000         | -3%   | -6%              |
| 2M25    | 18,000        | -2%   | -2%              |
| Mar-25  | 14,000        | 3%    | 5%               |
| Apr-25  | 12,000        | 4%    | -4%              |
| May-25  | 14,000        | 4%    | -4%              |
| Jun-25  | 12,000        | 2%    | 2%               |
| Jul-25  | 12,000        | 3%    | -1%              |
| Aug-25  | 12,000        | 3%    | 2%               |
| Sep-25  | 12,000        | 3%    | 2%               |
| Oct-25  | 12,000        | 3%    | 1%               |
| Nov-25  | 12,000        | 2%    | 1%               |
| Dec-25  | 14,000        | 2%    | -4%              |
| 2M26    | 18,000        | 6%    | -4%              |
| Mar-26  | 16,000        | 5%    | 10%              |
| Apr-26  | 14,000        | 5%    | 0%               |
</details>

Source: Hong Kong Census & Statistics Department.   
Note: Including: (1) food, alcoholic drinks & tobacco; (2) supermarkets; (3) fuel; and (4) other consumer goods (e.g., medicines, optical shops).   
We combined Jan & Feb data into 2M data to eliminate the CNY seasonality.

Figure 4: Hong Kong monthly retail sales – discretionary   
![](images/b56027d5a64ece0e7e0f64c365c4e3f7e259c8a41788ce8e2abc416e4ab11ac1.jpg)

<details>
<summary>line</summary>

| Month   | Value (HK$mn) | Y/Y   | vs. 2015-18 avg. |
|---------|---------------|-------|------------------|
| 2M24    |               | -3%   | -31%             |
| Mar-24  |               | -13%  | -29%             |
| Apr-24  |               | -19%  | -29%             |
| May-24  |               | -18%  | -33%             |
| Jun-24  |               | -17%  | -29%             |
| Jul-24  |               | -20%  | -34%             |
| Aug-24  |               | -18%  | -34%             |
| Sep-24  |               | -13%  | -29%             |
| Oct-24  |               | -4%   | -20%             |
| Nov-24  |               | -13%  | -27%             |
| Dec-24  |               | -15%  | -38%             |
| 2M25    |               | -14%  | -40%             |
| Mar-25  |               | -10%  | -36%             |
| Apr-25  |               | -9%   | -36%             |
| May-25  |               | 0%    | -33%             |
| Jun-25  |               | -1%   | -29%             |
| Jul-25  |               | 0%    | -34%             |
| Aug-25  |               | 5%    | -30%             |
| Sep-25  |               | 9%    | -22%             |
| Oct-25  |               | 10%   | -12%             |
| Nov-25  |               | 11%   | -20%             |
| Dec-25  |               | 11%   | -32%             |
| 2M26    |               | 19%   | -29%             |
| Mar-26  |               | 22%   | -22%             |
| Apr-26  |               | 13%   | -27%             |
</details>

Source: Hong Kong Census & Statistics Department.   
Note: Including: (1) clothing, footwear & allied products; (2) jewelry, watches, clocks & valuable goods; (3) department stores; and (4) consumer durable goods.   
We combined Jan & Feb data into 2M data to eliminate the CNY seasonality.

# Retail sales by category

Figure 5: Retail sales performance by type of retail outlet – April 2026   
![](images/63d10199293e0e09386463276b6c220f34ae5e8274b79c3947d5fd7898ed4403.jpg)

<details>
<summary>bar</summary>

| Category | Y/Y (%) | vs. 2015-18 avg. (%) |
|---|---|---|
| Consumer Durable Goods | 26 | -16 |
| Jewellery, Watches, Clocks & Valuable Gifts | 20 | -25 |
| Other Consumer Goods | 8 | 9 |
| Clothing, Footwear & Allied Products | 5 | -36 |
| Supermarkets | 3 | -3 |
| Food, Alcoholic Drinks & Tobacco | 0 | -13 |
| Department Stores | -7 | -37 |
| Fuels | -12 | -23 |
</details>

Source: Hong Kong Census & Statistics Department.

Figure 6: Retail sales performance by type of retail outlet - 4M26   
![](images/9b73ceeb9b797b752a08f1afa9e5386fe3c217dc6dd929e73d0ed691aff8afc4.jpg)

<details>
<summary>bar</summary>

| Category | Y/Y (%) | vs. 2015-18 avg. (%) |
|---|---|---|
| Consumer Durable Goods | 32 | -23 |
| Jewellery, Watches, Clocks & Valuable Gifts | 26 | -24 |
| Other Consumer Goods | 10 | 16 |
| Clothing, Footwear & Allied Products | 6 | -29 |
| Supermarkets | 2 | -3 |
| Food, Alcoholic Drinks & Tobacco | 2 | -9 |
| Department Stores | 1 | -38 |
| Fuels | -14 | -17 |
</details>

Source: Hong Kong Census & Statistics Department.

# Cross-border e-commerce penetration in Hong Kong

Figure 7: Pinduoduo (拼多多) - Monthly active users (MAU) in Hong Kong   
Pinduoduo MAU   
![](images/a13bb03f72aca47b0f300739d7d6ef78612925f1344b738915f300c3b73da53e.jpg)

<details>
<summary>line</summary>

| Date    | Value     |
|---------|-----------|
| Apr-18  | ~50,000   |
| Aug-18  | ~70,000   |
| Dec-18  | ~90,000   |
| Apr-19  | ~110,000  |
| Aug-19  | ~130,000  |
| Dec-19  | ~150,000  |
| Apr-20  | ~170,000  |
| Aug-20  | ~190,000  |
| Dec-20  | ~210,000  |
| Apr-21  | ~230,000  |
| Aug-21  | ~250,000  |
| Dec-21  | ~270,000  |
| Apr-22  | ~300,000  |
| Aug-22  | ~350,000  |
| Dec-22  | ~400,000  |
| Apr-23  | ~350,000  |
| Aug-23  | ~450,000  |
| Dec-23  | ~550,000  |
| Apr-24  | ~650,000  |
| Aug-24  | ~750,000  |
| Dec-24  | ~950,000  |
| Apr-25  | ~1,550,000|
| Aug-25  | ~1,650,000|
| Dec-25  | ~1,950,000|
| Apr-26  | ~2,150,000|
</details>

Source: Sensor Tower

Figure 8: Major non-local e-commerce players – monthly active users (MAU) in Hong Kong   
MAU   
![](images/2cadde935bbefc1f87afcab242665db35f104ab6592634ef0fc658c7b8c02d59.jpg)  
Source: Sensor Tower. Note: Major local e-commerce platforms (e.g. HKTV Mall) are not included here.

# Hong Kong Tourist Arrivals

Figure 9: Hong Kong monthly tourist arrivals   
![](images/1384d34cb42e15d8b6b6ab5da9ac1a87f135d20f2ba1f968874b67232afb313b.jpg)

<details>
<summary>bar_line</summary>

| Month | Total tourist arrivals | vs. 2018 (%) | Y/Y (%) |
|---|---|---|---|
| Jan-24 | 3,850,000 | -28 | -28 |
| Feb-24 | 4,000,000 | -24 | -24 |
| Mar-24 | 3,400,000 | -32 | 39 |
| Apr-24 | 3,400,000 | -36 | -17 |
| May-24 | 3,400,000 | -31 | -20 |
| Jun-24 | 3,100,000 | -34 | -14 |
| Jul-24 | 3,500,000 | -28 | -9 |
| Aug-24 | 4,400,000 | -24 | -9 |
| Sep-24 | 3,050,000 | -35 | -10 |
| Oct-24 | 3,950,000 | -30 | -18 |
| Nov-24 | 3,550,000 | -40 | -8 |
| Dec-24 | 3,650,000 | -35 | -8 |
| Jan-25 | 4,650,000 | -11 | 24 |
| Feb-25 | 3,650,000 | -31 | -8 |
| Mar-25 | 3,850,000 | -24 | 12 |
| Apr-25 | 3,950,000 | -27 | 13 |
| May-25 | 3,950,000 | -18 | 20 |
| Jun-25 | 3,450,000 | -27 | 11 |
| Jul-25 | 3,950,000 | -20 | 12 |
| Aug-25 | 5,150,000 | -13 | 16 |
| Sep-25 | 3,350,000 | -30 | -8 |
| Oct-25 | 3,750,000 | -22 | 12 |
| Nov-25 | 3,950,000 | -30 | 17 |
| Dec-25 | 4,650,000 | -29 | -9 |
| Jan-26 | 4,750,000 | -10 | 1 |
| Feb-26 | 5,350,000 | -3 | 40 |
| Mar-26 | 3,850,000 | -13 | -14 |
| Apr-26 | 3,650,000 | -20 | -10 |
| May-26 | 4,450,000 | -10 | -9 |
</details>

Source: Hong Kong Census & Statistics Department, CEIC.

# Valuation Summary

Table 1: Hong Kong Property & Conglomerates – Valuation Summary 

<table><tr><td rowspan="2">Company</td><td rowspan="2">Stock Code</td><td rowspan="2">JPM Rating</td><td rowspan="2">Last Close (HK$)</td><td rowspan="2" colspan="3">Market Cap US$M</td><td colspan="2">P/E</td><td colspan="2">Dvd Yield</td><td colspan="2">P/B</td><td colspan="4">Share Price Return</td><td></td></tr><tr><td>1FY (x)</td><td>2FY (x)</td><td>1FY (%)</td><td>2FY (%)</td><td>1FY (x)</td><td>2FY (x)</td><td>5D</td><td>YTD</td><td>1Y</td><td>Peak</td><td></td></tr><tr><td colspan="17">Hong Kong Property</td><td></td></tr><tr><td>Sun Hung Kai Properties</td><td>0016.HK</td><td>OW</td><td>127.90</td><td colspan="2">47,285</td><td>101.7</td><td>-39%</td><td>16.2</td><td>15.2</td><td>3.1%</td><td>3.3%</td><td>0.6</td><td>0.6</td><td>-5%</td><td>36%</td><td>60%</td><td>-14%</td></tr><tr><td>CK Asset</td><td>1113.HK</td><td>OW</td><td>47.80</td><td colspan="2">21,343</td><td>38.7</td><td>-48%</td><td>14.9</td><td>14.8</td><td>3.5%</td><td>3.5%</td><td>0.4</td><td>0.4</td><td>-1%</td><td>25%</td><td>53%</td><td>-8%</td></tr><tr><td>Henderson Land</td><td>0012.HK</td><td>N</td><td>30.60</td><td colspan="2">18,901</td><td>41.0</td><td>-50%</td><td>19.1</td><td>16.1</td><td>4.1%</td><td>4.1%</td><td>0.4</td><td>0.4</td><td>-3%</td><td>9%</td><td>35%</td><td>-14%</td></tr><tr><td>Sino Land</td><td>0083.HK</td><td>OW</td><td>11.81</td><td colspan="2">14,444</td><td>13.9</td><td>-35%</td><td>23.1</td><td>24.8</td><td>4.9%</td><td>4.9%</td><td>0.6</td><td>0.6</td><td>-1%</td><td>17%</td><td>57%</td><td>-11%</td></tr><tr><td>New World Development</td><td>0017.HK</td><td>N</td><td>8.02</td><td colspan="2">2,575</td><td>8.3</td><td>-59%</td><td>-12.1</td><td>-9.4</td><td>0.0%</td><td>0.0%</td><td>0.1</td><td>0.1</td><td>-6%</td><td>10%</td><td>79%</td><td>-86%</td></tr><tr><td>Wharf Holdings</td><td>0004.HK</td><td>NC</td><td>23.62</td><td colspan="2">9,209</td><td>13.7</td><td>-</td><td>15.6</td><td>15.1</td><td>1.8%</td><td>1.8%</td><td>0.5</td><td>0.5</td><td>1%</td><td>10%</td><td>13%</td><td>-23%</td></tr><tr><td>Kerry Properties</td><td>0683.HK</td><td>NC</td><td>20.66</td><td colspan="2">3,825</td><td>5.7</td><td>-</td><td>14.7</td><td>7.1</td><td>6.5%</td><td>6.5%</td><td>0.3</td><td>0.3</td><td>-5%</td><td>6%</td><td>18%</td><td>-17%</td></tr><tr><td colspan="6">Developers</td><td>57.7</td><td>-38%</td><td>16.6</td><td>15.6</td><td>3.5%</td><td>3.6%</td><td>0.5</td><td>0.5</td><td>-3%</td><td>24%</td><td>50%</td><td>-15%</td></tr><tr><td>Swire Properties</td><td>1972.HK</td><td>OW</td><td>22.68</td><td colspan="2">16,660</td><td>10.7</td><td>-51%</td><td>16.2</td><td>14.6</td><td>5.3%</td><td>5.6%</td><td>0.5</td><td>0.5</td><td>-2%</td><td>12%</td><td>38%</td><td>-14%</td></tr><tr><td>Wharf REIC</td><td>1997.HK</td><td>N</td><td>24.10</td><td colspan="2">9,336</td><td>16.3</td><td>-56%</td><td>11.6</td><td>11.6</td><td>5.4%</td><td>5.3%</td><td>0.4</td><td>0.4</td><td>-1%</td><td>1%</td><td>31%</td><td>-47%</td></tr><tr><td>HK Land (in US$)</td><td>HKLD.SI</td><td>OW</td><td>7.54</td><td colspan="2">16,186</td><td>24.9</td><td>-44%</td><td>35.2</td><td>33.2</td><td>3.5%</td><td>3.7%</td><td>0.5</td><td>0.5</td><td>-6%</td><td>11%</td><td>47%</td><td>-15%</td></tr><tr><td>Hang Lung Properties</td><td>0101.HK</td><td>OW</td><td>8.00</td><td colspan="2">5,161</td><td>11.3</td><td>-71%</td><td>12.7</td><td>11.9</td><td>6.5%</td><td>6.5%</td><td>0.3</td><td>0.3</td><td>-2%</td><td>-3%</td><td>37%</td><td>-60%</td></tr><tr><td>Hysan</td><td>0014.HK</td><td>NC</td><td>18.20</td><td colspan="2">2,385</td><td>6.0</td><td>-</td><td>8.9</td><td>10.6</td><td>5.9%</td><td>6.0%</td><td>0.3</td><td>0.3</td><td>-3%</td><td>0%</td><td>51%</td><td>-37%</td></tr><tr><td colspan="6">Landlords</td><td>16.2</td><td>-49%</td><td>20.8</td><td>19.6</td><td>4.9%</td><td>5.0%</td><td>0.5</td><td>0.5</td><td>-3%</td><td>7%</td><td>40%</td><td>-26%</td></tr><tr><td>Link REIT</td><td>0823.HK</td><td>N</td><td>39.22</td><td colspan="2">12,922</td><td>55.4</td><td>-</td><td>15.6</td><td>15.6</td><td>6.2%</td><td>6.3%</td><td>0.6</td><td>0.6</td><td>-3%</td><td>13%</td><td>2%</td><td>-42%</td></tr><tr><td>Fortune REIT</td><td>778.HK</td><td>NC</td><td>4.82</td><td colspan="2">1,265</td><td>2.0</td><td>-</td><td>16.6</td><td>16.6</td><td>7.1%</td><td>7.1%</td><td>0.4</td><td>0.4</td><td>1%</td><td>2%</td><td>16%</td><td>-30%</td></tr><tr><td>Champion REIT</td><td>2778.HK</td><td>NC</td><td>2.43</td><td colspan="2">1,902</td><td>0.5</td><td>-</td><td>19.8</td><td>19.8</td><td>5.8%</td><td>6.0%</td><td>0.4</td><td>0.4</td><td>3%</td><td>-2%</td><td>31%</td><td>-45%</td></tr><tr><td colspan="6">REITs</td><td>44.7</td><td>-</td><td>16.2</td><td>16.2</td><td>6.2%</td><td>6.4%</td><td>0.6</td><td>0.6</td><td>-2%</td><td>10%</td><td>6%</td><td>-41%</td></tr><tr><td colspan="6">Hong Kong Property (Overall)</td><td>45.3</td><td>-38%</td><td>17.7</td><td>16.8</td><td>4.1%</td><td>4.2%</td><td>0.5</td><td>0.5</td><td>-3%</td><td>18%</td><td>43%</td><td>-20%</td></tr>

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 02 Jun 2026 11:36 PM HKT

Disseminated 03 Jun 2026 04:00 AM HKT
"""
